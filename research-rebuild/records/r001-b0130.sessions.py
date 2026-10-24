# -*- coding: utf-8 -*-
"""批次 r001-b0130 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0130.sessions.py            # 写 out/r001-b0130.out.jsonl
  python3 records/r001-b0130.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0130"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0130.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "da96861e": {
  "analysis": {
   "question_context": "提问者就重庆一生日宴变「蛋糕大战」、KTV 包房一片狼藉一事征求评价，并问为什么有的人对浪费食物不以为意。作者未回应事件本身（正文未提重庆、生日宴、KTV），而以「财富的持有与善用义务」及「自然法高于人类法」立论，末段以「如何树立正确的财富观？」收束。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "财富是给人持有的、不是随便享用的；持有者有支配的职权，也有善用的义务；该义务由自然法规定，不能由人类立法规定。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "以自然法不认同的方式处理财富会遭自然机制反制；该驱动成本为0（如重力），人类法律定义其为非法也不停止，甚至拖垮法律体系；「财富并非可任由持有者随意处置」是其中一条。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "越过自然法红线会有人被本能中的强力因素驱动、无视法律惩罚你；人类法律即使百分之百贯彻也改变不了你受罚的现实，这是人类法与自然法关系的复杂性。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "人类法律必须认同并保护随意处置私有财产的自由，审判者角色由自然法保底；自然法常借罪人实施（罪人仍是罪人）；因此自然法绝对凌驾于人类法之上。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "仅因花钱买到使用权而浪费食物，或更广义地对美好事物、劳动凝结物不尊重，是触犯自然法的行为；人类法律里合法，自然法却会给出法律阻止不了的惩罚。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "劝告追求与持有财富者：财富要么不要，拿到就有看守善用之责，不愿承担就多让给别人；不要以为用经济与舆论机器造出的法律保护罩能保平安，自然法会把它变成支付不起的破烂；这不是恫吓，而是历史反复演示的事实。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020"], "summary": "浪费粮食、尤其出于娱乐目的浪费粮食是极大的禁忌；父母没教好是失职。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P021"], "summary": "以「如何树立正确的财富观？」一句作结。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "财富是给人持有的，不是给人随便享用的；持有者既有支配它的职权，也有善用它的义务。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "善用财富的义务不由人类社会立法规定、也不能由人类立法规定，因为它是由自然法规定的。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果采用自然法不认同的方式处理所持有的财富，就会遭遇自然法驱动的自然机制的反制；这种驱动无视人类法律，即使全世界法律把它定为非法并惩罚限制也不会停止，甚至常反过来令徒劳抑制它的人类法律体系崩溃。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法驱动机制的成本是0，如同重力使苹果落地；既然重力成本为0，一切绝对防止苹果落地的措施最终注定失败。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「财富并非可以任由财富持有者随意处置」是自然法规则中的一条。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越过自然法红线时，会有人被内置在本能中的强力因素驱动、无视法律来惩罚你；人类法律即使百分之百被贯彻，最多判处徒刑或死刑，也改变不了你会受到惩罚的现实。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类法律必须认同并坚定保护随意处置私有财产的自由，它所不能扮演的审判者角色由自然法保底。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然法驱使的机制常借着罪人来实施，那样做的人仍然是罪人（无论是否获赦免或逃脱惩罚）；正因如此，自然法绝对凌驾于人类法之上。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "仅因花钱购买到使用权而浪费食物，或更广义地对一切美好事物、劳动的凝结物没有尊重，是触犯自然法的行为；它在人类法律里合法，但自然法会记住并给出人类法律阻止不了的惩罚。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "财富要么不要，只要拿到就有看守和善用之责；如果不打算承担这份沉重、捉摸不定、喜怒无常的责任，就多把财富让给别人。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "不要以为聚在一起开动经济机器和舆论机器给自己写定完美的法律保护罩就可高枕无忧；自然法会轻松把这保护罩变成支付不起的破烂。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述说法不是威胁恫吓，而是认真读过历史就该明白的、被无数证据反复演示过的事实。", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "浪费粮食——尤其是出于娱乐目的浪费粮食——是极大的禁忌。", "evidence": ["E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母没有教好，是ta们失职。", "evidence": ["E22"]},
    {"claim_id": "C015", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "文章以「如何树立正确的财富观？」这一疑问句收尾，未在该句后给出回答。", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "定义前提：财富是给人持有的，不是给人随便享用的，持有者同时有支配职权与善用义务（P001）。",
    "界定该义务的来源：它不是人类立法规定的，也不能由人类立法规定（P002），而是由自然法规定的（P003）。",
    "机制说明：以自然法不认同的方式处理财富会遭自然机制反制，该驱动无视人类法律、甚至拖垮抑制它的人类法律体系（P004）。",
    "类比理由：该机制成本为0，如重力使苹果落地，故绝对防止苹果落地的措施注定失败（P005）。",
    "收束为上列规则之一：「财富并非可以任由财富持有者随意处置」（P006）。",
    "具体化惩罚途径：越过红线会有人被本能中的强力因素驱动、无视法律惩罚你（P007）；人类法律的贯彻改变不了你受罚的现实（P008）；这是人类法与自然法关系的复杂性（P009）。",
    "给出法律定位：人类法必须认同并保护随意处置私有财产的自由，审判者角色由自然法保底（P010）。",
    "补充归属问题：自然法常借罪人实施，但罪人仍是罪人（P011），故自然法绝对凌驾于人类法之上（P012）。",
    "落到本题：仅因买到使用权而浪费食物、对美好事物与劳动凝结物不尊重，是触犯自然法（P013），将受人类法律阻止不了的惩罚（P014）。",
    "行动劝告：追求与持有财富者要铭记此点（P015）；财富要么不要，拿到就有看守善用之责，不愿承担就让给别人（P016）；不要迷信自制的法律保护罩（P017）；这不是恫吓而是历史反复演示的事实（P018）。",
    "结论与归责：娱乐性浪费粮食是极大禁忌（P019），父母没教好是失职（P020）。",
    "以「如何树立正确的财富观？」作结（P021）。"
   ],
   "concept_usage": [
    {"term": "财富", "meaning": "被持有的对象；持有伴随支配的职权与善用的义务，不是供随意享用之物。", "evidence": "P001", "ambiguity": "未区分财富类型与规模，也未说明「善用」的判定标准。"},
    {"term": "自然法", "meaning": "高于人类法、由零成本机制驱动并以反制惩罚违规者的规则来源。", "evidence": "P003", "ambiguity": "本文未给出自然法的条文、来源或识别方法，只以重力作类比。"},
    {"term": "人类的法律（人类法）", "meaning": "由人类立法形成的法律；必须保护随意处置私有财产的自由，但无法取代自然法的审判者角色。", "evidence": "P010", "ambiguity": "与自然法冲突时的具体制度后果，本文未展开。"},
    {"term": "善用之责／看守之责", "meaning": "财富持有者对财富负担的义务，文中称其沉重、捉摸不定、喜怒无常。", "evidence": "P016", "ambiguity": "义务的具体内容与履行方式本文未列明。"},
    {"term": "禁忌", "meaning": "浪费粮食（尤其娱乐目的的浪费）被列为极大的禁忌。", "evidence": "P019", "ambiguity": "「禁忌」是否等同自然法红线，文中未明说。"},
    {"term": "劳动的凝结物", "meaning": "与「美好的事物」并列，对之不尊重即触犯自然法。", "evidence": "P013", "ambiguity": "术语未定义，是否即劳动产品，本文未说明。"},
    {"term": "罪人", "meaning": "被自然法机制借用去实施惩罚的人；作者强调其行为仍是犯罪。", "evidence": "P011", "ambiguity": "与人类法律意义上的犯罪是否同义，本文未辨析。"}
   ],
   "examples_and_targets": [
    "重庆生日宴变「蛋糕大战」、KTV 包房一片狼藉——出现在提问字段（Q001），属提问者提供的评价对象，正文未再提及。",
    "「为什么有的人对浪费食物不以为意」——提问者的问题（Q001），正文未直接回答该原因问题。",
    "重力让苹果掉到地上——作者类比，说明自然法驱动机制成本为0、绝对防止注定失败（P005）。",
    "「聚在一起、开动经济机器和舆论机器给自己写定一个完美的法律保护罩」——作者所指的群体行为与修辞材料（P017）。",
    "「你如果认真读过历史就该明白的、一而再再而三、用无数的证据反复反复对你演示过的事实」——作者所称的历史证据，未举出任何具体史例（P018）。",
    "父母没有教好——作者归责对象（P020）。"
   ],
   "conditions": [
    "如果采用某些自然法不认同的方式处理你持有的财富，就会遭遇自然机制的反制（P004）。",
    "即使全世界的现有法律把这种反制定义为非法并加以惩罚、限制，反制也不会停止（P004）。",
    "人类的法律即使能够百分之百被贯彻实施，最多不过判处徒刑甚至死刑，改变不了你会受到惩罚的现实（P008）。",
    "财富要么不要；只要拿到了，就有看守和善用之责（P016）。",
    "如果不打算承担这份责任，就多把财富让给别人（P016）。",
    "限定语「尤其是出于娱乐目的浪费粮食」被单独点为极大禁忌（P019）。",
    "「仅因为自己花钱购买到了使用权而浪费食物」被定为触犯自然法的情形（P013）。",
    "「所有想要追求财富的人、包括持有财富的人」是劝告的适用对象（P015）。"
   ],
   "rhetoric_and_tone": "训诫式断言，近乎布道；大量使用第二人称「你」直接告诫，并以「你们」指称制定法律保护罩的群体；用重力与苹果的类比把自然法机制自然化；「罪人」「禁忌」「赦免」等带宗教—法理色彩的词；命令式劝告（「要牢牢的铭记于心」「多把财富让给别人」）；自我辩护式声明「这不是一个威胁恫吓」；末段以疑问句「如何树立正确的财富观？」收尾。",
   "unresolved_questions": [
    "作者未直接评价提问所述重庆「蛋糕大战」事件本身，也未提 KTV 包房；正文评价对象与提问事件的对应关系由读者推定。",
    "「自然法」「自然机制」的具体内容、条文与识别方法本文未给出可操作定义。",
    "自然法反制的具体惩罚形式与经验证据本文未列举，仅称历史反复演示过。",
    "末段「如何树立正确的财富观？」在结构上被标记为 lexical 未覆盖片段（骨架 divergence=true），它是标题、话题标签还是正文段落需核对原始语料。",
    "「父母没有教好，是ta们失职」中的「ta们」指哪些父母，本文未明说。",
    "「更广义的说」所指的尊重对象边界（美好事物、劳动凝结物）未界定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "财富这东西，是给你持有的，不是交给你随便享用的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "你持有了你会有支配它的职权，但你也有善用它的义务。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "这个义务不是什么人类社会立法来规定的、也不能由人类立法来规定", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "它是由自然法规定的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "就会遭遇自然法驱动出来的自然机制的反制。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "这种由自然法驱动的反制也一样不会停止", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "因为它的驱动机制的成本是0", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P005", "quote": "一切要绝对防止苹果掉到地上的措施就都是最终注定失败的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P006", "quote": "“财富并非可以任由财富持有者随意处置”，就是其中的一条。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "就会有人被内置在ta本能中的强力因素驱动、无视法律来惩罚你。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "但这改变不了你会受到惩罚的现实。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "人类的法律必须要认同你随意处置私有财产的自由", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P010", "quote": "而它所不能扮演的审判者角色，自有自然法保底。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P011", "quote": "自然法所驱使的那些机制，常常借着罪人来实施", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P012", "quote": "但是恰恰因此，自然法才绝对的凌驾于人类法之上。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "对一切美好的事物、劳动的凝结物没有尊重，是触犯自然法的行为。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "但自然法会记住，会给你人类法律阻止不了的惩罚。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "财富你要么不要，只要你拿到了，你就有看守和善用之责。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P017", "quote": "自然法会轻松的把这法律保护罩变成一个你们支付不起的破烂。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P018", "quote": "这不是一个威胁恫吓", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P019", "quote": "浪费粮食——尤其是出于娱乐目的浪费粮食——是极大的禁忌。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P020", "quote": "父母没有教好，是ta们失职。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P021", "quote": "如何树立正确的财富观？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["法哲学／自然法", "财产与财富伦理", "道德训诫"],
   "issue_candidates": ["私有财产的支配自由与善用义务", "自然法高于人类法", "浪费食物（娱乐性浪费）的道德性质", "财富观的树立"],
   "text_function_candidates": ["论辩", "训诫", "答疑（未直接回应提问事件）"],
   "object_candidates": ["提问者（重庆生日宴蛋糕大战一事）", "财富持有者", "人类法律体系", "父母"],
   "working_keywords": ["自然法", "人类法", "善用之责", "看守", "禁忌", "罪人", "财富观"]
  },
  "notes": "无图片节点，正文可读。骨架 divergence=true：P021「如何树立正确的财富观？」被阅读包标注为 lexical 未覆盖片段，其结构归属需核对原始语料。brief 与正文前段高度重合，仅作导航，未用于支持主张。"
 },
 "b9d54197": {
  "analysis": {
   "question_context": "提问者问：为什么美联储敢这么大胆地印钱，不担心通胀等负面后果？作者未讨论美联储的操作或通胀机制，只用三句格言作答：把「勇敢」解释为别无选择的结果（不敢不勇敢），并以「印了至少能活着担心／不印连担心的机会都没有」作对比。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出一般命题：凡不能被解释为冲动的勇敢行为，都必然是不敢不勇敢的结果。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "把该命题落到印钱抉择上：印了至少还能活着担心，不印则连担心的机会都没有。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切不能被解释为冲动的勇敢行为，都必然是不敢不勇敢的结果。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "（就所讨论的印钱抉择而言）印了至少能活着担心，不印连担心的机会都没有。", "evidence": ["E2", "E3"]}
   ],
   "argument_steps": [
    "先给出一般命题：不能被解释为冲动的勇敢，都是「不敢不勇敢」的结果（P001）。",
    "以两句对偶把该命题对应到印钱：印了至少能活着担心（P002）；不印连担心的机会都没有（P003）。",
    "全篇不点明主语，也不解释印钱与通胀的机制，推论由读者依提问语境补足。"
   ],
   "concept_usage": [
    {"term": "勇敢", "meaning": "表面上的大胆行为；作者主张除冲动可解释者外，其实都是被迫、别无选择的结果。", "evidence": "P001", "ambiguity": "未界定「冲动」与「不敢不勇敢」的判定方式。"},
    {"term": "印（钱）", "meaning": "作为两害相权中的一个选项出现，正文未说明主体、规模与机制。", "evidence": "P002", "ambiguity": "主语在正文中缺失，是否指美联储只能靠提问字段（Q001）推定。"},
    {"term": "担心", "meaning": "对负面后果的忧虑，被设定为需要「活着」才可能有的东西。", "evidence": "P003", "ambiguity": "正文未提「通胀」等具体后果，该内容只见于提问字段。"}
   ],
   "examples_and_targets": [
    "美联储大胆印钱、通胀等负面后果——仅出现在提问字段（Q001），正文完全未提，属提问者提供的语境。",
    "正文未使用任何具体人物、事件、机构或数据作为例证。"
   ],
   "conditions": [
    "命题限定于「不能被解释为冲动的」勇敢行为（P001）。",
    "「印了」与「不印」两种情形被并列比较（P002、P003）。"
   ],
   "rhetoric_and_tone": "格言体、极简三句；对偶结构（「印了……／不印……」）；不点主语、不作论证展开，接近冷幽默式的反讽回答；「至少」「连……都」带让步—比较语气。",
   "unresolved_questions": [
    "正文未出现美联储、印钱机制与通胀，作者是否在回答提问所问的「为什么敢印」，只能从提问语境推定。",
    "「印了」「不印」的主语在正文中未明说，无法确定指美联储、美国还是其他主体。",
    "「活着担心」中的「活着」指谁（机构、国家还是持有者）本文未说明。",
    "三句之间的推论（一般命题如何推出印钱结论）未明写，属读者补足。",
    "brief 与正文逐句相同，不构成额外证据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "一切不能被解释为冲动的勇敢行为，都必然是不敢不勇敢的结果。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "印了至少能活着担心。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "不印连担心的机会都没有。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["格言／处世判断", "货币与货币政策（仅提问语境，正文未展开）"],
   "issue_candidates": ["美联储印钱与通胀担忧（提问所问，正文未回答）", "勇敢行为的动因"],
   "text_function_candidates": ["答疑（极简式）", "评论"],
   "object_candidates": ["美联储（仅见提问字段）", "印钱决策者（正文未点名）"],
   "working_keywords": ["勇敢", "不敢不勇敢", "冲动", "印钱", "担心"]
  },
  "notes": "无图片节点，正文可读，但全文仅3段、53个UTF-16字符，是极短回答。提问（Q001）与正文之间无显式连接词，主体归属依赖语境，未在正文中确认美联储等具体对象；正文亦未提通胀。brief 与正文同文，仅作导航。"
 },
 "044cc459": {
  "analysis": {
   "question_context": "提问者问：为什么最近「凡是摆老资格教训年轻人的，一个接一个翻车」？作者不解释该现象的成因，而是否定「以是否翻车来判断一个人的教训值不值得听」这一思路：先举尼采、爱因斯坦、牛顿说明翻车人人难免，再指该思路会导致拒绝一切教训与道德，并批评那种「非要找个理由才敢不听」的做法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "只要一个人想，ta可以等到每一个教训过ta的人都「翻车」；从父母、师长到政治伟人、思想巨擘都没有例外；「翻车」看似是普通人能避免的可耻失败，实际上只要是人类就没有永远不翻车的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "举例：年轻人推崇的尼采发疯、爱因斯坦抛弃妻子且儿子进精神病院、牛顿炒股亏掉十年收入；例子多到懒得再举。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "「翻车」与ta们说话对不对几乎无关；以没翻车就值得听、翻车了就不值得听来判断，看似有道理，其实是自我戕害。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "归谬：只听没有失败者的教训等于拒绝一切教训，只遵守道德完美者讲述的道德等于拒绝一切道德；这是扭曲了的懦夫行为。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"], "summary": "不打算听本来就不需要理由，成年人直接面对后果是天然权利、无需请示批准；但若非要编一个「逻辑」向旁人骗取赞同章才敢不听，则——。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016"], "summary": "两项后果：凭这点胆量，找到理由也同样不敢不听；损害人格、抛弃尊严，自然受旁人鄙视。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P017"], "summary": "以四字小标题「不听无罪，猥琐难饶」作警句收束。", "role": "transition"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019"], "summary": "行动劝告：谈恋爱时要睁大双眼，看不出这种行为的猥琐性、不感到恶心就活该不幸福；要教清楚自己的子女别做这种丑事。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要一个人想，ta可以等到每一个教训过ta的人都「翻车」；从父母、师长到政治伟人、思想巨擘都没有例外。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「翻车」听起来好像是普通人就能避免的可耻失败，实际上只要是人类，就没有永远「不翻车」的。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者举尼采发疯、爱因斯坦抛弃妻子且儿子进精神病院、牛顿炒股亏掉十年收入为例，说明「翻车」是普遍现象。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「翻车」和ta们说话对不对几乎没有什么联系。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "（作者所批评的流行思路）觉得一个人没「翻车」，ta说的话就是对的、值得听；「翻车」了，说的话就是错的、不值得听。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以是否「翻车」决定一个人的话是否值得听的思路看起来有道理，其实是自我戕害。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只听没有失败的人的教训，等于拒绝一切教训；只遵守道德完美的人讲述的道德，等于拒绝一切道德。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述做法都是一种扭曲了的懦夫行为。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "其实不打算听本来就不需要任何理由；作为成年人，不听某个教训而直接面对后果是天然权利，用不着向任何人请示求批准。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果非要编一个「逻辑」、从旁人那里骗一个赞同章才敢壮着胆子不听，那么：其一，凭这点胆量，找到理由也同样不敢不听；其二，损害自己的人格、抛弃自己的尊严，自然而然的会受到旁人的鄙视。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "小标题式断言：不听无罪，猥琐难饶。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谈恋爱时要睁大双眼：看不出这种行为的猥琐性、不对此感到恶心，就活该不幸福。", "evidence": ["E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要教清楚自己的子女，别做这种丑事。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "命题起点：只要一个人想，ta可以等到每一个教训过ta的人「翻车」，父母、师长、政治伟人、思想巨擘都无例外（P001、P002）。",
    "限定「翻车」概念：它不是普通人可避免的可耻失败，人类没有永远不翻车的（P002）。",
    "举例证成普遍性：尼采发疯（P003）、爱因斯坦抛弃妻子且儿子进精神病院（P004）、牛顿炒股亏掉十年收入（P005），并称例子多得懒得再举（P006）。",
    "切断关联：翻车与ta们说话对不对几乎无关（P007）。",
    "指出被批评思路并定性：以翻车与否决定听不听，看似有道理，实为自我戕害（P008）。",
    "归谬：只听没有失败者的教训=拒绝一切教训（P009），只遵守道德完美者的道德=拒绝一切道德（P010），这是扭曲了的懦夫行为（P011）。",
    "正面对照：不打算听本来不需理由（P012），成年人直接承担后果是天然权利，无需请示批准（P013）。",
    "指出实际做法：编一个「逻辑」，向旁人骗取赞同章才敢不听（P014）。",
    "推出两项后果：找到理由也同样不敢不听（P015）；损害人格、抛弃尊严，自然受鄙视（P016）。",
    "以四字小标题作警句：不听无罪，猥琐难饶（P017）。",
    "延伸劝告：恋爱时要识别并厌恶这种猥琐（P018），要教清楚自己的子女别做这种丑事（P019）。"
   ],
   "concept_usage": [
    {"term": "「翻车」", "meaning": "指一个人遭遇失败、出丑或人生事故（作者以尼采发疯、爱因斯坦家庭失败、牛顿炒股亏损为例）；作者强调其普遍难免。", "evidence": "P002", "ambiguity": "未给出判定「翻车」的标准，也未说明翻车与观点对错的关系为何被读者混同。"},
    {"term": "教训", "meaning": "老资格者对年轻人的训诫、劝告；作者讨论的是「要不要听」。", "evidence": "P009", "ambiguity": "未区分教训内容本身的真假优劣与说话者的人格。"},
    {"term": "「逻辑」", "meaning": "加引号使用，指为「不听」而编造出来的理由/说辞。", "evidence": "P014", "ambiguity": "作者未说明其与真正论证的区别标准。"},
    {"term": "赞同章", "meaning": "比喻从旁人处取得的批准、背书。", "evidence": "P014", "ambiguity": "「指着你来给ta们盖章的一群人」具体指哪些人，本文未明说。"},
    {"term": "猥琐", "meaning": "指不敢直接不听、非要找理由求批准的行为特征（小标题作「猥琐难饶」）。", "evidence": "P017", "ambiguity": "未给出判定尺度，兼含道德贬义与人格评价。"},
    {"term": "天然的权利", "meaning": "成年人直接面对不听教训之后果、不必向任何人请示批准的权利。", "evidence": "P013", "ambiguity": "其来源（自然、成年身份还是其他）本文未说明。"}
   ],
   "examples_and_targets": [
    "「凡是摆老资格教训年轻人的，一个接一个翻车」——提问者提供的现象（Q001）；作者未举出任何「最近翻车」的具体人物或事件，也未回答其原因。",
    "尼采——作者例证，称「年轻人推崇备至的尼采，直接就是个疯子，翻得方向盘都掉了」（P003）。",
    "爱因斯坦——作者例证，称其抛弃妻子、儿子进了精神病院（P004）。",
    "牛顿——作者例证，称其炒股票亏掉了十年收入，是「经典的韭菜表现」（P005）。",
    "父母、师长、政治伟人、思想巨擘——作者泛举的「教训过你」的人（P002）。",
    "「看不出这混账逻辑的、也指着你来给ta们盖章的一群人」——作者修辞材料，指给予赞同章的人（P014）。",
    "谈恋爱对象、自己的子女——劝告的适用对象（P018、P019）。"
   ],
   "conditions": [
    "条件在「只要一个人想」，即等谁翻车取决于主观意愿与时间（P001）。",
    "被批评思路以条件句描述：「觉得一个人没『翻车』，ta说的话就是对的，值得听；『翻车』了，说的话就是错的，不值得听」（P008）。",
    "天然权利的前提是「作为一个成年人」（P013）。",
    "「其实你不打算听」是后文「本来就不需要任何理由」的前提（P012）。",
    "「你非要……那么——」为条件结构，两项后果只在编理由求批准的情形下成立（P014）。",
    "劝告限定于「谈恋爱的时候」与教子女的场合（P018、P019）。"
   ],
   "rhetoric_and_tone": "雄辩式训诫加讥讽；第二人称「你」直接指责读者，并以反问句「算不算『翻车』？」发问；使用口语贬词「韭菜」「猥琐」「丑事」「活该」「混账逻辑」；用四字小标题「不听无罪，猥琐难饶」作警句；结构上先举反例、再断关联、后归谬（拒绝一切教训/道德），最后下人格判断；对读者作强烈道德评价。",
   "unresolved_questions": [
    "提问所指「最近……一个接一个翻车」的具体人物与事件，本文未举；作者也未回答提问的「为什么」，而是转为反驳判断标准。",
    "尼采「直接就是个疯子」、爱因斯坦「儿子进了精神病院」、牛顿「炒股票亏掉了十年收入」等事实断言未给来源，需外部核查。",
    "P002、P007、P014 等处「ta们」的指代对象需靠上下文推定，其中 P014 的「一群人」身份不明。",
    "P002「只要是人类，就没有永远『不翻车』的」是否包含作者自身，本文未明说。",
    "元数据中 updated_at（2025-12-18）远晚于 published_at（2021-06-05），而 provenance/superseded 均为 null，是否存在后续修改或版本差异需核对。",
    "「编一个『逻辑』」与正常论证的界限、以及「赞同章」的社会关系所指，本文未具体说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "只要一个人想，ta可以等到每一个教训过ta的人都“翻车”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "从父母，到师长，到政治伟人、思想巨擘，都没有例外。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "实际上只要是人类，就没有永远“不翻车”的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "年轻人推崇备至的尼采，直接就是个疯子，翻得方向盘都掉了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "爱因斯坦抛弃妻子，儿子进了精神病院，算不算“翻车”？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "牛顿炒股票亏掉了十年收入，经典的韭菜表现。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "“翻车”和ta们说话对不对几乎没有什么联系。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "觉得一个人没“翻车”，ta说的话就是对的，值得听", "relation": "context"},
    {"key": "E9", "paragraph_id": "P008", "quote": "这种思路看起来有道理，其实是自我戕害。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "只听没有失败的人的教训，等于拒绝一切教训。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "只遵守道德完美的人讲述的道德，等于拒绝一切道德。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "这都是一种扭曲了的懦夫行为。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "其实你不打算听，你本来就不需要任何理由。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "不听某个教训而直接面对后果本来就是你天然的权利", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "从别的看不出这混账逻辑的、也指着你来给ta们盖章的一群人那里骗一个赞同章", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "你其实找到了理由也同样不敢不听。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "你损害了自己的人格、抛弃了自己的尊严，自然而然的会受到旁人的鄙视。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P017", "quote": "不听无罪，猥琐难饶。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "你们要是看不出这种行为的猥琐性，不对此感到恶心，那真是活该不幸福。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P019", "quote": "教清楚自己的子女，别做这种丑事。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["代际关系与权威批评", "道德心理与人格评价", "言论接受与判断标准"],
   "issue_candidates": ["「摆老资格教训年轻人」的翻车现象（提问所问）", "以成败/人格决定言论是否值得听", "拒绝听从的正当性与理由需求"],
   "text_function_candidates": ["论辩", "批评", "训诫", "评论"],
   "object_candidates": ["提问者所述「摆老资格」者与年轻人（Q001）", "尼采", "爱因斯坦", "牛顿", "父母／师长／政治伟人／思想巨擘", "谈恋爱者", "子女"],
   "working_keywords": ["翻车", "教训", "自我戕害", "懦夫行为", "赞同章", "猥琐", "天然的权利"]
  },
  "notes": "无图片节点，正文可读；P017 为 heading 字段（「不听无罪，猥琐难饶」），其余为 body。元数据 updated_at（2025-12-18T06:00:57）远晚于 published_at（2021-06-05），provenance/superseded 均为 null，是否属后续版本修改待核查。brief 为正文前段的摘录，仅作导航，未用于支持主张。"
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
