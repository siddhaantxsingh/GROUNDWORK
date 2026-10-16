"""Chunking strategies.

All strategies preserve provenance and never cross a page boundary, so a
citation always names exactly one page: every chunk knows its document, the
first and last page it spans, and its section path. Sizes are in words
(whitespace tokens), which is what the evaluation varies.

* fixed:     sliding window of `size` words with `overlap`, ignoring structure
* sentence:  greedy packing of whole sentences up to `size` words
* structure: one chunk per section; long sections are sentence-packed;
             chunks never cross a section boundary
"""
from __future__ import annotations

from dataclasses import dataclass

from .ingest import Block
from .text import split_sentences


@dataclass(frozen=True)
class ChunkSpec:
    strategy: str = "structure"
    size: int = 200
    overlap: int = 40

    def __post_init__(self) -> None:
        if self.strategy not in ("fixed", "sentence", "structure"):
            raise ValueError(f"unknown chunking strategy {self.strategy!r}")
        if self.size < 8:
            raise ValueError("chunk size must be >= 8 words")
        if not 0 <= self.overlap < self.size:
            raise ValueError("overlap must be in [0, size)")


@dataclass(frozen=True)
class Chunk:
    ordinal: int
    text: str
    page_start: int
    page_end: int
    section: str


def _fixed(blocks: list[Block], spec: ChunkSpec) -> list[Chunk]:
    out: list[Chunk] = []
    pages: list[list[Block]] = []
    for b in blocks:
        if pages and pages[-1][0].page == b.page:
            pages[-1].append(b)
        else:
            pages.append([b])
    for group in pages:
        for c in _fixed_window(group, spec):
            out.append(Chunk(len(out), c.text, c.page_start, c.page_end, c.section))
    return out


def _fixed_window(blocks: list[Block], spec: ChunkSpec) -> list[Chunk]:
    words: list[tuple[str, int, str]] = []
    for b in blocks:
        words.extend((w, b.page, b.section) for w in b.text.split())
    out: list[Chunk] = []
    step = spec.size - spec.overlap
    i = 0
    while i < len(words):
        win = words[i : i + spec.size]
        pages = [p for _, p, _ in win]
        out.append(Chunk(len(out), " ".join(w for w, _, _ in win), min(pages), max(pages), win[0][2]))
        if i + spec.size >= len(words):
            break
        i += step
    return out


def _pack(sents: list[tuple[str, int, str]], size: int, start: int) -> list[Chunk]:
    """Greedy packing of (sentence, page, section) triples. A chunk takes the
    section of its first sentence. A single sentence longer than `size`
    becomes its own chunk(s), split at word boundaries (never dropped)."""
    out: list[Chunk] = []
    cur: list[tuple[str, int, str]] = []
    n = 0

    def emit() -> None:
        nonlocal cur, n
        if cur:
            pages = [p for _, p, _ in cur]
            out.append(Chunk(start + len(out), " ".join(s for s, _, _ in cur), min(pages), max(pages), cur[0][2]))
        cur, n = [], 0

    for s, page, sec in sents:
        w = s.split()
        if len(w) > size:
            emit()
            for k in range(0, len(w), size):
                out.append(Chunk(start + len(out), " ".join(w[k : k + size]), page, page, sec))
            continue
        if n + len(w) > size or (cur and cur[-1][1] != page):
            emit()
        cur.append((s, page, sec))
        n += len(w)
    emit()
    return out


def _sentence(blocks: list[Block], spec: ChunkSpec) -> list[Chunk]:
    return _pack([(s, b.page, b.section) for b in blocks for s in split_sentences(b.text)], spec.size, 0)


def _structure(blocks: list[Block], spec: ChunkSpec) -> list[Chunk]:
    out: list[Chunk] = []
    group: list[Block] = []

    def flush() -> None:
        if not group:
            return
        sents = [(s, b.page, b.section) for b in group for s in split_sentences(b.text)]
        out.extend(_pack(sents, spec.size, len(out)))
        group.clear()

    for b in blocks:
        if group and (b.section != group[0].section or b.page != group[0].page):
            flush()
        group.append(b)
    flush()
    return out


def chunk_blocks(blocks: list[Block], spec: ChunkSpec = ChunkSpec()) -> list[Chunk]:
    blocks = [b for b in blocks if b.text.strip()]
    if not blocks:
        return []
    fn = {"fixed": _fixed, "sentence": _sentence, "structure": _structure}[spec.strategy]
    chunks = fn(blocks, spec)
    return [c for c in chunks if c.text.strip()]
