# -*- coding: utf-8 -*-
"""批次 r001-b0034 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0034.sessions.py            # 写 out/r001-b0034.out.jsonl
  python3 records/r001-b0034.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0034"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0034.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e1bfc2ea": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：如何看待香港大专学界发言人邵岚接受外媒采访时称「不会谴责任何抗议者的暴力行为」？作者不讨论该采访的具体内容与出处，而是以“在亚洲没有幼稚的权利”为总判断，提出“history指数（文化资产）”框架，论证集体成熟是东亚自治体的存在资格，进而判定香港缺少这种文化资产、其“独立”诉求在逻辑上不可行，并称该发言人的言行是香港人“幼态”的典型表现。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开场判断：她没有明白——在亚洲，无论普通个人、政府、自治体还是作为群体的民众，都没有幼稚的权利。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "提出框架：用一个简单标量表达一个国家的精神财富（文化资产），暂称 history 指数，其值为“历史常识的信息量”×“国民人数”。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "论及秉赋，东亚最大的资源是不幼稚：不幼稚才能省掉低质量高代价的尝试、有整体稳定的群体情绪与根本稳定性；这种集体心理状态是社会结构的“地质板块”；但“不幼稚”没有捷径，必须靠对历史的接纳与内化。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "解释内化机制：成为中国人意味着把中国三千多年积累的集体回忆内化为精神内核的一部分，从而获得与个人生活经历不对称的成熟；千万个这样的人集中起来，才呈现可依赖的集体意识成熟。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "称这种集体性的“少年老成”构成东亚社会最大资源，也是人口稠密、人均资源永远低于世界平均的东亚各自治体长期立足的基本资格；在东亚，集体的成熟是任何自治体的存在资格，想要自治就要打通十八铜人阵、获得能创造“集体成熟”的可继承文化资产。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019"], "summary": "指出香港的悖论：要长期有效自治就必须拥有这种文化资产，而香港自身完全没有，只能向外寻求；唯一可行方案是承继中国的文化资产、通过成为“中国香港人”领取中国数千年的智慧财产权；理论上存在第二条路（自己在反复碰壁中学会），但其本钱绝非香港所能支付。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "推论：这才是英国不得不放弃香港的真正原因（它需要扶着才能站立而英国扶不起）；香港要作为自治体长期存在，唯一可能是需要北京帮助；即使在“gd最美好的梦想”里，“独立”也必须依靠极度善意的北京的支持；并以台湾情形类比（美国表态不支持某候选人则其连初选也过不去、自我审查比指派制更苛刻），最后称 gd 是“一条咬着自己尾巴想把自己吃掉的逻辑鲨鱼”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031"], "summary": "称香港人一直保持着一种“幼态”，这位发言人的言行只是这种幼态的典型表现，其人生曲折是自甘幼稚的代价；并断言幼稚无法长存，人最关键的财富是超出个人经历的成熟，作为中国人若低于平均水平尤其可惜。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "区分目标与路线：客观上目的是自由的，评判目标是否合法正义在自然法层面没有意义；有意义的是方案路线是否在逻辑上指向所追求的结果；若逻辑上不存在可行路径，该目标就是“永动机”，把失败都归为努力、斗志、投入问题就是选择自我毁灭；最基本意义上的成熟就是能看见哪些是“永动机”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张：在亚洲，无论普通个人、政府、自治体还是作为群体的民众，都没有幼稚的权利。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者提出用一个简单标量（暂称 history 指数）表达一个国家的精神财富即文化资产，其值为“历史常识的信息量”×“国民人数”。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为论及秉赋，东亚最大的资源就是不幼稚：不幼稚才能省掉低质量而高代价的尝试、才有整体稳定的群体情绪与根本稳定性，这种集体心理状态是社会结构的“地质板块”。", "evidence": ["E003", "E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种“不幼稚”没有捷径，必须靠对历史的接纳和内化来造就；成为中国人意味着把中国三千多年积累的集体回忆内化为自己精神内核的一部分，从而减轻幼稚病。", "evidence": ["E006", "E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这种集体性的“与个人经历不相称的少年老成”构成东亚社会的最大资源，也是东亚各自治体在人口稠密、人均资源永远低于世界平均的条件下长期立足的基本资格。", "evidence": ["E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张在东亚，集体的成熟是任何自治体的存在资格；想要自治就要打通十八铜人阵，获得可以继承的、能有效创造“集体成熟”的文化资产。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为香港的悖论在于：要长期有效自治就必须拥有这种文化资产，而香港自身完全没有、只能向外寻求；唯一可行的方案是承继中国的文化资产，即通过成为“中国香港人”领取中国数千年的智慧财产权。", "evidence": ["E013", "E014", "E015"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者承认理论上存在第二条路——自治体自己在反复碰壁的路线斗争中慢慢学会什么绝对不可以、什么必须坚持，但认为走这条路所需的本钱绝非香港自己所能支付。", "evidence": ["E016", "E017"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这才是英国不得不放弃香港的真正原因——因为它需要扶着才能站立，而英国扶不起。", "evidence": ["E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为香港若想作为自治体长期存在，唯一的可能性就是需要北京帮助；即使在“gd最美好的梦想”里，“独立”也必须依靠一个极度善意的北京的善意接受和努力支持才能存在。", "evidence": ["E019", "E020"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者以台湾情形类比预测：即使走完全部民主流程，只要美国表态、甚至只是暗示不支持某个候选人，该候选人就会连初选也过不去；届时的自我审查、自我限缩甚至比现在的指派制更苛刻和入微，现在觉得无法忍受的，那时将更无法承受。", "evidence": ["E021", "E022", "E023"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称 gd 成了一种需要谋求脱离的主体额外赞助才能达成的脱离、一种需要被攻击对象帮助才能完成的攻击，是“一条咬着自己的尾巴想把自己吃掉的逻辑鲨鱼”。", "evidence": ["E024", "E025"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为香港人一直保持着一种“幼态”，这位发言人的言行只是这种幼态的典型表现，由此带来的人生曲折是其自甘幼稚的选择无法回避的代价。", "evidence": ["E026", "E027"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言幼稚无法长存；人最关键的财富是超出个人经历的成熟；作为一个中国人若在这一点上低于平均水平，尤其可惜。", "evidence": ["E028", "E029"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分目标与路线：客观上目的是自由的，评判目标是否合法、是否正义在自然法层面没有意义；有意义的是人的方案路线选择是否在逻辑上指向他自己追求的结果。", "evidence": ["E030", "E031", "E032"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者认为如果逻辑上不存在可行的路径，就要认识到那个目标是“永动机”；选择“永动机”作目标并把一切失败都归为努力、斗志、投入问题，就是选择自我毁灭；最基本意义上的成熟就是能看见哪些是“永动机”。", "evidence": ["E033", "E034", "E035"]}
   ],
   "argument_steps": [
    "以“她没有明白一个问题”开场，抛出总判断：在亚洲没有幼稚的权利。",
    "提出 history 指数（历史常识的信息量×国民人数）作为衡量国家精神财富的框架。",
    "由该框架推出：论及秉赋，东亚最大的资源是不幼稚（省掉高代价尝试、群体情绪稳定）。",
    "以“地质板块”作比，说明不幼稚的集体心理状态是社会结构稳定的前提。",
    "指出“不幼稚”无捷径，须靠对历史的接纳与内化；成为中国人意味着内化三千多年的集体回忆。",
    "把个体内化汇成集体意识的成熟，并称其为东亚社会最大资源与自治体的基本资格。",
    "由“自治需要集体成熟”转到香港：香港要长期有效自治就必须拥有这种文化资产，而它自身完全没有。",
    "给出唯一可行方案（承继中国文化资产）与理论上的第二条路（自己碰壁学会），并否定后者在成本上可行。",
    "推论英国放弃香港的原因，以及香港长期存在必须依赖北京。",
    "以台湾初选与美国表态作类比，说明“独立”方案的自我限缩将更苛刻。",
    "以“逻辑鲨鱼”总结 gd 的自我矛盾。",
    "把上述归结为香港人的“幼态”与发言人的典型表现，并给出“幼稚无法长存”的判断。",
    "最后把讨论抽象为目标自由与路线可行性的区分，以“永动机”与“成熟”收束。"
   ],
   "concept_usage": [
    {"term": "history指数", "meaning": "作者自造的标量，用以表达一个国家的精神财富（文化资产），等于历史常识的信息量×国民人数", "evidence": "P004", "ambiguity": "如何度量“历史常识的信息量”未说明，也无取值示例"},
    {"term": "不幼稚／幼稚", "meaning": "本文中指集体性的成熟：经由对历史的接纳与内化而获得的、与个人经历不对称的成熟；幼稚则是其反面", "evidence": "P005", "ambiguity": "作者称不幼稚没有捷径，但未给出判定标准"},
    {"term": "文化资产", "meaning": "作者指可以继承的、能有效创造“集体成熟”的历史与智慧财产", "evidence": "P013", "ambiguity": "与 history 指数的关系未严格界定"},
    {"term": "地质板块", "meaning": "比喻社会结构得以稳定的基础（不幼稚的集体心理状态）", "evidence": "P006", "ambiguity": "比喻，未量化"},
    {"term": "十八铜人阵", "meaning": "比喻自治必须通过的考验或门槛", "evidence": "P013", "ambiguity": "未说明具体机制"},
    {"term": "永动机", "meaning": "作者用来指在逻辑上不存在可行路径、因而无法实现的目标", "evidence": "P036", "ambiguity": "比喻性定义，未给出判定程序"},
    {"term": "gd", "meaning": "文中对“港独”的缩写（本文未给出全称）", "evidence": "P022", "ambiguity": "缩写未展开，需外部核对语境"}
   ],
   "examples_and_targets": [
    "邵岚（提问中被引述的香港大专学界发言人；正文以“她”“这位发言人”指称，未复述其原话）",
    "英国放弃香港（作者给出的解释性判断，需外部核查）",
    "台湾的初选与“美国表态甚至只是暗示”（作者类比材料，需外部核查）",
    "“地质板块”（作者比喻）",
    "“十八铜人阵”（作者比喻）",
    "“逻辑鲨鱼”（作者比喻）",
    "“永动机”（作者比喻）",
    "被反驳对象：把“独立”视为可行目标、以幼稚态度对待暴力的主张（作者转述与批评，未指名具体文本）"
   ],
   "conditions": [
    "总判断以“在亚洲”为地域限定（P001）。",
    "history 指数以“如果我们用一个简单的标量来表达一个国家的精神财富”为假设（P002）。",
    "第二条路以“理论上存在”为限定，作者随即以成本否定其可行性（P019）。",
    "P022-P023 的推论以“哪怕在gd最美好的梦想里”“狂野到极点、退了一万万步的美梦”为极端假设，并以“如果美国表态——甚至只是暗示”为条件。",
    "P024 以“如果现在觉得无法忍受”为条件推出“那时候将更无法承受”。",
    "P034-P038 以“如果逻辑上不存在这种可行的路径”为条件。"
   ],
   "rhetoric_and_tone": "政治评论兼论说体：以概念命名（history 指数、地质板块、十八铜人阵、逻辑鲨鱼、永动机）构造框架，语气冷峻、断言密集；对香港人的“幼态”与“自甘幼稚”带训诫与贬抑色彩；对“gd”用缩写与比喻讥刺（“咬着自己尾巴想把自己吃掉”）；结尾由具体政治评论转为抽象的方法论劝诫。",
   "unresolved_questions": [
    "提问引述的邵岚原话与采访出处需外部核查；作者未复述该原话，只以“她”“这位发言人”指称。",
    "“history指数”如何度量“历史常识的信息量”与“国民人数”、如何取值，本文未说明，也无算例。",
    "“英国不得不放弃香港的真正原因”属作者的解释性判断，历史学界有不同说法，需外部核查。",
    "P023 关于台湾初选与“美国表态甚至只是暗示”的说法需外部核查，且作者以“理论上”“哪怕是美梦”等假设方式表述。",
    "“gd”为文中缩写，本文未给出全称与定义。",
    "“十八铜人阵”“逻辑鲨鱼”“永动机”均为比喻，作者未说明其判定的具体程序。",
    "本篇涉及香港、港独、台湾等政治议题，本记录只作归属登记与语气保留，不作价值裁决；正文中的政治性事实断言均记为待外部核查。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "在亚洲，无论是普通个人，又或者是政府、自治体、作为群体的民众，都没有幼稚的权利。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "一个国家的history指数可以表达为“历史常识的信息量”x“国民人数”。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "论及秉赋，东亚最大的资源，就是不幼稚。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "不幼稚，才能省掉低质量而高代价的尝试", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "这种不幼稚的集体心理状态，就是社会结构的“地质板块”。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "但这个“不幼稚”，是没有捷径的，是必须要靠对历史的接纳和内化来造就的。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "成为一个中国人，不可避免的意味着将中国三千多年所积累下来的集体回忆内化为你自己的精神内核的一部分。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "内化过程的完成，能在极大的意义上减轻你的幼稚病", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "是这种成熟、这种集体性的“与个人经历不相称的少年老成”，构成了东亚社会的最大资源。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "必须依赖集体性的成熟来对冲短缺的威胁", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "在东亚，集体的成熟是任何自治体的存在资格。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P013", "quote": "你想要自治，你就要打通十八铜人阵，获得可以继承的能有效创造“集体成熟”的文化资产。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P015", "quote": "香港最尴尬的问题就在于，她想要长期有效自治，就必须拥有这种文化资产。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P016", "quote": "而香港自身没有这种文化资产，完全没有。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P018", "quote": "唯一可行的解决方案就是承继中国的文化资产——也就是通过成为“中国香港人”，而领取中国数千年的智慧财产权。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P019", "quote": "理论上存在第二条路，那就是作为自治体，自己在数次乃至数十次的反复碰壁的路线斗争中慢慢学会什么是绝对不可以的", "relation": "qualifies"},
    {"key": "E017", "paragraph_id": "P019", "quote": "但走这第二条路所需要的本钱，绝非香港自己所能支付。", "relation": "qualifies"},
    {"key": "E018", "paragraph_id": "P020", "quote": "这才是英国不得不放弃香港的真正原因——因为它需要扶着才能站立，而英国扶不起。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P021", "quote": "这导致香港如果想要作为自治体长期存在，唯一的可能性就是需要北京帮助。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P022", "quote": "他们的“独立”也必须要依靠一个极度善意的北京的善意接受和努力支持才能存在。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P023", "quote": "如果美国表态——甚至只是暗示——不支持某个候选人，这个候选人就会连初选也过不去", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P023", "quote": "甚至要比现在的指派制更加苛刻和入微。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P024", "quote": "如果现在觉得无法忍受，那时候将更无法承受。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P025", "quote": "gd就成了一种需要谋求脱离的主体额外赞助才能达成的脱离", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P026", "quote": "这是一条咬着自己的尾巴想把自己吃掉的逻辑鲨鱼。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P027", "quote": "香港人因为种种原因一直都保持着一种“幼态”。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P028", "quote": "这位发言人的言行只是这种幼态的典型表现", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P029", "quote": "幼稚无法长存。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P030", "quote": "人最关键的财富，是超出个人经历的成熟。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P033", "quote": "客观上，目的是自由的。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P034", "quote": "人在选择目标上有天然的自由，去评判那种目标是或者不是合法的、那种目标是或者不是正义的，其实在自然法的层面上是没有意义的。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P035", "quote": "有意义的是人的方案路线选择是否在逻辑上指向他自己追求的结果。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P036", "quote": "如果逻辑上不存在这种可行的路径，那么就要认识到那个目标实际上是“永动机”。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P037", "quote": "人如果选择“永动机”作为目标，然后认为一切的失败都只是努力问题、斗志问题、投入问题，人就是选择了一种自我毁灭。", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P038", "quote": "最基本意义上的成熟，就是能看得见哪些是“永动机”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治评论", "文化/历史意识", "香港议题"],
   "issue_candidates": ["香港自治与文化资产", "集体成熟与幼稚", "港独的可行性", "台湾初选与美国角色"],
   "text_function_candidates": ["评论", "论说", "批评"],
   "object_candidates": ["香港", "中国大陆", "英国", "台湾", "美国", "邵岚"],
   "working_keywords": ["幼稚权", "history指数", "文化资产", "集体成熟", "永动机", "十八铜人阵"]
  },
  "notes": "本篇涉香港、港独、台湾等政治议题，本记录只登记作者判断与其条件/语气，不作价值裁决，也不把提问者的引述当作者主张。作者自造指标（history指数）与多处事实性判断（英国放弃香港的原因、台湾初选机制）均未给依据，已逐条记入 unresolved_questions 并标为待外部核查。无图片节点。"
 },
 "be6d869d": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：设计师这样的工作，可以做一辈子吗？作者先给出肯定判断（设计师是少有的能做到老的工作），随即转入他自称“顺便说一下”的职业选择与职业规划问题：以价值观为前提，以“需求的健壮性”论证职业前途，区分“职业”与“岗位”，并以“元问题／元知识／元技能”为框架，最后回到设计师为何能做到老。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "先给出判断：设计师是少有的能做到老的工作，也是现代年轻人可以选择的最佳职业之一；预告会顺便谈职业选择和职业规划，并留了一句“等找到时间”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009"], "summary": "称职业关乎生存，甚至比婚姻和生育更决定性；不合理的职业选择让人逆水行舟、竭尽全力而不得寸进，很快造成焦虑、抑郁甚至绝望。前提性论断：没有恰当的价值观就不存在任何合理的职业选择；遭遇职业危机的绝大多数不是选择本身不合理，而是价值观有根本缺陷，导致一切职业都不可选择，换职业只是暂时尚未崩坏。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "以“仅仅为了赚钱”为例说明价值观缺陷：这样就没有选择命运的能力，只是在被选择之后假装那是自己的选择。提出“工作是一种死法”——是对必死命运的彻底接纳及在此基础上的安排；有必死的觉悟才有不为“生机”所动的坚决，然后才有选择可言；否则一次次的选择只是有效期不断缩短的毒品。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "从需求角度界定职业前途：职业最终服务于会有人受益并付费的业务，其前途取决于所服务的需求；需求不消灭则业务与职业至少有最基本的前途。把需求面对未来变迁而持续存在的可能性称为需求的“健壮性”，并提问如何鉴定。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029"], "summary": "提出两种最健壮的需求：免于死亡与得到幸福；食物、住所、知识、必需品、安全、治疗满足前者，娱乐、抚慰、宽恕、新选择满足后者。二者没有满足可言，因此相关业务有来自需求本身的根本健壮性；终身投入的职业（“死所”）必须指向人类永远无法完全满足的需求，否则将面临中年踏空或最终成空，其恐惧会催生愚蠢浮躁的投机行为并因沉没成本把人拖进深渊。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "追问“到底什么是‘一个职业’”：以画画的、做广告文案的、写代码的、送外卖的、服装销售、地产中介为例，指出若这些就是心目中的职业则全都极不安全，因为深度太浅、容不下一个人的职业生涯与人生；大多数人像职场寄居蟹，不断因行业、婚姻、子女、父母、置产等原因换壳。作者称在现在这个历史时期只有可以自由化的职业才是真正的职业，否则只是寄居蟹壳——岗位（post）。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "给出“职业”的真正表达：designer、healer、manager、entertainer、explorer、broker、problem solver、dealer、peace maker、protector 这类元概念级别的表述；头衔上的限定词只是进入职业的“学徒认证”，客户助理、接线员不是职业而是职业中的阶段状态；只有区分阶段状态与职业才能避免在阶段角色上投入过多资源的战略性错误。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058"], "summary": "以接线生为例：同样一个月业余时间，学管理学原理与学“优秀接线员须知”是未来命运的分界线；前者的有效回报延续整个职业生涯，后者基本只延续到不再做接线员为止；有职业意识的人会更猛烈而坚决地投资“元知识”“元技能”，其投资不会因职业阶段变化变成沉没成本，因此无惧岗位与市场变化。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077"], "summary": "界定元问题：人生的元问题可规范表达为“找到一个足以支撑我接受死亡及死亡风险的理由”，其前置问题是“在我找到这个理由之前，我要避免死亡”；爱、享乐、权力欲望、解脱、信仰都是可能答案（作者称暂不讨论哪个更好）。元问题无声地追问每个人，人类行为都围绕它运转；有利于找到或固守答案的就是人类认为有价值的，也是乐意付出劳动回馈的；利润最终来自回答或帮助他人解决这个问题（或至少让人相信如此）；凡与元问题直接关联的就是元知识、元技能。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089"], "summary": "元知识主要是广义的语言，元技能是广义的观察、归纳、演绎与表达能力；越直接与元技能相连的工作越安全、越能“做到老”。回到设计师：它是发现问题、解决问题和表达方案的职业，在表达方面有高度专业训练，几大元技能都踩全了，所以能做到老；若越做越窄，只因本人不是真正的设计师，而是在做人肉印刷机之类的非智力劳务——这不是设计师这个职业的错。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断设计师是少有的能做到老的工作，也是现代年轻人可以选择的最佳职业之一。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称职业关乎生存，甚至是比婚姻和生育更加决定性的人生选择；不合理的职业选择会让人竭尽全力而不得寸进，并很快造成焦虑、抑郁甚至绝望。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出：如果没有一个恰当的价值观，就不存在任何合理的职业选择；遭遇职业危机的人绝大多数不是职业选择本身不合理，而是价值观有根本缺陷、导致一切职业都不可选择，因此换职业无法真正解决问题。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为若从事职业的原因仅仅只是“为了赚钱”，这个心态本身就注定了没有选择命运的能力；人其实从未选择，只是在被选择之后假装那是自己的选择。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出“工作是一种死法”，是对自身必死命运的彻底接纳及在此基础上的安排；因为有必死的觉悟才有不为“生机”所动的坚决，然后才有选择可言，否则一次次的选择只是有效期不断缩短的毒品。", "evidence": ["E007", "E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为职业的前途取决于该职业服务于什么样的需求：需求不消灭则业务与职业至少有最基本的前途，反之则职业消亡、非个人努力与天资所能对抗；作者把需求面对未来变迁持续存在的可能性称为需求的“健壮性”。", "evidence": ["E010", "E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出两种最健壮的需求——免于死亡与得到幸福；提供食物、住所、知识、必需品、安全、治疗是在满足第一需求，提供娱乐、抚慰、宽恕、新的选择是在满足第二需求。", "evidence": ["E012", "E013"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这两种根本需求没有满足可言，因此指向它们的业务有来自需求本身的根本健壮性；终身投入的职业（“死所”）一定要指向人类永远无法完全满足的需求，否则一生足够漫长，可能面临中年踏空或最终成空。", "evidence": ["E014", "E015"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为若把“画画的”“做广告文案的”“写代码的”这类表述当作职业，则这些全都极不安全，因为深度太浅、容不下一个人的整个职业生涯与人生；大多数人像职场寄居蟹，不断因行业、婚姻、子女、父母、置产等原因被迫换壳。", "evidence": ["E016", "E017"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者限定“在现在这个历史时期”：只有可以自由化的职业才可以被称为真正的职业，否则它就只是寄居蟹壳——岗位（post）。", "evidence": ["E018"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张职业应是 designer、healer、manager 这类“元概念”级别的表述；头衔上的限定词只是进入职业的“学徒认证”，客户助理、接线员不是职业而是职业中的阶段状态；只有区分阶段状态与职业才能避免战略性地在阶段角色上投入过多资源。", "evidence": ["E019", "E020", "E021"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以接线生为例：同样一个月的业余时间，学管理学原理与学“优秀接线员须知”是未来命运的分界线——前者的有效回报延续整个职业生涯，后者基本只延续到不再做接线员为止。", "evidence": ["E022", "E023"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称有正确职业意识的人会更猛烈而坚决地投资“元知识”“元技能”，而不是立竿见影的小技巧；因为掌握的是不受时代与具体环境限制的元技能元知识，这些投资不会因职业阶段变化变成沉没成本，所以他们无惧岗位与市场变化。", "evidence": ["E024", "E025"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把人生的元问题规范表达为“找到一个足以支撑我接受死亡及死亡风险的理由”，其前置问题是“在我找到这个理由之前，我要避免死亡”；并称爱、享乐、权力欲望、解脱、信仰都是元问题的可能答案选择，哪个更好更可行暂时不讨论。", "evidence": ["E026", "E027"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称无论人是否明确意识到，元问题都在无声地、一秒也没有放松地追问每一个人；人类的行为、努力与追求都围绕它运转；有利于找到或固守该答案的，就是人类最终认为有价值、也乐意付出劳动回馈的。", "evidence": ["E028", "E029"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为凡与元问题直接关联的就是元知识、元技能：元知识主要是广义的语言，元技能是指广义的观察、归纳、演绎与表达能力。", "evidence": ["E030", "E031"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为越直接与元技能相连的工作越安全、越能“做到老”；设计师之所以能做到老，是因为它本身就是发现问题、解决问题和表达方案的职业，在表达方面有高度专业训练、几大元技能都踩全了；若这个工作越做越窄，只因本人不是真正的设计师，而是在做人肉印刷机之类的非智力劳务，这不是设计师这个职业的错。", "evidence": ["E032", "E033", "E034", "E035"]}
   ],
   "argument_steps": [
    "先给出结论：设计师是少有的能做到老的工作、是年轻人可选的最佳职业之一。",
    "把话题扩到职业规划：职业关乎生存，比婚姻生育更决定性；不合理的职业选择会带来焦虑、抑郁与绝望。",
    "提出前提性论断：没有恰当的价值观就没有合理的职业选择；职业危机多源于价值观缺陷而非选择本身。",
    "以“仅仅为了赚钱”为例说明价值观缺陷，并提出“工作是一种死法”的界定，推出“有必死觉悟才有选择”。",
    "从需求界定职业前途，提出需求的“健壮性”问题。",
    "给出两种最健壮的需求（免于死亡、得到幸福）及其服务门类；指出它们没有满足可言，故职业应指向永远无法完全满足的需求。",
    "追问“什么是‘一个职业’”，以常见岗位名称说明其深度太浅，提出寄居蟹比喻。",
    "区分“真正的职业”与“岗位（post）”，标准是可否“自由化”。",
    "给出职业的元概念级表述（designer、healer、manager 等），并把头衔限定词降为“学徒认证”与阶段状态。",
    "以接线生的学习选择为例，说明元知识元技能投资的长期回报。",
    "提出“元问题”及其前置问题，并以之解释价值与利润的来源。",
    "界定元知识与元技能，回到设计师为何能做到老，并解释“越做越窄”的原因。"
   ],
   "concept_usage": [
    {"term": "元问题", "meaning": "人生的根本问题：“找到一个足以支撑我接受死亡及死亡风险的理由。”其前置问题是“在我找到这个理由之前，我要避免死亡”", "evidence": "P063", "ambiguity": "作者自称答案选择（爱、享乐等）暂不讨论"},
    {"term": "元知识／元技能", "meaning": "与元问题直接关联的知识与技能：元知识主要是广义的语言，元技能是广义的观察、归纳、演绎与表达能力", "evidence": "P078", "ambiguity": "“广义的”未进一步界定"},
    {"term": "健壮性", "meaning": "一种需求面对一切未来变迁而保持持续存在的可能性", "evidence": "P021", "ambiguity": "如何鉴定只给出“没有满足可言”这一标准"},
    {"term": "岗位（post）／职业", "meaning": "作者区分：只有可以自由化的才是真正的职业，否则只是寄居蟹壳式的岗位", "evidence": "P044", "ambiguity": "“自由化”的含义与判定方式未说明"},
    {"term": "死所", "meaning": "作者对终身投入的职业的称呼（与“工作是一种死法”呼应）", "evidence": "P028", "ambiguity": "以引号使用，未定义"},
    {"term": "学徒认证", "meaning": "作者对头衔上限定词（如门诊护士、客户助理、接线员）的定位：进入职业的阶段性身份", "evidence": "P052", "ambiguity": "认证机制未说明"},
    {"term": "元概念", "meaning": "作者指 designer、healer、manager 这类可作为职业选择的层级表述", "evidence": "P051", "ambiguity": "与“元知识／元技能”的关系未严格界定"}
   ],
   "examples_and_targets": [
    "不需要吃草的驴（作者类比：找不到这样的驴如同没有恰当价值观时找不到合理职业）",
    "职场寄居蟹（作者比喻）",
    "画画的、做广告文案的、写代码的、送外卖的、服装销售、地产中介（作者列举的岗位表述）",
    "designer、healer、manager、entertainer、explorer、broker、problem solver、dealer、peace maker、protector（作者列举的职业元概念）",
    "接线生：学管理学原理 vs 学“优秀接线员须知”（作者的例子）",
    "孙中山、郭靖等未出现；本篇实例以职业与行业为主",
    "“人在年轻的时候，最核心的能力是什么？”（P080，作者回指的外部文章标题；该文未在本篇给出）"
   ],
   "conditions": [
    "P007-P008 的前提是“如果你没有一个恰当的价值观”“如果你从事你的职业的原因仅仅只是‘为了赚钱’”。",
    "P010 的批评以“仅仅只是为了赚钱”这一动机为条件。",
    "P012 起的分岔以“如果你还是觉得工作只是为了活着，那么你就不必看下去了”为读者条件。",
    "P021 的前途判断以“需求不会消灭”为条件；反之则业务与职业消亡。",
    "P028 的告诫以“一生足够漫长”为时间条件，后果是“可能面临中年踏空或者最终成空”。",
    "P044 的“真正的职业”以“在现在这个历史时期”和“可以自由化”为限定。",
    "P065 作者明确把元问题答案的优劣（爱、享乐、权力欲望、解脱、信仰）列为暂不讨论。"
   ],
   "rhetoric_and_tone": "长文论说体，兼有训诫与断言：以“很遗憾”“我明确的告诉你”“记住”等直接呼告推动；用一连串反问（“你现在做的，到底是一个职业，还是一个岗位？”“你看懂没有？”“几大元技能都踩全了，怎么会那么被动呢？”）；以寄居蟹、死法、死所、毒品、深渊等比喻制造冷峻感；举岗位名称时用短行罗列，形成节奏。",
   "unresolved_questions": [
    "P003“等找到时间。”表明该回答在发布时可能是待补/未完成状态；而 P001 的结论与后续长文已写成，两者的写作时序本文未说明。",
    "P080“人在年轻的时候，最核心的能力是什么？”属 text 与 lexical 的未覆盖片段（divergence: text_has_content_not_in_lexical）；作者在 P081-P083 以“这一篇东西”“上面这篇”回指某篇外部文章，该文章未在本篇给出，其内容无法核对。",
    "“可以自由化的职业”未给出定义与判定标准（P044）。",
    "“广义的语言”“广义的观察、归纳、演绎与表达能力”的范围本文未界定（P078-P079）。",
    "元问题的诸答案（爱、享乐、权力欲望、解脱、信仰）作者明确称暂不讨论（P065）。",
    "“设计师”之外哪些职业同样满足元技能条件，本文只给了片段判断（P084-P085），未系统列举。",
    "文中关于行业与职业前景的判断（如岗位深度、寄居蟹式换壳）未见数据或来源，需外部核查。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "设计师是少有的能做到老的工作，也是现代年轻人可以选择的最佳职业之一。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P005", "quote": "职业关乎生存，甚至是比婚姻和生育更加决定性的人生选择。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P007", "quote": "如果你没有一个恰当的价值观，对你将不存在任何合理的职业选择。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "遭遇职业危机的人群中绝大多数都不是职业选择本身是否合理的问题，而是价值观本身有根本缺陷，导致一切职业都不可选择。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P010", "quote": "如果你从事你的职业的原因仅仅只是“为了赚钱”，那么这个心态本身就注定了你并没有选择命运的能力", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P011", "quote": "你其实从未选择，你只是在被选择之后假装那是你的选择。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P013", "quote": "因为工作是一种死法，是一种定意选定的死法。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P014", "quote": "因为有必死的觉悟，所以有不为所谓“生机”所动的坚决。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P016", "quote": "否则你一次次的“选择”，只是一种有效期不断缩短的毒品。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P020", "quote": "职业的前途取决于这种职业到底是在服务于什么样的需求。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P021", "quote": "如果我们把一种需求面对一切未来变迁而保持持续存在的可能性称之为需求的“健壮性”", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P023", "quote": "第一种，是免于死亡。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P025", "quote": "提供食物、提供住所、提供知识、提供生活必需品、提供安全、提供治疗……这些是在满足第一需求。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P027", "quote": "这两种根本需求，是没有满足可言的。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P028", "quote": "你所打算终身投入的职业、你的“死所”，一定是指向某个人类永远无法完全满足的需求。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P041", "quote": "它们的“深度”都太浅了，浅到容不下一个人全部的职业生涯、容不下一个人的人生。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P042", "quote": "我们中的绝大多数人，就好像职场寄居蟹。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P044", "quote": "只有可以自由化的职业，才可以被称为真正的职业。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P048", "quote": "我是一个designer，我是一个healer，我是一个manager", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P051", "quote": "能作为职业的选择，必定是这样的“元概念”。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P053", "quote": "只有明确的区分阶段状态与职业，你才能避免犯下战略性的错误", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P054", "quote": "你可以拿来去学管理学原理，也可以拿来学“优秀接线员须知”。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P056", "quote": "前者的有效回报会延续自己的整个职业生涯", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P057", "quote": "会更加猛烈而坚决的投资在“元知识”“元技能”上", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P058", "quote": "他们的这些个人发展的投资就不会因为一些职业阶段的变化而变成沉没成本。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P063", "quote": "人生的元问题可以规范的表达为——“找到一个足以支撑我接受死亡及死亡风险的理由。”", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P064", "quote": "“在我找到这个理由之前，我要避免死亡。”", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P067", "quote": "无论人是否明确的意识到了这个元问题，这个问题都在无声的、一秒也没有放松的追问着每一个人，无人幸免。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P069", "quote": "有利于人类找到元问题答案的、有利于人类固守自己找到的答案的，就是人类最终会认为有价值的", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P078", "quote": "元知识，主要是广义的语言。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P079", "quote": "元技能，是指广义的观察、归纳、演绎与表达能力。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P084", "quote": "越是直接与元技能相连的工作，就越是安全系数高，越是能“做到老”。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P085", "quote": "所谓设计师，本身就是一个发现问题、解决问题和表达方案的职业。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P088", "quote": "只会是因为你本身并不是真正的设计师", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P088", "quote": "而只是在做人肉印刷机之类的非智力劳务。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职业规划", "价值论/人生哲学"],
   "issue_candidates": ["设计师能否做一辈子", "职业与岗位的区分", "需求的健壮性", "元问题与元技能"],
   "text_function_candidates": ["答疑", "论说", "经验总结", "训诫"],
   "object_candidates": ["设计师", "接线员", "客户助理", "门诊护士", "年轻人"],
   "working_keywords": ["职业", "岗位", "元问题", "元知识", "元技能", "健壮性", "寄居蟹", "死所"]
  },
  "notes": "本篇 89 段、约 3.9 千字（UTF-16），为长文；P080 属 text 与 lexical 未覆盖片段（divergence），作者以“这一篇东西”“上面这篇”回指一篇未在本篇出现的外部文章，已记入未决问题。P003“等找到时间。”保留原样，未据此推断写作状态。无图片节点。"
 },
 "34c70769": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：如果能在全世界人类脑中同时播放一句话，你要说什么？作者不解释理由，直接给出两个短句作答，中文一句、拉丁文一句。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以“你终有一死”与拉丁文“MEMENTO MORI.”两句作答。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者选择要在全世界人类脑中同时播放的一句话是“你终有一死”，并以拉丁文 MEMENTO MORI 重述。", "evidence": ["E001", "E002"]}
   ],
   "argument_steps": [
    "直接给出中文短句“你终有一死。”",
    "以拉丁文 MEMENTO MORI. 复述同一句。"
   ],
   "concept_usage": [
    {"term": "MEMENTO MORI", "meaning": "作者用作“你终有一死”的拉丁文表述", "evidence": "P002", "ambiguity": "作者未解释其含义、出处与用意"}
   ],
   "examples_and_targets": [
    "“MEMENTO MORI.”（拉丁文箴言，作者用作回答本身）"
   ],
   "conditions": [
    "以提问的假设（能在全世界人类脑中同时播放一句话）为前提，未涉及播放的效果或后果。"
   ],
   "rhetoric_and_tone": "极简格言／铭文体：全篇仅两句、共 20 字（UTF-16），中文句加拉丁文重复，语气庄重如箴言，无解释、无称呼、无修辞展开。",
   "unresolved_questions": [
    "作者未说明为何选择这句话，也未说明希望它产生什么效果。",
    "MEMENTO MORI 的出处与作者对其的理解本文未说明（一般作为拉丁语箴言使用，此处不作裁决）。",
    "该短句是否另有所指或承接其他上下文，本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "你终有一死。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "MEMENTO MORI.", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲学/生死观"],
   "issue_candidates": ["对全人类说的一句话", "死亡意识"],
   "text_function_candidates": ["格言式回答"],
   "object_candidates": ["全人类"],
   "working_keywords": ["你终有一死", "MEMENTO MORI"]
  },
  "notes": "全篇仅两段 20 字，无图片节点；作者未给出任何理由或展开，本记录不代为补足。"
 },
 "fb286207": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：女儿自杀了，我该怎么办？作者不作安慰式回应，而是给出五条应对建议（用药稳住情绪、选择性回避熟人、读带救赎结局的经典名著、与通达开明的老人或修行者作抽离交流、悔罪改过并转移生命价值），并以“祝好”收束。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "第一条建议：吃抗抑郁药稳住情绪。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "第二条建议：扛过第一波熟人劝解之后，回避大部分熟人，只留少部分有支持作用的交往关系；理由是大部分人都不知道自己在干嘛，本质上只是在借“安慰你”的姿态安抚自己所受的惊吓。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "第三条建议：可以考虑读一些带救赎结局的经典文学名著，因为那些著作里有得救的先例与得救的历程，而且是确定的、没有变数的。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "第四条建议：与不知前情、不知你名的见多识广、通达开明的老人家或修行者做抽离的交流沟通；不要具体谈自己的事、只讲道理，不要只固着在第一个投缘的师傅身上，要广泛接触；理由是这些人往往见过各种生离死别而仍能不悲伤、不消极地活着。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "第五条建议：有罪悔罪、有过改过；人生没有结束，生命还可以造福于人，承接生命价值的可以不只是子女，也可以是任何年轻人、任何有子女的人；并以“有艺传艺，无艺传业”补充。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P009"], "summary": "以“祝好”收束。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的第一条建议是吃抗抑郁药稳住情绪。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议在扛过第一波熟人劝解之后回避大部分熟人、只留少部分有支持作用的交往关系，因为大部分人都不知道自己在干嘛，本质上只是在借着“安慰你”的姿态和动作安抚自己所受的惊吓。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议可以考虑读一些带救赎结局的经典文学名著，因为那些著作里面有得救的先例与得救的历程，而且是确定的、没有变数的。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议与不知前情、不知己名的见多识广、通达开明的老人家或修行者做抽离的交流沟通：不要具体谈自己的事、只是讲道理，且不要只固着在第一个投缘的师傅身上而要多方接触；理由是这些人往往见过各种生离死别、人间惨淡，仍能不悲伤、不消极地活着。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议有罪悔罪、有过改过，并指出人生没有结束、生命还可以造福于一些人；承接生命价值的可以不只是子女，也可以是任何年轻人、任何有子女的人（“有艺传艺，无艺传业”）。", "evidence": ["E007", "E008"]}
   ],
   "argument_steps": [
    "第一条：以药物稳住情绪。",
    "第二条：在熟人劝解的第一波之后收缩交往范围，并给出对“劝解者”动机的判断。",
    "第三条：以带救赎结局的经典文学名著提供确定的得救先例与历程。",
    "第四条：以抽离的、只讲道理的交流接触有阅历的老人或修行者，并要求多方接触而非固着一人。",
    "第五条：以悔罪改过与生命价值的转移（传艺或传业）给出出路。",
    "以“祝好”收束。"
   ],
   "concept_usage": [
    {"term": "抽离的交流沟通", "meaning": "作者指不涉具体事情的、只讲道理的交流方式", "evidence": "P005", "ambiguity": "具体形式与频次未说明"},
    {"term": "得救的先例／得救的历程", "meaning": "作者称经典文学名著中确定无疑的救赎叙事", "evidence": "P004", "ambiguity": "未列具体书目，“得救”的所指未定义"},
    {"term": "有艺传艺，无艺传业", "meaning": "作者对生命价值承接方式的概括：有技艺则传艺，无技艺则传事业", "evidence": "P008", "ambiguity": "八字短句，未展开"}
   ],
   "examples_and_targets": [
    "“安慰你”的熟人（作者判断其动机是安抚自己所受的惊吓）",
    "带救赎结局的经典文学名著（作者举例的读物类型，未列书名）",
    "见多识广、通达开明的老人家、修行者、师傅（作者建议的交流对象）",
    "任何年轻人、任何有子女的人（作者建议的价值承接对象）"
   ],
   "conditions": [
    "第一条为直接祈使（“吃抗抑郁药稳住情绪”），未加限定。",
    "第二条以“扛过第一波熟人劝解之后”为时序条件，并以“只留下少部分有支持作用的交往关系”为范围限定。",
    "第三条以“可以考虑”表述，属可选建议；其理由以“确定的、没有变数的”为条件。",
    "第四条以“可以考虑”表述，并限定为“不知前情、不知你名”“不要具体的谈你的事，只是讲道理”“不要只固着在第一个……要多多广泛的接触”。",
    "第五条以“有罪悔罪，有过改过”为前提，并以“可以不只是你的子女，也可以是……”列举替代对象。"
   ],
   "rhetoric_and_tone": "条目式实务建议（“第一……第五”），语气克制、命令与建议混用；第三条、第四条用“可以考虑”留出余地；对熟人劝解的判断带冷峻讥刺（“大部分人都不知道自己在干嘛”）；末句“祝好”转为简短祝愿。",
   "unresolved_questions": [
    "提问者的具体情况（女儿的年龄、自杀原因、家庭状况等）本文未涉及，作者也未追问。",
    "第一条“吃抗抑郁药稳住情绪”属医疗建议，作者未说明诊断、处方、剂量与就医途径，需专业核验。",
    "第三条“带救赎结局的经典的文学名著”未列具体书目。",
    "第四条“修行者”“师傅”所指的宗教或修行传统未说明；“抽离的”交流如何操作未展开。",
    "第五条“有罪悔罪，有过改过”中的“罪”与“过”具体指什么本文未说明。",
    "本篇 brief 与正文同源（brief 为正文前段截断），无额外信息。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "第一，吃抗抑郁药稳住情绪。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "第二，扛过第一波熟人劝解之后，回避大部分熟人，只留下少部分有支持作用的交往关系。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "大部分人都不知道自己在干嘛，本质上只是在借着“安慰你”的姿态和动作安抚ta们自己所受的惊吓。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "那些著作里面有得救的先例，也有得救的历程，而且是确定的、没有变数的。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "不要具体的谈你的事，只是讲道理。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "还能不悲伤、不消极的活着，ta们的经验值得你借鉴。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "承接你生命价值的可以不只是你的子女，也可以是任何年轻人、任何有子女的人。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "有艺传艺，无艺传业。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理危机应对", "丧亲/哀伤", "人生建议"],
   "issue_candidates": ["子女自杀后的应对", "如何面对熟人劝解", "生命价值的转移"],
   "text_function_candidates": ["建议清单", "安慰与实务指导"],
   "object_candidates": ["提问者（丧女者）", "熟人", "老人家", "修行者", "师傅"],
   "working_keywords": ["抗抑郁药", "熟人劝解", "救赎结局", "修行者", "有艺传艺"]
  },
  "notes": "作者以条目式建议作答，第三条与第四条用“可以考虑”留有选择余地，本记录保留该语气。第一条涉及用药，属需专业核验的建议，本记录不作裁决。无图片节点。"
 },
 "6606595d": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：如何看待中国电信杨峰义建言「降低电价才是 5G 部署的根本」？作者不评价该建言本身，而是指出“这位”（指建言者）漏掉了一个大问题——5G 基站耗能与传输信号正相关，进而论证 5G 传送同样信息量比 4G 更省能、总功率反而下降，流量增长则有定价与经济活动的支撑，最后称“这完全是一个伪问题”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "指出被评论者漏掉的大问题：5G 基站的功率消耗与传输的信号呈正相关；虽然不算“成正比”，但基站无信号传输时的“基础代谢”在总耗能中占比很小，约等于电脑待机耗能占满负荷运算耗能的占比。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "第二点：因信号本身的特性所限，5G 传送同样信息量所消耗的能量比 4G 更小；若整个网络传输的信息总量不变，则无论修多少基站，基站总体传送这些数据所耗能量 5G 会低于 4G（因为 5G 基站离用户近、波段负载信息的能力更强、效率更高）；于是观察到的会是所有基站负载很轻、总功率反而下降。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007"], "summary": "提出可能的追问：如果大家都觉得网速快，开始看 8K 电视、4K 直播，流量大增以至总传输量大涨，总功率岂不是大增？", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "回应之一：流量不是免费的，运营商普遍实行高速流量比低速流量更贵的定价策略，升级流量消耗要多付费用，且这部分费用已包含电费部分，因此不存在运营商自己亏本的问题。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "回应之二：信息流量与经济、民生活动的规模绝对正相关，每一点流量都对应需求与供应；以制造业突然消耗大量石油、双十一突然产生大量运费作类比反问，质疑为何要担心经济负担不起这笔电费。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012"], "summary": "结论：这完全是一个伪问题。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出被评论者漏掉了一个大问题：5G 基站的功率消耗是和传输的信号呈正相关的。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者承认这个“正相关”还算不上是“成正比”，但称基站在无信号传输状态下的“基础代谢”在整个基站耗能中占比很小，约等于电脑待机耗能占满负荷运算耗能的占比。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张因信号本身的特性所限，5G 传送同样的信息量所消耗的能量比 4G 更小；假设网络传输的信息总量规模不变，则无论修多少基站，基站总体为传送这些数据所消耗的能量 5G 会低于 4G。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测：会观察到所有基站都负载很轻，于是总功率反而会下降，而不是上升。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为流量不是免费的：运营商普遍实行高速流量比低速流量更贵的定价策略，升级流量消耗所付出的费用已包含电费部分，因此不会存在运营商自己亏本的问题。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张信息流量与经济、民生活动的规模是绝对正相关的，每一点流量都必然对应着需求和供应。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者以制造业突然消耗大量石油、双十一突然产生大量运费作类比反问，否定需要担心经济负担不起 5G 电费，并称这完全是一个伪问题。", "evidence": ["E008", "E009"]}
   ],
   "argument_steps": [
    "指出被评论者的建言漏掉了“基站耗能与传输信号正相关”这一大问题。",
    "限定该相关不是正比，但以电脑待机／满负荷的类比说明“基础代谢”占比很小。",
    "以信号特性与基站距离说明同信息量下 5G 耗能低于 4G，故总功率反而下降。",
    "主动提出“流量大涨是否导致总功率大增”的追问。",
    "以流量定价（含电费成本）回应运营商亏本问题。",
    "以流量与经济民生活动的正相关、以及制造业耗油与双十一运费的类比，说明不必担心电费负担。",
    "以“所以这完全是一个伪问题”作结。"
   ],
   "concept_usage": [
    {"term": "正相关／成正比", "meaning": "作者用来说明 5G 基站耗能与传输信号的关系：相关但不严格成比例", "evidence": "P001", "ambiguity": "未给出相关程度的定量说明"},
    {"term": "基础代谢", "meaning": "作者对基站在无信号传输状态下耗能的比喻", "evidence": "P002", "ambiguity": "未给出具体占比数值"},
    {"term": "伪问题", "meaning": "作者对“担心 5G 电费使经济负担不起”这一担忧的定性", "evidence": "P012", "ambiguity": "作者未逐一点名该问题的各种表述形式"},
    {"term": "信息流量", "meaning": "作者用作与经济、民生活动规模正相关的量", "evidence": "P009", "ambiguity": "与耗能的关系只作定性讨论"}
   ],
   "examples_and_targets": [
    "电脑没有计算任务待机时的耗能与满负荷运算时耗能的占比（作者类比）",
    "8K 电视、4K 直播（作者假设的流量增长情形）",
    "制造业突然消耗大量石油、双十一突然产生大量运费、淘宝店因运费大增而破产（作者类比反问）",
    "中国电信杨峰义（提问中的建言者，正文以“这位”指称，未复述其建言内容）"
   ],
   "conditions": [
    "P004 的结论以“假设我们的整个移动通信网络保持传输的信息总量规模不变化”为条件。",
    "P003 的前提是“因为信号本身的特性所限”。",
    "P007 的追问以“如果大家都觉得网速很快，于是都开始看起 8K 电视、4K 直播”为假设。",
    "P008 的定价论证以“如果运营商不是不识数的傻瓜”为限定。",
    "全篇为定性论证，未给出耗能、流量或电费的定量数据。"
   ],
   "rhetoric_and_tone": "反驳式论说：以“这位漏掉了一个很大的问题”直接点名对方疏漏；用“第二”“首先”“第二”分点推进；以两个反问（“你会担心制造业因为耗油量大增而破产……吗？”“于是为什么要如此担心我们的经济负担不起这个电费呢？”）与“不识数的傻瓜”这类口语讥刺加强语气；结论用极短断言“所以这完全是一个伪问题”。",
   "unresolved_questions": [
    "作者未给出任何定量依据（基站“基础代谢”占比、5G 与 4G 每比特能耗、基站数量与总耗能的关系），需外部核查。",
    "提问中的建言（“降低电价才是 5G 部署的根本”）的具体内容与出处见提问；正文只说“这位漏掉了一个很大的问题”，未复述建言。",
    "“这完全是一个伪问题”所指的具体问题（担心 5G 电费拖垮经济）需结合上文理解，作者未逐条列出被否定的论证。",
    "作者称 5G 基站离用户更近、波段负载信息能力更强、效率更高，但未给出技术参数或来源。",
    "P009“信息流量与经济、民生活动的规模是绝对正相关的”为作者的断言，未给出数据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "这位漏掉了一个很大的问题——5G基站的功率消耗是和传输的信号呈正相关的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "虽然这个“正相关”还算不上是“成正比”", "relation": "qualifies"},
    {"key": "E003", "paragraph_id": "P003", "quote": "因为信号本身的特性所限，5G传送同样的信息量所消耗的能量比4G更小。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "假设我们的整个移动通信网络保持传输的信息总量规模不变化", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "你只是会观察到所有的基站都负载很轻，于是总功率反而会下降，而不是会上升。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "如果运营商不是不识数的傻瓜，那么显然这部分费用是包含了电费的部分的。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "信息流量与经济、民生活动的规模是绝对正相关的。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "你会担心制造业因为耗油量大增而破产，或者淘宝店因为突然运费大增而破产吗？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "所以这完全是一个伪问题。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["通信技术/产业政策", "能源与成本"],
   "issue_candidates": ["5G 部署与电价", "基站耗能与信号的关系", "流量增长与总耗能"],
   "text_function_candidates": ["评论", "反驳", "技术经济分析"],
   "object_candidates": ["中国电信", "杨峰义", "5G基站", "4G", "运营商"],
   "working_keywords": ["5G", "耗能", "基础代谢", "电价", "流量", "伪问题"]
  },
  "notes": "本篇为定性反驳，无数据与出处；提问所指的建言者（中国电信杨峰义）在正文中仅以“这位”指称，其建言内容未复述，需与提问合看。相关技术数据均记为待外部核查。无图片节点。"
 },
 "dabd4834": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：如何识别一个人能否被有效地帮助？作者没有给出识别方法，而是直接否掉该问题的前提：人是不能救人的，因此不存在“我来救你”；他把对求助者所行的事界定为自己对上帝的义务（“唯尽义而已”），因而不必分辨对方是否“可救”，并警告凭私意救人是僭越神权。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "先否掉提问的前提：人是不能救人的，不存在“我来救你”这种情况；“我”既无资格也无能力救“你”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "把对求助者所行的帮助界定为自己对上帝承担的义务、对上帝命令的服从，即“唯尽义而已”；因为是尽义，所以不必分辨对方是否“可救”、后面是否会“得救”，无论对方如何，要说要做的基本一样。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "以救济机关的窗口办事员为喻：奉命做被指定的事、做到被指定的程度；不保证解决对方的问题或让其满意；解决了不必谢他而要谢机构，没解决也不必怪他、可去怪机构。对求助者没有个人恩德，故不能对其后续好运居功，也不为其后续厄运负责。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "主张每个人都是单独直接面对上帝、完完全全在上帝手里；不要指望任何人的帮助能改写上帝打算加诸在你身上的命运（无论好坏）。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012"], "summary": "判定凭私意“救人”就是僭越神权、自居为神（重罪）；对方只要寄予希望就等于认可这一点、就等于拜偶像的罪；两个都是罪人，后事极端不祥，结局总是施助者半途而废、受助者陷入“你害死我”的憎恨，因为没有人是上帝、每个人在某个阶段不能不放弃，而中途弃之不顾至少造成对方重大机会成本（本来可以别求医治）。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "结论：直道而行，各安天命；人不能救人，人只能自行其道，寄希望于上帝借此安排他人更好的命运。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者主张人是不能救人的，所以不存在“我来救你”这种情况，“我”既无资格也无能力来救“你”。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把对求助者所行的、对方觉得有帮助的事情界定为自己对上帝承担的义务、对上帝命令的服从，即“唯尽义而已”。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称因为自己是尽义，所以根本不必分辨对方是否“可救”、后面是否会“得救”；无论对方如何，他要说的话、要做的事基本上是一样的。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以救济机关的窗口办事员自比：奉命做被指定的事、做到被指定的程度；不保证解决对方的问题或让其满意；解决了不必谢他而应谢机构，没解决也不必怪他而可去怪机构。", "evidence": ["E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称对求助者没有个人的恩德，所以完全不能对其后续的好运居功，也不能因其后续的厄运负责。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张每个人都是单独直接面对上帝、完完全全在上帝手里；不要指望任何人的帮助能改写上帝打算加诸在其身上的命运，无论那在本人看来是好还是坏。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定凭私意“救人”就是僭越神权、自居为神（重罪），对方只要对自己寄予希望就等于认可这一点、就等于犯下拜偶像的罪；两个都是罪人，后事极端不祥。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预言结局总是施助者最终半途而废、受助者陷入“你害死我”的憎恨，因为没有人是上帝、每个人在某个阶段不能不放弃；而中途弃之不顾至少造成了对方重大的机会成本——对方本来可以别求医治。", "evidence": ["E011", "E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者结论：直道而行，各安天命；人不能救人，人只能自行其道，寄希望于上帝借此安排他人更好的命运。", "evidence": ["E013", "E014"]}
   ],
   "argument_steps": [
    "直接否定“人救人”，并否认“我来救你”这一情形（既无资格也无能力）。",
    "把帮助行为重新界定为对上帝的义务与服从（尽义）。",
    "由“尽义”推出不必分辨对方是否可救、是否会得救。",
    "以救济机关窗口办事员为喻，说明角色边界：不居功、不负责、不保证结果。",
    "以“每个人单独直接面对上帝”说明无人能改写他人命运。",
    "把凭私意救人判为僭越神权与自居为神，并指出对方寄予希望即构成拜偶像。",
    "预言双方结局（半途而废与被憎恨）并指出机会成本。",
    "以“直道而行，各安天命”与“人只能自行其道”收束。"
   ],
   "concept_usage": [
    {"term": "尽义", "meaning": "本文中指人对上帝承担的义务、对上帝命令的服从，而非对受助者个人的恩德", "evidence": "P004", "ambiguity": "义务的具体内容与判定方式未说明"},
    {"term": "可救／得救", "meaning": "作者否定的识别对象：对方是否“可救”、后面是否会“得救”", "evidence": "P005", "ambiguity": "两个词均加引号，未给出定义"},
    {"term": "僭越神权／自居为神", "meaning": "作者对凭私意救人的定性：把不属于人的权柄据为己有，属重罪", "evidence": "P010", "ambiguity": "判定标准未给出"},
    {"term": "机会成本", "meaning": "作者指受助者因被牵着走而失去的其他求助机会（本来可以别求医治）", "evidence": "P012", "ambiguity": "“医治”所指的具体处境未说明"},
    {"term": "直道而行，各安天命", "meaning": "作者给出的行动准则：自己走正道，各人承受自己的天命", "evidence": "P013", "ambiguity": "八字短语，未展开"}
   ],
   "examples_and_targets": [
    "救济机关的窗口办事员（作者自比的形象）",
    "上帝、神权、罪、偶像（作者的信仰框架，非外部事例）",
    "“你害死我”（作者预言的受助者反应）",
    "“ta本来可以别求医治”（作者举的机会成本情形，具体所指未说明）",
    "被否定的对象：提问中“如何识别一个人能否被有效地帮助”这一设问方式，以及凭私意救人的做法"
   ],
   "conditions": [
    "全篇以基督教上帝观（人对上帝的义务、神权、罪、偶像崇拜）为前提。",
    "P005 的“无论你是如何，我要说的话，我要做的事基本上是一样的”含“基本上”这一限定。",
    "P009 的劝告以“无论在你自己看来是好还是坏”为范围，不区分命运的好坏。",
    "P012 的判断以“因为没有人是上帝，所以每个人都在某个阶段不能不放弃”为条件，并以“至少”限定机会成本的规模。",
    "P006 的姿态以“奉命”“被指定的程度”为界限。"
   ],
   "rhetoric_and_tone": "宗教论说体，语气决断：以“人是不能救人的”开头直接否定提问前提；用窗口办事员的世俗比喻说明角色边界，降低个人情感色彩；连用“重罪”“罪人”“偶像”“后事极端不祥”等严厉词；以“直道而行，各安天命”八字收束，兼具训诫与自我定位。",
   "unresolved_questions": [
    "提问问的是“如何识别一个人能否被有效地帮助”，作者以“不必分辨”回应，实际上取消了识别问题本身；这一落差的含义需研究者判断。",
    "作者的信仰立场与所属传统本文未说明，“对上帝承担的义务”的具体内容亦未展开。",
    "P012“ta本来可以别求医治”中的“医治”所指的具体处境未说明。",
    "“尽义”如何判定（哪些行为算尽义）本文未给出标准。",
    "P006 的“机构”在比喻之外是否实指某类组织，本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "人是不能救人的。所以不存在一种情况叫做“我来救你”。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "“我”既无资格，也无能力来救“你”。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "是我对上帝承担的义务。是我对上帝的命令的服从。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "唯尽义而已。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "因为我是尽义，所以我根本不必去分辨你是否“可救”，后面是否会“得救”。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "这个姿态就好像救济机关的窗口办事员——我奉命在这里做事，做被指定的事，做到被指定的程度。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "我对你没有个人的恩德，所以完全不能对你后续的好运居功，也不能因为你后续的厄运负责。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "每个人都是单独直接面对上帝，并且完完全全的在上帝手里。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "不要指望任何人的帮助能帮你改写上帝打算加诸在你身上的命运", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "你要去凭私意“救人”，你就已经僭越了神权。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "最后总是走向你自己最终半途而废，而对方陷入“你害死我”的憎恨之中。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "因为没有人是上帝，所以每个人都在某个阶段不能不放弃。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "直道而行，各安天命。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "人不能救人，人只能自行其道，寄希望于上帝借此安排他人更好的命运。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教伦理", "助人伦理"],
   "issue_candidates": ["能否识别可救之人", "救人与僭越神权", "助人者的责任边界"],
   "text_function_candidates": ["答疑", "宗教论说", "训诫"],
   "object_candidates": ["上帝", "救济机关", "窗口办事员"],
   "working_keywords": ["人救人", "尽义", "可救", "得救", "僭越神权", "各安天命"]
  },
  "notes": "作者以基督教框架作答，本记录只登记其判断与前提，不作教义或事实裁决。作者没有回答提问要求的“识别方法”，而是主张不必分辨，此点已记入未决问题。无图片节点。"
 },
 "88e2e0eb": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：为什么高铁这么发达了还有人选择走更危险更费时间的高速路？作者先给出两条解释（行李与驾驶乐趣），随即指出该问题下的答案几乎一面倒盛赞自驾、贬低公共交通，令人担忧；随后用大段论证说明年节繁忙时段高速的危险与个人驾驶技术无关，最后建议除非有非常必要的理由不要走高速。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "给出第一条解释：主要原因更多不在人而在行李——有人可能需要带很多随身行李，而在高铁等公共交通工具上携带过多随身行李很麻烦。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "第二条解释：有人想趁这个机会享受驾驶乐趣，这是公共交通提供不了的；自驾风景更好、有纵横天地自由自在的体验，很多老司机属于这一类。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "指出该问题下的答案几乎一面倒盛赞自驾、贬低高铁和公共交通，令人担忧；并指出单就安全性而言，高铁自然胜过长途自驾很多倍。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "郑重建议：除非有非常必要的理由，否则不要在年节繁忙时段自驾上高速；提醒老司机不要掉以轻心，因为这个时段的事故往往不是个人驾驶水平高超就能避免的。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009"], "summary": "论证车距无法保持：车流密度大时，留足安全车距就会被后车超车插入，减速再拉开又会被下一辆抢空，不断被超车导致紧张疲劳，于是几乎肯定会维持一个插不进去的车距；因此不管技术如何，客观现实导致无法保持安全车距，强行保持会因不断被别车头而平添另一种危险。并强调此时是以 80-120km 的时速在车距不足以让另一辆车挤入的高度危险状态下行驶，不是在市区 40 码缓行。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012"], "summary": "论证连锁事故不可避免：前车急刹后，后车要经过反应时间才急刹，事故概率不随链条传递明显衰减，几乎每辆车都来不及刹车；即使自己能刹住，也不能保证后车能刹住，更不能保证后车不是超载货车、缺少经验的司机或刹车系统有缺陷的隐患车。并以调侃说明这跟驾驶技术无关（除非技术包含“张开魔法结界”或“短距垂直起降”）。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "补充条件：雾、霜、小雪、中雨大雨会使危险加倍，道路维护不佳则更高；并强调关键词是这种危险性与驾驶技术、与驾龄无关。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P015"], "summary": "提出唯一合理手段：道路管理者发布全路通告，临时把时速限制下降到 40-60 公里/小时，因为只有这个速度能基本保证事故不太会酿成重大连环相撞；但除非实现全线标识电子化，目前没有多少手段能瞬间通告整条路的全部司机，这个手段实际上用不上。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P016", "P017"], "summary": "结论与替代方案：若明知高速车辆会很多，除非有非常必要的理由不要走高速；可以少带行李、年货快递、到家后再租车，重要的体验另有解决方案，也没有必要把车开回家证明自己是有车一族。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P018", "P019"], "summary": "以“命更要紧，何况这还是全家的命”收束，并以反问“你们相信这些司机全都不是老司机吗？”作结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为人们选择自驾高速的主要原因“更多的不在于人，而在于行李”：有人可能有特殊原因需要带很多随身行李，而在高铁或一切公共交通工具上携带过多随身行李都很麻烦。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的第二个原因是有人想趁这个机会享受驾驶乐趣，这是公共交通提供不了的；自驾风景更好、有纵横天地自由自在的体验，很多老司机属于这一类。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出该问题下的答案几乎一面倒盛赞自驾、贬低高铁和公共交通，这令人担忧；单就安全性而言，高铁自然胜过长途自驾很多倍。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者郑重建议：除非有非常必要的理由，否则不要在年节繁忙时段自驾上高速。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提醒老司机不要掉以轻心、不要以为自己技术好就没意义，因为这个时段的事故往往不是个人驾驶水平高超就能避免的。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者论证车距无法保持：留足车距会被后车插入、减速再拉开会被继续抢空，不断被超车导致紧张疲劳，于是几乎肯定会维持一个插不进去的车距；因此不管技术如何，客观现实导致无法保持安全车距，强行保持会因不断被人别车头而平添另一种危险。", "evidence": ["E007", "E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者强调此时是以 80-120km 的时速、在车距不足以让另一辆车挤入的高度危险状态下行驶，而不是在市区以 40 码缓行、也不是每隔 500 米就有红灯的节奏。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者论证连锁事故不可避免：后车看到前车急刹要经过一个反应时间才急刹，事故概率不会随链条传递明显衰减，几乎每一辆车都来不及刹车；即使自己能刹住，也不能保证后车能刹住，也不能保证后车不是超载货车、缺少经验的司机或刹车系统有缺陷的隐患车。", "evidence": ["E010", "E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以调侃方式断言这跟驾驶技术无关：除非驾驶技术包含“张开魔法结界”或者“短距垂直起降”，否则舒马赫附体也没办法。", "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出遇到雾、霜、小雪、中雨大雨会更加加倍危险，道路维护程度不佳则危险性更高；并强调这种危险性与驾驶技术、与司机的驾龄无关。", "evidence": ["E013", "E014"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为在那种天气与交通流量下保证安全其实只有一个合理手段——道路管理者发布全路通告把时速临时限制下降到 40-60 公里/小时，只有这个速度能基本保证事故不太会酿成重大连环相撞；但除非实现全线标识电子化，目前没有多少手段能瞬间通告整条路的全部司机，这个手段实际上用不上。", "evidence": ["E015", "E016"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者结论：若明知高速公路车辆会很多，除非有非常必要的理由就不要走高速；并给出替代方案（少带行李、年货快递、到家后再租车、重要体验另有解决方案、不必开车回家证明有车），强调命更要紧，何况还是全家的命。", "evidence": ["E017", "E018"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问“你们相信这些司机全都不是老司机吗？”收束，质疑“靠老司机技术即可避险”的想法。", "evidence": ["E019"]}
   ],
   "argument_steps": [
    "先回答原问题：主因是行李，其次是享受驾驶乐趣。",
    "转而指出问题下的答案一面倒盛赞自驾、贬低公共交通，令人担忧。",
    "给出安全性对比：高铁胜过长途自驾很多倍。",
    "发出建议与提醒：除非必要，不要在年节繁忙时段自驾上高速；事故不是个人技术能避免。",
    "以车距被插入、被抢空、紧张疲劳说明无法保持安全车距。",
    "以反应时间与链条传递说明连环事故难以避免，且无法控制后车状态。",
    "以“魔法结界”“短距垂直起降”“舒马赫附体”强调与驾驶技术无关。",
    "补充天气与道路维护条件，再次强调与技术和驾龄无关。",
    "给出唯一合理手段（临时限速 40-60km/h）并指出其现实上难以实施。",
    "给出替代方案并以“命更要紧”与反问收束。"
   ],
   "concept_usage": [
    {"term": "安全车距", "meaning": "作者指高速行驶中为防止追尾而保留的车距；本文主张在高密度车流中客观无法保持", "evidence": "P007", "ambiguity": "未给出具体车距数值"},
    {"term": "反应时间", "meaning": "后车看到前车急刹到开始急刹之间的延迟", "evidence": "P010", "ambiguity": "未给出时长"},
    {"term": "隐患车", "meaning": "作者指刹车系统有缺陷的车辆", "evidence": "P011", "ambiguity": "无定义与判定方式"},
    {"term": "魔法结界／短距垂直起降", "meaning": "作者用来调侃“技术能避免此类事故”这一想法的虚构能力", "evidence": "P012", "ambiguity": "明显的玩笑修辞，不宜作字面理解"}
   ],
   "examples_and_targets": [
    "年节繁忙时段的自驾（作者讨论的具体场景）",
    "80-120km 的时速、市区 40 码缓行、每隔 500 米红灯（作者的速度与路况对比）",
    "超载货车、缺少经验的司机、刹车系统有缺陷的隐患车（作者列举的后车风险）",
    "“张开魔法结界”“短距垂直起降”“舒马赫附体”（作者的调侃）",
    "被批评对象：该问题下几乎一面倒盛赞自驾、贬低高铁与公共交通的答案（作者转述，未指具体作者）",
    "行李、年货快递、到家租车、有车一族（作者给出的替代方案材料）"
   ],
   "conditions": [
    "P005 的建议以“除非有非常必要的理由”为条件，并限定在“年节繁忙时段”。",
    "P013 的危险加倍以“如果遇到有雾、有霜、有小雪、有中雨大雨”为条件；P013 后半以“如果道路维护程度不佳”为条件。",
    "P015 的限速手段以“除非实现全线标识电子化”为条件，结论是该手段“实际上用不上”。",
    "P016 的结论以“如果你明知高速公路车辆会很多”为条件。",
    "P015 的“只有这个速度能基本保证”含“基本”这一限定。",
    "P012 的表述为反事实调侃（除非具备魔法结界或短距垂直起降）。"
   ],
   "rhetoric_and_tone": "劝导兼警告语气：以“郑重建议”“希望老司机们不要掉以轻心”“注意关键词”直接呼告；连用感叹号与反问（“但你别忘了现在你不是在市区道路上以40码缓行！”“你们相信这些司机全都不是老司机吗？”）；以“魔法结界”“舒马赫附体”作夸张幽默；结构上先答问题、再转入安全警告，最后给替代方案与“命更要紧”的收束。",
   "unresolved_questions": [
    "本篇含 6 个图片节点（IMG001-IMG006，均位于正文 P019 之后的 lexical 图片节点），图片内容未经核验，需人工或多模态复核；本记录不据图片生成任何主张。",
    "“年节繁忙时段”未具体化为日期或时段；80-120km、40-60 公里/小时等数值未给出来源。",
    "“单就安全性而言，高铁自然是胜过长途自驾很多倍”未给出统计数据或出处。",
    "“全线标识电子化”的具体技术方案与现状本文未说明。",
    "被批评的“一面倒盛赞自驾”的答案未指名具体作者或内容。",
    "因图片未核验，本篇 full_text_checked=false、status=needs_reread（按系统提示词第 5 节的保守解释）。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "主要原因更多的不在于人，而在于行李。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "第二就是有人想要趁这个机会享受驾驶乐趣。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "在这个问题下的答案几乎一面倒的盛赞自驾，贬低高铁和公共交通，这真的令人担忧。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "单就安全性而言，高铁自然是胜过长途自驾很多倍。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "郑重建议，除非有非常必要的理由，否则不要在年节繁忙时段自驾上高速。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "因为这个时段的事故往往不是你个人驾驶水平高超就能避免的。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "他一旦强行插入，安全车距就立刻减半，完全失去了安全缓冲的作用。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "所以不管你技术如何，客观现实会导致你没有办法保持安全车距。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "你是在以80-120km的时速在车距不足以让另一辆车挤入的高度危险状态行驶！", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "事故概率并不会随链条传递明显衰减！", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "你也不能保证后车不是超载货车，不是缺少经验的司机，不是刹车系统有缺陷的隐患车！", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "除非你的驾驶技术包含了“张开魔法结界”或者“短距垂直起降”，否则这跟你的技术无关！", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "如果遇到有雾、有霜、有小雪、有中雨大雨则更加会加倍危险。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "这种危险性与你的驾驶技术、与你是多老的司机无关。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "临时把时速限制下降到40-60公里/小时。只有这个速度能基本保证出现事故不太会酿成重大连环相撞。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P015", "quote": "但是，除非实现全线标识电子化，目前并没有多少手段能瞬间通告整条路的全部司机。这个手段实际上用不上。", "relation": "qualifies"},
    {"key": "E017", "paragraph_id": "P016", "quote": "所以，如果你明知高速公路车辆会很多，那么除非有非常必要的理由，不要走高速。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P018", "quote": "命更要紧，何况这还是全家的命。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P019", "quote": "你们相信这些司机全都不是老司机吗？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["交通安全", "出行选择"],
   "issue_candidates": ["为何选择自驾而非高铁", "年节高速的危险性", "限速与通告手段"],
   "text_function_candidates": ["答疑", "安全劝导", "论说"],
   "object_candidates": ["高铁", "高速公路", "老司机", "舒马赫", "道路管理者"],
   "working_keywords": ["安全车距", "反应时间", "年节繁忙时段", "80-120km", "连环相撞"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含 6 个图片节点（IMG001-IMG006，src 见记录 structure.images；lexical 中均位于正文 P019 之后的图片节点），图片内容未经核验，需图像核验；已读部分为正文文本。因图片未核验，本篇 full_text_checked=false、status=needs_reread（按系统提示词第 5 节“图片文章还要求 image_checked=true 才可 full_text_checked=true”的保守解释）。IMG001-IMG006 由 authoring.py 机械生成时因 image_checked=false 被标为 pending，未经查证。正文中的数值（80-120km、40-60 公里/小时）与“高铁胜过长途自驾很多倍”等断言均无来源，已记入未决问题。"
 },
 "5e6bf097": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：如何看待中国将在长三角开展外国人永久居留政策试点？作者不引述试点条文，而是以连串反问为“试点”辩护：先质疑“正常的声音微弱”，再问世界上有几个大国没有外国人永久居留政策并列出名单，随后逐条反驳“焦虑”的理由（落户更难、大开国门、与入籍混淆），最后指出现行政策是防敌反特心态的遗留、与中国开放政策不相称且成本由经济承担。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以反问开场：质疑知乎上正常的声音为何这么微弱；反问开展外国人永久居留政策试点有什么问题、难道中国打算一直做一个没有相称的外国人永久居留政策的奇怪国家；并问世界上有几个大国没有外国人永久居留政策。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "以“这是现在其它有永久居留政策的国家/地区名单”引出 38 项名单（阿根廷、澳大利亚、伯利兹……美国）。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P044"], "summary": "以马达加斯加、危地马拉、多米尼加、厄瓜多尔反问：中国是不如它们吗？", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P045", "P046", "P047", "P048"], "summary": "回应“焦虑”：反问嫌自己落户上海比外国人难、谁说外国人落户上海就更简单，并强调这是“永久居留”不是“入籍”；指出作为中国国民天生就有长三角的永久居留权，户籍与居留权不是同一概念；再以北上广深的“漂”们未被遣返原籍禁止入境、人口二十年翻了几倍反问其来源。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P049"], "summary": "以反问否定“大开国门”的担忧：难道存在永久居留政策，中国就会随便任何外国人毫无限制地获得居留权、任由几百万上千万越南人缅甸人老挝人涌入，或有上百万美国人德国人来争岗位？", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P050", "P051"], "summary": "指出：现有的永久居留政策是当年特殊状态下防敌反特心态的遗留结果，早就与中国现在的开放政策不相称；大量外籍在华工作者生活在几乎荒谬的别扭状态下，造成的额外成本有相当部分由中国经济增长承担，相关行政成本日渐沉重、都是要财政负担的；并反问是否为了“阴阳怪气的、永远哄不开心的巨婴”而不解决这些成本。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P052"], "summary": "以“幸好这是在中国”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑知乎上正常的声音微弱，并反问开展外国人永久居留政策试点有什么问题、难道中国打算一直做一个没有相称的外国人永久居留政策的奇怪国家。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以“世界上有几个大国没有外国人永久居留政策？”发问，并列出 38 项已有永久居留政策的国家/地区名单。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以马达加斯加、危地马拉、多米尼加、厄瓜多尔反问他所假定的反对者：中国是不如这些国家吗？", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问对方在焦虑什么、是否嫌自己落户上海比外国人难，并追问谁说外国人落户上海就更容易；同时强调这是“永久居留”而不是“入籍”。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张作为中国的国民天生就有长三角的永久居留权，并指出户籍与居留权不是同一个概念；又以北上广深的“漂”们未被“遣返原籍禁止入境”、二十年人口翻了几倍反问其人口来源。", "evidence": ["E007", "E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者以反问否定“存在永久居留政策中国就会大开国门”的担忧：不会随便任何外国人毫无限制地获得居留权、不会任由几百万上千万越南人缅甸人老挝人涌入，也不会有上百万美国人德国人来争岗位。", "evidence": ["E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为现有的永久居留政策是当年特殊状态下防敌反特心态的遗留结果，早就与中国现在的开放政策不相称；大量外籍在华工作者生活在几乎荒谬的别扭状态下，造成的额外成本有相当部分由中国经济增长承担，相关行政成本日渐沉重、都要财政负担。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问指责反对者是“阴阳怪气的、永远哄不开心的巨婴”，质问是否为了他们而不解决这些成本，并以“幸好这是在中国”收束。", "evidence": ["E012", "E013"]}
   ],
   "argument_steps": [
    "以“知乎现在正常的声音怎么这么微弱”开场，设定论辩对象为反对试点的声音。",
    "反问试点有什么问题，并以“难道中国打算一直做……奇怪国家”施压。",
    "以“世界上有几个大国没有……”发问并列出 38 项名单作为论据。",
    "以马达加斯加、危地马拉、多米尼加、厄瓜多尔反问中国是否不如它们。",
    "逐条回应焦虑：落户难度、居留与入籍的区别、国民的天然居留权、户籍与居留权的区别、北上广深人口来源。",
    "以反问否定“大开国门、外国人涌入”的担忧。",
    "指出现行政策的历史来源、与开放政策不相称、外籍工作者的处境成本与财政负担。",
    "以“巨婴”讥称反对者，并以“幸好这是在中国”收束。"
   ],
   "concept_usage": [
    {"term": "永久居留（权）", "meaning": "作者强调这是居留而非入籍；并称中国国民天生就有长三角的永久居留权", "evidence": "P045", "ambiguity": "未引述试点政策的具体条文与条件"},
    {"term": "户籍", "meaning": "作者明确与居留权区分开的概念", "evidence": "P047", "ambiguity": "两者的制度差异未展开"},
    {"term": "巨婴", "meaning": "作者对反对者的讥称", "evidence": "P051", "ambiguity": "情绪化用语，非定义"},
    {"term": "国家/地区名单", "meaning": "作者列出的已有永久居留政策的 38 项名称", "evidence": "P005", "ambiguity": "名单混合主权国家与地区，未说明收录标准"}
   ],
   "examples_and_targets": [
    "38 项国家/地区名单（阿根廷、澳大利亚、伯利兹、巴西……美国；作者用作论据）",
    "马达加斯加、危地马拉、多米尼加、厄瓜多尔（作者反问中的比较对象）",
    "北上广深的各种“漂”们、落户上海、996 的岗位（作者举例材料）",
    "几百万上千万越南人、缅甸人、老挝人；上百万美国人、德国人（作者反问中假定的数量）",
    "“巨婴”“阴阳怪气”（作者对反对者的讥称）",
    "被反驳对象：反对长三角外国人永久居留试点的声音（作者转述，未指名具体论者）"
   ],
   "conditions": [
    "全篇以提问所述的“长三角开展外国人永久居留政策试点”为讨论背景，作者未引述政策条文。",
    "多处为反问而非断言（P001、P002、P003、P044、P045、P047、P048、P049、P051），其表述力度依赖反问语气。",
    "P048 的反问以“这二十年”为时间范围，P049 的数量（几百万上千万、上百万）是反问中假定的数量。",
    "P050 的判断以“现有的永久居留政策是当年特殊状态下防敌反特心态的遗留结果”这一历史解释为前提。"
   ],
   "rhetoric_and_tone": "高强度反问与讥讽：全篇大量以问句推进（“有什么问题？”“你们在焦虑什么？”“难道你们觉得……”）；用比较法施压（“中国是不如马达加斯加还是不如危地马拉？”）；以“巨婴”“阴阳怪气”“哄不开心”等贬称攻击反对者；结尾“幸好这是在中国”为冷峭的收束。",
   "unresolved_questions": [
    "P005 为整份名单（38 项），P006-P043 是同一名单在 lexical 中的逐项节点（字符范围与 P005 重叠），本记录只按 P005 整体引用，未重复计量。",
    "名单把台湾、澳门、香港与主权国家并列（未加“地区”限定），原文如此，本记录照录不改写；该归类表述需研究者注意（涉领土表述，本记录不作裁决）。",
    "P031“巴拉圭巴拉圭永久居民”疑为原文重复或笔误，本记录保留原文未改写。",
    "名单中部分名称附有括号说明（如“美国（美国永久居民）”），各项制度的差异本文未说明，需外部核查。",
    "作者未给出中国现行永久居留政策的条文、外籍在华工作者的规模与成本数据。",
    "P049 中的“几百万上千万越南人缅甸人老挝人”“上百万美国人德国人”为反问中的假定数量，非作者给出的统计数据。",
    "P052“幸好这是在中国”的具体所指（庆幸该政策是在中国推行？）本文未展开。",
    "反对声音的具体论者与论据本文未指名，全部经作者转述。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "知乎现在正常的声音怎么这么微弱？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "开展外国人永久居留政策试点，有什么问题？难道中国打算一直做一个没有相称的外国人永久居留政策的奇怪国家？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "世界上有几个大国没有外国人永久居留政策？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P044", "quote": "中国是不如马达加斯加还是不如危地马拉？还是不如多米尼加、厄瓜多尔？", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P045", "quote": "你们在焦虑什么？嫌自己落户上海比外国人难？谁跟你说外国人落户上海就比你简单？", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P045", "quote": "另外看清楚——这是“永久居留”，不是“入籍”。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P046", "quote": "作为中国的国民，你天生就有长三角的永久居留权。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P047", "quote": "户籍难落？户籍跟居留权是一个概念吗？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P048", "quote": "北上广深的各种漂们，有多少被“遣返原籍禁止入境”了？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P049", "quote": "难道你们觉得存在永久居留政策，中国就会大开国门随便任何外国人毫无限制的获得居留权？", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P050", "quote": "现有的永久居留政策是当年特殊状态下防敌反特心态的遗留结果，早就与中国现在的开放政策不相称。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P051", "quote": "就为了你们这些阴阳怪气的、永远哄不开心的巨婴而不解决这些成本？", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P052", "quote": "幸好这是在中国。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["移民/居留政策", "公共政策评论"],
   "issue_candidates": ["长三角外国人永久居留试点", "永久居留与入籍的区别", "户籍与居留权", "外籍在华工作者的处境与成本"],
   "text_function_candidates": ["评论", "论辩", "政策辩护"],
   "object_candidates": ["中国", "长三角", "上海", "北上广深", "越南", "缅甸", "老挝", "美国", "德国", "马达加斯加", "危地马拉", "台湾", "澳门", "香港"],
   "working_keywords": ["永久居留", "入籍", "户籍", "长三角试点", "防敌反特", "巨婴"]
  },
  "notes": "lexical 结构特殊：P005 是整份名单，P006-P043 为同一名单的逐项节点且字符范围与 P005 重叠，本记录只按 P005 整体引用一次。名单中台湾、澳门、香港与主权国家并列，原文如此，照录未改写；P031“巴拉圭巴拉圭永久居民”疑为重复笔误，保留原文。作者未引述试点政策条文，正文中的数量均为反问中的假定值。无图片节点。"
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
