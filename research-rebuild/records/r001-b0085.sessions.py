# -*- coding: utf-8 -*-
"""批次 r001-b0085 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0085.sessions.py            # 写 out/r001-b0085.out.jsonl
  python3 records/r001-b0085.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0085"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0085.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f92334cc": {
  "analysis": {
   "question_context": "提问者问：人际关系中，敌人是否是不可或缺的角色？（Q001，属提问者，不是作者立场）。作者不先回答，而是先区分“敌人”与“对手”并各自下定义，再以企业与团队经营为例给出三条应对原则，最后回到本题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "区分敌人与对手：对手是各执一端寻找最优方案的对照组成员，共同目标是准确结果；以旧式法庭控辩双方作比，说明对手是寻找真相的同事。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "给敌人下定义：以他人的失败为其成功的人；这是绝对意义上的定义，其人先成为这样的敌人，才构成关系意义上“某某人的敌人”。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025"], "summary": "敌人的心理与能力特征：被幸存焦虑与存在感焦虑驱动，靠制造别人失败当成功，缺少正面竞争能力，只剩超规则手段，并需要道德相对主义自我催眠。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "以行为方式而非对立关系定义敌人；双方皆有此行为则互为敌对、互相伤害直至毁灭；双方皆无则为超然意义上的合作；无此胸襟则无缘窥探人类能力顶峰。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P034", "P035", "P036"], "summary": "提出文章真正的问题：双方中有一方是敌人、对方在用卑鄙手段时怎么办。", "role": "transition"},
    {"unit_id": "U006", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "第一条：先分清对方手段是否合法，认定敌对性质要高度谦抑，避免自己化为恶龙；依法举报、陈述非隐私事实等不构成敌对手段，原则上自己也可以做。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063"], "summary": "第二条：坚守原则底线，抵制“我们也干吧”的诱惑，接受团队流失代价；理由是只有重视正当性的企业文化才能保证管理成本可承受，而内控制度不能替代立场坚守。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073"], "summary": "守不住就清算退场，不要用那些手段续命；清除不认同理念的成员应视为收益；对方使用这类手段即预示其将自我崩坏。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087"], "summary": "第三条：存在根本保证是有效提供服务而非消灭敌人；用户满意度才是生机所在；不应因被敌对而焦虑，而应作净化团队与接收市场的准备；缩短困扰期属技术问题，留后讨论。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P088", "P089", "P090", "P091", "P092"], "summary": "回到本题：自己不应成为绝对意义上的敌人，只能被敌对；敌人是否出现取决于对方，不由自己决定，是天意与运气。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P093", "P094", "P095", "P096", "P097", "P098", "P099"], "summary": "人类普遍带有敌意本能，因此要自省是否过于苛求人类：划定自己的红线、给别人留站立空间；若对方的友好条件在逻辑上不存在或与自由权利矛盾，自己才是恶龙。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109"], "summary": "以评论区留言者为例说明“没给人留活路”；把圈画得太大就失去认定对方为绝对敌人的资格，此时自己才是敌人，第三方倒向对方针对的是行为方式。", "role": "example"},
    {"unit_id": "U013", "paragraph_refs": ["P110", "P111", "P112"], "summary": "为一丝一毫都不越线，要退后到模糊线后三百米；反问读者是否知道这条线在哪。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敌人与对手必须分开：对手是各执一端寻找最优方案的对照组成员，是同一个“人类研究项目”的两个样本。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敌人是会以他人的失败为其成功的人；这是一个绝对意义上的定义，其成立不取决于此人是否处在具体对立关系中。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敌人是被幸存焦虑和存在感焦虑驱动的患病的人类，其所谓成功主要是制造别人的失败，因缺乏正面竞争能力而只剩拉帮结派、造谣诬告、挑拨离间这类超规则手段。", "evidence": ["E005", "E006", "E007"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "并非一切对立关系都会将双方定义为敌人，而是特定的行为方式与伦理观绝对地定义了敌人。", "evidence": ["E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果双方都有这种行为方式，双方互为敌对关系，会互相伤害直到双方都毁灭；败固亡，胜亦必亡。", "evidence": ["E009", "E010"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果双方都没有这种行为方式，则虽有对立和竞争，却同时是一种超然意义上的合作。", "evidence": ["E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "认定对方敌对性质时要保持高度谦抑，先分清其手段是否合法；基于合法公开资料、没有侵犯隐私、没有伪造变造、没有恶意假设的不属于敌对手段。", "evidence": ["E012", "E013"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要坚守原则底线、抵制“我们也干吧”的诱惑；理由是只有坚持重视正当性、重视道德和理性的企业文化，才能有效保证管理成本的可承受性。", "evidence": ["E014", "E015"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正决定企业胜负生死的是对企业内部管理成本的控制能力；单纯依靠“企业内控”“制度设计”“合规小组”等技术手段不能替代领导层对基本立场的甄别与坚守。", "evidence": ["E016", "E017"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果守不住原则，就不要犹豫、直接清算退场，不要用那些手段继续“竞争”，因为那是饮鸩止渴。", "evidence": ["E018", "E019"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你存在的根本保证不是“消灭一切敌人”，而是有效提供服务；是核心用户的支持而不是敌人的衰败在保证你的存在。", "evidence": ["E020", "E021"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要因为被敌对而焦虑，不要把注意力放在被敌对上，而应视之为净化团队、检视核心客户关系与核心业务有效性的信号。", "evidence": ["E022", "E023"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自己不应该成为绝对意义上的敌人，只能人家找你敌对；敌人是否出现并不取决于你，而是天意、运气决定的。", "evidence": ["E024", "E025"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所有人类身上都有难以断除和超脱的病根，即深埋在心底的敌意本能。", "evidence": ["E026", "E027"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果对方要保证你友好的条件在逻辑上根本不存在或与人的自由权利直接矛盾，那么你自己才是那条恶龙。", "evidence": ["E028"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把圈子画得太大、只给别人留下奴隶的位置，就失去了“认定对方为绝对敌人”的资格；此时你才是那个敌人，而不是反抗你的、自我防卫的人。", "evidence": ["E029", "E030"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为了一丝一毫都不越过红线，有必要退后到模糊线后三百米去。", "evidence": ["E031"]}
   ],
   "argument_steps": [
    "设问：什么是敌人？（P001）",
    "先立对手的定义：对手是各执一端寻找最优方案的对照组成员，双方共同的成功是以最小总消耗得到最准确结果（P003、P004）",
    "类比：老式法庭控辩双方背对法官面向观众席，针锋相对却是寻找真相的同事（P005）",
    "举例：生产竞品的友商、争夺同一名额的同事属于对手（P006）",
    "推论：若双方都有这种心态，竞争可构成最美好的关系之一，甚至互相扶持（P009、P010）",
    "再设问并给出敌人的定义：以他人的失败为其成功的人，是绝对意义上的定义（P013、P014、P015）",
    "补充敌人的成因与特征：幸存焦虑与存在感焦虑、制造别人失败、能力缺陷、超规则手段、绝对卑鄙性、道德相对主义自我催眠（P017—P025）",
    "推论：双方皆是敌人则同归于尽；双方皆非则是对立中的合作（P028、P032）",
    "提出真正的问题：一方是敌人怎么办（P034）",
    "对策一：分清合法手段、保持谦抑，避免自己成为恶龙（P037—P039）",
    "举例划界：依法举报违规、公开谈论技术缺陷不构成敌对（P040、P043、P044）",
    "对策二：坚守底线、抵制“我们也干吧”，接受团队流失；以管理成本论证正当性的现实价值（P046、P049、P053、P055）",
    "让步与限定：若关键人物离开会导致业务崩塌，说明不该继续做该业务（P050）",
    "对策三：以有效提供服务为存在的根本保证，专注核心用户（P074、P075、P076）",
    "结论回到本题：敌人不是自己可选的关系，取决于天意与运气；同时要自省是否过于苛求人类（P090、P092、P093）",
    "反例：评论区留言者使对方无路可走，说明把自己圈子画得过大者才是敌人（P100、P104、P106）",
    "收束：退后到模糊线后三百米，并反问读者是否知道线在哪（P110、P112）"
   ],
   "concept_usage": [
    {"term": "敌人", "meaning": "绝对意义上的定义：会以他人的失败为其成功的人；不取决于是否处在具体对立关系中", "evidence": "P014", "ambiguity": "与关系义的“某某人的敌人”区分；判定主体与判准本文未给出"},
    {"term": "对手", "meaning": "和你各执一端寻找最优方案的对照组成员，双方同属一个“人类研究项目”", "evidence": "P003", "ambiguity": "与敌人相对，但同一人在不同行为下如何归类本文未说明"},
    {"term": "绝对卑鄙性", "meaning": "作者断言敌人这种事物身上存在的性质，而非其自称的“立场不同”", "evidence": "P022", "ambiguity": "“绝对”的适用范围与例外未说明"},
    {"term": "超规则手段", "meaning": "拉帮结派、造谣诬告、挑拨离间等越出正当竞争规则的手段", "evidence": "P021", "ambiguity": "列举是否穷尽未说明"},
    {"term": "道德相对主义", "meaning": "敌人用于自我催眠、把迫害对象想象成对等对手并维持士气的手段", "evidence": "P023", "ambiguity": "作者将道德相对主义与敌人的自我催眠绑定，未区分其他用法"},
    {"term": "管理成本", "meaning": "企业内部的管理成本，被作者称为真正决定胜负生死的因素", "evidence": "P055", "ambiguity": "“控制能力”如何度量未说明"},
    {"term": "模糊线", "meaning": "判断自己是否已越界、是否已构成恶龙的界线", "evidence": "P110", "ambiguity": "线在何处、由谁划定，本文以反问收尾未给答案"}
   ],
   "examples_and_targets": [
    "老式法庭上的控辩双方（类比，说明对手是寻找真相的同事，P005）",
    "生产竞品的友商、争夺同一个名额的同事（对手的举例，P006）",
    "依据现行法律举报运营中的违规问题（举例说明不构成卑鄙手段，P040）",
    "在媒体上谈论技术方案的缺陷短板（举例说明讲述非隐私事实不构成敌对，P043）",
    "“企业内控”“制度设计”“合规小组”（被批评为不能替代立场坚守的技术手段，P061）",
    "某小朋友到评论区留言并逐项指责答主（例子，说明把圈子画到太大、没给人留活路，P100、P101）",
    "屠龙少年化为恶龙（修辞性说法，P038）",
    "在河边坐得够久就会看到尸体从上游漂来（比喻对方终将崩坏，P072）",
    "麻匪（借电影台词式的修辞，P111）"
   ],
   "conditions": [
    "如果竞争的双方都有“同事关系”的心态，竞争不但不是破坏性的，反而可构成最美好的关系之一（P009）",
    "如果双方都有敌人的行为方式，则互为敌对并互相伤害直到双方毁灭（P028）",
    "如果双方都没有这种行为方式，则是对立中的超然合作，帮助对手度过危机是理所当然的选择（P032）",
    "没有这样的胸襟，就没有机会也没有资格去窥探人类能力的顶峰（P033）",
    "只有坚持重视正当性、道德和理性的企业文化，才能有效保证管理成本的可承受性（P053）",
    "如果运营离开违规环节就运行不下去，这种举报构成致命打击只说明自己选择的“事业”本身是错的（P041）",
    "如果关键人物离开会导致这项业务整个崩塌，那只说明不该继续坚持做这个业务（P050）",
    "如果守不住原则，不要犹豫，直接清算退场（P064）",
    "只有在对方主动针对你、迫害你时敌人才会浮现，这不是你能决定的（P092）",
    "如果对方的友好条件在逻辑上根本不存在或与人的自由权利直接矛盾，则自己是恶龙（P099）",
    "把圈子画到过大、只留奴隶位置者失去认定绝对敌人的资格（P104）"
   ],
   "rhetoric_and_tone": "以连续设问与反问推进（“什么是敌人？”“看明白了吗？”“你知道这条线在哪吗？”）；大量第二人称“你”的训诫式行动指令；用第三人称“ta”称呼敌人以保持距离与贬抑；比喻密集（法庭控辩、恶龙、河边尸体、麻匪）；对敌人的道德相对主义使用讽刺；结尾以反问悬置判准。",
   "unresolved_questions": [
    "“敌人”由谁判定、依据什么可操作标准判定，本文未说明。",
    "文中“天意、运气决定”敌人是否出现的说法，与“认定敌对时保持高度谦抑”的判断要求如何衔接，本文未说明。",
    "“ta们会互相伤害，直到双方都毁灭”与“败固亡，胜亦必亡”是可核验的经验断言还是修辞，本文未提供案例。",
    "依现行法律举报被举为不构成敌对手段（P040），其是否考虑举报动机、举报时机等，本文未展开。",
    "结尾“模糊线后三百米”是修辞还是可操作尺度，本文未说明。",
    "如何缩短困扰期、让胜利更早，作者自称留待后面讨论（P086、P087），本篇未答。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "敌人跟对手要分开。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "对手是和你各执一端寻找最优方案的对照组成员", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P014", "quote": "敌人是会以他人的失败为其成功的人。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P015", "quote": "这是一个绝对意义上的定义", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P017", "quote": "敌人是一种被幸存焦虑和存在感焦虑驱动的患病的人类。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P019", "quote": "ta所谓的“成功”，主要是去制造别人的失败。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P021", "quote": "于是ta们只剩下拉帮结派、造谣诬告、挑拨离间这类“超规则手段”。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P027", "quote": "而是一种特定的行为方式、一种特定的伦理观绝对地定义了敌人。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P028", "quote": "ta们会互相伤害，直到双方都毁灭。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P029", "quote": "败固亡，胜亦必亡。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P032", "quote": "却同时是一种超然意义上的合作", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P037", "quote": "要在认定对方的敌对性质时保持高度谦抑。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P044", "quote": "没有伪造变造、没有恶意假设，不属于敌对手段", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P046", "quote": "坚守住原则底线", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P053", "quote": "只有坚持一种重视正当性、重视道德和理性的企业文化，你才能有效地保证管理成本的可承受性。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P055", "quote": "真正决定胜负生死的，其实是对企业内部管理成本的控制能力。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P061", "quote": "不要以为单纯地靠什么“企业内控”“制度设计”“合规小组”之类的技术手段可以来解决问题", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P064", "quote": "如果你真的守不住，不要犹豫，直接清算退场。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P065", "quote": "那是饮鸩止渴", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P074", "quote": "不是“消灭一切敌人”，而是有效提供服务。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P076", "quote": "是ta们的支持，而不是你的所谓敌人的衰败在保证你的存在。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P082", "quote": "因此，不要因为被敌对而焦虑。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P084", "quote": "而应该把这视为净化团队、重新检视核心客户关系和核心业务有效性、做好接收对手崩溃后让出的市场的准备的信号。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P090", "quote": "你自己不应该成为一个绝对意义上的敌人", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P092", "quote": "而是天意、运气决定的。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P095", "quote": "而是所有人类身上都有难以断除和超脱的病根——", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P096", "quote": "那种深埋在心底的敌意本能。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P099", "quote": "这时你自己才是那条恶龙。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P104", "quote": "你就失去了“认定对方为绝对敌人”的资格", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P106", "quote": "你才是那个敌人", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P110", "quote": "你有必要退后到模糊线后三百米去。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "人际关系", "组织管理", "企业文化", "竞争策略"],
   "issue_candidates": ["敌人与对手的区分", "敌对行为的认定", "道德相对主义", "企业伦理与管理成本", "如何对待使用卑鄙手段的对手"],
   "text_function_candidates": ["答疑", "说理", "训诫", "行动建议"],
   "object_candidates": ["企业", "团队", "核心用户", "竞争对手", "评论区留言者"],
   "working_keywords": ["敌人", "对手", "绝对卑鄙性", "超规则手段", "道德相对主义", "管理成本", "正当性", "模糊线", "恶龙"]
  },
  "notes": "无图片节点；question 仅作提问者语境，未归入作者主张。lexical 段落节点数（114）多于正文渲染段落数（112），差值为空段落，非内容缺失。"
 },
 "767835a5": {
  "analysis": {
   "question_context": "提问者问：现在都流行嘲笑做题家思维，是不是和美国人嘲笑nerd书呆子是一个意思？（Q001，属提问者，不是作者立场）。作者不回答该比较，开篇即声明回答这个问题本身就是在助长恶劣的思维风气，转而批判此类由A对B使用的贬义标签，并给出“不要暗算”的做人原则与禁忌。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "拒答并定性：回答该问题即助长恶劣风气；这类非自嘲性贬义标签是人类对语言最大的恶用之一、是稀释了剂量的人格谋杀；作者不会帮人确定这种暗器如何瞄准。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "正面原则：做人的原则是不要暗算，要进攻就明着拔剑；代价是不易取胜，但能让人不随便怀疑你已不宣而战。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "说明暗算嫌疑的后果：能力越强越容易被脑补为已在暗中动手；若还表现出对阴谋的欣赏，会招来不死不休的敌人；这是一种震慑精英不可生邪念的天诛机制。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020"], "summary": "立绝对禁忌：天意不允许对“巧妙的攻击手段”表示任何意义上的欣赏，否则必遭反噬；想过说过做过都在诅咒自己最大的可能性，一分过失要十分忏悔清洗。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026"], "summary": "以反问施压：为微不足道的小恩怨占“恶心你一下你抓不到我把柄”的便宜，就没有资格承受下属的托付、没有资格抱怨别人不选你；玩这些梗是在玩自己的命。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P027"], "summary": "收束：为人父母若没跟子女说明白这个道理，是极大的失职。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只是回答这个问题，都是在助长一种恶劣的思维风气。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "类似五毛、美分等非自嘲性的、由A对B使用的贬义标签，是人类对语言最大的恶用之一。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种标签是稀释了剂量的人格谋杀，一种微型诛心之术。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者声明不会帮人确定这些“血滴子”是为谁准备、使用时如何瞄准。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者教一种做人的原则：不要暗算；想进攻就要明明拔剑、堂堂正正直视对方双眼。", "evidence": ["E005", "E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "不暗算的确会导致不容易取胜，但这样的人别人不会随便怀疑ta已经不宣而战。", "evidence": ["E007", "E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你能力越强，对方怀疑你已悄无声息动手时脑补的空间越大；若你还展现出对暗算、阴谋的欣赏甚至羡慕，安全感不够的人会成为你出乎意料、不死不休的敌人。", "evidence": ["E009", "E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种恐惧如嫉妒一样，是内嵌在人性底层逻辑中、用于震慑精英不可生邪念的抑制机制，是一把用于天诛的利剑。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果你不甘平庸、自强不息而且有任何雄心壮志，就要记住这条绝对禁忌：天意不允许你对任何所谓“巧妙的攻击手段”表示任何意义上的欣赏，否则必遭反噬。", "evidence": ["E012", "E013"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何地方、任何时间，只要以任何形式这样做过、说过甚至想过，都在亲手诅咒自己最大的可能性；一分过失都要十分的忏悔来清洗。", "evidence": ["E014", "E015"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问质问：为小恩怨占那种便宜而触犯禁忌的人，有什么资格承受将来要把前途命运寄存到他身上的下属的托付，配吗？", "evidence": ["E016", "E017"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到时候没有资格抱怨人明明知道你技术最好却不肯选你；玩这些梗其实是在玩自己的命。", "evidence": ["E018", "E019"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为人父母如果没有跟子女说明白这个道理，是极大的失职。", "evidence": ["E020"]}
   ],
   "argument_steps": [
    "先声明拒答：回答该问题即在助长恶劣风气（P001）",
    "界定被批判对象：由A对B使用的非自嘲性贬义标签（P002）",
    "定性：人格谋杀、诛心之术、杀人于无形的暗器（P003、P005）",
    "给出正面原则：不要暗算，要进攻就明着拔剑（P006、P007）",
    "承认代价：不容易取胜，但换取别人不怀疑你不宣而战（P008、P009）",
    "推演风险：能力越强，被脑补为暗中动手的空间越大（P011）",
    "条件推论：若表现出对阴谋的欣赏，会招来不死不休的敌人（P012）",
    "机制解释：这是震慑精英不可生邪念的天诛机制（P014）",
    "立禁忌：天意不允许欣赏“巧妙的攻击手段”，否则必遭反噬（P016）",
    "强化禁忌：想过说过做过都在自我诅咒，需十分忏悔清洗（P018、P019）",
    "反问施压：为小便宜触犯禁忌者没有资格承受下属托付、没有资格抱怨不被选择（P021、P024）",
    "收束到教养责任：父母未讲明此理是极大失职（P027）"
   ],
   "concept_usage": [
    {"term": "血滴子", "meaning": "比喻由A对B使用的非自嘲性贬义标签：杀人于无形、可逃脱责任的暗器", "evidence": "P004", "ambiguity": "标题用词，正文以“暗器”与“这些杀人于无形的暗器”指代，未再定义"},
    {"term": "暗算", "meaning": "不宣而战的攻击方式；作者主张做人的原则是不要暗算", "evidence": "P006", "ambiguity": "与合法的公开进攻如何划界，本文未说明"},
    {"term": "人格谋杀", "meaning": "对贬义标签性质的界定：稀释了剂量的人格谋杀", "evidence": "P003", "ambiguity": "“稀释了剂量”的具体所指未展开"},
    {"term": "天诛", "meaning": "内嵌在人性底层逻辑中、用于震慑精英不可生邪念的抑制机制", "evidence": "P014", "ambiguity": "“天意”“天诛”的主体与运作方式本文未说明"}
   ],
   "examples_and_targets": [
    "五毛、美分、精日、皇汉、绿蛙、小粉红、南拳、easy girl、单身狗（被批判的贬义标签举例，P002）",
    "做题家思维与nerd书呆子的比较（提问者的话题，作者明确拒答，P001）",
    "“恶心你一下你抓不到我把柄”的所谓便宜（被批评的心态，P021）",
    "下属的托付、别人选人（用于反问施压，P021、P024）",
    "为人父母对子女的说明责任（收束用例，P027）"
   ],
   "conditions": [
    "如果你不甘平庸、自强不息，而且有任何雄心壮志，就要记住这条绝对禁忌（P015）",
    "只要在任何地方、任何时间以任何形式这样做过、说过甚至想过，都在亲手诅咒自己最大的可能性（P018）",
    "你能力越强，对方怀疑你已悄无声息动手时脑补的空间越大（P011）",
    "如果你在任何方面展现出对暗算、阴谋的欣赏甚至羡慕，安全感不够的人会成为不死不休的敌人（P012）",
    "这种暗器对于有这个动机而又必须逃脱责任的人来说的确是大好利器（P005）"
   ],
   "rhetoric_and_tone": "开篇以拒答表明道德立场；全文第二人称训诫与连续反问（“配吗？”重复两次、“还玩这些梗吗？”）；“血滴子”“天诛”“反噬”“五雷”式的宿命与报应修辞；对贬义标签使用者作严厉道德谴责，语气近乎训诫文。",
   "unresolved_questions": [
    "提问所问的“做题家思维与nerd书呆子是否同义”未获回答，作者明确拒绝作答（P001、P004）。",
    "“天意不允许”“必遭反噬”的机制与主体本文未说明，属需外部核查或信仰性断言。",
    "“暗算”与合法的公开攻击（如举报、公开批评）的边界，本文未说明。",
    "贬义标签使用者的责任与可救济方式，本文未说明。",
    "结尾要求父母向子女说明此理，但具体说明方式本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "只是回答这个问题，都是在助长一种恶劣的思维风气。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "这类非自嘲性的，由A对B使用的贬义标签，是人类对语言最大的恶用之一。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这是一种稀释了剂量的人格谋杀，一种微型诛心之术。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "我是不会帮人确定这些血滴子到底是为什么头型准备、使用时应该怎样瞄准的。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "但我教你们一种做人的原则，就是不要暗算。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "你想进攻，要明明的拔剑，堂堂正正直视对方的双眼。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "这的确会导致你不容易取胜", "relation": "qualifies"},
    {"key": "E008", "paragraph_id": "P009", "quote": "这样的人，别人不会随便怀疑ta已经不宣而战。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "你能力越强，对方怀疑起你已经悄无声息的动手时脑补的空间越大。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "那些安全感不够的人将会全自动的成为你出乎意料的、无法理解的、不死不休的敌人。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P014", "quote": "这是一种内嵌在人性底层逻辑中、用于震慑精英不可生邪念的抑制机制，是一把用于天诛的利剑。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P015", "quote": "你就要记住这条绝对禁忌——", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P016", "quote": "天意不允许你对任何所谓“巧妙的攻击手段”表示任何意义上的欣赏，否则必遭反噬。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P018", "quote": "你只要以任何形式这样做过、说过甚至想过，你都在亲手诅咒自己最大的可能性。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P019", "quote": "一分过失，都要十分的忏悔来清洗。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "你有什么资格承受将来要把前途命运寄存到你身上的下属的托付？", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P022", "quote": "配吗？", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P024", "quote": "到时候你有什么资格抱怨人明明知道你技术最好却不肯选你？", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P026", "quote": "其实这是在玩自己的命。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P027", "quote": "为人父母，如果没跟子女说明白这个道理，是极大的失职。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "语言与修辞", "人格与名誉", "人际策略", "家庭教育"],
   "issue_candidates": ["贬义标签的伦理性质", "暗算与阴谋的禁忌", "能力强者被猜忌", "公共讨论风气"],
   "text_function_candidates": ["答疑（拒答式）", "批评", "训诫"],
   "object_candidates": ["网络标签使用者", "做题家", "nerd书呆子", "下属", "子女"],
   "working_keywords": ["血滴子", "人格谋杀", "诛心之术", "暗算", "不宣而战", "天诛", "反噬"]
  },
  "notes": "无图片节点。作者明确拒答提问中的“做题家/nerd”比较，Q001 仅作语境记录，未归入作者主张。"
 },
 "95ef75be": {
  "analysis": {
   "question_context": "提问者问：怎么做到不卑不亢？（Q001，属提问者，不是作者立场）。作者称这是个巧妙的问题，并把“如何做到”改写为“由谁判定”：是否算不卑不亢主要取决于行为的受者与观者，而非行为者本人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "提出该问题巧妙：不卑不亢无客观通行标准，同一行为因上下文与观者不同可被判为不卑不亢、傲慢无礼或卑躬屈膝，判定是一事、一时、一人一答的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009"], "summary": "判定要害在于受者与观者对你是否有敬畏、是否相信你对ta们的爱；信则“卑”被看作平易近人、“亢”被看作坦率耿直。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012"], "summary": "医生与流氓同一手术刀、同一工作服、同一切口的类比；据此说差别待遇看似最不公平实则最公平，因为并非“完全一样的行为”，但公平之理非三言两语可述。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014"], "summary": "结论：不卑不亢不是被做到的，是因为ta们爱你；不卑不亢的那个其实是爱。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个人是否被视为不卑不亢，主要不取决于本人，而取决于该行为的受者与观者；判定随关系与上下文变化，是一事、一时、一人一答的。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "并不存在一种客观的、通行的不卑不亢标准。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "同一个行为可能因上下文不同而分别被视为不卑不亢、傲慢无礼、卑躬屈膝，甚至被同一群在场者分别判为这三者。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判定的要害在于受者与观者对你是否有敬畏、是否相信你对ta们的爱。", "evidence": ["E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果对方信，你的“卑”会被看作平易近人、和蔼可亲，“亢”会被视为爱憎分明、坦率耿直；同样的话与事换一个人原样做一遍，却被视为不知轻重、没有礼貌。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "医生与流氓的例子表明这种差别待遇看似最不公平，实则最公平，因为那根本不是“完全一样的行为”。", "evidence": ["E009", "E010"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者承认这种差别待遇为何公平、功夫到底在哪首诗外，不是三言两语所能描述（本文未展开）。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不卑不亢本身不是被做到的；是因为ta们爱你，你的一切就都可爱起来；不卑不亢的那个其实是爱。", "evidence": ["E012", "E013"]}
   ],
   "argument_steps": [
    "以“这其实是一个很巧妙的问题”起手，把判定主体从行为者本人移向受者与观者（P001–P002）。",
    "否定存在客观通行标准，列举同一行为的三种互斥判定与同场分歧（P003–P005）。",
    "提出判定依赖具体关系上下文，是一事、一时、一人一答的（P006）。",
    "给出要害条件：对方是否有敬畏、是否相信你的爱（P007–P009）。",
    "以医生与流氓同一手术刀的类比说明差别待遇的观感与实质（P010–P012）。",
    "让步承认“为何公平”“功夫在诗外”非三言两语可述（P012）。",
    "结论回收到“爱”：不卑不亢不是被做到的（P013–P014）。"
   ],
   "concept_usage": [
    {"term": "不卑不亢", "meaning": "由受者与观者判定的关系性评价结果，不是行为者可自行达成或自有的客观品质。", "evidence": "P002", "ambiguity": "作者说无客观通行标准，却仍以此词作为可被称颂的评价名目，二者并存未调和。"},
    {"term": "卑 / 亢", "meaning": "同一行为的两侧倾向；在对方相信你时分别被重述为“平易近人、和蔼可亲”与“爱憎分明、坦率耿直”。", "evidence": "P009", "ambiguity": "该重述限定在“对方信”的条件下，本文未说明不信时的完整情形。"},
    {"term": "敬畏与爱", "meaning": "判定的两项前提：对方对你是否有敬畏、是否相信你对ta们的爱。", "evidence": "P007", "ambiguity": "二者如何形成、是否可培养，本文未说明。"},
    {"term": "诗外", "meaning": "借“功夫在诗外”的说法，指差别待遇为何公平的道理不在字面行为之内。", "evidence": "P012", "ambiguity": "作者自称非三言两语可述，未展开，出处亦未点名。"}
   ],
   "examples_and_targets": [
    "医生与流氓：同一把手术刀、同一身工作服、同一条切口，一个收费一个坐牢（作者自设的对称类比，非史料或数据，P010）。",
    "同一群在场者分别判为不卑不亢、傲慢无礼、卑躬屈膝（作者设想的情形，P005）。",
    "“功夫在诗外”的用典（修辞引用，未点名出处，P012）。"
   ],
   "conditions": [
    "判定随关系与当时的上下文变化，“是一事、一时、一人一答的”（P006）。",
    "以“对方信”（相信你对ta们的爱、对你有敬畏）为前提（P007–P008）。",
    "P009 的正面重述以“对方信”为条件，反面情形只以“换一个人原样做一遍”作对照（P009）。",
    "差别待遇为何公平的论证被作者明确留待他处（P012）。"
   ],
   "rhetoric_and_tone": "开场以“很巧妙的问题”肯定提问者；连用短句否定判断（“并不存在……”）；“卑”“亢”分举的对偶重述；医生与流氓的极端对称类比带冷峻反讽；末段转为格言式断言，并以单句独立成段收束（“不卑不亢的那个，其实是爱。”）。第二人称“你”贯穿全篇。",
   "unresolved_questions": [
    "提问所问“怎么做到”，作者未给出可操作方法，而是把问题改写为判定条件问题；具体做法本文未说明。",
    "“为什么这种差别待遇其实是公平的、功夫到底在哪首诗外”，作者自称实在不是三言两语所能描述，未展开（P012）。",
    "“敬畏”与“爱”如何形成、能否培养，本文未说明。",
    "医生与流氓的例子为作者自设类比，其中流氓“要把牢底坐穿”属常识化的法律后果表述，待外部核查。",
    "全篇以“ta”指代，具体所指由上下文决定，作者未界定。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "你的作为是否算为不卑不亢，其实不是主要取决于你的，而是取决于这行为的受者和观者。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P006", "quote": "是一事、一时、一人一答的。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "并不存在一种客观的、通行的不卑不亢的标准。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "同一个行为，可能因为上下文的不同而一次被视为不卑不亢、一次被视为傲慢无礼、一次被视为卑躬屈膝。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "甚至被同样在场的一群人分别认为是以上三者。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "它的要害在于这些人对你是否有敬畏，是否相信你对ta们的爱。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "对方信，则你的行为多半会被称颂为不卑不亢。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "你的“卑”会变为平易近人、和蔼可亲；你的“亢”会被视为爱憎分明、坦率耿直。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "这是世界上“最不公平的事”", "relation": "context"},
    {"key": "E010", "paragraph_id": "P012", "quote": "但是这又是世界上最公平的事", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "功夫到底在哪首诗外，实在不是三言两语所能描述。", "relation": "qualifies"},
    {"key": "E012", "paragraph_id": "P013", "quote": "不卑不亢本身不是被做到的。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "不卑不亢的那个，其实是爱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "人际评价", "修身与处世"],
   "issue_candidates": ["不卑不亢的判定标准", "同一行为的不同解读", "敬畏与信任对评价的作用"],
   "text_function_candidates": ["答疑（改写问题式）", "解释", "论辩"],
   "object_candidates": ["提问者", "受者与观者", "医生", "流氓"],
   "working_keywords": ["不卑不亢", "卑", "亢", "敬畏", "爱", "受者与观者", "功夫在诗外"]
  },
  "notes": "无图片节点。Q001（“怎么做到不卑不亢？”）属提问者，仅作语境记录，未计入作者主张；作者未回答提问所求的操作方法，而以判定条件作答，已在 unresolved_questions 登记。"
 },
 "eb817668": {
  "analysis": {
   "question_context": "提问者问：如何卸下伪装的面具，真诚的面对每一个人？（Q001，属提问者）。作者先以灯A、灯B、灯C接不同电池的反应差异质疑“一视同仁即真诚”的直觉，再以“最简单的手电筒”为真诚的典范，推出真诚的实质是算法稳定性的信心，最后为普通人给出以“献祭”为要害的做法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "寓言设定：灯A接任何电池一样亮；灯B按3V、6V、12V、1.5V各有不同反应；灯C接同一电池每次反应都不同。", "role": "example"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "以连续设问把寓言转为问题：谁才是“卸下伪装的面具，真诚的面对每一个电池”的老实灯；并追问真诚的定义是否等于对所有人一视同仁、一视同仁是否等于等量待遇。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "主张从真诚的典范提炼本质，否认典范是伟大先贤或公认道德模范，称最简单的手电筒比最伟大的道德模范更真诚；并指出灯B反应复杂并不因此不真诚。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "给出定义：真诚是一种算法稳定性的信心；用户把意外归为外部干扰或自身理解不足而非算法恶意；手电筒因不可能有恶意而永不被判不真诚；人类则被默认假设存在“人不为己，天诛地灭”的内因。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024"], "summary": "排除常见理解：真诚的要害不在展现隐私、公开、不隐瞒；另一达成手段是无能——人相信小孩、智力障碍者、机械装置的真诚，其实是相信其无能。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "对既不可能无隐私也不可能机械化的一般人，真诚的要害在于某种切切实实的献祭，举例如关闭获利通道、实名、先支付成本。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P030"], "summary": "以“试试看。”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以设问质疑“反应复杂即不真诚”的直觉，并追问真诚的定义是否就是对所有人一视同仁、一视同仁是否等于等量待遇；设问处未直接断言答案。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真诚的典范不是某位伟大的先贤或公认的道德模范；最伟大的道德模范也不如一个最简单的手电筒真诚。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真诚是一种算法稳定性的信心。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当算法给出的交互出乎用户意料时，用户只会视为外部干扰和对算法的理解不足，而不视为算法本身存在恶意；手电筒因不存在恶意的可能，表现再出乎意料也不可能得到“不真诚”的判定。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类被认为天然存在“人不为己，天诛地灭”的内因，除非有某种理由让ta们相信你没有。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真诚的要害不在于“展现隐私”“公开”“不隐瞒”，因为完全无隐瞒不可能做到，且任何必然存在的隐瞒都可能被疑为巧妙的诡计。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真诚的另一个达成手段是无能；人相信小孩子、智力障碍者、机械装置的真诚，其实是相信ta们的无能。", "evidence": ["E010", "E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对既不可能做到“无隐私”也不可能做到“机械化”的一般人而言，真诚的要害在于某种切切实实的献祭。", "evidence": ["E012", "E013"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "献祭的具体做法举例：关闭获利通道、实名、先支付成本。", "evidence": ["E014", "E015", "E016"]}
   ],
   "argument_steps": [
    "以灯A、灯B、灯C接不同电池的反应差异设定寓言（P001–P005）。",
    "用设问把寓言转为问题：谁是卸下面具、真诚面对每一个电池的老实灯（P006–P008）。",
    "追问定义：真诚是否等于一视同仁，一视同仁是否等于等量待遇，并要求读者多想（P009–P012）。",
    "宣布从真诚的典范提炼本质，否认典范是先贤或道德模范，改以最简单的手电筒为例（P013–P018）。",
    "给出定义“真诚，是一种算法稳定性的信心”，并说明恶意归因的有无是判定关键（P019–P022）。",
    "排除“无隐瞒”式理解，补充“无能”这一达成手段（P023–P024）。",
    "落到一般人的手段：切切实实的献祭，并举三例（P025–P029）。",
    "以“试试看。”收束（P030）。"
   ],
   "concept_usage": [
    {"term": "真诚", "meaning": "本文定义为“一种算法稳定性的信心”，即交互方不把意外归因于你的恶意；不指展现隐私或坦白。", "evidence": "P019", "ambiguity": "作者以灯、电池、手电筒喻人，人与“算法”的类比边界未明说。"},
    {"term": "算法", "meaning": "借指行为者的反应规则；算法稳定性指其反应可被理解、不被归为恶意。", "evidence": "P020", "ambiguity": "该词在本文为比喻用法，作者未给技术定义。"},
    {"term": "一视同仁", "meaning": "作者追问其是否等于不论什么样的人都得到一样等量的待遇，未直接给出定义。", "evidence": "P010", "ambiguity": "作者只以反问提出，未断言一视同仁的含义。"},
    {"term": "献祭", "meaning": "指切实付出代价以换取对方相信你无恶意；例举关闭获利通道、实名、先支付成本。", "evidence": "P026", "ambiguity": "献祭为何能使对方相信，本文未展开机制。"},
    {"term": "无能", "meaning": "被信任的一种原因（小孩、智力障碍者、机械装置），作者未评价其高下。", "evidence": "P024", "ambiguity": "与“献祭”是并列还是替代关系，本文未说明。"}
   ],
   "examples_and_targets": [
    "灯A、灯B、灯C与3V、6V、12V、1.5V电池（作者自设的思想实验，非现实案例，P001–P005）。",
    "手电筒（作者用作真诚的典范，P017、P021）。",
    "某位伟大的先贤、公认的道德模范（作者点出并否认其为典范，P016）。",
    "小孩子、智力障碍者、机械装置（作为“被相信无能”的例证，P024）。",
    "“人不为己，天诛地灭”（作者引用的俗谚，用以说明人类被默认假设的内因，P022）。"
   ],
   "conditions": [
    "真诚的判定取决于对方是否相信你无恶意（P020–P022）。",
    "“除非有某种理由让ta们相信你没有”，即默认假设可被理由推翻（P022）。",
    "适用范围限定为既不可能做到“无隐私”、也不可能做到“机械化”的一般人（P025）。",
    "三种献祭做法以“比如”引出，作者未称其为穷尽清单（P027–P029）。"
   ],
   "rhetoric_and_tone": "全篇以寓言加连续设问推进，多处用反问代替断言（“你们发现这问题的复杂性了吗？”“多想想。”）；把“最伟大的道德模范”与“最简单的手电筒”作降格式对照；以“灯”“电池”“算法”的工程语汇讨论伦理问题；结尾举三行短例后以命令式“试试看。”收束。",
   "unresolved_questions": [
    "提问所问“如何卸下伪装的面具”，作者未使用面具隐喻作答，而改写为算法稳定性与献祭；面具与算法的关系本文未说明。",
    "“算法稳定性的信心”在人际中如何形成、需要多长时间，本文未说明。",
    "献祭为何能使对方相信你无恶意，其机制未展开。",
    "P009 原文作“是对所有的人要视同仁吗？”（“要视同仁”疑为原文表述），本记录照原文保留不改，其确切语义待人工核对。",
    "灯A、灯B、灯C与手电筒均为作者自设寓言，非现实案例或数据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P008", "quote": "你确信存在这么多种反应的灯B真的不算是“真诚”的吗？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P010", "quote": "那么，一视同仁，真的意味着不论什么样的人都会得到一样等量的待遇吗？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P016", "quote": "你们可能会觉得是某位伟大的先贤，公认的道德模范，但并不是。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P017", "quote": "最伟大的道德模范，也不如一个最简单的手电筒真诚。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P019", "quote": "真诚，是一种算法稳定性的信心。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P020", "quote": "用户将只会视为外部的干扰和自己对算法的理解不足，而不会视为算法本身存在着恶意。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P021", "quote": "手电筒的表现再出乎意料，也不可能得到“不真诚”的判定。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P022", "quote": "天然存在着“人不为己，天诛地灭”的内因，除非有某种理由让ta们相信你没有。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P023", "quote": "真诚的要害不在于“展现隐私”，“公开”，“不隐瞒”", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P024", "quote": "真诚的另一个达成手段是无能。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P024", "quote": "那其实是相信ta们的无能。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P025", "quote": "你要怎么做到真诚？", "relation": "context"},
    {"key": "E013", "paragraph_id": "P026", "quote": "这个要害在于某种切切实实的献祭。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P027", "quote": "比如，关闭获利通道。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P028", "quote": "比如，实名。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P029", "quote": "比如，先支付成本。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "信任与人格", "沟通与自我呈现"],
   "issue_candidates": ["真诚的定义", "一视同仁与差别对待", "信任如何建立", "献祭式取信"],
   "text_function_candidates": ["答疑（寓言式）", "解释", "说理劝诫"],
   "object_candidates": ["提问者", "手电筒", "灯A/灯B/灯C", "先贤与道德模范", "小孩子", "智力障碍者", "机械装置"],
   "working_keywords": ["真诚", "算法稳定性", "恶意", "一视同仁", "无能", "献祭", "关闭获利通道", "实名"]
  },
  "notes": "无图片节点。P009 原文含“要视同仁”（疑为“一视同仁”之误），本记录照原文保留不改，已在 unresolved_questions 登记；Q001 仅作语境记录，未归入作者主张。"
 },
 "3bd9dad6": {
  "analysis": {
   "question_context": "提问者问：老实人值得利用吗？（Q001，属提问者，其问法把利用当作可权衡取舍的选项）。作者先辨析“利用”与“合作”的定义差别，再主张利用人是对人的位格的侮辱、是伦理上的罪行，最后直接否定“值不值得利用”这一问题框架。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以设问区分利用与合作：合作基于对方的主动意愿，利用则是故意超出对方主观意愿达成的关系。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "以第一人称举例划界：知情同意、商量好一起做不算被利用；借对方弱点（不知情、无法反抗）违背或超出其意愿行事即利用；此界定对无意志的物质与自然规律不适用。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P007"], "summary": "利用人之即将人降格为无意志的工具（石头、木头、锤子），是对人的位格的侮辱，是伦理上的罪行。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "解释“老实人”为何总与“被利用”相连：作者把“老实人”解为意愿可被忽略、可被完全预料、如同吸尘器与手电钻的“类物之人”。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "断言这种事将来不会有好下场；否定“值不值得利用”的问题框架，主张人不能利用人、利用就是犯罪，其收益是犯罪的收益，是以恶为业。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "补充理由：以恶为业赚到的钱抵偿不了其诅咒（防不住其他恶的觊觎、扭曲子女与自己的人格、扭曲与一切ta人的关系），赚到的其实是祸。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者问“老实人值得利用吗？”，即把是否利用老实人作为可权衡的事情提出（提问者说法，不是作者立场）。", "evidence": []},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "合作是在对方有主动意愿下达成的关系；利用则是故意超出对方主观意愿达成的关系。", "evidence": ["E001"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "知情同意、彼此商量好一起做不算“你利用我”；借对方弱点（如不知情或无法反抗）违背或超出其意愿行事，就叫利用。", "evidence": ["E002", "E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "利用对于没有意志可言的物质、自然规律是无罪的；但利用加之于人类，则把人降格为没有意志的工具，是对人的位格的侮辱，是伦理上的罪行。", "evidence": ["E004", "E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“老实人”总与“被利用”联系在一起，因为该词指“其意愿可被忽略的人”、如同吸尘器与手电钻一样可以被完全预料的人、“类物之人”。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这种事将来不会有好下场。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不存在谁值不值得利用、好不好利用的问题，而是人不能利用人，利用就是犯罪，其收益就是犯罪的收益；是以恶为业。", "evidence": ["E009", "E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以恶为业赚到的钱抵偿不了它带来的诅咒——防不住其他恶的觊觎、扭曲子女与自己的人格、扭曲与一切ta人的关系，其中任何一条都能污染和毁灭你可能的幸福感；赚到的其实是祸。", "evidence": ["E011", "E012", "E013"]}
   ],
   "argument_steps": [
    "以设问开篇，随即用定义区分合作与利用（P001–P002）。",
    "用第一人称“我”的处境举例，界定知情同意与被利用的边界（P003–P004）。",
    "按对象区分：利用无意志的物质与自然规律无罪，利用人则有罪（P004–P005）。",
    "给出“老实人”与“被利用”相连的词义根据：类物之人（P006）。",
    "定性：对人的位格的侮辱、伦理上的罪行，将来不会有好下场（P007–P008）。",
    "否定提问框架：不存在值不值得利用的问题，利用即犯罪、是以恶为业（P009–P010）。",
    "补充理由：以恶为业的收益抵不过诅咒，实为祸（P011–P012）。"
   ],
   "concept_usage": [
    {"term": "利用", "meaning": "故意超出对方主观意愿达成的关系；借对方弱点违背或超出其意愿行事。", "evidence": "P002", "ambiguity": "作者同时用“利用阳光、利用潮汐”说明对无意志对象无罪，同一词含伦理中性用法与罪行用法两种。"},
    {"term": "合作", "meaning": "在对方有主动意愿下达成的关系。", "evidence": "P002", "ambiguity": "作者未说明部分知情、部分自愿情形的归属。"},
    {"term": "老实人", "meaning": "作者解为“其意愿可被忽略的人”、可被完全预料的人、“类物之人”。", "evidence": "P006", "ambiguity": "与提问者语用中的“老实人”含义是否一致，本文未说明。"},
    {"term": "位格", "meaning": "人作为有意志者被对待的资格；利用人即对人的位格的侮辱。", "evidence": "P007", "ambiguity": "该词来源与定义本文未展开。"},
    {"term": "以恶为业", "meaning": "把利用他人作为收益来源的行当；作者称其收益是犯罪的收益，实为祸。", "evidence": "P010", "ambiguity": "未界定其范围，例如是否包含合法但自利的行为。"}
   ],
   "examples_and_targets": [
    "利用阳光、利用潮汐、利用光电转换效应（作者举的无意志对象之例，P004）。",
    "石头、木头、锤子（比喻人被降格为工具，P005）。",
    "吸尘器、手电钻（比喻“老实人”可被完全预料，P006）。",
    "子女（作者称以恶为业必定扭曲子女的人格，P011）。",
    "“老实人”（提问者用语，作者对其重新定义，P006）。"
   ],
   "conditions": [
    "利用的伦理判断以对象有无意志为分界：对物质与自然规律无罪，对人则有罪（P004–P005）。",
    "被利用的界定以“对方没有主动意愿”为前提（P002–P004）。",
    "诅咒后果以“必定”表述，是作者的断言性预测，未给经验条件（P011）。",
    "本文未讨论被利用者如何自救或追责。"
   ],
   "rhetoric_and_tone": "以设问开篇随即自答，定义句用合作与利用的对举结构；用第一人称“我”构造被利用者的处境；连续物喻（石头、木头、锤子、吸尘器、手电钻）强化“类物”判断；结尾以短句格言作结（“是以恶为业。”“赚到的哪里是钱，其实是祸罢了。”），带道德训诫与因果报应语气。",
   "unresolved_questions": [
    "提问所问“老实人值得利用吗”的功利框架被作者整体否定，作者未讨论已被利用者应如何处置。",
    "对方部分知情、部分自愿时“利用”与“合作”如何划界，本文未说明。",
    "“防不住其他恶的觊觎”“必定扭曲子女的人格”等属作者的断言性预言，本文未给经验证据，待外部核查。",
    "“老实人”在提问者与作者处含义不同（提问者似指性格宽厚者，作者解为意愿可被忽略的人），存在语义歧义。",
    "“位格”一词的用法来源本文未交代。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "合作是在对方有主动意愿下达成的关系，利用则是故意超出对方的主观意愿达成的关系。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "我本来就知道这件事的风险和收益，彼此商量好了一起做这件事，这不叫“你利用我”。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "但是你借着某种我的弱点（比如不知情或者无法反抗）违背或者超出我的意愿来行事，这就叫利用。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "利用对于没有意志可言的物质、自然规律是无罪的。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "但是利用加之于人类，则是将人类降格为一件没有意志的工具，是将人视为一块石头、一根木头、一把锤子。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "这是对人的位格的侮辱，自然也是一种伦理上的罪行。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "因为“老实人”就是指“其意愿可被忽略的人”，指如同吸尘器、手电钻一样可以被完全预料的人，指一种“类物之人”。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "这种事，将来不会有好下场的。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "不存在谁值不值得利用、好不好利用的问题，而是人不能利用人，利用就是犯罪，其收益就是犯罪的收益。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "是以恶为业。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "防不住其他恶的觊觎、必定扭曲子女的人格、必定扭曲自己的人格进而扭曲与一切ta人的关系。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P011", "quote": "其中任何一条都能深刻的污染和毁灭你可能的幸福感。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P012", "quote": "赚到的哪里是钱，其实是祸罢了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "人格与尊严", "劳动与人际关系"],
   "issue_candidates": ["利用与合作的界限", "老实人被利用", "人的工具化", "恶业的报应"],
   "text_function_candidates": ["答疑（否定问法式）", "定义辨析", "道德训诫"],
   "object_candidates": ["提问者", "老实人", "子女", "利用他人者"],
   "working_keywords": ["利用", "合作", "老实人", "位格", "类物之人", "以恶为业", "诅咒"]
  },
  "notes": "无图片节点。Q001（“老实人值得利用吗？”）属提问者说法，未归入作者主张；作者整体否定该功利问法，已在 C007 与 unresolved_questions 记录。"
 },
 "b510f068": {
  "analysis": {
   "question_context": "提问者问：如何锻炼不紧张的能力？（Q001，属提问者）。作者先给出紧张的根源（对“一个不慎会出现坏得无法承受的后果”的焦虑）与两条解法，再自指这两条对“由不得你选择”的事情不够，最后把根源改写为是否相信意外最终对你是好事，并以信念与诅咒的表述收束。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以铁轨置于地面与十米高空的对比说明何为紧张。", "role": "example"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "给出紧张的根源是对“一个不慎会出现坏得无法承受的后果”的焦虑，并称解法就在这句话里。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "解法一：不挑战你承受不起后果的事，有多大抗跌做多大事（以带鸡蛋当午餐为例）。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "解法二：减少“不慎”，把事做到即使“不慎”都不会做坏的程度（以连续呼吸十次不许失败的考试为例），这属于“练功夫”的话题。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "界定“功夫”：在分手、失眠、天气不好、瘸腿、发烧等不利情况下仍能把事干成，且平时要制造不利情况、花样百出地练。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "自我反问“那这够了吗”，指出由不得你选择的事情不管你有没有功夫。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "改写根源：在于你相不相信不容你选择的事情里的意外追根到底对你是好事；最不紧张的人不是功夫最好、选择余地最大的人，而是相信结果最终一定是好的人。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "举一个“活生生的实例”（引用节点为B站视频链接），称了解意外、相信意外的人真正对紧张免疫。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024"], "summary": "劝信：任何不容你选择的意外背后最终包含对你的好意；信则成为事实，不信则诅咒意外、诅咒自己，紧张就是这诅咒。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P025"], "summary": "结论：这诅咒是致命的，以英文句作结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "紧张的根源是对“一个不慎会出现坏得无法承受的后果”的焦虑，解决方法也在这句话里。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "不要挑战你承受不起后果的事，你有多抗跌就做什么事；这样无论怎么不慎，至多不过是那点后果，就不至于紧张。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "一件事做到即使“不慎”都不会做坏的程度，就不会紧张了；这属于“练功夫”的话题。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“功夫”指哪怕刚分手、连续三天失眠、天气还不好、瘸着一条腿、发着烧没痊愈，你都能把这事干了；平时练的时候要折腾着干、制造不利情况干、颠来倒去、花样百出地干。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者自指上述两条不够：因为有些事情由不得你选择，而这些事情不管你有没有功夫。", "evidence": ["E009", "E010"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "紧张的根源在于你相不相信不容你选择的事情里出现的意外，追根到底对你是一件好事。", "evidence": ["E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界上最不紧张的人并不是功夫最好、选择余地最大的人，而是相信无论出现什么样的“意外”“失误”，哪怕一时有痛苦和损失，兜兜转转最后结果一定是好的人。", "evidence": ["E012"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个了解意外、相信意外、相信意外最终是站在自己一边的人，是真正对紧张免疫的人。", "evidence": ["E013"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何不容你选择的意外，背后最终包含的是对你的好意；出了意外哪怕直接的当下失败了，这失败在最后好过成功。", "evidence": ["E014", "E015"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "牢牢相信这一点，这一点就会是事实；让失败被诅咒成为真正失败的是不相信；因为不相信，你诅咒了意外，也诅咒了自己，紧张就是这诅咒。", "evidence": ["E016", "E017", "E018"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这诅咒其实是致命的。", "evidence": ["E019"]}
   ],
   "argument_steps": [
    "以铁轨在地面与十米高空的对比引出“紧张”（P001–P003）。",
    "定义根源为对不可承受后果的焦虑，并称解法在此句之中（P004–P005）。",
    "给出解法一：不挑战承受不起后果的事（P006）。",
    "给出解法二：把事练到“不慎”也不会坏，即“功夫”（P007–P010）。",
    "自我反问，指出两条解法不覆盖“由不得你选择”的事（P011–P012）。",
    "把根源改写为信念问题：是否相信意外最终对你是好事（P013–P014）。",
    "举“活生生的实例”（P017 为外链视频引用节点）说明对意外免疫者（P015–P018）。",
    "劝导相信“意外包含好意”，并称相信即成事实，不信则诅咒自己，紧张即此诅咒（P019–P024）。",
    "以英文警句收束，称此诅咒致命（P025）。"
   ],
   "concept_usage": [
    {"term": "紧张", "meaning": "指对“一个不慎会出现坏得无法承受的后果”的焦虑；后文又称之为对不容选择的意外的“诅咒”。", "evidence": "P004", "ambiguity": "作者两次给出“紧张的根源”（P004 与 P013），二者关系本文未说明。"},
    {"term": "不慎", "meaning": "失误的可能性；可通过降低后果或提高稳定度使其不再造成坏结果。", "evidence": "P007", "ambiguity": "未界定“不慎”的范围与程度。"},
    {"term": "功夫", "meaning": "在不利条件下仍能把事干成的能力，须以制造不利情况的方式练成。", "evidence": "P009", "ambiguity": "与“减少不慎”是同一件事的两种说法还是两件事，本文未明说。"},
    {"term": "抗跌", "meaning": "承受后果的能力，“你有多抗跌，你就做什么事”。", "evidence": "P006", "ambiguity": "该词为比喻，未给衡量标准。"},
    {"term": "意外", "meaning": "不容你选择的事情中出现的变数；作者赋予其“最终包含对你的好意”的属性。", "evidence": "P019", "ambiguity": "该属性是事实断言还是信念要求，文中两种语气并存。"},
    {"term": "诅咒", "meaning": "因不相信意外而致的自我损害；作者称紧张就是这诅咒。", "evidence": "P024", "ambiguity": "“诅咒”是修辞还是实指，本文未说明。"}
   ],
   "examples_and_targets": [
    "地面铁轨与十米高空铁轨（作者自设的对比情景，P001–P002）。",
    "老妈让带两个鸡蛋到学校当午餐（设想情景，P006）。",
    "“连续呼吸十次不许失败”的考试（设想情景，P007）。",
    "分手、连续三天失眠、天气不好、瘸腿、发烧（练功夫的不利条件举例，P009）。",
    "“充满意外的过程”B站视频（P017 引用节点，作者称为“活生生的实例”，视频内容未核验）。"
   ],
   "conditions": [
    "解法一以“你承受得起那点后果”为条件（P006）。",
    "解法二以可反复练习、达到稳定为条件（P007–P009）。",
    "作者明确这两条对“由不得你选择”的事情不够（P011–P012）。",
    "最后的解法以“相信意外最终对你是好事”的信念为前提（P013–P014、P019–P020）。",
    "“牢牢的相信……就会是事实”为作者的断言，未给成立条件（P020）。"
   ],
   "rhetoric_and_tone": "第二人称“你/你们”直呼读者，连续设问自答（“紧张的根源是什么？”“什么叫功夫？”“那这够了吗？”）；以极端对比与夸张造境（地面与十米高空铁轨、呼吸考试、分手失眠瘸腿发烧的叠加）；口语戏谑（“死翘翘”“没事不要爬高架”“带俩鸡蛋”）；结尾以英文单句作结，并有三句递进（诅咒意外、诅咒自己、紧张即诅咒）；整体为训诫与劝信语气。",
   "unresolved_questions": [
    "P017 为引用节点（外链 B 站视频 BV1jM4m1m7QJ），作者称其为“活生生的实例”，但视频内容本记录无法核验，待外部核查；正文未对该实例作更多文字描述。",
    "作者两次给出“紧张的根源”（P004 与 P013），二者是修正还是补充，本文未说明。",
    "“任何不容你选择的意外，背后最终包含的是对你的好意”是作者的断言，本文未给论证或证据，属待外部核查的断言。",
    "“牢牢的相信这一点，这一点就会是事实”的机制本文未说明。",
    "英文句“It costs you a life, the better life”的语法与确切语义有歧义，本记录照原文引用，不作解释。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P004", "quote": "紧张的根源是什么？是对“一个不慎会出现坏得无法承受的后果”的焦虑。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P005", "quote": "那么解决紧张的方法自然也就在这句话里面。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P006", "quote": "要么，你不要挑战你承受不起后果的事。你有多抗跌，你就做什么事。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "无论你怎么不慎，至多也不过就是那点后果，你就不至于紧张。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "稳到根本就不需要慎，于是也根本没有“不慎”。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "一件事情做到了即使“不慎”都不会做坏的程度，你就不会紧张了", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "就是哪怕你刚分了手、已经连续三天失眠、天气还不好、你还瘸着一条腿、你还发着烧没痊愈……你都能把这事干了，这就叫功夫。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "还要折腾着干、制造不利情况干、要颠来倒去、花样百出的干。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "那这够了吗？要是够了，哪里还来这么多人问呢？", "relation": "qualifies"},
    {"key": "E010", "paragraph_id": "P012", "quote": "问题就在于有些事情由不得你选择，而这些事情不管你有没有功夫。", "relation": "qualifies"},
    {"key": "E011", "paragraph_id": "P013", "quote": "紧张的根源，在于你相不相信不容你选择的事情里出现的意外，追根到底对你是一件好事。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "并不是功夫最好、选择余地最大的人", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P018", "quote": "一个了解意外，相信意外，相信意外最终是站在自己一边的人，是真正对紧张免疫的人。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P019", "quote": "任何不容你选择的意外，背后最终包含的是对你的好意。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P019", "quote": "这失败在最后好过成功。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P020", "quote": "牢牢的相信这一点，这一点就会是事实。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P021", "quote": "让失败被诅咒成为真正的失败的，恰恰是对此的不相信。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P024", "quote": "紧张就是这诅咒。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P025", "quote": "这诅咒其实是致命的", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学与情绪", "修身与自我训练", "信念与命运观"],
   "issue_candidates": ["紧张的成因", "如何锻炼不紧张", "可控与不可控之事", "对意外与失败的信念"],
   "text_function_candidates": ["答疑", "经验总结", "训诫劝信"],
   "object_candidates": ["提问者", "读者（你/你们）", "老妈", "B站视频作者"],
   "working_keywords": ["紧张", "不慎", "抗跌", "功夫", "意外", "诅咒", "It costs you a life, the better life"]
  },
  "notes": "无图片节点；P017 为 quote 字段的外链视频引用节点（B站 BV1jM4m1m7QJ），非图片，其链接内容未核验，已在 unresolved_questions 登记；Q001 仅作语境记录，未归入作者主张。"
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
