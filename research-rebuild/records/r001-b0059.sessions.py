# -*- coding: utf-8 -*-
"""批次 r001-b0059 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0059.sessions.py            # 写 out/r001-b0059.out.jsonl
  python3 records/r001-b0059.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0059"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0059.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "96b7c75d": {
  "analysis": {
   "question_context": "提问字段问“如何修正傲慢？”（Q001，属提问者）。作者没有按“修正”路径给出操作步骤，而是先界定“什么叫做傲慢”，再把它与“显得傲慢”“被人指责傲慢”区分开，最后收窄到“对客观世界的傲慢”并给出不可证伪命题的边界。提问者的立场与作者立场不同，作者对“被指责傲慢”这一情境本身持反讽态度。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以设问开场，给出傲慢的定义：对可证伪的问题只有三分证据却有十分把握。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "按证据与结论的比例区分“不算傲慢”“谨慎”“稳健”，并强调刻度只对你自己而言，无须把证据全告诉别人来证明自己不傲慢。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "指出很多人的真问题不是傲慢，而是生怕别人觉得自己傲慢；因缺乏对自身证据与结论刻度的觉察，反而格外在意别人说自己傲慢。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "讽刺由此产生的“不显得傲慢”的技术：或以词谦意卑求高抬贵手，或狗斗不休逼对方认错，并称其为怯懦者无聊的自欺仪式。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "以“老鸟狮子搏兔”作对照：十倍冗余资源、效果对折又对折、三条独立路线论证；其结论看似惊世骇俗实则极端保守，菜鸟的质疑不能动摇它，那只是显得傲慢。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018"], "summary": "限定：这与偏执和讳疾忌医有别，区别在于结论不会因被指责傲慢而动摇；无数据与逻辑的指控更不足虑。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "让步并加条件：即使结论最后被证明错了，只要你清楚自己只是在赌最有胜率的赌注，在绝对逻辑意义上就无法是傲慢的，只存在“是否让人觉得傲慢”的问题。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024"], "summary": "归结：本质上只有一种傲慢，即误以为自己所信的结论是天经地义的客观事实；这本质上是对客观世界的傲慢，只要不是对客观世界傲慢，就从根上没有傲慢问题。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "理由：你只能做出目前这种质量的判断，不能仅因无新证据、无新论证的“傲慢”指责而改变立场；围绕别人情绪安排决定行不通，道德上也不可以——那等于合谋一场被刻意纵容的绑架。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P030", "P031", "P032"], "summary": "限定：指责对方傲慢而只接受其屈服，是唯有以性命相托的爱人（为子女一切后果买单的父母、以死相救的爱人）才有的特权。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P033", "P034", "P035", "P036"], "summary": "行动要求：以傲慢责备人要先想清对方“放弃傲慢”的后果；若对方仅因指责而改决策，亏损与受罪你必要承担赔偿，否则那份痛恨不会轻易善了。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P037", "P038", "P039", "P040"], "summary": "以短句与反问训诫：若不是性命相托，就如同作死、愚不可及；有事说事、有错说错，“人听了你的，栽了，你养啊？？”。", "role": "other"},
    {"unit_id": "U013", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046"], "summary": "自述立场：对无论据无论证的傲慢批判保持无视，是为了不让对方担上“让我人生不幸”的罪，因此一意孤行，并原谅对方以此说自己傲慢。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P047", "P048"], "summary": "回到定义：前面留了一个口子——“可证伪”；只有对可证伪的事物才存在被定性为傲慢的可能。", "role": "definition"},
    {"unit_id": "U015", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053"], "summary": "边界与反照：对不可证伪命题的坚定立场除非有碍客观可持续性，否则免于人的判断，属神裁管辖；坚持此类命题是天然自由；而明知无证伪通路却断言别人错，本身才是无可质疑的傲慢。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "傲慢指对有可证伪性的问题只有三分证据，却有十分把握。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "证据与结论相称即不算傲慢；五分证据下四分结论是谨慎，十分证据下一分结论是稳健。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "证据与结论的刻度只对你自己而言，你不需要把自己的证据全部告诉别人来证明自己不傲慢。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人真正的问题不是傲慢与否，而是生怕别人觉得自己傲慢。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "缺乏对自身证据与结论刻度的觉察能力时，人会长期处在自己看不出问题的证据与结论之中，因而特别在意别人说自己傲慢。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不显得傲慢”的技术与词谦意卑或狗斗不休，与是否傲慢无关，只是怯懦者无聊的自欺仪式。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老鸟以十倍冗余资源、效果反复对折、三条独立路线论证作准备，其结论极端保守，菜鸟的质疑不能动摇其判断。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被指责傲慢而不动摇，只是显得傲慢，并不是真的傲慢；这与偏执和讳疾忌医有区别。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "即使结论最后错了，只要你清楚自己只是在赌最有胜率的赌注，就仍然不能被称为傲慢。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本质上人只有一种傲慢，即误以为自己相信的结论是天经地义的客观事实，而不只是基于有限证据与不足智力下的赌注；这本质上是对客观世界的傲慢。", "evidence": ["E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要不是对客观世界傲慢，就从根上没有傲慢的问题。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人不能仅因一个没有提出新证据、新论证、无错误可指的人大声疾呼“傲慢”而改变结论和立场。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不能围绕别人的情绪安排决定，此路根本行不通；可以为对方痛苦改变语气、实施计划与优先级，但不能因此改变观点和立场。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从道德上也不可以因指责而改变立场，因为这等于与人合谋一场被刻意纵容的绑架。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "指责对方傲慢而只接受其屈服为结果，是唯有以性命相托的爱人才有的特权。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若对方仅因被指责傲慢而改变决策，由此而亏的本与受的罪，指责者必要承担、赔偿。", "evidence": ["E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有证据有论证就只摆论据和论证，不要多说傲慢；无凭无据指责人傲慢却不承担后果，如同作死，愚不可及。", "evidence": ["E23", "E24"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无视无据的傲慢批判，是为了不让对方担上“让我人生不幸”的罪。", "evidence": ["E25"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "定义中的“可证伪”是一个限定的口子：只有对可证伪的事物，才存在被定性为傲慢的可能。", "evidence": ["E26", "E27"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "对不具备可证伪性的命题采取坚定立场，除非影响到客观的可持续性，否则绝对免于人的判断；是否有碍可持续性靠上帝对人命运的实际揭示，不靠数学推断。", "evidence": ["E28", "E29"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对不可证伪命题的坚持与对命运的裁判，属神裁管辖，非人类所能置喙；这是一种天然的自由。", "evidence": ["E30", "E31"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在自己明确承认没有任何逻辑上可行的证伪通路的前提下断言别人是错的，本身是一种无可质疑的傲慢。", "evidence": ["E32"]},
    {"claim_id": "C023", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的一方要求：仅凭“你傲慢”的指责，被指责者就应改变结论与立场。（作者转述并反驳的指责者主张）", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "设问“什么叫做傲慢”，给出定义：可证伪问题上三分证据却十分把握。",
    "按证据—结论比例给出不算傲慢、谨慎、稳健三种刻度，并把刻度限定为自我评估。",
    "转折：多数人的真问题是怕被人觉得傲慢，并描述缺乏刻度觉察能力者的状态与自欺仪式。",
    "以“老鸟狮子搏兔”作正面对照，说明高把握可以来自冗余与多路论证，因而只是显得傲慢。",
    "限定与偏执、讳疾忌医的区别：结论不因被指责而动摇。",
    "让步：结论也可能错；再加条件——自知只是赌胜率最高的赌注，即不构成傲慢。",
    "归结唯一实质傲慢：把自认结论当成天经地义的客观事实，即对客观世界傲慢。",
    "给出实践理由与道德理由：不能为他人情绪改变立场，否则是合谋绑架。",
    "限定特权：只有以性命相托的爱人才有资格要求对方屈服。",
    "行动要求：指责者须预备承担对方改变决策的后果与赔偿。",
    "自述立场与收束：无视无据指责，以免对方担罪。",
    "回到定义补边界：可证伪是口子；不可证伪命题免于人的判断，属神裁；反向断言别错才是真正的傲慢。"
   ],
   "concept_usage": [
    {"term": "傲慢", "meaning": "本文中先定义为“对有可证伪性的问题只有三分证据，却有十分把握”；后收窄为唯一一种实质傲慢——误以为自己所信的结论是天经地义的客观事实。", "evidence": "P002", "ambiguity": "前后两处定义范围不同：前者是证据与把握不相称，后者是对客观世界的态度；作者用“本质上”连接，未说明二者是否等价。"},
    {"term": "可证伪", "meaning": "判定是否可能存在傲慢的边界条件；只有对可证伪的事物，才存在被定性为傲慢的可能。", "evidence": "P047", "ambiguity": "由谁、按什么标准判定一个命题是否可证伪，本文未说明。"},
    {"term": "证据／结论的刻度", "meaning": "对自身掌握几分证据、下了几分结论的觉察能力，用于自我评估而非向他人证明。", "evidence": "P004", "ambiguity": "“几分”如何计量未说明。"},
    {"term": "赌注／胜率", "meaning": "把一切来自自己的结论视为最有胜率的赌注而非最终真理。", "evidence": "P020", "ambiguity": "无。"},
    {"term": "对客观世界的傲慢", "meaning": "把自认结论当成天经地义的客观事实，是本文认定的唯一实质傲慢。", "evidence": "P023", "ambiguity": "“客观世界”的界定未展开。"},
    {"term": "神裁", "meaning": "对不可证伪命题的最终裁判权，靠上帝对人命运的实际揭示，非人类所能置喙。", "evidence": "P050", "ambiguity": "作者以神裁为不可证伪领域划界，但未说明人如何识别这种揭示。"},
    {"term": "老鸟／菜鸟", "meaning": "以准备方式（冗余资源、多路论证）与反应（质疑、以傲慢指责）区分的两类人。", "evidence": "P013", "ambiguity": "未给出区分标准，属修辞性对照。"},
    {"term": "讳疾忌医", "meaning": "作为与“不动摇”相对照的贬义状态，作者仅用于划界，未展开定义。", "evidence": "P016", "ambiguity": "定义未展开。"}
   ],
   "examples_and_targets": [
    "老鸟“狮子搏兔”：十倍冗余资源、效果对折又对折、三条截然不同路线论证——作者例证（正面对照）。",
    "菜鸟以“你怎么这么傲慢”安抚惊恐、倾泻不满——作者例证（被描述为反应方）。",
    "保安见穷人偷东西，以“仁慈和同情”为名任由得手，日后拿录像带要挟——作者类比，用于说明纵容式妥协是绑架。",
    "为子女一切后果买单的父母、为对方一切后果不惜以死相救的爱人——作者用以界定“要求屈服”的特权范围。",
    "“小朋友们”——作者训诫对象的称呼。",
    "“人类几千年的历史／自然规律／数学／逻辑没有动摇”——作者修辞性列举，非外部事实核查。"
   ],
   "conditions": [
    "适用范围限定于“有可证伪性的问题”；不可证伪命题另按 P049 处理。",
    "证据—结论刻度的评估前提是“这是对你自己而言”。",
    "即使结论错，仍需满足“你清楚知道即使有如此大把握，你仍然只是在赌这是正确的”这一条件，才不被称为傲慢。",
    "例外条件：“除非影响到客观的可持续性”。",
    "特权条件：只有以性命相托的爱人才有资格指责傲慢并只接受屈服。",
    "后果条件区分两种情形：对方因新证据新论证而采纳，责任在对方；对方仅因被指责傲慢而改变决策，指责者须承担并赔偿。",
    "若指责者不打算承担赔偿，且对方够得着他，则痛恨不会轻易善了。",
    "道德禁令的边界：可改变语气、实施计划、优先级，不可改变观点与立场。"
   ],
   "rhetoric_and_tone": "训诫与反讽为主：第二人称“你”直接施教，短句与破折号推进，大量反问（“不弄个水落石出，怎么睡得着觉？”“人听了你的，栽了，你养啊？？”）与感叹堆叠；自称“老纸白衣飘飘”带调侃与江湖气；单句成段的“愚不可及”以标题节点充当判决；用“小朋友们”称呼训诫对象，语气居高而刻意；对“显得傲慢”的技术使用“自欺仪式”“狗斗不休”等贬抑措辞。整体是概念澄清＋道德训诫＋立场自陈的混合文体，结构上先定义、后区分、末段回到定义补边界。",
   "unresolved_questions": [
    "提问者问“如何修正傲慢”，作者未正面给出修正路径，也未明说傲慢是否可修正；“修正”与作者的“从根上没有傲慢问题”是否相容，未说明。",
    "可证伪性的判定主体与判定标准未说明（P047-P048）。",
    "“上帝对人命运的实际揭示”如何被识别、由谁确认，本文未说明（P049-P050）。",
    "对客观世界的傲慢与证据—结论不相称的傲慢是否同一，作者未明说。",
    "“客观的可持续性”指什么（个人、社会还是人类）未界定。",
    "“老纸”一词疑为“老子”的口语戏写，原文如此，未作改动，可能影响语气解读。",
    "文末对不可证伪命题的结论（P053）与开头定义（P002）之间是否构成自我指涉，本文未讨论。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "傲慢就是对有可证伪性的问题只有三分证据，却有十分把握。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "有五分证据，下四分结论，这个可称为谨慎。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "但是你要看清楚，这是对你自己而言。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "很多人真正的问题根本不是傲慢不傲慢，是生怕别人觉得ta傲慢。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "ta几乎不会考虑自己有几分证据、又下了几分结论", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "因为“有人说我傲慢”对忐忑中的自己真的是一个很大的不祥之兆。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "只是不能承受自己的自由和独立的怯懦者无聊的自欺仪式。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "老鸟准备了十倍冗余的资源", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "老鸟做了三条截然不同路线的论证，都殊途同归", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "那只是显得傲慢而已，并没有什么真的傲慢。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "这跟偏执和讳疾忌医是有区别的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "那就是你清楚的知道即使你有如此大的把握，你仍然只是在赌这是正确的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "你都知道来自你自己的一切结论都只是最有胜率的赌注，而不是最终真理", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "本质上人只有一种傲慢，就是误以为自己所相信的某种结论是天经地义的客观事实", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "这本质上是对客观世界的傲慢。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "只要你不是对客观世界傲慢，你就从根上没有傲慢的问题。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "你只能做到你目前做到的这种质量的判断", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "你不能围绕着别人的情绪安排你的决定，这根本行不通", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "你可以为了对方的痛苦改变语气、改变实施计划、改变优先级，但是你不能因此改变观点和立场", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P028", "quote": "因为这是在与人合谋实施一场被刻意纵容的绑架。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P030", "quote": "指责对方傲慢而只接受对方的屈服为结果，是唯有以性命相托的爱人才有的特权。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P033", "quote": "如果对方仅仅是因为你指责傲慢而改变决策，那么由此而亏的本你必要承担、受的罪你必要赔偿。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P035", "quote": "有证据、有论证，你就应该只摆论据和论证，不要多说什么傲慢。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "愚不可及。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P042", "quote": "因为我不要让你担上“让我人生不幸”的罪。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P047", "quote": "你应该看到前面那个定义里留了一个口子——“可证伪”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P048", "quote": "只有对可证伪的事物，才存在被定性为傲慢的可能。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P049", "quote": "对于不具备可证伪性的命题采取坚定立场，除非影响到客观的可持续性，否则是绝对免于人的判断的", "relation": "qualifies"},
    {"key": "E29", "paragraph_id": "P049", "quote": "而是靠上帝对人命运的实际揭示。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P050", "quote": "这是神裁的管辖范围，非人类所能置喙。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P051", "quote": "这是一种天然的自由。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P053", "quote": "这本身是一种无可质疑的傲慢。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认识论／证据与信念", "伦理学／人际指责与责任", "方法论／判断校准", "宗教与神裁话题"],
   "issue_candidates": ["傲慢的定义与边界", "证据与结论的相称性", "被指责傲慢时的应对", "为他人情绪改变立场的道德性", "可证伪性与信仰领域的分界"],
   "text_function_candidates": ["答疑", "概念澄清", "论辩", "道德训诫", "立场自陈"],
   "object_candidates": ["提问者（匿名）", "老鸟／菜鸟", "指责者（泛称）", "父母", "以性命相托的爱人", "上帝（神裁）"],
   "working_keywords": ["傲慢", "可证伪", "三分证据", "十分把握", "谨慎", "稳健", "冗余", "老鸟", "狮子搏兔", "讳疾忌医", "绑架", "神裁", "赌注", "胜率"]
  },
  "notes": "正文 53 段（P038 为 heading 节点）。question 仅为提问者语境，未进入正文段落，故不作证据引用。作者未按“如何修正傲慢”作答，而是在定义与边界上重述问题；提问者立场未被归给作者。本批无图片。P049 引入“上帝对人命运的实际揭示”“神裁”，属作者主张而非引用宗教文本，已按作者语气记录（含“除非”条件）。"
 },
 "b6da422b": {
  "analysis": {
   "question_context": "提问字段问“如何迅速且合理地反驳别人？”（Q001，属提问者）。作者的回应是把这个提问本身判为伪问题：先否认“反驳权”是天然权利，主张它只能是被授予的特权，再论证只应把反驳权授予爱自己的人，最后指出出于真诚关心与爱的话语从一开始就不会是“反驳”姿态。作者并未提供反驳技巧；提问者的诉求与作者立场相反。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "指出多数人假定人人处于准备迎接反驳的状态、反驳权是天然权利，并直接判为错：反驳权不是基本人权，而是被授予的特权。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "前提：自由的首要表现形式是坚持己见；己见必是偏见；任何自由都必定以某个时刻停止接受反对意见为基本形式。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "以连续反问追问：我可能是错的，就要继续听下去？听到什么时候为止？等到所有人提完意见都满意了再决定？", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "结论性理由：无限延迟的自由即被废除、被剥夺的自由；自授天然反驳权并攻击拒绝者，实质损害他人自由的实现。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013"], "summary": "转述反驳权主张者以“信息茧房”恐吓，并判其大错特错。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "两点理由：人人获得反驳权在现实操作上不可行；既然想反驳者众多，就可以优中选优，只把反驳权赋予其中一部分人——这里就是魔鬼所在。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "攻其前提：对方以“只与爱自己的人对话必陷信息茧房”为主武器，其根子是误以为爱必定意味着附和；作者追问这一逻辑前提从何而来。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023"], "summary": "反证：非出于爱的反驳掺杂大量自私自利甚至伪造、欺骗、霸凌的罪；为自身可能获益而纵容甚至唆使他人犯无意识的罪，本身不道德。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P024", "P025", "P026"], "summary": "断言实践与效率上只有一条可选之路——只授予爱自己的人反驳权；爱的含义可以慢慢研究，但该原则不能改变，否则思想矿藏品位下降且终究逃不掉“不接受反驳”的罪名。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031"], "summary": "以沙中有金作类比反驳“泥沙俱下”式不筛选：你只有一条命，不筛选是实质意义上的半自杀；只能提高选择有效性，不能放弃、甚至不能放松筛选。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037"], "summary": "限定：有爱的人造成回音壁是政策掌握与对爱的认识问题，不是筛选的问题；坚持筛选别无选择，只能不断想清楚什么是爱。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042"], "summary": "自引并补下半句：抬高别人说服自己的成本是最愚蠢的事，但前提是对方爱你；只有你相信爱你的人享有无限制低的说服成本；对无爱的人连门都要关上。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050"], "summary": "收束到本题奥秘：出于真诚关心和爱的话语从一开始就不是反驳姿态，不认可会转化为需要对方解答的疑惑，因此“反驳”没有必要，这个问题成为伪问题。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "把“任何人都在准备迎接反驳”当作前提、把反驳权当作毋庸置疑的天然权利，是错的。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反驳权不是基本人权，而是一种被授予的特权。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的自由的首要表现形式是坚持己见；己见必是偏见；人有任何自由都必定以某个时刻停止接受反对意见为基本形式。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无限延迟的自由即被废除、被剥夺的自由。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人授予自己天然反驳权、并为反驳权被拒而攻击拒绝者，实质损害他人自由的实现。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "并非人人都应获得反驳权；仅从现实操作上就不可行，你看不过来也应付不过来。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然想反驳你的人众多，就可以优中选优，把反驳权只赋予其中一部分人。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“爱必定意味着附和”这一逻辑前提是错的；“提出反对、疑问就是不爱”显然是愚蠢的。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "非出于爱的反驳会掺杂大量自私自利，甚至伪造、欺骗、霸凌的罪。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为了自己可能的获益而纵容甚至唆使人们犯下无意识的罪，本身就是不道德的。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实践与效率上只有一条可选的路：只授予爱自己的人反驳权。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“只授予爱自己的人反驳权”这一原则不能改变，否则思想矿藏品位下降、大量无效挖掘，且最终仍会落得“不接受别人反驳”的罪名。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你只有一条命，不加筛选是一种实质意义上的半自杀，必须有所筛选。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "只能选择如何提高筛选的有效性（不断深挖爱的含义），不能放弃筛选本身，甚至连放松筛选都不行。", "evidence": ["E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只筛选有爱的人授予反驳权而搞出回音壁，不是筛选的问题，而是对爱的认识问题。", "evidence": ["E19"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "只有你相信爱你的人才享有无限低的说服成本待遇；不论是否认同，最后你必定还是会无法抗拒地走到这条路线。", "evidence": ["E20", "E21"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对无爱的人——那些反驳只是为了让自己安心、让自己荣耀的人——连门都要关上，没有门槛可言。", "evidence": ["E22"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出于对对方的真诚关心和爱时，话语从一开始就不会是“反驳”的姿态，因为不是要争胜利与屈服；不认可会转化为需要对方解答的疑惑。", "evidence": ["E23", "E24"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若如此，你面前不会出现“反驳”的必要，这个提问会成为伪问题，根本不需要得到回答。", "evidence": ["E25", "E26"]},
    {"claim_id": "C020", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的立场：任何人都处在准备迎接反驳的状态，反驳权是毋庸置疑的天然权利。（作者所否定的通行假定）", "evidence": ["E1"]},
    {"claim_id": "C021", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的论证链：爱必定意味着不反对→只让爱自己的人参与讨论就拿不到反对→必定陷入信息茧房→所以人必须允许和拥抱一切理由的反驳。（作者转述对方主张后逐环否定其前提）", "evidence": ["E27", "E28"]}
   ],
   "argument_steps": [
    "树靶：通行假定人人在准备迎接反驳、反驳权是天然权利，作者判为错。",
    "替换命题：反驳权不是基本人权，而是被授予的特权。",
    "建立前提：自由的首要形式是坚持己见，己见必是偏见，故自由必以某时刻停止接受反对为形式。",
    "反问推进：听到什么时候为止？等到所有人满意才决定？",
    "推出结论：无限延迟的自由即被剥夺的自由；自授反驳权损害他人自由。",
    "转述对方武器（信息茧房恐吓）并判错。",
    "给出两条理由：操作上不可行；可以优中选优只授予一部分人。",
    "攻击对方前提：爱不等于附和，追问该前提从何而来。",
    "反证：非爱之反驳掺杂自私与罪，纵容他人犯罪不道德。",
    "断言唯一可行之路：只授予爱自己的人反驳权，原则不可改变。",
    "用沙中金类比反驳不筛选，以“只有一条命”收束为必须筛选。",
    "限定：回音壁是政策掌握与对爱的认识问题，非筛选问题。",
    "自引并补下半句：低说服成本只给爱你的人；对无爱的人关门。",
    "收束：出于爱的话语不是反驳姿态，问题成为伪问题，无须回答。"
   ],
   "concept_usage": [
    {"term": "反驳权", "meaning": "本文核心：不是基本人权，而是一种被授予的特权，可按对象筛选授予。", "evidence": "P003", "ambiguity": "授予者与被授予者的关系只在“你—对方”框架内讨论，未涉及公共制度层面的权利。"},
    {"term": "己见", "meaning": "被界定为一种偏见、在绝对意义上永远有错可言的偏见，却是自由的首要表现形式。", "evidence": "P005", "ambiguity": "“绝对意义上永远有错可言”与“必定是偏见”的论证未展开。"},
    {"term": "信息茧房／玫瑰色的泡泡", "meaning": "作者转述对手的恐吓用语：只与爱自己的人对话就会困于自我构造的泡泡。", "evidence": "P012", "ambiguity": "作者未注明该概念来源；文中以转述方式使用，未承认其成立。"},
    {"term": "回音壁", "meaning": "只筛选出有爱的人授予反驳权后可能出现的状态；作者归因于对爱的认识问题而非筛选本身。", "evidence": "P035", "ambiguity": "回音壁与信息茧房是否同义，本文未说明。"},
    {"term": "爱", "meaning": "筛选反驳权对象的判据；作者明确说其含义要慢慢研究，且不等于附和。", "evidence": "P025", "ambiguity": "全文未给定义，作者自称“这个你慢慢研究”，是本文最大的开放性术语。"},
    {"term": "说服成本", "meaning": "作者自引的说法：抬高别人说服自己的成本是最愚蠢的事；下半句限定前提是对方爱你。", "evidence": "P038", "ambiguity": "“我曾经说过”为作者自引旧说，未给出出处。"},
    {"term": "思想矿藏／品位／泥沙俱下", "meaning": "把接受他人意见比作开采矿藏，筛选即控制品位；沙中有金不构成不筛选的理由。", "evidence": "P026", "ambiguity": "比喻性用法，无操作化标准。"},
    {"term": "伪问题", "meaning": "出于爱的话语不构成反驳，故“如何反驳”这一问题无须回答。", "evidence": "P049", "ambiguity": "未说明在什么范围内该问题仍成立。"}
   ],
   "examples_and_targets": [
    "以“信息茧房”“玫瑰色的泡泡”恐吓主张无限反驳权的人——作者的反驳对象（P012、P018）。",
    "“ta们最后不是一样走上拉黑删评‘不接受反驳’之路，就是自己躲起来只跟极少数的朋友说话”——作者例证，用来说明不筛选者最终也实行不下去（P033）。",
    "地上随便抓把沙子里面都有金子、五六个金原子——作者类比，反驳“被拒矿石里有金子”式的不筛选理由（P028）。",
    "“半自杀”——作者比喻，形容不加筛选（P029）。",
    "“你屁股完全歪了”“作者就是个xx贼”——作者举出的失当表达样例，用以说明不满情绪倾泻（P047）。",
    "“我曾经说过，世界上最愚蠢的事情就是抬高别人说服自己的成本”——作者自引旧说（P038）。"
   ],
   "conditions": [
    "全篇限定在“你”与潜在反驳者的人际讨论情境，未涉及制度性言论权利。",
    "被反驳方的条件句：若一个人只与爱自己的人对话，必定落入信息茧房（作者转述并否定其前提）。",
    "原则不可改变的条件后果：否则思想矿藏品位下降、大量无效挖掘，且最终仍落“不接受反驳”罪名。",
    "说服成本论断的前提：“前提是这个人是一个爱你的人”。",
    "对无爱者的处置是无条件的关门（“没有门槛可言”）。",
    "预言性断言：“不论你是否认同这说法，最后你必定还是会无法抗拒的走到这条路线上来”。",
    "收束部分的条件：“如果你是出于对对方的真诚的关心和爱”。"
   ],
   "rhetoric_and_tone": "论辩与训诫混合，语气强硬直接：以“这是错的”“其实ta们大错特错”“这从根上就错了”作判决式断言；大量反问施压（“听到什么时候为止？”“这就是泥沙俱下的理由吗？”“向对方倾泻这些情绪是想达到什么效果？”）；使用编号列举“1）2）”；以“这里就是魔鬼所在——”“说到这个点上，我们可以谈论本题的奥秘了——”作结构路标；用第二人称“你”“ta们”划分阵营，比喻系统密集（矿藏与品位、回音壁、泥沙俱下、半自杀、门槛）；一处自引旧说增强权威感。",
   "unresolved_questions": [
    "“爱”的含义作者明确未定义，只让读者慢慢研究（P025）；判定谁爱你、由谁判定，本文未说明。",
    "提问“如何迅速且合理地反驳别人”被作者判为伪问题，故本文未给任何反驳技巧；该判定适用的范围未说明。",
    "“回音壁”与“信息茧房”的关系、以及“政策掌握问题”的可操作标准未说明。",
    "“不接受别人反驳”的罪名由谁施加、在什么场合成立，本文未说明。",
    "“信息茧房”概念来源未注明，属转述（P012、P018）。",
    "作者自引“我曾经说过”的原文与出处未提供，无法核对。",
    "P020 的箭头式链条是作者对对方论证的转述与重构，非原文引用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人总在假定任何人都是处在“准备迎接反驳”状态", "relation": "contradicts"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这是错的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "反驳权不是基本人权，而是一种被授予的特权。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "人的自由的首要表现形式，就是坚持己见。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "“己见”必定是一种偏见、一种绝对意义上永远有错可言的偏见。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "人要有任何自由，都必定以在某个时刻停止接受反对意见为基本形式。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "无限延迟的自由即被废除的自由，即被剥夺的自由。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "就是在实质上损害他人自由的实现。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "显然不是人人都应该获得反驳权", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "你可以优中选优，把反驳权仅仅赋予其中一部分人。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "谁说“爱一定意味着不反对、只附和”？", "relation": "contradicts"},
    {"key": "E12", "paragraph_id": "P025", "quote": "“提出反对、疑问就是不爱”显然是愚蠢的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "不是出于爱，人的“反驳”里会掺杂大量的自私自利，甚至伪造、欺骗、霸凌的罪。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "为了自己可能的获益而纵容甚至唆使人们犯下无意识的罪，这本身就是不道德的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "人面前其实只有一条在实践上、效率上可选的路——就是只授予爱自己的人反驳权。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "但是“只授予爱自己的人反驳权”这个原则你不能改变。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P029", "quote": "问题是你只有一条命。不加筛选，就是一种实质意义上的半自杀，你必须有所筛选。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P031", "quote": "甚至连放松筛选都不行。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P035", "quote": "这不是筛选的问题，而是对爱的认识问题。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P040", "quote": "享有无限低的说服成本待遇的，只有你相信爱你的人", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P040", "quote": "不论你是否认同这说法，最后你必定还是会无法抗拒的走到这条路线上来。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P042", "quote": "连门都要关上，没有门槛可言。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P044", "quote": "那么你的话语从一开始姿态就不会是“反驳”的。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P048", "quote": "而是会自然而然的转化为一个【需要对方给予解答的疑惑】。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P049", "quote": "从始至终，你面前都不会出现“反驳”的必要。于是这个问题会成为伪问题。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P050", "quote": "它根本不需要得到回答。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P018", "quote": "如果一个人只与爱自己的人对话，必定会落入信息茧房", "relation": "contradicts"},
    {"key": "E28", "paragraph_id": "P020", "quote": "人必须允许和拥抱一切理由的反驳来保证自己的客观和进步。", "relation": "contradicts"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／自由与权利", "社会认识论／信息环境", "人际伦理与爱", "言论与讨论规范"],
   "issue_candidates": ["反驳权是否为天然权利", "信息茧房论证的成立与否", "筛选意见来源与回音壁", "说服成本与亲密关系", "爱与反对是否相容"],
   "text_function_candidates": ["答疑（实为改写提问为伪问题）", "论辩", "训诫", "概念澄清"],
   "object_candidates": ["提问者（匿名）", "主张无限反驳权的人（泛称）", "爱你的人", "无爱的人", "拉黑删评者（举例）"],
   "working_keywords": ["反驳权", "基本人权", "特权", "己见", "偏见", "信息茧房", "玫瑰色的泡泡", "回音壁", "筛选", "思想矿藏", "泥沙俱下", "说服成本", "伪问题"]
  },
  "notes": "正文 50 段，无图片；无 provenance/superseded。question（如何迅速且合理地反驳别人）属提问者，作者未按其诉求作答，而是将其判为伪问题，未归给作者。P018、P020 是作者转述对手（主张无限反驳权者）的论证，已按 opponent_view 记录，未写成作者主张。P038 为作者自引旧说“我曾经说过”，标为 author_explicit 并在 concept_usage 注记出处缺失。"
 },
 "9d341350": {
  "analysis": {
   "question_context": "提问字段问“中国的低端制造业产业转移方向是向中西部地区还是东南亚地区？”（Q001，属提问者，其前提是低端产业会持续存在并发生转移）。作者不接受这一前提框架，先指出人们隐性假设低端产业像不会蒸发的水银、只随成本流动，再把“真正的问题”改写为该意义上的低端产业是否仍然存在，最后回答：可简单转移的传统低端产业基本消失，故无所谓转移方向。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "点出隐性假设（低端产业长期存在、哪里成本低就流向哪里），并把真问题改写为该意义上的低端产业是否仍然存在，甚至是否正在消失。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "以手工制铁、煮海熬盐为例说明古老劳动密集工艺被整体淘汰；低端产业仍存在但下限迅速上移，已远离未受教育的文盲人群，劳动密集型产业本身在萎缩。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "给出“低端制造业的奥秘”即用人力柔性生产线对抗欠柔性自动化生产线，并列出三条消解因素：自动化产线成本飞速下降、全产业链广域分工、柔性化设计经验提高；重训员工未必比调线更便宜更快。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "以ABB双臂工业机器人为例：用手引导一遍即可教会调整抓取路径，并请读者比较机器人升级调整与教人哪个更快。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020", "P021"], "summary": "收束为“低端产业”正在历史性消失：二十年前小学辍学可找到低端产业工作，如今这样的岗位恐怕也少有。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027"], "summary": "作者表示不看好“低端产业转移”与“产值飞涨”；能靠初中以下文化程度人口承接的低端产业时代恐怕已过；老低端产业链已升级为品类齐全的新低端产业，实质是重新定义低端产业。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "外流产业A类：更原始、可靠半文盲运转的上一代低端产业；质量、产量、成本均无明显优势，是冢中枯骨；其利润核心实为环境管制低标准与剩余碳排放指标、逃掉的税。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040"], "summary": "外流产业B类：新低端产业的核心经验技术多与中国相关，很多是中国产业链附庸；转向越南印度的产业拿不到中国无意放弃的工艺流程，离开中国半成品与需求支撑会立刻遭遇困难，不会真正替代中国。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P041", "P042", "P043", "P044"], "summary": "结论：这些产业缺乏对欠教育劳动力的吸纳能力；中国真正的危机是产值上升而产业链岗位下降；故原低端产业无法向中西部转移，因为它们基本消失，没得可移。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者指出人们往往隐性假设低端产业像不会蒸发的水银，长期存在，只是哪里成本低就流向哪里。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者把真问题设定为：20世纪末到21世纪初意义上的“低端产业”本身是否仍然存在，甚至是否正在消失。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多古老的、能由劳动密集来暴力破解的工艺正在整个被淘汰。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "低端产业仍然存在，但其下限正在悄无声息地上移、迅速远离未受教育的文盲人群。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "依赖低端劳动力的劳动密集型产业本身正在萎缩。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“低端制造业的奥秘”，是用人力组成柔性生产线的方案，对抗设计安装调试自动化的欠柔性生产线方案。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "自动化生产线的成本正随现代工业经验积累飞速下降，未必一定比召集、供养和管理数万员工更慢更贵。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全产业链的广域分工在很大程度上系统消解了单生产线不够柔性的问题，且柔性化设计的经验正在飞速提高。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "重新训练教育程度不高的员工适应新工艺，并不见得一定比调整生产线更便宜和更快。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以ABB双臂工业机器人为例，柔性化前沿已能一遍教会，机器人升级调整的速度被用来与教会一个人作比较。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“低端产业”本身正在历史性的消失。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不看好所谓的“低端产业转移”和所谓的“产值飞涨”。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "能靠初中以下文化程度人口承接的低端产业大规模存在的历史时期恐怕已经过去。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "靠四处转移维持生存的低端产业，其产品正在迅速失去市场。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "占据“低端产业”生态位的新一代产业形态虽未到无人生产线程度，但已大大去劳动密集化。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不是不向西部转移，而是可以简单转移的传统低端产业已经死得差不多，没什么可转移的。", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "东南沿海老低端产业链已升级为品类齐全的新低端产业，并非升为高端产业，而是在实质上重新定义了低端产业。", "evidence": ["E20"]},
    {"claim_id": "C018", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "A类外流产业是可靠半文盲运转的上一代低端产业，确仍劳动密集、能支撑就业——前提是产品质量和产量有足够优势。", "evidence": ["E21"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些外移老低端产业在质量上远不是新一代的对手、产量无明显优势、成本优势也不明显，是冢中枯骨。", "evidence": ["E22"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些外移老低端产业的一大利润核心是欠发展国家对环境管制的低标准与发展中国家的剩余碳排放指标；赚的不是人工成本差，而是省掉的环保成本与用贿赂、“招商政策”逃掉的税。", "evidence": ["E23"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "B类溢出的新低端产业，其核心经验和技术大部分同中国有关，很多干脆是中国本土产业链的附庸。", "evidence": ["E24"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "转向越南和印度的产业很难拿到中国本来就无意放弃的工艺流程；这些流程只在中国存在，欧美无法重建，中国也绝不会轻易放弃。", "evidence": ["E25", "E26"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "台湾问题当前，中国要做好孤身对抗世界的完全准备，因此不能容产业链任何一环真正完全流失。", "evidence": ["E27"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "外移的生产环节离开中国产业链半成品的支持与需求的滋养，会立刻遭遇重大困难。", "evidence": ["E28"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧美需要的最终产品中间始终会有大量环节必须由中国完成；越南和印度能做的某些环节并不会真正形成对中国的替代。", "evidence": ["E29", "E30"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多工艺最先进的实践经验已经只有中国有；欧美自己十几二十年没真正下过那些低端生产线，想越过中国教给越南印度也办不到。", "evidence": ["E31"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "外移产业并没有老一代低端产业对欠教育劳动力的吸纳能力。", "evidence": ["E32"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国真正的危机不是工业总产值下降（因为没有也不会下降），而是总产值上升同时产业链岗位数量在下降。", "evidence": ["E33"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原低端产业无法向中西部转移，因为它们基本上消失了；事实是原来的低端产业变成了需要人更少的新低端产业，没得可移。", "evidence": ["E34", "E35"]}
   ],
   "argument_steps": [
    "指出提问框架中的隐性假设：低端产业如同不蒸发的水银，长期存在、随成本流动。",
    "改写问题：该意义上的“低端产业”本身是否还存在、是否正在消失。",
    "举证历史：手工制铁、煮海熬盐等劳动密集工艺被整体淘汰。",
    "提出下限上移命题：低端产业仍存在，但其门槛正远离未受教育人群。",
    "定义式归纳：低端制造业的奥秘是人力柔性生产线对抗欠柔性自动化线。",
    "给出三条消解因素（自动化成本下降、全产业链广域分工、柔性化设计经验提高）并比较重训员工与调线成本。",
    "以ABB双臂机器人为实例支持柔性化前沿。",
    "推出结论：低端产业正在历史性消失。",
    "表明立场：不看好低端产业转移与产值飞涨；旧低端产业升级为新低端产业。",
    "分类外流产业：A类（更原始、靠半文盲）不具备质量产量成本优势，利润核心是环境与税收套利。",
    "B类（新低端产业）依附中国产业链，拿不到中国不愿放弃的工艺流程。",
    "补充国家安全与产业链完整性理由（台湾问题、孤身对抗世界的准备）。",
    "推出预测：外移环节离开中国支撑会遭遇困难，不构成对中国的替代。",
    "归结真正危机：产值上升而岗位下降；故不存在可向中西部转移的产业。"
   ],
   "concept_usage": [
    {"term": "低端产业", "meaning": "本文中特指20世纪末到21世纪初意义上、能由劳动密集暴力破解、可由低教育程度人口承接的产业形态；作者主张这一形态正在消失并被重新定义。", "evidence": "P002", "ambiguity": "全文未给出可操作的划分标准；“新低端产业”与“高端产业”的界线作者只说“实质上重新定义”。"},
    {"term": "低端产业的下限", "meaning": "进入该产业所需的最低教育／训练门槛，作者主张其正在迅速上移。", "evidence": "P006", "ambiguity": "上移的度量与证据来源本文未给数据。"},
    {"term": "柔性生产线／欠柔性生产线", "meaning": "用以解释低端制造业竞争力的方案对比：人力组成的柔性产线 vs 设计安装调试自动化的欠柔性产线。", "evidence": "P009", "ambiguity": "为作者的概括性表述，未注明出处。"},
    {"term": "去劳动密集化", "meaning": "新一代占据低端产业生态位的产业形态所需人力大幅减少。", "evidence": "P025", "ambiguity": "无。"},
    {"term": "生态位", "meaning": "借用生物学比喻，指“低端产业”在产业体系中所占的位置可由新形态占据。", "evidence": "P025", "ambiguity": "比喻性用法。"},
    {"term": "新低端产业", "meaning": "东南沿海老低端产业链升级后的品类齐全形态；作者强调不是高端产业。", "evidence": "P027", "ambiguity": "与旧低端产业的区分标准未量化。"},
    {"term": "环境管制低标准／剩余碳排放指标", "meaning": "作者指认的外移老低端产业真实利润来源之一。", "evidence": "P031", "ambiguity": "属事实性断言，本文未提供数据，需外部核查。"}
   ],
   "examples_and_targets": [
    "手工制铁业、煮海熬盐的制盐业——作者例证（历史对照，说明工艺被淘汰）。",
    "ABB双臂工业机器人——作者例证（柔性化前沿；P014 为该文段文字，lexical 未覆盖）。",
    "工业机器人的流水线协作——作者例证（P017，lexical 未覆盖）。",
    "全自动宝马工厂是否会搬到印度和越南——作者反问式类比（P040）。",
    "小学辍学毕业（二十年前）、初中以下文化程度人口——作者用以标示门槛变化的人群。",
    "越南、印度、欧美、中国东南沿海、中西部、台湾问题——作者论证涉及的地区与情境（P034-P038、P035）。",
    "欠发展国家、发展中国家——作者指认环境与税收套利对象（P031）。"
   ],
   "conditions": [
    "讨论对象限定为“20世纪末到21世纪初意义上的‘低端产业’”。",
    "假设语气：“如果‘低端产业’本身干脆正在消失呢？”",
    "弱化语气：“未必就一定比召集、供养和管理数万员工更慢和更贵”“并不见得一定比调整生产线更便宜和更快”。",
    "A类产业的就业支撑能力附条件：“如果它们的产品质量和产量能有足够优势的话”。",
    "推测语气：“恐怕也少有这样的岗位存在了”“恐怕已经过去了”。",
    "政策前提：台湾问题当前，中国要做好孤身对抗世界的完全准备。",
    "范围性限定：“很多”“大部分”“相当大的比例”等未量化的程度词贯穿全文。"
   ],
   "rhetoric_and_tone": "产业评论与论辩结合，语气自信、带训示感：以“真正的问题是”“你们要注意”“甚至不客气的说”“说句实话”作推进标记，直接对读者说“你们可以看看这个例子”“你可以试试”；频繁使用反问（“手工制铁业今何在？”“难道ta们是要把全自动宝马工厂搬到印度和越南去吗？”）；贬抑性比喻“冢中枯骨，行尸走肉而已”“半自杀”式的强烈措辞；用 A）B）编号分类，结构为先破前提、再分类举证、后收结论。",
   "unresolved_questions": [
    "P014“ABB双臂工业机器人”、P017“工业机器人的流水线协作”两段为 lexical 未覆盖片段（text_lexical_divergence），疑为视频或图片说明文字；语料 lexical 中无 image 节点，故本记录未按图片文章处理，但是否对应媒体节点需人工核验。",
    "“低端产业”与“新低端产业”的划分标准未量化，作者未给数据来源。",
    "关于环境管制低标准、剩余碳排放指标、逃税等事实性断言无数据支撑，需外部核查（P031）。",
    "关于欧美“十几二十年没有真正下过那些低端生产线”等断言需外部核查（P039）。",
    "“台湾问题当前……孤身对抗世界”为作者的时局判断，本文未展开论证。",
    "提问者所问的转移方向（中西部／东南亚）在文中只被间接回答为“没得可移”，未给出分地区比较。",
    "“产值飞涨”具体所指的统计口径与时期未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人们往往在假设低端产业就像不会蒸发的水银，是长期存在的，只是哪里成本低就会流向哪里。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "真正的问题是，20世纪末到21世纪初意义上的“低端产业”本身是否还仍然存在？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果“低端产业”本身干脆正在消失呢？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "很多古老的、能由劳动密集来暴力破解的工艺正在整个的被淘汰。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "低端产业的下限正在迅速的远离未受教育的文盲人群。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "低端产业的下限正在悄无声息的上移", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "依赖低端劳动力的劳动密集型产业本身正在萎缩。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "就是用“人力组成柔性生产线”方案，来对抗“设计、安装与调试自动化的欠柔性生产线”方案。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "未必就一定比召集、供养和管理数万员工更慢和更贵。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P011", "quote": "全产业链的广域分工，在很大程度上系统的消解了单生产线不够柔性的问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "并不见得一定比调整生产线更便宜和更快。", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P015", "quote": "调整抓取路径，可以用你自己的手捏着机器人的手腕引导它做一遍——一遍教会。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "你可以试试是它升级快、调整快，还是教会一个人快。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "换句话说，“低端产业”本身正在历史性的消失。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "所以，我并不看好所谓的“低端产业转移”和所谓的“产值飞涨”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "能靠初中以下文化程度人口承接的低端产业大规模存在的历史时期恐怕已经过去了。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P024", "quote": "其产品也正在迅速的失去市场。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "但也大大的去劳动密集化了。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "不是不向西部转移，而是可以简单转移的传统低端产业已经死得差不多了，没什么可转移的。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P027", "quote": "它们并不是升级为高端产业了，而是在实质上重新定义了低端产业。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P029", "quote": "如果它们的产品质量和产量能有足够优势的话。", "relation": "qualifies"},
    {"key": "E22", "paragraph_id": "P030", "quote": "这是冢中枯骨，行尸走肉而已。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P031", "quote": "它们实际上赚的不是人工成本差，而是在赚省掉的环保成本、在赚用贿赂和“招商政策”逃掉的税。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P032", "quote": "这种新低端产业事实上大部分的核心经验和技术都和中国有关", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P034", "quote": "恐怕很难拿到中国本来就无意放弃的工艺流程。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P035", "quote": "这些流程只在中国存在，欧美无法重建，中国也绝不会轻易放弃", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P035", "quote": "台湾问题当前，中国要做好孤身对抗世界的完全准备，岂能容产业链的任何一环真正的完全流失？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P036", "quote": "会立刻遭遇重大困难。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P037", "quote": "中间仍然会——而且始终会有大量的环节必须由中国完成。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P038", "quote": "并不会真正形成对中国的替代。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P039", "quote": "有很多工艺最先进的实践经验已经只有中国有了。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P041", "quote": "它们并没有老一代低端产业对欠教育劳动力的吸纳能力。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P042", "quote": "而是尽管工业总产值在上升，但是产业链上的岗位数量在下降。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P043", "quote": "这就是为什么这些原低端产业无法向中西部转移——因为它们基本上消失了。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P044", "quote": "而是原来的低端产业变成了新低端产业，甚至需要的人都更少了，没得可移。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["产业经济／制造业", "国际产业转移", "劳动经济与就业", "技术与自动化"],
   "issue_candidates": ["低端产业是否正在消失", "产业转移方向（中西部／东南亚）", "自动化对劳动密集产业的替代", "产业链完整性与国家安全", "低教育劳动力就业岗位下降"],
   "text_function_candidates": ["答疑（改写提问前提）", "产业评论", "论证", "预测性判断"],
   "object_candidates": ["提问者（匿名）", "中国／东南沿海／中西部", "越南", "印度", "欧美", "欠发展国家／发展中国家", "ABB", "宝马", "台湾问题"],
   "working_keywords": ["低端产业", "劳动密集", "柔性生产线", "全产业链", "去劳动密集化", "生态位", "新低端产业", "碳排放指标", "环保成本", "招商政策", "岗位数量"]
  },
  "notes": "正文 44 段，无 image 节点；无 provenance/superseded。P014、P017 为 text_lexical_divergence（原文有内容 lexical 未覆盖），疑为视频／图片说明文字，已按正文记录但未声称看过任何图像；因 lexical 无 image 节点，本记录 images=[]，status 保持默认 read，并在 unresolved_questions 登记需人工核验。question 属提问者，其“低端产业将向某处转移”的前提被作者改写，未归给作者。P031、P039 等事实性断言已标注需外部核查。P014/P017 未作为证据引用。"
 },
 "045db0cb": {
  "analysis": {
   "question_context": "提问字段问“人的痛苦从根本上说源于哪？”（Q001，属提问者）。作者以承接式短答作答：痛苦源于“认为自己应得、配得”，随后逐条列举这类自我应得信念，最后归结到“平均水平”的幻想并给出“没得到，所以痛苦”的收束。全篇是作者本人的判断，无引用、无对手、无提问者立场混入。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接给出根源：认为自己应得、配得（承接提问省略主语“痛苦”）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006"], "summary": "列举应得信念：人天然应得安全、健康与正常寿命；应得平均水平待遇；别人应尊重甚至尊敬自己；人天生应拥有平等地位与机会；应享受令自己满意的公平。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "继续列举：付出自以为相同的劳动应得相同报酬；应有不少于任何人的权利、不多于任何人的义务、不弱于平均水平的运气。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "归结为“不低于平均水平”的自我信念与索取，并指出那个“平均水平”完全出自幻想和鼓吹。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P013"], "summary": "末句给出机制：没得到，所以痛苦。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的痛苦从根本上源于认为自己应得、配得。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种应得感包括：人天然应得安全、健康与正常寿命，应得平均水平待遇，别人应尊重甚至尊敬自己，人天生应拥有平等地位与平等机会、应享受令自己满意的公平。", "evidence": ["E2", "E3", "E4", "E5", "E6"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应得感还包括：付出自以为相同的劳动应得相同报酬，应有不少于任何人的权利、不多于任何人的义务、不弱于平均水平的运气。", "evidence": ["E7", "E8", "E9", "E10"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人坚定不移相信自己至少不低于平均水平，理应拥有不低于平均水平的一切。", "evidence": ["E11"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那个“平均水平”完全出自幻想和鼓吹。", "evidence": ["E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "机制是：没得到，所以痛苦。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "承接提问省略主语，直接给出根源判断：源于认为自己应得、配得。",
    "以排比列举展开“应得”的具体内容（安全健康寿命、平均待遇、被尊重、平等地位机会、满意的公平）。",
    "继续列举（同劳同酬、不少于任何人的权利、不多于任何人的义务、不弱于平均的运气）。",
    "归结为“不低于平均水平”的自我定位与索取。",
    "指出该“平均水平”出自幻想和鼓吹。",
    "以“没得到，所以痛苦”收束因果。"
   ],
   "concept_usage": [
    {"term": "应得／配得", "meaning": "本文中指派生痛苦的核心心态：认为自己理所应当获得某些待遇、地位与结果。", "evidence": "P001", "ambiguity": "作者未区分正当权利主张与错位期待，二者被合并处理。"},
    {"term": "平均水平", "meaning": "被作者界定为完全出自幻想和鼓吹的比较基准，人据此相信自己应得“不低于平均水平的一切”。", "evidence": "P012", "ambiguity": "参照群体（与谁比、在什么范围内比）未说明；“鼓吹”的主体未指明。"},
    {"term": "公平", "meaning": "文中指“令自己满意的公平”，即按自我满意度定义的公平。", "evidence": "P006", "ambiguity": "带贬义限定，作者未给出他所认可的公平标准。"}
   ],
   "examples_and_targets": [
    "无具名人物、事件、机构或数据。列举项（安全健康寿命、平均待遇、被尊重、平等地位机会、满意的公平、同劳同酬、权利与义务、运气）均属作者归纳的心态类型，非外部例证。",
    "“平均水平”作为被作者指认为幻想的对象（P012）。"
   ],
   "conditions": [
    "全篇未给出任何显式条件词；主张以无限制的“人”为主语，未标明例外或适用范围。",
    "隐含口径：所讨论的痛苦指“没得到（自认应得之物）”所引发的那一类。",
    "列举项均冠以“认为／相信自己”，即作者描述的是当事人的主观信念而非作者认可的事实。"
   ],
   "rhetoric_and_tone": "格言体与排比列举：全文承接提问省略主语“痛苦”，用九个“认为……”平行句铺排，句短、节奏齐整，无第一人称、无称呼、无反问、无引用；末两段以“而那个‘平均水平’，完全出自幻想和鼓吹”“没得到，所以痛苦”连续收束，语气冷峻、断言式，带贬抑（“幻想和鼓吹”）。",
   "unresolved_questions": [
    "作者未限定是否一切痛苦都源于此，也未讨论例外情形。",
    "“应得”与“配得”是否同义、是否有正当与不正当之分，本文未说明。",
    "“幻想和鼓吹”中的鼓吹者是谁、通过什么渠道，本文未说明。",
    "“平均水平”的参照群体与测量方式未说明。",
    "本文只给根源判断，未给出任何化解或修正的建议（提问未要求，但值得登记）。",
    "brief 与正文内容高度重合（brief 为同一文本的前缀截断），未据 brief 补写正文。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "源于认为自己应得、配得。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "认为人天然的应该得到安全、健康和正常寿命。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "认为自己理所应当获得平均水平的待遇。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "认为别人理所应当尊重自己，甚至尊敬自己。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "认为人天生应该拥有平等地位、平等机会。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "认为人天生应该享受到令自己满意的公平。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "认为付出了自以为与别人相同的劳动，应该获得与别人相同的报酬。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "认为自己应该有不少于任何人的权利。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "认为自己应该有不多于任何人的义务。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "认为自己应该有不弱于平均水平的运气。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "坚定不移的相信自己至少是一个不低于平均水平的人，理应拥有不低于平均水平的一切。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "而那个“平均水平”，完全出自幻想和鼓吹。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "没得到，所以痛苦。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／痛苦与期待", "心态与自我认知", "社会比较"],
   "issue_candidates": ["痛苦的根源", "应得感／配得感", "平均水平的幻想", "公平与平等的期待"],
   "text_function_candidates": ["答疑", "格言式简述", "因果归结"],
   "object_candidates": ["提问者（匿名）", "泛指的“人”（无具名人物）"],
   "working_keywords": ["应得", "配得", "平均水平", "平等地位", "公平", "幻想", "鼓吹", "痛苦"]
  },
  "notes": "正文 13 段，全部为 body，无 heading、无图片；无 provenance/superseded。question 属提问者，正文为承接式回答（省略主语），提问者立场未混入作者主张。brief 与正文重合（brief 是同一文本的截断前缀），仅作定位参考，未用于支持任何主张。全篇无外部例证与数据，故 examples_and_targets 仅登记列举项性质。"
 },
 "53e9189f": {
  "analysis": {
   "question_context": "提问字段问“什么是文字的张力？”（Q001，属提问者）。作者没有给出定义式答案，而是用一段第一人称的阅读体验书写来示范：被一段文字击中后不可逆地改变（回不去、来不及、忘不了、装不下去），并以粗口与抱怨收尾。全文可视为以体验代替定义的应答，是否构成对“什么是”的正面回答存在歧义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "以手术式意象起手：白刀子进红刀子出、眼睁睁挖出你的心、擦了擦、放回去。", "role": "other"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "插入被打断的日常（“你牙还没刷”）与主体的改变：你已不是原来的你，或终于知道原来的你不是你，咯噔一下——“完了。”", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "排比式申说不可逆：想回到没看到之前回不去了、想不被改变来不及了、想忘记也忘不了了、想继续装糊涂装不下去了。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "以“真tm的，难得糊涂”过渡，并用“这不是文字，这是命”把体验提到命运层面。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032"], "summary": "粗口式爆发与自我埋怨：手贱乱点什么、为什么不早睡、明天还要上班、为什么要多点这一下。", "role": "other"},
    {"unit_id": "U006", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "回到“我牙还没刷”，以“扎一针，见点血，不够吗？！”与“有必要用这么长的刀吗！”质问，末以“还更新吗？”“能不能不要总是半夜更新啊！！！”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被这样的文字击中之后不可逆：回不去、来不及、忘不了，也装不下去。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把这种被击中的体验表述为“这不是文字，这是命”，即提升到命运层面而非文字技巧层面。", "evidence": ["E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以“扎一针，见点血，不够吗？！”反问，并抱怨“有必要用这么长的刀吗！这么长的刀！！”，即以比喻质问文字杀伤的过当。", "evidence": ["E6", "E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以“还更新吗？”“能不能不要总是半夜更新啊！！！”表达对深夜更新的抱怨式追问。", "evidence": ["E8", "E9"]}
   ],
   "argument_steps": [
    "以“白刀子进，红刀子出”与挖心后放回的意象开场，把文字作用比作外科手术。",
    "用“你牙还没刷”打断，形成日常与剧痛的并置。",
    "宣告主体的改变：你已经不是原来的你，或终于知道原来的你不是你。",
    "以“你就咯噔一下。‘完了。’”标记醒悟时刻。",
    "以四组“想……，……不了”排比申说不可逆。",
    "借俗语“难得糊涂”表达宁可不知，随即断言“这不是文字，这是命”。",
    "转入粗口与自我埋怨，交代情境（手贱点开、深夜、明天还要上班）。",
    "回到“我牙还没刷”，用针与刀的比喻质问杀伤是否过当，以催更／抱怨式问句收尾。"
   ],
   "concept_usage": [
    {"term": "文字的张力", "meaning": "本文未作定义，而是以一段被文字击中、不可逆改变的阅读体验来示范该词所指。", "evidence": "P007", "ambiguity": "无命题化定义，也未给判定标准；与提问“什么是……”之间是示范关系而非界定关系。"},
    {"term": "命", "meaning": "用于把上述体验从“文字”层面拔高到不可回避的命运层面。", "evidence": "P026", "ambiguity": "修辞性用法，未说明与命运的具体关系。"},
    {"term": "刀／针", "meaning": "比喻文字的作用力与杀伤范围；“扎一针，见点血”对“这么长的刀”构成过当与否的对照。", "evidence": "P036", "ambiguity": "比喻的对应项（谁持刀、扎谁）随语境滑动，未固定。"},
    {"term": "难得糊涂", "meaning": "引用俗语，表示宁可保持不知情的状态，与“你已经知道了”形成对照。", "evidence": "P024", "ambiguity": "为俗语引用，非作者自创概念。"}
   ],
   "examples_and_targets": [
    "无具名人物、机构、数据或历史叙述。",
    "“你牙还没刷”“我明天还要上班”作为生活细节，用于制造日常与剧痛的落差（P005、P030）。",
    "“还更新吗？”“能不能不要总是半夜更新啊！！！”暗示某个连载作品的更新情境，但作品名、平台、作者均未出现（P040、P041）。"
   ],
   "conditions": [
    "情境依赖：夜晚、睡前、偶然点开更新（“我为什么不早点睡啊！”“为什么要多点这一下？！”）。",
    "不可逆的前提是“你已经知道了”（P017）。",
    "全篇以第二人称“你”与第一人称“我”交替，未给出适用范围或例外条件。",
    "无外部事实断言，故无条件性事实需核查。"
   ],
   "rhetoric_and_tone": "情绪书写与戏仿为主：短句分行、口语化、拟声与粗口变形（“真想Fu你一万个ck！”“Fuuuuuuuuu……ck！！！！”“md”“真tm的”）、感叹号与问号堆叠；第二人称“你”制造代入，第一人称“我”在后半转为哀嚎；重复“我牙还没刷”形成首尾呼应；“这不是文字，这是命”用短句对照制造断言效果。整体为夸张、自嘲、戏谑的叙事语气，而非论证语气。",
   "unresolved_questions": [
    "提问要求定义“什么是文字的张力”，本文未给定义或判定标准，是否算正面回答存在歧义。",
    "“半夜更新”的具体作品、平台与作者未出现，无法据此定位指涉对象，不得据 brief 补写。",
    "粗口的有意变形（Fu…ck、md、tm）原文如此，未作改写，可能影响语气与可引用性判断。",
    "本篇是真实阅读反应还是对读者反应的戏仿，正文未说明。",
    "brief 与正文高度重合（brief 为同一文本的前缀截断），仅作定位参考，未用于支持主张。",
    "存在“扎一针，见点血，不够吗？！”与“有必要用这么长的刀吗！”的比喻前后是否需要一致解释的歧义。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P014", "quote": "回不去了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P016", "quote": "来不及了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P019", "quote": "也忘不了了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P025", "quote": "这不是文字，", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P026", "quote": "这是命。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P036", "quote": "不够吗？！", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P037", "quote": "有必要用这么长的刀吗！", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P040", "quote": "还更新吗？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P041", "quote": "能不能不要总是半夜更新啊！！！", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "原来的你不是你。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文学／写作与修辞", "阅读体验", "情绪书写"],
   "issue_candidates": ["什么是文字张力", "文字对读者的不可逆影响", "深夜追更的体验"],
   "text_function_candidates": ["经验书写／叙事", "情绪表达", "以示范代替定义", "戏仿"],
   "object_candidates": ["第一人称“我”（作者）", "泛称“你”（读者）", "未具名的连载作品／平台"],
   "working_keywords": ["文字张力", "白刀子进，红刀子出", "挖心", "牙还没刷", "难得糊涂", "这不是文字，这是命", "半夜更新"]
  },
  "notes": "正文 41 段全部为 body，无 heading、无图片；无 provenance/superseded。本篇未按分析—论证结构写作，而是以体验示范应答提问；main_claims 只提取文中可直接定位的短断言（不可逆、不是文字是命、刀针质问、更新抱怨），未把叙事意象升格为定义。E10 作为 context 证据用于说明主体改变一节，未支持具体主张。brief 与正文重合（前缀截断），未据 brief 补写。"
 },
 "e122a811": {
  "analysis": {
   "question_context": "提问字段问“人生应该活成什么样子，该以什么样的方式活着？”（Q001，属提问者）。作者的应答主体是一个图片节点（IMG001）加一个指向哔哩哔哩视频《兰迪·波许教授的最后一课／Randy Pausch's Last Lecture》（2007，纪录片，美国）的链接；正文可读文本只有该链接的标题本身。图片内容未经核验，因此作者的具体主张与论证无法从可读文本确定，本篇标记为需图像核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "唯一可读正文是一行指向哔哩哔哩视频《兰迪·波许教授的最后一课》的链接标题；正文无其他文字论述。", "role": "context"}
   ],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [
    "兰迪·波许《最后一课》（Randy Pausch's Last Lecture，2007，纪录片，美国）—— P001 可读文本仅为指向该视频的链接标题，属引用外部材料的标题，不是作者的论述文字。",
    "IMG001（//asset.sooon.ai/p/2020-07/17/b39e9f0b89ebd4b1ea1f8b84d6621f5f.jpg）—— 图片节点，内容未经核验。",
    "哔哩哔哩（bilibili）—— 链接所指平台，出现在标题文字中（含“干杯~-bilibili”字样）。"
   ],
   "conditions": [
    "无可提取的论证条件：可读文本仅为链接标题。",
    "图片未核验，作者立场、条件与适用范围均无法判定。"
   ],
   "rhetoric_and_tone": "以图片加视频链接作答，无文字论述，因此无法从可读文本判断语气与修辞；可读文本本身是转载视频的标题，带有平台字样（哔哩哔哩、(゜-゜)つロ 干杯~-bilibili），非作者自撰的论述语句。",
   "unresolved_questions": [
    "图片未核验，需人工／多模态复核：IMG001 内容未知，本篇不能被视为已完整阅读。",
    "作者对“人生应该活成什么样子”的具体主张无法从可读文本确定，故 main_claims 留空而非据标题推测。",
    "P001 属 text_tail_not_in_lexical 片段，且来源于 lexical 中的 link 节点标题；作者是否另加了推荐语（可能在图片中）无从判断。",
    "链接目标 URL 仅存在于 lexical 的 link 节点，未在正文文字中展示，因此未据此写任何内容。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "兰迪·波许教授的最后一课", "relation": "context"},
    {"key": "E2", "paragraph_id": "P001", "quote": "Randy Pausch's Last Lecture", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["影像／纪录片推荐", "人生意义与生活方式"],
   "issue_candidates": ["人生应该活成什么样子", "以影像材料代替论述作答"],
   "text_function_candidates": ["以图片＋链接作答（无可读的文字论述）"],
   "object_candidates": ["兰迪·波许／Randy Pausch", "哔哩哔哩（bilibili）", "美国", "2007年"],
   "working_keywords": ["最后一课", "Last Lecture", "纪录片", "bilibili", "人生方式"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 1 个图片节点（IMG001，src=//asset.sooon.ai/p/2020-07/17/b39e9f0b89ebd4b1ea1f8b84d6621f5f.jpg），图片内容未经核验，需图像核验；已读部分仅为正文文本（一行视频链接标题）。按简报第 4 节，本篇 status=needs_reread、image_checked=False，不得标记 read。正文可读文本 81 字（P001），无其他段落；P001 为 text_tail_not_in_lexical 片段。未根据图片标题或上下文补写正文，main_claims 留空。"
 },
 "e0005624": {
  "analysis": {
   "question_context": "提问字段问“你认为在这个世界上存在绝对坚定的无神论者吗？”（Q001，属提问者，要求作者表态）。作者没有直接回答“存在／不存在”，而是把判定时点推到临终、把知情权归给本人：临终那几秒没什么力气留遗言，坚不坚定那时才知道，也只有人自己才知道。作者自身是否为无神论者、其倾向如何，正文未说明。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以“跟电视剧演的不一样”起手，提出反常识观察：人到临终那几秒是没什么力气留遗言的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "把判定时点定在临终：坚不坚定，那时候才知道。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "收窄知情范围：也只有人自己才知道。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与电视剧所演的不一样，人到了临终那几秒是没什么力气留遗言的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "信仰是否坚定，要到临终那时才知道。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "坚定与否也只有本人自己才知道。", "evidence": ["E3"]}
   ],
   "argument_steps": [
    "以“跟电视剧演的不一样”否定影视中临终留遗言的常见呈现。",
    "给出观察：临终那几秒没什么力气留遗言。",
    "据此把“坚不坚定”的检验时点定在临终。",
    "再把知情权收归本人：也只有人自己才知道。"
   ],
   "concept_usage": [
    {"term": "坚定", "meaning": "在本文语境中指无神论信仰是否绝对坚定；作者把它的检验推到临终时刻，且认为只有本人可知。", "evidence": "P002", "ambiguity": "未给判定标准，也未说明“自己知道”是否足以构成“绝对坚定”。"},
    {"term": "遗言", "meaning": "临终时留下的话语；作者认为临终几秒因无力而难以留下。", "evidence": "P001", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "电视剧（泛称）—— 作者用作对照的修辞材料，用以否定临终留遗言的常见呈现（P001）。",
    "无具名人物、机构、事件或数据；无神论者、信仰者均未被具名。"
   ],
   "conditions": [
    "时间条件：临终那几秒。",
    "知情条件：只有本人自己知道，排除外部观察者代为判定。",
    "全篇未对“绝对坚定”给出定义、观察指标或检验方式。",
    "适用范围未说明（是否只针对无神论者，还是泛指一切信仰坚定问题）。"
   ],
   "rhetoric_and_tone": "短句、口语、断言式，语气平静克制；以“跟电视剧演的不一样”作反常识开场，用“那时候才知道”“也只有人自己才知道”层层收窄，把公共可判定问题转为个人自知的问题；无称呼、无反问、无训诫，也没有对提问者或任何群体下判断。",
   "unresolved_questions": [
    "作者未直接回答是否存在绝对坚定的无神论者；以推迟判定时点与归给本人自知的方式回应，是否构成否定或回避，存在歧义。",
    "“坚定”的判定标准与检验方式未说明。",
    "“人到了临终那几秒是没什么力气留遗言的”为作者的观察性断言，无来源与证据，需外部核查。",
    "“只有人自己才知道”与“绝对坚定”的关系未说明：外人不可知是否等于不存在，本文未表态。",
    "作者未说明自身是否无神论者或其倾向。",
    "brief 与正文重合（brief 为同一文本的前缀），仅作定位参考，未据 brief 补写。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "跟电视剧演的不一样，人到了临终那几秒是没什么力气留遗言的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "坚不坚定，那时候才知道，", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "也只有人自己才知道。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教与信仰", "死亡与临终", "认识论／他人之心"],
   "issue_candidates": ["是否存在绝对坚定的无神论者", "以临终时刻检验信仰坚定", "自我认知的不可替代性"],
   "text_function_candidates": ["答疑（间接回应）", "短评", "格言式收束"],
   "object_candidates": ["提问者（匿名）", "电视剧（泛称）", "无神论者（泛称）"],
   "working_keywords": ["坚定", "无神论者", "临终", "遗言", "电视剧"]
  },
  "notes": "正文 3 段，全部为 body，无 heading、无图片；无 provenance/superseded。question 属提问者并明确要求作者表态，作者未直接给“存在／不存在”的答案，故未构造该主张，只记录文中三处可直接定位的断言。P001 的临终观察为作者断言而非引用，已登记需外部核查。brief 与正文重合，未用于支持主张。"
 },
 "45874a32": {
  "analysis": {
   "question_context": "提问字段问“如何做到知行合一?”（Q001，属提问者，属方法诉求）。作者未给操作步骤，而是先区分“知”与“信”，再解释“知而不行”的成因，进而把这一现象判读为“不是bug而是设计”，最后提出存在一条区分知而不行是否值得忧虑的“红线”，并以“（未完，待续）”结束。作者的回答是成因解释与评价性判断，不是方法指南。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "提出核心区分：知不等于信，信才影响行；以“没有信用将举步维艰”“学习对生活很重要”“毒品危害人生”三例说明很多人知道却不信，所以不行。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "给出成因：这些道理带“会”“很可能”“到将来”“大概率”“最终”“比较”等软话与非眼下的福利，而遵从它们出现的痛苦却不是大概率、不是将来、也不是比较的。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "由此推出人对硬证据的要求：需要更切肤、更直感的证据（众叛亲离一次、求一回职、领导一回事业、进一次看守所破产一回），要见了棺材才好落泪。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "翻案式判断：这不是bug而是设计——因为没人确知过去的总结是否仍适用于今天的将来，也没人能确定自己不是那个小概率；正因此人类不会成为老经验的绝对奴隶而灭绝于环境变迁；极少部分知而不信者猜对了，往往为新的危机提供新的转机。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019"], "summary": "限定与遗留问题：不能、甚至不应该考虑完全“改正”它；于是存在一条复杂而微妙的红线，红线内“知而不行”并不要紧，红线外才值得忧虑——而这条红线在哪里，作者以问句留待后文。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P020"], "summary": "作者自注文本未完：“（未完，待续）”。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "知不等于信，信才影响行。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人知道某些道理但并不信，所以不行（作者举信用、学习、毒品三例）。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些道理带着“会”“很可能”“到将来”“大概率”“最终”“比较”这类软话，带着“不见得”“不是眼下”的福利。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "遵从这些道理而出现的痛苦却不是大概率、不是将来、也不是比较的。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人需要有更切肤、更直感的证据，来支撑自己为将来的、可能的危险付出眼下的、现实的代价。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类硬证据是：真的众叛亲离一次、求一回职、领导一回事业、进一次看守所破产一回——要见了棺材才好落泪。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "知而不信并不是一个bug，而只是一种设计。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为没有人真的知道过去的总结是否还适用于今天的将来，也没有人能确定自己不是那个小概率。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恰恰是这一点从根本上保证了人类不会成为老经验、老体会的绝对奴隶而灭绝于环境变迁。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "尽管良率极低，但很少一部分对过去的金玉良言知而不信的人真的猜对了，往往正是这些人为新的危机提供新的转机。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这不是bug，而是一个有极大副作用、但可以保住人类不易灭绝的设计。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "你不能——甚至也不应该——考虑完全“改正”它。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这意味着存在一条复杂而微妙的红线：红线内“知而不行”并不要紧，红线外知而不行才值得忧虑。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者把“这条红线在哪里”作为未决问题提出，本文未给出答案。", "evidence": ["E18"]}
   ],
   "argument_steps": [
    "提出区分：知不等于信，信才影响行。",
    "以信用、学习、毒品三例举证“知道但不信，所以不行”。",
    "给成因：这些道理的后果带软话（会／很可能／到将来／大概率／最终／比较）与非眼下的福利。",
    "作对照：实际痛苦却不是大概率、不是将来、也不是比较的。",
    "推出人对证据的要求：需更切肤直感的硬证据，才能为将来可能的危险付出眼下现实的代价。",
    "列举硬证据的形态（众叛亲离、求职、领导事业、看守所、破产），并以俗语“要见了棺材才好落泪”收束。",
    "翻案：这不是bug，而是一种设计。",
    "给设计理由：无人确知过去总结是否仍适用、无人确定自己不是小概率。",
    "推出功能：这保证人类不会成为老经验的绝对奴隶而灭绝于环境变迁。",
    "加程度限定：良率极低，但少数知而不信者猜对，并为新危机提供转机。",
    "重申判断：有极大副作用但可保住人类不易灭绝的设计。",
    "给出规范结论：不能也不应考虑完全改正它。",
    "限定适用范围：存在一条红线，红线内外“知而不行”的意义不同。",
    "留下未决问题：红线在哪里；并以“（未完，待续）”标注文本未完。"
   ],
   "concept_usage": [
    {"term": "知／信", "meaning": "本文核心区分：知是知道某个说法，信才是影响行为的东西；知而不行被解释为知而不信。", "evidence": "P001", "ambiguity": "作者未说明“信”如何产生、能否被促成，也未给二者的判定标准。"},
    {"term": "软话", "meaning": "指“会”“很可能”“到将来”“大概率”“最终”“比较”等模糊限定词，使道理的后果显得不迫切。", "evidence": "P005", "ambiguity": "为作者的描述性用语，未界定其范围。"},
    {"term": "硬证据", "meaning": "更切肤、更直感的证据（众叛亲离、求职、领导事业、看守所、破产等亲身经历）。", "evidence": "P010", "ambiguity": "未说明硬证据是否足以必然促成“信”。"},
    {"term": "bug／设计", "meaning": "工程隐喻：把“知而不信”判读为有极大副作用但保全人类不易灭绝的“设计”，而非可修复的缺陷。", "evidence": "P012", "ambiguity": "未说明“设计”是否意味着有设计者（造物或演化），归属存疑。"},
    {"term": "红线", "meaning": "区分“知而不行”是否值得忧虑的界线；红线内不要紧，红线外才值得忧虑。", "evidence": "P018", "ambiguity": "位置未给出，作者明说这是未解决的问题（P019），且文本未完。"},
    {"term": "良率", "meaning": "工程隐喻，指“对金玉良言知而不信的人猜对”的比例极低。", "evidence": "P015", "ambiguity": "无数据支撑，仅为修辞性程度词。"}
   ],
   "examples_and_targets": [
    "“人没有信用，将来会举步维艰”“学习对生活很重要”“毒品会危害人生”——作者列举的三类“知而不信”命题（P002-P004），属作者例证。",
    "众叛亲离、求一回职、领导一回事业、进一次看守所、破产一回——作者列举的硬证据类型（P009）。",
    "“要见了棺材才好落泪”——俗语引用，作收束（P011）。",
    "“金玉良言”“老经验、老体会”——作者用语，指被传承的旧总结（P015、P014）。",
    "无具名人物、机构、事件或数据；未出现外部事实断言。"
   ],
   "conditions": [
    "主体为“很多人”，非全称判断。",
    "硬证据的获取条件：“要真的……一次”。",
    "程度限定：“尽管良率极低，但有很少的一部分”。",
    "规范禁止：“你不能——甚至也不应该——考虑完全‘改正’它”。",
    "条件结构：以“在这个红线内……这条红线之外……”区分两类知而不行。",
    "关键前提缺失：红线位置未给出；文本以“（未完，待续）”结束，本篇为未完成文本。"
   ],
   "rhetoric_and_tone": "解释性说理与工程隐喻结合：以“很多人知道……但是ta们并不信，所以不行”三句排比举例；用口语化措辞“软话”“硬证据”“要见了棺材才好落泪”；以“bug／设计”为核心比喻并两次重申（“这并不是一个bug，而是一种设计”“并不是一个bug，而是一个有极大副作用、但却可以保住人类不易灭绝的设计”）；语气冷静、带轻微翻案意味（先承认像缺陷，再改判为设计）；末尾以“（未完，待续）”直接标注文本未完。",
   "unresolved_questions": [
    "提问是“如何做到知行合一”，作者未给方法步骤，只给成因解释与评价，是否构成回答存在歧义。",
    "红线在哪里——作者自己作为问题提出并标注未完待续，本文未给答案（P019、P020）。",
    "“信”如何产生、能否被促成，本文未说明；硬证据是否必然带来信，也未说明。",
    "“设计”是否意味着存在设计者（造物或自然演化），作者未说明，属可能影响解释的歧义。",
    "“保证人类不易灭绝”的机制论证未展开，也未给“良率”“小概率”的任何数据。",
    "本篇为未完成文本，后续内容不在本记录范围内，不得据 brief 或其他文章补写。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "知不等于信，信才影响行。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "很多人知道“人没有信用，将来会举步维艰”，但是ta们并不信，所以不行。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "但是ta们不信这话的有效性，所以不行。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "很多人知道“毒品会危害人生”，但是ta们不信，所以不行。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "因为这些东西带着“会”、“很可能”、“到将来”、“大概率”、“最终”、“比较”这些“软话”，", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "带着“不见得”，带着“不是眼下”的“福利”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "遵从它们而出现的痛苦却不是“大概率”的、不是“将来”的，也不是“比较”的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "ta们需要有更切肤、更直感的证据，来支撑自己为将来的、可能的危险付出眼下的、现实的代价。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "要真的众叛亲离一次，要真的求一回职、领导一回事业，要真的进一次看守所破产一回。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "要见了棺材才好落泪。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "但这其实并不是一个bug，而只是一种设计。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "但却没有人真的知道过去的总结是否真的还适用于今天的将来，也没有人能确定自己不是那个小概率。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "从根本上保证了人类不会成为老经验、老体会的绝对奴隶而灭绝于环境变迁。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "往往也就是这些人，在为新的危机提供新的转机。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "而是一个有极大副作用、但却可以保住人类不易灭绝的设计。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "你不能——甚至也不应该——考虑完全“改正”它。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "在这个红线内，“知而不行”并不要紧，这条红线之外，知而不行才值得忧虑。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "问题是，这条红线在哪里？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／知行关系", "认识论／知识与信念", "道德心理学"],
   "issue_candidates": ["如何做到知行合一", "知与信的区别", "知而不行的成因", "人类对旧经验的依赖与突破", "值得忧虑的知而不行的边界"],
   "text_function_candidates": ["答疑（转为成因解释）", "解释性论证", "翻案式评论（未完成）"],
   "object_candidates": ["提问者（匿名）", "泛指的“很多人”“ta们”（无具名人物）"],
   "working_keywords": ["知行合一", "知", "信", "软话", "硬证据", "bug", "设计", "红线", "良率", "金玉良言"]
  },
  "notes": "正文 20 段，全部为 body，无 heading、无图片；无 provenance/superseded。P020“（未完，待续）”为作者自注，本篇为未完成文本：红线位置等关键结论缺失，已在 unresolved_questions 登记，未据 brief 或其他文章补写。question 属提问者（问方法），作者实际给的是成因解释与评价，未把提问者立场写成作者主张。“设计”是否为有设计者的设计，作者未说明，已标为歧义。brief 与正文重合（前缀截断），仅作定位参考。"
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
