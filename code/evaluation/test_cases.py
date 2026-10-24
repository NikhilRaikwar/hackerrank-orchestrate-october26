"""Synthetic behavioral tests independent of public sample IDs and labels.

Run: python -m unittest discover -s code/evaluation -p test_cases.py -v
"""
import csv
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit.engine import AuditEngine, deletion_intent
from audit.model import Fact, Scope, ordered_steps, tokens, validate_output

TIME = '2026-04-10T12:00:00Z'
BEFORE = '2026-04-09T12:00:00Z'
AFTER = '2026-04-11T12:00:00Z'


class AuditBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.csv('user_identities.csv', ['user_id', 'email', 'name', 'phone', 'email_hash', 'updated_at'],
                 [['user_90001', 'person@example.test', 'Example Person', '+44 12345', 'a'*64, BEFORE],
                  ['user_90002', 'person.jr@example.test', 'Other Person', '', 'b'*64, BEFORE]])
        self.csv('user_audit_log.csv', ['audit_id', 'user_id', 'event_time', 'field_name', 'old_value', 'new_value'],
                 [['audit_custom', 'user_90001', BEFORE, 'email', 'old@example.test', 'person@example.test']])
        self.csv('deletion_rules.csv', ['rule_id', 'data_category', 'condition', 'required_action'],
                 [['custom_'+str(i), category, 'Always', action] for i,(category,action) in enumerate([
                     ('USER_PROFILE','DELETE'), ('ANALYTICS_PROFILE','ANONYMIZE'),
                     ('SUPPORT_MESSAGE','REDACT'), ('ACCOUNT_TOMBSTONE','REDACT'),
                     ('SECURITY_AUDIT_LOG','RETAIN'), ('BACKUP_ARCHIVE','RETAIN')])])
        self.request = dict(case_id='custom_case', email='person@example.test', requested_at=BEFORE,
                            reported_at=TIME, reported_status='COMPLETE', audit_at=TIME,
                            request_text='Please erase my account and associated personal information.')

    def tearDown(self):
        self.temp.cleanup()

    def csv(self, name, fields, rows):
        with (self.root/name).open('w', encoding='utf-8', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(fields)
            writer.writerows(rows)

    def fact(self, resource, category, state, system='account_service', **kwargs):
        return Fact(system, resource, category, state, BEFORE, BEFORE, 'custom_evidence',
                    {}, {'user_90001'}, **kwargs)

    def engine(self, facts, scopes=None):
        reader = SimpleNamespace(facts=facts, scopes=scopes or [], activities=[], links=[],
                                 manifest=[dict(file_id='custom_evidence', captured_at=BEFORE)])
        return AuditEngine(self.root, reader)

    def test_non_deletion_does_not_authorize_cleanup(self):
        engine = self.engine([self.fact('account_90001','USER_PROFILE','PRESENT')])
        for text in ['Please remove me from marketing lists only. I still want receipts.',
                     'Do not close the account. I need help resetting my login.',
                     'This is an information request, not a request to erase it.']:
            result = engine.audit({**self.request, 'request_text': text})
            self.assertEqual((result['deletion_status'],result['steps_json']),('NOT_APPLICABLE',[]))

    def test_replica_copy_defeats_primary_deletion(self):
        primary = self.fact('account_90001','USER_PROFILE','ABSENT')
        replica = replace(primary, state='PRESENT', topology='regional_replica')
        result = self.engine([primary,replica]).audit(self.request)
        self.assertEqual(result['deletion_status'],'INCOMPLETE')
        self.assertIn('REPORT_REMAINING_RECORD',[s['operation'] for s in result['steps_json']])

    def test_new_primary_absence_does_not_prove_old_replica_cleanup(self):
        primary = self.fact('account_90001','USER_PROFILE','ABSENT')
        primary.observed = primary.available = TIME
        replica = replace(primary,state='PRESENT',topology='regional_replica',observed=BEFORE,available=BEFORE)
        self.assertEqual(self.engine([primary,replica]).audit(self.request)['deletion_status'],'INCOMPLETE')

    def test_historical_identifier_links_real_copy_not_similar_email(self):
        real = self.fact('account_90001','USER_PROFILE','PRESENT')
        real.links = {'old@example.test'}
        decoy = replace(real,resource='account_90002',links={'person.jr@example.test'})
        result = self.engine([real,decoy]).audit(self.request)
        self.assertEqual({s['resource_id'] for s in result['steps_json']},{'account_90001'})

    def test_future_evidence_does_not_complete_earlier_audit(self):
        present = self.fact('account_90001','USER_PROFILE','PRESENT')
        later = replace(present,state='ABSENT',observed=AFTER,available=AFTER)
        result = self.engine([present,later]).audit(self.request)
        self.assertEqual(result['deletion_status'],'INCOMPLETE')

    def test_tombstone_reference_and_security_record_are_preserved(self):
        facts = [self.fact('tombstone_90001','ACCOUNT_TOMBSTONE','REDACTED','identity_service'),
                 self.fact('audit_record_90001','SECURITY_AUDIT_LOG','PRESENT','security_service')]
        result = self.engine(facts).audit(self.request)
        self.assertEqual(result['deletion_status'],'COMPLETE')
        self.assertEqual({s['operation'] for s in result['steps_json']},
                         {'VERIFY_RECORD_PRESENT','VERIFY_RECORD_REDACTED'})

    def test_residual_hash_requires_redaction(self):
        fact = self.fact('tombstone_90001','ACCOUNT_TOMBSTONE','IDENTIFIABLE','identity_service')
        fact.payload = {'email_hash':'a'*64}
        result = self.engine([fact]).audit(self.request)
        self.assertEqual(result['deletion_status'],'INCOMPLETE')
        self.assertIn('REDACT_RECORD',[s['operation'] for s in result['steps_json']])

    def test_stop_flows_and_block_restore_before_cleanup(self):
        facts = [self.fact('account_90001','USER_PROFILE','PRESENT'),
                 self.fact('data_flow_90001','DATA_FLOW','ACTIVE','integration_service'),
                 self.fact('backup_90001','BACKUP_ARCHIVE','ACTIVE','backup_service')]
        result = self.engine(facts).audit(self.request)
        actions = [s['operation'] for s in result['steps_json'] if s['phase']=='REMEDIATION']
        self.assertEqual(actions,['DISABLE_DATA_FLOW','BLOCK_RESTORE','DELETE_RECORD'])
        self.assertTrue(all(s['evidence_id']=='' for s in result['steps_json'] if s['phase']!='FINDING'))

    def test_reordering_and_unrelated_records_do_not_change_answer(self):
        real = self.fact('account_90001','USER_PROFILE','PRESENT')
        unrelated = replace(real,resource='account_90002',links={'user_90002'})
        first = self.engine([real,unrelated]).audit(self.request)
        second = self.engine([unrelated,real]).audit(self.request)
        self.assertEqual(first,second)

    def test_later_sync_recreates_a_deleted_record(self):
        absent = self.fact('account_90001','USER_PROFILE','ABSENT')
        recreated = replace(absent,state='PRESENT',observed=TIME,available=TIME)
        self.assertEqual(self.engine([absent,recreated]).audit(self.request)['deletion_status'],'INCOMPLETE')

    def test_sql_absence_applies_only_to_linked_scope(self):
        present = self.fact('account_90001','USER_PROFILE','PRESENT')
        scope = Scope('account_service','USER_PROFILE',TIME,TIME,'custom_evidence',set(),links={'user_90002'})
        self.assertEqual(self.engine([present],[scope]).audit(self.request)['deletion_status'],'INCOMPLETE')


if __name__ == '__main__':
    unittest.main()
