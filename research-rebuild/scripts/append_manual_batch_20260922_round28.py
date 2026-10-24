#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the 2026-09-22 manual full-text review batch (round 28)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"

SPEC = [
    (
        "47dae311-6f5a-59fb-a758-d472dd903653",
        "不熟人",
        "A01",
        "A03",
        "正文中心是向内自省、自我认知与主体经验，镜子和自我对话说明已有认知框架内仍可产生认识。",
        "证据：‘对镜自照…你和自己并不熟’；AI仅在提问中出现，正文未展开AI技术或共存；官方未分配。",
    ),
    (
        "d93b79fe-bbc6-59ce-b310-3442b586de5e",
        "situationship",
        "A06",
        "A02;A01",
        "全文定义暧昧或不稳定亲密关系、承诺撤回、嫉妒与关系终止，核心是亲密关系与婚恋。",
        "证据：‘不排除性的暧昧关系’、‘进入了倒计时的暧昧关系’；性接触与同意、心理痛苦为副轴。",
    ),
    (
        "a68cfedd-8526-57a1-8049-c01f929abca3",
        "不是缺钾",
        "A01",
        "A06;A08;A09",
        "正文不做钾流失医学解释，中心是吃播或猎奇风险、名利刺激、孤独与爱作为生命保护，结论是人死于缺少这样的爱而非缺钾。",
        "证据：‘只有真正的爱是你健康的最后保险’、‘人是死于缺少这样的爱，不是缺钾’；机器A09主类由医疗设问触发。",
    ),
    (
        "8cd6313f-bb71-5922-b2dd-9b5692911dd6",
        "三岁",
        "A05",
        "A10;A04",
        "连续论证集中三岁儿童发展、母亲监护或养育责任与严重过失依据，核心是家庭亲子照护。",
        "证据：‘三岁是一个特别危险的年龄’、‘作为母亲…法院判定严重过失的基本依据’；机器A18把儿童或环境词面误作自然科学。",
    ),
    (
        "c037b709-70ab-5d89-952e-9cdc4ee7f924",
        "热的路",
        "A01",
        "A06;A05",
        "全文讨论价值感、被在乎、爱与冷漠循环及主体如何通过付出或信念获得关系安全，中心是心理主体与情绪劳动。",
        "证据：‘在你的父母、爱人、子女、挚友眼里…都有无可舍弃的价值’、‘冷漠导致冷漠，爱引发爱’；关系对象仅为副轴。",
    ),
    (
        "79913101-5fe4-5314-92b0-8886bf78f791",
        "七岁",
        "A04",
        "A05",
        "正文主体是六至七岁儿童语言、记忆、纪律、身体和学前教育准备，以及家长如何安排活动或教育。",
        "证据：‘词汇量大到足以构建长期记忆和服从秩序的分界点，就是6岁-7岁’、‘七岁之前…让孩子先玩好’；家庭监护为应用场景，A18仅为博物馆或标本触发场景，故不列副专题。",
    ),
    (
        "a10c2520-08a7-5d24-92d3-c25e343b4c7d",
        "和气生财神",
        "A08",
        "A12;A20",
        "文章解释和平或秩序如何扩大钱的效力、市场交换和拜金主义，核心是财富市场逻辑。",
        "证据：‘一切向钱看的前提，是钱有大用’、‘和平提供的确定性，天然的刺激拜金主义’；世界大战是形成条件。",
    ),
    (
        "fa45750e-5cfb-5f5f-bd13-321f8caf89ff",
        "夺门而入",
        "A12",
        "A13;A20",
        "全文讨论古代攻城的军事行动逻辑，包括攻墙、夺门、城防、云梯、地道和后援通道，核心是战争与军事。",
        "证据：‘攻城的常规逻辑是“攻墙，夺门”，而不是“攻门”’；工程技术和古代历史为副轴。",
    ),
]


def main() -> int:
    with PATH.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fields = list(reader.fieldnames or [])
    by_id = {row.get("id", ""): row for row in rows}
    added = 0
    updated = 0
    for aid, title, primary, secondary, basis, note in SPEC:
        confirmed_ids = {
            "47dae311-6f5a-59fb-a758-d472dd903653",
            "d93b79fe-bbc6-59ce-b310-3442b586de5e",
            "a68cfedd-8526-57a1-8049-c01f929abca3",
            "8cd6313f-bb71-5922-b2dd-9b5692911dd6",
            "a10c2520-08a7-5d24-92d3-c25e343b4c7d",
            "fa45750e-5cfb-5f5f-bd13-321f8caf89ff",
        }
        row = {
            "id": aid,
            "title": title,
            "primary_print_topic_code": primary,
            "secondary_print_topic_codes": secondary,
            "classification_status": "manual_confirmed" if aid in confirmed_ids else "manual_provisional",
            "decision_basis": basis,
            "review_note": note,
            "reviewer": "main-thread",
            "reviewed_at": "2026-09-22",
        }
        if aid in by_id:
            if by_id[aid] != row:
                by_id[aid].update(row)
                updated += 1
        else:
            rows.append(row)
            by_id[aid] = row
            added += 1
    with PATH.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"added={added} updated={updated} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
