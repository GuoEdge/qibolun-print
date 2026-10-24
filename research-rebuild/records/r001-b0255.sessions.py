# -*- coding: utf-8 -*-
"""批次 r001-b0255 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0255.sessions.py            # 写 out/r001-b0255.out.jsonl
  python3 records/r001-b0255.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0255"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0255.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "becd5793": {
  "analysis": {
   "question_context": "Q001 仅为三字短语“论竞争”，不是完整提问；本文是爱发电平台上的长篇讲演式文章（P021 自称“开讲”，P020 邀读者到评论区补充）。作者先用 P001—P021 复述“内卷论”的主张、示例与归因，并请读者核对有无遗漏；随后自 P022 起转入自己的论证：竞争能否被合谋关闭、烈度能否靠规则削弱、竞争是否净损失，末段给出个人竞争策略（planA/planB）与边界。P001—P021 的命题属被转述的“内卷论者”，不得因 P018 的讽刺语气而直接算作作者主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "复述内卷论：定义、例子A—D、道德规范/顶层设计与成本收益估算、失败归因；请读者补充，然后宣布开讲。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "设问：是否存在没有收益的竞争；以甲乙、资源不匮乏为条件，论证停战共识无法保证，停止备战才是愚蠢。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048"], "summary": "“超然的第三方”执法寓言（老王、张三李四、火影村、尼古拉斯匪帮）：须预付阻断竞争税并维持绝对优势，代价高到宁愿冒险；外部威胁不可免。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067"], "summary": "电影院隐喻的解答：真因是“不停止售票”（无限后来者不认先在共识）；竞争是不可合谋关闭的自然法则，强行干预徒劳且更速败，成功亦走向下一次灭绝危机。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085"], "summary": "烈度能否靠规则削弱：先立“完全消极仍维持相等预期寿命与生育机会”的满意标准；再以总体战与换战场说明政策封堵是打地鼠。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099"], "summary": "烈度长期恒定（仅以死亡为极限的竭尽全力）：优良资源与优质配偶永远相对稀缺，竞争者会顶着濒死极限入场。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113"], "summary": "烈度只取决于参与者人数；古代限于本村本县，现代交通通信使对手变为全国/全球，故根因是竞争者基数增长三四个数量级，而非房价、资本家、政府或工贼。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P114", "P115", "P116", "P117", "P118", "P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130", "P131", "P132", "P133", "P134", "P135", "P136", "P137", "P138"], "summary": "回应“净损失”：价值非物质；竞争额外产出“谁赢了”与“把东西放到赢家手里”两个结果，为社会命脉且无替代品，任何削弱其有效性的行为都在损害群体幸存。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P139", "P140", "P141", "P142", "P143", "P144", "P145", "P146", "P147"], "summary": "唯一改进方向：以防止竞争失效（如门槛过高）为设计目标；义务教育、高考、反垄断等皆为扩大参与资格，非免除竞争。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P148", "P149", "P150", "P151", "P152", "P153", "P154", "P155", "P156", "P157", "P158", "P159", "P160", "P161", "P162", "P163", "P164", "P165", "P166", "P167", "P168", "P169", "P170", "P171", "P172", "P173", "P174", "P175", "P176", "P177", "P178", "P179", "P180", "P181", "P182", "P183", "P184"], "summary": "对称的好消息：奖励与竞争助力同步提高，红海更红而蓝海更蓝；抱怨是自我伤害，选择喊内卷即自愿留在红海。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P185", "P186", "P187", "P188", "P189", "P190", "P191", "P192", "P193", "P194", "P195", "P196", "P197", "P198", "P199", "P200", "P201", "P202", "P203", "P204"], "summary": "如何赢得竞争：planA 全力求胜；planB 必须同样指向胜利，仅能保本的 planB 会变成优先计划并导致自欺。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P205", "P206", "P207", "P208", "P209", "P210", "P211", "P212", "P213", "P214", "P215", "P216", "P217", "P218", "P219", "P220", "P221", "P222", "P223", "P224", "P225", "P226", "P227", "P228", "P229", "P230", "P231", "P232"], "summary": "马克吐温案例：1865 年前的连环失败（送报、排字、引水、从军、伐木淘金）成为作家成就的本钱与蓝海生态位；planB 的秘密在此。", "role": "example"},
    {"unit_id": "U013", "paragraph_refs": ["P233", "P234", "P235", "P236", "P237", "P238", "P239"], "summary": "三条边界：不投入关键资产（信用、身心健康）、不敷衍不保留、失败所得资产仍可用；由此构成 planA_n 的必胜链。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P240", "P241", "P242", "P243", "P244", "P245", "P246", "P247", "P248", "P249", "P250", "P251", "P252", "P253", "P254", "P255", "P256", "P257", "P258"], "summary": "失败链的稀有性（马克吐温及洛克菲勒、李白、颜真卿、唐宗宋祖等）；竞争被界定为借认真与持守生效的分配机制，惩诫献祭信誉健康与他人之爱者。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P259", "P260"], "summary": "结语祝福（英文短句）。", "role": "conclusion"}],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "“内卷”被界定为过度竞争、恶性竞争、无效竞争；内卷论主张以道德规范或社会契约（“顶层设计”）强制限制竞争强度。", "evidence": ["E01", "E02"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "内卷论以露天电影院、中国厂商价格联盟、禁止超额加班与限时学习为例，称存在本可获得的净福利，且建立与监督规范的成本可由这份额外福利支付。", "evidence": ["E03", "E04"]},
    {"claim_id": "C003", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "内卷论把良策迟迟未落地归因于大企业的特殊影响力、地方政府怕失业而消极应付、少数“工贼”，以及房产与消费市场的高压。", "evidence": ["E05"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使资源不匮乏，停止竞争的努力仍然愚蠢：无人能保证共识不被对方撕毁，停战协议不等于停止备战协议。", "evidence": ["E06", "E07"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "达成停战协议之刻即进入“抢先撕毁协议”的新竞争；天真的乡愿等于实际选择自取灭亡。", "evidence": ["E08", "E09"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "由“超然的第三方”保障反内卷协议，须预付并长期缴纳“阻断竞争税”、维持其绝对优势，代价高到当事人宁愿冒险。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老电影院全员站立的真因是“不会停止售票”——无限后来者不承认先在共识，任何美好座次安排都会被新人击穿。", "evidence": ["E13", "E14", "E15", "E16"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无限竞争是不容人类自己合谋关闭的自然法则，中央政府、智者先贤、伟大统帅都没有发言干预的资格；强行干预首先因大量徒劳增加生存成本并更快导致失败。", "evidence": ["E17", "E18", "E19", "E20"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "干预者即便“成功”过上相安无事的闲暇生活，也只是走上下一次集体灭绝的危机。", "evidence": ["E21"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生存竞争是绝对总体战：对手会在受挫领域之外另开战场，政策封堵是打地鼠，最终耗尽财政收入与公信力。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生存竞争的烈度长期恒定，即“仅以死亡为极限的竭尽全力”；优良资源相对争夺者永远稀缺，稀缺科目被递补而不会变空。", "evidence": ["E25", "E26"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代竞争焦虑的根因是竞争者基数增长三四个数量级（免费义务教育、现代医疗、交通与信息技术），而非房价、资本家、政府或“工贼”。", "evidence": ["E27", "E28"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "竞争的社会净结果除杯子归属外还产出“到底谁赢了”与“将这件东西放到了赢家手里”两个答案，其价值在宏观时间尺度上足以抵消争夺损耗且还有剩余。", "evidence": ["E29", "E30", "E31"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这两个结果是社会命脉，任何降低其客观有效性的行为——无论出于何种政治正确的美好愿望——都在破坏群体的幸存机会。", "evidence": ["E32"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "竞争的唯一改进方向是以恰当设计防止竞争失效（如防止门槛过高、参赛者过少）；义务教育、统一高考、反垄断、破产法、基本保障都是为扩大参与资格而非免除竞争。", "evidence": ["E33", "E34"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "交通与信息技术使竞争者与竞争烈度上升，但奖励与竞争助力同步提高；对积极主动者是变容易，真正更残酷的是被生存危机押进场的“菜鸟”。", "evidence": ["E35", "E36"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "红海更红而蓝海更蓝；问题不是红海为何更红，而是更蓝的蓝海为何与你无缘，且世界对穷人与富人从未像今天这样公平——至少在中国如此。", "evidence": ["E37", "E38"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抱怨本身就是损失，是实打实的自我伤害，会取消合作、传授、订单与家人的期待。", "evidence": ["E39"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "合格的 planB 目标不是“保本”而是同样指向胜利；绝对保本的 planB 会成为优先计划，使 planA 变成自欺欺人。", "evidence": ["E40", "E41"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "马克吐温在成为作家之前的小学生、送报工、排字工、引水员、士兵、伐木者、淘金客身份上全部失败，这些失败恰是其作家成就的最大本钱与蓝海生态位。", "evidence": ["E42", "E43"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "尽力的边界在于健康与信用的可持续性不受损害：不投入关键资产（未来信用、生理与心理健康），但也不可不认真、不尽力。", "evidence": ["E44", "E45"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "竞争被描述为“必须借助认真和持守而生效的分配机制”，唯独惩诫把信誉、健康乃至他人的爱献祭给“赌/战神”的人。", "evidence": ["E46", "E47", "E48"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "守住边界者的必胜链迟早兑现（区别只在 n 值），孤注一掷者迟早必败。", "evidence": ["E49", "E50"]},
    {"claim_id": "C024", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "没有负责任的领导者会为一些人的软弱而背叛整个社会的前途——除非因为某种原因，他们没有负责。", "evidence": ["E51", "E52"]},
    {"claim_id": "C025", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只能指望“不必付出那么大规模代价就可以分出胜负”的改进尝试，但不要高估这种改进的效力。", "evidence": ["E53", "E54"]},
    {"claim_id": "C026", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者在展开论证前请读者核对：对“内卷论”的这一总结是否有遗漏，并要求到评论区补充。", "evidence": ["E55"]}],
   "argument_steps": [
    "复述“内卷论”：定义、例子A—D、以道德规范/顶层设计限制竞争强度、成本可由额外福利支付、失败归因，并请读者补漏（P001—P021）。",
    "设问是否存在无收益的竞争；以甲乙与资源不匮乏反推：停战共识不可保证，停止备战才是愚蠢（P022—P030）。",
    "以老王/张三李四/火影村寓言检验“超然的第三方”，得出阻断竞争税不可承受且外部威胁仍在（P031—P048）。",
    "重解电影院例子：病根是不停止售票（无限后来者）；竞争是不可合谋关闭的自然法则，干预徒劳（P049—P067）。",
    "先立“完全消极仍维持同等预期寿命与生育机会”的满意标准，再以总体战与打地鼠论证规则无法降低烈度（P068—P085）。",
    "论证烈度长期恒定：资源与配偶永远相对稀缺，总有对手顶着濒死极限竞争（P086—P099）。",
    "把烈度归因于唯一变量——竞争者人数，指出基数因教育与技术增长三四个数量级（P100—P113）。",
    "回应“净损失”质疑：价值非物质，竞争产出“谁赢了”与“东西归赢家”两个结果，是社会命脉且无替代（P114—P138）。",
    "界定唯一改进方向：防止竞争失效、扩大参与资格，而非免除竞争（P139—P147）。",
    "给出对称的好消息与态度要求：奖励与助力同步提高，抱怨是自伤（P148—P184）。",
    "提出 planA/planB 结构，强调 planB 必须同样指向胜利（P185—P204）。",
    "以马克吐温生平为例证，归纳三条边界与 planA_n 必胜链（P205—P239）。",
    "以失败链的稀有性推及历史人物，把竞争重述为认真与持守才生效的分配机制，给出结局判断与祝福（P240—P260）。"],
   "concept_usage": [
    {"term": "内卷", "meaning": "先作为被复述的理论术语出现（过度/恶性/无效竞争）；作者未自设定义，全篇当作反驳对象。", "evidence": "P001", "ambiguity": "定义在引号内属内卷论，非作者；作者从未给出自己的定义。"},
    {"term": "竞争／生存竞争", "meaning": "以生存概率、配偶与后代为赌注、无领域边界的角逐；作者称其为绝对总体战且不可合谋关闭。", "evidence": "P077", "ambiguity": "“竞争”与“生存竞争”常互换，未区分经济竞争与生存竞争。"},
    {"term": "阻断竞争税／反内卷税", "meaning": "寓言中为维持第三方执法者绝对优势而须事前预收、逐年补缴的保护费（文中为60%）。", "evidence": "P037", "ambiguity": "税率为寓言设定，非对现实政策的量化。"},
    {"term": "自然法则", "meaning": "指无限竞争不容人类合谋关闭，干预者无资格置喙。", "evidence": "P064", "ambiguity": "属自然化断言，未给论证形式或检验方式。"},
    {"term": "总体战", "meaning": "竞争不局限单一领域，一处受挫即转向其他战场。", "evidence": "P077", "ambiguity": "无。"},
    {"term": "竞争者基数", "meaning": "作者认定的烈度唯一变量：参与竞争的实际人数。", "evidence": "P100", "ambiguity": "“只取决于一个变量”为断言，未处理资源、制度等变量。"},
    {"term": "价值", "meaning": "否认价值等于物质，把社会层面的价值落在“谁赢了”与“把东西放到赢家手里”两个结果上。", "evidence": "P120", "ambiguity": "未给正面定义，只以反例与结果说明。"},
    {"term": "planA／planB", "meaning": "planA 全力求胜；planB 为失败后仍指向胜利的下一场竞争，不得以“保本”为目标。", "evidence": "P194", "ambiguity": "“同样指向胜利”未给可操作判据。"},
    {"term": "关键资产", "meaning": "未来的信用、生理健康与心理健康，构成“尽力”的边界。", "evidence": "P234", "ambiguity": "界限刻度由作者自述（P237），无通用标准。"}],
   "examples_and_targets": [
    "露天电影院前排站起致全员站立（内卷论示例A，转述；作者自解为“不停止售票”，P003、P051）",
    "中国厂商已具压倒性优势可结价格联盟（理论示例B，转述，P005）",
    "禁止超额加班法令的两结果：岗位增加、劳动者普遍受益（理论示例C，转述，P006—P008）",
    "阿里、华为被指不应以高工资补偿换取长劳动时间（内卷论的批评对象，转述，P009—P010）",
    "国企员工与公务员被列为“条件优厚者”（转述，非作者判断，P008）",
    "限时学习、禁止作业与处罚补课（理论示例D，转述，P011）",
    "老王头、张三、李四、火影村、尼古拉斯匪帮的坦克（作者自造寓言，说明第三方执法成本与外部威胁，P033—P048）",
    "60%“反内卷税”、“张三买辆车得先给老王买辆更好的”（作者寓言的量化与类比，P039—P040）",
    "三门课→学区房、抽签→私校、禁私校→少数民族身份、课外→体育艺术与微整容（作者举例说明换战场，P083）",
    "“永远是8成的男性，去追逐争夺那较好的3成女性”（作者稀缺性断言，无出处，P091）",
    "免费义务教育、现代医疗、高效交通、新信息技术（作者认定的竞争者基数膨胀原因，P110）",
    "义务教育、统一高考、反垄断、破产法、基本保障（作者举为扩大参与资格的措施，P140）",
    "快递、互联网、两百里外的天然气、气炉、机械锻锤（作者说明竞争助力同步提高，P155、P158—P161）",
    "马克吐温：先隐名描述生平（1835年生、七兄妹排老六、1847年丧父、印刷厂送报、1851年排字、1858年轮船引水员、弟死于爆炸、参加南方民兵、1861年随兄搞林业矿业、1862年入报社、1865年发表首篇代表作），后点名并给出2006年百人第16位、1898年63岁还清投资债务（作者核心案例，数据需外部核查，P206—P223）",
    "钱德勒与宋飞向马克吐温“脱帽致敬”（作者的类比修辞，P219）",
    "洛克菲勒、李白、颜真卿、唐宗宋祖、明祖清宗、拿破仑、俾斯麦、马恩列斯毛朱彭邓（作者列举“早年失败→在所分配角色里所向无敌”的例证，P247—P248）",
    "“恶俗女”“资本家”“工贼”等（作者列为被错误归因的对象，属修辞列举与反驳靶子，P107—P108）"],
   "conditions": [
    "理论复述以其自身前提呈现：P005 以“理论上显然存在一种政策的空间”开启价格联盟设想。",
    "甲乙推演的前提是“把‘资源匮乏，两个只能活一个’这个条件……一并拿掉”，且“只要停止竞争，甲乙至少目前都可以活”（P024—P025）。",
    "第三方方案以“要维持住老王的优势”与事前预收、每年补交“阻断竞争税”为条件（P037）。",
    "电影院结论以“不停止售票，无限循环播放，无限放一切人入场”为条件（P056）。",
    "“不必内卷”的唯一例外被限定为“除非你有本事停止售票——先让人类断子绝孙”（P062—P063）。",
    "干预失败的断言含让步假设：“而如果ta们竟然‘成功’了”（P066）。",
    "改进方向被限定为“不要高估这种‘改进’的效力”（P146），并以“除非因为某种原因，ta们没有负责”为限定（P143）。",
    "必胜链以“这尽力的边界在于健康、信用的可持续性不受损害”为边界（P237）。",
    "公平性断言被作者自限为“至少在中国是毫无疑问的如此”（P176）。"],
   "rhetoric_and_tone": "讲演/训诫体：第二人称“你们/你”直接施压，反复以“看懂没有？”“明白了吗？”设问推进；先以看似顺从的长篇复述铺垫“内卷论”，再以“每思及此，能不令人愤恨扼腕耶！”“卷死活该？”与“难得糊涂”“且枯燥”等反讽收束，属先扬后抑的诱敌结构。大量使用寓言（老王头、火影村、尼古拉斯匪帮）与隐喻（不停止售票、红海/蓝海、菜鸟屠宰场、打地鼠、锅盖、切开胸膛救心脏），并以“自然规律和数学”“为人类设计竞争的那一位”等权威化与准神学措辞加持。结尾改用英文祝福（Fight your good fight with all you can spare / May the force be with you all.）。全篇用“ta们”作中性第三人称，夹杂口语与网络语（卷、工贼、洗洗睡、搬砖）。",
   "unresolved_questions": [
    "无图片节点，图片核验不适用；P001—P260 已全部读完，status=read、full_text_checked=true。",
    "Q001 仅“论竞争”三字，无法确定是否即提问者所问；被复述的“内卷论者”未点名任何来源。",
    "P024“这个条件爱你都一并拿掉”疑为录入或转写残留，文义应为“也”，需版本核对。",
    "P138 结尾“谁也没有资格在自然规律和数学面前**”以星号中断，疑有脱字或删词，原句不可知。",
    "P111 引号不配对，P181“从按抱期待”、P072“指着”疑为错字；均按原文保留未改。",
    "马克吐温生平数据、《大西洋月刊》2006 年百人第16位、钱德勒与宋飞的致敬说法，均需外部核查。",
    "“烈度长期恒定”（P086）与“8成男性追3成女性”（P091）无数据或文献支持，需外部核查。",
    "P249“为人类设计竞争的那一位”含设计论/神学预设，指向未说明，可能影响结论解释。",
    "P118—P119 以物质能量守恒归谬“所有权转移全是净亏损”，其推论有效性需外部核查。",
    "体裁与版本不明：P020—P021 显示可能是讲演或视频稿文字版，平台记录未给媒介与修订信息。",
    "P247 以省略号列举历史人物，省略部分与列举标准不可知。"],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "是在指“过度竞争”，“恶性竞争”，“无效竞争”", "relation": "context"},
    {"key": "E02", "paragraph_id": "P013", "quote": "来达成和强制贯彻某种对竞争强度的限制性规则", "relation": "context"},
    {"key": "E03", "paragraph_id": "P004", "quote": "那么所有人都可以享受净福利", "relation": "context"},
    {"key": "E04", "paragraph_id": "P005", "quote": "本来都可以赚更多钱的", "relation": "context"},
    {"key": "E05", "paragraph_id": "P016", "quote": "是因为大企业动用自己的特殊影响力在阻挠这种政策的实施", "relation": "context"},
    {"key": "E06", "paragraph_id": "P027", "quote": "双方都不能保证共识不会被对方撕毁", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P028", "quote": "那只是停战协议，可不是停止备战协议", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P029", "quote": "双方就天然的进入了抢夺抢先撕毁协议的优势地位的新竞争", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P030", "quote": "任何天真的乡愿，都是在实际选择自取灭亡", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P037", "quote": "必须得是没出事之前先预收“阻断竞争税”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P039", "quote": "ta得先给老王买辆更好的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P040", "quote": "不需要缴纳60%“反内卷税”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P051", "quote": "它们不会停止售票", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P054", "quote": "新的挑战者不会承认任何的先在共识", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P056", "quote": "只会给这些后来人留下匪夷所思的美好破绽", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P058", "quote": "是忘记了参与竞争的并不只有现在进场的玩家", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P062", "quote": "你也不要幻想可以“不必内卷”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P064", "quote": "无限的竞争是不容人类自己合谋关闭的自然法则", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P064", "quote": "根本就没有发言干预的资格", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P065", "quote": "都必定首先会因为大量的徒劳而产生额外的生存成本", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P066", "quote": "ta们也只是走上了下一次集体灭绝的危机", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P077", "quote": "生存竞争是一种绝对总体战", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P083", "quote": "你规定入学只准考三门课，对方就会把学副科的资金转向去买学区房", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P084", "quote": "你也不可能做到用政策降低生存竞争的烈度", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P086", "quote": "仅以死亡为极限的竭尽全力", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P092", "quote": "永远会是稀缺的", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P109", "quote": "而是那个增长了三四个数量级的竞争者基数", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P110", "quote": "带来的这个一眼看不到尽头的对手基数", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P124", "quote": "它还额外得到了一个答案", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P125", "quote": "足以在宏观时间尺度上抵消", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P128", "quote": "而就是“到底谁赢了”和“将这件东西放到了赢家手里”这两个结果", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P132", "quote": "实质上都是在破坏群体的幸存机会", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P139", "quote": "只有一种改进的方向，就是通过恰当的设计，防止竞争的失效", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P141", "quote": "那是为了让参与社会总竞争的资格尽可能的扩大化", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P148", "quote": "生存竞争的烈度只会越来越大", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P164", "quote": "烈度提得有多高，则奖励亦有对等的提高", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P168", "quote": "而蓝海却在变得更蓝", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P174", "quote": "这个世界对穷人和富人，从来没有像今天这样公平", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P178", "quote": "抱怨本身就是损失，是实打实的自我伤害", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P194", "quote": "合格的planB的目标不是“保本”", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P201", "quote": "一定会成为优先计划", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P226", "quote": "正是因为他作为小学生、送报工、排字工人、引水员、士兵、伐木者、淘金客全都失败了", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P227", "quote": "这些失败，恰恰正是他最后生花妙笔的最大本钱，最大优势", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P234", "quote": "你不能投入你的关键资产", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P237", "quote": "这尽力的边界在于健康、信用的可持续性不受损害", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P249", "quote": "竞争根本不是一个关于“胜败”的机制", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P250", "quote": "它其实只是一种必须借助认真和持守而生效的分配机制", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P252", "quote": "总要把信誉、健康乃至他人的爱献祭给“赌/战神”的人", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P257", "quote": "前者迟早必胜，早不如迟", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P258", "quote": "后者迟早必败，迟不如早", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P142", "quote": "根本就没有负责任的领导者", "relation": "qualifies"},
    {"key": "E52", "paragraph_id": "P143", "quote": "除非因为某种原因，ta们没有负责", "relation": "qualifies"},
    {"key": "E53", "paragraph_id": "P144", "quote": "不必张三李四王五付出那么大规模的代价就可以分出胜负", "relation": "qualifies"},
    {"key": "E54", "paragraph_id": "P146", "quote": "不要高估这种“改进”的效力", "relation": "qualifies"},
    {"key": "E55", "paragraph_id": "P019", "quote": "有漏掉什么吗", "relation": "context"}]
  },
  "provisional_tags": {
   "domain_candidates": ["社会理论", "经济学（竞争与资源配置）", "政治哲学（政府能否限制竞争）", "人生策略/成功学"],
   "issue_candidates": ["内卷与过度竞争", "反内卷政策与“顶层设计”", "竞争能否被规则削弱", "竞争者人数与竞争烈度", "竞争的净收益与价值", "个人竞争策略（planA/planB）"],
   "text_function_candidates": ["论辩", "反驳", "讲演", "举例说理", "训诫劝告"],
   "object_candidates": ["内卷论者", "中央政府", "地方政府", "阿里", "华为", "国企员工与公务员", "老王/张三/李四（寓言人物）", "尼古拉斯匪帮", "马克吐温", "美国", "中国", "火影村"],
   "working_keywords": ["内卷", "过度竞争", "无效竞争", "阻断竞争税", "反内卷税", "顶层设计", "绝对总体战", "竞争者基数", "红海/蓝海", "planA/planB", "保本", "关键资产"]
  },
  "notes": "本批仅 1 篇（oversize，正文 11870 字、260 段）；无图片节点，图片核验不适用；P001—P260 全部读完，status=read、full_text_checked=true。归属处理：P001—P021 为对“内卷论”的复述与举证，定义、例子A—D、顶层设计主张、成本收益估算与失败归因均记为 opponent_view/attribution=opponent；作者仅以反讽显示立场，未据反讽归为作者主张；P019 请读者补漏记为 open_question。原文瑕疵按原样保留：P024“爱你”、P138 结尾“**”、P111 引号不配对、P181“从按抱期待”、P072“指着”；正文与 lexical 无分歧（仅 paragraph 260 个）。事实性数据均未外部核查，已登记于 unresolved_questions。"
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
