#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""质量评估（启发式，供研究者复核前快速筛检）。

统计每批/全语料的记录结构丰富度，并列出可能需要注意的记录：
- 主张、内容单元、概念、例证、条件、未决问题的数量分布；
- 只有提问者立场而没有作者主张（attribution 全为 questioner/opponent）；
- 无任何 evidence_refs；
- needs_reread / blocked 的记录（应逐条人工看原因）；
- 分析字段全空（question_context 为空）。

用法：
    python3 scripts/quality_report.py                 # 汇总 + 异常清单
    python3 scripts/quality_report.py --batch X        # 单批明细
    python3 scripts/quality_report.py --out X.json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import BATCH_DIR, REBUILD_ROOT, load_manifest, validate_batch  # noqa: E402

OUT_DIR = os.path.join(REBUILD_ROOT, "out")
RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")


def load_valid_records():
    man = load_manifest()
    records = []
    invalid_batches = []
    for b in man["batches"]:
        path = os.path.join(OUT_DIR, b["batch_id"] + ".out.jsonl")
        if not os.path.exists(path):
            continue
        ok, _result = validate_batch(os.path.join(BATCH_DIR, b["file"]), path)
        if not ok:
            invalid_batches.append(b["batch_id"])
            continue
        for line in open(path, encoding="utf-8"):
            if line.strip():
                records.append((b["batch_id"], json.loads(line)))
    return records, invalid_batches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch")
    ap.add_argument("--out")
    args = ap.parse_args()

    totals = {
        "records": 0,
        "with_claims": 0,
        "no_claims": 0,
        "no_evidence": 0,
        "empty_question_context": 0,
        "needs_reread": 0,
        "blocked": 0,
        "image_articles_pending": 0,
    }
    sums = {"claims": 0, "units": 0, "concepts": 0, "examples": 0, "conditions": 0, "unresolved": 0}
    flags = []
    records, invalid_batches = load_valid_records()
    for batch_id, r in records:
        if args.batch and batch_id != args.batch:
            continue
        totals["records"] += 1
        a = r.get("analysis") or {}
        claims = a.get("main_claims") or []
        units = a.get("content_units") or []
        sums["claims"] += len(claims)
        sums["units"] += len(units)
        sums["concepts"] += len(a.get("concept_usage") or [])
        sums["examples"] += len(a.get("examples_and_targets") or [])
        sums["conditions"] += len(a.get("conditions") or [])
        sums["unresolved"] += len(a.get("unresolved_questions") or [])
        if claims:
            totals["with_claims"] += 1
        else:
            totals["no_claims"] += 1
        if not (r.get("evidence_refs") or []):
            totals["no_evidence"] += 1
        if not str(a.get("question_context") or "").strip():
            totals["empty_question_context"] += 1
        st = str((r.get("reading") or {}).get("status"))
        if st == "needs_reread":
            totals["needs_reread"] += 1
            flags.append((batch_id, r["article_id"], "needs_reread", str(r.get("notes"))[:100]))
        if st == "blocked":
            totals["blocked"] += 1
            flags.append((batch_id, r["article_id"], "blocked", str(r.get("notes"))[:100]))
        for im in (r.get("structure") or {}).get("images") or []:
            if str(im.get("status")) == "pending":
                totals["image_articles_pending"] += 1
                break
        if not claims and not units:
            flags.append((batch_id, r["article_id"], "empty_analysis", str(r.get("metadata", {}).get("title"))))
        elif claims and all(
            str(c.get("attribution")) in ("questioner", "opponent") for c in claims
        ):
            flags.append(
                (batch_id, r["article_id"], "no_author_claim", str(r.get("metadata", {}).get("title")))
            )

    n = max(1, totals["records"])
    summary = {
        "records": totals["records"],
        "avg_claims": round(sums["claims"] / n, 2),
        "avg_content_units": round(sums["units"] / n, 2),
        "avg_concepts": round(sums["concepts"] / n, 2),
        "avg_examples": round(sums["examples"] / n, 2),
        "avg_conditions": round(sums["conditions"] / n, 2),
        "avg_unresolved": round(sums["unresolved"] / n, 2),
        **totals,
        "invalid_batches_excluded": len(invalid_batches),
        "invalid_batch_ids": invalid_batches,
        "flags": len(flags),
    }
    result = {"summary": summary, "flagged": flags[:500]}
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, ensure_ascii=False, indent=1)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    for f in flags[:20]:
        print("  %-14s %s %s %s" % (f[0], f[2], f[1][:8], f[3][:60]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
