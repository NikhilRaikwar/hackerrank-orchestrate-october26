# Northstar deletion audit agent

A terminal application that audits the supplied deletion requests against identity history,
operational evidence, local media, and the supplied deletion policy. It writes the required
`case_id,deletion_status,steps_json` CSV and does not perform destructive actions on real systems.

## Setup

Requires Python 3.10 or later and a vision-capable model account. From the repository root:

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r code/requirements.txt
```

Copy `.env.example` to `.env` and configure **one** provider:

```text
AIML_API_KEY=your-local-key
```

Or configure `OPENROUTER_API_KEY` or `OPENAI_API_KEY`. Never submit credentials.
The tested configuration is AI/ML API with `AUDIT_MODEL=gpt-4o`.
OpenRouter defaults to `openai/gpt-4.1-mini`; model availability depends on the account.
`AUDIT_PROVIDER`, `AUDIT_MODEL`, and `AUDIT_BASE_URL` can override the defaults.
The provider receives fictional participant-facing evidence and request text only.

Place the organizer-supplied `dataset/` beside `code/`. The submission ZIP deliberately
excludes that corpus, so restore the provided dataset when reproducing a clean run.

## Generate predictions

```sh
python code/main.py --dataset dataset --requests dataset/deletion_requests.csv --output output.csv
```

The default command `python code/main.py` uses those paths automatically.
The final output must have exactly 518 data rows sorted by case ID.
The runner checks request coverage, allowed operations/states, citations, sequential
step numbers, phase/operation/system/resource ordering, and status-specific constraints.
A normal run refuses to publish final results if any audit is unresolved.

`output.diagnostics.json` is a local provenance/coverage/usage report. It is not an upload.
`.audit_cache/` stores content-addressed model responses keyed by content, prompt, provider,
and model. Neither diagnostics nor caches are packaged. A clean run recomputes model work.
Temperature zero and deterministic postprocessing reduce variation; provider inference may
still vary across clean runs. The validated output from this development run is uploaded separately.

`--offline` and `--allow-partial` are diagnostic options. Offline mode omits multimodal
model interpretation; partial output is not suitable for submission.

## How it works

1. Parse CSV identity snapshots, historical changes, supplied policy, activities, and evidence manifest.
2. Load every SQL export in isolated in-memory SQLite; read JSON snapshots and nested service exports;
   correlate start/completion trace events across key/value, JSON, syslog, bracket, pipe and cloud logs.
3. Read local PDFs using their text layers; ask the model to extract business facts. Transcribe
   screenshots with vision and ground logical resource IDs through visible text and catalog references.
   Document/order/ticket references do not become fabricated resource IDs.
4. Classify multilingual request intent in batches. Non-deletion requests produce `NOT_APPLICABLE,[]`.
5. Resolve exact current/historical emails, stable references, hashes and resource links. Similar
   identifiers do not establish ownership. Catalog mappings can resolve display aliases.
6. Reconstruct each resource and replica at the audit cutoff. Job SUCCESS is not state proof.
   Keep restore/data-flow risks and detect retained data that still exposes prohibited identifiers.
7. Apply DELETE/REDACT/ANONYMIZE/RETAIN and tombstone rules. Preserve required retained records.
   Disable flows and block restores before record cleanup, then emit deterministic verification checks.

For a bundled historical snapshot or log stream, the contained explicit capture/event time
identifies the observation; an export timestamp is transport metadata. A later observation is
excluded. Standalone media and database snapshots use their capture times. This interpretation
is disclosed because some supplied exports contain earlier observations.

When a de-identified resource has lost ownership fields, an optional inference links a worker
operation to a uniquely nearby request report (at most ten minutes, with a twenty-minute
separation from alternatives). This links provenance only; it never trusts the claimed result
as proof of deletion. Such links are explicitly flagged in local diagnostics. Ambiguous
resources are not assigned using numeric case/resource patterns or sample answers.

## Evaluation

```sh
python code/evaluation/main.py --dataset dataset
python -m unittest discover -s code/evaluation -p test_cases.py -v
```

The evaluator runs all 32 public sample requests and compares parsed JSON against the supplied
sample answers. Only the evaluator reads `sample_output.csv`; inference never opens it.
For an existing prediction file:

```sh
python code/evaluation/main.py --predictions tmp/final_samples.csv
```

`code/evaluation/evaluation_report.md` contains measured status, whole-case, step, field and
sequence accuracy, explicit custom tests, failures and improvements. Public samples contain
no non-deletion cases; custom tests cover that gap. A perfect status score does not imply
perfect resource coverage, citations, ordered plans, or hidden-test performance.

`code/evaluation/usage_report.md` contains actual provider token usage and final-run accounting.
To regenerate after a run, obtain current provider pricing and pass the rates explicitly:

```sh
python code/evaluation/report_usage.py --diagnostics output.diagnostics.json --input-usd-per-million 2.5 --output-usd-per-million 10 --pricing-source "https://api.aimlapi.com/v1/models?id=openai/gpt-4o&include=pricing"
```

These example prices were verified for AI/ML API GPT-4o on 25 October 2026; recheck for future runs.
Local cache hits incur no new inference charge. The report also shows cold reproduction work
and amortizes shared artifact extraction across all 518 requests.

## Package and submit

```sh
python code/package_submission.py
```

This creates and validates `code.zip` using an explicit whitelist: this README, `.env.example`,
runnable Python sources, requirements, and the required Markdown evaluation/usage reports.
It excludes `dataset/`, local credentials, model caches, diagnostics, repository planning documents,
virtual environments, build caches, chat logs and nested archives.

Upload these three files in their corresponding slots:

- `code.zip`
- root `output.csv`
- root `log.txt` as the separate required chat transcript

Challenge upload page:
https://www.hackerrank.com/contests/hackerrank-orchestrate-october26/challenges/ghost-data-still-exists

The organizer also provides separate original-agent-trace ZIP guidance. Follow the live platform
if it exposes that additional upload; do not put a trace archive inside `code.zip`.

No leaderboard placement is claimed. See the evaluation report for the measured remaining limitations.
