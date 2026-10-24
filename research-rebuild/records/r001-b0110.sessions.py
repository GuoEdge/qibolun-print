# -*- coding: utf-8 -*-
"""批次 r001-b0110 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0110.sessions.py            # 写 out/r001-b0110.out.jsonl
  python3 records/r001-b0110.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0110"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0110.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "8388b3e4": {
  "analysis": {
   "question_context": "提问者（Q001）问：基督徒如何处理家人在信仰上的不理解、不支持甚至阻挠？提问者身份为面临家人阻挠的信徒，其立场只在 question 字段，不得归给作者。作者的回应不讨论教义或信仰权利，而是把问题改写成生活状态与履约结果问题：只要你过得健康、有成绩、有保障，就没人干预你信什么；家人真正不满的是你不给结果、只给解释。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "正面回答：生活状态好、工作收入事业到位，就不会有人干预信仰；理解与否不是关键，过得好不好才是关键。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "以“一个关键的秘密”引出反直觉命题：接受并不需要理解。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "以“你是否理解父亲的职业”作类比：不理解和不妨碍接受，若职业还支撑你的生活，你甚至欢迎它。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "指出你真正需要的是被接受；别人不接受的真实原因是“你拖累了人”，而你把原因误判为“不理解”，于是拼命解释。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "连串反问说明解释换不来饭、房租、放款、药费和汽油；只给解释不给结果就是剥削人。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "家人不满的不是信仰而是不给结果只给解释；“解释够好就会被放过”的经验其实只是对方为停止二次骚扰而放弃追究。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022"], "summary": "人不接受的是不能履约、不能守信的事实而非原因；失约伤人一次，逼人花时间放过你是第二次伤人。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024"], "summary": "条件性结论：能令人满意地履约就没人不接受你的信仰（还会有人好奇）；不能履约就没人能“理解你的信仰”，因为问题不在信仰。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "行动要求：去考试、做事、赚钱、保持健康、准时交付；停止逼人接受你的理由；只在别人提出请求时才解释。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P030", "P031", "P032", "P033"], "summary": "行动要求与义务：没做到时先谈赔偿，赔不起也要先谈；有义务避免对方因信任你受损，认赔是义务，赔不起就不要失约。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P034"], "summary": "收束：把这点改掉，再看有没有人干涉你的信仰。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要过得健康快乐、情绪稳定、工作有成绩、收入有保障、事业有方向，就不会有人来干预你信的是什么。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理解不理解不是关键，你过得健康不健康才是关键；接受并不需要理解。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你真正需要的是被接受而不是被理解；你真正的问题是拖累了人，别人因此不接受，而你误把原因当作“不理解”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "解释换不来饭、房租、放款、药费与汽油；只给解释不给结果就是在剥削人，还掠夺别人的时间来脱罪。", "evidence": ["E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人不接受你，是不能接受你不能履约、不能守信的事实，而不是不能接受其原因。", "evidence": ["E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "失约伤人一次，再占用别人的时间逼人放过你，是第二次伤人。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果你能令人满意地履行承诺和责任，就没人会“不接受你的信仰”，甚至会有人好奇、了解、参考、学习你的信仰。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果你不能令人满意地履行承诺和责任，就没人能“理解你的信仰”，因为人不能接受的是你行为的结果，而不是你的信仰如何。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人提出请求的时候才是你可以开始解释的时候，此外你没有强求别人花时间“理解”的权利。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没做到时应当开口直接谈赔偿而不是谈理由；你有义务避免让对方因信任你而受损失，对方宽免是仁慈，你认赔是义务。", "evidence": ["E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你如果赔不起，就不要失约。", "evidence": ["E17"]}
   ],
   "argument_steps": [
    "先给出正面答案：状态好则无人干预信仰，理解不是关键（P001—P003）。",
    "抛出反直觉前提：接受并不需要理解（P004—P005）。",
    "以“你并不理解父亲的职业”作类比，证明接受不依赖理解，甚至可因受益而欢迎（P006—P009）。",
    "把提问者的需要重新定义为“被接受”，并指出不被接受的真实原因是拖累了人（P010—P012）。",
    "用连串反问说明解释不产生实际结果，并给出“只给解释即剥削”的判断（P013—P014）。",
    "反驳“理解就会接受”的预设，指出所谓“解释够好就被放过”只是对方放弃追究（P015—P019）。",
    "把不接受的对象明确为失约的事实而非原因，并指出逼人理解构成二次伤害（P020—P022）。",
    "给出双向条件句：能履约则无人不接受信仰；不能履约则无人能“理解信仰”（P023—P024）。",
    "给出行动要求：先做事、准时交付；只在被请求时解释；失约先谈赔偿（P025—P032）。",
    "以“赔不起就不要失约”作收束并回指开场问题（P033—P034）。"
   ],
   "concept_usage": [
    {"term": "信仰", "meaning": "本文指提问者的宗教信仰；作者不讨论其内容，只把它当作被争夺的标签，主张争论焦点实为行为结果。", "evidence": "P024", "ambiguity": "作者未区分信仰内容与信仰者行为，全文不讨论教义对错。"},
    {"term": "理解 / 接受", "meaning": "作者将二者严格分开：理解是认知上的明白，接受是对既成事实的容纳；主张接受不以理解为条件。", "evidence": "P005", "ambiguity": "未说明在何种情形下接受仍需要最低限度的了解。"},
    {"term": "解释", "meaning": "特指失约或未交付结果后给出的理由说明；作者判定它不产生结果，且以占用他人时间为代价。", "evidence": "P014", "ambiguity": "未区分事前说明、事后说明与必要的协商。"},
    {"term": "剥削 / 掠夺人的时间", "meaning": "作者用以描述只给理由不给结果的单向索取。", "evidence": "P014", "ambiguity": "未给出适用边界，也未说明何种解释不算剥削。"},
    {"term": "赔偿 / 补偿", "meaning": "未达成结果时对对方的补救义务，含“赔不起先欠着也要先谈赔偿”。", "evidence": "P031", "ambiguity": "未说明赔偿标准、范围与履行期限。"},
    {"term": "履约 / 守约", "meaning": "按约定交付结果；作者把它设为判断信仰是否被接受的真正变量。", "evidence": "P032", "ambiguity": "未说明不可抗力或能力不足时的免责条件。"}
   ],
   "examples_and_targets": [
    "提问者及其家人（家人不理解、不支持甚至阻挠信仰）——回应对象，立场来自 question 字段，不属作者。",
    "“你真的理解你爹是做什么的吗”及其职业（工作内容、职责、风险、代价）——类比例证，支撑接受不依赖理解（P006—P009）。",
    "“说了五点到，你五点没到”——举例说明人不接受的是事实而非原因（P021）。",
    "“解释能当饭吃吗？解释能付房租吗？解释能让客户签字放款吗？”——反问式修辞材料（P013）。",
    "考试、做事、赚钱、保持健康、准时——行动清单（P025）。",
    "“从小到大你搞砸了事情，只要你解释得够好，就会被放过”——作者设为被反驳的成长经验（P018—P019）。"
   ],
   "conditions": [
    "前提条件：过得健康快乐、情绪稳定、工作有成绩、收入有保障、事业有方向（P001）。",
    "条件：只要他的职业没有妨碍你的生活（P008）；如果他的职业还给你的生活提供了支撑（P009）。",
    "条件句：如果你能令人满意地履行承诺和责任（P023）；如果你不能令人满意地履行承诺和责任（P024）。",
    "时点条件：什么时候你才可以开始解释？别人提出请求的时候（P028）；除这种时候没有强求别人花时间理解的权利（P029）。",
    "让步条件：赔偿不起，只能先欠着，也要先谈赔偿（P031）。",
    "限定：无论你填什么理由，都不能被接受（P026—P027）；你如果赔不起，就不要失约（P033）。"
   ],
   "rhetoric_and_tone": "全篇以第二人称“你”直接训诫，语气严厉、不留余地；大量反问连发（“解释能当饭吃吗？……”）、以“一个关键的秘密是——”与单独成段的标题句“接受并不需要理解。”制造断言节奏；对提问者的自我解释带有明显讽刺与责备（“而且你活该”），并以“五点没到”的生活场景作类比施压；结构为正面结论—秘密—类比—诊断—反驳—条件—行动要求—收束。",
   "unresolved_questions": [
    "提问者的具体处境（宗派、家人阻挠的具体形式）正文未说明，仅见于 question 字段。",
    "“谁也不会来干预你信的是什么”未界定干预的层面（家庭、社会、法律）与适用范围。",
    "作者把家人反对一律归因于“你不给结果”，未处理家人基于教义或宗教理由反对的情形。",
    "未说明“过得健康快乐、事业有方向”由谁判定、达到何种程度算达标。",
    "未讨论失约中不可抗力、能力不足或对方先违约的情形。",
    "“没有人能理解你的信仰”与“还会有人好奇你的信仰”之间的适用边界未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很简单，过得健康快乐，情绪稳定，工作有成绩，收入有保障，事业有方向，谁也不会来干预你信的是什么。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "理解不理解并不是关键，你过得健康不健康才是关键。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "接受并不需要理解。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "没有，只要他的职业没有妨碍你的生活。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "如果他的职业还给你的生活提供了支撑，你何止可以接受，你还很欢迎呢——哪怕你仍然根本不理解。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "你其实需要的是被接受，而不是需要被理解。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "你真正的问题是拖累了人，于是别人不接受。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "解释能当饭吃吗？解释能付房租吗？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "只给解释，不给结果，其实就是在剥削人。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "人不接受你，是因为不能接受你不能履约、不能守信的事实，而不是因为不能接受你不能履约、不能守信的原因。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "你没五点到，就是伤了人一次；你还要占用人的时间来逼人放过你，这是再伤人第二次。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "如果你能令人满意的履行你的承诺和责任，没人会“不接受你的信仰”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "如果你不能令人满意的履行你的承诺和责任，没人能“理解你的信仰”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P028", "quote": "什么时候你才可以开始解释？别人提出请求的时候。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P030", "quote": "人要养成习惯，什么事情没做到的时候，开口直接谈赔偿，而不要去谈“理由”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P032", "quote": "你有义务避免让对方因为信任你而受损失，你有责任避免造成这样的事实。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P033", "quote": "你如果赔不起，你就不要失约。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教信仰与社会关系", "家庭伦理", "责任与赔偿伦理"],
   "issue_candidates": ["信仰自由与家人不支持", "理解与接受的区分", "失约后的解释与赔偿义务"],
   "text_function_candidates": ["答问", "训诫", "论辩"],
   "object_candidates": ["提问者（基督徒）", "家人", "信仰", "承诺与履约", "赔偿"],
   "working_keywords": ["信仰自由", "理解", "接受", "解释", "履约", "赔偿"]
  },
  "notes": "正文完整读完（34 段，1330 字符），无图片节点；question 字段（Q001）属提问者，其处境仅作语境，不得归为作者主张。brief 与正文高度重合，仅作导航。元数据：published 2021-04-15，updated 2026-07-05。作者全程未讨论信仰内容本身，亦未给出宗教层面的辩护，属把问题改写为履约与赔偿问题。"
 },
 "68ccaf4f": {
  "analysis": {
   "question_context": "提问者（Q001）问：怎么才叫有责任感？提问者只是提出定义性问题，未给出自身立场。作者的回应是先给出一条规范原则（达成共识则给结果或给补偿），再把“把该原则视为自己理所当然的义务”这一自我认知定义为责任感，并由此推出关系效果与排除结论。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "先立原则：达成共识后要么给结果要么给未达成结果的补偿；把这条原则视为理所当然的义务，这种自我认知就是责任感。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "延伸定义：守约即尽责，无守约即有未尽的责；面对未尽的责应不否认、不逃避而力求补偿，以否认为耻、以逃避为羞、以不能补偿为憾。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "从关系另一方看：对方可相信要么拿到结果要么拿到赔偿；只有如此确信，关系才是有效的支撑、才值得维系和重视。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "推论：求生不易，人只欢迎能支撑生命者；失约且不补偿、也不认为自己有必要补偿的人应被排除；没有责任感的人必被避开。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P009"], "summary": "收束：别人都避之不及的人，自己想要过好的可能性为零。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "达成了一项共识，则要么给对方对应的结果，要么给对方没有达成结果的补偿。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把“结果或补偿”这条原则视为自己理所当然的义务，这种自我认知就叫做责任感。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "守约即尽责，没有守约就有未尽的责。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "面对未尽的责应当不否认、不逃避而是力求补偿，以否认为耻、以逃避为羞、以不能补偿为憾。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对关系另一方而言，责任感意味着对约定可以相信要么会拿到约定的结果，要么会拿到赔偿。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只有对方如此确信，关系才对对方成为一项有效的支撑，才是对方值得维系和重视的关系。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与人约定而失约、不能给出补偿、也不认为自己有必要补偿的人，都是只要能排除就应该排除的人。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个没有责任感的人必定要被别人避开，因为跟ta来往永远要吃哑巴亏。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "别人都避之不及的人，自己想要过好的可能性为零。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "立规范前提：达成共识即产生“给结果或给补偿”的义务（P001）。",
    "给出责任感的定义：把该义务视为自己理所当然的义务这种自我认知（P002）。",
    "补充定义：守约即尽责，未守约即产生未尽的责（P003）。",
    "规定对未尽责的态度：不否认、不逃避、力求补偿，并给出耻、羞、憾三种情感定位（P004）。",
    "转换视角到关系另一方：约定的可信内容为结果或赔偿（P005）。",
    "给出条件性判断：只有如此确信，关系才是有效的支撑、才值得维系（P006）。",
    "以“求生不易，人欢迎支撑自己生命的人”作前提，推出应排除失约且不补偿者（P007）。",
    "推出结论：无责任感者必被避开（P008）。",
    "收束为更强结论：被避开者过好的可能性为零（P009）。"
   ],
   "concept_usage": [
    {"term": "责任感", "meaning": "不是感受或态度，而是“把结果或补偿原则视为自己理所当然的义务”这一自我认知。", "evidence": "P002", "ambiguity": "未说明该自我认知如何形成、可否由外部判定。"},
    {"term": "共识 / 约定", "meaning": "触发结果或补偿义务的前提条件。", "evidence": "P001", "ambiguity": "未限定形式（口头、书面、默示）与范围。"},
    {"term": "守约 / 尽责 / 未尽的责", "meaning": "守约等于尽责；未守约即产生尚未了结的责任。", "evidence": "P003", "ambiguity": "未说明部分履行、迟延履行如何归类。"},
    {"term": "补偿 / 赔偿", "meaning": "未达成结果时的替代履行。", "evidence": "P004", "ambiguity": "未给出标准、额度、时限与无力补偿时的处理。"},
    {"term": "有效的支撑", "meaning": "关系对对方的价值判据：可指望拿到结果或赔偿。", "evidence": "P006", "ambiguity": "未说明除履约外其他关系价值是否计入。"},
    {"term": "排除", "meaning": "对失约且不补偿者的应然处置。", "evidence": "P007", "ambiguity": "未说明由谁排除、以何种方式排除。"}
   ],
   "examples_and_targets": [
    "无具体人物、事件或数据；文中唯一可辨认的背景陈述是“求生不易”（P007），作为推论前提而非例证。",
    "“别人都避之不及的人”（P009）——泛指对象，非具体人物。"
   ],
   "conditions": [
    "条件结构：达成了一项共识，则要么给你对应的结果，要么给你没有达成结果的补偿（P001）。",
    "条件：没有守约，就有未尽的责（P003）。",
    "条件：只有如此确信，你们的关系才对对方成为一项有效的支撑（P006）。",
    "限定对象：与人约定而失约，不能给出补偿、也不认为自己有必要补偿的人（P007）。",
    "依赖前提：求生不易，谁都欢迎能支撑自己生命的人而不是损害自己生命的人（P007）。"
   ],
   "rhetoric_and_tone": "短篇格言体与定义体，无称呼、无调侃；以“要么……要么……”的规范句式立论，用“以否认为耻，以逃避为羞，以不能补偿为憾”的排比强化态度要求；结论逐步加重，从“应该排除”到“必定要被避开”再到“可能性为零”，语气冷峻、确定，不作让步。",
   "unresolved_questions": [
    "“共识”的形式与范围未界定（口头、书面、默示承诺是否都算）。",
    "“补偿”的标准、额度、期限未说明；未讨论不可抗力或确实无力补偿的情形。",
    "未说明部分履行、迟延履行、对方先违约时是否仍适用同一结论。",
    "“别人都避之不及的人，自己想要过好的可能性为零”未给依据，也未限定观察范围。",
    "“应被排除”的执行主体与方式未说明。",
    "正文无例证，无法核对结论的经验适用范围。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "达成了一项共识，则要么给你对应的结果，要么给你没有达成结果的补偿。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "把这条原则视为自己理所当然的义务，这种自我认知就叫做责任感。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "守约即尽责，没有守约，就有未尽的责。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "面对未尽的责不否认、不逃避而是力求补偿，以否认为耻，以逃避为羞，以不能补偿为憾。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这对关系的另一方而言，就意味着对于跟你做的约定可以相信要么会拿到约定的结果，要么会拿到赔偿。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "只有如此确信，你们的关系才对对方成为一项有效的支撑，才是对方值得维系和重视的关系。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这就意味着与人约定而失约，不能给出补偿、也不认为自己有必要补偿的人都是只要能排除就应该排除的人。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "一个没有责任感的人，必定要被别人避开，因为跟ta来往永远要吃哑巴亏。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "而别人都避之不及的人，自己想要过好的可能性为零。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理与责任", "人际关系", "契约与信用"],
   "issue_candidates": ["责任感的定义", "失约后的补偿义务", "信用与关系维系"],
   "text_function_candidates": ["答问", "定义", "规范陈述"],
   "object_candidates": ["共识/约定", "结果与补偿", "责任感", "关系支撑"],
   "working_keywords": ["责任感", "守约", "尽责", "补偿", "信用"]
  },
  "notes": "正文完整读完（9 段，352 字符），无图片节点；question 字段仅为定义性提问，不含提问者立场。brief 与正文高度重合，仅作导航。元数据：published 2021-04-15，updated 2021-05-15。全文为规范定义式短篇，无例证、无数据、无引用，因此未列具体例证对象。"
 },
 "7a5b2d93": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么网络小说中，作者越是用心写，作品成绩（相对）越不好？提问者预设了“用心写”与“成绩差”的相关，并期待解释。作者不承认该预设中的“用心”是服务读者的用心，而是把“用心的自我表达”当作向观众索取的对象加以质疑，并以“杀必死”（服务观众）作为评判标准。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "反问开篇：别人为什么要看你的“自我表达”；并以“不是谁肯脱就都有人愿意看”作比。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "对比纯爽文：价值廉价甚至有害，但至少有服务观众的心（“杀必死”）。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "判断：这种“用心的自我表达”本应给观众钱，却既要观众站台喝彩又要观众付钱，是欺负人。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "条件分支：若属梵高式超越当代人的用心，就不要指望一出版就大卖，需长期等待读者成熟并保持代差继续写，日后可能成为经典。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "结论重申：这仍不是“自我表达”，仍是“杀必死”，并以方言反问收尾。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑读者有何理由去看作者的“自我表达”：不是谁肯脱就都有人愿意看。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "纯爽文提供的价值虽然廉价甚至有害，但好歹存着服务观众（“杀必死”）的心。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里说的“用心的自我表达”应该给观众钱，不能既要观众站台喝彩又要观众给钱。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果是类似梵高这种超越到当代人懂不了的另一种用心，就不要指望一出版就大卖赚钱。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这类写作要板凳坐得十年冷、等人类慢慢成熟，期间保持与读者的代差继续写，等读者读明白第一部时后面几部会成为经典。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即便是梵高式的用心，那仍然不是“自我表达”，而仍然是“杀必死”。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "以反问否定“读者有义务看你的自我表达”这一隐含前提（P001—P002）。",
    "引入“杀必死”作为评价尺度，并指出纯爽文至少在服务观众上有可取之处（P003—P004）。",
    "据此判断被称作“用心的自我表达”的作品对观众形成双重索取（要喝彩又要钱）（P005—P006）。",
    "给出条件分支：若用心属于梵高式超越当代理解，则应接受长期不畅销（P007）。",
    "给出该分支下的做法：长期等待读者成熟、保持代差继续写（P008）。",
    "收束并回到“杀必死”标准，用方言反问强化结论（P009—P011）。"
   ],
   "concept_usage": [
    {"term": "自我表达", "meaning": "作者指以自身表达为中心、不为观众提供服务的写作，与“杀必死”相对。", "evidence": "P001", "ambiguity": "全文未给出定义，只能从与纯爽文、杀必死的对照中推测。"},
    {"term": "杀必死", "meaning": "音译自日语 service，指存着服务观众的心；作者用它作为作品是否值得观众付费的标准。", "evidence": "P003", "ambiguity": "文中未定义，语义依赖语境与方言口语，属模糊关键词。"},
    {"term": "纯爽文", "meaning": "作者认为其价值廉价甚至有害，但仍有服务观众的自觉。", "evidence": "P003", "ambiguity": "未举例、未界定范围。"},
    {"term": "梵高", "meaning": "作为“超越到当代人懂不了”的用心之例，用于说明另一种用心需承受长期不被理解。", "evidence": "P007", "ambiguity": "以人物作类比，正文未提供史实依据。"},
    {"term": "代差", "meaning": "作者主张写作者应持续保持与读者理解水平的差距。", "evidence": "P008", "ambiguity": "未说明代差如何度量与维持。"}
   ],
   "examples_and_targets": [
    "网络小说中“越用心成绩越差”的作者——提问者所指对象，也是作者质疑“自我表达”说法的对象。",
    "纯爽文——对比对象，兼作反面参照（价值廉价甚至有害但服务观众）。",
    "梵高——类比人物，代表超越当代人理解的创作者。",
    "“不是谁肯脱就都有人愿意看”——类比修辞材料。",
    "“板凳坐得十年冷”——俗语，作长期等待的修辞。"
   ],
   "conditions": [
    "如果是另一种用心，类似梵高这种超越到当代人懂不了的（P007）→ 则不要指望一出版就大卖赚钱（P007）。",
    "这期间继续保持与读者的代差继续写（P008）为条件性做法，依赖“读者慢慢成熟”这一前提。",
    "“等读者们读明白你的第一部的时候”是后续结果成立的时间条件（P008）。",
    "“不是谁肯脱就都有人愿意看”隐含条件：观众是否愿意看不由作者单方决定（P002）。"
   ],
   "rhetoric_and_tone": "全篇口语化、戏谑与讽刺并重：开篇即反问，用“不是谁肯脱就都有人愿意看”的粗俗类比施压；反复敲击关键词“杀必死”，末尾以“杀必死！”“侬懂伐？！”的吴语方言呼喊收束，形成调侃式训诫；对“自我表达”的立场带明显讥讽（“这也太欺负人了”），但对梵高式用心给出条件性同情。",
   "unresolved_questions": [
    "“杀必死”未在文中定义，其确切含义与判定标准依赖语境，存在歧义。",
    "作者未直接回答提问中的机制问题（“越用心成绩（相对）越不好”如何计量、何以相关）。",
    "“成绩”一词未界定（销量、订阅、评价或平台推荐）。",
    "梵高的例子属外部史实，正文未给来源，需外部核查。",
    "“保持与读者的代差继续写”缺少可操作标准，也未说明作者如何判断读者已成熟。",
    "文中两处标点形态不一（“杀必死“ 的引号收尾），疑为原文录入差异，不影响语义但影响逐字引用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "别人为什么要看你的“自我表达”？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不是谁肯脱就都有人愿意看的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "纯爽文虽然提供的价值很廉价甚至有害，但是好歹是存着杀必死的心的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这里说的这种“用心的自我表达”，应该给观众钱啊，怎么能既要观众给自己站台喝彩，还要观众给钱？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "如果是另一种用心，类似梵高这种超越到当代人懂不了的，那么就不要指望一出版就大卖赚钱。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "那要板凳坐得十年冷，等着人类慢慢成熟。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "这样等读者们读明白你的第一部的时候，后面几部自然瞬间成为经典。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "而这仍然不是“自我表达”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P006", "quote": "这也太欺负人了。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["网络文学", "创作与读者关系", "内容付费"],
   "issue_candidates": ["自我表达与读者服务", "用心写作与作品成绩的关系", "作者与读者的交换关系"],
   "text_function_candidates": ["答问", "讽刺", "评论"],
   "object_candidates": ["网络小说作者", "纯爽文", "读者/观众", "自我表达"],
   "working_keywords": ["自我表达", "杀必死", "爽文", "用心写", "读者"]
  },
  "notes": "正文完整读完（11 段，277 字符），无图片节点；question 字段的预设（用心写→成绩差）属提问者，不得归为作者主张。brief 与正文高度重合，仅作导航。元数据：published 2021-04-15，updated 2025-09-26。文中“杀必死”为日语 service 音译，作者未定义；“侬懂伐”为吴语方言，保留原文。"
 },
 "98e8a2f8": {
  "analysis": {
   "question_context": "提问者（Q001）转述并询问：如何理解 14 日发布的央行工作论文中提到的「东南亚国家掉入中等收入陷阱」原因之一是「文科生太多」？提问者只是求解释，未表明赞同或反对。作者的回应分三层：一是逐条拆解该论文关于年轻人口与老龄化的假设，二是质疑该结论未先界定“文科”，三是从历史与文化角度反推“人文决定技术”，立场明显反对该论文归因，但作者的反对立场属作者本人，提问者立场不得混入。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总评：该论断含太多靠不住的假设。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "反驳“年轻人口＝劳动力”：晚清平均寿命三十几岁、人口结构年轻而生产力弱；按同逻辑非洲多国会走向太空。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "美国移民年轻化的构成是拉美裔、非裔移民与生育，是动力还是阻力难说；老年人口较多反而使治安、交通等成本下降。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009"], "summary": "脑力劳动效费比随年龄上升，企业偏好记录良好的老白领；以库克、乔布斯、盖茨反问老年人是否累赘。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "“年轻人多则生产力一定高”与“钢多就跑得快”无本质区别，是一种迷信。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "“人口老龄化危机”严格说是前现代问题；现代工业体力输出已主要靠机械，劳动密集型产业将成为历史。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "不是内卷迫使少生，而是过多年轻人口本身成问题，社会在本能调节人口结构。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "生育意愿低源于工作机会极端化的预期；老年人多不指望账户清零后给国家添负担，宁取“尊严绝命”。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "日本“老龄化危机”是错觉；若真是终极危机，难以解释十几亿人口的发达国家全都无为，可能是人家并没有那么疼。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032", "P033", "P034"], "summary": "以新冠数万亿支出与核废水问题作对照：若真视老龄化为根本威胁，应见巨额投入与放开移民、领养、单身税等措施；未穷尽手段就难说“很重视”。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P035", "P036", "P037"], "summary": "回到文科议题：该结论须先说明什么叫“文科”，并列经济学管理学、图书情报学、法学、新闻学、科学哲学、伦理学、艺术反问。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P038", "P039", "P040"], "summary": "反问对方是否还嫌中国文科太多；作者认为现有文科生太少、太不够用。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P041"], "summary": "搞来料加工确实不需要“文科”，但换方向当甲方就会知道“生产关系反向约束生产力发展”。", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "以先会作诗者灭邻居、女真人、马拉松等例说明技术先发优势有限，真正决定胜负的是“文科”的差距；创造这个中国的是文科生；反问换詹天佑是否成功率更高。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054", "P055"], "summary": "中国对文科的偏见很愚蠢，原因是文科教得烂、文科生未获正确充分训练，导致宏观软实力劣势与文科生个人困难；但据此削弱文科加强理工科如因前轮漏气而拆掉前轮。", "role": "claim"},
    {"unit_id": "U016", "paragraph_refs": ["P056", "P057", "P058", "P059", "P060", "P061"], "summary": "理工科解决人与自然、生产问题，人文解决人与人、分配问题；引孔子“不患寡而患不均”；理工让你能战，人文让你能胜。", "role": "reason"},
    {"unit_id": "U017", "paragraph_refs": ["P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073"], "summary": "理工科崇拜源于把百年国耻认定为技术失败；作者主张文化精神落后决定技术落后，中国是作为文化落后国家输给文化先进国家；人文赢则理工迟早必赢，人文输则理工迟早必输；所有胜利本质是文化胜利。", "role": "conclusion"},
    {"unit_id": "U018", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079"], "summary": "结尾讽刺：轻视文科的是一帮文理都不好的人，因为想把理工学到深处就会发现语文不行则逻辑必然稀烂。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的对象主张：东南亚国家掉入中等收入陷阱的原因之一是“文科生太多”；该主张来自央行工作论文并经提问者转述，作者随后质疑其未先界定“文科”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该论断里面含太多靠不住的假设。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "年轻人口不一定是“劳动力”：晚清中国平均寿命只有三十几岁、人口结构够年轻，但生产力并不强；按同一逻辑，非洲无数国家应很快走向太空。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "美国依赖移民呈现的年轻化，主要年轻在拉美裔、非裔的大量移民和生育上，将来是动力还是阻力还难说。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老年人口较多时治安、交通等成本会直线下降，且脑力劳动的效费比随年龄增长反而上升；稳定经营的企业偏好记录良好的老白领，老年人并非累赘。", "evidence": ["E6", "E7", "E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "认为“年轻人多，未来生产力一定就高”与“车用了很多钢就跑得贼快”没有本质区别，是一种迷信。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“人口老龄化危机”严格意义上是一个前现代问题；现在体力输出已主要靠机械，劳动密集型产业会成为历史，低端产业也将高度自动化。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是“内卷”“高压生存环境”迫使人类减少生育，而是过多的年轻人口本身成了问题，社会在本能地调节人口结构。", "evidence": ["E14"]},
    {"claim_id": "C009", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者转述：老百姓不生是因为深深觉得将来工作机会会极端化（要么金领职位，要么吃救济低保）。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_reported", "attribution": "author", "modality": "qualified", "statement": "作者认为大多数中国老年人的实际想法是不指望账户清零之后再给国家添负担，宁可“尊严绝命”。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "日本“老龄化危机”喊了二十年，但那是中国自己坐在火箭上看谁都慢产生的错觉；如果老龄化是必须逆转的终极危机，难以解释十几亿人口的发达国家全都无为，可能是因为人家并没有那么疼。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若老龄化真是根本威胁，就应见诸每年数万亿投入、放开婚姻移民与领养第三世界儿童、单身税、挪出医疗护理预算等必要手段；未穷尽必要手段就难以解释“很重视”。", "evidence": ["E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "“文科生太多挂钩中等收入陷阱”的结论应先说明什么叫“文科”，而经济学管理学、图书情报学、法学、新闻学、科学哲学、伦理学、艺术是否算文科并不清楚。", "evidence": ["E1", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国现有的文科生太少、太不够用，不应再减少；搞来料加工确实不需要“文科”，但换方向当甲方就会知道“生产关系反向约束生产力发展”。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生产技术带来的优势顶多维持五十、一百年，真正决定胜负的是“文科”的差距；创造这个中国的就是个不折不扣的文科生。", "evidence": ["E27", "E28", "E29"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国对文科的偏见很愚蠢，原因是文科教得很烂、文科生没有得到正确和充分的训练，这在宏观上造成文化、艺术、意识形态、组织协作、企业管理上的劣势，在微观上造成文科生个人困难。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "据此得出“文科生太多导致中等收入陷阱”并主张削弱文科加强理工科，就像因为前轮漏气而决定去掉前轮、把后轮气打足。", "evidence": ["E33"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理工科解决人与自然之间的问题，人文、史、哲、经管解决人与人之间的问题；理工解决生产问题，人文解决分配问题。", "evidence": ["E34", "E35"]},
    {"claim_id": "C019", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引孔子之言：不患寡而患不均，不患贫而患不安，均无贫、和无寡、安无倾，远人不服则修文德以来之。", "evidence": ["E36"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理工让你能战，是人文让你能胜。", "evidence": ["E37"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国不是作为文化先进的国家而输给技术先进的国家，而是作为文化落后的国家输给文化先进的国家；技术不如人只是输掉的具体形式，不是原因，是输在人文而不是输在理工。", "evidence": ["E38", "E39", "E40"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "人文赢了理工迟早必赢，人文输了理工迟早必输；所有的胜利本质上都是文化胜利，军事胜利、技术胜利只是文化胜利的支付方式。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "其实轻视文科的，是一帮文科理科都不好、也注定好不到哪去的人；真想把理工学到深处就会发现语文不行则逻辑必然稀烂。", "evidence": ["E44", "E45"]}
   ],
   "argument_steps": [
    "总评：该论断靠不住的假设太多（P001—P002）。",
    "拆解“年轻人口＝劳动力”的假设，用晚清寿命与非洲作反例与归谬（P003—P004）。",
    "拆解“移民年轻化带来优势”的假设，指出构成与不确定性（P005），并转而指出老年人口反而降低治安交通成本（P006）。",
    "以脑力劳动效费比、企业用人偏好与库克/乔布斯/盖茨之例反驳“老年人是累赘”（P007—P009）。",
    "指出“年轻人多则生产力必然高”是迷信，以“钢多跑得快”作类比（P010—P011）。",
    "论证“老龄化危机”是前现代问题：现代生产已机械化、劳动密集型将成历史（P012—P016）。",
    "给出替代解释：不是内卷迫使少生，而是过多年轻人口本身成问题，社会在调节人口结构（P017—P019）。",
    "转述生育意愿与老年人心态，支撑“危机”判断的落空（P020—P026）。",
    "以日本与发达国家作反例，反问若真是终极危机何以无人全力应对（P027—P030）。",
    "以新冠支出与核废水作对照，指出未穷尽必要手段就不能声称“很重视”（P031—P034）。",
    "回到文科议题：要求先界定“文科”，以学科列举反问（P035—P037）。",
    "反问对方是否还嫌文科太多，主张现有文科生太少（P038—P040）。",
    "让步：来料加工确实不需要文科，但当甲方会验证生产关系的反向约束（P041）。",
    "以历史例证（作诗者、女真人、马拉松）说明技术先发优势有限，文科差距才决定胜负（P042—P049）。",
    "给出对偏见的诊断：文科教得烂造成劣势，但削弱文科如拆前轮（P050—P055）。",
    "给出分工论并引孔子，得出“理工让你能战，人文让你能胜”（P056—P061）。",
    "追溯理工科崇拜来源并给出文化决定论结论（P062—P073）。",
    "结尾讽刺轻视文科者自身文理皆差（P074—P079）。"
   ],
   "concept_usage": [
    {"term": "文科", "meaning": "文中未给固定定义；作者先要求界定，再列举多个学科反问归属，并把“吟诗作对”与人文相区分。", "evidence": "P036", "ambiguity": "作者自己要求先定义，但全文未给出最终定义，所指随段落滑动（P037、P065）。"},
    {"term": "中等收入陷阱", "meaning": "引述央行工作论文用语，作者的质疑集中在其归因而非概念本身。", "evidence": "P035", "ambiguity": "正文未展开该概念的定义与测度。"},
    {"term": "劳动力", "meaning": "作者质疑“年轻人口＝劳动力”的等同，主张其取决于生产结构与训练。", "evidence": "P003", "ambiguity": "未给出替代判据。"},
    {"term": "人口老龄化危机", "meaning": "作者称其为前现代问题，是建立在旧生产结构上的判断。", "evidence": "P012", "ambiguity": "未说明该判断适用的国家与产业条件。"},
    {"term": "生产关系反向约束生产力发展", "meaning": "作者用来指以甲方位置（需求与组织端）反制生产端的机制。", "evidence": "P041", "ambiguity": "仅一句带过，未展开论证。"},
    {"term": "文化胜利", "meaning": "作者主张一切胜利的本质，军事与技术胜利只是其支付方式。", "evidence": "P073", "ambiguity": "未定义“文化”的范围与胜负判据。"},
    {"term": "软实力", "meaning": "作者用其指中国在文化、艺术、意识形态、组织协作等宏观方面的劣势。", "evidence": "P052", "ambiguity": "未给出衡量方式。"}
   ],
   "examples_and_targets": [
    "央行工作论文关于“东南亚掉入中等收入陷阱因文科生太多”的结论——被反驳对象（经提问者转述，正文未引原文）。",
    "晚清中国平均寿命三十几岁——反例（P003）。",
    "非洲无数国家的年轻年龄结构——归谬材料（P004）。",
    "美国拉美裔、非裔移民与生育——例证（P005）；抖音、飞叶子、炒币、零元购——讽刺修辞材料（P005）。",
    "库克、乔布斯、盖茨——反问式例证，说明老年人非累赘（P009）。",
    "福特T型车流水线、雅马哈制作所拿木头削螺旋桨——前现代生产的类比（P012）。",
    "送外卖、开滴滴、摘棉花、插秧、手撕包菜、收银——反问列举（P021）。",
    "猪头肉与糠咽菜——口语化类比（P024）。",
    "日本“老龄化危机”与被称“失败”的治理——被反驳对象（P027—P028）。",
    "新冠防治发行数万亿美欧元——对比论据（P031）；婚姻移民、领养第三世界儿童、单身税、医疗保健护理预算——反事实要求（P033）；核废水与三鞠躬——类比与讽刺材料（P034）。",
    "鸦片战争以来的百年国耻被认定为“技术的失败”——被作者质疑的流行认定（P063）。",
    "女真人——历史例证（P044）；马拉松——类比（P046）；詹天佑——反问例证（P049）。",
    "孔子“不患寡而患不均”一段——引用材料（P060）。",
    "支付宝账户与储蓄账户——类比（P073）。",
    "前轮漏气去拆前轮——类比（P053）。"
   ],
   "conditions": [
    "归谬前提：按“年轻人口即劳动力”的结构（P004）。",
    "条件：如果老龄化是这样一种终极危机，必须逆转（P029）；老龄化据说是要搞成人去楼空江山易姓的（P032）；即使摊到三十年来花（P032）。",
    "条件：如果只把吟诗作对视为“文科”，那的确是（P065）。",
    "条件：你换一个方向当一下甲方试试（P041）。",
    "时间尺度限定：生产技术优势顶多维持五十、一百年（P043）；两国相争动辄两三百年，两教相争动辄一两千年（P045）。",
    "依赖对象：现在世界工业的人口结构到底是什么样子、车间里还有多少重体力操作（P013—P014）。",
    "限定：等到“人文赢了／人文输了”两种条件下理工的必然结果（P071—P072）。"
   ],
   "rhetoric_and_tone": "强烈论辩体，语气辛辣、嘲讽且带训诫：通篇密集反问（“你还要减少点？！”），以归谬（非洲走向太空）和类比（钢多跑得快、前轮漏气、马拉松、支付宝）施压；混用网络语与口语（md、tnnd、好伐、爷、飞叶子、零元购）拉低对手立场；引用孔子提升人文一侧的分量；结构呈“拆解假设—转移论题到老龄化—以日本与发达国家反证—回到文科—追溯偏见来源—给出文化决定论”，段落多为短句连发，结论以格言式断言收束。",
   "unresolved_questions": [
    "P074 内容为“学理工科真的会影响文笔表达吗？怎么样可以兼顾？”，标注为 lexical 未覆盖片段，疑为平台相关问题或页面元素混入，是否属作者正文需外部核验，本记录未据其立论。",
    "央行工作论文原文未在正文引出，作者所反驳的具体表述只能依据提问者转述，需外部核查原论文。",
    "P048“创造这个中国的就是个不折不扣的文科生”未点名主体（上下文及 P049 提及詹天佑，疑指某位政治人物），文本未明说，不得代填。",
    "作者要求先界定“文科”，但全文始终未给出自己的最终定义，导致多处结论的适用范围不明。",
    "“每年一千几百亿美元的医疗保健护理预算”“晚清平均寿命三十几岁”“女真人的技术优势”等数据与史实均未给来源，需外部核查。",
    "P034“三鞠躬”所指事件未在文中说明。",
    "“所有胜利本质上都是文化胜利”为强断言，未给出反例处理或判据。",
    "P039 有“md”等粗口缩写，P005 的族裔表述带有明显刻板印象，属作者修辞，记录如实保留但不作正当性判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P035", "quote": "至于说“文科生太多挂钩中等收入陷阱”这种结论。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P001", "quote": "这里面有太多靠不住的假设。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "年轻人口就一定是“劳动力”吗？晚清中国的平均寿命也只有三十几岁，人口结构够年轻了吧？生产力很强吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "按这结构非洲无数国家应该很快会走向太空", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "他们到底是更擅长造航天飞机还是更擅长抖音、飞叶子、炒币和零元购还真不好说。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "倒是老年人口较多，治安、交通等种种成本会直线下降倒是真的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "并且脑力劳动的效费比随年龄增长反而会上升。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "很多稳定经营的企业对记录良好的老白领爱不释手好伐？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "谁说老年人就是累赘？库克是累赘吗？乔布斯是累赘吗？盖茨是累赘吗？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "认为“年轻人多，未来生产力一定就高”，跟“这车用了很多钢，肯定跑得贼快”有什么本质区别？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "这是一种迷信。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "“人口老龄化危机”严格意义上说是一个前现代问题", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "现在真正担任体力输出的已经主要是机械了，“劳动密集型产业”会眼睁睁的变成历史，即使是“低端产业”也会是高度自动化的。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "根本不是什么“内卷”“高压生存环境”迫使人类减少生育，而是过多的年轻人口本身成了问题，于是社会本能的在调节人口结构。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "为什么老百姓不生？因为老百姓深深的觉得将来工作机会会极端化——要么就是硕士博士毕业金领职位，要么就是吃救济低保。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "这怕是大多数，甚至绝大多数中国老年人的实际想法。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "尊严绝命。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P027", "quote": "坦白说，那是中国自己坐在火箭上看谁都慢产生的错觉", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "如果老龄化是这样一种终极危机，必须逆转，那么是那十几亿人口的发达国家全都是白痴，故意眼睁睁的看着自己衰落吗？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "有没有可能是因为人家自己并没有我们觉得的那么疼？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "大幅放开和鼓励婚姻移民该有的吧？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P034", "quote": "你既然没有穷尽必要手段，你怎么解释你的“很重视”？以三鞠躬为证吗？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P036", "quote": "你先说好什么叫“文科”吧。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "你还嫌中国文科太多？？你还要减少点？！", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P039", "quote": "连现有的文科生都嫌太少、太不够用", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "搞来料加工确实不需要“文科”，你换一个方向当一下甲方试试？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P043", "quote": "在历史的长河中，生产技术带来的优势顶多维持五十、一百年", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P047", "quote": "真正决定胜负的，是“文科”的差距。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P048", "quote": "创造这个中国的就是个不折不扣的文科生。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P050", "quote": "中国对文科的偏见是很愚蠢的。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P051", "quote": "为什么对文科有偏见？因为中国文科教得很烂，文科生远远没有得到正确和充分的训练。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P052", "quote": "软实力羸弱到令人发指，在微观上导致了文科生们自己个人的困难——学习离实战的距离比理科生更远。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P053", "quote": "但据此得出“文科生太多导致中等收入陷阱”这种结论，甚至喊着进一步削弱文科加强理工科", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P056", "quote": "理工科是在解决人与自然之间的问题，文、史、哲、经管这些人文学科是在解决人与人之间的问题。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P058", "quote": "理工在解决生产问题，人文在解决分配问题。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P060", "quote": "丘也闻有国有家者，不患寡而患不均，不患贫而患不安。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P061", "quote": "理工让你能战，是人文让你能胜。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P067", "quote": "恰恰是文化精神的落后决定了技术的落后。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P069", "quote": "而是作为文化落后的国家输给了文化先进的国家，技术上技不如人，只是输掉的具体形式，而不是输掉的原因。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P070", "quote": "是输在人文，而不是输在理工。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P071", "quote": "人文赢了，理工迟早必赢。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P072", "quote": "人文输了，理工迟早必输。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P073", "quote": "所有的胜利本质上都是文化胜利，军事胜利、技术胜利，只是文化胜利的支付方式。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P076", "quote": "其实轻视文科的，是一帮文科理科都不好、也注定好不到哪去的人。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P078", "quote": "因为你真的想把理工科学到深处，你会发现语文不行，逻辑必然稀烂。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人口与经济政策", "学科分工与教育", "历史与文化比较"],
   "issue_candidates": ["中等收入陷阱的归因", "文科生数量与经济发展的关系", "老龄化与劳动力结构", "理工科崇拜与人文价值"],
   "text_function_candidates": ["答问", "论辩", "反驳", "政策评论"],
   "object_candidates": ["央行工作论文", "文科/理工科", "老龄人口", "东南亚与中等收入陷阱"],
   "working_keywords": ["文科", "中等收入陷阱", "老龄化", "劳动力", "人口结构", "文化胜利"]
  },
  "notes": "正文完整读完（79 段，3085 字符），无图片节点；question 字段属提问者，其转述的央行工作论文主张在本记录中标为 opponent_view，不得写成作者说法。brief 与正文高度重合，仅作导航。元数据：published 2021-04-16，updated 2026-05-20。P074 为 lexical 未覆盖片段，内容看似平台相关问题文本，已记入未决问题，未据此立论。"
 },
 "eefce09c": {
  "analysis": {
   "question_context": "提问者（Q001）是老师，称自己的学生认为曹操屠城是合理的，问要怎么开导学生才能让他认识曹操屠城不合理；提问者本人持“曹操屠城不合理”的立场，并希望作者提供开导方法。作者不裁决该史事是否合理，也不给出开导方案，而是质疑问题中的关键词：“合理”指什么理？双方是否在谈同一个问题？作者的立场是方法论层面的澄清，不得把提问者的立场归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "追问“合理”指什么理，并列举公理、常理、道理、情理、义理、法理。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "指出双方各合自己认定的理，用同样文字主张的其实是两个不同命题。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "以南方人讨厌地瓜、北方人爱吃地瓜的类比说明双方互觉不可理喻。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "以“南方地瓜／北方地瓜”两图与省略号作停顿，反问“接着吵啊”，指出这样吵不可能说服对方。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P014"], "summary": "结论性方法：论证的前提是先搞清是否在谈同一个问题，否则不存在讨论的基础。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016"], "summary": "附带规则：不要指着别人在立论前给的定义喊“偷换概念”，那会丢老师和爹妈的脸。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "调侃收尾：想通这个道理、养好这个习惯可以多活五年，还可以美白、补肾。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "讨论前必须先问：“合理”到底是指什么理——公理、常理、道理、情理、义理还是法理。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他合的是他认定的那个理，你不合的是你认定的这个理；此理恐非彼理，所以双方用同样的文字主张的是完全不同的两个命题。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以南方人／北方人对地瓜的相反评价作类比：双方吵得天翻地覆且互相觉得对方不可理喻，说明分歧源于各自认定的标准不同。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样争论不可能说服对方。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "论证问题的前提，是要先搞清楚双方谈论的到底是不是同一个问题、是一个什么问题；否则不存在讨论的基础。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要指着别人在立论前给的定义喊“偷换概念”，那是论文作者普遍有的特权；那样做会丢老师和爹妈的脸。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想通这个道理、养好这个习惯，可以多活五年，还可以美白（调侃式断言）。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者未在正文中判定曹操屠城是否合理，也未给出提问者所要的“开导”方案，而是把问题改写为：双方所说的“理”是否同一个理。", "evidence": ["E3"]}
   ],
   "argument_steps": [
    "不直接回答“曹操屠城是否合理”，先追问论题关键词“合理”的所指（P001—P002）。",
    "指出争论双方各以其认定的“理”为标准，同一表述下是两个不同命题（P003）。",
    "用南北地瓜口味之争作类比，展示标准不同时争论如何互不可理喻（P004—P008）。",
    "以两张图和省略号作停顿，反问“接着吵啊”，指出争吵无法产生说服（P009—P013）。",
    "得出前提性规则：先确认是否在谈同一个问题，否则不存在讨论基础（P014）。",
    "附带给出辩论规则：不得指责他人在立论前给出的定义是“偷换概念”（P015—P016）。",
    "以多活五年、美白、补肾的戏谑收尾（P017—P019）。"
   ],
   "concept_usage": [
    {"term": "合理", "meaning": "文中未给出单一含义；作者列举公理、常理、道理、情理、义理、法理六种可能，指出各人实际使用的是自己认定的那一种。", "evidence": "P002", "ambiguity": "作者始终未说明哪一种是正确的“理”，也未给出通行标准。"},
    {"term": "理", "meaning": "各方据以判断正当性的标准，彼此不同即导致命题不同。", "evidence": "P003", "ambiguity": "未区分私人标准与公共标准，也未说明二者能否通约。"},
    {"term": "偷换概念", "meaning": "作者认为不应据此指责他人在立论前给出的定义，并把“立论前定义”比作论文作者的特权。", "evidence": "P015", "ambiguity": "未说明何种情形下才是真正的偷换概念。"},
    {"term": "曹操屠城", "meaning": "提问者与其学生争论的对象；正文只在提问语境中出现，作者未对其作任何评价。", "evidence": "P003", "ambiguity": "该史事本身在正文中未被叙述、未被考证。"}
   ],
   "examples_and_targets": [
    "提问者（老师）与其学生——提问者转述的争论双方，其立场（认为曹操屠城不合理）不属作者。",
    "南方人／北方人对地瓜（不甜／甜、烤着吃、地瓜干、剥不剥皮）——核心类比材料（P004—P007）。",
    "图片 IMG001、IMG002（紧邻“南方地瓜／北方地瓜”两段）——未读图，疑为南北地瓜对比配图，需图像核验。",
    "论文作者与程序员给变量命名——类比例证，用来说明立论前给定义的特权（P015）。",
    "“多活五年”“美白”“补肾”——戏谑性收尾修辞（P017—P019）。"
   ],
   "conditions": [
    "条件：否则不存在讨论的基础（P014，指未先确认是否同一问题）。",
    "限定：不要指着别人在立论前给的定义喊“偷换概念”（P015）。",
    "语境条件：P009—P011 两张图片与省略号插入议论之间，构成“接着吵啊”这一反问的前提，但图片内容不可辨。",
    "依赖前提：双方所用“合理”一词的所指可能不同（P001—P003）。"
   ],
   "rhetoric_and_tone": "以反问与类比代替直接回答：开篇即追问，全篇用南北地瓜的口语化场景调侃争论双方（“这不丧心病狂吗？”“这皮能用剥的吗？”），插入两张图与省略号作节奏停顿后再反问“接着吵啊？”，语气轻松、戏谑、略带嘲弄；对提问者想要“开导”的诉求不作正面裁决，而把矛头指向问题预设；结尾以“多活五年”“美白”“补肾”加“哼”字收束，属玩笑式训诫。",
   "unresolved_questions": [
    "两张图片（IMG001、IMG002）内容未经核验，疑为“南方地瓜／北方地瓜”配图；本记录无读图能力，需后续图像核验后才能确认图文关系。",
    "作者未评价“曹操屠城”是否合理，也未提供提问者所问的开导方法，该问题在正文中悬置。",
    "“他合的是他认定的那个理”中的“他”与“你”各自之理的具体内容，正文未说明。",
    "是否存在可共同接受的“理”或判定标准，正文未回答。",
    "“那会丢老师和爹妈的脸”的指向略有歧义（指喊“偷换概念”的人，还是指提问者本人）。",
    "“美白需要理由吗？”“还可以补肾！”两句属玩笑，是否含实指无法确定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“合理”到底是指什么理？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "是公理？常理？道理？情理？义理？法理？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "他合的是他认定的那个理，你不合的是你认定的这个理。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "此理恐非彼理，所以你们用同样的文字主张的是完全不同的两个命题。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "这就像一个南方人大喊最讨厌吃地瓜，一点都不甜；一个北方人大喊最爱吃地瓜，甜得要喝水。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "两边吵个天翻地覆，而且互相觉得对方不可理喻。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "看明白问题所在了吗？这要能说服对方才叫有鬼了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "所以，论证问题的前提，是要先搞清楚你们在谈论的到底是不是同一个问题、是一个什么问题。否则不存在讨论的基础。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "另外，不要指着别人在立论前给的定义喊“偷换概念”，那是论文作者普遍有的特权，就跟程序员有权给变量自由命名一样。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "那会丢老师和爹妈的脸。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "想通了这个道理，养好了这个习惯，你可以多活五年，还可以美白。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["论证与逻辑", "历史评价", "教育与说服"],
   "issue_candidates": ["“合理”的歧义", "争论前提的澄清", "定义权与偷换概念"],
   "text_function_candidates": ["答问", "方法论说明", "调侃"],
   "object_candidates": ["提问者与其学生", "曹操屠城", "合理/理", "南北地瓜"],
   "working_keywords": ["合理", "理", "偷换概念", "讨论基础", "曹操屠城"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 2 张图片（IMG001、IMG002，位于 P009—P011 之间的“南方地瓜／北方地瓜”处），本记录无读图能力，未能核验图像内容及其与正文的对应关系，故 status=needs_reread、image_checked=false，需后续图像核验。正文文字部分已完整读完（19 段，489 字符）。question 字段的立场（认为曹操屠城不合理、想开导学生）属提问者，作者未对其作评价，本记录不作代填。brief 与正文高度重合，仅作导航。元数据：published 2021-04-16，updated 2023-06-05。"
 },
 "bc382c56": {
  "analysis": {
   "question_context": "提问者（Q001）问：如何正确的审视自己？提问者只提出方法求助，未给出自身立场。作者的回应是否定该问题的前提：先追问“什么叫正确的审视了自己”“如何鉴定”，再用数学不及格的例子说明自我观察不是观察而是型塑，进而主张“正确的自我观察的方法”根本不存在，并给出替代方案（放弃“适合／不适合”决策模型、多给自己机会、把事做到最好），末段转入对读者（“你”）的直接劝勉。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "追问判据：什么叫正确的审视自己、如何鉴定；摆出“数学长期不及格故无数学才能”这一看似合理的推理，随即判定其并不对。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "核心命题：人的存在受观察影响；长期不及格常因自认无才能而不投入资源，形成自我强化的证据循环；这不是观察而是型塑，本质是人用“观察”这种仪式创造了自己。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013"], "summary": "机制描述：人在证据根本不足时被本能趋避反应驱使感染某种自我认知，经“自我观察”发作，留下永久瘢痕，结果在早期即已注定。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "追溯早期来源：子女偶然表现触发身边权威角色的反应；父母把语文理解问题误判为数学能力不足并告知“你数学天赋不好”，孩子为免苦熬而接受。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "后果展开：转向音乐班、时间被转拨、数学被长期放弃，事情就这样成了。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037"], "summary": "参与者皆无辜：父母已尽力、数学老师只能客观评分、孩子连话都说不清；小误会借每个人的“观察”发育成“有充分事实证据的事实”。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P038", "P039", "P040", "P041"], "summary": "机制的不对称性：对失败更敏感，负面体认权重大到极可能击溃正面体认；因此读者目前对自己的体认极大概率比实际向负面偏差。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054"], "summary": "诊断与结论：你并不像所有人包括你自己相信的那样无能；你们的“观察”是无效的；与其说你是那样，不如说你需要自己是那样，因为只有如此你才能勉强忍耐自己的生活。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P055", "P056", "P057", "P058", "P059"], "summary": "对提问动机的判断：来问“正确的观察方法”不过想要一个新处方、再开一个疗程的止疼药；而正确的自我观察的方法根本不存在。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P060", "P061", "P062", "P063", "P064"], "summary": "替代方案：抛弃“先靠自我观察搞清适合做什么再去做”的决策模型（其要害是销售恐惧）；只关心把落到头上的事做到最好的人会积累经验与通用方法，进而获得能做好任何事的信心，这信心带来安宁和幸福。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P065", "P066", "P067", "P068", "P069", "P070", "P071"], "summary": "具体建议：多给自己机会；一两次表现不好不要轻易归因于性格或人格特质；搞不懂多因前置基础不扎实，回到基本阶段打牢；专心去做，妖魔鬼怪自会消散。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098"], "summary": "收束劝勉：不受“适合／不适合”模型限制，命运放什么在我身上我就擅长什么；人类天生就是天才，难的是1+1而非微积分；会说人类语言却认为有知识非己所能，如同运行整个操作系统却说没装计算器；停止自我审视，你一定可以、一定适合。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "首先要追问什么叫“正确的审视了自己”，以及如何鉴定一个人是否正确地审视了自己。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "被作者设定并随后反驳的常识推理：一个人数学长期不及格，据此判定自己没有数学才能，这应该再合理也不过了。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "上述推理其实并不对。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的存在是受观察影响的；观察本身影响事物的存在状态，深刻到用“影响”来形容都不恰当，这不是观察而是型塑；本质上是人用“观察”这种仪式创造了自己。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人数学长期不及格，是因为自认为没有数学才能而从不投入严肃资源，由此面前摆满不行的“证据”，进一步相信自己不行，形成循环。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人是在证据根本不足的情况下被复杂的、隐蔽的、本能的趋避反应驱使而感染某种自我认知，经“自我观察”发作，最终给自我认知留下永久瘢痕；结果在证据极不充分的早期就已注定。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那个证据极不充分的早期，是子女的某些偶然行为或表现触发了身边权威角色的反应，再经由这些反应刺激出来的。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "举例：第一次数学没考好其实是年纪太小、没看懂或误解了题目的语文表达，属语言问题，却被焦虑的父母误以为“数学能力不足”。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母为免除“我很无能”的自我结论的伤害而对孩子说“你数学天赋不好”，孩子本能发现接受该结论即可免于每晚苦熬，于是接受。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "沿着这剧情看下去，每一个参与者都是无辜的：父母已尽力而为，数学老师只能客观评分且无法反复申辩，孩子连话都还说不清楚。", "evidence": ["E15", "E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个小误会是借着每一个参与者的“观察”一步步发育成一个“有充分事实证据的事实”。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该机制是不对称的，对失败更敏感；失败造成的负面体认比起初成功造成的正面体认权重大得多，大到极有可能击溃后者。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "如果读者是第一次见到这段话，那么因为负面权重更大这一问题普遍存在，读者目前对自己的体认有极大的概率比实际情况向负面偏差。", "evidence": ["E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你并不像所有人——包括你自己——所相信的那样无能；你们的“观察”是无效的；你比你“观察”到的更有能力，你的“性格”也根本不是你所“观察”的那样。", "evidence": ["E21", "E22", "E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与其说你是那样，不如说是你需要自己是那样——因为只有坚持相信你自己是那样，你才能勉强忍耐自己的生活；事情客观上是不是那样已经没有关系了。", "evidence": ["E24", "E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "来问“正确的观察方法”，不过是想要拿到一个新处方，好再给自己开一个疗程的止疼药。", "evidence": ["E26"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“正确的自我观察的方法”根本就不存在。", "evidence": ["E27"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这意味着要基本抛弃“靠自我观察搞清楚我适合做xx事情，然后我去做这件事情”的整个决策模型，因为该模型的要害在于销售一种“不找到适合的事努力就没有意义”的恐惧。", "evidence": ["E28", "E29"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有那些事情轮到头上就不考虑适不适合、只关心如何做到最好的人，会不断获得“我果然能把这件事做好”的经验和通用方法，进而获得“其实我能把任何落到我头上的事情做好”的信心；是这个信心让人安宁和幸福。", "evidence": ["E30", "E31"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议：多给自己一些机会；一次两次三次表现不好原因可能非常复杂，不要轻易认定为某种性格原因、品性原因或不可更改的人格特质问题。", "evidence": ["E32", "E33"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代科学与技术整体思路都有紧密的逻辑必然性，人“搞不懂”绝大多数是因为前置基础不扎实、概念一知半解；应回到基本阶段把基础打牢、手艺练精。", "evidence": ["E34"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绝大多数的技艺都和天赋没有什么大关系，是为平均智商和平均能力准备的；学不会、学不好绝大多数不是智商问题，而是被内心暗示与自我诅咒分了心。", "evidence": ["E35", "E36"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何一个人类天生就是天才；难的不是微积分而是1+1，生物用了几亿年才明白1+1，却只用了几千年就明白了微积分。", "evidence": ["E37", "E38", "E39"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做人工智能的人会清楚真正难的是教会ai理解什么是狗、什么是马、什么是太阳；你会说人类的语言，却认为有任何一种人类的普遍知识是你的智力所不能掌握的，犹如运行着整个操作系统的计算机说没装计算器软件就没有计算1+1的天赋。", "evidence": ["E40", "E41"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我会成为何种样人，完全不由我自己的所谓“天赋”、更不由我的“缺陷”决定，而只由命运把什么样的境遇放在我身上决定；放什么在我身上，我就会擅长什么。", "evidence": ["E42", "E43"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：停止这种“自我审视”，它没有意义；你一定可以，你一定适合，你有一切必要的天赋，只是需要给自己足够的机会看到这一点。", "evidence": ["E44", "E45"]}
   ],
   "argument_steps": [
    "追问判据：什么叫正确审视自己、如何鉴定（P001—P002）。",
    "给出一个看似合理的常识推理（数学长期不及格故无数学才能），随即否定它（P003—P005）。",
    "提出核心命题：人的存在受观察影响，观察是型塑而非观察，人用“观察”仪式创造了自己（P006—P010）。",
    "描述自我认知的形成机制：证据不足下的趋避反应、自我观察发作、永久瘢痕、早期注定（P011—P013）。",
    "追溯早期触发源：子女偶然表现引发权威角色反应（P014—P015）。",
    "展开例证：语文理解问题被误判为数学能力不足，父母告知“天赋不好”，孩子为免苦熬而接受（P016—P021）。",
    "展示后果：转向音乐班、数学资源被撤、老师也不再坚持（P022—P028）。",
    "说明参与者皆无辜，误会借每个人的观察发育为“有充分证据的事实”（P029—P037）。",
    "指出机制的不对称性：失败权重更大，故读者的自我体认向负面偏差（P038—P041）。",
    "给出诊断：你并非那样无能，你们的观察无效；与其说你是那样，不如说你需要自己是那样（P042—P054）。",
    "指出提问动机是想要新处方与止疼药，并断言正确的自我观察方法不存在（P055—P059）。",
    "给出替代决策模型与信心来源（P060—P064）。",
    "给出具体建议：多给机会、不轻易归因人格、回到基础、专心去做（P065—P071）。",
    "转入劝勉：不受“适合／不适合”模型限制，命运安排什么就擅长什么，人类天生是天才，难的是1+1；停止自我审视（P072—P098）。"
   ],
   "concept_usage": [
    {"term": "自我观察 / 自我审视", "meaning": "作者主张它并非中立观察，而是会影响被观察者存在状态的“型塑”仪式，并断言“正确的自我观察的方法”根本不存在。", "evidence": "P008", "ambiguity": "作者未给出可操作的替代判据，也未区分内省、他人反馈与客观测评。"},
    {"term": "观察", "meaning": "作者把它视为会改变对象存在状态的行为，深刻到“影响”一词都不恰当。", "evidence": "P006", "ambiguity": "未说明该机制的作用范围与可检验方式。"},
    {"term": "型塑", "meaning": "作者用来替代“观察”的描述：观察在塑造而非记录。", "evidence": "P008", "ambiguity": "文中未定义，属自造术语。"},
    {"term": "自我认知 / 体认", "meaning": "由证据不足的早期反应感染而来、经自我观察发作并留下永久瘢痕的结论；作者称其往往向负面偏差。", "evidence": "P011", "ambiguity": "未给个体判据，也未说明能否修正。"},
    {"term": "天赋", "meaning": "作者主张绝大多数技艺与天赋无关，人人都具备理解微积分乃至任何普遍知识的智力。", "evidence": "P069", "ambiguity": "与作者“天生就是天才”的强断言之间的界限未界定。"},
    {"term": "适合／不适合的模型", "meaning": "作者反对的决策模型：先自我观察确定适合之事再投入努力。", "evidence": "P061", "ambiguity": "未讨论兴趣、资源与现实约束下的取舍。"},
    {"term": "信心", "meaning": "由不断把落到头上的事做好而积累的经验与通用方法所产生，作者称其带来安宁和幸福。", "evidence": "P063", "ambiguity": "未说明失败反复出现时如何维持。"}
   ],
   "examples_and_targets": [
    "数学长期不及格并据以判定自己没有数学才能的人——提问者式困境的设例，也是作者反驳的常识推理（P003—P004）。",
    "焦虑的父母、额外补课、音乐班、音乐老师的夸赞、数学老师的评分——例证链条（P016—P028）。",
    "七岁、语文能力还不够打酱油的孩子——例证（P021）。",
    "福尔摩斯——类比，说明对父母分析能力的过高要求（P033）。",
    "天花后留下的疤痕——类比，描述自我认知的永久瘢痕（P011）。",
    "教会ai理解什么是狗、什么是马、什么是太阳——类比（P087）；蒙娜丽莎——类比（P087）。",
    "8847米与8848米、勃朗峰与乔戈里峰——类比（P091、P093）。",
    "运行着整个操作系统却没有安装计算器软件的计算机——类比（P095）。",
    "水稻之王、养猪仙人——夸张举例（P076—P077）；神的宠儿（P083）。"
   ],
   "conditions": [
    "条件：如果这是你第一次见到上面这段话（P041）→ 你目前对自己的体认极大概率向负面偏差。",
    "条件：只要责任在你头上，仍然还有时间、还有资源，那就继续积极努力下去（P066）。",
    "反事实条件：如果ta们有足够审慎周密的分析能力，也许可以设计更精密的测试技术，找到原因在语文水平上（P032）。",
    "依赖前提：只有坚持相信你自己是那样，你才能勉强忍耐自己的生活（P053）。",
    "年龄与能力条件：你才七岁，语文能力还不够打酱油（P021）；你连话都还说不清楚（P036）。",
    "限定：绝大多数的技艺、绝大多数情况（P069）；“真正难的是……”以人工智能与语言学习为例（P087）。"
   ],
   "rhetoric_and_tone": "第二人称“你”的长篇训导，语气强烈、断言密集并带怜悯与责备交织：频繁自问自答（“明白吗？”“这意味着什么呢？”“为什么？”）推进节奏；用整段例证叙事（数学—音乐班）替代论证；比喻密集（精神性过敏反应、瘢痕、妖魔鬼怪、8847米、操作系统与计算器）；对读者的自我审视作不留情面的判断（“不值一驳”“不过是想要拿到一个新处方”），末段转为格言式排比劝勉（水稻之王、养猪仙人、神的宠儿）。",
   "unresolved_questions": [
    "“人的存在是受观察影响的”这一核心命题未给出机制说明、证据或研究出处。",
    "“失败所造成的负面体认……权重大得多”未给数据或来源，属断言。",
    "“你目前对自己的体认有极大的概率比实际向负面偏差”是对读者的概率性判断，未给出个体层面的判定方法。",
    "“正确的自我观察的方法根本不存在”与后文“多给自己一些机会”“回到基本阶段”等建议之间是否存在张力，正文未处理。",
    "末段“命运安排我进入哪一行，行行我都会是第一流”等表述是字面主张还是修辞夸张，文中未界定。",
    "文中提及人工智能识别狗、马、太阳的难度，未给来源，需外部核查。",
    "原文有疑似录入错字：“所以ya才长期不及格”（P007）与“收于半生不熟”（P068），本记录照原文引用，不作改动。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "什么叫正确的审视了自己？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "如何鉴定一个人是否正确的审视了自己？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "根据自己数学长期不及格，判定自己没有数学才能，这应该再合理也不过了吧？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "其实并不对。", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P006", "quote": "人的存在是受观察影响的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "这不是一种观察，而是一种型塑。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "本质上，是人用“观察”这种仪式，创造了自己。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "很多人数学长期不及格，是因为ta自认为没有数学才能，于是从来不在数学上投入严肃的资源，所以ya才长期不及格。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "人们事实上是在证据根本不足的情况下，被某种复杂的、隐蔽的、本能的趋避反应所驱使，感染了某种自我认知", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "最后的结果实际上在那个证据极其不充分的早期就已经注定了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "是子女的某些偶然的行为、或者表现，触发了ta们身边的某些权威角色的反应，再经由这些反应刺激出来的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "你第一次数学没考好，其实是因为你年纪太小，没有看懂或者误解了题目的语文表达。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "他们为了免除“我很无能”的自我结论的伤害，开始对你说“你数学天赋不好”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "你的本能会发现如果你接受了这个结论，你就不需要再每天晚上苦熬这种精神肉体双重折磨了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P030", "quote": "你沿着这剧情看下去，你会发现每一个参与者都是无辜的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P036", "quote": "你有什么错呢？你连话都还说不清楚。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P037", "quote": "这个小小误会是怎样借着每一个参与者的“观察”一步步的发育成了一个“有充分事实证据的事实”，看清楚了吗？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P038", "quote": "而且，这个机制还有一个可怕的特性——它是不对称的，它对失败更敏感。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P039", "quote": "失败所造成的负面体认要比起初的成功所造成的正面体认权重大得多，大到前者有极大的概率可以击溃后者。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P041", "quote": "你目前对自己的体认有极大的概率是比实际情况向负面偏差的。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P043", "quote": "你并不像所有人——包括你自己——所相信的那样无能。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P045", "quote": "你们的“观察”是无效的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P049", "quote": "你是一个比你“观察”到的更有能力的人，你的“性格”也根本不是你所“观察”的那样。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P052", "quote": "其实与其说你是那样，不如说是你需要自己是那样。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P053", "quote": "因为只有坚持相信你自己是那样，你才能勉强忍耐自己的生活。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P055", "quote": "你到这里来问“正确的观察方法”，其实不过是想要拿到一个新处方，好再给自己开一个疗程的止疼药罢了。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P059", "quote": "根本就不存在。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P061", "quote": "意味着你要基本上抛弃“我要靠自我观察搞清楚我适合做xx事情，然后我去做这件事情”的这整个决策模型。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P062", "quote": "因为这个模型真正的要害，在于销售一种恐惧——一种“我不找到适合我做的事情我的努力就会没有意义”的恐惧。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P063", "quote": "只有那些一件事情轮到自己头上了，根本不去考虑自己适不适合干，而只关心如何把它做到最好的人，会不断地获得“我果然能把这件事做好”的经验", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P064", "quote": "是这个信心让你安宁和幸福。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P065", "quote": "第二，就是多给自己一些机会。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P066", "quote": "一次两次三次表现不好，原因可能是非常复杂的，不要轻易的认定那是某种性格原因、品性原因，某种不可更改的人格特质问题。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P068", "quote": "人之所以“搞不懂”，绝大多数的原因都是前置基础不扎实", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P069", "quote": "绝大多数的技艺都和天赋没有什么大关系，就是为平均智商和平均能力准备的。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P070", "quote": "只管专心去做，一旦做通了，这些妖魔鬼怪自然会消散。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P084", "quote": "任何一个人类，天生就是天才，这是显而易见，理所当然的。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P085", "quote": "难的不是微积分，难的是1+1。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P086", "quote": "生物用了几亿年，才明白了1+1，却只用了几千年就明白了微积分。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P087", "quote": "真正难的是教会ai理解什么是狗，什么是马，什么是太阳。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P095", "quote": "你会说人类的语言，却认为有任何一种人类的普遍知识是你的智力所不能掌握的", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P074", "quote": "我会成为何种样人，完全不由我自己的所谓“天赋”、更不由我的“缺陷”决定，而只由命运把什么样的境遇放在我身上决定。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P075", "quote": "放什么在我身上，我就会擅长什么。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P096", "quote": "停止这种“自我审视”，它没有意义。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P097", "quote": "你一定可以，你一定适合，你有一切必要的天赋，", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["自我认知与心理机制", "教育与天赋观", "成长与信心"],
   "issue_candidates": ["自我审视的可靠性", "观察对存在的塑造", "天赋论与努力", "负面偏差"],
   "text_function_candidates": ["答问", "训导", "劝勉", "心理机制说明"],
   "object_candidates": ["提问者", "自我观察/审视", "数学不及格的设例", "天赋与适合模型"],
   "working_keywords": ["自我审视", "观察", "型塑", "自我认知", "天赋", "信心"]
  },
  "notes": "正文完整读完（98 段，3812 字符），无图片节点；question 仅为方法求助，其预设（存在“正确的审视自己”的方法）在正文中被作者质疑，不得当作作者立场。brief 与正文高度重合，仅作导航。元数据：published 2021-04-17，updated 2022-06-19。原文含疑似录入错字：P007“所以ya才长期不及格”、P068“收于半生不熟”，本记录照原文引用未作改动。全文无具体数据与文献出处，机制的实证支持待外部核查。"
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
