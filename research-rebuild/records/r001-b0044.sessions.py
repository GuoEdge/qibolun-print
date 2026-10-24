# -*- coding: utf-8 -*-
"""批次 r001-b0044 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0044.sessions.py            # 写 out/r001-b0044.out.jsonl
  python3 records/r001-b0044.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0044"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0044.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "1aea8c65": {
  "analysis": {
   "question_context": "提问者（Q001）问“怎样看待美国仇华情绪？”。作者没有直接评价仇华情绪本身，而是把它解读为欧美内部政治危机的产物，并据此提出中国的应对主张：不指望靠表现诚意改变对方决心，应把主战场放在第三世界国家，以产能和对第三世界的援助优先级争取支持，并把“榜样的力量”作为一两代人的持续策略。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "预判欧美近期会有强烈反华宣传，可做工作但不要期其必成；理由是避实捣虚是策略常识。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009"], "summary": "反华宣传与其说针对中国，不如说是在力求自保：疫情已造成欧美内部舆论与制度危机，反制内部“反动思潮”若失败，最轻是执政当局集体下台，最重可能引发对制度本身的second guess；斗争极其残酷，死人过多可能让“红色旅”式组织复活；这是生死存亡问题，不是争面子的问题。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "风潮的根本动能本质上与中国不直接相关，而指向反对党、在野党与内部敌意小团体：名为反中，实为堵政敌、稳朝局；明知中国被冤枉也必须拿中国说事，长期国际关系副作用被先顾眼前压倒。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"], "summary": "转折：这并不意味着中国注定败局，因为主战场不在欧美本土，而在广大的前殖民地国家、第三世界国家。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "中国产能这张王牌对美欧有有效期：若拿捏过火，美欧可能数个月内转产自给；因此援助换筹码须在美欧产能爬坡到位前打出去；美欧清楚对华只有应急依赖，反中政治上更划算，还可唱红白脸。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "这一逻辑对第三世界普遍不成立：以尼日利亚、孟加拉、印度、印尼、菲律宾、巴基斯坦、巴西、埃塞俄比亚的人口规模为例，说明即便美欧产能爬起来也只能勉强满足自身内需，无力供应第三世界防疫物资。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037"], "summary": "第三世界既无替代援助者，其仇华势力也难有足够政治资本长期拒绝中国援助；保守地说至少相当一部分国家做不到铁齿到底，必须谨慎处理与将来唯一有效援助者的关系，甚至有必要尽早、尽快、尽量表达善意以争取援助优先级。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P038", "P039"], "summary": "行动建议：这些国家的领导层和精英阶级现在就应该大批飞往中国寻求庇护，去美英避难更像找死。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P040", "P041", "P042"], "summary": "中国这次疫情真正的舆论、外交主战场不是欧美；对欧美方针是避免和减少声望损害、已预期近期损失不可避免；地球剩下的四五十亿人口、百分之五六十陆地才是真正必胜之所。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "这几十亿人并不关心病毒起源，追究不了谁；但这次故事结局可能不同，并以三句设问提出“想不想有这个不同、怎么实现”；再以外交部编制有限、一边是不可求胜只能守成的阵地、一边是几十亿人口和几千万平方公里的可胜战场作对比。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P050"], "summary": "引用《孙子》知胜有五与“知彼知己，百战不殆”作为策略依据（引文块）。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P051", "P052", "P053", "P054", "P055"], "summary": "回应尼日利亚、肯尼亚等地反华舆论激化：这不改变作者的分析；主张等两个月看局势，反华派拒止中国援助有代价；中国没有必要、估计也没有计划、甚至也没有能力吃下全部第三世界国家，合理推测会把力量集中在让亲华或不太反华的国家得到明显更好的待遇与实际结果。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P056", "P057", "P058", "P059", "P060", "P061"], "summary": "以“榜样的力量是无穷的”为国内治理传统，举当年说服国人放弃公社制度的例子，主张造就“不反华就少死人、早致富、更快现代化”的结果；这是需要一两代人的持续努力，中国在非洲的目标应是二十到四十年内拉开友好国家与敌对国家的现代化程度差距，而不是“广泛支持非洲”。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P062", "P063"], "summary": "结尾指向另一篇知乎回答的链接标题“纳粹为什么那么仇恨犹太人？”，本文未展开其论证。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预期欧美近期会有强烈反华宣传，可以做一些工作，但不要期其必成。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为欧美近期反华宣传与其说是针对中国，不如说是在力求自保，防止自身出现重大政治危机、防止国民对制度的信心动摇。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者判断：若反制欧美内部“反动思潮”失败，最轻后果是执政当局全体引咎下台、政坛地震，最重甚至可能引发对制度本身的second guess。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者强调旨在改换制度的斗争是你死我活、极其残酷的，并让读者自己去查“红色旅”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者设想：若死人太多而责任无法推卸，丧亲者、失业者、破产者足以让“红色旅”式组织复活并孕育各种“xx主义学习小组”。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这不是与中国争夺舆论主动权的小问题，而是涉及数年乃至数十年国家稳定与基本安全的生死存亡问题。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这些风潮的根本动能本质上与中国并不直接相关，而直接指向反对党、在野党以及内部的敌意小团体：名为反中，实为堵政敌、稳朝局。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者分析：如果反中失败，在野党必将执政党钉在耻辱柱上、起码两届任期不能翻身，所以明知中国被冤枉也必须拿中国说事。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国在这次疫情中真正的舆论、外交主战场不是欧美本土，而是广大的前殖民地国家、第三世界国家。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为中国的王牌产能对美欧有有效期：若拿捏过火，美欧痛下决心压低需求并转产，有可能在数个月内实现总体自给自足，因此对美欧的援助筹码有必要在美欧产能爬坡到位之前打出去。", "evidence": ["E11", "E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为上述逻辑对第三世界国家普遍不成立，并以尼日利亚等国的人口规模说明美欧即便产能爬起也只能勉强满足自身内需。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者保守判断至少相当一部分第三世界国家无法铁齿到底，必须谨慎处理与将来唯一有效援助者的关系，甚至有必要尽早、尽快、尽量表达对中国的善意以争取援助优先级。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张这些国家的领导层和精英阶级现在就应该在大批飞往中国寻求庇护之中。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国在疫情中真正的舆论、外交主战场不是欧美；对欧美的方针是避免和减少声望损害，并已预期近期有一些损失不可避免。", "evidence": ["E18", "E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为地球剩下的四五十亿人口、百分之五六十的陆地才是真正必胜之所。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为外交部编制有限，一边是不可求胜、只能守成的阵地，另一边是几十亿人口、几千万平方公里的可胜甚至必胜战场，并以“你觉得中国会怎么选”收束。", "evidence": ["E21"]},
    {"claim_id": "C017", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引用《孙子》关于“知胜有五”与“知彼知己，百战不殆”的原文作为策略依据。", "evidence": ["E22"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为尼日利亚、肯尼亚等地反华舆论大幅激化并没有改变他此前的分析。", "evidence": ["E23"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国没有必要、估计也没有计划、甚至也没有能力吃下全部第三世界国家；合理推测会把力量集中在让选择亲华、甚至只是不太反华的国家得到明显好得多的待遇与实际结果。", "evidence": ["E24", "E25"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以中国信奉“榜样的力量是无穷的”这一国内治理传统为例，主张要造就“不反华就少死人、早致富、更快现代化”的结果；这是足足一两代人的持续努力，中国在非洲的目标应是二十到四十年内让友好国家明显拉开与敌对国家的现代化程度差距，而不是“广泛支持非洲”。", "evidence": ["E26", "E27", "E28"]}
   ],
   "argument_steps": [
    "预判欧美将有强烈反华宣传，可做工作但不要期其必成，理由是避实捣虚（P001-P002）。",
    "把反华宣传解释为欧美自保与内部制度危机所致，而非单纯针对中国（P003-P004）。",
    "强调改换制度之争的残酷性，设想死者过多导致“红色旅”式组织复活（P005-P008）。",
    "对比双方诉求：中国争面子，对方争命，不能指望诚意改变对方决心（P009）。",
    "指出风潮实际指向在野党与内部敌意团体，是堵政敌、稳朝局（P010-P013）。",
    "以反问转折，否定“注定败局”，提出主战场在第三世界（P014-P016）。",
    "论证产能王牌的有效期与美欧的算计（P017-P020）。",
    "以八个人口大国为例，论证第三世界对美欧援助的不可得（P021-P031）。",
    "反问第三世界能否长期拒绝中国援助，判断其必须争取中国援助优先级（P032-P037）。",
    "建议第三世界精英赴华寻求庇护（P038-P039）。",
    "确定主战场与对欧美方针，指出真正必胜之地（P040-P042）。",
    "以三句设问与外交部编制/两块战场的对比推进选择（P043-P049）。",
    "引《孙子》知胜之道为据（P050）。",
    "回应反华舆论激化的现实，提出集中力量于亲华国家（P051-P055）。",
    "以“榜样的力量”与公社到包产到户的先例，给出非洲目标的长期主张（P056-P061）。",
    "以指向另一篇回答的链接作结（P062-P063）。"
   ],
   "concept_usage": [
    {"term": "避实捣虚", "meaning": "作者用作预判与策略的常识依据，指避开实处、击其虚处。", "evidence": "P002", "ambiguity": "作者未展开此处“实/虚”具体所指。"},
    {"term": "产能", "meaning": "作者称为中国的王牌，指防疫物资等的制造能力，其对美欧的效力被限定为有有效期。", "evidence": "P017", "ambiguity": "未给出具体品类或数量；只以“几个月”估计美欧转产时间。"},
    {"term": "主战场", "meaning": "作者指中国舆论与外交应投入的主要方向：不是欧美本土，而是第三世界国家。", "evidence": "P016、P040", "ambiguity": "“主战场”是作者的比喻，未说明与官方口径的关系。"},
    {"term": "前殖民地国家、第三世界国家", "meaning": "作者用来指称其设定的主要争取对象，并以人口规模列举。", "evidence": "P016、P022-P031", "ambiguity": "两词在文中似可互换，作者未给界定标准。"},
    {"term": "榜样的力量是无穷的", "meaning": "作者称这是中国国内治理逻辑的一向传统，主张以造就成功样板来吸引第三世界国家。", "evidence": "P056、P058、P059", "ambiguity": "作者未说明与对外宣传口径的关系。"},
    {"term": "xx主义学习小组", "meaning": "作者设想在欧美社会动荡中孕育的地下小组形态，以“xx”代指。", "evidence": "P007", "ambiguity": "“xx”为占位，具体所指不明。"}
   ],
   "examples_and_targets": [
    "“红色旅”与各种“xx主义学习小组”（作者用以设想欧美内部动荡后果，非作者主张现实已发生）",
    "尼日利亚2.01亿、孟加拉1.7亿、印度13亿、印尼2.8亿、菲律宾1.05亿、巴基斯坦2.07亿、巴西2.1亿、埃塞俄比亚1.1亿（作者论证人口规模与援助缺口的数据，需外部核查）",
    "尼日利亚、肯尼亚等地反华舆论激化（作者引述“很多人说”的现实动向并予回应）",
    "《孙子》“知胜有五”与“知彼知己，百战不殆”引文（引用，非作者原创）",
    "当初说服国人放弃公社制度、让包干到户包产到户的地区多出几个万元户（作者用作类比先例）",
    "《纳粹为什么那么仇恨犹太人？》（文末链接指向的另一篇知乎回答标题，非本文论证内容）"
   ],
   "conditions": [
    "“可以做一些工作，但是不要期其必成”——作者对工作成效的限定。",
    "“如果反制这种内部的‘反动思潮’失败”——后果判断以反制失败为前提。",
    "“如果死人太多而责任也无法推卸”“甚至可能引发”——假设与可能性语气。",
    "“如果反中失败，在野党必将……”——对在野党行为的条件推演。",
    "“如果拿捏过火……是有可能在数个月内解决自身需求实现总体自给自足”——对产能王牌失效的条件与不确定估计。",
    "“在美欧产能爬坡到位之前打出去。再打迟就基本失去意义了”——时间窗口条件。",
    "“保守的说，至少相当一部分第三世界国家做不到”——作者对结论范围的自我限定。",
    "“中国没有必要、估计也没有计划、甚至也没有能力”——多重可能语气，非断言官方决定。",
    "“应该是会把力量集中在……”“合理的推测”——作者标明为推测。",
    "“二十到四十年内”“足足一两代人”——时间尺度条件。"
   ],
   "rhetoric_and_tone": "问答体的时评语气：大量第二人称“你/人家”对举与连续反问（P009、P032-P034、P039、P047、P049、P057）制造逼问感；军事—战争隐喻贯穿（主战场、王牌、必胜之所、守成）；夹用英文“Make no mistake”“second guess”；引《孙子》原文并以“你觉得中国会怎么选？”收束；对第三世界精英用“现在就应该在大批的飞往中国寻求庇护”这类半调侃半训诫的祈使句。",
   "unresolved_questions": [
    "文末 P062-P063 为指向另一篇知乎回答的链接（标题“纳粹为什么那么仇恨犹太人？”），本文未展开该链接的论证；该段为 text-tail 未被 lexical 覆盖的片段。",
    "各国人口数字、美欧“数个月内”转产自给、死亡与失业规模等均为作者断言，需外部核查。",
    "“xx主义学习小组”以“xx”占位，具体所指不明。",
    "“我们”与“中国”在 P041、P043-P048 间切换，作者以“我们要的是面子”发言，其代表主体未明说。",
    "元数据 updated_at 为 2025-03-31，远晚于 published_at 2020-04-08，无法判断正文是否有后改；版本差异待核查。",
    "无图片节点，图片状态 not_applicable。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "可以做一些工作，但是不要期其必成。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "欧美近期的反华宣传与其说是针对中国的，不如说是在力求自保", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "最轻的后果也是执政当局全体引咎下台、政坛地震", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "旨在改换制度的斗争是你死我活、极其残酷的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "足以让“红色旅”这样的组织复活，足以开始孕育各种“xx主义学习小组”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "而是涉及到数年乃至数十年国家稳定和基本安全的生死存亡的问题。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "这些风潮的根本动能本质上与中国并不直接相关", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "名为反中，实为堵政敌、稳朝局。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "明知中国是被冤枉，那也必须要拿中国说事。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "因为主战场根本就不是欧美本土，而是广大的前殖民地国家、第三世界国家。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "中国的王牌——产能——对美欧是有有效期的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "就有必要在美欧产能爬坡到位之前打出去。再打迟就基本失去意义了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "但是，这个逻辑对第三世界国家普遍不成立。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "举个例子，尼日利亚，人口2.01亿，谁有产能能救她？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P036", "quote": "保守的说，至少相当一部分第三世界国家做不到。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P037", "quote": "很有必要尽早、尽快、尽量的表达对中国的善意", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P038", "quote": "这些国家的领导层和精英阶级现在就应该在大批的飞往中国寻求庇护中", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P040", "quote": "中国在这次疫情中真正的舆论、外交预设的主战场就不是欧美。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P041", "quote": "对欧美，方针是避免和减少声望损害", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P042", "quote": "才是真正必胜之所。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P048", "quote": "一边是对方情急咬死的不可求胜、只能守成的阵地", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P050", "quote": "故知勝有五：知可以戰與不可以戰者勝", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P052", "quote": "这并没有改变我这里做的分析。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P054", "quote": "中国没有必要、估计也没有计划、甚至也没有能力吃下全部的第三世界国家。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P055", "quote": "应该是会把力量集中在让选择亲华的国家、甚至选择不太反华的国家的到明显好得多的待遇", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P056", "quote": "中国信奉的是“榜样的力量是无穷的”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P059", "quote": "造就“不反华就少死人、早致富、更快现代化”的结果。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P061", "quote": "应该是在二十到四十年内让友好国家明显的拉开与敌对国家的现代化程度差距", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P062", "quote": "关于现在的仇华浪潮，这个解读更触及本质：", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际政治", "国际关系与外交", "疫情与公共舆论", "中国外交", "非洲与第三世界发展"],
   "issue_candidates": ["美国仇华情绪", "欧美反华宣传的国内动因", "疫情外交与舆论战", "产能依赖与援助优先级", "中非关系目标", "第三世界国家的外交选择"],
   "text_function_candidates": ["时评", "策略分析", "答疑", "论辩"],
   "object_candidates": ["美国", "欧洲", "中国", "尼日利亚", "肯尼亚", "孟加拉", "印度", "印尼", "菲律宾", "巴基斯坦", "巴西", "埃塞俄比亚", "红色旅", "外交部", "在野党"],
   "working_keywords": ["避实捣虚", "反华宣传", "产能", "王牌", "主战场", "前殖民地国家", "第三世界", "榜样的力量是无穷的", "广泛支持非洲", "万元户", "红色旅"]
  },
  "notes": "无图片节点（image status not_applicable）。问答体：Q001 为提问者问“怎样看待美国仇华情绪？”，作者未评价情绪本身而给出策略分析，提问者立场未归给作者。P050 为《孙子》引文块（field=quote），已按 quoted_or_cited/cited_source 记录。P062-P063 为文末指向另一篇知乎回答的链接，标题“纳粹为什么那么仇恨犹太人？”混入正文尾部，属 text_tail_not_in_lexical（lexical 未覆盖片段），已在 unresolved_questions 登记。P041-P048 的“我们/中国”指称主体未明说。各国人口与时间估计需外部核查。"
 },
 "731fe9f8": {
  "analysis": {
   "question_context": "提问者（Q001）问：“觉得教育不好，你可以去当老师，觉得国家不好，你可以去当公务员。这种逻辑对不对？”提问者只提出问题、未表明自己赞成或反对。作者明确回答“当然对啊”，理由是这句原话主张的是【可以】而不是【必须】，并把在这句话下判“不对”“诡辩”的人当作需要警惕的对象加以批评。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "引述被问的句子后直接回答“当然对啊”：它说的是【可以】不是【必须】，并反问哪里逻辑不正确。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "以饿了可以吃鸡腿也可以喝粥作类比：想选喝粥不代表“饿了可以吃鸡腿”是错的；反问这还用得着“谈论”“探讨”吗，难道连基本的语文和逻辑都可以丢掉。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "判断这类表述正确到形同废话，若看不出问题就该检查自己的传感器；告诫读者对写下“不对”“诡辩”判语的人要多加小心，因为这些人解释协议时中文会变得神奇。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017"], "summary": "推论：不尊重语法和形式逻辑的人不能指望他尊重“约法”、不能成就任何事情，会一直失败并把失败归责于别人，把最近、最不能还手、最易被集体盯上的对象送进“核动力失败熔炉”；你以为你是同志，其实只是燃料储备。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "总结：主张“不必自己当教师也可以改善教育”是可以的；但若通过攻击“认为教育不好，可以自己去当教师”来“证明”它，要看做红色警报、跑远点。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "提出并强调原则：错误的方法远比错误的结论致命；选择伙伴不要选结论或方法与你一致的人，而要选遵循正确方法的人，因为方法有客观的正确标准。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031"], "summary": "要求自我审查：判定他人方法不对，是因为不符合基本客观规律，还是仅仅因为与你不同；并反问无视基本语义和逻辑的方法是否会因结论讨喜就变得可行。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035"], "summary": "说明做此审查的收益：决策会引向陷阱更少的人生路线，降低交错朋友、嫁错人、找错老板、雇错下属的几率；并称搞懂这一点起码值一两百万人民币。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这句话当然对，因为它说的是【可以】而没说【必须】，逻辑上没有问题。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者用饿了可以吃鸡腿也可以喝粥的类比说明：一个人想选喝粥且坚决喜欢喝粥，并不意味着“饿了可以吃鸡腿”是错的。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问这种表述是否还需要“谈论”和“探讨”、是否算一个需要谈论的“问题”，并质问难道连基本的语文和逻辑都可以丢掉。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这种表述显而易见无懈可击、正确到形同废话，居然也可以大段论述它如何不对；若读者没有察觉，就该检查自己的传感器、该清灰了。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者告诫：在这个问题下一抬手就写“不对”“诡辩”这种判语的人，如果你觉得他们是你的同志，你最好多加一点小心。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预判这类人在解释与你之间的协议时，嘴里的中文会变得神奇，因为他们生活在一个逻辑与你完全不兼容的奇怪次元空间。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问断言：一个人连语法和基本形式逻辑都不尊重，就不能指望他尊重与你之间的“约法”，也不能指望他能成就任何事情。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者判断这类人会一直失败，其个人史的主题是“谁应该为我这一次的失败负责”，并把最近、最不能还手、最容易被集体盯上的对象送进“核动力失败熔炉”。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言：你以为你是他们的同志，其实你是燃料储备而已。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分两种情形：主张“我认为不必自己当教师也可以改善教育”是可以的、完全没问题的；但若通过攻击“认为教育不好，可以自己去当教师”来“证明”该主张，就要看做红色警报、跑远点。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者强调：错误的方法远比错误的结论致命得多。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张人生必定要选择伙伴：不要选结论和你一致的人，也不要去选方法和你一致的人，而要选择遵循正确的方法的人；并称方法有客观的正确标准可言。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：判定他人的方法是否正确，是因为他们的方法与你不一样、因为他们与你自己不一样才认定他们错吗？并要求下结论前问自己：是因为不符合基本的客观规律，还是仅仅因为与你不同。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：一个无视基本语义和基本逻辑的方法，会因为我赞同或喜欢它在某些问题上的结论就自动变得可行吗？", "evidence": ["E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议做完这个审查再去观察人们是不是在这么做，由此让“要不要离这样的人远一点”的决策引向陷阱更少的人生路线，降低交错朋友、嫁错人、找错老板、雇错下属的几率。", "evidence": ["E25", "E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称搞懂这一点，对你起码值个一两百万人民币。", "evidence": ["E27"]}
   ],
   "argument_steps": [
    "引述被问的句子，直接回答“当然对啊”，理由是【可以】不是【必须】（P001-P003）。",
    "反问哪里逻辑不正确（P004）。",
    "以饿了吃鸡腿/喝粥的类比说明两种选择并存不构成矛盾（P005）。",
    "质问这种表述是否还需要谈论、是否连基本语文和逻辑都可以丢掉（P006-P007）。",
    "判定其为正确到形同废话的表述，转向批评写“不对”“诡辩”判语的人（P008-P011）。",
    "推论：不尊重语法与形式逻辑者不可信、不能成事、必失败并归责他人（P012-P015）。",
    "以“核动力失败熔炉”“燃料储备”讽刺这类人对同志的消耗（P016-P017）。",
    "总结区分：主张“不必自己当教师”可以，但以攻击原句来证明它则是红色警报（P018-P021）。",
    "提出原则：错误的方法远比错误的结论致命（P022-P023）。",
    "给出择友标准：选遵循正确方法的人，方法有客观标准（P024-P026）。",
    "要求自我审查：判定他人方法错误是因其违背客观规律，还是仅因与我不同（P027-P029）。",
    "以连续反问收束（P030-P031）。",
    "说明审查带来的具体收益并以估价收尾（P032-P035）。"
   ],
   "concept_usage": [
    {"term": "【可以】/【必须】", "meaning": "作者用方括号强调原句只主张“可以”，未被主张为“必须”，两者混同是误读的根源。", "evidence": "P003", "ambiguity": "方括号为原文强调标记，强调方式作者未说明。"},
    {"term": "红色警报", "meaning": "作者用来标示一种应远离的行为信号：以攻击一句正确的话来“证明”自己的主张。", "evidence": "P021", "ambiguity": "作者把它用作比喻，未给出判定标准。"},
    {"term": "方法/结论", "meaning": "作者把二者分开，主张错误的方法远比错误的结论致命，方法有客观的正确标准可言。", "evidence": "P023、P024、P026", "ambiguity": "“客观的正确标准”的具体内容与检验方式未说明。"},
    {"term": "逻辑扭曲力场、核动力失败熔炉", "meaning": "作者自造的讽刺性说法，指这类人把失败责任推给最弱者、并把身边人当消耗品。", "evidence": "P016", "ambiguity": "属修辞性命名，非作者定义的概念工具。"},
    {"term": "传感器", "meaning": "作者以“传感器该清灰”比喻读者对明显逻辑错误的判断力出了问题。", "evidence": "P008", "ambiguity": "比喻用法，未说明所指的具体判断能力。"},
    {"term": "ta们", "meaning": "作者用来指称在这句话下写“不对”“诡辩”判语的人。", "evidence": "P010", "ambiguity": "未指明任何具体群体或个人。"}
   ],
   "examples_and_targets": [
    "“觉得教育不好，你可以去当老师，觉得国家不好，你可以去当公务员”（提问者引述、被评论的句子；作者认为它正确）",
    "一个人肚子饿了可以去吃鸡腿，也可以去喝粥（作者类比，用以说明“可以”不排斥别的选择）",
    "在这个问题下写“不对”“诡辩”的人（作者批评与警告的对象，非提问者立场）",
    "“逻辑扭曲力场”“核动力失败熔炉”“燃料储备”（作者讽刺性比喻）",
    "交错朋友、嫁错人（女生们瞪大眼睛！）、找错老板、雇错下属（作者列举的损失场景）",
    "一两百万人民币（作者对收益的夸张估价，非数据）"
   ],
   "conditions": [
    "“如果一个人连语法和基本形式逻辑都不尊重，你难道还能指望……”（P012、P013 的两次条件句）。",
    "“如果你居然没有察觉，你真得要好好检查一下你自己的传感器了”（P008 条件）。",
    "“你如果觉得他们是你的同志，你最好多加一点小心”（P009 条件）。",
    "“如果是有人主张……这是可以的、完全没问题的。但是，看到有人通过攻击……”（P019-P021 的让步加转折条件）。",
    "“会因为我赞同或者喜欢这个方法在某些问题上的结论，这个方法就自动的变成可行的吗？”（P029 反问条件）。",
    "“做完这个审查，然后你再去观察人们是不是在这么做”（P032 前后顺序条件）。"
   ],
   "rhetoric_and_tone": "强烈的训诫、讽刺与警告语气：密集反问（P004、P006、P007、P012、P013、P027-P031）；第二人称“你”直接施压并给出行动命令（“跑远点！”“多加一点小心”）；贬抑性比喻（逻辑扭曲力场、核动力失败熔炉、燃料储备、传感器该清灰）；插入语调侃（“女生们瞪大眼睛！”）；短句独立成段（“会吗？”“能这么干吗？”）；以夸张估价（“起码值个一两百万人民币”）收尾。",
   "unresolved_questions": [
    "作者未举出任何具体人物、文章或事件作为“判语者”的实例，批评对象是泛指的“ta们”，主体不明。",
    "“方法有客观的正确标准可言”未说明该标准是什么、如何判定；“基本的客观规律”亦未展开。",
    "“一两百万人民币”是修辞性估价，文中无计算依据。",
    "提问者本人是否认同该句、为何发问，正文未说明。",
    "元数据 updated_at 为 2025-03-31，晚于 published_at 2020-04-11，无法判断正文是否有后改；版本差异待核查。",
    "无图片节点，图片状态 not_applicable。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "当然对啊。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "你当然【可以】啊，又没说你【必须】。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "难道意味着“饿了可以吃鸡腿”是错的？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "这可以是一个需要谈论的“问题”吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "难道连基本的语文和逻辑都可以丢掉了？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "正确到形同废话一样的表述", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "你最好多加一点小心。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "你会惊讶ta们嘴里的中文是如此神奇", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "你难道还能指望他能尊重和你之间的“约法”？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "你觉得他能成就任何事情吗？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "他们显然会一直失败", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "一切个人历史的主题就是“谁应该为我这一次的失败负责”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "将凑的最近、最不能还手、最容易被ta们集体盯上的对象送进ta们的核动力失败熔炉", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "其实你是燃料储备而已。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "这是可以的、完全没问题的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "看到有人通过攻击“认为教育不好，可以自己去当教师”来试图“证明”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "要看做红色警报，跑远点！", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "错误的方法，远比错误的结论致命得多。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P024", "quote": "不要去选择结论和你一致的人，也不要去选择方法和你一致的人。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P025", "quote": "要选择遵循正确的方法的人。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P026", "quote": "是的，方法有客观的正确标准可言。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P027", "quote": "是因为他们与你自己不一样，所以你才认定他们是错的吗？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P028", "quote": "到底是因为这个方法不符合基本的客观规律，还是这个方法与我不同而已？", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P029", "quote": "这个方法就自动的变成可行的吗？", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P032", "quote": "你的“要不要离这样的人远一点”的决策才会引导你走向陷阱更少的人生路线。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P033", "quote": "这会让你交错朋友、嫁错人（女生们瞪大眼睛！）、找错老板、雇错下属的几率大大的下降。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P034", "quote": "搞懂这一点，对你起码值个一两百万人民币。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言与逻辑", "思维方式", "人际判断与择友"],
   "issue_candidates": ["【可以】与【必须】的混淆", "以攻击正确表述来证明主张", "方法优先于结论", "与不尊重逻辑者交往的风险"],
   "text_function_candidates": ["答疑", "批评", "训诫", "论辩"],
   "object_candidates": ["教师", "公务员", "ta们"],
   "working_keywords": ["【可以】", "【必须】", "诡辩", "红色警报", "错误的方法", "错误的结论", "客观规律", "逻辑扭曲力场", "核动力失败熔炉", "燃料储备"]
  },
  "notes": "无图片节点（image status not_applicable）。问答体：Q001 的句子为提问者所引，作者判定它正确（“当然对啊”），并原样在 P001 重引；作者批评与警告的对象是“在这个问题下一抬手就写‘不对’、‘诡辩’这种判语的人”，不是提问者，未把批评对象当作提问者立场。P016/P017 的“逻辑扭曲力场”“核动力失败熔炉”“燃料储备”为作者讽刺性比喻，非事实断言；P034 的“一两百万人民币”为修辞性估价。"
 },
 "addc8fef": {
  "analysis": {
   "question_context": "提问者（Q001）问：美白宫经济顾问库德洛呼吁美公司撤离中国、美国将支付搬家费，这意味着什么、动机是什么？作者没有分析库德洛的动机，而是论证这种“搬回去”的做法在经济上不可行：企业会把它当成一笔可领的钱，而“宁死也要争口气”的路子中国自己已经用历史经验证明走不通。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以六项条件对照指出搬迁方向：从疫情控制最快、产业链最完善、基础设施最好、能源供应最强大、离统一中心市场最近、政局最稳定的地区，迁往各项都更差的地区，而美方只负责搬家费。", "role": "reason"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "归谬类比：如果这样可行，美国当然愿意为每位非法移民出搬家费请他们回去自己的国家，两者性质完全一样，非法移民问题早就应该不存在了。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "预测企业反应：本来准备破产、散伙的企业突然发现“搬家”的商机，平白多出一笔可领的钱；甚至可能催生“到中国创业、再领搬家费搬回美国”的创意；“属实低碳环保”“且双赢”为反讽。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "引出“很多人”的担心：其他国家因仇恨和敌视而宁可接受更高的成本、更低的产量和更低的利润——宁死也要争口气；作者称没有哪国人民比中国人民更明白这会是什么结果。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "以中国当年“勒紧裤腰带”“宁要xxxx草，不要xxxx苗”为例：大几亿人抱着必死决心勒过、勒出人类历史绝对记录；当年支撑的气（尸山血海的国仇家恨）远超现在支撑“世界人民”的情绪，但也没勒住。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017"], "summary": "讽刺性收束：把“祖传裤腰带”借给对方并喊“加油勒”，再宕开一句“现在油价很便宜”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出搬迁是从疫情控制最快、产业链最完善、基础设施最好、能源供应最强大、离统一中心市场最近、政局最稳定的地区，迁往各项条件都更差的地区，而美方只负责搬家费。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以归谬类比判断：如果这样可行，那么美国当然愿意为每位非法移民出搬家费请他们回去自己的国家，两者性质完全一样，非法移民问题早就应该不存在了。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者判断这只会让本来就已经准备破产的企业突然发现“搬家”的商机，本来准备散伙各回各家，平白多出一笔可以领的钱来。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者设想甚至搞不好会催生出“到中国‘创业’，然后领‘搬家费’‘搬回美国’”的创意。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“属实低碳环保”“且双赢”两句反讽这种做法。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者转述“很多人”的担心：其他国家会因为仇恨和敌视而宁可接受更高的成本、更低的产量和更低的利润——宁死也要争口气（作者随后以中国经验反驳这一路子可行）。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为世界上没有任何国家的人民比中国人民更能明白这事会是什么结果。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者叙述当年中国“勒紧裤腰带”“宁要xxxx草，不要xxxx苗”，大几亿人抱着必死的决心勒过、已勒出人类历史的绝对记录；当年支撑的气是尸山血海的国仇家恨，远超现在支撑“世界人民”的这点情绪，但中国也没勒住。", "evidence": ["E12", "E13", "E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“来，祖传裤腰带借给你，加油勒！”和“现在油价很便宜！”作讽刺性收束。", "evidence": ["E16", "E17"]}
   ],
   "argument_steps": [
    "以六项条件对举，指出搬迁方向是从更优地区迁往更差地区，且只给搬家费（P001-P003）。",
    "以非法移民搬家费作归谬类比（P004）。",
    "预判企业把它当商机，甚至出现“到中国创业再搬回美国”的创意（P005-P007）。",
    "以“属实低碳环保”“且双赢”反讽（P008-P009）。",
    "转入“很多人”的担心：为争口气宁可承受更高成本、更低产量与更低利润（P010）。",
    "指出中国人民最能明白这样做的结果（P011）。",
    "以中国勒紧裤腰带的历史经验说明“争口气”路线最终没勒住（P012-P015）。",
    "以借裤腰带与油价便宜的调侃收尾（P016-P017）。"
   ],
   "concept_usage": [
    {"term": "搬家费", "meaning": "作者指美国承诺为撤离中国的企业支付的搬迁费用，并把它当作企业眼中“可以领的钱”。", "evidence": "P003、P007", "ambiguity": "作者未给出该政策的金额、条件或出处，只围绕“只负责搬家费”作推论。"},
    {"term": "宁死也要争口气", "meaning": "作者转述“很多人”担心的他国心态：为仇恨与敌视宁可接受更高成本、更低产量、更低利润。", "evidence": "P010", "ambiguity": "该说法出自作者转述的担心，不是作者自己的主张。"},
    {"term": "勒紧裤腰带", "meaning": "作者用以指中国当年在极端困难下压缩消费、苦撑工业化的做法，并强调其规模与代价。", "evidence": "P012、P013、P016", "ambiguity": "所指的具体年代与政策作者未逐项说明。"},
    {"term": "“宁要xxxx草，不要xxxx苗”", "meaning": "作者引用的当年口号形式，用以说明“争口气”式选择的极端性。", "evidence": "P012", "ambiguity": "原文以 x 占位，具体字面不明，需外部核查。"},
    {"term": "属实低碳环保、且双赢", "meaning": "作者的反讽用语，讽刺“搬来搬去再领钱”的做法。", "evidence": "P008、P009", "ambiguity": "属修辞，无字面政策含义。"}
   ],
   "examples_and_targets": [
    "库德洛呼吁美公司撤离中国、美国支付搬家费（提问者提供的背景，作者评论的对象；本文未评价其动机）",
    "为每位非法移民出搬家费请其回国（作者归谬类比）",
    "本来准备破产的企业发现“搬家”商机、到中国“创业”再领“搬家费”“搬回美国”（作者设想的企业行为）",
    "中国当年“勒紧裤腰带”“宁要xxxx草，不要xxxx苗”、大几亿人勒过（作者历史例证）",
    "现在油价很便宜（收尾调侃，与论题的关系未说明）"
   ],
   "conditions": [
    "“如果这样可行，那么美国当然愿意为每位非法移民出搬家费……”——反事实假设下的归谬条件。",
    "“甚至搞不好会催生出……”——不确定的推测语气。",
    "“其他国家因为仇恨和敌视而宁可接受更高的成本、更低的产量和更低的利润”——作者转述的他人选择条件。",
    "“当年”支撑中国的那股气“远远的超过现在支撑‘世界人民’的这点情绪”——历史比较所依赖的条件。",
    "“这我们也没勒住”——以自身失败经验限定“争口气”路线的可行性。"
   ],
   "rhetoric_and_tone": "讥讽、轻蔑的短评语气：开篇用两组六项排比对照（P001/P002）先造成荒谬感；以非法移民类比归谬（P004）；反讽短语独立成段（“属实低碳环保。”“且双赢。”）；段末转为对读者的第二人称调侃（“来，祖传裤腰带借给你，加油勒！”）并以“现在油价很便宜！”宕开收束。",
   "unresolved_questions": [
    "P012 口号“宁要xxxx草，不要xxxx苗”以 x 占位，具体字面不明（疑为规避敏感词），需外部核查。",
    "库德洛的原话、美国支付搬家费的具体政策与法律依据，本文未给出来源，需外部核查。",
    "“现在油价很便宜！”与论题的关系未说明，是纯调侃还是另有指向不明。",
    "元数据 updated_at 为 2021-05-16，晚于 published_at 2020-04-12，无法判断正文是否有后改；版本差异待核查。",
    "无图片节点，图片状态 not_applicable。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "从疫情控制最快、产业链最完善、基础设施最好、能源供应最强大、离统一中心市场最近、政局最稳定的地区", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "搬迁去一旦发生疫情就不知道啥时候能控制、产业链不完整、基础设施不太好、能源结构性短缺、远离中心市场、政局不稳定的地区", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "只负责搬家费", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "那么美国当然愿意为每位非法移民出搬家费请他们回去自己的国家", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这只会让本来就已经准备破产的企业突然发现“搬家”的商机。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "平白多出一笔可以领的钱来。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "到中国“创业”，然后领“搬家费”“搬回美国”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "属实低碳环保。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "且双赢。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "宁可接受更高的成本、更低的产量和更低的利润——宁死也要争口气", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "世界上没有任何国家的人民比中国人民更能明白这事会是什么结果。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "当年我们“勒紧裤腰带”，“宁要xxxx草，不要xxxx苗”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "抱着必死的决心勒过了，已经勒出人类历史的绝对记录了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "远远的超过现在支撑“世界人民”的这点情绪。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "这我们也没勒住。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "来，祖传裤腰带借给你，加油勒！", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "现在油价很便宜！", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际经济与产业", "中美关系", "疫情与供应链"],
   "issue_candidates": ["美企撤离中国与搬家费", "产业链回迁的可行性", "为争口气承受更高成本", "中国勒紧裤腰带的历史经验"],
   "text_function_candidates": ["时评", "答疑", "讽刺短评", "论辩"],
   "object_candidates": ["库德洛", "美国", "中国", "非法移民", "在华美企"],
   "working_keywords": ["搬家费", "撤离中国", "产业链", "宁死也要争口气", "勒紧裤腰带", "宁要xxxx草，不要xxxx苗", "双赢", "低碳环保"]
  },
  "notes": "无图片节点（image status not_applicable）。问答体：Q001 中库德洛呼吁与支付搬家费为提问者提供的背景，作者未评价其动机，只论证回迁在经济上不可行。P010“很多人担心……”为作者转述的他人观点并随后反驳，已按 opponent_view + attribution=opponent 记录，未归给作者。P012 口号以 x 占位，属原文形态。"
 },
 "ea7b6f18": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何评价广州恒大俱乐部新建专业足球场的设计？”。正文完全没有提到该足球场或恒大，作者转而论述一种他称为“信力”的能力，主张人做事的格局与“信力”成比例，并劝读者从现在起鄙视自己在任何意义上的“愿赌不服输”。文章与提问对象的具体关联，正文未说明。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "指出一种“惊人的愚蠢”（堪称人类的癌症）：以看病不服诊断自己改方子、请专业司机却教人家开车、点大师手握再自己蘸酱油、请毕加索画完自己提笔“改正”四例说明，并把这种人概括为不能不赌又不能愿赌服输的赌徒。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008"], "summary": "转入正面说理：人做事的格局，和自己的“信力”是成比例的。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "定义“信力”为基于一系列看人、鉴定人的方法而建立起来的一种阻抗内生疑惧的力量；并说明看人鉴定人的技术高度复杂微妙，需要大量实践和练习，下多少力气、摔打多少回才有多强的眼光和定力。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "眼光锐利才能真愿赌服输：知道选择背后是交叉手段鉴定与重重阅历经验支撑，才能压住蠢念、按住贱手、真正得到真实帮助；这样找到的人已是你所能找到的最好的人，其充分独立发挥就是你能得到的最好结果。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "“愿赌服输”的完全为自己选择负责的精神支撑起用人不疑的气度；气度与眼光的结合使人找到对的人、获得本人做不到的更好结果；否则不但得不到高于自己水平的效能，还常常花巨大代价把自己的水平打折表现。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "放大到人类层面：若能少犯这种蠢早就衣食无忧、地上天国；绝大多数人因此入不敷出，明白人的盈余被分食，这种愚蠢如同黑洞吞掉几乎一切利润；若能看破并在正确路上积累功夫的人多一些，即使不作任何技术进步，人类也会总体幸福很多。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020"], "summary": "劝诫与结论：只要真的希望自己有出息，就从现在、此刻开始鄙视自己在任何意义上的“愿赌不服输”；做到了才有资格得到任何意义上的忠诚，而这种忠诚带来的效能是没这个信力的蠢人们做梦也想不到的。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言世界上流传着一种惊人的愚蠢，堪称人类的癌症。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以四个例子说明这种愚蠢：病得不轻去看医生却自己改方子、请了专业司机却教人家开车、去名寿司店点大师手握却自己再蘸酱油、请毕加索画完自己嫌“不好看”提笔“改正”。", "evidence": ["E2", "E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把这种人概括为“一个不能不赌的赌徒，又不能愿赌服输”，称其蠢到令人感到悲哀。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出人生道理：人做事的格局，和自己的“信力”是成比例的。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“信力”：它是基于一系列看人、鉴定人的方法而建立起来的一种阻抗内生疑惧的力量。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为看人、鉴定人的技术本身高度复杂微妙、需要大量的实践和练习；下了几分力气、摔打过多少回，才有多强的眼光和多强的定力。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为因为眼光锐利才能真正的愿赌服输：知道自己的选择背后有交叉手段鉴定与重重叠叠的阅历经验支撑，才能压住蠢念、按住贱手，真正得到真实的帮助。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这样找到的人已经是你能找到的最好的人，这人充分独立发挥的结果就是你能得到的最好的结果。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“愿赌服输”的完全为自己的选择负责的精神，才能支撑起用人不疑的气度；是气度和眼光的结合使你找到对的人、获得你本人做不到的更好的结果。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断否则你不但得不到高于自己水平的效能，还常常是花费巨大代价去把你自己的水平打折表现。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言绝大多数人都因此入不敷出，少部分明白人产生的盈余也为了养活这样的蠢材而被分食；是这种愚蠢如同黑洞一样吞吃掉了几乎一切的利润。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者判断如果能看破这一关键、潜心在正确的路上积累功夫的人多一些，即使不作任何技术进步，人类也会总体幸福很多。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者劝诫：只要你真的希望自己有点出息，就从现在、此刻开始鄙视自己在任何意义上的“愿赌不服输”；做到了才有资格得到任何意义上的忠诚。", "evidence": ["E17", "E18"]}
   ],
   "argument_steps": [
    "点出“惊人的愚蠢”并称其为人类的癌症（P001）。",
    "以四个外行干预内行的例子展开（P002-P005）。",
    "把这种人概括为不能愿赌服输的赌徒（P006）。",
    "提出核心命题：格局与“信力”成比例（P007-P008）。",
    "界定“信力”并说明看人、鉴定人需要大量实践（P009-P010）。",
    "论证眼光是愿赌服输的支撑，由此才能得到真实帮助（P011）。",
    "指出这样找到的人与结果已是最优（P012）。",
    "说明愿赌服输支撑用人不疑，气度加眼光带来超出自身水平的结果（P013）。",
    "对比否则的损失：花大代价把自己的水平打折表现（P014）。",
    "放大到人类层面，称这种愚蠢吞掉几乎一切利润（P015-P017）。",
    "以假设句式指出改善空间（P018）。",
    "以劝诫与结论收束（P019-P020）。"
   ],
   "concept_usage": [
    {"term": "信力", "meaning": "作者自造术语：基于一系列看人、鉴定人的方法而建立起来的一种阻抗内生疑惧的力量；作者称格局与其成比例。", "evidence": "P008、P009、P020", "ambiguity": "文中无量化或可操作的定义，未说明如何衡量。"},
    {"term": "愿赌服输", "meaning": "作者指完全为自己的选择负责、不把后果推给对方的精神，与“愿赌不服输”相对。", "evidence": "P006、P011、P013、P019", "ambiguity": "作者以赌博作喻，未说明与一般“承担风险”用法的区别。"},
    {"term": "用人不疑", "meaning": "作者借用成语指放手用人，并把它解释为“愿赌服输”精神支撑下的气度。", "evidence": "P013", "ambiguity": "作者对成语作了自己的解释，未说明与传统用法是否一致。"},
    {"term": "蠢念、贱手", "meaning": "作者的口语化贬称，指在疑惧驱动下想插手、干预的自身冲动。", "evidence": "P011", "ambiguity": "属训诫性用词，未定义具体行为。"},
    {"term": "格局", "meaning": "作者指人做事的规模与层次，称其与“信力”成比例。", "evidence": "P008", "ambiguity": "“成比例”的关系如何成立、如何衡量，作者未说明。"},
    {"term": "人类的癌症", "meaning": "作者对这种愚蠢的夸张指称，用于强调其普遍危害。", "evidence": "P001", "ambiguity": "修辞用语，非医学或事实判断。"}
   ],
   "examples_and_targets": [
    "看病不服诊断自己改方子、请专业司机却教人家开车、名寿司店点大师手握再蘸酱油、请毕加索画画再自己“改正”（作者并列的类比，未给出具体人物或事件出处）",
    "不能不赌又不能愿赌服输的赌徒（作者概括与训诫的对象）",
    "黑洞（比喻这种愚蠢吞吃利润）",
    "地上天国（作者对人类本可达到状态的夸张设想）",
    "广州恒大俱乐部新建专业足球场（提问对象，正文完全未提及）"
   ],
   "conditions": [
    "“病得不轻，去看医生，医生给了诊断，不服，自己改方子”——条件式场景描述。",
    "“因为你眼光锐利，你才能真正的愿赌服输”“有这个支撑，你才能压住自己的蠢念”——眼光与支撑作为前提条件。",
    "“否则，你不但得不到高于你自己水平的效能……”——反条件后果。",
    "“如果能看破这一关键……即使不作任何技术进步”——假设加让步。",
    "“只要你真的希望自己有点出息”——劝诫所设条件。",
    "“做到了，你才有资格得到任何意义上的忠诚”——结果以做到为前提。"
   ],
   "rhetoric_and_tone": "格言体训诫：开篇用四个“外行干预内行”的短例排比讽刺，随后转为正面说理并以自造术语“信力”命名；全篇以第二人称“你”直接对读者说话；用“蠢念”“贱手”“蠢材”等贬词加强训诫力度；用“癌症”“黑洞”“地上天国”等宏阔比喻拉高论断；结尾以“从现在、此刻，开始鄙视自己”的命令式短句收束。",
   "unresolved_questions": [
    "正文完全未提及提问对象“广州恒大俱乐部新建专业足球场”，也未说明与该问题的关联，提问与正文的对应关系无法从本文确定。",
    "“信力”为作者自造术语，未给出可操作定义或衡量方法；“看人、鉴定人的方法”也未具体列举。",
    "四个例子均无具体人物、时间或出处（“名寿司店”“大师”所指不明）。",
    "“人做事的格局，和自己的‘信力’是成比例的”中“成比例”的含义未说明。",
    "元数据 updated_at 为 2023-08-16，晚于 published_at 2020-04-17，无法判断正文是否有后改；版本差异待核查。",
    "无图片节点，图片状态 not_applicable。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "世界上流传着一种惊人的愚蠢，堪称人类的癌症。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "病得不轻，去看医生，医生给了诊断，不服，自己改方子。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "请个专业司机，坐副驾驶，教人家怎么开车。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "去名寿司店，点大师的手握，自己再蘸酱油。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "请毕加索画，画完了自己嫌“不好看”，提笔“改正”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "一个不能不赌的赌徒，又不能愿赌服输，真的是蠢到令人感到悲哀。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "那就是人做事的格局，和自己的“信力”是成比例的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "是基于一系列看人、鉴定人的方法而建立起来的一种阻抗内生疑惧的力量。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "你下了几分力气、摔打过多少回，你才能有多强的眼光和多强的定力。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "你才能压住自己的蠢念、按住自己的贱手，真正的得到真实的帮助。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "就是你能得到的最好的结果。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "才能支撑起用人不疑的气度。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "还常常是花费巨大代价去把你自己的水平打折表现。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "绝大多数人都因此入不敷出", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "如同黑洞一样吞吃掉了几乎一切的利润。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "即使不作任何技术进步，人类也会总体幸福很多。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "开始鄙视自己在任何意义上的“愿赌不服输”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "你才有资格得到任何意义上的忠诚。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲理", "识人与用人", "决策与责任"],
   "issue_candidates": ["愿赌不服输", "外行干预内行", "看人鉴人的能力", "用人不疑的代价", "信力与格局"],
   "text_function_candidates": ["答疑", "训诫", "格言式说理"],
   "object_candidates": ["医生", "专业司机", "名寿司店与大师", "毕加索", "赌徒"],
   "working_keywords": ["信力", "愿赌服输", "愿赌不服输", "用人不疑", "格局", "看人", "鉴定人", "蠢念", "贱手", "人类的癌症"]
  },
  "notes": "无图片节点（image status not_applicable）。问答体但与提问对象脱节：Q001 问恒大足球场设计，正文全篇未涉及足球场或恒大，已按文章实际内容记录并在 unresolved_questions 登记该缺口，未据标题或提问补写正文。“信力”“愿赌服输”“用人不疑”均只记录本文用法，不作跨文章统一。"
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
