#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
fields = ["id", "title", "primary_print_topic_code", "secondary_print_topic_codes", "classification_status", "decision_basis", "review_note", "reviewer", "reviewed_at"]
rows = [
    ("bfb53974-f062-5602-97a4-8cffc8d98c96", "你父我母", "A06", "A01;A02", "manual_confirmed", "正文中心是亲密关系中语言伤害、权力互相模仿和如何停止报复循环", "性别话语和情绪边界为副轴；核心是恋爱关系的可持续性", "main-thread", "2026-09-22"),
    ("c8e7c217-514b-5f9f-8279-699b3d60c9ea", "the rule of hope", "A06", "A01;A11", "manual_confirmed", "正文中心是亲密关系中一方希望依靠另一方时，承诺、能力与责任边界如何成立", "心理依赖和宗教式誓言为副轴；机器 A14 不应因英文文本或抽象表达而主导", "main-thread", "2026-09-22"),
    ("05064ec8-bff4-5aa6-9a2e-8fda573ce6a4", "无忌", "A05", "A01;A03", "manual_confirmed", "正文中心是亲子关系中如何理解爱、允许彼此优先照顾自己并解除相互债务逻辑", "主体边界和定义论证为副轴；不是单纯心理疗愈", "main-thread", "2026-09-22"),
    ("62c38852-3bde-54a5-9b56-d985263a6e44", "目标是你", "A05", "A04;A20", "manual_confirmed", "正文中心是父母与孩子共同学习历史、共同面对无知并形成学习方法的代际教育关系", "教育方法和历史材料为副轴；主轴是亲子引导", "main-thread", "2026-09-22"),
    ("ae795551-d487-5999-abb9-2c6bfedd6df0", "无私之友", "A06", "A08;A01", "manual_confirmed", "正文中心是不同教育和阶层背景的旧友如何通过共同活动维持平等、纯粹的友谊", "经济阶层与心理韧性为副轴；关系对象是友谊而非市场合作", "main-thread", "2026-09-22"),
    ("283f6975-e3ea-57b8-83e1-b713144f684c", "亲兄弟，明算帐", "A10", "A05;A08", "manual_confirmed", "正文中心是遗嘱、夫妻财产、医疗费用、债务与继承争议的法律安排", "亲属关系和财产交换为副轴；题目明确要求法律解读，主专题为 A10", "main-thread", "2026-09-22"),
]
with path.open(encoding="utf-8-sig", newline="") as f:
    existing = list(csv.DictReader(f))
seen = {r["id"] for r in existing}
new = [dict(zip(fields, r)) for r in rows if r[0] not in seen]
if new:
    with path.open("a", encoding="utf-8-sig", newline="") as f:
        csv.DictWriter(f, fieldnames=fields).writerows(new)
print({"existing": len(existing), "candidate_rows": len(rows), "appended": len(new), "total": len(existing) + len(new)})
