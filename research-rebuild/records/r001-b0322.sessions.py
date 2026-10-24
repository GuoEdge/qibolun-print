# -*- coding: utf-8 -*-
"""批次 r001-b0322 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0322.sessions.py            # 写 out/r001-b0322.out.jsonl
  python3 records/r001-b0322.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0322"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0322.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f651d0b4": {
  "analysis": {
   "question_context": "提问者（自述女，24岁，今年大学毕业）在知乎提问“抑郁症大学生如何挽回师生关系？”，question 字段仅此一句。正文以 13 个引用块（field=quote）转述提问者的长篇自述：她与最爱的大学老师 L（男，47岁）几近决裂，自述患抑郁症、就医与被副书记和辅导员看管的经过，以及反复不分时间地给 L 打电话、因 L 偏爱其他学生而吃醋争吵、吞药自杀、被拉黑、道歉无果，最后问“我该怎么办”。作者以《师生一场》为题逐段点评：既评提问者行为的伦理问题（求助越界、电话轰炸、对等报复、吃醋、忍不住、道歉再来一刀），也评 L 的处理方式（把风险告知副书记、明示私人感情），最后给出“停止主动联系”的建议。提问者的自述与诉求属被引材料，不等于作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "引用块：提问者自述与 L 几近决裂、设问“什么是爱”，并称向 L 诉苦告知抑郁症、L 承诺保密。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "作者质问该求助路径，以断腿不去医院却找邻居包扎作比，称对方本应免责而当事人不会免责。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "提出“拯救的特权”须经特殊授予，无授予者无权免责。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "回应 L 告知副书记：做法对但应事先声明；主张答应保密极罕见、须有对称的实质补偿。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "秘密托付的伦理账：批判“让对方背负秘密还应得感恩”的伦理观，主张为对方立场考虑得失是家庭作业。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P029", "P030", "P031"], "summary": "判断 L 跨红线要付代价；区分人类法与自然法。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035"], "summary": "反驳以“生活作息与常人无异”否定抑郁迹象，说明看管方被通知风险后必然警觉。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "分析电话轰炸：可被接听是危险信号，及早拒接才有余地，加倍拨打等于宣判关系死刑。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070"], "summary": "提出“为何不找父母”的隐藏情节与亲自核实 SOP，主张插手须自觉接受后果，并判定 L 无此自觉。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P071", "P072", "P073", "P074", "P075", "P076", "P077"], "summary": "反驳对等观：平等在于特权与代价对称及身份无关性。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095"], "summary": "判定 L 明示私人感情越界（get personal），否认行善可救赎徇私。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P096", "P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105"], "summary": "判定吃醋是以自身情绪给对方自由设界，必致自寻流放。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114", "P115"], "summary": "批判“忍不住”免责伦理，主张同档处罚、以治疗代替减免。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P116", "P117", "P118"], "summary": "禁止借他人电话绕过拒绝，指出这已是敌对手段。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130"], "summary": "评道歉的前提，并把“真真切切的进步”解释为停止主动联系，主动打扰即清零重算。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质问：为何头痛无法学习就能找 L 诉苦、为何可直接告知患抑郁症、有无诊断书，以及为何不去就医而找无医疗资质的 L。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以断腿不去医院却找邻居包扎作比，称对方勉力帮忙后反成造孽；对方本应免责，但当事人不会免其责，甚至可能举报非法行医。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张“拯救的特权”须经特殊授予，无授予即无权免责；而责任只要对方心头不快、口头自称就会产生。", "evidence": ["E4", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为 L 告知副书记本身是对的，但应在对方开始倾诉之前提前声明。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张“答应保密”应极罕见、须有对称的实质补偿，且受托背负秘密只会贬损托付者在自己心目中的地位。", "evidence": ["E9", "E11", "E12"]},
    {"claim_id": "C006", "claim_type": "opponent_view", "attribution": "unknown", "modality": "asserted", "statement": "作者转述一类人的相反看法：让对方背负秘密者自认应受对方感恩与回报；作者斥其为错乱伦理观、把掠夺当恩赐。", "evidence": ["E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者判断这种错乱伦理观势必让当事人在其后人生中付出惨烈代价。", "evidence": ["E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张“从对方立场考虑对方的得失”是每个人不可推卸的家庭作业，父母没教也要学会；学不会时社会直接惩戒本人。", "evidence": ["E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者判断 L 跨过红线极大概率要为傲慢和无知付出代价，并称“不知者无罪”只适用于人类法，自然法没有这种豁免。", "evidence": ["E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认以“生活作息与正常同学无异”否定抑郁迹象，指出迹象会从遣词造句中流露，看管方被通知风险后必然高度警觉。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断“电话轰炸却都能被接听”是极危险的信号，几乎没有什么关系不会被重创甚至毁灭，可靠办法几乎只有彻底断绝关系。", "evidence": ["E23", "E24"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者区分：对方拒接后你停打，关系尚有余地；若加倍拨打直到对方不得不关机或接听，就等于宣判关系死刑、只是延期执行。", "evidence": ["E25", "E26"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者提出隐藏情节：当事人有痛苦却轰炸老师而不找父母，一般因已与父母决裂或对父母失望；父母几乎可免责，是首选途径。", "evidence": ["E28", "E29"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张父母有特权仍解决不了，唯一解释是当事人把父母描述成极恶；单方描述须亲自核实，以核实为惯例性 SOP 声明往往能让纠缠退散。", "evidence": ["E31", "E33"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张父母无法负担抚养责任时第一顺位责任人是民政部门；越权顶替者会被免责并被追究责任。", "evidence": ["E34", "E35"]}
    ,{"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者不认为插手绝不可取：真正有爱的人可以无畏这种安排，但须自觉、毫无侥幸地接受责任，这才是真正英勇的爱。", "evidence": ["E36", "E38"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断 L 并没有这种自觉。", "evidence": ["E39"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张停止“你如何对我，我就可以如何对你”的对等观，称其为幼稚的伦理幻觉；平等不在对等处置权，而在特权与代价的对称、身份无关性。", "evidence": ["E40", "E41"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定 L 的话逾越伦理界限（get personal）；这类公事关系中无论有无私人感情都不允许对对方明示，否则会驱使对方触犯规则甚至法律并牵连自身。", "evidence": ["E44", "E45"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者推测 L 可能认为自己的选择虽出自私人偏爱，但因所行为善故可救赎徇私。", "evidence": ["E46", "E47"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认行善可救赎徇私：宣之于口的“喜欢”会把帮助重新定性为偏爱，明知对方以宠爱受之而不收手，“行善”即自行崩溃，因为宠溺是贿赂关系。", "evidence": ["E48", "E50"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张对方问“是否因为喜欢我”只该有一个答案：这是我的职责所在，我是尽忠职守。", "evidence": ["E51"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定吃醋非常愚蠢、从无好结果，因为它以自身情绪作为对方自由的新边界；跑去惩罚别人的人哪怕一时得逞也是自寻流放。", "evidence": ["E53", "E54", "E56"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者批判“忍不住只算意志失败、不算故意”的免责伦理，主张在自己这里忍不住就是故意、同档处罚，帮助应用治疗手段而非减免处罚。", "evidence": ["E57", "E58", "E59"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张不得借他人电话绕过对方的拒绝，这已是敌人才会用的手段；用敌对手段寻求友谊逻辑不通。", "evidence": ["E60", "E61"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张道歉一定有用、没有人不需要道歉，前提是真的有意义的道歉；“一边捅刀子一边对不起”的道歉是“再来一刀”的刮刮卡。", "evidence": ["E62", "E63"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把 L 说的“真真切切的进步”解释为“停止主动联系”，主张只能写在对方可自然回避之处，主动打扰即清零重算。", "evidence": ["E65", "E67"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者认为按此行事，对方若打算来找你自然会来，这是能争取到的最大修好概率。", "evidence": ["E68"]},
    {"claim_id": "C029", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者顺带提出的开放问题：徇私是不是善行的合法动机？", "evidence": ["E69"]},
    {"claim_id": "C030", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者自述的报复心态：要让 L 尝尝整天被人打电话的滋味。", "evidence": ["E70"]},
    {"claim_id": "C031", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者自述后悔、道歉无用、不知如何挽回与 L 的师生关系，并追问“我该怎么办”。", "evidence": ["E72"]},
    {"claim_id": "C032", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者自述：副书记和辅导员认定抑郁症一定会自杀而把她看得很严，给了她很大的心理压力。", "evidence": ["E74"]}
   ],
   "argument_steps": [
    "先质疑求助本身：为何能向无资质的 L 诉苦、为何不就医（P004）。",
    "以断腿找邻居包扎作类比，把无资质帮助的风险归给求助者（P005-P006）。",
    "定义“拯救的特权”须经特殊授予，无授予者无权免责（P010-P012）。",
    "据此评 L 告知副书记：方向对但缺事先声明（P014-P015）。",
    "转入保密本身：应极罕见且须有对称补偿（P016-P019）。",
    "批判“让对方背秘密还应得感恩”的伦理观并预告代价（P024-P028）。",
    "判定 L 跨红线要付代价，区分人类法与自然法（P029-P031）。",
    "反驳“生活作息无异即无抑郁”：看管方被通知风险后必然警觉（P033-P035）。",
    "分析电话轰炸：可被接听是危险信号，及早拒接才有余地（P039-P043）。",
    "提出隐藏情节“为何不找父母”，建议亲自核实并指出责任顺位（P047-P060）。",
    "让步：插手并非绝不可取，但须自觉接受后果，而 L 无此自觉（P061-P070）。",
    "反驳对等观：平等在于特权与代价对称、身份无关性（P072-P077）。",
    "判定 L 明示私人感情越界，并否认行善可救赎徇私（P079-P091）。",
    "以特蕾莎修女、消防队员类比：帮助不该被问成是否出于喜欢（P092-P095）。",
    "判定吃醋是以自身情绪给对方自由设界，必致流放（P097-P104）。",
    "批判“忍不住”免责伦理，主张同档处罚、以治疗代替减免（P107-P115）。",
    "禁止借他人电话绕过拒绝，指出这是敌对手段（P117-P118）。",
    "评道歉：有意义的道歉才有用，假道歉等于“再来一刀”（P120-P123）。",
    "解释“真真切切的进步”即停止主动联系（P125-P129）。",
    "结论：不主动打扰是能争取到的最大修好概率（P130）。"
   ],
   "concept_usage": [
    {"term": "拯救的特权", "meaning": "免于被追究的授权资格；作者列举父母/监护人、当事人本人、其合法授权者与法律指定的特殊专业人员", "evidence": "P011", "ambiguity": "未说明授予形式与救济途径，且一词兼跨法律与伦理豁免"},
    {"term": "保密义务", "meaning": "接受他人秘密后所负的负担，应极罕见且须有对称的实质补偿", "evidence": "P016", "ambiguity": "“99.99%/0.01%”是修辞性数量表达，非统计结论"},
    {"term": "责 / 免责", "meaning": "责任；作者称只要对方心头不快、口头自称就会产生，且不因“不知者无罪”而豁免", "evidence": "P012", "ambiguity": "“责”的性质（法律、职业还是道德）未限定"},
    {"term": "人类法 / 自然法", "meaning": "作者以“人类法”指有不知者无罪豁免的规则，以“自然法”指没有该豁免的规律性后果", "evidence": "P030", "ambiguity": "非标准法学定义，属作者概括用语"},
    {"term": "隐藏情节", "meaning": "当事人有痛苦却不找父母而找外人的未言明背景", "evidence": "P047", "ambiguity": "作者以“一般都是”限定，属推断"},
    {"term": "对等观", "meaning": "“你对我这样做，就意味着我可以对你这样做”，作者称为幼稚乃至出自臆想的伦理幻觉", "evidence": "P072", "ambiguity": "未区分其与正当互惠的界限"},
    {"term": "平等", "meaning": "作者定义为特殊权力与特别代价的对称，以及身份无关性两个维度", "evidence": "P074", "ambiguity": "与法律面前人人平等等常用含义的关系未说明"},
    {"term": "get personal", "meaning": "在公事关系中明示私人感情而逾越伦理界限", "evidence": "P079", "ambiguity": "英文俚语，未给形式化定义"},
    {"term": "徇私", "meaning": "因私人偏爱而行公事之实；作者否认行善可作为其合法动机", "evidence": "P084", "ambiguity": "先以开放问题提出，后文以否定回答收束"},
    {"term": "宠溺 / 受宠溺", "meaning": "作者将其界定为一种贿赂关系，不因一方在输出利益而改变", "evidence": "P091", "ambiguity": "属比喻性界定还是规范判断未说明"},
    {"term": "忍不住", "meaning": "当事人常用的免责理由；作者主张在自己这里等于故意、同档处罚", "evidence": "P110", "ambiguity": "作者同时承认误拨（压到按钮、Siri 误听）可作事故降档"},
    {"term": "吃醋", "meaning": "以自身情绪作为对方自由的新边界的行为", "evidence": "P098", "ambiguity": "未讨论其与正当不安的区别"},
    {"term": "真真切切的进步", "meaning": "作者把 L 的这句话解释为“停止主动联系”", "evidence": "P126", "ambiguity": "L 原话未给定义，此解属作者推断"},
    {"term": "情绪轰炸 / 电话轰炸", "meaning": "不分时间地点反复打电话倾倒情绪", "evidence": "P039", "ambiguity": "无量化标准"}
   ],
   "examples_and_targets": [
    "提问者（自述女，24岁）与大学老师 L（男，47岁）：全文分析对象，经历由 13 个引用块转述，属引用材料（P001、P013、P032 等）。",
    "L 的妻子：引用叙述中厌恶提问者并警告 L 不要再有联系（P106），作者未直接评价。",
    "副书记与辅导员：引用叙述中执行看管、陪护与免责声明程序（P032、P096）；作者据其立场分析看管责任（P035）。",
    "提问者的母亲：引用叙述中签免责声明书、送医、请 L 救人（P032、P096）；作者据此讨论父母责任与代位（P050-P060）。",
    "医生：引用叙述中与 L 通话，建议不要把提问者微信电话拉出黑名单（P106）。",
    "民政部门：作者主张其为父母无法负担抚养责任时的第一顺位责任人（P059），属制度性断言，待外部核查。",
    "特蕾莎修女、消防队员：作者类比，说明帮助者不应被问是否出于喜欢（P092、P093）。",
    "警察拘捕、师长约束、父母命令；连长与班长、姓张或蒙古族：作者例证，反驳对等处置权、说明身份无关性（P073、P076）。",
    "断腿找邻居包扎、万有引力、高压线、讨债人找躲债的：作者类比（P005、P031、P112、P117）。",
    "达摩克利斯之剑、石中剑与“胸怀利器，杀心自起”：作者修辞引用，形容徇私把柄（P081、P082）。",
    "拿汽油灭火、“再来一刀”刮刮卡、“忍不住优惠券”“免责大酬宾”、红孩儿：作者讽刺性比喻与调侃（P103、P105、P108、P121）。",
    "压到按钮、Siri 误听指令：作者举例，区分误拨事故与故意（P111）。"
   ],
   "conditions": [
    "“只有经过这种授予，你才能免于种种苛刻的追究”——免责以事先的特殊授予为条件（P010）。",
    "“没有这些，你是没有权利免责的，而这个责，只要对方心头不快、口头自称，你就会有”（P012）。",
    "保密的 0.01% 例外限于对方本与你有重大利益相关、令你有足额盈余的情形（P018）。",
    "L 告知副书记的做法成立的前提是应“在对方开始倾诉之前提前声明”（P014）。",
    "电话轰炸后关系是否还有余地，取决于对方拒接后你是否停打（P041、P042）。",
    "作者对 L 的评断带“极大概率”“很可能”“显然”等限定（P029、P070、P085）。",
    "“一般都是因为当事人已经和父母决裂了，或者对父母能解决问题已经不抱希望”——对隐藏情节的推断带概率限定（P048）。",
    "插手他人家庭责任可取的唯一前提是自觉接受后果、毫无侥幸（P061、P062）。",
    "“如果L老师严守这界限，这场对双方都沉重的折磨也不会发生”——反事实条件（P095）。",
    "看管者的高度警觉以“ta们已经被通知了这个风险”为前提（P035）。",
    "“在我这里，忍不住就是一种故意，同档处罚”以“我这里”为限定；误拨可按事故降档（P110、P111）。",
    "“真真切切的进步”以信息只放在对方可自然回避之处为条件，主动打扰即清零重算（P128、P129）。",
    "时间与场景：叙述涉及疫情期间学校封闭管理、出校就医需隔离三天三次核酸（P032）；文章发表于 2023-12-15。"
   ],
   "rhetoric_and_tone": "训诫式、冷峻的伦理论断与讽刺相杂：大量反问与质问（“为什么头痛无法学习，就意味着可以找L诉苦？”“你算老几？”），密集类比（断腿找邻居、万有引力、高压线、拿汽油灭火、讨债人），典故引用（达摩克利斯之剑、石中剑、“胸怀利器，杀心自起”），以及俚俗调侃（“红孩儿”“优惠券”“免责大酬宾”“刮刮卡”）。结构上以 13 个引用块转述提问者自述、逐段插入作者点评，并用“后文果然也印证了这一点”前后呼应；对提问者用“你”、对泛化读者用“你们”、对 L 用第三人称评断，规则宣示多用“你要……”“绝不要……”。",
   "unresolved_questions": [
    "P002“什么是爱？”是 body 字段、夹在 P001 与 P003 两个引用块之间；question 仅一句、brief 只是正文开头截断，无法确定它属提问者自述还是作者开篇设问，本记录不归给任何一方。",
    "答主（作者）的身份、资历与立场背景文内未说明，其“在我这里”等规则宣示的适用主体不明。",
    "P059“父母无法负担抚养责任，第一顺位的责任人是民政部门”属制度性断言，需外部核查。",
    "P030“人类法/自然法”的区分未给定义，属作者概括用语，作为法学标准术语使用可能失真。",
    "引用块内的提问者叙述（急诊、免责声明书、隔离三天三次核酸、吞药自杀等）均为单方叙述，无法核实，本记录只作引述。",
    "P012“这个责，只要对方心头不快、口头自称，你就会有”中的“责”性质（法律、职业、道德）未限定，可能影响解释。",
    "引用块边界依赖 lexical 标记；作者是否完整引用提问原文、有无删改，无法从本记录确认。",
    "更新时间 2024-12-09 晚于发表时间 2023-12-15，语料未说明是否有修订或版本差异。",
    "文中未说明 L 的最终态度变化与提问者的后续结果，无随访信息。",
    "作者对双方均有评断，但未区分哪些属可确知的内部信息、哪些属基于提问者单方叙述的推断，其判断的信息来源限制需注意。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "为什么头痛无法学习，就意味着可以找L诉苦？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "不去医院却去找隔壁邻居求包扎", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "其实对方应该免责的，但实际上你不会免ta的责。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "拯救的特权是要经过特殊的授予的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "只要对方心头不快、口头自称，你就会有", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "这本是对的，但该在对方开始倾诉之前提前声明。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "“答应保密”应该是一种极其罕见的现象", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "背负这种保密义务绝不可以没有对称的实质补偿", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "要我背负你的秘密，只会降低、贬损你在我心目中的地位", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "觉得自己让对方背负秘密，应该对方向自己感恩", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "这种完全错乱的伦理观势必将在其后的人生中让当事人付出惨烈的代价", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P027", "quote": "是每个人不可推卸的家庭作业", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P028", "quote": "社会不会、也没有这个义务去找你的父母算账", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P029", "quote": "他也极大概率要为自己的傲慢和无知付出代价", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P030", "quote": "自然法是没有这种豁免的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P033", "quote": "抑郁迹象并不是“平时待人接物、生活作息和正常同学无异”就可以否定的", "relation": "contradicts"},
    {"key": "E21", "paragraph_id": "P034", "quote": "抑郁的迹象是会从各种遣词造句、回应对话的方式中流露出来的", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P035", "quote": "你出事的话ta们就会产生巨大的职业责任", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P039", "quote": "是一个极其危险的信号", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P040", "quote": "几乎只有彻底断绝关系这一个选择", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P041", "quote": "这样就还算有转圜的余地", "relation": "qualifies"},
    {"key": "E26", "paragraph_id": "P042", "quote": "那么你已经等于宣判了关系的死刑", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P047", "quote": "为什么电话轰炸自己的大学老师，而不是自己的父母？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P048", "quote": "因为当事人已经和父母决裂了", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P051", "quote": "唯一的解释就是当事人会把父母描述成极端恶劣、愚蠢乃至邪恶的人", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P053", "quote": "这类纠缠往往会自动退散", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P059", "quote": "第一顺位的责任人是民政部门", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P060", "quote": "你未经授权擅自干了ta们的活", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P061", "quote": "真正有爱的人可以无畏这样的残忍安排", "relation": "qualifies"},
    {"key": "E38", "paragraph_id": "P063", "quote": "这才是真正英勇的爱", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P070", "quote": "但很显然，L老师并没有这样的自觉。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P072", "quote": "人要停止这类庸俗的“对等观”", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P074", "quote": "平等根本不体现在“对等处置权”上", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P079", "quote": "逾越了伦理界限，也就是俗称的get personal了", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P080", "quote": "在这类公事关系中都不允许对对方明示", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P085", "quote": "因为所行为善，所以可以救赎徇私的问题", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P086", "quote": "只要我是在行善，是出于信仰还是出于私心有什么关系呢？", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P087", "quote": "就会立刻被重新定性为“老师特别喜欢我所以对我偏爱”", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P091", "quote": "因为宠溺和受宠溺是一种贿赂关系", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P094", "quote": "这个问题只该有一种答案", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P097", "quote": "“吃醋”是一个非常愚蠢的行为，因为它从无好结果。", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P098", "quote": "要用自己的情绪作为对方自由的新边界", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P102", "quote": "哪怕一时得逞，也是在自寻流放", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P107", "quote": "“忍不住”要算意志的失败，不能算故意", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P110", "quote": "在我这里，忍不住就是一种故意，同档处罚", "relation": "supports"},
    {"key": "E59", "paragraph_id": "P114", "quote": "绝不能用“减免处罚”“高抬贵手”的方式帮助", "relation": "supports"},
    {"key": "E60", "paragraph_id": "P117", "quote": "这就已经是敌人才会用的手段了", "relation": "supports"},
    {"key": "E61", "paragraph_id": "P118", "quote": "用敌对手段寻求友谊，这是南辕北辙的做法，逻辑不通。", "relation": "supports"},
    {"key": "E62", "paragraph_id": "P120", "quote": "道歉一定有用，没有没用的可能性", "relation": "supports"},
    {"key": "E63", "paragraph_id": "P121", "quote": "本质上是一种“再来一刀”的刮刮卡", "relation": "supports"},
    {"key": "E65", "paragraph_id": "P126", "quote": "其实指的是“停止主动联系”", "relation": "supports"},
    {"key": "E67", "paragraph_id": "P129", "quote": "你主动打扰，就要清零、重算", "relation": "supports"},
    {"key": "E68", "paragraph_id": "P130", "quote": "对方如果打算来找你就自然会来", "relation": "supports"},
    {"key": "E69", "paragraph_id": "P084", "quote": "徇私是不是善行的合法动机？", "relation": "context"},
    {"key": "E70", "paragraph_id": "P071", "quote": "那我也让你尝尝整天被人打电话是个什么滋味！", "relation": "context"},
    {"key": "E72", "paragraph_id": "P124", "quote": "我该怎么办？", "relation": "context"},
    {"key": "E74", "paragraph_id": "P032", "quote": "副书记和辅导员就是觉得抑郁症一定会自杀", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理健康与抑郁症", "师生关系与校园伦理", "伦理学（责任、免责、特权）", "人际边界与关系修复", "高校学生管理与看管责任"],
   "issue_candidates": ["抑郁症学生的校园管理", "师生边界与 get personal", "保密承诺及其例外", "电话轰炸与情绪勒索", "道歉与关系修复", "父母责任与代为承担", "对等报复观", "吃醋", "“忍不住”能否免责"],
   "text_function_candidates": ["答疑/回应提问", "批评与训诫", "伦理论证", "案例点评"],
   "object_candidates": ["提问者", "L（大学老师）", "L 的妻子", "副书记", "辅导员", "提问者的母亲", "民政部门", "高校/学校", "特蕾莎修女", "消防队员"],
   "working_keywords": ["拯救的特权", "免责", "保密义务", "隐藏情节", "对等观", "身份无关性", "get personal", "徇私", "宠溺", "忍不住", "真真切切的进步", "情绪轰炸", "吃醋"]
  },
  "notes": "本篇为知乎答主对提问者自述的逐段点评式回答：13 个引用块（P001、P003、P013、P032、P036、P046、P071、P078、P096、P106、P116、P119、P124，field=quote）为提问者叙述，不得归给作者；其余 body 段落为作者评断。全文 130 段、无图片节点、正文非空，故 status=read、full_text_checked=true，无需图片核验。P002“什么是爱？”归属存疑，见 unresolved_questions 第 1 条。制度性断言（民政部门顺位、人类法/自然法）只记“待外部核查”，未作裁定。更新时间（2024-12-09）晚于发表时间（2023-12-15），语料未说明版本差异。"
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
