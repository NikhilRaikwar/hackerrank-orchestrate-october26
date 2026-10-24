"""Run the audit. Public sample answers are intentionally never opened here."""
import argparse
import json
from pathlib import Path
import time
from audit.ai import AIClient
from audit.evidence import EvidenceReader
from audit.engine import AuditEngine
from audit.model import read_csv, validate_output, write_output


def run(dataset, requests, output, offline=False, allow_partial=False):
    root = Path(__file__).resolve().parents[1]
    ai = AIClient(root, enabled=not offline)
    if not offline and not ai.enabled:
        raise RuntimeError('Configure a model key in the repo .env file or environment, or explicitly use --offline for diagnostics')
    started = time.monotonic()
    reader = EvidenceReader(Path(dataset), ai).load(media=not offline)
    requests = read_csv(requests)
    intents = ai.intents(requests) if ai.enabled else {}
    engine = AuditEngine(Path(dataset), reader)
    rows, failures = [], []
    for request in sorted(requests, key=lambda x: x['case_id']):
        try:
            decision = intents.get(request['case_id'], {}).get('deletion_authorized')
            rows.append(engine.audit(request, decision))
        except ValueError as error:
            failures.append(str(error))
    diagnostics = dict(extraction=reader.coverage, errors=reader.errors, failures=failures,
                       cases=engine.explanations, warnings=engine.warnings, usage=ai.usage_report(len(requests)),
                       elapsed_seconds=time.monotonic()-started, offline=offline)
    diagnostics_path = Path(output).with_suffix('.diagnostics.json')
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_path.write_text(json.dumps(diagnostics, ensure_ascii=False, indent=2), encoding='utf-8')
    if failures and not offline and not allow_partial:
        raise RuntimeError(f'{len(failures)} unresolved audits; inspect {diagnostics_path}. No final output was written.')
    ids = {x['file_id'] for x in reader.manifest} | {x['activity_id'] for x in reader.activities} | {x['audit_id'] for x in engine.audit_log}
    if not failures:
        validate_output(rows, requests, ids)
    write_output(output, rows)
    print(f'Wrote {len(rows)}/{len(requests)} audits; {len(failures)} unresolved; {len(reader.facts)} extracted observations')
    return rows, diagnostics


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=root/'dataset')
    parser.add_argument('--requests', type=Path)
    parser.add_argument('--output', type=Path, default=root/'output.csv')
    parser.add_argument('--offline', action='store_true', help='Diagnostic run without AI; does not meet full multimodal inference coverage')
    parser.add_argument('--allow-partial', action='store_true', help='Write provisional partial results for debugging; never use for final submission')
    args = parser.parse_args()
    run(args.dataset, args.requests or args.dataset/'deletion_requests.csv', args.output, args.offline, args.allow_partial)
