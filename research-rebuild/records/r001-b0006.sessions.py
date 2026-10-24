# -*- coding: utf-8 -*-
"""批次 r001-b0006 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0006.sessions.py            # 写 out/r001-b0006.out.jsonl
  python3 records/r001-b0006.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0006"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0006.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
    "793fedad": {
        "analysis": {
            "question_context": "提问者问“军衔是怎么一回事？”（Q001）。作者重述为“军队为什么要有阶级和阶级标志”，以“军衔是私兵向官兵发展的结果”为主线，从私兵与军衔制的冲突、中国古代军衔制实践与两重阻力、帝国循环、近现代中国军衔与西欧的关系、欧洲军衔制的雇佣军背景、军衔制核心在士兵及其军事意义展开；文末以分隔线标明后半为驳斥“现代军衔制起源于西欧军衔制”的“老答案”，并附平台话题标签。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "重述问题为“军队为什么要有阶级和阶级标志”，否定简单化的“层级指挥系统”解释，提出主线：军衔是私兵向官兵发展的结果。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P003"
                    ],
                    "summary": "私兵无军衔概念且反对强加的军衔制；古代武将以亲信充任“公职”私人控制军队，使法律意义上的军衔制被架空。",
                    "role": "reason"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P004"
                    ],
                    "summary": "制度意义上的军衔制中国至少在战国已出现；秦国耕战一体要求官兵分离；南宋为防藩镇强行轮换；近代以前军队国家化有两重阻力。",
                    "role": "reason"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P005"
                    ],
                    "summary": "第一重阻力：古代军队独立生存能力强，谋反不难维持甚至提高战斗力，国家只能依赖“兵将隔绝”与文官领军。",
                    "role": "reason"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P006"
                    ],
                    "summary": "第二重阻力：无标准化部队则调任与磨合成本相矛盾，强推军衔制与国家化必致战斗力下滑。",
                    "role": "reason"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P007"
                    ],
                    "summary": "古代帝国的循环：强盛时搞国家化、军衔制，随后军力下滑，或亡于军事失败或亡于藩镇私兵。",
                    "role": "conclusion"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P008"
                    ],
                    "summary": "失败不能否定中国曾推行过与欧洲军衔制本质相当的制度；以“哪个朝代没有军衔制”反问。",
                    "role": "claim"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P009"
                    ],
                    "summary": "“近现代中国军衔源自西欧”并非不言而喻：未全盘西化、无照搬的物质与制度基础，上校不等同 Colonel，且中国不可能切断传统另起源头。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P010"
                    ],
                    "summary": "欧洲军衔制用词相同源于雇佣军成分；但西欧军衔制发明权不可能属中世纪雇佣军，可认“直接继承”而不可谈“起源”。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P011"
                    ],
                    "summary": "军衔制核心不在军官而在士兵；改革关键是造就服从军衔制的士兵与相应制度。",
                    "role": "claim"
                },
                {
                    "unit_id": "U012",
                    "paragraph_refs": [
                        "P012"
                    ],
                    "summary": "驳“军衔制在军事上没意义”：无军衔制则指挥链脆弱，敌方可用说客、刺客、内应取胜；精锐部队的关键在全体下级对全体上级的服从。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U013",
                    "paragraph_refs": [
                        "P013"
                    ],
                    "summary": "以一句收束上半篇。",
                    "role": "conclusion"
                },
                {
                    "unit_id": "U014",
                    "paragraph_refs": [
                        "P014"
                    ],
                    "summary": "以分隔线标明以下为“老答案”，作者自评新版更好。",
                    "role": "transition"
                },
                {
                    "unit_id": "U015",
                    "paragraph_refs": [
                        "P015"
                    ],
                    "summary": "老答案：军衔阶级以国家军制为前提；论起源去封建领主身上找是找错方向；西欧军衔制是对帝国军制的复兴。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U016",
                    "paragraph_refs": [
                        "P016"
                    ],
                    "summary": "老答案：“军衔”译名被“荣衔”“加衔”污染而失真，本质是阶级制，应称“军阶”。",
                    "role": "claim"
                },
                {
                    "unit_id": "U017",
                    "paragraph_refs": [
                        "P017"
                    ],
                    "summary": "老答案：驳“解放军没有军阶照样打仗”，称其逻辑混账。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U018",
                    "paragraph_refs": [
                        "P018"
                    ],
                    "summary": "老答案：中共重视军阶但无条件推行；反对论调本质上是对抗军队国家化、保持主官个人掌握。",
                    "role": "reason"
                },
                {
                    "unit_id": "U019",
                    "paragraph_refs": [
                        "P019"
                    ],
                    "summary": "老答案：从高伤亡与指挥链再组织需求论军衔制是近代战争绝对必需品。",
                    "role": "reason"
                },
                {
                    "unit_id": "U020",
                    "paragraph_refs": [
                        "P020"
                    ],
                    "summary": "老答案：少尉与士官长不是问题，指挥权在少尉，但否决士官长建议致重伤亡需对军事法庭负责。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U021",
                    "paragraph_refs": [
                        "P021"
                    ],
                    "summary": "文末为平台话题标签，未被 lexical 结构覆盖。",
                    "role": "other"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者把问题重述为“军队为什么要有阶级和阶级标志”，称军衔实际上是阶级标志，并认为“层级指挥系统不严肃则易败亡”这种描述并不简单成立，军衔是私兵向官兵发展的结果。",
                    "evidence": [
                        "E1",
                        "E2"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "私兵因团队规模极小、从属关系近乎绝对固定而无军衔概念并反对强加的军衔制；古代武将任用子女、亲信、乡党、门客、熟人充任“公职”以私人控制军队，使法律意义上完善的军衔制被架空。",
                    "evidence": [
                        "E3",
                        "E4"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "单独讨论制度意义上的军衔制，中国至少在战国时代已开始出现；秦国耕战一体的动员制度要求实现官兵与部队的分离。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "大一统国家凡有官军制度、由国家支付军费的部队，其君主都想保住绝对控制权，无一例外尝试贯彻军衔制；南宋为防藩镇剥夺军人指挥权、强行轮换，被责“兵不知将，将不知兵”。",
                    "evidence": [
                        "E6",
                        "E7"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "古代军队独立生存能力极强，唯一绝对必要的物资只有粮食；除非孤军戍守荒无人烟的边疆，否则谋反不难维持战斗力，甚至可能因谋反而得到更多物资。",
                    "evidence": [
                        "E8",
                        "E9"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "国家无法靠掉断后勤大幅降低叛军战斗力，也无法保证官军拥有压倒性优势，故在控制军队上不得不依赖“兵将隔绝”的轮换制与文官领军；否则稍有松懈即成藩镇，军衔体制立刻被架空。",
                    "evidence": [
                        "E10",
                        "E11"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "无标准化部队时指挥官必须与部队熟悉磨合，磨合成本与频繁调任的防范手段直接矛盾；在管理理论与实践双不足时强推军衔制与国家化一定会使实际战斗力急剧下滑。",
                    "evidence": [
                        "E12",
                        "E13"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "古代帝国形成奇特循环：国力强盛时搞国家化、军衔制，然后军事实力急剧下滑并爆发危机，或亡于军事失败，或因松动而亡于藩镇私兵集团。",
                    "evidence": [
                        "E14"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "失败不能否定中国曾扎扎实实推行过与“现代欧洲军衔制”相比毫不逊色、本质相当的军衔制度。",
                    "evidence": [
                        "E15"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "中国军队从未全盘西化，直到解放战争打完也无照搬西方军制的物质与制度基础；中国的“上校”从未真正等同西方的 Colonel，以西方为师而非为父，且这个师始终没拜上。",
                    "evidence": [
                        "E16",
                        "E17"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "在中国，除非这事之前没有，否则根本不可能出现“某种现状的源头在西方”这种现象，这不是民族自豪感爆棚或政治性学术，而是不得不接受的事实。",
                    "evidence": [
                        "E18"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "欧洲军衔制各国沿用几乎相同的词汇，源于军事力量里深入骨髓的雇佣军成分；雇佣军最早领悟“军衔重于职务”的要害。",
                    "evidence": [
                        "E19",
                        "E20"
                    ]
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "有埃及、巴比伦、波斯、希腊、罗马甚至阿拉伯在前，西欧军衔制的发明权不可能轮到中世纪雇佣军；可说“直接继承西欧近代军事制度”，但谈“起源”则欠缺学术严谨。",
                    "evidence": [
                        "E21",
                        "E22"
                    ]
                },
                {
                    "claim_id": "C014",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "军衔制的核心不在军官而在士兵；改革关键是把旧武士改成服从军衔制的士兵，工作量绝大多数在造就这样的士兵与制度上。",
                    "evidence": [
                        "E23",
                        "E24"
                    ]
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "无军衔制改造则部队存在“军官阵亡即溃逃”的本质脆弱性，敌人会转用说客、刺客、内应取胜；精锐部队“满万不可敌”的关键在于对方需杀伤百分之几十而己方只需百分之几；“哀兵必胜”“兵在精不在多”的秘密即有效实现了军衔机制的部队。",
                    "evidence": [
                        "E25",
                        "E26",
                        "E27",
                        "E28",
                        "E29",
                        "E30"
                    ]
                },
                {
                    "claim_id": "C016",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "老答案：军衔阶级一开始就在国家军制下才有意义，论起源去欧洲封建领主身上找是找错了方向，罗马共和国时期的军职更接近现代军衔制；西欧军衔制本身是对帝国军制的复兴。",
                    "evidence": [
                        "E31",
                        "E32",
                        "E33"
                    ]
                },
                {
                    "claim_id": "C017",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "老答案：“军衔”这个命名是隐形障碍，“衔”被“荣衔”“加衔”污染并虚化；现代军衔制本质是裸裸的阶级制，应译为“军阶”；并驳“解放军没有军阶照样打好仗”，称没有 xx 也没灭亡不是 xx 不必要的合理依据。",
                    "evidence": [
                        "E34",
                        "E35",
                        "E36",
                        "E37"
                    ]
                },
                {
                    "claim_id": "C018",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "老答案：中共一直高度重视军阶，只是一直没有条件推行；国内出现反对和贬低军衔制的论调，本质上是有人想对抗军队国家化、保持长期军事主官对军队掌握的个人特殊优势。",
                    "evidence": [
                        "E38",
                        "E39",
                        "E40"
                    ]
                },
                {
                    "claim_id": "C019",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "没有彻底军衔化，一到战时调动部队就不得不顾虑主官的个人心态，真拿掉主官会让战斗力下降几成，这种隐患现代国家绝不可能容忍。",
                    "evidence": [
                        "E41"
                    ]
                },
                {
                    "claim_id": "C020",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "从效率视角看军衔制是近代战争的绝对必需品，因新战争技术大大提高伤亡率，部队必须能不断自行重组指挥链；自卫反击战并非典型现代化战争，下一次大战会更像海湾战争和苏联卫国战争。",
                    "evidence": [
                        "E42",
                        "E43",
                        "E44",
                        "E45"
                    ]
                },
                {
                    "claim_id": "C021",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "“年轻的少尉和资深的士官长”不是问题：指挥权在少尉无疑，但少尉应高度依赖士官长，否则否决建议而致重大伤亡需对军事法庭解释。",
                    "evidence": [
                        "E46",
                        "E47"
                    ]
                }
            ],
            "argument_steps": [
                "把提问重述为“军队为什么要有阶级和阶级标志”，否定简单化的“层级指挥系统”解释（P001、P002）。",
                "由私兵的规模与从属关系推出其无军衔概念、反对军衔制，并给出中国古代武将私人控制军队架空军衔制的例证（P003）。",
                "上溯战国秦国的耕战一体与军官—部队分离，说明军衔制的制度出现之早；再由大一统君主的控制欲推到南宋轮换制与“兵不知将，将不知兵”（P004）。",
                "提出近代以前“军队国家化”的两重阻力，并展开第一重：古代军队的后勤自给与谋反可行性（P005）。",
                "展开第二重阻力：部队无标准化、职业化则调任与磨合成本相矛盾，强行推行必致战斗力下滑（P006）。",
                "归纳为古代帝国的循环（P007）。",
                "转出正面判断：中国历代皆有军衔制，且与欧洲军衔制本质相当（P008）。",
                "讨论近现代中国军衔与西欧的关系，指出“源自西欧”并非不言而喻（P009）。",
                "讨论欧洲军衔制的雇佣军背景，区分“直接继承”与“起源”（P010）。",
                "纠正“军衔制核心在军官”的误区，指出核心在士兵（P011）。",
                "论证军衔制的军事意义：指挥链的自我重组能力、精锐部队的战斗力来源（P012）。",
                "上半篇收束（P013）。",
                "以分隔线标明以下为驳斥“起源于西欧”的老答案（P014）。",
                "老答案重申军衔阶级的国家军制前提，并把“西欧军衔制”的起源定位为对帝国军制的复兴（P015）。",
                "老答案指出“军衔”译名的污染，主张应称“军阶”（P016）。",
                "老答案反驳“解放军没有军阶照样打仗”（P017）。",
                "老答案说明中共并非不重视军阶而是无条件推行，并指认反对论调与军队国家化的对抗（P018）。",
                "老答案从近代战争的高伤亡与指挥链再组织需求论证军衔制必要（P019）。",
                "老答案回应少尉与士官长的关系（P020）。",
                "文末附平台话题标签（P021）。"
            ],
            "concept_usage": [
                {
                    "term": "军衔",
                    "meaning": "作者界定为阶级标志，并称现代军衔制本质上是赤裸裸的阶级制；军官的“官位”是军衔而不只是“职务”。",
                    "evidence": "P001、P012、P016",
                    "ambiguity": "作者同时主张应改译为“军阶”，术语在文中并用；对“军衔”与“职务”的边界只在 P012 举例说明。"
                },
                {
                    "term": "私兵",
                    "meaning": "作者指团队规模极小、从属关系近乎绝对固定、事实上没有军衔概念并反对军衔制的武装。",
                    "evidence": "P002、P003",
                    "ambiguity": "“规模极小”未给出量化标准。"
                },
                {
                    "term": "军队国家化",
                    "meaning": "作者指国家掌握军队、使指挥关系可依国家需要更换而对组织心态无碍的状态，是实行军衔制的前提与结果。",
                    "evidence": "P004、P005、P018",
                    "ambiguity": "作者未给出制度层面的完整定义。"
                },
                {
                    "term": "兵将隔绝 / 兵不知将，将不知兵",
                    "meaning": "作者指古代国家为防止藩镇而推行的轮换制度，使兵与将互不隶属、可依调令更换。",
                    "evidence": "P004、P005",
                    "ambiguity": "作者同时指出该制度与战斗力的矛盾，但未说明限度。"
                },
                {
                    "term": "藩镇",
                    "meaning": "作者指军衔体制被架空、指挥官不可更换的私兵化军事集团，其形成即意味着军衔制失效。",
                    "evidence": "P005、P007",
                    "ambiguity": "未给出判定“藩镇已成”的标准。"
                },
                {
                    "term": "军衔重于职务",
                    "meaning": "作者称这是雇佣军最早领悟的要害：身分等级高于具体职位。",
                    "evidence": "P010",
                    "ambiguity": "作者未展开该原则的具体制度含义。"
                },
                {
                    "term": "rank / 军阶",
                    "meaning": "作者认为“军衔”的译法扭曲了 rank 的原义，主张还原为“军阶/Rank”来理解其阶级制本质。",
                    "evidence": "P016",
                    "ambiguity": "作者称“后文会说明，这种安排也许是故意的”，但阅读包中所见正文未见对应的后文说明。"
                },
                {
                    "term": "银子弹",
                    "meaning": "作者用以比喻只需终结少数头领即可使未军衔化部队崩溃的打击方式。",
                    "evidence": "P012",
                    "ambiguity": "属比喻用法。"
                },
                {
                    "term": "满万不可敌",
                    "meaning": "作者引用的说法，用以说明精锐部队以杀伤少数头领制胜的秘密。",
                    "evidence": "P012",
                    "ambiguity": "作者未注明该说法的出处与所指具体部队。"
                }
            ],
            "examples_and_targets": [
                "中国古代武将任用子女、亲信、乡党、门客、熟人充任部队“公职”（作者例证，P003）。",
                "秦国军事改革与“入则为民、出则为兵”的耕战一体动员制度（作者例证，P004）。",
                "南宋为防藩镇剥夺军人指挥权、强行轮换，被指责“兵不知将，将不知兵”（作者例证，P004）。",
                "“以宴会为名赚来直接杀死”的极端更换指挥官手段（作者例证，P005）。",
                "标准军事操典的早期尝试（作者例证，P006）。",
                "杯酒释兵权（作者例证，P007）。",
                "印度军队的全盘西化、操练新军、军事顾问团、模范营、教导团（作者例证与对照，P009）。",
                "参将、游击、千总、把总等旧称呼与 Colonel、Captain 的对比（作者例证，P009）。",
                "洋务运动、五四运动、民族资产阶级革命、GCD 学习苏联的历史教训（作者引为证据，P009）。",
                "The military ranking system is origined from mediaeval mercenaries（作者引述并否定的说法，P010）。",
                "埃及、巴比伦、波斯、希腊、罗马、阿拉伯（作者列举的先例，P010）。",
                "“重新发明马顿定律”（原文如此，作者类比，P010）。",
                "欧洲雇佣兵、玄甲兵、白马队、八旗兵（作者列举的精锐部队例证，P012）。",
                "“哀兵必胜”“兵在精不在多”（作者引用的成语并给出其解释，P012）。",
                "罗马共和国时期的军团长、百夫长（作者称更接近现代军衔制，P015）。",
                "“荣衔”“加衔”（作者批评的对象，P016）。",
                "“解放军没有军阶照样打好仗，只要有职务就行了”（作者反驳的对象，P017）。",
                "原子弹、抗日战争、朝鲜战争（作者用于反问的例证，P017）。",
                "自卫反击战、对越战争、海湾战争、苏联卫国战争（作者用于区分战争形态的例证，P019）。",
                "年轻的少尉与资深的士官长（作者反驳的说法，P020）。"
            ],
            "conditions": [
                "“除非孤军戍守在荒无人烟的边疆”为古代军队谋反可行性的例外条件（P005）。",
                "“在略尽粮食财物之后”为叛军裹挟居民参军的情形条件（P005）。",
                "“在藩镇未成的阶段”为第二重阻力的时间条件（P006）。",
                "“在管理理论和实践双不足的前提下”为强行推行军衔制导致战斗力下滑的前提（P006）。",
                "“如果不是狭隘到只把中尉上校称作军衔的话”为 P008 反问的条件（P008）。",
                "“直到解放战争打完”为中国军队未照搬西方军制的时限（P009）。",
                "“在中国，除非这事之前没有”为中国不可能出现“源头在西方”的条件（P009）。",
                "“即使勉强建立所谓的模范营、教导团”为作者对西式编制落地的让步性限定（P009）。",
                "“勉强建立，也只会是以丧失战斗力为代价”为 P011 的让步条件。",
                "“如果没有切实实现军衔制改造”为 P012 后果推演的条件。",
                "“如果是没有实现军衔制的部队互相作战”为 P012 该段情形的限定。",
                "“无论认识不认识，熟悉不熟悉也能有效维持的服从”为作者对“服从”的限定。",
                "“一旦它受到重击，不能在几十分钟内进行再组织”为 P019 推演的触发条件。",
                "“战后除非大家都死绝”为 P020 责任追究的例外条件。",
                "作者多次使用“几乎”“恐怕”“也许”“大概”等限定词，部分结论以反问形式给出。"
            ],
            "rhetoric_and_tone": "论辩语气强烈、以断言和反问推进：大量使用“混账的”“找错了方向”“欠缺学术该有的基本严谨”“拍脑袋观点”等直斥式措辞；反问句密集（“中国哪个朝代没有军衔制？”“搞原子弹干什么？”“你商量一小时敌军都打到你身后去了”）；善用比喻与类比（“一颗银子弹”“两组头领带着巨量的保镖”“守财奴”“重新发明马顿定律”）；以“以之为师，而非以之为父”“浩然之叹”等对仗式表达强化立场；结构上分为新答与“老答案”两段，作者自评新版本更好，并直接对读者喊话（“恕我直言”“不要拿自卫反击战说事”）。",
            "unresolved_questions": [
                "文末 P021“社科答集/科学答集”为平台话题标签且 lexical 未覆盖该片段，是否属作者正文无法确定。",
                "P016 称“后文会说明，这种安排也许是故意的”，但阅读包中所见正文未见对应的后文说明。",
                "P010 中“马顿定律”应为“牛顿定律”之误（原文如此），是否属笔误未说明。",
                "“满万不可敌”“哀兵必胜”“兵在精不在多”等说法的出处未注明；玄甲兵、白马队的具体所指未展开。",
                "“军衔制”在中国历代的具体制度形态（P008 反问“哪个朝代没有军衔制”）未给出系统例证，属需外部核查的历史断言。",
                "P009、P018、P019 涉及近现代史与军事史的多项断言（如“直到自卫反击战……连统一服装都还没有做到”“wg 期间连军火库都会被哄抢”）未给出来源，属待外部核查。",
                "本篇 updated_at（2022-03-15）晚于 published_at（2018-10-06），正文是否经过修订、修订内容为何，语料未提供版本差异信息。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "军衔实际上是阶级标志。这",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "实际上是私兵向官兵发展的结果。",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "私兵因其团队规模极小、从属关系近乎绝对固定，事实上没有军衔概",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P003",
                    "quote": "的“军衔制”实际上被架空了。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P004",
                    "quote": "义上的“军衔制”的话，中国至少在战国时",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P004",
                    "quote": "，其君主都必然想要保住对军队的绝对控制权，于是无一例外都尝试过贯彻军衔制。",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P004",
                    "quote": "被后代不绝于耳的指责“兵不知将，将不知兵”。",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P005",
                    "quote": "的原始，相对现代有极大的独立生存能力",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P005",
                    "quote": "除非孤军戍守在荒无人烟的边疆，否则军队谋反是不难",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P005",
                    "quote": "国家没有能力通过简单的掐断后勤供应来控制来大幅降低叛军的战斗力，无法保证官军比叛军真的拥",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P005",
                    "quote": "否则稍有松懈，即成藩镇，藩镇一成，则军衔体制将立刻架空",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P006",
                    "quote": "没有标准化的部队，指挥官就不能走马上任立刻发挥战斗力，就必须要与部队熟悉磨合。",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P006",
                    "quote": "是强行推行军衔制和国家化，在管理理论和实践双不足的前提下一定会导致军队的实际战斗力急剧下滑。",
                    "relation": "supports"
                },
                {
                    "key": "E14",
                    "paragraph_id": "P007",
                    "quote": "这就形成了古代帝国的奇特循环",
                    "relation": "supports"
                },
                {
                    "key": "E15",
                    "paragraph_id": "P008",
                    "quote": "我们甚至可以反问一句——中国哪个朝代没有军衔制？",
                    "relation": "supports"
                },
                {
                    "key": "E16",
                    "paragraph_id": "P009",
                    "quote": "中国的“上校”，事实上从未真正等同过西方的Colonel。",
                    "relation": "supports"
                },
                {
                    "key": "E17",
                    "paragraph_id": "P009",
                    "quote": "这是以之为师，而非以之",
                    "relation": "supports"
                },
                {
                    "key": "E18",
                    "paragraph_id": "P009",
                    "quote": "否则根本就不可能出现“某种现状的源头在西方”这种现象",
                    "relation": "supports"
                },
                {
                    "key": "E19",
                    "paragraph_id": "P010",
                    "quote": "这源于欧洲各国的军事力量里有深入骨髓的雇佣军成分。",
                    "relation": "supports"
                },
                {
                    "key": "E20",
                    "paragraph_id": "P010",
                    "quote": "最早的领悟了“军衔重于职务”的要害。",
                    "relation": "supports"
                },
                {
                    "key": "E21",
                    "paragraph_id": "P010",
                    "quote": "有埃及、巴比伦、波斯、希腊、罗马甚至阿拉伯在前，西欧军衔制的发明权怎么可能轮得到中世纪雇佣军？",
                    "relation": "supports"
                },
                {
                    "key": "E22",
                    "paragraph_id": "P010",
                    "quote": "说“现代军衔制直接继承自西欧近代军事制度”，但要说“起源”，那就是欠缺学术该有的基本严谨。",
                    "relation": "supports"
                },
                {
                    "key": "E23",
                    "paragraph_id": "P011",
                    "quote": "军衔制的核心其实并不在于军官，而在于士兵。",
                    "relation": "supports"
                },
                {
                    "key": "E24",
                    "paragraph_id": "P011",
                    "quote": "实施军衔制的工作量绝大多数都是在造就这样的士兵、建立这样的制度上，而不是在给军官定",
                    "relation": "supports"
                },
                {
                    "key": "E25",
                    "paragraph_id": "P012",
                    "quote": "如果没有切实实现军衔制改造，则会有“军官阵",
                    "relation": "supports"
                },
                {
                    "key": "E26",
                    "paragraph_id": "P012",
                    "quote": "那么敌人毫无疑问会转而使用说客、刺客、内应来进行这场“战争”，而且",
                    "relation": "supports"
                },
                {
                    "key": "E27",
                    "paragraph_id": "P012",
                    "quote": "别人打败他们需要杀伤他们百分之几十，杀到无将可替，他们打败别人却只需要杀伤对方百分之几",
                    "relation": "supports"
                },
                {
                    "key": "E28",
                    "paragraph_id": "P012",
                    "quote": "十分之一的部队规模意味着几十分之一的供给压力，意味着“神速”。",
                    "relation": "supports"
                },
                {
                    "key": "E29",
                    "paragraph_id": "P012",
                    "quote": "哀兵、精兵都是有效的实现了军衔机制的部队。",
                    "relation": "supports"
                },
                {
                    "key": "E30",
                    "paragraph_id": "P012",
                    "quote": "精兵精在组织内全体士兵对全体军官的服从，全体下级对全体上级的服从——无论认识不认识，熟悉不熟悉也能",
                    "relation": "supports"
                },
                {
                    "key": "E31",
                    "paragraph_id": "P015",
                    "quote": "军衔阶级一开始就是在国家军制下才有意义的东西。",
                    "relation": "supports"
                },
                {
                    "key": "E32",
                    "paragraph_id": "P015",
                    "quote": "要论述军衔的起源，去欧洲封建领主身上找是完全找错了方向",
                    "relation": "supports"
                },
                {
                    "key": "E33",
                    "paragraph_id": "P015",
                    "quote": "而是封建时代结束、民族国家兴起之后，因封建制武装形式无力承担国防重任，对帝国军制的复兴的结果。",
                    "relation": "supports"
                },
                {
                    "key": "E34",
                    "paragraph_id": "P016",
                    "quote": "这个“衔”字被“荣衔”，“加衔”这种混账做法给污染了",
                    "relation": "supports"
                },
                {
                    "key": "E35",
                    "paragraph_id": "P016",
                    "quote": "阶级制，纯以贴切论，根本不该被翻译为“军衔”，而应该是“军阶”。",
                    "relation": "supports"
                },
                {
                    "key": "E36",
                    "paragraph_id": "P017",
                    "quote": "答案里有自称“解放军没有军阶照样打好仗，只要有职务就行了”。",
                    "relation": "contradicts"
                },
                {
                    "key": "E37",
                    "paragraph_id": "P017",
                    "quote": "没有xx也没灭亡",
                    "relation": "supports"
                },
                {
                    "key": "E38",
                    "paragraph_id": "P018",
                    "quote": "中共事实上一直高度重视军阶，只是一直没有条件去推行。",
                    "relation": "supports"
                },
                {
                    "key": "E39",
                    "paragraph_id": "P018",
                    "quote": "而既然交给给各地自决，不客气的说，一直到自卫反击战，中国有哪一年有过真正的喘息之机去实施严肃的军队正规化？",
                    "relation": "supports"
                },
                {
                    "key": "E40",
                    "paragraph_id": "P018",
                    "quote": "本质上是因为有人想对抗军队国家化，企图保持长期军事主官对军队掌握的个人特殊优势。",
                    "relation": "supports"
                },
                {
                    "key": "E41",
                    "paragraph_id": "P018",
                    "quote": "没有彻底军衔化，一到战时，调动部队担任任务就不得不顾虑主官的个人心态，真的痛下决心",
                    "relation": "supports"
                },
                {
                    "key": "E42",
                    "paragraph_id": "P019",
                    "quote": "军衔制是近代战争的绝对必需品。无他，伤亡太大。",
                    "relation": "supports"
                },
                {
                    "key": "E43",
                    "paragraph_id": "P019",
                    "quote": "一只部队不能不断的自行再次毫无歧义余地的反复组织",
                    "relation": "supports"
                },
                {
                    "key": "E44",
                    "paragraph_id": "P019",
                    "quote": "不要拿自卫反击战说事。那并不是典型意义上的现代化战争。",
                    "relation": "supports"
                },
                {
                    "key": "E45",
                    "paragraph_id": "P019",
                    "quote": "如果有下一次大战，那绝不会更像对越战争和抗战，而一定会更像海湾战争和苏联卫国战争。",
                    "relation": "supports"
                },
                {
                    "key": "E46",
                    "paragraph_id": "P020",
                    "quote": "指挥权在少尉无疑，但是少尉毫无疑问应该高度依赖士官长。",
                    "relation": "supports"
                },
                {
                    "key": "E47",
                    "paragraph_id": "P020",
                    "quote": "战后除非大家都死绝，否则否决士官长建议而导致重大伤亡你是要对军事法庭解释你的合理理由的。",
                    "relation": "supports"
                },
                {
                    "key": "E48",
                    "paragraph_id": "P021",
                    "quote": "社科答集",
                    "relation": "context"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "军事史",
                "军事制度",
                "中国历史",
                "组织理论"
            ],
            "issue_candidates": [
                "军衔制的起源与本质",
                "私兵与军队国家化",
                "藩镇与兵将隔绝",
                "中国古代军衔制",
                "近现代中国军制与西方的关系",
                "军衔译名",
                "指挥链的再组织能力"
            ],
            "text_function_candidates": [
                "答疑",
                "论辩",
                "历史解释",
                "概念辨析"
            ],
            "object_candidates": [
                "军衔",
                "私兵",
                "雇佣军",
                "秦国",
                "南宋",
                "藩镇",
                "西欧",
                "罗马共和国",
                "中共",
                "解放军",
                "英军",
                "苏联",
                "自卫反击战",
                "海湾战争"
            ],
            "working_keywords": [
                "军衔",
                "军阶",
                "rank",
                "私兵",
                "军队国家化",
                "兵不知将，将不知兵",
                "藩镇",
                "雇佣军",
                "满万不可敌",
                "哀兵必胜",
                "社科答集"
            ]
        },
        "notes": "无图片节点。text 与 lexical 有 1 处差异：正文末尾“社科答集/科学答集”（char_start=6057）为 lexical 未覆盖的平台话题标签，已登记。本篇实为“新答 + 分隔线 + 老答案”两段结构，作者自评新版本更好；老答案部分同样按作者正文记录，未作删减。"
    },
    "94815489": {
        "analysis": {
            "question_context": "提问者问“为什么女权指男女平权，男权就指男性特权？”（Q001）。作者把原因归为“太多人对权利结构缺少合理认知”，随后以公域/私域的区分界定平权，主张私域不以“对等”为特征而是“各凭条件做最大的主张”，并据此为女性在私域的主张辩护，指出问题在于“有人不想给”，最后回应“反对女权是否也是个人自由”。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": ["P001"],
                    "summary": "给出原因：太多人对权利结构缺少合理认知。",
                    "role": "claim",
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": ["P002", "P003", "P004"],
                    "summary": "区分两个领域：公域平权指平等地担当公职、平等享有公共资源、平等法律地位，靠追求对等、一致、无差别达成；私权领域的平权不以“对等”为特征，而是“各凭条件做最大的主张”，这里所谓平权指所有人都平等地享有做最大主张的机会。",
                    "role": "definition",
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": ["P005"],
                    "summary": "按狭义（只考虑公域的）平权论，可以说女权与“平权”无关；但私域利益分割靠暴力以外的实力博弈，女性凭生育能力、性优势、外貌优势乃至组织能力争取不违公域平权的私权利都合理合法，无须因他人观感放弃；作者称这一点写在现代社会的社会契约与基本法理中，是现代化的奠基石之一，若没有对公域的收缩和对私权的解放就不会有市场竞争和自由经济。",
                    "role": "reason",
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": ["P006", "P007"],
                    "summary": "提出批评的前提规则：公共批评须先作公私域判断；私域的行为、观念除非呈请他人评判，当事人都有不受评判的自由；这不是女权独享的权利，而是所有人都享有的权利，女性只是要求平等享有。",
                    "role": "claim",
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": ["P008", "P009"],
                    "summary": "指出问题在于有人不想给；其原因或是对平等无知、或是利用大众无知助威“皇帝梦”，都在法理逻辑上站不住脚；称不会有头脑清醒的公权部门敢于出头撑腰，因为那违宪违法并会造成经济界大哗与资本出逃，并把女性的择偶自由与企业的经营自由视为完全同一的东西。",
                    "role": "claim",
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": ["P010"],
                    "summary": "回应“反对女权是否也是个人自由”：反对是个人自由，但不能用“禁止女权提出主张”的方式去反对；以竞拍为喻（可以出更高价买下，但不能禁止别人出价）；对男性的苛求若在公域侵占他人权利则付诸行动即违法，否则是法律不完善，可呼吁推动立法；若在私域则只能凭实力竞争博弈。",
                    "role": "rebuttal",
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": ["P011"],
                    "summary": "称“女性都联合起来为难男性”这种苦恼不值得评论。",
                    "role": "conclusion",
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": ["P012"],
                    "summary": "文末“女性相关答集”为平台话题标签，未被 lexical 结构覆盖。",
                    "role": "other",
                },
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者把提问中的现象归因于：太多人对权利结构缺少合理认知。",
                    "evidence": ["E1"],
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者定义：平权在公共领域指平等地担当公职的权利、平等地享有公共资源的权利、平等的法律地位，这些部分靠不断追求对等、一致、无差别来达成。",
                    "evidence": ["E2"],
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称平权在私权领域根本不以追求“对等”为特征，而是以“各凭条件做最大的主张”为基本样式；此处平权指所有人都平等地享有做最大主张的机会。",
                    "evidence": ["E3", "E4"],
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称私域的利益分割本来就是靠暴力以外的实力尽情博弈，而不是靠“公平分配”；女性靠生育能力、性优势、外貌优势甚至女性组织的组织能力去争取不违公域平权的私权利都是合理合法的行为，没有必要也没有理由因任何人的个人观感做任何放弃。",
                    "evidence": ["E5", "E6"],
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称这一点对现代社会的公民是不言自明、天然成立的，是写在社会契约和基本法理这种社会底层制度逻辑里的、现代化的奠基石之一；没有对公域的收缩和对私权的解放，就不会有市场竞争和自由经济。",
                    "evidence": ["E7"],
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称进行任何公共批评的前提都是先进行公私域的判断；属于私域的行为、观念，除非呈请他人评判，否则当事人都有不受评判的自由。",
                    "evidence": ["E8"],
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称女性要求平等享有此权利并非女权独享的权利，而是普天下所有人都享有的权利。",
                    "evidence": ["E9"],
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称问题不在于女性要求这权利，而在于有人不想给。",
                    "evidence": ["E10"],
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者称无论反对者如何喊叫，也绝不会有什么头脑清醒的公权部门敢于出头撑腰，因为那是违宪违法、要瞬间造成经济界大哗和资本出逃的；如果今天女权的合法诉求受到非法打击，则明天私营企业的经营自由必定唇亡齿寒，外资更不会坐以待毙。",
                    "evidence": ["E11", "E12"],
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称本质上女性的择偶自由与企业的经营自由是完全同一的东西。",
                    "evidence": ["E13"],
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者承认反对女权也是个人自由，但不能用“禁止女权提出主张”的方式去反对；并以竞拍为喻：可以出更高的价买下，但不能禁止别人出价。",
                    "evidence": ["E14", "E15"],
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者称若有女性主张可怕的对男性的苛求：在公域侵占他人权利，只要付诸行动就是违法行为，否则就是法律不完善，可以呼吁和推动立法；若在私域，则只能凭自己的实力去竞争和博弈。",
                    "evidence": ["E16"],
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称“女性都联合起来为难男性”这种苦恼不值得评论。",
                    "evidence": ["E17"],
                },
            ],
            "argument_steps": [
                "先归因：对权利结构缺少合理认知（P001）。",
                "给出公私域两条定义：公域平权追求对等、一致、无差别；私域平权是各凭条件做最大的主张（P002、P003、P004）。",
                "承认按狭义（公域）平权论可以说女权与“平权”无关，但把私域界定为实力博弈，据此为女性的私域主张作合法性辩护（P005）。",
                "以社会契约与基本法理、市场竞争与自由经济为该项辩护加码（P005）。",
                "提出公共批评须先作公私域判断的规则（P006）。",
                "强调该自由为所有人共有而非女权独享（P007）。",
                "把争点定位为“有人不想给”（P008）。",
                "推测反对者的动机，并以违宪违法、经济界反应、资本出逃预测其后果（P009）。",
                "以“择偶自由与经营自由同一”收束该论证（P009）。",
                "回应“反对是否也是自由”，以竞拍为喻给出边界（P010）。",
                "以“不值得评论”收尾（P011）。",
                "附平台话题标签（P012）。",
            ],
            "concept_usage": [
                {
                    "term": "平权",
                    "meaning": "作者分两层使用：公域指平等担当公职、平等享有公共资源、平等法律地位（靠对等、一致、无差别达成）；私域指所有人都平等地享有“各凭条件做最大的主张”的机会。",
                    "evidence": "P002、P003、P004",
                    "ambiguity": "同一术语在公域与私域含义不同，作者未给出统一表述；也未说明两域冲突时如何取舍。",
                },
                {
                    "term": "公域 / 私权领域（私域）",
                    "meaning": "作者以是否需要公共评判来划分：公域是可要求对等与无差别的领域；私域是利益分割靠实力博弈、当事人有不受评判自由的领域。",
                    "evidence": "P002、P003、P006",
                    "ambiguity": "两域的具体边界与判定标准本文未给出，作者在 P010 也只是按“是否侵占他人权利”区分。",
                },
                {
                    "term": "各凭条件做最大的主张",
                    "meaning": "作者对私域平权样式的表述，并解释为所有人都平等地享有做最大主张的机会。",
                    "evidence": "P003、P004",
                    "ambiguity": "“条件”的范围（是否包含生育能力、外貌等）由 P005 举例给出，但未穷尽。",
                },
                {
                    "term": "实力博弈",
                    "meaning": "作者称私域利益分割的实际方式，指靠暴力以外的实力尽情博弈，而非“公平分配”。",
                    "evidence": "P005",
                    "ambiguity": "“实力”的边界与是否有上限未说明。",
                },
                {
                    "term": "社会契约和基本法理",
                    "meaning": "作者称私域主张自由写在其中的社会底层制度逻辑，是现代化的奠基石之一。",
                    "evidence": "P005",
                    "ambiguity": "未指明具体法条或理论来源。",
                },
                {
                    "term": "皇帝梦",
                    "meaning": "作者对反对女权者动机之一的描述（利用大众的无知来助威自己的皇帝梦）。",
                    "evidence": "P009",
                    "ambiguity": "属讽刺性表述，未指名对象。",
                },
            ],
            "examples_and_targets": [
                "女性靠生育能力、性优势、外貌优势、女性组织的组织能力争取私权利（作者例证，P005）。",
                "跳槽、竞购资源、竞争、选择伴侣等一系列“不许”的假设情形（作者用于反问的例证，P005）。",
                "违反宪法与法律、经济界大哗与资本出逃（作者对后果的预测性例证，P009）。",
                "私营企业的经营自由、外资（作者类比对象，P009）。",
                "竞拍（作者用于说明“反对可以但不能禁止出价”的类比，P010）。",
                "“女性都联合起来为难男性”（作者引述并拒绝评论的说法，P011）。",
                "“女性相关答集”（平台话题标签，P012）。",
            ],
            "conditions": [
                "“如果按照狭义的平权论——就是只考虑公域——那么，你可以说女权与‘平权’无关”为作者的让步性条件（P005）。",
                "“女性靠……去争取任何可以争取得到的、不违公域平权的私权利”以不违公域平权为限定（P005）。",
                "“除非呈请ta人评判，否则当事人都有不受评判的自由”为私域自由规则的例外条件（P006）。",
                "“只要付诸行动就是违法行为，否则就是法律不完善”为公域苛求的两种情形（P010）。",
                "“如果是在私域，那么你可以、也只能凭自己的实力去竞争和博弈”为私域情形下的限定（P010）。",
                "“至于扭头走后是不是还有别的选择，那是你自己实力的问题”为作者对后果的归属限定（P010）。",
                "作者多处使用“也许”“绝不是”“本质上”等词，动机判断以推测语气给出。",
            ],
            "rhetoric_and_tone": "论辩与法理式说理混合：先给定义再推结论，句式偏书面、术语化（“公域”“私权领域”“社会契约”“基本法理”）；使用连续排比的反问（“不许你凭自己的能力跳槽……你觉得这叫‘公平’还是叫‘压迫’？”）加强质问感；用竞拍作日常类比降低抽象度；对反对者使用带讽刺的评断（“助威自己的皇帝梦”“头脑清醒的公权部门”“不值得评论”），整体语气自信、边界感强。",
            "unresolved_questions": [
                "文末 P012“女性相关答集”为平台话题标签且 lexical 未覆盖该片段，是否属作者正文无法确定。",
                "公域与私域的具体边界与判定标准，本文未给出，仅以举例和“是否侵占他人权利”提示。",
                "“社会契约和基本法理”未指明具体法条或理论来源，相关法理断言属待外部核查。",
                "作者称“绝不会有什么头脑清醒的公权部门敢于出头撑腰”，为对未来的强预测，本文未给出经验依据。",
                "“女性都联合起来为难男性”这一说法的出处与所指未说明，作者仅表示“不值得评论”。",
                "本篇 updated_at（2024-12-18）远晚于 published_at（2018-10-13），正文是否经修订、修订内容为何，语料未提供版本差异信息。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "因为太多人对权利结构缺少合理认知。", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "平权在公共领域，是指平等地担当公职的权利、平等地享有公共资源的权利、平等的法律地位。", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P003", "quote": "平权在私权领域，则根本不以追求“对等”为特征，而是以“各凭条件做最大的主张”为基本样式。", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P004", "quote": "所谓的平权，在这里指所有人都平等地享有这做最大主张的机会。", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P005", "quote": "因为在私域的利益分割本来就是靠暴力以外的实力尽情博弈，而不是靠什么“公平分配”。", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P005", "quote": "女性靠生育能力、性优势、外貌优势、甚至女性组织的组织能力去争取任何可以争取得到的、不违公域平权的私权利都是合理合法的行为", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P005", "quote": "因为如果没有对公域的收缩和对私权的解放，就不会有市场竞争和自由经济。", "relation": "supports"},
                {"key": "E8", "paragraph_id": "P006", "quote": "进行任何公共批评的前提都是先进行公私域的判断。", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P007", "quote": "这不是女权所要求独享的权利，而是普天下所有人都享有的权利，女性在要求平等享有此权利。", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P008", "quote": "问题不在于女性要求这权利，而在于有人不想给。", "relation": "supports"},
                {"key": "E11", "paragraph_id": "P009", "quote": "也绝不会有什么头脑清醒的公权部门敢于出头撑腰——那是违宪违法、要瞬间造成经济界大哗和资本出逃的。", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P009", "quote": "因为如果今天女权的合法诉求受到非法打击，则明天私营企业的经营自由必定唇亡齿寒，外资更不会坐以待毙。", "relation": "supports"},
                {"key": "E13", "paragraph_id": "P009", "quote": "本质上，女性的择偶自由与企业的经营自由是完全同一的东西。", "relation": "supports"},
                {"key": "E14", "paragraph_id": "P010", "quote": "不错，反对女权也是你的个人自由。但是你不能用“禁止女权提出主张”的方式去反对。", "relation": "supports"},
                {"key": "E15", "paragraph_id": "P010", "quote": "就像大家一起参加竞拍，你可不可以反对人家买下？可以，你出更高的价买下就是，但你不能禁止别人出价。", "relation": "supports"},
                {"key": "E16", "paragraph_id": "P010", "quote": "如果是在公域侵占了他人权利，只要付诸行动就是违法行为，否则就是法律不完善，你可以呼吁和推动立法。", "relation": "supports"},
                {"key": "E17", "paragraph_id": "P011", "quote": "至于说“女性都联合起来为难男性”这种苦恼，不值得评论。", "relation": "supports"},
                {"key": "E18", "paragraph_id": "P012", "quote": "女性相关答集", "relation": "context"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["性别议题", "法理与权利理论", "公共讨论规范"],
            "issue_candidates": ["女权与平权的语义差异", "公域与私域的划分", "择偶自由与经营自由的类比", "反对女权的边界"],
            "text_function_candidates": ["答疑", "论辩", "概念辨析"],
            "object_candidates": ["女权", "男权", "女性", "公权部门", "私营企业", "外资"],
            "working_keywords": ["平权", "公域", "私权", "对等", "实力博弈", "社会契约", "择偶自由", "女性相关答集"],
        },
        "notes": "无图片节点。text 与 lexical 有 1 处差异：正文末尾“女性相关答集”（char_start=1157）为 lexical 未覆盖的平台话题标签，已登记。",
    },
    "bbe903b2": {
        "analysis": {
            "question_context": "提问者问“中华文明的自信来源于何处？”（Q001）。作者称这个问题“没头没脑”，但因不满该问题下其它答案而作答：先指出近现代中国常把“自信”的概念扭曲，再重新定义自信（对自己拥有有信度的认知的心理状态），区分自信与自豪，批评以“自豪感”为精神鸦片的心态，最后警告继续发掘“自信的理由”可能把中国引入错误估计能力的冲突。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": ["P001", "P002", "P003"],
                    "summary": "交代作答缘由（本不想回答，因看了该问题下的答案而觉得不说不行），指出中国近现代特别爱提自信而概念常被扭曲，并提出“自信到底是什么？应该以什么为基础？”两问。",
                    "role": "context",
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": ["P004"],
                    "summary": "以反问设定前提：假如一个人不是天下第一、也没有任何技能天下第一，他是否就不该有任何自信、就该“自卑”。",
                    "role": "reason",
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": ["P005"],
                    "summary": "主张自信与自豪没有也不该有关联；强行关联会得到病态的对“排名第一”的无意义追求，并因争夺第一者不纠结这些而浪费更多时间精力，反与顶尖水平无缘，陷入自欺欺人。",
                    "role": "claim",
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": ["P006", "P007", "P008", "P009"],
                    "summary": "给出自信的定义与例子：以“我不是跑得最快的人，但我对能在十二秒内跑完一百米有很强把握”为例；称自信不是对自己的崇拜，而是对自己拥有有信度的认知的人所处的心理状态；其价值在于知道自己能做到何事、预料符合事实、计划有高概率实现。",
                    "role": "definition",
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": ["P010", "P011"],
                    "summary": "指出自信人人本来就有，只是被觉得“不值钱”、不足夸耀人前；称人不是缺自信而是缺崇拜，需要的是化名为“自豪感”的被崇拜感。",
                    "role": "claim",
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": ["P012", "P013"],
                    "summary": "把“自豪感”称为某种体系为使人依附而提供的精神鸦片，承认其精神上的“美味”，但反问缺了它哪里活不下去；称所谓窘迫尴尬本质是戒断反应，并追问是为中华之崛起而奋斗还是为怕断瘾而饥不择食；末以“还不戒？！”催促。",
                    "role": "rebuttal",
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": ["P014", "P015"],
                    "summary": "称中国曾有辉煌、现世也不缺光彩，但这与它该不该“自信”毫无关系；它本来强大，不靠矜夸傲慢、虚妄荣耀或像守财奴一样每日数金子来维持；并再次反问人凭什么非要先“自豪”起来才能撑下去。",
                    "role": "reason",
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": ["P016"],
                    "summary": "称不分神考虑这些东西的人实际强大得多；承认强烈自尊心可作为心理驱动力（“怕断供的瘾君子当然什么都做得到”），但追问该驱动机制是否健康，并称不健康的长期后果能要命。",
                    "role": "qualification",
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": ["P017", "P018"],
                    "summary": "提出“少年强则国强”，称少年需要的自信与“天下第一”无关、与排名无关；关键在自信凭的是什么——不能凭“自信”去构建自信，得真的跑进过十秒才能相信下次可能跑进十秒；健康的自信需要艰苦卓绝、持续不断的努力；并称有一天凭这种认知赌上一切时才知道真正的自信是什么。",
                    "role": "conclusion",
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": ["P019"],
                    "summary": "警告：按该问题下各种答案继续发掘“自信的理由”，很可能将中国引入一场既错误估计自己能力、又基于错误理由的冲突；并称“弱小不是生存的障碍，傲慢才是”。",
                    "role": "conclusion",
                },
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称中国近现代以来特别爱提自信，而这个自信的概念常常是扭曲的。",
                    "evidence": ["E1"],
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者以反问提出前提：假如一个人并不是天下第一，而且没有任何一种技能是天下第一，他是不是就不该有任何自信、就该“自卑”。",
                    "evidence": ["E2"],
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者称自信与自豪没有、也不该有关联；一旦强行关联，获得的将不是任何意义上的“自信”，而是病态的对“排名第一”的无意义追求。",
                    "evidence": ["E3"],
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者称因为与你争夺第一的人不纠结这些而少浪费很大一笔时间和精力，你反而总是与顶尖水平无缘，于是总是沉浸在因无法甘心而无穷尽的自欺欺人之中。",
                    "evidence": ["E4"],
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者以举例定义自信：“我不是天下跑步最快的人，但是我对我能在十二秒内跑完一百米有很强的把握”，这个才叫做自信。",
                    "evidence": ["E5"],
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者称自信不是对自己的崇拜，而是对自己拥有有信度的认知的人所处的心理状态。",
                    "evidence": ["E6"],
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称一个人知道自己可以做到何事、预料确实符合事实、按此做的计划果然有高概率实现，这就是自信的实际意义和真实价值。",
                    "evidence": ["E7"],
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称自信是人人都应该有的东西，你本来就有，只是觉得那些“不值钱”、不足夸耀人前；你不是缺自信，你是缺崇拜，需要的是化名为“自豪感”的被崇拜感。",
                    "evidence": ["E8", "E9"],
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称“自豪感”只是某种体系为了你的依附而提供给你的精神鸦片，所谓“令人绝望的窘迫和尴尬”本质上只是精神鸦片令人不寒而栗的戒断反应。",
                    "evidence": ["E10", "E11"],
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称中国曾有种种辉煌、也不会缺现世的光彩，但这跟它该不该“自信”毫无关系；它本来如此强大，根本不需要那些“自豪”。",
                    "evidence": ["E12"],
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者承认很多人主张强烈的自尊心是自己的基本心理驱动力之一，并称驱动力客观存在，但追问这驱动机制是否健康，称驱动机制不健康长期后果能要命。",
                    "evidence": ["E13"],
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称少年所需要的自信跟“天下第一”不该有关系，这种真正的自信与排名无关，每个人都有也该有。",
                    "evidence": ["E14"],
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者称人不能凭“自信”去构建自己的自信；你得真的跑进过十秒，才能相信自己下次可能还能跑进十秒；要构建健康的、真实的自信，需要艰苦卓绝、持续不断的努力。",
                    "evidence": ["E15", "E16"],
                },
                {
                    "claim_id": "C014",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者警告：按照这个问题下各种答案的做法继续发掘“自信的理由”，很可能将中国引入一场既错误估计自己能力、又基于错误理由的冲突中去。",
                    "evidence": ["E17"],
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者以“弱小不是生存的障碍，傲慢才是”收束全文。",
                    "evidence": ["E18"],
                },
            ],
            "argument_steps": [
                "交代作答缘由并指出“自信”概念在中国近现代常被扭曲（P001、P002、P003）。",
                "以“不是天下第一是否就该自卑”的反问设定讨论前提（P004）。",
                "割断自信与自豪的关联，指出强行关联导致对排名的病态追求与自欺欺人（P005）。",
                "以跑步成绩为例给出自信的正例（P007）。",
                "以“不是对自己的崇拜”给出自信的定义（P008）。",
                "以“预料符合事实、计划高概率实现”说明自信的实际价值（P009）。",
                "指出人们本有自信却嫌其不值钱，真正缺的是被崇拜感（P010、P011）。",
                "把“自豪感”指为精神鸦片并追问其戒断反应（P012），以“还不戒？！”催促（P013）。",
                "以中国的历史与现实说明其不需要“自豪”（P014），再次反问（P015）。",
                "承认自尊心可作为驱动力，但质疑该机制是否健康（P016）。",
                "给出构建健康自信的路径：与排名无关、须以真实成绩为依据、须持续努力（P017、P018）。",
                "以“可能把中国引入错误估计能力的冲突”与“弱小不是生存的障碍，傲慢才是”收尾（P019）。",
            ],
            "concept_usage": [
                {
                    "term": "自信",
                    "meaning": "作者定义为“对自己拥有有信度的认知的人所处的心理状态”，并以“对能在十二秒内跑完一百米有很强把握”为例；其价值在于预料符合事实、计划高概率实现。",
                    "evidence": "P007、P008、P009",
                    "ambiguity": "作者未给出“有信度的认知”的判定标准。",
                },
                {
                    "term": "自豪（自豪感）",
                    "meaning": "作者将其与自信切割，称为“化名为自豪感的被崇拜感”，并指为某种体系为使人依附而提供的精神鸦片。",
                    "evidence": "P005、P011、P012",
                    "ambiguity": "作者未指明“某种体系”具体所指。",
                },
                {
                    "term": "精神鸦片",
                    "meaning": "作者对“自豪感”的比喻，称其精神上“美味”，但戒断反应令人不寒而栗。",
                    "evidence": "P012",
                    "ambiguity": "属比喻性表述，无定义。",
                },
                {
                    "term": "天下第一 / 排名",
                    "meaning": "作者用以指与自信被错误绑定的比较性目标，称真正的自信与之无关。",
                    "evidence": "P004、P005、P014、P017",
                    "ambiguity": "作者未说明是否存在可追求排名的正当场合。",
                },
                {
                    "term": "少年强则国强",
                    "meaning": "作者引用的说法，用以说明少年所需的自信与“天下第一”无关。",
                    "evidence": "P017",
                    "ambiguity": "作者未注明出处（语出梁启超《少年中国说》），也未展开。",
                },
            ],
            "examples_and_targets": [
                "“我不是天下跑步最快的人，但是我对我能在十二秒内跑完一百米有很强的把握”（作者的核心例证，P007）。",
                "跑进十秒与跑进十二秒的对比（作者用于说明自信须凭真实成绩的例子，P017）。",
                "中国曾有种种辉煌、世界第一人口大国、现世的光彩（作者用作对照的事实陈述，P014）。",
                "“像守财奴一样每天数一遍自己的金子”（作者的比喻，P014）。",
                "“怕断供的瘾君子”（作者对依赖自豪感者的比喻，P016）。",
                "“历史的路上满地都是‘自信’者的尸骨”（作者的比喻性说法，P019）。",
                "“弱小不是生存的障碍，傲慢才是”（作者引用的格言式表述，P019）。",
                "该问题下的各种答案（作者批评的对象，P001、P019）。",
                "“中华之崛起”（作者在反问中引用的说法，P012）。",
            ],
            "conditions": [
                "“假如一个人并不是天下第一，而且没有任何一种技能是天下第一”为 P004 反问的假设条件。",
                "“一旦你强行关联起来”为自信与自豪关联后的后果条件（P005）。",
                "“除非……”句式未出现；限定主要靠“本质上”“很可能”“应该”等词。",
                "“如果是在……”未出现；P018 以“有一天你凭着这种认知去赌上你的一切的时候”为时间条件。",
                "“按照这个问题下的各种答案的做法继续发掘‘自信的理由’”为 P019 警告的前提条件。",
                "作者在 P014 强调“这跟它该不该‘自信’毫无关系”，为对推论范围的限定。",
                "P016 以“很多人会主张……”引出对方观点后再作限定性追问，属让步式限定。",
            ],
            "rhetoric_and_tone": "训诫与反问交织的劝诫体：以第二人称“你”直呼读者，连续反问（“他是不是就不该有任何自信？就该‘自卑’？”“你到底哪里缺了这‘自豪感’活不下去？”“还不戒？！”）；大量使用贬抑性比喻（精神鸦片、瘾君子、守财奴、饥不择食）；以短句“还不戒？！”与英文“Again”调节节奏；对“该问题下的各种答案”持明显批评态度，末尾以格言式警句收束，整体语气激烈、价值判断鲜明。",
            "unresolved_questions": [
                "作者未指明“某种体系”（提供精神鸦片者）具体所指。",
                "“少年强则国强”的出处未注明（未提及梁启超《少年中国说》）。",
                "“中华文明的自信来源于何处”这一提问本身，作者未给出正面回答，而是改问“自信应以什么为基础”。",
                "“弱小不是生存的障碍，傲慢才是”是否为引用他处、出自何处，本文未说明。",
                "“历史的路上满地都是‘自信’者的尸骨”为修辞性断言，未给出例证。",
                "本篇 updated_at（2023-07-29）晚于 published_at（2018-10-15），正文是否经修订、修订内容为何，语料未提供版本差异信息。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P002", "quote": "中国近现代以来特别爱提自信，而这个自信的概念常常是扭曲的。", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P004", "quote": "假如一个人并不是天下第一，而且没有任何一种技能是天下第一，他是不是就不该有任何自信？就该“自卑”？", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P005", "quote": "注意，自信与自豪没有、也不该有关联。", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P005", "quote": "而且因为与你争夺第一的人不纠结这些而少浪费很大一笔时间和精力，你反而总是与顶尖水平无缘。", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P007", "quote": "“我不是天下跑步最快的人，但是我对我能在十二秒内跑完一百米有很强的把握”，这个，才叫做自信。", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P008", "quote": "看清楚，自信，不是对自己的崇拜！自信，是对自己拥有有信度的认知的人所处的心理状态。", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P009", "quote": "一个人知道自己可以做到何事，而且他的预料确实符合事实，他按此做的计划果然有高概率实现，这就是自信的实际意义和真实价值", "relation": "supports"},
                {"key": "E8", "paragraph_id": "P010", "quote": "自信是人人都应该有的东西。你本来就有，你只是觉得那些“不值钱”，不足夸耀人前", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P011", "quote": "你不是缺自信，你是缺崇拜。你需要的是化名为“自豪感”的被崇拜感。", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P012", "quote": "它只是某种体系为了你的依附而提供给你的精神鸦片。", "relation": "supports"},
                {"key": "E11", "paragraph_id": "P012", "quote": "这种“令人绝望的窘迫和尴尬”，本质上只是精神鸦片令人不寒而栗的戒断反应。", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P014", "quote": "这跟它该不该“自信”毫无关系。而它本来如此强大，根本不需要那些“自豪”。", "relation": "supports"},
                {"key": "E13", "paragraph_id": "P016", "quote": "很多人会主张强烈的自尊心是自己的基本心理驱动力之——那当然，怕断供的瘾君子当然“什么都做得到”。驱动力客观存在，但是这驱动机制健康吗？", "relation": "qualifies"},
                {"key": "E14", "paragraph_id": "P017", "quote": "少年强则国强，少年所需要的自信跟“天下第一”不该有关系。这种真正的自信，与你的排名无关，每个人都有，也该有。", "relation": "supports"},
                {"key": "E15", "paragraph_id": "P017", "quote": "你不能凭自己的“自信”吧？人不能凭“自信”去构建自己的自信。", "relation": "supports"},
                {"key": "E16", "paragraph_id": "P017", "quote": "要构建健康的、真实的自信，是需要艰苦卓绝、持续不断的努力的。", "relation": "supports"},
                {"key": "E17", "paragraph_id": "P019", "quote": "按照这个问题下的各种答案的做法继续发掘“自信的理由”，很可能将中国引入一场既错误估计自己能力，又基于错误理由的冲突中去。", "relation": "supports"},
                {"key": "E18", "paragraph_id": "P019", "quote": "毕竟，弱小不是生存的障碍，傲慢才是。", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["心理学", "文化批评", "社会心态"],
            "issue_candidates": ["自信与自豪的区分", "民族自豪感与精神依附", "排名的无意义追求", "中华文明自信的基础"],
            "text_function_candidates": ["答疑", "评论", "训诫", "批评"],
            "object_candidates": ["中国", "中华文明", "少年", "该问题下的答主", "公权部门（未出现）"],
            "working_keywords": ["自信", "自豪感", "被崇拜感", "精神鸦片", "天下第一", "排名", "少年强则国强", "傲慢"],
        },
        "notes": "无图片节点。本篇 text 与 lexical 无差异（divergence=false）。作者未正面回答“中华文明的自信来源于何处”，而是重定义为“自信应以什么为基础”，转写为对“自豪感”的批评。",
    },
    "43a68274": {
        "analysis": {
            "question_context": "提问者问“大脑是否记住了所有的东西？”（Q001）。作者先指出要定义“所有东西”，改以视觉数据量与脑细胞总数的数量级对比作答，最后让读者自行估计“大脑是不是‘记住了所有东西只是想不起来’”。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": ["P001", "P002"],
                    "summary": "指出提问需要先定义“所有东西”，并提出换一个提法。",
                    "role": "qualification",
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": ["P003"],
                    "summary": "估算视觉数据量：一眼窗外图像约230万像素（七百万视锥细胞除以三原色），经大脑处理生成约2亿有效像素；忽略有效分辨率只算实际230万，色彩分辨率按65000色计，一眼约2.3MByte；按每秒18帧、每天睁眼16小时计，一天视觉数据量为 18x3600x16x2.3/1024GB = 2328.75GB，且未计声音、脑补、梦与思考成果。",
                    "role": "reason",
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": ["P004"],
                    "summary": "给出对照量：人体脑细胞总数大概150亿个。",
                    "role": "reason",
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": ["P005"],
                    "summary": "请读者据此自行估计大脑是不是“记住了所有东西只是想不起来”。",
                    "role": "conclusion",
                },
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为这个问题需要定义什么叫做“所有东西”，因此换一个提法。",
                    "evidence": ["E1"],
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者估算：眼睛看一眼窗外接收到的图像大小大概是230万像素（七百万视锥细胞除以三原色），经大脑处理却生成大约2亿有效像素。",
                    "evidence": ["E2"],
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者在“忽略有效分辨率、只算实际分辨率230万、色彩分辨率算65000色、每秒18帧、每天睁眼16小时”等设定下算出一天视觉数据量约 2328.75GB，并声明只算了图像，没算声音、脑补、梦与思考成果。",
                    "evidence": ["E3", "E4"],
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称人体脑细胞总数大概150亿个。",
                    "evidence": ["E5"],
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者请读者据此估计：你的大脑是不是“记住了所有东西只是想不起来”。",
                    "evidence": ["E6"],
                },
            ],
            "argument_steps": [
                "指出提问缺少“所有东西”的定义，改为按视觉输入量估算（P001、P002）。",
                "给出视觉数据量的逐步估算过程与结果（P003）。",
                "给出脑细胞总数的对照量（P004）。",
                "不直接下结论，让读者自行比较并判断“记住了所有东西只是想不起来”是否成立（P005）。",
            ],
            "concept_usage": [
                {
                    "term": "所有东西",
                    "meaning": "作者称提问中的“所有东西”需要定义，否则无法回答，并以视觉输入为例替换该提法。",
                    "evidence": "P001、P002",
                    "ambiguity": "作者未给出自己认可的“所有东西”定义。",
                },
                {
                    "term": "有效像素",
                    "meaning": "作者称大脑处理后的生成量（约2亿），并明确在计算中暂时忽略。",
                    "evidence": "P003",
                    "ambiguity": "“经大脑处理却生成大约2亿有效像素”未给出来源。",
                },
                {
                    "term": "帧",
                    "meaning": "作者把视觉输入按每秒18帧折算，属于其计算假设。",
                    "evidence": "P003",
                    "ambiguity": "18帧/秒的取值依据未说明（原文用“宽泛一点，就算”）。",
                },
            ],
            "examples_and_targets": [
                "七百万视锥细胞除以三原色 → 230万像素（作者的计算设定，P003）。",
                "65000色、每秒18帧、每天睁眼16小时（作者的计算设定，P003）。",
                "18x3600x16x2.3/1024GB = 2328.75GB（作者给出的算式与结果，P003）。",
                "人体脑细胞总数大概150亿个（作者的对照数据，P004）。",
                "“记住了所有东西只是想不起来”（作者引述的常见说法并请读者自行判断，P005）。",
            ],
            "conditions": [
                "“这需要定义什么叫做‘所有东西’”为作者对提问可答性的限定（P001）。",
                "“这个有效分辨率我们暂时忽略，只算实际分辨率230万”为计算范围的限定（P003）。",
                "“考虑到你的色彩分辨率，我们就算65000色好了”为取值假设（P003）。",
                "“宽泛一点，就算这样的图像1秒钟就只产生18帧”为作者的粗略假设（P003）。",
                "“一天的视觉的数据量按睁眼16个小时算”为时间范围限定（P003）。",
                "“只算了图像，没算声音，没算你自己脑补的小姐姐，没算你做的梦，也没算你的思考成果”为计算覆盖范围的明确限定（P003）。",
            ],
            "rhetoric_and_tone": "极简的估算式回答：不直接下结论，靠“230万像素/2.3MByte/2328.75GB”与“150亿脑细胞”两组数量级形成暗示；“换一个提法吧”与末尾“你可以估计一下”把判断交回读者；夹入“没算你自己脑补的小姐姐”这类口语化调侃，语气轻松。",
            "unresolved_questions": [
                "作者未给出“所有东西”的定义，也未正面回答大脑是否记住了所有东西。",
                "七百万视锥细胞、2亿有效像素、65000色、18帧/秒、150亿脑细胞等数值均未注明来源，属待外部核查。",
                "算式 18x3600x16x2.3/1024GB = 2328.75GB 的单位与取整方式未说明（是否按二进制 GB 计算未注明）。",
                "作者用脑细胞总数与视觉数据量作对比，但未说明两者为何可直接比较（未讨论每个细胞的存储能力）。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "这需要定义什么叫做“所有东西”。", "relation": "qualifies"},
                {"key": "E2", "paragraph_id": "P003", "quote": "你眼睛看一眼窗外，接收到的图像大小大概是230万像素（七百万视锥细胞除以三原色），经大脑处理却生成大约2亿有效像素。", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P003", "quote": "一天的视觉的数据量按睁眼16个小时算，就是18x3600x16x2.3/1024GB = 2328.75GB", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P003", "quote": "只算了图像，没算声音，没算你自己脑补的小姐姐，没算你做的梦，也没算你的思考成果。", "relation": "qualifies"},
                {"key": "E5", "paragraph_id": "P004", "quote": "人体脑细胞总数大概150亿个。", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P005", "quote": "你可以估计一下你的大脑是不是“记住了所有东西只是想不起来”。", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["认知科学", "神经科学", "信息论"],
            "issue_candidates": ["记忆容量", "视觉信息量估算", "脑细胞数量与存储"],
            "text_function_candidates": ["答疑", "数量级估算"],
            "object_candidates": ["大脑", "视锥细胞", "脑细胞"],
            "working_keywords": ["所有东西", "像素", "视锥细胞", "有效像素", "帧", "脑细胞", "记住了所有东西只是想不起来"],
        },
        "notes": "无图片节点。本篇 text 与 lexical 无差异（divergence=false）。作者未给出正面结论，只提供两组数量级并请读者自行估计；多个数值需外部核查。",
    },
    "6e462ebf": {
        "analysis": {
            "question_context": "提问者三问：义和团是个什么样的组织？同外国侵略者作战等于送死吗？义和团为什么会兴起？（Q001）。作者未逐一回答，而是把矛头指向“义和团是反抗洋人对农民的压迫”这一流行解释：先称晚清社会中“要求完全履行明文契约”已属显而易见压迫，再以反问比较洋人与地主、满清的压迫程度，最后直接质疑持该说法的“专业历史研究者”的严谨性。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": ["P001"],
                    "summary": "提出背景判断：在晚清的中国社会，哪怕要求完全履行明文契约、不接受打折、不给优惠、不接受妥协，都已经算是一种显而易见的压迫。",
                    "role": "claim",
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": ["P002"],
                    "summary": "向持“义和团是反抗洋人对农民的压迫”说法者反问：洋人的压迫真的比他们自己家的地主更严重吗？比满清的压迫更严重吗？",
                    "role": "rebuttal",
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": ["P003"],
                    "summary": "提出另一个追问：洋人的“罪”到底是“压迫”的罪，还是“没有压迫资格就压迫我们”的罪。",
                    "role": "rebuttal",
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": ["P004"],
                    "summary": "称“义和团杀洋人是因为被压迫”是根本没有仔细想过的答案；并反问在压迫中国人的多种势力中，无论压迫之烈、获利之多、手段之残忍、持续之长久，洋人能排第几名。",
                    "role": "rebuttal",
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": ["P005"],
                    "summary": "直接批评一些端着“专业历史研究者”架子却称“义和团是因为反压迫”的人缺乏谈历史学术必要的严谨性，并列出三种可能：无心、学力不足、或明知不是这么回事而别有目的。",
                    "role": "conclusion",
                },
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称在晚清的中国社会，哪怕要求完全履行明文契约、不接受打折、不给优惠、不接受妥协，都已经算是一种显而易见的压迫了。",
                    "evidence": ["E1"],
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者向“义和团是反抗洋人对农民的压迫”的说法持有者反问：洋人对他们的压迫，真的比他们自己家的地主们更严重吗？比满清的压迫更严重吗？",
                    "evidence": ["E2"],
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者追问：洋人的“罪”，到底是“压迫”的罪，还是“没有压迫资格就压迫我们”的罪。",
                    "evidence": ["E3"],
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者称“所谓义和团杀洋人是因为‘被压迫’”其实是根本没有仔细想过的答案，并反问在压迫中国人的多种势力里，无论压迫之烈、获利之多、手段之残忍、持续之长久，洋人能排得上第几名。",
                    "evidence": ["E4", "E5"],
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称一些端着“专业历史研究者”架子却口口声声“义和团是因为反压迫”的人，没有谈历史学术必要的严谨性；要么是无心的，要么是学力不足，要么就是明知不是这么回事而别有目的。",
                    "evidence": ["E6"],
                },
            ],
            "argument_steps": [
                "先给定晚清社会的背景判断：要求完全履行明文契约已属压迫（P001）。",
                "以反问把“洋人压迫”与“自家地主”“满清”的压迫作比较（P002）。",
                "进而追问“罪”的性质是压迫本身还是“没有压迫资格”（P003）。",
                "否定“因被压迫而杀洋人”的解释，并以“压迫程度排名”反问（P004）。",
                "把批评指向持该说法的“专业历史研究者”，列举三种可能（P005）。",
            ],
            "concept_usage": [
                {
                    "term": "压迫",
                    "meaning": "作者在晚清语境下使用，并把“要求完全履行明文契约、不接受打折、不给优惠、不接受妥协”也纳入“显而易见的压迫”。",
                    "evidence": "P001、P002、P004",
                    "ambiguity": "作者未给出“压迫”的定义与衡量尺度，比较对象（地主、满清、洋人）的压迫程度也未给出数据。",
                },
                {
                    "term": "明文契约",
                    "meaning": "作者称在晚清社会中严格履行明文契约本身即构成压迫，是其论证的前提。",
                    "evidence": "P001",
                    "ambiguity": "未指明具体条约或契约，也未说明是否为不平等条约。",
                },
                {
                    "term": "没有压迫资格就压迫我们",
                    "meaning": "作者用以重述“洋人的罪”的另一种可能：问题不在压迫本身，而在压迫者的资格。",
                    "evidence": "P003",
                    "ambiguity": "该表述是作者对他人心理的概括，未指明具体所指。",
                },
                {
                    "term": "专业历史研究者",
                    "meaning": "作者对被批评对象的称呼（端着该架子而称义和团因反压迫者）。",
                    "evidence": "P005",
                    "ambiguity": "作者未指名任何人或著作。",
                },
            ],
            "examples_and_targets": [
                "晚清中国社会中“要求完全履行明文契约”的情形（作者的前提例证，P001）。",
                "义和团（提问对象，作者在 P004 引述关于其杀洋人原因的说法）。",
                "洋人、地主、满清（作者用作压迫程度的比较对象，P002、P004）。",
                "“专业历史研究者”（作者的批评对象，P005）。",
            ],
            "conditions": [
                "“在晚清的中国社会”为全文讨论的时代限定（P001）。",
                "“哪怕要求完全履行明文契约，不接受打折、不给优惠、不接受妥协”为作者对“压迫”门槛的限定（P001）。",
                "“在‘压迫’中国人的多种势力里面”为 P004 比较的范围限定（P004）。",
                "“要么ta们是无心的，要么是学力不足，要么就是明知不是这么回事而别有目的”为作者对批评对象动机的三种可能并列，未择一断言（P005）。",
            ],
            "rhetoric_and_tone": "质问式短评，语气尖锐：连续使用反问（“真的比ta们自己家的地主们更严重吗？”“能排得上第几名？”）而不给正面论证；以“口口声声”“恕我直言”“端着……架子”等措辞表达不满；结尾以三种动机的并列暗指对方别有目的，带明显训诫与讽刺色彩。",
            "unresolved_questions": [
                "提问的三个问题（义和团是什么样的组织、同外国侵略者作战是否等于送死、义和团为什么兴起）在正文中均未正面回答。",
                "“洋人的压迫与地主、满清的压迫孰轻孰重”只以反问提出，未给出史料或数据。",
                "被批评的“专业历史研究者”未指名，其具体论述无法核对。",
                "“明文契约”具体所指（是否指不平等条约）未说明。",
                "作者未说明义和团兴起的自身原因，也未讨论其组织形态。",
                "本篇 updated_at（2025-09-24）远晚于 published_at（2018-10-21），正文是否经修订、修订内容为何，语料未提供版本差异信息。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "在晚清的中国社会，哪怕要求完全履行明文契约，不接受打折、不给优惠、不接受妥协，都已经算是一种显而易见的压迫了。", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "洋人对ta们的压迫，真的比ta们自己家的地主们更严重吗？比满清的压迫更严重吗？", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P003", "quote": "洋人的“罪”，到底是“压迫”的罪，还是“没有压迫资格就压迫我们”的罪？", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P004", "quote": "所谓义和团杀洋人是因为“被压迫”其实是根本没有仔细想过的答案。", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P004", "quote": "无论是压迫之烈、获利之多、手段之残忍、持续之长久，“洋人”能排得上第几名？", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P005", "quote": "一些端着“专业历史研究者”架子却口口声声“义和团是因为反压迫”的人，没有谈历史学术必要的严谨性。", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["中国近代史", "史学方法", "社会批评"],
            "issue_candidates": ["义和团运动的成因", "洋人与地主、满清压迫的比较", "历史研究的严谨性"],
            "text_function_candidates": ["答疑", "批评", "论辩"],
            "object_candidates": ["义和团", "洋人", "地主", "满清", "专业历史研究者", "晚清中国"],
            "working_keywords": ["义和团", "压迫", "明文契约", "洋人", "满清", "反压迫", "严谨性"],
        },
        "notes": "无图片节点。本篇 text 与 lexical 无差异（divergence=false）。正文为极短的质问式回答，三个提问均未正面回答；对被批评者的动机只列三种可能，未择一断言，记录时保留该不确定性。",
    },
    "c2f0a020": {
        "analysis": {
            "question_context": "提问者问“这个世界上有无条件的爱吗？”（Q001）。作者由“爱”的定义推出其必然无条件，指出人类是需要所得的存在，因此可持续的爱只有两条路线：由完全不需要回报的存在承担，或由外部的、不需要回报的存在替被爱者支付；并称若否决这一存在，毫无所求的爱会一同幻灭，最终变成强买强卖的放债行为。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": ["P001"],
                    "summary": "提出定义性判断：可以被称为爱的，必然是无条件的，这是爱的定义决定的。",
                    "role": "definition",
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": ["P002", "P003"],
                    "summary": "提出人类方面的前提：人无法永生、无法超越自然规律、无法摆脱自身局限，需要生存、收获、安全、正反馈等所得；因此爱若要可持续，逻辑上只有两条可行路线。",
                    "role": "reason",
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": ["P004", "P005"],
                    "summary": "列出两条路线：A. 存在于完全不需要任何回报的存在身上；B. 由一种外部的、不需要回报的存在帮助人类成全——爱人所需要的由该存在支付，被爱者不欠债，爱人者不被耗尽，爱才可持续。",
                    "role": "claim",
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": ["P006"],
                    "summary": "给出反面推论：若否决掉这个存在，毫无所求的爱也就一同幻灭；没有别的事物能补全这等式的缺口，等式越运转越失衡，最后“爱”人的人必要将大笔“债务”记到被“爱”者身上，“爱”就成了一种强买强卖的放债行为。",
                    "role": "conclusion",
                },
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称可以被称为爱的，必然是无条件的，这是爱的定义决定的。",
                    "evidence": ["E1"],
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者称人类作为一种无法永生、无法超越自然规律、同时也无法摆脱自身局限的存在，需要生存、需要收获、需要安全、需要正反馈等等所得。",
                    "evidence": ["E2"],
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者称所以爱从逻辑上说，如果要可持续，就只有两种可行的路线。",
                    "evidence": ["E3"],
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "路线A：在完全不需要任何回报的存在身上存在。",
                    "evidence": ["E4"],
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "路线B：由一种外部的、不需要回报的存在帮助人类成全——爱人的人所需要的，不由被爱的人支付，而是由这个存在支付；这样被爱的人并不欠债，而爱人的人又不被耗尽，爱才可以持续。",
                    "evidence": ["E5"],
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者称如果否决掉这个存在，那么毫无所求的爱也就一同幻灭了；没有别的事物能补全这等式的缺口，这等式越是运转就越是失衡，最后“爱”人的人必要将大笔的“债务”记到被“爱”者身上，“爱”就成了一种强买强卖的放债行为了。",
                    "evidence": ["E6", "E7"],
                },
            ],
            "argument_steps": [
                "由爱的定义推出：可称为爱者必然无条件（P001）。",
                "指出人的有限性与需要（生存、收获、安全、正反馈）（P002）。",
                "由上述前提推出可持续的爱只有两条路线（P003）。",
                "给出路线A：存在于完全不需要回报的存在身上（P004）。",
                "给出路线B：由外部的、不需要回报的存在代为支付，使被爱者不欠债、爱人者不被耗尽（P005）。",
                "反证：若否决该存在，爱将失衡并转为放债行为（P006）。",
            ],
            "concept_usage": [
                {
                    "term": "无条件的爱",
                    "meaning": "作者称可被称为爱者必然无条件，并把“无条件”落到“爱人者所需的回报不由被爱者支付”这一点上。",
                    "evidence": "P001、P005、P006",
                    "ambiguity": "作者未给出“爱”的完整定义，只称“这是爱的定义决定的”。",
                },
                {
                    "term": "这个存在 / 一种外部的、不需要回报的存在",
                    "meaning": "作者用以指路线B中代替被爱者支付回报的外部存在，作者未在正文中点名。",
                    "evidence": "P005、P006",
                    "ambiguity": "该存在的具体所指（是否指神）本文未明说，不能代为补足。",
                },
                {
                    "term": "债务 / 放债行为",
                    "meaning": "作者称当外部存在被否决时，爱人者会把大笔“债务”记到被爱者身上，使“爱”变成强买强卖的放债行为。",
                    "evidence": "P006",
                    "ambiguity": "“债务”是比喻还是实际的心理/伦理机制，作者未展开。",
                },
                {
                    "term": "正反馈",
                    "meaning": "作者列举的人类所需之一，与生存、收获、安全并列。",
                    "evidence": "P002",
                    "ambiguity": "未给出定义。",
                },
            ],
            "examples_and_targets": [
                "“无法永生、无法超越自然规律、无法摆脱自身局限”的人类处境（作者的前提陈述，P002）。",
                "“需要生存、需要收获、需要安全、需要正反馈等等等等所得”（作者列举，P002）。",
                "A、B 两条路线的列举（作者的分类，P004、P005）。",
                "“强买强卖的放债行为”（作者对失去外部支付者后之“爱”的比喻，P006）。",
            ],
            "conditions": [
                "“如果要可持续”为作者推演两条路线的条件（P003）。",
                "“如果否决掉这个存在”为 P006 反面推论的条件（P006）。",
                "“在完全不需要任何回报的存在身上”为路线A的限定（P004）。",
                "“爱人的人所需要的，不由被爱的人支付，而是由这个存在支付”为路线B成立的机制条件（P005）。",
                "作者以“从逻辑上说”标明该推演为逻辑推论而非经验断言（P003）。",
            ],
            "rhetoric_and_tone": "简洁的推演体，采用 A/B 分条列举与“如果……那么……”的条件句式；关键处给“爱”“债务”“爱”加引号，暗示这些词在此语境下已被扭曲；末句“强买强卖的放债行为”带批判性比喻色彩；全文未点名任何宗教或人物，语气冷静、抽象。",
            "unresolved_questions": [
                "路线B中“一种外部的、不需要回报的存在”具体所指为何，本文未明说（未出现“神”“上帝”等词）。",
                "“爱的定义”本身在正文中未给出，作者称其决定“爱必然无条件”。",
                "两条路线是否穷尽所有可能，作者以“只有两种可行的路线”断言但未论证排他性。",
                "“债务”机制是心理性的还是伦理性的，本文未说明。",
                "brief 首句与 P001 相同、其余为正文并合，无法判定 brief 是否为作者原话的独立片段。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "可以被称为爱的，必然是无条件的。这是爱的定义决定的。", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "而人类作为一种无法永生、无法超越自然规律、同时也无法摆脱自身局限的存在，需要生存、需要收获、需要安全、需要正反馈等等等等所得。", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P003", "quote": "所以爱从逻辑上说，如果要可持续，就只有两种可行的路线：", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P004", "quote": "A. 在完全不需要任何回报的存在身上存在。", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P005", "quote": "B. 由一种外部的、不需要回报的存在帮助人类成全。", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P006", "quote": "如果否决掉这个存在，那么毫无所求的爱也就一同幻灭了。", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P006", "quote": "“爱”就成了一种强买强卖的放债行为了。", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["伦理学", "情感哲学", "宗教哲学"],
            "issue_candidates": ["无条件的爱是否可能", "爱的可持续性与回报", "爱的债务化"],
            "text_function_candidates": ["答疑", "逻辑推演", "概念辨析"],
            "object_candidates": ["人类", "爱人的人", "被爱的人", "完全不需要任何回报的存在", "外部的、不需要回报的存在"],
            "working_keywords": ["无条件的爱", "回报", "可持续", "债务", "放债", "正反馈"],
        },
        "notes": "无图片节点。本篇 text 与 lexical 无差异（divergence=false）。作者未点名“外部的、不需要回报的存在”为何，记录中不作补足。",
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
