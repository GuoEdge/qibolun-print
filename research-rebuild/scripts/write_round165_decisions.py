#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round165 decisions: the 22 shortest manual_provisional records.

This script only writes new round files under
``research-rebuild/reports/rebuild-20260926/round165``.  It never edits the
manual decision table, the formal index, or the corpus.  The manual table is
updated later, and separately, by ``apply_rebuild_20260926.py`` so that every
round keeps its own immutable decision record first.

Decision rule used (rule revision R1-R3, recorded in the round report):

R1  upgrade ``manual_provisional`` -> ``manual_confirmed`` only when the
    corpus body itself contains the author's own treatment of the centre
    question, that treatment fixes exactly one print primary topic, and the
    body evidence is quoted in the decision row.
R2  otherwise keep ``manual_provisional`` and classify the blocking reason.
R3  bodies under 20 characters are ``body_too_short_for_center``: the text is
    a fragment, a quoted line or an idiom, and any topic would have to be
    imported from the title or the question, which the project rules forbid.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research-rebuild/reports/rebuild-20260926"
ROUND = OUT / "round165"
REVIEW_DATE = "2026-09-26"
REVIEWER = "main-thread+round165-body-review"

# id -> (new_primary, new_secondary, new_status, blocking_reason, evidence_quote, reason)
D = {
    "e108515f-375c-53c9-8f6d-1ee2c16b275a": (
        "A00", "", "manual_provisional", "source_empty",
        "（正文为空，0 字符；唯一图片经 round118 复核为夜间影视片段，字幕“兽医—动物”）",
        "正文为空，正文证据不存在。原主码 A12 由题面推出，违反“正文中心问题优先于标题”，改为 A00（注册表允许“材料不足”使用 A00 并保留待审）。图片不能补足空正文，两篇文章保留排除候选身份。",
    ),
    "c5354fb0-7345-5864-8522-2c0cfdad3c2e": (
        "A00", "", "manual_provisional", "source_empty",
        "（正文为空，0 字符；7 张图均为马匹绘画/版画，未显示阉割、年代或出处）",
        "同前条：正文为空，原 A12 只由题面推出，无正文依据，改为 A00 待审。图片只能证明存在马的视觉素材，不能支持任何专题，保留排除候选身份。",
    ),
    "c0a13aa7-6476-5774-b661-e424f933d513": (
        "A06", "A03", "manual_provisional", "body_too_short_for_center",
        "全篇正文：“这怪我。”",
        "正文 4 字，为孤立短句，既未展开题面要求的“隐晦表达爱意”，也未形成可辨认中心操作。A06 只能由题面推出，按 R3 保持暂定。",
    ),
    "1015117d-47f5-5e6d-8648-373790bd96b6": (
        "A11", "A01", "manual_provisional", "body_too_short_for_center",
        "全篇正文：“择善固执。”",
        "正文 5 字，是《中庸》成语的引用，未说明“善”的规范依据或行动领域。A11（宗教自然法与世俗论证）与 A01 的主次无法由正文确定，按 R3 保持暂定。",
    ),
    "9b6db870-bac2-5741-b015-bd793dcd6dbe": (
        "A01", "A11", "manual_provisional", "body_too_short_for_center",
        "全篇正文：“怜悯者从不羡慕。”",
        "正文 8 字，是单句因果断言，未区分这是心理状态描述还是伦理判断。A01 与 A11 的边界不能由正文确定，按 R3 保持暂定。",
    ),
    "d60f14af-095b-5c1c-8ddb-65b97894e53d": (
        "A08", "A03", "manual_provisional", "body_too_short_for_center",
        "全篇正文：““我是来出差的。””",
        "正文 9 字，是题面所问“婉拒推销”的一句示例台词，未说明适用关系、场合或理由。A08 只能由题面推出，按 R3 保持暂定。",
    ),
    "cdf1315e-9753-550f-8e55-651c06dfa32f": (
        "A00", "", "manual_provisional", "source_truncated",
        "全篇正文：“如果没有伦理道德，厂”（在“厂”字后中断）",
        "正文在句中截断，只有 10 字，医学伦理、照料或其他专题均无正文支持。保持 A00 待审并记录源材料截断，不据标题推断专题。",
    ),
    "e8873042-d451-5335-87d7-638f1926a64a": (
        "A15", "A03", "manual_provisional", "body_too_short_for_center",
        "全篇正文：“一个为了凝视你而骗你去凝视的深渊。”",
        "正文 17 字，是单句隐喻式定义，既未展开“刻奇是什么”的概念界定，也未给出“如何克服”的任何步骤。近阈值案例：若日后取得完整正文可优先重审，本轮按 R3 保持暂定。",
    ),
    "5316551a-199f-5363-8436-1c4d4a72bbc2": (
        "A00", "", "manual_provisional", "body_question_mismatch",
        "全篇正文：“因为麻醉剂必将替代兴奋剂成为人类最廉价的终极方案。”",
        "题面问“狄俄尼索斯为什么可以取代宙斯”，正文却是关于麻醉剂与兴奋剂的一句断言，题文不匹配。正文既无神话/宗教论证，也无药物或社会论证的展开，保持 A00 待审。",
    ),
    "41c47afa-ca71-5905-924e-bc87c5a24f35": (
        "A11", "", "manual_provisional", "body_is_pointer",
        "全篇正文：“耆那教是一个很值得注意的教派。／搜索一下什么叫做“萨恩塔拉”（santhara)。”",
        "正文 41 字是检索指引，没有作者对耆那教或萨恩塔拉的解释与论证。教派名称可以提示 A11，但正文本身未完成任何中心操作，保持暂定。",
    ),
    "913f1fd9-3d73-546a-b924-70174ef27403": (
        "A03", "", "manual_confirmed", "",
        "正文逐条切断概念等同：“普通不是正常。／普通不是健康。／普通不是正义。／普通不是安全。／普通啥都不是。”",
        "正文本身完成了“拆分普通/正常/健康/正义/安全”的概念边界操作，正是认识论与概念论证的中心动作，A03 由正文直接支持。原副码 A16（媒体舆论）在正文中没有任何对应内容，属审核期加入的语境标签，按“副专题须有正文支持”删除。副码清空为 0 个。",
    ),
    "e122a811-8341-594f-bce6-b50983b7e485": (
        "A00", "", "manual_provisional", "body_is_pointer",
        "全篇正文：“兰迪·波许教授的最后一课 Randy Pausch's Last Lecture 【2007】【纪录片】【美国_哔哩哔哩 ...】”",
        "正文只有外链视频标题，没有作者可复核的论述。已有图片只能确认人物资料图。保持 A00 待审并保留排除候选身份。",
    ),
    "85aecfc3-f160-531a-8404-42441717edd4": (
        "A15", "", "manual_confirmed", "",
        "作者给出的替代方案本身即作品方案：“你可以联合其他同学一起完成一个追着打的行为艺术——／…《群像•破坏着破坏着的破坏者的破坏者》／…在每个作品前都装上摄像头，录下破坏的慢动作：／《被凝视的毁灭者》”",
        "正文以两个具名作品方案回答“是否劝他放弃”，中心操作是艺术实践提案，A15 由正文直接支持。原副码 A07/A10 是审核者附加的风险与组织语境，正文未展开组织关系或法律问题，删除；副码清空为 0 个。",
    ),
    "6cab9392-d433-535d-a891-464294858932": (
        "A07", "A04", "manual_confirmed", "",
        "正文自设比较并给出理由：“为什么要求以职位相称全民会口诛笔伐？／日本学生会叫会长叫部长叫前辈叫主将不是惯例么？…／呵斥本身的确比较中二，但是呵斥本身没什么问题。这并不因为学生会似乎没有什么实权而有所改变吧。”",
        "正文围绕学生组织中的职位称谓、呵斥惯例与“有无实权”的辩解展开，中心是组织内的权威与服从规则，A07 由正文支持；学校场景为副轴 A04。原副码 A03/A17 改为 A04：正文未做概念论证，也没有民族身份秩序的展开，只有中日惯例比较作为论据。",
    ),
    "a687351f-28f0-5b9a-8d9c-41682da6e7a8": (
        "A04", "A03", "manual_confirmed", "",
        "正文以反问列出唯一路径并收束为论点：“击败人不是只有这些办法吗？…／正面进攻，实力取胜，／一视同仁，吾道唯一。”",
        "正文的论点是击败一个人只能靠具体能力与实力，不能靠道德身份区分，中心是能力与竞争，A04 由正文支持；论辩形式为副轴 A03。原副码 A07（职场组织）在正文中无对应内容，删除。",
    ),
    "a147c2b8-a54d-57cc-9558-3449a8dce120": (
        "A10", "A05", "manual_confirmed", "",
        "正文论点：“要考虑到对方的父母可能用命解决问题。／法律、道德、公众舆论这些东西，／在对方打算用命替自己的子女解决自己认为必须解决的问题的时候，／不堪一击。”",
        "正文直接论断法律、道德与舆论在致命暴力面前的限度，中心是暴力犯罪与法律秩序的效力边界，A10 由正文支持；家庭亲属动机为副轴 A05。文末“原回答搬迁到了这里”说明本条目是迁移片段，作为限制记录，不改变专题。",
    ),
    "7d9d6244-95ea-553f-b951-089dfb31ce42": (
        "A17", "A03;A18", "manual_confirmed", "",
        "正文给出成因假说与比较观察：“我一直怀疑，其实语言才是对不同文化环境的同一人种造成总体面貌发育差异的根本原因。／日本老人的面相和中国老人、韩国老人、蒙古族老人、苗族老人的面相差异，很可能是因为各自语言的具体发音方式和表情要求所塑造出来的。”",
        "正文全部以族群（ABC、日本人、韩国人、蒙古族、苗族）的体貌识别差异为对象，中心是族群识别与身份秩序，A17 由正文支持；假说论证与发育/生理机制为副轴 A03、A18。作者使用“怀疑/很可能”属作者自己的置信声明，须在证据层记录；按框架“不得仅因事实主张未核验而使用临时状态”，该理由不构成暂定依据。",
    ),
    "beb62240-efcb-50cb-ac99-b2ef1dc53fbf": (
        "A11", "A01", "manual_provisional", "body_is_quotation",
        "全篇正文为一整段经文引文，自“所以我告诉你们，不要为生命忧虑吃什么，喝什么”至“还不如这花一朵呢！”",
        "正文 197 字全部是《马太福音》引文，没有作者自己的解释、判断或行动要求。专题只能由引文主题与题面推断，保持暂定；正文引用的经文归属与译本仍未核验。",
    ),
    "02b823b2-64d3-5356-bb11-e8c089c72013": (
        "A11", "A09;A01", "manual_confirmed", "",
        "正文自建因果链：“中医不会灭绝，因为人的绝望不会灭绝。…／这些东西一定是纯理性所不能支持的。…／凡绝望者，必定是对一切理性的工具都绝望了。这时还能给他希望的，只有先前理性所支撑不了的东西了。”",
        "正文把传统医学的存续解释为“理性无法支撑的希望机制”，中心是信念性/宗教性解释而非医学疗效或医疗制度，A11 由正文支持；医学对象与绝望心理为副轴 A09、A01。原审核理由“疗效与医学史未核验”属事实核验层，按框架不作为暂定依据，改为在风险注记中保留。",
    ),
    "96522ec0-3832-570f-8a0c-c3dfd7fef58f": (
        "A01", "A03", "manual_confirmed", "",
        "正文区分两类痛苦：“只是需要熬就能熬过去的苦，其实后味回甘的乌龙茶而已。／…真正的苦，是没了希望本身——不知道还该指望什么、也不知道还能指望什么，即使有所指望，也完全没有任何它能实现的信心。”",
        "正文的中心操作是把“可熬的困境”与“失去希望本身”区分开，落点在主体的希望与承受，A01 由正文支持；概念区分本身为副轴 A03。原副码 A03 保留，round142 曾改列的 A11 在正文中无宗教内容，不采纳。正文触及自杀意念，风险注记保留。",
    ),
    "45874a32-c9d4-5cac-838d-26096e36a328": (
        "A03", "A01;A11", "manual_confirmed", "",
        "正文提出中心命题并展开：“知不等于信，信才影响行。…／ta们需要有更切肤、更直感的证据，来支撑自己为将来的、可能的危险付出眼下的、现实的代价。…／恰恰是这一点，从根本上保证了人类不会成为老经验、老体会的绝对奴隶而灭绝于环境变迁。”",
        "正文 659 字是完整的认识论论证（知道/相信/证据强度/软话与硬证据），中心由正文直接支持为 A03；主体心理与规范/伦理推论为副轴 A01、A11。正文末“（未完，待续）”记为版本限制：本确认只覆盖现有正文可见的中心，不追认未发表部分。",
    ),
    "f56baf4c-6d3c-5b38-aba5-1a38b413f041": (
        "A01", "A03;A11", "manual_confirmed", "",
        "正文论点为“一切特质你都有”，并以坦克与打磨彩蛋作比：“你当然是你所讨厌的那种人，这个不用问。／人不是什么高纯物质，而是一种“全元素杂合体”。…／你是每一种人，所以你一定也是你讨厌的那种人。／别忘了，你也是你所喜欢的那种人。”",
        "正文 676 字是作者关于自我认识与人格复合性的完整论证，落点在主体判断与自我投射，A01 由正文支持；属性归属的论证方式为副轴 A03，末句的宽恕/伦理收束为副轴 A11。正文以“（侵删）”引用一张图作为比喻，图片经 round118 视觉复核 1/1 且未改变专题，图片的最终保留决定另行记录。",
    ),
}


def main() -> int:
    packets = {p["id"]: p for p in json.loads((OUT / "pending-92-fulltext.json").read_text(encoding="utf-8"))}
    rows = list(csv.DictReader((ROUND / "round165-selection.csv").open(encoding="utf-8-sig")))
    ids = [r["id"] for r in rows]
    assert set(ids) == set(D), (set(ids) ^ set(D))

    decision_fields = ["id", "title", "primary", "secondary", "status", "basis", "risk_note"]
    audit_fields = ["id", "title", "source_ordinal", "body_char_count", "old_primary", "old_secondary",
                    "old_status", "new_primary", "new_secondary", "new_status", "blocking_reason",
                    "body_evidence_quote", "decision_reason", "reviewer", "reviewed_at"]
    rev_fields = ["id", "title", "old_primary", "old_secondary", "old_status", "new_primary",
                  "new_secondary", "new_status", "basis", "risk_note", "revision_source", "revised_at"]

    decisions, audits, revs = [], [], []
    for article_id in ids:
        p = packets[article_id]
        new_p, new_s, new_st, block, quote, reason = D[article_id]
        old_p = p["manual_primary"]
        old_s = p["manual_secondary"]
        old_st = p["manual_status"]
        risk = p["manual_review_note"]
        decisions.append({
            "id": article_id, "title": p["title"], "primary": new_p, "secondary": new_s,
            "status": new_st, "basis": reason, "risk_note": risk,
        })
        audits.append({
            "id": article_id, "title": p["title"], "source_ordinal": p["source_ordinal"],
            "body_char_count": p["body_char_count"], "old_primary": old_p, "old_secondary": old_s,
            "old_status": old_st, "new_primary": new_p, "new_secondary": new_s, "new_status": new_st,
            "blocking_reason": block, "body_evidence_quote": quote, "decision_reason": reason,
            "reviewer": REVIEWER, "reviewed_at": REVIEW_DATE,
        })
        if (old_p, old_s, old_st) != (new_p, new_s, new_st):
            revs.append({
                "id": article_id, "title": p["title"], "old_primary": old_p, "old_secondary": old_s,
                "old_status": old_st, "new_primary": new_p, "new_secondary": new_s, "new_status": new_st,
                "basis": reason, "risk_note": risk,
                "revision_source": "round165-decisions.tsv (body reread)", "revised_at": REVIEW_DATE,
            })

    for name, fields, data in (
        ("round165-decisions.tsv", decision_fields, decisions),
        ("round165-body-evidence-audit.tsv", audit_fields, audits),
        ("round165-revision-log.csv", rev_fields, revs),
    ):
        path = ROUND / name
        delim = "\t" if name.endswith(".tsv") else ","
        with path.open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter=delim)
            w.writeheader(); w.writerows(data)

    print(json.dumps({
        "round": 165, "records": len(ids),
        "body_chars": sum(packets[i]["body_char_count"] for i in ids),
        "confirmed": sum(1 for i in ids if D[i][2] == "manual_confirmed"),
        "provisional": sum(1 for i in ids if D[i][2] == "manual_provisional"),
        "revisions": len(revs),
        "primary_changed": sum(1 for i in ids if D[i][0] != packets[i]["manual_primary"]),
        "secondary_changed": sum(1 for i in ids if D[i][1] != packets[i]["manual_secondary"]),
        "blocking_reasons": {
            r: sum(1 for i in ids if D[i][3] == r) for r in sorted({D[i][3] for i in ids if D[i][3]})
        },
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
