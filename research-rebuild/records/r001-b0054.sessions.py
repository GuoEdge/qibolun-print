# -*- coding: utf-8 -*-
"""批次 r001-b0054 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0054.sessions.py            # 写 out/r001-b0054.out.jsonl
  python3 records/r001-b0054.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0054"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0054.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "58e6a94d": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）自述高一，问“学习重要还是朋友重要”。作者未讨论“学习”一侧，只以“如果真称得上是朋友”为条件回答“朋友重要”，随后把话题转向“你有没有朋友、有没有资格拥有朋友”。二选一的框架属于提问者，作者只回应其中一端并重新定义了问题焦点。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以“真称得上是朋友”为条件，直接给出“朋友重要”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "以飞机多一个引擎作类比，并用个人观察说明真朋友数量与事业成就的对应。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "界定真朋友不是裙带、酒肉、利益之交，并称这种朋友值得任何牺牲。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "连续反问“你有吗”“你受得起吗”，把问题转向资格。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "主张没有英雄气就没有交友的能力与资格；理由是朋友必为英雄，而受得起需自身英勇。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "限定“受得起”不是偿还或经济补偿，而是不辜负、不让对方牺牲白费。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "划出分界线：达到这条线才成其为朋友，低于此线只是cosplay想象中的朋友。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019"], "summary": "指出校园安稳与家长保底使高中朋友少受考验，并提出“自己为自己买单”是谈感情的双向基础。", "role": "context"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021"], "summary": "叙述毕业后朋友自然消失、三四十岁记不起名字。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "要求重新考虑有没有朋友与资格、丢掉幻想，并把告诫扩展到女性读者，以NEVER SETTLE收束。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果真称得上是朋友，那么朋友比学习重要。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "多一个真朋友如同飞机多一个引擎；能有效担当朋友伦理的人不会是loser。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "据作者观察，有一个真朋友的人不会过得很失败，有两个即可成事，超过两个则独角兽企业也不是不可企及。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本文所指的朋友不是裙带、酒肉、利益之交，而是能为义理死战的朋友。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者反问读者：你有这样的朋友吗？就算真有，你自己受得起吗？", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人内里没有真正的英雄气，就没能力做别人的朋友，也没资格拥有朋友；因为每个朋友都必然是英雄。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为朋友之义去面对困难、损失和牺牲是不折不扣的英勇行为，而这种英勇必须以自身的英勇才能受得起。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "受得起不是偿还，也不是足量经济补偿，而是不辜负、不让对方的牺牲白费。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "低于这条线的关系只是认真cosplay想象中的朋友，享受无需付出代价的情绪快感。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "校园相对安稳、学生有家长保底，使高中时期的朋友很少真正面对朋友之义的考验，即使遇到也往往由家长出头负担。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "情即是义，无义则无情；自己为自己的一切买单是与人谈任何感情的双向基础。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "对以一张脸或一张卡为凭的人：没资格做你朋友的人，没有能力和你谈爱。", "evidence": ["E17"]}
   ],
   "argument_steps": [
    "以条件句给出结论：若称得上朋友，则朋友重要（P001）。",
    "用飞机引擎类比真朋友的增益（P002）。",
    "以个人观察列出真朋友数量与事业成就的对应（P003）。",
    "界定真朋友并称其值得任何牺牲（P004-P005）。",
    "用反问把话题从“哪个重要”转到“你有没有、受不受得起”（P006-P007）。",
    "提出英雄气是交友能力与资格的前提，理由是朋友必为英雄（P008-P009）。",
    "说明朋友之义中的牺牲即英勇，受得起需自身英勇（P010-P011）。",
    "限定受得起不等于偿还或经济补偿，而是不辜负（P012-P014）。",
    "划界：达线才是朋友，低于此线是cosplay（P015-P016）。",
    "补充处境条件：校园安稳与家长保底使高中友谊少受考验，继而提出“自己买单”为基础（P017-P019）。",
    "以毕业后朋友消失的观察收束（P020-P021）。",
    "提出行动要求：重新评估朋友与资格、丢掉幻想，并转向女性读者（P022-P028）。"
   ],
   "concept_usage": [
    {"term": "朋友／真朋友", "meaning": "以能否为义理面对困难、损失和牺牲来界定，明确排除裙带、酒肉、利益之交（P004）。", "evidence": "P004", "ambiguity": "未给出可操作的判定标准；“真称得上是朋友”本身未定义。"},
    {"term": "朋友伦理", "meaning": "出现在“能有效担当朋友伦理的人”一语中，指承担朋友之义的能力（P002）。", "evidence": "P002", "ambiguity": "术语未定义，仅一笔带过。"},
    {"term": "英雄气／英雄", "meaning": "能为朋友之义（或不管什么义理）面对困难、损失、牺牲的品质；每个朋友都必然是英雄（P008-P010）。", "evidence": "P008", "ambiguity": "未说明如何判定谁是英雄；与身份地位无关（P010）。"},
    {"term": "受得起", "meaning": "不是偿还、不是经济补偿，而是不辜负、不让对方的牺牲白费（P011-P012、P014）。", "evidence": "P012", "ambiguity": "与“还”刻意区分，但“不辜负”的具体行为未说明。"},
    {"term": "情／义", "meaning": "“情义情义，情即是义”，无义则无情；并以“义是别人买单”质疑那种情的成色（P018）。", "evidence": "P018", "ambiguity": "以买单一事衡量情之成色，属修辞性推论。"},
    {"term": "买单", "meaning": "“自己为自己的一切买单”作为与人谈任何感情的双向基础（P019）。", "evidence": "P019", "ambiguity": "未说明是否仅指经济层面。"}
   ],
   "examples_and_targets": [
    "飞机多一个引擎（作者的类比，P002）",
    "三人同心、其利断金（成语式修辞，P003）",
    "美团、滴滴这类独角兽企业（成就量级的例证，P003；非外部已证实事实）",
    "富贵不能淫、贫贱不能移、威武不能屈（孟子语式的引用，P004）",
    "赵客缦胡缨，吴钩霜雪明（李白《侠客行》引用，P004）",
    "两肋插刀、割头换颈、吞炭漆面、托妻献子（典故堆叠，P005）",
    "目盲、肢残者（作为“我还没有见过失败”的边界例证，P003）",
    "cosplay（比喻，P016）",
    "女孩子们以及凭一张脸或一张卡谈爱者（告诫对象／隐含反驳对象，P025-P027）"
   ],
   "conditions": [
    "前提条件：“如果真称得上是朋友”（P001）",
    "观察限定：“我还没有见过”，属个人经验范围（P003）",
    "处境条件：校园的相对安稳环境与学生有家长保底（P017）",
    "频度限定：“很少遇到”“往往其实是家长出头负担了”“就算不幸遇到了”（P017）",
    "受得起的条件：自身有英勇／是个英雄（P011、P013）",
    "时间条件：毕业后、等你三四十岁（P020-P021）"
   ],
   "rhetoric_and_tone": "第二人称训诫式劝导，密集反问（P006、P007、P013、P026、P027）；夸张类比与典故堆叠；英语词点缀（loser、die in vain、cosplay、NEVER SETTLE!）；多用感叹号与祈使句（“然后丢掉幻想！”）；结尾由“小男生”扩展到女性读者，语气从论证转为告诫。",
   "unresolved_questions": [
    "正文完全未讨论“学习”一侧的价值或取舍，问题中的比较只被“朋友重要”一端回应；标题“朋友与学习”与正文重心不完全对应。",
    "“能有效担当朋友伦理的人”未定义。",
    "“英雄气”“英雄”的判定标准未给出，读者无法据此自查。",
    "P003 的真朋友数量与事业成就对应为作者个人观察，无数据或来源，需外部核查；其中对美团、滴滴的表述是事实断言还是夸张修辞，未明示。",
    "“没资格拥有朋友”“没资格做你朋友之人”等断言的适用对象与范围未限定（未说明是否涵盖所有读者）。",
    "本文未说明“学习”与“朋友”在时间、精力上如何取舍，作者的答案是否要求以朋友为优先未明说。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "如果真称得上是朋友，那么当然是朋友重要。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "能有效担当朋友伦理的人，没有一个会是loser", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "有一个真朋友的人，我还没有见过过得很失败的", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "我说的不是那种裙带、酒肉、利益之交", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "问题是，你有吗？", "relation": "context"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你就算真有，你自己受得起吗？", "relation": "context"},
    {"key": "E7", "paragraph_id": "P008", "quote": "内里没有一股真正的英雄气，是没能力做别人的朋友的", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "因为每个朋友都必然是一个英雄。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "去面对困难、损失和牺牲，这都是不折不扣的英勇行为", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "必须以你自身的英勇才能受得起", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "是绝不让对方die in vain的受得起，是不辜负的受得起", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P014", "quote": "而是要你真正成就有价值的事，不使ta的牺牲白费", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P016", "quote": "只是认真的cosplay着想象中的朋友", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "校园的相对安稳环境，以及学生有家长保底的客观条件", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P018", "quote": "情义情义，情即是义。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "自己为自己的一切买单，这是你与人谈任何感情的基础", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "没资格做你朋友之人，有什么能力和你谈爱？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系伦理", "青少年成长"],
   "issue_candidates": ["朋友与学习的取舍", "真朋友的判定标准", "交友资格与“受得起”", "校园友谊未受考验", "感情中的自我承担"],
   "text_function_candidates": ["答疑", "训诫式劝导", "论辩"],
   "object_candidates": ["高一学生（提问者）", "女性读者", "美团", "滴滴"],
   "working_keywords": ["朋友伦理", "真朋友", "英雄气", "受得起", "die in vain", "不辜负", "情义", "买单", "cosplay", "NEVER SETTLE"]
  },
  "notes": "正文未讨论“学习”，只回应“朋友重要”一端并把重心移到交友资格；brief 在“有超过两个”处截断，属语料摘要字段本身的截断，仅作导航，未用于支持主张。P003 关于真朋友数量与事业成就的对应为作者个人观察，无来源，登记为待外部核查。无图片，结构与正文一致（lexical 段落节点数多于正文段落数，差额为空白段落节点）。"
 },
 "9138c22a": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）问“戴几百块的手表丢人吗”。作者不直接讨论价格与面子，而是先给出“世界上最好的表”的功能规格与价格上限，主张手表在功能上已经到头，再指出说“丢人”的人其实说的是珠宝，最后附评论区推荐与致谢。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以功能条件列举“世界上最好的表”的规格。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "给出价格区间并断言手表功能已到顶。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "超过这个顶级的不是表，而是带计时功能的首饰或仪器。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "重解“丢人”一说：对方想说的是珠宝，并以“理解、同情和怜悯”作反讽收束。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009"], "summary": "回应推荐请求，列出评论区推荐型号，并补充精工的传统表盘。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012"], "summary": "“评论区淘金”部分给出电波表校时App外链并致谢评论者。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上最好的表是自动电波对时、有夜光、钛合金加皮表带、西装表样式、光动能潜水表这类以实用功能为标准的表。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类表的价位一般一两千元，三五千元就算顶级。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "手表在功能上已经到头；再往上就不是表，而是带计时功能的首饰或仪器。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说“戴几百块的手表丢人”的人，其实想说的是“戴几百块的珠宝丢人”，是语文不太好。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对这类人应当理解、同情和怜悯。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "评论区推荐的具体型号：Casio Edifice、西铁城蓝天使、卡西欧海神、西铁城空中之鹰。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "另有说法提到精工；精工表盘较传统，适合不喜欢三眼四眼和一堆表冠的人（推荐主体未标明）。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "先定义“世界上最好的表”的实用功能清单与价位（P001-P002）。",
    "断言手表在功能上已到头（P003）。",
    "以此划界：再往上是首饰或仪器，不再是表（P004）。",
    "据此重解“戴几百块的手表丢人”的语义，把评价对象换成珠宝（P005）。",
    "以反讽式建议收束论点（P006）。",
    "回应推荐请求，列出评论区型号并补充精工（P007-P009）。",
    "附加评论区淘金的外链与致谢（P010-P012）。"
   ],
   "concept_usage": [
    {"term": "最好的表", "meaning": "以实用功能规格（免调整、夜间可用、耐汗耐海水、可配正装、免充电、防尘防水）而非品牌或价格来定义（P001）。", "evidence": "P001", "ambiguity": "“最好”被限定为功能维度，未讨论工艺、收藏或品牌价值。"},
    {"term": "表／首饰／仪器", "meaning": "以计时功能是否为本职来划界：顶级之上的是“带计时功能的首饰”或“带计时功能的仪器”（P003-P004）。", "evidence": "P004", "ambiguity": "未给出价格或品类的具体分界点。"},
    {"term": "丢人", "meaning": "作者把“戴几百块手表丢人”重解为“戴几百块珠宝丢人”，即评价对象被偷换（P005）。", "evidence": "P005", "ambiguity": "属对他人用意的重述，非作者自己的评价标准。"},
    {"term": "电波对时／光动能／钛合金", "meaning": "P001 中作为功能条件的术语，括号内给出其功能理由。", "evidence": "P001", "ambiguity": "未说明这些功能的实现原理或可靠性差异。"}
   ],
   "examples_and_targets": [
    "Casio Edifice、西铁城蓝天使、卡西欧海神、西铁城空中之鹰（评论区推荐型号，P008，作者明确标注来源）",
    "精工（推荐主体未标明，P009）",
    "“人家”——说戴几百块手表丢人者（被重解／调侃对象，P005-P006）",
    "电波表校时App（外链，P011）",
    "评论区用户 @Sybeky（致谢对象，P012）"
   ],
   "conditions": [
    "功能条件（括号内明列）：免调整、夜间可用、防手汗与海水腐蚀、可配正装、免充电、免上弦、防尘防水（P001）",
    "价格条件：一般一两千，三五千算顶级（P002）",
    "适用条件：不喜欢三眼四眼各种数据转盘一堆表冠的可以考虑精工（P009）",
    "未给出适用场景限定（如正装、运动、潜水场景的取舍未说明）"
   ],
   "rhetoric_and_tone": "冷幽默与反讽：把对方的话重解为“珠宝”后评“他语文不太好”，再以“要理解、同情和怜悯”作结；短句断言（“手表这就到头了”）；正文用括号密集夹注功能理由；结构上以分隔线分为正文、推荐、评论区淘金三段（lexical 含 horizontalrule 节点）。",
   "unresolved_questions": [
    "“人家”具体指谁（泛指的他人还是具体评论者）未标明；C004 是对他人用意的重述，作者认同该重解但未说明依据。",
    "P009 精工的推荐归属不明：它出现在“以上是评论区推荐”之后，是否也属评论区推荐或作者补充，正文未标明。",
    "推荐型号的价格、性能是否与“最好”的功能规格相符未经核验，登记为待外部核查。",
    "P011 外链（电波表校时App）内容未查看，正文仅有链接文字；该段在 lexical 中为 link 节点，正文与结构不完全一致。",
    "更新时间 2021-05-20 晚于发布时间 2020-06-19，正文可能经增补，但无版本差异说明。",
    "“戴几百块的手表丢人吗”这一提问者的问题未被直接回答“丢不丢人”，只被改写为语义误用问题。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "世界上最好的表就是自动电波对时的（免调整）、有夜光的（夜间可用）", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "一般一两千就买到了，三五千就算顶级了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "手表这就到头了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "再往上就不是表了，而是带计时功能的首饰，或者带计时功能的仪器。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "其实他想说的是“戴几百块的珠宝”丢人，他语文不太好。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "要理解、同情和怜悯。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "以上是评论区推荐。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "精工也有。——精工表盘传统一些", "relation": "context"},
    {"key": "E9", "paragraph_id": "P011", "quote": "电波表校时App上线了，帮你快速对时授时", "relation": "context"},
    {"key": "E10", "paragraph_id": "P012", "quote": "感谢评论区 @Sybeky", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["消费与生活方式", "腕表"],
   "issue_candidates": ["手表价格与体面", "功能上限与奢侈品的界限", "消费符号与语义误用"],
   "text_function_candidates": ["答疑", "评论", "调侃"],
   "object_candidates": ["卡西欧", "西铁城", "精工", "知乎评论区", "@Sybeky"],
   "working_keywords": ["电波对时", "光动能", "钛合金", "潜水表", "蓝天使", "海神", "空中之鹰", "Casio Edifice", "丢人", "首饰", "仪器"]
  },
  "notes": "本篇含外链节点（P011 电波表校时App）并在 lexical 中以 link 形式存在，正文只有链接文字，未查看其内容；P008 明确标注推荐来自评论区，已按 cited_source 归属；P009 归属不明，标 unknown。brief 与正文一致但截断于“而是”。更新时间晚于发布时间，未见版本说明。无图片。"
 },
 "1edec003": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）设问“如果人类的自杀率在50%以上，社会将如何发展”。作者不回答社会发展，而是判定提问方向反了，并把问题改写成“社会发展到什么程度，人类自杀率会达到50%”，其间给出一条条件性断言：人类全体获得无限寿命时几乎100%自杀。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接判定提问方向反了。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "在“全体获得无限寿命”的假设下，断言人类几乎100%自杀。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "据此把问题改写为“社会发展到什么程度，人类自杀率会达到50%”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "提问者把因果关系问反了：不是自杀率高导致某种社会，而是社会发展到某个程度才使自杀率达到50%。", "evidence": ["E1", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "当人类全体获得无限寿命时，人类几乎100%都是自杀的。", "evidence": ["E2"]}
   ],
   "argument_steps": [
    "先否定提问的前提方向（P001）。",
    "给出反向的极端条件命题：无限寿命条件下几乎人人自杀（P002）。",
    "由此把原问题改写为追问“社会发展到什么程度才会出现50%自杀率”（P003）。"
   ],
   "concept_usage": [
    {"term": "自杀率50%", "meaning": "提问者设定的数值；作者不否定该数值，只把它从“前提”改置为“待解释的结果”（P003）。", "evidence": "P003", "ambiguity": "未说明50%的统计口径、时间尺度与人群范围。"},
    {"term": "无限寿命", "meaning": "作为假设条件出现的状态，作者未定义其技术含义（P002）。", "evidence": "P002", "ambiguity": "是生物意义上的不死、还是医学延长寿命，本文未说明。"},
    {"term": "问反了", "meaning": "作者对提问方向的判定，指因果或提问次序颠倒（P001）。", "evidence": "P001", "ambiguity": "未展开说明为何是反的。"}
   ],
   "examples_and_targets": [
    "“人类全体”（假设对象，P002）",
    "无具体人物、机构、地区、时期或数据；无引用来源"
   ],
   "conditions": [
    "明确假设条件：“当人类全体获得无限寿命时”（P002）",
    "不确定限定：“几乎100%”，保留少数例外（P002）",
    "未给出社会制度、时间尺度、技术条件等其他前提"
   ],
   "rhetoric_and_tone": "极简三段，开门见山否定（“你问反了”）；断言式短句，不作论证；以改写问句收尾，语气直接、近乎判定式。",
   "unresolved_questions": [
    "“无限寿命时人类几乎100%自杀”的机制、依据与来源均未说明，属未论证的条件性断言，登记为待外部核查。",
    "“几乎100%”的例外者是谁、为何例外，未说明。",
    "提问者真正问的“社会将如何发展”未被回答，作者只改写了问题。",
    "本文未说明该判断是字面主张还是夸张／反讽。",
    "无图片，正文与 lexical 结构一致（3 段）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你问反了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "当人类全体获得无限寿命时，人类几乎100%都是自杀的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "正确的问法是“社会发展到什么程度，人类自杀率会达到50%”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会理论", "人口", "未来学"],
   "issue_candidates": ["自杀率与社会形态", "无限寿命的后果", "提问方向与因果次序"],
   "text_function_candidates": ["答疑", "反驳提问前提"],
   "object_candidates": ["人类"],
   "working_keywords": ["自杀率", "无限寿命", "50%", "问反了"]
  },
  "notes": "全文仅 67 字，为对提问前提的改写式回答，未给出论证与来源；C002 属条件性断言，登记为待外部核查，不作为已证实事实。brief 与正文内容一致。无图片。"
 },
 "c2b25366": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）问“中国在大国博弈中的水平如何”。作者先否定“大国博弈”这一提法（认为过于沙文主义、无视中小国家话语权），改用“地缘政治博弈”，随后自建“铁笼模式／拓荒模式”两模式框架与“到达能力”这一关键变量，用历史叙述推到“世界重新走向铁笼模式”，再以中国的长期铁笼经验解释中国走向上风。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "批评“大国博弈”提法并改用“地缘政治博弈”，声明中国有优势，先讲游戏规则。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "提出游戏有两个模式，先定义模式A铁笼模式。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "以铁笼与玩家的比喻描写铁笼模式：玩家不能离开、彼此不完全了解、场面微妙。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "铁笼模式最关键技能是“读空气”和“写空气”；微妙信号被捕捉研判，外人难解共识如何形成，东亚文化圈更易心领神会。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "定义模式B拓荒模式：从同一营地出发、四周未知荒野、各自出击，以荒野收益定老大并可能地位逆转。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P018"], "summary": "两模式的交替上演构成国际地缘政治博弈的基本机制。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "到达能力是关键要害；到达能力弱则形成纸牌屋式铁笼（举例各圈层），突破铁笼四壁则进入荒野模式，瓜分殆尽后回到更大的铁笼。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P024"], "summary": "限定：一般情况下旧铁笼崩溃释放的新荒野不大，荒野模式持续不久便回到铁笼模式。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "地理大发现是异数：四大洲版图开放给欧洲玩家，使世界主流模式锁定拓荒模式500年，是欧洲1500—2000年称霸的最主要原因。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P029", "P030"], "summary": "预测：除非太空殖民足够经济，世界正迅速重回铁笼模式，这一次的铁笼是地球本身。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P031", "P032", "P033", "P034"], "summary": "以中国三千年铁笼经验与五个朝代“金牌”对比美国“小学没毕业”，并比较法国、土耳其，得出中国渐渐走向上风。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“大国博弈”的讲法不好，过于沙文主义、基本无视中小国家话语权，作者更愿用“地缘政治博弈”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国在地缘政治博弈中有优势。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "地缘政治博弈有两种模式，两者的交替上演构成其基本机制。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "铁笼模式中最关键的技能是“读空气”和“写空气”。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "铁笼模式中坐姿、语气、敬语体、发言顺序等微妙信号会被捕捉、解读、研判和反应；不懂这些的人难以理解玩家几乎无动作却分出尊卑座次并达成牢固共识。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "东亚文化圈的人对此心领神会，而向欧美文化圈的陌生人解释则不知从何说起。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "拓荒模式中各玩家的首要问题不是帐篷内争夺，而是各凭条件四面出击；谁是老大主要看谁从荒野获得最丰厚收益，收益最丰厚者有可能获得戏剧性地位逆转。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关键在于到达能力：到达能力越不过既有围墙，围墙内的玩家就是铁笼模式；人类到达能力弱时自然分成几大纸牌屋各玩各的。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "历史上形成环地中海、东亚、南美、北美等圈层；中国自身则有巴蜀、黄河流域、长江中下游流域、长城以北等圈层。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到达能力突破铁笼四壁后进入荒野模式，待新荒野瓜分殆尽达到新边界，便在更大的铁笼里重新开始铁笼模式。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "一般来说旧铁笼崩溃释放的新荒野并不大，所谓“荒野”往往只是从前的铁笼B，因此荒野模式持续不久就会回到铁笼模式。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "1500年左右的地理大发现是异数：四个洲的巨大版图开放给欧洲铁笼玩家，将世界主流模式锁定在拓荒模式500年，这是欧洲国家1500年至2000年称霸最主要的原因。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "除非太空殖民变得足够经济，否则世界地缘政治的游戏模式正迅速重新走向铁笼模式，这一次的铁笼是地球本身。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国是在东亚铁笼里玩了三千多年铁笼模式的大玩家，至少有汉、唐、元、明、清五个“世锦赛金牌”。", "evidence": ["E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在铁笼模式里，美国“小学没毕业”。", "evidence": ["E22"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只有法国、土耳其这类有过“笼王”经验的国家勉强算有类似经验，但体量与实力不足，作者估计它们也没有意愿来参加决赛。", "evidence": ["E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国长期铁笼模式的经验就是中国渐渐走向上风的原因。", "evidence": ["E24"]}
   ],
   "argument_steps": [
    "先改换术语：以“地缘政治博弈”替代“大国博弈”，理由是后者沙文主义、无视中小国家话语权（P001）。",
    "声明中国有优势并预告先讲游戏规则（P002-P003）。",
    "给出两种模式并定义模式A铁笼模式（P004-P005），用铁笼与玩家的比喻展开（P006-P009）。",
    "指出铁笼模式的关键技能是读空气、写空气，并说明信号机制与东亚／欧美文化圈差异（P010-P013）。",
    "定义模式B拓荒模式及其胜负标准（P014-P017）。",
    "归纳两模式交替为基本机制（P018）。",
    "提出到达能力是关键变量，并用圈层史与模式切换史说明（P019-P023）。",
    "以“一般来说”限定常态下荒野模式短暂（P024）。",
    "以地理大发现为异数，解释欧洲500年称霸（P025-P028）。",
    "预测在无经济可行的太空殖民前提下世界重回铁笼模式，铁笼即地球（P029-P030）。",
    "以中国的长期铁笼经验、美国与法土的对比，得出中国渐渐走向上风（P031-P034）。"
   ],
   "concept_usage": [
    {"term": "地缘政治博弈", "meaning": "作者偏好的框架术语，用以替代“大国博弈”，强调中小国家的话语权（P001）。", "evidence": "P001", "ambiguity": "未说明该术语与“大国博弈”在分析结论上的具体差别。"},
    {"term": "铁笼模式", "meaning": "玩家被限制在同一空间内、不能离开、彼此不完全了解，靠微妙信号分出座次与达成共识的博弈模式（P005-P013）。", "evidence": "P010", "ambiguity": "“不能离开”是技术限制还是规则限制，未说明。"},
    {"term": "拓荒模式／荒野模式", "meaning": "玩家从同一营地出发、面向未知荒野各凭条件出击，以荒野收益决定地位的模式（P014-P017、P022）。", "evidence": "P016", "ambiguity": "P014 称“拓荒模式”，P022 称“荒野模式”，同一模式有两种叫法，是否完全等同未明说。"},
    {"term": "到达能力", "meaning": "决定铁笼边界与模式切换的关键变量；越不过围墙则铁笼，突破四壁则拓荒（P019-P023）。", "evidence": "P019", "ambiguity": "未定义其构成（交通、军事、通信、技术？），也未说明如何度量。"},
    {"term": "纸牌屋", "meaning": "到达能力弱时人类自然分成的几大互不往来的圈层（P020）。", "evidence": "P020", "ambiguity": "与“铁笼”是否同义，文中并用。"},
    {"term": "读空气／写空气", "meaning": "铁笼模式下解读与发出微妙信号的能力（P010-P011）。", "evidence": "P010", "ambiguity": "未说明习得方式与判别标准。"},
    {"term": "笼王／世锦赛金牌／决赛", "meaning": "竞技隐喻：长期铁笼模式经验（笼王）、历史成就（金牌）与当下竞争（决赛）（P031、P033）。", "evidence": "P031", "ambiguity": "“金牌”的具体标准未说明。"},
    {"term": "沙文主义", "meaning": "作者对“大国博弈”提法的评价（P001）。", "evidence": "P001", "ambiguity": "作者未展开该评价的推理。"}
   ],
   "examples_and_targets": [
    "铁笼、玩家、个头大／心眼多／肉厚／手长（作者自造的比喻与类型描写，P006）",
    "读空气、敬语体切换、发言顺序、摸鼻子扯衣袖使眼色（东亚交际经验举例，P010-P011）",
    "东亚文化圈与欧美文化圈（对比对象，P013）",
    "营地与未知荒野（作者自造比喻，P015）",
    "纸牌屋（比喻，P020）",
    "环地中海、东亚、南美、北美（历史地理圈层，P021）",
    "巴蜀、黄河流域、长江中下游流域、长城以北（中国内部圈层，P021）",
    "1500年左右的地理大发现；北美、南美、中南非洲、大洋洲（历史叙述，P025）",
    "汉、唐、元、明、清（作为“世锦赛金牌”的朝代列举，P031）",
    "美国（被讽刺的对比对象，P032）",
    "法国、土耳其（有“笼王”经验的比较对象，P033）",
    "太空殖民（未来条件，P029）",
    "中小国家（P001 中被指为被“大国博弈”提法无视的一方）"
   ],
   "conditions": [
    "关键例外条件：除非太空殖民变得足够经济，否则重回铁笼模式（P029）",
    "常态限定：“一般来说”“更多的情况是”（P024）",
    "触发条件：到达能力越不过既有的围墙（P020）；人类到达能力弱的时候（P020）",
    "或然限定：“有可能获得戏剧性的地位逆转”（P017）",
    "时间限定：从1500年左右开始、锁定500年、从1500年称霸到2000年（P025-P027）；中国三千年、五个朝代（P031）",
    "推测限定：“估计也没有这个意愿”（P033）；“至少”五个金牌（P031）",
    "未说明适用规模与判据：模式判断所需的到达能力阈值、圈层划分标准未给"
   ],
   "rhetoric_and_tone": "讲解式口语（“啥意思呢？打个形象的比喻”），贯穿比喻（铁笼、兽王、荒野、纸牌屋、笼王）；竞技隐喻（世锦赛金牌、决赛）；第二人称号召（“你们应该看到这故事的走向了”）；英语插入 with all due respect 作讽刺性礼貌；对美国的贬抑式调侃（“小学没毕业”）；开头对“大国博弈”提法作政治性批评。",
   "unresolved_questions": [
    "“到达能力”未定义、未给出度量方式，却是全文关键变量。",
    "两模式框架与到达能力说均是作者自建，本文未给出处、数据或文献依据，登记为待外部核查。",
    "P024 的常态规律与 P025 的“异数”之间缺乏判据：什么条件下新荒野算大、算异数，未说明。",
    "欧洲1500—2000年称霸被归因于拓荒模式为“最主要的原因”，未讨论其他因素（如工业革命、制度、军事技术）。",
    "历史断代与量化表述（地理大发现1500年左右、称霸到2000年、锁定500年、中国三千年、汉唐宋元明清五个金牌）为作者叙述，待外部核查。",
    "术语不一致：P014“拓荒模式”与 P022“荒野模式”。",
    "“美国小学没毕业”是修辞还是实质判断不明确，判断依据未给。",
    "“中国渐渐走向上风”的衡量标准与依据未说明；提问者所问的“水平如何”未被量化回答。",
    "P013 关于文化圈理解差异的断言（“想必”）无依据说明。",
    "无图片，正文与 lexical 结构一致（35 个段落节点）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“大国博弈”这个讲法不是很好，太过于沙文主义", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "中国在这方面当然是有优势。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这种游戏有两个模式。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P018", "quote": "这两个模式的交替上演，就构成了国际地缘政治博弈的基本机制。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "最关键的技能就是“读空气”的能力和“写空气”的能力", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "就已经莫名其妙的分出了尊卑座次，而且达成了共识", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "东亚文化圈的人想必不必多说自然心领神会", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P016", "quote": "首要问题反倒不是在帐篷里争夺，而是各自凭着自己的条件四面出击", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "有可能获得戏剧性的地位逆转", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P019", "quote": "这里面最关键的要害就是到达能力。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P020", "quote": "人类到达能力弱的时候，自然而然的分成了几大纸牌屋", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P021", "quote": "环地中海是一圈，东亚是一圈，南美一圈，北美一圈。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "每一次到达能力突破了铁笼的四壁", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "于是在更大的铁笼里，重新开始铁笼模式。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "开放出来的新荒野并不大", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P025", "quote": "从1500年左右开始的地理大发现", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "将整个世界的主流游戏模式锁定在了拓荒模式500年", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P027", "quote": "这其实就是欧洲国家从1500年称霸到2000年最主要的原因。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "除非太空殖民变得足够经济，否则世界地缘政治的游戏模式正在迅速的重新走向铁笼模式", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P030", "quote": "这一次的铁笼是地球本身。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P031", "quote": "在东亚铁笼里玩了三千多年铁笼模式的大玩家", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P032", "quote": "美国小学没毕业。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P033", "quote": "只有法国、土耳其这样同样有过“笼王”经验的国家", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P034", "quote": "这其实就是中国渐渐走向上风的原因。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系", "地缘政治", "历史叙述"],
   "issue_candidates": ["术语与话语权（大国博弈 vs 地缘政治博弈）", "铁笼与拓荒两种模式的交替", "到达能力与技术条件", "地理大发现与欧洲霸权", "中国的地缘经验与走向"],
   "text_function_candidates": ["解释", "框架提出", "论辩", "预测"],
   "object_candidates": ["中国", "美国", "欧洲", "法国", "土耳其", "东亚", "环地中海", "南美", "北美", "大洋洲", "中小国家", "汉", "唐", "元", "明", "清"],
   "working_keywords": ["地缘政治博弈", "铁笼模式", "拓荒模式", "荒野模式", "读空气", "写空气", "到达能力", "纸牌屋", "兽王", "笼王", "世锦赛金牌", "太空殖民", "沙文主义"]
  },
  "notes": "本篇是作者自建框架的完整论述：两种模式与“到达能力”均无出处，属作者设定，初读只如实记录其主张与限定。注意 P014“拓荒模式”与 P022“荒野模式”用词不一致；历史断代、专名与归因（1500—2000 年、三千年、五个朝代）登记为待外部核查。提问者的“大国博弈”说法被作者改换术语后作答，二者不是同一表述。无图片，正文与 lexical 一致（35 段落节点）。"
 },
 "9909de34": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）问“黑人有没有可能自己建一个州”。作者不直接回答，而是指向 Tulsa “Black Wallstreet” Massacre，称其为历史上黑人最接近凭诚实努力、依法经营在一个地区占据优势、形成有效控制的一刻，简述该地区的繁荣与自卫部队后以“失败了”作结，再把该地与发布当天的川普连任竞选集会起点并置。本篇含 4 个图片节点与外链视频，图片内容未经核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "让读者去了解 Tulsa “Black Wallstreet” Massacre。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "历史叙述与评价：该地区是黑人最接近形成有效控制的一刻；聚集黑人精英、经济繁荣自给、市场竞争力强；黑人希望建立自己的社区与家园；一战退伍黑人士兵组织半正规自卫部队。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "以“失败了”给出结局。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009"], "summary": "点出该地是川普连任竞选集会起点（就在今天），并以“值得记录的原点”“秋风起于青萍之末”暗示变局开端。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "附 Vox 相关视频外链并致谢评论区提供链接者。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "塔尔萨“Black Wallstreet”是历史上黑人最接近凭借诚实努力、依法经营在一个地区真正占据优势、形成有效控制的一刻。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该地区聚集了各地黑人精英，经济繁荣且自给自足，市场竞争力强；黑人们希望形成自己的社区与在美国的家园。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一战回乡的黑人士兵曾在该地区自发组织一支半正规的自卫部队。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这一努力失败了。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个地方是川普连任竞选集会的起点，就在发布当日。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "多年以后人们回忆起今天，可能会发现这是美国一个值得记录的原点。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“秋风起于青萍之末”暗示此刻已是某种大变动的开端（典故式表述，所指未明说）。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "以“了解一下”把提问引向具体历史事件（P001）。",
    "给出评价性判断：这是黑人最接近形成有效控制的一刻（P002）。",
    "补充该地区繁荣、自给、有竞争力的叙述（P003）。",
    "叙述黑人的家园期望与退伍士兵的自卫部队（P004-P005）。",
    "以两字短句给出结局：失败了（P006）。",
    "把该地与当天的川普连任竞选集会起点并置，并以“原点”“秋风起于青萍之末”暗示变局（P007-P009）。",
    "附外链视频并致谢提供者（P010-P011）。"
   ],
   "concept_usage": [
    {"term": "Black Wallstreet", "meaning": "指 Tulsa 的这一黑人聚居区及其经济成就，作者用其作为黑人自治最接近成功的例证（P001-P002）。", "evidence": "P002", "ambiguity": "该名称在正文中以外文引号形式出现，未给出中文对应与范围界定。"},
    {"term": "有效控制", "meaning": "作者衡量“最接近成功”的标准：在一个地区真正占据优势并形成有效控制（P002）。", "evidence": "P002", "ambiguity": "未说明有效控制的判据（人口、经济、治安、政治？）。"},
    {"term": "原点", "meaning": "作者称今天可能是美国一个值得记录的原点，指某个进程的起点（P008）。", "evidence": "P008", "ambiguity": "“原点”所指为何（种族冲突、政治转向？）未明说。"},
    {"term": "秋风起于青萍之末", "meaning": "典故式表述，用以暗示大变动的开端（P009）。", "evidence": "P009", "ambiguity": "作者未点明所指的是何种变动。"}
   ],
   "examples_and_targets": [
    "Tulsa “Black Wallstreet” Massacre（历史事件，作者引为论据，P001）",
    "该地区的黑人精英、自给自足经济、市场竞争力（历史叙述，P003）",
    "一战战场上回乡的黑人士兵及其半正规自卫部队（历史叙述，P005）",
    "川普连任竞选集会起点（时政对象，P007）",
    "Vox 视频《塔尔萨种族大屠杀——黑色华尔街消亡》（外链，P010，未查看内容）",
    "评论区用户 @冰原（致谢对象，P011）"
   ],
   "conditions": [
    "时间条件：本篇写于 2020-06-21，“就在今天”指发布当日的集会（P007）",
    "范围限定：作者称其为“历史上黑人最接近……”的一刻，属最高级比较（P002）",
    "或然限定：“可能会发现到这是美国一个值得记录的原点”（P008）",
    "未给条件：黑人能否建州这一提问未被直接回答，也没有给出可复制的条件分析"
   ],
   "rhetoric_and_tone": "极短篇：历史叙述＋时政时点并置＋典故收尾。语气克制，以“失败了。”独立成句作转折；“就在今天”“今天，秋风起于青萍之末”把历史与当下叠合，带预言性暗示；附外链并致谢，呈资料分享姿态。",
   "unresolved_questions": [
    "图片未核验：本篇含 4 个图片节点（IMG001—IMG004），本记录未读图，需人工／多模态复核，故 status=needs_reread、image_checked=false。",
    "P010 外链视频（Vox·哔哩哔哩）内容未查看，其对本篇论点的支持程度不明。",
    "作者未明说川普集会地点与塔尔萨屠杀之间的关联，只作并置，读者可能自行推断。",
    "历史事实（屠杀经过、地区繁荣程度、自卫部队）正文未给出处，登记为待外部核查。",
    "“失败了”所指是屠杀终结了该社区，还是“建国”理想失败，未展开。",
    "提问者的“自己建一个州”未被正面回应，本文只提供一个历史先例。",
    "P010、P011 在 lexical 中为 link 节点与空段落，正文与结构不完全一致。",
    "brief 在“黑人们抱着强”处截断，属语料摘要字段截断，仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "历史上黑人最接近凭借诚实努力、依法经营在一个地区真正占据优势", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "聚集了四面八方而来的黑人精英，经济上相当繁荣而且自给自足", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "黑人们抱着强烈的希望，想要形成自己的社区，自己在美国的家园。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "从一战战场上回乡的黑人士兵们自发的在这个地区组织了一支半正规的自卫部队", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "失败了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "这个地方，是川普连任竞选的集会起点。就在今天。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "可能会发现到这是美国一个值得记录的原点", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "今天，秋风起于青萍之末。", "relation": "context"},
    {"key": "E9", "paragraph_id": "P010", "quote": "塔尔萨种族大屠杀——黑色华尔街消亡", "relation": "context"},
    {"key": "E10", "paragraph_id": "P011", "quote": "感谢评论区 @冰原 提供链接", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["美国史", "种族与族群", "时政评论"],
   "issue_candidates": ["黑人自治与建州可能", "塔尔萨种族屠杀", "黑人华尔街的兴衰", "川普竞选集会与种族历史的并置"],
   "text_function_candidates": ["答疑", "历史点引", "评论"],
   "object_candidates": ["黑人", "Tulsa", "Black Wallstreet", "川普", "美国", "Vox", "一战黑人士兵", "@冰原"],
   "working_keywords": ["黑色华尔街", "种族大屠杀", "自给自足", "自卫部队", "原点", "青萍之末"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 4 个图片节点（IMG001—IMG004，lexical 中对应若干空段落节点），子代理无读图能力，图片内容未经核验，故 status=needs_reread、image_checked=False；已读部分为正文文本与结构清单。P010 为外链（Vox 视频·哔哩哔哩），未查看其内容；P011 致谢评论区 @冰原。P007 的时点表述（“就在今天”）对应 2020-06-20 川普塔尔萨竞选集会，属时效性内容，待外部核查；历史事实正文未给来源，登记待外部核查。作者未明说集会地点与屠杀的关联。brief 截断于“黑人们抱着强”，仅作导航。"
 },
 "d169a3ca": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）问“如何看待说谎这件事”。作者不谈个案评价，而是提出“说谎政策”应有天然质量标准（能否最有效抑制说谎），先引述并反驳一般流行的“疾谎如仇”策略，再从“人不可能不说谎”“人都是恶的”推出“不计较人的恶”“尽可能豁免人的诚实义务”，最后用买卖赊账的例子说明以可承受损失换取关系深入的授信式做法，主张这是成本最低、最有效的解决谎言问题的方法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "说谎被视为麻烦甚至威胁；评价“说谎政策”的天然质量标准是能否最有效抑制说谎。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "引述一般流行的策略（朋友绝不能说谎或隐瞒，否则即背叛）并声明作者不这样设计策略。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "理由：人不可能做到不说谎，认知不可能完全客观真实，所有描述本身就是错的（不精确即是错误）；未被追究的表达只是误差小、未造成明显痛感。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "从疑心到辩解无效的链条，并列出五重“无可避免”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "结论：绝对罪化与高度敏感是埋在一切亲密关系里的两根雷管，会使其不可避免走向失败；作者称这是客观事实而非价值判断；亲密关系范围含朋友、同志、同事、师生等。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "限定：也可以选择不追求长期亲密关系，未必不可行；以下论述基于“将有效关系视为人生的绝对核心资产”的价值观设定，设定即“不计较人的恶”。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "理由：人都是恶的、管不住潜意识与本能；计较人的恶只能浅交，最终反目成仇，“越爱，越成仇”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "训诫式断言：不容忍人的恶是一件（大）残忍的事。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "定义：衡量一件事能否称为能力的标准是它是否提高对他人的恶的耐受程度。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P032", "P033"], "summary": "交往的前提应是愿以可忍受的痛苦去赌足够的收益，赌输则愿赌服输。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "策略应用：尽可能豁免人的诚实义务——奉行没有承诺就无诚实义务、少索取承诺（可以不问就不问）、遏制隐私刺探冲动；无明文承诺处发现说谎也不予追究。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "定义“不予追究”（不含终止关系）并说明终止关系是个人自由；以卖米赊账为例：选择相信就自己负全责，不追索，但停止再次交易。", "role": "example"},
    {"unit_id": "U013", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064"], "summary": "管理谎言靠三条（米好、对无抵押信任的风险承受力保守掌握、自身是低交易成本的优秀交易对象）＋严苛审查继续来往资格；并用授信额度累积示例说明信用是自己打拼出来的，“交易额”即合作深入程度。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072"], "summary": "解释一般人采用“疾谎如仇”模式的成因：不耐烦精细风险管理、生存挑战逼迫结成超高风险关系、以暴力威胁夺取未来利益作抵押、以隐私调查求安全、以相互威慑缔结关系，而这种关系有天然半衰期且在实践上逻辑不通。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080"], "summary": "若嫌信用积累太慢，给出三条选择：尽早开始、自强不息提高承受力与首次授信额度、提高经营能力（利润率与关系进展速度成指数关系）。", "role": "action_advice"},
    {"unit_id": "U016", "paragraph_refs": ["P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089"], "summary": "结论：只要足够耐心，这是必胜之策；胜券在握者有更大仁慈；结果是人们宁可对别人说谎也不愿对你说谎，因为对你说谎最安全最不被追讨；最后反问失去你是否值得可惜。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对待说谎的态度（“说谎政策”）有一个天然的质量标准：看它能不能最有效地抑制说谎现象的发生。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "一般流行的策略是：做我朋友绝对不能对我说谎、不能隐瞒与我利害相关的重要信息，否则就是背叛，背叛就要狠狠报复。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人不可能做到“不说谎”：人对自身和事物很少有（或根本不可能有）完全客观真实的认知，所有的描述本身就是错的（不精确即是错误）。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那些被认为没有问题的表达，只是错误和误差不大、没造成明显痛感后果，所以没被拿来说事。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "损失反复或过大时人会产生无法抑制的疑心；疑心一起，被怀疑者除全额赔偿潜在损失外无法靠逻辑说明说服对方，辩解没有证明效力。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从表述错误到疑心辩解不清构成一条五重“无可避免”的链条（含“只要相处够密切、时间足够久”这一条件）。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切亲密关系迟早会因“对谎言的绝对罪化”和“对谎言的高度敏感”而不可避免走向失败；这是客观事实，不是价值判断。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果不打破这道铁链，任何亲密关系都注定不能持久。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "也可以选择不再追求长期亲密关系，这未必不可行；下文论述则以“将有效关系视为人生的绝对核心资产”的价值观为设定前提。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "追根到底人都是恶的：即使抱有极大善意和决心，人也管理不住自己的潜意识和本能。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "计较人的恶就只能浅交、无法深交；高频交往必然经勉强忍受、忍无可忍到反目成仇，最后双双后悔认识对方，“越爱，越成仇”。", "evidence": ["E17", "E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不容忍人的恶是一件足称残忍的事；丝毫不能容忍更是大残忍。", "evidence": ["E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一件事能否称为能力，最基本的衡量方式是它是否提高你对他人的恶的耐受程度；“我有多能承受弱人的恶”是绝对有效的标准。", "evidence": ["E20", "E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人与人相交不应以“肯定有净获益”为前提，而应以“愿意忍受可忍受的痛苦来赌足够收益”为前提；赌输则愿赌服输、于人无尤。", "evidence": ["E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该策略在撒谎问题上的应用就是尽可能豁免人的诚实义务：奉行“没有承诺就无诚实义务”，并尽可能少索取承诺（可以不问就不问），遏制不安全感驱动的隐私刺探。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不予追究”指不自行授予惩罚、讨还的权利，不包括终止关系；终止关系是完全的个人自由，不需要对方有过错或公正审判。", "evidence": ["E26", "E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在赊账例子中，选择相信对方就自己负全责：对方不还钱时责怪自己的判断力，不去追索，但会停止再次卖米。", "evidence": ["E28"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "管理谎言靠三条：米好使对方掂量失去交易资格的损失；对“无抵押绝对信任风险承受力”保守掌握；自身是快捷授信、低交易成本、次生风险小的优秀交易对象；并以极其严苛的标准审查继续来往的资格。", "evidence": ["E29", "E30", "E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "信用是对方自己打拼出来的，而作者一直是先伸出橄榄枝的一方。", "evidence": ["E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者对一般人采用“疾谎如仇”模式的解释：不耐烦做精细风险管理，生存挑战逼迫尽快结成超出自身风险承担能力的关系，于是用暴力威胁夺取对方未来利益作抵押，并靠大量隐私调查求安全。", "evidence": ["E33"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基于相互威慑的关系有天然半衰期；它不可选不是因为形而上的原因，而是实践上逻辑不通。", "evidence": ["E34", "E35"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不能因为嫌可行的方法慢就换成不可行的方法；可行的加速选择是尽早开始、自强不息提高承受力与首次授信额度、提高经营能力（利润率与关系进展速度成指数关系）。", "evidence": ["E36", "E37", "E38"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "只要你有足够耐心，这就是系统战胜谎言的必胜之策；胜券在握的人自然而然有更大的仁慈。", "evidence": ["E39", "E40"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "结果是人们宁可对别人说谎，也不愿对你说谎——恰恰因为对你说谎最安全最不会被追讨；这是成本最低、最有效的解决谎言问题的方法，而非靠暴力与交叉抽查。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C025", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以反问收尾：以你所做的，失去你真的值得可惜吗？", "evidence": ["E44"]}
   ],
   "argument_steps": [
    "提出评价标准：说谎政策的好坏看能否最有效抑制说谎（P001-P002）。",
    "引述一般流行的“疾谎如仇”策略并声明自己不采用（P003-P005）。",
    "给出前提一：人不可能不说谎，因为认知不可能完全客观真实，所有描述本身就是错的（P006-P008）。",
    "给出由损失到疑心、再到辩解无效的链条，并列为五重不可避免（P009-P011）。",
    "推出结论：绝对罪化与高度敏感使一切亲密关系不可避免走向失败，并称其为客观事实（P012-P016）。",
    "作出限定：可以不追求长期亲密关系，下文以“有效关系是人生绝对核心资产”为价值观设定（P017-P018）。",
    "给出前提二：人都是恶的、管不住本能，计较则只能浅交并终至反目成仇（P019-P023）。",
    "以训诫式断言强化：不容忍人的恶是残忍的事（P024-P027）。",
    "确立能力标准：是否提高对他人的恶的耐受程度（P028-P031）。",
    "提出交往前提：以可忍受的痛苦赌足够收益，赌输愿赌服输（P032-P033）。",
    "把策略落到说谎问题：尽可能豁免人的诚实义务（少问、少索取承诺、不刺探隐私）（P034-P041）。",
    "界定“不予追究”并保留终止关系的自由（P042-P043）。",
    "用卖米赊账的例子演示自担风险、不追索但停止交易（P044-P049）。",
    "给出管理谎言的三条依靠与严格的资格审查，并用授信累积示例说明交易额的增长（P050-P064）。",
    "解释一般人为何采用“疾谎如仇”模式，指出其相互威慑关系的半衰期与逻辑不通（P065-P072）。",
    "给出嫌慢时的三条加速选择（P073-P080）。",
    "收束为必胜之策，并推出“人们不愿对你说谎”的结果与最后反问（P081-P089）。"
   ],
   "concept_usage": [
    {"term": "说谎／谎言", "meaning": "被等价于“表述不符合事实”，因此包含不可避免的认知误差与不精确（P006-P008）。", "evidence": "P006", "ambiguity": "“不精确即是错误”是作者给定的强定义，与日常“说谎”含故意欺瞒的用法不同，作者未讨论这一差别。"},
    {"term": "说谎政策", "meaning": "个人对待说谎的态度问题，其质量标准是能否最有效抑制说谎（P002）。", "evidence": "P002", "ambiguity": "“最有效”的度量方式未说明。"},
    {"term": "对谎言的绝对罪化／对谎言的高度敏感", "meaning": "作者概括的流行策略的两个特征，称其为埋在一切亲密关系里的两根雷管（P012-P013）。", "evidence": "P013", "ambiguity": "作者未标明该概括的出处或代表人物，与 P003 的引述关系未明说。"},
    {"term": "亲密关系", "meaning": "不只指恋人关系，还包括一切长期而关键的关系，如朋友、同志、同事、师生（P015）。", "evidence": "P015", "ambiguity": "未说明是否存在不适用该结论的例外关系。"},
    {"term": "恶", "meaning": "人皆有之、源于潜意识与本能的不可管理（P019）。", "evidence": "P019", "ambiguity": "未定义“恶”的内容与程度；“弱人的恶”一语中的“弱人”也未说明。"},
    {"term": "能力（衡量标准）", "meaning": "一件事能否称为能力，看它是否提高对他人的恶的耐受程度；反之则是缺陷（P028-P031）。", "evidence": "P031", "ambiguity": "该标准是充分条件还是必要条件未说明，且与“耐受恶”互为定义，存在循环之嫌。"},
    {"term": "豁免诚实义务", "meaning": "奉行“没有承诺就无诚实义务”，并尽可能少索取承诺、少刺探隐私（P036-P038）。", "evidence": "P036", "ambiguity": "哪些信息属于必须询问的例外，未说明。"},
    {"term": "不予追究", "meaning": "不自行授予自己惩罚、讨还的权利，但不包括终止关系（P042）。", "evidence": "P042", "ambiguity": "与“不追索”的关系未明确区分。"},
    {"term": "无抵押绝对信任（授信）", "meaning": "以自己承受得起的损失为上限先给出信任，额度随往来与利润率增长（P053、P056-P058）。", "evidence": "P053", "ambiguity": "授信额度与利润率的换算方式只有示例，未给一般规则。"},
    {"term": "交易额", "meaning": "作者称其“是合作深入程度的另一种表述”（P064）。", "evidence": "P064", "ambiguity": "未说明除货币外的度量方式。"},
    {"term": "疾谎如仇", "meaning": "作者给一般人策略起的名称，特征是以暴力威胁与隐私调查为抵押（P065-P068）。", "evidence": "P065", "ambiguity": "命名是否作者自造、是否有出处，未说明。"},
    {"term": "半衰期", "meaning": "相互威慑式关系的天然衰减（P071）。", "evidence": "P071", "ambiguity": "借用物理术语，未给出衰减速度或判据。"},
    {"term": "罪原", "meaning": "P009 中“人的罪原就会发生作用”一语，作者用以指人身上会被触发的某种机制。", "evidence": "P009", "ambiguity": "疑为错字（罪愆／罪源？），含义无法确定，见未决问题。"}
   ],
   "examples_and_targets": [
    "一般流行的策略（被引述并对照的他人观点，P003）",
    "米与十块钱赊账的例子（作者自设的例子，P044-P058）",
    "马云（假设例：一开口可授信100万，P077）",
    "守财奴（“钱越多越疑心别人要绑票你”的缺陷例，P030）",
    "利润率20%与10%的授信次数计算（示例，P080）",
    "摸底调查、上查三代、外查九族、一日三查、不定时抽查（对他人做法的描写，P068）",
    "拿刀架在别人脖子上外加疯狂交叉抽查（比喻，P088）",
    "“疾谎如仇”模式与相互威慑、对等补偿（作者对他人策略的分析，P065-P070）"
   ],
   "conditions": [
    "链条成立条件：“只要相处够密切、时间足够久”（P011）",
    "结论条件：“如果你不打破这道铁链”（P016）",
    "价值观设定前提：“将有效关系视为人生的绝对核心资产”（P017）；作者另注明若不追求长期亲密关系则下文不适用",
    "原则性条件：“没有承诺就无诚实义务”（P036）；“可以不问的，就索性不问”（P037）",
    "追究范围限定：“在没有明文承诺的部分”（P041）；“如果发现了对方在说谎”（P041）",
    "风险限定：授信额度限于自己赔得起的范围（P047、P053、P062）",
    "时间与耐心条件：“只要你有足够耐心”（P081）",
    "权衡限定：“不太值得”（P053）；“不是不能……而是逻辑不通”（P072）",
    "未说明：不同文化、不同权力关系下的适用性未被讨论"
   ],
   "rhetoric_and_tone": "第一人称经验与自我设计（“我不是这样设计我的策略”）；强断言与重复强调（“记住这句话——”三连排比 P025-P027）；密集反问（P035、P050、P065、P073、P089）；引述流行策略时保留脏话（P003 引文内，属他人话语）；交易与商业隐喻（授信、交易额、利润率、半衰期）；对读者的第二人称劝导；以“愿赌服输”“一笑置之”等自陈态度；结尾以反问把问题推回读者。",
   "unresolved_questions": [
    "P009“人的罪原”用词不明，疑为“罪愆／罪源”之误，含义无法确定。",
    "“不精确即是错误”（P006）作为前提未加证明；它与日常语言中“说谎”含故意欺瞒的用法之间的关系未讨论。",
    "“人都是恶的”（P019）未定义“恶”，也未给依据；“弱人的恶”（P031）中的“弱人”未说明。",
    "P028-P031 的能力标准与“耐受恶”可能互为定义，是否循环未说明。",
    "“对谎言的绝对罪化”和“对谎言的高度敏感”是作者对流行策略的概括，未标明出处或代表人物，与 P003 引文的关系未明说。",
    "P066 对一般人动机的解释（不耐烦、生存挑战逼迫、暴力威胁抵押）为作者推测，无证据。",
    "P080 的“指数关系”未给推导与算式口径（只说“拿出计算器试试”）。",
    "P082“胜券在握的人，自然而然有更大的仁慈”缺依据。",
    "P047-P058 的米价与利润数字（10元、3元、7元、15元等）为示例假设，未逐项核算是否存在算术不一致。",
    "无图片，正文与 lexical 一致（89 个段落节点）；brief 截断于“否则就是背叛我”，仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "就有一个天然的质量标准——看它能不能最有效的抑制说谎现象的发生", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "做我的朋友绝对不能对我说谎，也不能对我隐瞒可能与我利害相关的重要信息", "relation": "context"},
    {"key": "E3", "paragraph_id": "P006", "quote": "首先认识到人是不可能做到“不说谎”的", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "所有的描述本身就是错的（不精确即是错误）", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "只是其错误和误差不是很大，没有酿成当事人有明显痛感的后果", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "你就会无法抑制自己的疑心", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "都不过是抵死也不承认的表现罢了，根本没有证明效力", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "表述错误，无可避免", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "只要相处够密切、时间足够久", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P012", "quote": "迟早会因为“对谎言的绝对罪化”和“对谎言的高度敏感”而不可避免的走向失败", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "这是两根埋在一切亲密关系里的雷管", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "这不是什么价值判断，而是一种不以人的意志喜好为转移的客观事实", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "你的任何亲密关系都注定不能持久", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "这个也未必不可行", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P017", "quote": "将有效关系视为人生的绝对核心资产", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P019", "quote": "追根到底，人都是恶的", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "你就只能和人浅交，无法和人深交", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "越爱，越成仇。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "不容忍人的恶，是一件足称残忍的事。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P028", "quote": "它是否会提高你对他人的恶的耐受程度？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P031", "quote": "“我有多能承受弱人的恶”是一个绝对有效的标准", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P032", "quote": "而是以“我愿意以忍受我可以忍受的痛苦，来赌我会获得足够的收益”为前提的", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P034", "quote": "就是尽可能豁免人的诚实义务", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P036", "quote": "奉行“没有承诺就无诚实义务”的原则", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P038", "quote": "尽可能遏制自己的不安全感驱动的隐私刺探冲动", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P042", "quote": "是指不自行授予自己惩罚、讨还的权利，不包括终止关系", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P043", "quote": "终止关系是完全的个人自由", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P048", "quote": "我选择了相信你，我就自己负全责", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P052", "quote": "然后你不得不掂量被我切断交易资格的损失", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P053", "quote": "靠我对“无抵押绝对信任风险承受力”的保守掌握", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P055", "quote": "但极其严苛的审查继续来往的资格", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P059", "quote": "你的信用，其实是你打拼出来的", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P066", "quote": "ta们动用了自己的暴力威胁能力，强行夺取了对方的未来利益", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P071", "quote": "其实存在着一个天然的半衰期", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P072", "quote": "不是因为什么形而上的原因，而是实践上逻辑不通", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P074", "quote": "不能因为嫌一个可行的方法慢而换成一个不可行的方法", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P077", "quote": "提高自己首次授信的额度", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P079", "quote": "这个利润率和关系的最大健康进展速度有直接关系——而且是指数关系", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P081", "quote": "只要你有足够耐心，这是必胜之策", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P082", "quote": "胜券在握的人，自然而然有更大的仁慈。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P085", "quote": "恰恰对你说谎是最安全、最不会被追讨的，所以反而最不愿对你说谎", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P087", "quote": "才使得人们主动的不愿意以谎言对你", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P088", "quote": "这才是成本最低、最有效的解决谎言问题的方法", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P089", "quote": "那么，以你所做的，失去你真的值得可惜吗？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理", "人际关系", "策略与风险管理"],
   "issue_candidates": ["说谎政策的质量标准", "对谎言的绝对罪化与高度敏感", "亲密关系的可持续性", "对他人之恶的容忍", "以授信与信用积累替代威慑"],
   "text_function_candidates": ["答疑", "论辩", "经验总结", "行动建议"],
   "object_candidates": ["马云", "守财奴", "朋友", "同志", "同事", "师生", "恋人"],
   "working_keywords": ["说谎政策", "绝对罪化", "高度敏感", "雷管", "亲密关系", "不计较人的恶", "耐受程度", "豁免诚实义务", "无抵押绝对信任", "授信", "交易额", "疾谎如仇", "半衰期", "愿赌服输"]
  },
  "notes": "长篇策略论述，正文 89 段完整，无图片。P003 的“一般流行的策略”以引号引述，属他人观点，已按 opponent_view／opponent 记录，未归给作者。P009“罪原”疑为错字，已在未决问题登记，引用保留原文用字。P066 等处对他人心理与动机的解释是作者的因果推测。P080 的算术示例与 P047-P058 的数字未逐项核算。brief 截断于“否则就是背叛我”，仅作导航，未用于支持主张。"
 },
 "7950429d": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）自述随着对女权主义的理解加深而越来越怀疑女权主义，问“女权到底是什么”。作者不回答“女权的内容”，而是先反问一个家庭若只要接受女性对自身权利的追求就会破碎，它对女性还有什么正当的存在理由；随后反驳争辩“正确／错误的女权”的人，指出自己谈的是女性“争取女权”这一权利本身，并批评题干把家庭破裂归因于“女性想要争取女权”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以反问质问那种一接受女性权利追求就破碎的“家庭”的正当性，称想不出任何说得通的理由，并以屠宰场作比。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "指出很多人在争辩“正确／错误的女权”，但作者谈的是女性“争取女权”这一权利本身。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "把内容问题暂置，先问女性能不能争取女性权利。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "批评题干把“家庭破裂”归因于“女性想要争取女权”而非某项确切权利，并称之为“【连根反】”。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "把“女权到底是什么”指向另一篇文章（链接标题：《第一性》《为什么女权指男女平权，男权就指男性特权？》）。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "如果一个“家庭”只要接受女性对自身权利的追求就会破碎，这个“家庭”对女性就没有正当的存在理由（以反问形式提出）。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "这种“家庭”与屠宰场没有区别（以反问形式提出）。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人争辩“正确／错误的女权”，但他们错了；作者谈的是女性“争取女权”这一权利本身。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "女权的内容可以稍后再谈，先要问：女性能不能争取女性权利。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "题干把“家庭破裂”归因于“女性想要争取女权”，而不是归因于女性想要争取某项确切的权利，这就是“【连根反】”，没什么可喊冤的。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "关于女权到底是什么，作者指出另有一篇写了（链接标题指向《第一性》与《为什么女权指男女平权，男权就指男性特权？》）。", "evidence": ["E9", "E10"]}
   ],
   "argument_steps": [
    "以条件式反问判断那种家庭的正当性（P001）。",
    "声明想不出任何说得通的理由，并以屠宰场作比（P002-P003）。",
    "把流行的“正确／错误女权”之争判为跑题，改问“争取女权”这一权利本身（P004-P005）。",
    "把内容问题暂置，先问女性能不能争取女性权利（P006）。",
    "回到题干，指其归因对象是“女性想要争取女权”而非某项确切权利，并命名为“【连根反】”（P007-P008）。",
    "把“女权是什么”转交给另一篇文章（P009-P010）。"
   ],
   "concept_usage": [
    {"term": "女权", "meaning": "本篇被拆成两层：女权的“内容”（正确／错误之争）与女性“争取女权”这一权利本身；作者只谈后者（P005-P006）。", "evidence": "P005", "ambiguity": "作者未在本文给出女权的定义，指向另一篇；两层之间的关系未展开。"},
    {"term": "连根反", "meaning": "作者用来指题干式的归因方式：把家庭破裂归因于“女性想要争取女权”这一根本，而不是某项确切权利（P008）。", "evidence": "P008", "ambiguity": "该词为作者自造或借用的标签，本文未定义其含义，方括号写法也未说明。"},
    {"term": "正当的存在理由", "meaning": "作者衡量家庭的尺度：能否容纳女性对自身权利的追求（P001）。", "evidence": "P001", "ambiguity": "未说明“正当”的判据与他人权利的边界。"},
    {"term": "屠宰场", "meaning": "对上述“家庭”的比喻性对照物（P003）。", "evidence": "P003", "ambiguity": "属修辞性类比，作者未展开可比性。"}
   ],
   "examples_and_targets": [
    "那种“只要接受女性的对自己权利的追求就会破碎”的家庭（被质疑对象，P001）",
    "屠宰场（比喻，P003）",
    "争辩“正确／错误的女权”的很多人（被反驳对象，P004-P005）",
    "题干（提问者的表述，被批评对象，P007）",
    "《第一性》《为什么女权指男女平权，男权就指男性特权？》（外链文章标题，P010，内容未查看）"
   ],
   "conditions": [
    "条件句：“如果一个‘家庭’只要接受女性的对自己权利的追求就会破碎的话”（P001）",
    "归因限定：题干归因于“女性想要争取女权”，而非“女性想要争取xxx确切的权利”（P007）",
    "暂置条件：“女权是什么内容再谈”（P006）",
    "未说明：家庭、女性、权利的具体范围与不同文化／法律条件下的差异未被讨论"
   ],
   "rhetoric_and_tone": "连续反问（P001、P003、P006）；“你们错了”的直接指责；以“屠宰场”作尖锐类比；“没什么可喊冤的”带讥讽；用方括号【连根反】作标签式命名；末尾以链接把定义问题转交他文。",
   "unresolved_questions": [
    "“连根反”未在本文定义，方括号用法含义不明。",
    "作者所称题干内容（把“家庭破裂”归因于“女性想要争取女权”）与输入 question 字段不逐字对应（输入问题只有“我越来越怀疑女权主义的观点。女权到底是什么？”），可能题干另有版本或被截断，需核对原始题干。",
    "“女权到底是什么”本文未回答，指向 P010 的两条外链标题，链接内容未查看。",
    "P010 在 lexical 中为两个 link 节点与空段落，正文与结构不完全一致。",
    "提问者“怀疑女权主义”的立场未被作者直接回应，作者只回应了题干中的归因方式。",
    "无图片；未说明“正当的存在理由”的判据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个“家庭”对女性有什么正当的存在的理由？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "我实在是想不出任何一条说得通的理由。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这种“家庭”和屠宰场有什么区别？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "很多人在争辩什么叫“正确的女权”，什么叫“错误的女权”。", "relation": "context"},
    {"key": "E5", "paragraph_id": "P005", "quote": "我在谈的是女性“争取女权”这一权利本身", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "女性能不能争取女性权利？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "可不是归因于“女性想要争取xxx确切的权利”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "这就是【连根反】", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "至于女权到底是什么，这里面有一篇写了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "为什么女权指男女平权，男权就指男性特权？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别议题", "女权", "家庭伦理"],
   "issue_candidates": ["女性争取权利的权利", "家庭的正当性", "“正确／错误女权”之争", "题干的归因方式"],
   "text_function_candidates": ["答疑", "反驳", "评论"],
   "object_candidates": ["女性", "家庭", "提问者"],
   "working_keywords": ["女权", "男权", "平权", "男性特权", "连根反", "屠宰场", "正当的存在理由", "第一性"]
  },
  "notes": "含两条外链节点（P010 的两行链接标题：《第一性》《为什么女权指男女平权，男权就指男性特权？》），链接内容未查看；lexical 另有 horizontalrule 节点，正文与结构不完全一致。P004-P005 的“很多人／你们”是被作者反驳的他人（争辩正确与错误女权者），已按被反驳观点记录。P007 所称题干内容与输入 question 字段不逐字对应，已登记待核。无图片。"
 },
 "220f3a75": {
  "analysis": {
   "question_context": "提问者（Q001，归提问者）问“摩擦力的原理是什么”。作者判定这个问题本身需要修改：摩擦力是按力的效果表现命名的，不是可单独讨论的合法概念，因此“原理”之问无意义；正确做法是把摩擦现象的不同机制分开、分别回答其原理。作者随后给出工程上的判断：真正有必要从原理上回答的大概只有分子级别上有序（或均一）表面之间的摩擦，并指出现代工业回避干摩擦的实践与利用摩擦机制切换的设计。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "判定“摩擦力”是按效果表现命名，因此不是可单独讨论的合法概念（作者评其为 nasty）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "以“拉力／推力／冲击力”为同类概念，指出问“推力的原理”没有意义。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "只有以力的机制本身命名的力（电磁力、万有引力）才有“原理”可言。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "断言：无效的问题就没有有效的答案。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "结论：该问题需修改，应把摩擦现象的不同机制分开，分别回答各自原理。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P007"], "summary": "限定：工程上真正有必要从原理回答的摩擦问题大概只有分子级别上有序（或均一）表面之间的摩擦，往往涉及非固相，只有该级别才有可有效计算的基础。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P008", "P009"], "summary": "实践表现：对工况稳定有高度追求的设计极力避免干摩擦（润滑或悬浮）；否则没法算，摩擦效应随速度变化，系统稍复杂即表现神秘，威胁可靠性与可用性。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P010"], "summary": "评价：能巧妙利用同一摩擦对多种摩擦机制切换作为核心效能的设计是令人感叹的杰作。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“摩擦力”是按力的效果表现来命名的，因此甚至不是一个可以被单独讨论的合法概念。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "摩擦力本质上与“拉力”“推力”“冲击力”同类；问“推力的原理是什么”没有意义。", "evidence": ["E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有以力的机制本身来命名的力（如电磁力、万有引力）才能合法地问“原理”。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无效的问题就没有有效的答案。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该问题需要修改才能有合理答案：应把摩擦现象的不同机制分开，分别回答不同摩擦现象的原理。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在工程上，真正有必要从原理上回答的摩擦问题大概只有分子级别上有序（或均一）表面之间的摩擦，这往往涉及非固相；只有这个级别才有可以有效计算的基础。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代工业中对工况稳定有高度追求的设计都极力避免干摩擦，或用充分润滑或用悬浮，直接回避固相表面的摩擦问题。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "否则没法算：运转速度不同就会发生复杂的摩擦效应变化，系统稍复杂表现就是神秘的，严重威胁设计的可靠性和可用性。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能巧妙利用同一摩擦对多种摩擦机制切换作为核心效能的设计，是令人感叹的杰作。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "先给概念定性：摩擦力按效果命名，不是可单独讨论的合法概念（P001-P002）。",
    "以拉力、推力、冲击力作同类类比，指出问“推力的原理”无意义（P003）。",
    "对比以机制命名的力（电磁力、万有引力）才有“原理”可言（P004）。",
    "给出总判断：无效的问题没有有效答案（P005）。",
    "提出修改方案：分开摩擦现象的不同机制，分别回答（P006）。",
    "限定可行范围：大概只有分子级别上有序（或均一）表面的摩擦有必要且有可计算基础（P007）。",
    "以工业实践佐证：回避干摩擦、否则无法计算并威胁可靠性（P008-P009）。",
    "以对利用摩擦机制切换的设计的赞赏收束（P010）。"
   ],
   "concept_usage": [
    {"term": "摩擦力", "meaning": "按力的效果表现命名的概念；作者认为它不是一个可以被单独讨论的合法概念（P002）。", "evidence": "P002", "ambiguity": "作者未说明在什么替代框架下讨论这些现象。"},
    {"term": "命名方式（效果命名／机制命名）", "meaning": "区分问题是否合法的标准：以机制命名的力才有“原理”属性（P002-P004）。", "evidence": "P004", "ambiguity": "“机制”与“效果”的划界标准未严格给出。"},
    {"term": "干摩擦", "meaning": "固相表面之间的摩擦问题，现代工业中对工况稳定有高追求的设计极力避免（P008）。", "evidence": "P008", "ambiguity": "未界定干摩擦与润滑、悬浮状态之间的过渡条件。"},
    {"term": "分子级别上有序（或均一）的表面", "meaning": "作者认为唯一有必要从原理回答且有可计算基础的摩擦问题所在（P007）。", "evidence": "P007", "ambiguity": "“有序／均一”的判据与测量方式未说明。"},
    {"term": "同摩擦对", "meaning": "P010 中作为设计核心的术语，指构成摩擦的一对表面；其多种摩擦机制的切换可被利用。", "evidence": "P010", "ambiguity": "该术语未定义，具体指哪些机制未列出。"},
    {"term": "nasty", "meaning": "作者对“摩擦力”这一概念的评语，指其难处理、不合法（P001）。", "evidence": "P001", "ambiguity": "属口语评价，未给出技术定义。"}
   ],
   "examples_and_targets": [
    "拉力、推力、冲击力（作为同类概念的类比，P003）",
    "电磁力、万有引力（作为以机制命名的对照示例，P004）",
    "充分润滑、悬浮（现代工业回避干摩擦的做法，P008）",
    "同摩擦对多种摩擦机制的切换（被赞赏的设计思路，P010）",
    "提问者的“摩擦力的原理”之问（被判定为无效问题，P005-P006）"
   ],
   "conditions": [
    "领域限定：“在工程上”（P007）",
    "范围限定：“大概只有在分子级别上有序（或均一）的表面之间的摩擦”（P007）",
    "或然与频度限定：“往往是涉及到非固相的摩擦问题”“大概只有”（P007）",
    "对象限定：“对工况稳定有高度追求的设计”（P008）",
    "条件后果：“运转速度不同”“系统稍微复杂”（P009）",
    "未说明：适用尺度（宏观低速、真空、生物摩擦等）与各机制的分类清单"
   ],
   "rhetoric_and_tone": "概念批评式，语气直接；用英文口语词 nasty 作评语；以第二人称示范式论证（“你看，你就根本不会问”）；断言短句（“无效的问题，就没有有效的答案。”）；以工程实践与设计鉴赏收尾，带赞赏口吻。",
   "unresolved_questions": [
    "作者只提出应把摩擦现象的不同机制分开回答，却未在本文列出机制分类，也未回答任何一种机制的“原理”。",
    "“分子级别上有序（或均一）的表面”的判据、测量与“非固相”摩擦的含义未展开。",
    "“有意义／无意义”“合法概念”的判断标准未严格定义，属作者的语言哲学用法。",
    "“同摩擦对”未定义；可切换的多种摩擦机制未列举。",
    "作者关于命名与可计算性的判断是否为相关领域共识，需外部核查；本文未给出任何出处。",
    "无图片，正文与 lexical 结构一致（10 个段落节点）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“摩擦力”老实说是一个非常nasty的概念。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "它是根据力的效果表现来命名", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "就不是一个可以被单独讨论的合法概念", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "本质上它是和“拉力”“推力”“冲击力”一样的概念", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "因为你知道这样问是没有意义的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "只有以力的机制本身来命名的那些才能合法的问出这个问题", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "无效的问题，就没有有效的答案。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "所以这个问题是需要修改才能有合理的答案的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P006", "quote": "把摩擦现象的不同机制分开，然后分别回答不同的摩擦现象的原理", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "大概只有在分子级别上有序（或均一）的表面之间的摩擦", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P007", "quote": "才有一个可以有效计算的基础", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "对工况稳定有高度追求的设计都极力的避免干摩擦", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P009", "quote": "不然没法算。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P009", "quote": "严重的威胁设计的可靠性和可用性", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P010", "quote": "能巧妙的利用同摩擦对的多种摩擦机制的切换来作为核心效能的设计", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["物理学", "摩擦学", "工程设计"],
   "issue_candidates": ["摩擦力的命名与概念合法性", "力的分类（效果命名与机制命名）", "摩擦问题的可计算性", "干摩擦的回避与利用"],
   "text_function_candidates": ["答疑", "概念批评", "解释"],
   "object_candidates": ["现代工业设计", "摩擦对"],
   "working_keywords": ["摩擦力", "拉力", "推力", "冲击力", "电磁力", "万有引力", "nasty", "干摩擦", "润滑", "悬浮", "同摩擦对", "分子级别", "非固相"]
  },
  "notes": "概念批评式短文：只提出“应分开机制分别回答”，未给出机制分类与任何具体原理；P007 的“大概只有”等限定已保留。作者判断是否属领域共识登记为待外部核查，本文未给出处。无图片，正文与 lexical 一致（10 个段落节点）。"
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
