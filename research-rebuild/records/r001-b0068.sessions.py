# -*- coding: utf-8 -*-
"""批次 r001-b0068 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0068.sessions.py            # 写 out/r001-b0068.out.jsonl
  python3 records/r001-b0068.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0068"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0068.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "934a653a": {
  "analysis": {
   "question_context": "提问者问世界上是否有真正意义上的无价之宝（Q001，属提问者）。作者以肯定回答回应，自行给出无价之宝的两条判定条件并举例；P012 之后转为对一条批评意见的反驳。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接肯定存在无价之宝，并声明其需满足两个条件。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "条件一：价值恒久存在、每年产生新收益；作者称只要承认时间无限，价值即为无限。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "条件二：价值与时间呈复利关系，以逐年递增的价值序列表示。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "举例：物理定律、无时效限制且能指导实践的知识、历史均属此类。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P011"], "summary": "由上述条件推出无价之宝数量很多。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P012"], "summary": "强调前文论述不含文学性因素。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014", "P015"], "summary": "反驳把作者原话解释成弱版本、并据此断定作者不懂数学的说法。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上存在无价之宝，其需满足两个条件（价值恒久存在、价值与时间呈复利关系）。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要价值恒久存在且承认时间无限，该事物的价值自然就是无限的。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "物理定律、不具时效限制且能有效指导实践的知识属于此类事物；历史也是其中一大类，因为历史是永恒的。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "以上论述不含任何文学性因素（即非修辞夸张）。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述并反驳的对方说法：把作者的话解释成弱版本，称作者不懂（高中）数学，并认为恒久存在之物的影响会是收敛的。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把别人的话解释成弱版本、再拿它作为对方愚蠢的确据，这种行为模式容易出问题。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "先给出肯定判断：世界上有无价之宝（P001）。",
    "给出判定条件一：价值恒久存在、每年产生新收益（P003）。",
    "补充推论：只要承认时间无限，其价值即为无限（P004）。",
    "给出判定条件二：价值与时间呈复利关系，价值逐年递增（P005、P006）。",
    "说明同时满足者更是显而易见的无价之宝（P007）。",
    "列举例证：物理定律、无时效限制且能指导实践的知识、历史（P008—P010）。",
    "推出结论：据此可知有很多东西是无价之宝（P011）。",
    "声明前文不含文学性因素（P012）。",
    "转入反驳：指出对方把原话解释成弱版本并以此为其愚蠢的确据（P013—P015）。"
   ],
   "concept_usage": [
    {"term": "无价之宝", "meaning": "本文中由作者给出判定标准：价值恒久存在、每年产生新收益，且价值与时间呈复利关系的事物。", "evidence": "P002", "ambiguity": "两条条件是否必须同时满足，还是第一条成立时第二条自然成立，本文未说明。"},
    {"term": "复利关系", "meaning": "以 A1 < A2 < A3 逐年递增的价值序列表示的价值增长关系。", "evidence": "P006", "ambiguity": "只给出不等式序列，未给出函数形式或增长率限定。"},
    {"term": "时间无限", "meaning": "作者设定的前提，用以推出恒久之物的价值为无限。", "evidence": "P004", "ambiguity": "以“只要你承认”引入，属条件性前提，非无条件断言。"},
    {"term": "文学性的因素", "meaning": "作者称前文论述不含该因素，用以强调其表述是字面而非修辞。", "evidence": "P012", "ambiguity": "“文学性”的具体所指未界定。"}
   ],
   "examples_and_targets": [
    "物理定律、不具有时效限制的、能有效指导实践的知识——作者例证（P008）。",
    "历史——作者例证，并以“1840年打过鸦片战争”这一命题在1845年与2020年同样成立加以说明（P009、P010）。",
    "“捏出个梗来说明我不懂数学”“说这话的人不懂高中数学”“影响会是收敛的”——被作者反驳的对方说法，对方原话未引出（P013、P014）。"
   ],
   "conditions": [
    "“无价之宝只要满足两个条件”——作者给出的条件式界定（P002），但未说明两条是否都必要。",
    "“只要你承认时间是无限的”——价值无限性成立的前提（P004）。",
    "“不具有时效限制的、能有效指导实践的知识”——作者对知识类例证的限定（P008）。"
   ],
   "rhetoric_and_tone": "开篇以“当然”作直接肯定；中段用序数“第一/第二”与数学记法作说明性列举，并在 P012 强调“没有任何文学性的因素”。篇末 P013—P015 语气转为讥讽与训诫（“非要捏出个梗”“这种行为模式容易出问题啊”），连用“居然”表达不满，未点名批评对象。",
   "unresolved_questions": [
    "复利关系的严格含义（函数形式、增长率）本文未说明，仅有递增序列。",
    "被反驳者的原话在正文中未被完整引用，只能从作者转述推知，争论对象与语境不明。",
    "“1840年打过鸦片战争”作为历史命题的例子是否涉及时效性争议本文未展开；作者对“历史事件有时间属性、历史没有”的界定未给出更细限定。",
    "作者未说明第一条条件单独成立时是否已足以称为无价之宝，P007“更进一阶”的指向不明。",
    "P012 与 P013 之间存在一个字符位（chars 347—349）的空隙，原因不明，或为原文分段符/空行。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "无价之宝只要满足两个条件：", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "第一，其价值恒久存在，每年都会因为它而产生新的收益。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "只要你承认时间是无限的，这件东西的价值自然就会是无限的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "物理定律或不具有时效限制的、能有效指导实践的知识都属于这类事物。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "在1845年和在2020年都同样成立——其实历史是永恒的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "以上没有任何文学性的因素。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "很简单的东西，非要捏出个梗来说明我不懂数学。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "一种可以恒久存在的东西，居然有人会觉得它的影响会是收敛的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "把别人的话解释成弱版本然后拿来作为其愚蠢的确据", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["价值与价值判断", "数学（复利、收敛概念的使用）", "历史认识论"],
   "issue_candidates": ["是否存在无价之宝及其判定标准", "价值与时间的关系", "历史命题的恒久性", "对批评者误读的回应"],
   "text_function_candidates": ["答疑", "论证", "反驳"],
   "object_candidates": ["未具名的批评者", "鸦片战争（作为历史命题示例提及）"],
   "working_keywords": ["无价之宝", "复利", "时间无限", "收敛", "历史", "物理定律", "文学性"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问属提问者（Q001）；作者的肯定回答、两条判定条件与例证为其本人内容。P012 之后转入对批评意见的反驳，被反驳者身份与原文不可见。P012—P013 存在 1 字符定位空隙，骨架未标记结构分歧（divergence=false）。"
 },
 "b8b9016b": {
  "analysis": {
   "question_context": "提问者问知乎大V Patrick Zhang 退出知乎是否是知乎的一大损失、对知乎会产生什么影响（Q001，属提问者）。作者先用前二十段讨论“以人为中心考虑问题、把对某答案的反对扩大到该答主全部言行”的行为模式及风险，至 P022 才转向回答知乎是否受损的问题。正文未出现该大V姓名。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出观察：很多人喜欢以人为中心考虑问题，会因A问题的分歧跑到B问题下质问答主。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "展开例证：A问题未认错则B、C、D、E都成火力范围，甚至追查疑似匿名答案。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "指出该习惯的后果：对方须整个从你的领地消失；并以反问质疑其正当性。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "作出区分：反对某件事正常，扩大范围即直接攻击人；并警告要确保自己扛得住。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "给出理由：此类人的地位、影响力、资源与人脉常与对立面有数量级差异，触怒对方招致灾难性打击。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "断言这是作死玩火；说明虽人数众多但被随机选作典型即躲无可躲，末以反问收束。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017"], "summary": "结论：对事不对人、一事一议是保命的东西，违背者愚不可及。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "推论：不懂禁忌者被视为不值得投资的不安全资产，被实际绝交。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P022"], "summary": "回应提问：任何心智成熟、有实际工作经验、立意输出有效信息的人退出，对知乎对大众都是损失。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "反驳：有错误但言之有物的信息亦是收益，世界上根本没有正确信息，指对方以伪造的完美打压真实的次完美。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P027", "P028", "P029"], "summary": "以反问收束（有什么可自豪的、这样找得到男/女朋友么）。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人有一个奇怪的问题：喜欢以人为中心考虑问题，例如因对同一答主在A问题的答案不满而跑到B问题下质询。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种处世习惯意味着一个人若在一件事上没让你满意，就必须整个从你的领地消失，否则在其所有你够得着的事情上都会遭遇麻烦乃至袭击。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反对某件事是正常的，扩大范围就不是在反对这件事，而是直接攻击人。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "对这种行为无所顾忌的人，其社会地位、影响力、能动用的资源和人脉甚至谋略，往往与其对立面有数量级的差异。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "真正触怒对方会使问题变成没有尽头、你死我活、身份与肉体消灭的问题，给本人带来难以想象的压力和灾难。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对事不对人、一事一议不只是美德或一句老话，而是保命的东西；违背这条法则愚不可及。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不懂这点禁忌的人会被有实力的老江湖视为不值得投资的不安全资产，被实际绝交，想不栽跟头都难。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何心智成熟的、有实际工作经验的、立意输出有效信息的人，无论其提供的信息质量如何，退出对知乎、对大众都是损失。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "言之有物的有错误的信息一样是收益。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界上根本就没有正确信息，言之有物的有错误的信息就是人类能获得的最好极品，已经没有更好的一级。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述并反驳的对方立场：存在“没有错误的正确信息”，可据此打压“有错误的信息”。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑这样做的人：有什么可自豪的；并追问这样是否找得到男/女朋友。", "evidence": ["E15", "E16"]}
   ],
   "argument_steps": [
    "提出观察：很多人喜欢以人为中心考虑问题（P001）。",
    "举例：同一答主在两个问题下的答案被跨题追责，匿名答案也被侦察（P002—P004）。",
    "指出后果：对方必须整个从你的领地消失（P005），并以反问质疑其正当性（P006）。",
    "作出区分：反对某件事正常，扩大范围即攻击人（P007），并警告要确保自己扛得住（P008）。",
    "给出理由：此类人的资源常与对立面有数量级差异，触怒对方后果严重（P009—P011）。",
    "断言这是作死玩火，被随机选作典型即躲无可躲（P012—P014）。",
    "得出结论：对事不对人是保命法则，违背者愚不可及（P015—P017）。",
    "推论：不懂禁忌者将被视为不安全资产而遭实际绝交（P018—P021）。",
    "回应提问：合格的信息输出者退出对知乎与大众都是损失（P022）。",
    "反驳：错误信息亦是收益，所谓正确信息并不存在，对方以伪造的完美指责真实的次完美（P023—P026）。",
    "以反问收束（P027—P029）。"
   ],
   "concept_usage": [
    {"term": "对人不对事 / 对事不对人", "meaning": "作者以“一事一议”界定对事不对人；把因一事不满而扩大到对方全部言行称为对人不对事，即直接攻击人。", "evidence": "P007", "ambiguity": "标题作“对人不对事”（被批评对象），正文主张“对事不对人”（应然法则），二者为对照关系。"},
    {"term": "领地", "meaning": "指一个人能触及或施加影响的范围，作者以此描述冲突扩散的边界。", "evidence": "P005", "ambiguity": "为比喻用法，未给出判定标准。"},
    {"term": "安全资产 / 不安全资产", "meaning": "以投资语汇指称在他人眼中是否值得投入关系与机会的人；不懂禁忌者被认为不安全。", "evidence": "P018", "ambiguity": "判定条件（如“人生大难”）未细化。"},
    {"term": "言之有物的有错误的信息", "meaning": "内容有错但言之有物的信息；作者认为它仍是收益，且是人类能获得的最好一级。", "evidence": "P023", "ambiguity": "“言之有物”的标准与“错误”的判据本文均未给出。"}
   ],
   "examples_and_targets": [
    "知乎问题A、B、C、D、E——作者构造的说明性例子（P002、P003）。",
    "疑似同一答主的匿名答案被“火力侦察”——作者举例（P004）。",
    "俄罗斯轮盘赌与“一包烟”——作者类比与修辞（P017）。",
    "知乎大V退出知乎——提问者提出的语境（Q001）；正文仅以“这对知乎是不是损失”承接，未出现该大V姓名（P022）。",
    "作者批评的“你们”——以“没有错误的正确信息”打压有错误信息的人，身份未指明（P023、P026）。"
   ],
   "conditions": [
    "“一个人如果在一件事情上没能让你满意”——后果成立的条件（P005）。",
    "“你最好确保对方真的认真起来你扛得住”——警告所依赖的前提（P008）。",
    "“往往和ta的对立面有数量级的差异”——以“往往”限定（P009）。",
    "“任何心智成熟的、有实际工作经验的、立意输出有效信息的人”——作者对损失判断对象的限定（P022）。",
    "“无论其提供的信息质量如何”——排除信息质量作为条件（P022）。"
   ],
   "rhetoric_and_tone": "以训诫与警告语气为主，第二人称“你”直接对话读者；多处反问（P006、P014、P015、P027、P028、P029）；比喻与夸张并用（火力范围、火力侦察、领地、俄罗斯轮盘赌、一包烟、作死和玩火、“真的是不知死活”）；P023—P026 转为激烈论战口吻，指控对方是出于对权力的贪欲而策划的谎言。",
   "unresolved_questions": [
    "提问所指的知乎大V姓名在正文中未出现，作者是否针对该事件作答只能由 P022“至于说这对知乎是不是损失”间接判断。",
    "作者批评的“你们”具体指谁、是否为某类回答者，本文未说明。",
    "P028“这样找得到男/女朋友么？”的对象是否为前述行为者，只能由上下文推知，未明确点出。",
    "“世界上根本就没有正确信息”为强断言，其适用范围（是否限于社会议题、是否含数学与自然科学命题）本文未说明，属需研究者判断处。",
    "不安全资产的评估标准与“人一共能应付几个人”的规模依据本文未给出。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我发现很多人有一个很奇怪的问题，喜欢以人为中心考虑问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "有人不同意问题A里面的答案，常常就会跑到问题B下面质问答主问题A里的问题。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "这个人就必须整个的从你的“领地”里消失", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "你扩大范围，那就不是在反对这件事，而是在直接攻击人了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "往往和ta的对立面有数量级的差异", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "恐怕真正带来的是你自己的个人难以想象的压力和灾难。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P015", "quote": "对事不对人、一事一议，你以为只是美德而已吗？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "这是保命的东西。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "违背这条法则，等于为了一包烟报名参加俄罗斯轮盘赌，愚不可及。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "有实力的老江湖普遍认定你是目前不值得投资的不安全资产", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "无论其提供的信息质量如何，退出对知乎、对大众都是损失。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "言之有物的有错误的信息一样是收益。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "世界上根本就没有正确信息", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "冒充成了“没有错误的正确信息”来打压“有错误的信息”而已", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P027", "quote": "有什么可自豪的？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P028", "quote": "别的不说，这样找得到男/女朋友么？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会交往与人际冲突", "网络社区行为（知乎）", "信息与错误的认识论讨论"],
   "issue_candidates": ["对人不对事的行为模式及其风险", "对事不对人的必要性", "错误信息是否有价值", "是否存在正确信息"],
   "text_function_candidates": ["答疑", "训诫与警告", "论辩", "批评"],
   "object_candidates": ["知乎（平台）", "知乎大V（提问提及，正文未具名）", "匿名答主", "有实力的老江湖"],
   "working_keywords": ["对人不对事", "对事不对人", "一事一议", "火力范围", "安全资产", "言之有物的有错误的信息", "正确信息"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问（Q001）所指的具体人物与事件未在正文出现，作者对提问的直接回答集中在本篇后段 P022 起；P001—P021 为一般化的行为模式讨论，不能当作对具体事件的陈述。P023—P026 的反驳对象身份未指明。"
 },
 "bb625dfd": {
  "analysis": {
   "question_context": "提问者问电车难题是否有正义的解决方式，若有则基于怎样的正义（Q001，属提问者）。作者不以“正义”为框架作答，而是主张电车难题时时刻刻摆在每个人面前，并把掌权者的伦理责任（必须选择、必须负罪、不可推脱）作为答案，最后附言劝人不要追求权力。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开篇定调：追求出人头地者须先读明白，不要抱侥幸。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "电车难题并非远事：每个人不是扳闸者就是被绑者，或同时皆是，没有人不被卷入某个决定。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "断言害就是一种杀，伤也是一种死。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "举例：城市规划者、政策制定者、企业管理者的决定直接改变他人命运。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016"], "summary": "你总要选择、常在选让谁受损；以greater good为由与扳道工的理由无异（反问）。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "唯一健康的态度是对选择永怀歉疚；选择将来总会被证明出于幼稚和傲慢。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "你确实是凶手、确实负有责任，受害者家人的责怪并不冤枉。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "承认罪的伦理存在才有资格继续掌权；不承认者将陷入认知失调并最终大败。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028"], "summary": "给出唯一答案的表述，并称只有最温柔的人甘愿领受这份折磨。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "作者只肯把决定自己命运的权柄交给会愧疚者，不追随为扳道工脱罪的理论及其赞同者。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P033", "P034"], "summary": "人的全部努力首先是为了逃脱这样的人，这已反向决定了电车难题的答案。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P035", "P036", "P037", "P038"], "summary": "不选此答案者不配掌任何权，将被一切关系流放，走向死亡。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P039", "P040", "P041"], "summary": "结论：答案只有一个，无论选什么必须负罪不可推脱，只有不推脱者可得宽免。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P042", "P043", "P044", "P045"], "summary": "附言：不要追求权力，除非做好心理准备；觉得权力荣耀抵得过折磨者会被权力吞噬。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "电车难题摆在每一个人面前，本质上人不是那个扳闸的，就是被困在铁轨上的，或同时皆是。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有人没被牵涉到某个决定之中：不是下决定的人，就是被下决定的对象之一。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "害就是一种杀，伤也是一种死。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "规划者、政策制定者、企业管理者的一纸一行决定了他人的处境，他们总要选择、常常是在选让谁受损。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "作者以反问质疑的立场：以greater good为理由说明自己的选择是正当的（作者问这与电车难题扳道工的理由有何不同）。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "行使必定牵涉他人命运的权力，唯一健康的态度是对自己的选择永怀歉疚。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "你的选择在将来总是会被证明出于某种当时没察觉或不承认的幼稚和傲慢；你确实是一名凶手，确实对受害者的死亡负有责任。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "承认这罪的伦理存在，才有资格得到怜悯去继续执掌权限。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不承认罪责、自以为功或英雄者，会陷入难以实事求是的认知失调，最终必将大败。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "唯一能长期掌权而不受权力诅咒、保住心理健康与心灵平静的答案，只能是承认对不起受害者、理由苍白且无力补偿。", "evidence": ["E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有最温柔的人才能甘愿领受这份折磨；作者只肯把选择自己命运的权柄交给会真的愧疚负罪的人。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要有得选择，作者不会追随发明理论为扳道工的选择脱罪的人及其赞同者，因为这样的人不配决定作者的命运。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的全部努力首先都是为了不至于沦落到这样的人手中；人性中这一点不接受、不甘愿已反向决定了电车难题的答案。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "凡不选这答案的皆不配掌权；这类人将在事实上不被欢迎参与任何可能影响他人命运的决定，走向被一切关系流放乃至死亡。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：理论随人说，答案其实只有一个；无论选什么都必须负罪、不可推脱，只有不推脱的人可以得宽免。", "evidence": ["E27", "E28", "E29"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要追求权力，除非对此做好心理准备；觉得权力荣耀抵得过折磨的都会被权力吞噬。", "evidence": ["E30", "E31"]}
   ],
   "argument_steps": [
    "开篇要求追求出人头地者先读明白，不要抱侥幸（P001、P002）。",
    "把电车难题普遍化：每个人或是扳闸者或是被绑者，或同时皆是（P003—P006）。",
    "定义式断言：害就是杀，伤就是死（P007、P008）。",
    "以规划者、政策制定者、企业管理者为例说明决定改变他人命运（P009—P013）。",
    "指出选择不可避免，并以反问否定用greater good为自己开脱（P014—P016）。",
    "提出唯一健康的态度是永怀歉疚，并预言选择终将被证明出于幼稚与傲慢（P017、P018）。",
    "断定掌权者确为凶手、确有责任（P019—P022）。",
    "以承认为罪责前提，推出不承认者必将大败（P023—P026）。",
    "给出唯一答案的表述与“最温柔的人”之说（P027、P028）。",
    "表明作者不愿把命运交给为扳道工脱罪者（P029—P032）。",
    "以人的全部努力在于逃脱这类人为理由，反推答案已被决定（P033、P034）。",
    "推出不选此答案者不配掌权、被关系流放（P035—P038）。",
    "收束为唯一答案与不可推脱的负罪（P039—P041）。",
    "附言劝止追求权力，除非做好心理准备（P042—P045）。"
   ],
   "concept_usage": [
    {"term": "电车难题", "meaning": "本文不限于原版思想实验，而指一切“必须让某人受损”的选择处境，人人身处其中。", "evidence": "P004", "ambiguity": "作者未讨论该思想实验的原始设定与各种变体，直接作普遍化使用。"},
    {"term": "greater good", "meaning": "作者转述的选择理由（为多数人利益而牺牲少数人），并以反问否定其能为自己脱罪。", "evidence": "P016", "ambiguity": "未指明该说法出自何种理论或何人之口。"},
    {"term": "罪 / 负罪", "meaning": "作者要求掌权者承认的伦理责任：选择导致他人受害即负有责任，不可推脱。", "evidence": "P023", "ambiguity": "文中兼用伦理与宗教语汇（怜悯、宽免、地狱之门），未说明是修辞还是宗教框架。"},
    {"term": "权力诅咒 / 权力吞噬", "meaning": "长期掌权者若不承认负罪而自以为立功，将被权力吞噬并走向大败。", "evidence": "P044", "ambiguity": "机制描述为心理与关系层面的连锁后果，未给出可检验的限定。"},
    {"term": "流放", "meaning": "被一切关系不由自主地排斥，作者称这等于曲折地走向死亡。", "evidence": "P038", "ambiguity": "“人是社会关系的总和”一语被直接使用，未注明出处或界定。"}
   ],
   "examples_and_targets": [
    "城市的规划者（红线一歪）、政策制定者（两掌宽一张纸）、企业管理者（一行小字）——作者例证（P009、P011、P013）。",
    "greater good——被作者以反问质疑的选择理由（P016）。",
    "被单独绑在铁轨上的牺牲者——作者类比，用于指代因决定而受伤受害的人（P018）。",
    "发明理论为扳道工的选择脱罪的人、赞同他们的人、尝试而未成功的人——作者的拒斥对象（P031）。",
    "阿谀奉承的寄生者的吹捧（“王霸之气”）——作者反驳的他人说法（P025）。"
   ],
   "conditions": [
    "“只要有得选择”——P031 拒斥追随对象的前提。",
    "“凡掌权，必定时时刻刻要面对电车难题”——作者断言该问题的适用范围（P027）。",
    "“不要追求权力，除非你对此做好心理准备”——附言中的例外条件（P042）。",
    "“无论你选什么，你都必须负罪”——选择内容不影响负罪要求（P040）。",
    "“哪怕是微不足道的影响”——P036 对涉他决定范围的放宽限定。"
   ],
   "rhetoric_and_tone": "训诫与布道式语气，第二人称“你”贯穿全篇；大量短句排比（“每时每刻、每分每秒”“大到国家社稷、小到一家一户”）；连续反问（P010、P012、P016）；使用宗教语汇（罪、怜悯、宽免、地狱之门向你敞开、“我实实在在的告诉你们”）；结尾以英文“Yet another poetic irony.”收束，带反讽意味。",
   "unresolved_questions": [
    "提问以“正义”为问法（是否有正义的解决方式、基于怎样的正义），作者全篇未使用“正义”一词作答，是否构成对提问的直接回答需研究者判断。",
    "greater good 未指明出处、理论或主张者；P025 提到的“阿谀奉承的寄生者”也未指明对象。",
    "P006“你灵魂和命运也甚稀薄”语义含混，疑有脱字或省略，无法确定确切所指。",
    "宗教语汇（罪、地狱、宽免、得祝福得平安）属修辞还是作者的宗教框架，本文未说明。",
    "作者自称“我不会追随……的人”，其中“追随”的语境（现实政治或一般关系）未界定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "其实本质上你不是那个扳闸的，就是被困在铁轨上的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "或者同时皆是。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "没有人没被牵涉到某个决定之中，你不是下决定的人，就是被下决定的对象之一。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "害就是一种杀，伤也是一种死。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "你是城市的规划者，红线一歪，就有人无德无能上天堂，有人流血流汗下地狱，", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "你是政策制定者，两掌宽一张纸，就有人白忙一生，有人鸡犬升天，", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "你总是要选，你的选择并不总是幸运到无人受伤。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "但这跟电车难题的扳道工的理由有什么不同？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "唯一健康的态度，就是对自己的选择永怀歉疚。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "你的选择在将来总是会被证明是出于某种当时自己没察觉", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "你确实是一名凶手。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "你确实有责任，你确实对这人的死亡负有责任。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "你承认这罪的伦理存在，你才有资格得到怜悯去继续执掌这个权限。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "那么地狱之门就此向你敞开。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "你不可避免的要陷入一种很难再实事求是的认知失调之中", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "最后你必将大败。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "唯一能长期掌权而不受权力诅咒、保住心理健康、心灵平静、并最后有望得祝福、得平安的结局的答案", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "只有最温柔的人，才能甘愿领受这份大部分人都会齐声帮ta开脱的折磨。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P030", "quote": "而不是得意洋洋自以为立功的“人”手中。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P031", "quote": "我不会追随那些发明任何理论去为扳道工的选择脱罪的人", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P032", "quote": "因为这样的人，不配决定我的命运。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P033", "quote": "其实人的全部努力，首先都是为了不至于沦落到这样的人手中", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P034", "quote": "其实已经反向的决定了电车难题的答案。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P035", "quote": "凡不选这答案的，皆不配掌权。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P036", "quote": "大到国家社稷、小到一家一户，任何权都不配掌。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P038", "quote": "人是社会关系的总和，被一切关系不由自主的流放，就是曲折的走向死亡。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P039", "quote": "所以，理论随人去说，答案其实只有一个。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P040", "quote": "无论你选什么，你都必须负罪，不可推脱。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P041", "quote": "只有不推脱的人，可以得宽免。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P042", "quote": "不要追求权力，除非你对此做好心理准备。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P044", "quote": "觉得物有所值的，都会被权力吞噬。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学（选择与责任）", "政治哲学（权力与掌权者责任）", "思想实验的通俗化讨论"],
   "issue_candidates": ["电车难题是否有正义解法", "掌权者的伦理责任与负罪", "功利主义式理由（greater good）的正当性", "权力对人的影响"],
   "text_function_candidates": ["答疑", "训诫", "论辩", "说理散文"],
   "object_candidates": ["掌权者/领袖", "城市规划者", "政策制定者", "企业管理者", "被牺牲者", "为扳道工脱罪的理论发明者"],
   "working_keywords": ["电车难题", "扳道工", "greater good", "负罪", "歉疚", "权力诅咒", "流放", "王霸之气"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问属提问者（Q001）；作者未采用“正义”框架，而以负罪与不可推脱作答，作答方式的转换已在 unresolved_questions 登记。P031—P033 的“这样的人/追随”指向为作者主观立场表述，非对提问者的转述。"
 },
 "38180b82": {
  "analysis": {
   "question_context": "提问者问“无法和别人太过亲近该怎么办”（Q001，属提问者）。作者不直接给建议，而是先要求给出测量亲密程度的方法并按极值确定最佳策略，随后自建“亲密量”（亲密度对关系存续时间的积分）模型，推出亲密关系存在红线，红线之上为“狎”、之下为“亲密不足”，并反问提问者其问题在红线哪一侧。文末标“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "先提问题（最亲能有多亲）并要求给出亲密程度的测量/标定方法，据此求极值定策略。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "请读者先在评论区作答，作者随后给出自己的看法。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "提出基本概念“亲密量”：亲密度对亲密关系存续时间的积分。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "举例：与小超市老板1rw、累计互动30小时，亲密量为30rwh。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "举例：与同桌好友平均50rw、三年计得270000rwh；闹别扭期间按翻白眼的强度计。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "说明用功率单位的原因：关系强度以输出功率衡量，如同车辆爬坡；该部分暂不展开。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020"], "summary": "关系总量与存续时间正相关；极值取决于强度与强度可持续的时间。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022", "P023"], "summary": "以“金风玉露一相逢”与同桌对比；时间只计互动时间，隔海三十年只算15分钟。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "跨过某些线就注定不能长久，总量不增反降；与总量极值对应的是关系本该有的极限，再往前迈实为抛弃。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "亲密的极限是“永远”；超过限度的亲密消耗损害关系，老话称之为“狎”。", "role": "definition"},
    {"unit_id": "U011", "paragraph_refs": ["P032", "P033"], "summary": "行动建议：红线下的亲密不足可追求改进并归因于自身；红线上的亲密不要羡慕，要消除对诱惑的瘾。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P034", "P035", "P036"], "summary": "反问提问者其问题在红线哪一侧，并声明红线位置与“狎”的定义待续。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要有效谈论该问题须先提出“亲密量”概念：亲密量即亲密度对亲密关系存续时间的积分。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "亲密关系强度是用输出功率来衡量的量；人依靠亲密关系对抗外力侵袭，犹如车辆爬坡。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关系的总量与它存续的时间直接正相关。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人和人最亲密能有多亲密这个极值，不仅取决于关系强度（瞬间功率），还取决于这种强度能持续多久。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "时间只计算互动的时间：隔海相望三十年只通两封信，只能算15分钟而不能算30年。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "跨过某些线就注定不能长久，不能长久则总量会不增反降；与总量极值对应的是亲密关系本该有的极限，再往前迈实为抛弃。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "亲密的极限不是耳鬓厮磨，而是“永远”。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "某些超过限度的亲密是对关系的消耗和损害，感受上可能令人陶醉，但很可能埋下长期问题并在远期演变为关系灾难。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种超过红线的亲密，老话叫做“狎”。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没到红线的亲密不足可以追求改进，可以认为是你自己的感情能力不足；过了红线的不必羡慕，应通过观察和思辨消除瘾，而不是到处问怎么获得满足。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问提问者：其“无法和人太亲近”的问题在红线上还是红线下。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "红线在哪里、什么叫做“狎”，本篇未给出，作者标记为未完待续。", "evidence": ["E15", "E16"]}
   ],
   "argument_steps": [
    "先提出“人跟人最亲能有多亲”的问题，并要求先给出测量亲密程度的方法（P001—P005）。",
    "邀请读者先作答，随后提出作者自己的看法（P006、P007）。",
    "定义“亲密量”＝亲密度对关系存续时间的积分（P008、P009）。",
    "以与小超市老板的关系算出30rwh（P010—P012）。",
    "以与同桌好友的关系算出270000rwh，并说明闹别扭期间按该期间强度计（P013、P014）。",
    "解释采用功率单位（瓦特）的理由：强度即输出功率，如车辆爬坡（P015—P017），并声明暂不展开（P018）。",
    "推出总量与存续时间正相关（P019）。",
    "推出极值取决于强度与可持续时间（P020）。",
    "以“金风玉露一相逢”与同桌对比，限定时间只计互动时间（P021—P023）。",
    "推出红线：跨线不能长久、总量不增反降，极值对应关系极限，再往前即抛弃（P024—P027）。",
    "给出亲密极限的判断（“永远”）与越线之“狎”的命名（P028—P031）。",
    "给出行动建议：线下可改进，线上不必羡慕（P032、P033）。",
    "反问提问者所处位置，并说明红线与“狎”的定义待续（P034—P036）。"
   ],
   "concept_usage": [
    {"term": "亲密量", "meaning": "作者自建的量：亲密度对亲密关系存续时间的积分；用于比较不同关系的总量。", "evidence": "P009", "ambiguity": "积分形式与量纲未严格给出，仅在例证中按强度×小时估算。"},
    {"term": "rw（relationship watt 关系瓦特）/ rwh", "meaning": "作者自拟的强度单位与总量单位；1rw 以与小区门口小超市老板每天买包烟的关系为参照。", "evidence": "P010", "ambiguity": "参照点为主观设定，未说明如何测量或标定不同关系的rw值。"},
    {"term": "关系的总量", "meaning": "作者称可理解为份量或能量，与存续时间直接正相关。", "evidence": "P019", "ambiguity": "“份量还是能量”两种理解并存，作者未择一。"},
    {"term": "红线 / 极限", "meaning": "与总量极值相对应的亲密上限，越过即总量下降，老话称“狎”。", "evidence": "P025", "ambiguity": "红线的具体位置本篇未给出，作者明确标为待续。"},
    {"term": "狎", "meaning": "作者引老话，指超过红线的亲密。", "evidence": "P031", "ambiguity": "定义留到续篇，本篇只有命名。"},
    {"term": "亲密不足", "meaning": "未到红线的亲密状态，作者认为可追求改进并归因于自身感情能力。", "evidence": "P032", "ambiguity": "与“无法和人太亲近”的对应关系由作者以反问提出，未判定。"}
   ],
   "examples_and_targets": [
    "小区门口小超市老板，每天买包烟、五年、累计互动30小时——作者构造的计量例证（P010—P012）。",
    "同桌好友，三年、平均50rw、算出270000rwh——作者构造的计量例证（P013）。",
    "闹别扭期间按“翻白眼的亲密强度”计算——作者的说明性补充（P014）。",
    "车辆爬坡与发动机功率——作者类比（P016）。",
    "“金风玉露一相逢”，设1000rw、持续30天、计30000rw——作者引用的成句并自设数值（P021）。",
    "隔海相望三十年只通两封信——作者构造的反例，用来说明时间只计互动（P023）。"
   ],
   "conditions": [
    "“假设有一种关系的亲密强度是1rw”“假设这个亲密度是平均50rw”——作者的建模假设（P010、P013）。",
    "“这个时间只计算了互动的时间”——计量口径的限定（P023）。",
    "“跨过了某些线，就注定不能长久”——红线后果的适用条件（P025）。",
    "“只要有得选择”不适用；本篇相关限定为“没到红线的……你可以追求改进”（P032）。",
    "“很可能在某方面令人陶醉，但也很可能会……演变成……关系灾难”——以双重“很可能”限定（P030）。"
   ],
   "rhetoric_and_tone": "以建模与物理单位作类比展开，语气偏教学式、带自造术语的玩笑感（relationship watt/关系瓦特、翻白眼的亲密强度）；P006 邀请读者在评论区先答，形成互动式结构；末段以反问结束并把定义留到续篇（“未完，待续”）。整体不训诫，收束带悬念。",
   "unresolved_questions": [
    "红线具体位置与“狎”的定义本篇未给出，作者标“（未完，待续）”，续篇是否存在需另行核查。",
    "P021 将1000rw持续30天计为30000rw，与 P013 按“一天10小时”累计小时数的算法口径不一致，本文未说明该处以何种时间口径计。",
    "rw 值如何测量或标定（除小超市老板这一参照点外）本文未说明，模型的量纲一致性无法判断。",
    "P005 要求“按照你的方法求极值，根据这个极值来确定最佳策略”，但正文未给出统一的最佳策略表述，只在 P032、P033 给出分侧建议。",
    "“亲密量”能否跨关系比较（不同关系类型的rw是否可通约）本文未说明。",
    "P036 标“未完，待续”，本篇属未完成文本，全文结构无法回看。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P008", "quote": "为了能有效地谈论这个问题，我们首先提出一个基本概念——亲密量。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P009", "quote": "亲密量即亲密度对亲密关系存续时间的积分。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P016", "quote": "因为亲密关系的强度是一种用输出功率来衡量的量。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P019", "quote": "是和它存续的时间直接正相关的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P020", "quote": "还取决于这种强度的亲密能持续多久。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P023", "quote": "这个时间只计算了互动的时间", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P025", "quote": "跨过了某些线，就注定不能长久。不能长久，总量会不增反降。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P026", "quote": "与那个总量极值所对应的，就是亲密关系本该有的极限。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P028", "quote": "亲密的极限，不是耳鬓厮磨，而是“永远”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P030", "quote": "某些超过这个限度的亲密，是一种对关系的消耗和损害。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P031", "quote": "这种超过红线的亲密，老话就叫做“狎”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P032", "quote": "没到红线的“亲密不足”，你可以追求改进", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P033", "quote": "过了红线的那些亲密不要羡慕，不要受诱惑。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P034", "quote": "到底是在红线上还是红线下，你想好了吗？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P035", "quote": "那么，这些红线在哪？什么叫做“狎”？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P036", "quote": "（未完，待续）", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系/亲密关系", "类比建模（借用物理量）", "伦理与自我修养建议"],
   "issue_candidates": ["亲密程度的测量", "亲密关系是否存在上限", "越界亲密（狎）的危害", "亲密不足与无法亲近的区分"],
   "text_function_candidates": ["答疑", "概念建模", "说理", "互动式写作"],
   "object_candidates": ["提问者（无法和人太亲近者）", "小区门口小超市老板", "同桌好友", "读者（被邀在评论区作答）"],
   "working_keywords": ["亲密量", "关系瓦特", "rw", "rwh", "极值", "红线", "狎", "亲密不足", "永远"]
  },
  "notes": "本篇无图片节点，正文完整可读；文本自带“（未完，待续）”标记，属作者明示的未完成篇，本次按现有正文完整阅读并记录。提问属提问者（Q001），作者未直接判定提问者的处境在红线哪一侧，而以反问收束。P021 的计量口径与 P013 不一致，已登记为未决问题，未据此改写作者原意。"
 },
 "2a91b754": {
  "analysis": {
   "question_context": "提问者问“你一旦辞职了，好像任何人都不认识你了，是真的吗”（Q001，属提问者）。作者未直接判定该说法真假，而是区分“做员工”与“认准老大跟团队”两种关系，主张做员工时应避免与同事的私人交往、以工作效能和职业伦理立足，并把“离职后没人理会”的解决方向限定为展现工作效能与职业伦理水平。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出全文的区分：入职做员工与认准老大跟团队是两码事。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "理由：企业有流程架构，忌讳员工间超出工作关系的关系；并举例会计/出纳/预算主管、生产/质检。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "展开风险：恋爱、联姻、借贷、担保、合伙等会扭曲工作关系，甚至招致性骚扰类罪名；隐形竞争使人无谓受伤。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "正面主张：同事间最好的关系是靠能力与职业精神赢得看重；行动要求：不要称兄道弟、拉帮结派、搞攻守同盟。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "后果推演：有实力创造更好前途者的警觉会使你少获内推offer，职业生涯提升变慢。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "预测：未来商业模式是项目式的，升职关键人物是现在的同事、师傅与teamleader；赢得关注靠工作效能与职业伦理，而非下班混熟。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013"], "summary": "反例：创业只拉酒肉同事者出于对自身能力不自信，其项目大概率前景不好。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015", "P016"], "summary": "小结：做到上述即可在离职后获得机会，因为你是可被拉拢的资源。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018", "P019"], "summary": "转入第二种关系：跟老大、加入核心团队是更深的合伙关系（期权、决策权、独当一面），会涉及私人交往。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P020", "P021"], "summary": "举例：唐顿庄园的主仆关系；但无论如何专业关系仍然优先。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P022", "P023", "P024"], "summary": "结论与行动建议：解决“离职没人理会”只能靠工作效能与职业伦理；走混熟一路只解决症状，等着的恐怕是被再宰一刀的盘算，并以反问收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "入职做员工，和认准了老大跟团队是两码事。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做员工时，其他员工最好不要有私人交往，因为企业有流程架构，比较忌讳员工之间有超出工作关系的其他关系。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "同事之间的恋爱、联姻、借贷、担保、合伙等关系交往一个不好手一滑就会扭曲工作关系，弄不好瞬间可能有性骚扰这类罪名落到头上。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "同事之间的最好关系是通过高度的能力和职业精神赢得所有人的看重。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要称兄道弟、拉帮结派，不要搞攻守同盟之类的各种小动作。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述行为不是拉近关系以便工作，而是自绝生路，因为真有实力创造更好职业前途的人看到这些行为会警觉三分。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "对你警觉三分、对别人警觉两分，将来收到内推offer的就是别人而不是你，职业生涯提升自然就慢。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "将来的商业模式里一切都会是项目式的，岗位本质上围绕项目存在而极少再围绕公司职能存在。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "将来让你升职的大概率是你现在的同事、师傅和teamleader，而不是现在公司的老板。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "得到他们关注和在意的最好办法是高度的工作效能和严密的职业伦理自觉，绝不是下班多在一起混熟。", "evidence": ["E10", "E11"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "创业时只拉酒肉欢歌的同事的人，其选择出于对自身管理与专业能力不自信，这样的人无论创业还是新项目大概率前景不好。", "evidence": ["E12", "E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "只要做到以效能和职业伦理立足，离职之后自然有人给你机会，因为你是个资源、拉到你就是赚到。", "evidence": ["E14", "E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "跟老大、加入核心团队是另一码事：不是工资关系，而是准备给期权、决策权、独当一面的委任或培养机会的更深的合伙关系，会涉及私人交往。", "evidence": ["E16", "E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种关系有样本，比如《唐顿庄园》里的主仆关系，既保持专业、又有不明言的私人感情；但专业关系仍然优先。", "evidence": ["E18", "E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若认为离职后没人理会是需要解决的问题，解决方向不可以是混成哥们或闺蜜，只能是展现工作效能和职业伦理水平。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "走混熟这条路只能解决没人理会的症状，等着你的恐怕都是还可以再宰一刀的盘算。", "evidence": ["E21"]}
   ],
   "argument_steps": [
    "提出区分：做员工与跟老大/团队是两码事（P001）。",
    "给出理由：企业流程架构忌讳工作关系之外的关系，并举例说明（P002）。",
    "补充风险：同事间恋爱、借贷、担保等会扭曲工作关系，且同僚有隐形竞争（P003、P004）。",
    "提出正面标准：以能力与职业精神赢得看重；要求不称兄道弟、不搞攻守同盟（P005、P006）。",
    "推出后果：有实力者警觉导致内推机会旁落、职业提升变慢（P007、P008）。",
    "以未来项目式商业模式为理由，指出升职关键人物与赢得关注的方式（P009—P012）。",
    "以“创业只拉酒肉同事”为反例（P013）。",
    "小结：如此则离职后有人给机会，因为你是资源（P014—P016）。",
    "转入第二种关系：跟老大、入核心团队属合伙关系，会涉及私人交往（P017—P019）。",
    "举《唐顿庄园》主仆关系为样本，并保留专业优先（P020、P021）。",
    "给出结论与行动方向，并以反问收束（P022—P024）。"
   ],
   "concept_usage": [
    {"term": "做员工 / 认准老大跟团队", "meaning": "作者用这组区分把职场关系分为工资-职能关系与更深合伙关系，两类的私人交往尺度不同。", "evidence": "P001", "ambiguity": "两类关系的边界与转化条件未给出明确判据。"},
    {"term": "职业伦理（职业伦理自觉/水平）", "meaning": "作者视为赢得同事看重与他人投资的核心品质之一，与工作效能并列。", "evidence": "P011", "ambiguity": "具体内容（保密、尽责等）本文未列举。"},
    {"term": "资源 / 资产", "meaning": "以可被他人拉拢获利的对象来描述有能力的员工，作者据此解释离职后仍有人给机会。", "evidence": "P016", "ambiguity": "“拉到你就是赚到”的衡量标准未给出。"},
    {"term": "合伙关系", "meaning": "跟老大、入核心团队所对应的关系：以期权、决策权、独当一面的委任为标志。", "evidence": "P018", "ambiguity": "与普通雇佣关系的界线及私人交往的限度未量化。"}
   ],
   "examples_and_targets": [
    "会计、出纳、预算主管下班一起唱K；生产与质检亲如姐妹——作者构造的例子（P002）。",
    "同事之间的恋爱、联姻、借贷、担保、合伙——作者列举的风险场景（P003）。",
    "只拉酒肉欢歌同事的创业者——作者的反例（P013）。",
    "《唐顿庄园》里的主仆关系——作者引用的作品样本，用以说明既专业又有不明言私人感情的关系（P020）。",
    "“将来”的项目式商业模式与升职路径——作者的预测性叙述（P009、P010）。"
   ],
   "conditions": [
    "“因为企业有流程架构”——私人交往禁忌成立的组织前提（P002）。",
    "“弄的不好瞬间可能会有性骚扰这类的罪名落到你头上”——以“弄的不好”为条件（P003）。",
    "“尤其是同僚之间常有隐形的竞争关系”——限定竞争场景（P004）。",
    "“大概率”出现两次（P010、P013），均用于未来预测的限定。",
    "“只要你做到了这样，离职之后自然有人给你机会”——P015 的前置条件。",
    "“这种就不是工资关系，而是准备给你期权……”——第二种关系的成立条件（P018）。"
   ],
   "rhetoric_and_tone": "教训与经验总结口吻，短句加祈使句（不要称兄道弟、好自为之）；以“你”直接对话；用反问收尾（“你确信更好吗？”）；以利弊推演而非道德说理展开，语气务实、略带警告。",
   "unresolved_questions": [
    "提问问“辞职后好像任何人都不认识你了，是真的吗”，作者未直接判定该说法真假，只给出解决方向，是否为回答需研究者判断。",
    "P010 原文作“你你现在的同事”，有一处重复字，疑为录入或原稿笔误，未作改动。",
    "P023 的引号不配对（“没人理会“、“还可以再宰一刀“），原文如此，引用时照录。",
    "《唐顿庄园》主仆关系的具体所指与适用限度，本文未展开，属需外部核查的作品内容。",
    "“将来”的时间范围与依据未说明；P009 对项目式商业模式的预测属作者判断，非既成事实。",
    "“性骚扰这类的罪名”所指的具体情形与法律语境本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "入职做员工，和认准了老大跟团队是两码事。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "做员工，其他员工最好不要有私人交往。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "弄的不好瞬间可能会有性骚扰这类的罪名落到你头上。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "同事之间的最好关系就是通过高度的能力和职业精神赢得所有人的看重", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "不要称兄道弟、拉帮结派，不要搞攻守同盟之类的各种小动作。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "因为真有实力给你创造更好的职业前途的人，看到这些行为都会对你警觉三分。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "将来收到内推offer的就是别人而不是你。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "将来的商业模式里一切都会是项目式的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "将来让你升职的大概率是你你现在的同事、师傅和teamleader，而不是现在公司的老板。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "是高度的工作效能和严密的职业伦理自觉。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "绝不是“下班多在一起混熟”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "所以要靠“熟”“亲热”来带给自己心理安全感。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "大概率前景不好。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "只要你做到了这样，离职之后自然有人给你机会。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "你是个资源，拉到你就是赚到", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "而是准备给你期权、给你参与决策权、给你独当一面的委任或者向这方向发展的培养机会的更深的合伙关系。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "这的确会涉及到一些私人交往", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "比如唐顿庄园里的主仆关系，就是既保持专业、又有不明言的私人感情的关系。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "但无论如何，专业关系仍然优先。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "那么解决的方向不可以是“混成哥们/闺蜜”，而只能是展现工作效能和职业伦理水平。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "你解决了“没人理会“的症状", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场关系与职业发展", "组织管理（流程架构与内控）", "人际边界与风险管理"],
   "issue_candidates": ["离职后人际关系是否失效", "员工间私人交往的利弊", "以能力还是以私交立足", "跟老大/入核心团队的合伙关系"],
   "text_function_candidates": ["答疑", "经验总结", "建议（训诫式）", "预测"],
   "object_candidates": ["员工/同事", "老板", "师傅与teamleader", "创业者", "《唐顿庄园》主仆（引用）"],
   "working_keywords": ["人走茶凉", "私人交往", "职业伦理", "内推offer", "项目式", "期权", "合伙关系", "资源"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问（Q001）属提问者；作者未直接判定“辞职后没人认识你”真假，而以关系分类和行动方向作答。P010 有重复字“你你”，P023 引号不配对，均为原文形态，引用时照录、未改写。"
 },
 "39a005c0": {
  "analysis": {
   "question_context": "提问者问南方民居为什么流行白墙黑瓦、这种建筑审美的起源是什么、为什么北方不是这样（Q001，属提问者）。作者主张民居配色的主导要素是成本与实用性而非审美，逐项解释石灰与黑瓦的成因，并反驳知乎用户@陆土根“顾左右而言他”的指责，说明别处不用该配色的原因。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总主张：民居配色的主导要素一般是成本和实用性，不是审美。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "分项解释：刷石灰防潮防霉且便宜可重刷；黑瓦源于最便宜的深灰色瓦在潮湿环境长苔藓而变黑。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "提出审美的来源：在该环境下适应久了，由对建筑群所体现生活的精神皈依而生的忠诚宣示。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "以假设的霸王龙与“霸王黄”作类比，说明颜色评价的从属性。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009"], "summary": "理由：古代选色极奢华——漆层厚、天然漆贵、矿物颜料稀缺、植物色素易褪色、附着力差且维护成本高。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012"], "summary": "推论：刷漆之物多属地位崇高者，一般东西没资格；往墙上刷更是奢华，或只能鎏金包金。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "小结：各地民居基本都是建材本色，雕梁画栋是富贵人家专属。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P015"], "summary": "引述@陆土根的指责：说作者“顾左右而言他”，理由是“别的地方就不是这个颜色”。", "role": "context"},
    {"unit_id": "U009", "paragraph_refs": ["P016", "P017"], "summary": "反驳：别的地方没这个需求或材料；北方要防冷不防潮，两广、吊脚楼、土楼、窑洞都无需刷白；并反问是否要拿近代化后的居民楼举例。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P018", "P019"], "summary": "反驳：“闽南民居大红大绿”多半指庙宇；红墙绿瓦非平民可用，用之属违制。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P020"], "summary": "以广州陈家祠为例：顶级民居也通体灰色，只是砖石规格高。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "基础民居配色的主导要素一般是成本和实用性，不是出于什么审美。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "刷石灰可以有效防潮防霉（主要是防霉），又便宜，每隔几年可以再刷一遍。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "黑瓦首先是瓦不加特别材料选择时最便宜最普通的深灰色瓦；变黑是时间久了潮湿环境下长了苔藓。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "审美是在这个环境下适应久了，由对该建筑群所体现生活的精神皈依所生发出来的一种忠诚宣示。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "假设霸王龙活着、长成泥巴黄，这个黄多半会被命名为“霸王黄”并被认为是超级牛的好颜色，说明颜色评价取决于处境。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代要“选色”很奢华：天然漆工艺复杂产量小、矿物性颜料色素稀缺不能大面积用于建筑、植物性色素易褪色变黑。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "除天然漆及鎏金、包金外，其它涂料附着力糟糕、易剥落，要不剥落须付出沉重维护成本。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "刷得油光水滑的往往是地位崇高的东西，一般的东西没资格刷漆；往墙上刷更是奢华。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "各地民居基本上都是最实惠合用的建材是什么颜色房子就是什么颜色，都是本色；专门雕梁画栋是富贵人家的专属选择。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引述的第三方指责（@陆土根）：说作者“顾左右而言他”，理由是“别的地方就不是这个颜色”。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问反驳：别的地方没这个需求或没这个材料，很难理解吗。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "北方要的是不冷而非防潮防霉；两广、吊脚楼、土楼、窑洞等居住形态也无需刷白。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问是否要拿最近一百年近代化之后修的“居民楼”来举例。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "“闽南民居就大红大绿”这类话多半说的是庙宇这类宗教建筑。", "evidence": ["E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "红墙绿瓦非平民可用，如果有，属于违制，足够杀头流放。", "evidence": ["E19"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "广州陈家祠已是顶级民居，也一样是通体灰色，只是砖石规格高一点。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "提出总主张：民居配色主导要素是成本与实用性，不是审美（P001）。",
    "分项给出石灰与黑瓦的成因（P002、P003）。",
    "提出审美的来源：环境适应与精神皈依下的忠诚宣示（P004）。",
    "以霸王龙/“霸王黄”的假设作类比（P005、P006）。",
    "以古代选色的材料与工艺成本作理由（P007—P009）。",
    "推出漆色为地位象征、墙面刷色更奢华（P010—P012）。",
    "小结各地民居为本色，雕梁画栋属富贵人家（P013、P014）。",
    "引述@陆土根的指责（P015）。",
    "以需求与材料差异反驳，并列举北方、两广、吊脚楼、土楼、窑洞（P016），反问是否以近代居民楼举例（P017）。",
    "反驳“闽南大红大绿”之说，指出应指庙宇，并说明红墙绿瓦属违制（P018、P019）。",
    "以广州陈家祠通体灰色收尾（P020）。"
   ],
   "concept_usage": [
    {"term": "审美", "meaning": "本文不把审美当作配色原因，而把它解释为对该环境下生活方式的适应与精神皈依所生的忠诚宣示。", "evidence": "P004", "ambiguity": "作者未否认审美存在，只否认它是民居配色的主导要素。"},
    {"term": "本色", "meaning": "最实惠合用的建材自身的颜色，作者以此概括各地民居的普遍配色状况。", "evidence": "P013", "ambiguity": "与“白墙黑瓦”是否为同一种“本色”未直接说明。"},
    {"term": "选色", "meaning": "指古代对建筑涂层颜色的主动选择，作者称之为很奢华的行为。", "evidence": "P007", "ambiguity": "引导内用法，未给出时代与阶层的适用范围。"},
    {"term": "违制", "meaning": "作者称红墙绿瓦非平民可用，若使用即属违制，可致杀头流放。", "evidence": "P019", "ambiguity": "所指具体朝代与法令本文未说明，属待外部核查的事实断言。"}
   ],
   "examples_and_targets": [
    "假设活着的霸王龙与“霸王黄”——作者假设性类比（P005）。",
    "琴、弓、梳妆盒、文具、鎏金、包金——作者列举的漆色使用对象（P010、P012）。",
    "@陆土根——作者引述并反驳的知乎用户（P015）。",
    "北方、两广、吊脚楼、土楼、窑洞——作者列举的反例地域与居住形态（P016）。",
    "最近一百年近代化之后修的“居民楼”——作者以反问质疑的举例对象（P017）。",
    "闽南民居“大红大绿”、庙宇——作者区分并反驳的说法（P018）。",
    "广州陈家祠、砖石规格——作者例证，属事实断言（P020）。"
   ],
   "conditions": [
    "“基础的民居的配色的主导要素一般是……”——以“一般”限定（P001）。",
    "“假设霸王龙活着”——明确的假设条件（P005）。",
    "“做漆器想要寿命好，漆层厚度怕不要几毫米”——以“怕不要”表达推测（P008）。",
    "“只有真正的富贵人家可以小小的用那么一点”——限定使用者（P008）。",
    "“如果有，属于违制”——以条件句表述（P019）。",
    "“多半说的是庙宇这类宗教建筑”——以“多半”限定（P018）。"
   ],
   "rhetoric_and_tone": "驳论语气，开篇即下判断并以材料与成本逐条立论；面对质疑时用连续反问反击（P016、P017），带较强对抗性与口语化调侃（“很遗憾，人类就这德行”“刷成白色嫌自己柴火太多么”“刷白干啥”）；以@提及方式直接回应批评者，结构上先是自述立论、后是逐条反驳。",
   "unresolved_questions": [
    "提问问的是“这种建筑审美的起源”，作者的回答重心在成本与实用性，并以 P004 给出审美来源的一种解释，是否正面回应“起源”需研究者判断。",
    "@陆土根的完整原话与争论上下文不可见，正文只引其一句指责，需回查知乎原帖。",
    "P017 以反问提出“最近一百年近代化之后修的居民楼”，作者未明确该对象是否属于其讨论范围。",
    "“红墙绿瓦非平民可用……足够杀头流放”与“广州陈家祠……通体灰色，只是砖石规格高一点”均属事实断言，涉及具体建筑史与制度史，待外部核查。",
    "“霸王黄”类比中作者未说明颜色命名与地位的关系是否普遍成立。",
    "作者未说明“白墙黑瓦”中“白”的石灰与“黑”的苔藓是否为同一维护周期内的共存状态。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "基础的民居的配色的主导要素一般是成本和实用性，不是出于什么审美。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "刷石灰可以有效防潮防霉（主要是防霉），又便宜，每隔几年就可以再刷一遍。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "是因为时间久了，潮湿环境下长了苔藓，颜色更深，于是看起来漆黑一片。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "审美是在这个环境下适应久了，由对这个建筑群所体现出来的生活的精神皈依所生发出来的一种忠诚宣示。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这个黄多半被命名为“霸王黄”，被认为是一种超级牛的好颜色。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "很遗憾，人类就这德行。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "顺便说一声，在古代要“选色”是很奢华的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "天然漆工艺复杂、产量很小，贵得要命。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "其它的涂料附着力都糟糕得很，涂上去没几个月就破了，剥落了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "刷得油光水滑的，往往都是地位崇高的东西", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "拿来往墙上刷，更是奢华得很", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "其实各地的民居基本上都是最实惠合用的建材是啥颜色，房子就是啥颜色，都是本色。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "这个绝对是富贵人家的专属选择。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "@陆土根在这说我“顾左右而言他”，理由是“别的地方就不是这个颜色”。", "relation": "context"},
    {"key": "E15", "paragraph_id": "P016", "quote": "别的地方没这个需求，或者没这个材料，很难理解吗？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "北方需要防什么潮、防什么霉？北方要的是不冷", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "还是说要拿最近一百年近代化之后修的“居民楼”来举例？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "多半说的是庙宇这类宗教建筑。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "红墙绿瓦非平民可用，如果有，属于违制，足够杀头流放了。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "也一样是通体灰色，只是砖石规格高一点而已。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["建筑史/民居建筑", "材料与工艺成本", "审美观念的社会成因"],
   "issue_candidates": ["南方民居白墙黑瓦的成因", "民居配色的主导要素是成本还是审美", "北方及其他地区为何不用该配色", "红墙绿瓦的使用限制"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "科普式解释"],
   "object_candidates": ["南方民居", "北方民居", "闽南民居", "庙宇/宗教建筑", "广州陈家祠", "@陆土根（知乎用户）", "富贵人家/平民"],
   "working_keywords": ["白墙黑瓦", "石灰", "苔藓", "本色", "选色", "违制", "雕梁画栋", "霸王黄"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问属提问者（Q001）。P015 为作者引述的第三方（@陆土根）指责，已按 quoted_or_cited + cited_source 单列，未归入作者主张。文中含若干建筑史与制度史事实断言（红墙绿瓦违制、广州陈家祠、闽南庙宇），初读不作外部裁决，已登记为待外部核查。"
 },
 "72feb2fa": {
  "analysis": {
   "question_context": "提问者问为什么人类喝地球的水需要过滤，而其他任何一种地球的生物可以直接喝地球的水（Q001，属提问者，其前提是其他生物可直接饮水）。作者否定该前提，说明动物也会择水而饮，并把差异归因于人类聚居方式改变了水源污染状况，而非动物的抵抗力更强。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "否定提问前提：动物也不会乱喝水，它们嗅觉灵敏，味道不对的水不喝。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "列举动物实际饮用的水（溪水/泉水、地下水、流速较快的河水、气味正常的湖水、露水、雨水）与不喝的水（枯枝败叶、有死老鼠的水坑水）。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "补充：植食动物大部分水分来自野生植物枝叶果实，几乎不需喝水；小片死水也不喝。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "理由：工业时代之前人口不稠密地区污染程度很低，动物不愁水喝。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "因果链：人类靠引水道、坎儿井、深井、运水车远离自然水源聚居，导致居住区水源污染程度可能较高且风险集中。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "由上述处境推出人类用加热或酿酒消毒的做法。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012"], "summary": "反向对照：人类可以喝动物栖居地的活水，而动物喝人类聚居地被污染的水反而受不了。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P013"], "summary": "结论：要害不在于动物的抵抗力，而在于水有所不同。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P014"], "summary": "补充例证：人类饲养动物喝的水一般特别净化过，房前屋后的水不敢让牲口乱喝。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "动物也不会乱喝水（否定提问所设定的“其他生物可以直接喝”这一前提）。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "动物嗅觉很灵敏，闻起来味道不对的水不会乱喝。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "动物一般会去喝溪水/泉水、地下水、流速较快的河水、气味正常的湖水，以及露水和雨水。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "掉满枯枝败叶、有死老鼠的水坑水与那种小片死水，动物是不喝的。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "还有很多植食动物的大部分水分直接来自野生植物的枝叶果实，几乎不需要喝水。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在工业时代之前，人口不稠密的地区污染程度很低，动物不愁水喝。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类自从发明引水道、坎儿井、深井、运水车等手段之后，实现了远离自然水源聚居。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "远离水源聚居反而使居住区水源污染程度可能比较高（井少、打水不规范、杂物或鼠虫掉入），且离河远、挑水消耗劳动力可能得不偿失。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以人类学会了用加热或者酿酒的方式来消毒。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "人类其实可以喝动物栖居地的那些活水，相对还是比较安全的。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "反而是动物若进入人类聚居地区、喝人类居住地那些多少被污染了的水，会受不了。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要害其实不在于动物有多大的抵抗力，而在于水有所不同。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "人类的饲养动物喝的水一般是特别净化过的，房前屋后的水不敢让牲口乱喝。", "evidence": ["E17"]}
   ],
   "argument_steps": [
    "先否定提问前提：动物也不会乱喝水（P001）。",
    "给出理由：嗅觉灵敏，味道不对的水不喝（P002）。",
    "列举动物饮用的水源类型（P003）。",
    "列举动物拒饮的水（水坑水、小片死水）（P004、P006）。",
    "补充植食动物的水分来源（P005）。",
    "给出历史条件：工业时代之前人口稀少地区污染低（P007）。",
    "给出因果链：人类以引水、蓄水手段远离自然水源聚居（P008），反使居住区水源污染风险集中（P009）。",
    "推出人类以加热或酿酒消毒（P010）。",
    "作双向对照：人可饮动物栖居地活水（P011），动物饮人类聚居地水会受不了（P012），并以饲养动物饮水佐证（P014）。",
    "得出结论：要害在于水有所不同，而非动物抵抗力（P013）。"
   ],
   "concept_usage": [
    {"term": "水有所不同", "meaning": "作者用来替换“动物抵抗力更强”的解释：差别在水的污染状况而非饮用者的体质。", "evidence": "P013", "ambiguity": "未给出水质判定的具体指标或阈值。"},
    {"term": "活水 / 死水", "meaning": "作者以“溪水/泉水、流速较快的河水”等指活水，以“小片死水”“掉满枯枝败叶的水坑水”指死水。", "evidence": "P003", "ambiguity": "未给出活水与死水的判定标准，属日常语用。"},
    {"term": "污染程度", "meaning": "用于比较地区与水源的洁净状况，作者以人口稠密度与取水方式解释其差异。", "evidence": "P007", "ambiguity": "“污染”所指为微生物、杂物还是化学污染，本文未区分。"},
    {"term": "消毒", "meaning": "作者举加热与酿酒两种方式，作为人类应对聚居区水质的办法。", "evidence": "P010", "ambiguity": "未说明这两种方式是否等同于现代的过滤。"}
   ],
   "examples_and_targets": [
    "溪水/泉水（融化雪水、自然降雨在山地造成的地表水）、地下水、流速较快的河水、气味正常的湖水、露水、雨水——作者列举的动物饮水来源（P003）。",
    "月牙泉——作者举的地下水实例，属具体地理事实断言（P003）。",
    "掉满枯枝败叶、有死老鼠的水坑水与小片死水——作者列举的动物拒饮水（P004、P006）。",
    "引水道、坎儿井、深井、运水车——作者列举的人类取水技术手段（P008）。",
    "村里就一两口可以喝的水井、老鼠昆虫掉入——作者举的聚居区污染场景（P009）。",
    "提问所说的“过滤”与“其他任何一种地球的生物可以直接喝”——被作者以“动物也不会乱喝水”间接回应（Q001、P001）。"
   ],
   "conditions": [
    "“它们一般很自然的会去喝……”——以“一般”限定（P003）。",
    "“在工业时代之前，人口又不稠密的地区”——时间与人口密度的双重条件（P007）。",
    "“居住区水源污染程度可能比较高”“可能得不偿失”——以“可能”限定（P009）。",
    "“人类其实是可以喝……相对还是比较安全的”——以“其实”“相对”作限定（P011）。",
    "“人类的饲养动物喝的水一般是特别净化过的”——以“一般”限定（P014）。",
    "“尤其是动物无法远离水源栖居”——对动物不愁水喝一说的补充限定（P007）。"
   ],
   "rhetoric_and_tone": "以纠正式科普口吻展开，开篇直接否定提问前提（“动物也不会乱喝水的”）；多用列举与对照（喝什么/不喝什么、人/动物、工业时代之前/之后），语气平实、无训诫色彩；未使用反问或讽刺。",
   "unresolved_questions": [
    "提问以“其他任何一种地球的生物”为全称，作者的回答集中在动物（且以野生动物为主），未讨论植物、微生物等非动物类生物，覆盖范围是否充分需研究者判断。",
    "提问所问的“过滤”未被直接讨论；作者给出的是加热与酿酒消毒，与现代水处理的对应关系本文未说明。",
    "“月牙泉这类凹坑低于地下水位渗出的地下水”为具体地理断言，待外部核查。",
    "“人类其实是可以喝动物栖居地的那些活水的，相对还是比较安全的”未给出适用条件与风险边界（如是否需即时饮用、是否适用于所有活水）。",
    "动物拒饮的判断依据（嗅觉是否足以辨别病原体）本文未论证，只作现象描述。",
    "“动物是不愁水喝的”与“尤其是动物无法远离水源栖居”之间的推论关系未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "动物也不会乱喝水的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "它们嗅觉很灵敏，闻起来味道不对的水不会乱喝。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "它们一般很自然的会去喝溪水/泉水", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "或者流速较快的河水、气味正常的湖水这类水、还有露水、雨水。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "那种掉满枯枝败叶，有死老鼠的水坑水，它们也是不喝的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "那种小片死水它们是不喝的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "还有很多植食动物的大部分的水分都直接来自野生植物的枝叶果实，几乎不需要喝什么水。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "在工业时代之前，人口又不稠密的地区污染程度很低，动物是不愁水喝的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "人类自从发明了引水道、坎儿井、深井、运水车……等等这些手段之后，就实现了远离自然水源聚居。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "结果反而导致了居住区水源污染程度可能比较高", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "水质就危险得很。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P009", "quote": "离河又远，挑水要消耗劳动力，可能得不偿失。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P010", "quote": "所以人类学会了用加热或者酿酒的方式来消毒。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P011", "quote": "人类其实是可以喝动物栖居地的那些活水的，相对还是比较安全的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P012", "quote": "反而是动物要是进入了人类聚居地区，喝人类居住地那些多少被污染了的水，动物会受不了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "所以要害其实不在于动物有多大的抵抗力，而在于水有所不同。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "人类的饲养动物喝的水一般是特别净化过的，房前屋后的水可不敢让牲口乱喝。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["动物行为与生态", "公共卫生/饮水安全", "人类聚居史与技术史"],
   "issue_candidates": ["野生动物是否可以直接饮水", "人类为何需要处理饮水", "聚居方式与水源污染的关系", "动物抵抗力与水质的归因"],
   "text_function_candidates": ["答疑", "纠正式解释", "科普说明"],
   "object_candidates": ["动物（野生动物）", "植食动物", "人类", "饲养动物/牲口", "月牙泉（地名）"],
   "working_keywords": ["活水", "死水", "地下水", "引水道", "坎儿井", "污染程度", "消毒", "抵抗力"]
  },
  "notes": "本篇无图片节点，正文完整可读。提问属提问者（Q001），其“其他生物可以直接喝”的前提被作者否定，已按 negated 记录，未把提问者说法当作作者主张。文中“月牙泉”等具体地理/历史断言属待外部核查项，初读不作裁决。"
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
