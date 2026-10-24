# -*- coding: utf-8 -*-
"""批次 r001-b0261 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0261.sessions.py            # 写 out/r001-b0261.out.jsonl
  python3 records/r001-b0261.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import autofill_empty_analysis, build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0261"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0261.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "16dc173e": {
  "analysis": {
   "question_context": "提问者问：在体制内没人提携是否就绝对永无出头之日（Q001）。作者不接受提问者的“绝对/永远”措辞框架，转而批评用绝对化断言为放弃作辩护的心态；正文没有讨论体制内提携的具体机制，也未回答“有没有出头之日”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以连续反问质疑：是否有必要把软弱掩饰到这种地步，“概率小”本已足够。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "指出问题核心不是选择是否合理明智，而是连一点可能性都承受不起的脆弱。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "把不认可的选择说得一无是处是败相，会招致他人回避厌弃，其伤害大于“永无出头之日”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "对一切保持实事求是是王者之气，你在此让人折服的程度决定选择被重视的程度。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "认同不来自策略高明；卖弄策略者是走投无路的菜鸟，成熟者只以对事实的诚实掌握展现实力。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "以面对危险警告不逃不慌为例，给出三种可能解释并声明不解释，归纳出淡定谈事实本身即展现实力。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "由两种人并列被如何选择，推及社会由人构成、被选择者众则“没办法”变“有办法”。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P030", "P031"], "summary": "收尾反问并给出行动建议：让孩子看这篇，早点剪掉其“精神阑尾”。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：只有把结论说到“绝对”“永远”，才能安慰自己放弃没有错吗；“概率小”本已足以证明自己不是软弱而是明智。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当人软弱到连一点可能性都承受不起，问题的核心就不再是选择是否合理明智，而变成世界上还有什么挑战对他容易到可以承受。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "把自己不认可、不愿做的选择描述得一无是处，是刺眼的败相；凭这种对其它选择极不客观的自欺欺人，多半可判断此人正处在失败进程中。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种姿态招致的异性婉拒、投资人回避、朋友远离、同事厌弃，对人的伤害远大于所谓“绝对永远没有出头之日”。", "evidence": ["E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "始终对一切保持实事求是的态度是王者之气；你在实事求是上让人折服的程度，决定你的选择被重视和在意的程度。", "evidence": ["E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "让人认同的不是策略高明——成年人不会随便暴露策略；逢人卖弄策略者多是走投无路的菜鸟，成熟的人只通过展现对事实的诚实而深入的掌握来展现实力。", "evidence": ["E010", "E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "面对“非常危险”的警告仍不落荒而逃、看上去也不担心，作者声明不解释，只给出三种可能：没能力却不慌（风险承受力惊人）、有能力、或勇气与智慧并重。", "evidence": ["E016", "E017", "E019"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个能不偏不倚、不美化不贬斥不歪曲地淡定谈论事实的人，不必依赖任何其它技巧或实力卖弄，仅凭淡定自若、没有焦虑，就已逻辑有效地展现了令人难以忘怀的实力。", "evidence": ["E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会由人构成而人管理世界，选择你的人每一个都是力量：选的人多了，没办法也会有办法；没人选，有办法都会变成没办法。", "evidence": ["E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议把这篇让孩子看明白，早点剪掉其“精神阑尾”，免得他犯错。", "evidence": ["E015"]}
   ],
   "argument_steps": [
    "复述并质疑提问者的绝对化措辞（“绝对”？“永远”？）",
    "反问是否有必要为掩饰软弱而如此，指出“概率小”本已足够",
    "重新定义问题核心：不是选择的合理性，而是承受不起任何可能性的脆弱",
    "断言这种自欺欺人暴露败相，会被他人察觉",
    "推及后果：他人回避厌弃的伤害大于“永无出头之日”",
    "给出正面标准：实事求是即王者之气，决定选择被重视的程度",
    "反面论证：认同不来自策略高明，因为成年人不会随便暴露策略",
    "举例（对危险警告的回应）：列出不逃不慌的三种可能，故意不解释",
    "归纳他人选择的社会机制：选的人多则没办法变有办法",
    "收尾反问并给出行动建议：给孩子看，剪掉精神阑尾"
   ],
   "concept_usage": [
    {"term": "实事求是", "meaning": "对事实不美化、不贬斥、不歪曲的诚实而深入的掌握，并可淡定谈论；作者把它直接当作实力的证明", "evidence": "P010", "ambiguity": "未界定“事实”的范围，“淡定谈事实=展现实力”是作者的引申"},
    {"term": "精神阑尾", "meaning": "比喻应尽早切除的无用且有害的心理成分，指向以绝对化断言安慰自己的软弱", "evidence": "P031", "ambiguity": "正文未明确定义其具体所指"},
    {"term": "王者之气", "meaning": "指始终对一切保持实事求是的态度所呈现的气质", "evidence": "P010", "ambiguity": "修辞性用语，非严格定义"},
    {"term": "出头之日", "meaning": "沿用提问者用语，指在体制内获得提携、晋升的前景", "evidence": "P009", "ambiguity": "作者未讨论其机制，也未给出判断标准"},
    {"term": "实力", "meaning": "文中指通过对事实的诚实而深入的掌握所展现的能力，而非策略卖弄", "evidence": "P015", "ambiguity": "“不解释”的姿态是否也算实力，文中未说明"}
   ],
   "examples_and_targets": [
    "提问者的“绝对”“永远”表述（Q001/P001）——作者的反驳对象是这种措辞，不是提问者本人被归为作者立场",
    "“这事非常危险，第一第二第三第四，你要注意”（P016）——引号内为他人警告，说话者未指明，是作者回应的场景（引用/修辞材料）",
    "异性、投资人、朋友、同事的反应（P008）——作者用来说明后果的修辞性列举，非数据证据",
    "逢人就卖弄高明策略的“菜鸟”（P014）——作者贬斥的行为类型（修辞材料）",
    "“小崽子”与“精神阑尾”（P031）——行动建议的对象与比喻",
    "标题“大冰箱”取自 P022“盘算的都是冰箱里还有没有空间”——比喻性标题"
   ],
   "conditions": [
    "全文以第二人称“你”面向作出“放弃”判断的人；未限定体制、行业或具体处境",
    "“多半正在下一个失败的进程中”使用概率限定（P007）",
    "作者对危险的回应以“但是我显然没落荒而逃”为条件设定（P017）",
    "三种解释以“要么……要么……”给出，且作者声明“不解释”，属修辞性悬置（P019—P023）",
    "“选的人多了，没办法也会有办法”依赖“社会由人构成、人管理世界”这一前提（P027—P028）"
   ],
   "rhetoric_and_tone": "第二人称训诫体，密集短句与反问；对提问者措辞带讥讽（“来，你再多说几句‘永远’、‘绝对’我听听？”）；对孩子用贬称（“小崽子”“精神阑尾”）；以“不解释。你可以猜。”制造悬念；用排比加强气势（“异性要婉拒你，投资人要回避你……”）；整体是居高临下的教导与敲打语气。",
   "unresolved_questions": [
    "未回答提问者关于体制内提携的实质问题，“出头之日”的标准与情境均未界定",
    "P016 引号内警告的说话者不明：是提问者、他人还是假想对话者，正文未说明",
    "P017—P023 的“我”是作者本人经历还是设想的示范情境，正文未说明",
    "作者自述“我不解释”（P019），三种解释只是修辞性悬置，不能当作其自陈事实",
    "段落字符范围有小间隙（P029 止于 942、P030 起于 944；P030 止于 965、P031 起于 967），lexical 统计 33 个 paragraph 节点而正文渲染为 31 段，可能有未渲染的结构片段",
    "brief 字段与正文 P001—P005 重叠且在“问题的核心就变成了以这样”处截断，疑为平台摘要截断，不能单独支持作者主张"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "“绝对”？“永远”？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "光是“概率小”还不够证明自己“不是软弱而是明智”", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "问题的核心就根本不是你的选择有多合理", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "世界上究竟有什么挑战对你容易到可以承受的了", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "这是一种非常刺眼的败相", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "就知道你多半正在下一个失败的进程中", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "这些东西对你的伤害远比那个所谓的“绝对永远没有出头之日”的东西大。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "这是一种王者之气", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "你在实事求是上让人有多折服，你的选择就有多让人重视和在意。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "不是你的策略有多高明所以让人认同", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P015", "quote": "成熟的人仅仅只通过展现自己对事实的诚实而深入的掌握来展现自己的实力。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P024", "quote": "就已经逻辑有效的展现了令人难以忘怀的实力", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P028", "quote": "选的人多了，没办法也会有办法。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P029", "quote": "没人选，有办法都会变成没办法。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P031", "quote": "早点剪了ta的精神阑尾", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "那么我肯定是有惊人的风险承受能力", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P022", "quote": "神挡杀神，魔挡杀魔", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P016", "quote": "这事非常危险，第一第二第三第四，你要注意", "relation": "context"},
    {"key": "E019", "paragraph_id": "P019", "quote": "这个嘛，不解释。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场晋升", "体制内", "心理与行为", "社会评价"],
   "issue_candidates": ["绝对化断言与放弃的自我辩护", "实事求是与实力展现", "他人选择与社会机制"],
   "text_function_candidates": ["答疑", "批评", "训诫", "论辩"],
   "object_candidates": ["提问者（身份未明）", "体制内单位", "异性", "投资人", "朋友", "同事", "子女"],
   "working_keywords": ["绝对", "永远", "实事求是", "王者之气", "精神阑尾", "败相", "出头之日", "风险承受能力"]
  },
  "notes": "无图片节点。正文与 lexical 结构计数不一致（lexical 33 个 paragraph、正文 31 段）；段落字符范围存在小间隙；brief 为被截断的平台摘要，与正文 P001—P005 重叠。本文未讨论体制内提携机制，提问者立场未被当作作者立场。"
 },
 "6511b53f": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "454ddc14": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "cc2624fb": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


autofill_empty_analysis(BATCH, SKELETON, ANALYSIS)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None, help='输出 JSONL 路径（默认 out/<batch>.out.jsonl）')
    args = ap.parse_args()
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row['article']
        uid = UID_BY_ID[art['id']]
        if uid not in ANALYSIS:
            raise SystemExit('ANALYSIS 缺少 %s (%s)' % (uid, art.get('title')))
        p = ANALYSIS[uid]
        records.append(build_record(
            row, row['batch_id'], row['corpus_sha256'],
            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', '')))
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
