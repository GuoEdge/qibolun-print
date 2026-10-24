#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the next正文-reviewed A-topic decisions without touching raw corpus."""
from __future__ import annotations
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
fields = ["id", "title", "primary_print_topic_code", "secondary_print_topic_codes",
          "classification_status", "decision_basis", "review_note", "reviewer", "reviewed_at"]
rows = [
    ("c201a314-1917-5f3a-9c57-c9ca2b21a583", "小而大", "A13", "A05;A15", "manual_confirmed",
     "正文中心是住宅空间与开发设计如何提供可重定义的功能自由，而非一般待客文化或面积偏好",
     "空间功能设计为技术工程主轴；家庭居住与审美文化为副轴，纠正机器 A15 主专题", "main-thread", "2026-09-22"),
    ("810a4734-3c29-5b4d-80cb-1c217b762785", "工贼", "A10", "A07;A03", "manual_confirmed",
     "正文中心是‘工贼’这一政治制度性指控在国家—企业结构中的合法性及其颠覆国家政权含义",
     "劳动组织和概念论证为副轴；不按一般职场协作机械归 A07", "main-thread", "2026-09-22"),
    ("ee40cf28-da20-5301-b942-0b8f81516fa8", "消声", "A10", "A06;A03", "manual_confirmed",
     "正文中心是邻里噪声争议中的取证、沟通、报警与起诉路径",
     "邻里关系是场景，录音取证与法律程序是行动主线；机器 A06 应改 A10", "main-thread", "2026-09-22"),
    ("d815035a-6fab-5358-8948-eeccf2e54d60", "算法关系", "A16", "A14;A01", "manual_confirmed",
     "正文中心是推荐算法塑造信息环境，以及用户如何用关注、停留和反馈行为反制有害内容",
     "算法机制和情绪后果为副轴；主问题是公共认知与媒介环境", "main-thread", "2026-09-22"),
    ("717cca42-6926-5321-b071-a34942427a57", "必也正名", "A16", "A14;A03", "manual_confirmed",
     "正文中心是平台应依据可观察的内容体验治理传播，而不应把不可证实的作者身份当作事实",
     "AI 文本识别与平台治理是副轴；‘正名’是事实证据和公共传播规则的论证方法", "main-thread", "2026-09-22"),
    ("c553b5f8-a317-540a-9525-ad5fc93dc4ea", "此座无人", "A10", "A08;A03", "manual_confirmed",
     "正文中心是铁路改签规则、公共补贴与占座造成的公共资源侵占及其规范边界",
     "市场成本和事实论证为副轴；保留机器 A10 主专题", "main-thread", "2026-09-22"),
    ("c17b7011-2d5a-583f-9720-a695d890ddd2", "顺天改命", "A01", "A11;A03", "manual_confirmed",
     "正文中心是主体如何处理志向、命运、成败压力与抑郁风险",
     "宗教/命运语言和论证方式为副轴；不把作者的心理判断当医学诊断", "main-thread", "2026-09-22"),
    ("753593ca-9bf8-5e20-9713-d7579f65c0a4", "打个颠倒", "A05", "A04;A01", "manual_confirmed",
     "正文中心是父母对幼儿失范、羞耻与惩戒责任的反转判断",
     "儿童教育和情绪反应为副轴；家庭代际责任是中心", "main-thread", "2026-09-22"),
    ("e0d169df-10fd-5b29-b51e-d95a627ab20f", "适度引导", "A05", "A06;A04", "manual_confirmed",
     "正文中心是父母如何在阶层偏见下引导女儿交友、保护并培养社会化能力",
     "友情是对象场景，亲子引导和社会化责任是主轴", "main-thread", "2026-09-22"),
    ("3e4a41df-16a0-5b80-beeb-19ee08fe7329", "白菜救世", "A08", "A07;A12", "manual_confirmed",
     "正文中心是产业白菜化、就业吸纳、996 与价格及劳动力结构的关系",
     "组织协作和全球南北秩序为副轴；纠正机器 A07 主专题", "main-thread", "2026-09-22"),
    ("b404b2a8-321c-5077-a127-6850ffa25f6d", "无知的智者", "A03", "A01;A04", "manual_confirmed",
     "正文中心是对高智、低智、智慧与品德的知识论和价值判断重估",
     "心理和教育为应用副轴；纠正机器 A04 主专题", "main-thread", "2026-09-22"),
    ("76d8036f-4674-5b55-9f52-5f108421ba2a", "片新剧老", "A15", "A16;A08", "manual_confirmed",
     "正文中心是电影与戏剧的媒介生产、现场表演和成熟周期",
     "传播时效与票房/市场为副轴；艺术生产是主轴", "main-thread", "2026-09-22"),
]
with path.open(encoding="utf-8-sig", newline="") as f:
    existing = list(csv.DictReader(f))
seen = {r["id"] for r in existing}
new = [dict(zip(fields, r)) for r in rows if r[0] not in seen]
if new:
    with path.open("a", encoding="utf-8-sig", newline="") as f:
        csv.DictWriter(f, fieldnames=fields).writerows(new)
print({"existing": len(existing), "candidate_rows": len(rows), "appended": len(new), "total": len(existing)+len(new)})
