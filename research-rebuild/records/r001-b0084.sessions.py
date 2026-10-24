# -*- coding: utf-8 -*-
"""批次 r001-b0084 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0084.sessions.py            # 写 out/r001-b0084.out.jsonl
  python3 records/r001-b0084.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0084"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0084.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e5cc0350": {
  "analysis": {
   "question_context": "提问者问：自己举报同学考试作弊，致其被处分丢了学位证，随后自己好像被全班孤立，自己是否有错（Q001，属提问者语境）。作者不讨论作弊与举报本身的是非细节，直接就提问者的自我怀疑给出判断、出路与后果推演。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回答：提问者没有错。", "role": "conclusion"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "给出路：需要找到一群同样认为这没有错的人，到他们中间生活；世界上确实存在这样的人群。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "若找不到，则只能在“宁可孤独”与“宁可见义不为”之间自行选择。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007"], "summary": "限定归因并推演后果：选见义不为是软弱而非正确或明智；后一种自我认知会恶化生活圈，滑入无耻人群并受折磨。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者举报作弊同学后被孤立，这件事上提问者没有错。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者需要的是找到一群同样认为这没有错的人并到他们中间生活；世界上确实存在这样的人群。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果找不到这样的人群，那么在宁可孤独与宁可见义不为之间的取舍属于提问者自己的选择问题。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果选择了见义不为，那是因为自己软弱（软弱可以原谅），而不是因为那样是“对的”“更明智的”。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把见义不为认知为正确虽会让人舒服一些，却会逐渐恶化生活圈，使人无可抗拒地滑落到无耻的人中间，每天被无耻折磨。", "evidence": ["E006", "E007"]}
   ],
   "argument_steps": [
    "先给结论：你没有错（P001）",
    "给出出路：找到认同这没有错的人群并生活在其中（P002）",
    "确认该人群存在（P003）",
    "设定条件：找不到时在孤独与见义不为之间自选（P004）",
    "限定归因：选见义不为是软弱，不是正确或明智（P005）",
    "推演后果：错误自我认知会恶化生活圈直至如入地狱（P006、P007）"
   ],
   "concept_usage": [
    {"term": "错", "meaning": "就提问者举报作弊后被孤立的处境判断其没有错，本文未展开界定标准", "evidence": "P001", "ambiguity": "判断依据本文未说明"},
    {"term": "见义不为", "meaning": "面对同学作弊而不坚持是非的选项", "evidence": "P004", "ambiguity": "“义”的具体所指本文未展开"},
    {"term": "软弱", "meaning": "对选择见义不为的归因，作者认为可以原谅", "evidence": "P005", "ambiguity": "软弱与判断错误之间的关系本文未说明"}
   ],
   "examples_and_targets": [
    "同学考试作弊被举报、丢了学位证、举报者被全班孤立（提问者的处境，本文回应对象，Q001）",
    "“一群都认为这没有错的人”与“一群无耻的人”（作者对照的两种生活圈，P002、P006）",
    "“如入地狱”（对滑落后的处境的比喻，P007）"
   ],
   "conditions": [
    "如果找不到认同这没有错的人群，才需要在孤独与见义不为之间自行选择（P004）",
    "如果选了见义不为，其可原谅性来自软弱，而不是来自那种做法正确（P005）"
   ],
   "rhetoric_and_tone": "极短篇。开篇零铺垫直接判定“你没有错”，第二人称对提问者说话；以“如入地狱”四字独立成段收束；语气简峻、断言，无调侃与训诫式铺陈。",
   "unresolved_questions": [
    "作者未说明判断“没有错”所依据的标准，也未讨论作弊、举报与处分本身的是非（P001）。",
    "除“滑落到无耻的人中间”一说外，两种选择的后果本文未展开（P004、P006）。",
    "brief 与正文内容高度重合（同一答案的另一呈现），不作为额外证据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "你没有错。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "你只是需要找到一群都认为这没有错的人，去ta们中间生活。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "世界上的确存在这样的人群。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "这个就是你自己的选择问题了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "那么记住这是因为你软弱——这可以原谅——不是因为那样是“对的”“更明智的”。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "让你无可抗拒的滑落到一群无耻的人中间去，每天被无耻折磨。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "如入地狱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "校园生活", "人际处境"],
   "issue_candidates": ["举报作弊后的孤立", "是非判断与群体认同", "见义不为的归因"],
   "text_function_candidates": ["答疑", "断语式短评"],
   "object_candidates": ["提问者", "作弊同学", "全班同学"],
   "working_keywords": ["错", "孤立", "见义不为", "软弱", "如入地狱"]
  },
  "notes": "无图片节点。Q001 仅作提问者语境记录，未归入作者主张；brief 与正文重合，只作导航。"
 },
 "b5618967": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问“该不该追求有对象的人？”（Q001，属提问者语境，问题本身未表露立场）。作者不围绕“对方是否已有对象”作答，而是把问题改写为“可不可以追求人”，给出否定答案并重新界定“追求”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接给出答案：不可以。", "role": "conclusion"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "限定理由：否定不是出于“别人的对象”，而是任何人都不应该追求。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "定义“追求”为把他人意愿从A变为B的行为，并据此判其为利用人性弱点、损人利己。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "独立短句“——什么是‘追’。”，似小标题或图片说明，指向对“追”的界定。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "设问自答：只是“追”也不行。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P006"], "summary": "代拟“不追就没希望、孤苦一生”的顾虑，回应说“心里装着别人的自由”的人用不着追。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "追求已有对象的人是不可以的（答案是不可以）。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "否定的理由不是“别人的对象”，而是任何人都不应该追求。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“追求”只能用于“事业”“成就”，其宾语根本就不可以是人。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“追求”是一种用自己的行为把ta人的意愿从原本的A变为现在的B的行为。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "追求终究是利用人性的弱点扭转他人意愿以求得自己得逞，属损人利己，没有权利如此。", "evidence": ["E005"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "连“追”都不行，不只是不能追已有对象的人。", "evidence": ["E006"]},
    {"claim_id": "C007", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "作者代拟并反驳的顾虑：追都不追岂不完全没有希望、难道孤苦一生。", "evidence": ["E007"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "心里装着别人的自由到了这一步的人，从来用不着追。", "evidence": ["E008"]}
   ],
   "argument_steps": [
    "先给结论：不可以（P001）",
    "限定理由：不是“别人的对象”，而是任何人都不该追求（P002）",
    "定义“追求”：用自己的行为把ta人的意愿从原本的A变为现在的B（P003）",
    "由定义推出：追求是利用人性弱点、损人利己，无权如此（P003）",
    "以独立短句点题“什么是‘追’”（P004）",
    "设问自答：追也不行（P005）",
    "代拟并反驳“不追就没希望”的顾虑，给出替代状态：装着别人的自由的人用不着追（P006）"
   ],
   "concept_usage": [
    {"term": "追/追求", "meaning": "用自己的行为把他人的意愿从原本的A变为现在的B的行为，作者限定其只能用于“事业”“成就”，宾语不可以是人", "evidence": "P003", "ambiguity": "作者未说明“事业/成就”与“人”在宾语上的界线依据"},
    {"term": "别人的对象", "meaning": "提问者预设的禁止理由（对方已有伴侣），作者明确不以它为理由", "evidence": "P002", "ambiguity": "本文未说明；作者只说这不是原因"},
    {"term": "自由", "meaning": "用于描述“心里装着别人的自由”的人，因而无需追求", "evidence": "P006", "ambiguity": "“自由”的界定与判断标准本文未展开"}
   ],
   "examples_and_targets": [
    "提问者的问题“该不该追求有对象的人？”（回应对象，Q001，仅提问者语境）",
    "“事业”“成就”作为“追求”的正当宾语（作者举例，P003）",
    "“原本人家要半年才会愿意，因为你‘追’，变成三个月”（意愿被扭转的示例，作者举例，P003）",
    "“难道孤苦一生”作为被作者代拟并反驳的顾虑（作者自设的反驳对象，P006）",
    "图片 IMG001（src 见 structure，内容未核验，见 notes）"
   ],
   "conditions": [
    "否定范围被作者扩大：不限于“有对象的人”，而是任何人都不应该追求（P002）",
    "“损人利己”的判定以“追求＝改变他人意愿的行为”这一界定为前提（P003）",
    "“从来用不着追”只适用于“心里装着别人的自由到了这一步的人”（P006）"
   ],
   "rhetoric_and_tone": "短篇断语体。开篇零铺垫直接给否定答案；以设问自答推进（“追都不行吗？不行。”“岂不是完全没有希望了？”）；用“ta”作人称代词；以“不信你可以问问她们”作口语化收束。文末附有 1 个图片节点。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001），图片内容未核验，需人工/多模态复核后才能判定全文理解；故 status=needs_reread。",
    "P004“——什么是‘追’。”为独立短句，它与图片的位置关系及是否为图片说明，本文无法确定。",
    "作者未说明“追求”与一般交往、表达好感之间的界线（P003）。",
    "“心里装着别人的自由”的主体与具体含义未展开（P006）。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "答案是不可以。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "但这不是出于“别人的对象”这种原因，而是任何人都不应该追求。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "追求只能用于“事业”“成就”，追求的宾语根本就不可以是人。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "因为“追求”是一种用自己的行为把ta人的意愿从原本的A变为现在的B的行为。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P003", "quote": "追根到底，这手段终究是利用人性的弱点，扭转ta人的意愿，求得自己的得逞。你没有权利如此损人利己。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "追都不行吗？不行。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "那追都不追，岂不是完全没有希望了？难道孤苦一生？", "relation": "contradicts"},
    {"key": "E008", "paragraph_id": "P006", "quote": "心里装着别人的自由到了这一步的人，从来用不着追。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "恋爱伦理", "人际关系"],
   "issue_candidates": ["追求他人是否正当", "改变他人意愿与操纵", "自由与不追"],
   "text_function_candidates": ["答疑", "论辩", "断语式短评"],
   "object_candidates": ["提问者", "被追求者"],
   "working_keywords": ["追求", "事业", "成就", "损人利己", "人性的弱点", "自由"]
  },
  "notes": "本篇含 1 个图片节点（IMG001），图片内容未经核验，故 status=needs_reread、image_checked=False；已读部分为正文文本（P001—P006）。brief 与正文高度重合且被截断，只作导航。Q001 仅作提问者语境记录，未归入作者主张。"
 },
 "a496a21a": {
  "analysis": {
   "question_context": "提问者问“我为什么很反感别人吹牛?”（Q001，属提问者语境）。正文显示提问者另列有若干“条款”并把症状指向“这位老师”，但该问题正文未包含在本记录中；作者以“我与这位老师行为类似却得到不同感受”为切口作答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "交代关系线索：题主关注、点赞过作者，问题似专门为邀请作者而提；作者假设题主不讨厌自己并留出纠正余地。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "作者自陈也常“说很多很大的词”、讲宏大的话，也被人写帖评为“无知”“不懂装懂”“装逼”，且未给出业绩或头衔。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "反问：按题主列出的条款，作者症状更重却被邀请作答，为何感受不同。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "指出评论区里有人说中了。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "给出最大区别：那位老师占用别人的注意力，让人感到ta只为自己的利益，且是强行占用。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P007"], "summary": "作者处听者一开始就可选择听或不听，听了即含自愿，故减少负面评价几率。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P008", "P009"], "summary": "作者掌握一些说话原则，使话更容易被听者觉得是“为你说的”，故同样有问题处也不易招致负面评价。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P010"], "summary": "听者对作者模棱两可处会下意识往积极方向补全，并因此获得更多思考成果。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P011"], "summary": "对那位老师的不确切处，听者会向负面方向判定，得到其较糟糕的结论。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P012", "P013"], "summary": "追问是否看懂，并指出看懂后也能做看起来完全一样的事而有不同结果。", "role": "transition"},
    {"unit_id": "U011", "paragraph_refs": ["P014", "P015", "P016"], "summary": "归结为“爱”：爱可原理性遮盖许多罪，使能力同样不足者得到不同结果，这是最大的现实主义。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "questioner", "modality": "asserted", "statement": "据作者转述，题主列出了若干条款，并把“吹牛”的症状指向“这位老师”。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自陈其行为与“这位老师”类似，甚至“有过之而无不及”。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最大的区别在于那位老师占用了别人的注意力，却让人感到ta只是为了自己的利益，而并没有出于听者利益的考虑。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那位老师是强行占用注意力，想不听需自己努力离开；作者的表达一开始就可选择听或不听。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "因为听者一开始就有一份自愿在内，这减少了很多对作者负面评价的几率。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者掌握一些说话原则，使他的话更容易被听者觉得是“为你说的”，而不是“为了我说的”。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "听者对作者模棱两可的话会下意识乐意往积极方面补全，这种补全还会促进其获得更多思考成果。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "对那位老师的不确切处，听者会向负面方向判定，即使他实际并不那么糟糕也会得到较糟糕的结论。", "evidence": ["E009", "E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关键是爱；爱可以原理性的遮盖许多罪，让能力同样不足的人得到截然不同的好的结果。", "evidence": ["E011", "E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这一点无关理想和浪漫，这是最大的现实主义。", "evidence": ["E013"]}
   ],
   "argument_steps": [
    "交代关系线索：题主关注、点赞、似专门邀请（P001），并假设题主不讨厌自己（P002）",
    "自陈也说大词、也被评“无知/不懂装懂/装逼”，且无业绩头衔（P003）",
    "以“我症状更重却被邀请”反问差异来源（P004）",
    "指出评论区已有人说中（P005）",
    "区别一：占用注意力且被疑为自身利益 vs 可自由选择且被信为听者利益（P006、P007）",
    "区别二：说话原则使话被听成“为你说的”（P008、P009）",
    "机制说明：积极补全 vs 负面判定（P010、P011）",
    "追问是否看懂，指出同样的事可有不同结果（P012、P013）",
    "归因于“爱”，并断言这是最大的现实主义（P014—P016）"
   ],
   "concept_usage": [
    {"term": "吹牛", "meaning": "提问者反感的现象；作者以自己的“说很多很大的词”“讲一些……很宏大的话”与之对照，本文未给定义", "evidence": "P003", "ambiguity": "作者未界定“吹牛”与“说大词”的界线"},
    {"term": "占用注意力", "meaning": "描述那位老师的行为方式，特征是强行、需听者努力才能离开", "evidence": "P006", "ambiguity": "无"},
    {"term": "自愿", "meaning": "听者一开始可选择听或不听所内含的成分", "evidence": "P007", "ambiguity": "“自愿”是否足以改变评价，作者只说“减少了很多……几率”"},
    {"term": "爱", "meaning": "使能力同样不足的人得到截然不同的好结果的关键，可“原理性的遮盖许多罪”", "evidence": "P015", "ambiguity": "“原理性”与“遮盖”的机制本文未展开"}
   ],
   "examples_and_targets": [
    "题主关注作者、点赞三个答案、专门邀请（作者自陈的关系线索，P001）",
    "知乎上专门写帖子评价作者“无知”“不懂装懂”“装逼”（作者转述的外部评价，P003）",
    "“这位老师”（题主问题中的对象，作者用作对照，P004、P006、P011）",
    "“评论区里有人说中了”（作者引述评论区，P005；具体内容本文未给出）"
   ],
   "conditions": [
    "作者的前提假设：“先大胆假设你应该是不讨厌我的”，并声明猜错可纠正（P002）",
    "区别成立的条件是听者一开始能否选择听或不听（P006、P007）",
    "只断言“减少了很多”负面评价几率，未断言必然不被负面评价（P007）"
   ],
   "rhetoric_and_tone": "问答体，第二人称直接对题主说话。以自我暴露（也说大词、被评“装逼”、无头衔）构成对照；连续反问（“为什么你还会邀请我来回答这个问题？”“这里的关键看懂没有？”）；末段以“爱”“最大的现实主义”作断语式收束。",
   "unresolved_questions": [
    "提问者问题的正文（“各种条款”与“这位老师”的具体描述）未包含在本记录中，question 字段只有标题（Q001），相关主体无法核实，待原始平台页面核查。",
    "作者所称“说话的原则”的具体内容本文未说明（P008）。",
    "“爱可以原理性的遮盖许多罪”的机制本文未展开（P015）。",
    "P005“评论区里有人说中了”所指的具体评论内容本文未给出。",
    "brief 在本记录中被截断（止于“你会发现我也经常”），只作导航。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P004", "quote": "按照你列出的各种条款，我似乎都比这位老师症状严重得多。", "relation": "context"},
    {"key": "E002", "paragraph_id": "P004", "quote": "我跟这位老师的行为类似，甚至“有过之而无不及”，给你的感受却不一样，这是为什么？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "你会发现我也经常说很多很大的词", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "这位老师占用了别人的注意力，却让你感到ta只是为了ta自己的利益，而并没有出于你的利益的考虑。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "而且ta是强行占用的，你想要不听，需要你做出努力离开", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "而你只要是听了，一开始就有一份自愿在内。这就减少了很多对我负面评价的几率。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "使得我说的这些话更容易被你觉得是为你说的，而不是为了我说的。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "你会下意识的乐意去往积极的方面补全那些没说确切的地方。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "这时你却会因为这个原因，向负面的方向作判定。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "那么即使他实际并不是那样糟糕，你也会得到他比较糟糕的结论。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P014", "quote": "这个关键就是爱。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P015", "quote": "爱可以原理性的遮盖许多罪，让能力同样不足的人得到截然不同的好的结果。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P016", "quote": "这一点无关理想和浪漫，这是最大的现实主义。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "网络社区行为", "说服与传播"],
   "issue_candidates": ["反感吹牛的心理机制", "注意力占用与自愿", "自我利益与听者利益", "爱的遮盖作用"],
   "text_function_candidates": ["答疑", "自辩式说明", "经验总结"],
   "object_candidates": ["题主（提问者）", "这位老师", "知乎平台", "知乎评论区"],
   "working_keywords": ["吹牛", "占用注意力", "自愿", "说话的原则", "爱", "最大的现实主义"]
  },
  "notes": "无图片节点。题主提供的“条款”与“这位老师”的原始语境不在本记录内，凡涉题主描述处标注 attribution=questioner；P005 评论区“有人说中了”按作者引述处理，内容本文未给出。"
 },
 "e26a2168": {
  "analysis": {
   "question_context": "提问者问“情侣之间聊什么话题能增进感情？”（Q001，属提问者语境）。作者不接受该提问的预设，先判定提问者“年纪还小”、以为感情靠有趣引发和维持，再把增进感情归结为宽容，并在末尾给出自己所认可的话题清单。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "判定提问者年纪还小、以为感情靠有趣引发和维持，问话题是想借用别人的存货。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "正反判断：感情不靠海外奇谈等，也不靠志同道合、仰慕崇拜、互相贪恋，而是靠宽容、靠原谅。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "预言迟早出现重大分歧甚至针锋相对，届时兴趣相投、利益一致、美好回忆都微不足道。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "能救你们的唯有宽容的能力；感情追根到底是宽容的能源存量与能力的合并量。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "行动建议：好好过以积累美好回忆（宽容的燃料），好好聊、多拿他人他事做练习分析（宽容的能力和经验）。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015"], "summary": "建议分析仇恨来源与避免方式、分析更好的表达与反应，此即理解的能力本质；理解才能谅解，谅解才能宽容。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018"], "summary": "警告：最危险的构建感情方式是彼此附和共同的仇恨，今天支撑仇恨的理由明天会指向你。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "结论：真正珍重感情就去聊情有可原、事出有因、不忍、宽容、谅解和修复，这是唯一真正增进感情的话题。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者年纪还小，以为感情只靠有趣来引发和维持，问该话题是想在穷尽有趣之后借用别人的存货。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "感情不是靠海外奇谈、伟大构想、天才巧思、鲜明立场、熊熊斗志，而是靠宽容存在的。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真正可持续的感情不靠志同道合、仰慕崇拜、互相贪恋，而是靠宽容、靠原谅。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "迟早有一天你们会发现彼此之间有重大分歧，甚至算针锋相对。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "兴趣相投、利益一致、美好回忆在要害的、绕不开的分歧面前微不足道。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能救你们的唯有宽容的能力；感情追根到底只是宽容的能源存量和宽容的能力的合并量。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "彼此珍重的人要好好过以积累美好回忆（宽容的燃料），聊天要多拿他人他事做练习和分析（宽容的能力与经验）。", "evidence": ["E010", "E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "要去分析更好的表达和反应，可以很大几率避免和消解仇恨；这种分析就是理解的能力本质。", "evidence": ["E012", "E013"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能理解才能谅解，能谅解才能宽容。", "evidence": ["E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "最危险的构建感情方式是彼此附和共同的仇恨并自认志同道合，因为今天被判定充分而支撑仇恨的理由，明天会有另一个亦够充分并直指向你。", "evidence": ["E015", "E016"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正珍重感情就应去聊情有可原、事出有因、不忍、宽容、谅解和修复，这是唯一真正增进感情的话题。", "evidence": ["E017", "E018"]}
   ],
   "argument_steps": [
    "先判定提问者年纪小、以为感情靠有趣维持（P001）",
    "以否定排比给出正面主张：感情靠宽容存在（P002）",
    "继续排除志同道合、仰慕崇拜、互相贪恋，落到“宽容”“原谅”（P003—P005）",
    "预言分歧与针锋相对的必然出现，使兴趣/利益/回忆失重（P006—P008）",
    "把感情定义为宽容的能源存量与能力的合并量（P009、P010）",
    "给出积累宽容燃料与能力的具体做法（P011—P013）",
    "以“分析仇恨”训练理解力，串起理解—谅解—宽容（P014、P015）",
    "反面警告：共同仇恨式的情感构建最危险，仇恨理由终将指向自己（P016—P018）",
    "收束为唯一真正增进感情的话题清单（P019—P023）"
   ],
   "concept_usage": [
    {"term": "宽容", "meaning": "感情存在与可持续的根基，又被表述为“能源存量”和“能力”的合并量", "evidence": "P002", "ambiguity": "与无原则退让的界线本文未说明"},
    {"term": "原谅", "meaning": "与宽容并列的感情依赖项，未单独展开", "evidence": "P005", "ambiguity": "与“宽容”的差别本文未说明"},
    {"term": "宽容的燃料", "meaning": "指美好回忆的积累", "evidence": "P011", "ambiguity": "比喻，未给出量化或判定标准"},
    {"term": "理解", "meaning": "分析仇恨来源与更好表达方式的能力，被视为“理解的能力本质”，是谅解与宽容的前置环节", "evidence": "P014", "ambiguity": "“能力本质”所指未展开"},
    {"term": "仇恨", "meaning": "需被分析来源与避免方式的对象；以共同仇恨构建感情被作者判为最危险", "evidence": "P016", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "提问者的提问“情侣之间聊什么话题能增进感情？”（回应对象，Q001；作者判其想借别人的存货，P001）",
    "海外奇谈、伟大构想、天才巧思、鲜明立场、熊熊斗志（被否定的感情来源，P002）",
    "志同道合、仰慕崇拜、互相贪恋（被否定的可持续感情基础，P003）",
    "兴趣相投、利益一致、美好回忆（被判为在分歧面前微不足道，P008）",
    "彼此附和共同的仇恨、自认志同道合的同志（被判为最危险的构建方式，P016）"
   ],
   "conditions": [
    "作者以“你们年纪还小”为前提作判断（P001）",
    "以“迟早有一天”预期分歧与针锋相对会出现（P006、P007）",
    "分析仇恨的收益被限定为“很大几率”避免和消解仇恨（P014）",
    "话题清单以“真的珍重感情”为前提（P019）"
   ],
   "rhetoric_and_tone": "第二人称“你们”，过来人式的训导口吻。多用否定排比（“不是靠……也不是靠……更不是靠……”）；短句独立成段（“而是靠宽容。”“靠原谅。”“直指向你。”）；含“心里发酸、眼里有泪”一类抒情表达；以“唯一真正增进感情的话题”作强断言收束。",
   "unresolved_questions": [
    "作者未说明“宽容”与无原则退让的界线（P002、P009）。",
    "“宽容的能源存量和宽容的能力的合并量”为比喻式表述，未给出可操作界定（P010）。",
    "“理解的能力本质”一句的具体所指本文未展开（P014）。",
    "作者以“你们年纪还小”作判断，但作者身份/年龄及该判断的依据本文未给出（P001）。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "你们年纪还小，还以为感情只是靠有趣来引发和维持", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "其实感情不是靠什么海外奇谈、伟大构想、天才巧思、鲜明立场、熊熊斗志，而是靠宽容存在的。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "真正可持续的感情，不是靠志同道合、也不是靠仰慕崇拜、更不是靠互相贪恋。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "靠原谅。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "迟早有一天，你们会发现你们彼此之间有某件事有重大的分歧。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "迟早有一天，你们会发现你们何止是不同、甚至可以算针锋相对。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "微不足道到令人心里发酸、眼里有泪。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "能救你们的，唯有宽容的能力。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "所谓的感情，其实追根到底只是宽容的能源存量和宽容的能力的合并量。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "过的时候要好好过，积累美好回忆，这是在积累宽容的燃料。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "聊的时候要好好聊，要多拿他人他事多做练习和分析，这是在积累宽容的能力和经验。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "要去分析有什么更好的表达和反应，可以很大几率的避免和消解仇恨。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "而这就是理解的能力本质。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P015", "quote": "能理解，才能谅解，能谅解，才能宽容。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P016", "quote": "世界上最危险的构建感情的方式，就是彼此附和着共同的仇恨，以为因为有共同的仇恨对象、于是是志同道合的同志。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P018", "quote": "直指向你。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P019", "quote": "真的珍重感情，去聊情有可原，", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P023", "quote": "这其实是唯一真正增进感情的话题。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["情感/婚恋", "伦理学", "人际沟通"],
   "issue_candidates": ["增进感情的话题", "宽容作为感情基础", "共同仇恨与情感构建", "理解与谅解"],
   "text_function_candidates": ["答疑", "训导式建议", "经验总结"],
   "object_candidates": ["提问者（情侣双方）"],
   "working_keywords": ["宽容", "原谅", "理解", "仇恨", "宽容的燃料", "志同道合"]
  },
  "notes": "无图片节点。Q001 仅作提问者语境记录；P001 对提问者的判断按作者主张记录（attribution=author）。P018“直指向你。”承接 P017，语义需与上一段连读。"
 },
 "92aa0eef": {
  "analysis": {
   "question_context": "提问者（题主）称与女友还有40多天结婚，却失去结婚信心、想分手，问结婚成功率大不大（Q001，属提问者语境）。作者据题主自答中贴出的女方原话作答，指出两个问题（“必须白头到老”的心结与“不够成熟”），给出决策逻辑、行动建议，并对关系作积极面评价。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "交代语境：看过题主自答，肯定其贴出女方原话的诚意，并说明因问题典型而作答。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "第一个问题：必须放下“没有白头到老把握就不结”的心结；坚持它逻辑上只能“不结”；绝对把握不存在，有可能做成就已可做。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011"], "summary": "提出三条件，满足则一件事绝对可做、无所谓“错误”，得到的是收获或另一种收获，是“正确的错误”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012"], "summary": "行动建议：不要反复确认胜算，胜算他人与自己都给不了，此理适用于人生所有事。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "批判“庙算决胜论”：成因是忽略小后果失败与事后归因；逻辑上对但无实践指导意义；是庸俗/惰性归因法，结论政治正确却毫无意义；实为社会调适机制。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021"], "summary": "行动建议：摆脱该影响，把焦点从“如何确定概率”转到“失败时如何管理负面影响并亦有所得”。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P022"], "summary": "独立一句“由绝对真实所构成的世界是更美好还是更残酷？”，功能不明。", "role": "other"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "第二个问题：双方还不够成熟；迹象一是房子问题——未考虑第三方案、处理方式刚性。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032", "P033"], "summary": "迹象二是女方“无法接受”有点多；人生必须接受的东西远超这些，且多为天灾人祸。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035", "P036", "P037"], "summary": "提出“柔软度”：以策略灵活性与可接受范围大来打底（杂食动物之喻），有它才易达成共识、不易变成“两角债”。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P038", "P039", "P040"], "summary": "评估与建议：探索力与接受次好结果积累不足；观念一转就有“新手礼包”；但转变是为自己不是为对方。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046"], "summary": "积极方面：叙述未定性为人品/道德问题且双方都不舍，故是有希望的好事；要害是选择想办法还是选择定罪。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051"], "summary": "关系中真正的爱不是体贴照顾，而是万般痛苦而不愿定罪的忍耐，这已是真正意义上的爱。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P052", "P053"], "summary": "结论：解决不了的问题会有预料不到的助力带来变数，这也是作者说这些话的原因。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P054", "P055", "P056"], "summary": "限定“爱”的所指：良善之人对他人的仁爱，而非基于romance的超常优待；双方都有这份善良。", "role": "qualification"},
    {"unit_id": "U016", "paragraph_refs": ["P057"], "summary": "结尾孤立词“第一性”，含义不明。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "题主“结婚就预期一定要白头到老，没有把握就不愿意结”的想法必须放下。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要坚持该想法，逻辑上就只会有一个答案，就是不结。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何事情若要求只有绝对有把握成功才能做，答案都只能是不做；世界上根本没有“绝对把握”，因为世界永远不会受人控制。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做一件事只要有可能做成，就已经可做；满足“有逻辑上可见的成功概率、有无论成败都值得一做的理由、有足以保证‘成固欣然败亦喜’的安排”三条件，就绝对可做。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "满足三条件后决定做就无所谓“错误”，得到的只会是收获或另一种收获，即使未达首要目标也会成为“正确的错误”。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "要做的不是反复确认有多少“胜算”；胜算对方、网友、父母、马云都给不了，更不在自己手中。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人相信“庙算决胜论”是因为在思想上作了弊：后果小的失败被忽略，不能忽略的失败被归因为“错误的估计了成功率，轻视了失败概率”。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "该总结逻辑上对，但实践上没有真实指导意义，因为事前永远不可能正确估计失败概率；它是庸俗/惰性归因法，本质是拒绝面对真正的问题。", "evidence": ["E011", "E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“庙算”式结论是社会面对过于艰难问题时的调适机制（coping mechanism），不为解决问题而只是敷衍，却深刻影响了思维范式；题主应摆脱它。", "evidence": ["E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应把焦点从“如何确定概率”转到“如果失败，如何管理失败的负面影响以及如何亦有所得”的策略设计上；前者没有答案，只有后者有答案。", "evidence": ["E015", "E016"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "你们现在还不够成熟，其实还无法承受婚姻这种长期关系的要求（有两个迹象）。", "evidence": ["E017"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "房子问题上你们似乎没考虑过这两个方案之外的其他方案，在这类重大问题上的处理方式非常刚性，是不成熟的信号。", "evidence": ["E018", "E019"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "女方说的“无法接受”有点多；人生必须接受的东西远超这些，且多为不以人的意志为转移的天灾人祸。", "evidence": ["E020", "E021"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "柔软度要靠策略的灵活性（智慧）与对生活待遇的可接受范围大来打底；有柔软度才容易达成妥协和共识，关系才不易变成“两角债”。", "evidence": ["E022", "E023", "E024"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "看明白道理、观念一转就会有“新手礼包”，但做这个转变不是为了对方，而是为了自己，不要把债记在对方身上。", "evidence": ["E025", "E026"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "积极方面在于叙述中克制住未定性为人品问题、道德问题，且双方都表达不舍，所以这是有希望的好事；真正的要害是选择想办法还是选择定罪。", "evidence": ["E027", "E028", "E029"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关系中真正的爱不是万般体贴与殷勤照顾，而是万般痛苦而不愿定罪的忍耐；这种爱指良善之人对他人的仁爱，不是基于romance的超常优待。", "evidence": ["E030", "E031", "E032"]},
    {"claim_id": "C018", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者以“结婚的成功率大吗”提问，关注的是胜算判断（问题原文见 Q001；此处经作者 P012 的转述定位）。", "evidence": ["E009"]}
   ],
   "argument_steps": [
    "先肯定题主贴出女方原话的诚意，点明问题典型（P001）",
    "第一个问题：要求“白头到老的把握”的心结必须放下（P002）",
    "理由：坚持它只能得出“不结”；绝对把握不存在，有可能做成就已可做（P003—P005）",
    "给出三条件与“绝对可做”“正确的错误”（P006—P011）",
    "行动建议：不要反复确认胜算（P012）",
    "反驳“庙算决胜论”：思想作弊、无实践指导意义、拒绝面对真正问题、社会调适机制（P013—P018）",
    "要求摆脱该影响，把焦点转到失败后的策略设计（P019—P021）",
    "插入独立问句“由绝对真实所构成的世界是更美好还是更残酷？”（P022）",
    "第二个问题：不够成熟；迹象一为房子问题的刚性处理（P023—P030）",
    "迹象二为女方“无法接受”过多，而人生须接受者更多（P031—P033）",
    "提出并展开“柔软度”，关联到共识与“两角债”（P034—P037）",
    "评估积累不足，给出“新手礼包”与“为自己不为对方”的建议（P038—P040）",
    "转向积极方面，指出真正的要害是选择想办法还是定罪（P041—P046）",
    "把真正的爱界定为不愿定罪的忍耐（P047—P051）",
    "收束：问题会有预料不到的助力带来变数（P052、P053）",
    "补充界定“爱”为仁爱而非romance（P054—P056）"
   ],
   "concept_usage": [
    {"term": "绝对把握", "meaning": "被作者否定的一种决策前提：要求只有绝对有把握成功才做，世界永远不会受人控制", "evidence": "P004", "ambiguity": "无"},
    {"term": "庙算决胜论", "meaning": "指事前反复估算成功率再决定做不做的决策观，作者称其为思想作弊与社会调适机制的产物", "evidence": "P013", "ambiguity": "该术语是否为作者自造本文未说明"},
    {"term": "正确的错误", "meaning": "满足三条件去做而未达首要目标，因获得其他帮助而仍算正确的失败", "evidence": "P011", "ambiguity": "判定“正确的错误”的标准本文未细化"},
    {"term": "柔软度", "meaning": "以策略灵活性（智慧）与对生活待遇可接受范围大为基础的应变能力", "evidence": "P034", "ambiguity": "与“刚性”相对的边界本文未量化"},
    {"term": "两角债", "meaning": "描述关系中互相记账、循环计较谁欠谁的形态", "evidence": "P037", "ambiguity": "为比喻性说法"},
    {"term": "爱", "meaning": "本文特指良善之人对他人的仁爱、万般痛苦而不愿定罪的忍耐，明确排除基于romance的超常优待", "evidence": "P054", "ambiguity": "作者专门补充界定，说明该词在文中易被误解"},
    {"term": "第一性", "meaning": "文末孤立出现的词，无上下文，含义不明", "evidence": "P057", "ambiguity": "无法判定是标题、标签还是未完成的句子"}
   ],
   "examples_and_targets": [
    "题主自答中贴出的女方原话（作者用作依据，P001）",
    "看有把握的电影却遇停电没看成（被忽略计失败的小后果例子，作者举例，P013）",
    "“做错了题永远怪自己‘不够认真’”（用于类比庸俗/惰性归因法，P015）",
    "马云（用于列举“胜算”无人能给的修辞性排比，P012）",
    "跳槽、公司倒闭迁址、三年后住处（用于质疑对现地址执着的反问，P029、P030）",
    "一线市中心全款房产（作者据以判断经济条件不窘迫，P026）",
    "杂食动物 vs 只能吃箭竹叶子、必要时少吃或饿两天（柔软度的比喻，P035）",
    "“新手礼包”（描述观念转变后的即刻改善，P039）",
    "“神颜”“明日黄花”（对条件优越者的修辞性评价，P048）"
   ],
   "conditions": [
    "决策三条件：有逻辑上可见的成功概率、有无论成败都值得一做的理由、有足以保证“成固欣然败亦喜”的安排（P006—P009）",
    "只要有可能做成即已可做（P005）；只要坚持“必须有把握”就只能不结（P003）",
    "作者关于成功的概率判断的前提是“事前无法正确估计失败概率”（P014）",
    "柔软度的收益以“自觉认同要往这方面努力”为条件（P039）",
    "对“爱”的理解被限定为仁爱而非romance，以防读者误解（P054）",
    "题主的处境限定：还有40多天结婚、存在房子方案分歧（Q001、P025、P026）"
   ],
   "rhetoric_and_tone": "长篇分点答疑。“第一个问题/第二个问题”结构；大量反问与直问（“你们想过吗？”“为什么？”）；比喻密集（杂食动物、箭竹叶子、新手礼包、两角债）；第二人称直呼“你/你们”；列举“对方给不了、网友给不了、父母给不了、马云也给不了”带调侃；末尾以孤立词“第一性”突兀收尾。",
   "unresolved_questions": [
    "P012“这甚至不是结婚这一件事的问题，而是你人生中的所有事都不能适用于这个决策逻辑。”中“不能适用于”与上下文语义关系不明，疑为笔误，需回原文/平台版本核对，不作改写。",
    "P022“由绝对真实所构成的世界是更美好还是更残酷？”独立成段，且被标为 lexical 未覆盖片段，其功能（小标题/旁白/待续句）无法确定。",
    "P057“第一性”为文末孤立词，含义与功能不明。",
    "题主自答的补充内容与女方原话不在本记录中（P001 提到），无法核对其具体内容。",
    "brief 在本记录中被截断（止于“因为只”），只作导航。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "这个想法你必须放下", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "因为只要你坚持这个想法，逻辑上就只会有一个答案，就是不结。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "任何事情，如果要求只有绝对有把握成功的前提下才能做，答案都一定只能是不做。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "世界上根本没有所谓“绝对把握”这回事，因为世界永远不会受人控制。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "做一件事，是只要这件事有可能做成，就已经可做。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "满足这三个条件，一件事情就绝对可做。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P010", "quote": "满足了这三个条件，决定做这件事就无所谓“错误”可言，你得到的只会是一种收获或另一种收获。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P011", "quote": "成为一个正确的错误。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "反复确认会有多少“胜算”", "relation": "context"},
    {"key": "E010", "paragraph_id": "P013", "quote": "人之所以会相信“庙算决胜论”，是因为在思想上作了弊", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P014", "quote": "但是在实践上没有真实的指导意义，因为你永远不可能做到在事前正确的估计失败概率。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P016", "quote": "将原因归结到人无法改进的问题上，本质上是在拒绝面对真正的问题。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P018", "quote": "这只是一个社会在面对过于艰难的问题时的调适机制（coping mechanism）。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P019", "quote": "你要摆脱这样的影响，因为它本来就不是为个人生活幸福设计的。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P020", "quote": "不要把问题的焦点放在“如何确定概率”上，而应该放在“如果失败，则如何管理失败的负面影响，以及如何亦有所得”的策略设计上。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "前者没有答案，只有后者有答案。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P023", "quote": "第二个问题，就是你们现在还不够成熟，其实还无法承受婚姻这种长期关系的要求。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P026", "quote": "你们似乎没有怎么考虑过除了这两个方案之外的其他方案。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P028", "quote": "你们在这类重大问题上的处理方式非常刚性，这是一个不成熟的信号。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P031", "quote": "第二个，是女方说的“无法接受”有点多。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P032", "quote": "真正值得忧虑的，是人生中必须要接受的东西远超过你们目前声言“无法接受”的这些事情。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P034", "quote": "这个柔软度首先要靠策略的灵活性也就是智慧来打底，然后要靠对生活待遇的可接受范围大来打底。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P036", "quote": "有这种柔软度，人才容易达成妥协和共识", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P037", "quote": "这关系也就不容易变成“两角债”关系", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P039", "quote": "只要你们看明白了这个道理，观念一转，就会有新手礼包。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P040", "quote": "做这个转变不是为了对方，而本身就是为了自己，不要把债记在对方身上。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P042", "quote": "而没有定性为人品问题、道德问题。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P043", "quote": "而且双方都表达了不舍之意。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P046", "quote": "真正的要害，在于双方在这个节点上是选择想办法，还是选择定罪。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P047", "quote": "你们关系中真正的爱的成分、既不是相处时万般体贴，也不是什么殷勤照顾", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P049", "quote": "真正有分量的，其实是这一点万般痛苦而不愿定罪的忍耐。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P054", "quote": "我说的这种爱，指的是良善之人对他人的仁爱，不是指那种基于romance的对特定人的超常优待。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋决策", "伦理学", "风险评估/决策论", "社会心理"],
   "issue_candidates": ["婚姻成功率与绝对把握", "庙算决胜论批判", "柔性与妥协能力", "两角债关系", "仁爱与romance之辨"],
   "text_function_candidates": ["答疑", "论辩", "经验总结", "劝导"],
   "object_candidates": ["提问者（题主）", "题主女友", "网友", "父母", "马云"],
   "working_keywords": ["绝对把握", "庙算决胜论", "正确的错误", "柔软度", "两角债", "仁爱", "romance", "第一性"]
  },
  "notes": "无图片节点。Q001 仅作提问者语境；C018 为提问者侧问题，经作者 P012 转述定位，未归给作者。P022、P057 被结构脚本标为 lexical 未覆盖片段，属正文内容，已按原文保留定位。P012 中“不能适用于”疑为笔误，只记录不修改。"
 },
 "1a3e0866": {
  "analysis": {
   "question_context": "提问者问“温柔的人不适合做老师吗?”（Q001，属提问者语境）。作者先以自设的连环设问翻转“温柔/严厉”的对立，再把严厉的条件归到受者内心的良知认同上，最后正面回答：温柔是教师的天命。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "以自设问题开场：温柔与严厉是否反义词、温柔者是否必不严厉、有无“严厉的温柔”。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005"], "summary": "提出判断：严厉必须是温柔的，否则不成其为严厉，只是暴虐。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "解释严厉生效的条件：受者内心站在你这一边、其神性与你共鸣，且你已降低力度、婉转方式。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "你是受者良知的代言人；真正可畏的不是棍棒或鄙夷，而是内心良知的定罪。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012"], "summary": "教师的任务是为无语的良知代言、是促使双方修合的翻译，要做到信、达、雅：信与达是严厉，雅是温柔。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "效果：良知因被代为转达而安定，学生的无名焦虑才能缓解，学生会知道你的温柔所在。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "界定严厉的限度：遵循最低必要原则、是最轻程度和最柔选择；对不必要伤害的克制就是温柔与力量根源。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P017"], "summary": "断言这种话能“洞石穿金，移山倒海，破心中贼”。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P018", "P019", "P020"], "summary": "回答问题：温柔是教师的天命；不温柔就没有严厉的资格与权柄。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P021", "P022"], "summary": "以“唯文心，可以雕龙”与英文句“Another poetic irony.”收尾。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "严厉必须是温柔的，否则就不成其为严厉，而仅仅是暴虐。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "严厉之所以成为严厉、能令受者诚惶诚恐，是因为受者自己内心站在你这一边、其神性与你共鸣。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教师只是受者自己良知的代言人；真正可畏的不是家长的棍棒或社会的鄙夷，而是内心良知的定罪。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教师的任务是为这无语的良知代言，是意图让双方修合的翻译；要做到信、达和雅，信与达是严厉，雅是温柔。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "良知听见自己的意思已被转达便会安定下来，学生的无名焦虑才能缓解，并会知道你的温柔所在。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "严厉遵循最低必要原则、是不得不为的最轻程度和最柔选择；对任何一分不必要伤害的克制就是温柔，是使人与人的良知修合的力量根源。", "evidence": ["E009", "E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "温柔是教师的天命；不温柔，就没有严厉的资格，也没有严厉的权柄。", "evidence": ["E011", "E012"]}
   ],
   "argument_steps": [
    "以连环设问打开“温柔/严厉”的对照（P001—P004）",
    "给出判断：严厉必须温柔，否则只是暴虐（P005）",
    "说明严厉生效的条件在受者内心（内在神性与良知共鸣）（P006—P008）",
    "转到“良知”：真正可畏的是内心良知的定罪（P009）",
    "以“代言良知／翻译”定位教师，并以信达雅对应严厉与温柔（P010—P012）",
    "推演效果：良知安定则学生焦虑缓解（P013、P014）",
    "界定严厉的最低必要限度，并把该克制等同于温柔（P015、P016）",
    "断言其效力（洞石穿金、破心中贼）（P017）",
    "回答问题：温柔是教师的天命，不温柔则无严厉的资格与权柄（P018—P020）",
    "以“唯文心，可以雕龙”与英文句收束（P021、P022）"
   ],
   "concept_usage": [
    {"term": "温柔", "meaning": "对任何一分不必要伤害的克制；与严厉不是反义词，而是严厉成立的条件，也是教师的天命", "evidence": "P016", "ambiguity": "未给出可操作的判定标准"},
    {"term": "严厉", "meaning": "以受者内心认同其正确为前提的强力表达；须遵循最低必要原则", "evidence": "P005", "ambiguity": "严厉的具体做法本文未举例"},
    {"term": "暴虐", "meaning": "严厉缺乏温柔（受者内心不站在你这一边）时的形态", "evidence": "P005", "ambiguity": "无"},
    {"term": "良知/神性", "meaning": "教师代为发言的对象，也是严厉真正的畏惧来源；文中用“神性”“良知”交替指称", "evidence": "P009", "ambiguity": "“神性”与“良知”的关系本文未界定"},
    {"term": "信、达和雅", "meaning": "被作者挪用为代言/翻译的准则，其中信与达对应严厉，雅对应温柔", "evidence": "P012", "ambiguity": "借用翻译学标准的依据本文未说明"}
   ],
   "examples_and_targets": [
    "提问者的提问“温柔的人不适合做老师吗?”（回应对象，Q001）",
    "“家长的棍棒”“社会的鄙夷”与被对比的“内心良知的定罪”（作者举例，P009）",
    "“受者诚惶诚恐、战战兢兢、汗不敢出”（对严厉效果的描述，P006）",
    "“洞石穿金，移山倒海，破心中贼”（修辞性夸张，P017）",
    "“唯文心，可以雕龙”（化用《文心雕龙》的收束语，P021）",
    "“Another poetic irony.”（英文收尾句，功能不明，P022）"
   ],
   "conditions": [
    "严厉成立的条件是受者自己内心站在教师这一边（P006、P007）",
    "严厉须遵循最低必要原则、以最轻程度与最柔方式进行（P015）",
    "温柔作为天命的前提性问题由“适合当教师吗”改写为“温柔的人适合当教师吗？”，题面与文内问法方向不同（Q001、P018）"
   ],
   "rhetoric_and_tone": "布道/训诫式语气。以自设连环问句开场，随后逐层论断；第二人称“你”直接对教师说话；用“ta”“祂”作人称代词；“诚惶诚恐、战战兢兢、汗不敢出”等文言化表达；“唯文心，可以雕龙”化用典故；以英文句“Another poetic irony.”突兀收尾。",
   "unresolved_questions": [
    "P022“Another poetic irony.”的具体所指与功能本文未说明，是否为对全篇的自我评注不明。",
    "“神性”（P007）与“良知”（P009、P010、P013）在文中交替出现，二者关系未界定。",
    "“信、达和雅”被直接对应为严厉与温柔，其依据本文未展开（P011、P012）。",
    "题面为“温柔的人不适合做老师吗?”，文内改写为“温柔的人适合当教师吗？”（P018），问法方向与题面不同，是否同一问题需回平台核对。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P005", "quote": "其实，严厉必须是温柔的，否则就不成其为严厉，而仅仅是暴虐而已罢了。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P006", "quote": "严厉之所以能成其为严厉，能令受者诚惶诚恐、战战兢兢、汗不敢出，是因为受者自己内心站在你这一边。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P007", "quote": "是受者自己内心的神性与你共鸣", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P009", "quote": "你其实只是ta自己良知的代言人。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "真正可畏的，不是家长的棍棒，也不是社会的鄙夷，而是内心良知的定罪。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P010", "quote": "你的任务是为这无语的良知代言，你其实是一个意图让双方修合的翻译。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P012", "quote": "信与达里是那份严厉，雅就是这份温柔。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P013", "quote": "祂安定了下来，则学生那份不可解的无名焦虑才能缓解。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P015", "quote": "你的确是严厉的，但你的严厉在小心翼翼、深思熟虑的遵循最低必要原则，已是不得不为的最轻程度和最柔选择。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P016", "quote": "这份小心翼翼、深思熟虑的、对任何一分不必要的伤害的克制，就是温柔", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P019", "quote": "温柔是教师的天命。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P020", "quote": "不温柔，没有严厉的资格，也没有严厉的权柄。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育学", "伦理学", "师道/修身"],
   "issue_candidates": ["温柔与严厉是否对立", "严厉的正当条件", "良知与教育", "教师的天命"],
   "text_function_candidates": ["答疑", "论说", "训诫式散文"],
   "object_candidates": ["提问者", "教师", "学生/受者"],
   "working_keywords": ["温柔", "严厉", "暴虐", "良知", "神性", "信达雅", "最低必要原则"]
  },
  "notes": "无图片节点。Q001 仅作提问者语境。末尾英文句与“第一性”式的孤立词不同，P022 为完整英文句但功能不明，已入未决问题。结构脚本记 lexical 段落 25 个而正文有效段落 22 个，差异为空白段落，非正文缺失。"
 },
 "250b12b2": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问“是否有很多人歧视奢侈品？”（Q001，属提问者语境）。作者把问题转为对“仇视奢侈品消费”这一心态的批评，主张问题不在奢侈品本身而在“进口”，并给出自己认可的两种消费心态与“正确的鉴赏观”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "指认一种心态：把富人的奢侈品消费视为罪恶，并把奢侈品税视为对该观点的背书，理解为“艰苦朴素”的一部分。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "判定该心态大错：征收奢侈品税的关键原因是现阶段奢侈品多为进口，而非“奢侈品有罪”。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "假设奢侈品为国内产品，论证其结果是极低边际成本、高效率、完全自愿的财富转移，并具极高税收效率。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "追问实业机构拿到钱后的用途（研发下一代领先技术），并举德瑞精密制造、意法设计品牌、瑞士机床为例。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "以 Bumotec 为图证：logo 与宣传手册显示珠宝钟表加工、涡轮叶片、超级跑车零件（依赖图片，未核验）。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020"], "summary": "指出直接受益者是工匠、工程师、技师，有机会摆脱996拼体力劳动；对比富人交出的资金，问这安排有何不好。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023"], "summary": "区分问题所在：问题在“进口”而不在“奢侈品”消费本身；本国奢侈品交易对本国实业是美好安排，甚至是中国制造业由大而强的必由之路。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026"], "summary": "以反问推进：中国若成第一制造业强国，难道不生产被别国以超额溢价追求的产品？难道要勒令它不准往贵里卖？", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "第一条心态：不要基于炫耀或“证明实力”购买奢侈品；此类“策略”只对愚人有用，在明白人眼里是扣分信号，并带强烈贬斥与后果预测。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P034", "P035"], "summary": "第二条心态：买真正意义上的奢侈品须抱着“选择一个够资格的对象接受我这笔财富”的心态，此心态不败坏家风与价值观。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040"], "summary": "界定“真正意义上的奢侈品”：无特别实用价值、并非绝对必要的“多余之物”，内嵌引人沉迷的毒性，须被转性/救赎才可能安全。", "role": "definition"},
    {"unit_id": "U012", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "提出“救赎”：奢侈品的慈善性质——奖励极致技艺与卓越思考，不是“消费”而是捐赠，是“见义勇为”。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053"], "summary": "界定“正确的鉴赏观”＝你要懂（不只懂官网八卦/品牌故事，还要懂背后的心思与可贵之处）；未经经历者没有无害参与买卖的资格。", "role": "definition"},
    {"unit_id": "U014", "paragraph_refs": ["P054", "P055", "P056", "P057"], "summary": "界定“有所建树”＝传世之作（有人肯接且有人接了）；在此之前没有充分实用理由的购买都应避免，且与价格无关。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者观察到的国内传统心态是仇视奢侈品消费，把富人的奢侈品消费视为不可容忍的奢侈浪费与罪恶，并把奢侈品税视为对该观点的背书。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "把上述心态理解为“保持艰苦朴素的优良传统”是大错而特错；中国征收奢侈品税的关键原因根本不是“奢侈品有罪”，而是现阶段奢侈品多为进口产品。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若假设奢侈品都是国内产品，则富人购买奢侈品的结果是以极少的边际成本实现极高效率、完全自愿的财富转移，从财富集中处转向技艺精湛、经营卓越的实业部门。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实业机构会把资金用于研发下一代领先全球的技术、占住下一个世代的顶尖；德国瑞士的精密制造优势、意大利的设计传统和法国的文化品牌即由此而来。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "瑞士的精密机床是为做出更精致的机芯而创造出来的，其技术与技艺并不只用于手表（以 Bumotec 为例证，依赖未核验图片）。", "evidence": ["E009", "E010"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "直接受益的工匠、工程师、技师因这项交易有很大机会摆脱996的拼体力劳动方式，这甚至是最好的途径之一。", "evidence": ["E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题是现在在进口奢侈品；问题在“进口”而不在“奢侈品”消费本身。", "evidence": ["E012", "E013"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本国消费中发生的本国奢侈品交易对本国实业部门是非常美好的安排，甚至是中国制造业由大而强的必由之路。", "evidence": ["E014"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "反问：中国若走向世界第一制造业强国，难道不会生产出被其他国家以超额溢价追求的产品？难道要勒令它“不准往贵里卖”？", "evidence": ["E015", "E016"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第一条：不要基于炫耀或“证明实力”的目的购买奢侈品，因为这对购买者自己是极其深刻的损害。", "evidence": ["E017"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“通过展现自己很有钱然后指望勾出别人的钱来”的策略只对脑子还不清楚、未摆脱拜物冲动的愚人有用；在真正握有生产力优势的明白人眼里只是扣分信号。", "evidence": ["E018"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若已有第一桶金仍用这套手段，只能说明没这个命：八成机会五年内赌光或乱投亏光，九成九的机会子女不成器，“富”半代而已。", "evidence": ["E019"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二条：买真正意义上的奢侈品必须抱着“选择一个够资格的对象接受我这笔财富”的心态；只有这种心态不会败坏家风、破坏子孙品格、导致欲望膨胀等。", "evidence": ["E020", "E021"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正意义上的奢侈品没有特别的实用价值（显卡、深潜器、防寒服、卫星电话再贵也不算；空军一号值53亿美金也不是），它是并非绝对必要的“多余之物”。", "evidence": ["E022", "E023", "E024"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "奢侈品天生带“超出必要的享受”属性、逻辑内嵌“引人沉迷享受”的毒性，必须被转性、找到救赎才有可能是安全的。", "evidence": ["E025", "E026"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最大的救赎是奢侈品天生带有的慈善性质：在正确的鉴赏观界定下，它是奖励极致技艺和卓越思考的最贴切形式；这不是“消费”而是捐赠，是“见义勇为”。", "evidence": ["E027", "E028", "E029"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正确的鉴赏观就是“你要懂”：不只懂官网八卦、品牌故事，还要懂背后的心思与可贵之处；没有相关经历的人不会懂。", "evidence": ["E030", "E031"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在历尽千般、有所建树、八风不动心之前，人根本没有无害地参与奢侈品买卖的资格；“有所建树”指传世之作（有人肯接且有人接了）；在此之前没有充分实用理由的购买都应避免，且与价格无关。", "evidence": ["E032", "E033", "E034"]}
   ],
   "argument_steps": [
    "指认被批评的心态：仇视奢侈品消费、视之为罪恶、以奢侈品税为背书（P001—P003）",
    "判定其错误并给出真实原因：税因“多为进口”而非“有罪”（P004、P005）",
    "作反事实假设：若为国内产品，则奢侈品消费是高效率的自愿财富转移（P006—P008）",
    "追问资金去向，举德瑞意法的制造与设计传统（P009、P010）",
    "以 Bumotec 的 logo 与宣传手册作图像例证（P011—P018，图片未核验）",
    "指出受益者为工匠、工程师、技师，可摆脱996（P019、P020）",
    "收紧结论：问题在“进口”而非奢侈品消费本身；本国交易是必由之路（P021—P023）",
    "以反问排除“第一强国不该卖贵”的立场（P024—P026）",
    "转为个人建议第一条：勿以炫耀/证明实力为目的购买（P027—P033）",
    "建议第二条：以“选择够资格的对象接受财富”的心态购买（P034、P035）",
    "界定真正意义上的奢侈品及其毒性，提出“转性/救赎”（P036—P040）",
    "把救赎落在“慈善性质”与“见义勇为”上（P041—P047）",
    "界定“正确的鉴赏观”＝你要懂，并给出资格门槛（P048—P056）",
    "收束：与价格无关（P057）"
   ],
   "concept_usage": [
    {"term": "奢侈品", "meaning": "并非绝对必要的“多余之物”，无特别实用价值，作者明确把高价实用品（显卡、深潜器、防寒服、卫星电话、空军一号）排除在外", "evidence": "P036", "ambiguity": "“多余之物”与实用品的界线靠举例划分，未给统一标准"},
    {"term": "进口", "meaning": "被作者指为真正问题的环节：现阶段国内消费的奢侈品多为进口产品，故税收与产业收益外流", "evidence": "P022", "ambiguity": "作者未给出税制或贸易数据依据，属待外部核查的事实性论断"},
    {"term": "正确的鉴赏观", "meaning": "“你要懂”：懂背后的心思与可贵之处，而非只懂官网八卦、品牌故事", "evidence": "P050", "ambiguity": "“懂”的程度与判定标准本文未量化"},
    {"term": "有所建树", "meaning": "创造了一番事业且有人肯接、有人接了，即传世之作", "evidence": "P055", "ambiguity": "“传世”的时间尺度本文未说明"},
    {"term": "救赎/转性", "meaning": "指把奢侈品的“毒性”转为慈善性质，即奖励极致技艺与卓越思考", "evidence": "P041", "ambiguity": "为作者自设的框架词，未系统界定"}
   ],
   "examples_and_targets": [
    "珠宝、游艇、皮鞋（富人消费的具体例子，P002）",
    "二十克媒介物、一张皮革、一张纸加一点颜料（描述交易标的，P008）",
    "德国瑞士的精密制造优势、意大利的设计传统、法国的文化品牌（作者例证，P009）",
    "瑞士的精密机床与机芯（作者例证，P010）",
    "Bumotec 及其 logo、宣传手册（作者图证，P011—P018；6 张图片未核验）",
    "996（网络语，描述拼体力劳动方式，P019）",
    "超高速最新显卡、万米深潜器、超科技防寒服、卫星电话（被排除在奢侈品之外的实用品，P036）",
    "空军一号值53亿美金（被排除在奢侈品之外的例子，P037）",
    "“红粉遗佳人，宝剑赠英雄”（修辞性引语，P047）",
    "“官网八卦”“品牌故事”（被贬为不足的鉴赏知识，P051）"
   ],
   "conditions": [
    "作者论断以“现阶段奢侈品多为进口产品”为前提（P005）",
    "关键论证以反事实假设“假设奢侈品都是来自中国国内的产品”为条件（P006）",
    "“健康的消费心态”以“在正确的鉴赏观的界定下”为条件（P041）",
    "购买资格以“历尽千般、有所建树、八风不动心”为前提（P053）",
    "关于炫富策略的后果预测带概率限定（“八成机会”“九成九的机会”，P033）"
   ],
   "rhetoric_and_tone": "论战/训诫混合语气。开篇点出“非常奇妙的传统心态”并直接判“大错而特错”；连串反问（“够直白了吗？”“这够典型了吗？”“想穷一辈子？”）；对炫富者使用强烈贬斥语（“眼瞎”“精神上的残疾”“成事不足败事有余”“你爹妈不爱你”“家教不严”）；以图证“一锤定音”；引用“红粉遗佳人，宝剑赠英雄”；结尾“这跟价格没有关系”作硬收束。",
   "unresolved_questions": [
    "本篇含 6 个图片节点（IMG001—IMG006：Bumotec logo 与宣传手册页），图片内容未核验，需图像核验后才能判定全文；故 status=needs_reread。P012—P018 的“够直白了吗？”“这够典型了吗？”等论断直接依赖图像内容，目前只能确认文字表述。",
    "关于中国奢侈品税的征收原因与“现阶段奢侈品多为进口产品”属事实性论断，本文未给法规或数据依据，待外部核查（P005）。",
    "“Bumotec”的企业背景、产品线与图证内容的对应关系无法从文本确证，待外部核查（P011—P018）。",
    "P030—P033 的攻击性指称中“你”是否有具体所指（是否指向某类读者或特定对象）不明确。",
    "“国内”具体所指范围（中国大陆或更广）本文未明说（P001）。",
    "brief 在本记录中被截断（止于“把这理解为”之后的段落），只作导航。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "我发现国内有一种非常奇妙的传统心态——仇视奢侈品消费。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "是不可容忍的奢侈浪费，是一种罪恶", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "这大错而特错。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "中国征收奢侈品税的关键原因根本不是“奢侈品有罪”，而是因为现阶段奢侈品多为进口产品。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "假设奢侈品都是来自中国国内的产品", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "是用极少的边际成本获得了极高效率的、基于完全自愿的财富转移", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "它们要去研发下一代领先全球的技术，去占住下一个世代的顶尖。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "你以为德国瑞士的精密制造优势是哪里来的？意大利的设计传统和法国的文化品牌是怎么来的？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "瑞士的精密机床是为做出更精致的机芯而创造出来的", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P016", "quote": "反手就是涡轮叶片。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P019", "quote": "因为这项肥美的交易，有很大机会摆脱996的拼体力劳动方式", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P021", "quote": "真正的问题是ta们现在是在进口奢侈品。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P022", "quote": "问题在“进口”，而不在“奢侈品”消费本身。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "甚至是中国制造业由大而强的必由之路。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "难道中国有一天走向了世界第一制造业强国，竟然不会生产出大批被其他国家视为值得用超额溢价去追求那一点极致性能和底蕴的产品？", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P025", "quote": "难道谁世界第一了，要勒令它“不准往贵里卖”？", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P028", "quote": "不要基于炫耀或者“证明实力”的目的购买奢侈品，因为这对你自己是一种极其深刻的损害。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P029", "quote": "在明白人——也就是真正握有生产力优势，能扎实的改变你的命运的人——眼里，只会是扣分信号。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P033", "quote": "八成机会五年内你不是赌光就是乱投亏光", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P034", "quote": "必须要抱着“这是在选择一个够资格的对象接受我这笔财富”的心态。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P035", "quote": "只有这种心态不会败坏家风、破坏子孙的品格", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P036", "quote": "什么是真正意义上的奢侈品？就是它并没有特别的实用价值", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P037", "quote": "空军一号值53亿美金，但它并不是奢侈品。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P038", "quote": "奢侈品是一种并非绝对必要的“多余之物”。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P039", "quote": "于是逻辑内嵌了“引人沉迷享受”的毒性。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P040", "quote": "它必须被转性，必须找到救赎才有可能是安全的。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P041", "quote": "在正确的鉴赏观的界定下，它是奖励极致技艺和卓越思考的最贴切的形式。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P046", "quote": "这不是“消费”，而是基于惺惺相惜、心意相通的捐赠。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P047", "quote": "这叫见义勇为。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P050", "quote": "就是你要懂。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P052", "quote": "你自己没有人海沉浮、大起大落，没胼手胝足、流汗流泪乃至流血的拼杀过，你是不会懂的。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P053", "quote": "你根本没有无害的参与奢侈品买卖的资格。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P055", "quote": "你创造了一番事业，有人肯接而且有人接了，这叫做有所建树。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P057", "quote": "这跟价格没有关系。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["经济学/消费", "税收政策", "伦理学", "制造业与产业"],
   "issue_candidates": ["奢侈品消费是否罪恶", "奢侈品税与进口", "财富转移与实业投入", "炫富的负外部性", "鉴赏观与购买资格"],
   "text_function_candidates": ["答疑", "论辩", "批评", "经验总结"],
   "object_candidates": ["中国", "德国", "瑞士", "意大利", "法国", "富裕阶层", "工匠/工程师/技师", "Bumotec"],
   "working_keywords": ["奢侈品", "进口", "奢侈品税", "财富转移", "正确的鉴赏观", "见义勇为", "有所建树"]
  },
  "notes": "本篇含 6 个图片节点（IMG001—IMG006，Bumotec logo 与宣传手册页），图片内容未经核验，故 status=needs_reread、image_checked=False；已读部分为正文文本（P001—P057）。涉及税制与产业的事实性论断（P005、P009、P010）均按作者说法记录，未作外部采信，待外部核查。Q001 仅作提问者语境。"
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
