# Engineering audit (2026-10-14)

Two sources of findings: the benchmark itself (D*) and an independent adversarial review run as a separate agent with read-only access that had to reproduce every claim (A*). Every fix has a regression test that **fails on the code before the fix** (verified by stashing the fix and re-running: `tests/test_generation_safety.py` D1–D2; `tests/test_audit_regressions.py` 17 of 21 cases failed before, the other 4 are guard cases that already held).

| ID | Severity | Defect | Fix | Test |
|---|---|---|---|---|
| D1 | medium | Python list literals quoted from sources (`[0, 1, 2]`) were parsed as citations, depressing citation precision | numbers outside 1..#sources are not citations; ≤6 numbers per marker | `test_list_literals_in_quoted_text_are_not_citations` |
| D2 | medium | grounding re-split the answer text; sentences without final punctuation merged, mixing citations | extractive provider returns structured `segments`; validator uses them | `test_extractive_validation_uses_its_own_segmentation` |
| A1 | high | after deleting below the LSA threshold, a restart loaded the hashing embedder while stored vectors were LSA | the saved model is authoritative and always loaded | `test_a1_*` |
| A2 | high | LSA refit (model save + re-embed) ran outside the ingest transaction; a failure left a committed document, a mismatched model, and stale cache | ingest + model + re-embed in one transaction; memory and cache updated only after commit | `test_a2_*` |
| A3 | medium | output sanitiser missed upper-case schemes, protocol-relative URLs, HTML `<img>`/`<a>`, reference-style links, userinfo host spoofing | case-insensitive, `//` URLs, HTML/ref-def stripping, host from `urlsplit().hostname` | `test_a3_*` |
| A4 | medium | HTML: unclosed or mismatched headings swallowed following content | heading closes on any block start or any closing heading tag | `test_a4_*` |
| A5 | medium | Markdown: closing fence not matched to its opener; `## C#` lost its `#` | CommonMark fence matching; strip closing hashes only after whitespace | `test_a5_*` |
| A6 | medium | the global engine lock was held during answer generation (possibly a 60 s HTTP call), blocking every tenant and `/healthz` | generation and grounding run outside the lock; health check uses a bounded acquire | `test_a6_*` |
| A7 | low-medium | source-delimiter look-alikes (zero-width, full-width, `_`, split) survived fencing; full-width injections evaded the scanner | NFKC + invisible-character removal; every `<<`/`>>` run inside sources is replaced | `test_a7_*` |
| A8 | low | unauthenticated `/metrics` listed tenant names | aggregate gauges only; optional `GW_METRICS_TOKEN` | `test_a8_*` |
| A9 | low | cache hits were not written to the usage log | logged with mode `cached:<config>` | `test_a9_*` |
| S1 | medium | stemmer produced different stems for inflections ("resolved" → resolv, "resolves" → resolve), so answers to "How are X resolved?" missed the right sentence; found by the Campus AI OS browser test | silent-e removal after suffix stripping | `test_stem_inflections_agree` |
| A10 | low | docs referenced a non-existent `dense_backend` option and a missing limitations file | docs corrected; `docs/limitations.md` added | — |

Checked by the reviewer and found correct: BM25 formula/IDF, RRF, weighted fusion, NDCG/MRR/recall, bootstrap CI and paired test, page-bounded chunking, tenant scoping of `doc_ids` and SQL.

Passing tests are evidence, not proof; the remaining known weaknesses are listed in `docs/limitations.md`.
