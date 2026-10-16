"""Model integration points that run in CI WITHOUT any model file:
asymmetric query embedding, the neural-reranker hook, grounding enforcement
for LLM output, env configuration, the fixed-embedder lifecycle in the
engine, and the generation metrics. Real-model tests are in
test_local_models.py (marker `localmodel`, opt-in)."""
import numpy as np
import pytest

from groundwork import config
from groundwork.embed import HashingEmbedder, embed_queries
from groundwork.engine import Engine, EngineConfig, PaddedEmbedder
from groundwork.evaluation.generation_eval import query_term_coverage, strip_citations
from groundwork.generate import ABSTAIN, Answer, ExtractiveProvider, GroundedProvider, Source, check_grounding
from groundwork.retrieve import ChunkRecord, Corpus, RetrievalConfig, retrieve
from groundwork.store import Store, connect, migrate


class AsymmetricEmbedder:
    """Documents and queries go through different paths, like nomic's prefixes."""

    def __init__(self, dim=32):
        self.inner, self.dim, self.name = HashingEmbedder(dim), dim, f"asym-{dim}"
        self.query_calls = self.doc_calls = 0

    def embed(self, texts):
        self.doc_calls += 1
        return self.inner.embed(["search_document: " + t for t in texts])

    def embed_query(self, texts):
        self.query_calls += 1
        return self.inner.embed(["search_query: " + t for t in texts])


def _recs():
    texts = ["the gearbox needs oil every 500 hours", "inspect blades yearly for cracks", "lock out the rotor before climbing"]
    return [ChunkRecord(f"c{i}", f"d{i}", f"d{i}", 0, t, 1, 1, f"S{i}") for i, t in enumerate(texts)]


def test_queries_use_the_query_path_of_asymmetric_embedders():
    emb = AsymmetricEmbedder()
    c = Corpus(emb)
    c.add(_recs())
    assert emb.doc_calls == 1 and emb.query_calls == 0
    retrieve(c, "gearbox oil", 2, RetrievalConfig("dense"))
    retrieve(c, "gearbox oil", 2, RetrievalConfig("hybrid", rerank=True))
    assert emb.query_calls == 2 and emb.doc_calls == 1
    # symmetric embedders fall back to embed()
    h = HashingEmbedder(16)
    assert np.allclose(embed_queries(h, ["x y"]), h.embed(["x y"]))
    # the engine's padding wrapper keeps the distinction
    p = PaddedEmbedder(emb, 64)
    assert p.embed_query(["q"]).shape == (1, 64) and emb.query_calls == 3


class ReverseReranker:
    name = "reverse"

    def score(self, query, texts):
        return [float(i) for i in range(len(texts))]  # last candidate gets the highest score


def test_model_reranker_rescores_only_the_top_depth():
    c = Corpus(None)
    c.add(_recs())
    base = retrieve(c, "gearbox oil blades rotor", 3, RetrievalConfig("bm25"))
    cfg = RetrievalConfig("bm25", model_reranker=ReverseReranker(), model_rerank_depth=2)
    got = retrieve(c, "gearbox oil blades rotor", 3, cfg)
    assert [h.chunk.id for h in got[:2]] == [base[1].chunk.id, base[0].chunk.id]
    assert got[2].chunk.id == base[2].chunk.id  # below depth: untouched
    assert got[0].sources["first_stage_rank"] == 2
    assert cfg.label() == "bm25+reverse@2"


SOURCES = [Source(1, "c1", "d", "doc", 4, 4, "S", "The gearbox must be lubricated every 500 operating hours."),
           Source(2, "c2", "d", "doc", 7, 7, "S", "Inspect the blades once a year.")]


class FixedProvider:
    name = "fixed"

    def __init__(self, text):
        self.text = text

    def generate(self, query, sources):
        from groundwork.generate import parse_citations

        _, cites = parse_citations(self.text, max_source=len(sources))
        return Answer(self.text, sources, cites, self.text == ABSTAIN, self.name, {"tokens_in": 10})


def test_grounding_enforcement_drops_unsupported_and_uncited_sentences():
    raw = ("The gearbox must be lubricated every 500 operating hours [1]. "
           "It also needs synthetic whale oil from Norway [1]. Blades are fine.")
    a = GroundedProvider(FixedProvider(raw)).generate("gearbox?", SOURCES)
    assert not a.abstained and a.text == "The gearbox must be lubricated every 500 operating hours [1]."
    assert a.usage["dropped_sentences"] == 2 and a.usage["raw_grounding"]["supported"] == 1
    g = check_grounding(a)
    assert g.groundedness == 1.0 and g.citation_precision == 1.0
    assert check_grounding(FixedProvider(raw).generate("gearbox?", SOURCES)).groundedness == pytest.approx(1 / 3)


def test_grounding_enforcement_abstains_when_nothing_is_supported():
    a = GroundedProvider(FixedProvider("Paris is the capital of France [2].")).generate("q", SOURCES)
    assert a.abstained and a.text == ABSTAIN and a.usage["raw_answer"].startswith("Paris")
    assert GroundedProvider(FixedProvider(ABSTAIN)).generate("q", SOURCES).abstained


def test_provider_and_embedder_config_from_env(monkeypatch):
    for k in ("GW_LLM_PROVIDER", "GW_EMBEDDER", "GW_RERANKER"):
        monkeypatch.delenv(k, raising=False)
    assert isinstance(config.provider_from_env(), ExtractiveProvider)
    assert config.embedder_from_env() is None and config.reranker_from_env() == (None, 0)
    monkeypatch.setenv("GW_LLM_PROVIDER", "nonsense")
    with pytest.raises(ValueError):
        config.provider_from_env()
    monkeypatch.setenv("GW_LLM_PROVIDER", "openai")
    monkeypatch.setenv("GW_LLM_BASE_URL", "http://x")
    monkeypatch.setenv("GW_LLM_MODEL", "m")
    assert config.provider_from_env().name == "openai-compatible:m"
    monkeypatch.setenv("GW_ENFORCE_GROUNDING", "1")
    assert isinstance(config.provider_from_env(), GroundedProvider)
    monkeypatch.setenv("GW_EMBEDDER", "word2vec")
    with pytest.raises(ValueError):
        config.embedder_from_env()


def test_dim_too_small_for_fixed_embedder_is_a_clear_error(monkeypatch):
    monkeypatch.setitem(config._CACHE, ("nomic",), AsymmetricEmbedder(768))
    monkeypatch.setenv("GW_EMBEDDER", "nomic")
    with pytest.raises(ValueError, match="GW_DIM"):
        config.apply_to_engine_config(EngineConfig(dim=256))
    assert config.apply_to_engine_config(EngineConfig(dim=768)).embedder.name == "asym-768"


DOC = b"# Manual\n\n## Gearbox\n\nThe gearbox must be lubricated every 500 operating hours.\n\n## Blades\n\nInspect the blades once a year.\n"


def _engine(url, embedder=None):
    conn = connect(url)
    cfg = EngineConfig(dim=64, embedder=embedder, lsa_min_chunks=1000)
    migrate(conn, cfg.dim)
    return Engine(Store(conn), cfg)


def test_switching_to_a_fixed_embedder_reembeds_stored_vectors(db_url):
    eng = _engine(db_url)
    eng.ingest("t", "manual.md", DOC)
    recs, vecs = eng.store.load_chunks("t")
    fixed = AsymmetricEmbedder(32)
    eng2 = _engine(db_url, fixed)  # restart with the neural embedder configured
    ti = eng2.load_tenant("t")
    recs2, vecs2 = eng2.store.load_chunks("t")
    from groundwork.retrieve import embed_text

    want = PaddedEmbedder(fixed, 64).embed([embed_text(r) for r in recs2])
    assert np.allclose(vecs2, want, atol=1e-6) and not np.allclose(vecs, vecs2)
    assert eng2.store.load_embedder("t")[0] == "asym-32" and ti.corpus.embedder.name == "asym-32"
    # new documents are embedded with the same model, and it is never refitted
    eng2.ingest("t", "more.md", b"# More\n\nRotor lock procedure before climbing the tower.\n")
    assert eng2.load_tenant("t").corpus.embedder.name == "asym-32"
    hits = eng2.query("t", "how often is the gearbox lubricated", generate=False, cfg=RetrievalConfig("dense"))["hits"]
    assert hits and fixed.query_calls >= 1
    # and back to the default: vectors return to the hashing space
    eng3 = _engine(db_url)
    assert eng3.load_tenant("t").corpus.embedder.name.startswith("hashing") and eng3.store.load_embedder("t") is None


def test_generation_metric_helpers():
    assert strip_citations("Oil every 500 hours [1, 2]. Yes [3].") == "Oil every 500 hours . Yes ."
    assert query_term_coverage("gearbox oil interval", "The gearbox oil [1].") == pytest.approx(2 / 3)


def test_uncited_copied_sentence_is_attributed_to_its_source_unless_strict():
    # Observed with Qwen2.5-0.5B in Campus AI OS: the right sentence, but no [n] marker.
    raw = "Inspect the blades once a year. Bring a ladder."
    a = GroundedProvider(FixedProvider(raw)).generate("blades?", SOURCES)
    assert not a.abstained and a.text == "Inspect the blades once a year [2]."
    assert a.usage["auto_attributed_sentences"] == 1 and a.usage["dropped_sentences"] == 1
    assert check_grounding(a).groundedness == 1.0
    strict = GroundedProvider(FixedProvider(raw), attribute_uncited=False).generate("blades?", SOURCES)
    assert strict.abstained and strict.provider == "fixed+enforced-strict"
