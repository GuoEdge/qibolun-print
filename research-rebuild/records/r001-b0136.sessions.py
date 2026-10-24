# -*- coding: utf-8 -*-
"""批次 r001-b0136 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0136.sessions.py            # 写 out/r001-b0136.out.jsonl
  python3 records/r001-b0136.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0136"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0136.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "1b8ad80d": {
  "analysis": {
   "question_context": "知乎提问（Q001）仅一句“女权主义到底是什么?”，属提问者，无立场预设。作者未复述该问题，而是自设议题：从古代战争与近代总体战的形态差别入手，区分“女权浪潮/女权运动”与“女权主义运动”，并对“女权主义”作否定性判定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以“要从古代说起”开启历史论证。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "先摆出“现代进入和平年代、斗争已缓和”的流行观感，随即判其为根本性误解。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "古代战争受季节、阶层、地域限制，烈度低、动员力有限，成本主要由最弱势少数人承担。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "近代国家高度组织化使一战二战成为总体战，战败耗尽国本，故不能排除占一半人口的女性力量。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "由前提给出女权崛起的历史根源，并否定“思想进步”与“统治者开明”两种解释。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "女权运动是浪潮之上的运动；精英与投机者自认掌握“女权的定义权”属幻觉或姿态；不存在“女权主义运动”。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "以国际竞争为前提说明“主义”只能退守艺术领域，主张女权位格高于男性必不为竞争现实所容。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016"], "summary": "自设反问“是否等于不支持女性主张权利”，回答“并不是”。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018"], "summary": "女权运动两阶段：第一阶段争取法律平等已随宪法承认完成，重心转向充分享有平等法律地位。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "先指很多人误解平权，再给出平权定义：制度不偏向任何一方、机会平等、合法合规所得即公平利益。", "role": "definition"},
    {"unit_id": "U011", "paragraph_refs": ["P023", "P024", "P025"], "summary": "女性可用生育权与性权利争取立法与利益；平权同样支持男性主张权利；两者互为盟友、成果互相转化。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P026"], "summary": "对照指出“女权主义运动”敌视男权运动，甚至不接受“男权运动”概念。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P027", "P028", "P029"], "summary": "总结：“女权主义”是对女权概念的滥用、不该出现的“主义”；以“争取一切，但不苟得”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把“国家间与人间斗争已缓和”当作古今之别，是根本性误解：古代战争低烈度且动员有限，真正的变化是近代总体战。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女权崛起的历史根源是总体战条件下国家必须调动全部人口（含女性），既非女权主义者的思想觉醒，也非统治者的开明。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女权运动是浪潮之上由知识精英与投机者占立潮头的运动；其“女权主义”理论苍白，源于误认自己掌握“女权的定义权”。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不存在也不可能存在“女权主义运动”；一旦升格为主张女权位格高于男性的主义，必不为国际竞争现实所容。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女权运动第一阶段（为女性争取法律上的平等地位）已随宪法承认完成，现阶段重心转向对已成立的平等法律地位的充分享有。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平权的本质是制度不再在群体博弈之间偏向任何一方；凡经合法合规手段争取来的优势与利益都是公平的利益。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女权运动必然同情并支持男权运动，两者互为盟友、成果互相转化；而“女权主义运动”则敌视男权运动。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认“女权运动与女权主义运动不一样”等于“不支持女性过度主张自己的权利”。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“女权主义”的本质是对女权概念的滥用，是一种不该出现的“主义”，女性不需要它来为自身要求背书。", "evidence": ["E16"]},
    {"claim_id": "C010", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "（作者转述并批评的误解）把平权理解为“我得到什么，你就该得到什么”“我不要求什么，你就不该要求什么”。", "evidence": ["E17"]}
   ],
   "argument_steps": [
    "设问式开场：要从“古代”说起（P001）。",
    "先立后破：摆出“两次大战后进入和平年代、斗争缓和”的观感（P002-P003），随即断言这是根本性误解（P004）。",
    "给出古代战争的条件性描述：季节、阶层、地域限制，低烈度、动员力有限、成本由最弱势少数人支付（P005-P007）。",
    "对比近代总体战：国家组织高度效率化，战败即耗尽一代青壮年与国力（P008）。",
    "推出必要性：竞争中排除一半人口的力量不可考虑（P009）。",
    "得出结论：女权崛起源于新社会关系对原始社会关系的历史性胜利（P010）。",
    "给出运动与浪潮的区分，并指“女权主义”理论苍白源于对定义权的误认（P011）。",
    "以“何以见得”自问，用国际竞争说明“主义”不能占据社会运动舞台（P012-P014）。",
    "设置并否证可能的误读：不等于不支持女性主张权利（P015-P016）。",
    "给出女权运动两阶段的任务划分（P017-P018）。",
    "定义平权，并以合法合规为界划定公平利益（P019-P022）。",
    "由平权定义推出女权与男权的盟友关系及其与“女权主义运动”的根本差别（P023-P026）。",
    "总结答题并给出结语式格言（P027-P029）。"
   ],
   "concept_usage": [
    {"term": "女权运动", "meaning": "女性所主张的平权运动，是浪潮之上的运动；分两阶段，必然同情支持男权运动。", "evidence": "P017", "ambiguity": "与“女权主义运动”严格对立使用；作者强调“注意，不是女权主义运动”。"},
    {"term": "女权主义/女权主义运动", "meaning": "主张女权位格高于男性、自认掌握女权定义权的“主义”及其运动；作者判其为对女权概念的滥用。", "evidence": "P014", "ambiguity": "作者用引号包裹以示距离；未给出该词在他人用法中的定义。"},
    {"term": "平权", "meaning": "制度不再在群体博弈之间偏向任何一方，所有人有平等机会用尽力量争取地位与资源。", "evidence": "P020", "ambiguity": "作者明确指出“很多人对平权有误解”（P019），本文含义是作者的界定而非通行定义。"},
    {"term": "总体战", "meaning": "近代国家组织形式高度效率化后，凡参战即地无分南北、人无分长幼的全面动员。", "evidence": "P008", "ambiguity": "未给出学术定义，属作者用法。"},
    {"term": "位格", "meaning": "用于说明“女权主义运动”主张女权在地位上高于男性。", "evidence": "P014", "ambiguity": "术语来源与精确含义未说明。"},
    {"term": "定义权", "meaning": "作者称女权主义者在理论上误认自己掌握的东西，是“幻觉和姿态”的来源。", "evidence": "P011", "ambiguity": "属作者自造表述，需结合上下文理解。"},
    {"term": "男权运动", "meaning": "在合法前提下主张男性权利的行动，被作者视为女权运动的盟友。", "evidence": "P024", "ambiguity": "作者指“女权主义运动”甚至不能想象这一概念（P026）。"}
   ],
   "examples_and_targets": [
    "一战、二战与“总体战”（P008）：作者的历史论据，用于对比古代战争。",
    "古代战争的季节、阶层、地域限制与低烈度、周期性高潮（P005-P007）：作者的历史论据。",
    "“宪法承认”作为女权运动第一阶段完成的标志（P017）：作者的事实性断言，未指明具体条款，待外部核查。",
    "“知识精英和看到了其巨大的政治价值的投机者”（P011）：作者对女权运动领导层的指认，带批评色彩。",
    "冲浪与“我们控制着浪潮的方向”的幻觉（P011）：类比，说明运动与浪潮的关系。",
    "“老虎皮”（P028）：比喻，指女权主义是不必要的背书。",
    "两次世界大战后经冷战进入“和平年代”的流行观感（P002-P003）：被作者反驳的对象。",
    "“平权＝我得到什么你就该得到什么”的流行理解（P019）：被作者指为误解的对象。"
   ],
   "conditions": [
    "整体论证以“现代国家之间竞争如此激烈”为前提（P014）。",
    "结论的适用对象是现代国家与国际竞争语境，非普遍历史断言。",
    "否定“女权主义运动”的条件限定为：一旦升格为主张女权位格高于男性（P014）。",
    "平权的边界条件为“合法合规手段”与“合法程序基础”，并明确不以武力为手段（P022、P023、P028）。",
    "两阶段划分以“宪法承认”已完成第一阶段为前提（P017）。",
    "古代战争的低烈度判断带有“每隔上百年（乃至数百年）会有一个高潮”的限定（P005）。"
   ],
   "rhetoric_and_tone": "论辩与训诫混合的断言体：先用“其实这是一种根本性的误解”直接否定流行观感，再层层推进。行文使用自问自答（“何以见得？”“这并不是。”），对“女权主义”“主义”普遍加引号表示距离与否弃，用“ta们”这一非标准写法指代论敌。结尾转为对女性读者的第二人称直接劝说（“你们所提出的要求”），并以中英夹杂的格言“争取一切，但不苟得。Let the better one win.”收束，带口号式修辞。",
   "unresolved_questions": [
    "“宪法承认”具体指哪一法律或条款、何时完成，正文未说明，待外部核查。",
    "P015“那么，这是否意味着……呢？”的自问句，是作者自设的反问，还是转述读者/对话者的质疑，正文未标明主体，本记录按保守方式处理为作者自问，归属存疑。",
    "“知识精英和看到了其巨大的政治价值的投机者”具体指哪些群体或组织，未说明。",
    "作者断言“不存在、也不可能存在女权主义运动”，其判定标准（除国际竞争外）未展开。",
    "结论“女性也根本不需要这种没有意义的老虎皮”依赖对“背书”作用的理解，正文未说明反事实情形。",
    "updated_at（2025-05-23）明显晚于 published_at（2021-06-19），是否有事后修改或追加无法从记录判断，属版本疑点。",
    "结尾英文“Let the better one win.”与中文“争取一切，但不苟得”的关系未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "其实这是一种根本性的误解。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P008", "quote": "因为国家组织形式的高度效率化，凡参战，就是总体战。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P010", "quote": "这才是女权崛起的历史根源。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "而是出于人类无力抗拒的新社会关系对不能充分调动资源的原始社会关系的历史性胜利。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "“女权主义”之所以在理论上苍白和构建无力，在于ta们错误的认为自己掌握着“女权的定义权”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "根本就不存在、也不可能存在“女权主义运动”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "“女权运动”一旦升格为“女权主义运动”，即主张女权在位格上高于男性，则必不为国际竞争的苛刻现实所容。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "它的使命是为女性争取法律上的平等地位，这一使命已经随着宪法承认历史性的完成了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "女权运动的主要关注议题，是争取对已经成立的平等法律地位的充分享有。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "平权的本质，是指制度将不再在群体博弈之间偏向于任何一方，仅此而已。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "凡经合法合规手段所能争取来的优势和利益，都是公平的利益。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P025", "quote": "女权运动必然同情并支持男权运动，因为大家本来就是抗争不平等的盟友。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "而“女权主义运动”则敌视和反对男权运动。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "并不是。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "那么，这是否意味着“女权运动与女权主义运动不一样，不支持女性过度主张自己的权利”呢？", "relation": "context"},
    {"key": "E16", "paragraph_id": "P028", "quote": "“女权主义”的本质是对女权概念的滥用，是一种不该出现的“主义”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "很多人对平权有误解。", "relation": "context"},
    {"key": "E18", "paragraph_id": "P009", "quote": "在竞争中排除整整占一半人口的女性的力量是不可考虑的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "争取一切，但不苟得。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别与社会理论", "政治哲学", "战争史/国际政治", "社会运动研究"],
   "issue_candidates": ["女权主义的定义", "平权的含义", "女权运动与男权运动的关系", "战争形态与国家动员", "身份政治与定义权"],
   "text_function_candidates": ["答疑（知乎回答）", "论辩", "概念辨析", "批评"],
   "object_candidates": ["女权主义者/女权组织", "知识精英", "投机者", "男性", "现代国家", "一战与二战"],
   "working_keywords": ["女权运动", "女权主义运动", "平权", "位格", "定义权", "总体战", "国际竞争", "男权运动", "浪潮"]
  },
  "notes": "无图片节点（images=0），正文 29 段已完整阅读，图片规则不适用。P015 自问句归属存疑（按作者自问保守处理）。“宪法承认”为待外部核查的事实性断言。updated_at 晚于 published_at 属版本疑点。P029 中英夹杂为原文。"
 },
 "74e10cdb": {
  "analysis": {
   "question_context": "知乎提问（Q001）：怎么样培养创新能力？属提问者。作者直接面向该问题作答，但先要求定义创新，再按“先例与信息可得程度”给出 L0—L5 分级，最后指出培养的起点是认知创新价值与正确的成本收益核算。正文以“（未完，待续）”结束，作者自陈尚待续写。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出谈创新能力须先定义创新。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "给出“创新有一连串等级”的框架及 L0—L2 的定义：复现示范、靠已知成品补全缺失环节、只确认成品可能而自猜路线。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "给出 L3—L5 的定义：以自然为先例、仅有理论计算支撑、连理论支撑也没有的反例探索。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "判定从 L1 起就已经有了创新、已涉及创新的能力（并再次强调）。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013"], "summary": "回答培养创新能力的起点：清楚认知创新的价值、进行正确的成本收益核算。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015"], "summary": "转述“有人说”的通俗算法：把创新成果卖了，减去设计、实验、测试、制造、销售、税等成本看余数，正赚负亏。", "role": "context"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017"], "summary": "以“对不对呢？——对。”认可上述算法。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P018"], "summary": "以“（未完，待续）”标记正文未完成。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谈创新能力必须先定义什么叫创新，而创新不是单一状态，而是一连串等级（文中列 L0—L5）。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按该分级逐级递进，从 L1 开始就已经有了创新，已经涉及创新的能力（L0 仅为跟随示范复现）。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "创新等级可按“是否有先例、先例是人类的还是自然的、是否只有理论支撑”来区分：L3 跟随自然的先例，L4 只有理论计算中的可行对象，L5 连理论支撑也没有。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "培养创新能力的起点是清楚的认知创新的价值、进行正确的成本收益核算。", "evidence": ["E8"]},
    {"claim_id": "C005", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "（转述未具名的“有人说”）所谓成本收益核算，就是把创新成果拿来卖，减去设计、实验、测试、制造、销售、税等成本后看余数，正数即赚、负数即亏。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对上述通俗成本收益核算回答“对”，即认可其方向正确。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "定义先行：要谈创新能力，先定义创新（P001）。",
    "提出存在一连串创新等级（P002）。",
    "逐级给出 L0—L2：跟随示范复现（P003）、凭已知成品补全缺失环节（P004）、只确认成品可能而自猜路线（P005）。",
    "继续给出 L3—L5：以自然为先例（P006-P007）、仅有理论计算支撑（P008）、连理论支撑也没有的反例探索（P009）。",
    "结论：五级逐级递进，L1 起已有创新，已涉及创新能力（P010-P011）。",
    "转到培养问题：起点是认知创新价值与正确的成本收益核算（P012-P013）。",
    "引入并转述“有人说”的通俗算法（P014-P015）。",
    "以自问自答认可该算法（P016-P017）。",
    "以“（未完，待续）”终止（P018）。"
   ],
   "concept_usage": [
    {"term": "创新（分级 L0—L5）", "meaning": "按“别人是否做过、自己知道多少、成品是否存在、先例属人类还是自然、是否有理论支撑”划分的连续等级，逐级递进。", "evidence": "P002", "ambiguity": "L0 与 L1 的界线由作者判定；“从L1开始就已经有了创新”依赖对 L0 的排除。"},
    {"term": "L0（复现）", "meaning": "知道别人做过，跟随示范与讲解重复其做法以复现结果或掌握复现能力。", "evidence": "P003", "ambiguity": "作者未直言 L0 不是创新，仅由 P010 的“从L1开始”间接确定。"},
    {"term": "L1（补全）", "meaning": "拿得到成品、部分知道方法概要，靠自己补全缺失环节以复现结果；此为创新的起点。", "evidence": "P004", "ambiguity": "“部分知道对方的方法概要”未给出量化标准。"},
    {"term": "L2（猜路线）", "meaning": "只确认成品可能，完全不知道原理与工艺路线，尝试猜出自己的一条路线复现同样结果。", "evidence": "P005", "ambiguity": "与 L1 的差别被限定为信息缺失程度。"},
    {"term": "L3（自然先例）", "meaning": "对象非人类创作而存在于自然界（如雷电），即跟随自然的先例而非人类的先例。", "evidence": "P007", "ambiguity": "“自然存在的样本”与“自然先例”的关系未进一步界定。"},
    {"term": "L4（理论先行）", "meaning": "既无人类先例也无自然样本，只存在于理论计算之中，从理性上推测可行并把理论化为现实。", "evidence": "P008", "ambiguity": "未说明理论计算出错时如何归档。"},
    {"term": "L5（无反例支撑）", "meaning": "无人类先例、无自然样本、亦无理论支撑，仅因好奇该反例是否可能存在而探索。", "evidence": "P009", "ambiguity": "作者未给出实例，也未说明如何判断此类探索的价值。"},
    {"term": "成本收益核算", "meaning": "作者给出的培养起点：认知创新价值并对创新活动做正确的成本收益核算。", "evidence": "P013", "ambiguity": "正文未展开“正确”的标准，仅认可了“有人”给出的通俗算法。"}
   ],
   "examples_and_targets": [
    "雷电（P006）：作者例证，用来说明 L3“跟随自然的先例”。",
    "“把创新的东西拿来卖……看余数”（P014）：未具名的“有人说”的通俗成本收益算法，被作者转述并认可。",
    "设计、实验、测试、制造、销售、税（P014）：他人算式中列举的成本项，属被转述材料。"
   ],
   "conditions": [
    "分级以“别人是否做过、自己是否知道、能否拿到成品、是否知道原理与工艺路线”等信息条件为判据（P003-P005）。",
    "“从 L1 开始就已经有了创新”以 L0 不属于创新为隐含前提（P010）。",
    "L3 的条件是成品并非由某个人类创作，而存在于自然界之中（P006）。",
    "L4 的条件是既无人类先例也无自然样本，仅存在于理论计算之中（P008）。",
    "L5 的条件是连理论支撑也没有（P009）。",
    "对成本收益算法的认可仅限该算法本身，作者标注“（未完，待续）”，未给出完整核算方法（P018）。"
   ],
   "rhetoric_and_tone": "教科书式的分层定义体：先声明“首先要定义什么叫创新”，再逐级编号陈述，句式高度平行；对读者统一使用第二人称“你”。行文中使用自问自答（“那么，培养创新的能力的起点是什么呢？”“对不对呢？”“对。”）推进；末段以括号“（未完，待续）”直接交代文本未完成。",
   "unresolved_questions": [
    "正文以“（未完，待续）”结束：成本收益核算的具体做法、以及如何据此培养创新能力均未展开，属作者自陈的未完成状态。",
    "提问者问“怎么样培养创新能力”，本文实际只给出起点，未给出完整培养路径。",
    "L5 无实例，也未说明“好奇反例是否存在”何以构成创新能力。",
    "“部分知道对方的方法概要”（L1）与“完全不知道对方的原理”（L2）之间缺少可操作的分界标准。",
    "“正确的成本收益核算”中“正确”的判据未说明，作者仅以“对。”认可了他人列举的算式。",
    "L0—L5 是否穷尽创新等级、各等级能否跳跃或重叠，正文未说明。",
    "P014 的成本项被作者转述为“……啊、……啊”的口语列举，是否为其完整算法无法确证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "要谈创新的能力，首先要定义什么叫创新。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "创新有一连串的等级。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P010", "quote": "这五级逐级递进，从L1开始，就已经有了创新。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P011", "quote": "注意，再说一遍——L1已经存在创新。在这里，已经涉及到了创新的能力。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "从另一个角度来看，这也意味着你并不是在跟随某个人类的先例，而是在跟随自然的先例。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "它只是存在于理论计算之中，你从理性上推测它是可行的，在尝试将理论化为现实。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "甚至也没有理论本身的支撑，你仅仅是在好奇它作为完全不合乎常识和既有理论的反例", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "是清楚的认知创新的价值、进行正确的成本收益核算。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "有人说这个我会，不就是把创新的东西拿来卖", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "对。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E12", "paragraph_id": "P006", "quote": "而是存在于自然界之中。譬如你看到雷电，意识到雷电是可能的，于是你尝试自己制造雷电。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P004", "quote": "你在尝试靠自己补全那些缺失的环节，以求复现其结果", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["创新与认知方法论", "知识论/技术史", "教育与管理"],
   "issue_candidates": ["创新的定义与分级", "创新能力的培养起点", "成本收益核算", "先例与模仿的关系"],
   "text_function_candidates": ["答疑（知乎回答）", "概念定义", "未完待续的连载式说明"],
   "object_candidates": ["创新者", "自然界", "未具名的“有人说”者"],
   "working_keywords": ["创新", "L0", "L1", "L2", "L3", "L4", "L5", "先例", "复现", "成本收益核算"]
  },
  "notes": "无图片节点（images=0），正文 18 段已完整阅读，图片规则不适用。正文以作者自陈的“（未完，待续）”结束，本记录按已发布全文阅读，未据 brief 或标题补写未出现的后续内容；完整性缺口见 unresolved_questions。P014 的成本收益算法由未具名的“有人说”提出，作者在 P017 以“对。”认可，归属已分开记录。"
 },
 "96a67cba": {
  "analysis": {
   "question_context": "知乎提问（Q001）：如何评价赛雷话金发布视频揭露「不让中国人吃海鲜」事件背后的反华组织利益链？属提问者。作者未直接评价该视频或该利益链事实，而是把问题抽象为“面对可能出于敌意、逻辑不成立、证据不真实的观点，国家/社会最好的处理手段是什么”，主张不把“可能别有用心”当作取消讨论资格或实施惩罚的充分依据；同时明确表示不反对这位博主提供这些信息。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "把提问抽象为“最好的处理手段是什么”，并界定“最好”＝成本最低、收益最高、风险最小。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "给出立场前提：以组织综合收益为标准，发挥对组织规则的影响力，作为价值判断与行动的基本方法。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "建议不要把重心放在“可能别有用心”上：不是不关心，而是别把它当作取消资格、消灭讨论、决定惩罚的充分依据。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "健康社会应在“逻辑不成立、证据不真实”上设防；负担不起“由敌人说出来就不听不试”的政策。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "问题1：敌人可反向操纵“身份立场一票否决论”，挑衅式主张我方抛弃不起的东西，让我方喷成世界公敌；这是阳谋。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "指认很多人此刻正在犯此错误：未帮中国获得更多朋友，可能制造本不该有的敌人，而那可能正是对方目的。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "问题2：会减少可听到的选项——凡可能被认为与敌人有关联者都闭嘴，对方以极小代价削弱我方智力资源与社会稳定支撑要素。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027"], "summary": "后果推演：对方正在开庆功宴，言路被堵、提醒问题的门槛被抬高；若被锁进这条轨道，民族复兴无望。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032", "P033"], "summary": "问题3：延缓甚至阉割公众明辨是非能力的成长；成熟者不因敌友改变事实判断标准，标准只有一个且越严格越好。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039", "P040"], "summary": "机制解释：不过滤者经手案子远多于你；靠十不存一的题量练不出别人全量题量的解题能力。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P041", "P042", "P043"], "summary": "更危险的追问：查不出关联不等于安全；以沉默反复宣扬身份决定论会把“失智症”写入社会心理底层，可能酿成浩劫。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P044", "P045"], "summary": "行动建议：把智力资源投入逻辑严谨与论据真实；话语精英应帮助中国公民成为难以被诱导的成熟公众。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051"], "summary": "澄清与限定：不反对警惕说话人立场、不反对该博主提供信息甚至欣赏其手段；反对的是赋予该信息过于要害的权重。", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057"], "summary": "以美国为对照，重申应把精力集中于话错在哪、论据何处不成立，用理性解决，不给对方反弹琵琶的余地。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P058", "P059"], "summary": "以“正面批评：”起头，其后紧接一句与本论题无关的问句，正文在此断裂，主体与意图不明。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "处理“可能出于敌意、逻辑不成立、证据不真实”的观点，其“最好”的手段应以成本最低、收益最高、风险最小为标准。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若真关心所在组织利益，应以综合收益为出发点、通过发挥对组织规则的影响力来最大化组织繁荣前景，这才是一切价值判断、政策建议与行动决定的基本方法。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议不要把重心放在“可能别有用心”上：并非毫不关心，而是不要把这一点视为取消资格、消灭讨论必要或决定实施惩罚的充分依据。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "健康社会应有充分力量在“逻辑不成立、证据不真实”上设立防线，以避免对“出于敌意的目的”的严重依赖。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我们负担不起“一个命题逻辑成立、证据真实，但由敌人说出来就不要听、不要试”这种政策。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "主张身份立场一票否决会被敌人反向操纵：对方挑衅式主张我方其实抛弃不起的东西，诱使我方攻击，最终使我方成为世界公敌。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人（包括此刻）正在犯这种错误；这样做没有帮中国获得更多朋友，反而可能制造本不该有的敌人，甚至实际上帮了对方。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "以身份预过滤的后果是：可能被视为与敌人有关联的人全都闭嘴，对方仅用几枚闲棋就以极小代价削弱我方大量智力资源与社会稳定支撑要素，这是以战术失败实现的战略性成功。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果中国如此轻易被锁进这条轨道，就不必期待民族复兴，因为民族复兴不可能仅靠“纯血天使”完成。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "身份/立场预过滤政策会在发展上延缓、长远看甚至阉割掉公众明辨是非能力的成长。", "evidence": ["E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成熟的人不应因对方友善而放松事实判断标准，也不应因对方敌对而收紧标准；标准只有一个，即最严格的那一个，一视同仁。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不过滤身份的人经手的案子远多于过滤者，靠十不存一的题量练不出别人全量题量的解题能力。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质疑“查不出任何关联的就一定是安全的”这一被该做法默认的假定。", "evidence": ["E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这种以震耳欲聋的沉默反复宣扬身份决定论的做法，会把一种失智症写入社会心理底层；不加警惕和防范会酿成浩劫。", "evidence": ["E23", "E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应把智力资源投入逻辑严谨与论据真实，为大众提供“为什么这个看法不成立、何以见得论据不真实”的思想资源，并帮助中国公民成为难以被诱导做出错误决策的成熟公众。", "evidence": ["E25", "E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者澄清：不是反对人去警惕说话人的立场，也不是反对这位博主提供这些信息，甚至比较欣赏其只用对方自愿公开的信息、未破坏隐私。", "evidence": ["E27", "E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者反对的是把这一点身份信息赋予过于要害的权重；该信息可作为加倍仔细检查逻辑与论据的必要性依据，但不该成为跳过逻辑检查和论据检查直接宣判的依据。", "evidence": ["E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言美国很明显正在被卷入这种错误：越来越深的意识形态化、唯立场化，任由出身、种族绑架甚至废除理性判断。", "evidence": ["E31", "E32"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应把精力集中于那些话到底哪里说错了、哪些论据不成立，用理性解决，从而不给对方留下反弹琵琶的余地，也不中离间计。", "evidence": ["E33", "E34"]}
   ],
   "argument_steps": [
    "把具体事件抽象为一般问题，并界定“最好”＝成本最低、收益最高、风险最小（P001-P002）。",
    "立立场前提：以组织综合收益为判断与行动的基本方法（P003）。",
    "给出核心建议：不把“可能别有用心”当作取消资格/消灭讨论/实施惩罚的充分依据（P004-P005）。",
    "给出正面理由：健康社会应在逻辑与证据上设防，负担不起“敌人说的就不听不试”的政策（P006-P007）。",
    "列举危害之一：敌人可反向操纵身份否决游戏，诱使我方攻击自由、民主、环保等，属阳谋（P008-P013）。",
    "指认现实：很多人此刻正在犯此错误，效果适得其反（P014-P017）。",
    "列举危害之二：减少可听到的选项，使可能被牵连者闭嘴，对方以极小代价削弱我方智力资源（P018-P022）。",
    "推演后果：对方开庆功宴、言路被堵，若锁进轨道则民族复兴无望（P023-P027）。",
    "列举危害之三：阉割公众明辨是非能力的成长，并给出“标准只有一个且最严格”的原则（P028-P033）。",
    "解释机制：不过滤者题量远多，10% 题量练不出 100% 题量的能力（P034-P040）。",
    "追加更危险的追问：查不出关联不等于安全，沉默的宣扬会把失智症写入社会心理底层（P041-P043）。",
    "给出行动建议：专注逻辑与论据，帮助公民成为成熟公众（P044-P045）。",
    "作澄清与让步：不反对警惕立场、不反对该博主提供信息，只反对赋予该信息过于要害的权重（P046-P051）。",
    "以美国为对照重申立场：用理性解决，不给对方反弹琵琶的余地（P052-P057）。",
    "文本在“正面批评：”后断裂（P058-P059）。"
   ],
   "concept_usage": [
    {"term": "反弹琵琶", "meaning": "对方借我方对身份的抨击反过来做文章的策略；作者主张不给对方留下这种余地。", "evidence": "P056", "ambiguity": "仅作标题与结尾用语出现，正文未给出定义。"},
    {"term": "身份立场一票否决论", "meaning": "作者对“只要说话人身份/立场属于敌人，其观点即被取消讨论资格”这一做法的命名。", "evidence": "P009", "ambiguity": "属作者命名，未说明该词是否为他人自称。"},
    {"term": "阳谋", "meaning": "对方无需隐藏意图即可奏效的操纵策略，会用在缺乏警觉性的组织身上。", "evidence": "P013", "ambiguity": "未给出与阴谋的严格区分。"},
    {"term": "事实判断的标准", "meaning": "判断事实的唯一标准，即最严格的那一个；不因对方友善或敌对而放松或收紧。", "evidence": "P031", "ambiguity": "“最严格”的具体内容未展开。"},
    {"term": "身份判断/立场判断（预过滤）", "meaning": "在逻辑与证据审查之前以说话人身份、立场作筛选的做法，作者认为它会阉割事实判断能力。", "evidence": "P034", "ambiguity": "与必要的“警惕”之间的界线由作者在 P049 划定。"},
    {"term": "纯血天使", "meaning": "毫无可疑关联、无可置疑的人；作者以此讽刺“提醒问题”的门槛被抬到极高。", "evidence": "P024", "ambiguity": "讽喻性用词，非固定术语。"},
    {"term": "智力资源", "meaning": "可用于逻辑审查与证据检验的判断能力与人才，被身份预过滤大量削弱。", "evidence": "P021", "ambiguity": "外延未界定。"},
    {"term": "社会性死亡", "meaning": "只要说话（尤其身处瓜前李下而说逆耳忠言）就可能招致的遭遇。", "evidence": "P023", "ambiguity": "作为被担忧的后果引入，未定义。"}
   ],
   "examples_and_targets": [
    "赛雷话金视频及“反华组织利益链”（提问 Q001）：提问者语境；作者以“这位博主”指代，明确不反对其提供信息并欣赏其只用公开信息（P046-P047），未评价视频内容本身。",
    "“引诱你喷自由，引诱你喷民主，引诱你喷所有西方人、引诱你喷环保”（P011）：作者设想的对方挑衅清单，属举例。",
    "孔子“三人行，必有我师焉”（P029）：作者引用，用来说明师不必是好人、友人。",
    "美国（P052-P053）：作者作为陷入唯立场化错误的反面例证/对照对象。",
    "“Best 10000 dollars ever spend!”（P025）：英文引语（原文如此），用以形容对方的低成本高收益，说话者与出处未注明。",
    "蚊子叮咬（P023）：比喻，形容代价之小。",
    "庆功宴（P023）：带推测语气的修辞性场景。",
    "“查完三代查五代、查完三族查九族”（P037）：夸张修辞，形容身份审查之苛刻。",
    "“照镜子”式的对照（P054）：反问读者为何轮到自己也要咬钩。",
    "“正面批评：”与“世界上最严重的环境问题是什么？”（P058-P059）：正文末尾断裂片段，疑为混入的关联提问文本，非本文论题。"
   ],
   "conditions": [
    "问题对象被限定为“可能出于敌意的目的的、逻辑不成立的、证据不真实的观点”（P001）。",
    "“最好”的判据限定为成本最低、收益最高、风险最小（P002）。",
    "建议以“如果你真的关心所在组织的利益”为前提（P003）。",
    "关键限定：不是说叫人对此毫不关心，而是不作为充分依据（P005）。",
    "三大危害的论证以“如果仅仅因为说话人的身份是敌人、或者与敌人有关”为条件（P019）。",
    "民族复兴受损的推演带“如果中国如此轻易的就被锁进了这条轨道”的前提（P026）。",
    "结论自我限定：不反对警惕立场、不反对该博主提供信息，且所反对者仅限“赋予过于要害的权重”（P046-P049）。",
    "该信息的正当用法被限定为“需要投入更多资源、加倍仔细检查”的依据，而非直接宣判的依据（P049）。",
    "“越严格、越严谨、越可靠，越好”为高标准要求，未给出可量化边界（P032）。"
   ],
   "rhetoric_and_tone": "高强度论辩与训诫语气：连续使用质问句（“谁说查不出任何关联的、就一定是安全的？”“但是轮到自己，为什么就也要迫不及待的咬这个钩呢？”）向读者施压，称呼直指“你”。插入“恕我直言”“我坦率地讲”等断言式插话；使用夸张与讽刺（“对方大概现在正在开庆功宴”“荒腔走板的脑瘫状态”“如同蚊子叮咬”“查完三代查五代、查完三族查九族”）以及一次英文引语。结构上用“1）2）3）”序数组织三大危害，末段以“正面批评：”示意转入新环节但正文随之中断。",
   "unresolved_questions": [
    "P059“世界上最严重的环境问题是什么？”紧接在“正面批评：”之后，属正文末尾断裂，疑为混入的关联提问文本；作者是否计划展开、该句主体为何，均不明，本记录未据此补写作者主张。",
    "Q001 所述赛雷话金视频内容与“反华组织利益链”的事实，正文未复述、未直接核实，属待外部核查；作者仅以“这位博主”指代。",
    "P025 英文引语“Best 10000 dollars ever spend!”（原文如此，含语法不规范处，未改动）的说话者、出处与指向对象均未注明。",
    "作者反复提及的“对方”具体指哪个国家、组织或群体，正文未指名。",
    "“美国很明显正在被卷入这种错误中”为作者的事实性断言，未给证据，属待外部核查。",
    "三方面问题是否穷尽，正文未说明；标题“反弹琵琶”的完整含义未在正文展开。",
    "“智力资源”“社会稳定支撑要素”“失智症”等表述的外延未界定。",
    "作者称“很多人在犯这种错误……此时此刻、现在，就在犯”，所指具体言论或事件未点名。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "一个国家、一个社会，能采取的最好的处理手段是什么？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "所谓最好，当然是指成本最低、收益最高、风险最小。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这才是你对组织内一切问题进行价值判断，政策建议和行动决定的基本方法。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "基于这个立场，我建议人们不要把重心放在“可能别有用心”上。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而是不要把这一点视为“取消资格”/“消灭讨论的必要”/“决定实施惩罚”的充分依据。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "以避免对“出于敌意的目的”的严重依赖。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "因为，我们负担不起“一个命题，其逻辑是成立的，证据是真实的，但很不幸它是由敌人说出来，我们就不要听、不要试”这样一种政策。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "敌人可以反向操纵这个游戏。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "对方就会挑衅式的主张一些你其实抛弃不起的东西，让你喷，你喷完了就会变成世界公敌。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "这是一种会毫不犹豫的用在没有这个警觉性的组织身上的阳谋。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "而恕我直言，很多人在犯这种错误。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "这并没有真的帮助中国获得更多朋友，但却有可能制造了本不该有的敌人", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "这意味着对方用了极小的代价——几个根本不怕被骂的、无足轻重的闲棋", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "这是一种重大的、一本万利的战略性的成功，它只是以一种战术的失败来实现罢了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "如果中国如此轻易的就被锁进了这条轨道，就不必期待什么民族复兴了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P027", "quote": "因为民族复兴不可能仅仅依靠纯血天使来完成。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P028", "quote": "3）它会在发展上延缓、甚至从长远来看会阉割掉公众明辨是非能力的成长。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P030", "quote": "也不应该因为对方是敌对的、就“收紧”实施判断的标准。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "事实判断的标准只有一个，就是最严格的那一个。万言万当，一视同仁。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P035", "quote": "道理极其朴素——不做这过滤的人，经手的案子很自然会比你多。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P040", "quote": "你想靠10%的题量练出人家100%题量的解题能力", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P041", "quote": "更危险的是——谁说查不出任何关联的、就一定是安全的？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P042", "quote": "把这种执着——严格说是一种失智症——写入社会心理的底层。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P043", "quote": "不加警惕和防范，是实实在在会酿成浩劫的。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P044", "quote": "不要把你的智力资源投入到对说话者立场和身份的在意上去", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P045", "quote": "都难以诱导做出错误决策”的成熟的公众。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P046", "quote": "我不是在反对人去警惕说话人的立场，或者反对这位博主提供这些信息。", "relation": "qualifies"},
    {"key": "E28", "paragraph_id": "P047", "quote": "我甚至比较欣赏ta并没有使用破坏ta人隐私的手段", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P048", "quote": "我所反对的，是人们把这一点信息赋予了过于要害的权重。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P049", "quote": "但是不该成为跳过逻辑检查和论据检查直接宣判的依据。", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P052", "quote": "美国很明显正在被卷入这种错误中。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P053", "quote": "使得一个昔日的强国，陷入到荒腔走板的脑瘫状态。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P055", "quote": "把精力集中到那些话到底哪里说错了、哪些论据并不成立上，用理性来解决它。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P056", "quote": "既不给对方留下反弹琵琶的余地，也不中ta们的离间计。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P025", "quote": "“Best 10000 dollars ever spend!”", "relation": "context"},
    {"key": "E36", "paragraph_id": "P059", "quote": "世界上最严重的环境问题是什么？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学/公共理性", "舆论与传播", "国际关系", "社会心理与公共政策"],
   "issue_candidates": ["身份立场与观点资格", "对敌意言论的处理策略", "事实判断标准", "言论空间与自我审查", "认知开放度与判断力训练"],
   "text_function_candidates": ["答疑（知乎回答）", "论辩", "政策批评", "行动建议"],
   "object_candidates": ["赛雷话金（提问所指博主）", "美国", "中国话语精英", "网民", "敌人/对方", "孔子"],
   "working_keywords": ["反弹琵琶", "身份立场一票否决论", "阳谋", "事实判断", "智力资源", "纯血天使", "社会性死亡", "离间计"]
  },
  "notes": "无图片节点（images=0），正文 P001—P058 为作者论述并已完整阅读。P059（“世界上最严重的环境问题是什么？”）紧接“正面批评：”之后，属正文末尾断裂、疑为混入的关联提问文本，未据其补写任何作者主张。提问字段所述赛雷话金视频属提问者语境，作者未评价视频内容，仅声明不反对这位博主提供信息。P025 英文引语照原文保留（含 spend 用法不规范处，未改动）。涉及美国现状、“反华组织利益链”等事实性断言均标为待外部核查。"
 },
 "48215fd7": {
  "analysis": {
   "question_context": "知乎提问（Q001）：如何反驳老一辈人「我们那个年代那么艰苦都活下来了，现在的年轻人条件那么好却经常出现心理问题」的言论？提问者转述了老一辈的说法并寻求“反驳”方法。作者没有提供反驳话术，而是承认其中一部分事实（这一代承压能力确实较弱），同时指出老一辈的基本假设不成立，并把重点转向批评提问者设想的那种冷嘲热讽式应对。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接给出核心判断：生活条件好本来就会造成心理脆弱。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "承认老一辈苦难的真实与强度，同时指出其“富裕换强健心理”“富裕避免痛苦”的基本假设不成立。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009"], "summary": "论证这一代承压能力确实较弱：幸存者偏差不改变结论，幸存本身是强健的证明；那种黑暗恐惧非后来者所能想象。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "提出苦难的来源区分：天给的灾难往往造就人，人给的灾难就算没杀死人也往往毁灭人。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "归结：老一辈的强悍人格是时代造就，条件不在，这一代确实要软弱不少；答案很朴素。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "转向批评应对方式：冷嘲热讽是无效且糟糕的应对，且首先是一种应激造成的误判。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024"], "summary": "逐项核算该应对的收益：免不掉教训、无心理满足、无物质与社会收益、招致目睹者差评，且未降低感叹再发生的概率。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026"], "summary": "行动准则：控制情绪冲动、做理性有效的事，这本身就是成熟。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生活条件好本来就会造成心理脆弱，这没有什么好奇怪的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老一辈经受的苦难是威胁基本生存的，其强度远超 90 后、00 后乃至 80、70 后的想象，这是无可争辩的客观事实。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "老一辈的基本假设——“富裕的生活可以理所当然换到强健的心理承受力”“富裕就可以避免一切痛苦”——一开始就是不成立的。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "客观来说这一代年轻人的普遍承压能力确实显著弱于老一辈；以“幸存者偏差”相诘并不改变这个结论，因为从那个年代幸存本身就是强健的证明。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "苦难只有来自上天（而非另一个人的决定，即便主观上出于教育目的）才具有形塑人格的作用。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "天给的灾难因无可仇恨，若未杀死人往往造就人；人给的灾难因直接引起仇恨，即使没杀死人也往往毁灭人。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老一辈人的强悍人格是时代造就的结果，该“幸运”条件现已不存在，所以这一代确实要软弱不少。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“老人在说谎吹牛、图谋教训你的资格”的姿态去冷嘲热讽，是一种非常无效而且糟糕的应对。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“老人在谋求教训你的资格”是应激造成的不假思索的误判：他们根本不觉得这个资格还需要“谋求”。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种应对在所有方面都是亏损：不免教训、无任何收益、招致目睹者差评，也没有降低老人感叹再发生的概率。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "（提问者转述的老一辈说法，非作者主张）我们那个年代那么艰苦都活下来了，现在的年轻人条件那么好却经常出现心理问题。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何时候都要控制情绪冲动、做理性有效的事，而不是随情绪指挥怎么痛快怎么来，这本身就是成熟。", "evidence": ["E16", "E17"]}
   ],
   "argument_steps": [
    "开篇直接给出核心判断：生活条件好会造成心理脆弱（P001）。",
    "承认老一辈苦难的真实性，同时否证其“富裕换强健”“富裕免痛苦”的基本假设（P002-P003）。",
    "正面承认这一代承压能力较弱，并反驳“幸存者偏差”式辩护（P004）。",
    "以 70/80/90/00 后的理解限度说明那种压力的不可想象（P005-P006）。",
    "指出幸存者受了极深塑造，含极强求生意志，并与长征幸存者类比（P007-P009）。",
    "提出关键区分：苦难以来源分天给与人给，前者造就人、后者毁灭人（P010-P014）。",
    "结论：老一辈的强悍是时代造就，条件不再，这一代确实较弱（P015-P016）。",
    "转折批评提问者设想的应对方式：冷嘲热讽无效且糟糕（P017）。",
    "指出该应对源于应激误判（P018）。",
    "逐项核算损失：收益全无、损失多项、概率未降（P019-P024）。",
    "给出行动准则与“成熟”的定义（P025-P026）。"
   ],
   "concept_usage": [
    {"term": "心理脆弱", "meaning": "由生活条件变好而带来的承压能力不足，作者视其为可预期的结果而非异常。", "evidence": "P001", "ambiguity": "未给出程度或衡量标准。"},
    {"term": "幸存者偏差", "meaning": "作者提到并处理的可能的反驳（老人是幸存者），他承认这一机制存在但认为不改变结论。", "evidence": "P004", "ambiguity": "作者未使用该术语的严格定义，也未展开统计论证。"},
    {"term": "来自上天的苦难／人给的灾难", "meaning": "按苦难来源作的二分：无可仇恨者往往造就人；直接引起仇恨者即使未致人死也往往毁灭人。", "evidence": "P013", "ambiguity": "边界依赖“是否可仇恨”，未给出判定程序。"},
    {"term": "强悍人格", "meaning": "老一辈在死亡、饥饿、恐惧中长期磨出的求生意志与承受力，被作者称为时代造就的结果。", "evidence": "P015", "ambiguity": "作者未区分其中的心理疾病/创伤与能力。"},
    {"term": "成熟", "meaning": "控制情绪冲动、做理性有效的事，而非随情绪图痛快。", "evidence": "P026", "ambiguity": "与“软弱/坚强”的关系未说明。"},
    {"term": "无效的应对", "meaning": "作者对冷嘲热讽式反应的判定：既不免除教训，也不带来任何收益，还提高反感。", "evidence": "P019", "ambiguity": "作者以列举方式界定，未给出替代做法的话术。"}
   ],
   "examples_and_targets": [
    "老一辈转述言论（提问 Q001）：提问者引述并被请求反驳的对象，本记录归在提问者名下（C011）。",
    "纪录片、小说和想象（P005）：作者用以说明后辈理解那种黑暗恐惧的手段不足。",
    "两万五千里长征、九死一生活下来的人（P008）：作者类比，说明极端经历带来的坚强。",
    "40-50-60 后与死亡、饥饿、恐惧“跳了很多年的贴面舞”（P009）：作者的历史叙述与比喻。",
    "得病丢一条腿（P011）与被“教育”砍腿（P012）：作者构造的对照例子，说明天给与人给灾难的差别。",
    "90 后、00 后、80 后、70 后（含 75 前/75 后之分）（P002、P004、P005）：代际划分，作者用来说明苦难经验的分布。",
    "冷嘲热讽、应激反应（P017）：被作者批评的应对方式与对象。"
   ],
   "conditions": [
    "“生活条件好造成心理脆弱”是对趋势性现象的断言，作者未给出适用范围或量化标准（P001）。",
    "对老一辈苦难强度的判断以“威胁人的基本生存”为界定（P002）。",
    "否定的是老一辈的两条基本假设，而非其苦难经历本身（P003）。",
    "“幸存者偏差”被承认为可能的解释机制，但作者认为不改变结论（P004）。",
    "苦难来源二分的关键限定：不能来自另一个人的决定，哪怕主观上出于“教育的目的”（P010）。",
    "代际判断有细分限定：70 后只捎上尾巴，且限于 75 前那一半，75 后懂事时改开已开始（P005）。",
    "对该应对方式的批评以提问者设想的那种“冷嘲热讽/应激反击”为对象，非泛指一切反驳（P017）。"
   ],
   "rhetoric_and_tone": "以断定句开篇（“本来就会”“这没什么好奇怪的”），语气冷静而带训诫。对老一辈使用“ta们”，对其苦难使用“贴面舞”“无可争辩的客观事实”等强表述以示郑重；对提问者设想的应对方式则转为责备与反问（“而你用这么大的损失，真的换到了自己良好的心理感受了吗？”“所以是不是又糟糕、又无效？”），并以“这本身就是成熟”作结，带有教导读者的意味。",
   "unresolved_questions": [
    "作者未给出提问者所要的“反驳”话术；实际回应是“不必反驳、也不必嘲讽”，两者关系是否等同，正文未说明。",
    "“生活条件好本来就会造成心理脆弱”未给出机制解释或证据来源，属作者断言，待外部核查。",
    "“老一辈”“现在这一代”的年龄边界除 75 前/75 后一处细分外未界定。",
    "“苦难只有来自上天的才有形塑人格的作用”是强概括，作者未讨论反例（如人为的、由制度造成的苦难中也有坚韧者）。",
    "作者称老一辈“当然有大量的心理疾病和心灵创伤”，该事实性断言未给依据，待外部核查。",
    "作者批评的“冷嘲热讽”是否为提问者的实际打算，正文未确认，仅针对该姿态发言。",
    "updated_at（2021-09-12）晚于 published_at（2021-06-20），是否存在修改无法确定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "生活条件好，本来就会造成心理脆弱，这没什么好奇怪的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这是一种无可争辩的客观事实。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一开始就是不成立的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "的确现在的这一代年轻人的普遍承压能力是显著的弱于老一辈的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "从那个年代幸存，本身就是不可否认的强健的证明。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "只有来自上天的，才有这个形塑人格的作用，它不能来自另一个人的决定", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "哪怕它主观上是出于“教育的目的”。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P013", "quote": "天给的灾难，因为无可仇恨，如果没有杀死人，往往造就人；", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "人给的灾难，因为直接引起仇恨，就算没有杀死人，也往往毁灭人。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "老一辈人的强悍人格，是一种时代造就的结果。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "其实是一种非常无效、而且糟糕的应对。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "ta们根本不觉得教训你的资格还需要怎么去“谋求”一下。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "说它无效，是因为你既不会因为这个做法免掉教训", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "几乎每一个目睹者都会因此差评你。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P002", "quote": "老一辈所经受过的苦难，是威胁人的基本生存的东西", "relation": "context"},
    {"key": "E16", "paragraph_id": "P025", "quote": "要控制住自己的情绪冲动，做理性有效的事", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "这本身就是成熟。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "所有的方面都是亏损，并且也没有降低它发生的概率。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理", "代际关系", "苦难与人格形成", "沟通与情绪管理"],
   "issue_candidates": ["代际心理承受力差异", "幸存者偏差", "苦难的来源与人格塑造", "如何应对长辈的教训式感叹"],
   "text_function_candidates": ["答疑（知乎回答）", "论辩", "批评纠正", "经验总结"],
   "object_candidates": ["老一辈（40-50-60 后）", "90 后/00 后/80 后/70 后", "提问者", "长征幸存者"],
   "working_keywords": ["心理脆弱", "承压能力", "幸存者偏差", "天给的灾难", "人给的灾难", "应激", "成熟"]
  },
  "notes": "无图片节点（images=0），正文 26 段已完整阅读。提问者转述的老一辈言论按 attribution=questioner 记录（C011、E15），未归给作者；作者对该言论的态度是部分承认（承压能力确实较弱）＋否证其基本假设。作者的事实性断言（苦难强度、老一辈心理疾病状况）标为待外部核查。updated_at 晚于 published_at，属版本疑点。"
 },
 "4b9acfe8": {
  "analysis": {
   "question_context": "知乎提问（Q001）：限制你自由的最主要因素是什么？属提问者。作者以一个自认“特别俗、政治不正确”的角度作答：答案是钱，并给出三条论证（钱可使违法之事成为可能、钱可作为“自由规则选择器”、无法支付成本的法定自由在实践上不存在），进而推论穷国的自由困难首要是贫穷，最后落到人权。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出一个自认政治不正确但现实的角度，给出总命题：钱是自由的最佳载体，并声明有三条。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "第一条：钱可以事实上使法律不允许的事情成为可能；对有钱且懂得使用者，法律限制很大程度上没有实际作用。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "第二条：在货币可跨国兑换且公民可跨国流动时，钱成为“自由规则选择器”，可选国籍身份与对应法律制度。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "第三条（作者标为重点）：一切法律所许可的自由若无法支付成本，在实践上不存在，如无钱则无法享用上网自由。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "推论：穷国自由问题的首要困难是贫穷本身；放宽法律授予的自由实际上专属富人；若穷人被锁死而只增长富人的“理论自由”，国家自由总量反而下降。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014"], "summary": "反向推论：在可流动、可兑换的前提下，即使法律不变，仅让成员变富也创造了更多自由。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "上升到人权：自由是人权最根本的量度，故使成员变富的国家对人权有真实贡献，即使从古典自由主义角度看。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P017"], "summary": "收束：客观上限制一个人自由程度的主要世俗因素的确是钱。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "客观上，限制一个人自由程度的主要世俗因素的确是钱（作者对这个自认“政治不正确”的角度的正面回答）。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自从“通货”概念被普遍确立以来，钱就是自由的最佳载体。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "钱可以在事实上使法律所不允许的事情成为可能：对有充足金钱且懂得如何使用的人，法律限制在很大程度上没有实际限制作用。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果货币可跨国兑换、该国公民也可比较自由地跨国流动，钱就成为“自由规则选择器”，人可借它选择自己喜欢的国籍身份和对应的法律制度。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切法律所许可的自由，如果无法支付其成本，在实践上是不存在的；法律给了自由并不意味着真的拥有它。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "穷国自由问题的首要困难并非法律、体制如何不自由，而是贫穷本身。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "穷国通过放宽法律所授予的自由，绝大多数在实践上只专属于富人，与绝大多数人无关。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果授予的自由导致穷人被锁死在无法实践自由的窘态、只增长富人的“理论自由”，就会造成一国自由总量事实上的下降；作者称这某种意义上就是拉美、非洲大量国家现有困境的本质。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在国民可跨国流动、货币可跨国兑换（即使要经过易货贸易或跨境投资等曲折）的前提下，即使法律法条不变，仅使成员变得更富有也创造了更多自由。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自由就是人权最根本的量度；因此使成员变富的国家对人类人权有真实贡献，即使从纯粹的古典自由主义角度看。", "evidence": ["E15", "E16"]}
   ],
   "argument_steps": [
    "先自嘲式定位：这是个俗且政治不正确的角度（P001）。",
    "给出答案：钱（P002）。",
    "提出总命题：通货确立以来钱就是自由的最佳载体，并预告三条（P003）。",
    "第一条：钱使法律不允许的事在事实上成为可能（P004-P006）。",
    "第二条：货币可兑换＋人员可流动时，钱成为自由规则选择器（P007-P008）。",
    "第三条（重点）：无法支付成本的法定自由在实践上不存在，以上网自由为例（P009-P010）。",
    "推论到国家层面：穷国自由的首要困难是贫穷；放宽法律只让富人受益（P011-P012）。",
    "进一步推论：若穷人被锁死而只增长富人理论自由，则自由总量下降，并以拉美、非洲为例（P013）。",
    "反向推论：仅使成员变富也能创造更多自由（P014）。",
    "上升到人权尺度并给出结论（P015-P017）。"
   ],
   "concept_usage": [
    {"term": "自由", "meaning": "本文主要指实践上可享有的自由，而非仅仅法律许可的自由；无法支付成本的法律自由“在实践上是不存在的”。", "evidence": "P009", "ambiguity": "作者未给出自由的总量度量方法，却使用了“自由总量”的说法（P013）。"},
    {"term": "钱/通货", "meaning": "自由的最佳载体、实质限制自由的主要世俗因素，也可充当“自由规则选择器”。", "evidence": "P003", "ambiguity": "作者区分“懂得如何使用”的条件，未说明其判断标准。"},
    {"term": "自由规则选择器", "meaning": "在货币可跨国兑换且公民可跨国流动的条件下，钱可用来选择国籍身份与对应的法律制度。", "evidence": "P007", "ambiguity": "属作者自造表述；未讨论并非所有国家都允许这种选择。"},
    {"term": "理论自由", "meaning": "法律授予但在实践中无法行使的自由，作者认为这种自由只对不缺自由的人增长。", "evidence": "P013", "ambiguity": "与“实践自由”的界线由是否可支付成本决定。"},
    {"term": "人权", "meaning": "以自由为最根本量度；故增加国民财富即对人权有真实贡献。", "evidence": "P015", "ambiguity": "作者未展开人权的其他维度，只给出这一量度。"},
    {"term": "古典自由主义", "meaning": "作为论证的参照视角：即使按这一视角，使成员变富的国家也真实贡献了人权。", "evidence": "P016", "ambiguity": "作者未界定其所指的古典自由主义具体主张。"}
   ],
   "examples_and_targets": [
    "“政治不正确”的自我定位（P001）：修辞性铺垫，作者自知该角度易受批评。",
    "德国（P008）：举例说明因条条框框多而可以移民到他国的情形。",
    "上网自由与网费、上网设备（P010）：作者例证，说明无法支付成本则自由不存在。",
    "拉美、非洲大量国家的现有困境（P013）：作者的事实性断言与举例，待外部核查。",
    "易货贸易、跨境投资（P014）：作者列举的货币跨国兑换的曲折形式。",
    "“通货”概念被普遍确立（P003）：作者的历史性预设，未给出时间或范围。"
   ],
   "conditions": [
    "第一条以“有充足的金钱、而且懂得如何使用”为限定条件（P005）。",
    "第二条以“货币可以跨国兑换、该国公民也可以比较自由的跨国流动”为条件（P007）。",
    "第三条对一切法律许可的自由成立，判定标准是能否支付其成本（P009）。",
    "自由总量下降的判断带“如果它所授予的自由会导致穷人被锁死……而只增长了……富人的‘理论自由’”的条件（P013）。",
    "反向推论以“国民可以跨国流动、其货币可以跨国兑换（即使要经过一定曲折）”为前提（P014）。",
    "人权贡献的结论限定“即使是从纯粹的古典自由主义的角度来看”也成立（P016）。",
    "作者明确该角度“可以说政治不正确”，属自我限定的立场声明（P001）。"
   ],
   "rhetoric_and_tone": "以自嘲开场（“有一个特别俗的角度，可以说政治不正确”）降低姿态，随后用“客观上……的确是钱”作强硬收束。行文用序数“1）2）3）”组织三条论证，并在第三条前加重语气（“重点在这了——”）。对读者使用第二人称“你”（“你没钱付网费”），对国家层面则用“穷国/一个国家”作主语，带政策评论口吻。整体是断言式的现实主义论述，反问与比喻很少。",
   "unresolved_questions": [
    "“自由总量”如何度量、以何为单位，正文未说明，与其“无法支付成本即不存在”的界定之间存在张力。",
    "“穷国的自由问题的首要困难……是贫穷本身”为作者断言，未给数据或案例细节，待外部核查。",
    "“拉美、非洲大量国家现有的困境的本质”是强概括，正文未举任何具体国家或指标，待外部核查。",
    "“懂得如何使用（金钱）”的判据未说明，使第一条的适用范围含糊。",
    "“通货”概念被普遍确立的时间与范围未说明。",
    "作者称该角度“政治不正确”，但未说明它冒犯的是何种立场，也未处理可能的反驳。",
    "updated_at（2026-04-11）远晚于 published_at（2021-06-21），是否有事后修改无法从记录判断，属版本疑点。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "那就是钱。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P017", "quote": "客观上，限制一个人的自由程度的主要世俗因素，的确是钱。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "自从“通货”这个概念被普遍确立以来，它就是自由的最佳载体。有三条：", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "1）钱可以在事实上使法律所不允许的事情成为可能。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "对于有充足的金钱、而且懂得如何使用的人，其实在很大程度上是没有实际限制作用的。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P007", "quote": "这些钱可以变成一种“自由规则选择器”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "人可以借着它自由的选择自己喜欢的国籍身份和对应的法律制度。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "一切法律所许可的自由，如果你没法支付其成本，在实践上是不存在的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "尽管法律给了你这个自由，并不意味着你真的拥有了它。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "而是贫穷本身。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "绝大多数在实践上只专属于富人，其实与绝大多数人无关。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "它甚至会造成一个国家的自由总量的事实上的下降", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P013", "quote": "这是拉美、非洲大量国家现有的困境的本质。", "relation": "context"},
    {"key": "E14", "paragraph_id": "P014", "quote": "仅仅是使得其成员变得更富有了，那么它也创造了更多的自由。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "自由就是人权最根本的量度。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "即使是从纯粹的古典自由主义的角度来看。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P001", "quote": "有一个特别俗的角度，可以说政治不正确", "relation": "context"},
    {"key": "E18", "paragraph_id": "P008", "quote": "你可以移民去某个没有你在意的限制的国家", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学/自由理论", "发展经济学", "人权论述", "货币与国际流动"],
   "issue_candidates": ["自由的主要限制因素", "法律自由与实践自由的差别", "金钱与自由的关系", "穷国自由困境", "自由作为人权量度"],
   "text_function_candidates": ["答疑（知乎回答）", "论辩", "政策评论", "概念辨析"],
   "object_candidates": ["穷国", "富人/穷人", "拉美与非洲国家", "德国", "古典自由主义者"],
   "working_keywords": ["自由", "钱", "通货", "自由规则选择器", "理论自由", "自由总量", "人权", "古典自由主义"]
  },
  "notes": "无图片节点（images=0），正文 17 段已完整阅读。作者自陈该角度“政治不正确”，属其自我限定；涉及穷国困境、拉美非洲现状的事实性断言均标为待外部核查。updated_at（2026-04-11）远晚于 published_at（2021-06-21），属版本疑点。"
 },
 "c1f11601": {
  "analysis": {
   "question_context": "知乎提问（Q001）：杭州女子跳车调查结果公布，因司机未按导航行驶乘客恐慌跳车，类似情况下，司机和乘客该怎么做才对？属提问者，且已包含提问者对事件经过的陈述（司机未按导航行驶、乘客恐慌跳车）。作者不复述事件、也不直接给乘客/司机的操作清单，而是先界定平台、司机、乘客三方的权利关系，再提出以“是否反社会”为核心的是非判准。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "界定三方关系：乘客信任与接受的是平台选择并委派的服务；只有乘客有权修改路线，司机无权自行修改，要改须先商量并由乘客决定。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "给出条件性判断：若经乘客同意修改路线而乘客跳车，则属乘客自身的思维一致性问题。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "判定未经同意改线且经抗议不更正、反指乘客过激属于反社会行为，并界定“反社会性”不是道德判断而是“法则确立则社会不能有效运转”。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "给出判定方法：把该条款提前公布，看它在竞争中能否生存（如平台宣布可不经同意自由选路是否完蛋）。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "提出“是非尺”与包容极限：是非曲直用“总体看会不会完蛋”来量，社会可以包容的极限是不反社会。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "对比两种处境：不反社会者总可指望找到必要的朋友、同事和同志；反社会者只能隐藏伪装，“寻找同类”是自我暴露与自我戕害。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "总结伦理的两条标准：可操作性与社会性/反社会性，前者是准生证、后者是暂住证，缺一不可。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P015"], "summary": "正文末尾紧接一段追加提问文本（货拉拉跳窗女生、如何应对潜在危险、怎么培养安全感），非作者论述。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "乘客信任的不是司机而是平台；乘客接受的是平台选择的路线和平台委派的驾驶服务。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能修改路线的只有乘客自己，司机没有权利自行修改路线；要改必须先与乘客商量、由乘客决定。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果是“经过乘客同意修改路线，乘客跳车”，那确实属于乘客自己有思维一致性问题。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "未经乘客同意而修改路线、经乘客抗议也不更正、反过来指责乘客“过激反应”“神经过敏”，是一种反社会行为。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“反社会性”不是指道德不道德，而是指“如果这个法则确立，一个社会不能有效运转”。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判断行为是否反社会，有个简单实用的办法：把该条款提前公布出去，看它在竞争中能否生存。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是非曲直要用“总体看会不会完蛋”这把尺子去量；一个社会可以包容的极限是不反社会。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不反社会的人总可以指望找到必要的朋友、同事和同志；若是反社会的，就只能靠隐藏、伪装、自己派遣，“寻找同类”既自我暴露又自我戕害。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对一个伦理，第一看有没有可操作性，第二看有没有社会性/反社会性；前者是准生证、后者是暂住证，缺一不可。", "evidence": ["E13", "E14"]}
   ],
   "argument_steps": [
    "先界定三方关系：乘客信任平台、接受平台选择与委派（P001-P002）。",
    "由关系界定推出改线权限：只有乘客有权改，须商量并由乘客决定（P003）。",
    "区分情形：经同意的改线＋跳车属乘客自身一致性问题（P004）。",
    "对相反情形作否定评价：未经同意改线且不更正、反指乘客过激，是反社会行为（P005）。",
    "定义“反社会性”为非道德判断，而以社会能否有效运转为准（P006）。",
    "给出可操作的判定方法：公布条款、看竞争存活（P007-P008）。",
    "提出尺度并界定包容极限（P009-P010）。",
    "以“能否找到同类与同志”对比反社会与非反社会的处境（P011-P012）。",
    "总结伦理两标准并给出准生证/暂住证比喻（P013-P014）。",
    "文本末尾混入追加提问文本（P015）。"
   ],
   "concept_usage": [
    {"term": "反社会行为/反社会性", "meaning": "不是道德评价，而是“如果这个法则确立，一个社会不能有效运转”；判据是总体看会不会完蛋。", "evidence": "P006", "ambiguity": "作者明确区别于“道德不道德”，但未说明“有效运转”的具体指标。"},
    {"term": "思维一致性问题", "meaning": "用于描述“同意改线后又跳车”的乘客自身前后不一致。", "evidence": "P004", "ambiguity": "术语未定义，作者未展开。"},
    {"term": "平台/司机/乘客的关系", "meaning": "乘客与平台之间存在信任与服务委派关系，路线选择权归乘客，司机只是被委派的驾驶服务提供者。", "evidence": "P002", "ambiguity": "作者未说明该权利归属的依据是平台规则、合同还是法律。"},
    {"term": "准生证/暂住证", "meaning": "比喻伦理的两条标准：可操作性是前提，社会性是持续存在条件。", "evidence": "P014", "ambiguity": "比喻性表述，非严格定义。"},
    {"term": "是非尺", "meaning": "衡量是非曲直的尺度，即“总体看会不会完蛋”。", "evidence": "P009", "ambiguity": "标题用“是非尺”，正文未给出该尺度的量化方式。"}
   ],
   "examples_and_targets": [
    "杭州女子跳车事件（提问 Q001 所述）：提问者提供的事件语境，作者未复述细节、未核实。",
    "假设中的平台条款“我的平台允许自己不经乘客同意自由决定走哪条路”（P008）：作者构造的检验例子。",
    "货拉拉跳窗女生与“怎么培养安全感”（P015）：文末混入的追加提问文本，非作者论述，本记录未据此作答。",
    "“过激反应”“神经过敏”的指责（P005）：被作者判为反社会行为的对象用语。",
    "朋友、同事和同志（P011）：作者用以描述不反社会者的社会支持。"
   ],
   "conditions": [
    "“属乘客自己有思维一致性问题”的判定附条件：必须经过乘客同意才修改路线（P004）。",
    "反社会行为的判定附条件：未经乘客同意而修改路线、经过抗议也不更正、并反过来指责乘客（P005）。",
    "“反社会性”的定义依赖反事实条件——“如果这个法则确立”（P006）。",
    "检验方法依赖该条款可被提前公布、且存在竞争环境（P008）。",
    "包容极限的表述为“一个社会可以包容的极限是不反社会”（P010）。",
    "伦理两标准被限定为缺一不可（P014）。",
    "全部判断限于平台派单乘车的服务关系语境，未声明是否适用于其他关系类型。"
   ],
   "rhetoric_and_tone": "短句、断言的判准式写法，几乎没有铺垫，第一句即下结论（“乘客信任的不是司机，而是平台。”）。用反问设问推进（“如何确定一个行为是不是反社会行为？”），并以“这把尺子”“准生证”“暂住证”等生活化比喻把判准固定下来。语气冷静、规范，带规则说明书的意味，无讽刺或情绪化措辞。",
   "unresolved_questions": [
    "P015（“为什么有网友说货拉拉跳窗女生是被害妄想症？女性在面对潜在危险时应该如何应对？/怎么培养安全感？”）属混入正文末尾的追加提问文本，非作者论述；本记录未据此补写任何主张。",
    "提问者问“司机和乘客该怎么做才对”，作者给出的是是非判准（是否反社会），并未给出司机与乘客的具体行动建议。",
    "“思维一致性问题”未定义，其判断标准不明。",
    "“司机是没有权利自己修改路线的”未说明依据（平台规则、合同法还是法律），待外部核查。",
    "“总体看会不会完蛋”这把尺子如何适用于非竞争性领域（家庭、伦理等），正文未说明。",
    "提问所述事件经过（司机未按导航行驶、乘客恐慌跳车）在正文中未复述，属提问者陈述，待外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "乘客信任的不是司机，而是平台。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "乘客接受的是平台选择的路线和平台委派的驾驶服务。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "能修改路线的，只有乘客自己，司机是没有权利自己修改路线的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "那么这确实属于乘客自己有思维一致性问题。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这是一种反社会行为。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "而是指“如果这个法则确立，一个社会不能有效运转”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "提前把这个条款公布出去，看看在竞争中是否能生存可以了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "你觉得它会不会完蛋？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "是非曲直，要用“总体看会不会完蛋”这个尺子去量。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "一个社会可以包容的极限是不反社会。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "你总可以指望能找到必要的朋友、同事和同志", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "出来“寻找同类”就是一个不但是自我暴露、而且是自我戕害的行为。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "对于一个伦理，第一看有没有可操作性，第二就看有没有社会性/反社会性。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "这两条，前一个是准生证，后一个是暂住证，缺一不可。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P003", "quote": "要改可以，必须要先跟乘客商量，由乘客决定。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/规范判断", "平台经济与出行服务", "社会秩序与规则评价"],
   "issue_candidates": ["网约车路线修改权限", "反社会行为的判定标准", "社会包容的极限", "伦理的可操作性标准"],
   "text_function_candidates": ["答疑（知乎回答）", "判准提出", "规则评论"],
   "object_candidates": ["网约车平台", "司机", "乘客", "货拉拉跳窗女生（提问文本）", "杭州跳车女子（提问文本）"],
   "working_keywords": ["反社会行为", "反社会性", "是非尺", "准生证", "暂住证", "思维一致性问题", "有效运转"]
  },
  "notes": "无图片节点（images=0），作者论述为 P001—P014，已完整阅读。P015 为混入正文末尾的追加提问文本（货拉拉跳窗女生、如何培养安全感），非作者论述，未据此补写主张。提问者对事件经过的陈述（司机未按导航行驶、乘客恐慌跳车）属提问者说法，正文未复述亦未核实；作者主要提供是非判准而非行动建议。"
 },
 "0b30253c": {
  "analysis": {
   "question_context": "知乎提问（Q001）：创业破产的后果有哪些？属提问者。作者先否定提问所预设的那种“一铺清袋”式创业，然后给出以“先失败三次以上”为前提的三条红线（个人不破产、不要赖账、不要害人）与连败三场应取得的收获，最后回答：红线之内创业破产没什么后果，红线之外不叫创业而叫滥赌。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以调侃否定提问所预设的模式：市场一死公司全死、债主上门、破产拍卖甚至跳楼，不叫创业，叫一铺清袋赌大小。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "提出准备条件：想创业的人要先做好失败三次以上的准备，以完美计划的三次失败保证第四次成功。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "第一条红线“个人不破产”：公司可破产清算，人和家庭不行，不拉亲戚朋友下水，三次都不可以借钱、不压房子和父母棺材本。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "回应“太保守”的质疑：在此限制前提下能创多大业就是多大业；“再加一点钱撑一撑”是错觉，问题不是钱多能解决。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "第二条红线“不要赖账”：钱不够付工资、货款、水电费、贷款就结业，不要拿别人的钱续命。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "第三条红线“不要害人”：不搞假冒伪劣、坑蒙拐骗、偷鸡摸狗，不干将来怕人揭发的事；头几个是实验项目，不值得拿终身参赛资格赌博。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "收获之一：拿到一群人对你“死不倒架”的信心，他们是一辈子的资产，也是这几次创业真正的客户。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028"], "summary": "收获之二：把低级错误亲自体验一遍、消除侥幸；必有看错人、定位错、不公正、不谦卑，成功最多懂一半。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P029", "P030", "P031"], "summary": "收获之三：把成本、收益、人是怎么回事搞明白，因为想不到的成本会把算好的利润吃干净。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037"], "summary": "最重要的收获：学会失败、不再恐惧它，把失败变成朋友与合伙人；失败之神站在身边后才可考虑多冒一点风险。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P038", "P039", "P040", "P041"], "summary": "给出“毕业”标准：最大失败是不亏不欠、不偷不抢前提下至少不赔不赚，且未失去创业热情与梦想。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P042", "P043", "P044", "P045"], "summary": "结论：遵循该法则，创业破产没啥大不了的后果；红线之内没啥后果（只是要从“微创业”起步），红线之外叫滥赌，后果来自傲慢、虚荣和贪婪。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“市场一死，整个公司全死，跟着就是债主一窝蜂上门讨债，再接下来就是破产拍卖，甚至是跳楼”这种情况不叫创业，叫一铺清袋赌大小。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想创业的人，要做好先失败三次以上再动手的准备；以完美计划的三次失败去保证第四次获得真正的成功。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第一条红线是个人不破产：公司可以破产清算，人不行、家庭不行，更不能拉亲戚朋友下水；这意味着三次都不可以借钱，不要压房子、不要压爹妈棺材本。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在这个（不借钱、不压房的）限制前提下，你能创多大业那就是多大业；“这太保守”的质疑不成立。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "开头几次创业不要有“只要再加一点钱撑一撑就好了”的错觉，因为这几次创业里的问题根本不是钱多就可以解决的。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二条红线是不要赖账：算起来剩下的钱不够付工资、货款、水电费、还贷款了就结业，不要盘算着拿别人的钱续命。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第三条红线是不要害人：生意不好也不搞假冒伪劣、坑蒙拐骗、偷鸡摸狗；不管认不认同法律，都不要干将来怕人揭发的事。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "头几个项目是实验项目，不值得拿终身参赛资格去赌博。", "evidence": ["E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "连败三场要拿到的第一样东西是一群人对你“死不倒架”的信心，这些人是一辈子的资产，也是这几次创业真正的客户。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要把低级错误都亲自体验一遍、消除低级的侥幸；不要有任何侥幸，你一定会看错人、做错定位、不公正、不谦卑。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些东西一定要有过失败才会真的懂：成功了不算，成功最多懂一半。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要把成本、收益、人是怎么回事搞个明白，因为各种想不到的成本会把本来算好的利润吃干净。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最重要的是学会摔倒、学会挨打，学会失败并不再恐惧它，把失败争取到自己这边来，成为朋友和合伙人。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "等失败之神站在你身边了，才可以考虑稍微多冒一点风险；届时往往不需要赌咒发誓，自然会有钱愿意跟你一起冒险。", "evidence": ["E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "达到这一步的标准是：最大的失败只是“结业时一算，能在不亏不欠、不偷不抢的前提下稳定保证至少不赔不赚”，且没有失去创业热情和梦想。", "evidence": ["E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "遵循这个法则，创业破产没啥大不了的后果：红线之内创业没啥后果，只不过很多人得先从“微创业”起步。", "evidence": ["E27", "E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "红线之外不叫创业，叫滥赌；有后果也不是创业造成的，而是伪装成“创业”的傲慢、虚荣和贪婪造成的。", "evidence": ["E29", "E30"]}
   ],
   "argument_steps": [
    "先否定提问预设的那种创业模式，判其为赌博（P001-P003）。",
    "提出准备条件：先失败三次以上，以三次失败保证第四次成功（P004-P005）。",
    "给出第一原则“个人不破产”及其推论：不借钱、不压房子、不动父母棺材本（P006-P009）。",
    "预设并回应“太保守”的质疑，指出限制之下能创多大业就是多大业（P010-P012）。",
    "给出第二原则“不要赖账”与结业条件（P013-P015）。",
    "给出第三原则“不要害人”并说明实验项目不值得赌上终身资格（P016-P019）。",
    "列出连败三场应得的四项收获：团队信心、亲自犯错、搞懂成本收益与人、学会失败（P020-P033）。",
    "以胜利之神/失败之神的拟人对照说明与失败为友的收益（P034-P037）。",
    "给出“毕业”标准与守则的效果（P038-P041）。",
    "结论：红线之内创业破产没什么后果，红线之外叫滥赌（P042-P045）。"
   ],
   "concept_usage": [
    {"term": "创业红线", "meaning": "三条不可越过的原则：个人不破产、不要赖账、不要害人；越线者不算创业。", "evidence": "P007", "ambiguity": "红线之外的具体补救办法未说明。"},
    {"term": "一铺清袋赌大小", "meaning": "粤语色彩的说法，指把全部身家一次押上的赌博式创业。", "evidence": "P001", "ambiguity": "口语化表述，未给出判定标准（如负债比例）。"},
    {"term": "先失败三次", "meaning": "动手前就要准备的、计划内允许发生的三次失败（实验项目）。", "evidence": "P005", "ambiguity": "“三次”是经验数字还是硬性要求，正文未说明；也未说明如何保证失败可控。"},
    {"term": "个人不破产", "meaning": "公司可以破产清算，但个人与家庭不能被拖入破产，不拉亲戚朋友下水。", "evidence": "P008", "ambiguity": "家庭财产与公司财产的界线未具体界定。"},
    {"term": "死不倒架", "meaning": "团队成员对你保持的信心与其所看重的品格，被作者称为一辈子的资产。", "evidence": "P021", "ambiguity": "口语化表述，未说明如何挑选与验证。"},
    {"term": "毕业", "meaning": "达到最大失败仅是不赔不赚、且未失去创业热情与梦想的状态。", "evidence": "P039", "ambiguity": "毕业后的行为准则是否变化未说明。"},
    {"term": "失败之神", "meaning": "拟人化的失败，被作者要求争取为朋友与合伙人；它站在身边才可多冒风险。", "evidence": "P035", "ambiguity": "修辞性概念的判断标准未说明。"}
   ],
   "examples_and_targets": [
    "“市场一死，整个公司全死……甚至是跳楼”（P001）：被作者否定并重新命名的对象（提问所预设的模式）。",
    "工地搬砖（P002-P003）：自嘲式调侃，形容赌输赌赢的同一结局。",
    "“亲，这边建议直接快进到工地搬砖呢”（P003）：网店客服式调侃修辞。",
    "压房子、压爹妈棺材本（P009）：具体禁止行为举例。",
    "“这太保守了吧？这什么时候才能创业啊？”（P010）：作者预设并回应的质疑。",
    "假冒伪劣、坑蒙拐骗、偷鸡摸狗（P017）：被禁止的行为举例。",
    "胜利之神与失败之神的拟人对照（P034-P035）：比喻性修辞。",
    "“微创业”“印不了大名片、吹不了牛”（P043）：对红线内创业起点的描述。"
   ],
   "conditions": [
    "全部建议以“先失败三次以上再动手”的准备期设定为前提（P004-P005）。",
    "三条红线的适用被限定为“这三次计划失败里面”（P006）。",
    "“个人不破产”的硬性条件：这三次都不可以借钱，不要压房子、不要压爹妈棺材本（P009）。",
    "“在这个限制前提下，你能创多大业，那就是多大业”——规模以不借钱、不押家庭财产为上限（P011）。",
    "“不要赖账”的触发条件是剩余资金不足以支付工资、货款、水电费、贷款（P014）。",
    "“不要害人”的判定包含法律之外的自我约束：“不管你认不认同法律，不要干些将来怕人揭发的事”（P018）。",
    "“稍微多冒一点风险”以失败之神站在身边（即已学会失败）为前提（P036）。",
    "结论的适用边界明确区分为“这根红线之内”与“这根红线之外”（P043-P044）。"
   ],
   "rhetoric_and_tone": "调侃与训诫并行的第二人称劝导体：开篇用“一铺清袋赌大小”“工地搬砖”“亲，这边建议直接快进到工地搬砖呢”（网店客服式调侃）消解悲情，随后转为密集的命令句（“不要压房子”“不要盘算着拿别人的钱续命”“不要干些将来怕人揭发的事”）。中段用“你要拿到的是什么？”自问自答列四项收获，并以“胜利之神/失败之神”拟人化作修辞对比；结尾以“信不信由你”式的强硬与“有后果都不是创业造成的，是伪装成‘创业’的傲慢、虚荣和贪婪造成的”作论断收束。",
   "unresolved_questions": [
    "“先失败三次以上”中的“三次”是经验数字还是硬性要求，正文未说明依据。",
    "P005“完美的计划三次失败，去保证第四次获得真正的成功”未说明如何保证失败只发生三次、且不越红线。",
    "“微创业”的具体规模、形式与门槛未定义。",
    "若已借款、已拉亲友或已押房产（即已越线）应如何处理，正文未说明。",
    "“毕业”之后是否仍适用同一红线，正文未说明。",
    "P021“只花这么多钱就买到这份信心”中的“这么多钱”未给出量化范围。",
    "三条红线是否穷尽（作者未说明是否还有第四条），正文未说明。",
    "updated_at（2021-06-23）晚于 published_at（2021-06-22），是否存在修改无法确定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这不叫创业，这叫一铺清袋赌大小。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "想创业的人，要做好先失败三次以上再动手的准备。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "完美的计划三次失败，去保证第四次获得真正的成功。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "第一，个人不破产。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "公司可以破产清算，人不行，家庭不行，更不必谈拉亲戚朋友下水了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "这意味着这三次都不可以借钱。不要压房子、不要压爹妈棺材本。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "在这个限制前提下，你能创多大业，那就是多大业。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "这太保守了吧？这什么时候才能创业啊？", "relation": "context"},
    {"key": "E9", "paragraph_id": "P012", "quote": "你不要有“只要再加一点钱撑一撑就好了”的错觉", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "第二，不要赖账。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "算起来剩下的钱不够付工资了、付货款、付水电费、还贷款了，就结业。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "第三，不要害人。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "不管你认不认同法律，不要干些将来怕人揭发的事。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "头几个是实验项目，不值得拿终身参赛资格赌博。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "你要拿到一群人对你“死不倒架”的信心。这些人在将来是你一辈子的资产。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "不如说你这几次真正的客户是这帮人。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P024", "quote": "你要把低级错误都亲自体验一遍。消除一些低级的侥幸。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "你不要有任何侥幸——你一定会看错人、一定会做错定位、一定会不公正、一定会不谦卑。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P027", "quote": "成功了不算，成功最多懂一半——必须要失败过才有可能真懂。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "你要把成本是怎么回事、收益是怎么回事，人是怎么回事，搞个明白。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P030", "quote": "各种你打死也想不到的成本会冒出来，把你本来算好的利润吃个干净。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P032", "quote": "你要学会失败，学会不再恐惧它", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P033", "quote": "你要把失败争取到你这边来、成为你的朋友，你的合伙人。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P035", "quote": "失败之神站在旁边帮你拎包，你才真的是无往而不胜。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P036", "quote": "等失败之神站在你身边了，你才可以考虑稍微多冒一点风险了。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P039", "quote": "能在不亏不欠、不偷不抢的前提下稳定的保证至少不赔不赚", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P042", "quote": "遵循这个法则，创业破产没啥大不了的后果。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P043", "quote": "这根红线之内，创业没啥后果", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P044", "quote": "这根红线之外，不叫创业，叫滥赌。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P045", "quote": "是伪装成“创业”的傲慢、虚荣和贪婪造成的。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P012", "quote": "因为这几次创业里你会有的问题，根本不是钱多就可以解决的。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P015", "quote": "不要盘算着拿别人的钱续命。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P017", "quote": "不要看生意不好了搞假冒伪劣，坑蒙拐骗，甚至搞些偷鸡摸狗的事。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["创业与风险管理", "商业伦理", "个人理财与债务", "失败学习/经验总结"],
   "issue_candidates": ["创业破产的后果", "创业前的失败准备", "不借钱与个人破产隔离", "不赖账与及时结业", "不害人的底线"],
   "text_function_candidates": ["答疑（知乎回答）", "经验总结", "行动守则", "训诫式劝导"],
   "object_candidates": ["创业者", "团队成员", "债主", "亲戚朋友", "失败之神/胜利之神（拟人）"],
   "working_keywords": ["创业红线", "一铺清袋", "个人不破产", "不要赖账", "不要害人", "死不倒架", "微创业", "滥赌", "先失败三次"]
  },
  "notes": "无图片节点（images=0），正文 45 段已完整阅读。开头的“市场一死……跳楼”是作者引述并否定的创业模式（与提问语境相关），作者对它的判定为“不叫创业，叫一铺清袋赌大小”。文中“三次”“这么多钱”等表述未量化，已登记为未决问题。updated_at 晚于 published_at，属版本疑点。"
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
