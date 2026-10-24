#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate the A-topic candidate and manual-audit contract.

This check is intentionally structural.  It does not decide an article's
topic and it does not treat a candidate as a confirmed classification.  It
keeps the final print index reproducible by catching invalid topic codes,
duplicate IDs, primary/secondary overlap, incomplete manual decisions and
sampling gaps before a rebuild is consumed by downstream reports.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
CANDIDATES = REPORTS / "print-topic-candidates-v2.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
SAMPLE = REPORTS / "print-topic-audit-sample-v2.csv"
INDEX = REPORTS / "print-index/print-research-index.csv"
OUT_JSON = REPORTS / "print-topic-structure-audit-v2.json"
OUT_MD = REPORTS / "print-topic-structure-audit-v2.md"

FORMAL_STATUSES = {
    "audited", "manual_confirmed", "manual_provisional", "review_required",
    "needs_human_classification", "uncertain",
}
MANUAL_STATUSES = {"manual_confirmed", "manual_provisional"}
AUDIT_DECISIONS = {
    "confirmed", "reassign_needed", "secondary_only_change", "candidate_removed",
    "native_unassigned_valid", "needs_image_review", "uncertain", "pending_manual_read",
}
TOPICS = {f"A{i:02d}" for i in range(22)}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def read_corpus_rows(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if row.get("id"):
                    rows[str(row["id"])] = row
    return rows


def split_codes(value: str) -> list[str]:
    return [x.strip() for x in str(value or "").split(";") if x.strip()]


def duplicate_count(values: list[str]) -> int:
    return len(values) - len(set(values))


def main() -> int:
    candidates = read_csv(CANDIDATES)
    manual = read_csv(MANUAL)
    sample = read_csv(SAMPLE)
    corpus_rows = read_corpus_rows(CORPUS)
    corpus_ids = list(corpus_rows)

    errors: list[str] = []
    warnings: list[str] = []

    candidate_ids = [r.get("id", "") for r in candidates]
    corpus_set = set(corpus_ids)
    candidate_set = set(candidate_ids)
    if duplicate_count(candidate_ids):
        errors.append(f"candidate duplicate IDs: {duplicate_count(candidate_ids)}")
    missing = sorted(corpus_set - candidate_set)
    extra = sorted(candidate_set - corpus_set)
    if missing:
        errors.append(f"candidate IDs missing from corpus: {len(missing)}")
    if extra:
        errors.append(f"candidate IDs absent from corpus: {len(extra)}")
    if len(corpus_ids) != 4305:
        warnings.append(f"corpus record count is {len(corpus_ids)}, expected current v2 baseline 4305")

    candidate_status = Counter(r.get("classification_status", "") for r in candidates)
    invalid_primary: list[str] = []
    invalid_secondary: list[str] = []
    overlap: list[str] = []
    too_many_secondary: list[str] = []
    missing_candidate_evidence: list[str] = []
    for row in candidates:
        aid = row.get("id", "")
        primary = row.get("primary_print_topic", "")
        secondary = split_codes(row.get("secondary_print_topics", ""))
        if primary not in TOPICS:
            invalid_primary.append(aid)
        if any(code not in TOPICS for code in secondary):
            invalid_secondary.append(aid)
        if primary and primary in secondary:
            overlap.append(aid)
        if len(secondary) > 3:
            too_many_secondary.append(aid)
        if row.get("topic_candidate_codes") and not row.get("candidate_topic_rule_ids") and row.get("candidate_route_status") not in {"manual_decision", "concept_only_candidate"}:
            missing_candidate_evidence.append(aid)
        if row.get("classification_status") not in FORMAL_STATUSES:
            errors.append(f"invalid formal candidate status for {aid}: {row.get('classification_status')}")
    if invalid_primary:
        errors.append(f"invalid candidate primary topic codes: {len(invalid_primary)}")
    if invalid_secondary:
        errors.append(f"invalid candidate secondary topic codes: {len(invalid_secondary)}")
    if overlap:
        errors.append(f"candidate primary/secondary overlap: {len(overlap)}")
    if too_many_secondary:
        errors.append(f"candidate rows with >3 secondary topics: {len(too_many_secondary)}")
    if missing_candidate_evidence:
        warnings.append(f"candidate rows with route codes but no rule IDs: {len(missing_candidate_evidence)}")

    manual_ids = [r.get("id", "") for r in manual]
    if duplicate_count(manual_ids):
        errors.append(f"manual decision duplicate IDs: {duplicate_count(manual_ids)}")
    manual_unknown_ids = sorted(set(manual_ids) - candidate_set)
    if manual_unknown_ids:
        errors.append(f"manual decisions absent from candidate layer: {len(manual_unknown_ids)}")
    manual_invalid: list[str] = []
    manual_incomplete: list[str] = []
    manual_title_mismatch: list[str] = []
    manual_overlap: list[str] = []
    for row in manual:
        aid = row.get("id", "")
        primary = row.get("primary_print_topic_code", "")
        secondary = split_codes(row.get("secondary_print_topic_codes", ""))
        status = row.get("classification_status", "")
        if primary not in TOPICS:
            manual_invalid.append(aid)
        if any(code not in TOPICS for code in secondary) or primary in secondary:
            manual_overlap.append(aid)
        if status not in MANUAL_STATUSES:
            errors.append(f"invalid manual status for {aid}: {status}")
        if status in MANUAL_STATUSES and not row.get("decision_basis", "").strip():
            manual_incomplete.append(aid)
        if aid in corpus_rows and row.get("title", "") != str(corpus_rows[aid].get("title") or ""):
            manual_title_mismatch.append(aid)
    if manual_invalid:
        errors.append(f"manual rows with invalid primary topic: {len(manual_invalid)}")
    if manual_overlap:
        errors.append(f"manual primary/secondary overlap or invalid secondary: {len(manual_overlap)}")
    if manual_incomplete:
        errors.append(f"manual confirmed/provisional rows without decision_basis: {len(manual_incomplete)}")
    if manual_title_mismatch:
        errors.append(f"manual titles do not match corpus by ID: {len(manual_title_mismatch)}")

    # The formal index is a derived print surface.  When present, explicit
    # manual decisions must survive derivation exactly, including secondary
    # topics and status.  This catches candidate-layer overwrites that basic
    # code/uniqueness checks cannot see.
    index_rows = read_csv(INDEX)
    if index_rows:
        index_by_id = {row.get("id", ""): row for row in index_rows}
        parity_errors: list[str] = []
        for row in manual:
            aid = row.get("id", "")
            derived = index_by_id.get(aid)
            if not derived:
                parity_errors.append(f"missing formal index row: {aid}")
                continue
            expected_secondary = split_codes(row.get("secondary_print_topic_codes", ""))
            actual_secondary = split_codes(derived.get("secondary_print_topics", ""))
            if row.get("primary_print_topic_code") != derived.get("primary_print_topic"):
                parity_errors.append(f"manual/index primary mismatch: {aid}")
            if expected_secondary != actual_secondary:
                parity_errors.append(f"manual/index secondary mismatch: {aid}")
            if row.get("classification_status") != derived.get("classification_status"):
                parity_errors.append(f"manual/index status mismatch: {aid}")
        if parity_errors:
            errors.extend(parity_errors[:50])
            if len(parity_errors) > 50:
                errors.append(f"additional manual/index parity errors: {len(parity_errors) - 50}")
    else:
        warnings.append("formal index absent; manual/index parity not checked")

    sample_ids = [r.get("id", "") for r in sample]
    if duplicate_count(sample_ids):
        errors.append(f"sample duplicate IDs: {duplicate_count(sample_ids)}")
    sample_unknown = sorted(set(sample_ids) - candidate_set)
    if sample_unknown:
        errors.append(f"sample IDs absent from candidate layer: {len(sample_unknown)}")
    sample_decision_counts = Counter(r.get("audit_decision", "") for r in sample)
    sample_invalid_decisions = [r.get("id", "") for r in sample if r.get("audit_decision", "") not in AUDIT_DECISIONS]
    if sample_invalid_decisions:
        errors.append(f"sample rows with invalid audit_decision: {len(sample_invalid_decisions)}")
    for row in sample:
        decision = row.get("audit_decision", "")
        if decision in {"confirmed", "reassign_needed", "secondary_only_change", "candidate_removed"} and row.get("decision_primary_print_topic", "") not in TOPICS:
            errors.append(f"sample {row.get('id')} has {decision} without valid decision_primary_print_topic")
        if decision in {"confirmed", "reassign_needed", "secondary_only_change", "candidate_removed"} and not row.get("decision_note", "").strip():
            warnings.append(f"sample {row.get('id')} has {decision} without decision_note")

    strata = Counter(reason for row in sample for reason in split_codes(row.get("audit_strata", "")))
    topic_sample_counts = {topic: strata.get(f"topic_boundary:{topic}", 0) for topic in sorted(TOPICS)}
    missing_topic_samples = [topic for topic, count in topic_sample_counts.items() if count == 0]
    if missing_topic_samples:
        errors.append("missing topic boundary samples: " + ",".join(missing_topic_samples))
    official_nodes = len({reason.split(":", 1)[1] for reason in strata if reason.startswith("official_practice:")})
    if official_nodes == 0:
        errors.append("no official practice node appears in sample")
    for topic in ("A12", "A19"):
        count = sum(r.get("primary_print_topic") == topic for r in candidates)
        if count < 10:
            warnings.append(f"{topic} has only {count} candidate primary records; require boundary review and check legacy-route contamination")

    result = {
        "corpus_records": len(corpus_ids),
        "candidate_records": len(candidates),
        "candidate_unique_ids": len(candidate_set),
        "candidate_status_counts": dict(candidate_status),
        "manual_records": len(manual),
        "manual_status_counts": dict(Counter(r.get("classification_status", "") for r in manual)),
        "manual_title_mismatch_count": len(manual_title_mismatch),
        "formal_index_records": len(index_rows),
        "sample_records": len(sample),
        "sample_unique_ids": len(set(sample_ids)),
        "sample_decision_counts": dict(sample_decision_counts),
        "sample_strata_counts": dict(strata),
        "topic_sample_counts": topic_sample_counts,
        "official_practice_nodes_sampled": official_nodes,
        "warnings": warnings,
        "errors": errors,
        "pass": not errors,
        "inputs": [str(CANDIDATES), str(MANUAL), str(SAMPLE), str(CORPUS)],
        "interpretation": "结构 PASS 只表示字段、唯一性和抽样入口可用，不表示文章语义分类已经完成。",
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# 打印主专题结构校验（v2）", "",
        f"结果：{'PASS' if result['pass'] else 'FAIL'}；候选 {len(candidates):,} 行；人工决定 {len(manual):,} 行；抽样 {len(sample):,} 行。", "",
        f"- 候选状态：{dict(candidate_status)}",
        f"- 抽样决定：{dict(sample_decision_counts)}",
        f"- 已覆盖官方实践节点：{official_nodes}",
        "", "## 专题边界抽样", "", "|代码|样本数|", "|---|---:|",
    ]
    lines.extend(f"|{topic}|{topic_sample_counts[topic]}|" for topic in sorted(TOPICS))
    lines.extend(["", "## Errors", ""])
    lines.extend(f"- {item}" for item in errors) if errors else lines.append("- 无")
    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {item}" for item in warnings) if warnings else lines.append("- 无")
    lines.extend(["", "结构 PASS 不等于语义审阅完成；只有填写抽样决定并重建全量索引后，才能把状态提升为人工确认。", ""])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
