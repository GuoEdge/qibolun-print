#!/usr/bin/env python3
"""Build non-final native-category candidates for local articles absent upstream.

This is a routing aid only.  It never writes an official category edge and keeps
the evidence used for each lexical suggestion so a later reader can accept,
reject, or replace the candidate.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
SUMMARY = ROOT / "research-rebuild/reports/native-article-category-summary.csv"
TREE = ROOT / "research-rebuild/reports/official-outline-tree.csv"
OUT_DIR = ROOT / "research-rebuild/reports/native-coverage"
OUT_CSV = OUT_DIR / "local-unclassified-candidates.csv"
OUT_JSON = OUT_DIR / "local-unclassified-candidates.json"
OUT_REPORT = OUT_DIR / "local-unclassified-candidates-report.json"


def read_jsonl(path: Path) -> dict[str, dict]:
    rows = {}
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                rows[str(row["id"])] = row
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def lexical_text(article: dict) -> str:
    """Use source fields plus textual Lexical nodes when the normalized body is empty."""
    bits = [article.get("title", ""), article.get("question", ""), article.get("brief", ""), article.get("text", "")]
    raw = article.get("lexical", "")
    if raw:
        try:
            tree = json.loads(raw) if isinstance(raw, str) else raw
            def walk(value):
                if isinstance(value, dict):
                    if value.get("type") in {"text", "quote", "heading", "paragraph", "listitem"}:
                        text = value.get("text")
                        if isinstance(text, str):
                            yield text
                    for child in value.values():
                        yield from walk(child)
                elif isinstance(value, list):
                    for child in value:
                        yield from walk(child)
            bits.extend(walk(tree))
        except (TypeError, ValueError, json.JSONDecodeError):
            pass
    return " ".join(str(x) for x in bits if x)


def excerpt(article: dict, limit: int = 1200) -> str:
    text = "\n".join(x for x in [
        f"提问：{article.get('question', '').strip()}" if article.get("question") else "",
        f"正文：{article.get('text', '').strip()}" if article.get("text") else f"摘要：{article.get('brief', '').strip()}" if article.get("brief") else "",
    ] if x)
    return text[:limit] + ("…" if len(text) > limit else "")


def candidates(text: str, leaves: list[dict[str, str]], limit: int = 5):
    scored = []
    for node in leaves:
        name = node.get("name", "").strip()
        path = node.get("path_names", "")
        desc = node.get("description", "").strip()
        if not name:
            continue
        name_hits = len(re.findall(re.escape(name), text))
        path_parts = [p for p in path.split(" / ") if p and p != name]
        path_hits = sum(len(re.findall(re.escape(part), text)) for part in path_parts)
        terms = set(re.findall(r"[\u4e00-\u9fff]{2,}", desc))
        desc_hits = sum(1 for term in terms if term in text)
        score = name_hits * 6 + path_hits * 2 + min(desc_hits, 4)
        if score:
            evidence = []
            if name_hits:
                evidence.append(f"节点名:{name}×{name_hits}")
            if path_hits:
                evidence.append(f"路径词:{path_hits}")
            if desc_hits:
                evidence.append(f"描述词:{desc_hits}")
            scored.append((score, name_hits, path, node, ";".join(evidence)))
    scored.sort(key=lambda x: (-x[0], -x[1], x[2], x[3].get("id", "")))
    return scored[:limit]


def add_paths(tree: list[dict[str, str]]) -> list[dict[str, str]]:
    """Derive stable root-to-leaf paths from the exported ID-only tree."""
    by_id = {row.get("id", ""): row for row in tree}
    for row in tree:
        chain = []
        cur = row
        seen = set()
        while cur and cur.get("id") not in seen:
            seen.add(cur.get("id", ""))
            chain.append(cur)
            cur = by_id.get(cur.get("parentId", ""))
        row["path_names"] = " / ".join(item.get("name", "") for item in reversed(chain) if item.get("name"))
    return tree


def main() -> None:
    corpus = read_jsonl(CORPUS)
    summary = {row["article_id"]: row for row in read_csv(SUMMARY)}
    tree = add_paths(read_csv(TREE))
    leaves = [row for row in tree if row.get("kind") == "LeoPractice"]
    missing = [aid for aid, row in summary.items() if not int(row.get("native_category_count") or 0)]
    rows = []
    counts = Counter()
    for aid in sorted(missing):
        article = corpus[aid]
        text = lexical_text(article)
        scored = candidates(text, leaves)
        top = scored[0][0] if scored else 0
        tie_count = sum(item[0] == top for item in scored) if scored else 0
        # Scores route reading only; they never imply that the article is in the
        # official outline.  High means a strong lexical lead, not confirmation.
        status = "high_candidate" if top >= 6 and tie_count == 1 else "review_candidate" if top else "no_lexical_candidate"
        counts[status] += 1
        rows.append({
            "article_id": aid,
            "title": article.get("title", ""),
            "question": article.get("question", ""),
            "publishedAt": article.get("publishedAt", ""),
            "url": article.get("url", ""),
            "candidate_status": status,
            "top_score": top,
            "tie_count": tie_count,
            "candidate_paths": ";".join(f"{item[3].get('path_names', '')}[{item[0]}]" for item in scored),
            "match_reasons": ";".join(f"{item[3].get('path_names', '')}:{item[4]}" for item in scored),
            "evidence_excerpt": excerpt(article),
            "official_assignment": "unassigned_pending_manual_read",
            "review_decision": "pending_manual_read",
            "review_note": "",
        })
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    OUT_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    report = {
        "generated_at": "2026-09-21",
        "corpus_records": len(corpus),
        "unclassified_records": len(rows),
        "candidate_status_counts": dict(counts),
        "leaf_nodes_considered": len(leaves),
        "official_assignment_written": False,
        "method": "标题、提问、摘要/正文及 lexical 文本节点与官方 LeoPractice 节点名、路径词、描述词做词面匹配；候选仅供人工细读路由，不是官方分类结论。",
        "outputs": [str(OUT_CSV), str(OUT_JSON), str(OUT_REPORT)],
    }
    OUT_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
