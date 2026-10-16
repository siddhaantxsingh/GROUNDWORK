"""Embedding providers.

The built-in, dependency-free dense retrievers (used by default and in CI)
are:

* `HashingEmbedder` — signed feature hashing of unigrams + bigrams with
  sublinear TF. Needs no training; a weak but honest dense baseline.
* `LSAEmbedder` — latent semantic analysis: TF-IDF fitted on the indexed
  corpus, then a truncated SVD (scipy ARPACK). Queries are folded in with
  the same projection. This is a corpus-trained linear model, NOT a neural
  sentence embedder, and the benchmarks label it as such.

Every provider returns L2-normalised float32 rows, so cosine similarity is a
dot product and pgvector's `<=>` (cosine distance) ranks identically to
numpy. A real model plugs in by implementing the same `Embedder` protocol;
`local_models.NomicEmbedder` (nomic-embed-text-v1.5 through llama.cpp) is
the opt-in neural implementation, and it adds `embed_query` for its query
prefix (see `embed_queries`).
"""
from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Protocol, Sequence

import numpy as np

from .text import tokenize


class Embedder(Protocol):
    name: str
    dim: int

    def embed(self, texts: Sequence[str]) -> np.ndarray: ...


def embed_queries(embedder, texts: Sequence[str]) -> np.ndarray:
    """Embed search queries. Asymmetric models (e.g. nomic-embed-text, which
    expects `search_query:` vs `search_document:` prefixes) expose
    `embed_query`; symmetric embedders (LSA, hashing) use `embed` for both."""
    f = getattr(embedder, "embed_query", None)
    return f(texts) if f is not None else embedder.embed(texts)


def _l2(m: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(m, axis=1, keepdims=True)
    n[n == 0] = 1.0
    return (m / n).astype(np.float32)


def _features(text: str) -> list[str]:
    toks = tokenize(text)
    return toks + [f"{a} {b}" for a, b in zip(toks, toks[1:])]


class HashingEmbedder:
    def __init__(self, dim: int = 384) -> None:
        self.dim = dim
        self.name = f"hashing-{dim}"

    def _bucket(self, feat: str) -> tuple[int, float]:
        h = int.from_bytes(hashlib.blake2b(feat.encode(), digest_size=8).digest(), "little")
        return h % self.dim, (1.0 if (h >> 63) & 1 else -1.0)

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        out = np.zeros((len(texts), self.dim), dtype=np.float64)
        for i, t in enumerate(texts):
            for f, c in Counter(_features(t)).items():
                j, s = self._bucket(f)
                out[i, j] += s * (1.0 + math.log(c))
        return _l2(out)


class LSAEmbedder:
    """TF-IDF + truncated SVD. `fit` must be called on the corpus first."""

    def __init__(self, dim: int = 256, max_vocab: int = 60000, min_df: int = 2) -> None:
        self.dim, self.max_vocab, self.min_df = dim, max_vocab, min_df
        self.vocab: dict[str, int] = {}
        self.idf: np.ndarray | None = None
        self.components: np.ndarray | None = None  # (vocab, dim)
        self.name = f"lsa-{dim}"

    @property
    def fitted(self) -> bool:
        return self.components is not None

    def _tfidf(self, texts: Sequence[str]):
        from scipy.sparse import csr_matrix

        rows, cols, vals = [], [], []
        for i, t in enumerate(texts):
            for f, c in Counter(tokenize(t)).items():
                j = self.vocab.get(f)
                if j is not None:
                    rows.append(i)
                    cols.append(j)
                    vals.append((1.0 + math.log(c)) * self.idf[j])
        m = csr_matrix((vals, (rows, cols)), shape=(len(texts), len(self.vocab)), dtype=np.float64)
        # Row-normalise so long chunks do not dominate the factorisation.
        norms = np.sqrt(m.multiply(m).sum(axis=1)).A.ravel()
        norms[norms == 0] = 1.0
        from scipy.sparse import diags

        return diags(1.0 / norms) @ m

    def fit(self, texts: Sequence[str], seed: int = 0) -> "LSAEmbedder":
        from scipy.sparse.linalg import svds

        df: Counter = Counter()
        for t in texts:
            df.update(set(tokenize(t)))
        terms = [t for t, c in df.items() if c >= self.min_df]
        terms.sort(key=lambda t: (-df[t], t))
        terms = terms[: self.max_vocab]
        self.vocab = {t: i for i, t in enumerate(terms)}
        n = len(texts)
        self.idf = np.array([math.log((1 + n) / (1 + df[t])) + 1.0 for t in terms])
        x = self._tfidf(texts)
        k = min(self.dim, min(x.shape) - 1)
        if k < 1:
            raise ValueError("corpus too small for LSA")
        rng = np.random.default_rng(seed)
        v0 = rng.standard_normal(min(x.shape))
        _, s, vt = svds(x, k=k, v0=v0)
        order = np.argsort(-s)
        comps = vt[order].T  # (vocab, k)
        # Deterministic sign: largest-magnitude loading of each component positive.
        signs = np.sign(comps[np.abs(comps).argmax(axis=0), np.arange(comps.shape[1])])
        signs[signs == 0] = 1
        self.components = comps * signs
        self.dim = comps.shape[1]
        self.name = f"lsa-{self.dim}"
        return self

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        if not self.fitted:
            raise RuntimeError("LSAEmbedder.embed called before fit")
        return _l2(np.asarray(self._tfidf(texts) @ self.components))

    def save(self, path: str | Path) -> None:
        p = Path(path)
        np.savez_compressed(p, idf=self.idf, components=self.components)
        p.with_suffix(".vocab.json").write_text(json.dumps({"vocab": self.vocab, "dim": self.dim}))

    @classmethod
    def load(cls, path: str | Path) -> "LSAEmbedder":
        p = Path(path)
        meta = json.loads(p.with_suffix(".vocab.json").read_text())
        z = np.load(p if p.suffix == ".npz" else p.with_suffix(".npz"))
        e = cls(dim=meta["dim"])
        e.vocab, e.idf, e.components = meta["vocab"], z["idf"], z["components"]
        e.name = f"lsa-{e.dim}"
        return e
