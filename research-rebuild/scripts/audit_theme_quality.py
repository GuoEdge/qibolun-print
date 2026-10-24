#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit the v2 theme map without changing corpus or classification outputs.

The v2 map intentionally combines a conservative route layer with the old
audited 23-concept map.  This report measures how wide those routes are and
separates evidence-backed manual decisions from provisional machine
candidates.  It is an audit artifact, not a replacement for article-level
close reading.
"""

from __future__ import annotations

import csv
import json
import math
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "research-rebuild/reports/article-theme-map-v2.csv"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
OUT = ROOT / "research-rebuild/reports"

# Reuse the exact candidate cue dictionary used by the classifier for a
# question-only diagnostic.  This is intentionally not a second classifier:
# it only exposes concepts that came from DeepSeek/body evidence rather than
# from the article's own title/question, which is a useful overreach signal.
sys.path.insert(0, str(ROOT / "research-rebuild/scripts"))
from classify_v2_with_sampling import CUES  # noqa: E402

CONCEPTS = {
    "事实与证据", "定义与达意", "能力与学习", "选择与自由", "责任与后果",
    "成本与总账", "信用与信任", "爱与回应", "净输出与不掠夺", "边界与许可",
    "照料与家庭", "劳动与组织", "财富与市场", "法律与秩序", "权力与异议",
    "技术与工程", "文明与历史", "民族与身份", "生态与自然", "人工智能与机器",
    "心理与主体", "性别与身体", "宗教与自然法",
}


def load_corpus() -> dict[str, dict]:
    result: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                result[row["id"]] = row
    return result


def concepts(row: dict) -> list[str]:
    return [x for x in (row.get("concepts") or "").split(";") if x]


def percentile(values: list[int], p: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    rank = (len(ordered) - 1) * p
    lo, hi = math.floor(rank), math.ceil(rank)
    if lo == hi:
        return float(ordered[lo])
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (rank - lo)


def title_question(article: dict) -> str:
    return f"{article.get('title', '')}｜{article.get('question', '')}".strip("｜")


def direct_question_concepts(article: dict) -> list[str]:
    text = title_question(article)
    found = []
    for concept, cues in CUES.items():
        if any(cue.lower() in text.lower() for cue in cues):
            found.append(concept)
    return found


def main() -> None:
    with MAP.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    articles = load_corpus()

    card = [len(concepts(row)) for row in rows]
    theme_counts = Counter(theme for row in rows for theme in concepts(row))
    source_counts = Counter(row.get("source", "") for row in rows)
    status_counts = Counter(row.get("audit_status", "") for row in rows)
    confidence_counts = Counter(row.get("confidence", "") for row in rows)
    first_pass_counts = Counter(row.get("first_pass_status", "") for row in rows)
    manual_filled_missing = [
        row for row in rows
        if row.get("source") == "manual_decision" and row.get("first_pass_status") == "missing"
    ]
    invalid = [
        {"ordinal": row.get("ordinal"), "id": row.get("id"), "title": row.get("title"), "invalid": [x for x in concepts(row) if x not in CONCEPTS]}
        for row in rows
        if any(x not in CONCEPTS for x in concepts(row))
    ]
    duplicate_ids = [k for k, n in Counter(row.get("id") for row in rows).items() if n != 1]
    missing_articles = [row.get("id") for row in rows if row.get("id") not in articles]

    # The width cut is a routing-risk diagnostic.  It does not assert that a
    # wide article is wrong; it identifies records that need a primary/secondary
    # decision before printing into separate thematic binders.
    wide = []
    for row in rows:
        cs = concepts(row)
        if len(cs) >= 10:
            article = articles.get(row.get("id"), {})
            wide.append({
                "ordinal": row.get("ordinal"), "id": row.get("id"),
                "title": row.get("title", article.get("title", "")),
                "question": article.get("question", ""),
                "concept_count": len(cs), "concepts": row.get("concepts", ""),
                "primary": row.get("primary", ""), "source": row.get("source", ""),
                "audit_status": row.get("audit_status", ""),
            })

    # New candidate risk is narrower than old-map width: low cue score,
    # tied top score, or candidate sets with six themes are all useful review
    # signals.  Keep a deterministic queue so later runs are diffable.
    candidate_rows = [row for row in rows if row.get("source") == "new_first_pass_candidate"]
    candidate_risk = []
    candidate_overreach = []
    for row in candidate_rows:
        try:
            top = int(row.get("top_score") or 0)
        except ValueError:
            top = 0
        try:
            ties = int(row.get("tie_count") or 0)
        except ValueError:
            ties = 0
        cs = concepts(row)
        flags = []
        if top <= 1:
            flags.append("low_top_score")
        if ties >= 2:
            flags.append("top_tie")
        if len(cs) >= 6:
            flags.append("wide_candidate")
        if row.get("first_pass_status") == "missing":
            flags.append("missing_first_pass")
        if flags:
            article = articles.get(row.get("id"), {})
            direct = direct_question_concepts(article)
            assigned = concepts(row)
            spill = [concept for concept in assigned if concept not in direct]
            missing_direct = [concept for concept in direct if concept not in assigned]
            # This is deliberately conservative: a question can imply a
            # concept without naming its cue, so only flag large spillover.
            if len(assigned) >= 4 and len(spill) >= 4:
                candidate_overreach.append({
                    "ordinal": row.get("ordinal"), "id": row.get("id"),
                    "title": row.get("title", article.get("title", "")),
                    "question": article.get("question", ""),
                    "assigned_concepts": row.get("concepts", ""),
                    "question_direct_concepts": ";".join(direct),
                    "question_spillover_concepts": ";".join(spill),
                    "question_missing_direct_concepts": ";".join(missing_direct),
                    "concept_count": len(assigned), "spillover_count": len(spill),
                    "top_score": top, "tie_count": ties,
                    "matched_cues": row.get("matched_cues", ""),
                    "audit_status": row.get("audit_status", ""),
                    "review_reason": "assigned concepts not directly visible in title/question; inspect body evidence",
                })
            candidate_risk.append({
                "ordinal": row.get("ordinal"), "id": row.get("id"),
                "title": row.get("title", article.get("title", "")),
                "question": article.get("question", ""),
                "primary": row.get("primary", ""), "concepts": row.get("concepts", ""),
                "concept_count": len(cs), "top_score": top, "tie_count": ties,
                "matched_cues": row.get("matched_cues", ""),
                "audit_status": row.get("audit_status", ""),
                "risk_flags": ";".join(flags),
            })

    # A balanced deterministic sample for human inspection: up to three wide
    # records per primary concept plus all low-score/tie candidate records.
    by_primary: dict[str, list[dict]] = defaultdict(list)
    for row in wide:
        by_primary[row.get("primary", "")].append(row)
    review: list[dict] = []
    seen: set[str] = set()
    for primary in sorted(by_primary):
        for row in sorted(by_primary[primary], key=lambda x: int(x.get("ordinal") or 0))[:3]:
            review.append({**row, "review_reason": "wide_route"})
            seen.add(row["id"])
    for row in candidate_risk:
        if row["id"] not in seen:
            review.append({**row, "review_reason": row["risk_flags"]})
            seen.add(row["id"])

    summary = {
        "map_records": len(rows),
        "corpus_records": len(articles),
        "map_ids_unique": not duplicate_ids,
        "map_ids_missing_corpus": len(missing_articles),
        "invalid_concepts": len(invalid),
        "theme_count": len(theme_counts),
        "theme_counts": dict(theme_counts),
        "source_counts": dict(source_counts),
        "audit_status_counts": dict(status_counts),
        "confidence_counts": dict(confidence_counts),
        "first_pass_status_counts": dict(first_pass_counts),
        "strict_deepseek_coverage": sum(row.get("first_pass_status") == "covered" for row in rows),
        "manual_decision_filled_missing_first_pass": len(manual_filled_missing),
        "effective_theme_coverage": sum(bool(concepts(row)) for row in rows),
        "concept_cardinality": {
            "distribution": dict(sorted(Counter(card).items())),
            "mean": round(statistics.mean(card), 4) if card else 0,
            "median": statistics.median(card) if card else 0,
            "p90": percentile(card, 0.90),
            "p95": percentile(card, 0.95),
            "max": max(card) if card else 0,
            "empty": sum(value == 0 for value in card),
            "single": sum(value == 1 for value in card),
            "multi": sum(value > 1 for value in card),
            "wide_ge10": len(wide),
            "wide_rate": round(len(wide) / len(rows), 6) if rows else 0,
        },
        "new_candidate_records": len(candidate_rows),
        "new_candidate_risk_records": len(candidate_risk),
        "new_candidate_risk_flags": dict(Counter(flag for row in candidate_risk for flag in row["risk_flags"].split(";"))),
        "new_candidate_question_overreach_records": len(candidate_overreach),
        "review_queue_records": len(review),
        "interpretation": [
            "旧映射的多主题宽度是研究路由信号，不应直接作为互斥打印分类。",
            "正式打印前至少应为每篇确定一个主专题，并将其余主题保留为可回查的次级标签。",
            "新增候选中的低分、并列和宽候选必须回到正文/官方节点证据进行人工复核。",
        ],
        "outputs": [],
    }

    json_path = OUT / "theme-quality-audit-v2.json"
    wide_path = OUT / "theme-quality-wide-routes-v2.csv"
    risk_path = OUT / "theme-quality-candidate-risk-v2.csv"
    review_path = OUT / "theme-quality-review-sample-v2.csv"
    overreach_path = OUT / "theme-quality-candidate-overreach-v2.csv"
    md_path = OUT / "theme-quality-audit-v2.md"
    OUT.mkdir(parents=True, exist_ok=True)

    with wide_path.open("w", encoding="utf-8-sig", newline="") as fh:
        fields = ["ordinal", "id", "title", "question", "concept_count", "concepts", "primary", "source", "audit_status"]
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(wide)
    with risk_path.open("w", encoding="utf-8-sig", newline="") as fh:
        fields = ["ordinal", "id", "title", "question", "primary", "concepts", "concept_count", "top_score", "tie_count", "matched_cues", "audit_status", "risk_flags"]
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(candidate_risk)
    with review_path.open("w", encoding="utf-8-sig", newline="") as fh:
        fields = ["ordinal", "id", "title", "question", "concept_count", "concepts", "primary", "source", "audit_status", "review_reason", "top_score", "tie_count", "matched_cues", "risk_flags"]
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader()
        for row in review:
            writer.writerow({field: row.get(field, "") for field in fields})
    with overreach_path.open("w", encoding="utf-8-sig", newline="") as fh:
        fields = ["ordinal", "id", "title", "question", "assigned_concepts", "question_direct_concepts", "question_spillover_concepts", "question_missing_direct_concepts", "concept_count", "spillover_count", "top_score", "tie_count", "matched_cues", "audit_status", "review_reason"]
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader(); writer.writerows(candidate_overreach)

    summary["outputs"] = [str(json_path), str(wide_path), str(risk_path), str(review_path), str(overreach_path), str(md_path)]
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    md = [
        "# v2 全量主题映射质量审计",
        "",
        "本报告只审计 `article-theme-map-v2.csv`，不改原始语料、旧映射或官方分类边表。",
        "",
        f"- 语料/映射：{len(articles):,}/{len(rows):,}；ID重复 {len(duplicate_ids)}；映射ID不在语料 {len(missing_articles)}；非法主题 {len(invalid)}。",
        f"- 每篇主题数：均值 {summary['concept_cardinality']['mean']}，中位数 {summary['concept_cardinality']['median']}，P90 {summary['concept_cardinality']['p90']}，P95 {summary['concept_cardinality']['p95']}，最大 {summary['concept_cardinality']['max']}。",
        f"- 多主题文章 {summary['concept_cardinality']['multi']:,}（{summary['concept_cardinality']['multi']/len(rows):.1%}）；10 个及以上主题 {len(wide):,}（{len(wide)/len(rows):.1%}）。",
        f"- 新增候选 {len(candidate_rows):,}；风险队列 {len(candidate_risk):,}；抽样队列 {len(review):,}。",
        f"- 题目直接线索与候选主题不一致的过宽诊断记录 {len(candidate_overreach):,}（仅作正文复核入口，不直接判错）。",
        f"- DeepSeek 严格覆盖 {summary['strict_deepseek_coverage']:,}/{len(rows):,}；另有人工决定补位 {len(manual_filled_missing):,}，主题映射有效覆盖 {summary['effective_theme_coverage']:,}/{len(rows):,}。",
        "",
        "## 使用边界",
        "",
        "旧 23 主题映射平均每篇约 7 个标签，因此更适合检索/路由；打印研究需要另设一个主专题字段，次级主题只作为交叉索引。宽路线样本和新增候选风险表提供后续正文复核入口。",
        "",
        "## 主题分布",
        "",
        "| 主题 | 篇数 | 占比 |",
        "|---|---:|---:|",
    ]
    for theme, count in theme_counts.most_common():
        md.append(f"| {theme} | {count:,} | {count/len(rows):.1%} |")
    md.extend(["", "## 风险标记", "", "| 标记 | 篇数 |", "|---|---:|"])
    for flag, count in Counter(flag for row in candidate_risk for flag in row["risk_flags"].split(";")).most_common():
        md.append(f"| {flag} | {count:,} |")
    md.append("")
    md_path.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
