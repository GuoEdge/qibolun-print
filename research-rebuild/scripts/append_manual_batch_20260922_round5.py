#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
fields = ["id", "title", "primary_print_topic_code", "secondary_print_topic_codes", "classification_status", "decision_basis", "review_note", "reviewer", "reviewed_at"]
rows = [
    ("492b5110-a59f-5544-93a0-2347a2e979a8", "扁舟", "A12", "A20;A03", "manual_confirmed", "正文中心是不同政治秩序中权力集中、地方治理与历史制度为何反复回到原位", "文学/历史材料和概念判断为副轴；不按小说题面机械归 A15", "main-thread", "2026-09-22"),
    ("f29bab0a-75f6-5a71-88bc-d268607cb465", "船底洞", "A13", "A18;A10", "manual_confirmed", "正文中心是船舶燃油系统、结构维修、通风检测与火灾风险的工程安全处理", "能源系统和安全责任为副轴；机器 A07 不能解释技术行动主线", "main-thread", "2026-09-22"),
    ("905f6068-fbf4-5ec9-b6b6-b6f0757e77d7", "不合群", "A01", "A06;A05", "manual_confirmed", "正文中心是个体面对群体接触恐惧、社会退缩与自我选择时的心理边界", "同伴关系和父母劝导是形成场景；不把家庭题面作为主专题", "main-thread", "2026-09-22"),
    ("cb678465-a091-5f99-b900-1a9f6569e039", "闭环", "A14", "A03;A13", "manual_confirmed", "正文中心是 AI 生成代码、模型迭代和软件系统闭环验证的可靠性问题", "技术实现与事实验证为副轴；人工智能与机器是主轴", "main-thread", "2026-09-22"),
    ("53940ad1-7ae6-514e-b403-7abf84d07c3d", "去伪存真", "A10", "A03;A07", "manual_confirmed", "正文中心是企业规则、产品安全和消费者维权中责任归属与可执行边界", "事实辨析和组织责任为副轴；具体产品场景不改变法律秩序主轴", "main-thread", "2026-09-22"),
    ("aa39afa2-e3e1-5b4c-81b9-7c1af007b266", "自医者", "A06", "A01;A08", "manual_confirmed", "正文中心是长期亲密关系中的价值观冲突、共同生活成本和是否继续结合的判断", "心理恐惧与经济条件为副轴；文章行动建议围绕关系边界，不是医学主题", "main-thread", "2026-09-22"),
]
with path.open(encoding="utf-8-sig", newline="") as f:
    existing = list(csv.DictReader(f))
seen = {r["id"] for r in existing}
new = [dict(zip(fields, r)) for r in rows if r[0] not in seen]
if new:
    with path.open("a", encoding="utf-8-sig", newline="") as f:
        csv.DictWriter(f, fieldnames=fields).writerows(new)
print({"existing": len(existing), "candidate_rows": len(rows), "appended": len(new), "total": len(existing)+len(new)})
