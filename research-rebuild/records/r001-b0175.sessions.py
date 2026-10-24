# -*- coding: utf-8 -*-
"""批次 r001-b0175 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0175.sessions.py            # 写 out/r001-b0175.out.jsonl
  python3 records/r001-b0175.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0175"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0175.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "aa3362a3": {
  "analysis": {
   "question_context": "提问者问“爱是主动，这个观点对吗？”（Q001），即请作者判断“爱＝主动”这一看法是否成立；提问者本身未展开立场。作者借题提出一个关于爱的原则：爱不是主动，而是“主动的被动”——主动作为、但把选择权完全留给对方。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "点题：借提问说一个关于爱的原则，并直接给出命题“爱是被动的”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "界定这条“红线”：竭尽全力保留对方的不知情权、不参与权、不接受权、不赞赏权、不回报权，不惜被埋没、被误解、被伤害，也不追求自己的益处；称之为“主动作为的被动”。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "用四个逐级递进的给钱例子说明主动与主动的被动之别，并称越向该方向进发越接近爱。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020"], "summary": "说明为何强调被动：爱不是权力；主动对别人做事首先是侵犯，“被算为好”是第二性、不必然的；人无权凭自信把别人命运夺来下注；否则一切干涉都可正当化，天使与魔鬼之别只在肯不肯自戴“不伤人”的枷锁。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "以“讲道理”为例：应把道理放在别人会去寻找答案的地方等待，而不是凭对方躲不开的对话流强行塞入其对话框、私信、房间或饭桌；“出于善意”不等于不是冒犯。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "承认被动的代价是眼看着危险只能干着急，但指出一旦自行解除限制，就没有任何有效论证能证明干涉造成的痛苦小于所避免的痛苦；侵犯自主权则是确定的，且“主动逻辑”无逻辑休止符。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "反驳折中方案（有时主动、有时被动）：那只是换汤不换药，一切想干预的情形都会自动变成“非常有必要合理干预”，动机不过是“不甘心没回报”，即贪。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037"], "summary": "结论：爱要不变成他人的灾难，唯一选择是严守被动；主动的努力是为了给对方最大选择余地；爱是无声把全世界放在对方伸手可及处等对方来拿。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱是被动的，它是一种“主动作为的被动”。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱的全部行动准则要严守“被动”红线：永远竭尽全力保留对方的不知情权、不参与权、不接受权、不赞赏权、不回报权，不惜被埋没、被误解、被遗忘、被辜负乃至被伤害，也不追求自己的益处。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "给人备好一笔钱由对方自己决定是否领走，是“主动的被动”；为其设立工作机会则升一级，对方还多了“不感激权”；把钱掉在其家门口，对方更有选择权、不感激权与不知情权。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越向“主动的被动”这个方向进发，就越接近于爱。", "evidence": ["E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱不是一种权力；主动对别人做任何事（包括自认为有帮助的事）首先是一种侵犯，“被算为好”是第二性的、不必然的，只是有一定概率被人宽容、原谅。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人没有权利仅凭“自信有一定概率能让你受益”就替别人开设赌局、把别人的命运夺过来下注。", "evidence": ["E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果“自信能让你受益”就算爱，那么一切对人的侵犯和干涉只需加上这种“自信”就可彻底正当化（归谬）。", "evidence": ["E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "魔鬼与天使的区别，就在于肯不肯为不伤人而自愿戴上“枷锁”。", "evidence": ["E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱是尽最大的主动去做尽可能被动的事：讲道理应放在别人会去寻找答案的地方、等别人需要时来寻找，而不是凭着对方躲不开与你的对话流，强行放进对方不得不看到的地方（对话框、私信、堵在房间或饭桌）。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“出于善意”并不表示这不是一种冒犯。", "evidence": ["E19"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "被动的代价是大量“眼看着危险，只能干着急”和理论上主动一点就可免除的灾难痛苦；但一旦自行解除这限制，将没有任何有效论证可以证明因你的干涉而起的痛苦小于你所“避免”的痛苦。", "evidence": ["E20", "E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方是否会遭受你以为会发生的痛苦不好说，但你侵犯了对方的自主权是确定无疑的；只要认定“主动逻辑”，对人的干涉就再也没有逻辑有效的休止符，且在一切想实施干涉的情境下全部有效。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "unknown", "modality": "hypothetical", "statement": "作者设想读者可能提出的折中立场：“不要这么极端——某些情况下我主动，某些情况下我坚守被动。”（作者随后反驳）", "evidence": ["E25"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "折中只是换汤不换药：一切想横加干预的情形都会自动成为“非常有必要合理干预”的情形，背后深刻的动机不过是“不甘心没回报”，即贪。", "evidence": ["E26", "E27", "E28"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱想要不演变成他人的灾难，唯一的选择就是严守被动；可以竭尽全力地主动，但这种努力是为了留给对方最大的选择余地、创造最好的“被动”。", "evidence": ["E29", "E30"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱不是“送给对方全世界”，而是无声地把全世界放在对方伸手可及的地方，等对方来拿。", "evidence": ["E31"]}
   ],
   "argument_steps": [
    "先立命题：爱是被动的，并称之为“主动作为的被动”（P002、P005）。",
    "给出行动红线：保留对方的知情/参与/接受/赞赏/回报等各项拒绝权，不追求自己的益处（P003-P004）。",
    "用给钱的四级例子把“主动”与“主动的被动”分开：直接给钱是主动；备好钱等对方领是主动的被动；设立工作机会再加“不感激权”；钱掉门口再加“不知情权”（P008-P011）。",
    "由例子得出方向性判断：越这样越接近爱（P012）。",
    "追问为何强调被动，回答：爱不是权力（power）（P013-P014）。",
    "理由：主动对别人做事首先是侵犯，被算为“好”是第二性、靠概率的（P015-P016）。",
    "前提：你没有权利强迫别人加入你的赌局，也无权凭自信替他人下注（P017-P018）。",
    "归谬：若自信即爱，则一切侵犯干涉都可正当化；由此把“肯不肯自戴枷锁”立为天使与魔鬼之别（P019-P020）。",
    "换例落实：讲道理应放在别人会去寻找的地方等，而非强行塞入对方躲不开的渠道；“出于善意”不等于不是冒犯（P021-P024）。",
    "让步：承认被动带来干着急与可能被免除的灾难（P025）。",
    "反驳解除限制：没有有效论证能证明干涉之痛小于所避之痛（P026）；对方受苦与否不好说，侵犯自主权确定；干涉逻辑无休止符（P027-P028）。",
    "预设读者折中方案并反驳：换汤不换药，动机是“不甘心没回报”，即贪（P029-P032）。",
    "结论：唯一选择是严守被动；主动的努力用于创造最大的“被动”（P033-P034）。",
    "收束：爱是把全世界放在对方伸手可及处等对方来拿，是主动的被动，是被动的（P035-P037）。"
   ],
   "concept_usage": [
    {"term": "爱", "meaning": "本文未给正面定义，而以行为准则界定：一种严守被动、保留对方全部拒绝权、不追求自身益处、把选择权留给对方的状态或行为模式。", "evidence": "P002", "ambiguity": "P004 的“不追求自己的益处”与 P033-P034 的“竭尽全力的主动”之间的张力，本文未展开说明。"},
    {"term": "主动的被动", "meaning": "主动准备条件、创造机会，但把是否接受、是否知情、是否回报的主动权完全留在对方手里。", "evidence": "P009", "ambiguity": "作者称设立工作机会“升一级”（P010）、把钱掉门口再加“不知情权”（P011），但未说明判定升级的统一标准。"},
    {"term": "权力（power）", "meaning": "对他人施加作为、迫使他人进入自己设定的处境的能力；作者称爱不是这种东西。", "evidence": "P014", "ambiguity": "仅以英文 power 括注，未定义边界。"},
    {"term": "侵犯", "meaning": "主动对别人做任何事（含自认为有帮助的事）的第一性性质，必然发生；“被算为好”只是第二性、不必然。", "evidence": "P015", "ambiguity": "“任何事”的外延未限定（P015）。"},
    {"term": "枷锁", "meaning": "为不伤人而自愿接受的自我限制，作者以此区分天使与魔鬼。", "evidence": "P020", "ambiguity": "“枷锁”的具体内容与可豁免情形未说明。"},
    {"term": "赌局", "meaning": "以他人的命运为筹码、由自己下注的行为；作者用它指代未经同意的主动干预。", "evidence": "P017", "ambiguity": "比喻性用法，未界定何种干预算“开设赌局”。"},
    {"term": "贪", "meaning": "作者对折中式干预背后动机的判定——“不甘心没回报”。", "evidence": "P032", "ambiguity": "属于对动机的判断，本文未提供可核查依据。"}
   ],
   "examples_and_targets": [
    {"item": "直接打一笔钱给对方（对方没开口要）", "role": "作者例证：说明什么叫“主动”（P008）"},
    {"item": "准备好一笔钱，告诉对方需要可以领走", "role": "作者例证：说明什么叫“主动的被动”（P009）"},
    {"item": "准备好一笔钱设立一个工作并告知正在招人", "role": "作者例证：升一级的主动的被动，增加“不感激权”（P010）"},
    {"item": "准备好一笔钱掉在对方家门口被其捡到", "role": "作者例证：再增加“不知情权”（P011）"},
    {"item": "讲道理时的两种做法：放在别人会去寻找答案的地方等对方来寻找／直接发到对话框、私信、把人堵在房间里或饭桌上", "role": "作者例证（正例与反例）（P022-P023）"},
    {"item": "“魔鬼”与“天使”", "role": "修辞材料：用于把“肯不肯自戴枷锁”确立为区分标准（P020）"},
    {"item": "“赌局”“下注”", "role": "比喻材料：描述未经同意的主动干预（P017-P018）"},
    {"item": "“贪”", "role": "修辞性断语：对折中干预动机的概括（P032）"}
   ],
   "conditions": [
    "作者的行动准则面向“爱”这一目标：只有在“爱想要不演变成一种他人的灾难”的前提下，严守被动才是“唯一的选择”（P033）。",
    "主动行为仍被允许，但限定其目的：努力须“为了留给对方最大的选择余地，为了创造最好的‘被动’”（P034）。",
    "让步条件：被动会带来“眼看着危险，只能干着急”以及理论上主动一点就可免除的对方灾难与痛苦（P025）。",
    "解除限制的条件性后果：一旦自行解除限制，就“将没有任何有效的论证可以证明”干涉之痛小于所避之痛（P026）。",
    "确定性对比：对方是否遭受预想的痛苦“不好说”，侵犯自主权则确定无疑（P027）。",
    "适用范围：作者称“主动逻辑”在“你想实施的一切干涉情境下，全部有效”（P027-P028）。",
    "对折中方案的否定是无限定的：任何“某些情况下主动”的划分都会自动被视为“非常有必要合理干预”（P031）。",
    "对读者的提醒以反问与告诫形式给出，未标明例外人群或紧急情形（P018-P020、P024）。"
   ],
   "rhetoric_and_tone": "格言体、短句断言，层层递进；大量反问（“你觉得这是爱吗？”“此时魔鬼和天使有何区别？”）与第二人称的提醒、警告（“提醒你一下”“看清楚”）；用“红线”“枷锁”“赌局”“贪”等比喻；结尾以“爱是主动的被动／爱是被动的”回环收束，带训诫与劝服色彩。",
   "unresolved_questions": [
    "提问者只问“爱是主动，这个观点对吗”，未说明其依据与语境；作者全文面向“爱是主动”这一说法作答，但未指名或引用具体出处。",
    "本文未给“爱”正面定义，仅以被动准则与例子反推；也未说明被动原则是否存在例外（如紧急救助、对未成年子女、对方无力自主的情形）。",
    "P025 承认“眼看着危险，只能干着急”是真实代价，但本文未给取舍标准，只在 P026-P028 以论证不可行来否定解除限制。",
    "P004 的“不知情权、不参与权、不接受权、不赞赏权、不回报权”是作者自造术语，本文未逐一定义或举例。",
    "作者称“主动的对别人做任何事”都首先是侵犯（P015），但未界定“任何事”的边界与“侵犯”程度差异。",
    "P031 断定折中方案的动机“终究不过是‘不甘心没回报’”，属于对他人动机的判定，本文未提供可核查证据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "爱是被动的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "它是一种主动作为的被动。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "它永远竭尽全力保留对方的不知情权、不参与权、不接受权、不赞赏权、不回报权", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "它的全部行动准则都要严守这条红线", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "这个叫主动的被动。因为拿这笔钱的主动权在对方手里，对方可以选择不要。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "这是升一级的主动的被动", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "对方不但有选择权，而且有不感激权、还有不知情权。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "你越向这个方向进发，你越是接近于爱。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "因为爱不是一种权力（power）。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "都首先是一种侵犯", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "侵犯是第一性的，是必然的；被算为“好”是第二性的，是不必然的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "你没有权利强迫别人加入你的赌局", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "一个人仅仅凭着“自信有一定概率能让你受益”就径直开设赌局", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "那么一切对人的侵犯和干涉就只需要加上这种“自信”就可以彻底正当化。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "肯不肯为不伤人而自愿戴上这“枷锁”，就是这区别。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "爱是尽最大的主动，去做尽可能被动的事。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "放在别人会去寻找答案的地方，等别人需要这答案时来寻找。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "凭着对方躲不开与你的对话流，强行放进对方不得不看到的地方", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P024", "quote": "“出于善意”，并不表示这不是一种冒犯。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P025", "quote": "大量的“眼看着危险，只能干着急”", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P026", "quote": "将没有任何有效的论证可以证明，因你的干涉而起的痛苦和折磨会小于你所“避免”掉的“痛苦和折磨”。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P027", "quote": "但是你侵犯了对方的自主权，这一点是板上钉钉、确定无疑的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "你对人的干涉就再也没有逻辑有效的休止符", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P028", "quote": "它在你想实施的一切干涉情境下，全部有效。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P029", "quote": "某些情况下我主动，某些情况下我坚守被动。", "relation": "context"},
    {"key": "E26", "paragraph_id": "P030", "quote": "那只是换汤不换药。", "relation": "contradicts"},
    {"key": "E27", "paragraph_id": "P031", "quote": "都会自动成为“非常有必要合理干预”的情形", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P031", "quote": "终究不过是“不甘心没回报”这几个字而已", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P033", "quote": "爱想要不演变成一种他人的灾难，唯一的选择就是严守被动。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P034", "quote": "但这种努力是为了留给对方最大的选择余地，为了创造最好的“被动”。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P035", "quote": "爱是无声的把全世界放在对方伸手可及的地方，等对方来拿。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德哲学", "情感与爱", "人际关系与界限"],
   "issue_candidates": ["爱是否等于主动", "帮助/干预他人的正当性", "自主权与知情权", "善意与冒犯的界线", "动机（回报期待）与贪"],
   "text_function_candidates": ["答疑", "论辩", "格言式说理"],
   "object_candidates": ["提问者（未具名）", "泛指的“对方”/被爱者", "泛指的“你”/施爱者"],
   "working_keywords": ["主动的被动", "被动", "侵犯", "赌局", "枷锁", "自主权", "不知情权", "不感激权", "贪"]
  },
  "notes": "无图片、正文完整（37 段，无 text/lexical 结构分歧）。提问者问题仅一句，全篇为作者回应；文中“你”“对方”均为泛称，无具名人物与可核查事实。"
 },
 "e59be25c": {
  "analysis": {
   "question_context": "提问者问“起步晚的人生还有救吗?”（Q001），即在与同龄人比较中感到进度落后的人生是否还有出路；提问者未展开自己的判断。作者以编号条目作答，标出“第一”“第二”两点：第一点重排“起步晚”的衡量标准并否定用身体/可持续性换抢先一步；第二点只写出标题式提问“什么叫‘有救’？”，正文即结束。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "第一点开头：起步晚不晚不按出生算而按死亡算；以同年出生、寿命长10年的假设说明进度差可被寿命差抵消。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "给出理由：现代科技发展、经济繁荣、寿命延长与老年生活质量提高可期，因此“早年用拼身体换比同龄人快一步”是错误策略；保养得当可在50、60岁保持30、40岁的工作能力，且医疗进步、社会服务发展、工作脑力化还能延长时间。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "许多“再不赶上就来不及”的节点（18岁考大学、25岁结婚）并不成立；但承认生理性事务（如女性生育）确有客观时间限制，并指现代医疗提供了延长/延后的选择。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "自问“不要用身体换快一步”是否只适用于身体，回答身体只是可持续性的重要因素之一，真正答案是不要用可持续性换“抢先一步”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"], "summary": "举例说明还不要拿信誉、财务可持续性（澳门赌场、“倾家荡产创业”）去换抢先一步，并以“抢什么抢，死得比发得还快”作结。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P015"], "summary": "提出第二点“什么叫‘有救’？”，正文到此结束，第二点内容未展开。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "起步晚不晚，不是按出生算的，而是按死亡算的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "假如与某甲同年出生而寿命比某甲长10年，那么某甲20岁做到的，你30岁做到也不迟。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“早年用拼身体来换比同龄人快一步”是一个错误的策略（理由：现代科技发展、经济繁荣、寿命延长与老年生活质量提高都可期）。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果保养得当，完全可以在50岁甚至60岁保持和30、40岁相近的工作能力；若考虑医疗技术进步、社会服务体系发展与未来人类工作的脑力化趋势，这个时间还可以延长。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "很多被视为“再不赶上就来不及了”的节点对你并不成立：并非非要18岁考上大学，也不是“25还不结婚就来不及了”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "确实存在步调问题的主要是生理性事务（如女性的生育问题），确有客观时间限制；但即使这一点，现代医疗技术也提供了延长生育期限、延后生育行为的选择。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "身体只是可持续性中的一个重要因素；“不要用身体换快一步”的真正答案是不要用可持续性换“抢先一步”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "也不要拿抛弃信誉或财务可持续性去换抢先一步（如跑去澳门赌场或“倾家荡产创业”）。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对“抢先一步”的做法给出贬评性警告：抢什么抢，死得比发得还快。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者提出第二点“什么叫‘有救’？”，但正文未给出回答。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "先重排衡量尺度：起步晚不晚按死亡而非出生计算（P001）。",
    "以假设例证说明：同年出生而寿命长10年，则20岁做到的30岁做到也不迟（P003）。",
    "给出趋势性理由：现代科技发展、经济繁荣、寿命延长、老年生活质量提高可期，因此“用拼身体换快一步”是错误策略（P004）。",
    "延伸条件：保养得当时50、60岁可保持30、40岁的工作能力；医疗进步、社会服务发展、工作脑力化趋势还能延长时间；职业生涯比父辈、祖父辈长很多（P005）。",
    "否证常见节点：即使晚几年考大学也来得及，并非25岁不结婚就来不及（P006-P007）。",
    "让步并限定：确有生理性事务（如女性生育）存在客观时间限制，但现代医疗也提供延长/延后的选择（P008）。",
    "自问自答扩大范围：身体只是可持续性的一个因素，真正的答案是不用可持续性换“抢先一步”（P009-P011）。",
    "举例补充：不要拿信誉、财务可持续性（澳门赌场、“倾家荡产创业”）换抢先一步（P012-P013）。",
    "以口语化断言收束第一点：“抢什么抢，死得比发得还快”（P014）。",
    "提出第二点“什么叫‘有救’？”后正文结束，未继续论证（P015）。"
   ],
   "concept_usage": [
    {"term": "起步晚", "meaning": "相对同龄人的进度落后；作者主张以死亡为终点而非以出生为起点来衡量，故“晚”的判断取决于寿命差。", "evidence": "P001", "ambiguity": "未说明如何预知自身寿命，也未界定除寿命外是否还有其他衡量维度。"},
    {"term": "有救", "meaning": "提问者使用的词；作者在 P015 追问“什么叫‘有救’？”但正文未给出定义或答案。", "evidence": "P015", "ambiguity": "文中无界定，第二部分缺失。"},
    {"term": "可持续性", "meaning": "身体、信誉、财务等可长期维持的因素，作者视之为不应被牺牲以换取速度的东西。", "evidence": "P010", "ambiguity": "仅列举三类，未给出统一判据。"},
    {"term": "抢先一步／快一步", "meaning": "以牺牲可持续性为代价换取相对同龄人更快的进度；作者判定为错误策略。", "evidence": "P004", "ambiguity": "未界定“一步”的度量与比较对象范围。"},
    {"term": "生理性的事务", "meaning": "存在客观时间限制的事务，作者以女性的生育问题为例。", "evidence": "P008", "ambiguity": "仅给一例，未说明是否还有同类事项。"}
   ],
   "examples_and_targets": [
    {"item": "“某甲”（与读者同年出生的假想同龄人）", "role": "作者假设例证：用寿命差说明进度差可被抵消（P003）"},
    {"item": "18岁考上大学、25岁结婚", "role": "反驳对象：被视为“来不及”的节点，作者称并不成立（P007）"},
    {"item": "女性的生育问题", "role": "作者承认的例外/客观时间限制，并以现代医疗技术部分缓解（P008）"},
    {"item": "跑去澳门赌场、“倾家荡产创业”", "role": "作者反面例证：拿财务可持续性换抢先一步（P013）"},
    {"item": "现代科技发展、经济繁荣、寿命延长、老年生活质量提高", "role": "作者的趋势论据（P004）"},
    {"item": "医疗技术进步、社会服务体系发展、未来人类工作的脑力化趋势", "role": "作者的趋势论据，用于延长可工作年限的判断（P005）"},
    {"item": "父母这一代、祖父这一代", "role": "比较材料：说明当代职业生涯可比上一代长很多（P005）"}
   ],
   "conditions": [
    "假设条件：“假如你跟某甲同年出生，但是你比某甲寿命长10年”（P003）。",
    "条件性判断：“如果你保养得当，你完全可以在50岁甚至60岁年纪保持和30、40岁相近的工作能力”（P005）。",
    "前瞻条件：若考虑医疗技术进步、社会服务体系发展与工作脑力化趋势，“这个时间还可以延长”（P005）。",
    "限定：确有步调问题的主要是生理性事务，其中女性生育“的确是有客观的时间限制的”（P008）。",
    "缓解条件：即使生育这一点，“现代医疗技术也提供了不少可以延长生育期限、延后生育行为的选择”（P008）。",
    "全篇结构条件：只完成“第一”点的论述；“第二，什么叫‘有救’？”之后无正文（P015）。",
    "对“有救”的最终结论：本文未给出（P015）。"
   ],
   "rhetoric_and_tone": "直接答疑、编号条目式（“第一…第二…”）；用“你”“某甲”“ta们”称呼；短句断言夹反问（“啥意思呢？”“只适用于身体吗？”）；口语化贬评收束（“抢什么抢，死得比发得还快”）；结尾以“第二，什么叫‘有救’？”戛然而止。",
   "unresolved_questions": [
    "正文止于 P015“第二，什么叫‘有救’？”，第二点的回答在语料中缺失；brief 亦在“所以‘早年用拼身体来换比同龄人快一步’是一个”处截断，疑为源记录截断/文章未完，需外部核查原始页面。",
    "提问者所说“有救”的具体含义未说明，作者在 P015 追问后未作答，故全篇未对“起步晚的人生还有救吗”给出直接结论。",
    "P001 以死亡年龄衡量起步早晚，依赖对自身寿命的预知，本文未说明如何得知。",
    "P004-P005 引用的科技、经济、寿命、医疗、工作脑力化等趋势未提供数据或来源，属待外部核查的事实性断言。",
    "P008 提到现代医疗“提供了不少可以延长生育期限、延后生育行为的选择”，未具体说明是哪些选择。",
    "“可持续性”仅以身体、信誉、财务三类举例，未说明是否还有其他类别及其优先顺序。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "第一，起步晚不晚，不是按你出生算的，是按你死亡算的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "假如你跟某甲同年出生，但是你比某甲寿命长10年，那么某甲在20岁做到的，你30岁做到也不迟。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "所以“早年用拼身体来换比同龄人快一步”是一个错误的策略。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "你完全可以在50岁甚至60岁年纪保持和30、40岁相近的工作能力", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "以及未来人类工作的脑力化趋势，这个时间还可以延长", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "很多ta们觉得“再不赶上就来不及了”的所谓节点，对你而言并不成立。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "你也并不是“25还不结婚就来不及了”。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "那的确是有客观的时间限制的", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P008", "quote": "现代医疗技术也提供了不少可以延长生育期限、延后生育行为的选择", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P010", "quote": "身体只不过是可持续性中的一个重要因素。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "真正的答案是不要用可持续性换“抢先一步”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "你也不要拿抛弃信誉换抢先一步。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "你也不要拿财务可持续性去换抢先一步——比如跑去澳门赌场或者“倾家荡产创业”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "抢什么抢，死得比发得还快。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "第二，什么叫“有救”？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生规划/生涯发展", "时间管理与健康", "社会经济趋势"],
   "issue_candidates": ["起步晚与年龄焦虑", "用健康换速度", "可持续性与抢先一步的取舍", "生育的时间窗口", "长寿与职业周期"],
   "text_function_candidates": ["答疑", "经验总结", "劝告"],
   "object_candidates": ["提问者（未具名）", "“某甲”（假想同龄人）", "女性（生育问题）", "父母这一代/祖父这一代"],
   "working_keywords": ["起步晚", "有救", "可持续性", "抢先一步", "拼身体", "寿命", "生理性的事务", "脑力化"]
  },
  "notes": "无图片。正文仅 15 段，止于“第二，什么叫‘有救’？”且 brief 亦在句中截断（“…是一个”），疑为源记录截断或文章未完成，第二点内容缺失，需外部核查原始页面；已读部分为现存全部正文文本，未据标题或问题补写缺失内容。"
 },
 "09575f9e": {
  "analysis": {
   "question_context": "提问者问“诚实有没有度？那个度是什么？”（Q001）。作者先否定“诚实＝说心里话／说真话”式抽象原则（称其无可操作性），再以“会导致别人‘诚实’评价的行为模式”重立方法论，把实践意义上的诚实定义为“事实保险业务”，最后答“度”即“谱”（有谱、靠谱）；文中另有相当篇幅是对“家长”的训诫与对“你自己”的劝说。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "定义诚实为“会导致别人‘诚实’评价的行为模式”；批评“说心里话／说真话”式抽象原则没有可操作性。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "反问论证“心里话”与“真话”都无法自行分辨（爱/恨、信/疑、强烈觉得≠真、听不懂与做不到可能有不想的成分），故建立其上的诚实实践从根上不诚实。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "替代方法论：研究人们认可为诚实的行为模式的共性，反向得出实践含义；诚实是有规矩的。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "不知真相时，实践意义上的诚实是“事实保险业务”：发出见证即承保，投保人以好意、信用作报酬，风险发生则兑付约定赔偿；诚实＝承保人充分履行承诺责任的状态。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046"], "summary": "要点一“保险事项要界定清晰”：保险合同式清晰表述与“我爱你／相信你／坏话”等模糊担保对比；界定不清必得“不诚实”评价（双方按各自利益定义、裁判权在对方）；以“公园风很大”之争为例。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062"], "summary": "对策：技术上用“有准头的话”（可判定赔偿责任是否生效的工具）并举改写例；战略上避免向爱不足者提供该服务，界定成本与对方的爱成反相关，描述能力不足可靠对爱的敏感弥补。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075"], "summary": "要点二“赔偿责任要明确”：责任是风险发生后的赔偿而非保证绝对为事实；区分“告知信息”与“事实担保”，诚实即“若它不正确，你承诺按你的声言补偿”。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090"], "summary": "反驳“他人有义务告诉自己绝对真理、不应验即可裁断欺骗”之说：他人无当然告知担保义务，验证与兑现是投保人自己的责任；唯一可指责处是对方不履行自己声明的责任；把完美为真当作理所当然义务是暴虐。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114"], "summary": "家长训诫：该标准等于要子女举泰山再判其罪，将导致失望、被恨、被看穿虚伪；子女会继承此理念苛求自己与他人，最终被当作“绝不可交谈”的信息贱民驱逐。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P115", "P116", "P117", "P118", "P119", "P120", "P121"], "summary": "对“你自己”的第一条理由：不改则无人愿冒“不诚实”风险告知你义务以外的信息，而别人有义务告诉你的东西少到几乎没有。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P122", "P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130", "P131", "P132", "P133", "P134", "P135", "P136", "P137", "P138"], "summary": "第二条理由：“大众”多半只是“我们村”；概念分幼年版（只适用于人为控制的特化环境）与成年版（适用于“旷野”）；多数人被困幼年版；多数人看法相同不能证明其正确，因正是这一样的看法导致了一样的痛苦。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P139", "P140", "P141", "P142", "P143", "P144", "P145", "P146", "P147", "P148"], "summary": "第三条理由：运营“有限责任诚实观”需大量练习，本质是敏捷的“起草保险合同”能力；说话要给出判定是否兑现的方法与责任，角色已定责任时比着尺度说话，天然无责任时明确免责（以“素问”置顶说明为示范）。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P149", "P150", "P151", "P152"], "summary": "结论：越成熟越不在意对方是否诚实，而在意是否有谱、是否靠谱；“谱”就是诚实的“度”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "诚实是一种会导致别人的“诚实”评价的行为模式。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“诚实就是说心里话／说真话”这类抽象原则没有可操作性，不应作为思考诚实的起点。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "“心里话”与“真话”都无法自行分辨：爱/恨、信/疑都可能是心里话，强烈觉得≠真，听不懂与做不到背后可能是不想听、不想做。", "evidence": ["E4", "E5", "E6", "E7", "E8"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“诚实就是讲真话”要求你自己能分辨真话，而你没有这个能力；凡建立在这两个前提上的诚实实践，从根上就是傲慢、虚伪和不诚实的。", "evidence": ["E10", "E11"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应循“诚实是会导致ta人评价‘诚实’的行为模式”这一方法论：研究人们认可为诚实的行为模式的共性，反向得出实践含义；诚实是有规矩的。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实践意义上的诚实是“事实保险业务”：发出见证即承保，投保人以好意、信用作报酬，风险发生则兑付约定赔偿；诚实＝承保人充分履行其承诺责任的状态。", "evidence": ["E16", "E17", "E19"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要点一：保险事项（你所担保的事实内容）要界定清晰。", "evidence": ["E20"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "界定不清时你注定会得到“不诚实”的评价：无爱时双方各按对自己有利的定义认定事实、定义分离，而判定犯规的裁判权在对方手上。", "evidence": ["E21", "E22", "E23"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术上要“说有准头的话”：靠提供判定赔偿责任是否生效的工具，如“公园的旗子就没有静止的时候”；“准头”即可清晰界定是与否的鉴定工具。", "evidence": ["E25", "E26", "E28"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "战略上要避免向没有足够爱的对象提供该服务；有爱的人较少按自己利益定性，判定标准可能接近甚至重合；描述成本与对方的爱成反相关，描述能力不足可靠对爱的敏感弥补。", "evidence": ["E29", "E30", "E31", "E32"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要点二：赔偿责任要明确；你并不保证所担保事项绝对为事实，真正的责任是风险发生后向对方赔偿（如保险公司不保证你不得癌症）；不承担无限责任就要界定清楚被证伪时的补偿。", "evidence": ["E33", "E34", "E35"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要区分“告知信息”与“对信息真实性作担保”：诚实并非信息一定正确，而是“若它不正确，你承诺按照你的声言补偿对方”；诚信体现在对方是否承担自己声明的（而非你给对方定义的）责任上。", "evidence": ["E36", "E37", "E38", "E39"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "unknown", "modality": "asserted", "statement": "作者转述并反驳的一种立场（他称为“小孩子们”最容易犯的致命错误）：自认为所有人都有义务告诉自己绝对真理，并有权在一切“不应验”时自由裁断对方“欺骗”的罪。", "evidence": ["E40", "E51"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人对你没有任何当然的告知、担保义务；单纯告知你你已经赚了；验证真假、让它兑现成为你的福利都是你的责任；你没有资格嫌赔偿少或追加报复。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你唯一能指责对方不诚实的地方，是按其自己给出的判定标准没有符合事实时，对方没有履行自己承诺的担保责任。", "evidence": ["E44", "E45"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人从根本上不能保证所言为实，把“完美为真”当作人类理所当然的义务是暴虐的；把“不可能为真”视为“不诚实”对青少年尤其苛刻，等于要子女举起泰山再因其举不起判其道德罪。", "evidence": ["E46", "E47", "E48"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若坚持该判定，你必定终身失望乃至绝望、被子女恨并被视为虚伪（你自己也达不到该标准）；子女会继承此理念苛求自己与他人，最终被当作“绝不可交谈”的信息贱民驱逐。", "evidence": ["E49", "E50", "E52"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不改的第一条现实理由：将没有人愿意冒着“不诚实”的风险告诉你义务以外的信息，而人家有义务告诉你的东西少到几乎没有。", "evidence": ["E53", "E54"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“大众”多半只是“我们村”的代称；概念分幼年版（只适用于人为控制的特化环境）与成年版（适用于“旷野”）；大部分的人一生被困在幼年版，三十岁后因负担家庭领导管理责任才被现实叫醒。", "evidence": ["E55", "E56", "E58", "E59"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谈伦理不能以“大部分人都和我的看法一样”证明“我的看法是对的”，因为不幸福、受制于人的也是大多数，而正是这一样的看法导致了一样的痛苦；抱着旧概念问也无用。", "evidence": ["E60", "E61", "E62", "E63"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "运营“有限责任诚实观”需大量练习，本质是敏捷的“起草保险合同”的能力；说负责任的话要给出判定是否兑现的方法与愿承担的责任；角色已定责任时比着尺度说话，天然无责任时明确说明免责。", "evidence": ["E64", "E65", "E66", "E67"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "练熟后可据有该习惯者给出的反馈（一系列“事实保险合同”）管理风险，经济安全近乎“事实保险组合合约的连续套利操作”；越成熟越不在意对方是否诚实，而在意是否有谱、是否靠谱——“谱”就是诚实的“度”。", "evidence": ["E69", "E70", "E71", "E72"]}
   ],
   "argument_steps": [
    "设问并定义：诚实是一种会导致别人的“诚实”评价的行为模式（P001-P002）。",
    "否定通行前提：“说心里话／说真话”没有可操作性（P004-P006）。",
    "拆解“心里话”与“真话”：爱/恨、信/疑皆可为心里话；强烈觉得≠真；听不懂、做不到可能源于不想（P007-P016）。",
    "反证：该前提要求自能分辨真话而人无此能力，故其上的诚实实践从根上不诚实（P017-P021）。",
    "替代方法论：研究人们认可为诚实的行为模式的共性，反向求实践含义；诚实是有规矩的（P022-P025）。",
    "答“不知真相时诚实是什么”：实践意义上的“事实保险业务”——承保、投保、好意信用作报酬、约定赔偿（P026-P029）。",
    "要点一：保险事项须界定清晰，以保险合同表述与“我爱你／相信你／坏话”为正反例（P030-P037）。",
    "推论：界定不清必得“不诚实”评价，因定义分离而裁判权在对方；“公园风很大”之争即例（P038-P046）。",
    "对策（技术）：用有“准头”的表述提供判定赔偿责任的工具（P047-P055）。",
    "对策（战略）：避免向爱不足者提供服务；成本与对方的爱成反相关，可用对爱的敏感弥补描述能力不足（P056-P062）。",
    "要点二：赔偿责任要明确，责任是风险发生后的赔偿而非保证绝对为事实（P063-P066）。",
    "区分告知信息与事实担保，把诚实落实为“若它不正确，你承诺按照你的声言补偿对方”（P067-P075）。",
    "反驳儿童式诚实观：他人无当然告知担保义务，验证与兑现是投保人自己的责任；唯一可指责处是对方不履行自己声明的责任（P076-P088）。",
    "根本理由：人不能保证所言为实，把“完美为真”当作理所当然义务是暴虐（P089-P090）。",
    "用于家长：该标准等于要子女举泰山再判其罪，将导致失望、被恨、被看穿虚伪（P091-P096）。",
    "推演代际后果：子女继承此理念苛求自己与他人，最终被当作“信息贱民”驱逐（P097-P114）。",
    "对“你自己”的三条理由：不改则无人愿告知义务以外的信息（P115-P121）；“大众”只是“我们村”，多数不证明正确（P122-P138）；运营有限责任诚实观需大量练习（P139-P148）。",
    "结论：以“谱”（有谱、靠谱）代替“诚实”，“谱”就是诚实的“度”（P149-P152）。"
   ],
   "concept_usage": [
    {"term": "诚实", "meaning": "本文先定义为“会导致别人的‘诚实’评价的行为模式”，再在实践意义上定义为承保人充分履行“事实保险业务”承诺责任的状态。", "evidence": "P002", "ambiguity": "两种定义在对方恶意或坚持己方定义时如何取舍，本文未整合说明。"},
    {"term": "心里话／真话", "meaning": "通行诚实观的两个前提；作者认为二者都无法由自己分辨，故不可作实践标准。", "evidence": "P004", "ambiguity": "未正面给出“真话”的可操作定义，只以“有准头的话”替代。"},
    {"term": "事实保险业务", "meaning": "把“向人发出见证”类比为开发专项保险业务：你是承保人，对方是投保人，以好意与信用付酬，风险发生则兑付约定赔偿。", "evidence": "P028", "ambiguity": "“约定赔偿”的形式与非交易关系中的适用方式未举例。"},
    {"term": "担保／赔偿责任", "meaning": "对陈述真实性所作的正式承诺及其违约后果；作者以此区分“信息提示”与“事实担保”。", "evidence": "P073", "ambiguity": "“社会契约默认无可追责”的范围（P074）未界定。"},
    {"term": "准头", "meaning": "可供清晰界定是与否的鉴定工具，即让赔偿责任是否生效可判定的表述方式。", "evidence": "P055", "ambiguity": "未给出判断某表述是否有准头的统一尺度。"},
    {"term": "幼年版／成年版（概念）", "meaning": "幼年版是幼儿期接收的简化版本，简单粗暴、分明，只适用于人为控制的特化环境；成年版复杂含糊，适用于“旷野”。", "evidence": "P124", "ambiguity": "两者的转换条件与判定标准未给出。"},
    {"term": "有谱／靠谱／谱", "meaning": "有谱＝说话做事自动附带可执行的责任界定；靠谱＝主动承担自己给出的事实保险合同的保险责任；“谱”用来代替“诚实”，即其“度”。", "evidence": "P151", "ambiguity": "“谱”如何度量、能否分级未说明。"},
    {"term": "爱", "meaning": "本文中作为影响对方如何对事实定性的因素：有爱的人较少按自己利益定性，故界定成本与对方的爱成反相关。", "evidence": "P057", "ambiguity": "全文未定义“爱”，也未给出判别对方“有没有足够爱”的方法。"}
   ],
   "examples_and_targets": [
    {"item": "保险合同担保“活到70岁”“八十岁前不得大病并列清单”", "role": "作者例证：清晰界定的正面示例（P033-P034）"},
    {"item": "担保“我爱你”“我真的相信你”“某甲在背后说你的坏话”", "role": "作者例证：界定不清的示例（P035-P037）"},
    {"item": "“今天公园风很大”之争：一方指旗子没静止，另一方指风筝要助跑才能升空", "role": "作者例证：定义分离导致被判“不诚实”（P043-P044）"},
    {"item": "改写为“公园的旗子就没有静止的时候”“ta已经进了重症监护室”等", "role": "作者例证：有准头表述的示范（P049-P052）"},
    {"item": "保险公司不保证你不得癌症，只在癌症发生时提供约定保险金", "role": "作者类比：担保责任是赔偿而非保证事实（P065）"},
    {"item": "“这要不是真的，赔你10块钱”，事后证明不真而未赔", "role": "作者例证：不诚实体现在不履行赔偿责任（P088）"},
    {"item": "“要求子女举起泰山，然后因其举不起判其道德罪”", "role": "作者类比：批评把不可能之事当作义务（P093）"},
    {"item": "“信息贱民”“直接驱逐”“阿鼻地狱里哀嚎”", "role": "修辞材料：描述继承残暴诚实观的后果（P098-P110）"},
    {"item": "“如何用负数相加得到100”", "role": "作者类比：抱旧概念提问徒劳无益（P138）"},
    {"item": "“我们村”“幼儿园、学校一样的环境”“旷野”“丛林般的市场和社会现实”", "role": "作者比喻：幼年版与成年版概念的适用环境（P122-P125）"},
    {"item": "“素问自己的置顶说明”", "role": "作者举的示范：免责说明的实例（P145）；“素问”主体未说明"},
    {"item": "“事实保险组合合约的连续套利操作”", "role": "作者比喻：长期管理风险后的经济安全状态（P148）"}
   ],
   "conditions": [
    "条件性后果：界定不清晰时“你注定会得到‘不诚实’的评价，绝无任何悬念”（P038）。",
    "前提条件：对方按偏向其利益的定义认定事实，是“在没有爱来压制ta自己自保的恐惧的前提下”（P039）。",
    "结构性条件：界定不清时“判定犯规的裁判权却在对方手上”（P040），故“你一定会被判定犯规”（P041）。",
    "技术条件：描述清晰“不是看你的自我感觉，而是靠提供一种判定赔偿责任是否生效的工具”（P048）；“只有说有准头的话你才有可能不落入这个结局”（P054）。",
    "战略与成本条件：要谨慎避免向没有足够爱的对象提供该服务（P056）；在结果正面的前提下，成本与对方的爱成反相关（P060-P061）。",
    "责任限定条件：“如果你不打算承担无限责任，那么你一定要界定清楚如果对方发现这不是事实时你会付出的补偿是什么”（P066）。",
    "角色条件：责任已被职责、角色规定好时比着这个尺度说话（P143）；角色天然没有责任时要明确说明“我这些话是没违约责任的”（P144）。",
    "练习与对象条件：运营有限责任诚实观需大量练习（P139），长期有效反馈来自有该习惯与训练的人，构成“靠谱之人”的世界（P146-P148）。"
   ],
   "rhetoric_and_tone": "讲义式设问—自答推进（“诚实到底是什么？”“什么叫心里话？”“问题来了……”）；以保险业术语（承保、投保、兑付、理赔、套利）贯穿全篇作概念骨架；大量第二人称训诫与反问（“家长们，你们仔仔细细地听清楚”），兼用排比、夸张与讽刺（“大摇大摆的坐在王座上，等着四方‘臣子’向你进贡真理”“信息贱民”“阿鼻地狱里哀嚎”）；口语化贬评（“谁活腻了肯跟你玩这种游戏？”）；结尾以定义句收束。",
   "unresolved_questions": [
    "提问者问“度是什么”，作者最终以“谱”作答，但“谱”的判定标准、分级与边界仍以“可执行的责任界定”描述，未给出可操作的量表。",
    "作者先用“会导致别人的‘诚实’评价”定义诚实（P002），后以“履行自己声明的担保责任”定义（P029、P075）；当对方坚持自己的定义并握有裁判权时（P044）以何者为准，本文未整合说明。",
    "P145“你们都知道素问自己的置顶说明”——“素问”指谁/哪个账号、置顶说明原文为何，本文均未说明，需外部核查。",
    "P028-P029 的保险类比中，“好意、信用作为报酬”与“约定赔偿”在亲情、友情等非交易关系中的具体形式，本文未举例说明。",
    "P039 以“有没有爱”作为对方如何对事实定性的前提，但全文未定义“爱”，也未给出判断对方“有没有足够爱”的方法，可能影响该战略建议的可操作性。",
    "P122-P130 关于“大众只是我们村”“大部分的人一生被困在幼年版认知”的判断属社会性断言，未提供数据或来源，需外部核查。",
    "P090 称“确保所言绝对非虚”是“全知全能的神才能做到的神迹”，属修辞性表述，未给出论证细节。",
    "作者的写作对象在“家长们”（P091）与“你自己”（P115）之间切换，文中“ta们”“小孩子们”的所指群体边界不明。",
    "本文未单独讨论“明知为假仍作担保”即故意欺骗的情形，只区分了信息提示与事实担保两类行为。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "诚实是一种会导致别人的“诚实”评价的行为模式。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "“诚实就是说心里话”“诚实就是说真话”这类抽象的原则", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "这些话根本没有可操作性，说了等于没说", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "你以为你爱ta是心里话，那么你恨ta就不是心里话？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "自以为了解自己的心，你知道这有多傲慢吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "你强烈的觉得你应该减肥，你减了几斤？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "只要不觉得是假话，就一定是真话吗？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "还是因为不想听懂、没有听，所以听不懂？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "必须要你自己能分辨什么是真话", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "从根上就是傲慢、虚伪和从根本上不诚实的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "诚实是会导致ta人评价‘诚实’的一种行为模式", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "从这里去反向得出诚实的实践层面上的含义", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "诚实是有规矩的，搞清楚这些规矩，并且按规矩行事", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P027", "quote": "在实践意义上是一种“事实保险业务”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P028", "quote": "你本质上是开发了一项专项保险业务。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "承保人充分向投保人履行其事实保险业务的承诺责任的状态", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P031", "quote": "第一，保险事项要界定清晰。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P038", "quote": "你注定会得到“不诚实”的评价", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P039", "quote": "对方一定会按照偏向ta的利益而非偏向你的利益的定义", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P040", "quote": "判定犯规的裁判权却在对方手上。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P048", "quote": "靠提供一种判定赔偿责任是否生效的工具", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P049", "quote": "你应该说“公园的旗子就没有静止的时候”。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P055", "quote": "是一种可供清晰界定是与否的鉴定工具", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P056", "quote": "谨慎地避免向没有足够爱的对象提供这项服务", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P057", "quote": "有爱的人会较少的按照ta自己的利益", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P060", "quote": "这个成本和对方对你的爱成反相关。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P062", "quote": "可以靠对对方爱的水平的敏感弥补。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P063", "quote": "第二，赔偿责任要明确", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P064", "quote": "是在该担保事项发生风险后，向对方承担赔偿责任", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P066", "quote": "如果对方发现这不是事实时你会付出的补偿", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P069", "quote": "2）你对这信息的真实性做了一定的担保。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P071", "quote": "而是“若它不正确，你承诺按照你的声言补偿对方”。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P074", "quote": "声明过不承担担保责任，或由社会契约默认无可追责", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P075", "quote": "对方是否承担自己声明的", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P077", "quote": "ta们自认为所有的人都有义务要告诉自己绝对真理", "relation": "contradicts"},
    {"key": "E41", "paragraph_id": "P080", "quote": "别人对你没有任何当然的告知、担保义务。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P082", "quote": "验证它的真假，是你的责任。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P086", "quote": "没有资格自说自话的在对方头上追加报复", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P087", "quote": "对方没有履行对方自己承诺的担保责任", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P088", "quote": "是ta没赔给你这10块钱，才构成不诚实。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P090", "quote": "任何把完美地做到这一点作为人类理所当然的义务", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P091", "quote": "把“不可能为真”视为“不诚实”", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P093", "quote": "因为你本质上是在要求子女举起泰山", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P094", "quote": "因为你自己也根本达不到你自己生成的诚实标准。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P097", "quote": "同样继承这样愚蠢而残暴的所谓“诚实”理念", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P102", "quote": "那就是“不诚实”，理当人人得而诛之。", "relation": "contradicts"},
    {"key": "E52", "paragraph_id": "P110", "quote": "直接将ta们视为“绝不可交谈”的信息贱民", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P117", "quote": "没有人愿意冒着“不诚实”的风险", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P119", "quote": "人家有义务要告诉你的东西其实是多么的少", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P122", "quote": "“大众”其实在绝大多数情况下只是“我们村”的代称", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P123", "quote": "几乎所有的概念都存在着两个版本", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P125", "quote": "在丛林般的市场和社会现实里幸存和壮大", "relation": "supports"},
    {"key": "E59", "paragraph_id": "P126", "quote": "大部分的人，一生都被困在幼年版的认知之中", "relation": "supports"},
    {"key": "E60", "paragraph_id": "P130", "quote": "不幸福的也是大多数、受制于人的也是大多数", "relation": "supports"},
    {"key": "E61", "paragraph_id": "P132", "quote": "不能将“大部分人都和我的看法一样”", "relation": "supports"},
    {"key": "E62", "paragraph_id": "P133", "quote": "因为恰恰是这一样的看法，才导致了一样的痛苦。", "relation": "supports"},
    {"key": "E63", "paragraph_id": "P138", "quote": "等于在问“如何用负数相加得到100”，徒劳无益", "relation": "supports"},
    {"key": "E64", "paragraph_id": "P140", "quote": "是一种敏捷的“起草保险合同”的能力", "relation": "supports"},
    {"key": "E65", "paragraph_id": "P142", "quote": "非常注意给出判定是否兑现的方法", "relation": "supports"},
    {"key": "E66", "paragraph_id": "P143", "quote": "你应尽的责任已经被你的职责、角色规定好了", "relation": "supports"},
    {"key": "E67", "paragraph_id": "P144", "quote": "我这些话是没违约责任的，听不听、信不信你要自己掂量", "relation": "supports"},
    {"key": "E69", "paragraph_id": "P148", "quote": "“事实保险组合合约的连续套利操作”", "relation": "supports"},
    {"key": "E70", "paragraph_id": "P150", "quote": "转而在意对方是否有谱、是否靠谱。", "relation": "supports"},
    {"key": "E71", "paragraph_id": "P151", "quote": "有谱，就是说话做事自动附带可执行的责任界定", "relation": "supports"},
    {"key": "E72", "paragraph_id": "P152", "quote": "用“谱”来代替“诚实”，“谱”就是诚实的“度”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德哲学", "语言与沟通", "契约与责任", "家庭教育", "社会认知与成熟"],
   "issue_candidates": ["诚实的定义与度", "说真话是否可操作", "担保责任与赔偿责任", "信息提示与事实担保的区分", "家长对子女的诚实要求", "多数人观念与幼年/成年版概念", "信誉与靠谱"],
   "text_function_candidates": ["答疑", "论辩", "概念重构", "训诫/劝告", "类比说理"],
   "object_candidates": ["提问者（未具名）", "家长（被训诫对象）", "子女/青少年", "“小孩子们”（指持有儿童式诚实观者）", "素问（文中提及的账号或作者自称，未说明）", "保险公司（类比对象）"],
   "working_keywords": ["诚实", "事实保险业务", "担保", "赔偿责任", "准头", "信息提示", "有谱", "靠谱", "谱", "幼年版", "成年版", "我们村", "爱"]
  },
  "notes": "无图片；正文完整（152 段，无 text/lexical 结构分歧），已通读全部段落。文中“素问自己的置顶说明”（P145）未说明“素问”是谁或哪个平台的账号，需外部核查；文中“ta们”“小孩子们”“家长们”所指群体边界不明。"
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
