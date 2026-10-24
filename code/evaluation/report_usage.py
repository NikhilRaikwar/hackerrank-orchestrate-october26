"""Generate the required usage report from the actual final-run diagnostics."""
import argparse
from collections import defaultdict
import json
from pathlib import Path


def report(data, input_rate, output_rate, pricing_source):
    usage = data['usage']
    entries = usage['entries']
    groups = defaultdict(list)
    for entry in entries:
        groups[(entry['provider'],entry['model'])].append(entry)
    lines = ['# Final full-dataset usage and cost', '',
             f"Requests audited: **{usage['requests']}**. Offline mode: **{data['offline']}**. "
             f"Runtime: {data['elapsed_seconds']:.2f} seconds.", '',
             'The final run uses content-addressed local extraction/classification caches. '
             'The table distinguishes new network calls/tokens from the logical model work reused by this run. '
             'Cached records retain the provider-returned usage from the original inference; no token counts are invented.', '',
             '| Provider / model | Fresh calls | Local cache hits | Fresh input | Fresh output | Reused input | Reused output |',
             '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    total_input = total_output = fresh_input = fresh_output = 0
    missing = False
    for (provider,model), items in groups.items():
        missing |= any(x.get('input_tokens') is None or x.get('output_tokens') is None for x in items)
        fi = sum(x.get('input_tokens') or 0 for x in items if not x['cache_hit'])
        fo = sum(x.get('output_tokens') or 0 for x in items if not x['cache_hit'])
        ri = sum(x.get('input_tokens') or 0 for x in items if x['cache_hit'])
        ro = sum(x.get('output_tokens') or 0 for x in items if x['cache_hit'])
        total_input += fi+ri
        total_output += fo+ro
        fresh_input += fi
        fresh_output += fo
        lines.append(f'| {provider} / {model} | {sum(not x["cache_hit"] for x in items)} | {sum(x["cache_hit"] for x in items)} | {fi:,} | {fo:,} | {ri:,} | {ro:,} |')
    count = usage['requests']
    cold = (total_input*input_rate+total_output*output_rate)/1_000_000
    fresh = (fresh_input*input_rate+fresh_output*output_rate)/1_000_000
    lines += [f'| **Overall** | **{usage["calls"]}** | **{usage["cache_hits"]}** | **{fresh_input:,}** | **{fresh_output:,}** | **{total_input-fresh_input:,}** | **{total_output-fresh_output:,}** |', '',
              f'Overall logical input tokens: **{total_input:,}**; output: **{total_output:,}**; total: **{total_input+total_output:,}**.', '',
              f'Average logical input/output/total per request: **{total_input/count:.2f} / {total_output/count:.2f} / {(total_input+total_output)/count:.2f}**.', '',
              f'Fresh inference tokens in this final run: **{fresh_input+fresh_output:,}**; average **{(fresh_input+fresh_output)/count:.2f}** per request.', '',
              f'Estimated cold reproduction cost, including shared artifact extraction: **USD {cold:.6f}** total; **USD {cold/count:.8f}** per request.', '',
              f'Estimated incremental inference cost of this final run: **USD {fresh:.6f}** total; **USD {fresh/count:.8f}** per request.', '',
              f'Price assumptions: USD **{input_rate}** per million input tokens and **{output_rate}** per million output tokens. '
              f'Source checked 25 October 2026: {pricing_source}', '',
              'The live AI/ML API catalog lists the user-provided text token unit at USD 2.50/million and model-generated tokens at USD 10/million for GPT-4o. '
              'Its cached-provider token unit is USD 1.25/million, but this estimate uses the full input rate for conservative cold reproduction. '
              'Local cache hits send no request and incur no new model charge. Taxes, provider billing adjustments, retries without returned usage, and network/CPU costs are excluded. '
              'This is an estimate rather than an account billing statement. Development experiments and the coding assistant are outside this final inference run.', '',
              'Shared multimodal extraction is charged once to the entire run and amortized across all requests; it is not repeated for each request. '
              'Prompts are in code/audit/ai.py and code/audit/evidence.py. Raw caches are excluded from the submission; a clean run recomputes them.', '',
              f'Provider token usage missing from any logical request: **{missing}**.', '',
              '## Work breakdown', '', '| Task | Logical calls | Input tokens | Output tokens |', '| --- | ---: | ---: | ---: |']
    for task in sorted({x['task'] for x in entries}):
        items = [x for x in entries if x['task']==task]
        lines.append(f'| {task} | {len(items)} | {sum(x.get("input_tokens") or 0 for x in items):,} | {sum(x.get("output_tokens") or 0 for x in items):,} |')
    return '\n'.join(lines)+'\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostics', type=Path, required=True)
    parser.add_argument('--report', type=Path, default=Path(__file__).parent/'usage_report.md')
    parser.add_argument('--input-usd-per-million', type=float, required=True)
    parser.add_argument('--output-usd-per-million', type=float, required=True)
    parser.add_argument('--pricing-source', required=True)
    args = parser.parse_args()
    data = json.loads(args.diagnostics.read_text(encoding='utf-8'))
    args.report.write_text(report(data,args.input_usd_per_million,args.output_usd_per_million,args.pricing_source),encoding='utf-8')
    print('Usage report written:',args.report)
