"""Build the `pystdlib` known-item retrieval benchmark from the Python
standard library's own docstrings (human-written, shipped with CPython).

For every public function / class / method with a docstring:
  * query    = the docstring's first sentence (its summary line)
  * document = one Markdown file per module; a section per object containing
               the signature heading and the REST of the docstring
               (the summary sentence is removed, so the answer text never
               contains the query verbatim)
  * qrel     = (module document, section heading) — exactly one relevant
               section per query (known-item search)

Filters: summary >= 6 words, body >= 25 words after removing the summary,
summary unique across the whole library (duplicated summaries such as
"Return self==value." are ambiguous and dropped).

Queries are split into dev / test by a hash of the query id, so parameters
can be tuned on dev and reported on test.

Run: python -m groundwork.evaluation.stdlib_corpus OUT_DIR
Modules are imported in this process; modules with import side effects
(GUI, `this`, `antigravity`, test packages) are excluded.
"""
from __future__ import annotations

import hashlib
import importlib
import inspect
import json
import re
import sys
import warnings
from collections import Counter
from pathlib import Path

from ..text import split_sentences

EXCLUDE_PREFIXES = (
    "antigravity", "this", "tkinter", "turtle", "turtledemo", "idlelib", "test", "lib2to3", "ensurepip",
    "pydoc_data", "__", "_", "venv", "msilib", "winreg", "winsound", "nt", "msvcrt", "_winapi",
)


def _summary_and_body(doc: str) -> tuple[str, str] | None:
    doc = inspect.cleandoc(doc)
    paras = [p.strip() for p in re.split(r"\n\s*\n", doc) if p.strip()]
    if not paras:
        return None
    # Skip a leading signature line such as "dumps(obj, ...) -> str".
    if re.match(r"^[\w.]+\(.*\)(\s*->.*)?$", paras[0].splitlines()[0]) and len(paras) > 1:
        paras = paras[1:]
    sents = split_sentences(paras[0])
    if not sents:
        return None
    summary = sents[0]
    rest_first = " ".join(sents[1:])
    body = "\n\n".join(([rest_first] if rest_first else []) + paras[1:]).strip()
    return summary, body


def _signature(name: str, obj) -> str:
    try:
        return f"{name}{inspect.signature(obj)}"
    except Exception:  # signature() evaluates text signatures and can fail in many ways
        return f"{name}(...)"


def collect() -> list[dict]:
    warnings.simplefilter("ignore")
    items: list[dict] = []
    for modname in sorted(sys.stdlib_module_names):
        if modname.startswith(EXCLUDE_PREFIXES):
            continue
        try:
            mod = importlib.import_module(modname)
        except Exception:
            continue
        for attr, obj in sorted(vars(mod).items()):
            if attr.startswith("_") or getattr(obj, "__module__", None) != modname:
                continue
            if not (inspect.isfunction(obj) or inspect.isclass(obj) or inspect.isbuiltin(obj)):
                continue
            entries = [(f"{modname}.{attr}", obj)]
            if inspect.isclass(obj):
                for mname, m in sorted(vars(obj).items()):
                    if not mname.startswith("_") and (inspect.isfunction(m) or inspect.ismethoddescriptor(m)):
                        entries.append((f"{modname}.{attr}.{mname}", m))
            for qual, o in entries:
                doc = getattr(o, "__doc__", None)
                if not isinstance(doc, str):
                    continue
                sb = _summary_and_body(doc)
                if not sb:
                    continue
                summary, body = sb
                items.append({"module": modname, "qualname": qual, "heading": _signature(qual, o),
                              "summary": summary, "body": body})
    return items


def build(out: Path) -> dict:
    items = collect()
    counts = Counter(i["summary"].lower() for i in items)
    keep = [i for i in items if counts[i["summary"].lower()] == 1
            and len(i["summary"].split()) >= 6 and len(i["body"].split()) >= 25]
    keep_ids = {id(i) for i in keep}
    # Documents contain EVERY collected object: the filtered-out ones are
    # distractors (their full docstring, summary included) so the benchmark
    # is not limited to the 1-of-N sections that have queries.
    by_mod: dict[str, list[dict]] = {}
    for i in items:
        by_mod.setdefault(i["module"], []).append(i)
    docs_dir = out / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    queries, qrels = [], []
    distractors = 0
    for mod, objs in sorted(by_mod.items()):
        if not any(id(o) in keep_ids for o in objs):
            continue
        lines = [f"# {mod}", ""]
        seen: Counter = Counter()
        for o in objs:
            seen[o["heading"]] += 1
            heading = o["heading"] if seen[o["heading"]] == 1 else f"{o['heading']} [{seen[o['heading']]}]"
            o["_heading"] = heading
            text = o["body"] if id(o) in keep_ids else (o["summary"] + " " + o["body"]).strip()
            distractors += id(o) not in keep_ids
            lines += [f"## {heading}", "", text, ""]
        (docs_dir / f"{mod}.md").write_text("\n".join(lines))
        for o in objs:
            if id(o) not in keep_ids:
                continue
            qid = hashlib.sha1(o["qualname"].encode()).hexdigest()[:12]
            split = "test" if int(qid, 16) % 2 else "dev"
            queries.append({"id": qid, "text": o["summary"], "split": split, "qualname": o["qualname"]})
            qrels.append({"query_id": qid, "doc": f"{mod}.md", "section": f"{mod} > {o['_heading']}", "relevance": 1})
    (out / "queries.jsonl").write_text("".join(json.dumps(q) + "\n" for q in queries))
    (out / "qrels.jsonl").write_text("".join(json.dumps(q) + "\n" for q in qrels))
    manifest = {
        "name": "pystdlib-known-item",
        "python": sys.version.split()[0],
        "documents": len(list(docs_dir.glob("*.md"))),
        "sections_total": len(queries) + distractors,
        "distractor_sections": distractors,
        "queries": len(queries),
        "dev": sum(q["split"] == "dev" for q in queries),
        "test": sum(q["split"] == "test" for q in queries),
        "candidates_before_filter": len(items),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest


if __name__ == "__main__":
    print(json.dumps(build(Path(sys.argv[1] if len(sys.argv) > 1 else "data/pystdlib")), indent=2))
