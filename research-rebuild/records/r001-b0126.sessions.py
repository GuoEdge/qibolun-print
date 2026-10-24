# -*- coding: utf-8 -*-
"""批次 r001-b0126 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0126.sessions.py            # 写 out/r001-b0126.out.jsonl
  python3 records/r001-b0126.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0126"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0126.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "b145ac9e": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者（Q001）问：特别不喜欢（反感）别人对自己评头论足，是自己的问题还是别人的问题。提问者的立场（反感、怀疑自己也有问题）属提问者，作者在正文中给出自己的回答。作者先回答该问题，随后转向回应「本回答本身是否也在对他人评头论足」的预期质疑，并以自指方式反驳「优越论」。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "直接回答：对你评头论足是别人的问题；属缺少家教、父母失职，也是自己不知死活、不负责任；因为这样做易丧失机会、断送前途、树敌。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "行动建议：对主张这是「权利」的人要远离；这种「友情」一文不值，是将来定「没义气」罪的伏笔。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "把责任归到父母：未教会这常识即失职；父母在子女面前对别人评头论足，是用行动坑害子女，这就叫缺少家教。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "以预设反驳与提问作过渡：「这怎么可能」「怎样才能做到对事不对人」「难道你不是总是在评价别人吗」。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"], "summary": "提出预期质疑（本回答是否也在评头论足），宣布以本回答自身为例说明区别，并列出「要素」。", "role": "transition"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"], "summary": "两条区分要素：针对行为而非具体个人；对「不可行」判断给出论证；并以写下物理公式证明永动机不可能作类比。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "面向自认被针对的读者：作者对其身份与行为一无所知；论证可被质疑、可被反驳；引号内给出带前提与例外条件的示范判断。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024"], "summary": "称上述话是事实判断而非价值判断；给出「愚蠢」的定义；再次声明作者不知道读者是谁、做的是否属于此情况。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "反问推进：评价你的是你自己而非作者；把做论证的人骂一顿并定性「含沙射影」「傲慢」缺乏合理性与正当性；反问是否要让全世界围着个人喜怒决定什么论证可做。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034"], "summary": "反问「谁是巨婴」，列出两种候选作对比，声称再次论证了巨婴行为而未评价具体的人，仍是事实判断。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P035", "P036", "P037"], "summary": "提出「优越论」这一常见报复说法；反问自己是否说过自己不是这样的人；坦率表示与其说在批评别人不如说在批评自己。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046"], "summary": "自指：作者称自己也在造永动机，做明知结果不好仍继续做的事，贪嗔痴无一可免；不是至圣先师，只是更早犯错更深的老蠢蛋；其论证对自己同样适用，故无优越感可言。", "role": "qualification"},
    {"unit_id": "U013", "paragraph_refs": ["P047", "P048", "P049", "P050"], "summary": "反问优越论者如何论证出「有无法掩饰的优越感」，是否靠「凡说别人做错的人只是在炫耀自己没做错」倒推；说明自己向来不喜自指，今日破例。", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P051", "P052", "P053", "P054"], "summary": "结论：不是每个让你觉得自己做错了的人都构成对你个人评头论足，这是有例外的；不是每个说如何是错的人都在炫耀自己没做错。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "喜欢对你评头论足，是别人的问题。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种做法是缺少家教、父母失职，也是自己不知死活、对自己不负责任。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为这么做很容易丧失机会、断送前途、无意义树敌，纯属找倒霉。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对哭着喊着主张这是「权利」的人应当远离；这种人的「友情」一文不值，只是将来定「没义气」罪的伏笔。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母在子女面前整天对别人评头论足，就是在用实际行动坑害子女，这就叫缺少家教。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本回答与「评头论足」的区别在于：它针对一种行为而非具体个人，并对该行为的「不可行」判断给出了论证。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对读者是谁、其行为是否属于该情况一无所知，因此并未对读者做出判断。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述判断是事实判断而非价值判断，其中「愚蠢」有客观定义。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "评价读者的不是写这些话的作者，而是读者自己。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "把做论证的人骂一顿并给人定性「含沙射影」「傲慢」，作者质疑其合理性与正当性。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称此处再次论证了巨婴行为，却没有评价具体的人，仍然是事实判断。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "预期有读者认为这个回答本身就是在「对他人评头论足」。", "evidence": ["E19"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "「优越论」式反击：你这人优越感这么强，不就是你没这事，你就比我们高了一等。", "evidence": ["E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自陈自己也在造永动机、做明知故犯的蠢事，贪嗔痴无一可免，所以说这些话时没有任何优越感可言。", "evidence": ["E21", "E22", "E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认自己是洁白无瑕、目光超卓的至圣先师，称自己只是比读者更早犯错、犯得更深的老蠢蛋。", "evidence": ["E24"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是每个会让你觉得自己做错了的人都构成对你个人评头论足，这是有例外的；不是每个说如何是错的人都在炫耀自己没做错。", "evidence": ["E25", "E26"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称做这些论证时与其说在批评那些自以为被「针对」的人，不如说是在批评自己。", "evidence": ["E27"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质疑优越论者能否论证出「有无法掩饰的优越感」，并指其靠「凡说别人做错的人只是在炫耀自己没做错」这一「永恒真理」倒推。", "evidence": ["E28"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：是否因为本人造永动机，就要永久消灭这个话题、让全世界围着个人喜怒决定什么论证可做。", "evidence": ["E29"]}
   ],
   "argument_steps": [
    "直接回答提问：对你评头论足是别人的问题，并归因于缺少家教、父母失职与本人不负责任（P001—P003）。",
    "给出行动建议：远离主张这是「权利」的人，其友情是将来定「没义气」罪的伏笔（P004—P005）。",
    "归因到父母示范：在子女面前对别人评头论足是用行动坑害子女，这叫缺少家教（P006—P007）。",
    "以预设反问过渡（这可能吗、如何做到对事不对人、你不是总在评价别人吗）（P008—P011）。",
    "提出预期质疑并设定判准：本回答针对行为而非个人，且给出「何以不可行」的论证，并以物理公式证明永动机作类比（P012—P017）。",
    "限定作者认知范围：作者不知道读者是谁、做的是否属于该情况；论证可被质疑与反驳（P018—P021）。",
    "定义与定性：这是事实判断不是价值判断，并给出「愚蠢」的定义（P022—P024）。",
    "反问推进：评价你的是你自己；骂做论证的人缺乏合理性与正当性（P025—P029）。",
    "以「谁是巨婴」的两难对比作反驳，声称仍未评价具体的人（P030—P034）。",
    "反驳「优越论」：作者反问自己是否做过这些事，并声明是在批评自己（P035—P037）。",
    "自指举证：作者自认在造永动机、贪嗔痴无一可免、只是更早犯错的老蠢蛋，故无优越感（P038—P046）。",
    "要求对方举证「无法掩饰的优越感」，指其依据是「永恒真理」式的倒推（P047—P050）。",
    "结论：让人觉得自己做错的人并不都构成对你个人评头论足，存在例外（P051—P054）。"
   ],
   "concept_usage": [
    {"term": "评头论足", "meaning": "本文指针对具体个人、且未给出论证的评价；作者以此与「针对行为并给出论证」的批评相区分。", "evidence": "P013", "ambiguity": "先用于指他人的不良行为（P001—P006），后用于界定读者对本回答的误认（P012—P013），所指随语境滑动。"},
    {"term": "对事不对人", "meaning": "作者以「针对一种行为，不是具体的个人」来界定该说法（P015）。", "evidence": "P010", "ambiguity": "该短语以提问句形式出现在正文（P010），正文未直接回答；上下文中是否属作者自设小标题不明。"},
    {"term": "事实判断／价值判断", "meaning": "作者称其结论是事实判断而非价值判断（P022、P034）。", "evidence": "P022", "ambiguity": "作者未给出两者的判别标准，也未论证该结论为何不属价值判断。"},
    {"term": "愚蠢", "meaning": "作者的定义：明知结果不可避免、自己也不要这结果，仍然自欺欺人去做；称这是「愚蠢的客观定义」（P023）。", "evidence": "P023", "ambiguity": "作者自称「客观定义」但未在文中论证其客观性。"},
    {"term": "巨婴", "meaning": "作者用以指一边主张「人不可以评价人」、一边把普遍性论证当作针对自己的人，靠两种候选对比来界定（P030—P033）。", "evidence": "P031", "ambiguity": "无明确定义，仅以反问与两难对比呈现。"},
    {"term": "优越论", "meaning": "作者对「你这人怎么优越感这么强」这类反击说法的命名（P035）。", "evidence": "P035", "ambiguity": "作者称其为「所谓的优越论」，未说明是否为既有说法。"},
    {"term": "永动机", "meaning": "类比物：指明知结果不可避免且自己不要该结果、仍自欺欺人去做的事；作者并以此自指（P038）。", "evidence": "P021", "ambiguity": "同一喻体既用于一般论证也用于作者自我指认，读者可能混用两种用法。"},
    {"term": "缺少家教", "meaning": "指父母未教会基本常识，甚至以自身行为作错误示范（P002、P006、P007）。", "evidence": "P007", "ambiguity": "作者将其同时归为父母的失职与本人的不负责任，责任主体在两处表述中并存。"}
   ],
   "examples_and_targets": [
    "提问者的处境（别人对自己评头论足、反感），作为作者回应对象而非作者立场（Q001）。",
    "哭着喊着主张这是「权利」的人——作者的行动建议对象与批评对象（P004—P005）。",
    "在子女面前对别人评头论足的父母——作者举以说明「缺少家教」的例证（P006）。",
    "写下物理公式证明永动机不可能——作者的类比（P017），并延伸为「明知故犯者虚掷人生」的示范论证（P021、P031）。",
    "本回答自身——作者用作区分「评头论足」与「对事论证」的样本来分析（P012—P017）。",
    "「优越论」者及其「永恒真理」（凡说别人做错的人只是在炫耀自己没做错）——作者的反驳对象（P035、P049）。",
    "贪、嗔、痴——作者自指时所借的佛教术语式修辞材料（P040）。",
    "至圣先师、洁白无瑕、目光超卓犹如神助——作者用以否定读者可能的误解（P041）。"
   ],
   "conditions": [
    "作者的判断限于「行为」层面：他只说行为不可行，并声明不知道读者是谁、做的是否属于该情况（P019、P024）。",
    "若读者打算追求有意义的度过人生，把时间花在造永动机上不明智；除非能先推翻这些论证，否则继续坚持就是一种愚蠢（P021 的条件句，作者以引号呈现）。",
    "只要读者找得到运算不严谨或定义不准确之处，当然可以指出（P020 允许反驳的条件）。",
    "对「主张这是权利的人」的建议带有时间条件：这种关系不早点断掉，混久了难有别的结局（P004）。",
    "对读者的适用以其自认符合该行为为前提（P018、P025 的「对吧」式设问）。"
   ],
   "rhetoric_and_tone": "通篇第二人称「你／你们」直接对话读者；反问极为密集（P008—P011、P018、P025、P028—P032、P036、P047—P049）；以引号挪用对方话语并加以命名（「权利」「永恒真理」「优越论」「含沙射影」「傲慢」）；训诫与调侃并用（「呵呵」「谁是巨婴？」「那么，现在尴尬了吧？」）；以自嘲与自我指认作论证手段（「我就在造永动机」「老蠢蛋」「贪、嗔、痴，无一可免」）；用物理公式／永动机类比承担论证；结构上从回答提问者转入回应本回答的读者，最后回到对提问的作答。",
   "unresolved_questions": [
    "图片节点 IMG001 未核验，图片内容未知（可能为配图或分隔图），需人工或多模态复核；本篇因此标记 needs_reread。",
    "P010「怎样才能做到「对事不对人」？」疑为插入的小标题或引用句，正文未直接回答，其归属（作者自设标题或平台元素）不明。",
    "P021 引号内整段无外部出处，无法确定是作者自拟的示范话术还是引用他人；按上下文疑为作者自拟，但正文未说明。",
    "P054 为 heading 字段且与 P052 文字重复（「这是有例外的。」），正文与 lexical 结构存在分歧（divergence=true），可能是标题回填或重复节点。",
    "P015—P016 所列「要素」是否为区分「评头论足」与「对事论证」的穷尽标准，作者未说明；仅两条是否充分亦未论证。",
    "作者称「愚蠢」有客观定义（P023），其「客观」依据未在文中论证，属待研究者核查的断言。",
    "文中的「作者」为第三人称自指（P019、P024），属修辞安排；作者身份、与提问者的关系未说明。",
    "提问者所反感的「评头论足」具体情形（家庭、职场或网络）正文未交代，作者的判断所适用的场景因此不明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "喜欢对你评头论足当然是别人的问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这是缺少家教，父母失职。也是自己不知死活，对自己不负责任。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "因为这么做很容易丧失机会、断送前途、乃至于毫无意义的树敌", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "哭着喊着要主张这是“权利”的，离ta远点。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这种人的“友情”一文不值", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "爹妈自己在子女面前整天对别人评头论足，就是在用实际行动坑害子女。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这就叫缺少家教。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "它是在针对一种行为，不是具体的个人。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "给出了“它何以不可行”的论证。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "这就像写下了物理公式，证明永动机不可能。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "作者对你是谁根本一无所知", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P024", "quote": "作者仍然不知道你是谁", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "这话不是价值判断，而是事实判断。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "这就是愚蠢的客观定义。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "评价你的并不是写这些话的作者", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P027", "quote": "你还给人定性“含沙射影”、“傲慢”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P028", "quote": "你说说看，这合理性和正当性在哪里？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P033", "quote": "这里再次成功的论证了巨婴行为，但是却没有评价具体的人。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P012", "quote": "估计有人会觉得这个回答本身就是在“对他人评头论足”", "relation": "context"},
    {"key": "E20", "paragraph_id": "P035", "quote": "你这人怎么优越感这么强？", "relation": "context"},
    {"key": "E21", "paragraph_id": "P038", "quote": "我就在造永动机。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P040", "quote": "贪、嗔、痴，无一可免。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P046", "quote": "我说这些话的时候，没有任何优越感可言", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P043", "quote": "我只是比你们更早犯错、犯得更深的老蠢蛋。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P051", "quote": "不是每个会让你觉得自己做错了的人，都构成对你个人评头论足。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P053", "quote": "不是每个说如何是错的人，都是在炫耀自己没做错。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P037", "quote": "不如说我是在批评我自己。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P049", "quote": "是靠“凡说别人做错的人，只是在炫耀自己没做错”这一“永恒真理”倒推的吗？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P029", "quote": "难道就因为你本人在造永动机，你就要永久消灭掉这个话题？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往规范", "家庭教育", "论证与批评的方法论", "社会评论"],
   "issue_candidates": ["如何应对他人对自己的评头论足", "「对事不对人」的界限", "事实判断与价值判断的区分", "被批评者的防御性反击（优越论）", "父母言行对子女的影响"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "训诫", "经验总结"],
   "object_candidates": ["提问者", "主张评头论足是「权利」的人", "「优越论」者", "父母", "作者本人"],
   "working_keywords": ["评头论足", "对事不对人", "事实判断", "价值判断", "优越论", "巨婴", "永动机", "缺少家教"]
  },
  "notes": "本篇含 1 个图片节点（IMG001），图片内容未经核验，需图像核验；已读部分为正文文本。status=needs_reread 的原因即图片未核验。另：正文与 lexical 结构存在分歧（divergence=true，见 P054 与 P052 重复、P010 未覆盖片段）；P021 引号段无外部出处。本文未引述需外部核查的数据或文献。"
 },
 "a88f2258": {
  "analysis": {
   "question_context": "提问者（Q001）问「如何看待离婚冷静期?」。提问本身无立场表述，作者以编号两条作出回答：先论该制度对离婚率数据的影响只是暂时错觉，再论其对结婚率的伤害恐怕深远不可弥补。作者未讨论该制度的具体条文、期限与例外情形。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "论点一：离婚冷静期导致的「离婚率下降」更多是一种暂时的统计错觉。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "水库类比论证：离婚冲动如水位的涨落，围坝越高蓄积痛苦越多，只有超过上限才溢流；提高门槛等于扩容而未切断上游来水，离婚案例只是进入「蓄水状态」，等新增库容填满后流量恢复原样；因为失败婚姻积累的伤害无限加深，会超过一切固定禁锢的力量。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "跨国历史例证：五十多年前意大利无离婚制度，直接催生「意大利式离婚」即谋杀；爱尔兰1996年离婚合法化毫厘之差勉强过线，导致非婚同居常态化。其中 P007、P009 为链接标题残留。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013"], "summary": "推论：门槛抬高只是让痛苦大坝坝体增高、把决口期推迟一两年；一两年后离婚数据会重新回归，也许略低于历史水平，但那以婚姻平均质量下降为补偿；故这一「正面影响」恐怕只是暂时的幻觉。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015"], "summary": "论点二：离婚冷静期对结婚率的伤害恐怕深远而不可弥补；作者明示不作解释，称相信每个女孩子都有自己的答案。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016"], "summary": "结尾：将来看数据吧。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "离婚冷静期所导致的「离婚率下降」现象，更多的是一种暂时的统计错觉。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以「痛苦水库」作类比：离婚冲动如同水库水位，围坝越高越能蓄积更多痛苦，只有超过上限才开始溢流。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提高离婚门槛在实效上等于水库扩容，但没有切断上游流下来的河流。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "离婚案例只是进入了「蓄水状态」，等新增库容被再次填满，原来是多大的流量到时候还是多大。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "失败的婚姻积累的伤害是无限加深的，会超过一切固定的禁锢的力量。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "就在仅仅五十多年前，意大利根本没有离婚制度，这直接催生出了「意大利式离婚」这一术语——谋杀。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱尔兰的离婚合法化在1996年，毫厘之差勉强过线。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "（爱尔兰的情形）导致的结果是非婚同居常态化。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "离婚冷静期抬高的门槛只是让痛苦大坝坝体增高，把决口期推迟一两年，一两年后离婚数据自然会重新回归。", "evidence": ["E9", "E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "回归后的数据也许会比历史水平低一点，但那是以婚姻的平均质量下降作为补偿。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这一「正面影响」恐怕只是暂时的幻觉。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "离婚冷静期对于结婚率的伤害恐怕是深远而不可弥补的。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对第二点不作解释，称相信每个女孩子都有自己的答案，并表示将来看数据。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "提出论点一：冷静期带来的「离婚率下降」更多是暂时的统计错觉（P001）。",
    "建立水库类比：离婚冲动如水位的蓄积与溢流，围坝越高蓄积痛苦越多（P002）。",
    "把门槛提高换算为水库扩容，并指出上游来水未被切断（P003）。",
    "推论一：离婚案例进入「蓄水状态」，新增库容填满后流量复原（P004）。",
    "给出前提性理由：失败婚姻积累的伤害无限加深，会超过一切固定禁锢的力量（P005）。",
    "举意大利例：无离婚制度催生「意大利式离婚」即谋杀（P006）。",
    "举爱尔兰例：1996年离婚合法化勉强过线，结果非婚同居常态化（P008、P010）。",
    "得出结论：门槛抬高只是把决口期推迟一两年，数据将回归，代价是婚姻平均质量下降，「正面影响」是暂时幻觉（P011—P013）。",
    "提出论点二：对结婚率的伤害恐怕深远而不可弥补，但不作论证（P014—P015）。",
    "收尾：将来看数据吧（P016）。"
   ],
   "concept_usage": [
    {"term": "离婚冷静期", "meaning": "本文中与「提高离婚门槛」「抬高的离婚门槛」互换使用，指抬高离婚门槛的制度安排。", "evidence": "P003", "ambiguity": "作者未说明其具体条文、期限与例外，仅按其抬高门槛的实效效果讨论。"},
    {"term": "痛苦水库／痛苦大坝", "meaning": "核心比喻：离婚冲动的水位与围坝，门槛提高相当于扩容或坝体增高，决口期被推迟。", "evidence": "P002", "ambiguity": "前段用「水库／围坝／溢流」，后段改用「大坝／坝体／决口」，喻体未统一。"},
    {"term": "蓄水状态", "meaning": "离婚案例因门槛陡然升高而被积压、未释放的状态。", "evidence": "P004", "ambiguity": "为作者自造的描述语，无量化界定。"},
    {"term": "统计错觉", "meaning": "作者对冷静期后「离婚率下降」这一现象的定性；后文又称其为「暂时的幻觉」。", "evidence": "P001", "ambiguity": "「错觉」与 P013「幻觉」并用，作者未区分二者。"},
    {"term": "意大利式离婚", "meaning": "作者称其为一个术语，指在无离婚制度下以谋杀达成离婚。", "evidence": "P006", "ambiguity": "作者未给出出处或年份细节，该术语及年代均待外部核查。"},
    {"term": "非婚同居常态化", "meaning": "作者对爱尔兰离婚合法化后结果的概括。", "evidence": "P010", "ambiguity": "该句紧接 P009 链接标题，其是否为对链接内容的概括、以及是否仅为爱尔兰情形，正文未说明。"},
    {"term": "婚姻的平均质量", "meaning": "作者用以说明离婚数据回落所付出的代价。", "evidence": "P012", "ambiguity": "无衡量方式或指标，属未定义概念。"}
   ],
   "examples_and_targets": [
    "意大利：五十多年前根本没有离婚制度，作者称这直接催生「意大利式离婚」这一术语即谋杀——作者的历史例证（P006）。",
    "「意大利式离婚_百度百科」链接标题——资料来源标记，正文未给出链接地址（P007）。",
    "爱尔兰：1996年离婚合法化毫厘之差勉强过线——作者的历史例证（P008）。",
    "「西欧唯一禁止离婚的国家……_百科TA说」链接标题——资料来源标记，正文未给出链接地址（P009）。",
    "非婚同居常态化——作者对上述爱尔兰情形的结果概括（P010）。",
    "「每一个女孩子」——作者用以指代对结婚率后果有自身答案的读者群体（P015）。",
    "未来的数据——作者承诺的验证依据（P016）。"
   ],
   "conditions": [
    "「离婚率下降」的判定限于冷静期实施后的统计表现，作者称其「更多的」是暂时错觉，未完全否认存在其他成分（P001）。",
    "伤害会超过禁锢力量这一断言以「失败的婚姻积累的伤害是无限加深的」为前提（P005）。",
    "时间条件：决口期被推迟「一两年」，数据约在「一两年后」回归（P011、P012）。",
    "作者的预测带保留词：也许比历史水平低一点、恐怕只是暂时的幻觉、对结婚率的伤害恐怕深远而不可弥补（P012—P014）。",
    "论点二作者明示不作论证（「这个不解释了」），其成立取决于读者自身判断（P015）。",
    "跨国历史例证（意大利、爱尔兰）为不同时期、不同制度的类比，作者未说明其与当下情形的可比性条件。"
   ],
   "rhetoric_and_tone": "以编号（1）2））组织回答，条理式评论；通篇以水库／大坝比喻承担论证；用「你们要知道」直接称呼读者；用「这个不解释了」与「将来看数据吧」作省略与悬置；「我相信每一个女孩子都有自己的答案」带调侃兼回避论证的语气；以「恐怕」「也许」保留推测性，未作绝对断言。",
   "unresolved_questions": [
    "「五十多年前意大利根本没有离婚制度」及「意大利式离婚」指谋杀的年代与法律细节需外部核查（P006）。",
    "「爱尔兰离婚合法化是哪年？1996年，毫厘之差勉强过线」需外部核查；作者未说明是公投、法案还是其他程序（P008）。",
    "P007、P009 仅为链接标题（百度百科、「百科TA说」），正文未给出可核验的链接或引文内容，属来源标记而非论证。",
    "P010「导致的结果是非婚同居常态化」与爱尔兰情形的因果归属未说明；该段与 P009 字符边界相接（349），可能为链接标题与正文段落的切分问题。",
    "「婚姻的平均质量」（P012）无衡量标准，无法确定其下降如何被观察。",
    "论点二（对结婚率的伤害深远而不可弥补）作者明确不作论证（P015），故无作者理由可考。",
    "提问为「如何看待离婚冷静期」，正文未讨论该制度的具体条文、冷静期长度与例外情形，也未给出处。",
    "正文与 lexical 结构存在分歧（divergence=true）：P007、P009 为未覆盖片段，疑为平台链接元素混入正文。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "更多的是一种暂时的统计错觉。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "离婚冲动如同痛苦水库的水位。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "提高离婚门槛，实效上等于这水库扩容了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "离婚案例进入了“蓄水状态”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "失败的婚姻积累的伤害是无限加深的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这直接催生出了“意大利式离婚”这一术语——谋杀。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "爱尔兰离婚合法化是哪年？1996年，毫厘之差勉强过线。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "导致的结果是非婚同居常态化。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "只是意味着痛苦大坝的坝体增高了，把决口期推迟了一两年。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "一两年后的离婚数据自然会重新回归。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "但那是以婚姻的平均质量下降作为补偿的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "这一“正面影响”恐怕只是暂时的幻觉。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "离婚冷静期对于结婚率的伤害恐怕是深远而不可弥补的。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "我相信每一个女孩子都有自己的答案。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "将来看数据吧。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚姻家庭制度", "社会政策评论", "统计数据解读"],
   "issue_candidates": ["离婚冷静期的实际效果", "离婚率与结婚率的变化", "提高离婚门槛的社会后果", "婚姻痛苦与制度约束的关系"],
   "text_function_candidates": ["答疑", "评论", "预测", "类比论证"],
   "object_candidates": ["离婚冷静期制度", "意大利", "爱尔兰", "已婚与拟婚人群"],
   "working_keywords": ["离婚冷静期", "离婚率", "结婚率", "痛苦水库", "蓄水状态", "意大利式离婚", "非婚同居", "婚姻的平均质量"]
  },
  "notes": "本篇无图片；正文与 lexical 结构存在分歧（divergence=true）：P007、P009 为百度百科／「百科TA说」链接标题残留（疑为平台元素混入正文），且 P009 与 P010 字符边界相接。文中的意大利、爱尔兰史实与年份属作者断言，未给出处，已登记为待外部核查。"
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
