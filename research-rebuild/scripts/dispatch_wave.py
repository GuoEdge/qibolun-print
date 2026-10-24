#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""波次派发助手：计算待办批次 → 生成子代理任务文件 → 打印可直接复制的启动清单。

用法：
    python3 scripts/dispatch_wave.py --agents 16 --per 2            # 生成任务文件并打印清单
    python3 scripts/dispatch_wave.py --agents 16 --per 2 --list w01 # 只看某个代理的任务文件
    python3 scripts/dispatch_wave.py --status                       # 只统计待办

待办判定（权威）：out/<batch>.out.jsonl 不存在，或存在但未通过 lib_rebuild.validate_batch。
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import BATCH_DIR, REBUILD_ROOT, load_manifest, validate_batch  # noqa: E402
import schedule_batches as S  # noqa: E402

OUT_DIR = os.path.join(REBUILD_ROOT, "out")
INFLIGHT_DIR = os.path.join(REBUILD_ROOT, "prompts", "inflight")


def todo_batches():
    man = load_manifest()
    todo = []
    passed = 0
    for b in man["batches"]:
        outp = os.path.join(OUT_DIR, b["batch_id"] + ".out.jsonl")
        if not os.path.exists(outp):
            todo.append(b["batch_id"])
            continue
        ok, _res = validate_batch(os.path.join(BATCH_DIR, b["file"]), outp)
        if ok:
            passed += 1
        else:
            todo.append(b["batch_id"])
    return todo, passed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agents", type=int, default=16)
    ap.add_argument("--per", type=int, default=2)
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--list")
    ap.add_argument("--offset", type=int, default=0, help="跳过前 N 个待办（避免重复派发在飞批次）")
    ap.add_argument("--tag", default="a", help="本波标签，用于生成不冲突的任务文件名（如 a/b/c）")
    args = ap.parse_args()

    todo, passed = todo_batches()
    if args.status:
        print(json.dumps({"passed": passed, "todo": len(todo), "todo_head": todo[:16]}, ensure_ascii=False))
        return 0

    if args.list:
        path = os.path.join(INFLIGHT_DIR, args.list + ".md")
        print(open(path, encoding="utf-8").read() if os.path.exists(path) else "缺少 %s" % path)
        return 0

    todo = todo[args.offset :]
    groups = [todo[i * args.per : (i + 1) * args.per] for i in range(args.agents)]
    os.makedirs(INFLIGHT_DIR, exist_ok=True)
    rows = []
    for i, g in enumerate(groups, 1):
        if not g:
            break
        agent = "%s%02d" % (args.tag, i)
        path = os.path.join(INFLIGHT_DIR, agent + ".md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(S.PROMPT_TEMPLATE.format(batches="、".join(g)))
        rows.append({"agent": agent, "batches": g, "prompt_file": path})
    with open(os.path.join(REBUILD_ROOT, "reports", "wave-manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1)
    print(json.dumps({"passed": passed, "todo": len(todo), "agents": rows}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
