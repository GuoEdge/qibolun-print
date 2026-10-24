#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""初读待办清单：以"是否通过机械验收"为唯一权威口径，输出待办/已完成批次。

用法：
    python3 scripts/worklist.py --status                 # 只统计
    python3 scripts/worklist.py --chunk 48               # 输出下一块待办（每行一个批次号）
    python3 scripts/worklist.py --chunk 48 --json        # JSON 形式（含 size/article_count）
    python3 scripts/worklist.py --retry-failed           # 只列"有 out 文件但未 PASS"的批次

判定：out/<batch>.out.jsonl 存在且 lib_rebuild.validate_batch 通过 = 已完成。
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import BATCH_DIR, REBUILD_ROOT, load_manifest, validate_batch  # noqa: E402

OUT_DIR = os.path.join(REBUILD_ROOT, "out")


def scan():
    man = load_manifest()
    passed, todo, failed = [], [], []
    for b in man["batches"]:
        bid = b["batch_id"]
        outp = os.path.join(OUT_DIR, bid + ".out.jsonl")
        item = {
            "batch": bid,
            "articles": b["article_count"],
            "chars": b["body_chars"],
            "has_out": os.path.exists(outp),
        }
        if not item["has_out"]:
            todo.append(item)
            continue
        ok, res = validate_batch(os.path.join(BATCH_DIR, b["file"]), outp)
        if ok:
            passed.append(item)
        else:
            item["failures"] = (res.get("failures") or [])[:3]
            failed.append(item)
            todo.append(item)
    return man, passed, failed, todo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--chunk", type=int, default=0, help="输出前 N 个待办批次号")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--retry-failed", action="store_true", help="只列有 out 但未 PASS 的批次")
    args = ap.parse_args()

    man, passed, failed, todo = scan()
    if args.status:
        print(
            json.dumps(
                {
                    "batches_total": man["batch_count"] if "batch_count" in man else len(man["batches"]),
                    "passed": len(passed),
                    "failed_existing": len(failed),
                    "todo": len(todo),
                    "articles_passed": sum(x["articles"] for x in passed),
                    "articles_todo": sum(x["articles"] for x in todo),
                    "chars_todo": sum(x["chars"] for x in todo),
                    "failed_batches": [x["batch"] for x in failed],
                },
                ensure_ascii=False,
                indent=1,
            )
        )
        return 0

    pool = failed if args.retry_failed else todo
    sel = pool[args.offset : args.offset + args.chunk] if args.chunk else pool
    if args.json:
        print(json.dumps(sel, ensure_ascii=False))
    else:
        for x in sel:
            print(x["batch"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
