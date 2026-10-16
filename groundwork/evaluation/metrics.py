"""Retrieval and generation metrics (deterministic; no model judges).

Rankings are lists of *unit ids* (sections, documents or chunks). Callers
map chunk rankings to the unit that relevance is labelled at and dedupe
first (`dedupe_ranking`), so chunking granularity does not inflate scores.
"""
from __future__ import annotations

import math
from typing import Iterable, Sequence


def dedupe_ranking(units: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out = []
    for u in units:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def recall_at_k(ranking: Sequence[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    return len(set(ranking[:k]) & relevant) / len(relevant)


def precision_at_k(ranking: Sequence[str], relevant: set[str], k: int) -> float:
    if k <= 0:
        return 0.0
    return len([u for u in ranking[:k] if u in relevant]) / k


def reciprocal_rank(ranking: Sequence[str], relevant: set[str], k: int | None = None) -> float:
    for i, u in enumerate(ranking[:k] if k else ranking, start=1):
        if u in relevant:
            return 1.0 / i
    return 0.0


def ndcg_at_k(ranking: Sequence[str], gains: dict[str, float], k: int) -> float:
    """NDCG with exponential gain (2^rel - 1) and log2 discount."""
    dcg = sum((2 ** gains.get(u, 0.0) - 1) / math.log2(i + 2) for i, u in enumerate(ranking[:k]))
    ideal = sorted(gains.values(), reverse=True)[:k]
    idcg = sum((2 ** g - 1) / math.log2(i + 2) for i, g in enumerate(ideal))
    return dcg / idcg if idcg > 0 else 0.0


def mean(xs: Iterable[float]) -> float:
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 0.0


def bootstrap_ci(xs: Sequence[float], iters: int = 2000, alpha: float = 0.05, seed: int = 0) -> tuple[float, float]:
    """Percentile bootstrap CI of the mean (for reporting run-to-run uncertainty
    over the query sample)."""
    import random

    if not xs:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(xs)
    means = sorted(sum(xs[rng.randrange(n)] for _ in range(n)) / n for _ in range(iters))
    return means[int(alpha / 2 * iters)], means[int((1 - alpha / 2) * iters) - 1]


def paired_bootstrap_pvalue(a: Sequence[float], b: Sequence[float], iters: int = 2000, seed: int = 0) -> float:
    """Two-sided paired bootstrap test of mean(a) == mean(b) on the same queries."""
    import random

    if len(a) != len(b) or not a:
        raise ValueError("paired test needs equal-length non-empty samples")
    d = [x - y for x, y in zip(a, b)]
    obs = sum(d) / len(d)
    centered = [x - obs for x in d]
    rng = random.Random(seed)
    n = len(d)
    extreme = 0
    for _ in range(iters):
        m = sum(centered[rng.randrange(n)] for _ in range(n)) / n
        if abs(m) >= abs(obs) - 1e-12:
            extreme += 1
    return (extreme + 1) / (iters + 1)


def citation_precision_recall(cited: set[str], supporting: set[str], relevant: set[str]) -> tuple[float, float]:
    """precision = share of citations that are valid (point at a chunk that
    actually supports the sentence it is attached to);
    recall = share of relevant units that the answer cites."""
    precision = len(cited & supporting) / len(cited) if cited else 0.0
    recall = len(cited & relevant) / len(relevant) if relevant else 0.0
    return precision, recall
