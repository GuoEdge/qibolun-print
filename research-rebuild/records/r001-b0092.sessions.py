# -*- coding: utf-8 -*-
"""批次 r001-b0092 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0092.sessions.py            # 写 out/r001-b0092.out.jsonl
  python3 records/r001-b0092.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0092"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0092.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "86c208a0": {
  "analysis": {
   "question_context": "提问者问“怎样成为一个有魄力的人？”，默认“魄力”是一种可学习、可获取的个人能力。作者不回答“怎么学”，而是先拆解被公众称为“魄力”的典型场景（大老板力排众议推出颠覆性策略、事成后被赞一代枭雄），判定其归因错误，并把“魄力”改述为位置与数据条件造成的客观结果。提问者的立场（魄力可学）属于提问者，不是作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "复述“魄力”的流行剧本：老板一意孤行、团队将信将疑照做、事后成功被赞枭雄（若看错则不会进入样本）。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "点出该剧本被归结为“超人的智慧与勇气”，作者判定两方面都错。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008"], "summary": "作者解释：领袖因独特思考角色与最高保密级别而拥有更高数据起点，结论自然与只掌握部分数据者不同。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "数据不能全面公开，且环境瞬息万变，取得全员一致信服既不现实也无时间。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011"], "summary": "领导者处境上只能是孤家寡人，其他人只能信托、下好离手、愿赌服输。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "由不同意属理所当然，推出事情须靠力排众议与下属职业精神，故成功组织讲求服从精神。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015"], "summary": "结论：此事与勇气智慧关系不大，是组织实践常态；驱动者是无法寻求理解的恐惧与危机。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018"], "summary": "重新定义勇气（对不行动的怯懦、正确的怯懦），并否定为显示“狠气”而做的鲁莽。", "role": "definition"},
    {"unit_id": "U009", "paragraph_refs": ["P019", "P020"], "summary": "魄力是提前看到危险并坚持推进的客观显现；归因于数据而非“特殊的英明”是“有魄力/不知死活”的分界线。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P021"], "summary": "到该位置自然“有魄力”，它不是能力而是“职业危害”，不用“学”。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P022", "P023", "P024"], "summary": "转折收束：真正的问题是如何走到领袖位置、下属为何能执行无法核实的决策，话题由此通向 Faith。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "把力排众议式的“魄力”归结为“超人的智慧与勇气”是错的，两个方面都错。", "evidence": ["E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "领袖能更早看到更大图景，不见得因为伟大睿智，而是因为其拥有最高保密级别、是企业全部最高机密数据的唯一知情者。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因数据起点更高，其结论必然不为只掌握部分数据者所同意；而数据不能全面公开，取得全员一致信服常常根本不现实。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使不顾敏感信息外泄，组织所处环境瞬息万变，也根本没时间向各级做心服口服的说服工作。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "位置上领导者只能是孤家寡人，其他人只能信托于他、下好离手、愿赌服输；有赌未为输，总好过什么也做不成。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然他人不赞同理所当然，事情就须靠领导者力排众议、坚定不移，并依赖下属职业精神来贯彻；这也是成功组织讲求服从精神的原因。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这其实与“勇气”和“智慧”没多大关系，只是组织实践中大量存在的常见现象；造成“远见卓识”的是只有你知道的数据，不是“惊人才干”。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正驱动领导者的是无法寻求他人理解的恐惧和危机。", "evidence": ["E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的勇气只是对不行动本身的怯懦；勇气只是一种正确的怯懦。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "为显示自己的“狠气”而做的事情不叫勇气，只是愚蠢的、往往被事实证明不堪一击的鲁莽。", "evidence": ["E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是因为提前看到了别人无法直接看到的危险而坚定不移往前推，才客观上显出有魄力。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把结论的与众不同归因于“看到了不同的数据”而非自己“有特殊的英明”，是“有魄力”与“不知死活”的筛选线。", "evidence": ["E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到了该位置自然就会“有魄力”；它本身不是一种能力，而是“职业危害”，不用“学”。", "evidence": ["E20"]},
    {"claim_id": "C014", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者把问题转向：你是怎样一步步走到领袖位置的？这群人为何能放下疑虑去执行其实无法核实是否合理的决策？", "evidence": ["E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "行文至此，话题已经是在谈论 Faith。", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "先承认并复述“魄力”的流行剧本（力排众议、事后成功被赞枭雄），并点出看错者不会进入样本。",
    "指出该剧本被归结为“超人的智慧与勇气”，随即否定这一归因。",
    "给出替代解释：领袖的思考角色与最高保密级别使其数据起点更高。",
    "补充条件：数据不能全面分享；环境瞬息万变，来不及逐一说服。",
    "由此推出领导者只能被信托，事情须靠力排众议与下属职业精神，故组织讲求服从。",
    "收束为与勇气智慧无关的组织常态，并把驱动因素定为无法寻求理解的恐惧与危机。",
    "重新定义勇气（正确的怯懦），否定“狠气”式鲁莽。",
    "给出“有魄力/不知死活”的归因分界线，并判定魄力是位置带来的“职业危害”。",
    "留下问题：如何走到该位置、下属凭什么执行无法核实的决策（Faith）。"
   ],
   "concept_usage": [
    {"term": "魄力", "meaning": "外界对领袖力排众议式决策的称赞；作者主张它实为位置与数据优势的客观显现，而非个人能力。", "evidence": "P001", "ambiguity": "作者既用它指流行说法，又用它指客观效果，两个用法在文中并存。"},
    {"term": "职业危害（occupational hazard）", "meaning": "到达领袖位置后自然产生的处境性后果，作者以此与“能力”对立。", "evidence": "P021", "ambiguity": "作者用英文原词括注，未给出定义细化。"},
    {"term": "勇气", "meaning": "被重述为“对不行动本身的怯懦”“一种正确的怯懦”，与显示“狠气”相对。", "evidence": "P016", "ambiguity": "与常识中“勇敢”的正面含义不同，文中未展开论证该重定义。"},
    {"term": "保密级别／最高机密数据", "meaning": "领袖判断优势的来源：独享企业全部最高机密数据且不能全面分享。", "evidence": "P008", "ambiguity": "未说明何种组织规模或行业适用。"},
    {"term": "服从精神", "meaning": "成功组织所讲求的下属品质，对应“你先说服我”式下属的反面。", "evidence": "P013", "ambiguity": "未界定服从的边界。"},
    {"term": "Faith", "meaning": "结尾处指下属据以执行无法核实之决策的东西；以破折号引出，未展开。", "evidence": "P024", "ambiguity": "全篇仅此一处，无定义。"}
   ],
   "examples_and_targets": [
    "大老板力排众议提出颠覆性策略、事后被赞“一代枭雄”的桥段（P001-P005）：作者复述的流行叙事，同时是被分析、被改述的对象。",
    "“事后诸葛亮们”（P005）：被作者用来指称事后归因者的修辞称呼。",
    "旅长、团长（P010）：以军事层级类比需被说服的中层，属修辞性类比。",
    "“你先说服我”的神仙（P013）：被作者引作反面下属形象。",
    "P004“看错了也就全剧终了，不会放进这个数据集里”：指样本选择现象，语料/数据集语境未在正文说明。"
   ],
   "conditions": [
    "“典型表现常常是”（P001）：作者对流行剧本的概括带频率限定。",
    "“这并不见得是因为ta多么伟大睿智”（P008）：明确保留，不排除个人因素。",
    "“在大多数情况下”（P010）：说明无时间说服是常态而非全部情形。",
    "“数据常常是不能全面与任何人分享的”（P008）：以“常常”限定。",
    "结论依赖于“到了这个位置/身居九重之上”的处境（P011、P021），不是对所有管理者的普遍断言。"
   ],
   "rhetoric_and_tone": "冷峻、反常识的断言体；先立流行剧本再一句“但这是错的”翻转；大量军事与古语化比喻（身居九重之上、旅长团长、下好离手、愿赌服输）；用独立短句给勇气下判词（P016、P017）；全篇用性别中立的“ta”；末段以破折号加英文单词 Faith 收束，留下悬念。",
   "unresolved_questions": [
    "P004“不会放进这个数据集里”指向的样本筛选机制与“数据集”语境，正文未说明。",
    "作者把问题转为“如何走到领袖位置”（P022）但未回答该问题。",
    "Faith 一词在本文未定义、未展开（P024）。",
    "“妥善、应分的处理手段”一类判断在本文未出现，作者未说明除服从与力排众议外还有哪些可选做法。",
    "军事比喻（旅长团长、九重之上）对应的组织形态未明说，是否专指企业未说明。",
    "“看对/看错”的判定主体与时间尺度未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“魄力”的典型表现常常是大老板有一天好像发了疯，力排众议、一意孤行的提出了颠覆性的策略。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P006", "quote": "这个常常被归结为一种“超人的智慧与勇气”。", "relation": "context"},
    {"key": "E3", "paragraph_id": "P007", "quote": "但这是错的，两个方面都错了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "而是因为ta有最高的保密级别，某种意义上是唯一知道企业全部最高机密数据的人。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "ta做判断的数据起点就高一些，自然会得出每一个只掌握部分数据的人都不见得会同意的结论。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "取得全部团队成员的一致信服常常根本是不现实的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "组织所处的瞬息万变的环境条件也根本没给你时间做这样的工作", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "其他人只能信托于你，下好离手、愿赌服输。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "有赌未为输，总好过什么也做不成。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "那么很自然事情多多少少都要靠你力排众议，靠你坚定不移，并且要依赖下属的职业精神来贯彻。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "这也是为什么成功的组织讲求服从精神。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "这其实与“勇气”和“智慧”没多大关系。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "真正让你有“独特见解”“远见卓识”的是只有你能知道的一些数据，而不是你有“惊人才干”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "真正驱动你的，是无法寻求ta人理解的恐惧和危机。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "永远记住，真正的勇气，只是对不行动本身的怯懦。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "勇气只是一种正确的怯懦。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "为了显示自己的“狠气”而做的事情，不叫勇气", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "是因为你提前看到了别人没法直接看到的危险，所以你坚定不移的往前推", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "是“有魄力”和“不知死活”的一道筛选线。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "这本身本身并不是一种能力，而是一种“职业危害”（occupational hazard），不用“学”。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "真正的问题是，你是怎么一步步走到那个领袖位置上的。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "为什么这群人可以放下自己的疑虑去执行ta们其实无法核实是否真的合理的决策？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P024", "quote": "——我们已经在谈论Faith了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理", "领导力", "决策与信息", "归因与认知"],
   "issue_candidates": ["魄力的来源与归因", "领袖的信息优势与保密", "服从与执行力", "勇气的定义", "幸存者偏差"],
   "text_function_candidates": ["答疑", "论辩", "概念澄清", "反常识修正"],
   "object_candidates": ["知乎提问者", "大老板/领袖", "下属与团队", "事后评论者"],
   "working_keywords": ["魄力", "职业危害", "occupational hazard", "保密级别", "力排众议", "服从精神", "勇气", "怯懦", "Faith"]
  },
  "notes": "无图片节点，正文完整可读。提问（怎样成为有魄力的人）隐含“魄力可学”，作者实际否定这一点，属提问者立场与作者立场的分歧，未混同。P004 提及“数据集”，疑与语料/平台语境有关，未在正文说明。"
 },
 "cf744236": {
  "analysis": {
   "question_context": "提问者问“顶级作家和普通作家的差距体现在哪些方面?”，预设可用“顶级/普通”的等级差来衡量作家。作者不按该框架作答，改以“作家想说什么”分三档，并以一句反问质疑“顶级”这一提法本身。提问者的等级框架属提问者，作者的回应是换掉评价坐标。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以三行排比给出作家三档：三流想说欲罢不能的故事，二流想说不容置疑的答案，伟大想说无言以对的问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "反问式质疑提问所用的“顶级”提法（“顶级”是什么鬼）。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者按作家“想说什么”分三档：三流作家想说一个欲罢不能的故事，二流作家想说一个不容置疑的答案，伟大作家想说一个无言以对的问题。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑“顶级”这一提法本身，未接受提问的“顶级/普通”框架。", "evidence": ["E4"]}
   ],
   "argument_steps": [
    "不下等级判词，改以“想说的内容”给作家分三档（故事／答案／问题）。",
    "三档以排比并列，未给判准与例证。",
    "末句以口语反问对“顶级”一词本身提出质疑。"
   ],
   "concept_usage": [
    {"term": "三流作家／二流作家／伟大作家", "meaning": "按作家“想说的东西”区分的三档（欲罢不能的故事／不容置疑的答案／无言以对的问题），不是按技艺或销量分高下。", "evidence": "P001", "ambiguity": "分档依据与“三流—二流—伟大”的递进关系未说明；与提问的“顶级/普通”如何对应未说明。"},
    {"term": "顶级", "meaning": "提问者使用的等级提法，作者以反问表示不接受。", "evidence": "P004", "ambiguity": "是修辞性吐槽还是明确的概念否定，正文未展开。"}
   ],
   "examples_and_targets": [
    "提问框架“顶级作家和普通作家的差距”（Q001）：被作者反问、回避的对象，属提问者说法。",
    "“欲罢不能的故事／不容置疑的答案／无言以对的问题”（P001-P003）：作者自拟的三类写作目标，非具体作家例证。",
    "正文未出现任何具体作家、作品或数据。"
   ],
   "conditions": [
    "三句均为无条件的并列断言式短句，正文未出现“如果”“除非”“通常”“可能”等限定词。",
    "全文未说明该分档适用的时代、文体或读者范围。"
   ],
   "rhetoric_and_tone": "格言体三行排比，句子结构完全对称、以“想说一个……”反复；末句突然转为口语吐槽（“是什么鬼”），以落差否定提问的等级框架。全篇 60 字，无展开论证。",
   "unresolved_questions": [
    "分档判准与理由未说明（为何故事/答案/问题对应三流/二流/伟大）。",
    "“欲罢不能”“不容置疑”“无言以对”各自的评价含义未界定。",
    "作者未直接回答提问的“差距体现在哪些方面”。",
    "末句是否等于明确否定“顶级”概念，还是仅表达不屑，无法确定。",
    "正文之外是否另有展开（如评论或后续补充），本记录不可见。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "三流作家想说一个欲罢不能的故事，", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "二流作家想说一个不容置疑的答案。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "伟大作家想说一个无言以对的问题。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "“顶级”是什么鬼。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文学与写作", "文艺评论"],
   "issue_candidates": ["作家高下的判准", "写作目的（故事/答案/问题）", "等级化评价框架的适用性"],
   "text_function_candidates": ["评论", "格言式回应", "质疑提问框架"],
   "object_candidates": ["提问者", "三流/二流/伟大作家"],
   "working_keywords": ["三流作家", "二流作家", "伟大作家", "欲罢不能", "不容置疑", "无言以对", "顶级"]
  },
  "notes": "无图片节点，正文完整（仅 4 段 60 字）。brief 前三行与正文 P001-P003 一致，brief 末尾““顶级”是什么鬼。”即 P004。作者未正面回答提问所列的“差距体现在哪些方面”。"
 },
 "b203d8f0": {
  "analysis": {
   "question_context": "提问者问“如何看待有人觉得防止男性青少年女性化是在歧视女性？”，把讨论设定在“是否构成歧视女性”的判断上。作者不直接裁决该标签，转而追问“防止男性青少年女性化”到底要防的是什么“化”，并分析“防止xx化”这一句式的结构，主张该句式空格里不可以接人类身份。提问者转述的“有人觉得……是歧视女性”属提问者与他人说法，不是作者主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "连续追问要防止的具体内容，并列举温柔化、含蓄化、卫生化、安静化、皮肤细腻化、苗条化以及“女性”格子里可能填的软弱、脆弱、幼稚、愚蠢、无知。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P012", "P013"], "summary": "给出核心判断：“防止xx化”句式空格里不可以接人类身份，否则就是教科书式地对人不对事。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015"], "summary": "批评在此问题上纠缠的众多论者为“越抹越黑”，再追问该句式究竟是什么句式。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P016", "P017"], "summary": "以邻居打小孩、骂其将来变得跟隔壁那人一样为例，指出这就是要防止小孩“你”化。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P018"], "summary": "以反问收束：把这种处境翻译给读者自己，问“这对你算啥”。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反复追问“防止男性青少年女性化”具体要防的是什么“化”，要求把“女性”这一格子里填的内容说清楚。", "evidence": ["E1", "E2", "E3", "E5"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“防止xx化”这种句式的空格里根本就不可以接人类身份，否则就是教科书式地对人不对事。", "evidence": ["E6", "E7"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者批评围绕此问题纠缠的众多论者是在越抹越黑。", "evidence": ["E8"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以邻居打骂小孩的类比说明：所谓“防止xx化”实质是要防止自己的小孩变成某个具体的人（“你”化）。", "evidence": ["E9", "E10"]},
    {"claim_id": "C005", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以反问要求读者设身处地：若被这样对待，这对你算啥。", "evidence": ["E11"]}
   ],
   "argument_steps": [
    "以“说清楚点”开场，把争论从立场判断拉回概念界定：到底要防什么“化”。",
    "连续列举若干谈不上负面的“化”（温柔、含蓄、卫生、安静、皮肤细腻、苗条）以显该表述难以界定。",
    "进一步追问“女性”格子里填的是什么，并列出软弱、脆弱、幼稚、愚蠢、无知等负面词。",
    "给出句式层面的判断：空格里不可以接人类身份，否则是对人不对事。",
    "批评纠缠者为越抹越黑，并再问该句式是什么句式。",
    "用邻居打小孩的类比把“防止xx化”还原为“防止小孩变成某个具体的人”。",
    "以“这对你算啥”的反问把处境转给读者。"
   ],
   "concept_usage": [
    {"term": "防止xx化／防止女性化", "meaning": "作者把它当作一个可检验的句式：空格若填人类身份即不成立；对“女性化”本身则要求给出具体所指。", "evidence": "P012", "ambiguity": "作者未给该句式一个正面定义，只给出否定性判准。"},
    {"term": "“女性”那个格子", "meaning": "作者用以指称该表述中被填入内容的空位，候选内容为软弱、脆弱、幼稚、愚蠢、无知。", "evidence": "P009", "ambiguity": "作者以反问列举，未确认哪一项才是提出者本意。"},
    {"term": "对人不对事", "meaning": "作者的评价坐标：以人类身份而非具体行为为靶，故属教科书式错误。", "evidence": "P013", "ambiguity": "未给出“对事”的正面标准。"},
    {"term": "“你”化", "meaning": "作者自造的类比说法，指把某个具体的人当作要防止变成的对象。", "evidence": "P017", "ambiguity": "属修辞构造，非既有术语。"}
   ],
   "examples_and_targets": [
    "候选“化”清单：温柔化、含蓄化、卫生化、安静化、皮肤细腻化、苗条化（P002-P007）：作者设问式例举，用以暴露表述不可界定。",
    "负面属性清单：软弱、脆弱、幼稚、愚蠢、无知（P010）：作者设问式例举。",
    "隔壁邻居打小孩并骂“你不努力，你将来就会变得跟隔壁那人一样”（P016）：作者虚构的类比场景。",
    "“防止自己的小孩‘你’化”（P017）：作者类比的关键构造。",
    "被批评对象：“无数人非要在这越抹越黑”（P014），未具名；提问中“有人觉得……是在歧视女性”（Q001）属提问者转述，本文未点明具体来源。"
   ],
   "conditions": [
    "“否则是教科书式地对人不对事”（P013）：以 P012 的判准为条件的推论。",
    "作者的追问针对“防止男性青少年女性化”这一表述（P001），未指名任何具体文件、机构或时间。",
    "全文以反问构成，未声明结论的适用范围；对“歧视女性”标签本身未作正面判定。"
   ],
   "rhetoric_and_tone": "通篇反问与追问，语气强硬、带挑衅与激将（“有胆说个清楚吗？”“是什么鬼”式的质问）；以极短并列句排比（温柔化？含蓄化？卫生化？）制造围攻感；引述邻居台词时用感叹与拟声（“你还敢躲？！啪！啪！”）增强戏剧性；末句用第二人称“你”把处境压给读者。",
   "unresolved_questions": [
    "作者未正面回应“防止男性青少年女性化是否歧视女性”这一提问框架。",
    "文中“有人觉得”“无数人”均未具名，所针对的具体言论、文件或机构不明，需外部核查该讨论背景。",
    "“卫生化”“安静化”等是否被作者视为对女性的刻板印象，正文未明说。",
    "作者未给出“对事”的正面标准，也未说明该句式可接受的填法。",
    "正文未出现“歧视”一词，提问中的这一定性在正文中没有被处理，需在研究中注意二者不对称。",
    "brief 末尾“女性化，具体是”为截断片段，正文 P011 为完整句“女性化，具体是什么化，有胆说个清楚吗？”，以正文为准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "说清楚点，这具体是要防止男性青少年什么化？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P008", "quote": "来，说清楚这具体是要防他们什么“化”？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P009", "quote": "“女性”那个格子里，填的到底是什么？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "软弱？脆弱？幼稚？愚蠢？无知？", "relation": "context"},
    {"key": "E5", "paragraph_id": "P011", "quote": "女性化，具体是什么化，有胆说个清楚吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "“防止xx化”这种句式，空格里根本就不可以接人类身份。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "否则是教科书式地对人不对事。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "无数人非要在这越抹越黑。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "你不努力，你将来就会变得跟隔壁那人一样！", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "这就是人家要防止自己的小孩“你”化！", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "你翻译翻译，这对你算啥？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别议题", "语言与修辞分析", "公共表述评论"],
   "issue_candidates": ["“防止男性青少年女性化”表述", "性别刻板印象", "以人类身份为靶的表述方式", "概念界定缺失"],
   "text_function_candidates": ["批评", "反问式论辩", "概念追问"],
   "object_candidates": ["提问者", "提出“防止女性化”者（未具名）", "男性青少年", "女性", "被当作反例的邻居小孩"],
   "working_keywords": ["防止女性化", "防止xx化", "女性化", "对事不对人", "人类身份", "温柔化", "含蓄化", "卫生化", "安静化"]
  },
  "notes": "无图片节点，正文完整（18 段）。作者以追问与句式分析代替对“歧视女性”标签的正面裁判；正文未出现“歧视”一词，提问中的定性未被作者直接处理，登记于未决问题。文中被批评对象均未具名，背景需外部核查。"
 },
 "f04084e1": {
  "analysis": {
   "question_context": "提问者问“为什么日本的大街上没有早餐供应？”，要求解释一个现象。作者给出两条并列解释：一是环境法规下中国式早餐摊的垃圾产生量会招致重罚，罚款摊入成本后价格高到吃不起；二是日本街边因被人放置炸弹而基本没有垃圾桶，消费者的碗与包装袋无处处置。属对提问者问题的解释性回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "解释路径一：环境法规下垃圾产生量招致重罚，罚款摊入成本使早餐贵到吃不起。", "role": "reason"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "解释路径二：因被人放过炸弹，街边基本没垃圾桶，吃完的碗与包装袋无处可丢。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在日本的环境法规下，按中国早餐摊那种垃圾产生量，经营者恐怕会被罚到极重。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把罚款摊入成本，早餐会贵到人吃不起（因而难以经营）。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为曾被人放置炸弹，日本街边基本没有垃圾桶。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问消费者吃完的碗、撕下的包装袋该端上电车还是塞进西装口袋或背包，指出垃圾无处处置使街头早餐模式难以成立。", "evidence": ["E4"]}
   ],
   "argument_steps": [
    "以日本环境法规为前提，按中国早餐摊的垃圾产生量推重罚。",
    "把罚款摊入售价，推出早餐贵到人吃不起。",
    "另举一条理由：因炸弹事件，街边基本没有垃圾桶。",
    "以反问呈现消费者垃圾无处可丢的处境，收束解释。"
   ],
   "concept_usage": [
    {"term": "环境法规", "meaning": "作者指日本对街头经营与垃圾处置的法规约束，用以解释重罚。", "evidence": "P001", "ambiguity": "未给出法规名称、条款或罚款额度。"},
    {"term": "中国早餐摊那种垃圾产生量", "meaning": "作者用作比较基准的垃圾产生规模。", "evidence": "P001", "ambiguity": "无数据支撑，仅为量级类比。"},
    {"term": "罚款摊进去", "meaning": "把罚款作为成本项计入售价的假设性推演。", "evidence": "P002", "ambiguity": "未说明是否真有人如此定价。"},
    {"term": "被人放过炸弹", "meaning": "作者给出的日本街边没有垃圾桶的原因。", "evidence": "P003", "ambiguity": "未指明具体事件、时间与地点，待外部核查。"}
   ],
   "examples_and_targets": [
    "中国早餐摊（P001）：作为垃圾产生量的比较基准，属类比材料。",
    "日本街边无垃圾桶及“被人放过炸弹”（P003）：作者的事实断言，本文无出处，待外部核查。",
    "消费者场景：吃完的碗、撕下的包装袋、端上电车、西装口袋、背包（P003）：作者反问式例证。",
    "提问“为什么日本的大街上没有早餐供应？”（Q001）：被解释的对象，属提问者说法。"
   ],
   "conditions": [
    "“在日本的环境法规下”（P001）：结论限于日本法规环境。",
    "“按中国早餐摊那种垃圾产生量”（P001）：以中国摊贩的量级为比较前提。",
    "“把罚款摊进去”（P002）：假设性成本转嫁条件。",
    "“基本没垃圾桶”（P003）：以“基本”作程度限定，未称完全没有。",
    "全文未说明所指城市、时段、例外情形，也未排除其他可能原因。"
   ],
   "rhetoric_and_tone": "口语化短句与夸张说法（“怕不要被罚到死”）；连续反问把读者代入消费者处境（“要端上电车么？还是塞进西装口袋或者背包？”）；两条理由平行罗列，无数据与展开论证，属简短解释体。",
   "unresolved_questions": [
    "“被人放过炸弹”具体指哪一事件、何时何地，正文未说明，需外部核查。",
    "未给出环境法规名称、罚款额度或早餐摊垃圾量的任何数据。",
    "未讨论其他可能解释（如便利店与自带早餐习惯、通勤结构、房租人力成本）是否被排除。",
    "“日本的大街”所指城市或范围未说明。",
    "正文仅 107 字，作者未说明这两条解释的确定程度，事实断言需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在日本的环境法规下，按中国早餐摊那种垃圾产生量，怕不要被罚到死。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "把罚款摊进去，早餐贵到人吃不起。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "因为被人放过炸弹，日本街边基本没垃圾桶", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "你吃完的碗、撕下的包装袋要端上电车么？还是塞进西装口袋或者背包？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会观察", "城市生活", "公共管理与环境卫生"],
   "issue_candidates": ["日本街头早餐供应缺失", "垃圾处置与法规成本", "街头经营的外部性"],
   "text_function_candidates": ["答疑", "解释", "经验推断"],
   "object_candidates": ["日本（街头与法规）", "中国早餐摊", "日本消费者"],
   "working_keywords": ["环境法规", "早餐摊", "垃圾产生量", "罚款", "垃圾桶", "炸弹", "电车"]
  },
  "notes": "无图片节点，正文完整但极短（3 段 107 字）。关于环境法规与“被人放过炸弹”的事实断言本文无出处，登记为待外部核查，本记录不作裁决。"
 },
 "7c1411c5": {
  "analysis": {
   "question_context": "提问者问“战胜抑郁症的人是不是相当于涅槃重生？”，预设“战胜”与“涅槃重生”可以直接等同。作者承认这一说法“错是不错的”，随即把问题转为“什么叫做‘战胜’了”，用一连串假设情境与反问检验“死里逃生”是否等于战胜，最后给出两条标准，并判定严格意义上“涅槃重生”不够资格形容真正的不同。提问中的判断属提问者，作者未简单认同。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "让步后重设问题：说法不算错，但“战胜”一词未被定义。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009"], "summary": "三组假设情境反问：赌博负债后中彩票、高考失利后留学转移注意力、吃药拖着等到危机消退，这些算不算“战胜”。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011"], "summary": "概括多数人只是靠药物、顾虑和安慰拖着，到时过境迁侥幸死里逃生；并提到历史上确有把死里逃生称为“胜利”的传统。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014"], "summary": "提出“战胜”的第一条标准：同样的事重演时是否不会再次陷入同样的绝望。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "以两次癌症的对照说明第一条标准：未再同样绝望算战胜了一点，仍一样绝望则谈不上胜。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019"], "summary": "否定死里逃生的心理效应等于战胜，并追问这些效应对卷土重来的下一轮敌人有何意义。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "以敌国再犯为喻：对旧敌的笃定感不构成改变，虚幻安全感反而妨碍实际准备，唯有沟、墙、粮、兵有用。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "第二条标准与结论：任何悲惨都不再令你绝望才是全胜；严格意义上“涅槃重生”不够资格形容这种不同。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P029"], "summary": "两个与悲观、运气有关的句子，疑为平台关联问题或话题标签混入，作者未承接。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "“战胜抑郁症相当于涅槃重生”这话错是不错的，问题在于“什么叫做‘战胜’了”尚未明确。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以三组假设情境反问：靠中彩票式的外部转机、靠换环境转移注意力、靠药物拖着等到危机消退，这些算不算“战胜”了抑郁症。", "evidence": ["E3", "E4", "E6", "E7"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大部分人只是借着药物、顾虑和安慰拼命拖着，等时过境迁侥幸死里逃生，约等于被围城中吃尽粮食、马、老鼠、人而熬到敌人退走。", "evidence": ["E8", "E9"]},
    {"claim_id": "C004", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者说句实话：历史书上的确有把这种死里逃生称为“胜利”的传统。", "evidence": ["E10"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“战胜”的标准有两个：一是同样的事情重新发生一次时不会再次陷入同样的绝望；二是不再会有任何事情让你真正的绝望。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "第一次癌症误诊死里逃生、第二次真确诊却未像第一次那样绝望，可算一种战胜——不算全胜，但至少战胜了一点。", "evidence": ["E14"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "死里逃生的如释重负、“及时行乐”的洒脱心态与“得道飞升”“大彻大悟”感，并不叫做战胜。", "evidence": ["E15", "E16"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "再来一次故事会有好的不同才叫进步；这些心理效应面对卷土重来的下一轮敌人意义存疑。", "evidence": ["E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "死里逃生带来的虚幻安全感和“成熟感”会造成“北狄不过如此”的幻觉，妨碍深挖沟、高筑墙、广积粮、精练兵。", "evidence": ["E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "让你下次有所不同的不是“不过如此”的“战略藐视”，而是深挖的沟、高筑的墙、广积的粮、精练的兵。", "evidence": ["E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "即使世上所有能想象与不能想象的悲惨一起发生仍不绝望，才是真正的全胜；若是这个意义上的战胜，你才会真的有所不同。", "evidence": ["E20", "E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "严格意义上说，“涅槃重生”不够资格形容这种不同。", "evidence": ["E22"]}
   ],
   "argument_steps": [
    "承认提问说法不错，但把争论焦点移到“战胜”的定义。",
    "用三个假设情境反问：外部转机、注意力转移、拖着等危机消退是否算战胜。",
    "概括多数人的实况是借着药物、顾虑、安慰熬到时过境迁，属侥幸死里逃生。",
    "引述历史上把死里逃生称为“胜利”的传统，作为需要重新审视的对照。",
    "给出第一条标准：同样的事重演是否不再陷入同样绝望，并以两次癌症的对照说明。",
    "否定死里逃生的心理效应等于战胜，追问其对下一轮打击的意义。",
    "以敌国再犯为喻，说明虚幻安全感妨碍实际准备，唯有沟、墙、粮、兵有效。",
    "给出第二条标准（永不绝望）并作结：这是真正的全胜，“涅槃重生”不够资格形容。"
   ],
   "concept_usage": [
    {"term": "战胜", "meaning": "作者以两条标准界定：重演时不再次陷入同样绝望；不再有任何事情让你真正绝望。不等同于结果上脱离痛苦。", "evidence": "P013", "ambiguity": "两条标准是并列还是递进（半胜/全胜）文中略有滑动。"},
    {"term": "涅槃重生", "meaning": "提问者用语；作者认为严格意义上不够资格形容第二条标准达成后的不同。", "evidence": "P028", "ambiguity": "作者未说明该词应有何种更严格用法。"},
    {"term": "死里逃生", "meaning": "多数人靠药物、顾虑、安慰拖到时过境迁的状态；作者明确不承认其构成战胜。", "evidence": "P010", "ambiguity": "作者同时承认历史上有把死里逃生称为胜利的传统，二者关系未调和。"},
    {"term": "全胜", "meaning": "第二条标准达成，即任何悲惨一起发生仍不绝望。", "evidence": "P026", "ambiguity": "与 P015“不算全胜”的用法一致，但可达成的判准未给。"},
    {"term": "战略藐视", "meaning": "作者贬抑的心态，与深挖沟、高筑墙、广积粮、精练兵的实体准备相对立。", "evidence": "P024", "ambiguity": "作者未说明其来源（疑似化用军事成句）。"},
    {"term": "the devil I know", "meaning": "面对去年来过的同一敌人时的笃定感。", "evidence": "P020", "ambiguity": "作者未展开该俗语的含义。"}
   ],
   "examples_and_targets": [
    "赌博输光家产、欠一百来万，一个月后中一亿福利彩票（P003-P004）：作者假设情境，用于反问。",
    "高考失利掉头发、家里凑钱送乌克兰留学、忙着查“如何与乌克兰妹子深入交流”（P006）：作者假设情境，带调侃色彩。",
    "吃药熬着、被“冲喜”、危机消退（P008）：作者列举的常见情形。",
    "被围城中吃粮食、吃马、吃老鼠、吃人，熬到冬天敌人退走（P010）：类比材料。",
    "第一次癌症误诊、第二次真确诊但未同样绝望（P015）：作者用于界定第一条标准的例证。",
    "历史书把死里逃生称为“胜利”的传统（P011）：作者引述的说法，未给出处，待外部核查。",
    "北狄、南蛮、东夷、西戎（P020-P021）：古代外敌代称，喻不同类型的下一轮打击，属修辞材料。",
    "深挖沟、高筑墙、广积粮、精练兵（P023-P024）：历史成句作类比。",
    "“得道飞升”“大彻大悟”“我看待一切的感觉都不同了”（P017）：被作者贬抑的他人话语风格，未具名。",
    "P029 关于悲观与运气的两句（P029）：疑为平台关联问题或话题标签混入正文。"
   ],
   "conditions": [
    "“如果同样的事情重新发生一次”（P014）：第一条标准的条件表述。",
    "“如果还是一样绝望，那么胜在哪里了？”（P016）：反事实检验。",
    "“也许来的还是去年来过的北狄”（P020）／“但若这次来的是南蛮呢？东夷呢？西戎呢？”（P021）：以敌人类型变化为条件。",
    "“即使此刻就身患绝症了、众叛亲离了……你仍然不会绝望”（P026）：第二条标准的极端假设。",
    "“如果是这个意义上的战胜”（P027）／“严格意义上说”（P028）：结论的限定语。",
    "第一次／第二次癌症的对照（P015）以“不像第一次那样绝望”为判定条件。"
   ],
   "rhetoric_and_tone": "全篇以设问推进（“算不算”“这算不算”“胜在哪里了”）；采用让步—反驳结构（“错是不错的”→“但是那并不叫做战胜”）；密集使用守城与军事比喻（围城、北狄南蛮东夷西戎、战略藐视、战略轰炸、沟墙粮兵）；夹杂口语调侃（乌克兰妹子、还不如一根香烟管用）；以“严格意义上说”作训诫式收束；不使用个人病史叙事，全部为设例与论辩。",
   "unresolved_questions": [
    "作者未说明“抑郁症”与其设例中的处境性痛苦是否同一，也未讨论药物与临床治疗的作用（仅在 P010 提到“借着药物、顾虑和安慰拼命的拖着”）。",
    "P011“历史书上的确是有把这个称为‘胜利’的传统”未给出处，需外部核查。",
    "P029 两句（悲观的人如何变乐观、运气极差如何恢复运气）疑为平台关联问题或话题标签混入正文，作者未承接；该段被 render 标为 lexical 未覆盖片段。",
    "提问的“涅槃重生”框架未被直接肯定或否定，只被判为“不够资格”形容。",
    "第二条标准（永不绝望）是否可达成、如何检验，正文未说明。",
    "“大部分人”所指范围与依据未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这话错是不错的。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "问题是，什么叫做“战胜”了？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "结果一个月以后，ta突然中了一个亿的福利彩票。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "那么ta算不算“战胜了抑郁症”？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "ta很快就忙着查“如何与乌克兰妹子深入交流”去了。", "relation": "context"},
    {"key": "E6", "paragraph_id": "P008", "quote": "吃药熬着、拖着，等到了事情有了转机，注意力转移了，被“冲喜”了，危机消退了", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "这算不算“战胜”了抑郁症？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "大部分人，只是借着药物、顾虑和安慰拼命的拖着，等到了时过境迁，于是侥幸死里逃生而已。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "约等于被围了，躲在城里吃粮食、吃马、吃老鼠、吃人，熬到了冬天敌人退走了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "说句实话，历史书上的确是有把这个称为“胜利”的传统。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "战胜的标准有两个：", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "1）同样的事情如果重新发生一次，是否不会再次陷入同样的绝望。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P025", "quote": "2）不再会有任何事情让你真正的绝望。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "那么算一种战胜——虽然不算全胜，但至少的确算战胜了一点。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "可能会给你一种强烈的“得道飞升”“大彻大悟”感", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "但是那并不叫做战胜。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "再来一次，故事会有好的不同才叫进步。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "还会造成“北狄不过如此”的幻觉，妨碍你去深挖沟、高筑墙、广积粮、精练兵。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P024", "quote": "会让你下次有所不同的不是“不过如此”的“战略藐视”，而是深挖的沟、高筑的墙、广积的粮、精练的兵", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P026", "quote": "你仍然不会绝望——这才是真正的全胜了。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P027", "quote": "如果是这个意义上的战胜，那么你的确会真的有所不同了。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P028", "quote": "严格意义上说，“涅槃重生”不够资格形容这种不同。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理健康", "心理调适与创伤", "军事史喻证", "人生哲学"],
   "issue_candidates": ["抑郁症“战胜”的判准", "心理效应与真实改变之别", "幸存与胜利之别", "创伤后的战略藐视风险"],
   "text_function_candidates": ["答疑", "概念辨析", "论辩", "训诫"],
   "object_candidates": ["提问者", "抑郁症经历者", "被围城池（喻）", "北狄/南蛮/东夷/西戎（喻）"],
   "working_keywords": ["战胜", "涅槃重生", "死里逃生", "全胜", "及时行乐", "冲喜", "战略藐视", "深挖沟", "高筑墙", "广积粮", "精练兵", "the devil I know"]
  },
  "notes": "无图片节点。正文 29 段完整可读，但 P029 被 render 标为“⚠lexical未覆盖片段”，内容为两句与悲观、运气有关的问句，疑为平台关联问题或话题标签混入正文，已单列为内容单元 U029 并在未决问题登记。P003、P006、P015 为作者假设性例证，非真实个案；P011 关于历史书写传统的说法无出处，待外部核查。"
 },
 "f1e1842d": {
  "analysis": {
   "question_context": "提问者问“为什么年轻人敢手撕领导？”，预设“敢”是需要解释的新现象。作者先给出解释（当代人较少亲眼见到得罪领导的惨痛后果，因而对后果更乐观），但随即判定新旧两代人的态度其实都不对，并把回答转为行动规范：领导有问题自有妥善手段，“手撕”永远错，应按能否辞得起职分层处理。提问中的“敢”的框架属提问者，作者不认同其隐含的可为性。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "解释当下原因：惨痛教训的可见度下降使人们对后果乐观；以前单位是人生整个舞台，如今最坏不过被辞退换工作。", "role": "reason"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "对照三四十年前：得罪领导可能几十年不能翻身的案例传说比比皆是，人们丝毫不敢乐观。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "判定两代人的态度其实都不对。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P004", "P005"], "summary": "给出原则：领导有问题自有妥善、应分的手段；“手撕”永远错，且与是否承受得起后果无关。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007", "P008"], "summary": "三步建议：辞得起职就辞职；辞不起就努力获取辞职的本钱；没有余力积累就辞职去攒本。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010"], "summary": "对既无余力积累又无法辞职者的判断：这就是你应得的待遇，是事实在告诉你“少妄想”。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012"], "summary": "给出区分不公与妄求的判准：能否换到更好的工作，即“事实给你的活答案”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P013", "P014"], "summary": "两种情形：对方顾忌你辞职则用不到手撕；不顾忌则手撕只会后悔，幸存者分享不具代表性。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P015"], "summary": "以幸存飞行员的叙述为类比，指出据此判断“高射机枪打不死人”是致命错误。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "年轻人敢手撕领导，是因为见到惨痛教训的情况变少，人们对后果更乐观；以前单位几乎是人生整个舞台，如今得罪领导最坏不过被辞退、背着负面背景调查换工作。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "早三四十年前无意间得罪领导而几十年不能翻身的案例传说比比皆是，所以人们对这件事一点也不敢乐观。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这两代人的态度其实都不对。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "领导有问题，自有妥善、应分的手段去处理。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“手撕”永远都是错的：这与有没有背得起的后果无关，而是它本来就不是解决对领导不认可的正当手段。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "处理方式应分层：辞得起职就辞职；辞不起职就努力获取辞职的本钱；被工作占满精力以至没有余力积累本钱，就辞职去攒本。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若被工作占满精力、一辞职就无法生活又无法迅速换到更好工作，那就是你应得的待遇——这是事实在告诉你“少妄想”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "区分别人对自己不公与自己在妄求的分界线是事实给的活答案：能换到更好的工作，要求就不过分；换不到而就地手撕要更好的，则根本要不到。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果对方顾忌你辞职，你哪里用得到手撕。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果对方并不顾忌你辞职，手撕只会让你自己后悔莫及；幸存者的得意分享不代表此事大有可为，粉身碎骨的高出一个数量级。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "听信幸存者“高射机枪打不死人”式的叙述，是在犯致命错误。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "先解释现象：惨痛教训的可见度下降使当代人对后果乐观。",
    "以三四十年前得罪领导几十年不能翻身的传说作对照，说明上一代不敢乐观。",
    "判定两代人的态度都不对，把问题从“为什么敢”转为“该怎么做”。",
    "给出原则：领导问题有妥善手段，“手撕”永远错且与后果能否承受无关。",
    "以能否辞得起职为轴给出三步行动建议。",
    "对既无本钱又无余力者的处境下判断（应得的待遇／少妄想）。",
    "给出区分不公与妄求的判准：能否换到更好的工作。",
    "分两种情形收束：对方顾忌你辞职则不必手撕；不顾忌则手撕只会后悔。",
    "以幸存者偏差的类比（高射机枪打不死人）警告判断错误。"
   ],
   "concept_usage": [
    {"term": "手撕", "meaning": "指与领导直接冲突对抗的做法；作者判定其永远错误，且不是解决对领导不认可的正当手段。", "evidence": "P005", "ambiguity": "作者未界定“手撕”的具体行为边界。"},
    {"term": "辞职的本钱", "meaning": "能否离职所依赖的经济与机会条件，作者建议按处境分层积累。", "evidence": "P007", "ambiguity": "未给出本钱的具体标准或数量。"},
    {"term": "应得的待遇", "meaning": "作者对既无辞职本钱又无余力积累者处境的定性，与“少妄想”相连。", "evidence": "P009", "ambiguity": "是否包含道德评价，文中未明说。"},
    {"term": "事实给你的活答案", "meaning": "以能否换到更好工作来检验要求是否过分的判准。", "evidence": "P012", "ambiguity": "该判准依赖劳动市场条件，作者未讨论市场本身的限制。"},
    {"term": "幸存者（偏差）", "meaning": "作者未用“偏差”一词，但以“幸存者得意洋洋的分享”与“粉身碎骨的高出一个数量级”表达同一机制。", "evidence": "P014", "ambiguity": "“高出一个数量级”无数据来源。"}
   ],
   "examples_and_targets": [
    "以前“单位就是人生的几乎整个舞台”、得罪领导几十年不能翻身的案例传说（P001-P002）：作者的历史对照叙述，无出处，待外部核查。",
    "“鸡即使是惨，也没惨在猴子们面前”（P001）：俗语式修辞。",
    "“战战兢兢，汗不敢出”（P002）：成句修辞。",
    "飞行员幸存者叙述“当时十把高射机枪对着我……炸了它个稀巴烂”（P015）：作者转述/构造的幸存者话语，用作偏差警示材料。",
    "反驳对象：因后果变轻而认为手撕可行的当代态度，以及据幸存者分享作判断者（P014-P015）；均为不具名对象。",
    "前提中被承认存在的“领导有问题”（P004）：作者不否认该前提，但否定其手段选择。"
   ],
   "conditions": [
    "“你能辞得起职，你就辞职”（P006）／“你辞不起职，你就努力获取辞职的本钱”（P007）／“你被工作占据了全部精力以至于没有余力去积累能辞职的本钱”（P008）／“如果你被工作占据了全部精力，又一辞职就会无法生活”（P009）：四种处境分支。",
    "“如果对方顾忌你辞职”（P013）／“如果对方并不顾忌你辞职”（P014）：两种对手情形。",
    "“不要看着这里好像很多幸存者得意洋洋的分享，就以为这事大有可为”（P014）：对样本代表性的限定。",
    "结论依赖“现在”与“早三四十年前”的时代对照（P001-P002）。"
   ],
   "rhetoric_and_tone": "第二人称“你”贯穿全篇的训诫口吻；三段辞职建议用“你能……你就……”排比推进；以“这话很难听，但是这话是句大实话”作强硬表态；夹杂动物俗语（鸡与猴子）与军事飞行比喻（高射机枪、直线俯冲、粉身碎骨）；破折号插入判断与告诫；对幸存者叙事带明显嘲讽（“喝得红光满面”）。",
   "unresolved_questions": [
    "P004 的“妥善、应分的手段”具体指什么，正文未说明（未提法律、劳动仲裁或工会途径）。",
    "“早三四十年前”的案例传说与“负面的背景调查”未给出处，需外部核查。",
    "“粉身碎骨的高出一个数量级”无数据来源。",
    "提问中的“年轻人”与文中“两代人”的对照未严格对应：提问问为何敢，作者答两代人都错。",
    "“手撕”的行为边界（当面冲突、举报、公开对抗是否都算）未界定。",
    "P001 提到“猴子们自己也不定多久以后就辞职了”，其推论未被展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "因为现在这样做而得到显而易见的惨痛教训的情况比较少了，所以人们开始对这样做的后果比较乐观了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "以前单位就是人生的几乎整个舞台。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P001", "quote": "现在得罪了领导最坏不过是被辞退、背着一个负面的背景调查换工作。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "早三四十年前，关于如何无意间得罪了领导而几十年不能翻身的案例传说比比皆是，所在多有，所以人们对这件事一点也不敢乐观。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "那么这两代人谁对了呢？其实都不对。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "领导有问题，自有妥善、应分的手段去处理。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "“手撕”永远都是错的。这跟有没有背得起的后果没有关系，而是这本来就不是解决对领导不认可的正当手段。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "你能辞得起职，你就辞职。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "你辞不起职，你就努力获取辞职的本钱。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "那么就辞职去攒本。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "那么你最好认识清楚——这就是你应得的待遇。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "这是事实在告诉你“少妄想”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "你不服，你就换，能换到更好的，那么你的要求就不过分", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "如果对方顾忌你辞职，你哪里用得到手撕？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "“手撕”只会让你自己后悔莫及", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "就以为“高射机枪打不死人”，这是在犯致命错误。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场关系", "组织行为", "风险判断", "代际差异"],
   "issue_candidates": ["手撕领导的后果", "辞职本钱与退路", "幸存者偏差", "不公与妄求的区分"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "行动建议"],
   "object_candidates": ["提问者", "年轻人", "领导", "三四十年前的从业者", "幸存者"],
   "working_keywords": ["手撕", "领导", "辞职的本钱", "应得的待遇", "少妄想", "幸存者", "粉身碎骨", "高射机枪"]
  },
  "notes": "无图片节点，正文完整（15 段）。P015 的飞行员叙述系作者转述/构造的幸存者话语，非作者本人经历，不得归为作者亲历。文中事实性断言（三四十年前的案例、背景调查、数量级差距）均无出处，登记为待外部核查。"
 },
 "0d1cbdf6": {
  "analysis": {
   "question_context": "提问者问“怎么看一个人有没有领导力？”，要求给出可判断的标志。作者不列行为清单，而是先区分“领导（lead）”与“管理（manage）”，把领导界定为从无路处开路、带人航向未知之地，再指出其要害是三项精神产品（世界观、价值观、人生观）的成熟与分享，并反驳“仲裁权来自给工资”的流行看法，最后给出按三条齐备程度的分层判断与去留建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以设问区分领导与管理，界定领导的职责：开路、航向未知、解决团队对未来的迷茫焦虑、观察多年期环境变迁、决定理想愿景与价值观、维护决策与顾问团队。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "履行职责的要害是完整自洽的世界观与通顺可持续的价值观，即高度成熟的世界观、价值观和人生观。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "领导本质上是对三项精神产品的分享；其质量带来追随价值，也因此获得仲裁的授权。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "反驳“仲裁权来自给工资”，并把纯金钱强迫关系定性为奴役和寄生关系，强调做事效果完全不同。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"], "summary": "分层判断：三条齐备为上上之选，退而求其次要道德观、价值观成熟，再退要愿景清晰而且坚定。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016"], "summary": "三条皆无则此非久留之处、非可托之人，意味着不能“定居”，应及早准备后路。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "领导是从没有路的地方走出路来、从走过的路上走出新路来，带领他人航向未知之地；领导主要解决团队对未来的迷茫和焦虑，管理团队的愿景和信心。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "领导负责观察未来一年、三年、五年、十年的环境变迁，决定团队的理想、愿景和价值观/伦理原则，并据此维护决策团队和顾问团队。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "履行这些职责最重要的要害，是完整自洽的世界观与通顺可持续的价值观，即高度成熟的世界观、价值观和人生观。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在本质上，所谓“领导”就是对世界观、价值观、人生观这三项精神产品的分享。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是这三项精神产品的高质量带来了其他人追随的价值，也因此才获得仲裁的授权。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "认为仲裁的权利来自给工资是完全错误的，因为有能力者也可以选择去别处领这份工资。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "那些为了钱不得不忍受强迫的人与领导之间根本不是领导和被领导的关系，只是一种奴役和寄生关系，做起事来效果完全不同。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判断的去留梯度：三条齐备为上上之选；退而求其次要道德观、价值观成熟；再退而求其次要愿景清晰而且坚定。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "三条一条都没有（至少不让你信服和乐观），就意味着此非久留之处、此非可托之人，你还不能“定居”，不能停止寻找，要及早准备后路。", "evidence": ["E12", "E13"]}
   ],
   "argument_steps": [
    "以“什么是领导、什么是管理”的设问开场，把问题转为定义问题。",
    "界定领导为开路与航向未知，并列出其职责范围（环境观察、愿景与价值观、维护决策与顾问团队）。",
    "指出职责的要害是完整自洽的世界观与可持续的价值观，即三观的高度成熟。",
    "给出本质判断：领导是三项精神产品的分享。",
    "从精神产品的质量推出追随价值与仲裁授权。",
    "反驳“授权来自工资”，并以奴役/寄生关系与之对照。",
    "把判断标准转为分层梯度：三条齐备→道德观价值观成熟→愿景清晰坚定→退无可退。",
    "以“此非久留之处，此非可托之人”给出离职与备后路的建议。"
   ],
   "concept_usage": [
    {"term": "领导（lead）", "meaning": "从无路处走出路、从旧路走出新路、带他人航向未知之地；解决团队对未来的迷茫与焦虑；本质是三项精神产品的分享。", "evidence": "P002", "ambiguity": "与“管理”的界线由职责描述间接给出，未作定义式对照。"},
    {"term": "管理（manage）", "meaning": "仅在开篇与“领导”并列提问时出现，正文未单独界定。", "evidence": "P001", "ambiguity": "作者未回答自己提出的“什么是管理”，属正文缺口。"},
    {"term": "仲裁的授权／仲裁的权利", "meaning": "追随者因精神产品质量而授予领导的裁决地位；作者否认其来自工资。", "evidence": "P008", "ambiguity": "“仲裁”的主体与事项范围未定义。"},
    {"term": "三项精神产品／三条", "meaning": "世界观、价值观、人生观（P006）；在后文分层建议处替换为“道德观、价值观”“愿景”。", "evidence": "P007", "ambiguity": "术语在 P006 与 P013-P014 之间有滑动，需人工核对是否同一组。"},
    {"term": "奴役和寄生关系", "meaning": "作者对纯以金钱强迫维持的雇佣关系的定性，与领导—被领导关系对立。", "evidence": "P010", "ambiguity": "带有强烈评价色彩，未给出判别标准。"},
    {"term": "定居", "meaning": "作者比喻长期托付于某一组织、停止寻找的状态。", "evidence": "P016", "ambiguity": "为比喻用法，无正式定义。"}
   ],
   "examples_and_targets": [
    "被反驳观点：“很多人认为仲裁的权利是来自于给工资”（P009-P010），对象不具名。",
    "“那些真的有能力、你想要获得分人才”（P009）：作者举例说明有能者可另择雇主，原文表述如此。",
    "“那些为了钱不能不‘忍受你的强迫’的人”（P010）：作者用以界定奴役/寄生关系的对象。",
    "时间尺度：未来一年、三年、五年、十年（P003）：作者提出的领导观察周期。",
    "正文未出现具体人物、机构或历史事件。"
   ],
   "conditions": [
    "“这往往体现在对历史的熟知和对时势的敏感……”（P005）：以“往往”限定。",
    "“至少不让你信服和乐观”（P015）：把“三条皆无”的判断限定在主观信服与乐观层面。",
    "分层条件：三条齐备／退而求其次／再退而求其次／退无可退（P012-P015）。",
    "结论以“要”字构成职责与行动要求（P002、P003、P016），未说明例外情形。"
   ],
   "rhetoric_and_tone": "以定义式设问开篇；正文多用排比与递退结构（上上之选→退而求其次→再退→退无可退）；书面语训诫与建议口吻并用；末段用文言式对句“此非久留之处，此非可托之人”与“定居”隐喻收束，判断色彩鲜明。",
   "unresolved_questions": [
    "作者在 P001 提出“什么是管理（manage）”，正文未作界定，属未答问题。",
    "“三项精神产品”（世界观/价值观/人生观）与后文“道德观、价值观”“愿景”的对应关系有滑动，需人工核对。",
    "“仲裁”一词未定义，谁向谁仲裁、授权对象与范围均未说明。",
    "除“给工资”之外的授权机制（如制度、任期、选举）未讨论。",
    "正文无具体人物或组织例证，判断标准如何操作化未说明。",
    "正文与 brief 有重叠：brief 首段与 P001-P002 基本相同，brief 末尾句与 P003 前半相同。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "领导，是要从没有路的地方走出路来，从走过的路上走出新路来，是要带领他人航向未知之地。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "领导要负责观察未来一年、三年、五年、十年的环境变迁", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "最重要的要害，是一个足够完整和自洽的世界观，一个足够通顺和可持续的价值观。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "这其实就是高度成熟的世界观、价值观和人生观。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "在本质上，所谓“领导”，就是对这三项精神产品的分享。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "是这三项精神产品的高质量，带来了其他人追随的价值，也因此才获得仲裁的授权。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "很多人认为仲裁的权利是来自于给工资，其实这是完全错误的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "而只是一种奴役和寄生关系。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "三条齐备，上上之选。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "退而求其次，要道德观、价值观成熟。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "再退而求其次，要愿景清晰而且坚定。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "那就意味着此非久留之处，此非可托之人。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "那就意味着你还不能“定居”，你不能停止寻找，要及早准备后路。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["领导力", "组织管理", "价值观与伦理"],
   "issue_candidates": ["领导与管理的区别", "领导力的判据", "权威与授权的来源", "追随与去留判断"],
   "text_function_candidates": ["答疑", "定义与解释", "论辩", "建议"],
   "object_candidates": ["提问者", "领导者", "追随者", "决策团队与顾问团队"],
   "working_keywords": ["领导", "管理", "lead", "manage", "世界观", "价值观", "人生观", "仲裁的授权", "精神产品", "奴役", "寄生", "定居"]
  },
  "notes": "无图片节点，正文完整（16 段）。作者对“管理（manage）”只提问未定义，属正文缺口，已登记未决问题。P009“那些真的有能力、你想要获得分人才”原文如此（疑有漏字），引文按原文保留，未作改写。"
 },
 "c4d83e89": {
  "analysis": {
   "question_context": "提问者只问“什么是正义？”。作者给出一个自称终极的定义（能让人类走向最大繁荣的伦理观），主张各流派之争其实都发生在“人类”“最大”“繁荣”三个词的定义上，然后从这一定义推出“正义必须是可行的”这一首要方面，区分“正义本身”与“正义的理想”，批评以攻击其他意识形态来主张正义的做法，并以对年轻人的劝告收束。全篇为作者自述的论辩，无引述的具名对象。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出正义定义（能让人类走向最大繁荣的伦理观），并主张该表述是终极的，不同意者所称“正义”只是同名异指。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "指出各派争议都发生在“人类”“最大”“繁荣”的定义上，并列举分歧类型。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "把这些分歧收在“人类最大繁荣”的共同前提之下，并把论述范围限定为此时此刻可断言的问题。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "由定义内在推出首要方面：正义必须是可行的，不可行的理念不属于正义讨论的范畴。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017"], "summary": "区分“正义的理想”与“正义本身”：现阶段不可行者只能是理想，理想不可作现实审判的法理基础。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019"], "summary": "对“无先例但理论可行”是否算不可行，作者承认为争议，需靠各行其是的天裁逻辑。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022"], "summary": "判定连“理论可行”都未达成却强烈主张者暂无被严肃讨论的资格，应先理顺逻辑，不要先主张正义性。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "可行性深不见底；历史上解决可行性者登上伦理王座直到被证伪；多数人信服不等于终极真理。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "主张正义须靠主张可行，而非指斥其他意识形态邪恶；有效主张须以实务历练为前提，否则无益而有害。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032", "P033", "P034"], "summary": "劝告年轻人先切实做事、近距离观察成败得失，不要过早拿起“正义”的“武器”，并记住先问可不可行。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P035", "P036"], "summary": "结论与标题句：正义观之间的竞争即可行性的竞争；正义并非最“当行”之事，而是最可行之事。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正义是一种能让人类走向最大繁荣的伦理观。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个定义表述是终极的，关于正义的一切不同流派都不能不同意；若不同意（或其等效命题），其所称“正义”只是一种发音上、字形上的巧合。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "各流派之间的一切争议都发生在对“人类”“最大”“繁荣”的定义上，而不发生在这个表述本身上。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "分歧表现为：有人把与自己种族、出身、阶级、立场不同者排除在配享繁荣的人类范围外；有人对“繁荣”理解不同；有人对“最大限度”理解不同。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论如何，“人类最大繁荣”这个共识是没有疑义可言的共同前提。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在此共识之上如何争论是未来人类历史要完成的历程；作者只站在此时此刻，谈论此时此刻就可以断言的问题。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正义必须是可行的，这是正义的定义所内在决定的；主张不可行的正义与“人类的最大繁荣”根本对立，故不可行的理念不属于正义讨论的范畴。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果只是现阶段不可行而将来可行，且你自己也认同这个阶段不可行，那么它至少不可以被视作正义本身，只能视为正义的理想。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正义的理想并非正义本身，这是两个不一样的概念；正义可作现实审判的法理基础，正义的理想不可以。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "若只是没有先例证明其可行而理论上可行，算不算不可行？作者认为这里存在争议，靠的是各行其是、may the best win 的天裁逻辑。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那些连“理论可行”也没有达成就加以强烈主张的伦理主张，暂时没有被严肃讨论的资格，更不应该进入被大力推行的阶段。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这不是说这些理念应被扫入垃圾堆，而是其主张者应首先把运行逻辑理顺、说通，求得理论可行、将来可行的成熟度。", "evidence": ["E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要在主张可行性之前就主张正义性。", "evidence": ["E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可行性本身是一个深不见底的问题，很难想象有任何伦理体系敢于宣称自己已经彻底解决了可行性问题。", "evidence": ["E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在现实历史中，若谁足够令人信服地解决了可行性问题，它就先于同期其他意识形态登上伦理的王座——直到它被事实证明其预告是错误的。", "evidence": ["E22"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类社会的兴衰转折本身就是一个又一个正义观在各自时代完成了“令人信服的表达了自己的可行性”的过程。", "evidence": ["E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“令足够多的人足够信服”并不是“终极真理”的可靠替代品。", "evidence": ["E24"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "主张其正义必须通过主张其可行来进行，而不是通过主张其他意识形态如何邪恶来进行；后者无效，且会消耗本可投入可行性证明的精力而损害该理念的机会。", "evidence": ["E25", "E26"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想要有效主张正义，必须以久历沉浮、见多识广和深刻而广泛的实务历练为前提，否则无益而有害。", "evidence": ["E27", "E28"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者希望年轻人先看清论述，省下时光去切实做事、尝试开创事业、近距离观察成败得失，绝不要在立起事业或经历几次失败前就拿起“正义”的“武器”。", "evidence": ["E29", "E30"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "牢牢记住：问应不应该之前，一定先问可不可行；正义观之间的竞争本质上就是可行性的竞争。", "evidence": ["E31", "E32"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正义并非最“当行”之事，而是最可行之事。", "evidence": ["E33"]}
   ],
   "argument_steps": [
    "先下定义：正义是能让人类走向最大繁荣的伦理观。",
    "主张该表述为终极，并规定不同意者所称“正义”只是同名异指。",
    "把各派分歧定位到“人类”“最大”“繁荣”的定义上，并列举分歧类型。",
    "把“人类最大繁荣”确立为共同前提，同时限定论述范围为当下可断言者。",
    "由定义内在推出首要方面：正义必须可行。",
    "追问何谓不可行，区分“正义本身”与“正义的理想”。",
    "承认“无先例但理论可行”属争议地带，交由天裁逻辑。",
    "对连理论可行都未达成者作出资格判断，并要求先理顺逻辑。",
    "指出可行性问题深不见底，历史由可行性的说服力裁决，但多数人信服非真理。",
    "收束为方法要求：以可行性论证正义，须以实务历练为前提。",
    "以对年轻人的劝告和标题句作结。"
   ],
   "concept_usage": [
    {"term": "正义", "meaning": "能让人类走向最大繁荣的伦理观；须可行，且可作为现实审判的法理基础。", "evidence": "P001", "ambiguity": "定义中的“人类”“最大”“繁荣”被作者留待未来争论，未在本文裁定。"},
    {"term": "正义的理想／正义本身", "meaning": "现阶段不可行者只能算理想；理想与正义本身是两个不一样的概念。", "evidence": "P014", "ambiguity": "判定“现阶段不可行”的主体与时段未明确。"},
    {"term": "人类的最大繁荣", "meaning": "被作者称为没有疑义可言的共同前提，也是判定不可行正义与之对立的基准。", "evidence": "P008", "ambiguity": "具体含义按作者自述仍是未来争论的对象。"},
    {"term": "可行／不可行", "meaning": "作者的核心判准，文中至少分出三档：现阶段不可行而将来可行、无先例而理论可行、连理论可行都未达成。", "evidence": "P011", "ambiguity": "各档之间如何判定与跨越，作者未给出操作标准。"},
    {"term": "天裁逻辑", "meaning": "无先例可依时各行其是、may the best win 的竞争性裁决方式。", "evidence": "P019", "ambiguity": "作者未说明该逻辑是否为其所认可的制度。"},
    {"term": "伦理的王座", "meaning": "历史上因令人信服地解决可行性问题而取得的支配地位。", "evidence": "P024", "ambiguity": "属比喻，未界定其标志。"},
    {"term": "当行", "meaning": "标题句中与“可行”相对的用语；作者主张正义是最可行之事而非最当行之事。", "evidence": "P036", "ambiguity": "“当行”一词在正文中未定义，仅见于末段标题句。"}
   ],
   "examples_and_targets": [
    "“关于正义的一切不同流派”（P002）：作者设定的对话与约束对象，未具名。",
    "分歧例举：是否把种族/出身/阶级/立场不同者算入人类；繁荣=赚钱或多子多孙；最大限度=经济规模、最广分布或永续存在（P004-P006）：作者列举的分歧类型。",
    "历史叙述：可行性主张者登上伦理王座直到被证伪；社会兴衰转折即各正义观证明自身可行性的过程（P024-P025）：作者的历史论断，无出处，待外部核查。",
    "批评对象：以指斥其他意识形态邪恶来主张自身正义者（P027-P028）；连理论可行都未达成却强烈主张者（P020）；过早拿起“正义”“武器”的年轻人（P031-P032）。均不具名。",
    "“小朋友们”（P031）：作者对青年读者的称呼，属修辞性称呼。"
   ],
   "conditions": [
    "“如果ta不同意这个表述（或其等效命题）”（P002）：作者定义之约束力的条件。",
    "“如果只是现阶段不可行，而将来可行”（P013）／“如果你自己也认同这个阶段不可行”（P014）：第一阶段限定。",
    "“如果只是没有先例证明其可行，而理论上可行”（P018）：第二阶段限定，作者明确称为争议。",
    "“如果谁真的足够令人信服的解决了可行性问题”（P024）／“直到它被事实证明其预告是错误的”（P024）：历史判断的条件与期限。",
    "“在自己还没有真正的立起一番事业或至少经历几次失败前”（P032）：对年轻人的劝告所设的时间条件。",
    "“我们只站在此时此刻，谈论此时此刻就可以断言的问题”（P009）：全篇的论述范围限定。"
   ],
   "rhetoric_and_tone": "定义—论证—劝诫的三段结构；断言性强（“终极的”“确定无疑”“完全错误的”）；以连续反问推进（“何谓不可行？”“算不算不可行？”）；用让步句收紧批评（“这不是说……而是指……”）；末段转为训诫口吻（“我希望小朋友们”“牢牢记住”），并以对句式的标题句收束；夹用英文短语 may the best win。",
   "unresolved_questions": [
    "定义中“人类”“最大”“繁荣”的具体含义，作者明确留给未来历史，本文未裁定（P003、P009）。",
    "“可行性”未给出可操作的判准，作者自称其深不见底（P023）。",
    "“天裁逻辑”是否为作者认可的制度安排，未说明（P019）。",
    "历史论断（可行性者登王座、兴衰转折即可行性证明过程）无出处，需外部核查（P024-P025）。",
    "“终极的”这一自我评价仅以“不同意即同名异指”支撑，作者未处理可能的反例。",
    "“当行”一词仅见于末段标题句（P036），正文未定义，其与“可行”的对举关系需人工核对。",
    "全篇未出现具名的思想流派、人物或著作，论证对象均为不具名泛指。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "正义是一种能让人类走向最大繁荣的伦理观。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这个定义表述是终极的，关于正义的一切不同流派都不能不同意这个表述。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "就可以断言ta所称其为“正义”的东西只是一种发音上、字形上的巧合。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "ta们之间一切的争议，都发生在对“人类”、“最大”、“繁荣”的定义上，而并不发生在这个表述本身上。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "的部分人不包括在配享受繁荣的人类范围内；", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "在于有的人认为“繁荣”是指赚钱、有的人认为指“多子多孙”、有的人则均不同意；", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "在于有的人认为“最大限度”是指经济规模、有的人认为指最广分布，有的人认为指永续存在，", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "这个“人类最大繁荣”的共识是没有疑义可言的共同前提。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "我们只站在此时此刻，谈论此时此刻就可以断言的问题。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "这问题的首要方面，就是正义必须是可行的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "因此从原理上就可以确定无疑的得知“不可行的理念不属于正义讨论的范畴”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "如果只是现阶段不可行，而将来可行，算不算不可行？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "那么它至少不可以被视作正义本身，而只能视为正义的理想。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "重复一遍——正义的理想，并非正义本身。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "正义是可以拿来作为现实审判的法理基础的，而正义的理想不可以。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "第二，如果只是没有先例证明其可行，而理论上可行，算不算不可行？", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "这里存在争议。存在争议，就靠的是各行其是、may the best win的天裁逻辑。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "这些暂时还没有被严肃讨论的资格，更不应该进入被大力推行的阶段。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "而是指它的主张者应该首先专注于将它的运行逻辑理顺、说通", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "换句话说，不要在主张可行性之前就主张正义性。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "可行性本身就是一个深不见底的问题，很难想象有任何伦理体系敢于宣称自己已经彻底的解决了可行性问题。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "它先于一切其它同期尚未完成这一成就的其他意识形态而登上伦理的王座——直到它被事实证明其预告是错误的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "人类社会的兴衰转折，本身就是一个又一个的正义观在各自的时代完成了“令人信服的表达了自己的可行性”的过程。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "“令足够多的人足够信服”并不是“终极真理”的可靠替代品。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P027", "quote": "主张其正义，必须通过主张其可行来进行，而不是通过主张与其不符的其他意识形态如何邪恶来进行。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P028", "quote": "后者是无效的行为，并不会真的增加你信念的力量", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P029", "quote": "必须以久历沉浮、见多识广为前提，必须以深刻而广泛的实务历练为前提。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P030", "quote": "否则是无益而有害的。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P031", "quote": "学会省下自己宝贵的时光首先去切实做事、去尝试开创事业、去近距离的观察成败得失。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P032", "quote": "而绝不要在自己还没有真正的立起一番事业或至少经历几次失败前，就拿起“正义”的“武器”", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P034", "quote": "牢牢记住——问应不应该之前，一定先问可不可行。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P035", "quote": "正义观之间的竞争，本质上就是可行性的竞争。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P036", "quote": "正义并非最“当行”之事，而是最可行之事。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "政治哲学", "历史哲学", "方法论"],
   "issue_candidates": ["正义的定义", "可行性与正义性的关系", "正义的理想与正义本身之别", "意识形态竞争", "青年的行动次序"],
   "text_function_candidates": ["答疑", "论辩", "定义与概念澄清", "训诫与劝告"],
   "object_candidates": ["提问者", "各正义流派（不具名）", "年轻人/“小朋友们”", "历史中的意识形态"],
   "working_keywords": ["正义", "最大繁荣", "可行性", "正义的理想", "天裁逻辑", "may the best win", "伦理的王座", "当行"]
  },
  "notes": "无图片节点，正文完整（35 段正文 + 1 段 heading，共 36 段）；P036 为 heading 节点，内容为结论句。全篇未出现具名流派或人物，论证对象为泛指，已在未决问题登记。历史论断无出处，待外部核查，本记录不作裁决。"
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
