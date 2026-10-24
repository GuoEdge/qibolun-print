# -*- coding: utf-8 -*-
"""批次 r001-b0161 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0161.sessions.py            # 写 out/r001-b0161.out.jsonl
  python3 records/r001-b0161.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0161"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0161.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e1e6c6a3": {
  "analysis": {
   "question_context": "提问者问“中国的侠义精神是否还能延续下去？”。正文没有回应“中国”或“能否延续”，而是针对“很多人对行侠仗义极其过敏、认为这是鼓动人去送死”的顾虑，论证个人为什么必须行侠、以及具体怎么做。提问者立场不计入作者主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "摆出语境：一提行侠仗义就被联想到鼓动人送死，作者称之为社会悲哀；其隐含假设是可以缩着头苟活一生。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "质疑该假设：侠义不是可以避开不要的东西；判断一件事要看“不做”的成本风险；勇敢的本质是不勇敢死得更快更惨。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "理由一：没有侠骨会招来更多试探与凌辱，因为明哲保身者可预料、可管控；非侠的风险由不得自己选。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "理由二：只保自己命的人没有人愿保，故孤立无援；一身慷慨豪侠之气反而让敌人心生敬畏、不敢贸然试探。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "理由三：侠是政治斗争艺术与军事战斗能力，只能在战斗中学；这些事无孔不入、躲无可躲，须从可承受的风险开始积累。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052"], "summary": "第三点（编号与前重复）：择偶、择业两大关口要求侠气罡气；担不起风险的人被视为指望不上，资产也以敢于动用为前提。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061"], "summary": "小结与反驳：侠的危险可选，非侠的危险逃无可逃，是敬酒不吃吃罚酒；嫌这套答案不现实、魔怔的人是因为已决心不做。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P062", "P063", "P064", "P065", "P066"], "summary": "行动建议一：见不平不公至少要考虑有什么可做的；这份考虑本身就是行侠仗义的一部分。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081"], "summary": "行动建议二：以想不到足够安全的帮助手段为耻；举鸣笛、报警、叫人、递绳杆、匿名捐助等；首先归为处事能力缺陷，且这些手段是将来自己遇险时说服旁人的预案。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091"], "summary": "行动建议三：以无所作为为耻，并给出两种合法方式——做了则以不能做得更多为耻，不做则接受痛苦、不讲“道德绑架”这类话。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100", "P101"], "summary": "结论：他人对你有期望时相当宽厚，可原谅想不到办法或缺勇气，但不能容忍既什么也不做又要逃掉惭愧与羞耻。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人对“行侠仗义”极其过敏，一提就联想到鼓动人去送死，作者称之为社会悲哀。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "侠义精神说到底不是一种可以选择避开不要的东西。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一件事要不要做，不能只看做它的成本和风险，还要看不做的成本和风险；若后者超过前者，前者无论多大也必须做。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "勇敢的本质不是无意义的勇猛和赌气，而是不勇敢比勇敢死得更快更惨，由不得你不勇敢。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有侠骨的人会因缺少不可冒犯的刚强之气而招来更多试探甚至凌辱，这种气质招来的风险不比一身侠气带来的危险小。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有侠气者该冒什么危险可以自选；没有这身罡气，自动找上门的风险由不得你选也由不得你逃，极为被动。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只顾保自己命的人，别人没有理由保他，于是会孤立无援。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "侠不只是侠骨与浪漫想象，还是一种政治斗争艺术和必须靠硬功夫支撑的军事战斗能力，而这种能力只能在战斗中学习。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类事无孔不入地存在于全部生存空间（办公室、供应商、客户、小区），躲无可躲、逃无可逃。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "择偶与择业两大人生关口对侠气罡气有残酷要求，一心想逃者必栽跟头；担不起风险的人不被看好。", "evidence": ["E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "侠有危险但是可选的危险，非侠同样有危险且逃无可逃；这是敬酒不吃吃罚酒、非喝不可的一杯。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "认为这套答案“不现实”“没必要”“太理想”甚至“魔怔”的人，是因为已做定了不做的决定。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "行侠仗义的第一步是：凡见不平不公，无论做多做少，至少要考虑有什么可做的，即使考虑后决定什么也不做。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想不到任何既可使力又够安全的办法，首先不是正义感缺失，而是处事能力上的缺陷，应为自己的智商和对世界了解的匮乏感到耻辱。", "evidence": ["E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你今天能想到的对弱者足够安全的帮助手段，都是将来自己遇险时说服害怕风险的旁人的预案。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以无所作为为耻有两种合法方式：做了则以不能做得更多为耻；什么也不做则接受痛苦，而不讲“道德绑架”这类话。", "evidence": ["E24", "E25"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他人可以接受你因想不到办法或缺勇气而什么也不做，但不容忍你什么也没做还要连惭愧和羞耻都逃干净。", "evidence": ["E26", "E27"]}
   ],
   "argument_steps": [
    "先立语境：一提行侠仗义就被当成鼓动人送死，作者断言这是社会悲哀。",
    "指出反对者的隐含前提是“很大概率可以缩着头苟活一生”，并直接质疑该前提。",
    "提出成本比较原则：要同时计算做与不做的成本风险，后者更大则必须做。",
    "由此重新定义勇敢：不是勇猛赌气，而是不勇敢死得更快更惨。",
    "列三条理由：招人凌辱、孤立无援、事到临头没有技术。",
    "补充第三点：择偶与择业对侠气罡气的要求（序号与前文重复）。",
    "用“敬酒不吃吃罚酒”收束：两种危险必选其一，并预设反对者“不现实/魔怔”的反应予以反驳。",
    "给出行动要求三条：至少要考虑；以想不到安全手段为耻；以无所作为为耻。",
    "结论：他人能原谅能力或勇气不足，但不原谅既不做又要逃掉羞耻。"
   ],
   "concept_usage": [
    {"term": "侠/侠义精神", "meaning": "本文指一套兼含刚强之气、政治斗争艺术与军事战斗能力的实践品质，而非单纯道德意愿或浪漫想象。", "evidence": "P025", "ambiguity": "既说“不是可以避开不要的东西”，又说侠有风险，二者关系未展开。"},
    {"term": "罡气/先天罡气", "meaning": "与侠骨并列的一种不可冒犯的刚强气质，作者用“先天”修饰。", "evidence": "P012", "ambiguity": "与“侠气”是否同义未说明，文中交替使用。"},
    {"term": "明哲保身", "meaning": "作者笔下指绝对现实、绝不冒险的缩头态度，带有贬义并加引号。", "evidence": "P010", "ambiguity": "作者将其等同于“公开喊老实点免得惹事”的人。"},
    {"term": "敬酒不吃吃罚酒", "meaning": "借俗语表达可选危险与逃无可逃的危险之间的二选一。", "evidence": "P054", "ambiguity": "无。"},
    {"term": "行侠仗义", "meaning": "被作者具体化为“至少考虑有什么可做的”“以想不到安全手段为耻”“以无所作为为耻”三条可操作要求。", "evidence": "P062", "ambiguity": "未给出可做之事的下限标准。"}
   ],
   "examples_and_targets": [
    "“小孩听信了出去勇斗流氓英勇就义”的想象画面——作者反驳对象（P001）。",
    "北极熊与电击枪——作者类比，说明孤家寡人再强也会被针对（P017）。",
    "扫地僧——作者借用小说人物作类比，说明敌人无法用调查确定你是否孤立无援（P019）。",
    "“卖了店去跪求柯里昂教父”——作者引用《教父》意象，反问平时不积累侠气者的出路（P038）。",
    "择偶与择业——作者举的两大人生关口（P041、P049）。",
    "“晚上送女性回家的勇气”——作者用以判断对方风险应对经验（P051）。",
    "骑自行车与赤脚走路的对比——作者类比，说明不做此决定者自然觉得这些答案不现实（P057）。",
    "鸣笛示警、隔着街区报警、跑去叫人、找绳子长杆、匿名捐助——作者给出的安全帮助手段（P070）。"
   ],
   "conditions": [
    "反对者立场依赖的前提是“很大概率人可以缩着头苟活一生”，作者认为该前提需要检验（P003）。",
    "成本比较原则带条件：如果“不做”的成本风险超过“做”的成本风险，则无论后者多大都必须做（P006-P007）。",
    "行动建议带减免条件：没人要求你随时随地拿命搏，也不一定要求你具体做什么事（P064）。",
    "不得以环境或条件不佳为由跳过考虑：可以先考虑再决定什么也不做，但不能直接跳到“我什么也不能做”（P065）。",
    "安全帮助手段的前提取自“你不想卷入麻烦”“高度注意保护自身”等自保条件（P068-P069）。",
    "宽容条件：他人能接受你因想不到办法或缺勇气而不做，但不能接受你逃避惭愧羞耻（P094-P095）。"
   ],
   "rhetoric_and_tone": "训诫式第二人称说理，大量反问与连续追问（“你就想着时候掏出来就顶用？”“天下哪来这么便宜的事？”），口语与俗语并用，比喻密集（敬酒罚酒、骑自行车、北极熊与电击枪、自造偶像式的托付），并直接贬斥反对者（“蠢事”“混账话”“魔怔”）。结构上先破对方前提，再列理由，最后给行动条款。",
   "unresolved_questions": [
    "提问者所问“中国的侠义精神是否还能延续下去”未在正文中正面回答，正文转为个人是否必须行侠及如何行侠。",
    "P039“3）人生的关键事务……”与P023“3）事到临头发现没有技术”同为第3条，序号重复，可能为原文笔误或分段缺失。",
    "“侠骨”“侠气”“罡气”“先天罡气”几个词的界限在文中未说明。",
    "“见义勇为的策略就显得非常的不安全”一段（P003）是对他人看法的转述，其具体指涉对象不明。",
    "更新时间（2023-08-31）晚于发布时间（2021-09-15），版本差异与改动范围未说明。",
    "正文未提供任何数据或外部材料支撑“这种气质招来的风险绝对不比……小”的比较判断，属作者断言。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我发现很多人对“行侠仗义”极其过敏", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "侠义精神说到底不是一种你可以选择避开不要的东西", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "绝不能只看做它的成本和风险，还要看不做它的成本和风险", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "如果后者超过前者，则前者无论有多大，你也必须要做", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "不勇敢比勇敢死得更快更惨，由不得你不勇敢", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "一个人若没有侠骨，会因为缺那一股不能冒犯的刚强之气招来更多的试探甚至凌辱", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "这种气质本身会招来的风险绝对不比有一身侠气所带来的危险小", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "没有这身先天罡气，自动找上门来的风险可由不得你选，也由不得你逃", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "只保自己命的人，别人哪里找不到，又有什么必要要来保你？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P025", "quote": "它同样是一种牢固站稳正义立场、促使路人不由自主成为盟友的政治斗争艺术", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P026", "quote": "这种能力只能在战斗中学习", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P028", "quote": "因为这些事会无孔不入的、无远弗届的存在于你所有的生存空间", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P029", "quote": "你躲无可躲，逃无可逃", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P040", "quote": "一心想逃，几大人生关口你必栽跟头", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P042", "quote": "对身无英气和刚性、一份风险担不起的缩头党绝无好感", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P053", "quote": "侠有危险，那是你可以选的危险；非侠同样有危险，是逃无可逃的危险", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P054", "quote": "这一杯你是非喝不可的", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P055", "quote": "没做这决心的人看这些东西永远会是“不现实”、“没必要”、“太理想”", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P063", "quote": "凡见不平、不公，无论你做多做少，至少你要考虑一下有什么可做的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P065", "quote": "你可以考虑之后决定什么也不做", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P071", "quote": "而首先是处事能力上的缺陷", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P077", "quote": "而是你该为你的智商、为你对世界的了解的匮乏感到耻辱", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P072", "quote": "其实都是将来你自己遇险时，你可以用来说服那些有意帮你但却害怕风险的旁人的预案", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P088", "quote": "两种方式都是合法的以无所作为为耻", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P090", "quote": "不想办法去说“觉得我必须做点什么的人全是道德绑架我”这种混账话", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P094", "quote": "ta们完全可以接受你因为想不到办法、于是什么也不做", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P095", "quote": "想要连那点惭愧和羞耻都逃得一干二净", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理与道德实践", "社会心理与风险判断", "处世策略"],
   "issue_candidates": ["侠义精神的当代必要性", "见义勇为的风险与成本", "明哲保身与孤立无援", "道德绑架与羞耻感"],
   "text_function_candidates": ["论辩", "答疑", "训诫式劝导", "经验总结"],
   "object_candidates": ["行侠仗义者", "明哲保身者", "凌辱者与试探者", "柯里昂教父（引用）", "扫地僧（引用）"],
   "working_keywords": ["侠义精神", "侠骨", "罡气", "明哲保身", "敬酒不吃吃罚酒", "道德绑架", "风险"]
  },
  "notes": "本篇无图片节点。正文未回答提问中的“中国”与“能否延续”，属答非所问式转向，已在 question_context 与 unresolved_questions 记录。P039 序号与前文重复，为原文可见的编号问题。brief 与P001-P003高度重复。"
 },
 "216d13e6": {
  "analysis": {
   "question_context": "提问者问“插队到底是不是没有公德心的行为？”。正文不作是非表态，直接给出两种“合理插队”的操作办法，并把结论落在“不要简单认定某种行为本身就是不道德的，主要要看你怎么做”。提问者的“公德心”框架属提问者，正文未使用该词。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "方法一：从队尾开始逐个询问能否排在ta前面，直到第一个拒绝者之后。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "该办法的道理：逐个问显得尊重规则且确有急迫性，可用车票机票佐证；后面的人同意后有惯性效应。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "方法二：出钱从前往后问，用报酬换位置，直到有人答应；作者称这同样不损害其他排队者利益。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013", "P014"], "summary": "操作细节：不要问正在办理的人；按被耽误时间乘以平均工资四到八倍估算对价；被拒绝不得怨恨，仍要道歉、受责备要低头受教。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "经验预期：做得够诚意，可能问不到几个就有人免费让位，人们的慷慨会出乎意料。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "结论：很多事情都有可做之法，不要简单认定某种行为本身不道德，主要看你怎么做；看得懂的人自由更大。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "插队有两种可合理操作的办法，其一为从队尾逐一征询同意，直到第一个拒绝者之后。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "一般来说，肯一个个询问会让所有人知道你是尊重规则的，而且你是真的很急，并可出示车票机票证明急迫程度。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出钱换位置的做法同样没有损害其他排队者的利益，没有人有反对的必要。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要询问正在办理的那一位，因为那会拖延所有人的时间，最好从第二位、第三位开始问起。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对价要按估算耽误别人的时间，乘以平均工资的四倍到八倍再取整。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被拒绝不能有丝毫怨恨；人家即使肯收钱也一样欠人家情，要道歉，对方责备你也要低头受教。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "很多事情都有可做之法，不要简单认定某种行为本身就是不道德的，主要要看你怎么做；看得懂的人会有大得多的自由。", "evidence": ["E7", "E8"]}
   ],
   "argument_steps": [
    "先不判断插队是否缺德，直接给出两条可执行路径。",
    "为路径一给出理由：逐一征询＝尊重规则＋急迫性可证，且后面的人同意会形成惯性。",
    "为路径二给出理由：付费换位不损害其他排队者利益。",
    "补充操作细节：不问正在办理者、按时间成本估对价、被拒绝不得怨恨且须道歉。",
    "以“可能有人免费让位”作为正向经验预期。",
    "收束为一般原则：行为是否道德取决于怎么做，而不是行为本身。"
   ],
   "concept_usage": [
    {"term": "合理插队", "meaning": "通过逐一征得同意或支付对价换取位置，使插队不再被作者视为损害他人。", "evidence": "P001", "ambiguity": "作者未给出“合理”的判定标准，也未讨论无人同意时的情形。"},
    {"term": "对价", "meaning": "按他人被耽误的时间和平均工资的四到八倍折算出的报酬。", "evidence": "P011", "ambiguity": "四到八倍的依据未说明。"},
    {"term": "公德心", "meaning": "仅出现在提问者的问题中，正文未使用该词，也未回答是或否。", "evidence": "P018", "ambiguity": "提问概念与正文结论之间无显式对接。"}
   ],
   "examples_and_targets": [
    "车票机票——作者建议用来证明急迫性的材料（P003）。",
    "工资折算示例：一万块每个月，10000/22/8/60*4 = 3.8元一分钟，耽误15分钟约60-120块——作者给出的算账例（P011、P012）。",
    "排队现场的其他排队者与正在办理的那一位——作者设定为需要被尊重和补偿的对象（P007、P009）。"
   ],
   "conditions": [
    "需要能证明具体的急迫性（如车票机票）（P003）。",
    "对价估算以“按照一万块每个月”为示例基准，四到八倍为给出的区间（P011）。",
    "付费换位须“直到有一位答应你为止”，未答应则不能强换（P006）。",
    "被拒绝后不得有丝毫怨恨，且须道歉与受教（P014）。",
    "结论以“一般来说”“很可能”“不信你试试看”等限定语给出，未声称必然如此（P003、P015、P020）。"
   ],
   "rhetoric_and_tone": "操作手册式第二人称指导，条目化编号，语气平实带劝诱；用具体算账（3.8元一分钟、60-120块）增强可操作性；结尾用“不信你试试看”作轻松邀请。",
   "unresolved_questions": [
    "提问所问“插队到底是不是没有公德心的行为”未获直接回答，正文以“怎么做”替换“是不是”的问题。",
    "“平均工资的四倍到八倍”这一倍数的来源与依据，正文未说明。",
    "若队列中无人同意（或多数人拒绝），作者未说明该怎么办。",
    "brief 与正文前两段基本重合，疑为正文摘录，不作独立证据。",
    "发布时间2021-09-15、更新时间2025-09-22，跨四年，版本差异与改动范围未说明。",
    "正文未出现“公德心”一词，平台话题标签亦未出现在正文中。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "从队尾开始一个一个的问能不能排在ta前面，直到你到达第一个拒绝的人后面", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "所有人都会知道你是尊重规则的，而且你是真的很急", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "这样同样没有损害其他排队者的利益，没有人有反对的必要", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "不要询问正在办理的那一位，因为那会拖延所有人的时间", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "估算可能要花去的别人的时间，乘以平均工资的四倍到八倍再取整", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P014", "quote": "被拒绝你不能有丝毫的怨恨", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P018", "quote": "不要简单的认定某种行为本身就是不道德的，主要要看你怎么做", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P019", "quote": "看得懂的人会有大得多的自由", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["日常伦理", "社会规则与公共秩序", "谈判与交易"],
   "issue_candidates": ["插队是否缺德", "规则内的例外操作", "时间成本的定价", "对他人同意的征询"],
   "text_function_candidates": ["答疑", "操作指南", "经验总结"],
   "object_candidates": ["排队者", "插队者", "正在办理业务的人"],
   "working_keywords": ["插队", "公德心", "对价", "报酬换位", "排队"]
  },
  "notes": "本篇无图片节点。正文未直接回答提问者的“是否没有公德心”，而是给出替代性操作方案，已在 question_context 与 unresolved_questions 记录。brief 为正文前段的节选式重复。"
 },
 "0ccda9c2": {
  "analysis": {
   "question_context": "提问者问“相爱的人会相互隐瞒过去吗？”。作者反转问题：相爱的人根本不问过去，用不着对方再隐瞒；并把“倒查一生”的做法作为主要批评对象，主张把亲密关系当作可随时终止的、每天两清的小额交易来经营。提问者的问题框架不计入作者主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "立论：相爱的人根本不问过去；作者自述给出优待只基于现在的观察与判断，与对方的过去和现在如何无关。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "反驳“我要献出一生所以要倒查你的一生”：现代亲密关系没有“永远不能分手/离婚”这一条，你随时可以拉闸且无需理由。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "类比定性：这是长期重复的临时小额交易而非一次性巨型交易，如同每天在门口超市买水；应把关系变成这种模式，不要“以身相许”模式。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "“以身相许”模式的致命问题一：凭什么要求对方先交出全部隐私给一个“挑货”的人；并比作“给我五百帮我解冻账户，我给你五百万”的诈骗套路。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028"], "summary": "问题二：问到了也无法确知是否真实与完整；敢于全部坦承的恰是真爱者，会造假的人只说一半，于是这个测试专门淘汰真爱人。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034"], "summary": "两个原因：前现代思维惯性；贪图“彻底托付”与“彻底控制”的快感；而完全托付是自造偶像，没有人能一生守得住这种完美要求。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044"], "summary": "成本与稳定性论证：洗衣做饭等已相互抵消，隐私监控是单独的负担；这种双向高契约成本关系数学上高度不稳定，真正稳固的是“不查户口、每天两清”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054"], "summary": "批控制狂：什么都问、要批准和纠正，结果是安全感虚假、净提高门槛、净提高生活成本、净损失生活体验，宣布停止做这种蠢事。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P055", "P056", "P057", "P058", "P059", "P060", "P061"], "summary": "替代方案问答：怕有病就戴套、要体检报告；欠钱与你无关，强化用印签章程序；至于通缉犯则不必问。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071"], "summary": "主张“不知情”本身有保护作用；安全措施不论问不问都应全备；以爱为名要你放下戒心者应取消资格；作者自述接受对方保持一切怀疑和戒备。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079"], "summary": "银行与VIP客户类比：应介绍准备金制度与存款再保险，而不是交出账目让客户查实力；也不能让VIP不经安检直闯金库，因为本行首先要能存在。", "role": "example"},
    {"unit_id": "U012", "paragraph_refs": ["P080", "P081", "P082", "P083"], "summary": "结论：传统婚恋观在数学上荒谬、实践成绩惨不忍睹；“知道一切”的做法二十岁成功率低、三四十岁崩溃可能大，综合而言是最坏选择。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P084", "P085", "P086", "P087"], "summary": "回应质疑：“现实中分不开”正因你一开始就采用分不开的相处方式，属循环论证。", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096"], "summary": "反驳“血肉相连、水乳交融”：若它只是拆不开的铁棺材就与爱无关；不给对方离去设障碍，才能确信ta留下完全是因为爱。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "相爱的人根本不问过去，用不着对方再“隐瞒”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自述：给别人优待只基于现在的观察与判断，与对方以前如何伟大、家庭如何了不起或曾如何犯错无关，也与对方现在如何没有关系。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代亲密关系并没有“嫁鸡随鸡嫁狗随狗，永远不能分手/离婚”这一条，你手里随时握着闸门、随时可以拉闸且无需理由。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果要论交易性质，现代亲密关系是长期重复的临时小额交易，而不是一次性的巨型交易。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应把关系变成每天买水那种模式，而不要搞“以身相许”模式，后者害人害己。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当一个人开始这样问，孔夫子、关老爷都过不了这一关，一定会问到某种污点和缺憾；真没有污点又要嫌人太老实、没胆魄。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敢于向你坦承可能导致你放弃的一切事实的人，恰恰是真爱你而奋不顾身的人；只爱自己不在乎你上不上当的人则话只说一半。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种追问的唯一效果是淘汰真爱你的人，是一个无法淘汰伪装者、专门为难真爱人的特殊测试。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样做的两个原因：前现代的思维惯性在无脑重复传统；以及贪图“彻底托付”和“彻底控制”的快感。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“毫无保留的托付”本来就不是人类可以承受的东西，谁受了，将来必然成为“可耻的欺骗者”。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "洗衣做饭、端茶倒水等双方各做一份已经抵消；从年报到日报的隐私监控是另一份单独负担，需要额外的价值来补偿。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者不绝对断言该做法行不通，但认为这种“双向高契约成本关系”数学上是高度不稳定的。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "控制狂式追问最后没有收益：安全感是虚假的、净提高达成关系的门槛、净提高生活成本、净损失生活体验，一无是处。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们只想到问清楚对自己的好处，大大忽略了“不知情”对自己的保护作用。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自述立场：我爱你的第一表现，就是接受你对我保持一切怀疑、保持一切戒备，不会称之为敌意。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若对方以爱为名无法接受一视同仁的安全体系、要靠挖掘全部隐私来满足安全感，那ta既不知道爱是什么，也承受不起爱的实际重量。", "evidence": ["E22", "E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "传统所谓“婚恋观”在此问题上充满数学上显而易见的荒谬性；用“知道一切”的做法二十岁建立关系成功率甚低，三四十岁关系崩溃可能性极大，综合而言是最坏的选择。", "evidence": ["E24", "E25"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“现实中不可能想分开就能分开”的辩解属循环论证：你先自己做成分不开，再说“说分就分”不现实。", "evidence": ["E26", "E27"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要给对方的离去设立任何障碍，这样你才能确信对方没有离去完全是因为爱；ta还在就是真爱。", "evidence": ["E28"]}
   ],
   "argument_steps": [
    "先反转提问：不是隐瞒问题，而是根本不该问。",
    "以自身做法（只按现在的观察判断给优待）作为立论示范。",
    "拆解对方逻辑：献出一生所以要倒查一生；指出前提不存在——关系可随时终止。",
    "用超市买水类比，把关系重新定性为长期重复的临时小额交易。",
    "列举“以身相许”模式的问题：索取全部隐私、以诈骗式承诺换信任。",
    "进一步指出追问无法验证真伪，反而专门淘汰真爱者。",
    "给出如此做的两个动机：前现代惯性、贪图彻底托付与控制的快感。",
    "从成本与稳定性继续反驳：隐私监控是净负担，双向高契约成本关系不稳定。",
    "指出控制狂做法的四项净损失，宣布一无是处。",
    "给出替代方案：戴套与体检报告、用印签章程序，而非追问。",
    "提出“不知情”的保护作用，并确立以安全体系为先的相处原则。",
    "用银行与VIP客户类比说明安全程序不可让位。",
    "以传统婚恋观的数学荒谬与实践惨败作结论。",
    "回应“分不开”的质疑为循环论证。",
    "反驳“血肉相连”，落到不设离去障碍才能确证爱。"
   ],
   "concept_usage": [
    {"term": "以身相许模式", "meaning": "作者指以一次性彻底托付、不可退出为前提的亲密关系形态，被判定为害人害己。", "evidence": "P013", "ambiguity": "作者以“长期重复的临时小额交易”作对立面，未给出居中形态。"},
    {"term": "双向高契约成本关系", "meaning": "双方都要交出大量隐私与接受监控的关系，作者称其在数学上高度不稳定。", "evidence": "P039", "ambiguity": "“数学上”为修辞用法，文中未给出任何模型或数据。"},
    {"term": "不知情", "meaning": "作者主张对对方某些信息的不知道本身构成对自己的保护（如对方是通缉犯的例子）。", "evidence": "P062", "ambiguity": "与作者同时主张的“安全措施应全备”之间的边界未明确。"},
    {"term": "准备金制度/存款再保险", "meaning": "银行类比中用来回应客户查账要求的专业制度性保障，代替交出账目。", "evidence": "P075", "ambiguity": "类比映射到亲密关系中的对应物未说明。"},
    {"term": "真爱/真正的爱", "meaning": "在可随时离开而不离开的条件下仍然留下的关系。", "evidence": "P094", "ambiguity": "未给出可操作判据，只给出必要条件。"}
   ],
   "examples_and_targets": [
    "孔夫子、关老爷——作者借中国文化人物作夸张例，说明再完美的人也过不了盘问这关（P018）。",
    "门口超市买水、每天给老板三块钱——作者的核心类比（P011、P012）。",
    "“给我五百帮我解冻账户，我给你五百万”——作者称此为电信诈骗套路，用于类比对方的交易要求（P021）。",
    "重金求子的富婆——作者讽刺性反问（P022）。",
    "性奴隶——作者用以质问控制型关系的待遇差别（P047）。",
    "年报、月报、周报、日报——作者对隐私监控义务升级的形象说法（P035）。",
    "买汽水给老板一百万零三块——作者类比双向高契约成本关系（P040）。",
    "银行与VIP客户、金库安检——作者正面类比，主张安全程序优先（P073-P079）。",
    "“血肉相连，水乳交融”“一同活埋”“粘骨胶”——作者的反驳对象所用词句（P088-P092）。"
   ],
   "conditions": [
    "“如果要论交易性质”为前提限定，作者承认是换一个角度定性（P010）。",
    "作者不绝对否定其做法可行：“也不说你这一定行不通吧，但是……”（P039）。",
    "安全措施的要求是无条件全备，不问与不问都应具备（P064）。",
    "对“有病”“欠钱”等具体风险的替代方案有明说条件：戴套、要体检报告、强化用印签章程序（P057、P059）。",
    "结论建立在“随时可以分手离婚”这一关系条件之上，若该条件不成立则论证前提变化（P007-P009）。",
    "对传统婚恋观的失败判断以“二十岁”“三四十岁”为时间条件，并未给出统计数据（P081）。"
   ],
   "rhetoric_and_tone": "强论辩语气，第二人称直斥，密集反问与感叹（“你有这么恨自己吗？”“这跟爱有什么关系？”），大量贬义判断（蠢事、一无是处、尸横遍野、铁棺材、金锁链），并用数学化措辞（数学上高度不稳定、数学上显而易见的荒谬）加强断言力度。结构上先立论、再逐条反驳、结尾用类比与反问收束。",
   "unresolved_questions": [
    "P096“怎样确定你的女朋友（男朋友）是适合的结婚对象？”为渲染包标记的 lexical 未覆盖片段，疑为平台追加的相关问题标题混入正文，不属于作者论述，需人工核对原始页面。",
    "作者以“数学上”描述关系稳定性与荒谬性，但正文未给出任何模型、数据或推导。",
    "“不知情”的保护作用与“安全措施应全备”如何并存，正文只举通缉犯一例，未给出一般规则。",
    "银行／VIP客户类比的映射关系（谁是银行、何为准备金）未在文中说明。",
    "发布时间2021-09-16、更新时间2025-05-25，版本差异与改动范围未说明。",
    "文中未出现平台话题标签，但结尾出现疑似相关问答链接文本，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "相爱的人根本不问过去，用不着对方再“隐瞒”", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "给你任何优待都是基于我现在的观察、现在的判断", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "这跟你现在如何，没有什么关系", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "现在的亲密关系并没有“嫁鸡随鸡嫁狗随狗，永远不能分手/离婚”这一条啊", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "你手里随时握着闸门，随时可以拉闸", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "你事实上是在做长期重复的临时小额交易，而不是在做一次性的巨型交易", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "要学会把自己的关系变成这种模式，而不要搞“以身相许”模式", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "以身相许模式害人害己", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "孔夫子、关老爷都过不了ta这关", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P024", "quote": "敢于向你坦承可能会导致你放弃的一切事实的人，恰恰是真的爱你而奋不顾身的人", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P025", "quote": "只爱自己而不在乎你上不上当的人，肯定话只说一半", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P026", "quote": "这是一个无法淘汰伪装者、专门为难真爱人的特殊测试", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P030", "quote": "前现代的思维惯性至今没有扭转，只是在无脑的盲目重复传统", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P031", "quote": "贪图“彻底托付”和“彻底控制”的快感", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P034", "quote": "“毫无保留的托付”本来就不是人类可以承受的东西", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P037", "quote": "你这份从年报到日报的隐私监控是另一份单独的负担", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P039", "quote": "你这种“双向高契约成本关系”数学上是高度不稳定的", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P049", "quote": "得到的安全感是虚假的。根本无法断言对方讲的是实话", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P052", "quote": "净损失生活体验", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P062", "quote": "你只想到了问清楚对你的好处，大大忽略了“不知情”对你的保护作用", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P066", "quote": "我爱你的第一表现，就是我接受你对我保持一切怀疑、保持一切戒备", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P070", "quote": "想要靠挖掘我全部的隐私、你对我全部的自由来满足你的“安全感”", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P071", "quote": "你既不知道爱是什么，也承受不起爱的实际重量", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P080", "quote": "传统的所谓“婚恋观”在这个问题上充满着数学上显而易见的荒谬性", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P081", "quote": "你在二十岁建立关系的成功率甚低，而到了三四十岁会关系崩溃的可能性极大", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P086", "quote": "是因为你一开始就用了出了问题分不开的相处方式", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P087", "quote": "你先自己做成分不开，然后说“说分就分”不现实，这属于循环论证", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P094", "quote": "不要给对方的离去设立任何障碍，这样你才能确信对方没有离去完全是因为爱", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系伦理", "隐私与信任", "风险与制度安排"],
   "issue_candidates": ["是否应追问恋人过去", "彻底托付与控制欲", "隐私披露的成本", "婚恋观的前现代惯性"],
   "text_function_candidates": ["答疑", "论辩", "批评", "经验总结"],
   "object_candidates": ["提问者", "追问隐私的一方", "被追问的一方", "银行与VIP客户（类比）"],
   "working_keywords": ["以身相许模式", "双向高契约成本关系", "不知情", "隐私监控", "循环论证", "血肉相连"]
  },
  "notes": "本篇无图片节点。末尾P096为渲染包标注的“lexical未覆盖片段”，内容是一句平台相关问答标题，疑混入正文，已在 unresolved_questions 记录，未据此提出任何主张。作者用“数学上”形容稳定性与荒谬性属修辞，非实证结论。"
 },
 "d354eef8": {
  "analysis": {
   "question_context": "提问者问“应该向恋人坦白自己的过去吗？”。作者认为该问题找错了方向：关键不在要不要告知，而在有没有足够把握对方能不在意你的过去；并把“明知对方受不了却仍要对方接受”判为欲望而非爱。提问者的问题框架不计入作者主张。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "重置问题：关键不在是否告知，而在有无把握对方不在意你的过去；没有把握就不要贪图自己的欲望，不为自己欲望给对方加重负才叫爱。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014"], "summary": "区分对象：能受得了的人会主动让你不必说；男孩女孩美好但受不了；只有真正的爱与能承担的爱者可以让你不必担心因漏说或做错而失去ta们。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "给出答案：对方不在乎知不知道才可以告诉、却没有绝对必要；对方非知道不可则告诉不得也没有必要；即使你洁白无瑕，遇到非洁白不可的人也一样。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P023"], "summary": "收束句：爱不是孩子的事。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个问题令人迷惑，原因在于答案经常找错了方向。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关键并不在于要不要告知过去，而在于你有没有足够把握对方能够不在意你的过去。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "如果你没有把握对方可以接受你的过去，就不要贪图自己心里那点欲望；想跟对方喜结连理是欲望，那不叫爱。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不为了自己的欲望、在明知对方受不了的前提下脑补对方肯定受得了并愿意受，从而给对方加上重负，这才叫爱。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能受得了的人会主动说不用讲了、不管你以前怎样都决定试一试。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "男孩子、女孩子很美好，但是ta们受不了；而你明明知道。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有真正的爱能给你想要的庇护所，只有强大到能支撑真正的爱的人能成为你的答案。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正能爱的人可以让你不必担心因为漏说了什么、做错过什么就失去ta们。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "只有对方是不在乎知不知道的，你才可以告诉，但你也没有绝对的必要去告诉。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方如果非知道不可，你告诉不得，而且很遗憾的——你没有告诉的必要了。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你的过去干不干净根本不重要；只要对方是非洁白不可、非知道不可的人，你即使现在够洁白，将来也会不堪其扰，结局相同。", "evidence": ["E12", "E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱不是孩子的事。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "先指出问题被问错了方向。",
    "把关键改设为：你是否有足够把握对方不在意你的过去。",
    "区分欲望与爱：为满足自己要在一起而让对方背负无法承受的过去，不算爱。",
    "以“能受得了的人会主动说”作为正面判据。",
    "指出不成熟的男孩女孩承受不了，只有真正的爱能提供庇护所。",
    "按对方态度给出两分支结论：不在乎者可以说但无必要；非知道不可者既不能说也无必要。",
    "再推进一层：即使自身洁白，只要对方是非洁白不可的人，结局同样。",
    "以“爱不是孩子的事”收束。"
   ],
   "concept_usage": [
    {"term": "把握", "meaning": "指对“对方能够不在意你的过去”这一点的确信程度，是作者替换原问题的核心判据。", "evidence": "P002", "ambiguity": "如何获得这种把握、把握到何种程度算足够，未说明。"},
    {"term": "爱/真正的爱", "meaning": "本文指不为自己欲望给对方加重负、能承受对方过去、能提供庇护所的品质。", "evidence": "P005", "ambiguity": "与“恋爱”“欲望”的界线只以“受不受得了”举例说明，未定义。"},
    {"term": "男孩/女孩（男孩子、女孩子）", "meaning": "作者指承受不了对方过去的恋人类型，与“男人和女人”对立使用。", "evidence": "P009", "ambiguity": "没有给出年龄或成熟度的判定标准。"},
    {"term": "庇护所", "meaning": "真正的爱所提供的、不必担心因漏说或做错而失去对方的关系状态。", "evidence": "P010", "ambiguity": "与依附、依赖的差别未讨论。"}
   ],
   "examples_and_targets": [
    "“你不用说了，我不管你以前怎样”——作者引述能受得了的人会主动说的话（P006）。",
    "男孩子、女孩子与男人、女人——作者用作承受力对照的群体类别（P007、P009）。",
    "“ta们原谅过比你严重得多的人”——作者所述判断依据，但ta们指谁未在正文说明（P012）。"
   ],
   "conditions": [
    "结论以“如果你没有把握对方可以接受你的过去”为条件（P003）。",
    "对“给对方加重负”的判定以“明知对方受不了”为前提（P005）。",
    "告知的条件：只有对方不在乎知不知道，你才可以告诉，且没有绝对必要（P016）。",
    "不告知的条件：对方非知道不可时，告诉不得，也没有必要（P017）。",
    "外推条件：只要对方是非洁白不可、非知道不可的人，即使自己现在洁白也一样（P021）。"
   ],
   "rhetoric_and_tone": "短句断行、断言式语气，第二人称直陈并夹带警告（“你明明知道”“你只会伤人又伤己”）；用“男孩/女孩”与“男人/女人”的对照形成价值区分；结尾用“爱不是孩子的事”作格言式收束。",
   "unresolved_questions": [
    "标题“BoyzIIMen”（美国男子演唱组合名）与正文内容的关系未在正文中说明，标题含义不明。",
    "“男孩子、女孩子”与“男人、女人”的区分标准（年龄、成熟度或别的维度）未在正文中给出。",
    "P012“因为你目睹过ta们原谅过比你严重得多的人”中的“ta们”指代不明，无法确定是泛指真正能爱的人还是某一具体群体。",
    "作者未说明如何在事前判断对方属于“受得了的人”。",
    "发布时间2021-09-16、更新时间2021-09-17，无法判断是否存在修订。",
    "正文未出现平台话题标签；brief 为正文前段的节选式重复。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这问题之所以令人迷惑，原因在于答案经常找错了方向", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "关键并不在于要不要告知过去，而在于你有没有足够把握对方能够不在意你的过去", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果你没有把握对方可以接受你的过去，你就不要贪图你自己心里那点欲望", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你想跟对方喜结连理，那是你的欲望，那不叫爱", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "给对方加上这么大的重负，这才叫爱", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "你不用说了，我不管你以前怎样，我已经下定决定要试一试", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "男孩子，女孩子，很美好，但是ta们受不了", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "只有真正的爱能给你你想要的庇护所", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "可以让你不必担心因为漏说了什么、做错过什么就“失去”ta们", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "只有对方是不在乎知不知道的，你才可以告诉，但你却也没有绝对的必要去告诉", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "而对方如果非知道不可，你告诉不得", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "其实你的过去干不干净根本不重要", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "你即使现在够洁白、现在可以让ta知道，将来也会不堪其扰", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "爱不是孩子的事", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系伦理", "沟通与自我披露"],
   "issue_candidates": ["是否向恋人坦白过去", "欲望与爱的区分", "承受力与择偶判断"],
   "text_function_candidates": ["答疑", "论辩", "劝导"],
   "object_candidates": ["提问者", "恋人（男孩/女孩、男人/女人）", "能受得了的人"],
   "working_keywords": ["坦白过去", "把握", "庇护所", "真正的爱", "欲望"]
  },
  "notes": "本篇无图片节点。正文未解释标题“BoyzIIMen”与内容的关联，已登记为未决问题。brief 与正文前段重复，仅作导航。"
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
