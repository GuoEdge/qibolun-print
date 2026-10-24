# -*- coding: utf-8 -*-
"""批次 r001-b0046 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0046.sessions.py            # 写 out/r001-b0046.out.jsonl
  python3 records/r001-b0046.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0046"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0046.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "5103c8f4": {
  "analysis": {
   "question_context": "提问者问：抛开伦理，放弃老人的防疫措施到底有什么损害？（Q001；属提问者，不是作者立场）。作者不回答伦理层面，而是直接改写提问前提：先断言社会实际由五十岁以上的老年精英支配，再据此把“放弃老人”重述为放弃穷人中最弱势的一群，并请读者按这一实质版本考虑立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总起：世界的主宰是五十岁以上的精英集团；任何国家皆然，朝鲜或有小特别，但实际运作仍是一群五十岁以上的老人。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"], "summary": "以年龄刻度比喻精神发育：二十岁近乎只是一团肉，五十岁才是青春期；多数人一辈子未在精神上发育到成人状态。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011"], "summary": "精神成熟与成为精英存在锁定关系，淬炼机会只有精英享有且天生有限，公立教育拉不平，结构性改变提升也有限。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013"], "summary": "结论与反问：真正的主宰必定是已步入老年的老人；反问谁能排除这些真正的主人。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016"], "summary": "重述提问：所谓“放弃老人”实质是放弃进不了专属医院的穷人、穷人中最弱势的一群；立场自便，但要按实质版考虑。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界的主宰是五十岁以上的精英集团，其依据是这一群体掌握的财富规模、政治资源与学术话语权。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为任何国家都是如此，大概只有朝鲜可能有点小特别；但即使在那里，实际掌握运作的仍是一群五十岁以上的老人。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在社会学意义上，二十岁、三十岁、四十岁只是刚睁眼、才有视听觉、刚懂事的阶段，五十岁才算有效的成人。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这是就发育正常者而言；大部分的人一辈子也没有在精神上发育到成人状态。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "发育到成人状态与成为精英存在锁定关系，因为某些特定的发育条件实际上只有精英才享有。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这些淬炼机会注定有限，且只有这些机会才能最有效地把人淬炼成精神上成熟的人；社会并未超出蚁群太多，不能靠公立教育拉平，结构性改变也只能稍微提高成熟者比例。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何社会和文明里，真正的主宰必定是一路过关斩将、步入老年的一般生理意义上的老人。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“放弃老人”，本质上是在放弃没能力去不会放弃老人的专属医院的穷人。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“放弃老人”是在放弃穷人中最好欺负的一群人。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "赞成或反对各有权利，但应按照作者给出的实质版考虑自己的立场。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "提问者设问“抛开伦理”后，作者不进入伦理评价，而是断言提问的事实前提不成立：真正的主宰是五十岁以上的老年精英。",
    "以年龄刻度作反讽式类比：二十岁如婴儿、三十岁才有视听觉、四十岁刚懂事、五十岁才是青春期，把“成年”的界线整体后移。",
    "限定：以上只适用于发育正常者，多数人一生未达精神上的成人状态。",
    "给出机制：成人状态的发育条件只有精英才享有，故成熟与精英身份相互锁定。",
    "给出资源约束：这类机会客观上有限，公立教育只能水涨船高，只有结构性改变能略微提高成熟者比例。",
    "由机制推出主宰命题：各文明真正的主宰必然是生理意义上的老人。",
    "以反问强化：没有人能排除社会真正的主人。",
    "据此重述提问：所谓放弃老人，实际是放弃进不了专属医院的穷人。",
    "收窄对象：被放弃的是穷人中最好欺负的一群。",
    "不作伦理结论，只要求读者按这一实质版本形成自己的立场。"
   ],
   "concept_usage": [
    {"term": "老人", "meaning": "本文中不是泛指年长者，而是特指步入老年的一般生理意义上的社会真正主宰", "evidence": "P012", "ambiguity": "与“五十岁以上的精英集团”混用，未说明二者的边界"},
    {"term": "精英", "meaning": "享有特定发育条件、并被这些条件淬炼为精神上成熟者的人", "evidence": "P009", "ambiguity": "未给出可操作的判定标准"},
    {"term": "成人状态", "meaning": "精神上的成熟状态，作者把它的门槛放在五十岁", "evidence": "P008", "ambiguity": "属隐喻性刻度，未说明如何认定"},
    {"term": "专属医院", "meaning": "不会放弃老人的、只有有能力者才去得起的医疗机构", "evidence": "P014", "ambiguity": "未指明国别或具体机构，属修辞性说法"},
    {"term": "蚁群", "meaning": "用来比喻社会结构：关键类型的机会客观有限，不因教育普及而拉平", "evidence": "P011", "ambiguity": "类比而非论证，未界定相似点范围"}
   ],
   "examples_and_targets": [
    "五十岁以上的精英集团（作者的总体判断对象）",
    "朝鲜（作者设为可能的例外，随后自行限定）",
    "正恩小朋友（作者对金正恩的调侃式称呼，作为朝鲜例外的限定条件）",
    "主刀大夫见惯生死（作者的例证，说明精英享有的发育条件）",
    "总工程师考虑“二十年后这坝有裂纹怎么修”（作者的例证）",
    "前线指挥官面对一失手就尸袋成堆的压力（作者的例证）",
    "十八铜人阵（作者借用的比喻，指层层筛选的经历）",
    "防疫措施与放弃老人的政策争论（提问者给定的情境，属作者重述的对象）",
    "“没能力去不会放弃老人的专属医院的穷人”（作者对政策受体的界定）"
   ],
   "conditions": [
    "提问者明确要求抛开伦理，作者在正文中确实未讨论伦理，只谈损害与实质对象（Q001、P016）",
    "关于朝鲜的判断带“大概”“可能有点小特别”的限定（P002）",
    "对成人状态的判断限定在“幸运的发育正常的进程”之内（P008）",
    "淬炼机会被明说为注定有限，且只有这些机会才最有效（P010）",
    "公立教育被认为无法拉平差距；结构性改变也只能稍微提高成熟者比例，没有太大的本质提高（P011）",
    "主宰命题限定为“任何社会和文明里”（P012）",
    "作者把立场选择交给读者，只要求按实质版考虑（P016）"
   ],
   "rhetoric_and_tone": "论辩兼调侃。以“别开玩笑了”开头直接否定提问前提，语气讥诮；用年龄发育刻度作夸张类比（二十岁近乎只是一团肉），用“正恩小朋友”“十八铜人阵”“蚁群”等戏谑用语；两处反问（P013 谁能做到排除社会真正的主人？P016 之外无正面伦理结论）；结尾把判断权退回读者，不作道德裁决。",
   "unresolved_questions": [
    "“老人”的具体年龄界线与外延（是否等于五十岁以上）本文未说明",
    "“社会的结构性改变”具体指什么，本文未说明",
    "朝鲜例外的判断属于事实断言，需外部核查",
    "P014“没能力去不会放弃老人的专属医院的穷人”语句不顺（“没能力去”似缺“去不了的”一层），含义可解但有歧义",
    "P013“谁能做到排除社会真正的主人，各文明体真正的主宰？”为反问，未给出答案或判据",
    "提问中的“防疫措施”具体指哪一时段、哪一国的措施，本文未说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个世界的主宰是五十岁以上的精英集团", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "在整个朝鲜实际掌握运作的仍然是一群五十岁以上的老人", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P003", "quote": "二十岁只是刚睁眼的婴儿，近乎只是一团肉", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "五十岁才是青春期，才成其为一个有效的成人", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "大部分的人一辈子也没有在精神上发育到成人状态", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P009", "quote": "发育到成人状态和成为精英本身就是有锁定关系的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "这些机会是注定有限的", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "并不能靠公立教育来拉平", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "真正的主宰必定是一路过关斩将、打穿十八铜人阵以后已经步入老年的一般生理意义上的老人", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "本质上是在放弃没能力去不会放弃老人的专属医院的穷人", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "是在放弃穷人中最好欺负的一群人", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "请按照这个实质版考虑你的立场", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治社会学", "代际结构", "公共卫生伦理", "防疫政策"],
   "issue_candidates": ["放弃老人式防疫政策的实际受害者", "老年精英集团与社会支配结构", "精神成熟与精英身份的锁定", "教育能否拉平发育机会"],
   "text_function_candidates": ["答疑", "论辩", "反驳提问前提", "社会观察"],
   "object_candidates": ["五十岁以上的精英集团", "朝鲜", "金正恩", "穷人", "专属医院", "主刀大夫", "总工程师", "前线指挥官"],
   "working_keywords": ["老人", "精英集团", "成人状态", "锁定关系", "专属医院", "十八铜人阵", "蚁群", "结构性改变"]
  },
  "notes": "无图片节点。正文极短（710 字符，16 段），一次读完。提问者立场（是否应放弃老人）与作者立场（重述实质受害者）已分开。作者未给出伦理结论，只对政策受体作实质界定。文中“正恩小朋友”为对金正恩的调侃式指称，其所属国别判断为作者的事实断言，待外部核查。"
 },
 "2133f3d8": {
   "analysis": {
     "question_context": "提问者问“如何树立正确的财富观？”（Q001，属提问者）。作者先界定财富观＝对“财富的本质是什么”与“财富应该如何管理”两问的解答，再以“可持续性标准”为判定正确性的天然标准，随后分财富本质与实践守则展开一套以上帝、自然法与神义论为前提的财富伦理。",
     "content_units": [
       {
         "unit_id": "U001",
         "paragraph_refs": [
           "P001",
           "P002",
           "P003",
           "P004",
           "P005",
           "P006",
           "P007"
         ],
         "summary": "界定财富观两问；各意识形态皆有财富观，故须先立标准。",
         "role": "definition"
       },
       {
         "unit_id": "U002",
         "paragraph_refs": [
           "P008",
           "P009",
           "P010",
           "P011",
           "P012",
           "P013",
           "P014",
           "P015",
           "P016",
           "P017",
           "P018"
         ],
         "summary": "可持续性标准、两种模式、两层价值判断法则。",
         "role": "claim"
       },
       {
         "unit_id": "U003",
         "paragraph_refs": [
           "P019",
           "P020",
           "P021",
           "P022",
           "P023",
           "P024",
           "P025",
           "P026",
           "P027",
           "P028",
           "P029",
           "P030"
         ],
         "summary": "财富被赐予：人力占比甚微、运气不可排除，主权在天。",
         "role": "reason"
       },
       {
         "unit_id": "U004",
         "paragraph_refs": [
           "P031",
           "P032",
           "P033",
           "P034",
           "P035",
           "P036",
           "P037",
           "P038",
           "P039",
           "P040",
           "P041",
           "P042"
         ],
         "summary": "只有管理权；判“私有财产神圣不可侵犯”为误解；滥用者被消灭。",
         "role": "claim"
       },
       {
         "unit_id": "U005",
         "paragraph_refs": [
           "P043",
           "P044",
           "P045",
           "P046",
           "P047",
           "P048",
           "P049",
           "P050",
           "P051",
           "P052",
           "P053",
           "P054",
           "P055"
         ],
         "summary": "财富即责任；从享乐看财富中性甚至负面；守则首条为简朴。",
         "role": "conclusion"
       },
       {
         "unit_id": "U006",
         "paragraph_refs": [
           "P056",
           "P057",
           "P058",
           "P059",
           "P060",
           "P061",
           "P062",
           "P063",
           "P064",
           "P065",
           "P066",
           "P067",
           "P068",
           "P069",
           "P070"
         ],
         "summary": "存量财富优先用于自身健康平安但须更严自律；反驳“消费即收入”式浪费繁荣说。",
         "role": "rebuttal"
       },
       {
         "unit_id": "U007",
         "paragraph_refs": [
           "P071",
           "P072",
           "P073",
           "P074",
           "P075",
           "P076",
           "P077",
           "P078",
           "P079"
         ],
         "summary": "第二优先为子女供养（义务），其他成人供养本质是慈善；必要成本受节俭原则约束。",
         "role": "action_advice"
       },
       {
         "unit_id": "U008",
         "paragraph_refs": [
           "P080",
           "P081",
           "P082",
           "P083",
           "P084",
           "P085",
           "P086",
           "P087",
           "P088",
           "P089",
           "P090",
           "P091",
           "P092",
           "P093",
           "P094",
           "P095",
           "P096",
           "P097",
           "P098",
           "P099",
           "P100",
           "P101",
           "P102",
           "P103"
         ],
         "summary": "慈善主要指投资：正外部性、有效、不患得患失；投资是群体的祷告；“天使原则”。",
         "role": "claim"
       },
       {
         "unit_id": "U009",
         "paragraph_refs": [
           "P104",
           "P105",
           "P106",
           "P107",
           "P108",
           "P109",
           "P110",
           "P111",
           "P112",
           "P113",
           "P114",
           "P115",
           "P116",
           "P117",
           "P118",
           "P119",
           "P120",
           "P121",
           "P122",
           "P123",
           "P124",
           "P125",
           "P126",
           "P127",
           "P128",
           "P129",
           "P130",
           "P131",
           "P132",
           "P133"
         ],
         "summary": "更简手段（股票／指数基金）；“次要”指无条件匿名捐赠及数额与匿名细则。",
         "role": "action_advice"
       },
       {
         "unit_id": "U010",
         "paragraph_refs": [
           "P134",
           "P135",
           "P136",
           "P137",
           "P138",
           "P139",
           "P140",
           "P141",
           "P142",
           "P143",
           "P144",
           "P145",
           "P146",
           "P147",
           "P148",
           "P149",
           "P150",
           "P151",
           "P152",
           "P153",
           "P154",
           "P155",
           "P156",
           "P157",
           "P158",
           "P159",
           "P160",
           "P161",
           "P162",
           "P163",
           "P164",
           "P165",
           "P166",
           "P167",
           "P168",
           "P169",
           "P170",
           "P171",
           "P172"
         ],
         "summary": "捐赠下限不得为零（净收入与遗产）；以神义论与“生命也受节俭原则约束”解释；篇末未完待续。",
         "role": "conclusion"
       }
     ],
     "main_claims": [
       {
         "claim_id": "C001",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "财富观即对财富本质与财富管理两问的解答。",
         "evidence": [
           "E1"
         ]
       },
       {
         "claim_id": "C002",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "天然的正确标准是“可持续性标准”：理念获得追随者的能力大于追随者损失的速率。",
         "evidence": [
           "E2"
         ]
       },
       {
         "claim_id": "C003",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "可持续性有传染病模式与繁衍模式两种。",
         "evidence": [
           "E3"
         ]
       },
       {
         "claim_id": "C004",
         "claim_type": "author_qualified",
         "attribution": "author",
         "modality": "qualified",
         "statement": "所谈是理念自身的可持续性；最终无力断言无限可持续的理念孰对孰错。",
         "evidence": [
           "E4"
         ]
       },
       {
         "claim_id": "C005",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "两层法则：不具可持续性者无参选资格；可自可持续者中以有利于人类可持续者更优。",
         "evidence": [
           "E5"
         ]
       },
       {
         "claim_id": "C006",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "人力在最终产品的绝对构成要素中占比甚微，运气不可排除，劳动只是赢得一张抽奖券。",
         "evidence": [
           "E6"
         ]
       },
       {
         "claim_id": "C007",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "财富本质上是被赐予的而非赢来的，不存在“理应获得”，主权在天。",
         "evidence": [
           "E7"
         ]
       },
       {
         "claim_id": "C008",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "人所拥有的是被赐予的管理权而非所有权，且附有妥善运用以兑现祂对人类的爱的条件。",
         "evidence": [
           "E8"
         ]
       },
       {
         "claim_id": "C009",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "“私有财产神圣不可侵犯”是错的；滥用受托财富属自然法不容的窃取，终至被剥夺乃至消灭。",
         "evidence": [
           "E9",
           "E10"
         ]
       },
       {
         "claim_id": "C010",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "每一分财富都预定要经由领受者转交给全人类；财富越大责任与惩罚越重。",
         "evidence": [
           "E11"
         ]
       },
       {
         "claim_id": "C011",
         "claim_type": "author_qualified",
         "attribution": "author",
         "modality": "qualified",
         "statement": "从纯粹享乐立场看财富中性甚至负面；若无对等自觉，致富是途经欲望而通向地狱的路。",
         "evidence": [
           "E12"
         ]
       },
       {
         "claim_id": "C012",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "存量财富首先用于自身健康平安，但该优先权易被滥用，须在奢侈浪费的认定上采较严标准。",
         "evidence": [
           "E13"
         ]
       },
       {
         "claim_id": "C013",
         "claim_type": "opponent_view",
         "attribution": "opponent",
         "modality": "asserted",
         "statement": "被作者反驳的流行理论：一人的消费即另一人的收入，人人奢侈浪费即可互相刺激、实现更大的繁荣。",
         "evidence": [
           "E14"
         ]
       },
       {
         "claim_id": "C014",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "negated",
         "statement": "该理论是错的：浪费指不带来价值积淀的财富使用，这种繁荣迫使“无主”自然环境承受损失。",
         "evidence": [
           "E15"
         ]
       },
       {
         "claim_id": "C015",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "第二优先是子女供养的义务；其他成人不能与子女竞争优先关系，帮助他们是慈善。",
         "evidence": [
           "E16"
         ]
       },
       {
         "claim_id": "C016",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "凡列入“必要成本”的支出都遵循节俭原则，越优先保障者标准越严。",
         "evidence": [
           "E17"
         ]
       },
       {
         "claim_id": "C017",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "慈善【主要】指投资：选择有正外部性的事业，做有效的、完全不患得患失的投资。",
         "evidence": [
           "E18"
         ]
       },
       {
         "claim_id": "C018",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "投资须严格计算风险、在道德原则约束下公平竞争追求最大利润；不是变相的天女散花。",
         "evidence": [
           "E19",
           "E20"
         ]
       },
       {
         "claim_id": "C019",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "“次要”指无条件的匿名捐赠，数额小到不介意、以可接受没有任何回报为限；你只是邮递员，不可由此牟取个人利益。",
         "evidence": [
           "E21",
           "E22"
         ]
       },
       {
         "claim_id": "C020",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "negated",
         "statement": "但也不能把捐赠降到零：凡有净收入必有捐献，临终遗产中捐献部分也不能为零。",
         "evidence": [
           "E23"
         ]
       },
       {
         "claim_id": "C021",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "此下限的理由是相信上帝的爱者必信上帝绝不会给予你承受不起的遭遇，这就是神义论。",
         "evidence": [
           "E24"
         ]
       },
       {
         "claim_id": "C022",
         "claim_type": "author_qualified",
         "attribution": "author",
         "modality": "qualified",
         "statement": "“遗产必须分出一部分捐掉”是误解：若继承人继承你的财富观，可将全部遗产移交他们。",
         "evidence": [
           "E25"
         ]
       },
       {
         "claim_id": "C023",
         "claim_type": "author_explicit",
         "attribution": "author",
         "modality": "asserted",
         "statement": "该条款的真因是人不得将全部受托财富耗尽于保命；生命亦受节俭原则约束，须准备在恰当的点放弃优先权。",
         "evidence": [
           "E26",
           "E27"
         ]
       },
       {
         "claim_id": "C024",
         "claim_type": "author_qualified",
         "attribution": "author",
         "modality": "qualified",
         "statement": "仅因意外太快、来不及下令用光而客观上有所剩余，这不算数；建议提前立好遗嘱。",
         "evidence": [
           "E28"
         ]
       }
     ],
     "argument_steps": [
       "定义财富观；各意识形态皆有财富观，故须先立判定正确的标准。",
       "提出可持续性标准：获得追随者的能力大于追随者损失的速率。",
       "分传染病模式与繁衍模式两种维持机制。",
       "限定为理念自身的可持续性，承认无力断言无限可持续者孰对孰错。",
       "得两层法则：不具可持续性者无参选资格；可自可持续者中以有利于人类可持续者更优。",
       "财富本质一：财富经由有效的祈祷被赐予（人力占比甚微、运气不可排除）。",
       "以农业与团队研发为例，说明被默认“不应出问题”的环节其实无人保证。",
       "推出劳动只是抽奖券、主权在天而无公平与否。",
       "本质二：只有被赐予的管理权，以“总经理与公司所有者”为类比，判“私有财产神圣不可侵犯”为错。",
       "警告滥用：诅咒收紧、终至财富与后代被消灭；扩大到“财富即责任”。",
       "进入守则：生活简朴；存量财富首用于自身健康平安，但须更严自律。",
       "反驳“消费即收入、奢侈浪费刺激繁荣”。",
       "第二优先：子女供养是义务，其他成人供养本质是慈善；必要成本受节俭原则约束。",
       "重解“普遍增大支出导致繁荣”系指慷慨慈善。",
       "解释“慈善主要指投资”：正外部性＋有效性＋不患得患失；投资是群体的祷告。",
       "提出“天使原则”，区分守法则与未守法则的亏损；给出买股票或指数基金的简化手段。",
       "解释“次要”：无条件的匿名捐赠及数额、匿名、不得谋私利等细则。",
       "规定捐赠下限不得为零：净收入必有捐献，遗嘱必有留给世人的部分。",
       "以神义论解释第一条下限；澄清教育成功的继承人可继承全部财富。",
       "给出第二条下限的真因：不得耗尽财富保命，生命也要节俭，须在恰当的点放弃优先权并提前立遗嘱。"
     ],
     "concept_usage": [
       {
         "term": "财富观",
         "meaning": "对财富本质与财富管理两问的解答",
         "evidence": "P003",
         "ambiguity": "作者只取这两问"
       },
       {
         "term": "可持续性标准",
         "meaning": "获得追随者的能力大于追随者损失的速率",
         "evidence": "P008",
         "ambiguity": "无可计量尺度"
       },
       {
         "term": "管理权／所有权",
         "meaning": "所有的是有条件的代管资格而非可任意处置的所有权",
         "evidence": "P037",
         "ambiguity": "与世俗法权关系未展开"
       },
       {
         "term": "正外部性",
         "meaning": "副作用可由利润补偿、各方未亏本且有合理利润、外部第三方受益",
         "evidence": "P083",
         "ambiguity": "判定标准未给出"
       },
       {
         "term": "天使原则",
         "meaning": "把投入视作对正确事业的天使投资，光荣的失败也算最好的运用",
         "evidence": "P094",
         "ambiguity": "与“有效投资”存在张力"
       },
       {
         "term": "节俭原则",
         "meaning": "凡列入“必要成本”的支出均受约束，越优先者标准越严",
         "evidence": "P073",
         "ambiguity": "无量化界线"
       },
       {
         "term": "神义论",
         "meaning": "无论如何都相信神的义，不将艰苦视作恶意折磨",
         "evidence": "P144",
         "ambiguity": "与“神罚”并存，分界未说明"
       }
     ],
     "examples_and_targets": [
       "太平天国（例：致死率百分百的理念因初代倒霉蛋灭绝而湮灭）",
       "阳光、降雨、土地、空气、昆虫（例证：人力只占粮食生长很小部分）",
       "团队研发上市所赖的没染病、没离婚、没遭至亲去世、没被车撞、办公室没倒塌（例证）",
       "“总经理”与公司所有者（类比：人只是管家而非主人）",
       "一顿用二十只鸡、一百斤米（例证：浪费不带来价值积淀）",
       "“一个人的消费就是另一个人的收入”（作者明确反驳的流行理论）",
       "父母、配偶、亲属、朋友与子女（用于区分义务与慈善）",
       "环保、医疗、养老、正当科学研究、艺术探索（作者举的达标事业）",
       "股票或指数基金（作者给出的投资手段）",
       "黑天鹅与灰犀牛（修辞：要知道它们的主人是谁）",
       "坐车没钱者、付不起手术费者、山区失学少年（匿名捐赠对象）",
       "“一次指路”与“一个铜板”（非货币形式的最小捐赠）",
       "继承人（含养子养女，天赐责任对象）",
       "烧香占卜吃致幻剂所得的谶语卦辞（作者否定为神意愿）"
     ],
     "conditions": [
       "整套论证以对上帝、自然法秩序与神义论的信仰为前提，多用“如果…那么”“只要是真的”等条件式",
       "第一优先用于自身健康平安以“只要是真的”有需要为前提；上帝不设一刀切数字但洞知人心",
       "无回报捐赠以“你可以接受没有任何回报”“不会介意、不会长期念念不忘”为数额上限",
       "投资有效性要求在道德原则约束下参与公平竞争",
       "遗产可全部留给继承人的前提是他们继承了你的财富观",
       "信仰成熟、信心强大且不以世俗为念者，捐赠比例可扩大",
       "对父母、配偶、亲属、朋友的供养以对方本应自负生存责任为前提",
       "篇末“（未完，待续）”提示本文非完整论述"
     ],
     "rhetoric_and_tone": "训诫与布道式断言混合。以第二人称“你/你们”直接告诫（“这句话你们记住”“恕我直言”）；反复用“但这是错的”作强硬转折；以反问施压（“有谁对你保证了这些环节不会出问题？”）；括号内插入对“选择”的解构式讥讽；以“神圣”“诅咒”“震怒”“贪污和亵渎”等宗教语汇建立权威；用“总经理”“邮递员”“天女散花”“天使投资”等比喻组织论证；先立标准与本质，再列实践守则，层层加码至“生命也要节俭”。",
     "unresolved_questions": [
       "“理念的可持续性”如何观察或计量，本文未说明",
       "“神赐”与“自然法”是同一回事还是两层，本文未明确区分",
       "“自然法则的认知义务在受管辖者自身”，但“不知道”者的责任如何成立，未展开",
       "“正外部性”三项条件由谁判定、如何判定，本文未说明",
       "“天使原则”与“投资要严格计算风险、追求最大利润”之间的关系，本文未详述",
       "错别字照原文保留：P039“秩序所欲”、P053“途经欲望”、P126“亿”为异体字",
       "P116 句末无标点，句意不完整",
       "P004 为列表父节点，与 P005、P006 文本重复，系结构重复而非正文重复",
       "篇末标“（未完，待续）”；P089 提到另有“直接赠送式的慈善”的讨论，不在本批次内",
       "该财富伦理对非信仰者的适用性，本文未说明",
       "同一理念能否兼具传染病模式与繁衍模式，本文未说明",
       "被反驳的“消费即收入”理论已按 opponent_view 记录，未归给作者"
     ],
     "evidence": [
       {
         "key": "E1",
         "paragraph_id": "P003",
         "quote": "财富观是指对以下两个问题",
         "relation": "supports"
       },
       {
         "key": "E2",
         "paragraph_id": "P008",
         "quote": "一个理念获得追随者的能力大于追随者损失的速率",
         "relation": "supports"
       },
       {
         "key": "E3",
         "paragraph_id": "P009",
         "quote": "可持续性本身又分两种模式",
         "relation": "supports"
       },
       {
         "key": "E4",
         "paragraph_id": "P012",
         "quote": "而不是理念的追随者的可持续性",
         "relation": "qualifies"
       },
       {
         "key": "E5",
         "paragraph_id": "P017",
         "quote": "有利于人类自身的可持续性的",
         "relation": "supports"
       },
       {
         "key": "E6",
         "paragraph_id": "P027",
         "quote": "劳动只是为你赢得了一张抽奖券",
         "relation": "supports"
       },
       {
         "key": "E7",
         "paragraph_id": "P028",
         "quote": "财富在本质上是被赐予的",
         "relation": "supports"
       },
       {
         "key": "E8",
         "paragraph_id": "P037",
         "quote": "而是人被赐予的管理权",
         "relation": "supports"
       },
       {
         "key": "E9",
         "paragraph_id": "P035",
         "quote": "但这是错的",
         "relation": "supports"
       },
       {
         "key": "E10",
         "paragraph_id": "P042",
         "quote": "自然法所不容的窃取行为",
         "relation": "supports"
       },
       {
         "key": "E11",
         "paragraph_id": "P046",
         "quote": "对爱的最大实践",
         "relation": "supports"
       },
       {
         "key": "E12",
         "paragraph_id": "P053",
         "quote": "也是途经欲望而通向",
         "relation": "supports"
       },
       {
         "key": "E13",
         "paragraph_id": "P062",
         "quote": "越要遵循更严格的节俭",
         "relation": "supports"
       },
       {
         "key": "E14",
         "paragraph_id": "P066",
         "quote": "因为一个人的消费就是另一个人的",
         "relation": "context"
       },
       {
         "key": "E15",
         "paragraph_id": "P068",
         "quote": "所谓浪费，是指不会带来价值积淀",
         "relation": "contradicts"
       },
       {
         "key": "E16",
         "paragraph_id": "P072",
         "quote": "父母、配偶、亲属、朋友都并不能与子女竞争",
         "relation": "supports"
       },
       {
         "key": "E17",
         "paragraph_id": "P073",
         "quote": "都必然要遵循节俭原则",
         "relation": "supports"
       },
       {
         "key": "E18",
         "paragraph_id": "P081",
         "quote": "做【有效的】、【完全不患得患失的】投资",
         "relation": "supports"
       },
       {
         "key": "E19",
         "paragraph_id": "P086",
         "quote": "投资要严格的计算风险",
         "relation": "supports"
       },
       {
         "key": "E20",
         "paragraph_id": "P095",
         "quote": "一样是得到了最好的运用",
         "relation": "supports"
       },
       {
         "key": "E21",
         "paragraph_id": "P121",
         "quote": "没有已知利害关系的不特定对象",
         "relation": "supports"
       },
       {
         "key": "E22",
         "paragraph_id": "P129",
         "quote": "避免你将这些变成一种投资",
         "relation": "supports"
       },
       {
         "key": "E23",
         "paragraph_id": "P137",
         "quote": "也就是凡有净收入，必有捐献",
         "relation": "supports"
       },
       {
         "key": "E24",
         "paragraph_id": "P144",
         "quote": "这就是神义论",
         "relation": "supports"
       },
       {
         "key": "E25",
         "paragraph_id": "P155",
         "quote": "这并不表示你的遗产必须要分出一部分来捐掉",
         "relation": "qualifies"
       },
       {
         "key": "E26",
         "paragraph_id": "P162",
         "quote": "你不能将全部被托付的财富耗尽用于保住自己的生命",
         "relation": "supports"
       },
       {
         "key": "E27",
         "paragraph_id": "P168",
         "quote": "我已经不再应该享有",
         "relation": "supports"
       },
       {
         "key": "E28",
         "paragraph_id": "P171",
         "quote": "我建议你提前立好遗嘱",
         "relation": "supports"
       }
     ]
   },
   "provisional_tags": {
     "domain_candidates": [
       "宗教伦理",
       "财富伦理",
       "经济学（投资与消费）",
       "社会哲学",
       "意识形态理论"
     ],
     "issue_candidates": [
       "何为正确的财富观",
       "理念的可持续性标准",
       "财富是被赐予的还是赢来的",
       "所有权与管理权之别",
       "奢侈浪费是否刺激繁荣",
       "慈善与投资的界限",
       "匿名捐赠与捐赠下限",
       "遗产的公益份额",
       "生命的节俭原则"
     ],
     "text_function_candidates": [
       "答疑",
       "训诫",
       "系统论述",
       "论辩",
       "反驳流行理论"
     ],
     "object_candidates": [
       "上帝／神",
       "自然法",
       "太平天国",
       "继承人",
       "子女",
       "父母与配偶",
       "慈善机构",
       "指数基金",
       "黑天鹅与灰犀牛"
     ],
     "working_keywords": [
       "财富观",
       "可持续性标准",
       "传染病模式",
       "繁衍模式",
       "被赐予",
       "管理权",
       "所有权",
       "私有财产神圣不可侵犯",
       "财富即责任",
       "节俭原则",
       "正外部性",
       "天使原则",
       "天女散花",
       "神义论",
       "遗嘱"
     ]
   },
   "notes": "无图片节点，正文 9097 字符（172 段），全文读完。提问者问句与作者论述已分开；作者明确反驳的“消费即收入／奢侈浪费刺激繁荣”理论按 opponent_view + attribution=opponent 记录，未归给作者；篇末标“（未完，待续）”，作者另提到“直接赠送式的慈善”的讨论，均非本篇内容，未据以补全。错别字与异体字照原文保留未改写。P004 与 P005/P006 文本重叠系列表父子节点所致，非正文重复。为满足单篇 40000 字符上限，已合并同类主张并压缩短引与摘要文字，未删减证据定位与未决问题。"
 }}
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
