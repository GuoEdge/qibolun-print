# -*- coding: utf-8 -*-
"""批次 r001-b0048 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0048.sessions.py            # 写 out/r001-b0048.out.jsonl
  python3 records/r001-b0048.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0048"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0048.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "b95e3891": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "回答知乎提问“纳粹为什么那么仇恨犹太人？”（Q001，属提问者）。作者称该问题在中国被最广泛误解、几无靠谱答案，因对中国有特殊时代意义而作答（P001），并把论域从“纳粹为何仇恨”改写为欧洲长期排犹的思想根源（P099-P100），再转入对中国的现实意义（P140-P141）。提问者的“纳粹仇恨”框架不等于作者立场：作者认为纳粹顺承路德起头的反犹主义纲领，并因反犹是德国的一大“国际卖点”而更反犹（P137-P138）。P204“中国芯片产业前景到底怎么样？”与篇尾 P268“怎样看待美国仇华情绪？”是平台卡片／链接标题，作者仅作引例与关联条目，其正文不在本篇。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"],
     "summary": "开篇：问题被广泛误解、因对中国有时代意义而作答；要害在对待“约”的态度。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"],
     "summary": "引《出埃及记》十诫为“约”的条款；对价是完美守约则救世主降临、仇敌尽灭（含两次完美安息日之说）。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028"],
     "summary": "以安息日为切口提大量边界问题并强调石刑之严；犹太经学努力与《米士拿》39类禁工使解读细密化，推出“谁守得住”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034"],
     "summary": "犹太教以“最佳实践”、补赎仪轨与忏悔之诚应对；结果是傲视四邻为“法盲加蛮夷”。", "role": "context"},
    {"unit_id": "U005", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048"],
     "summary": "基督教三层反对（放水打折、献祭洗罪不可靠、无罪常态）及正面主张（约非人力可守、从轻解释即自封为神、唯靠恩典）。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067"],
     "summary": "律法主义三重后果：消解契约道德（改考题）、系统性不公（富人免疫、穷人卑贱）、奖励钻法者而惩罚积极守约者。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079"],
     "summary": "引《马太福音》12、15章；展开基督教律法观：以爱替代律法主义、律法为“必要之恶”、立法谦抑而守法敬畏。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095"],
     "summary": "普通法由真实案情与先例驱动而反成典范；对照预先立法的缺陷（大幅修正、变法、秦律改汉律）；自注大陆法系并非无好处。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P096", "P097", "P098"],
     "summary": "旁论：中国近乎宗教式的立法狂热是对律法主义系统风险的无知，属最根本的危险之一。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P099", "P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114", "P115", "P116", "P117", "P118", "P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127"],
     "summary": "排犹根源：两教律法观三重对立；无“不歧视”解法（针对性限制即歧视）；合作成本与公共产品论证；落到“合法致富／合法致贫”的灵魂撕扯。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P128", "P129", "P130", "P131", "P132", "P133", "P134", "P135", "P136", "P137", "P138", "P139"],
     "summary": "原理总结：价值观→禁忌→竞争归因→文明冲突全员动员；德国个案（路德的反犹倾向、纳粹的国际“奖励”）。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P140", "P141", "P142", "P143", "P144", "P145", "P146", "P147", "P148", "P149", "P150", "P151", "P152", "P153", "P154", "P155", "P156", "P157", "P158", "P159", "P160", "P161", "P162", "P163", "P164", "P165", "P166", "P167", "P168"],
     "summary": "现实意义：中国人被塑造成“新犹太人”且该形象在西方中下层卖得好；争公平与展示事实皆无效；犹太人“正面事实”努力失败的先例。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P169", "P170", "P171", "P172", "P173", "P174", "P175", "P176", "P177", "P178", "P179", "P180", "P181", "P182", "P183", "P184", "P185", "P186", "P187", "P188", "P189", "P190", "P191", "P192", "P193", "P194", "P195", "P196", "P197", "P198", "P199", "P200", "P201"],
     "summary": "有实力也不够、以避战为追求；和平努力即比武器更有效的进攻（引《孙子》谋攻）；反驳“入关”论为放弃人心战场的失败主义。", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P202", "P203", "P204", "P205", "P206", "P207", "P208", "P209", "P210", "P211", "P212", "P213", "P214", "P215", "P216", "P217", "P218", "P219", "P220", "P221", "P222", "P223", "P224", "P225", "P226", "P227", "P228", "P229"],
     "summary": "行动方案：三条件选材＋兼利自己的无差别公共产品；中国人口份额使其最有利；机制在基督教禁忌与“仇华即反基督”。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P230", "P231", "P232", "P233", "P234", "P235", "P236", "P237", "P238", "P239", "P240", "P241", "P242", "P243", "P244", "P245", "P246", "P247", "P248", "P249", "P250", "P251", "P252", "P253", "P254", "P255", "P256", "P257", "P258", "P259", "P260", "P261", "P262", "P263", "P264", "P265", "P266", "P267", "P268"],
     "summary": "结论：无需皈依，好撒马利亚人原则带来不可攻击性；与中国古今理想及前新教基督教相合；美国自弃理想；收尾“老子出关”（附未核验图片）。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "该问题在中国被最广泛误解、几乎没有靠谱答案。", "evidence": ["E01"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "反犹问题的根本要害在对待“约”的态度的不同。", "evidence": ["E02"]},
    {"claim_id": "C003", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "作者转述犹太人相信完美守约则上帝派遣救世主扫平全部仇敌。", "evidence": ["E03"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "安息日律必然引出时间、人员、寄居者、牲畜、何谓“工”等真实边界问题。", "evidence": ["E05"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "对律法的重视必然导致细密解读，逻辑后果是“谁守得住”。", "evidence": ["E08"]},
    {"claim_id": "C006", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "作者转述犹太教以“最佳实践”与补赎仪轨应对律法的不可守。", "evidence": ["E09"]},
    {"claim_id": "C007", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "作者转述基督教三层反对：放水打折、献祭洗罪不可靠、否定“无罪常态”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "作者转述基督教：约本来就是凡人无法完美遵守的。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "作者转述：得救唯一可能是靠上帝把不及格算成及格。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：律法主义消解了神人契约的道德力量。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：律法系统性不公——富人靠罚款、雇穷人代为犯罪而免疫。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：律法利于钻法者，惩罚积极守约者、奖励消极守约者。", "evidence": ["E21"]},
    {"claim_id": "C013", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "作者转述基督教：人类律法本身是“必要之恶”。", "evidence": ["E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者概括基督教法律态度：立法极端谦抑、守法高度敬畏。", "evidence": ["E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：以真实案情驱动的普通法，反而成了现代主流法律实践典范。", "evidence": ["E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "预先立法的体系一旦思想进展即须大幅修正，终需彻底重来。", "evidence": ["E26"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified",
     "statement": "作者自注：并非说大陆法系没有好处。", "evidence": ["E28"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：立法狂热基因属犹太／罗马文化，而非基督文化。", "evidence": ["E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者旁论：中国近乎宗教式的立法狂热是最根本的危险之一。", "evidence": ["E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：两教律法观的对立基于最核心的价值观。", "evidence": ["E34"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：无“不歧视”解法，拉平优势只能靠专门针对犹太人的限制。", "evidence": ["E36"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：一个犹太人即把整个社区拉平到犹太人的逻辑上。", "evidence": ["E39"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：犹太人合法富裕、基督徒合法贫穷。", "evidence": ["E40"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者原理总结：价值观→行为禁忌→竞争归因→文明冲突全员动员。", "evidence": ["E42", "E43", "E44"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：德国反犹尤烈，路德本人即有强烈反犹倾向。", "evidence": ["E45"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：纳粹更反犹，因反犹是德国的一大“国际卖点”。", "evidence": ["E46"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：有人试图把中国人塑造成“新的犹太人”。", "evidence": ["E47"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者主张：谈公平无意义；列举积极事实对冲消极事实行不通。", "evidence": ["E51"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者举证：犹太人捐献、宣传、服役仍失败（含纳粹德军中的十五万犹太裔士兵）。", "evidence": ["E54"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：中国实力自保有余而“进取”绝对不足。", "evidence": ["E55"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者反驳：喊入关即放弃第一战场——人心的战场。", "evidence": ["E58"]},
    {"claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者行动原则：选与基督教理想、中国国家理想、现实利益一致的目标。", "evidence": ["E60"]},
    {"claim_id": "C033", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：中国人口占五分之一，普惠产品必然最有利于中国。", "evidence": ["E62"]},
    {"claim_id": "C034", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：只有基督教自己的禁忌能最有效抑制其自己的问题。", "evidence": ["E63"]},
    {"claim_id": "C035", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者主张：中国不需要皈依基督教。", "evidence": ["E66"]},
    {"claim_id": "C036", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者主张：伦理逻辑一致的异族因好撒马利亚人原则获得不可攻击性。", "evidence": ["E67"]},
    {"claim_id": "C037", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者主张：中国应选择可承受的“好撒马利亚人”策略并行动。", "evidence": ["E68"]},
    {"claim_id": "C038", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：共产主义理想与基督教人间天国理想几乎完全一致。", "evidence": ["E70"]},
    {"claim_id": "C039", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者判断：美国之病在自弃理想与原则，正堕落为异端。", "evidence": ["E72"]},
    {"claim_id": "C040", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "作者反驳入关论：中国要过的关是“老子出关”而非蛮夷入关。", "evidence": ["E74"]}
   ],
   "argument_steps": [
    "声明问题被广泛误解、对中国有时代意义，设定论域为「对待约的态度」（P001-P003）。",
    "引《出埃及记》十诫为「约」的条款，概括对价：完美守约→救世主降临（P005-P008）。",
    "取安息日连提时间／人员／寄居者／牲畜／何谓「工」的边界问题（P011-P018）。",
    "强调石刑之严与经学教育之努力，举《米士拿》39类禁工（P020-P024）。",
    "推出「这谁守得住」的逻辑后果（P026）。",
    "述犹太教最佳实践、补赎仪轨与忏悔之诚，落到视四邻为法盲蛮夷（P029-P034）。",
    "转述基督教三层反对（P037-P040）与正面主张：约非人力可守、从轻解释即自封为神、唯靠恩典（P042-P046）。",
    "列律法主义后果：消解契约道德、系统性不公、奖励钻法者（P049-P066）。",
    "引《马太福音》12、15章为基督教对律法主义的经典断语（P068-P071）。",
    "展开基督教律法观：以爱替代律法主义、律法为必要之恶、立法谦抑守法敬畏（P072-P079）。",
    "以普通法与预先立法对照，举秦律→汉律说明后者缺陷（P080-P092）。",
    "自注大陆法系并非无好处，下结论「法制健全」是消极立法倾向的结果（P093-P095）。",
    "旁论中国立法狂热之危险，转入排犹根源（P096-P100）。",
    "三重对立→无「不歧视」解法→针对性限制即迫害，以合作成本与企业类比补强（P101-P122）。",
    "落到合法致富／合法致贫与灵魂撕扯，提示《威尼斯商人》（P123-P127）。",
    "归纳价值观→禁忌→文明冲突原理，再述德国与纳粹的国际「奖励」机制（P128-P139）。",
    "转入现实意义：中国人被塑造成「新犹太人」；争公平无意义、展示事实无效（P141-P157）。",
    "以犹太人「正面事实」努力失败为鉴（哈伯、Weiss Strasse、十五万士兵）（P158-P168）。",
    "论实力不足以解决，主张避战并把和平努力当进攻，引《孙子》谋攻（P169-P192）。",
    "反驳「入关」论为放弃人心战场的失败主义，以明清易代讽喻（P193-P201）。",
    "提出行动方案：选材三条件＋普惠公共产品，中国人口份额使其最有利（P202-P216）。",
    "论证机制：基督教禁忌不可逾越（旷野试探），仇华与反基督相连即政治自杀（P217-P229）。",
    "以好撒马利亚人原则说明无需皈依即可获得不可攻击性，主张中国采纳（P230-P245）。",
    "接续中国古今理想与前新教基督教的反资本主义传统，指出美国自弃理想而堕落（P246-P260）。",
    "收尾：不用共产主义或民族主义语言劝告邻居；入关论不成立，中国是「老子出关」（P260-P266）。"
   ],
   "concept_usage": [
    {"term": "约（the Covenant）", "meaning": "上帝与以色列的契约，守约与否决定救恩。", "evidence": "P003", "ambiguity": "作者只取「对待约的态度」为要害，未展开圣约神学。"},
    {"term": "最佳实践", "meaning": "犹太教为让中产阶级可照办而对律法作的中庸化解释。", "evidence": "P029", "ambiguity": "带引号的贬义用法，系作者转述基督教评价。"},
    {"term": "补赎仪轨", "meaning": "按违规种类献祭以清洗罪行的制度。", "evidence": "P031", "ambiguity": "以口语列举，未给完整清单。"},
    {"term": "无罪常态／无罪自觉", "meaning": "靠最佳实践与及时献祭维持的常态无罪状态及由此的「有权得救」。", "evidence": "P040", "ambiguity": "作者标明这是基督教所否定的对象。"},
    {"term": "律法主义", "meaning": "以细密法条与解释技术取代圣约道德要求的实践倾向。", "evidence": "P050", "ambiguity": "全文无单一形式定义，兼指犹太教实践与一般立法狂热。"},
    {"term": "必要之恶", "meaning": "基督教对人类律法的定位：爱的能力不成熟时的痛苦妥协。", "evidence": "P078", "ambiguity": "作者引为基督教立场，未讨论教内差异。"},
    {"term": "入关", "meaning": "知乎上主张中国效法女真入关、以蛮力破局的话语，本文的反驳对象。", "evidence": "P193", "ambiguity": "未给出该论说的具体文本来源，只针对口号。"},
    {"term": "好撒马利亚人原则", "meaning": "与基督教伦理实践一致的异族也可获得不可攻击性的教义依据。", "evidence": "P242", "ambiguity": "作者将其从个人伦理推广到国家策略，属其推论。"},
    {"term": "天道", "meaning": "作者用语，指与「做最大的和平努力」相配的正当天理立场。", "evidence": "P179", "ambiguity": "本篇未定义，确切所指需结合作者其他文章。"}
   ],
   "examples_and_targets": [
    "《出埃及记》20章2-17节（P005）：经文证据，作为「约」的条款。",
    "安息日捡柴要处石刑（P020）：举证律法之严。",
    "《米士拿》39类禁工、安息日的路程等细则（P024）：引文，作者标注来源为 blog.udn.com 的《他勒目》宋西诺版转述。",
    "波斯人、希腊人、罗马人被犹太人视为法盲蛮夷（P034）：转述的犹太视角，非作者对他者的评价。",
    "《马太福音》12:1-8、15:1-9（P068、P071）：经文引用，基督教对律法主义的经典断语。",
    "《马太福音》4:1-11 旷野受试探（P223）：经文引用，说明禁忌不可逾越。",
    "《路加福音》10:25-37 好撒马利亚人（P234）：经文引用，本文策略主张的教义依据。",
    "《马太福音》19:20-24、《路加福音》12:33（P255）：经文引用，前新教基督教反对无限积累财富。",
    "《孙子·谋攻》（P192）：引用，支撑「不战而屈人之兵」。",
    "秦律被「彻底推翻」改为汉律（P090）：作者举的变法例，带调侃（P091）。",
    "《威尼斯商人》（P126）：作者建议的阅读参照。",
    "马丁·路德（P137）：作者点名的反犹倾向者，德语圣经编定者。",
    "弗里茨·哈伯制造毒气弹、其妻自杀（P161）；沃尔特·拉特瑙主张效忠而遇刺（P162）；Bernard Weiss Strasse 获一级铁十字、任柏林刑警总局长仍被迫逃亡（P163）：犹太人效忠仍遭弃的例子，人名与史实待核。",
    "纳粹德军中的十五万犹太裔士兵（P166）：数据，来源未注明。",
    "川普、班农、纳瓦罗、希特勒、戈培尔（P217）：作者并列的煽动者名单。",
    "「入关」论者、大清、宁锦防线、女真／大明（P193-P201、P261-P264）：反驳对象与讽喻材料。",
    "范曾作《老子出关》图（IMG001，图注 P267）：配图，内容未经核验。",
    "P204「中国芯片产业前景到底怎么样？」与篇尾 P268「怎样看待美国仇华情绪？」：平台卡片／链接标题，分别为策略引例与关联条目，正文不在本篇。"
   ],
   "conditions": [
    "作答动机限定：因为这个问题对中国有特殊的时代意义（P001）。",
    "作者自限论域为「对待约的态度」，声明不在救恩论上多做论述（P003、P047）。",
    "视角限定：多处作「在基督教看来」「站在中世纪基督徒的立场上」（P067、P116）。",
    "明确让步：「我不是说大陆法系没有好处」（P093）。",
    "实力前提：谈和平努力的进攻性以「拥有一支足够强大的武力」为前提（P191）。",
    "实力判断：自保有余、「进取」绝对不足（P171）。",
    "避战强度：即便能不损一人杀光对手，也一样要尽一切可能避免战争（P176）。",
    "纳粹更反犹的条件：反犹被国际社会当作「奖励」的机制（P138）。",
    "策略成立条件：目标须同时满足三条件（与基督教理想一致、与中国国家理想一致、与现实利益一致）（P208-P210）。",
    "效果依赖对象：须落在基督徒与「文化基督徒」在意的禁忌上（P228）。",
    "语言条件：提醒邻居不能用共产主义或民族主义的语言（P260）。",
    "未明说的边界：除芯片一例外，未给出「和平努力」与「公共产品」的具体清单（P202-P206）。"
   ],
   "rhetoric_and_tone": "论辩与训诫混合体：以圣经纪文为权威材料，密集使用反问（「这谁守得住？」「然则大清如今安在？」）、夸张与讽喻（「改考题」「法盲加蛮夷」「宁锦防线」「你们才是大明」），间以口语调侃（「禁撸八百天起吧」「哇嘎泥共，这次铁定行！ ；O」）和强调性重复（「我再说一遍」）。对读者常以「你们」直呼并下禁令，断言与训诫语调强；叙述教义时用转述＋断语并加视角限定；末段以「老子出关」收束并配图。",
   "unresolved_questions": [
    "IMG001 未核验：据图注 P267「（范曾 作，侵删）」及上下文，图为《老子出关》题材，画面内容需人工或多模态复核。",
    "P204「中国芯片产业前景到底怎么样？」与篇尾 P268「怎样看待美国仇华情绪？」是平台卡片／链接标题（lexical 未覆盖片段），被引正文不在此篇，需回平台核对。",
    "P024 引文标注来源为 blog.udn.com（《他勒目》宋西诺版转述），版本、译文与页码准确性待外部核查。",
    "圣经引文（P005、P068、P071、P223、P234、P255）用和合本，作者未逐处标注版本与出处细节，个别章节需核对。",
    "P163 人名「Bernard Weiss Strasse」拼写、职务与一级铁十字等史实待外部核查。",
    "P166「纳粹德军中有十五万犹太裔士兵」的数据来源未给出，待外部核查。",
    "P049「已经实践了一千四百年——按最保守的估计，也有近六百年」的时间口径未说明依据。",
    "「好撒马利亚人」策略的具体载体（什么算「兼利自己的无差别人类公共产品」）只给出芯片一例，P204 卡片正文不在本篇。",
    "「天道」「老子出关」等收尾用语本篇未定义，确切所指需结合作者其他文章。",
    "updated_at（2021-05-15）晚于 published_at（2020-05-07），是否存在修订或增补未标注，provenance／superseded 均为 null。",
    "作者对犹太教／基督教教义的概括未给出教内流派差异，其代表性待专业复核。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "这个问题在中国是一个被最广泛误解的问题", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P003", "quote": "对待“约”（the Covenant）的态度的不同", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P006", "quote": "只要照着这个约执行，而且执行完美，上帝就会伸手派遣救世主", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P022", "quote": "上面提的这几个问题每一个都是真实的问题", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P026", "quote": "而这样的解读必然带来一个逻辑的后果——这谁守得住？", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P029", "quote": "中产阶级基本可以照办的“最佳实践”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P038", "quote": "基督教认为这是因为自己做不到，就自己放水打折", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P040", "quote": "给自己构建了一个“无罪的常态”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P042", "quote": "上帝的约本来就是凡人无法完美遵守的", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P045", "quote": "唯一的可能性就是靠上帝把人类本不及格的行为算成及格", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P050", "quote": "律法主义已经实际上消解了神人契约的道德力量", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P055", "quote": "富人或者依靠轻松的支付罚款，或者依靠雇佣穷人代为犯罪", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P065", "quote": "它事实上惩罚了积极守约者、极大的奖励了消极守约者", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P078", "quote": "人类的律法本身就是一种“必要之恶”", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P079", "quote": "在立法上极端谦抑，如无绝对必要绝不立法", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P085", "quote": "反而成了现代一大主流的法律实践典范", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P087", "quote": "一旦人类在思想上有所进展，则整个体系都要面临大幅的修正", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P093", "quote": "我不是说大陆法系没有好处", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P095", "quote": "真正有立法狂热基因的是犹太/罗马文化，而不是基督文化", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P096", "quote": "中国现在就有近乎宗教式的强烈的立法狂热", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P101", "quote": "是基于最核心的核心价值观", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P113", "quote": "想要拉平这种优势，势必要引入专门针对犹太人的额外限制", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P117", "quote": "被一步步拉平到犹太人的逻辑上", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P123", "quote": "犹太人会合法的富裕起来，而基督徒会合法的贫穷下去", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P130", "quote": "价值观必定会造成“有所为、有所不为”的行为禁忌", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P131", "quote": "是不是因为对方占了可以为所欲为的便宜", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P132", "quote": "而是文明的脊椎、心脏和大脑", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P137", "quote": "自己就有强烈的反犹倾向", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P138", "quote": "反犹是希特勒德国的一大“国际卖点”", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P141", "quote": "尝试把中国人塑造成“新的犹太人”", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P157", "quote": "依靠列举积极事实来对冲对方列举的消极事实", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P166", "quote": "甚至就在纳粹德军之中，就有十五万犹太裔士兵", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P171", "quote": "我们的实力只是自保有余，“进取”绝对不足", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P193", "quote": "“喊入关”本身就是放弃至关重要的第一战场——人心的战场", "relation": "supports"},
    {"key": "E60", "paragraph_id": "P208", "quote": "该目标与基督教文化自身的理想要有无法反驳的协调一致性", "relation": "supports"},
    {"key": "E62", "paragraph_id": "P214", "quote": "一切普惠全人类的公共产品都必然现实的符合中国人的利益", "relation": "supports"},
    {"key": "E63", "paragraph_id": "P221", "quote": "只有基督教文化自己的禁忌和规则", "relation": "supports"},
    {"key": "E66", "paragraph_id": "P232", "quote": "——不需要。", "relation": "supports"},
    {"key": "E67", "paragraph_id": "P242", "quote": "就将因为好撒马利亚人原则获得不可攻击性", "relation": "supports"},
    {"key": "E68", "paragraph_id": "P245", "quote": "中国要明智的选择自己可以承受的“好撒马利亚人”策略", "relation": "supports"},
    {"key": "E70", "paragraph_id": "P253", "quote": "共产主义理想与基督教的人间天国理想", "relation": "supports"},
    {"key": "E72", "paragraph_id": "P259", "quote": "而来自于它自身对自身理想和原则的离弃", "relation": "supports"},
    {"key": "E74", "paragraph_id": "P266", "quote": "而是老子出关。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教与神学（犹太教／基督教律法观）", "法律思想史", "欧洲反犹史与纳粹德国", "国际政治与中美关系", "中国立法问题"],
   "issue_candidates": ["反犹主义的宗教—律法根源", "律法主义的社会后果", "排犹与歧视性立法的悖论", "把中国塑造成「新犹太人」的舆论策略", "中国对外公共产品战略", "对「入关」论的批评"],
   "text_function_candidates": ["答疑", "论辩", "批评", "历史解释", "策略建议", "训诫"],
   "object_candidates": ["犹太人／犹太教", "基督徒／基督教（天主教、东正教、新教、路德宗）", "纳粹德国／希特勒／戈培尔", "马丁·路德", "美国", "中国", "知乎「入关」论者"],
   "working_keywords": ["约（the Covenant）", "安息日", "最佳实践", "补赎仪轨", "无罪常态", "必要之恶", "普通法／判例法", "立法狂热", "文明冲突", "好撒马利亚人", "文化基督徒", "入关", "老子出关"]
  },
  "notes": "含 1 个图片节点 IMG001（结构位置在 P266“而是老子出关。”与图注 P267“（范曾 作，侵删）”之间），图片内容未经核验，故 status=needs_reread；正文 268 段已读完。另有两处 lexical 未覆盖片段：P204“中国芯片产业前景到底怎么样？”与篇尾“怎样看待美国仇华情绪？”，为平台卡片／链接标题，非本篇正文。8 个 quote 段（P005、P024、P068、P071、P192、P223、P234、P255）为经文／古籍引文，归属已在分析中区分。provenance／superseded 均为 null；updated_at 晚于 published_at，是否修订未标注。"
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
