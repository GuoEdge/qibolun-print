# -*- coding: utf-8 -*-
"""批次 r001-b0022 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0022.sessions.py            # 写 out/r001-b0022.out.jsonl
  python3 records/r001-b0022.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0022"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0022.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "85d05c4a": {
  "analysis": {
   "question_context": "提问者（Q001）问“怎样确定你的女朋友（男朋友）是适合的结婚对象？”。作者给出的办法是：准备一份婚前协议（明确财产分割、以离婚为前提约定生育抚育、约定“无理由离婚”），并观察对方对这份协议的反应——看到协议就大失所望、觉得“那为什么还要结婚”的人一定不可以选择，只有能毫无障碍地接受协议且有契约意识的人值得考虑。作者并把这一检验背后的原理归结为：不尊重他人“古怪”权利的人，会以道德观与造成损失的能力为筹码，逼迫对方与其“保持和谐一致”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出办法：有一种非常简单而实用、绝对有效的办法，即准备一件婚前协议；协议至少要包含若干条款。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "财产条款：明确婚前与婚内财产分割，婚前财产不参与共有、婚后双方工作所得也直接属于个人；担当家务计算报酬、公共开销一人一半、不能支付的部分视为借贷并在离婚时转为个人债务；礼物视为接收方个人财产、无归还义务；对财物做完全切割、杜绝搭顺风车，任何时候离婚均可干脆利索地完成无异议余地的财产分割；父母的抚养义务归个人，对方除必要礼节外不承担经济义务。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "生育抚育与离婚条款：以可能的离婚为前提约定生育和抚育（即如果离婚，子女抚养权默认归谁）；约定共同认可“无理由离婚”，一方提出离婚无需给出所谓合理的理由，也不接受对离婚理由合理性的评判。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012"], "summary": "理想的协议版本有两个特征：它是合法的；它的规定之严厉令人忍不住叫出来“如果是这样，那为什么要结婚？”。看到协议就大失所望、觉得“那为什么还要结婚”的人一定不可以选择，因为那意味着他的一切投入都是为了获得那些“婚姻价值”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "以连续反问追问对方的恐惧：为什么让对方改变主意必须付出高昂代价对你如此重要？为什么要这么敏感和执着地防范对方改变主意？“解释一下，你在怕什么？”只有认为“即使是这样，我也认为仍有结婚的理由”、并明白“这些约定再古怪，提出这些也是人家的正当权利”的人，才有资格与你继续行路。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017"], "summary": "行动建议：不要等到谈婚论嫁再这么做，在谈情说爱之前就最好先亮底牌；只有能毫无障碍地接受这份协议且有契约意识的人才值得考虑。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "背后的原理：不尊重他人“古怪”权利的人，一定会以自己的价值观和道德观为依据、以他对你造成客观损失的能力为筹码，逼迫你去【跟他】“保持和谐一致”，实际上是一种以造成你的损失为威胁手段的、要求你向他靠拢的统治手段；而这份协议会极大地提高在婚姻中做这种尝试的难度；如果他本来就没有这种打算，协议对他也没有任何冒犯；如果他觉得协议会使婚姻失去对他的“价值”和“意义”，那你就看到对方实际上是在做什么了。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024"], "summary": "对谋求这种权力者的强烈评价：与ta的贪婪相比，ta这点殷勤廉价得可耻；ta谋求的那种权力之贵重不是任何贿赂所能相配的；哪怕ta物质上更富有、看似不签协议你更占物质便宜，都是如此。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "对爱的界定与对方应具备的品质：爱一定建立在任何时候都会尊重你的意愿、时刻准备为你的合法权利忍受一切不便的基础上；“我爱你”三个字不可以成为随时可以拿出来命令你放弃某项个人自由的大义名分；作者以第一人称拟出一段最重要的个人品质（别人的合法权利会让我觉得不便，那只是我的命运；若会造成我的“损失”，那只是意味着原本那利润就是白得的），并称只有真的这样想的人才配在你有一切不仁慈的权利时得到你的仁慈，而且是一得再得。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035"], "summary": "结论：那些寻求“婚姻的价值”的“契约惊讶者”，寻求的就是“不必感激的权利”；那绝不是可以接受的追求，也绝不能用“你也不必感激”来交换；只有能在这“毫无意义”之外仍能看到意义的人值得严肃考虑深入交往，不成情侣也要考虑作为朋友，因为这是经典的赢家特征——能签这协议的，就能结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出有一种非常简单而实用的办法（并称绝对有效）：准备好一件婚前协议，协议至少要包含他所列的若干条款。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出财产条款：明确婚前与婚内财产分割，婚前财产不参与共有、婚后双方工作所得也直接属于个人；担当家务要计算报酬、公共开销一人一半、不能支付的部分视为借贷并在离婚时转为个人债务；礼物应视为接收方的个人财产、没有任何归还义务；并对财物做完全切割、杜绝任何一方搭顺风车。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出应以可能的离婚为前提约定生育与抚育（即如果离婚，子女抚养权默认归谁），并约定共同认可“无理由离婚”——一方提出离婚无需给出所谓合理的理由，也不接受对离婚理由合理性的评判。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为理想的协议版本有两个特征：它是合法的；它的规定之严厉令人忍不住叫出来“如果是这样，那为什么要结婚？”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为看到这份协议就会大失所望、觉得“那为什么还要结婚”的人一定不可以选择，因为那意味着他的一切投入都是为了获得那些“婚姻价值”。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问追问：为什么让对方改变主意必须付出高昂的代价对你如此重要？你为什么要这么敏感和执着地防范对方改变主意？并直接要求对方解释“你在怕什么？”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为只有那些认为“即使是这样，我也认为仍有结婚的理由”、并且明白“这些约定再古怪，提出这些也是人家的正当权利”的人，才有资格与你继续行路；并建议在谈情说爱之前就先亮底牌，只有能毫无障碍地接受这份协议且有契约意识的人才值得考虑。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出背后的原理：一个不尊重他人“古怪”的权利的人，一定会以自己的价值观和道德观为依据、以他对你造成客观损失的能力为筹码，逼迫你去【跟他】“保持和谐一致”，实际上那是一种以造成你的损失为威胁手段的、要求你向他靠拢的统治手段；而这份协议会极大地提高在婚姻中做这种尝试的难度。", "evidence": ["E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者判断：如果他本来就没有任何这种打算，他将会发现这份协议对他也没有任何冒犯；如果他觉得这份协议的存在会使婚姻失去对他的“价值”和“意义”，那么你就看到对方实际上是在做什么了。", "evidence": ["E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者评价：与ta的贪婪相比，ta这点殷勤廉价得可耻；ta所谋求的那种权力之贵重，不是任何贿赂所能相配的；哪怕ta是物质上更富有的一方、看似不签这协议你会在物质上更占便宜，都是如此。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定爱：爱一定是建立在任何时候都会尊重你的意愿的基础之上的，是建立在时刻准备为你的合法权利忍受一切不便的基础上的；无论如何，“我爱你”三个字不可以成为一种随时可以拿出来命令你放弃某项个人自由的大义名分。", "evidence": ["E22", "E23"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以第一人称拟出并推荐一种个人品质：别人的合法权利会让我觉得不便，那只是我的命运；如果会造成我的“损失”，那只是意味着原本那利润就是白得的；他认为这是可托付之人必须有的品质，只有真的这样想的人，才配在你有一切不仁慈的权利时得到你的仁慈，而且是一得再得。", "evidence": ["E24", "E25"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为那些寻求“婚姻的价值”的“契约惊讶者”，寻求的就是“不必感激的权利”；那绝不是一种可以接受的追求，也绝不能用“你也不必感激”来交换。", "evidence": ["E26", "E27"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为只有能在这“毫无意义”之外仍能看到意义的人值得严肃考虑深入交往；不成情侣也要考虑作为朋友，因为这是经典的赢家特征——能签这协议的，就能结。", "evidence": ["E28", "E29", "E30"]}
   ],
   "argument_steps": [
    "提出方法并称其简单实用、绝对有效（P001-P002）。",
    "列出协议的第一类条款：财产切割、家务报酬、共同开销与债务、礼物归属、父母抚养义务（P003-P005）。",
    "列出第二、三类条款：生育抚育约定与“无理由离婚”（P006-P007）。",
    "给出理想协议的两个特征，并据此筛选对象（P008-P012）。",
    "以连续反问逼问对方在怕什么（P013-P014）。",
    "给出通过标准：能接受协议且明白他人的正当权利（P015）。",
    "给出时机建议与对象筛选标准（P016-P017）。",
    "解释原理：不尊重他人“古怪”权利者实为以损失相威胁的统治手段（P018-P019）。",
    "给出两种反应的分辨方式（P020-P021）。",
    "以强烈措辞评价其所谋求的权力（P022-P024）。",
    "界定爱与“我爱你”不能作为大义名分（P025-P026）。",
    "以第一人称拟出可托付之人的品质（P027-P029）。",
    "收束：否定“不必感激的权利”，给出结论“能签这协议的，就能结”（P030-P035）。"
   ],
   "concept_usage": [
    {"term": "婚前协议", "meaning": "作者提出的检验工具：以财产切割、生育抚育约定与“无理由离婚”为内容的协议，用来观察对方对他人权利的尊重程度。", "evidence": "P002、P004-P007", "ambiguity": "协议条款的可执行性与法律效力，作者只称理想版本“是合法的”，未举法律依据。"},
    {"term": "婚姻价值", "meaning": "作者用来指对方试图从婚姻中获取的好处；认为一切投入都为获得这些“婚姻价值”的人不可以选择。", "evidence": "P012", "ambiguity": "该词为作者带引号的用法，未逐项界定具体内容。"},
    {"term": "契约惊讶者", "meaning": "作者自造的说法，指对这份协议感到惊讶、寻求“不必感激的权利”的人。", "evidence": "P030", "ambiguity": "术语为作者自设，未给出定义或适用范围。"},
    {"term": "不必感激的权利", "meaning": "作者认为“契约惊讶者”所追求的东西：既要得到对方的一切，又不必对之感激。", "evidence": "P030", "ambiguity": "作者未说明该“权利”在法律或道德上如何被主张。"},
    {"term": "统治手段", "meaning": "作者对“逼迫对方保持和谐一致”的定性：以造成对方损失为威胁手段、要求对方靠拢。", "evidence": "P018", "ambiguity": "该定性为作者的判断，未给出实例。"},
    {"term": "大义名分", "meaning": "作者用来指“我爱你”被用作命令对方放弃个人自由的正当理由。", "evidence": "P026", "ambiguity": "该词借自传统政治伦理用语，作者未作界定。"},
    {"term": "【跟他】", "meaning": "作者以方括号强调的字样，强调“向对方靠拢”的方向。", "evidence": "P018", "ambiguity": "方括号为原文强调标记，强调方式未说明。"}
   ],
   "examples_and_targets": [
    "婚前协议的具体条款（作者自拟的建议方案）",
    "“如果是这样，那为什么要结婚？”（作者引述被筛选者可能的反应，非作者主张）",
    "“那为什么还要结婚”（同上，作者引用以作筛选判据）",
    "“别人的合法权利会让我觉得不便……那只是我的命运……”（作者以第一人称拟出的品质陈述，用以标示可托付之人的标准，非提问者立场）",
    "物质上更富有的一方（作者讨论的对象情形）",
    "ta（作者行文中对第三方的中性指称，未区分性别）"
   ],
   "conditions": [
    "“至少要包含以下条款”——作者所列条款为最低要求（P003）",
    "“以可能的离婚为前提”（P006）",
    "“如果离婚，子女抚养权默认归谁”（P006）",
    "“如果他本来就没有任何这种打算”“如果他觉得这份协议的存在会使婚姻失去对他的‘价值’和‘意义’”（P020、P021）",
    "“哪怕ta是物质上更富有的一方，看似不签这协议你会在物质上更占便宜”（P024）",
    "“只有能毫无障碍的接受这份协议且有契约意识的人才值得考虑”“能签这协议的，就能结”（P017、P035）",
    "“在谈情说爱之前就最好先亮底牌”——时机条件（P016）"
   ],
   "rhetoric_and_tone": "强烈的断言与第二人称对话：开头即称办法“绝对有效”，多用“一定不可以选择”“相信我”“绝不能”等绝对化措辞；连续反问追问对方动机（“你在怕什么？”）；以【跟他】作括号强调，用“廉价得可耻”“统治手段”等贬斥性表述评价其所谋求的权力；结尾转为格言式短句（“能签这协议的，就能结。”“因为这是经典的赢家特征。”），整体带有劝诫与筛选指南的语气。",
   "unresolved_questions": [
    "“绝对有效”未给依据；协议的实际可执行性、法律效力与公证需求本文未说明（作者仅称理想版本“是合法的”）",
    "“契约惊讶者”“不必感激的权利”“婚姻价值”“大义名分”等为作者自造或特定用法，本文未逐一定义",
    "对方拒绝签署时的处置，作者只给出“一定不可以选择”，未讨论其他情形",
    "作者未讨论协议在无婚前财产或一方不同意时的替代方案",
    "P018 的方括号【跟他】为原文强调标记，其强调方式未说明",
    "updated_at(2021-05-25) 晚于 published_at(2019-05-15)，版本差异本文未说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有一种非常简单而实用的办法，绝对有效，有空写一下。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "担当家务要计算报酬，公共开销一人一半，不能支付的部分视为借贷，离婚时应转变为个人债务。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "杜绝任何一方搭顺风车的可能", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "以可能的离婚为前提，做好关于生育和抚育的约定。即如果离婚，子女抚养权默认归谁。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "约定共同认可“无理由离婚”，即一方提出离婚无需给出所谓合理的理由，也不接受对离婚理由合理性的评判", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "1）它是合法的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "2）它的规定之严厉，令人忍不住叫出来“如果是这样，那为什么要结婚？”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "看到这一份协议就会大失所望，觉得“那为什么还要结婚”的人，一定不可以选择。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "因为那意味着他的一切投入，都是为了获得那些“婚姻价值”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "为什么让对方改变主意必须付出高昂的代价对你如此的重要？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "解释一下，你在怕什么？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "只有那些认为“即使是这样，我也认为仍有结婚的理由”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "不要等到谈婚论嫁再这么做，在谈情说爱之前就最好先亮底牌。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "只有能毫无障碍的接受这份协议且有契约意识的人才值得考虑。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "实际上那是一种以造成你的损失为威胁手段的、要求你向他靠拢的统治手段。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "而这份协议会极大的提高在婚姻中做这种尝试的难度。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "如果他本来就没有任何这种打算，他将会发现这份协议对他也没有任何冒犯。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "那么你就看到对方实际上是在做什么了。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "与ta的贪婪相比，ta这点殷勤廉价得可耻。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "ta所谋求的那种权力之贵重，不是任何贿赂所能相配的。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "哪怕ta是物质上更富有的一方，看似不签这协议你会在物质上更占便宜，都是如此。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "爱一定是建立在在任何时候都会尊重你的意愿的基础之上的，是建立在时刻准备为你的合法权利忍受一切不便的基础上的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P026", "quote": "“我爱你”三个字不可以成为一种随时可以拿出来命令你放弃某项个人自由的大义名分。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "那只是我的命运。如果会造成我的‘损失’，那只是意味着原本那利润就是白得的", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "这是一个可托付之人必须有的品质。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P030", "quote": "那些寻求“婚姻的价值”的“契约惊讶者”，寻求的就是“不必感激的权利”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P031", "quote": "相信我，那绝不是一种可以接受的追求，也绝不能用“你也不必感激”来交换。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P032", "quote": "只有能在这“毫无意义”之外仍能看到意义的人，值得你严肃的考虑深入的交往。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P034", "quote": "因为这是经典的赢家特征。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P035", "quote": "能签这协议的，就能结。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚姻与家庭", "契约与法律关系", "伦理与人格评价"],
   "issue_candidates": ["如何确定结婚对象", "婚前协议", "财产分割与家务报酬", "无理由离婚", "尊重他人权利与爱的界定"],
   "text_function_candidates": ["答疑", "行动建议", "劝诫", "筛选标准"],
   "object_candidates": ["提问者", "结婚对象（女朋友／男朋友）", "契约惊讶者", "父母"],
   "working_keywords": ["婚前协议", "婚前财产", "婚内财产", "家务报酬", "无理由离婚", "婚姻价值", "契约惊讶者", "不必感激的权利", "统治手段", "大义名分"]
  },
  "notes": "无图片节点。本文为知乎问答体；P027 中“别人的合法权利会让我觉得不便……那只是我的命运……”是作者以第一人称拟出的品质陈述（用以标示可托付之人的标准），并非提问者立场，已按 author_explicit + attribution=author 记录。P010-P011 引号内“那为什么要结婚”为作者引述被筛选者可能的反应。协议条款的法律效力与可执行性需外部核查。updated_at(2021-05-25) 晚于 published_at(2019-05-15)，版本关系本文未说明。"
 },
 "110e0b03": {
  "analysis": {
   "question_context": "提问者（Q001）问“什么才是门当户对？”。作者先以概率论证说明读者几乎必然是名门之后、只是忘记了先人的世家传承，因此才失去“门户”，并澄清“门当户对”不是嫌贫爱富；随后给出自己的理解：永世长存的家族与另一个永世长存的家族永远门当户对，讲究门当户对真正嫌的是“没有身为一个家族祖宗的自觉”。文中以“（7.9续）”“（7.10更新）”分段续写，末段标“（未完，待续）”，并以“如之奈何？”收束；P063 的“家族答集”及相关问题标题疑为平台集子标签与关联文章标题混入正文。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "点题：要好好说一说门当户对的问题，因为这个问题对中国太重要了。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "以反问与概率论证提出：如果算过名门世家与一般平民的生育率差异、子女幸存率差异，就会看到从数学概率上讲，你的整个祖宗链条里完全没有名门背景的可能性几乎为零；中国只有几千个姓，即使折算掉易姓、自号、在极近的年代归化的成分，这些姓里也尽皆曾有过不折不扣的名门，而且是屡屡崛起、层层叠叠的名门；因此你们全部是世家子弟，例外的可能性接近于零。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012"], "summary": "指出读者曾有历经数代乃至数十代先人血汗总结出的黄金一般的世家传承与家族经验，只是忘记了；一忘就归零，多少代先人累世沉浮才明白的教训和禁忌都不知道了，只好从自己开始重新经历若干代人的沉浮去重新知道。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015"], "summary": "推论：是因为不知道这些，你才失去了“门户”，才有与别人的“门不当、户不对”；并以反问指出你连门户都没有，怎么和有门户的去“门当户对”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "澄清：这不是说你家不够有钱、于是和“家资万贯的家庭”不门当户对；对方如果因为这个来嫌弃你，你大可以放心——你有机会看着这家人在两代之内家破人亡、曲终人散；这样看待门户的家庭没有资格称“门户”，那不是你跟ta们门户不对，而是ta们跟你门户不对。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "指出谈得上门户的世家懂得一个最朴素的道理：财富并不是最难获得的家族资源，传承和韧性才是，超越自身和时代的胸襟和自觉才是。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "给出定义与门槛：你自己就是你后人的祖宗、是你自己家族的开创者；“门当户对”就是永世长存的家族和另一个永世长存的家族永远门当户对，一时之间谁盛谁衰都只是次要的、暂时的起伏；正确的理解不是嫌你穷、不是嫌你不走运，而是嫌你没有身为一个家族祖宗的自觉；这种自觉性正是谈婚论嫁的基本门槛，迈过了明白道理的世家大族不会认为你真有什么门不当户不对，因为永生的东西分什么贫富贵贱；没这种自觉就不是门当户对的问题，而是干脆最好不要祸害ta人。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "以反问要求读者想清楚“什么叫做身为祖宗的自觉”，并指出：能明白这一点，你与世上任何一家都只有对方能不能配得起你的问题，没有你配不配得起对方的问题；真正的世家一定看得懂这一点，看得到你有建立传承的自觉，对方就明白你这家族是必须重视的存在；无论现在势力强弱、一时尊卑如何，与世长存的家族之间只能互相平视——这才是人人平等的根子：永恒者必与永恒者平等。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P034", "P035"], "summary": "对三代而亡的“富家”的判定：只是不值得特别关注的烟尘，没有资格得到重视、也没有必要在意，其彼此间的态度最终随其消亡而毫无意义；能成其为门户的，尽皆门当户对，哪怕此时你贫ta富、你“贱”ta贵。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040"], "summary": "（7.9续）给出“祖宗的自觉”的定义：不再仅从自身的立场来看待成功，而是把成功看作一种家族事业；每一代的祖宗都不必力求速成，但要寻求为家族后代更进一步地夯实基础——要求事业，但更要求基业。", "role": "definition"},
    {"unit_id": "U011", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045"], "summary": "理由是代际能力与机会有限、世事无常：若总是存着“一定要在自己这一代当个富一代”的心，心怀侥幸、急功近利、铤而走险，反而往往导致久作不兴；即使侥幸谋得浮财，家风不靖、根基不稳，浮财不足以为福反而足以为祸；最大的问题在于“每一代人都想在自己这一代完成大翻身”这种投机策略，无理性的焦虑驱使人不断投机取巧、越失败越加倍，要么一败涂地，要么侥幸成功后把侥幸当作成功之道加倍下注直至再次失去一切还更深陷；而以家族基业为考量中心的人可以轻松摆脱这种恶性循环。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P046", "P047", "P048", "P049"], "summary": "提出正确的家族战略：每一代人都谋求为下一代创造更好的根基，哪怕每代只拱一小卒、代代不息，也终有一天走到“这一代人想不成功也难”的优势状态；这成功水到渠成、自自然然，且因代代家风的建设积累足以持久、能循环光大，财富可以开枝散叶、越发同气连枝，总体上更加稳固；这对身为列祖列宗的先辈也是一种解脱——创业先祖的任务不再是这一代谋得亿万身家，而只是为家族后代留下可继承的正资产、充分可借鉴的经验教训以及良好的教育；这是朴实、踏实、不必依赖疯狂幸运的目标；而且一旦眼光从谋一世变为谋万世，做事反而容易有定性、有踏实的成果、有同志、有意料之外的帮助。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060"], "summary": "（7.10更新）界定家族的边界：基业所及，即为族人；强调不要以血缘为界，要把与基业相关的所有人都视为家族成员，绝不能仅仅偏向自己的亲属或直系血亲；对志同道合处在同一生态中的平辈爱之如己，对托庇并尽力奉献的晚辈视如己出，这是拥有足够资源和人才应对未来风险绝对不能少的安排；越爱惜自己的子女血亲，就越要明白ta们需要这些不同姓、不沾亲的兄弟姐妹叔伯姑姨；同姓族人是不容选择的，仅从概率上说也很难支撑基业所必需的才智需求，等着每代都同时出现大量文武俊才且绵延不绝是非常困难也是短视的；家族必须存在有效吸收外部人才的机制，古代靠乡谊、同僚、同窗、结交、联姻、收养、结拜，手段繁复说明古人完全理解这个道理；可惜现代人际关系原子化、社会伦理个人化之后，原有的社会性伦理约束已几乎崩溃，手段几乎尽数失效，但问题仍然存在。", "role": "definition"},
    {"unit_id": "U014", "paragraph_refs": ["P061", "P062", "P063"], "summary": "以“如之奈何？”与“（未完，待续）”结束正文，并推荐一个关于养成正确家风的集子；P063“家族答集／为什么中国没有出现百年家族企业？而欧美家族企业很常见？”疑为平台集子标签与关联文章标题混入正文。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为门当户对的问题对中国太重要，因此要好好说一说。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以反问与概率论证提出：如果人们算过名门世家和一般平民的生育率差异、子女幸存率差异，就会看到一个很朴素的事实——从数学概率上讲，你的整个祖宗链条里完全没有名门背景的可能性几乎为零；中国一共只有几千个姓，即使折算掉易姓、自号、在极近的年代归化的成分，这几千个姓里也尽皆曾有过不折不扣的名门，而且是屡屡崛起、层层叠叠的名门；所以你们全部是世家子弟，例外的可能性接近于零。", "evidence": ["E2", "E3", "E4", "E5", "E6"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为读者曾有历经数代乃至数十代先人的血汗总结出的黄金一般的世家传承、家族经验，只是忘记了；一忘就归零，多少代先人累世沉浮才明白的教训和禁忌都不知道了，只好从自己开始再经历若干代人的沉浮去重新知道。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为正是因为不知道这些，你才失去了“门户”，才有与别人的“门不当、户不对”；并反问你连门户都没有，怎么和有门户的去“门当户对”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者澄清这不是在说你家不够有钱于是和“家资万贯的家庭”不“门当户对”；若对方因此嫌弃你，你大可以放心——你有机会看着这家人在两代之内家破人亡、曲终人散；这样看待门户的家庭没有资格称“门户”，那不是你跟ta们门户不对，而是ta们跟你门户不对。", "evidence": ["E12", "E13", "E14", "E15"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为谈得上门户的世家懂得一个最朴素的道理：财富并不是最难获得的家族资源，传承和韧性才是，超越自身和时代的胸襟和自觉才是。", "evidence": ["E16", "E17"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出：你自己就是你后人的祖宗、是你自己家族的开创者；所谓“门当户对”，就是永世长存的家族和另一个永世长存的家族永远门当户对，一时之间谁盛谁衰对永世长存的家族而言都只是次要的、暂时的起伏。", "evidence": ["E18", "E19"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为讲究“门当户对”时正确的理解不是嫌你穷、不是嫌你不走运，而是嫌你没有身为一个家族祖宗的自觉；这种自觉性正是谈婚论嫁的基本门槛，迈过这个门槛，明白道理的世家大族不会认为你真的有什么门不当户不对，因为永生的东西分什么贫富贵贱；没这种自觉，就不是门当户对的问题，而是干脆最好不要祸害ta人。", "evidence": ["E20", "E21", "E22", "E23"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问要求读者想清楚：你有没有这个身为祖宗的自觉？什么叫做“身为祖宗的自觉”？", "evidence": ["E24", "E25"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为能明白这一点，你与这世上任何一家都只有对方能不能配得起你的问题，没有你配不配得起对方的问题；真正的世家一定看得懂这一点，看得到你有建立传承的自觉，对方就明白你这家族是必须重视的存在。", "evidence": ["E26", "E27"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为无论现在的势力强弱、一时尊卑如何，与世长存的家族之间只能互相平视；这才是人人平等的根子——永恒者必与永恒者平等。", "evidence": ["E28", "E29"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为三代而亡的“富家”只是不值得特别关注的烟尘，没有资格得到重视、也没有必要在意，他们彼此间的态度最终随着其消亡而毫无意义；能成其为门户的，尽皆门当户对，哪怕此时你贫ta富、你“贱”ta贵。", "evidence": ["E30", "E31"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出“祖宗的自觉”的定义：不再仅从自身的立场来看待成功，而是把成功看作一种家族事业；每一代的祖宗都不必力求速成，但要寻求为家族后代更进一步地夯实基础——一言以蔽之，要求事业，但更要求基业。", "evidence": ["E32", "E33", "E34"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者认为一人一代的能力总是有限的、机会总是难得的；若是总是存着“一定要在自己这一代当个富一代”的心，不断心怀侥幸、急功近利、想要铤而走险、一蹴而就，反而往往容易导致久作不兴，即使侥幸谋得浮财，家风不靖、根基不稳，这浮财不但不足以为福，反而足以为祸。", "evidence": ["E35"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把最大的问题归于“每一代人都想要在自己这一代完成大翻身”这种投机策略：没有理性的焦虑感驱使人不断投机取巧，越是失败后半生越要加倍投机取巧；要么一败涂地，要么侥幸成功后把侥幸当作成功之道加倍下注，直到再次失去一切还更加深陷；而以家族基业为考量中心的人可以轻松摆脱这种恶性循环。", "evidence": ["E36", "E37", "E38"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出正确的家族战略是每一代人都谋求为下一代创造更好的根基，哪怕每一代都只是拱一小卒、代代不息，也终有一天会走到“这一代人想不成功也难”的优势状态；而且这成功水到渠成、自自然然，且因代代家风的建设积累足以持久、能循环光大，财富可以开枝散叶、越发同气连枝，总体上更加稳固。", "evidence": ["E39", "E40"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这对身为列祖列宗的先辈也是一种解脱：创业先祖的任务不再是在自己这一代谋得亿万身家，而只是为家族后代留下可以继承的一份正资产和充分可借鉴的经验教训以及良好的教育；这是朴实、踏实、可以追求、不必依赖疯狂幸运的目标；而且一旦眼光从谋一世变为谋万世，做事反而容易有定性、有踏实的成果、有同志、有意料之外的帮助，比那些憋着心思必需一代成功的人更容易获得真实的成功。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出家族的边界是“基业所及，即为族人”，并再强调不要以血缘为界：要把与基业相关的所有人都视为家族成员，绝不能仅仅偏向自己的亲属或直系血亲；对志同道合处在同一生态中的平辈爱之如己，对托庇和仰赖这一生态生存并且尽力奉献的晚辈视如己出，这是拥有足够资源和人才来应对未来风险绝对不能少的安排。", "evidence": ["E44", "E45", "E46"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为越爱惜自己的子女血亲，就越要明白ta们需要这些不同姓、不沾亲的兄弟、姐妹、叔伯、姑姨；同姓族人是不容选择的，即使仅从概率上说也很难支撑一个基业所必需的才智需求，等着每一代都同时出现大量文武俊才且绵延不绝是非常困难也是短视的。", "evidence": ["E47", "E48"]},
    {"claim_id": "C020", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者指出家族必须存在一种能有效吸收外部人才的机制：在古代靠的是乡谊、同僚、同窗、结交、联姻、收养、结拜，手段繁复说明古人完全理解这个道理；可惜时过境迁，在现代人际关系原子化、社会伦理个人化之后，原有的对乡党、同学、朋友、结拜兄弟甚至联姻配偶、亲生子女的社会性伦理约束已经几乎崩溃，手段几乎已经尽数失效，但问题仍然存在。", "evidence": ["E49", "E50", "E51", "E52"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以“如之奈何？”收束正文，并标注“（未完，待续）”，未给出答案。", "evidence": ["E53", "E54"]}
   ],
   "argument_steps": [
    "点题并强调门当户对对中国的分量（P001-P002）。",
    "以概率论证提出“你们全部是世家子弟”（P003-P007）。",
    "指出先人的世家传承已被忘记、一忘归零（P008-P012）。",
    "推论失去“门户”的由来（P013-P015）。",
    "澄清门当户对不是嫌贫爱富（P016-P019）。",
    "指出世家真正的资源是传承、韧性与胸襟自觉（P020-P021）。",
    "给出“门当户对”的定义与基本门槛——“身为祖宗的自觉”（P022-P026）。",
    "以反问要求读者自省，并推出“只有对方配不配得起你”的判断（P027-P033）。",
    "判定三代而亡的“富家”与“尽皆门当户对”（P034-P035）。",
    "（7.9续）定义“祖宗的自觉”与“基业先于事业”（P036-P040）。",
    "说明代际投机策略的恶性循环，给出代代夯实根基的家族战略（P041-P049）。",
    "（7.10更新）界定家族以基业为界、不以血缘为界，并说明吸收外部人才机制的历史与现状（P050-P060）。",
    "以“如之奈何？”与“（未完，待续）”收束，并推荐相关集子（P061-P063）。"
   ],
   "concept_usage": [
    {"term": "门户", "meaning": "作者用它指家族经数代传承而形成的门第；失去门户即失去与有门户者“门当户对”的资格；能成其为门户者须与世长存。", "evidence": "P013、P014、P018、P035", "ambiguity": "“门户”的成立标准（代数、规模、传承形式）本文未给出。"},
    {"term": "门当户对", "meaning": "作者的定义：永世长存的家族和另一个永世长存的家族永远门当户对；讲究门当户对真正嫌的是“没有身为一个家族祖宗的自觉”，而非贫富。", "evidence": "P023、P024", "ambiguity": "该定义与通常婚配意义上的门当户对差异较大，作者未与其他用法对照。"},
    {"term": "身为祖宗的自觉", "meaning": "作者的定义：不再仅从自身立场看待成功，而把成功看作一种家族事业；每一代不必力求速成，但要为家族后代夯实基础。", "evidence": "P038、P039", "ambiguity": "作者反复以反问要求读者自己想清楚，未给出更细的判定方式。"},
    {"term": "基业、事业", "meaning": "作者以“要求事业，但更要求基业”区分两者：基业指可为后代承继、代代夯实的家族根基。", "evidence": "P040、P052", "ambiguity": "两者的界线与衡量方式本文未说明。"},
    {"term": "基业所及，即为族人", "meaning": "作者给出的家族边界原则：以基业相关范围为族人，而非以血缘为界。", "evidence": "P052、P053、P054", "ambiguity": "“基业所及”的具体范围本文未界定。"},
    {"term": "永世长存、永生", "meaning": "作者用来指家族意义上的长久延续（“永世长存的家族”“永生的东西分什么贫富贵贱”），在 P026 与宗教意义上的永生并不相同。", "evidence": "P023、P025、P032、P033", "ambiguity": "作者未对“永世长存”的时间尺度或条件作界定。"},
    {"term": "世家子弟", "meaning": "作者由概率论证得出的对读者的称谓：你们的祖宗链条里几乎不可能完全没有名门背景。", "evidence": "P007", "ambiguity": "该称谓依据作者的生育率与幸存率概率论证，未给数据来源。"}
   ],
   "examples_and_targets": [
    "名门世家与一般平民的生育率差异、子女幸存率差异（作者的概率论证依据，未给来源，待外部核查）",
    "中国几千个姓、易姓、自号、在极近的年代归化（作者的历史叙述，待外部核查）",
    "“富一代”“大翻身”“拱一小卒”（作者对投机心态与渐进战略的用语）",
    "三代而亡的“富家”（作者的评价对象）",
    "乡谊、同僚、同窗、结交、联姻、收养、结拜（作者列举的古代吸收外部人才的手段）",
    "现代人际关系原子化、社会伦理个人化（作者对当代状况的判断）",
    "“家族答集”与“为什么中国没有出现百年家族企业？而欧美家族企业很常见？”（P063，疑为平台集子标签与关联文章标题，非作者正文）"
   ],
   "conditions": [
    "“如果你们算过名门世家和一般平民的生育率差异、子女幸存率差异。你们会看到一个很朴素的事实”——概率结论以该计算为前提（P004）",
    "“即使折算掉易姓、自号、在极近的年代归化的成分”（P005）",
    "“对方如果因为这个来嫌弃你”（P017）",
    "“你真的迈过了这个门槛”（P025）",
    "“哪怕此时你贫ta富，你‘贱’ta贵”（P035）",
    "“哪怕每一代都只是拱一小卒”（P046）",
    "“即使侥幸谋得浮财”（P042）",
    "“即使仅仅从概率上说”（P057）",
    "“一旦你的眼光不再是谋一世，而是为了谋万世”（P049）"
   ],
   "rhetoric_and_tone": "布道式训诫与第二人称呼告：反复的“你们”与反问（“你们有没有想过……？”“你连门户都没有，怎么和有门户的去‘门当户对’呢？”），以概率与历史叙述作权威支撑，用对偶与格言式短句（“只是，你们忘记了。”重复出现、“要求事业，但更要求基业”“永恒者必与永恒者平等”），并以“（7.9续）”“（7.10更新）”“（未完，待续）”标记连载结构，末尾推荐集子；整体语气笃定、说教性强，兼具宣言感。",
   "unresolved_questions": [
    "P063“家族答集”及“为什么中国没有出现百年家族企业？而欧美家族企业很常见？”疑为平台集子标签与关联文章标题混入正文（lexical 结构未覆盖，text_tail_not_in_lexical），是否为作者本人所写未标注",
    "文中生育率／子女幸存率差异、姓氏数量、易姓与归化等论据未给来源，需外部核查",
    "“永世长存”“永生”在家族意义上的具体含义与判定标准本文未说明",
    "P037“（7.9续）”、P050“（7.10更新）”、P061“（未完，待续）”表明系连载；正文内部日期（7.9、7.10）与 published_at(2019-05-19) 的关系本文未说明",
    "P060“如之奈何？”为开放设问，作者未给出答案（文章未完成）",
    "“基业所及，即为族人”的实施方式（如收养、结拜在现代法律下如何成立）本文未说明",
    "updated_at(2025-10-12) 晚于 published_at(2019-05-19)，版本差异本文未说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "因为这个问题对中国太重要了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "从数学概率上讲，你的整个祖宗链条里完全没有名门背景的可能性几乎为零。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "中国一共只有几千个姓。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这几千个姓里也尽皆曾有过不折不扣的名门。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "而且是屡屡崛起的名门，层层叠叠的名门。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你们全部是世家子弟，例外的可能性接近于零。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "你们曾有历经数代乃至数十代先人的血汗总结出的黄金一般的世家传承、家族经验。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "你们一忘，就归零了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "只好从自己开始再经历这若干代人的沉浮去重新知道。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "是因为你不知道这些，你才失去了“门户”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "你连门户都没有，怎么和有门户的去“门当户对”呢？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "不要误会，这不是在说你家不够有钱于是和别的“家资万贯的家庭”不“门当户对”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "你有机会看着这家人在两代之内家破人亡、曲终人散去。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "这样看待门户的家庭，没有资格称“门户”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "那不是你跟ta们门户不对，而是ta们跟你门户不对。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "财富并不是最难获得的家族资源，传承和韧性才是。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "超越自身和时代的胸襟和自觉才是。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "你要知道，你自己就是你后人的祖宗，是你自己家族的开创者。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "永世长存的家族和另一个永世长存的家族，永远门当户对。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P024", "quote": "不是嫌你穷，不是嫌你不走运，而是嫌你没有身为一个家族祖宗的自觉。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P025", "quote": "永生的东西分什么贫富贵贱？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "这种自觉性其实正是谈婚论嫁的基本门槛。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P026", "quote": "而是干脆最好不要祸害ta人。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "你有没有这个身为祖宗的自觉？", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "什么叫做“身为祖宗的自觉”？你们不妨好好想一想清楚。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P029", "quote": "都只有对方能不能配得起你的问题，没有你配不配得起对方的问题。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P031", "quote": "看得到你有建立传承的自觉，对方就明白你这家族是必须重视的存在。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P032", "quote": "与世长存的家族之间只能互相平视。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P033", "quote": "这才是人人平等的根子——永恒者必与永恒者平等。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P034", "quote": "三代而亡的“富家”，只是不值得特别关注的烟尘。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P035", "quote": "能成其为门户的，尽皆门当户对。哪怕此时你贫ta富，你“贱”ta贵。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P038", "quote": "所谓祖宗的自觉，就是不再仅从自身的立场来看待成功，而是把成功看作一种家族事业。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P039", "quote": "每一代的祖宗都不必力求速成，但要寻求为家族后代更进一步的夯实基础。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P040", "quote": "一言以蔽之——要求事业，但更要求基业。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P042", "quote": "反而往往容易导致久作不兴", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P043", "quote": "这中间最大的问题就在于“每一代人都想要在自己这一代完成大翻身”这种投机策略。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P044", "quote": "直到再次失去一切，还要更加深陷。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P045", "quote": "以家族基业为考量中心的人就可以轻松的摆脱这种恶性循环。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P046", "quote": "正确的家族战略，是每一代人都谋求为下一代创造更好的根基", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P046", "quote": "也终有一天会走到“这一代人想不成功也难”的优势状态。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P047", "quote": "而只是为家族后代留下可以继承的一份正资产和充分可借鉴的经验教训，以及良好的教育而已。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P048", "quote": "这是一种朴实的、踏实的、可以追求，不必依赖什么疯狂的幸运的目标。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P049", "quote": "反而比那些憋着心思必需一代成功的人们更容易获得真实的成功。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P052", "quote": "这一点万分的重要——基业所及，即为族人。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P053", "quote": "不要——再强调一遍——不要以血缘为界。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P055", "quote": "对志同道合处在同一生态中的平辈爱之如己，对托庇和仰赖这一生态生存并且尽力奉献的晚辈视如己出", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P056", "quote": "你越是爱惜自己的子女血亲，就越是要明白ta们需要这些不同姓、不沾亲的兄弟、姐妹、叔伯、姑姨。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P057", "quote": "同姓族人是不容选择的，即使仅仅从概率上说，也很难支撑一个基业所必需的才智需求。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P058", "quote": "家族必须存在一种机制能有效的吸收外部的人才。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P058", "quote": "这靠的是乡谊、同僚、同窗、结交、联姻、收养、结拜。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P059", "quote": "原有的对乡党、同学、朋友、结拜兄弟甚至联姻配偶、亲生子女的社会性伦理约束已经几乎崩溃了。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P060", "quote": "手段几乎已经尽数失效，但问题仍然存在，如之奈何？", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P061", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E54", "paragraph_id": "P062", "quote": "下面这个集子，对于养成正确的家风都有关系，建议仔细的想想。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家族与门第", "婚姻与家庭", "教育传承", "社会流动"],
   "issue_candidates": ["什么才是门当户对", "门户的丧失与重建", "身为祖宗的自觉", "家族战略与代际积累", "家族边界与人才吸收"],
   "text_function_candidates": ["答疑", "训诫", "连载论述", "倡议"],
   "object_candidates": ["名门世家", "富家", "同姓族人", "现代家庭", "中国"],
   "working_keywords": ["门当户对", "门户", "世家子弟", "由富而贵", "祖宗的自觉", "基业", "事业", "富一代", "家族战略", "基业所及，即为族人", "乡谊", "结拜"]
  },
  "notes": "无图片节点。本文为知乎问答体并带连载标记（P037“（7.9续）”、P050“（7.10更新）”、P061“（未完，待续）”），正文未完成，P060 以“如之奈何？”作开放式收束。P063“家族答集”及“为什么中国没有出现百年家族企业？而欧美家族企业很常见？”为 lexical 未覆盖片段（text_tail_not_in_lexical），疑为平台集子标签与关联文章标题混入正文，已在 unresolved_questions 登记。文中概率论证与姓氏、归化等论据未给来源，需外部核查。updated_at(2025-10-12) 晚于 published_at(2019-05-19)，版本关系本文未说明。"
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
