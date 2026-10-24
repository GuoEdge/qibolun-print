#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
fields = ["id", "title", "primary_print_topic_code", "secondary_print_topic_codes", "classification_status", "decision_basis", "review_note", "reviewer", "reviewed_at"]
rows = [
    ("1fe28dda-3e35-5a05-95bc-18612f2078c5", "母亲节", "A05", "A06;A08", "manual_confirmed", "正文中心是成年子女如何理解母亲的情感期待、经济帮助与陪伴边界", "亲情表达和旅行消费是关系与市场副轴；不把节日消费简单等同于孝道", "main-thread", "2026-09-22"),
    ("722b34b8-6c9e-5435-9be9-03535d8395d3", "why so serious", "A08", "A07;A06", "manual_confirmed", "正文中心是鞋业供应链、稳定生产关系与成本/风险如何塑造行业结构", "企业协作和长期关系为副轴；机器 A07 不足以覆盖市场成本主线", "main-thread", "2026-09-22"),
    ("ef2aeee8-4846-58d5-974c-79ee15246340", "我家保", "A07", "A05;A04", "manual_confirmed", "正文中心是职场沟通、组织评价和个人能力在家庭牵挂与工作责任之间的边界处理", "家庭与教育经历是背景；行动建议围绕工作组织与专业能力", "main-thread", "2026-09-22"),
    ("0acc13b7-01f6-5e8e-a801-867219041fab", "对话", "A12", "A03;A06", "manual_confirmed", "正文中心是国际政治争论中如何保持对等、证据化和可继续对话的外交秩序", "论证规则与对话关系为副轴；不是一般亲密关系冲突", "main-thread", "2026-09-22"),
    ("a4123e76-a713-521b-998d-796705667af7", "权力之巅", "A20", "A12;A03", "manual_confirmed", "正文中心是历史权力、政治阴谋与人物评价如何被叙述和重新解释", "战争/政权材料和事实论证为副轴；主轴是历史文明的历时评论", "main-thread", "2026-09-22"),
    ("a792c667-5952-5a57-8897-8b31b4c451bd", "成年后", "A05", "A01;A08", "manual_confirmed", "正文中心是成年子女照料父母、恢复生活秩序并建立可持续生计与家庭责任", "心理压力和赚钱能力为副轴；家庭代际责任是行动中心", "main-thread", "2026-09-22"),
]
with path.open(encoding="utf-8-sig", newline="") as f:
    existing = list(csv.DictReader(f))
seen = {r["id"] for r in existing}
new = [dict(zip(fields, r)) for r in rows if r[0] not in seen]
if new:
    with path.open("a", encoding="utf-8-sig", newline="") as f:
        csv.DictWriter(f, fieldnames=fields).writerows(new)
print({"existing": len(existing), "candidate_rows": len(rows), "appended": len(new), "total": len(existing)+len(new)})
