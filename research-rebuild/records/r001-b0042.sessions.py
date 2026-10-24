# -*- coding: utf-8 -*-
"""批次 r001-b0042 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0042.sessions.py            # 写 out/r001-b0042.out.jsonl
  python3 records/r001-b0042.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0042"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0042.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "3f3ffe4e": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待作家方方遭举报，被指疫情期间用特权送亲属出境？”；方方、举报、特权送亲属出境均属提问者提供的事件语境，不得当作作者立场。作者未回应举报与特权一事，改为分析方方日记所谓“纪实”的含义：读者把“我收到传言并相信”误读为“传言内容为真”的证言（P001-P009），进而讨论有公共影响力的写作者借含糊表达规避责任的“言论自由黑魔法”（P010-P018），最后给出三条自我防护建议（P019-P055）。正文未出现“方方”二字，只以“她”“一名作家”指称。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "指出读日记时的逻辑错误；把“纪实”拆成收到传言、相信、形成看法三个动作，逐一承认为事实。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "界定这种“纪实”的实际内容，并断言它不含“传言内容为真”的证言功能，也不含“为武汉人仗义执言”的功能。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009"], "summary": "反证：否则任何人（包括讨厌方方的人）都能据自己所信的传言去“仗义执言”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015"], "summary": "提出“真正的问题”：有公共影响力的作家是否没意识到这种表态的性质；并引述、反讽“都可以、都是合法的自由权利”式辩护。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018"], "summary": "论断知识分子、精英阶层只需初级训练即可掌握这种黑魔法，安全地既达成目的又摆脱责任；批评无意义，除非完全剥夺言论自由；自由是“合法攻击”的庇护所。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "建议之一：对逻辑关系高度敏感、分辨特洛伊木马以防被暗示性文字诱导；并断言被误导是自己的义务与责任（含 heading“被误导，就是你活该”等断语）。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039", "P040"], "summary": "建议之二：甄别和管理自己的信源；把人为麻瓜、黑法师、白法师、灰法师四种。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052"], "summary": "对该分类的自我限定：白法师也拔不净误导本能，最白的也只是很淡的灰法师；因为“魔戒”非人力可挡；并说明为何仍需控制黑白灰比例（白法师看得更多，但黑魔法有毒，施术者终将沦为魔戒的奴隶）。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P053", "P054", "P055"], "summary": "建议之三与收束：希望读者学会后能有点抵抗力；以“得到世界却失去神志值不值”追问；自注本篇主题是讲魔戒。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为很多读者读方方日记时犯了逻辑错误：她所说的“纪实”只是收到传言、相信传言并形成看法，并不承担“传言内容为真”的证言功能。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言这种“纪实”也根本不包含“为武汉人仗义执言”的功能。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以反证方式指出：若承认这种证言功能，则任何人（包括讨厌方方的人）都可凭自己所信的“特朗普贪污”“方方收了美国钱”一类传言去“仗义执言”。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者把真正的问题提为反问：一名吃文字饭、确认自己有公共影响力的作家，是不是真的没意识到“我听说了这些传言，我很相信”的表态是怎样的“充满智慧”的行为。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者引述这类“黑魔法”话术的自我辩护（说话人未标明）：被误导者自己负责，说话人只是说他自己相信，没有义务也不可能为别人的个人判断负责。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言知识分子、精英阶层只需非常初级的训练就能掌握这种“言论自由黑魔法”，做到安安全全地既达成目的又摆脱责任。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为批评这类人没有意义，因为这是“天意留下的特权”，除非完全剥夺一切言论自由。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言自由天生就是“合法攻击”的庇护所。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张应对之道第一是形成对逻辑关系的高度敏感、学会分辨这种特洛伊木马，防止被暗示性文字诱导作出证据和逻辑所不支持的判断。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言别人有“误导权”“表达含糊权”，都是合法且任何时候都不可能剥夺的权利，因此“变得不容易被误导”是自己的义务。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以 heading 断语宣称“被误导，就是你活该”，被误导干了蠢事要还债、坐牢乃至被处决都是罪有应得。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把人为四种：没意识到这套“拳法”的麻瓜、学会后用以取利的黑法师、竭力精研以从自身拔除的白法师、对敌人用对朋友不用的灰法师。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张最白的白法师也只是很淡很淡的灰法师，因为那枚“无责任的引诱ta人为自己的目的、理想服务、付账”的魔戒非人力所能抵挡。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称不能靠认证白法师而高枕无忧；理由是在以抵抗和拔除为目的的精研中，只有白法师最能排除黑魔法对事实和真理的扭曲。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预言这黑魔法有毒：施术者会产生越来越强烈的幻觉，甚至丧失自己的目的、沦为魔戒的奴隶，其话因而特别没营养、没新意、没价值。", "evidence": ["E21", "E22"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者表示希望读者学会这黑魔法、尝到魔戒威力时能稍微有点抵抗力，并以“人得到世界，却失去自己的神志——也就是生命本身——值得吗？”作结。", "evidence": ["E23", "E24"]}
   ],
   "argument_steps": [
    "破题：很多人读方方日记时犯了逻辑错误（P001）。",
    "界定“纪实”＝收到传言＋相信＋形成看法，三个动作各自成立（P002-P005）。",
    "界定该“纪实”的事实内容，并断言其不含证言功能与仗义执言功能（P006-P008）。",
    "反证：否则人人都能据自己所信的传言“仗义执言”（P009）。",
    "提出真正的问题：有公共影响力的写作者是否没意识到这种表态的性质（P010-P011）。",
    "引述并反讽辩护话术：都可以、都是合法的自由权利；由此得利只是“无可指责的幸运”（P012-P015）。",
    "论断：知识分子、精英靠初级训练即可掌握黑魔法，安全地达成目的又摆脱责任；批评无意义，自由是“合法攻击”的庇护所（P016-P018）。",
    "建议一：对逻辑关系高度敏感、识别特洛伊木马；并断言被误导是自己的义务与责任（P019-P033）。",
    "建议二：甄别信源；人分麻瓜、黑法师、白法师、灰法师四种（P034-P040）。",
    "自我限定：白法师也拔不净误导本能，最白的也只是很淡的灰法师；魔戒非人力可挡（P041-P046）。",
    "说明仍需控制黑白灰比例的理由：白法师看得更多，但黑魔法有毒，施术者终将沦为魔戒的奴隶（P047-P052）。",
    "建议三与收束：希望读者有抵抗力；以“得到世界却失去神志”追问；自注本篇讲魔戒（P053-P055）。"
   ],
   "concept_usage": [
    {"term": "纪实", "meaning": "本文中指“我收到了这样那样的传言，我都相信得很，然后我认为ABC”，即收到传言、相信、形成看法；不含“传言内容为真”的证言功能。", "evidence": "P002", "ambiguity": "作者用引号重述该词，未引用日记原文，是否等同原作者本意本文未说明。"},
    {"term": "误导权／表达含糊权", "meaning": "作者用来指说话人可以含糊表达、使人误判而不承担责任的说法。", "evidence": "P025", "ambiguity": "作者未给出实定法依据，是否为反讽性的自造词，本文未说明。"},
    {"term": "言论自由黑魔法／黑法师", "meaning": "借“言论自由”的含糊与暗示空间达成目的又摆脱责任的技巧；使用者称黑法师。", "evidence": "P016", "ambiguity": "未具名对手，“黑魔法”的具体手段清单本文未界定。"},
    {"term": "白法师／灰法师／麻瓜", "meaning": "作者自创四分类中的三类：竭力从自身拔除误导本能者、对敌用对友不用者、根本没意识到这套“拳法”者。", "evidence": "P037", "ambiguity": "分类判据与边界未定义；“朋友/敌人”何时成立被作者称为“神秘问题”。"},
    {"term": "魔戒", "meaning": "比喻“无责任的引诱ta人为自己的目的、理想服务、付账”的东西，作者称其非人力所能抵挡。", "evidence": "P044", "ambiguity": "与“黑魔法”的关系（技巧面与工具面）本文未明确界定。"},
    {"term": "特洛伊木马", "meaning": "指暗示性文字，读者会据此作出证据和逻辑所不支持的判断。", "evidence": "P020", "ambiguity": "未给出识别标准。"},
    {"term": "自由", "meaning": "本文中主要指言论自由，被说成“合法攻击”的庇护所，且除非完全剥夺一切言论自由便无法剥夺。", "evidence": "P017", "ambiguity": "未区分不同种类的自由，“一切言论自由”的范围未界定。"}
   ],
   "examples_and_targets": [
    "方方遭举报、被指用特权送亲属出境：提问者提供的事件语境（Q001），正文未提及、未表态，也未出现“方方”二字。",
    "“特朗普贪污”传言：作者假设的例子，用于反证（P009）。",
    "“方方收了美国钱”传言：作者举出的、讨厌方方的人所信的传言，用于同一反证（P009）。",
    "知识分子、精英阶层：作者批评的对象群体（P016）。",
    "“出狱时去杀ta全家”：作者举出的反例兼修辞（P023）。",
    "四种人（麻瓜、黑法师、白法师、灰法师）：作者自创的比喻分类（P036-P040）。",
    "“魔戒”“特洛伊木马”“黑魔法”：作者的比喻材料（P016、P020、P044等）。"
   ],
   "conditions": [
    "“纪实”的含义以作者对该词的重述为前提，正文未直接引用日记原文（P002）。",
    "P009 用“否则明天你也就可以……”的假设句式作反证。",
    "P010 的对象限定为“作为一名作家，一名吃了一辈子文字饭，而且确认自己有一定公共影响力的人”。",
    "P012-P015 是作者模拟并反讽的辩护话术，属引述/反讽，不是作者主张。",
    "P017 以“除非你完全的剥夺一切言论自由”为条件。",
    "P020 的建议以防止“被这种暗示性文字诱导作出证据和逻辑所不支持的判断”为目的。",
    "P028、P029 为 heading 中的极端断语（“活该”“罪有应得”），其适用情形本文未作限定。",
    "P053、P054 为作者的希望与追问，非事实断言。"
   ],
   "rhetoric_and_tone": "反讽、训诫与第二人称喊话混合：大量设问追问（“你看懂没有？！”“你说是不是？”），以“黑魔法/白法师/灰法师/魔戒/特洛伊木马”构成贯穿全篇的比喻体系；断言极端（“活该”“罪有应得”）又夹杂玩笑口吻（“别想着等你出狱时去杀ta全家——那是违法的”“好啦好啦，这篇主要是讲魔戒好伐啦”）；结构为“1）2）3）”三条行动建议。",
   "unresolved_questions": [
    "正文未点名“方方”，只用“她”“一名作家”，提问所指对象与正文讨论对象是否同一，需研究者判断。",
    "Q001 所指的“遭举报、被指用特权送亲属出境”一事，正文完全未提及、未表态。",
    "作者对“纪实”的界定是否等同方方日记原文用法，正文未引用日记原文，需回查。",
    "P012-P015 的辩护话术是作者模拟还是引用真实文本，本文未说明说话人。",
    "P016“知识分子、精英阶层”的具体所指不明。",
    "四分类与“魔戒”“黑魔法”的关系、“控制黑白灰比例”的具体做法，本文未给出判据。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人看方方日记的时候犯了一个逻辑错误。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "我收到了这样那样的传言，我都相信得很，然后我认为ABC", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "这个“纪实”，完全没有包含任何“那些传言本身所说的内容都是事实”的证言功能。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "也根本不包含任何“为武汉人仗义执言”的功能。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "否则明天你也就可以根据你所相信的“特朗普贪污”的传言“仗义执言”了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "是不是真的没意识到“我听说了这些传言，我很相信”的表态是一种怎样的“充满智慧”的行为。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "我没有义务、也不可能为别人的个人判断负责。", "relation": "context"},
    {"key": "E8", "paragraph_id": "P016", "quote": "知识分子、精英阶层，只需要非常初级的训练就能掌握这种言论自由黑魔法。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "批评ta们是没有意义的，因为这是天意留下的特权", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "除非你完全的剥夺一切言论自由。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P018", "quote": "自由天生就是“合法攻击”的庇护所。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "形成对逻辑关系的高度敏感，学会分辨这种特洛伊木马。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P025", "quote": "别人有“误导权”，你懂不懂？有“表达含糊权”，你懂不懂？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P027", "quote": "这意味着“变得不容易被误导”是你自己的义务。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P028", "quote": "被误导，就是你活该。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P037", "quote": "第一种，根本就没意识到还有这个“拳法”的麻瓜。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P040", "quote": "第四种，对敌人用黑魔法，对朋友不用的灰法师。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P043", "quote": "事实上，最白的白法师也只是很淡很淡的灰法师而已。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P044", "quote": "因为这枚“无责任的引诱ta人为自己的目的、理想服务、付账”的魔戒，非人力所能抵挡。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P048", "quote": "只有白法师能最大程度的排除和对抗黑魔法本身对事实和真理的扭曲", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P049", "quote": "施术者自己会产生越来越强烈的幻觉。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P050", "quote": "里面装载的都是想要绕过证据、逻辑和分析，直接诉诸感情、情绪和本能的东西。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P053", "quote": "我希望有一天你学会了这黑魔法，开始尝到或者目睹这枚魔戒的威力的时候，能稍微有点抵抗力。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P054", "quote": "人得到世界，却失去自己的神志——也就是生命本身——值得吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["言论与传播伦理", "公共写作与知识分子", "逻辑与认知防护"],
   "issue_candidates": ["“纪实”与证言功能的区分", "含糊表达与误导的责任分配", "言论自由的边界与滥用", "信源甄别与自我防护"],
   "text_function_candidates": ["评论", "论辩", "训诫", "答疑（部分回应）"],
   "object_candidates": ["方方（正文未点名，仅提问出现）", "作家/知识分子/精英阶层", "白法师、黑法师、灰法师（比喻主体）"],
   "working_keywords": ["纪实", "特洛伊木马", "黑魔法", "白法师", "灰法师", "魔戒", "误导权", "表达含糊权", "信源", "证言功能"]
  },
  "notes": "正文无图片节点。提问问的是方方遭举报及特权送亲属出境一事，正文未提此事、未点名方方，主题落在日记“纪实”的含义与言论责任上，问答之间存在错位。brief 字段为正文语句摘录，仅作导航。"
 },
 "b706166b": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么中国刀在国际上不如日本刀出名？”，属提问者设定的比较对象（中国刀／日本刀／国际评价）。作者没有从刀剑工艺层面作答，而是给出一个文明规模与专业分化的解释：中国以文官政治和官僚制度立身，不靠军功贵族与一夫之勇（P001-P005）；欧美日本构成另一个“专业”，好刀好枪是那一边的专业共鸣，中国的专业如今只剩自己一个学生／教授，且无法“转系”（P006-P009）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出前提：中国以文官政治与早熟官僚制度为立身之本，军功贵族式的立身之本只能支撑山川之险的州县规模实体。", "role": "reason"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "论证中国问题不是一夫之勇能解决的：春秋战国诸侯已在思考王道与霸道之别、喊出“要学万人敌”；中国的规模必须靠意识形态赢得人心支持，不能靠武力恐惧维持。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "给出答案要害：作为“国际”的欧美日本是另一个专业，好刀好枪是他们的专业共鸣；中国所在的专业只剩自己一个学生／教授，专业不同关注自然不同，而且想转系都不行。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国是以文官政治和惊人早熟的官僚制度作为立身之本，而不是以军功贵族为立身之本。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为军功贵族式的立身之本只能支撑四面有山川之险的州县规模政治实体，根本不适用于中国这种天下三十几州、绵延万里的生存状态。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称一夫之勇解决不了中国的问题，并举春秋战国诸侯思考王道与霸道之别、“要学万人敌”的需求为证。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言中国的规模必须依靠某种意识形态来赢得人心主动的支持，不可能靠武力支撑的恐惧维持运转；武勇只能治乡县，仁孝才有希望治天下。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把答案“要害”归于专业分化：作为“国际”的欧美日本是一个专业，好刀好枪是他们的专业共鸣；中国所在的专业目前只剩自己一个学生／教授，以前的同窗都已“挂在墙上”。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为专业不同关注的东西自然不同，而且中国想“转系”都不行。", "evidence": ["E9", "E10"]}
   ],
   "argument_steps": [
    "前提一：中国以文官政治与早熟官僚制度立身，不以军功贵族立身（P001）。",
    "前提二：军功贵族式实体只适用于州县规模，不适用于中国的规模（P002）。",
    "理由：一夫之勇解决不了中国问题；春秋战国诸侯已在思考王道霸道、“要学万人敌”（P003）。",
    "推论：中国必须靠意识形态赢得人心支持，不能靠武力恐惧；武勇只能治乡县，仁孝才有希望治天下（P004、P005）。",
    "转折到“国际”：欧美日本是另一个专业，好刀好枪是其专业共鸣（P006）。",
    "对照：中国的专业只剩自己一个学生／教授，以前的同窗都“挂在墙上”（P007）。",
    "结论：专业不同关注不同，而且想转系都不行（P008、P009）。"
   ],
   "concept_usage": [
    {"term": "专业", "meaning": "比喻不同文明／国家群体长期专注并互相评价的领域与共鸣点；中国与欧美日分属不同“专业”。", "evidence": "P006", "ambiguity": "“专业”如何划分、边界何在，本文未定义。"},
    {"term": "“国际”", "meaning": "作者加引号使用，指以欧洲、美国、日本为主体的评价圈。", "evidence": "P006", "ambiguity": "“国际”是否只含欧美日本、是否包含其他地区，本文未说明。"},
    {"term": "万人敌", "meaning": "作者引诸侯“要学万人敌”的说法，指超越一夫之勇的能力需求。", "evidence": "P003", "ambiguity": "正文未标明出处（通常指《史记》项羽语），需外部核查。"},
    {"term": "文官政治／军功贵族", "meaning": "作者对比的两种立身之本：前者依托官僚制度与意识形态，后者依托军功与个人武勇。", "evidence": "P001", "ambiguity": "两者的历史适用范围与转型时点本文未说明。"},
    {"term": "转系", "meaning": "比喻中国改变自身所属“专业”、转向欧美日本那一套评价体系。", "evidence": "P009", "ambiguity": "为何“不行”只给了一句断语，未给出理由。"}
   ],
   "examples_and_targets": [
    "中国刀与日本刀：提问者设定的比较对象（Q001），正文未从器物或工艺层面比较。",
    "欧洲、美国、日本：作者所指“国际”的构成，也是“好刀好枪”那一专业的共鸣者（P006）。",
    "春秋战国时代的诸侯：作者的历史叙述，用于说明“要学万人敌”的需求（P003）。",
    "王道与霸道：作者引述诸侯思考的区分（P003）。",
    "“挂在墙上的同窗”：作者的比喻，指中国所在专业中已消亡的其他成员（P007）。",
    "“转系”：作者的比喻（P009）。"
   ],
   "conditions": [
    "P002 以“后者只能支撑……根本不能适用于中国这种……”的限定句式，把军功贵族模式限定在州县规模。",
    "P005 “仁孝才有希望治天下”保留“有希望”的或然语气，非断言必然。",
    "P006 用引号限定“国际”的所指为欧洲、美国和日本。",
    "P009 的“你”是对读者的假设性指称（“你想转系都不行”）。"
   ],
   "rhetoric_and_tone": "文言化的短句与对仗（“武勇只能治乡县，仁孝才有希望治天下”），以“专业／转系／同窗挂在墙上”构成比喻链，语气冷峻、略带调侃（“而且很遗憾”）；全文未直接描述刀剑本身，而是把提问转为文明规模与评价体系的解释。",
   "unresolved_questions": [
    "正文未直接回答中国刀与日本刀在工艺、使用或传播上的差异，提问的器物层面问题未被处理。",
    "“以前那些同窗都已经挂在墙上了”所指的具体文明／政治实体未说明，需研究者判断。",
    "“要学万人敌”的出处与语境本文未标注，需外部核查。",
    "“国际”是否只指欧美日本、中国所在“专业”还有哪些成员，本文未说明。",
    "“中国是以文官政治……作为立身之本”是高度概括的历史断言，本文未提供依据，需外部核查。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中国是以文官政治和惊人早熟的官僚制度作为立身之本，又不是以军功贵族为立身之本。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "后者只能支撑四面有山川之险的州县规模的政治实体", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一夫之勇，无非十人敌百人敌，这完全不能解决中国的问题。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "喊出了“要学万人敌”的需求。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "中国的规模必须依靠某种意识形态来赢得人心主动的支持，而不可能靠武力支撑的恐惧来维持运转。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "武勇只能治乡县，仁孝才有希望治天下。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "作为“国际”的欧洲和美国和日本是一个专业的，好刀好枪是他们的专业共鸣。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "而中国所在的专业，目前只剩下自己这一个学生/教授。以前那些同窗都已经挂在墙上了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "大家专业都不同，当然关注的东西不一样。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "而且很遗憾，你想转系都不行。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["历史与文明比较", "军事与社会结构", "国际评价体系"],
   "issue_candidates": ["中国刀与日本刀的国际知名度差异", "文官政治与军功贵族的分野", "文明规模与治理方式"],
   "text_function_candidates": ["答疑", "解释", "评论"],
   "object_candidates": ["中国", "欧洲", "美国", "日本", "春秋战国诸侯"],
   "working_keywords": ["文官政治", "官僚制度", "军功贵族", "万人敌", "王道", "霸道", "专业", "转系", "国际"]
  },
  "notes": "正文无图片节点。brief 为正文语句摘录，仅作导航。提问问的是刀的知名度，正文从文明规模与“专业”分化角度作答，未涉及刀剑工艺。"
 },
 "e266c1dd": {
  "analysis": {
   "question_context": "提问者（Q001）问“铲屎官们都说猫惧怕出门，为什么说猫是野生动物的杀手？”，即就“猫怕出门”与“猫是野生动物杀手”两个流行说法发问。作者未讨论猫捕杀野生动物，只用两行对照（“你眼中的出门：”“猫眼中的出门：”，两处对照内容由两张图片承担）加三句调侃作答：猫不是不爱出门，而是“野外之王”，只是不喜欢跟愚蠢的人类一起出门。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "设置“你眼中的出门”与“猫眼中的出门”两行对照；两行之下各有一张图片，对照内容未经核验。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "作者以调侃口吻断言：猫不是不爱出门，而是“野外之王”，只是非常不喜欢跟愚蠢的人类一起出门。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认“猫不爱出门”的说法，称猫是“野外之王”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为猫只是非常不喜欢跟愚蠢的人类一起出门。", "evidence": ["E2"]}
   ],
   "argument_steps": [
    "以两行对照（你眼中的出门／猫眼中的出门）预设人与猫对“出门”的理解不同，具体内容在两图中（P001、P002）。",
    "断言猫不是不爱出门，而是“野外之王”（P003）。",
    "把原因归于猫不喜欢跟愚蠢的人类一起出门（P004）。",
    "以“心累！！”收尾（P005）。"
   ],
   "concept_usage": [
    {"term": "出门", "meaning": "本文中被拆成“你眼中”与“猫眼中”两种理解，作者未在文字中说明其具体差别，差别由两张图片承担。", "evidence": "P001", "ambiguity": "两图的对照内容未核验，文字未说明猫眼中的“出门”具体指什么。"},
    {"term": "野外之王", "meaning": "作者对猫的称呼，用于否认“猫惧怕出门”。", "evidence": "P003", "ambiguity": "是修辞还是实指（如指猫的捕猎能力）本文未界定。"},
    {"term": "愚蠢的人类", "meaning": "作者拟猫的口吻对人类的戏称。", "evidence": "P004", "ambiguity": "为调侃修辞，非对人类的实质判断。"}
   ],
   "examples_and_targets": [
    "两张图片（IMG001、IMG002）：分别置于“你眼中的出门”与“猫眼中的出门”之后，是本篇对照内容的主要承担者，未经核验。",
    "提问者所说的“猫是野生动物的杀手”：提问者语境（Q001），正文未回应、未提供捕猎相关论据。"
   ],
   "conditions": [
    "P003 用“根本不是”的否定句式否认“猫不爱出门”。",
    "P004 用“只是”把原因限定为不喜欢跟人类一起出门。",
    "P001、P002 的对照是否成立依赖两张图片，文字本身未给出内容。"
   ],
   "rhetoric_and_tone": "极短篇，口语化、拟人化（代猫立言）、感叹号连用（“好吗！”“心累！！”），并调侃人类；主要信息以两张对比图承担，文字只作点题。",
   "unresolved_questions": [
    "图片未核验，需人工/多模态复核：IMG001、IMG002 的内容及其与“你眼中的出门／猫眼中的出门”两行的对应关系无法确认。",
    "提问所说的“猫是野生动物的杀手”（猫捕杀野生动物）正文未直接回答，也未提供任何捕猎或生态影响的论据。",
    "“野外之王”是修辞还是实指，本文未界定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "猫根本不是不爱出门，人家是野外之王好吗！", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "ta只是非常不喜欢跟愚蠢的人类一起出门！", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P001", "quote": "你眼中的出门：", "relation": "context"},
    {"key": "E4", "paragraph_id": "P002", "quote": "猫眼中的出门：", "relation": "context"},
    {"key": "E5", "paragraph_id": "P005", "quote": "心累！！", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宠物与动物行为", "网络问答调侃"],
   "issue_candidates": ["猫是否怕出门", "猫与野生动物捕杀的关系（正文未涉及）", "图文对照"],
   "text_function_candidates": ["答疑（未正面回应）", "调侃", "图文段子"],
   "object_candidates": ["猫", "铲屎官/人类"],
   "working_keywords": ["出门", "野外之王", "心累", "猫眼中的出门"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 2 个图片节点（IMG001、IMG002），图片内容未经核验，需图像核验；已读部分为正文文本。两行文字（P001、P002）是对图片的引题，缺少图片则对照内容不完整，故标 needs_reread。"
 },
 "3bf1a7c6": {
  "analysis": {
   "question_context": "提问者（Q001）问“男人维护女权是一种什么心理？”，暗含对男性支持女权之动机的追问。作者不讨论具体心理，而是先给出一套伦理命题的坐标（是否合我利益×我是否赞成，共A/B/C/D四类：P001-P005），把“只需要兽性”的A、C象限与“必须不为空”的B、D象限分开（P006、P007），最后把问题反过来抛给所有男性：为什么“对女权的维护”不该在B、D这两个象限里，并要求对方解释为什么不该（P008、P009）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "把个人面对伦理命题的情况按“是否符合我的利益”与“我是否赞成”分成A、B、C、D四类。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "断言A和C两个象限只需兽性；只要不是纯粹的直立畜生，B和D这两个象限必须不为空。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "把问题转向所有男性：为什么“对女权的维护”不该在B、D象限里，并要求解释为什么不该。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把所有伦理命题按“是否符合我的利益”和“我是否赞成”两组标准分为A、B、C、D四种情况。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言A和C这两个象限不需要人性，只需要兽性就够了。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言只要不是纯粹的直立畜生，B和D这两个象限必须不为空。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者向所有男性反问：为什么“对女权的维护”不该在B、D这两个象限里，并要求对方解释为什么不该。", "evidence": ["E6", "E7"]}
   ],
   "argument_steps": [
    "设定坐标：伦理命题按是否符合我的利益、我是否赞成分为A、B、C、D四类（P001-P005）。",
    "分类判断：A和C只需兽性，不需要人性（P006）。",
    "规范要求：只要不是纯粹的直立畜生，B和D两个象限必须不为空（P007）。",
    "转向提问语境：把“对女权的维护”放入这一框架，反问为什么它不该在B、D象限，并要求解释（P008、P009）。"
   ],
   "concept_usage": [
    {"term": "伦理命题", "meaning": "本文指个人可表态的伦理主张；其分类只看“是否符合我的利益”与“我是否赞成”。", "evidence": "P001", "ambiguity": "“利益”的范围（物质、社会、心理）与“赞成”的依据本文未说明。"},
    {"term": "象限", "meaning": "借坐标系说法指A/B/C/D四类组合。", "evidence": "P002", "ambiguity": "仅为分类比喻，未说明两类标准是否穷尽。"},
    {"term": "人性／兽性", "meaning": "作者用法：只为自身利益赞成或反对只需“兽性”；能违背自身利益或偏好则是“人性”的证明。", "evidence": "P006", "ambiguity": "未定义两者的判据，也未说明“人性”是否需要其他条件。"},
    {"term": "直立畜生", "meaning": "作者的贬称，指只在A、C象限行动的人。", "evidence": "P007", "ambiguity": "为修辞性贬称，无严格定义。"},
    {"term": "对女权的维护", "meaning": "本文的讨论对象，指男性对女权的支持立场；作者把它作为可放入B或D象限的伦理命题。", "evidence": "P008", "ambiguity": "未说明“维护”具体指哪些主张或行动。"}
   ],
   "examples_and_targets": [
    "无具体人物、事件或数据；全文只用A/B/C/D四象限的抽象分类。",
    "提问者的“男人维护女权是一种什么心理”：提问者语境（Q001），作者未直接回答该心理问题，而是把它改写为规范性的反问。",
    "标题“BD象限不为空”：作者命题的概括。"
   ],
   "conditions": [
    "P002-P005 以“符合／不符合我的利益”“赞成／不赞成”两组条件界定四类。",
    "P007 以“只要不是个纯粹的直立畜生”为条件，要求B、D不为空。",
    "P008 的对象范围为“所有的男性”。",
    "P009 要求持相反意见者作出解释（“解释一下，为什么不该？”），属诘问而非作者自答。"
   ],
   "rhetoric_and_tone": "极简、抽象、近乎公理化的分条陈述（A）B）C）D）），随后用带贬义的条件句（“纯粹的直立畜生”）与一个挑衅式反问收尾；把提问者对动机的猜疑转为要求对方举证的诘问。",
   "unresolved_questions": [
    "正文未直接回答“男人维护女权是一种什么心理”，只给出四象限框架和一个反问。",
    "“利益”的范围与“赞成”的依据本文未说明。",
    "“B和D这两个象限必须不为空”是经验断言还是规范性要求，本文未说明。",
    "未提供任何具体女权议题、行动或例证，故“对女权的维护”具体指什么无法确定。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "对个人来说，所有的伦理命题一共分为这么几种情况：", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "B）符合我的利益，但我不赞成；", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "D）不符合我的利益，但我赞成。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "其中A和C这两个象限不需要人性，只需要兽性就够了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "只要不是个纯粹的直立畜生，你的B和D这两个象限必须不为空。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "所以，有一个问题客观的摆在了所有的男性面前——为什么“对女权的维护”不该在这两个象限里？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "解释一下，为什么不该？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "性别议题", "概念框架"],
   "issue_candidates": ["男性支持女权的动机", "利他与利益的关系", "伦理立场的分类"],
   "text_function_candidates": ["论辩", "定义", "诘问"],
   "object_candidates": ["男性", "女权（维护女权者）"],
   "working_keywords": ["伦理命题", "象限", "人性", "兽性", "直立畜生", "BD象限不为空"]
  },
  "notes": "正文无图片节点，正文共9段（另含1个空段，lexical 计数10）。brief 为正文语句摘录，仅作导航。作者未回答提问的心理问题，而是给出分类框架并向反对者反问。"
 },
 "4adfa0a0": {
  "analysis": {
   "question_context": "提问者（Q001）问“中国人离开中国后很容易被同化吗？”。作者先声明转载许可（P001、P002），随即直接否定“容易同化”之说：中国人、犹太人都是出了名的难同化（P003-P011）；再借“现在中国还有什么文化”引出对中国文化的界定（P012-P014）；随后区分微观原因（历史记忆使外来体系“内化失败”）与宏观原因（超大规模本体的“热力学”机制，P015-P039）；纠正“对方消失、我们岿然不动”的错觉（P040-P045）；列举大量外来事物（P046-P056）；最后作出“中国文化总会同化外来文化”的判断并对《外国人居留条例》表示不担忧，转而劝告国人不要以“难被同化”为麻木顽固的自豪，而应大胆开放学习（P057-P087）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开头回应转载提醒：作者称已说过许可，即使未注明转载也一并许可。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "否定“容易同化”：中犹都出了名难同化（二代被同化、三四代回来寻根）；文化背景强势到“人家还不信你真的同化了”；从书本上可能赞同某些逻辑，但接触其丑陋另一面后会意识到中国文化不是白给的；将来中国追上超过美国后会更明显，“谁同化谁还很难说”。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P012", "P013", "P014"], "summary": "借“现在中国还有什么文化”引出对中国文化的界定（P014 为引用块）：中国人认识事物、做决策的特殊共性及其互动机制、评价机制，不是祭祖、民乐之类，与用何种语言体系表达关系甚微；以华人移民“送礼而非找工会律师”的决策模式为例。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "解释中犹难同化的微观机制：常不自觉觉得别人的处事方式短视、考虑欠妥；悠久历史记忆使脑海里浮现未防住的后果（“这事岳飞干过，挂了”），于是外来体系内化失败；并声明这不见得是值得骄傲的属性，只是客观如此。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "自我限定：前述“因古老民族内心隐生的傲慢而难同化”只是特定中国人和犹太人的微观动力学原因，不是宏观社会学视角的“热力学”原因；两种文明的抗同化原因完全不同。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "以白颜料比喻犹太文明：沾染的部分被认定不再属于犹太民族而统统切除，所以犹太人一直是白色（顶多变象牙白）。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "以白颜料比喻中国文明：本体极大，遇到其他颜色就抱进怀里糅合搅拌，一次次变成更大一团的新颜色，最终成为池塘大的“黑色”；这才是宏观角度“中华文明难以被同化”的原因。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045"], "summary": "纠正错觉：看似对方“同化失败”地消失、我们岿然不动，事实是我们几乎没有抗拒、以近乎“自卑”的心态狂热吸收对方，只因本体太大，结果总是“我们略微变色，而对方消失在了我们之中”。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "列举青花瓷、“爸爸”“妈妈”、“什么”、骑马与马镫、色即是空、罗汉菩萨、阎王、地狱等，反问有几个中国人意识到这些原本不是中华文明的一部分。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063"], "summary": "结论：中国的“难同化”不靠犹太人式“上帝选民”的绝对高傲与坚决抗拒，而靠超大人口与社会规模，能以“自卑心态”仰慕异文明却仍然壮大；因此“怕被同化”不适用于中国这个东方巨兽，相关恐惧是欧洲式的。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076"], "summary": "进一步论证：这种恐惧到晚清才随西方文化传入；此前闭关锁国是自信得太过头；中国只会变成新的中国，是逻辑性免疫；世人称中国“保守”是本末倒置，中国一向是世界上最激进的文明，以历代制度革新为证。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087"], "summary": "总结与劝诫：作出“中国文化总会同化外来文化”的判断，对《外国人居留条例》毫不担忧；劝人不要以“我们不容易被同化”为麻木顽固的自豪，而应大胆、贪婪、“毫无底线”地学习；若为保持本色闭关自守，就辜负了“极难被同化”的种族天赋，也抛弃了“混一宇内之志”；并引“那位设计师”的“开放、开放、坚定不移的开放”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者主张中国人、犹太人都是出了名的难同化，并以二代被同化、三四代回来寻根返乡为例反问“何来‘容易同化’一说”。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为从书本上或许会逻辑性地赞同某些中国文化所不赞同的逻辑，但接触其丑陋的另一面后，会意识到中国文化也不是白给的。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者预测，尤其在将来中国逐渐追上和超过美国、美国霸权破灭失去超常利益之后，中国文化没当初看小册子所想的那么简单会越来越明显；到底最后谁同化谁还很难说。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者引述（P014 引用块，说话人未标明）对中国文化的界定：中国人认识事物、做决策的特殊共性，及其互动机制与评价机制；不是祭祖、民乐之类，也与用何种语言体系表达关系甚微。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中犹难同化的微观原因是：常不自觉觉得别人的处事方式短视、考虑欠妥，且悠久历史记忆使其联想到未防住的后果，于是外来体系“内化失败”、同化被阻挡。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明这个问题不见得是很值得骄傲的属性，只是客观如此。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者自我限定：“因古老民族内心隐生的傲慢而难同化”只是特定中国人和犹太人的、微观社会学视角的动力学原因，不是宏观社会学视角的“热力学”原因；犹太文明与中国文明抗同化的原因完全不同。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以白颜料比喻犹太文明抗同化：被沾染的部分被认定不再属于犹太民族而统统切除，所以犹太人一直是白色（顶多变象牙白）。", "evidence": ["E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“一大团白”比喻中国文明：遇到其他颜色会抱进怀里糅合搅拌，一次次变成更大一团的新颜色，最终成为池塘大的“黑色”；这才是宏观角度“中华文明难以被同化”的原因。", "evidence": ["E17", "E18", "E19", "E20"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者纠正“对方消失、我们岿然不动”的观感：我们几乎不抗拒、以近乎“自卑”的心态狂热吸收对方，只因本体太大，结果总是“我们略微变色，而对方消失在了我们之中”。", "evidence": ["E21", "E22"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列举青花瓷、称呼、骑马、马镫、佛语、罗汉菩萨、阎王、地狱等，主张许多今天被视为中国文化的东西原本是外来的。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国的“难同化”不是靠犹太人式“上帝选民”的绝对高傲与坚决抗拒，而是因超大人口与社会规模，能以“自卑心态”仰慕异文明却仍壮大；这种“自卑”换其他民族都致命，唯独中国凭借超大规模的本体免疫。", "evidence": ["E26", "E27", "E28"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者说自己几乎从不担心中国人“崇洋媚外”“数典忘祖”，认为那是从欧美意识形态继承来的欧洲式恐惧，是只有匈牙利人、法国人才需要担心的问题；“怕被同化”不适用于中国这个东方巨兽。", "evidence": ["E29", "E30"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种恐惧到晚清才第一次随西方文化传入；此前闭关锁国不是害怕外来文明，而是自信得太过头、不想被质量不行的叫卖打扰。", "evidence": ["E31"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国无论怎样暴烈的变革、怎样“丧失自我”，都只会变成新的中国而绝不会变成“异民族”（逻辑性的免疫）；世人说中国“保守”是本末倒置，中国实际上一向是世界上最激进的文明，文化上的“稳定”是无需努力自然就有的天然属性。", "evidence": ["E32", "E33"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以周代殷商至民国肇造的历史序列为证，主张每次都是奔着开创而去、干的是一马当先革旧鼎新的新事，“中国文化守旧”之说几乎是睁眼说瞎话。", "evidence": ["E34", "E35"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者作出“中国文化总会同化外来文化”的判断，并据此对《外国人居留条例》毫不担忧：中国是敞开了任人“同化”，最后一定是稍稍变化而终归抱元守一的中国。", "evidence": ["E36", "E37"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者劝诫国人：不要以“我们内心骄傲、别人都是小孩子，所以我们不容易被同化”变得麻木顽固甚或以之为自豪；身为中国人有最大的资本“异化”，应大胆、贪婪、“毫无底线”地学习；若为“保持民族的本色”而闭关自守，就辜负了“极难被同化”的种族天赋，也抛弃了最大的本色——混一宇内之志。", "evidence": ["E38", "E39", "E40"]},
    {"claim_id": "C019", "claim_type": "author_reported", "attribution": "cited_source", "modality": "asserted", "statement": "作者引述“那位设计师”的话作结：开放、开放、坚定不移的开放（正文未点明此人是谁）。", "evidence": ["E41"]}
   ],
   "argument_steps": [
    "开头声明转载许可（P001、P002）。",
    "直接否定“容易同化”：中犹都出了名难同化，被同化者后代又回来寻根；文化背景强势到同化不被承认（P003-P007）。",
    "让步与转折：书本上可能逻辑性赞同某些外来逻辑，但接触其丑陋一面后评价改变；将来中美地位变化后更明显（P008-P011）。",
    "借“现在中国还有什么文化”引出中国文化的定义（引用块）：决策与认识事物的共性，而非文化符号（P012-P014）。",
    "微观解释：历史记忆使人联想到未防住的后果，外来体系内化失败（P015-P020）；并声明该属性不见得值得骄傲（P021）。",
    "自我限定：前述原因是特定人群的微观动力学原因，不是宏观“热力学”原因；中犹抗同化原因完全不同（P024-P027）。",
    "比喻一：犹太人是被沾染即切除的白颜料，故一直白（P028-P031）。",
    "比喻二：中国是极大一团白，遇色则拥抱糅合，越变越大，终成池塘大的“黑色”（P032-P039）。",
    "纠正错觉：不是对方同化失败，而是我们几乎全部吸纳，只因本体太大（P040-P045）。",
    "例证：青花瓷、爸爸妈妈、什么、骑马、马镫、色即是空、罗汉菩萨、阎王、地狱等原本外来（P046-P056）。",
    "结论：难同化源于超大规模本体而非“上帝选民”式高傲；“怕被同化”是晚清传入的欧洲式恐惧，不适用于中国（P057-P065）。",
    "历史论证：中国只会变成新的中国，是逻辑性免疫；说中国守旧是本末倒置，历代制度革新为证（P066-P076）。",
    "总结与劝诫：对《外国人居留条例》不担忧；不要把“难被同化”当作麻木顽固的自豪，应大胆开放学习；闭关自守则辜负种族天赋与“混一宇内之志”（P077-P085）。",
    "引“那位设计师”的话收尾：开放、开放、坚定不移的开放（P086、P087）。"
   ],
   "concept_usage": [
    {"term": "同化", "meaning": "本文中指外来文化对中国个体与中华文明的改变与吸纳；作者区分微观（个体难被同化）与宏观（文明整体“难以被同化”）两个层次。", "evidence": "P015", "ambiguity": "作者在两个层次上使用同一词，未给出统一定义。"},
    {"term": "中国文化", "meaning": "文中引用块界定为中国人认识事物、做决策的特殊共性及其互动机制与评价机制，而非祭祖、民乐等符号。", "evidence": "P014", "ambiguity": "该界定出自引用块，说话人未标明；与作者另一篇《文化》正文高度重合。"},
    {"term": "微观社会学视角的动力学原因／宏观社会学视角的“热力学”原因", "meaning": "作者自造的方法论区分：前者指个体因历史记忆而抗拒内化，后者指文明整体因规模而吸纳外来者。", "evidence": "P025", "ambiguity": "两个视角的界定与关系本文未展开。"},
    {"term": "种族天赋／物理免疫／逻辑性的免疫", "meaning": "比喻性说法，指中国因超大规模而对“失去本色”免于风险。", "evidence": "P058", "ambiguity": "属修辞还是实指，本文未界定；三处说法是否同义亦未说明。"},
    {"term": "自卑", "meaning": "作者加引号使用，指近乎自卑地仰慕异文明、狂热吸收对方的心态。", "evidence": "P042", "ambiguity": "作者自己加引号，未说明与通常义的区别。"},
    {"term": "混一宇内之志", "meaning": "作者称其为中华民族最大的本色。", "evidence": "P085", "ambiguity": "未给出出处与具体所指。"},
    {"term": "保守／激进", "meaning": "作者反转常识用法：世人称中国“保守”，作者称中国一向是世界上最激进的文明。", "evidence": "P067", "ambiguity": "未界定衡量标准。"},
    {"term": "那位设计师", "meaning": "P086 中引述“开放、开放、坚定不移的开放”的说话人。", "evidence": "P086", "ambiguity": "正文未点名，需研究者判断所指。"}
   ],
   "examples_and_targets": [
    "犹太人：作者类比与例证（白颜料比喻；安息日、逾越节无酵饼、妥拉、通婚等连串反问，P029-P031）。",
    "中国人：作者类比（极大一团白颜料、池塘大的“黑色”，P033-P038）。",
    "青花瓷、中国人称呼父母为“爸爸”“妈妈”、“什么”、赵武灵王之前无人骑马、大汉骑兵无马镫、色即是空、罗汉菩萨、阎王、地狱：作者列举的“原本外来”例证（P047-P055）。",
    "岳飞、秦桧：作者以引语式例子说明历史记忆导致内化失败（P018、P019）。",
    "匈牙利人、法国人：作者举例说明“欧洲式恐惧”的适用范围（P061）。",
    "鲸鱼学企鹅怕海豹：作者类比，说明中国人不必跟着怕（P062）。",
    "十万吨的巨轮：作者类比，说明中国文化“想不稳定”很难（P069）。",
    "周代殷商、强秦代周、汉代秦兴、隋唐代汉、宋代旧唐、明逐元虏、明亡清兴、民国肇造：作者的历史叙述与论据（P071）。",
    "共产主义：作者称“现在是先锋到挑战人类经验的共产主义”（P073）。",
    "《外国人居留条例》：作者评论对象，表示毫不担忧（P078）。",
    "“那位设计师”：作者引述对象，正文未点名（P086）。",
    "提问者所问“中国人离开中国后是否容易被同化”：提问者语境（Q001），正文以否定回答之。"
   ],
   "conditions": [
    "P016 用“常常不自觉”限定该心理机制的常态性。",
    "P021 用“不见得是……只是客观如此”限定了对“难同化”的评价。",
    "P025、P026 对前述原因作范围限定：只是特定人群、微观视角。",
    "P033 以“假设我们最早也是白色的”引出比喻，属假设性说明。",
    "P038 用“我们有极大的把握”表示高概率而非确定。",
    "P042 用“几乎没有抗拒对方的任何影响”作程度限定。",
    "P058 称这是“天生有一种神奇的种族天赋”。",
    "P060 以“换了任何一个其他的民族……唯独中国……对此免疫”作对比限定。",
    "P061 用“几乎从不担心”表示作者个人态度而非事实断言。",
    "P070 把“落后个上百年”限定为“在几千年历史里只是短短的一瞬”。",
    "P078 用“毫不担忧”表态；P082 用“无论怎样开放”作全称条件。",
    "P084 用“到最后结果一定是”作预测性断言；P085 用“如果……而闭关自守，就……”作条件句。",
    "P014 为结构上的引用块（field=quote），其内容是否作者自引，本文未说明。"
   ],
   "rhetoric_and_tone": "长篇论辩与训诫：以“白颜料／池塘／东方巨兽／十万吨巨轮”构成比喻体系，密集使用反问与激将（“你信不？”“是不是不信？”“现在有几个中国人意识得到……？”“你跟着怕什么？”），夹杂口语与自嘲（“OK，不知道为啥这个答案这么火爆”“我写得太随便了”）；以“我们”的第一人称共同体口吻贯穿；结尾转为对读者的劝诫与动员；文中有两处指向其他知乎问题的裸标题（P013、P023）和一段引用块（P014）。",
   "unresolved_questions": [
    "P013、P023 为“⚠lexical未覆盖片段”，正文中是两个指向其他知乎问题的裸标题（“如何理解中国文化？”“中国有哪些逆天的文物？”），其功能（链接或引用）本文未说明。",
    "P014 为结构上的引用块，说话人未标明；其内容与作者另一篇《文化》正文几乎一致，是否作者自引需核查（初读不做跨文章归纳）。",
    "“那位设计师”未点名，所指需研究者判断。",
    "历史断言需外部核查：晚清才传入“怕被同化”的恐惧、闭关锁国的原因、历代制度列举、“唯一传承至今的古文明”等，本文均未提供出处。",
    "具体事实断言需外部核查：“青花瓷可是中东来的”“‘什么’可恐怕并不是《诗经》所用的中文”“赵武灵王之前，中国是没有人骑马的”“大汉骑兵骑马，没有马镫”等（作者用“恐怕”“可不是什么‘正统’的叫法”等限定义表述）。",
    "P075、P076 中“似乎没有啥改变”加引号，是否为某种常见说法，本文未说明。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "中国人、犹太人都是出了名的难同化，甚至有二代被同化了、一句中文都不会说了，到三代、四代又回来寻根返乡的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "何来“容易同化”一说？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "如此强势的文化背景，你想同化，人家还不信你真的同化了呢。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "你立刻会意识到中国的文化也不是白给的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "尤其是在将来中国在各个方面逐渐追上和超过美国、而美国的霸权破灭失去相关的超常利益之后", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "到底最后谁同化谁，还很难说。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "所谓的中国文化，是指中国人认识事物的一种特殊共性、中国人做决策的一种特殊共性。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "完全不是什么祭祖、民乐之类的东西。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "因为ta们常常不自觉的觉得异于自己处事方式的其他做法很短视、考虑欠妥。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "想到了这些，这些体系和应对逻辑就会内化失败，同化就被阻挡了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "这个问题，不见得是一个很值得骄傲的属性，只是客观如此罢了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P025", "quote": "那只是特定的中国人和犹太人不容易被同化的原因", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P026", "quote": "这不是犹太文明和中国文明不容易被外来文化同化的宏观社会学视角的“热力学”原因。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P027", "quote": "实际上，犹太文明抗同化的原因和中国文明抗同化的原因是完全不同的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "ta们会把那些被染灰的、染蓝的、染红的、染黄的……统统切除。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P031", "quote": "犹太人原来是白色的，后来也一直都是白色的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P033", "quote": "假设我们最早也是白色的，但是我们是一大团白——极大极大的一大团白。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P034", "quote": "不，我们会把那团蓝色抱进怀里，糅合搅拌，最后变成更大一团的“极淡的蓝白色”。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P037", "quote": "一次又一次，我们已经变成了池塘那么大的一团的望之如同深渊一般的神秘的“黑色”。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P039", "quote": "这才是从文明的宏观角度来看，“中华文明难以被同化”的原因。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P042", "quote": "我们几乎是抱着一种近乎“自卑”的心态，把对方看作“先进”“强大”的代表热切的拥抱了，狂热的吸收了", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P043", "quote": "结果都是“我们略微变色，而对方消失在了我们之中”。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P047", "quote": "青花瓷可是中东来的；", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P055", "quote": "地狱，并不是中国本土自生出来的。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P056", "quote": "现在有几个中国人意识得到这些“原本不是中华文明的一部分”？", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P057", "quote": "中国的“难同化”，不是靠犹太人那样本着内心“上帝选民”的绝对高傲，对外界影响的持之以恒的坚决抗拒而造成的。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P058", "quote": "它可以时常抱着一种足以令其他小民族亡国灭种的“自卑心态”去“仰慕”异文明，到最后却是它活蹦乱跳的活下来了、而且更加壮大。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P060", "quote": "唯独中国凭借超大规模的本体对此免疫。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P061", "quote": "这是一种无意识的从欧美的意识形态里继承而来的欧洲式的恐惧，是只有匈牙利人、法国人才需要担心的问题。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P063", "quote": "“怕被同化”本身干脆是不适用于中国这个东方巨兽的。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P064", "quote": "你会发现这种恐惧是到晚清才第一次随着西方文化传进来的“新艺能”。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P066", "quote": "都只会变成新的中国，而绝不会变成一个“异民族”——它对此是逻辑性的免疫。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P067", "quote": "中国实际上一向是世界上最激进的文明。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P071", "quote": "周代殷商，分封天下；强秦代周，乃有郡县；", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P074", "quote": "从哪里去谈“中国文化守旧”？——这几乎是睁眼说瞎话。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P077", "quote": "看明白了这一点，你就能看明白为什么我会作“中国文化总会同化外来文化”这样的判断。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P078", "quote": "这也是为什么我对《外国人居留条例》毫不担忧。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P081", "quote": "其实身为中国人，你是有最大的资本“异化”的，这是你身为中国人最大的财富，不要辜负这一份天赐。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P084", "quote": "只管大胆的、贪婪的、“毫无底线”的学习，到最后结果一定是“别人变得和你一样”。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P085", "quote": "而且恰恰是抛弃了中华民族最大的本色——混一宇内之志。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P086", "quote": "所以，那位设计师会说——开放、开放、坚定不移的开放。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P001", "quote": "谢谢各位提醒我有一样的回答，不过我已经说过这是许可的。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文明比较与文化认同", "社会结构与规模效应", "历史评论"],
   "issue_candidates": ["中国人／中华文明是否容易被同化", "文化符号与文化本体的区分", "外来文化对中国的影响", "对外开放与民族本色"],
   "text_function_candidates": ["答疑", "论辩", "评论", "劝诫"],
   "object_candidates": ["中国人", "犹太人", "中华民族", "美国", "《外国人居留条例》", "那位设计师（未点名）", "匈牙利人", "法国人"],
   "working_keywords": ["同化", "反同化", "白颜料", "中华文明", "犹太文明", "热力学原因", "种族天赋", "混一宇内之志", "文化符号", "开放"]
  },
  "notes": "正文无图片节点。P013、P023 在阅读包中标注“⚠lexical未覆盖片段”，正文中是两个指向其他知乎问题的裸标题；P014 为结构上的引用块（field=quote），与作者另一篇《文化》正文高度重合，本文中作为论证基础被引用。brief 为正文语句摘录，仅作导航。"
 },
 "64fda1e3": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何理解中国文化？”。作者借题给出对“文化”的一般界定：文化本质上是“一群人对于决策机制的群体共识”，而音乐、春联、京戏、祭祖、书法、篆刻、诗词等只是文化的符号与产品（P002-P004）；以“工厂—声音—罐头”的比喻说明外人只能接触符号、工人熟悉的惯例与厂规才是本体（P005-P013）；据此界定中国文化为中国人认识事物、做决策的特殊共性（P016-P020），并主张中国文化几乎没有任何显著改变，其本体是勤俭、重视教育、稳扎稳打这类处事本能与“千千万万的句子”交织出的共性（P022-P047）；最后提出文化依赖于土地而非人种的假设性说法（P048）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "提出界定：文化是“一群人对于决策机制的群体共识”，而特色音乐、春联、京戏、祭祖、书法、篆刻、诗词等是文化的符号与产品。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "以工厂作比：外人只能听声音、吃罐头；工人眼里的惯例、厂规、内部笑话才是日常；没人（包括厂长）知道厂里到底有多少惯例和悄无声息的传统，其中甚至很多自相矛盾。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "工厂换业务后声音与产品改变，外人以为啥都变了；其实工艺、决策机制、部门结构变化甚微——对这些的共同认知才是文化。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "指出研究文化应紧盯“如何理解事物、如何决策”；由此界定中国文化为中国人认识事物、做决策的特殊共性，并强调与语言体系关系甚微；以华人移民“送礼而非找工会律师”的决策模式为例。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "反驳“中国文化沦丧／断根”之说：作者称这样说的人不知道自己在说什么；事实上中国文化几乎没有任何显著改变，勤俭、首选受教育、避免冒险等处事本能才是本体；马褂辫子之事“算个屁大的事”。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044"], "summary": "列举大量被作者称为“这才是中国文化”的句子（部分以“blar”省略），并主张这些千千万万的句子交织出中国人的共性，使中国人之间有特殊的交流前提，影响集体行动的走向与可选策略范围。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P045", "P046", "P047"], "summary": "对照美日英俄：中国人觉得不可接受的事、显然首选的方案都与之不同；这才是文化的本体与要害，其余只是影子、气味、边角余料。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P048", "P049", "P050"], "summary": "提出文化甚至不依赖于中国人、而依赖于中国这块土地的假设：若一万年前是一群印度人在此繁衍至今，其行为方式将与现在的中国人极其近似，与人种无关；并以“中国有哪些逆天的文物？”引出文化符号与文化的例子。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张文化本质上就是一群人对于决策机制的群体共识。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者主张特色音乐、春联、京戏、祭祖仪式、书法、篆刻、诗词等都不是文化，而是文化的符号、文化的产品。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以工厂比喻说明：外人只能通过声音和产品接触一个群体，而工人眼里的惯例、厂规等才是文化本体；且没有任何人（包括厂长）知道厂里有多少惯例和悄无声息的传统。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张工厂换业务后声音与产品改变，但工艺、决策机制、部门结构变化甚微；对这些的共同认知才是文化。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张真正研究文化的人紧盯文化如何理解事物、如何做出决策，而不是视觉听觉之类的感官符号。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“所谓的中国文化”为中国人认识事物、做决策的特殊共性，它带来不同的互动机制、组织关系、应对方案与评分制度；不是祭祖、民乐之类，与用何种语言体系表达关系甚微。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以华人移民的例子说明：哪怕想法全用英文想、全程没有闪过“中国”念头，“送礼而不是找工会律师”这种决策模式也非常中国，起作用的是化为思维底层逻辑的中国文化。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为喊“中国文化沦丧了”“中国文化已经断根了”的人根本不知道自己在说什么；事实上中国文化几乎没有任何显著的改变。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以勤俭原则、首选受教育改变命运、倾向避免冒险稳扎稳打为例，主张这些不言自明的处事本能才是中国文化的本体。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为穿不穿马褂、剪不剪辫子根本算个屁大的事。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列举“富贵不能淫、贫贱不能移、威武不能屈”等句子，主张这些千千万万的句子交织出了中国人的共性。", "evidence": ["E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“你是中国人，我会预期你知道这些”构成中国人和中国人之间特殊的交流前提，无形中深刻影响这群人集体行动的走向和可选策略的范围。", "evidence": ["E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国人觉得不可接受的事与显然首选的方案，与美国人、日本人、英国人、俄国人截然不同；这才是文化的本体与要害，其余只是影子、气味、边角余料。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者提出假设：中国的文化甚至可以说是不依赖于中国人、而依赖于中国这块土地的；若一万年前是一群印度人穿越喜马拉雅山在此定居繁衍至今，这群人将与现在的中国人有极其近似的行为方式，这跟人种没有关系。", "evidence": ["E25"]}
   ],
   "argument_steps": [
    "界定文化：一群人对于决策机制的群体共识（P002）。",
    "区分符号：音乐、春联、京戏、祭祖、书法、篆刻、诗词是文化的符号与产品（P004）。",
    "工厂比喻：外人只能听声音、吃罐头；工人熟悉的是惯例与厂规；无人尽知厂内传统，且多有自相矛盾（P005-P009）。",
    "换业务：声音与产品变了，工艺、决策机制、部门结构变化甚微；对这些的共同认知才是文化（P010-P013）。",
    "研究方法：紧盯如何理解事物、如何决策，而非感官符号（P015）。",
    "界定中国文化，并声明与语言体系关系甚微；以华人移民的决策模式为例（P016-P020）。",
    "反驳“文化沦丧／断根”之说，并列出勤俭、教育、稳扎稳打等本体（P022-P027）。",
    "以“才算个屁大的事”否定马褂辫子一类符号的意义（P028）。",
    "排比列举“这才是中国文化”的句子，主张其交织出中国人的共性并构成特殊交流前提（P029-P044）。",
    "对照美日英俄，归结文化本体与要害（P045-P047）。",
    "假设性收束：文化依赖土地而非人种，并以“中国有哪些逆天的文物？”引出文化符号的例子（P048-P050）。"
   ],
   "concept_usage": [
    {"term": "文化", "meaning": "本文界定为“一群人对于决策机制的群体共识”；表现为对“工艺、决策机制、部门结构”的共同认知。", "evidence": "P002", "ambiguity": "“决策机制”与“群体共识”如何形成、如何测量，本文未说明。"},
    {"term": "文化的符号／文化的产品", "meaning": "音乐、春联、京戏、祭祖、书法、篆刻、诗词、文物等可见可听的产物；作者称其为工厂的“声音”和“罐头”。", "evidence": "P004", "ambiguity": "符号与本体之间是否存在相互影响，本文未讨论。"},
    {"term": "厂规／惯例", "meaning": "比喻群体内部习惯成自然的决策惯例，其中许多来源不明甚至自相矛盾。", "evidence": "P007", "ambiguity": "为比喻说法，未给出与“文化”的严格对应关系。"},
    {"term": "评分制度", "meaning": "作者称相同的挑战会被“一种特殊的评分制度”去评分，是文化共性的一部分。", "evidence": "P016", "ambiguity": "“评分制度”具体所指未说明。"},
    {"term": "交流前提", "meaning": "中国人之间因共享这些句子而形成的默契预期（“你懂我懂这些”），影响集体行动与可选策略。", "evidence": "P044", "ambiguity": "未说明其边界与例外。"},
    {"term": "blar", "meaning": "作者自造的省略写法，用于替代古文句子的后半段（“blarblarblar”）。", "evidence": "P030", "ambiguity": "为戏仿式省略，非实义词；原句未完整给出。"}
   ],
   "examples_and_targets": [
    "特色音乐、春联、京戏、祭祖仪式、书法、篆刻、诗词：作者列举并否定的“文化符号”清单（P004）。",
    "工厂、厂长、老师傅、罐头、声音：作者的比喻材料（P005-P009）。",
    "牛顿公式与F、A、M、V／甲乙丙丁：作者类比，说明表达语言与本体无关（P017）。",
    "华人移民“送礼”而非“找工会律师”：作者例证（P018）。",
    "勤俭原则、首选受教育、避免冒险稳扎稳打：作者列举的文化本体例证（P024-P026）。",
    "马褂、辫子：作者用于反衬符号之微不足道的例子（P028）。",
    "“富贵不能淫、贫贱不能移、威武不能屈”“天将降大任于斯人也”“鱼我所欲也、熊掌亦我所欲也”“己所不欲”“有朋自远方来”“天下兴亡，匹夫blar”“学而时习之”“君子之行，如日月之blar”“三杯吐然诺、五岳倒为轻”“道可blar”“先下手blar，无毒不blar”“敬鬼神而blar”“虽九死其犹未悔兮”：作者排比列举的句子（P029-P042）。",
    "美国人、日本人、英国人、俄国人：作者的对照群体（P045）。",
    "假设穿越喜马拉雅山定居的印度人：作者的思想实验（P048）。",
    "“中国有哪些逆天的文物？”：P050 的裸标题（lexical未覆盖片段），指向另一篇问答，功能未说明。"
   ],
   "conditions": [
    "P005 以“打个比方”标明工厂为比喻而非实指。",
    "P006 用“外面的人没有办法拆开这座厂、也没有办法搬走它”限定外人的认知途径。",
    "P009 称“几乎只有在里面当工人干上几年一条路”，为经验性限定。",
    "P011 用“在外人看来”限定误判的视角。",
    "P018 的“如果他第一下意识是……”为假设性描述。",
    "P019 用“哪怕……全程没有闪过任何‘中国’的念头”作让步条件。",
    "P022 引述他人说法（“很多人在喊……”）作为被批评对象，非作者主张。",
    "P035、P037 等句以“blar”省略，原句不完整。",
    "P048 用“甚至可以说”“假设”标明为推测性说法。",
    "P044 用“我会预期”标明是作者的预期而非事实统计。"
   ],
   "rhetoric_and_tone": "讲解体与比喻教学：以工厂、罐头、声音贯穿全篇，反复设问（“明白了吗？”“看明白了吗？”），排比列举古文句并以“blarblar”戏仿收尾，夹杂口语粗话（“根本算个屁大的事”），用第一人称“我”的预期与“你”的默契构成共同体口吻；对“文化沦丧”论者语气带讥讽。",
   "unresolved_questions": [
    "P050 为“⚠lexical未覆盖片段”，正文只有一个指向另一知乎问题（“中国有哪些逆天的文物？”）的裸标题，其功能（链接或引用）本文未说明。",
    "P030-P042 中的“blar”为作者自造省略写法，原句未完整给出，无法核对引用文本。",
    "“中国的文化依赖于中国这块土地”属思想实验，其论证依据本文未给出。",
    "“评分制度”“决策机制”的具体所指与衡量方式本文未说明。",
    "“中国文化几乎没有任何显著的改变”的范围与衡量标准本文未说明（作者仅举三例）。",
    "P044 的“交流前提”是否存在例外或边界，本文未说明。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "文化本质上就是一群人对于决策机制的群体共识。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "这些都不是文化，而是文化的符号，是文化的产品。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "打个比方，群体像一座工厂，这些杂七杂八的东西只是这座工厂运转时发出的声音，输送出去的罐头。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "他们眼里是各种各种各样习惯成自然的惯例和厂规。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "没有任何一个工人——包括厂长在内——知道厂里到底有多少种惯例和悄无声息的传统。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "其实呢——工艺没变、决策机制、部门结构这些东西变化甚微。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "而对这些“工艺、决策机制、部门结构”的共同认知，才是文化。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "真正研究文化的人，紧盯着的就是这个文化将如何理解事物、如何做出决策。而不是这些视觉听觉之类的感官符号。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "所谓的中国文化，是指中国人认识事物的一种特殊共性、中国人做决策的一种特殊共性。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "也跟这一套合作机制、评价机制是用什么样的语言体系来表达关系甚微。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "他这样的决策模式就非常中国。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "哪怕ta这些想法是用英文想的，全程没有闪过任何“中国”的念头，这其实也是个中国念头。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "起作用的就是中国的文化。深入骨髓、深入灵魂已经化为思维底层逻辑的中国文化。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "很多人在喊什么中国文化沦丧了呀，什么中国文化已经断根了啊……这都是根本不知道自己到底在说什么。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "事实上中国文化几乎没有任何显著的改变。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "举个例子，勤俭原则就是中国文化的一部分，绝大多数的中国人仍然唾弃不勤不俭的人。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "这些不言自明的处事本能才是中国文化的本体。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "穿不穿马褂，剪不剪辫子，根本算个屁大的事。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "富贵不能淫、贫贱不能移、威武不能屈，这才是中国文化；", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P043", "quote": "这些千千万万的句子，交织出了中国人的共性。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P044", "quote": "这就导致中国人和中国人在一起会有一种特殊的交流前提，无形中会深刻的影响这群人的集体行动的走向和可选策略的范围。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P045", "quote": "中国人觉得不可接受的事，和美国人、日本人、英国人是不同的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P046", "quote": "这才是文化的本体、它的要害。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P047", "quote": "其他那些只不过是文化的影子、气味、边角余料而已。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P048", "quote": "中国的文化，甚至可以说是不依赖于中国人存在的，而是依赖于中国这块土地的。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P048", "quote": "这跟人种没有关系。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P050", "quote": "中国有哪些逆天的文物？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文化理论", "文化认同", "社会学"],
   "issue_candidates": ["文化的界定（本体与符号）", "中国文化是否断裂", "中国人的决策共性", "文化与土地／人种的关系"],
   "text_function_candidates": ["答疑", "解释", "评论"],
   "object_candidates": ["中国人", "美国人", "日本人", "英国人", "俄国人", "华人移民"],
   "working_keywords": ["文化", "文化的符号", "文化的产品", "决策机制", "群体共识", "厂规", "评分制度", "交流前提", "blar"]
  },
  "notes": "正文无图片节点。P050 在阅读包中标注“⚠lexical未覆盖片段”，正文中是一个指向另一知乎问题的裸标题。brief 为正文语句摘录，仅作导航。本篇与同批《中国式反同化》（4adfa0a0）共用“中国文化＝决策共性”的界定与华人移民例证，初读只记录本文用法，不作跨文章归纳。"
 },
 "e7e358f9": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何评价加州尔湾（橙县）华人于当地时间19日自发组织武装卫队的行为？”，即请作者评价该事件。作者未直接评价该武装卫队的对错，而是以戏仿“美国方式（the American way）”的口吻提出一套商业—法律方案：组织先请律师、成立基金会与保险公司、上市融资、设赏金与影视游戏产业链（P001-P027），并在结尾把话题接回“华人难同化”，称同化至今第一念头还是“当黄飞鸿，搞团练”（P028、P029）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出严肃前提：在美国，值得认真对待的组织的基本共同点是至少有一名律师；真想干就先请律师、把枪放一边；并反问华人不是WASP红脖子，学不了ta们。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "以“美国方式”设问，随后给出方案第一步：几个领头的凑一千万美元，成立“Asian Guardian Foundation”，与纽约顶尖律所签约，为华人自卫还击致诉案件提供金融服务。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "方案延伸：基金会下设保险公司向亚裔社区出售法律责任险（一年一千美元、保辩护费用50万美金），聘保安公司提供会员 on call 服务，形成“你负责开枪，我们负责为你请律师”的分工，再上市融资。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "继续戏仿式扩张：凑一亿美元基金、雇赏金猎人追杀伤害亚裔者并先为猎人找好律师、拥有追杀故事独家版权，进而出书、拍《杀死鲍勃》系列与《新复仇者联盟》、卖周边、做直播带货与游戏、办全球职业联赛。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027"], "summary": "收束方案：利润由会员分红、部分作亚裔权益基金；“资本主义国家要用资本主义手段”，把“正义天诛”做成利润丰厚的生意且一切绝对合法；讥讽这样强烈的需求都做不成生意是“在美国白混了”。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P028", "P029"], "summary": "结尾接回“华人难同化”：同化到现在第一念头还是当黄飞鸿、搞团练。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张在美国任何值得稍微认真对待的组织的基本共同点是拥有至少一名律师；真想干，枪先放一边，先请一个有点起码常识的律师。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：华人又不是WASP红脖子，能学ta们吗？即认为华人不能照搬WASP红脖子的做法。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以“美国方式”的戏仿口吻提出假设性第一步：几个领头的凑一千万美元，成立“Asian Guardian Foundation”，与纽约顶尖律所签约，为华人自卫还击案件中杀伤他人而被起诉者提供金融服务。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者继续以戏仿口吻设想：基金会下设保险公司向亚裔社区出售法律责任险（一年一千美元、保辩护费用50万美金），聘保安公司提供 on call 服务，并强调“你负责开枪，我们负责为你请律师”“业务量有了，上市，融资”。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者设想凑一亿美元基金、雇赏金猎人追杀伤害亚裔者，并先把赏金猎人的律师找好、承诺败诉赔偿几百万。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者设想把追杀故事做成出版、电影、周边、直播带货、游戏与全球职业联赛等衍生生意。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张利润由所有会员分红、部分用作亚裔权益基金，并归结为“资本主义国家要用资本主义手段”。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者宣称要把“正义天诛”做成一门利润丰厚的生意，并称一切绝对合法（不服可找协会律师团）。", "evidence": ["E16", "E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者讥讽：这么强烈、大面积的需求都不能做成有利润的生意，是“在美国白混了”。", "evidence": ["E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者据此重提“华人难同化”：同化到现在第一念头还是当黄飞鸿、搞团练。", "evidence": ["E19", "E20"]}
   ],
   "argument_steps": [
    "严肃前提：美国任何值得认真对待的组织都至少有律师；先请律师，枪放一边（P001、P002）。",
    "划界：华人不是WASP红脖子，不能照搬其方式（P003）。",
    "以“the American way”设问并转入戏仿方案（P004）。",
    "方案一：凑一千万美元、成立基金会、与顶尖律所签约、为自卫还击案件提供金融服务（P005-P007）。",
    "方案二：设保险公司卖法律责任险、聘保安公司，分工为“你负责开枪，我们负责为你请律师”，再到上市融资（P008-P011）。",
    "方案三：凑一亿美元基金、雇赏金猎人并先为其找律师、拥有故事版权，延伸到影视、周边、带货、游戏与联赛（P012-P021）。",
    "收束：利润分红、部分作亚裔权益基金；“资本主义国家要用资本主义手段”，把“正义天诛”做成利润丰厚的生意且绝对合法（P022-P026）。",
    "讥讽与结论：这样的需求都做不成生意是“在美国白混了”；并接回“华人难同化”，第一念头还是黄飞鸿、团练（P027-P029）。"
   ],
   "concept_usage": [
    {"term": "美国方式（the American way）", "meaning": "本文中作者以戏仿口吻所指的一套做法：以律师、基金会、保险、上市、版权与衍生生意来组织行动。", "evidence": "P004", "ambiguity": "作者未说明“美国方式”是描述、讽刺还是其真实建议。"},
    {"term": "拥有至少一名律师", "meaning": "作者用来界定“值得稍微认真对待的组织”的最低共同点。", "evidence": "P001", "ambiguity": "为夸张式概括，未给出依据。"},
    {"term": "WASP红脖子", "meaning": "作者用来指华人无法照搬的另一种美国群体及其行事方式。", "evidence": "P003", "ambiguity": "为带贬义的口语标签，作者未界定其范围。"},
    {"term": "正义天诛", "meaning": "作者对“追杀伤害亚裔者”一类行动的称呼，并称要把它做成利润丰厚的生意。", "evidence": "P024", "ambiguity": "为戏仿用语，是否作者真实主张需研究者判断。"},
    {"term": "华人难同化", "meaning": "作者在结尾重提的判断，用来解释华人第一反应为何是“当黄飞鸿，搞团练”。", "evidence": "P028", "ambiguity": "该判断的论证不在本文，与作者另一篇《中国式反同化》呼应，初读不作跨文章归纳。"}
   ],
   "examples_and_targets": [
    "加州尔湾（橙县）华人自发组织武装卫队：提问者提供的事件语境（Q001），正文未直接评价事件本身。",
    "WASP红脖子：作者用作对照的群体（P003）。",
    "Asian Guardian Foundation：作者拟想的基金会名称（P007）。",
    "纽约顶尖律所、法律责任险（一年一千美元／保50万美金）、on call 保安服务：作者方案中的机构与产品（P007-P009）。",
    "赏金猎人：作者方案中的角色（P012、P013）。",
    "《杀死鲍勃》系列、昆汀、糖浆、《新复仇者联盟》、《杀手代号94》、电锯：作者戏仿影视与游戏作品的材料（P015-P019）。",
    "李佳琦、炽天使：作者举例的带货人物（P018）。",
    "黄飞鸿、团练：作者用于说明“第一念头”的修辞材料（P029）。"
   ],
   "conditions": [
    "P003 以“你们又不是WASP红脖子”作条件，得出“能学ta们吗”。",
    "P007 限定基金的用途为“华人在自卫还击案件中杀伤他人而被起诉的案件”。",
    "P013 以“如果我们没本事帮你把官司打赢”为条件，承诺赔偿。",
    "P024 以“你们只管来搞我们”为条件；P025 断言“一切绝对合法”。",
    "P027 的讥讽以“这么强烈的、大面积的需求”为对象。",
    "P028 的“华人难同化”为跨文章判断的引用式重提，本文未论证。"
   ],
   "rhetoric_and_tone": "通篇反讽与戏仿商业计划书：第二人称喊话（“你负责开枪”“你们只管来搞我们”）、夸张数字（一千万、一亿、几个亿）、黑色幽默（《杀死鲍勃》、加倍预算买糖浆、电锯全成就）、夹杂英文插入语（Well, what is the American way？）与网络带货梗；结尾突然转回严肃主题“华人难同化”，形成讽刺落点。",
   "unresolved_questions": [
    "正文未直接评价尔湾（橙县）华人组织武装卫队这一事件的是非，也未核实事件细节，需外部核查。",
    "全篇为夸张戏仿，其中哪些是作者真实主张（如“组织要先请律师”）、哪些只是反讽，需研究者判断。",
    "“Asian Guardian Foundation”等名称与整套方案是否作者真实建议，本文未说明。",
    "P028“华人难同化”的判断依据不在本文（与作者另一篇《中国式反同化》呼应），初读不作跨文章归纳。",
    "昆汀、李佳琦、炽天使等人名为修辞性提及，作者未对其作任何评价。",
    "本篇无图片节点，正文文本已完整阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在美国，任何值得稍微认真对待的组织的基本共同点是——拥有至少一名律师。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "真想干，枪都先放一边，先请一个有点起码常识的律师。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你们又不是WASP红脖子，能学ta们吗？！", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "Well, what is the American way？", "relation": "context"},
    {"key": "E5", "paragraph_id": "P005", "quote": "几个领头的凑钱，先拿个一千万美元。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "成立一个基金会，就叫“Asian Guardian Foundation”，跟纽约顶尖的律所签好协议", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "接着基金会下面开一家保险公司，对整个亚裔社区出售法律责任险。一年一千美元，保你辩护费用50万美金。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "你负责开枪，我们负责为你请律师。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "先凑个一亿美元基金放在这里。谁敢伤害亚裔，找赏金猎人追杀ta到天涯海角！", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "先把赏金猎人的律师找好。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "然后开出版公司和电影公司，把追杀故事出书、拍电影，就叫《杀死鲍勃》系列。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "然后出系列游戏，《杀手代号94》！", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "接人气猎人出狱后开直播，做新媒体接广告业务——李佳琦是谁？让炽天使教你怎么带货！", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "利润由所有会员分红，部分用作亚裔权益基金。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "资本主义国家要用资本主义手段！", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "你们只管来搞我们，我们会把正义天诛做成一门利润丰厚的生意。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "放心，一切绝对合法，不服去找我们的协会律师团聊。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P027", "quote": "这么强烈的、大面积的需求你们都不能做成有利润的生意，你们在美国白混了。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "而且我说什么来着——华人难同化！", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "看到没，同化到现在第一念头还是当黄飞鸿，搞团练。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["海外华人社会", "治安与自卫", "商业与法律组织"],
   "issue_candidates": ["华人武装自卫的组织方式", "在美国用法律与商业手段维权的路径", "华人是否难同化"],
   "text_function_candidates": ["答疑（未直接评价）", "讽刺", "戏仿方案"],
   "object_candidates": ["加州尔湾（橙县）华人", "亚裔社区", "WASP红脖子", "纽约律所", "赏金猎人", "黄飞鸿"],
   "working_keywords": ["美国方式", "the American way", "律师", "基金会", "法律责任险", "赏金猎人", "正义天诛", "资本主义手段", "华人难同化", "黄飞鸿", "团练"]
  },
  "notes": "正文无图片节点。提问请评价华人自发武装卫队，正文以戏仿“美国方式”的商业—法律方案作答，未直接评价该事件。brief 为正文语句摘录，仅作导航。结尾“华人难同化”与同批《中国式反同化》（4adfa0a0）呼应，初读只记录本文表述。"
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
