# -*- coding: utf-8 -*-
"""批次 r001-b0028 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0028.sessions.py            # 写 out/r001-b0028.out.jsonl
  python3 records/r001-b0028.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0028"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0028.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "c60c486a": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：游戏内无恶不作的人是否会比在游戏内尽量行善的人人品差？提问者把问题限定在游戏行为与人品的关系上。作者未直接回答游戏场景，而是转向“怎么评论人品差”，给出一套由轻到重的判断标准：先排除“谋生模式”这一评价层面，再谈取乐模式、道德投机主义、道德场景化，最后论及无耻与“不以为耻，反以为荣”的极恶，并把结论落到家族答集的回避法则上。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出全文问题——怎么评论人品差，并预告分条递进。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "第一条：取乐的模式可怕；明确把谋生模式排除在本次评价之外，并声明不等于替“身不由己”开脱。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "取乐在生存需求之上、没有迫不得已的借口，故以恶为乐可作说明问题的指标；列举杀生、成瘾物、霸凌、见利忘义等取乐方式，并称其为危险信号、易发展成反社会人格。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "第二条：道德投机主义——是否遵守道德与法则取决于会不会被抓、代价是否得不偿失。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "以中国法则“君子不欺暗室”为对照。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "第三条：道德场景化——对道德议题无确切立场，随情境与利益切换并真诚表演；单看一幕无懈可击，两幕并置则以“具体问题具体分析”与“傻”作解，而每次“傻”都落在占便宜的位置上；作者将其与道德虚无主义区分开。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "上述几条都算人品差，但不算差到极点：几乎人人或多或少有之，且表现隐蔽、需要极强的自省能力才能看见。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024"], "summary": "极恶是无耻：明知故犯而不觉羞耻、不惭愧、无焦虑，因而没有修正驱动力，作者称这已可诊断为反社会人格，遇到必须果断回避。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P025"], "summary": "在无耻之上还有一类“王中之王”——不以为耻反以为荣。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030"], "summary": "行动建议：家训必须包含回避法则；用相关话题试探“反正没人管”式回答来识别；发现一个剔除一个；但不是全然隔绝，而是不接纳为家族成员。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P031"], "summary": "结尾残留平台/文集标签“家族答集”。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "评价人品差应聚焦取乐的模式，而不去评价谋生的模式；作者声明这一搁置不等于认为使上“身不由己”的理由就无罪无恶。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "取乐在生存需求之上、没有迫不得已的借口，因此以恶为乐可作为说明人品问题的指标；这类取乐方式是危险信号，容易发展成反社会人格。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道德投机主义指是否遵守道德、契约与法则全看会不会被抓住、代价是否得不偿失。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "道德场景化的人对道德议题没有确切立场，按情境与自身利益切换立场，且能演得真诚；其“傻”总是落在占便宜的位置上。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "上述几条都算人品差，但不算差到极点：几乎人人都或多或少有，且表现隐蔽，需要坚决的自省决心与长期积累的自省能力才看得见。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极恶是无耻：明知、故犯而不觉羞耻、不惭愧、无不适与焦虑，因而毫无修正驱动力；作者称这已可非常有效地诊断为反社会人格。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对这类人不可以接纳为家族成员，家训必须包含这条回避法则；但不是不可以打交道。", "evidence": ["E13", "E14"]},
    {"claim_id": "C008", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "文中引述中国法则“君子不欺暗室”作为正面对照：不因没人看见就推翻准则，不因可逃脱惩罚就去作恶。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "以设问开篇“怎么评论人品差？”并声明按条递进（P001—P002）。",
    "界定评价范围：只评取乐、暂不评谋生，并补充该搁置不等于认可“身不由己”无罪（P003—P005）。",
    "提出理由：取乐在生存需求之上、无迫不得已的借口，故“以恶为乐”可作指标（P006）。",
    "举例杀生、成瘾物、霸凌、见利忘义等取乐（P007），断言其为危险信号、易发展成反社会人格（P008）。",
    "第二条：定义道德投机主义——按被抓概率与代价计算是否守则（P009—P010），以“这里又没有人管”等为例（P011）。",
    "引中国法则“君子不欺暗室”作正面对照（P012）。",
    "第三条：定义道德场景化——无确切立场、随情境与利益真切切换（P013—P014）；以“单看一幕无懈可击”与“两幕并置”说明（P015—P016）；点出其“傻”总落在占便宜处（P017）；与道德虚无主义作区分（P018）。",
    "让步与限定：这几点算人品差但不到极点，因为人人多少有之、且难以看见（P019—P021）。",
    "给出极恶标准：无耻，即明知故犯而无羞耻、无焦虑、无修正驱动力，可诊断为反社会人格（P022—P023），并警告不回避形同玩火（P024）。",
    "再上一层：不以为耻反以为荣者（P025）。",
    "落到行动：家训须含回避法则（P026）、用“反正没人管”式回答识别（P027）、发现一个剔除一个（P028），但非全然隔绝，而是不接纳为家族成员（P029—P030）。"
   ],
   "concept_usage": [
    {"term": "人品差", "meaning": "本篇以三条可观察的行为模式（取乐方式可怕、道德投机主义、道德场景化）作为人品差的指标，并把更严重的“无耻”“不以为耻反以为荣”分出层级。", "evidence": "P019", "ambiguity": "未给出统一的人品定义，只按层级列举；也未回答提问中的游戏场景。"},
    {"term": "取乐", "meaning": "人在生存需求之上、没有“为了生存迫不得已”借口的活动领域。", "evidence": "P006", "ambiguity": "与谋生行为的界线由作者划分，未给出具体判准。"},
    {"term": "道德投机主义", "meaning": "是否遵守道德原则、契约或法则，全看会不会被抓住、抓住是否付出得不偿失的代价。", "evidence": "P010", "ambiguity": "作者补充“有时候只是假装计算”，即当事人的计算可能是妄断，未展开区分。"},
    {"term": "道德场景化／道德情境化", "meaning": "对道德议题无确切立场，立场随情境与自身利益切换；作者与“道德虚无主义”区分，称后者只是道德已死亡，前者还要把道德尸体做成木偶演戏赚钱。", "evidence": "P018", "ambiguity": "P013 作“道德场景化”、P018 作“道德情境化”，两种写法并存。"},
    {"term": "无耻", "meaning": "自己已明知、已经故犯，却不觉得羞耻、不惭愧、无不适与焦虑，因而毫无修正驱动力。", "evidence": "P023", "ambiguity": "作者称这“可以非常有效的”诊断为反社会人格，未说明依据何种诊断标准。"},
    {"term": "回避法则", "meaning": "家训中必须包含的条目：识别无耻之徒，避免将其纳入家族。", "evidence": "P026", "ambiguity": "适用范围限定在“有意建立自己家族的人”，未展开到其他组织。"}
   ],
   "examples_and_targets": [
    "提问者的游戏情境（游戏内无恶不作 vs 行善）——作者未回答，转向一般性评论（P001）。",
    "“好以杀生取乐，好以成瘾物取乐，好以霸凌取乐，好以见利忘义取乐”——作者列举的取乐方式（P007）。",
    "“这里又没有人管”“抓到了也无非重新注册一个新号”——作者作为投机主义道德观体现的引例（P011）。",
    "“君子不欺暗室”——作者引用的中国法则，作为正面对照（P012）。",
    "“对啊，有什么问题吗？具体问题具体分析嘛。”——作者虚拟场景化者被两幕并置时的反应（P016）。",
    "“反正没人管”“这样的人多的是，不多我一个”——作者建议用来试探的“神回复”样例（P027）。",
    "家族／家训／家族答集——作者的行动落点与文集标签（P026、P031）。"
   ],
   "conditions": [
    "全文只评“取乐”，暂不评“谋生”（P004、P005）。",
    "搁置谋生模式“不等于”使上该理由就肯定算无罪无恶（P004）。",
    "这些特征“是个人就或多或少有这么一点，大概只是程度不同”（P021）。",
    "看得见这些问题需要坚决的自省决心与长期积累的自省能力（P021）。",
    "无耻要到“自己已经明知，已经故犯”的程度才算（P023）。",
    "回避法则的适用对象是“有意建立自己家族的人”（P026）。",
    "不是不可以打交道，而是不可以接纳为家族成员（P029、P030）。"
   ],
   "rhetoric_and_tone": "问答式训诫口吻，反问与设问密集（“那什么是极恶呢？”“为啥呢？”）；用递进编号组织（第一条、第二条、第三条）；多处插入自我限定与澄清（“注意，我不是在说……”“我没说……”“我们暂且不谈”）；比喻强烈，如“如利刃一般的危险因素”“把道德的尸体拿来做成木偶”“形同把脑袋别在裤腰带里玩火”“王中之王”；以“家族答集”收尾并给出可操作的剔除法则。",
   "unresolved_questions": [
    "提问所问的“游戏内无恶不作是否比行善者人品差”在正文中没有被直接回答，只被转成一般性人品评论。",
    "“反社会人格”的诊断依据与标准，本文未说明，属待外部核查。",
    "“君子不欺暗室”的出处与原文表述，本文未注明。",
    "文末“家族答集”标签为平台/文集残留，非正文论述。",
    "P031 为 lexical 未覆盖片段（骨架 divergence=true），已按正文原样保留。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "第一条，取乐的模式可怕。注意，我不是在说谋生的模式可怕，我是说ta取乐的模式可怕。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "我没说使上这个理由就肯定算无罪无恶了，我只是说这个层面我们暂时不予评价。", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P006", "quote": "取乐，没有“这是为了生存迫不得已”的借口。所以，“取乐的方式可怕”——也就是以恶为乐——就是一种可以说明问题的指标。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "这些人身上存在着如利刃一般的危险因素，很容易发展成反社会人格。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "ta是否遵守，全看会不会被抓住，抓住是不是会付出得不偿失的代价。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "这样的心态，就是投机主义道德观的体现。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "就是他对一个道德议题没有确切立场。采取哪个立场，全看情境，看自己的利益。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "只是，“巧合”的是，他每次“傻”都“傻”在很占便宜的位置上了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "这几条，都可以不折不扣的算人品差。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P021", "quote": "因为是个人就或多或少有这么一点，大概只是程度不同。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P023", "quote": "那就是无耻——自己已经明知，已经故犯，但不觉得羞耻，不惭愧，没有不适感，没有焦虑感，于是毫无修正的驱动力。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "这已经可以非常有效的将这人诊断为“反社会人格”了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "你的家训里必须包含这一条回避法则——要高度注意识别无耻之徒，避免误把ta们纳入自己的家族之中。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P030", "quote": "而是不可以将ta们接纳为你的家族成员。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P012", "quote": "叫做“君子不欺暗室”——不因为没人看得见，就推翻自己的准则；不因为可以逃脱惩罚，就去作恶。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德哲学", "人格与行为分析", "家族与家训"],
   "issue_candidates": ["人品评判标准", "以恶为乐", "道德投机主义", "道德相对化/场景化", "反社会人格识别与回避"],
   "text_function_candidates": ["答疑", "论辩", "经验总结", "训诫"],
   "object_candidates": ["游戏玩家（提问语境）", "反社会人格者", "家族成员", "家族答集"],
   "working_keywords": ["人品差", "取乐", "谋生", "道德投机主义", "君子不欺暗室", "道德场景化", "道德情境化", "无耻", "反社会人格", "回避法则", "家族答集"]
  },
  "notes": "正文最后一段 P031 为平台/文集标签“家族答集”，属结构残留，未计入作者论述。问答体裁：提问问的是游戏内行为与人品的关系，作者未直接回应，改以一般性条目作答，已在 unresolved_questions 登记。"
 },
 "3b6dc172": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：为什么电影中的巨兽不可能存在？提问者自带“不可能存在”的预设。作者没有顺着该预设回答，而是先提出“单论尺寸的话，是可以存在的”，随后给出一套假设性的构造设想，并把难点从尺寸转到自卫手段。全文是短篇设想式推演，不是对现实生物或某部电影的实证考察。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回应提问预设：仅就尺寸而言，是可以存在的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "给出浮力机制设想：生物把自体排出的甲烷存入巨大皮囊成为“甲烷气球怪”，由此可达十层楼高而不必担心骨骼支撑与心脏血压；并引《星际争霸》的 Overlord 为典型例子。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "指出真正的问题是自卫手段，并给出最经典的自卫设想：携带黄蜂式共生生物群落，自身充当航空母舰。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者把命题限定在“单论尺寸”这一层面：仅就尺寸而言，巨兽是可以存在的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "设想某种生物把自体排出的甲烷有效存储在巨大皮囊中，即可成为“甲烷气球怪”，从而不受骨骼承重与心脏血压的限制。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "尺寸不成问题之后，巨兽真正的问题是需要找到有效的自卫手段，例如喷火；最经典的自卫手段是自带类似黄蜂的共生生物群落，自身担当航空母舰的角色。", "evidence": ["E3", "E4"]}
   ],
   "argument_steps": [
    "先修正提问前提：不是尺寸不行，“单论尺寸的话，是可以存在的”（P001）。",
    "给出浮力机制设想：甲烷存于皮囊形成“气球怪”，于是骨骼与心脏血压都不再是限制（P002—P003）。",
    "举《星际争霸》的 Overlord 作为这一设想的典型例子（P003）。",
    "把问题从尺寸转到自卫，并举喷火等可能手段（P004）。",
    "给出最经典的自卫方案：与类似黄蜂的共生生物群落配合，本体担任航空母舰（P005）。"
   ],
   "concept_usage": [
    {"term": "尺寸", "meaning": "本文特指生物体量/高度这一单一维度；作者用“单论尺寸”把它与其他可行性条件（承重、血压、自卫）切开。", "evidence": "P001", "ambiguity": "未给出可存在尺寸的上限数值，也未讨论浮力、代谢等其他物理约束。"},
    {"term": "甲烷气球怪", "meaning": "作者设想的生物形态：以自体排出的甲烷充入巨大皮囊获得浮力，从而支撑巨大体量。", "evidence": "P002", "ambiguity": "甲烷来源、皮囊材料与密封性等本文未说明。"},
    {"term": "共生生物群落", "meaning": "作者设想中巨兽携带的、类似黄蜂的群体，用于自卫；巨兽本体承担航空母舰式平台角色。", "evidence": "P005", "ambiguity": "共生关系的维持方式与能量来源本文未说明。"}
   ],
   "examples_and_targets": [
    "《星际争霸》中的 Overlord——作者举为“甲烷气球怪”设想的典型例子，属虚构作品引用（P003）。",
    "黄蜂——作者用作共生生物群落的类比对象（P005）。",
    "航空母舰——作者用作巨兽角色的比喻（P005）。",
    "喷火——作者举的自卫手段之一（P004）。"
   ],
   "conditions": [
    "结论限定在“单论尺寸”这一前提下（P001）。",
    "方案以“某种生物可以把自体排出的甲烷有效的存储在自己巨大的皮囊里”为假设条件（P002）。",
    "十层楼高与“不必担心骨骼/血压”依赖于上述浮力设想（P003）。",
    "自卫手段以“找到某种有效的手段”为前提，作者用“比如喷火什么的”表示举例而非定论（P004）。"
   ],
   "rhetoric_and_tone": "简短、口语化的设想式答疑，语气轻松；用“是可以存在的”“那就想要十层楼高都可以”的让步式说法修正提问预设；以“典型例子就是星际里的Overlord了”“最经典的自卫手段应该是……”等带推测色彩的说法展开，未给数据或引文。",
   "unresolved_questions": [
    "本文未说明“电影中的巨兽”具体指哪部作品或哪类形象。",
    "甲烷气球怪的浮力、代谢、皮囊材料、甲烷来源等物理细节本文未说明，也无计算或数据。",
    "《星际争霸》Overlord 的设定细节本文未展开，属虚构作品，需外部核查。",
    "对提问中“不可能存在”的原由（如平方立方定律之类）本文未说明，也未逐一回应。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "单论尺寸的话，是可以存在的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "比如某种生物可以把自体排出的甲烷有效的存储在自己巨大的皮囊里，就可以成为一个“甲烷气球怪”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "它的问题是需要找到某种有效的手段来达成自卫。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "最经典的自卫手段应该是自带很多类似黄蜂一样的共生生物群落，自己担当航空母舰的角色。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["科普/假设推演", "生物学与力学设想", "游戏设定讨论"],
   "issue_candidates": ["巨兽的尺寸可行性", "浮力替代骨骼承重", "巨兽的自卫方式", "电影设定的现实性"],
   "text_function_candidates": ["答疑", "假设推演", "科幻设定讨论"],
   "object_candidates": ["电影中的巨兽", "甲烷气球怪", "《星际争霸》Overlord", "黄蜂", "航空母舰"],
   "working_keywords": ["尺寸", "甲烷", "皮囊", "甲烷气球怪", "骨骼", "血压", "自卫", "共生生物群落", "航空母舰", "Overlord"]
  },
  "notes": "本篇为极短篇假设推演，正文 196 字；作者用“是可以存在的”“应该”等限定与推测语气，未给数据与出处。引《星际争霸》Overlord 属虚构作品，未展开设定细节，已在 unresolved_questions 登记。"
 },
 "95a97047": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：我出钱你出力，为什么学生就得更尊敬老师？提问者以“出钱／出力”的交易关系为前提质疑尊师的必要性。作者不接受这个前提，先立“天、地、君、亲、师”五者都需敬畏，再逐一解释地（自然规律）、天（可能性）、君（自己选的领导者）、亲（天地合意替你作的第一个选择），由此推出师的位置，并把“不敬师”重新解释为老师背弃“为师的资格”之后的“神人伦理”问题；最后给出“尊敬”的技术性定义（补强／补弱）与“学生必须尊敬老师”的结论，文末标“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "立论：天、地、君、亲、师，人一生必须对这五样有足够敬畏。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "释“地”：地指自然规律与世界的恒常法则，不敬规律必遭失败，故不能不敬自然规律。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "释“天”：天指天意，即神秘莫测的可能性；不要凭自信断言可能与不可能，因为世界不由任何人决定，不能不敬畏可能性。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "天地相合决定了很多必须接受的事；可以寻求改变，但必须先接受起点；把质问“凭什么是我”视为不敬天地，以残疾复健、装假肢为例，并称这种不敬会招致第二轮打击与社会性绝境。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "释“君”：君指自己选的领导者；因是自愿选择，服从即对自己的选择负责；可退出、可收回意愿，但不可在未退出前离弃，不敬所选之君实质上是不敬自己。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "释“亲”：天地合意为你作的第一个选择就是双亲；无论好坏都是发到手里的牌；不能不敬天地，也就不能不敬亲与父母代作的选择。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "推出“师”：天地亲合意为你选择了一个君，这个君就是师；师不是好为人师者自选的，而是你的选择、父母意愿与客观限制机遇共同决定的结果。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030"], "summary": "要害：可以另作选择，但不可把“错误教导”的责任放在老师身上；理由是没有任何人在任何时刻任何事上完全正确（人无察觉绝对真相、无绝对准确表达、无绝对正确理解的能力），故本质上没人在教正确的东西。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036", "P037"], "summary": "若不赦免老师的“错误教导”，就没有够资格的人敢当老师；为师的基本资格是“我教的注定全是错的”的自觉，所教不是真理而是有质量的错误；只要学“正确的东西”者没有做学生的资格。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042"], "summary": "对有志成师者的告诫：违此条不要惊讶将来被“欺师灭祖”；无选择不怪你，有选择仍接纳则无资格；唯一例外是定意牺牲、愿背负一切冤屈的纯然的爱，且要记得徒弟将来必要怨你。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050"], "summary": "对建家族者的额外提醒：择师要遵循此原则，不看文凭门派光环；知者能者不足为师，只有觉者可以为师；真正的老师所传的自觉与嗅觉是瑰宝，名师常传递傲慢与虚荣，家族覆灭常因几个关键传人踏错红线。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058"], "summary": "站稳择师后可见：这师不难敬；学生的不敬多起于老师自居绝对真理、闯入人潜意识中为全知全能者留出的禁地，故这不是师生伦理问题而是“神人伦理”问题；有自觉的老师被不敬的概率大降。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063"], "summary": "够资格的老师面前，学生不会想起“我给了钱凭什么还要尊敬你”；理由一是这种老师举世奇珍，理由二是其学费多半靠近可开范围的下限；具体原因留待下回分解。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068", "P069"], "summary": "转入正题：如何确切定义尊敬（respect）；因语言与表达的天然局限，听话者必须对模糊处作猜测性补足，要害在于补足的方向。", "role": "definition"},
    {"unit_id": "U015", "paragraph_refs": ["P070", "P071", "P072", "P073"], "summary": "补弱的一方把你的话补成更虚弱愚蠢的版本，以证明自己更明智，只在荒谬时才稍收敛，这叫不尊敬；另一些人则首先向强处补足。", "role": "definition"},
    {"unit_id": "U016", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084"], "summary": "按弱假定还是强假定接话可判断对方是否有足够敬畏；敬畏不是把人当神膜拜，而是尊重神／自然的无限能力；对可能性保持敬畏者先假定强版本，除非有明确证据排除，甚至证据也不一定能排除；尊敬即对世界无限可能的敬畏，是一种不分对象、不计条件、一视同仁的习惯。", "role": "definition"},
    {"unit_id": "U017", "paragraph_refs": ["P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092"], "summary": "真教师看重求学者是否足够尊敬：即使不谈品德，仅就沟通效率与有限生命的运用而言，习惯补弱者绝对劣于习惯补强者；最优方案往往唯一，劣化版本无限；需要你花时间排除其劣化版本才能对话的对象应予排除，这不是歧视而是珍惜生命；只有补强的人才有资格从教学中获得成效，所以学生必须尊敬老师。", "role": "conclusion"},
    {"unit_id": "U018", "paragraph_refs": ["P093"], "summary": "文末标注“（未完，待续）”。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "天、地、君、亲、师这五样，人一生必须有足够的敬畏。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“地”指自然规律与世界的恒常法则，有规律的东西硬“不信邪”只会失败，故不能不敬。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“天”指天意，通俗说指神秘莫测的可能性；不要凭自信断言可能与不可能，因为世界不由任何人决定。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "天地相合决定的事必须接受，但可以寻求改变——改变须以接受起点为前提，这样不算不敬天地；质问老天“凭什么是我”才是。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“君”指自己选的领导者；因其为自愿选择，服从即对自己的选择负责，而不敬所选之君实质上是不敬自己。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "天地合意为你作的第一个选择就是替你选择双亲，故不能不敬亲，也就不能不敬父母在你尚不能自理时替你作的选择。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母为你选择的那个“君”就是“师”，这就是不能不敬师的理由；师不是好为人师者自选的，而是你自己的选择与命运限制共同决定的。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可以另作选择，但不可以把“错误教导”的责任放在老师身上——因为没有任何人在任何时刻任何事上完全正确，本质上没人在教正确的东西。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为师的基本资格就是“我教的注定全是错的”的自觉；所教不是真理而是“有质量的错误”，这是人类能给予人类的最好的东西。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "只要学“正确的东西”且认为教错就对不起自己的尊敬，就没有做学生的资格；为师者若无选择接纳这样的人不怪他，有选择而接纳则无资格；唯一例外是愿背负一切冤屈、定意牺牲去成全对方的爱。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为家族成员择师要不遗余力地遵循这一原则，不看文凭、门派与光环；知者、能者不足为师，只有觉者可以为师。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学生的不敬极大多数从老师自己背弃“为师的资格”开始：老师自居绝对真理便闯入人潜意识中为全知全能者留出的禁地，所以这不是师生伦理问题而是“神人伦理”问题。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "面对够资格的老师，学生大概根本不会想起“我给了钱凭什么还要尊敬你”，因为这种老师举世奇珍，且其学费多半靠近可开范围的下限。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "界定“尊敬”的可操作判据：听者对你的模糊表达是首先向弱处补足还是向强处补足；先向弱处补足的态度就叫做不尊敬。", "evidence": ["E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敬畏不是把人当神膜拜，而是审视一个人是否尊重神／自然的无限能力；对可能性保持敬畏者会先假定对方在表述强版本，除非有明确证据排除。", "evidence": ["E26", "E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓尊敬，即以尊重表达出的对世界的无限可能的敬畏；它是一种不分对象、不计条件、对一切对象一视同仁的习惯。", "evidence": ["E28", "E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个习惯补弱的人绝对劣于习惯补强的人；需要你花时间去除其构建的劣化版本才能获得新对话起点的对象，在你并非别无选择时绝对应予排除——“这不是歧视，这只是珍惜生命”。", "evidence": ["E30", "E31"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有补强的人，才有资格、有真实的可能从教学中获得成效，所以学生必须尊敬老师。", "evidence": ["E32", "E33"]}
   ],
   "argument_steps": [
    "立五敬：天、地、君、亲、师都必须有足够敬畏（P001—P002）。",
    "定义“地”＝自然规律与恒常法则，以万有引力与跳崖为例说明不敬必败（P003—P004）。",
    "定义“天”＝天意＝神秘莫测的可能性，禁止凭自信断言可能／不可能（P005—P006）。",
    "论天地相合：必须接受既定起点，但可在接受之后寻求改变；以残疾复健、装假肢为例；把质问“凭什么是我”判为不敬天地，并称其招致第二轮打击与社会性绝境（P007—P010）。",
    "定义“君”＝自己选的领导者，服从即对自己选择负责；可退出但不可未退出先离弃（P011—P014）。",
    "定义“亲”＝天地合意替你作的第一个选择，无论好坏是发到手里的牌（P015—P019）。",
    "由天地亲合意推出“师”：父母为你选的“君”即师；师非自封，是你自己的选择与命运限制共同决定（P020—P024）。",
    "提出要害：可以另作选择，但不可把错误教导的责任推给老师（P025）。",
    "给出理由：没有人任何时刻任何事完全正确，故本质上没人在教“正确的东西”（P026—P030）。",
    "反证：若不赦免老师的“错误教导”，就没有够资格的人敢当老师（P031）。",
    "导出为师资格：有“我教的注定全是错的”的自觉，所教是“有质量的错误”（P032—P036）。",
    "导出为徒资格：只求“正确的东西”者没有做学生的资格（P037）。",
    "面向为师者的训诫与唯一例外：定意牺牲的爱（P038—P042）。",
    "面向建家族者的择师铁律：只有觉者可以为师（P043—P050）。",
    "转折：站稳择师这步，这师不难敬；不敬多因老师自封为神，属“神人伦理”问题（P051—P058）。",
    "回应提问：够资格的老师面前不会产生“我给了钱凭什么尊敬你”的疑问，给出两条理由，并声明具体原因下回分解（P059—P063）。",
    "转入技术定义：语言模糊迫使听者猜测性补足，要害在补足方向（P064—P069）。",
    "定义不尊敬＝首先向下补成虚弱愚蠢版本；相对者首先向强处补足（P070—P074）。",
    "给出判据与敬畏的定义，进而把“尊敬”定义为对世界无限可能的敬畏（P074—P084）。",
    "给出教师重视尊敬的理由：补弱者沟通效率低、需排除的对象浪费生命，只有补强者能从教学获益（P085—P091）。",
    "结论：所以学生必须尊敬老师；文末标“（未完，待续）”（P092—P093）。"
   ],
   "concept_usage": [
    {"term": "天、地、君、亲、师", "meaning": "全文框架：地＝自然规律／世界恒常法则；天＝天意／神秘莫测的可能性；君＝你自己选的领导者；亲＝天地合意替你选择的双亲；师＝父母（天地亲合意）为你选择的“君”。", "evidence": "P003", "ambiguity": "作者明确“君，不是指皇帝”（P011），并用“天地合意”的拟人化表述，未说明其本体。"},
    {"term": "敬／敬畏", "meaning": "不是对人的膜拜，而是承认规律与无限可能性非自己所能断言；不敬的表现是“不信邪”、质问老天、要求绝对正确的教导。", "evidence": "P075", "ambiguity": "“敬”与“畏”在文中连用，未分别定义。"},
    {"term": "师（为师的资格）", "meaning": "师非自封，而是由客观限制、机遇与相关方意愿共同决定；为师的资格在于自觉“我教的注定全是错的”，所教为“有质量的错误”。", "evidence": "P033", "ambiguity": "“好为人师是一种罪过”一句以插入语出现，未展开其论证。"},
    {"term": "有质量的错误", "meaning": "相对于“真理”的提法：人类能给予人类的最好的东西，即自觉错误但仍有价值的教导。", "evidence": "P036", "ambiguity": "未给出衡量“质量”的标准。"},
    {"term": "尊敬（respect）", "meaning": "以尊重表达出的对世界的无限可能的敬畏；其可操作判据是听话者在模糊处首先向强处还是弱处补足，且不分对象、不计条件。", "evidence": "P080", "ambiguity": "作者称其为“技术流和实用的方法”，属于鉴定手段而非情感定义。"},
    {"term": "补强／补弱", "meaning": "补弱＝把对方的话往更虚弱愚蠢的版本补足以证明自己更明智；补强＝先假定对方在表述强版本。", "evidence": "P070", "ambiguity": "作者称模糊表达常有四五个乃至七八个版本，但未给出版本划分方法。"},
    {"term": "神人伦理", "meaning": "作者把最常见的“不敬师”重新定性：不是师生伦理问题，而是凡人自封为神、闯入人潜意识禁地所引发的问题。", "evidence": "P057", "ambiguity": "该提法为作者自造术语，未展开界定。"}
   ],
   "examples_and_targets": [
    "万有引力定律与“不敬你跳崖试试看”——作者举例说明敬地（P003）。",
    "“我就不信我这次醉驾就会出事”“我就不信有人能抓到我”——作者作为不敬天的说法举例（P005）。",
    "“凭什么是我得病”“凭什么我家没钱”“凭什么我爹不是李刚”——作者作为不敬天地的质问举例（P008）。",
    "受伤残疾、复健、装假肢——作者作为“接受起点后努力”的正面例子（P009）。",
    "好为人师——作者称其为罪过，作为师之位非自封的说明（P024）。",
    "“欺师灭祖”——作者引用该成语警告违背此条的为师者（P038）。",
    "文凭、名门大派、光环、高足——作者列为择师时不应先看的东西（P044）。",
    "“名师”与“技压天下”——作者作为传递傲慢与虚荣的反面对象（P048、P049）。",
    "“我给了钱凭什么还要尊敬你”——作者直接回应的提问者说法（P059）。",
    "respect——作者在定义尊敬时并列的英文词（P065）。",
    "“言传身教他如何待人接物”一语见 brief，不在正文内。"
   ],
   "conditions": [
    "寻求改变须“首先基于接受那个起点”，否则即为不敬天地（P007）。",
    "对君：只有在没有退出和收回意愿的前提下直接离弃才是不敬（P013）。",
    "为师资格条款对“没有任何选择”的人宽免，“你如果有任何选择的余地而接纳”才无资格（P038）。",
    "唯一例外是“认真地准备牺牲自己，接受一切误解”的定意牺牲之爱（P040）。",
    "本文所讲多针对“有意建立自己家族的初代们”（P043）。",
    "补强假定有例外：“除非有明确的证据能排除这种可能性”，且“甚至就是有所谓的证据，也并不一定能排除”（P076）。",
    "排除补弱者以“在你并非别无选择的前提下”为条件（P089）。",
    "本文为“前言”，敬师的具体逻辑与技术以及学费原因留待下回分解（P063、P064）。"
   ],
   "rhetoric_and_tone": "训诫与讲理混合的长篇答疑，第二人称“你”贯穿，带有师长口吻；用定义—推论—反证的链条层层推进（“为什么？”“要害在哪？”“为什么这样说？”）；多处以“记住这句话——”“重复一遍”“听仔细”等命令式强调；含夸张与反讽（“一败涂地沦为万世笑柄”“自封为神”“王中之王”式的称呼未见于本篇）；出现英文词 respect 与一句英文以外的插说；文末以“（未完，待续）”收束。",
   "unresolved_questions": [
    "“天地合意”“天意”是否有确定所指，本文未说明，具拟人化表述。",
    "“你的学费不会给你不敬的立场”的具体原因，作者明言“下回分解”，本篇未说明（P063）。",
    "“神人伦理”为作者自造术语，未给界定。",
    "第 P047 段称可继承“深刻的自觉、对这种人的敏感的嗅觉”，其具体内容本文未说明。",
    "P093 为 lexical 未覆盖片段“（未完，待续）”，本篇为系列未完稿。",
    "“好为人师是一种罪过”未给出论证，属断言。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "人一生必须对这五样东西有足够的敬畏。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "你不能不敬自然规律，是谓敬地。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "你不能不敬畏可能性，是谓敬天。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "但是寻求改变，一定是首先基于接受那个起点", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "什么叫不敬天地？就是仿佛自己有某种至高无上的审查权", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "君，不是指皇帝，是指你自己选的领导者。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "不敬自己选择的君，实质上是不敬自己。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P018", "quote": "你不能不敬天地，你也就不能不敬亲。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P021", "quote": "这个父母为你选择的“君”，恰恰就是“师”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P024", "quote": "是你选的，是你的命运的种种客观限制和机遇决定的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P025", "quote": "但你不可以将任何“错误的教导”的责任放在你的老师身上。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P028", "quote": "因为没有任何人、在任何一个时刻、在任何一件事情上是完全正确的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P033", "quote": "就是有没有这个“我教的注定全是错的”的自觉。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P036", "quote": "我教的不是真理，而是有质量的错误，这就是身为人类能给予人类的最好的东西了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P037", "quote": "那么对不起，你就没有做学生的资格。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P038", "quote": "你如果有任何选择的余地而接纳这种没有学生资格的人", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P041", "quote": "也就是出于愿意背负一切冤屈而死也要拯救对方于万一的、定意牺牲的、纯然的爱。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P044", "quote": "为家族成员择师，要不遗余力地、极尽一切可能地遵循这一原则。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P045", "quote": "知者不足为师、能者也不足为师，只有觉者可以为师。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P053", "quote": "学生对老师的“不敬”，极大多数是从老师自己背弃了“为师的资格”开始。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P057", "quote": "根本就不是一个“师生伦理问题”，而是一个“神人伦理”问题。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P061", "quote": "这种老师是举世奇珍，你能遇到一个就先要回去拜谢祖宗保佑了。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P062", "quote": "多半是靠近下限而不是上限的", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P070", "quote": "有的人会将这模糊性首先往下补，将你的话补足成为一个更为虚弱和愚蠢的版本", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P072", "quote": "这样的态度，就叫做不尊敬。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P075", "quote": "而是在审视一个人是否尊重神/自然的无限能力", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P076", "quote": "ta们永远会首先假定对方在表述的是强版本", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P080", "quote": "所谓尊敬，即以尊重表达出的对世界的无限可能的敬畏——这是一份信仰的礼物。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P084", "quote": "尊敬是一种对一切对象都默认适用的、不言自明的、一视同仁的习惯。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P086", "quote": "一个习惯补弱的人也绝对地劣于习惯补强的人", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P090", "quote": "这不是歧视，这只是珍惜生命。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P091", "quote": "只有补强的人，才有资格、有真实的可能从教学中获得成效。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P092", "quote": "所以学生必须尊敬老师。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "教育与师生关系", "文化与传统观念", "家族与家训", "语言与沟通"],
   "issue_candidates": ["尊师的理据", "付费与尊敬的关系", "为师资格", "为徒资格", "尊敬的技术性定义", "沟通中的补强与补弱", "天地君亲师框架"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "经验总结", "系列讲稿（未完待续）"],
   "object_candidates": ["提问者（出钱方）", "学生", "老师", "父母", "领导者", "家族初代", "名师"],
   "working_keywords": ["天、地、君、亲、师", "敬地", "敬天", "敬亲", "为师的资格", "有质量的错误", "神人伦理", "尊敬（respect）", "补强", "补弱", "敬畏", "家族答集"]
  },
  "notes": "正文共 93 段、4713 字，文末标“（未完，待续）”，属系列未完稿；P093 为 lexical 未覆盖片段。brief 中“言传身教他如何待人接物”一语见于 P010 正文（“超过所谓的‘言传身教他如何待人接物’”），未另立证据。提问者的“我出钱你出力”立场已单列为提问语境，未计入作者主张；作者在 P059—P062 直接回应了该质疑，但把具体原因留到下一篇（P063），已在 unresolved_questions 登记。"
 },
 "d4033d19": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：如何理解「可怜之人，必有可恨之处」？提问者请作者解释这句俗语。作者并不为该俗语辩护，而是把它称为“特别好玩的逻辑梗”，指出不管人可不可怜都有可恨之处，因而这句话在逻辑上并不成立；随后把它的真实功能解释为“为了不愿同情而找的理由”，并用一段带讽刺意味的“心路历程”Step 1—Step 8 演示这种自我说服过程。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "把该俗语定性为“特别好玩的逻辑梗”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "提出真正的前提：不管人可不可怜都有可恨之处；一个人是否可恨全看你是不是恨他、要不要去找可恨点。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "理由：仇恨是人类的种族天赋，对“注定能力有限、注定愚蠢、注定傲慢”的人类找出恨点极容易，“加个零都不叫事”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "顺推：人必可恨，可怜的人自然也有可恨之处，否则就是基本逻辑要重修。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "指出该句的真实功能：那是为了不愿同情而找的理由；欲不同情也同样不患无辞。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020"], "summary": "以 Step 1—Step 8 演示心路历程：从看见可怜人，到怕自己虚伪而不舒服，到用俗语去找可恨之处，再到把毛病说成其倒霉的原因、判定“活该”、转而检讨自己，最后以“活该！！x2”收尾。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“可怜之人，必有可恨之处”是个逻辑梗：其实不管人可不可怜，都有可恨之处。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个人是不是可恨，全看你是不是恨他、要不要去找可恨点，即“可恨”取决于评判者的态度与寻找。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "仇恨是人类的种族天赋；对注定能力有限、注定愚蠢、注定傲慢的人类找出恨点极其容易，故“人必可恨”。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该俗语提供的是不愿同情时的理由——欲加之罪不患无词，欲不同情也一样不患无辞。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "以 Step 1—8 演示的心路历程显示：人先因不愿付出行动、怕被当作虚伪而去找对方的可恨之处，再用“活该”完成自我说服。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C006", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "文中以“老话说得好，可怜之人必有可恨之处”复述被讨论的俗语，属被引述的说法而非作者主张。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "开篇给该俗语定性为“特别好玩的逻辑梗”（P001）。",
    "换前提：不管可不可怜都有可恨之处（P002）。",
    "推出“可恨”取决于判断者：全看你是不是恨他、要不要去找可恨点（P003）。",
    "给理由：仇恨是人类的种族天赋，在能力有限、愚蠢、傲慢的人类身上找恨点极容易（P004—P005）。",
    "顺推该俗语的字面结论也成立：人必可恨，可怜的人当然也有可恨之处（P006—P007）。",
    "转出真实功能：这句话是为了不愿同情而找的理由（P008—P010）；以“欲不同情，也一样不患无辞”作类比收束（P011）。",
    "以 Step 1—8 的心路历程演示这一自我说服过程（P012—P020）。"
   ],
   "concept_usage": [
    {"term": "可恨", "meaning": "本文中被相对化：不是对象固有的人格属性，而是仇恨者是否愿意寻找的结果（“一个人是不是可恨，全看你是不是恨他”）。", "evidence": "P003", "ambiguity": "作者未区分“客观上值得恨”与“被恨”两种读法。"},
    {"term": "仇恨", "meaning": "被作者称为人类的种族天赋，指人轻易能找到恨点的能力。", "evidence": "P004", "ambiguity": "“种族天赋”为修辞性说法，未给依据。"},
    {"term": "逻辑梗", "meaning": "作者对该俗语的定性：其“必有”式的推论在更宽的前提下失去意义（因为人人皆有可恨之处）。", "evidence": "P001", "ambiguity": "作者未以逻辑学形式展开这一批评。"},
    {"term": "同情", "meaning": "与“做点什么”相连：若可怜对方就要行动，不作为则自认虚伪并受折磨。", "evidence": "P014", "ambiguity": "作者把这套动机写成“心路历程”，未声明其为普遍心理机制。"}
   ],
   "examples_and_targets": [
    "“可怜之人，必有可恨之处”——被讨论的俗语，作者称其为“老话说得好”的引用（P001、P015）。",
    "“欲加之罪不患无词”——作者引用的成语式说法，用以类比“欲不同情”（P011）。",
    "Step 1—Step 8 心路历程——作者自拟的讽刺性叙事（P013—P020）。",
    "“活该！”“活该！！x2”——作者虚拟的结论式感叹（P017、P020）。",
    "未能给出具体人物、事件或数据：本篇没有实例或统计。"
   ],
   "conditions": [
    "结论的前提是“不管人可不可怜，都有可恨之处”（P002）。",
    "“可恨”的判断以评判者是否去找为条件（P003）。",
    "作者对心路历程的表述用“Step”编号，属演示性叙事，未声明是某一具体个人的真实经历（P012—P020）。"
   ],
   "rhetoric_and_tone": "调侃、反讽、短句节奏；以“好吧”“其实呢”“当然啦”“啊呀呀”等口语语气词拉开距离；用 Step 1—8 的分步叙事把“不愿同情”的自我说服过程戏剧化，并以“他活该！”“活该！！x2”作讽刺性收束；对“注定能力有限、注定愚蠢、注定傲慢的人类”使用夸张。",
   "unresolved_questions": [
    "该俗语的出处本文未注明，只写“老话说得好”。",
    "Step 1—8 是作者自拟的心路历程演示，还是对某人真实心理的归纳，本文未说明。",
    "作者提出“人必可恨”但未给出可恨的判准或反例处理方式。",
    "正文中 P011 与 P012、P014 与 P015 之间的字符区间存在空档（正文换行），文本已按正文原样保留。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "其实呢，是不管人可不可怜，都有可恨之处。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "一个人是不是可恨，全看你是不是恨他，要不要去找可恨点。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "仇恨是人类的种族天赋。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "那是为了不愿同情而找的理由啊。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P014", "quote": "我要是什么都不做，我岂不是一个虚伪之人吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P015", "quote": "我来找找他有没有可恨之处", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P017", "quote": "Step 5: 他活该！", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "老话说得好，可怜之人必有可恨之处。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理", "道德情感", "俗语批判"],
   "issue_candidates": ["可怜与可恨的关系", "同情的动机与回避", "仇恨的心理机制", "俗语的逻辑问题"],
   "text_function_candidates": ["答疑", "评论", "反讽性叙事"],
   "object_candidates": ["可怜人", "同情者", "旁观者", "老话/俗语"],
   "working_keywords": ["可怜之人必有可恨之处", "逻辑梗", "可恨", "仇恨", "种族天赋", "同情", "活该", "心路历程"]
  },
  "notes": "本篇为短篇反讽评论（638 字）。作者并未否认该俗语的字面推论（P006—P007），而是否定其意义并揭示其功能（P008—P011）。“可怜之人必有可恨之处”在 P015 属被引俗语，已用 quoted_or_cited + cited_source 标注，未归给作者。Step 1—8 为作者自拟的演示性叙事，已在 unresolved_questions 登记其性质。"
 },
 "958169e5": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：如何能从不断的自我否定与自我怀疑中走出来？提问者把自我怀疑当作需要摆脱的困境。作者先以设问反问“你为什么要走出来呢”，不接受该前提，反而断言不可抑制的自我怀疑与自我否定是成熟的标志，并指出“必须绝对自信才能行动”的方法论注定导致反复崩溃；结论是不要把力气花在重建自信上，而是“将错就错”。篇末以“同时用开水送服：何谓‘自信’？”引出姊妹篇。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "以反问开篇，要求提问者列举“要走出来”的理由，并罗列可能的理由（痛苦、没有尊严、憋屈、不自信就做不下去）。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009"], "summary": "反问：如果你根本不可能是对的呢？并判断提问者在方法论上是错的，要学的不是重建自信。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "正面主张：永远不可抑制的自我怀疑与自我否定是成熟的标志、是好事、是进步；世界上不存在提问者想象的那种“自信”的健康生活方式，那种自信逻辑上是无本之木。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P014"], "summary": "提出真正的问题：在“我肯定是在用错误的方法追求着错误的目标”这一前提下，如何重建生存动力。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017"], "summary": "描述依赖“绝对正确”感者的结局：成熟与经验增长后必然发现自己原先认为对的东西有大量天真幼稚，若按“只能相信自己绝对正确”的方法论行动，看到错误就会崩溃，因而一定会再次崩溃。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020"], "summary": "换一套新立场、恢复“我这回肯定正确了”的出发点只是借到新赌本，赌局未变，仍会再次崩溃。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "除打垮逻辑三段论外，不真正悔改者只有一条路：不认错、逃避刺激源、拒不对话，靠逃避维持表面安全感；逻辑注定其终将走到物理性绝境，甚至宁可吸毒或“最后搏一把”也不认错。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027"], "summary": "反驳“偶然幸运／发达了就不一样”：发达会刺激双倍下注并把子女压进同一条路；长期看无人逃脱，一天不改就一天在通向大绝望、大抑郁的铁轨道上。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P028", "P029", "P030"], "summary": "给出真相：前半生成果本就来自用错误方法追寻错误目标；“只有正确的目标和正确的方法才能保证令人满意的结果”是逻辑没学好的蠢话，因为二者对人类根本不可能拥有，历史上也没有任何成功靠它们成就。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032", "P033"], "summary": "关键区分：目标与方法不正确并不构成根本威胁，态度不正确、一见不正确就恐慌绝望才是病根。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P034", "P035", "P036"], "summary": "结论与行动建议：不需要“自信”才能好好做事，要让“自信瘾”患者互相鼓励跳坑；你要学会将错就错；末段“哦，忘了谢邀”。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P037", "P038"], "summary": "以“同时用开水送服：何谓‘自信’？”引出关联篇目，属结构残留。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者不接受提问的前提，反问“你为什么要从自我否定与自我怀疑中走出来呢”，要求先列举理由。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你要学会的不是“重建自信”或“走出来”，恰恰相反，不可抑制的自我怀疑与自我否定才是人开始成熟的标志。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上不存在提问者所想象的那种“自信”的健康生活方式，那种自信从逻辑上就是无本之木。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "真正的问题是：基于“我肯定是在用错误的方法追求着错误的目标”这一永远正确的逻辑前提，如何重建自己的生存动力。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "靠构建虚幻的“绝对正确”感行动的人，随着成熟与经验增长必然看到自己的错误，按“只能相信自己绝对正确”的方法论，看到错误就会崩溃，因而一定会再次崩溃。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若不真正悔改，除打垮逻辑三段论外只有一条路：不认错、逃避一切可能引发自我怀疑的刺激源，靠长期练熟的逃避法维持表面安全感，直到客观时间给出无法不面对的绝境。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“发达”并不意味着不同：它使人以为成功源于自己的英明神武，从而双倍下注并把子女压进同一条路；长期看无人逃脱，一天不改就一天在通向大绝望、大抑郁的铁轨道上。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "前半生的成果本就来自使用错误的方法追寻错误的目标；“只有正确的目标和正确的方法才能保证令人满意的结果”是蠢话，因为二者对人类根本不可能拥有，历史上也没有任何成功靠它们成就。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "目标与方法不正确并不构成根本威胁；态度不正确、一看到不正确就恐慌绝望，才是当前惶惶不可终日的病根。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不需要“自信”才能好好做事，作者要读者学会“将错就错”。", "evidence": ["E17", "E18"]}
   ],
   "argument_steps": [
    "以反问拒绝提问前提：先问“你为什么要走出来”，并要求列举理由（P002—P004）。",
    "列举并悬置若干可能的理由（痛苦、尊严、憋屈、不自信就做不下去）（P005—P006）。",
    "提出反诘：如果你根本不可能是对的呢？并断言提问者在方法论上错了（P007—P008）。",
    "正面立论：要学的不是重建自信；不可抑制的自我怀疑与自我否定是成熟的标志、是好事、是进步（P009—P012）。",
    "否定“自信”式健康生活方式的逻辑基础（P013）。",
    "重述真正的问题：在“用错误方法追求错误目标”的前提下重建生存动力（P014）。",
    "论证依赖“绝对正确”感的必然后果：成熟后看到错误→崩溃；因此一定会再次崩溃（P015—P017）。",
    "以赌博为喻说明换新立场只是借新赌本，赌局未变（P018—P020）。",
    "给出不悔改者的唯一出路：逃避、不认错，直到客观绝境（P021—P023），甚至宁可吸毒或最后搏一把（P024）。",
    "否定“发了就不一样”的例外（P025—P027）。",
    "提出真相：错误方法与目标本就是前半生成果的来源（P028）；“正确目标＋正确方法”之说是蠢话（P029—P030）。",
    "作出区分：目标与方法不正确不构成根本威胁，态度不正确才是病根（P031—P032）。",
    "结论与行动建议：不需要自信，学会将错就错（P034—P035），并引出姊妹篇（P037—P038）。"
   ],
   "concept_usage": [
    {"term": "自我怀疑／自我否定", "meaning": "本文中被重新评价为“人开始成熟的标志”“好事”“进步”，而非需要消除的症状。", "evidence": "P010", "ambiguity": "作者未区分健康的自我怀疑与病理性的自我否定。"},
    {"term": "自信", "meaning": "指提问者想象的那种“绝对正确”式的确信；作者称其为虚幻、逻辑上的无本之木，并用“自信瘾”称其依赖者。", "evidence": "P013", "ambiguity": "作者未给出替代性的“信心”含义，只说“将错就错”。"},
    {"term": "逻辑三段论", "meaning": "作者用作“只能以自己相信绝对正确的方法做绝对自信正确的事才是安全的”这一推理结构的代称，称不打破它就只剩逃避一途。", "evidence": "P021", "ambiguity": "文中未给出该三段论的形式化表述。"},
    {"term": "将错就错", "meaning": "作者给出的替代态度：在承认目标与方法必然错误的前提下继续行动，而不是等待绝对正确。", "evidence": "P035", "ambiguity": "未展开具体做法。"},
    {"term": "赌本／赌局", "meaning": "比喻：换新立场、新方法只是借到新赌本，而“靠绝对正确感行动”的赌局本身没有改变。", "evidence": "P019", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "提问者的处境与可能理由（痛苦、没有尊严、憋屈、窝囊、想拿真理糊对方一脸）——作者复述并反问（P005）。",
    "“重建自信”“从自我怀疑、自我否定中走出来”——作者直接反驳的流行说法（P009）。",
    "赌博比喻：“借到了一笔新赌本，赌局并没有变”（P019）。",
    "“最后搏一把”“有赌未为输”——作者引用的赌徒说法（P024）。",
    "吸毒——作者作为宁可如此也不认错的例子（P024）。",
    "“自信瘾”患者——作者对被“自信”依赖者的称呼（P034）。",
    "“何谓‘自信’？”——文末指向的关联篇目（P038）。"
   ],
   "conditions": [
    "成立前提被作者表述为“永远正确”：即人只能以归根到底必然错误的方法追求必然错误的目标（P007、P014）。",
    "推论使用“如果……呢”的假设句式（P007）；崩溃的结论以“遵循……的方法论”为条件（P015—P017）。",
    "“除非你打垮逻辑三段论，否则只要你不真正的悔改”限定唯一出路（P021）。",
    "“长期看”是作者对结局判断的时间尺度（P026、P027）。",
    "作者用“很多人”“大部分人”描述现象范围，未主张人人如此（P022、P024）。"
   ],
   "rhetoric_and_tone": "高强度反问与斥责式口吻：“且让我超大音量问你一句”“明白吗？”“推出什么？”“看懂了没有？”；以“狗屁‘自信’”“自信瘾患者互相鼓励着跳坑”等粗直贬语加强语气；用“赌本／赌局”“铁轨道”作比喻；以“听好了，真相是——”“听仔细关键词”等命令式强调；结尾“哦，忘了谢邀”与“同时用开水送服”带调侃意味。",
   "unresolved_questions": [
    "“将错就错”的具体做法本文未展开，只在结尾一句给出。",
    "“逻辑三段论”在本文中未形式化，所指为作者自述的推理结构。",
    "作者对“历史上从来就没有过任何一种成功是靠着这两个东西成就的”一断言未给出例证或数据，属待外部核查。",
    "P038“何谓‘自信’？”为 lexical 未覆盖片段，指向另一篇关联回答，本篇未展开。",
    "作者称“很多人到这时还是宁可去吸毒”，未给出实例或统计。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "你为什么要从自我否定与自我怀疑中走出来呢？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P010", "quote": "永远不可抑制的自我怀疑和自我否定，才是人开始成熟的标志。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P013", "quote": "那种自信从逻辑上就是无本之木。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P014", "quote": "你要怎么重建自己的生存动力。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P015", "quote": "这是绝对不可避免的，一丁点侥幸都不要有。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P016", "quote": "——看到错误就会崩溃，而你又肯定会看到错误，推出什么？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P017", "quote": "你一定会再次崩溃。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P021", "quote": "除非你打垮逻辑三段论，否则只要你不真正的悔改，你可选的路就只有一条", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P023", "quote": "直到客观时间给他们物理性的、实践上山穷水尽的、他们完全无法不承认不面对的绝境才会走下这条封闭快速路。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P025", "quote": "那些“发达”只会让他们以为自己的“成功”是来自自己的英明神武，刺激他们双倍下注", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P027", "quote": "一天不改，就一天还在这条通向大绝望、大抑郁的铁轨道上。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P028", "quote": "你前半生取得的任何成果，本来就是从使用错误的方法追寻错误的目标的过程中得来。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P029", "quote": "因为“正确的目标”和“正确的方法”是对人类来说根本不可能拥有的东西。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P030", "quote": "历史上、从没有、任何一种成功是靠这两个不存在的东西成就的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P031", "quote": "你的目标不正确，你的方法不正确，对你的成功并不构成根本的威胁。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P032", "quote": "你的态度不正确，一看到不正确就恐慌和绝望，才是你现在惶惶不可终日的病根。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P034", "quote": "谁说你需要什么狗屁“自信”才能好好做事？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P035", "quote": "你要学会将错就错。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与自我认识", "方法论", "人生哲学"],
   "issue_candidates": ["自我否定与自我怀疑", "自信的可靠性", "绝对正确感与崩溃循环", "错误方法与错误目标", "将错就错"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "驳论"],
   "object_candidates": ["提问者", "“自信瘾”患者", "依赖绝对正确感的人", "作者自述的关联篇《何谓“自信”》"],
   "working_keywords": ["自我怀疑", "自我否定", "自信", "重建自信", "无本之木", "生存动力", "绝对正确", "逻辑三段论", "悔改", "将错就错", "赌本", "铁轨道"]
  },
  "notes": "正文 38 段，其中 P003、P020 为 heading 节点；P020 的标题内容与 P017 的判断重复（“你一定会再次崩溃”）。P038“何谓‘自信’？”为 lexical 未覆盖片段（骨架 divergence=true），指向关联篇目，已在 unresolved_questions 登记。全文以反问与预测语气为主，已按 modality=questioned/predicted 保留。"
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
