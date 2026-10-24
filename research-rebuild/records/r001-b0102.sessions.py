# -*- coding: utf-8 -*-
"""批次 r001-b0102 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0102.sessions.py            # 写 out/r001-b0102.out.jsonl
  python3 records/r001-b0102.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0102"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0102.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "23d38351": {
  "analysis": {
   "question_context": "提问者问如何看待济南大学女生自杀、遗书称“自杀仅仅是因为我爸爸”，以及家庭矛盾导致的心理问题应如何疏导。作者没有复述事件经过，而是转到“训诫”的正当性：父母训诫子女是否正当、边界与操作原则何在，并把训诫的正当性归结为爱，最后回到这起事件，称孩子在放弃前给了最后一次原谅、父母应原谅她。提问者立场与作者立场需分开。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004"], "summary": "引出“训诫”问题：父母训诫子女常见，但其正当性、边界与操作原则使很多人迷茫。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005","P006","P007","P008"], "summary": "常见正当性依据“我担心不说你，你将来会吃亏”自相矛盾：父母并非上帝，无法保证判断正确；此结不解，训诫正当性存疑，人便率性而为。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009","P010","P011","P012","P013"], "summary": "爱必须深思熟虑、穷尽合理性；“我怕我的愚蠢将我的爱变成你的苦难”的忐忑是爱的本质特征与核心机制，保证爱穷尽智慧并成为智慧的恒久驱动器。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P014","P015","P016","P017","P018"], "summary": "贪婪与恐惧驱动智性则指向灾难，并因要享受成果而拒绝忐忑，走向自欺的自洽与板结刚硬的傲慢；傲慢无视他人痛苦，坚定只无视自身苦难。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P019","P020","P021"], "summary": "爱人者不会因自己的理论完美而认定他人痛苦无价值；只要痛苦仍在且自己尚有神志，就仍有反思再反思的必要。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P022","P023","P024","P025","P026","P027","P028","P029","P030"], "summary": "子女首先需要的是父母的“永远忐忑”及由此催生的无限反思，而非软语温言；有这份忐忑，仍残留的痛苦才是命中注定、最小、最好可能，而非出自父母的恶意。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P031","P032","P033","P034","P035","P036","P037","P038"], "summary": "永不止息的反思使父母不再有“你倒霉你活该”的刚硬自信，并让子女看到自己的痛苦在促使父母成长，故父母永远心存歉意；子女不能原谅的是父母为心安理得而拥抱的从不反思的傲慢。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P039","P040","P041","P042","P043","P044"], "summary": "反问父母：无忐忑、无犹豫、无更新，只有刚硬的自洽，哪里有爱；不出于爱没有资格获得宽恕；实际是子女在爱甚至溺爱父母。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P045","P046","P047","P048"], "summary": "回到事件：这孩子溺爱不动了、放弃了，放弃前给了最后一次原谅，你们要原谅她；并归结训诫所必要的资格与证明。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱是一件极其需要深思熟虑、追根问底的事情；不是穷尽合理性追求之结果的东西不成其为爱。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“我怕我的愚蠢将我的爱变成你的苦难”的忐忑本身就是爱的本质特征之一，是爱最核心的机制。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "贪婪与恐惧对智性的驱动最终指向自己和他人的灾难，并因要享受成果而拒绝忐忑，走向板结刚硬的傲慢。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "傲慢者敢于无视的是他人的痛苦，坚定者敢于无视的是自己的苦难。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "子女首先需要的不是父母的软语温言，而是“永远的忐忑”及由此必然催生的无限反思。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在无限忐忑与竭尽反思下父母仍挣扎不放弃的训诫，虽不能确保正确，已是子女所能得到的最小痛苦、最好可能。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "子女不能原谅的不是父母的错，而是父母为了自己心安理得而迫不及待拥抱的、从不反思的傲慢。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不出于爱就没有资格获得宽恕；训诫所必要的资格与证明即在于出于爱的忐忑与反思。", "evidence": ["E8","E9"]}
   ],
   "argument_steps": [
    "提出问题：父母训诫子女常见，但正当性、边界与操作原则令人迷茫。",
    "指出常见正当性依据“怕你将来吃亏”无法自证：父母并非上帝，可能判断错误。",
    "给出正面命题：爱的本质是“怕自己的愚蠢把爱变成对方的苦难”的永恒忐忑，它保证爱穷尽智慧。",
    "以贪婪与恐惧驱动智性的后果作反面对照，引出刚硬的自洽与傲慢。",
    "据此重释训诫：子女需要的是父母永不止息的忐忑与反思，而非软语温言或刚硬自信。",
    "回到具体事件：孩子放弃前给了最后一次原谅，因此父母应原谅她；训诫的资格在于爱。"
   ],
   "concept_usage": [
    {"term": "训诫", "meaning": "父母对子女的告诫与纠正；本文讨论其正当性来源与边界。", "evidence": "P002", "ambiguity": "未给出可操作的边界规则，只给出资格条件。"},
    {"term": "爱", "meaning": "以“怕自己的愚蠢把爱变成对方苦难”的永恒忐忑为核心机制、穷尽合理性的行动。", "evidence": "P010", "ambiguity": "带有宗教化色彩，未界定与亲情的具体关系。"},
    {"term": "忐忑", "meaning": "对自身可能犯错、可能伤害所爱之人的持续不安，是作者所说的爱的核心。", "evidence": "P010", "ambiguity": "未说明其与病理性焦虑的界限。"},
    {"term": "刚硬的自洽/傲慢", "meaning": "为摆脱忐忑、享受自洽而拒绝反思的封闭状态。", "evidence": "P016", "ambiguity": "与“坚定”的区分被作者断言，未给判据。"}
   ],
   "examples_and_targets": [
    "提问所指的济南大学女生自杀与遗书事件（回应对象/背景）",
    "“我担心不说你，你将来会吃亏”这一常见训诫理由（被质疑的通俗观点）",
    "贪婪与恐惧对智性的驱动（作者的对照材料）",
    "“你爹”（作者讥讽的、自称有爱却刚硬不反思的父母形象）"
   ],
   "conditions": [
    "训诫的正当性讨论以“若过不去判断可能出错这一关，整个正当性都存疑”为前提。",
    "爱的忐忑以父母有神志、尚未丧失反思能力为前提，“直到生命的最后一刻，人的灵智消失为止”。",
    "子女能看见父母的忐忑与反思，是其宽恕与相信“已是最小痛苦”的条件。"
   ],
   "rhetoric_and_tone": "强烈训诫与道德谴责语气；大量反问与第二人称直呼“父母们”“你们”；排比与重复（“一次、又一次、又一次”）；宗教化措辞（“照着神的样子造出来的人”“罪”“宽恕”）；由抽象论理转向对具体事件的哀悼与呼吁。",
   "unresolved_questions": [
    "P049“为什么人们不喜欢被批评？”疑为平台相关推荐或下一问标题混入，非本文论证。",
    "事件事实（遗书内容、家庭经过）未在正文复述，需外部核查；作者与提问者对事件的立场未逐点分开。",
    "正文并未给出提问所问“家庭矛盾导致的心理问题应如何疏导”的具体操作方案。",
    "“神”“罪”“宽恕”等用语的具体所指与是否具有宗教含义未界定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P009", "quote": "爱是一件极其需要深思熟虑、追根问底的事情", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P011", "quote": "这个永恒的担忧，本身就是爱，是爱最核心的机制", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P017", "quote": "因此，后者总是走向板结的、刚硬的傲慢", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P018", "quote": "坚定者敢于无视的是自己的苦难，而傲慢者敢于无视的是他人的痛苦", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P023", "quote": "ta们要的只是你们这【永远的忐忑】啊", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P029", "quote": "但已经是一个人所能得到的最小痛苦、最好可能了", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P037", "quote": "而是你们为了自己心安理得而迫不及待拥抱的那一份刚硬如铁的、从不反思的傲慢", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P041", "quote": "不是出于爱，你有什么资格获得宽恕", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P048", "quote": "你们知道训诫所必要的资格、和这资格的证明是什么了吗", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理", "家庭教育", "情感与爱"],
   "issue_candidates": ["训诫的正当性", "爱的本质与机制", "亲子关系与宽恕", "对自杀事件的回应"],
   "text_function_candidates": ["论说", "训诫", "答问"],
   "object_candidates": ["父母", "子女", "训诫", "爱", "反思", "宽恕"],
   "working_keywords": ["训诫", "永远忐忑", "反思", "刚硬的自洽", "傲慢", "宽恕", "爱"]
  },
  "notes": "正文末 P049“为什么人们不喜欢被批评？”疑为平台相关推荐/下一问标题混入，已在 unresolved_questions 标注。本文以“训诫”立论回应提问，未直接给出心理疏导的操作方案。"
 },
 "6394ed80": {
  "analysis": {
   "question_context": "提问者问面子和尊严的关系与区别。作者以“假面”为题，主张面子是一套不断发送实力/资源/价值/地位信号、诱使对方形成既贪求又畏惧态度的社交把戏，可快速替代尊重；而尊重是需要磨砺与觉醒的能力、是无条件给予的义务，二者有本质区别，且只有尊重才能赢得真正有能力者的合作，其内核是爱。注意：正文谈的是“尊重”，未直接界定提问所用的“尊严”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005"], "summary": "面子的机制：不断发送自己有实力/资源/价值/地位的信号以形塑关系，诱使对方既贪求又畏惧，被误认为等于“尊重”，是可快速达成的替代品。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006","P007","P008","P009","P010","P011"], "summary": "尊重的本质：必须建立在尊重的能力上，需要磨砺淬炼与觉醒；尊重语境下保持礼仪、慎重对待他人感受是无条件的义务，不出于害怕报复、贪图回报或争取崇拜。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P012","P013","P014","P015","P016"], "summary": "尊重因免费、默认、无条件而量大、成本极低，反被面子信徒视为“不够给面子”；面子礼数华丽却充满条件，要求随时证明够格、上道、懂事；被尊重者自由而不受“得面子”的窒息束缚。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P017","P018","P019","P020","P021","P022"], "summary": "人们因无法相信不出于恐惧和贪婪的尊重存在，便见不到它、也无从对比发现手中面子的假；正确的尊重常被误读为“不给面子”，加剧面子焦虑，使面子成为精神生活主题。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023","P024","P025","P026","P027","P028","P029","P030"], "summary": "面子口头禅是信号；装傻扮小者的自保与隐形者；面子文化中长大的孩子几乎无缘见到真正的尊重，往往要到近不惑之年吃足苦头后才可能醒悟，而其子女已过教养期。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P031","P032","P033","P034","P035","P036","P037","P038","P039","P040"], "summary": "尊重为何重要：它是唯一能让真正有能力的人考虑合作机会的要害；真有本事的人不缺面子，面子的把戏对他们是无聊陷阱，心下只有累与厌。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P041","P042","P043","P044","P045","P046","P047","P048"], "summary": "不给面子的主要办法是礼貌谢绝、断绝接触，而非面斥；面子党以伤卖惨使人欠下“伤害感情债”；最好的策略仍然是尊重。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P049","P050","P051","P052","P053","P054","P055","P056","P057","P058","P059","P060","P061","P062","P063","P064","P065","P066"], "summary": "只有尊重能同时尊重喜爱与不喜爱、亲近与仇恨、前来与离开、联结与断开、同意与反对等，从而为存在更大的人撑起可来可去、可进可止而不必担心怨恨报复的空间；这就是王者之气与得道多助之道。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P067","P068","P069","P070","P071","P072"], "summary": "懂与不懂尊重造成事实上的等级差异，并作为“遗传性文化病”代代相传；无条件尊重其实是长期存续需被接受的义务，只是有缓刑机制；误把面子当尊重者最好早点醒悟。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P073","P074","P075","P076","P077","P078","P079"], "summary": "能改变命运的人会寻找能燃起其信心的人；撑起信与望的尊重到底是什么——是爱；轻如鸿毛的爱胜过重如泰山的面子。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "面子的秘密是不断发送自身有实力/资源/价值/地位的信号来形塑他人与自己的关系，诱使对方形成既贪求又畏惧的“最佳态度”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "尊重必须建立在尊重的能力上，且这种能力需要磨砺淬炼与觉醒，并非普遍被拥有。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在尊重的语境下，对人保持礼仪、慎重对待他人感受是无条件的，因为这是人对人应尽的义务。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“面子”一族礼数华丽周全，但那是有无数条件的，要你随时证明“够格”、要你“上道”“懂事”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "尊重是唯一能让真正有能力的人正襟危坐、考虑给你合作机会的要害；面子不行。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真有本事的人根本不缺面子，面子的把戏是给无能之辈做关系投机用的无聊游戏。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不给面子的主要办法不是当面“不给面子”，而是礼貌谢绝、断绝接触途径，因为面子党会以伤卖惨使人欠下感情债。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有尊重能同时尊重对方的一切选择与状态，为存在更大的人撑起不必担心怨恨、报复的空间，这就是得道多助的道。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "懂与不懂尊重会造成事实上的等级差异，并作为“遗传性文化病”代代相传；无条件尊重是长期存续需被接受的义务，只是有缓刑机制。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "撑起信与望的尊重其实就是爱；轻如鸿毛的爱胜过重如泰山的面子。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "先描述面子的机制：发送信号、诱使对方形成既贪求又畏惧的态度，被误当尊重。",
    "界定真正的尊重：它是需要能力与觉醒的无条件义务，不因恐惧或贪婪。",
    "对比二者成本与体验：尊重免费量大反被嫌“不够给面子”，面子有无数条件并带来窒息。",
    "说明面子文化为何自我延续：人们不信有无条件的尊重，孩子见不到真尊重，往往中年才醒悟。",
    "论证为何尊重更重要：真正有能力的人不缺面子，只被尊重打动。",
    "给出实践策略：对面子党应礼貌谢绝、断绝接触，最终仍以尊重回应。",
    "上升到“得道多助”与代际文化病，并把尊重的内核归结为爱。"
   ],
   "concept_usage": [
    {"term": "面子", "meaning": "通过发送实力/资源/价值/地位信号、以条件交换来形塑关系的社交把戏。", "evidence": "P001", "ambiguity": "与“尊严”的关系未直接界定。"},
    {"term": "尊重", "meaning": "以尊重能力为基础、无条件给予、把对方当人对待的义务性态度与空间。", "evidence": "P008", "ambiguity": "“尊重能力”如何获得只给了“磨砺/觉醒”的说法。"},
    {"term": "遗传性文化病", "meaning": "不懂尊重的行为模式通过教养在代际间复制。", "evidence": "P068", "ambiguity": "以“绝嗣”作因果推断，无经验证据。"},
    {"term": "爱", "meaning": "作者把尊重的实质与最高形态称为爱。", "evidence": "P076", "ambiguity": "与一般情感意义的“爱”未作区分。"}
   ],
   "examples_and_targets": [
    "“君子之交，其淡如水”（作者引用的对照典故）",
    "“给你脸了”“就为了争个面子至于吗”等口头禅（被分析的信号）",
    "英雄美人、提着礼物排队的人（被面子套路包围的有能力者）",
    "中计的女孩子、面子文化中的小孩子（受害者例证）"
   ],
   "conditions": [
    "面子的“替代尊重”效果以对方也信面子、且以利相交为前提。",
    "尊重能奏效以对方是有尊重能力的人为前提，否则会被误读为“不给面子”。",
    "作者称无条件尊重并非绝对无条件，条件是“你遵守，自然就饶你一命”，并有代际缓刑。"
   ],
   "rhetoric_and_tone": "讽刺与轻蔑语气（“面子党”“老子不稀罕”）；大量排比（尊重喜爱/不喜爱、亲近/仇恨……）；格言化短句收束（“是爱”“轻如鸿毛的爱，胜过重如泰山的面子”）；对有能力者与面子投机者的对比刻画。",
   "unresolved_questions": [
    "提问问“面子和尊严的关系”，正文只谈“面子”与“尊重”，未界定或回答“尊严”。",
    "“遗传性文化病”“绝嗣”等因果主张缺少经验证据，属强断言，需外部核查。",
    "“得道多助的那个道”与“王者之气”未作进一步界定。",
    "文中“尊重”是否等同于提问者所说的“尊严”不能由本文确定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "面子的秘密，就是要在社交之中不断的发送自己很有实力", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P007", "quote": "尊重是一种需要磨砺和淬炼、需要觉醒才会有的能力", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P010", "quote": "而仅仅是因为这是人对人应尽的义务", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P014", "quote": "但是那是有无数条件的，是要你随时证明“够格”的", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P032", "quote": "因为尊重是唯一能让真正有能力的人正襟危坐，考虑给你合作的机会的要害", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P034", "quote": "真有本事的人根本不缺面子", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P041", "quote": "而是“礼貌谢绝”“断绝接触途径”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P063", "quote": "而只有懂得尊重的人可以为ta们撑起可以来、可以去", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P069", "quote": "本身就意味着“无条件尊重”其实是一种想要长期存续就需要被接受的义务", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P077", "quote": "轻如鸿毛的爱，胜过重如泰山的面子", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理", "社会关系", "文化批评"],
   "issue_candidates": ["面子与尊重之别", "尊重的条件性", "关系投机", "文化代际传递"],
   "text_function_candidates": ["论说", "对比辨析", "答问"],
   "object_candidates": ["面子", "尊重", "能力者", "面子文化", "爱"],
   "working_keywords": ["面子", "尊重", "假面", "无条件尊重", "得道多助", "爱"]
  },
  "notes": "提问使用“尊严”，正文使用“尊重”，未直接给出“尊严”定义或与面子的对照，已在 unresolved_questions 标注。"
 },
 "4e7ea5d1": {
  "analysis": {
   "question_context": "提问者直接问“什么是自然法？”。作者用一个思想实验给出定义：假设两个互不相识、语言不通的智慧生物在旷野相遇，双方对彼此行为模式的估计必有一个交集，这个交集就是自然法；再由“新来宾是否会让交集为空”区分自然法主义者。作者把自然法分为狭义（智慧生命必然共同遵守的伦理法则，即“自然伦理”）与广义（还包含自然规律），并列出普遍管辖、绝对公正、无司法成本、绝对权威四大优势，最后指出广义自然法启示人类关于“法”的理想。文末标“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002"], "summary": "提出可以用一个很简单的思考工具来理解自然法。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013"], "summary": "旷野相遇思想实验：双方（乃至更多来客）彼此估计对方行为模式，层层求交；这个交集中装着的就是自然法。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P014","P015","P016"], "summary": "变种问题：若新来宾使交集为空，是承认交集合法为空，还是认定该来宾只是无人机；答“不为空+无人机”者即狭义自然法主义者。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P017","P018","P019"], "summary": "“狭义”的含义：自然法仅含智慧生命必然共同遵守的伦理法则，即“自然伦理”；若取广义，则集合必然不为空。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P020","P021","P022","P023","P024","P025"], "summary": "广义自然法包含自然规律（牛顿定律、热力学定律等）；不承认者只能说明其不具智慧生物资格、位格降级为“东西”。为让话题有意义，本文取狭义。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P026","P027","P028","P029","P030","P031","P032","P033","P034","P035"], "summary": "优势一“普遍管辖”：不需受管辖者知情同意，不依赖其个人理解；这些法则必须天然自动成立，因为没人能承担“需对方同意才成立”的代价。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P036","P037","P038"], "summary": "优势二“绝对公正”：不受限辖下任何一方，永无“既是运动员又是裁判”问题；人类立法无法避免，即使交由人工智能审判也由编写维护者代行裁判。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P039","P040"], "summary": "优势三“没有司法成本”：违反后结果自然出现，不需凑钱请人执行判决，也不担心该判未判与徇私枉纵。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P041","P042","P043","P044"], "summary": "优势四“绝对权威”：判决绝对有效、无可辩驳；对结果感到意外只能怪自己搞错，这一基本假设是逻辑思维的根基，动摇会导致理性崩溃。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P045","P046"], "summary": "结论：包含自然规律的广义自然法启示了人类一切关于“法”的理想，是立法司法的终极目标与伦理准则的质量标准；（未完，待续）。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把多个智慧生物彼此估计对方行为模式的交集层层求交，这个交集中装着的就是自然法。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "狭义自然法只包含智慧生命必然共同遵守的伦理法则，即“自然伦理”；广义自然法则还包含自然规律，且必然不为空。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不承认自然规律（含其朴素版本）只能说明该对象尚无足以称为智慧生物的资格，会使其位格降格为“东西”。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法普遍管辖：不需要受管辖者的知情和同意，也不依赖于其个人理解。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法必须天然、自动地成立，因为没有人能承担“需对方同意才能成立、需对方正确理解才能实施”的代价。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法绝对公正，不受限于辖下任何一方，永远不会出现“既是运动员、又是裁判”的问题，而人类立法无法避免。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法没有司法成本：违反后结果自然出现，不需专门凑钱请人执行判决。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法的判决绝对有效、无可辩驳，任何人对结果感到意外都只能怪自己搞错了什么。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对自然法绝对公平的信念是智慧生物进行逻辑思维的根基，动摇它会导致理性崩溃。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "包含自然规律的广义自然法启示了人类一切关于“法”的理想，是立法司法的终极目标与伦理准则的质量标准。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "以旷野相遇、语言不通的双方互相估计行为模式为思想实验。",
    "层层求交，把交集界定为自然法；再以“交集是否为空”区分自然法主义者。",
    "区分狭义（伦理法则/自然伦理）与广义（含自然规律）两种自然法，并说明本文取狭义。",
    "依次论证自然法四大优势：普遍管辖、绝对公正、无司法成本、绝对权威。",
    "由绝对权威推出对自然法的信服是理性思维的根基。",
    "结论：广义自然法是人类一切“法”之理想与伦理准则的质量标准。"
   ],
   "concept_usage": [
    {"term": "自然法", "meaning": "智慧生物彼此对行为模式估计的交集；狭义指必然共同遵守的伦理法则。", "evidence": "P013", "ambiguity": "狭义/广义切换，且文末未完，定义仍在展开。"},
    {"term": "自然伦理", "meaning": "狭义自然法的别名，仅指伦理法则。", "evidence": "P018", "ambiguity": "与广义自然法的关系依赖“智慧生命”定义。"},
    {"term": "普遍管辖", "meaning": "无需受管辖者知情同意即自动生效。", "evidence": "P028", "ambiguity": "与“正当性”的关系未展开。"},
    {"term": "位格降级", "meaning": "不承认自然规律者被视为“东西”而非智慧生物。", "evidence": "P023", "ambiguity": "判据较为循环。"}
   ],
   "examples_and_targets": [
    "旷野相遇的双方与蓝皮肤外星人（思想实验设定）",
    "第三个外星人/新来宾与“无人机”假设（变种问题）",
    "牛顿定律、热力学定律、万有引力定律、动量守恒（广义自然法例证）",
    "石头能打破头、高温能导致烧伤（朴素版本的自然规律）",
    "拆房子割麦子、掉落悬崖摔死（普遍管辖例证）",
    "人工智能根据大数据审判（被反驳的替代立法方案）",
    "手肿了却辩称已采取足够措施（绝对权威例证）"
   ],
   "conditions": [
    "思想实验假设对方是智慧生物，且双方对彼此行为模式的估计存在交集；层层求交后交集“略小一点”但不断言为空。",
    "本文讨论的是狭义自然法，即以伦理法则为限；取广义则结论被锁定、话题失去意义。",
    "自然法的效力以“不承认者会实际受损（被揍、摔死等）”为经验前提。"
   ],
   "rhetoric_and_tone": "以思想实验和层层设问推进；用外星人、无人机、香菇、精神错乱等比喻与夸张；断言式收束（“就是自然法”“必然是自然法学派”）；带论战性的驳论（反驳“需对方同意”的立法观与AI审判方案）。",
   "unresolved_questions": [
    "文末标“（未完，待续）”，自然法问题未完结。",
    "“智慧生命”的判据与“位格降级”的推理是否循环，需进一步界定。",
    "“交集必然不为空”被作为信仰性前提接受，而非证明。",
    "自然法与伦理、法律、宗教等概念的关系在本文未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P013", "quote": "这个交集里装着的，就是自然法", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P018", "quote": "这种自然法仅仅只包含智慧生命所必然共同遵守的伦理法则", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P022", "quote": "只能说明该对象尚无足以称为智慧生物的资格", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P029", "quote": "它不需要受管辖者的知情和同意，不依赖于受管辖者的个人理解", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P033", "quote": "因为没有人能承担这些法则需要对方同意才能成立", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P037", "quote": "自然法不受限于其辖下的任何一方", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P039", "quote": "自然法没有司法成本", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P042", "quote": "自然法的判决绝对的有效，无可辩驳", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P043", "quote": "这一基本假设是人类（包括一切智慧生物）进行逻辑思维的根基", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P045", "quote": "包含了自然规律的广义自然法启示了人类一切关于“法”这一事物的理想", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["法哲学", "伦理学", "认识论"],
   "issue_candidates": ["自然法的定义", "自然伦理与自然规律", "法的正当性", "立法者的自我约束"],
   "text_function_candidates": ["论说", "概念界定", "答问"],
   "object_candidates": ["自然法", "自然伦理", "自然规律", "智慧生物", "立法"],
   "working_keywords": ["自然法", "自然伦理", "思想实验", "普遍管辖", "绝对公正", "绝对权威"]
  },
  "notes": "文末“（未完，待续）”，本文为系列之一，自然法定义尚未完结；“自然法绝对公平”“交集不为空”等为作者前提性断言，已在 unresolved_questions 标注。"
 },
 "4f7e63e4": {
  "analysis": {
   "question_context": "提问者问《觉醒年代》编剧借辜鸿铭之口说“我头上的辫子是有形的，而你们心中的辫子是无形的”中，“心中的辫子”指什么。作者没有顺着编剧台词解释，而是先质疑辜鸿铭被神化的形象与学术成就：列举不出确切成就，其《论语》英译爱自由发挥、关键概念误译，“十三个博士学位”“倒读英文镇洋人”等传说不可信；最后反过来说，“心中的辫子”恰恰是那种非把辜的传说形象维护住不可的冲动背后的脆弱心态。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005"], "summary": "质疑辜鸿铭的确切学术成就，追问其翻译《论语》是否真被看过、译得如何，指辜译《论语》出了名地爱自己发挥。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P006","P007","P008","P009"], "summary": "以《论语》首章“人不知而不愠”的辜译为样本，引出具体文本批评。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P010","P011","P012","P013","P014","P015","P016","P017"], "summary": "逐点批评该译文：“君子”译成 wise and good man 是错的（类似把“道”译作 principle/way）；“人不知”不应译为 not noticed of men；of men 不必逐字直译；“愠”译 discomposure 姑且算行但显晦涩。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P018","P019"], "summary": "指“十三个博士学位”是假的，以当时人类寿命判断不可能实实在在完成这种成就。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P020","P021"], "summary": "指“倒读英文镇洋人”只是段子，人证物证全无，就算做到也只是“实时视觉转换”能力，不值得震惊。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P022","P023","P024"], "summary": "结论：辜鸿铭唯一擅长的是教外语，别的都一塌糊涂；其“名言”不值得深究；传说中牛得威震天的形象不过是个纸糊的人偶。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P025","P026","P027"], "summary": "点题：“心中的辫子”恰恰是非把辜的传说形象维护住不可的冲动背后的脆弱心态。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "辜鸿铭的确切学术成就难以列举；他翻译《论语》是出了名的爱自己发挥。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把“君子”这个级别的概念意译为“wise and good man”是错的；如同把“道”译作 principle/way，只要用自认为贴切的英语词汇就是错。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“人不知”译为“not noticed of men”（没被注意到）不合原意，“of men”也不必逐字直译出来。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“十三个博士学位”是假的，以当时人类寿命不可能实实在在完成这种成就。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“倒读英文镇洋人”这种段子人证物证全无，即便做到也只是“实时视觉转换”能力。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "辜鸿铭唯一擅长的就是教外语，别的都是一塌糊涂；他这些所谓“名言”不值得花时间深究。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "传说中牛得威震天的辜鸿铭形象，不过是个纸糊的人偶。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“心中的辫子”恰恰就是非把辜的传说形象维护住不可的冲动背后的脆弱心态。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "以追问“辜鸿铭到底留下什么确切学术成就”开场，质疑其被神化的形象。",
    "以其《论语》首章的英译为样本，批评关键概念“君子”“人不知”“愠”的译法。",
    "指出“十三个博士学位”与“倒读英文镇洋人”两个传说不可信。",
    "下结论：其唯一所长是教外语，形象是“纸糊的人偶”。",
    "最后反转回答提问：所谓“心中的辫子”是维护这一传说形象背后的脆弱心态。"
   ],
   "concept_usage": [
    {"term": "心中的辫子", "meaning": "作者指非把辜鸿铭的传说形象维护住不可的冲动背后的脆弱心态。", "evidence": "P027", "ambiguity": "与编剧台词的原本含义不同，属作者重新定义。"},
    {"term": "君子", "meaning": "《论语》中概念复杂、不宜意译为 wise and good man。", "evidence": "P011", "ambiguity": "作者未给出自认正确的译法。"},
    {"term": "意译", "meaning": "对“君子”“道”这类核心概念的翻译方式；作者主张只要用英语词替代就是错。", "evidence": "P012", "ambiguity": "近乎“不可译”的立场，未给可行替代。"}
   ],
   "examples_and_targets": [
    "电视剧《觉醒年代》编剧借辜鸿铭之口说的台词（被讨论对象）",
    "辜译《论语》“人不知而不愠，不亦君子乎？”（文本证据；见 P009 quote 段）",
    "“十三个博士学位”“倒读英文镇洋人”传说（被反驳对象）",
    "“国际震惊部”（作者对传说的讽刺称呼）"
   ],
   "conditions": [
    "对译文的批评以“《论语》有些认识”的读者为前提。",
    "对“十三个博士学位”的否定以“人类当时寿命”为经验约束。",
    "本文未提供辜鸿铭全部学术成果清单，批评以举证责任在其支持者为隐含前提。"
   ],
   "rhetoric_and_tone": "强烈质疑与讥讽语气；一连串反问（“你们谁能列举一下”“你们谁真的去看过”）；口语化贬抑（“活见鬼的句子”“一塌糊涂”“纸糊的人偶”）；以具体译文逐字批评代替抽象评价。",
   "unresolved_questions": [
    "本篇含 2 个图片节点（IMG001、IMG002），图片未核验，需人工/多模态复核。",
    "IMG001、IMG002 内容不明，无法确定是否为辜译书影或人物图，不能据其补写正文。",
    "“十三个博士学位”真伪、辜译《论语》版本与具体页码需外部文献核查。",
    "P006、P019、P020 等处带有“lexical未覆盖片段”标记，疑为平台加粗/小标题结构混入正文，需核对结构。",
    "作者未给出辜鸿铭学术成就的完整清单，反驳以举证责任分配为策略。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P005", "quote": "辜译《论语》是出了名的自己爱发挥", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P012", "quote": "只要用，就是错", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P014", "quote": "“人不知”，是指人没注意到你吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P018", "quote": "以人类当时的寿命有没有可能是实实在在完成这种成就", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P020", "quote": "人证物证何在", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P022", "quote": "辜鸿铭这人唯一擅长的就是教外语，别的都是一塌糊涂", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P024", "quote": "不过是个纸糊的人偶", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P027", "quote": "恰恰就是这种非把辜的传说形象维护住不可的冲动背后的脆弱心态", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文化批评", "翻译批评", "人物评价"],
   "issue_candidates": ["辜鸿铭形象的神化", "《论语》英译的忠实性", "学术成就的举证", "心中的辫子"],
   "text_function_candidates": ["反驳", "书评/译评", "答问"],
   "object_candidates": ["辜鸿铭", "《论语》英译", "十三个博士学位", "觉醒年代", "心中的辫子"],
   "working_keywords": ["辜鸿铭", "辫子", "论语英译", "君子", "意译", "纸糊的人偶"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 2 个图片节点（IMG001、IMG002），图片内容未经核验，需图像核验；已读部分为正文文本。"
 },
 "eb5a9db0": {
  "analysis": {
   "question_context": "回应提问者关于原画做到当前阶段后如何继续的问题，作者将原画定义为服务后续制作与玩家理解的视觉设计，而非单纯追求画面好看。",
   "content_units": [
    {"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006"],"summary":"好原画要让建模、动画、特效能够准确制作并让玩家不出戏；结构、材质和形状必须清楚，复杂结构需有零件分解图。","role":"definition"},
    {"unit_id":"U002","paragraph_refs":["P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028"],"summary":"角色、道具和场景的细节要有文化根源与合理理由，原画师需积累机械、材料、解剖、生态、服装、兵器和文化史知识，并解释具体结构与使用方式。","role":"reason"},
    {"unit_id":"U003","paragraph_refs":["P029","P030","P031","P032"],"summary":"原画师的高明在于理解制作流程、策划意图和玩家心理；原画是设计表达工作，不必局限于手绘。","role":"claim"},
    {"unit_id":"U004","paragraph_refs":["P033","P034","P035","P036","P037","P038"],"summary":"作者把知识积累置于手绘能力之上，将原画称为视觉编剧工作；手绘需达标但知识匮乏会限制前途，并直接批评提问者基础仍不足。","role":"conclusion"}
   ],
   "main_claims": [
    {"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"好原画的标准是让后续制作流程能够理解和实现，并避免玩家因设计不合理而出戏。","evidence":["E1"]},
    {"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"角色、道具、场景的一切细节都应有文化根源和合理理由。","evidence":["E2"]},
    {"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"原画师首先应具备文化史和艺术批评方面的理解，甚至不必真正会画画。","evidence":["E3"]},
    {"claim_id":"C004","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"做原画最重要的是知识积累，而不是手绘能力。","evidence":["E4"]},
    {"claim_id":"C005","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"原画不是单纯的美术工作，而是视觉编剧工作；手绘达标即可，知识匮乏才会限制前途。","evidence":["E5","E6"]}
   ],
   "argument_steps": ["先以制作团队和玩家的结果定义好原画，再说明结构表达和分解图要求。","随后列举文化史与技术知识如何支撑细节合理性。","最后把原画定位为视觉编剧工作，强调知识积累高于手绘炫技。"],
   "concept_usage": [
    {"term":"原画","meaning":"为后续制作流程准确实现而进行的视觉设计与表达","evidence":"P002"},
    {"term":"文化根源","meaning":"设计细节应能由历史、材料、使用方式等背景解释","evidence":"P007"},
    {"term":"视觉编剧","meaning":"通过视觉方案把设定、结构和故事意图写清楚","evidence":"P034"}
   ],
   "examples_and_targets": ["建模、动画、特效等后续制作组及玩家是评价原画结果的对象。","作者列举皮袍、火铳、双手剑、板甲、马鞍马镫、弓箭和载具散热等结构问题作为知识要求的例子。","末段直接针对提问者的手绘基础作批评。"],
   "conditions": ["复杂组合结构需要零件分解图。","设计细节应能说明文化来源、材料和实际使用理由。","手绘至少要达到能够准确表达设计意图的程度。"],
   "rhetoric_and_tone": "训诫式、直接而带吐槽；大量排比列举技术问题，使用第二人称和口语化的严厉批评。",
   "unresolved_questions": ["文章未给出具体学习路径或阶段性练习计划。","所列技术与历史判断未逐项提供外部来源，需另行核验。"],
   "evidence": [
    {"key":"E1","paragraph_id":"P002","quote":"让建模、动画、特效组做得不骂娘，玩家不翻白眼，才是好原画。","relation":"supports"},
    {"key":"E2","paragraph_id":"P007","quote":"一切细节都要有文化根源，有合理理由。","relation":"supports"},
    {"key":"E3","paragraph_id":"P030","quote":"ta甚至不必真的会画画，而首要的应该是一位文化史学家和艺术批评家。","relation":"supports"},
    {"key":"E4","paragraph_id":"P033","quote":"做原画最重要的是知识积累，不是手绘能力。","relation":"supports"},
    {"key":"E5","paragraph_id":"P034","quote":"原画根本就不是一个美术工作，而是一个视觉编剧工作","relation":"supports"},
    {"key":"E6","paragraph_id":"P037","quote":"手绘达标就可以了，是知识匮乏才使人没有前途！","relation":"supports"}
   ]
  },
  "provisional_tags": {"domain_candidates":["游戏制作","视觉设计"],"issue_candidates":["原画能力结构","知识积累与手绘"],"text_function_candidates":["方法说明","训诫"],"object_candidates":["原画师","游戏美术流程"],"working_keywords":["原画","视觉编剧","文化史","结构合理"]},
  "notes": "文章无图片；技术例证主要用于说明作者的能力标准，未独立核验其事实准确性。"
 },
 "669447b3": {
  "analysis": {
   "question_context": "回应提问者关于如何合适地赞美一个人的问题；作者不提供赞美技巧，而是把称赞改写为对事实的陈述。",
   "content_units": [
    {"unit_id":"U001","paragraph_refs":["P001","P002","P003"],"summary":"作者说自己从不赞美人，称一个人做得不错是因为那是事实。","role":"claim"},
    {"unit_id":"U002","paragraph_refs":["P004","P005","P006","P007"],"summary":"列出做得很好、很美、很善良、很努力等具体评价作为事实陈述的例子。","role":"example"},
    {"unit_id":"U003","paragraph_refs":["P008","P009","P010"],"summary":"再次强调读者知道作者不赞美人，作者只讲事实。","role":"conclusion"}
   ],
   "main_claims": [
    {"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者自称从不赞美人。","evidence":["E1"]},
    {"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"当作者说一个人做得不错时，依据是这符合事实。","evidence":["E2"]},
    {"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者把自己的表达定位为只讲事实，而不是赞美。","evidence":["E3"]}
   ],
   "argument_steps": ["先否定自己在进行赞美，再把正面评价的依据限定为事实。","列举四种具体评价作为例子。","结尾重复只讲事实的自我定位。"],
   "concept_usage": [{"term":"赞美","meaning":"带有主观抬高意味的评价，作者明确否认自己采用这一方式","evidence":"P001"},{"term":"事实","meaning":"作者认为足以支持正面评价的客观依据","evidence":"P003"}],
   "examples_and_targets": ["做得很好、很美、很善良、很努力是作者列举的评价句式。"],
   "conditions": ["正面评价只有在作者认为其为事实时才会说出。"],
   "rhetoric_and_tone": "极短句、重复和排比构成的冷静自述，带有刻意澄清和轻微反讽。",
   "unresolved_questions": ["作者没有说明如何验证‘事实’，也没有给出一般性的赞美方法。"],
   "evidence": [
    {"key":"E1","paragraph_id":"P001","quote":"我从不赞美人。","relation":"supports"},
    {"key":"E2","paragraph_id":"P003","quote":"那是因为这是事实。","relation":"supports"},
    {"key":"E3","paragraph_id":"P010","quote":"我只讲事实。","relation":"supports"}
   ]
  },
  "provisional_tags": {"domain_candidates":["人际表达"],"issue_candidates":["赞美与事实"],"text_function_candidates":["短答","自我定位"],"object_candidates":["赞美者","被评价者"],"working_keywords":["赞美","事实","评价"]},
  "notes": "篇幅很短；回答采取反向定义，没有展开操作性建议。"
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
