#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a deterministic manual audit queue for the A00-A21 print spine.

The queue is a sampling instrument, not a classifier.  It deliberately
over-samples disagreements, ties, new records, official multi-label edges,
unassigned records, images and topic boundaries.  Every row keeps the
candidate topic and source evidence so a reviewer can return to the article,
official path and old route before changing the classification.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
CANDIDATES = REPORTS / "print-topic-candidates-v2.csv"
NATIVE_SUMMARY = REPORTS / "native-article-category-summary.csv"
NATIVE_EDGES = REPORTS / "native-article-category-edges.csv"
NATIVE_CATEGORIES = REPORTS / "native-category-summary.csv"
OUT_CSV = REPORTS / "print-topic-audit-sample-v2.csv"
OUT_JSONL = REPORTS / "print-topic-audit-sample-v2.jsonl"
OUT_JSON = REPORTS / "print-topic-audit-sample-v2.summary.json"
OUT_MD = REPORTS / "print-topic-audit-sample-v2.md"
SEED = "qibo-print-topic-audit-20260922-v1"

TOPICS = [f"A{i:02d}" for i in range(1, 22)] + ["A00"]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def read_jsonl(path: Path) -> dict[str, dict]:
    result: dict[str, dict] = {}
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                if row.get("id"):
                    result[row["id"]] = row
    return result


def stable_rank(value: str) -> str:
    return hashlib.sha256(f"{SEED}:{value}".encode("utf-8")).hexdigest()


def unique(values):
    result = []
    seen = set()
    for value in values:
        value = str(value or "").strip()
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def ints(value: str) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def main() -> int:
    corpus = read_jsonl(CORPUS)
    candidate_rows = read_csv(CANDIDATES)
    candidates = {row.get("id", ""): row for row in candidate_rows if row.get("id")}
    # The audit queue is regenerated from candidate evidence, but an article
    # already decided in the manual A-topic table must not be shown as an
    # unread pending row in the derived audit copy.  Keep the source table
    # authoritative and only project its decision fields here.
    manual_rows = {
        row.get("id", ""): row
        for row in read_csv(DATA / "print-topic-manual-decisions-v2.csv")
        if row.get("id")
    }
    summaries = {row.get("article_id", ""): row for row in read_csv(NATIVE_SUMMARY) if row.get("article_id")}
    edges = read_csv(NATIVE_EDGES)
    edges_by_article: dict[str, list[dict[str, str]]] = defaultdict(list)
    edges_by_category: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        aid = edge.get("article_id", "")
        cid = edge.get("native_category_id", "")
        if aid:
            edges_by_article[aid].append(edge)
        if cid and aid:
            edges_by_category[cid].append(aid)
    category_rows = read_csv(NATIVE_CATEGORIES)
    category_by_id = {row.get("native_category_id", ""): row for row in category_rows if row.get("native_category_id")}

    # Each set stores (article id, reason).  Selection is deterministic and
    # the union is deduplicated before writing the review queue.
    selected: dict[str, set[str]] = defaultdict(set)

    def add(aid: str, reason: str) -> None:
        if aid in corpus and aid in candidates:
            selected[aid].add(reason)

    def take(ids, reason: str, limit: int | None = None) -> None:
        ordered = sorted(set(ids), key=stable_rank)
        if limit is not None:
            ordered = ordered[:limit]
        for aid in ordered:
            add(aid, reason)

    # 1. New v2 records: all are required in the classification queue.  The
    # fixed 4050 boundary is the source-version boundary used by the rebuild.
    new_ids = [row["id"] for row in candidate_rows if ints(row.get("source_ordinal")) > 4050]
    take(new_ids, "new_v2_all")

    # High-risk candidate rows are explicit strata even when the article is
    # already selected by the new-record rule.  For the old 4,050 records the
    # risk strata are sampled rather than expanded to the full corpus; the
    # new v2 records remain fully queued above.
    risk_ids: dict[str, list[str]] = defaultdict(list)
    for row in candidate_rows:
        aid = row["id"]
        is_new = ints(row.get("source_ordinal")) > 4050
        tie_count = ints(row.get("topic_candidate_tie_count"))
        code_count = len(unique((row.get("topic_candidate_codes") or "").split(";")))
        if tie_count > 1:
            (add if is_new else lambda x, reason: risk_ids[reason].append(x))(aid, "candidate_tie")
        if ints(row.get("topic_candidate_score")) <= 1:
            (add if is_new else lambda x, reason: risk_ids[reason].append(x))(aid, "low_candidate_score")
        # The old concept layer is intentionally broad (often 10+ candidate
        # codes per article).  Treating every such row as a boundary sample
        # would recreate the full corpus queue.  Cross-domain priority is
        # therefore applied to new records, where it is a required review
        # layer; old records enter via bounded tie/status/topic samples.
        if is_new and code_count >= 3:
            add(aid, "cross_domain_candidate")
        if row.get("primary_topic_status") in {"needs_human_classification", "uncertain"}:
            (add if is_new else lambda x, reason: risk_ids[reason].append(x))(aid, "formal_status_pending")
        if row.get("image_review_required", "false").lower() == "true":
            add(aid, "image_review_required")
        if row.get("source_material_status") != "text_present":
            add(aid, "source_material_incomplete")

    # Bounded old-record risk samples are fixed by the same hash seed, so a
    # later rerun changes only when the candidate input changes.
    take(risk_ids["candidate_tie"], "candidate_tie", max(60, math.ceil(len(set(risk_ids["candidate_tie"])) * 0.10)))
    take(risk_ids["low_candidate_score"], "low_candidate_score", None)
    take(risk_ids["formal_status_pending"], "formal_status_pending", max(100, math.ceil(len(set(risk_ids["formal_status_pending"])) * 0.10)))

    # 2. Official coverage: at least one sample per populated LeoPractice;
    # high-frequency practice nodes receive three.  Multi-edge articles and
    # the local-unassigned set receive the fixed minimum required by the
    # framework (30 and 10%, with at least 60 for unassigned).
    populated_categories = {cid: set(aids) for cid, aids in edges_by_category.items() if aids}
    for cid, aids in populated_categories.items():
        take(aids, f"official_practice:{cid}", 1)
    high_frequency = sorted(populated_categories.items(), key=lambda item: (-len(item[1]), item[0]))[:15]
    for cid, aids in high_frequency:
        take(aids, f"official_high_frequency:{cid}", 3)

    multi_ids = [aid for aid, summary in summaries.items() if ints(summary.get("native_category_count")) > 1]
    take(multi_ids, "official_multi_label", 30)
    unassigned_ids = [aid for aid, summary in summaries.items() if summary.get("native_assignment_status") != "confirmed"]
    unassigned_limit = max(60, math.ceil(len(unassigned_ids) * 0.10))
    take(unassigned_ids, "official_unassigned", unassigned_limit)

    # 3. Boundary practice nodes: low old-theme purity is only a risk signal,
    # never a reassignment.  Keep a bounded sample of 40 for review.
    divergent_ids = []
    for cid, category in category_by_id.items():
        if ints(category.get("local_match_count")) >= 5:
            try:
                purity = float(category.get("top_theme_purity") or 0)
            except ValueError:
                purity = 0
            if purity < 0.60:
                divergent_ids.extend(populated_categories.get(cid, set()))
    take(divergent_ids, "official_low_purity_boundary", 40)

    # 4. Ensure every A-topic gets a boundary batch, including A00.  A topic
    # gets up to three deterministic rows from its candidate primary set,
    # with pending/high-risk rows preferred by the global rank below.
    for topic in TOPICS:
        ids = [row["id"] for row in candidate_rows if row.get("primary_print_topic") == topic]
        take(ids, f"topic_boundary:{topic}", 3)

    # Materialize one row per article.  The evidence columns are copied from
    # the candidate layer; they are not silently transformed into decisions.
    rows = []
    for aid in sorted(selected, key=stable_rank):
        candidate = candidates[aid]
        article = corpus[aid]
        article_edges = edges_by_article.get(aid, [])
        paths = unique(edge.get("native_parent_path_names", "") for edge in article_edges)
        roots = unique(path.split(" / ", 1)[0] for path in paths if path)
        reasons = sorted(selected[aid])
        row = {
            "audit_id": f"PTA-{len(rows) + 1:05d}",
            "source_ordinal": candidate.get("source_ordinal", ""),
            "id": aid,
            "title": article.get("title", candidate.get("title", "")),
            "published_at": article.get("publishedAt", ""),
            "audit_strata": ";".join(reasons),
            "primary_print_topic_candidate": candidate.get("primary_print_topic", ""),
            "candidate_topic_codes": candidate.get("topic_candidate_codes", ""),
            "candidate_route_status": candidate.get("candidate_route_status", ""),
            "classification_status": candidate.get("classification_status", candidate.get("primary_topic_status", "")),
            "primary_topic_rule_ids": candidate.get("primary_topic_rule_ids", ""),
            "candidate_topic_rule_ids": candidate.get("candidate_topic_rule_ids", ""),
            "candidate_topic_evidence": candidate.get("candidate_topic_evidence", ""),
            "topic_candidate_score_trace": candidate.get("topic_candidate_score_trace", ""),
            "primary_topic_sources": candidate.get("primary_topic_sources", ""),
            "candidate_tie_count": candidate.get("topic_candidate_tie_count", ""),
            "candidate_score": candidate.get("topic_candidate_score", ""),
            "official_assignment_status": summaries.get(aid, {}).get("native_assignment_status", "unassigned"),
            "official_root_names": ";".join(roots),
            "official_object_practice_paths": ";".join(paths),
            "official_edge_count": str(len(article_edges)),
            "image_count": candidate.get("image_count", "0"),
            "image_review_required": candidate.get("image_review_required", "false"),
            "source_material_status": candidate.get("source_material_status", ""),
            "question": article.get("question", ""),
            "body_excerpt": (article.get("text") or article.get("brief") or "")[:1200],
            "audit_decision": "pending_manual_read",
            "reviewer": "",
            "reviewed_at": "",
            "decision_primary_print_topic": "",
            "decision_secondary_print_topics": "",
            "decision_note": "",
        }
        manual = manual_rows.get(aid)
        if manual:
            status = manual.get("classification_status", "")
            # A provisional decision is still a useful human reading result,
            # but it must remain visibly short of final confirmation.
            if status == "manual_confirmed":
                row["audit_decision"] = "confirmed"
            elif status == "manual_provisional":
                note = f"{manual.get('review_note', '')} {manual.get('decision_basis', '')}"
                row["audit_decision"] = (
                    "needs_image_review"
                    if "图" in note or row["image_review_required"] == "true"
                    else "uncertain"
                )
            else:
                row["audit_decision"] = "uncertain"
            row["reviewer"] = manual.get("reviewer", "")
            row["reviewed_at"] = manual.get("reviewed_at", "")
            row["decision_primary_print_topic"] = manual.get("primary_print_topic_code", "")
            row["decision_secondary_print_topics"] = manual.get("secondary_print_topic_codes", "")
            row["decision_note"] = "; ".join(
                value for value in (
                    manual.get("decision_basis", ""),
                    manual.get("review_note", ""),
                ) if value
            )
        rows.append(row)

    fields = list(rows[0]) if rows else []
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with OUT_JSONL.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    stratum_counts = Counter(reason for row in rows for reason in row["audit_strata"].split(";") if reason)
    summary = {
        "generated_at": datetime.now().astimezone().date().isoformat(),
        "seed": SEED,
        "corpus_records": len(corpus),
        "candidate_records": len(candidate_rows),
        "sample_records": len(rows),
        "unique_sample_ids": len({row["id"] for row in rows}),
        "stratum_counts": dict(sorted(stratum_counts.items())),
        "topic_sample_counts": {topic: sum(f"topic_boundary:{topic}" in row["audit_strata"].split(";") for row in rows) for topic in TOPICS},
        "official_practice_nodes_populated": len(populated_categories),
        "official_unassigned_records": len(unassigned_ids),
        "official_unassigned_target": unassigned_limit,
        "official_multi_label_records": len(multi_ids),
        "image_review_records": sum(row["image_review_required"] == "true" for row in rows),
        "outputs": [str(OUT_CSV), str(OUT_JSONL), str(OUT_JSON), str(OUT_MD)],
        "manual_projected_records": sum(row["audit_decision"] != "pending_manual_read" for row in rows),
        "interpretation": "候选字段仍是机器定位证据；已存在的人工决定会投影到抽样副本，正式分类仍以人工决定表和派生索引为准。",
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 打印主专题人工抽样审计队列（v2）", "",
        f"生成日期：{datetime.now().astimezone().date().isoformat()}；固定种子：`{SEED}`。", "",
        "本队列用于细读、判断和修正，不把机器候选写成定稿。每行须回到问题、正文、官方路径和既有论文路由后再填写决定。", "",
        f"- 语料：{len(corpus):,} 篇；候选行：{len(candidate_rows):,}；抽样去重后：{len(rows):,} 篇。",
        f"- 官方已命中：{len(corpus) - len(unassigned_ids):,}；官方未命中：{len(unassigned_ids):,}；未命中抽样目标：{unassigned_limit:,}。",
        f"- 官方有文章实践节点：{len(populated_categories):,}；每个节点至少抽 1 篇；高频前 15 个节点各最多 3 篇。",
        "",
        "## 抽样层数量", "", "|抽样层|记录数|", "|---|---:|",
    ]
    for key, count in sorted(stratum_counts.items()):
        lines.append(f"|{key}|{count:,}|")
    lines.extend(["", "## 审核字段", "", "- `audit_decision`：`confirmed`、`reassign_needed`、`secondary_only_change`、`candidate_removed`、`native_unassigned_valid`、`needs_image_review`、`uncertain` 或 `pending_manual_read`。", "- `decision_primary_print_topic`：只在回看正文后填写 A00-A21；保留候选时也要显式填写，不能留空。", "- `decision_secondary_print_topics`：填写正文支持的副专题（零至三个），不得包含主专题。", "- `decision_note`：记录中心问题、边界理由和支持该决定的正文段落/短引；引用候选规则时使用 `candidate_topic_rule_ids`。", "- 机器字段如 `candidate_route_status`、`candidate_topic_codes`、`candidate_topic_evidence`、`candidate_score` 只用于定位风险，不是正式结论。", "", "## 输出", "", f"- `{OUT_CSV.name}`：人工填写主表。", f"- `{OUT_JSONL.name}`：同一队列的结构化副本。", f"- `{OUT_JSON.name}`：固定种子和覆盖统计。", ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
