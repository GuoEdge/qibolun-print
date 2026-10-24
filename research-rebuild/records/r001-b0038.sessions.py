# -*- coding: utf-8 -*-
"""批次 r001-b0038 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0038.sessions.py            # 写 out/r001-b0038.out.jsonl
  python3 records/r001-b0038.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0038"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0038.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "60af0305": {
  "analysis": {
   "question_context": "提问者（Q001）问“如果「知乎」即将改名，叫什么新名字会取悦你？”，即邀请答主为知乎改名献策。作者没有提出任何名字，而是在 P001 直接拒绝参与（不接受知乎的自我命名，只能自己注销账号离开），随后把话题转为对“借他人私营服务侮辱对方”的训诫：先断定这类行为没有“正义”（P002）、要求基本是非对错观念（P003），再指出其影响自我认知与他人观感（P004-P006），给出交友告诫（P007）与“食碗面，翻碗底”的为人忌（P008），区分“不喜欢/严厉的表达”与“侮辱和霸凌”（P009-P011），以泰森、马云、平台三组例子反驳“霸凌只对弱者才算”的思路（P012-P019），给出霸凌定义与和平预设前提（P020-P022），最后以校园恶霸、“实力不济卑鄙凑”和“你们不要沾染”收束（P023-P029）。全篇未讨论知乎改名一事，也未点名任何具体主体。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "作者拒绝参与提问所求的命名建议：不接受知乎的自我命名，只能自己注销账号离开。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003"],
     "summary": "判断这类行为没有“正义”，并要求人要有基本的是非对错观念。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P004", "P005", "P006"],
     "summary": "说明后果：这不是一时一地谁强权的问题，会影响自我认知与他人观感；别人眼中的“混蛋”形象对个人生活的决定性远大于自我想象的“正义使者”。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P007", "P008"],
     "summary": "对读者的告诫：不要对与这类人交往抱有好结果的侥幸；并引“食碗面，翻碗底”断为为人大忌。",
     "role": "action_advice"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P009", "P010", "P011"],
     "summary": "限定与区分：不喜欢、不高兴不意味着有权利侮辱对方；可以用严厉的表达，严厉的表达不找借口、不假公济私、不阴阳怪气，不是侮辱和霸凌；劝人不要染上侮辱和霸凌的恶习。",
     "role": "qualification"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019"],
     "summary": "反驳“霸凌只有对弱者才算，对强者就不算”的流行思路，并以泰森（睡着被踹、背后被捅）、马云（匿名造谣）、有绝对管理权的平台（阴阳怪气侮辱）为例，逐个判为“算”。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P020", "P021", "P022"],
     "summary": "给出霸凌定义（背叛和平的预设发起的偷袭）；指出战场上双方一开始就知道对方是敌人时该概念失效；除此之外人对人普遍存在和平架设，使借助背叛假设的攻击尤其不义。",
     "role": "definition"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": ["P023", "P024", "P025", "P026"],
     "summary": "进一步论证：校园恶霸的攻击不是“基于实力的攻击”；霸凌最大的问题是“实力不济卑鄙凑”，用卑鄙取得局部武力优势后捂住“卑鄙”谈“压倒性实力”；这种强大感是幻觉，迟早撞上 real deal 而粉身碎骨。",
     "role": "reason"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": ["P027", "P028", "P029"],
     "summary": "结论与训诫：仗“法不责众”和“语言技巧”搞阴阳怪气与“背后捅泰森”没有区别，没有资格当作勇敢吹嘘，只是不自知的无耻；“你们不要沾染”。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者不接受知乎的自我命名，认为自己只能注销账号离开。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：世界上不存在用别人的私营服务去侮辱别人的“正义”。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为这类行为不是一时一地谁是强权的问题，而会影响行为人自己的认知和别人对他的观感，且后者对其生活更具决定性。",
     "evidence": ["E3", "E4", "E5"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“如果你珍惜自己的生命和幸福”为条件，劝读者不要对与这类人交往会有好结果抱有侥幸。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者区分“不喜欢、不高兴”与“侮辱”：前者不等于有权侮辱对方，且可以改用不找借口、不假公济私、不阴阳怪气的严厉表达，后者才是侮辱和霸凌。",
     "evidence": ["E8", "E9"]
    },
    {
     "claim_id": "C006",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "作者转述并反驳的一种流行思路：霸凌只有对弱者才算，对强者就不算。",
     "evidence": ["E10"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以泰森、马云和有绝对管理权的平台为例，主张对强者（乃至平台）的偷袭、造谣与阴阳怪气侮辱同样算霸凌。",
     "evidence": ["E11", "E12", "E13"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出定义：霸凌就是背叛和平的预设发起的偷袭。",
     "evidence": ["E14"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者以“如果你是在战场上，大家一开始就知道对方是敌人”为条件，称霸凌这个概念自然失效；除此之外人对人普遍存在和平架设，使借助背叛这个假设的攻击尤其不义。",
     "evidence": ["E15", "E16"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称校园恶霸那种攻击不能叫“基于实力的攻击”，因为其要躲进小巷卫生间并威胁对方不准告诉家长、老师。",
     "evidence": ["E17"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为霸凌最大的问题是“实力不济卑鄙凑”：靠卑鄙形成局部武力优势，再把“卑鄙”捂住、昂然谈起“压倒性实力”。",
     "evidence": ["E18"]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预言这种卑鄙得逞造成的强大感只是幻觉，迟早有一天让当事人在信心满满时撞上 real deal、粉身碎骨。",
     "evidence": ["E19"]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言仗着“法不责众”和“语言技巧”搞这类阴阳怪气与“背后捅泰森”性质没有区别，没有资格作为勇敢吹嘘，只是不自知的无耻。",
     "evidence": ["E20", "E21"]
    }
   ],
   "argument_steps": [
    "拒绝提问所求：不接受知乎的自我命名，只能自己注销账号离开（P001）。",
    "价值判断：不存在用别人的私营服务去侮辱别人的“正义”，人要有点基本的是非对错观念（P002、P003）。",
    "后果论证：这不是一时一地谁强权的问题，会影响自我认知与他人观感，别人对你的观感对你的生活更具决定性（P004-P006）。",
    "行动告诫：不要对与这类人交往抱有好结果的侥幸；引俗语“食碗面，翻碗底，是为人大忌”（P007、P008）。",
    "让步与划界：不是不能不喜欢、不能不高兴，而是不喜欢不等于有权侮辱；可用严厉表达，严厉表达不是侮辱和霸凌（P009-P011）。",
    "树靶：很多人的思路是“霸凌只有对弱者才算，对强者就不算”（P012）。",
    "例证反驳：趁泰森睡着踹一脚、背后捅泰森一刀、匿名造马云的谣、阴阳怪气侮辱有绝对管理权的平台，都算（P013-P019）。",
    "给出定义与前提：霸凌是背叛和平的预设发起的偷袭；战场上的敌人关系使该概念失效；除此之外人对人有普遍和平架设（P020-P022）。",
    "反例推进：校园恶霸并非“基于实力的攻击”；霸凌最大问题是“实力不济卑鄙凑”并掩盖卑鄙（P023、P024）。",
    "贬斥与预测：何其无耻；这种强大感是幻觉，迟早撞上 real deal（P025、P026）。",
    "结论训诫：阴阳怪气与“背后捅泰森”无区别，不是勇敢而是无耻；劝读者不要沾染（P027-P029）。"
   ],
   "concept_usage": [
    {
     "term": "霸凌",
     "meaning": "本文定义为“背叛和平的预设发起的偷袭”，并明确不限于对弱者：对强者、对平台同样成立；与“堂堂正正、基于实力的攻击”相对。",
     "evidence": "P020",
     "ambiguity": "定义只给出一句断语，未说明判定要件（如伤害程度、双方关系、是否需持续），也未说明对“强者”的攻击为何仍算霸凌的完整理由。"
    },
    {
     "term": "和平的预设/和平架设",
     "meaning": "人对人普遍存在的和平预设；霸凌之所以不义，在于背叛这一假设；战场上双方均知互为敌人时该预设不存在，故霸凌概念失效。",
     "evidence": "P021",
     "ambiguity": "“和平架设”的成立范围、例外与强度未界定。"
    },
    {
     "term": "严厉的表达",
     "meaning": "作者允许的反对方式：不找借口、不假公济私、不阴阳怪气，因而不是侮辱和霸凌。",
     "evidence": "P010",
     "ambiguity": "只给否定式特征，未给出正面标准。"
    },
    {
     "term": "实力不济卑鄙凑",
     "meaning": "作者对被反驳者行为方式的概括：靠卑鄙形成局部武力优势，再把“卑鄙”两个字捂住，昂然谈起“压倒性实力”。",
     "evidence": "P024",
     "ambiguity": "为作者自造短语，未给出判定标准。"
    },
    {
     "term": "食碗面，翻碗底",
     "meaning": "作者引用的俗语，用来说明“受人之惠却反手侮辱对方”是为人忌。",
     "evidence": "P008",
     "ambiguity": "作者未解释该俗语的字面义与来源，本文对其含义未展开说明。"
    },
    {
     "term": "real deal",
     "meaning": "文中英文插入语，用于说明靠卑鄙得逞者终将遇到真正的对手。",
     "evidence": "P026",
     "ambiguity": "本文未解释该词的具体所指。"
    },
    {
     "term": "平台",
     "meaning": "指有绝对管理权的一方；在提问语境下可能指知乎，但正文未点名。",
     "evidence": "P018",
     "ambiguity": "是否特指知乎、以及“平台”与“提问所指对象”是否同一，本文未说明。"
    }
   ],
   "examples_and_targets": [
    "泰森：作者例证（一拳能打死牛、睡着被踹、背后被捅），用于反驳“对强者不算霸凌”（P013、P015、P016）。",
    "马云：作者例证（比你有钱得多、匿名造谣），用于同一反驳（P017）。",
    "有绝对管理权的平台：作者例证（阴阳怪气地侮辱平台也算霸凌）（P018、P019）。",
    "战场与敌人：作者设定为霸凌概念失效的假设情形（P021）。",
    "学校里面的恶霸：作者举例并反驳“基于实力的攻击”之说（P023）。",
    "“背后捅泰森”：作者用于类比的修辞材料（P027）。",
    "俗语“食碗面，翻碗底”：作者引用的修辞/训诫材料（P008）。",
    "提问者提出的“知乎改名”：提问者材料，正文未回应、未提出任何新名字（Q001）。"
   ],
   "conditions": [
    "P007 的告诫以“一个人无论在任何对象面前犯现在这种行为”与“如果你珍惜自己的生命和幸福”为条件。",
    "P021 以“如果你是在战场上，大家一开始就知道对方是敌人”为假设条件，得出霸凌概念自然失效。",
    "P022 用“除此之外”限定：上述战场情形之外，人对人普遍存在和平架设。",
    "P012 以“很多人的思路”引出被反驳的流行看法，属于被作者反驳的观点而非作者主张。",
    "P026 以“迟早有一天”作预测性表述，非已发生事实。",
    "P010 对“严厉的表达”给出否定式限定（不找借口、不假公济私、不阴阳怪气）。"
   ],
   "rhetoric_and_tone": "训诫体与断语式短句为主：大量设问自答（“算不算？”“当然算。”“也算。”）形成连打节奏；直接对读者喊话（“看得见我这条的人们记住”“你们不要沾染”）；情绪强烈（“何其无耻”）；引用粤语俗谚与英文插入语（real deal）；把提问的“改名”语境转为对侮辱/霸凌的道德训斥，未回应提问本身。",
   "unresolved_questions": [
    "提问问“知乎即将改名，叫什么新名字会取悦你”，正文未提出任何名字，也未讨论知乎改名一事，问答之间的对应关系需研究者判断。",
    "作者批评的具体对象与主体不明：正文未点名任何个人、机构或事件；“现在这种行为”“自我命名”具体指什么，本文未说明。",
    "P018 的“平台”是否特指知乎，本文未说明。",
    "“知乎即将改名”一事本文未提供依据，是否属实需外部核查。",
    "作者身份、与平台的关系（是否为平台使用者/受惠者）本文未说明，而“食碗面，翻碗底”的用法依赖这层关系。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不接受知乎的自我命名，只能自己注销账号离开。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "世界上没有用别人的私营服务去侮辱别人的“正义”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "不要以为这只是一时一地谁是强权的问题，这会影响到你对自己的认知和别人对你的观感。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "你以为这是正义使者，在别人看来却是一种绝不会想要在自己生活中保留的混蛋。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "后者对你的生活比前者有决定性得多。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "如果你珍惜自己的生命和幸福，请务必不要对与这些人交往抱有会有好结果的侥幸。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "食碗面，翻碗底，是为人大忌。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "而是说你不喜欢、不高兴，不意味着你有权利侮辱对方。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P010", "quote": "严厉的表达是不找借口、不假公济私、不阴阳怪气的，它不是侮辱和霸凌。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P012", "quote": "很多人的思路是“霸凌只有对弱者才算，对强者就不算”。", "relation": "context"},
    {"key": "E11", "paragraph_id": "P013", "quote": "比如泰森一拳能打死牛，那么趁泰森睡着，踹泰森一脚算不算霸凌泰森？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "马云比你有钱得多，匿名造马云的谣算不算？当然也算。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "平台有绝对的管理权，那么阴阳怪气的侮辱一下平台算不算？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "什么叫霸凌？就是背叛和平的预设发起的偷袭。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "如果你是在战场上，大家一开始就知道对方是敌人，那么自然霸凌这个概念自然失效。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P022", "quote": "除此之外，人对人普遍存在和平架设，这使得借助背叛这个假设而做的攻击尤其的不义。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "不要以为学校里面的恶霸那种攻击就叫“基于实力的攻击”——堂堂正正为什么要找小巷子卫生间？为什么要威胁对方不准告诉家长、告诉老师？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "霸凌最大的问题就是“实力不济卑鄙凑”，靠卑鄙形成了局部武力优势，然后把“卑鄙”两个字捂住，昂然谈起“压倒性实力”来。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "这种卑鄙得逞造成的强大感只是一种幻觉、迟早有一天让当事人在信心满满时撞上real deal，粉身碎骨。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P027", "quote": "仗着“法不责众”和“语言技巧”搞这类阴阳怪气，其实跟“背后捅泰森”性质没有任何区别。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P028", "quote": "这没有资格拿来作为一种勇敢吹嘘，只是一种不自知的无耻而已。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P029", "quote": "你们不要沾染。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理/道德评论", "网络社区与平台关系", "暴力与欺凌"],
   "issue_candidates": ["霸凌的界定与边界", "对强者或平台是否构成霸凌", "受惠者反过来侮辱对方", "提问：为知乎改名"],
   "text_function_candidates": ["评论", "训诫", "论辩", "答疑（未回应所问）"],
   "object_candidates": ["知乎（提问所指，正文未点名）", "平台管理方", "泰森", "马云", "学校恶霸"],
   "working_keywords": ["翻碗底", "霸凌", "和平的预设", "和平架设", "实力不济卑鄙凑", "real deal", "严厉的表达", "阴阳怪气", "法不责众"]
  },
  "notes": "正文无图片节点。提问请求为“给知乎改名献策”，正文未提出任何名字，故内容单元按作者实际论述（侮辱/霸凌的训诫）划分，未据提问补写。brief 字段为正文语句摘录，仅作导航。"
 },
 "90c3f6e6": {
  "analysis": {
   "question_context": "提问者（Q001）问疫情期间组织小区蔬菜采购的最佳实践。作者以方案书作答，给出“物业与生鲜供应点/大型商超配合的规模化供应方案”（P001-P019）与“小区居民或居民区外围生鲜超市自建团购服务方案框架”（P020-P150）两套方案；自述因武汉部分地区已要求商超停止接受个人采购而紧急追加（P002），套装设计节自注“待完善”（P084）。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "标题与缘起：物业与生鲜供应点/大型商超配合的规模化供应方案；因武汉部分地区要求商超停止接受个人采购，紧急追加供参考。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P005",
      "P006",
      "P007",
      "P008",
      "P011",
      "P016",
      "P017",
      "P019"
     ],
     "summary": "第一套方案流程：极简套装按人口定量（只能要或不要）；限时在线表单收需求、窗口不宜深夜；每周两次、特殊困难例外；向生鲜店发布口粮包标准并由其采购分装、统一交付；口粮包四类组合及规格；收货抽查并邀两家以上供应商调次日订单；分发到门栋或门前“敲门即走”，可收服务费；为老人困难户征集志愿者代下单。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P020",
      "P021",
      "P022",
      "P023",
      "P024",
      "P025",
      "P026"
     ],
     "summary": "第二套方案框架与挑战：居民反复询问单价数量库存、频繁改单取消造成人力记录压力；缺少严谨简洁的服务约定致反复询问与误解纠纷，损耗志愿者热情与公信力。",
     "role": "context"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P027",
      "P028",
      "P030",
      "P033",
      "P036",
      "P037"
     ],
     "summary": "规则思路与《基本规则》：以高度限制交易灵活性降低服务成本、提高效率、压缩沟通与争议；含固定套装、一口价、不可增减定制、订单不可撤销、超时未领取视作捐赠、短信收货凭证、次日配送与未配送可退款、只服务名单内用户、不建议超能力吸纳成员。",
     "role": "action_advice"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P039",
      "P040",
      "P045",
      "P047"
     ],
     "summary": "组建团队：负责人、物资采购、物资分装、配送管理、后台管理、社区/物业外协员、买菜群沟通负责人等角色的职责、资质与任职要求。",
     "role": "action_advice"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P048",
      "P050",
      "P051",
      "P052",
      "P059"
     ],
     "summary": "团队成员心理建设：居民习惯高体贴消费而可能语言暴力，志愿者既期待尊重又是业余临时人员，落差造成严重心理冲击；负责人应及时干预（退款并解除攻击者资格、打预防针、多招客服、保障志愿者家庭、积累话术手册、条件许可时设专人接手难接待客户、录制短视频）。",
     "role": "action_advice"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P060",
      "P061",
      "P062",
      "P063",
      "P064"
     ],
     "summary": "订单系统方案：推荐基于微信群接龙的简易订单系统（附视频教程指引），并给出番茄表单方案（注册、选用“小区超市”模板与视频设置指南）。",
     "role": "action_advice"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P065",
      "P068",
      "P069",
      "P074",
      "P083"
     ],
     "summary": "各类范本：群公告范本及规则细则（不可议价、按套餐、不可撤销、超时视作捐赠、短信凭证、配送退款、仅注册会员、满量停单、特困人士认捐上报社区等），及订单与收货确认短信范本。",
     "role": "example"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P084",
      "P086",
      "P087",
      "P090",
      "P091",
      "P093"
     ],
     "summary": "套装设计最佳实践（标题自注“待完善”）：最大重量不宜超5公斤、宜固定重量、不宜加次级包装、不宜多易碎成分、单套价格宜200元内、应提供廉价与轻加工套装（优先困难人士）、可考虑糖尿病人套装、可按品类或冷藏设计。",
     "role": "action_advice"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P096",
      "P098",
      "P112",
      "P128",
      "P141",
      "P148"
     ],
     "summary": "套装设计经典方案（作者注明摘抄自某大型商超方案；覆盖 P096-P150）：肉食套A/B/C、蔬菜套A/B、水果套A/B、水产套A/B、大厨房商品套餐、主食套的品项与数量。",
     "role": "example"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "因武汉部分地区已要求大型商超停止接受个人采购，作者紧急追加本方案供参考。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "第一套方案主张物业发布极简套装标准并按人口定量（只能要或不要），以限时在线表单统计次日需求、下单窗口不宜深夜，原则上每周两次（特殊困难除外）。",
     "evidence": [
      "E2",
      "E3",
      "E4"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "主张物业向附近生鲜店发布“居民标准口粮供应包”标准并由其大批量采购、分装、统一交付；建议口粮包为蔬菜包+蛋白质包+水果包+主食包，蔬菜包5斤一包、四到五品种、只做大致要求，鱼肉蛋奶包5斤且重量准确，水果包用低值耐存品种，主食包用标准包装工业品。",
     "evidence": [
      "E5",
      "E6",
      "E7",
      "E8",
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "主张收货时抽查样本并宜邀请两家以上供应商配货、按结果修改次日订单分配比例；收货后组织人力或志愿者分发到门栋、或放门前“敲门即走”由居民自取以避免大规模外出，物业可按订购量收额外服务费。",
     "evidence": [
      "E11",
      "E12"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "主张动员业委会组织热心业主志愿者接受下单、配送培训并在楼栋群指导、转交售后；对无子女帮助的老人或困难户可征集志愿者电话询问、代下单。",
     "evidence": [
      "E13",
      "E14"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "列出团购主要挑战：居民反复询问单价数量库存；途径瞬息万变致居民频繁改单、造成人力记录压力；缺少严谨简洁的服务约定致误解纠纷，损耗志愿者热情与公信力。",
     "evidence": [
      "E15",
      "E16",
      "E17"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "说明规则思路为高度限制交易灵活性，以降低服务成本、提高效率、压缩沟通必要性、减少订单复杂度与争议风险。",
     "evidence": [
      "E18"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "列出《基本规则》：一口价、按套餐不接受增减定制、订单不可撤销、超时未领取视作捐赠、须先发短信作收货凭证、配送原则上次日可延迟、疫情结束仍未配送可凭短信退款、只服务名单内用户、不建议超能力吸纳成员。",
     "evidence": [
      "E19",
      "E20",
      "E21",
      "E22",
      "E23",
      "E24",
      "E25"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "主张组建团队并给出分工：负责人掌资金、必要时垫付、对外联络货源并对纠纷负最终责任；物资采购需资质与授权；另设物资分装、配送管理、后台管理、社区/物业外协员、买菜群沟通负责人。",
     "evidence": [
      "E26",
      "E27"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "认为居民习惯高体贴消费而可能以嘲讽等语言暴力表达不满，志愿者又自认应得额外尊重却属业余临时人员，落差会对志愿服务人员造成严重心理冲击。",
     "evidence": [
      "E28"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "主张负责人须及时干预：随时准备退款并解除语言攻击者资格（须礼貌）、打预防针、多招客服、优先保障志愿者家庭、积累话术手册；条件许可下设专人接手难接待客户、录制短视频。",
     "evidence": [
      "E29",
      "E30",
      "E31",
      "E32",
      "E33",
      "E34",
      "E35"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "给出套装设计准则：最大重量不宜超5公斤、宜固定重量；不宜加次级包装（便于客户自行消毒）；不宜多易碎成分；单套价格宜200元内；应提供廉价与轻加工套装（优先困难人士）；可考虑糖尿病人套装、按品类或冷藏设计。",
     "evidence": [
      "E36",
      "E37",
      "E38",
      "E39",
      "E40",
      "E41"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "quoted_or_cited",
     "attribution": "cited_source",
     "modality": "asserted",
     "statement": "作者注明“套装设计的经典方案”摘抄自某大型商超方案，并列出肉食套A/B/C、蔬菜套、水果套、水产套、大厨房商品套餐、主食套等组合。",
     "evidence": [
      "E42",
      "E43"
     ]
    }
   ],
   "argument_steps": [
    "缘起：武汉部分地区商超停止接受个人采购，紧急追加物业+商超规模化供应方案（P001、P002）。",
    "第一套方案流程：定量极简套装（P005）、限时表单（P006）、每周两次及例外（P007）、口粮包标准与分装交付（P008）、口粮包组合规格（P011-P015）、抽查与两家以上供应商（P016）、分发到门栋或门前（P017）、业委会与志愿者（P018）、困难户代下单（P019）。",
    "第二套方案先列挑战（P022-P026），再说明限制交易灵活性的规则思路（P027）与《基本规则》（P028-P038），并给出群公告与短信范本（P068-P083）。",
    "团队分工（P039-P047）与成员心理建设及干预手段（P048-P059）；订单系统方案：微信群接龙（推荐）与番茄表单（P060-P064）。",
    "套装设计准则（P084-P095），并以某大型商超经典套餐清单作示例（P096-P150）。"
   ],
   "concept_usage": [
    {
     "term": "标准口粮包（居民标准口粮供应包）",
     "meaning": "蔬菜包+蛋白质包+水果包+主食包组合、按固定重量分装的定量供应单元，由生鲜经营人员采购分装后交付物业。",
     "evidence": "P008",
     "ambiguity": "各包品种与重量在文中为“建议/一般要求”，非强制标准。"
    },
    {
     "term": "套装/套餐",
     "meaning": "内容与价格固定、不可增减定制的供应单元（2-3个固定套装、一口价）。",
     "evidence": "P029",
     "ambiguity": "“套装”“套餐”“标准包”混用。"
    },
    {
     "term": "高度限制交易灵活性",
     "meaning": "作者自述的规则设计思路：牺牲交易灵活性以降低服务成本、提高效率、减少沟通与争议。",
     "evidence": "P027",
     "ambiguity": "为作者自述思路，未给出适用边界或反例。"
    },
    {
     "term": "敲门即走",
     "meaning": "按清单把货放到居民门前、敲门后离开，由居民自取，避免大规模外出。",
     "evidence": "P017",
     "ambiguity": "未说明错领处置（范本另有超时未领取视作捐赠）。"
    }
   ],
   "examples_and_targets": [
    "武汉市部分地区要求商超停止接受个人采购需求：方案缘起背景，未给来源，待外部核查（P002）。",
    "物业、业委会、社区、志愿者、生鲜经营人员/附近蔬菜销售商家：方案中的组织主体与角色（P005-P019、P040-P047）。",
    "番茄表单、简道云：作者推荐并呼吁开发模板的在线表单服务（P035、P064）。",
    "微信群接龙与哔哩哔哩视频教程：作者推荐的订单收集方式及教程（P060-P062）。",
    "某大型商超方案：作者标注的摘抄来源，未具名（P097）；套餐清单与范本含“（时限）”等占位符（P098-P150、P068、P074、P081）。"
   ],
   "conditions": [
    "缘起条件：鉴于武汉部分地区已要求大型商超停止接受个人采购需求（P002）。",
    "例外条件：原则上每周供应两次，没赶上的居民除非有特殊困难情况，否则请下次预约（P007）。",
    "条件性干预：如果条件许可，另设专人接手难接待客户、录制小视频（P058、P059）。",
    "条件性退款：如直至疫情结束仍未配送，买家可凭确认短信请求退款（P036、P075）。",
    "限量机制：达到当天最大接单数量时以修改密码停止接单（P077）。",
    "语气限定：大量“建议/宜/一般/原则上/不宜/不建议”表明多数条款为参考方案而非强制（P009、P016、P038、P086-P095）。",
    "自我限定：标题自注“待完善”表明该节未定稿（P084）；背景为新冠疫情下的武汉，未写具体日期。"
   ],
   "rhetoric_and_tone": "操作手册/方案书体：分节标题、条目清单、祈使与流程句，大量“建议/宜/不宜/原则上”使语气为建议而非命令；兼有对外用户公告范本（敬语“请您留意”“请慎重确认”）、视频教程与在线表单指引及“待完善”自注。",
   "unresolved_questions": [
    "正文与 lexical 结构差异：登记 1 处 text_has_content_not_in_lexical（P062，位置 2599）及“lexical 独有约 6794 字”；逐节点核对后 150 个结构节点文本均连续出现在 text 中、覆盖全部 4354 字符（未覆盖 107 字符为换行），疑为容器与子项重复的度量差，待结构侧复核。",
    "P061-P062、P064 提到的视频教程与“视频设置指南”只有标题/指引，视频内容未被记录，无法阅读。",
    "“摘抄自某大型商超方案”未具名来源，无法核查（P097）。",
    "“武汉市部分地区已经开始要求大型商超停止接受个人采购需求”为作者陈述，未给来源，需外部核查（P002）。",
    "作者身份、所属机构与方案的实际执行情况，本文未说明。",
    "群公告范本中的“（时限）”“xxxxxxx”等为占位符，实际填写内容未给出（P074、P081）。",
    "标题注明“待完善”，方案是否为最终版本、是否分多次更新，正文未说明（P084）。",
    "P004 等列表容器段落与 P005-P019 等子项文本逐条重复（生成器按 lexical 展开），同一内容在段落序列中出现两次。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P002",
     "quote": "已经开始要求大型商超停止接受个人采购需求",
     "relation": "context"
    },
    {
     "key": "E2",
     "paragraph_id": "P005",
     "quote": "每户按人口构成定量供应，只能选择要或者不要",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P006",
     "quote": "开放下单的窗口时间不宜是深夜",
     "relation": "qualifies"
    },
    {
     "key": "E4",
     "paragraph_id": "P007",
     "quote": "除非有特殊困难情况",
     "relation": "qualifies"
    },
    {
     "key": "E5",
     "paragraph_id": "P008",
     "quote": "由生鲜经营人员大批量采购",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P011",
     "quote": "标准口粮包建议为蔬菜包+蛋白质包+水果包+主食包组合。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P012",
     "quote": "设计总量为5斤一包",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P013",
     "quote": "鱼肉蛋奶包要求重量准确、质量保证。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P014",
     "quote": "水果包一般要求为香蕉、蜜桔、苹果",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P015",
     "quote": "主食包一般要求采用标准包装的工业产品组合。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P016",
     "quote": "宜同时邀请两家以上的供应商参与配货",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P017",
     "quote": "敲门即走，由居民自行收取",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P018",
     "quote": "动员业委会组织小区热心业主组成志愿者",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P019",
     "quote": "由志愿者电话询问需求、代替ta们下单。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P024",
     "quote": "居民反复询问单价数量和库存问题。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P025",
     "quote": "频繁修改需求和取消订单",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P026",
     "quote": "严重损耗志愿服务人员的热情与公信力。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P027",
     "quote": "高度限制交易灵活性以降低服务成本",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P030",
     "quote": "一口价，不可议价。",
     "relation": "supports"
    },
    {
     "key": "E20",
     "paragraph_id": "P032",
     "quote": "订单一旦提交成功，将不允许撤销和修改。",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P033",
     "quote": "视作买家将该份货品无偿捐赠",
     "relation": "supports"
    },
    {
     "key": "E22",
     "paragraph_id": "P034",
     "quote": "需要先发送指定格式的短信作为收货凭证",
     "relation": "supports"
    },
    {
     "key": "E23",
     "paragraph_id": "P036",
     "quote": "买家可以凭确认短信请求退款",
     "relation": "supports"
    },
    {
     "key": "E24",
     "paragraph_id": "P037",
     "quote": "原则上只对特定名单内的用户服务。",
     "relation": "supports"
    },
    {
     "key": "E25",
     "paragraph_id": "P038",
     "quote": "不建议团购组织者超能力的吸纳团购成员",
     "relation": "supports"
    },
    {
     "key": "E26",
     "paragraph_id": "P041",
     "quote": "必要时垫付资金，对外联络货源",
     "relation": "supports"
    },
    {
     "key": "E27",
     "paragraph_id": "P045",
     "quote": "后台管理人员一名，要求熟悉电脑操作",
     "relation": "supports"
    },
    {
     "key": "E28",
     "paragraph_id": "P050",
     "quote": "对志愿服务人员会有严重的心理冲击",
     "relation": "supports"
    },
    {
     "key": "E29",
     "paragraph_id": "P051",
     "quote": "组织的负责人需要高度重视",
     "relation": "supports"
    },
    {
     "key": "E30",
     "paragraph_id": "P053",
     "quote": "解除发动语言攻击的会员的资格",
     "relation": "supports"
    },
    {
     "key": "E31",
     "paragraph_id": "P054",
     "quote": "提前对志愿服务人员打好预防针",
     "relation": "supports"
    },
    {
     "key": "E32",
     "paragraph_id": "P055",
     "quote": "多招募一些直接负责客服的志愿者",
     "relation": "supports"
    },
    {
     "key": "E33",
     "paragraph_id": "P056",
     "quote": "优先保障志愿者家庭的供应。",
     "relation": "supports"
    },
    {
     "key": "E34",
     "paragraph_id": "P057",
     "quote": "尽快积累话术手册",
     "relation": "supports"
    },
    {
     "key": "E35",
     "paragraph_id": "P059",
     "quote": "如果条件许可，可以录制小视频",
     "relation": "supports"
    },
    {
     "key": "E36",
     "paragraph_id": "P087",
     "quote": "套装方案最大重量不宜超过5公斤",
     "relation": "supports"
    },
    {
     "key": "E37",
     "paragraph_id": "P088",
     "quote": "不宜再加次级包装",
     "relation": "supports"
    },
    {
     "key": "E38",
     "paragraph_id": "P090",
     "quote": "单套价格宜在200元范围内为宜",
     "relation": "supports"
    },
    {
     "key": "E39",
     "paragraph_id": "P091",
     "quote": "应提供廉价套装",
     "relation": "supports"
    },
    {
     "key": "E40",
     "paragraph_id": "P092",
     "quote": "应提供轻加工（仅需加热消毒即食熟食）为主的套装",
     "relation": "supports"
    },
    {
     "key": "E41",
     "paragraph_id": "P093",
     "quote": "可以考虑提供针对糖尿病患者的套装",
     "relation": "supports"
    },
    {
     "key": "E42",
     "paragraph_id": "P097",
     "quote": "（摘抄自某大型商超方案）",
     "relation": "context"
    },
    {
     "key": "E43",
     "paragraph_id": "P098",
     "quote": "肉食套A",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "公共卫生应急",
    "社区治理",
    "生鲜供应与物流",
    "志愿服务管理"
   ],
   "issue_candidates": [
    "疫情期间小区蔬菜采购组织",
    "物业与商超规模化供应",
    "社区团购规则设计",
    "志愿者心理建设与纠纷处理",
    "订单收集工具",
    "标准套装设计"
   ],
   "text_function_candidates": [
    "方案/操作指南",
    "经验总结",
    "答疑"
   ],
   "object_candidates": [
    "武汉市",
    "大型商超",
    "物业",
    "业委会",
    "志愿者",
    "番茄表单",
    "简道云",
    "微信群接龙"
   ],
   "working_keywords": [
    "标准口粮包",
    "套装/套餐",
    "敲门即走",
    "一口价",
    "接龙",
    "高度限制交易灵活性",
    "特困人士"
   ]
  },
  "notes": "正文无图片节点，故标 read。已按简报 3.1 压缩（合并同类主张、缩短短引），未删减证据定位与未决问题。正文含 lexical 容器与子项重复（如 P004 覆盖 P005-P019），系生成器展开；已登记 1 处 text/lexical 差异（P062）及“lexical 独有约 6794 字”，逐节点核对未见正文缺失。"
 },
 "e42be94f": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么大家对网上的求助信息都无动于衷呢？”。作者没有回答这一“为什么”，而是从自身经历出发（P001：最近帮助转发了一些紧急求助信息，感到当事人方寸已乱），给出求助信息撰写与传播的六条沟通要点（P002-P027）：准确描述所需帮助、联络方式的选择、注明时效、终止求助的信号机制、制成图片防篡改、以及不建议悬赏的自我让步。P003 以“求免疫血浆”为例，指向疫情语境（出版日期 2020-02-20），但正文未点明疫情。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "写作缘起：作者近期帮助转发紧急求助信息，感到当事人方寸已乱，为便于其制作转发信息并更有效率地获得帮助，写下沟通要点。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002", "P003"],
     "summary": "要点一：必须准确、有效、严谨描述所需的具体帮助，以压缩无效信息比例、提高有效信息被看到的几率；以求助免疫血浆为例，须注明血型、输血地点、输血方式与献血资格，否则条件不匹配的献血者来电会妨碍有效信息传递、耽误获救速度与机会。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"],
     "summary": "要点二：除非有专门志愿者使用多座席自动转接的呼叫中心系统，否则最好不要用电话，改用微博号、微信号、qq号、邮箱号，或用多个电话小号；作者判求助人用自己手机是错误，并说明无效信息涌入占线、妨碍号码对外沟通（医院、救护来电同样生死攸关）、求助人心理脆弱无力重复应答等理由；建议留电子邮件或由志愿帮助者用闲置电话承担联络，闲置号可用阿里小号等虚拟号绑定自有号码自助实名开通，各大运营商也有此类业务。",
     "role": "action_advice"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P009", "P010", "P011"],
     "summary": "要点三：要准确注明时效（年月日时）；否则求助信息经连锁传播后可能早已时过境迁仍在自行流传，甚至可能流传十年之久，新接收者误以为是眼下的事而发起新转发，对求助人形成长期困扰。",
     "role": "action_advice"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P012", "P013", "P014", "P015"],
     "summary": "要点四：如果有条件，最好给出终止该求助的信号机制；道义上对帮助者负有给 closure 的责任，实用上也可避免长期困扰；机制可设计为给出微博地址并置顶一条微博或在签名中注明，便于他人转发前查证是否已解决。",
     "role": "action_advice"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023"],
     "summary": "要点五：制作成图片，既有利于转发，也有利于防篡改；作者列举篡改现象（为取乐、有其他目的、拷贝粘贴时漏删、自认原文不准确或手误而自行增删修改），并强调关键信息不应分叉出不准确的衍生版本，图片也便于他人准确转发。",
     "role": "action_advice"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P024", "P025", "P026", "P027"],
     "summary": "要点六：理智地说不建议悬赏或许以重谢；理由是悬赏利于增加线索数量但会大大降低质量（有人先打电话问清、甚至产生幻觉拿不存在的线索赌运气），且会削弱部分人的帮助意愿（“既然悬赏了，想必会有很多人帮ta吧”）；但悬赏能给绝望中的求助者心理安慰，故这一条不强劝。",
     "role": "action_advice"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张求助信息一定要准确、有效、严谨地描述所需的具体帮助，以压缩无效信息比例、提高有效信息被看到的速度和几率。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以求助免疫血浆为例，主张必须注明血型、输血地点、输血方式以及献血资格，否则条件不匹配的献血者来电会妨碍有效信息传递、耽误获救速度与机会。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“除非有专门的志愿者使用多座席自动转接的呼叫中心系统帮助处理来电”为例外条件，主张最好不要使用电话作为联络方式，可改用微博号、微信号、qq号、邮箱号；若仍觉得电话最好，推荐使用多个电话小号。",
     "evidence": ["E4"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为求助人在情急之下用自己的手机作为求助信息联络方式是一个错误。",
     "evidence": ["E5"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出的理由：会有大量无效信息涌入（记者问新闻线索、自媒体挖材料）造成占线，既影响接到有效信息的几率，又妨碍该号码的对外沟通，而医院、救护的电话同样生死攸关；求助人此时心理压力巨大、脆弱紧张，无力应对一轮轮重复应答。",
     "evidence": ["E6"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者主张更好的办法是留下电子邮件；若嫌邮件不够直接，最好请志愿帮助者用不涉及重要用途的闲置电话承担联络；有可能最好多留几路电话以加大单位时间接听量。",
     "evidence": ["E7"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称闲置号码并不难获得，例如阿里小号提供收快递用的虚拟号码，与原有号码绑定即可自助实名认证和立刻开通，各大运营商也有此类业务可在官方 app 中查找。",
     "evidence": ["E8"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张求助信息要准确注明时效（年月日时）；否则可能在事情早已时过境迁后仍在自行流传，甚至流传十年之久并被误认为是眼下的事而再次转发，对求助人形成长期困扰。",
     "evidence": ["E9", "E10", "E11"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者主张如果有条件，最好给出一个终止该求助的信号机制：道义上对出手帮助的人负有给 closure 的责任，实用上也可避免长期困扰。",
     "evidence": ["E12", "E13", "E14"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出终止机制的具体设计：给出一个微博地址并置顶一条微博，或在签名中明确注明，使他人转发前可循链接查证事情是否已解决，避免转发无效信息、无谓占用自己和朋友的资源。",
     "evidence": ["E15"]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张把求助信息制作成图片，因为既有利于转发，也有利于防篡改。",
     "evidence": ["E16"]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称确实存在篡改求助信息的现象，动机包括取乐、有其他目的、拷贝粘贴时漏删，以及自认为原文不准确或手误而替人增删修改。",
     "evidence": ["E17", "E18", "E19"]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为关键信息不应分叉出不准确的衍生版本，因此有必要直接制成不易篡改的图片，且图片也便于他人准确转发。",
     "evidence": ["E20", "E21"]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“理智地说”为限定，不建议悬赏或许以重谢。",
     "evidence": ["E22"]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称实践证明悬赏虽非常有利于增加线索数量，但会大大降低线索质量，重赏之下有人先打电话问清楚、甚至产生幻觉拿不存在的线索赌运气；悬赏还会削弱部分人的帮助意愿。",
     "evidence": ["E23", "E24"]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者让步：悬赏毕竟能在现实意义上给绝望中的求助者带来重要的心理安慰，所以这一条不强劝。",
     "evidence": ["E25"]
    }
   ],
   "argument_steps": [
    "说明写作缘起：帮转求助信息时发现当事人方寸已乱，故写下沟通基本要点（P001）。",
    "要点一：准确、有效、严谨描述所需帮助；以免疫血浆求助须注明血型、地点、方式、献血资格为例（P002、P003）。",
    "要点二：先给例外条件（有专门志愿者使用多座席自动转接呼叫中心）再给建议（不用电话、改用网络账号或多路小号）（P004）。",
    "判断“用自己的手机”是错误（P005），并给出占用线路与心理负担两方面理由（P006）。",
    "给出替代方案：留电子邮件、由志愿帮助者用闲置电话、多留几路电话（P007）；说明闲置号码的获取途径（P008）。",
    "要点三：注明时效（P009）→ 未注明的后果是信息在时过境迁后仍自行流传、甚至流传十年并引发新转发（P010、P011）。",
    "要点四：有条件时给出终止求助的信号机制（P012）→ 道义理由（给 closure）（P013）与实用理由（避免长期困扰）（P014）→ 具体做法（微博置顶或签名注明）（P015）。",
    "要点五：制作成图片（P016）→ 说明确实存在篡改现象及四类动机（P017-P021）→ 结论是避免关键信息分叉出不准确版本并便于准确转发（P022、P023）。",
    "要点六：不建议悬赏（P024）→ 质量下降与帮助意愿削弱两重理由（P025、P026）→ 让步：悬赏有心理安慰作用，故不强劝（P027）。"
   ],
   "concept_usage": [
    {
     "term": "时效",
     "meaning": "指求助信息应注明的年、月、日、时等时间信息，使接收者能判断事情是否仍在当下。",
     "evidence": "P009",
     "ambiguity": "文中未规定具体格式或更新频率。"
    },
    {
     "term": "终止该求助的信号机制",
     "meaning": "让转发者能查证求助是否已经解决的机制（如微博置顶、签名注明），以便停止转发。",
     "evidence": "P012",
     "ambiguity": "作者称“如果有条件”最好给出，未说明无条件时的替代做法。"
    },
    {
     "term": "closure",
     "meaning": "文中英文词，指给帮助过自己的人一个“此事已了结”的交代。",
     "evidence": "P013",
     "ambiguity": "作者未给出定义，仅以道义责任的方式使用。"
    },
    {
     "term": "无效信息/有效信息",
     "meaning": "条件不匹配、占用来电线路或妨碍传播的信息；反之则是能推进获救的信息。",
     "evidence": "P002",
     "ambiguity": "判定标准由求助者事先描述决定，文中未给一般规则。"
    },
    {
     "term": "电话小号/闲置电话/虚拟号码",
     "meaning": "不承担重要用途、可多路并用的联络号码（如阿里小号提供的收快递用虚拟号码）。",
     "evidence": "P008",
     "ambiguity": "作者称“就我所知”，未给出版本或时效信息。"
    },
    {
     "term": "悬赏/许以重谢",
     "meaning": "以报酬换取线索的做法，作者不建议使用，但承认其心理安慰作用。",
     "evidence": "P024",
     "ambiguity": "“实践证明”未给出来源；何种金额或形式属悬赏未界定。"
    }
   ],
   "examples_and_targets": [
    "求免疫血浆的求助信息：作者举例（须注明血型、输血地点、输血方式、献血资格），指向疫情语境（P003）。",
    "新闻记者与自媒体：作者所述会打进电话问新闻线索、挖材料的无效来电者（P006）。",
    "医院、救护的电话：作者用于对照说明号码不可被占用的例子（P006）。",
    "阿里小号：作者举例的虚拟号码服务（收快递用），可绑定自有号码自助实名开通（P008）。",
    "各大运营商的官方 app：作者提及可查找同类业务（P008）。",
    "微博号、微信号、qq号、邮箱号：作者建议的联络方式（P004、P007）。",
    "微博置顶微博/签名注明：作者举例的终止求助机制（P015）。",
    "篡改求助信息者：作者所述的四类情形（取乐、有其他目的、拷贝粘贴漏删、自认修正）（P018-P021）。"
   ],
   "conditions": [
    "P004 以“除非有专门的志愿者使用多座席自动转接的呼叫中心系统帮助处理来电”为不使用电话的例外条件。",
    "P004 “如果仍然觉得电话号码最好，推荐使用多个电话小号”。",
    "P007 “如果实在嫌电子邮件不够直接，也最好请某个志愿的帮助者使用一个不涉及重要用途的闲置电话”。",
    "P007 “如果有可能，最好干脆多留几路电话，以便加大单位时间的接听量”。",
    "P012 以“如果有条件”限定终止信号机制的建议。",
    "P010 “在某些情况下甚至可能流传十年之久”为可能性表述，非已核事实。",
    "P024 “理智地说”与 P027 “所以这一条不强劝”构成作者对第六条建议的自我限定。",
    "P017 “也许你难以相信”表明作者预期读者对篡改现象的怀疑。",
    "语境：文中以“求免疫血浆”“疫情”相关场景出现（P003），但正文未点明具体疫情与时间。"
   ],
   "rhetoric_and_tone": "实用指南与规劝体：编号分条（1）至 6））、先给结论再给理由、密集使用“一定要/最好/不建议/推荐/可以”等建议性措辞；以第二人称“你”直接对求助者说话，语气体谅（“方寸已乱”“情急之下来不及多想”）而非指责；用“举个例子”“实践证明”“就我所知”引出例证与经验；末条主动让步（“不强劝”），并预判读者怀疑（“也许你难以相信”）。",
   "unresolved_questions": [
    "提问问“为什么大家对网上的求助信息都无动于衷”，正文未回答该问题本身，而是转向求助信息的撰写建议，问答对应关系需研究者判断。",
    "作者近期帮助转发的具体求助信息、求助人、事件与时间均未点名（P001 仅称“一些紧急求助信息”）。",
    "“实践证明”未给出来源或数据，悬赏对线索质量的影响需外部核查（P025）。",
    "阿里小号与各运营商虚拟号码业务的具体状态需外部核查，且与文章写作时点（2020 年 2 月）相关（P008）。",
    "P010 “甚至可能流传十年之久”为可能性表述，无法核验。",
    "正文建议“制作成图片”，但本记录中无图片节点，作者所述图片本身不在语料内。",
    "作者身份、所帮助转发的渠道（微博或其他平台）本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "最近我帮助转发了一些紧急求助信息，感觉到发送这些信息的当事人方寸已乱", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "一定要准确、有效、严谨的描述你所需要的具体帮助", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一定要注明血型、输血地点、输血方式以及献血资格", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "除非有专门的志愿者使用多座席自动转接的呼叫中心系统帮助处理来电，否则最好不要使用电话作为联络方式。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P005", "quote": "很多求助人在情急之下来不及多想，就用自己的手机作为求助信息的联络方式。这是一个错误。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "因为一定会有大量的无效信息涌进来（有新闻记者打进来问新闻线索的，有自媒体打进来挖材料的），大量占线。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "更好的办法是留下电子邮件。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "比如阿里小号就有提供收快递用的虚拟号码，只需要和自己的原有号码绑定就可以实现自助实名认证和立刻开通。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "3）要准确注明时效。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "如果自己身上没有注明年月日时，你会发现很可能事情早已时过境迁，这条求救信息却还在自行流传。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "这很可能对求助人形成一种长期的困扰。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "4）如果有条件，最好给出一个终止该求助的信号机制。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P013", "quote": "你有一定的道义责任要给ta们一个closure", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "其次，从纯粹实用的角度来说，也应该有一个终止的信号机制，以免出现上面说过的长期困扰。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "这个机制也不难设计，比如给出一个微博地址，然后置顶自己的一条微博，或者在自己的签名中进行明确的注明。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "5）制作成图片，既有利于转发，也有利于防篡改。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "的确存在一些篡改求助信息的现象。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "有的人仅仅只是拷贝粘贴的时候选少了一些字或者误删除了一些字。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "有的人是自己觉得你说得不够准确或者自己觉得信息的某部分肯定是手误写错了，自己帮你增删修改了部分内容。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "但无论如何，你不会希望这么关键的信息分叉出一些不准确的衍生版本。所以，有必要直接制成不是那么容易篡改的图片。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "做成图片，也很有利于大家方便而准确无误的帮你转发。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "6）理智地说，不建议悬赏或者许以重谢。", "relation": "qualifies"},
    {"key": "E23", "paragraph_id": "P025", "quote": "实践证明，悬赏虽然非常有利于增加线索的数量，但是会大大的降低线索的质量。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "悬赏在某种意义上会削弱部分人对你的帮助意愿", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P027", "quote": "但悬赏毕竟能够在现实意义上给绝望中的求助者带来一些重要的心理安慰，所以这一条不强劝。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["公共卫生应急", "网络传播与信息管理", "社会救助/公益"],
   "issue_candidates": ["求助信息如何撰写", "联络方式的选择", "求助时效与终止信号", "信息防篡改", "悬赏的利弊"],
   "text_function_candidates": ["指南/建议", "经验总结", "答疑（未回答所问）"],
   "object_candidates": ["求助者（ta们）", "志愿者", "新闻记者", "自媒体", "阿里小号", "运营商", "微博", "微信", "qq", "医院", "救护"],
   "working_keywords": ["免疫血浆", "电话小号", "closure", "终止信号机制", "时效", "悬赏", "防篡改"]
  },
  "notes": "正文无图片节点。问答存在错位：提问问旁观者为何对求助信息无动于衷，正文实为写给求助者的信息撰写建议，已在 unresolved_questions 登记。brief 字段为正文摘录，仅作导航。"
 },
 "6ee1126a": {
  "analysis": {
   "question_context": "提问者（Q001）问“集体主义和个人主义矛盾吗？”。作者仅以两段作答：先给出一般化判断“所有的主义都和所有的其他主义矛盾”（P001），再以反问“不然怎么叫主义？”收束（P002）。正文未出现“集体主义”“个人主义”二词，也未针对提问所举的两种主义作专门回答。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "直接给出一般化判断：所有的主义都和所有的其他主义矛盾。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002"],
     "summary": "以反问“不然怎么叫主义？”收束，未展开定义、理由或例证。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：所有的主义都和所有的其他主义矛盾。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者以反问“不然怎么叫主义？”收束，暗示相互矛盾是“主义”之所以为主义的特征（原句为反问，未展开论证）。",
     "evidence": ["E2"]
    }
   ],
   "argument_steps": [
    "直接给出一般性判断：所有的主义都和所有的其他主义矛盾（P001）。",
    "以反问“不然怎么叫主义？”作结，未给出定义、前提、例证或条件（P002）。"
   ],
   "concept_usage": [
    {
     "term": "主义",
     "meaning": "本文只在“彼此矛盾”这一点上使用该词，并以反问暗示相互矛盾是其构成特征；未给出定义。",
     "evidence": "P001",
     "ambiguity": "判断范围不明：是否包括非政治性“主义”、是否指一切主义之间必然矛盾，本文未说明。"
    },
    {
     "term": "矛盾",
     "meaning": "文中作为“主义之间”的关系词使用，未说明是逻辑矛盾、立场冲突还是实践冲突。",
     "evidence": "P001",
     "ambiguity": "“矛盾”的含义与判定标准本文未界定。"
    },
    {
     "term": "集体主义/个人主义",
     "meaning": "提问者所问的两个词，正文未出现、未使用。",
     "evidence": "P001",
     "ambiguity": "作者是否认为二者属于其所说的“主义”并相互矛盾，本文未说明。"
    }
   ],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "极简作答：一句断言加一句反问（“不然怎么叫主义？”），带口语化反问与不容置疑的断言语气，未展开论证；全文仅 26 字。",
   "unresolved_questions": [
    "正文未直接回答“集体主义和个人主义是否矛盾”，只给出“所有的主义都和所有的其他主义矛盾”的一般论断。",
    "“主义”在本文中未被定义，判断范围（是否包括一切主义、是否必然矛盾）不明。",
    "正文未给出任何例证、理由或限定条件，无法判断作者是否主张排除了例外情形。",
    "正文仅 26 字（2 段），是否为完整回答、是否存在更早/更晚版本，需版本侧复核；语料 provenance/superseded 均为 null。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "所有的主义都和所有的其他主义矛盾。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不然怎么叫主义？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学/意识形态"],
   "issue_candidates": ["集体主义与个人主义是否矛盾", "“主义”的界定"],
   "text_function_candidates": ["简答", "反问式评论"],
   "object_candidates": [],
   "working_keywords": ["主义", "矛盾", "集体主义", "个人主义"]
  },
  "notes": "正文仅 26 字、2 段，无图片节点；本记录按现有 text 全文填写，未据提问补写集体主义/个人主义的具体论述。正文未出现平台话题标签。"
 }
}  # noqa: E501


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
