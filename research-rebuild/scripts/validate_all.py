#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全批次机械验收：逐批调用 lib_rebuild.validate_batch，汇总为报告。

用法：
    python3 scripts/validate_all.py                 # 验收所有已有输出的批次
    python3 scripts/validate_all.py --batch r001-b0001
    python3 scripts/validate_all.py --report reports/validation-report.json
    python3 scripts/validate_all.py --aggregate     # 通过验收的批次汇总为 records/reading-records-v2.jsonl

验收通过的判定：该批 out/<batch>.out.jsonl 存在，且 lib_rebuild.validate_batch 返回 PASS。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import (  # noqa: E402
    BATCH_DIR,
    REBUILD_ROOT,
    load_manifest,
    read_jsonl,
    validate_batch,
)

OUT_DIR = os.path.join(REBUILD_ROOT, "out")
RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch")
    ap.add_argument("--report", default=os.path.join(REBUILD_ROOT, "reports", "validation-report.json"))
    ap.add_argument("--aggregate", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    man = load_manifest()
    batches = man["batches"]
    if args.batch:
        want = args.batch if args.batch.endswith(".jsonl") else args.batch + ".jsonl"
        batches = [b for b in batches if b["file"] == want or b["batch_id"] == args.batch]
        if not batches:
            print("找不到批次 %s" % args.batch)
            return 2

    t0 = time.time()
    results = []
    passed = failed = missing = 0
    status_counter = {}
    articles_done = 0
    for b in batches:
        inp = os.path.join(BATCH_DIR, b["file"])
        outp = os.path.join(OUT_DIR, b["batch_id"] + ".out.jsonl")
        if not os.path.exists(outp):
            missing += 1
            results.append(
                {"batch_id": b["batch_id"], "status": "MISSING", "failures": [], "warnings": []}
            )
            continue
        ok, res = validate_batch(inp, outp)
        rec = {
            "batch_id": b["batch_id"],
            "status": res["status"],
            "input_records": res["input_records"],
            "output_records": res["output_records"],
            "failures": res["failures"],
            "warnings": res["warnings"],
        }
        results.append(rec)
        if ok:
            passed += 1
            articles_done += res["output_records"]
            for line in open(outp, encoding="utf-8"):
                if line.strip():
                    r = json.loads(line)
                    st = str((r.get("reading") or {}).get("status"))
                    status_counter[st] = status_counter.get(st, 0) + 1
        else:
            failed += 1

    summary = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "batches_total": len(batches),
        "batches_passed": passed,
        "batches_failed": failed,
        "batches_missing": missing,
        "articles_in_passed_batches": articles_done,
        "reading_status_counts": status_counter,
        "elapsed_sec": round(time.time() - t0, 2),
        "result": "PASS" if failed == 0 and missing == 0 else "INCOMPLETE",
    }
    report = {"summary": summary, "batches": results}
    os.makedirs(os.path.dirname(args.report), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)

    if not args.quiet:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        for r in results:
            if r["status"] != "PASS":
                print("  %-14s %s" % (r["batch_id"], r["status"]))
                for f in r["failures"][:5]:
                    print("      %s" % f)

    if args.aggregate and failed == 0 and missing == 0:
        os.makedirs(RECORDS_DIR, exist_ok=True)
        agg = os.path.join(RECORDS_DIR, "reading-records-v2.jsonl")
        n = 0
        with open(agg, "w", encoding="utf-8") as fh:
            for b in batches:
                outp = os.path.join(OUT_DIR, b["batch_id"] + ".out.jsonl")
                if not os.path.exists(outp):
                    continue
                for line in open(outp, encoding="utf-8"):
                    if line.strip():
                        fh.write(line if line.endswith("\n") else line + "\n")
                        n += 1
        print("aggregated %d records -> %s" % (n, agg))

    return 0 if (failed == 0 and missing == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
