# -*- coding: utf-8 -*-
"""批次 r001-b0039 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0039.sessions.py            # 写 out/r001-b0039.out.jsonl
  python3 records/r001-b0039.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0039"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0039.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "2a9e96de": {
  "analysis": {
   "question_context": "提问者（Q001）问“女生如何培养自己的时尚感觉和品味？”。作者（P001）先把时尚感觉与品味问题重新界定为思想问题而非视觉审美问题，随后给出五个自我定位问题（P002-P008），再逐一反驳“我高兴就好”与“越广受欢迎越好”两种评价标准（P011-P029），提出“外貌是一道编过码的半透膜”“吸引爱人的人、给贪婪的人添堵”的战略（P030-P046），最后给出落地方法：把美感建立在意义之上、先理清每件东西存在的逻辑再谈色彩质感形状（P061-P092）。P009、P010、P060 为连载式插话（“先吃饭，吃完再说”“回来了，书接上文”“待会儿继续”），P093 末行含平台话题标签。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "重新界定问题：个人时尚感觉与品味问题本质上不是视觉审美问题，而是思想问题。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007", "P008"],
     "summary": "给出五个自我定位问题（你心中你是谁、你希望成为谁、你希望别人觉得你是谁、你能接受理想与现实多大差距、别人如何认识到你想表达的自我），并称回答好这五个问题就能推算出自己的选择。",
     "role": "definition"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P009", "P010"],
     "summary": "连载式插话：先吃饭、回来续写。",
     "role": "transition"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"],
     "summary": "先摆正方法论问题（如何评价个人表达是好的），列出两种常见答案——“我高兴就好”“越广受欢迎越好”，并判定两种答案都是错的。",
     "role": "claim"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P017", "P018", "P019", "P020"],
     "summary": "反驳第一种答案：照此行事者多被评论为“怪胎”“不合群的混蛋”“自以为了不起”而非“有个性”“勇敢”；因为你是别人世界的组成部分，不考虑ta人感受、不研究审美规律去表达个性，流露的是无情和冷漠，等于给自己下诅咒。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029"],
     "summary": "反驳第二种答案：好美之心后面十之八九是贪欲；贪婪者会下重注讨好，但投入的都是你欠下的本息，他们会把重本称为爱、把收不回的本息称为你的罪并据此发起“天诛”；即使能拒绝，做冰山美人也有代价；为了淘金而光芒万丈、在蚊蝇围绕中苦等是笨得让人心疼的办法。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P030", "P031", "P032", "P033", "P034"],
     "summary": "正面主张：外貌应是编过码的半透膜，识得的人值得、不值得的人识不得；目标不是人人都喜欢，而是“大部分人都不喜欢，但那特别的一群人却会视如珍宝”的样子。",
     "role": "claim"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040"],
     "summary": "区分两类人：区别在于爱；爱人是正资产永远不嫌多，贪婪者是负资产永远不嫌少；外观设计的基本战略是吸引爱人的注意、给贪婪的人处处添堵，一体两面，绝不是无差别吸引。",
     "role": "claim"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046"],
     "summary": "给出识别两类人的三条做法（是否知道权界、是否尊重权界、能否接受别人合法行使自由导致自己利益受损），并称守住第三条者值得吸引，守不住者会把你的自由因自身利益剥夺，构成剥夺和奴役。",
     "role": "reason"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": ["P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059"],
     "summary": "把两类人与审美风格打通：贪婪者在意美貌的可交易性，偏好万众一心、有强烈通兑性的审美，厌恶小众有门槛的审美；因此要避开网红装与最流行方案，真正的fashion“奇怪”是因为击碎通兑性、对贪婪者达成自我鸡肋化，这也正是谈论fashion的起点。",
     "role": "conclusion"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": ["P060", "P061", "P062", "P063"],
     "summary": "转入具体做法指南：把美感建立在意义之上，在考虑款式颜色样式之前先考虑内容。",
     "role": "action_advice"
    },
    {
     "unit_id": "U012",
     "paragraph_refs": ["P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075"],
     "summary": "以欧洲婚礼“一旧一新一借一蓝”惯例作类比，提出“一件为你的信仰/理想/经历/原则/习惯”，并给出两条原则：每件东西的选择先有精神上、实用上的理由，含义彼此以你所赞同的方式协调、在价值观里自洽；这首先是一个“埋梗的游戏”，外表是一本编码的书。",
     "role": "action_advice"
    },
    {
     "unit_id": "U013",
     "paragraph_refs": ["P076", "P077", "P078", "P079", "P080", "P081", "P082"],
     "summary": "举两个“埋梗”典范：剑道服袴的折叠纹象征五伦与精忠尽孝；佛教僧衣（粪扫衣、坏色衣、割截衣、福田衣）的由来。并归纳共性：成型装束背后的理由极少是因为好看，而是实用理由或信仰象征；是内在逻辑自洽的组合定义出美，而非美学原则指导它们。",
     "role": "example"
    },
    {
     "unit_id": "U014",
     "paragraph_refs": ["P083", "P084", "P085"],
     "summary": "以忍者装束为例：完全为猎杀潜行、无美学理由，人们因热爱强悍而反过来认为它有力之美；因此应先理清身上所有事物存在的逻辑并令其自洽统一，投入的思考越多越趋向于成为同类的共同选择，这种共鸣就是令ta们感到美的信号。",
     "role": "reason"
    },
    {
     "unit_id": "U015",
     "paragraph_refs": ["P086", "P087", "P088", "P089", "P090", "P091", "P092"],
     "summary": "结论：在逻辑统一的前提下再考虑色彩质感形状，视觉问题会容易得多，并会形成属于你的“构型”即fashion；它有对特定人群来说永恒的合理性，因此会流行成为时尚，并成为带在身上的测试题——看得懂的人有资格得到额外关注。",
     "role": "conclusion"
    },
    {
     "unit_id": "U016",
     "paragraph_refs": ["P093"],
     "summary": "末段为“什么叫做「时尚」？”与平台话题标签“女性相关答集”，该段未被 lexical 结构覆盖。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：个人时尚感觉问题和品味问题本质上不是一个视觉审美问题，而是一个思想问题。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张你穿什么、如何行卧坐立取决于五个问题（你心中你是谁、你希望成为谁、你希望别人觉得你是谁、你能接受理想与现实多大差距、你认为别人如何才能认识到你想表达的自我），回答好这五个问题就可以推算出自己的选择。",
     "evidence": ["E2", "E3", "E4", "E5"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定评价个人表达好坏的两种常见答案——“我高兴就好”“越广受欢迎越好”——都是错的。",
     "evidence": ["E6", "E7", "E8"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预言遵循“我高兴就好”去走，绝大多数人会被评论为“怪胎”“不合群的混蛋”“自以为了不起”，而不是“有个性”“勇敢”。",
     "evidence": ["E9"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出的理由：你是别人世界的一个组成部分；选择不考虑ta人感受（不研究人的审美规律和基本审美心理、无视美学规律）去表达“个性”，流露的是无情和冷漠，等于给自己下诅咒。",
     "evidence": ["E10", "E11"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为“越广受欢迎越好”背后十之八九是贪欲：贪婪者投入的都是你欠下的本息，他们会把重本称为爱、把收不回的本息称为你的罪，授予自己报复的正当性并对你发起“天诛”。",
     "evidence": ["E12", "E13", "E14"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张外貌应该是一道编过码的半透膜——识得的人就是值得的人，不值得的人就识不得；不是把自己变成所有人都喜欢的样子，而是“大部分人都不喜欢，但那特别的一群人却会视如珍宝”的样子。",
     "evidence": ["E15", "E16"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以“区别在于爱”划分两类人：爱人对人永远是正资产、永远不嫌多，贪婪的人对人则是负资产、永远不嫌少；外观设计的基本战略是吸引爱人的注意、给贪婪的人处处添堵，绝不是“无差别吸引”。",
     "evidence": ["E17", "E18", "E19"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出识别两类人的三条做法：是否知道权界在哪里、是否尊重权界、是否能接受别人合法行使自由导致自己利益受损；前两条是第三条的基础，关键是第三条。",
     "evidence": ["E20", "E21"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称守不住第三条的人会成为人的负资产：只要靠近就会发现自己的自由常被此人因为ta自己的利益剥夺，这对你就构成剥夺和奴役。",
     "evidence": ["E22"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称贪婪者在意美貌的可交易性，喜欢万众一心不假思索就会喜欢、具有强烈通兑性的审美，天生厌恶小众的、独特的、有认知门槛的审美。",
     "evidence": ["E23", "E24"]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者建议避开网红装与眼下最具广泛认可度的最流行方案；并称真正的fashion多少有些“奇怪”的内在原因是击碎通兑性、对贪婪者达成自我鸡肋化，这是一重保护。",
     "evidence": ["E25", "E26"]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出具体做法：把美感建立在意义之上，在考虑款式颜色样式之前先考虑内容；每一件东西的选择都要先有精神上、实用上的理由，含义彼此以你所赞同的方式互相协调、选择逻辑在价值观里自洽。",
     "evidence": ["E27", "E28", "E29"]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称成型装束背后的理由极少是因为好看，而是职业身份的实用理由或精神信仰的象征性理由；是这些内在逻辑完全自洽的事物的组合定义出了一种美，而不是美学原则来指导了它们。",
     "evidence": ["E30", "E31"]
    },
    {
     "claim_id": "C015",
     "claim_type": "quoted_or_cited",
     "attribution": "cited_source",
     "modality": "asserted",
     "statement": "作者引述剑道服袴的折叠纹象征五伦道德与精忠尽孝，以及佛教僧衣（粪扫衣、坏色衣、割截衣、福田衣）的由来，作为“埋梗”的典范。",
     "evidence": ["E34", "E35"]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张先理清身上所有事物存在的逻辑并令其自洽统一，在前一议题得到高质量解决的前提下视觉问题会容易得多，并会形成属于你的“构型”；fashion成为“时尚”在于它有对特定人群来说永恒的合理性。",
     "evidence": ["E32", "E39"]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称这一套设计会成为带在身上的一套测试题——看得懂的人有资格得到你的额外关注。",
     "evidence": ["E33"]
    }
   ],
   "argument_steps": [
    "重新界定问题：时尚与品味是思想问题而非视觉审美问题（P001）。",
    "提出五个自我定位问题，并称回答后即可推算选择（P002-P008）。",
    "以插话表明分次续写（P009、P010）。",
    "提出评价方法论问题“如何评价我的个人表达是好的”，列出两种常见答案（P011-P015），判定两者皆错（P016）。",
    "反驳答案一：不考虑他人感受的“个性”会招致负面评价，是无情和冷漠，等于自我诅咒（P017-P020）。",
    "反驳答案二：越广受欢迎越好背后的贪欲逻辑与“天诛”，以及为淘金而光芒万丈的代价（P021-P029）。",
    "正面主张：外貌是编过码的半透膜，目标是“大部分人都不喜欢，但那特别的一群人视如珍宝”（P030-P034）。",
    "给出战略：吸引爱人的人、给贪婪的人添堵，并给出识别两类人的三条标准（P035-P046）。",
    "把两类人对应到审美风格差异，得出避开网红装、击碎通兑性的行动结论（P047-P059）。",
    "给出落地指南：把美感建立在意义之上（P061-P063），以婚礼惯例类比“一件为你的信仰/理想/经历/原则/习惯”（P064-P075）。",
    "以剑道服、佛教僧衣、忍者装束为例归纳：装束的理由极少因为好看，逻辑自洽的组合定义出美（P076-P085）。",
    "结论：先统一逻辑再谈视觉，形成个人的“构型”与时尚，并成为筛选同类的一套测试题（P086-P092）。"
   ],
   "concept_usage": [
    {
     "term": "时尚感觉/品味",
     "meaning": "本文将其界定为思想问题：由自我认知与表达意图决定，而非视觉审美技巧。",
     "evidence": "P001",
     "ambiguity": "未给出“品味”与“时尚”的区分，二者在文中基本并用。"
    },
    {
     "term": "编过码的半透膜",
     "meaning": "作者对外貌的比喻：识得的人（值得的人）能读懂，不值得的人识不得。",
     "evidence": "P031",
     "ambiguity": "“编码”的具体规则由后文“埋梗”与逻辑自洽原则补充，未给出统一标准。"
    },
    {
     "term": "爱人的人/贪婪的人",
     "meaning": "作者对人群的两分：以是否尊重权界、能否接受他人合法行使自由导致自己利益受损为判据；前者是正资产，后者是负资产。",
     "evidence": "P036",
     "ambiguity": "两分法是否穷尽所有人、是否存在中间类型，本文未说明。"
    },
    {
     "term": "权界",
     "meaning": "作者用于识别两类人的核心标准（是否知道、是否尊重、能否接受他人合法行使自由带来的自身利益受损）。",
     "evidence": "P042",
     "ambiguity": "“权界”未定义，边界如何划定未说明。"
    },
    {
     "term": "通兑性",
     "meaning": "审美可被普遍共同认可、从而可交易的性质；贪婪者偏好高通兑性审美。",
     "evidence": "P051",
     "ambiguity": "为作者自造词，未给出度量或例证清单。"
    },
    {
     "term": "自我鸡肋化",
     "meaning": "通过击碎通兑性使自己对于贪婪者失去交易价值，从而获得保护。",
     "evidence": "P057",
     "ambiguity": "为作者自造表述，未说明适用限度。"
    },
    {
     "term": "埋梗的游戏",
     "meaning": "作者对外表设计的说法：每件东西带含义且彼此协调，外表是一本编码的书。",
     "evidence": "P075",
     "ambiguity": "“梗”的公共可读性与个人私密性之间的边界未说明。"
    },
    {
     "term": "构型",
     "meaning": "逻辑统一后形成的属于个人的整体外形，即属于你的fashion。",
     "evidence": "P087",
     "ambiguity": "未给出判定“构型”成型的标准。"
    },
    {
     "term": "天诛",
     "meaning": "作者形容贪婪者在收不回投入时对“你”发起的报复。",
     "evidence": "P025",
     "ambiguity": "为修辞性说法，非事实描述。"
    }
   ],
   "examples_and_targets": [
    "网红装与眼下最具广泛认可度的最流行方案：作者建议避开的对象（P056）。",
    "欧洲婚礼惯例“Something old, something new, something borrowed, something blue and a silver sixpence in your shoe.”：作者引用并类比的材料（P065、P066）。",
    "剑道服的袴（hakama）及其折叠纹象征：作者引例（引文块）（P077）。",
    "佛教僧衣（粪扫衣、百衲衣、坏色衣、割截衣、福田衣；说一切有部皂色衣、大众部黄色衣等）：作者引例（引文块）（P079）。",
    "忍者装束：作者例证（完全为猎杀潜行，因强悍而被认为有力量的美）（P083、P089）。",
    "“怪胎”“不合群的混蛋”“自以为了不起”“有个性”“勇敢”：作者所述他人可能给出的评价标签（P017）。",
    "“驴打滚的利”：作者比喻（P024）。",
    "“冰山美人”：作者所述拒绝追求者的代价的说法（P026）。"
   ],
   "conditions": [
    "P006 以“你能/打算接受3和1、2之间存在怎样的、多大的差距”为条件性提问。",
    "P017 “绝大多数人都会被评论为……”为概率性限定，非全称。",
    "P023 “这好美之心后面十之八九都是贪欲”为概率限定。",
    "P026 “即使你自己有本能的智慧去拒绝这些人，如果你真的是美人的话”为假设条件。",
    "P046 以“守得住第三条/守不住第三条”作条件分支。",
    "P052 限定贪婪者厌恶的审美类型为“小众的、独特的、不是直接诉诸低级感官的、有认知门槛的”。",
    "P054 “对爱人的人，因为他们不需要拿你的美貌兑换利益，他们就没有这种强迫性”为条件性说明。",
    "P087 “在前一个议题得到高质量解决的前提下”为前置条件。",
    "P088 “只要以后还有人会有你一样的信仰、希望、原则……如果你的思考是深入的、实际的”为条件。"
   ],
   "rhetoric_and_tone": "长篇说教/训诫体，通篇以第二人称“你”直接对读者说话并反复追问（“不是吗？”“对吗？”“你看到关联了吗？”）；大量破折号短句与口语插入（“先吃饭，吃完再说”“回来了，书接上文”“待会儿继续”“OK”）；比喻密集（半透膜、编码的书、埋梗、通兑性、鸡肋、驴打滚的利、天诛、冰山美人）；中英混用（fashion、pass）；引用英文婚礼俗谚与两段引文块（剑道服、佛教僧衣）；带有强烈预警口吻（“为了保住你的小命”）。",
   "unresolved_questions": [
    "P093（字符 4096-4112）含平台话题标签“女性相关答集”，与正文“什么叫做「时尚」？”混排，且该段未被 lexical 结构覆盖（阅读包登记 text_tail_not_in_lexical）；该篇是否被平台加标签或截断，需研究者判断。",
    "提问为“女生如何培养……”，正文通篇以泛称“你/你们”展开，未特指女性，性别指向差异需研究者判断。",
    "P077、P079 为引文块（field=quote），作者未在正文标明具体来源，P079 内含 [3][6] 等脚注标记，出处需外部核查。",
    "“权界”“贪欲”“爱人的人”等关键概念均未定义，判定标准需研究者复核。",
    "P009、P010、P060 表明本文为分次续写，是否存在其他更新版本本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "个人时尚感觉问题和品味问题，本质上不是一个视觉审美问题，而是一个思想问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你穿什么，如何行卧坐立，取决于以下几个因素：", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "你能/打算接受3和1、2之间存在怎样的、多大的差距？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "你认为别人如何才能认识到你想要表达的自我？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "回答好这五个问题，你就可以推算出你的选择。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P014", "quote": "我高兴就好，我高兴的，就是真我，管你喜欢不喜欢。", "relation": "context"},
    {"key": "E7", "paragraph_id": "P015", "quote": "越广受欢迎越好，越引人尊敬/渴望/羡慕越好。", "relation": "context"},
    {"key": "E8", "paragraph_id": "P016", "quote": "但这两种答案都是错的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "遵循第一条去走，绝大多数人都会被评论为“怪胎”“不合群的混蛋”“自以为了不起”这类负面评价，而并不是“有个性”“勇敢”这类正面评价。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "因为不管你愿意不愿意，你是别人的世界的一个组成部分。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "全身写满无情和冷漠，你当然是在给自己下诅咒。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "但这好美之心后面十之八九都是贪欲。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "但是，请不要怀疑贪婪者的智商和职业伦理——在你身上投入的，都是你欠下的，还有驴打滚的利。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P025", "quote": "他们会把之前所下的重本称之为爱，把收不回的本息称为你的罪，授予自己报复的正当性，对你发起“天诛”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P031", "quote": "记住，你的外貌应该是一道编过码的半透膜——识得的人，就是值得的人；不值得的人，就识不得。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P033", "quote": "你不是要把自己变成所有人都喜欢的样子，你是要把自己变成“大部分人都不喜欢，但那特别的一群人却会视如珍宝”的样子。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P036", "quote": "区别在于爱。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P038", "quote": "爱人的人，对人永远是正资产，永远不嫌多；而贪婪的人，对人则是负资产，永远不嫌少。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P039", "quote": "吸引爱人的人的注意，而给贪婪的人处处添堵。一体两面，缺一不可。绝不是“无差别吸引”。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P042", "quote": "1）此人知不知道权界在哪里？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P045", "quote": "前两条是第三条的基础，关键就是第三条。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P046", "quote": "守不住第三条，那么这人就会成为人的负资产，你只要靠近，就会发现自己的自由常被此人因为ta自己的利益剥夺", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P051", "quote": "贪婪者喜欢那种万众一心不假思索就会喜欢的审美，那种具有强烈通兑性的审美。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P052", "quote": "他们天生厌恶小众的、独特的、不是直接诉诸低级感官的、有认知门槛的审美。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P056", "quote": "1）你要避开网红装，避开眼下最具有广泛认可度的、最流行的方案——为了保住你的小命。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P057", "quote": "2）这其实就是为什么真正的fashion会多少有些“奇怪”的内在原因——击碎通兑性，可以对贪婪者达成自我鸡肋化，这是一重保护。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P062", "quote": "那就是把美感建立在意义之上。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P073", "quote": "1）每一件东西的选择，都要先有精神上的、实用上的理由。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P074", "quote": "2）这些东西的含义彼此之间要以你所赞同的方式互相协调。也就是选择逻辑要在你的价值观里自洽。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P080", "quote": "那些理由极少是因为好看。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P082", "quote": "实际上，是这些内在逻辑完全自洽的事物的组合定义出了一种美，而不是美学原则来指导了它们。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P090", "quote": "不是因为它猎奇或者有某种视觉刺激，而在于它有内在的、对于特定人群来说永恒的合理性。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P092", "quote": "——看得懂的人，有资格得到你的额外关注。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P077", "quote": "剑道服的袴（hakama)前面有五片折叠纹,象征着君臣之义,父子之亲,夫妻之别,长幼之序,朋友之信五伦道德,后面中间的一片折叠纹则代表精忠尽孝,决不二心。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P079", "quote": "这称为“粪扫衣”、“（百）衲衣”。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P064", "quote": "你们有没有听过婚礼的规矩？", "relation": "context"},
    {"key": "E37", "paragraph_id": "P065", "quote": "Something old, something new, something borrowed, something blue and a silver sixpence in your shoe.", "relation": "context"},
    {"key": "E38", "paragraph_id": "P093", "quote": "什么叫做「时尚」？", "relation": "context"},
    {"key": "E39", "paragraph_id": "P087", "quote": "相信我，在前一个议题得到高质量解决的前提下，视觉问题会变得容易得多。而且你一定会形成一个属于你的“构型”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["服饰与审美", "自我表达与人格", "人际关系与择友"],
   "issue_candidates": ["如何培养时尚感觉与品味", "审美评价标准的两种误区", "以穿着筛选交往对象", "通兑性审美与网红装"],
   "text_function_candidates": ["评论/论述", "指南", "训诫", "连载长文"],
   "object_candidates": ["剑道服（袴）", "佛教僧衣", "忍者装束", "欧洲婚礼惯例", "网红装"],
   "working_keywords": ["半透膜", "埋梗", "通兑性", "自我鸡肋化", "权界", "爱人的人", "贪婪的人", "构型", "fashion"]
  },
  "notes": "正文无图片节点。P093 末行含平台话题标签“女性相关答集”，与正文混排且未被 lexical 覆盖，已在 unresolved_questions 登记。brief 字段为正文摘录，仅作导航。"
 },
 "418def6a": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待类似「中国人的素质不如外国人的素质」的言论？”。作者没有直接评价该言论本身，而是提出一套解释框架：东方文明与西方文明在下意识层面存在“冒险可能会输/赢”的根本差别（P001），由此东方文明对风险估计不足抱有恐惧（P002），因而中国人对对手的评价系统性偏高（P004、P005），这种高估实为深刻的戒备和警惕（P003），常被误读为崇拜、谄媚、吹捧（P006），并被错误地归结为“民族自尊心”或“逆向民族主义”问题（P010）；作者另给出“友军评价偏低”的验证性证据（P011）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "提出文明差异命题：东方文明下意识认为“冒险可能会输”，西方文明下意识觉得“冒险可能会赢”；因此东方文明恐惧自己对风险估计不足，而西方人往往没意识到这种高估背后是深刻的戒备和警惕。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P004", "P005", "P006"],
     "summary": "推论：中国人倾向于认为对手比自己聪明强大（史书墓志铭的印象）；因此当中国人对你评价系统性偏高时，表示ta们内心深处觉得你对ta们有敌意；这常被不懂事的小孩子或西方人误认为“崇拜”“谄媚”“吹捧”。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P007", "P008", "P009"],
     "summary": "评断：因此“恨铁不成钢”者是不懂事，“飘飘欲仙”者是不知死活；中国成年人“谦虚”起来“谁说我好我跟谁急”。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P010"],
     "summary": "反驳问题框架：把这类现象当作“民族自尊心”或“逆向民族主义”问题只是没长大、拿西方人的眼镜看世界，问题问错了就找不到答案。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P011", "P012"],
     "summary": "给出验证性证据：ta们几乎从不会这样赞誉自己信赖的友军，友军普遍评价偏低；并以“你爹对你评价是不是就不高”反问作结。",
     "role": "reason"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出：东方文明和西方文明有一个根本差别——东方文明下意识会认为“冒险可能会输”，西方文明下意识会觉得“冒险可能会赢”。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称东方文明会下意识恐惧自己对风险估计不足，以致梦见敌人戏剧性大翻盘而惊醒。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为西方人往往没有意识到，这种（对对手的）高估背后其实是深刻的戒备和警惕。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称中国人总是倾向于认为对手比自己聪明和强大。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：当中国人普遍对你评价系统性偏高时，那表示ta们内心深处挥之不去地觉得你对ta们有敌意。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称这种评价常被不懂事的小孩子或者西方人误认为“崇拜”“谄媚”“吹捧”。",
     "evidence": ["E6"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定“恨铁不成钢”者是不懂事，“飘飘欲仙”者是不知死活。",
     "evidence": ["E7", "E8"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者描述中国成年人“谦虚”起来恨不得掏出枪来玩命、谁说好就跟谁急。",
     "evidence": ["E9"]
    },
    {
     "claim_id": "C009",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "作者转述并反驳的一种问题框架：把上述现象当作“民族自尊心”问题或“逆向民族主义”问题。",
     "evidence": ["E10"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出验证性证据：ta们几乎从不会这样赞誉自己信赖的友军，友军普遍评价偏低。",
     "evidence": ["E11"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者以反问作结：你爹对你评价是不是就不高？",
     "evidence": ["E12"]
    }
   ],
   "argument_steps": [
    "提出文明差异命题：东方下意识认为冒险可能输，西方下意识觉得冒险可能赢（P001）。",
    "推论东方文明恐惧对风险估计不足，而西方人未意识到高估背后的戒备与警惕（P002、P003）。",
    "推论中国人倾向高估对手（史书墓志铭的印象）（P004）。",
    "得出机制判断：中国人对你评价系统性偏高＝内心深处觉得你有敌意（P005），并指出常被误读为崇拜/谄媚/吹捧（P006）。",
    "对两类反应下判断：“恨铁不成钢”者不懂事，“飘飘欲仙”者不知死活（P007、P008）。",
    "以中国成年人“谦虚”的表现补充说明（P009）。",
    "否定提问可能采用的两种框架（民族自尊心、逆向民族主义），称其问错了问题（P010）。",
    "给出验证性证据（对友军评价普遍偏低），并以家庭关系的反问收束（P011、P012）。"
   ],
   "concept_usage": [
    {
     "term": "东方文明/西方文明",
     "meaning": "作者以“下意识”层面的风险预期差异来区分两大文明：一个认为冒险可能输，一个觉得冒险可能赢。",
     "evidence": "P001",
     "ambiguity": "两者范围、所指人群与依据均未界定，属高度概括的命题。"
    },
    {
     "term": "高估（评价系统性偏高）",
     "meaning": "中国人对对手（乃至外国人）的评价普遍偏高，作者称其实质是戒备与警惕。",
     "evidence": "P005",
     "ambiguity": "“系统性偏高”的判断标准与经验依据文中未给出。"
    },
    {
     "term": "民族自尊心/逆向民族主义",
     "meaning": "作者点名的两种错误问题框架，认为它们只是拿西方人的眼镜看世界。",
     "evidence": "P010",
     "ambiguity": "作者未定义这两个词，也未说明谁在这样使用；它们是被反驳的框架而非作者主张。"
    },
    {
     "term": "友军",
     "meaning": "作者用于验证“评价偏高＝敌意”的证据对象：被信赖的友军反而评价偏低。",
     "evidence": "P011",
     "ambiguity": "“友军”所指（盟国、同阵营者还是熟人）未说明。"
    }
   ],
   "examples_and_targets": [
    "中国史书上给对手们写的墓志铭：作者举例，并以“钢铁侠和绿巨人”作夸张修辞（P004）。",
    "“恨铁不成钢”者与“飘飘欲仙”者：作者评断的两类人（P007、P008）。",
    "中国成年人“谦虚”起来的表现：作者叙事举例（P009）。",
    "“民族自尊心”问题、“逆向民族主义”问题：作者反驳的问题框架（P010）。",
    "友军：作者提出的验证性证据对象（P011）。",
    "“你爹”：作者以家庭关系作反问的修辞材料（P012）。",
    "提问者所举「中国人的素质不如外国人的素质」的言论：提问者材料，正文未直接评价（Q001）。"
   ],
   "conditions": [
    "P001 以“下意识”为限定，作者称差别发生在下意识层面。",
    "P005 以“普遍对你评价系统性偏高的时候”为条件。",
    "P010 以“只是没长大，只是拿着西方人的眼镜看待世界的结果”作评断性归因。",
    "P011 “几乎从不会”为概率性限定。",
    "P012 以反问提出，未作断言。"
   ],
   "rhetoric_and_tone": "断言式短文，反讽与反问密集（“你明白为什么了吗？”“你爹对你评价是不是就不高？”）；口语俚语（“掏出枪来玩命”“谁说我好我跟谁急”“不懂事”“不知死活”）；漫画式夸张（钢铁侠、绿巨人）；直接否定提问可能采用的框架（“连问题都问错了”）。",
   "unresolved_questions": [
    "提问问“如何看待「中国人的素质不如外国人的素质」的言论”，正文未直接评价该言论本身，而是解释中国人评价偏高的机制，问答对应关系需研究者判断。",
    "“东方文明/西方文明”的范围、所指与依据本文未说明，属大跨度概括，需研究者谨慎对待。",
    "“中国史书上给对手们写的墓志铭”未举具体例证，需外部核查。",
    "P005、P011 中“ta们”的具体所指（中国人、对手或其他）存在歧义，需按上下文理解。",
    "“你爹对你评价是不是就不高”为反问式例证，能否推广到一般家庭关系，本文未说明。",
    "作者未给出任何数据或文献支持“评价系统性偏高”“友军评价偏低”的判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "东方文明和西方文明有一个根本的差别，就是东方文明下意识会认为“冒险可能会输”，而西方文明下意识会觉得“冒险可能会赢”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因此，东方文明会下意识的恐惧自己对风险估计不足", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "所以西方人往往没有意识到，这种高估背后其实是深刻的戒备和警惕。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "中国人总是倾向于认为对手比自己聪明和强大", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "所以当中国人普遍对你评价系统性偏高的时候，那表示ta们在内心深处挥之不去的觉得你对ta们有敌意。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这常常被不懂事的小孩子或者西方人误认为是一种“崇拜”，一种“谄媚”，一种“吹捧”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "因此“恨铁不成钢”者，是不懂事。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "因此飘飘欲仙者，是不知死活。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "中国成年人“谦虚”起来恨不得掏出枪来玩命，谁说我好我跟谁急。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "以为这是什么“民族自尊心”问题或者“逆向民族主义”问题，只是没长大，只是拿着西方人的眼镜看待世界的结果。", "relation": "contradicts"},
    {"key": "E11", "paragraph_id": "P011", "quote": "给你们个验证性证据——ta们几乎从不会这样赞誉自己信赖的友军。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "你爹对你评价是不是就不高？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文化比较", "国民心态", "国际认知"],
   "issue_candidates": ["中国人的素质不如外国人论", "对对手评价偏高的机制", "民族自尊心/逆向民族主义框架之争"],
   "text_function_candidates": ["评论", "解释", "反驳"],
   "object_candidates": ["东方文明", "西方文明", "中国人", "史书墓志铭", "友军"],
   "working_keywords": ["冒险可能会输", "冒险可能会赢", "高估", "戒备和警惕", "逆向民族主义", "恨铁不成钢"]
  },
  "notes": "正文无图片节点；正文与 lexical 无差异。正文未直接回应提问所指言论本身，已在 unresolved_questions 登记。"
 },
 "33b07cf1": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待新冠肺炎期间全网开始怼钉钉?”。作者不从舆情或产品功能入手，而是从劳资关系与技术手段的角度论证：对抗“被侵犯个人时间”不能靠消灭通信工具（P001-P003），钉钉只是与电报、电话、互联网等同类技术（P005）；这些技术虽让老板抓得更紧，却也让更多人当老板更容易、带来更多工作机会（P008），而工作机会才是劳动者对抗老板的唯一本钱（P009）；在没有这些技术的时代老板同样叫得到你（P010-P013）；因此钉钉战术上让劳动者痛苦、战略上有利（P018），并斥责因疫情不能到校而抱怨钉钉的学生没有持有观点的资格（P019、P020）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "开篇判断与类比：对抗“被侵犯个人时间”不可能靠消灭通信工具，否则应把电话一起丢掉；老板能用钉钉做到的，用电话同样能做到（连串反问）。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P004", "P005", "P006", "P007"],
     "summary": "转述并反驳“钉钉的罪恶是把摆脱不了的奴役关系变得更频繁深入”的批评：电报、电话、传真机、复印机、打印机、汽车、火车、电子邮件、互联网都在扮演同样角色；没有它们老板更压迫不到你，为何不反对它们。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P008", "P009"],
     "summary": "正面理由：这些技术固然让老板抓你更紧，但也让更多人当老板更容易，能带来更多企业、团队与工作机会；更多工作机会才是对抗老板的唯一本钱。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P010", "P011", "P012", "P013"],
     "summary": "历史反证：在没有这些技术手段的时代，老板并不会叫不到你——劳动者要自己求人收留、住柴房拉磨当长工或进集体宿舍三班倒卖命。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P014", "P015", "P016", "P017"],
     "summary": "条件性论断：只要你需要工作、只要背后没有触手可及的跳槽机会，就不要妄想老板叫不到你、不要指望老板尊重你的劳动时间（不管立什么法），因为是你自己在通过放弃这些“权利”为自己求保险；并以“老板只叫别人不叫你”的反问加强。",
     "role": "qualification"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P018", "P019", "P020", "P021"],
     "summary": "结论与训斥：钉钉的发明战术上让你痛苦、战略上对你有利；因疫情不能到校而抱怨钉钉的学生没有持有观点的资格（除非认为蚂蚁跟着甜味爬也是观点），那是家庭教育失败的表征、loser 的表征；生活是“敬酒不吃吃罚酒”的游戏。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者断言：想要对抗“被侵犯个人时间”，不可能靠消灭通信工具的方式，否则应该把电话一起丢掉。",
     "evidence": ["E1", "E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称老板能用钉钉做到的事，用电话同样能做到。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C003",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "questioned",
     "statement": "作者转述的批评意见（以“是吧？”反问形式）：钉钉的“罪恶”是把这种你摆脱不了的“奴役关系”变得更频繁深入了。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者列举电报、电话、传真机、复印机、打印机、汽车、火车、电子邮件、互联网，称它们都在扮演同样的角色。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称这些技术固然让老板抓你更紧，但也让更多人当起老板来更容易，能让世界上有更多企业、更多团队、更多工作机会。",
     "evidence": ["E6"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：更多工作机会才是你对抗老板的唯一本钱。",
     "evidence": ["E7"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以历史反证：在没有这些技术手段的时代，劳动者要自己求人收留、住前院柴房拉磨当长工或进集体宿舍三班倒卖命，老板并不会因缺少技术手段就叫不到你。",
     "evidence": ["E8", "E16"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“只要你需要工作，无论什么时代，无论什么技术条件”为条件，称不要妄想老板会叫不到你。",
     "evidence": ["E9"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“只要你背后没有别的跳槽机会触手可及”为条件，称不要指望老板会尊重你的劳动时间，不管你立什么法。",
     "evidence": ["E10"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者解释原因：是你自己在通过放弃这些“权利”为没有其他退路的自己求保险。",
     "evidence": ["E11"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者结论：钉钉的发明战术上让你痛苦，但战略上对你有利。",
     "evidence": ["E12"]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称那些因疫情不能到校、觉得钉钉搅合了长假美梦的学生没有持有观点的资格。",
     "evidence": ["E13"]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者称那只是家庭教育失败的效果大爆发、是 loser 的表征，将来自有一件接一件的残酷事教ta们做人。",
     "evidence": ["E14"]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以俗语收束：生活是一种“敬酒不吃吃罚酒”的游戏。",
     "evidence": ["E15"]
    }
   ],
   "argument_steps": [
    "提出判断：对抗被侵犯个人时间不能靠消灭通信工具（P001、P002）。",
    "以连串反问指出电话与钉钉功能等价（P003）。",
    "转述“钉钉加深奴役关系”的批评（P004），并以电报、电话、互联网等同类技术反问反驳（P005、P006、P007）。",
    "提出正面理由：技术让老板抓得更紧，也让更多人当老板更容易、创造更多工作机会（P008），而工作机会是唯一本钱（P009）。",
    "以历史情境内反驳“没有技术就自由”：无技术时代劳动者仍需上门求工（P010-P013）。",
    "给出条件性普遍论断：只要需要工作、没有跳槽机会，老板就能叫到你、不必尊重你的劳动时间（P014、P015），因为这是劳动者自我求保险（P016、P017）。",
    "得出结论：钉钉战术上痛苦、战略上有利（P018）。",
    "训斥抱怨钉钉的学生，并以“敬酒不吃吃罚酒”收束（P019-P021）。"
   ],
   "concept_usage": [
    {
     "term": "钉钉",
     "meaning": "本文把它作为办公通信工具的一般代表，与电报、电话、互联网等并列，而非单独评价其产品设计。",
     "evidence": "P005",
     "ambiguity": "文中未提及钉钉在疫情期间的具体功能（如线上上课），提问所指的“全网怼钉钉”语境未展开。"
    },
    {
     "term": "奴役关系",
     "meaning": "带引号使用，指作者转述的批评者所说的、劳动者摆脱不了的被支配关系。",
     "evidence": "P004",
     "ambiguity": "作者是否认可该词所指的关系，文中未明说。"
    },
    {
     "term": "权利",
     "meaning": "带引号使用，指劳动者放弃以换取保险的“权利”（如不被随时叫到）。",
     "evidence": "P016",
     "ambiguity": "引号表明作者对其正当性存疑，具体所指未定义。"
    },
    {
     "term": "唯一本钱",
     "meaning": "作者称更多工作机会是劳动者对抗老板的唯一依仗。",
     "evidence": "P009",
     "ambiguity": "“唯一”为绝对化表述，文中未论证是否还有其它依仗（如法律、技能、组织）。"
    },
    {
     "term": "战术/战略",
     "meaning": "作者评价钉钉的两个层次：战术上使劳动者痛苦，战略上对劳动者有利。",
     "evidence": "P018",
     "ambiguity": "未说明“战略有利”的时间尺度与受益机制细节。"
    }
   ],
   "examples_and_targets": [
    "钉钉：提问所指的讨论对象（Q001、P004、P018）。",
    "电话、短信、电报、传真机、复印机、打印机、汽车、火车、电子邮件、互联网：作者并列举例的技术手段（P003、P005）。",
    "前院柴房拉磨当长工、集体宿舍大通铺一天三班倒：作者对无技术时代劳动境况的叙事（P012）。",
    "抖音：作者用于反问的修辞材料（P017）。",
    "因疫情不能到校的学生：作者训斥的对象（P019、P020）。",
    "“蚂蚁跟着甜味爬”：作者贬低学生意见的类比（P019）。",
    "“敬酒不吃吃罚酒”：作者引用的俗语（P021）。"
   ],
   "conditions": [
    "P014 “只要你需要工作，无论什么时代，无论什么技术条件”。",
    "P015 “只要你背后没有别的跳槽机会触手可及……不管你立什么法”。",
    "P010 “在上面那些东西都没有的时代”为假设性反问条件。",
    "P019 “除非你认为蚂蚁跟着甜味爬也是一种观点”为反讽式例外条件。",
    "P004 以“是吧？”的反问形式转述流行批评，非作者主张。"
   ],
   "rhetoric_and_tone": "第二人称训斥体：连续反问（P003 五连问、P005-P007、P010、P013、P017）与自答（“你错了！”）；口语化贬斥（“loser”“醒一醒吧”）；命令与劝导混杂（“你要自己乖乖的……”）；以俗语作结（“敬酒不吃吃罚酒”）；对特定群体（学生）下贬抑判断。",
   "unresolved_questions": [
    "提问为“如何看待新冠肺炎期间全网开始怼钉钉”，正文未叙述该舆情经过，也未提及钉钉在疫情中的具体功能（如线上授课），仅从劳资与技术角度论证；问答对应关系需研究者判断。",
    "P019“没有持有观点的资格”的判定依据与所指学生范围，本文未说明。",
    "P004“奴役关系”、P016“权利”均带引号，作者是否认可这些说法需研究者判断。",
    "“更多工作机会”等论断未给出数据或来源，需外部核查。",
    "作者身份、是否使用钉钉、是否身处疫情相关行业，本文未说明。",
    "平台话题标签未见；正文与 lexical 无差异。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "想要对抗“被侵犯个人时间”，不可能靠消灭通信工具的方式。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "否则你应该把你的电话一起丢掉。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "老板能用钉钉做到的，哪一样不能用电话做到？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "钉钉的“罪恶”是把这种你摆脱不了的“奴役关系”变得更频繁深入了，是吧？", "relation": "context"},
    {"key": "E5", "paragraph_id": "P005", "quote": "问题是，电报、电话、传真机、复印机、打印机、汽车、火车、电子邮件、互联网……哪个不是在扮演同样的角色？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "这些东西固然能让老板抓你更紧，但也让更多人当起老板来更容易。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "更多工作机会才是你对抗老板的唯一本钱！", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "你要自己乖乖的、求爷爷告奶奶的、求上门去看人肯不肯收你住在前院柴房里让你拉磨当长工。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "只要你需要工作，无论什么时代，无论什么技术条件，你都不要妄想老板会叫不到你。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P015", "quote": "只要你背后没有别的跳槽机会触手可及，你就不要指望老板会尊重你的劳动时间——不管你立什么法。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P016", "quote": "因为是你自己在通过放弃这些“权利”为没有其他退路的自己求保险。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "钉钉的发明，战术上让你痛苦，但是战略上对你有利！", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "至于那些因为疫情不能到校觉得钉钉搅合了他们长假美梦的学生，ta们没有持有观点的资格", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "那只是家庭教育失败的效果大爆发罢了——这都是些loser的表征", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "醒一醒吧！生活是一种“敬酒不吃吃罚酒”的游戏！", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "你看那时候老板们是不是会因为缺少技术手段就叫不到你？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["劳动与雇佣关系", "通信技术与工作", "网络舆情"],
   "issue_candidates": ["疫情期钉钉被批", "工作时间的边界", "通信工具与劳动控制", "工作机会与议价能力"],
   "text_function_candidates": ["评论", "论辩", "训诫"],
   "object_candidates": ["钉钉", "老板", "学生", "电报、电话、传真机、互联网等技术", "抖音"],
   "working_keywords": ["奴役关系", "个人时间", "劳动时间", "唯一本钱", "跳槽机会", "战术/战略", "敬酒不吃吃罚酒"]
  },
  "notes": "正文无图片节点；正文与 lexical 无差异。正文未展开提问所指“全网怼钉钉”的舆情经过，已在 unresolved_questions 登记。"
 },
 "208c5abc": {
  "analysis": {
   "question_context": "提问者（Q001）请作者介绍“各种调味料的基本用法以及搭配方法”。作者没有逐一介绍调味料，而是给出一个“基本思路”（P001）：现今调味料工业由专业研发中心以简化流程、标准化调味为中心开发复合调味料，供大型连锁餐厅降本提效（P002-P004）；连锁餐厅委托大厂研发专利调料包，并通常自建菜谱网站推广自研产品（P005-P007）；作者举例列出几个菜谱网站（P008），并称对没学过烹饪的普通人，活用这个工具已能做出镇住场面的大菜（P009），最后以“了解你的时代，你才能活在你的时代”收束（P010）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "开篇给出思路定位：一个基本思路足以解决烹饪苦手所面临的绝大多数调味问题。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003", "P004"],
     "summary": "描述调味料工业现状：专业研发中心以简化作业流程、标准化调味为中心思想开发专业复合调味料，帮助大型连锁餐厅降低成本、提高效率；很多连锁餐厅直接使用这些方案。",
     "role": "context"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P005", "P006"],
     "summary": "说明产业链作法：连锁餐厅拿出经典菜委托某家大厂代为研究专利调料包（一碗面开一包、一只鸭淋一包）；厂商一般会开发菜谱网站推广自研产品，而委托产品属客户机密。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P007", "P008"],
     "summary": "以“例如”列出菜谱网站：联合利华饮食策划、太太乐、厨邦美食；该段（P008）在 text 中存在但未被 lexical 结构覆盖。",
     "role": "example"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P009", "P010"],
     "summary": "结论：对没学过烹饪的普通人，活用这个工具已可以做出不少能镇住场面的大菜；了解你的时代，你才能活在你的时代。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称给出一个基本思路，足以解决烹饪苦手所面临的绝大多数调味问题。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称现在的调味料工业由专业研发中心以简化作业流程、标准化调味为中心思想开发各类专业复合调味料，以帮助大型连锁餐厅降低成本和提高效率。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称很多连锁餐厅直接使用这些方案，并拿出自己的经典菜委托某家大厂代为研究专利调料包。",
     "evidence": ["E3", "E4"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称这些企业一般都会开发某种菜谱网站推广自研产品，而委托产品是客户机密。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者举例列出联合利华饮食策划、太太乐、厨邦美食等菜谱网站，并称对没学过烹饪的普通人，活用这个工具已可以做出不少能镇住场面的大菜。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以格言式表述收束：了解你的时代，你才能活在你的时代。",
     "evidence": ["E8"]
    }
   ],
   "argument_steps": [
    "给出总体判断：一个基本思路即可解决绝大多数调味问题（P001）。",
    "描述调味料工业的现状与动机（简化流程、标准化调味、降本提效）（P002-P004）。",
    "说明连锁餐厅委托大厂研发专利调料包、并自建菜谱网站推广自研产品（P005、P006）。",
    "以“例如”列出具体菜谱网站（P007、P008）。",
    "得出结论：普通人活用这一工具即可做出大菜，并归结为“了解你的时代”（P009、P010）。"
   ],
   "concept_usage": [
    {
     "term": "专业复合调味料",
     "meaning": "由专业研发中心以简化作业流程、标准化调味为中心思想开发、面向大型连锁餐厅的调味产品。",
     "evidence": "P003",
     "ambiguity": "具体成分、与家用调味料的关系，文中未说明。"
    },
    {
     "term": "专利调料包",
     "meaning": "连锁餐厅委托大厂代为研究的、对应其经典菜的调料包（一碗面一包、一只鸭一包）。",
     "evidence": "P005",
     "ambiguity": "“专利”具体指配方专利还是商业机密，文中未区分。"
    },
    {
     "term": "菜谱网站",
     "meaning": "调味料企业为推广自研产品而开发的网站，作者建议普通人以此解决调味问题。",
     "evidence": "P006",
     "ambiguity": "作者未说明这些站点内容的可靠性与适用条件。"
    },
    {
     "term": "烹饪苦手",
     "meaning": "作者设定的目标读者：没学过烹饪、调味有困难的普通人。",
     "evidence": "P001",
     "ambiguity": "与 P009“没学过烹饪的普通人”为同一对象，文中未给界定。"
    }
   ],
   "examples_and_targets": [
    "联合利华饮食策划-专业厨师掌上菜谱库网站：作者举例的菜谱网站（P008）。",
    "太太乐（含太太乐鸡精官网）：作者举例的菜谱网站（P008）。",
    "厨邦美食：作者举例的菜谱网站（P008）。",
    "大型连锁餐厅、专业研发中心、某家大厂：作者所述产业链主体（P003-P006）。",
    "“一碗面直接开一包，一只鸭直接淋一包”：作者对调料包用法的举例（P005）。",
    "提问者所问“各种调味料的基本用法以及搭配方法”：提问者材料，正文未逐项介绍（Q001）。"
   ],
   "conditions": [
    "P001 以“绝大多数调味问题”为限定，非全部。",
    "P006 “一般都会开发某种菜谱网站”为概率限定。",
    "P006 括号内“（委托产品是客户机密）”为补充限定。",
    "P009 以“对没学过烹饪的普通人”为对象限定。"
   ],
   "rhetoric_and_tone": "极简说明体，口语化开场（“给你们一个基本思路”“现在的调味料工业是这个样子的”）；不给具体配方，而是把读者导向工业化的复合调味料与厂商菜谱网站；以“例如”直接排列网站标题（P008 呈链接式文本）；结尾用格言式短句收束。",
   "unresolved_questions": [
    "提问请作者介绍各种调味料的基本用法与搭配方法，正文未逐一介绍，而是建议使用厂商复合调味料与菜谱网站；问答对应关系需研究者判断。",
    "P008（联合利华饮食策划、太太乐、厨邦美食等标题）在 text 中存在但未被 lexical 结构覆盖（阅读包登记 text_has_content_not_in_lexical @212），原文此处疑为链接列表，链接地址未保留。",
    "P005“某家大厂”未具名，委托关系无法核查。",
    "文中未说明这些菜谱网站于写作时点是否仍可用，需外部核查。",
    "“了解你的时代，你才能活在你的时代”未展开，属格言式表述。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "给你们一个基本思路，足以解决烹饪苦手所面临的绝大多数调味问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "由专业的研发中心以简化作业流程、标准化调味为中心思想开发各类专业复合调味料，以帮助大型连锁餐厅降低成本和提高效率。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "很多连锁餐厅直接用的就是这些方案。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "它们拿出自己的经典菜来，委托某家大厂代为研究专利调料包。一碗面直接开一包，一只鸭直接淋一包。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "而它们一般都会开发某种菜谱网站推广它们的自研产品。（委托产品是客户机密）", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "联合利华饮食策划-专业厨师掌上菜谱库网站", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "对没学过烹饪的普通人，活用这个工具已经可以做出不少可以镇住场面的大菜了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "了解你的时代，你才能活在你的时代。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["烹饪与调味", "食品工业", "餐饮连锁"],
   "issue_candidates": ["调味料的用法与搭配", "复合调味料与标准化", "厂商菜谱网站的利用"],
   "text_function_candidates": ["答疑（以思路代替清单）", "经验介绍"],
   "object_candidates": ["联合利华饮食策划", "太太乐", "厨邦美食", "大型连锁餐厅", "专业研发中心", "某家大厂"],
   "working_keywords": ["复合调味料", "专利调料包", "标准化调味", "菜谱网站", "烹饪苦手"]
  },
  "notes": "正文无图片节点。P008 的网站标题在 text 中存在但 lexical 未覆盖，已在 unresolved_questions 登记。正文仅 321 字，未提供调味料搭配清单。"
 },
 "328789e0": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何应对他人的捧杀？”。作者先铺陈中国“本质精英制”的文化背景与权力诱惑（P002-P017），再给出答案的前半部分：真正从权位中解脱的基本原则是不仅不争取还要避之不及（P019），只有在退无可退时才可忍受权力重负（P020）；其核心机制是——若真心不恋权位，捧杀即对你无效（P022、P026）；但作者随即指出，这种“决心”若只是出于对“杀”的恐惧，就靠不住（P028-P032），并以“为什么追求权力就一定有害、为什么我不能是少数例外”的未答问题与“（未完，待续）”结束（P033、P034）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "开场回应提问：这个问题问得非常好，作者要好好答一答。",
     "role": "transition"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007", "P008"],
     "summary": "铺陈文化背景：中国是本质精英制社会，文化基因深处给精英预留宝座；列举唯才是举、选贤任能等说法，并称整个中华文明只有老子唱反调，随后以庄子、杜甫、陶渊明、碧桂园等典故调侃；最后回到“外儒内法，士大夫为万般最高”与名利许诺。",
     "role": "context"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"],
     "summary": "描述权力机制的代价与诱惑：谁高分谁能、谁能谁话事、谁话事谁负全责并在必然失败里被献祭；用“食得盐就要抵得渴”说明代价，连番追问读者是否想清楚、是否要学“食得盐而不必挨渴的妙计”，并以“你想好了，再往下看”设下阅读门槛。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P018"],
     "summary": "声明后文只写给真打算从其中解脱的人，勉强假装者后果自负。",
     "role": "qualification"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P019", "P020", "P021"],
     "summary": "给出基本原则与唯一可忍受权力的前提：任何一种权位不但不积极争取、还要避之不及；只有一切有意愿且大众愿意接受的人都不存在、你退无可退时，才可忍受权力的重负。",
     "role": "claim"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"],
     "summary": "说明捧杀为何无效：若真心不恋权位（是再三推辞避让而不可得才临时顶替、毫无恋栈意图、没有贪婪），权力对你没有“杀气”，捧杀即无效；作者以第一人称自述“真闲云野鹤”、承诺谁想坐这位子只管开口、能说服成员接受便让位，因此无人需为此“杀”他，他亦不必猜疑。",
     "role": "reason"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032"],
     "summary": "反转与反驳：真正的关窍在于如何不勉强、不纠结地真有这个决心；作者称读者“上当了”，因为这个 mindset 不能是出于愿望的“决心”，只能是自然的认知、对“追求权力是有毒的、是坏的”充满论证与依据的信服；若只是怕“杀”而躲捧，顺境时就会因自信不怕杀而不拒捧，而这种顺境几乎必然到来，所以所谓的“决心”靠不住。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": ["P033", "P034"],
     "summary": "以未答问题收尾：为什么追求权力一定有害？历史上声威赫赫者并非个个不得好死、很多人名垂青史，为什么我不能是少数例外？末行注明“（未完，待续）”。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称中国是一个本质精英制的社会，天然从文化基因的深处本能地给精英预留了宝座。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称整个中华文明只有老子喊“绝圣弃智”“不尚贤使民不争”，并以诗文典故调侃这类隐逸姿态。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者概括权力机制：谁高分谁就能、谁能谁话事、谁话事谁负全责，谁负全责谁就在必然到来的、人算不如天算的失败里被献祭。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以俗语说明代价：你要食得盐，你就要抵得渴。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出解脱的基本原则：任何一种权位，不但不去积极争取，而且还要避之不及。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者提出只有一种前提可以忍受权力的重负：一切有意愿而大众又愿意接受的人都已经不存在、退无可退、再不接受会有你付出生命也不愿看到的后果发生。",
     "evidence": ["E6"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者称若你真心实意是这样的想法，捧杀对你就已经无效了——因为你是再三推辞避让而不可得才临时顶替、毫无恋栈意图、没有贪婪，权力对你没有那份“杀气”。",
     "evidence": ["E7"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以第一人称自述立场：不是假装闲云野鹤走终南捷径，而是真闲云野鹤自得其乐，是应你们之请才勉为其难；谁想坐这个位置只管开口，只要能说服组织成员接受，铁定让位。",
     "evidence": ["E8", "E17"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称只要你真的“下了这决心”，就已经对“捧杀”免疫；而真正的关窍在于如何不勉强、不纠结、坦坦荡荡、真实地有这个“决心”。",
     "evidence": ["E9", "E10"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定读者“上当了”：这个 mindset 不可以是出于愿望而下的“决心”，只能是自然的认知、一种对“追求权力是有毒的，是坏的”的充满论证和依据的信服。",
     "evidence": ["E11"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预言若只是因害怕“捧”背后的“杀”而下意识躲着捧，则顺境到来时会因自信不怕杀而不拒捧，而这种顺境几乎必然到来，所以所谓的“决心”是靠不住的。",
     "evidence": ["E12", "E13", "E14"]
    },
    {
     "claim_id": "C012",
     "claim_type": "open_question",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者在文末提出未答的问题：为什么“追求权力”就一定“有害”？历史上声威赫赫之人并非个个不得好死、很多人名垂青史，为什么我不能是那个少数例外？",
     "evidence": ["E15", "E16"]
    }
   ],
   "argument_steps": [
    "回应提问，表示要认真作答（P001）。",
    "铺陈文化背景：本质精英制社会给精英预留宝座，仅老子唱反调（P002-P008）。",
    "说明权力机制的代价：负全责者终被献祭（P009），并用“食得盐抵得渴”点出代价（P010）。",
    "以连番追问施压：能不能吃这盐、是否想好、是否要学“食得盐而不必挨渴的妙计”（P011-P016）。",
    "设定阅读门槛：后文只写给真打算解脱的人，假装者后果自负（P017、P018）。",
    "给出基本原则（不争取且避之不及）与唯一可忍受权力的前提（P019、P020）。",
    "说明捧杀无效的机制，并以第一人称自述其“让位”立场（P021-P026）。",
    "反转：决心不能出于愿望而只能是自然的认知，否则顺境一来就会不拒捧（P027-P032）。",
    "以未答的核心问题与“（未完，待续）”结束（P033、P034）。"
   ],
   "concept_usage": [
    {
     "term": "捧杀",
     "meaning": "本文未给出定义，而是把它放在“权力—责任—献祭”的框架中解释：被捧者对权力的贪婪使“捧”背后的“杀”生效。",
     "evidence": "P022",
     "ambiguity": "未定义、未举例，问答之间的概念对应关系需研究者判断。"
    },
    {
     "term": "本质精英制",
     "meaning": "作者对中国社会的概括：文化基因深处本能地给精英预留宝座。",
     "evidence": "P002",
     "ambiguity": "为宏大论断，未给出界定与依据。"
    },
    {
     "term": "权位/权力",
     "meaning": "作者主张不积极争取且避之不及的对象；文中谈其“重负”“杀气”与让位问题。",
     "evidence": "P019",
     "ambiguity": "权力的范围（政治权力、组织职位或一般支配关系）未界定。"
    },
    {
     "term": "决心（vs 自然的认知）",
     "meaning": "作者区分：出于愿望而下的“决心”靠不住；只有对“追求权力有毒”的充满论证与依据的信服（自然的认知）才有效。",
     "evidence": "P029",
     "ambiguity": "如何区分二者、如何形成“自然的认知”，本文未给出方法。"
    },
    {
     "term": "mindset",
     "meaning": "文中英文词，指上述面对权力与捧杀的心态。",
     "evidence": "P029",
     "ambiguity": "中英混用，未定义。"
    },
    {
     "term": "彀中",
     "meaning": "作者形容天下英雄都跳不出的圈套。",
     "evidence": "P008",
     "ambiguity": "典故式用法，未展开。"
    },
    {
     "term": "食得盐，抵得渴",
     "meaning": "粤语式俗语，作者用来说明享受权力收益必须承受相应代价。",
     "evidence": "P010",
     "ambiguity": "未解释该俗语的字面义。"
    },
    {
     "term": "终南捷径",
     "meaning": "典故，指假装隐居以求仕进；作者以此否定自己的动机。",
     "evidence": "P023",
     "ambiguity": "未展开典故来源。"
    }
   ],
   "examples_and_targets": [
    "老子及其“绝圣弃智”“不尚贤使民不争”：作者提及并调侃（P004）。",
    "庄子“子非鱼安知鱼之乐”、杜甫“三重茅”“安得广厦千万间”、陶渊明“采菊东篱下”：作者以诗文典故调侃（P004、P005）。",
    "碧桂园：作者以“去为碧桂园带盐（代言）”作讽刺材料（P004）。",
    "“书中自有黄金屋/千钟粟”、林徽因、阮玲玉：作者改写引用的名利许诺（P007）。",
    "冯唐、李广：作者引典故说明名臣良将的际遇（P008）。",
    "白玉堂、黄金屋、千钟粟、颜如玉：作者列举被追逐的权力收益（P012）。",
    "闲云野鹤、终南捷径：作者自述立场的典故（P023）。",
    "历史上声威赫赫之人、名垂青史者：作者在 P033 提出但未展开的反例。"
   ],
   "conditions": [
    "P018 限定后文读者：只有真打算从其中解脱的人能用，勉强假装没有意义，后果自负。",
    "P020 以“只有一种前提”限定可忍受权力重负的情形。",
    "P022 以“你真心实意是这样的想法”为捧杀无效的条件。",
    "P023 “只要你能有机会说服的了这组织里的成员接受你，我铁定让位”。",
    "P026 以“只要你真的‘下了这决心’”为免疫条件。",
    "P030 以“如果你不是出于什么原因真的是这样想的”为假设条件。",
    "P033 三个反问提出后未作答，文末标注“（未完，待续）”。"
   ],
   "rhetoric_and_tone": "文言化与骈偶、典故密集（唯才是举/选贤任能/陈力就列；冯唐易老、李广难封；终南捷径；采菊东篱下），夹杂网络式调侃（“鬼才想知道你有多乐”“去为碧桂园带盐”）；自称“老衲”“我”，以连番追问向读者施压（“你真的想好了吗？”）；先后设阅读门槛（“后果只能自负，勿谓言之不预也”）；以“（未完，待续）”收尾。",
   "unresolved_questions": [
    "正文以“（未完，待续）”结束（P034），P033 提出的核心问题（为什么追求权力一定有害、为何不能是少数例外）未回答，本篇属未完成文本。",
    "“捧杀”在本文中未定义、未举例，与提问所问“他人的捧杀”的对应关系需研究者判断。",
    "作者以第一人称自述其权位、让位承诺与所在组织（P023），其身份与所指组织本文未说明。",
    "大量典故（老子、庄子、杜甫、陶渊明、冯唐、李广、终南捷径等）为修辞引用，未给出来源版本。",
    "“中国是一个本质精英制的社会”为宏大论断，未给出依据，需研究者谨慎对待。",
    "是否存在续篇或后续更新，本语料未收录。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "中国是一个本质精英制的社会，天然从文化基因的深处就本能的给精英预留了宝座。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "整个中华文明，就只有老子喊绝圣弃智大道乃绝，不尚贤使民不争。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P009", "quote": "谁高分，谁就能，谁能，谁话事，谁话事，谁就要负全责。谁负全责，谁就在必然到来的、人算不如天算的失败里被献祭。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "你要食得盐，你就要抵得渴。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P019", "quote": "就是一个基本原则——任何一种权位，不但不去积极争取，而且还要避之不及。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P020", "quote": "只有一种前提，你可以忍受权力的重负——一切有意愿而大众又愿意接受的人都已经不存在了，你已经退无可退", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P022", "quote": "其实，你真心实意是这样的想法，捧杀对你就已经无效了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P023", "quote": "我不是假装闲云野鹤要去走终南捷径，我是真闲云野鹤自得其乐。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P026", "quote": "所以，只要你真的“下了这决心”，你就已经对“捧杀”免疫了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P027", "quote": "真正的关窍在于——你如何能不勉强的、不纠结的、坦坦荡荡的、真实的有这个“决心”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P029", "quote": "因为这个mindset根本就不可以是一种处于愿望而下的“决心”，而只能是一种自然的认知。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P030", "quote": "如果你不是出于什么原因真的是这样想的，只是因为害怕“捧”背后的“杀”而下意识的躲着捧，那么等你风调雨顺、觉得天下无事不可为的顺境时，你就会因为自信不怕杀而不拒捧。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P031", "quote": "而这种顺境，几乎因为你在内心深处对被捧的渴望压倒对杀的恐惧而必然到来。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P032", "quote": "你那个所谓的“决心”是靠不住的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P033", "quote": "为什么我就不可以是那个少数例外呢？", "relation": "context"},
    {"key": "E16", "paragraph_id": "P034", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E17", "paragraph_id": "P023", "quote": "你们谁想坐我这个位置，只管开口，我必然给你一切的机会甚至帮助", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治文化", "权力与责任", "人生策略"],
   "issue_candidates": ["如何应对捧杀", "权位的代价与献祭", "让位与不恋权位", "决心与自然认知之别"],
   "text_function_candidates": ["评论", "论辩", "训诫（含未完成篇章）"],
   "object_candidates": ["中国社会/中华文明", "老子", "庄子", "杜甫", "陶渊明", "冯唐", "李广", "碧桂园", "组织（未具名）"],
   "working_keywords": ["捧杀", "本质精英制", "权位", "避之不及", "杀气", "mindset", "自然的认知", "终南捷径", "食得盐抵得渴"]
  },
  "notes": "正文无图片节点；正文与 lexical 无差异。P034“（未完，待续）”表明本篇未完成，P033 的核心问题未作答，已在 unresolved_questions 登记。"
 },
 "f2c3a70c": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何反驳道德虚无主义者？”。作者的回答是否定这一问法本身：道德虚无主义者不能用“反驳”对待（P001），因为逻辑自洽的体系对外部反驳免疫（P002），只能靠对方自己痛苦到愿意凭 faith 跨越“没有充分证据”的鸿沟（P003-P005）；随后作者用大量篇幅描述道德虚无主义者的痛苦与处境（无价值无目的、畏难而退、亲密关系消亡、与异类互相放逐、与同类不能相容、成为“关系冲浪者”、终将耗尽体力），并指出有人靠资源“买麻醉剂”麻醉这份痛苦，这部分“完全没得反驳”（P006-P015）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "直接否定提问方式：道德虚无主义者不能用“反驳”这种方式去对待。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003"],
     "summary": "给出理由：他们的逻辑是自洽的，凡逻辑自洽的意识形态体系用外部“反驳”都没有用，对方有无穷预备答案；应敬畏对方的智力，他们是验算过千百遍、确信这是安全外壳才选择的最后栖身之所。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P004", "P005"],
     "summary": "说明可能的出路：只有对方自己想突破而力所不能及、向你发出求救信号，在内外合作下靠 leap of faith 完成；且只能靠ta自己有足够痛苦、有被痛苦驱动的强烈意愿，凭 faith 跨越“没有充分证据”的鸿沟。",
     "role": "qualification"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P006", "P007"],
     "summary": "分析道德虚无主义的痛苦：生活没有价值、人生没有目的，因而难以承受较大现实困难、难以做成略有挑战的事，遇到困难时避免困难成了唾手可得的利益；他们容易来回打转、亲密关系因畏难而退消亡，落入终极孤寂。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"],
     "summary": "描述其关系处境：与异类互相放逐（非虚无主义者发现他们后选择有限，他们遇压力损失时断尾逃生，难以被原谅）；与同类更彼此不能容忍（最大情谊不过隔空点赞）；于是成为“关系冲浪者”狼狈划水，终将耗尽体力，因为他们不能甘受那份应分的寂寞，而寂静无声的未来就是那个痛苦。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P014", "P015"],
     "summary": "例外与收束：很多人“幸运”地有足够资源买麻醉剂麻醉那个痛苦，有人靠变卖祖产达到“麻醉剂自由”；这个就完全没得“反驳”了。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者断言：道德虚无主义者不能用“反驳”这种方式去对待。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称他们的逻辑是自洽的；凡是逻辑自洽的意识形态体系，用外部的“反驳”都没有用，对方自然有无穷的预备答案。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张要敬畏对方的智力：他们自己验算过千百遍，确信这是安全的外壳，才选择作为最后一个栖身之所。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称这个循环只有在对方自己想突破而力所不能及、向你发出求救信号时，才能在你和他的内外合作之下靠 leap of faith 完成。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称这只能靠ta自己有足够的痛苦、不愿再继续这么过下去，愿意在最后关头不靠“充分的证据”而凭 faith 跨越鸿沟，才有可能从壳里走出来。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者把道德虚无主义的痛苦界定为“生活没有价值，于是人生没有目的”，并称其结果是很难承受较大现实困难、很难做成略有挑战的事，遇到困难时避免困难成为唾手可得的利益、继续前进成了显而易见的愚蠢。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者称他们容易来回打转、生活于轮回，一段段亲密关系因畏难而退自然消亡，于是不可避免落入终极的孤寂。",
     "evidence": ["E8"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称他们与异类互相放逐：他们遇到要为关系扛压力扛损失时会断尾逃生，这显然很难被原谅，因此几乎与异类无长久之缘。",
     "evidence": ["E9"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称他们与同类因是同类而更彼此不能容忍，最大的同类情谊不过是在知乎这种地方隔空互相点赞，现实中共同生活或合作办不到。",
     "evidence": ["E10"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称他们只能成为“关系冲浪者”，在一个潮头熄灭前爬上另一个潮头，绝大多数时候狼狈划水，并终将耗尽体力。",
     "evidence": ["E11", "E12"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者解释其不断划水爬浪头的原因是不能甘受那份应分的寂寞，而那个寂静无声的未来就是那个痛苦。",
     "evidence": ["E13", "E14"]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称很多人“幸运”地有足够资源买麻醉剂去麻醉那个痛苦，也有人靠变卖祖产达到“麻醉剂自由”，这个就完全没得“反驳”了。",
     "evidence": ["E15", "E16"]
    }
   ],
   "argument_steps": [
    "否定提问预设：不能用“反驳”对待道德虚无主义者（P001）。",
    "给出理由：逻辑自洽的体系对外部反驳免疫，且应敬畏对方的智力（P002、P003）。",
    "说明唯一可能的突破路径：对方自己求救＋内外合作＋leap of faith，且需其自身有足够痛苦与意愿（P004、P005）。",
    "描述虚无主义的痛苦：无价值、无目的导致畏难而退、难以成事（P006）。",
    "描述其关系后果：轮回、亲密关系消亡、终极孤寂（P007）。",
    "描述其与异类、同类的关系：互相放逐、彼此不能容忍（P008、P009）。",
    "以“关系冲浪者”比喻其狼狈处境与耗尽体力（P010、P011）。",
    "解释其动力：不能甘受寂寞，寂静的未来即是痛苦（P012、P013）。",
    "收束于例外：靠资源“买麻醉剂”者，作者自认无法反驳（P014、P015）。"
   ],
   "concept_usage": [
    {
     "term": "道德虚无主义（者）",
     "meaning": "本文未给出定义，而是把它当作一个“逻辑自洽的意识形态体系”与一种生活处境来描写。",
     "evidence": "P001",
     "ambiguity": "未界定范围与判定标准；文中对其生活状态的描述属作者判断。"
    },
    {
     "term": "反驳",
     "meaning": "作者否定的对待方式：从外部以证据与论证驳倒对方的体系。",
     "evidence": "P002",
     "ambiguity": "未说明“反驳”与其他说服方式的界限。"
    },
    {
     "term": "安全的外壳/最后一个栖身之所",
     "meaning": "作者对虚无主义体系功能的比喻：对方验算过后选择的庇护结构。",
     "evidence": "P003",
     "ambiguity": "为比喻，未给出可检验的界定。"
    },
    {
     "term": "leap of faith/faith",
     "meaning": "文中英文词：在最后关头不靠“充分的证据”而凭信念跨越“没有充分证据”的鸿沟。",
     "evidence": "P004",
     "ambiguity": "与宗教信仰的关系未说明。"
    },
    {
     "term": "关系冲浪者",
     "meaning": "作者对虚无主义者关系模式的比喻：在潮头熄灭前爬上另一个潮头。",
     "evidence": "P010",
     "ambiguity": "为贬抑性比喻，缺乏经验界定。"
    },
    {
     "term": "麻醉剂/麻醉剂自由",
     "meaning": "带引号的比喻，指用资源麻醉“那份痛苦”；靠变卖祖产者可达到“麻醉剂自由”。",
     "evidence": "P014",
     "ambiguity": "具体所指（消费、娱乐、药物等）本文未说明。"
    }
   ],
   "examples_and_targets": [
    "“他们”（道德虚无主义者）：作者描述与评断的对象（P003-P015）。",
    "非虚无主义者：作者称一旦发现他们会与之互相放逐的一方（P008）。",
    "知乎：作者举例的“隔空互相点赞”场所（P009）。",
    "冲浪纪录片、海龟姿势划水：作者比喻材料（P010）。",
    "变卖祖产、“祖宗积德”：作者所述靠资源麻醉痛苦的情形（P014）。",
    "提问者所问“如何反驳道德虚无主义者”：提问者材料，作者否定这一问法（Q001）。"
   ],
   "conditions": [
    "P002 “凡是逻辑自洽的意识形态体系”为条件性前提。",
    "P003 “肯定也验算过千百遍了”为推测性表述。",
    "P004 “只有对方自己想突破而自己力所不能及的时候”为唯一条件。",
    "P005 “只有靠自己有足够的痛苦……才有可能从那个壳里走出来”。",
    "P008 “至少非虚无主义者一旦发现他们，就是没有多少选择的”为限定。",
    "P014 “很多人非常‘幸运’的……”引号表反讽，非字面褒义。",
    "P015 “这个就完全没得‘反驳’了”为作者自认的例外情形。"
   ],
   "rhetoric_and_tone": "冷静分析与讽刺性描写并用；引号反讽密集（“幸运”“祖宗积德”“麻醉剂自由”“关系冲浪者”“反驳”）；比喻成串（外壳、栖身之所、鸿沟、轮回、断尾逃生、海龟姿势划水、麻醉剂）；反问（“他们又为什么一定要划水爬浪头呢？”）；中英混用（leap of faith、faith）；以自认无法反驳的一句作结。",
   "unresolved_questions": [
    "提问问“如何反驳道德虚无主义者”，正文主张不能以“反驳”对待，未给出可操作方案；问答对应关系需研究者判断。",
    "“道德虚无主义者”在本文中未定义、未给判定标准，作者对其生活处境的描述亦未给经验证据。",
    "“麻醉剂”“麻醉剂自由”为比喻，具体所指本文未说明。",
    "作者自身立场（是否非虚无主义者）未直接声明，仅以“你”“他们”的用词显示旁观视角，需研究者判断。",
    "P009 提及“知乎”属平台名，为作者例证。",
    "“leap of faith”与“faith”的确切所指及其与宗教信念的关系，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "道德虚无主义者不能用“反驳”这种方式去对待。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "他们的逻辑是自洽的。凡是逻辑自洽的意识形态体系，用外部的“反驳”都是没有用的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你也要敬畏对方自己的智力。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这个循环，只有对方自己想突破而自己力所不能及的时候，向你发出求救的信号。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而这只能靠ta自己有足够的痛苦，不愿再继续这么过下去。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "道德虚无主义的痛苦是什么？生活没有价值，于是人生没有目的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "本来目的就没有意义，那么在前往任何目的地的路上遇到了太大的困难，那么避免困难自然就成了唾手可得的利益，继续前进就成了一种显而易见的愚蠢。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "一段段的亲密关系都因为他们畏难而退自然消亡。于是不可避免的落入终极的孤寂之中。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "而他们遇到要为关系扛压力扛损失的时候，也会断尾逃生，这显然是很难被原谅的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "他们最大的同类情谊，不过是在知乎这种地方隔空互相点赞。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "于是他们就只能成为“关系冲浪者”，想办法在一个潮头熄灭之前爬上另一个潮头。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "而且到最后他们终将耗尽体力。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "因为他们又不能甘受那份应分的寂寞。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "那个寂静无声的未来，就是那个痛苦。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "很多人非常“幸运”的有足够的资源买麻醉剂去麻醉那个痛苦。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "这个就完全没得“反驳”了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德哲学", "人生意义", "心理与人际关系"],
   "issue_candidates": ["如何对待道德虚无主义者", "逻辑自洽体系与外部反驳", "虚无主义者的痛苦与孤寂"],
   "text_function_candidates": ["评论", "分析", "劝导（否定提问方式）"],
   "object_candidates": ["道德虚无主义者", "非虚无主义者", "知乎"],
   "working_keywords": ["道德虚无主义", "逻辑自洽", "外壳", "leap of faith", "faith", "关系冲浪者", "麻醉剂自由"]
  },
  "notes": "正文无图片节点；正文与 lexical 无差异。文中对道德虚无主义者生活状态的描述均为作者判断（非提问者立场），本记录按 attribution=author 登记。"
 },
 "99919a57": {
  "analysis": {
   "question_context": "提问者（Q001）问“猫咪这么可爱又柔弱的动物是如何在弱肉强食的进化史上幸存的？”。作者以“利用地形”这一基本战术作答（P001）：钻进尺寸合适的洞穴、掌握树上活动技能、夜间视力最强等都能让动物在特定环境中成为王者（P002-P004），因此猫科动物之强往往是其所处环境条件下的强悍（P005），家猫在其“老家”很可能是该生态位上无敌的王者（P006）；作者最后否定把动物关进同一笼子比输赢的衡量标准（P007）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "提出基本命题：动物有一种基本的战术来放大自己的战斗能力，就是利用地形。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003", "P004"],
     "summary": "以三种情形举例：钻进一定尺寸洞穴者可成为“洞穴里的百兽之王”；有独特树上活动技能者可成为“树上之王”；夜间视力最强者可成为“夜间之王”。",
     "role": "example"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P005", "P006"],
     "summary": "落到猫科：猫科动物之强往往是其所处环境条件下的强悍；家猫个头不大，但在其老家很可能是该生态位上名副其实、无敌的王者。",
     "role": "conclusion"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P007"],
     "summary": "否定常见的比较方式：把动物关到同一个笼子里看谁打得赢谁是没有意义的。",
     "role": "rebuttal"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：动物有一种基本的战术来放大自己的战斗能力，就是利用地形。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者举例：钻进一定尺寸的洞穴里，体重明显大过它的动物不可能进来，它就瞬间成为洞穴里的百兽之王。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者举例：有独特的树上活动技能、幼弱树枝只能承受它这么大的个体，它就成了树上之王。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者举例：因为夜间视力最强、比它壮的都没它夜间视力好，它就成了夜间之王。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：猫科动物之强，往往是在它们所处的环境条件下的强悍。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称家猫个头虽不大，但在它们的老家它很可能是那个生态位上名副其实、无敌的王者。",
     "evidence": ["E6"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否定一般人类的衡量标准：把动物关到同一个笼子里看谁打得赢谁，这是没有意义的。",
     "evidence": ["E7"]
    }
   ],
   "argument_steps": [
    "提出“利用地形放大战斗力”的基本命题（P001）。",
    "以洞穴、树上、夜间三种情形举例说明环境位优势（P002-P004）。",
    "归纳到猫科：其强悍是环境条件下的强悍（P005）。",
    "推论家猫在其原产地生态位上很可能是王者（P006）。",
    "否定“关进同一笼子比输赢”的衡量方式（P007）。"
   ],
   "concept_usage": [
    {
     "term": "利用地形",
     "meaning": "作者所称动物放大自身战斗能力的基本战术。",
     "evidence": "P001",
     "ambiguity": "“地形”是否包括夜行性等非空间条件，文中未严格界定（P004 的夜间视力即属非地形因素）。"
    },
    {
     "term": "洞穴里的百兽之王/树上之王/夜间之王",
     "meaning": "作者对环境位优势的形象化命名。",
     "evidence": "P002",
     "ambiguity": "为修辞性说法，非学术术语。"
    },
    {
     "term": "生态位",
     "meaning": "作者称家猫在其老家很可能是该生态位上名副其实的王者。",
     "evidence": "P006",
     "ambiguity": "未给出定义，也未指明“老家”的具体地区或物种。"
    }
   ],
   "examples_and_targets": [
    "钻进一定尺寸洞穴的动物：作者举例（P002）。",
    "具备树上活动技能的动物：作者举例（P003）。",
    "夜间视力最强的动物：作者举例（P004）。",
    "猫科动物与“你家的猫”：作者举例与提问对象（P005、P006）。",
    "把动物关到同一个笼子里看谁打得赢谁的衡量标准：作者反驳对象（P007）。",
    "提问中“可爱又柔弱”“弱肉强食”的说法：提问者材料，正文未使用这些词（Q001）。"
   ],
   "conditions": [
    "P002 “钻进一定尺寸的洞穴里”为条件。",
    "P002-P004 三例均以“比如/又或者”引出假设性情形。",
    "P005 “往往”为概率性限定。",
    "P006 “在它们的老家”“很可能”为地点与概率限定。"
   ],
   "rhetoric_and_tone": "简短说明文；三段“又或者”排比举例；以“百兽之王/树上之王/夜间之王”作形象化命名；末句直接否定人类常见的比较方式（“这是没有意义的”）；对读者以“你家的猫”拉近距离。",
   "unresolved_questions": [
    "正文未直接回答“猫咪如何在弱肉强食的进化史上幸存”的全过程，只给出“利用地形/环境条件下的强悍”这一解释；是否还涉及其它机制（繁殖策略、群居、人类驯养等），本文未说明。",
    "“它们的老家”具体所指地区与物种未说明，需外部核查。",
    "P002-P004 的三例均未指明具体物种。",
    "“生态位”未加定义。",
    "提问中的“可爱又柔弱”与“弱肉强食”在正文中未被使用或评价。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "动物有一种基本的战术来放大自己的战斗能力，就是利用地形。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "比如钻进一定尺寸的洞穴里，体重明显大过它的动物不可能进来，它就瞬间成为洞穴里的百兽之王了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "又或者它有独特的树上活动技能，幼弱的树枝只能承受得住它这么大的个体，它就成了树上之王。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "又或者因为夜间视力最强，比它壮的都没它夜间视力好，它就成了夜间之王。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "猫科动物之强，往往是在它们所处的环境条件下的强悍。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "别看你家的猫个头不大，在它们的老家它很可能是那个生态位上名副其实的王者，无敌的那种。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "一般人类的衡量标准是把动物关到同一个笼子里看谁打得赢谁，这是没有意义的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["动物行为/进化生态"],
   "issue_candidates": ["猫科动物的生存优势", "地形与环境位的作用", "笼中比较是否有意义"],
   "text_function_candidates": ["解释", "短答"],
   "object_candidates": ["猫科动物", "家猫", "洞穴动物", "树栖动物", "夜行性动物"],
   "working_keywords": ["利用地形", "百兽之王", "树上之王", "夜间之王", "生态位", "环境条件"]
  },
  "notes": "正文无图片节点；正文与 lexical 无差异。正文未直接使用提问中的“可爱又柔弱”“弱肉强食”等词，已在 unresolved_questions 登记。"
 },
 "7b9fc1f4": {
  "analysis": {
   "question_context": "提问者（Q001）问“我要怎样做才可以让一线的医生护士不这么辛苦?”。作者按地域与能力分三种情形给出建议：在非武汉非湖北地区者对任何疾病风险保持高谨慎策略，以便本地医疗系统放心派出援助（P001），援助越多前线医护越有机会换班休息（P002）；在武汉或湖北当地且有能力者担任志愿者协助社区降低居民暴露必要（如代领团购菜），减少进一步传染（P004）；没能力出力者至少看护各个微信群、QQ群和业主论坛，及时坚韧地打击谣言和攻击煽动等言论，保持一线社区人员和志愿者的士气（P005）。作者称这些都是“很现实的帮助”（P003、P006），以“诸君努力”收束（P007）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "情形一（非武汉非湖北）：这段时间对任何疾病风险保持高谨慎策略，好让本地医疗系统放心派出援助；援助越多，前线医护越有机会换班休息；这就是很现实的帮助。",
     "role": "action_advice"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P004"],
     "summary": "情形二（武汉或湖北当地、有能力）：担任志愿者协助社区降低居民暴露必要（如代领团购菜等），减少进一步传染。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P005"],
     "summary": "情形三（没能力出力）：最少可以看护各个微信群、QQ群和业主论坛，及时并且坚韧不拔地打击谣言和攻击煽动等言论，帮助保持一线社区人员和志愿者群体的士气。",
     "role": "action_advice"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P006", "P007"],
     "summary": "总结与勉励：这都有非常现实的帮助；诸君努力。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者建议：如果你在非武汉非湖北地区，这段时间对待任何疾病风险都保持高谨慎策略，好让你本地的医疗系统可以放心派出援助。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称援助越多，前线医护就有更多的机会换班休息，这就是很现实的帮助。",
     "evidence": ["E2", "E3"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者建议：如果你在武汉或者湖北当地，有能力的话可以担任志愿者协助社区降低居民暴露必要（比如代领团购菜等），减少进一步传染。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者建议：如果没能力出力，最少可以看护各个微信群、QQ群和业主论坛，及时并且坚韧不拔的打击谣言和攻击煽动等言论，帮助保持一线社区人员和志愿者群体的士气。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者总结：这都有非常现实的帮助。",
     "evidence": ["E6"]
    }
   ],
   "argument_steps": [
    "按地域分情形给建议：非湖北地区者保持高谨慎策略，使本地医疗系统可放心派出援助（P001）。",
    "说明传导机制：援助越多，前线医护越有机会换班休息（P002）。",
    "评价这是很现实的帮助（P003）。",
    "第二种情形：湖北当地有能力者做志愿者，降低居民暴露必要（P004）。",
    "第三种情形：没能力者看护网络社群、打击谣言与煽动言论以维持士气（P005）。",
    "总结并勉励（P006、P007）。"
   ],
   "concept_usage": [
    {
     "term": "高谨慎策略",
     "meaning": "作者建议非湖北地区居民对待任何疾病风险采取的策略，目的是让本地医疗系统放心派出援助。",
     "evidence": "P001",
     "ambiguity": "具体内容（哪些行为、何种程度）本文未说明。"
    },
    {
     "term": "暴露必要",
     "meaning": "指居民不得不外出暴露的情形；志愿者协助社区降低这种必要。",
     "evidence": "P004",
     "ambiguity": "未定义，也未列全可降低暴露的方式（仅举代领团购菜）。"
    },
    {
     "term": "士气",
     "meaning": "作者建议通过打击谣言与煽动言论来保持一线社区人员和志愿者的士气。",
     "evidence": "P005",
     "ambiguity": "“谣言”“攻击煽动”的判定标准与执行主体未说明。"
    },
    {
     "term": "很现实的帮助/非常现实的帮助",
     "meaning": "作者对上述三类行动的自我评价用语。",
     "evidence": "P003",
     "ambiguity": "为评价性表述，未给出效果衡量。"
    }
   ],
   "examples_and_targets": [
    "武汉、湖北：作者据以分情形的地区（P001、P004）。",
    "本地医疗系统、前线医护：作者建议的受益对象与传导环节（P001、P002）。",
    "志愿者、社区：作者建议的行动主体（P004）。",
    "代领团购菜：作者所举降低暴露的示例（P004）。",
    "微信群、QQ群、业主论坛：作者所举需看护的信息场域（P005）。",
    "谣言和攻击煽动等言论：作者建议打击的对象（P005）。",
    "提问中“一线的医生护士不这么辛苦”：提问者材料，正文以三类间接行动回应（Q001）。"
   ],
   "conditions": [
    "P001 “如果你在非武汉非湖北地区，那么……”。",
    "P004 “如果你是在武汉或者湖北当地，那么有能力的话……”。",
    "P005 “如果你没能力出力，那么最少可以……”。",
    "P002 “援助越多，前线医护就有更多的机会换班休息”为条件性传导表述。",
    "P003、P006 以“这就是/这都有非常现实的帮助”作评价性收束。"
   ],
   "rhetoric_and_tone": "简短的分情形行动建议；三个“如果……那么……”平行结构（按地域与能力分层，逐层降低行动门槛）；语气务实直接（“这就是很现实的帮助”“这都有非常现实的帮助”）；以“诸君努力”作勉励式收尾。",
   "unresolved_questions": [
    "提问问“我要怎样做才可以让一线的医生护士不这么辛苦”，正文给出三类间接做法（本地谨慎、当地做志愿者、看护网络社群），未涉及捐赠、物资等其他方式，也未论证做法与减轻医护负担之间的因果强度。",
    "“高谨慎策略”的具体内容本文未说明。",
    "“谣言和攻击煽动等言论”的判定标准与由谁执行，本文未说明。",
    "文章日期为 2020-03-01，正文未写明疫情阶段与相关政策的依据，需外部核查。",
    "作者是否身处武汉/湖北、其身份为何，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "如果你在非武汉非湖北地区，那么这段时间对待任何疾病风险都保持高谨慎策略，好让你本地的医疗系统可以放心派出援助。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "援助越多，前线医护就有更多的机会换班休息。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这就是很现实的帮助。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "如果你是在武汉或者湖北当地，那么有能力的话可以担任志愿者协助社区降低居民暴露必要（比如代领团购菜等），减少进一步传染。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "如果你没能力出力，那么最少可以看护各个微信群、QQ群和业主论坛，及时并且坚韧不拔的打击谣言和攻击煽动等言论，帮助保持一线社区人员和志愿者群体的士气。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这都有非常现实的帮助。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "诸君努力。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["公共卫生应急", "志愿服务", "社区治理"],
   "issue_candidates": ["如何减轻一线医护负担", "疫情期间普通人的可行行动", "网络社群中的谣言与煽动"],
   "text_function_candidates": ["行动建议", "短答"],
   "object_candidates": ["武汉", "湖北", "本地医疗系统", "前线医护", "志愿者", "社区", "微信群", "QQ群", "业主论坛"],
   "working_keywords": ["高谨慎策略", "暴露必要", "代领团购菜", "谣言", "士气", "援助"]
  },
  "notes": "正文无图片节点；正文与 lexical 无差异。正文按地域与能力分三种情形给建议，句短（241 字），未涉及物资捐赠等其他助医方式。"
 }
}  # noqa: E501


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
