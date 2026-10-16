# ADR 0003 — Deterministic evaluation first, model judges never as ground truth

Status: accepted (2026-10-14)

Decision: retrieval quality is measured against labelled qrels (Recall@K, MRR, NDCG with bootstrap CIs and paired tests); generation is measured with deterministic checks (citation validity, lexical support, abstention). Parameters are tuned on the dev split and reported on the test split. No LLM judge is used; if one is added it is reported separately and never gates a merge on its own.

Consequences: groundedness numbers are a lexical proxy and are labelled as such.
