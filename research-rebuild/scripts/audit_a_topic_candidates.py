#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit and sample the A-topic candidate layer.

The candidate table is intentionally provisional.  This report checks its
structural coverage and emits a deterministic, stratified reading sample; it
does not promote any row to a final research classification.
"""

from __future__ import annotations

import csv
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
INPUT = REPORTS / "a-topic-candidates-v2.csv"
OUT_CSV = REPORTS / "a-topic-candidate-review-sample-v2.csv"
OUT_JSON = REPORTS / "a-topic-candidate-audit-v2.json"
OUT_MD = REPORTS / "a-topic-candidate-audit-v2.md"

SEED = 20260922
TOPICS = [f"A{i:02d}" for i in range(1, 22)]
VALID_TOPICS = set(TOPICS) | {"A00"}


def read_rows() -> list[dict[str, str]]:
    with INPUT.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def sample_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rng = random.Random(SEED)
    by_topic: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_status: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_topic[row.get("primary_print_topic", "")].append(row)
        by_status[row.get("classification_status", "")].append(row)
    chosen: dict[str, dict[str, str]] = {}

    def take(pool: list[dict[str, str]], count: int) -> None:
        pool = list(pool)
        rng.shuffle(pool)
        for row in pool[:count]:
            chosen[row["id"]] = row

    # Every topic gets a baseline sample, including low-volume A12/A17/A19.
    for topic in TOPICS + ["A00"]:
        take(by_topic.get(topic, []), 5)
    # Conflicts and unassigned/legacy queues are the high-risk strata.
    take(by_status.get("strong_domain_conflict", []), 40)
    take(by_status.get("official_multi", []), 30)
    take(by_status.get("legacy_needs_human", []), 20)
    take(by_status.get("legacy_route", []), 10)
    take(by_status.get("official_direct", []), 20)
    # Keep rows that have no official path visible in the review queue.
    take([r for r in rows if not r.get("official_paths")], 30)
    return sorted(chosen.values(), key=lambda r: int(r.get("source_ordinal") or 0))


def main() -> None:
    rows = read_rows()
    ids = [r.get("id", "") for r in rows]
    topic_counts = Counter(r.get("primary_print_topic", "") for r in rows)
    status_counts = Counter(r.get("classification_status", "") for r in rows)
    official_counts = Counter(r.get("official_assignment_status", "") for r in rows)
    strong_counts = Counter()
    for row in rows:
        for topic in (row.get("strong_domain_topics") or "").split(";"):
            if topic:
                strong_counts[topic] += 1
    sample = sample_rows(rows)
    sample_fields = [
        "sample_id", "stratum", "source_ordinal", "id", "title",
        "primary_print_topic", "secondary_print_topics", "classification_status",
        "strong_domain_topics", "strong_domain_hits", "official_paths",
        "legacy_paper_routes", "legacy_concepts", "question", "classification_note",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=sample_fields)
        writer.writeheader()
        for index, row in enumerate(sample, 1):
            topic = row.get("primary_print_topic", "")
            status = row.get("classification_status", "")
            if status == "strong_domain_conflict":
                stratum = "strong_domain_conflict"
            elif not row.get("official_paths"):
                stratum = "official_unassigned"
            elif status in {"official_multi", "legacy_needs_human"}:
                stratum = status
            else:
                stratum = f"topic_{topic}"
            output = {field: row.get(field, "") for field in sample_fields}
            output["sample_id"] = f"ATC-{index:04d}"
            output["stratum"] = stratum
            writer.writerow(output)

    duplicate_ids = len(ids) - len(set(ids))
    invalid_topics = sorted(set(topic_counts) - VALID_TOPICS)
    empty_primary = sum(not r.get("primary_print_topic") for r in rows)
    result = {
        "input": str(INPUT),
        "records": len(rows),
        "unique_ids": len(set(ids)),
        "duplicate_ids": duplicate_ids,
        "empty_primary": empty_primary,
        "invalid_primary_topics": invalid_topics,
        "primary_topic_counts": dict(topic_counts),
        "missing_primary_topics": [topic for topic in TOPICS if not topic_counts.get(topic)],
        "classification_status_counts": dict(status_counts),
        "official_assignment_status_counts": dict(official_counts),
        "strong_domain_topic_counts": dict(strong_counts),
        "strong_domain_rows": sum(bool(r.get("strong_domain_topics")) for r in rows),
        "sample_records": len(sample),
        "sample_seed": SEED,
        "sample_strata_counts": dict(Counter(
            "strong_domain_conflict" if r.get("classification_status") == "strong_domain_conflict"
            else "official_unassigned" if not r.get("official_paths")
            else r.get("classification_status", "")
            for r in sample
        )),
        "outputs": [str(OUT_CSV), str(OUT_JSON), str(OUT_MD)],
        "interpretation": "结构覆盖通过不等于语义分类完成；抽样行必须回到正文、图片和官方实践边逐篇确认。",
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# A01–A21 / A00 主专题候选层审计",
        "",
        "本报告审计 `a-topic-candidates-v2.csv` 的 A01–A21 专题及 A00 待审占位结构覆盖和抽样入口，不把机器候选升级为正式研究结论。",
        "",
        f"- 记录：{len(rows)}；唯一 ID：{len(set(ids))}；重复 ID：{duplicate_ids}",
        f"- 空主专题：{empty_primary}；非法主专题：{len(invalid_topics)}；固定抽样种子：{SEED}",
        f"- 强领域线索记录：{result['strong_domain_rows']}；抽样记录：{len(sample)}",
        "",
        "## 主专题覆盖",
        "",
        "|代码|文章数|",
        "|---|---:|",
    ]
    for topic in TOPICS:
        lines.append(f"|{topic}|{topic_counts.get(topic, 0)}|")
    lines += [
        "",
        "## 状态",
        "",
        "|状态|文章数|",
        "|---|---:|",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"|{status}|{count}|")
    lines += [
        "",
        "## 使用抽样表",
        "",
        "`a-topic-candidate-review-sample-v2.csv` 按 A01–A21、A00、强领域冲突、官方多标签、官方未分配和旧论文路由风险分层。优先细读 `strong_domain_conflict`，再抽查每个低频专题和官方路径过宽的样本。",
        "",
        "强领域线索只用于发现泛官方路径覆盖问题；正文中心问题、连续论证和必要的图像证据仍是人工确认主专题的依据。",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
