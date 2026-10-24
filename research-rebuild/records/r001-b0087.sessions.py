# -*- coding: utf-8 -*-
"""批次 r001-b0087 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0087.sessions.py            # 写 out/r001-b0087.out.jsonl
  python3 records/r001-b0087.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0087"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0087.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f4b99aaa": {
  "analysis": {
   "question_context": "提问者问如何真正做到「君子和而不同」「求同存异」（Q001，属提问者）。作者未评述该提法本身，而是把“求同存异”定义为关于双方下一步共同计划的谈判中要贯彻的三条原则，再由三要素（世界观/价值观/人生观）、三阶段操作流程、常见错误、协商技巧，推进到“先在的共识文本”这一隐藏要害，末段把该原则引申为群体判据与生存策略。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "给出求同存异的三条原则：行动须基于三方面共识（求同）；行动须避免任一方因三方面分歧受损（存异）；各方对三方面的认识不受他方管辖和审判。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "设问三要素从何而来，答曰即世界观、价值观与人生观的化名，并逐一对应。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011"], "summary": "称三条对国家这类实体仍成立，只是要素凝聚需要复杂过程与机制、原理无不同；三要素决定任何意志体的未来行为，共同行动协议必从三要素开始。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "给出操作框架：第一阶段“各自阐述”，并列出四项技术（事实研究方法论、相关性判断、跨文化有效表达、理解偏差判断）。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020"], "summary": "第二阶段“形成共识”：形成各方都同意的正式共识文本，并点出常见错误所在。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "错误a（误以为共识只应包含大家都同意的部分）：作者反驳称记录“张三主张xxxx、李四主张yyyy”本身也是共识的一部分。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "错误b（未意识到共识须以所有人都同意的表述记录）：凝聚共识即形成一致文本，时间应投资于“形成所有人都同意可以这样写的文本”；并称会议需主要工作语言，否则多语版本协商成本可能过大。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "错误c（判断ta人）：此阶段唯一事务是记录，不应品头论足；掺杂价值判断是渎职和欺诈，并以讥讽语气斥其不体面。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P037", "P038", "P039", "P040"], "summary": "第三阶段“协商行动计划方案”：方案须回应两质疑（如何匹配一致部分、如何尊重异议部分），且回应是否妥善实行一票否决。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046"], "summary": "列三条协商技巧：异议可从共同行动收益中获得补偿；收益不足可排除异议者；既不能补偿又不能排除就应放弃投入。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051"], "summary": "指出隐藏要害：各方常已通过准入机制存在先在的共识文本（企业章程、政党、同盟条约），它往往才是真正的主要部分，现场共识只是“累进更新”，故此类讨论常高效有结果。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P052", "P053", "P054", "P055"], "summary": "引申：这是“人以群分”的底层机制；可把能否在求同存异下达成有净收益的妥协当作同群的绝对有效判据，并称抓住善用此机制者、排除做不到者是明智生存策略。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“求同存异”定义为关于双方下一步共同计划的谈判中贯彻三条原则：行动基于事实认定、原则逻辑、行动目标的共识；行动避免任一方因三方面分歧受损；各方对三方面的认识不受他方管辖和审判。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这三要素即世界观、价值观和人生观的化名，事实认定对应世界观、原则逻辑对应价值观、行动目标对应人生观。", "evidence": ["E004", "E005"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称若把三条放诸国家这类实体仍然成立，但三要素的凝聚要有一个复杂的过程和机制，原理上并无不同。", "evidence": ["E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称三要素决定任何一个意志体的未来行为，任何关于共同行动的协议一定也从这三要素开始。", "evidence": ["E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者反驳“共识应只包含大家都同意的部分”：各方持何主张本身也是共识的一部分，在共识文本中写下“张三认为/提出/主张yyyy”没有问题。", "evidence": ["E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称凝聚共识的过程就是形成一致文本的过程，世界上不存在文本不一致的共识，应把时间投资到“形成一个所有人都同意可以这样写的文本”上。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称共识阶段最重要的唯一事务是记录，不应包含对ta人认知、原则和追求的品头论足，参与者掺杂价值判断是渎职和欺诈行为。", "evidence": ["E013", "E014"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求所有方案都必须回应两质疑——如何匹配共识文本中的一致部分、如何尊重其中的异议部分，且对“是否妥善回应”实行一票否决。", "evidence": ["E015", "E016"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出三条协商技巧：异议可从共同行动收益中补偿；收益不足以补偿时可将异议者排除以减小达成一致的难度；既不能补偿又不能排除就应放弃继续投入。", "evidence": ["E017", "E018", "E019"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出隐藏要害：各方常因准入机制而预先存在先在的共识文本（如雇佣合同带来企业章程），这些先在条件往往才是真正的主要部分，现场新声明的共识只是它的“累进更新”。", "evidence": ["E020", "E021", "E022"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是“人以群分”的底层机制，并称可把“能与之在求同存异原则下达成有净收益的妥协”看作“我们是同一群体”的绝对有效判据；称抓住善用此机制的人、排除做不到的人是明智生存策略。", "evidence": ["E023", "E024", "E025"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称会议一定要有一个主要工作语言，因为共同表述若要在三四种语言版本上全部达成各方一致，其工作量（协商成本）可能过于巨大。", "evidence": ["E026"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称若不放弃无法补偿又不能排除异议者的方案，就是放弃了求同存异的原则。", "evidence": ["E027"]}
   ],
   "argument_steps": [
    "先给定义：把求同存异拆成求同、存异、互不审判三条原则（P001—P004）。",
    "自设提问“为什么是这三个要素”，作答为世界观、价值观、人生观的化名（P005—P009）。",
    "限定与推广：放诸国家等实体仍成立，只是要素凝聚需要复杂过程机制（P010—P011）。",
    "给操作框架：各自阐述（含四项技术）→形成共识→协商行动计划方案（P012—P040）。",
    "在“形成共识”阶段列举并反驳三种常见错误：只写同意部分、不重视一致文本、判断ta人（P021—P036）。",
    "在“协商方案”阶段给两条质问与一票否决，再给三条处理异议的技巧（P038—P046）。",
    "让步/补充：承认各方常有先在的共识文本，现场共识只是累进更新，故讨论常高效（P047—P051）。",
    "结论式引申：该机制即“人以群分”的底层机制，可用作同群判据与生存策略（P052—P055）。"
   ],
   "concept_usage": [
    {"term": "求同存异", "meaning": "关于双方下一步共同计划的谈判中贯彻三原则的做法，而非泛泛的宽容态度", "evidence": "P001", "ambiguity": "作者未说明该定义是否也适用于非“共同计划”性质的争论"},
    {"term": "存异", "meaning": "行动都必须避免导致任何一方因为对事实认定、原则逻辑、行动目标的不同认识而受损", "evidence": "P003", "ambiguity": "与“不受他方管辖和审判”一条在操作上如何衔接，本文未展开"},
    {"term": "事实认定 / 原则逻辑 / 行动目标", "meaning": "作者所称的三要素，分别是世界观、价值观、人生观的化名", "evidence": "P006", "ambiguity": "三者的边界与重叠处本文未说明"},
    {"term": "意志体", "meaning": "其未来行为被三要素决定的实体，作者举国家为例", "evidence": "P011", "ambiguity": "“意志体”的判定标准与范围本文未定义"},
    {"term": "共识文本", "meaning": "所有各方都同意的正式文本，包含一切必要的注释，并记录各方不同主张", "evidence": "P019", "ambiguity": "注释的效力与边界本文未说明"},
    {"term": "异议", "meaning": "被记录进共识文本的分歧，可由共同行动收益补偿或在无法补偿时被排除", "evidence": "P042", "ambiguity": "异议者的判定门槛未说明"},
    {"term": "先在的共识文本", "meaning": "各方通过某种准入机制预先已共同承认的文本，如企业章程，可被讨论直接引用", "evidence": "P047", "ambiguity": "与现场新声明共识冲突时何者优先，本文未说明"},
    {"term": "累进更新", "meaning": "现场新声明的共识相对先在共识文本的地位", "evidence": "P050", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "国家这类实体作为三原则适用对象的例子（作者推广，P010）",
    "会议主要工作语言与三四种语言版本的成本问题（作者举例，P031）",
    "“在本次会议上张三主张xxxx、李四主张yyyy”作为共识记录内容的示例（作者举例，P023—P024）",
    "同一企业成员通过雇佣合同共同承认企业章程、政党成员、同盟条约盟国（作者举例，P048—P049）",
    "“人以群分”作为该机制的解释对象（作者引用俗语，P052）"
   ],
   "conditions": [
    "“如果你放诸于国家这样的实体，这三条仍然成立”（P010，条件句，并附“不过……原理上并无不同”的限定）",
    "方案是否妥善回应两质疑“实行一票否决制”，且“讨论的任何一方认为没有回应，就是没有妥善回应”（P040）",
    "协商技巧2只在“共同行动的收益不足以补偿异议者的损失”时适用（P043）",
    "“如果既不能做到……又不能将异议方加以排除”，才应放弃投入（P045）；“如果此时不作放弃”即放弃原则（P046）",
    "“可能过于巨大”用于多语版本协商成本，语气为可能而非必然（P031）",
    "全文以“双方”“各方”“意志体”为讨论对象，未限定具体行业或议题规模"
   ],
   "rhetoric_and_tone": "操作手册式的条列结构（1）2）3）、a）b）c）），配合第二人称训诫与规范语气；多处自设问句（“为什么是这三个要素？”“这里存在几个关键的要害”）；对“判断ta人”的斥责使用讽刺与粗俗比喻（“请回家先把奶吃足”“丢爹妈脸到让人觉得ta们没有尽到基本教养责任”）；通篇使用性别中立的“ta”。",
   "unresolved_questions": [
    "“意志体”的范围与判定标准本文未定义（P011）；国家实体三要素“凝聚”的复杂过程和机制，本文亦未说明（P010）。",
    "第三原则“不受任何其他一方的管辖和审判”在出现违反时的后果或救济手段，本文未说明。",
    "先在本共识文本与现场新声明共识发生冲突时的优先级，本文未说明。",
    "lexical 节点统计为 60 个 paragraph 节点，而可读正文分段为 55 段，差异疑似来自空段落节点；本文未见明显缺失文本（build 不报 divergence）。",
    "元数据含 updated_at（2021-05-16）晚于 published_at（2020-12-31），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "所谓求同存异，意思就是关于双方下一步共同计划的谈判中贯彻三个原则：", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "所有的行动必须基于双方关于事实认定、原则逻辑、行动目标的共识——此即求同。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "所有的行动都必须避免导致任何一方因为上述三个方面的不同认识而受损——此即存异。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "其实这三个要素就是世界观、价值观和人生观的化名。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "事实认定，就是世界观。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P010", "quote": "如果你放诸于国家这样的实体，这三条仍然成立，不过这三个要素的凝聚就要有一个复杂的过程和机制，但是原理上并无不同。", "relation": "qualifies"},
    {"key": "E007", "paragraph_id": "P011", "quote": "这三个要素决定了任何一个意志体的未来行为，自然任何关于共同行动的协议一定也是从这三个要素开始。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P023", "quote": "因为“在本次会议上张三主张xxxx、李四主张yyyy”这件事情本身也是共识的一部分。", "relation": "contradicts"},
    {"key": "E009", "paragraph_id": "P024", "quote": "在这一阶段的共识文本中写下“关于xxx问题，张三认为 / 提出 / 主张 yyyy”是没有任何问题的。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P026", "quote": "凝聚共识的过程，就是形成一致文本的过程。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P027", "quote": "世界上不存在文本不一致的共识，这在时间上根本行不通。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P028", "quote": "把所有的时间都投资到“形成一个所有人都同意可以这样写的文本”上。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P033", "quote": "在这个阶段里，最重要的唯一事务是记录。不应该包含任何对ta人的认知、原则和追求的品头论足。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P035", "quote": "任何参与者在这个过程里掺杂任何价值判断都是渎职和欺诈行为。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P038", "quote": "所有的方案都必须负责回应两种质疑——它如何匹配了共识文本中的一致部分？它如何尊重了共识文本中的异议部分？", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P040", "quote": "这一判断是实行一票否决制的——也就是讨论的任何一方认为没有回应，就是没有妥善回应，也就意味着该计划不能被视为有效。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P042", "quote": "异议可以从共同行动的收益中得到补偿。商定补偿的标准，额度和方式即可。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P043", "quote": "如果共同行动的收益不足以补偿异议者的损失，则可以将该异议者排除在外，减小达成一致的难度。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P045", "quote": "就应该干脆的放弃继续投入资源探索这种可能性。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P047", "quote": "就是一开始加入这个讨论的所有各方常常预先已经通过某种准入机制有过一个先在的共识文本存在。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P048", "quote": "比如，同一企业的成员，就通过雇佣合同而共同承认了企业章程", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P050", "quote": "这些先在的条件往往还是真正的主要部分，现场所被新声明的共识只是它的一个“累进更新”而已。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P052", "quote": "这也是“人以群分”的底层机制", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P053", "quote": "看作“我们是同一群体”的绝对有效判据。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P055", "quote": "抓住这些人，排除做不到的人，是一种显而易见的明智生存策略。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P031", "quote": "这也是为什么会议一定要有一个主要工作语言", "relation": "qualifies"},
    {"key": "E027", "paragraph_id": "P046", "quote": "如果此时不作放弃，那么你就放弃了求同存异的原则。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["谈判与协商", "认识论与方法论", "群体与组织"],
   "issue_candidates": ["求同存异的操作化", "共识文本的形成", "异议处理机制", "会议语言与协商成本", "群体边界"],
   "text_function_candidates": ["答疑", "操作指南", "论辩", "训诫"],
   "object_candidates": ["国家", "企业", "政党", "同盟", "会议"],
   "working_keywords": ["求同存异", "共识文本", "异议", "一票否决", "准入机制", "累进更新", "人以群分", "意志体"]
  },
  "notes": "本篇无图片节点，正文完整可读。问题（Q001）属提问者，作者未直接回应“君子和而不同”这一提法本身，而是给出自己的三原则定义与操作框架，故问题立场未计入作者主张。brief 与正文前段重合且被截断，仅作导航。文中“ta人”“ta们”为原文用法，引文按原文照录。"
 },
 "0eeda817": {
  "analysis": {
   "question_context": "提问者问怎样研究一个群体的决策机制（Q001，属提问者）。作者只给出一条研究起点（从群体的生存环境入手）和一条方法论警告（不要满足于直接观察），并自陈暂时只能泛泛说到这里，未给出具体研究步骤或指标。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "给出研究起点：首先总是要从这个群体的生存环境开始入手。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "说明理由：环境定义群体面对的问题与行为模式，决策过程与偏好归根到底被环境中最稳定的因素长期型塑。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "方法警告：不要满足于直接观察结果，世界上多的是看似民主的独裁和看似独裁的民主，那往往不能正确抓住问题本质。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "自陈把握限度：暂时只能泛泛说到这里。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张研究群体决策机制首先总是要从该群体的生存环境入手。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称生存环境定义了群体面对的问题与行为模式，群体的决策过程与决策偏好归根到底是被其环境中最稳定的因素长期型塑的。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者告诫不要满足于直接的观察结果，因为世界上多的是看似民主的独裁和看似独裁的民主，那往往并不能正确抓住问题的本质。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者自陈本篇只是提纲式回答，暂时只能泛泛说到这里。", "evidence": ["E006"]}
   ],
   "argument_steps": [
    "给起点：从群体的生存环境入手（P001）。",
    "给机制：环境定义问题与行为模式，最稳定的因素长期型塑决策过程与偏好（P002）。",
    "给警告：勿止于直接观察，表面制度形式（看似民主的独裁／看似独裁的民主）可能误导（P003）。",
    "自陈边界：暂时只能泛泛说到这里（P004）。"
   ],
   "concept_usage": [
    {"term": "生存环境", "meaning": "定义群体面对的问题与行为模式、并长期型塑其决策过程与偏好的因素总体", "evidence": "P002", "ambiguity": "未界定具体包含哪些因素（地理、经济、制度等）"},
    {"term": "看似民主的独裁 / 看似独裁的民主", "meaning": "表面制度形式与实际决策机制不一致的两类现象，作者用以警告直接观察的不可靠", "evidence": "P003", "ambiguity": "未给判别标准，也未举实例"}
   ],
   "examples_and_targets": [
    "“看似民主的独裁和看似独裁的民主”作为观察陷阱的例子（作者举例，未指名任何国家或案例，P003）"
   ],
   "conditions": [
    "“首先总是要从……开始入手”（P001，方法上的优先/必要条件）",
    "“归根到底是被其环境中最稳定的因素长期型塑的”（P002，限定为长期作用与最稳定因素）",
    "“往往并不能正确的抓住问题的本质”（P003，或然限定）",
    "“暂时来说”（P004，时间性限定，表明结论不完整）"
   ],
   "rhetoric_and_tone": "箴言式的方法论提要，句子简短、命令式（“不要满足于……”）；无案例、无论证展开，末句以自陈限度收束，语气克制。",
   "unresolved_questions": [
    "“生存环境”包含哪些因素、如何判定“最稳定”、研究的具体步骤与可操作指标，本文均未说明。",
    "未举任何具体案例；“看似民主的独裁／看似独裁的民主”的判别标准本文未说明。",
    "brief 与正文逐句重合且末句被截断（“那往往并不能正”），brief 仅作导航。",
    "元数据 updated_at（2021-05-16）晚于 published_at（2021-01-01），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "这首先总是要从这个群体的生存环境开始入手。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "生存环境定义了这个群体面对的问题，也定义了这个群体的行为模式。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P002", "quote": "这个群体做出决策的过程以及决策的偏好归根到底是被其环境中最稳定的因素长期型塑的。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "不要满足于一些直接的观察结果。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P003", "quote": "世界上多的是看似民主的独裁和看似独裁的民主。那往往并不能正确的抓住问题的本质。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P004", "quote": "暂时来说只能泛泛的说到这里。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治学方法论", "社会研究"],
   "issue_candidates": ["群体决策机制的研究方法", "环境与决策偏好的关系"],
   "text_function_candidates": ["答疑", "方法提纲"],
   "object_candidates": ["群体", "生存环境"],
   "working_keywords": ["生存环境", "决策机制", "决策偏好", "直接观察", "看似民主的独裁"]
  },
  "notes": "本篇无图片节点，正文完整可读（4 段）。brief 与正文重复且被截断，按简报只作导航。作者未给案例与操作步骤，属提纲式回答。"
 },
 "0c019eb3": {
  "analysis": {
   "question_context": "提问者就“民调显示特朗普获评 2020 美国人心中最受尊敬男性”一事征询看法（Q001，属提问者）。作者未评估民调本身，而是借题论述“成熟”与立场的关系：先立论成年人不会把一切与立场混为一谈，再举幼稚的捆绑式认知，随后以自己对特朗普努力和毅力的敬佩为例，说明尊重敌人不等于认同其主张，最后解释该称号在美国语境中的含义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出前提：想被看成成熟的人（或正确认识成熟），就要明白成年人不会将一切都和立场混为一谈。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "称小孩子最大的认知障碍与幼稚的本质特征在此：把原谅与追偿、尊重与服从、尊敬与追随、喜欢与爱、爱与顺从绑在一起。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010"], "summary": "逐条列举上述捆绑的具体表现，并称因此ta们没有 respect the enemy / game / effort 的概念。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "作者自述高度敬佩特朗普追求自身目标时的努力、毅力和坚持，称其展现了“虽千万人吾往矣”的坚决与令人惊叹的勇气和控制力。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013"], "summary": "反问嘲笑者：若被同样孤立、嘲弄、掣肘、攻击，谁有把握能有同样好的表现。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015"], "summary": "划定界限：这不影响反对他和他的主张斗争，作者称自己对其主张无任何赞同；但不要因反感一个人就认为凡尊敬这人的都是傻x。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "称看不到敌人优点、不承认敌人长处、不尊重敌人绝非对敌人的打击，反而是需要自己警醒的信号；只有被恐惧抓住的人才失去超然视角，而那往往才是真正胜利的关键。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021"], "summary": "解释称号由来：那句粗话是支持和反对双方都会给trump的共同评价，在美国人眼里是一句赞美的话。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称成年人不会将一切都和立场混为一谈，这是想被看成成熟的人、或想正确认识成熟意味着什么的人必须明白的道理。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称小孩子最大的认知障碍与幼稚的本质特征，是把原谅与追偿、尊重与服从、尊敬与追随、喜欢与爱、爱与顺从等成对概念绑在一起。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种捆绑式认知使人根本没有 respect the enemy / game / effort 的概念，并举例：认为“尊敬”必定意味着“追随”和“认同”。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自述高度敬佩特朗普在追求自己的目标时付出的努力和展现的毅力与坚持，并称在不考虑立场的前提下，其展现了“虽千万人吾往矣”的坚决与令人惊叹的勇气和控制力。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问嘲笑特朗普出丑的人：若被这样孤立、嘲弄、掣肘、攻击，你们谁有把握能有他同样好的表现。", "evidence": ["E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称敬佩不妨碍反对特朗普并与其主张斗争，并称任何了解其立场的人都知道他对其主张没有任何赞同之处。", "evidence": ["E010"]},
    {"claim_id": "C007", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述并反驳的一种看法：因为反感一个人，就理所当然认为凡尊敬这人的肯定都是傻x。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称看不到敌人的优点、不能承认敌人的长处、不能尊重敌人，绝不是一种“对敌人的打击”，反而是一种极其需要自己警醒的信号。", "evidence": ["E012", "E013"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称只有被恐惧抓住的人才会失去超然的视角，而恰恰是这超然的视角往往才是真正胜利的关键。", "evidence": ["E014", "E015"]},
    {"claim_id": "C010", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者称“a tough m*ther f*king son of b*tch”是支持和反对双方都会给trump的共同评价，并称这句话在美国人眼里是一句赞美的话。", "evidence": ["E016"]}
   ],
   "argument_steps": [
    "立论：成熟=不把一切都与立场混为一谈（P001—P002）。",
    "给反例：幼稚的本质特征是把原谅/追偿、尊重/服从、尊敬/追随、喜欢/爱、爱/顺从等绑在一起（P003—P008）。",
    "归纳：捆绑式认知使人没有 respect the enemy / game / effort 的概念（P009—P010）。",
    "自陈示范：敬佩特朗普的努力、毅力与勇气，但“在不考虑立场的前提下”说（P011—P012）。",
    "反问反驳：以嘲笑者自身能否承受同样处境质问（P013）。",
    "让步与划界：敬佩不妨碍反对其主张，作者对其主张无任何赞同（P014）。",
    "反驳对手观点：不因反感一个人就否定尊敬他的人（P015）。",
    "推进：不承认敌人优点不是打击敌人，而是恐惧的信号；超然视角才是胜利关键（P016—P019）。",
    "收尾解释称号：该粗口式评价在美国语境中是赞美（P020—P021）。"
   ],
   "concept_usage": [
    {"term": "立场", "meaning": "对特朗普及其主张的赞成或反对；作者称自己对其主张无任何赞同，并强调立场不应与尊敬、敬佩混同", "evidence": "P002", "ambiguity": "作者未给出“立场”与他所称的尊敬之间关系的系统界定"},
    {"term": "尊敬", "meaning": "对敌人付出的努力、毅力与勇气的承认，不等于服从或认同", "evidence": "P009", "ambiguity": "与“敬佩”在文中交替使用，未作区分"},
    {"term": "respect the enemy / game / effort", "meaning": "作者借英文短语指对敌人、比赛（规则）与努力的尊重，称捆绑式认知者没有这一概念", "evidence": "P010", "ambiguity": "作者未给中文对应释义，三个对象的确切所指依赖读者推断"},
    {"term": "成熟 / 幼稚", "meaning": "成熟=不将一切与立场混为一谈；幼稚的本质特征=把多组不同概念绑在一起", "evidence": "P002", "ambiguity": "作者以“小孩子”作比喻，未说明是否指实际年龄还是心理状态"},
    {"term": "超然的视角", "meaning": "不被恐惧抓住时才能保持的视角，作者称其往往是真正胜利的关键", "evidence": "P019", "ambiguity": "未说明如何获得或判定"}
   ],
   "examples_and_targets": [
    "特朗普：核心对象。作者敬佩其在追求自己目标时的努力、毅力与坚持（作者自述立场，P011—P012），同时称自己对其主张无任何赞同（P014）；并以那句粗口式评价解释其获称号的原因（P021）",
    "嘲笑特朗普出丑的“你们”：作者的反驳对象（P013）",
    "“虽千万人吾往矣”：作者引语，用于形容特朗普的坚决（P012）",
    "“a tough m*ther f*king son of b*tch”：作者转述的、支持和反对双方共同给出的评价（P021）",
    "民调与“最受尊敬男性”称号：提问者提供的话题背景，作者未核查其机制（Q001、P020）"
   ],
   "conditions": [
    "“在不考虑立场的前提下”，才称特朗普展现了勇气和控制力（P012）",
    "“这不妨碍你去反对他，和他的主张斗争”——敬佩与反对并存（P014）",
    "“任何了解我对他的立场的人”为免责限定（P014）",
    "“只有被恐惧抓住的人，才会失去超然的视角”（P018，必要条件式）",
    "“往往才是你真正胜利的关键”（P019，或然限定）",
    "“在美国人眼里”为语义语境限定，作者以此解释称号（P021）"
   ],
   "rhetoric_and_tone": "训诫与劝谕语气，直接以“你们”质问；含反问句（“你们谁有把握能有他同样好的表现？”）；格言式短句（“只有被恐惧抓住的人，才会失去超然的视角”）；先澄清自身立场再批评同侧听众，避免被误读为替特朗普主张辩护；末段直接引粗口原文并说明其在美式语境中为赞美，带调侃意味。",
   "unresolved_questions": [
    "民调本身（机构、样本、结果、评选机制）本文未说明也未核查；“最受尊敬男性”称号的由来依赖读者外部知识。",
    "特朗普受到的围攻、孤立、嘲弄、掣肘的具体事件本文未列举。",
    "P010 的“ta们”指哪些人（幼稚者、嘲笑者或一般公众）需依上下文推断，正文未明确。",
    "“respect the enemy / game / effort”中的 game 具体指什么，本文未说明。",
    "元数据 updated_at（2021-05-16）晚于 published_at（2021-01-01），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "你一定要明白一个道理：", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "成年人不会将一切都和立场混为一谈。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "小孩子最大的认知障碍就在这里，这也是幼稚的本质特征。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "那就是将原谅与追偿、尊重与服从、尊敬与追随、喜欢与爱、爱与顺从……都绑在一起。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "认为“尊敬”必定意味着“追随”和“认同”。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P010", "quote": "因此ta们根本没有respect the enemy / game / effort的概念。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P011", "quote": "我高度敬佩特朗普在追求他自己的目标时付出的努力和展现出来的毅力和坚持。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P012", "quote": "他的确展现了令人惊叹的勇气和控制力。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P013", "quote": "你们谁有把握能有他同样好的表现？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P014", "quote": "任何了解我对他的立场的人都应该知道我对他的主张没有任何赞同之处。", "relation": "qualifies"},
    {"key": "E011", "paragraph_id": "P015", "quote": "但是不要因为你反感一个人就理所当然的认为凡尊敬这人的肯定都是傻x。", "relation": "contradicts"},
    {"key": "E012", "paragraph_id": "P016", "quote": "这绝不是一种“对敌人的打击”——根本不能。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P017", "quote": "这反而是一种极其需要你自己警醒的信号。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P018", "quote": "只有被恐惧抓住的人，才会失去超然的视角。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P019", "quote": "恰恰是这个超然的视角，往往才是你真正胜利的关键。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "在美国人眼里是一句赞美的话。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理与认知", "政治评论", "修辞与说服"],
   "issue_candidates": ["立场与尊敬的区别", "敌我认知", "成熟与幼稚的判据", "美国政治人物评价"],
   "text_function_candidates": ["答疑", "评论", "论辩", "训诫"],
   "object_candidates": ["特朗普", "美国", "民调", "知乎提问者"],
   "working_keywords": ["立场", "尊敬", "求同存异外的另一面", "respect the enemy", "超然的视角", "成熟", "幼稚"]
  },
  "notes": "本篇无图片节点，正文完整可读。Q001 属提问者，其“你怎么看”的中立征询未被当作作者立场。作者明确声明对特朗普的主张无任何赞同，其对特朗普个人努力与毅力的敬佩为作者自述，已分列主张（C004/C006），不得合并为“作者支持特朗普”。末段英文粗口按原文照录为引文。working_keywords 中的“求同存异外的另一面”为本篇与同批《求同存异》的工作性关联线索，非作者用语，仅供检索。"
 },
 "dcecd060": {
  "analysis": {
   "question_context": "提问者问如何证明自己是对的（Q001，属提问者）。作者不提供证明方法，而是否定该目标本身：主张先把自己与观点分离开，搞清楚命题真假才有意义；随后批评以求胜为目的的行为模式，并以英雄主义、讨论的神圣性、参与者资格与知识来源等论点展开训诫式论述。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "给出秘诀：把自己与观点分离（Alienate yourself），命题不是“你的”、与自负无关；搞清楚真假才有意义，“证明它”毫无意义，根本不配是目标。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006"], "summary": "批评为证明自己观点“肯定是对的”而用捏造证据、辩论技巧、财力、地位、权力力求取胜，并视为与名誉、地位、权威性相关的背水之战，称其蠢到可笑。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011"], "summary": "连续追问“为什么要这样”，称这种行为模式让人变成可怜虫、丢掉被严肃对待的必要；听众的不耐烦与反击不是评判问题对错，而是惩罚你把探索真理玷污成尿远比赛。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "追问“为了什么”：为被不称职父母、不尽责师长、不友爱同侪伤得拼不起来的自尊，把任何事变成强迫别人承认、抚慰、崇拜自己的雪耻之战；并指出在场每个人同样有这三种遭遇，故“你错了”。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019"], "summary": "称“三者皆无”是三件奇迹，亚历山大、凯撒、牛顿、爱因斯坦、达尔文、马克思都没有这份幸运，并请对方把伟大名字数下来、翻遍传记验证。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025"], "summary": "提出英雄主义：放得下就是英雄；只盯问题真伪本身是自我牺牲的英雄主义；公平对待并捍卫所有提案、忘掉你我、拆散揉碎取最合理部分是集体的英雄主义；如此则真理之神同在、知识与运气分赐在场者；无私无我、唯有事实与逻辑。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031"], "summary": "称应极少用到“我”字；充斥“我”字的对话是谈判，而知识不能由一群人谈判决定；在场者在乎“哪个方案最好”而非“谁的方案最好”；以反问斥责强夺他人时间证明自己伟大者。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "称讨论是所有参与者用生命做献祭以求知识的神圣之事，没有你我他、没有胜负，只有对亵渎者的愤怒；人不是在攻击你的观点而是在惩罚你糟蹋众人生命；以“我的观点正确”辩解无效，即使证明你是对的也必遭放逐。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P039", "P040", "P041", "P042"], "summary": "给出反向职责：避免不懂、不尊重讨论真实属性的人闯入，介绍人须为被介绍者负责；参与资格不是学历、证书、职位，而是懂不懂“讨论”到底是什么。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P043", "P044", "P045"], "summary": "对比：由“学术权威”和“天才”参与的尿尿比赛只留一地污秽；由文盲合作的真正讨论也会有令圣哲三思的结晶；知识不是靠“伟大的头脑”想出来的，而是靠在场者恪尽职守、英勇放下执念，因受世界祝福而被赐予的。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P046", "P047", "P048"], "summary": "收束训诫：记住这一点；停止在还穿着开裆裤的小屁孩身上浪费生命；去拿拖把把地拖干净。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问“如何证明自己是对的？”——其预设是把“证明自己正确”当作可欲目标；作者否定该目标本身，未给出任何证明方法。", "evidence": []},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称至关重要的秘诀是把你自己和观点分离开，该命题并不是“你的”命题、不是你的主张或发明、与自负无关。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称搞清楚命题是真是假才有意义，而“证明它”是一个毫无意义的目标，甚至根本就不该是、不配是一个目标。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问批评：为证明自己观点“肯定是对的”而用捏造的证据、辩论技巧、财力、地位、权力力求取胜，并视为与名誉、地位、权威性相关的背水之战，本身就蠢到可笑。", "evidence": ["E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种行为模式本身让人变成可怜虫、丢掉被任何人严肃对待的必要；听众的不耐烦和反击不是出于问题对错，而是在惩罚你把探索真理玷污成尿远比赛。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者反驳“不称职的父母、不尽责的师长、不友爱的同侪”是只有自己才有的不幸：在场每一个人都同样有，三者皆无才是三件奇迹，亚历山大、凯撒、牛顿、爱因斯坦、达尔文、马克思都没有这份幸运。", "evidence": ["E009", "E010", "E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称放得下就是英雄；在探讨问题时眼睛只盯着问题本身的真伪，本身就是一种自我牺牲的英雄主义；公平对待并捍卫所有提案、忘记你我、拆散揉碎取最合理部分，是集体的英雄主义。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称你感受到这种英雄气，真理之神就与你们同在，知识甚至运气就会分赐给所有在场的人；无私无我、唯有事实与逻辑才是一场讨论应该给你的体会。", "evidence": ["E015", "E016"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称讨论中应极少有机会用到“我”字；充斥“我”字的对话是谈判，而知识不能由一群人谈判决定；在场者在乎的是“哪个方案最好”而不是“谁的方案最好”。", "evidence": ["E017", "E018", "E019"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称一场讨论是所有参与者用生命做献祭以求知识的神圣的事，没有“你的”“我的”“ta的”，根本没有什么“胜负”，只有对亵渎者的愤怒；人不是在攻击你的观点，而是在惩罚你糟蹋这么多人生命的行为。", "evidence": ["E020", "E021", "E022"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称用自己的观点有多正确来“辩解”是无效的，即使证明你是对的，你也必遭放逐。", "evidence": ["E023", "E024"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称明白此理者负有天然职责：避免让不懂、不尊重讨论真实属性的人闯入；谁介绍来的谁就要为ta负责；参加讨论的资格不是学历、证书、职位，而是懂不懂“讨论”到底是什么。", "evidence": ["E025", "E026", "E027"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称由“学术权威”和“天才”参与的尿尿比赛只会留下一地污秽，而由文盲合作的真正的讨论一样会有令圣哲也要三思的结晶；知识不是靠“伟大的头脑”想出来的，而是靠在场的所有人恪尽职守、英勇放下执念，因受世界的祝福而被赐予的。", "evidence": ["E028", "E029", "E030"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以训诫收束：停止在还穿着开裆裤的小屁孩身上浪费生命。", "evidence": ["E031"]}
   ],
   "argument_steps": [
    "给前提：把自己与观点分离，命题不是“你的”，与自负无关（P001—P003）。",
    "否定目标：真假才有意义，“证明它”无意义、不配为目标（P004—P005）。",
    "给反例并反问：以捏造证据、辩论技巧、财力、地位、权力求胜是蠢到可笑（P006—P008）。",
    "归因：这种行为模式使人变成可怜虫，听众反击是在惩罚对真理的玷污（P009—P010）。",
    "追问动机：是否在把一切变成强迫他人承认自己的雪耻之战（P012—P013）。",
    "反驳借口：三种不幸人人皆有，“三者皆无”才是奇迹，并请对方查证伟人传记（P014—P019）。",
    "提出正面标准：放得下是英雄；只问真伪是自我牺牲的英雄主义；公平对待所有提案是集体英雄主义（P020—P025）。",
    "以“我”字为判据：充斥“我”字的是谈判，知识不能靠谈判决定（P026—P028）。",
    "升级定性：讨论是以生命献祭求知识的神圣之事，无你我、无胜负，只有对亵渎者的愤怒；辩解无效，证明对了也遭放逐（P032—P038）。",
    "给出职责与资格标准：挡住不懂讨论的人，资格在懂不懂“讨论”本身（P039—P042）。",
    "对比两种讨论（权威的尿尿比赛／文盲的真正讨论），说明知识来源（P043—P045）。",
    "训诫收束：停止浪费生命，去把地拖干净（P046—P048）。"
   ],
   "concept_usage": [
    {"term": "把你自己和这个观点分离开（Alienate yourself）", "meaning": "作者所称的首要秘诀：不把命题当作“我的”主张、发明，与自负脱钩", "evidence": "P001", "ambiguity": "作者未给出可操作的分离方法"},
    {"term": "证明", "meaning": "作者否定意义上的“证明自己是对的”，与“搞清楚命题真假”相对", "evidence": "P004", "ambiguity": "作者未说明通常意义的证明与这里的“证明”是否同一所指"},
    {"term": "英雄主义 / 英雄气", "meaning": "放下自我执念、只问问题真伪（自我牺牲的英雄主义）与公平对待并捍卫所有提案（集体的英雄主义）", "evidence": "P021", "ambiguity": "两种英雄主义的关系与判定标准未说明"},
    {"term": "“我”字（作为判据）", "meaning": "作者把对话中“我”字出现的频率当作是否在谈判而非探讨问题的信号", "evidence": "P026", "ambiguity": "为修辞性判据，未给严格标准"},
    {"term": "讨论", "meaning": "所有参与者用生命做献祭以求知识的神圣合作，无胜负、无你我，参与者须具备懂“讨论”为何物的资格", "evidence": "P032", "ambiguity": "与一般意义的辩论、谈判的边界，作者以态度而非规则区分"},
    {"term": "亵渎者 / 亵渎", "meaning": "出于自私、猥琐和傲慢糟蹋讨论这一神圣事务的人及其行为", "evidence": "P035", "ambiguity": "判定主体与程序未说明"}
   ],
   "examples_and_targets": [
    "捏造的证据、辩论的技巧、财力、地位、权力：作者列举的求胜手段（批评对象，P006）",
    "尿远比赛 / 尿尿比赛：作者对以求胜为目的之“讨论”的贬称（修辞，P010、P043）",
    "不称职的父母、不尽责的师长、不友爱的同侪：作者假设的对方动机来源，并反驳其为“标配”（P013—P015）",
    "亚历山大、凯撒、牛顿、爱因斯坦、达尔文、马克思：作者用以说明“三者皆无”之罕见的例子（P018）",
    "圆桌、介绍人、学历/证书/职位：作者论参与者资格时的比喻与列举（P039—P041）",
    "文盲合作的真正讨论（对照例，P044）",
    "开裆裤的小屁孩、拖把：收尾训诫的修辞材料（P047—P048）"
   ],
   "conditions": [
    "论述以第二人称“你”为对象，针对的是“以求胜证明自己正确”的行为模式，而非某一具体学科问题",
    "“不管这是多么可怜的权力”为插入性限定（P006）",
    "“在探讨问题时”限定英雄主义的适用范围（P021）",
    "“如果你明白这个道理”为条件句，才推出防止他人闯入的职责（P039）",
    "“一场由所谓‘学术权威’和‘天才’参与的”与“一场由文盲合作的”为对照条件（P043—P044）",
    "“这资格不是指学历、不是指证书、不是指职位”为否定式限定（P041）"
   ],
   "rhetoric_and_tone": "极强烈的训诫与斥责语气：连续反问（“为什么要这样？”“为了什么？”“想想清楚！”“你有什么资格强夺别人的时间来证明自己的伟大？”）、感叹句密集、祈使句收尾（“停止在还穿着开裆裤的小屁孩身上浪费生命！”“另外去拿拖把把地给我拖干净！”）；使用粗俗贬称（“尿远比赛”“尿尿比赛”“小屁孩”）与宗教式措辞（“真理之神”“神圣”“献祭”“亵渎”“受世界的祝福”）；第二人称“你”贯穿全篇。",
   "unresolved_questions": [
    "提问（Q001）的预设被作者否定，但作者未给出任何可操作的“证明”方法，也未说明在何种场合证明是必要的。",
    "“把你自己和这个观点分离开”的具体做法本文未说明。",
    "作者未说明如何区分“探讨问题”与“谈判”，只以“我”字出现频率作修辞性判据。",
    "“谁介绍来的谁负责”在实践中的追责方式本文未说明。",
    "“ta的”在 P033 中作为被否定的所有格出现，作者未说明其与“他/她”的用法关系（全文用“ta”）。",
    "元数据 updated_at（2025-10-07）远晚于 published_at（2021-01-02），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "把你自己和这个观点分离开（Alienate yourself）。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "你打算搞清楚的这个命题，并不是“你的”命题。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "不是“你的主张”，不是“你的发明”，和你的自负（ego）无关。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "搞清楚它是真是假才是有意义的，“证明它”是一个毫无意义的目标。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "甚至根本就不该是一个目标，不配是一个目标。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "以至于要用捏造的证据、用辩论的技巧、用财力、用地位、用权力（不管这是多么可怜的权力）来力求取胜", "relation": "contradicts"},
    {"key": "E007", "paragraph_id": "P009", "quote": "是这样的行为模式本身让你变成可怜虫，让你自己丢掉了任何人严肃对待你的必要。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "而是在惩罚你把探索真理这样一件神圣的事务玷污成了尿远比赛。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P014", "quote": "在场的人，每一个人都同样有不称职的父母、不尽责的师长、不友爱的同侪！", "relation": "contradicts"},
    {"key": "E010", "paragraph_id": "P017", "quote": "“三者皆无”，这是三件奇迹。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P018", "quote": "这份幸运，亚历山大没有、凯撒也没有、牛顿也没有、爱因斯坦也没有、达尔文也没有、马克思也没有。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P020", "quote": "放得下，就是英雄。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P021", "quote": "在探讨问题时，眼睛只盯着问题本身的真伪，这本身就是一种自我牺牲的英雄主义行为。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "公平的对待所有摆在桌面上的提案，公平的捍卫所有的提案，忘记所谓的你的我的", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "你感受到这种英雄气，真理之神就与你们同在。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P025", "quote": "无私无我，唯有事实与逻辑——这才是一场讨论应该给你的体会。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P026", "quote": "你应该极少有机会用到“我”字！", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P027", "quote": "那是谈判！知识是可以由一群人谈判决定的吗？！", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P028", "quote": "在场所有的人在乎的是“哪个方案最好”，不是“谁的方案最好”。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P032", "quote": "一场讨论，是所有参与者用生命做献祭以求知识的神圣的事。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P034", "quote": "根本没有什么“胜负”。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P036", "quote": "人不是在“攻击”你的“观点”，人是在惩罚你糟蹋这么多人生命的行为！", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P037", "quote": "你用自己的观点有多正确来“辩解”是无效的！", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P038", "quote": "证明你是对的，你也必遭放逐！", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P039", "quote": "避免让不懂、不尊重这件事的真实属性的人闯入。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P040", "quote": "这人是谁介绍来的，谁就要为ta负责。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P042", "quote": "这个资格是指懂不懂“讨论”到底是什么。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P043", "quote": "一场由所谓“学术权威”和“天才”参与的尿尿比赛也一样只会留下一地污秽。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P044", "quote": "一场由文盲合作的真正的讨论，一样会有令圣哲也要三思的结晶。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P045", "quote": "知识不是靠所谓“伟大的头脑”“想”出来的", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P047", "quote": "停止在还穿着开裆裤的小屁孩身上浪费生命！", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认识论与讨论伦理", "说服与辩论", "教育与人格"],
   "issue_candidates": ["证明自己正确的目标是否成立", "讨论中的自我与立场", "参与讨论的资格", "知识的来源"],
   "text_function_candidates": ["答疑", "训诫", "论辩", "批评"],
   "object_candidates": ["提问者", "学术权威", "天才", "文盲", "父母", "师长", "同侪", "亚历山大", "凯撒", "牛顿", "爱因斯坦", "达尔文", "马克思"],
   "working_keywords": ["Alienate yourself", "证明", "英雄主义", "尿远比赛", "讨论", "资格", "献祭", "亵渎"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问（Q001）的预设被作者正面否定，已作 open_question/questioner 单列，未把“如何证明自己是对的”当作作者主张。文中对“你”的斥责属训诫修辞，作者未指名任何现实对象；对提问动机（不称职的父母等）的描写是作者的反问与归因，非事实认定。"
 },
 "24f7df8d": {
  "analysis": {
   "question_context": "提问者问如何提升自己的格局（Q001，属提问者）。作者以判据式短答回应“不怕肯定别人，不惜否定自己”，随即指出多数人自以为做到、实际是以认错交换想要的结果，并分别界定“否定自己”与“肯定ta人”的真实含义；未给出训练步骤。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "正面作答：不怕肯定别人，不惜否定自己。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "指出很多人都觉得自己做到了，但这并没那么容易做到。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "称绝大多数人的实际做法是出于害怕他人的某个决定，用“我错了”“你是对的”交换自己想要的结果；作者定性为出卖自己、收买他人，是另一门生意。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "界定“否定自己”：在逻辑上真正找到自己判断中的逻辑断裂和论据不充分；否定到底的结果是更接近正确，而不是“你失败了”。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012"], "summary": "界定“肯定ta人”：在他人论证中找到你应该承认的论证和证据；结果未必是“ta是对的”，更不是“我送你一场胜利，求你多爱我一会儿”。", "role": "definition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对“如何提升格局”的回答是：不怕肯定别人，不惜否定自己。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称很多人都觉得自己做到了，但这可没那么容易做到。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称绝大多数人所做的其实只是因为害怕他人的某个决定，用“我错了”“你是对的”来交换一个自己想要的结果；这不叫“否定自己”“肯定他人”，而叫出卖自己、收买他人，完全是另一门生意。", "evidence": ["E004", "E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“否定自己”：在逻辑上真正的找到自己的判断中的逻辑断裂和论据不充分；否定到底的结果是你更接近正确了，而不是“你失败了”。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者界定“肯定ta人”：在他人的论证中找到你应该承认的论证和证据；肯定的结果未必是“ta是对的”，更不是“我送你一场胜利，求你多爱我一会儿”。", "evidence": ["E009", "E010", "E011"]}
   ],
   "argument_steps": [
    "正面立论：不怕肯定别人，不惜否定自己（P001）。",
    "加限定：很多人自以为做到，实际并不容易（P002—P003）。",
    "揭示实际行为：因害怕他人的决定而用认错交换结果（P004）。",
    "定性：这叫出卖自己、收买他人，是另一门生意（P005—P007）。",
    "给出“否定自己”的真实含义与结果（P008—P009）。",
    "给出“肯定ta人”的真实含义与结果，并排除两种误解（P010—P012）。"
   ],
   "concept_usage": [
    {"term": "格局", "meaning": "提问用语与篇题；作者未加定义，只以“不怕肯定别人，不惜否定自己”作答", "evidence": "P001", "ambiguity": "作者未说明格局与这两个行为之间的推导关系"},
    {"term": "否定自己", "meaning": "在逻辑上真正找到自己判断中的逻辑断裂和论据不充分；结果是更接近正确而非失败", "evidence": "P008", "ambiguity": "与自我贬低、认错的边界，作者以“逻辑上”限定但未给判据"},
    {"term": "肯定ta人", "meaning": "在他人的论证中找到你应该承认的论证和证据；结果未必是承认ta对", "evidence": "P010", "ambiguity": "“应该承认”的标准未说明"},
    {"term": "出卖自己，收买他人", "meaning": "作者对以“我错了”“你是对的”换取自己想要结果的定性", "evidence": "P006", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "“我错了”“你是对的”：作者引述多数人用以交换结果的两句话（P004）",
    "“我送你一场胜利，求你多爱我一会儿”：作者用以讽刺的引语（P012）",
    "“绝大多数人”：作者批评的对象，未指名、未给数据（P004）"
   ],
   "conditions": [
    "“很多人”“绝大多数人”为量化限定，作者未给任何数据来源（P002、P004）",
    "“这完全是另一门生意”表明作者把交换式认错排除在“否定自己/肯定他人”之外（P007）",
    "“未必是‘ta是对的’”“更不是……”为否定式限定，保留结果的其他可能（P011—P012）"
   ],
   "rhetoric_and_tone": "简短问答体：先给八字式答案，再纠偏；用“这不叫……这叫……”的对比句式定性；结尾以带讥讽的引语（“求你多爱我一会儿”）收束，语气冷静而带刺，无训诫式长篇展开。",
   "unresolved_questions": [
    "作者未定义“格局”本身，也未说明“不怕肯定别人，不惜否定自己”为何能提升格局。",
    "如何在实践中区分“真正的否定自己”与“以认错换结果”，本文未给判据。",
    "未给任何提升方法、训练步骤或实例。",
    "元数据 updated_at（2025-03-31）晚于 published_at（2021-01-02），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "不怕肯定别人，不惜否定自己。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "我发现很多人都觉得自己做到了。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这可没那么容易做到。", "relation": "qualifies"},
    {"key": "E004", "paragraph_id": "P004", "quote": "绝大多数人所做的其实只是因为害怕他人的某个决定，用“我错了”，“你是对的”来交换一个自己想要的结果。", "relation": "contradicts"},
    {"key": "E005", "paragraph_id": "P006", "quote": "这叫出卖自己，收买他人。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "这完全是另一门生意。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "否定自己，是指在逻辑上真正的找到自己的判断中的逻辑断裂和论据不充分，", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "否定到底的结果是你更接近正确了，而不是“你失败了”；", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "肯定ta人，是指在他人的论证中找到你应该承认的论证和证据，", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "肯定的结果未必是“ta是对的”。", "relation": "qualifies"},
    {"key": "E011", "paragraph_id": "P012", "quote": "更不是“我送你一场胜利，求你多爱我一会儿”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认知与自我修养", "说服与沟通"],
   "issue_candidates": ["格局的提升", "否定自己与肯定他人的真实含义", "以认错交换利益"],
   "text_function_candidates": ["答疑", "纠偏", "评论"],
   "object_candidates": ["提问者", "绝大多数人"],
   "working_keywords": ["格局", "肯定别人", "否定自己", "逻辑断裂", "论据不充分", "出卖自己，收买他人"]
  },
  "notes": "本篇无图片节点，正文完整可读（12 段）。Q001 属提问者；作者的回答简短，未展开操作步骤。“绝大多数人”为作者概括，正文未给数据来源，故未按事实断言处理。"
 },
 "373f860b": {
  "analysis": {
   "question_context": "提问者问如何判断个人的悟性高低（Q001，属提问者）。作者先描述“思考”的循环过程，再给出判断标准：悟性即“修改再试”的热情及其所客观呈现的“勤奋”，没有悟性则是没有审视、没有修改、只有再试；随后把这种表现解释为一种对父母和老师的隐性报复，并以引述的子女内心独白展开，最后直接警示父母。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "描述思考过程：解不开就退后审视方法、修改再试，反复循环；即使验证了结论、有更优雅解法、甚至发现更好的问题提法，仍退后审视、修改再试、回到第一步。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P012"], "summary": "插入一句感叹（“唉，人为什么非要吃饭和睡觉呢。”）作节奏转折。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014"], "summary": "给出判断标准：悟性就是“修改再试”的热情，是这种热情所客观呈现的“勤奋”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "给反面标准：没有悟性就是没有“审视”、没有“修改”、只有“再试”；并以上了发条、跑到门边不停撞门的铁皮青蛙作比，直到爹妈因“努力”而放过自己。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "重新定性：这其实不是“没有悟性”的问题，而是一种隐性的报复，报复只想多快好省拿到好成绩单以证明自己尽责/绩效优秀的父母和老师；随后以引述的子女内心独白展开。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P032", "P033"], "summary": "要求每一个父母看清楚这段话，并说明这也是把答案放在“家族答集”里的原因。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P034", "P035"], "summary": "警告：每一个子女手里都有这件武器，最后输的一定是父母。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称思考的过程就是解不开就立刻退后审视自己的方法、修改方法之后再试；即使验证了结论、发现更优雅的解决、甚至发现更好的问题提法，也仍退后审视、修改再试，回到第一步。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定悟性：就是“修改再试”的热情，是这种热情所客观呈现的“勤奋”。", "evidence": ["E004", "E005"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者界定“没有悟性”：就是没有“审视”、没有“修改”、只有“再试”。", "evidence": ["E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以铁皮青蛙作比：那种毫无修改的反复再试就像上了发条、跑到门边不停撞门的青蛙，直到爹妈因为“努力”而放过自己为止。", "evidence": ["E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这其实不是“没有悟性”的问题，而是一种隐性的报复。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是在报复那些只想多快好省拿到一张好成绩单、拿去证明自己已经尽责／绩效优秀的父母和老师。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "hypothetical", "statement": "作者引述／代拟的子女内心独白：自称没有“不努力”、只是单纯的“没有悟性”，把命拼上、保证努力到父母没有借口，以此让父母无法交差——此段为被引述的子女声音，非作者本人主张。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求每一个父母都看清楚这段话，并称这是他把该答案放在家族答集里面的原因。", "evidence": ["E013", "E014"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者警告父母：每一个子女手里都有这件武器，最后输的一定是你们。", "evidence": ["E015", "E016"]}
   ],
   "argument_steps": [
    "定义思考：解不开→退后审视方法→修改→再试，反复循环，直至验证结论乃至更换问题提法（P001—P011）。",
    "插入感叹句作转折（P012）。",
    "给正面判据：悟性=“修改再试”的热情=客观呈现的“勤奋”（P013—P014）。",
    "给反面判据：没有悟性=没有审视、没有修改、只有再试（P015—P018）。",
    "用铁皮青蛙比喻其机械性与“为免被追究而努力”的性质（P019）。",
    "重新定性：这不是没有悟性，而是隐性的报复（P020）。",
    "指明报复对象：只要好成绩单以证明自己尽责/绩效优秀的父母和老师（P021）。",
    "以引述的子女内心独白呈现报复的逻辑（P022—P031）。",
    "对父母喊话：看清楚这段话，并说明该答案属“家族答集”（P032—P033）。",
    "以预测收束：子女手里都有这件武器，最后输的一定是父母（P034—P035）。"
   ],
   "concept_usage": [
    {"term": "悟性", "meaning": "作者界定为“修改再试”的热情，以及这种热情所客观呈现的“勤奋”；反面是没有审视与修改、只有再试", "evidence": "P013", "ambiguity": "作者把悟性与热情、勤奋等同，未区分天赋与行为倾向"},
    {"term": "审视", "meaning": "退后检查自己所用的方法", "evidence": "P001", "ambiguity": "审视的标准与深度未说明"},
    {"term": "修改", "meaning": "在再试之前改动方法；没有悟性的表现即完全没有修改", "evidence": "P015", "ambiguity": "无"},
    {"term": "隐性的报复", "meaning": "作者对“只努力不改方法”这一表现的解释：以表面的努力使父母无法交差", "evidence": "P020", "ambiguity": "是否为子女自觉行为，本文未说明"},
    {"term": "这件武器", "meaning": "子女以“努力但没悟性”使父母无法交差的手段", "evidence": "P034", "ambiguity": "无"},
    {"term": "家族答集", "meaning": "作者自述该答案所属的集合/栏目", "evidence": "P033", "ambiguity": "属平台/栏目信息，正文未解释其范围"}
   ],
   "examples_and_targets": [
    "上了发条但已经跑到门边的铁皮青蛙（作者比喻，P019）",
    "“好成绩单”“绩效优秀”（作者指父母与老师的诉求，P021）",
    "子女的内心独白（作者引述/代拟，P022—P031）",
    "“唉，人为什么非要吃饭和睡觉呢。”（插入的感叹，P012）",
    "“家族答集”（作者自述答案所属集合，P033）"
   ],
   "conditions": [
    "“直到感觉解开了”表明循环的结束以主观感觉为条件（P004）",
    "“每一个父母”“每一个子女”“最后输的一定是你们”为全称与预测性表述，作者未给依据（P032、P034、P035）",
    "反面判据以“没有……没有……只有……”三重否定界定（P015）",
    "该文以父母为主要读者对象，末段直接对“你们”（父母）说话（P032—P035）"
   ],
   "rhetoric_and_tone": "排比与重复构成节奏（“没解开，退后审视，修改再试”等连写五段）；插入感叹句（P012）调节语气；以铁皮青蛙作讽刺比喻；引号内自 P022 至 P031 排布子女内心独白，语气激烈（“我拼了这条命”“我看你们拿什么交差”）；末段直接对父母喊话，带警告与宣判语气。",
   "unresolved_questions": [
    "“悟性”与“勤奋”的关系（是否同一事物的内外两面）本文未进一步说明。",
    "未给出判断他人悟性高低的可操作标准；“审视”与“修改”达到何种程度才算有悟性，本文未说明。",
    "“隐性的报复”是否为子女的自觉行为，本文未说明。",
    "引号内子女独白的说话者未在正文中标明，仅由 P032“每一个父母，都看清楚这段话”间接指向子女视角。",
    "正文出现“家族答集”（P033），属平台/栏目名混入正文，未见于 lexical 结构节点。",
    "元数据 updated_at（2023-04-07）晚于 published_at（2021-01-02），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "就是一个问题解不开，立刻退后审视自己的方法，修改方法之后再试；", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P006", "quote": "再次验证了结论，但觉得还可以有更优雅的解决，退后审视，修改再试；", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P008", "quote": "再次验证了结论，但发现问题本身可以有更好的提法，退后审视，重新提出问题；", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P013", "quote": "悟性是什么东西？就是“修改再试”的热情，", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P014", "quote": "是这种热情所客观呈现的“勤奋”。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P015", "quote": "什么叫没有悟性？就是没有“审视”、没有“修改”、只有“再试”。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P019", "quote": "就像上了发条但已经跑到门边的铁皮青蛙，不停的咔哒、咔哒、咔哒撞门，直到爹妈因为“努力”而放过自己为止。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P020", "quote": "这其实不是“没有悟性”的问题，而是一种隐性的报复。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P021", "quote": "这是在报复那些只想多快好省的得到一张好成绩单，拿去证明自己已经尽责/绩效优秀的父母和老师——", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P022", "quote": "我没有“不努力”，我只是单纯的“没有悟性”。", "relation": "context"},
    {"key": "E011", "paragraph_id": "P025", "quote": "我拼了这条命——反正我活着只是满足你们无尽虚荣的工具，", "relation": "context"},
    {"key": "E012", "paragraph_id": "P028", "quote": "但是我蠢，可以吗？", "relation": "context"},
    {"key": "E013", "paragraph_id": "P032", "quote": "每一个父母，都看清楚这段话。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P033", "quote": "这也是我为什么把这个答案放在家族答集里面。", "relation": "context"},
    {"key": "E015", "paragraph_id": "P034", "quote": "每一个子女手里都有这件武器，", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P035", "quote": "最后输的一定是你们。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育与亲子关系", "学习方法与认知", "心理动机"],
   "issue_candidates": ["悟性的判据", "努力与改方法", "子女对父母教育方式的隐性反抗"],
   "text_function_candidates": ["答疑", "经验总结", "训诫"],
   "object_candidates": ["父母", "老师", "子女", "家族答集"],
   "working_keywords": ["悟性", "审视", "修改再试", "铁皮青蛙", "隐性的报复", "好成绩单", "家族答集"]
  },
  "notes": "本篇无图片节点，正文完整可读（35 段）。P033 提及“家族答集”属平台/栏目名混入正文，已登记。P022—P031 引号内为被引述/代拟的子女内心独白，依 P032 的提示未归为作者主张，已单列为 quoted_or_cited/unknown。Q001 属提问者，作者的回答侧重“无悟性”的表现与动机，未给出可直接测量他人的标准。"
 },
 "d5d2eb94": {
  "analysis": {
   "question_context": "提问者是家长：孩子住校晚上打游戏到深夜影响别人，对舍管指正批评过度敏感，遇此类事觉得全世界和他作对，家长该怎么办（Q001，属提问者）。作者未按家长视角给操作建议，而是换一个方向、以书信体直接对“你”（子女）说话：先陈述社会秩序与个人自由的机制，否认“统治阶级阴谋”式解释，再指出抱怨与发脾气是低效努力，随后转为自我归责——承认自己长期直接满足孩子的愿望、以牺牲其学习处理不满足的机会为代价——最后把“在可以推卸责任时选择承担责任”确立为尊严的根基，并当场授予孩子直呼其名的权利。P001 交代原答被平台删除、遂换方向，属元话语。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "元话语：原答写了一半被知乎吞掉，故换一个方向说。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "社会有秩序，其中最大的秩序是个人自由；侵犯他人合法权利会招致有责任维护者与你为敌，若仍无效还会有更高更多的力量被动员起来；因此确实是全世界要与你为敌，而且这不是主观感觉而是事实。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "否认“少数统治阶级的阴谋”这一解释：原因是这种逻辑下的社会在现代化竞争里会毫无战斗力、会被别的社会形态吞没统治同化；此系物竞天择路径展露的天意，与万有引力无本质区别；觉得公平与否、接受与否都不改变事实。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "限定：世界是否与你为敌你改变不了（投石入水不能要求不起波纹）；要么打败世界。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012"], "summary": "推翻秩序重建新秩序并非无人做到（举新中国），但需要大量愿紧紧团结、舍生忘死的同志；对同寝室同学和宿管团结失败，至少要有大得多的群体团结成功来抵偿，否则即净失败；后续行为应走向更有效更广泛的团结。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "指出“你”所做的只是向作者抱怨哭诉；作者本已站在其一边，哭诉折算成愿承受的损失并未提高上限多少；这至少是低效努力，唯一净效果是造成“已足够努力”的幻觉，便于接受失败。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "限定：生气没问题，成年后无人评判你的想法对错；问题在于能否做到、是否打算承受愿望的全部重量、是否想透彻；仅发脾气是希望一表达强烈愿望世界就如你所愿。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025"], "summary": "自我归责：怪自己没让孩子明白世界的游戏规则、使其误以为许愿即可实现；因不能忍受孩子困苦、为最快缓解自己的痛苦而常直接替其实现愿望；这牺牲了孩子学习处理不满足的机会，是贿赂欲望、使孩子成为同谋，两个软弱的人私相贿赂、出卖了本来可以伟大的灵魂。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P026", "P027", "P028"], "summary": "责任划分：今天之前孩子不知情故无责任，今天起要负起看守自己灵魂的责任；作者负责停止行贿，孩子负责停止受贿。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035"], "summary": "追问：不会做上述计算也怪作者，可接受计算错误、水平不够，但要问选择“发脾气”之前有没有做过计算；若没做过则你可以怪我，这确可理解为没让你学会让理智凌驾于情绪，未成年时作者负一切教育责任、无自我辩护余地；最后反问是否要认定这全是作者的责任。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040", "P041"], "summary": "以“很好”应答，记下具体时刻（2021年1月3日13点33分）；指出孩子在可以合法推卸全部责任时选择承担一部分责任，并因此获得直呼作者名字、禁止作者用小名称呼的权利。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046"], "summary": "提出尊严论：在可以不承担时决定承担自己选择的责任是尊严的根基（非破坏能力、父母、学历才干）；推卸责任或呼叫父母买单者失去尊严；尊严是他人对你价值的本能敬畏；不能分担反而加重他人负担者被视为待清扫的垃圾、待卸的包袱，人们凭吃亏的感觉即发动排斥与攻击，故难免遍体鳞伤。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P047", "P048"], "summary": "要求孩子回答现在打算怎么做。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053"], "summary": "人可以怎么生活不由统治阶级、父母、老师或敌人规定；世界埋藏了决定所有人行为方向的规则，是规则在回应你（放开苹果即下落；推卸责任增加他人负担，人就用轻蔑、攻击排除你）；奖惩机制已告诉你有尊严、受尊敬和爱戴的人生该怎样过，但其复杂性需一生理解，作者自陈也时常被它教育；作者会陪着孩子摸索，将来孩子的领悟可做作者老师。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P054", "P055", "P056", "P057"], "summary": "再次道歉未尽教导之责；感激并自豪于孩子选择承担部分责任；要求去做刚才决定要做的，再看结果与后续；以“去吧”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称社会是有秩序的，其中最大的秩序就是个人自由；侵犯别人的合法权利，所有对维护该权利有责任的人就不得不行动起来与你为敌，若这些人行动仍无效，还会有更高更多的力量被动员起来与你为敌。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“全世界都要与你为敌”不是你觉得如此而已，事实就是如此。", "evidence": ["E004", "E005"]},
    {"claim_id": "C003", "claim_type": "opponent_view", "attribution": "opponent", "modality": "negated", "statement": "作者转述并否认的一种解释：这种与违规者为敌的局面是“少数统治阶级的阴谋”。持论者与出处未指明。", "evidence": ["E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的替代原因：不遵守这个逻辑的社会在现代化的竞争里会毫无战斗力，会被别的社会形态吞没、统治和同化，到最后还是会稳定在现在这个现状上。", "evidence": ["E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是通过物竞天择的路径展露的天意，和万有引力把所有苹果都拉着往下掉没有本质的区别；觉得公平也罢、不公平也罢，接受也罢、不接受也罢，事实就是如此。", "evidence": ["E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称世界会不会与你为敌这个部分你改变不了（如同丢石入水不能要求水不起波纹）；要么你打败世界。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称不能接受现有秩序、将它推翻重建并非没有人做到过（并以“不然哪来的新中国呢”为例），但那需要同志，大量愿意紧紧团结、舍生忘死的同志。", "evidence": ["E013", "E014"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称对同寝室同学和宿管的团结失败，至少需要有一个大得多的群体与你团结成功作为有效抵偿，否则本身就是一种净失败；接下去的行为应该走向更有效、更广泛的团结。", "evidence": ["E015", "E016"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称“你”所做的只是向作者抱怨、哭诉不满；作者本已站在其一边，哭诉虽可能增强支持动机，但折算成打算为这件事承受的损失并未提高上限多少；这就算不是无效的，至少也是低效的努力，唯一净效果只是造成“已经做了足够努力”的幻觉，使其较易接受随之而来的失败。", "evidence": ["E017", "E018", "E019", "E020"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称你生气没什么问题，成年后也没有人能说你的想法对或不对；所有问题在于你能不能做得到、是否打算承受自己愿望的全部重量、是否把整个事情想透彻了。", "evidence": ["E021", "E022"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自我归责：这不全怪你，先要怪作者——作者没让孩子明白世界的游戏规则，使其误以为只要许愿作者就能实现；因为不能忍受孩子困苦、为最快缓解自己的痛苦，作者常常直接替其实现愿望和需求。", "evidence": ["E023", "E024", "E025"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把这种代偿定性为贿赂：这对他自己有好处，却以牺牲孩子学习努力处理自己不满足的机会为代价；他为了自己的脆弱牺牲了孩子的成长，只是贿赂了孩子的欲望、使其成为同谋；这种事情终究是两个软弱的人私相贿赂，出卖了一个本来可以伟大的灵魂。", "evidence": ["E026", "E027", "E028"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者划分责任：今天之前的你没有责任（作为受教育者不知情，是作者身为教育者的失职）；但今天起你要负起看守自己灵魂的责任；作者负责停止行贿，你要负责停止受贿。", "evidence": ["E029", "E030", "E031"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：你选择“发脾气”这个反应之前，做过这个计算没有？若没做过则你可以怪我，这确可理解为作者没给足够教导、没让你学会让理智凌驾于情绪，未成年时作者负一切教育责任、无自我辩护余地；并反问：那么你要选择认定这全是我的责任吗？", "evidence": ["E032", "E033", "E034", "E035", "E036"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认定：孩子在可以合理合法推卸掉全部责任时选择自己承担起一部分责任；因为这个选择，从这一刻起孩子有权利直呼作者的名字，也可在任何时候禁止作者用小名称呼他。", "evidence": ["E037", "E038"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称在可以不承担的时候决定承担起自己选择的责任，这就是一个人尊严的根基——不是造成破坏的能力、不是尊贵的父母、不是学历才干；在该担当的时候推卸责任或呼叫父母买单的人则会失去尊严。", "evidence": ["E039", "E040", "E041"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定尊严是他人对你价值的本能敬畏；不能分担他人生活重负、反而加重他人负担的人会被每个人本能地看成待清扫的垃圾、待卸下的包袱，人们凭吃亏的感觉就会发动排斥和攻击，甚至不需算清吃了多少亏。", "evidence": ["E042", "E043"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人可以怎么生活不是统治阶级、父母、老师或敌人可以规定的；世界里埋藏了决定所有人行为方向的规则，是这个规则在给你回应（放开苹果苹果就会往下掉；推卸责任、增加人的负担，人就会用轻蔑、攻击来排除你）。", "evidence": ["E044", "E045", "E046"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称世界的奖惩机制已经在告诉你应该怎样过一个有尊严、受尊敬和爱戴的人生；但不要轻忽这个奖惩机制的复杂性，这需要你用尽一生去慢慢理解，即使作者比孩子多活几十年也并未完全明白它的全部要求，时常被它教育。", "evidence": ["E047", "E048"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者承诺会陪着孩子慢慢理解和摸索，并称将来孩子会有自己的领悟启发作者、可以做作者（即其父母）的老师。", "evidence": ["E049"]},
    {"claim_id": "C021", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者报告写作经过：本来写了一半，被知乎吞了，看来是上天不允许他那样回答，所以他换一个方向说。", "evidence": ["E050"]}
   ],
   "argument_steps": [
    "交代写作经过：原答被平台吞掉，换方向重写（P001）。",
    "前提：社会有秩序，最大的秩序是个人自由；侵犯他人合法权利会招致维护该权利者的集体反击并逐级升级（P002）。",
    "断言：因此全世界都要与你为敌是事实而非错觉（P003—P004）。",
    "反驳“少数统治阶级的阴谋”解释，改以社会竞争淘汰力与物竞天择式天意解释（P005—P006）。",
    "以公平/接受与否的排比强调事实不可改变（P007）。",
    "设两条路：世界是否与你为敌不可改（投石入水之喻），要么打败世界（P008—P009）。",
    "给推翻秩序的条件：需大量愿团结、舍生忘死的同志，并举新中国为例（P010—P011）。",
    "给出净收益计算：团结失败须由更大群体的团结成功抵偿，否则净失败，故应走向更广泛的团结（P012）。",
    "指出对方实际行为是抱怨哭诉，判定其至少低效、只制造已努力的幻觉（P013—P016）。",
    "限定：生气无妨、成年后无人评判想法；问题在能否做到与是否想透（P017—P019）。",
    "转折与自我归责：先要怪自己长期以直接满足愿望贿赂孩子的欲望（P020—P025）。",
    "划定责任分界：今日之前你无责任，今日起各自停止行贿与受贿（P026—P028）。",
    "追问是否做过成本计算，并让步：若没做过你可以怪我；再反问是否认定全怪作者（P029—P035）。",
    "以时刻标记完成仪式：在可以推卸全部责任时选择承担，故授予直呼其名之权（P036—P041）。",
    "提出尊严论：尊严根基在于可选择不担当时仍选择担当，推卸者失去尊严、被人本能排斥（P042—P046）。",
    "要求回答打算怎么做（P047—P048）。",
    "收束于世界规则与奖惩机制：规则在回应你，强调其复杂性并承诺陪伴（P049—P056）。"
   ],
   "concept_usage": [
    {"term": "个人自由", "meaning": "作者称其为社会秩序中“最大的秩序”，是被侵犯即会招致集体反击的对象", "evidence": "P002", "ambiguity": "作者未界定自由的边界与“合法权利”的判定标准"},
    {"term": "物竞天择的天意", "meaning": "作者把现存社会秩序解释为通过物竞天择路径展露的天意，类比万有引力", "evidence": "P006", "ambiguity": "“天意”是否含目的性，作者未说明"},
    {"term": "团结／同志", "meaning": "对抗世界或推翻秩序所需的条件；团结失败须由更大群体的团结成功作有效抵偿", "evidence": "P011", "ambiguity": "“大的多的群体”“有效抵偿”的量化标准未给"},
    {"term": "行贿／受贿", "meaning": "作者对亲子间“直接满足愿望”关系的隐喻：父母以代偿缓解自身痛苦为行贿，子女接受为受贿", "evidence": "P028", "ambiguity": "以经济犯罪词喻亲子关系，作者未说明其适用范围"},
    {"term": "计算", "meaning": "作者指在采取“发脾气”等反应前对得失与可承受损失的折算", "evidence": "P031", "ambiguity": "计算的具体项目与折算方式未说明"},
    {"term": "尊严", "meaning": "他人对你价值的本能敬畏；其根基是“在可以不担当的时候，能明智的选择担当”", "evidence": "P042", "ambiguity": "尊严既被说成他人本能反应，又被说成可由自己选择获得，二者关系未说明"},
    {"term": "世界的奖惩机制", "meaning": "作者称埋藏于世界、决定所有人行为方向的规则，会依据行为给出回应（推卸责任即遭轻蔑攻击）", "evidence": "P050", "ambiguity": "机制的构成与“复杂性”所指未说明"}
   ],
   "examples_and_targets": [
    "同寝室同学与宿管：提问所述冲突对象，作者用作“团结失败”的一方（P012）",
    "“少数统治阶级的阴谋”：作者转述并否认的解释框架，未指明持论者（P005）",
    "万有引力／放开苹果即下落：作者的类比（P006、P050）",
    "丢石入水不能要求水不起波纹：作者的类比（P008）",
    "新中国：作者举以证明推翻旧秩序、重建新秩序并非无人做到的历史事例（P010）",
    "“同志”“舍生忘死”：作者说明推翻秩序条件时使用的革命史语汇（P011）",
    "公元2021年1月3日13点33分：作者自记的仪式性时刻，作为责任分界标记（P037）",
    "“直呼我的名字”“禁止我用你的小名称呼你”：作者设定的权利转移标记（P040）",
    "“待清扫的垃圾、待卸下的包袱”：作者用以描述被排斥者的处境（P045）",
    "知乎：作者称其吞掉原答的平台（P001）"
   ],
   "conditions": [
    "“如果这些人行动起来还是无效，那么还会有更高更多的力量被动员起来”——反击按条件逐级升级（P002）",
    "“要么你打败世界”为二择一设定，且附条件：需要大量愿紧紧团结、舍生忘死的同志（P009、P011）",
    "团结失败须由“大的多的群体”团结成功作有效抵偿，否则即“净失败”（P012）",
    "“你可以怪我”以“你没有做过（计算）”为条件（P032）",
    "“对于未成年的你我负有一切的教育责任”——教育责任以未成年为限（P033）",
    "“等你成年了，也没有人能来跟你说你的什么想法对或者不对”——以成年为界（P017）",
    "责任分界以具体时刻（2021年1月3日13点33分）与“可以合理合法的推卸掉全部责任”为前提（P037、P039）",
    "作者承诺陪伴与理解机制以“你用尽一生去慢慢理解”“将来你会有你的领悟”为预期（P052、P053）"
   ],
   "rhetoric_and_tone": "书信体／对话体，通篇以第二人称对“你”说话，与提问的家长视角错位。先以冷峻的机制陈述配合排比（“你觉得公平也罢……你接受也罢……”）确立事实不可争；继以万有引力、投石入水等比喻把社会秩序自然化。中段急转为自我归责（“这不全怪你，这先要怪我”），并用“行贿／受贿”“两个软弱的人私相贿赂”“出卖了一个本来可以伟大的灵魂”等强烈隐喻；多处反问与追问（“你在做的是什么呢？”“你怎么可能不遍体鳞伤？”“你要选择认定这全是我的责任吗？”）。末段以仪式化时刻标记、授予直呼名字的权利以及“去做你刚才决定要做的”收束，语气由训诫转为郑重与期许。",
   "unresolved_questions": [
    "提问者是家长，正文却改换方向、直接对“你”（子女）说话，未给家长可执行的处理办法；“你”是否即提问者的孩子、是否指作者本人子女，正文未说明。",
    "P010 以“不然哪来的新中国呢”作为推翻旧秩序、重建新秩序的例子，属作者的历史叙述，需外部核查（含史观问题），本文未展开。",
    "P005 的“少数统治阶级的阴谋”未指明是谁的主张或出处，仅能确定为被作者否认的立场。",
    "P037 的具体时刻（2021年1月3日13点33分）及“你选择了自己承担起一部分责任”是否确有对应事件，无法由正文核验。",
    "P024 称“我会在我的遗产里面对这一点负起我应有的责任”，“遗产”所指（遗嘱、财产或其他）未说明。",
    "P001 称原答被知乎吞掉，平台删除原因与原文内容均未说明（版本／平台事项）。",
    "元数据 updated_at（2021-05-16）晚于 published_at（2021-01-03），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "社会是有秩序的，其中最大的秩序就是个人自由。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "你侵犯了别人的合法权利，那么所有对维护这个合法权利有责任的人就不得不行动起来与你为敌。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P002", "quote": "如果这些人行动起来还是无效，那么还会有更高更多的力量被动员起来与你为敌。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "从这个意义上说，的确是全世界都要与你为敌。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P004", "quote": "这不是你觉得如此而已，事实就是如此。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "只是这并不是“少数统治阶级的阴谋”", "relation": "contradicts"},
    {"key": "E007", "paragraph_id": "P005", "quote": "而是因为不遵守这个逻辑的社会在现代化的竞争里会毫无战斗力，会被别的社会形态吞没、统治和同化", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P006", "quote": "这是通过物竞天择的路径展露的天意，和万有引力把所有苹果都拉着往下掉没有本质的区别。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P007", "quote": "你觉得公平也罢，觉得不公平也罢，事实就是如此。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P008", "quote": "它会不会与你为敌这个部分你是改变不了的。", "relation": "qualifies"},
    {"key": "E011", "paragraph_id": "P008", "quote": "你丢块石头到水里，你不能要求水不起波纹。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P009", "quote": "要么你打败世界。", "relation": "context"},
    {"key": "E013", "paragraph_id": "P010", "quote": "不能接受现有秩序，将它推翻，重建一个新秩序，这不是没有人做到过——不然哪来的新中国呢。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P011", "quote": "但是那需要同志，大量的愿意紧紧团结、舍生忘死的同志。", "relation": "qualifies"},
    {"key": "E015", "paragraph_id": "P012", "quote": "对同寝室同学和宿管的团结失败至少需要有一个大的多的群体与你团结成功作为有效的抵偿", "relation": "qualifies"},
    {"key": "E016", "paragraph_id": "P012", "quote": "你接下去的行为应该走向更有效、更广泛的团结。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P013", "quote": "你在做的是什么呢？你在向我抱怨，哭诉你的不满。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P014", "quote": "我本来就是站在你这边的，不用你哭诉，我的立场也不会有改变。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P015", "quote": "这就算不是无效的，至少也是低效的努力。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P016", "quote": "它唯一的净效果，只是给你造成你已经做了足够努力的幻觉，让你比较容易接受随之而来的失败而已。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P017", "quote": "你生气，没什么问题，等你成年了，也没有人能来跟你说你的什么想法对或者不对。", "relation": "qualifies"},
    {"key": "E022", "paragraph_id": "P018", "quote": "所有的问题都在于你能不能做得到，是不是打算承受你自己愿望的全部重量，是不是把整个事情想透彻了。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P020", "quote": "这不全怪你，这先要怪我。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P021", "quote": "是我在你成长的过程中没有让你清楚的明白这个世界的游戏规则，让你误以为只要对我许愿，我就能帮你实现。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P021", "quote": "为了最快的缓解我自己的痛苦，我常常直接帮你实现你的愿望和需求。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P022", "quote": "这对我有好处，但却是以牺牲了你学习努力处理自己的不满足的机会为代价。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P023", "quote": "我为了我的脆弱，而牺牲了你的成长，我只是贿赂了你的欲望，让你成了我的同谋而已。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P025", "quote": "终究是两个软弱的人私相贿赂，出卖了一个本来可以伟大的灵魂。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P026", "quote": "所以今天之前的你是没有责任的。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P027", "quote": "从今天起，你要负起看守你自己灵魂的责任。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P028", "quote": "我要负责停止行贿，你要负责停止受贿。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P031", "quote": "你选择“发脾气”这个反应之前，做过这个计算没有？", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P032", "quote": "如果你没有做过，那么你可以怪我。", "relation": "qualifies"},
    {"key": "E034", "paragraph_id": "P033", "quote": "这的确可以理解为是我没有给你足够的教导，让你没有学会让理智凌驾于情绪。", "relation": "qualifies"},
    {"key": "E035", "paragraph_id": "P034", "quote": "你如果选择怪我，我没有任何自我辩护的余地，必须接受。", "relation": "qualifies"},
    {"key": "E036", "paragraph_id": "P035", "quote": "那么，你要选择认定这全是我的责任吗？", "relation": "supports"},
    {"key": "E037", "paragraph_id": "P039", "quote": "你在这个时刻，在可以合理合法的推卸掉全部责任的时候，选择了自己承担起一部分责任。", "relation": "supports"},
    {"key": "E038", "paragraph_id": "P040", "quote": "从这一刻开始，你有权利直呼我的名字了，你也可以在任何时候禁止我用你的小名称呼你。", "relation": "supports"},
    {"key": "E039", "paragraph_id": "P042", "quote": "在可以不承担的时候，决定承担起自己选择的责任，这就是一个人尊严的根基。", "relation": "supports"},
    {"key": "E040", "paragraph_id": "P043", "quote": "在该担当的时候，想办法推卸责任，或者呼叫出父母买单的人，则会失去尊严。", "relation": "supports"},
    {"key": "E041", "paragraph_id": "P044", "quote": "尊严是什么？是他人对你价值的本能敬畏。", "relation": "supports"},
    {"key": "E042", "paragraph_id": "P045", "quote": "人们凭着本能的反应就会加以排斥和攻击，ta们甚至不需要清楚的算清楚到底吃了多少亏，仅仅凭着吃亏的感觉就已经要发动攻击了。", "relation": "supports"},
    {"key": "E043", "paragraph_id": "P046", "quote": "你怎么可能不遍体鳞伤？", "relation": "supports"},
    {"key": "E044", "paragraph_id": "P049", "quote": "你记住，人可以怎么生活，其实不是什么统治阶级、或者父母、或者老师、或者敌人可以规定的。", "relation": "supports"},
    {"key": "E045", "paragraph_id": "P050", "quote": "世界里埋藏了决定所有人行为方向的规则，是这个规则在给你回应，你放开苹果，苹果就会往下掉。", "relation": "supports"},
    {"key": "E046", "paragraph_id": "P050", "quote": "你推卸责任，增加人的负担，人就会用轻蔑、攻击来排除你。", "relation": "supports"},
    {"key": "E047", "paragraph_id": "P051", "quote": "世界的奖惩机制其实已经在对你说话，它其实已经告诉了你应该怎样过一个有尊严、受尊敬和爱戴的人生。", "relation": "supports"},
    {"key": "E048", "paragraph_id": "P052", "quote": "即使身为你的父母，比你多活几十年，我也并没有完全明白它的全部要求，时常被它教育。", "relation": "qualifies"},
    {"key": "E049", "paragraph_id": "P053", "quote": "我会陪着你慢慢去理解和摸索，而且将来你会有你的领悟会启发我，可以做我的老师。", "relation": "supports"},
    {"key": "E050", "paragraph_id": "P001", "quote": "本来写了一半了，被知乎吞了。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭教育与亲子关系", "社会秩序与规则", "责任与尊严"],
   "issue_candidates": ["孩子违规后对批评过度敏感", "抱怨与发脾气的有效性", "父母代偿与责任转移", "尊严的构成", "以团结对抗秩序的可能性"],
   "text_function_candidates": ["答疑", "书信体训诫", "自我检讨", "评论"],
   "object_candidates": ["提问的家长", "子女（“你”）", "同寝室同学", "宿管", "知乎", "新中国", "统治阶级"],
   "working_keywords": ["与世界为敌", "个人自由", "物竞天择", "天意", "团结", "同志", "行贿", "受贿", "计算", "尊严", "奖惩机制", "直呼我的名字"]
  },
  "notes": "本篇无图片节点，正文完整可读（57 段）。Q001 属提问者（家长）；作者未按家长视角作答，而是换方向、以书信体直接对“你”（子女）说话（P001 说明原答被平台删除），提问者与收信人不同，已在 question_context 与未决问题中登记。P005“少数统治阶级的阴谋”系被否认的立场，已单列为 opponent_view，未归为作者主张。P010“新中国”、P037 具体时刻、P024“遗产”等属作者叙述或承诺，需外部核查或正文无法核验。"
 },
 "4f088894": {
  "analysis": {
   "question_context": "提问者（子女一方）问妈妈总是不敲门就推开自己的房间门、该怎么办（Q001，属提问者）。作者没有回答如何阻止妈妈，而是转向对“父母们”喊话，论证父母为什么应该尊重子女的隐私：隐私权既是父母从养育责任中解脱的出口，也是生命“舵轮”指挥权渐进移交的机制；成年之前隐私不是理所当然的权利，而是掌握在父母手里、必须由父母授予的特权，子女须经一系列“魔法问题”式试炼一点点赢得（earn）它；父母作为考官与子女站在同一边，判负标准是父母未在法定期限前完成移交。P045 直接引用了另一篇答问的提问原文作为“魔法问题”的示例。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "向父母发问：到底为什么应该尊重子女的隐私，想通了吗；不要只想到不知情造成的恐惧、把一切隐私看成洪水猛兽；ta的隐私权也是父母的炼狱出口，因为ta不让你们知道的，ta也没想过让你们负责。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "理由：一切没让父母知道的都是子女主动隔离的，父母当然不必负责；父母会死、不可能负一辈子责，有些责想负也负不起，因此必须在某个点上从这些责任里解脱出来。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014"], "summary": "反问是否要让这一转变在某天像关掉电灯一样突然停止，并摹写“啪嗒，好了，我们撤了啊”的场景；指出一般人的做法是死死捏住舵轮，直到子女上大学或外出打工时被客观现实踢出舷窗外，目送毫无掌舵经验的子女开船消失在天际线上。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017"], "summary": "提出更理想的做法：稳定、受控、渐进、可逆地在练习中转移指挥权，而这一移交过程的关键就在于隐私权的授予。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019"], "summary": "提出隐私权的性质：子女需经一系列精心设计的试炼一点一点赢得（earn）隐私权；成年之前它不是理所当然的权利，而是掌握在父母手里、必须由父母授予的特权。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "以“欲得自由，必承其重”说明授予的条件；作者以父母第一人称自陈：能放心卸下的是有信心子女能理解其代价、可承受或愿意帮其分担的部分，因而乐意让其自由隐瞒；作者也不希望永远看守、已精疲力尽，希望放心地不知道，故在授予隐私权上是子女的盟友、早已迫不及待的共犯，只要可以就会给，因为这对作者不是收益而是折磨和损失。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030"], "summary": "提出“魔法问题”：作者无比希望子女答对一些魔法问题，但既不能告知是哪些问题、也不能告知答对会获得什么礼物，因为一旦告知就失去了构建信念的魔力。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036"], "summary": "列出试炼内容：可以推卸责任时不推卸、可以享受时不享受、父母觉得会屈服时不屈服、父母觉得会放弃时不放弃、在父母想不到办法处超出预料想到办法；任一点上让父母暗忖自己也没能力做出更公义、更勇敢、更智慧的选择，那一部分信息即成为子女的隐私新边界。", "role": "definition"},
    {"unit_id": "U009", "paragraph_refs": ["P037", "P038"], "summary": "断言这是非常困难的目标，但也是唯一能让父母心悦诚服地在法定期限到来之前移交最高决定权而不觉得自己失职的办法，并强调“唯一办法”。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P039", "P040", "P041", "P042"], "summary": "提示父母作为考官站在子女同一边；未给足机会、ta没考过足够科目、放水帮ta作弊过关，三种情形都算父母输了。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048"], "summary": "行动要求：去寻找那些魔法问题、越多越好，不动声色毫无暗示地让ta一次次尝试，并举一个示例（引用另一问的提问原文）；ta没考过属父母教育责任的一部分，应把道理讲更深、示范做更确切、案例让ta看更真，ta什么时候考过父母什么时候解脱。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P049", "P050", "P051"], "summary": "结论：死抓住子女隐私权不放、好去向别人证明自己是“负责任的父母”，是损害ta的利益以有利于自己，没有理由被称为“爱”；世界上最受诅咒的事并不是恶，而是窃取爱的名。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者向父母发问：到底为什么你们应该尊重子女的隐私，你们想通了吗；并称不要只想到不知情对你们造成的恐惧，于是把一切隐私都看成洪水猛兽。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称ta的隐私权也是父母的“炼狱出口”，因为ta不让你们知道的，ta也没想过让你们负责。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称一切ta没有让你们知道的，都是ta主动对你们隔离的，你们根本不知道而且是ta亲手安排的，所以当然不必负责。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称父母会死、不可能为子女负一辈子责，何况有些责想负也负不起，因此必须在某个点上从这些责任里解脱出来。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问父母是否打算让这一转变在某一天像关掉电灯一样突然停止，并摹写“啪嗒，好了，我们撤了啊，祝你好运”作为反例场景。", "evidence": ["E009", "E010"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者描述一般人的做法：死死把舵轮捏在自己手里，直到子女上大学或去外地打工时被客观现实一脚踢出舷窗外，然后目送没有任何掌舵经验的子女开着帆船消失在天际线上。", "evidence": ["E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称更理想的做法是稳定的、受控的、渐进的、可逆的在练习中转移指挥权，而这个移交过程的关键就在于隐私权的授予。", "evidence": ["E012", "E013"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称子女需要经过一系列精心设计的试炼、一点一点赢得（earn）隐私权；这在ta成年之前并不是一项理所当然的权利，而是一项掌握在父母手里、必须由父母授予的特权。", "evidence": ["E014", "E015"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“欲得自由，必承其重”为前提，称他能放心让子女从肩头卸下的是他有信心子女能理解其代价、相信其可承受或愿意帮其分担因而可承受的部分，于是也是他乐意让子女自由对他隐瞒的部分。", "evidence": ["E016", "E017"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以父母第一人称自陈：不希望永远夜不能寐地看守子女，此时此刻已精疲力尽，也希望可以放心的不知道；在“授予你隐私权”方面他绝对是子女的盟友、一个早已迫不及待的共犯，只要可以就会给，因为这对作者不是收益而是无尽的折磨和损失。", "evidence": ["E018", "E019", "E020", "E021"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者提出授予的唯一条件：我唯一的要求，是我放下它不会更让我恐惧和疯狂。", "evidence": ["E022"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称无比希望子女答对一些“魔法问题”，但既不能告诉是哪些问题，也不能告诉答对了会获得什么样的礼物，因为一旦告诉就失去了构建他对子女信念的魔力。", "evidence": ["E023", "E024", "E025"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列出试炼内容：在可以推卸责任的时候不推卸、在可以享受的时候不享受、在父母觉得会屈服的时候不屈服、在父母觉得会放弃的时候不放弃、在父母觉得其想不到办法的地方超出预料想到办法。", "evidence": ["E026", "E027", "E028"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称子女在任何一点上让父母暗忖自己也没能力做出更公义、更勇敢、更智慧的选择，父母在那一点上继续用判断压倒子女的判断就是毫无意义的双输，那一部分信息即可视为子女的隐私新边界。", "evidence": ["E029", "E030"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是非常困难的目标，但这是唯一能让父母心悦诚服地将最高决定权在法定期限到来之前移交子女而不觉得自己失职的办法，并强调“唯一办法”。", "evidence": ["E031", "E032"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称父母作为考官是站在子女同一边的；法定期限到来前没给过ta足够机会、ta没考过足够科目、父母放水帮ta作弊过关，三种情形都算父母输了。", "evidence": ["E033", "E034", "E035", "E036"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求父母去寻找那些“魔法问题”、越多越好，不动声色、毫无暗示地让子女一次次尝试；并称ta没考过是父母教育责任的一部分，应把道理再讲深一点、示范再做确切一点、案例让ta再看真一点，ta什么时候考过，父母什么时候解脱。", "evidence": ["E037", "E038", "E039", "E040"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称死抓住子女的隐私权不放、好去向别人证明自己是一个“负责任的父母”，这是损害ta的利益以有利于自己，没有理由被称为“爱”。", "evidence": ["E041", "E042"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称世界上最受诅咒的事并不是恶，而是窃取爱的名。", "evidence": ["E043"]},
    {"claim_id": "C020", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "作者把另一篇答问的提问原文直接引为本篇所谓“魔法问题”的示例（孩子住校深夜打游戏影响别人、对舍管批评过度敏感、觉得全世界与他作对，家长该怎么办）——该句为被引用的提问者说法，非作者主张，作者未在此处作答。", "evidence": ["E044"]}
   ],
   "argument_steps": [
    "以反问向父母立题：为什么应该尊重子女的隐私（P001）。",
    "排除误解：不要只因不知情的恐惧就把隐私当洪水猛兽（P002）。",
    "提出理由：隐私权是父母的“炼狱出口”，子女不让知道的即未打算让父母负责（P003—P004）。",
    "展开：子女主动隔离的信息父母不必负责（P006）。",
    "加重前提：父母会死、负不了一辈子责，必须在某点解脱（P007—P008）。",
    "反问并讽刺突然交接的场景（“啪嗒，好了，我们撤了啊”）（P009—P011）。",
    "描述一般人的失败做法：捏住舵轮直到被现实踢出舷窗外（P012—P014）。",
    "给出更优做法：稳定、受控、渐进、可逆地转移指挥权（P015）。",
    "点出移交关键即隐私权的授予（P016—P017）。",
    "定义隐私权的性质：须经试炼赢得，成年之前是由父母授予的特权（P018—P019）。",
    "以“欲得自由，必承其重”说明授予条件，并以父母第一人称自陈疲惫与共犯立场（P020—P028）。",
    "引入“魔法问题”：不可告知内容与礼物，否则失去魔力（P029—P030）。",
    "列出试炼清单并给出隐私新边界的判据（P031—P036）。",
    "强调这是唯一办法（P037—P038）。",
    "设定考官立场与三种判负情形（P039—P042）。",
    "行动要求：主动寻找魔法问题并反复试炼，未考过属父母责任（P043—P048）。",
    "结论：抓权不放是以损害子女利益来利己，不能称为“爱”，并以“窃取爱的名”收束（P049—P051）。"
   ],
   "concept_usage": [
    {"term": "隐私权", "meaning": "成年之前不是理所当然的权利，而是由父母掌握、须经试炼逐点授予的特权；其边界随子女在具体事项上展现的判断力而扩张", "evidence": "P019", "ambiguity": "作者未说明试炼通过与否由谁判定、能否申诉或复核"},
    {"term": "炼狱出口", "meaning": "作者对隐私权的比喻：子女不让父母知道的事，父母即不必负责，故隐私权使父母得以从责任中解脱", "evidence": "P003", "ambiguity": "与后文“隐私权是特权”的定位关系，作者未说明"},
    {"term": "生命舵轮的交接", "meaning": "父母把最高决定权逐步移交子女的过程，关键在隐私权的授予", "evidence": "P012", "ambiguity": "“指挥权”“最高决定权”的范围与法定成年后仍存多少影响，未说明"},
    {"term": "魔法问题", "meaning": "作者设计的、用于试炼子女的隐藏考题；不可告知子女是哪些问题及其礼物", "evidence": "P029", "ambiguity": "具体内容、评分方式与“礼物”均未说明，作者明言不告知"},
    {"term": "earn（赢得）", "meaning": "作者用英文标注隐私权的取得方式：一点一点赢得，而非天然享有", "evidence": "P018", "ambiguity": "“赢得”的标准由父母单方掌握，作者未给客观判据"},
    {"term": "考官", "meaning": "父母在试炼中的角色，且作者强调考官站在子女同一边", "evidence": "P039", "ambiguity": "考官与子女同边却握有评分权，二者张力未说明"},
    {"term": "窃取爱的名", "meaning": "作者对以“爱”为名损害子女利益（如死抓隐私权以自证负责）的定性", "evidence": "P051", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "妈妈不敲门推门：提问者所述情境（Q001，属提问者），作者未直接回应（未见于正文段落）",
    "“啪嗒，好了，我们撤了啊，祝你好运。”：作者摹写的突然交接场景（P010）",
    "“还比个✌️——这样吗？”：作者带表情符号的反讽（P011）",
    "子女出门上大学／去外地打工被客观现实一脚踢出舷窗外：作者举的常见交接时点（P013）",
    "小帆船消失在天际线：作者比喻（P013）",
    "“一个早已迫不及待的共犯”：作者自我定位的比喻（P025）",
    "“魔法问题”与“礼物”：作者设定的试炼机制（P029—P030）",
    "被引用的另一问提问原文（孩子住校深夜打游戏影响别人……家长该怎么办？）：作者引为魔法问题示例（P045）",
    "“负责任的父母”：作者批评的自我证明动机（P049）"
   ],
   "conditions": [
    "隐私权“在ta成年之前”不是理所当然的权利，而是须由父母授予的特权（P019）",
    "移交以“法定期限到来之前”为时限（P037、P040）",
    "授予以父母能承受为条件：“只要可以，我就会给你”（P026）",
    "“我唯一的要求，是我放下它不会更让我恐惧和疯狂”——授予的限制条件（P027）",
    "“因为一旦告诉了你，它们就失去了构建我对你的信念的魔力”——魔法问题不可告知的条件（P030）",
    "“你在任何一点上让我暗忖我也没能力做出比你更公义、更勇敢、更智慧的选择”——隐私新边界的成立条件（P036）",
    "判负三情形：没给足机会、ta没考过足够科目、放水帮ta作弊过关（P040—P042）",
    "“ta什么时候考过，你什么时候解脱”——解脱以子女通过试炼为条件（P048）",
    "全篇以“你们会死”“负不了一辈子责”为前提推演父母的解脱必要（P007）",
    "作者以父母第一人称自述（“即使此时此刻，我也已经精疲力尽”），条件依赖其自身处境与感受（P023）"
   ],
   "rhetoric_and_tone": "通篇以“父母们”“你们”为称呼对象，与提问者（子女）错位，作者未回答提问者的实际问题。密集使用反问（“你们想通了吗？”“你们真的想这样吗？”“还比个✌️——这样吗？”“这有什么理由被称为‘爱’呢？”）与比喻（“炼狱出口”“生命舵轮”“像关掉电灯一样”“开着这艘小帆船消失在天际线上”“一个早已迫不及待的共犯”）。后半以“魔法问题—考官—考过—放水帮ta作弊”构成贯穿的考试隐喻，并给出清单式排比（“在可以……的时候不……”）。结尾转为格言式断言（“世界上最受诅咒的事并不是恶，而是窃取爱的名”）。语气兼有训诫、反讽与让步式的自我暴露（自陈精疲力尽、也想放心地不知道）。",
   "unresolved_questions": [
    "提问者（子女）问的是妈妈不敲门推门该怎么办，作者全文向父母喊话，未给子女任何可执行的应对办法；回应与提问的错位需研究者判定。",
    "P045 直接引用了另一篇答问的提问原文（孩子住校晚上打游戏到深夜影响别人……家长该怎么办？），该段为 lexical 未覆盖片段（本篇 divergence=true）；作者未说明该示例与本篇的关系，也未给出该示例的答案。",
    "“魔法问题”具体是哪些问题、由谁设计、如何判定通过，作者明言不能告知；“礼物”内容亦未说明。",
    "“法定期限”所指（成年、法定成年年龄或其他）正文未明确。",
    "“炼狱出口”“生命舵轮”“共犯”“窃取爱的名”等隐喻的边界与所指，作者未定义。",
    "作者以父母第一人称写作，但其与收信子女、与提问者的关系均未在正文中说明。",
    "P011 含表情符号（“还比个✌️——这样吗？”），字形与编码需核验，可能影响逐字引用。",
    "元数据 updated_at（2026-05-20）晚于 published_at（2021-01-03），版本差异内容本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "父母们，到底为什么你们应该尊重子女的隐私，你们想通了吗？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "你们不要光想到不知情对你们造成的恐惧，于是把一切隐私都看成洪水猛兽。", "relation": "qualifies"},
    {"key": "E003", "paragraph_id": "P003", "quote": "你们还要仔仔细细的看清楚——ta的隐私权，也是你们的炼狱出口。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "因为ta不让你们知道的，ta也没想过让你们负责。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "一切ta没有让你们知道的，都是ta真的、真的不会责怪你们的，因为那是ta主动对你们隔离的。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "你们根本都不知道，而且是ta亲手安排的，你们当然不必负责。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "你们是会死的，你们是不可能为ta负一辈子责的。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "因此，你们必须在某个点上，从这些责任里解脱出来。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "你们打算让这个转变在某一天像关掉电灯一样停止吗？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "“啪嗒，好了，我们撤了啊，祝你好运。”", "relation": "context"},
    {"key": "E011", "paragraph_id": "P013", "quote": "死死捏在自己手里，直到有一天，子女出门上大学了，或者去外地打工了，被客观现实一脚踢出舷窗外", "relation": "contradicts"},
    {"key": "E012", "paragraph_id": "P015", "quote": "稳定的、受控的、渐进的、可逆的在练习中转移这项至关重要的指挥权，是更理想的做法。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P017", "quote": "这个移交过程的关键就在于隐私权的授予。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P018", "quote": "ta需要经过一系列精心设计的试炼，一点一点的赢得（earn）ta的隐私权。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P019", "quote": "这在ta成年之前并不是一项理所当然的权利，而是一项掌握在你手里、必须由你授予的特权。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P020", "quote": "欲得自由，必承其重。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P021", "quote": "我能放心让你从我肩头卸下的，是我有信心你能理解其代价的、我相信你可以承受或我愿意帮你分担使得你可以承受的", "relation": "qualifies"},
    {"key": "E018", "paragraph_id": "P023", "quote": "我一点也不希望永远夜不能寐的看守你，说实话，即使是此时此刻，我也已经精疲力尽。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P024", "quote": "我也希望可以放心的不知道。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P025", "quote": "所以在“授予你隐私权”方面，请你相信我绝对是你的盟友，一个早已迫不及待的共犯。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P026", "quote": "因为它对我并不是收益，而是无尽的折磨和损失。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P027", "quote": "我唯一的要求，是我放下它不会更让我恐惧和疯狂。", "relation": "qualifies"},
    {"key": "E023", "paragraph_id": "P029", "quote": "所以，我无比希望你答对一些“魔法问题”。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P030", "quote": "我既不能告诉你是哪些问题，也不能告诉你答对了会获得什么样的礼物。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P030", "quote": "因为一旦告诉了你，它们就失去了构建我对你的信念的魔力。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P031", "quote": "你要在可以推卸责任的时候不推卸、", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P033", "quote": "在我觉得我会屈服的时候不屈服、", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P035", "quote": "在我觉得你这个年纪大概想不到办法的地方，超出我预料的想到办法。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P036", "quote": "我在那一点上继续用我的判断来压倒你的判断就是一种毫无意义的双输", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P036", "quote": "那一部分信息你就可以视为自己的隐私新边界。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P037", "quote": "但这是唯一能让我心悦诚服的将最高决定权在法定期限到来之前移交给你而不觉得自己失职的办法。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P038", "quote": "看清楚，唯一办法。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P039", "quote": "作为考官，你们是站在子女同一边的。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P040", "quote": "ta在法定期限到来之前，你们没给过ta足够的机会，你们就输了。", "relation": "qualifies"},
    {"key": "E035", "paragraph_id": "P041", "quote": "ta没考过足够的科目，你们也输了。", "relation": "qualifies"},
    {"key": "E036", "paragraph_id": "P042", "quote": "你们放水帮ta作弊过关，你们也输了。", "relation": "qualifies"},
    {"key": "E037", "paragraph_id": "P043", "quote": "你们要去寻找那些“魔法问题”，越多越好。不动声色、毫无暗示的让ta一次次的尝试。", "relation": "supports"},
    {"key": "E038", "paragraph_id": "P046", "quote": "ta没考过，那是你的教育责任的一部分。", "relation": "supports"},
    {"key": "E039", "paragraph_id": "P047", "quote": "道理再讲深一点，示范再做确切一点，案例让ta再看真一点。", "relation": "supports"},
    {"key": "E040", "paragraph_id": "P048", "quote": "ta什么时候考过，你什么时候解脱。", "relation": "supports"},
    {"key": "E041", "paragraph_id": "P049", "quote": "至于死抓住子女的隐私权不放，好去向别人证明自己是一个“负责任的父母”，这是损害ta的利益以有利于自己。", "relation": "supports"},
    {"key": "E042", "paragraph_id": "P050", "quote": "这有什么理由被称为“爱”呢？", "relation": "supports"},
    {"key": "E043", "paragraph_id": "P051", "quote": "世界上最受诅咒的事并不是恶，而是窃取爱的名。", "relation": "supports"},
    {"key": "E044", "paragraph_id": "P045", "quote": "孩子住校晚上打游戏到深夜影响别人，对舍管指正批评过度敏感，遇此类事觉得全世界和他做对，家长该怎么办？", "relation": "context"},
    {"key": "E045", "paragraph_id": "P011", "quote": "还比个✌️——这样吗？", "relation": "context"},
    {"key": "E046", "paragraph_id": "P014", "quote": "你们真的想这样吗？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭教育与亲子关系", "隐私与权利边界", "责任转移与成长"],
   "issue_candidates": ["父母不敲门进房间", "隐私权在成年前的性质", "父母养育责任的退出机制", "试炼式考核与最高决定权移交"],
   "text_function_candidates": ["答疑", "训诫", "论辩式说理", "经验总结"],
   "object_candidates": ["父母", "子女", "提问者", "考官"],
   "working_keywords": ["隐私权", "炼狱出口", "生命舵轮的交接", "earn", "魔法问题", "考官", "法定期限", "欲得自由，必承其重", "窃取爱的名"]
  },
  "notes": "本篇无图片节点，正文完整可读（51 段）。Q001 属提问者（子女），作者未回答“怎么办”，而是转向对父母喊话，提问者与受话对象错位，已在 question_context 与未决问题登记。本篇 text 与 lexical 存在分歧（divergence=true，P045“⚠lexical未覆盖片段”）：P045 直接引用了另一篇答问的提问原文（与本批 d5d2eb94《与世界为敌》的 Q001 同文），已作为被引用的提问者说法单列（C020，attribution=questioner），未归为作者主张。作者以父母第一人称自述（“我也已经精疲力尽”），其与收信子女及提问者的关系正文未说明。P011 含表情符号，逐字引用需注意编码。元数据 updated_at（2026-05-20）晚于 published_at（2021-01-03），版本差异未说明。"
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
