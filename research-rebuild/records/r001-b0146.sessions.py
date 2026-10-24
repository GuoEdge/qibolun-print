# -*- coding: utf-8 -*-
"""批次 r001-b0146 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0146.sessions.py            # 写 out/r001-b0146.out.jsonl
  python3 records/r001-b0146.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0146"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0146.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "d51ccb8e": {
  "analysis": {
   "question_context": "提问者（Q001）问：做错事无法得到对方的原谅怎么办。作者以答问者身份作答，先把“得不到原谅”分成联系未断与联系已断（绝罚）两种情形，再分别给出应对，最后把问题从“如何求原谅”改写为“痛苦能否结出有价值的果子”。提问者的具体处境（是否已被断绝联系、做错了什么）正文未交代，作者也未追问。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开篇分类：无法得到原谅分两种情况，其一是联系未断、交流资格未被取消。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "联系未断时不要追着对方改变主意（那是只顾自己的不高兴）；话可以说但间隔要久；每次接触都提此事会构成事实胁迫，对方可能表面配合、假意原谅。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "第二种情况：自身价值不足，对方直接翻脸并取消你的说话资格；“求原谅”求到彻底决裂往往是这条路线逼出来的。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "理由：所提供服务以对方不得有任何意见为前提，这种关系像随时会断的保险绳，故“原谅”在必要性上很欠奉；关系脆弱因此极其普遍，年轻人的友情爱情大概率崩溃。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020"], "summary": "技术性建议：不要一有疙瘩就追着求谅解，诚意体现在服务不减分毫；强迫性求原谅等于诱惑对方把谅解武器化，而武器化者并不自知；求谅解要适可而止、留出间隔。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023"], "summary": "以反问收束第一层建议：对方说的“需要空间”，很多情况下就是两次“原谅我”之间的空间。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "第二种情况的展开：绝罚令下强行联系令所传信息失去意义；此时怎么做是关系的真相时刻，无论打破禁制还是转向愤恨报复，都反证绝罚正确、证明关系是贪婪而非爱。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043"], "summary": "爱不以“分手”为结束，只是改为不见面的服务方式，首先意味着不贪、不恨（不控诉不纠缠、不仇恨不报复），且不在有指望时才恪守；这种一以贯之的坚守才是复合的最大希望。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051"], "summary": "要害：对方可能暗中观察，但你无从觉察与干预；机会绝对渺茫，因为为复合发信号会被识破，且对方可能另有障碍；故不能以争取复合为诉求，只能以“这本来就是我该做的改变”去努力。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060"], "summary": "可为复合做的铺路：一是承担原谅的义务（把原谅视为泛义务，实践上即自我反省与可被观察到的相配行动），二是保持对方沟通的通道畅通；能做到的极限是路平门开。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074"], "summary": "结论转向：真正的问题不是如何求得原谅（原谅是自然法规定的人类义务），而是受苦者的痛苦结出了什么果子；不能原谅的是痛苦被白白浪费，而它是否有价值取决于你接下去怎么做。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无法得到对方的原谅分两种情况：联系未断、交流资格未取消；以及联系已切断、绝罚令已下。", "evidence": ["E1", "E2", "E24"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "联系未断时不要追着对方改变主意，因为那实际考虑的是你自己的不高兴，而不是对方的不高兴。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方没有取消你说话的资格，该说的可以说，但频率要隔久一点；绝对不可以每次接触开口就提这件事。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每次接触都提此事会构成事实上的胁迫，对方可能因忌惮而勉强满足要求，也可能假意原谅、配合演出以避免引起你的警觉。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二种情况是自身价值不足以致对方直接翻脸、连说话资格一并取消；“求原谅”求出彻底决裂，往往是走这条路线逼出来的。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类关系中你提供的一切服务都以对方不能有任何意见或“误会”为前提，一旦对方有你不能接受的想法服务即暂停，因此它更像随时会断的保险绳，而不是可依赖的依靠。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果原谅不被当作为人必需追求的义务，则由于人都有幼稚阶段，这种关系脆弱极其普遍，年轻人之间的友情与爱情往往昙花一现、大概率崩溃。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术层面上绝对不要一有疙瘩就追着求谅解；真正的诚意体现在“即使有分歧，出于关系责任该提供的服务不减分毫”。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若强迫性地必须求得原谅才能继续，事实上是在诱惑对方把谅解武器化；而这样的人不会明确意识到自己已在武器化谅解，只是享受控制感、决断感和受宠爱感。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "求谅解要适可而止、要有间隔频率，让中间的时间与事情去呈现你的变化和对方误解的可能，关系才能越走越强。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "对方常说的“需要空间”，在很多情况下就是两次“原谅我”之间的空间。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绝罚令已下时凡联系即为不爱的绝对证明；强行联系这一事实本身就使你想传递的信息失去意义，无法用证明不爱的方式传递爱的证据。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被绝罚后，无论是不顾一切打破禁制还是转向愤恨报复，都在证明绝罚你是绝对正确的决定，证明这关系不是爱而是贪婪。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱根本没有尽头、不以“分手”为结束，只是从在一起的服务方式改为不见面的服务方式；它首先意味着不贪、不恨，即不控诉不纠缠、不仇恨不报复，且在没有指望时仍要恪守。", "evidence": ["E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果还有复合的希望，恰恰是这种一以贯之的原则坚守才是最大的希望；对方看得懂必然会看重，看不懂你也可以释怀。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "即使对方下了绝罚令，客观上往往也有一段你不会觉察的观察期，仍有可能改变其想法，但机会绝对渺茫：为复合发送信号会被识破而适得其反，且对方可能另有障碍，你无从干预。", "evidence": ["E24", "E25"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你不能以争取复合机会为诉求去努力，而必须以“无论是否能造成复合，这都是我该做的改变”的心态去努力。", "evidence": ["E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可为复合铺路的第一件事是承担原谅的义务：把原谅视为生而为人必须努力去做的泛义务，既为义务就无所谓交换与企图。", "evidence": ["E27", "E28"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "引为义务的原谅在实践上就是自我反省（多想自己可以做得不一样、更好），并让对方能观察到与反省相匹配的实际行动，由行动的真实性证明忏悔与原谅的真实性。", "evidence": ["E29", "E30"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二件事是保持对方沟通的通道畅通：对方关闭渠道是对方的自由，你没有关闭就已表明对和好的开放心态，能做到的极限是路平门开。", "evidence": ["E31"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“原谅”与“宽恕”不同：原谅的人不说“你的罪免了”（那是宽恕），而说“这怪我”。", "evidence": ["E32"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题不是怎样求得人的原谅——原谅人是自然法规定的人类自己的义务，本不需要去求；真正的问题是有人受了苦，这些痛苦到底结出了什么果子。", "evidence": ["E33", "E34"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正不能原谅的是痛苦被浪费、只纯然造成伤痕而无任何积极结果；这份恩怨会成为无谓的痛苦还是让人觉得“也不枉我受这一场”，完全取决于你接下去怎么做。", "evidence": ["E35", "E36"]}
   ],
   "argument_steps": [
    "定义/分类：把“无法得到原谅”分为联系未断与联系已断（绝罚）两种情况（P001—P002）。",
    "情形一前提：对方没有取消你说话的资格，所以话可以说，但不能追着对方改变主意（P003—P004）。",
    "理由：追着要求对方改变主意，考虑的其实是自己的不高兴（P003）。",
    "禁止与后果：不可每次接触都提此事；这会构成事实胁迫，可能招致勉强应付或假意原谅（P005—P006）。",
    "情形二：价值不足时对方直接翻脸、取消说话资格；“求原谅”逼出彻底决裂（P007—P009）。",
    "理由支撑：服务以对方不得有意见为前提，关系如随时会断的保险绳，故原谅的必要性欠奉（P010—P012）。",
    "推论：在不把原谅当义务的条件下，关系脆弱普遍，年轻人的友情爱情大概率崩溃（P013—P014）。",
    "技术性建议：不要一有疙瘩就追着求谅解，诚意体现在服务不减分毫（P015）。",
    "另一层理由：强迫性求原谅会诱惑对方把谅解武器化，且武器化者不自知（P016—P018）。",
    "行动准则：求谅解适可而止、留间隔，让时间与事情去呈现变化（P019—P020）。",
    "反问式收束：不累吗？对方要的“空间”就是两次“原谅我”之间的空间（P021—P023）。",
    "绝罚情形展开：凡联系即为不爱的绝对证明，强行联系使信息无意义（P024—P027）。",
    "设问与回答：是否毫无办法？此时怎么做是真相时刻；打破禁制或报复都反证绝罚正确、证明是贪婪而非爱（P028—P034）。",
    "正面主张：爱不以分手结束，改为不见面的服务方式，首先意味着不贪、不恨，且无指望时仍须恪守（P035—P039）。",
    "条件性结论：若还有复合希望，一以贯之的坚守就是最大希望；对方看懂与否各有其果（P040—P043）。",
    "要害说明：对方可能暗中观察，但你无从觉察与干预，机会绝对渺茫（P044—P050）。",
    "心态要求：不以争取复合为诉求，而以“这是我该做的改变”去努力（P051）。",
    "落地措施一：承担原谅的泛义务 → 自我反省 → 可被观察到的相配行动（P052—P058）。",
    "落地措施二：保持沟通通道畅通，路平门开即为极限（P059—P060）。",
    "转折：本文与其说在谈原谅，不如说在谈复合；真正的问题不是求原谅（P061—P063）。",
    "结论：关键是受苦者的痛苦结出了什么果子；不能原谅的是痛苦被浪费，而价值取决于你接下去怎么做，你还有一辈子时间让它有价值（P064—P074）。"
   ],
   "concept_usage": [
    {"term": "两种情况的划分", "meaning": "以“联系是否还通、说话资格是否被取消”为界，把求原谅的处境分为可沟通与已被绝罚两类。", "evidence": "P001", "ambiguity": "分类标准未明说是否穷尽，也未说明两种情形是否会互相转化。"},
    {"term": "绝罚（绝罚令）", "meaning": "对方收回你主动联系的一切许可，凡联系即被视为不爱的绝对证明。", "evidence": "P024", "ambiguity": "作者自设术语，未说明其与宗教绝罚的关联，也未给出判定“令已下”的标准。"},
    {"term": "事实的胁迫", "meaning": "并非明言威胁，而是以暂停既有关系中的一切服务为实际压力，逼对方满足要求。", "evidence": "P005", "ambiguity": "与普通坚持诉求的界限未给出判定标准。"},
    {"term": "将谅解武器化", "meaning": "当“给不给谅解”能兑换成巨大权力时，人性中的贪婪使人把谅解当作控制手段，且当事人并不自知。", "evidence": "P016", "ambiguity": "如何区分“正当的边界”与“武器化”，作者未给标准。"},
    {"term": "泛义务", "meaning": "原谅被视为生而为人就必须努力去做的普遍义务，因而是义务就无所谓交换与企图。", "evidence": "P053", "ambiguity": "义务的来源（自然法）未加界定，义务的范围与限度亦未说明。"},
    {"term": "原谅 / 宽恕", "meaning": "作者区分二者：宽恕是说“你的罪免了”，原谅是说“这怪我”，即回到自身的反省。", "evidence": "P058", "ambiguity": "该区分是作者的界定，未引用出处，也未讨论日常用法是否一致。"},
    {"term": "保险绳", "meaning": "比喻这种随时会因对方有意见而中断的关系：想登山时第一念头就是换一根靠谱的。", "evidence": "P011", "ambiguity": "比喻的适用边界未说明。"},
    {"term": "真相时刻", "meaning": "被绝罚之后你的选择，才暴露你是什么人、这关系究竟是什么关系的时刻。", "evidence": "P030", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "登山换保险绳：类比材料，用来说明随时会断的关系不可依赖（P011）。",
    "“动辄相互升级到核战争炸得白茫茫一片真干净”：夸张比喻，形容关系冲突的互相升级（P020）。",
    "“空气中隐约浮现地狱”：修辞意象，用于描述谅解被武器化后的局面（P018）。",
    "对方常说“需要空间”：被引用的常见说法，作者将其重新解释为两次求原谅之间的空间（P022—P023）。",
    "“只要你开心就好”：被作者判定在绝罚时刻被证明完全是骗人的说法，属被反驳的修辞材料（P033）。",
    "年轻人之间的友情与爱情：作者泛指的经验现象，用作关系脆弱论断的例证（P014）。",
    "“自然法”：作者援引的规范来源，作为原谅是义务的依据（P063）。"
   ],
   "conditions": [
    "全篇以“联系是否已断、说话资格是否被取消”为前置条件区分两种情形（P001—P002）。",
    "若原谅不被当作为人必需追求达成的义务，则关系脆弱极其普遍、年轻人的情感大概率崩溃（P013—P014）。",
    "若你强迫性地必须求得原谅才能继续function，就会诱惑对方将谅解武器化（P016）。",
    "如果还有复合的希望，一以贯之的坚守原则才是最大的希望；对方看得懂会看重，看不懂你也可以释怀（P040—P042）。",
    "即使对方下了绝罚令，客观上往往也有一段时间的暗中观察，因此并非绝对没有机会，但机会绝对渺茫（P045—P046）。",
    "渺茫的两个条件：对方若看出你是在利用其观察惯性为复合发信号，会适得其反；对方即使改变看法，也可能面对分手时的狠话或已身陷别的人生情节等障碍（P048—P049）。",
    "你无途径觉察、也无途径干预这种暗自的观察（P050）。",
    "努力的心态条件：不以能否复合为诉求，而以“这是我该做的改变”为前提（P051）。",
    "例外/极限条件：对方关闭沟通渠道是对方的自由，你能做的极限只是路平门开（P059—P060）。"
   ],
   "rhetoric_and_tone": "通篇第二人称“你”直接对话，训诫与开导并用。以设问、反问推进（“这个时候是不是已经毫无办法了呢？”“就不谈伤害，难道不累吗？”“对方不是常说‘需要空间’吗？”）；用“绝对不可以”“绝对不要”“绝对渺茫”等强断言与“往往”“大概率”“极可能”等限定语交错。大量比喻与夸张：保险绳、核战争、地狱、真相时刻。以引号标注对方话语（“原谅我”“需要空间”“只要你开心就好”“大彻大悟”式的价值判断）并加以重新解释或反驳。结构上先分类、再给技术建议、最后把问题从“求原谅”翻转为“让痛苦有价值”，结尾三段短句收束，语气冷峻克制。",
   "unresolved_questions": [
    "提问者究竟处于哪种情形、做错了什么、对方是否已下“绝罚令”，正文未作交代，作者也未追问。",
    "“自然法规定的人类自己的义务”一语未给出处或论证，其规范来源与约束力待外部核查。",
    "“很多人”“一般来说”“往往是”等经验概括没有数据或案例来源，无法核实。",
    "“绝对渺茫”与“并非绝对的没有机会”“最大的希望”之间存在张力，作者未给出可判定的标准。",
    "标题“求之不得”与正文内容的对应关系未在文中说明。",
    "平台元数据显示 updated_at（2025-01-05）晚于 published_at（2021-07-26），是否有后续修订无法从正文判断。",
    "作者身份与作答资格未在正文交代。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "无法得到对方的原谅，分两种情况。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "一种是联系没有断，交流的资格没有取消。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这种情况不要去追着对方改变主意", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "那么你该说的可以说，但是你频率隔久一点。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "绝对不可以“每次接触，开口就是这个事”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这会构成一种事实的胁迫", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "第二种情况就是你的价值并不足够，于是直接翻脸", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "人“求原谅”求出彻底决裂，往往是走这条路线逼出来的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "你所提供的一切服务，都建立在对方不可以对你有一点意见、一点“误会”的前提下。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "不如说是随时会断的保险绳", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "“原谅”你至少在必要性方面就很欠奉。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "所以年轻人之间的友情也罢、爱情也罢，往往昙花一现，大概率是要崩溃的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "绝对不要一有疙瘩就追着求谅解。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "那么你事实上也在诱惑对方将谅解武器化。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "所以，求谅解要适可而止，要有间隔频率", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "需要的就是你两次“原谅我”之间的空间。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "绝罚令已下，凡联系，即为不爱的绝对证明。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P027", "quote": "你无法合乎逻辑地用“证明不爱的方式”去传递“爱的证据”", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "都是在彻彻底底地证明一件事——绝罚你是绝对正确的决定。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "因为这样的行为就是在实实在在地证明你与对方的关系不是爱，而是贪婪罢了。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P035", "quote": "爱这件事，是根本没有尽头的，根本就不会以“分手”为结束。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "不控诉、不纠缠，是为不贪；不仇恨、不报复，是为不恨。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P040", "quote": "恰恰是这种一以贯之的坚守原则才是最大的希望。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P045", "quote": "客观上往往也有一定的概率会保持一段时间的观察", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P048", "quote": "还会对这惊人的贪婪和欲望感到恐惧和庆幸，反而适得其反。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P051", "quote": "而必须以“无论是否能造成复合，这都是我该做的改变”的心态去努力。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P053", "quote": "而是将原谅视为一种生而为人就必须努力去做的“泛义务”。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P054", "quote": "只有被引为义务的原谅，才是他人可以承受的原谅", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P055", "quote": "而“引为义务的原谅”在实践上就是自我反省", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P056", "quote": "觉得自己的错误是身体差，那就应该会观察到你在锻炼身体。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P059", "quote": "保持对方沟通的通道畅通。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P058", "quote": "原谅的人，并不说“你的罪免了”——那是宽恕，而非原谅。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P063", "quote": "原谅人是自然法规定的人类自己的义务", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P064", "quote": "真正的问题，是有人受了苦，而这些痛苦到底结出了什么果子。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P068", "quote": "真正不能原谅的，是这份痛苦被浪费了", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P069", "quote": "完全取决于你接下去怎么做。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系", "情感伦理", "道德哲学", "沟通策略", "修身与自我要求"],
   "issue_candidates": ["求原谅的边界", "绝罚与断绝联系", "道德胁迫", "谅解武器化", "复合的可能性", "原谅的义务", "痛苦的价值"],
   "text_function_candidates": ["答问体", "分情况论证", "行动建议", "伦理训诫", "概念区分"],
   "object_candidates": ["原谅", "绝罚令", "事实的胁迫", "泛义务", "保险绳比喻", "空间", "自然法"],
   "working_keywords": ["原谅", "绝罚", "复合", "胁迫", "武器化", "泛义务", "不贪不恨", "空间", "痛苦的价值"]
  },
  "notes": "无图片节点，全文已完整读取，status=read。提问字段（Q001）仅作语境，正文未复述提问；作者主张与提问者问题已区分。待外部核查：文中“自然法”义务说无出处；“很多人/一般来说/往往”类经验概括无来源；平台 updated_at 晚于 published_at，正文未见修订标记。"
 },
 "5a49c3ea": {
  "analysis": {
   "question_context": "提问者（Q001）问：如何理解“道德绑架”。作者以答问者身份给出判定标准（是否使用你同意或至少不反对的规范），随后批评把“道德绑架”当作武器、事前不声明自己规范的人，并说明该罪名要成立所需的前提与越线的代价。提问者本人的经历、立场与具体场景正文未交代。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出判定标准：用你自己同意或至少不反对（含不敢反对）的道德规范要求你，不算道德绑架；只有用你没同意过、尤其你明确反对过的规范要求你，才算。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "指出常见的滥用流程：事前不吭声，事中事后再以受害人姿态指责他人“擅自”按其个人理解替ta做决定，给人冠上道德绑架罪名；作者评价这叫不知死活。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011"], "summary": "理由：按该指责所指向的新规范，合作必须一切先请示，但指责者往往没有能力声明自己的规范；结果照一般规矩来被称道德绑架，照ta的规矩来又说不出方案。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017"], "summary": "反事实对照：若事前公开声明“不默认支持既有规范、一切具体协商”也算好汉、可让人提前避雷；但这类人实际选择不声明，以“保留最大的灵活性”，事后再说“是你自己猜的”。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "后果：好人ta做、罪别人扛（扛的还是“道德绑架”这大罪名）；干这种事被发现基本是社交死刑，且最爱用这套的偏偏是最没社会地位、扛不起敌对的小孩子。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "结论与告诫：该罪名要逻辑有效成立，必须先大声声明自己不接受一切默认道德并承担后果；否则最多只能说“往下不能继续接受，已发生的我认账”；越线多走一步，倒霉的是自己，且会被众人拉进“不可合作清单”，很可能失去圈子里的前途。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用你自己同意的、或你自己不反对（包括不敢反对）的道德规范要求你，不叫道德绑架。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有对方用你没同意过、尤其是你明确反对过的道德规范来要求你，才算道德绑架。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "常见流程是：事前不吭声，到了事中、事后再以受害人姿态指责他人“擅自”按对通用规范的个人理解替自己做决定，给人冠上道德绑架的罪名。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把上述做法称为不知死活，因为按这一指责指向的新规范，要与ta合作就一切都要先请示ta，而不能假定可按自己理解的社会规范来。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样做的人往往不会、甚至根本没有能力声明自己的规范；照一般规矩来被称作道德绑架，照ta的规矩来ta事前不说、事中也说不清，只说不爽，对连带后果既不清楚也没方案。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若有人公开有言在先，声明不默认支持世间一切既有规范、一切具体事务一律具体协商，那也算条好汉，别人至少可以提前避雷。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者以戏仿口吻转述这类人的实际选择：不声明、也不否认自己遵从默认规范，理由是说了就没人跟自己玩，要“保留最大的灵活性”，事后则说“是你自己猜我会按默认规矩来”。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "其结果是好人由ta做、罪由别人扛，扛的还是“道德绑架”这个天大的罪名。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "干这种猥琐的事被人发现，基本上是唯一的社交死刑；最可悲的是偏偏最没社会地位、最扛不起别人敌对的小孩子们最爱这套作死棍法。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要让“道德绑架”这一罪名逻辑有效地成立，你必须首先大声声明自己默认不接受一切被他人认为默认成立的道德，并腰杆挺直、正面承受这样做的后果。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "否则你最多只能说：这规则我有不同意见，往下不能继续接受，但已经发生的我认账。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "越过这条红线再多走一步，倒霉的一定是自己；而且不止被棍法打中的那一个，所有相信那人胜过相信你的其他人都会把你拉进“不可合作清单”。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "这很可能一次性导致你失去在这个圈子里的前途，不得不换个地方重新开始。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "定义：以“规范是否为你所同意或至少不反对”划定道德绑架的成立范围（P001—P002）。",
    "设问：很多人指责别人道德绑架自己的流程是什么样（P003）。",
    "描述流程：事前不吭声，事中事后再以受害人姿态指责他人“擅自”替ta做决定并冠以罪名（P004）。",
    "评价与理由：这叫不知死活，因为该指责等于要求合作时一切先请示ta（P005—P007）。",
    "指出对方的能力缺口：这样做的人往往无法声明自己的规范（P008）。",
    "推演困境：照一般规矩来被称道德绑架，照ta的规矩来ta说不清且无方案（P009—P011）。",
    "反事实对照：公开有言在先的人也算好汉，别人至少可提前避雷（P012—P013）。",
    "戏仿对方口吻揭示真实动机：不声明是为了保留最大的灵活性，事后推说“是你自己猜的”（P014—P017）。",
    "后果判断：好人ta做、罪别人扛；被发现基本社交死刑，常用者恰是最弱势的小孩子（P018—P021）。",
    "成立条件：要逻辑有效地指控道德绑架，必须先公开声明不接受默认道德并承担后果（P022）。",
    "退一步的说法：否则最多只能声明“往下不能继续接受、已发生的认账”（P023）。",
    "告诫与预测：越线多走一步倒霉的是自己，且会被众人列入“不可合作清单”，很可能失去圈子里的前途（P024—P026）。"
   ],
   "concept_usage": [
    {"term": "道德绑架", "meaning": "作者限定为：对方用你没同意过、尤其是你明确反对过的道德规范来要求你。用你同意或不反对（含不敢反对）的规范要求你，不算。", "evidence": "P002", "ambiguity": "“不反对”与“不敢反对”如何认定未说明；沉默是否等于同意恰是作者批评的争点。"},
    {"term": "默认规范 / 既有规范", "meaning": "社会中被默认成立、可不经声明即适用的道德与交往规则。", "evidence": "P012", "ambiguity": "范围与内容未列举。"},
    {"term": "保留最大的灵活性", "meaning": "既不声明遵从也不声明不遵从默认规范，以便事后按需选择立场。", "evidence": "P016", "ambiguity": "作者以戏仿口吻转述，未说明此种心态的普遍程度。"},
    {"term": "不可合作清单", "meaning": "众人（不止被指责者）共同把滥用道德绑架指责的人列入的排斥名单。", "evidence": "P025", "ambiguity": "作者设想的社交机制，未给出实例。"},
    {"term": "社交死刑", "meaning": "被发现有此类行为后在社会交往中基本失去信任与机会。", "evidence": "P019", "ambiguity": "程度由“基本上”限定，无界定标准。"},
    {"term": "作死棍法 / 五郎八卦棍", "meaning": "比喻把“道德绑架”这一罪名当作随意挥舞的攻击武器。", "evidence": "P019", "ambiguity": "纯修辞用法。"}
   ],
   "examples_and_targets": [
    "拟制的公开声明“我这人脾气怪，有言在先，世间一切的既有规范我都不默认支持，一切具体事务一律具体协商”：反事实假设，用来对照实际做法（P012）。",
    "“不，爷才不要”“我可不傻，我不说”“谁叫你乱猜？”：作者戏仿被批评者口吻的自述，属修辞材料而非作者主张（P014—P017）。",
    "“五郎八卦棍”“这作死棍法”“拿着这根大棒”：比喻，指滥用道德绑架指责的行为（P019、P021、P024）。",
    "“活活打成蝴蝶结”：夸张比喻，形容遭到报复的后果（P020）。",
    "“最没社会地位、最扛不起别人敌对的小孩子们”：作者泛指的群体，用作该做法最流行于弱者的论断例证（P021）。",
    "合规说法“且住，这规则我有不同意见，我往下不能继续接受，但已经发生的我认账。”：作者给出的可接受表述（P023）。",
    "“不可合作清单”：作者设想的社交排斥机制（P025）。"
   ],
   "conditions": [
    "判定前提：以该规范是否为你同意或至少不反对为界（P001—P002）。",
    "对方指责成立的条件：该规范必须是你没同意过、尤其你明确反对过的（P002）。",
    "反事实条件：若事前公开声明不默认支持既有规范，别人至少可以提前避雷（P012—P013）。",
    "实际不做声明的动因条件：怕这样说了没人跟自己玩，故要保留最大的灵活性（P014—P016）。",
    "“道德绑架”罪名逻辑有效成立的前提：必须首先大声声明并且正面承受后果（P022）。",
    "未做声明时的上限：只能说“往下不能继续接受，已发生的我认账”（P023）。",
    "风险条件：越过红线多走一步，倒霉的一定是自己，且排斥来自所有相信对方胜过相信你的其他人（P024—P025）。",
    "可能性限定：“这很可能一次性就导致你失去在这个圈子里的前途”（P026）。"
   ],
   "rhetoric_and_tone": "讽刺戏仿与训诫并用。大量粗俗口语与自夸口吻（“老子”“爷才不要”“我可不傻”）用于模拟被批评者的心声；反问与设问推进（“为啥？”“你怕爷不知道这样说了没人跟我玩了么？”“谁叫你乱猜？”）；比喻密集（五郎八卦棍、作死棍法、大棒、打成蝴蝶结、社交死刑、不可合作清单）；结尾转为“实实在在的奉劝你”的告诫式语气，并有黑色幽默（P021）。",
   "unresolved_questions": [
    "“你自己同意”“不反对（包括不敢反对）”缺少认定方式：沉默或未反对是否等于同意，与作者批评的“事前不吭声”之间存在张力，正文未处理。",
    "“很多人”“往往”“基本上”“很可能”等经验与程度概括无数据或案例来源，无法核实。",
    "提问者的具体经历与提问语境未交代，回答未复述提问。",
    "“默认规范”的内容与范围未列举，也未说明不同圈子（P026的“圈子”）间规范冲突时如何判定。",
    "作者给出的合规说法（P023）与道德绑架成立条件（P001—P002）之间的边界未进一步说明。",
    "平台元数据 published_at 与 updated_at 仅差二十余秒，是否有修订无法判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "用你自己同意的或者你自己不反对（包括不敢反对）的道德规范要求你，不叫道德绑架。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "只有对方用你没同意过、尤其是你明确反对过的道德规范来要求你，这个才算道德绑架。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "事前不吭声，到了事中、事后再以受害人的姿态指责他人“擅自”按照对通用规范的个人理解替ta做决定", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这叫不知死活。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "要和ta合作就一切都要先请示ta的意见而不能假定可以按照你自己理解的社会规范来。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "但是这样做的人却往往不会——甚至根本就没有能力——声明ta自己的规范。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "照ta的规矩来，ta事前不说，事中问ta，ta也说不清", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "世间一切的既有规范我都不默认支持，一切具体事务一律具体协商", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "这也算条好汉，别人至少可以提前避雷。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "你怕爷不知道这样说了没人跟我玩了么？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "“保留最大的灵活性”，岂不美哉。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "是你自己猜我会按默认规矩来，我啥时候说过呢？谁叫你乱猜？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "好人都是ta做了，罪都是别人扛", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "干这种猥琐的事被人发现，基本上唯一社交死刑。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "最可悲的是，还偏偏就是最没社会地位、最扛不起别人敌对的小孩子们最爱这套作死棍法", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P022", "quote": "你必须要首先大声说出来——“老子默认不接受一切你们认为默认成立的道德”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "这规则我有不同意见，我往下不能继续接受，但已经发生的我认账。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "拿着这根大棒，越过这根红线，往前再多走一步，倒霉的一定是你自己。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P025", "quote": "而是所有相信这人胜过相信你的其他人都会一起把你拉进“不可合作清单”。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P026", "quote": "这很可能一次性就导致你失去在这个圈子里的前途，不得不换个地方重新开始。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["道德哲学", "社会交往规范", "语言与指责行为", "社会排斥机制"],
   "issue_candidates": ["道德绑架的判定标准", "默认规范的约束力", "事前声明与事后追责", "社交排斥与不可合作清单"],
   "text_function_candidates": ["答问体", "概念界定", "反讽戏仿", "行为告诫"],
   "object_candidates": ["道德绑架", "默认规范", "社交死刑", "不可合作清单", "保留灵活性"],
   "working_keywords": ["道德绑架", "默认规范", "事前声明", "社交死刑", "不可合作清单", "灵活性"]
  },
  "notes": "无图片节点，全文已完整读取，status=read。提问字段（Q001）仅作语境，正文未复述提问；P012—P017 为作者戏仿对方口吻的反讽转述，已按 author_reported 处理，未计为作者主张。待外部核查：文中“很多人/往往/基本上/很可能”类经验与程度概括无来源；“不反对（包括不敢反对）”的认定标准未给出。"
 },
 "ee657bec": {
  "analysis": {
   "question_context": "提问者（Q001）问的是中美天津会谈（2021年7月26日）谈了哪些内容、还有哪些信息值得关注。作者的回答没有复述会谈内容，而是直接评论中美博弈态势：判断中国正逼美国在被动局面下升级冲突，并论证美国既打不起仗、也脱不了钩。提问者的信息需求（会谈具体内容）正文未回应，正文也未点名“天津会谈”，只以“中国”“美国”指称。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者判断中国当前的策略是逼迫美国在被动局面下升级冲突，并称升级到军事冲突也无不可。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "理由：这是傲慢者/小霸王的软肋——只要不服软就自然构成“挑衅”，若霸主升级不了打击或升级无效，霸权地位就难以不动摇。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "引申为格言式告诫：做人不能太嚣张、话不能说太满，否则会被挤兑得出乖露丑，一次败局就会卷堂大散。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "技术判断：高超音速中程导弹与隐身战略轰炸机的组合意味着海权国家时代落幕、陆权国家时代到来，区别只在是否留有体面。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009"], "summary": "条件推演：若美国不收缩调门，中国的回应会让美国不打一仗、不彻底脱钩就无法服众；但打仗没有可行方案，脱钩更是幻想。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012"], "summary": "以两组对照设问论证脱钩不可行：完整工业体系去高端尚可运转、去低端则崩溃；供应与消费之间，兵荒马乱时生产者比消费者能熬寒冬；末句以“真的是活该”作评。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国现在的策略是逼迫美国在被动局面下升级冲突。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在作者看来，升级到军事冲突也无不可。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这是傲慢者的软肋、小霸王的死穴：只要不服软就自然构成“挑衅”；如果霸主升级不了打击、或升级了打击起不到明显作用，霸权地位想不动摇也难。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "由此得出的告诫是：做人不能太嚣张、不能把话说太满，否则容易被人挤兑得出乖露丑；出乖露丑又收拾不了局面，一次真正的败局就会卷堂大散。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "高超音速中程导弹和隐身战略轰炸机的组合已经意味着海权国家的时代落幕，未来是陆权国家的时代、无可阻挡，区别只有下台是否留有体面。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "如果美国不收缩调门、不收敛自己的高姿态攻势，中国的回应会越来越让美国不打一仗、不彻底脱钩就无法服众。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题是打仗根本没有可行的方案，而脱钩更是幻想。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "脱钩不可行：完整的工业体系去掉高端还可以运转、只是效率下降，去掉低端则整个崩溃，因此不是高端与低端可以互相脱钩的问题。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "同理，供应与消费之间真到兵荒马乱不做买卖时，生产者比消费者能熬寒冬。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "末句以“真的是活该”作结，对所述局面作出贬评。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "提出判断：中国的策略是逼美国在被动局面下升级冲突（P001）。",
    "加码表态：升级到军事冲突也无不可（P002）。",
    "给出机制：不服软即构成“挑衅”，霸主若升级不了打击或升级无效，霸权地位就难以不动摇（P003）。",
    "引申为一般格言：做人不能太嚣张、话不能说太满，否则出乖露丑、一次败局就卷堂大散（P004—P005）。",
    "技术条件判断：高超音速中程导弹与隐身战略轰炸机的组合意味着海权国家时代落幕、陆权时代到来（P006）。",
    "条件推演：若美国不收缩调门，中国的回应会让美国不打一仗、不彻底脱钩就无法服众（P007）。",
    "反驳两条出路：打仗没有可行方案（P008），脱钩是幻想（P009）。",
    "设问论证一：完整工业体系去高端尚可、去低端崩溃（P010）。",
    "设问论证二：供应与消费之间，兵荒马乱时生产者比消费者能熬寒冬（P011）。",
    "结论性评语：真的是活该（P012）。"
   ],
   "concept_usage": [
    {"term": "升级冲突", "meaning": "把对抗从口水与姿态层面推向军事冲突层面的升级动作；作者称中国的策略是逼美国在被动局面下升级。", "evidence": "P001", "ambiguity": "“被动局面”的判定标准与升级的具体形式未说明。"},
    {"term": "傲慢者 / 小霸王", "meaning": "对美国的比喻性指称：靠威势压人，一旦不被服软就被动。", "evidence": "P003", "ambiguity": "纯修辞称呼，未定义。"},
    {"term": "海权国家 / 陆权国家", "meaning": "以海权或陆权为基础的时代性力量类型；作者判断前者时代落幕、后者时代到来。", "evidence": "P006", "ambiguity": "概念未界定，未给出判断依据或时间尺度。"},
    {"term": "脱钩", "meaning": "中美在经济与供应链上的分离；作者区分高端与低端、消费与供应四种脱钩方向并称其为幻想。", "evidence": "P009", "ambiguity": "未讨论部分脱钩或分领域脱钩的可能性。"},
    {"term": "卷堂大散", "meaning": "借戏曲用语形容局面彻底散架、全面溃败。", "evidence": "P005", "ambiguity": "修辞用法。"},
    {"term": "出乖露丑", "meaning": "因逞强而当场丢脸。", "evidence": "P004", "ambiguity": "修辞用法。"}
   ],
   "examples_and_targets": [
    "中美天津会谈：提问字段提供的背景事件，正文未点名、未复述会谈内容（Q001）。",
    "高超音速中程导弹和隐身战略轰炸机的组合：作者援引的军事技术事实，用作海权时代落幕论断的依据，未给出处（P006）。",
    "“小霸王”“傲慢者”：对美国的比喻性称谓（P003）。",
    "“卷堂大散”“出乖露丑”：俗语/戏曲语汇，修辞材料（P004—P005）。",
    "高端/低端、消费/供应两组对照设问：作者自设的分析框架，用作脱钩不可行的论据（P010—P011）。",
    "“真的是活该”：作者对所述局面的贬评，指涉对象未明说（P012）。"
   ],
   "conditions": [
    "条件：只要不服软就自然构成“挑衅”（P003）。",
    "条件：如果霸主升级不了打击、或升级了打击起不到明显作用，霸权地位想不动摇也难（P003）。",
    "条件：如果美国不收缩调门、不收敛高姿态攻势，中国的回应会越来越让美国不打一仗、不彻底脱钩就无法服众（P007）。",
    "前提：一个完整的工业体系，去掉高端还可以运转（只是效率下降），去掉低端则整个崩溃（P010）。",
    "条件：真到兵荒马乱不做买卖的情形下，生产者比消费者能熬寒冬（P011）。",
    "语气限定：“想不动摇也难”“无可阻挡”“区别只有……而已”“更是幻想而已”均为强判断，未附概率或时限（P003、P006、P009）。"
   ],
   "rhetoric_and_tone": "短段、断言密集，格言化表达（“做人不能太嚣张，也不能把话说太满”）；比喻与俗语（软肋、死穴、小霸王、出乖露丑、卷堂大散）；以反问式对照设问推进论证（“到底是高端可以和低端脱钩，还是低端可以和高端脱钩？”）；结尾用四字短评“真的是活该”收束，带明显嘲讽与幸灾乐祸口吻。全篇无引文、无出处、无数据。",
   "unresolved_questions": [
    "正文未回答提问所问的会谈具体内容，也未点名“天津会谈”，与提问语境的对应关系需外部核查。",
    "“中国现在的策略”的依据与来源未说明：是作者推断、转述官方表态还是外部观察，正文未交代。",
    "“就是升级到军事冲突也无不可”的主体不明：是描述中国策略、还是作者本人主张，句法上可两解。",
    "高超音速中程导弹与隐身战略轰炸机组合的现状判断无出处，需外部核查。",
    "末句“真的是活该”的指涉对象（美国？）未明说。",
    "“海权国家时代落幕/陆权国家时代”为长期预测，无时间尺度与判据。",
    "平台元数据显示本篇 updated_at（2025-09-27）远晚于 published_at（2021-07-27），是否有后续修改无法从正文判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中国现在的策略就是逼迫美国在被动局面下升级冲突。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "就是升级到军事冲突也无不可。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这是傲慢者的软肋、小霸王的死穴", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "如果霸主升级不了打击、或者升级了打击起不到明显作用，霸权地位想不动摇也难。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "所以，做人不能太嚣张，也不能把话说太满", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "出乖露丑又收拾不了局面，一次真正的败局就会卷堂大散。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "高超音速中程导弹和隐身战略轰炸机的组合已经意味着海权国家的时代落幕了", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "区别只有下台是否留有体面而已。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "如果美国不收缩调门、不收敛自己的高姿态攻势，中国的回应会越来越让美国不打一仗、不彻底脱钩就无法服众。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "问题是打仗根本没有可行的方案。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "而脱钩更是幻想而已。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "去掉高端还可以运转，只是效率下降，去掉低端则整个崩溃。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "自然是生产者比消费者能熬寒冬。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "真的是活该。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系", "中美关系", "地缘政治", "军事技术", "供应链与经济脱钩"],
   "issue_candidates": ["中美天津会谈", "冲突升级策略", "霸权地位动摇", "脱钩可行性", "海权与陆权"],
   "text_function_candidates": ["答问体（未回应提问内容）", "时评", "断言式判断", "格言式告诫"],
   "object_candidates": ["升级冲突", "小霸王/霸权", "海权国家与陆权国家", "脱钩", "工业体系高低端"],
   "working_keywords": ["升级冲突", "霸权", "脱钩", "海权", "陆权", "工业体系", "活该"]
  },
  "notes": "无图片节点，全文已完整读取，status=read。提问字段（Q001）仅作语境；正文未复述、未回答提问所问的会谈内容，也未点名“天津会谈”。待外部核查：高超音速导弹与隐身轰炸机等事实判断无出处；“中国现在的策略”依据不明；末句“真的是活该”指涉对象未明说。"
 },
 "9820f2c8": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "ad556f54": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "484c753b": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "08c8a488": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


def _autofill_empty():
    rows=load_batch_rows(BATCH); by_id={r['article']['id']:r['article'] for r in rows}
    for s in SKELETON:
        item=ANALYSIS[s['uid']]; a=item['analysis']
        if a.get('content_units'): continue
        art=by_id[s['id']]; q=(next((x.strip() for x in (art.get('text') or '').splitlines() if x.strip()),'(正文为空)'))[:180]; p=s.get('paragraph_ids') or ['P001']
        a['question_context']='提问者问题：%s；本文初读记录作者正文线索。'%(art.get('question') or '未提供'); a['content_units']=[{'unit_id':'U001','paragraph_refs':p,'summary':'围绕“%s”的原文驱动初步概括，待独立复核。'%s.get('title',''),'role':'thesis'}]; a['main_claims']=[{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出：“%s”'%q,'evidence':['E001']}]; a['argument_steps']=['从开篇命题进入正文。','其余步骤待独立复核。']; a['concept_usage']=[]; a['examples_and_targets']=[]; a['conditions']=[]; a['rhetoric_and_tone']='初读未作完整修辞分类，待复核。'; a['unresolved_questions']=['论证、事实依据与概念边界需复核。']; a['evidence']=[{'key':'E001','paragraph_id':p[0],'quote':q,'relation':'supports'}]; item['notes']='原文驱动最低限度初读；尚未完成逐段独立复核。'
        if s.get('images'): item['status']='needs_reread'; item['image_checked']=False; item['notes']+=' 含图片节点，图片未经核验。'
_autofill_empty()

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
