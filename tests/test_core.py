"""Unit and property tests: text, ingestion, chunking, BM25, fusion, metrics."""
import io
import math

import numpy as np
import pytest
from hypothesis import given, settings, strategies as st

from groundwork.bm25 import BM25Index
from groundwork.chunking import ChunkSpec, chunk_blocks
from groundwork.embed import HashingEmbedder, LSAEmbedder
from groundwork.evaluation.metrics import dedupe_ranking, ndcg_at_k, paired_bootstrap_pvalue, recall_at_k, reciprocal_rank
from groundwork.ingest import Block, ParseError, parse
from groundwork.retrieve import ChunkRecord, Corpus, Hit, RetrievalConfig, retrieve, rm3_expand, rrf, weighted_fusion
from groundwork.text import split_sentences, stem, tokenize

# ------------------------------------------------------------------ text


def test_tokenize_keeps_identifiers_and_parts():
    assert tokenize("Use dump_json, then json.loads()") == ["use", "dump_json", "dump", "json", "json", "load"]


def test_stem_is_conservative():
    assert stem("string") == "string" and stem("strings") == "string"
    assert stem("processing") == "process" and stem("queries") == "query"


def test_stem_inflections_agree():
    # Regression (found by the Campus AI OS browser test): "resolved" and
    # "resolves" used to stem to "resolv" and "resolve".
    for family in (["resolve", "resolves", "resolved", "resolving"], ["store", "stores", "stored", "storing"],
                   ["replace", "replaces", "replaced", "replacing"]):
        assert len({stem(w) for w in family}) == 1, family


def test_sentence_split_keeps_dotted_names():
    s = split_sentences("Call os.path.join here. Then return 3.5 items! Next")
    assert s == ["Call os.path.join here.", "Then return 3.5 items!", "Next"]


# ------------------------------------------------------------------ ingestion


def test_markdown_sections_and_fenced_code():
    md = b"# Title\n\nIntro text.\n\n## Install\n\n```sh\n# not a heading\npip install x\n```\n\n### Linux\n\nUse apt.\n\n## Usage\n\nRun it.\n"
    doc = parse("guide.md", md)
    secs = [(b.section, b.text[:12]) for b in doc.blocks]
    assert ("Title", "Intro text.") in secs
    assert any(s == "Title > Install" and t.startswith("```sh") for s, t in secs)
    assert ("Title > Install > Linux", "Use apt.") in secs
    assert ("Title > Usage", "Run it.") in secs
    assert doc.title == "Title"


def test_html_skips_scripts_and_tracks_headings():
    html = b"<html><head><title>T</title><style>p{}</style></head><body><h1>A</h1><p>one</p><script>evil()</script><h2>B</h2><p>two &amp; three</p></body></html>"
    doc = parse("x.html", html)
    assert doc.title == "T"
    assert [(b.section, b.text) for b in doc.blocks] == [("A", "one"), ("A > B", "two & three")]


def _pdf(pages: list[str]) -> bytes:
    from fpdf import FPDF

    pdf = FPDF()
    pdf.set_font("helvetica", size=11)
    for text in pages:
        pdf.add_page()
        pdf.multi_cell(0, 6, text)
    return bytes(pdf.output())


def test_pdf_page_numbers_are_preserved():
    data = _pdf(["Alpha page talks about turbines and blades.", "Beta page covers gearbox lubrication intervals.", "Gamma page lists safety checks."])
    doc = parse("manual.pdf", data)
    assert doc.page_count == 3
    pages = {b.page for b in doc.blocks if "gearbox" in b.text}
    assert pages == {2}


@pytest.mark.parametrize("data,name", [(b"%PDF-1.4 garbage", "x.pdf"), (b"not a pdf", "x.pdf"), (b"\x00\x01\x02binary", "x.bin")])
def test_bad_inputs_raise_parse_error(data, name):
    with pytest.raises(ParseError):
        parse(name, data)


def test_size_limit(monkeypatch):
    import groundwork.ingest as ing

    monkeypatch.setattr(ing, "MAX_DOCUMENT_BYTES", 10)
    with pytest.raises(ParseError):
        ing.parse("a.txt", b"x" * 11)


# ------------------------------------------------------------------ chunking

words = st.text(alphabet="abcdefghij ", min_size=1, max_size=60).map(lambda s: " ".join(s.split()) or "a")
blocks_st = st.lists(st.builds(lambda t, p, s: Block(t + ".", p, s), words, st.integers(1, 5), st.sampled_from(["", "A", "B"])), min_size=1, max_size=20)


@settings(max_examples=150, deadline=None)
@given(blocks_st, st.sampled_from(["fixed", "sentence", "structure"]), st.integers(8, 40))
def test_chunking_never_loses_words(blocks, strategy, size):
    spec = ChunkSpec(strategy, size, min(4, size - 1))
    chunks = chunk_blocks(blocks, spec)
    src = [w for b in blocks for w in b.text.split()]
    got = [w for c in chunks for w in c.text.split()]
    if strategy == "fixed":
        assert set(src) <= set(got)  # overlap repeats words
    else:
        assert got == src  # exact, in order
    # Page boundaries are respected even when blocks alternate pages.
    for c in chunks:
        assert 1 <= c.page_start == c.page_end  # chunks never cross pages
        assert len(c.text.split()) <= size or strategy == "fixed" and len(c.text.split()) <= size
    assert [c.ordinal for c in chunks] == list(range(len(chunks)))


def test_structure_chunks_never_cross_sections():
    blocks = [Block("One two three.", 1, "A"), Block("Four five.", 1, "A"), Block("Six seven.", 2, "B")]
    chunks = chunk_blocks(blocks, ChunkSpec("structure", 50, 0))
    assert [(c.section, c.text) for c in chunks] == [("A", "One two three. Four five."), ("B", "Six seven.")]
    assert chunks[1].page_start == 2


def test_invalid_chunk_spec():
    with pytest.raises(ValueError):
        ChunkSpec("fixed", 10, 10)
    with pytest.raises(ValueError):
        ChunkSpec("magic")


# ------------------------------------------------------------------ BM25


def test_bm25_matches_formula():
    idx = BM25Index(k1=1.2, b=0.75)
    idx.add("d1", tokens=["apple", "banana", "apple"])
    idx.add("d2", tokens=["banana", "cherry"])
    idx.add("d3", tokens=["cherry", "cherry", "date", "egg"])
    n, avgdl = 3, 9 / 3
    idf = math.log(1 + (n - 1 + 0.5) / (1 + 0.5))
    expected = idf * 2 * 2.2 / (2 + 1.2 * (1 - 0.75 + 0.75 * 3 / avgdl))
    (doc, score), = idx.search("", 1, terms=["apple"])
    assert doc == "d1" and score == pytest.approx(expected)


texts = st.lists(st.lists(st.sampled_from("abcdefgh"), min_size=1, max_size=12), min_size=2, max_size=12)


@settings(max_examples=150, deadline=None)
@given(texts, st.data())
def test_bm25_delete_equals_never_added(docs, data):
    victim = data.draw(st.integers(0, len(docs) - 1))
    a, b = BM25Index(), BM25Index()
    for i, d in enumerate(docs):
        a.add(f"d{i}", tokens=d)
        if i != victim:
            b.add(f"d{i}", tokens=d)
    a.delete(f"d{victim}")
    for q in "abcdefgh":
        assert a.search("", 20, terms=[q]) == pytest.approx(b.search("", 20, terms=[q]))
    assert a.avgdl == pytest.approx(b.avgdl)


def test_bm25_ties_are_deterministic_and_filter_applies_before_topk():
    idx = BM25Index()
    for i in range(50):
        idx.add(f"d{i:02d}", tokens=["x"] * (1 + i % 3))
    top = idx.search("", 5, terms=["x"])
    assert top == idx.search("", 5, terms=["x"])
    # A filter selecting a low-scoring document must still return it.
    low = top[-1][0]
    worst = min(idx.score_terms(["x"]).items(), key=lambda kv: (kv[1], kv[0]))[0]
    assert idx.search("", 1, terms=["x"], allowed={worst})[0][0] == worst
    assert low != worst


# ------------------------------------------------------------------ embeddings / dense / fusion


def _corpus(emb=None):
    recs = [ChunkRecord(f"c{i}", f"doc{i % 3}", f"doc{i % 3}", i, t, 1, 1, "")
            for i, t in enumerate(["the cat sat on the mat", "dogs chase cats in the yard", "stock markets fell sharply",
                                   "interest rates and inflation", "a cat and a dog played", "bond yields rose with rates"])]
    c = Corpus(emb or HashingEmbedder(64))
    c.add(recs)
    return c


def test_dense_search_equals_bruteforce_and_respects_filter():
    c = _corpus()
    q = c.embedder.embed(["cat on a mat"])[0]
    hits = c.search_dense("cat on a mat", 6)
    ids, m = c._matrix()
    brute = sorted(ids, key=lambda i: -(m[ids.index(i)] @ q))
    assert [h.chunk.id for h in hits] == brute
    only = c.search_dense("cat on a mat", 3, lambda ch: ch.doc_id == "doc2")
    assert {h.chunk.doc_id for h in only} == {"doc2"} and len(only) == 2


def test_corpus_delete_doc_removes_from_both_indexes():
    c = _corpus()
    c.delete_doc("doc0")
    assert all(h.chunk.doc_id != "doc0" for h in c.search_dense("cat", 10))
    assert all(h.chunk.doc_id != "doc0" for h in c.search_bm25("cat", 10))
    assert len(c) == 4


def test_lsa_is_deterministic_and_normalised():
    texts = [f"topic {i % 4} word{i % 7} common filler text {i}" for i in range(60)]
    a = LSAEmbedder(dim=8, min_df=1).fit(texts).embed(texts[:5])
    b = LSAEmbedder(dim=8, min_df=1).fit(texts).embed(texts[:5])
    assert np.allclose(a, b)
    assert np.allclose(np.linalg.norm(a, axis=1), 1.0, atol=1e-5)


def test_rrf_and_weighted_fusion():
    r = [ChunkRecord(x, "d", "d", 0, x, 1, 1, "") for x in "abc"]
    l1 = [Hit(r[0], 3), Hit(r[1], 2)]
    l2 = [Hit(r[1], 0.9), Hit(r[2], 0.1)]
    fused = rrf([l1, l2], 3, k_rrf=60)
    assert [h.chunk.id for h in fused] == ["b", "a", "c"]
    assert fused[0].score == pytest.approx(1 / 62 + 1 / 61)
    w = weighted_fusion([l1, l2], [0.5, 0.5], 3)
    assert [h.chunk.id for h in w] == ["a", "b", "c"] or [h.chunk.id for h in w][0] in "ab"


def test_rm3_keeps_original_terms_strongest():
    c = _corpus()
    terms, weights = rm3_expand(c, "cat")
    assert weights["cat"] == pytest.approx(1.0)
    assert all(w <= 1.0 for w in weights.values())


def test_retrieve_pipeline_all_modes():
    c = _corpus()
    for cfg in [RetrievalConfig("bm25"), RetrievalConfig("dense"), RetrievalConfig("hybrid"), RetrievalConfig("hybrid", fusion="weighted"),
                RetrievalConfig("hybrid", rewrite="rm3", rerank=True)]:
        t = {}
        hits = retrieve(c, "cat", 3, cfg, timings=t)
        assert 0 < len(hits) <= 3 and t["total_ms"] >= 0


# ------------------------------------------------------------------ metrics


def test_metrics_known_values():
    ranking = ["x", "a", "y", "b"]
    rel = {"a", "b"}
    assert recall_at_k(ranking, rel, 2) == 0.5
    assert reciprocal_rank(ranking, rel) == 0.5
    ideal = (1 / math.log2(2) + 1 / math.log2(3))
    assert ndcg_at_k(ranking, {"a": 1, "b": 1}, 4) == pytest.approx((1 / math.log2(3) + 1 / math.log2(5)) / ideal)
    assert dedupe_ranking(["a", "a", "b", "a"]) == ["a", "b"]
    assert paired_bootstrap_pvalue([1.0] * 30, [1.0] * 30) == pytest.approx(1.0)
    assert paired_bootstrap_pvalue([1.0] * 30, [0.0] * 30) < 0.01
