# -*- coding: utf-8 -*-
"""批次 r001-b0030 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0030.sessions.py            # 写 out/r001-b0030.out.jsonl
  python3 records/r001-b0030.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0030"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0030.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f3283eb3": {
  "analysis": {
   "question_context": "提问者问「当孩子受到欺凌时，是否选择反抗？」（Q001，属提问者）。作者把问题转成「孩子受了欺凌，父母应该如何教导」，明确反对很多人主张的教孩子「打回去」，先列三条反对理由，再提出自己的总体策略：不靠个人武力而靠团体／公共服务能力，家长应引导子女以提供价值与公共服务获得安全与影响力。正文末尾标注「（未完，待续）」。",
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
     "summary": "引入与立论：作者把问题转为父母应如何教导；指出很多人主张教孩子「打回去」，并断言这绝对是错的。",
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
     "summary": "错误点1：可能造成确实人身伤害与严重法律后果（可检出伤害处置极严、可能被击毙、可能坐牢、四厘米累计伤口即轻伤标准），并反驳「未成年人打死人都没罪」的读者纠正。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P010",
      "P011",
      "P012"
     ],
     "summary": "错误点2：后续争议中家长兜底与否都失败——胜则造出新霸主甚至霸王，败则失信于子女；决策树所有分支都指向最终失败；并预先反驳「我表弟不是这样」的举例。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P013",
      "P014",
      "P015",
      "P016",
      "P017",
      "P018"
     ],
     "summary": "错误点3：子女会被贴上暴力倾向者标签，被同学家长回避而孤立；即使场面上赢了却要转学，也难说是赢。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P019",
      "P020",
      "P021"
     ],
     "summary": "小结：只管打回去的处理肯定是错的；它在几十年前治安散养、法度不严的时代曾经正确，但在遍地监控、社会安定、法度严密的时代再教就是送子女入火坑。",
     "role": "conclusion"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P022",
      "P023",
      "P024",
      "P025",
      "P026",
      "P027",
      "P028",
      "P029",
      "P030",
      "P031",
      "P032"
     ],
     "summary": "总体策略的起点：霸凌者的第一要害是欺软怕硬，其残酷常是从欺凌他自己的霸凌者处学来；因此要让「你在安全榜上不能垫底」，有两条路线——有团体分担威胁，或自身武力更强；「打回去」只能占第二条。",
     "role": "reason"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P033",
      "P034",
      "P035",
      "P036",
      "P037",
      "P038",
      "P039",
      "P040"
     ],
     "summary": "论证应走第一条路：霸凌者常拉帮结伙、仗势欺人，个人武力胜不过团伙；且霸凌者愚蠢，可能先干掉最难搞定的「立威」；明确存在一个愿同生共死的团体（哪怕两三人）就足以让对方三思。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P041",
      "P042",
      "P043",
      "P044",
      "P045"
     ],
     "summary": "可行性的来源：凡有霸凌处就有抱团抵抗的迫切需求，同被欺凌者的彻骨仇恨驱动力胜过霸凌快感，这是天定规律；但作者也指出这常常是一个新的霸凌团体的崛起过程。",
     "role": "claim"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P046",
      "P047",
      "P048",
      "P049",
      "P050",
      "P051",
      "P052",
      "P053",
      "P054"
     ],
     "summary": "反面后果：家长若不有效作为，孤立的子女几乎必然走进三条路——彻底懦弱并形成对暴力的崇拜情结、打了回去而埋下对暴力的信任、趋炎附势入帮派。",
     "role": "reason"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P055",
      "P056",
      "P057",
      "P058"
     ],
     "summary": "唯一正道：家长自己对正义的力量有认知、对正义的技术有造诣，引导孩子以有效信念与深思熟虑的策略获取对霸凌者及其团体的优势；这也是培养未来领袖的最好的家庭教育。",
     "role": "conclusion"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P059",
      "P060",
      "P061",
      "P062",
      "P063",
      "P064",
      "P065"
     ],
     "summary": "具体做法第一：要有可输出的价值，拥有提供价值的能力，才能有基本社会地位、成为局中人；家长可考虑为子女提供一定支持（除非环境有明确禁令）。",
     "role": "action_advice"
    },
    {
     "unit_id": "U012",
     "paragraph_refs": [
      "P066",
      "P067",
      "P068",
      "P069",
      "P070",
      "P071",
      "P072",
      "P073",
      "P074",
      "P075",
      "P076",
      "P077",
      "P078",
      "P079",
      "P080",
      "P081",
      "P082",
      "P083",
      "P084",
      "P085",
      "P086",
      "P087",
      "P088"
     ],
     "summary": "具体做法第二：有计划、有策略地把自己的优势转换成某种公共服务（补习小组、球队、画贺卡、请喝汽水等）；这样做是无条件的、不是投机；真正有力的是「我要有能力，我还要以这个能力对周围发生建设性的影响」这一价值观。",
     "role": "action_advice"
    },
    {
     "unit_id": "U013",
     "paragraph_refs": [
      "P089",
      "P090",
      "P091",
      "P092",
      "P093",
      "P094",
      "P095",
      "P096",
      "P097"
     ],
     "summary": "反霸凌的根基：提供基础公共服务者是天然避风港（如医生护士不受随意攻击），并会经由拒绝提供服务的能力获得客观、天然不可剥夺的权力；服务越关键，豁免越有力。",
     "role": "reason"
    },
    {
     "unit_id": "U014",
     "paragraph_refs": [
      "P098",
      "P099",
      "P100",
      "P101",
      "P102"
     ],
     "summary": "对能力不足者的回应：能提供的关键公共服务总是有的，只需转变想法——不是只有造冰激凌的人才在提供冰激凌服务；找到提供价值的角度就能获得社群权力与安全。（未完，待续）",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "（作者所反对的流行主张）有很多人主张教受欺凌的孩子「打回去」。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "教孩子「打回去」绝对是错的。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "如果造成确实的人身伤害，将造成非常严重的麻烦：现代法治社会对可检出的人身伤害处置极其严重；养成这样的行事习惯，将来随时可能坐牢。",
     "evidence": [
      "E3",
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "（被作者反驳的读者观点）有读者以「未成年人打死人都没罪」来纠正作者。",
     "evidence": [
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "家长兜底与否都会失败：兜底成功就创造出一个新霸主（甚至霸王项羽），拒绝兜底则失去信用；这种剧情发展下去，决策树上所有的分支都指向最终失败。",
     "evidence": [
      "E6",
      "E7"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "「我表弟不是这样」式的举例不构成反驳，因为那是有别的事情教育了他，摸电门也有幸存者，这与守则无关。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "教孩子打回去会让子女被贴上暴力倾向者的标签，其他家长会避免子女与其交往。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "「只管打回去」的处理肯定是错的；这种处理曾经正确过，但那是在好几十年前治安近乎半散养的时代。",
     "evidence": [
      "E10",
      "E11"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "在遍地监控、社会安定、法度严密、警力可以聚焦在少数伤害案件的时代，再教「直接武力反击侵犯」就是送子女入火坑。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "霸凌者的第一个要害是势必欺软怕硬；其对弱者的残酷常常是从欺凌他自己的霸凌者身上学来的。",
     "evidence": [
      "E13",
      "E14"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要让「你在安全榜上不能垫底」：要么有团体愿意为你共同对抗暴力侵扰，要么自身武力比其他人更强。",
     "evidence": [
      "E15"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "「打回去」之所以常被认为有效，是因为它占住了第二条（自身武力）路线；但真正切实可行、应行的是第一条路（团体）。",
     "evidence": [
      "E16",
      "E17"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "第二条路只能带来非常有限的安全：霸凌者常拉帮结伙，个人武力再强也胜不过一个团伙；且他们并不总能正确评估武力排行，可能先挑最难搞定的来「立威」。",
     "evidence": [
      "E18",
      "E19"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "明确存在一个团体愿与你同生共死，哪怕只有两三个人，也已经很足够让对方三思。",
     "evidence": [
      "E20"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "但凡存在霸凌的地方，也就存在欲抱团抵抗霸凌的极其迫切的需求与有所作为之机；同被欺凌者对霸凌者的仇恨驱动力要远远胜过霸凌的快感对霸凌者的驱动力。",
     "evidence": [
      "E21",
      "E22"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "（作者同时指出的代价）这种抱团抵抗常常是一个新的霸凌团体的崛起过程。",
     "evidence": [
      "E23"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "predicted",
     "statement": "家长若不有效作为，孤立的子女几乎必然走进三条路中的一条：彻底懦弱并对暴力既愤恨又崇拜、打了回去而埋下对暴力的信任、趋炎附势入帮派。",
     "evidence": [
      "E24",
      "E25"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "唯一在逻辑上有长期正效应的策略（也是唯一正道）是：家长自己对正义的力量有认知、对正义的技术有造诣，引导孩子凭有效的信念和深思熟虑的策略去获取对霸凌者及其团体的优势。",
     "evidence": [
      "E26",
      "E27"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "这是培养未来的领袖的最好的家庭教育：能做好孩子王、或学会识别与连结孩子王，是子女将来安身立命最决定性的保障。",
     "evidence": [
      "E28"
     ]
    },
    {
     "claim_id": "C020",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "第一，一切的关键是你要有可输出的价值：人天然有责任拥有提供价值的能力。",
     "evidence": [
      "E29",
      "E30"
     ]
    },
    {
     "claim_id": "C021",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为家长可以考虑自己为子女提供一定支持（这也许不够政治正确，但切实可行），除非子女所处环境有明确禁令禁止这种支持。",
     "evidence": [
      "E31"
     ]
    },
    {
     "claim_id": "C022",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "第二，你要有计划、有策略的将自己的优势转换成某种公共服务。",
     "evidence": [
      "E32"
     ]
    },
    {
     "claim_id": "C023",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "这样做是无条件的，不是为了「打造不被欺负的基础」而做的投机行为，而只是一个人应该要做的事、应该有的行为模式。",
     "evidence": [
      "E33",
      "E34"
     ]
    },
    {
     "claim_id": "C024",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "真正有力的是最根本的价值观——「我要有能力，我还要以这个能力对周围发生建设性的影响」，而不是那些机巧、策略。",
     "evidence": [
      "E35"
     ]
    },
    {
     "claim_id": "C025",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "在最低的层面，任何一个社会团体都会避免攻击基础公共服务的提供者；参与提供公共福利的位置就是天然的避风港（例如再残暴的恶棍也不会随便屠杀医生护士）。",
     "evidence": [
      "E36",
      "E37"
     ]
    },
    {
     "claim_id": "C026",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作为某种服务的主要提供者，你会经由拒绝提供服务的能力拥有一种客观的、天然不可剥夺的权力。",
     "evidence": [
      "E38"
     ]
    },
    {
     "claim_id": "C027",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "提供公共服务者享有豁免，而且享有主动权；提供的服务越关键，豁免越有力，主动权越大。",
     "evidence": [
      "E39"
     ]
    },
    {
     "claim_id": "C028",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "「没有能力提供关键公共服务」的想法是错的——你能提供的关键公共服务总是有的，只需转变几点想法：不是只有制造冰激凌的人才在提供冰激凌这种服务。",
     "evidence": [
      "E40",
      "E41"
     ]
    }
   ],
   "argument_steps": [
    "把提问转为父母应如何教导，并点名反对「打回去」（P002-P004）",
    "反对理由1：人身伤害与法律后果（P006），并预先反驳「未成年人打死人都没罪」（P007-P008）",
    "反对理由2：兜底与否皆败的决策树推演（P010-P011），并预先反驳个案举例（P012）",
    "反对理由3：暴力标签导致社交孤立与转学困境（P013-P018）",
    "小结：处理肯定是错的，它只在几十年前的治安条件下正确（P019-P021）",
    "转入总体策略，从霸凌者的天然缺陷（欺软怕硬）说起（P022-P027）",
    "给出两条路线并指出「打回去」只占第二条（P028-P032）",
    "论证第一条路更可行：霸凌者结伙、且愚蠢、可能立威（P033-P038）",
    "指出团体抵抗的现实基础：被欺凌者的仇恨驱动力更强（P041-P044），同时提示其可能演变为新的霸凌团体（P045）",
    "列出家长不作为时子女的三条路（P046-P054）",
    "给出唯一正道：家长对正义的力量与技术有造诣并引导孩子（P055-P058）",
    "展开做法一：拥有可输出的价值，家长可给予支持（P059-P065）",
    "展开做法二：把优势转换成公共服务，且这是无条件的（P066-P088）",
    "解释为何要讲这套「理想主义」：公共服务提供者是天然避风港并拥有客观权力（P089-P097）",
    "回应「能力不足」的疑虑：关键公共服务总是找得到（P098-P101），文末标注未完待续（P102）"
   ],
   "concept_usage": [
    {
     "term": "打回去／只管打回去",
     "meaning": "教孩子在受欺凌时直接以武力反击的做法；作者明确反对，但承认它在几十年前曾经正确。",
     "evidence": "P004",
     "ambiguity": "作者未区分不同程度、不同场景的武力反击。"
    },
    {
     "term": "安全榜",
     "meaning": "霸凌者挑选对象时按「是否好下手」形成的隐性排序；作者主张不能垫底。",
     "evidence": "P028",
     "ambiguity": "作者自创的比喻说法，无客观量表。"
    },
    {
     "term": "立威",
     "meaning": "霸凌者先对最难搞定的目标下手以建立威势的策略。",
     "evidence": "P036",
     "ambiguity": "无。"
    },
    {
     "term": "同生共死",
     "meaning": "作者对理想互助团体的描述：明确存在愿意共同承担威胁的团体。",
     "evidence": "P039",
     "ambiguity": "未说明如何在校园环境中形成或维持。"
    },
    {
     "term": "可输出的价值",
     "meaning": "能够为他人提供利益、有利于他人生存与实现理想的能力；作者视为社会地位的基础。",
     "evidence": "P060",
     "ambiguity": "未给具体能力清单。"
    },
    {
     "term": "公共服务",
     "meaning": "本文中指把个人优势转换为无差别惠及他人的服务（补习小组、球队、请喝汽水等）。",
     "evidence": "P066",
     "ambiguity": "与公共部门提供的公共服务不同，属作者借用的宽泛说法。"
    },
    {
     "term": "豁免／客观的、天然不可剥夺的权力",
     "meaning": "服务提供者因可拒绝供应而获得的保护与影响力。",
     "evidence": "P093",
     "ambiguity": "作者以「组织行为学规律」「绝对命令」等表述支撑，未给出处。"
    },
    {
     "term": "唯一正道",
     "meaning": "作者对「家长引导子女以策略获取对霸凌者的优势」这一路线的定位。",
     "evidence": "P056",
     "ambiguity": "排他性断言，未讨论其他可能有效的做法。"
    }
   ],
   "examples_and_targets": [
    "「四厘米伤口」「累计四厘米」「人体轻伤鉴定标准」「三年以下有期徒刑」（作者的法律论据，需外部核查）",
    "「我的爸爸是李刚」（网络流行语，作者用作骄纵后果的例证）",
    "霸王项羽（作者类比新霸主的结局）",
    "「我表弟不是这样」（作者预设并反驳的读者举例方式）",
    "「摸电门也有幸存者」（作者类比，说明个案幸存不构成反驳）",
    "「远犯强汉者」（作者戏仿古语，用于描述过度敏感者的处境）",
    "罗密欧朱丽叶式的大彻大悟、地藏菩萨般的耐心（修辞材料）",
    "「再残暴的恶棍，也不会随便屠杀医生护士」（作者例证公共服务提供者的避风港地位）",
    "造冰激凌车的人、冰激凌车的司机（作者例证「人人可提供进一步的服务」）",
    "同学家长、转学、无人区的正中间（作者对孤立后果的描绘）"
   ],
   "conditions": [
    "如果造成确实的人身伤害（P006 的条件）",
    "如果对方有心算无心（P008 的假设）",
    "如果你的孩子动手打了人，你去撑腰且成功避免了惩罚（P010 的假设）",
    "在某一次他动手之后拒绝给他兜底（P010 的假设）",
    "除非你上小学时就血盆大口、肌肉虬结、面带金印（P037 的调侃式限定）",
    "除非另有奇缘相解（P049 的限定）",
    "除非你子女所处的环境有某种明确的禁令禁止父母提供这种支持（P065 的限定）",
    "无论是不是被承认、被奖励、「得不偿失」、「值得」（P079 的无条件列举）",
    "只有历尽沧桑的成人在某种运气赐予的际遇下才能领有（P054 对「正义属性」的条件限定）"
   ],
   "rhetoric_and_tone": "家长教育训诫体，第二人称「你」直接对家长说话；大量反问（「你晚上睡不睡得着觉」「情何以堪？」「你打算要怎么跟他解释？」）与冷峻的后果推演（决策树、三条路）；夹杂俚俗与贬语（「这小崽子」「打遍天下无敌手」「你是混蛋」）；用「天定的规律」「唯一正道」「绝对命令」等绝对化措辞；结尾段落转为近乎信仰宣言式的格言体（「因为有我，这事可望会变好一点」）。整体为「先破后立」的长篇论说，末段标注未完待续。",
   "unresolved_questions": [
    "正文末尾为「（未完，待续）」，本篇未完结，后续内容不在本记录中。",
    "法律细节（故意伤害罪硬标准、人体轻伤鉴定标准、累计四厘米、三年以下有期徒刑）属作者论据，需外部核查，尤其「累计四厘米」的表述需核实其与鉴定标准的对应关系。",
    "「未成年人打死人都没罪」是作者转述的读者意见，原文不在本记录中，不得当作读者原话引用。",
    "「罗密欧朱丽叶式的大彻大悟」等比喻未展开，含义不完全确定。",
    "「组织行为学规律」「绝对命令」等表述无出处，作者未引任何研究或文献。",
    "本文未区分校园霸凌的不同类型（肢体、言语、关系、网络），亦未讨论学校/教师角色与制度性救济途径。",
    "家长为子女提供支持（P065）与「无条件提供公共服务」（P072-P074）之间的张力，作者未展开说明。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P003",
     "quote": "我看到有很多人主张教孩子“打回去”。",
     "relation": "context"
    },
    {
     "key": "E2",
     "paragraph_id": "P004",
     "quote": "这个绝对是错的。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P006",
     "quote": "现代法治社会对于可检出的人身伤害处置极其严重",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P006",
     "quote": "养成这样的行事习惯，将来随时可能坐牢",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P007",
     "quote": "很多阅读能力有缺陷的人跑来纠正我未成年人打死人都没罪",
     "relation": "contradicts"
    },
    {
     "key": "E6",
     "paragraph_id": "P010",
     "quote": "那么你自己就创造出了一个新霸主",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P011",
     "quote": "决策树上所有的分支都指向最终失败",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P012",
     "quote": "摸电门也有幸存者，这跟“不能摸电门”的守则无关。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P014",
     "quote": "所有的同学家长知道这事之后都会考虑避免子女再跟你的子女交往",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P019",
     "quote": "所以，那类“只管打回去”的处理肯定是错的。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P020",
     "quote": "这种处理曾经正确过——但那是在好几十年前。",
     "relation": "qualifies"
    },
    {
     "key": "E12",
     "paragraph_id": "P021",
     "quote": "再教这种“直接武力反击侵犯”就是送子女入火坑了",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P025",
     "quote": "第一个要害——霸凌者势必欺软怕硬。",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P026",
     "quote": "霸凌者对弱者的残酷，常常是从欺凌他自己的霸凌者身上学来的",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P028",
     "quote": "你需要某种原因使得你在安全榜上不能垫底",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P032",
     "quote": "因为“打回去”可以占住第二条。",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P033",
     "quote": "但是事实上，真正切实可行的、应行的，是第一条路。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P035",
     "quote": "你个人的武力再强，也胜不过一个哪怕很小的团伙",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P036",
     "quote": "在自信能搞得定的目标对象中，先干掉那个最难搞定的来“立威”",
     "relation": "supports"
    },
    {
     "key": "E20",
     "paragraph_id": "P039",
     "quote": "而明确的存在一个团体愿与你同生共死，哪怕只有两三个人，也已经很足够让对方三思了。",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P041",
     "quote": "但凡存在霸凌的地方，也就存在欲抱团抵抗霸凌的极其迫切的需求",
     "relation": "supports"
    },
    {
     "key": "E22",
     "paragraph_id": "P042",
     "quote": "这种对霸凌者的仇恨的驱动力，要远远胜过霸凌的快感对霸凌者的驱动力。",
     "relation": "supports"
    },
    {
     "key": "E23",
     "paragraph_id": "P045",
     "quote": "讽刺的是，这常常是一个新的霸凌团体的崛起过程。",
     "relation": "qualifies"
    },
    {
     "key": "E24",
     "paragraph_id": "P046",
     "quote": "你如果不有效作为，则孤立的子女几乎必然走进这三条路中的一条",
     "relation": "supports"
    },
    {
     "key": "E25",
     "paragraph_id": "P051",
     "quote": "第三条路——趋炎附势，以逢迎贿赂换取强者的保护。",
     "relation": "supports"
    },
    {
     "key": "E26",
     "paragraph_id": "P055",
     "quote": "就是你自己对正义的力量有认知，对正义的技术有造诣",
     "relation": "supports"
    },
    {
     "key": "E27",
     "paragraph_id": "P056",
     "quote": "这是唯一在逻辑上有长期正效应的策略。也是唯一正道。",
     "relation": "supports"
    },
    {
     "key": "E28",
     "paragraph_id": "P057",
     "quote": "这是培养未来的领袖的最好的家庭教育",
     "relation": "supports"
    },
    {
     "key": "E29",
     "paragraph_id": "P060",
     "quote": "第一，一切的关键，你要有可输出的价值。",
     "relation": "supports"
    },
    {
     "key": "E30",
     "paragraph_id": "P061",
     "quote": "要拥有提供价值的能力，要有利于他人生存的能力，利于他人实现自己理想的能力",
     "relation": "supports"
    },
    {
     "key": "E31",
     "paragraph_id": "P065",
     "quote": "除非你子女所处的环境有某种明确的禁令禁止父母提供这种支持。",
     "relation": "qualifies"
    },
    {
     "key": "E32",
     "paragraph_id": "P066",
     "quote": "第二，你要有计划、有策略的将自己的优势转换成某种公共服务。",
     "relation": "supports"
    },
    {
     "key": "E33",
     "paragraph_id": "P072",
     "quote": "这样做是无条件的。",
     "relation": "supports"
    },
    {
     "key": "E34",
     "paragraph_id": "P074",
     "quote": "这不是为了“打造不被欺负的基础”而做的投机行为",
     "relation": "supports"
    },
    {
     "key": "E35",
     "paragraph_id": "P083",
     "quote": "真正有力的是这个最根本的价值观——“我要有能力，我还要以这个能力对周围发生建设性的影响。”",
     "relation": "supports"
    },
    {
     "key": "E36",
     "paragraph_id": "P090",
     "quote": "任何一个社会团体都会避免攻击基础公共服务的提供者",
     "relation": "supports"
    },
    {
     "key": "E37",
     "paragraph_id": "P091",
     "quote": "再残暴的恶棍，也不会随便屠杀医生护士",
     "relation": "supports"
    },
    {
     "key": "E38",
     "paragraph_id": "P093",
     "quote": "你自然会经由拒绝提供服务的能力拥有一种客观的、天然不可剥夺的权力。",
     "relation": "supports"
    },
    {
     "key": "E39",
     "paragraph_id": "P097",
     "quote": "提供公共服务者享有豁免，而且享有主动权。提供的服务越关键，豁免越有力，主动权越大。",
     "relation": "supports"
    },
    {
     "key": "E40",
     "paragraph_id": "P099",
     "quote": "其实你错了，你能提供的关键公共服务总是有的。",
     "relation": "supports"
    },
    {
     "key": "E41",
     "paragraph_id": "P101",
     "quote": "并不是只有制造冰激凌的人才在提供冰激凌这种服务",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "家庭教育",
    "校园霸凌",
    "社会策略",
    "组织行为"
   ],
   "issue_candidates": [
    "孩子受欺凌是否反抗",
    "以团体对抗霸凌",
    "家长的角色",
    "公共服务与安全感"
   ],
   "text_function_candidates": [
    "答疑",
    "训诫",
    "策略建议",
    "长篇论说"
   ],
   "object_candidates": [
    "受欺凌儿童",
    "家长",
    "霸凌者及其团体",
    "同学家长",
    "学校"
   ],
   "working_keywords": [
    "打回去",
    "安全榜",
    "立威",
    "同生共死",
    "可输出的价值",
    "公共服务",
    "豁免",
    "唯一正道"
   ]
  },
  "notes": "正文无图片节点。正文末尾为「（未完，待续）」，本篇不完整，后续论证（如何提供进一步的服务等）不在本记录内。文中「未成年人打死人都没罪」为作者转述的读者意见（对手观点），已按 opponent_view 登记。法律细节与「组织行为学规律」「绝对命令」等表述均需外部核查。"
 },
 "f9472f2a": {
  "analysis": {
   "question_context": "提问者问「我妹妹画这种画怎么办？」（Q001，属提问者）。作者没有直接给出处理办法，而是先批评该问题下「没事」「是好事」「要珍惜艺术天才」的多数回答（认为这些人是借题发挥、群体狂欢、不必负责），再面向父母列出三个问题：发现太晚暴露信息掌握机制缺陷、孩子可能借惊人行为博关注、孩子可能对父母有报复心，并以「这些话是写给父母看的」收束。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "对多数回答的批评：把「没事」「是好事不是坏事」「要珍惜艺术天才」一类观点归为借题发挥、群体狂欢、不需为任何事情负责。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006",
      "P007",
      "P008",
      "P009"
     ],
     "summary": "第一点：对应该引起人类恶心反感的东西无感甚至迷恋，本身的确是心理变态的征兆；人类的反感本能是演化淘汰的结果（不回避者基本死绝）。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P010",
      "P011",
      "P012",
      "P013"
     ],
     "summary": "第二点：对引起家人严重反应的事务淡定自若的继续，是反社会人格的迹象；需要深切的诊断和干预，但诊断结果要改变的未必是当事人本身，而可能是家人。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P014",
      "P015"
     ],
     "summary": "反驳以「恐怖的艺术」「创作自由」为之辩解者：想做这种艺术家可以自己去走，不要把自己的需要投射到别人身上；被监护人走什么路由监护人决定；市场成功不等于正当性（海洛因、芬太尼、大麻之例）。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P016",
      "P017",
      "P018",
      "P019"
     ],
     "summary": "回答提问（「答案是的确有问题」）：第一大问题——到现在这种程度才发现，说明对受监护人的信息掌握存在机制性缺陷；父母面对的是不可能百分百完成的任务，只能尽人事、安天命。",
     "role": "claim"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P020",
      "P021",
      "P022",
      "P023"
     ],
     "summary": "第二大问题：孩子可能缺少社会地位，想借小众的惊人行为博取关注；关注即存在的证据，失去关注如同死亡，这是永远填不满的毒瘾；人应有别的价值依托。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P024",
      "P025",
      "P026",
      "P027",
      "P028"
     ],
     "summary": "第三大问题：孩子可能对父母有报复心，父母的痛苦反而构成奖励与行为动力；原因可能是子女价值观体系判定父母有罪，也可能是父母自己确有错；无论如何值得花心思寻找，责任终究在父母。",
     "role": "claim"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P029",
      "P030"
     ],
     "summary": "收束：这些话不是写给小孩看的，是写给父母看的；告诫在评论区狂欢者「你们根本不知道自己在说什么」。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "（作者所批评的多数回答）这里大多数的观点都是「好好」「没事」「没关系」「一点毛病没有」「是好事不是坏事」「要珍惜艺术天才」。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "对应该引起人类恶心和反感的东西无感甚至迷恋，本身的确是心理变态的征兆。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人类对粘液、腐烂物、病变皮肤、畸形的本能反感是演化淘汰的结果：在这几百万年里不本能反感而回避的基本都死绝了。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "对会引起家人严重反应的事务淡定自若的继续，是反社会人格的迹象；无论家人因何恐惧、也无论这恐惧是否合理，正常的人都会有所顾虑、有所纠结。",
     "evidence": [
      "E4",
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "是不是有问题、是什么问题、要如何纠正，需要进一步查探；但当事人需要深切的诊断和干预是毋庸置疑的——只不过诊断结果要改变的未必是当事人本身，也可能是家人。",
     "evidence": [
      "E6",
      "E7"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "想走「恐怖的艺术」路线、用艺术性为之辩解并争取「创作自由」的人，尽可以自己去走这条路，不要把自己的需要投射到别人身上。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "被监护人走什么路，监护人才有权决定；除非监护人做了法律不允许的行为，否则没人有资格依据自己的喜好和价值观去压倒监护人的价值观。",
     "evidence": [
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "不要因为日本或西方有且昌盛就当成好东西：能取得「市场成功」广受欢迎并不意味着这东西就有理所当然的正当性。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "到如今这种程度才发现，意味着在受监护人的信息掌握上存在机制性的缺陷——现代小孩大部分时间在父母视线之外活动，这对没有受过专业训练的父母是非常困难的挑战。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "父母面对的是一个不可能百分百完成的任务，方法都要求近乎专业的能力，所以只能尽人事、安天命。",
     "evidence": [
      "E13",
      "E14"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "第二大问题：这孩子可能缺少社会地位，所以可能想要借小众的惊人行为博取关注。",
     "evidence": [
      "E15"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "靠外部关注确认存在是一条非常危险的路：关注即为存在的证据，失去关注如同死亡，这是永远填不满的毒瘾、没有回头路，将来总会有人借关注的施舍操控其人生。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人不应该去追求这种关注，而应该有别的价值依托；即使默默无闻也不会动摇的幸福才是真实的幸福。",
     "evidence": [
      "E17"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "第三个问题：孩子可能对父母有报复心，因而父母的痛苦不但不对她构成负担，反而构成一种奖励、成为一种行为的动力。",
     "evidence": [
      "E18"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "报复心的成因可能是子女的价值观体系判定父母有罪（于是折磨只是正常惩罚），也可能是父母自己确有错、超出了子女能谅解的限度；无论怎样都存在值得花心思寻找的问题。",
     "evidence": [
      "E19",
      "E20"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "这些话根本不是写给孩子看的，是写给父母看的；在评论区狂欢的人根本不知道自己在说什么。",
     "evidence": [
      "E21",
      "E22"
     ]
    }
   ],
   "argument_steps": [
    "先指认并批评该问题下的多数回答（P001-P003）",
    "给出第一点判断：对恶心反感之物无感甚至迷恋是心理变态的征兆（P005）",
    "以演化淘汰为理由支持该判断（P008），并以「炫耀尝不到味道、看不见东西」类比贬斥（P009）",
    "给出第二点判断：对家人严重反应无动于衷地继续是反社会人格的迹象（P010-P011）",
    "限定：需进一步查探问题性质，但干预必要；且要改变的未必是当事人（P012-P013）",
    "反驳「恐怖艺术/创作自由」的辩护，并确立监护人决定权（P014）",
    "以市场成功不等于正当性反驳「日本/西方有且昌盛」（P015）",
    "明确回答：的确有问题（P016）",
    "展开第一大问题：发现太晚说明信息掌握机制缺陷，父母只能尽人事安天命（P017-P019）",
    "展开第二大问题：可能因缺社会地位而借惊人行为博关注，关注成瘾极危险（P020-P023）",
    "展开第三大问题：可能对父母有报复心，父母痛苦反成奖励（P024-P028）",
    "收束：本文写给父母，不是写给评论区的小孩（P029-P030）"
   ],
   "concept_usage": [
    {
     "term": "心理变态的征兆",
     "meaning": "作者对「对恶心反感之物无感甚至迷恋」的判断用语。",
     "evidence": "P005",
     "ambiguity": "非临床诊断用语，作者未引诊断标准。"
    },
    {
     "term": "反社会人格",
     "meaning": "作者对「对家人严重反应淡定自若地继续」的判断用语。",
     "evidence": "P010",
     "ambiguity": "同样非临床诊断，且作者随后说需进一步查探。"
    },
    {
     "term": "社会化过程",
     "meaning": "个体习得社会规范的过程；作者称直接继续是「社会化过程有重大缺陷的表征」。",
     "evidence": "P011",
     "ambiguity": "无。"
    },
    {
     "term": "监护人／被监护人",
     "meaning": "作者据以分配决定权的法律—伦理角色：走什么路由监护人决定。",
     "evidence": "P014",
     "ambiguity": "作者未讨论被监护人自身意愿的权重与年龄界限。"
    },
    {
     "term": "市场成功",
     "meaning": "广受欢迎、有商业成绩；作者主张它不构成正当性。",
     "evidence": "P015",
     "ambiguity": "无。"
    },
    {
     "term": "关注即为存在的证据",
     "meaning": "作者对「以外部关注确认自身存在」这一现代心态的概括。",
     "evidence": "P021",
     "ambiguity": "属作者论断，未给出经验依据。"
    },
    {
     "term": "尽人事，安天命",
     "meaning": "作者给父母的行动限度：努力但仍须承认成功不由人力决定。",
     "evidence": "P019",
     "ambiguity": "无。"
    },
    {
     "term": "恶之花",
     "meaning": "标题用词，正文 P021 以「无数的恶之花是从这条藤上结出来的」出现，指由博取关注这条路径结出的恶果。",
     "evidence": "P021",
     "ambiguity": "未给出严格定义，带文学/象征色彩。"
    }
   ],
   "examples_and_targets": [
    "「腐烂的尸体、溃败的皮肤、支离破碎的残肢、蛆虫、粘液、畸形」（作者列举的触发反感之物）",
    "「这就像在炫耀自己尝不到味道、看不见东西」（作者类比）",
    "海洛因、芬太尼（作者类比，说明广受欢迎不等于正当）",
    "加拿大和荷兰合法种大麻、「农学家幼苗」（作者类比，反驳以「国外合法」为据的辩护）",
    "想走「恐怖的艺术」路线、争取「创作自由」的评论者（作者的批评对象）",
    "「这位作者」（P012，指涉画画的当事人，具体指代见未决问题）",
    "评论区「小孩子们」（作者的训斥对象）"
   ],
   "conditions": [
    "无论家人因为什么感到恐惧万分，也无论你自己觉得这种恐惧是否合理（P011 的让步条件）",
    "除非ta做了什么法律不允许的行为（P014 的限定）",
    "要是出现一个小孩非常痴迷种大麻（P015 的假设）",
    "到了现在这种程度才发现（P017 的前提）",
    "即使默默无闻也不会动摇的幸福才是真实的幸福（P022 的让步）",
    "有可能是……也可能是……（P025 的两种可能）",
    "本文中多处「可能」用于描述孩子的动机，属推测性限定"
   ],
   "rhetoric_and_tone": "训斥与反讽为主：开篇即以反问斥责评论区（「你们是觉得一切都是跟你们有关吧？」「是吗？」）；使用宗教/天命式表述（「上天看在你努力的份上伸手赐予的」「只能祝父母们的努力得到上天的垂怜」）；夹杂「小孩子们别狂欢了」等直接训诫；对「艺术性」「创作自由」「国外合法」等辩护逐一以类比反驳；结尾以对评论者的警告收束。整体语气强硬、道德色彩浓，同情对象明确为父母。",
   "unresolved_questions": [
    "提问中「这种画」的具体内容本文未描述，也未附任何图像（本记录无图片节点）；作者的评价依赖原问题中未被本记录涵盖的材料，需回查原问题及其图片。",
    "P012 的「这位作者」指代不明：可能指画画的当事人（提问者的妹妹），也可能指原问题的提问者；作者未明确。",
    "对当事人「需要深切的诊断和干预」的判断由作者作出，但作者未提供任何专业诊断依据，需谨慎对待（属作者判断，非已证实事实）。",
    "P021「无数的恶之花是从这条藤上结出来的」中的「这条藤」具体所指（博取关注）需结合上下文推断，作者未明确定义。",
    "「日本或者西方有且昌盛的东西」这一表述未指明具体国家政策与作品类型，无法核查。",
    "P016「答案是的确有问题。」在语料中被标为 heading 字段，但它位于正文中段、承担段落功能，属正文/结构不一致，已登记。",
    "P031 为平台话题标签「家族答集」混入正文，非作者论述内容。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "这里大多数的观点都是“好好”“没事”“没关系”“一点毛病没有”“是好事不是坏事”“要珍惜艺术天才”。",
     "relation": "context"
    },
    {
     "key": "E2",
     "paragraph_id": "P005",
     "quote": "对应该引起人类恶心和反感的东西无感甚至迷恋，本身的确是心理变态的征兆。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P008",
     "quote": "看到粘液、腐烂物、病变皮肤、畸形不本能反感而回避的，在这几百万年里基本都死绝了。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P010",
     "quote": "对于会引起家人严重反应的事务淡定自若的继续，这是反社会人格的迹象。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P011",
     "quote": "直接继续是一种非常残忍的行为，也是社会化过程有重大缺陷的表征。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P012",
     "quote": "但这位作者需要深切的诊断和干预是毋庸置疑的。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P013",
     "quote": "只不过诊断的结果要改变的未必是作者本身，而可能是作者的家人罢了。",
     "relation": "qualifies"
    },
    {
     "key": "E8",
     "paragraph_id": "P014",
     "quote": "你们想做这种艺术家尽可以自己去走这条路，不要把自己的需要投射到别人身上。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P014",
     "quote": "被监护人走什么路，监护人才有权决定。",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P014",
     "quote": "否则没人有资格依据自己的喜好和价值观去压倒监护人的价值观",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P015",
     "quote": "能取得“市场成功”广受欢迎并不意味着这东西就有理所当然的正当性",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P017",
     "quote": "意味着在受监护人的信息掌握上存在机制性的缺陷",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P019",
     "quote": "面对的都是一个不可能百分百完成的任务",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P019",
     "quote": "所以只能尽人事，安天命",
     "relation": "qualifies"
    },
    {
     "key": "E15",
     "paragraph_id": "P020",
     "quote": "是这孩子可能缺少社会地位，所以可能想要借小众的惊人行为博取关注",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P021",
     "quote": "关注即为存在的证据，失去关注如同死亡。这是一种永远填不满的毒瘾，没有回头路。",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P022",
     "quote": "人不应该去追求这种关注，而应该有别的价值依托。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P024",
     "quote": "是孩子可能对父母有报复心，因而父母的痛苦不但不对她构成负担，反而构成一种奖励，成为一种行为的动力",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P025",
     "quote": "有可能是子女的价值观体系有问题，根据那个体系，ta们在判定父母有罪",
     "relation": "supports"
    },
    {
     "key": "E20",
     "paragraph_id": "P025",
     "quote": "也可能是父母自己的确有错，超出了子女能谅解的限度",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P029",
     "quote": "小孩子们别狂欢了，这些话根本不是写给你们看的，是写给父母们看的。",
     "relation": "supports"
    },
    {
     "key": "E22",
     "paragraph_id": "P030",
     "quote": "知乎不是只有你们存在，你们根本不知道自己在说什么。",
     "relation": "supports"
    },
    {
     "key": "E23",
     "paragraph_id": "P031",
     "quote": "家族答集",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "家庭教育",
    "青少年心理",
    "艺术与伦理",
    "网络舆论"
   ],
   "issue_candidates": [
    "未成年人创作阴暗题材",
    "监护权与创作自由",
    "以惊人行为博取关注",
    "亲子报复心理"
   ],
   "text_function_candidates": [
    "答疑",
    "批评",
    "训诫",
    "对评论者的回应"
   ],
   "object_candidates": [
    "父母（监护人）",
    "未成年当事人",
    "评论区答主/小孩",
    "日本与西方国家"
   ],
   "working_keywords": [
    "心理变态的征兆",
    "反社会人格",
    "监护人",
    "创作自由",
    "关注成瘾",
    "恶之花",
    "尽人事安天命"
   ]
  },
  "notes": "正文无图片节点，但提问所指的「这种画」内容不在本记录中，需回查原问题及其图片。P016「答案是的确有问题。」被语料标为 heading 字段却位于正文中段，属正文/结构不一致；P031 为平台话题标签「家族答集」混入正文，非作者论述。P012 的「这位作者」指代不明，作者对当事人的心理判断无专业诊断依据，属作者判断。"
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
