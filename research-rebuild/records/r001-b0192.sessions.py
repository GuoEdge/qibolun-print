# -*- coding: utf-8 -*-
"""批次 r001-b0192 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0192.sessions.py            # 写 out/r001-b0192.out.jsonl
  python3 records/r001-b0192.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0192"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0192.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "4660735d": {
  "analysis": {
   "question_context": "本文回应知乎问题“俄罗斯那么大为什么打乌克兰那么吃力？”（提问者立场不计入作者）。作者开篇声明完全同意某答案里引用的对俄军营战斗群特点分析，随即反对该分析把这些“问题”定性为“单纯的缺陷”，并以其对俄军战略任务与战场条件的理解逐条反驳，兼评俄乌战争第一阶段的战术、战报与认知战。文中所述战况截至2022年4月初第一阶段。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "表态：同意所引分析对营战斗群特点的描述，但反对把这些问题定性为“单纯的缺陷”，称此定性傲慢且危险。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "反驳“俄军犯错”：不存在“六边形部队”；改革是自身条件与战略任务的权衡；以中俄演习表现断言犯错不合逻辑。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "核心解释：对抗美军/解放军对俄是核武力问题，所引短板多属伪问题、恰是俄军用意；作者据此对俄赢面乐观。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021"], "summary": "回应“需外围翼护”：克里米亚、叙利亚、顿巴斯均有当地亲俄民兵补位。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024"], "summary": "回应“火力输出不足”：营战斗群始终在黑海舰队巡航导弹射程内作战，黑海舰队未参加中俄演习。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026"], "summary": "回应“持续突击能力不足”：反问哪支俄军被分配了“持续突击任务”。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054"], "summary": "回应“难以后送”：俄军无攻坚任务、高速机动，乌军指挥混乱难以拦截；乌军战果有限且多伪造；俄军少量失误反证第一周成功。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P055", "P056", "P057", "P058", "P059"], "summary": "回应“炮兵配比过强”：确实只做围困与火力支援；部署属“结硬寨打呆仗”，乌军偷袭代价高。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080"], "summary": "相持阶段：乌军两类战果手段代价高难持续；视频战果打折后≈全部战果≈俄军通报。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098"], "summary": "信息战与士气：俄军以“有报必信”和极简通报消耗乌军可信度；乌军战报难以为继、士兵靠药物维持。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P099", "P100", "P101", "P102", "P103"], "summary": "旁证：引外链与战前报道说明乌军吸毒旧况；虐杀俘虏、滥杀平民并上传，显示前线部队精神近崩溃。", "role": "example"},
    {"unit_id": "U012", "paragraph_refs": ["P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114", "P115"], "summary": "推论：乌军无力执行复杂任务、可能轻微袭扰即溃散；药物与偏执导致对平民施暴。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P116", "P117", "P118", "P119", "P120", "P121", "P122"], "summary": "布查：真相或永不可得，以平民是否追随俄军撤走为判据；斥“卫国战争”叙事，随后拉回主题。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130", "P131", "P132", "P133"], "summary": "回到主题：指挥“原始”是为前线临机决断与士气，“这不是bug，这是feature”，是红军的军魂。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P134", "P135", "P136", "P137", "P138", "P139", "P140", "P141"], "summary": "营级编制目的：铁路战略机动甩开敌人；作为“最小可用单位”即插即用，成为“拔不动的钉子”。", "role": "claim"},
    {"unit_id": "U016", "paragraph_refs": ["P142", "P143", "P144", "P145", "P146", "P147", "P148", "P149", "P150", "P151", "P152", "P153", "P154", "P155", "P156", "P157", "P158"], "summary": "适用条件：依赖空优、远程火力、当地友军与核盾牌；在该类条件下近乎无敌，邻国再无加入北约机会。", "role": "qualification"},
    {"unit_id": "U017", "paragraph_refs": ["P159", "P160", "P161", "P162", "P163", "P164", "P165", "P166", "P167", "P168", "P169"], "summary": "战略外推：以乌克兰为“头羊”根绝他国倒向西方；中亚与一带一路受益，北约恐已开始结束。", "role": "claim"},
    {"unit_id": "U018", "paragraph_refs": ["P170", "P171", "P172", "P173", "P174", "P175", "P176", "P177", "P178", "P179", "P180", "P181", "P182", "P183", "P184", "P185", "P186", "P187", "P188", "P189", "P190", "P191", "P192", "P193", "P194", "P195"], "summary": "结尾劝诫：警告台湾网军勿投入认知战；中国“坐庄”等结果再下注；建议检阅自身认知。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者同意所引分析对营战斗群特点的描述，但绝不同意把这些问题定性为“单纯的缺陷”，认为该定性傲慢且会致指挥官惨败。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上根本不存在“六边形部队”。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "俄军改革是自身条件与战略任务的权衡取舍，不是“低级错误”；以中俄演习表现断言俄军犯错是逻辑错误，因其不以解放军或美军为假想敌。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C004", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被引分析主张营战术群需外围翼护、火力输出不足、持续突击能力不足、难以后送、炮兵配比过强不利巷战，并视之为俄军缺陷。", "evidence": ["E11", "E24"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对俄而言“对抗美军/解放军”是单纯的核武力问题，无常规对抗需求；所引短板在俄战略思想里几乎全是伪问题，反而正是其用意所在。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者据此对乌克兰之战俄军赢面很大持乐观估计。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "回应“需外围翼护”：克里米亚、叙利亚、顿巴斯恰好都有有相当能力的当地亲俄民兵补位。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "回应“火力输出不足”：营战斗群一直在黑海舰队巡航导弹射程内作战，从未越雷池一步。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问否认“持续突击能力不足”：哪支俄军被分配了“持续突击任务”？", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者自称敢大胆地说：俄军这次人员伤亡高度接近俄军自己的通报，甚为轻微。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "俄军无攻坚任务、集中兵力高速机动直扑要地，突击阶段不会遭遇乌军严肃阻击，损失源于快速机动；所谓“大幅虚报损失”只是基于“俄军肯定撒谎”的臆断。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "首轮导弹攻击使乌军指挥、情报、通讯陷入混乱，故“乌军造成重大杀伤”如同军事奇迹；乌军未能弯折俄军进军直线，其视频战果几乎就是该阶段全部战果。", "evidence": ["E19", "E20", "E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "俄军明显失误只有留人看守损坏装备、侦查分队穿越居民点遭袭；这种“低级错误”反证第一周行动高度成功。", "evidence": ["E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "回应“炮兵配比过强”：确实只做围困和火力支援，未打巷战；部署属“结硬寨打呆仗”，乌军偷袭会先撞上前出步兵并暴露于炮火与反炮兵雷达。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "乌军两类战果手段都难持续：肩扛导弹的天生缺陷使胜率偏向俄空军；渗透偷袭弹药少、幸存度低，无法造成成规模杀伤。", "evidence": ["E27", "E28", "E30"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "乌军击落视频数量已高度接近其击落总数，没有多少“未被记录的击落”——乌军拿命换宣传素材，不会错过任何一次。", "evidence": ["E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "乌军视频战果存在大量拙劣伪造（甚至拿T64装作T72），打折后已≈其全部战果，也极大接近俄军自己的通报。", "evidence": ["E31", "E32", "E33"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "俄军靠“有报必信”与极简通报撑过信息战早期、夺走乌军认知战的可信度；第二阶段无法掩盖的战果释放后，乌军认知战会彻底破产。", "evidence": ["E34", "E35"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "乌军已进入“抱头挨打，无隙可乘”的极端被动状态；前线部队精神已到崩溃边缘，命令其向前靠拢可能在极轻微袭扰下溃散。", "evidence": ["E36", "E39", "E40"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "乌军不靠强效镇静剂和兴奋剂无法正常作息，作者据此判断其必须成建制、大面积吸毒维持战斗力（以外链与战前报道为旁证），且药物与偏执会导致对平民成规模施暴。", "evidence": ["E37", "E38", "E41"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "布查“大屠杀”也许永远没有确切真相；作者以平民是否宁可追随俄军撤走、边界居民是否向俄方逃亡为判据，称其胜过“欧盟调查团”一万倍。", "evidence": ["E42", "E43"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "指挥“原始”是因现场信息对决策影响重大、须由师级以上军官在听得见炮声处临机决断且关乎士气；“这不是bug，这是feature”，是红军的军魂。", "evidence": ["E44", "E45", "E46", "E47"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "营级编制为依靠铁路运力实现战略机动、甩开被动部署的敌人，并作为“最小可用单位”立刻投入作战；其目的几乎可化为“成为一颗拔不动的钉子”。", "evidence": ["E48", "E49", "E50"]},
    {"claim_id": "C024", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "在空优、远程火力支援可及、当地友军可得的前提下，除非核弹直接命中炮兵阵地，否则没有常规陆军能在支援火力倾泻前拔掉它；它从未打算用于没有空优、海空火覆盖不到的战场。", "evidence": ["E51", "E52", "E53"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该体制基于“周边有事”设想与俄国力条件精心设计、近乎完美适配；能打垮它的对手被核盾牌拒止或结为准盟友，未加入北约的前苏联成员国将再无机会加入。", "evidence": ["E53", "E54", "E55"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "俄拿乌克兰开刀因为它是前苏联国家里最难打的“头羊”，其被斩首将根绝他国倒向西方的妄念；北约恐已开始结束，除非顶着核弹孤注一掷。", "evidence": ["E56", "E57", "E58"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国完全可以接受所谓俄罗斯战败，中国之强已强到无视规则的地步。", "evidence": ["E59", "E60"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者警告台湾网军：这不是他们该掺合的游戏；他要庄家赔的“恐怕就是你们”，建议其砍断把自己绑在幻想幽灵船上的缆绳。", "evidence": ["E61", "E62", "E63"]}
   ],
   "argument_steps": [
    "表态：同意所引分析，反对“单纯的缺陷”定性。",
    "前提否证：不存在“六边形部队”；改革是权衡取舍。",
    "指出所引批评的逻辑错误：俄军不以解放军/美军为假想敌。",
    "核心解释：对抗美军/解放军是核武力问题，短板多为伪问题。",
    "逐条回应：翼护→亲俄民兵；火力→黑海舰队；突击→无此任务；后送→无攻坚。",
    "突击阶段推演：乌军难以拦截，只有民兵骚扰。",
    "以乌军指挥瘫痪、进军直线未受阻反证“大量杀伤”无据。",
    "承认少量失误，转为第一周成功的旁证。",
    "回应炮兵配比：只做围困火力支援，结硬寨打呆仗。",
    "相持阶段：乌军两类手段不可持续，视频战果≈全部战果≈俄军通报。",
    "信息战：俄军“有报必信”将夺走乌军可信度。",
    "由乌军精神崩溃与吸毒推论其战斗力与对平民施暴。",
    "以平民流向为判据谈布查，斥“卫国战争”，拉回主题。",
    "回到主题：指挥“原始”是feature，是红军军魂。",
    "解释营级编制的战略机动与“拔不动的钉子”作用。",
    "归纳适用条件，断言该类战场无敌。",
    "外推：头羊论、中亚、北约的结束、中国“坐庄”。",
    "结尾劝诫台湾网军，附延伸阅读。"
   ],
   "concept_usage": [
    {"term": "营战术群／营战斗群／战术营", "meaning": "俄军以营为基干、配属坦克炮兵防空，可铁路战略机动并在其他军种掩护下钉守要地的合成战术单位。", "evidence": "P057", "ambiguity": "文中三个称呼混用，未给编制细节。"},
    {"term": "六边形部队", "meaning": "各方面无短板的理想部队；用于否证“短板即缺陷”的前提。", "evidence": "P006", "ambiguity": "借用的比喻，未注出处。"},
    {"term": "伪问题", "meaning": "从俄军战略思想看并不成立、无须解决的问题。", "evidence": "P017", "ambiguity": "判断标准由作者给出，未逐条论证。"},
    {"term": "核武力问题", "meaning": "作者对俄与美军/解放军常规对抗需求的定位：归为核力量层面。", "evidence": "P014", "ambiguity": "未说明核门槛与常规冲突的界线。"},
    {"term": "结硬寨打呆仗／拔不动的钉子", "meaning": "作者对营战斗群防御样式的概括：筑阵地、以火力环带固守、几乎无法被常规陆军拔除。", "evidence": "P058", "ambiguity": "比喻性概括，未量化“无法拔除”的时限。"},
    {"term": "拉胯战术", "meaning": "转引他人对俄军编制的贬称，并在文中反转其贬义。", "evidence": "P165", "ambiguity": "贬称来源未标明。"},
    {"term": "bug／feature", "meaning": "作者用英文词区分“设计失误”与“有意设计”，主张俄军指挥体制属后者。", "evidence": "P132", "ambiguity": "英文词与中文正文混用。"},
    {"term": "认知战", "meaning": "本文特指乌方及其支持者的信息与舆论作战，作者判断其将破产。", "evidence": "P081", "ambiguity": "与舆论战、信息战交替使用，未作区分。"},
    {"term": "绿区", "meaning": "营级战斗群以火力圈出的受控区域，友军随后进入。", "evidence": "P149", "ambiguity": "未给范围标准，与前文“八十公里”关系不明。"}
   ],
   "examples_and_targets": [
    "被引答案的营战斗群短板清单（翼护、火力、突击、后送、炮兵配比）：引用并反驳的对象（P019、P022、P025、P027、P055）。",
    "克里米亚、叙利亚、顿巴斯：作者证据——当地亲俄民兵可补翼护（P020）。",
    "黑海舰队巡航导弹射程与中俄演习：作者证据，黑海舰队未参演（P023、P024）。",
    "2022年俄军高速突击与“不攻坚”下的最短直线轨迹：作者证据（P026、P048）。",
    "乌军“击落直升机”“拖走损坏坦克”视频：作者指为可视频化战果乃至伪造（T64装T72）（P050、P074、P075）。",
    "超低空攻击机（su-25、34）对肩扛导弹的推演：作者例证（P063、P064）。",
    "taskandpurpose.com 外链及中文报道《乌克兰军队如何堕落？》《乌军俘虏身上搜出毒品》：旁证（P099—P101）。",
    "布查“大屠杀”与“欧盟调查团”：预判与反驳对象（P116、P117、P119）。",
    "美军将官在亚利桑那电战基地“打战棋游戏”：对比与修辞材料（P123）。",
    "“四百公里外的空调参谋”：作者对远程指挥的贬称（P126、P131）。",
    "前苏联/独联体国家名单（亚美尼亚、阿塞拜疆、格鲁吉亚、摩尔多瓦、中亚各国乃至叙利亚）：推演对象（P159）。",
    "阿拉伯帝国垄断丝路、一带一路与北极航道：类比与推演（P160）。",
    "泽连斯基（文中亦作“泽林斯基”）与“抠像部队和演讲戏码”：嘲讽对象（P090、P169）。",
    "台湾网军：训诫与警告对象（P170、P182）。",
    "中国“坐庄”赌博比喻：修辞材料（P173—P182）。"
   ],
   "conditions": [
    "依赖压倒性空优、远程火力支援可及和当地友军可得（前苏联国家必有大量俄族或俄语人群）（P152）。",
    "从未打算用于海空火覆盖不到、没有空优的战场（P142）。",
    "八十公里场域内，除非核弹直接命中炮兵阵地，常规陆军无法在支援火力到达前拔除它（P140）。",
    "判俄军批评无效的前提：俄军不以解放军或美军为假想敌，演习表现非评价标准（P010、P011）。",
    "突击阶段判断依赖：乌军措手不及、重兵集团不敢出城、接触者多为缺训练缺补给的民兵（P030—P036）。",
    "俄军伤亡轻微之说带推测语气（“我敢大胆的说”）（P028）。",
    "乌军吸毒之说以“战前报道”与外链为旁证，非本文独立核实（P099、P100）。",
    "布查只给判据不给结论：看平民是否追随俄军撤走、边界居民是否向俄方逃亡（P116—P119）。",
    "设想若这些“毒虫”保住政权，被枉杀者将被钉在耻辱柱上（P111）。",
    "中国可接受俄战败的附带条件：俄不进入西亚和阿富汗一线、不再勾搭越南（P161）。",
    "北约结局的例外：“除非它有胆顶着核弹孤注一掷”（P166）。"
   ],
   "rhetoric_and_tone": "论战式答问，语气强硬自信：先声明同意所引分析的事实描述，再以“但是，我绝不同意……”转折定调。大量反问（“你说巧不巧？”“难道为了向网友求赞吗？”“怎么拦截？怎么阻击？”“但谁又能换他们的防呢？”）与“——真巧”的逐条反驳结构；讽刺与贬称密集（“拉胯”“毒虫”“抠像部队”“四百公里外的空调参谋”“老子训儿子”），并夹叙夹议地推演战场。后半段由战况评论转为对台湾网军的训诫与“坐庄”赌博比喻，间以外部链接、报道标题作旁证。",
   "unresolved_questions": [
    "图片未核验：IMG001（//asset.sooon.ai/p/2022-04/06/61c320c9603acd30798164bec329d413.jpg）位于正文第99段外链之后，内容未经查看，需人工/多模态复核。",
    "作者“完全同意”的那篇答案在本文未给出链接、作者或标题，其原始表述无法核对；本文只能按引号复原其观点（P019、P022、P025、P027、P055）。",
    "正文与 lexical 结构存在未覆盖片段（P003、P099、P101、P195 标记“lexical未覆盖片段”），且 lexical 含 text 未包含的图片节点，结构核验未完成。",
    "文中战况、伤亡数字、装备损失、乌军吸毒与虐杀等事实断言均需外部核查；作者仅以一条外链与中文报道标题作旁证，未展开来源。",
    "布查事件真相、欧盟调查团结论、乌军战报真伪等属作者预判，本文未提供可核事实。",
    "P195 “百年未有之变局”所指文章未给出URL或上下文，需核查该链接目标。",
    "同一人在文中作“泽连斯基”（P090）与“泽林斯基”（P169）两种写法，原文如此，未统一。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我完全同意这答案里引用的对俄军营战斗群的特点分析", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "我绝不同意这篇东西里对这些“问题”的定性", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "这是一种极其傲慢的定性", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "因为世界上根本不存在“六边形部队”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "经过深思熟虑的权衡取舍，绝非什么“低级错误”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "仅仅凭着“到中国演习表现不好”来断言“俄军犯错”，是一种基本逻辑错误", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "因为俄军从未以解放军或美军为假想敌", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "对俄罗斯是一个单纯的核武力问题", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "几乎全部是伪问题，不但不是缺陷，反而恰恰正是俄军的用意所在", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "我乐观估计乌克兰之战俄军赢面很大的主要依据之一", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "营战术群在高威胁环境下需要外围部队翼护", "relation": "context"},
    {"key": "E12", "paragraph_id": "P020", "quote": "俄军正好都有“有相当能力的当地亲俄民兵”可以补这个位", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "营战斗群一直在黑海舰队巡航导弹射程范围内作战，从未越雷池一步", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "哪支俄军被分配了“持续突击任务”？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P028", "quote": "俄军这次的人员伤亡高度接近俄军自己的通报，的确甚为轻微", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P029", "quote": "俄军根本没有计划任何攻坚任务，而是一直集中兵力保持高速机动，直扑要地", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P031", "quote": "俄军在突击阶段根本就不会遭遇乌军的严肃阻击", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P037", "quote": "根本没有合理的战术逻辑去发生什么重大伤亡", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P041", "quote": "这开场的几轮导弹攻击令多少乌军单位的指挥、情报、通讯机构陷入了混乱", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P047", "quote": "说乌军对俄军造成了什么重大杀伤，那实在是天降神兵的军事奇迹", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P049", "quote": "乌军甚至没能使哪几根直线弯上一弯", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P050", "quote": "恐怕就是乌军在那一阶段所获得的全部“战果”了", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P054", "quote": "才更进一步印证了俄军在第一周行动的高度成功", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P055", "quote": "营战术群炮兵火力配比过强，不利巷战，只利围困和火力支援", "relation": "context"},
    {"key": "E25", "paragraph_id": "P056", "quote": "他们的确只做了“围困和火力支援”，确实没有搞什么“完全不适用”的巷战", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P058", "quote": "这种部署纯属结硬寨打呆仗", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P063", "quote": "超低飞行突击的攻击机其实是很难用肩扛导弹锁定的", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P065", "quote": "因为肩扛导弹的天生缺陷，这胜率严重的偏向俄空军", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P067", "quote": "乌军的击落总数一定高度接近。并没有多少“未被记录的击落”", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P070", "quote": "但这些战术几乎没有可持续性", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P075", "quote": "甚至直接拿T64装作T72来拍", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P079", "quote": "已经高度接近乌军的全部战果", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P080", "quote": "这一数字，极大的接近俄军自己的通报", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P081", "quote": "依靠一贯的“有报必信”来撑过信息战的早期阶段", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P084", "quote": "乌军的认知战会彻底破产", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P090", "quote": "乌军已经进入了“抱头挨打，无隙可乘”的极端被动状态", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P096", "quote": "不靠强效镇静剂和兴奋剂，乌军士兵根本无法正常作息", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P097", "quote": "必须靠成建制的、大面积的吸毒来维持基本的战斗力", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P103", "quote": "其他的前线乌军部队在精神上已经到了崩溃边缘", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P104", "quote": "他们可能在极轻微的袭扰下溃散", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P109", "quote": "会导致他们对平民成规模的施暴冲动", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P118", "quote": "乌克兰平民是不是宁可追随俄军撤走，只留下无人区给乌军接收", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P119", "quote": "这一现象的有无，胜过所谓的“欧盟调查团”一万倍", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P124", "quote": "是“高清大屏”无法传输的信息", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P127", "quote": "必须让一个少将以上的师级、集团军级军官在听得见炮声、看得见敌阵的地方临机决断", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P132", "quote": "这不是bug，这是feature。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P133", "quote": "是红军的军魂。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P134", "quote": "这种单位首先是为了能依靠铁路运力实现成建制的战略机动", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P137", "quote": "营级战斗群却可以以一个“最小可用单位”的形式立刻投入作战", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P138", "quote": "成为一颗拔不动的钉子", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P140", "quote": "否则世界上没有任何常规陆军能在海军、空天军、火箭军的支援火力倾泻下来之前拔得掉你", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P142", "quote": "从未打算过用于空天军、火箭军、海军覆盖不到而没有空优的任何战场", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P152", "quote": "以低至极点的燃料、弹药、人员消耗和极大的战略机动性", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P153", "quote": "它举起核盾牌绝对拒止在外", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P154", "quote": "你将永远也没有机会再幻想加入了", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P158", "quote": "它拿乌克兰开刀，就是因为这是前苏联国家里最难打的头羊", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P159", "quote": "将会根绝亚美尼亚、阿塞拜疆、格鲁吉亚", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P164", "quote": "北约在这次战略突袭之下，恐怕已经开始了自己的结束", "relation": "supports"},
    {"key": "E59", "paragraph_id": "P171", "quote": "我们是完全可以接受所谓俄罗斯战败的", "relation": "supports"},
    {"key": "E60", "paragraph_id": "P172", "quote": "中国之强，已经强到了无视规则的地步", "relation": "supports"},
    {"key": "E61", "paragraph_id": "P185", "quote": "砍断把自己绑在这幻想的幽灵船上的缆绳", "relation": "supports"},
    {"key": "E62", "paragraph_id": "P170", "quote": "这不是你们该掺合的游戏", "relation": "supports"},
    {"key": "E63", "paragraph_id": "P182", "quote": "恐怕就是你们。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["军事与国防", "俄乌战争", "国际关系与地缘政治", "作战编制与战术理论", "舆论战/认知战"],
   "issue_candidates": ["俄军营级战术群（BTG）编制优劣", "俄军2022年乌克兰攻势第一阶段评估", "俄军指挥体制与前线临机决断", "俄乌战报与视频战果可信度", "布查事件", "北约与欧洲安全格局", "中亚与台海的连带效应"],
   "text_function_candidates": ["答疑（知乎答问）", "论辩/反驳", "战况评论", "预测", "训诫/劝告"],
   "object_candidates": ["俄罗斯", "乌克兰", "俄军营战术群", "乌军", "北约", "美国", "中国", "黑海舰队", "顿巴斯民兵", "车臣兵", "泽连斯基（文中亦作泽林斯基）", "台湾网军", "中亚国家", "欧盟", "苏联军事遗产"],
   "working_keywords": ["营战术群", "营战斗群", "战术营", "六边形部队", "伪问题", "拔不动的钉子", "结硬寨打呆仗", "最小可用单位", "有报必信", "认知战", "拉胯战术", "核盾牌", "绿区", "布查", "头羊"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "图片文章：正文含 1 个图片节点 IMG001（位于第99段 taskandpurpose.com 外链之后），图片内容未经核验，故 status=needs_reread、image_checked=false；已读部分为正文文本（195 段、9014 字符）。正文与 lexical 结构存在未覆盖片段（P003、P099、P101、P195 标为“lexical未覆盖片段”），且 lexical 含 text 之外的图片节点，结构核验未完成，已登记于 unresolved_questions。被作者引用并反驳的那篇分析未在本文给出链接或出处，其观点仅按本文引号记为 opponent_view，未归给作者；提问字段 Q001 与正文 P003 重复，属正文转述提问，同样不计入作者立场。文中大量事实性战况与外部报道标题需外部核查。"
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
