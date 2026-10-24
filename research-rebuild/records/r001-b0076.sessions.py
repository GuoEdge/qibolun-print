# -*- coding: utf-8 -*-
"""批次 r001-b0076 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0076.sessions.py            # 写 out/r001-b0076.out.jsonl
  python3 records/r001-b0076.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0076"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0076.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "0a47c7bf": {
  "analysis": {
   "question_context": "提问者（Q001）问“怎么反驳精神资本家的自我努力论”，即请求给出反驳“努力—成功”许诺式论调的方法。作者未按提问者的框架提供逐条反驳程序，而是转向“是否需要反驳”这一前提：指出努力本身不以功利结果为条件，关于努力的命题真假与是否要努力无关。提问者的立场不等于作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以反问把问题从“如何反驳”转向“反驳成功之后用什么代替努力”。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "转述一种被作者视为奇怪的论调：努力若不能百分之百保证成功即吃亏、不如不努力；成功后应停止努力。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "指出持此论者面对双重困境（同等努力更痛苦、更不易成功），并称这两个“格外”本身已回答问题：这样理解努力就努不了力。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "正面主张：无论境遇如何人都应坚持不懈地努力，因为这是度过与享受人生的最好方式；关于努力的命题真假与是否要努力无关。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "用吃饭的类比区分“努力”与关于努力的具体承诺：该调整的是被承诺的具体做法，不是努力本身，二者是两个问题。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P007", "P008", "P009"], "summary": "以反问和列举说明学习与努力本身是收益；停止努力者只是“未亡人”，不努力者连玩和享受的水平都低。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P010", "P011"], "summary": "命题式断言：享受本身要努力、努力本身就是享受；并反问“不需要努力”的生活有何可向往。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P012", "P013"], "summary": "行动建议：可以用喜欢的努力替换不喜欢的劳役，但不能用“不必努力”替换并指望变得幸福。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论富贵贫穷、健全残疾、顺境逆境，人都应该坚持不懈地努力；这不是为了糊口或出人头地，而是度过和享受人生的最好方式。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论别人关于努力的命题是真是假，都与自己是否要努力没有关系。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在“努力—许诺”的问题上，应调整的是具体的错误承诺或做法，而不是努力本身；二者是两个不同的问题。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "（被作者转述并反驳的论调）努力如果不能百分之百保证“成功”、不能兑现升职加薪等许诺，就是上当吃亏，不如不努力；一旦成功就应停止努力。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "享受本身就是要努力的，努力本身就是享受。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要妄想用“不必努力”替换不喜欢的劳役就会变得幸福；那样只会变成不知自己去向的活死人。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "停止努力，人就不再是活人。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "P001 反问：反驳成功之后拿什么代替“努力”（把问题从反驳技术转向替代方案）。",
    "P002 转述待反驳论调：努力不保证成功即吃亏；成功后应停止努力。",
    "P003-P004 指出该论调者的双重困境，并称困境本身已回答问题（如此理解努力就努不了力）。",
    "P005 提出正面主张并切断“努力”与“关于努力的命题”的联系。",
    "P006 以吃饭类比说明该调整的是具体承诺，而非努力本身。",
    "P007-P009 以反问与生活例证说明努力本身是收益，停止努力者只是“未亡人”。",
    "P010-P011 命题式断言努力与享受同一，并反问无努力生活的价值。",
    "P012-P013 行动建议与否定式警告：可替换劳役，不可替换为“不必努力”。"
   ],
   "concept_usage": [
    {"term": "努力", "meaning": "指人度过人生、享受人生的方式本身，而非换取成功的工具；其正当性不取决于任何关于努力的命题真假。", "evidence": "P005", "ambiguity": "未区分努力的种类、强度与方向；也未给出区分“努力”与盲目劳役的判据。"},
    {"term": "自我努力论／精神资本家", "meaning": "仅出现在提问字段（Q001），正文未使用这两个词，也未指名具体主张者。", "evidence": "P002", "ambiguity": "正文以“奇怪的论调”指代被反驳对象，归属与出处不明。"},
    {"term": "成功", "meaning": "在转述的论调中指升职加薪、得宝获美等许诺的兑现；作者未正面定义。", "evidence": "P002", "ambiguity": "引号使用表明作者对该词持保留态度。"},
    {"term": "享受", "meaning": "与努力同构的体验，需要努力才能达到；作者称努力本身就是享受。", "evidence": "P010", "ambiguity": "未说明享受与劳役痛苦如何共存。"}
   ],
   "examples_and_targets": [
    "吃饭类比：有人承诺连吃五碗白米饭给一百块而后食言，应调整的是“连吃五碗白米饭”而非“吃饭”（P006，作者类比）。",
    "冲浪、滑翔伞、钓鱼、摩托越野、攀岩、滑雪、潜水、自由搏击、射箭、射击（P009，作者列举，说明玩也需努力）。",
    "语数外、做题、坐办公室、跑业务（P012，作者举例，指可用喜欢的努力替换的劳役）。",
    "反驳对象：提问中所称“精神资本家的自我努力论”，以及P002转述的“努力无百分之百保证即吃亏”“成功后应停止努力”的论调；作者未指明其来源与主张者。"
   ],
   "conditions": [
    "对象范围前提：无论富贵或贫穷、健全或残疾、顺境或逆境（P005）。",
    "成立条件：关于努力的命题真假不影响是否要努力的判断（P005）。",
    "替换条件：只能用自己喜欢的努力替换不喜欢的劳役，不能用“不必努力”替换（P012-P013）。",
    "后果预测：以“不必努力”替换者不会变得幸福（P013，属作者的否定式预测）。"
   ],
   "rhetoric_and_tone": "反问密集（P001、P007、P011），以第二人称“你”直接劝导；用吃饭作日常类比；语气由调侃转为训诫，出现“未亡人”“活死人”“避如蛇蝎”等夸张与贬抑性比喻；全篇为劝导式论辩，未引用任何他人文本。",
   "unresolved_questions": [
    "正文未出现“精神资本家”一词，也未指明“自我努力论”的具体主张者或出处；被反驳对象仅以P002的描述存在，无法核对其原意。",
    "提问者问“怎么反驳”，正文未给出针对该论点的反驳程序，而是主张不必在此层面回应；这是否构成对提问的完整回答，正文未说明。",
    "“努力”与盲目劳役、被剥削的延长劳动之间的界线，正文未给判据（P006、P012 仅以类比区分）。",
    "P009 关于各种玩乐“水平低得令人尴尬”的判断属作者经验断言，需外部核查。",
    "平台字段为知乎问答，正文与brief基本一致（brief为正文截断），未见版本差异说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P005", "quote": "人都应该坚持不懈的努力。这不是为了糊口或者出人头地", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "无论谁跟你说了什么关于努力的命题，也不管这些命题是真是假，都跟你是不是要努力没有关系。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "你应该调整的是“连吃五碗白米饭”，而不是“吃饭”。这其实根本是两个不同的问题。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "似乎努力如果不能百分之百保证“成功”，不能如许诺的那样升职加薪、得宝获美，就上当了", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P010", "quote": "享受本身就是要努力的。努力本身就是享受。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P013", "quote": "不要妄想用“不必努力”来替换它们你会“变得幸福”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "停止努力，人就不再是活人，而只是“未亡人”罢了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生观与伦理", "劳动与工作观念"],
   "issue_candidates": ["努力是否必须以成功为条件", "如何回应“自我努力论”", "努力与享受的关系"],
   "text_function_candidates": ["答疑", "论辩", "劝导"],
   "object_candidates": ["精神资本家（仅见于提问字段，正文未出现）"],
   "working_keywords": ["努力", "自我努力论", "成功", "享受", "未亡人", "活死人"]
  },
  "notes": "本篇无图片节点，正文13段全部读完，正文与brief一致（brief为正文开头截断）。提问者所问的“精神资本家”与被反驳论调的主张者在正文中均未指名，已在unresolved_questions登记；“反驳”对象按opponent_view归属，未归给作者。"
 },
 "40e8c68d": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何培养出得力的下属？”，属管理学/职场操作类提问。作者先否定问题的普遍前提（称对大多数私企只是伪问题），再把“培养”抬到极高的门槛上重新定义，随后转到“得力”的定义问题并给出两个切入口；文末标注未完待续。回答不是操作手册式的步骤清单，而是资格与前提的审查。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "提出“培养下属”只出现在能让人终身投靠的体系（央企国企、政府机构、科研院所、跨国企业），对多数私企是伪问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "限定讨论范围：只谈能使该关系成立的情形，并要求先核实与下属的关系强度，随后给出“硬指标”。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "硬指标一：组织要能管到下属整个职业生涯全周期，对成员生老病死都有说法，否则对方无从放心托付命运。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "硬指标二：要有传承超过一代的东西才有资格谈对他人的培养；否则只能叫传授。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "定义“培养”：远超过“帮带”，是为师为父那样亲近而权威的关系，双方有额外的权柄与服从，否则只是客气话。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "“培养”的真正宾语是传人；对一般的下属只该谈负责任的指挥和公平的奖惩。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "对比培训与培养：培训以利润为本、兼具教育与测试，培养以人为中心、可忍受利润折损，培养者以得到最强组织或最完美传人为“盈利”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024"], "summary": "小结论与劝告：低于门槛者应继续以利润为中心，不要拿这一套去左右信任自己的人的命运。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027"], "summary": "硬指标三：受培养者要有终身之志，须先想清楚人生走向，否则是浪费彼此的感情和生命。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "“快速培养”的秘诀在选材的洞察力：培养者先盘清自己资格，再看对象是否真想走这条路，看其豁得出去、受委屈、扛挫折、人品原则，直到愿意拿被彻底辜负去赌。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P035", "P036"], "summary": "条件双向满足则事半功倍；仅为快速提升生产力而开口谈培养，则可能把一般上下级关系搞砸、人事两空。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P037", "P038", "P039", "P040"], "summary": "转入“得力”的定义：追问是否指好用的私人部下、能否在离位后带对方走；否则培养会变成与对方意愿的精神拔河。", "role": "transition"},
    {"unit_id": "U013", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046"], "summary": "切入口A：主动照顾对方技能的通用性，分清岗位要求与个人要求，并对个人要求提供对等补偿；反向要求改造自己的工作方式以适应主流最佳实践。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P047", "P048", "P049"], "summary": "切入口B：顺应对方个人的理想，可摆脱通用性顾虑，但以对方确有该志向为前提。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054"], "summary": "甄别伪志向，提出最低限度的合格志向是追求人类与自我的双赢；理由是这样的人强大后挟利要价、搞手段的概率较小，避免培养出反噬的野兽。", "role": "qualification"},
    {"unit_id": "U016", "paragraph_refs": ["P055"], "summary": "文末标注“（未完，待续）”。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谈得上“培养下属”的场景一般出在有本事让人终身投靠的体系里；对大多数私企这只是伪问题。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "要成立培养关系，组织至少要有可能、打算或规划管到下属整个职业生涯直到结束的全周期。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要有传承超过一代的东西，才有资格谈对他人的培养；不到“经过检验能让人寄托生命价值”的程度只能叫传授。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "培养是远超“帮带”的关系，是为师为父那样亲近而权威的关系，双方之间必有额外的权柄与服从。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“培养”的真正宾语是传人；对下属只该谈负责任的指挥、公平的奖惩，谈不到“培养”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "培训以利润为本，培养以人为中心，可以忍受利润受到折损。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "培养关系的另一个前提是受培养的人要有终身之志；接受培养涉及人生走向，应先想清楚再请求被培养。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "若条件不满足却为快速提升生产力去谈培养，大概率不只事倍功半，更可能把原本可行的一般上下级关系搞砸。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "切入口之一是主动照顾对方技能的通用性，并分清岗位要求与自己的个人要求；对个人要求须提供对等补偿，否则构成实质的掠夺。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人的志向是伪志向，其真正志向是获得最大的资源尽情享乐，这种“志向”没资格得到额外赞助。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最低限度的合格志向至少是追求人类与自我的双赢，理由是这样的人强大了之后挟利要价、搞手段的概率比较小。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "P001-P004 先否定问题前提：能谈培养的体系有限，私企多为伪问题（上下级由一般劳动力市场招聘、存续期短、上司年轻资浅）。",
    "P005-P007 限定讨论范围并给出核实关系强度的“硬指标”。",
    "P008-P009 指标一：全职业生涯周期的可承诺性与生老病死的说法（例外：和尚庙、修道院类特殊规矩）。",
    "P010-P014 指标二：传承超过一代的东西，才由“传授”升格为“培养”。",
    "P015-P016 定义培养为亲近而权威、带额外权柄与服从的关系，指出“快速培养”是客气话。",
    "P017-P018 澄清培养的宾语是传人而非一般下属，给出对下属的正当关系内容。",
    "P019-P022 以培训/培养对比给出判据：利润为本 vs 以人为本。",
    "P023-P024 劝告低于门槛者以利润为中心，不要误人子弟。",
    "P025-P027 指标三：受培养者须有终身之志。",
    "P028-P034 提出选材洞察力是“快速培养”的秘诀，并给出观察维度与下赌注的标准。",
    "P035-P036 双向条件满足与否的结果对比（事半功倍 vs 人事两空）。",
    "P037-P040 转入“得力”的定义追问（私人部下？能否带走？）。",
    "P041-P046 切入口A：技能通用性与岗位要求/个人要求之分。",
    "P047-P049 切入口B：顺应对方个人理想。",
    "P050-P054 甄别伪志向与设定最低志向门槛，理由是防止反噬。",
    "P055 标注未完待续。"
   ],
   "concept_usage": [
    {"term": "培养", "meaning": "远超“帮带”、为师为父般亲近而权威的关系；以人为中心、以得到更强组织或最完美传人为盈利，可忍受利润折损。", "evidence": "P015", "ambiguity": "与培训、帮带、传授的界线由作者自定，未给可操作判据。"},
    {"term": "培训／岗前培训／技能训练", "meaning": "以利润为本，兼具教育与测试，测试不佳即淘汰，没有大责任与强关心。", "evidence": "P021", "ambiguity": "未说明培训在何种规模或时长下可转化为培养。"},
    {"term": "传人", "meaning": "“培养”的真正宾语；因“有事弟子服其劳”而同时是一般意义上的下属。", "evidence": "P017", "ambiguity": "无。"},
    {"term": "得力", "meaning": "作者未直接定义，而是先追问其含义（是否指私人部下好用、能否被带走）。", "evidence": "P038", "ambiguity": "全篇未给出“得力”的正面定义，正文此处似未写完。"},
    {"term": "通用（技能通用性）", "meaning": "指自己升迁、调遣、退出或对方离职后，技能不发生大的浪费、可适用于同类岗位。", "evidence": "P043", "ambiguity": "“大的浪费”的程度标准未说明。"},
    {"term": "终身之志", "meaning": "受培养者对自己人生走向有清楚选择并愿为此负责，表现为豁得出去、受得起委屈、扛得住挫折。", "evidence": "P025", "ambiguity": "如何验证“真”志向（口头之外的判据）作者只给“一看，再看”。"},
    {"term": "伪志向", "meaning": "真正志向是获得最大资源尽情享乐，产品、成果、服务只是就近操起的吃饭家伙。", "evidence": "P050", "ambiguity": "甄别方式未给。"},
    {"term": "双赢", "meaning": "最低限度合格志向：把人类／非利益相关方的某个人群的利益摆在至少不比本人收益更低的地位上。", "evidence": "P051", "ambiguity": "“非利益相关方”的界定未展开。"}
   ],
   "examples_and_targets": [
    "央企国企、政府机构、科研院所、跨国企业（P002，作者举例，指能谈培养的体系）。",
    "和尚庙、修道院（P009，作者点明的例外情形）。",
    "岗位要求 vs 个人要求（P044，作者的区分工具，并称以后者取代前者须对等补偿，否则是实质的掠夺）。",
    "产品开发者（P048，作者举例说明顺应个人理想）。",
    "“长壮了就从身边咬起的野兽”（P053，作者比喻，指被培养者的反噬风险）。",
    "被质疑/被反驳对象：把“培养下属”当作可普遍操作的管理技术、追求“快速培养”提升生产力的做法（P016、P028、P036）。"
   ],
   "conditions": [
    "讨论前提：只谈能使得培养关系成立的情形（P005）。",
    "组织条件：能管到整个职业生涯直到结束的全周期，至少要有这种可能性、打算或规划（P008）。",
    "组织须对成员的生老病死都有说法，且不能存在“你若这样我们就会解除关系”式条款；例外为和尚庙、修道院这类有特殊规矩的（P009）。",
    "资格条件：要有传承超过一代的东西，且经检验确能让人寄托生命价值（P011、P014）。",
    "对象条件：受培养者有终身之志、人品与做人的原则（P025、P031、P032）。",
    "风险意愿条件：培养者要看一看再看，直到愿意拿被彻底辜负去赌，才可一试（P033、P034）。",
    "通用性策略条件：除非对方不打算做这种职位，否则无法通过换老板、换企业回避必要的学习（P046）。",
    "志向门槛条件：最低限度合格志向为追求人类与自我的双赢（P051）。",
    "场景限制：一般的私企、规模很大的新生企业往往不适用（P003）。"
   ],
   "rhetoric_and_tone": "训诫与劝告语气，用编号“1）2）3）”与“A）B）”组织硬指标与切入口；反问式推进（P023“现在你明白为什么这事一定要这么高的门槛了吗？”，P039“那么人家为什么要追求成为你的一个特别好用的私人助理呢？”）；第二人称“你”直呼读者并连续追问（P040）；条件式警告（P024、P036）；比喻性贬抑（P053“长壮了就从身边咬起的野兽”）；文末自标“（未完，待续）”。",
   "unresolved_questions": [
    "正文末尾标注“（未完，待续）”，“得力”的正面定义与是否还有切入口C等未见，本篇为未完成文本。",
    "“培养者资格”的两条硬指标如何具体判定（多长算全周期、什么算传承超过一代）正文未给判据。",
    "选材“洞察力”被作者称为快速培养的秘诀，但除“一看，再看”外未给可操作方法。",
    "P002/P003 关于央企国企、政府机构、科研院所、跨国企业及私企的判断属作者的经验归类，未提供依据，需外部核查。",
    "P043“通用化技能”与P048“顺应个人理想”两条切入口在冲突时如何取舍，正文未说明。",
    "P044“对等的补偿”如何度量，正文未说明；P052 关于持有双赢志向者“搞手段概率比较小”为概率性判断，无数据支撑。",
    "平台字段为知乎问答，更新时间为2025年，正文是否改版、与初版差异如何，正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "谈得上“培养下属”的场景，一般都出在有本事让人终身投靠的体系里面", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "所以这对大多数私企都只是伪问题。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P008", "quote": "你这组织要能管到下属的整个职业生涯直到结束的全周期", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P011", "quote": "你要有传承超过一代的玩意儿，才有资格谈对他人的培养。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P015", "quote": "培养，是一种远超过“帮带”的关系。是为师为父那样亲近而权威的关系。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P017", "quote": "“培养”的真正宾语，其实是传人", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P018", "quote": "你对下属只该谈负责任的指挥、公平的奖惩，是谈不到“培养”的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P021", "quote": "培训的中心是利润，是以利润为本的；培养的中心是人", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P025", "quote": "培养关系的另一个前提，是受培养的人得要有终身之志。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P036", "quote": "那么大概率得到的不仅仅是事倍功半这种扫兴的挫折，更可能把原本可行的一般上下属关系搞砸", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P043", "quote": "所谓通用，是指你升迁、调遣、退出了，对方要服务于同一岗位的继任者时技能不发生大的浪费", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P050", "quote": "很多人的志向是伪志向，他们的真正志向是获得最大的资源尽情享乐", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P052", "quote": "而是因为持有这类志向的人强大了之后挟利要价、上蹿下跳搞手段的概率比较小。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P044", "quote": "敦促对方适应你的个人要求，你就要对对方提供对等的补偿，否则这构成一种实质的掠夺。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P055", "quote": "（未完，待续）", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理与人际关系", "师徒/传承伦理", "职场经验总结"],
   "issue_candidates": ["培养与培训的界线", "培养者资格门槛", "选材与志向甄别", "下属的通用性技能与个人要求"],
   "text_function_candidates": ["答疑", "经验总结", "训诫/劝告", "概念辨析"],
   "object_candidates": ["央企国企", "政府机构", "科研院所", "跨国企业", "私企（作者举例的体系类型）"],
   "working_keywords": ["培养", "培训", "帮带", "传人", "终身之志", "通用性", "伪志向", "双赢"]
  },
  "notes": "本篇无图片节点，55段正文全部读完。文末自标“（未完，待续）”，属未完成文本，已在unresolved_questions登记；其中“得力”的正面定义缺失，未据标题或brief补写。brief与正文一致（为正文截断）。作者以“硬指标”“切入口”组织内容，属经验总结+训诫，非实证研究；其中的体系归类与概率性判断未提供依据。"
 },
 "13015fe8": {
  "analysis": {
   "question_context": "提问者（Q001）问“执着和偏执的区别在哪里？”，属概念辨析类提问。作者先给出适用范围限定（只对有可证伪性的命题成立），再以逐条对照的方式给出两者的判定特征，最后补一条行为层面的限定。全文不涉及具体人物或事件。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "限定适用前提：对没有可证伪性的命题（如“英特纳雄耐尔总有一天会实现”）谈不到固执或偏执，那只是信仰；只有对“产品上市达到销售目标”“设计能实现有效运转”这类可证伪问题才可能有此定性。", "role": "qualification"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "以设问切入两者的区别。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "执着者的特征：知道自己坚持的东西不完美，抱“世界上没有完美的东西，你总要选择一个”的心态；对指出者感情中性，老调重弹会困扰但仍感谢关心，新视角则感谢提示。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "偏执者的特征：不承认也不能承认自己的选择不完美，不能接受别人这样说，对指出者憎恶并实施报复、试图“斩首示众，以儆效尤”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "行为层面的比较与限定：执着不如偏执那样有攻击性；但拉黑、拒绝无意义的对话不算“有攻击性”。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "执着/偏执的定性只对具有可证伪性的命题成立；对没有可证伪性的命题（如“英特纳雄耐尔总有一天会实现”）相信者只是信仰，谈不到固执或偏执。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "执着的人知道自己坚持的东西不完美，是抱着“世界上没有完美的东西，你总要选择一个”的心态坚持。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "执着者对指出其不完美的人感情是中性的：老调重弹会困扰但感谢关心，新视角则感谢提示。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "偏执的人不承认、也不能承认自己选择的答案不完美，不能接受别人说自己的选择不完美。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "偏执者对指出这一点的人是憎恶的，并会实施报复，总是尝试“斩首示众，以儆效尤”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "从行为上说，执着不如偏执那样有攻击性。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "拉黑、拒绝无意义的对话不算“有攻击性”。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "P001 先立适用范围：只有可证伪的命题才谈得上固执/偏执，不可证伪者只是信仰（举“英特纳雄耐尔总有一天会实现”为例）。",
    "P002 设问两者的区别。",
    "P003-P004 给出执着一侧的两个特征：自知不完美 + 对指出者的中性感情（分老调重弹与新视角两种情形）。",
    "P005-P006 给出偏执一侧的两个特征：拒不承认不完美 + 对指出者憎恶并报复。",
    "P007 以行为攻击性作比较式小结。",
    "P008 补一条排除性限定：拉黑与拒绝无意义对话不算攻击性。"
   ],
   "concept_usage": [
    {"term": "可证伪性", "meaning": "判定能否使用固执/偏执定性的前提条件；作者以“英特纳雄耐尔总有一天会实现”为不可证伪示例，以“这种产品上市会达到销售目标”“这种设计能实现有效运转”为可证伪示例。", "evidence": "P001", "ambiguity": "未给出可证伪性的定义或判定标准，仅以例子说明。"},
    {"term": "执着", "meaning": "明知所坚持的东西不完美仍选择坚持，对指出者持中性感情。", "evidence": "P003", "ambiguity": "“执着”是褒义、贬义还是中性，正文未表态。"},
    {"term": "偏执", "meaning": "不承认也不能承认自己的选择不完美，对指出者憎恶并实施报复。", "evidence": "P005", "ambiguity": "是否包含不实施报复但拒不承认的情形，正文未说明。"},
    {"term": "信仰", "meaning": "对没有可证伪性的命题的相信，与固执/偏执分属不同范畴。", "evidence": "P001", "ambiguity": "未说明信仰者若同时坚持可证伪的判断该如何定性。"},
    {"term": "攻击性", "meaning": "以是否对指出者实施报复来衡量；拉黑、拒绝无意义的对话被明确排除。", "evidence": "P007", "ambiguity": "除拉黑与拒绝对话外还有哪些行为不算攻击性，未列举。"}
   ],
   "examples_and_targets": [
    "“英特纳雄耐尔总有一天会实现”（P001，作者举的不可证伪命题示例，属修辞/论据材料，非作者立场）。",
    "“这种产品上市会达到销售目标”“这种设计能实现有效运转”（P001，作者举的可证伪问题示例）。",
    "“世界上没有完美的东西，你总要选择一个”（P003，作者引述的执着者心态）。",
    "“斩首示众，以儆效尤”（P006，作者用以描述偏执者报复行为的成语，带讽刺色彩）。",
    "反驳/澄清对象：把拉黑、拒绝无意义对话当作“有攻击性”的常见理解（P008）。"
   ],
   "conditions": [
    "适用前提：命题必须具有可证伪性，否则不成立（P001）。",
    "场景限定：产品上市销售目标、设计能否有效运转这类可验证问题（P001）。",
    "层面限定：“行为上说”才作攻击性比较（P007）。",
    "排除项：拉黑、拒绝无意义的对话不算有攻击性（P008）。"
   ],
   "rhetoric_and_tone": "冷静的辨析语体，采用执着/偏执逐条对照的结构；以“首先要注意——”“注意——”作提示语，用引号标示被讨论的术语与成语；对偏执者的描述使用“憎恶”“报复”“斩首示众，以儆效尤”等带贬抑色彩且略带讽刺的措辞；全篇无第二人称直呼，未引用他人文本。",
   "unresolved_questions": [
    "“可证伪性”未给定义或判定标准，仅以两个例子说明，边界情形（宗教、政治信念与可验证判断混合）未讨论。",
    "P005-P006 中报复行为的具体所指、范围与程度未说明；“不能承认”是心理状态还是公开表现，正文未区分。",
    "执着与偏执是类别差异还是同一维度的程度差异，正文未明确表态。",
    "作者未区分“指出者”的说法正确与否；若指出错误，偏执者的反应是否另有定性，正文未说明。",
    "更新时间为2025年（晚于发表时间2020年），正文是否有修订、与初版差异如何，正文未说明。",
    "提问者问“区别在哪里”，作者给出特征对比但未给可操作判据（如自我检测或他人判断的方法）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这些对没有可证伪性的命题不成立", "relation": "qualifies"},
    {"key": "E2", "paragraph_id": "P001", "quote": "只有对“这种产品上市会达到销售目标”“这种设计能实现有效运转”这类有可证伪性的问题才可能存在固执/偏执的定性。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "执着的人知道自己坚持的东西不完美", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "ta们对指出这一点的人的感情是中性的", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "偏执的人不承认、也不能承认自己选择的答案不完美", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "ta们对于指出这一点的人是憎恶的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "ta们会对指出这一点的人实施报复，总是尝试“斩首示众，以儆效尤”。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "行为上说，执着不如偏执那样有攻击性。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "拉黑、拒绝无意义的对话不算“有攻击性”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认知与心理", "概念辨析", "人际冲突"],
   "issue_candidates": ["执着与偏执的判定标准", "可证伪性作为适用前提", "对批评者的反应差异"],
   "text_function_candidates": ["答疑", "概念辨析", "评论"],
   "object_candidates": ["英特纳雄耐尔（作为不可证伪命题的例子）"],
   "working_keywords": ["可证伪性", "执着", "偏执", "信仰", "攻击性", "斩首示众"]
  },
  "notes": "本篇无图片节点，8段正文全部读完，正文与brief一致（brief为正文截断）。作者以“可证伪性”限定全篇适用范围，属限性条件，已在conditions与C001中保留。文中“英特纳雄耐尔总有一天会实现”是作者举的不可证伪示例，属举例材料，未当作作者立场。全篇未出现具体人物或事件，也无引用他人文本。"
 },
 "a7027ceb": {
  "analysis": {
   "question_context": "提问者（Q001）问“中国有没有已经垄断世界的技术？”，是要求举出具体技术的事实性提问。作者未逐项列举已垄断的技术，而是给出一个机制性回答：领先技术的根基是独有的需求与足够大的市场，并据此预测中国技术领域的前景。全篇多为作者的机制主张与预测，含少量政策判断的自我限定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "提出总规律：独得之秘的根基来自独有的需求而非天才；在中国有更大应用前景的领域最终一定会诞生中国领先世界的技术，且该技术若在他处找到相似场景就会成为优势技术；此规律对所有技术发展有效。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006"], "summary": "以“火种不如干柴”作比，举大型基建工程与重型装备为例：只有中国有需求，于是只有中国有为研究买单的场景，培育出独有技术和组织。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "以法、日、德铁路技术的反问作反例，并以深渊巨龙、池塘生态位的比喻说明丰富场景孕育出的物种/技术具有对外压倒性。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "结论：技术的关键不是扶持政策，而是市场；中国技术上真正需要解决的是消除不必要的内部垄断（把市场做深）与消除不必要的对外封闭（把市场做大），解决后技术优势会自然发育。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "推论：技术人员会被企业和组织争夺、待遇提高，时间会形成“传承”级护城河；要加快进程需造就比当年资本主义国家更快的开放速度与更大的市场量级。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016"], "summary": "预测特斯拉最终会成为首先专注于中国市场需求的中国企业，迟早有人改籍来中国创建芯片、引擎企业；并以堤防拦不住露珠雨滴作比。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "指出真正的难点是在不安全国际环境下维持国有经济绝对主体性造成的垄断性过高与知识产权障碍过多；判断现有成就是基本平衡态，重要的是平衡点移动方向；预计会进一步降低对外开放门槛，并推测中央也看到把“柴”烘得更干、堆得更高的必要性。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022"], "summary": "预测未来三五年在引入民间资本涉足重大研究项目的制度创新、科教体制创新和知识产权保护实践上会有更大动作，与扩大对外经济合作协调一致；结论是中国技术领域前景相当乐观。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "独得之秘的根基并不来自独特的天才，而是来自独有的需求。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "凡是在中国拥有更大应用前景的领域，最终都一定会诞生中国领先于世界的技术；这更多取决于中国的独特性，而不是人才、资本。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果这种技术在世界上的任何地方找到了相似的应用场景，它就一定会压倒其他技术成为优势技术。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在技术发展的宏观层面，灵感的火种远不如遍地的干柴重要。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术的关键、最根本的要害不是具体的扶持政策，而是市场。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国在技术上真正需要解决的只有两个问题：消除不必要的内部垄断把市场做深；消除不必要的对外封闭把市场做大。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这（独有的需求—市场—技术）其实就是所有“全球垄断的技术”的共同出生路径。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "特斯拉最终会成为首先专注于（如果不是唯一专注于）中国市场需求的中国企业；迟早也会有人改籍来中国创建全新的芯片企业、引擎企业。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "现在真正的难点，是在不安全的国际环境下要维持国有经济的绝对主体性所造成的垄断性过高和对私有经济知识产权的障碍过多。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "negated", "statement": "作者表示不相信中央没有看到除了把“柴”铺得更宽之外，还有把柴烘得更干、堆得更高的必要性。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不出意料，未来三五年在引入民间资本涉足重大研究项目的制度创新、科教体制创新和知识产权保护实践上会有更大的动作。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的技术领域前景相当乐观。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "P001 提出命题：独得之秘来自独有的需求，不是天才。",
    "P002-P003 推出机制：应用前景大→必然产生领先技术；技术若在他处有相似场景→压倒其他技术。",
    "P004 声明规律的普遍性（对所有技术发展有效）。",
    "P005-P006 以“火种不如干柴”为喻，举大型基建、重型装备为例。",
    "P007-P008 以法日德铁路的反问作反例，用深渊巨龙与池塘生态位作类比论证。",
    "P009-P010 归纳为“全球垄断的技术”的共同出生路径，并把要害定为市场而非扶持政策。",
    "P011-P012 给出两个待解决问题的政策结论（做深市场、做大市场）。",
    "P013-P014 推论人才待遇与传承级护城河，提出加快进程需更大开放速度与市场量级。",
    "P015-P016 以特斯拉与改籍创业的预测和堤防比喻强化论证。",
    "P017-P018 承认真正难点（国有经济主体性带来的垄断与知识产权障碍），并提出“平衡态与平衡点移动”的判断框架。",
    "P019-P020 判断政策将先降低对外开放门槛，并推测中央看到内部改善的必要性。",
    "P021-P022 预测未来三五年的制度与体制创新动作，收束为乐观结论。"
   ],
   "concept_usage": [
    {"term": "独得之秘", "meaning": "独有需求所孕育出的领先技术及其组织。", "evidence": "P001", "ambiguity": "未给出判定某项技术是否属于“独得之秘”的标准。"},
    {"term": "独有的需求／市场", "meaning": "技术领先的根本条件；作者把市场列为最根本要害，并区分“做深”（消除内部垄断）与“做大”（消除对外封闭）。", "evidence": "P010", "ambiguity": "“市场”未被量化（规模、份额），“够大”只有P015的“市场够大，份额够多”。"},
    {"term": "干柴／火种", "meaning": "干柴喻需求与应用场景，火种喻灵感；作者主张前者远比后者重要。", "evidence": "P005", "ambiguity": "比喻性用法，未定义转换关系。"},
    {"term": "传承级的护城河", "meaning": "技术与组织经时间沉淀形成的壁垒。", "evidence": "P013", "ambiguity": "“沉淀”的时间尺度未说明。"},
    {"term": "平衡态／平衡点", "meaning": "用以描述中国现状（基本处于平衡态的现状）；作者主张绝对限制程度不重要，重要的是平衡点向哪一边移动。", "evidence": "P018", "ambiguity": "“平衡态”是借用的物理/经济概念，未给出判据。"},
    {"term": "国有经济的绝对主体性", "meaning": "被作者列为造成垄断性过高与知识产权障碍的真正难点所在的政策取向。", "evidence": "P017", "ambiguity": "作者未说明该主体性是否应调整，只谈降低对外门槛与做宽市场。"}
   ],
   "examples_and_targets": [
    "大型基建工程、重型装备（P006，作者例证，称只有中国有为研究买单的场景）。",
    "法国、日本、德国的铁路技术，以及冰原、沙漠、喜马拉雅山、长江、横断山脉、大型铁路网信号系统（P007，作者以连续反问作为反例，属修辞性论据，事实细节待外部核查）。",
    "深渊与巨龙、池塘与生态位、密林物种、被夹带到小岛的统治物种（P008，作者类比）。",
    "特斯拉（P015，作者预测其将专注于中国市场需求）。",
    "改籍来中国创建芯片企业、引擎企业的人（P015，作者的预测性举例）。",
    "行政堤防、江河、露珠、雨滴（P016，作者比喻，指行政手段拦不住技术与市场流动）。",
    "“柴铺得更宽／烘得更干、堆得更高”（P020，作者比喻，指扩大市场与提高市场质量）。",
    "隐含反驳对象：把技术领先归因于独特天才、人才、资本或具体扶持政策的看法（P001、P002、P010）。"
   ],
   "conditions": [
    "时间尺度条件：结论以“最终”“迟早”“未来三五年”表述，属预测而非已发生事实（P002、P015、P021）。",
    "条件式命题：如果这种技术在世界上的任何地方找到了相似的应用场景（P003）。",
    "政策前提：先解决内部垄断与对外封闭两个问题，技术优势才会被自然捕捉和发育（P011、P012）。",
    "加速条件：造就比当年资本主义国家快得多的开放速度和大的多的市场量级（P014）。",
    "环境限定：在不安全的国际环境下维持国有经济的绝对主体性（P017）。",
    "确定性自我标注：作者用“肉眼可见”“我也不信”“不出意料”标明其判断为推测（P019、P020、P021）。"
   ],
   "rhetoric_and_tone": "宣言式短句与排比（P010“而是市场、市场、以及市场”）；连续反问（P007“法国有冰原和沙漠吗？有喜马拉雅山吗？”）；生态与战争式隐喻（深渊巨龙、堤防、干柴火种）；预测语气用“看着吧——”“迟早”标出；结尾以“前景相当乐观”作乐观断言。全篇未引用他人文本，也未指名具体政策文件或数据来源。",
   "unresolved_questions": [
    "提问者问“中国有没有已经垄断世界的技术”，正文未列举任何具体已垄断技术的名称或证据，只给机制与方向；“有没有”的事实问题未被直接回答。",
    "P007 关于法国、日本、德国地理条件与铁路网数据能力的反问属修辞性反例，其中事实细节需外部核查。",
    "P015 特斯拉与改籍创业属预测，正文未给依据、时间表或判定标准。",
    "P017-P019 关于国有经济主体性、知识产权障碍、政策平衡点与政策走向的判断，未提供数据或文件依据，需外部核查。",
    "“独有的需求”“更大的应用前景”如何度量，正文未说明。",
    "更新时间为2021年，若以当前时点检验P021的“未来三五年”预测是否兑现，需外部核查；本篇不自行裁决。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "独得之秘的根基，并不来自独特的天才，而是来自独有的需求。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "凡是在中国拥有更大的应用前景的领域，最终都一定会诞生中国领先于世界的技术。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果这种技术在世界上的任何地方找到了相似的应用场景，这种技术就一定会压倒其他技术成为优势技术。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "在技术发展的宏观层面，灵感的火种远不如遍地的干柴重要。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "技术的关键最根本的要害不是具体的扶持政策，而是市场、市场、以及市场。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "第一是消除不必要的内部垄断，把市场做深；第二是消除不必要的对外封闭，把市场做大。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "这其实就是所有“全球垄断的技术”的共同出生路径。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "特斯拉最终会成为首先专注于（如果不是唯一专注于）中国市场需求的中国企业。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "现在真正的难点，是在不安全的国际环境下要维持国有经济的绝对主体性所造成的垄断性过高和对私有经济知识产权的障碍过多。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P020", "quote": "而我也不信中央没有看到除了把柴铺得更宽之外还有把柴烘得更干、堆得更高的必要性。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "未来三五年在引入民间资本涉足重大研究项目的制度创新、科教体制创新和知识产权保护实践上会有更大的动作。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "中国的技术领域前景相当乐观。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P006", "quote": "典型的例子就是大型基建工程、重型装备。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["技术与产业政策", "中国经济", "国际竞争"],
   "issue_candidates": ["技术领先的成因（需求/市场 vs 人才资本与扶持政策）", "中国已垄断技术的判定", "市场做深与做大", "知识产权与民间资本参与重大研究"],
   "text_function_candidates": ["答疑", "论辩", "预测/评论"],
   "object_candidates": ["中国", "法国", "日本", "德国", "特斯拉", "中央"],
   "working_keywords": ["独得之秘", "独有的需求", "干柴/火种", "市场", "内部垄断", "对外封闭", "传承级护城河", "平衡态"]
  },
  "notes": "本篇无图片节点，22段正文全部读完，正文与brief一致（brief为正文截断）。全篇含多处预测性表述（P002的“最终”、P015的“迟早/最终”、P021的“未来三五年”），已按predicted/predicted/hypothetical分别标注，未当作已实现事实。事实性断言（法日德地理与铁路网、特斯拉走向、政策动作）一律登记为待外部核查，未在本篇裁决。"
 },
 "ca98070c": {
  "analysis": {
   "question_context": "提问者（Q001）问“计划经济为什么会失败？”，提问本身预设了计划经济已经失败。作者直接否定该预设：失败的只是苏联，而不是计划经济；并进一步主张经济体制不是领导层可选择的结果，比较计划与市场谁更优越本身是伪问题。全篇为强论辩性回答，含对论辩对手动机的指控。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "否定提问预设：只是苏联失败了，不是计划经济失败；苏联失败很大程度因文化、社会、人口积淀承受不起其宏伟志向；而以举杠铃比喻说明“发力姿势不合理”式归因虽“对”却毫无营养，反而应说苏联计划经济已创造惊人奇迹。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "论据：沙俄一战前仍是农奴制国家、工业垫底、海军近零；若一开始搞自由放任市场经济，连摸杠铃的机会都没有；只是那个奇迹没能帮它举住杠铃。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "给出机制：市场经济的前提是足够的安全环境，进入战备状态自由经济必被战时经济取代；“苏联计划经济”的本质就是“战时经济”；苏联生存空间逼仄，没有机会从战时经济转轨。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "结论：苏联实施计划经济在那种条件下是对的，失误在于没能争取到更安全和平的发展条件；历史不容假设，这几乎是宿命，甚至不存在选择。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "反驳“经济体制是领导层选择的结果”：经济政策是对经济现实的体认和适应的结果，是先被客观现实决定再被明文接受的过程；安全与否不由自己选择。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017"], "summary": "举例：美国危机时会往计划经济换挡，中国越安全则越往自由经济换挡；个人意愿与决策层理想不决定宏观长期走向。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022", "P023"], "summary": "主张“计划与市场谁更优越”是伪问题，给出两条理由：决定权不在人类手上（强行调高或调低计划度都会自取灭亡）；锄头与镰刀各适其用，只谈形状光泽的“选美讨论”的用处是诱骗邻居放下锄头改用镰刀，好在其绝收后卖米。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029"], "summary": "反过来要求对方先给出“一种经济运行机制所谓成功的可靠定义”，或证明“使得计划经济不必然失败的成功定义逻辑上不存在”；并拒绝以结论反推定义的立场。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P030"], "summary": "限定：这个成功标准不能高到“任何经济体制都失败”的程度。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035"], "summary": "以原始飞行器屡败而热气球早已能飞的历史类比，主张计划经济是复杂概念、有探索成长过程；衡量标准应是这次是否比上次飞得远、今年是否超过去年，有此种表现的新事物不能被简单断为必然失败。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040", "P041", "P042"], "summary": "追问计划经济是否体现进步轨迹：几乎每家企业都是计划经济的典范，最大有效竞争规模随管理技术提升而扩大；在能确切证明存在上限之前不能断言计划经济必然失败；前提是不能超过可有效管理的规模上限。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P043", "P044", "P045", "P046"], "summary": "论据：苏联的规模上限受纸、笔、手工插接电话限制，远不到一个国家；今天的人工智能、大数据、工业互联网等技术已把可支撑规模上限扩展到与小型国家相当，并以现代最大企业年销售额达千亿美元级、与许多国家GDP相当为证。", "role": "example"},
    {"unit_id": "U013", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051"], "summary": "问题转为能否把该策略用于几百万至十亿级群体、计划要管到什么方面与深度；指出“哪些不纳入计划”本身也是计划的一部分；趋势是从“天生可以随便”转向“天生就不能随便”。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056"], "summary": "理由：世界已进入新阶段，“先放任、出了问题再立约管束”的模式不可持续，因为短短几年放任即可孵化万亿规模跨国实体，若事后被证明致命，一国、一个文明乃至人类都可能承受不起；该模式一百年前是好策略，现在仍基本可行，一百年后将显而易见地愚蠢。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P057", "P058", "P059", "P060"], "summary": "结论与预测：没本钱犯错的国家应学会计划经济的必要技能并建立相应体制与权力构造；有本钱犯错的国家只是先等本钱输光；未来必定属于“按计划放任”的计划经济国家；这不是人类能凭好恶选择的。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "失败的只是苏联，而不是计划经济。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "苏联的失败很大程度上是因为其文化、社会、人口积淀承受不起它自己的宏伟志向，而不是它的“经济制度不合理”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以苏联当时的社会结构、文化积淀与时间限制，与其说计划经济失败，不如说它已经创造了惊人的奇迹。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“苏联计划经济”的本质不是哲学思想的差异，而就是“战时经济”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "苏联实施计划经济在那种前提条件下是对的，其失误不在于实施了计划经济，而在于没能争取到更安全和平的发展条件。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "（作者反驳的观点）人们认为自己所处的国家实行什么样的经济体制是领导层“选择”的结果。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "经济政策是对经济现实的体认和适应的结果，是被客观现实先决定、然后被明文接受的过程；安全或不安全不由自己选择。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "比较“计划经济和市场经济谁更优越”本身就是一个错误的伪问题，没有实际意义。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不管觉得哪种体制“更好”，决定权都不在人类手上：强行调低计划度就是自取灭亡，安全危机撑不起高计划度而强行调高则地位不保。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在能确切证明“最大有效竞争规模”存在数学上限之前，不能断言“计划经济必然失败”。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "几乎每一家企业都在内部进行强计划指令管理，这本身就说明“用合理的自上而下的计划管理内部资源分配以发挥最强对外竞争力”是毫无疑问的首选策略，前提是不超过可有效管理的规模上限。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "（作者反驳的观点）用婴儿期笨拙的计划经济实践所展现的缺陷来断言“凡属计划经济必定会失败”。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只谈形状颜色和光泽的体制“选美讨论”，最大的“用处”只是诱骗邻居放下锄头改用镰刀，好在其绝收之后卖米。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "自由放任、发现恶果再改在一百年前是好策略，现在仍基本可行，但一百年后将变得显而易见的愚蠢。", "evidence": ["E14"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "未来必定会属于“按计划放任”的计划经济国家，而不可能属于“原教旨主义自由经济”国家；这不是人类可以凭自己的好恶选择的东西。", "evidence": ["E15", "E16"]}
   ],
   "argument_steps": [
    "P001 直接否定提问预设：失败的是苏联，不是计划经济。",
    "P002-P003 给出归因（文化社会人口积淀不足）并用举杠铃比喻评价“发力姿势不合理”式归因的正确但无营养。",
    "P004 转向反面判断：应说苏联计划经济创造了奇迹。",
    "P005-P007 以沙俄起点低为论据，并作反事实推论（若搞自由放任则连摸杠铃机会都没有）。",
    "P008-P009 提出机制与定义：安全环境决定体制，战备状态下自由经济必被战时经济取代；苏联计划经济即战时经济。",
    "P010-P012 以生存空间逼仄说明无转轨机会，判定其实施计划经济是对的，失误在未争取到安全和平条件。",
    "P013-P015 反驳“体制是领导层选择”的误解，提出经济政策是对现实的体认与适应。",
    "P016-P017 以美中换挡为例，说明宏观长期走向不由个人意愿决定。",
    "P018-P023 判定优劣比较是伪问题，给两条理由并以锄头镰刀与卖米之喻指控对手动机。",
    "P024-P029 反向要求对方先定义“成功”或证明不存在此种定义。",
    "P030 限定成功标准不能高到任何体制都失败。",
    "P031-P035 以飞行器/热气球的历史类比，提出以“是否刷新记录”为衡量标准。",
    "P036-P042 把检验落到企业内部计划管理的事实与“最大有效竞争规模”是否上升上。",
    "P043-P046 以苏联工具限制与今日技术条件、千亿美元级企业规模为论据。",
    "P047-P051 把问题转为规模与计划边界，并提出“有理由才放任”正在击败“有理由才管制”。",
    "P052-P056 说明理由：放任几年即可孵化万亿级跨国实体，事后致命的后果无人承受得起。",
    "P057-P060 结论与预测：没本钱犯错的国家应学计划经济技能，未来属于“按计划放任”的国家。"
   ],
   "concept_usage": [
    {"term": "计划经济", "meaning": "本文在苏联语境中与“战时经济”实质等同；同时也用于指企业内部的自上而下计划指令管理与未来的“按计划放任”体制；作者强调它是复杂概念，存在探索和成长过程。", "evidence": "P009", "ambiguity": "“计划经济”的多个用法（战时经济、企业内部计划管理、未来体制）在文中未作统一界定，存在歧义。"},
    {"term": "战时经济", "meaning": "战备状态下取代自由经济的形态；作者用它界定“苏联计划经济”。", "evidence": "P008", "ambiguity": "战时经济与计划经济的界线未说明。"},
    {"term": "安全（环境）", "meaning": "决定经济体制走向的客观变量：安全则可行自由经济，不安全则必须计划。", "evidence": "P015", "ambiguity": "“安全”如何度量未说明。"},
    {"term": "最大有效竞争规模／可有效管理的规模上限", "meaning": "计划经济能否成立的规模变量，随管理技术与工具提升而扩大。", "evidence": "P039", "ambiguity": "是否存在数学上限，作者称尚不能证明。"},
    {"term": "伪问题", "meaning": "指“计划与市场谁更优越”的比较（P018），亦用于P024-P029对“成功定义”的追问。", "evidence": "P018", "ambiguity": "作者未说明在何种条件下该比较才有意义（P021 的锄头镰刀之喻暗示取决于用途）。"},
    {"term": "按计划放任", "meaning": "作者对未来的计划经济社会形态的概括：以“有理由才放任”为原则。", "evidence": "P059", "ambiguity": "具体制度形态及其与既有计划经济的差别未说明。"},
    {"term": "自由放任", "meaning": "先放任、出现问题再设立新社会契约管束的传统模式；其“原教旨主义”版本被作者判为没有未来。", "evidence": "P053", "ambiguity": "“原教旨主义自由经济”的定义未给出。"}
   ],
   "examples_and_targets": [
    "苏联与沙俄：一战前仍是农奴制国家、工业水平列强垫底、海军实力近乎于零（P005，作者论据，事实细节待外部核查）。",
    "身体瘦弱的小孩举杠铃、被认定为“发力姿势不合理”（P002、P007，作者类比）。",
    "美国、西欧、拉美、日韩菲台、中国（P010，作者用于对比苏联生存空间）。",
    "坐在火车上的人与铁轨、扳道工（P020，作者类比：决定权不在讨论者手上）。",
    "锄头与镰刀、诱骗邻居换工具再卖米（P021、P022，作者类比，并以之指控论辩对手的动机）。",
    "原始飞行器的屡屡失败与热气球的滞空（P031、P032，作者历史类比，事实细节待外部核查）。",
    "以纸、笔、手工插接电话运营的实体 vs 人工智能、大数据、工业互联网、高铁、涡扇喷气式客机（P043、P044，作者工具条件对比）。",
    "现代最大企业年销售额达千亿美元级、与很多国家GDP相当（P046，作者数据断言，待外部核查）。",
    "反驳对象一：断言“凡属计划经济必定会失败”者（未指名，P031）。",
    "反驳对象二：认为经济体制是领导层“选择”的结果者（未指名，P013）。",
    "反驳对象三：进行体制“选美讨论”并据此劝人换轨者（未指名，P022）。"
   ],
   "conditions": [
    "前提条件：市场经济的前提是有足够的安全环境；一旦进入战备状态，自由经济必然被战时经济取代，非人力所能抗拒（P008）。",
    "规模条件：不能超过可以有效管理的规模上限，要保持计划的有效性（P042）。",
    "工具／技术条件：苏联受纸、笔、手工插接电话限制，今日技术已使可支撑规模与小型国家相当（P043、P045）。",
    "方法论条件：成功定义不能高到“任何经济体制都失败”的程度（P030）；须先给出定义或证明其不存在（P028、P029）。",
    "时间条件：一百年前／现在／一百年后的策略有效性不同（P056）；未来“必定”（P059）。",
    "反事实条件：如果苏联一开始就搞自由放任市场经济（P006）；作者同时声明历史不容假设（P012）。",
    "主体限定：分别针对“没本钱犯错的国家”与“有本钱犯错的国家”（P057、P058）。"
   ],
   "rhetoric_and_tone": "强论辩语气：开篇即否定提问预设；反问密集（P003“这样认定“对”吗？”，P025、P026、P039）；类比贯穿全篇（举杠铃、锄头镰刀、火车铁轨、飞行器与热气球）；含直接训斥与讥讽（P023“不要犯蠢。”，P022“诱骗邻居放下锄头改用镰刀”，P027“建议不要浪费别人的时间”）；以“你们”“你”直接对话读者；结尾用“看着吧”引出预言式断言。",
   "unresolved_questions": [
    "提问问“计划经济为什么会失败”，作者否定提问前提，未逐条讨论通常列举的失败原因（如激励、信息、计算问题）。",
    "“文化、社会、人口积淀”如何度量、达到什么水平才算“承受得起宏伟志向”，正文未给判据（P002）。",
    "“计划经济”在本文中至少有三重用法（战时经济、企业内部计划管理、未来“按计划放任”体制），相互界线未界定，可能影响解释。",
    "P005、P031、P032、P038、P046 的历史叙述与数据（沙俄工业水平、最大企业年销售额、最大有效竞争规模变化）需外部核查，本篇不裁决。",
    "P022、P027 对论辩对手动机的指控（诱骗邻居、浪费别人时间）属作者判断，未提供证据或指名对象。",
    "“按计划放任”的制度形态、计划边界的划分原则（P048、P049）未展开。",
    "文章更新时间为2022年（发表2020年），是否有修改、与初版差异如何，正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "那只是苏联失败了，而不是计划经济失败了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "苏联的失败原因很大程度上是因为它的文化、社会、人口积淀承受不起它自己的宏伟志向", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "与其说是苏联的计划经济失败了，不如说是苏联的计划经济已经创造了惊人的奇迹。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "“苏联计划经济”的本质根本不是什么哲学思想的差异，而就是“战时经济”四个字而已。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "它的失误不在于实施了计划经济，而在于没能争取到更安全和平的发展条件。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P013", "quote": "人们最大的误解，就是认为自己所在的国家实行着什么样的经济体制是领导层“选择”的结果。", "relation": "contradicts"},
    {"key": "E7", "paragraph_id": "P015", "quote": "经济政策是对经济现实的体认和适应的结果", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P018", "quote": "比较“计划经济和市场经济谁更优越”，本身就是一个错误的伪问题，没有实际意义。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "你的计划度该有这么高，你出于“对自由的向往”强行调低，你就是在自取灭亡", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P040", "quote": "在你能确切的证明有这个上限之前，你不能断言“计划经济必然失败”。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P041", "quote": "几乎每一家企业都在内部进行强计划指令管理这种基本的事实", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P031", "quote": "来断言“凡属计划经济必定会失败”", "relation": "contradicts"},
    {"key": "E13", "paragraph_id": "P022", "quote": "最大的“用处”只是用来诱骗邻居放下锄头改用镰刀，好在他绝收之后卖米。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P056", "quote": "自由放任，发现恶果再改，在一百年前是好策略，现在仍然基本可行，但一百年后将变得显而易见的愚蠢。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P059", "quote": "未来必定会属于“按计划放任”的计划经济国家", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P060", "quote": "这不是人类可以凭自己的好恶选择的东西。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P008", "quote": "实施市场经济的前提是你有足够的安全环境。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P042", "quote": "前提只是你不能超过你可以有效管理的规模上限，要保持计划的有效性。", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P030", "quote": "注意这个标准显然不能高到“任何经济体制都失败”这个程度。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["经济体制与经济史", "政治经济学", "国际战略与安全"],
   "issue_candidates": ["苏联计划经济失败的原因", "经济体制是否可选择", "计划与市场优劣比较是否成立", "计划的有效规模上限", "放任与管制的次序"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "预测/评论"],
   "object_candidates": ["苏联", "沙俄", "美国", "中国", "西欧", "拉美", "日韩菲台"],
   "working_keywords": ["计划经济", "市场经济", "战时经济", "安全环境", "伪问题", "最大有效竞争规模", "按计划放任", "自由放任"]
  },
  "notes": "本篇无图片节点，60段正文全部读完，正文与brief一致（brief为正文截断）。提问预设“计划经济为什么会失败”，作者否定该预设，故提问预设未归给作者，作者的反驳对象按opponent_view/opponent登记（P013、P031，均未指名）。文中历史与数据断言（沙俄工业水平、飞行器史、千亿美元级企业规模）一律登记为待外部核查，未在本篇裁决。P019 的计划度强行调高/调低、P056 的百年尺度、P059 的“必定”均保留其条件与预测语气。"
 },
 "23d679c7": {
  "analysis": {
   "question_context": "提问者（Q001）问“人是怎么变强的？”，属人生经验/认识论类提问。作者以格言体回答：变强从谦卑开始，即从信任个人意志与判断转向依靠方法与对自身局限的认识；并给出“是人皆弱”的论断，把真正的强大定义为对绝对软弱的自觉。全文为断言式短句，无举例展开与外部引用。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出总命题：人是从谦卑开始变强的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "以排比给出谦卑的四组表现：从凭意志力对抗诱惑转向用方法降低系统难度；从凭好记性转向记笔记；从自认绝对公正转向理解正义的复杂性；从相信自己料事如神转向不再认为“看不到问题就是没有问题”和“我不喜欢的就是错”。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "转折性判断：直到人学会敬畏为止，用各种手段获得的“变强感”都只是预谋已久的幻觉，其真实性来自迫不及待的精神毒瘾。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "论断：是人皆弱，没人是所谓强大的；即使世界冠军在真正的问题面前也只是蝼蚁。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "限定与结论：唯一相对强的是对这一认识更深刻、把一切建立在绝对弱者自觉之上的人；清楚认识到自己的绝对软弱不是怯懦而是真正的刚勇，那才是真正强大的起点。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人是从谦卑开始变强的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谦卑表现为从依赖意志力、记性、自我公正感与料事如神，转向依靠方法、习惯、对复杂性的理解和对自身盲区的警觉。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "直到人学会敬畏为止，人用各种手段获得的“变强感”实际都是预谋已久的幻觉，其真实性只来自一种迫不及待的精神毒瘾。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是人皆弱，没人是所谓强大的；即使是世界冠军，在真正的问题的挑战面前也只是蝼蚁。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "唯一相对强的是对这一认识比别人更为深刻、更深地将一切建立在绝对弱者自觉之上的人，即那些花了很多努力去学习和练习如何作为弱者生存的人。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "清楚地认识到自己的绝对软弱不是怯懦，而是一种真正的刚勇，那才是真正强大的起点。", "evidence": ["E8", "E9"]}
   ],
   "argument_steps": [
    "P001 提出总命题（变强从谦卑开始）。",
    "P002-P005 以四组“从……转而开始……”排比具体化谦卑的内容（方法与系统、习惯、理解复杂性、警觉自身盲区）。",
    "P006 给出反面判据：未学会敬畏之前所获的“变强感”是幻觉与精神毒瘾。",
    "P007-P008 提出“是人皆弱”的普遍论断并推向极端（世界冠军也只是蝼蚁）。",
    "P009 作限定：唯一相对强的是对软弱认识更深、以弱者自觉为基础的人。",
    "P010-P011 重新定性：承认绝对软弱是刚勇而非怯懦，是真正强大的起点。"
   ],
   "concept_usage": [
    {"term": "谦卑", "meaning": "变强的起点；具体指放弃对个人意志力、记性、公正感、预判力的信任，转而依靠方法、习惯与对复杂性的理解。", "evidence": "P001", "ambiguity": "未区分谦卑与自我贬低；也未说明其与“敬畏”的关系。"},
    {"term": "敬畏", "meaning": "终止“变强感”幻觉的转折点，以“直到……为止”的条件式出现。", "evidence": "P006", "ambiguity": "敬畏的对象与内容正文完全未说明。"},
    {"term": "变强感", "meaning": "未学会敬畏之前通过各种手段获得的自我感觉；作者判其为幻觉，其真实性来自精神毒瘾。", "evidence": "P006", "ambiguity": "与真实“变强”的区别标准未给。"},
    {"term": "绝对弱者自觉", "meaning": "把一切建立在对自身绝对软弱的认识之上；作者视之为唯一相对强的根据。", "evidence": "P009", "ambiguity": "该自觉如何转化为行动未说明。"},
    {"term": "刚勇", "meaning": "与怯懦对举，指清楚认识到自己的绝对软弱。", "evidence": "P010", "ambiguity": "未说明其与通常所谓勇敢的关系。"}
   ],
   "examples_and_targets": [
    "凭意志力对抗诱惑 vs 降低对抗诱惑的系统难度（P002，作者举例）。",
    "凭好记性记得 vs 养成记笔记的习惯（P003，作者举例）。",
    "认为自己绝对公正 vs 理解正义的复杂性（P004，作者举例）。",
    "相信自己料事如神 vs 不再认为“看不到问题就是没有问题”和“我不喜欢的就是错”（P005，作者举例）。",
    "世界冠军（P008，作者举的极端反例，说明“没人是所谓强大的”）。",
    "被反驳/被否定的对象：未学会敬畏之前以各种手段获取“变强感”的做法（P006，作者判为幻觉）。"
   ],
   "conditions": [
    "时间/条件限定：直到人学会敬畏为止（P006），此前所获的“变强感”均属幻觉。",
    "适用范围：泛称的“人”，未限定年龄、处境或领域（P001、P007）。",
    "限定语：“唯一相对强的”（P009）表明作者只作相对比较，不作绝对断言。"
   ],
   "rhetoric_and_tone": "格言体与箴言式短句；四组“从……转而开始……”排比（P002-P005）；定义式与悖论式判断（“绝对软弱”对应“真正的刚勇”）；末尾两段以短句层层递进收束；无第二人称直呼，无引用与举例展开，语气冷峻、训诫性但不斥责具体对象。",
   "unresolved_questions": [
    "“敬畏”的对象（自然、规律、他人还是自身局限）正文完全未说明，是解释本篇的关键空白。",
    "“绝对弱者自觉”如何转化为具体行动、如何与学习方法（P002-P005）衔接，正文未说明。",
    "“变强感”与真实“变强”的判别标准未给；提问者问“怎么变强”，正文只给起点与认识论条件，未给过程机制。",
    "P008 以世界冠军作“蝼蚁”的比喻属修辞性断言，未给依据。",
    "更新时间为2025年（晚于发表时间2020年），正文是否有修订、与初版差异如何，正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人是从谦卑开始变强的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "从认为自己可以凭意志力对抗诱惑，转而开始思考方法来降低对抗诱惑的系统难度。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "从相信自己料事如神，转而开始不再认为“看不到问题就是没有问题”和“我不喜欢的就是错”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "直到人学会敬畏为止，人采取各种手段获得“变强感”，实际获得的都是一种预谋已久的幻觉", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P007", "quote": "是人皆弱。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "没人是所谓强大的。即使是世界冠军，在真正的问题的挑战面前也只是蝼蚁。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "唯一相对强的，是对这一认识比别人更为深刻，于是更深地将一切建立在绝对弱者自觉之上的人", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "清楚的认识到自己的绝对软弱，那不是怯懦，而是一种真正的刚勇。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "那才是真正强大的起点。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲学与自我修养", "认识论/自我认识"],
   "issue_candidates": ["变强的起点", "谦卑与敬畏", "自我评价的幻觉", "弱者自觉与刚勇"],
   "text_function_candidates": ["答疑", "格言/箴言", "劝导"],
   "object_candidates": ["世界冠军（作为极端反例）"],
   "working_keywords": ["谦卑", "敬畏", "变强感", "是人皆弱", "绝对弱者自觉", "刚勇"]
  },
  "notes": "本篇无图片节点，11段正文全部读完，正文与brief一致（brief为正文截断）。全篇为格言式断言，无具体案例与数据；“敬畏”的对象未说明，已登记为关键空白，未据brief或标题补写。四组排比属作者举例性说明，已归入content_units而非独立主张。"
 },
 "c4effbba": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么25岁个人资产接近3000W，年收入70W，幸福感几乎没有？”，属个人处境类提问，提问者自述的资产与收入数据属于提问者说法。作者未回应具体数字与处境，只以四句隐喻作答：幸福不在已有的路与远方的目标，而在前进过程本身。全文67字，无举例、无引用、无数据。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以对偶否定—肯定的句式界定幸福：不是背后的路，也不是远方的目标，而是前进时掠过耳边的风。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "以运动与静止的条件对照收束：在动就有风；停下则不论停在多么了不起的地方，风就没了。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "幸福不是背后的路，也不是远方的目标。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "幸福是前进时掠过耳边的风。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "在动就有风；停下时不管停在多么了不起的地方，风就没了。", "evidence": ["E3", "E4"]}
   ],
   "argument_steps": [
    "P001 以否定句排除两种对幸福的定位（已走的路、远方的目标）。",
    "P002 给出正面隐喻（前进时掠过耳边的风）。",
    "P003 以“在动就有风”给出正面条件。",
    "P004 以“停下则风没了”给出反面条件并收束全篇。"
   ],
   "concept_usage": [
    {"term": "幸福", "meaning": "本文中不指资产、收入等既有条件，也不指未来目标，而指前进过程本身。", "evidence": "P002", "ambiguity": "未说明“前进”指收入增长、能力提升还是别的维度。"},
    {"term": "路／目标", "meaning": "分别喻指已经取得的成就（背后的路）与将来要达到的成就（远方的目标），均被排除在幸福之外。", "evidence": "P001", "ambiguity": "二者与“前进”的关系未展开。"},
    {"term": "风", "meaning": "隐喻前进过程中产生的体验；以运动为存在条件，停止即消失。", "evidence": "P004", "ambiguity": "未说明风的内容（愉悦、意义感或其他）。"}
   ],
   "examples_and_targets": [
    "背后已走过的路、远方尚未到达的目标（P001，作者用以排除的两种定位，属修辞材料）。",
    "掠过耳边的风（P002、P003、P004，作者的核心隐喻）。",
    "提问者自述的“25岁、个人资产接近3000W、年收入70W、幸福感几乎没有”未在正文出现，作者未以其为论据也未加评论。"
   ],
   "conditions": [
    "条件对照：在动（前进）则有风；停下则风消失，且与停留地多么了不起无关（P003、P004）。",
    "对象范围：第二人称“你”，未限定年龄、资产或职业条件。"
   ],
   "rhetoric_and_tone": "全篇为隐喻式短句与对偶（“不是……也不是……而是……”）；四段两两成对，接近箴言/诗句；语气平静、劝谕，无训诫与讽刺；未直接回应提问者的数字与焦虑，也未使用否定提问者的措辞。",
   "unresolved_questions": [
    "提问者所述具体情形（25岁、3000W、70W）在正文中完全未出现，作者是否认为资产与幸福感无关，正文未说明。",
    "“前进”的判定标准（收入、能力、关系还是别的）未说明，因而该隐喻缺少可检验判据。",
    "全篇为诗性隐喻，未给经验证据；是否主张“停下的富裕者必然不幸”无法从文中确定。",
    "更新时间为2021年，正文是否有修订、与初版差异如何，正文未说明。",
    "本篇属极短文本（正文67字），未展开论证，提问者的“为什么”未被直接因果性回答。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "幸福不是你背后的路，也不是你远方的目标，", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "而是你前进时掠过耳边的风。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你在动，就有风。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你停下，不管你停在多么了不起的地方，风就没了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生感悟/幸福观", "财富与心态"],
   "issue_candidates": ["高收入与低幸福感", "幸福是否来自前进过程而非既有成就"],
   "text_function_candidates": ["答疑（隐喻式回应）", "感言/箴言"],
   "object_candidates": ["unknown（正文未指名任何人物、机构或地区）"],
   "working_keywords": ["幸福", "前进", "风", "目标", "停下"]
  },
  "notes": "本篇无图片节点，4段正文（共67字）全部读完，正文与brief一致。全篇为隐喻短句，提问者的资产与收入数据未进入正文，未据此推断作者立场；因无经验主张与可检验判据，已在unresolved_questions登记。"
 },
 "1068d35e": {
  "analysis": {
   "question_context": "提问者（Q001）问“加班和超额工作是否正在毁掉中国大部分的劳动者？”，提问预设了“加班/996正在毁掉劳动者”的判断，属提问者说法。作者先给出提高收入的两条做法并推荐“四小时满负荷+四小时提升单位时间价值”的策略，随后否定提问预设：真正毁掉人的不是996，而是废弃了提升单位时间价值这条路。全篇为策略建议+归因反驳。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出提高收入的两个做法：A 在单位小时工资基本不变的前提下延长劳动时间；B 维持劳动时间不变、提高单位小时工资。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "给出建议与理由：不要找做满八小时的工作，最理想是只满负荷工作四小时并用另外四小时让这四小时更值钱；延长工作时间有极限，提升单位时间价值是无限的，靠多花时间才多赚钱的事其实是亏的。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "以较强措辞给出标准：若非个人特别兴趣，一天需工作超过四小时才能满足人生需求是一种需摆脱的失败；四小时以下获得的收入才是真实的收入；四小时即可得的小康胜过日夜煎熬日进斗金。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013"], "summary": "给出两个“走在正路上”的迹象（四小时不变而收入增多；收入稳定而工时变短），并称后者更厉害，降到0时是神仙中人。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "回到本题：真正让人陷入深渊的不是996，而是人们走不了“用四个小时去加强另外四个小时”的路、平白浪费掉那四个小时；在责任到来（恋爱、买房、生娃、供养老病）而无路可走时，996反而还算给了挣扎的机会。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019"], "summary": "指认真正的毁人原因：很早自认“不是读书的料”，用“我学不进去”“这个社会还是要靠关系”废弃了那条唯一出路；没了这条路就只剩996一个选择。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "回应“没读大学就活该996”式的不公平质疑：问题根本不在公平不公平；条件好按条件好的走法、条件不好按条件不好的走法，走了就有好处。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "给出可缩放的最低起点（四小时→一小时→半小时→十分钟）与方向：以“提高单位时间报酬”为本位导向，坚持就会有改善的一天，越改善越能活。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "对以各种理由解释无法使用该策略者的收束性回应：去跟数学商量；真正过不去的是简单的数学，不是“资本家”或“社会”，数学不关心你为什么做不到。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提高收入有两个做法：在单位小时工资基本不变的前提下延长劳动时间；维持劳动时间不变而提高单位小时工资。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议不要找做满八小时的工作，最理想的是找只会满负荷工作四小时的工作，用另外四小时让这四小时不断变得更值钱。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "延长工作时间是有极限的，提升单位时间价值却是无限的；需要多花时间才会多赚钱的事其实是亏的。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "如果不是出于个人的特别兴趣，一天需要工作超过四小时才能满足人生需求，是一种需要摆脱的失败。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个人一天工作四小时以下获得的收入才是真实的收入。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两个迹象显示走在正路上：维持四小时不变而收入越来越多；或收入稳定而工作时间越来越短。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真正让人陷入深渊的不是996，而是人们走不了“用四个小时去加强另外四个小时”的路，绝大多数人平白浪费掉这四个小时。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "（被作者反驳的说法）很多人空想“只要强行禁止996，就可以不必996了”；作者称成年人实为要扩大收入而只有996这一条路可走。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "毁掉自己的根本不是996；在责任到来无路可走的时候，996还算给了挣扎一下的机会。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正毁掉你的是很早就自认“不是读书的料”，用“我学不进去”“这个社会还是要靠关系”废弃了那条唯一出路。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "对“没读大学就活该996”式质疑，问题根本不是公平不公平。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正跟你过不去的是简单的数学，不是什么“资本家”或者“社会”；数学不关心你为什么做不到。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“提高单位时间报酬”为本位导向是策略问题、方向问题；起点可以缩到一小时、半小时甚至十分钟，坚持就会有改善的一天。", "evidence": ["E17", "E18"]}
   ],
   "argument_steps": [
    "P001-P003 定义两条提高收入的路径（A 延长时间；B 提高单位小时工资）。",
    "P004-P005 给出建议：不要做满八小时，理想是四小时满负荷+四小时增值。",
    "P006-P007 给出理由（时间有极限、单位价值无限；多花时间才多赚钱是亏的）。",
    "P008-P010 以较强措辞设定标准（超过四小时才够用是失败；四小时以下才是真实收入）。",
    "P011-P013 给出“走在正路上”的两个迹象，并抬高第二种（工时递减、降到0为神仙中人）。",
    "P014-P015 转入本题：真正致人深渊的是走不了“用四个小时加强另外四个小时”的路。",
    "P016 说明现实压力（恋爱、买房、生育、养老）使四小时不够，并反驳“禁止996即可不必996”的空想。",
    "P017 否定命题：毁掉自己的不是996，反而996提供了挣扎机会。",
    "P018-P019 指认真正的毁人原因（自认不是读书的料、废弃唯一出路）。",
    "P020-P024 回应公平质疑：问题不在公平，而在是否按自身条件走这条路。",
    "P025-P028 给出可缩放的起点与方向，主张坚持会改善。",
    "P029-P032 以“数学”作结，否定以资本家/社会作解释的理由。"
   ],
   "concept_usage": [
    {"term": "做法A／做法B", "meaning": "提高收入的两条路径：延长劳动时间（单位小时工资基本不变）／维持劳动时间而提高单位小时工资。", "evidence": "P002", "ambiguity": "两条路径能否并存、优先级如何，作者倾向于B但未严格排斥A。"},
    {"term": "单位小时工资／单位时间价值", "meaning": "被作者视为可无限提升的变量，是其建议的核心指标。", "evidence": "P006", "ambiguity": "如何提升单位时间价值的具体方法，正文只以“用四个小时去加强另外四个小时”概括。"},
    {"term": "“用四个小时去加强另外四个小时”", "meaning": "作者对做法B的具象表述：一半工时维持负荷，另一半用于提升自身价值。", "evidence": "P005", "ambiguity": "“加强”的具体内容（学习、技能、关系）未列举。"},
    {"term": "996", "meaning": "本文中作为“只有延长劳动时间一条路”的代称；作者否认它是毁掉劳动者的原因，并称其在无路可走时提供了挣扎机会。", "evidence": "P017", "ambiguity": "未与“超额工作”“加班”作严格区分。"},
    {"term": "真实的收入", "meaning": "一天工作四小时以下所获得的收入。", "evidence": "P009", "ambiguity": "该界定未给依据，也未讨论行业/岗位差异。"},
    {"term": "数学", "meaning": "喻指不以个人意愿与公平诉求为转移的客观约束。", "evidence": "P031", "ambiguity": "该比喻是否承认制度性/结构性因素，正文未说明。"},
    {"term": "那条唯一出路／读书", "meaning": "作者指认的、被自认“不是读书的料”者所废弃的提升单位时间价值的路径。", "evidence": "P018", "ambiguity": "“唯一”的适用范围与例外（职业培训、技能路径）未说明。"}
   ],
   "examples_and_targets": [
    "谈恋爱、买房、生娃、供老人病患（P016，作者列举的现实支出压力场景）。",
    "“只要强行禁止996，就可以不必996了”（P016，作者转述并反驳的空想）。",
    "“不是读书的料”“我学不进去”“这个社会还是要靠关系”（P018，作者引述并反驳的说法）。",
    "“难道没读大学就活该996”（P020，作者引述的读者反应/“不公平”质疑）。",
    "“资本家”“社会”（P031，作者指认并被其否定的替代归因对象）。",
    "“神仙中人”（P013，作者对工时降到0者的戏称，属修辞材料）。",
    "反驳对象：把劳动者困境归因于996或加班制度、或归因于资本家与社会的看法（P015、P017、P031）。"
   ],
   "conditions": [
    "做法A的前提：单位小时工资基本不变（P002）；做法B的前提：维持劳动时间不变（P003）。",
    "起点可缩放：找不到每天四小时的，就从一小时、半小时、十分钟起步（P025、P026）。",
    "条件式限定：如果不是出于个人的特别兴趣（P008）；在你的责任到来无路可走的时候（P017）。",
    "对象限定：“真正厉害的，是最后这一种人”（P012，指工时递减者）。",
    "适用范围未限定行业、岗位与技能起点，作者以“四小时”为普遍标准（P005、P009）。"
   ],
   "rhetoric_and_tone": "劝告与训诫语气，第二人称“你”直呼并连续追问；反复使用“真正……的不是……而是……”对举结构（P015、P017、P018、P031）；反问推进（P019“没了那条路，你不是只剩下996一个选择了吗？”）；对读者质疑作归谬式回应（P020-P023）；结尾把“数学”拟人化以作冷峻驳斥（P030“你去跟数学商量，看它原不原谅你。”），带讥讽意味；P008 用“失败”作强判断。",
   "unresolved_questions": [
    "“四小时”标准的依据（行业、岗位、技能起点差异）正文未说明，属作者自定标准。",
    "提问问“是否正在毁掉中国大部分的劳动者”，其中“大部分”的规模判断正文未给数据或统计依据，需外部核查。",
    "P016 关于恋爱、购房、生育、养老支出使四小时不够的判断属作者经验陈述，未提供数据。",
    "把“读书”称为“那条唯一出路”的适用范围与例外，正文未说明，存在歧义。",
    "“数学不关心你为什么做不到”是以客观约束消解制度性质疑的比喻；作者是否承认制度性因素的作用，正文未明确。",
    "P031 直接否定“资本家”与“社会”的解释力，但未讨论劳动时长与报酬的制度安排，该省略可能影响解释。",
    "更新时间为2025年（晚于发表时间2020年），正文是否有修订、与初版差异如何，正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "做法A，最简单，在单位小时工资基本不变的前提下延长劳动时间。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "做法B，维持劳动时间不变，提高单位小时工资。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "我建议人不要找做满八小时的工作。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "最理想的做法是要找只会满负荷工作四小时的工作", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "要知道延长工作时间是有极限的，但是提升单位时间价值却是无限的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "需要你多花时间才会多赚钱的事，其实是亏的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "如果不是出于个人的特别兴趣，一天需要工作超过四个小时才能满足人生需求，其实是一种需要摆脱的失败。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "一个人一天工作四小时以下获得的收入才是真实的收入。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "要么维持四小时不变，你的收入越来越多；要么收入维持在一个稳定的水平上，工作时间变得越来越短。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "真正让人陷入深渊的不是什么996，而是出于种种原因，人们走不了“用四个小时去加强另外四个小时”的路", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "很多人在空想“只要强行禁止996，就可以不必996了”，其实这都是还没活醒罢了。", "relation": "contradicts"},
    {"key": "E12", "paragraph_id": "P017", "quote": "毁掉自己的，根本不是996", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "真正毁掉你的，是你很早就自认“不是读书的料”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "这里的问题根本不是公平不公平。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P031", "quote": "真正跟你过不去的是简单的数学，不是什么“资本家”或者“社会”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P032", "quote": "数学不关心你为什么做不到。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "以“提高单位时间报酬”为本位导向，这是策略问题、方向问题", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "哪怕是十分钟也好。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["劳动与收入", "职业发展与个人策略", "工作伦理"],
   "issue_candidates": ["加班/996是否毁掉劳动者", "提高收入的两条路径", "单位时间价值的提升", "公平与个人条件"],
   "text_function_candidates": ["答疑", "策略建议", "反驳", "训诫/劝告"],
   "object_candidates": ["中国劳动者（提问所指群体）", "资本家", "社会（被作者否定的归因对象）"],
   "working_keywords": ["996", "加班", "单位小时工资", "单位时间价值", "四小时", "读书", "数学"]
  },
  "notes": "本篇无图片节点，32段正文全部读完，正文与brief一致（brief为正文截断）。提问预设（加班/996正在毁掉大部分劳动者）属提问者说法，未归给作者；“强行禁止996即可不必996”“没读大学就活该996”等按opponent_view/opponent/questioned登记。P006、P009、P016 的经验与规模判断无数据支撑，已登记待外部核查；P031-P032 对“资本家/社会”归因的否定保留其否定语气。"
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
