#!/usr/bin/env python3
"""Create the auditable Round142 classification TSV without mutating source data."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
BATCH = REPORTS / "live-manual-batch-v2-round142-short.csv"
OUT = REPORTS / "round142-decisions.tsv"

# All 20 records remain provisional: the independent reread found micro-text,
# retrieval prompts, metaphors, or unfinished articles that do not justify a
# confirmed semantic decision.
D = {
    "没伦理": ("A00", "", "正文截断为‘如果没有伦理道德，厂’，材料不足以确认医学伦理专题。", "正文截断；医学和伦理后果未展开。"),
    "婉拒": ("A08", "", "题目和一句话指向拒绝消费推销的交易边界，A08仅作最稳妥候选。", "正文只有一句话，适用关系和效果未说明。"),
    "刻奇": ("A15", "A03", "题目讨论Kitsch，答复以审美/文化隐喻回应；概念论证为副轴。", "正文极短，术语和美学主张未展开。"),
    "普通不普通": ("A03", "A16", "正文拆解普通、正常、健康、正义、安全的概念边界；公共规范为弱副轴。", "价值判断未作外部统计或伦理核验。"),
    "爱语": ("A00", "", "正文只有‘这怪我’，无法确认对隐晦表达爱意的具体论证。", "文本过短且语义开放。"),
    "坚持": ("A11", "A03", "‘择善固执’把坚持限定为对善/原则的持守；规范入口明确但未展开。", "‘善’的含义和规范依据未核验。"),
    "穿越幽谷": ("A11", "A01", "福音书引文以信仰回答低谷中的支撑来源；心理低谷为应用场景。", "引文出处、宗教解释和心理效果未核验。"),
    "不羡慕": ("A01", "", "格言直接处理羡慕情绪及比较姿态，属于主体心理入口。", "正文仅八字，心理关系未核验。"),
    "创新问题": ("A04", "A03;A13", "L0-L5创新层级及培养起点是中心，定义和技术路线为副轴。", "正文未完；创新等级和培养方法未核验。"),
    "陌生宗教": ("A11", "", "正文点出耆那教和santhara作为少见宗教入口，未形成完整论证。", "正文只是检索提示，宗教事实未核验。"),
    "拼命解决": ("A10", "A05", "围绕灭门暴力、法律、道德和舆论的失效边界展开，司法犯罪为主轴，亲属关系为场景。", "正文短且有搬迁残留；案件和法律判断未核验。"),
    "行为艺术": ("A15", "A06;A10", "反制性行为艺术和摄像记录回应毁坏毕设，艺术行动为主轴，协作/责任为副轴。", "展览、作品和法律责任未核验。"),
    "相由言生": ("A17", "A03;A18", "语言、文化环境与族群身份/面貌差异是假说中心，证据和身体因果为副轴。", "作者明确使用‘怀疑’和‘很可能’，不是事实结论。"),
    "知行合一": ("A03", "A01", "区分知道、相信、行动与证据，讨论经验规则边界；主体心理为副轴。", "正文未完；心理和社会判断未核验。"),
    "活死人3": ("A10", "A01;A03", "以公交蓄意报复为入口，论证价值崩溃、社会伤害和公共安全；心理机制为副轴。", "事件和预防机制未核验；枪/保险/火药是比喻。"),
    "酒神与天神": ("A11", "A15;A03", "神话替代题目使用麻醉剂/兴奋剂文化隐喻，宗教/神话入口更稳妥。", "仅一句且多义；药物、神话史和趋势未展开。"),
    "中医灭绝": ("A11", "A09;A01", "传统医学作为绝望中的希望和超理性支持是中心，医学对象和主体绝望为副轴。", "不会灭绝是作者预测，医学史和疗效未核验。"),
    "乌龙茶": ("A01", "A11", "区分可适应困境与失去希望的心理痛苦，围绕希望和绝望展开；规范/信仰为副轴。", "疾病与绝望判断未临床核验，不构成危机建议。"),
    "学生官僚": ("A07", "A03;A17", "学生组织职位称谓、上下级惯例和服从秩序是中心；跨文化比较为副轴。", "日本惯例和中日比较未核验。"),
    "运动最强": ("A18", "A03", "先定义运动能力，再用有效过载和尺度效应比较物种；定义推理为副轴。", "生物力学结论是作者推测，未核验。"),
}

with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
assert len(batch) == 20
assert {r["title"] for r in batch} == set(D)

fields = ["id", "title", "primary", "secondary", "status", "basis", "risk_note"]
with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
    writer.writeheader()
    for row in batch:
        primary, secondary, basis, risk = D[row["title"]]
        writer.writerow({"id": row["id"], "title": row["title"], "primary": primary,
                         "secondary": secondary, "status": "manual_provisional",
                         "basis": basis, "risk_note": risk})
print({"round": 142, "records": len(batch), "provisional": len(batch), "output": str(OUT)})
