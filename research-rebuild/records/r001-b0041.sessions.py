# -*- coding: utf-8 -*-
"""批次 r001-b0041 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0041.sessions.py            # 写 out/r001-b0041.out.jsonl
  python3 records/r001-b0041.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0041"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0041.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "cbfe5527": {
  "analysis": {
   "question_context": "提问者（Q001）问“做好计划还是顺其自然？”。作者不直接二选一，而是先承认做计划不错、问题在于多数人缺少必要的技术准备（P001），把通常所谓的计划判为“计划家家酒”（P002-P003），再用军队与实验室两个范例（P008-P011）说明好计划来自对可靠要素的综合运用（P013-P018），进而提出以SOP为基石的技术标准（P019-P042），最后把SOP落到中国人的单字功夫与个人基本功上（P043-P070）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "立论：做计划不错，但多数人缺少技术准备；把只在脑中设想步骤、写下步骤或分解愿望的做法判为“计划家家酒”，不算计划。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "方法前提 learn from the best：向最上心、最拼命、失败代价最大的人学；据此选定军队（做不成损失最大）与实验室（执行最好）两个观察窗口。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "两家的共同原则：计划必须是对已知可靠要素的综合运用；计划前先做大量工作造出结实的“砖块”，如军队以规范训练与反复测试取得战术动作的可靠数据。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "可靠性原理：计划必须由千锤百炼的SOP构成；计划可靠性等于关键路径上各步骤可靠性的乘积，并以四个关键步骤各80%得40.96%为例说明；SOP化后可保证95%以上可靠性。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028"], "summary": "把标准提高到六西格玛（百万分之三点四失误），并算出需两千多个六西格玛SOP才有约99.3%准时交付；以走路上学由两千个标准sop串联而成回应“怎么可能办得到”。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P029", "P030", "P031"], "summary": "结论一：没有SOP及其可靠性就没有资格做计划；普通人做计划只是过家家，因为其计划由未经严格训练测试的“无定形任务”组成，因而没有制定计划的基础。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040"], "summary": "SOP的六项要求：基于基本原理、极尽合理、界定清晰、经过充分测试、健壮（低标准高抗干扰）、高度自觉（内置纠错与质检机制），并逐项给出理由。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P041", "P042"], "summary": "指出另有一个SOP开发设计的实例（公开演示，仍在进行中）：如何才能做出一碗美味的蛋羹；本篇未展开其内容。", "role": "transition"},
    {"unit_id": "U009", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047"], "summary": "SOP的练习要求：视作最重要的个人资产反复强化，直到如呼吸般自然、执行时不消耗心力与压力；对SOP掌握的牢固深刻程度就是基本功。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055"], "summary": "计划失败的病根是步骤抗干扰能力差；须把计划归化为大量SOP加少量临时过程的组合，并以轨道交通与站点间步行骑车打车的类比说明刚柔并济的分工。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P056", "P057", "P058", "P059", "P060", "P061"], "summary": "效能与SOP数量相关；中文单字动词已把SOP划分内化，每个单字都是一门被几千年历史提纯的功夫，占住一个字足以立足，占住三四个乃至八到十个字足以开宗立派。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070"], "summary": "以“吹／描／刺”等字连问读者功夫是否到家，收束为三段式结论：没有SOP就没有功夫、没有功夫没有资格做计划、没有计划人生必败，要读者自己掂量。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为做计划是不错的，但问题在于很多人缺少做计划所必要的技术准备。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定只在脑中设想步骤写下、或把愿望分解一下的做法不能叫“计划”，只能叫“计划家家酒”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出做事的基本原则是 learn from the best：向对这件事最上心、最拼命、做不好会饿肚子甚至会死的人学，其次向成绩最好的好手学。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为军队是最在乎计划、做不成损失最大的，实验室是计划执行得最好最完美的，因此二者是观察好计划的最好窗口。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出军队与实验室做计划的原则是：计划必须是对已知可靠要素的综合运用，做计划前先造出足够结实的“砖块”。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为计划若不是由千锤百炼的SOP构建而成就谈不上可靠性；计划的可靠性完全由关键路径上步骤可靠性的乘积决定。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者假设一个计划由六个任务组成、四个在关键路径上且各自准时可能性80%，则准时交付可能性为0.8^4=40.96%，有六成机会延迟；而经反复测试的SOP可保证95%以上可靠性。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称现代商业实践要求六西格玛的可靠性，即只允许百万分之三点四的失误，需两千多个六西格玛SOP组成的计划才能有约99.3%的准时交付概率。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以徒步上学为例，称那是由两千个标准sop首尾相连而成的计划，用以说明高可靠性SOP组合并非不可能。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定：没有SOP、没有SOP的可靠性就没有资格做计划；一般人的计划只是过家家，因其由未经严格训练测试的“无定形任务”组成，根本没有制定计划的基础。", "evidence": ["E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出SOP的定义：不是按时间顺序排列的操作说明，而是基于基本原理的、极尽合理的、界定清晰的、经过充分测试的、健壮的、高度自觉的系统化方法。", "evidence": ["E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求SOP每一步都有原理支持，否则可能实际无效、不能达成目标，其余一切也就枉然。", "evidence": ["E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求SOP界定清晰：每一步的起止、交付物、副产物与步骤归属都应有明确定义。", "evidence": ["E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为决定SOP真实设计品质的是测试结果，而不是自觉完美的计算；SOP应有高容错性与抗干扰性，步骤难度应低于一般人经简单训练即可达到的水准，此即健壮性。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者解释“高度自觉”：SOP中应安排便捷有效的排错机制与关键节点质检措施，使失误能被察觉、及时纠正，并让执行人对进度与质量细节保持觉察。", "evidence": ["E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议SOP一旦设计好就视作最重要的个人资产反复练习强化，直到掌握一切变通与细节、能如呼吸般自然执行。", "evidence": ["E27", "E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为执行SOP应是不消耗心力、不紧张、无压力的轻松体验，并以刷牙洗脸为例。", "evidence": ["E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为计划总是不能如愿执行的根本要害在于步骤的抗干扰能力太差，每步偏差积累就会使计划完全失败。", "evidence": ["E30", "E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张把计划归化为大量SOP与少量临时过程的组合，以轨道交通与站点间步行、骑车、打车的类比说明：SOP坚硬可靠、临时环节柔软灵活，计划才能刚柔并济。", "evidence": ["E32", "E33", "E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为一个人的效能几乎完全看ta身上有多少可靠的SOP可用。", "evidence": ["E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称中国人有特殊文化优势：SOP的划分已在语言中内化，每一个单字动词都是一门被几千年历史识别提纯的SOP，占住一个字即可在人间立足，占住三四个乃至八到十个字足够开宗立派。", "evidence": ["E36", "E37", "E38"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以三段式作结：没有SOP就没有功夫，没有功夫没有资格做计划，没有计划你人生必败。", "evidence": ["E39", "E40", "E41"]}
   ],
   "argument_steps": [
    "承认做计划不错，但把问题定位为技术准备不足（P001）。",
    "否定流行的“计划”做法，判为计划家家酒（P002-P003）。",
    "提出 learn from the best 的取材原则（P005-P006）。",
    "按该原则选定军队与实验室两个范例，分别说明其失败代价与执行水平（P007-P011）。",
    "抽出两家的共同原则：计划是对已知可靠要素的综合运用，须先造“砖块”（P012-P018）。",
    "引入SOP，并以可靠性乘积公式与数值例子量化计划可靠性（P019-P022）。",
    "把标准提高到六西格玛并用走路上学作反直觉例证（P023-P028）。",
    "得出“没有SOP就没有资格做计划”的结论（P029-P031）。",
    "给出SOP的六项要求并逐项解释（P032-P040）。",
    "指出另有一篇蛋羹SOP实例，本篇不展开（P041-P042）。",
    "说明SOP的练习方式与掌握程度即基本功（P043-P047）。",
    "用抗干扰能力解释计划失败，并提出SOP加临时过程的组合与交通类比（P048-P055）。",
    "把SOP数量与个人效能挂钩，转入中文单字功夫的文化优势（P056-P061）。",
    "以连问检验读者功夫，收束为三重结论式断语（P062-P070）。"
   ],
   "concept_usage": [
    {"term": "SOP", "meaning": "作者定义为基于基本原理、极尽合理、界定清晰、经过充分测试、健壮、高度自觉的系统化方法，而非按时间顺序排列的操作说明", "evidence": "P032", "ambiguity": "与“流程”“清单”“习惯”的边界未逐项界定"},
    {"term": "计划家家酒", "meaning": "作者对仅在脑中设想步骤、写下步骤或分解愿望这类做法的贬称", "evidence": "P003", "ambiguity": "未给出从“家家酒”过渡到合格计划的完整判据"},
    {"term": "砖块", "meaning": "计划所依赖的、事先通过训练与测试取得的可靠要素与数据", "evidence": "P014", "ambiguity": "比喻与SOP的关系只在后文被等价使用"},
    {"term": "关键路径", "meaning": "由延迟就会影响计划交付的事件首尾相连形成的事件路径", "evidence": "P020", "ambiguity": "定义随文给出，未展开计算方法"},
    {"term": "六西格玛", "meaning": "作者引作现代商业实践的可靠性要求，即只允许百万分之三点四的失误", "evidence": "P023-P024", "ambiguity": "与统计学六西格玛的原义关系未说明"},
    {"term": "健壮性", "meaning": "低标准、高抗干扰的设计特性", "evidence": "P039", "ambiguity": "“低标准”的具体门槛未量化"},
    {"term": "高度自觉", "meaning": "SOP内置排错与质检机制，使失误可被察觉纠正、执行人保持觉察", "evidence": "P040", "ambiguity": "与“自动化监控”的区别未说明"},
    {"term": "临时过程／胶水环节", "meaning": "无法SOP化的灵活机变环节，需投入机动时间、预算与违约预备金", "evidence": "P050-P055", "ambiguity": "如何判定某环节不可SOP化未给出标准"}
   ],
   "examples_and_targets": [
    "军队：作者用作“对计划最在乎、损失最大”的范例，并举师级人力、机动性、油料、弹药、火力、生存力及六小时空中机动等训练细节（P008、P014-P016）。",
    "实验室：作者用作“计划执行最好、最完美”的范例，理由是实验计划出漏洞则几年人力经费打水漂（P010）。",
    "冷天试、热天试、大风天试、大雨天试、大雪天试：军队测试条件的举例（P016）。",
    "总参谋部的侧翼牵制计划：作者举出的计划样式示例（P016）。",
    "徒步上学、刷牙洗脸：作者举出的日常高可靠性SOP类比（P027、P046）。",
    "蛋羹SOP实例：作者称另有公开演示且仍在进行中，本篇只出现标题（P041-P042）。",
    "地铁、高铁等轨道交通与站点间步行、骑车、打车：作者用于说明SOP与临时过程的类比（P051）。",
    "吹、拉、弹、念、做、打、说、学、逗、唱、描、摹、写、画、洗、染、编、织、切、割、斩、剁、蒸、炒、煮、炸、烹、炙、腌、渍、刺、扫、劈、卸、勾、挂、投、缠、雕、钻、刻、划、测、算、计、谋、骑、射：作者列举的中文单字动词功夫（P059）。",
    "“计划家家酒”“无定形任务”：作者自造的说法，属修辞材料（P003、P029）。"
   ],
   "conditions": [
    "数值推演以“假设一个计划由六个任务组成”“它们每个的准时可能性是80%”等条件句给出（P021）。",
    "SOP的可行性被限定在测试与训练条件成立的前提下（P037-P038）。",
    "灵活机变环节的前提是把一切能SOP化的环节先SOP化（P055）。",
    "“六西格玛”标准被作者表述为现代商业实践的要求，而非所有计划的普遍门槛（P023）。",
    "结论用“没有……就没有……”的全称否定句式，未附加例外（P067-P069）。"
   ],
   "rhetoric_and_tone": "讲授与训诫混合：用“同志们”“请你仔细想一下”“看到问题所在了吗”“看懂这事的发展方向没有”等呼告与设问推进；大量军队与工程的量化细节造成权威感；末尾转入“叫你吹，你气力悠长吗”式连问，语气转为质问与激励，并以“自己掂量一下应该怎么做吧”收束；对普通人的计划用“过家家”“无定形任务”等贬称。",
   "unresolved_questions": [
    "P042（“如何才能做出一碗美味的蛋羹？”）在 lexical 结构中标注为未覆盖片段，正文与结构存在一处不一致，且该SOP实例的内容不在本篇，需查其外链或后续文章。",
    "“计划家家酒”与合格计划之间的门槛（SOP数量、可靠性下限）正文只给举例，未给统一判据。",
    "六西格玛（百万分之三点四）与统计学原义的对应关系、以及“两千多个SOP约99.3%”的算式未列出，属待核算。",
    "“一个人的效能几乎完全看ta身上有多少可靠的SOP可用”为作者断言，未给出经验依据。",
    "中文单字动词等于SOP、以及“占住一个字即可立足”的说法未给出界定的检验标准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "做计划是不错的，但是问题在于很多人缺少做计划所必要的技术准备。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "类似这种都不能叫“计划”，而只能叫做“计划家家酒”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "做事情有一个基本的原则，就是learn from the best。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "想要学什么，就要从对这件事最上心、做得最拼命、做不好就会饿肚子 / 会死的那些人身上去学。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "军队设计的计划执行不了，那是要尸山血海、丧权辱国甚至亡国灭种的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "实验室设计的实验计划要是有逻辑漏洞或者执行困难，等于是几年时间、人力、经费全部打水漂。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "什么叫好的计划？军队和实验室是两个最好的观察窗口。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "他们的原则非常简单——计划必须是对已知可靠要素的综合运用。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "他们在做计划之前，先做了大量的工作使得计划拥有足够结实的“砖块”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P019", "quote": "计划如果不是由千锤百炼的SOP（Standard Operating Procedure）构建而成，是谈不上可靠性的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P020", "quote": "计划的可靠性，完全是由计划关键路径上的步骤的可靠性的乘积决定。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P021", "quote": "那么计划准时交付的可能性就是0.8^4 = 40.96%。有六成机会会延迟交付。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "那么这种风雨无阻日练夜练反复测试的sop，就可以保证95%以上的可靠性。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "同志们，现代商业实践的要求是六西格玛的可靠性。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "这是什么意思？只允许百万分之三点四的失误。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "有两千多个六西格玛SOP组成的计划，才能有大约99.3%的准时交付的概率。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "你每天都办到了——你徒步走去学校上学，哪次失败了？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P029", "quote": "没有SOP，没有SOP的可靠性，就没有资格做计划。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "因为一般人所做的计划常常是由没有严格训练测试的不结实的“无定形任务”组成的。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "SOP并不是一些按照时间顺序排列的操作说明，而必须是一个基于基本原理的、极尽合理的、界定清晰的、经过充分测试的、健壮的、高度自觉的系统化方法。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "SOP的每一个步骤安排、每一个步骤的细节，都应该有足够的原理支持而不能是知其然而不知其所以然的照方抓药。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P035", "quote": "它必须是界定清晰的，每一个步骤从何处起，到何处止，交付什么样的交付物，产生什么样的副产物，都应有充分的定义和准确的界定。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "最终是测试结果——而不是自觉完美的计算——决定着你的SOP的真实设计品质。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "它其中的每一个步骤都并不要求操作者有什么特殊的过人天赋", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P039", "quote": "这种低标准、高抗干扰的设计特性，就称为健壮性。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P040", "quote": "高度自觉，是指SOP中应安排足够的便捷有效的排除错误的机制", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P043", "quote": "SOP一旦设计好了，就要视作最重要的个人资产反复加以练习和强化。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P044", "quote": "直到你掌握它的一切变通、一切细节的原因、一切操作的要点，能如呼吸般自然从容的执行它为止。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P045", "quote": "执行你的SOP，应该是一种完全不消耗心力的轻松的体验，完全不会令你感到任何紧张，也不会感到任何压力。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P048", "quote": "其根本的要害就在于你计划的步骤的抗干扰能力太差。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P049", "quote": "如果你每一步都发生交付时间和交付物的偏差，积累十次你的计划就会完全失败。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P050", "quote": "合理来说，你必须将你的计划归化成为大量的SOP和少量的临时过程的组合。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P051", "quote": "SOP就犹如地铁、高铁这些轨道交通，而那些临时过程就如同在站点与站点之间的步行、骑车和打车过程。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P055", "quote": "SOP是坚硬可靠的，胶水环节是柔软灵活的，于是你的计划才会刚柔并济", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P056", "quote": "坦白说，一个人的效能，几乎完全的看ta身上有多少可靠的SOP可用。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P057", "quote": "其实中国人有一个特殊的文化优势，那就是事实上SOP的划分已经在语言中内化了。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P058", "quote": "在中国，每一个单字的动词，都是一门单独的SOP，是被几千年历史识别提纯的功夫——", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P061", "quote": "真正占住一个字，你已经可以在人间立足，无惧任何竞争。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P067", "quote": "没有SOP，就没有功夫。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P068", "quote": "没有功夫，没有资格做计划。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P069", "quote": "没有计划，你人生必败。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["方法论", "管理与组织", "军事", "科研实践", "技艺与修养"],
   "issue_candidates": ["做计划与顺其自然", "计划可靠性与SOP", "关键路径与可靠性乘积", "六西格玛标准", "中文单字功夫"],
   "text_function_candidates": ["答疑", "方法讲授", "训诫", "经验总结"],
   "object_candidates": ["军队", "实验室", "总参谋部", "一般做计划的人", "中国人"],
   "working_keywords": ["SOP", "计划家家酒", "砖块", "关键路径", "六西格玛", "健壮性", "高度自觉", "临时过程", "learn from the best"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。该篇 lexical 与正文存在 1 处 divergence（P042“如何才能做出一碗美味的蛋羹？”为 lexical 未覆盖片段），已记入 unresolved_questions。brief 在阅读包中截断，仅作导航。"
 },
 "f5cfadcb": {
  "analysis": {
   "question_context": "提问者（Q001）问“政治信仰和宗教信仰有何区别？”。作者不比较两者，而是先判定这两个都是伪概念（P001），给出自己对“信仰”的定义（P002），指出该价值观中已包含某种政治立场（P003），从而否认存在“政治信仰”“宗教信仰”的分类法，并判定该问题本身无意义（P004-P005）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接判定：政治信仰与宗教信仰根本是两个伪概念。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "给出定义：信仰是一个完整的世界观以及从它延伸出来的价值观；这个价值观中包含了某种政治立场。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "推出结论：不存在“政治信仰”“宗教信仰”的分类法；该问题本身无意义，如同问橘子的味道和苹果有什么区别。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定“政治信仰”和“宗教信仰”根本是两个伪概念。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义信仰为一个完整的世界观以及从它延伸出来的价值观，并认为这个价值观中包含了某种政治立场。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认存在“政治信仰”“宗教信仰”的分类法，判定该问题本身无意义。", "evidence": ["E4", "E5"]}
   ],
   "argument_steps": [
    "先给结论：两者都是伪概念（P001）。",
    "给出“信仰”的统一定义：完整世界观及其延伸的价值观（P002）。",
    "指出该价值观必然包含政治立场，故无须另立“政治信仰”一类（P003）。",
    "否定分类法并判定问题无意义，以橘子与苹果的类比作结（P004-P005）。"
   ],
   "concept_usage": [
    {"term": "信仰", "meaning": "一个完整的世界观以及从它延伸出来的价值观", "evidence": "P002", "ambiguity": "定义的覆盖面未讨论，也未说明与信念、意识形态的关系"},
    {"term": "政治信仰／宗教信仰", "meaning": "作者判为伪概念与不存在的分类法", "evidence": "P001、P004", "ambiguity": "未说明日常语境中这两个词各指什么、为何是伪概念"},
    {"term": "政治立场", "meaning": "作者认为已包含在上述价值观之中，因而不构成独立的信仰类型", "evidence": "P003", "ambiguity": "“某种政治立场”的具体含义未展开"}
   ],
   "examples_and_targets": [
    "“橘子的味道和一个苹果有什么区别”：作者用以类比该问题无意义的修辞材料（P005）。",
    "提问者提出的“政治信仰”“宗教信仰”二分：被作者否定的对象（Q001、P001、P004）。"
   ],
   "conditions": [
    "全文为无条件断语，未使用假如、通常、可能等限定语，也未区分不同人群或语境。"
   ],
   "rhetoric_and_tone": "五行短答，先断后释再断；语气斩截（“根本”“根本就不存在”）；以水果类比贬抑提问方式；不对提问者作人身评价，但直接判定问题无意义。",
   "unresolved_questions": [
    "正文未说明“政治信仰”“宗教信仰”这两个词在通常用法中各指什么，也未举例说明为何它们不成立。",
    "作者未讨论“政治立场”与“信仰”是否可能分离，也未给出判定某人有无信仰的标准。",
    "全文仅 111 字，未涉及宗教或政治的任何具体内容，提问所问的“区别”实际未逐项比较。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这根本是两个伪概念。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "信仰就是一个完整的世界观以及从它延伸出来的价值观。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这个价值观中包含了某种政治立场。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "根本就不存在什么“政治信仰”“宗教信仰”的分类法。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这问题本身无意义，犹如在问“橘子的味道和一个苹果有什么区别”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教与信仰", "政治哲学", "概念辨析"],
   "issue_candidates": ["政治信仰与宗教信仰的区别", "信仰的定义", "分类法的成立与否"],
   "text_function_candidates": ["答疑", "概念否定", "短评"],
   "object_candidates": ["提问者", "信仰者", "政治信仰与宗教信仰的概念使用者"],
   "working_keywords": ["伪概念", "世界观", "价值观", "政治立场", "分类法"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。本篇为超短答（111 字）。"
 },
 "c2fe7432": {
  "analysis": {
   "question_context": "提问者（Q001）问“黑人的贫穷究竟是自己造成的，还是别人造成的？”。作者不讨论黑人贫困的实际成因，而是先把问题改写为“答案对谁有意义”：对黑人自己，唯一可用的答案是“是我自己造成的”；随后把该思路推广为一条普遍的责任伦理——对自己命运负责的答案只有“天意”与“原因与我有关”两种，凡把初始行动归于他人者都是注定的loser（P002、P010-P013），最后落到交友与做人的告诫（P018-P022）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "改写问题：对别人也许可有不同答案，但对黑人自己唯一可用的答案是“是我自己造成的”；世界上有意义的答案只有“没办法，是天意”和“原因与我有关”两个。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "对外人的推演：若真关心黑人，研究该问题的唯一方向是“我可以做什么来造成结果的变化”；找不到该做的事，答案就是天意；找得到，事情如此就是因为自己没做这件事。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "把同一推演用于涉事人自身：“我的遭遇是怎么造成的”唯一研究方向是“我可以做什么使结果不同”；找不到任何可造成不同的可能性，就归为天意。作者自述已重复两次。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "普遍化：对自己命运只有两个可能的责任人——天和你；想有出息、配得上追随依靠的人，思维逻辑里不应再允许有别人；把初始行动归结他人者是注定的loser；找得到行动则责任在你，找不到就认命。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "对抱怨的批评：不要指望别人自动变好；即使法律或道德似乎要求对方改变，也不能因此不动用这些武器；不满若未归结为“你可以做什么、何时做”，就是成人最可耻的行为——抱怨；停在可怜状态的是自己。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019"], "summary": "行动建议与铁律：遇到这种人躲远点；“只帮助在自助的人”是做人铁律，要刻进灵魂成为习惯与本能。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022"], "summary": "收益与收束：如此不会缺少好的伴侣与团队；女孩子遇到这类人腿都发软，因为这就是所谓的英勇。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为这个问题对别人也许可以有不同的答案，但对黑人自己，唯一可用的答案是“是我自己造成的”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言世界上有意义的答案只有两个：“没办法，是天意”和“原因与我有关”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为外人若真关心黑人，研究该问题的唯一方向是“我可以做什么来造成结果的变化”；找不到则该事是天意，找得到则该事的现状是因为自己没做这件事。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以“假如你自己本身就是涉事人”把同一逻辑用于自身遭遇：唯一研究方向是“我可以做什么使得结果不同”，这是唯一对你有意义的答案。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为对于你自己的命运只有两个可能的责任人：天和你。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为想有出息、想配得上任何人追随依靠的人，在自己的思维逻辑里不应再允许有别的人。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定凡将改变任何问题所需采取的初始行动归结到他人身上的人，都是注定的loser。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为找得到可采取的行动时改变的责任就在自己，找不到就应当认命。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者反对埋怨别人不自动变好，理由是没有任何人有义务额外花成本自我变化去改善你的生活。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为即使存在某种法律或道德使对方似乎有改变的责任与义务，也不能因此以为自己不需要去运用这些法律或道德武器行动。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定不满若最终没有总结到“你可以做什么、你何时去做”，就是成人能做的最可耻、最让人看不起的行为——抱怨。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为不管多可怜，选择停留在该状态的都是自己。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出做人铁律：遇到这种人躲远点；“只帮助在自助的人”不遵守者如同自寻死路。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者认为把该原则刻成习惯与本能使成本能后，就不会缺少好的伴侣和好的团队。", "evidence": ["E18", "E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称女孩子遇到这类人腿都发软，因为这就是所谓的英勇。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "把提问的归因之争改写为“答案对谁有意义”的问题（P001）。",
    "限定有意义的答案只有天意与原因与我有关两种（P002）。",
    "先对外人推演：唯一研究方向是我能做什么；找不到／找得到分别对应天意与自己的未行动（P003-P005）。",
    "再把同一推演用于涉事人自身（P006-P008）。",
    "归纳为普遍命题：对自己命运只有天和你两个责任人（P010）。",
    "提出身份要求：想被人追随依靠就不允许把别的人放进归因里（P011）。",
    "给出判语：把初始行动归给他人者注定是loser（P012）。",
    "给出二分处理：找得到行动则责任在你，找不到就认命（P013）。",
    "反驳抱怨与等待他人自动改变（P014-P017）。",
    "给出人际行动建议与“只帮助在自助的人”铁律（P018-P019）。",
    "以收益与“英勇”肯定作结（P020-P022）。"
   ],
   "concept_usage": [
    {"term": "有意义的答案", "meaning": "作者按“对谁有意义”而非“事实成因”划分的答案类型，只有“天意”和“原因与我有关”两种", "evidence": "P002", "ambiguity": "作者未否认事实层面可有其他归因，但未说明两类答案与事实的关系"},
    {"term": "天意", "meaning": "在穷尽自身可采取行动之后仍找不到可造成不同之事的归因", "evidence": "P004、P008", "ambiguity": "“实在找不到”的判定标准与穷尽程度未说明"},
    {"term": "loser", "meaning": "作者对把改变问题的初始行动归结到他人身上者的贬称", "evidence": "P012", "ambiguity": "未给出具体判定标准"},
    {"term": "英勇", "meaning": "作者用以肯定承担责任、不抱怨者的说法", "evidence": "P022", "ambiguity": "与通常“英勇”的含义关系未说明"},
    {"term": "只帮助在自助的人", "meaning": "作者称为做人铁律的交友与助人原则", "evidence": "P018", "ambiguity": "“自助”的判定标准未给出"}
   ],
   "examples_and_targets": [
    "黑人及其贫穷：提问者设定的对象；作者只把它当作“对当事者有意义的答案”的例子，未讨论其贫困的实际成因（Q001、P001）。",
    "“自动变得好一点”：作者引述并反对的期待（P014）。",
    "法律或道德武器：作者举例说明即使对方有责任也应自己动用（P015）。",
    "抱怨：作者判为成人最可耻的行为（P016）。",
    "女孩子腿都发软：作者用以说明该类人气质的修辞化叙述（P021）。"
   ],
   "conditions": [
    "核心判断被限定为“对黑人自己”而言，作者明说对别人也许可以有不同的答案（P001）。",
    "外人视角以“真的关心黑人”为前提（P003）。",
    "自身视角以“假如你自己本身就是涉事人”的假设引出（P006）。",
    "“天意”结论以“实在找不到任何一种你做了可以造成不同的可能性的事”为条件（P008）。",
    "法律与道德的让步以“哪怕存在……你也不要以为……”的条件句给出（P015）。"
   ],
   "rhetoric_and_tone": "训诫与裁决口吻：以“你算什么东西？”“找不到你就给我认命”“切记”等命令与斥责句对读者施压；用“注定的loser”“最可耻、最让人看不起”下重判；反复自陈“我已经重复了两次”以强调；结尾用“女孩子遇到这类人腿都发软”作世俗化收束，与前文严厉语气形成落差。",
   "unresolved_questions": [
    "提问问的是黑人贫困的成因（自己造成还是别人造成），正文未讨论任何实际成因、历史或数据，只讨论“对当事者有意义”的答案类型。",
    "作者未说明“对别人也许可以有不同的答案”中“别人”可给出哪些答案，也未说明事实归因与有意义答案的关系。",
    "“实在找不到”任何可造成不同之事的判定标准与穷尽程度未说明，该条件可能决定结论是天意还是自己的责任。",
    "“只帮助在自助的人”中“自助”的判定标准未给出。",
    "把黑人问题与个人责任伦理相衔接的推论是否成立，正文未作论证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个问题，对别人也许可以有不同的答案，但是对黑人自己，唯一可用的答案就是“是我自己造成的”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "世界上有意义的答案只有两个——“没办法，是天意”和“原因与我有关”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果你是外人，真的关心黑人，那么你研究这个问题的唯一方向就是“这里面我可以做什么来造成结果的变化”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你找不到这个可以做的事，那么答案就是“这是天意，我没办法”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你找得到，那么这件事之所以是这样，就是因为你没有做这件事。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "假如你自己本身就是涉事人，那么同样的——“我的这个遭遇是怎么造成的”这个问题，唯一的研究方向就是“我可以做什么使得结果不同”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这是唯一对你有意义的答案。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "这个世界上，对于你自己的命运只有两个可能的责任人，一个是天，一个是你。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "如果你想做一个有出息的，想有一天配得上任何人追随、依靠，那么在你的思维逻辑里，你自己就不应该再允许还有任何别的人。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "凡将改变任何问题所需要采取的初始行动归结到他人身上的人，都是注定的loser。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "如果你找得到你可以采取的行动，改变它的责任就在于你，找不到你就给我认命。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "不要埋怨任何人为什么不可以“自动变得好一点”，以便你可以生活得更轻松一点。", "relation": "contradicts"},
    {"key": "E13", "paragraph_id": "P014", "quote": "凭什么世界上有任何一个人有义务额外花成本自我变化去改善你的生活？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "哪怕存在某种法律或者某种道德，导致对方似乎有这个责任和义务去做这个改变，你也不要以为你不需要去运用这个法律或者道德武器去行动。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P016", "quote": "你对任何事物的不满，如果最终没有总结到你可以做什么、你何时去做，你就是在做这个世界上一个成人能做的最可耻、最让人看不起的行为——抱怨。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "选择停留在这个状态的都是你自己。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "“只帮助在自助的人”是一个做人的铁律，不遵守者如同自寻死路，切记。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "然后你会发现——你不会缺少好的伴侣，也不会缺少好的团队。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "直白告诉你，女孩子遇到这类人腿都发软。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "因为这就是所谓的英勇。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["责任伦理", "社会问题", "为人处世", "心理归因"],
   "issue_candidates": ["黑人贫穷的归因", "自我责任与他人责任", "抱怨与行动", "只帮助在自助的人"],
   "text_function_candidates": ["答疑", "训诫", "劝导", "论辩"],
   "object_candidates": ["黑人", "外人／关心者", "涉事人", "抱怨者", "女孩子", "loser"],
   "working_keywords": ["是我自己造成的", "天意", "原因与我有关", "loser", "抱怨", "只帮助在自助的人", "英勇"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。提问涉及黑人贫困的实际成因，正文未讨论，只讨论“对当事者有意义的答案”，已在 unresolved_questions 标注。"
 },
 "c7a80384": {
  "analysis": {
   "question_context": "提问者（Q001）问“你的好朋友杀了人，向你求救，你会怎么办？”。作者给出明确做法：立刻帮ta找律师，安排在律师陪同下去自首（P001），并声明这不是抖机灵（P002）；随后把重点从“怎么帮”转到“怎样事先避免被这类人选中”：公开表过态、被认知为原则问题上宁死不屈的人，反而会以最健康的状态躲开把朋友当庇护所的人（P003-P012）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接作答：立刻帮朋友找律师，安排其在律师陪同下去自首；并声明这不是抖机灵的话。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"], "summary": "防御机制说明：若他人对你有“特别较真、原则问题宁死不屈”的认知且知道你已公开表态，就躲开了拿你当庇护所的“朋友”；反之，爱在交际场拍胸脯鼓吹义气者所吸引的“兄弟”多缺少原则、认为赚钱最重要、道德都是虚的，其唯一道德是“讲义气”，最容易要跑路，并可能带着“万一你不讲义气，我们就帮你讲义气”的打算投奔你。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009"], "summary": "以“你没听过吕伯奢么？”作典故式质问，未展开典故内容。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "上述认知与表态的保护作用：对方要么已做好自首准备只是来求助，要么只是想找安全庇护所，因你会带来额外暴露风险而不会在一堆“兄弟”里选你。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017"], "summary": "反面对照与告诫：就不会在开门倒茶后才听对方说刚杀了人；有不速之客习惯的人不宜结交；电视剧里的肝胆相照与真实情形不同，对方来之前已做好“最坏打算”，届时你会后悔当年拍胸脯，并追问这样做是否值得；再次强调这不是玩笑。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者回答：好朋友杀了人来求救，应当立刻帮ta找律师，安排ta在律师陪同下去自首，这不是抖机灵的话。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为若他人对你有“特别较真、在原则问题上宁死不屈”的认知，并知道你已经就此问题公开表过态，你其实就已经以最健康的状态躲过了这种杀了人来拿你当庇护所的“朋友”。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者批评在交际场上拍胸脯、鼓吹“够兄弟”“讲义气”的做法：这样容易吃到交易红利，但给红利的“兄弟”往往是做事缺少原则、觉得赚钱最重要、道德都是虚的人。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这类人唯一的道德就是“讲义气”，最容易发生“要跑路”的危险，并会带着“万一你不讲义气，我们就帮你讲义气”的打算来投奔你。", "evidence": ["E6", "E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为前述认知与你“会帮找律师、安排送去自首”的声言会起至关重要的保护作用：真准备自首的只是来求助，只想找庇护所的则不会选你，因为你会带来额外暴露风险。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提醒：有做不速之客习惯的人不宜结交；真实情形不像小说写的那么肝胆相照，对方来之前已做好“最坏打算”。", "evidence": ["E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：即使你确实因为拍胸脯而赚钱（其实未必真赚着），到了那个时候你会觉得值得吗？并再次强调这不是玩笑。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "直接给出处置方案：找律师、陪同自首（P001）。",
    "声明该答案不是修辞性抖机灵（P002）。",
    "提出防御机制：他人对你的原则性认知与你的公开表态会筛掉拿你当庇护所的人（P003）。",
    "反面批评：拍胸脯讲义气招来的“兄弟”缺少原则（P004-P005）。",
    "推演风险：这类人唯一道德是义气，容易跑路，并可能强行要求你讲义气（P006-P008）。",
    "以吕伯奢典故施压（P009）。",
    "说明表态如何把求助者分成“准备自首”和“另寻庇护所”两类（P010-P012）。",
    "以生活化场景与电视剧情对比，追问收益是否值得，并重申不是玩笑（P013-P017）。"
   ],
   "concept_usage": [
    {"term": "讲义气", "meaning": "本文中被批评者自认的唯一道德，指不问原则地为“兄弟”兜底", "evidence": "P006", "ambiguity": "作者未给出自己认可的义气标准"},
    {"term": "庇护所", "meaning": "杀人后寻求藏身与掩护的去处；作者强调真求助与找庇护所的动机不同", "evidence": "P003、P012", "ambiguity": "如何在实际情境中区分两种动机，正文只给出“不会选你”的推断"},
    {"term": "交易红利", "meaning": "因被认为够义气而在交际中获得的好处", "evidence": "P005", "ambiguity": "红利的具体形式与代价未量化"},
    {"term": "不速之客", "meaning": "有不打招呼就登门习惯的人，被作者列为不宜结交", "evidence": "P013", "ambiguity": "与本题情形的关联由读者推断"}
   ],
   "examples_and_targets": [
    "吕伯奢：作者引用的典故式人物，用于警告收留逃难者可能招祸；典故内容正文未展开（P009）。",
    "拍胸脯、鼓吹“够兄弟”“讲义气”：被作者批评的交际行为（P004）。",
    "“万一你不讲义气，我们就帮你讲义气”：作者设想对方可能抱持的打算（P008）。",
    "打开家门、茶都倒好之后才听见“其实，我刚杀了个人，没别的地方去了，住几天就走”：作者举出的典型场景（P013）。",
    "电视剧／小说：作者用以对照真实情形的虚构作品（P014）。",
    "“把自己当年拍胸脯的手砍下来”：修辞性想象（P015）。"
   ],
   "conditions": [
    "防御机制成立的前提是：他人对你有上述认知，并且知道你已经就此问题公开表过态（P003）。",
    "对方行为被作者分为两种可能，用“要么……要么……”给出（P011-P012）。",
    "“有做不速之客的习惯的人，不宜结交”是一条一般化告诫，未附例外（P013）。",
    "关于赚钱的追问以“也许你确实因为那样做而赚钱了——其实实际情况是都未必真赚着了”作让步与保留（P016）。"
   ],
   "rhetoric_and_tone": "格言式短答，先给方案再论防御；用“这不是一句抖机灵的话”“这不是一个玩笑”反复声明严肃性；以“你没听过吕伯奢么？”的反问施加文化与道德压力；用“恨不得把自己当年拍胸脯的手砍下来”的夸张与电视剧对照的讽刺；对读者使用第二人称直接假设情境。",
   "unresolved_questions": [
    "吕伯奢典故的具体内容与版本（如出自《三国演义》的叙述）正文未说明，作者以读者应知为前提，需外部核查。",
    "作者未讨论若朋友未自首、或自己确有法律责任时的处理细节，也未提及法律义务本身。",
    "“交易红利”“其实实际情况是都未必真赚着了”均为无出处的经验判断。",
    "“不会在一堆‘兄弟’里面选择你”是基于风险推理的预测，正文未给出事例。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "当然是立刻帮ta找律师，安排ta在律师陪同下去自首。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这不是一句抖机灵的话。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "在ta人眼里，如果对你有一个“特别较真、在原则问题上宁死不屈”的认知，并且知道你已经就此问题公开表过态，你其实就已经以最健康的状态躲过了这种杀了人来拿你当庇护所的“朋友”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "很多人意识不到这种危险，生怕自己“没人脉”，喜欢在交际场上拍胸脯，鼓吹自己“够兄弟”“讲义气”。", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P005", "quote": "往往也是一些做事缺少原则、觉得“赚钱最重要、道德都是虚的”的人。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "ta们唯一的道德就是“讲义气”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "ta们最容易发生“要跑路”的危险。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "于是有很大可能会带着“万一你不讲义气，我们就帮你讲义气”的打算来“投奔”你。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "这个时候上面说的那个“这人很轴、原则问题宁死不屈”的认知和你所作的“如果是这种情况，我会帮找律师，安排送去自首”的声言就会起到至关重要的保护作用。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "要么ta就已做好自首的准备，只是来找你帮忙。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "要么ta其实只是想寻找安全的庇护所，ta就不会在一堆“兄弟”里面选择你。因为你会给ta带来额外的暴露风险。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "特别提醒你，有做不速之客的习惯的人，不宜结交。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "对方来之前可是做好“最坏打算”的。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "也许你确实因为那样做而赚钱了——其实实际情况是都未必真赚着了——但是到了这个时候，你会觉得值得吗？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "这不是一个玩笑。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["为人处世", "人际风险", "法律与道德"],
   "issue_candidates": ["好友杀人求救如何应对", "义气与原则", "自首与庇护", "择友风险"],
   "text_function_candidates": ["答疑", "劝导", "告诫", "经验总结"],
   "object_candidates": ["好朋友（杀人者）", "律师", "讲江湖义气的“兄弟”", "吕伯奢", "电视剧与小说"],
   "working_keywords": ["找律师", "自首", "讲义气", "庇护所", "拍胸脯", "吕伯奢", "不速之客"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。"
 },
 "b6bafaf0": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待「云南某集团首席执行官和人事总监邮件互怼，裁撤人力资源团队」一事，以及对人力岗位的相关言论？”。作者先判断该企业会比较艰难、信里的推断逻辑不成立（P001-P002），反驳“砍掉也不是过不下去”的部门存废标准（P003-P005），为HR的职能边界辩护（P006-P008），提出CEO对决策负全责、不存在“该骂的建议”的责任伦理（P009-P012），推演骂人者陷入的恶性循环（P013-P017），给出领袖资格的定义（P018-P045），再回到本案批评该CEO并追究董事会与股东的责任（P046-P058），最后落到领导与管理的资格问题（P059-P073）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总体判断：估计这家企业会比较艰难；信里面的推断在逻辑上不成立。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "部门存废标准应是“是不是有比没有好”，而不是“不要它是不是就没法过”；按后者标准可依次裁掉秘书、清洁工、销售，最后总裁裁得只剩自己。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "HR不是战略部门，没有义务思考公司未来策略，甚至不应花这个精力；若HR主动交疫情应对建议书，作者说自己反而会骂；除非CEO给了任务安排，本职应先做好。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "责任伦理：CEO对决策负全部责任，其他人只是给建议，世界上不存在“该骂的建议”；建议质量不高是批准者的责任，要骂只能骂自己；解约还得道歉补偿；不这样承担责任的人不配被认真辅佐；请人帮忙帮得不好不能怪帮手。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017"], "summary": "恶性循环推演：帮得不好就骂人者是比较差的求助者，精兵强将不优先选他，会选他的是更糟糕的人，于是总得到“不可接受的表现”，又狂怒开骂，进一步证明其糟糕，循环恶化。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "领袖资格：领袖在某种意义上就是“让别人不担心帮坏了会被定罪”的人；这就是领袖需要的全部资格认证，不是专业水平或战略高度，而是基本的、钢铁一样的责任伦理。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029"], "summary": "兜底宣言：我话事、我找你帮我、我负全责；工资之外也是我兜底；你放胆大闹天宫、打死玉皇大帝都是我兜底；全世界人都喜欢这个待遇；真正悬在帮手头上的达摩克利斯之剑是“为什么该给你、为什么不给他、为什么明天还该给你”，而不是“惩罚”。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "人才之痛与君臣际会：人才愁的是舞台带着自己无法承受的重量（火箭专家买不起火箭，火箭炸了要他赔就只能放弃理想）；引“君以国士待我，我必以国士报之”，当得了君自有国士来投；当君之法是绝不推卸择人责任；这种人极少，遇见即是君臣际会；两个确信化为强烈乐观与集体意志力，这就是企业灵魂里的那口气。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "护住那口气是领袖最大的责任：有它在企业能扛住差不多任何损失；员工会减薪、放无薪假、离职后仍撑你；由此形成二次锁定——领袖不躲则大家生死与共，领袖躲了把责任推给对方“赔火箭”，就再也不会有下一支火箭。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P046", "P047", "P048"], "summary": "对本案CEO的判断：他的技术性理由是否成立根本不重要，因为他失了礼、破坏了管理伦理，已丧失领袖资格；董事会若不能及时发现并解除其职务，那是活该血本无归。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054"], "summary": "以归谬反驳其“技术分析”：同样几条判据可以套到财务部门（只报数据、不直接赚钱、无非高级填表员、简单操作训练员工即可），那要不要把财务部也裁了；一种法则若出门第一步就碰壁，说明提出者没有基本自省能力、连验算都没做，聪明才智都用在文过饰非、把狂怒装饰成“正义天诛”。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P055", "P056", "P057", "P058"], "summary": "责任要求：该CEO若不立刻下罪己诏，连职业生涯是否有资格继续都成问题；当初投票扶他上去的股东按义理应向其他股东谢罪并主动承担损失；若装糊涂，企业本身有化为乌有的风险，因为会导致董事会丧失原则和荣誉，而没有这两样企业不可能成为伟大的企业。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063", "P064"], "summary": "论“伟大的企业”不是过高要求：只有伟大的企业能薪火相传而不散架；散架则一辈子白忙甚至给下一代挖坑，几个亿也不够两年亏；该CEO寒了“国士”的心（指其他旁观者而非HR）、废了非国士的士气，年度计划必给大耳光；引“周不得亡其鼎，秦不能失其鹿”，称为管理ABC。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P065", "P066", "P067", "P068", "P069"], "summary": "领导与管理的资格论：领导和管理首先不是MBA课教的技能，而是资格；有资格则技能来自炊事班养猪或自学皆可君临天下，无资格则读中欧哈佛北大复旦也是精致的废物；并以“欧洲人可以不懂，作为一个中国人你不懂”质问，称这是三千年血写的常识。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P070", "P071", "P072", "P073"], "summary": "三句收束：你是领袖，一切的错都在你；万方有罪，罪在朕躬；君子死，而冠不免。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者估计这家企业会比较艰难，并判定信里面的推断逻辑不成立。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出部门存废的判准是“是不是有比没有好”，而不是“不要这个部门是不是就没法过了”。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以反证说明该标准会导致荒谬结果：若按“砍掉也过得下去”裁员，秘书、清洁工、销售都能裁，最后裁得只剩总裁自己。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为HR不是战略部门，本来没有义务思考公司未来策略，甚至不应花这个精力；若未经安排就交公司疫情应对建议书，反而该挨骂。", "evidence": ["E6", "E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为CEO对决策负全部责任，其他人只是给建议，世界上根本不存在“该骂的建议”。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为下属建议质量不高是批准其就任者的责任，要骂只能骂自己；解约还需道歉补偿；不这样承担全部应有责任的人，本来就不配被认真辅佐。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为请人帮忙、帮得不好就骂人的人是较差的求助者，精兵强将会不优先选他，会选他的是更糟、眼光更差的人，于是总得到不可接受的表现。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为领袖若不能时时把这条放在心上，不管现在多么辉煌都将是过眼云烟。", "evidence": ["E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义领袖：在某种意义上就是“让别人不担心帮坏了会被定罪”的人；这是领袖需要的全部资格认证，既非专业水平也非战略高度，而是基本的、钢铁一样的责任伦理。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者申明兜底原则：我话事、我找你帮我、我负全责；工资之外也是我兜底；你放胆大闹天宫、打死玉皇大帝都由我兜底。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为真正悬在帮手头上的达摩克利斯之剑，是“为什么该把这份待遇给你、为什么不给他、为什么明天还该给你”，而不是“惩罚”。", "evidence": ["E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出人才之痛在于施展才干所需舞台带着自己无法承受的重量，并举火箭专家买不起火箭、火箭炸了要他赔只能放弃理想为例。", "evidence": ["E23", "E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者引“君以国士待我，我必以国士报之”，认为当得了这个君自有国士来投，而当君之法是宁可打落牙齿和血吞、打死也绝不推卸自己择人的责任。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这种领袖太少、垮一个少一个，一辈子不见得遇到一个；遇见了就是君臣际会，永远挺你到底，因此不能不珍惜。", "evidence": ["E28", "E29"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为领袖最大的责任是护住企业灵魂里的那口气；有这口气在，企业能扛住差不多任何损失，员工会减薪、放无薪假甚至离职后仍继续撑你。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出二次锁定：大家让你不败不朽，你就不该躲责任；领袖不躲则大家生死与共帮你扛，领袖若躲了、把责任推给帮手让其“赔火箭”，那你就再也不会有下一支火箭。", "evidence": ["E33", "E34", "E35"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为以这位CEO的所作所为，其技术性理由是否成立根本不重要：他失了礼、破坏了管理伦理，已经丧失了领袖资格；董事会若不能及时发现并解除其职务，那是活该血本无归。", "evidence": ["E36", "E37", "E38"]},
    {"claim_id": "C018", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以归谬指出其“技术分析”的昏聩：同样的判据每条都能套到财务部门，若成立就要把财务部也整个裁掉，说明提出者没有基本自省能力、连一个验算都没做。", "evidence": ["E39", "E40", "E41"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为该CEO若不立刻下罪己诏，不要说继续担任CEO，连职业生涯是否有资格继续都成问题。", "evidence": ["E42"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为当初投票把他扶上去的股东，按照义理原则有必要出来对其他股东谢罪，主动承担由该CEO造成的损失；若装糊涂避免失去金钱，企业本身将有化为乌有的风险，因为会导致董事会丧失原则和荣誉。", "evidence": ["E43", "E44"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“伟大的企业”不是特别高的要求，而是存续的底线：只有伟大的企业能薪火相传而不散架，散架则一辈子白忙，几个亿也不够两年亏。", "evidence": ["E45", "E46"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为该CEO寒了旁观“国士”们的心、废了非国士的士气，会使战略错误几乎犯定、年度计划必定给一个大耳光。", "evidence": ["E47"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为领导和管理首先不是MBA课里教的技能，而是领导和管理的资格：有资格则技能来自何处皆可君临天下，无资格则名校出身也是精致的废物。", "evidence": ["E48", "E49", "E50"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以三句断语收束：你是领袖，一切的错都在你；万方有罪，罪在朕躬；君子死，而冠不免。", "evidence": ["E51", "E52", "E53"]}
   ],
   "argument_steps": [
    "先下总体判断并否定信中的推断（P001-P002）。",
    "提出部门存废的正确判准，并以连续裁员的归谬反驳原判准（P003-P005）。",
    "为HR辩护：非战略部门不应越界思考公司战略，本职优先（P006-P008）。",
    "确立CEO责任伦理：决策责任全在CEO，不存在该骂的建议（P009-P012）。",
    "推演骂人者导致的求助者恶性循环（P013-P017）。",
    "给出领袖资格定义：让别人不担心帮坏了会被定罪（P018-P021）。",
    "以兜底宣言与达摩克利斯之剑说明帮手为何愿意追随（P022-P029）。",
    "用人才之痛与国士相报说明这种领袖的稀缺与价值（P030-P038）。",
    "说明护住那口气的责任及“二次锁定”机制（P039-P045）。",
    "回到本案：技术理由不重要，失礼与破坏管理伦理已使其丧失资格（P046-P048）。",
    "以财务部门的归谬揭其“技术分析”的昏聩（P049-P054）。",
    "提出罪己诏与股东谢罪的要求，并警告董事会丧失原则的后果（P055-P058）。",
    "论证伟大的企业是存续底线，指出寒心与士气后果（P059-P064）。",
    "把问题提升为领导与管理的资格论，并以三句古语式断语收束（P065-P073）。"
   ],
   "concept_usage": [
    {"term": "领袖／领袖资格", "meaning": "作者定义为让别人不担心帮坏了会被定罪的人；其资格是责任伦理而非专业水平或战略高度", "evidence": "P019-P021", "ambiguity": "与“管理者”“老板”的边界未系统界定"},
    {"term": "国士", "meaning": "有能力、会折服来投并忠诚的人才；作者强调不是特指HR的人", "evidence": "P032、P062", "ambiguity": "判定谁算国士的标准未给出"},
    {"term": "兜底", "meaning": "领袖承担决策与后果的全部责任，包括下属行为造成的损失", "evidence": "P022-P024", "ambiguity": "与法律责任的界限未讨论"},
    {"term": "那口气", "meaning": "由国士的乐观与集体意志力构成的企业灵魂", "evidence": "P037-P039", "ambiguity": "比喻性说法，未给出可观察指标"},
    {"term": "二次锁定", "meaning": "帮手让领袖不败不朽之后，反过来更不允许领袖躲责任", "evidence": "P042", "ambiguity": "该机制如何具体运作未展开"},
    {"term": "达摩克利斯之剑", "meaning": "作者指真正悬在帮手头上的，是“凭什么是你而不是他”的追问，而非惩罚", "evidence": "P029", "ambiguity": "与通常典故含义的差别未说明"},
    {"term": "罪己诏", "meaning": "作者要求该CEO作的公开自我归罪", "evidence": "P055", "ambiguity": "具体形式与范围未说明"},
    {"term": "管理ABC", "meaning": "作者对所引“周不得亡其鼎，秦不能失其鹿”的定性", "evidence": "P063-P064", "ambiguity": "该古语的具体所指由读者推断"}
   ],
   "examples_and_targets": [
    "云南某集团CEO与人事总监的邮件互怼、裁撤人力资源团队：提问者提供的语境；正文未点名公司，也未逐句引用原邮件（Q001、P002、P046）。",
    "秘书、清洁工、销售、财务部：作者用于归谬“砍掉也过得下去”判准的举例（P004、P050）。",
    "火箭专家买不起火箭、火箭炸了要他赔：作者用来说明人才之痛的类比（P030）。",
    "“君以国士待我，我必以国士报之”：作者引用的古语式说法（P032）。",
    "大闹天宫、打死玉皇大帝：作者用来说明兜底的夸张比喻（P024）。",
    "“无非高级填表员”“简单的操作根本不需要专人来做，训练一下员工让他们自己学会填表就可以了”：P050 中带引号的说法，作者将其套用于财务部门；是原信原话还是作者戏拟，正文未说明。",
    "“正义天诛”：作者对被批评者自我正当化措辞的戏拟（P054）。",
    "中欧、哈佛、北大、复旦：作者举出的商学院与高校（P067）。",
    "炊事班养猪、教英语时看网站自学：作者举出的技能来源（P066）。",
    "“周不得亡其鼎，秦不能失其鹿”“万方有罪，罪在朕躬”“君子死，而冠不免”：作者引用的古语（P063、P072、P073）。",
    "“收入急剧下降/家道中落是什么体验”：作者设想其子女将来会在知乎提的问题（P061）。"
   ],
   "conditions": [
    "部门判准被作者表述为应然标准（“而是看是不是有比没有好”）（P003）。",
    "HR的职能边界以“除非我自己给了你这个任务安排”为条件（P008）。",
    "责任伦理被作者限定在他自己任CEO的情形（换了是我、我是CEO）（P007、P009）。",
    "对求助者恶性循环的描述使用“如果你是这样一个……的人”的条件句（P013）。",
    "对本案的批评附带保留：“他的技术性理由是否成立根本不重要”，即以伦理而非技术理由定论（P046）。",
    "对股东的追责以“按照义理原则”为限定，非法律义务（P056）。",
    "“伟大的企业”被作者限定为存续底线而非高要求（P059-P060）。"
   ],
   "rhetoric_and_tone": "论辩与训诫并重：先破后立，用连续归谬（秘书—清洁工—销售—财务部）压对手；大量使用第一人称代言式宣言（“我话事”“我负全责”“你放胆大闹天宫”）；以“听清楚”“记住——”发号施令；对当事人用“惊人的昏聩”“愚…”“蠢蛋”“还有脸大声吼”“精致的废物”等强烈贬语；末段连引三句古语作结，语气转为格言式庄重；整体带有君臣伦理的叙事框架。",
   "unresolved_questions": [
    "正文未点名涉事企业，也未引用原邮件的具体文字；作者的“信里面的推断”只能由提问与转述推知，原邮件内容需外部核查。",
    "P050 中带引号的短语（“无非高级填表员”等）究竟是原信文字还是作者的戏拟，正文未说明，本记录按 unknown 处理，未归给作者或对方。",
    "作者主张的“领袖负全责”与法律责任、公司治理规则之间的关系未讨论；对股东“按照义理原则”谢罪的要求亦未给出依据。",
    "“国士”“那口气”“二次锁定”等说法均为比喻性表述，未给出可检验的判据。",
    "P063“周不得亡其鼎，秦不能失其鹿”与管理的对应关系由作者一句“这是管理ABC”带过，未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "估计这家企业会比较艰难。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "信里面的推断是逻辑不成立的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一个企业里的部门是否应该存在，不是看“不要这个部门是不是就没法过了”，而是看“是不是有比没有好”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "把秘书裁了；没有清洁工，大家动手扫扫地也不是不能过，把清洁工也裁了", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "最后总裁真的是总裁了，裁得只剩自己了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "HR部门又不是战略部门，本来就没有义务去思考公司未来策略，甚至都不应该去花这个精力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "换了是我，现在人力资源部交一份公司应该如何应对疫情的建议书给我，恐怕反而会挨骂。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "除非我自己给了你这个任务安排，否则你该干嘛就该干嘛，干了这些你本职有时间干好吗？", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P009", "quote": "我是CEO，我对做出决策有全部责任，其他人只不过是给建议。世界上根本不存在“该骂的建议”这个概念。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "你是我批准就任的人，你提出来的建议质量不高是我的责任，要骂只能骂我自己。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "我如果不是这样承担全部应有责任的人，本来就不配你认真辅佐。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "自己请了人来帮手，帮得不好就不能怪帮手。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "如果你是这样一个求人帮忙，帮得不好就骂人的人，你就是一个比较差的求助者。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "于是进一步证明你是一个很糟糕的求助者，于是变得更不值得选择", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "身为领袖，这条不能时时刻刻放在心里，不管你现在多么辉煌都将是过眼云烟。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "领袖，在某种意义上说，就是“让别人不担心帮坏了会被定罪”的人。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "这就是一个领袖需要的全部资格认证。既不是什么专业水平，也不是什么战略高度。就是这个基本的、钢铁一样的责任伦理。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "我话事，我找你帮我，我负全责。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "你拿了工资，也是我兜底。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P024", "quote": "我选了你，你放胆大闹天宫。打死了玉皇大帝，都是我兜底。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P027", "quote": "你要回答的是我为什么应该把这份待遇给你？为什么不给他？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P029", "quote": "这才是悬在帮手们头上的达摩克利斯之剑。而不是什么“惩罚”。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P030", "quote": "人才们不愁吃，不愁穿，愁的是施展自己的才干所需要的舞台带着自己无法承受的重量。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P030", "quote": "如果火箭炸了要他赔，他只能放弃火箭的理想。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P032", "quote": "“君以国士待我，我必以国士报之。”", "relation": "context"},
    {"key": "E26", "paragraph_id": "P033", "quote": "你当的了这个君，自有国士来投。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P034", "quote": "就是宁可打落牙齿和血吞、打死也绝不推卸自己择人的责任，然后你才能成为国士们眼里值得拼命保住的明君。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "这种人太少，垮一个少一个。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P035", "quote": "遇见了，就是君臣际会，永远挺你到底。于是自然就不能不珍惜。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P038", "quote": "这就是一个企业灵魂里的那口气。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P039", "quote": "领袖最大的责任，就是护住这口气。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P040", "quote": "企业亏损了，这些人都肯自动减薪甚至放无薪假来撑你。被迫离职了，都会一样继续撑你。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P042", "quote": "而这带来了一个二次锁定——我们让你不败不朽，你还“躲责任？！", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P043", "quote": "领袖不躲，那就大家生死与共，帮你扛，因为值得为你扛。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P045", "quote": "他们“悔改”了，你的火箭倒是不会炸了——因为你再也不会有下一支火箭了。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P046", "quote": "以这位CEO的所作所为，他的技术性理由是否成立根本不重要。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P047", "quote": "他失了礼，破坏了管理伦理，已经丧失了领袖资格。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P048", "quote": "董事会如果不能及时发现、及早解除他的职务，那是活该血本无归。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P050", "quote": "财务部门一样每一条都符合——就是报数据的", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P052", "quote": "要不要把财务部整个裁了？", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P054", "quote": "说明没有基本的自省能力，连一个验算都没做。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P055", "quote": "他如果不立刻下罪己诏，不要说继续担任CEO，连职业生涯是否有资格继续都成问题。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P056", "quote": "董事会里当初投票把他扶上去的那一部分股东，按照义理原则有必要出来对其他股东谢罪，主动提出承担由于这位CEO所造成的损失。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P058", "quote": "没有这两样，一家企业是不可能成为伟大的企业的。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P060", "quote": "错了。只有伟大的企业能薪火相传而不散架。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P061", "quote": "按这个案例的严重程度，几个亿不够两年亏的", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P062", "quote": "而这位CEO寒了“国士”们的心——我指的不是HR的人，而是其他看着这事的人", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P065", "quote": "听清楚——领导和管理，首先根本不是mba课里教的那些技能，而是领导和管理的资格。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P066", "quote": "就算你的技能是在参军时在炊事班养猪时感悟到的，还是在教英语时看网站自己学的，都一样君临天下。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P067", "quote": "没有这个充分的资格，你尽管去读中欧哈佛北大复旦，你一样是个精致的废物。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P071", "quote": "你是领袖，一切的错都在你。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P072", "quote": "万方有罪，罪在朕躬。", "relation": "context"},
    {"key": "E53", "paragraph_id": "P073", "quote": "君子死，而冠不免。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["企业管理", "组织与人事", "领导力与责任伦理", "公共事件评论"],
   "issue_candidates": ["CEO与HR邮件互怼", "裁撤人力资源团队", "部门存废判准", "CEO的责任归属", "领袖资格", "国士与君臣际会", "董事会与股东责任"],
   "text_function_candidates": ["答疑", "评论", "批评", "论辩", "训诫"],
   "object_candidates": ["云南某集团CEO（提问者提出，正文未点名）", "人事总监（提问者提出）", "HR部门", "董事会", "股东", "国士", "人才", "员工"],
   "working_keywords": ["越界", "有比没有好", "该骂的建议", "责任伦理", "兜底", "达摩克利斯之剑", "国士", "那口气", "罪己诏", "管理ABC"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。提问所述企业名、邮件原文均不在正文中；P050 引号内短语的归属按 unknown 处理，未归给作者或对方，已记入 unresolved_questions。"
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
