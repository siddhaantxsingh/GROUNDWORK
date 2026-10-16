# Contributing

1. `pip install -e '.[dev]'`; start PostgreSQL (with pgvector) and Redis; run `pytest`.
2. Every bug fix comes with a test that fails without the fix.
3. Retrieval changes must keep `tests/test_regression.py` green; if a change intentionally moves the baseline, re-run `benchmarks/retrieval_bench.py ... --update-baseline` and commit the new results together with the change.
4. Never tune parameters on the test split.
