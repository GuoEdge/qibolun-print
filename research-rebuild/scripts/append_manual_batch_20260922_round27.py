#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the 2026-09-22 manual full-text review batch (round 27)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"

SPEC = [
    ("fa9ad31e-ce15-5830-8c99-cdbeccfd276f", "礼兵", "A07", "A06;A03", "正文全文；中心是宿舍作息冲突中的自我适应、管理者协调、规则与正式裁决边界，礼不是债或恩。", "正文完整，无图片依赖。"),
    ("e1ff309f-d6e8-5884-8eb4-b6e6ee650cca", "难怪你", "A05", "A09;A01", "正文全文；以猫医疗与费用为切口，中心是亲子代际冲突、家庭财务一体化、子女独立与父母照料秩序。", "医疗场景为副轴，正文完整，无图片依赖。"),
    ("69a3dff6-bb55-5783-96ea-bd33c0c6ba46", "挣钱的技术", "A08", "A04;A07", "正文全文；区分面客与支持面客的挣钱技术，从客户需求和销售过程反推学习与职业技能，中心是劳动市场价值。", "正文完整，无图片依赖。"),
    ("08d7d074-76c1-572b-952b-bb0cd1424c56", "和平嘉奖", "A06", "A12", "正文全文；中心是友谊关系如何在共同挑战中形成，战争与和平是关系条件而非主问题。", "正文完整，无图片依赖。"),
    ("fc4ee94e-b699-51da-bfa1-97ffe234491a", "好好做饭", "A05", "A09", "正文全文；围绕给孩子做饭与家庭日常照料责任，食物安全和健康为副轴。", "正文完整，无图片依赖。"),
    ("25929da3-b62f-5335-b597-8cc0d0c70f2a", "对影成三人", "A04", "A05;A01", "正文全文；以成绩与师生关系冲突为例，中心是教育不能以成绩替代社会能力，并要求培养尊重与合作。", "正文完整，无图片依赖。"),
    ("67231fc3-fd70-534b-b395-840ab39535d3", "通而融", "A07", "A03", "正文全文；中心是职场规则的制定、执行、请示和私下协商，讨论谁有权判定规则不合理。", "正文完整，无图片依赖。"),
    ("727c0c97-781c-56cc-9a91-1a0d7eab4ef2", "正确的强大", "A06", "A04;A01", "正文全文；以异性交往为语境，中心是通过阅历、学习、技能与持续提供乐趣建立亲密关系。", "正文完整，无图片依赖。"),
    ("fedadbd7-2954-5679-ba74-564b76c57363", "生育抑郁", "A02", "A05;A01", "正文全文；中心是孕产身体、性别处境与生育风险的社会保障，伴侣照料和情绪支持为副轴。", "正文完整，无图片依赖。"),
    ("d4833e93-aff8-5846-9e11-a7726d48c410", "石头缝", "A15", "A08;A16", "正文全文；中心是中国电影的审美错位、艺术生产和产业突破，资本市场与媒体认知为副轴。", "正文完整，无图片依赖。"),
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
        status = "manual_confirmed"
        row = {
            "id": aid,
            "title": title,
            "primary_print_topic_code": primary,
            "secondary_print_topic_codes": secondary,
            "classification_status": status,
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
