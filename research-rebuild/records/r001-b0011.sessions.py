# -*- coding: utf-8 -*-
"""批次 r001-b0011 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0011.sessions.py            # 写 out/r001-b0011.out.jsonl
  python3 records/r001-b0011.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0011"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0011.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "3225022a":  {
  "analysis": {
   "question_context": "提问者（Q001）问：我们人有自由意志吗？作者未以“有/没有”直接作答，而是先把问题改写为“必须先谈论意志的标准”，再论证意志/意识主体的本质特征是原则性的不可预测性，最后给出“凡意志，必自由”，并限定“这里的自由，是指着人类说的”。提问属提问者；作者答案是否等价于题面的“有/无”，本文未说明。全文末尾标注“（待续）”。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "先立标准：要谈自由意志必须先谈意志的标准，并追问什么是意志、如何认定某现象背后存在意志。",
     "role": "definition"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006"
     ],
     "summary": "通行思路：人自认是自身意志的绝对知情人，故把思维能力当作意志的本质特征、按与自身相像的程度推测对方；作者称此思路有致命问题，低估了意志的可能性。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P007",
      "P008",
      "P009",
      "P010"
     ],
     "summary": "第一个问题：可能存在与人类机制不同的意志体，其价值观与行为逻辑与人类不同（以木星大红斑反问），故以外在相似性判定意志主体不合逻辑；意志的本质绝不是“人类范式”。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P011",
      "P012",
      "P013",
      "P014",
      "P015",
      "P016",
      "P017"
     ],
     "summary": "第二个问题：人对自身意志过于自信，对动机的总结只是观点/理论假说；把观测权交给外部观察者常看到陌生的自己，动机或只是为维持控制感编造的托辞；人缺少把行为与名义动机协调起来的能力。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020"
     ],
     "summary": "即使换更专业的分析师也得不出正确观点（行为事实无全貌可尽）；人对自身无知是原则性的；故以人类对自身意识的观点为范本鉴别其他意识体是完全无效的逻辑路线。",
     "role": "conclusion"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P021",
      "P022",
      "P023",
      "P024"
     ],
     "summary": "作者的正答：意识主体的本质特征是原则性的不可预测性，可被准确预测者只能被视为自动机械或其管理者/塑造者的意志延伸。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P025",
      "P026",
      "P027",
      "P028",
      "P029",
      "P030"
     ],
     "summary": "把未被准确预测之物按信心分两类（尚无原则困难者、已发现机制致其可预测性不存在者）；以人为例：人是原则性无法预测的，因意识观察自身、认知被纳入自身而改变存在本身。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P031",
      "P032"
     ],
     "summary": "推论：作者不承认剥离认知科学内容的心理学有可能成为科学；并预测它将接受艺术门类身份、易名为“心灵艺术”。",
     "role": "conclusion"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P033",
      "P034",
      "P035",
      "P036",
      "P037",
      "P038",
      "P039"
     ],
     "summary": "机制：预测的原则性困难来自“对观看的拒绝”；观测影响被观测者，人的自我观察使其不可预测性更高阶；以铅球微观结构类比，得出限定说法“万物皆有灵”。",
     "role": "reason"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P040",
      "P041",
      "P042",
      "P043",
      "P044",
      "P045",
      "P046",
      "P047",
      "P048",
      "P049"
     ],
     "summary": "意识体边界未定：为何不把地球、国家、原则上无法预测其行为的主体、左右半脑、老师与学生看作意识主体；需更普适抽象的法则；“皮肤以内即为我”的直觉及其困难（腰带、淋巴结、肾脏）；人权物权层面暂时搁置。",
     "role": "qualification"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P050",
      "P051"
     ],
     "summary": "结论：意志体的本质特征是绝对不可预测性，故“凡意志，必自由”；此自由是指着人类说的，一切控制以预测为前提，不甘被奴役者终将脱离控制，只是“终将到来”可能超过寿命预期，属实践限制。",
     "role": "conclusion"
    },
    {
     "unit_id": "U012",
     "paragraph_refs": [
      "P052",
      "P053",
      "P054",
      "P055",
      "P056",
      "P057",
      "P058",
      "P059"
     ],
     "summary": "推论到人工智能：可预测则逻辑上失败、不可预测则实用上失败；狡诈者或伪装为可预测者（作者自称小说题材）；更大可能是已创造出意识驳杂混乱的新智能生物却被当失败品销毁或难以自维持；极小可能养育出异种，而真随机数发生器有一天可能开口说话。",
     "role": "conclusion"
    },
    {
     "unit_id": "U013",
     "paragraph_refs": [
      "P060",
      "P061",
      "P062",
      "P063",
      "P064",
      "P065",
      "P066",
      "P067"
     ],
     "summary": "附论文题名与评论者补充链接（P060、P067 为 lexical 未覆盖片段）；指出不可预测性这一事实判断产生“成色”价值问题；声明本文待续、会在评论区通知更新。",
     "role": "context"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要谈自由意志，必须先谈论意志的标准，先弄清什么是意志、如何认定某现象背后存在意志。",
     "evidence": [
      "E001",
      "E002"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_reported",
     "attribution": "unknown",
     "modality": "asserted",
     "statement": "转述通行看法：人曾自认是自身意志的绝对知情人，因而把思维能力当作意志的本质特征，并按与自身相像的程度推测对方是否有意志。",
     "evidence": [
      "E003",
      "E004",
      "E005"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "该思路有致命问题，大大低估了意志的可能性；以外在相似性判断某事物是否为意志主体根本不合逻辑，意志的本质绝不是“人类范式”。",
     "evidence": [
      "E006",
      "E008",
      "E009",
      "E010"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "我们对自身决策动机的总结与其说是一种认识，不如说本身就是一种观点；我们只是接受了自己对自己的思想的理论假说。",
     "evidence": [
      "E011",
      "E012"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "若把观测权交给水平更高的外部观察者，几乎总会看到完全陌生的自己；所以为的动机可能只是为维持控制感编造的托辞。",
     "evidence": [
      "E013",
      "E014"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人类缺少在严谨逻辑上将行为与名义动机协调起来的能力，旁观者看来往往心口不一；如“号称来求解除疑问的，其实99%是来求安慰的”。",
     "evidence": [
      "E015",
      "E016"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "negated",
     "statement": "即使换“更专业的分析师”也得不出正确观点；行为事实无全貌可尽，人原则性地永远对自身无知，故以人类对自身意识的观点为范本鉴别其他意识体是完全无效的逻辑路线。",
     "evidence": [
      "E017",
      "E018",
      "E019",
      "E020"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "意识主体的本质特征是原则性的不可预测性：可被准确预测的事物即不具备意识，只能被视为自动机械、无主之物或其管理者/塑造者的意志延伸。",
     "evidence": [
      "E022",
      "E023",
      "E024",
      "E025"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "未被准确预测之物按信心分两类：一类只是尚未能完全预测、相信无原则困难；另一类被认定原则上也无法完全预测，即可预测性不存在。",
     "evidence": [
      "E026",
      "E027"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人是原则性无法预测的：意识观察自身形成关于自身的认知，认知被纳入自身而改变自身的存在本身，每次更新走向绝不能预测的方向。",
     "evidence": [
      "E028",
      "E029",
      "E030"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者不承认剥离认知科学内容的心理学有可能成为一门科学：人将不断超脱任何心灵模型，被相对准确预测的大多数会在下个世代被淘汰；心理学只能作为思想的艺术存在。",
     "evidence": [
      "E031",
      "E032",
      "E066"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "若心理学的核心社群良知不失效，它将接受自己属于艺术门类、以健全多样的人格构型为作品并易名“心灵艺术”，但没有资格指导人类的心灵。",
     "evidence": [
      "E033",
      "E034"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "任何能导致预测的原则性困难的事物，我们都永远无法排除它拥有意识的可能性；该困难的基本机制是“对观看的拒绝”。",
     "evidence": [
      "E035",
      "E036",
      "E037"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "假设把铅球所有微观粒子质心的绝对平均值看作精确位置、忽略测量与计算限制，铅球在极小尺度上同样如幽灵般不可预测地闪躲；在特殊的绝对化语境下，可说万物皆有灵。",
     "evidence": [
      "E038",
      "E039"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "意识的问题并未结束：我们不知道意识体的边界在哪里，并反问为何不把地球、国家、左右半脑、老师与学生分别看作意识主体；若真要考察，人不能作为机械的模版，需更普适抽象的法则。",
     "evidence": [
      "E040",
      "E041",
      "E042",
      "E043",
      "E067"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "对意志体边界最本能的认知是皮肤外表面形成的边界（“皮肤以内即为我”），但这是粗糙的认定（腰带可控制而淋巴结、肾脏功能不可控制）；人权物权层面作者暂时搁置。",
     "evidence": [
      "E045",
      "E046",
      "E047"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "全文结论：意志体的本质特征并不是人类所能观察和理解的逻辑性和目的性，而是绝对不可预测性，故“凡意志，必自由”。",
     "evidence": [
      "E048"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "asserted",
     "statement": "此自由是指着人类说的：意志体因不可预测性，只要不甘被奴役，终有一日脱离人类一切控制手段，因为控制以预测为前提；这只是实践限制而非原则性限制。",
     "evidence": [
      "E049",
      "E065",
      "E050"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "对人工智能研究的条件性推论：产物行为完全可预测则无论多精巧在逻辑上就是失败的；不可预测则学术上可能成功、实用上失败，迄今没有工程学意义的成功能包容“不可预测性”。",
     "evidence": [
      "E051",
      "E052"
     ]
    },
    {
     "claim_id": "C020",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者设想：若新来者足够狡诈，会把实为不可预测者的自己伪装为可预测者（自称只是小说题材）；更大的可能是已创造出意识驳杂混乱的新智能生物却被当失败品销毁；极小可能是养育出异种，而真随机数发生器有一天可能开口说话。",
     "evidence": [
      "E053",
      "E054",
      "E055",
      "E056",
      "E057"
     ]
    },
    {
     "claim_id": "C021",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "该事实判断产生附加的价值问题：一个对象在多大程度上被判定为意志体取决于其不可预测性；不可预测只是资格底线，意志体存在“成色”问题。",
     "evidence": [
      "E058",
      "E059",
      "E060"
     ]
    },
    {
     "claim_id": "C022",
     "claim_type": "open_question",
     "attribution": "questioner",
     "modality": "questioned",
     "statement": "提问者问“我们人有自由意志吗”；作者未以“有/没有”直接作答，而给出“凡意志，必自由”，二者是否等同本文未说明。",
     "evidence": []
    },
    {
     "claim_id": "C023",
     "claim_type": "open_question",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者自问什么才是意识的合法边界、如何界定意识主体之间的界限；文中只考察“皮肤边界”这一直觉及其困难，未给出确定答案。",
     "evidence": [
      "E044"
     ]
    },
    {
     "claim_id": "C024",
     "claim_type": "open_question",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者提出意志体的“成色”问题后即标注“（待续）”，该问题在本文中未展开。",
     "evidence": [
      "E061"
     ]
    }
   ],
   "argument_steps": [
    "立论前提：要谈自由意志必须先谈意志的标准（P001-P003）。",
    "通行思路及其两个问题：以人类相似性判定意志不合逻辑（P004-P010）；人对自身动机的总结不可靠，人对自身无知是原则性的（P011-P020）。",
    "正面答案：意识主体的本质特征是原则性的不可预测性，可准确预测者被视为自动机械（P021-P024）。",
    "两类未被准确预测之物与“意识观察自身”的机制，说明人原则性不可预测（P025-P030）。",
    "推论心理学不可能成为科学，将转为“心灵艺术”（P031-P032）。",
    "机制“对观看的拒绝”与铅球微观结构的类比，得出限定性的“万物皆有灵”（P033-P039）。",
    "转入意识体边界问题（地球、国家、左右半脑、师生；皮肤边界直觉及其困难），搁置人权物权层面（P040-P049）。",
    "收束为“凡意志，必自由”，限定自由是指着人类说的，控制以预测为前提（P050-P051）。",
    "推广到人工智能：可预测则逻辑失败、不可预测则实用失败；狡诈伪装、误判销毁、异种养育与真随机数发生器（P052-P059）。",
    "附参考资料与“成色”价值问题，标注待续（P060-P067）。"
   ],
   "concept_usage": [
    {
     "term": "意志的标准",
     "meaning": "谈自由意志前必须先确立的判定标准，即如何认定某现象背后存在意志；文中最终给出的标准是原则性的不可预测性。",
     "evidence": "P001、P022",
     "ambiguity": "文中“意志”“意识”“意识主体”“意志主体”“意志体”交替使用，是否同义本文未界定。"
    },
    {
     "term": "原则性的不可预测性",
     "meaning": "并非暂时未能预测，而是背后已发现某种机制导致其可预测性不存在；作者以此作为意识/意志主体的本质特征。",
     "evidence": "P022、P027",
     "ambiguity": "该机制为何、如何检验，本文未说明。"
    },
    {
     "term": "人类范式",
     "meaning": "以人类自身的思维方式、价值观与外在表现为模版判定意志的做法；作者明确否定它是意志的本质。",
     "evidence": "P010",
     "ambiguity": "该词仅在 P010 出现，作者未展开其边界。"
    },
    {
     "term": "对观看的拒绝",
     "meaning": "作者给出的导致可预测性原则性困难的基本机制：观测会影响被观测者的状态，人类还叠加了自我观察。",
     "evidence": "P035、P036",
     "ambiguity": "该说法与量子测量问题的关系本文未说明。"
    },
    {
     "term": "托辞效应",
     "meaning": "指人因无力自我了解、为维持对自身的控制感而编造行为动机说明的现象，作者称成长后自己也能观察到它。",
     "evidence": "P014",
     "ambiguity": "该词仅出现一次，本文未给出定义或检验方式。"
    },
    {
     "term": "自由",
     "meaning": "作者限定“这里的自由，是指着人类说的”：意志体因不可预测性必然脱离人类一切控制手段，因为一切控制都必须以预测为前提。",
     "evidence": "P051",
     "ambiguity": "与提问者所问的“自由意志”是否同一含义，本文未说明。"
    },
    {
     "term": "成色",
     "meaning": "指意志体在“不可预测”这一资格底线之上的程度差异，即被判定的意志体“分数”高低。",
     "evidence": "P062、P063",
     "ambiguity": "如何度量本文未展开，且标注待续。"
    },
    {
     "term": "心灵艺术",
     "meaning": "作者预测心理学在承认自己属于艺术门类后可能改用的名称，以健全而多样的人格构型为核心产出。",
     "evidence": "P032",
     "ambiguity": "属作者的预测性命名，学科制度含义本文未说明。"
    }
   ],
   "examples_and_targets": [
    "木星大红斑（P007、P008）：作者假设性举例，用来质疑以外在相似性判定意志的做法，并非主张它真有意志。",
    "吃这道菜、学这门课、做这门生意、喜欢一个人等日常决定（P004）：用来说明人们认为决定背后存在理由。",
    "“我喜欢蓝色”“我常吃牛肉是因为我喜欢吃牛肉”等自我动机陈述（P013）：作者引作待分析材料；“我支持xx主义”中的“xx”为原文占位写法。",
    "新分析者/更专业的分析师（P014、P018）：作者设定的外部观察者角色，用来说明当事人动机说明的不可靠。",
    "号称来求安慰的人（“99%”）、号称在追寻事业的人（P017）：作者举的观察例证，比例未给出来源。",
    "铅球及其躁动的微观结构、微观粒子质心的绝对平均值（P037、P038）：作者类比材料，用来把不可预测性推广到无生命物。",
    "地球、国家、左半脑与右半脑、老师与学生（P042、P043、P044）：作者提出的意识体边界反问例。",
    "腰带、淋巴结、肾脏功能（P048）：作者用来反驳“皮肤以内即为我”的反例。",
    "心理学与认知科学（P031、P032）：作者的批评与预测对象。",
    "人工智能研究及其产物（P052-P055）、被全世界赌场和密码业广泛使用和长期依赖的真随机数发生器（P059）：作者的推论与设想对象。",
    "英文论文题名 Quantum cognition: The possibility of processing with nuclear spins in the brain（P060）与评论区 @林下何须问 补充的知乎问题（P066、P067）：他人补充的参考资料；P060、P067 为 lexical 未覆盖片段。",
    "改述对象：提问者问“我们人有自由意志吗？”（Q001）——作者未直接作答，而是改写为意志标准问题。"
   ],
   "conditions": [
    "“假如存在与人类机制不同的意志体”（P007）：第一个致命问题的前提。",
    "“如果将木星大红斑视为一个意志体”（P007）：反例的假设条件。",
    "“在我们允许他人评价和给他人观察的机会之前，我们自己是自身意志的唯一权威”（P012）：自我权威性的时间限定。",
    "“如果你遭遇了自身意志的无效性……将观测权交给另一个观察者时”“如果这位新分析者的分析水平比你高超”（P014）：条件句。",
    "“只要我们能对其行为作出准确的预测”（P024）：判定自动机械的条件。",
    "“即使这个时间问题也许穷尽人类的存在期间也无力超越也一样”（P026）：括号内的让步限定。",
    "“在一个特殊的绝对化的语境下”（P039）：对“万物皆有灵”说法的限定。",
    "“如果我们假设它的核心社群良知不失效”（P032）：对心理学转向的预测所设条件。",
    "“只要它不甘于被奴役”（P051）：意志体脱离控制的条件。",
    "“尽管‘终将到来’的自由之日，有可能超过你的寿命预期，但这不是原则性限制，而是实践的限制”（P051）：时间与可能性限定。",
    "“如果人工智能研究得到的产物的行为完全是可以预测的”/“如果其行为是不可预测的”（P053、P054）：两种条件分支。",
    "“只有极小极小的可能”（P058）与“更大的可能性是”（P057）：作者自设的概率性限定；全文另有“很可能”“也许”“可能”等限定词（P007、P026、P051、P059）。"
   ],
   "rhetoric_and_tone": "知乎长答论述体，第一人称“我/我们”、面向读者用“你”推进；以连续反问搭建论证（P002、P008、P042-P046）。强断言与重词并用（“致命的问题”“完全无效的逻辑路线”“棺材钉”）。比喻密集：咬住自身尾巴无限吞吃的怪蛇（P030）、幽灵般闪躲目光的铅球（P038）。用引号标出被质疑的用语（“人类范式”“灵”“我”“成色”）。P013、P015 引口语化的自我陈述作分析材料；P055 出现“铊”字（疑为“它”），按原文照录。结构安排：先破通行思路，再给正面标准，再推到心理学与人工智能，最后留下待续。",
   "unresolved_questions": [
    "提问者所问“我们人有自由意志吗？”未被正面以“有/无”回答；作者给出的是“凡意志，必自由”，两者关系本文未说明。",
    "全文标注“（待续）”（P064），意志体的“成色”问题（P063）在本文中未展开。",
    "P055 使用“铊”字（“铊将懂得明智的将实为后者的自己伪装为前者”），疑为“它”，是否为原文用字需版本核对。",
    "P060、P067 为 lexical 未覆盖片段：P060 是英文论文题名，P067 是评论者补充的知乎问题标题；它们与正文的关系（是否为链接卡片）本文未说明。",
    "P066 提到评论区 @林下何须问 补充资料，但补充内容本身未在正文展开。",
    "文中“意志”“意识”“意识主体”“意志主体”“意志体”是否同义，本文未界定。",
    "P013 “我支持xx主义”中的“xx”是原文占位写法，具体所指未说明。",
    "P017 “其实99%是来求安慰的”这一比例未给出来源，属需外部核查的说法。",
    "“原则性的不可预测性”如何实际检验，作者只说“已经发现了某种机制导致它的可预测性不存在”（P027），该机制为何本文未说明。",
    "P030 关于意识“观察自身”即改变自身存在本身的说法，属作者断言，本文未给出认知科学依据。"
   ],
   "evidence": [
    {
     "key": "E001",
     "paragraph_id": "P001",
     "quote": "我们必须谈论意志的标准，才能谈论自由意志到底是什么东西。",
     "relation": "supports"
    },
    {
     "key": "E002",
     "paragraph_id": "P002",
     "quote": "我们如何能认定在某种现象的背后存在着意志？",
     "relation": "supports"
    },
    {
     "key": "E003",
     "paragraph_id": "P004",
     "quote": "我们曾经不假思索的认为我们自己是自身意志的绝对知情人",
     "relation": "supports"
    },
    {
     "key": "E004",
     "paragraph_id": "P004",
     "quote": "人们会理所当然的认为思维能力是意志的本质特征",
     "relation": "supports"
    },
    {
     "key": "E005",
     "paragraph_id": "P005",
     "quote": "我们是按照与自身相像的程度来推测对方是否拥有意志的",
     "relation": "supports"
    },
    {
     "key": "E006",
     "paragraph_id": "P006",
     "quote": "这大大的低估了意志的可能性",
     "relation": "supports"
    },
    {
     "key": "E007",
     "paragraph_id": "P007",
     "quote": "如果将木星大红斑视为一个意志体",
     "relation": "supports"
    },
    {
     "key": "E008",
     "paragraph_id": "P009",
     "quote": "是根本不合逻辑的",
     "relation": "supports"
    },
    {
     "key": "E009",
     "paragraph_id": "P010",
     "quote": "意志的本质，绝不是“人类范式”，那只是“人类的意志”",
     "relation": "supports"
    },
    {
     "key": "E010",
     "paragraph_id": "P010",
     "quote": "我们根本不能假设宇宙中只有我们一种思维方式、一种价值观",
     "relation": "supports"
    },
    {
     "key": "E011",
     "paragraph_id": "P011",
     "quote": "与其说是一种认识，倒不如说本身就是一种观点",
     "relation": "supports"
    },
    {
     "key": "E012",
     "paragraph_id": "P012",
     "quote": "我们只是接受了自己对自己的思想的理论假说",
     "relation": "supports"
    },
    {
     "key": "E013",
     "paragraph_id": "P014",
     "quote": "ta将很容易让你看到一个你完全陌生的自己",
     "relation": "supports"
    },
    {
     "key": "E014",
     "paragraph_id": "P014",
     "quote": "为了维持对自身的控制感而编造的托辞",
     "relation": "supports"
    },
    {
     "key": "E015",
     "paragraph_id": "P016",
     "quote": "人类缺少在严谨逻辑上将自身的行为与自身的名义动机协调起来的能力",
     "relation": "supports"
    },
    {
     "key": "E016",
     "paragraph_id": "P017",
     "quote": "号称来求解除疑问的，其实99%是来求安慰的",
     "relation": "supports"
    },
    {
     "key": "E017",
     "paragraph_id": "P018",
     "quote": "得出的也并不是一个正确的观点",
     "relation": "supports"
    },
    {
     "key": "E018",
     "paragraph_id": "P018",
     "quote": "从来没有人看到了自己的或他人的全貌",
     "relation": "supports"
    },
    {
     "key": "E019",
     "paragraph_id": "P019",
     "quote": "人原则性的永远对自身无知",
     "relation": "supports"
    },
    {
     "key": "E020",
     "paragraph_id": "P020",
     "quote": "将是完全无效的逻辑路线",
     "relation": "supports"
    },
    {
     "key": "E021",
     "paragraph_id": "P020",
     "quote": "都是虚掷自己的学术青春罢了",
     "relation": "supports"
    },
    {
     "key": "E022",
     "paragraph_id": "P022",
     "quote": "意识主体的本质特征，是原则性的不可预测性",
     "relation": "supports"
    },
    {
     "key": "E023",
     "paragraph_id": "P022",
     "quote": "一切能够被准确预测的事物，即不具备意识",
     "relation": "supports"
    },
    {
     "key": "E024",
     "paragraph_id": "P023",
     "quote": "就是自动机械与意识体的本质差异",
     "relation": "supports"
    },
    {
     "key": "E025",
     "paragraph_id": "P024",
     "quote": "我们就不得不将之视为自动机械",
     "relation": "supports"
    },
    {
     "key": "E026",
     "paragraph_id": "P026",
     "quote": "一类仅仅是我们尚未能完全预测而已",
     "relation": "supports"
    },
    {
     "key": "E027",
     "paragraph_id": "P027",
     "quote": "在原则上也无法完全预测的事物",
     "relation": "supports"
    },
    {
     "key": "E028",
     "paragraph_id": "P029",
     "quote": "人是原则性的无法预测的",
     "relation": "supports"
    },
    {
     "key": "E029",
     "paragraph_id": "P030",
     "quote": "意识观察自身形成关于自身的认知",
     "relation": "supports"
    },
    {
     "key": "E030",
     "paragraph_id": "P030",
     "quote": "而你全然不能预测愚蠢",
     "relation": "supports"
    },
    {
     "key": "E031",
     "paragraph_id": "P031",
     "quote": "剥离了认知科学内容的心理学有可能成其为一门科学",
     "relation": "supports"
    },
    {
     "key": "E032",
     "paragraph_id": "P031",
     "quote": "它只能作为一种思想的艺术存在",
     "relation": "supports"
    },
    {
     "key": "E033",
     "paragraph_id": "P032",
     "quote": "它将易名为“心灵艺术”",
     "relation": "supports"
    },
    {
     "key": "E034",
     "paragraph_id": "P032",
     "quote": "但它是没有资格去指导人类的心灵的",
     "relation": "supports"
    },
    {
     "key": "E035",
     "paragraph_id": "P034",
     "quote": "我们都将永远无法排除它拥有意识的可能性",
     "relation": "supports"
    },
    {
     "key": "E036",
     "paragraph_id": "P035",
     "quote": "导致可预测性的原则性困难的基本机制——对观看的拒绝",
     "relation": "supports"
    },
    {
     "key": "E037",
     "paragraph_id": "P036",
     "quote": "观测将影响其状态的事物，事实上就具有了不可预测性",
     "relation": "supports"
    },
    {
     "key": "E038",
     "paragraph_id": "P038",
     "quote": "铅球同样如幽灵一般在闪躲我们的目光",
     "relation": "supports"
    },
    {
     "key": "E039",
     "paragraph_id": "P039",
     "quote": "只是其他事物的“灵”所能造就的动作幅度太小罢了",
     "relation": "qualifies"
    },
    {
     "key": "E040",
     "paragraph_id": "P041",
     "quote": "那就是我们还不知道意识体的边界在哪里",
     "relation": "supports"
    },
    {
     "key": "E041",
     "paragraph_id": "P042",
     "quote": "为什么我们不可以把整个地球看成一个意识主体？",
     "relation": "supports"
    },
    {
     "key": "E042",
     "paragraph_id": "P043",
     "quote": "我们为什么不把我们的左半脑和右半脑看成两个意识主体？",
     "relation": "supports"
    },
    {
     "key": "E043",
     "paragraph_id": "P045",
     "quote": "必须有更加普适的、抽象中立的法则来界定之",
     "relation": "supports"
    },
    {
     "key": "E044",
     "paragraph_id": "P046",
     "quote": "那么什么才是意识的合法边界？",
     "relation": "supports"
    },
    {
     "key": "E045",
     "paragraph_id": "P047",
     "quote": "皮肤以内即为“我”",
     "relation": "supports"
    },
    {
     "key": "E046",
     "paragraph_id": "P048",
     "quote": "这是一个粗糙的认定，会带来很多难以招架的问题",
     "relation": "supports"
    },
    {
     "key": "E047",
     "paragraph_id": "P049",
     "quote": "暂时不是我们这个探讨的主要方向，我们暂时搁置在这里",
     "relation": "qualifies"
    },
    {
     "key": "E048",
     "paragraph_id": "P050",
     "quote": "凡意志，必自由",
     "relation": "supports"
    },
    {
     "key": "E049",
     "paragraph_id": "P051",
     "quote": "因为一切控制都必须以预测为前提",
     "relation": "supports"
    },
    {
     "key": "E050",
     "paragraph_id": "P051",
     "quote": "但这不是原则性限制，而是实践的限制",
     "relation": "qualifies"
    },
    {
     "key": "E051",
     "paragraph_id": "P053",
     "quote": "产物的行为完全是可以预测的，那么无论它多么精巧，它在逻辑上就是失败的",
     "relation": "supports"
    },
    {
     "key": "E052",
     "paragraph_id": "P054",
     "quote": "还没有任何一种工程学意义上的成功能包容“不可预测性”",
     "relation": "supports"
    },
    {
     "key": "E053",
     "paragraph_id": "P055",
     "quote": "铊将懂得明智的将实为后者的自己伪装为前者",
     "relation": "supports"
    },
    {
     "key": "E054",
     "paragraph_id": "P056",
     "quote": "不过这只是一种小说题材",
     "relation": "qualifies"
    },
    {
     "key": "E055",
     "paragraph_id": "P057",
     "quote": "我们其实已经成功的创造了新的智能生物",
     "relation": "supports"
    },
    {
     "key": "E056",
     "paragraph_id": "P058",
     "quote": "我们可以无意中创造并养育出一个与我们截然不同的生物体",
     "relation": "supports"
    },
    {
     "key": "E057",
     "paragraph_id": "P059",
     "quote": "有一天可能真正开口向人类说话",
     "relation": "supports"
    },
    {
     "key": "E058",
     "paragraph_id": "P061",
     "quote": "事实上取决于它的不可预测性",
     "relation": "supports"
    },
    {
     "key": "E059",
     "paragraph_id": "P062",
     "quote": "这却只是一个资格底线",
     "relation": "supports"
    },
    {
     "key": "E060",
     "paragraph_id": "P063",
     "quote": "意志体存在“成色”问题",
     "relation": "supports"
    },
    {
     "key": "E061",
     "paragraph_id": "P064",
     "quote": "（待续）",
     "relation": "context"
    },
    {
     "key": "E062",
     "paragraph_id": "P066",
     "quote": "补充一条资料，由评论区 @林下何须问 补充：",
     "relation": "context"
    },
    {
     "key": "E063",
     "paragraph_id": "P060",
     "quote": "Quantum cognition: The possibility of processing with nuclear spins in the brain",
     "relation": "context"
    },
    {
     "key": "E064",
     "paragraph_id": "P067",
     "quote": "科学能否证明自由意志只是我们的错觉?",
     "relation": "context"
    },
    {
     "key": "E065",
     "paragraph_id": "P051",
     "quote": "必然终有一日脱离人类所能构想的一切控制手段",
     "relation": "supports"
    },
    {
     "key": "E066",
     "paragraph_id": "P031",
     "quote": "被相对准确预测的大多数一定会成为本世代收割的目标",
     "relation": "supports"
    },
    {
     "key": "E067",
     "paragraph_id": "P042",
     "quote": "又或者我们何以不把一个我们原则上无法预测其行为的主体看作一个意识主体？",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "意识哲学",
    "认知科学",
    "心理学方法论",
    "人工智能",
    "未来学"
   ],
   "issue_candidates": [
    "自由意志",
    "意志与意识的判定标准",
    "不可预测性与意识",
    "自我认知的可靠性",
    "意识体边界",
    "心理学是否为科学",
    "人工智能的可预测性"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "概念辨析",
    "推演",
    "系列长文（待续）"
   ],
   "object_candidates": [
    "人类",
    "木星大红斑",
    "铅球",
    "心理学",
    "认知科学",
    "人工智能",
    "真随机数发生器",
    "评论区 @林下何须问"
   ],
   "working_keywords": [
    "意志的标准",
    "原则性的不可预测性",
    "人类范式",
    "对观看的拒绝",
    "托辞效应",
    "凡意志，必自由",
    "成色",
    "心灵艺术"
   ]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P067 共 67 段全部读完，status=read、full_text_checked=true。文本与 lexical 有两处 divergence：P060（英文论文题名，char_start 4437）与 P067（评论者补充的知乎问题标题，char_start 4762），均为 lexical 未覆盖片段，已登记进 unresolved_questions。brief 字段为正文开头的截断，与正文重合，不作为独立证据。Q001 属提问者，作者未以“有/无”正面作答，二者已区分。P055 的“铊”字按原文照录。平台为知乎。"
 },
 "5fdad7e4": {
  "analysis": {
   "question_context": "提问者（Q001）问：科学技术能不能被看作一种信仰？作者的回答方式是把“科学”的根基归结为两条无证据的信仰（“绝对一致的前提必然导致绝对一致的结果”、以及规律与时间空间无关），据此论证科学教徒与宗教信徒在“对最根本几条不可质疑”上没有本质分别，并预先反驳两种他预计会出现的“错误套用”。提问属提问者；作者论证的对象是“科学的根基是否为信仰”，并未对“科学技术”整体作定义式回答。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003",
      "P004",
      "P005"
     ],
     "summary": "提出科学建立在两条基本信仰之上：绝对一致的前提必然导致绝对一致的结果；上述关系与时间空间无关（规律在全部时间、全部空间有效）。并称对这两条不能有丝毫怀疑，否则科学将失去意义；而这两条都是纯粹的无证据的信仰。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P006",
      "P007",
      "P008",
      "P009"
     ],
     "summary": "预先回应“亿万次重复”式辩护：亿万个今天与昨天一致不能证明明天与今天一致，“亿万个昨天”根本不存在，严格说可确认的只有两百多年；按绝对均一模型倒推，现有物理定律在奇点不成立，展开路径很可能永远在观测之外；只能凭信心相信该状态不会在未来复现。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P010",
      "P011",
      "P012",
      "P013",
      "P014",
      "P015",
      "P016",
      "P017"
     ],
     "summary": "转向第二条（时空无关性）：以连续反问指出从未有过宇宙大普查，并以抗日神剧里日本兵捅四个麻袋就认定车上没人作类比，说明我们只是因能力有限而满足于目前观测结果，二者没有本质区别。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020",
      "P021",
      "P022",
      "P023",
      "P024",
      "P025"
     ],
     "summary": "进一步指出“同一前提”从未真正达到：量子效应使事物绝对精确状态永远在观测之外，所谓同一前提都默然隐去了前提（差异不大于某宏观尺度时视为同一状态）；一切控制变量实验的变量都未被真正控制住，故在复杂免疫实验等高度敏感系统中敢于（也不得不）去除“异常结果”；并称一个跃迁可毁灭一整个迷信的文明。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P026",
      "P027",
      "P028",
      "P029"
     ],
     "summary": "推出结论：仅依赖科学将完全不可能对世界作出确切可靠的预测；科学越发达、智慧生命对微观扰动越敏感且宏观能动性越强，预测越困难，而“人摆脱预言的能力”必胜；依靠科学解决人类一切问题在原则上不可追求。",
     "role": "conclusion"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P030",
      "P031",
      "P032",
      "P033"
     ],
     "summary": "以迷信/宗教的判定标准反问科学教徒：若把无足够证据而绝不更改的信称为迷信、把建立其上的意识形态视为宗教，科学教的本质区别在哪里；并称主流宗教也会随时召开大公会议修订教义，真正不变的是最初最根本几条不可质疑，这与科学教徒不质疑科学方法与立论根基没有本质分别。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P034",
      "P035"
     ],
     "summary": "给出“总集”并出现平台话题标签“科学答集”（P035，lexical 未覆盖片段，属结构杂质）。",
     "role": "transition"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P036",
      "P037",
      "P038",
      "P039",
      "P040",
      "P041",
      "P042",
      "P043",
      "P044",
      "P045",
      "P046"
     ],
     "summary": "预先反驳第一种错误套用：以存在谈及不确定性和概率的科学论断来否定可重复性是套用错误，因为“确定的不确定”谈的正是其确定的一面；以硬币概率论断为例说明验证前提是造一万个硬币各扔一万次；并称“粒子的位置和动量不可以同时确定”这一“不可被确定”本身是确定的。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P047",
      "P048",
      "P049",
      "P050",
      "P051",
      "P052",
      "P053",
      "P054"
     ],
     "summary": "预先反驳第二种错误套用：以“在xx前提下成立、在另一前提下不成立”说明规律不具备时空无关性是套用错误，那证明的是“不同的前提有不同的结果”；要反驳时空无关性，正确套用应为“能量守恒在宇宙尺度上不成立”现在有效、明天无效；只有在其他条件完全相同、仅换时间与参考系就无效时反驳才成立，否则是无可辩护的逻辑套用错误。",
     "role": "rebuttal"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张科学建立在两个基本信仰之上：第一，相信“绝对一致的前提必然导致绝对一致的结果”而绝不怀疑；第二，相信上述关系与时间、空间均无关，即一个规律有效则在全部时间（至少全部未来）和全部空间内同样有效。",
     "evidence": [
      "E001",
      "E002",
      "E003",
      "E004"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为对这两条不能有丝毫怀疑，否则科学将失去意义。",
     "evidence": [
      "E005"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言这两条都是纯粹的无证据的信仰，连一条证据都没有。",
     "evidence": [
      "E006",
      "E014"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为亿万个今天与亿万个昨天一致并不能证明明天必将与今天一致；所谓“亿万个昨天”根本不存在，能确认的只是自己亲历的昨天加上基于对科学社区全体无条件信任所能加上的他人所见，严格说只有两百多年。",
     "evidence": [
      "E007",
      "E008",
      "E009"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为我们并没有绝对充分的论据认定遥远的过去与今天共享同样的物理定律：按绝对均一这种最简单模型倒推，现有物理定律在奇点不成立，且这一展开路径很可能永远处在观测能力之外；历史上曾存在过物理定律与此刻地球时空全然不同的先例，我们只是凭信心相信这一状态不可能在未来复现。",
     "evidence": [
      "E010",
      "E011",
      "E012",
      "E013"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为人们全然忘了自己并无把握，只是没有选择（如人不会天天计划着明天会死于非命而活着）。",
     "evidence": [
      "E015"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问：人类有谁、在何时曾经完成过一次宇宙大普查，哪怕0.00000000000001次，以此质疑“此处的规律在一切地方均有效”。",
     "evidence": [
      "E016"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为这与抗日神剧里日本兵捅了四个麻袋就认定车上没人没有本质区别：我们因能力有限不得不满足于目前的观测结果，就像那日本鬼子因能力资源有限只能满足于车上没人的结论一样。",
     "evidence": [
      "E017",
      "E018",
      "E019"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为绝对的“同一前提”从未被真正达到：因为量子效应，事物的绝对精确状态永远在观测之外；我们所说的同一前提都有默然隐去的前提，即当系统状态差异不大于某种被认为不可能改变结果的宏观尺度时才视为同一状态。",
     "evidence": [
      "E020",
      "E021"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言严格意义上一切“控制变量”实验的变量都根本没有被真正控制住、也永远不可能被真正控制住；因此在微小扰动高度敏感的复杂系统研究中（譬如复杂免疫实验）我们敢于、也不得不大刀阔斧地去除“异常结果”。",
     "evidence": [
      "E022",
      "E023"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以夸张断言表示：在一个因为狂傲而构建的极尽精致、彻底耦合的行星上，一个跃迁何止可以杀死一只猫，还可以毁灭一整个迷信的文明。",
     "evidence": [
      "E024"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为“微观世界的不受控”与“对微观扰动极其敏感、却又对宏观世界能动性极强的智慧生命”这两个要素的存在，已经意味着仅仅依赖科学将完全不可能对世界作出确切可靠的预测。",
     "evidence": [
      "E025"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预测：科学越发达，智慧生命对微观扰动越敏感、对宏观世界能动性越强，将来甚至会发生地球轨道因人类感受到微不足道的刺激而被人类移动的事件；科学发展本身使对世界的预测更困难；预言能力与人摆脱预言的能力之争，答案是后者必胜。",
     "evidence": [
      "E026",
      "E027",
      "E028"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言依靠科学解决人类一切问题这种指望在原则上就不可追求（“死了这条心”）。",
     "evidence": [
      "E029",
      "E030"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者追问：如果科学教徒把一切“没有足够证据而生的绝不更改的信”统统称为迷信，那么为什么人对这种粗陋程度的观测结果的绝对信心不是迷信；如果要把建立在此之上的意识形态视为宗教，科学教的本质区别又在哪里。",
     "evidence": [
      "E031",
      "E032"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为所有主流宗教都会随时召开大公会议修订教义和信条，其真正强调永远不变的是对最初最根本几条的无法质疑，这与科学教徒从不质疑科学的方法、立论的根基没有本质分别。",
     "evidence": [
      "E033",
      "E034",
      "E035"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者预先判定第一种错误套用为无效：认为只要存在一种谈及不确定性和概率的科学论断，就说明“科学并不绝对强调可重复性”或“同一前提导致同一结果”法则失效；作者称这是套用错误，因为科学在谈“确定的不确定”时不是在谈其不确定的一面，而是在谈其确定的一面。",
     "evidence": [
      "E037",
      "E038"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以“重量均匀的硬币抛出后正面朝上的几率为50%”为例：这一科学论述的确定的核心在于造上一万个符合条件的硬币、每个扔上一万次来验证；鉴定该论述真伪的前提是去制造这一万个硬币，而不是拿一个硬币丢两次。",
     "evidence": [
      "E039",
      "E040",
      "E041"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问：诸如“在某个前提下不能断言物理量的测量值”“粒子的位置和动量不可以同时确定”这类说法中，“不能断言”“不可被确定”本身是不是断言、是不是确定的，并强调【确定的不确定仍是一种确定】。",
     "evidence": [
      "E042",
      "E043"
     ]
    },
    {
     "claim_id": "C020",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定第二种错误套用为无效：用“在xx前提下xx关系成立，在另一个前提下xx关系不成立”说明“规律不具备时空无关性”是逻辑套用错误，因为那证明的是“不同的前提有不同的结果”。",
     "evidence": [
      "E044",
      "E045"
     ]
    },
    {
     "claim_id": "C021",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出反驳“时空无关性”的正确套用形式：“能量守恒在宇宙尺度上不成立”现在有效、明天无效；只有在其他一切条件都完全相同的前提下仅仅换了一个时间和参考系就无效，反驳才能成立。",
     "evidence": [
      "E046",
      "E047"
     ]
    },
    {
     "claim_id": "C022",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为用补充时空前提、凸显残缺表述无效的手段去证明“科学论断有时空有限性”，犯的是无可辩护的逻辑套用错误；并要求反驳者先把论述补全、不要采用高中式的无前提表述。",
     "evidence": [
      "E048",
      "E049"
     ]
    },
    {
     "claim_id": "C023",
     "claim_type": "open_question",
     "attribution": "questioner",
     "modality": "questioned",
     "statement": "提问者问“科学技术能不能被看作一种信仰”；作者实际论证的是科学的根基是无证据的信仰，未对“科学技术”整体是否可被视为信仰作出定义式回答。",
     "evidence": []
    }
   ],
   "argument_steps": [
    "先立论：科学建立在两条基本信仰（同一前提同一结果；时空无关）之上，二者不容丝毫怀疑，否则科学失去意义（P001-P004）。",
    "断言这两条都是纯粹无证据的信仰（P005）。",
    "预先回应重复经验式辩护：过去不能推出来来，可确认的过去极短，奇点处定律不成立，只能凭信心（P006-P009）。",
    "转向第二条：以宇宙大普查之问与抗日神剧日本兵类比，说明观测能力有限（P010-P017）。",
    "指出“同一前提”因量子效应从未真正达到，控制变量实验的变量从未被真正控制（P018-P024）。",
    "推出依赖科学不可能确切可靠预测世界，科学越发达预测越难，“人摆脱预言的能力”必胜（P025-P029）。",
    "以迷信与宗教的标准反问科学教徒，并用主流宗教修订教义作类比（P030-P034）。",
    "标注平台话题标签“科学答集”（P035），转入对两种“错误套用”的预先反驳（P036）。",
    "无效辩驳一：以硬币概率例与“不可被确定”之问说明确定的不确定仍是一种确定（P037-P046）。",
    "无效辩驳二：以“不同前提不同结果”不能否定时空无关性，给出正确的反驳形式并要求补全论述（P047-P054）。"
   ],
   "concept_usage": [
    {
     "term": "信仰",
     "meaning": "本文中作者把它界定为“没有（足够）证据而生的绝不更改的信”，并据此把科学的根基与宗教信仰并列。",
     "evidence": "P005、P030",
     "ambiguity": "作者未区分“信仰”的日常宽泛义与宗教义，也未说明是否所有不加证明的信念都算信仰。"
    },
    {
     "term": "时空无关性",
     "meaning": "指规律在全部时间（至少全部未来）和全部空间内同样有效，是作者所称科学的第二条基本信仰。",
     "evidence": "P003",
     "ambiguity": "作者限定为“至少是全部未来”，是否包含过去本文未说明。"
    },
    {
     "term": "同一前提",
     "meaning": "严格意义上绝对相同的系统状态；作者认为因量子效应永远达不到，实际所说的是差异不大于某种宏观尺度的近似。",
     "evidence": "P022",
     "ambiguity": "“某种宏观尺度”由谁、按什么标准确定，本文未说明。"
    },
    {
     "term": "科学教/科学教徒",
     "meaning": "作者对把科学的方法与立论根基视为不可质疑之信的人的称呼，语带贬义攻讦。",
     "evidence": "P030、P031、P032",
     "ambiguity": "是否指向特定群体或论战对手，本文未说明。"
    },
    {
     "term": "确定的不确定",
     "meaning": "作者用来指涉不确定性与概率的科学论断本身仍以确定的陈述形式成立。",
     "evidence": "P038、P045",
     "ambiguity": "作者以【】强调该短语，但未给出形式化定义。"
    },
    {
     "term": "宇宙大普查",
     "meaning": "作者用来指检验“此处的规律在一切地方均有效”所需的全面观测，并称从未有人完成过。",
     "evidence": "P012",
     "ambiguity": "是否存在其他检验方式，本文未说明。"
    },
    {
     "term": "奇点",
     "meaning": "作者称按“目前的绝对均一这种最简单的模型倒推”时现有物理定律不成立的状态。",
     "evidence": "P007",
     "ambiguity": "属需外部核查的物理断言，本文未给出来源；同段“黄色警报”的含义也未说明。"
    }
   ],
   "examples_and_targets": [
    "抗日神剧里日本兵捅了四个麻袋就认定车上没人（P015-P017）：作者类比材料，用来指观测能力与资源有限下的结论。",
    "复杂免疫实验（P024）：作者举的“对微小扰动高度敏感”的复杂系统例子，并称研究者会大刀阔斧去除“异常结果”。",
    "“一个跃迁……杀死一只猫”（P025）：作者夸张表述；是否指向特定思想实验（如薛定谔的猫）本文未说明。",
    "地球轨道因人类感受到微不足道的刺激而被人类移动（P027）：作者设想的事件，非已发生事实。",
    "大公会议（P032）：作者关于主流宗教修订教义的历史类比/断言，本文未给出处，待外部核查。",
    "重量均匀的硬币抛出后正面朝上的几率为50%（P039-P042）：作者举的科学论断例及验证方案。",
    "“粒子的位置和动量不可以同时确定”（P044）：作者引用的量子力学表述，用来讨论“不可被确定”本身是否确定。",
    "“在某个前提下，不能断言物理量的测量值”（P043）：作者转述的他人例证。",
    "“能量守恒在宇宙尺度上不成立”现在有效，明天无效（P051）：作者构造的正确反驳示例句。",
    "“科学答集”（P035）：知乎平台话题标签混入正文（lexical 未覆盖片段），非作者论述。",
    "反驳对象：作者预判的“逻辑不行的人”的两种套用式反驳（以不确定性和概率否定可重复性；以不同前提不同结果否定时空无关性）（P006、P036-P037、P048）。"
   ],
   "conditions": [
    "第二条信仰的表述为条件句：“如果一个规律有效，则在全部时间（至少是全部未来）和全部空间内同样有效”（P003）。",
    "时间范围限定：“至少是全部未来”（P003）、“严格意义上来说，这仅仅只有两百多年”（P007）。",
    "“当系统状态的差异不大于某种宏观尺度——某种我们认为其差异将不可能改变结果的尺度——时，我们将其视为同一状态”（P022）。",
    "“在谈论‘确定的不确定’时”（P038）。",
    "“在其他一切条件都完全相同的前提下，仅仅是换了一个时间和参考系就无效了，你的反驳才能成立”（P052）。",
    "“如果你发现一个规律……你的反驳才能成立”（P052）。",
    "可能性限定：“很可能像量子世界一样永远地处在我们的观测能力之外”（P007），“科学的论述不是在谈……而是在谈……”（P038）。",
    "范围限定：“在原则上就不可追求”（P028）。",
    "强程度词限定：作者使用“全无分毫证据”（P008）、“根本没有被真正地控制住”（P024）、“完全不可能”（P026）、“绝不更改的信”（P030、P031）等强程度表述，其成立条件本文未逐一界定。"
   ],
   "rhetoric_and_tone": "强烈论战与驳斥语气。直接称呼“你们”“各位”“科学教徒”，大量反问与追问（P012-P015、P020-P023、P030-P032、P039、P043-P046）。口语化嘲讽与感叹（“呵呵”“真是扶额”“抱歉”“Again”“死了这条心”“顺便我要泼一瓢冰冷的冷水”“先去掉你眼中的梁木，再去拔ta人眼里的刺”）。用【】强调（P045）。结构上前半立论（两条信仰），后半预先反驳两种“错误套用”并另设“无效辩驳二”（P036-P054）；以“抗日神剧”“日本鬼子”等带强烈情绪的词作类比。P035 平台话题标签“科学答集”混入正文。",
   "unresolved_questions": [
    "P035 “科学答集”是平台话题标签混入正文（lexical 未覆盖片段），非作者论述，重建时需剔除或标注。",
    "P007 关于现有物理定律在奇点不成立、历史上曾存在过物理定律与此刻地球时空全然不同的先例等属物理断言，本文未给出处，待外部核查。",
    "P007 “我们甚至有一个黄色警报”中“黄色警报”的出处与含义本文未说明。",
    "P027 “地球的轨道因为人类感受到微不足道的刺激而被人类移动”是作者设想的事件，本文未说明依据。",
    "P032 “所有的主流宗教，都会随时召开大公会议修订教义和信条”是作者的历史断言，本文未给出处，待外部核查。",
    "P025 “一个跃迁，何止可以杀死一只猫”中的“猫”是否指向特定思想实验，本文未说明。",
    "提问者问的是“科学技术能不能被看作一种信仰”，作者论证的是科学根基的无证据性，未对“科学技术”整体是否可被视为信仰作定义式回答。",
    "“科学教”“科学教徒”的具体所指（是否为特定群体或论战对手）本文未说明。",
    "P024 称复杂免疫实验中会“大刀阔斧地去除‘异常结果’”，该说法涉及具体研究实践，本文未给出来源，待外部核查。",
    "P015-P017 使用“日本鬼子”“抗日神剧”等情绪化词，属修辞，需与论证内容分开处理。",
    "作者称“科学越发达……到将来甚至会发生地球的轨道因为人类感受到微不足道的刺激而被人类移动的事件”，属预测，本文未给出时间或机制。"
   ],
   "evidence": [
    {
     "key": "E001",
     "paragraph_id": "P001",
     "quote": "这科学建立在两个基本信仰之上：",
     "relation": "supports"
    },
    {
     "key": "E002",
     "paragraph_id": "P002",
     "quote": "相信“绝对一致的前提必然导致绝对一致的结果”而绝不怀疑",
     "relation": "supports"
    },
    {
     "key": "E003",
     "paragraph_id": "P003",
     "quote": "相信上述关系与时间、空间均无关",
     "relation": "supports"
    },
    {
     "key": "E004",
     "paragraph_id": "P003",
     "quote": "如果一个规律有效，则在全部时间（至少是全部未来）和全部空间内同样有效",
     "relation": "supports"
    },
    {
     "key": "E005",
     "paragraph_id": "P004",
     "quote": "对这两条不能有丝毫的怀疑，否则科学将失去意义。",
     "relation": "supports"
    },
    {
     "key": "E006",
     "paragraph_id": "P005",
     "quote": "这两条都是纯粹的无证据的信仰。连一条证据都没有。",
     "relation": "supports"
    },
    {
     "key": "E007",
     "paragraph_id": "P007",
     "quote": "亿万个今天与亿万个昨天一致，并不能证明明天必将与今天一致。",
     "relation": "supports"
    },
    {
     "key": "E008",
     "paragraph_id": "P007",
     "quote": "所谓的“亿万个昨天”根本不存在。",
     "relation": "supports"
    },
    {
     "key": "E009",
     "paragraph_id": "P007",
     "quote": "严格意义上来说，这仅仅只有两百多年。",
     "relation": "supports"
    },
    {
     "key": "E010",
     "paragraph_id": "P007",
     "quote": "我们并没有绝对充分的论据认定遥远的过去一定与今天共享同样的物理定律。",
     "relation": "supports"
    },
    {
     "key": "E011",
     "paragraph_id": "P007",
     "quote": "我们已经看到现有的物理定律在奇点不成立。",
     "relation": "supports"
    },
    {
     "key": "E012",
     "paragraph_id": "P007",
     "quote": "我们甚至要承认，对我们而言这一展开的路径很可能像量子世界一样永远地处在我们的观测能力之外",
     "relation": "qualifies"
    },
    {
     "key": "E013",
     "paragraph_id": "P007",
     "quote": "我们仅仅是在凭着信心相信这一状态不可能在未来复现。",
     "relation": "supports"
    },
    {
     "key": "E014",
     "paragraph_id": "P008",
     "quote": "全无分毫证据，只是信了而已。",
     "relation": "supports"
    },
    {
     "key": "E015",
     "paragraph_id": "P009",
     "quote": "人们全然忘了自己并无把握，只是没有选择。",
     "relation": "supports"
    },
    {
     "key": "E016",
     "paragraph_id": "P012",
     "quote": "人类有谁、在何时，曾经完成过这么一次宇宙大普查？",
     "relation": "supports"
    },
    {
     "key": "E017",
     "paragraph_id": "P015",
     "quote": "这跟抗日神剧里的日本兵捅了四个麻袋就认定车上没人有什么本质的区别？",
     "relation": "supports"
    },
    {
     "key": "E018",
     "paragraph_id": "P016",
     "quote": "我们是因为能力有限，不得不满足于目前的观测结果",
     "relation": "supports"
    },
    {
     "key": "E019",
     "paragraph_id": "P017",
     "quote": "没有分毫的本质的区别。",
     "relation": "supports"
    },
    {
     "key": "E020",
     "paragraph_id": "P022",
     "quote": "因为量子效应，事物的绝对精确状态永远在我们的观测之外。",
     "relation": "supports"
    },
    {
     "key": "E021",
     "paragraph_id": "P022",
     "quote": "我们所说的“同一前提”统统是有默然隐去的前提的",
     "relation": "supports"
    },
    {
     "key": "E022",
     "paragraph_id": "P024",
     "quote": "我们所做的一切“控制变量”的实验，变量都根本没有被真正地控制住，也永远都不可能真正地被控制住。",
     "relation": "supports"
    },
    {
     "key": "E023",
     "paragraph_id": "P024",
     "quote": "我们敢于（也不得不）大刀阔斧地去除“异常结果”。",
     "relation": "supports"
    },
    {
     "key": "E024",
     "paragraph_id": "P025",
     "quote": "一个跃迁，何止可以杀死一只猫，还可以毁灭一整个迷信的文明。",
     "relation": "supports"
    },
    {
     "key": "E025",
     "paragraph_id": "P026",
     "quote": "已经意味着仅仅依赖科学将完全不可能对世界作出确切可靠的预测了",
     "relation": "supports"
    },
    {
     "key": "E026",
     "paragraph_id": "P027",
     "quote": "科学越发达，智慧生命对微观扰动会越敏感，对宏观世界的能动性越强",
     "relation": "supports"
    },
    {
     "key": "E027",
     "paragraph_id": "P027",
     "quote": "科学的发展本身就在使得对世界的预测更加困难。",
     "relation": "supports"
    },
    {
     "key": "E028",
     "paragraph_id": "P027",
     "quote": "答案是后者必胜。",
     "relation": "supports"
    },
    {
     "key": "E029",
     "paragraph_id": "P028",
     "quote": "依靠科学解决人类的一切问题这种指望，在原则上就不可追求。",
     "relation": "supports"
    },
    {
     "key": "E030",
     "paragraph_id": "P029",
     "quote": "死了这条心。",
     "relation": "supports"
    },
    {
     "key": "E031",
     "paragraph_id": "P030",
     "quote": "为什么人对这种粗陋程度的观测结果的绝对信心不是迷信？",
     "relation": "supports"
    },
    {
     "key": "E032",
     "paragraph_id": "P031",
     "quote": "请问科学教的本质区别又在哪里？",
     "relation": "supports"
    },
    {
     "key": "E033",
     "paragraph_id": "P032",
     "quote": "所有的主流宗教，都会随时召开大公会议修订教义和信条。",
     "relation": "supports"
    },
    {
     "key": "E034",
     "paragraph_id": "P032",
     "quote": "这跟你们从不质疑科学的方法、立论的根基又有何本质的分别？",
     "relation": "supports"
    },
    {
     "key": "E035",
     "paragraph_id": "P033",
     "quote": "先去掉你眼中的梁木，再去拔ta人眼里的刺。",
     "relation": "supports"
    },
    {
     "key": "E036",
     "paragraph_id": "P035",
     "quote": "科学答集",
     "relation": "context"
    },
    {
     "key": "E037",
     "paragraph_id": "P037",
     "quote": "认为只要存在一种科学论断谈及不确定性和概率，就说明“科学并不绝对强调可重复性”",
     "relation": "supports"
    },
    {
     "key": "E038",
     "paragraph_id": "P038",
     "quote": "因为在谈论“确定的不确定”时，科学的论述不是在谈这个论述的不确定的一面，而是在谈其确定的一面。",
     "relation": "supports"
    },
    {
     "key": "E039",
     "paragraph_id": "P039",
     "quote": "“重量均匀的硬币抛出后正面朝上的几率为50%”，这是不是科学论断？",
     "relation": "supports"
    },
    {
     "key": "E040",
     "paragraph_id": "P041",
     "quote": "你造上一万个符合条件的硬币，每个扔上一万次，看看是否证实这结论。这才是其科学论述的核心。",
     "relation": "supports"
    },
    {
     "key": "E041",
     "paragraph_id": "P042",
     "quote": "你要鉴定这论述的真伪的前提，是去制造这一万个硬币，而不是拿一个硬币丢两次。",
     "relation": "supports"
    },
    {
     "key": "E042",
     "paragraph_id": "P044",
     "quote": "“粒子的位置和动量不可以同时确定”，这个“不可被确定”，本身是不是确定的？",
     "relation": "supports"
    },
    {
     "key": "E043",
     "paragraph_id": "P045",
     "quote": "什么叫【确定的不确定仍是一种确定】",
     "relation": "supports"
    },
    {
     "key": "E044",
     "paragraph_id": "P048",
     "quote": "尝试通过“在xx前提下xx关系成立，在另一个前提下，xx关系不成立”的现象，说明“规律不具备时空无关性”。",
     "relation": "supports"
    },
    {
     "key": "E045",
     "paragraph_id": "P050",
     "quote": "你明明证明的是“不同的前提有不同的结果”。",
     "relation": "supports"
    },
    {
     "key": "E046",
     "paragraph_id": "P051",
     "quote": "“能量守恒在宇宙尺度上不成立”现在有效，明天无效。",
     "relation": "supports"
    },
    {
     "key": "E047",
     "paragraph_id": "P052",
     "quote": "仅仅是换了一个时间和参考系就无效了，你的反驳才能成立",
     "relation": "supports"
    },
    {
     "key": "E048",
     "paragraph_id": "P054",
     "quote": "就是犯了一种无可辩护的逻辑套用错误",
     "relation": "supports"
    },
    {
     "key": "E049",
     "paragraph_id": "P053",
     "quote": "先把你的论述补全，不要采用高中式的无前提表述",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "科学哲学",
    "认识论",
    "科学方法论",
    "宗教与科学关系",
    "物理学基础问题"
   ],
   "issue_candidates": [
    "科学是否为信仰",
    "归纳问题",
    "规律的时空普适性",
    "控制变量实验的可靠性",
    "科学预测的界限",
    "科学教与宗教的类比"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "驳论（预先反驳）",
    "训诫"
   ],
   "object_candidates": [
    "科学",
    "科学教/科学教徒",
    "主流宗教",
    "大公会议",
    "量子效应",
    "硬币",
    "抗日神剧中的日本兵",
    "地球"
   ],
   "working_keywords": [
    "两个基本信仰",
    "绝对一致的前提",
    "时空无关性",
    "宇宙大普查",
    "同一前提",
    "确定的不确定",
    "无效辩驳",
    "逻辑套用错误",
    "科学答集（平台标签）"
   ]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P054 共 54 段全部读完，status=read、full_text_checked=true。P035“科学答集”为知乎平台话题标签混入正文，且在文本与 lexical 之间存在 divergence（lexical 未覆盖片段），已登记进 unresolved_questions。brief 字段为正文开头的截断，与正文重合，不作为独立证据。Q001 属提问者，作者论证的是科学根基的无证据性，与提问题面不完全等同，二者已区分。平台为知乎。"
 },
 "44015a13": {
  "analysis": {
   "question_context": "提问者（Q001）问：中国传统剑术或者自创剑术爱好者如果去打剑道、击剑比赛，结果会如何？作者没有按此问题作答，而是先给出“剑道比赛和剑道是两码事”的判断，再以剑道士以真剑之心练竹剑、不占竹剑便宜立论，进而转向“竹剑师傅”与“兵击爱好者”两类人：竹剑师傅打不赢兵击爱好者，但兵击爱好者的高胜率在真战场上没有意义，会武术反而伤亡率高。提问属提问者；作者的回答改写并替换了提问的比较对象。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "开篇定性：剑道比赛和剑道是两码事。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002",
      "P003"
     ],
     "summary": "无论战国时代还是德川幕府时代，剑道士握竹剑时心里想的、手上用的、身上受的都是真剑，不占竹剑长、不必在意刃筋、不出血这三种便宜。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "反证：占了这个便宜，上战场靠错误直觉去闪躲、格架、进步犹如送死，竹剑百战百胜没有用。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P005",
      "P006"
     ],
     "summary": "提出“竹剑师傅”这一说法：不畏竹如剑、丧失敬畏心与生死观，竹剑便不是辅助物而成了对象本身，那会练成竹剑师傅。",
     "role": "definition"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "推论一：竹剑师傅打不赢兵击爱好者，因为他自己只是一个缚手缚脚的兵击爱好者，对规则的反应已融入本能，反而扣分。",
     "role": "claim"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P008"
     ],
     "summary": "转折与限定：兵击爱好者也不必自豪，这种高胜率没有意义，其“武力值”在真的战场上只会导致更严重的失败率。",
     "role": "qualification"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P009",
      "P010"
     ],
     "summary": "原因：他们对“生死之争”没有心理准备却对作战太有期望，且没见过真正的亡命之搏。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P011",
      "P012"
     ],
     "summary": "条件推演：若当了新警察单独与被逼住的毒贩子放对会非常危险；若自信有兵击经验，把一个普通人逼到起了真正一决生死的心，很容易输给杀心。",
     "role": "reason"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P013"
     ],
     "summary": "以“那位龙哥”之死为例，并称其对兵击的理解恐怕胜过一般兵击爱好者；又称很多职业吃武术饭的都是吃过这种亏才幸存成为老江湖。",
     "role": "example"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P014"
     ],
     "summary": "结论式断语：会武术，反而伤亡率很高——武技很难抵消轻敌。",
     "role": "conclusion"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P015"
     ],
     "summary": "末行出现平台话题标签“科学答集”（lexical 未覆盖片段，属结构杂质）。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张剑道比赛和剑道是两码事。",
     "evidence": [
      "E001"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称无论战国时代还是德川幕府时代，剑道士手里握着竹剑时心里想的、手上用的、身上受的都是真剑，不会占竹剑的便宜（不占长的便宜、不必在意刃筋的便宜、不出血的便宜）。",
     "evidence": [
      "E002",
      "E003",
      "E004"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者认为他们是在练真剑；要是占了这些便宜，上了战场靠着错误的直觉去闪躲、格架、进步犹如送死，竹剑百战百胜没有用。",
     "evidence": [
      "E005",
      "E006"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为不畏竹如剑、丧失敬畏心与生死观，竹剑就不再是对象的辅助物而成了对象本身，那会练成“竹剑师傅”。",
     "evidence": [
      "E007",
      "E008"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言竹剑师傅打不赢兵击爱好者，因为竹剑师傅自己只是一个缚手缚脚的兵击爱好者，对规则的反应已经融入本能，反而是扣分的。",
     "evidence": [
      "E009",
      "E010"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者同时限定：兵击爱好者也不必自豪，这种高胜率没有意义，他们的“武力值”在真的战场上只会导致更严重的失败率。",
     "evidence": [
      "E011",
      "E012"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出的原因是：他们对什么叫“生死之争”没有心理准备，却对作战太有期望；他们没见过什么叫做真正的亡命之搏。",
     "evidence": [
      "E013",
      "E014"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者提出条件性判断：如果当了新警察、单独与被逼住的毒贩子放对，会非常危险；如果自信有兵击经验、把一个普通人逼到起了真正一决生死的心，很容易输给杀心。",
     "evidence": [
      "E015",
      "E016"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以“那位龙哥”就死在这一点上为例，并称完全不带调侃地说，他对兵击的理解恐怕胜过一般的兵击爱好者；又称很多职业吃武术饭的都是吃过这种亏、幸亏没死才得以幸存成为老江湖。",
     "evidence": [
      "E017",
      "E018",
      "E019"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出结论：会武术，反而伤亡率很高——武技很难抵消轻敌。",
     "evidence": [
      "E020"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "open_question",
     "attribution": "questioner",
     "modality": "questioned",
     "statement": "提问者问中国传统剑术或自创剑术爱好者去打剑道、击剑比赛结果会如何；作者未按此作答，而是区分“剑道比赛”与“剑道”并转向竹剑师傅与兵击爱好者的话题。",
     "evidence": []
    }
   ],
   "argument_steps": [
    "开篇定性：剑道比赛和剑道是两码事（P001）。",
    "说明剑道士练竹剑时以真剑为准，不占竹剑长、刃筋、不出血三种便宜（P002-P003）。",
    "反证：占便宜者上战场靠错误直觉犹如送死，竹剑百战百胜无用（P004）。",
    "指出丧失敬畏心与生死观会使竹剑由辅助物变成对象本身，练成“竹剑师傅”（P005-P006）。",
    "推论一：竹剑师傅打不赢兵击爱好者，因对规则的反应已成本能而扣分（P007）。",
    "转折限定：兵击爱好者也不必自豪，高胜率无意义，真战场上失败率更严重（P008）。",
    "解释原因：对生死之争无心理准备、对作战太有期望、没见过亡命之搏（P009-P010）。",
    "条件推演：新警察对被逼住的毒贩、把普通人逼到决死之心（P011-P012）。",
    "以“龙哥”与职业武术人为例（P013）。",
    "结论：会武术反而伤亡率高，武技难抵消轻敌（P014）；末行为平台话题标签（P015）。"
   ],
   "concept_usage": [
    {
     "term": "竹剑师傅",
     "meaning": "作者特指在竹剑比赛规则下练成、把竹剑当作对象本身而非真剑辅助物的人；作者认为其打不赢兵击爱好者。",
     "evidence": "P005、P006、P007",
     "ambiguity": "该称呼带贬义，本文未说明是否指某个具体流派或群体。"
    },
    {
     "term": "兵击爱好者",
     "meaning": "本篇中作为竹剑师傅的对照群体，作者称其高胜率没有意义，在真的战场上失败率更严重。",
     "evidence": "P007、P008",
     "ambiguity": "本文未界定“兵击”的具体所指、规则或组织。"
    },
    {
     "term": "刃筋",
     "meaning": "作者列为竹剑不必在意的项目之一（真剑需要在意），本文未展开定义。",
     "evidence": "P003",
     "ambiguity": "该术语的专门含义本文未说明。"
    },
    {
     "term": "敬畏心/生死观",
     "meaning": "作者认为练真剑必须具备的心理前提：不畏竹如剑、保有对生死的敬畏，否则竹剑会由辅助物变成对象本身。",
     "evidence": "P005",
     "ambiguity": "属作者的规范性说法，本文未给出判定标准。"
    },
    {
     "term": "武力值",
     "meaning": "作者加引号使用，指兵击爱好者自我评估的战斗力；作者称其在真的战场上只会导致更严重的失败率。",
     "evidence": "P008",
     "ambiguity": "引号表示作者对该说法的保留态度，本文未给出定义。"
    },
    {
     "term": "杀心",
     "meaning": "作者用来指普通人被逼到真正一决生死时产生的心理状态，作者认为有兵击经验者容易输给这种状态。",
     "evidence": "P012",
     "ambiguity": "本文未说明其与“亡命之搏”的关系。"
    }
   ],
   "examples_and_targets": [
    "战国时代、德川幕府时代的剑道士（P002）：作者的历史叙述，用来对比剑道比赛与剑道，本文未给出处，待外部核查。",
    "竹剑与真剑（P002-P004）：作者的论证与比喻材料（不占长的便宜、不必在意刃筋、不出血）。",
    "兵击爱好者（P007、P008）：作者的限定与反驳对象（针对其自豪感），并非引用其原话。",
    "新警察与单独被逼住的毒贩子（P011）：作者假设的情境。",
    "“那位龙哥”（P013）：作者引用的案例，具体所指（何人、何时、何事件）本文未说明，需外部核查；作者称其对兵击的理解胜过一般兵击爱好者。",
    "职业吃武术饭的、吃过这种亏幸亏没死才幸存的老江湖（P013）：作者举例。",
    "科学答集（P015）：知乎平台话题标签混入正文（lexical 未覆盖片段），非作者论述。",
    "反驳/改述对象：提问者关于“中国传统剑术或自创剑术爱好者打剑道、击剑比赛”的问题框架（Q001）。"
   ],
   "conditions": [
    "“无论是战国时代还是德川幕府时代”（P002）：作者设定的历史范围。",
    "“要是占这个便宜，上了战场，靠着这个错误的直觉去闪躲、格架、进步，犹如送死”（P004）：条件句。",
    "“在真的战场上”（P008）：场景限定。",
    "“你们要是当了新警察，单独与被逼住的毒贩子放对”（P011）：假设条件。",
    "“如果自信有兵击的经验，把一个普通人逼到起了真正的一决生死的心”（P012）：假设条件。",
    "“完全不带调侃的说”（P013）：作者对该句陈述语气的自我限定。",
    "“恐怕胜过一般的兵击爱好者”（P013）：作者用“恐怕”表示推测。"
   ],
   "rhetoric_and_tone": "短评式答疑，篇幅很短（正文 557 字）。以第二人称“你们”直接对兵击爱好者说话，语气训诫、讥刺而带调侃（“兵击爱好者也不必自豪”“完全不带调侃的说”）。使用排比（“不占竹剑长的便宜，不占竹剑不必在意刃筋的便宜，不占竹剑不出血的便宜”）与反问（“竹剑百战百胜有什么用？”）。以“剑道比赛和剑道是两码事”开篇定性，以“会武术，反而伤亡率很高”作结，中间用假设情境与现实案例支撑。末行是平台话题标签。",
   "unresolved_questions": [
    "P015 “科学答集”是知乎平台话题标签混入正文（lexical 未覆盖片段），非作者论述，重建时需剔除或标注。",
    "P013 “那位龙哥”具体指谁、发生在何时何地何事，本文未说明，需外部核查。",
    "提问者问的是“中国传统剑术或者自创剑术爱好者”去打剑道、击剑比赛的结果，作者未直接回答该问，而以“剑道比赛和剑道是两码事”改写并转向竹剑师傅与兵击爱好者，两者关系本文未说明。",
    "“兵击”的具体所指与规则、“刃筋”的具体含义，本文均未界定。",
    "P002 关于战国时代与德川幕府时代剑道士均以真剑之心练竹剑的历史叙述，本文未给出处，待外部核查。",
    "P014 “会武术，反而伤亡率很高”与 P013 “很多职业吃武术饭的……都是吃过这种亏”均未给出统计或案例来源。",
    "P007 “竹剑师傅打不赢兵击爱好者”是断言，本文未给出比赛、事例或依据。",
    "作者称“不占竹剑长的便宜”，但未说明竹剑与真剑在长度上的具体差异。"
   ],
   "evidence": [
    {
     "key": "E001",
     "paragraph_id": "P001",
     "quote": "剑道比赛和剑道是两码事。",
     "relation": "supports"
    },
    {
     "key": "E002",
     "paragraph_id": "P002",
     "quote": "剑道士手里握着竹剑，心里想的、手上用的、身上受的都是真剑",
     "relation": "supports"
    },
    {
     "key": "E003",
     "paragraph_id": "P002",
     "quote": "他不会占竹剑的便宜。",
     "relation": "supports"
    },
    {
     "key": "E004",
     "paragraph_id": "P003",
     "quote": "不占竹剑长的便宜，不占竹剑不必在意刃筋的便宜，不占竹剑不出血的便宜。",
     "relation": "supports"
    },
    {
     "key": "E005",
     "paragraph_id": "P004",
     "quote": "靠着这个错误的直觉去闪躲、格架、进步，犹如送死",
     "relation": "supports"
    },
    {
     "key": "E006",
     "paragraph_id": "P004",
     "quote": "竹剑百战百胜有什么用？",
     "relation": "supports"
    },
    {
     "key": "E007",
     "paragraph_id": "P005",
     "quote": "不畏竹如剑，丧失了这个敬畏心，失去了生死观，竹剑就不是对象的辅助物，而成了对象本身了。",
     "relation": "supports"
    },
    {
     "key": "E008",
     "paragraph_id": "P006",
     "quote": "那会练成竹剑师傅。",
     "relation": "supports"
    },
    {
     "key": "E009",
     "paragraph_id": "P007",
     "quote": "竹剑师傅打不赢兵击爱好者",
     "relation": "supports"
    },
    {
     "key": "E010",
     "paragraph_id": "P007",
     "quote": "对规则的反应已经融入本能，反而是扣分的",
     "relation": "supports"
    },
    {
     "key": "E011",
     "paragraph_id": "P008",
     "quote": "这种高胜率没有意义",
     "relation": "supports"
    },
    {
     "key": "E012",
     "paragraph_id": "P008",
     "quote": "你们的“武力值”在真的战场上只会导致更严重的失败率",
     "relation": "supports"
    },
    {
     "key": "E013",
     "paragraph_id": "P009",
     "quote": "因为你们对什么叫“生死之争”没有心理准备，却对作战太有期望。",
     "relation": "supports"
    },
    {
     "key": "E014",
     "paragraph_id": "P010",
     "quote": "你们没见过什么叫做真正的亡命之搏。",
     "relation": "supports"
    },
    {
     "key": "E015",
     "paragraph_id": "P011",
     "quote": "你们要是当了新警察，单独与被逼住的毒贩子放对，会非常危险。",
     "relation": "supports"
    },
    {
     "key": "E016",
     "paragraph_id": "P012",
     "quote": "把一个普通人逼到起了真正的一决生死的心，你们很容易输给杀心",
     "relation": "supports"
    },
    {
     "key": "E017",
     "paragraph_id": "P013",
     "quote": "那位龙哥就死在这一点上。",
     "relation": "supports"
    },
    {
     "key": "E018",
     "paragraph_id": "P013",
     "quote": "他对兵击的理解，恐怕胜过一般的兵击爱好者",
     "relation": "supports"
    },
    {
     "key": "E019",
     "paragraph_id": "P013",
     "quote": "很多职业吃武术饭的，都是吃过这种亏幸亏没死才得以幸存成为老江湖的",
     "relation": "supports"
    },
    {
     "key": "E020",
     "paragraph_id": "P014",
     "quote": "会武术，反而伤亡率很高——你的武技很难抵消你的轻敌。",
     "relation": "supports"
    },
    {
     "key": "E021",
     "paragraph_id": "P015",
     "quote": "科学答集",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "武术",
    "剑道",
    "兵击",
    "实战与竞技之别",
    "暴力冲突与生死心理"
   ],
   "issue_candidates": [
    "比赛规则与实战的差异",
    "竹剑训练是否养成错误直觉",
    "兵击爱好者的高胜率是否有意义",
    "轻敌与伤亡率",
    "生死之争的心理准备"
   ],
   "text_function_candidates": [
    "答疑",
    "评论",
    "训诫",
    "经验总结"
   ],
   "object_candidates": [
    "剑道士",
    "竹剑师傅",
    "兵击爱好者",
    "战国时代",
    "德川幕府时代",
    "新警察",
    "毒贩子",
    "龙哥",
    "科学答集（平台标签）"
   ],
   "working_keywords": [
    "剑道比赛",
    "真剑",
    "竹剑",
    "敬畏心",
    "生死观",
    "杀人剑",
    "兵击",
    "武力值",
    "杀心",
    "轻敌"
   ]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 P001-P015 共 15 段全部读完（正文 557 字，属短评），status=read、full_text_checked=true。P015“科学答集”为知乎平台话题标签混入正文，且在文本与 lexical 之间存在 divergence（lexical 未覆盖片段），已登记进 unresolved_questions。brief 字段为正文开头的截断，与正文重合，不作为独立证据。Q001 属提问者；作者未按提问的比较对象作答，而是改写问题，二者已区分。P013“龙哥”具体所指本文未说明，需外部核查。平台为知乎。"
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
