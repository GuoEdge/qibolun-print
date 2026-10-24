# -*- coding: utf-8 -*-
"""批次 r001-b0100 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0100.sessions.py            # 写 out/r001-b0100.out.jsonl
  python3 records/r001-b0100.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0100"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0100.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "b4019eab": {
  "analysis": {
   "question_context": "提问者（Q001）问“怎么培养安全感？”。作者在正文开头说明本篇“实际上是上接这一篇的”（P001），并在 P002 放置指向其另一篇回答（货拉拉跳窗女生相关问答）的外链节点；随后以“第一个问题是，为什么安全感很重要？”（P003）进入正题：先论安全感缺乏与过强的双重危害，再破除“绝对安全观”，从人与自然的关系、对专业犯罪者的震慑、警觉心，直到“向死而生”与“安全感来自勇气”作结。P002 的标题文字属外链，不是作者本篇正文主张；Q001 的提问立场不得归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "标明本篇接续前一篇回答，并提出先回答“安全感为什么重要”。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "安全感是压舱石；缺乏者会在刺激面前做高成本反应（疏远关系、足不出户、易受惊、恐惧背叛），导致生存成本过高并拖累亲人。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "安全感过强同样有害（对风险不敏感、保障投资不足）；不足与过剩常并存伴生，过剩常态催生不足的焦虑，类比自负与自卑。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016"], "summary": "破题先破除“绝对安全观”：安全概率的成本急剧上升、不可持续的安全无意义、对安全的绝对追求损害实际安全，须容纳并管理意外，以中性甚至积极态度看待风险。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "安全来自两个方面，第一是与自然的关系：自然的要求恒久且责任在人、不接受反驳；了解并顺应自然规律（含社会、经济规律）是安全感体系的根基，顺应自然法则的技能长期有效，与自然关系牢固是最大源泉。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040"], "summary": "由此得到最大底牌“此处不留爷，自有留爷处”；与自然关系密切的人是组织核心资产，受所属一切关系的慎重对待与对等保护，是对付潜在恶意的基本筹码。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P041", "P042", "P043"], "summary": "反驳“身强力壮即可自保”：身体强壮只对理智的业余侵犯者有效，且易因安全感过强而松懈，“以有心算无心，虽有力亦不能胜”。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P044", "P045", "P046", "P047", "P048", "P049", "P050"], "summary": "真正震慑在于侵犯者顾虑你方关系网必然发动的追查惩罚；要害之一是展现自己是有价值、有背景的利益环节，干练气质自然流露。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P051", "P052", "P053", "P054", "P055", "P056"], "summary": "要害之二：绝不让任何人相信你与一切人断联；宣称“没有一个朋友可信”等于画靶子，绝对断线对犯意者诱惑极大，不法之地极危险即因此。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068"], "summary": "终极策略是让人意识到你有很强的爱的能力（Caritas，不限男女情爱）；基于 caritas 的羁绊深于利害，伤害这样的人必遭不计代价索取正义的追偿，是震慑邪恶的达摩克利斯之剑。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078"], "summary": "相应禁忌：不在陌生人面前以真实身份流露愤世嫉俗的极端观点，因为那等于公开证明你无亲密关系、消失了无人追查；这些策略好过请一堆保镖。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090"], "summary": "警觉心没有过逾：以跳车女孩被嘲讽为例，主张对物理威胁不反应应是思考后的决定而非未觉察；只有警觉与忧患意识者才会走向总体防御体系。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098"], "summary": "仅有气质、联系与安全保障仍不够：蠢人、病人、无心之人不可防，人终会遇到警觉不到、应对不来也无法震慑的危险。", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P099", "P100", "P101", "P102", "P103", "P104"], "summary": "最终安全来自明了人生价值、全力以赴、随时可死而无憾（向死而生）；真正保证安全感的不是武力实力，而是勇气。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "安全感是人的压舱石；没有安全感的人显著特征是会在刺激面前做出高成本的反应。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "安全感缺乏导致生存成本过高，并因亲密关系的共生性夺取亲人的精力与资源，最终可能迫使他人脱离亲密关系。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "安全感过强同样为害甚烈：对风险不敏感、对未来风险保障投资不足，后果往往由爱他的人支付。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "安全感不足与过剩并不互斥，反而常常伴生；安全感过剩的常态会催生安全感不足的高度焦虑，类似自负与自卑的伴生。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“绝对安全观”（认为完全的安全可以且应该追求）应当被破除。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "支撑安全概率的成本随概率上升而急剧增大，从 99.9999% 升到 100% 所需代价超过人类有史以来创造的全部财富。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不可持续的安全没有意义；对安全的绝对追求本身就会损害实际的安全水平，人不可能只学避免风险而免掉冒险这门课。", "evidence": ["E009", "E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "意外一定会发生，绝对不允许它发生反而使它更多发生且更具突然性和破坏性；要害是容纳、管理意外而非仅仅排除。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正确的安全观以正确、中性甚至积极的看待风险为起点。", "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自然的要求恒久存在、不接受反驳、上诉或第三方审判，认清这些要求的责任无条件在人类一方。", "evidence": ["E013", "E014"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "确知自己未抵触已知自然规律、并已尽最大可能了解自然规律，是人类健康的安全感体系的根基。", "evidence": ["E015"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "社会规律、经济规律等由自然法设定的关于人的法则也是自然律的一部分，虽受“zz正确”干扰，仍不以个人意志为转移。", "evidence": ["E016"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "顺应自然法则习得的技能只要自然规律不改就长期有效；其中不受具体人、具体条件限制的成分越大，越属于与自然的关系。", "evidence": ["E017", "E018"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与自然的关系牢固是安全感最大的源泉，最大底牌是“此处不留爷，自有留爷处”。", "evidence": ["E019"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与自然关系密切的人是组织的核心资产，会受到其所属一切关系的慎重对待和对等保护，这种礼遇是应对潜在恶意的基本筹码。", "evidence": ["E020", "E021"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "身强力壮仅对理智的业余侵犯者有一定吓阻，对有系统、有计划、有经验的侵犯者几乎无意义；身强力壮者反而易因安全感过强而松懈。", "evidence": ["E022", "E023"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正震慑侵犯者的是其对伤害你之后果的顾虑——由你的同志、朋友、亲人、社区（含公检法）必然发动的追查和惩罚。", "evidence": ["E024"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要害之一是自己展现出的能力有价值，足以让人意识到你多半是某种利益关系的重要环节。", "evidence": ["E025"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要害之二是不要让任何人相信你与一切人断联；说出“没有一个朋友可信”等于在自己身上画靶子。", "evidence": ["E026", "E027"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术性手段之上的终极策略，是让人意识到你身上有很强的爱的能力，即不限于男女情爱的 Caritas。", "evidence": ["E028"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基于 caritas 的关心与羁绊深入人性本能、先于物质利益、决定价值观，不同于有止损线、可交易、有期限、可收买的利益照顾。", "evidence": ["E029", "E030"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "伤害为人所深爱的人必面对不计代价的追偿，那不是复仇或求偿而是索取正义，是震慑一切邪恶的达摩克利斯之剑。", "evidence": ["E031", "E032"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要在陌生人面前以实际身份流露愤世嫉俗的极端观点，因为这类言论会让人估计你没有任何有质量的亲密关系、消失了也无人追查。", "evidence": ["E033", "E034"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对老练的专业掠食者而言，这些策略是作者可以负担的较好方案，好过请一堆保镖。", "evidence": ["E035"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "警觉心没有过逾；对可能构成物理威胁的事物不做出明显反应，应是思考过预防与反制措施后的决定，而不是根本没觉察到威胁的可能。", "evidence": ["E036", "E037"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "嘲弄跳车女孩警觉心“想象力丰富”的态度才是不健康、不知死活的幼稚；“你想太多”常出自无力感下的鸵鸟政策，或是在掩盖攻击意图。", "evidence": ["E038", "E039", "E040"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有具备警觉心与忧患意识的人，才会最终走上寻求总体性、全面性、决定性防御体系的路。", "evidence": ["E041"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "足够的警觉心、应对训练与安全保障并不足以完全保证安全感，因为人终会遇到警觉不到、应对不来、也无法震慑的危险。", "evidence": ["E042", "E043"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正带来最终安全的是明了自己的人生价值并全力以赴，随时随地处在可以死而无憾的状态。", "evidence": ["E044"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "向死而生是人的勇气可能的最大、最坚实的根底，是战胜贪念和恐惧的最后保证。", "evidence": ["E045"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真正保证安全感的从来不是武力或实力；安全感的来源不是安全的“保障”，安全感来自勇气。", "evidence": ["E046", "E047"]}
   ],
   "argument_steps": [
    "本篇接续前一篇回答，先答“安全感为什么重要”（P001—P003）。",
    "界定危害：安全感缺乏者以高成本反应应对刺激，生存成本过高并牵累亲人（P004—P005）。",
    "补充反向危害：安全感过强则风险保障投资不足；二者常伴生，过剩常态催生不足焦虑（P006—P009）。",
    "破题：先破除“绝对安全观”——成本随安全概率急升、不可持续的安全无意义、绝对追求反损安全（P010—P014）。",
    "正面起点：意外必然发生，须容纳与管理；以中性甚至积极态度看待风险（P015—P016）。",
    "构建路径一：与自然的关系——自然要求恒久、责任在人、不接受反驳；顺应自然规律（含社会、经济规律）与技能积累构成安全感根基与最大底牌（P017—P036）。",
    "由自然关系推出人际筹码：人是应对客观世界的资本，受关系网保护即是对潜在恶意的筹码（P037—P040）。",
    "反驳武力自保论（P041—P043），提出震慑来自后果顾虑（P044—P045）。",
    "要害一：展现自己有价值、是利益环节（P046—P050）；要害二：绝不让人相信你与一切人断联（P051—P056）。",
    "终极策略：展现爱的能力（Caritas）→ 基于 caritas 的追偿即“索取正义”，构成终极震慑（P057—P068）。",
    "相应禁忌：不公开流露愤世嫉俗的极端观点；这些策略好过保镖（P069—P078）。",
    "补论警觉心：以跳车女孩案例反驳嘲讽者，主张反应应是思考后的决定（P079—P090）。",
    "让步限定：蠢人、病人、无心之人不可防，警觉与保障仍有极限（P091—P098）。",
    "结论：明了自己的人生价值、向死而生；安全感来自勇气（P099—P104）。"
   ],
   "concept_usage": [
    {"term": "安全感", "meaning": "人的“压舱石”，表现为面对刺激不做高成本反应、并能管理风险的状态；文中兼论其缺乏与过强两种偏差", "evidence": "P004", "ambiguity": "未给出可操作的界定或度量，缺乏与过强均以后果描述"},
    {"term": "绝对安全观", "meaning": "认为完全的安全可以追求（甚至理所当然、应该追求）的观念，作者主张破除", "evidence": "P011", "ambiguity": "作者未说明现实中谁会持此观念"},
    {"term": "自然／自然规律", "meaning": "不仅指金木水火土，也包括人类自身及社会规律、经济规律等由自然法设定的关于人的法则", "evidence": "P026", "ambiguity": "外延被作者扩张到社会与经济领域，边界依赖“自然法”这一未定义的设定；P027"},
    {"term": "Caritas", "meaning": "不限于男女情爱的一种爱的能力，能带来深入人性本能的关心与情感羁绊", "evidence": "P059", "ambiguity": "未给出词源或定义出处，也未说明与一般“爱”的区别；P063"},
    {"term": "正义", "meaning": "由牵连者自身价值观驱动、不计代价实施的追偿，作者将其与复仇、求偿相区分", "evidence": "P065", "ambiguity": "仅一句断言，未展开判定标准；P066"},
    {"term": "向死而生", "meaning": "明了自己的人生价值并全力以赴、随时随地可以死而无憾的状态", "evidence": "P099", "ambiguity": "属格言式表述，未说明如何达成；P102"},
    {"term": "性感", "meaning": "结尾用以关联安全感（“性感的根源是安全感”），并称亿万富翁与独裁君主毫不性感", "evidence": "P103", "ambiguity": "本篇未定义，与《幽默与性感》一篇的用法是否同一含义不明"},
    {"term": "专业犯罪者／专业掠食者", "meaning": "有系统、有计划、有经验、以犯罪为生意并奉行低风险原则的侵犯者", "evidence": "P041", "ambiguity": "未给出区分业余与专业的标准；P050"}
   ],
   "examples_and_targets": [
    "货拉拉跳窗女生事件与嘲弄其警觉心的网民（作者的反驳对象，P002、P080、P081）",
    "“有人在你面前举起铁锤，你要想想ta是不是会用来攻击你”（作者的设问例证，P080）",
    "金三角、战乱之地、蛮荒西部、戈壁无人区（作者论据：不法之地极危险的主因，P056）",
    "骑车、游泳、奔跑、驾驶、种植、收割、开采、提炼、锻造、雕刻、速写、描述、测量、建筑、拆除、计算、计划、管理、组织（作者列举的顺应自然法则的技能，P031）",
    "村子里的农夫和战士、公司里最有业绩的销售员（作者类比：组织核心资产，P039）",
    "公检法（作者列举的追查与惩罚主体，P044）",
    "达摩克利斯之剑（作者修辞，P067）",
    "“此处不留爷，自有留爷处”（作者引俗语作最大底牌，P036）",
    "亿万富翁与疑神疑鬼的独裁君主（作者举例：富甲天下、权倾一时却毫不性感，P103）",
    "“那美好的仗我已经打过了，当跑的路我已经跑尽了”（作者引述／化用的宗教语句，用作向死而生的自述，P101）",
    "“世界上没有一个好人”“人间不值得”（作者列为禁忌的愤世嫉俗言论样例，P070）"
   ],
   "conditions": [
    "以“如果我们把安全风险设为不失败概率”为假设前提（P012）",
    "以“想从99.9999爬升到100%”为极端条件说明成本（P012）",
    "“只要自然规律不做修改，就会一直有效”的条件限定（P031）",
    "“你所做的之中不受具体人、具体条件限制的成分越大……”的程度条件（P032）",
    "“如果身边人无法再承受这样的损失而离开”的假设（P007）",
    "“如果对方是有系统、有计划、尤其是有经验的”限定（P041）；并自注“对不理智的业余侵犯者也没意义”（P041）",
    "“只要ta们没有把握逃脱这种追查，ta们就不会轻易的动手实施”的条件（P045）",
    "“不要让任何人在任何时刻相信”的绝对化要求（P051）",
    "“如果你一定要说来发泄一下，切记要确保一切能听见这些话的人里面没有人有可能知道你是谁”的例外条件（P075）",
    "“那些喜欢把‘你想太多’挂在嘴边的人……如果ta们不是在尝试掩盖自己的攻击意图的话”这一保留（P090）"
   ],
   "rhetoric_and_tone": "训诫体格言体，通篇第二人称“你”直接告诫；大量排比与递进（“不接受反驳、不接受上诉、不接受任何第三方的审判和修订”），并用“压舱石”“达摩克利斯之剑”“剑与盾”“一堆肉”等比喻。对读者以教练口吻下达禁忌与策略，对嘲讽者转为讥讽与激愤（“不知死活的幼稚”“悔恨入骨的愚蠢”）；P099—P101 转为庄重的自述式抒情并化用宗教语句；P103 以“性感”收束，与作者其他篇目用语呼应。结构为“为什么重要—如何构建—仍有极限—最终靠勇气”的层层推进。",
   "unresolved_questions": [
    "P002 与 P060 为外链节点（分别指向作者另一篇回答与问答“爱到底是什么”），其文字混入正文流且未被 lexical 覆盖，属结构差异；链接目标内容不在本篇范围",
    "P018 称“安全来自两个方面”，但正文只显式标出“1）来自人与自然的良好关系”，第二方面没有编号标题；按后文推断应指与他人的关系／爱的能力，文中未明说，属结构缺口",
    "成本—概率论述（90%→95%、99.9999%→100% 需填进人类全部财富）无数据来源，属示意性论证，需外部核查（P012）",
    "Caritas 一词未给出定义或出处（是否指基督教的爱德），需外部核查（P059、P063）",
    "“zz正确”为拼音缩写，所指不明确，需外部核查（P028）",
    "以“反社会人格”作为“病人”的举例属通俗用法，非临床诊断，作者未给依据（P094）",
    "“专业犯罪者”的行为规律（做的是生意、奉行小心行得万年船）为作者断言，无数据或案例来源（P050）",
    "文章 published_at 2021-03-06、updated_at 2023-07-24，是否存在后续增补删改，本文未说明",
    "brief 与正文开头（P004）重复且被截断于“疏远一”，brief 其余内容未在正文出现，差异原因未说明",
    "篇末“性感”与《幽默与性感》（同批 d558794b）中“性感即勇敢”的用法是否同一含义，本篇未说明"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P004", "quote": "安全感是人的压舱石", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "就是会在刺激面前做出高成本的反应", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "还会因为亲密关系的共生性而夺取亲人的精力和资源", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P007", "quote": "所谓安全感过强，是指对风险的可能性不敏感，因此对未来的风险保障投资不足", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P008", "quote": "安全感不足和安全过剩，不但可以并存，而且恰恰常常是伴生在一起的", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "这一点颇为类似自负与自卑的伴生关系——唯其自负，所以自卑", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P011", "quote": "你要破除掉“绝对安全观”", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P012", "quote": "把人类有史以来创造的全部财富都填进去，也根本不够", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P013", "quote": "你要考虑到不可持续的安全是没有意义的", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P014", "quote": "对于安全的绝对追求，本身就会损害实际的安全水平", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P015", "quote": "要害在于要容纳意外，管理意外，而不是仅仅排除意外", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P016", "quote": "正确的安全观，首先就以正确的、中性的、甚至是积极的看待风险为起点", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P021", "quote": "自然的要求恒久存在，不符合要求就要遭受损失", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "自然不接受反驳、不接受上诉、不接受任何第三方的审判和修订", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "是人类健康的安全感体系的根基", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P027", "quote": "社会规律、经济规律……等等一切由自然法设定的关于人的法则，一样是自然律的一部分", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P031", "quote": "只要自然规律不做修改，就会一直有效", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P032", "quote": "你所做的之中不受具体人、具体条件限制的成分越大，它就越成其为你与自然的关系的一部分", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P034", "quote": "你与自然的关系牢固，会是你安全感的最大的源泉", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P039", "quote": "属于组织的核心资产", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P040", "quote": "这样的人会受到ta所属的一切关系的慎重对待和对等保护", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P041", "quote": "几乎对理智的、专业的、有经验的侵犯者没有意义", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P042", "quote": "而且所谓身强力壮的人，反而容易因为安全感过强而意识松懈", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P044", "quote": "那些由你的同志、你的朋友、你的亲人、你的社区（这包括了公检法）必然发动的追查和惩罚", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P047", "quote": "你自己展现出的能力是有价值的，足以让人意识到你多半是某种利益关系的重要环节", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P051", "quote": "你处在与一切人都断联的状态", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P053", "quote": "你等于在自己身上画了一个靶子", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P059", "quote": "这说的不是限于那种男女情爱，而是指Caritas", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P062", "quote": "是有止损线的，是可以交易的、也是有期限的", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P063", "quote": "不是被价值观所决定，而是决定价值观的东西", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P064", "quote": "你必定要面对被不计代价也要实施的追偿", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P066", "quote": "不是复仇、不是求偿，而是索取正义", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P070", "quote": "不要在陌生人面前以实际身份流露愤世嫉俗的极端观点", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P071", "quote": "你消失了估计没有人会真的会来追查和关心", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P078", "quote": "它要好过请一堆保镖", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P079", "quote": "警觉心是没有过逾的", "relation": "supports"},
    {"key": "E037", "paragraph_id": "P082", "quote": "都应该是思考过预防和反制措施后的决定", "relation": "supports"},
    {"key": "E038", "paragraph_id": "P080", "quote": "无数的人嘲弄女孩的警觉心是“想象力丰富”", "relation": "context"},
    {"key": "E039", "paragraph_id": "P081", "quote": "但其实这种嘲讽本身才是不健康、而且是不知死活的幼稚态度", "relation": "supports"},
    {"key": "E040", "paragraph_id": "P089", "quote": "受不了这种无力感于是宁可选择鸵鸟政策求个虚假的心安而已", "relation": "supports"},
    {"key": "E041", "paragraph_id": "P087", "quote": "只有有这种警觉心和忧患意识的人，才会最终走上寻求某种有总体性的、全面性的、决定性的防御体系的路", "relation": "supports"},
    {"key": "E042", "paragraph_id": "P096", "quote": "有足够的警觉心，有足够的应对的训练，也有足够的安全保障，并不足以完全保证你的安全感", "relation": "supports"},
    {"key": "E043", "paragraph_id": "P097", "quote": "你一定会遇到你警觉不到、应对不来、也无法震慑的危险", "relation": "supports"},
    {"key": "E044", "paragraph_id": "P099", "quote": "是明了自己的人生价值，并全力以赴的加以努力，随时随地处在可以死而无憾的状态", "relation": "supports"},
    {"key": "E045", "paragraph_id": "P102", "quote": "向死而生，是人的勇气可能的最大的、也是最坚实的根底", "relation": "supports"},
    {"key": "E046", "paragraph_id": "P103", "quote": "真正保证你的安全感的，从来就不是什么武力或者实力", "relation": "supports"},
    {"key": "E047", "paragraph_id": "P104", "quote": "安全感来自勇气", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与人格", "安全与风险", "人际关系", "自然法／规律", "犯罪预防"],
   "issue_candidates": ["安全感的培养", "绝对安全观的成本", "安全感过剩与不足的伴生", "与自然规律的关系", "对专业犯罪者的震慑", "警觉心与社会嘲讽"],
   "text_function_candidates": ["答疑", "论说", "训诫", "经验总结", "驳论"],
   "object_candidates": ["货拉拉跳窗女生事件及嘲讽者", "专业犯罪者／专业掠食者", "公检法", "组织与家庭", "亿万富翁与独裁君主"],
   "working_keywords": ["安全感", "压舱石", "高成本的反应", "绝对安全观", "容纳意外", "自然规律", "此处不留爷，自有留爷处", "专业犯罪者", "断联", "Caritas", "正义", "达摩克利斯之剑", "警觉心", "向死而生", "勇气", "性感"]
  },
  "notes": "P002、P060 为 lexical 中的 link 节点（外链到作者另一篇回答及问答“爱到底是什么”），文字混入 text 流，形成 text/lexical 分段差异，故 structure.lexical.divergence=true；这两处不属本篇论证内容。P018 声明“安全来自两个方面”但只列出第一方面，第二方面无编号标题（结构缺口，已在 unresolved_questions 登记）。brief 与正文 P004 开头重复且被截断。无图片节点，status=read。"
 },
 "d558794b": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待「女人幽默会消减性感」？”，其中引号内的说法出自未具名的他者，提问者只是转述并询问看法，其自身立场未表明。作者不讨论该说法的真假，而是反过来质问持此说法的“男人”自己是否还剩性感，并以“性感即勇敢”作断语收束。全文极短（217 字），无标题、无图片、无引文块。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "把问题反过来问：觉得“女人幽默就会消减性感”的男人们自己是否还剩哪怕一丁点性感。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "讥讽这类人猥琐难当、面目可憎，没有挑挑拣拣的资格，怕是只剩“卖可怜”“唤醒母性”一条路。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "给出断语“性感即勇敢”，并称容不下女人幽默的软弱者没资格被称为成年人。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "以“未成年人”“作业写完没得”收尾，把对手贬为不该凑热闹的小孩。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "unknown", "modality": "asserted", "statement": "提问所引“女人幽默会消减性感”的说法是本文的反驳对象；该说法出自未具名者，提问者仅以引号转述。", "evidence": []},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "觉得“女人幽默就会消减性感”的男人们，自己是否还剩哪怕一丁点性感，作者以此反问否定其评判资格。", "evidence": ["E001"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在作者看来这类人猥琐难当、面目可憎，没有对女人性感与否挑挑拣拣的资格。", "evidence": ["E002", "E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这类人怕是只剩下“卖可怜”“唤醒母性”这条路可走。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "性感即勇敢。", "evidence": ["E005"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "连女人幽默都容不下的软弱者，不是有没有资格被称为男人的问题，而是没资格被称为成年人。", "evidence": ["E006"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以“未成年人在这凑什么热闹？”“作业写完没得？”讥讽持该说法者，暗指其不成熟。", "evidence": ["E007", "E008"]}
   ],
   "argument_steps": [
    "不回答原问题的真假，转而反问持论者自身是否还有性感（P001—P002）。",
    "以“猥琐难当、面目可憎”“没有挑挑拣拣的资格”贬斥对方（P003）。",
    "预言对方只剩“卖可怜”“唤醒母性”一条路（P004）。",
    "抛出断语“性感即勇敢”，并据“容不下女人幽默”判定其为软弱者、没资格被称为成年人（P005—P006）。",
    "以“未成年人”“作业写完没得”把对手贬为小孩作结（P007—P008）。"
   ],
   "concept_usage": [
    {"term": "性感", "meaning": "作者以“性感即勇敢”作界定，并把能否容下女人幽默与一个人是否性感挂钩", "evidence": "P005", "ambiguity": "仅一句断语，未论证勇敢与性感的关系"},
    {"term": "软弱者", "meaning": "作者用以指连女人幽默都容不下的人，与“性感即勇敢”相对", "evidence": "P006", "ambiguity": "未界定“软弱”的具体所指"},
    {"term": "成年人", "meaning": "作者用作资格判准：容不下女人幽默者没资格被称为成年人", "evidence": "P006", "ambiguity": "属贬抑性评价标准，未给出定义"},
    {"term": "母性", "meaning": "“唤醒母性”指此类男性只能靠博取怜悯获得关注，带讥讽", "evidence": "P004", "ambiguity": "系作者对反驳对象的讥讽性描述，非分析性用法"}
   ],
   "examples_and_targets": [
    "提问中引述的“女人幽默会消减性感”说法及其持有者“男人”们（作者的反驳对象，P002、P003）",
    "“卖可怜”“唤醒母性”（作者对反驳对象的讥讽性描述，P004）",
    "“未成年人”“作业写完没得”（作者对反驳对象的贬称与调侃，P007、P008）"
   ],
   "conditions": [
    "以“连女人幽默都容不下”作为判定软弱者／未成年人的条件（P006）",
    "全文为极短评论，未给出其他明说的场景、时间或程度限定"
   ],
   "rhetoric_and_tone": "极短的口语化回击，讥讽与训诫并存。开篇即以省略号与反问接手话题，连续反问（P001—P003）逼问对方资格；用“猥琐难当，面目可憎”“卖可怜”“唤醒母性”等贬语；以祈使句“记住了”抛出断语，再用“未成年人在这凑什么热闹？”“作业写完没得？”的师长口吻收尾，带明显的羞辱与调侃色彩。",
   "unresolved_questions": [
    "提问中引号内的“女人幽默会消减性感”出自何人、何种语境，question 未说明，作者亦未追问该说法来源",
    "作者称对方“猥琐难当，面目可憎”“只剩下卖可怜、唤醒母性”属贬抑评价，无事实依据可核（P003、P004）",
    "“性感即勇敢”未展开论证；“性感”“勇敢”的具体含义及二者关系本文未说明（P005）",
    "正文仅 217 字，provenance 为 null；updated_at（2021-05-15）晚于 published_at（2021-03-07），是否存在删改未说明",
    "文中未出现图片节点与结构标题，是否有配图或被删内容无法判断"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "觉得“女人幽默就会消减性感”的“男人”们自己还剩下哪怕一丁点性感吗？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "看着都觉得猥琐难当，面目可憎好吗？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "哪里还有什么挑挑拣拣的资格？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "怕是只剩下“卖可怜”“唤醒母性”这条路可走了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "记住了，性感即勇敢。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "连女人幽默都容不下的软弱者，不是有没有资格被称为男人的问题，而是没资格被称为成年人。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "未成年人在这凑什么热闹？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "作业写完没得？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别与两性话题", "幽默", "人格与成熟"],
   "issue_candidates": ["女人幽默是否消减性感", "男性评判女性性感的资格", "成年与成熟的标准"],
   "text_function_candidates": ["答疑", "驳论", "讥讽短文"],
   "object_candidates": ["持“女人幽默消减性感”说法的男性", "提问者"],
   "working_keywords": ["幽默", "性感", "性感即勇敢", "软弱者", "成年人", "母性", "卖可怜"]
  },
  "notes": "极短评论（217 字、8 段），无图片、无结构标题；提问引号内的说法属未具名他者，非提问者立场、更非作者立场，已单独记为 opponent_view（attribution=unknown）。文中“性感即勇敢”与同批 b4019eab《安全感》结尾“性感的根源是安全感”用语相呼应，但本篇未说明二者关系。"
 },
 "9519155b": {
  "analysis": {
   "question_context": "提问者（Q001）问“你们怎么看「若批评无自由，则赞美无意义」这句话？”，引号内的命题出自未具名的他者，提问者只询问看法，未表明自身立场。作者直接否证这句话：称从未见过“不被允许”的批评，并把冒批评之名的侮辱损害与之区分，又称赞美的实质意义本来有限、与批评自由无关，最后以“人需要的是追加投资”和“无意义的赞美”收尾。P002“为什么人们不喜欢被批评？”是 lexical 中的外链节点（指向另一回答），不属本篇论证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "断言批评从未“不被允许”，小到个人大到国家不允许批评就要灭亡，自然法则没给人“不允许批评的自由”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "外链节点“为什么人们不喜欢被批评？”，指向另一篇回答，非本篇论证内容。", "role": "other"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "把冒批评之名的“批评”界定为侮辱和损害，并否认存在侮辱与损害的合法自由。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P004", "P005"], "summary": "赞美天生实质意义有限，与批评自由无关；被真诚赞美的垃圾和蠢行比比皆是，赞美不是“正确加冕”，其“意义”被放大只因人类总体不成熟。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "判定该句是形式对称、朗朗上口而逻辑无效的空话，并指出其隐含“用批评自由换有意义赞美”的鬼逻辑。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P008", "P009"], "summary": "提出人需要的是“追加投资”而非赞美；只有嘴动而脚、手、钱不动，才叫“无意义的赞美”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "unknown", "modality": "asserted", "statement": "提问所引“若批评无自由，则赞美无意义”是本文否证的对象；该说法出自未具名者，提问者仅询问看法。", "evidence": []},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者没见过“不被允许”的批评；自然法则根本就没给人“不允许批评的自由”。", "evidence": ["E001", "E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "小到个人，大到国家，不允许批评就要灭亡。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "冒批评的名而行的“批评”实质上只是侮辱和损害，世上不存在侮辱与损害的合法自由。", "evidence": ["E004", "E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "赞美天生实质意义有限，与“批评”自由不自由没有关系。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被大量真诚赞美的垃圾和蠢行比比皆是；被赞美并不成其为任何意义上的“正确加冕”。", "evidence": ["E007", "E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "赞美的“意义”被搞得这么大只因人类总体的不成熟，并不是真得了赞美就怎么着了。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“若批评无自由，则赞美无意义”只是一句形式对称、朗朗上口，实际逻辑无效的空话。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这句话隐含着一个逻辑：似乎给予批评的自由是为了换得（也可以换得到）“有意义的赞美”。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人需要的不是赞美，而是追加投资。", "evidence": ["E012"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "脚上不动、手上也不动、钱上也不动而只有嘴动，这才叫“无意义的赞美”。", "evidence": ["E013"]}
   ],
   "argument_steps": [
    "先否证前提：批评从未不被允许，自然法则未给人禁止批评的自由（P001）。",
    "区分概念：冒批评之名的“批评”只是侮辱和损害，不存在这种合法自由（P003）。",
    "否证后半句：赞美本身实质意义有限，与批评自由无关；被赞美的垃圾与蠢行比比皆是，赞美不是“正确加冕”（P004—P005）。",
    "整体判定该句为逻辑无效的空话，并指出其隐含的交换逻辑（P006—P007）。",
    "以正面主张收束：人需要的是追加投资；只有嘴动的赞美才是“无意义的赞美”（P008—P009）。"
   ],
   "concept_usage": [
    {"term": "批评的自由", "meaning": "作者称从未见过“不被允许”的批评，并称自然法则没给人“不允许批评的自由”；同时把冒批评之名的侮辱损害排除在“批评”之外", "evidence": "P001", "ambiguity": "未给出区分“批评”与“侮辱和损害”的标准；P003"},
    {"term": "赞美", "meaning": "作者称其天生实质意义有限，不构成“正确加冕”，与批评自由无关", "evidence": "P004", "ambiguity": "未说明“意义”的具体衡量方式；P005"},
    {"term": "追加投资", "meaning": "作者用以替代赞美的正面要求，指脚、手、钱上的实际投入", "evidence": "P008", "ambiguity": "未说明投资的主体、对象与形式；P009"},
    {"term": "无意义的赞美", "meaning": "只有嘴动而脚、手、钱都不动的赞美，被作者作为该词的定义", "evidence": "P009", "ambiguity": "定义以列举方式给出，未覆盖其他情形"}
   ],
   "examples_and_targets": [
    "“若批评无自由，则赞美无意义”这句话（提问引述、作者否证对象，P001—P007）",
    "“为什么人们不喜欢被批评？”外链节点（指向另一回答，P002）",
    "被大量真诚赞美的垃圾和蠢行（作者论据，P005）",
    "冒批评的名而行的“批评”（作者指认的对象，P003）",
    "小到个人、大到国家（作者论据的适用范围，P001）"
   ],
   "conditions": [
    "以“小到个人，大到国家”为论断的适用范围（P001）",
    "“至于冒批评的名而行的‘批评’”这一限定：作者否定的是冒名者，不是批评本身（P003）",
    "“说实话”作为语气限定，标示作者的主观判断（P004）",
    "把赞美“意义”被放大的原因限定为“人类总体的不成熟”（P005）"
   ],
   "rhetoric_and_tone": "短评式论辩，反讽与断语并重。以“我还没见过”“事实上自然法则根本就没给人”等绝对化措辞直接否证；连续反问（“世上哪来侮辱与损害的合法自由？”“和‘批评’自由不自由有什么关系？”）拆解对方命题；用“昏头涨脑的鬼逻辑”“空话”“搞的这么大”等口语贬语；结尾以“脚上不动，手上也不动，钱上也不动，只有嘴动”的排比把抽象命题落为行动要求。",
   "unresolved_questions": [
    "P002“为什么人们不喜欢被批评？”为 lexical 中的 link 节点，指向另一篇回答（question/22987136/answer/1434894604），链接内容不在本篇范围",
    "骨架 paragraph_chars 显示 P002 结束与 P003 起始同在第 76 字符，text 与 lexical 在此处存在分段差异（structure.lexical.divergence=true）",
    "“自然法则根本就没给人‘不允许批评的自由’”为作者断言，未展开其自然法依据（P001）",
    "“追加投资”未说明投资的主体与形式（谁向谁投资、投资什么）（P008）",
    "“若批评无自由，则赞美无意义”的原始出处与语境 question 未说明，需外部核查",
    "updated_at 为 2026-03-06，远晚于 published_at（2021-03-07），是否存在后续增补或修改，本文未说明",
    "brief 与正文 P001、P003、P004 文字重复且同样被截断，brief 其余内容未在正文出现"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "这种批评，我还没见过“不被允许”的", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P001", "quote": "事实上自然法则根本就没给人“不允许批评的自由”", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P001", "quote": "小到个人，大到国家，不允许批评就要灭亡", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "至于冒批评的名而行的“批评”，实质上只是侮辱和损害", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P003", "quote": "世上哪来侮辱与损害的合法自由？", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P004", "quote": "至于赞美，说实话天生实质意义就有限，和“批评”自由不自由有什么关系？", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P005", "quote": "被大量真诚赞美的垃圾和蠢行比比皆是", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P005", "quote": "被赞美并不成其为任何意义上的“正确加冕”", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P005", "quote": "只是因为人类总体的不成熟而已，并不是真的得了赞美就怎么着了", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P006", "quote": "这只是一句说起来形式对称、朗朗上口，实际上逻辑无效的空话。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P007", "quote": "似乎给予批评的自由是为了换得（也可以换得到）“有意义的赞美”似的", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P008", "quote": "人需要的不是赞美，而是追加投资。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P009", "quote": "脚上不动，手上也不动，钱上也不动，只有嘴动，这才叫“无意义的赞美”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["言论与批评", "价值观与社会心理", "语言逻辑"],
   "issue_candidates": ["批评自由与赞美意义的关系", "批评与侮辱损害的界限", "赞美的实质意义", "追加投资对赞美的替代"],
   "text_function_candidates": ["答疑", "评论", "驳论"],
   "object_candidates": ["“若批评无自由，则赞美无意义”的持论者", "被赞美的垃圾和蠢行", "冒批评之名者"],
   "working_keywords": ["批评", "自由", "赞美", "正确加冕", "空话", "鬼逻辑", "追加投资", "无意义的赞美"]
  },
  "notes": "P002 为 lexical link 节点（外链至另一回答），text 中其文字与 P003 同段，导致骨架 P002/P003 字符范围在第 76 字符相接，属 text/lexical 分段差异，已在 notes 与 unresolved_questions 说明。本题命题出自提问引述、来源未具名，已单独记为 opponent_view（attribution=unknown），未归给作者。无图片节点，status=read。"
 },
 "c1e53f26": {
  "analysis": {
   "question_context": "提问者（Q001）问“怎样才能很好的平衡学习和玩的关系？”。作者不接受通常意义上的“平衡”提法：对真正的学习者而言学习本身就是玩，需要平衡的是沉浸学习对身体的损耗；对未能进入这种状态的孩子，父母该做的不是就比例讨价还价，而是提高其眼界与自身的鉴赏力，并警惕以“务实”为名否决精神追求的代际传递。文中 P012 引杜甫诗句（lexical 中为 quote 节点），作为“观者如山的荣耀”的例证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "很多人没能把学习变成高级的玩耍；对“天才”而言学习是自己设计和寻找关卡的通关游戏，其好玩耐玩远胜市面游戏，“天才”只是沉迷的结果。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "真正体会学习乐趣的人要平衡的是沉迷思考对身体的负担与损害，体育锻炼有助学习快感；学习本身就是玩，“玩”只为更好享受学（学将来被工作代替）。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "一般所谓“学与玩的平衡”是讨价还价设定公允比例，这种谈判没有意义，此时的“学”只是做样子给家长看；正确做法是换老师、换题材、换科目直到进入第一种境界。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "提高眼界、培养饥渴，带ta接触神人、观赏思维的艺术，使其看到观者如山的荣耀并升起敬畏；引杜甫诗句为例。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "喜欢斯金纳机式的“玩”是因为好东西见得少、心太窄、立志太低；而“看见好东西”不易，多数父母缺少欣赏所需的基本素养，这才是真正的问题。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023"], "summary": "道听途说带孩子接触往往“没觉得有啥好的”；看芭蕾、围棋、射箭都看不出功夫；这份看得见好东西的眼光是父母欠子女的学习债，父母鉴赏力决定子女志向的高度。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "对精神财富的麻木会传染，失去共鸣只剩感官比较，敌不过游戏、AV和毒品；感官刺激已工业化而需钱买单，于是追求变成搞更多钱；提供不了钱不能衡量的价值就只能比便宜比快，子女落入血腥红海，届时喊“内卷”“绝望”无人听。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "父母不知官能快感之外还有让灵魂颤抖的美是不行的；若自己无能为力至少要明白出路并闭嘴少说“不能吃的东西没有用”；“识货”的下一代有望在下下代培育“读书种子”；天才是【从对正确的东西上瘾】来的，妨碍天才的是化名“务实”的【文化上的性无能】，此“性”指神性。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P040", "P041", "P042"], "summary": "神性的享乐是本能追求，部落时代人类已能饿着肚子围篝火吟唱歌舞；因贫穷困苦否决精神追求是弃绝生而为人的高贵、把子女扭成野兽，每代子女本会随机出现转变趋势却被“务实”代代阉割。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "再穷的人也必有几百代先祖、曾有富有的几代，一经困窘又捡起“实用”论；这种“实用”论是可习得的遗传病，好一代荫庇两三代、坏一代祸害两三代；结尾反问并警告再说“不能吃有什么用”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "对“天才”而言，学习是自己设计和寻找关卡的通关游戏，其好玩、耐玩程度远胜市面上的游戏；“天才”只是沉迷这种游戏的自然而然的结果。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正体会到学习乐趣的人需要平衡的是沉迷探索和思考对身体造成的负担与损害。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学习本身就是玩，所谓平衡只是平衡超好玩的玩与没那么好玩的玩。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "“玩”只是为了更好地享受学（学的地位将来会被工作代替），若不是为这点价值，“玩”没有必要存在。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "一般所谓的“学与玩的平衡”是通过讨价还价设定公允比例，这种谈判没有意义。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这种谈判下的“学”只是浪费生命做样子给家长看，以维持家长“ta将来还有出息的可能性”的最后一点幻想。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若没能让子女体会学习本身的乐趣，应不断换老师、换题材、换科目直到其在某一门类进入这个境界，而不是启动“学与玩的平衡”谈判。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要提高子女的眼界、培养其饥渴，带其接触神人、近距离观赏思维的艺术，使其看到观者如山的荣耀并升起敬畏。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人喜欢斯金纳机式的“玩”，说到底是因为好东西见得少、心太窄、立志太低。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大部分父母缺少欣赏本身所需要的基本素养，这才是真正的问题。", "evidence": ["E012"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这一份看得见什么是好东西的眼光，是父母们欠子女的一份学习债。", "evidence": ["E013"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "父母拥有的鉴赏能力在很大程度上决定子女可能立下的志向的高度。", "evidence": ["E014"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对精神财富缺少心弦颤动的共鸣，这份麻木和漠然会传染给子女。", "evidence": ["E015"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "失去共鸣后剩下的全是比甜、比鲜、比大、比爽这些直通感官的东西，而在这方面比不过游戏、AV和毒品。", "evidence": ["E016"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "感官刺激已经工业化，享受只需给钱，于是人生追求变成搞更多的钱为更强感官刺激买单。", "evidence": ["E017"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提供不了钱不能衡量的价值，就只好去提供钱可以衡量的价值，一天到晚比别人更便宜、更快。", "evidence": ["E018"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这样子女终将落入只比成本、比利润、比效率的血腥红海与最长的天梯、最冷酷的绞肉机，届时喊“内卷”“绝望”无人听。", "evidence": ["E019", "E020"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为人父母却不知世上除官能快感之外还有什么能让灵魂颤抖的美，这其实是不行的。", "evidence": ["E021"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这不是要求父母现在就学会欣赏；若确实无能为力，至少要明白出路在这里，知道闭嘴不说或少说“不能吃的东西没有用”。", "evidence": ["E022"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这样下一代跨过天堑的难度会小一点，至少学得会识货；而“识货”的下一代很有希望在下下代培育出“读书种子”。", "evidence": ["E023"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "天才根本不是从“努力”来的，而是【从对正确的东西上瘾】上来的。", "evidence": ["E024"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正妨碍家族里出现天才的，是那个化名为所谓“务实”的【文化上的性无能】。", "evidence": ["E025"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里的“性”不是男女之性，而是人身上的神性；所谓“文化上的性无能”是神性的性无能。", "evidence": ["E026"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "神性的享乐是人的本能追求，即使在衣不蔽体、朝不保夕的部落时代，人类已能饿着肚子围着篝火吟唱歌舞。", "evidence": ["E027"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为贫穷困苦而否决一切精神追求的价值、视为“没用”，是弃绝生而为人的高贵，并要把子女都扭成野兽。", "evidence": ["E028"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一代子女都天生会随机出现转变的趋势和尝试，只是被“务实”一代一代地阉割了。", "evidence": ["E029"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种“实用”论是一种可以习得的遗传病：哪一代好了就可荫庇两三代，哪一代得了往往也要祸害两三代。", "evidence": ["E030", "E031"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以“你再说句‘不能吃有什么用’试试？”的反问收尾，警告这种论调的危害。", "evidence": ["E032"]},
    {"claim_id": "C029", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "引杜甫诗句“昔有佳人公孙氏，一舞剑器动四方。观者如山色沮丧，天地为之久低昂”，用作“观者如山的荣耀”的例证。", "evidence": ["E033"]}
   ],
   "argument_steps": [
    "否定前提：学习本可成为高级的玩耍，很多人只是没遇到好老师与际遇（P001—P002）。",
    "重新界定“平衡”：真正沉迷学习者要平衡的是身体损耗，“玩”只是为更好享受学（P003—P006）。",
    "反驳通行理解：把“学与玩平衡”当作比例谈判没有意义，那是做样子给家长看（P007—P009）。",
    "给出替代做法：换老师、换题材、换科目，直到进入以学习为玩的境界（P010）。",
    "如何培养：提高眼界与饥渴，接触神人与思维的艺术，引杜诗为证（P011—P012）。",
    "诊断成因：喜欢斯金纳机式的玩是见识少、立志低；父母缺少鉴赏素养是真正问题（P013—P016）。",
    "举例说明“看不见好东西”：芭蕾、围棋、射箭皆看不出功夫，这份眼光是父母欠的学习债（P017—P023）。",
    "后果推演：麻木传染→只剩感官比较→不敌游戏、AV、毒品→追求搞钱→落入成本与效率的血腥红海（P024—P031）。",
    "提出要求：父母至少要明白出路、闭嘴少说“没用”，使下一代学会“识货”（P032—P035）。",
    "归因升级：天才来自对正确的东西上瘾，妨碍天才的是化名“务实”的文化上的性无能（即神性的性无能）（P036—P039）。",
    "人性论据：神性享乐是本能，贫穷不能否决精神追求；每代子女本会尝试转变却被“务实”阉割（P040—P042）。",
    "结论：这种“实用”论是可习得的遗传病，代代相传；以反问警告收束（P043—P049）。"
   ],
   "concept_usage": [
    {"term": "学与玩的平衡", "meaning": "作者否认通常含义（按比例讨价还价），主张学习本身就是玩，需平衡的是学习与身体负担、以及超好玩的玩与没那么好玩的玩", "evidence": "P005", "ambiguity": "该词在文中同时指作者自己的用法与他所要反驳的“一般所谓”用法；P006、P007"},
    {"term": "天才", "meaning": "沉迷于“自己设计和寻找关卡”的学习游戏的自然而然的结果，而非从努力来的", "evidence": "P002", "ambiguity": "作者未给出识别标准，仅以“上瘾”与“识货”描述；P036"},
    {"term": "高级的玩耍／至高游戏", "meaning": "作者对学习本身的称呼，与市面游戏、斯金纳机式的“玩”相对", "evidence": "P001", "ambiguity": "属比喻性表述，未界定其与普通游戏的结构差异；P003"},
    {"term": "识货", "meaning": "看得见什么是好东西的眼光与鉴赏力，被作者称为父母欠子女的学习债", "evidence": "P022", "ambiguity": "未说明如何习得或衡量；P035"},
    {"term": "读书种子", "meaning": "由“识货”的下一代培育出的、实质意义上表现卓越的天才", "evidence": "P035", "ambiguity": "未说明是否为作者自造词及其确切标准"},
    {"term": "务实／实用论", "meaning": "“肚子都没填饱，还要搞这些没用的”式论调；作者称其为化名“务实”的文化上的性无能、可习得的遗传病", "evidence": "P037", "ambiguity": "作者把日常“务实”与特定论调等同，未区分其不同用法；P044、P045"},
    {"term": "神性／文化上的性无能", "meaning": "“性”不是男女之性，而是人身上的神性；“文化上的性无能”指以“务实”为名否决精神追求", "evidence": "P038", "ambiguity": "双关修辞，作者未给出“神性”的正面定义；P039"},
    {"term": "内卷", "meaning": "作者设想子女未来会喊的口号，作为其推演结果的表征", "evidence": "P031", "ambiguity": "未加定义，属引用式用法"}
   ],
   "examples_and_targets": [
    "杜甫诗句“昔有佳人公孙氏，一舞剑器动四方……”（作者引文，P012）",
    "芭蕾、围棋、射箭（作者举例：看不出其中的功夫，P018—P020）",
    "游戏、AV和毒品（作者类比：感官刺激的工业化产品，P026、P027）",
    "“获胜CG”（作者借游戏术语指廉价快感，P011）",
    "斯金纳机（作者类比廉价刺激机制，P013）",
    "部落时代饿着肚子围着篝火吟唱歌舞的人类（作者论据，P040）",
    "“读书种子”（作者用语，P035）",
    "血腥红海、最长的天梯、最冷酷的绞肉机（作者比喻，P030）",
    "官能快感与“能让灵魂颤抖的美”（作者的对立概念，P032）",
    "“不能吃的东西没有用”“不能吃有什么用”（作者反驳的“务实／实用”论调，P034、P049）"
   ],
   "conditions": [
    "“对于‘天才’而言”的限定（P002）",
    "“对于真正体会到学习这门至高游戏的乐趣的人而言”的限定（P003）",
    "“如果ta们够幸运”的假设（P004）",
    "“若不是为这点价值”的让步条件（P006）",
    "“如果你没能让子女体会到学习本身的乐趣”的条件（P010）",
    "“你如果确实自己无能为力，你至少要明白出路在这里”的退让条件（P033）",
    "“不论多么贫穷”的让步条件（P042、P043）",
    "“一经意外困窘”的条件（P044）",
    "“哪一代好了……哪一代得了……”的世代条件分布（P046、P047）"
   ],
   "rhetoric_and_tone": "训诫与激愤并存的教育评论，通篇第二人称“你”与“ta们”交替指向父母与子女。密集使用反问（“喊给谁听？”“有什么比得过游戏、AV和毒品呢？”“你们看懂这要害所在了吗？”“你再说句‘不能吃有什么用’试试？”）与咒骂式措辞（“这个狗娘养的‘务实’”）；以游戏术语（关卡、通关、获胜CG、毒瘾）重构学习体验，以双关（“文化上的性无能”“神性”）加重贬抑；引杜甫诗句提升“看见好东西”的庄严感；结尾以世代遗传病与反问施压。",
   "unresolved_questions": [
    "P012 引诗未标明出处与作者（杜甫《观公孙大娘弟子舞剑器行》），需外部核查",
    "“斯金纳机”（Skinner box）为外来术语，作者未解释其含义（P013）",
    "“【从对正确的东西上瘾】”“【文化上的性无能】”原文用方括号强调，是否对应平台强调格式或作者自加的着重，无法从文本确认（P036、P037）",
    "P011 中“那些神人”所指不明，作者未举例",
    "“哪一代好了，就可以荫庇两三代”等属作者的世代经验断言，无数据或案例来源（P046、P047）",
    "brief 与正文开头重合但不完整（末尾“对于真正体会到学习这门至”处截断），brief 其余内容未在正文出现",
    "updated_at（2021-05-15）晚于 published_at（2021-03-07），是否有修改未说明",
    "“读书种子”是否为作者自造词及其确切含义未定义（P035）",
    "“多接触那些神人”“观赏那些思维的艺术”未给出具体对象与途径（P011）"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "对于“天才”而言，“学习”是一种自己设计和寻找关卡的通关游戏", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "所谓的“天才”，只是沉迷这种游戏的自然而然的结果", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "需要平衡的是沉迷于探索和思考的乐趣而对身体造成的负担与损害", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "学习本身就是玩，这其实是在要求平衡超好玩的玩和没那么好玩的玩而已", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "“玩”只是为了更好的享受学（学的地位将来会被工作代替）", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "是想要通过讨价还价设定一个公允的“比例”", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "只是这样谈判，都意味这样的谈判没有意义", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "所谓的“学”只不过是浪费自己的生命做个样子给家长看", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "而是不断的再换老师、换题材、换科目，直到ta可以在某一个门类里进入这个境界为止", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "要提高ta的眼界，培养ta的饥渴", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P014", "quote": "说到底，其实是好东西见得少了，心太窄了，于是立志太低了", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P016", "quote": "而大部分父母们缺少欣赏本身所需要的基本素养，这才是真正的问题", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P022", "quote": "这一份看得见什么是好东西的眼光，其实是父母们欠子女的一份学习债", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "身为父母拥有的鉴赏能力，在很大程度上决定了子女可能立下的志向的高度", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "这份麻木和漠然是会传染给子女的", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P026", "quote": "而既然是这样，有什么比得过游戏、AV和毒品呢？", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P027", "quote": "这些东西已经工业化了，要享受只需要给钱就可以了", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P029", "quote": "你提供不了钱不能衡量的价值，你当然就只好去提供钱可以衡量的价值", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P030", "quote": "只比成本、比利润、比效率的血腥红海", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P031", "quote": "到时候再喊“内卷”，喊“绝望”，喊给谁听？", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P032", "quote": "为人父母，却不知世上除了官能快感之外还有什么能让灵魂颤抖的美，这其实是不行的", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P034", "quote": "你要知道闭嘴不说或者少说“不能吃的东西没有用”", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P035", "quote": "“识货”的下一代，就很有希望在下下代培育出出“读书种子”", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P036", "quote": "天才其实根本不是从“努力”来的，而是【从对正确的东西上瘾】上来的", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P037", "quote": "真正妨碍家族里出现天才的，是那个化名为所谓“务实”的【文化上的性无能】", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P038", "quote": "这里的性，不是男女之性，而是人身上的神性", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P040", "quote": "那些尚未成型的人类就已经可以饿着肚子围着篝火吟唱歌舞了", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P040", "quote": "自己要把自己活成野兽、而且要把子女都扭成野兽", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P042", "quote": "只是ta们一代一代的被这个狗娘养的“务实”给一代一代的阉割了", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P045", "quote": "这种“实用”论其实是一种可以习得的遗传病", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P047", "quote": "哪一代得了，往往也要祸害两三代", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P049", "quote": "所以，你再说句“不能吃有什么用”试试？", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P012", "quote": "昔有佳人公孙氏，一舞剑器动四方。观者如山色沮丧，天地为之久低昂。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育与学习", "家庭与代际传递", "审美与精神生活", "文化与价值观"],
   "issue_candidates": ["学与玩的平衡", "把学习变成游戏", "父母鉴赏力与子女志向", "感官刺激与精神追求", "务实论对天才的压制"],
   "text_function_candidates": ["答疑", "论说", "训诫", "经验总结", "批评"],
   "object_candidates": ["父母与子女", "天才／读书种子", "教师与科目", "游戏、AV、毒品等感官工业", "杜甫（引文作者）"],
   "working_keywords": ["学与玩", "高级的玩耍", "通关游戏", "斯金纳机", "鉴赏力", "识货", "学习债", "读书种子", "从对正确的东西上瘾", "务实", "文化上的性无能", "神性", "实用论", "内卷"]
  },
  "notes": "P012 为 lexical quote 节点（杜甫诗句），作者引以例证“观者如山的荣耀”，属 cited_source，未归为作者自述。正文无图片节点，status=read。brief 与正文开头重合但被截断于“对于真正体会到学习这门至”。文中“文化上的性无能”“神性”为作者双关修辞，已在 concept_usage 与 rhetoric 中注明，不作价值判断。"
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
