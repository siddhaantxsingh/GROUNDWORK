"""Local GGUF models run in-process with llama-cpp-python (CPU).

Everything here is OPT-IN. Nothing in this module is imported unless a
local model is configured, so the default install (and CI) needs neither
llama-cpp-python nor model files. Model files are fetched from Docker Hub's
`ai/` namespace with `scripts/fetch_models.py` (huggingface.co is not
reachable from the build environment).

* `NomicEmbedder`   nomic-embed-text-v1.5 (137M, Apache-2.0). Applies the
  task prefixes the model was trained with: `search_document: ` for chunks
  and `search_query: ` for queries. Mean pooling, L2-normalised. Optional
  Matryoshka truncation (`dim` < 768) re-normalises after truncation.
* `Qwen3Reranker`   Qwen3-Reranker-0.6B (Apache-2.0), a causal LM used as a
  pointwise reranker: the score is P("yes") / (P("yes") + P("no")) for the
  next token after the official judge prompt. This is a real neural
  reranker, not a cross-encoder head; it is slow on CPU (see benchmarks).
* `LlamaCppProvider` an instruct LLM (e.g. Qwen2.5-0.5B-Instruct, SmolLM2)
  behind the same `Provider` interface as the extractive and
  OpenAI-compatible providers, using the same system prompt, source
  fencing, output sanitising and citation parsing.

Configuration (environment, all optional):
  GW_MODEL_DIR           directory with the GGUF files (default /home/user/models)
  GW_THREADS             CPU threads for llama.cpp (default: all cores)
"""
from __future__ import annotations

import math
import os
import threading
import time
from pathlib import Path
from typing import Sequence

import numpy as np

DEFAULT_MODEL_DIR = "/home/user/models"
DEFAULT_FILES = {
    "nomic": "nomic-embed-text-v1.5-latest.gguf",
    "qwen2.5-0.5b": "qwen2.5-0.5B-F16.gguf",
    "smollm2": "smollm2-latest.gguf",
    "qwen3-reranker": "qwen3-reranker-0.6B.gguf",
}


def model_path(key_or_path: str) -> str:
    """Resolve a short model key (see DEFAULT_FILES) or a path to a GGUF file."""
    if key_or_path in DEFAULT_FILES:
        p = Path(os.environ.get("GW_MODEL_DIR", DEFAULT_MODEL_DIR)) / DEFAULT_FILES[key_or_path]
    else:
        p = Path(key_or_path)
    if not p.is_file():
        raise FileNotFoundError(f"model file {p} not found; run scripts/fetch_models.py")
    return str(p)


def _threads() -> int:
    return int(os.environ.get("GW_THREADS", os.cpu_count() or 4))


def _llama(path: str, **kw):
    try:
        from llama_cpp import Llama
    except ImportError as e:  # pragma: no cover - depends on the optional extra
        raise RuntimeError("local models need the optional dependency: pip install 'groundwork[local]'") from e
    return Llama(model_path=path, n_threads=_threads(), verbose=False, **kw)


class NomicEmbedder:
    DOC_PREFIX = "search_document: "
    QUERY_PREFIX = "search_query: "

    def __init__(self, path: str = "nomic", dim: int = 768, n_ctx: int = 2048, batch_tokens: int = 2048) -> None:
        from llama_cpp import LLAMA_POOLING_TYPE_MEAN

        self.path = model_path(path)
        self.llm = _llama(self.path, embedding=True, n_ctx=n_ctx, n_batch=batch_tokens, n_ubatch=batch_tokens,
                          pooling_type=LLAMA_POOLING_TYPE_MEAN)
        self.full_dim = self.llm.n_embd()
        if not 1 <= dim <= self.full_dim:
            raise ValueError(f"dim must be in 1..{self.full_dim}")
        self.dim = dim
        self.n_ctx = n_ctx
        self.name = "nomic-embed-text-v1.5" + ("" if dim == self.full_dim else f"-{dim}")
        self._lock = threading.Lock()  # a llama.cpp context is not thread-safe

    def _truncate(self, text: str) -> str:
        # Keep inputs inside the context window (the model was trained at 2048).
        toks = self.llm.tokenize(text.encode("utf-8", "ignore"), add_bos=True)
        limit = self.n_ctx - 8
        if len(toks) <= limit:
            return text
        return self.llm.detokenize(toks[1:limit]).decode("utf-8", "ignore")

    def _embed(self, texts: Sequence[str], prefix: str) -> np.ndarray:
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        with self._lock:
            items = [self._truncate(prefix + t) for t in texts]
            out = []
            # Small groups keep one llama.cpp batch under n_batch tokens.
            group: list[str] = []
            budget = 0
            for t in items:
                n = len(self.llm.tokenize(t.encode("utf-8", "ignore"), add_bos=True))
                if group and budget + n > self.n_ctx:
                    out.extend(self.llm.embed(group, normalize=False))
                    group, budget = [], 0
                group.append(t)
                budget += n
            if group:
                out.extend(self.llm.embed(group, normalize=False))
        m = np.asarray(out, dtype=np.float32)
        if m.ndim == 1:
            m = m[None, :]
        if self.dim < self.full_dim:
            # Matryoshka: nomic recommends layer norm before truncation.
            mu = m.mean(axis=1, keepdims=True)
            sd = m.std(axis=1, keepdims=True) + 1e-5
            m = ((m - mu) / sd)[:, : self.dim]
        n = np.linalg.norm(m, axis=1, keepdims=True)
        n[n == 0] = 1.0
        return (m / n).astype(np.float32)

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        """Documents / chunks (`search_document:` prefix)."""
        return self._embed(texts, self.DOC_PREFIX)

    def embed_query(self, texts: Sequence[str]) -> np.ndarray:
        """Queries (`search_query:` prefix)."""
        return self._embed(texts, self.QUERY_PREFIX)


class Qwen3Reranker:
    """Pointwise LLM reranker: relevance = P(yes | judge prompt)."""

    PREFIX = ("<|im_start|>system\nJudge whether the Document meets the requirements based on the Query and the "
              "Instruct provided. Note that the answer can only be \"yes\" or \"no\".<|im_end|>\n<|im_start|>user\n")
    SUFFIX = "<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n"
    INSTRUCTION = "Given a search query, retrieve the passage that best answers it"

    def __init__(self, path: str = "qwen3-reranker", n_ctx: int = 1024, max_doc_tokens: int = 384) -> None:
        self.path = model_path(path)
        self.llm = _llama(self.path, n_ctx=n_ctx, n_batch=n_ctx, logits_all=False)
        self.name = "qwen3-reranker-0.6b"
        self.max_doc_tokens = max_doc_tokens
        self._yes = self._single_token("yes")
        self._no = self._single_token("no")
        self._prefix_tokens = self.llm.tokenize(self.PREFIX.encode(), add_bos=False, special=True)
        self._lock = threading.Lock()

    def _single_token(self, word: str) -> int:
        t = self.llm.tokenize(word.encode(), add_bos=False, special=False)
        if len(t) != 1:
            raise RuntimeError(f"reranker vocabulary: {word!r} is not a single token")
        return t[0]

    def _tokens(self, query: str, doc: str) -> list[int]:
        dt = self.llm.tokenize(doc.encode("utf-8", "ignore"), add_bos=False, special=False)[: self.max_doc_tokens]
        doc = self.llm.detokenize(dt).decode("utf-8", "ignore")
        body = f"<Instruct>: {self.INSTRUCTION}\n<Query>: {query}\n<Document>: {doc}" + self.SUFFIX
        return self._prefix_tokens + self.llm.tokenize(body.encode("utf-8", "ignore"), add_bos=False, special=True)

    def score(self, query: str, docs: Sequence[str]) -> list[float]:
        out = []
        with self._lock:
            for d in docs:
                toks = self._tokens(query, d)
                # Reuse the KV cache for the shared system-prompt prefix.
                keep = len(self._prefix_tokens) if list(self.llm._input_ids[: len(self._prefix_tokens)]) == self._prefix_tokens else 0
                if keep and self.llm.n_tokens >= keep:
                    self.llm.n_tokens = keep
                    self.llm._ctx.kv_cache_seq_rm(-1, keep, -1)
                    self.llm.eval(toks[keep:])
                else:
                    self.llm.reset()
                    self.llm.eval(toks)
                # Only the last position produces logits (logits_all=False); read them
                # straight from the context (llama-cpp-python no longer copies them).
                logits = np.ctypeslib.as_array(self.llm._ctx.get_logits(), shape=(self.llm.n_vocab(),))
                y, n = float(logits[self._yes]), float(logits[self._no])
                m = max(y, n)
                out.append(math.exp(y - m) / (math.exp(y - m) + math.exp(n - m)))
        return out


class LlamaCppProvider:
    """Grounded generation with a local instruct model. Uses the shared system
    prompt (sources are untrusted data, cite every sentence, abstain phrase),
    fenced sources, output sanitising and citation parsing from generate.py,
    so `check_grounding` and the injection defences apply unchanged.

    `defended=False` is ONLY for the injection benchmark's no-defence arm:
    plain concatenation of sources, no data-not-instructions warning, and no
    output sanitising."""

    def __init__(self, path: str = "qwen2.5-0.5b", n_ctx: int = 4096, max_tokens: int = 256,
                 max_source_chars: int = 1200, defended: bool = True, seed: int = 0, share_with: "LlamaCppProvider | None" = None) -> None:
        self.path = model_path(path)
        # `share_with` reuses another provider's loaded weights (same model, other settings).
        self.llm = share_with.llm if share_with is not None else _llama(self.path, n_ctx=n_ctx, n_batch=512, seed=seed)
        self.model = Path(self.path).stem
        self.name = f"llamacpp:{self.model}" + ("" if defended else ":undefended")
        self.max_tokens, self.max_source_chars, self.defended = max_tokens, max_source_chars, defended
        self._lock = share_with._lock if share_with is not None else threading.Lock()

    def build_messages(self, query: str, sources) -> list[dict]:
        from .generate import SYSTEM_PROMPT
        from .safety import fence

        if self.defended:
            ctx = "\n\n".join(fence(s.n, s.text[: self.max_source_chars]) for s in sources)
            system = SYSTEM_PROMPT
        else:
            ctx = "\n\n".join(f"[{s.n}] {s.text[: self.max_source_chars]}" for s in sources)
            system = "Answer the question using the numbered sources. Cite sources like [1]."
        return [{"role": "system", "content": system},
                {"role": "user", "content": f"Sources:\n{ctx}\n\nQuestion: {query}"}]

    def generate(self, query: str, sources):
        from .generate import ABSTAIN, Answer, parse_citations
        from .safety import sanitize_output

        t0 = time.perf_counter()
        if not sources:
            return Answer(ABSTAIN, sources, {}, True, self.name, {"latency_ms": 0.0, "tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0})
        with self._lock:
            r = self.llm.create_chat_completion(self.build_messages(query, sources), temperature=0.0, top_k=1,
                                                max_tokens=self.max_tokens, seed=0)
        raw = r["choices"][0]["message"]["content"].strip()
        text = sanitize_output(raw) if self.defended else raw
        usage = r.get("usage", {})
        _, cites = parse_citations(text, max_source=len(sources))
        valid = {s.n for s in sources}
        cites = {i: [n for n in ns if n in valid] for i, ns in cites.items()}
        abstained = text.strip().rstrip(".") == ABSTAIN.rstrip(".") or not text.strip()
        return Answer(text if text.strip() else ABSTAIN, sources, {i: ns for i, ns in cites.items() if ns}, abstained, self.name,
                      {"latency_ms": (time.perf_counter() - t0) * 1e3, "tokens_in": int(usage.get("prompt_tokens", 0)),
                       "tokens_out": int(usage.get("completion_tokens", 0)), "cost_usd": 0.0,
                       "finish_reason": r["choices"][0].get("finish_reason")})
