# -*- coding: utf-8 -*-
"""批次 r001-b0056 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0056.sessions.py            # 写 out/r001-b0056.out.jsonl
  python3 records/r001-b0056.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0056"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0056.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "67e3fa57": {
  "analysis": {
   "question_context": "提问者问如何看待高晓松的直播被骂到终止（Q001），即要求评价一场以辱骂迫使直播中止的公共事件；提问者未陈述立场。作者未复述事件经过，直接从“批评”与“骂/暴力”的概念区分入手给出判断。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"], "summary": "界定批评：不是语言暴力艺术、不是骂，而是真诚支持、珍贵罕见的礼物、不带侮辱、唯恐不够温柔、遵循最低伤害原则，是爱不是恨。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P009", "P010"], "summary": "判定高晓松所遭遇的不是批评而是暴力；暴力没有正义可言。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "推演暴力的自我增殖：以暴力得利即证明暴力有效，从而埋下更大暴力的动机与仇恨艳羡的种子；仇恨者使暴力转向你，羡慕者去伤害别人；人彼此曲折相连。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P017", "P018", "P019"], "summary": "对暴力的总体判断：速效崇拜是人类最黑暗的痼疾之一；无论理由多可理解乃至正义，暴力发生仍是人类的失败，成果以人类总体更大美好可能的丧失为代价。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P020"], "summary": "结论：这件事没有什么值得高兴的。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "批评并不是一种语言暴力艺术。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "骂并不是批评，批评并不是骂。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评是真诚的支持、珍贵而罕见的礼物，不带侮辱，绝无毁灭杀伤对方之意，反而希望对方发现风险、了解机会、改变缺陷、得到发展。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "批评遵循最低伤害原则：只有无法避免、找不到办法避免的痛，才能被批评者视为不得不接受的风险而不得已用之。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "批评是唯恐不够温柔的，是一种爱，不是一种恨。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "高晓松所遭遇到的并不是批评，而就是暴力。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "暴力没有正义可言。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "用暴力得到的东西都是更大、更多的暴力的肥料：得利即证明暴力有效，由此埋下追求暴力的决心与动机，种下仇恨和艳羡的种子；仇恨你的将使更大暴力指向你，羡慕你的将去伤害别人。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对暴力的速效的崇拜，是人类最黑暗的痼疾之一。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "无论暴力的理由多么可以理解、无可避免乃至正义，它的发生都仍然是人类的失败。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "暴力的成果无论多么美妙绚丽，都是以人类总体更大的美好可能的丧失为代价的。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这件事没有什么值得高兴的。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "先立定义：批评不是语言暴力艺术，骂与批评互相不是（P001-P002）。",
    "正面刻画批评：真诚支持、珍贵罕见、不带侮辱、唯恐不够温柔、希望对方变好（P003-P005）。",
    "给出批评的限定原则：最低伤害，痛仅在无法避免时被接受（P006）。",
    "以爱与恨作归属判断（P007-P008）。",
    "把问题所述事件归入暴力而非批评（P009），并断言暴力无正义（P010）。",
    "由“得利即证明有效”推演暴力的自我增殖与回流（P011-P015），以人的普遍联结为前提（P016）。",
    "上升到总判断：速效崇拜是痼疾，暴力发生是人类的失败，成果以总体美好可能的丧失为代价（P017-P019）。",
    "结论：此事不值得高兴（P020）。"
   ],
   "concept_usage": [
    {"term": "批评", "meaning": "真诚支持、不带侮辱、唯恐不够温柔、遵循最低伤害原则、希望对方变好的表达（P003,P005,P006）；与骂、暴力对举。", "evidence": "P003", "ambiguity": "未给出区分批评与否定的操作性边界，也未说明批评是否必须被接受。"},
    {"term": "骂 / 语言暴力艺术", "meaning": "被排除在批评之外，归入语言暴力（P001,P002）；正文未给判定标准。", "evidence": "P002", "ambiguity": "“骂”的范围（是否含一切负面评价）未界定。"},
    {"term": "暴力", "meaning": "用于指本次事件中迫使直播终止的攻击行为，并作为其后续后果推演的起点（P009,P010,P011）。", "evidence": "P009", "ambiguity": "未说明是否包含制度性、自卫性暴力。"},
    {"term": "最低伤害原则", "meaning": "批评者只把无法避免的痛视为不得不接受的风险（P006）。", "evidence": "P006", "ambiguity": "“无法避免”由谁判定未说明。"},
    {"term": "速效的崇拜", "meaning": "对暴力见效快的崇拜，被作者称为人类最黑暗的痼疾之一（P017）。", "evidence": "P017", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "高晓松的直播被骂到终止：提问者所问事件（Q001），作者据以判定“不是批评而就是暴力”的实例（P009）；正文未叙述事件细节。属作者论断的适用对象。",
    "以第二人称“你”指代的施暴得利者：作者推演其后果（P012-P016），未指名。属论辩中的假设对象。",
    "人类总体：被作者设定为暴力代价的承担者（P018,P019）；属作者论断中的集体主体。",
    "“肥料”“种子”“痼疾”：比喻性修辞材料（P011,P013,P017）。"
   ],
   "conditions": [
    "最低伤害原则只在“仅有无法避免、找不到办法避免的痛”这一条件下成立（P006）。",
    "对暴力后果的推演以“你借此得到了好处”为条件（P012）。",
    "推演依赖的前提是“任何人其实都是曲折的和其他一切人联结在一起的”（P016）。",
    "作者明确暴力理由可“可以理解和无可避免、乃至于正义”，但结论不因理由正当而改变（P018）。"
   ],
   "rhetoric_and_tone": "格言体短句并列，多以“是/不是”下判断；第二人称“你”直接训诫并把读者代入施暴得利者位置（P012-P016）；通篇无事件细节，语气庄重、道德劝诫，带“肥料”“种子”“痼疾”等比喻；以否定句收束（P020）。",
   "unresolved_questions": [
    "提问所述高晓松直播被骂到终止的具体经过，正文未叙述，无法判断作者所指范围（Q001,P009）。",
    "“骂”与“批评”的判定边界，正文未给出标准（P001,P002）。",
    "P012-P016 中第二人称“你”具体指施暴网民还是泛指，未明示。",
    "P010“暴力没有正义可言”与 P018 承认暴力理由可“乃至于正义”，是否为例外（如自卫），正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "批评并不是一种语言暴力艺术。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "骂并不是批评，批评并不是骂。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "批评是一种真诚的支持，是一种珍贵而且罕见的礼物，是不带侮辱的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "反而是希望对方发现没有发现的风险、了解没有了解的机会、改变没能改变的缺陷、得到未能得到的发展。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "仅有无法避免、找不到办法避免的痛，才能被批评者视为不得不接受的风险，不得已而用之。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P005", "quote": "是唯恐不够温柔的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "不是一种恨。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "高晓松所遭遇到的，并不是批评，而就是暴力而已。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "暴力没有正义可言。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "用暴力得到的东西，都是更大、更多的暴力的肥料。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "你就埋下了多大、多深的追求暴力的决心和动机，种下了仇恨和艳羡的种子。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "仇恨你的，将来那更大的暴力就直接指向你。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "对暴力的速效的崇拜，是人类最黑暗的痼疾之一。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "它的发生都仍然是人类的失败。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P019", "quote": "都是以人类总体更大的美好可能的丧失为代价的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "这件事没有什么值得高兴的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德评论", "网络舆论现象评论"],
   "issue_candidates": ["批评与语言暴力的界限", "网络围攻致直播中止", "暴力的自我增殖与代价"],
   "text_function_candidates": ["评论", "训诫/劝诫", "概念辨析"],
   "object_candidates": ["高晓松", "参与辱骂的网民"],
   "working_keywords": ["批评", "骂", "语言暴力艺术", "最低伤害原则", "暴力的肥料", "速效的崇拜"]
  },
  "notes": "提问（Q001）属提问者，未作为作者主张。无图片节点；provenance/superseded 均为 null。brief 与正文前段重复，仅作导航。"
 },
 "ceea855a": {
  "analysis": {
   "question_context": "提问者问“老公太事逼该怎么办？”（Q001），即如何处理伴侣对细节过分挑剔；提问者只用“事逼”一词定性，未描述具体行为。作者不直接给处置办法，而是解释这种行为的一般逻辑与来源，纠正观察者的误读，并给出一句应答建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "把该行为解释为想通过控制一切细节确保成功、避免失败，大概是对现状不满所做的努力，其基本逻辑一般是“把细节做好，成功会自然到来”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "说明机制：一点小处不顺心就如鲠在喉、夜不能寐；强迫症并非真的喜欢强迫症，而是受不了“被这些细节拖累、失去成功的可能”的想象。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "归因与条件：可视为高度责任感的副作用，责任越大焦虑越重；若人信不过自己的运气，出现这样的控制狂、强迫症难以避免。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "指出观察者的误读：未分享这种压力的人无法理解，会觉得对方“没有必要的讲究细节”，作者判定这是误解。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P009"], "summary": "行动建议：此时他需要听到“有情饮水饱”，而不是“你怎么这么事逼”。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "伴侣的表现更像是想通过控制一切细节来确保成功和避免失败。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这大概是对现状不满而做的努力，其基本逻辑一般是“把细节做好，成功会自然到来”。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "强迫症并非真的喜欢有强迫症，其实是受不了“被这些细节拖累、失去成功的可能”的想象。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "某种程度上这也可以被认为是高度的责任感带来的副作用，责任越大焦虑就越重。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "如果人信不过自己的运气，那么出现这样的控制狂、强迫症是难以避免的。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "没有分享这种压力的观察者会觉得对方“没有必要的讲究细节”，但作者判定这是误解。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种情况下他需要听到“有情饮水饱”，而不是“你怎么这么事逼”。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "先给行为定性：控细节以保成功、避失败（P001）。",
    "补两层解释：来源是对现状不满的努力，其内在公式是“把细节做好，成功会自然到来”（P002-P003）。",
    "描述体验层面：小处不顺心即难以忍受（P004）。",
    "揭示强迫症的真正驱动力是不愿面对失败的想象，而非喜欢强迫本身（P005）。",
    "以责任与焦虑的正比及“信不过运气”给出条件性归因（P006）。",
    "反驳观察者的误读：未分享压力者会觉得细节讲究没有必要（P007-P008）。",
    "给出应答建议（P009）。"
   ],
   "concept_usage": [
    {"term": "事逼", "meaning": "提问者用语，指伴侣对细节过分挑剔（Q001）；作者正文未复用该词，改以“控制狂、强迫症”描述（P006）。", "evidence": "P006", "ambiguity": "作者未对其外延作界定。"},
    {"term": "控制狂 / 强迫症", "meaning": "本文指对细节的强迫性控制，作者将其解释为对失败想象的不能忍受与责任感副作用（P005,P006）。", "evidence": "P005", "ambiguity": "未说明是否为临床诊断用法。"},
    {"term": "责任感", "meaning": "与焦虑正相关的压力来源（P006）。", "evidence": "P006", "ambiguity": "未说明何种责任。"},
    {"term": "运气", "meaning": "人对自己不可控因素的信任（P006）。", "evidence": "P006", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "提问者的“老公”：被解释对象（P001-P006），具体行为未在正文出现。",
    "“有情饮水饱”：作者建议使用的安慰话语（P009），属行动建议材料。",
    "“你怎么这么事逼”：作者建议避免的回应（P009），属被否定说法。",
    "未分享这种压力的观察者：被指为误读者（P007,P008）。"
   ],
   "conditions": [
    "判断以“更像是”“大概”“一般”“某种程度上”等限定词给出，非确定断言（P001,P002,P003,P006）。",
    "控制型强迫行为以“人信不过自己的运气”为条件（P006）。",
    "误解的成立前提是观察者“自己没有分享这种压力”（P007）。",
    "建议的情境限定为对方处于这种压力之下时（P009）。"
   ],
   "rhetoric_and_tone": "解释性、体谅式语气，逐句加限定词（更像是/大概/一般/某种程度上）；以引号标出通俗口号“把细节做好，成功会自然到来”；用反问“强迫症哪里是真的喜欢有强迫症呢”；结尾以直接引语形式给出对答建议。",
   "unresolved_questions": [
    "提问者所述“太事逼”的具体行为未在正文展开，无法判断作者的解释覆盖哪些情形（Q001,P001）。",
    "“强迫症”“控制狂”是否为临床意义用法，正文未说明（P005,P006）。",
    "若对方并非“信不过运气”而是其他原因，该解释是否仍适用，正文未说明（P006）。",
    "“有情饮水饱”为何能缓解该压力，正文未给依据（P009）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这更像是想要通过控制一切细节，确保成功和避免失败。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这大概是对现状不满而做的努力。", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P003", "quote": "把细节做好，成功会自然到来", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "那其实是受不了“被这些细节拖累、失去成功的可能”的想象。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "某种程度上，这也可以被认为是高度的责任感带来的副作用。责任越大，焦虑就越重。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这时候如果人信不过自己的运气，那么出现这样的的控制狂、强迫症是难以避免的。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P007", "quote": "就会觉得对方“没有必要的讲究细节”。", "relation": "contradicts"},
    {"key": "E8", "paragraph_id": "P008", "quote": "这是误解。", "relation": "contradicts"},
    {"key": "E9", "paragraph_id": "P009", "quote": "他需要听到你说“有情饮水饱”，而不是“你怎么这么事逼”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系/家庭生活", "行为与心理的解释"],
   "issue_candidates": ["伴侣对细节过分挑剔", "强迫性控制行为的成因", "观察者的误读与沟通用语"],
   "text_function_candidates": ["答疑", "解释", "行动建议"],
   "object_candidates": ["提问者的老公", "未分享压力的观察者"],
   "working_keywords": ["事逼", "控制一切细节", "强迫症", "责任感", "运气", "有情饮水饱"]
  },
  "notes": "提问（Q001）属提问者。无图片节点；provenance/superseded 均为 null。P006 原文含“这样的的”重复字，短引按原文逐字保留。"
 },
 "81405a02": {
  "analysis": {
   "question_context": "提问者问“怎么教训厚颜无耻不知好歹的人？”（Q001），已预设对方厚颜无耻、不知好歹并寻求教训办法。作者先否定“教训”这一处置，进而质疑提问者的定性可能出于受伤泄愤，主张以权利界限与制度裁断处理反对，并把重心转向自我防护与自身价值的衡量。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接回应“不用教训”，理由是对方将来已经怪可怜；并指出提问者不能按自己喜恶下定论，也可能因受伤而给对方贴“厚颜无耻、不知好歹”的标签泄愤。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "人性论据：人是智商很低级的动物，根本层面并不比婴儿好多少；聪明才智多用于把欲望包装成华丽正义而非自我怀疑；聪明人也干低级事；作者自承同样有此本能。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "制度性建议：不能完全相信自己的本能直觉，一切反对以权利界限为界、循社会契约约定的默认途径解决，以免误判造成太深的罪；人类才有法庭和裁判以避免当事人自我正义化；制度不完美但好过自己不高兴就判人死罪。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "替代性裁决：人的命运本身才是最好的法官；若对方真是厚颜无耻、不知好歹，自然慢慢没人帮、将来日子难过，因为谁都不傻。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "自我保护必要但要面向现实、有效管理；最终解决问题靠专注坚持、把自己的路走好、让更多人因你过得更好，你自然越来越被爱，爱你的人才是真正的财富。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "价值衡量：默默爱护你的人是依靠；问题不在有没有人恨你（世上没有不招人恨的人），而在有没有人爱你以及你有没有好好对待爱你的人；价值不以消灭恶人衡量（恶人如蘑菇），而以“最终撑不住之前帮到多少人”衡量。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "收束：人最终会撑不住（总会死），但可以反问“谁说最后一定撑不住就不值得做”；做得一分也是好。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不用教训，ta们将来已经怪可怜的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "提问者不能按自己的喜恶给对方下定论，也有可能是自己受伤后把对方定义为“厚颜无耻、不知好歹”来泄愤。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人是智商很低级的动物，在根本层面上并不比婴儿好多少，不要过于信得过自己肯定公正。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的聪明才智很多时候只用在于把自己的欲望包装得很华丽和正义，并不会用在怀疑自己是否正确；很多聪明人也在干低级的事。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自承同样有这种把欲望包装成正义的本能。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不能完全相信自己的本能直觉，一切的反对都要以权利界限为界、循社会契约约定的默认途径去解决，以防误判造成太深的罪。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "人类设立法庭和裁判以避免当事人自己的自我正义化；这种制度并不完美，但好过自己不高兴就判人死罪。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "追根到底人的命运本身才是最好的法官：如果对方真的是厚颜无耻、不知好歹，自然慢慢就没人帮ta，将来自然日子难过。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谁都不傻，不会上很多回当。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "合理设置防御、自我保护是必要的，以避免过度损失，要面向现实采取有效管理。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最终解决问题靠的是一直专注和坚持，把自己的路走好，让更多的人因为你的存在而过得更好。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "你自然会越来越被爱；爱你的人才是你真正的财富。", "evidence": ["E13", "E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "问题不在于有没有人恨你（世上没有不招任何人恨的人），而在于有没有人爱你，以及爱你的人你有没有尽量好好对待。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "你的价值不能用消灭了几个恶人来衡量——恶人如蘑菇，天气一潮湿就自动长出来，这是低效的做法。", "evidence": ["E16", "E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的价值是用“你在最终撑不住之前，有帮到多少人”来衡量的。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "人最终还是会撑不住的（总会死），但作者反问：谁说最后一定撑不住就不值得做？", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做得一分也是好。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "先否定处置方式并给出理由：不用教训，对方将来已经怪可怜（P001）。",
    "质疑提问者的定性来源：可能出于受伤泄愤，且不能按喜恶定论（P002）。",
    "以人性论支撑上述怀疑：人并不比婴儿高明多少，才智多用于包装欲望，作者自承同有本能（P003-P004）。",
    "由不可信任本能推出程序性要求：以权利界限为界、循社会契约默认途径，故有法庭裁判，虽不完美但胜过自行判死罪（P005-P006）。",
    "提出替代裁决者：命运才是最好的法官，若对方真如此则自然没人帮（P007-P008）。",
    "承认自我防护必要，但把重心定位在专注坚持与自身建设（P009）。",
    "给出价值衡量标准：不以消灭恶人、而以帮到多少人衡量（P013-P014）。",
    "以死亡为前提作让步后反问，收于“做得一分也是好”（P015-P016）。"
   ],
   "concept_usage": [
    {"term": "厚颜无耻、不知好歹", "meaning": "提问者对某类人的定性（Q001）；作者将其视为可能出于受伤泄愤的标签并加以质疑，未确认其外延（P002）。", "evidence": "P002", "ambiguity": "作者未否定该现象存在，只质疑提问者的判断资格。"},
    {"term": "权利界限", "meaning": "作者主张的反对行为边界（P005）。", "evidence": "P005", "ambiguity": "具体界限内容未说明。"},
    {"term": "社会契约约定的默认途径", "meaning": "解决争端的制度化渠道（P005），与法庭裁判相衔接（P005）。", "evidence": "P005", "ambiguity": "在本文未具体化。"},
    {"term": "自我正义化", "meaning": "当事人自行把自身立场正当化；法庭与裁判用以避免之（P005）。", "evidence": "P005", "ambiguity": "无。"},
    {"term": "命运（最好的法官）", "meaning": "指人际后果的自然裁决机制（P007）。", "evidence": "P007", "ambiguity": "作者以“追根到底”引出，未给出机制说明。"},
    {"term": "恶人如蘑菇", "meaning": "比喻恶人自发、易生，用以说明“消灭”思路的低效（P013）。", "evidence": "P013", "ambiguity": "无。"},
    {"term": "价值", "meaning": "以“最终撑不住之前帮到多少人”衡量，并明确不以消灭恶人衡量（P013,P014）。", "evidence": "P014", "ambiguity": "“帮到”的判定标准未说明。"}
   ],
   "examples_and_targets": [
    "提问者所指的“厚颜无耻、不知好歹的人”：被质疑的定性对象（Q001,P002），作者未确认其存在。",
    "法庭和裁判：作者援引的制度例证（P005,P006）。",
    "婴儿：用来支持“人在根本层面并不更高明”的类比（P003）。",
    "蘑菇与空气净化器：比喻及括号内的生活类比（P013），属修辞材料兼建议。",
    "病人、恶人、恨你的人、爱你的人：作者对处境的分类用语（P012）。"
   ],
   "conditions": [
    "“不用教训”以后果立论：对方“将来已经怪可怜”（P001）。",
    "对方会没人帮、日子难过的推论以“如果对方真的是厚颜无耻、不知好歹”为条件（P007）。",
    "自我保护被限定为“合理设置防御”并避免过度损失（P009）。",
    "价值衡量以“最终撑不住之前”即死亡为终点条件（P014,P015）。",
    "制度途径的有效性以存在“权利界限”与“社会契约约定的默认途径”为前提（P005）。"
   ],
   "rhetoric_and_tone": "劝解与训诫混合；开篇即否定提问者的处置方式（“不用教训”），通篇以“你/你自己”直接对话；以“包括我，也一样会有这种本能”自承来降低训诫姿态；用反问“你总会死吧？但谁说最后一定撑不住，就不值得做呢？”；括号内插入空气净化器的生活建议带调侃；以“恶人如蘑菇”设喻。",
   "unresolved_questions": [
    "提问者所指对方的具体行为未在正文出现，无法判断作者质疑的针对性（Q001,P002）。",
    "“权利界限”与“社会契约约定的默认途径”在本文未具体化（P005）。",
    "若不存在可用的裁判途径，作者建议如何适用，正文未说明（P005,P006）。",
    "P001“ta们将来已经怪可怜的”未给出依据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不用教训，ta们将来已经怪可怜的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "也有可能是你自己受伤了，就把对方定义为“厚颜无耻、不知好歹”来泄愤而已。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "人说实话是一种智商很低级的动物，并没有在根本的层面上比婴儿好多少，不要过于信得过自己肯定公正。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "人的聪明才智都只是用在了“把自己的欲望包装得很华丽和正义”上而已，并不会用在“怀疑我这样做是不是正确”上。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "包括我，也一样会有这种本能。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "一切的反对，都要以权利界限为界，循社会契约约定的默认途径去解决，以防万一误判，造成太深的罪。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "所以人类才有法庭和裁判，去避免当事人自己的自我正义化。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "但是好过你自己不高兴了就判人死罪。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P007", "quote": "如果对方真的是厚颜无耻、不知好歹，那么自然慢慢就没人帮ta了，ta将来自然日子难过。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "谁都不傻，不会上很多回当。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "合理设置防御，自我保护肯定是必要的", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P009", "quote": "解决问题靠的是一直专注和坚持，把你自己的路走好，让更多的人因为你的存在而过得更好。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P010", "quote": "你自然会越来越被爱。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P011", "quote": "爱你的人，才是你真正的财富。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P012", "quote": "而在于有没有人爱你，而爱你的人你有没有尽量好好对待。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "你的价值不能用你消灭了几个恶人来衡量", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P013", "quote": "恶人如蘑菇，天气一潮湿就自动的长出来了，这是一种低效的做法", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P014", "quote": "人的价值是用“你在最终撑不住之前，有帮到多少人”来衡量的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P015", "quote": "但谁说最后一定撑不住，就不值得做呢？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P016", "quote": "做得一分也是好。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/处世", "人际冲突与情绪", "制度与争端解决"],
   "issue_candidates": ["是否应当“教训”讨厌的人", "自我正义化与误判风险", "人的价值如何衡量"],
   "text_function_candidates": ["答疑", "劝诫/训诫", "论辩"],
   "object_candidates": ["提问者", "提问者所指的厚颜无耻不知好歹者", "法庭与裁判"],
   "working_keywords": ["厚颜无耻", "不知好歹", "权利界限", "社会契约", "自我正义化", "恶人如蘑菇", "撑不住"]
  },
  "notes": "提问（Q001）属提问者，其“厚颜无耻、不知好歹”的定性未被当作作者判断，作者明确质疑该定性（P002）。无图片节点；provenance/superseded 均为 null。P013 括号内文字为原文自带的插入语。lexical 段落计数为 17，而正文实际分段 16，差 1 应为尾部空段，未标记 text/lexical divergence。"
 },
 "eb01897e": {
  "analysis": {
   "question_context": "提问者问“由绝对真实所构成的世界是更美好还是更残酷？”（Q001），是二选一的评价性问题。作者不选任何一边，先否定问题前提（世界不分真实与虚幻），把“真实/虚幻”重解为对自己认知的信心表达，把发问动因归为对失败的恐惧与决策困境，再给出研究与价值观重建的出路，最后指出对无此出路者问题只会有坏答案。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "否定前提并重下定义：世界不分所谓真实和虚幻；人对世界的认知只有一个（用来预测下一步并决定我该做什么的那一个）；“真实”“虚幻”只是对自己的了解的信心足不足的曲折表达。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "说明摇摆之痛与被转换的问题：过度害怕时在若干版本（若干人生选择）间摇摆，产生“到底哪个是真实的”的痛苦；人们真正关心的是哪个决策对、结果好，只是不自觉地把决策困境用“如果认知是真实的，结果就会好”变换成认识问题。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "反驳以认识论方式求解：谈物理定律、科学实验、学术文献、历史经验没有用，因为每种“真实”都有同样自洽的竞争对手；根本原因不在认识能力，而在于过于害怕失败，用犹豫不决、两边下注、多等等、多看看、多靠靠来拖延逃避，并把恐惧伪装成“学术研究”的样子。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "提出真问题与其定义：真正要解决的是如何消灭失败本身，即通过深思熟虑的价值观建设消除失败的可能性，使所有结果都是不同意义的成功。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "溏心卤蛋例证：方案A四处找做法确保煮成功，煮不出即失败；方案B设计可复现实验计划并记录，即使全没煮出也知道哪些方法不好（成功），煮出则成功加二，还练习了研究开放问题的能力；对方案B只要记录足够就没有失败可言。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "结论与价值重估：从对失败的恐惧与对成功的执着中解脱；不了解完全真实的世界不是可怕威胁，反而如名剧、陈酿，不知道它真实的样子并不可怕反而可慕；最讽刺的是能看到多种“难以判断真伪的世界版本”背后不过是恐惧在耳边低语；心无挂碍才会面对真实的未知、才知道自己不知道什么；只有真实的未知才是历史留给你的礼物，可以成为幸福源泉。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032"], "summary": "方法一：利用“真理探索只要有效就无所谓失败”为一切计划赋予严肃有效的研究意义，具体三件事——熟悉该方向已做过的工作不重新造轮子；具备设计具有有效检验效力的试验方案的能力；设计记录过程的方案（结果不重要，准确完善的记录至关重要）。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "方法二及其受限条件：重建人生价值观；若价值观只是最大限度追求个人快感则策略无效，因为没有“可接受结果不好只要过程记录”的从容；记录只为自己时复用机会有限；可多次复用的东西探索余地极小、属“实践学习”，难享失败豁免；真正的认识空白与复杂问题（如开企业、提供有竞争力的产品）一旦失败，经验大概率不由自己再用、时机可能确实失去；除非成为公共智慧财产否则对本人价值不大，而捐为公共财产也难获有效回报；故把探索传递给家族下一代（尤其承担赡养义务者）是一种重要补救。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "退路断绝的反例：若没有这样的下一代或不相信其承担赡养义务，盈利成败再次成为不可承受之重，又回到“真实世界是否特别痛苦”之问，且除“是的，真的痛苦”不会有其他结论；不是没有其他答案，而是即使有人说“很幸福”你也无力相信——比起可怕的真实更怕信了美好幻觉吃大亏；在你问之前就已注定只有坏答案可以被接受，而你也无力停止自我折磨。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P050", "P051"], "summary": "收束：反问“你们看明白问题的根源在哪了吗”，并希望这些话能让读者少受无谓的痛苦。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界其实是不分所谓真实和虚幻的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对世界的认知只有一个，就是自己用来预测“下一步会发生什么”然后决定“我该做什么”的那一个。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“真实”和“虚幻”只是人对自己的这种了解的信心的一种巧妙的曲折表达：信心十足就认定自己了解真实世界，信心不足就觉得自己的认识是虚幻。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "因过度害怕而在若干版本（也可理解为若干人生选择）间摇摆时，人就会产生“到底哪个是真实的”这样的痛苦。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们关心的并不是到底哪个是真实的，而是哪个决策会是对的、结果会好、能改善处境；只是不自觉地把决策困境通过“如果认知是真实的，结果就会好”变换成了一个认识问题。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "用物理定律、科学实验、学术文献、历史经验与人们探讨哪个认识是真实的没有用，因为你所“销售”的每一种“真实”几乎都有同样自洽、合理、证据充足、历史悠久的竞争对手。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们解决不了“到底哪是对世界的真实认知”的根本原因不在于认识能力，而在于过于害怕失败，想靠犹豫不决、两边下注、多等等、多看看、多靠靠来拖延、逃避失败提前变成现实，并把这种逃避与恐惧伪装成“学术研究”的样子。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正要解决的是如何消灭失败本身；即通过深思熟虑的价值观的建设将失败的可能性消除掉，使得所有结果都是不同意义的成功。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "对方案B（设计可复现实验并记录）而言，只要做好足够的记录，就没有失败可言。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "走到这一步就能从对失败的恐惧和成功的执着里解脱出来：不了解完全真实的世界不是可怕威胁，反而犹如闻名已久的名剧、舍不得品尝的陈酿；不知道它真实的样子并不可怕，反而可慕。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "走到这步反而能看到至少有很多版本的所谓难以“判断真伪的世界版本”，背后不过是恐惧这个魔鬼在耳边低语。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "心无挂碍才会面对真实的未知、才会知道自己到底不知道什么；只有真实的未知才是历史留给你的礼物，我们不知道真实的世界是什么样，但这本可以是你的幸福源泉。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "方法一：利用“真理探索只要有效就无所谓失败”的特性为一切计划赋予严肃而有效的研究的意义；必做三件事——熟悉所选方向上已做过的工作、不重新造轮子，具备设计有有效检验效力的试验方案的能力，设计记录过程的方案（计划的结果并不重要，准确完善的记录才至关重要）。", "evidence": ["E17", "E18", "E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果你的人生价值观就是最大限度追求个人快感，这些策略对你是无效的，因为最终意义上你没有“可以接受结果不好只要得到过程记录”的从容。", "evidence": ["E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "记录若只为自己准备，再次用上它的机会有限；能在生命中多次复用的东西探索余地极小，早已被几千年文明史中的前辈试过，做的是“实践学习”，不容易享受到失败豁免效应福利。", "evidence": ["E22", "E23"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "对真正的认识空白与真正复杂的问题（如如何开一家有效的企业、如何提供一种有竞争力的产品），若你失败了，经验大概率不会由你自己再次利用；下一次很可能不能再做这件产品、也不能再次尝试这样的生意，因为时机对你个人可能确实失去了。", "evidence": ["E24", "E25"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "你的探索除非成为某种公共智慧财产，你本人是没有太大的价值的；而捐献出来成为公共智慧财产，你也很难获得公共的多少有效回报。", "evidence": ["E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把这份探索传递给自己的家族下一代（尤其是对你承担赡养义务的下一代）是一种重要的补救。", "evidence": ["E27"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若没有这样的下一代，或你并不相信ta们对赡养义务的承担，盈利上的成败就会再次成为不可承受之重，又会回到“到底什么是真实的世界、是否特别痛苦”的追问。", "evidence": ["E28", "E29"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种追问除了“是的，真的痛苦”不会有其他结论；并非没有其他答案，而是即使有人告诉你“不，很幸福”，你也没有能力相信——比起“可怕的真实”，你更害怕信了“美好的幻觉”吃大亏。", "evidence": ["E30", "E31"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美好的必须是幻觉，否则你可能会信，然后每分每秒都会害怕信错；这样的“信”本身没有什么快乐可言；在你问之前其实就已经注定只有坏的答案才可以被接受，而你也无力停止自我折磨。", "evidence": ["E32", "E33", "E34"]}
   ],
   "argument_steps": [
    "先否定问题的前提：世界不分真实与虚幻（P001）。",
    "重下定义：认知只有一个（预测＋决策用），真实/虚幻是信心的曲折表达（P002-P003）。",
    "描述现象：过度害怕导致在若干版本间摇摆并产生“哪个真实”的痛苦（P004）。",
    "揭示真正的关切：决策对不对、结果好不好，认识问题是由此变换而来（P005）。",
    "反驳以证据说服的路径：每一种“真实”都有自洽的竞争对手，故说服无用（P006-P007）。",
    "归因转换：问题不在认识能力，而在逃避失败并把恐惧伪装成学术研究（P008）。",
    "提出真问题并定义“消灭失败本身”（P009-P010）。",
    "以溏心卤蛋方案A/B对照例证“无失败”的做法（P011-P019）。",
    "得出结论并重估未知：解脱、可慕的未知、恐惧的低语（P020-P026）。",
    "给出方法一（研究化＋三件必做工作）（P027-P032）。",
    "给出方法二（价值观重建）并限定：追求个人快感者无效（P033-P034）。",
    "追问记录为谁而作，指出复用限制与公共财产的回报不足（P035-P040）。",
    "提出家族继承作为补救，并设定其条件（P041-P042）。",
    "以条件不成立的推演作反证：回到“真的痛苦”，且只有坏答案可被接受（P043-P049）。",
    "以反问与祝愿收束（P050-P051）。"
   ],
   "concept_usage": [
    {"term": "真实 / 虚幻", "meaning": "不是世界的属性，而是人对自己的了解的信心足或不足的表达（P003）；作者否定世界本身分真实与虚幻（P001）。", "evidence": "P003", "ambiguity": "作者仍沿用“完全真实的世界”一语（P020），与 P001 的否定并存，存在用语张力。"},
    {"term": "对世界的认知", "meaning": "只有一个，即用来预测“下一步会发生什么”并决定“我该做什么”的那一个（P002）。", "evidence": "P002", "ambiguity": "无。"},
    {"term": "消灭失败本身", "meaning": "通过深思熟虑的价值观建设消除失败的可能性，使所有结果都是不同意义的成功（P010）。", "evidence": "P010", "ambiguity": "价值观建设的具体内容未给出。"},
    {"term": "研究 / 学术研究", "meaning": "正面用法指有效力、有记录的真理探索（P028,P031,P032）；反面用法指逃避失败的伪装（P008），同词两义需区分。", "evidence": "P008", "ambiguity": "作者未给出区分真研究与伪装的判据。"},
    {"term": "检验效力", "meaning": "试验方案能得出有效经验教训的性质（P031）。", "evidence": "P031", "ambiguity": "判定标准未说明。"},
    {"term": "公共智慧财产", "meaning": "探索成果公开后成为公共可用的知识资产（P040）。", "evidence": "P040", "ambiguity": "与“有效回报”的对应关系未展开。"},
    {"term": "心无挂碍", "meaning": "摆脱对失败的恐惧与对成功的执着之后的状态，是面对真实的未知的条件（P023）。", "evidence": "P023", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "溏心卤蛋（方案A查要诀求成功 vs 方案B做可复现实验并记录）：作者自举例证，用于对照有失败与无失败两种做法（P011-P019）。",
    "物理定律、科学实验、学术文献、历史经验：被作者指为说服无效的说理材料（P006）。",
    "“如何开一家有效的企业”“如何提供一种有竞争力的产品”：作者举的真正的认识空白与复杂问题（P038）。",
    "闻名已久的名剧、舍不得品尝的陈酿：比喻（P020）。",
    "恐惧这个魔鬼在你耳边低语：拟人化比喻（P022）。",
    "家族下一代（尤其承担赡养义务者）：作者提出的经验承接者（P041）；没有或不信任该义务的下一代则是反例条件（P042）。",
    "追求个人快感的人生价值观：被作者设为策略失效的条件性对象（P034）。"
   ],
   "conditions": [
    "论证对象限定为过度害怕、过于害怕失败的人（P004,P008）。",
    "方法一以“真理探索只要有效就无所谓失败”的特性为适用前提（P028）。",
    "方法二在“人生价值观就是最大限度的追求个人快感”时无效（P034）。",
    "失败豁免对可多次复用的内容不适用，真正的认识空白与复杂问题又受“个人时机失去”限制（P037,P038,P039）。",
    "经验传递作为补救以有下一代且相信其承担赡养义务为条件，否则结论回到“真的痛苦”（P041,P042,P043）。",
    "方案B以能稳定买到同样鸡蛋、找到同样测量工具厨具的可复现实验计划、以及足够的记录为条件（P015,P019）。"
   ],
   "rhetoric_and_tone": "分析性长文；第二人称“你/你们”混用，直接对读者说理；多次反问（“到底哪个是真实的”“为什么呢”“你们看明白问题的根源在哪了吗”）；以“销售”“小公式”“魔鬼”“名剧”“陈酿”等比喻与轻度讽刺（“最讽刺的事情就出现了”）；以溏心卤蛋这一日常事例作类比；结构上先破后立，再以条件不成立的反例收束。",
   "unresolved_questions": [
    "作者未正面回答提问者“更美好还是更残酷”的二选一，而是改写问题（Q001,P001）。",
    "“深思熟虑的价值观的建设”具体包含什么，正文未给出（P010）。",
    "P031“具有有效检验效力的试验方案”的判定标准未说明。",
    "作者以“公共的多少有效回报”不足为由转向家族继承（P040,P041），该判断的依据未给出。",
    "P004“若干版本”与“若干种人生选择”是否为同一所指，作者仅以“这也可以被理解为”带过。",
    "P050-P051 的“你们”具体所指（提问者以外的读者？）未明示。",
    "P001 否定世界分真实虚幻，P020 又谈“完全真实的世界”，用语是否自洽需研究者复核（待外部核查属解释问题，非事实核查）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "遗憾的是，世界其实是不分所谓真实和虚幻的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "人对世界的认知只有一个，就是自己用来预测“下一步会发生什么”然后决定“我该做什么”的那一个。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "所谓的“真实”和“虚幻”，只是人对自己的这种对世界的了解的信心的一种巧妙的曲折表达。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "时，人就会产生“到底哪个是真实的”这样的痛苦。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "ta们只是不自觉的把这种自己解不开的决策困境，通过“如果认知是真实的，结果就会好”这个小公式变换成了一个认识问题。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "你会发现这是没有用的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "因为你所“销售”的每一种“真实”，几乎都有同样自洽的、合理的、证据充足的、历史悠久的竞争对手。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "ta们只是把这种逃避、恐惧，伪装成了“学术研究”的样子。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "你真正要解决的，是如何消灭失败本身。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "就是通过深思熟虑的价值观的建设将失败的可能性消除掉，使得所有的结果都是不同意义的成功。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "对于方案B而言，只要做好足够的记录，就没有失败可言。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "你会发现，这时候你就能从对失败的恐惧和成功的执着里解脱出来", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "并不是可怕的，反而是可慕的。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "背后不过是恐惧这个魔鬼在你耳边低语。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "心无挂碍，你才会面对真实的未知。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "只有真实的未知，才是历史留给你的礼物。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P028", "quote": "首先，就是利用“真理探索只要有效就无所谓失败”的特性，为你的一切计划赋予严肃而有效的研究的意义。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P030", "quote": "第一，你需要熟悉在你所选择的真理探索方向上已经做过的工作，不要重新造轮子；", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "你要有设计具有有效检验效力的试验方案的能力", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "某种意义上说，计划的结果并不重要，准确完善的记录才至关重要。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P034", "quote": "如果你的人生价值观就是最大限度的追求个人快感的话，这些策略对你是无效的。", "relation": "qualifies"},
    {"key": "E22", "paragraph_id": "P036", "quote": "因为这份记录如果只是为你自己准备的，那么你会很清楚你再次能用上它的机会是有限的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "这是不容易享受到上面的失败豁免效应福利的。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "如果你失败了，那么你的经验大概率不会是你自己来再次利用。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P039", "quote": "因为对你个人而言，这个时机可能确实失去了。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P040", "quote": "而你捐献出来成为公共智慧财产，你也很难获得公共的多少有效回报。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P041", "quote": "把这份探索传递给自己的家族下一代（尤其是对你承担赡养义务的下一代）是一种重要的补救。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P042", "quote": "但如果你没有这样的下一代，或者你并不相信ta们对赡养义务的承担。", "relation": "qualifies"},
    {"key": "E29", "paragraph_id": "P043", "quote": "这个时候，你就会发现具体的盈利上的成败就再次成为了不可承受之重。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P045", "quote": "而且除了“是的，真的痛苦”，你不会得到其他结论的。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P046", "quote": "比起“可怕的真实”，你更害怕信了“美好的幻觉”吃大亏。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P047", "quote": "美好的必须是幻觉，否则你可能会信，然后你每分每秒都会害怕，会想象信错了。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P048", "quote": "在你问之前，其实就已经注定只有坏的答案才可以被接受了。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P049", "quote": "而你也无力停止自我折磨。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认识论/认知与决策", "价值观与人生策略", "情绪与恐惧心理"],
   "issue_candidates": ["真实与虚幻之辨", "面对失败与不确定性", "拖延与两边下注", "经验传承与价值观重建"],
   "text_function_candidates": ["答疑", "论辩", "方法论建议", "概念辨析"],
   "object_candidates": ["提问者", "追问真实世界的发问者", "家族下一代"],
   "working_keywords": ["真实", "虚幻", "消灭失败本身", "失败豁免效应", "检验效力", "溏心卤蛋", "心无挂碍", "公共智慧财产"]
  },
  "notes": "提问（Q001）属提问者，其二选一表述未被当作作者立场，作者改写问题前提。无图片节点；provenance/superseded 均为 null。作者在否定“真实/虚幻”之分（P001）之后仍沿用“完全真实的世界”“真实的未知”等说法（P020,P023,P025），属本篇用语张力，未作改写，留待研究者复核。"
 },
 "1f1595c3": {
  "analysis": {
   "question_context": "提问者问如何看待网上动不动就“屁股歪了”的评价（Q001），问题指向一种网络公共讨论现象。作者不评价该现象的是非，而是陈述自己把这类说法与“先论立场再论是非”的习惯视为禁忌并提前拉黑的个人规则及其理由。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "个人规则：该词对作者是禁忌词；凡对作者说这种话的、或被作者认为有先论立场再论是非习惯的（哪怕暗示性的，含评论区内、别处回答评论区遇到、从未交谈过的），作者都会提前拉黑，即使误判也在所不惜。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007"], "summary": "理由一：这样的人对“讨论问题”这个问题来说，“屁股是歪的”。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "理由二：他们根本没有值得人探讨时间的价值——不是没有知识，而是这种习惯者拥有稀缺、新鲜、一般视野所不及知识的概率太低，而后者才真正值得时间；他们终日网上游荡，用点赞关注奖赏站队者、用踩和攻击性评论惩罚不站队者。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "范围与准则：不限于狭隘民族主义者，也包括所谓pro-democracy的一群；与具体立场无关，而与人的行为准则有关；有立场没问题，只有立场没有是非才令人敬谢不敏。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "结论：你不拉黑他们你什么也干不了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“屁股歪了”这类说法对作者是禁忌词。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "凡对作者说这种话的、或被作者认为有先论立场再论是非习惯的人（含暗示性的，含在作者评论区、别处回答或评论区遇到而从未交谈过的），作者都会提前拉黑，即使误判也在所不惜。", "evidence": ["E2", "E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样的人对“讨论问题”这个问题来说“屁股是歪的”。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他们根本没有值得人探讨时间的价值：不是因为他们没有知识，而是有这样习惯的人拥有稀缺的、新鲜的、一般视野所不及的知识的概率太低，而后者才是真正值得时间的东西。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他们终日所做的只是在网上游荡，想拿不值钱的点赞和关注奖赏站队者，拿踩和攻击性的评论尝试惩罚不站队的人。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这并不限于狭隘民族主义者，也包括所谓的pro-democracy的一群；这跟具体的立场没有关系，而是跟人的行为准则有关系。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有立场什么问题也没有，但是只有立场、没有是非就令人敬谢不敏。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你不拉黑他们你什么也干不了。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "先声明个人规则：该词是禁忌词（P001）。",
    "界定触发条件：对我说这种话者、或有此习惯者，含暗示性与未交谈者（P002-P004）。",
    "声明执行方式与代价承受：提前拉黑，误判也在所不惜（P005-P006）。",
    "给出第一条理由：此类人对“讨论问题”本身“屁股是歪的”（P007）。",
    "给出第二条理由：其拥有稀缺新鲜知识的概率太低，故不值得时间；并描述其主要行为（点赞奖赏站队、踩与攻击惩罚不站队）（P008-P009）。",
    "限定范围与准则：不限立场阵营，关键在行为准则；有立场无问题，只有立场没有是非不可取（P010-P011）。",
    "以断言收束：不拉黑就什么也干不了（P012）。"
   ],
   "concept_usage": [
    {"term": "屁股歪了 / 屁股是歪的", "meaning": "提问者所问的网络评价用语（Q001）；作者把它当作“先论立场再论是非”习惯的标志，并在正文中以引号复用该词（P002,P007）。", "evidence": "P007", "ambiguity": "作者未给该词的判定标准，只在引号中借用。"},
    {"term": "禁忌词", "meaning": "作者对该词的个人态度标记，触发提前拉黑（P001）。", "evidence": "P001", "ambiguity": "无。"},
    {"term": "拉黑", "meaning": "作者的处理方式，包含对未交谈者的预防性拉黑（P004,P005）。", "evidence": "P005", "ambiguity": "未说明是否等同于否认其公共讨论资格。"},
    {"term": "先论立场再论是非", "meaning": "作者界定的禁忌习惯，与“有立场”区分开（P002,P011）。", "evidence": "P002", "ambiguity": "判定标准未给出。"},
    {"term": "狭隘民族主义者 / pro-democracy 的一群", "meaning": "作者点出的两类同样适用的群体（P010）。", "evidence": "P010", "ambiguity": "两类群体的具体所指未说明。"},
    {"term": "稀缺的、新鲜的、一般视野所不及的知识", "meaning": "作者认为真正值得时间的东西（P008）。", "evidence": "P008", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "说“屁股歪了”的人及被认为有先论立场再论是非习惯的人：作者的拉黑对象（P002-P005），属被批评对象。",
    "作者的评论区、别的回答与评论区：作者遇到此类人的场景（P004）。",
    "狭隘民族主义者、所谓pro-democracy的一群：作者点名的两类群体（P010），属被批评对象，非引用。",
    "不值钱的“点赞”和“关注”、踩和攻击性的评论：作者描述的这类人的行为手段（P009）。"
   ],
   "conditions": [
    "拉黑以“对我说这种话”或“被我认为有这种习惯”为条件，并扩展到“哪怕是暗示性的”（P002,P003）。",
    "作者明示包含误判可能：即使误判也在所不惜（P006）。",
    "判断被限定为与具体立场无关、只与行为准则有关（P010,P011）。",
    "拉黑范围包含从未交谈者，即不以其实际发言为前提（P004）。"
   ],
   "rhetoric_and_tone": "第一人称声明式，短句分行罗列规则（P002-P006 近乎清单）；语气决绝并自我限定范围（“对我是禁忌词”），明示不惜误判；对批评对象使用“终日游荡”“不值钱的点赞”等贬抑措辞；结尾为断言式结论（P012）。",
   "unresolved_questions": [
    "作者未回答提问者在公共层面“如何看待”这类评价的问题，只陈述个人处置规则（Q001,P001）。",
    "“先论立场再论是非”的判定标准未给出，作者自承可能误判（P002,P006）。",
    "“所谓的pro-democracy的一群”具体所指未说明（P010）。",
    "P008 否定其讨论价值与 P012 的“什么也干不了”之间的关系（是效果判断还是价值判断）未进一步说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个词对我是禁忌词。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "凡是对我说这种话的，或者被我认为有这种先论立场再论是非的习惯的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "包括我的评论区以内遇到的、在别的回答、评论区中闲逛遇到的、根本没说过一句话的，", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "我都会提前拉黑。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "即使误判也在所不惜。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P007", "quote": "因为这样的人对“讨论问题”这个问题来说，“屁股是歪的”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "他们根本没有值得人探讨时间的价值", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "拥有稀缺的、新鲜的、一般视野所不及的知识的概率太低——而后者才是真正值得时间的东西。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "拿不值钱的“点赞”和“关注”来奖赏别人站ta那一队，拿踩和攻击性的评论尝试惩罚不站ta们这一队的人。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "这并不限于狭隘民族主义者，也包括所谓的pro-democracy的一群。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "这其实跟具体的立场没有关系，是跟人的行为准则有关系。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "有立场什么问题也没有，但是只有立场、没有是非就令人敬谢不敏。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "你不拉黑他们你什么也干不了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["网络讨论文化", "言论与行为准则", "个人边界与自我管理"],
   "issue_candidates": ["“屁股歪了”式站队评价", "立场与是非的关系", "以拉黑应对立场先行者"],
   "text_function_candidates": ["答疑（偏个人立场声明）", "批评", "经验总结"],
   "object_candidates": ["提问者", "说“屁股歪了”的人", "狭隘民族主义者", "所谓pro-democracy的一群", "作者本人"],
   "working_keywords": ["屁股歪了", "禁忌词", "拉黑", "先论立场再论是非", "行为准则", "点赞", "关注"]
  },
  "notes": "提问（Q001）属提问者；作者只陈述个人规则，未对公共现象作整体评价。无图片节点；provenance/superseded 均为 null。P007 中的“屁股是歪的”为作者加引号复用的说法。"
 },
 "c947b0a0": {
  "analysis": {
   "question_context": "提问者问人在年轻的时候最核心的能力是什么（Q001）。作者主张是“无歧义、完备、简洁的表达能力”，先给三项要求的定义与地位论证，再列出一系列训练科目与练习步骤；正文首两段夹有专栏/练习入口文字，正文以“（未完，待续）”结束，且多处指向示例图片。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "栏目与练习入口信息：练习总集锦、投稿到该专栏、作者会做示范和点评。与论证无直接关系，疑为平台/栏目导引文字。", "role": "other"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "主张：人需要拥有的最重要的核心能力，就是无歧义、完备、简洁的表达能力。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "定义三项要求：无歧义＝极大压缩所有人把A理解为B的可能性（无错）；完备性＝待指各项中没有被遗漏的必要要素（含必要语素）（无漏）；简洁＝达到同样表达效果前提下占用人最少的理解资源（无费）。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "论证地位：该能力强度直接关系到将来能达到的高度；因为学习就是在意识里构建对世界的无错、无漏的表达；学习成果本质上只是【你的判断力支撑之下】的一组你看不出如何有错有漏的关于世界的表达。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017"], "summary": "判断力的上限与第三条要求的必要性：判断力决定水准的极限；表达若不简洁，有限的“运存”难以在一次运算中容纳足够命题，影响察觉错漏的能力，从而锁定无错无漏的水准上限；人只能把能力提高到觉察不出错漏的程度。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "定性：从纯技术性能力上说这是一切其它能力的底层、核心中的核心；是七十二绝技背后的那个小无相功；是评价子女学术进步时唯一真正需要关心的指标；它事实上就是学习能力、理解能力、探索能力、创造力的实质，其他名字只是同一能力在不同场景下的别称。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "精英论：这是精英与非精英的真正分界；精英不按社会地位而本质按此能力划分，完全可能在社会决策链的中下层；该能力强的人必非池中之物，若环境存在天花板，最强者有强烈趋势达到甚至打穿天花板。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035"], "summary": "训练科目一（画面关系表达）：与朋友各搜配置相当的平面房型图，用语音指引对方在不看图前提下绘制墙体、窗户、门、楼梯等基本结构（不含软装），记录到墙体封闭最后一笔的总时间T，比较差异、交换角色再测，应观察到T值有效下降与误差逐次缩小。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P036", "P037"], "summary": "练习参考行，文本为“1″、核心能力训练 | 房屋布局表述方案汇总”，疑为外部链接/标题文字混入正文。", "role": "other"},
    {"unit_id": "U010", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043"], "summary": "进阶练习：默写世界各地的行政区划轮廓图（如中国各省、市地图）；先观察图形并转化为文字表述，再脱离参考物按文字表述默写，最后与原图对照，应观察到越来越准确和迅速。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P044", "P045", "P046", "P047"], "summary": "练习2：找有演出剧本可参考的影视，观看后自行反推剧本（台词不必全写），写好一幕与原剧本对照；建议找英文剧本，因中文剧本一般过于侧重台词。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "科目二（关系描述）与练习：为集合中每个个体建立唯一代号编码系统，要求规则尽可能简短且他人依同一规则得出完全相同的代号；进阶为取常见物品“爆炸图”为每个零件命名，要求命名唯一且他人能据命名准确识别；命名典范要求有足够的望文生义性、高度简洁性和明显区分性。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067"], "summary": "科目三（结构化表达与图形建模）：结构化口头与文字表达、编制表格、用表达式描述数学关系、用坐标图/饼图/柱图等表达数值关系、绘制规范流程图、用例图/时序图/类图（UML）、绘制透视准确的线条素描。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P068", "P069", "P070", "P071", "P072", "P073", "P074"], "summary": "素描相关练习与进阶：绘制任意角度1:1:1比例的立方块轴测图（尺寸准确）；熟练较简单立体形状轴测图；参考实物或图片绘制三点透视单反相机（附件齐全且角度须与图片不同）；绘制桌上互相堆叠的单反相机。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P075", "P076", "P077", "P078", "P079"], "summary": "如可能则掌握快速表现技法（建筑类、产品设计类）；练习用简单线条绘制自己的客厅、表达街景。", "role": "action_advice"},
    {"unit_id": "U016", "paragraph_refs": ["P080", "P081", "P082", "P083"], "summary": "如可能则掌握简单3D建模工具、最好进一步掌握3D打印技术；如可能则掌握油泥造型能力；学会绘制标准（工业/建筑）图纸。", "role": "action_advice"},
    {"unit_id": "U017", "paragraph_refs": ["P084", "P085", "P086", "P087", "P088", "P089"], "summary": "信息分类科目与练习：学会尽可能系统的信息分类技术（图书馆学、情报学）；为自己的电脑文件构建绝对完备的编目，要求任一文件可依分类体系准确预测位置，且无论增加什么类型文件都不导致原有分类改名或原有文件重新归类。", "role": "action_advice"},
    {"unit_id": "U018", "paragraph_refs": ["P090"], "summary": "文末自注“（未完，待续）”，正文未完结。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人需要拥有的最重要的核心能力，就是无歧义、完备、简洁的表达能力。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无歧义指极大的压缩所有人把A理解为B的可能性，即无错。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "完备性指待指各项之中没有被遗漏的必要的要素（也包括语句中必要的语素），即无漏。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "简洁指在达到同样的表达效果的前提下，占用人最少的理解资源，即无费。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "一个人无错、无漏、无费的表达能力有多强，直接关系到ta将来能达到的高度。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓的学习就是在自己的意识里构建对世界的无错、无漏的表达；学习的成果本质上只是【你的判断力支撑之下】的一组你看不出如何有错、如何有漏的关于世界的表达。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你的判断力决定了你的水准的极限。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为这种表达若不尽量简洁，你有限的运存就很难在一次运算中容纳足够的命题，这会直接影响察觉错与漏的能力，从而锁定你对世界的表达能力的无错、无漏的水准上限。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你只能将自己的能力提高到自己觉察不出错和漏的程度；你觉察错漏的能力有多高，就决定了你的思维能力的极限。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从纯粹技术性的能力上说，这是一切其它能力的底层，是核心中的核心。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这项能力就是七十二绝技背后的那个小无相功，是评价子女学术进步时唯一真正需要关心的指标；它事实上就是学习能力、理解能力、探索能力、创造力的实质，其他名字只是同一能力在不同场景、上下文中的别称。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这就是精英与非精英的真正分界：精英不是按社会地位分，而是本质按这个能力分，完全可能在社会决策链的中下层。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "这个能力强的人必非池中之物；如果这个环境是存在天花板的，这个能力最强的人有强烈的趋势会达到天花板，甚至把天花板打穿。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列出一套训练科目与具体练习（画面关系表达、关系描述与编码命名、结构化表达与图形建模、透视素描与三维、信息分类），并给出操作步骤与预期观察结果（如T值有效下降、误差逐次缩小、默写越来越准确迅速）。", "evidence": ["E20", "E21", "E22", "E25"]}
   ],
   "argument_steps": [
    "先给主张：最重要的核心能力是无歧义、完备、简洁的表达能力（P003）。",
    "逐项定义：无错（无歧义）、无漏（完备）、无费（简洁）（P005-P007）。",
    "以“关系到将来能达到的高度”立重要性（P008），并设问为什么关键（P009）。",
    "以学习的定义作答：学习即构建对世界的无错无漏表达，其成果受判断力支撑（P010-P011）。",
    "点出“魔鬼”即判断力限制水准极限（P012-P013）。",
    "由此推出第三条要求无费：不简洁则运存不足、难以察觉错漏，锁定上限（P014-P017）。",
    "上升定性：一切能力的底层、核心中的核心、小无相功、各类能力的实质与别称（P018-P022）。",
    "扩展为精英判据并给出天花板趋势（P023-P026）。",
    "转入操作层：列训练科目与练习步骤、进阶与预期观察结果（P027-P089）。",
    "自注未完结（P090）。"
   ],
   "concept_usage": [
    {"term": "无歧义 / 无错", "meaning": "极大压缩所有人把A理解为B的可能性（P005）。", "evidence": "P005", "ambiguity": "“极大压缩”到何种程度算达标未说明。"},
    {"term": "完备性 / 无漏", "meaning": "待指各项之中没有被遗漏的必要要素，也包括语句中必要的语素（P006）。", "evidence": "P006", "ambiguity": "“必要要素”的判定标准未说明。"},
    {"term": "简洁 / 无费", "meaning": "在达到同样表达效果的前提下占用人最少的理解资源（P007）。", "evidence": "P007", "ambiguity": "“理解资源”未量化。"},
    {"term": "判断力", "meaning": "决定表达能力与水准极限的支撑条件（P011,P013）。", "evidence": "P013", "ambiguity": "判断力本身如何形成未说明。"},
    {"term": "运存", "meaning": "借用计算机术语比喻一次运算中可容纳的命题量（P015）。", "evidence": "P015", "ambiguity": "非严格术语，未定义。"},
    {"term": "精英", "meaning": "本文不按社会地位、而本质按该项表达能力界定（P024,P025）。", "evidence": "P024", "ambiguity": "与通常社会含义的差异作者未展开。"},
    {"term": "小无相功 / 七十二绝技", "meaning": "借用武侠设定的比喻，指该能力是其他技能背后的根基（P019）。", "evidence": "P019", "ambiguity": "比喻来源未注明。"}
   ],
   "examples_and_targets": [
    "平面房型图语音指引绘制练习（含计时T、交换角色）：作者设计的训练例（P031-P035）。",
    "世界行政区划轮廓图默写（如中国各省、市地图）：进阶练习例（P039）。",
    "影视剧本反推（建议英文剧本）：练习2（P045-P047）。",
    "“爆炸图”零件命名与命名典范：编码命名练习（P053,P055）。",
    "UML、轴测图、三点透视单反相机、客厅与街景速写、3D打印、油泥造型：作者列举的科目（P065,P069,P073,P074,P078,P079,P081,P082）。",
    "电脑文件编目：信息分类练习（P087-P089）。",
    "图片节点 IMG001-IMG010：正文以“例如下图”“参考下图”“如下”指向示例图，内容未核验（P031,P036,P054,P055,P078,P079）。",
    "“练习总集锦”与该专栏：平台/栏目导引文字（P002）。"
   ],
   "conditions": [
    "房型图练习限定为配置相当的平面房型图，且绘制“不含软装”、以墙体封闭的最后一笔计时（P031,P032）。",
    "编码/命名以“其他人依照这一规则……会得出完全相同的代号”为成立条件（P051）。",
    "素描进阶要求绘制角度必须与参考图片角度不同（P073）。",
    "简洁性限定为“在达到同样的表达效果的前提下”（P007）。",
    "关于天花板打穿的判断以“如果这个环境是存在天花板的”为条件（P026）。",
    "3D建模/3D打印、油泥造型、快速表现技法等科目均以“如果可能”为条件（P075,P080,P081,P082）。",
    "正文自注“（未完，待续）”，科目未列完（P090）。"
   ],
   "rhetoric_and_tone": "教学与训练手册语气；先以定义式短句立论（无错/无漏/无费），再以“核心中的核心”“七十二绝技背后的那个小无相功”等比喻抬高该能力；有直接对读者的设问（“为什么这个能力如此的关键呢？”“你们看到魔鬼了吗？”）与“把它涂黑给你们看”这类带格式暗示的表达；科目部分为清单式祈使句；夹入专栏导引（P002）与链接式文本（P037）。",
   "unresolved_questions": [
    "本篇含 10 个图片节点（IMG001-IMG010），正文多处以“例如下图”“参考下图”“如下”指向示例图，图片内容未经核验，需人工/多模态复核（P031,P036,P054,P055,P078,P079）。",
    "因图片未核验，本篇不得标记 read，image_checked=False，status=needs_reread。",
    "P001“提升核心能力科目练习”与 P037“1″、核心能力训练 | 房屋布局表述方案汇总”为 lexical 未覆盖片段（文本/结构差异 2 处），疑为标题或链接文字混入正文，性质待人工确认。",
    "P002“这里有练习总集锦。做了练习可以申请投稿到这个专栏”疑为平台栏目导引或推广文字混入正文，其归属（作者本人栏目还是平台生成）待核。",
    "P028/P029、P048/P049、P057-P059、P060-P062、P063-P065、P066/P067、P075/P076、P080-P083、P084/P085 存在同一文本被 list 与 listitem 重复登记的情况，属结构登记差异而非正文重复。",
    "P012“我已经把它涂黑给你们看了”疑指原文的加粗或标记格式，纯文本中不可见，格式信息待核。",
    "正文自注“（未完，待续）”，训练科目未列完（P090）。",
    "作者称该能力是评价子女学术进步时“唯一真正需要关心指标”（P019），该绝对化表述的依据未给出。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "人需要拥有的最重要的核心能力，就是无歧义、完备、简洁的表达能力。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "无歧义，是指极大的压缩所有人把A理解为B的可能性，即无错。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "完备性，是指待指各项之中没有被遗漏的必要的要素（也包括语句中必要的语素），即无漏。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "简洁，是指在达到同样的表达效果的前提下，占用人最少的理解资源，即无费。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "直接关系到ta将来能达到的高度。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "因为所谓的学习，就是在自己的意识里构建对世界的无错、无漏的表达。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "学习的成果，在本质意义上只是【你的判断力支撑之下】的一组你看不出如何有错、如何有漏的关于世界的表达。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "你的判断力决定了你的水准的极限。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "因为这种表达若不是尽量简洁的，你有限的运存就很难在一次运算中容纳足够的命题。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "于是会直接的锁定你对世界的表达能力的无错、无漏的水准上限。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "你只能将自己的能力提高到自己觉察不出错和漏的程度。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "从纯粹技术性的能力上说，这是一切其它能力的底层，是核心中的核心。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "这项能力，就是七十二绝技背后的那个小无相功", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "它在事实上就是学习能力、理解能力、探索能力、创造力的实质。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "那些不同名字的所谓重要能力，只是这项能力在不同的场景下、不同的上下文中的别称。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "这就是精英与非精英的真正分界。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P024", "quote": "精英不是按照人所处的社会地位来分的，而是本质的按照这个能力来分的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "精英完全有可能在社会决策链的中下层。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "这个能力强的人，必非池中之物。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P035", "quote": "应观察到T值有效下降和绘制误差逐次缩小。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P039", "quote": "默写世界各地的行政区划轮廓图——例如中国各省、市地图。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P051", "quote": "要求编码系统规则尽可能简短", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P053", "quote": "要求每一种零件的命名都是唯一的，且其他人能根据你的命名准确的将该零件识别出来。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P055", "quote": "有足够的望文生义性、高度简洁性和彼此之间的明显区分性", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P088", "quote": "任何一个文件都可以基于这个分类体系准确的预测其所在的位置。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P090", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E27", "paragraph_id": "P002", "quote": "这里有练习总集锦。做了练习可以申请投稿到这个专栏。我有时间会做示范和点评。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言表达与思维训练", "学习与认知方法", "教育与能力培养"],
   "issue_candidates": ["最核心能力的界定（无歧义/完备/简洁）", "表达能力与学习能力、判断力的关系", "精英的判定标准", "训练科目与练习设计"],
   "text_function_candidates": ["答疑", "主张与论证", "训练手册/操作清单"],
   "object_candidates": ["年轻人", "子女", "精英与非精英", "专栏投稿者"],
   "working_keywords": ["无歧义", "完备性", "简洁", "无错", "无漏", "无费", "判断力", "运存", "小无相功", "编码系统", "UML", "编目"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 10 个图片节点（IMG001-IMG010），图片内容未经核验，需图像核验；已读部分为正文文本（90 段全部读完）。故 status=needs_reread、image_checked=False。另登记：lexical 未覆盖片段 2 处（P001、P037，疑为标题/链接文字混入正文）、P002 疑为栏目导引或推广文字混入正文、list 与 listitem 存在同文本重复登记、正文自注“（未完，待续）”。无 provenance/superseded。"
 },
 "a4ba5682": {
  "analysis": {
   "question_context": "提问者问碰到成事不足败事有余的人怎么处理好（Q001）。作者给出“看出来就远离/跳船/不结交”的直接建议，指出以项目成败鉴定的传统办法无效，提出以“只破不立”识别这类人，并推演这种表现在组织中被掌权者标记后的后果，末段给出网上发泄的自保忠告。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"], "summary": "直接建议：看出来就赶紧有多远躲多远；团队里有这种人且其不在被开除轨道上就早点考虑跳船；熟人圈有就尽量躲远；不是熟人就尽量不要结交。理由是不这么做是对自己不负责、时间极其宝贵；唯一合乎逻辑的打交道理由是打算拯救ta而非合作。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015"], "summary": "反驳传统鉴定法：以“参与的项目是否屡屡失败”来鉴定极其无效——失败原因太多（被拖累、运气、难度），成功也不证明不是败事有余（可能早被识别“供起来”、危害被管理得较好），有人还靠白混来的履历爬到显赫唬人的位置；且代价奇高，如要尝了才知道鸡蛋坏。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "给出识别信号：看这人是不是从不建立、只是拆毁；对什么理论都不满意（尤其只是感情上不爽）、对什么方案都不满却不加预算、问理论/产品/方案都没有——即“只有破，没有立”，是成事不足败事有余的鲜明信号。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P025", "P026", "P027"], "summary": "理由：因为ta只练过败事，没有练过成事；练啥啥行是最朴素的道理。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P028", "P029"], "summary": "让步与限定：可以指出不足，但绝对不能在自己没有其它建立的前提下表示不满。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "后果推演：掌权者对此表现极其敏感；网上蒙脸喷后果不大，但在公司会上几次就会被做上“败事有余”的无形记号，被认定为“尚有剩余价值、可以做点简单杂事的边角余料”；领袖已无声无息判了组织前途的死刑；善良正派者冒险告知让你离开，次之者找借口开除，最心狠者继续用你却让你多年升不上去（当无脑杂事熟练工、吃定你无能怯懦），月饼聚餐不忘你甚至“特亲切”，但决策与独当一面的事不会给你，因为谁都不想为你陪葬；连站ta队的人也会被认定为不知好歹、绝不可作重大授权。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P042", "P043", "P044"], "summary": "回应不服者：预料知乎上很多人不服并以引号引出其反驳；回应是反问“不然你们以为资本家残酷是指什么地方残酷”，并主张资本家最残酷处不是加班压榨等表象，而是毫不留情、“宁可错杀一千、也不放过一个”、毫无顾忌地从工具性上判断人的习性。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049"], "summary": "引出加引号的第一人称自辩（我可怜你，谁可怜我？／我放过你，谁放过我？／我养你，谁养我？／我开的不是慈善机构），并以“ta们相信市场在用同样的残酷手段论断ta们”解释该逻辑。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P050", "P051", "P052", "P053"], "summary": "题外忠告：若舍弃不了在网上喷人发泄这种“减压方式”，请确保真实生活里绝对没人知道你的账号（基本自保）；但最好是自我反省、不要在网上养成这种习惯，因为若你的老板没本事看出这种掩饰，ta自己也没啥前途；不要抱有任何幻想。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "答案很直白：看出来了就赶紧有多远躲多远；团队里有这种人且其不在被开除轨道上，就早点考虑跳船；熟人圈有就尽量躲远；不是熟人就尽量不要结交。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这听起来残酷无情，但不这么做是对你自己不负责；时间极其宝贵，不要浪费。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "唯一合乎逻辑的觉得应该和这种人打交道的理由，是你打算拯救ta，而不是要和ta合作。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "以“参与的项目是不是屡屡失败”来鉴定是极其无效的办法，因为项目失败的原因太多——被别的人拖累、运气不好、本身难度太高。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使很成功也并不能说明这人就不是败事有余——那可能是ta早被别人识别出来“供起来”，只是危害被管理得比较好；有的人甚至因这种白混来的履历爬到很显赫、很唬人的位置。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这种极其不可靠的鉴定方法还代价奇高——需要尝尝才能鉴定一个鸡蛋是不是坏的，近乎没有意义。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "识别方法是看这人是不是从不建立，只是拆毁。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对什么理论都不满意（尤其只是感情上不爽）、对什么方案都不满却不加预算、问理论/产品/方案都没有，即“只有破，没有立”，这就是成事不足、败事有余的鲜明信号。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原因是ta只练过败事、没有练过成事；“练啥，啥行”是世界上最朴素的道理。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "你可以指出不足，但作者真心实意告诫：绝对不能在自己没有其它建立的前提下表示不满。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "真正握着能影响你命运权力的人对这种表现非常敏感；在网上蒙脸喷后果不大，但若在网上养成习惯并在公司会上来这么几下，只需极少几次就会被做上“败事有余”的无形记号，被认定为“尚有剩余价值、可以做点简单杂事的边角余料”。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "领袖实际上已经无声无息地判了你组织前途的死刑；比较善良正派的老板会冒险告知让你离开，比较不善良者会找借口（岗位调整、业务转向）开除你，最心狠手辣的则不动声色继续用你而让你三年五年十年都升不上去。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没人会把需要决策、需要独当一面的事情给你做，因为谁都不想为你陪葬——因为这样的人成事不足、败事有余。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种人的危害甚至残酷到这种程度——连在公司里站ta队的人，都会被默默认定为不知好歹、绝不可作重大授权。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "资本家最残酷的地方不是加班、压榨劳动力这些表象，而是毫不留情的、“宁可错杀一千、也不放过一个”的、毫无顾忌地从工具性上判断人的残酷习性。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "文中以加引号的第一人称语段呈现资本家的自辩逻辑（“我可怜你，谁可怜我？”“我放过你，谁放过我？”“我养你，谁养我？”“我开的不是慈善机构。”）；作者并说明这是因为ta们相信市场在用同样残酷的手段论断ta们。引语的说话者在正文未点名，仅可由上文的“ta们”（资本家）推知。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果你实在舍弃不了在网上喷人发泄这种“减压方式”，那么请确保真实生活里绝对没人知道你的账号，这好歹算是一道基本的自保手段；但最好是自我反省，也不要在网上养成这种习惯。", "evidence": ["E25", "E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "要是你的老板没这个本事看出这种掩饰，ta自己也没啥前途；不要对此抱有任何幻想。", "evidence": ["E27"]}
   ],
   "argument_steps": [
    "先给直白建议并分场景落实：跳船、躲远、不结交（P001-P004）。",
    "为建议辩护：不这么做是对自己不负责，时间宝贵；唯一正当的接触理由是拯救而非合作（P005-P008）。",
    "转入识别问题：以项目成败鉴定是否可靠（P009-P010）。",
    "反驳传统鉴定法：失败原因多元、成功不证明、白混履历可爬高、鉴定代价奇高（P011-P015）。",
    "给出替代信号：从不建立只拆毁，对理论/方案/产品均无而只会不满，即“只有破，没有立”（P016-P024）。",
    "给出理由：只练过败事、没练过成事（P025-P027）。",
    "以假想的质疑作让步，并给出限定：可以指出不足，但无自身建立时不可表示不满（P028-P029）。",
    "推演组织后果：被标记、被边缘化、被继续使用但不授权，殃及站队者（P030-P041）。",
    "回应不服者，转入对资本家工具性判断的论断（P042-P044）。",
    "以加引号的资本家自辩语段与其市场处境解释该逻辑（P045-P049）。",
    "给出题外忠告：网上发泄的自保与自我反省（P050-P053）。"
   ],
   "concept_usage": [
    {"term": "成事不足、败事有余", "meaning": "本文的识别标签，作者给出判据“只有破，没有立”（P024）；并被描述为掌权者给人的无形记号（P032）。", "evidence": "P024", "ambiguity": "作者未给程度门槛，只说“鲜明信号”。"},
    {"term": "只有破，没有立", "meaning": "从不建立、只是拆毁：对理论、方案均不满意而无自己的理论、产品、方案（P017,P021,P022,P023）。", "evidence": "P024", "ambiguity": "“立”的规模标准未说明。"},
    {"term": "供起来", "meaning": "被人早早识别后安置于危害可控的位置（P013）。", "evidence": "P013", "ambiguity": "无。"},
    {"term": "剩余价值 / 边角余料", "meaning": "掌权者对被标记者的工具性定位（P032）。", "evidence": "P032", "ambiguity": "无。"},
    {"term": "从工具性上判断人", "meaning": "作者界定的资本家最残酷的习性（P044）。", "evidence": "P044", "ambiguity": "无。"},
    {"term": "负资产 / 陪葬", "meaning": "描述被淘汰者处境与后果的用词（P036,P040）。", "evidence": "P040", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "成事不足败事有余的人：提问所问对象与作者建议远离的对象（Q001,P001-P004）。",
    "以项目是否屡屡失败作鉴定的传统办法：被作者反驳的做法（P010-P015）。",
    "“需要尝尝才能鉴定一个鸡蛋是不是坏的”：类比（P015）。",
    "“天上的太阳也有人嫌太热”：类比，用来说明不满意是廉价立场（P019）。",
    "知乎上不服的读者：作者假想的反驳者，其话以引号引出（P042），属被回应对象而非实际引用。",
    "老板/领袖/资本家：作者分析的行为主体（P034,P036,P037,P044,P045），其中“ta们”指资本家。",
    "引号内的第一人称自辩语段（P046-P049）：作者引出的资本家逻辑，说话者未点名。",
    "中秋月饼、年底聚餐、“特亲切”、驴子：比喻与修辞材料（P038）。"
   ],
   "conditions": [
    "建议按场景分别限定：团队内、熟人圈、非熟人（P002,P003,P004）。",
    "被标记的后果以“你如果在网上养成了习惯，在公司会上来这么几下”为条件，且只需极少几次（P032）。",
    "网上蒙脸喷与在公司会上的表现被明确区分，前者后果不大（P031,P032）。",
    "最心狠老板的做法以“吃定你无能且怯懦、根本走投无路”为条件（P037）。",
    "忠告以“如果你实在舍弃不了在网上喷人发泄这种‘减压方式’”为条件（P050）。",
    "对资本家行为的解释以“ta们相信市场在用同样的残酷手段论断ta们”为前提（P045）。"
   ],
   "rhetoric_and_tone": "断言式、口语化直白的建议口吻（“有多远躲多远”“谁脑子有水”）；大量第二人称“你/你们”的警告与训诫；频繁使用反问（“你怎么知道一个人是成事不足败事有余的？”“不然你们以为资本家残酷是指什么地方残酷？”）；以引号引出假想反驳并直接回应；用“边角余料”“驴子”“陪葬”“断肠路”等贬抑比喻描述后果；结尾是不容幻想的告诫语气。",
   "unresolved_questions": [
    "P046-P049 引号内第一人称自辩的说话者未在正文点名，仅可由 P045 的“ta们”（资本家）推知。",
    "“练啥，啥行”与“只练过败事”之间的关系未给出经验依据（P026,P027）。",
    "掌权者“对这种表现有多么敏感”的程度与依据未说明（P030）。",
    "资本家“宁可错杀一千、也不放过一个”的习性判断无具体案例或数据支持（P044），属作者断言，待外部核查。",
    "提问者所说的“成事不足败事有余的人”的具体情形未在正文出现（Q001）。",
    "P042 引号内的不服之辞为作者假想的读者反应，非实际引用来源。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "其实答案本身是很直白的——看出来了就赶紧有多远躲多远。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "那么你就早点考虑跳船。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "如果这人还不是你的熟人，那么尽量不要结交。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "但是你不这么做，是对你自己不负责。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "唯一合乎逻辑的觉得应该和这种人打交道的理由，是你打算拯救ta，而不是要去和ta合作。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P011", "quote": "其实这是一个极其无效的办法。", "relation": "contradicts"},
    {"key": "E7", "paragraph_id": "P012", "quote": "因为项目失败的原因太多，可能是因为被别的人拖累，可能是运气不好，可能是本身难度太高。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "那可能是ta早早就被别人识别出来“供起来”了，只是ta的危害被管理得比较好而已。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "需要尝尝才能鉴定一个鸡蛋是不是坏的，这种鉴定方法近乎没有意义。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "你要看这人是不是从不建立，只是拆毁。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P020", "quote": "对什么方案都不满——预算ta可不会加。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P024", "quote": "也就是“只有破，没有立”，这就是成事不足、败事有余的鲜明信号。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "因为ta只练过败事，没有练过成事啊。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P029", "quote": "绝对不能在自己没有其它建立的前提下表示不满。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P030", "quote": "你们难以想象真正握着能影响你命运的权力的人对这种表现有多么敏感。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P032", "quote": "你头上就会被做上“败事有余”的无形记号", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P033", "quote": "领袖实际上已经无声无息的判了你组织前途的死刑。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P037", "quote": "只是你三年五年十年都莫名其妙的升不上去。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P040", "quote": "因为谁都不想为你陪葬", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P041", "quote": "连在公司里站ta队的人，都会被默默的认定为不知好歹、绝不可作重大授权。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P044", "quote": "而是毫不留情的、“宁可错杀一千、也不放过一个”的、毫无顾忌的从工具性上判断人的残酷习性。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P045", "quote": "因为ta们相信市场在用同样的残酷手段论断ta们，连一丝一毫的温情也不会给ta们留。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P046", "quote": "“我可怜你，谁可怜我？", "relation": "context"},
    {"key": "E24", "paragraph_id": "P049", "quote": "我开的不是慈善机构。”", "relation": "context"},
    {"key": "E25", "paragraph_id": "P050", "quote": "那么请确保你真实生活里绝对没人知道你的账号。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P051", "quote": "这好歹算是一道基本的自保手段。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P052", "quote": "要是你的老板没这个本事看出这种掩饰，ta自己也没啥前途。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场/组织行为", "识人与合作", "网络言论的现实后果"],
   "issue_candidates": ["如何识别成事不足败事有余者", "项目成败能否作为判据", "“只破不立”信号", "组织中的工具性评价"],
   "text_function_candidates": ["答疑", "经验总结", "训诫/忠告", "论辩"],
   "object_candidates": ["提问者", "成事不足败事有余的人", "老板/领袖/资本家", "知乎读者"],
   "working_keywords": ["成事不足败事有余", "只有破没有立", "供起来", "无形记号", "边角余料", "陪葬", "工具性判断"]
  },
  "notes": "提问（Q001）属提问者。无图片节点；provenance/superseded 均为 null。P046-P049 为加引号的第一人称引语，按 quoted_or_cited+cited_source 登记，未归为作者主张；P042 引号内为作者假想的读者反驳，按被回应观点处理。"
 },
 "4638a3d0": {
  "analysis": {
   "question_context": "提问者问“瘾，和‘习惯’是一样的吗？”（Q001）。作者先承认二者有深刻的同质性（都是强迫性、都有戒断反应），指出并否定用“程度大法”作区分的通行做法，提出本质区别在扩张性与维持性，并据此给出把维持性事务建成习惯、把进取性价值追求建成瘾的策略。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "肯定问题并给前提：习惯和瘾有显而易见的深刻的同质性，都是强迫性的、都有戒断反应。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "呈现并归纳通行区分法：一般人用“程度大法”，以戒断反应程度或养成门槛高低划分（P005、P006 为引号内表述）；作者质疑“程度”在哪天知道，并指出这种办法实质上已等于说“其实瘾就是一种习惯，习惯就是一种瘾”。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011"], "summary": "否定上述等同并给出本质区别：但这是不对的；作为同样有戒断反应、同样有养成条件的强迫性行为模式，其本质区别在于瘾有扩张性、习惯只有维持性；瘾永远饥渴，习惯是满足的。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014"], "summary": "回答动机与总策略：因为存在关键的顶层策略问题——人要理性地、策略地建构自己的习惯和瘾；不是要去除瘾，而是通过深思熟虑把它安排在合适的位置上。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "策略表述：把一切人生中维持性的事务构建成习惯；把人生中进取性的价值追求构建成瘾。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "习惯的做法：吃喝拉撒、清洁维持、每日新闻阅读等养成固定习惯，让其透明地、自动地完成，几乎不占据注意力，像“我刷牙了吗”那样，只有未完成才引起注意。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023"], "summary": "瘾的做法：价值追求应如同成瘾一般，牢牢占据极大的主观注意力，见缝插针的时间与闲余精力都被抓来创造和享受这个过程，连结果都没那么重要；念念不忘。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026"], "summary": "结论与条件：瘾不是问题，真正的问题是对什么上瘾、这个瘾的附加效应是什么、这些效应是否伤人；如果附加效应是有利于人的，那么你就注定成功，而且必受祝福。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "习惯和瘾有显而易见的深刻的同质性：它们都是强迫性的，都有戒断反应。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者转述“一般人”区分习惯与瘾时使用的“程度大法”：如“戒断反应低于一定程度的就是习惯，高于一定程度的就是瘾”“养成门槛高到一定程度的就是习惯，养成门槛低到一定程度的就是瘾”。说话者仅称“一般人”，未指名来源。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“程度”在哪天知道；这种“程度大法”实质上已经等于把“其实瘾就是一种习惯，习惯就是一种瘾”这句话说出来了。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "把习惯与瘾视为同一种东西（只是程度不同）的说法，作者判定为不对。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "习惯和瘾作为同样有戒断反应、同样有养成条件的强迫性行为模式，它们的本质区别在于瘾有扩张性，而习惯只有维持性。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "瘾是永远饥渴的，而习惯是满足的。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里存在一个关键的顶层策略问题——人要理性的、策略的建构自己的习惯和瘾。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不是要去除瘾，而是要通过深思熟虑，将它安排在一个合适的位置上。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "策略表述：把一切人生中维持性的事务构建成习惯；把人生中进取性的价值追求构建成瘾。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "吃喝拉撒、清洁维持、每日新闻阅读等都应养成固定的习惯，让它透明地、自动地完成，几乎不占据注意力，只有它们的未完成才会引起注意。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "价值追求应该如同成瘾一般，牢牢占据极大的主观注意力，见缝插针的时间与闲余精力都被毫不留情地抓来创造和享受这个过程，甚至连结果都没那么重要。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "瘾不是问题，真正的问题是你对什么上瘾、这个瘾的附加效应是什么、这些效应是否伤人。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "如果这些附加效应是有利于人的，那么你就注定成功，而且必受祝福。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "先肯定问题并给出共同点：二者都是强迫性、都有戒断反应（P001-P003）。",
    "呈现通行区分法：以程度高低划分的“程度大法”（P004-P006）。",
    "质疑该法的可操作性：“程度”在哪，天知道（P007）。",
    "指出该法实质上等同“瘾就是一种习惯，习惯就是一种瘾”（P008）。",
    "明确否定该等同：但这是不对的（P009）。",
    "给出本质区别：扩张性 vs 维持性；饥渴 vs 满足（P010-P011）。",
    "交代回答动机：顶层策略问题——理性、策略地建构习惯和瘾（P012-P013）。",
    "给出总取向：不去除瘾，而将其安排在合适位置（P014）。",
    "给出策略二分表述（P015-P016）。",
    "分别说明习惯侧做法（透明自动、不占注意力）与瘾侧做法（占据注意力、念念不忘）（P017-P023）。",
    "结论：问题不在瘾而在对什么上瘾及附加效应，附加效应利人则注定成功（P024-P026）。"
   ],
   "concept_usage": [
    {"term": "习惯", "meaning": "有戒断反应、有养成条件的强迫性行为模式，特征为维持性、满足（P003,P010,P011）；被建议用于承载维持性事务（P016）。", "evidence": "P010", "ambiguity": "与日常语义的差异未说明。"},
    {"term": "瘾", "meaning": "同类强迫性行为模式，但具扩张性、永远饥渴（P010,P011）；作者主张不去除而安置（P014）。", "evidence": "P011", "ambiguity": "未说明是否包含病理性成瘾。"},
    {"term": "戒断反应", "meaning": "二者共有的强迫性标志（P003），也是通行区分法的划分依据（P005）。", "evidence": "P003", "ambiguity": "无。"},
    {"term": "程度大法", "meaning": "作者对以程度高低区分习惯与瘾的通俗做法的命名，属被批评对象（P004,P008）。", "evidence": "P004", "ambiguity": "无。"},
    {"term": "扩张性 / 维持性", "meaning": "作者提出的本质区别（P010）。", "evidence": "P010", "ambiguity": "未给出判定标准。"},
    {"term": "维持性的事务 / 进取性的价值追求", "meaning": "策略的二分对象（P016）。", "evidence": "P016", "ambiguity": "具体归属由谁判定未说明。"},
    {"term": "附加效应", "meaning": "瘾带来的后果；作者以此替代“是否有瘾”作为真正的问题（P024）。", "evidence": "P024", "ambiguity": "判断标准与判断者未说明。"}
   ],
   "examples_and_targets": [
    "“一般人”的“程度大法”：被反驳的通行说法（P004），其表述以引号引出（P005,P006）。",
    "吃喝拉撒、清洁维持、每日新闻阅读：作者举的习惯对象（P017）。",
    "“我刷牙了吗”：日常经验的类比（P019）。",
    "瘾的附加效应是否伤人：作者界定的真正问题（P024）。",
    "“～～”波浪线：原文自带的符号，用于摹写通俗语气（P005,P006）。"
   ],
   "conditions": [
    "同质性的限定为“同样有戒断反应、同样有养成条件的强迫性行为模式”（P010）。",
    "策略对象限定为“维持性的事务”与“进取性的价值追求”两类（P016）。",
    "结论“注定成功、必受祝福”以“附加效应是有利于人的”为条件（P025）。",
    "“合适的位置”如何判定，正文未说明（P014）。"
   ],
   "rhetoric_and_tone": "以“这又是一个极好的问题”先肯定提问者；用引号加波浪线摹写并调侃通俗说法（“程度大法”“～～”）；以短句和否定句立论（“但这是不对的”）；以日常事例（刷牙）作类比；结尾用“念念不忘”“必受祝福”等短句收束，带格言与祝福语气。",
   "unresolved_questions": [
    "“一般人”的“程度大法”具体出处未给出，属作者概括的通行说法（P004-P006）。",
    "“瘾有扩张性、习惯只有维持性”的判定标准与依据未展开（P010,P011）。",
    "“合适的位置”如何界定、由谁判定未说明（P014）。",
    "“附加效应是有利于人的”由谁判断、判断失误如何处理未说明（P024,P025）。",
    "作者未讨论成瘾的医学或临床层面，未说明本文的“瘾”是否包含病理性成瘾（P010,P011）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "习惯和瘾有显而易见的深刻的同质性。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "它们都是强迫性的——也就是说它们都有戒断反应。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "“戒断反应低于一定程度的就是习惯～～高于一定程度的就是瘾～～”", "relation": "context"},
    {"key": "E4", "paragraph_id": "P006", "quote": "“养成门槛高到一定程度的就是习惯～～养成门槛低到一定程度的就是瘾～～”", "relation": "context"},
    {"key": "E5", "paragraph_id": "P007", "quote": "“程度”在哪？天知道。", "relation": "contradicts"},
    {"key": "E6", "paragraph_id": "P008", "quote": "这种“程度大法”实质上已经等于把这话说出来了——“其实瘾就是一种习惯，习惯就是一种瘾”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "但这是不对的。", "relation": "contradicts"},
    {"key": "E8", "paragraph_id": "P010", "quote": "它们的本质区别，在于瘾有扩张性，而习惯只有维持性。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "瘾是永远饥渴的，而习惯是满足的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "人要理性的、策略的建构自己的习惯和瘾。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "不是要去除瘾，而是要通过深思熟虑，将它安排在一个合适的位置上。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "把一切人生中维持性的事务构建成习惯；把人生中进取性的价值追求构建成瘾。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "以至于它们的完成几乎不会占据你的注意力。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "就像你早上出门时有时会疑惑“我刷牙了吗”这样。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "只有它们的未完成才会引起你的注意。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P022", "quote": "甚至连结果都没那么重要了。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "念念不忘。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "瘾不是问题，真正的问题是你对什么上瘾，这个瘾的附加效应是什么，这些效应是否伤人。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P025", "quote": "如果这些附加效应是有利于人的，那么你就注定成功，", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["行为习惯与自我管理", "心理与动机", "人生策略"],
   "issue_candidates": ["习惯与瘾的区别", "“程度大法”作为区分标准的失效", "习惯与瘾的建构策略"],
   "text_function_candidates": ["答疑", "概念辨析", "策略建议"],
   "object_candidates": ["提问者", "“一般人”（通行说法的持有者）"],
   "working_keywords": ["习惯", "瘾", "强迫性", "戒断反应", "程度大法", "扩张性", "维持性", "维持性事务", "进取性价值追求", "附加效应"]
  },
  "notes": "提问（Q001）属提问者。无图片节点；provenance/superseded 均为 null。P005、P006 为引号内的“一般人”说法，按 quoted_or_cited+unknown 登记，未归为作者主张；P008 是作者对该说法实质的归纳，P009 起为作者的反驳。"
 }
}


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
