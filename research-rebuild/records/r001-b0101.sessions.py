# -*- coding: utf-8 -*-
"""批次 r001-b0101 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0101.sessions.py            # 写 out/r001-b0101.out.jsonl
  python3 records/r001-b0101.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0101"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0101.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "808c5b72": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何让别人心甘情愿地把他所学的教给我？”。作者不讨论如何劝说老师，而是从学习者一侧给出条件与做法：超额完成作业、尊师、学以致用、分红，并把目标定为“使得教你成为一种享受”。提问者的处境与立场未归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"], "summary": "开篇给出唯一一条做法：永远超额完成作业。理由是布置作业意味着老师对学生作出承诺（做好会有审阅反馈）并付出心血；“等额完成”只是足够礼貌、不够资格；任一方面不达标不必解释理由。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "三条注意：学习是改变命运的事；做不到的理由只能免于惩罚、改变不了命运；对不闲的人“不优先”会演变成“停止”，而好老师没可能很闲。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "限定与升华：高难大量的作业完成一半也可能已是超额，老师心里有杆秤；教与学是相互敬重，任何一方不敬即实质宣告放弃；作业只能让人惊喜、不容让人失望。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "提出真正的秘诀是使教你成为一种享受；高质量完成作业只是其中一项关键内容，已算及格，之上还有发挥空间。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024"], "summary": "补充之一：要尊师；作者称尊师的理由与技术细节需要专门讨论，其后接一句设问“我出钱你出力，为什么学生就得更尊敬老师？”。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035"], "summary": "补充之二：学以致用分两个层面——对所学话语体系学以致用（用新术语、范式、方法论沟通），以及拿教的东西做出有用、有趣之物；不致用则教育失败、所学迅速遗忘；学生致用又能反过来激发老师的使命感与责任感。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043"], "summary": "补充之三：分红。让老师从学生日后收益中长期获益，能学到对方能教的极限；老师傅留一手是人之常情，实质是分红不够、对方信不过。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P044"], "summary": "结论：做到这几条，想没出息都很难。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "让别人愿意教的办法只有一条：永远超额完成作业。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "布置作业就是老师对学生作出承诺（做好会有下一步审阅与反馈），也是老师付出心血。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "时间、数量、质量刚好达标的“等额完成”只表示足够礼貌、不够资格，能否被教还要看运气能否搭上好同学的顺风车。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "任一方面不达标都不必解释理由：理由是个人权利，但任何理由都意味着那件事被认为比学习重要，解释没有必要。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学习是改变命运的事；对命运不满却把改变命运放在次要优先级的人应自问是否真的那么不满。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做不到的理由只能让人免于惩罚，改变不了命运。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "对不是很闲的人来说，“不优先”会自然演变成“停止”，而好老师没可能很闲。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作业难度很高、量很大时，完成一半也许就已经是超额；老师心里有杆秤，不会轻看一份好作业背后的心血。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教与学是“你敬我一尺，我敬你一丈”的关系，任何一方的不敬都意味着实质的宣告放弃。", "evidence": ["E012", "E013"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的秘诀是想办法使教你成为一种享受；高质量完成作业是其中一项关键内容，做到即已及格。", "evidence": ["E014", "E015"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要尊师；作者称尊师的理由与技术细节本身是一个需要专门讨论的问题。", "evidence": ["E016"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学以致用分两个层面：用所学到的话语体系沟通，以及拿教的东西做出有用、有趣的东西。", "evidence": ["E017", "E018"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若学了不准备致用，就注定令人失望，教育实际上失败，所学过两三个月也会忘记。", "evidence": ["E019", "E020"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学生学以致用是老师产生强烈使命感和责任感的高效扳机。", "evidence": ["E021"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "分红对几乎所有老师有最大的激励效果：学生学得多好直接关系老师的未来收益，在这种体系下学生能学到的是对方能教的极限。", "evidence": ["E022", "E023"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老师傅怕绝活教出去自己没饭吃是人之常情，但那实际上是指学生分红分得不够、对方信不过。", "evidence": ["E024", "E025"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做到超额完成作业、尊师、学以致用、分红这几条，想没出息都很难。", "evidence": ["E026"]}
   ],
   "argument_steps": [
    "先给结论式做法：永远超额完成作业（P001-P002）。",
    "用“布置作业=承诺+心血”说明老师一方的付出，确立学生对等义务（P003-P004）。",
    "区分“等额完成”与超额：前者只算足够礼貌、不够资格（P005-P006）。",
    "排除解释理由的路径：任何理由都等于认定别的事比学习优先，故不必解释（P007）。",
    "以“学习是改变命运的事”“理由只能免于惩罚”两条提高优先级要求（P009-P011）。",
    "指出不优先会演变为停止，好老师没可能很闲（P012）。",
    "让步/限定：高难大量作业下完成一半也可能是超额，老师不会轻看心血（P013）。",
    "把教与学定义为相互敬重，不敬即实质放弃；反问学生是否也能放弃改变自己的命运（P014-P016）。",
    "把秘诀从“完成作业”提升为“使教你成为一种享受”（P020-P021）。",
    "补充三条：尊师、学以致用（两个层面）、分红（P023-P043）。",
    "结论：做到这几条想没出息都很难（P044）。"
   ],
   "concept_usage": [
    {"term": "超额完成作业", "meaning": "在时间、数量、质量上超出老师要求的下限，是作者给出的唯一核心做法。", "evidence": "P002", "ambiguity": "P013 补充说明标准不机械：作业难度高、量大时，完成一半也可能算超额。"},
    {"term": "等额完成", "meaning": "时间、数量、质量刚好达标，作者评价为“只是足够礼貌”。", "evidence": "P005", "ambiguity": "作者未给出“超额”的可操作判定标准。"},
    {"term": "使得教你成为一种享受", "meaning": "作者所称的真正秘诀，高质量完成作业是其一项关键内容。", "evidence": "P020", "ambiguity": "除作业、尊师、致用、分红外，作者未穷举其余内容。"},
    {"term": "学以致用", "meaning": "本文分两层：使用所学的新术语体系/表达范式/方法论沟通；拿教的东西做出有用、有趣之物。", "evidence": "P027", "ambiguity": "“有用”的判定标准由谁定，本文未说明。"},
    {"term": "分红", "meaning": "学生从习得技能中长期向老师提供收益，使老师利益与学生水平绑定。", "evidence": "P038", "ambiguity": "分红的具体形式、比例、期限本文未说明。"},
    {"term": "尊师", "meaning": "作者列为补充第一条，并称其理由与技术细节需专门讨论。", "evidence": "P023", "ambiguity": "本文未展开尊师的具体内容，紧接的 P024 是一句设问。"}
   ],
   "examples_and_targets": [
    "“上一节教了你这叫正弦，下一节你就最好不要再指着这个扶额‘这个啥来着....那个啥……’”——作者举的不使用所学话语体系的反例（P028）",
    "“师徒online”——作者对把教学当作陪伴娱乐的讽喻（P031）",
    "“我出钱你出力，为什么学生就得更尊敬老师？”——作者列出的待专门讨论的设问，疑为指向另一篇文章的引题（P024）",
    "“老师傅怕绝活教给你自己没饭吃”——作者主动提出并回应的顾虑（P040）",
    "“学费”“排队等着交学费的人”——作者用来说明金钱不构成被教的充分条件（P032）"
   ],
   "conditions": [
    "“在时间、数量、质量上的任何一方面不达标”——P007 的讨论以不达标为条件。",
    "“对于不是很闲的人来说”——P012 明确把“不优先→停止”的推断限定在不闲的人。",
    "“有的作业布置的难度很高、量很大”——P013 的超额判定以此为前提。",
    "“如果你学了不准备致用”——P033 的失望与失败判断是条件句。",
    "“你不是想学来致用，麻烦你先说清楚”——P032 要求事先声明意图。",
    "“这对某些老师傅仍然不够”——P040 承认分红机制对部分老师傅仍不足。"
   ],
   "rhetoric_and_tone": "问答体中的训诫与规劝语气：大量使用第二人称“你”，以“记住了”“说白了”“不信你试试”等口语短句推进；用反问（“到底你想要搞哪样？”“学生是不是可以放弃改变自己的命运？”）施压；对“等额完成”作贬抑式评价（“只是足够礼貌”），对老师一方的付出作道义强调。",
   "unresolved_questions": [
    "P024“我出钱你出力，为什么学生就得更尊敬老师？”在渲染中被标为 lexical 未覆盖片段，疑为混入正文的文章链接标题或引题，主体与归属不明。",
    "本篇 text 与 lexical 存在分歧（divergence=true），P024 处 lexical 未覆盖，是否影响段落划分需人工复核。",
    "“分红”的具体形式、比例与期限，本文未说明。",
    "“超额”的判定标准依赖老师“心里那杆秤”，本文未给出可操作标准。",
    "“尊师”的具体内容被作者推给“专门讨论”，本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "永远超额完成作业。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "给你布置作业，就是对你有所承诺，承诺了你做好作业会有下一步的审阅和反馈。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "给你布置作业，就是对你花了心血。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "表示你只是足够礼貌", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "因为只是“足够礼貌”是不够资格的。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "在时间、数量、质量上的任何一方面不达标，不要谈任何为什么不达标的理由。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "所以根本没有必要解释，因为肯定成立。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "学习是改变命运的事。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "为什么做不到的理由只能让你免于惩罚，改变不了你的命运。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "“不优先”自然而然会演变成“停止”，而好老师没可能很闲。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "也许你完成一半就已经是超额了", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "教与学，说穿了是一件你敬我一尺，我敬你一丈的事。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P015", "quote": "任何一方的不敬，都意味着实质的宣告放弃。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P020", "quote": "真正的秘诀是——想办法使得教你成为一种享受。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P021", "quote": "“高质量完成作业”之所以很关键，是因为它是“使得教你成为一种享受”的一项关键内容。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P023", "quote": "尊师是一件非常复杂的事情，它的理由、技术细节本身是一个需要专门讨论的问题。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P027", "quote": "第一，是要对所学到的话语体系学以致用。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P029", "quote": "第二，是拿教你的东西做出有用、有趣的东西来。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P033", "quote": "如果你学了不准备致用，你就注定令人失望。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P034", "quote": "过得两三个月，你还记得什么？", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P035", "quote": "学生学以致用，是一个老师产生强烈使命感和责任感的高效板机。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P037", "quote": "这对几乎所有的老师都有最大的激励效果。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P038", "quote": "你学得多好直接关系到老师的未来收益", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P040", "quote": "因为怕绝活教给你自己没饭吃，这是人之常情。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P041", "quote": "那实际上是指你分红分得不够，对方信不过。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P044", "quote": "你做到这几条，想没出息都很难。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "学习与成长", "师生关系"],
   "issue_candidates": ["如何获得他人的传授", "作业与学习态度", "尊师", "学以致用", "师徒利益绑定"],
   "text_function_candidates": ["答疑", "经验总结", "训诫式规劝"],
   "object_candidates": ["学生", "老师", "老师傅", "知乎提问者"],
   "working_keywords": ["超额完成作业", "等额完成", "足够礼貌", "使得教你成为一种享受", "学以致用", "尊师", "分红", "顺风车", "朽木不可雕也"]
  },
  "notes": "问答体：Q001 为提问者问如何让别人心甘情愿地教，作者的回答全部是学习者一侧的条件与做法，未把提问者立场当作作者立场。本篇 text 与 lexical 有分歧（divergence=true）：P024“我出钱你出力，为什么学生就得更尊敬老师？”为 lexical 未覆盖片段，疑为引题/链接标题混入正文，已在 unresolved_questions 登记。无图片节点。"
 },
 "0c2ac588": {
  "analysis": {
   "question_context": "提问者（Q001）问“女孩子用身体交换自己的未来是否值得？”。作者的回应不讨论该交易是否值得，而是先反驳问题预设：一切未来都是用身体换的，并指问题的措辞本身带有恶心感。提问者的“是否值得”框架未归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "以连续反问反驳提问预设：任何未来都是用身体换的，程序员、设计师、销售员乃至爱因斯坦都不例外。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P006"], "summary": "指出问题措辞本身渗透着恶心感，言下之意是“女孩子的身体”只能拿来做性交易。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "以反问指出对男性说“不能用身体换未来”实际等于劝人不要熬夜工作、拼命学习、过度训练；并以“呸！！！”表达斥责。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "收束：身体何止可以换自己的未来，还可以换一个国家的未来。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有任何未来不是用身体换的：写代码、画图、扫街、用大脑想相对论都属于用身体换未来。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该问题的表达方式渗透着恶心感，其言下之意是“女孩子的身体”只能拿来做性交易。", "evidence": ["E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问道：对男性说“不能用身体换未来”，不就是在劝人不要熬夜工作、不要拼命学习、不要过度训练吗？", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "身体何止可以换自己的未来，还可以换一个国家的未来。", "evidence": ["E006"]}
   ],
   "argument_steps": [
    "不回答“是否值得”，而以反问列举写代码、画图、扫街、想相对论，指出一切未来都用身体换（P001-P005）。",
    "转而审视问题措辞，指出其言下之意是把女孩子身体限定为只能做性交易（P006）。",
    "用男性能否被同样劝告的反问，暴露原说法的不对称（P007）。",
    "以斥责词与“还可以换一个国家的未来”收束（P008-P009）。"
   ],
   "concept_usage": [
    {"term": "身体", "meaning": "本文把身体扩展到包含大脑在内的劳动与消耗载体（“难道大脑不算身体？”）。", "evidence": "P005", "ambiguity": "作者未界定“用身体换”与“用身体工作”的边界。"},
    {"term": "用身体换未来", "meaning": "被作者普遍化为一切职业与活动的共同形式，用以消解提问中特指性交易的用法。", "evidence": "P001", "ambiguity": "作者未讨论该短语在性交易语境下的特殊含义。"}
   ],
   "examples_and_targets": [
    "程序员写代码、设计师画图、销售员扫街——作者用于反驳“身体换未来”特殊性的类比（P002-P004）",
    "爱因斯坦用大脑想相对论——作者用于把“大脑”并入“身体”的例证（P005）",
    "提问者的原问题“女孩子用身体交换自己的未来是否值得？”——作者的反驳对象（Q001，属提问者，非作者立场）"
   ],
   "conditions": [
    "“对男性说一句‘不能用身体换未来’”——P007 的反问以对男性说这句话为条件。",
    "图片节点未核验，正文与图片的关系不明。"
   ],
   "rhetoric_and_tone": "短句反问连发，语气激烈斥责：以“难道不是”“就不是”排比反问，末段用“呸！！！”直接表达厌恶，并以“还可以换一个国家的未来”作夸张式收束。",
   "unresolved_questions": [
    "本篇含 6 个图片节点（IMG001..IMG006），图片内容未经核验，需人工/多模态复核；正文与图片的关系不明。",
    "以“换一个国家的未来”指什么、由谁完成，本文未说明。",
    "作者未回答原问题的“是否值得”，也未给出替代判断标准。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "有什么未来不是用身体换的？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "销售员扫街难道不是用身体扫的？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "爱因斯坦用大脑想相对论，难道大脑不算身体？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "这个问题本身用的就是一种恶心感渗透到字缝里的表达", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "为啥就是在劝人不要熬夜工作、不要拼命学习、不要过度训练？", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "还可以换一个国家的未来。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别议题", "社会伦理", "劳动与身体"],
   "issue_candidates": ["身体与未来交换的说法", "性交易与劳动的类比", "提问措辞中的性别预设"],
   "text_function_candidates": ["答疑", "驳论", "情绪化短评"],
   "object_candidates": ["女性", "男性", "程序员", "设计师", "销售员", "爱因斯坦"],
   "working_keywords": ["用身体换", "性交易", "恶心感", "熬夜工作", "过度训练"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 6 个图片节点（IMG001..IMG006），图片内容未经核验，需图像核验；已读部分为正文文本。无图片文字可据，故未据图片补写任何正文。Q001 属提问者，其“是否值得”框架未归给作者；作者实际做的是反驳问题预设。"
 },
 "64b86806": {
  "analysis": {
   "question_context": "提问者（Q001）问“放弃使用「她」字是性别歧视，还是男女平等？”，要求在该二选一框架内作答。作者未接受这个二选一，而是陈述自己的用字习惯与主张：一直用“ta”指代包含男女两种可能的第三人称并提倡如此，并另提一个造字方案。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "陈述并提倡自己的用法：用“ta”指代包含男女两种可能的第三人称。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "提出一个造字方案：用“且也”替代“他”专指男性第三人称，以便把“人也”归还给无特指第三人称。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "限定：历史转变缓慢，只能耐心等待将来。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自己一直用“ta”指代包含男女两种可能的第三人称，并且提倡这种用法。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为有一个造字可以替代“他”来专指男性第三人称，以便把“人也”归还给无特指第三人称，这个字就是“且也”。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为历史的转变是缓慢的，只能耐心期之以将来。", "evidence": ["E004"]}
   ],
   "argument_steps": [
    "先说明自己的既有用法（用 ta 指代男女两种可能）并表明提倡（P001-P002）。",
    "给出替代方案：造字“且也”专指男性第三人称，把“人也”归还无特指第三人称（P003）。",
    "以“历史的转变是缓慢的”作让步与预期管理，主张耐心等待（P004）。"
   ],
   "concept_usage": [
    {"term": "ta", "meaning": "作者用来指代包含男女两种可能的第三人称的写法。", "evidence": "P001", "ambiguity": "作者未说明该写法在正式书面语中的规范依据。"},
    {"term": "且也", "meaning": "作者提出的造字，用以替代“他”专指男性第三人称。", "evidence": "P003", "ambiguity": "字形、读音、是否已有使用或收录，本文未说明。"},
    {"term": "人也", "meaning": "作者认为应从“他”字中归还给无特指第三人称的构字成分。", "evidence": "P003", "ambiguity": "作者未解释“人也”与“他”的字源关系依据。"}
   ],
   "examples_and_targets": [
    "“且也”造字方案——作者自己提出的用字建议（P003）",
    "提问者的二选一框架（放弃使用「她」字是性别歧视还是男女平等）——作者未在其内作答（Q001，属提问者）"
   ],
   "conditions": [
    "“但是历史的转变是缓慢的”——P004 对方案落地时间的限定，语气是等待将来。"
   ],
   "rhetoric_and_tone": "极简陈述体，语气平和、主张明确：以“我一直用……”“并且提倡如此”直接表态，末句用“只能耐心期之以将来”表示对长期等待的接受，无讽刺或论战色彩。",
   "unresolved_questions": [
    "作者未回答提问者“放弃使用「她」字是性别歧视还是男女平等”的二选一问题。",
    "“且也”的字形、读音、使用与收录情况，本文未说明。",
    "作者未说明“ta”作为第三人称写法在书面语中的规范依据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "我一直用ta来指代包含男女两种可能的第三人称。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "并且提倡如此。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "就是 “且也”。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "但是历史的转变是缓慢的，只能耐心期之以将来。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言学与文字", "性别议题"],
   "issue_candidates": ["第三人称代词的性别问题", "汉字造字与用字改革", "「她」字的使用"],
   "text_function_candidates": ["答疑", "表态", "建议"],
   "object_candidates": ["作者本人", "提问者"],
   "working_keywords": ["ta", "她", "他", "且也", "人也", "无特指第三人称"]
  },
  "notes": "问答体：Q001 为提问者的二选一问题，作者未在其框架内作答，提问者立场未归给作者。无图片节点。立场性表述（“提倡如此”）为作者明示。"
 },
 "fb61d5d3": {
  "analysis": {
   "question_context": "提问者（Q001）问“明明是自己在理，明明对方是强盗逻辑，可就是不能有力反驳，怎么办？”。作者先不做反驳技巧指导，而是重新界定“强盗逻辑”这一概念并划出误用边界，最后指出要处理的是强盗问题而非逻辑问题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以设问引出定义：强盗逻辑是一种并不自洽、但因对方掌握暴力手段而使人不敢反驳的论证逻辑。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "划界与辨析：只是感情上不能接受、理智上找不到漏洞，且不存在对方以非法暴力实施结论，不能算强盗逻辑；强盗逻辑的关键是逻辑不连贯，若对方站在法庭上其论证不堪一击；把不喜欢的论证一律定性为强盗逻辑是常见逻辑错误，只流露自身脆弱。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "给出应对方向：真正遇到强盗以暴力主张逻辑断裂的论证时，主要问题是强盗问题而非逻辑问题；强盗实施的不是学术讨论，如指鹿为马的意义不在动物分类学。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "结论：强盗问题解决后，逻辑问题不解决也自然迎刃而解。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强盗逻辑是指一种并不自洽，但因为对方掌握着暴力手段、于是你不敢反驳的论证逻辑。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果只是感情上无法接受、理智上找不到漏洞，且不存在对方用非法暴力实施结论的问题，就不能归类为强盗逻辑。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强盗逻辑的关键在于它逻辑不连贯、存在脱节；若对方不是法外强盗而站在法庭上，其论证不堪一击，全靠无法被缉拿才使荒谬论证可以被拿来说嘴。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把自己不喜欢但找不到问题的论证定性为强盗逻辑，是一种常见的逻辑错误，并不显示对方的荒谬蛮横，只是流露了自身的脆弱。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果确实遇到强盗凭暴力主张逻辑断裂的荒谬论证，要处理的主要问题不是逻辑问题，而是强盗问题。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强盗实施的并不是一种学术讨论，逻辑不逻辑不是那场宣讲会的要义所在，就像指鹿为马的意义并不在动物分类学上。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强盗问题解决了，逻辑问题不需要解决也自然迎刃而解。", "evidence": ["E008"]}
   ],
   "argument_steps": [
    "设问“强盗逻辑到底是什么东西”，随即给出定义：不自洽＋对方掌握暴力手段＋你不敢反驳（P001-P002）。",
    "用反例划界：仅情感上不接受、理智上无漏洞、无非法暴力实施结论者，不算强盗逻辑（P003）。",
    "说明关键在逻辑脱节，并以“站在法庭上不堪一击”假定情形反衬暴力才是支撑（P004）。",
    "指出误用该词是常见逻辑错误，暴露的是自身脆弱（P005）。",
    "转向应对：真正遇到强盗时，主要问题是强盗问题（P006）。",
    "以指鹿为马作类比，说明那不是说理场合（P007）。",
    "结论：强盗问题解决，逻辑问题自然解决（P008）。"
   ],
   "concept_usage": [
    {"term": "强盗逻辑", "meaning": "并不自洽、因对方掌握暴力手段而使人不敢反驳的论证逻辑；作者强调其关键在逻辑不连贯且依赖法外暴力。", "evidence": "P002", "ambiguity": "作者同时指出该词常被误用于自己不喜欢的论证（P005）。"},
    {"term": "强盗", "meaning": "掌握暴力手段、无法被缉拿、不在法庭与学术讨论秩序内的一方。", "evidence": "P004", "ambiguity": "是否包括合法强制力（如法律制裁）本文未说明。"},
    {"term": "指鹿为马", "meaning": "作者用作类比，说明此类宣讲的意义不在逻辑或分类学，而在权力宣示。", "evidence": "P007", "ambiguity": "作者未展开该典故的史实细节。"}
   ],
   "examples_and_targets": [
    "“ta站在法庭上，ta的论证是不堪一击的”——作者设定的反事实情形，用于说明暴力才是支撑（P004）",
    "指鹿为马——作者用作类比，说明强盗场合的要义不在逻辑（P007）",
    "提问者所说“明明自己在理，明明对方是强盗逻辑”——作者重新界定该词，隐含对提问者用法的限定（Q001 属提问者）"
   ],
   "conditions": [
    "“如果你只是纯粹感情上无法接受对方的论证结果，但从理智上找不到对方的漏洞”——P003 的排除条件。",
    "“如果ta不是一个法外的强盗，而是站在法庭上”——P004 的反事实假设。",
    "“如果确实遇到了强盗凭着自己的暴力主张一种逻辑断裂的荒谬论证”——P006 的适用条件。",
    "“全靠ta是一个无法被缉拿的强盗”——P004 表明该情形以对方无法被追究为前提。"
   ],
   "rhetoric_and_tone": "概念辨析体的纠正语气：先设问后自答给定义，再以条件句划界；批评用语直接（“只是流露了自身的脆弱”），并用“指鹿为马”作类比收束，带训诫与去魅意味。",
   "unresolved_questions": [
    "作者未给出“强盗问题”的具体处理办法，只说明它不是逻辑问题。",
    "“掌握着暴力手段”是否包含合法强制力，本文未说明。",
    "P004 中“ta”所指（使用强盗逻辑的一方还是强盗本人）未明确区分。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "强盗逻辑是指一种并不自洽，但是因为对方掌握着暴力手段，于是你不敢反驳的论证逻辑。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "那么这并不能归类为强盗逻辑。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "强盗逻辑的关键在于它逻辑不连贯，其实是存在脱节的", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "全靠ta是一个无法被缉拿的强盗，所以才使得那个荒谬的论证可以被拿来说嘴。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "而只是流露了自身的脆弱。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "你要处理的主要问题不是逻辑问题，而是强盗问题。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "就像指鹿为马的意义并不在于动物分类学上。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "强盗问题解决了，逻辑问题不需要解决也自然迎刃而解。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["逻辑与论证", "语言与概念辨析", "权力与暴力"],
   "issue_candidates": ["强盗逻辑的定义", "论证中的人身强制", "逻辑谬误的误用"],
   "text_function_candidates": ["答疑", "概念辨析", "驳论"],
   "object_candidates": ["强盗", "法庭", "指鹿为马"],
   "working_keywords": ["强盗逻辑", "不自洽", "暴力手段", "逻辑不连贯", "脱节", "指鹿为马", "宣讲会"]
  },
  "notes": "问答体：Q001 属提问者，作者未直接提供反驳技巧，而是重定义概念并指出真遇到强盗时主要问题是强盗问题；提问者对该词的用法被作者隐含限定，未归给作者。无图片节点。文中“ta”指代对象在 P004 未明确，已登记。"
 },
 "0af76841": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么受过高等教育的人也会迷信（信神信星座信宗教）？”。作者不接受该问题的前提，先贬低“本科高等教育”的实际水平，再指出提问把神、宗教、星座混为一谈本身就分不清“信”与“迷信”，最后给出解释：迷信是人的本能，超脱迷信是极高门槛。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "重新界定本科高等教育的水平：只是要求高一点的扫盲班；毕业只表示理论上有了开始正经学习的基础能力与知识，约等于鸟有了翅膀和肌肉，离会飞还有距离。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006"], "summary": "反问有几个人真的够资格毕业，并以“给新生腾床位、办手续赶人出院、放弃治疗”讽喻毕业。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "指出提问方对“什么叫信、什么叫迷信”根本分不清；把神、宗教和星座划到一起论证“迷信”属于不知道自己在说什么，本身就是在迷信状态下说话。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "给出解释与门槛：迷信是人的本能，“能超脱迷信”是超凡入圣级别的智慧（佛教为菩萨罗汉乃至佛陀，基督教为圣徒）；名垂千古的思想家也没有几个过得了这条线，起步价是释迦摩尼、苏格拉底、老子这一级。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013"], "summary": "以“别说昏话”收束并斥责。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“本科高等教育”只不过是要求高一点的扫盲班水平；高等教育毕业只表示理论上有了鉴定其他信息真假与高低的基础能力和知识。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "截止毕业这个点，只约等于鸟有了翅膀也有了肌肉，离会飞还有距离。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问到底有几个人真的是够资格毕业的，并称毕业只是为给新生腾床位而办手续赶人出院、放弃治疗。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为把神、宗教和星座划到一起拿来论证“迷信”，属于人还没活醒、不知道自己在说什么的水平；这本身就是在迷信状态下说出来的话。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迷信是人的本能，“能超脱迷信”是超凡入圣级别的智慧水平，在佛教已是菩萨罗汉乃至佛陀，在基督教已是圣徒。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "即使高至名垂千古的思想家，也没有几个过得了这条线；这条线的起步价是释迦摩尼、苏格拉底、老子这一级。", "evidence": ["E009", "E010"]}
   ],
   "argument_steps": [
    "先降低“本科高等教育”的含义：只是要求高一点的扫盲班（P001）。",
    "限定毕业的实际所得：只是理论上有了基础能力与知识，约等于有翅膀有肌肉但还不会飞（P002-P004）。",
    "以反问质疑毕业资格的普遍性，并用“腾床位、赶人出院、放弃治疗”讽喻毕业（P005-P006）。",
    "指出提问方对“信/迷信”分不清，把神、宗教、星座混作一谈本身即在迷信状态下说话（P007-P009）。",
    "给出正面解释：迷信是本能，超脱迷信属超凡入圣级别（P010）。",
    "用思想家也少有过线与“起步价”人物抬高标准（P011-P012）。",
    "以短句斥责收束（P013）。"
   ],
   "concept_usage": [
    {"term": "本科高等教育", "meaning": "作者称其为要求高一点的扫盲班水平，毕业只代表理论上具备基础鉴定能力。", "evidence": "P001", "ambiguity": "作者未说明该评价针对哪一地区或时期的高等教育。"},
    {"term": "迷信", "meaning": "作者称迷信是人的本能，与“能超脱迷信”的极高智慧相对；并反对把神、宗教、星座混为一谈。", "evidence": "P010", "ambiguity": "作者指出他人分不清“什么叫信、什么叫迷信”，但本文未给出自己的定义。"},
    {"term": "这条线", "meaning": "指“能超脱迷信”的门槛。", "evidence": "P011", "ambiguity": "门槛的具体判定标准本文未说明。"}
   ],
   "examples_and_targets": [
    "“只约等于鸟有了翅膀也有了肌肉”“但离会飞还有距离”——作者类比毕业与真正会学的关系（P003-P004）",
    "“给新生腾出床位，所以办个手续赶人出院，放弃治疗”——作者对毕业流程的讽喻（P006）",
    "佛教的菩萨罗汉乃至佛陀、基督教的圣徒——作者用来标示超脱迷信的门槛（P010）",
    "释迦摩尼、苏格拉底、老子——作者所列的“起步价”人物（P012）",
    "“会把神、宗教和星座划到一起拿来论证‘迷信’”——作者批评的说法，与提问者的问题框架相近（提问属提问者）（P008）",
    "“还问为什么别人会迷信”——作者对提问本身的讥讽（P009）"
   ],
   "conditions": [
    "“因为理论上有了足够鉴定其他信息真假与高低的基础能力和知识”——P002 把毕业所得限定为“理论上”。",
    "“但截止毕业这个点”——P003 明确评估的时间点。",
    "“即使高至名垂千古的思想家，也没有几个过得了这条线”——P011 以让步句式抬高标准。"
   ],
   "rhetoric_and_tone": "训诫与讥讽并用的语气：以“摸摸自己的良心”“你摸摸看还有多远”“别说昏话”直接对读者施压；用“活幽默”讥讽提问；以“扫盲班”“放弃治疗”“腾床位”等贬抑比喻重述毕业，反问句密集。",
   "unresolved_questions": [
    "作者批评他人分不清“什么叫信、什么叫迷信”，但本文未给出作者自己的“信/迷信”定义。",
    "“这条线”的具体判定标准，本文未说明。",
    "“有几个人真的是够资格毕业”是反问，作者未提供任何数据。",
    "作者未说明其高教评价所针对的地区、时期与学校类型。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "“本科高等教育”其实只不过是个要求高一点的扫盲班水平而已。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "只是表示有了一些开始正经的学习的基础", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "只约等于鸟有了翅膀也有了肌肉。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "到底有几个人真的是够资格毕业的？", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "那只是因为要给新生腾出床位，所以办个手续赶人出院，放弃治疗罢了。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "就属于人还没活醒、不知道自己在说什么的水平。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "这本身就是在迷信状态下说出来的话", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "迷信是人的本能，“能超脱迷信”是超凡入圣级别的智慧水平。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "也没有几个过得了这条线的。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "起步价就是释迦摩尼、苏格拉底、老子这一级", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "宗教与信仰", "认知与迷信"],
   "issue_candidates": ["高等教育的实际水平", "迷信与信仰的区分", "受过高等教育者为何迷信"],
   "text_function_candidates": ["答疑", "驳论", "训诫式批评"],
   "object_candidates": ["本科高等教育", "神", "宗教", "星座", "佛教", "基督教", "释迦摩尼", "苏格拉底", "老子"],
   "working_keywords": ["扫盲班", "迷信", "本能", "超凡入圣", "菩萨罗汉", "圣徒", "这条线", "活幽默"]
  },
  "notes": "问答体：Q001 属提问者，其“信神信星座信宗教”被作者当作批评对象（把神、宗教、星座划到一起），提问者立场未归给作者。无图片节点。作者未给出“信/迷信”的正面定义，已登记为未决问题。"
 },
 "5d1eba64": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么，这几年教育培训机构频繁倒闭？”。作者不列举经营或政策原因，而给出一个行业性质层面的答案：教育行业必须由教育家来做，而这一代办教育机构的人多是把其他行业的市场运营成功经验搬过来，缺的正是教育家。提问者的“频繁倒闭”现象描述未归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接给出答案：教育行业必须要有教育家来做；并声明这句看似废话的话其实不是废话。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "历史语境与批评对象：改革开放释放市场经济机制，造就一批不掌握专业优势而掌握市场运营优势的生意人的普遍成功；其秘诀是取平均水平的专业班底再补市场交互短板，专业不用好、生意做好即可，全国分销渠道卖低水平产品也能成功；这种特殊机遇造成“专业不重要、模式才重要”的迷信。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "把上述模式套到教育上的表现：发明小班制就叫“教育事业”，上线在线约课功能就叫“教育机构”，愁的都是生源与教学资源，仍在玩“资源整合”。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "行业性质论证：教育是最古老的职业，短板永远在内容与精神内核而非形式；教育行业必须以教育家为主体，只有“优质老师”加“有力市场营销”活不了；有教育家才有资格求活，否则只能运营一两年、只有这么长时间收回投资，其余要素都只是“一次性耗材”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "对教育家的要求与定义：教育家必须是老板本人并在体系中掌握至高无上的权利；只能由教育家补经营短板，不能由生意人补师资短板；教育家指把人生黄金时段与主要价值用在教育上、对教育有宗教性虔诚的人，即“赚钱是为了教书”而非“教书是为了赚钱”的人。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P023", "P024"], "summary": "以两句反问收束：你有吗？你没有，你还奇怪你为什么会垮？", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育行业必须要有教育家来做；作者称这句看似废话的话其实并不是废话。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国改革开放以后释放的第一要素是市场经济机制，因此出现了一大批不掌握专业优势、但掌握市场运营优势的生意人的普遍成功。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这批生意人的成功秘诀是取平均水平的专业班底、只补市场交互短板；“专业不用好，只要生意做得好就行”，全国性分销体系即使卖低水平产品也能获得极大成功。", "evidence": ["E004", "E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种因特殊历史阶段造就的特殊机遇，给那一代人乃至直到这一代国人留下了“专业不重要、模式才重要”的迷信。", "evidence": ["E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把上述模式用于教育，表现为发明小班制就搞“教育事业”、上线在线约课功能就搞“教育机构”，其关注点仍是生源与教学资源，即所谓“资源整合”。", "evidence": ["E008", "E009", "E010", "E011"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育是人类最古老的职业，其短板永远不在教育形式如何优化，而在教育的内容与精神内核如何优化。", "evidence": ["E012", "E013"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育行业是必须以教育家为主体的行业；不是有“优质的老师”和“有力的市场营销”就能活，有教育家才有资格求活。", "evidence": ["E014", "E015", "E016"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "否则（没有教育家）只能运营一两年，只有这么长时间收回投资；因为没有教育家，其他一切要素都只是“一次性耗材”，不是要耗尽就是要过期作废。", "evidence": ["E017", "E018"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育家必须是老板自己并在整个体系中掌握至高无上的权利；只能是教育家补足经营能力的短板，而不能是生意人补足“师资”的短板。", "evidence": ["E019", "E020"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓教育家，指把自己人生黄金时段和主要价值都用在教育上、对教育事业有宗教性虔诚的人，即“赚钱是为了教书”而不是“教书是为了赚钱”的人。", "evidence": ["E021", "E022"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问要求办教育机构者自问是否具备教育家条件，并断言没有就会垮。", "evidence": ["E023", "E024"]}
   ],
   "argument_steps": [
    "先给结论：教育行业必须要有教育家来做，并预告这不是废话（P001-P002）。",
    "铺陈历史语境：改革开放释放市场机制，造就不懂专业但懂运营的生意人的普遍成功（P003）。",
    "描述其模式：平均水平专业班底＋补市场交互短板，靠渠道而非专业取胜（P004-P006）。",
    "指出由此形成“专业不重要、模式才重要”的迷信（P007）。",
    "举教育领域的具体表现：小班制叫教育事业、约课功能叫教育机构，仍做“资源整合”（P008-P011）。",
    "转向行业性质：教育最古老，短板在内容与精神内核而非形式（P012-P013）。",
    "推出规范性结论：必须以教育家为主体，有教育家才有资格求活（P014-P016）。",
    "给出反证式后果预测：否则只能运营一两年，其他要素皆为一次性耗材（P017-P018）。",
    "补充权力与补短板方向：教育家必须是老板本人（P019-P020）。",
    "定义教育家（P021-P022），以反问收束（P023-P024）。"
   ],
   "concept_usage": [
    {"term": "教育家", "meaning": "本文定义为把自己人生的黄金时段和主要价值都用在教育上、对教育事业有宗教性虔诚的人，即“赚钱是为了教书”而非“教书是为了赚钱”的人；且必须是老板本人并掌握至高无上的权利。", "evidence": "P021", "ambiguity": "本文未给出可操作的判定标准，也未说明如何识别。"},
    {"term": "市场经济机制", "meaning": "作者称中国改革开放以后释放的第一要素，是那批生意人成功的条件。", "evidence": "P003", "ambiguity": "本文未展开该机制的具体内容与时间范围。"},
    {"term": "资源整合", "meaning": "作者对教育机构只关注生源与教学资源的做法的贬称。", "evidence": "P011", "ambiguity": "作者用“所谓”加引号，未给出该词在其用法中的严格定义。"},
    {"term": "一次性耗材", "meaning": "作者称没有教育家时，其他一切要素（如师资、营销）都会耗尽或过期作废。", "evidence": "P018", "ambiguity": "作者未说明耗尽的周期与判定方式。"}
   ],
   "examples_and_targets": [
    "“发明个小班制，就搞一个‘教育事业’”“上线个在线约课的小功能，也搞个‘教育机构’”——作者讽刺的行业内做法（P008-P009）",
    "“生源”和“教学资源”、“资源整合”——作者点出的机构关注点与其贬称（P010-P011）",
    "“优质的老师”和“有力的市场营销”——作者认为不足以支撑教育机构的条件（P015）",
    "“一次性耗材”——作者对无教育家条件下其他要素的比喻（P018）",
    "“赚钱是为了教书”“教书是为了赚钱”——作者用来区分教育家与生意人的对举（P022）",
    "提问者所述的“这几年教育培训机构频繁倒闭”——作者的回应对象，作者未引用具体案例或数据（Q001，属提问者）"
   ],
   "conditions": [
    "“中国改革开放以后释放的第一要素就是市场经济机制”——P003 把该现象限定在特定历史阶段。",
    "“一个渠道遍及全国的分销体系”——P006 的成功以渠道规模为条件。",
    "“有教育家，你才有资格求活”——P016 以具备教育家为前提。",
    "“否则你最好提前脑子清醒一点——你只能运营一两年”——P017 以没有教育家为条件给出后果预测。",
    "“而且教育家必须是老板自己，在整个体系中掌握至高无上的至高无上的权利”——P019 对权力位置提出条件。"
   ],
   "rhetoric_and_tone": "训诫与行业批评语气：先立判断再自辩“看似一句废话，其实并不是”；用“所谓”“迷信”“还是在玩……这一套”等贬抑措辞批评同行；以“你有吗？”“你还奇怪你为什么会垮？”的反问直接施压；多处使用引号标示其所不认可的说法（“教育事业”“教育机构”“资源整合”“优质的老师”）。",
   "unresolved_questions": [
    "作者未提供任何关于教育培训机构倒闭的统计、案例或时间范围，问题中的“频繁倒闭”仅被当作现象背景。",
    "“教育家”如何识别与判定，本文未给出可操作标准。",
    "“你只能运营一两年”这一期限的依据，本文未说明。",
    "“教育家必须是老板自己，在整个体系中掌握至高无上的权利”是否适用于公立或非营利教育机构，本文未说明。",
    "作者称“直到这一代国人仍然固有的迷信”，所指群体范围本文未界定。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "因为教育行业必须要有教育家来做。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "这看似一句废话，其实并不是。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "中国改革开放以后释放的第一要素就是市场经济机制", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "我只取一个平均水平的专业班底，然后提升它与市场交互方面的短板就可以了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "专业不用好，只要生意做得好就行。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "即使卖的只是行业中的低水平产品，也可以获得极大的成功。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "以为专业不重要，模式才重要。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "发明个小班制，就搞一个“教育事业”", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "上线个在线约课的小功能，也搞个“教育机构”", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "愁的都是“生源”和“教学资源”。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "还是在玩所谓“资源整合”这一套。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "教育是人类最古老的职业。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "而在于教育的内容、教育的精神内核要如何优化。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "教育行业，是必须以教育家为主体的行业。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "不是你有所谓“优质的老师”和“有力的市场营销”就能活的。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P016", "quote": "有教育家，你才有资格求活。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P017", "quote": "你只能运营一两年，只有这么长时间收回投资。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P018", "quote": "一切其他的一切要素都只是“一次性耗材”", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P019", "quote": "教育家必须是老板自己", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P020", "quote": "只能是教育家补足经营能力的短板，而不能是生意人补足“师资”的短板。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P021", "quote": "所谓教育家，是指把自己人生的黄金时段和主要价值都用在教育上的那一批人", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P022", "quote": "那种“赚钱是为了教书”、而不是“教书是为了赚钱”的人。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P023", "quote": "你有吗？", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P024", "quote": "你没有，你还奇怪你为什么会垮？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "商业与经营", "中国经济与改革"],
   "issue_candidates": ["教育培训机构倒闭原因", "教育行业的专业性", "教育家与生意人的关系", "市场运营模式能否移植到教育"],
   "text_function_candidates": ["答疑", "行业批评", "论辩"],
   "object_candidates": ["教育家", "生意人", "教育培训机构", "中国改革开放", "新生", "老师"],
   "working_keywords": ["教育家", "市场经济机制", "市场运营优势", "专业班底", "资源整合", "一次性耗材", "小班制", "赚钱是为了教书"]
  },
  "notes": "问答体：Q001 属提问者，其“教育培训机构频繁倒闭”的现象描述与“为什么”的提问框架未归给作者；作者未引用任何机构名称、统计或政策。作者对“教育家”的界定为本文自述，未给判定标准，已登记为未决问题。无图片节点。"
 },
 "00f9eb3c": {
  "analysis": {
   "question_context": "提问者（Q001）问“袁崇焕杀毛文龙，是不是和秦桧杀岳飞是一个道理？”。作者不接受这一类比：先指出两事在程序合法性上相反，再说明袁崇焕此举的真正后果是撕毁官僚集团的最大契约，最后比较两人水平并把责任归于崇祯与组织选拔机制。提问者的“一个道理”框架属于提问者，作者明确否定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以两句程序判断否定类比：秦桧杀岳飞走合法程序，袁崇焕杀毛文龙非法，故没有任何“一样道理”可言。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "说明后果：此举撕毁官僚集团自己的最大契约，从此忠诚无意义；这种损失无法由暂时的军事胜利挽回，因为此后胜利本身成了“成功经验”的证明，“越胜利”组织崩溃越快。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "用公司类比：偷了公司一笔钱却谈了个大单，仍必须被定义为失败；若反过来认定为成功、果敢并开表彰大会，企业下场可想而知；况且这里是偷钱又丢了大单。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015"], "summary": "人物比较与归因：袁崇焕与秦桧水平差距不可以道里计；秦桧可算政治家，只是撞在儒家借古讽今的枪口上；袁崇焕才干胸襟有限，放在该位置是组织选拔机制彻底失控的结果；严格说是崇祯的无能害死毛文龙，袁只是随时可能爆炸的硝化甘油，这与美国人民绝望到选川普当总统没有本质区别。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "秦桧杀岳飞是走合法程序的，而袁崇焕杀毛文龙是非法的。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "两件事之间没有任何“一样道理”可言。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "袁崇焕杀毛文龙算是撕毁了官僚集团自己的最大契约，从此忠诚无意义了。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种损失不是任何暂时的军事胜利可以挽回的，因为从此开始胜利本身就是“此为成功经验”的证明。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越“胜利”，组织崩溃越快。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“偷了公司一笔钱却谈了个大单”为喻：这必须被定义为失败，而不能算成功。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者假设若反过来把此事认定为成功、果敢并开表彰大会，则企业下场不言自明；况且这里是偷钱又丢了大单。", "evidence": ["E010", "E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "袁崇焕和秦桧比，水平差距不可以道里计；秦桧实打实还可以算政治家，他只是撞在了儒家借古讽今的枪口上。", "evidence": ["E012", "E013"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "袁崇焕才干胸襟都有限得很，把他放在那个位置上是一种组织选拔机制彻底失控的结果。", "evidence": ["E014"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "严格意义上说，是崇祯的无能害死了毛文龙，袁崇焕只是一瓶放在哪里都随时可能爆炸的硝化甘油。", "evidence": ["E015"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此事跟美国人民绝望了连川普都选来当总统没有本质的区别。", "evidence": ["E016"]}
   ],
   "argument_steps": [
    "先做程序判断：秦桧走合法程序，袁崇焕非法（P001-P002）。",
    "据程序差异直接否定提问者的“一个道理”类比（P003）。",
    "指出真实后果是撕毁官僚集团的最大契约、使忠诚无意义（P004）。",
    "说明该损失不可由军事胜利挽回，并给出“胜利成为成功经验证明→组织崩溃加快”的机制（P005-P006）。",
    "以偷钱谈大单的公司类比说明此类“成功”必须定义为失败（P007-P008）。",
    "以反事实设问强化：若开表彰大会，企业下场如何（P009）。",
    "补一句加重：这里是偷钱还丢了大单（P010）。",
    "比较两人水平并重新定性秦桧（P011-P012）。",
    "把袁崇焕的上位归因于组织选拔机制失控（P013）。",
    "最后把责任指向崇祯的无能，并用硝化甘油与美国大选作类比收束（P014-P015）。"
   ],
   "concept_usage": [
    {"term": "合法程序", "meaning": "作者用以区分秦桧杀岳飞与袁崇焕杀毛文龙的首要标准。", "evidence": "P001", "ambiguity": "作者未说明所依据的法令、程序或史料。"},
    {"term": "官僚集团自己的最大契约", "meaning": "作者称袁崇焕杀毛文龙所撕毁的东西，后果是“从此忠诚无意义”。", "evidence": "P004", "ambiguity": "该契约的具体内容与主体（皇帝、文官集团、武将）本文未说明。"},
    {"term": "“胜利”", "meaning": "作者加引号使用，指在契约已被撕毁之后取得的军事胜利，其效果是反过来证明违规做法是成功经验。", "evidence": "P005", "ambiguity": "作者未指明具体指哪一场或哪几场胜利。"},
    {"term": "硝化甘油", "meaning": "作者对袁崇焕的比喻：才干胸襟有限，放在哪里都随时可能爆炸。", "evidence": "P014", "ambiguity": "比喻的适用范围与作者对袁崇焕的具体评价标准未展开。"}
   ],
   "examples_and_targets": [
    "秦桧杀岳飞、袁崇焕杀毛文龙——提问者提出的类比对象，作者据程序合法性予以否定（Q001 属提问者；P001-P003 为作者回应）",
    "“某人偷了公司一笔钱，结果谈了个大单”——作者用来说明“成功”仍须定义为失败的类比（P007-P008）",
    "“开起表彰大会”——作者反事实假设中的场景（P009）",
    "崇祯——作者指为毛文龙之死的实际责任者（P014）",
    "儒家借古讽今——作者用以解释秦桧被定性的因素（P012）",
    "美国人民选川普当总统——作者用作“绝望之下选拔失控”的类比（P015）",
    "“ta老人家”——P010 中出现的主体，指代对象未在正文明确"
   ],
   "conditions": [
    "“如果反过来认定这是一种成功，一种果敢，还开起表彰大会”——P009 为反事实假设。",
    "“这种损失，不是任何暂时的军事胜利可以挽回的”——P005 以“暂时”限定胜利。",
    "“严格意义上说”——P014 为作者的限定语。",
    "“更不要说ta老人家是偷了公司一笔钱，还丢了个大单了”——P010 以“更不要说”递进，属假设语境下的加重说法。"
   ],
   "rhetoric_and_tone": "短句判断＋类比的说理语气，带明显贬抑与讽刺：以两句程序判断直接切断提问者的类比；给“一样道理”“胜利”“成功经验”加引号表示反讽；用公司偷钱、表彰大会、硝化甘油、选川普等比喻施压；对袁崇焕的评价用词严厉（“才干胸襟都有限的很”“组织选拔机制彻底失控”），对秦桧则作相对区分的评价（“实打实还是可以算政治家的”）。",
   "unresolved_questions": [
    "“秦桧杀岳飞是走合法程序的”“袁崇焕杀毛文龙是非法的”均为作者的历史断言，本文未给出史料、法条或出处，待外部核查。",
    "“官僚集团自己的最大契约”具体指什么、由谁订立，本文未说明。",
    "P010“ta老人家”的指代对象（毛文龙、袁崇焕或他人）在正文中未明确。",
    "“越‘胜利’，组织崩溃越快”所依据的历史范围与经验证据，本文未说明。",
    "美国大选类比与明末史事的可比性边界，作者未作限定。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "秦桧杀岳飞是走合法程序的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "袁崇焕杀毛文龙是非法的。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "没有任何“一样道理”可言。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "算是撕毁了官僚集团自己的最大契约，从此忠诚无意义了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "这种损失，不是任何暂时的军事胜利可以挽回的", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "胜利本身就是“此为成功经验”的证明。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "越“胜利”，组织崩溃越快。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "这就像某人偷了公司一笔钱，结果谈了个大单。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "这必须被定义为失败。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P009", "quote": "如果反过来认定这是一种成功，一种果敢，还开起表彰大会", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P010", "quote": "更不要说ta老人家是偷了公司一笔钱，还丢了个大单了。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P011", "quote": "袁崇焕和秦桧比，水平差距不可以道里计。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P012", "quote": "秦桧实打实还是可以算政治家的，他只是撞在了儒家借古讽今的枪口上。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P013", "quote": "把他放在那个位置上是一种组织选拔机制彻底失控的结果。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P014", "quote": "是崇祯的无能害死了毛文龙，袁崇焕只是一瓶放在哪里都随时可能爆炸的硝化甘油。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P015", "quote": "这跟美国人民绝望了连川普都选来当总统没有本质的区别。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["历史", "明史", "组织与制度", "政治评论"],
   "issue_candidates": ["袁崇焕杀毛文龙与秦桧杀岳飞是否同理", "军事胜利与组织秩序的关系", "明末组织选拔机制", "历史人物评价"],
   "text_function_candidates": ["答疑", "驳论", "历史评论"],
   "object_candidates": ["袁崇焕", "毛文龙", "秦桧", "岳飞", "崇祯", "儒家", "官僚集团", "川普", "美国人民"],
   "working_keywords": ["合法程序", "非法", "最大契约", "忠诚", "成功经验", "组织崩溃", "组织选拔机制", "硝化甘油", "借古讽今"]
  },
  "notes": "问答体：Q001 属提问者，其“是不是一个道理”的类比被作者以“没有任何‘一样道理’可言”明确否定，提问者框架未归给作者。文中史事判断（秦桧走合法程序、袁崇焕非法、崇祯无能等）为作者断言，语料未附出处，已登记为待外部核查。P010“ta老人家”指代未明，已登记。无图片节点。"
 },
 "a09de2e3": {
  "analysis": {
   "question_context": "提问者（Q001）问“这样的AI是真的吗？”，指向语料中未复述的某个AI（本文无图片节点，正文也未描述其形态）。作者不判断该AI的真伪，而是直接指出其底层设定“一开始就不合理”，并以“痛苦最小化优先于收益最大化”重述驱动意志体的逻辑，最后给出模拟人类的建议方向。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "否定式开场与核心命题：一开始就不合理；驱动意志体的基本逻辑是争取痛苦最小化而非收益最大化；收益最大化只是痛苦最小化的一种策略，不是可相提并论的原则。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "以人类行为作证：人类难以实现收益最大化，是因为两者冲突时收益最大化常态性地被放弃；作者评价这是健康的。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "对“贪婪战胜痛苦”作双重否定：这既错误（极大概率甚至必然导致自我毁灭）也不义（造成他人灾难）；作者以“幸亏如此”表态，并称“ta们”同意“这很合理”时就已经双双错误。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "给出模拟人类的方向与后果对照：要模拟人类的懦弱而非贪婪；懦弱会自然衍生出恰到好处的贪婪，真实程度令人吃惊；反过来则得到荒谬结果。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "（针对该AI的设定）一开始就不合理。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "驱动意志体的基本逻辑是争取痛苦最小化，而不是争取收益最大化。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "收益最大化只是痛苦最小化的一种策略，根本不是可以相提并论的原则。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类总是难以实现收益最大化，是因为当收益最大化与痛苦最小化冲突时，收益最大化常态性地被放弃。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述状态是健康的。", "evidence": ["E005"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "人不可以常态性地靠着贪婪战胜痛苦：这既是错误的——会极大概率（甚至必然）导致自己的毁灭，也是不义的——会造成他人的灾难。", "evidence": ["E006", "E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称幸亏如此；并说“ta们”在同意“这很合理”的时候就已经双双错误。", "evidence": ["E008", "E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想要模拟人类，要去模拟人类的懦弱，而不是人类的贪婪。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "懦弱自然会衍生出恰到好处的贪婪，其真实程度会让人吃惊。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果反过来（模拟贪婪），得到的恰恰是这个荒谬的结果。", "evidence": ["E012"]}
   ],
   "argument_steps": [
    "先否定：一开始就不合理（P001）。",
    "给出替代原理：意志体的基本逻辑是痛苦最小化，而非收益最大化（P002）。",
    "压低收益最大化的地位：它只是策略，不是同级原则（P003）。",
    "以人类行为作证：冲突时收益最大化常态被放弃（P004）。",
    "评价该状态为健康（P005）。",
    "用错误与不义双重理由否定“靠贪婪战胜痛苦”（P006）。",
    "以“幸亏如此”表态，并指出“ta们”同意“这很合理”时已双双错误（P007-P008）。",
    "给出正面建议：模拟懦弱而非贪婪（P009）。",
    "预期效果：懦弱衍生恰到好处的贪婪，真实度惊人；反之得到荒谬结果（P010-P011）。"
   ],
   "concept_usage": [
    {"term": "意志体", "meaning": "作者讨论的对象，其行为据作者说由“争取痛苦最小化”驱动。", "evidence": "P002", "ambiguity": "作者未界定意志体是否包括AI，也未说明其与“人类”的关系。"},
    {"term": "痛苦最小化", "meaning": "作者称为驱动意志体的基本逻辑，收益最大化只是它的一种策略。", "evidence": "P002", "ambiguity": "作者未说明痛苦如何度量、由谁判定。"},
    {"term": "收益最大化", "meaning": "被作者降格为策略，并称其在与痛苦最小化冲突时常态性被放弃。", "evidence": "P003", "ambiguity": "作者未给出“收益”的范围（经济收益或其他）。"},
    {"term": "懦弱", "meaning": "作者主张应被模拟的人类特征，称其会自然衍生出恰到好处的贪婪。", "evidence": "P009", "ambiguity": "作者未定义懦弱的具体行为表现，也未说明模拟的技术方式。"},
    {"term": "健康的", "meaning": "作者对“收益最大化常态性被放弃”这一状态的评价。", "evidence": "P005", "ambiguity": "“健康”是就个体、群体还是系统而言，本文未说明。"}
   ],
   "examples_and_targets": [
    "“人类总是难以实现收益最大化”——作者用来说明痛苦最小化优先于收益最大化的经验例证（P004）",
    "“ta们同意‘这很合理’”——作者暗指的某方（疑指该AI的开发者或讨论者），正文未明确所指（P008）",
    "“这样的AI”——提问者所指对象，语料未附描述或图片，作者未复述其细节（Q001，属提问者）"
   ],
   "conditions": [
    "“当收益最大化与痛苦最小化冲突时”——P004 明确给出冲突这一条件。",
    "“人不可以常态性的靠着贪婪战胜痛苦”——P006 以“常态性”为限定。",
    "“这会极大概率（甚至是必然的）导致自己的毁灭”——P006 保留概率与必然的两种强度。",
    "“但你如果反过来”——P011 为假设条件句。"
   ],
   "rhetoric_and_tone": "短句论断体，语气斩截并带价值评判：以“一开始就不合理”直接否定提问所指；用“根本不是可以相提并论的原则”“幸亏如此”表态；以“错误”“不义”作双重定性；末段用“其真实程度会让你吃惊”作预告式收束。",
   "unresolved_questions": [
    "提问（Q001）所指的“这样的AI”在语料中没有描述，本篇也无图片节点（0 张），作者未复述其形态与设定，需外部核查原问题语境。",
    "P001“一开始就不合理”所针对的具体对象（该AI的哪一项设定）本文未说明。",
    "P008“ta们”的指代对象在正文中未明确。",
    "作者未为其“痛苦最小化优先”的命题提供依据或来源，也未说明该命题可否验证。",
    "作者未说明如何在技术上实现“模拟懦弱”。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "一开始就不合理。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "驱动意志体的基本逻辑是争取痛苦最小化，而不是争取收益最大化。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "收益最大化只是痛苦最小化的一种策略，而根本不是可以相提并论的原则。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "因为当收益最大化与痛苦最小化冲突时，收益最大化常态性的被放弃。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "而这是健康的。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "人不可以常态性的靠着贪婪战胜痛苦", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "这会极大概率（甚至是必然的）导致自己的毁灭", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "幸亏如此。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "其实在ta们同意“这很合理”的时候，就已经双双错误了。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P009", "quote": "想要模拟人类，要去模拟人类的懦弱，而不是人类的贪婪。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P010", "quote": "懦弱自然会衍生出恰到好处的贪婪，其真实程度会让你吃惊。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P011", "quote": "但你如果反过来，得到的恰恰是这个荒谬的结果。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人工智能", "行为与动机", "伦理"],
   "issue_candidates": ["AI是否真实", "AI的动机设定", "收益最大化与痛苦最小化", "模拟人类的方式"],
   "text_function_candidates": ["答疑", "评论", "命题式论断"],
   "object_candidates": ["AI", "意志体", "人类"],
   "working_keywords": ["意志体", "痛苦最小化", "收益最大化", "懦弱", "贪婪", "模拟人类", "健康的", "不义"]
  },
  "notes": "问答体：Q001 属提问者（问“这样的AI是真的吗？”），作者未回答真伪，而是否定其设定前提；提问者立场未归给作者。本篇正文无可读图片、无图片节点（0 张），但提问所指的AI对象在语料中无任何描述，已在 unresolved_questions 登记为需外部核查。无图片节点，故按正文文本记为 read。"
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
