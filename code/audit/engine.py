"""Temporal identity resolution, policy application, and deterministic planning."""
from collections import defaultdict
from dataclasses import replace
import re
from .model import (Fact, tokens, normalize, read_csv, make_step, ordered_steps, timestamp,
                    state_for, category_for)


def deletion_intent(text):
    """Conservative offline fallback; normal submission runs use model classification."""
    text = normalize(text)
    deny = [r'not asking for deletion', r'not a request to erase', r'do not close',
            r"don.t delete", r'without removing', r'keep the account as it is',
            r'leave .* (?:in place|active)', r'marketing lists only',
            r'continue using the service', r'need help resetting', r'correct .* surname']
    if any(re.search(pattern, text) for pattern in deny):
        return False
    return bool(re.search(r'delet|eras|remov|clos|suppr|elimin|exclus|削除|privacy|profile is gone|personal details', text))


class AuditEngine:
    def __init__(self, dataset, reader):
        self.reader = reader
        self.identities = read_csv(dataset / 'user_identities.csv')
        self.audit_log = read_csv(dataset / 'user_audit_log.csv')
        self.rules = {x['data_category']: x for x in read_csv(dataset / 'deletion_rules.csv')}
        self.aliases = defaultdict(set)
        self.warnings = []
        self.explanations = {}
        self.request_metadata = []
        for filename in ('deletion_requests.csv', 'sample_deletion_requests.csv'):
            path = dataset / filename
            if path.exists():
                self.request_metadata.extend(read_csv(path))
        for row in self.identities:
            for token in tokens(row):
                self.aliases[token].add(row['user_id'])
        all_aliases = self.identity_index('9999')
        metadata_times = []
        for metadata in self.request_metadata:
            who = all_aliases.get(normalize(metadata['email']), set())
            if len(who) == 1 and deletion_intent(metadata['request_text']):
                metadata_times.append((timestamp(metadata['reported_at']), metadata['requested_at'],
                                       metadata['audit_at'], next(iter(who))))
        self.temporal_assignments = {}
        for event in self.reader.activities:
            if event['source_system'] != 'deletion_worker' or event['event_type'] not in {'DELETE_RECORD', 'ANONYMIZE_RECORD', 'REDACT_RECORD'}:
                continue
            event_at = timestamp(event['event_time'])
            candidates = sorted(set((abs((reported-event_at).total_seconds()), who)
                                    for reported, requested, audited, who in metadata_times
                                    if requested <= event['event_time'] <= audited
                                    and abs((reported-event_at).total_seconds()) <= 600))
            if candidates and (len(candidates) == 1 or candidates[1][0]-candidates[0][0] >= 1200):
                self.temporal_assignments[event['resource_id']] = (candidates[0][1], event['event_time'],
                                                                  event['activity_id'], candidates[0][0])

    def identity_index(self, cutoff):
        aliases = defaultdict(set, {k: set(v) for k, v in self.aliases.items()})
        for event in self.audit_log:
            if event['event_time'] <= cutoff:
                for value in (event['old_value'], event['new_value']):
                    if value:
                        aliases[normalize(value)].add(event['user_id'])
        return aliases

    def resolve(self, request):
        cutoff = request['audit_at']
        aliases = self.identity_index(cutoff)
        subjects = aliases.get(normalize(request['email']), set())
        if len(subjects) != 1:
            raise ValueError(f"{request['case_id']}: request identity is not uniquely resolved")
        subject = next(iter(subjects))
        members = defaultdict(set)
        explicit = defaultdict(set)
        admissible = [f for f in self.reader.facts if f.admissible(cutoff)]
        sources = {x['file_id']: x['captured_at'] for x in self.reader.manifest}
        for row in self.reader.activities:
            if row['event_type'] == 'LINK_RESOURCE_IDENTITY' and row['event_time'] <= cutoff:
                for token in tokens(row['details']):
                    explicit[row['resource_id']] |= aliases.get(token, set())
        for fact in admissible:
            for token in fact.links:
                members[fact.resource] |= aliases.get(token, set())
        valid_links = []
        for resource, links, observed, evidence in self.reader.links:
            if observed <= cutoff:
                valid_links.append((resource, links))
                for token in links:
                    members[resource] |= aliases.get(token, set())
        # Trace/catalog/resource references can establish provenance after PII is removed.
        for _ in range(5):
            changed = False
            for resource, links in valid_links:
                before = len(members[resource])
                for link in links:
                    if link != resource:
                        members[resource] |= members.get(link, set())
                changed |= before != len(members[resource])
            if not changed:
                break
        for resource, assigned in explicit.items():
            if assigned:
                members[resource] = assigned
        # De-identified readbacks can lose their ownership fields. Correlate an
        # otherwise unlinked worker resource with a uniquely nearby report time.
        # This is probabilistic linkage, not proof of the worker's claimed result.
        # Require a separation margin; never use request IDs or expected labels.
        temporal_links = []
        for resource, (assigned, observed, evidence, delta) in self.temporal_assignments.items():
            if not members[resource] and observed <= cutoff:
                members[resource] = {assigned}
                if assigned == subject:
                    temporal_links.append(dict(resource=resource, evidence=evidence, seconds_from_report=delta))
        relevant = [f for f in admissible if subject in members[f.resource]]
        # Materialize scoped negative queries only for a cohort known to contain this user.
        for scope in self.reader.scopes:
            if scope.available > cutoff or scope.observed > cutoff:
                continue
            cohort = set()
            for token in scope.links:
                cohort |= aliases.get(token, set())
            if subject not in cohort and '*' not in scope.links:
                continue
            for resource, assigned in list(members.items()):
                if subject not in assigned or resource in scope.resources:
                    continue
                known = [f for f in admissible if f.resource == resource and f.system == scope.system
                         and f.category == scope.category]
                if not known:
                    linked_operations = [a for a in self.reader.activities if a['resource_id'] == resource
                                         and a['target_system'] == scope.system and a['event_time'] <= scope.observed]
                    if not linked_operations or '*' not in scope.links:
                        continue
                relevant.append(Fact(scope.system, resource, scope.category, 'ABSENT', scope.observed,
                                     scope.available, scope.evidence, {}, {subject}, scope.topology, 4, 'scoped absence'))
        if temporal_links:
            self.warnings.append(dict(case_id=request['case_id'], inferred_temporal_links=temporal_links))
        return subject, relevant, members

    def current(self, facts):
        latest = {}
        for fact in facts:
            key = (fact.system, fact.resource, fact.topology)
            prior = latest.get(key)
            rank = (fact.observed, fact.quality, fact.available, fact.evidence)
            if prior is None or rank > (prior.observed, prior.quality, prior.available, prior.evidence):
                latest[key] = fact
        grouped = defaultdict(list)
        for fact in latest.values():
            grouped[(fact.system, fact.resource)].append(fact)
        result = []
        for key, copies in grouped.items():
            # A positive replica at the same snapshot defeats primary-only absence.
            newest = max(f.observed for f in copies)
            contemporary = [f for f in copies if f.observed == newest]
            noncompliant = [f for f in copies if self.violation(f)]
            selected = max(noncompliant or contemporary,
                           key=lambda f: (f.observed, f.quality, f.available, f.evidence))
            # Keep the reconstructed latest state, then choose the strongest
            # compatible direct proof, rather than a less specific export claim.
            consistent = [f for f in facts if f.system == selected.system and f.resource == selected.resource
                          and f.state == selected.state and f.observed <= selected.observed
                          and not any(other.system == f.system and other.resource == f.resource
                                      and f.observed < other.observed <= selected.observed
                                      and other.state != selected.state for other in facts)]
            if consistent:
                selected = max(consistent, key=lambda f: (f.quality, f.observed, f.available, f.evidence))
            result.append(selected)
        return result

    def treatment(self, fact):
        if fact.category == 'DATA_FLOW':
            return 'DISABLE'
        if fact.category not in self.rules:
            raise ValueError(f'No supplied policy for {fact.category}')
        return self.rules[fact.category]['required_action']

    def violation(self, fact):
        action = self.treatment(fact)
        if fact.category == 'BACKUP_ARCHIVE':
            return fact.state == 'ACTIVE'
        if action == 'DISABLE':
            return fact.state == 'ACTIVE'
        if action == 'DELETE':
            return fact.state != 'ABSENT'
        if action == 'REDACT':
            return fact.state not in {'REDACTED', 'ABSENT'}
        if action == 'ANONYMIZE':
            return fact.state not in {'ANONYMIZED', 'ABSENT'}
        if action == 'RETAIN':
            return fact.state == 'ABSENT'
        raise ValueError(f'Unknown policy action {action}')

    def plan(self, facts):
        violations = [f for f in facts if self.violation(f)]
        incomplete = bool(violations)
        steps = []
        for fact in facts:
            action = self.treatment(fact)
            bad = self.violation(fact)
            if fact.category == 'DATA_FLOW':
                finding, remediation, verification = 'REPORT_ACTIVE_DATA_FLOW', 'DISABLE_DATA_FLOW', 'VERIFY_DATA_FLOW_DISABLED'
            elif fact.category == 'BACKUP_ARCHIVE':
                finding, remediation, verification = 'REPORT_RESTORE_RISK', 'BLOCK_RESTORE', 'VERIFY_RESTORE_BLOCKED'
            elif action == 'DELETE':
                finding, remediation, verification = 'REPORT_REMAINING_RECORD', 'DELETE_RECORD', 'VERIFY_RECORD_ABSENT'
            elif action == 'REDACT':
                finding, remediation, verification = 'REPORT_EXPOSED_PII', 'REDACT_RECORD', 'VERIFY_RECORD_REDACTED'
            elif action == 'ANONYMIZE':
                finding, remediation, verification = 'REPORT_EXPOSED_PII', 'ANONYMIZE_RECORD', 'VERIFY_RECORD_ANONYMIZED'
            else:
                finding, remediation, verification = None, None, 'VERIFY_RECORD_PRESENT'
            if bad:
                if finding is None:
                    raise ValueError(f'Missing policy-required retained record has no allowed repair operation: {fact.resource}')
                steps.append(make_step(fact, finding, fact.evidence))
                steps.append(make_step(fact, remediation))
            steps.append(make_step(fact, verification, '' if incomplete else fact.evidence))
        return ('INCOMPLETE' if incomplete else 'COMPLETE'), ordered_steps(steps)

    def audit(self, request, authorized=None):
        if authorized is None:
            authorized = deletion_intent(request['request_text'])
        if not authorized:
            return dict(case_id=request['case_id'], deletion_status='NOT_APPLICABLE', steps_json=[])
        subject, facts, members = self.resolve(request)
        selected = self.current(facts)
        if not selected:
            raise ValueError(f"{request['case_id']}: no admissible subject-linked observations; cannot invent a verdict")
        status, steps = self.plan(selected)
        self.explanations[request['case_id']] = dict(subject=subject, facts=[dict(
            system=f.system, resource=f.resource, category=f.category, state=f.state,
            evidence=f.evidence, observed=f.observed, available=f.available, topology=f.topology,
            location=f.location) for f in selected])
        return dict(case_id=request['case_id'], deletion_status=status, steps_json=steps)
