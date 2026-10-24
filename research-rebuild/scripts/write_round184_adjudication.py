#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round184: final adjudication of the 12 remaining `manual_provisional` records.

Material check performed first (all local, no credentials, no site crawl):

  1. ``text`` vs ``brief`` vs ``lexical`` for each record — identical, so the
     short body is not a crawl artefact of one field;
  2. the old 4,050-record corpus — no fuller version;
  3. the source answer URL — Zhihu answers HTTP 403 to credential-free requests,
     and the project rules forbid using Cookie/CSRF/session values, so the
     source text cannot be re-obtained.

Conclusion: for the records below the short body IS the author's complete
published answer.  Rule R5 therefore applies.

R5 (极短回答裁决)
    A body may fix the print topic even when very short, provided it is verified
    to be the author's COMPLETE answer and
      (a) the body itself is the deliverable the question asks for
          (an example line, a definition, a judgement, a script), and
      (b) that deliverable identifies exactly one A-topic domain.
    It stays provisional when the body merely POINTS ELSEWHERE (a search
    instruction or an external link), is SOMEONE ELSE'S TEXT (a scripture
    quotation), is TRUNCATED, is EMPTY, or does not match the question.

Result: 5 confirmed, 7 stay provisional.  Applying this rule needs the manual
decision table and its derived indexes to be rebuilt afterwards.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
OUT = R / "reports/rebuild-20260926/round184"
MANUAL = R / "data/print-topic-manual-decisions-v2.csv"
REVIEW_DATE = "2026-09-26"
REVIEWER = "main-thread+round184-short-answer-adjudication"

# id -> (title, new_primary, new_secondary, new_status, blocking_reason, quote, reason)
D = {
    "c0a13aa7-6476-5774-b661-e424f933d513": (
        "爱语", "A06", "", "manual_confirmed", "",
        "这怪我。",
        "R5 确认。题面要的是“可以隐晦表示我爱你的句子”，正文给出的正是这一句台词本身——它就是题面所要的交付物，不需要额外展开。中心是亲密关系中的隐晦表达，A06 由正文（即交付物本身）确定。原副码 A03 删除：正文没有定义、证据或论证内容，它只是一句台词，A03 属审核期联想。"),
    "1015117d-47f5-5e6d-8648-373790bd96b6": (
        "坚持", "A03", "A11", "manual_confirmed", "",
        "择善固执。",
        "R5 确认。题面问“什么是坚持”，正文给出的正是作者的定义式回答“择善固执”，属题面所要的定义交付物，中心操作是定义与达意，A03 由正文确定；“善”的规范性来源构成副轴 A11。原副码 A01 删除：正文没有任何情绪、主体感受或情绪劳动内容，A01 属审核期联想。"),
    "9b6db870-bac2-5741-b015-bd793dcd6dbe": (
        "不羡慕", "A01", "A11", "manual_confirmed", "",
        "怜悯者从不羡慕。",
        "R5 确认。题面问“怎么才能达到不羡慕别人的境界”，正文给出的判断是：达到者即“怜悯者”——不羡慕是主体状态的结果。中心是主体的情绪境界，A01 由正文确定；“怜悯”的伦理性构成副轴 A11。"),
    "d60f14af-095b-5c1c-8ddb-65b97894e53d": (
        "婉拒", "A08", "A03", "manual_confirmed", "",
        "“我是来出差的。”",
        "R5 确认。题面问“如何婉拒健身房、按摩院、美容院等的推销”，正文给出的正是这句拒绝话术本身，属题面所要的交付物；场景由消费与服务交易定义，A08 由正文确定，语言策略为副轴 A03。"),
    "e8873042-d451-5335-87d7-638f1926a64a": (
        "刻奇", "A15", "A03", "manual_confirmed", "",
        "一个为了凝视你而骗你去凝视的深渊。",
        "R5 确认。题面第一问是“刻奇（Kitsch）是什么”，正文给出的正是作者的完整定义（有主谓结构的隐喻式界定：刻奇＝一种以被凝视为目的、诱使你去凝视的深渊），属定义交付物，域为审美与文化，A15 由正文确定；概念界定方式为副轴 A03。题面第二问“如何克服刻奇”未被正文回答，记为覆盖限制，不作为主题阻塞理由。"),
    "41c47afa-ca71-5905-924e-bc87c5a24f35": (
        "陌生宗教", "A11", "", "manual_provisional", "body_is_pointer",
        "耆那教是一个很值得注意的教派。／搜索一下什么叫做“萨恩塔拉”（santhara)。",
        "维持暂定。正文的操作内容是指向**他处**（要求读者自行检索“萨恩塔拉”），文章的中心不在文章之内；“很值得注意”是无依据的评价。按 R5，指向他处的正文不确认主题，保持 A11 + 待审。"),
    "e122a811-8341-594f-bce6-b50983b7e485": (
        "活成这样", "A00", "", "manual_provisional", "body_is_pointer",
        "兰迪·波许教授的最后一课 Randy Pausch's Last Lecture 【2007】【纪录片】【美国_哔哩哔哩",
        "维持暂定。正文只有外链视频标题，指向他处，无作者论述。保持 A00 + 待审，并保留排除候选身份。"),
    "beb62240-efcb-50cb-ac99-b2ef1dc53fbf": (
        "穿越幽谷", "A11", "A01", "manual_provisional", "body_is_quotation",
        "所以我告诉你们，不要为生命忧虑吃什么，喝什么；为身体忧虑穿什么。",
        "维持暂定。正文 197 字是**他人的文本**（《马太福音》引文），不是作者自己的论述或交付物。与“婉拒”的区别：那里引号内的话是作者**提出的话术**，这里引文是经文本身。按 R5，他人文本不确认主题，保持 A11 + 待审。"),
    "cdf1315e-9753-550f-8e55-651c06dfa32f": (
        "没伦理", "A00", "", "manual_provisional", "source_truncated",
        "如果没有伦理道德，厂",
        "维持暂定。正文在“厂”字后中断，属**截断**而非极短回答；`text`/`brief`/`lexical` 三字段一致、旧语料同篇同样截断、源站 403 不可再取，因此无法补全。保持 A00 + 待审。"),
    "5316551a-199f-5363-8436-1c4d4a72bbc2": (
        "酒神与天神", "A00", "", "manual_provisional", "body_question_mismatch",
        "因为麻醉剂必将替代兴奋剂成为人类最廉价的终极方案。",
        "维持暂定。题面问“狄俄尼索斯为什么可以取代宙斯”，正文却是关于麻醉剂与兴奋剂的断言，**与题面不匹配**，无法确定作者究竟在回答什么。保持 A00 + 待审。"),
    "e108515f-375c-53c9-8f6d-1ee2c16b275a": (
        "最大成长速度", "A00", "", "manual_provisional", "source_empty",
        "（正文为空，text/brief/lexical 均为空；唯一图片为夜间影视片段）",
        "维持暂定。正文为**空**，无任何可裁决的文本。保持 A00 + 待审；按用户指令，该篇**不进入印装册**（语料仍原样保留，未删除）。"),
    "c5354fb0-7345-5864-8522-2c0cfdad3c2e": (
        "战马阉割", "A00", "", "manual_provisional", "source_empty",
        "（正文为空，text/brief/lexical 均为空；7 张图均为马匹绘画/版画）",
        "维持暂定。正文为**空**，无任何可裁决的文本。保持 A00 + 待审；按用户指令，该篇**不进入印装册**（语料仍原样保留，未删除）。"),
}

NOT_PRINTED = {"e108515f-375c-53c9-8f6d-1ee2c16b275a", "c5354fb0-7345-5864-8522-2c0cfdad3c2e"}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    corpora = {}
    for line in (ROOT / "sooon-q9adg-articles-v2.jsonl").open(encoding="utf-8"):
        if line.strip():
            o = json.loads(line)
            if o["id"] in D:
                corpora[o["id"]] = o

    def squash(v: str) -> str:
        return "".join((v or "").split())

    rows, bad = [], []
    for aid, (title, p, s, st, br, quote, reason) in D.items():
        text = corpora[aid].get("text") or ""
        check = squash(quote.split("／")[0])
        hit = check and check in squash(text)
        if st == "manual_confirmed" and not hit:
            bad.append((title, quote))
        rows.append({"id": aid, "title": title, "new_primary": p, "new_secondary": s,
                     "new_status": st, "blocking_reason": br, "body_char_count": len(text),
                     "body_evidence_quote": quote, "decision_reason": reason,
                     "quote_verbatim": "yes" if hit else ("n/a" if st != "manual_confirmed" else "NO"),
                     "in_print_package": "no" if aid in NOT_PRINTED else "yes",
                     "reviewer": REVIEWER, "reviewed_at": REVIEW_DATE})
    if bad:
        print("QUOTE MISMATCH — aborting:", bad)
        return 1

    rows.sort(key=lambda r: r["body_char_count"])
    with (OUT / "round184-short-answer-adjudication.tsv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader(); w.writerows(rows)

    # apply to the live manual table
    man = list(csv.DictReader(MANUAL.open(encoding="utf-8-sig")))
    fields = list(man[0].keys())
    n = 0
    changed = []
    for r in man:
        if r["id"] in D:
            title, p, s, st, br, quote, reason = D[r["id"]]
            if (r["primary_print_topic_code"], r["secondary_print_topic_codes"],
                r["classification_status"]) != (p, s, st):
                changed.append({"id": r["id"], "title": title,
                                "old": f'{r["primary_print_topic_code"]}/{r["secondary_print_topic_codes"]}/{r["classification_status"]}',
                                "new": f"{p}/{s}/{st}"})
            r["primary_print_topic_code"] = p
            r["secondary_print_topic_codes"] = s
            r["classification_status"] = st
            r["decision_basis"] = reason
            r["review_note"] = ((r["review_note"] + " " if r["review_note"] else "")
                                + f"[round184 极短回答终局裁决；阻塞原因={br or '无'}；"
                                  f"材料核实：text/brief/lexical 一致、旧语料同篇一致、源站 403 不可再取。]")
            r["reviewer"] = REVIEWER
            r["reviewed_at"] = REVIEW_DATE
            n += 1
    tmp = MANUAL.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(man)
    tmp.replace(MANUAL)

    from collections import Counter
    summary = {"records": len(rows), "confirmed": sum(1 for r in rows if r["new_status"] == "manual_confirmed"),
               "provisional": sum(1 for r in rows if r["new_status"] == "manual_provisional"),
               "rows_updated": n, "status_changed": changed,
               "left_provisional": sorted((r["title"], r["blocking_reason"]) for r in rows if r["new_status"] == "manual_provisional"),
               "excluded_from_print": sorted(D[i][0] for i in NOT_PRINTED),
               "manual_status_after": dict(Counter(r["classification_status"] for r in man))}
    (OUT / "round184-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
