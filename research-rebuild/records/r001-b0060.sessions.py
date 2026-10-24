# -*- coding: utf-8 -*-
"""批次 r001-b0060 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0060.sessions.py            # 写 out/r001-b0060.out.jsonl
  python3 records/r001-b0060.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0060"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0060.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "987f35d0": {
  "analysis": {
   "question_context": "提问者问“人生而平等吗？”（Q001，属提问者）。作者以自撰长文回应，先界定“平等”在法律上的含义，再逐层检查制度平等能否保证结果平等，最后给出“生而平等”的两个版本与自然法意义上的一种说法。作者立场不等于提问者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "提出“人人平等”概念复杂，给出平等=同等处置的法律定义，并以杀人量刑为例。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013"], "summary": "回应两处质疑（14岁以下不负刑责、妇女保护法与外国人管理），主张对所有人均等的区别对待、以及对等的表决权所形成的偏向性法令仍属平等。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "指出前人／先辈对后人的优势无法消除，并说明100%遗产税与公共抚养两种极端方案不可行，故平等制度并不保证平等结果。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "提出是否用程序不平等修正结果不平等这一问题，并称对该问题的态度构成人类社会的制度分界线。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "叙述第一类立场：只实现程序平等并接受一切结果，以赌局概率均等为类比，被称为资本主义而本质上是古典平等主义。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P033", "P034", "P035", "P036"], "summary": "叙述第二类立场：须消除血缘传承的历史性优势，在均等赌局前均分筹码，甚至重新均分结果。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046"], "summary": "分述两种模式各自的困难：前者有周期性极端不平等导致社会倾覆，后者缺少替代性积极性机制。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051"], "summary": "指出后一模式原则上安排了以神性／利他精神替代利益驱动的激励机制，但需长期培育与文化土壤，过渡期称为“初级阶段”。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057"], "summary": "版本A：在古典平等主义者眼里，人人生而平等是现状，个体落点不同不等于牌局不公平。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P058", "P059", "P060", "P061"], "summary": "版本B：在另一部分人眼里“人人生而平等”仍是追求中的目标，实为“人人理应生而平等”。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P062", "P063", "P064", "P065", "P066", "P067", "P068"], "summary": "补充更先在的观察：人在自然法面前天然平等，并自评此结论未必有实际参考意义。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平等的根本定义是法律上的同等待遇：无论出身、贫富、知识、权位，同样的行为在法律上得到同等处置。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "针对所有人的均等区别对待（如14岁以下一律不负刑事责任）仍然是平等。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "经全体代表民主决议、由对等表决权形成的优待特殊群体的法令，虽结果偏向某些人，但决策权对等，故本质上仍平等。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正无法解决的问题是前人对后人、先辈对后辈的绝对不平等，包括知识、经验与社会关系的继承优势。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会不可能实行100%遗产税与子女完全公共抚养，故上述历史性不平等是死结。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "制度在程序上无论多么平等，其结果在实践中也无法平等；即便一切归零，三四代内也会沿血缘代际重新分层且一代比一代严重。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是否用程序的不平等修正结果的不平等，是人类社会的制度分界线，对这一问题的态度将人类社会分为两类。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "第一类（作者称“古典平等主义”／资本主义）认为只须实现程序平等并接受由此造成的一切现状与未来，只要程序平等，结果再悬殊也应认定为平等。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "第二类认为必须消除血缘传承的历史性优势对程序平等机制的影响：不抛弃平等程序，而是在入场前均分筹码，甚至重新均分已定的结果。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "两种模式各有困难：前者会出现周期性极端不平等并导致社会倾覆，被逼到绝境者将转向弱肉强食的自然法则自救。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "后一模式原则上以人天生神性经长期打磨养护替代利益驱动为激励安排，但需长期培育并维持文化土壤，至少逻辑上可行，难在旧引擎已关、新引擎未起的过渡期。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“人人生而平等”有两个版本：版本A视其为现状（人人已经生而平等），版本B视其为仍在追求的目标（人人理应生而平等），后者尚需漫长摸索。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在自然法面前人人天然平等（万有引力、死亡、硫酸与雨水不区分贫富），故从这个意义上也可以说人生而平等；但作者自评这类结论未必有实际参考意义。", "evidence": ["E18", "E19"]}
   ],
   "argument_steps": [
    "定义：先把平等限定为法律上的同等待遇，弱化提问中“生而”的字面含义。",
    "以杀人量刑为例说明法庭不看被告的财富与地位。",
    "预设质疑一（14岁以下无刑责）→ 答：对所有人均等的区别对待仍是平等。",
    "预设质疑二（妇女保护法、外国人管理条例）→ 答：对等表决权形成的集体意志，属被决定的不平等，本质仍平等。",
    "转折：真正解决不了的是前人对后人的绝对不平等（法律由前人制定、18岁前无投票权、继承优势）。",
    "以100%遗产税会被规避、强行公共抚养的推行者已不存在，论证死结不可解。",
    "引出制度分界线之问：是否以程序不平等修正结果不平等。",
    "第一类立场：只认程序平等，以赌局概率均等为类比，程序平等则结果无论多悬殊都算平等。",
    "第二类立场：保留平等程序，但在入场前均分筹码，并在结果落定后重新均分。",
    "让步式并列：两种模式各有困难——前者周期性倾覆，后者缺替代性激励。",
    "对后者的补充：原则上以神性与利他精神替代利益驱动，需长期文化土壤，并把它与“初级阶段”相连。",
    "结论式收束：给出“生而平等”的版本A与版本B。",
    "追加更先在的观察：自然法面前天然平等，同时自我限缩其参考意义。"
   ],
   "concept_usage": [
    {"term": "平等", "meaning": "本文首先指法律上的同等待遇（同等行为同等处置），后扩展为程序平等、结果平等与自然法平等三层用法。", "evidence": "P002", "ambiguity": "同一词在文中跨法律、制度、自然法三层使用，作者未系统区分，易生歧义。"},
    {"term": "程序平等／结果平等", "meaning": "程序平等指规则与概率对等；结果平等指实际分配状态，作者称后者在实践中无法达到。", "evidence": "P025", "ambiguity": "“结果无法平等”与“结果应否被修正”被作者分开处理。"},
    {"term": "自然法／自然法则", "meaning": "两处用法不同：自然法指万有引力、死亡等不因人而异的规律（P063-P066）；自然法则指弱肉强食的自我救济（P039）。", "evidence": "P039", "ambiguity": "同词两义，读者可能混淆，作者未说明二者关系。"},
    {"term": "古典平等主义", "meaning": "作者对只认程序平等一类立场的命名，并称其经济学实践为资本主义，但强调资本主义只是其行为表现而非本质。", "evidence": "P032", "ambiguity": "属作者自定术语，与常见政治学用法是否一致需外部核查。"},
    {"term": "初级阶段", "meaning": "指旧激励机制已关闭、新机制尚未爬升、且面临外部敌意竞争的困难过渡期。", "evidence": "P051", "ambiguity": "作者以“所谓的”加引号使用，未指明具体所指对象的完整定义。"},
    {"term": "被决定的不平等", "meaning": "指因对等表决权而形成的、结果偏向某群体的法令，作者认为其本质上仍属平等。", "evidence": "P013", "ambiguity": "“理论上”对等的决策权与实际影响力之间的差距，作者以“理论上、逻辑上”自我限定。"}
   ],
   "examples_and_targets": [
    "杀人判无期徒刑的假想案例与第AZS354320号被告：作者例证，说明法律同等待遇不看贫富地位（P003、P004）。",
    "14岁以下杀人无刑事责任：作为预设质疑被作者回应，属被反驳的质疑（P007-P009）。",
    "妇女保护法与外国人管理条例：作为预设质疑被作者回应（P010-P013）。",
    "100%遗产税被以“亏损交易”形式规避、把子女交公家统一抚养的“公共后代”：作者反例，论证死结不可解（P019、P020）。",
    "面临重大社会变革的国家“大清盘、一切归零”：作者例证，说明三四代内重新分层（P023）。",
    "赌博下注赌大小、均分筹码、重新分配筹码：作者类比，贯穿两类立场的说明（P031、P034-P036、P044）。",
    "“今亡亦死，举大事亦死，等死，死国可乎？”：引用句（出自史书，本文未注明出处），用于描述绝境者的自救转向（P041）。"
   ],
   "conditions": [
    "平等定义以“只要你做出同样的行为，在法律上你会得到同等的处置”为前提（P002）。",
    "区别对待仍属平等，条件是它“针对所有人均等”（P009）。",
    "优待性法令仍属平等，条件是其经全体代表民主决议、且表决权在理论上对等（P012、P013）。",
    "“结果无法平等”的判断以遗产税与公共抚养两条路都不可行为条件（P018-P020）。",
    "重新分层“不过三四代人”是作者给出的时间尺度估计（P023）。",
    "后一模式的激励替代“需要长期的培育和养护”、需维持文化土壤，作者称其只是“至少逻辑上”通（P047-P049）。",
    "自然法平等的说法以万有引力、大脑缺氧、硫酸与雨水等情形为限（P064-P066），且作者称其未必有实际参考意义（P068）。"
   ],
   "rhetoric_and_tone": "论说体为主，语气克制而带训诫与冷峻的现实主义。大量使用反问与自设问答（“有人问”“那么又有人问”“难道不是专门偏向妇女的吗？”）推进。以赌局、赌大小为主要比喻，以“死结”“前情提要”“版本A／版本B”作结构标记。末尾以第二人称“你”泛称读者，用“敬酒不吃，你们就吃罚酒”等俗语渲染绝境者口吻，并自评结论“未必具有实际的参考意义”，带自我限缩的反讽。整体不点名具体国家或学派，以“两类”“一部分人”抽象处理。",
   "unresolved_questions": [
    "Q001的提问者是否期待特定答案，正文未回应提问者的任何附加预设，仅自设问题。",
    "“资本主义”与“古典平等主义”的对应关系是作者自定用法，是否符合学术通行定义需外部核查（P032）。",
    "“推行这政策的实体目前似乎没有活着的了”与“面临过重大社会变革的国家”未点名，无法确定所指历史对象，需外部核查（P020、P023）。",
    "P041引文出处未标注（“今亡亦死，举大事亦死，等死，死国可乎？”），需外部核查。",
    "作者对两类立场是否有所倾向，正文未明说；末段自评“未必具有实际的参考意义”令结论强度不明。",
    "“神性”“利他精神”“献身的神性享乐”等表述未作定义，其可验证性存疑（P047）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "只要你做出同样的行为，在法律上你会得到同等的处置", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P006", "quote": "这个就叫做法律上的同等待遇，也就是平等的根本定义。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P009", "quote": "这种区别对待，实际上是针对所有人均等的区别对待。于是仍然是平等的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P013", "quote": "因为这个决策权理论上是对等的，所以它仍然属于平等的被决定的不平等", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P016", "quote": "他人从自己的先辈处继承下来的优势，尤其是知识的、经验的、社会关系的优势解决不了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P018", "quote": "因为人类社会不可能宣布100%的遗产税和子女完全公共抚养。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P023", "quote": "不过三四代人，就会重新出现沿着血缘代际积累而形成的明显的分层。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P028", "quote": "是对这个问题的态度，将人类社会分成了两类。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P029", "quote": "一类是认定人类应该仅仅实现程序的平等而接受因此造成的一切现状和未来。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P031", "quote": "只要程序是平等的，则结果无论多么悬殊，都必须被认定为平等的", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P034", "quote": "而是要在机会均等的赌局之前，还要均分筹码，确保每个人入局时筹码一样。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P038", "quote": "前者存在周期性的极端不平等导致的社会倾覆。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P039", "quote": "没有饭吃、没有衣穿的人们都将转向自然法则", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P047", "quote": "人类天生拥有的神性可以经过长期的打磨和养护发挥出来", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P049", "quote": "问题只是怎么度过这一场旧的引擎已经关闭，而新的引擎转速还没有爬升起来的时期？", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P057", "quote": "所以，人人已经生而平等。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P058", "quote": "“人人生而平等”仍然是一个正在追求的远大目标", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P063", "quote": "实际上，每个人在自然法面前是天然平等的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P068", "quote": "这样的结论未必具有实际的参考意义。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学", "法理学", "社会理论"],
   "issue_candidates": ["平等概念辨析", "程序平等与结果平等", "代际继承优势", "遗产税与公共抚养", "再分配与激励机制"],
   "text_function_candidates": ["答疑", "论辩", "概念解释"],
   "object_candidates": ["资本主义", "古典平等主义", "14岁以下未成年人", "妇女", "外国人", "面临重大社会变革的国家"],
   "working_keywords": ["生而平等", "同等待遇", "程序平等", "结果平等", "遗产税", "公共后代", "自然法", "初级阶段", "筹码"]
  },
  "notes": "无图片节点（图片节点 0），正文与 lexical 结构均为 paragraph，无版本差异（provenance/superseded 为 null）。提问（Q001「人生而平等吗？」）仅作为语境，其立场未归给作者。P041 引文出处原文未标注；P020、P023 所指历史对象未点名，均已登记为待外部核查。"
 },
 "ae55535c": {
  "analysis": {
   "question_context": "提问者预设“把土地分给三分之一的人，其他人从事工商业这样对国家好处更大”，据此问古代中国为何抑商（Q001，属提问者，作者未接受该预设）。作者以自撰答文回应：先重定义“商”，再说明抑商的真实目的与相关文献的可靠性问题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出重农抑商之问，并主张先要搞清古代“商”指什么。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "论述春秋战国的商是装备精良的职业武装力量，有防御与二次报复能力，并以山贼跪迎、给“养路钱”的场面加以渲染。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P018", "P019", "P020"], "summary": "说明掌握沿途运输武力后，可把本地废物远运换取黄金、奴隶、特许状等，并用于造更多刀甲、聚更多人。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P021", "P022"], "summary": "归结为海商即海盗、陆商即私军；此种力量在君主未建成绝对控制前只能由国君自己掌握。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "反问“岂有不抑商之说”，指商多为王弟王叔、左丞相右将军乃至国君“仲父”。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P027", "P028"], "summary": "核心结论：抑商根本不是为了重农，而是为了尊王；重农之说只是遮掩，跟随此说者被骗。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033"], "summary": "以商鞅五马分尸、商朝以刻满吃人图案的大火锅出名，反问“商人”在战国人眼中是何形象。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P034", "P035", "P036", "P037"], "summary": "方法论主张：历史文献基本上是盗贼指示专业骗子写的，只有不慎处才说实话，须像审赌场老千一样交叉盘问。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P038", "P039", "P040", "P041"], "summary": "回应“有名商人没几个、也没多大武装力量”的质疑，列出信陵君等一长串人物，让读者去查其生意与部众规模。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论抑商必须先搞清古代“商”指什么，不能按后世的商贩形象理解。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "春秋战国时代的商是装备精良的职业武装力量，否则无法在当时的条件下送货并携款返回。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "商队不仅保有足够防御能力，还具备确保惩戒的二次报复能力，使沿途武力设伏暗算也得不偿失。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "商队武力至少要到“快速机动混成装甲特战旅”的水平，否则不是经商而是送货上门的献爱心活动。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "掌握运输武力后，可把本地废物运往各地换取黄金、美女、奴隶、特许状、荣誉官职等，并用以扩充刀甲与人手。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "海商即海盗，陆商即私军；在国君未成就霸业、未建立“一翻手就能连根拔起”的控制前，这种力量当然必须由国君自己做。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "商人多是王弟王叔、左丞相右将军，甚至是国君的“仲父”，所以抑商根本不是为了重农，而是为了尊王。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "重农只是含糊的遮掩之辞；凡跟着讲重农如何重要、商业如何抢占农业人口资源的人，都是被一并骗了。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "反问式论证：商鞅被五马分尸并非因为“太爱好农业”；商朝以刻满吃人图案的大火锅出名，可知“商人”在战国人眼中的形象。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "历史文献基本上可看作盗贼指示专业骗子写的，只在不慎处说真话，须以审讯赌场老千的方式交叉比对才能得到真相。", "evidence": ["E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "针对“有名商人没几个、也没听说有大多武装力量”的质疑，作者列出信陵君、平原君、春申君、孟尝君、吴起、刘濞、张士诚、曾国藩、李鸿章、袁世凯、张作霖等人物，要求查其生意与部众规模。", "evidence": ["E17", "E18"]}
   ],
   "argument_steps": [
    "承接提问，先不回答重农抑商本身，而要求先界定古代“商”的实际形态。",
    "给出正面论断：商即装备精良的职业武装力量，理由是春秋战国的运输安全条件。",
    "以“你还想走暗镖不成”与前哨举旗渲染商队的排场。",
    "强调商队具备防御与二次报复能力，令设伏者得不能偿失。",
    "以山贼主动跪迎、缴纳“养路钱”的场景说明商队的实际威势。",
    "反面推论：达不到此水平就不是经商，而是献爱心。",
    "说明武力的经济用途：远途换取稀缺物资与政治资源，并用于扩军。",
    "归纳：海商即海盗、陆商即私军；此类力量在君主集权未完成前必须由国君自掌。",
    "反问“只有国君无能，抑不了商之说、岂有不抑商之说”，把抑商与国君能力挂钩。",
    "点出商人身份（王弟王叔、丞相将军、仲父），得出抑商为尊王的结论。",
    "指出重农是遮掩之辞，跟随此说者被骗。",
    "以商鞅结局与“商朝”词源反问旁证商人形象之凶险。",
    "插入史学方法论：文献不可直接采信，须交叉盘问。",
    "以人物清单回应“商人无武装”的质疑，要读者自行核查其生意与部众。"
   ],
   "concept_usage": [
    {"term": "商", "meaning": "本文特指春秋战国时代拥有武装、能自行保障长途运输与报复能力的职业武力集团，不是小商贩。", "evidence": "P003", "ambiguity": "作者未区分不同时代与不同规模的商人，属整体化用法。"},
    {"term": "抑商", "meaning": "作者限定为国家压制这类武装性商业力量的政策，其真实目的是尊王而非重农。", "evidence": "P027", "ambiguity": "与通行的经济史用法（抑制工商）不同，需注意这是作者的重新定义。"},
    {"term": "尊王", "meaning": "指维护国君对暴力与财富的独占地位，防止王族、重臣以商养兵。", "evidence": "P027", "ambiguity": "正文只给出“尊王”二字，未展开其制度内容。"},
    {"term": "商（商朝）", "meaning": "作者以“商人”一词源于商朝、且商朝以刻满吃人图案的大火锅出名，暗示商与暴力凶险相连。", "evidence": "P030", "ambiguity": "该词源与形象关联是修辞性联想，作者未提供文献依据。"},
    {"term": "“仲父”", "meaning": "指权势大到国君要鞠躬叫爸爸的人物，用以说明大商人的政治地位。", "evidence": "P026", "ambiguity": "带戏谑色彩，非严格称谓界定。"},
    {"term": "暗镖", "meaning": "作者用以反问当时大宗货运不可能秘密进行的说法。", "evidence": "P006", "ambiguity": "仅作修辞反问，未展开论述。"}
   ],
   "examples_and_targets": [
    "山贼跪在道边行礼、摆山货并交“养路钱”：作者设想的场景，属修辞与例证（P013、P014）。",
    "“我武～维扬～”前哨举旗：修辞性插语，渲染商队威仪（P007）。",
    "商鞅五马分尸：作者用作反问式证据，反驳“重农”解释（P029）。",
    "商朝以刻满吃人图案的大火锅出名：作者用作文词源与形象联想（P030-P032）。",
    "“盗贼指示专业骗子写的”与“审赌场老千”：对历史文献与治史方法的比喻（P034、P036）。",
    "信陵君、平原君、春申君、孟尝君、吴起、刘濞、折御卿、张士诚、毛文龙、祖大寿、吴三桂、郑芝龙、曾国藩、曾国荃、李鸿章、荣禄、袁世凯、阎锡山、张作霖：作者列举并要求查证其生意与部众，用以反驳“商人无武装”的质疑（P039）。",
    "“没有成就霸业”“天下英雄尽入吾彀中”：引用式表述（P022，原文未注明出处）。"
   ],
   "conditions": [
    "商人须为武装力量这一判断以“春秋战国那种社会条件”为前提（P004）。",
    "武力水平的下限被作者定为“至少也要到这个水平”，否则不构成经商（P017）。",
    "商队武力用于换取的对象包括特许状、荣誉官职、奴隶等，属当时制度条件（P018、P019）。",
    "“必须国君自己做”以尚未成就霸业、尚未建立可随时连根拔起的控制为条件（P022）。",
    "抑商为尊王的结论依赖于商人多为王族重臣这一身份判断（P025、P026）。",
    "文献不可信与交叉盘问的方法主张未给出适用范围限制（P034-P036）。"
   ],
   "rhetoric_and_tone": "口语化、戏谑而强势，多用反问与夸张（“快速机动混成装甲特战旅”“送货上门的献爱心活动”“树都会上猪”）。频繁以第二人称“你”直接诘问读者（“你们自己掂量一下”）。叙事上采用场景化描写（商队列队而行、山贼跪迎）替代论证细节。对主流经济史解释持揭露口吻，称跟随者为“被他们一并骗了”。整体带阴谋论式修辞色彩，但作者以“要注意，你不要觉得这很夸张”自我加固。",
   "unresolved_questions": [
    "提问者预设“把土地分给三分之一的人，其他人从事工商业”，作者未直接评估该方案，仅重定义“商”。",
    "“天下英雄尽入吾彀中”未注明出处，需外部核查（P022）。",
    "商鞅被五马分尸的史实与原因、商朝“刻满吃人图案的大火锅”所指文物，均需外部核查（P029、P032）。",
    "P039所列人物的“生意”与武装规模，作者只要求读者自行查证，正文未给证据。",
    "“海商，即海盗；陆商，即私军”是全称判断，正文未讨论反例。",
    "作者对历史文献的整体性判断（盗贼指示专业骗子写的）未给出适用条件与例外，其强度不明。",
    "“尊王”所指的制度安排与具体朝代（如秦之抑商）正文未展开对应。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "先要搞清楚在古代何者为商。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "商都是些装备精良的职业武装力量。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "你根本没命把货送到目的地，也没命把钱运回家", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "不但保有足够的防御能力，还保证有二次报复确保足够惩戒的能力。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "长戈利剑、强弓劲弩、高车重甲、前呼后拥的快速机动混成装甲特战旅", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P017", "quote": "这是至少也要到这个水平，不然你不是在经商，而是在搞送货上门的献爱心活动。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P018", "quote": "你可以把本地的泥土都不如、只能烂在地里的垃圾烧硬了拖到各种地方换黄金", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P021", "quote": "海商，即海盗；陆商，即私军。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P022", "quote": "朕一翻手就能连根拔起", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P025", "quote": "说穿了不是王弟王叔，就是左丞相、右将军。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P027", "quote": "抑商，根本不是为了“重农”，抑商是为了尊王。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P028", "quote": "凡是跟着拿重农如何重要、商业如何抢占农业人口资源来说事的，都是被他们一并骗了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P029", "quote": "否则商鞅为什么五马分尸？因为太爱好农业么？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P032", "quote": "人家是以刻满了吃人图案的大火锅出名的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P034", "quote": "这基本上可以看作都是盗贼指示专业骗子写的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P036", "quote": "才能从对不拢的榫头上", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P039", "quote": "信陵君、平原君、春申君、孟尝君、吴起、刘濞、折御卿", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P040", "quote": "去查查他们生意做得怎么样，是不是手里只有几百人上千人。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中国古代史", "经济史", "政治史", "史学方法"],
   "issue_candidates": ["重农抑商政策动因", "先秦商人的武装性质", "君主集权与暴力垄断", "历史文献可靠性"],
   "text_function_candidates": ["答疑", "论辩", "翻案式解释"],
   "object_candidates": ["春秋战国", "商朝", "商鞅", "信陵君", "平原君", "春申君", "孟尝君", "吴起", "刘濞", "张士诚", "曾国藩", "李鸿章", "袁世凯", "张作霖"],
   "working_keywords": ["重农抑商", "抑商", "尊王", "私军", "海盗", "商队", "养路钱", "暗镖", "特许状"]
  },
  "notes": "无图片节点，正文与 lexical 均为 paragraph，无版本差异。提问者关于“分地三分之一、其余从事工商业”的预设未被作者采纳，也未归给作者。P022“天下英雄尽入吾彀中”、P029 商鞅结局、P032 商朝文物形象，均为待外部核查项。"
 },
 "1b66c244": {
  "analysis": {
   "question_context": "提问者就“成都一小区母子跳楼坠亡，警方已封锁现场”询问现场情况与调查结果（Q001，属提问者）。作者没有回答案情与调查结果，而是以叹息开篇，转向旁观者能做什么的一般性劝告。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以叹息开篇，主张平时多伸手帮人，可让人对社会和未来多些期待，并帮自觉无解的人护住最后一点指望。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "给出理由：屡屡得到陌生人意外帮助的人，远比没有此类经历的人不易绝望。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "推论：不要吝惜对陌生人的一点随机帮助；人人都随手帮一下，对每个人都有重大意义。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "定位这种做法的效力与边界：这是旁观者最有效的实际干预，且不是临事挺身而出，而是平时勿以善小而不为。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平时对人多伸手帮一把，能让人对社会和未来有额外的期待，并帮助自觉无法解决问题的人护住最后一点指望。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "屡屡得到来自陌生人完全意外的帮助的人，比没有这种经历的人更不容易绝望。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人不应吝惜对陌生人的一点随机帮助，人人都随手帮一下对每个人都意义重大。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平时的随机帮助差不多是旁观者能对这类不幸事件做出的最有效的实际干预。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "有效的干预不是事到临头再挺身而出大包大揽，而是平时勿以善小而不为。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "以对事件的叹息起笔，不作案情判断，直接转入旁观者能做什么。",
    "提出日常小帮助的心理效果：给人额外的期待、护住最后一点指望。",
    "以“屡屡得到”与“没有这种经历”的对比支持该效果，诉诸经验性判断。",
    "推出行动建议：不要吝惜随机的帮助。",
    "把该建议普遍化：人人都随手帮一下，对每个人都意义重大。",
    "限定其效力范围：这是旁观者最有效的实际干预。",
    "以否定句排除另一种做法（临事大包大揽），落到“勿以善小而不为”的古语上收束。"
   ],
   "concept_usage": [
    {"term": "随机的帮助", "meaning": "指日常中不针对特定危机、偶然发生的对陌生人的小帮助。", "evidence": "P004", "ambiguity": "作者未界定帮助的形式、规模与场合。"},
    {"term": "最后一点指望", "meaning": "指处于绝境者维持不放弃的心理底线，可由他人的意外善意加以保全。", "evidence": "P002", "ambiguity": "属形象化表述，未给出判定标准。"},
    {"term": "实际干预", "meaning": "指旁观者针对此类不幸事件所能采取、且作者认为最有效的行动。", "evidence": "P006", "ambiguity": "与专业救助、报警等干预形式的关系正文未说明。"},
    {"term": "勿以善小而不为", "meaning": "借古语表达平时的细小善行不应被忽略，是本文的结论性口号。", "evidence": "P007", "ambiguity": "标题作“毋以善小而不为”，正文作“勿以善小而不为”，用字不同。"}
   ],
   "examples_and_targets": [
    "成都一小区母子跳楼坠亡事件：来自提问字段的新闻事件，作者未叙述案情，仅以“唉”与一般性劝告回应，属语境而非作者论据（Q001、P001）。",
    "“屡屡得到来自陌生人的完全意外的帮助的人”与“没有这样的经历的人”的对比：作者的一般化经验例证（P003）。",
    "“事到临头再挺身而出大包大揽”：作者在结论处否定的另一种干预方式（P007）。"
   ],
   "conditions": [
    "帮助被限定为“没事遇到人”时的随手之举，即非危机情境下的日常行为（P001）。",
    "效果表述为“这在很多时候能帮助”，带频率限定（P002）。",
    "易绝望程度的比较被限定为“会远远的更不容易绝望”，属相对判断而非绝对保证（P003）。",
    "文章限定的作用对象是“觉得自己没办法解决问题的人”（P002）。",
    "“差不多也是……最有效的实际干预”以“差不多”修饰，作者未作绝对断言（P006）。"
   ],
   "rhetoric_and_tone": "篇幅极短（7段），语气低沉、克制而带劝谕性。以叹词“唉”开篇，回避对具体事件的评论，全篇用一般化的第三人称与泛指“人”“你”说理。使用“护住最后一点指望”“人人都随手帮一下”等口语化表达。结论以否定句加古语收束，带轻微训诫意味，但未指责任何人。",
   "unresolved_questions": [
    "提问者所问的现场情况与调查结果，正文完全未回答，也未说明不回答的理由。",
    "作者是否了解该事件的具体经过，正文未显示。",
    "“屡屡得到……会远远的更不容易绝望”的对比是否有依据，正文未给出数据或来源，需外部核查（P003）。",
    "标题作“毋以善小而不为”而正文作“勿以善小而不为”，用字不一致（P007）。",
    "“最有效的实际干预”与其他干预形式（如报警、专业心理援助）的关系未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "没事遇到人多伸手帮一把，让人对社会和未来有一些额外的期待。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "能帮助那些觉得自己没办法解决问题的人护住最后一点指望", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "会远远的更不容易绝望", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "不要吝惜自己对陌生人的一点随机的帮助", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "人人都随手帮一下人，对于每个人都意义重大。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这差不多也是作为旁观者真正能做到的对这种不幸事件最有效的实际干预了。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "不是事到临头再挺身而出大包大揽，而是平时勿以善小而不为。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会伦理", "社会心理"],
   "issue_candidates": ["陌生人互助", "绝望与心理支持", "旁观者的干预方式", "自杀事件的公共讨论"],
   "text_function_candidates": ["短评", "劝谕", "感慨"],
   "object_candidates": ["成都", "陌生人", "旁观者", "警方"],
   "working_keywords": ["善小", "随机的帮助", "最后一点指望", "绝望", "实际干预"]
  },
  "notes": "无图片节点，正文与 lexical 均为 paragraph，无版本差异。本文未回答提问者关于案情与调查结果的询问，也未对事件作事实陈述，故不涉及事实归属；标题与正文“毋／勿以善小而不为”用字不一致已登记。"
 },
 "62c1e4b8": {
  "analysis": {
   "question_context": "提问者问“为什么相信别人这么难？”（Q001，属提问者）。作者把问题重构为“对人授信的技术问题”，不讨论难的情感原因，而是给出授信决策需要处理的功课清单，并批评常见的粗暴授信方式。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "批评很多人的授信方式只有两极或寥寥几档，像吊扇一样。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "主张信任是多维度、多模式的复合问题，单维度线性调节（甚至离散）无法应对，并以只给飞机一个手动换挡器作类比。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "提出核心判断：相信别人是相当复杂的技术活，而不是勇气课。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "罗列授信决策须回答的二十余个问题：信任的时机与期限、议题、程度、证据置信度、担保与抵押、救济方式、威慑类型、救济成本、保险、双方误判的识别与修正、损失管理等。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "结论：把这些功课做好才能有效对他人授信，否则次次失败只能犯愁。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人对他人授信的方式太粗暴，只在全开与全关之间选择，或仅分为亲父母、夫妻、亲戚、同事、朋友、路人等寥寥几档。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "信任是多维度、多模式的复合问题，单维度的线性调节甚至离散调节无法合理对付该问题。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "相信别人是一门相当复杂的技术活，而不是一门勇气课。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有效授信须逐项处理时机、期限、议题、程度、证据置信度、担保抵押、救济与威慑手段、救济成本、保险、对方及自身误判的识别与修正、误判损失管理等功课。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有把这些功课都做好才能做到有效授信，否则会次次失败并为此犯愁。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "先批评现状：把授信压缩成两极或少数离散档位。",
    "以“跟吊扇似的”比喻离散档位的机械与粗放。",
    "提出结构性理由：信任是多维度、多模式的复合问题。",
    "以“只给一个手动换挡器就让人开飞机”类比工具与问题不匹配。",
    "给出定性判断：信任是技术活而非勇气课，把问题从态度转向技术。",
    "以连续问句列举授信决策的全部待办事项，涵盖信任范围、担保、救济、威慑、保险、误判管理。",
    "条件式收束：完成这些功课才谈得上有效授信，否则必然失败。"
   ],
   "concept_usage": [
    {"term": "授信", "meaning": "本文指对他人给予信任的决策行为，被作者当作可分维度、分档位、可管理的技术操作。", "evidence": "P001", "ambiguity": "作者借用了金融用语，但未说明与金融授信的差别。"},
    {"term": "多维度、多模式", "meaning": "指信任可在不同议题、不同程度上分别设定，而非单一刻度。", "evidence": "P003", "ambiguity": "具体维度清单散见于P005的问句，未系统分类。"},
    {"term": "信任决策到期", "meaning": "指对信任设定有效期或下一次核验时点。", "evidence": "P005", "ambiguity": "如何确定期限，正文未说明。"},
    {"term": "被动威慑／积极威慑", "meaning": "作为救济手段的两种威慑类型被并列提出，未展开定义。", "evidence": "P005", "ambiguity": "术语在本文未定义，读者需自行理解。"},
    {"term": "救济", "meaning": "指信任被辜负后的补救途径，作者列举仲裁、起诉等形式。", "evidence": "P005", "ambiguity": "未涉及救济失败后的处理。"}
   ],
   "examples_and_targets": [
    "亲父母一档、夫妻一档、亲戚一档、同事一档、朋友一档、路人一档“跟吊扇似的”：作者对常见授信方式的批评性例证（P002）。",
    "给一架飞机却只给一个手动换挡器：作者类比，比喻工具与问题不匹配（P003）；“怎么不摔个嘴啃泥”为夸张说法。",
    "“要么肝胆相照，要么先下手为强”：作者概括的两种极端授信态度（P001）。",
    "担保人、抵押物、仲裁、起诉、保险：作者列举的现实制度性手段，属其提出的功课清单（P005）。",
    "“对方是不是出现了对局势的误判？比如认为你别无选择？”：作者设想的博弈情境（P005）。"
   ],
   "conditions": [
    "全篇建议以“对人授信”这种人际信任关系为对象，不涉及制度性信用（P001、P006）。",
    "条件式结论：“要把这些功课都做好，你才可以做到有效的对他人授信”（P006）。",
    "失败判断带频率限定：“你次次都失败，自然要抓着头发犯愁了”（P006）。",
    "议题维度中含前置筛选问句“这个议题属于可以托付给人的议题吗？”，暗示部分议题不可托付（P005）。",
    "救济手段的列举以存在担保人、抵押物、仲裁与保险等制度资源为隐含前提（P005）。"
   ],
   "rhetoric_and_tone": "短篇说理，语气干脆、略带调侃与批评。以“太粗暴了”“跟吊扇似的”“摔个嘴啃泥”等口语化比喻降低抽象度。核心修辞是把信任问题从道德／勇气问题改写为技术问题（“技术活”“勇气课”）。P005 以二十余个连续问句构成清单式排比，是全文结构重心，节奏急促，但未给答案。全篇用第二人称“你”泛指读者。",
   "unresolved_questions": [
    "提问者问“为什么相信别人这么难”，作者未直接回答“难”的原因，而是给出应做的事项清单。",
    "P005 的二十余问均无操作答案，如何具体设计各维度与档位正文未说明。",
    "“被动威慑／积极威慑”未定义，其区分需外部核查或作者其他文本佐证（P005）。",
    "“授信”是否与金融语境下的授信同义，正文未界定（P001）。",
    "作者未讨论信任能力可否训练、由谁训练，以及此技术对亲密关系的适用限度。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人对人授信技术太粗暴了——要么肝胆相照，要么先下手为强。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "亲父母一档、夫妻一档、亲戚一档、同事一档、朋友一档、路人一档，跟吊扇似的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "信任是一个多维度、多模式的复合问题，只有单维度的线性调节", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "相信别人是一门相当复杂的技术活，而不是一门勇气课。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "有没有担保人？有没有抵押物？救济手段是什么？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "是被动威慑？还是积极威慑？救济成本是多少？是否有相应的保险可以购买？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "如何判断自己目前误判的可能方向？如何管理自己误判造成的损失和威胁？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "要把这些功课都做好，你才可以做到有效的对他人授信。否则你次次都失败", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系", "决策方法", "风险管理"],
   "issue_candidates": ["信任的维度与程度", "授信决策流程", "担保与救济机制", "误判管理"],
   "text_function_candidates": ["答疑", "方法建议", "批评"],
   "object_candidates": ["亲父母", "夫妻", "亲戚", "同事", "朋友", "路人", "担保人"],
   "working_keywords": ["授信", "信任决策", "多维度", "多模式", "救济", "威慑", "保险", "误判"]
  },
  "notes": "无图片节点，正文与 lexical 均为 paragraph，无版本差异。提问（Q001）只作语境，作者未按其字面作答。“被动威慑／积极威慑”等术语原文未定义，登记为需外部核查／待后续文本佐证；P005 问句清单的具体操作答案正文未给出。"
 },
 "26958a21": {
  "analysis": {
   "question_context": "提问者问“技术是价值中立的吗？”（Q001，属提问者）。作者给出一个拆分式回答：技术本身中立，但围绕技术的一切人类行为都不中立；随后转入对掌握技术原初构想者的责任劝告，并直接否定“技术是中性的”这一说法在实践中的用法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "核心命题：技术本身价值中立，但设想、开发、传播、应用、管制等技术相关行为没有一个是中立的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "以“意在毁灭地球的技术”为例，说明从设想、研发测试到传播、应用各环节都不中立。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "提出可替技术辩护的说法：同一技术也可用于解决来袭小行星或切开月球降低潮汐效应。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "反驳上述辩护：良性运用与恶性运用不对称且不可逆；即使技术可逆向运用，地球一旦消失也无人再拉动操纵杆。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "由极端情形推及一般技术：很多技术既非出于善意被开发也非出于善意被应用，只是幸运地未造成无法承受的后果，人类受害后才找到管理与善用的手段。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "即使出于良好初心引入知识图谱的技术，也迟早被恶意探索恶意应用；技术客观上是对人类的挑战、人类命运的切换器。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018"], "summary": "对掌握原初构想者的责任陈述：你握着人类命运的可能性与是否把人类放上考场的决定权；虽可推给别人且会失掉财富名望权势，仍希望你慎而重之；能站到认知最前线者非出于偶然，也不需靠这些满足虚荣或吃饭。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "结论与训诫：在是否把人类没准备好的技术引入知识图谱一事上责任是完全的；不要用“技术是中性的”自欺，也不要再对别人说；神器人类尚不配拥有，先看到者是人类守夜人，有看守之责不得逃避。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术本身是价值中立的，但围绕技术的行为——从设想、开发、传播、应用到管制——没有一个是中立的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以一种意在毁灭地球的技术为例，其设想行为、研发期间的构思与测试、传播行为和应用都谈不上中立。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“该技术也可用于解决来袭小行星或切开月球降低潮汐”这一辩护不成立，因为良性运用与恶性运用并不对称，更加不是可逆的。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "退一步说，即使毁灭地球的技术可以逆向运用把地球重新拼拢，技术一旦被应用地球就消失了，无法指望还有人再拉一次操纵杆。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多技术既非出于善意被开发也非出于善意被应用，它们只是幸运地未造成人类承受不起的负面后果，人类在受害之后才找到管理与另外善用的手段。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使出于良好初心被引入人类知识图谱的技术，也迟早会被恶意的人探索恶意的应用。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术客观上是对人类的挑战、人类命运的切换器；手握某项技术的原初构想，就握着人类某种命运的可能性与是否把人类放到考场上的决定权。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者承认“你不做也会有别人做”“晚开口只是把审判日拖后几天，且会失去巨大的财富、名望和权势”，但即便如此仍希望对方慎而重之。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "以“我也不太相信”这一自陈判断，认为能站到人类认知最前线的人并非出于偶然，也不会真的需要这些专利费、虚荣或成就感。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在是否将人类没有准备好的技术引入人类的知识图谱这件事上，先看到者的责任是完全的。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要用“技术是中性的”这种说法自欺欺人，因为这根本不是技术本身是否中性的问题，尤其是在看到这些话的前提下；也不要再对别人说这些话。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有太多神器人类还不配拥有；先看到者就是被选中的人类的守夜人，有看守之责，不应逃避。", "evidence": ["E18", "E19"]}
   ],
   "argument_steps": [
    "先作概念拆分：中立与否适用于技术周围的人类行为，而不适用于技术本身。",
    "以“意在毁灭地球的技术”作极端例子，逐环节（设想、研发、传播、应用）指出其不中立。",
    "替可能的辩护方提出理由：同一技术也可用于对付小行星、切开月球。",
    "以不对称性与不可逆性反驳该辩护。",
    "用“退一万步讲”作让步式假设，再以“谁来拉第二次操纵杆”反诘，堵住可逆性退路。",
    "由极端情形下降至普通技术：开发与应用多非出于善意，只是后果幸运地可承受。",
    "归纳出受害在前、管理与善用在后的过程模式。",
    "进一步指出良好初心的技术同样会被恶意应用。",
    "提升判断层级：技术是人类命运的切换器，构想者握有决定权。",
    "承认替代者存在、拖延有限、个人会付出财富名望权势的代价，仍作劝告。",
    "以对读者身份与能力的判断（非出于偶然、不需专利费）支持责任归属。",
    "结论：责任是完全的，禁止以“技术是中性的”自欺或再传播该说法。",
    "以“守夜人”意象收束，下达看守之责的行动要求。"
   ],
   "concept_usage": [
    {"term": "技术中立", "meaning": "作者只在“技术本身”这一层面承认价值中立，并否定把该说法用于为技术相关行为开脱。", "evidence": "P001", "ambiguity": "“技术本身”与技术相关行为的边界如何划定，正文未界定。"},
    {"term": "设想技术／开发技术／传播技术／应用技术／管制技术", "meaning": "作者用以指称围绕技术的五类人类行为，并逐一否认其中立性。", "evidence": "P001", "ambiguity": "五类行为是否穷尽、彼此如何区分，未说明。"},
    {"term": "对称／可逆", "meaning": "指良性运用与恶性运用在后果上不对等、且不能相互抵消恢复。", "evidence": "P007", "ambiguity": "未给出衡量对称性的标准。"},
    {"term": "人类的知识图谱", "meaning": "指人类既有知识总体，作者把“是否引入”当作可抉择的门槛。", "evidence": "P012", "ambiguity": "知识图谱能否被人为封锁，正文未讨论。"},
    {"term": "命运的切换器", "meaning": "作者对技术的定性：技术能把人类切换到另一种命运轨道。", "evidence": "P013", "ambiguity": "属隐喻式表述，无操作定义。"},
    {"term": "守夜人", "meaning": "指先于他人看到危险技术可能性的人，被作者赋予看守人类的责任。", "evidence": "P022", "ambiguity": "“被选中”由谁选中、守夜人权限与后果，正文未说明。"},
    {"term": "神器", "meaning": "指人类尚不配拥有的强有力技术。", "evidence": "P022", "ambiguity": "哪些技术属于神器，作者未列标准。"}
   ],
   "examples_and_targets": [
    "意在毁灭地球的技术：作者设想的极端例证，用于说明各环节不中立（P002-P008）。",
    "用该技术解决来袭的流浪小行星、把月球切成两半降低潮汐效应：作者替辩护方设想的用途，属被反驳的说法（P006）。",
    "“即使毁灭地球的技术可以逆向运用重新把地球拼拢起来”：作者假设的让步情形，随后被其反诘否定（P008）。",
    "“很多技术都不是出于善意被开发出来、也不是出于善意被应用的”：作者对一般技术史的判断，未举具体技术（P009）。",
    "“技术是中性的”这句话：作者明确点名的被反驳说法（P020）。",
    "“被选中的人类的守夜人”：宗教／文学色彩的修辞意象（P022）。",
    "“失去巨大的财富、名望和权势”“等着这些专利费吃饭”：作者设想读者可能付出的代价与利益，属劝告中的让步（P015、P017）。"
   ],
   "conditions": [
    "中立性判断被限定在“技术本身”这一层面，行为的非中立不推论为技术本身非中立（P001）。",
    "极端例证以“意在毁灭地球的技术”为假想前提（P002）。",
    "P008为让步式假设（“退一万讲”），作者并非承认可逆性成立。",
    "一般技术“只是幸运的未能造成人类所承受不起的负面后果”，以“幸运”与“承受不起”为限定（P010）。",
    "责任劝告的对象被限定为“能站到人类认知最前线”“手握某种技术的原初构想”的人（P014、P017）。",
    "禁止自欺的效力被限定为“尤其是在你看到了这些话的前提下”（P020）。",
    "作者对读者能力与动机的判断以“我也不太相信”明示为个人判断而非事实断言（P017）。"
   ],
   "rhetoric_and_tone": "由论说转向训诫与劝勉，语气庄重、紧迫，带准宗教色彩。使用“守夜人”“被选中”“审判日”“神器”等意象，把技术选择提升为命运与道德抉择。多次以“是的，也许……是的，也许……”作让步排比后仍坚持劝告，并以第二人称“你”“你们”直接对话，形成私人告诫的口吻。P020 直斥“鬼话”，语气转为强烈的否定与禁止（“不要……也不要再……”）。全篇少用数据与具体案例，主要靠假设情境与价值宣示推进。",
   "unresolved_questions": [
    "“技术本身中立、行为不中立”的切分标准正文未界定，何种行为可算技术本身的一部分无说明。",
    "“没有一个是所谓中立的”是对五类行为的全称否定，正文未考虑反例。",
    "“有太多神器，人类还不配拥有”的判断标准未给出，哪些技术属于此类亦未列举（P022）。",
    "“被选中的人类的守夜人”中“被选中”的主体与依据不明（P022）。",
    "责任的“完全”在他人也可开发同一技术的情况下如何成立，正文仅以让步方式带过，未展开论证（P015、P019）。",
    "作者所指“人类没有准备好的技术”是否包含具体现实技术，正文未说明，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "技术本身是价值中立的，但是围绕着技术的行为", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "一种意在毁灭地球的技术，从设想开始，设想的行为就不是中立的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "应用它更谈不上中立。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "比如用来解决来袭的流浪小行星啊", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P007", "quote": "对一种技术的良性的运用和对该技术恶性的运用并非对称的，更加不是可逆的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "准备再靠谁去再拉一次操纵杆把地球拼回来？", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P009", "quote": "很多技术都不是出于善意被开发出来、也不是出于善意被应用的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "这必定包含了一个人类先深受其害、大难不死、然后尝到点甜头的过程。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "也同样迟早会被恶意的人探索恶意的应用。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "技术客观上是一种对人类的挑战，一种人类命运的切换器。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "手握着是否把人类放到这个考场上的决定权", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "你会因此失去巨大的财富、名望和权势。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P017", "quote": "没有一个是真的出于偶然，而且我也不太相信你作为这样的人", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P018", "quote": "以你的能力，想要衣食无忧，并不会成其为不可逾越的困难。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "你的责任是完全的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "不要用任何“技术是中性的“这种鬼话自欺欺人", "relation": "contradicts"},
    {"key": "E17", "paragraph_id": "P021", "quote": "自然，也不要再对别人说这些话。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "有太多的神器，人类还不配拥有，你先看到，你就是被选中的人类的守夜人。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "你有看守之责，不要逃避。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["技术哲学", "科技伦理", "价值论"],
   "issue_candidates": ["技术中立命题", "技术开发与应用的道德责任", "双重用途困境", "知识封锁与责任归属"],
   "text_function_candidates": ["答疑", "论辩", "劝诫"],
   "object_candidates": ["人类", "研究者／技术发明者", "恶意的人"],
   "working_keywords": ["技术中立", "价值中立", "双重用途", "知识图谱", "守夜人", "神器", "审判日", "切换器"]
  },
  "notes": "无图片节点，正文与 lexical 均为 paragraph，无版本差异。原文 P020 引号使用不配对（“技术是中性的“），引文按原文逐字复制。本文不涉具体技术或机构，所举“毁灭地球的技术”为假设例证，均未标为已证实的外部事实。"
 },
 "6190752a": {
  "analysis": {
   "question_context": "提问者问“如何判断一个领导是在培养你，还是在压榨你？”（Q001，属提问者，该问句预设两者是对立的两难）。作者直接否认该两难成立：判断的关键不在领导，而在你自己是否有自己的道路；并把“压榨”的判定标准改写为是否给过选择权。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "否认两难：即便领导在培养你，你也必须有自己的道路，把命运寄托在“全靠领导栽培”或“全看爹妈养育”上是对自己命运不负责任。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "限定：并非不能有意跟随某领导走到底，前提是你清楚该领导要去的地方与你要去的地方同路，而非在不知去哪时偷懒推给“我就跟着这人”。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "以“你也要去那里，ta也要去那里”定义同路者，以“揪住对方的裤腰带——老司机带带我”刻画攀附者，指明同样是跟，前者是同行后者是攀附。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "领导（若非靠裙带上位的假货）大概率能分辨两者，且待遇不同：对前者留有余地与客气，对后者流露轻视；若发现攀附者才被当亲信，则应加紧锻炼基础技能、多考点证、多攒个人成就，此非久留之地。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015"], "summary": "提出压榨与培养并非对立互斥的属性，并给出简单红线：有没有给过你选择权。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "以岗位职责与交期为例说明：在你同意范围内要求再严厉、你自己定的紧交期以及被施压后自己提出的紧日子，都不算压榨；只要同意且对方未用违法或暴力手段，即便迫于失业压力妥协也无资格称压榨。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025"], "summary": "以水果摊还价为类比，论证对方有竭尽合法范围争取最好结果的自由，并再申明红线所在。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030"], "summary": "列出构成压榨的反例：事后单方提前交期且不觉得抱歉、按约定办到却不给约定报酬、因打工而看低人格、无约定未经同意以非法手段侵占合法利益；但仍重申凡你同意过的一概不算。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032", "P033"], "summary": "把两个问题联系起来：认为它们构成“对立的权衡关系”，本身已意味着你不是同路者而是攀附者；越礼非法侵占他人利益者与任何人都不同路，因其自己没走在正路上。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038"], "summary": "点出人的真盘算：用软弱、“乖”、忍耐凌辱换取不抛弃与视为亲信，只把“容我攀附”换成更好听的“培养我”；并断言走攀附逻辑者到最后讨不了好，以“良禽择木而栖，当心你的脚下”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“领导在培养你还是压榨你”不构成两难判断，你用不着去做这种判断。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即便领导在培养你，你也必须有自己的道路，不能把命运寄托在“全靠领导栽培”上，如不能寄托在“全看爹妈如何养育”上一样。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把命运寄托于领导的栽培是对自己的命运不负责任。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者并非否定有意计划跟随某领导走到底，前提是你自己清楚该领导要去的地方确实与你要去的地方同路。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "同路者与攀附者的区别在于：前者因确实要去同样的地方而理智地同行，后者是在不知要去哪里时把“我要决定去哪里”的懒偷掉。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "领导若不是靠裙带上位的假货，大概率完全清楚你是同行者还是攀附者，且两类人的待遇不同。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若发现攀附者才被认定为亲信、同行者常被猜忌防备，应加紧锻炼基础技能、多考点证、多攒个人成就，因为此处非久留之地。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "压榨与培养根本不是互相对立、互相排斥的属性。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "压榨的简单红线是：有没有给过你选择权；在你同意范围之内的要求，你觉得多严厉都不叫压榨。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即便你因扛不住压力而自己提出紧交期、或因迫于失业压力而妥协，只要对方未使用违法或暴力手段，你都没资格说对方压榨。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方有竭尽合法范围的全力获得自己可获得的最好结果的自由，如水果摊还价中只要卖了就是自己愿意。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "构成压榨的是：约定后单方突然提前交期且理所当然毫不抱歉、按约定办到而不给约定报酬、因你打这份工就认为你人格较低而不礼貌、以及无约定未经同意以非法手段侵占你的合法利益。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把“培养”与“压榨”看作一种对立的权衡关系，本身就已意味着你不是一个同路者，而是一个攀附者。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "人的真盘算是用软弱、“乖”、忍耐凌辱来换取不被抛弃与视为亲信，只把“容我攀附”换成更好听的“培养我”；但走攀附逻辑的到最后不会让你讨得了好。", "evidence": ["E20", "E21", "E22"]}
   ],
   "argument_steps": [
    "直接否认提问所设的两难：这根本不构成两难判断。",
    "把关注点从领导行为转向下属自身：你也要有自己的道路。",
    "以“全看爹妈如何养育”作类比，论证寄望他人栽培是不负责任。",
    "以“注意，我并不是说你不能……”作让步，为跟随领导留出条件性空间。",
    "区分两种“跟着”：基于同一目的地的理智同行，与偷懒式的推卸。",
    "以“你也要去那里……ta走在你前头”正面定义同路，以“老司机带带我”刻画攀附。",
    "以“前者是同行，而后者是攀附”作对举式定性。",
    "加入对领导辨识能力的限定（若不是靠裙带上位的假货），并对比两类待遇。",
    "给出处境性行动建议：若攀附者反被当亲信，则应攒技能与资历并准备离开。",
    "转折到第二问：压榨与培养并非对立属性。",
    "提出可操作红线：有没有给过你选择权。",
    "以岗位职责、交期两例证明“同意之内不算压榨”。",
    "以设问“算不算压榨呢？”自答“一样不算”，处理被施压后自行让步的情形。",
    "给出压榨的成立条件：同意＋无违法暴力手段则不成立，即便因失业压力妥协。",
    "以水果摊还价类比说明合法范围内争取最好结果的自由。",
    "列举构成压榨的四种情形（擅自提前交期、克扣约定报酬、人格轻视、非法侵占）。",
    "再以“但是记住，只要你同意过的，就不算”重申红线。",
    "把两问联系：视其为权衡关系即自证攀附者身份。",
    "指出非法侵占他人利益者自己没有正路，因而谈不上同路。",
    "揭示攀附的心理盘算与其话语包装。",
    "以“走攀附逻辑的，到最后不会让你讨得了好”作预测性警告，以“良禽择木而栖，当心你的脚下”收束。"
   ],
   "concept_usage": [
    {"term": "同路者", "meaning": "指自己明确要去某地、因目的地相同而理智地与他人同行的人。", "evidence": "P006", "ambiguity": "“同路”是否含价值一致，正文只以“要去的地方”表述。"},
    {"term": "攀附", "meaning": "指不知道自己的方向，只因对方“在前头”就抓住对方裤腰带跟随；作者视为对自身选择责任的推卸。", "evidence": "P008", "ambiguity": "与一般意义上的依赖、学习、请教的界线未界定。"},
    {"term": "压榨", "meaning": "作者的操作性定义：未给选择权、未经同意，或以违法暴力手段及无约定方式侵占你的合法利益。", "evidence": "P029", "ambiguity": "与劳动法上的违法用工标准是否一致，正文未对照。"},
    {"term": "选择权", "meaning": "本文的核心红线：决定是否接受某项要求的机会；只要同意过即视为行使过选择权。", "evidence": "P015", "ambiguity": "迫于失业压力而作的同意被作者仍算作同意，与“实质自由”的常见理解存在张力。"},
    {"term": "培养", "meaning": "被作者视为与压榨不同层面的属性，可与压榨同时存在。", "evidence": "P014", "ambiguity": "正文未给出“培养”的正面定义。"},
    {"term": "靠裙带上位的假货", "meaning": "指无真才实学、靠关系上位的领导，作者以此限定领导辨识力的判断。", "evidence": "P009", "ambiguity": "属贬称，无判定标准。"}
   ],
   "examples_and_targets": [
    "“全看爹妈如何养育”：作者类比，说明把命运寄望于他人栽培的性质（P002）。",
    "“老司机带带我”与“揪住对方的裤腰带”：作者用口语化意象刻画攀附者（P007）。",
    "“莫欺少年穷”：作者引用的成语，用以描述对同行者的客气（P011）。",
    "招聘时的岗位职责、交期由谁确定：作者举的职场实例，用于检验“同意范围内不算压榨”（P016、P017）。",
    "“被施压后自己提出紧日子”：作者自设的边界情形并自答不算压榨（P018-P020）。",
    "去水果摊还价：作者类比，论证合法范围内争取最好结果的自由（P024）。",
    "“你不卖我就打死你、我就砸你摊、我就把你绑走饿几天、我就去你儿子学校放炸弹”：作者列举的非法暴力威胁反例（P024）。",
    "“中国大部分的领导其实都不够资格成为合格的领导”：作者对国内领导群体的整体性判断（P012）。",
    "“良禽择木而栖”：作者引用古语作为结语（P038）。"
   ],
   "conditions": [
    "跟随领导的前提是“你自己的确清楚这个领导要去的地方的确与你要去的地方同路”（P004）。",
    "对领导辨识力的判断以“领导自己如果不是个靠裙带上位的假货”为条件（P009）。",
    "“前者的待遇和后者不一样”的作者判断带“大概率”限定（P009、P010）。",
    "不算压榨的条件：在你同意范围之内、交期由你定、对方未使用违法或暴力手段（P016、P017、P021、P022）。",
    "水果摊类比中排除的情形是无任何非法暴力威胁，作者的表述为“你没有进行任何意义上的非法暴力威胁”（P024）。",
    "“觉得是面子上却不过同意的，或者是怕失业而同意的，都是你同意的”属作者对同意范围的强限定（P030）。",
    "行动建议（攒证、攒成就）以“攀附者才会被认定为亲信而同行者常被猜忌防备”这一观察成立为条件（P013）。"
   ],
   "rhetoric_and_tone": "第二人称“你”贯穿全篇的训诫式口吻，语气直率、略带讥讽与道德压力。使用口语化贬称（“假货”“糊涂蛋”式的攀附者形象）与戏仿对白（“乖，昨天作业拿来我看”式的上下级想象见P007的“老司机带带我”）。结构上以“注意，我并不是说……”作自我限定，以“但是记住”重申结论，避免绝对化。大量使用设问自答（“算不算压榨呢？——一样不算”）推进。结尾用古语与警告句（“当心你的脚下”）加强训诫色彩。对“中国大部分的领导”作整体性贬评，带情绪色彩。",
   "unresolved_questions": [
    "“培养”在本文没有正面定义，作者只否定其与压榨的对立关系（P014）。",
    "作者对“中国大部分的领导其实都不够资格成为合格的领导”的判断未给依据，需外部核查（P012）。",
    "因失业压力而作的同意仍算同意，此标准与劳动法或实质自由视角的关系正文未讨论（P022、P030）。",
    "“同路”的判断标准（目的地由谁判定、可否改变）正文未说明，读者可能难以自测。",
    "若领导既在培养你又在压榨你，作者未给出行动方案，只给出压榨的识别红线。",
    "作者未讨论下属提出条件、协商交期的可能，例子中交期多由下属自定或被施压后自定（P017、P018）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你用不着去做这种两难判断，因为这根本不构成两难判断。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "ta是在培养你，你也要有自己的道路，而不能把自己的命运寄托在“全靠领导栽培”上。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这个是对自己的命运不负责任。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "前提是你自己的确清楚这个领导要去的地方的确与你要去的地方同路", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而不是在自己不知道要去哪里的前提下偷掉这个“我要决定去哪里”的懒", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "同样是“跟着”，前者是同行，而后者是攀附。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "ta大概率完全清楚你是前者还是后者。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P011", "quote": "对后者则多少会难以控制的流露出微妙的轻视和鄙夷。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "记得加紧锻炼基础技能，多考点证、多攒点个人成就——此非你久留之地。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "这跟“培养”根本不是互相对立、互相排斥的属性。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "有一个简单的红线在这里——给没给过你选择权？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "在你的同意范围之内要求你，你觉得多严厉都不叫压榨。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "一样不算。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "哪怕你是因为迫于失业压力而妥协，你都没资格说对方压榨你。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "因为对方有竭尽合法范围的全力获得自己可以获得的最好结果的自由。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "水果摊主只要卖了就是自己愿意", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "结果他突然要你明天交，而且一副理所当然毫无可抱歉处的样子，这就是压榨你。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "觉得你打了ta这份工你的人格就比较低，于是对你不礼貌，这就叫压榨你。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P032", "quote": "觉得它们构成一种“对立的权衡关系”，本身就已经意味着你不是一个同路者，而是一个攀附者。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "能忍耐凌辱和侵犯来换取对方不抛弃、视为亲信、容自己攀附。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P036", "quote": "只需要把“容我攀附”换成更好听的“培养我”，就完美了。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "走攀附逻辑的，到最后不会让你讨得了好。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场关系", "组织行为", "人生选择"],
   "issue_candidates": ["领导培养与压榨的区分", "同路与攀附", "同意的边界与选择权", "职场中的合法性与暴力"],
   "text_function_candidates": ["答疑", "劝诫", "论辩"],
   "object_candidates": ["领导", "下属", "中国大部分的领导"],
   "working_keywords": ["培养", "压榨", "同路者", "攀附", "选择权", "红线", "良禽择木而栖"]
  },
  "notes": "无图片节点，正文与 lexical 均为 paragraph，无版本差异。提问（Q001）预设“培养／压榨”为对立两难，作者明确否认该预设，故该预设未被记为作者主张。文中对“中国大部分的领导”的整体评价属作者判断，未提供依据，已登记待外部核查。"
 },
 "ef094234": {
  "analysis": {
   "question_context": "提问者问“我们为什么要生孩子？”（Q001，属提问者）。作者的回答是：实际上的“理由”只是“天注定”，人为此想象的种种合理理由都是自我抚慰与自我催眠，真正的“理由”是未能抗拒的种种原因；作者随后把这一断言的意义限定为父母对自身处境的自我认定，而非客观真理。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "核心命题：生育的实际理由只是“天注定”，因为生育的意义与影响超出人类理解预料的范围，故一切自觉的理由都没有意义、只是一种自我抚慰与自我催眠，且这些理由并不足够。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010"], "summary": "逐一列举并拆解养育防老、天伦之乐、继承衣钵、传宗接代、实现未竟事业、维系夫妻感情等理由。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012"], "summary": "给出结构性理由：子女一生漫长且自由，任何打算都可能因世事变迁与其自由选择而落空，故生养的自欺欺人之处在于确信越强、破灭时越抑郁；想得开者自嘲了事，想不明白者把后果发泄到子女身上。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015"], "summary": "区分“理由”与“原因”：生育没有理由，只有当时机缘巧合的原因；社会灌输的责任、许诺的美好体验、政策激励、伦理压力，加生物本能与心理本能，构成生育的原因。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "自我限定：此前说法不是“客观的真理”，而是告诉父母一个更严肃的问题——接受这一自我认定就能把无形的利刃从子女脖子上移走；真正的判断不是断言真假，而是“你的英明神武重要，还是ta们幸福一些重要”。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "重申因果：事情的发生不是由于当时的种种打算（那些只是润滑油、传动零件，未必关键），而是未能抗拒的原因；上天选择你过有子女的生活并把ta们赐给你。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "给出态度建议：这条轨道有苦有甜、不高于也不低于其他道路，不应想象它更高贵（这种想象必有反噬）；要紧的是把发到的牌打好，而自认出于英明智慧勇敢的理由选择生育会妨碍这点，导致固执、易怒、易放弃、易迷茫失望。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "结论性重申：生育没有所谓合理的理由，只有原因；它是纯粹的命运安排，过去如此、今日亦然、将来也不会改变。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生育的实际“理由”只是“天注定”三字。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生育的意义和影响之重大超过一切人类所能理解和预料的范围。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不管你以为自己因为什么原因、什么打算而觉得生孩子合理，都是没有意义的，因为事后会发现那只是一种自我抚慰、一种自我催眠，这些理由并不足够。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养儿防老、天伦之乐、继承衣钵、传宗接代、实现未竟事业、维系夫妻感情等具体理由都会在子女成长与实际选择中落空。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "子女一生太漫长且自由，任何放在他们身上的打算都可能因世事变迁与其不可剥夺的自由选择而落空，因此无论基于什么超级实用的理由生养都是自欺欺人。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "对自欺欺人的理由有多确信，就会在它破灭时有多抑郁；想不明白的人会把自己自欺欺人的后果毫无建设性地发泄到子女身上。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生育子女并没有什么理由，而只有当时机缘巧合原因。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会灌输的责任、许诺的美好体验、为自身稳定与延续构建的政策激励、伦理压力，以及生物本能与心理本能，合起来构成生育的原因。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者声明自己不是在说这是“客观的真理”，而是在告诉父母一个更严肃的问题：不接受该认定则子女脖子上会被架上刀，接受则刀被放下。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "你真正要做的判断不是断言本身真实与否（不想接受自然能找到足够多的“充分论述”，更可以拒绝讨论），而是“你的英明神武重要，还是ta们幸福一些重要”。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "生育的发生不是因为当时所做的种种打算——那只是润滑油、传动零件，甚至未必是真正关键的要素——而是因为种种未能抗拒的原因。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有子女的生活轨道有苦也有甜、既不高于也不低于其他道路；不应因这条道路是自己无法更改且目前看似主流的，就强行想象它更高贵，这种想象必有反噬。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "自认为出于英明、智慧、勇敢的理由选择生育，会妨碍你把发到的牌打好，使你变得不必要的固执、无谓的易怒、出乎意料的易放弃、更轻易陷入迷茫和失望。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "生育没有所谓“合理”的理由，只有原因；它是一种纯粹的命运的安排，过去如此、今日亦然、将来也不会改变。", "evidence": ["E20", "E21"]}
   ],
   "argument_steps": [
    "直接给出一句话答案：“天注定”，取代提问所问的理由。",
    "给出理由：生育的意义与影响超出人类理解与预料的范围。",
    "推论：一切自觉的生育打算都无意义，是自我抚慰、自我催眠；理由是“并不足够”。",
    "以养儿防老为例：孩子未满五岁就已不知谁防谁老。",
    "以天伦之乐为例：孩子未十岁就怀念没有孩子的快乐。",
    "以继承衣钵为例：孩子看不上你的衣钵，要学马斯克上火星。",
    "以传宗接代为例：孩子毕业后再没回过张家村。",
    "以实现未竟事业为例：反问生育时是否真有未竟事业，并指出就业时“未竟的事业”已不知多少种。",
    "以维系夫妻感情为例，以反问“这个需要回答吗？”带过。",
    "给出结构性论证：子女一生漫长而自由，任何打算都可能落空。",
    "指出自欺欺人的代价：确信越强，破灭时越抑郁。",
    "区分两种反应：想得开者自嘲，想不明白者向子女发泄。",
    "作概念区分：没有理由，只有机缘巧合的原因。",
    "列举构成原因的诸因素：社会灌输、政策激励、伦理压力、生物与心理本能。",
    "归纳：一点点意外与侥幸，加强大的社会、生理压力与推力，构成生育的原因。",
    "自我限定：这不是“客观的真理”，而是给父母的自我认定；其价值在于把架在子女脖子上的刀移走。",
    "对举接受与不接受该认定的后果。",
    "把争论的焦点从断言真假转到价值排序：英明神武与子女幸福哪个重要。",
    "重申发生机制：打算只是润滑油与传动零件，真正起作用的是未能抗拒的原因。",
    "以“上天选择了你”“天赐了ta们给你”作命运式表述。",
    "评价这条轨道：有苦有甜，不比别的道路高贵，强行想象高贵必有反噬。",
    "给出行动指向：要紧的是把发到的牌打好。",
    "指出妨碍打好牌的具体信念及其四项后果。",
    "以“生育没有理由，只有原因”“纯粹的命运的安排”及时间上的普遍化收束，末句“就是这样”作结。"
   ],
   "concept_usage": [
    {"term": "理由／原因", "meaning": "本文的核心区分：“理由”指人为自己设想的合理依据（被否定为自我催眠）；“原因”指未能抗拒的社会、生理、心理推力与机缘巧合（被肯定为实际发生机制）。", "evidence": "P013", "ambiguity": "两者在作者用法中的界线仍依赖直觉，未给出判定标准。"},
    {"term": "天注定／命运的安排", "meaning": "对生育发生机制的命名，强调非人为选择、非意图所致。", "evidence": "P028", "ambiguity": "是否指向超自然主体，与“上天选择了你”并用时尤为含混。"},
    {"term": "自我催眠", "meaning": "指人事后为自己的生育行为编造并相信的合理解释。", "evidence": "P003", "ambiguity": "如何区分自我催眠与真实动机，正文未提供检验方法。"},
    {"term": "无形的利刃／架上一把刀", "meaning": "比喻父母把自欺欺人的理由加诸子女，使子女承担父母的期待与失望。", "evidence": "P016", "ambiguity": "属比喻，未说明具体伤害机制。"},
    {"term": "轨道", "meaning": "指有子女的生活道路，被描述为有苦有甜、与其他道路等值。", "evidence": "P022", "ambiguity": "与“牌”的比喻并用，二者关系未说明。"},
    {"term": "英明神武", "meaning": "作者对父母自认出于智慧勇敢而选择生育这一自我形象的带讽刺称呼。", "evidence": "P017", "ambiguity": "贬义用法，非严格概念。"},
    {"term": "发给你的一手牌", "meaning": "指个人无法选择的既成处境，任务是如何把它打好。", "evidence": "P024", "ambiguity": "与“命运的安排”是否同义未说明。"}
   ],
   "examples_and_targets": [
    "养儿防老：“ta还没长到五岁，你就已经开始意识到还不知道是谁防谁老”，作者拆解用语例（P005）。",
    "天伦之乐：“ta还没十岁，你就时常怀念没ta的日子多快乐”（P006）。",
    "继承衣钵：“人家要学马斯克上火星”，含现实人物马斯克（P007）。",
    "传宗接代：“他毕业之后再也没有回过张家村”，含地名“张家村”（P008）。",
    "实现未竟的事业：作者以连续反问质疑理由的自洽性（P009）。",
    "维系夫妻感情：以反问“这个需要回答吗？”作省略式处理（P010）。",
    "家庭减税、生育补贴、唯有家庭完整者才能担任的重要职务、没有子女者受到的欺压：作者列举的政策激励与社会压力（P014）。",
    "妊娠反应与激素刺激、对未合群从众的恐惧：作者列举的生理与心理本能（P014）。",
    "“润滑油、传动零件”：机械类比，说明打算在生育发生中的次要地位（P020）。",
    "“把你的命运寄托在……”“把一把无形的利刃从子女的脖子上移走”：作者的比喻性论证用语（P016）。"
   ],
   "conditions": [
    "核心断言的适用范围被明确限定为“父母对自身处境的自我认定”，作者否认其为“客观的真理”（P016）。",
    "子女打算落空的条件是“世事的变迁和ta们不可剥夺的自由选择”（P011）。",
    "抑郁程度随对理由的确信度而变化，属条件性预测（P011）。",
    "接受该认定的收益被限定为“ta们的人生会幸福一些”，非绝对保证（P016）。",
    "生育原因的构成被表述为“一点点意外，加一点点侥幸，加强大的社会因素、生理因素的压力和推力”（P015）。",
    "轨道等值判断的适用对象为“自己无法更改（而且目前看起来是主流的）道路”（P023）。",
    "“过去如此，今日亦然，将来也不会改变”是作者对命运安排说的时间性全称断言，未附条件（P029）。"
   ],
   "rhetoric_and_tone": "第二人称“你”贯穿的劝诫口吻，语气直率、带刺而夹有自嘲与俗语。多处使用反问与设问（“你确信你生娃的时候有所谓未竟的事业吗？”“这个需要回答吗？”）。以六个“你觉得是为了……”排比逐条拆解常见理由，节奏整齐。使用“糊涂蛋”“自欺欺人”“英明神武”“天注定”等带评价色彩的口语词。末尾自设读者反驳（“你不想接受，自然能找到足够多的‘充分论述’”）并预先收束，显示论辩自觉。整体把论证重心从事实真伪转向价值排序（子女幸福优先），并以“就是这样”作断然收尾。",
   "unresolved_questions": [
    "“上天选择了你”“天赐了ta们给你”是否指有意志的超自然主体，正文未说明，属主体不明的表述（P021）。",
    "“理由”与“原因”的区分标准未形式化，何种自觉动机可算“原因”而非“理由”存在歧义（P013、P027）。",
    "P007提及“马斯克上火星”、P008提及“张家村”，均为举例中的现实／具体名称，作者未提供依据，需外部核查其指涉。",
    "社会政策激励（家庭减税、生育补贴、唯家庭完整者可任要职、无子女者受欺压）的具体制度与地区未指明（P014）。",
    "接受该自我认定是否真能减少子女所受压力，正文只作断言而未给经验依据（P016）。",
    "作者对父母“发泄到子女身上”的普遍性描述未给依据（P012）。",
    "标题“生育理由”与正文结论“没有理由，只有原因”构成张力，正文未说明标题立场。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "实际上的“理由”，只是是“天注定”三字而已。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "其意义和影响之重大超过了一切人类所能理解和预料的范围。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "因为这些理由并不足够。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "ta还没长到五岁，你就已经开始意识到还不知道是谁防谁老。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "人家根本看不上你这点衣钵。人家要学马斯克上火星。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "都有极大的可能因为世事的变迁和ta们不可剥夺的自由选择而落空。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "你对这个自欺欺人的理由有多确信，就会在它破灭时有多抑郁。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "则将自己自欺欺人的后果拿来毫无建设性的发泄到子女身上。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "生育子女，并没有什么理由，而只有当时机缘巧合原因。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "合起来构成了你生育的原因。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "构成了人生育的原因。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "我不是在告诉你这是一种“客观的真理”", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P017", "quote": "不接受这个认定，你是“英明神武”的，但是ta们脖子上会架上一把刀。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P019", "quote": "还是ta们幸福一些重要？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "而是就是因为种种你未能抗拒的原因发生了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "它既不高于、也不低于其他的道路。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "这种想象必有反噬。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "而是发给你的这手牌你要怎么打好。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "它会让你变得不必要的固执、无谓的易怒、出乎意料的易放弃、更轻易的陷入迷茫和失望。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P027", "quote": "生育没有（所谓“合理”的）理由，只有原因。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P029", "quote": "过去如此，今日亦然，将来也不会改变。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭伦理", "生育观念", "人生哲学"],
   "issue_candidates": ["生育理由与原因之别", "养儿防老等期望的落空", "社会与政策的生育激励", "父母的自我认定与子女压力"],
   "text_function_candidates": ["答疑", "劝诫", "论辩"],
   "object_candidates": ["父母", "子女", "马斯克", "张家村"],
   "working_keywords": ["天注定", "理由", "原因", "自我催眠", "命运的安排", "轨道", "一手牌", "利刃"]
  },
  "notes": "无图片节点，正文与 lexical 均为 paragraph，无版本差异。原文 P001 有重复字“只是是”，引文按原文逐字复制未作修正。作者明确把核心断言限定为自我认定而非“客观的真理”（P016），登记时应区分此限定。P007“马斯克”、P008“张家村”、P014 政策激励清单均登记为待外部核查项。"
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
