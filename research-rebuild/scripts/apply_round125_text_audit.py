#!/usr/bin/env python3
"""Apply the size-budgeted Round125 full-text reread."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round125-selection.csv"
FULLTEXT = REPORTS / "round125-fulltext.json"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round125-decisions.tsv"
AUDIT = REPORTS / "round125-text-audit.tsv"
parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


DECISIONS_BY_TITLE = {
    "慢点发财": ("A10", "A16", "社会信任被敲诈勒索和腐败盗用，中心是犯罪/规则惩罚，公共信任与名望为副轴。", "案件事实、刑罚及社会信任后果未独立核验。"),
    "热的路": ("A06", "A01", "正文围绕亲友、爱人与朋友如何在无交换价值时仍相互在乎，亲密关系为主、主体情感为副。", "爱与冷漠的循环是作者判断，不是心理学结论。"),
    "无能为力": ("A11", "A05;A07", "正文以照护亲人、接手同事工作等情境论证社会责任与伦理义务，伦理规范为主，家庭和组织为副。", "进化、人类责任与“愧疚”论证未作社会科学核验。"),
    "空手入白刃": ("A12", "A13", "正文中心是持械冲突中的自卫/武器控制策略，属于暴力与战术场景；工具和武器技术为副。", "含有可能造成伤害的自卫建议，成功率和安全性未核验，不构成操作指南。"),
    "舆论战": ("A16", "A12", "全文讨论国际舆论、宣传和公共认知如何影响中外战略平衡，媒体舆论为主、国际秩序为副。", "关于国家战略、国际力量和战争风险的判断未独立核验。"),
    "义和团": ("A20", "A12", "正文以义和团及晚清压迫解释为历史因果与史学批评中心，战争/外国势力为副。", "义和团史实、各方压迫程度和作者对研究者的评价未独立核验。"),
    "奠仪几何": ("A19", "A08;A05", "正文围绕父丧、葬礼、奠仪和亲属账目处理，死亡祭祀为主，金钱伦理和家庭责任为副。", "礼金习俗、费用和亲属权利义务未作法律或社会事实核验。"),
    "消声": ("A10", "A03;A06", "正文处理邻里噪音争议，核心是取证、报警、调解和诉讼的规则路径；证据与邻里关系为副。", "录音、警方调解、曝光和诉讼做法的合法性及安全后果未核验，不鼓励威胁或公开个人信息。"),
    "移山填谷": ("A18", "A13;A10", "正文分析河道清淤、矿山尾矿及环境危害，生态环境为主，工程处置和监管为副。", "尾矿工艺、比例、运输推断及具体事件尚未独立核验。"),
    "宾格": ("A06", "A16", "正文讨论头像作为第一印象、交往边界和对他人焦虑的影响，关系选择为主，公共形象为副。", "关于人类对图像的普遍反应是作者概括。"),
    "甜老虎": ("A07", "A06;A12", "正文把谦让、友爱、盟友和冲突升级作为合作/组织策略，职场组织与合作为主，关系和对抗为副。", "威慑、搏杀和公众形象的因果判断未核验，不构成现实冲突建议。"),
    "话事人": ("A12", "A10", "正文以俄美战争假设讨论国家决策、战略影响力和专家治理，国际外交为主，国家制度为副。", "对中国决策机制、专家影响及国际战争的描述未独立核验。"),
    "撒钱": ("A08", "A10", "正文提出以公民信用贷款替代现金发放的经济政策方案，财富/信贷与公共服务为主，制度规则为副。", "贷款、社会信用、移民和宏观经济效果均未核验，不构成政策建议。"),
    "液相呼吸": ("A13", "A09;A18", "正文按氧交换、毒性、动力和气液转换分析液体呼吸的工程可行性，技术工程为主，医学与生物科学为副。", "生理、ECMO、材料和科幻技术判断未独立核验，不是医疗建议。"),
    "伟大": ("A17", "A11;A12", "正文围绕中华民族及民族是否伟大定义跨民族责任与身份秩序，民族身份为主，伦理责任和国际秩序为副。", "民族史、国际政治和“伟大”标准是作者规范性判断，未作事实核验。"),
    "人吃人": ("A08", "A20;A11", "正文用“暗吃人”解释强制劳动和剥削的经济机制，劳动/资源关系为主，历史例证和伦理批评为副。", "历史案例、疾病、劳动收益和人类行为因果均未独立核验。"),
    "富豪的香港": ("A10", "A08;A07", "正文以香港富豪、地产垄断和治理结构分析权力配置，国家/治理为主，财富市场和组织权力为副。", "GDP、富豪资产、香港政治经济及制度判断未独立核验。"),
    "臭": ("A18", "A03", "正文从热力学、代谢和嗅觉演化解释排泄物气味，生态/自然科学为主，科学论证为副。", "热力学、生化分子和跨物种演化断言未独立核验。"),
    "极目": ("A13", "A14", "正文把折叠屏放入显示、脑机接口和人机输入技术路线讨论，技术工程为主，未来人机秩序为副。", "脑机接口、MR、显示产业和时间预测未独立核验。"),
    "宇宙战争": ("A12", "A13;A18", "正文以星际战争的推进成本、收益和战略理性为中心，战争外交为主，推进工程和宇宙科学为副。", "推进计算、历史军运数据及外星文明假设未核验。"),
    "掏耳朵": ("A18", "A09", "正文讨论动物耳道寄生、演化防御和人类医疗技术，动物/自然科学为主，照料和疾病为副。", "耳螨致死、演化、生理和圣经引文等主张未独立核验，不是兽医建议。"),
    "恐惧的度量": ("A03", "A01;A18", "正文先定义恐惧，再比较人类和动物的恐惧机制，概念论证为主，心理和自然科学为副。", "草履虫、物种恐惧和人类快感等比较认知判断未独立核验。"),
    "如意金箍顶门杠": ("A06", "A01", "正文以爱河和勇气区分趋避与逢凶化吉，亲密关系为主，主体勇气为副。", "“智者必勇”等是作者价值判断。"),
    "百洁灵": ("A02", "A06;A01", "正文围绕性经历、处女情结、婚恋安全感和成熟度，性/身体与同意为主，婚恋和主体成熟为副。", "关于性经历、洁癖和婚姻风险的普遍化判断未核验，不构成医疗或关系处方。"),
    "好大亏": ("A11", "A06", "正文讨论牺牲、社会互助与承认他人价值的伦理义务，伦理规范为主，社会关系为副。", "牺牲与社会帮助的因果判断是作者论证，未作社会实证核验。"),
    "柳下会": ("A16", "A01;A08", "正文给自媒体创作建议，中心是公共传播和受众关系，主体动机与长期财富为副。", "AI、平台传播、善行与财富效果未独立核验。"),
    "右手出": ("A01", "A04;A03", "正文解释青少年愤怒/怨恨并提出“右手规则”作为持续行动方法，主体情绪为主，学习方法和论证为副。", "迷宫数学、代际心理和时代挑战的普遍化判断未核验。"),
    "一介伟人": ("A11", "A01;A03", "正文把伟大定义为解除他人苦难、承担服务责任，伦理使命为主，主体经验与论证为副。", "伟大、服务和痛苦的标准是作者规范性判断。"),
    "魔丸真火": ("A12", "A03", "正文以敌我博弈、威慑和双输信条分析冲突策略，战争/战略为主，博弈论证为副。", "冲突升级、威慑和社会反应是作者推演，不构成现实对抗建议。"),
    "铜人": ("A09", "A11;A19", "正文讨论社会对自杀者的挽回、照料和资源义务，医疗/危机照料为主，伦理和死亡为副。", "自杀干预及“不能阻止”等判断未作临床或公共政策核验；现实危机应寻求专业急救。"),
    "三宅一生": ("A10", "A12;A11", "正文把恶意、隔离、反制和冲突升级作为风险治理问题，规则/安全为主，敌我对抗和仁慈边界为副。", "含有报复、武力和威胁性推演，未核验且不构成法律或安全建议。"),
    "认栽": ("A10", "A03", "正文以入室犯罪和安全疏忽的讽刺回应讨论风险承担，犯罪/安全场景为主，责任归因为副。", "案件、人物引述和自救效果未独立核验，不构成安保或自卫建议。"),
    "职业介绍": ("A07", "A16", "正文提供不披露真实职业时的礼貌化职业称呼，职场身份与劳动关系为主，公共表达为副。", "职业称谓是幽默示例，不是职业或法律陈述。"),
    "my dear offender": ("A03", "A06", "正文以反讽话术回应被辱骂，中心是语言反馈和表达策略，社会互动为副。", "“止疼药、消毒纸巾和保险”等是威胁式修辞，不构成报复或安全建议。"),
}


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields, rows, delimiter: str = ",") -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> None:
    _, batch = read_csv(BATCH)
    fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
    manual_fields, manual = read_csv(MANUAL)
    assert 0 < len(batch) <= 50 and len(batch) == len(fulltext) == 34
    assert [row["id"] for row in batch] == [row["id"] for row in fulltext]
    assert [row["title"] for row in batch] == [row["title"] for row in fulltext]
    assert sum(len(row.get("text") or "") for row in fulltext) == 29979
    assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)
    assert {row["title"] for row in batch} == set(DECISIONS_BY_TITLE)
    _, registry = read_csv(DATA / "print-topic-registry-v2.csv")
    codes = {row["code"] for row in registry}
    manual_by_id = {row["id"]: row for row in manual}
    assert len(manual_by_id) == len(manual) == 4305

    decision_fields = ["id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary", "status", "decision", "basis", "risk_boundary"]
    audit_fields = ["id", "title", "text_chars", "current_primary", "current_secondary", "recommended_primary", "recommended_secondary", "recommended_status", "decision_basis", "fact_risk"]
    decisions, audits, updates = [], [], []
    already = 0
    for row, article in zip(batch, fulltext):
        title = row["title"]
        primary, secondary, basis, risk = DECISIONS_BY_TITLE[title]
        secondary_codes = [code for code in secondary.split(";") if code]
        assert primary in codes and all(code in codes and code != primary for code in secondary_codes)
        assert len(secondary_codes) <= 3 and len(secondary_codes) == len(set(secondary_codes))
        assert len(article.get("text") or "") == int(row["body_char_count"])
        current = manual_by_id[row["id"]]
        assert current["title"] == title
        status = "manual_confirmed"
        decisions.append({"id": row["id"], "title": title, "old_primary": current["primary_print_topic_code"], "old_secondary": current["secondary_print_topic_codes"], "new_primary": primary, "new_secondary": secondary, "status": status, "decision": "retain" if primary == current["primary_print_topic_code"] else "promote", "basis": basis, "risk_boundary": risk})
        audits.append({"id": row["id"], "title": title, "text_chars": row["body_char_count"], "current_primary": current["primary_print_topic_code"], "current_secondary": current["secondary_print_topic_codes"], "recommended_primary": primary, "recommended_secondary": secondary, "recommended_status": status, "decision_basis": basis, "fact_risk": risk})
        desired = {"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary, "classification_status": status, "decision_basis": basis}
        if all(current.get(key, "") == value for key, value in desired.items()):
            already += 1
            continue
        assert current["classification_status"] == "manual_provisional"
        assert current["primary_print_topic_code"] == row.get("candidate_primary", "")
        assert current["secondary_print_topic_codes"] == row.get("candidate_secondary", "")
        current.update(desired)
        current["review_note"] = f"Round125 size-budgeted full-text reread; body_chars={row['body_char_count']}; batch={BATCH.name}; Fact-risk boundary: {risk}"
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round125-text-reread").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)
    assert already in {0, len(batch)}
    atomic_write(DECISIONS, decision_fields, decisions, "\t")
    atomic_write(AUDIT, audit_fields, audits, "\t")
    if updates and not args.dry_run:
        atomic_write(MANUAL, manual_fields, manual)
    print(json.dumps({"round": 125, "records": len(batch), "body_chars": 29979, "updated": len(updates), "confirmed": len(batch), "provisional": 0, "manual_total": len(manual), "dry_run": args.dry_run}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
