"""Independent public-sample evaluator with field, set and sequence metrics."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import run
from audit.model import read_csv


FIELDS = ('step_no', 'phase', 'system_id', 'resource_id', 'operation', 'state', 'evidence_id')


def identity(step):
    return tuple(step[key] for key in ('phase', 'system_id', 'resource_id', 'operation'))


def evaluate(predictions, expected):
    predictions = {r['case_id']: {**r, 'steps_json': json.loads(r['steps_json']) if isinstance(r['steps_json'], str) else r['steps_json']} for r in predictions}
    totals = Counter()
    confusion = Counter()
    mismatches = []
    for row in expected:
        gold = json.loads(row['steps_json']) if isinstance(row['steps_json'], str) else row['steps_json']
        pred = predictions.get(row['case_id'], dict(deletion_status='MISSING', steps_json=[]))
        steps = pred['steps_json']
        same_status = pred['deletion_status'] == row['deletion_status']
        same_sequence = steps == gold
        totals.update(cases=1, status_correct=int(same_status), case_exact=int(same_status and same_sequence),
                      sequence_exact=int(same_sequence), predicted_steps=len(steps), expected_steps=len(gold))
        confusion[(row['deletion_status'], pred['deletion_status'])] += 1
        pm, gm = {identity(x): x for x in steps}, {identity(x): x for x in gold}
        matches = pm.keys() & gm.keys()
        totals['step_identity_matches'] += len(matches)
        totals['step_exact_matches'] += sum(pm[key] == gm[key] for key in matches)
        for key in gm.keys() | pm.keys():
            totals['field_denominator'] += len(FIELDS)
            if key in matches:
                totals['fields_correct'] += sum(pm[key][f] == gm[key][f] for f in FIELDS)
        if not (same_status and same_sequence):
            mismatches.append(dict(case_id=row['case_id'], expected_status=row['deletion_status'], predicted_status=pred['deletion_status'],
                                   missing=[gm[k] for k in gm.keys()-pm.keys()], extra=[pm[k] for k in pm.keys()-gm.keys()],
                                   changed=[dict(expected=gm[k], predicted=pm[k]) for k in matches if gm[k] != pm[k]]))
    ratio = lambda a, b: totals[a] / totals[b] if totals[b] else 1.0
    metrics = dict(status_accuracy=ratio('status_correct', 'cases'), exact_case_accuracy=ratio('case_exact', 'cases'),
                   sequence_accuracy=ratio('sequence_exact', 'cases'), field_accuracy=ratio('fields_correct', 'field_denominator'),
                   step_precision=ratio('step_identity_matches', 'predicted_steps'), step_recall=ratio('step_identity_matches', 'expected_steps'),
                   exact_step_precision=ratio('step_exact_matches', 'predicted_steps'), counts=dict(totals),
                   confusion={f'{k[0]} -> {k[1]}': v for k,v in confusion.items()})
    p, r = metrics['step_precision'], metrics['step_recall']
    metrics['step_f1'] = 2*p*r/(p+r) if p+r else 0
    return metrics, mismatches


def markdown(metrics, mismatches):
    lines = ['# Evaluation report', '', '## Public samples', '',
             'Sample answers are used only by this independent evaluator, never by inference.', '',
             '| Metric | Result |', '| --- | --- |']
    for key, value in metrics.items():
        if isinstance(value, float):
            lines.append(f'| {key} | {value:.4%} |')
    lines += ['', 'Counts: `' + json.dumps(metrics['counts'], sort_keys=True) + '`', '',
              'Confusion: `' + json.dumps(metrics['confusion'], sort_keys=True) + '`', '',
              'Step precision/recall aligns by (phase, system, resource, operation). Exact step match includes numbering and citation. '
              'Field accuracy compares seven fields over the union of aligned step identities; missing/extra steps contribute seven errors. '
              'Sequence accuracy requires the complete ordered JSON array to match. Whole-case accuracy also requires matching status.', '',
              '## Remaining public-sample differences', '']
    for item in mismatches:
        lines += [f"### {item['case_id']}", '', f"Status: {item['predicted_status']} / expected {item['expected_status']}", '',
                  '```text', json.dumps(item, ensure_ascii=False, indent=2), '```', '']
    if not mismatches:
        lines.append('None.')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=root/'dataset')
    parser.add_argument('--requests', type=Path)
    parser.add_argument('--expected', type=Path)
    parser.add_argument('--predictions', type=Path)
    parser.add_argument('--report', type=Path, default=Path(__file__).parent/'evaluation_report.md')
    parser.add_argument('--offline', action='store_true')
    args = parser.parse_args()
    if args.predictions:
        rows = read_csv(args.predictions)
    else:
        rows, _ = run(args.dataset, args.requests or args.dataset/'sample_deletion_requests.csv', root/'tmp'/'sample_predictions.csv', args.offline)
    metrics, mismatches = evaluate(rows, read_csv(args.expected or args.dataset/'sample_output.csv'))
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(markdown(metrics, mismatches), encoding='utf-8')
    print(json.dumps(metrics, indent=2))
