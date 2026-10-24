#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次调度器：按"已完成/待处理"生成波次分配与子代理启动指令。

用法：
    python3 scripts/schedule_batches.py --status                  # 总体进度
    python3 scripts/schedule_batches.py --next --size 3 --waves 8 # 生成下一波分配
    python3 scripts/schedule_batches.py --next --size 3 --waves 8 --prompts  # 同时打印启动提示词
    python3 scripts/schedule_batches.py --mark-done r001-b0005    # 手工标记
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
RECORDS_DIR = os.path.join(REBUILD_ROOT, "records")
STATE_PATH = os.path.join(REBUILD_ROOT, "reports", "scheduler-state.json")

PROMPT_TEMPLATE = """你是"岐伯论"独立重建项目的初读执行代理。请完成以下批次的全量初读记录：{batches}。
本任务只做一个批次；请逐篇填写并**每 1—2 篇就落盘一次**（edit 追加），不要攒到最后一次性写完。
开工前先跑 `python3 scripts/build_batch.py <batch> --check`：已 PASS 就直接回报；已有非空 uid 条目一律保留不重写。

第一步（必须）：完整阅读 /mnt/d/岐伯论/research-rebuild/prompts/initial-reading-brief.md，严格按其中"第一部分的固定流程"逐批执行。骨架已预生成在 records/<batch>.sessions.py（配套 <batch>.skeleton.json），只填 ANALYSIS，不要运行 build_sessions.py。

对每个批次依次执行，直到 python3 scripts/build_batch.py <batch> 输出 "status": "PASS"：
1) python3 scripts/render_batch.py <batch>    # 渲染并读完该批全部文章（提问/正文/结构/图片）
2) 填写 records/<batch>.sessions.py 的 ANALYSIS（key = 骨架里的 uid）
3) python3 scripts/build_batch.py <batch>     # 生成 + 机械验收；FAIL 就按清单修复后重跑

硬性约束：只处理被指派的批次；不得修改 scripts/ 下的公共脚本；不得改写原始语料 sooon-q9adg-articles-v2.jsonl；evidence 的 quote 必须是所引段落原文的连续片段（逐字一致，含中文引号）；提问者立场不得归给作者，被反驳观点用 opponent_view + attribution=opponent；保留否定/反问/假设/条件/限定语气；没有的内容用空数组或写"本文未说明"，不得臆测补全；有图片的文章按简报第 4 节标 needs_reread + image_checked=false 并在 notes 说明。

全部批次 PASS 后，按简报第 6 节格式回报（每批不超过 6 行）：批次号、验收结果、status 分布、写作要点、遗留疑点。不要输出 JSONL 本身。"""


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    return {"completed": [], "assigned": {}}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=1)


def completed_batches():
    man = load_manifest()
    done = []
    for b in man["batches"]:
        outp = os.path.join(OUT_DIR, b["batch_id"] + ".out.jsonl")
        if not os.path.exists(outp):
            continue
        ok, _result = validate_batch(os.path.join(BATCH_DIR, b["file"]), outp)
        if ok:
            done.append(b["batch_id"])
    return done


def status():
    man = load_manifest()
    total = len(man["batches"])
    done = completed_batches()
    state = load_state()
    assigned = state.get("assigned", {})
    pending = [b["batch_id"] for b in man["batches"] if b["batch_id"] not in done]
    inflight = sorted(set(assigned) - set(done))
    return {
        "batches_total": total,
        "batches_done": len(done),
        "batches_pending": len(pending),
        "batches_assigned_inflight": len(inflight),
        "pending_head": pending[:20],
        "pending_tail": pending[-5:],
    }


def next_wave(size, waves):
    man = load_manifest()
    order = [b["batch_id"] for b in man["batches"]]
    done = set(completed_batches())
    state = load_state()
    assigned = state.get("assigned", {})
    inflight = set(assigned) - done
    pending = [b for b in order if b not in done and b not in inflight]
    per_agent = max(1, size)
    agents = []
    for i in range(waves):
        chunk = pending[i * per_agent : (i + 1) * per_agent]
        if not chunk:
            break
        agents.append(chunk)
        for b in chunk:
            assigned[b] = "wave-%d-agent-%d" % (len(state.get("waves", [])) + 1, i + 1)
    state["assigned"] = {b: agent for b, agent in assigned.items() if b not in done}
    waves_list = state.setdefault("waves", [])
    waves_list.append({"wave": len(waves_list) + 1, "agents": agents})
    save_state(state)
    return agents


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--next", action="store_true")
    ap.add_argument("--size", type=int, default=3)
    ap.add_argument("--waves", type=int, default=8)
    ap.add_argument("--prompts", action="store_true")
    ap.add_argument("--mark-done", nargs="*")
    args = ap.parse_args()

    if args.mark_done:
        state = load_state()
        for b in args.mark_done:
            if b not in state["completed"]:
                state["completed"].append(b)
        save_state(state)

    if args.status or (not args.next and not args.mark_done):
        print(json.dumps(status(), ensure_ascii=False, indent=1))

    if args.next:
        agents = next_wave(args.size, args.waves)
        print(json.dumps({"agents": agents, "batches": sum(len(a) for a in agents)}, ensure_ascii=False))
        if args.prompts:
            for i, chunk in enumerate(agents, 1):
                print("\n===== AGENT %d =====" % i)
                print(PROMPT_TEMPLATE.format(batches="、".join(chunk)))


if __name__ == "__main__":
    main()
