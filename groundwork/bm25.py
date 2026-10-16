"""Okapi BM25 over an in-memory inverted index (implemented from scratch).

score(q, d) = sum_{t in q} idf(t) * tf(t,d) * (k1 + 1) / (tf(t,d) + k1 * (1 - b + b * |d| / avgdl))
idf(t)      = ln(1 + (N - df(t) + 0.5) / (df(t) + 0.5))      (Lucene variant: never negative)

The index supports incremental add and delete; statistics (N, avgdl, df)
always reflect the current live set, so deleting a document changes scores
exactly as if it had never been added (tested by a property test).
Query evaluation is term-at-a-time with score accumulators; top-k by heap.
Ties are broken by chunk id so results are deterministic.
"""
from __future__ import annotations

import heapq
import math
from collections import Counter, defaultdict
from typing import Iterable

from .text import tokenize


class BM25Index:
    def __init__(self, k1: float = 1.2, b: float = 0.75) -> None:
        if k1 < 0 or not 0 <= b <= 1:
            raise ValueError("BM25 requires k1 >= 0 and 0 <= b <= 1")
        self.k1, self.b = k1, b
        self.postings: dict[str, dict[str, int]] = defaultdict(dict)
        self.doc_len: dict[str, int] = {}
        self.doc_terms: dict[str, list[str]] = {}  # distinct terms per doc, for deletion
        self.total_len = 0

    def __len__(self) -> int:
        return len(self.doc_len)

    def __contains__(self, doc_id: str) -> bool:
        return doc_id in self.doc_len

    @property
    def avgdl(self) -> float:
        return self.total_len / len(self.doc_len) if self.doc_len else 0.0

    def add(self, doc_id: str, text: str | None = None, tokens: list[str] | None = None) -> None:
        if doc_id in self.doc_len:
            self.delete(doc_id)
        toks = tokens if tokens is not None else tokenize(text or "")
        tf = Counter(toks)
        for t, c in tf.items():
            self.postings[t][doc_id] = c
        self.doc_len[doc_id] = len(toks)
        self.doc_terms[doc_id] = list(tf)
        self.total_len += len(toks)

    def add_many(self, items: Iterable[tuple[str, str]]) -> None:
        for doc_id, text in items:
            self.add(doc_id, text)

    def delete(self, doc_id: str) -> bool:
        if doc_id not in self.doc_len:
            return False
        for t in self.doc_terms.pop(doc_id):
            plist = self.postings[t]
            plist.pop(doc_id, None)
            if not plist:
                del self.postings[t]
        self.total_len -= self.doc_len.pop(doc_id)
        return True

    def idf(self, term: str) -> float:
        n = len(self.doc_len)
        df = len(self.postings.get(term, ()))
        return math.log(1.0 + (n - df + 0.5) / (df + 0.5))

    def score_terms(self, terms: list[str], weights: dict[str, float] | None = None) -> dict[str, float]:
        """Accumulated BM25 score per matching document. `weights` lets query
        expansion (RM3) weight expansion terms below the original ones."""
        acc: dict[str, float] = defaultdict(float)
        if not self.doc_len:
            return acc
        avgdl = self.avgdl or 1.0
        k1, b = self.k1, self.b
        qtf = Counter(terms)
        for t, qc in qtf.items():
            plist = self.postings.get(t)
            if not plist:
                continue
            w = self.idf(t) * qc * (weights.get(t, 1.0) if weights else 1.0)
            for d, tf in plist.items():
                norm = k1 * (1.0 - b + b * self.doc_len[d] / avgdl)
                acc[d] += w * tf * (k1 + 1.0) / (tf + norm)
        return acc

    def search(self, query: str, k: int = 10, *, allowed: set[str] | None = None,
               weights: dict[str, float] | None = None, terms: list[str] | None = None) -> list[tuple[str, float]]:
        terms = terms if terms is not None else tokenize(query)
        acc = self.score_terms(terms, weights)
        items = acc.items() if allowed is None else ((d, s) for d, s in acc.items() if d in allowed)
        return heapq.nsmallest(k, ((d, s) for d, s in items), key=lambda x: (-x[1], x[0]))

    def term_vector(self, doc_id: str) -> Counter:
        return Counter({t: self.postings[t][doc_id] for t in self.doc_terms.get(doc_id, [])})
