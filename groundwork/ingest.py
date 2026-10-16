"""Document parsing into page- and section-aware blocks.

Every parser returns a list of `Block`s: a run of text with the 1-based page
it came from and the heading path it sits under. Page numbers are what
citations point at, so they are never guessed: formats without pages
(text, Markdown, HTML) report page 1 for all blocks.
"""
from __future__ import annotations

import hashlib
import io
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser


class ParseError(ValueError):
    """The document cannot be parsed (corrupt, unsupported, too large)."""


MAX_DOCUMENT_BYTES = 50 * 1024 * 1024
MAX_PDF_PAGES = 2000


@dataclass(frozen=True)
class Block:
    text: str
    page: int
    section: str  # " > "-joined heading path, "" at top level


@dataclass
class ParsedDocument:
    title: str
    media_type: str
    blocks: list[Block]
    sha256: str
    page_count: int
    meta: dict = field(default_factory=dict)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _decode(data: bytes) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1")


def parse_text(data: bytes, title: str) -> ParsedDocument:
    text = _decode(data)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return ParsedDocument(title, "text/plain", [Block(p, 1, "") for p in paras], _sha(data), 1)


_MD_HEADING = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+#+)?\s*$")
_MD_FENCE = re.compile(r"^(`{3,}|~{3,})")


def parse_markdown(data: bytes, title: str) -> ParsedDocument:
    """Headings define sections; fenced code blocks are kept verbatim and
    never interpreted as headings."""
    path: list[str] = []
    blocks: list[Block] = []
    buf: list[str] = []
    in_fence = False

    def flush() -> None:
        txt = "\n".join(buf).strip()
        buf.clear()
        if txt:
            for para in re.split(r"\n\s*\n", txt) if not txt.startswith(("```", "~~~")) else [txt]:
                if para.strip():
                    blocks.append(Block(para.strip(), 1, " > ".join(path)))

    fence: str | None = None  # opening fence run, e.g. "```" or "~~~~"
    for line in _decode(data).splitlines():
        fm = _MD_FENCE.match(line.strip())
        # CommonMark: a fence closes only with the same character and at
        # least the same length; other fence-like lines are code content.
        if fm and (fence is None or (fm.group(1)[0] == fence[0] and len(fm.group(1)) >= len(fence)
                                     and line.strip() == fm.group(1))):
            if fence is None:
                flush()
                fence = fm.group(1)
                buf.append(line)
            else:
                buf.append(line)
                fence = None
                flush()
            in_fence = fence is not None
            continue
        m = None if in_fence else _MD_HEADING.match(line)
        if m:
            flush()
            level = len(m.group(1))
            del path[level - 1 :]
            while len(path) < level - 1:
                path.append("")
            path.append(m.group(2).strip())
            continue
        buf.append(line)
    flush()
    doc_title = next((b.section.split(" > ")[0] for b in blocks if b.section), title)
    return ParsedDocument(doc_title or title, "text/markdown", blocks, _sha(data), 1)


class _HTMLToBlocks(HTMLParser):
    BLOCK_TAGS = {"p", "div", "li", "pre", "td", "th", "section", "article", "blockquote", "br", "tr", "dd", "dt"}
    SKIP_TAGS = {"script", "style", "noscript", "template", "svg"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.path: list[str] = []
        self.blocks: list[Block] = []
        self.buf: list[str] = []
        self.skip = 0
        self.heading: int | None = None
        self.head_buf: list[str] = []
        self.title = ""
        self.in_title = False

    def _flush(self) -> None:
        txt = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf.clear()
        if txt:
            self.blocks.append(Block(txt, 1, " > ".join(p for p in self.path if p)))

    def _close_heading(self) -> None:
        """End the open heading with whatever text it collected. Called on its
        closing tag, on ANY closing heading tag (mismatched </h2> after <h1>),
        and on any block-level start tag (unclosed heading), so malformed HTML
        never swallows the content that follows."""
        if self.heading is None:
            return
        text = re.sub(r"\s+", " ", "".join(self.head_buf)).strip()
        level = self.heading
        self.heading = None
        self.head_buf = []
        del self.path[level - 1 :]
        while len(self.path) < level - 1:
            self.path.append("")
        self.path.append(text)

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self.skip += 1
            return
        if tag == "title":
            self.in_title = True
        if re.fullmatch(r"h[1-6]", tag):
            self._close_heading()
            self._flush()
            self.heading = int(tag[1])
            self.head_buf = []
        elif tag in self.BLOCK_TAGS:
            self._close_heading()
            self._flush()

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
            return
        if tag == "title":
            self.in_title = False
        if re.fullmatch(r"h[1-6]", tag):
            self._close_heading()
        elif tag in self.BLOCK_TAGS:
            self._flush()

    def handle_data(self, data):
        if self.skip:
            return
        if self.in_title:
            self.title += data
            return
        if self.heading is not None:
            self.head_buf.append(data)
        else:
            self.buf.append(data)


def parse_html(data: bytes, title: str) -> ParsedDocument:
    p = _HTMLToBlocks()
    p.feed(_decode(data))
    p.close()
    p._close_heading()
    p._flush()
    return ParsedDocument(p.title.strip() or title, "text/html", p.blocks, _sha(data), 1)


def parse_pdf(data: bytes, title: str) -> ParsedDocument:
    """Text extraction per page with pypdf. Scanned (image-only) pages yield
    no text; they are reported in meta['empty_pages'], never OCR-guessed."""
    from pypdf import PdfReader
    from pypdf.errors import PdfReadError

    try:
        reader = PdfReader(io.BytesIO(data), strict=False)
        if reader.is_encrypted:
            raise ParseError("encrypted PDF")
        n = len(reader.pages)
    except (PdfReadError, ValueError, KeyError, TypeError) as e:
        raise ParseError(f"unreadable PDF: {e}") from e
    if n > MAX_PDF_PAGES:
        raise ParseError(f"PDF has {n} pages (limit {MAX_PDF_PAGES})")
    blocks: list[Block] = []
    empty: list[int] = []
    section = ""
    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as e:  # pypdf raises assorted errors on damaged streams
            raise ParseError(f"page {i}: {e}") from e
        paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n|\n(?=[A-Z0-9#])", text)]
        paras = [p for p in paras if p]
        if not paras:
            empty.append(i)
        for para in paras:
            # A short line in title case without a final period is treated as a heading.
            if len(para) < 80 and not para.endswith((".", ":", ",")) and para[:1].isupper() and len(para.split()) <= 10:
                section = para
                continue
            blocks.append(Block(para, i, section))
    meta = {"empty_pages": empty}
    info_title = (reader.metadata.title if reader.metadata and reader.metadata.title else "") or title
    return ParsedDocument(str(info_title), "application/pdf", blocks, _sha(data), n, meta)


PARSERS = {
    "text/plain": parse_text,
    "text/markdown": parse_markdown,
    "text/html": parse_html,
    "application/pdf": parse_pdf,
}

EXTENSIONS = {".txt": "text/plain", ".md": "text/markdown", ".markdown": "text/markdown", ".html": "text/html", ".htm": "text/html", ".pdf": "application/pdf"}


def sniff_media_type(filename: str, data: bytes) -> str:
    if data[:5] == b"%PDF-":
        return "application/pdf"
    for ext, mt in EXTENSIONS.items():
        if filename.lower().endswith(ext):
            if mt == "application/pdf":
                raise ParseError("file named .pdf is not a PDF")
            return mt
    head = data[:512].lstrip().lower()
    if head.startswith((b"<!doctype html", b"<html")):
        return "text/html"
    return "text/plain"


def parse(filename: str, data: bytes, media_type: str | None = None) -> ParsedDocument:
    if len(data) > MAX_DOCUMENT_BYTES:
        raise ParseError(f"document is {len(data)} bytes (limit {MAX_DOCUMENT_BYTES})")
    if b"\x00" in data[:4096] and data[:5] != b"%PDF-":
        raise ParseError("binary file is not a supported document type")
    mt = media_type or sniff_media_type(filename, data)
    if mt not in PARSERS:
        raise ParseError(f"unsupported media type {mt}")
    title = re.sub(r"\.[a-z]+$", "", filename.rsplit("/", 1)[-1])
    return PARSERS[mt](data, title)
