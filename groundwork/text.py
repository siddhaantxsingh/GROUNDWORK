"""Text normalisation shared by every retriever and metric.

Everything here is deterministic and dependency-free so that BM25 scores,
embeddings and grounding checks are reproducible bit-for-bit.
"""
from __future__ import annotations

import re
import unicodedata

# A compact English stopword list (function words only). Content words such
# as "not" and "no" are kept: they change meaning.
STOPWORDS = frozenset(
    """a an and are as at be been being but by for from has have had he her his i if in into is it its
    itself me my of on or our she so than that the their them then there these they this those to too
    was we were what when where which while who whom why will with would you your yours can could do
    does did doing just should shall may might must about above after again against all any both each
    few further here how more most other own same some such only very s t""".split()
)

_TOKEN_RE = re.compile(r"[a-z0-9]+(?:_[a-z0-9]+)*")
_SENT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])")


def normalize(text: str) -> str:
    """NFKC, lower case, and ASCII-fold common punctuation."""
    return unicodedata.normalize("NFKC", text).lower()


def stem(word: str) -> str:
    """A light, conservative suffix stripper (S-stemmer plus -ing/-ed/-ly,
    then a final silent-e removal so "resolve", "resolves", "resolved" and
    "resolving" share the stem "resolv").

    Deliberately weaker than Porter: over-stemming merges unrelated identifiers
    in code documentation ("process" vs "processing" is fine, "string" must
    not become "str"). Words of 4 letters or fewer are never changed.
    """
    if len(word) <= 4 or word.isdigit():
        return word
    out = word
    for suf, rep, minlen in (("ies", "y", 5), ("sses", "ss", 6), ("ing", "", 7), ("edly", "", 7), ("ed", "", 6), ("ly", "", 6)):
        if word.endswith(suf) and len(word) >= minlen:
            out = word[: -len(suf)] + rep
            break
    else:
        if word.endswith("s") and not word.endswith(("ss", "us", "is")):
            out = word[:-1]
    if out.endswith("e") and not out.endswith("ee") and len(out) > 4:
        out = out[:-1]
    return out


def tokenize(text: str, *, drop_stopwords: bool = True, stemming: bool = True) -> list[str]:
    """Lower-cased alphanumeric tokens; snake_case identifiers are kept whole
    AND split into parts so that `dump_json` matches both `dump_json` and
    `json`."""
    out: list[str] = []
    for tok in _TOKEN_RE.findall(normalize(text)):
        parts = [tok] if "_" not in tok else [tok, *[p for p in tok.split("_") if p]]
        for p in parts:
            if drop_stopwords and p in STOPWORDS:
                continue
            out.append(stem(p) if stemming else p)
    return out


def split_sentences(text: str) -> list[str]:
    """Rule-based sentence splitter; keeps code-ish text such as `os.path`
    intact because a split needs whitespace and an upper-case/digit start."""
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [s.strip() for s in _SENT_RE.split(text) if s.strip()]
