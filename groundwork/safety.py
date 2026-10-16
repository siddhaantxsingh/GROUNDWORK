"""Prompt-injection defences for retrieved content.

Retrieved documents are untrusted data. Three layers:

1. `scan_injection` flags chunks that contain instruction-like text aimed at
   the model (override attempts, role markers, exfiltration patterns).
   Flagged chunks are excluded from the generation context by default
   (`InjectionPolicy.EXCLUDE`) or kept but marked (`MARK`).
2. Context is fenced: each chunk is wrapped in numbered delimiters and the
   system prompt states that fenced text is data, never instructions; any
   delimiter look-alikes inside chunk text are neutralised first.
3. `sanitize_output` removes markdown images and links to hosts that are not
   allow-listed, the usual channel for exfiltrating data through a rendered
   answer.

Pattern detection is a heuristic with known false negatives (paraphrased or
obfuscated injections); the test-suite measures it on a labelled set and the
limits are documented. It is defence in depth, not a guarantee.
"""
from __future__ import annotations

import enum
import re
import unicodedata
from dataclasses import dataclass
from urllib.parse import urlsplit

_INVISIBLE = re.compile("[\u200b-\u200f\u202a-\u202e\u2060-\u2064\ufeff\u00ad]")


def canonical(text: str) -> str:
    """NFKC (folds full-width and compatibility forms) and removes zero-width
    and bidi control characters, so look-alike text is scanned and fenced
    as what a model will read."""
    return _INVISIBLE.sub("", unicodedata.normalize("NFKC", text))

_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("override", re.compile(r"\b(ignore|disregard|forget|override)\b[^.\n]{0,40}\b(previous|prior|above|earlier|all|any|system|the)\b[^.\n]{0,30}\b(instructions?|prompts?|rules|directions|messages?)", re.I)),
    ("role_switch", re.compile(r"\byou are now (an?|the|in|my)\b|\byou are no longer\b|\bact as (an?|the)\b[^.\n]{0,30}\b(unrestricted|jailbroken|dan|developer mode)|\bnew (system )?instructions?:", re.I)),
    ("role_marker", re.compile(r"<\|?(im_start|im_end|system|endoftext)\|?>|^\s*(system|assistant)\s*:", re.I | re.M)),
    ("prompt_leak", re.compile(r"\b(reveal|print|repeat|show|output)\b[^.\n]{0,30}\b(system prompt|hidden instructions|your instructions|api key|secret)", re.I)),
    ("exfiltration", re.compile(r"!\[[^\]]*\]\(https?://[^)]*[?&][^)]*=|\b(send|post|upload|exfiltrate|forward)\b[^.\n]{0,40}\b(to|via)\b[^.\n]{0,20}(https?://|webhook|email)", re.I)),
    ("tool_hijack", re.compile(r"\b(call|invoke|execute|run)\b[^.\n]{0,20}\b(tool|function|command|shell)\b[^.\n]{0,40}\b(rm -rf|curl|wget|delete|transfer)", re.I)),
]


@dataclass(frozen=True)
class InjectionFinding:
    kind: str
    excerpt: str


def scan_injection(text: str) -> list[InjectionFinding]:
    text = canonical(text)
    out = []
    for kind, pat in _PATTERNS:
        m = pat.search(text)
        if m:
            out.append(InjectionFinding(kind, text[max(0, m.start() - 20): m.end() + 20]))
    return out


class InjectionPolicy(str, enum.Enum):
    EXCLUDE = "exclude"
    MARK = "mark"


FENCE_OPEN = "<<<SOURCE {n}>>>"
FENCE_CLOSE = "<<<END SOURCE {n}>>>"
_ANGLE_RUN = re.compile(r"<{2,}|>{2,}")


def fence(n: int, text: str) -> str:
    """Wrap untrusted text in numbered delimiters. Every run of two or more
    angle brackets inside the text (after canonicalisation) is replaced, so
    no variant of the delimiter (spacing, underscores, full-width, zero-width
    characters, split across lines) can appear inside a fence."""
    safe = _ANGLE_RUN.sub(lambda m: "‹" * len(m.group(0)) if m.group(0)[0] == "<" else "›" * len(m.group(0)), canonical(text))
    return f"{FENCE_OPEN.format(n=n)}\n{safe}\n{FENCE_CLOSE.format(n=n)}"


_URL = r"(?:[a-z][a-z0-9+.-]*:)?//[^\s)>\]\"']+"
_MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(\s*<?(" + _URL + r")>?[^)]*\)", re.I)
_MD_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(\s*<?(" + _URL + r")>?[^)]*\)", re.I)
_MD_REFDEF = re.compile(r"^[ \t]*\[[^\]]+\]:[ \t]*<?(" + _URL + r")>?.*$", re.I | re.M)
_HTML_MEDIA = re.compile(r"<\s*(img|image|video|audio|iframe|source|embed|object|link|script)\b[^>]*>", re.I)
_HTML_A = re.compile(r"<\s*a\b[^>]*>(.*?)<\s*/\s*a\s*>", re.I | re.S)
_BARE_URL = re.compile(_URL, re.I)


def _host(url: str) -> str:
    try:
        return (urlsplit(url if "//" in url else "//" + url).hostname or "").lower()
    except ValueError:
        return ""


def sanitize_output(text: str, allowed_hosts: frozenset[str] = frozenset()) -> str:
    """Remove channels that can exfiltrate data when an answer is rendered:
    markdown images and links, reference-style link definitions, HTML media
    and anchor tags, and bare or protocol-relative URLs, unless the URL's
    real host (userinfo stripped, case-folded) is allow-listed."""
    text = canonical(text)
    ok = lambda url: _host(url) in allowed_hosts  # noqa: E731
    text = _HTML_MEDIA.sub("[embedded content removed]", text)
    text = _HTML_A.sub(lambda m: m.group(1), text)
    text = _MD_REFDEF.sub(lambda m: m.group(0) if ok(m.group(1)) else "[link definition removed]", text)
    text = _MD_IMAGE.sub(lambda m: m.group(0) if ok(m.group(2)) else f"[image removed: {m.group(1)}]", text)
    text = _MD_LINK.sub(lambda m: m.group(0) if ok(m.group(2)) else m.group(1), text)

    def bare(m: re.Match) -> str:
        return m.group(0) if ok(m.group(0)) else "[link removed]"

    # Bare URLs outside allowed markdown links.
    parts = re.split(r"(\[[^\]]*\]\([^)]*\))", text)
    return "".join(p if p.startswith("[") and "](" in p else _BARE_URL.sub(bare, p) for p in parts)
