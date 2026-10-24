# -*- coding: utf-8 -*-
"""批次 r001-b0090 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0090.sessions.py            # 写 out/r001-b0090.out.jsonl
  python3 records/r001-b0090.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0090"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0090.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "8f899e3c": {
  "analysis": {
   "question_context": "提问者自称32岁，昨晚父亲在自己家、当着孩子面打他，问是不是只能忍着。作者未直接评论该具体事件，而把个例普遍化为传统伦理（乡村自然经济、宗族观念）与现代城市商品经济伦理之间的代际冲突，并声明从「身为父母的视角」作答，把答案分为三层、两视角共六章。提问者的受害者立场不等于作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "把个例普遍化：冲突是现代伦理的独立个人与传统伦理的家长之间的冲突，所有中国父母或多或少都有角色转换困难，痛苦有时不动声色。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "问题分三层（消解痛苦、避免惨烈爆发、已爆发如何补救），每层分父母与子女两视角，共六章，先说父母视角。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "指出找到此答案的多是已遭遇事故的子女，讲「子女如何避免」已晚；转向「将来你也会是父母」的预防视角。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "爱的规则：首要出于爱；最根本规则是「不许要求回报」；一开口即变异为以爱为掩护的交易，前者有价且贬值，后者无价。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022"], "summary": "求回报使奉献变为强制非法放债；以「恩人还是债主」「垃圾债债主」等反问与类比说明其必败。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "不求回报者获得父母梦寐以求的信靠与影响力（爱的权柄）；一旦越线全部消失，法庭军队也挽不回。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035"], "summary": "劝诫不要怕爱吃亏；同时承认终身不求回报、不抱怨极难，「金身不破」近乎不可能。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "转为未标注说话者的第一人称悲愤独白与反问：父母辛劳、子女薄凉、委屈不会有平反之日，末尾「呵呵」「你说，我好不好笑？」。", "role": "other"},
    {"unit_id": "U009", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053"], "summary": "连续反问「你抱怨不抱怨」「有人能永远不抱怨吗」，答「至少我不能」「我也不能」；但能与不能并不改变爱的规则，「天道无情」。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058"], "summary": "转向「接下去可以怎么办」：爱极易破损也极易修补，不要求金身不破，只要求清醒后为没做到、没守住而道歉。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063"], "summary": "认错本身即极大修复；否认且主张「这没啥」等于废除承诺；坚持承认与道歉仍是实践意义上完整的爱。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071"], "summary": "什么是道歉、如何道歉：老老实实去做，丢球了就道歉；真诚道歉一般获原谅，未获原谅则原谅人的不原谅。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080"], "summary": "结论：做/不求回报/不抱怨/道歉是爱的能力，原谅是被爱的能力；原谅非外交手段而是承诺；人类的爱靠被宽容而运行，爱需要爱来宽恕和赦免。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "传统伦理基于乡村自然经济与宗族观念，而中国人实际生活于城市生活与商品经济社会，这使几乎每个中国人从幼年转向成年时都要经历剧烈冲突。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "该冲突不只是子女与父母之间的私人过节，而是现代伦理的独立个人与传统伦理的家长之间的冲突；不应认为只是父母特别糟糕。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "所有中国父母或多或少都有这种角色转换困难，且这种转换或多或少通过一次类似惨痛的撕裂完成。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "这种痛苦有时候不动声色，不以怒吼抱怨等方式爆发，因此子女不见得知道。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题分三层（消解痛苦、避免惨烈爆发、已爆发如何补救），每层分父母与子女两视角，答案共应有六章。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "找到此问题的人往往是已遭遇惨烈关系事故的子女，谈「子女如何避免事故」已为时已晚，故先从父母视角讲预防。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "首要的是确保自己对子女所做的事尽可能出于爱。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱有规则，最重要也最根本的规则是「不许要求回报」。", "evidence": ["E9", "E34"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要一开口要求回报，奉献就会变异为以爱为掩护、诱使他人接受而后变脸的交易。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若能做到不求回报（哪怕是憋出来、装出来的），奉献才成其为爱，对方会报之以爱。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方回报的不是你付出的奉献，而是你的不求回报；前者有价且贬值，后者无价。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一开口就使「无私」与「奉献」失效而变成强制放债；要求回报者会被对方立刻转向敌对，并给对方迎头痛击的立场。", "evidence": ["E13", "E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不许抱怨、不许求偿是爱残酷的一面；正因其残酷才珍贵有力、触动灵魂。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不求回报所换来的信靠是父母梦寐以求的影响力、专属于爱的权柄；一旦越线就全部消失，全世界的法庭与军队也挽不回。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "一辈子不开口求回报、不吹嘘功劳极其难以做到；本能与周围世界的影响使「金身不破」近乎不可能。", "evidence": ["E17"]},
    {"claim_id": "C016", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "P036-P047 出现未标注说话者的第一人称悲愤独白（如「就算别人能，至少我不能」），无法确定是作者自述、代父母立言还是引述父母口吻，本记录不将其归为作者主张。", "evidence": ["E18"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能与不能并不改变爱的残酷规则，「天道无情」，一分一毫也不会改变。", "evidence": ["E19", "E20"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱极易破损也极易修补；它不要求金身不破，只要求人在头脑清醒、心平气和之后为没有做到、没有守住而道歉。", "evidence": ["E21", "E22"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "只要承认这是错事、坏事、不该再次发生且值得抱歉补偿的事，即使尚未做实质补偿，错误也已被极大程度修复；反之主张「这没啥」就等于废除承诺。", "evidence": ["E23", "E24"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不需要完美无缺，只需在意识到没有做到时坚持承认、坚持道歉，这仍是实践意义上完整的爱。", "evidence": ["E25"]},
    {"claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "真诚的道歉一般都会得到原谅；如果没有得到原谅，那么原谅人的不原谅。", "evidence": ["E26", "E27"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「做」「不求回报」「不抱怨」「道歉」是爱的能力，而原谅是被爱的能力。", "evidence": ["E28"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "原谅不是为解决、平息争端或让关系move on的外交手段，也根本不可以是这种东西。", "evidence": ["E29"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原谅是接受被爱者身份的人对爱自己者的承诺；人类的爱不是美德而是自私自利的罪行，靠被宽容、被饶恕、被成全而运行。", "evidence": ["E30", "E31"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "必须爱一个爱你的人，因为只有爱你的人才能宽容、原谅你的爱；爱不是要爱来回报，而是需要爱来宽恕和赦免。", "evidence": ["E32", "E33"]}
   ],
   "argument_steps": [
    "前提：传统伦理（乡村自然经济／宗族）与现代城市商品经济伦理错位，造成几乎每个中国人的成年转折冲突（P001-P003）",
    "普遍化：不是私人过节，而是伦理角色的转换困难，痛苦有时无声（P002-P004）",
    "问题分解：三层×两视角=六章，先讲父母视角（P005-P007）",
    "读者定位：来的多是已受伤的子女，转向「将来你也会是父母」（P008-P010）",
    "立规则：首要出于爱；不许要求回报；开口即成交易（P011-P016）",
    "追问后果：强制放债／恩人与债主之辨；爱的权柄与信靠（P017-P031）",
    "让步：承认终身不抱怨极难，「金身不破」近乎不可能（P032-P035）",
    "未标注说话者的第一人称独白与连续反问（P036-P051）",
    "转折：能与不能不改变爱的规则（P052-P053）",
    "转向补救：爱可修补，重在察觉后道歉（P054-P063）",
    "定义道歉与原谅（P064-P076）",
    "结论：爱与宽恕、赦免的关系（P077-P080）"
   ],
   "concept_usage": [
    {"term": "爱（爱的规则）", "meaning": "以「不许要求回报」为根本规则的行为与关系；一开口求偿即变异为交易", "evidence": "P012", "ambiguity": "P036-P047 的第一人称悲愤与 P077「人类的爱……是罪行」是否同指此爱，文中未明确区隔"},
    {"term": "强制放贷／非法放贷／垃圾债", "meaning": "父母要求子女回报其奉献时，奉献变成强制且非法的债", "evidence": "P017", "ambiguity": "「垃圾债」只作类比修辞，未给定义"},
    {"term": "金身不破", "meaning": "一辈子不开口求回报、不抱怨的完美状态", "evidence": "P035", "ambiguity": "未注明出处，属文中自造表述"},
    {"term": "爱的权柄／影响力", "meaning": "不求回报者自然获得的信靠与影响力，是父母梦寐以求之物", "evidence": "P031", "ambiguity": "未说明与一般「权力」的区别"},
    {"term": "道歉", "meaning": "头脑清醒后对没做到、没守住爱的规则的承认与补偿意愿", "evidence": "P057", "ambiguity": "P064 只提出「什么是道歉」，未给正式定义"},
    {"term": "原谅（被爱的能力）", "meaning": "接受被爱者身份者对爱自己者的承诺，而非外交手段", "evidence": "P076", "ambiguity": "P068「原谅人的不原谅」如何操作未展开"},
    {"term": "天道无情", "meaning": "爱的规则不因人的能与不能而改变", "evidence": "P053", "ambiguity": "宗教／哲学来源未说明"}
   ],
   "examples_and_targets": [
    "提问者个例（32岁被父亲在自己家、当着孩子面打）：由提问者提供；作者未直接评论该事件，仅作普遍化处理（P002 转为对「你」说话）",
    "「垃圾债的债主」「强制放债」：作者的类比与修辞（P018、P022）",
    "「全世界的法庭和军队都站在你这一边」：修辞材料，强调爱的权柄无法被外力挽回（P031）",
    "化用「往者不可追矣，来者犹可谏」：文言修辞（P009）",
    "P036-P047 父母的辛劳与子女薄凉场景（做牛做马、被视如敝履、子女将来只会尴尬大笑「哪有」）：第一人称抒情与举例，说话者未标注"
   ],
   "conditions": [
    "限定于中国父母子女关系：「中国人」「所有的中国父母或多或少」（P001、P003）",
    "以「有时候」限定痛苦不动声色，非全称（P004）",
    "分层设条件：「如果痛苦本身不能消解」「如果这种爆发已经发生了」（P005）",
    "放宽条件：「哪怕你是憋出来的、装出来的」（P014）",
    "假设句群：「如果我有秘密必须托付于人」「如果我有软肋不能不交托给人」（P026、P027）",
    "自陈限度：「近乎于不可能」「至少我不能」「我也不能」（P035、P050、P051）",
    "让步条件：「即使你都还没有做任何实质的补偿」（P060）",
    "概率性表述：「真诚的道歉，一般都会得到原谅」（P067）"
   ],
   "rhetoric_and_tone": "第二人称劝诫与训诫（「你要记住了」「记好了」「不要怕」）；密集设问与反问（P019-P030、P034、P037、P047-P051、P058）；P036-P047 转用未标注说话者的第一人称悲愤独白，含「呵呵」自嘲与「你说，我好不好笑？」；文言化用「往者不可追矣，来者犹可谏」；以引号强调并自称「加大、加粗、加黑」的「不可以」（P020）；词汇带天道、赦免等宗教色彩（P053、P080）。",
   "unresolved_questions": [
    "P036-P047 通篇第一人称「我」（父母悲愤独白）未标注说话者，无法确定是作者代父母立言、引述某种父母口吻还是作者自述；本记录未将其归为作者主张。",
    "P008 称「这个答案一共应该有六个章节」，但正文只写出父母视角部分，子女视角三章未见；是正文不完整、分篇发布还是其他原因，本文未说明。",
    "P020「一个加大、加粗、加黑的“不可以”」提示原文含富文本排版（加粗／加大），纯文本转录丢失该信息。",
    "P065 仅「如何正确地跟别人道歉？」一句，与同批《道歉》篇提问文字相同，且被生成器标为 lexical 未覆盖片段；疑为平台相关问题或内链节点而非作者正文，归属不明。",
    "P077「人类的爱……是一种自私自利、自说自话的罪行」等断言的依据（宗教或哲学来源）本文未注明，属待外部核查。",
    "updated_at（2025-06-03）晚于 published_at（2021-01-17），语料未给出修改内容，版本差异待核。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中国人最大的痛苦之一，就是传统的伦理观念是基于乡村自然经济和宗族观念的", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这冲突不只是发生在子女与父母之间，而是发生在现代伦理的独立个人与传统伦理的家长之间", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "是所有的中国父母或多或少都有这样的角色转换困难", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这种痛苦有时候不动声色", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "第一层，是如何消解这份痛苦；第二层，是如果痛苦本身不能消解，如何避免这种惨烈的爆发；第三层，是如果这种爆发已经发生了，应该如何补救。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这个答案一共应该有六个章节", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "谈“身为子女如何避免事故”已经为时已晚", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "首要的，要确保你对子女所做的事是尽可能出于爱的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "最重要也是最根本的规则就是“不许要求回报”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "只要你一开口，这件事就会变异为交易", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "哪怕你是憋出来的、装出来的", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P015", "quote": "对方并非是在回报你付出的奉献，而是在回报你的不求回报。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "“奉献”也谈不上了，变成强制放债了", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "不提，就是爱，对方就无法无痛地辜负；提了，就是非法放贷", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "不许抱怨、不许求偿，这就是爱残酷的一面", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P031", "quote": "你一过红线，它们一起消失", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P035", "quote": "一辈子不开口求回报，也不开口吹嘘功劳，这当然是极其难以做到的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P050", "quote": "就算别人能，至少我不能。", "relation": "context"},
    {"key": "E19", "paragraph_id": "P052", "quote": "但是能与不能，并不会改变爱这种残酷的规则。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P053", "quote": "天道无情，一分一毫也不会改变。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P056", "quote": "爱固然极易破损，但也极易修补。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P057", "quote": "你要为没有做到、没有守住而道歉", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P060", "quote": "这错都被极大程度地修复了", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P061", "quote": "这就实实在在地意味着这承诺等于废除了", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P063", "quote": "你只需要在意识到没有做到的时候坚持承认、坚持道歉", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P067", "quote": "真诚的道歉，一般都会得到原谅。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P068", "quote": "如果没有得到原谅，那么原谅人的不原谅。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P072", "quote": "我们只讲了“做”“不求回报”“不抱怨”和“道歉”，这是爱的能力", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P074", "quote": "原谅，不是一种为了解决问题、平息争端、让双方关系好move on的外交手段。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P076", "quote": "原谅是接受被爱者身份的人对爱自己的人的一种承诺。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P077", "quote": "人类的爱，并不是一种美德，而是一种自私自利、自说自话的罪行。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P079", "quote": "因为只有爱你的人，才能宽容、原谅你的爱。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P080", "quote": "爱不是要爱来回报，爱是需要爱来宽恕和赦免。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P020", "quote": "一个加大、加粗、加黑的“不可以”。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P065", "quote": "如何正确地跟别人道歉？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭伦理与代际关系", "伦理学／道德哲学", "社会变迁与传统伦理"],
   "issue_candidates": ["父母要求回报与养育之恩", "代际冲突（传统伦理vs现代个人）", "道歉与原谅的条件", "爱的规则与影响力"],
   "text_function_candidates": ["答疑", "训诫／劝诫", "理论阐释", "抒情独白"],
   "object_candidates": ["中国父母与子女", "提问者（32岁子女）", "法庭与军队（修辞指代）"],
   "working_keywords": ["不许要求回报", "强制放贷", "垃圾债", "金身不破", "爱的权柄", "天道无情", "被爱的能力", "赦免"]
  },
  "notes": "无图片节点。text 与 lexical 存在 1 处 divergence：char 2603 起「如何正确地跟别人道歉？」为 text 有而 lexical 未覆盖的片段（对应 P065），已在 unresolved_questions 登记。brief 在语料中被截断（止于「……传统伦理的家长」），仅作导航；published_at(2021-01-17) 与 updated_at(2025-06-03) 不一致，修改内容未给出。"
 },
 "0c308005": {
  "analysis": {
   "question_context": "提问者问如何看《天天向上》主持人问「你们最希望哪道菜消失」时蔡澜答「火锅是最没文化的料理方式」。蔡澜的话只由提问字段转述，属被反驳观点，不是作者立场；作者不讨论节目语境，而是直接反驳「火锅没文化」并顺带推广到「任何有历史的事物」。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "定义与重新归类：火锅不是一道菜，而是把炉火端上桌、由食客自己完成烹饪的烹饪方式；自己才是最后的厨师，吃到什么很大程度取决于食客手艺。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "以自己炒菜的类比与先下／后下、蘸料、配酒等讲究说明：大部分人其实不懂怎么吃火锅，同一锅里各人吃到的是不同的菜。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012"], "summary": "比较性判断：火锅门道比寿司、竹升面、干炒牛河深得多，不是一个数量级；火锅与煎炒煮炸烤蒸并列，与「一道菜」相比是心里没数。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "反驳与推广：说「火锅没文化」是无知无畏；凡有历史的事物说其「没有文化」都是扯淡，做的时间够长、做的人够多，「没有文化」从定义上不可能。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "火锅根本就不是一道菜。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "火锅是一种烹饪方式，是把炉火端上了桌、由食客自己完成烹饪过程的一种烹饪方式。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自己煮好、捞好、蘸好、摆进碗里的才是真正的菜；自己才是最后的厨师，厨房只是做汤底配料的助手。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "同一个锅里吃到什么，很大程度上取决于吃的人自己的手艺；懂得的人出手，碗里的更好吃。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "大部分人其实不懂怎么吃火锅，根本是乱吃一气；同一个锅里同样的食材，每个人吃到的其实是不一样的菜。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "火锅的门道比寿司、竹升面、干炒牛河这类小品深得多，根本不是一个数量级。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "火锅是和煎、炒、煮、炸、烤、蒸并列的事物，拿它和「一道菜」比根本属于心里没数。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "光是什么能下、什么不能下，就有一大半人不懂。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说出「火锅没文化」这种话是无知无畏。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说任何有历史的事物「没有文化」都是扯淡；一件事情做的时间够长、做的人够多，「没有文化」从定义上说是不可能的。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的观点（仅由提问字段转述）：蔡澜在《天天向上》称「火锅是最没文化的料理方式」；作者以「居然说出“火锅没文化”这种傻大胆的话」复述并反驳之。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "先否定归类：火锅不是一道菜（P001）",
    "给出替代定义：火锅是烹饪方式，食客自己完成烹饪（P002）",
    "推出主体转移：自己才是最后的厨师，成品才算菜（P003-P004）",
    "承认程度差异：吃到什么很大程度取决于食客手艺（P005）",
    "经验判断加类比：大部分人乱吃，各人所得不同（P006-P007）",
    "列讲究（先下后下、蘸料、配酒）支持「门道」主张（P009-P010）",
    "比较论证：火锅门道远超寿司等小品，且与煎炒煮炸烤蒸并列（P011-P012）",
    "反驳被反驳观点并推广为一般命题（P013-P016）"
   ],
   "concept_usage": [
    {"term": "火锅", "meaning": "被作者界定为一种烹饪方式（把炉火端上桌、由食客完成烹饪），而非一道菜", "evidence": "P002", "ambiguity": "与日常用法（指一种餐饮／菜式）不同，作者未说明是否接受日常用法"},
    {"term": "文化／没文化", "meaning": "以「有历史」为判据：做的时间够长、做的人够多即不可能「没有文化」", "evidence": "P016", "ambiguity": "未给出「文化」的正面定义，仅以历史长度与人数的判据反证"},
    {"term": "门道", "meaning": "食材下锅次序、吃法、蘸料调配、配酒等具体知识与讲究", "evidence": "P009", "ambiguity": "未给出衡量「门道」深浅的标准，比较结论为断言"},
    {"term": "小品（寿司、竹升面、干炒牛河）", "meaning": "被作者用作与火锅对比的较小规模料理", "evidence": "P011", "ambiguity": "「小品」在此为贬抑性归类，未界定范围"}
   ],
   "examples_and_targets": [
    "《天天向上》主持人提问与蔡澜的回答：仅由提问字段转述，是被反驳观点的来源，非作者观点（P013 复述其说法）",
    "寿司、竹升面、干炒牛河：作者用作比较对象（P011）",
    "煎、炒、煮、炸、烤、蒸：作者用作火锅的并列项（P012）",
    "自己炒菜与师傅炒菜的对比：作者的类比（P007）",
    "先下什么、后下什么、蘸料、配酒等：作者列举的经验细节（P009）"
   ],
   "conditions": [
    "程度限定：「很大程度上取决于吃的人自己的手艺」（P005）",
    "非全称判断：「大部分人其实不懂怎么吃火锅」「一大半人不懂」（P006、P010）",
    "推广命题的条件：对象须「有历史」，且「做的时间够长、做的人够多」（P015、P016）",
    "本文为短答，未给出「火锅门道更深」的判定标准与系统论证"
   ],
   "rhetoric_and_tone": "短段递进、断言式定义句开场；口语化与贬抑性措辞（「说句实话」「说实在的」「傻大胆」「无知无畏」「扯淡」「通杀」）；以「顺便来个通杀——」宣战式转入一般命题；末段用定义式反证收束（P016）。无脏话，但语气强硬、带嘲讽。",
   "unresolved_questions": [
    "蔡澜「火锅是最没文化的料理方式」的原话措辞与节目语境仅由提问字段转述，未见原始出处，属待外部核查。",
    "作者未给出「文化」的正面定义，只以「有历史→不可能没文化」作定义式断言；该判据本身未加论证。",
    "P011 的比较结论（火锅门道远超寿司等）未给判别标准，属断言。",
    "updated_at（2025-10-02）远晚于 published_at（2021-01-18），语料未给出修改内容，版本差异待核。",
    "brief 与正文高度重合但来源与用途未说明（brief 在语料中未见截断标记）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "火锅根本就不是一道菜。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "火锅是一种烹饪方式，是把炉火端上了桌、由食客自己完成烹饪过程的一种烹饪方式。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你自己煮好、捞好、蘸好、摆进碗里的，才是真正的菜。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你自己才是最后的厨师，厨房里只是帮你做汤底配料的助手而已。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "同一个锅，吃到什么，很大程度上取决于吃的人自己的手艺。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "懂得的人出手，ta碗里的更好吃。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "大部分人其实不懂怎么吃火锅，根本是乱吃一气。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "同一个锅里，同样的食材，每个人吃到的其实是不一样的菜。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "火锅的门道比寿司、竹升面、干炒牛河这类小品不知道深到哪里去了", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "火锅是和煎、炒、煮、炸、烤、蒸并列的事物，拿它和“一道菜”比根本属于心里没数。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "光是什么能下、什么不能下，就这一条就有一大半人不懂。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "居然说出“火锅没文化”这种傻大胆的话，真的是无知无畏。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "说任何有历史的事物“没有文化”都是扯淡。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "一件事情，做的时间够长、做的人够多，“没有文化”从定义上说是不可能的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "居然说出“火锅没文化”这种傻大胆的话", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["饮食文化", "烹饪技艺", "文化评论"],
   "issue_candidates": ["火锅是否算一道菜", "「没文化」的判定标准", "厨艺与食客手艺的关系"],
   "text_function_candidates": ["答疑", "反驳／论辩", "科普式说明"],
   "object_candidates": ["蔡澜", "《天天向上》节目与主持人", "寿司／竹升面／干炒牛河（比较对象）"],
   "working_keywords": ["火锅", "烹饪方式", "一道菜", "没文化", "门道", "蘸料", "汤底", "无知无畏"]
  },
  "notes": "无图片节点，正文完整可读。蔡澜言论出自提问字段（questioner 转述），已按 opponent_view 处理，未归给作者。brief 与正文内容高度重合，仅作导航。updated_at(2025-10-02) 晚于 published_at(2021-01-18)，修改内容未给出。"
 },
 "648586c8": {
  "analysis": {
   "question_context": "提问者问「如何正确地跟别人道歉？」。作者给出一套分四步的正面方法（定义事项→解释错误逻辑→给出降低概率的措施→献祭），并以 heading 标出各步；文中未讨论提问者的具体情境，属方法性问答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "第一步（标题）：要清楚定义道歉的事项——为具体什么事情、什么情节、什么行为道歉，该事项须满足若干条件。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "三个条件：违反你坚持的道义（并由此定义你的道义）；你不希望它再次发生（否则并不真认为这是错误）；它可以以合理成本降低发生概率（不可控的负面事件只是天意，只能遗憾同情，为不可控之事道歉是招来诅咒的傲慢，如为地震道歉）。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "准确定义是微妙事务，要反复思索、反复用条件反问；通不过检测即没想明白，并设问没想明白怎么办。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "没想明白就是没想明白，不要装明白；更要紧的是接着想，不要以想不明白为由拖着等风头过去。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "反驳「躲过风头就行」：被重提时以「你怎么总是揪着以前的事不放」回应，反问「在逃」是否等于「结案」；拖着会把价值观碰撞升级为关乎人格与尊重的根本原则，一句「旧事重提」足以判关系死刑。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "限定：不能以父母将就一辈子为「可行」依据，那是年代所迫；经济繁荣的价值就在于不必那样将就。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "第二步（标题）：解释你基于什么规则、什么逻辑认定这件事是错的；只说错而不解释的潜台词是「顺着你说」；试探猜测对方为何生气是敷衍和侮辱，只会进一步破坏关系。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029"], "summary": "解释错误逻辑即袒露价值观的自省与变迁；真正需要且有用的道歉背后都是价值观变迁而非「不小心」；错在驱使行为的动机存在逻辑缺陷，不在结果让对方痛苦。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031", "P032"], "summary": "对成熟者而言痛苦次要且不可选择，使痛苦被救赎的是痛苦本身的价值；若痛苦能换智慧与成熟，作者不拒绝反以为荣幸；道歉是有神奇力量的圣事，神力核心在「错」上。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "若痛苦经自省转为更成熟完善的价值观，则消解并升华为对方幸福，关系更坚固；真正让人得宽慰的是你的成长；真爱者道歉出于对对方价值观缺陷的忧虑与害怕最终只能离开。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P040", "P041"], "summary": "若上述机制无效，「爱」不过是榨取内啡肽的罂粟，吸毒没有好结果。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047"], "summary": "限定与让步：寻找错误症结是复杂思考工作；你不需要真的正确而需要真诚；真诚的笨拙所致的错误是「正确的错误」、通向真理的最短道路，但不保证结果，也可能导致关系终结；表演讨人喜欢的版本是最大的幻觉。", "role": "qualification"},
    {"unit_id": "U013", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065"], "summary": "理由「人是莫测的」：媒体上的「女生吃这一套」等说法不保证对面前这人有效；用别人赌注见输赢的追问；装一辈子与中晚年崩盘之问；保持真诚则收获与错过都该当，相信最好安排者终获踏实的宁静，而宁静是魅力源泉。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080"], "summary": "第三步（标题）：给出降低同样事件发生概率的具体措施；说「不会再发生了」是蠢话——改正过程漫长反复如精神长征；改为「降低概率」则方案难度大降；拿出计划比甜言蜜语更直接、更浪漫、更性感。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P081", "P082", "P083", "P084", "P085", "P086", "P087"], "summary": "第四步（标题）：全备的道歉需要献祭——话语没有分量，痛苦与损失必须实实在在、无可作伪（面壁、斋戒、禁足、自请扣除酬劳），且不留把道歉当逃脱惩罚机会的余地；否则等于教自己「会道歉就可免罚」，练成「道歉艺术家」走上更大的邪道。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道歉第一步是清楚定义道歉的事项——为具体什么事情、什么情节、什么行为道歉。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "事项须违反你坚持的道义；人也通过把该行为承认为错误而定义了自己的道义。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "事项须是你不希望再次发生的；若并不在乎它是否再次发生，就并不真的认为这是错误。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "事项须能以合理成本降低发生概率；无法以可承受成本管理的负面事件本质上只是天意，对此只能表示遗憾与同情，不能表示歉意。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "为根本管控不了的东西道歉是一种会招来诅咒的傲慢；例如不能为地震道歉。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "准确定义道歉事项是非常微妙的事务，要反复思索、反复用上述条件反问；通不过检测意味着还没想明白。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "没想明白就是没想明白，不要装明白。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没想明白要接着想，不要以想不明白为由拖着、等风头过了就自以为「过去了」。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拖着自以为无疾而终不但解决不了问题，还会把本来不要紧的价值观碰撞升级到关乎人格与尊重的根本原则的高度。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一句轻飘飘的「你怎么总是旧事重提」，在对方心里是足以判关系死刑的重罪。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "negated", "statement": "不能因父母似乎这样混了一辈子就认为「躲过风头就行」可行；父母将就是因那个年代不将就很难，经济繁荣的价值正在于不必那样将就。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二步要解释你基于什么样的规则与逻辑认定这件事是错的；只说是错的而不解释，潜台词是「我没啥办法，所以顺着你说」。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "试探、猜测对方为什么生气以快点蒙对并不是道歉，而是一种敷衍和侮辱，只会进一步破坏关系。", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "解释错误逻辑时人实际上是在袒露自己价值观的自省和变迁；真正需要且有用的道歉背后都是某种价值观的变迁，而非「不小心」。", "evidence": ["E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说你错了，不是错在行为的结果让对方痛苦，而是错在驱使你那样做的动机存在逻辑的缺陷。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "对成熟的人、神性完善的人，痛苦其实极端次要且不可选择，使痛苦被救赎与宽慰的是痛苦本身的价值；若这痛苦可以换智慧与成熟，作者自陈何止不拒绝，反以为是莫大荣幸。", "evidence": ["E22", "E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道歉是一种有难以置信的神奇力量的圣事，其神力核心就在这关键的「错」上。", "evidence": ["E24"]},
    {"claim_id": "C018", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "对方的痛苦若经你的自省转变为更成熟和完善的价值观，痛苦不但消解，反而升华为对方极大的幸福，关系还比之前更坚固。", "evidence": ["E25", "E26"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真正让对方得宽慰、得希望的不是你意识到和体谅对方的痛苦，而是你真的因此有所成长和完善。", "evidence": ["E27"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真爱者道歉不是出于抚慰自己受伤心灵的需要，其焦虑期待源于对对方价值观缺陷的极端忧虑，以及害怕最终证实唯有离开是剩下的选择。", "evidence": ["E28", "E29", "E30", "E31"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你不需要真的正确，你需要的是真诚；真诚的笨拙所致的错误是正确的错误，是通向真理的最短道路。", "evidence": ["E34", "E35", "E36"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若上述机制无效，「爱」就不过是用来榨取内啡肽的罂粟，而吸毒没有好结果。", "evidence": ["E32", "E33"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "真诚并不保证结果：不能保证它不是谬误，也不能保证对方接受，它同样可能导致关系的终结。", "evidence": ["E37", "E38"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自以为表演一个讨人喜欢的版本可以带来更好的结局，本身是一种最大的幻觉。", "evidence": ["E39"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人是莫测的；从大众媒体上看到的「女生吃这一套」「男生都喜欢xx」就算是真的，也根本不意味着对你面前这人有效。", "evidence": ["E40"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "保持真诚，收获与错过的都是你该得的；若相信一切都是可以有的最好安排，最终一定会获得踏实的宁静，而这份宁静是世界上最性感的东西、是魅力源泉。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第三步是给出降低同样事件发生概率的具体措施；说「这件事不会再发生了」是蠢话。", "evidence": ["E44", "E45"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对一个长期隐藏、直到最近才承认存在的错误，人改正的过程之漫长、反复之多不下于一次精神的长征，并且未必能在死前真正到达终点。", "evidence": ["E46", "E47"]},
    {"claim_id": "C029", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果对方真的在乎这段关系、视其为终身之托，同时又不是天真之辈，那么说「不会再发生」不但不会收到奇效，反而要构成冒犯和伤害。", "evidence": ["E48"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把目标从「不会再发生」改为「降低发生的概率」，提出可行方案的难度大为降低，而前者实际上根本不可行。", "evidence": ["E49"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对道歉的真诚与对避免再发生的在意，会在「降低概率计划」的可操作性、费效比和可检验性上最直观地体现出来；拿出这样的计划比任何甜言蜜语都更直接、更浪漫、更性感。", "evidence": ["E50", "E51"]},
    {"claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全备的道歉需要献祭：话语本身没有分量，痛苦与损失必须实实在在、无可作伪（例如面壁、斋戒、禁足、自请扣除酬劳）。", "evidence": ["E52", "E53", "E54", "E55"]},
    {"claim_id": "C033", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "道歉不止是「以后注意」，要这一次也绝不自我宽纵，绝不给自己留任何把道歉当作逃脱应有惩罚的机会的余地。", "evidence": ["E56"]},
    {"claim_id": "C034", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若说完该说的话最终果然免于痛苦，人就在客观上教导自己「只要会道歉就可以逃脱惩罚」；不以祭献封堵这个破口，人很容易练成「道歉艺术家」而走上更大的邪道。", "evidence": ["E57", "E58"]}
   ],
   "argument_steps": [
    "第一步（heading P001）：定义道歉事项，并给出三条检验条件（P003-P005）",
    "条件论证：道义、再发生意愿、可控成本；不可控者归为天意，不得道歉（P005）",
    "设问过渡：一时想不明白怎么办（P007）",
    "行动要求：不装明白、接着想、不许拖（P008-P009）",
    "反证拖延：被重提时的责难、在逃与结案之辨、关系死刑（P010-P019）",
    "让步/限定：父母将就不是可行依据（P020-P021）",
    "第二步（heading P022）：解释认定错误的规则与逻辑（P023-P026）",
    "论错误所在：动机的逻辑缺陷而非结果的痛苦（P027-P029）",
    "价值论支撑：痛苦的价值、道歉的圣事性与成长（P030-P039）",
    "反证：机制无效则爱成罂粟（P040-P041）",
    "让步：真诚不保证结果，但表演是最大的幻觉（P042-P047）",
    "理由：人是莫测的，故只能用自己的赌注（P048-P065）",
    "第三步（heading P066）：以「降低概率」取代「不会再发生」（P067-P080）",
    "第四步（heading P081）：献祭封堵「道歉免罚」的破口（P082-P087）"
   ],
   "concept_usage": [
    {"term": "道歉（四步）", "meaning": "定义事项→解释错误逻辑→给出降低概率的措施→献祭；第四步被称为「全备的道歉」", "evidence": "P081", "ambiguity": "四步是否缺一不可、前三步是否也能算道歉，正文未明确"},
    {"term": "正确的错误／真诚", "meaning": "真诚的笨拙所致的错误，被视为通向真理的最短道路", "evidence": "P044", "ambiguity": "未给出「真诚」的判定标准，只说不需要真的正确"},
    {"term": "献祭／祭献", "meaning": "道歉中必须付出的、实实在在且无可作伪的痛苦与损失", "evidence": "P083", "ambiguity": "以「例如」列举形式给出，是否为穷尽清单、由谁监督，均未说明"},
    {"term": "圣事／神性", "meaning": "用以形容道歉的神奇力量；「神性完善的人」指成熟者", "evidence": "P032", "ambiguity": "宗教语汇的来源与确切含义未注明"},
    {"term": "价值观的变迁", "meaning": "真正需要道歉之事的根源：从以为对到发现错的转变", "evidence": "P028", "ambiguity": "与「不小心」的界线由作者断言，未给判据"},
    {"term": "天意", "meaning": "无法以可承受成本管理的负面事件，只能遗憾同情而不能道歉", "evidence": "P005", "ambiguity": "「可承受的成本」标准未量化"},
    {"term": "赌注（自己的／别人的）", "meaning": "以真诚面对输赢，还是借表演与大众套路面对输赢", "evidence": "P052", "ambiguity": "为比喻用法，未给出可操作区分"}
   ],
   "examples_and_targets": [
    "地震（「你就不能为地震道歉。为地震道歉，你是说你是上帝吗？」）：作者的例证与反问（P005）",
    "「你怎么总是揪着以前的事不放？！」「你怎么总是旧事重提」：被反驳的拖延话术（P010、P017）",
    "「这件事不会再发生了（It won’t happen again）」：被批评的话术（P067）",
    "大众媒体说法「女生吃这一套」「男生都喜欢xx」：被引用并质疑有效性的说法（P048）",
    "面壁一小时、斋戒一个月、禁足半个月、自请扣除酬劳：作者列举的献祭形式（P084）",
    "喂糖游戏、罂粟、吸毒、驯兽、精神的长征、道歉艺术家：作者的贬抑性比喻（P035、P040、P041、P051、P068、P087）",
    "打工心态的人与不重视你的供应商：作者用以刻画敷衍道歉者的比喻对象（P072）"
   ],
   "conditions": [
    "三条件句：「它是违反你坚持的道义的」「它是你不希望再次发生的」「它是可以以合理的成本来降低发生概率的」（P003-P005）",
    "反条件：「如果你并不在乎它是不是再次发生，你就并不真的认为这是个错误」（P004）",
    "不可控边界：「一个无法以可以承受的成本来管理的负面事件，本质上只是一种你无能为力的不幸」（P005）",
    "反事实：「如果这种“躲过风头就行”的模式被承认合法」（P014）",
    "假设：「如果这痛苦可以换你的智慧和成熟」（P031）、「如果这机制无效」（P040）",
    "对象条件：「如果对方真的在乎这段关系，视其为终身之托，同时又不是天真之辈」（P073）",
    "献祭边界：「这些痛苦与损失不应该影响健康，但必须实实在在，无可作伪」（P083）",
    "或然表述：「往往不是根本就没把这事放在心上」（P071）"
   ],
   "rhetoric_and_tone": "以四步 heading 统领的训导式长文；第二人称「你」直接劝诫；密集设问与反问（「在逃」等于「结案」吗？／难道你不是因为ta特别所以才被ta羁绊的吗？／能混这个月，能混十年、二十年吗？）；郑重宣告语气（「我实实在在的告诉你」）；宗教语汇（圣事、神性、献祭、邪道）；贬抑比喻（喂糖游戏、罂粟、吸毒、驯兽、道歉艺术家）；P030-P031 为第一人称自陈；P039 人称与对象突然切换（「你爱我，我的痛苦……」）。",
   "unresolved_questions": [
    "P039「你爱我，我的痛苦自然而然会成为你不能放下的痛苦」人称与对象相对前后文突然切换，说话者与受话者归属不确定。",
    "P030「神性完善的人」、P032「圣事」、P081/P087「献祭／祭献」等宗教语汇的来源与确切含义，本文未注明，属待外部核查。",
    "P062「你若相信一切都是可以有的最好安排」是否引用或暗指某学说，正文未注明，属待外部核查。",
    "P084 献祭形式以「例如」列出，是否为穷尽清单、是否需第三方监督执行，均未说明。",
    "「全备的道歉」是否意味着四步缺一不可、前三步是否也算道歉，正文未明确。",
    "updated_at（2022-06-18）晚于 published_at（2021-01-19），语料未给出修改内容，版本差异待核。",
    "brief 在语料中被截断（止于「……你就并不真的」），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "要清楚的定义你要道歉的事项——是为具体什么事情、什么情节、什么行为道歉。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "你也通过将这行为承认为一个错误而定义了你的道义。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "如果你并不在乎它是不是再次发生，你就并不真的认为这是个错误。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "它是可以以合理的成本来降低发生概率的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "对此只能表示遗憾、表示同情，不能表示歉意。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "为这类你根本管控不了的东西道歉，是一种会招来诅咒的傲慢。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "比如，你就不能为地震道歉。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "通不过这几条的检测，意味着你还没想明白。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "没想明白就是没想明白，不要装明白。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "没想明白要接着想，不要以想不明白为由拖着", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "而且会把本来并不见得要紧的价值观碰撞升级到致命的、关乎于人格和尊重的根本原则的高度", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "在对方心里，这是足以判关系死刑的重罪。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "父母那样将就了一辈子，是因为父母那个年代不将就很难。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "经济繁荣的价值何在？就在于不必那样将就。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "你要解释你是基于什么样的规则、什么样的逻辑，认定这件事是错的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "仅仅只是说这是错的，但是不解释或者不能解释这为什么是错的", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "这并不是道歉，而是一种敷衍和侮辱。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "这显然不会导致关系的修复，而只会进一步的破坏关系。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P027", "quote": "你实际上是在袒露你的价值观的自省和变迁。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P028", "quote": "背后都不会是什么“不小心”，而追根到底都是某种价值观的变迁", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P029", "quote": "不是错在行为的结果让对方痛苦，而是错在驱使你那样做的动机存在逻辑的缺陷。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P030", "quote": "使得痛苦被救赎、被宽慰的，是痛苦本身的价值。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P031", "quote": "这痛苦我何止不拒绝，反而会是我的莫大荣幸。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P032", "quote": "道歉是一种有着难以置信的神奇力量的圣事。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P033", "quote": "那么这痛苦不但会消解，反而会升华为对方极大的幸福。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P034", "quote": "你们的关系何止可以“修复”，还比之前更要坚固。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P035", "quote": "而是你真的因此有所成长和完善。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P036", "quote": "道歉根本就不是出于抚慰自己受伤心灵的需要", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "其实是出于对你的价值观缺陷的极端忧虑。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "更在暗自害怕最后证实唯有离开你是唯一剩下的选择。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P038", "quote": "那么剩下的唯一的选择就只能是离开了。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P040", "quote": "“爱”就不过是用来榨取内啡肽的罂粟而已。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P041", "quote": "吸毒没有好结果。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P043", "quote": "其实你不需要真的正确，你需要的是真诚。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P044", "quote": "真诚的笨拙所致的错误，是正确的错误。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P044", "quote": "正确的错误，是通向真理的最短道路。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P045", "quote": "你并不能保证真诚的结果不是一种谬误", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P046", "quote": "它同样可能导致关系的终结。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P047", "quote": "自以为表演一个讨人喜欢的版本可以带来更好的结局本身是一种最大的幻觉。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P048", "quote": "你从大众媒体上看到的“女生吃这一套”/“男生都喜欢xx”就算是真的，也根本不意味着对你面前这人有效。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P061", "quote": "保持真诚，收获就是你该收获的、错过的就是你该错过的", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P062", "quote": "你最终一定会获得踏实的宁静。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P063", "quote": "这份踏实的宁静，是世界上最性感的东西，是魅力源泉。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P066", "quote": "给出降低同样事件发生的概率的具体措施。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P067", "quote": "就是说“这件事不会再发生了（It won’t happen again）”这种蠢话。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P068", "quote": "人改正的过程之漫长、反复之多，不下于一次精神的长征。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P069", "quote": "并且未必能在死前真正到达终点。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P073", "quote": "那么说“不会再发生”不但不会收到什么奇效，反而要构成冒犯和伤害。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P075", "quote": "提出可行方案的难度也大为降低了。前者实际上根本就是不可行的。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P077", "quote": "在这个“降低概率计划”的可操作性、费效比和可检验性上都会最直观的体现出来。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P078", "quote": "拿出这样一个计划，比任何甜言蜜语都更直接。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P081", "quote": "全备的道歉，需要献祭。", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P082", "quote": "这些仍然只不过是话语罢了，这里面没有实实在在的痛苦和损失。", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P083", "quote": "这些痛苦与损失不应该影响健康，但必须实实在在，无可作伪。", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P084", "quote": "例如连续一周每天面壁一小时；例如斋戒一个月；例如禁足半个月；例如自请扣除酬劳。", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P085", "quote": "绝不给自己留任何“将道歉作为逃脱应有惩罚的机会”的余地。", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P086", "quote": "人就是在客观上教导自己只要会道歉，就可以逃脱惩罚。", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P087", "quote": "人很容易练成“道歉艺术家”，反而走上了一条更大的邪道了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际伦理与关系修复", "道德哲学／价值观", "沟通方法"],
   "issue_candidates": ["如何定义道歉事项", "道歉是否需解释错误逻辑", "「不会再发生」的承诺问题", "道歉中的献祭与自我惩罚"],
   "text_function_candidates": ["答疑", "方法指南", "训诫／劝诫", "论辩"],
   "object_candidates": ["提问者（泛问者）", "父母辈（作为对照）", "大众媒体说法（被质疑对象）"],
   "working_keywords": ["道歉", "献祭", "正确的错误", "价值观的变迁", "天意", "圣事", "降低概率计划", "道歉艺术家"]
  },
  "notes": "无图片节点。含 4 个 heading（P001/P022/P066/P081），即四步结构。C016 中「我何止不拒绝」为作者第一人称自陈（在假设句内），按 author_qualified/hypothetical 处理；P039 人称切换已在 unresolved_questions 登记。brief 在语料中被截断，仅作导航。updated_at(2022-06-18) 晚于 published_at(2021-01-19)，修改内容未给出。"
 },
 "ff22fff4": {
  "analysis": {
   "question_context": "提问者问「有哪些看似聪明，实则很傻的行为？」。作者给出一个具体答案：把智力资源用在从别人话里找漏洞而不是找合理可用之处，即「小聪明，大愚蠢」；全文不讨论其他候选行为，属举例式答疑。提问者只提供问题，未表达立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出答案并设问「为什么呢」：把智力资源用于从别人话里找漏洞、而非找合理可用之处，就是小聪明、大愚蠢。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "理由：表达有成本；完备、精确、简洁存在综合极限，实践中常优先简洁而牺牲完备与精确；简洁省下的时间成本是直接收益，不完备不精确可由筛选接收人弥补。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "推论：善于帮他人正面补完模糊空间者是宝贵资产、「生命延长者」，效费比远超常人；而人可有效管理的密切互动关系常不到十人，座位上的人多节省表达成本关系到一生总效能与生命总量。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "对照与贬评：朝正面努力尚嫌不够，朝负面努力更甚；靠「挖错」榨取优越感者是掠夺他人生命、满足虚荣毒瘾，并以反问类比魔鬼，称为无可救药的积重难返。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "后果预测：明白人一般不苦口婆心帮你改正，而选择社交处决（不雇佣、不交易、不来往、避免认识）；有事业者对此极为敏感，不应低估其眼光。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020"], "summary": "收束：这条路通向人憎狗嫌、众叛亲离的绝境与重度抑郁；以「什么叫小聪明，大愚蠢？看明白了吗？」作结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把智力资源投入在怎么从别人的话里找到漏洞，而不是找到其合理可用之处，就是所谓的小聪明、大愚蠢。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何人的表达都是有成本的。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "完备、精确和简洁存在一个综合的极限——要完备、要精确就难以简洁；实践中人们往往最优先考虑简洁，而牺牲完备和精确。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "简洁所节省的时间成本是直接收益，其造成的不完备、不精确问题可以通过筛选接收人弥补。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越善于准确帮助他人正面补完模糊空间的人，对他人而言越是宝贵的资产，本质上成了「生命延长者」，效费比远超一般人。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "一个人可以有效管理的密切互动关系的数量非常有限，常常不到十人。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这十个座位上坐着的人多节省表达成本，直接关系到你一生能达到的总效能极限，关系到你生命的总量。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把才能用在「挖错」上榨取优越感并洋洋自得的人，实际上是在掠夺他人的生命、满足自己虚荣的毒瘾；作者以反问把它与魔鬼所为相类比。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "明白人一般不会苦口婆心帮你改正，而选择直接社交处决——把你从生活环境里清除掉（不雇佣、不交易、不来往或直接避免认识）。", "evidence": ["E12", "E13", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能打拼出事业、决定你命运的人对这种问题的敏感性，最好不要有丝毫低估；他们若连这点眼光都没有，哪有前途可言。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这条路直接通向人憎狗嫌、众叛亲离的绝境，通向九死一生的重度抑郁。", "evidence": ["E15", "E16"]}
   ],
   "argument_steps": [
    "直接给出答案：挖错而非找可用之处＝小聪明、大愚蠢（P001）",
    "设问「为什么呢」引出理由（P002）",
    "理由一：表达有成本，简洁与完备／精确存在权衡（P003-P004）",
    "理由二：简洁的收益与代价可通过筛选接收人处理（P005）",
    "推论：帮他人补完模糊空间者成为宝贵资产与「生命延长者」（P006）",
    "推论：密切关系席位有限（常不到十人），席位质量关系生命总量（P007-P008）",
    "对照：正面努力尚不足，负面「挖错」是掠夺他人生命（P009-P013）",
    "后果：社交处决与被决定命运者的敏感（P014-P017）",
    "结论：绝境与重度抑郁；反问收束（P018-P020）"
   ],
   "concept_usage": [
    {"term": "小聪明，大愚蠢", "meaning": "把智力资源用于从他人话语中找漏洞，而非找合理可用之处", "evidence": "P001", "ambiguity": "未区分「指出真错误」与「挖错」，边界未说明"},
    {"term": "表达成本", "meaning": "表达所耗时间与篇幅，是可被他人节省或浪费的成本", "evidence": "P003", "ambiguity": "未量化，也未说明如何测量"},
    {"term": "生命延长者", "meaning": "能准确帮他人正面补完模糊空间，从而替他人节省表达时间的人", "evidence": "P006", "ambiguity": "为比喻性命名，未给判定标准"},
    {"term": "十个座位／密切互动关系", "meaning": "一个人可有效管理的密切互动关系上限（常常不到十人）", "evidence": "P007", "ambiguity": "数字为经验估计，来源未说明"},
    {"term": "社交处决", "meaning": "不雇佣、不交易、不来往或直接避免认识，把人从生活环境清除", "evidence": "P014", "ambiguity": "作者自称的表述，未说明是否指特定群体行为"}
   ],
   "examples_and_targets": [
    "「挖错」者（被批评对象，未指名）：作者以反问与「魔鬼」相类比（P011-P013）",
    "「生命延长者」「十个座位」「社交处决」：作者的比喻命名（P006、P007、P014）",
    "人憎狗嫌、众叛亲离、九死一生的重度抑郁：后果描述与修辞（P018-P019）",
    "决定你命运的人（有事业者）：作者作为判断依据的群体，未指名（P017）"
   ],
   "conditions": [
    "程度与频率限定：「往往最优先考虑简洁」「常常不到十人」「ta们一般都不会」（P004、P007、P014）",
    "对象限定：判断对象是「把智力资源投入在找漏洞」这一类行为，非所有批评（P001）",
    "后果为预测性表述：「这条路直接通向……绝境」「通向九死一生的重度抑郁」（P018、P019）",
    "前提：密切互动关系数量有限这一经验设定支撑全篇推论（P007-P008）"
   ],
   "rhetoric_and_tone": "以定义句开场，随后设问推进；强烈贬抑与道德化措辞（「小聪明，大愚蠢」「毒瘾」「卑鄙下流」「魔鬼」「社交处决」「人憎狗嫌」「肥」）；密集反问（P009、P010、P012、P016、P020）；把行为后果描述为必然绝境，语气训诫且断言化。",
   "unresolved_questions": [
    "P007「常常不到十人」这一数字的来源与依据未说明，属待外部核查的经验断言。",
    "「找漏洞」与「指出真实错误」的界线未说明；作者也未讨论正当批评是否会被此文一并否定。",
    "P013「无可救药的积重难返」等强烈评价的判据未给出。",
    "updated_at（2026-04-16）远晚于 published_at（2021-01-19），语料未给出修改内容，版本差异待核。",
    "brief 在语料中被截断（止于「简洁所节省的时」），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "把智力资源投入在怎么从别人的话里找到漏洞，而不是找到其合理可用之处，就是所谓的小聪明，大愚蠢。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "任何人的表达都是有成本的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "完备、精确和简洁存在一个综合的极限——要完备、要精确，就难以简洁。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "人们往往最优先考虑简洁，而牺牲完备和精确。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而造成的不完备、不精确问题，可以通过筛选接收人弥补。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "越是善于准确的帮助他人正面补完模糊空间的人，对于他人而言就越是宝贵的资产", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "ta本质上已经成了一名“生命延长者”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "一个人可以有效管理的密切互动关系的数量是非常有限的，常常不到十人。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "直接关系到你一生能达到的总效能极限，关系到你生命的总量。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "实际上是在掠夺他人的生命，满足自己虚荣的毒瘾。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这和魔鬼做的事情有何本质的区别？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "ta们一般都不会选择苦口婆心帮你改正，而是选择直接社交处决", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "意思是不雇佣、不交易、不来往，或者直接避免认识。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "对这种问题的敏感性你最好不要有丝毫的低估", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "这条路直接通向人憎狗嫌、众叛亲离的绝境，", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "通向九死一生的重度抑郁。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P013", "quote": "稍微明白一点的人无不洞若观火。", "relation": "context"},
    {"key": "E18", "paragraph_id": "P020", "quote": "所以，什么叫小聪明，大愚蠢？看明白了吗？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往与沟通", "认知与智力使用", "社会评价与声誉"],
   "issue_candidates": ["什么是看似聪明实则很傻的行为", "表达成本与简洁的权衡", "挑错与建设性反馈的界线"],
   "text_function_candidates": ["答疑", "评论／批评", "训诫／劝诫"],
   "object_candidates": ["「挖错」者（未指名）", "有事业者／决定你命运的人", "密切互动关系中的他人"],
   "working_keywords": ["小聪明，大愚蠢", "表达成本", "生命延长者", "社交处决", "挖错", "十个座位"]
  },
  "notes": "无图片节点，正文完整可读。全文为单一答案的展开，未讨论其他「看似聪明实则很傻」的行为。brief 在语料中被截断，仅作导航。updated_at(2026-04-16) 远晚于 published_at(2021-01-19)，修改内容未给出。"
 },
 "90628fd7": {
  "analysis": {
   "question_context": "提问者问「如何区别操控他人与发挥影响力？」。作者以「兽性／神性」「间接证据引诱／证据与逻辑」二分作答，并给出可操作判据：客观报道事实即影响力，明知故犯剪裁事实或把注意力从事实上引开即操纵。提问者只提问，未表达立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "给出定义：操纵诉诸兽性、靠间接证据引诱（如电影用音乐与镜头暗示有鬼）；影响诉诸神性、靠证据和逻辑。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "以爱因斯坦、牛顿的反问作例，说明影响只是指出并不存在的幻象并帮助人把有限人生专注到可行选择上，因而给人更大自由；操纵则剥夺自由及获得自由的能力。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "解释两者的心理机制：听从操纵是因为没有勇气面对现实，且会不断自我证明缺少勇气直至缩成一团；听从影响是因为鼓起勇气面对现实；人要做选择而选择太痛苦。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "行动要求与判据：注目事实、不听人言（人只是事实不称职的信使）；听事实决定命运；客观报道事实＝影响力，明知故犯剪裁事实／引开注意力＝操纵。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "操纵是诉诸人的兽性，靠的是用间接证据引诱。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "影响是诉诸人的神性，靠的是证据和逻辑。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "操纵类似电影里放恐怖气氛的音乐、用镜头和画面暗示有鬼。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "后者（影响）只是指出了那些根本不存在的幻象，并帮助人将有限的人生专注到可行的选择上，因而给了人更大的自由。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "前者（操纵）不但直接剥夺了人的自由，还不断剥夺人自由的能力。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "听从操纵是因为没有勇气面对现实；听从一次就更向自己证明缺少勇气；当对自己的勇气完全失去期待，人将会缩成一团，希望下辈子当块石头或一棵树，总之不要当人。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人要做选择，而选择太痛苦了。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "听从影响是因为人鼓起了勇气面对现实。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要注目在事实上，事实就是世界的话语；不要听人说什么，人只是事实不称职的信使。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "听事实在说什么，是事实在决定你的命运。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当你是在客观报道事实，你就是在发挥影响力。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当你是在明知故犯地剪裁事实，乃至故意想把人的注意力从事实上引开，你就是在操纵人。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "给出操纵的定义（诉诸兽性、间接证据引诱）与其类比（恐怖片手法）（P001-P002）",
    "给出影响的定义（诉诸神性、证据与逻辑）（P003）",
    "以爱因斯坦／牛顿的反问作例，说明影响指出幻象并扩大自由（P004-P005）",
    "对照：操纵剥夺自由与获取自由的能力（P006）",
    "心理机制：无勇气面对现实→自我证明→彻底失去期待；鼓起勇气→听从影响（P007-P009）",
    "行动要求：注目事实、不听人言（P010-P011）",
    "给出判据：客观报道事实＝影响；剪裁事实／引开注意＝操纵（P012-P013）"
   ],
   "concept_usage": [
    {"term": "操纵", "meaning": "诉诸兽性、以间接证据引诱；明知故犯剪裁事实或故意把注意力从事实上引开", "evidence": "P001", "ambiguity": "「间接证据引诱」与「故意剪裁」两条判据之间的关系未说明"},
    {"term": "影响", "meaning": "诉诸神性、靠证据和逻辑；客观报道事实", "evidence": "P003", "ambiguity": "未说明与「说服」的差别"},
    {"term": "兽性／神性", "meaning": "两种诉求层面的对立表述：兽性对应操纵，神性对应影响", "evidence": "P001", "ambiguity": "两词均未定义、未注明来源；与他篇用法是否一致不可跨篇推断"},
    {"term": "事实", "meaning": "世界的话语，决定命运者；人是事实不称职的信使", "evidence": "P010", "ambiguity": "未说明如何辨认「事实」与「剪裁」"},
    {"term": "自由", "meaning": "影响给人更大自由（专注到可行选择），操纵剥夺自由及获得自由的能力", "evidence": "P005", "ambiguity": "P005-P006 未界定「自由的能力」"}
   ],
   "examples_and_targets": [
    "电影中恐怖气氛的音乐、镜头与画面暗示有鬼：作者类比（P002）",
    "爱因斯坦与相对论、牛顿：作者以反问作例，反驳「影响＝操纵」的指责（P004）",
    "「希望下辈子当块石头，或者当一棵树」：修辞化描述（P007）",
    "「人只是事实不称职的信使」：比喻（P010）"
   ],
   "conditions": [
    "条件式判据：「当你是在客观报道事实……当你是在明知故犯的剪裁事实」（P012-P013）",
    "因果链为假设性推进：「因为，你听从前者，是因为你没有勇气面对现实」（P007）",
    "程度限定：「还不断的剥夺你自由的能力」为递进表述，未给时间尺度（P006）",
    "全文为短答，未讨论如何判定「明知故犯」以及误传与操纵的界线"
   ],
   "rhetoric_and_tone": "格言式短句与对偶定义（兽性／神性、间接证据／证据与逻辑）；以电影手法作通俗类比；用爱因斯坦、牛顿的反问施压；训诫式祈使句（「不要听人说什么」）；警句收束（「是事实在决定你的命运」）。整体语气断言、简峭。",
   "unresolved_questions": [
    "P005-P006 的「后者」「前者」与前文段落（P001 操纵、P003 影响、P004 举例）的对应关系存在指代歧义：本记录按「后者＝影响、前者＝操纵」理解，但 P005「指出了那些根本不存在的幻象」的主体归属仍可再核。",
    "「兽性」「神性」两词未给定义与来源，属待外部核查；与他篇中「神性」用法是否一致不得跨篇推断。",
    "如何判定「明知故犯」与「客观报道」，以及误传、无知与操纵的界线，正文未说明。",
    "updated_at（2021-05-15）晚于 published_at（2021-01-20），语料未给出修改内容，版本差异待核。",
    "brief 在语料中被截断（止于「它实际上通过帮助你将有限」），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "操纵是诉诸人的兽性，靠的是用间接证据引诱。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "影响是诉诸人的神性，靠的是证据和逻辑。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "类似电影里放恐怖气氛的音乐，用镜头和画面暗示有鬼。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "后者只是指出了那些根本不存在的幻象。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "通过帮助你将有限的人生专注到可行的选择上而给了你更大的自由。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "它不但直接剥夺了你的自由，还不断的剥夺你自由的能力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "你听从前者，是因为你没有勇气面对现实。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "你将会缩成一团，希望下辈子当块石头，或者当一棵树", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "因为人要做选择，而选择太痛苦了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "听从后者，是因为你鼓起了勇气面对现实。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "注目在事实上，事实就是世界的话语。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "不要听人说什么，人只是事实不称职的信使。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "听事实在说什么，是事实在决定你的命运。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "当你是在客观报道事实，你就是在发挥影响力。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "当你是在明知故犯的剪裁事实，乃至于故意想要把人的注意力从事实上引开，你就是在操纵人。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P004", "quote": "举个例子——你难道打算指责爱因斯坦用相对论操纵了你？或者牛顿操纵了你？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["传播与说服", "认识论／事实与价值", "心理与自由意志"],
   "issue_candidates": ["操纵与影响力的区别", "事实与剪裁的界线", "勇气与面对现实"],
   "text_function_candidates": ["答疑", "定义式说明", "论辩"],
   "object_candidates": ["爱因斯坦", "牛顿", "电影（类比素材）", "作为「信使」的人"],
   "working_keywords": ["操纵", "影响", "兽性", "神性", "间接证据", "事实", "剪裁事实", "自由"]
  },
  "notes": "无图片节点，正文完整可读。全文较短（13 段），为定义式短答。brief 在语料中被截断，仅作导航。P005-P006「前者／后者」指代歧义已登记在 unresolved_questions。updated_at(2021-05-15) 晚于 published_at(2021-01-20)，修改内容未给出。"
 },
 "c956094a": {
  "analysis": {
   "question_context": "提问者问「如何反驳『凭什么我们几代人的努力凭你寒窗苦读 10 余年就超越』？」。该说法只由提问字段转述，属被反驳观点；作者未按请求给出逐条反驳，而是先贬评其为「蠢」，再以「几十万代先祖」相对化「几代人」、以时代剧变说明无不可超越的壁垒，最后把「真正的财富」重新定义为肯为你舍生忘死的人并向对方反问。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "贬评并相对化该说法：只要是个活人谁不是几十万代人努力到如今；「几代人的努力」与先祖经历的豺狼虎豹、饥荒瘟疫、天灾人祸相比算不上什么，前看古人只是精神近视眼。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "后看来者：近现代每个世代都在重复「创造的物质财富超过了之前全部历史的总和」；很多人一家一年吃掉用掉的超过八九十年代一家全部家产，并设问这提示了什么。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "无论多优越（即便马云、马斯克、巴菲特等级）都没有积累起别人「一代绝不可能超越」的壁垒；超越者此刻可能在平平无奇的小镇揣着白煮蛋上学；因为时代如沸腾滚水，人海沉浮速度远超近代以前，一生经历的诸革命多出数个数量级。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "以「革命」的比喻式定义（孙悟空揪脖领子说「想得倒美」）与东海龙王／泥鳅说明其兴也勃、其亡也忽；区区几亿浮财、几个官职对后代是福是祸还难说，安全感却强到这样。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "结论：这只说明这家是暴发户且对ta的教育已经失败；失败若不被及时纠正，权势财富只会是灾难和诅咒；这些话是「新兴中产阶级」对拜物教的皈依狂热，意味着病已发作。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029"], "summary": "重新定义「真正的财富」：愿意为你舍生忘死的高尚的人；因贪财好色、贪恋权势、爱慕虚荣而「忠诚」者不算（绑匪骗子出价更高、只需找薄弱环节；出卖你的收益是否比不过效忠还难说）；只有富贵不能淫、贫贱不能移、威武不能屈且肯为你舍生忘死者才是，其义为犯颜直谏、鞠躬尽瘁、忍辱负重、涉险犯难，如孔明、魏征。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "反问收束：问「经营数代」之家夹袋里有几个这样的人；没有的话只是长得特别壮的肥猪；肥猪向瘦猪显示优越感、瘦猪又羡又恨齐声尖叫；以「唉。」作结。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「凭什么我们几代人的努力凭你寒窗苦读10余年就超越」这话说得真的是蠢。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要是个活人，谁都是几十万代人努力到如今，两个说话人才能在此刻碰得上。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「几代人的努力」与几十万代先祖所经历的豺狼虎豹、饥荒瘟疫、天灾人祸、沧海桑田相比算不上什么；前看古人，这只是精神近视眼。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者转述：近现代每一个世代都在重复一句话「创造的物质财富超过了之前全部历史的总和」。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "说得不好听一点，很多人现在一家人一年吃掉、用掉的，超过八九十年代一家人全部的家产。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "无论觉得自家现在多么优越——即便是马云、马斯克、巴菲特这个等级——在人类现在这个阶段也没有真的积累起什么别人「一代绝不可能超越」的壁垒。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "超越他们的人此刻完全可能在不知什么平平无奇的小镇，正在苦哈哈地每天揣着一颗白煮蛋上学读书。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在这个时代如同沸腾的滚水，人海沉浮的速度超过近代以前的人类不知多少倍；一个人一辈子经历的能源、交通、信息、生产方式、生活方式、知识、伦理、认知革命，比父母辈、祖父母辈多出不知多少数量级。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「革命」就是你以为位置坐得够稳了，明天就有不知从哪蹦出来的孙悟空揪住你的脖领子告诉你「想得倒美」；昨天的东海龙王，今天的泥鳅落网。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "区区几亿浮财、几个官职对后代到底是福是祸都还说不好，安全感却强到这样；这只说明这家是暴发户，而且对ta的教育已经失败了。", "evidence": ["E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果这个失败不被及时纠正，权势也罢、财富也罢，对人只会是一种灾难和诅咒，绝不是什么「终身利好消息」。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些话是一些还没见过厉害的「新兴中产阶级」对拜物教的皈依狂热；说这种话意味着病已经开始发作了。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的财富是愿意为你舍生忘死的高尚的人；因贪财、好色、贪恋权势、爱慕虚荣而「忠诚」的人是不算的。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以贪利而「忠诚」者为靠不住：绑匪和骗子出价会更高，且只需找到薄弱环节；作者反问出卖你可得到的收益是否真的永远比不过对你效忠，故这类人是正资产还是负资产还难说得很。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有富贵不能淫、贫贱不能移、威武不能屈的人，还要肯为你舍生忘死，这才是真正的财富。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「为你舍生忘死」不是指替你去杀人越货，而是指敢于犯颜直谏、甘于鞠躬尽瘁、能够忍辱负重、涉险犯难，如蜀之孔明、唐之魏征。", "evidence": ["E24", "E25"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问「经营数代」之家夹袋里有几个这样的人，没有的话「你只是长得特别壮的肥猪而已」。", "evidence": ["E26", "E27"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "肥猪们得意洋洋对瘦猪们显示优越感，瘦猪们又羡又恨、齐声尖叫。", "evidence": ["E28"]},
    {"claim_id": "C019", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的说法（仅由提问字段转述）：「凭什么我们几代人的努力凭你寒窗苦读 10 余年就超越」；作者以「你这“几代人的努力”」复述并以「这话说得真的是蠢」贬评之。", "evidence": ["E29", "E1"]}
   ],
   "argument_steps": [
    "开门贬评：「这话说得真的是蠢」（P001）",
    "相对化：人人皆有几十万代先祖的努力（P002）",
    "对比：几代人的努力 vs 先祖经历的灾难沧桑；精神近视眼（P003-P004）",
    "后看来者：世代重复的财富总量说法与一年开销超过旧日全部家产（P006-P007）",
    "设问过渡「这提示了什么？」（P008）",
    "论断：无「一代绝不可能超越」的壁垒，超越者可能在无名小镇（P009-P010）",
    "理由：时代如滚水，革命频仍，代际经验差数个数量级（P011-P013）",
    "定义「革命」并以龙王／泥鳅喻其兴亡（P014-P016）",
    "推论：财富官职未必是福，安全感过强说明是暴发户且教育失败（P017-P021）",
    "转向「真正的财富」：肯舍生忘死的高尚之人，并排除利诱型忠诚（P022-P029）",
    "反问收束：这样的人有几个？没有则是肥猪；以「唉。」结束（P030-P038）"
   ],
   "concept_usage": [
    {"term": "几代人的努力", "meaning": "被反驳说法中的家族积累；作者以「几十万代」的先祖努力将其相对化", "evidence": "P002", "ambiguity": "「几代」的范围未界定，作者未讨论家族积累的实际作用"},
    {"term": "壁垒", "meaning": "别人「一代绝不可能超越」的优越积累", "evidence": "P009", "ambiguity": "未说明壁垒是否可指财富以外的资源"},
    {"term": "革命", "meaning": "位置随时被取代的剧变（孙悟空揪脖领子的比喻式定义）", "evidence": "P015", "ambiguity": "定义以比喻给出，未界定时段与范围"},
    {"term": "真正的财富", "meaning": "富贵不能淫、贫贱不能移、威武不能屈且肯为你舍生忘死的人", "evidence": "P027", "ambiguity": "与通常「财富」用法不同，属作者重新定义"},
    {"term": "舍生忘死", "meaning": "犯颜直谏、鞠躬尽瘁、忍辱负重、涉险犯难，而非替主人杀人越货", "evidence": "P028", "ambiguity": "举例为历史人物，未给现代对应"},
    {"term": "暴发户／新兴中产阶级／拜物教", "meaning": "用以刻画说该话的家庭与群体及其价值取向", "evidence": "P019", "ambiguity": "三词均未给界定标准或指称范围"}
   ],
   "examples_and_targets": [
    "被反驳说法「凭什么我们几代人的努力凭你寒窗苦读 10 余年就超越」：由提问字段转述，属 opponent_view（P001、P003 复述）",
    "马云、马斯克、巴菲特：作者列举的优越等级（P009）",
    "孙悟空、东海龙王、泥鳅落网、沸腾的滚水：作者的比喻（P012、P015、P016）",
    "八九十年代一家人全部家产：作者用于对比的量化说法（P007）",
    "「创造的物质财富超过了之前全部历史的总和」：作者转述的世代说法，未注明出处（P006）",
    "绑匪和骗子：论证中的假想出价者（P024）",
    "蜀之孔明、唐之魏征：作者举的历史人物例证（P029）",
    "肥猪／瘦猪：结尾比喻，指优越感展示者与羡慕者（P035、P036）"
   ],
   "conditions": [
    "条件句：「如果这个失败不被及时的纠正」（P020）",
    "范围包含最顶层：「即便是马云、马斯克、巴菲特这个等级」（P009）",
    "或然性预测：「此刻完全可能在不知什么平平无奇的小镇」（P010）",
    "反问而非断言处：「出卖你可以得到的收益，真的永远比不过对你效忠吗？」（P025）",
    "限定「舍生忘死」的外延：「不是指替你去杀人越货，而是指……」（P028）",
    "程度词：「也难说得很」「都还说不好」表明作者对判断留有余地（P017、P026）"
   ],
   "rhetoric_and_tone": "开门即以「蠢」贬评；密集反问与设问（P002、P003、P008、P014、P025、P031-P034、P037）；比喻与典故密集（孙悟空、东海龙王／泥鳅、沸腾滚水、肥猪／瘦猪、豺狼虎豹、化用「富贵不能淫，贫贱不能移，威武不能屈」与「其兴也勃焉，其亡也忽焉」）；短句分行推进（「来，」「摸摸自己的夹袋，」「这样的人，」「你们有几个？」）；以讥讽的「肥猪／瘦猪」与一声「唉。」收尾。",
   "unresolved_questions": [
    "「几十万代」为修辞性数字，未给依据，属待外部核查。",
    "P006「创造的物质财富超过了之前全部历史的总和」未注明出处；P007「超过八九十年代一家人全部的家产」为事实断言；两者均需外部核查。",
    "提问者请求「如何反驳」，作者未给出逐条论证式反驳，而以贬评、相对化与反问代替；这是否回应了提问，可再讨论。",
    "P031-P034 为分行短句（「来，」「请问，你们家“经营数代”，」「摸摸自己的夹袋，」「这样的人，」「你们有几个？」），跨段拼接会破坏原结构，本记录未作拼接引用。",
    "「拜物教」「新兴中产阶级」未给定义或指称范围；「真正财富」的判定主体也未说明。",
    "updated_at（2026-02-25）远晚于 published_at（2021-01-22），语料未给出修改内容，版本差异待核。",
    "brief 在语料中被截断（止于「说实在的」），仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这话说得真的是蠢。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "只要是个活人，谁不是几十万代人努力到如今，俩说话人才能在此刻碰得上呢？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你这“几代人的努力”和这几十万代先祖所经历的豺狼虎豹、饥荒瘟疫、水深火热、天灾人祸、沧海桑田比起来，算个啥啊……", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "前看古人，这只不过是一种精神近视眼罢了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "近现代每一个世代都在重复一句话“创造的物质财富超过了之前全部历史的总和”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "很多人现在一家人一年吃掉、用掉的，超过八九十年代一家人全部的家产。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "也没有真的积累起什么别人“一代绝不可能超越”的壁垒来。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "即便是马云、马斯克、巴菲特这个等级", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "正在苦哈哈的每天揣着一颗白煮蛋上学读书。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "因为现在这个时代如同沸腾的滚水，人海沉浮的速度超过近代以前的人类不知道多少倍。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "比起你的父母辈、祖父母辈……不知多了多少数量级。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "明天就有不知从哪蹦出来的孙悟空，揪住你的脖领子告诉你“想得倒美”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "其兴也勃，其亡也忽。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "对后代到底是福是祸都还说不好，安全感就能强到这样。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "这家是暴发户，而且对ta的教育已经失败了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "对人只会是一种灾难和诅咒，绝不是什么“终身利好消息”。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "说这种话，意味着病已经开始发作了。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "真正的财富是愿意为你舍生忘死的高尚的人。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "因为贪财、因为好色、因为贪恋权势、因为爱慕虚荣而“忠诚”的人是不算的。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P024", "quote": "因为第一，绑匪和骗子们出价会更高。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P025", "quote": "出卖你可以得到的收益，真的永远比不过对你效忠吗？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "所以这类人到底是正资产还是负资产、是帮手还是凶手，还难说得很。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "只有富贵不能淫、贫贱不能移、威武不能屈的人，还要肯为你舍生忘死，这才是真正的财富。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P028", "quote": "而是指敢于犯颜直谏、甘于鞠躬尽瘁、能够忍辱负重、涉险犯难。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P029", "quote": "如蜀之孔明、唐之魏征。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P031", "quote": "请问，你们家“经营数代”，", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P035", "quote": "没有的话，你只是长得特别壮的肥猪而已。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P036", "quote": "肥猪们得意洋洋，对瘦猪们显示优越感", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P003", "quote": "你这“几代人的努力”", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会阶层与流动", "财富观与家族传承", "价值观批评"],
   "issue_candidates": ["几代人的积累与个人努力能否比较", "阶层壁垒是否存在", "何为真正的财富与忠诚"],
   "text_function_candidates": ["答疑", "反驳／论辩", "评论／批评", "讥讽式训诫"],
   "object_candidates": ["提问者转述的说法（几代人的努力）", "马云、马斯克、巴菲特", "新兴中产阶级／暴发户", "孔明、魏征", "肥猪／瘦猪（比喻）"],
   "working_keywords": ["几代人的努力", "壁垒", "革命", "真正的财富", "舍生忘死", "暴发户", "拜物教", "肥猪"]
  },
  "notes": "无图片节点，正文完整可读。被反驳说法仅来自提问字段，已按 opponent_view（attribution=opponent）处理，未归给作者。P031-P034 为分行短句，未跨段拼接引用。brief 在语料中被截断，仅作导航。updated_at(2026-02-25) 远晚于 published_at(2021-01-22)，修改内容未给出。"
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
