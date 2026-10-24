#!/usr/bin/env python3
"""Apply the deduplicated Round124 short-text reread."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round124-candidate-batch.csv"
FULLTEXT = REPORTS / "round124-fulltext.json"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round124-decisions.tsv"
AUDIT = REPORTS / "round124-text-audit.tsv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


# These are正文中心 decisions, not claims that the article's facts or advice
# have been independently verified. Short or semantically incomplete answers
# remain provisional even when their title suggests a plausible topic.
DECISION_BY_TITLE = {
    "爱语": ("A00", "", "manual_provisional", "正文仅四字“这怪我”，没有可复核的爱意表达或论证中心。", "材料不足；不能由题目推定A06或A01。"),
    "坚持": ("A11", "A03", "manual_provisional", "“择善固执”只给出价值化定义，显示善与坚持的伦理方向，但没有展开语境。", "单句不足以判断A11与一般概念定义A03的边界。"),
    "不羡慕": ("A01", "A11", "manual_provisional", "“怜悯者从不羡慕”指向羡慕、怜悯和主体情绪关系，但没有解释机制。", "格言过短，不能把怜悯直接当作稳定伦理结论。"),
    "刻奇": ("A15", "A03", "manual_provisional", "回答以“凝视”与审美深渊隐喻刻奇，中心明显落在审美文化批评。", "没有给出可复核定义或克服路径，保留待审。"),
    "最重要的能力": ("A06", "A01", "manual_confirmed", "正文直接把最重要的能力界定为爱与被爱，中心是亲密关系能力，主体情感为副轴。", "“爱和被爱”的价值判断未作心理学核验。"),
    "政治": ("A10", "A03", "manual_confirmed", "正文将政治界定为对应然的博弈与结果的治理实践，中心是政治/治理概念，定义方法为副轴。", "定义是作者的规范性概括，不等同于政治学共识。"),
    "唯此为大": ("A19", "", "manual_confirmed", "“你终有一死/MEMENTO MORI”以死亡意识和记忆提醒为唯一中心。", "拉丁语格言的文化来源未作考据。"),
    "好批评": ("A16", "A03", "manual_confirmed", "问题以媒体传播为场景，回答评价批评如何影响公共对象，媒体公共认知为主、批评标准为副。", "原媒体视频及其背景未独立核验。"),
    "同性恋": ("A11", "A02", "manual_confirmed", "盲审修正：题目明确问基督教中的罪与爱，宗教规范是正文中心；性取向/性伦理为副轴。", "基督教教义及“爱即非罪”的规范判断未独立核验。"),
    "废话": ("A03", "", "manual_confirmed", "正文用是否影响行为、是否被记住来定义废话，中心是语言功能和定义边界。", "这是作者给出的判准，不是语言学定论。"),
    "去世之前": ("A19", "A11", "manual_confirmed", "正文是临终者与死后相逢的悼亡安慰语，死亡/纪念为主，来世想象为副轴。", "来世表达是安慰性修辞，未作宗教或事实断言核验。"),
    "酒神与天神": ("A11", "A03", "manual_provisional", "盲审修正：宗教/神话入口仍是主轴，但以麻醉剂替代兴奋剂的回答属于概念论证，不足以推出心理主体副轴。", "没有回答神话谱系；药物与人类终极方案的判断未独立核验。"),
    "主义": ("A03", "", "manual_confirmed", "正文把不同主义之间的矛盾作为定义性语言游戏，中心是抽象概念与论辩。", "极简回答未展开具体政治意识形态事实。"),
    "星星": ("A19", "A05", "manual_confirmed", "正文以儿童提问为入口回应死亡及星星意象，死亡/悼亡为主，亲子沟通为副轴。", "“人死后变成星星”的说法是安慰性表达，不是事实结论。"),
    "同情的资格": ("A11", "", "manual_confirmed", "正文区分同情的资格与对无知者的义务，并以“上帝黑色幽默”作伦理修辞，中心是规范义务。", "“义务”是作者的伦理判断，宗教意象未作教义核验。"),
    "至勇": ("A11", "A19", "manual_confirmed", "正文将面对死亡时的希望视为勇气，围绕灵魂/希望与终极价值的信念判断展开。", "希望与勇气的价值判断未作宗教或心理实证核验。"),
    "极端不忠诚": ("A03", "A16", "manual_confirmed", "正文把极端化重新定义为背叛，中心是忠诚概念的论证，网络舆论场景为副轴。", "所涉罗翔微博及网友解读未独立核验。"),
    "隐私就是生命": ("A13", "A10", "manual_confirmed", "问题来自AirTag技术产品，回答把产品使用的核心价值归结为隐私保护；技术路径为主、隐私权边界为副。", "AirTag功能、安全性和隐私风险未独立核验。"),
    "陌生宗教": ("A11", "", "manual_provisional", "正文只点出耆那教和santhara，主题方向是宗教，但没有形成可复核的介绍。", "材料极不完整，不能补写宗教史实。"),
    "不尊重与不接受": ("A02", "A03", "manual_confirmed", "正文区分“不接受”和“不尊重”，以性/性别边界与同意为中心，概念区分为副轴。", "强奸类比是作者的规范性表达，不构成法律结论。"),
    "强强": ("A06", "A01", "manual_confirmed", "正文以交友中对强者的不信任作自嘲回答，关系选择为主、自我评价为副。", "玩笑式自我比较不等于人格或心理测量。"),
    "理性的代价": ("A01", "A06", "manual_confirmed", "正文讨论过度理性导致他人把行为理解为故意，中心是主体形象与情绪表达，关系信任为副。", "关于他人心理反应是作者推断。"),
    "艺术生歧视": ("A15", "A16", "manual_confirmed", "正文解释对艺术生偏见的文化心理来源，艺术/文化身份为主，社会观感为副。", "关于偏见成因的普遍化判断未作社会科学核验。"),
    "慎终": ("A11", "A19", "manual_confirmed", "问题讨论无神论信念，回答把临终时刻作为信念检验，宗教/信念为主、死亡为副。", "临终生理状态的断言未作医学核验。"),
    "元天赋": ("A04", "A01", "manual_confirmed", "正文把天赋界定为不断找到坚持理由的能力，中心是能力形成与学习坚持，主体动机为副。", "天赋定义是作者理论，不是教育心理学结论。"),
    "普通不普通": ("A03", "A06", "manual_provisional", "正文批评把普通等同正常、健康、正义或安全，中心是概念边界，婚姻问题只是题面场景。", "未回答具体婚姻情境，正文证据不足以确认关系专题权重。"),
    "真爱永远": ("A06", "A01", "manual_confirmed", "正文直接处理恋爱关系中“永远对你好”的回应，亲密关系为主，情感主体为副。", "“永远”是关系承诺修辞，不是可验证保证。"),
    "三流作家": ("A15", "A03", "manual_confirmed", "正文以作家层级和故事/答案/问题的差异评价文学创作，艺术生产为主、认识论为副。", "作家等级是作者审美判断。"),
    "小重罪": ("A03", "A10", "manual_confirmed", "正文用刑罚和司法程序的讽刺隐喻讨论浪费时间、失礼等社会惩罚，语言/论证为主，法律框架为副。", "“社交死缓”等不是实际刑法或司法建议。"),
    "幸福感": ("A01", "A08", "manual_confirmed", "正文把幸福定义为前进过程中的感受，而非资产或收入终点，主体体验为主，财富背景为副。", "幸福与行动的关系是作者隐喻，不是心理测量结论。"),
    "预备死亡": ("A19", "A01", "manual_confirmed", "正文以写遗嘱和反复修订应对死亡恐惧，死亡准备为主，主体焦虑为副。", "遗嘱、公证的具体法律效果未核验。"),
    "高等生命": ("A18", "A03", "manual_confirmed", "正文以食物链和智慧生物等级反驳“高等生命食粮”设想，生命/自然科学为主，等级论证为副。", "科幻式推理不是生物学事实。"),
    "法庭大忌": ("A10", "A03", "manual_confirmed", "正文直接讨论法庭中质疑法官及法律争辩的行为边界，司法场景为主，论证方式为副。", "法庭程序和法官行为的普遍性判断未作法律核验。"),
    "与世长存": ("A20", "A15", "manual_confirmed", "正文回答数据保存问题时转向经典文本靠共同体持续保存，文明传承为主，文化生产为副。", "列举经典的历史地位未作来源考据。"),
    "上上大吉": ("A06", "A01", "manual_confirmed", "正文把失恋后的再爱困难类比为事故后的谨慎，亲密关系为主，欲望/情绪调节为副。", "飙车类比和“幸运”是修辞，不是创伤或安全判断。"),
    "四正道": ("A11", "A09;A06", "manual_confirmed", "正文用使人饱足、病愈、被陪伴、和解来判定正确道路，伦理价值标准为主，照料和关系结果为副。", "“绝对正面价值”是规范判断，不是医疗或社会效果证明。"),
    "双向奔赴": ("A06", "A01", "manual_confirmed", "正文把双向奔赴界定为双方都愿意走完全程，亲密关系为主，主体意愿为副。", "关系隐喻未涉及具体个案事实。"),
    "赞美": ("A03", "", "manual_confirmed", "正文区分赞美与事实陈述，中心是评价语言的真实性和表达边界。", "“只讲事实”的自我描述未作外部验证。"),
    "行为艺术": ("A15", "A10", "manual_provisional", "盲审修正：行为艺术仍是正文场景中心，但“追着打”及录像回应涉及人身、财产和证据边界，保留司法/安全副轴并暂定。", "追打、破坏和录像建议是反讽表达，可能涉及伤害、财产损毁和取证合法性，未核验且不构成行动建议。"),
    "“其实”": ("A03", "", "manual_confirmed", "正文分析“其实/实际上”在承认前述观察后引入更准确概括的语用功能，中心是语言定义。", "语用解释未以语料研究核验。"),
    "坚持感动": ("A06", "A01", "manual_confirmed", "正文讨论未经允许持续帮助为何会造成恐惧，中心是关系边界与恩惠资格，主体自主为副。", "关于帮助者动机的概括是作者判断。"),
    "嫉妒或崇拜": ("A01", "A03", "manual_confirmed", "正文用自我与他人差距的归因解释嫉妒或崇拜，心理主体为主，因果解释为副。", "心理机制是作者推断，不是心理学诊断。"),
    "悲观癖": ("A01", "A11", "manual_confirmed", "正文把悲观描述为会传播的心理依赖，并把乐观与信仰、勇气相连，主体情绪为主、信念为副。", "“毒瘾”是比喻，不能作为心理或成瘾诊断。"),
    "日本早餐": ("A08", "A10", "manual_confirmed", "正文从早餐摊成本、垃圾处理和城市规则解释市场供给，财富/消费为主、法规环境为副。", "日本法规、罚款、垃圾桶和爆炸事件均未独立核验。"),
    "铺路石": ("A19", "A13", "manual_confirmed", "正文设想将骨灰制成盲道铺装，死亡纪念为主，公共工程材料为副。", "骨灰建材和盲道实施可行性未核验。"),
    "一句话": ("A01", "A11", "manual_confirmed", "正文以“世界为你而造”鼓励个体继续活着，中心是主体生命意志，世界观/信念为副。", "鼓励性宇宙观不是事实断言；未提供危机评估或专业干预。"),
    "不打盲人": ("A06", "A01", "manual_confirmed", "正文把回应讽刺转为确认对方处境并避免落井下石，社会相处与边界为主，主体克制为副。", "盲人比喻涉及残障刻板印象，未作残障研究或沟通建议核验。"),
    "按需分配": ("A08", "A05", "manual_confirmed", "正文讨论基本生活保障与生育约束的经济条件，资源分配为主，家庭/生育为副。", "“唯一必要条件”等经济与人口判断未独立核验，且作者声明不等于政策主张。"),
    "陨石弹头": ("A03", "A15", "manual_confirmed", "正文批评科幻作品中由碎片判断人造物的逻辑，证据推理为主，文学作品批评为副。", "作品情节及“碎片足以判断”的技术判断未作外部核验。"),
    "不感兴趣": ("A02", "A03", "manual_confirmed", "正文以女性与知识兴趣为题，使用性别化和强奸隐喻解释知识消费，性别身体/同意为主，论证批评为副。", "关于性别群体兴趣的概括和“适应性”说法未有证据支持，不能当作事实。"),
}

BLIND_REVIEW_TITLES = {"同性恋", "酒神与天神", "行为艺术"}


def read_csv(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str = ",") -> None:
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
    assert len(batch) == len(fulltext) == 50
    assert [row["id"] for row in batch] == [row["id"] for row in fulltext]
    assert [row["title"] for row in batch] == [row["title"] for row in fulltext]
    assert sum(len(row.get("text") or "") for row in fulltext) == 2929
    assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)
    assert len(DECISION_BY_TITLE) == 50
    assert {row["title"] for row in batch} == set(DECISION_BY_TITLE)

    _, registry = read_csv(DATA / "print-topic-registry-v2.csv")
    codes = {row["code"] for row in registry}
    manual_by_id = {row["id"]: row for row in manual}
    assert len(manual_by_id) == len(manual) == 4305

    decision_fields = [
        "id", "title", "old_primary", "old_secondary", "new_primary", "new_secondary",
        "status", "decision", "basis", "risk_boundary",
    ]
    audit_fields = [
        "id", "title", "text_chars", "current_primary", "current_secondary",
        "recommended_primary", "recommended_secondary", "recommended_status",
        "decision_basis", "fact_risk",
    ]
    decisions = []
    audits = []
    updates = []
    already_applied = 0
    for row, article in zip(batch, fulltext):
        title = row["title"]
        primary, secondary, status, basis, risk = DECISION_BY_TITLE[title]
        secondary_codes = [code for code in secondary.split(";") if code]
        assert primary in codes and all(code in codes and code != primary for code in secondary_codes)
        assert len(secondary_codes) <= 3 and len(secondary_codes) == len(set(secondary_codes))
        assert len(article.get("text") or "") == int(row["body_char_count"])
        current = manual_by_id[row["id"]]
        assert current["title"] == title
        decisions.append({
            "id": row["id"], "title": title,
            "old_primary": current["primary_print_topic_code"],
            "old_secondary": current["secondary_print_topic_codes"],
            "new_primary": primary, "new_secondary": secondary,
            "status": status,
            "decision": (
                "blind_review_correction"
                if title in BLIND_REVIEW_TITLES
                else ("retain" if primary == current["primary_print_topic_code"] else "promote")
            ),
            "basis": basis, "risk_boundary": risk,
        })
        audits.append({
            "id": row["id"], "title": title, "text_chars": row["body_char_count"],
            "current_primary": current["primary_print_topic_code"],
            "current_secondary": current["secondary_print_topic_codes"],
            "recommended_primary": primary, "recommended_secondary": secondary,
            "recommended_status": status, "decision_basis": basis, "fact_risk": risk,
        })
        desired = {
            "primary_print_topic_code": primary,
            "secondary_print_topic_codes": secondary,
            "classification_status": status,
            "decision_basis": basis,
        }
        if all(current.get(key, "") == value for key, value in desired.items()):
            already_applied += 1
            continue
        if current["classification_status"] != "manual_provisional":
            assert all(current.get(key, "") == value for key, value in desired.items())
            already_applied += 1
            continue
        assert current["primary_print_topic_code"] == row.get("candidate_primary", "")
        assert current["secondary_print_topic_codes"] == row.get("candidate_secondary", "")
        current.update(desired)
        current["review_note"] = (
            f"Round124 deduplicated short-text reread; body_chars={row['body_char_count']}; "
            f"batch={BATCH.name}; Fact-risk boundary: {risk}"
        )
        current["reviewer"] = (current.get("reviewer", "main-thread") + "+round124-text-reread").strip("+")
        current["reviewed_at"] = date.today().isoformat()
        updates.append(current)

    assert already_applied in {0, 50}
    atomic_write(DECISIONS, decision_fields, decisions, "\t")
    atomic_write(AUDIT, audit_fields, audits, "\t")
    if updates and not args.dry_run:
        atomic_write(MANUAL, manual_fields, manual)
    print(json.dumps({
        "round": 124, "records": len(batch), "body_chars": 2929,
        "updated": len(updates),
        "confirmed": sum(row["status"] == "manual_confirmed" for row in decisions),
        "provisional": sum(row["status"] == "manual_provisional" for row in decisions),
        "manual_total": len(manual), "dry_run": args.dry_run,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
