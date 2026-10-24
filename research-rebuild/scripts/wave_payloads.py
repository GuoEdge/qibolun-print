#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 scheduler-state.json 读取"已分配但未完成"的批次，按代理分组输出启动载荷。

用法：
    python3 scripts/wave_payloads.py --json      # 输出 [{agent, batches, prompt}, ...]
    python3 scripts/wave_payloads.py             # 人类可读
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib_rebuild import REBUILD_ROOT  # noqa: E402
from schedule_batches import PROMPT_TEMPLATE, completed_batches  # noqa: E402

STATE_PATH = os.path.join(REBUILD_ROOT, "reports", "scheduler-state.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    with open(STATE_PATH, encoding="utf-8") as fh:
        state = json.load(fh)
    assigned = state.get("assigned", {})
    done = set(completed_batches())
    groups = {}
    for batch, agent in assigned.items():
        if batch in done:
            continue
        groups.setdefault(agent, []).append(batch)
    payloads = []
    for agent, batches in groups.items():
        batches.sort()
        payloads.append(
            {
                "agent": agent,
                "batches": batches,
                "description": "Initial reading %s" % batches[0][-4:],
                "prompt": PROMPT_TEMPLATE.format(batches="、".join(batches)),
            }
        )
    payloads.sort(key=lambda p: p["batches"][0])
    if args.json:
        print(json.dumps(payloads, ensure_ascii=False, indent=1))
    else:
        for p in payloads:
            print("%-18s %s" % (p["agent"], " ".join(p["batches"])))


if __name__ == "__main__":
    main()
