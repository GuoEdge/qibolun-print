# -*- coding: utf-8 -*-
"""批次 r001-b0019 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0019.sessions.py            # 写 out/r001-b0019.out.jsonl
  python3 records/r001-b0019.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0019"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0019.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "0d2e3bdf": {
  "analysis": {
   "question_context": "提问者（Q001）问：上帝和魔鬼打赌玩弄约伯的原因是什么？这一问法（把《约伯记》读成上帝与魔鬼打赌、玩弄约伯）属于提问者。作者开篇即明确不回答上帝的动机，改问“这一篇东西为什么会存活下来，被传承两千六百年”，并从巴比伦之囚的历史处境、一神信仰的脆弱性、行善与赏赐的关系等角度给出自己的解读。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"],
     "summary": "重设问题：上帝的动机不重要，重要的是《约伯记》为何能存活两千六百年；并交代历史处境——旧约大部分在巴比伦之囚期间由犹太长老精英编辑成型，亡国为奴者除对上帝的指望别无指望，唯一能对抗民族熔炉的就是“那个指望”和对它的信心。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P006", "P007", "P008", "P009"],
     "summary": "叙述《约伯记》的正典地位：它在无数歌谣传说残片中入选，作为最令信仰者痛苦的篇章却从未被怀疑正典资格，两千六百年来信徒为它痛苦纠结而它没有被删掉，作者称之为神迹般的谜。",
     "role": "context"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"],
     "summary": "提出解读之钥：秘密不在约伯或上帝怎样，而在于绝境中的犹太人为何对令一般人无法接受的东西心有所感；约伯记的首要意义是让神的存在性与个人遭遇的“公平性”脱钩，从而彻底消除一神信仰的脆弱性。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020"],
     "summary": "指出接受此说后局面是：神仍是真实且唯一的存在，人没有选择；别的偶像更甜但是假的；某些遭遇只是历史被安排的段落，与善恶无关，因此因山拦路而喊“不相信它存在”是愚蠢且无意义的。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P021", "P022", "P023", "P024", "P025"],
     "summary": "以巴比伦作对照：其信仰中没有约伯记，败即视为被神抛弃，只能胜不能败；而因约伯记，失败对犹太民族没有额外威力，当失败不能根本伤害你时，失败就失去一切真实威力。",
     "role": "example"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036"],
     "summary": "论行善与赏赐：神的意愿不遵从人的“自以为”，约伯记是分开犹太信仰与原始偶像崇拜的第一道隔离墙，上帝不能降格为“善行交易员”；行善是无对价的义务，不是可报销的欠条；想与神谈生意者无法接受，宣称“有善必赏”的圈子是骗局。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052"],
     "summary": "论接受条款的后果：完全理解并接受约伯记的人信仰动机被清洗，善报变格为赏赐；以两种帮助者为例说明这种人是上帝安排的保障，接受条款者得到自然法则驱动的整个人类文明的护佑；并称约伯所受的苦救了无可计量的兆亿生灵，在剧情里必须是“毫无意义”。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": ["P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068"],
     "summary": "以设问转入耶稣的回答：除因恶受苦，还可能因义受苦；用间谍为例说明恰恰因为某人义，九死一生且必要的事就必须由他承担，现世没有足够回报，唯一可相信的回报是上帝在永生里的回报。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": ["P069", "P070", "P071", "P072", "P073", "P074"],
     "summary": "收束：世界依靠“傻人”的牺牲维持；约伯受折磨不是因为有罪当罚，而是放在他身上的使命；追求为义就是在追求约伯的待遇，信仰因此有了重量。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者明确不讨论故事中上帝的动机，而把问题改为《约伯记》为何能存活并被传承两千六百年；他认为解读的秘密不在约伯或上帝怎样，而在于身处绝境的犹太人为何对这种令一般人无法接受的东西心有所感。",
     "evidence": ["E1", "E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者叙述历史背景：现在公认《约伯记》是《圣经》中最古老篇章之一，有人认为它是整部《圣经》的开端；现在所见的旧约很大一部分是在公元前587～538年巴比伦之囚期间由犹太民族的长老精英编辑成型的。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判断：一般历史上这种亡国时刻民族会被同化熔解，唯一能对抗这熔炉的东西就是“那个指望”和对那唯一指望的信心。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称《约伯记》作为最令信仰者痛苦的篇章奇迹般入选，从未被怀疑正典资格；据其所见所闻，尚未有任何一个教派（哪怕异端教派）提出应把它当伪经删掉；两千六百年来没有一个信徒不为它痛苦纠结、怀疑信仰，而它没有被删掉。",
     "evidence": ["E5", "E6"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者提出约伯记首要的意义：如果你认定它是真实的，神的存在性与你的遭遇的“公平性”就脱离关联；即使自以为义人而遭厄运，逻辑上也不可再以此为理由怀疑神的存在性，因此它彻底消除了一神信仰的脆弱性，剩下的只是“这样的神有什么意义”这第二个问题。",
     "evidence": ["E7", "E8", "E9"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以拟言概括约伯记最直接的意思：“非常抱歉，神就是这样一个很麻烦的神，但是祂存在”，并指出此时的问题不是要不要信祂——神仍然真实且唯一，人没有选择。",
     "evidence": ["E10", "E11"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定：因为痛恨一座拦路的山而要喊着“不相信它的存在”，是愚蠢而且毫无意义的；某些遭遇只是历史被安排的段落，与你是否善良、公义无关，并且可能令你痛苦。",
     "evidence": ["E12", "E13"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以巴比伦人的信仰作对照：其中没有约伯记，所以打了败仗就可以认定是神抛弃了他们，因此巴比伦只能胜不能败，胜则存、败则亡。",
     "evidence": ["E14"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张对犹太人的上帝没这回事：因为约伯记的存在，失败对犹太民族没有额外的威力，即使失败一两千年、流浪被驱逐欺辱掠夺绞杀，也不因此而有信仰本身的危机；当失败不可能根本地伤害你时，失败就失去了一切真实的威力。",
     "evidence": ["E15", "E16"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张约伯记是分开犹太信仰与原始偶像崇拜的第一道隔离墙，上帝因此无法被降格为一种“‘善行’交易员”，即使行善也不能保证换取绝对福利。",
     "evidence": ["E17"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张行善是一种义务、没有任何对价的义务；不行有祸有诅咒，行了不过是该当、是零，不是可以凭发票找上帝报销的欠条；上帝所赐的一切没有一分是因为欠了你，只能理解为纯然、完全没有支付义务的额外赏赐。",
     "evidence": ["E18", "E19"]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者判断想和神谈生意、准备各种交易技巧的人没有一个能接受这样的“条款”；刻意无视它的人终有一天会被赶出大门，因无法忍受自认为不公的遭遇而抛弃信仰；只有能接受这一点的人能留存，而宣称“有善必赏”的圈子是假的、每一个都是骗局。",
     "evidence": ["E20", "E21"]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张每一个完全理解并接受约伯记的人，信仰动机都一次性得到完全清洗，可以毫不羞愧地说“我行善，不是为了所谓的善报”；信约伯记而行善，得到的善报因此全部变格为赏赐。",
     "evidence": ["E22", "E23"]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以两种帮助者为例：认为帮助是应该的人，你对他的帮助心就是上帝为他安排的保障；接受约伯记那“不公平”“残暴”的条款并把行善当作无报酬义务承担的人，直接得到自然法则驱动的整个人类文明的护佑，抗拒的文明则可以准备毁灭，无论它有神无神。",
     "evidence": ["E24", "E25"]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张约伯所受的苦救了直到人类毁灭之日的无可计量的兆亿生灵，因此并非毫无意义；但在那剧情里必须是“毫无意义”，唯有在那里“毫无意义”，才能成全这无量的意义。",
     "evidence": ["E26", "E27"]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者先设问旧约中约伯记是否使“善有善报、恶有恶报”与“公平在我，我必报应”落空，随后称这问题在约伯记诞生六百年后由耶稣回答：一个人除了因恶受苦，还可能因为义受苦；因为世上有甚艰难而确必要的事只能交给义人，恰恰因为你的义，这大艰难、大必要的事便必要给你，你难以推辞避让；且不要指望现世足够的回报，唯一可以相信存在的回报是上帝必然在永生里给你的回报。",
     "evidence": ["E28", "E29", "E30", "E31"]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张这个世界依靠那些“傻人”的牺牲得以维持；约伯并非毫无理由受到折磨，这折磨不是因为他有罪当罚，而是一种放置在他身上的使命；追求成为义人就是在无形中追求约伯的待遇，因此苦难降临时谈不上“不公平”，信仰也因此有了重量。",
     "evidence": ["E32", "E33", "E34", "E35"]
    }
   ],
   "argument_steps": [
    "拒绝提问设定的“上帝的动机”问题，改问文本为何能存活两千六百年（P001）。",
    "交代巴比伦之囚与旧约编辑成型的历史处境，指出亡国民族通常被同化熔解，唯一对抗力量是对“那个指望”的信心（P002-P005）。",
    "叙述《约伯记》在最痛苦的篇章中却稳居正典、从未被提议删除的例外地位（P006-P009）。",
    "提出解读之钥：不是约伯或上帝怎样，而是绝境中的犹太人为何对令一般人无法接受的东西心有所感（P010）。",
    "指出信仰最脆弱之时是自认为做得好却遭厄运之时，而约伯记使神的存在性与遭遇的公平性脱钩（P011-P013）。",
    "把该结论概括为“神很麻烦但祂存在”，并强调此时人没有选择（P014-P016）。",
    "说明偶像更甜但是假的，遭遇与善恶无关，弃绝上帝如同否认拦路的山（P017-P020）。",
    "以巴比伦只能胜不能败作反例，对照犹太民族因约伯记而免除信仰危机（P021-P025）。",
    "处理“行善与赏赐”：上帝不是善行交易员，行善是无对价义务，谈生意者不能接受（P026-P032）。",
    "指出无视此条款者终会因自认不公而抛弃信仰，只有接受者留存，宣称“有善必赏”的圈子是骗局（P033-P036）。",
    "说明接受者的信仰动机被清洗，善报变格为赏赐（P037-P038）。",
    "以两种帮助者为例，推出接受条款者得到人类文明的护佑（P039-P045）。",
    "回看约伯的苦：救了无量生灵，但在剧情里必须“毫无意义”（P046-P052）。",
    "用两个设问（善有善报是否不成立、“公平在我，我必报应”是否空话）引出耶稣的回答：因义受苦（P053-P057）。",
    "以间谍为例说明义人承担必死任务、现世无回报，唯一指望是永生里的回报（P058-P068）。",
    "以“傻人”维持世界收束，把约伯的苦定性为使命，落到“信仰因此有了重量”（P069-P074）。"
   ],
   "concept_usage": [
    {"term": "约伯记", "meaning": "文中指《圣经》中的《约伯记》篇章；作者用它指一种使神的存在性与个人遭遇的公平性脱钩、把行善规定为无对价义务的信仰条款。", "evidence": "P012", "ambiguity": "作者既谈该文本的历史与正典地位，也谈其神学含义，两个层面未严格分开"},
    {"term": "那个指望", "meaning": "文中指亡国为奴的犹太人对上帝的唯一指望，作者称它是唯一能对抗民族熔炉的东西。", "evidence": "P005", "ambiguity": "作者未给出更具体的界定"},
    {"term": "“善行”交易员", "meaning": "作者自造的贬称，指把上帝理解为按善行兑付福利的交易对方的看法。", "evidence": "P027", "ambiguity": "是比喻性说法，未对应具体教派或人物"},
    {"term": "因义受苦", "meaning": "文中指并非因罪受罚，而是因为义而被交付艰难必要的使命而受苦；这是作者所述耶稣对约伯记遗留问题的回答。", "evidence": "P057", "ambiguity": "作者未说明这一回答在经文中的具体出处"},
    {"term": "使命", "meaning": "作者对约伯受苦的定性：不是有罪当罚，而是放置在他身上的使命。", "evidence": "P072", "ambiguity": "使命的来源、内容与判定方式，本文未展开"}
   ],
   "examples_and_targets": [
    "《约伯记》《旧约》《启示录》《雅各书》、君士坦丁会议：作者引用的经文与教会史材料，属历史/文本叙述（P002、P006）。",
    "巴比伦人与巴比伦之囚：作者用作对照性历史例证（P003、P021）。",
    "犹太民族两千六百年的流浪、被驱逐、被欺辱、被掠夺、被绞杀：作者举的历史经验（P024）。",
    "两种帮助者（认为帮助是应该的人 / 认为你欠了他的人）与“二百两银子”：作者的类比例证（P039-P042）。",
    "“杀人放火金腰带，修桥补路无尸骸”：作者引用的俗语，用来说明父母教导子女的现实考虑（P069）。",
    "“公平在我，我必报应”：作者设问时引用的经文语句（P055）。",
    "深入敌后的间谍与抽牌（抽中大王给一百万、抽不中枪毙）：作者的类比例证，说明义人承担必死任务、不能当生意做（P060-P067）。",
    "耶稣：作者称其在约伯记诞生六百年后对相关问题作出回答（P056-P057）。"
   ],
   "conditions": [
    "前提条件：作者的解读以“认定约伯记是真实的”为条件（P012）。",
    "让步条件：即使遭受厄运、即使自以为义人，逻辑上也不可再以此怀疑神的存在性（P012）；即使失败一千年、两千年，也不因此有信仰本身的危机（P024）。",
    "历史条件：论述被限定在巴比伦之囚及五经时代第一批文献的背景下（P005）。",
    "范围限定：作者称“以我所见所闻”尚未听过任何教派提议删除约伯记（P007）。",
    "未说明：间谍、抽牌均为类比，文中未讨论现实中是否存在等价的“安排”，也未说明“自然法则驱动的整个人类文明的护佑”如何被验证。"
   ],
   "rhetoric_and_tone": "布道式论说与训诫并重：大量反问（“人世间岂得常胜不败者？”“那你去还是不去？”）、设问引出转折、以“你”直呼读者；用“非常抱歉，神就是这样一个很麻烦的神”这类拟言戏剧化经义，用抽牌与间谍任务等直白比喻讲代价，结尾以“信仰就因此有了重量”作警句。全篇语气笃定，对提问的“打赌玩弄”框架不作回应。",
   "unresolved_questions": [
    "作者关于《约伯记》成书年代、正典形成过程、巴比伦之囚期间旧约编辑的叙述属作者转述，需外部核查（P002、P006-P007）。",
    "提问者问“上帝和魔鬼打赌玩弄约伯的原因”，作者明确不回答，只给出自己的解读框架，本文未说明该问题本身是否成立。",
    "作者引用的经文语句（如“公平在我，我必报应”）未注明具体出处，需外部核查（P055）。",
    "“自然法则驱动的整个人类文明的护佑”“哪个文明敢抗拒，哪个文明就可以准备毁灭”为强断言，文中未给经验依据（P044）。",
    "文中“那些圈子是假的。每一个都是骗局”指向宣称“有善必赏”的宗教圈子，具体所指主体不明（P034-P035）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "故事里上帝的动机并不重要，重要的是这一篇东西为什么会存活下来，被传承两千六百年。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P010", "quote": "而是为什么身处这样的绝境之中的犹太人，却对这样一种令一般人无法接受的东西心有所感。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "很大一部分是在公元前587～538年期间——也就是巴比伦之囚期间——由犹太民族的长老精英们编辑成型的。", "relation": "context"},
    {"key": "E4", "paragraph_id": "P005", "quote": "唯一能对抗这熔炉的东西，就是“那个指望”和对那唯一指望的信心。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "尚未听过任何一个教派，哪怕是异端教派，提出过“我觉得约伯记是伪经，我们应该删掉它”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "两千六百年来，没有一个信徒不为它痛苦纠结、怀疑信仰，而它却没有被删掉。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "则神的存在性与你的遭遇的“公平性”就脱离关联了", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "约伯记彻底地消除了一神信仰的脆弱性。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "但这问题已经是第二问题，而不是第一问题了。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P014", "quote": "神就是这样一个很麻烦的神，但是祂存在。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "你是没有选择的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "这就好像因为痛恨屋门口的一座山拦路，要喊着“不相信它的存在”一样愚蠢而且毫无意义。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "仅仅只是历史的一个被安排的段落，与你是否善良、是否公义无关。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "也正因为如此，巴比伦只能胜，不能败。胜则存，败则亡。", "relation": "context"},
    {"key": "E15", "paragraph_id": "P024", "quote": "犹太人都不因此而有信仰本身的危机。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "当失败不可能根本的伤害你时，失败就失去了一切真实的威力。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "上帝因此而无法被降格为一种“‘善行’交易员”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P030", "quote": "你行善，是一种义务，没有任何对价的义务。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "上帝所赐给你的一切，没有任何一分是因为欠了你的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P033", "quote": "终有一天会被赶出大门", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P035", "quote": "那些圈子是假的。每一个都是骗局。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "我行善，不是为了所谓的善报。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P038", "quote": "信约伯记而行善，得到的善报因此而全部变格为赏赐。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P043", "quote": "前者是接受约伯记的人，你对他所生的帮助心，就是上帝为他安排的保障。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P044", "quote": "你就直接得到自然法则驱动的整个人类文明的护佑。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P046", "quote": "约伯所受的苦，救了直到人类毁灭之日", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P049", "quote": "唯有在那里“毫无意义”，才能成全这无量的意义。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P055", "quote": "那么“公平在我，我必报应”岂不是一句空话？", "relation": "context"},
    {"key": "E29", "paragraph_id": "P057", "quote": "一个人，除了因为恶而受苦，还可能因为义受苦。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P058", "quote": "恰恰因为你的义，你难以推辞避让。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P068", "quote": "你唯一可以相信存在的回报，就是上帝必然在永生里给你的回报。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P071", "quote": "这个世界，是依靠着那些“傻人”的牺牲得以维持的。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P072", "quote": "约伯并非毫无理由受到折磨，只是这折磨并非因为他有罪当罚，而是一种放置在他身上的使命。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P073", "quote": "你就是在无形中追求约伯的待遇", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P074", "quote": "信仰就因此有了重量。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教/圣经研究（作者解读）", "神义论", "犹太民族史", "信仰伦理"],
   "issue_candidates": ["约伯记为何被传承", "神的存在性与遭遇公平性的关系", "一神信仰的脆弱性", "行善与赏赐（善行交易员）", "因义受苦与使命", "苦难的意义"],
   "text_function_candidates": ["答问", "解经式论说", "护教/训诫", "历史叙述"],
   "object_candidates": ["约伯", "上帝", "犹太人", "巴比伦人", "耶稣", "《约伯记》", "《圣经》旧约", "教派与异端教派"],
   "working_keywords": ["巴比伦之囚", "正典资格", "神迹般的谜", "善行交易员", "对价的义务", "因义受苦", "使命", "信仰的重量"]
  },
  "notes": "无图片、正文非空。提问中“上帝和魔鬼打赌玩弄约伯”的框架属提问者，作者明确不予回答（P001），已在 question_context 分开登记。文中关于《约伯记》成书年代、正典形成、巴比伦之囚期间旧约编辑等叙述为作者的转述与判断，属 author_reported，需外部核查；“公平在我，我必报应”为作者引用的经文语句，属引用材料而非作者原创主张。"
 },
 "d6aebcf1": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么华夏有五千年文明，却没有发展出体系化的现代科学？作者的答复不直接罗列原因，而是从“古代王朝眼中技术进步是什么”入手：朝廷以能否帮助中央压倒地方来筛选技术，而科学又随机、不可禁止、赢家通吃，因此在以维持统治为第一利益的政体下不可能被系统发展；最后指出系统发展科学需要一种近乎狂妄的乐观，而这需要类似宗教式的信念前提。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009"],
     "summary": "提出王朝的技术筛选标准：理想的技术进步须先在中央领地被发现，且广泛流传后仍天然在中央领地得到压倒性更好应用；简言之无法帮中央压倒地方即为坏技术，连对双方同等有利也算坏事，能过此过滤器的技术极少。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"],
     "summary": "说明中央相对地方在资源、交通、外贸、人力等方面天生劣势，唯一优势是政务人才密集且常反成劣势；即使技术先被中央发现，也常在某诸侯处有更好应用环境，封锁机密代价大且难持久，结果新技术大概率导致力量失衡。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"],
     "summary": "给出决策逻辑：无生死存亡理由时不变为上；即使变亦死不变亦死、乃至九死一生，大多仍选不变碰运气；只有变则尚有生机、不变必死时才有人敢闹一回，这就是帝国的逻辑和宿命。",
     "role": "conclusion"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P020", "P021", "P022", "P023"],
     "summary": "转而论科学：科学随机启动、靠思想传播无法禁止、谁先适应谁赢家通吃，朝廷自知是最输不起的一个；以人为主宰的政体必以维持统治为第一利益，失去外部敌人与威胁后就会对科学失去兴趣甚至警惕扑杀。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P024", "P025", "P026", "P027"],
     "summary": "结论落在信念前提：除非相信世界由全知全能者创造、主宰未来并绝对照顾自己，除非相信君权天授不可被夺，否则无法拥有作为上位者发展科学所需的近乎狂妄的乐观；无论勇气来自多奇怪的逻辑，先有勇气才谈得上系统发展科学。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张在古代王朝眼里“技术进步”几乎全是坏东西。",
     "evidence": ["E1", "E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出王朝认可的理想技术进步须满足两个条件：必须首先在中央领地被发现而不是诸侯领地；必须在难以避免的广泛流传之后仍天然在中央领地得到压倒性的更好应用。简单说，无法帮助中央压倒地方的技术就是坏技术。",
     "evidence": ["E3", "E4", "E5"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出哪怕一项技术对中央和地方一样有利，对中央集团也是坏事——因为相对力量对比会从2:1变成3:2，中央反而更危险。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定只有能闯过这一过滤器的技术才会被容许存在，并以“那么你算算看，有几样？”暗示数量极少。",
     "evidence": ["E8", "E9"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为中央相对地方在资源、交通、对外接触、对外贸易、人力资源等方面都有天生劣势，唯一的优势是政务人才比较密集，而这在很多时候反而是一种劣势。",
     "evidence": ["E10"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者指出即使某项技术先被中央集团发现，也往往会在某处诸侯那里找到更好的应用环境；要确保技术不会比较有利于地方，需要严防死守、投入大量精力和金钱封锁机密，即便如此也很难长久保持。",
     "evidence": ["E11"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者判断一项新技术大概率最终会导致力量失衡，给地方以挑战中央的实力和由这实力刺激出来的野心；并以“十室九空、尸横枕藉”反问那点粮食增产是否值得。",
     "evidence": ["E12", "E13"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者总结朝廷的决策逻辑：没有生死存亡的理由时还是不变为上；即使到了变亦死、不变亦死的时候，大半还是会选不变而死；甚至变则九死一生、不变亦九死一生时仍选不变去碰运气；只有变则尚有生机、不变则必死无疑时，才会有新党敢提着脑袋闹一回。这就是帝国的逻辑和宿命。",
     "evidence": ["E14", "E15", "E16", "E17"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出对于永远不知道下一把开什么宝、依靠思想传播无法禁止、谁先适应谁就稳吃迟到者乃至赢家通吃的科学，朝廷心知肚明自己是这一窝狼崽子里包袱最重、体力最差、输面最大的一个。",
     "evidence": ["E18", "E19"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张任何以人为主宰的政体都无法不把维持自己的统治看作第一利益，因此一旦失去外部的敌人和威胁，就会立刻完全失去对科学的兴趣，甚至要专为警惕和扑杀；凭着人自己，人无法自信到绝对相信任何即将到来的未知都必然最终有利于自己。",
     "evidence": ["E20", "E21"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者主张除非你相信世界是被一个全知全能的事物创造、祂主宰一切未来并且绝对照顾我，除非你相信君权出自天授、绝不可能被夺走，否则无法拥有作为上位者发展科学所需要的那种近乎狂妄的乐观；不管勇气来自多么奇怪的逻辑，也要先有这个勇气才谈得上系统的发展科学。",
     "evidence": ["E22", "E23", "E24"]
    }
   ],
   "argument_steps": [
    "先提出古代王朝看待技术进步的基本态度：几乎全是坏东西（P001-P002）。",
    "给出王朝的技术筛选标准（发现地与应用优势两条），并简化为“能否帮中央压倒地方”（P003-P006）。",
    "用2:1与3:2的算例说明即使同等有利也威胁中央（P007）。",
    "指出能过此过滤器的技术极少（P008-P009）。",
    "解释中央相对地方的结构性劣势与封锁机密的困难（P010-P011）。",
    "推出新技术大概率造成力量失衡，并以战乱代价反问收益（P012-P013）。",
    "归纳朝廷“不变为上”的决策梯度，直至“变则尚有生机”才可能变法（P014-P019）。",
    "转向科学：科学不可控、赢家通吃，朝廷自知输面最大（P020-P022）。",
    "提升为一般命题：以人为主宰的政体以维持统治为第一利益，失去外部威胁后必压制科学（P023）。",
    "给出信念前提：唯有宗教式的全知全能信仰或君权天授信念才能提供发展科学所需的近乎狂妄的乐观（P024-P027）。"
   ],
   "concept_usage": [
    {"term": "技术进步", "meaning": "本文特指王朝视角下的技术，其价值由是否有利于中央压倒地方来判定。", "evidence": "P006", "ambiguity": "作者未区分技术与科学，P020 起才把可控技术同科学分开"},
    {"term": "中央/地方（诸侯）", "meaning": "文中指王朝中央集团与诸侯领地，二者存在资源与力量的结构性竞争关系。", "evidence": "P010", "ambiguity": "未指定具体朝代，属一般化论述"},
    {"term": "科学", "meaning": "文中指随机启动、依靠思想传播因而无法禁止、谁先适应谁就赢家通吃的事业，与可控制的技术相区别。", "evidence": "P021", "ambiguity": "作者未给出科学的严格定义"},
    {"term": "近乎狂妄的乐观", "meaning": "作者指上位者发展科学所需的、相信未知必有利于自己的勇气，其来源只能是宗教式信念。", "evidence": "P026", "ambiguity": "作者未说明该信念是否必要且充分"}
   ],
   "examples_and_targets": [
    "“以前我们是2:1，现在我们是3:2。我变得更危险了。”：作者虚构的算例，用说明同等有利也威胁中央（P007）。",
    "诸侯的良港、有弹性的木料、有耐力的马、大铁矿：作者举的地方应用优势条件（P011）。",
    "群雄逐鹿、十室九空、尸横枕藉：作者描述技术扩散可能引发的战乱代价（P013）。",
    "新党提着脑袋闹一回：作者对变法条件的描述（P018）。",
    "“一个死胖子，去赞助这种随机启动、跑输了杀全家的百米跑大奖赛”：作者的比喻，形容朝廷在科学竞赛中的处境（P022）。",
    "“世界是被一个全知全能的事物创造、祂主宰一切未来、并且祂绝对照顾我”：作者设定的信念前提（P024）。",
    "君权出自天授、绝不可能有人在你自己不背叛神的前提下夺走：作者设定的第二种信念前提（P025）。"
   ],
   "conditions": [
    "筛选条件：技术须先在中央领地发现，且在广泛流传后中央仍能得到压倒性更好应用（P004-P005）。",
    "让步条件：即使技术与地方同等有利、即使中央先发现，也仍可能不利于中央（P007、P011）。",
    "决策条件：只有在“变则尚有生机，不变则必死无疑”时，才可能出现变法（P018）。",
    "前提条件：一旦失去外部的敌人和威胁，政体就会失去对科学的兴趣（P023）。",
    "信念条件：除非相信全知全能者的绝对照顾，或相信君权天授不可被夺，否则没有发展科学所需的乐观（P024-P026）。",
    "未说明：作者未讨论中国以外的王朝/政体是否同样如此，也未给出历史实例或数据。"
   ],
   "rhetoric_and_tone": "以“朝廷诸公算账”的口吻作翻案式解释，多用反问（“值得用十室九空、尸横枕藉的惨剧来换吗？”“是想找死吗？”）与戏谑比喻（死胖子跑百米大奖赛、狼崽子），语气笃定、带讥诮；结尾转为带宗教色彩的严肃断言。",
   "unresolved_questions": [
    "作者未举出任何具体朝代、技术或史料作为例证，全文为一般化推演，需外部核查（P010、P011）。",
    "“中央—地方”二分是否能涵盖提问所指的五千年文明跨度，本文未说明。",
    "作者称政体失去外部威胁后“就会立刻完全失去对科学的兴趣”为强断言，未给依据（P023）。",
    "结尾关于唯一神信仰与科学发展的关系未展开论证，也未回应其他可能的解释（P024-P027）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人大概意识不到在古代王朝眼里“技术进步”到底是一种什么样的存在。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "答案是“几乎全是坏东西”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "第一，它必须首先在中央领地被发现，而不是在诸侯领地；", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "也天然的在中央领地里能得到压倒性的更好的应用", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "如果一项技术无法帮助中央压倒地方，那么它就是坏技术。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "哪怕它是对中央和地方都一样有利，也对中央集团是坏事。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "以前我们是2:1，现在我们是3:2。我变得更危险了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "能闯得过这个过滤器的技术，才会被容许存在。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "那么你算算看，有几样？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "唯一的优势就是政务人才比较密集——在很多时候这反而是一种劣势。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P011", "quote": "要确保某项技术不会比较有利于地方，需要严防死守，投入大量的精力和金钱来封锁机密，即使如此，也很难长久保持。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "结果，一项新技术大概率最终会导致力量的失衡，给地方以挑战中央的实力和由这实力刺激出来的野心。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "值得用十室九空、尸横枕藉的惨剧来换吗？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "没有生死存亡的理由，不是变亦死、不变亦死的时候，还是不变为上。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "甚至就是到了变亦死，不变亦死的时候，大半还是会选不变而死。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "只有变则尚有生机，不变则必死无疑的时候，才会有新党敢提着脑袋闹一回。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "这就是帝国的逻辑和宿命。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "依靠思想传播于是完全无法禁止、谁先适应谁就稳吃迟到者，乃至赢家通吃的科学", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "自己是这一窝狼崽子里包袱最重、体力最差、输面最大的一个", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "任何以人为主宰的政体，都无法不把维持自己的统治看作第一利益", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "一旦失去外部的敌人和威胁，就会立刻完全失去对科学的兴趣，甚至要专为警惕和扑杀。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "除非你真的相信“世界是被一个全知全能的事物创造、祂主宰一切未来、并且祂绝对照顾我。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P026", "quote": "除非你相信这个疯狂的假设，否则你无法拥有作为上位者发展科学所需要的那种近乎狂妄的乐观。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "你也要先有这个勇气才谈得上系统的发展科学。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中国科技史（作者解释）", "政治经济学式分析", "王朝政治", "科学与信仰"],
   "issue_candidates": ["为何未发展出体系化现代科学", "王朝的技术筛选机制", "中央与地方的力量竞争", "变法条件", "科学不可控与赢家通吃", "发展科学所需的信念前提"],
   "text_function_candidates": ["答问", "解释", "翻案式评论", "推演"],
   "object_candidates": ["古代王朝/朝廷", "中央领地", "诸侯领地", "新党", "科学", "技术进步"],
   "working_keywords": ["过滤器", "中央压倒地方", "力量失衡", "不变为上", "帝国的逻辑和宿命", "赢家通吃", "近乎狂妄的乐观"]
  },
  "notes": "无图片、正文非空。提问中“华夏有五千年文明却没有发展出体系化的现代科学”这一前提属提问者，作者未讨论该前提的表述，只给出自己的机制性解释。全文为一般化推演，未举具体朝代或史料实例，已在 unresolved_questions 登记。"
 },
 "3aeb41af": {
  "analysis": {
   "question_context": "提问者（Q001）问：有哪些以为是小罪，其实是重罪，判刑很重的案例？这是要求真实案例的提问。作者没有给出任何现实案例或法律分析，而是以戏仿刑事判决的方式列出两种社交行为及其“处罚”，并补出审判程序，属玩笑式回答。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002"],
     "summary": "以判决句式列出两项“小罪”与对应处罚：浪费别人的时间处社交死缓；公共场合行为不检处全民流放。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P003", "P004"],
     "summary": "补出程序性条款：无陪审团、无辩护律师、不接受上诉；一经判决立即执行、不得保释。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以戏仿判决的方式提出两项“小罪”及其处罚：浪费别人的时间，处社交死缓；公共场合行为不检，处全民流放。",
     "evidence": ["E1", "E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者为上述“判决”补出程序：无陪审团，无辩护律师，不接受上诉；一经判决，立即执行，不得保释。",
     "evidence": ["E3", "E4"]
    }
   ],
   "argument_steps": [
    "不回答提问所问的真实案例，改用戏仿的罪刑清单作答（P001-P002）。",
    "以四条程序性短句强化“社交性重罪”无程序保障的夸张效果（P003-P004）。"
   ],
   "concept_usage": [
    {"term": "社交死缓", "meaning": "作者自造的处罚名目，指在社交层面被判处死刑缓期执行式的排斥。", "evidence": "P001", "ambiguity": "非法律术语，作者未解释其具体含义与执行方式"},
    {"term": "全民流放", "meaning": "作者自造的处罚名目，指被公众集体排斥/放逐。", "evidence": "P002", "ambiguity": "同上，未说明由谁判定、如何执行"}
   ],
   "examples_and_targets": [
    "浪费别人的时间：作者列为“小罪”的第一项（P001）。",
    "公共场合行为不检：作者列为“小罪”的第二项（P002）。",
    "本文无真实案例、人物、机构、时间或数据。"
   ],
   "conditions": [
    "未说明：本文未说明这两项行为的判定标准、适用对象与执行主体。",
    "未说明：无陪审团、无辩护律师、不接受上诉等程序条款是戏仿设定，作者未说明其对应何种现实场景。"
   ],
   "rhetoric_and_tone": "冷面戏仿：用“处……”“一经判决，立即执行，不得保释”等拟法律条文句式，把社交失礼写成重罪，制造反差幽默；全篇四句、每句一段，语气克制不下判断。",
   "unresolved_questions": [
    "提问要求“案例”，本文未提供任何真实案例或法律信息。",
    "“社交死缓”“全民流放”为作者自造的比喻性处罚，判定主体与标准不明。",
    "作者是否针对特定事件或人群而写，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "浪费别人的时间，处社交死缓。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "公共场合行为不检，处全民流放。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "无陪审团，无辩护律师，不接受上诉。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "一经判决，立即执行，不得保释。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社交规范（戏仿）", "法律话题（玩笑式回应）"],
   "issue_candidates": ["小罪与重罪的错位", "社交失礼的后果", "审判程序的缺失（戏仿）"],
   "text_function_candidates": ["答问", "讽刺/玩笑", "拟条文戏仿"],
   "object_candidates": ["浪费别人时间的人", "公共场合行为不检者", "陪审团", "辩护律师", "上诉", "保释"],
   "working_keywords": ["社交死缓", "全民流放", "不接受上诉", "不得保释"]
  },
  "notes": "无图片、正文非空；全文 64 字，四句。本篇为戏仿式玩笑回答，不含真实案例、法律意见或可核验事实；提问所问“案例”未被回答，已在 unresolved_questions 登记。短引与归纳均按戏仿性质保留，不把“社交死缓”“全民流放”写成作者主张的现实刑罚。"
 },
 "27a051de": {
  "analysis": {
   "question_context": "提问者（Q001）问：我用传统弓射箭，箭射到靶子上为什么是歪的？作者没有逐一解释箭为何歪，而是给出一条练习次序上的建议：先分清“东倒西歪”与“全朝一边歪”，在动作不一致造成的散乱被消除之前不要急着调弓调箭。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002"],
     "summary": "前提与要害：传统弓不太好多说；如果箭是东倒西歪而不是朝同一方向歪，最好先不要调来调去。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P003"],
     "summary": "给出次序：先打成全朝一边歪再调弓调箭；否则调完后用自己的动作去打看不到变化，仍东倒西歪，只是多了一层觉察不出的全体偏转——调整其实已造成变化，但被动作不一致造成的散乱掩盖。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P004"],
     "summary": "给出例外：除非现在的动作会导致箭打弓窗、发出响亮的啪的一声响并使尾羽很快坏掉，否则还是先接着打。",
     "role": "qualification"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P005"],
     "summary": "预期结果：打过一两万箭，很可能这个现象自动消失，弓也没问题、箭也没问题。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称传统弓不太好多说，但有一条要害：如果箭是东倒西歪而不是朝着同一个方向歪，那么最好还是不要先调来调去。",
     "evidence": ["E1", "E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张先打成全朝一边歪再调弓调箭；否则调完后用自己的动作去打看不到任何变化，仍会东倒西歪，只是这些东倒西歪会有你觉察不出的全体偏转——调整已经造成了变化，但被动作不一致造成的散乱掩盖了。",
     "evidence": ["E3", "E4"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者给出例外条件：除非现在的动作会导致箭打弓窗、发出响亮的啪的一声响并导致尾羽很快坏掉，否则还是先接着打。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预期：打过一两万箭，很可能这个现象自动消失了，弓也没问题，箭也没问题。",
     "evidence": ["E6"]
    }
   ],
   "argument_steps": [
    "先承认传统弓难以一概而论，再给出唯一“要害”（P001）。",
    "区分两种散布：东倒西歪与全朝一边歪，并建议前者先不要调整（P002）。",
    "给出调整次序：先打成全朝一边歪，再调弓调箭（P003）。",
    "解释原因：动作不一致的散乱会掩盖调整带来的全体偏转（P003）。",
    "给出例外：只有打弓窗、出声响、坏尾羽时才需先处理（P004）。",
    "给出预期：练到一两万箭后现象可能自行消失（P005）。"
   ],
   "concept_usage": [
    {"term": "东倒西歪", "meaning": "文中指箭着靶方向散乱、不朝同一方向歪，作者把它归因于射手动作不一致。", "evidence": "P002", "ambiguity": "作者未说明如何量化判定“东倒西歪”"},
    {"term": "全体偏转", "meaning": "文中指调整弓或箭后所有箭一致发生的偏转，因动作散乱而不易被射手察觉。", "evidence": "P003", "ambiguity": "属经验描述，未给出观察方法"},
    {"term": "打弓窗", "meaning": "文中指箭在发射时撞击弓窗，伴随响亮的啪的一声并加速尾羽损坏，是作者设定的例外情形。", "evidence": "P004", "ambiguity": "作者未说明其成因与处置办法"}
   ],
   "examples_and_targets": [
    "箭打弓窗、响亮的啪的一声响、尾羽很快坏掉：作者举的例外情形（P004）。",
    "“打过一两万箭”：作者给出的练习量经验值（P005）。",
    "本文无人物、机构、数据或文献引用。"
   ],
   "conditions": [
    "条件句：如果你的箭是东倒西歪而不是朝同一个方向歪，最好先不要调来调去（P002）。",
    "次序条件：先打成全朝一边歪，再调弓调箭（P003）。",
    "例外条件：除非动作会导致箭打弓窗、出声响并很快坏尾羽，否则先接着打（P004）。",
    "程度限定：“很可能这个现象自动消失了”为作者的估计，未给概率或依据（P005）。"
   ],
   "rhetoric_and_tone": "简短经验谈，先给结论再给理由与例外；用“不太好多说”“有一条要害”等口语化限定语气，不下绝对判断。",
   "unresolved_questions": [
    "作者未解释“箭射到靶子上是歪的”本身的成因（箭、弓、动作各占多少），只给出练习次序建议。",
    "“打过一两万箭”为经验估计，未说明依据与适用条件（P005）。",
    "何时才应开始调弓调箭、如何调，本文未说明，只给出“先打成全朝一边歪”的判据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "传统弓不太好多说。不过有一条要害是这样的：", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "如果你的箭是东倒西歪而不是朝着同一个方向歪，那么最好还是不要先调来调去。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "先打成全朝一边歪再调弓调箭。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "其实你的调整已经造成了变化，但被你的动作不一致造成的散乱掩盖了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "除非你现在的动作会导致箭打弓窗，发出响亮的啪的一声响，并且导致尾羽很快坏掉，否则你还是先接着打吧。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P005", "quote": "打过一两万箭，很可能这个现象自动消失了，弓也没问题，箭也没问题。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["射箭技术（传统弓）", "训练经验"],
   "issue_candidates": ["箭着靶歪斜", "散布与系统偏差的区分", "调弓调箭的时机", "打弓窗与尾羽损坏"],
   "text_function_candidates": ["答问", "经验建议", "技术指点"],
   "object_candidates": ["传统弓", "箭", "靶", "弓窗", "尾羽"],
   "working_keywords": ["东倒西歪", "全朝一边歪", "全体偏转", "打弓窗", "一两万箭"]
  },
  "notes": "无图片、正文非空；全文 243 字。P004 与上一段之间存在一个未被 lexical 覆盖的空行/间隙，不影响正文可读性（生成的段落 P004 char_start=160 与 P003 char_end=159 相接）。作者只给练习次序建议，未解释提问所问“箭为何歪”的成因，已在 unresolved_questions 登记。"
 },
 "95ae40bd": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么武松在张青处得了行者服装后就一直当自己是行者了？作者不讨论武松的心理，而是就这身装备逐件“去魅”：按字面含义，张青给的只是标准的在外云游僧人装备，谈不上“杀气”“死气”。文中配有 5 张图片（戒刀、牦牛顶骨念珠、永乐宫壁画直裰等），本记录未核验图片内容。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002"],
     "summary": "总说：张青给的那身装备若按字面含义，没有任何“杀气”“死气”可言，只是标准的在外云游的僧人装备。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009"],
     "summary": "先说戒刀：引佛学辞典说明其为比丘所持小刀、供割切三衣之用、属道具；文中以图片示意（未核验），并称其刃长按佛教法度最长不超过六指、约十来厘米，与西餐圆头餐刀相近。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"],
     "summary": "再说人顶骨念珠：不是一百零八个骷髅头；文中所示牦牛顶骨制品与人顶骨在外观上没有本质区别，并反问读者是否觉得快被吓死。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P015", "P016", "P017"],
     "summary": "最后说直裰：以永乐宫壁画的僧道衣着为据，左边光头僧人们穿的就是直裰，并反问这算“神装”吗。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P018", "P019"],
     "summary": "收束：一个人腰插两把圆头餐刀、脖挂白念珠，何来“一身杀气”；并训诫式地劝对方多读点书、少玩点游戏。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者主张：张青给的那一身装备，如果就是字面含义的话，其实没有任何“杀气”“死气”可言，只是标准的在外云游的僧人装备。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "quoted_or_cited",
     "attribution": "cited_source",
     "modality": "asserted",
     "statement": "作者引用佛学辞典条目说明戒刀是比丘所持之小刀，供割切三衣之用，并称戒刀皆是道具、佛不许斫截一切草木坏鬼神村。",
     "evidence": ["E2", "E3", "E4"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称戒刀刃长按佛教法度最长不超过六指——也就是十来厘米而已，说白了大概跟平时吃西餐用的圆头餐刀差不多。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者指出所谓人顶骨念珠不是一百零八个骷髅头。",
     "evidence": ["E6"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称文中所示牦牛顶骨制品和人顶骨在外观上没有什么本质区别（该判断以文中图片为据，图片内容本记录未核验）。",
     "evidence": ["E7"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以永乐宫壁画为据，称壁画左边光头僧人们穿的就是直裰。",
     "evidence": ["E8"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问：一个人穿这么一身、腰上插两把圆头餐刀、脖子上挂一串白念珠，何来“一身杀气”；并批评这种想象者应多读点书、少玩点游戏。",
     "evidence": ["E9", "E10"]
    }
   ],
   "argument_steps": [
    "先立总判断：这身装备按字面含义并无杀气死气，是标准云游僧装备（P002）。",
    "逐件去魅之一——戒刀：引辞典定义其为割衣小刀、属道具，再以图示并给出六指的长度与餐刀类比（P003-P008）。",
    "逐件去魅之二——人顶骨念珠：否定“一百零八个骷髅头”的想象，并称牦牛顶骨制品与人顶骨外观无本质区别（P011-P013）。",
    "逐件去魅之三——直裰：以永乐宫壁画中僧人衣着为例（P015-P016）。",
    "以“一身杀气”的反问和“多读点书，少玩点游戏”的训诫收尾（P018-P019）。"
   ],
   "concept_usage": [
    {"term": "戒刀", "meaning": "文中据辞典指比丘所持之小刀，供割切三衣之用，属“道具”，并非兵器。", "evidence": "P005", "ambiguity": "所引辞典版本与条目来源本文未注明"},
    {"term": "行者服装", "meaning": "提问所指张青给武松的一身装备；作者把它还原为标准的在外云游的僧人装备。", "evidence": "P002", "ambiguity": "作者未逐项列出该装备的完整清单"},
    {"term": "直裰", "meaning": "文中指僧道所着的一种衣服，作者以永乐宫壁画为据说明。", "evidence": "P016", "ambiguity": "未给出形制细节，依赖图片（未核验）"},
    {"term": "人顶骨念珠", "meaning": "文中否定了“一百零八个骷髅头”的通俗想象，并称牦牛顶骨制品与人顶骨外观无本质区别。", "evidence": "P012", "ambiguity": "作者未说明人顶骨念珠的实际形制与来源"}
   ],
   "examples_and_targets": [
    "佛学辞典条目（《僧史略》《释氏要览》等）：作者引用的文献材料，属 cited_source（P005）。",
    "“比丘十八物之戒刀_念念观自在_新浪博客”：作者标注的图片来源（P007）。",
    "西餐用的圆头餐刀：作者的类比物（P008）。",
    "牦牛顶骨制品：作者举的对照物，用以说明外观无本质区别（P013）。",
    "永乐宫壁画的僧道衣着：作者以图为据的例子（P016）。",
    "“多读点书，少玩点游戏”：作者对想象“一身杀气”者的训诫（P019）。"
   ],
   "conditions": [
    "前提条件：“如果就是字面含义的话”限定了作者的总判断（P002）。",
    "依据条件：戒刀刃长不超过六指“按照佛教法度”，属作者对教规的转述（P008）。",
    "图片条件：P006“大概长这样”、P016“下图是……”等结论依赖文中 5 张图片，图片内容本记录未核验。",
    "未说明：作者未说明武松为何自认行者（提问所问），也未讨论《水浒传》文本细节。"
   ],
   "rhetoric_and_tone": "考据式“去魅”加调侃：先引辞典与图片来源，再用长度、外观比较把“神装”还原为日常物；连续反问（“你有觉得快被吓死吗？”“‘神装’吗？”“‘一身杀气’？”）与结尾训诫式短句（“多读点书，少玩点游戏。”）构成讽刺语气。",
   "unresolved_questions": [
    "本篇含 5 个图片节点（IMG001-IMG005），图片内容未经核验，需人工/多模态复核；正文中“大概长这样”“下图是永乐宫壁画的僧道衣着”等判断依赖这些图片。",
    "P010“佛教常识 戒刀”是 lexical 未覆盖的正文片段，性质可能是图片说明或来源标注，主体不明。",
    "所引佛学辞典条目、图片来源及“佛教法度最长不超过六指”的说法未注明版本，需外部核查。",
    "提问所问“武松为何一直当自己是行者”，本文未直接回答。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "其实没有任何“杀气”“死气”可言。标准的在外云游的僧人装备罢了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "（物名）比丘所持之小刀。供割切三衣之用。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "戒刀皆是道具", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "盖佛不许斫截一切草木坏鬼神村故", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "这个东西刃长按照佛教法度最长不超过六指——也就是十来厘米而已。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "这玩意不是一百零八个骷髅头。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "下面这个是牦牛顶骨制品，和人顶骨在外观上没什么本质区别：", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "下图是永乐宫壁画的僧道衣着。左边光头僧人们穿的就是直裰：", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "腰上插两把圆头餐刀，脖子上挂一串白念珠——“一身杀气”？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P019", "quote": "多读点书，少玩点游戏。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["佛教器物常识", "《水浒传》细节考（去魅式）", "名物考证"],
   "issue_candidates": ["戒刀是什么", "人顶骨念珠的形制", "直裰与僧衣", "行者装备是否有杀气"],
   "text_function_candidates": ["答问", "名物解释", "调侃式考据", "训诫"],
   "object_candidates": ["武松", "张青", "戒刀", "人顶骨念珠", "牦牛顶骨制品", "直裰", "永乐宫壁画", "西餐圆头餐刀"],
   "working_keywords": ["行者服装", "道具", "六指", "骷髅头", "直裰", "一身杀气"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 5 个图片节点（IMG001..IMG005），图片内容未经核验，需图像核验；已读部分为正文文本。文中 P006“大概长这样”、P016“下图是……”等判断依赖图片，图片未核验前不能视为已核对。P010“佛教常识 戒刀”为 lexical 未覆盖的正文片段（可能为图片说明或来源标注），主体不明，已登记。"
 },
 "5a3ad0a5": {
  "analysis": {
   "question_context": "提问者（Q001）问：长城这么矮究竟能拦住什么？提问以“长城矮”为前提。作者先修正算法：长城的高度要从山脚下算、厚度要从墙背算到敌人能有效集结兵力的出发阵地前沿，因此有效高度与厚度都在百米以上；随后把长城重新定义为古代技术条件下的高架快速路、信息传递系统与“空间武器”，并反驳“封锁经济”说。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "修正“高/厚”的算法：高度从山脚下算起，故实际有效高度基本在百米以上；厚度从墙背算到敌人能有效集结兵力的出发阵地前沿，故有效厚度也在百米以上。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"],
     "summary": "由此说明军事价值：在山顶修路、每隔一段修小宿舍，即等于拥有高百米宽百米的巨大城墙，砖由老天爷铺好；有强烈防御需求的帝王觉得没有比这更便宜的，喊“秦王暴政”者非装糊涂即真蠢。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"],
     "summary": "重新定义长城的“墙”：它更像高铁自带的高架，目的是造成裕度以抹平山峰高差、便于通行；严格说是古代技术条件下修建的高架快速路，城楼本质是高速公路服务区；被视为墙的部分是当时最经济持久的路面支撑技术，“高度”不是它的追求。",
     "role": "definition"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P014", "P015"],
     "summary": "提出这条高速路本质是一件“空间武器”：沿着它时间会变慢几十倍，两旁穿越者的移动速度只有路上旅行者的几十分之一；战略上约等于绿巨人对抗闪电侠。",
     "role": "claim"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P016"],
     "summary": "反驳“长城为封锁经济”之说：控制经济只需关卡不需城；西欧不靠长城，德意志小诸侯仅靠丘陵间道路设卡就能重剥商旅。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P017", "P018"],
     "summary": "提出第二个用意是替代萨德：长城取地区制高点，烽火一日千里，在电报发明前是人类传递信息最快的手段；烽火台之间有deadman switch，失联超时同样触发报警；要害是不被发现，而不是破墙。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025"],
     "summary": "说明长城在多数方向上都有两道以上：拆墙过去后两边的守方并不在边墙上拼命，等爬到第二层城墙，守军已在城墙上吃烧烤吃胖了；并以调侃笔法描写破墙者的处境与“毅然来归”者的全副披挂。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": ["P026"],
     "summary": "末尾“科学答集”为平台话题标签混入正文，不属作者论述。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张长城的高度要从山脚下算起而不能从城墙根算起，所以实际有效高度基本都在百米以上；厚度要从墙背算到敌人能有效集结兵力的出发阵地前沿，所以实际有效厚度也在百米以上。",
     "evidence": ["E1", "E2", "E3"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者据此判定修长城的军事价值明显：只要在山顶上修一条路、每隔一段修一个小宿舍，就拥有一座高百米宽百米的巨大城墙，别的砖老天爷都帮你铺好了；“高度”根本不是它的追求。",
     "evidence": ["E4", "E5"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出旁人觉得修长城是“劳民伤财”，但有强烈防御需求的帝王觉得没有比这更便宜的；那些喊着“秦王暴政”的，都是些揣着明白装糊涂的混蛋或者真正的蠢货。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为长城“墙”的作用更类似高铁自带的高架：不是为自身搞出高度，而是造成裕度抹平山峰顶端的高差，使其平缓易通行；严格说它是古代技术条件下修建的一条高架快速路，城楼本质上只是“高速公路服务区”；被视为墙的部分是当时最经济持久的路面支撑技术。",
     "evidence": ["E8", "E9", "E10", "E11"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张这条高速路本质上是一件“空间武器”：沿着它时间会变慢几十倍，两旁穿越者的移动速度是这条路上旅行者的几十分之一；从战略上约等于绿巨人对抗闪电侠。",
     "evidence": ["E12", "E13"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者反驳“长城为封锁经济”之说，认为这基本上谈不上：想控制经济只需要关卡、不需要城，并以西欧不依靠长城、德意志小诸侯靠丘陵间道路设卡敲商旅竹杠为例。",
     "evidence": ["E14", "E15"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出长城的第二个用意是替代萨德：它取的都是地区制高点，烽火一起一日千里，直到电报发明之前一直是人类传递信息最快的手段、从未被超越；烽火台之间有deadman switch，彼此失联超过常规允许的时间限度同样触发报警；要害是不被发现，而不是什么破墙。",
     "evidence": ["E16", "E17", "E18"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出长城不是一道墙，而是几乎在任何方向上都有两道以上，只不过有些只是单独的关隘外加两侧的崇山峻岭。",
     "evidence": ["E19"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以调侃笔法说明破墙者的处境：拆墙过去后两边的守方不会在边墙上拼命，等花一个多月爬到第二层城墙，守军已在城墙上吃烧烤吃胖了；破墙者连一部满电的红米都凑不出来。",
     "evidence": ["E20", "E21"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问：这就是那么多少数民族“毅然来归”的原因；而“来归”的时候，人家可是全族带着全副披挂的。",
     "evidence": ["E22", "E23"]
    }
   ],
   "argument_steps": [
    "先修正提问的“矮”：高度从山脚算、厚度从墙背算到敌军出发阵地前沿（P001-P003）。",
    "用“山顶修路+小宿舍”的换算说明其军事价值，并指出防御需求强者认为它极便宜（P004-P007）。",
    "以“秦王暴政”批评者作靶子，转向对长城功能的重新定义（P008-P009）。",
    "把长城定义为高架快速路与“高速公路服务区”，解释“墙”是当时最经济持久的路面支撑技术，“高度”非其追求（P010-P013）。",
    "提出“空间武器”比喻：沿线时间变慢、两侧移动速度差数十倍（P014-P015）。",
    "反驳“封锁经济”说，指出控制经济只需关卡（P016）。",
    "提出第二个用意：替代萨德，靠烽火与deadman switch实现快速预警，要害是不被发现（P017-P018）。",
    "说明长城在多方向上有多道，破墙者仍需逐层突破（P019-P021）。",
    "以调侃描写破墙者的狼狈与“来归”者的全副披挂收尾（P022-P025）。"
   ],
   "concept_usage": [
    {"term": "长城的“高度”", "meaning": "作者主张按山脚起算的有效高度（百米以上），而非可见墙体本身的高度。", "evidence": "P001", "ambiguity": "作者未给出具体的山体落差或墙体高度数据"},
    {"term": "高架快速路", "meaning": "作者对长城实质的定义：为抹平山峰高差、便于通行而修的路面支撑结构，城楼相当于服务区。", "evidence": "P010", "ambiguity": "是比喻性定义，作者未给出工程学论证"},
    {"term": "空间武器", "meaning": "作者用来形容长城造成的移动速度差：沿墙移动极快，墙外穿越极慢，形成战略优势。", "evidence": "P014", "ambiguity": "“时间会变慢几十倍”为文学化表述，无量化依据"},
    {"term": "deadman switch", "meaning": "作者用该词指烽火台之间以失联超时自动触发报警的机制。", "evidence": "P018", "ambiguity": "作者未提供史料证明该机制的实际存在"},
    {"term": "替代萨德", "meaning": "作者对长城第二个用意的说法：以制高点与烽火体系实现预警。", "evidence": "P017", "ambiguity": "以现代武器系统作比，非历史术语"}
   ],
   "examples_and_targets": [
    "“秦王暴政”的批评者：作者的反驳对象与贬称（P008）。",
    "高铁自带的高架、高速公路服务区：作者的类比物（P009、P010）。",
    "绿巨人对闪电侠：作者的比喻，说明速度差带来的战略优势（P015）。",
    "西欧国家与德意志满地爬的小诸侯设卡敲商旅竹杠：作者用来反驳“封锁经济”说的例子（P016）。",
    "萨德、deadman switch：作者引用的现代军事技术作比（P017、P018）。",
    "王二小、方便面、消息树、啤酒、dota、烧烤、满电的红米：作者调侃式叙事中的通俗意象（P020-P022）。",
    "“来归”的少数民族与全副披挂：作者带调侃的历史叙述（P024、P025）。",
    "上海的房子卖三千一平：作者说明“便宜不捡”心态的类比（P007）。"
   ],
   "conditions": [
    "起算条件：高度从山脚下算起，厚度从墙背算到敌人能有效集结兵力的出发阵地前沿（P001、P003）。",
    "技术条件：“墙”的形态受古代没有现浇钢筋混凝土、没有预制构件技术、又须考虑长期维护成本所限（P011）。",
    "时间限定：长城烽火作为最快信息手段限于“直到电报发明之前”（P018）。",
    "反语式条件：“有本事游牧民族两天翻过去并且把城墙修复，否则挖墙是没有意义的”，强调要害是不被发现（P018）。",
    "未说明：作者未给出长城的高度、厚度、烽火传递速度等具体数据，也未提供史料出处。"
   ],
   "rhetoric_and_tone": "翻案式论证配调侃叙事：先用“第一个问题/第二个问题”的口语结构纠偏，再用“你要不要？不要不是傻吗？”等自问自答推动；比喻密集（高架、服务区、空间武器、绿巨人对抗闪电侠），并穿插粗直贬称（混蛋或者真正的蠢货）与网络化玩笑（方便面、dota、满电的红米、吃烧烤吃胖了）；结尾以“来归”者的全副披挂作反讽收束。",
   "unresolved_questions": [
    "文中关于长城有效高度/厚度、烽火传递速度、deadman switch 机制的说法均未注明史料或数据来源，需外部核查（P001-P003、P018）。",
    "“沿着它，时间会变慢几十倍”为文学化表达，具体所指（行军速度差或调度时间差）本文未说明（P014）。",
    "正文末尾 P026“科学答集”为平台话题标签混入正文（structure.divergence=text_tail_not_in_lexical），不属作者论述。",
    "提问所问“长城能拦住什么”未被直接回答，作者改以修正算法与重新定义长城作答。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "第一个问题，长城的高度要从山脚下算起，不能从城墙根算起。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "所以基本上长城的实际有效高度都在百米以上。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "长城的厚度要从墙背算到敌人能有效集结兵力出发阵地前沿", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你就可以拥有一座高百米宽百米的巨大城墙，别的砖老天爷都帮你铺好了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P013", "quote": "“高度”根本就不是它的追求。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "但是在深感切肤之痛、有强烈的防御需求的帝王们却觉得没有比这更便宜的了", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "那些喊着“秦王暴政”的，都是些揣着明白装糊涂的混蛋或者真正的蠢货。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "其实长城本身的“墙”的作用，更类似我们的高铁所自带的高架", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "严格说，长城只是在古代技术条件下修建的一条高架快速路。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "你们看为墙的东西，是因为古代没有现浇钢筋混凝土，也没有预制构件技术", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "而长城的城楼本质上只是“高速公路服务区”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "这条高速路本质上是一件“空间武器”。沿着它，时间会变慢几十倍。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "从战略上来说，这约等于绿巨人对抗闪电侠。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "有人说长城是为了封锁经济——这基本上是谈不上的。", "relation": "contradicts"},
    {"key": "E15", "paragraph_id": "P016", "quote": "想控制经济，只需要关卡，不需要城。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "长城的第二个用意是替代萨德。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "实际上直到电报发明之前，长城烽火一直是人类传递信息最快的手段，从未被超越。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "彼此之间失联超过常规允许的时间限度，一样会触发报警。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "长城不是一道墙，而是几乎在任何方向上都有两道以上", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "等你吭哧吭哧花了一个多月爬到第二层城墙上，守军在城墙上吃烧烤都吃胖了。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "低头看看你们这一帮老少爷们连一个满电的红米都凑不出来", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "要不然你觉得为什么那么多少数民族“毅然来归”？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "“来归”的时候人家可是全族带着全副披挂的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["古代军事工程", "长城史（作者解释）", "交通与信息传递史", "军事比喻"],
   "issue_candidates": ["长城的高度与厚度如何计算", "长城的军事价值", "长城是否为经济封锁", "烽火预警与deadman switch", "多道城墙的防御纵深"],
   "text_function_candidates": ["答问", "翻案式解释", "反驳", "调侃式科普"],
   "object_candidates": ["长城", "城楼", "烽火台", "游牧民族", "秦王", "德意志诸侯", "西欧国家", "萨德", "高铁"],
   "working_keywords": ["有效高度", "有效厚度", "高架快速路", "高速公路服务区", "空间武器", "deadman switch", "来归"]
  },
  "notes": "无图片、正文非空。提问中“长城这么矮”的前提属提问者，作者以“高度从山脚算、厚度从墙背算”先行修正，已在 question_context 分开登记。正文末尾 P026“科学答集”为平台话题标签混入正文（structure.divergence=text_tail_not_in_lexical），不属作者论述，未纳入内容单元主张。文中的数据与机制说法均无出处，已列入未决问题。"
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
