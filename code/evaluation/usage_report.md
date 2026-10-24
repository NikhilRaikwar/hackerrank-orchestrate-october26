# Final full-dataset usage and cost

Requests audited: **518**. Offline mode: **False**. Runtime: 7.28 seconds.

The final run uses content-addressed local extraction/classification caches. The table distinguishes new network calls/tokens from the logical model work reused by this run. Cached records retain the provider-returned usage from the original inference; no token counts are invented.

| Provider / model | Fresh calls | Local cache hits | Fresh input | Fresh output | Reused input | Reused output |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| aiml / gpt-4o | 0 | 39 | 0 | 0 | 58,638 | 21,388 |
| **Overall** | **0** | **39** | **0** | **0** | **58,638** | **21,388** |

Overall logical input tokens: **58,638**; output: **21,388**; total: **80,026**.

Average logical input/output/total per request: **113.20 / 41.29 / 154.49**.

Fresh inference tokens in this final run: **0**; average **0.00** per request.

Estimated cold reproduction cost, including shared artifact extraction: **USD 0.360475** total; **USD 0.00069590** per request.

Estimated incremental inference cost of this final run: **USD 0.000000** total; **USD 0.00000000** per request.

Price assumptions: USD **2.5** per million input tokens and **10.0** per million output tokens. Source checked 25 October 2026: https://api.aimlapi.com/v1/models?id=openai/gpt-4o&include=pricing

The live AI/ML API catalog lists the user-provided text token unit at USD 2.50/million and model-generated tokens at USD 10/million for GPT-4o. Its cached-provider token unit is USD 1.25/million, but this estimate uses the full input rate for conservative cold reproduction. Local cache hits send no request and incur no new model charge. Taxes, provider billing adjustments, retries without returned usage, and network/CPU costs are excluded. This is an estimate rather than an account billing statement. Development experiments and the coding assistant are outside this final inference run.

Shared multimodal extraction is charged once to the entire run and amortized across all requests; it is not repeated for each request. Prompts are in code/audit/ai.py and code/audit/evidence.py. Raw caches are excluded from the submission; a clean run recomputes them.

Provider token usage missing from any logical request: **False**.

## Work breakdown

| Task | Logical calls | Input tokens | Output tokens |
| --- | ---: | ---: | ---: |
| intent | 13 | 27,504 | 12,954 |
| pdf | 4 | 2,468 | 1,210 |
| vision | 11 | 15,499 | 3,283 |
| vision_ocr | 11 | 13,167 | 3,941 |
