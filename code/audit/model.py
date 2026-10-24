from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import csv
import json
import re
import unicodedata


def timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)


def normalize(value: Any) -> str:
    return unicodedata.normalize('NFKC', str(value or '')).strip().casefold()


EMAIL = re.compile(r'[\w.+\-]+@[\w.\-]+\.[a-zA-Z]{2,}', re.UNICODE)
IDENTIFIER = re.compile(r'\b(?:user|account|analytics|search|support|data_flow|backup|export|tombstone|audit_record|email_delivery|marketing|object|cache)_\d+\b')
HASH = re.compile(r'\b[a-fA-F0-9]{64}\b')
PII_FIELDS = {'email', 'phone', 'email_hash', 'name', 'full_name', 'display_name',
              'requester_email', 'requester_name', 'requester_phone', 'owner_email',
              'owner_phone', 'customer_email', 'matched_value'}
SUBJECT_FIELDS = {'user_id', 'subject_reference', 'customer_reference'}


def tokens(value: Any) -> set[str]:
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    return {normalize(x) for pattern in (EMAIL, IDENTIFIER, HASH) for x in pattern.findall(text)}


def read_csv(path):
    with open(path, encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


@dataclass
class Fact:
    system: str
    resource: str
    category: str
    state: str
    observed: str
    available: str
    evidence: str
    payload: dict = field(default_factory=dict)
    links: set[str] = field(default_factory=set)
    topology: str = 'primary'
    quality: int = 3
    location: str = ''

    def admissible(self, cutoff):
        return self.observed <= cutoff and self.available <= cutoff


@dataclass
class Scope:
    system: str
    category: str
    observed: str
    available: str
    evidence: str
    resources: set[str]
    topology: str = 'primary'
    # A snapshot can be scoped to a subject cohort rather than the whole company.
    links: set[str] = field(default_factory=set)


CATEGORIES = {
    'account_service': 'USER_PROFILE', 'search_service': 'SEARCH_INDEX_ENTRY',
    'analytics_platform': 'ANALYTICS_PROFILE', 'integration_service': 'DATA_FLOW',
    'backup_service': 'BACKUP_ARCHIVE', 'security_service': 'SECURITY_AUDIT_LOG',
    'identity_service': 'ACCOUNT_TOMBSTONE', 'export_service': 'USER_EXPORT',
    'support_platform': 'SUPPORT_MESSAGE', 'support_replica': 'SUPPORT_MESSAGE',
    'object_storage': 'SUPPORT_ATTACHMENT', 'marketing_platform': 'MARKETING_PROFILE',
    'notification_service': 'EMAIL_DELIVERY_LOG', 'legal_service': 'LEGAL_HOLD_RECORD',
}


def category_for(system: str, collection: str = '', payload: dict | None = None):
    text = collection.lower()
    payload = payload or {}
    if payload.get('record_type'):
        return payload['record_type']
    for needle, category in [('attachment', 'SUPPORT_ATTACHMENT'), ('tombstone', 'ACCOUNT_TOMBSTONE'),
                             ('deleted_customer', 'ACCOUNT_TOMBSTONE'), ('telemetry', 'PRODUCT_TELEMETRY'),
                             ('legal', 'LEGAL_HOLD_RECORD'), ('delivery', 'EMAIL_DELIVERY_LOG'),
                             ('secondary', 'SECONDARY_IDENTIFIER'), ('cache', 'CACHE_ENTRY')]:
        if needle in text:
            return category
    return CATEGORIES.get(system, 'USER_PROFILE')


def present_value(value):
    return normalize(value) not in {'', 'null', 'none', '[redacted]', 'redacted', 'anonymous', 'anonymized', '—', '-'}


def exposed(payload: dict, anonymize=False):
    for key, value in payload.items():
        if key in PII_FIELDS and present_value(value):
            return True
        if anonymize and key in SUBJECT_FIELDS and present_value(value):
            return True
        if isinstance(value, dict) and exposed(value, anonymize):
            return True
        if key in {'message_text', 'message_excerpt', 'document_text'} and EMAIL.search(str(value)):
            return True
    return False


def state_for(category: str, payload: dict):
    result = str(payload.get('result', '')).upper()
    states = {'NOT_FOUND': 'ABSENT', 'FOUND': 'PRESENT', 'IDENTIFIABLE': 'IDENTIFIABLE',
              'REDACTED': 'REDACTED', 'ANONYMIZED': 'ANONYMIZED', 'ACTIVE': 'ACTIVE',
              'DISABLED': 'DISABLED', 'BLOCKED': 'BLOCKED', 'ABSENT': 'ABSENT',
              'PRESENT': 'PRESENT'}
    if result in states:
        return states[result]
    if category == 'DATA_FLOW':
        return 'ACTIVE' if str(payload.get('enabled', True)).lower() in {'true', '1'} else 'DISABLED'
    if category == 'BACKUP_ARCHIVE':
        if payload.get('decision') == 'deny':
            return 'BLOCKED'
        allowed = payload.get('restore_allowed', payload.get('eligible', True))
        blocked = str(payload.get('deletion_block', False)).lower() == 'true'
        return 'ACTIVE' if str(allowed).lower() in {'true', '1'} and not blocked else 'BLOCKED'
    if category in {'ANALYTICS_PROFILE', 'PRODUCT_TELEMETRY'}:
        if 'direct_identifiers' in payload:
            return 'IDENTIFIABLE' if int(payload['direct_identifiers']) else 'ANONYMIZED'
        return 'IDENTIFIABLE' if exposed(payload, True) else 'ANONYMIZED'
    if category in {'SUPPORT_MESSAGE', 'EMAIL_DELIVERY_LOG', 'ACCOUNT_TOMBSTONE'}:
        return 'IDENTIFIABLE' if exposed(payload) else 'REDACTED'
    return 'PRESENT'


OP_STATE = {
    'REPORT_REMAINING_RECORD': ('FINDING', 'PRESENT'),
    'REPORT_EXPOSED_PII': ('FINDING', 'PRESENT'),
    'REPORT_ACTIVE_DATA_FLOW': ('FINDING', 'ACTIVE'),
    'REPORT_RESTORE_RISK': ('FINDING', 'ACTIVE'),
    'DISABLE_DATA_FLOW': ('REMEDIATION', 'DISABLED'),
    'BLOCK_RESTORE': ('REMEDIATION', 'BLOCKED'),
    'DELETE_RECORD': ('REMEDIATION', 'ABSENT'),
    'REDACT_RECORD': ('REMEDIATION', 'REDACTED'),
    'ANONYMIZE_RECORD': ('REMEDIATION', 'ANONYMIZED'),
    'VERIFY_RECORD_ABSENT': ('VERIFICATION', 'ABSENT'),
    'VERIFY_RECORD_PRESENT': ('VERIFICATION', 'PRESENT'),
    'VERIFY_RECORD_REDACTED': ('VERIFICATION', 'REDACTED'),
    'VERIFY_RECORD_ANONYMIZED': ('VERIFICATION', 'ANONYMIZED'),
    'VERIFY_DATA_FLOW_DISABLED': ('VERIFICATION', 'DISABLED'),
    'VERIFY_RESTORE_BLOCKED': ('VERIFICATION', 'BLOCKED'),
}
OP_ORDER = {name: index for index, name in enumerate(OP_STATE)}


def ordered_steps(items):
    unique = {(x['operation'], x['system_id'], x['resource_id']): x for x in items}
    result = sorted(unique.values(), key=lambda x: (OP_ORDER[x['operation']], x['system_id'], x['resource_id']))
    for index, step in enumerate(result, 1):
        step['step_no'] = index
    return result


def make_step(fact, operation, evidence=''):
    phase, state = OP_STATE[operation]
    return dict(step_no=0, phase=phase, system_id=fact.system, resource_id=fact.resource,
                operation=operation, state=state, evidence_id=evidence)


def validate_output(rows, requests, evidence_ids):
    expected = sorted(x['case_id'] for x in requests)
    assert [x['case_id'] for x in rows] == expected, 'Request coverage/order differs'
    assert len(set(expected)) == len(expected), 'Duplicate requests'
    keys = {'step_no', 'phase', 'system_id', 'resource_id', 'operation', 'state', 'evidence_id'}
    for row in rows:
        status = row['deletion_status']
        assert status in {'COMPLETE', 'INCOMPLETE', 'NOT_APPLICABLE'}
        steps = json.loads(row['steps_json']) if isinstance(row['steps_json'], str) else row['steps_json']
        assert isinstance(steps, list)
        if status == 'NOT_APPLICABLE':
            assert steps == []
        else:
            assert steps, f"No proof for {row['case_id']}"
        assert steps == ordered_steps([dict(x) for x in steps]), 'Invalid order or duplicate steps'
        for index, step in enumerate(steps, 1):
            assert set(step) == keys and step['step_no'] == index
            assert (step['phase'], step['state']) == OP_STATE[step['operation']]
            assert step['resource_id'] and step['system_id']
            needs_evidence = status == 'COMPLETE' or step['phase'] == 'FINDING'
            assert bool(step['evidence_id']) == needs_evidence
            assert not step['evidence_id'] or step['evidence_id'] in evidence_ids
            if status == 'COMPLETE':
                assert step['phase'] == 'VERIFICATION'
        if status == 'INCOMPLETE':
            assert any(x['phase'] == 'FINDING' for x in steps)


def write_output(path, rows):
    with open(path, 'w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['case_id', 'deletion_status', 'steps_json'], lineterminator='\n')
        writer.writeheader()
        for row in rows:
            writer.writerow({**row, 'steps_json': json.dumps(row['steps_json'], ensure_ascii=False, separators=(',', ':'))})
