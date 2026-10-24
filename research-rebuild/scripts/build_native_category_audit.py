#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a deterministic, evidence-bearing audit sample for native categories."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
REPORTS = ROOT / "research-rebuild/reports"
TREE = REPORTS / "official-outline-tree.csv"
SUMMARY = REPORTS / "native-article-category-summary.csv"
EDGES = REPORTS / "native-article-category-edges.csv"
THEMES = REPORTS / "article-theme-map-v2.csv"
OUT_CSV = REPORTS / "native-category-audit-sample.csv"
OUT_JSONL = REPORTS / "native-category-audit-sample.jsonl"
OUT_REPORT = REPORTS / "native-category-audit-report.json"
OUT_METHOD = REPORTS / "native-category-audit-method.md"
SEED = "qibo-native-outline-20260921-v1"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_jsonl(path: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                item = json.loads(line)
                out[str(item["id"])] = item
    return out


def stable_rank(value: str) -> str:
    return hashlib.sha256(f"{SEED}:{value}".encode("utf-8")).hexdigest()


def excerpt(article: dict, limit: int = 900) -> str:
    bits = []
    if article.get("question"):
        bits.append("提问：" + str(article["question"]).strip())
    if article.get("text"):
        bits.append("正文：" + str(article["text"]).strip())
    elif article.get("brief"):
        bits.append("摘要：" + str(article["brief"]).strip())
    value = "\n".join(bits)
    return value[:limit] + ("…" if len(value) > limit else "")


def category_candidates(text: str, leaves: list[dict[str, str]], limit: int = 3):
    """Return lexical hints only; they are explicitly non-final."""
    scored = []
    for node in leaves:
        name = node.get("name", "").strip()
        desc = node.get("description", "").strip()
        if not name:
            continue
        name_hits = len(re.findall(re.escape(name), text or ""))
        desc_terms = [x for x in re.findall(r"[\u4e00-\u9fff]{2,}", desc) if len(x) >= 2]
        desc_hits = sum(1 for term in set(desc_terms) if term in (text or ""))
        score = name_hits * 5 + min(desc_hits, 3)
        if score:
            scored.append((score, node))
    scored.sort(key=lambda x: (-x[0], x[1].get("path_names", ""), x[1].get("id", "")))
    return scored[:limit]


def main() -> None:
    corpus = load_jsonl(CORPUS)
    tree_rows = read_csv(TREE)
    tree = {row["id"]: row for row in tree_rows}
    leaves = [row for row in tree_rows if row.get("kind") == "LeoPractice"]
    summaries = {row["article_id"]: row for row in read_csv(SUMMARY)}
    themes = {row["id"]: row for row in read_csv(THEMES)}
    edges = read_csv(EDGES)

    by_article = defaultdict(list)
    by_category = defaultdict(list)
    for edge in edges:
        aid = edge["article_id"]
        if aid in corpus:
            by_article[aid].append(edge)
            by_category[edge["native_category_id"]].append(aid)

    strata = defaultdict(list)
    for aid in corpus:
        summary = summaries.get(aid, {})
        native_count = int(summary.get("native_category_count") or 0)
        old = themes.get(aid, {})
        if native_count == 0:
            strata["native_unassigned"].append(aid)
        elif native_count > 1:
            strata["native_multi_category"].append(aid)
        if not old.get("primary"):
            strata["old_theme_unassigned"].append(aid)

    category_rows = read_csv(REPORTS / "native-category-summary.csv")
    low_purity_categories = set()
    for row in category_rows:
        count = int(row.get("api_unique_article_count") or 0)
        purity = float(row.get("top_theme_purity") or 0)
        if count >= 5 and purity < 0.60:
            low_purity_categories.add(row["native_category_id"])
    for cid in low_purity_categories:
        for aid in by_category.get(cid, []):
            strata["theme_divergence"].append(aid)

    selected = defaultdict(set)

    def take(stratum: str, n):
        ids = sorted(set(strata.get(stratum, [])), key=stable_rank)
        selected[stratum].update(ids if n is None else ids[:n])

    take("native_unassigned", max(60, math.ceil(len(strata["native_unassigned"]) * 0.10)))
    take("native_multi_category", 30)
    take("old_theme_unassigned", None)
    take("theme_divergence", 40)

    for cid, aids in by_category.items():
        if aids:
            selected["category_coverage"].add(sorted(set(aids), key=stable_rank)[0])
    for cid, aids in sorted(by_category.items(), key=lambda kv: (-len(set(kv[1])), kv[0]))[:15]:
        selected["category_high_frequency"].update(sorted(set(aids), key=stable_rank)[:3])

    all_selected = set().union(*selected.values()) if selected else set()
    rows = []
    for aid in sorted(all_selected, key=stable_rank):
        article = corpus[aid]
        summary = summaries.get(aid, {})
        article_edges = by_article.get(aid, [])
        categories = sorted({e.get("native_category_name", "") for e in article_edges if e.get("native_category_name")})
        paths = sorted({e.get("native_parent_path_names", "") for e in article_edges if e.get("native_parent_path_names")})
        roots = sorted({p.split(" / ", 1)[0] for p in paths if p})
        text = " ".join(str(article.get(k, "")) for k in ("title", "question", "brief", "text"))
        candidates = category_candidates(text, leaves)
        reasons = [name for name, ids in selected.items() if aid in ids]
        old = themes.get(aid, {})
        rows.append({
            "audit_id": f"NCA-{len(rows)+1:04d}",
            "article_id": aid,
            "title": str(article.get("title", "")),
            "publishedAt": str(article.get("publishedAt", "")),
            "audit_strata": ";".join(sorted(reasons)),
            "native_status": summary.get("native_assignment_status", "unassigned"),
            "native_category_count": summary.get("native_category_count", "0"),
            "native_categories": ";".join(categories),
            "native_paths": ";".join(paths),
            "native_roots": ";".join(roots),
            "old_primary_theme": old.get("primary", ""),
            "old_concepts": old.get("concepts", ""),
            "candidate_native_categories_nonfinal": ";".join(f"{node.get('path_names','')}[{score}]" for score, node in candidates),
            "evidence_excerpt": excerpt(article),
            "audit_decision": "pending_manual_read",
            "decision_note": "",
        })

    fields = list(rows[0]) if rows else []
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with OUT_JSONL.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    empty_nodes = [row for row in tree_rows if row.get("kind") == "LeoPractice" and not by_category.get(row["id"])]
    report = {
        "generatedAt": "2026-09-21",
        "seed": SEED,
        "corpusRecords": len(corpus),
        "nativeTreeNodes": len(tree_rows),
        "nativePracticeNodes": len(leaves),
        "populatedPracticeNodes": len(by_category),
        "emptyPracticeNodes": len(empty_nodes),
        "unassignedLocalRecords": len(strata["native_unassigned"]),
        "multiCategoryLocalRecords": len(strata["native_multi_category"]),
        "lowPurityPracticeNodes": len(low_purity_categories),
        "sampleRecords": len(rows),
        "sampleByStratum": {key: len(set(value)) for key, value in sorted(selected.items())},
        "emptyPracticeNodeIds": [row["id"] for row in empty_nodes],
        "outputs": [str(OUT_CSV), str(OUT_JSONL), str(OUT_REPORT), str(OUT_METHOD)],
        "interpretation": "candidate_native_categories_nonfinal 是词面提示，只有人工细读后填写 audit_decision 才形成修正。",
    }
    OUT_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    method = f"""# 官方岐伯分类抽样审计

生成日期：2026-09-21；固定种子：{SEED}。

## 目的

官方分类（与谁或什么对象发生何种实践）与既有 23 主题（文章处理何种跨域研究问题）是两个不同维度。此审计只检查官方分类的覆盖、节点一致性与边界，不把官方标签直接替换旧主题，也不把词面候选当成语义结论。

## 抽样层

- category_coverage：每个有文章的官方 LeoPractice 节点至少 1 篇。
- category_high_frequency：15 个高频节点各取最多 3 篇。
- native_unassigned：本地语料未出现在官方库存的文章取约 10%（至少 60 篇）。
- native_multi_category：官方多标签文章取 30 篇。
- theme_divergence：官方节点内旧主题最高占比低于 60% 的节点抽取 40 篇。
- old_theme_unassigned：旧主题为空的文章全部纳入。

## 审核字段

evidence_excerpt 是提问与正文的短摘录；candidate_native_categories_nonfinal 仅由词面重合生成，不能替代阅读。人工审核填写：

- confirmed：官方标签与文章实际实践关系一致；
- reassign_needed：应改到已有官方节点；
- native_unassigned_valid：官方确实没有合适节点；
- api_or_version_gap：疑似官方接口库存、下线或 ID 版本差异；
- needs_image_review：正文不足，必须核验图片；
- uncertain：证据不足，暂不决定。

## 当前覆盖事实

本地语料 {len(corpus)} 篇；官方树 {len(tree_rows)} 节点，其中 LeoPractice {len(leaves)} 个；有文章的实践节点 {len(by_category)} 个，空实践节点 {len(empty_nodes)} 个；本地命中 {len(corpus)-len(strata['native_unassigned'])} 篇，未命中 {len(strata['native_unassigned'])} 篇；抽样队列 {len(rows)} 篇。

## 研究结构

最终索引保留三列：官方岐伯分类（多标签）、旧 23 主题（多主题）、审计状态与证据。官方分类用于对象—实践导航，旧主题用于跨对象比较；未经审计的候选不得进入定稿结论。
"""
    OUT_METHOD.write_text(method, encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
