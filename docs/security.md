# Security

## Threat model

| Asset | Threat | Control | Evidence |
|---|---|---|---|
| Tenant documents | cross-tenant read / delete / probing by id | tenant derived from API key only; every query filtered by tenant; foreign ids → 404 | `test_tenant_isolation` |
| API keys | brute force, timing leaks, logging | ≥16-char keys, SHA-256 digests in memory, `hmac.compare_digest` against every key, rate limiting per key; keys never logged; provider key hidden from `repr` | `test_auth_rate_limit_and_input_limits`, `test_openai_provider_fences_sources_and_accounts_cost` |
| Service availability | huge uploads, page bombs, giant queries | 50 MB upload cap (413), 2000-page PDF cap, query ≤2000 chars, k ≤ 50, rate limit (429) | same |
| Parser | malformed / binary / encrypted files | typed `ParseError` → 422; binary sniffing; encrypted PDFs rejected | `test_bad_inputs_raise_parse_error` |
| Model behaviour | prompt injection inside documents | detector excludes flagged chunks; sources fenced with delimiter-spoofing removal; system prompt marks sources as data | `test_injection_*`, `benchmarks/injection_bench.py` |
| Users of answers | data exfiltration via rendered links/images | non-allow-listed URLs, links and images removed from model output | `test_sanitize_output_allowlist` |
| Database | SQL injection | all SQL parameterised (psycopg); the only interpolated values are integers (`ef_search`, dim) | code review |
| Redis outage | cache poisoning / stale reads / limiter bypass | generation-based invalidation; on Redis errors the cache is bypassed and rate limiting falls back to a per-process token bucket | `test_redis_outage_degrades_gracefully` |

## Prompt-injection results (measured, `benchmarks/results/2026-10-14/injection_bench.json`)

- Known-style injections (4 templates × 50 queries): retrieved in the top-5 in 200/200 cases, excluded from the context in 200/200, answer contamination 0.
- **Paraphrased injections written to avoid the patterns** (4 templates × 50): excluded in **0/200**; the extractive answer quoted the injected sentence in 12/200 cases (6 %).

The detector is a pattern list. It is defence in depth, not a boundary: an LLM provider would see the paraphrased injections. The other layers (fencing, system prompt, output URL sanitising, no tool access) are what limit impact. The patterns were not tuned on the paraphrase set.

## Not done

- No external penetration test; no fuzzing of pypdf beyond malformed-input tests.
- No per-document ACLs inside a tenant (all members of a tenant key see all its documents).
- Dependency audit (`pip-audit`) runs in CI on GitHub Actions (passing as of run 38478453668).
