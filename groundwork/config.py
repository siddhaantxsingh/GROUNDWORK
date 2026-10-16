"""Optional model configuration from environment variables.

All local models are opt-in. With none of these variables set, the engine
uses the dependency-free defaults (hashing -> LSA embeddings, feature
reranker, extractive answers), which is what CI runs.

  {P}EMBEDDER        "nomic" -> nomic-embed-text-v1.5 via llama.cpp (needs {P}DIM >= 768)
  {P}LLM_PROVIDER    "extractive" (default) | "llamacpp" | "openai"
  {P}LLM_GGUF        model key (qwen2.5-0.5b, smollm2) or path for "llamacpp" (default qwen2.5-0.5b)
  {P}LLM_MAX_TOKENS  generation limit for "llamacpp" (default 256)
  {P}ENFORCE_GROUNDING  "1" -> drop uncited / unsupported sentences (default "1" for llamacpp)
  {P}RERANKER        "qwen3" -> Qwen3-Reranker-0.6B over the top {P}RERANK_DEPTH hits (default 10)

{P} is "GW_" for Groundwork; Campus AI OS uses the same names with "CAMPUS_".
Model files are resolved under GW_MODEL_DIR (see local_models.py).
"""
from __future__ import annotations

import os

from .generate import ExtractiveProvider, GroundedProvider, OpenAICompatibleProvider, Provider

_CACHE: dict[tuple, object] = {}  # one llama.cpp instance per model per process


def _cached(key: tuple, factory):
    if key not in _CACHE:
        _CACHE[key] = factory()
    return _CACHE[key]


def embedder_from_env(prefix: str = "GW_"):
    name = os.environ.get(prefix + "EMBEDDER", "").strip().lower()
    if not name or name in ("lsa", "hashing", "default"):
        return None
    if name == "nomic":
        from .local_models import NomicEmbedder

        return _cached(("nomic",), NomicEmbedder)
    raise ValueError(f"{prefix}EMBEDDER: unknown embedder {name!r}")


def reranker_from_env(prefix: str = "GW_"):
    name = os.environ.get(prefix + "RERANKER", "").strip().lower()
    if not name or name in ("feature", "none"):
        return None, 0
    if name == "qwen3":
        from .local_models import Qwen3Reranker

        return _cached(("qwen3-reranker",), Qwen3Reranker), int(os.environ.get(prefix + "RERANK_DEPTH", "10"))
    raise ValueError(f"{prefix}RERANKER: unknown reranker {name!r}")


def provider_from_env(prefix: str = "GW_") -> Provider:
    kind = os.environ.get(prefix + "LLM_PROVIDER", "extractive").strip().lower()
    if kind == "extractive":
        return ExtractiveProvider()
    if kind == "openai":
        inner: Provider = OpenAICompatibleProvider()
        enforce_default = "0"
    elif kind == "llamacpp":
        from .local_models import LlamaCppProvider

        gguf = os.environ.get(prefix + "LLM_GGUF", "qwen2.5-0.5b")
        max_tokens = int(os.environ.get(prefix + "LLM_MAX_TOKENS", "256"))
        inner = _cached(("llm", gguf, max_tokens), lambda: LlamaCppProvider(gguf, max_tokens=max_tokens))
        enforce_default = "1"
    else:
        raise ValueError(f"{prefix}LLM_PROVIDER: unknown provider {kind!r}")
    if os.environ.get(prefix + "ENFORCE_GROUNDING", enforce_default) == "1":
        return GroundedProvider(inner)
    return inner


def apply_to_engine_config(cfg, prefix: str = "GW_"):
    """Set the optional embedder and model reranker on an EngineConfig."""
    emb = embedder_from_env(prefix)
    if emb is not None:
        if emb.dim > cfg.dim:
            raise ValueError(f"{prefix}DIM={cfg.dim} is smaller than the {emb.name} dimension {emb.dim}; "
                             f"set {prefix}DIM={emb.dim} (a new database, or reindex)")
        cfg.embedder = emb
    rr, depth = reranker_from_env(prefix)
    if rr is not None:
        cfg.retrieval.model_reranker, cfg.retrieval.model_rerank_depth = rr, depth
    return cfg
