# -*- coding: utf-8 -*-
"""批次 r001-b0074 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0074.sessions.py            # 写 out/r001-b0074.out.jsonl
  python3 records/r001-b0074.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0074"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0074.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "36b37007": {
  "analysis": {
   "question_context": "提问者（自述初为人师两个月）问：被学生骂「傻 B」，哪里出了问题？作者没有直接评估该具体事件，而是借题提出一个一般性观念框架：先区分「出了不好的结果」与「真存在问题」，再据此判断该不该把某事当作问题来处理。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出要人先树立的观念：结果不好不必然意味着存在问题；很多「结果不好」只是只能接受的本来常态，不代表有人失职、做错或恶意操作。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "给出区分标准：要害不在发生的频率和常见程度，而在解决该事所需成本与收益能否相抵。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "以逐次追加投入降低故障率的算例说明边际收益递减，主张不如把最后三百万省下来做坏机回收，并把相抵处称为平衡点。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "结论：过了平衡点就应从「视为问题」转向「视为应该接受的常态」，因为不接受的危害更大。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "以教师、医生、知乎写作者为例并推及司机、军警、经营者，说明职业固有的伤害或损失不能以「绝对不能接受」的态度应对。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P014"], "summary": "限定：底线要先踩住，否则具体措施枉然；仍应努力降低概率、减轻程度，但这些措施须以「解决不了也罢」的态度处理。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "理由：抱「绝对不可接受」的态度会强化问题源的信心和权力；抱「不解决也可以接受」的态度会传递令对方气馁的信息，态度淡定则对方气焰消散，办法效力翻倍。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024"], "summary": "收束：先心硬如铁再谈技巧战术；以技巧弥补勇气者只是在挥舞白旗；心硬如铁即已定然赢，你决定赢就赢，战术技巧只决定受降形式。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "并不是出了不好的结果就一定存在问题；很多事情的「结果不好」是一种只能接受的本来常态，并不表示一定有人失职、做错或进行恶意操作。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "区分「只能接受的常态」与「有问题」的要害不在事情的频率和常见程度，而根本在于解决该事所需成本与收益是否可以相抵。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "以追加投入降故障率为例算账，作者认为不如把后三百万省下来搞坏机回收，「很可能」还便宜点。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "过了平衡点就应从「将其视为问题」转向「将其视为应该接受的常态」，因为不接受的危害更大。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教师生涯中的学生辱骂、行医生涯中的病人死亡、知乎上的被喷，以及司机的事故、军警的伤亡、经营者的投资失误，都不可以以「绝对不能接受」的态度来应对。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这条底线要先踩住，否则想什么具体措施都是枉然；仍要去降低概率和减轻程度，但这些措施首先都要以「解决不了也罢」的态度处理。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抱「这绝对不可接受」的态度去解决问题，会给予问题源至高无上的信心和权力，使其格外激烈地对抗；抱「其实我不解决也可以接受」的态度，遣词造句和姿势表情会自然传递出令对方气馁、消极的信息。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "办法未必有效，但态度淡定如铁会使对方气焰消散、问题源自己瘪下去，于是什么办法都自然会效力翻三倍。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要先心硬如铁，再谈技巧战术；想以优良技巧战术弥补自己找不着的勇气者，技巧战术本身只是挥舞白旗的舞蹈技巧。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "心硬如铁就已经定然赢了；你决定赢你就赢了，战术和技巧只是在决定以什么形式受降。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "先立观念：结果不好≠存在问题；「结果不好」可能只是只能接受的本来常态（P001-P003）。",
    "设问如何区分常态与问题（P004），答以成本与收益能否相抵，而非发生频率（P005）。",
    "以逐次投入降故障率的算例演示边际收益递减，得出平衡点（P006-P008）。",
    "由平衡点推出态度转向：过了平衡点即视为应接受的常态，因不接受危害更大（P009）。",
    "把该原则类推到教师、医生、知乎写作者、司机、军警、经营者（P010-P013）。",
    "让步与限定：仍要努力降低概率和程度，但须以「解决不了也罢」的态度处理（P014）。",
    "给出去恶化的机制解释：态度通过信心/气馁的信息传递影响问题源（P015-P017）。",
    "结论落到意志优先：先心硬如铁，技巧战术只决定受降形式（P018-P024）。"
   ],
   "concept_usage": [
    {"term": "问题（problem）", "meaning": "本文指需要归因于失职、做错或恶意并被要求消除的异常状态；作者以解决它的成本收益是否相抵来界定其边界。", "evidence": "P002", "ambiguity": "未说明成本与收益如何计量、由谁判断。"},
    {"term": "只能接受的本来常态", "meaning": "结果不好但无归因对象、且不接受的危害更大的状态。", "evidence": "P003", "ambiguity": "与「问题」的界线依赖成本收益判断，作者未给出判定主体与程序。"},
    {"term": "平衡点", "meaning": "继续投入解决问题的边际收益与成本相抵的位置；过此点应转为接受常态。", "evidence": "P008", "ambiguity": "以算例示意，未给出一般化的确定方法。"},
    {"term": "问题源", "meaning": "造成该不好结果、与之搏斗的对象（含人或事）。", "evidence": "P015", "ambiguity": "作者将问题源拟人化，未区分人事与物理故障。"},
    {"term": "心硬如铁", "meaning": "先具备「解决不了也罢」的底线态度，而非具体技巧。", "evidence": "P020", "ambiguity": "与不作为、摆烂的界线仅由P014「仍要努力降低概率和减轻程度」间接区分。"}
   ],
   "examples_and_targets": [
    "投入100万把故障率从20%降到10%、再投100万降到7%、再到6%、再到破产（P006）：作者举的说明性算例，未标注数据来源。",
    "把后300万省下来搞坏机回收（P007）：作者提出的替代方案。",
    "教师被学生骂、医生遇到病人死亡、知乎写东西被喷（P010-P012）：作者列举的同类场景。",
    "事故之于司机、伤亡之于军警、投资失误之于经营者（P013）：作者类推的场景。",
    "提问者「初为人师两个月被学生骂」的具体事件（Q001）：属提问者说法，作者未逐案评估。",
    "「你是磐石，对方就是蒲草」、白旗与受降（P019、P021、P022、P024）：作者使用的比喻与修辞材料。"
   ],
   "conditions": [
    "以「在漫长的教师生涯中」「如果有学生骂你你就受不了的话」等长期职业与条件句表述适用范围（P010-P012）。",
    "只有在「过了这个平衡点」之后才转向接受常态（P009）。",
    "接受常态不等于放弃措施：仍要努力降低概率、减轻程度，只是态度上以「解决不了也罢」处理（P014）。",
    "作者未说明成本收益如何计量、平衡点由谁判定、以及「失职或恶意」如何与常态区分。"
   ],
   "rhetoric_and_tone": "训诫式短论。第二人称「你」直陈，多用断言与格言短句（「你是磐石，对方就是蒲草」「心硬如铁，你已经定然赢了」）；以教师/医生/知乎/司机/军警/经营者构成排比；把「问题源」拟人化为「兴致勃勃、跃跃欲试」的搏斗者；用反问「岂有白旗宗师大获全胜的道理？」；结尾以受降的战争隐喻收束。",
   "unresolved_questions": [
    "成本与收益如何计量、由谁判断、平衡点如何确定，正文未说明。",
    "「只能接受的常态」与「失职/恶意」在具体案例（如学生辱骂初任教师）中如何划界，正文未逐案说明。",
    "提问者所处情境（初为人师两个月、被学生骂）是否含制度或管理问题，作者未评估。",
    "结尾「你决定赢，你就赢了」是断言还是修辞夸张，正文未加限定。",
    "P006的投入产出算例未标注数据来源，属说明性举例而非经验证据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "并不是出了不好的结果，就一定存在着问题（problem）。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "很多事情的“结果不好”是一种只能接受的本来常态，并不表示一定在什么地方有人失职、做错或者进行恶意操作。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "要害并不在于这事发生的频率和常见程度，而根本的在于解决这事所需要花的成本和收益是否可以相抵。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "你不如选择把这后300万省下来搞坏机回收，很可能还便宜点。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "过了这个平衡点，就要从“将其视为问题”转向“将其视为应该接受的常态”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "如果有学生骂你你就受不了的话，你是做不了教师这一行的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "都是不可以以“绝对不能接受”的态度来应对的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "但是这些措施首先都要以一种“解决不了也罢”的态度去处理。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "因为你本身就给了这些“问题源”至高无上的信心和权力。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "你的遣词造句、姿势表情会自然而然的传递出一种让对方莫名气馁、消极的信息。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "因为你的态度淡定如铁，对方的气焰就消散了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "先心硬如铁，再谈技巧战术。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "技巧、战术本身就只是挥舞白旗的舞蹈技巧罢了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "心硬如铁，你已经定然赢了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "你决定赢，你就赢了，战术和技巧只是在决定以什么形式受降。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教师职业与教育现场", "心态与自我调适", "风险/成本收益权衡"],
   "issue_candidates": ["初任教师被学生辱骂后的应对", "如何区分「问题」与「只能接受的常态」", "解决问题的成本收益平衡点", "面对问题源的态度如何影响结果"],
   "text_function_candidates": ["答疑", "经验总结", "训诫劝勉"],
   "object_candidates": ["初为人师的提问者", "学生", "教师", "医生", "知乎写作者", "司机", "军警", "经营者"],
   "working_keywords": ["problem", "平衡点", "只能接受的常态", "解决不了也罢", "问题源", "心硬如铁", "受降"]
  },
  "notes": "无图片节点；正文与lexical结构一致（24段）。作者未直接评估提问者的具体处境，只给出一般性原则。P006的投入产出算例未标注来源，属说明性举例；P015-P017对「问题源」的拟人化描述为修辞性解释，非经验研究结论。status=read，full_text_checked=true。"
 },
 "75d0b07c": {
  "analysis": {
   "question_context": "提问者问：32岁一事无成，如何改变自己颓废的状态？作者没有直接给行动清单，而是重构问题：把「一事无成」解释为「事」的标准被定得过高，进而提出人唯一需要追求的事业是「不以恶为业」，并界定其含义、边界与两种反面形态。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "判断「三十几岁一事无成」一般源于把「事」定义得过高；这与其说是客观的自我判定，不如说是一种认知自我的方法在三十岁无以为继。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "说明标准如何被抬高：十几二十几岁时自己、父母、外界都强调你微不足道、要奋进；于是要全球震惊、天下瞩目、百十号人或财务自由才算略有小成，未达这百分之八九十的人都达不到的标准就算「一事无成」。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "抱着这种成事观想不颓废很难；许多「成就」远在其上的人也在苦恼自己一事无成、颓废、无能与迷茫。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012"], "summary": "提出人一生应追求的最大事业只有一条——不以恶为业；不需辉煌、万众瞩目、家财万贯、公侯万代；仅此一条已需极大忍耐、勇气与智慧，超过出人头地的伟业。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "理由：单单不以恶为业地活着就是伟大成就，足以在任何权贵面前不必自卑，秦皇汉武唐宗宋祖也不足以凌驾其上；若能帮一两个人也过上这样的生活，便已到达事业顶峰。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018"], "summary": "限定：存在高于该层级的成就，但不应列入志在必得的努力目标，而应视为「得之我幸、不得我命」的赐予；否则要看你得几轮抑郁症才改得过来，改过来才算做好承接赏赐的准备。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "界定：不以恶为业不是「不为恶」；人类没有准确分辨善恶的能力，一直在有意无意作恶，这是解决不了的永恒困境，所以标准退守到别拿罪恶当事业。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024"], "summary": "边界情形：被迫靠明知伤害别人的营生糊口者，只要时刻留意减少和停止的机会、锻炼获取机会的能力，并以此为羞为耻、想着停下，就算在遵行不以恶为业。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "再度界定：不以恶为业指行为、努力、态度而非具体状态；不得不寄身黑社会但不甘不愿者仍可有效遵行，并因此与乐得以恶为业的同僚成为两类人，如同南北相向途中短暂交汇。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P029"], "summary": "行动建议：不要忧虑现在能否完全靠善良行为活着，要忧虑有没有为此不安、有没有切实努力、明天有没有比今天不得不作的恶少一点。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034"], "summary": "区分以恶为业的两种形式：羡慕以恶为业者的收益并恨自己无能；拒绝观察反思自身恶的成分、自认正义；并判定后者更危险，是人一步步下滑的真实机制，会创造出坚固的邪恶。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039"], "summary": "结论：不以恶为业不是现状问题（现状极大依赖起点），而是坚持往何处去、成色多大的问题；不看海拔高度只看推力方向；向上飞者为天使，向下扑者为恶魔；天堂地狱只在一念之间。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "三十几岁「一事无成」，一般是因为把「事」定义得比较高。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「一事无成」与其说是客观的自我判定，不如说是一种一贯的认知自我的方法在三十岁无以为继了。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被抬高的成事标准（全球震惊、天下瞩目、百十号人、财务自由）是百分之八九十的人都达不到的，未达标就被算作「一事无成」。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抱着这种成事观，想不颓废是很难的；许多成就远在其上的人也在苦恼自己一事无成、颓废、无能与迷茫。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人一生应该追求的最大事业只有一条，就是不以恶为业；不需要辉煌、万众瞩目、家财万贯或公侯万代。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "仅「不以恶为业」这一条就已需要极大的忍耐、勇气和智慧，远远超过出人头地、公侯万代的伟业。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "单单不以恶为业地活着就是伟大成就，足以在任何权贵面前不必自卑；若能帮一两个人也过上这样的生活，就已到达一个人所能追求的事业顶峰。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "高于该层级的成就存在，但不应列入志在必得的努力目标，而应视为「得之我幸、不得我命」的赐予。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若把「得不到就是我无能」当作努力目标而改不过来，作者以「得一轮抑郁症改不改得过来、得两轮够不够」作为后果设问；改过来才算做好承接赏赐的准备，否则成就是诅咒。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「不以恶为业」不是说「不为恶」，因为人类没有准确分辨善恶的能力、一直在有意无意作恶，这是解决不了的永恒困境，所以标准退守到别拿罪恶当事业。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若因某种原因必须靠明知伤害别人的营生活命，只要时刻留意减少和停止的机会、锻炼抓住机会的能力，并以此为羞为耻、想着停下，就已经算是不以恶为业。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不以恶为业不是指一种具体的状态，而是指一种行为、一种努力、一种态度；不得不寄身黑社会但不甘不愿者仍可有效遵行该原则。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以恶为业有两种形式：羡慕以恶为业者的收益并怨恨自己没胆量；拒绝观察反思自身恶的成分、自认处在完美善良状态。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两种形态中后者更危险，因为它才是人一步步往下滑的真实机制，会创造出残暴不可言、坚固刚硬无比的邪恶。", "evidence": ["E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不以恶为业不是现状问题（现状极大依赖起点），而是坚持往何处去、这坚持有多大成色的问题；不看海拔高度，只看推力方向。", "evidence": ["E26", "E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从地狱里拼命向上飞的哪怕没飞起来也是天使，从天堂里往下扑的哪怕身披圣光亦为恶魔；天堂地狱并不遥远，只在一念之间。", "evidence": ["E28", "E29", "E30"]},
    {"claim_id": "C017", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问：32岁一事无成，如何改变自己颓废的状态？（属提问者说法，作者未按此框架作答，而是重构了「一事无成」与「事业」的含义。）", "evidence": []}
   ],
   "argument_steps": [
    "先重构提问前提：「一事无成」源于把「事」定义得过高（P001）。",
    "把它改述为认知自我方法在三十岁失效，而非客观判定（P002）。",
    "追溯标准的来源：十几二十几岁时外界的「你微不足道、要奋进」（P003-P005）。",
    "指出后果：抱此成事观难以不颓废，连成就更高者也在自我否定（P006-P007）。",
    "提出替代答案：唯一需要追求的事业是不以恶为业（P008-P012）。",
    "给出理由：仅此一条即伟大成就，胜过权贵与帝王（P013-P015）。",
    "设限：更高成就存在，但只能当作赐予而非努力目标（P016-P018）。",
    "界定概念：不以恶为业≠不为恶，因人类无法准确分辨善恶（P019-P022）。",
    "处理边界情形：被迫为恶者的努力与羞耻心也算遵行（P023-P024）。",
    "再界定为行为/努力/态度，并以黑社会成员为例（P025-P028）。",
    "给行动建议：忧虑不安、努力与明天的恶是否少一点（P029）。",
    "区分两种以恶为业，指出自认正义者更危险（P030-P034）。",
    "结论：不看现状海拔只看推力方向，念头之间即天堂地狱（P035-P039）。"
   ],
   "concept_usage": [
    {"term": "「事」/成事观", "meaning": "本文指被外界抬高的成就门槛（全球震惊、天下瞩目、百十号人、财务自由），未达标即被判为一事无成。", "evidence": "P004", "ambiguity": "作者未给出「事」的正面定义，只以反例与「不以恶为业」对照。"},
    {"term": "不以恶为业", "meaning": "别拿罪恶当事业；是一种行为、努力、态度，而非具体状态或现状。", "evidence": "P022", "ambiguity": "作者明确否认它等于「不为恶」（P020），但未给出「恶」的判定标准。"},
    {"term": "以恶为业（两种形式）", "meaning": "一是羡慕以恶为业者的收益并恨自己无能；二是拒绝观察反思自身恶的成分并自认正义。", "evidence": "P031", "ambiguity": "第二种的判定标准未说明，作者称其更危险。"},
    {"term": "颓废", "meaning": "该词见于提问者问题与作者对他人心态的复述（ta们也觉得自己颓废），本文未把它当作作者自设术语。", "evidence": "P007", "ambiguity": "作者未定义颓废，也未按提问者的因果框架作答。"},
    {"term": "推力方向 / 海拔高度", "meaning": "作者用以比喻评判标准：不看现状起点的高低，只看努力或坚持的方向。", "evidence": "P036", "ambiguity": "比喻性用法，「方向」如何判定未给出操作性标准。"},
    {"term": "天使 / 恶魔", "meaning": "作者以向上的努力与向下的堕落标示两类人生，与出身起点无关。", "evidence": "P037", "ambiguity": "修辞性二元划分，未处理中间状态。"}
   ],
   "examples_and_targets": [
    "提问者「32岁、颓废、一事无成」的处境（Q001）：属提问者说法，作者未直接评估其个人情况。",
    "全球震惊、天下瞩目、手下百十号人的小局面、财务自由（P004）：作者列举的被抬高标准。",
    "「人间失格」「生而为人，对不起」（P005）：作者化用的流行语句，作讽刺性修辞，未标注出处。",
    "成就远在你之上却仍苦恼一事无成的人（P006-P007）：作者用作对比的泛称对象。",
    "秦皇汉武、唐宗宋祖、帝王将相（P013、P015）：作者用作对比的历史人物，属修辞性材料。",
    "抑郁症（P017）：作者用作条件性后果预测，非医学论断。",
    "黑社会成员（P023-P027）：作者用作「不以恶为业可与非状态化遵行」的例证。",
    "南北相向途中交汇的行路比喻（P028）：作者类比。",
    "天堂/地狱、天使/恶魔、背对阳光与仰面向上（P037-P038）：作者修辞材料。"
   ],
   "conditions": [
    "对象条件：讨论对象为「三十几岁」者，问题出自32岁的提问者（P001、Q001）。",
    "成因条件：标准被抬高发生于「在十几岁二十几岁的时候，自己也罢、父母也罢、外界也罢」（P003）。",
    "反事实条件：若把高于「不以恶为业」的成就当作志在必得的目标而改不过来，作者以「得一轮抑郁症改不改得过来」设问（P017）。",
    "例外情形：因命运没有选择、不得不寄身于伤害他人的营生者，仍算遵行不以恶为业（P023、P026）。",
    "前提：人类没有准确分辨善恶的能力，故标准只能是「不以恶为业」而非「不为恶」（P021）。",
    "作者未说明「恶」的判定标准、努力是否足够的尺度，以及「正确方向」如何认定。"
   ],
   "rhetoric_and_tone": "劝慰与训诫混合的短论。第二人称「你」与第三人称「ta们」交替；多用格言式短句收束（「不以恶为业，是不看海拔高度，只看推力方向的」）；带讽刺（「多么『废物』的标准啊，简直人间失格，生而为人，对不起啊」）；以反问推进（「其实，人一生应该追求的最大事业是什么呢？」「有没有高于这个层级的成就可言呢？」）；善用对比与比喻（天堂/地狱、天使/恶魔、南北相向）；结尾三句层层收束于「其实只在一念之间」。",
   "unresolved_questions": [
    "「恶」的判定标准与「人类没有准确分辨善恶的能力」这一前提如何补救，正文未说明。",
    "「不以恶为业」中「业」的范围（职业、事业还是行为习惯）未明确界定。",
    "作者对提问者个人处境（32岁、颓废）未作具体评估，只给出概念重构与一般原则。",
    "「得之我幸、不得我命」的赐予观与P023「不断获取更大的抓住这类机会的能力」之间是否存在张力，正文未说明。",
    "P005化用的「人间失格」「生而为人，对不起」未标注出处，是否为引文无法从语料判定。",
    "全文以断言与比喻为主，未提供经验证据或数据；P017的抑郁症说法属条件性预测。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "三十几岁“一事无成”，一般是因为把“事”定义得比较高", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不如说是一种一贯的认知自我的方法在三十岁无以为继了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "一定要做到全球震惊、天下瞩目，才算略有小成", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "没超出这个百分之八九十的人都达不到的标准，就不算“事”，就算“一事无成”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "只要你抱着这个成事观，你想不颓废是很难的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "ta们也觉得自己颓废，而且无能和迷茫，也“一事无成”着呢。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "其实只有一条，就是不以恶为业。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "不以恶为业，就是一个人唯一需要追求的事业了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "因为就这一条，就已经需要极大的忍耐、极大的勇气、极大的智慧了", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "单单只是活着，不以恶为业的活着，就是伟大成就", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "哪怕只有一个也罢，你都已经到达了一个人所能追求的事业顶峰了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "有没有高于这个层级的成就可言呢？当然有。但是，那并不应该列入一个人志在必得的努力目标。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "那就看你得一轮抑郁症你改不改得过来", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "到那时那些成就赐给你才不构成一种诅咒。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "这不是说“不为恶”——大家现实一点，这是不可能办到的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "人类没有准确的分辨善恶的能力，因此其实一直都在有意无意的作恶，这一点是解决不了的永恒的困境。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "所以，这个标准才退守到了“不以恶为业”——别拿罪恶当事业。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "锻炼自身，不断获取更大的抓住这类机会的能力，你就已经算是不以恶为业。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P024", "quote": "但只要你以此为羞、为耻，想着停下、努力谋求停下，你已经算是在遵行“不以恶为业”。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P025", "quote": "不以恶为业，不是指一种具体的状态，而是指一种行为、一种努力、一种态度。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P026", "quote": "一个人可以同时既身为黑社会，但是仍然有效的遵行不以恶为业的原则", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P031", "quote": "第一种，是羡慕那些以恶为业的人的丰厚收益，怨恨自己没有做恶的胆量和能力", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P032", "quote": "第二种，是拒绝观察和反思自己现状中恶的成分，主张自己现在处在完美的善良状态", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P033", "quote": "而且，这两种心态之中，后者更加危险——因为它才是人一步步往下滑的真实机制。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P034", "quote": "恰恰是这种“自信”的自我开脱、自认正义的心态，才会创造出残暴不可言、而且坚固刚硬无比的邪恶。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P035", "quote": "不以恶为业，不是一个现状问题", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P036", "quote": "不以恶为业，是不看海拔高度，只看推力方向的。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P037", "quote": "从地狱里拼命向上飞的，哪怕没能飞起来，也是天使；从天堂里往下扑的，哪怕身披圣光，亦为恶魔。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P038", "quote": "天堂和地狱并没有天地之遥——背对阳光，即入地狱，仰面向上，即至天堂。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P039", "quote": "其实只在一念之间。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲学/伦理", "自我认知与评价", "职业与成就观"],
   "issue_candidates": ["三十几岁「一事无成」的自我判定", "成事标准被抬高", "不以恶为业的含义与边界", "以恶为业的两种形式", "现状与努力方向的区分"],
   "text_function_candidates": ["答疑", "劝慰", "训诫", "概念界定"],
   "object_candidates": ["提问者（32岁）", "秦皇汉武", "唐宗宋祖", "帝王将相", "黑社会成员", "权贵"],
   "working_keywords": ["不以恶为业", "为恶", "成事观", "颓废", "得之我幸、不得我命", "推力方向", "一念之间"]
  },
  "notes": "无图片节点；正文与lexical结构一致（39段）。作者未直接评估提问者个人处境，而是重构问题。P005「人间失格」「生而为人，对不起」为化用的流行语句，原文未标出处，是否为引文待核。P017以抑郁症作条件性后果设问，属修辞性预测而非医学论断。全文无比喻以外的经验证据。status=read，full_text_checked=true。"
 },
 "c4bab8ec": {
  "analysis": {
   "question_context": "提问者问「强基计划最终会如何收场」。作者开头即声明借该问题谈人生前途选择的一般方法，未就政策本身作答；正文依次评从众流、先知流、稳健流，再转入基础学科选择、中国科研体系与外部技术竞争的评论。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "声明借题谈前途选择，列出A从众流、B先知流、C稳健流三个流行策略，称逐个看优缺点。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008"], "summary": "从众流最好操作、决策后有最好的心理体验（错也不是唯一错的、不缺同路人），这是其最大甚至唯一福利。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "真正从众门槛高，需购买统计调查宏观研究报告；自称从众的学生家长极少花过这笔钱。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014"], "summary": "「从众流」本质不是从众而是「从村」：被动定居信息村，交出家人命运以换取日后的「乡谊」。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "村子即世界的时代已永远过去，各类圈子都不会陪你走完命运选择的周期，「从村流」历史性破产。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "照「都说」去选等于拿命宣誓加入村子，无真理性，唯一福利的辩护与肯定承诺也无真实性。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024"], "summary": "先知流是自己关注趋势、自己找资料下结论下注；别人说法只是「开题」引子而非结论；你下注你买单。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "限定：无人能真正赌中未来；真正的选择是自己选还是让别人选；两者成败几率一样，差别只在多赢「自己下注」本身。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031", "P032", "P033"], "summary": "真正有实质影响的是稳健流：选不会被淘汰的基础学科；万变不离其宗，永远不错的是万变；迎历史潮流之「宗」最优。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038"], "summary": "专业定位应晚至研究生/博士阶段、职业上换第二份工作时；早于此冒极大风险；作者不认为低于35岁能有效选择命运。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "反驳「有钱人的孩子不会学基础学科」：恰相反，权贵孩子大批学所谓无用专业，工科医科计算机对上层属不务正业，热门应用工科是中下层中产执念。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P046", "P047", "P048"], "summary": "中国要改变科研体系与美国硬碰硬竞争，需最硬基础领域分庭抗礼；战略需求、钱与市场倾斜政策都不成问题。", "role": "context"},
    {"unit_id": "U013", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "反驳看空强基计划者「未来二十年与过去一样」的思路；预测重点单位将一抢而空，硬攻坚领域会成为待遇最好、资源最多的前排座位。", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062"], "summary": "名校读什么专业不重要；君子不器，本科以通识教育为主；本科生选基础学科更有意义，面向找工作选专业可笑。", "role": "claim"},
    {"unit_id": "U015", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067"], "summary": "人生常识：尖酸刻薄的人说的话不要听；不是悲观预期不要听而是尖酸刻薄不要听；嬉笑怒骂式表达已远离客观范围。", "role": "action_advice"},
    {"unit_id": "U016", "paragraph_refs": ["P068", "P069", "P070", "P071"], "summary": "针对冷嘲热讽与「程序员前景灰暗」之说，指出程序员们普遍认为软件赚钱不靠程序员，反问谁对。", "role": "rebuttal"},
    {"unit_id": "U017", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076"], "summary": "中国科研问题「大却还不够大」；未到不能忍受时常得到「继续忍」；作者称知识分子应会感谢川普给了「无可忍」。", "role": "reason"},
    {"unit_id": "U018", "paragraph_refs": ["P077", "P078", "P079", "P080", "P081"], "summary": "限定与预测：背水一战不等于不会挫折与代价；预料出现骗补、失败与一代人补课，但中国不会回头。", "role": "qualification"},
    {"unit_id": "U019", "paragraph_refs": ["P082", "P083", "P084", "P085", "P086", "P087"], "summary": "结论：这是救亡图存；只有自己搞出来封锁才会从内部崩溃；接下来说是好大一轮千金买马骨与迁木立信，以设问收尾。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者借「强基计划」问题谈人生前途选择，归纳出从众流、先知流、稳健流三个流行策略。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从众流最好操作且决策后有最好的心理体验，能带来极大的心理安慰；这是其最大的、甚至是唯一的福利。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的从众门槛极高，需购买统计调查宏观研究报告；自称按主流意见决策的学生或家长极少花过这笔钱。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「从众流」最要害处是ta们根本没在从众，本质上是在「从村」——把命运交给信息村村民以换取「乡谊」。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「村子即世界」的时代已永远过去，没有哪组村民会陪你走完命运选择的生命周期；「从村流」已经历史性的破产了。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "照「都说」去选等于拿自己的命宣誓加入ta们的村子，没有真实可靠的真理性，「被承诺辩护和肯定」也毫无真实性。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用前途命运去换一个不存在、自己幻想出来的「福利」，是作者想不到更甚的愚蠢。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "先知流是自己长期关注趋势、自己找资料下结论下注；别人的说法只是「开题」的引子，不能表示结论。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有人能真正赌中未来；真正的选择不是选哪种命运选项，而是选择自己选还是让别人选。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自己选和别人选的成败几率本质上一样（哪怕别人是马云、比尔盖茨）；多赢的只是「自己下注」本身，赌局输赢未受实质影响。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正有实质影响的是稳健流：选不会被淘汰的基础学科；万变不离其宗，真正永远不错的是万变。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在诸「宗」中向自己所下注的历史潮流倾斜，去选能迎历史之潮而上的「宗」，是最优选择。", "evidence": ["E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "确切专业定位应属研究生甚至博士阶段、职业上换第二份工作时的事；早于此节点做定位，无论自认多热门都在冒极大风险。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不认为低于35岁的人可以实际有效地选择自己的命运。", "evidence": ["E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反驳「有钱人的孩子不会学基础学科」：权贵孩子恰恰大批学这类被视作无用的专业，工科医科计算机对上层阶级属不务正业，热门应用工科才是中下层中产的执念。", "evidence": ["E25", "E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国要大面积改变科研体系，与美国在每一领域硬碰硬竞争，需最硬基础领域的分庭抗礼；战略需求、钱与市场倾斜政策都不成问题。", "evidence": ["E27", "E28"]},
    {"claim_id": "C017", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的观点：很多人看不上强基计划、喊它「骗人入坑」，也不相信中国科研系统可能有什么改观；作者把其思路归为「参考过去二十年的经验数据，认定未来二十年必定完全一样」。", "evidence": ["E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问「谁说未来二十年和过去二十年一样」，并以「肉眼可见的不再会一样了」否定该推断。", "evidence": ["E30"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者估计过几年重点单位会把强基计划人才一抢而空且直奔关键领域；预计硬攻坚领域将成为待遇最好、职业最稳定、最好拿到资源的前排座位。", "evidence": ["E31", "E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对第一流名校而言读什么专业根本不重要（跨专业就业是常态）；君子不器，人不是被本科专业定义的。", "evidence": ["E33", "E34"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对本科生而言选基础学科远比选应用学科有意义；「面向找工作」选本科专业可笑，因为企业要的是名校出身，赌的是综合底蕴和长期潜力。", "evidence": ["E35", "E36"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人生常识：说话尖酸刻薄的人说的话不要听；不是预期悲观的话不要听（恰恰相反要多听），而是【尖酸刻薄】的话不要听。", "evidence": ["E37", "E38"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用嬉笑怒骂、尖酸刻薄方式表达不看好时，看法已远离客观范围；与其说ta客观看到不行，不如说ta希望它不行——希望与事实关系甚小，与私人情绪关系甚大。", "evidence": ["E39", "E40"]},
    {"claim_id": "C024", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者转述并反驳的说法：无数人冷嘲热讽，笃定「基础学科没前途」、当程序员实惠，并称中国程序员前景一片灰暗；作者则以程序员们普遍认为软件赚钱不靠程序员作回应。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国科研确有很多问题，但要害在于「大却还不够大」；没大到不能忍受时答案常是「继续忍」，只有忍无可忍的威胁才带来付出试错成本的合法性。", "evidence": ["E44", "E45"]},
    {"claim_id": "C026", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者说未来几年科技工作者和知识分子应会感谢川普给了想躲都躲不掉的「无可忍」；同时限定这绝不是说背水一战就不会笨拙、挫折、不付出大量代价。", "evidence": ["E46", "E47"]},
    {"claim_id": "C027", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者预料接下来会出现大量骗补、假项目、夭折、失败，以及整整一代人的「补缴学费」和「补课」。", "evidence": ["E48"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使如此中国不会回头，唯一出路仍是向前；这不是天下争霸，而是救亡图存。", "evidence": ["E49", "E50"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有自己搞出来并展现「必然要搞出来」的决心与事实，封锁才会从内部出现崩溃。", "evidence": ["E51"]},
    {"claim_id": "C030", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者按惯例预测接下来是好大一轮「千金买马骨」和「迁木立信」，并以「要买谁的马骨? 立谁的信？」设问收尾，未给出答案。", "evidence": ["E52", "E53"]},
    {"claim_id": "C031", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问「强基计划最终会如何收场」；作者未就政策本身逐项作答（属提问者问题，非作者主张）。", "evidence": []}
   ],
   "argument_steps": [
    "声明借题发挥并列出三种策略（P001-P006）。",
    "从众流的福利是心理安慰与同路人（P007-P008）；指出真正从众门槛高（P010-P013）。",
    "重命名为「从村流」，指其交出命运换乡谊（P014）。",
    "以村子即世界已过去论证从村流历史性破产（P015-P019），判定其愚蠢（P020-P021）。",
    "评先知流：自己判断下注（P022-P024）；限定无人能赌中未来、真正的选择是自己选还是别人选、成败几率相同（P025-P029）。",
    "转向稳健流：选基础学科与迎历史潮流之「宗」（P030-P033）。",
    "给出时间条件：专业定位应晚至研究生/换第二份工作，低于35岁难以有效选择命运（P034-P038）。",
    "反驳「有钱人的孩子不学基础学科」（P039-P045）。",
    "转入中国情境：技术竞争与战略、资金、政策条件（P046-P048）。",
    "反驳看空强基计划者并反问未来二十年是否一样，预测人才被争抢（P049-P056）。",
    "论证名校本科专业不重要、本科以通识教育为主（P057-P062）。",
    "给言论取舍规则：不听尖酸刻薄之言（P063-P067）；以程序员自身看法反驳冷嘲热讽（P068-P071）。",
    "论证中国的问题「大却还不够大」，只有无可忍才带来改变成本（P072-P076）。",
    "限定并预测代价，结论落到救亡图存与封锁从内部崩溃（P077-P087）。"
   ],
   "concept_usage": [
    {"term": "从众流", "meaning": "按主流意见做人生决策的策略；作者区分真正的从众（需统计调查数据）与实为「从村」的自称从众。", "evidence": "P003", "ambiguity": "「主流意见」与「众」的量化门槛未给出。"},
    {"term": "从村流 / 信息村 / 乡谊", "meaning": "被动定居信息村、把自身与家人命运交给村民以换取日后「乡谊」；「村子」涵盖微博圈、朋友圈、同学圈等各类圈子。", "evidence": "P014", "ambiguity": "「村」的规模门槛与「乡谊」内容未界定。"},
    {"term": "先知流", "meaning": "自己长期关注未来趋势、自己找资料下结论、自己下赌注的策略。", "evidence": "P022", "ambiguity": "作者随即否认人能真正赌中未来，术语与其有效性存在张力。"},
    {"term": "稳健流", "meaning": "按「无论世界怎样发展都不会被淘汰」的法则做保守选择，典型为自然科学、文学、哲学、绘画、音乐理论等基础学科。", "evidence": "P031", "ambiguity": "基础学科清单边界与「不被淘汰」的判据未说明。"},
    {"term": "万变不离其宗 / 「宗」/ 万变", "meaning": "「宗」指不变的基础学科；作者称真正永远不错的是万变，并主张选迎历史之潮而上的「宗」。", "evidence": "P032", "ambiguity": "以悖论式修辞表述，未给出判定标准。"},
    {"term": "君子不器", "meaning": "作者引以说明人不应被本科专业定义。", "evidence": "P058", "ambiguity": "引用未标出处，属成语化用。"},
    {"term": "救亡图存", "meaning": "作者用以界定中美技术竞争的性质——不是天下争霸，而是无退路的生存问题。", "evidence": "P082", "ambiguity": "属作者判断，未提供论证。"},
    {"term": "尖酸刻薄", "meaning": "指以嬉笑怒骂方式表达不看好的言论，作者主张排除在参考之外。", "evidence": "P064", "ambiguity": "与「预期悲观」的区分仅按表达方式，标准未给出。"},
    {"term": "强基计划", "meaning": "问题所问的中国基础学科招生培养计划；作者只使用该词，未介绍政策内容。", "evidence": "P049", "ambiguity": "未说明具体条款，判断建立在一般趋势推断上。"}
   ],
   "examples_and_targets": [
    "统计调查宏观研究报告价格表（P011，紧邻IMG001）：作者用作「真正从众门槛高」的材料；图片内容未核验。",
    "微博圈、朋友圈、同学圈、同事圈、家族圈、邻居圈、豆瓣圈、知乎圈（P017）：作者列举的各种「村子」。",
    "马云、比尔盖茨（P026）：作者用作「别人」的极端例子。",
    "自然科学、文学、哲学、绘画、音乐理论（P031）；哲学、文学、人类学、政治学、经济学、伦理学、法学、数学、艺术、神学（P041）；工程学/医学/计算机（P042）：作者列举的专业。",
    "伊顿公学、哈罗公学（P043）：作者建议读者自行打听，属待外部核查的断言。",
    "钱学森及其时代GDP（P055）：作者用以回应「担心默默奉献」。",
    "学物理搞量化交易、学生物搞计算机、学中文搞新闻、学哲学搞企业管理（P057）；北大考古专业与企业高管培养路线（P061）：作者举例。",
    "5G、芯片制造、生物科技、航空航天、材料科学（P047）；十月份近十万亿人民币投入芯片全产业链研发（P056）：作者的事实/数据断言，待外部核查。",
    "川普（P048、P075）：作者视为外部压力来源。",
    "千金买马骨、迁木立信（P086）：作者引用的典故作收尾修辞。",
    "看空强基计划者（P049）、冷嘲热讽者（P068）、担心成为钱学森的人（P055）：被作者反驳或转述的他人说法。"
   ],
   "conditions": [
    "适用对象：为自己或子女做专业与前途决策的学生与家长（P012、P062）。",
    "时间条件：近代以前／最近一百多年／落到个人只有二十年（P015）；讨论范围为未来二十年（P050-P052）。",
    "年龄与阶段条件：作者称低于35岁不能实际有效选择命运（P037）；专业定位应在研究生、博士阶段或换第二份工作时（P034）。",
    "预测性限定语：「我估计过几年只怕完全是另一个景象」（P054）、「以我所见只怕是」（P056）、「意料之中会出现」（P078）、「按照惯例」（P086）。",
    "依赖前提：所下注的历史潮流判断成立（P033）；潮流判断错误时后果未说明。",
    "外部条件：封锁与卡脖子持续或加剧（P052、P085）。",
    "作者未说明「万变不离其宗」的判据、基础学科完整清单与「尖酸刻薄」的判定标准。"
   ],
   "rhetoric_and_tone": "长篇论辩体，第二人称「你们」直呼读者，反问诘问密集（「你们谁真的去『从』了？」「谁说未来二十年和过去二十年一样？」「人家不给你，你难道去死？」）；讽刺与训斥（「世界上的愚蠢，我竟想不到还有比此更甚的」）；重复强调（「『从村流』已经历史性的破产了——再重复一遍」）；战争与博弈隐喻（背水一战、救亡图存、下注、千金买马骨）；口语化短评穿插（「拜托」「好吗」「不要全凭想象」）；结尾设问不答。",
   "unresolved_questions": [
    "图片未核验，需人工/多模态复核：IMG001（//asset.sooon.ai/p/2020-09/26/a98a9eee8c8ec2191344c8d51d3f7393.jpg）内容不可见；P011「典型的基于统计调查的宏观研究报告价格表」紧邻该图，疑为其说明文字，但无法确认图中是否有价格数据。",
    "P069「感觉中国程序员前景一片灰暗，是这样吗？」被标为lexical未覆盖片段（text_lexical_divergence，char_start≈3839）；该句是否为引用他人说法无引号标记，归属需复核。",
    "P056「十月份近十万亿人民币准备放进芯片制造的全产业链研发」为待外部核查的事实断言，作者未给出出处。",
    "P043伊顿公学、哈罗公学毕业生去向为待外部核查的事实断言。",
    "P037「低于35岁的人可以实际有效的选择自己的命运」的判断依据未说明。",
    "作者未介绍强基计划的政策内容（P001声明借题发挥），提问者所问「最终会如何收场」未获直接回答，只有趋势性判断。",
    "lexical节点统计为paragraph:88、image:1，正文分段为87段，存在1处结构不一致（P069附近）。",
    "文中夹用英文词（如P044「fancy」、P055「gdp」）未加解释，是否为原文如此需核对。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "借这个问题说一下到底人要怎么选择自己的人生前途。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这一共有三个流行的策略：", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "从众流的好处，是最好操作，而且在决策后有最好的心理体验", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "甚至是唯一的福利。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "只有极少极少是真正的从众的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "花过哪怕一笔钱去购买这种最基本的数据报告？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "ta们本质上是在从村。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "“村子即世界”的时代已经永远的过去了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "“从村流”已经历史性的破产了", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "本质上不过是在拿自己的命宣誓加入ta们的村子", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "世界上的愚蠢，我竟想不到还有比此更甚的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "所谓先知流，就是自己长期关注未来的趋势动向。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "别人说好或者不好，只不过时一个“开题”的引子", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P025", "quote": "世界上没有人能真正的赌中未来，因为没有人是上帝。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "自己选和别人选的成败几率是一样的", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P027", "quote": "但你多赢了一次“自己下注”这件事本身。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P029", "quote": "赌局本身的输赢，并没有受到实质影响。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P030", "quote": "真正会有实质影响的，实际上是“稳健流”。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "这类作为一切其他学科的基础学科。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "真正永远不错的，是万变。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "去选择一个能迎历史之潮而上的“宗”，则是最优的选择。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P034", "quote": "在职业上应该是【换第二份工作时】决定的事。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P035", "quote": "你都是在冒极大的风险。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P037", "quote": "我不认为低于35岁的人可以实际有效的选择自己的命运。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P041", "quote": "在学哲学、文学、人类学、政治学、经济学、伦理学、法学、数学、艺术甚至神学", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P044", "quote": "只是中产阶级——而且还是中下层中产阶级——的执念好吗？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P047", "quote": "中国要大面积的改变原有的科研体系来和美国在每一个领域来一场硬碰硬的技术竞争", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P048", "quote": "现在的中国战略需求是不成问题的", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P049", "quote": "现在很多人看不上强基计划，喊着是“骗人入坑”", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P050", "quote": "问题是，谁说未来二十年和过去二十年一样？", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P054", "quote": "是大批拥有各种优先权的重点单位来一抢而空", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P056", "quote": "只怕是中国待遇最好、职业最稳定，最好拿到资源的前排座位", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P057", "quote": "对这些学校你读什么专业根本就不重要。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P058", "quote": "人不是被自己本科选的专业定义的", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P059", "quote": "对于本科生，选择基础学科专业远比选择应用学科专业更有意义。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P061", "quote": "企业要的是名校出身，赌的是综合底蕴和长期潜力。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P063", "quote": "说话尖酸刻薄的人，ta们说的话不要听。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P064", "quote": "是【尖酸刻薄】的话不要听。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P065", "quote": "ta的看法就已远离客观范围了。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P066", "quote": "而和人的私人情绪关系甚大。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P068", "quote": "无数人跑来冷嘲热讽，似乎万分笃定“基础学科没前途”", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P069", "quote": "感觉中国程序员前景一片灰暗，是这样吗？", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P070", "quote": "人家普遍觉得软件赚钱根本不靠程序员。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P073", "quote": "在于它们是大问题，但却还不够大", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P074", "quote": "它常常得到的答案是“继续忍”。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P075", "quote": "给了你们这个想躲都躲不掉的“无可忍”。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P077", "quote": "就不会笨拙、挫折、不会付出大量的代价。", "relation": "qualifies"},
    {"key": "E48", "paragraph_id": "P078", "quote": "接下来意料之中的会出现大量的骗补、假项目、夭折、失败……", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P080", "quote": "但是，即使是这样，中国不会回头的。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P082", "quote": "这其实是救亡图存。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P085", "quote": "封锁才会从内部出现崩溃。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P086", "quote": "是好大一轮“千金买马骨”和“迁木立信”。", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P087", "quote": "要买谁的马骨? 立谁的信？", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P052", "quote": "所有被卡脖子的东西，中国都需要人去攻坚", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育与升学选择", "科技政策与中美技术竞争", "人生决策方法论", "社会评论"],
   "issue_candidates": ["强基计划的前景", "人生前途的三种策略", "基础学科与应用学科的选择", "中国科研体系的改革", "对外部技术封锁的应对"],
   "text_function_candidates": ["答疑（声明借题发挥）", "论辩", "批评", "趋势预测"],
   "object_candidates": ["强基计划", "学生与家长", "权贵/上层阶级", "中产阶级", "伊顿公学", "哈罗公学", "川普", "钱学森", "马云", "比尔盖茨", "中国", "美国", "程序员"],
   "working_keywords": ["从众流", "从村流", "信息村", "乡谊", "先知流", "稳健流", "万变不离其宗", "君子不器", "救亡图存", "千金买马骨", "迁木立信", "尖酸刻薄"]
  },
  "status": "needs_reread",
  "full_text_checked": False,
  "image_checked": False,
  "notes": "本篇含1个图片节点 IMG001（//asset.sooon.ai/p/2020-09/26/a98a9eee8c8ec2191344c8d51d3f7393.jpg），图片内容未经核验，需图像核验；已读部分为正文文本，故 status=needs_reread、image_checked=false，并按系统提示词第5节将 full_text_checked 置为 false（有图片未核对不得标记完成）。P011「典型的基于统计调查的宏观研究报告价格表」紧邻该图，疑为其说明文字，但无法确认图中内容。lexical节点统计为 paragraph:88 / image:1，正文分段87段，存在1处 text_lexical_divergence：P069「感觉中国程序员前景一片灰暗，是这样吗？」为lexical未覆盖片段（char_start≈3839）。P043与P056为待外部核查的事实断言。"
 },
 "96126fae": {
  "analysis": {
   "question_context": "提问者列出综合格斗、跆拳道、散打、搏击、拳击、泰拳，问哪个适合女孩子。作者没有逐项比较这六种项目，而是先以「学来自卫防身还是学来锻炼身体」把问题一分为二，再按两种目的分别给出建议，并明确否定搏击用于自卫。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以目的设问切分问题：学自卫防身还是学锻炼身体。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "自卫防身应直奔女子自卫术、长跑和力量。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "自卫的优先级是敢于致伤失能的钢铁意志，其次体能和力量，最后才是招数；招数最简单直接，练几次就会。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P004", "P005"], "summary": "若为修养身心、强身健体（作者明确不算自卫技能），建议练精神性较强的东西，如弓道、剑道、跆拳道、合气道、太极拳。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "不推荐练搏击：搏击以打比赛为目标，未登堂入室则不适合自卫，且竞赛性强，与其说放松不如说是另一种焦虑。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P008", "P009"], "summary": "强身健体不宜好勇斗狠、不宜以击败他人为目的，应以在追求自己定义的完美中寻找和接受自我为基本样式——不是与人斗，而是与自己斗。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自卫防身应当直奔女子自卫术、长跑和力量。", "evidence": ["E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自卫首先重要的不是招数，而是敢于致伤失能的钢铁意志，其次是体能和力量，最后才是招数；招数一般最简单直接，练几次就会。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果是练来修养身心、强身健体，作者建议多练精神性比较强的东西，如弓道、剑道、跆拳道、合气道、太极拳；并明确这不能视为自卫技能。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不推荐练搏击：搏击总体上以打比赛为目标，不是练到登堂入室就不适合自卫；其目的性、竞赛性强，与其说是放松，不如说是另一种焦虑。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强身健体的东西不宜好勇斗狠、不宜以击败他人为目的，而应以在追求自己定义的完美过程中寻找和接受自我为基本样式。", "evidence": ["E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "练武的取向不是与人斗，而是与自己斗。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问：综合格斗、跆拳道、散打、搏击、拳击、泰拳，哪个适合女孩子？（属提问者问题；作者未逐项比较，只按目的二分作答。）", "evidence": []}
   ],
   "argument_steps": [
    "先以目的设问切分提问（P001）。",
    "就自卫防身给出方向：女子自卫术、长跑、力量（P002）。",
    "给出自卫的能力排序：意志>体能和力量>招数（P003）。",
    "就强身健体给出方向并列项目，且声明其不算自卫技能（P004-P005）。",
    "否定搏击用于自卫，理由是竞赛目标与焦虑属性（P006-P007）。",
    "结论：健身的取向应与自己斗而非与他人斗（P008-P009）。"
   ],
   "concept_usage": [
    {"term": "自卫/自卫技能", "meaning": "以防身制敌为目的的技能；作者称其核心是敢于致伤失能的意志而非招数，并明确把强身健体排除在自卫技能之外。", "evidence": "P003", "ambiguity": "未给出「致伤失能」的法律与伦理边界及训练方法。"},
    {"term": "招数", "meaning": "具体技术动作；作者称其最简单直接、练几次就会。", "evidence": "P003", "ambiguity": "未说明招数在实战中的具体作用。"},
    {"term": "精神性比较强的东西", "meaning": "作者用以指弓道、剑道、跆拳道、合气道、太极拳一类适合修养身心的项目。", "evidence": "P005", "ambiguity": "「精神性」的判据未定义。"},
    {"term": "搏击", "meaning": "以打比赛为目标的对抗项目；作者认为其不适合自卫，也不宜作放松。", "evidence": "P007", "ambiguity": "未界定与综合格斗、散打、拳击、泰拳的包含关系。"},
    {"term": "好勇斗狠", "meaning": "作者用以描述强身健体不宜采取的目的取向。", "evidence": "P008", "ambiguity": "未给出判定何种训练属于好勇斗狠的标准。"}
   ],
   "examples_and_targets": [
    "提问者列举的综合格斗、跆拳道、散打、搏击、拳击、泰拳（Q001）：属提问者选项，作者未逐项点评。",
    "女子自卫术、长跑、力量（P002）：作者建议。",
    "弓道、剑道、跆拳道、合气道、太极拳（P005）：作者建议。",
    "搏击（P006-P007）：作者不推荐的对象。",
    "「白痴练几次也会了」（P003）：作者使用的夸张修辞。"
   ],
   "conditions": [
    "以目的为条件：是学自卫防身，还是学锻炼身体（P001）。",
    "若为强身健体，作者明确「这不能视为自卫技能」（P004）。",
    "搏击只在「不是练到登堂入室」的条件下被认为不适合自卫（P007）。",
    "作者未说明为何要单列「女子」自卫术，也未说明性别差异的理由。",
    "作者未说明「钢铁意志」的训练方式与适用对象。"
   ],
   "rhetoric_and_tone": "短答式答疑。开门见山以二选一设问切分问题；判断直截（「不推荐练搏击」）；用极端化措辞（「白痴练几次也会了」）；结尾以对偶短句收束（「不是与人斗，而是与自己斗。」）。",
   "unresolved_questions": [
    "作者未说明「女子自卫术」具体指哪一套体系及其有效性依据。",
    "未解释为何在自卫场景下单列「女子」自卫术，性别差异的理由未说明。",
    "「敢于致伤失能的钢铁意志」如何训练、其法律与伦理边界如何，正文未说明。",
    "未逐项评价提问者列出的六种项目（综合格斗、散打、拳击、泰拳等），只给出对搏击类的总体判断。",
    "「精神性比较强」的判定标准未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这是要学来自卫防身，还是要学来锻炼身体？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "自卫防身直奔女子自卫术、长跑和力量。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "自卫首先重要的不是招数，而是敢于致伤失能的钢铁意志，其次是体能和力量，最后才是招数。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "招数一般都是最简单直接的招数，白痴练几次也会了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "注意这不能视为自卫技能", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P005", "quote": "比如弓道、剑道、跆拳道、合气道、太极拳。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "不推荐练搏击。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "搏击总体上还是以打比赛为目标的，不是练到登堂入室，不适合自卫。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "与其说是一种放松，还不如说是另一种焦虑。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "强身健体的东西不宜好勇斗狠，不宜以击败他人为目的", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "不是与人斗，而是与自己斗。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["武术/格斗训练", "个人安全与防身", "健身与身心修养"],
   "issue_candidates": ["女性防身项目的选择", "自卫中意志、体能、招数的优先级", "搏击是否适合自卫", "强身健体的目的取向"],
   "text_function_candidates": ["答疑", "建议", "评论"],
   "object_candidates": ["女孩子", "综合格斗", "跆拳道", "散打", "搏击", "拳击", "泰拳", "女子自卫术", "弓道", "剑道", "合气道", "太极拳"],
   "working_keywords": ["自卫防身", "致伤失能", "钢铁意志", "招数", "精神性", "好勇斗狠", "与自己斗"]
  },
  "notes": "无图片节点；正文与lexical结构一致（9段）。作者未逐项点评提问者列出的六种项目，只按「自卫/健身」两种目的作答。P003「致伤失能」的法律与训练边界未说明。status=read，full_text_checked=true。"
 },
 "034b5293": {
  "analysis": {
   "question_context": "提问者问两件事：人对世界的认识是否会受母语限制和影响，以及语言能否影响思想。作者以「当然会」直接肯定，并进而主张要做严肃思考基本必须学一门与母语不同源的语言。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接肯定母语会影响对世界的认识，并给出建议：要做严肃有价值的思考，基本必须学一门与母语不同源的语言。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "语言是思想的载体，在最深处甚至无法翻译。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "举 normal/普通、free/自由、moral/道德、爱/love 为例，说明元概念无法翻译构成文化鸿沟。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007"], "summary": "因底层概念的根本差别，英文与其中文译文之间存在很难说清的错位，常常南辕北辙，甚至造成不知自己在说什么、想什么的心脑分离。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008"], "summary": "结论：语言能力不好是致命的缺陷、思想的绝症，是必须解决的问题，不要有任何侥幸。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对世界的认识当然会受母语的限制和影响。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果打算做点严肃的有价值的思考，基本上必须要学一门与母语不同源的语言。", "evidence": ["E1"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "语言是思想的载体，在最深处甚至是无法翻译的。", "evidence": ["E2"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多元概念的无法翻译是文化之间难以跨越的鸿沟，作者以 normal、free、moral、爱/love 为例。", "evidence": ["E3", "E4", "E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为这些底层概念上的根本差别，一篇英文和它的中文译文之间存在着很难说得清的错位，常常南辕北辙。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "译文的错位甚至经常造成人们不知道自己在说什么、在想什么的一种奇异的心脑分离。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "语言能力不好是一种致命的缺陷、思想的绝症，是必须解决掉的问题，对这一点不要有任何侥幸。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问：人对世界的认识会受到自己母语的限制和影响吗？语言可以影响我们的思想吗？（属提问者问题，含两个子问题；作者未分别作答。）", "evidence": []}
   ],
   "argument_steps": [
    "先直接肯定母语影响认识，并推出学习不同源语言的建议（P001）。",
    "给出理由：语言是思想的载体，最深处无法翻译（P002）。",
    "以四个元概念译例说明文化鸿沟（P003-P004）。",
    "由此推出英中译文之间的系统性错位乃至心脑分离（P005-P007）。",
    "结论：语言能力不好是必须解决的致命缺陷（P008）。"
   ],
   "concept_usage": [
    {"term": "母语", "meaning": "人自幼习得的语言；作者主张它限制并影响人对世界的认识。", "evidence": "P001", "ambiguity": "影响的程度与可否被完全克服未说明。"},
    {"term": "元概念", "meaning": "作者用以指 normal、free、moral、爱一类底层概念，并称其无法翻译。", "evidence": "P003", "ambiguity": "术语「元概念」未定义，边界不清。"},
    {"term": "语言是思想的载体", "meaning": "作者用以表述语言与思想的关系，并称在最深处无法翻译。", "evidence": "P002", "ambiguity": "未说明载体关系是决定性的还是影响性的，与P001「影响」的强度是否一致不明。"},
    {"term": "不同源的语言", "meaning": "作者建议学习的对象。", "evidence": "P001", "ambiguity": "「同源/不同源」按语系、文字还是别的标准判定，未说明。"},
    {"term": "心脑分离", "meaning": "作者用以描述译文错位造成的人们不知自己在说什么、在想什么的状态。", "evidence": "P007", "ambiguity": "属比喻性说法，未给出可观察的判定方式。"}
   ],
   "examples_and_targets": [
    "normal 不能翻译为「普通」、free 不能直接视为「自由」、moral 译为「道德」很勉强（P003）：作者的语言学例证，属待外部核查的断言。",
    "把「爱」对应为「love」是个巨大的坑（P004）：作者的例证。",
    "英文与它中文译文之间的错位（P005-P006）：作者论断的对象。",
    "提问者的两个问题（Q001）：属提问者说法，作者以「当然会」承接但未分别作答。"
   ],
   "conditions": [
    "建议的条件限定：「如果你打算做点严肃的有价值的思考」，「基本上」必须学不同源语言（P001）。",
    "作者未说明不同源语言的清单、学习程度与检验方式。",
    "未说明母语的限制是绝对的还是可以部分克服。"
   ],
   "rhetoric_and_tone": "极短答。先以「当然会」直接肯定提问，随后以断言推进；用强烈措辞（「巨大的坑」「致命的缺陷、思想的绝症」）；结尾以命令式收束（「不要有任何侥幸」）；未给出文献、实验或引用依据。",
   "unresolved_questions": [
    "作者未说明其「语言影响认识」主张的依据，正文无文献、实验或引用。",
    "「与母语不同源的语言」如何界定（语系、文字还是其他标准）未说明。",
    "normal/free/moral/爱-love 的不可译性论断属待外部核查的语言学断言。",
    "「心脑分离」的具体所指与判定方式未说明。",
    "提问者实际问了「认识是否受限」与「语言是否影响思想」两个方面，作者未区分作答。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "当然会，所以如果你打算做点严肃的有价值的思考，基本上必须要学一门与母语不同源的语言。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "语言是思想的载体，在最深处甚至是无法翻译的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "很多元概念的无法翻译是文化之间难以跨越的鸿沟。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "比如“normal”其实不能翻译为“普通”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "“moral”翻译为“道德”其实也很勉强。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "把“爱”对应为“love”也是个巨大的坑。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "因为这些底层的概念上的根本差别，一篇英文和它的中文译文之间存在着很难说得清的错位。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "常常南辕北辙。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "它甚至经常会造成人们不知道自己在说什么、在想什么的一种奇异的心脑分离。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "语言能力不好，是一种致命的缺陷、思想的绝症，是必须要解决掉的问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "对这一点，不要有任何侥幸。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言学与语言思维关系", "翻译研究", "认知与文化差异"],
   "issue_candidates": ["母语对认识的限制", "语言是否影响思想", "元概念的不可译性", "语言能力与思考能力"],
   "text_function_candidates": ["答疑", "断言式评论"],
   "object_candidates": ["母语", "英文", "中文", "normal", "free", "moral", "love"],
   "working_keywords": ["元概念", "无法翻译", "不同源的语言", "思想的载体", "心脑分离", "错位"]
  },
  "notes": "无图片节点；正文与lexical结构一致（8段）。篇幅极短，作者未提供任何文献、实验或引用依据；normal/free/moral/爱-love 的不可译性属待外部核查的语言学断言。提问者的两个子问题未分别作答。status=read，full_text_checked=true。"
 },
 "b9073126": {
  "analysis": {
   "question_context": "提问者问如何看待《蜘蛛侠1》台词「能力越大，责任越大」，以及具有相应能力的人是否应因不作为而受谴责。作者没有正面评价该台词，而是先确立伦理讨论的方法（应然须来自实然，不能来自多数人的愿望），再把「能力」界定为 power（能量、权力）而非 talent（特长），据此论证大能力自带风险，承担责任是自保与解脱之道。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "主张不要用人为构建的应然法则去剥夺别人的自由，因为这往往成本高昂而最终要破产。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "界定：应然必须来自不以人类意志为转移的实然，而不能直接来自人类自己的愿望。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "理由：以社会大多数成员的欲望指向作为应然准绳立法是难以避免的错误；作者自设「聚在一起不就是为了实现共同欲望吗」的反问，并以「不要以为人多心齐就能文成武德一统江湖」「结果往往是扑街」回应。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "结论：论证一种伦理法则是否应当遵守，要去寻找它实然的基础，而不是有多少人喜欢它。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "转题：拥有很大的能力首先面临很大的挑战——有人觊觎你的能力要你效命，推辞再三也难免牵连家人；即「匹夫无罪，怀璧其罪」。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "主张能力大到能左右成败、影响他人或集团生死荣辱时，现有法律保护与司法力量保不住平安，那只是无能力者的幻想；不吃敬酒就会见识各种罚酒；「不能用之，即当杀之」不只是小说童话。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013"], "summary": "限定：一般人把「能力越大责任越大」理解成 talent（特长）式的责任，而不是 power（能量、权力）；作者强调是 POWER。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015"], "summary": "界定 power 的后果：你帮谁谁就可能赢、背叛谁谁就可能由胜转败、站在谁的对立面就是谁的心腹大患；能力天生带着诅咒，抵抗不了则下场惨不忍睹。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P016", "P017", "P018"], "summary": "出路：找到正确的一群人、对ta们承担能力的责任；功利上可获利害相关的同志挡在诅咒面前，信仰上可因尽力而为而无惧死亡，从而让罚酒丧失力量、获得从容与自由。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P019"], "summary": "界定责任来源：这份责任不是社会约法或公民道德规定的，而是自然规律通过人性内嵌的逻辑架在颈动脉上的；只要真有能力、又嚷嚷出去、又没找到足够有效的负责对象，就手起刀落。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P020"], "summary": "结论：若想无罪，就把怀里的和氏璧藏好，不要不甘寂寞天天截图发朋友圈找死。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要试图通过人为构建某种应然法则去剥夺别人的自由，这往往是成本高昂而最终要破产的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应然必须来自某种不以人类意志为转移的实然，而不能直接来自人类自己的愿望（如「社会的大多数成员都很喜欢这个主意」）。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用社会大多数成员的欲望指向作为应然的准绳进行立法，是人类一种难以避免的错误。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "不要以为人多且欲望强烈（所谓「心齐」）这么干就会成功，作者称结果往往是扑街。", "evidence": ["E5", "E24"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "论证一种伦理法则是否应当遵守，要去寻找它实然的基础，而不是有多少人喜欢它、希望它成为事实。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拥有很大的能力首先面临很大的挑战：有人觊觎你的能力来要你效命，推辞再三也不能免；即所谓「匹夫无罪，怀璧其罪」。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能力大到可以左右事情成败、影响他人甚至一个集团的生死荣辱时，现有的法律保护与司法力量保不住平安，那只是没有这种能力的人的美好幻想。", "evidence": ["E22", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你不吃敬酒才会见识到世上有多少种罚酒；「不能用之，即当杀之」不只是小说上的童话，大国争雄时手握关键者缩起来也不行。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者纠正的一般理解（未具名的「一般人」）：把「能力越大责任越大」想成跑得更快、吃得更多、画得更像这类 talent（特长），而不是 power（能量、权力）。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本文讨论的「能力」是 power（能量、权力），而不是 talent（特长）。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拥有 power 意味着：你帮谁谁就可能赢，背叛谁谁就可能由胜转败，站在谁的对立面就是谁的心腹大患；想与人为善则成为恶人的眼中钉。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能力天生就带着诅咒，抵抗不了这些诅咒的人下场惨不忍睹；作者以「自古英雄如美人」与陈圆圆的下场设问。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "破解这份沉重诅咒唯一的出路，就是找到正确的一群人，对ta们承担能力的责任。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "承担责任从功利角度才会有足够的、你所选择的、与你利害相关、命运相连的同志挡在诅咒面前；从信仰角度只有承担根植于信仰的责任，才可以因已尽力而为而无惧死亡，罚酒才丧失力量，才有从容和自由。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这份能力附带的责任不是社会约法、公民道德规定给你的，而是自然规律通过人性内嵌的逻辑架在你颈动脉上的。", "evidence": ["E21", "E25"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "只要真的有能力、又嚷嚷出去了、又没有找到足够有效的负责对象，自然规律就会手起刀落；作者因此主张：想无罪就把怀里的和氏璧藏好，不要天天截图发朋友圈找死。", "evidence": ["E26", "E27"]},
    {"claim_id": "C017", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问如何看待《蜘蛛侠1》台词「能力越大，责任越大」，以及具有相应能力的人是否应因不作为而受谴责（属提问者问题；作者未直接回答是否应受谴责，而是重构为能力自带风险的论证）。", "evidence": []}
   ],
   "argument_steps": [
    "先立方法：不要用人为应然法则剥夺他人自由（P001）。",
    "定义应然的来源：须来自不以人类意志为转移的实然（P002）。",
    "以多数人欲望立法的错误为理由，并用「人多心齐」的反例收束（P003-P004）。",
    "得出结论：论证伦理法则要找实然基础而非受欢迎程度（P005）。",
    "转题：大能力首先带来被觊觎与被胁迫的挑战（P006-P007）。",
    "主张法律与司法保护不了有能力者，罚酒形式多样（P008-P011）。",
    "限定「能力」的含义为 power 而非 talent（P012-P013）。",
    "说明 power 的后果与「诅咒」（P014-P015）。",
    "给出出路：找到正确的一群人并承担责任，功利与信仰两条理由（P016-P018）。",
    "界定责任来源为自然规律，并给出三条件同时成立时的后果（P019）。",
    "结论：要么藏好和氏璧，要么承担责任的警告式收束（P020）。"
   ],
   "concept_usage": [
    {"term": "应然/实然", "meaning": "作者用以区分伦理法则的来源：应然必须来自不以人类意志为转移的实然，不能来自多数人的愿望。", "evidence": "P002", "ambiguity": "未给出判定某实然是否「不以人类意志为转移」的操作标准。"},
    {"term": "talent（特长）与 power（能量、权力）", "meaning": "作者用前者指跑得更快、吃得更多、画得更像一类特长，用后者指能左右成败、影响他人或集团命运的能力；本文讨论的是 power。", "evidence": "P012", "ambiguity": "power 的边界与分级未给出，英文词义区分依赖作者自述。"},
    {"term": "责任", "meaning": "本文特指对「正确的一群人」承担的责任，其功能是抵御能力带来的诅咒。", "evidence": "P016", "ambiguity": "「正确的一群人」如何判定、责任的具体内容均未说明。"},
    {"term": "诅咒", "meaning": "作者用以指大能力招致的觊觎、胁迫与敌意。", "evidence": "P015", "ambiguity": "属比喻性用法，未给出可检验的界定。"},
    {"term": "自然规律", "meaning": "作者用以指能力附带责任的来源，称其通过人性内嵌的逻辑起作用。", "evidence": "P019", "ambiguity": "未说明它与生物规律、社会规律的关系，也未给出依据。"},
    {"term": "罚酒/敬酒", "meaning": "作者用以指对有能力者的胁迫手段，罚酒形式多样且会随不服从升级。", "evidence": "P010", "ambiguity": "属比喻性用法。"},
    {"term": "匹夫无罪，怀璧其罪 / 和氏璧", "meaning": "作者引用的成语与典故，用以说明有能力者因能力本身而招祸。", "evidence": "P007", "ambiguity": "引用未标出处，属成语化用。"}
   ],
   "examples_and_targets": [
    "《蜘蛛侠1》台词「能力越大，责任越大」（Q001）：提问者引述的影视台词；作者未评价台词本身，而是重构「能力」的含义（P012）。",
    "三顾茅庐、请老娘曹营一叙、赚家小去梁山享福、敬酒罚酒（P006、P010）：作者使用的典故与比喻。",
    "匹夫无罪，怀璧其罪（P007）与和氏璧（P020）：作者引用的成语典故。",
    "「不能用之，即当杀之」（P011）：作者引述并反问其是否只是小说上的童话。",
    "大国争雄（P011）：作者设定的情境。",
    "跑得更快吃得更多画得更像（P012）：作者列举的「一般人」所想的 talent。",
    "陈圆圆（P015）：作者引作「自古英雄如美人」的例证，属待外部核查的历史叙述。",
    "大伯拎着你的脖领子（P019）：作者使用的修辞材料。",
    "f*k yo all、tm（P019、P020）：原文所含的口语化粗话表达，部分字符是否经平台处理无法判定。",
    "社会约法、公民道德（P019）：作者否定的责任来源。"
   ],
   "conditions": [
    "三条件同时成立时作者称自然规律会「手起刀落」：真的有能力、又嚷嚷出去了、又没有找到足够有效的负责对象（P019）。",
    "适用对象限定：本文讨论的能力是 power（能量、权力），不是 talent（特长）（P012）。",
    "情形限定：一种能力大到可以左右事情的成败，能影响到ta人甚至一个集团的生死荣辱（P008）。",
    "作者以「你以为……吗？」的反问形式表述法律无力的判断，未给出经验证据或案例数据（P008）。",
    "作者未说明「正确的一群人」的判定标准与所承担责任的边界。"
   ],
   "rhetoric_and_tone": "论辩与训诫混合。第二人称「你」直陈；用典密集（三顾茅庐、曹营、梁山、怀璧其罪、陈圆圆）；反问与诘问密集（「你以为就现在的『法律保护』、司法力量就能保得住你的平安吗？」「POWER，明白吗？」「陈圆圆下场如何？」）；以威胁性比喻推进（颈动脉、手起刀落）；结论以粗话式警告收束（「那就手起刀落，f*k yo all」「天天截图发朋友圈找死」）。",
   "unresolved_questions": [
    "提问者问的是「具有相应能力的人是否应该因为不作为而受到谴责」，作者将问题重构为能力（power）自带风险、承担责任是自保，未直接回答是否应受谴责。",
    "「正确的一群人」如何判定、由谁判定，正文未说明。",
    "作者称责任来自「自然规律通过人性内嵌的逻辑」，其依据与可检验性未说明。",
    "陈圆圆的历史下场属待外部核查的叙述，作者未给出出处。",
    "talent 与 power 的词义区分依赖作者自行界定，未给出词典或学术依据。",
    "文中「f*k yo all」「tm」等为原文所有（部分字符以星号或缩写呈现），是否经平台处理无法从语料判定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不要试图通过人为构建某种应然法则去剥夺别人的自由，这往往是成本高昂而最终要破产的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "应然必须是来自某种不以人类意志为转移的实然", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "而不能是直接来自人类自己的愿望", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "用社会大多数成员的欲望指向来作为应然的准绳进行立法，是人类一种难以避免的错误。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P003", "quote": "不要以为你们人多而且欲望都很强烈（即所谓“心齐”），这么干就会文成武德一统江湖。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "结果往往是扑街。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "所以，论证一种伦理法则是否应当遵守，要去寻找它实然的基础，而不是有多少人喜欢它、希望它成为事实。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "自然有人觊觎你的能力来三顾茅庐，要你效命。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "匹夫无罪，怀璧其罪。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P008", "quote": "一种能力能大到可以左右事情的成败，能影响到ta人、甚至一个集团的生死荣辱", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "那只是没有这种能力的人的美好幻想。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "你不吃敬酒，你才会见识到世上有多少种罚酒。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "你以为这真只是小说上的童话吗？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "一般人想能力越大责任越大，想的都是跑得更快吃得更多画得更像这类所谓talent（特长），而不是power（能量、权力）。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "POWER，明白吗？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "你帮谁，谁就可能赢；背叛谁，谁就可能由胜转败；站在谁的对立面，就是谁的心腹大患。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "它天生就带着诅咒，人如果抵抗不了这些诅咒，下场惨不忍睹。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "自古英雄如美人，长得好看只有好处吗？陈圆圆下场如何？", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "而要破解这份沉重的诅咒，唯一的出路，就是找到正确的一群人，对ta们承担能力的责任。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P017", "quote": "才会有足够的、你所选择的、与你利害相关、命运相连的同志去挡在这种诅咒面前", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "只有你承担了根植于信仰的责任，你才可以因为已经尽力而为而随时随地无惧于死亡。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P018", "quote": "那些种种的罚酒才能丧失它的力量，你才有从容和自由可言。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P019", "quote": "这份能力附带的责任，不是什么社会约法、公民道德规定给你的，而是自然规律通过人性内嵌的逻辑架在你颈动脉上的。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P019", "quote": "自然规律根本不管你有没有个大伯拎着你的脖领子给你这个提示", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P019", "quote": "反正只要你真的有能力、你又嚷嚷出去了、你又没有找到足够有效的负责对象，那就手起刀落", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P020", "quote": "要么，你这匹夫想要无罪，怀里的和氏璧就tm藏好点！", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/政治哲学", "权力与责任", "社会规范与立法依据"],
   "issue_candidates": ["能力越大责任越大", "应然的来源（实然基础与多数人欲望）", "有能力者是否应因不作为受谴责", "权力带来的风险与自保"],
   "text_function_candidates": ["答疑", "论辩", "训诫"],
   "object_candidates": ["《蜘蛛侠1》", "陈圆圆", "和氏璧", "大国", "自然规律", "社会约法/公民道德"],
   "working_keywords": ["应然", "实然", "talent", "power", "诅咒", "罚酒", "怀璧其罪", "正确的一群人", "手起刀落"]
  },
  "notes": "无图片节点；正文与lexical结构一致（20段）。提问者问「是否应因不作为受谴责」，作者未直接回答，而是重构为能力（power）自带风险、承担责任是自保与解脱的论证。文中「f*k yo all」「tm」为原文所有。P015陈圆圆的历史下场属待外部核查的叙述；P019称责任来自「自然规律」未给出依据。status=read，full_text_checked=true。"
 },
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
