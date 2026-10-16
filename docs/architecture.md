# Architecture

```
            upload (multipart)                      query
                  │                                   │
          ┌───────▼────────┐                 ┌────────▼─────────┐
          │ ingest.parse   │ md/html/txt/pdf │ retrieve()        │
          │ Block(text,    │  page-aware     │  [RM3 rewrite]    │
          │  page,section) │                 │  BM25 ─┐          │
          └───────┬────────┘                 │  dense ┼─ fusion  │
          ┌───────▼────────┐                 │        └ (RRF/w)  │
          │ chunking       │ never crosses   │  [rerank]         │
          │ structure/     │ a page or       └────────┬─────────┘
          │ sentence/fixed │ (structure) a            │ top-k hits
          └───────┬────────┘ section         ┌────────▼─────────┐
          ┌───────▼────────┐                 │ safety.scan →    │ flagged chunks
          │ embed (LSA /   │                 │ build_sources    │ excluded
          │ hashing)       │                 └────────┬─────────┘
          └───────┬────────┘                 ┌────────▼─────────┐
   one tx ┌───────▼────────┐                 │ Provider          │ extractive (default)
          │ PostgreSQL     │◄── rebuild ─────│  .generate        │ or OpenAI-compatible
          │ documents,     │   at start      └────────┬─────────┘
          │ chunks+vector, │                 ┌────────▼─────────┐
          │ embedders,     │                 │ check_grounding   │ per-sentence support,
          │ query_log,     │                 │                   │ citation validity
          │ eval_runs      │                 └──────────────────┘
          └────────────────┘   Redis: query cache (per-tenant generation) + rate limits
```

## Modules

| Module | Responsibility |
|---|---|
| `text.py` | tokenizer (keeps `snake_case` identifiers whole and split), conservative stemmer, sentence splitter |
| `ingest.py` | parsers → `Block(text, page, section)`; size / page limits; PDF via pypdf, pages never guessed |
| `chunking.py` | `structure` (per section), `sentence` (packing), `fixed` (sliding window); all page-bounded |
| `bm25.py` | inverted index, Okapi BM25 (Lucene idf), incremental add/delete, deterministic top-k |
| `embed.py` | `HashingEmbedder`, `LSAEmbedder` (TF-IDF + truncated SVD); `Embedder` protocol for real models |
| `retrieve.py` | `Corpus` (BM25 + dense matrix), filters before top-k, RRF, weighted fusion, RM3, feature reranker |
| `generate.py` | sources, providers (extractive, OpenAI-compatible), citation parsing, grounding validation |
| `safety.py` | injection scanner, source fencing, output URL sanitiser |
| `store.py` | schema/migrations, transactional ingest, pgvector HNSW search, usage and eval persistence |
| `engine.py` | per-tenant index lifecycle (hashing → LSA refit with full re-embed), cache invalidation |
| `api.py` | FastAPI, API-key auth → tenant, rate limiting, metrics, health |
| `evaluation/` | dataset builder (pystdlib), metrics, retrieval evaluation |

## Invariants

1. **Atomic ingest** — a document row and all its chunks/embeddings are written in one transaction (test: `test_failed_ingest_leaves_no_partial_document`).
2. **Idempotent ingest** — `UNIQUE (tenant, sha256)`; re-uploading the same bytes returns the existing document (test: `test_reupload_is_idempotent`).
3. **Tenant isolation** — every read and write is filtered by the tenant derived from the API key; another tenant's document id behaves as missing (test: `test_tenant_isolation`).
4. **Filters before top-k** — metadata filters are applied inside each retriever (tests: `test_bm25_ties_are_deterministic_and_filter_applies_before_topk`, `test_dense_search_equals_bruteforce_and_respects_filter`).
5. **Delete = never added** for BM25 statistics (property test).
6. **One embedding space per tenant** — the saved model is authoritative; a refit saves the model and re-embeds every chunk in the same transaction as the triggering ingest (tests: `test_lsa_refit_reembeds_everything_consistently`, `test_a1_*`, `test_a2_*`).
7. **No stale cache** — any ingest/delete increments the tenant's cache generation (test: `test_delete_removes_from_results_and_invalidates_cache`).
8. **Citations name one page** — chunks never cross page boundaries.

## Trade-offs

- The query-time index is in memory (rebuilt from PostgreSQL at start). This keeps BM25 and the reranker simple and fast, at the cost of start-up time and memory proportional to the corpus; pgvector search is available for the dense part (`Store.ann_search`).
- A single process with a lock around database access: correct and simple; not horizontally scalable as is (see limitations).
- Lexical grounding check instead of an NLI model: deterministic and cheap, but it can accept a sentence that reuses source words with a different meaning (see `docs/limitations.md`).
