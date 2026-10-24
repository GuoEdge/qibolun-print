# -*- coding: utf-8 -*-
"""批次 r001-b0127 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0127.sessions.py            # 写 out/r001-b0127.out.jsonl
  python3 records/r001-b0127.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0127"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0127.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "3391e97d": {
  "analysis": {
   "question_context": "知乎提问“厦门千人斩说明什么问题？”（Q001，属提问者）。作者未复述该事件，正文亦无“厦门”“千人斩”字样；回答把问题改写为为何“海王”比“舔狗”更容易“得手”，即婚姻向追求者相对临时向追求者的悬殊劣势（P001、P004）。正文以第二人称对“你/你们”说话，中途转向“裁判员”作规则批评（P034），后半转入“女性文化/英雄/爱”的正面论述（P066 起、P195 起）。作者明确拒绝把问题落在当事人道德上（P001、P010）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005"], "summary": "改写问题：不问当事人道德，改问婚姻向追求者的劣势。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006","P007","P008"], "summary": "立方法论要求：思考的产出是调整预期与策略；情绪消费无益。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009","P010","P011","P012","P013","P014"], "summary": "驳“女性普遍道德崩坏”：无法排除历来如此或条件使然。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P015","P016","P017","P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028","P029"], "summary": "优势A：退出机制→短期密集投入→高数量级表现与误判；附年化对比与自反追问。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P030","P031","P032","P033"], "summary": "建议：想建立长期关系就别报名“经济安全最大化”裁判的比赛。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P034","P035","P036","P037"], "summary": "批评裁判规则缺维度与反作弊，会招来羊毛党。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P038","P039","P040","P041","P042","P043","P044","P045","P046","P047"], "summary": "优势B：临时关系对价远小于终身关系；以并购与租游艇一天作比。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P048","P049","P050","P051","P052","P053","P054","P055","P056","P057","P058","P059","P060","P061"], "summary": "收购前提与保障缺失：多数人不接受要约、终身无硬保障、排他要求霸道。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P062","P063","P064","P065"], "summary": "限定：这是顺你自身逻辑的顺推；真正原因在行动与逻辑不一致、不成熟。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P066","P067","P068","P069","P070","P071","P072"], "summary": "“女性文化”对不成熟迹象绝对敏感，形成无法自述的排序算法。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P073","P074","P075","P076","P077","P078"], "summary": "汇总三条前提并设问是否绝症。", "role": "transition"},
    {"unit_id": "U012", "paragraph_refs": ["P079","P080","P081","P082","P083","P084","P085","P086","P087","P088","P089","P090","P091","P092","P093","P094","P095","P096","P097","P098","P099"], "summary": "存在不依赖任何人的男/女；“女人全这样”是自证闭环，导向三选一。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P100","P101","P102","P103","P104","P105","P106","P107"], "summary": "出路与誓言：对“不是所有女性都唯利是图”固执到底，不走拿钱买这条路。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P108","P109","P110","P111","P112","P113","P114","P115","P116","P117","P118","P119","P120","P121","P122","P123","P124","P125","P126","P127","P128","P129","P130","P131","P132","P133","P134","P135","P136","P137","P138","P139","P140","P141"], "summary": "女性首先愿选英勇；“海王”的秘密是与英雄三分相像，而非见钱眼开。", "role": "claim"},
    {"unit_id": "U015", "paragraph_refs": ["P142","P143","P144","P145","P146","P147","P148","P149","P150","P151","P152","P153","P154"], "summary": "界定“全力以赴”：不是掏钱、时间与尊严；她要的是一句对不起与时间。", "role": "definition"},
    {"unit_id": "U016", "paragraph_refs": ["P155","P156","P157","P158","P159","P160","P161","P162","P163","P164","P165","P166","P167","P168","P169","P170","P171","P172","P173","P174","P175","P176","P177","P178","P179","P180"], "summary": "以“霸道总裁”文类、十三阿哥、浩南哥等文本采样归纳偏好内核。", "role": "example"},
    {"unit_id": "U017", "paragraph_refs": ["P181","P182","P183","P184","P185","P186","P187","P188","P189","P190","P191","P192","P193","P194"], "summary": "断言此为文化/基因底色；“女性都爱钱”是掩饰软弱的借口。", "role": "claim"},
    {"unit_id": "U018", "paragraph_refs": ["P195","P196","P197","P198","P199","P200","P201","P202","P203","P204","P205","P206","P207","P208","P209","P210","P211","P212","P213","P214","P215","P216","P217","P218","P219","P220","P221","P222","P223","P224","P225","P226","P227","P228"], "summary": "辨析“慕强”：英雄之强在心上与道歉；引文块界定“有权判定的人”。", "role": "definition"},
    {"unit_id": "U019", "paragraph_refs": ["P229","P230","P231","P232","P233","P234","P235","P236","P237","P238","P239","P240","P241","P242","P243","P244","P245"], "summary": "英雄因“仅当对方是英雄才奋不顾身”者隐藏；爱必须由被爱成全。", "role": "conclusion"},
    {"unit_id": "U020", "paragraph_refs": ["P246","P247","P248","P249","P250","P251","P252","P253","P254","P255","P256","P257","P258"], "summary": "若对方不是英雄就不要显露；失掉指望后转向物质条件与彩礼；未完待续。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该关心的不是当事人道德，而是“海王”比“舔狗”更易得手，即婚姻向追求者的悬殊劣势。", "evidence": ["E01", "E02"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“注意和思考”的交付物应是调整自己的预期与行动策略，而非给人定一个执行不了的罪名；情绪消费只是精神毒瘾。", "evidence": ["E03", "E04"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“女性普遍道德崩坏”既无现实意义、方法论上也不通：无法排除历来如此，或只是如今才有实现条件。", "evidence": ["E05", "E07", "E08"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "优势A：临时求欢者有可靠退出机制、无须维持对方长期预期，能把有限投入压到极短时间，造出高数量级的直观表现与极大误判。", "evidence": ["E09"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在女方确实遵从物质安全最大化策略的前提下，按年化投入计你是公平落败；而你自己正是用暗示经济保障参赛、并选了相信执行该规则的裁判。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想建立可持续长期关系就不应报名“经济安全最大化”裁判的比赛：长跑规则下任何一段速度落后即判输，报名那一刻已输。", "evidence": ["E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只凭经济豪爽与眼下服从强度判定，规则有缺陷；不引入更多维度与反作弊技巧，会失去有价值玩家并招来大批羊毛党。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "优势B：临时关系比终身关系的对价小得多；终身承诺要求一生相爱、以自己为优先并专一。", "evidence": ["E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抱收购目的者出价再高也不够高，因为很大部分人根本不打算卖；且“永远”无硬保障：离婚自由、旧日公论与宗教风险已消失。", "evidence": ["E17", "E18", "E19"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“被排在后面”只是顺着读者自身逻辑的顺推，不是断言女性真如此排序；真正原因是其未按自身逻辑行动、尚处糊涂盲目。", "evidence": ["E20", "E21"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女性文化对一切不成熟迹象绝对敏感（不是穷、丑、社会地位低），并养成当事人自己也无法说明的排序算法。", "evidence": ["E22", "E23"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "存在很多不打算依赖任何人的女性/男性，其不吃的那一套可归结为“假定所有人肯定都在找长期饭票”；相信女人全这样则成自证闭环，最终只能三选一。", "evidence": ["E24", "E25", "E26", "E27"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出路始于对“不是所有女性都唯利是图”固执到底，即不走拿钱买这条路。", "evidence": ["E28", "E29"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若有得选，几乎每位女性都愿首先选择英勇，是失望到绝望才退而求其次选饭票或及时行乐；不缺钱与独立的奇女子随时代增多。", "evidence": ["E30", "E31"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "不排除有些“短期投机者”确实靠战术得当而成功，但真正原因是女生不接受“为了防止我产生过高的未来期望，对我实施爱的配给制”的逻辑。", "evidence": ["E32", "E33"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "海王真正的秘密不是女性“见钱眼开”，而是其与英雄的三分相像。", "evidence": ["E34", "E35"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从“霸道总裁”文类、十三阿哥、浩南哥等文本采样看，女性偏好的内核是不为金钱所动、肯舍黄带子、只问对不对得起自己。", "evidence": ["E37", "E38"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以抖音、“头条”为据断言“中国女性都看脸看钱”，与其说是有依据，不如说是掩饰自身软弱的借口。", "evidence": ["E39", "E40"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "女性天生爱英雄但不是“慕强”；权势逼人在女性眼里的正常评价是弱。", "evidence": ["E41", "E42"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“全力以赴”难在战胜本能逃避；英雄与普通人的区别在于被判定不够好时道歉而非抱怨，这表示尊重对方不满意的权利。", "evidence": ["E43", "E44"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱是彻头彻尾的英勇；只要是基于爱的亲密关系（不论性别与性取向），本质都是在寻找属于自己的英雄。", "evidence": ["E45", "E46"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "找不到英雄不是因为英雄太少，而是自觉的英雄最忌讳“仅当对方是英雄才考虑奋不顾身”的人，因而隐藏自身；爱必须由被爱成全、双方须是成对的英雄。", "evidence": ["E47", "E48", "E49"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "失去指望后，人最终会放弃真爱的可能性，转而谈“经济实力”“稳定工作”“有车有房”，活着却知道自己遗憾。", "evidence": ["E50"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "她要的不是勉强挤出的钱、时间与尊严，而是一句对不起和你在困难中挤出的时间。", "evidence": ["E36"]},
    {"claim_id": "C025", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "引号段落（P102—P106）以第一人称立誓：无论多少反面证据都相信到底，不走拿钱买这条路，因为怕买到就失去“不是这样的那一位”。", "evidence": ["E29"]},
    {"claim_id": "C026", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "引文块（P219）界定“有权做这判定的人”：父母、合法监护人、被父母托付的老师、依法指派者，以及自己授权的师友、合伙人、客户、评论者与恋人。", "evidence": ["E51"]},
    {"claim_id": "C027", "claim_type": "opponent_view", "attribution": "unknown", "modality": "asserted", "statement": "被作者反驳的两种立场：把问题归为当事人道德（“女性普遍道德崩坏”）；以及“自己投入很大，理应比临时投入者占绝对高优先级”。", "evidence": ["E06", "E52"]},
    {"claim_id": "C028", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问“厦门千人斩说明什么问题？”；作者未在正文叙述该事件，而把问题改写为择偶成功率问题。", "evidence": ["E02"]}
   ],
   "argument_steps": [
    "改写问题：不问当事人道德，改问婚姻向者为何劣势（P001、P004）。",
    "立方法论：思考的产出是调整预期与策略，不是定罪；情绪消费只增绝望（P006—P008）。",
    "驳“道德崩坏”：无法排除历来如此或仅因技术条件才显现（P010—P013）。",
    "优势A：退出机制→极短时间密集投入→高一个数量级的直观表现（P016）。",
    "年化对比：多年三十几万 vs 一周一两万、一天5000、两小时2000（P017—P020）。",
    "推论：若女方遵物质安全最大化，婚姻向者是公平落败（P021—P023）。",
    "自反追问：你用暗示经济保障参赛，并选了这个裁判（P026—P027）。",
    "建议：想建立长期关系就不要报名该裁判的比赛（P030—P033）。",
    "转向裁判员：规则缺维度与反作弊会招来羊毛党（P034—P036）。",
    "优势B：临时关系对价远小于终身关系（P038—P042、P044）。",
    "类比：上亿并购 vs 两万租游艇一天（P045—P047）。",
    "收购前提：对方须正寻求被收购；多数人不接受要约（P048—P051）。",
    "“永远”无硬保障：离婚自由，旧日公论与宗教风险消失（P053—P056）。",
    "排他谈判要求之霸道（P060—P061）。",
    "限定：这是按你自己逻辑的顺推，非说女性真如此排序（P062）。",
    "真正原因：未按自身逻辑行动、不成熟、只是幻影（P063—P065）。",
    "“女性文化”对不成熟敏感，形成不自知的排序算法（P066—P072）。",
    "汇总三条前提，设问是否绝症（P073—P078）。",
    "反驳绝望：存在不依赖任何人的男/女；唯饭票论是自证闭环（P079—P099）。",
    "出路与誓言：对“不是所有女性都唯利是图”固执到底（P100—P107）。",
    "正面主张：女性首先愿选英勇；海王的秘密是与英雄三分相像（P108—P141）。",
    "界定“全力以赴”的真意（P142—P154）。",
    "以文艺文本采样归纳偏好内核（P155—P180）。",
    "断言文化/基因底色，把“女性都爱钱”判为软弱借口（P181—P194）。",
    "辨析“慕强”：强在心上、在道歉与尊重评判权（P195—P228）。",
    "结论：英雄隐藏自身；爱须由被爱成全；最终转向物质条件与彩礼（P229—P256）。"
   ],
   "concept_usage": [
    {"term": "海王／舔狗", "meaning": "作者借网络词指短期多偶者与婚姻向追求者，并称其“真够脏”（P002），后改称临时向/婚姻向追求者（P004）。", "evidence": "P001", "ambiguity": "两套称法是否同指未说明。"},
    {"term": "经济安全最大化／物质安全最大化", "meaning": "作者设想的择偶判定原则，称其“基本上是女性几百万年来养成的本能”（P076）。", "evidence": "P023", "ambiguity": "作为推理前提使用，未提供其为女性实际准则的证据。"},
    {"term": "裁判员／比赛规则", "meaning": "择偶竞争被比作有裁判按规则判定的比赛：你选了相信执行该规则的裁判（P026），裁判员自身也需改规则（P034—P036）。", "evidence": "P026", "ambiguity": "裁判既似指女方又似指规则，主体有滑动。"},
    {"term": "对价", "meaning": "交换条件：临时关系只要一夜贪欢，终身关系要求一生相爱、以自己为优先、专一（P038—P044）。", "evidence": "P038", "ambiguity": "未说明如何计量。"},
    {"term": "并购／全面收购／租一天", "meaning": "婚姻向追求比作上亿并购，临时关系比作两万租游艇一天；很多人不接受任何收购要约（P045—P050）。", "evidence": "P048", "ambiguity": "比喻与真实行为的对应边界未给。"},
    {"term": "排序算法", "meaning": "女性“在接受自己身份过程中养成的”、当事人意识不到的排序机制（P070—P072）。", "evidence": "P070", "ambiguity": "作者承认当事人自述不了，等于不可直接验证。"},
    {"term": "女性文化", "meaning": "“天生的敏锐观察者的文化”，核心主题是对一切不成熟迹象的绝对敏感（P066）。", "evidence": "P066", "ambiguity": "以“文化”作整体主体，内部差异与例外未界定。"},
    {"term": "不成熟", "meaning": "思维不连贯、逻辑不通顺，尤指主张与行动不自洽（P063—P066）。", "evidence": "P066", "ambiguity": "无操作化判定标准。"},
    {"term": "英勇／英雄", "meaning": "爱是“彻头彻尾的英勇”（P228）；英雄＝全力以赴而仍被判定不够好时道歉而非抱怨、尊重对方评判权（P213—P222）。", "evidence": "P214", "ambiguity": "与武侠、影视示例的对应由作者自拟。"},
    {"term": "慕强", "meaning": "作者否认女性偏好是慕强，称权势逼人在女性眼里是弱（P196、P201）。", "evidence": "P201", "ambiguity": "又称“强无人不慕”（P204），两处“强”含义需分辨。"},
    {"term": "全力以赴", "meaning": "相处一天必要全力以赴（P126）；难在战胜本能逃避（P220）；不是掏空钱、时间与尊严（P143）。", "evidence": "P220", "ambiguity": "短期密集投入（P016）与心性（P220）两处含义不同。"},
    {"term": "饭票／唯饭票论者", "meaning": "以长期经济保障为择偶目标者及其逻辑：假定所有人都在找长期饭票（P084、P087、P095）。", "evidence": "P084", "ambiguity": "比例与适用范围未说明。"},
    {"term": "短期投机者", "meaning": "他人对屡屡成功者的定性，作者质疑其解释力（P119、P123）。", "evidence": "P123", "ambiguity": "作者只部分接受该定性（P124），未给替代称法。"},
    {"term": "无间地狱／精神毒瘾", "meaning": "修辞性比喻：道德判决式新闻消费如烟土毒瘾（P007）；坚持“女人全这样”的世界如无间地狱（P097）。", "evidence": "P097", "ambiguity": "比喻不构成可检验命题。"}
   ],
   "examples_and_targets": [
    "“厦门千人斩”：仅见提问字段（Q001），正文未复述；属提问者背景。",
    "几年花三十几万未获青睐者（P017）：作者的反驳与训诫对象。",
    "年化换算（一周一两万→年化50—100万；一天5000→130万；两小时2000→208万，P018—P020）：作者自设论证数据，非外部统计。",
    "网游礼品规则与羊毛党（P036）：作者类比。",
    "上亿并购与“两万租一天游艇”（P045—P046）：作者类比。",
    "胡一刀/胡夫人（P111）、郭靖/黄蓉（P112、P197）、红拂/李靖（P198）：文学人物，类比例证。",
    "“霸道总裁”文类（P155—P168）：文本采样，归出“写的是霸道女主”。",
    "十三阿哥、黄带子（P169—P175）：清宫剧情节，证“肯舍黄带子”“以国士相报”。",
    "浩南哥（P176—P179）：《古惑仔》人物，证“只要你是个英雄，我都可以原谅”。",
    "抖音、“头条”（P184）：被批评的信息来源。",
    "彩礼、“经济实力”“稳定工作”“有车有房”（P254—P255）：作者指出的替代话语。",
    "女性宏观数据（职业、经济、政治地位与自我意识“都在很明显的增长”，P117）：无具体数字。",
    "“管理未来期望”“爱的配给制”（P125—P128）：作者所斥的相处逻辑。"
   ],
   "conditions": [
    "推理前提：女方以“经济安全最大化/物质安全最大化”为最高原则（P023、P076），作者称其近乎几百万年的本能。",
    "作者自设限定：被排在后面只是顺着读者自身逻辑的顺推（P062）。",
    "敏感对象限于不成熟，不是穷、丑、社会地位低（P066）。",
    "适用范围：基于爱的亲密关系，不论男女与性取向（P229）。",
    "英雄隐藏自身的条件：对方不是英雄就不要显露（P246）；这是被勉强与贪心惩罚后的教训（P243）。",
    "誓言前提：无论多少反面证据、辜负与挫折（P100、P103）。",
    "例外与保留：存在不依赖任何人的男/女（P080）；不排除有些投机者战术得当（P124）；“话也不说死”（P140）。",
    "趋势限定：越来越多人不接受收购要约（P048）；奇女子越来越多（P116）。",
    "制度条件：法律给男性随时离婚的自由（P053）；旧日公论与宗教风险已消失（P056）。",
    "评判权范围：仅父母、监护人、依法指派者与本人授权者有权判定，未授权者属“不畏强暴”范畴（P219）。",
    "代价：坚持“女人全这样”者只能三选一（P093、P098）。"
   ],
   "rhetoric_and_tone": "第二人称“你/你们”的训诫体，反问连发（P011—P014、P025、P029、P059、P089、P096）；口语粗口（“md”“呸呸呸”P002、“tm”P132、“去他x的”P102）并当场改口，形成自我纠偏叙事。比喻贯穿：比赛/裁判/长跑短跑、并购与租赁、网游礼品与羊毛党、烟土与精神毒瘾、无间地狱。短句排比与金句收束（P126、P228）；直斥读者动机（P184），又自称“我tm说着都心疼”（P132）。以文艺文本作“采样点拟合曲线”（P180）的归纳式论证；末尾自注未写完（P257—P258）。",
   "unresolved_questions": [
    "提问的“厦门千人斩”事件正文完全未叙述（全文无“厦门”“千人斩”字样）；“这数据如此的悬殊”（P005）未给出处，事件与数据待外部核查。",
    "P018—P020 的“年化”换算为作者自设算法，折算规则与依据未说明。",
    "P101—P107 引号内第一人称誓言未标明说话者与出处（自拟、引用他人或代读者立誓不明）。",
    "P219 为 lexical quote 节点，内容似术语界定，但未标注说话者与来源，归属待核。",
    "P085、P093 称“数学证明了/数学已经告诉你”，正文未给模型与推导。",
    "P068“上百万年”、P181“写在基因里”、P195“女性天生爱英雄”属无引证的演化/生物学断言，待外部核查；与 P080、P113 承认的例外范围关系不清。",
    "P117“各种宏观数据”、P118“四千多年里最不需要找饭票的时代”均未列具体数据。",
    "本篇自称未写完（P257—P258“未完，待续”）；published 2021-05-26、updated 2021-06-27，是否有续篇或后续版本待查。",
    "brief 与正文 P001 重复且在“……和”处截断（元数据缺字）。",
    "作者一面作“女性文化”“写在基因里”（P066、P181）式整体概括，一面强调“不是所有女性”（P080、P100），普遍程度与例外范围未界定。",
    "“裁判员”主体有滑动：P026 指“你选择相信其执行规则的裁判”，P034 又说“裁判员们自己也要想清楚”。",
    "lexical 段落节点 274 与可读正文 258 段不一致，差异原因未查明。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "为什么“海王”比“舔狗”更容易“得手”", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P004", "quote": "婚姻向的追求者反而比以临时向的追求者有如此显然的劣势", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P006", "quote": "而应该是“我应该如何调整我的预期和行动策略”", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P007", "quote": "只是一种精神毒瘾", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P010", "quote": "在方法论上本来就是逻辑不通的", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P010", "quote": "女性普遍道德崩坏", "relation": "contradicts"},
    {"key": "E07", "paragraph_id": "P012", "quote": "只是现在有了飞机高铁可以实现", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P013", "quote": "你怎么知道这不是女性历来就有的倾向？", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P016", "quote": "ta们因为预知自己有可靠的退出机制", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "折合“年化投资预期”可是五十万、一百万起步", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P023", "quote": "只要女性的确遵从物质安全最大化策略", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P026", "quote": "你自己不就是在用不断暗示你将提供经济保障", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P030", "quote": "不要去选择“经济安全最大化”的裁判员", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P035", "quote": "在经济上是否豪爽、在眼下的服从强度上是否足够大", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P036", "quote": "不但失去有价值的玩家，还招来大批的羊毛党", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P038", "quote": "就是临时关系比终身关系要的对价小得多", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P048", "quote": "将来会越来越多——是不接受任何收购要约", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P049", "quote": "无论你出价多高，其实都不够高", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P055", "quote": "你宣称的所谓永远，并没有任何硬的保障", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P062", "quote": "可不是在说女性真的就是按照这个逻辑", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P063", "quote": "而是你没有顺着你自己的逻辑", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P066", "quote": "核心主题就是对一切不成熟迹象的绝对敏感", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P070", "quote": "触发了女性在接受自己身份过程中养成的排序算法", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P080", "quote": "存在着很多不打算依赖任何人的女性/男性", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P084", "quote": "就是假定所有的人肯定都在“找长期饭票”", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P091", "quote": "你要相信世界上的女人全是这样，没人能向你证明不是", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P098", "quote": "去当海王躲一辈子、苦苦追求然后天天恐惧被比下去", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P100", "quote": "对“不是所有女性都唯利是图”这一点固执到底", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P106", "quote": "买到了，会失去了不是这样的那一位", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P108", "quote": "几乎每一位女性都愿意首先选择这样的英勇", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P113", "quote": "不缺宠爱、不缺独立、不缺自由的奇女子", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P124", "quote": "不排除有些的确是这样", "relation": "qualifies"},
    {"key": "E33", "paragraph_id": "P125", "quote": "“为了防止我产生过高的未来期望，对我实施爱的配给制”", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P133", "quote": "因为她们不是“见钱眼开”", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P135", "quote": "是那份你们没有的和英雄的三分相像", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P151", "quote": "她要的是你一句对不起", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P158", "quote": "它写的是一个打落牙齿往肚里咽，绝不低头的人", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P179", "quote": "不是对不对得起我，是对不对得起你自己", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P184", "quote": "不如说是对这掩饰自身软弱的借口迫不及待", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P191", "quote": "而是因为你太软弱", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P196", "quote": "但这不是“慕强”", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P201", "quote": "权势逼人在女性眼里的正常评价是弱", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P214", "quote": "一个英雄会道歉", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P220", "quote": "不在于在事务方面，而在于战胜自己的本能的逃避上", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P228", "quote": "爱是一种彻头彻尾的英勇", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P229", "quote": "本质上都是在寻找属于自己的英雄", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P235", "quote": "最忌讳的，就是“仅当对方是英雄才会考虑奋不顾身”", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P243", "quote": "于是ta们选择了对你隐藏自己的存在", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P244", "quote": "爱必须由被爱成全", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P254", "quote": "转而去谈“经济实力”“稳定工作”“有车有房”", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P219", "quote": "你天生的父母、合法监护人、被父母托付的老师", "relation": "context"},
    {"key": "E52", "paragraph_id": "P039", "quote": "自己应该比那些临时投入的人占有绝对高的优先级", "relation": "contradicts"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋与择偶", "性别议题", "社会交换/策略类比（作者自设框架）", "人格与伦理（英雄、英勇、成熟）", "演化心理学式断言（作者自称，无引证）"],
   "issue_candidates": ["短期关系与婚姻向追求的成功率差异", "择偶中的物质条件与安全感", "彩礼与婚姻市场话语", "道德判决与情绪消费", "成熟度/逻辑自洽作为择偶信号", "“慕强”与英雄气质的区分", "真爱的可能与自我隐藏"],
   "text_function_candidates": ["答疑（知乎回答）", "论辩与反驳", "训诫劝导（第二人称）", "类比式解释", "未完成连载"],
   "object_candidates": ["提问者", "作者设想的“你/你们”（婚姻向男性追求者）", "被作者整体概括的“女性”", "海王/短期投机者", "“裁判员”（择偶判定方）", "霸道总裁文类、清宫剧、古惑仔（文艺文本）", "郭靖/黄蓉、胡一刀/胡夫人、红拂/李靖（文学人物）", "抖音、“头条”"],
   "working_keywords": ["海王", "舔狗", "临时向/婚姻向追求者", "经济安全最大化", "裁判员", "对价", "并购/收购", "排序算法", "女性文化", "不成熟", "全力以赴", "英雄", "慕强", "饭票", "短期投机者", "彩礼", "honor"]
  },
  "notes": "无图片节点（images=[]、image_checked=false 属正常），正文非空，故 status=read。提问（Q001“厦门千人斩说明什么问题？”）属提问者，正文未复述该事件，也未出现“厦门”“千人斩”字样；brief 与正文 P001 重复且在“和”处截断。正文无平台话题标签文字混入，无 provenance/superseded 版本信息；published_at 2021-05-26、updated_at 2021-06-27，正文自称“（未完，待续）”。结构方面：lexical 含 1 个 quote 节点（对应 P219），段落节点计数 274 与可读段落 258 不一致；text 与 lexical 无 divergence 告警。P101/P107 是独立成段的引号开合标记，故引文块为 P102—P106。"
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
