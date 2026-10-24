# -*- coding: utf-8 -*-
"""批次 r001-b0061 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0061.sessions.py            # 写 out/r001-b0061.out.jsonl
  python3 records/r001-b0061.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0061"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0061.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "4ff7810c": {
  "analysis": {
   "question_context": "提问者（知乎问题）问“你心目中完美的养老院是什么样的？”，作者的正文是对这一设问的直接回答与理念申说，并顺带回应“太理想、不适合大多数人”的质疑（P032）。提问者的问法本身预设养老院是一种“设施/机构”，作者的答复则重新规定其性质，提问者立场不等于作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "描述流行的养老院想象：消费毕生积蓄换取不必劳动而“纯享福”，问题被化约为娱乐项目与护理手段的利润平衡。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "断言凡按上述想象办养老院者必然失败。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004", "P005"], "summary": "提出养老院本质上是关于生存和死亡的学术机构、修院，提供的是平安的、向死而生的死法而非舒适的活法。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "连续界定：解脱尘世执着恩怨的修行所、探索与传授超越个人得失生死之知识与技艺的研究所/实践场/教学中心、聚集老年中年幼年三代的生死大学。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "主张它应成为制度性、周期性、与社会紧密互动的学术与慈善机构，并把访问交流列为学校、医疗教育、企事业、监管教化机构的常规制度安排。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "理由：临终之人的价值被死亡恐惧引发的讳疾忌医浪费，社会因此失去无法用金钱弥补的生死观早期教育。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013"], "summary": "它最常进行的活动应是生命哲学与伦理学的研究、讨论和传承，以及帮助原谅、修和、宽容、放下和送别的实践。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015", "P016"], "summary": "其生活体验应忙碌、奋进、矢志不渝、视死如归，帮助人超脱私己成为无我之我，并为人类做最后的努力。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "人生最大遗憾是因恐惧死亡匮乏而未专心爱过；临终反而是最纯粹的机会，但缺乏学习实践常使机会落空，这个短板正是养老院必须补足的灵魂。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "反面论证：否则高档安乐窝实为地狱，身边高频死亡使人不得平安，并以游戏机龙虾ICU之设问和候刑室类比否定纯享乐方案。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P029"], "summary": "行动建议：在机构明白并实践该理念之前，其股票不值得投资。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P030"], "summary": "格言式判断：最好的死法是鞠躬尽瘁、死而后已。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P031"], "summary": "正文中混入的独立问句“如何树立正确的财富观？”，与上下文无衔接、lexical 未覆盖，疑为平台插入片段，未纳入作者论证。", "role": "other"},
    {"unit_id": "U014", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "回应“太理想、不适合多数人”的质疑：不适合而羡慕者可外围围观或短期交流；加入者须经多轮谈论、实践、试炼、资格与发愿，任何一环都可自由改变主意。", "role": "qualification"},
    {"unit_id": "U015", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044"], "summary": "收束：走到最后者注定不多且非拿钱可进，须提前十几二十年寻同路人找可做之事；所做的事须与世无争、非政治影响力、非世俗商品、图利者得不偿失、没有尽头，故能代代传承。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把养老院当成消费毕生积蓄换取“纯享福”的生活与护理设施、只盘算娱乐与护理的成本利润者，必然失败。", "evidence": ["E023", "E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养老院首先应是一所关于生存和死亡的学术机构，本质上首先是一种修院；它提供的不是舒适的活法，而是平安的、向死而生的死法。", "evidence": ["E002", "E024", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养老院应是解脱尘世执着恩怨的修行所，是探索与传授超越个人得失、成败、荣辱、生死的知识与技艺的研究所、实践场和教学中心，是聚集老年人、中年讨论者和幼年学习者的生死大学。", "evidence": ["E025", "E026", "E027"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养老院应成为制度性、周期性、与社会紧密深刻互动的学术与慈善机构；访问并与其展开制度化周期性交流应成为义务教育学校、医疗教育机构、企事业机构、监管教化机构的常规制度性安排。", "evidence": ["E004", "E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "临终之人的价值被非理性的死亡恐惧引发的病态讳疾忌医完全浪费，社会也损失了极珍贵的生死观早期教育，而这种教育不是加大金钱投资或任何其他形式可以弥补和替代的。", "evidence": ["E006", "E028"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养老院最常进行的活动应是关于人的生命的哲学、伦理学的研究、讨论和传承，以及帮助原谅、修和、宽容、放下和送别的实践。", "evidence": ["E007", "E029"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养老院的生活体验不应散漫闲适，而应忙碌、奋进、矢志不渝，充满视死如归的激情，帮助人超脱私己成为无我之我。", "evidence": ["E030", "E031"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人生最大的遗憾不是活得不幸福，而是因为恐惧死亡和匮乏，没有真正毫无顾忌、专心专意地爱过。", "evidence": ["E008"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "临终虽是最纯最美的机会，但人一生疏于学习练习、缺少实践经验，机会常常不能转化为有效效果、难以带来平安喜乐；补足这个短板是养老院最值得也必须补足之处，是其灵魂。", "evidence": ["E009", "E010", "E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只搞好吃好喝的养老院根本行不通：燃烧毕生积蓄的安乐窝、逍遥乡反而是最令人心惊胆战的地狱。", "evidence": ["E032", "E012"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在看到养老机构明白并实实在在地实践这一理念之前，他们的股票不值得投资。", "evidence": ["E013"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最好的死法是鞠躬尽瘁、死而后已。", "evidence": ["E033"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "有人质疑这样的机构太理想、对大多数人并不适合（作者转述并作答的反对意见，非作者主张）。", "evidence": ["E014"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对不适合而羡慕的人，可以外围围观或做短期交流；要加入者须经一轮轮谈论、实践、试炼、获得资格、发愿，且任何一环都可完全自由、毫无后果地改变主意。", "evidence": ["E015", "E016", "E017"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "走到最后一层的注定不会是很多人，因为这件事并非任何人都办得到；它不是花钱申请就能进，而要从十几二十几年前就开始寻找同路的人、找到可做的事。", "evidence": ["E018", "E019", "E034"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这件事必须与世无争、不可转化为政治影响力、不能转化为与世俗竞争的商品，须是图利之人觉得得不偿失而所有人苦于没人肯去做的事，并且没有尽头，所以才能代代传承。", "evidence": ["E020", "E035", "E021", "E022", "E036"]}
   ],
   "argument_steps": [
    "先立被否定的流行想象：养老院＝舒适生活设施＋护理机构，用积蓄换“纯享福”，只求娱乐与护理的成本利润平衡（P001）。",
    "以“凡是这样想的人，必然要失败”直接否定该路线（P002）。",
    "正面重新定义：关于生存和死亡的学术机构、修院，提供向死而生的死法（P003–P005）。",
    "用一组“它应该是……”递进界定修行所、研究所/实践场/教学中心、三代共学的生死大学（P006–P008）。",
    "推进到制度层面：制度性周期性机构，并把访问交流设为各类机构的常规安排（P009–P010）。",
    "给出理由：临终者价值被死亡恐惧浪费，社会损失不可用金钱弥补的生死观教育（P011–P012）。",
    "说明其日常活动（生命哲学伦理学的研习传承、帮助原谅修和宽容放下送别）与应有生活体验（忙碌奋进、视死如归、无我之我）（P013–P016）。",
    "以人生遗憾与“最后的机会”说明为何要补足临终学习实践的短板，并称之为养老院的灵魂（P017–P021）。",
    "反面例证与类比：安乐窝实为地狱、游戏机龙虾ICU之问、候刑室类比，推出好吃好喝路线行不通（P022–P028）。",
    "落到投资判断：理念未实践前股票不值得投资；并给出“最好的死法”格言（P029–P030）。",
    "预设并回应“太理想、不适合多数人”的质疑，区分围观者与加入者的多轮试炼路径（P032–P036）。",
    "结论：能走到最后者少、非金钱可入，须早寻同路人并做与世无争、无尽头之事，故能代代传承（P037–P044）。"
   ],
   "concept_usage": [
    {"term": "养老院／养老机构", "meaning": "本文中被重新规定为以生死之学为核心的学术机构、修院、修行所、研究所与实践教学中心，而非消费型生活设施。", "evidence": "P003", "ambiguity": "同一篇中“它”在学术机构、慈善机构、修院、大学之间滑动，组织形态边界未明。"},
    {"term": "“纯享福”", "meaning": "引号标示的流行想象：消费毕生积蓄换取不必再劳动即可享受。", "evidence": "P001", "ambiguity": "作者引述并否定，非作者主张。"},
    {"term": "修院", "meaning": "类比宗教修行机构，指养老院在本质上首先应是修行场所。", "evidence": "P004", "ambiguity": "是类比还是制度主张，未明说。"},
    {"term": "向死而生", "meaning": "与“舒适的活法”相对的死亡态度，即平安地面对死亡。", "evidence": "P005", "ambiguity": "未给出可操作定义。"},
    {"term": "灵魂", "meaning": "比喻用法：养老院必须拥有的核心，即补足临终学习与实践的短板。", "evidence": "P021", "ambiguity": "修辞性表述，非制度定义。"},
    {"term": "与世无争", "meaning": "加入者所从事之事的性质条件之一，与政治影响力、世俗商品相对。", "evidence": "P040", "ambiguity": "具体判准未给出。"},
    {"term": "股票不值得投资", "meaning": "针对养老机构的具体行动/投资判断，附有时间条件（理念被实践之前）。", "evidence": "P029", "ambiguity": "未指名任何公司或行业，属待外部核查的事实性断言。"}
   ],
   "examples_and_targets": [
    "隔壁老张的房刚空掉、老李被从卫生间抱出来送走：作者用来例示养老院中高频死亡的日常场景（作者例证/情境描写，P024）。",
    "一万台游戏机、龙虾和鲜鲍、每隔一间房就是最先进的icu和最训练有素的护士：假想的豪华配置清单，作为被反驳的“纯享乐”方案（P026）。",
    "死刑犯行刑前一周受到的饮食优待与密切安排的医疗看护：类比材料，用以说明好吃好喝的候刑室性质（P027）。",
    "义务教育学校、医疗教育机构、企事业机构、监管教化机构：作者建议建立制度化交流的机构类型（P010）。",
    "老年人、中年讨论者、幼年学习者：作者设定的机构成员构成（P008）。",
    "图利之人、拿钱申请者、买养老机构股票者：作者论证中的对象类别（P029、P038、P042）。",
    "“如何树立正确的财富观？”：出现在P031的独立问句，lexical 未覆盖，非本文论证使用的例子（P031）。"
   ],
   "conditions": [
    "投资判断附时间条件：“在看到养老机构明白这个理念、实实在在地实践起这个理念之前”（P029）。",
    "生死观早期教育“甚至不是加大金钱投资（或任何其他形式）可以弥补和替代的”（P012）。",
    "加入路径条件：必须经过多轮谈论、实践、试炼、获得资格、发愿，但任何一环都可自由改变主意（P034–P035）。",
    "人数条件：“走到最后一层的注定不会是很多人，因为这件事本来并非任何人都可以办得到”（P037）。",
    "资格条件：不是拿钱申请即可进入，须自己从十几二十几年前开始寻找同路人（P038–P039）。",
    "所做之事的性质条件：与世无争、不可转化为政治影响力、不能转化为与世俗竞争的商品、图利者觉得得不偿失、没有尽头（P040–P043）。",
    "对“太理想／不适合大多数人”的质疑只给出围观与短期交流的应对，未说明不适合者的替代安排（P032–P033）。"
   ],
   "rhetoric_and_tone": "训诫与布道式断言，短句排比（“它应该是……”“它必须……”连用），第二人称“你”直接对话读者；密集反问（“又怎么样呢？”“有本质什么区别？”）；宗教与修行语汇（修院、修行所、发愿、无我之我、荣耀）；强否定与夸张意象（地狱、候刑室、在劫难逃）；引号标示流行说法（“纯享福”“对得起余生”“养老机构”）；以格言收束（“最好的死法，是鞠躬尽瘁、死而后已。”）。",
   "unresolved_questions": [
    "P031“如何树立正确的财富观？”为正文中出现但 lexical 未覆盖的独立问句，与前后段（P030 最好的死法、P032 关于太理想的反问）无衔接，疑为平台插入的话题/问题片段，归属不明，需人工核对；本记录未将其作为作者主张。",
    "“这样的机构”究竟指学术机构、慈善机构、修院还是大学，文中并列多种说法，组织形态与法律身份边界未明。",
    "加入资格“一轮轮”谈论、实践、试炼的主持者、判准与期限，正文未说明。",
    "“他们的股票不值得投资”未指名任何公司或行业，也无数据，属待外部核查的事实性断言。",
    "对“不适合而羡慕的人”只给围观或短期交流，未说明其余大多数人的替代性生死教育安排。",
    "机构的资金来源、运营主体、与既有养老与医疗制度的关系，正文未说明。",
    "本篇 updated_at 晚于首次发布（2021-06-19 vs 2020-07-25），语料未提供 provenance/superseded，版本差异不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "凡是这样想的人，必然要失败。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "养老院首先应该是一所关于生存和死亡的学术机构。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "而是在提供一种平安的、向死而生的死法。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P009", "quote": "它应该成为一家制度性的、周期性的、本质意义上的、与社会有紧密而深刻的互动的学术机构和慈善机构。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P010", "quote": "应该是义务教育学校、医疗教育机构、企事业机构、监管教化机构的常规制度性安排。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P011", "quote": "临终之人的价值，被非理性的死亡恐惧引发的病态讳疾忌医完全浪费了。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P013", "quote": "它最常进行的活动，应该是关于人的生命的哲学、伦理学的研究、讨论和传承", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P017", "quote": "人生最大的遗憾，其实不是活的不幸福，而是因为恐惧死亡和匮乏，而没有真正毫无顾忌的、专心专意的爱过。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P019", "quote": "你反而获得了这个最纯、最美、最无顾忌的机会。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P020", "quote": "这样的机会常常并不能转化为真正有效的、值得你安慰的实际效果", "relation": "qualifies"},
    {"key": "E011", "paragraph_id": "P021", "quote": "这个短板，才是一个“养老院”真正最值得补足、也必须补足的东西。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P028", "quote": "那么仅仅搞好吃好喝的养老院就是根本行不通的。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P029", "quote": "在看到养老机构明白这个理念、实实在在地实践起这个理念之前，他们的股票是不值得投资的。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P032", "quote": "很多人在问这样的机构岂不是太理想了吗？对大多数人并不适合啊……", "relation": "context"},
    {"key": "E015", "paragraph_id": "P033", "quote": "对于不适合而羡慕的人，可以外围围观或者做短期交流。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P034", "quote": "这是要一轮一轮的谈论，一轮轮的实践，一轮一轮的试炼，一轮一轮的获得资格，一轮一轮的发愿的过程。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P035", "quote": "任何一环，你都可以完全自由的、毫无后果的改变主意。", "relation": "qualifies"},
    {"key": "E018", "paragraph_id": "P037", "quote": "走到最后一层的注定不会是很多人，因为这件事本来并非任何人都可以办得到。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P038", "quote": "这不是谁办了，你只要拿钱去申请就可以进得去的。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P040", "quote": "这事不是随便什么事，它必须是与世无争的事。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P042", "quote": "它必须是一种只要图利之人就觉得得不偿失，而所有人都苦于没人肯去做的事。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P043", "quote": "这事还要没有尽头，逻辑上就没有做成可言。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P001", "quote": "很多人都觉得养老院是一个舒适的生活设施外加一个密切伺候设备完善的护理机构", "relation": "context"},
    {"key": "E024", "paragraph_id": "P004", "quote": "它在本质上，首先必须是一种修院。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P006", "quote": "它应该是人解脱尘世执着和恩怨的修行所。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P007", "quote": "获取和传授这类知识和技艺的研究所、实践场和教学中心。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P008", "quote": "它应该是一所聚集了老年人、中年讨论者和幼年学习者的关于生和死的大学。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P012", "quote": "这种教育，甚至不是加大金钱投资（或任何其他形式）可以弥补和替代的。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P013", "quote": "帮助原谅、帮助修和、帮助宽容、帮助放下和帮助送别的实践。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P014", "quote": "反而应该是忙碌的、奋进的和矢志不渝的。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P016", "quote": "它应该是帮助人最后超脱私己，成为无我之我的地方。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P023", "quote": "那些燃烧毕生积蓄的安乐窝、逍遥乡，反而是最令人心惊胆战的地狱。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P030", "quote": "最好的死法，是鞠躬尽瘁、死而后已。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P039", "quote": "而是你自己从十几二十几年前就要开始寻找同路的人，找到可做的事。", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P041", "quote": "它不可以转化为政治影响力，也不能转化为某种与世俗竞争的商品。", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P044", "quote": "所以才能代代传承。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["临终关怀与生死学", "养老制度与机构设计", "宗教/修行与生命教育", "投资判断（养老产业）"],
   "issue_candidates": ["养老院的性质与目标", "临终者价值的利用", "生死观早期教育", "死亡恐惧与讳疾忌医", "加入资格与试炼机制", "养老机构股票是否值得投资"],
   "text_function_candidates": ["答疑（回应设问）", "理念申说", "批评（否定流行养老院模式）", "训诫/劝勉"],
   "object_candidates": ["养老院/养老机构", "义务教育学校", "医疗教育机构", "企事业机构", "监管教化机构", "投资者/图利之人", "老年人、中年讨论者、幼年学习者"],
   "working_keywords": ["向死而生", "修院", "修行所", "无我之我", "纯享福", "候刑室", "生死观早期教育", "与世无争", "代代传承"]
  },
  "notes": "本篇无图片节点。正文存在 text/lexical 分歧：P031“如何树立正确的财富观？”为 text 有而 lexical 未覆盖的片段（skeleton divergence=true），已在 unresolved_questions 登记，未据此建立任何作者主张。"
 },
 "ff409442": {
  "analysis": {
   "question_context": "提问者（知乎问题）问“如何定义「有用」？”，要求给出定义。作者的正文是直接给出的定义性回答：以三条编号条件界定“有价值”，并附自查方法与一条排除项。全文为作者主张，未引述他人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "第一条：有人想要，且是想要到肯拿有价值的东西（尤其专门付出的时间）来换的程度，而非随便什么程度的想要。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "什么代价也不打算付出的白要不属于想要。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006"], "summary": "给出自我追问清单（出钱、出力、冒险、担责、流血、流汗），都没有就不该自欺欺人说“我想要”。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "排除项：为它“伤心”“难过”这类“感情损失”不计分。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "第二条：得到之后这人会变好，即拥有更多可能性——以前办不到的事可以办到；健康、财富、智慧是三种不同形式的“可能性通货”。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P011"], "summary": "第三条：得到这东西的人，也使得被ta所祝福的人得到更多可能性。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013"], "summary": "结论：任何事物只要满足这三个条件，就是绝对意义上有价值的，哪怕它是免费的——尤其当它是免费的。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“有用/有价值”的第一条件是有人想要，且是想要到肯拿有价值的东西（尤其专门付出的时间）来换的程度。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "什么代价也不打算付出的白要不属于想要。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判断自己是否真的“想要”，应追问是否为它出钱、出力、冒险、担责、流血、流汗；都没有就不应自欺欺人说“我想要”。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "negated", "statement": "为它“伤心”“难过”这类“感情损失”不计分。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二条件是得到之后这人会变好，即ta自己因此拥有更多可能性，以前办不到的事可以办到。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "健康、财富、智慧归根到底只是三种不同形式的“可能性通货”。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第三条件是得到这东西的人，也使得被ta所祝福的人得到更多的可能性。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何事物只要满足这三个条件，就是绝对意义上有价值的，哪怕它是免费的——尤其当它是免费的。", "evidence": ["E010", "E011"]}
   ],
   "argument_steps": [
    "以编号列举方式直接给出定义，第一条为“有人想要”（P001）。",
    "限定“想要”的强度：须肯拿有价值之物、尤其是专门付出的时间来换（P002）。",
    "排除无代价的白要（P003）。",
    "把判准转为可操作的自问清单：出钱/出力/冒险/担责/流血/流汗，否则是自欺（P004–P006）。",
    "追加排除项：感情损失不计分（P007）。",
    "第二条：得到者自身可能性增加（P008–P009），并把健康、财富、智慧归为“可能性通货”（P010）。",
    "第三条：得到者使被其祝福的人也获得更多可能性（P011）。",
    "结论：三条件同时满足即绝对意义上有价值，免费不构成减分（P012–P013）。"
   ],
   "concept_usage": [
    {"term": "有用／有价值", "meaning": "由三条条件共同界定的“绝对意义上有价值”，而非价格或主观效用。", "evidence": "P012", "ambiguity": "提问用「有用」，正文主要用“有价值/绝对意义上有价值”，二者是否同义未说明。"},
    {"term": "想要", "meaning": "以达到肯付出有价值之物（尤其专门付出的时间）为凭的意愿。", "evidence": "P002", "ambiguity": "“有价值的东西”的范围未列举完整。"},
    {"term": "可能性", "meaning": "“变好”的判据：能办到以前办不到的事。", "evidence": "P009", "ambiguity": "如何度量、由谁判定未说明。"},
    {"term": "可能性通货", "meaning": "比喻：健康、财富、智慧是三种不同形式的可交换“可能性”。", "evidence": "P010", "ambiguity": "三者能否互换、兑换率如何未说明。"},
    {"term": "祝福", "meaning": "得到者使他人也获得更多可能性的关系。", "evidence": "P011", "ambiguity": "“被ta所祝福的人”范围未界定。"},
    {"term": "感情损失", "meaning": "被明确排除在代价之外的项目（伤心、难过等）。", "evidence": "P007", "ambiguity": "只给排除，未说明何种非物质付出可以计分。"}
   ],
   "examples_and_targets": [
    "自问清单“我为此出钱了吗？出力了吗？冒险了吗？担责了吗？流血了吗？流汗了吗？”：作者给出的自查例证（P004）。",
    "“我为它‘伤心’了、‘难过’了”式的感情付出：被作者列为不计分的排除项（P007）。",
    "健康、财富、智慧：作者列举的三种“可能性通货”（P010）。",
    "“免费的”事物：作者用来强调结论的边界样例（P013）。",
    "全篇未出现具体人物、机构、事件或数据。"
   ],
   "conditions": [
    "“想要”须达到肯付出有价值之物（尤其时间）的程度；不打算付代价的白要被排除（P002–P003）。",
    "“感情损失”不计分，即非物质情绪付出不构成代价（P007）。",
    "三条件须同时满足才称“绝对意义上有价值”（P012）。",
    "“尤其当它是免费的”是对免费事物的特别强调，非排除条件（P013）。",
    "全篇为普遍化定义，未限定适用对象、时间或场景。"
   ],
   "rhetoric_and_tone": "简洁断言＋编号推进（第一/第二/第三）；第二人称训诫式自省清单；口语插入语“Btw”；破折号强调；短句断喝（“不，你不想。”）；结尾以反直觉强调收束（“哪怕它是免费的——尤其当它是免费的。”）。",
   "unresolved_questions": [
    "提问用「有用」，正文用“有价值／绝对意义上有价值”，两者是否同义、回答是否覆盖「有用」的日常用法，文中未说明。",
    "三条件以“只要满足……就是”表述为充分条件，但是否同时为必要条件，正文未说明。",
    "“可能性”的度量方式与“变好”的判定主体未说明。",
    "“被ta所祝福的人”的范围（直接受赠者、间接受益者或其他）未界定。",
    "“感情损失不计分”只给排除项，未说明何种非货币付出可以计分（如时间以外的代价形式）。",
    "“绝对意义上有价值”是否等同道德意义上的“好”，文中未展开。",
    "本篇 updated_at（2021-05-25）晚于发布（2020-07-26），语料无 provenance/superseded，版本差异不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "而是想要到肯拿有价值的东西——尤其是专门付出的时间——来换的程度。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "什么代价也不打算付出的白要不属于想要。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "我为此出钱了吗？出力了吗？冒险了吗？担责了吗？流血了吗？流汗了吗？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "都没有，就不要一直自欺欺人说“我想要”。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "我为它“伤心”了、“难过”了这类“感情损失”不计分。", "relation": "qualifies"},
    {"key": "E006", "paragraph_id": "P008", "quote": "第二，这人得到之后会变好。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "某些以前ta办不到的事，因为有了这个ta可以办到了。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "健康、财富、智慧，归根到底其实只是三种不同形式的“可能性通货”。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "第三，得到了这东西的人，也使得被ta所祝福的人得到更多的可能性。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "任何事物，只要满足这三个条件，就是绝对意义上有价值的。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "哪怕它是免费的——尤其当它是免费的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["价值论/定义问题", "日常语用辨析", "行为与动机自省"],
   "issue_candidates": ["如何定义有用/有价值", "意愿与代价的关系", "可能性的增加作为价值判据", "感情的代价是否计分", "免费事物的价值"],
   "text_function_candidates": ["答疑（回应定义提问）", "定义/辨析", "说教/自省指导"],
   "object_candidates": ["提问者/读者（第二人称“你”）", "得到某物的人（ta）", "被其祝福的人"],
   "working_keywords": ["有用", "有价值", "想要", "可能性", "可能性通货", "变好", "祝福", "感情损失", "代价", "免费"]
  },
  "notes": "本篇无图片节点，无 text/lexical 分歧。全篇为作者自述定义，无引用、转述或反驳对象（除被排除的“感情损失”用法）。"
 },
 "ab86a299": {
  "analysis": {
   "question_context": "提问者（知乎问题）问“做一个棱角分明的人有错吗？”，带辩护性预设。作者先重新界定“棱角”，再回答：有原则是好事，但“有棱角”绝对是坏事；同时反驳由此推出袖手旁观的结论，要求见不义必须有所作为而极尽可能谨慎。提问者的立场不等于作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "重新界定：棱角不是有无原则或正义感，而是基于原则和正义感的行动是否有不必要的进攻性。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "提出问题：被触犯义理原则是否意味着获得惩罚、打击、伤害对方的正当性，请读者自省。", "role": "questioned"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "指出关键在于是否自认是正义的最高法官、拥有不可辩驳的权威判断；“有棱角”即“我自知正义”与“我可施以刑罚”的自我认定。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "判断：有原则是好事（至少不坏），但“有棱角”绝对是坏事。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "理由：他人可能在毫无觉察与沟通机会时就被视为必须天诛的国贼，年轻人尤甚；以血滴子、雍正王朝、新选组为喻与反问。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "让步并反驳：判断不见得准确不是袖手旁观的理由，只是出手谨慎的理由；世界上没有绝对准确正义的人，绝对完美等于抛弃正义与真理的可能性。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015", "P016"], "summary": "行动要求：见到良知所不能认同的不义一定要有所作为，同时因判断力有限、情绪冲动、私心难除而极尽可能谨慎，循最稳妥最正当途径避免过大不可逆伤害。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "谨慎的具体化：连用词与句式都要自问；私下向有正当职责者反映优于先到处嚷嚷；以判断错误后果与“流血现场未必是凶手”的例子说明不可逆伤害风险。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P022", "P023"], "summary": "“上去就是一砖头”即所谓“有棱角”，并指这类棱角驱动过打向“反动学术权威”的铜头武装带和砸向人头的U型锁。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P024", "P025"], "summary": "结论与讽刺：不要相信“年轻人就是要有点棱角”的鬼话，说这话的人往往自己不给别人尝棱角的机会。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "棱角不是指有没有原则或正义感，而是指基于自己的原则和正义感所采取的行动是否有不必要的进攻性。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关键在于人是否在某种程度上认定自己就是正义的最高法官、拥有不可辩驳的权威判断；“有棱角”即“我自知正义”与“我可施以刑罚”的自我认定。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有原则是一件好事，至少是一件不坏的事；但“有棱角”绝对是一件坏事。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人很可能在没有任何觉察和沟通机会时就被视为必须天诛的国贼，缺少体会的年轻人尤其如此。", "evidence": ["E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "自己的判断不见得准确、行动不能保证绝对正义，并不是应该袖手旁观的理由，而只是应该出手谨慎的理由。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上根本没有判断绝对准确、行动绝对正义的人；正义不可避免要靠不够正义的人用并非完美无缺的办法执行，要求绝对完美等于抛弃正义的一切可能性。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "见到不义一定要有所作为，无论是对是错；因良知不认同的不义而完全无所作为是绝对不可取的。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要考虑到判断力有限、情绪冲动、私心无法清除，因此极尽可能谨慎；谨慎指循最稳妥、最正当的途径，尽可能避免一切过大的、不可逆的伤害。", "evidence": ["E011", "E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然可以私下去向有正当职责管理此事的人员反映，就不可以用“先到处嚷嚷开”的办法，因为后者造成的影响立刻不可逆、不可控。", "evidence": ["E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使看到一人躺在地上满是鲜血、另一人拿着刀，也不能断定后者就是凶手（也可能是抢救路人的大夫），所以不能上去就是一砖头，而要立刻叫警察。", "evidence": ["E015", "E016"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要相信“年轻人就是要有点棱角”的鬼话；说这话的人往往自己不肯给别人尝被“棱角”对待的滋味。", "evidence": ["E017", "E018"]}
   ],
   "argument_steps": [
    "以否定式定义开头：棱角无关原则或正义感的有无（P001），而指行动中不必要的进攻性（P002）。",
    "以问句把读者带入自省：被冒犯是否等于获得惩罚伤害对方的正当性（P003–P004）。",
    "点出关键在自我认定为正义最高法官，并给“有棱角”下判断式定义（P005–P006）。",
    "给出核心评价：有原则是好事，有棱角绝对是坏事（P007）。",
    "列举理由：误判与缺乏沟通机会，年轻人尤甚，用血滴子、雍正王朝、新选组作夸张类比与反问（P008–P009）。",
    "自行提出反对意见（难道该高高挂起？）并断然否定（“错了。”），区分“应谨慎”与“应旁观”（P010–P012）。",
    "以“真理注定由谬误之人讲述”作平行类比强化（P013）。",
    "给出行动要求的两面：必须有所作为，同时极尽可能谨慎（P014–P016）。",
    "把谨慎操作化：措辞自问、选择渠道（私下反映优于公开嚷嚷）、比较误判后果的不可逆性、以血案现场为例（P017–P021）。",
    "反面界定：上去就是一砖头即“有棱角”，并指其历史后果（P022–P023）。",
    "结论：以讽刺引语否定“年轻人要有棱角”的说法（P024–P025）。"
   ],
   "concept_usage": [
    {"term": "棱角", "meaning": "本文界定为基于原则与正义感的行动中不必要的进攻性，以及“我自知正义／我可施以刑罚”的自我认定；作者评价其为坏事。", "evidence": "P002", "ambiguity": "“不必要的进攻性”的判准未给出；作者用“在最终意义上”作限定（P006）。"},
    {"term": "原则／正义感", "meaning": "与棱角相区分的东西，作者认为有原则本身是好或至少不坏的事。", "evidence": "P007", "ambiguity": "未说明原则从何而来、如何检验。"},
    {"term": "正义的最高法官", "meaning": "被批评的自我定位：自认拥有不可辩驳的权威判断。", "evidence": "P005", "ambiguity": "是心理描述还是制度批评，未明说。"},
    {"term": "谨慎", "meaning": "循最稳妥、最正当的途径，尽可能避免一切过大的、不可逆的伤害。", "evidence": "P016", "ambiguity": "与“一定要有所作为”冲突时的优先级未给出。"},
    {"term": "不可逆的伤害", "meaning": "谨慎要避免的核心风险，包括冤枉他人乃至无意间杀人。", "evidence": "P016", "ambiguity": "未给出风险可接受程度的界线。"},
    {"term": "有所作为", "meaning": "见到良知不认同的不义必须有行动，无论对错。", "evidence": "P014", "ambiguity": "行动的合法与有效边界未展开。"}
   ],
   "examples_and_targets": [
    "血滴子、雍正王朝：夸张比喻，形容年轻人把规则全执行出来的杀伤规模（P008，修辞材料）。",
    "新选组：反问“谁愿意与新选组同区？”，用作类比（P009，修辞材料）。",
    "私下向有正当职责管理此事的人员反映 vs 先到处嚷嚷开：作者的行动方案对比（P018，作者例证与建议）。",
    "一人躺在地上满是鲜血、另一人拿着一把刀，也可能是用简陋工具抢救路人的大夫：作者反例，说明判断易错（P021）。",
    "上去就是一砖头：被批评的“有棱角”行为（P022，反驳对象）。",
    "打向“反动学术权威”的铜头武装带、砸向人头的U型锁：作者举的历史指涉，作为棱角后果的例证（P023；具体史实待外部核查）。",
    "“年轻人就是要有点棱角”：被作者称为鬼话的流行说法（P024，反驳对象）。",
    "“年轻人有棱角很好嘛——可惜我这刚好已经招满人了。”：作者引用的讽刺性回应（P025；说话者为作者假想的招聘者，非作者立场转述）。"
   ],
   "conditions": [
    "以“有人触犯到你的义理原则、被你看作不正义”为假设前提，追问惩罚的正当性（P003）。",
    "“在最终意义上”限定棱角的定义层级（P006）。",
    "“哪怕只是一句话”也须追问是否必要用贬义词、反问句（P017）。",
    "“既然这个办法可行”为前提，推出不可用公开嚷嚷的办法（P018）。",
    "“如果你弄错了”假设条件下分析两种渠道的不同后果（P019）。",
    "“即使你看到……也不能表示”限定从现象判断凶手的可靠性（P021）。",
    "“你要充分地考虑到你可能判断错误”要求以不确定为前提行动（P020）。"
   ],
   "rhetoric_and_tone": "训诫与劝导语气，第二人称“你”贯穿；密集反问（“这是否意味着……？”“谁愿意与新选组同区？”“难道……高高挂起吗？”）；让步—反驳结构（提问、再以“错了。”断然否定）；反讽与夸张（血滴子武装整个雍正王朝、U型锁、鬼话、社交黑名单）；以讽刺引语收束，全篇带强烈的道德劝谕色彩。",
   "unresolved_questions": [
    "判定“不义”的主体与标准未给出；“有正当职责管理这件事的人员”具体指哪些岗位与程序，正文未说明。",
    "“不必要的进攻性”中“必要”的判准未界定。",
    "铜头武装带与U型锁所指的具体历史事件与人群，正文未说明，相关史实待外部核查。",
    "私下反映若无效或渠道本身不正当、不作为时应当如何，正文未说明。",
    "“一定要有所作为”与“极尽可能谨慎”冲突时的优先次序，正文未给出。",
    "提问者问“有错吗”，作者答“绝对是坏事”，但未界定坏的程度、后果形态与是否可补救。",
    "本篇 updated_at 为 2026-01-11，远晚于发布（2020-07-27），语料无 provenance/superseded，是否经修改不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "棱角不是指你有没有原则或者正义感。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "棱角是指你基于自己的原则和正义感而采取的行动是否有不必要的进攻性。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "你是否会在某种程度上认定自己就是正义的最高法官，拥有不可辩驳的权威判断。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "就是指人有这种“我自知正义”和“我可施以刑罚”的自我认定。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "但是“有棱角”，这绝对是一件坏事。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "人家很可能没有任何觉察和沟通的机会就已经被你视为必须天诛的国贼了。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P012", "quote": "并不是你应该袖手旁观的理由，它们只是你应该出手谨慎的理由。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P012", "quote": "因为世界上根本没有这种判断绝对准确、行动绝对正义的人。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "一定要绝对完美，等于彻底抛弃正义的一切可能性。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P014", "quote": "见到不义，一定要有所作为，无论是对是错，你都要有所作为。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P015", "quote": "你的判断力有限、你的情绪冲动、你的私心无法清除，所以要极尽可能的谨慎。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P016", "quote": "所谓谨慎，是指循最稳妥、最正当的途径，尽可能避免一切过大的、不可逆的伤害。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P018", "quote": "你可以私下去向有正当职责管理这件事的人员反映情况。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P018", "quote": "因为你直接嚷嚷开，造成的影响立刻就是不可逆、不可控的。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P021", "quote": "也不能表示这人就是凶手——ta也可能是用简陋工具抢救路人的大夫。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "所以你不能上去就是一砖头，而是要立刻叫警察。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P024", "quote": "永远不要相信那种“年轻人就是要有点棱角”的鬼话", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P024", "quote": "你看ta肯不肯给你机会让ta尝尝被“棱角”的滋味？", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P008", "quote": "浑身的规则都提取出来做成血滴子足以武装整个雍正王朝", "relation": "context"},
    {"key": "E020", "paragraph_id": "P023", "quote": "就是它驱动了打向“反动学术权威”的铜头武装带和砸向人头的U型锁。", "relation": "context"},
    {"key": "E021", "paragraph_id": "P025", "quote": "“年轻人有棱角很好嘛——可惜我这刚好已经招满人了。”", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理与正义观", "个人品格/处世方式", "公共行动与判断风险"],
   "issue_candidates": ["棱角与原则的区别", "私自惩罚他人的正当性", "判断错误的不可逆后果", "见不义是否应当介入", "谨慎与作为的张力"],
   "text_function_candidates": ["答疑（回应提问）", "辨析/正名", "论辩（反驳流行说法）", "训诫/劝谕"],
   "object_candidates": ["提问者", "读者（第二人称“你”）", "年轻人", "有正当职责管理此事的人员", "警察", "“反动学术权威”批斗相关历史指涉", "新选组", "雍正王朝"],
   "working_keywords": ["棱角", "原则", "正义感", "正义的最高法官", "我自知正义", "我可施以刑罚", "谨慎", "不可逆的伤害", "有所作为", "血滴子", "U型锁"]
  },
  "notes": "本篇无图片节点，无 text/lexical 分歧。P025 的引语为作者假想的招聘者台词，记录中按上下文标为讽刺引语，未归为作者立场。"
 },
 "df3a1f00": {
  "analysis": {
   "question_context": "提问者（知乎问题）以反事实假设提问“假如血管不在皮肤表层，当代医学将会如何？”。作者不讨论医学层面，而是把该假设当作解剖学前提，推演人体供血方案被迫改变后的连锁后果。全篇为假设性推演，未引述他人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回应假设：首先出问题的不是医学，而是人类自己怕是要完蛋。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "解剖前提与类比：大流量血管不能随意穿行肌肉，如住宅楼网线须走“管井”，即沿肌肉交错间隙、骨缝可保留的沟槽或体表。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "陈述现行方案：内外层肌肉各靠相应毛细血管，穿插靠总管找空隙通过，深入肌肉内部的只有最后几级毛细血管。", "role": "context"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "在取消体表主血管的前提下，供血起点都在肌肉层下，表层肌肉须靠粗几级的次级血管硬从内向外穿。", "role": "hypothetical"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009"], "summary": "后果链：用力时肌肉收缩把埋在肌肉里的中级血管挤干（如吸满水的海绵），血压陡升恐逆向扰乱心律，表层肌肉供血中断。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "进一步后果：多蹦多顶会全身绀紫、一头栽倒在地。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012"], "summary": "结论：肌肉层须减弱到现在的一半厚度（放弃外层难供血的一半），人类怕要变成瘦竹竿；这是非常坏的方案。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果血管不在皮肤表层，首先出问题的不是医学，而是人类自己怕是要完蛋。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大流量的血管不能在肌肉里随便穿来穿去，它像住宅楼网线必须走身体里的“管井”，即沿肌肉交错的间隙、骨缝可保留的沟槽或体表。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现行方案是内层肌肉靠内层毛细血管、外层肌肉靠外层毛细血管，穿插靠总管找空隙通过，深入肌肉内部的只有最后几级毛细血管。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "在不允许主血管走体表的前提下，供血起点都在肌肉层下面，要让表层肌肉得到血液供应，须靠粗几级的次级血管硬在肌肉里从内向外穿。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "用力时肌肉收缩会把埋在肌肉里面的中级血管一起“挤干”（它们像埋在肌肉里吸满水的海绵），血压会陡然上升，恐怕足以逆向扰乱心律。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "表层肌肉会因供血中断而憋得不行，多蹦多顶只怕会全身绀紫、一头栽倒在地。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "结果肌肉层基本都要减弱到现在的一半厚度（放弃外层难以供血的一半），人类怕是要变成瘦竹竿。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是个非常坏的方案。", "evidence": ["E011"]}
   ],
   "argument_steps": [
    "接过提问的假设，先给出总判断：受害的不是医学而是人类存续（P001）。",
    "给出解剖学前提并用“住宅楼网线走管井”类比，指明大流量血管的可行通道（P002–P004）。",
    "描述现行供血方案，为反事实推演设定对照（P005）。",
    "在前提中取消体表通道，推出供血起点下移、次级血管须由内向外硬穿的替代路径（P006）。",
    "推演后果链：肌肉收缩→中级血管被挤干（海绵比喻）→血压陡升→心律可能被逆向扰乱→表层供血中断（P007–P009）。",
    "加重后果：多蹦多顶会全身绀紫、栽倒（P010）。",
    "推出结构性代价：肌肉层须减半，人类变瘦竹竿；定性为非常坏的方案（P011–P012）。"
   ],
   "concept_usage": [
    {"term": "“管井”", "meaning": "比喻住宅楼网线的走线通道，指大流量血管可用的解剖通道：肌肉交错间隙、骨缝沟槽、体表。", "evidence": "P002", "ambiguity": "三类通道之间的取舍关系未说明。"},
    {"term": "主血管／总管／次级血管／中级血管／毛细血管", "meaning": "按管径与层级描述的供血路径，用于说明体表通道取消后的替代困难。", "evidence": "P005", "ambiguity": "未给出各层级的解剖学定义或数据。"},
    {"term": "体表", "meaning": "被假设取消的血管通道，也是全文讨论的变量。", "evidence": "P004", "ambiguity": "提问设为“不在皮肤表层”，作者读作“不允许主血管走体表”（P006）。"},
    {"term": "“穿越火线”／“挤干”／“海绵”", "meaning": "比喻肌肉收缩对埋于其中的血管的挤压效应。", "evidence": "P007", "ambiguity": "为形象化说明，未给出压力数值。"},
    {"term": "绀紫", "meaning": "表层肌肉供血中断后的体表表现。", "evidence": "P010", "ambiguity": "未说明其出现的阈值条件。"}
   ],
   "examples_and_targets": [
    "住宅楼里的网线走“管井”：类比材料，说明大流量血管的通道约束（P002）。",
    "埋在肌肉里的一块吸满水的“海绵”：类比材料，说明肌肉收缩挤干血管（P007）。",
    "“假如血管不在皮肤表层”：提问者设定的反事实前提，是本文的讨论对象（P001、P006）。",
    "“一半厚度”“粗几级的次级血管”：作者的数量性估计，非引用数据（P006、P011）。",
    "全篇未出现具体人物、机构、事件或文献。"
   ],
   "conditions": [
    "全篇以提问者的反事实假设为条件：血管不在皮肤表层（P001）。",
    "“在你不允许主血管走体表的前提下”为明确前提（P006）。",
    "“你一用力，肌肉一收缩”为触发后果链的动作条件（P007）。",
    "“你多蹦两下，多顶几下”为加剧后果的动作条件（P010）。",
    "推测语气贯穿：“怕是要完蛋”“恐怕足以”“只怕会”“怕是要变成”（P001、P008、P010、P011）。",
    "假设如何实现（先天变异、手术改造或纯思想实验）未说明；静脉、淋巴等其余管道是否受同一前提约束亦未说明。"
   ],
   "rhetoric_and_tone": "工程式假设推演＋生活化类比（网线管井、海绵、穿越火线）；第二人称“你”把读者代入身体；后果层层递进带黑色幽默（“怕是完蛋”“瘦竹竿”）；结尾以短句定性收束（“这是个非常坏的方案。”）。",
   "unresolved_questions": [
    "提问问“当代医学将会如何”，作者未回答医学层面，只推演人体后果，问题的一半未获回应。",
    "“一半厚度”“粗几级”等为作者估算，无数据来源，属解剖学/生理学事实性判断，待外部核查。",
    "“恐怕足以逆向扰乱你的心律”的生理机制未展开。",
    "该假设如何成立（先天变异、手术改造还是思想实验）未说明。",
    "未讨论静脉、淋巴等其余管道是否同样受“不走体表”前提约束。",
    "未说明取代方案在解剖上是否只是“坏”，还是根本不可行。",
    "本篇 updated_at（2021-11-12）晚于发布（2020-07-28），语料无 provenance/superseded，版本差异不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "如果那些不在皮肤表层，出问题的首先还不是医学，而是人类自己怕是要完蛋。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "大流量的血管是不能在肌肉里随便穿来穿去的，它就像你家住宅楼里的网线，必须走身体里的“管井”。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "不沿着肌肉交错的间隙，就是在骨缝可以保留的沟槽里。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "现在的方案是内层肌肉靠内层毛细血管，外层肌肉靠外层毛细血管", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "那么所有的起点就都在肌肉层下面了，要让表层肌肉都得到血液供应，要靠粗几级的次级血管强行“穿越火线”——硬在肌肉里从内向外穿。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "这些埋在肌肉里面的中级血管就会一起被“挤干”", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "你的血压就会陡然上升，恐怕足以逆向扰乱你的心律。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "更不用说一用力表层肌肉就憋得不行——血液供应中断了。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "你多蹦两下，多顶几下，只怕会全身绀紫，一头栽倒在地。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "人类怕是要变成瘦竹竿了。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "这是个非常坏的方案。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P007", "quote": "因为它们总的来说就好像埋在肌肉里的一块吸满水的“海绵”。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["解剖学/生理学假设推演", "人体结构与供血", "反事实工程分析"],
   "issue_candidates": ["体表血管通道的必要性", "把主血管埋入肌肉的后果", "肌肉收缩对血管的挤压", "人体形态的代价"],
   "text_function_candidates": ["答疑（回应假设性问题）", "推演/解释", "评论（评价该方案）"],
   "object_candidates": ["提问者", "读者（第二人称“你”）", "人类（作为推演对象）", "住宅楼网线/管井（类比）"],
   "working_keywords": ["皮肤表层", "管井", "主血管", "毛细血管", "次级血管", "穿越火线", "海绵", "血压", "心律", "绀紫", "瘦竹竿"]
  },
  "notes": "本篇无图片节点，无 text/lexical 分歧。全文为假设性推演，主要判断以 hypothetical/predicted 模态登记，未把推演结果写成外部事实。"
 },
 "9b6321a0": {
  "analysis": {
   "question_context": "提问者（知乎问题）问“什么叫做「完整的工业体系」？”。作者以定义＋正名作答：把“完整工业体系”界定为最大规模工业现代大国的工业体系，并反驳“类目罗列”式的定义路线。全篇为作者主张，未指名引用他人论述。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出定义：完整工业体系说白了就是“最大规模的工业现代大国的工业体系”；类似中国体量的国家完成现代化即自然构成新定义。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "定义权的历史转移：先在英国，后在苏联和美国手里。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "定义的奥妙在于“量体裁衣”，而不是来自类目罗列。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "反驳类目罗列路线：它只是把眼下霸主的状态改用类目描述，显得像“客观标准”，其实是完全“主观”的。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P008"], "summary": "理由：小国有的共性需求大国都有，因为大国本质上只是实现了“绝对同盟”的一体化“小国”联邦。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P009"], "summary": "只要大国完成现代化，仅从一般成本考量也会考虑用自己的力量实现供应。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P010", "P011"], "summary": "差距所在：大国会有小国没有或无力独立支撑的需求（水利治理、跨地域交通、能源输送、全球定位系统、深海极地外空探测、超大船舶、重载铁路、广域网络、超级计算机、大数据、基础物理研究等）；名单随时代霸主不同，不必特别去列。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P012"], "summary": "对比：这些需求小国要么没有，要么靠条约合作或市场交换满足；大国可以、甚至必须自己满足。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P013", "P014", "P015"], "summary": "结论：需求最多且能自己满足，自然生成同时代最完整的工业体系，谁跟它比都不够“完整”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "完整工业体系说白了就是“最大规模的工业现代大国的工业体系”。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "一个类似中国体量的国家完成了现代化，它的工业体系就自然构成“完整的工业体系”的新定义。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个定义权在中国起来之前属于苏联和美国，在苏美起来之前属于英国。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该定义的奥妙在于它是“量体裁衣”的，而不是来自什么类目罗列。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "走类目罗列路线的总结只是把眼下霸主的状态改用类目方式描述出来，显得像“客观标准”，其实它是完全“主观”的。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "小国有的共性需求大国都有，因为大国本质上只是一个实现了“绝对同盟”的一体化了的“小国”联邦。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这些需求只要大国完成了现代化，仅仅从一般的成本考量也会考虑用自己的力量来实现供应。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大国会有一些小国没有、或者绝对无力独立支撑的需求，如全流域水利治理、跨地域交通建设、超大范围超远距离能源输送、独立的全球定位系统、深海极地外空的探测和利用等；这个名单对每个时代的霸主都不一样，不必特别去列。", "evidence": ["E010", "E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些需求小国要么没有，要么靠条约合作或市场交换来满足；大国则可以自己满足，甚至也必须要自己满足。", "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然需求最多而且能自己满足，自然而然就会生成同时代最完整的工业体系，谁跟它比都不够“完整”。", "evidence": ["E013", "E014"]}
   ],
   "argument_steps": [
    "以“说白了”给出定义：完整工业体系即最大规模工业现代大国的工业体系（P001）。",
    "以体量类比中国说明定义随现代化大国更替（P002）。",
    "用定义权转移史（英国→苏联和美国→中国）支撑定义的相对性（P003–P004）。",
    "点出定义的奥妙是“量体裁衣”而非类目罗列（P005）。",
    "反驳类目罗列路线：它把霸主状态包装成“客观标准”，其实是主观的（P006–P007）。",
    "论证大国必有小国的共性需求：大国是实现了“绝对同盟”的一体化小国联邦（P008）。",
    "补充成本理由：现代化后大国从成本考量也会自行供应（P009）。",
    "列举大国独有需求，并说明名单随时代霸主变化、不必去列（P010–P011）。",
    "对比小国（条约合作/市场交换）与大国（可以且必须自给）（P012）。",
    "结论：需求最多＋能自给→同时代最完整的工业体系（P013–P015）。"
   ],
   "concept_usage": [
    {"term": "完整的工业体系", "meaning": "本文定义为“最大规模的工业现代大国的工业体系”，随霸主更替而变化，非固定类目清单。", "evidence": "P001", "ambiguity": "“完整”的可否量化、判准未给出。"},
    {"term": "定义权", "meaning": "由谁的状态被当作标准，历史上随霸主转移（英国→苏联和美国→中国）。", "evidence": "P003", "ambiguity": "未说明转移的具体机制与时点。"},
    {"term": "量体裁衣／类目罗列", "meaning": "两种定义方式的对比；后者被作者判为把霸主状态伪装成客观标准。", "evidence": "P005", "ambiguity": "作者未给出替代性的判准。"},
    {"term": "绝对同盟", "meaning": "用于描述大国本质：一体化了的“小国”联邦。", "evidence": "P008", "ambiguity": "未展开其含义与成立条件。"},
    {"term": "“客观标准”／“主观”", "meaning": "带引号使用，指类目罗列所伪装的客观性与其实际的主观性。", "evidence": "P006", "ambiguity": "作者未界定主客观标准的分界。"},
    {"term": "霸主", "meaning": "同时代最强、其状态被当作标准的国家。", "evidence": "P011", "ambiguity": "未说明霸主地位的判定标准。"}
   ],
   "examples_and_targets": [
    "中国：作为“类似中国体量”的现代化主体和当前定义权候选（P002、P003）。",
    "苏联、美国、英国：作者给出的历史上掌握定义权的霸主序列（P003–P004）。",
    "需求清单：全流域水利治理、跨地域交通建设、超大范围超远距离能源输送、独立全球定位系统、深海极地外空探测和利用、超大船舶、重载铁路、超高速广域网络、超级计算机、大数据、基础物理研究（P010，作者例证）。",
    "“类目罗列”路线的总结：被反驳对象（P006）。",
    "小国、大国、条约合作、市场交换：对比对象（P008、P012）。",
    "全篇未出现具体人物、机构、数据或文献引用。"
   ],
   "conditions": [
    "“一个类似中国体量的国家完成了现代化”为条件句，未断言已完成（P002）。",
    "“只要这个大国完成了现代化”为自给供应的条件（P009）。",
    "“对每个时代的霸主都不一样”——需求名单具时代相对性（P011）。",
    "“要么小国没有，要么有也是靠条约合作或者市场交换来满足”为两类情形的划分（P012）。",
    "以国别体量与现代化程度为隐含条件；“完整”的量化判据缺失。",
    "未说明中国是否已完成现代化，也未说明当下定义权归属。"
   ],
   "rhetoric_and_tone": "论辩与正名语气，断言式短句（“就是这样而已。”）；引号密集标示被质疑或需要重估的术语（“完整的工业体系”“量体裁衣”“客观标准”“主观”）；以英→苏美→中的历史序列推进；用排比式长清单强化“大国独有需求”的印象，并以“说白了”拉近口语距离。",
   "unresolved_questions": [
    "“类似中国体量”的判据（人口、面积、经济规模或其他）未说明。",
    "全文是否断言中国已完成现代化、当前定义权归属如何，均未明说（P002 为条件句）。",
    "“绝对同盟”的具体含义与成立条件未展开。",
    "否定类目罗列后未提供替代的可操作判准，“完整”仍无可量化标准。",
    "需求清单以“比如”举出且作者说“不必特别去列”，其边界不定。",
    "“这个定义权在苏联和美国手里”“在英国手里”等历史断言无出处与数据，属待外部核查。",
    "本篇 updated_at（2021-10-10）晚于发布（2020-07-28），语料无 provenance/superseded，版本差异不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "完整工业体系，说白了，就是“最大规模的工业现代大国的工业体系”。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "一个类似中国体量的国家完成了现代化，那么它的工业体系就自然构成“完整的工业体系”的新定义。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "中国没起来之前，这个定义权就在苏联和美国手里。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "苏联和美国没起来之前，这个定义就在英国手里。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "就在于它是“量体裁衣”的，而不是来自什么类目罗列。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "实际上只是在把眼下的霸主的状态改用类目的方式描述出来，显得好像是一个“客观标准”罢了。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "其实它是完全“主观”的。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "因为大国本质上只是一个实现了“绝对同盟”的一体化了的“小国”联邦。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "仅仅从一般的成本考量也会考虑用自己的力量来实现供应。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "大国会有一些小国没有、或者绝对无力独立支撑的需求", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "这个名单对每个时代的霸主都不一样，其实不必特别去列。", "relation": "qualifies"},
    {"key": "E012", "paragraph_id": "P012", "quote": "而不像大国，可以自己满足——甚至也必须要自己满足。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P013", "quote": "自然而然就会生成同时代最完整的工业体系。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "谁跟它比，都不够“完整”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["工业体系与国民经济", "概念定义/话语权", "大国与小国比较", "国际格局史"],
   "issue_candidates": ["完整工业体系的定义", "定义权归属", "类目罗列与量体裁衣之争", "小国共性需求与大国独有需求", "自给供应与条约合作/市场交换"],
   "text_function_candidates": ["答疑（回应定义提问）", "正名/辨析", "论辩（反驳类目罗列路线）"],
   "object_candidates": ["中国", "苏联", "美国", "英国", "大国", "小国", "霸主"],
   "working_keywords": ["完整的工业体系", "定义权", "量体裁衣", "类目罗列", "客观标准", "绝对同盟", "全流域水利治理", "全球定位系统", "基础物理研究", "自给"]
  },
  "notes": "本篇无图片节点，无 text/lexical 分歧。文中涉及定义权历史与大国需求的历史性断言均为作者陈述，本记录只作定位，不代为核实。"
 },
 "0eb2277c": {
  "analysis": {
   "question_context": "提问者（知乎问题）请求“有没有人能送我一句话，作为我努力活着的信念?”。作者以一篇短格言体给出劝慰式回应：世界专为你而造、世界随你的状态变化、你最重要、请不要放弃。全篇为作者对提问者的直接劝勉，未引述他人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总起断言：归根结底，这个世界是专为你而造的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007"], "summary": "六组“你……，世界就……”排比：存在/幸福/沮丧/仁慈/恨/放弃分别对应世界的活/亮/灰暗/宽容/恶毒/毁灭。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008"], "summary": "断言：世界上最重要的人就是你。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "结语请求：请不要放弃。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "归根结底，这个世界是专为你而造的。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界随“你”的状态而变：你存在世界就活着，你幸福世界就亮了，你沮丧世界就陷入灰暗，你仁慈世界就对一切都宽容，你恨世界就恶毒，你放弃世界就毁灭了。", "evidence": ["E002", "E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上最重要的人就是你。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "请不要放弃。", "evidence": ["E006"]}
   ],
   "argument_steps": [
    "以“归根结底”作总起断言：世界专为你而造（P001）。",
    "用六组状态对应句把世界的变化系于“你”的状态（P002–P007）。",
    "推出“世界上最重要的人就是你”（P008）。",
    "落到劝勉结论：请不要放弃（P009）。",
    "全篇无以理据支撑的推理链，靠排比与断言推进。"
   ],
   "concept_usage": [
    {"term": "世界", "meaning": "随“你”的状态而变动的对应物，用于劝慰而非宇宙论论证。", "evidence": "P001", "ambiguity": "是字面主张还是修辞劝慰，文中未明示。"},
    {"term": "你", "meaning": "直接称呼受话者（提问者/读者），全篇的参照中心。", "evidence": "P002", "ambiguity": "未说明该称呼是否仅针对提问者。"},
    {"term": "专为你而造", "meaning": "强调个体重要性的说法，为全篇定调。", "evidence": "P001", "ambiguity": "是否为宗教/唯心论命题，未说明。"},
    {"term": "放弃", "meaning": "被劝阻的行为，与“世界就毁灭了”相连。", "evidence": "P007", "ambiguity": "未界定放弃的具体所指（放弃生命或放弃努力）。"}
   ],
   "examples_and_targets": [
    "全篇无具体人物、事件、机构、地点或数据。",
    "六组状态对应（存在/幸福/沮丧/仁慈/恨/放弃）为修辞性列举，非经验例证（P002–P007）。",
    "劝勉对象为提问者/读者（第二人称“你”）。"
   ],
   "conditions": [
    "全篇为普遍化断言，无显式条件、例外或时间限定；“归根结底”作总括限定（P001）。",
    "“你放弃，世界就毁灭了”为条件—后果句，但条件如何成立未说明（P007）。",
    "未说明世界随你而变是字面事实描述还是比喻/劝慰修辞，两种读法均可能，本记录不代为裁决。"
   ],
   "rhetoric_and_tone": "第二人称劝勉/励志格言体；短句排比与留白分段形成节奏（lexical 含空段落）；从“世界”到“你”的情感递进；以直接请求收束（“请不要放弃。”），整体温和、鼓励、无训诫与讽刺。",
   "unresolved_questions": [
    "“这个世界是专为你而造的”是字面主张还是修辞劝慰，正文未明示，本记录不代为判定。",
    "该说法与宗教或唯心论命题的关系，正文未提及，属待外部思想史核查（不作结论）。",
    "作者未追问提问者“努力活着”的具体处境，也未给出可操作的行动建议。",
    "“放弃”的所指（放弃生命、放弃努力或其他）未界定。",
    "lexical 段落节点数为 13 而正文非空段落为 9，差额为空白段落，已按非空段落编号。",
    "本篇 updated_at（2022-05-26）晚于发布（2020-07-28），语料无 provenance/superseded，版本差异不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "归根结底，这个世界是专为你而造的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "你存在，世界就活着。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "你仁慈，世界就对一切都宽容。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P007", "quote": "你放弃，世界就毁灭了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P008", "quote": "世界上最重要的人就是你。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "请不要放弃。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生信念/心理劝慰", "励志格言", "生死与存在态度"],
   "issue_candidates": ["个体在世界中的位置", "情绪与世界状态的对应", "放弃与坚持", "自我重要性"],
   "text_function_candidates": ["答疑（回应“送我一句话”的请求）", "劝慰/鼓励", "格言体写作"],
   "object_candidates": ["提问者", "读者（第二人称“你”）", "世界"],
   "working_keywords": ["专为你而造", "世界", "最重要的人", "放弃", "信念"]
  },
  "notes": "本篇无图片节点，无 text/lexical 分歧（lexical 含空段落，已跳过）。全篇为劝慰性短章，未建立经验论证；相关判断按 asserted 模态登记，未当作外部事实。"
 },
 "1015117d": {
  "analysis": {
   "question_context": "提问者（知乎问题）问“什么是坚持?”。作者只以“择善固执。”一句四字作答，未展开解释。全篇为作者给出的一句定义式回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以“择善固执”四字回答“什么是坚持”。", "role": "definition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "坚持即择善固执（选择善并固执持守）。", "evidence": ["E001"]}
   ],
   "argument_steps": [
    "仅一步：以成语式短语“择善固执”直接给出坚持的界定，未提供理由、例证或条件说明（P001）。"
   ],
   "concept_usage": [
    {"term": "坚持", "meaning": "本文以“择善固执”界定，即选择善并固执持守。", "evidence": "P001", "ambiguity": "未说明与常见用法（持续、不放弃）的关系。"},
    {"term": "择善固执", "meaning": "借用的成语式表述，作为坚持的定义。", "evidence": "P001", "ambiguity": "“善”的判准与判定者未说明。"}
   ],
   "examples_and_targets": [
    "全篇无例子、人物、事件、机构、地点或数据。"
   ],
   "conditions": [
    "无显式条件；“择善”暗含前提——所坚持者须为善，即坚持本身不构成正当性，但正文未展开。",
    "正文仅 5 字符，未说明适用范围、程度或例外情形。"
   ],
   "rhetoric_and_tone": "极简格言体：仅四字成语作答，无解释、无称呼、无论证，以格言代替说明。",
   "unresolved_questions": [
    "“善”的判准由谁依何标准判定，正文未说明。",
    "所坚持者若非善（对恶的固执）是否仍称坚持，正文未说明。",
    "正文仅 5 字符（“择善固执。”），是否为节选、平台截断或版本残缺，语料无 provenance/superseded 字段，无法确认，需人工核对原帖。",
    "提问问“什么是坚持”，回答只给成语，未说明该界定与持续、不放弃等常见含义的关系。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "择善固执。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/品格", "日常概念辨析"],
   "issue_candidates": ["坚持的定义", "坚持与善的关系"],
   "text_function_candidates": ["答疑（回应提问）", "格言式表态"],
   "object_candidates": ["提问者"],
   "working_keywords": ["坚持", "择善固执", "善"]
  },
  "notes": "本篇无图片节点；正文非空但极短（5 字符），已完整读取，故 status=read；是否存在内容残缺/版本截断无法从语料判断，已在 unresolved_questions 登记，建议人工核对原帖。"
 },
 "2dc75fb5": {
  "analysis": {
   "question_context": "提问者（知乎问题）问“善良应该论心还是论迹?”，要求在心/迹之间作选择。作者先给出选择（当然是论心），随即重新规定“心”的内容：不是自认在做好事，而是怀疑自己在做坏事、自知不配。全篇为作者主张，未引述他人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回答：当然是论心。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "限定“心”的含义：不论“人的心里相不相信自己是在做好事”，而论“人的心里是不是怀疑自己在做坏事”。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "描述该心理状态：拿不准自己是不是在做好事，只觉得就算冒做坏事的险也不能不有所作为。", "role": "context"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "父母教子女的类比：不知是否对、是否适合将来的世界，却不能因顾忌有错就什么都不讲。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "判断：在谦卑、保守的状态下讲出来、做出来的，才往往被上天垂怜、成全好的结果。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P006", "P007"], "summary": "界定善良：真正善良的人无时无刻不清醒知道自己不配称为善良；这个“自知不配”才是善良所论的心，而非“一片好意”。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P008"], "summary": "收束：善良的人永远忐忑。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "善良应当论心。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "论心不是论“人的心里相不相信自己是在做好事”，而是论“人的心里是不是怀疑自己在做坏事”。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人其实拿不准自己是不是在做好事，只是觉得就算冒一下可能是在做坏事的险，也不能不有所作为。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在谦卑、保守的状态下讲出来、做出来的，才往往被上天垂怜，成全出一个好的结果。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正善良的人无时无刻不清醒地知道自己不配称为善良；正是这个“自知不配”才是善良所论的心，而不是所谓的“一片好意”。", "evidence": ["E005", "E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "善良的人永远忐忑。", "evidence": ["E007"]}
   ],
   "argument_steps": [
    "先断然给出选择：当然是论心（P001）。",
    "立即限定“心”的所指，排除“相信自己是在做好事”，代之以“怀疑自己在做坏事”（P002）。",
    "描述该状态：不确定是否在做好事，但认定不能不有所作为（P003）。",
    "以父母教子女作类比，说明在不确定中仍须行动（P004）。",
    "给出结果判断：谦卑、保守状态下的言行才往往被上天垂怜、成全好结果（P005）。",
    "界定善良的标志为“无时无刻不清醒知道自己不配称为善良”，并把“自知不配”确立为善良所论的心（P006–P007）。",
    "以“善良的人永远忐忑”收束（P008）。"
   ],
   "concept_usage": [
    {"term": "论心／论迹", "meaning": "评价善良的两种根据；作者取论心，并重新规定“心”的内容。", "evidence": "P001", "ambiguity": "“迹”的一面除被提问者提及外，作者未具体讨论。"},
    {"term": "心", "meaning": "本文指“是否怀疑自己在做坏事”的自我怀疑与“自知不配”，而非自信在做好事。", "evidence": "P002", "ambiguity": "怀疑的程度门槛未界定。"},
    {"term": "善良", "meaning": "以自我怀疑与自知不配为标志的品质；真正善良者不认为自己配称善良。", "evidence": "P006", "ambiguity": "是否排除心安理得的善行，未说明。"},
    {"term": "一片好意", "meaning": "被明确排除在“善良所论的心”之外的说法。", "evidence": "P007", "ambiguity": "作者未说明“好意”与“怀疑自己做坏事”能否并存。"},
    {"term": "谦卑、保守的状态", "meaning": "行动时的自我定位，被认为与好结果相关。", "evidence": "P005", "ambiguity": "如何达成该状态未说明。"},
    {"term": "上天垂怜", "meaning": "结果被成全的说法，带传统/宗教语汇。", "evidence": "P005", "ambiguity": "是否字面宗教主张或修辞，未说明。"}
   ],
   "examples_and_targets": [
    "做父母的教子女：类比材料，说明在不知对错与是否适合将来世界的情况下仍不能什么都不讲（P004，作者类比）。",
    "“人的心里相不相信自己是在做好事”：被作者否定的理解方式（P002，反驳对象）。",
    "“一片好意”：被排除在善良所论的心之外的说法（P007，反驳对象）。",
    "提问者的“论心还是论迹”二选一：提问者设定的框架（P001，提问者说法）。",
    "全篇未出现具体人物、机构、事件或数据。"
   ],
   "conditions": [
    "“就算冒一下可能是在做坏事的险，也不能不有所作为”为行动条件（P003）。",
    "“在这个谦卑、保守的状态下”限定好结果的出现范围（P005）。",
    "“往往被上天垂怜”为频率限定，非必然承诺（P005）。",
    "“无时无刻不”为全称限定，涵盖善良者的一切时刻（P006）。",
    "未给出判定“自知不配”真伪的方法，也未界定“怀疑自己做坏事”的程度门槛。"
   ],
   "rhetoric_and_tone": "短句格言体，第二人称“你”与泛指陈述交替；以“当然”起手作断然回答；父母教子女的日常类比拉近距离；结尾连续两段以“自知不配”“永远忐忑”收束，带训诫与自省色彩；使用“上天垂怜”“一片好意”等传统/口语语汇。",
   "unresolved_questions": [
    "“迹”的一面除提问者提及外，作者未讨论，为何不论迹未展开。",
    "“上天垂怜”是字面宗教主张还是修辞，正文未说明。",
    "“怀疑自己在做坏事”的程度门槛（有怀疑即可，还是须有行动约束）未界定。",
    "“善良的人永远忐忑”是否排除心安理得的善行，正文未说明。",
    "未给出判定“自知不配”真伪的方法，即该标准是否可被伪装。",
    "以父母教子女为类比，未说明该类比在何种范围内成立。",
    "本篇 updated_at（2021-05-25）晚于发布（2020-07-28），语料无 provenance/superseded，版本差异不可考。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "当然是论心。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "而是论“人的心里是不是怀疑自己在做坏事”。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "只是实在觉得“就算冒一下可能是在做坏事的险，也不能不有所作为”。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "在这个谦卑、保守的状态下讲出来、做出来的，才往往被上天垂怜，成全出一个好的结果。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "真正善良的人，无时无刻不清醒的知道自己不配称为善良。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "才是善良所论的心，而不是所谓的“一片好意”。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "善良的人永远忐忑。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P004", "quote": "但实在不能因为顾忌可能有错就什么都不讲。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学（善恶评价）", "道德心理学", "中国传统语汇（论心论迹）"],
   "issue_candidates": ["善良评价标准：心还是迹", "自我怀疑与自知不配", "在不确定中是否应当行动", "好意与善良的区别"],
   "text_function_candidates": ["答疑（回应二选一提问）", "辨析/定义", "训诫/自省劝导"],
   "object_candidates": ["提问者", "读者（第二人称“你”）", "做父母的人", "真正善良的人"],
   "working_keywords": ["论心", "论迹", "善良", "怀疑自己在做坏事", "自知不配", "一片好意", "谦卑", "保守", "上天垂怜", "忐忑"]
  },
  "notes": "本篇无图片节点，无 text/lexical 分歧。P004 的父母教子女为作者类比，非经验证据；“上天垂怜”按作者表述登记，未判定其宗教含义。"
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
