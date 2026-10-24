#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
fields = ["id", "title", "primary_print_topic_code", "secondary_print_topic_codes", "classification_status", "decision_basis", "review_note", "reviewer", "reviewed_at"]
rows = [
    ("358deb28-06ba-5a5f-b6f9-a9b09864a1ac", "兔子与斗鸡", "A04", "A01;A07", "manual_confirmed", "正文中心是新人从焦虑、依赖指导到职业能力与成熟人格形成的学徒式学习路径", "心理不安和团队合作是形成机制；主轴是职业学习与能力成长", "main-thread", "2026-09-22"),
    ("72e969b8-57eb-55d9-b66f-afd4ad01c288", "第二春", "A08", "A01;A07", "manual_confirmed", "正文中心是房产损失后重新进入劳动、修复收入与生活选择的财富和生计问题", "心理韧性与职业行动为副轴；主轴是财产损失后的经济路径", "main-thread", "2026-09-22"),
    ("4090ce55-1932-562d-9b91-c31bfd8ca365", "老人的战争", "A14", "A04;A05;A12", "manual_confirmed", "正文中心是 AI、机器人和劳动技术改变代际交替、生育与社会化教育结构的未来秩序", "教育、家庭和人口政治为副轴；机器技术是引发结构变化的主轴", "main-thread", "2026-09-22"),
    ("dcdf558b-311b-57a2-980b-0af5fa8092e8", "无缘故", "A03", "A01;A10", "manual_confirmed", "正文中心是‘无缘无故’这一归因表达如何遮蔽因果、责任和对方主体性", "心理防御和冲突秩序为副轴；主问题是概念与论证边界", "main-thread", "2026-09-22"),
    ("bd990aaa-424d-55e4-a66f-4b7ff240b28c", "和气生财", "A08", "A07;A10", "manual_confirmed", "正文中心是健身房经营规则、外来服务占用场地与商业生计之间的公平边界", "组织管理和规则责任为副轴；商业伦理与经营可持续性是主轴", "main-thread", "2026-09-22"),
    ("9229f485-68c9-5212-ae2e-9e8e051c5d89", "无名氏", "A05", "A01;A06", "manual_confirmed", "正文中心是家庭成员在亲情关系中建立照料、独立和边界的责任安排", "心理压力和亲密关系为副轴；家庭代际责任是中心", "main-thread", "2026-09-22"),
]
with path.open(encoding="utf-8-sig", newline="") as f:
    existing = list(csv.DictReader(f))
seen = {r["id"] for r in existing}
new = [dict(zip(fields, r)) for r in rows if r[0] not in seen]
if new:
    with path.open("a", encoding="utf-8-sig", newline="") as f:
        csv.DictWriter(f, fieldnames=fields).writerows(new)
print({"existing": len(existing), "candidate_rows": len(rows), "appended": len(new), "total": len(existing) + len(new)})
