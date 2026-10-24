# -*- coding: utf-8 -*-
"""批次 r001-b0097 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0097.sessions.py            # 写 out/r001-b0097.out.jsonl
  python3 records/r001-b0097.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0097"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0097.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "1b4bff20": {
  "analysis": {
   "question_context": "提问者（Q001）问：家父有藏书五万本，应该怎么处理这笔资源。作者不评价该问题本身，直接给出取舍标准与执行细则（P001—P002 起以“值得传代”为分类轴）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "传代标准一：与个人命运深刻关联者作家族史文物；建议令尊写个人史，重在留原始史料而非史论。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "标准二：与时代历史相连的经典文献与原件，主张其长远必然增值。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "标准三：心血所寄的艺术品、限量制作与签名本类藏品。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036"], "summary": "永久藏书的成本与保存条件：恒湿、避光、防虫、防尘、防火、防借，故规模须精选。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042"], "summary": "不值得传代但仍于人有益者：或卖、或捐、或送，并给出分工标准。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "“有资格的人”的定义与世家之好的构建；把辨识这样的人本身当作一项工作。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P054", "P055"], "summary": "两个短标题句，未展开。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与个人命运深刻关联、影响过自己人生观价值观的书可作家族史文物传代，附个人笔记者尤甚。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为子孙立言是祖辈能为子孙做的最重要的事，超过留下亿万家财。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为子孙立言应是留下可供总结的基本资料，而非个人版成功密码；只给总结而不给论据与前提，传下去的是会引来灾难的教条。", "evidence": ["E004", "E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "带原始史料的个人编年史比“祖训”更重要；没有史料的史论是剥夺子孙自由的束缚。", "evidence": ["E007"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "与时代历史相连的经典文献可作传代标准；作者以“如果你们打算让家族永久流传”为前提断言这类财富远期收益必然可收获。", "evidence": ["E008", "E009", "E010"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这类当时随手可得的原件会因同类在时间长河中纷纷消逝而无限增值，非孤本亦因互证价值成为无价之宝。", "evidence": ["E011", "E012"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术品类藏书（限量制作、心血所寄、签名本等）可考虑保留。", "evidence": ["E013", "E014"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "划入永久藏书要慎之又慎，因保存有恒湿、避光、防虫、防尘、防火、防借等成本与占地，规模须尽可能精选。", "evidence": ["E015", "E016", "E017"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "永久藏书绝不允许以任何理由外借，故“办私人图书馆”不适用于这批永久私人藏书。", "evidence": ["E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不值得传代但仍于人有益者不应在藏者手里湮灭，须为其寻求更好的保管者；低价值过时破损者卖、有参考价值而品相好者捐、有收藏价值而不合主题者郑重相赠。", "evidence": ["E019", "E020", "E021", "E022"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“有资格的人”指同样懂得并打算如此规划自己人生和家族财富、懂得礼物之重与价值之人；受赠并记录下来即构建永恒的家族关系与个人关联。", "evidence": ["E023", "E024"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "两个有永续传承之心而在思想上屡有关联的家族，若行正道则必然举足轻重、不易倾覆。", "evidence": ["E025"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“前途不可限量”不是指聪明、考试成绩好或工作光鲜，而是对这种深谋远虑的人生自觉的准确评价。", "evidence": ["E026", "E027"]},
    {"claim_id": "C014", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以“新冠这件事，你留下了些什么？”设问，未给答案。", "evidence": ["E028"]}
   ],
   "argument_steps": [
    "先立分类轴：值得传代的妥善保存（P001）。",
    "给出传代标准一（个人命运关联）并引申出撰写个人史的建议（P003—P005）。",
    "以三不朽为框架，论证为子孙立言人人力所能及且为祖荫首要（P007）。",
    "界定“为子孙立言”=留原始史料，反对只留结论式祖训（P008—P010）。",
    "给出标准二（时代文献）并举海湾战争、911、08金融风暴、新冠为例（P012—P017）。",
    "以原件必然消逝推出必然增值（P019—P021）。",
    "给出标准三（艺术品与签名本）（P023—P026）。",
    "转向成本：慎入永久藏书，列恒湿、避光、防虫、防尘、防火、防借六项保存要求（P027—P036）。",
    "给出不值得传代者的处理：卖、捐、送（P037—P042）。",
    "界定受赠资格、世家之好与辨识人才的价值（P043—P053）。"
   ],
   "concept_usage": [
    {"term": "传代", "meaning": "在家族内永久保存并传承，区别于仅保存或变卖", "evidence": "P001", "ambiguity": "未给判断的量化标准"},
    {"term": "为子孙立言", "meaning": "客观记录自己的实际轨迹、留下可供子孙总结的基本资料，而非讲个人版成功密码", "evidence": "P008", "ambiguity": "与《左传》三不朽的“立言”用法未必等同"},
    {"term": "史料／史论", "meaning": "史料=原始资料，史论=总结性论断；作者主张前者优先", "evidence": "P010", "ambiguity": "无"},
    {"term": "永久藏书", "meaning": "划入永久保存、不外借、需专门设施与家风教育的那批书", "evidence": "P027", "ambiguity": "与“私人图书馆”明确区分（P034）"},
    {"term": "世家之好", "meaning": "两家在精神与思想上相互影响、以赠书与个人史料为线索的永续家族关系", "evidence": "P045", "ambiguity": "未说明如何维持"}
   ],
   "examples_and_targets": [
    "家父藏书五万本（提问者提供的情境，P001/Q001）",
    "《起居注》《食货志》（类比，P008）",
    "“不可如何、理当如何”的“祖训”（被批评的对照物，P010）",
    "海湾战争、911、08金融风暴、新冠（作者所举应当留证的例子，P014—P017）",
    "倾尽一生手绘的鸟类图鉴与限量装帧制作（作者举例，P024）",
    "签名本与早年作品（作者举例，P026）",
    "“莫欺少年穷”“奇货可居”“前途不可限量”（修辞用语，P050—P052）"
   ],
   "conditions": [
    "以“值得传代的标准”为前提展开三分类（P002）",
    "“如果你们打算让家族永久流传”，远期收益才“必然可以收获”（P021）",
    "“如果你现在要开始收藏这类作品”，须先懂鉴赏且与志趣相合（P025）",
    "永久藏书需恒湿设备、避光、防虫、防尘、防火、防借等条件与占用空间（P028—P035）",
    "受赠者限于“有资格的人”（P042—P043）",
    "两个家族须“行的是正道”才不易倾覆（P046）"
   ],
   "rhetoric_and_tone": "训诫与经验指导为主，第二人称“你”直接给出执行标准；用“慎之又慎”“实为祖荫之首要”“奇货可居”等文言化、夸张化措辞；多处反问（“新冠这件事，你留下了些什么？”）；结尾两个短标题句（P054、P055）突兀收束，未展开。",
   "unresolved_questions": [
    "本篇含 3 个图片节点（IMG001—IMG003），图片内容未核验，需人工/多模态复核",
    "P054“如将溺之人在激流中寻找浮木。”与 P055“会浪费人时间的，不再视为书籍，而视为物料使用。”为两个未展开的标题句，其指代对象与行文位置（是否属本文或系其他答案片段）不明",
    "“立功、立德、立言，为三不朽”未注明出处（通常溯至《左传》），需外部核查",
    "海湾战争、911、08金融风暴的举例为作者主张，未给数据或文献，属待外部核查的事实性叙述",
    "正文未说明五万本藏书的具体类型，分类建议如何落地无法确定"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P003", "quote": "与个人命运有深刻关联，影响过自己的人生观、价值观的，可以作为家族史的文物传代。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "这其中，尤以附有个人笔记的为甚。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P011", "quote": "是一个祖辈能为子孙做的最重要、最有价值的事，超过留下亿万家财。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "不是要去总结自己的一生体会、去讲一个个人版的成功密码", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "则传下去的与其说是经验，不如说是将来必定会引来灾难的教条。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "绝不意味着在子孙的年代还是正确的", "relation": "qualifies"},
    {"key": "E007", "paragraph_id": "P010", "quote": "没有史料的史论，不足以称为一份增进子孙自由的礼物，反而成为一种剥夺子孙自由的束缚。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P012", "quote": "与时代历史紧密相连的、可以作为历史史料的经典文献。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P018", "quote": "也同样是活的、真的历史文献", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P021", "quote": "如果你们打算让家族永久流传，那么这份财富的远期收益是必然可以收获的", "relation": "qualifies"},
    {"key": "E011", "paragraph_id": "P019", "quote": "在未来必定会因为同类在无限的时间长河中必然的纷纷消逝而无限的增值", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P020", "quote": "同样会因为有互相验证的价值而成为无价之宝", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P023", "quote": "艺术品，心血所寄。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P024", "quote": "所制作出来的限量发行实物，可以考虑保留", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P027", "quote": "划入永久藏书要慎之又慎。这类东西并不是没有成本的。", "relation": "qualifies"},
    {"key": "E016", "paragraph_id": "P036", "quote": "所以永久藏书的规模要尽可能精选，慎而又慎。", "relation": "qualifies"},
    {"key": "E017", "paragraph_id": "P035", "quote": "这些设施都是要成本的，也要占地，而且需要子孙后代的相应的家风教育。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P034", "quote": "绝不允许以任何理由外借", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P038", "quote": "不应该在你手里湮灭，应该保持在人类手中", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P040", "quote": "低价值的，过时了的，有过大破损的，尽量卖。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P041", "quote": "不值得长期付出保存成本、但品相仍然良好的，尽量捐。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P042", "quote": "择有资格的人，或加签、或用印、或题字，郑重相赠。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P043", "quote": "那些同样懂得和打算这样规划自己人生和家族财富的人", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P044", "quote": "实际上是构建永恒的家族关系和个人关联", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P046", "quote": "如果行的是正道，想不举足轻重都很困难", "relation": "qualifies"},
    {"key": "E026", "paragraph_id": "P049", "quote": "不是指你多聪明，考试考得多好，找了份多光鲜的工作", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P050", "quote": "是对这种深谋远虑、至于无极的人生自觉不偏不倚、毫无恭维的准确评价而已", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P017", "quote": "新冠这件事，你留下了些什么？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家族传承", "藏书与文献保存", "人生规划"],
   "issue_candidates": ["藏书处置", "个人史与家族史料", "文物级藏品的保存条件", "赠书与世家交往"],
   "text_function_candidates": ["答疑", "经验总结", "行动建议", "训诫"],
   "object_candidates": ["提问者的父亲", "子孙后代", "有资格受赠者", "出版社与装帧设计师"],
   "working_keywords": ["传代", "为子孙立言", "史料", "史论", "永久藏书", "世家之好", "奇货可居"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 3 个图片节点（IMG001—IMG003），图片内容未经核验，需图像核验；已读部分为正文文本 P001—P055 全文。P054、P055 两个标题句未展开，指代不明，已登记待人工判断。"
 },
 "df5ca875": {
  "analysis": {
   "question_context": "提问者（Q001）问“越南未来能成为像日韩这样的发达国家吗？”。作者未预测越南前景，而是改写提问所用概念的界定方式，未点名越南与日韩任何一方。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以英文原文界定“发达国家”为“已发展国家”，并称其判断线相对稳定、客观。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "区分“已发展国家”与“世界排名”，指出迟早所有国家都会成为已发展国家，排位属于另一组概念。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“发达国家”的原文是 developed country，即“已发展国家”，其判断有一根相对稳定的客观线，不是简单按收入划分。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是不是已发展国家与一个国家的“世界排名”没有必然关系。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "迟早有一天，地球上所有的国家都会变成已发展国家。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与排位相关的是“先进/落后国家”“优势国家”“主导国家”这类概念，与“已发展国家”不同。", "evidence": ["E005"]}
   ],
   "argument_steps": [
    "先回到词源，把“发达国家”还原为“已发展国家”（P001）。",
    "给出该判断依据的性质：相对稳定的客观线，非收入单一标准（P002）。",
    "切断“已发展国家”与“世界排名”的必然联系（P003）。",
    "预言所有国家迟早都会成为已发展国家（P004）。",
    "把排位问题归给另一组概念（P005）。"
   ],
   "concept_usage": [
    {"term": "发达国家／已发展国家", "meaning": "developed country 的直译，指已完成发展这一状态，作者称其有一根相对稳定的客观线", "evidence": "P001", "ambiguity": "作者未说明这条“客观线”的具体指标"},
    {"term": "世界排名", "meaning": "国家之间的排序，作者认为与是否已发展没有必然关系", "evidence": "P003", "ambiguity": "未说明排名的口径"},
    {"term": "先进/落后国家、优势国家、主导国家", "meaning": "作者认为与排位相关的概念群，用以替换提问中的比较框架", "evidence": "P005", "ambiguity": "未逐一定义"}
   ],
   "examples_and_targets": [],
   "conditions": [
    "“迟早有一天”标示为预测性判断，不是当下事实（P004）",
    "“不是简单按收入来划分”为对常见划分法的限定（P002）"
   ],
   "rhetoric_and_tone": "极简的词典式答复，无例证、无数据、无寒暄，五段近乎定义与推论；以“其实”“迟早”缓和断言。",
   "unresolved_questions": [
    "作者所称“相对稳定的客观线”具体是什么，正文未说明",
    "“迟早有一天”未给时间范围，也未说明依据，需外部核查",
    "本篇未回应提问者的越南、日韩个案，故不能据此推断作者对越南前景的判断",
    "brief 结尾“跟排位有关系的是“先进/落后”被截断，属导航字段不完整，不影响正文"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "发达国家 的原文是 developed country —— 已发展国家。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "这是有一根相对稳定的客观线的，不是简单按收入来划分的。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "其实与一个国家的“世界排名”没有必然关系", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "迟早有一天，地球上所有的国家都会变成已发展国家。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "跟排位有关系的是“先进/落后国家”，“优势国家”，“主导国家”这类概念。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["发展经济学", "国际政治"],
   "issue_candidates": ["发达国家的界定", "国家排名与发展阶段之辨"],
   "text_function_candidates": ["答疑", "概念澄清"],
   "object_candidates": ["发达国家", "发展中国家", "越南", "日本", "韩国"],
   "working_keywords": ["developed country", "已发展国家", "世界排名", "先进/落后国家"]
  },
  "notes": "无图片，图片核验不适用；正文 P001—P005 全读完，status=read、full_text_checked=true。全文仅 158 字符，未涉及越南与日韩个案，提问者立场未归给作者。"
 },
 "6e68f889": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何有效的制怒？”（且用“有效”暗示求方法）。作者不接受这一提问框架，先论“没有爱就没有制怒的根本必要”，并把制怒落到罪责归属与以身相代上；文中“有人问‘为什么是徒然’”是作者自设的追问（P009）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "两条前言式建议：生活在爱你的人中间，不向对你无爱的人发怒。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "不要把发怒看作正义的表现；流行的“我喜欢的我才爱”不是爱。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "不以爱为念的制怒是徒然：受怒者的识怒能力远胜制怒者的伪装，否认发怒者多是想免罪。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022", "P023"], "summary": "真正制怒=从根上斩断怒的源头，须以身相代，且必须视为本分而非功劳。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "罪责归因的推演：天意无可罪，人选了ta人故不能强求；一切怒的立场消解，遂无怒可生。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040"], "summary": "反问是否愿意以身替罪；只有出于“不合逻辑”的原因才做得到，爱不符合那个逻辑。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生活在爱你的人中间，发怒的后果常会被自然消解。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要向对你无爱的人发怒：这不仅是无用和有害的问题，最重要的是无爱的人不配得。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要把发怒看成一种正义的表现，不要以为被激怒就说明自己在正义一方。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们总以为自己正义、发怒是对方罪有应得，而事实绝大多数情况下不如ta们所料。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "“爱不受挑衅，不轻易发怒。”作者引为论据，未注明出处。", "evidence": ["E005"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "流行的“我喜欢的、对我有利的我才爱”不是爱；人们其实喜欢的只有自己，所谓喜欢别人大多是喜欢别人喜欢自己。", "evidence": ["E006"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "没有爱就没有制怒的根本必要；叶公好龙式的“制怒需求”不足以支撑真正制怒所需的决绝。", "evidence": ["E007", "E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不以爱为念、不以爱人为必须尽的义来谈“制怒”只是徒然，那只是看风色的技巧与假装无怒的伪装术。", "evidence": ["E009"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "受怒者若没有随时识别他人可能在发怒的观察力是致命的；制怒者三心二意的伪装敌不过受怒者拿命练出的识怒能力。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "竭力否认发怒的人“大部分”是想让对方知错能改，同时免掉自己发火、施压、强迫人的罪名。", "evidence": ["E013"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正制怒要从根上斩断怒的源头，需要剜心剖腹般的决绝，并接受自己变得与绝大多数人不同。", "evidence": ["E014", "E015"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "制怒的根本之道不是把罪定在别人身上再自我制止“行刑”，而是【以身相代】。", "evidence": ["E016"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "罪加于人的制怒是自欺欺人；唯一真正有效的手段是把罪归于自己以身相代，且必须视为毫无功劳的本分，不能出于骄傲或成圣的渴望。", "evidence": ["E017", "E018"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "令人沮丧的事常有无数环节取决于人力无法改变的天意，而天意无可罪；剩下的他人责任依附于你对ta人的选择，你不能强求人做到一切“不应该做错”的事。", "evidence": ["E019", "E020"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "承诺未做到按契约该追偿就追偿，但作为自己签订契约并界定违约责任的一方，作者以反问质疑“我”责怪对方未履约的立场。", "evidence": ["E021"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要你想，一切罪责（亦即发怒的立场）要么可归于天，要么可归于你自己；天无可罪，故“万方有罪，罪在朕躬”，向自己发怒也因“人不如神理所当然”而消解。", "evidence": ["E022", "E023", "E024"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "怒的立场消解后便无怒可生、自然无怒待制，这是真正制怒唯一的出路。", "evidence": ["E025"]},
    {"claim_id": "C018", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以“割肉喂鹰、以身饲虎……你愿意做吗？”设问，未给答案。", "evidence": ["E026"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要不想做，世界会提供一千一万条理由说“不做是正义的”；顺着那套“逻辑”，人类会被理直气壮的报复毁灭。", "evidence": ["E027", "E028"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱不符合那套“逻辑”。", "evidence": ["E029"]}
   ],
   "argument_steps": [
    "先给两条前提式建议：在爱你的人中间、不向无爱的人发怒（P001—P002）。",
    "否定“发怒=正义”，指出人高估自己的正义（P003—P004）。",
    "引“爱不受挑衅，不轻易发怒”为准则（P005）。",
    "重新界定爱，否定“我喜欢的我才爱”（P006）。",
    "由“没有爱就没有制怒的根本必要”推出流行制怒需求是撒娇式的（P007）。",
    "以受怒者的识怒能力说明不以爱为念的制怒是徒然（P008—P013）。",
    "用否认发怒的对话与“不讲武德”说明否认者的动机（P014—P017）。",
    "定义真正制怒=斩断源头，需决绝与接受非常态（P018—P019）。",
    "提出罪责的存在是发怒的前提（P020）。",
    "给出根本之道：不以罪加于人而以身相代，且视为本分（P021—P023）。",
    "指出这单靠人自己做不到（P024）。",
    "以天意、他人的责任依附于你的选择、强求人成为神三层推演消解罪责（P025—P030）。",
    "引“万方有罪，罪在朕躬”，并消解自责（P031—P033）。",
    "结论：无怒可生，自然无怒待制（P034）。",
    "以愿否以身替罪的反问与“爱不符合那个逻辑”收束（P035—P040）。"
   ],
   "concept_usage": [
    {"term": "制怒", "meaning": "作者区分两种：流行的“管理愤怒”式制怒（被判为徒然）与从根上斩断怒的源头（真正制怒）", "evidence": "P018", "ambiguity": "同一词在文中两种含义并用"},
    {"term": "爱", "meaning": "不以“我喜欢的、对我有利的”为标准的爱；作者称无爱则无制怒的根本必要", "evidence": "P006", "ambiguity": "未给正面定义，主要以否定式说明"},
    {"term": "受怒者／识怒狂魔／生存狂", "meaning": "被发怒者面对的一方，作者称其因“练不好就会死”而具备极强的识怒能力", "evidence": "P011", "ambiguity": "“生存狂”一词未界定，是否为特定群体不明"},
    {"term": "【以身相代】", "meaning": "把罪归于自己、自己承担，且视为毫无功劳的本分与理所应当的义务", "evidence": "P022", "ambiguity": "方括号为原文所有，用法带有术语化与宗教色彩"},
    {"term": "天意", "meaning": "人力无法改变的环节，作者称其无可罪", "evidence": "P025", "ambiguity": "未说明其范围"},
    {"term": "契约／违约补偿", "meaning": "被用来说明“自己界定了违约责任的一方无立场责怪对方未履约”", "evidence": "P029", "ambiguity": "此处为类比，非法律论述"}
   ],
   "examples_and_targets": [
    "“老虎不发威，会被别人当病猫”（作者举的流行心态，被批评，P007）",
    "“叶公好龙式的撒娇式的‘制怒需求’”（作者的贬称，P007）",
    "刀术／盾术的对比（类比，P011）",
    "“你瞎说，我哪有！？”的对话场景（作者设想的反驳并加以回应，P014—P015）",
    "“年轻人不讲武德，这好吗？这不好。”（网络流行语式引用，P017）",
    "“割肉喂鹰、以身饲虎”（宗教典故式类比，P035）",
    "“万方有罪，罪在朕躬”（引语，未注明出处，P031）"
   ],
   "conditions": [
    "“若真要制怒，你就要接受非常态”（P019）",
    "“往往客观上有待定的‘罪责’存在”中的“往往”为概率限定（P020）",
    "以身相代“不能是出于骄傲、出于成圣的渴望，必须是视为毫无功劳的本分”（P022）",
    "“常常有无数的环节其实非人之罪”中的“常常”为概率限定（P025）",
    "“只要你不想”与“只有你出于……一定要这样做，你才做得到”构成条件句（P036、P037）",
    "受怒者的观察能力被表述为“没有……那可是致命的”的假设性后果（P010）"
   ],
   "rhetoric_and_tone": "训诫与反问为主，夹杂讽刺与网络调侃（“叶公好龙式的撒娇式的‘制怒需求’”“年轻人不讲武德”）；以第二人称“你”直指读者；大量使用军事与身体隐喻（刀术／盾术、识怒狂魔、剜心剖腹、割肉喂鹰、以身饲虎）；结论带有宗教式决绝与“唯一的出路”式排他断言；结尾“幸亏如此”短句收束。",
   "unresolved_questions": [
    "本篇无图片节点，图片核验不适用",
    "“爱不受挑衅，不轻易发怒。”（P005）与“万方有罪，罪在朕躬”（P031）均未注明出处，属待核查的引文来源",
    "“这单靠人自己是做不到的”（P024）之后并未说明人靠什么才能做到，文中未补充（是否指向信仰或恩典，正文未说明）",
    "“受怒者”“识怒狂魔”“生存狂”是否指特定群体或仅修辞，正文未说明",
    "P029 以契约与违约补偿类比人际关系，作者未说明该类比适用于何种关系（雇佣、婚姻等）",
    "brief 第 1 条与正文 P001—P002 对应，但正文未出现“第一”的编号而以“第二”起（P003），编号不一致，属结构疑点"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "生活在爱你的人中间，这样你发怒的后果常会被自然消解。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "最重要的是无爱的人不配得", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "不要把发怒看成是一种正义的表现", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "其实事实绝大多数情况下都不如ta们所料", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "爱不受挑衅，不轻易发怒。", "relation": "context"},
    {"key": "E006", "paragraph_id": "P006", "quote": "而这根本不是爱", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "没有爱，就没有制怒的根本必要", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "根本不足以支撑真正的制怒所需要的那种剜心剖腹般决绝", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "谈“制怒”只是徒然而已", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "那可是致命的", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "怎么可能那么容易胜过那些知道“练不好就会死”的受怒者们拿命别在裤腰带里练的盾术？", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P013", "quote": "根本就是赤裸裸写在脸上的", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P016", "quote": "大部分是想要对方“知错能改”", "relation": "qualifies"},
    {"key": "E014", "paragraph_id": "P018", "quote": "也就是从根上斩断怒的源头，要的是一种剜心剖腹般的决绝", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P019", "quote": "你就要接受非常态", "relation": "qualifies"},
    {"key": "E016", "paragraph_id": "P021", "quote": "而是【以身相代】", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P022", "quote": "就是将罪归于自己，自己以身相代", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P022", "quote": "必须是视为毫无功劳的本分，理所应当的义务", "relation": "qualifies"},
    {"key": "E019", "paragraph_id": "P025", "quote": "而天意无可罪", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P026", "quote": "你不能强求人做到一切“不应该做错”的事", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P029", "quote": "“我”有立场去责怪对方没能履约吗？", "relation": "qualifies"},
    {"key": "E022", "paragraph_id": "P030", "quote": "要么可以归于天，要么可以归于你自己", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P031", "quote": "天无可罪，是以万方有罪，罪在朕躬。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P032", "quote": "人不如神，不是理所当然吗？", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P034", "quote": "无怒可生，自然无怒待制。这是真正制怒唯一的出路。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P035", "quote": "你愿意做吗？", "relation": "context"},
    {"key": "E027", "paragraph_id": "P036", "quote": "世界为你准备了一千一万条理由告诉你不做是正义的", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P038", "quote": "人类会被一切“理直气壮的报复”毫无悬念的毁灭", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P039", "quote": "爱不符合那个逻辑。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "道德修养", "宗教思想"],
   "issue_candidates": ["愤怒的控制", "正义感与自我辩护", "罪责归属与以身相代"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "劝诫"],
   "object_candidates": ["制怒者", "受怒者", "生存狂", "易怒者", "年轻人"],
   "working_keywords": ["制怒", "以身相代", "剜心剖腹", "识怒", "天意", "罪在朕躬", "爱"]
  },
  "notes": "无图片，图片核验不适用；正文 P001—P040 全读完，status=read、full_text_checked=true。提问者的“如何有效制怒”未被作者直接采纳，作者重新界定“制怒”并否定流行版本，提问者立场未归给作者。P014“——“你瞎说，我哪有！？””为作者设想的对方反驳并随即回应，按文中对话材料记录，未归为作者主张。P005、P031 两处引语未注明出处，已登记待外部核查。正文出现“第二”而无“第一”，编号不连续，已在 unresolved_questions 登记。"
 },
 "2afb5f2f": {
  "analysis": {
   "question_context": "提问者（Q001）问“有哪些经典的法律漏洞？”。作者不给案例清单，而是自设一个思想实验（特异功能/未知科技凝视杀人）并连续反问，最后点明该设定真正描述的是法律是否应承认“巫术杀人”概念。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"], "summary": "思想实验设定：能力者凝视五秒致人死亡，证据俱全并被公诉，庭上又瞪死陪审团成员。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "机制完全不可检出与说明，被告拒绝自证其罪、实验室测试全失败，事件可被解释为惊人巧合。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019"], "summary": "连续追问：怎么判、能否放出去、凭什么处决、在完全遵循并允许修订法律的前提下如何解决、这样的人是否绝不会出现。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "点明主题是法律是否应承认“巫术杀人”这一“准事实”，并给出非洲/南美洲巫术信念下自卫杀人的难题。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "以“白化病谋杀”为现实表现形式，称其正在实际发生，并引联合国大会文件（文件本体未随正文呈现）。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者设定一个假设：某人拥有未知优势或科技，只要默想特定数字并凝视目标五秒即可致其死亡。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "设定中不存在任何已知物理、化学、生物、电磁技术能检出其杀人机制，属“真 · 认知鸿沟”。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "设定中被告拒绝自证其罪，且测试结果失败，故事件也可被解释为“惊人的巧合”。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以“这位要怎么判？”“这位能放出去吗？”“凭什么？”等连续设问提出难题，未给答案。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的提问条件限定为：不许用栽赃诬陷、监禁事故等手段作弊，须在完全、积极遵循法律甚至允许修订法律的前提下靠法律解决。", "evidence": ["E009"]},
    {"claim_id": "C006", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者追问“这样的人，真的是无论人类如何发展，都绝不会出现的吗？”未给答案。", "evidence": ["E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个思想实验的主题，是法律是否应该承认“巫术杀人”概念；其设定真正描述的是一种机制不明、无法以科学方法确切认定为事实的“准事实”。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者报告事实：在非洲和南美洲，人们确实普遍相信巫术的存在，个人是否认同不是问题、关键是当事人自己确实认同。", "evidence": ["E012"]},
    {"claim_id": "C009", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者提出问题：当非洲部落居民确信被下诅咒、以杀死对方为唯一自救方式而杀人，是否应被视为正当防卫？并强调此时该国大部分国民确实相信这种巫术。", "evidence": ["E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“白化病谋杀”是该现象的一种典型表现形式。", "evidence": ["E015"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个问题绝不是什么架空幻想，而是现在正在实际发生的问题。", "evidence": ["E016"]}
   ],
   "argument_steps": [
    "以“给一个思考题你们来考虑考虑”开篇（P001）。",
    "设定特异功能/未知科技与凝视五秒致死的机制（P002—P003）。",
    "补足事实要件：时间、地点、动机俱全，并有录像（P004—P005）。",
    "推进情节：检察官公诉、被告在法庭上再杀人（P006—P007）。",
    "排除已知科学的解释路径，称为认知鸿沟（P008—P010）。",
    "加入被告拒绝自证其罪与测试失败，使巧合解释成立（P011—P013）。",
    "抛出一连串追问（P014—P019）。",
    "点题：主题是法律是否承认“巫术杀人”，“准事实”概念（P020）。",
    "以非洲、南美洲的巫术信念与部落自卫杀人问题把假设转为现实议题（P021—P023）。",
    "以白化病谋杀与联合国大会文件收束（P024—P027）。"
   ],
   "concept_usage": [
    {"term": "法律漏洞", "meaning": "提问者所用标题词；作者未直接定义，而是以“无法可依的处置难题”呈现", "evidence": "P017", "ambiguity": "作者未使用“法律漏洞”一词界定自己的问题"},
    {"term": "巫术杀人", "meaning": "机制不明的、无法以科学方法确切认定为事实的杀人方式，作者主张问题主题在于法律是否应承认该概念", "evidence": "P020", "ambiguity": "作者未给出承认或不承认的立场，仅提出问题"},
    {"term": "准事实", "meaning": "机制不明、无法以科学方法确切认定为事实的“事实”", "evidence": "P020", "ambiguity": "原文以引号标注，未进一步定义"},
    {"term": "真 · 认知鸿沟", "meaning": "作者用来形容人类完全无法理解其机制的处境", "evidence": "P010", "ambiguity": "网络化措辞，非学理定义"},
    {"term": "正当防卫", "meaning": "在巫术信念之下以杀人为自救的情形是否可归入该法律概念，作者以设问提出", "evidence": "P022", "ambiguity": "作者未表明立场"},
    {"term": "白化病谋杀", "meaning": "作者称为该现象的一种典型表现形式", "evidence": "P024", "ambiguity": "正文未说明其定义与具体案情"}
   ],
   "examples_and_targets": [
    "假设中的特异功能者/掌握未知科技者（作者自设的思想实验主体，P002—P003）",
    "检察官公诉与法庭上瞪死陪审团成员（作者虚构的情节，P006—P007）",
    "费马大定律（作者类比，实指费马大定理，原文作“费马大定律”，P009）",
    "“栽赃诬陷”“监禁事故”式作弊手段（作者预先排除的做法，P017）",
    "非洲和南美洲的巫术信念（作者举出的现实情形，P021）",
    "非洲部落居民因确信被下诅咒而杀人的假设情形（作者提出的问题，P022）",
    "白化病谋杀与联合国大会文件（作者举出的现实问题与材料，P024—P027）"
   ],
   "conditions": [
    "“假设，某人真的有某种特异功能——或者ta掌握了某种人类没有掌握的……科技”为全篇假设前提（P002）",
    "“只要在心里持续默想一串特定的数字，然后朝目标凝视五秒”为能力生效条件（P003）",
    "“在完全的、积极的遵循法律的前提下，甚至允许你修订法律的前提下”为提问条件（P017）",
    "“你个人是否认同不是问题，关键是人家自己确实认同”为讨论巫术问题的条件（P021）",
    "“在此信念之下”与“此时该部落国家的大部分国民都确实相信存在这种巫术”为自卫问题的前提（P022—P023）"
   ],
   "rhetoric_and_tone": "思辨式、悬置结论的提问体：全文大量使用反问与第二人称“你/你们”（“那么，这位要怎么判？”“凭什么？”），以虚构情节推演到极端；用词带有网络化调侃（“真 · 认知鸿沟”“淡定自若”）；末段以联合国文件标题收束，正文未附文件内容。",
   "unresolved_questions": [
    "本篇无图片节点，图片核验不适用",
    "作者抛出“怎么判”“能不能放出去”“凭甚么处决”“怎么办”等一连串追问后未给任何答案，本文未说明作者的结论",
    "作者称“看看这个联合国大会文件”，但正文只出现文件标题（P027），文件本体不在正文中，属材料缺失，需外部核查",
    "P027“联合会大会：白化病谋杀问题”带“⚠lexical未覆盖片段”标记，且“联合会大会”疑为“联合国大会”之误（原文如此），文本与结构存在分歧，需人工核对",
    "“白化病谋杀”的具体案情与统计数据正文未给出，需外部核查",
    "P009 将“费马大定理”写作“费马大定律”，是否为笔误需核对原文（原文如此，未改写）"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "假设，某人真的有某种特异功能", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "只要在心里持续默想一串特定的数字，然后朝目标凝视五秒，目标就会死", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P008", "quote": "没有任何已知的物理、化学、生物、电磁……技术能检测到ta到底是怎么做到的", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P010", "quote": "真 · 认知鸿沟。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P011", "quote": "而且很显然，这位也拒绝自证其罪。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P013", "quote": "于是，这一切也可以被解释为一种“惊人的巧合”。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P014", "quote": "那么，这位要怎么判？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P016", "quote": "你能有什么理由？凭什么？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P017", "quote": "在完全的、积极的遵循法律的前提下，甚至允许你修订法律的前提下", "relation": "qualifies"},
    {"key": "E010", "paragraph_id": "P018", "quote": "真的是无论人类如何发展，都绝不会出现的吗？", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P020", "quote": "是法律是否应该承认“巫术杀人”概念", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P021", "quote": "人们确实普遍相信巫术的存在", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P022", "quote": "这是否应该被视为一种正当防卫行为？", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "该部落国家的大部分国民都确实相信存在这种巫术", "relation": "qualifies"},
    {"key": "E015", "paragraph_id": "P024", "quote": "就是“白化病谋杀”问题", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P025", "quote": "而是现在正在实际发生的问题", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["法理学", "刑法", "科学与法律的关系", "人类学"],
   "issue_candidates": ["法律漏洞", "机制不明行为的可罚性", "巫术信念与正当防卫", "白化病谋杀"],
   "text_function_candidates": ["答疑", "思辨提问", "论辩", "举例"],
   "object_candidates": ["特异功能者（假设）", "检察官", "陪审团", "非洲部落居民", "联合国大会"],
   "working_keywords": ["巫术杀人", "准事实", "认知鸿沟", "白化病谋杀", "正当防卫"]
  },
  "notes": "无图片，图片核验不适用；正文 P001—P027 全读完，status=read、full_text_checked=true。本篇为提问体，作者只提出问题与设定，未给出结论，故 main_claims 中凡属追问者记为 open_question，不得推定为作者立场。P017 的“作弊”排除条款属作者自设的答题条件，按 qualified 记录。语料记录标 divergence=true（P027 为 lexical 未覆盖片段），已登记。"
 },
 "b38dcebe": {
  "analysis": {
   "question_context": "提问者（Q001，立场属提问者）问：印度都敢这样了，我们为什么不主动出击？这是主战/强硬主张式设问，预设对方已然挑衅、我方应当主动出手。作者完全不承接该问题，也不给时政判断或政策主张，而是以一个《圣斗士星矢》的桥段/网络梗作答：黄金圣斗士最令人恐惧的时候不是拿出光速拳狠揍星矢的时候，而是天马彗星拳、星云锁链、曙光女神、庐山升龙霸齐上、富士山都打塌之后，沙加仍打坐闭眼、眉头微皱地说“谁tm这么吵，还让不让人睡了。nnd明天不要上班啊都。”——即把“主动出击”的热闹比作打上门去的喧闹，而把真正令人恐惧的一方放在不动声色、被打扰的一方。末尾以“不要问我是谁，我是希瑞。”自嘲式收束。正文极短（180 字符）且为调侃文体，作者未明确指认沙加或五小强对应哪一方，立场只能判为“以梗回避正面回答”，不得据以推定作者对中印局势的主张。本篇含 1 个图片节点（IMG001），图片内容未经核验，正文与图片的衔接关系（P006“侵删”、P007“的这个时候。”）无法完全确定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "以《圣斗士星矢》作比：最令人恐惧的不是拿出光速拳把星矢往死里揍之时，而是众招齐发、富士山都打塌之后沙加仍打坐闭眼、眉头微皱。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005"], "summary": "引沙加台词，其反应是嫌吵和要上班，而非出手。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "“侵删”“的这个时候。”两处孤立残句，疑为图片标注或文本截断。", "role": "other"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "以“不要问我是谁，我是希瑞。”自嘲式收束，未作正面论述。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以《圣斗士星矢》桥段作比：黄金圣斗士最令人恐惧的时候不是拿出光速拳把星矢往死里揍的时候，而是众招齐发、富士山都打塌之后沙加仍打坐闭眼、眉头微皱的时候。", "evidence": ["E001", "E002", "E003", "E004"]},
    {"claim_id": "C002", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "所引《圣斗士星矢》角色沙加的台词（被引角色话语，非作者判断）：谁tm这么吵，还让不让人睡了。nnd明天不要上班啊都。", "evidence": ["E005"]}
   ],
   "argument_steps": [
    "以“黄金圣斗士最令人恐惧的时候”起句，先排除“拿出光速拳狠揍星矢”这一项（P001—P002）。",
    "以“而是”给出所选项：五小强绝招齐发、富士山打塌、庐山瀑布倒流等极端热闹之后，沙加仍打坐闭眼、眉头微皱（P003—P004）。",
    "以沙加台词点出他的反应是嫌吵与要上班（P005）。",
    "以“侵删”“的这个时候。”两处残句过渡（P006—P007）。",
    "以“不要问我是谁，我是希瑞。”自嘲收束，未回到提问者的时政设问（P008）。"
   ],
   "concept_usage": [
    {"term": "最令人恐惧的时候", "meaning": "本文特指对手用尽大招仍不能撼动、而此方不动声色的时刻", "evidence": "P001—P004", "ambiguity": "未明示对应现实中的哪一方，需读者自行映射"},
    {"term": "光速拳/天马彗星拳/星云锁链/曙光女神/庐山升龙霸", "meaning": "借《圣斗士星矢》招式名铺陈“打上门去”的热闹场面", "evidence": "P002—P003", "ambiguity": "本文未作解释，属外部动漫典故"},
    {"term": "沙加", "meaning": "被引动漫角色，本文借其“打坐闭眼、眉头微皱”的姿态表达不动声色", "evidence": "P004—P005", "ambiguity": "其在本文中的喻指对象未说明"},
    {"term": "希瑞", "meaning": "结尾自称（出自动画角色名），属自嘲式署名/梗", "evidence": "P008", "ambiguity": "未说明自称用意"}
   ],
   "examples_and_targets": [
    "《圣斗士星矢》桥段（作者类比/修辞材料，P001—P005）",
    "沙加的台词（被引角色话语，P005）",
    "“侵删”（借用图片的标注式残句，P006）",
    "“不要问我是谁，我是希瑞。”（自嘲式收束，P008）",
    "提问者的“印度都敢这样了，我们为什么不主动出击？”（提问者立场，作者未正面回应）"
   ],
   "conditions": [
    "全篇以动漫比喻成立为前提，作者未给出把比喻映射到时事的明示条件或对象。",
    "“最令人恐惧”的判定依赖“对方用尽手段而此方不为所动”这一情境（P002—P004）。",
    "P006“侵删”表明文本与图片存在借用关系，图片内容未核验。"
   ],
   "rhetoric_and_tone": "极短篇，通篇用动漫梗与招式名并列铺陈（用加号连缀五个招式），以角色台词和自称“希瑞”作冷幽默收束；对提问者的强硬设问不作正面表态，也不展开论证；口语与拼音缩写（tm、nnd）并用，语气调侃。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001），图片内容未核验，需人工/多模态复核；图片与正文的衔接关系不明。",
    "作者未明示沙加与五小强分别对应现实中的哪一方，其对提问者主战立场的态度只能判为未作正面回答，不得据此推定其政治立场。",
    "P006“侵删”、P007“的这个时候。”为孤立残句，其归属与位置（是否属本篇或系他处片段）不明。",
    "提问者所称“印度都敢这样了”指涉的具体事件，正文未说明，需外部核查。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "黄金圣斗士最令人恐惧的时候，", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "不是最后光速拳都拿出来把星矢往死里揍的时候。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "富士山都打塌了，庐山瀑布都倒流了", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "沙加打坐闭着眼，眉头微皱——", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "谁tm这么吵，还让不让人睡了。nnd明天不要上班啊都。", "relation": "context"},
    {"key": "E006", "paragraph_id": "P006", "quote": "侵删", "relation": "context"},
    {"key": "E007", "paragraph_id": "P008", "quote": "不要问我是谁，我是希瑞。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["时政（提问语境）", "网络文化/动漫梗"],
   "issue_candidates": ["对印强硬/主动出击主张（提问者提出）", "以动漫梗代替正面表态"],
   "text_function_candidates": ["调侃", "以比喻代答", "叙事（借用动漫情节）"],
   "object_candidates": ["印度（提问者提及）", "沙加", "星矢", "紫龙", "阿瞬", "一辉", "希瑞", "黄金圣斗士"],
   "working_keywords": ["黄金圣斗士", "光速拳", "天马彗星拳", "庐山升龙霸", "沙加", "希瑞", "主动出击"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 1 个图片节点（IMG001），图片内容未经核验，故 status=needs_reread、image_checked=false；已读部分为全部正文文本（P001—P008，共 180 字符）。原有 question_context 非空，按接手规则原样保留，仅补全其余字段。作者未对提问者的主战设问作正面表态，main_claims 只登记作者明示的比喻判断与所引角色台词，未把提问者立场或动漫台词归给作者。"
 },
 "39039726": {
  "analysis": {
   "question_context": "提问者（Q001）问：「等于」的严格定义是什么？这是求定义的学理问题，提问者未预设答案。作者给出自己的定义：“等于”的意思是“在待考察的指标上，等号左右的对象无可见区别”，并用天平称重的例子说明（同一台秤无法区分体重都是 100 斤的你和张三，故说二者体重相等），再切换到数学领域解释 A=B。作者随后提出他认为“一般人常忽略”的要点：等于关系只能用于对象的属性（Attribute）而不能用于对象本身（Entity），并补充“entity 本身可以是 attribute”（亲生兄弟的“父亲”属性栏都是隔壁老王，故 A.父亲 = B.父亲）。接着自问自答“难道一个实体就不能直接等于另一个实体吗？”——答案是显然的不能，因为语义已内蕴区分；以两个在基因、颜色、个头乃至每个电子运动状态都完全一致的苹果为例，指出它们的位置属性必然不同；若连空间位置都合并，则关系不再是“相等”而是“是”（A 就是 B，只有“它的两个别称”）。最后以计算机语言中“A == B”（A 与 B 相等）与“A = B”（令 B 成为 A／将 B 赋予 A 之名）作对照，结论是“A 等于 B”与“A 即是 B”是两个概念。立场区分：提问者只要定义，作者给出的是自己的一套界定加论证，不是转述标准教科书定义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "给出“等于”的定义（在待考察指标上无可见区别），以同一台秤无法区分两个体重100斤的人为例，得出“张三的体重与你相等”。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "把表述切换到数学领域：A=B 指 A 的“值”属性与 B 的“值”属性无可见的区分。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "提出作者认为一般人常忽略之点：等于关系只能用于属性（Attribute）而不能用于对象本身。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "限定：entity 本身可以是 attribute，如亲生兄弟的“父亲”属性栏都是隔壁老王，故 A.父亲 = B.父亲。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "自问自答：实体不能直接等于另一实体，因为语意已内蕴区分。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017"], "summary": "思想实验：两个在基因、颜色、个头直到每个电子运动状态都一致的苹果仍是两个，因位置属性必然不一致。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020"], "summary": "假设空间位置也合并，则关系不再是“相等”而是“是”，只有“它的两个别称”。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022"], "summary": "对照计算机语言的 == 与 =，结论：“A等于B”与“A即是B”是两个概念。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“等于”的意思是“在待考察的指标上，等号左右的对象无可见区别”。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "切换到数学领域，A=B 意思是 A 的“值”属性与 B 的“值”属性无可见的区分，即就其数值而言 A 等于 B。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一般人常忽略：“等于”关系只能用于对象的属性，而不能用于对象本身。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "限定：entity 本身可以是 attribute，例如一对亲生兄弟的“父亲”属性栏都是隔壁老王，于是 A.父亲 = B.父亲。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个实体不能直接“等于”另一个实体，因为语意已内蕴这一结果：既称为另一实体，它必定与本实体存在某种区分。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使两个苹果在基因、颜色、个头直到每个电子的运动状态都完全一致，它们仍是两个苹果，因为位置属性必然不一致。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果连空间位置也合并，这种关系就不再是“相等”而是“是”：A就是B，不是“它们相等”，而是只有“它的两个别称”。", "evidence": ["E010", "E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "计算机语言把这两种关系分别表示为“A == B”（A与B相等）和“A=B”（令B成为A／将B赋予A之名）；“A等于B”与“A即是B”是两个概念。", "evidence": ["E012", "E013"]}
   ],
   "argument_steps": [
    "先给定义，再用秤的例子把“无可见区别”具体化（P001—P004）。",
    "把定义平移到数学记号 A=B，指明被比较的是“值”这一属性（P005—P007）。",
    "提出属性／实体（Attribute／Entity）之分，主张等于只适用于属性（P008—P009）。",
    "随即加以限定：entity 本身可以是 attribute，以“父亲”属性栏为例（P010—P012）。",
    "自设问题“实体能否直接等于实体”，答不能，理由是命名本身内蕴区分（P013—P015）。",
    "用两个完全一致的苹果与位置属性作检验（P016—P017）。",
    "以“位置合并则不再是相等而是‘是’”作假设推演（P018—P020）。",
    "以计算机语言的 == 与 = 收束，得出“等于”与“即是”是两个概念（P021—P022）。"
   ],
   "concept_usage": [
    {"term": "等于/相等", "meaning": "在待考察的指标上等号左右的对象无可见区别；作者主张其只适用于属性", "evidence": "P001、P007、P008", "ambiguity": "“可见区别”由谁判定、辨别力门槛未说明"},
    {"term": "属性（Attribute）", "meaning": "被比较的等位属性栏位，如“值”“父亲”", "evidence": "P007、P009、P011", "ambiguity": "未给形式定义"},
    {"term": "实体（Entity）", "meaning": "对象本身；作者先说等于不能用于实体，又限定实体可充当属性值", "evidence": "P008—P011", "ambiguity": "与属性的划分标准未给出"},
    {"term": "是/即是", "meaning": "与“相等”相对的关系，指同一对象的两个别称", "evidence": "P019、P020、P022", "ambiguity": "未与逻辑学中的同一性概念作对照"},
    {"term": "A == B 与 A=B", "meaning": "计算机语言中表示“相等”与“赋值/命名”两种不同关系的记号", "evidence": "P021", "ambiguity": "未说明具体语言，属一般化陈述"}
   ],
   "examples_and_targets": [
    "天平称重（作者例证，P002—P004）",
    "数学记号 A=B（作者例证，P005—P007）",
    "亲生兄弟的“父亲”属性栏都是隔壁老王（作者例证，P011—P012）",
    "两个在基因、颜色、个头、每个电子运动状态都完全一致的苹果（作者思想实验，P016—P017）",
    "计算机语言的 A == B 与 A=B（作者类比，P021）"
   ],
   "conditions": [
    "定义以“待考察的指标”和“评价者”为前提：同一台秤无法区分两个体重100斤的人（P002—P003）。",
    "“无可见区别”依赖观察/评价手段的分辨力，本文未给阈值。",
    "“实体不能等于实体”依赖“既称为另一实体则必存在某种区分”这一语义前提（P015）。",
    "空间位置合并的情形为作者自设的假设推演（P018）。"
   ],
   "rhetoric_and_tone": "定义—举例式讲解，语气平实；用“举个例子”“不过要注意”作过渡，自设一问一答（“难道一个实体就不能直接‘等于’另一个实体吗？”接“答案是显然的不能。”），并以“隔壁老王”一类口语例子带轻微幽默，情绪色彩弱。",
   "unresolved_questions": [
    "“可见区别”的判据与观察者分辨力门槛，正文未说明。",
    "Attribute 与 Entity 的划分标准未给定义；“entity本身可以是attribute”与“等于不能用于对象本身”如何统一，作者只以属性栏举例说明，未形式化。",
    "“语意已经内蕴了这一结果”属命名层面的论据，是否足以排除同一实体的两个名称之间的相等，正文未展开。",
    "本文定义与数学/逻辑中相等（同一性）关系的异同，作者未提及，需外部核查。",
    "无图片，图片核验不适用。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "在待考察的指标上，等号左右的对象无可见区别", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P007", "quote": "A的‘值’这个属性与B的‘值’这个属性无可见的区分", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P007", "quote": "就其数值而言，A等于B", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "“等于”关系只能用于对象的属性，而不能用于对象本身", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P010", "quote": "不过要注意，entity本身可以是attribute。", "relation": "qualifies"},
    {"key": "E006", "paragraph_id": "P012", "quote": "于是 A.父亲 = B.父亲。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P014", "quote": "答案是显然的不能。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P015", "quote": "因为语意已经内蕴了这一结果", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P017", "quote": "它们也仍然是两个苹果，因为苹果A和苹果B的位置属性仍然必然不一致", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P019", "quote": "这种关系就不再是“相等”，而是“是”", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P020", "quote": "不是“它们相等”，而是根本没有“它们”，只有“它的两个别称”了。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P021", "quote": "这两种不同的关系被分别表示为“A == B ”（即“A与B相等”），和“A=B”", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P022", "quote": "“A等于B”，与“A即是B”，是两个概念。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言哲学/逻辑学（定义与同一性）", "数学基础", "计算机语言语义"],
   "issue_candidates": ["“等于”的严格定义", "属性与实体的区分", "相等与“是”（同一）的区别"],
   "text_function_candidates": ["答疑", "定义与举例式讲解", "自问自答式论证"],
   "object_candidates": ["张三（举例）", "隔壁老王（举例）", "两个苹果（思想实验）", "计算机语言（类比对象）", "秤（评价者举例）"],
   "working_keywords": ["等于", "Attribute", "Entity", "可见区别", "等于关系", "A == B", "A=B", "别称"]
  },
  "notes": "无图片，图片核验不适用；正文 P001—P022（779 字符）全读完，status=read。原有 question_context 非空，按接手规则原样保留，仅补全其余字段。作者给出的是自定义界定加论证，不属转述教科书定义；“一般人常忽略”“答案为显然的不能”等均为作者主张。元数据显示 updated_at（2026-02-18）晚于 published_at（2021-02-25），正文是否经后续修订无法由语料判断，已登记。"
 },
 "4a647263": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：为什么有网友说货拉拉跳窗女生是被害妄想症？女性在面对潜在危险时应该如何应对？问题把“货拉拉跳窗女生”事件与网友的“被害妄想症”说法一并带入，并附一个应对方式的求教。作者不讨论案件事实认定，而是先给“被害妄想”划判准，再拒绝“防御性过强”的定性，把问题重述为“只有疑而没有手段和体系”，最后给出以被动式防御为核心的建议；提问者问的性别维度作者未专门展开。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "界定“被害妄想”：界限在威胁行为本身是否真实存在；以举铁锤与双手空空为例，只有臆想不存在之物（尤其幻听幻视幻觉）才算，并以反问排除扩大化用法。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008"], "summary": "在“当事女孩确因观察到可疑迹象而跳车”的假设下讨论，指出只要观察到可疑迹象就已排除“被害妄想”。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015"], "summary": "追问可否归咎“防御性过强”，断言世界上不存在这种问题，无论多强都不为错，劝人降低防御性等于劝人少活两年。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P016", "P017"], "summary": "重述真正的问题：不是多疑或防御，而是只有“疑”却没有对应的手段和体系；该女生因缺少妥当处理手段而出问题。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022", "P023"], "summary": "以战场侦查兵、参谋部、国防军作类比：侦查强预判强国力不强，才采用举国动员式极端反应；不应靠削弱侦查与预判解决。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "指认定性为“被害妄想/防御性过强”即走削弱之路；解释劝说者作为“盟国”不愿支援的动机（增强国力难、且帮出的能力将来是入侵麻烦），代拟其自白后评“这不是傻，这只是不爱罢了”。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P031", "P032", "P033"], "summary": "限定：爱可遇不可求，不懂爱是默认常态；苛求对方之爱则自身之爱何在；随即转向专注自己的问题。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P034", "P035", "P036", "P037"], "summary": "三条行动建议：只能选择加强国防建设；不要怪劝你“不要被迫害妄想”的人；重视不把问题如此定性的人；并转入如何构建防御体系。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "防御体系要点一：打消“不要多想流”的干扰（该前提推不出“人不能多想”）；主体须为被动式而非主动式；低运行成本、低维护是绝对标准。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "要点二：解释“不要多想”话语的来源（自己想的办法实行不了、反致抑郁，故求心情愉快），并反驳说思考防御本身是乐趣，以椰子作比。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P057", "P058", "P059", "P060"], "summary": "结尾以情绪化停顿和后续链接提示收束。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“被害妄想”的基准界限，在于你所推想威胁的行为本身是否真实存在。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基于现实存在的行为或事物推理设想出可能的威胁，只能叫防御性过强；只有臆想出根本不存在的行为和事物（尤其出现幻听、幻视、幻觉）并据此设想威胁，才可称被害妄想。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定把“被害妄想”用在货拉拉当事女生身上：不管其解读是否靠谱，只要观察到了可疑迹象，就已经排除了“被害妄想”这回事。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界上根本不存在“防御性过强”这么个问题，无论多强的防御性都不为错；劝人降低防御性如同劝人“别那么小心”“少活两年”。", "evidence": ["E005", "E006", "E029"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题不是“多疑”或“防御”，而是只有“疑”却没有对应的手段和体系；该女生是因缺少足够妥当的处理手段而出问题。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "侦查能力强、预判能力强而国力不强，就容易采用“举国动员，在此一举”的极端手段且误判后果沉重；这种问题不应通过削弱侦查、削弱预判来解决。", "evidence": ["E009", "E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把问题定性为“被害妄想”“防御性过强”，就是打算走削弱侦查、削弱预判这条路。", "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "劝人者如此定性，不单因为“增强国力”太难太累，也因其作为利益关联方/“盟国”没兴趣、没能力、甚至不希望对方走这条路；且帮对方建立的能力将来会成为自己入侵的麻烦。", "evidence": ["E012", "E013"]},
    {"claim_id": "C009", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者以引号代拟被批评的劝说者口吻（属代拟的他人立场，非作者自述）：为啥要花时间、花精力、花资源，去造成我将来的不方便？就为了让你过得更好一些吗？我可没这么傻。", "evidence": ["E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对上引态度的评断：这不是傻，这只是不爱罢了；而知道爱是什么且恰好与你有缘的人本就是可遇不可求的罕见事物，不懂爱是默认常态。", "evidence": ["E015", "E016"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "行动建议：你只有一个选择，只能选择“加强国防建设”，不可能选“削弱侦查”和“削弱推测”；不要怪那些劝你“不要被迫害妄想”的人（ta们一般不知自己为何这么说）；要重视不把问题如此定性的人。", "evidence": ["E017", "E018", "E019"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "防御体系的主体必须是被动式的而不能是主动式的；低运行成本、低维护需求是一切有效的个人安全防御体系的绝对标准。", "evidence": ["E020", "E021"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“世界上风险无穷多，你注意不过来”这一前提并不必然推出“人不能多想”的结论。", "evidence": ["E022"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "思考和研究如何防御、应对某种风险是一种乐趣；阅读各类求生手册、了解反窃听反诈骗等系统理论技术工具也是乐趣。", "evidence": ["E023", "E024"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者对“不要多想”话语来源的解释：说者因自己想出的办法实行不了、反而抑郁，于是反向求心情愉快，没结果的思考成了负担。", "evidence": ["E025", "E026"]},
    {"claim_id": "C016", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的一方说法（由提问者转述引入的网友意见）：货拉拉跳窗女生是“被害妄想症”。", "evidence": ["E027"]},
    {"claim_id": "C017", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者另问“女性在面对潜在危险时应该如何应对？”——作者未按性别专门作答，其回应以通用防御体系展开。", "evidence": ["E028"]}
   ],
   "argument_steps": [
    "先立判准：被害妄想的界限在威胁行为是否真实存在（P001—P003）。",
    "区分两种情形：基于真实行为的推想属“防御性过强”，只有臆想不存在之物（含幻听幻视）才是被害妄想（P004—P005）。",
    "以反问排除扩大化用法，并把话题转入本案（P006—P008）。",
    "再问：排除了被害妄想，能否归咎“防御性过强”？答不存在这种问题，无论多强都不为错（P009—P015）。",
    "重述真正问题：只有“疑”而无手段和体系；以战场侦查—参谋—国防军类比说明极端反应来自能力不匹配（P016—P023）。",
    "指出定性之争的后果：定性为被害妄想/防御性过强等于走削弱侦查与预判之路（P024）。",
    "解释劝说者动机（增强国力难、盟国不愿支援、帮出的能力将来是麻烦），代拟其自白并评“这不是傻，这只是不爱罢了”（P025—P031）。",
    "转向行动建议三条，并提出如何构建防御体系（P032—P037）。",
    "展开防御体系要点：打消“不要多想流”，主体须为被动式，低运行成本低维护为绝对标准（P038—P047）。",
    "反驳“不要多想”的来源并指出思考本身是乐趣，以椰子作比（P048—P056）。",
    "以情绪化停顿与后续链接收束（P057—P060）。"
   ],
   "concept_usage": [
    {"term": "被害妄想", "meaning": "本文限定为基于并不存在的行为和事物（尤其幻觉）设想威胁；判准是所推想威胁的行为本身是否真实存在", "evidence": "P001、P005", "ambiguity": "未引用临床诊断标准，属作者自设判准"},
    {"term": "防御性过强", "meaning": "作者认为不成立的说法，与“过于认真”“过于公平”等同类", "evidence": "P013、P014", "ambiguity": "作者先用它指基于真实威胁的推想，随后又否定其为问题"},
    {"term": "国防/国力/盟国", "meaning": "军事类比术语，指个人应对风险的手段、资源与外部支持关系", "evidence": "P019、P026、P028", "ambiguity": "类比与个人情境的对应关系由读者自行映射"},
    {"term": "被动式防御/主动防御", "meaning": "被动式指常在、低维护、无需临场决策的防御（高墙深壕铁丝网）；主动防御指需人观察决策执行的临时防御（站岗放哨巡逻扫荡）", "evidence": "P043、P044", "ambiguity": "未给成本阈值"},
    {"term": "多想/不要多想流", "meaning": "对风险的持续推想；作者反对以“人不能多想”限制它", "evidence": "P039、P040、P047", "ambiguity": "“多想”的边界未界定"},
    {"term": "爱", "meaning": "在“劝说者是否真心为对方好”的意义上使用（“这只是不爱罢了”）", "evidence": "P030、P031", "ambiguity": "未给定义，带道德劝诫色彩"}
   ],
   "examples_and_targets": [
    "货拉拉跳窗女生（提问者引入的事件，作者仅作假设性讨论，P007—P008）",
    "当面举铁锤与双手空空（作者的界定例证，P002—P003）",
    "幻听、幻视、幻觉（作者的例证，P005）",
    "“过于认真”“过于公平”“过于正义”“过于正确”“过于健康”“过于环保”“过于有效”（作者举例的同类“昏话”，P013）",
    "侦查兵、参谋部、国防军，以及谈判、游说、埋伏、伪装、牵制、游击、机动、迂回、分化、刺探、策反（作者军事类比，P019）",
    "倾巢出动大决战、隔着八百里迁都、直接投降（作者举例的极端反应，P019）",
    "“盟国”的参战/支援义务与漫长国防建设（作者类比，P027）",
    "作者代拟的劝说者自白（P029，被讽刺与被反驳的对象）",
    "末日求生手册、荒野求生指南、空难自救生存、城市安全手册、独自生存（作者例证，P053）",
    "反窃听、反偷拍、反诈骗、反跟踪、反绑架、反拦截、反破译、反骚扰（作者例证，P053）",
    "用脑袋撞、用牙咬、用指甲抠椰子（作者类比，P056）",
    "“怎么培养安全感？”（篇末后续链接标题，P060）"
   ],
   "conditions": [
    "对本案的分析以“先假设当事女孩的确就是因为观察到若干她觉得可疑的迹象而最后选择了跳车”为前提，作者未核验案件事实（P007）。",
    "“无论多强的防御性，都不为错”为无保留的全称判断（P014）。",
    "防御体系的改进须在“尽可能避免提高总体成本”这一坚定前提下进行（P046）。",
    "被动式防御的判准依赖“常在、无需临场决策、低维护成本”（P043）。",
    "对劝说者动机的解释以其“利益关联方/盟国”类比成立为条件（P026—P028）。",
    "结论的适用语境被限定为“个人安全防御体系”（P045）。"
   ],
   "rhetoric_and_tone": "连续反问与设问（“那还有谁不是被害妄想症？”“是吗？”“这话能听吗？”），冷嘲与口语训诫并用（“站着说话不腰疼”“没有意义的昏话”“我可没这么傻”），军事类比贯穿全篇；以第二人称给出行动建议和编号条目；篇末用“……”“缓一会儿，等我把白眼从后脑勺转回来”作情绪化停顿，再以链接句收束。",
   "unresolved_questions": [
    "货拉拉事件的具体事实（女孩是否确因观察到可疑迹象而跳车）作者只作假设，未核验，需外部核查。",
    "“低运行成本、低维护需求”的具体成本门槛与被动式防御的可操作清单，正文未给。",
    "作者解释“不要多想”者的心理时使用全称概括（“ta们”），个体差异未讨论。",
    "P059“后续转到这里：”指向的后续文章不在本篇正文内；P060“怎么培养安全感？”为标题式残句（语料标 divergence=true，lexical 未覆盖）。",
    "提问者所问“女性在面对潜在危险时应该如何应对”中的性别维度，作者未专门展开，其建议以中性主体叙述。",
    "无图片，图片核验不适用。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "“被害妄想”的基准界限，在于你所推想威胁的行为本身是否真实存在。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "推理或者设想出对自己可能的威胁，这不叫做被害妄想，只能叫防御性过强", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "臆想出根本不存在的行为和事物——尤其是出现幻听、幻视、幻觉", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "都已经排除了“被害妄想”这回事", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P014", "quote": "世界上根本不存在“防御性过强”这么个问题。无论多强的防御性，都不为错。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P015", "quote": "这跟劝你“别那么小心”“少活两年”没什么区别", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P016", "quote": "真正的问题，不是“多疑”，不是“防御”，而是只有“疑”，却没有对应的手段和体系。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P017", "quote": "这个女生不是因为防御心过强而出问题，而是因为缺少足够妥当的处理手段而出问题。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P022", "quote": "侦查强，预判强，国力不强，于是容易采用“举国动员，在此一举”的处理手段，误判则后果沉重。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P023", "quote": "这样一个问题，应该通过削弱侦查、削弱预判来解决吗？", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P024", "quote": "定性为“被害妄想”“防御性过强”，就是打算走这条路。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P026", "quote": "劝说者作为利益关联方、作为“盟国”，没兴趣、没能力，甚至不希望帮助被劝说者走“增强国力”这条路。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P028", "quote": "帮助对方建立起的每一种技巧、能力、策略，在将来自己想要入侵时都是麻烦。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P029", "quote": "“为啥要花时间、花精力、花资源，去造成我将来的不方便？就为了让你过得更好一些吗？我可没这么傻。”", "relation": "context"},
    {"key": "E015", "paragraph_id": "P030", "quote": "这不是傻，这只是不爱罢了。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P031", "quote": "知道爱是什么、而且还恰好和你有缘的人，本来就是可遇而不可求的罕见事物", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P034", "quote": "你只有一个选择，你只能选择“加强国防建设”——你根本不可能选“削弱侦查”和“削弱推测”。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P035", "quote": "不要怪那些劝你“不要被迫害妄想”的人。ta们一般都不知道自己为什么会这么说。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P036", "quote": "要重视那些不把问题定性为“被迫害妄想”的人。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P042", "quote": "防御体系的主体必须是被动式的，而不能是主动式的。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P045", "quote": "低运行成本、低维护需求，是一切有效的个人安全防御体系的绝对标准。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P040", "quote": "这个前提并不必然可以推出后面这个结果", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P052", "quote": "思考和研究如何防御和应对某种风险是一种乐趣。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P053", "quote": "了解反窃听、反偷拍、反诈骗、反跟踪、反绑架、反拦截、反破译、反骚扰……的系统理论、技术、工具，是一种乐趣！", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P048", "quote": "因为ta们自己的体验是自己想了半天想出来的办法自己根本实行不了", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P049", "quote": "所以反向的明智之策就是至少求一个心情愉快", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P008", "quote": "说这种话，纯属于站着说话不腰疼", "relation": "contradicts"},
    {"key": "E028", "paragraph_id": "P037", "quote": "那么，你要怎么构建你的防御体系呢？", "relation": "context"},
    {"key": "E029", "paragraph_id": "P013", "quote": "属于没有意义的昏话", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会事件评论", "安全防护/风险应对", "心理学概念辨析（被害妄想）", "军事类比/战略隐喻"],
   "issue_candidates": ["货拉拉跳窗事件与网友定性", "被害妄想与防御性过强的界限", "个人安全防御体系建设", "劝说者的动机与责任"],
   "text_function_candidates": ["答疑（回应提问）", "概念辨析", "反驳与批评", "行动建议", "类比说理"],
   "object_candidates": ["货拉拉跳窗女生（提问者引入）", "网友（被反驳说法的来源）", "劝说者/“盟国”（作者批评对象）", "侦查兵、参谋部、国防军（类比角色）"],
   "working_keywords": ["被害妄想", "防御性过强", "国防建设", "被动式防御", "主动防御", "多想", "安全感"]
  },
  "notes": "无图片，图片核验不适用；正文 P001—P060（2559 字符）全读完，status=read。本篇原为空条目，现全部填写。语料标 divergence=true（P060“怎么培养安全感？”为 lexical 未覆盖片段），已在 unresolved_questions 登记。作者对货拉拉案只作假设性讨论，未认定案件事实；“被害妄想症”的说法来自提问者转述的网友意见，记为 opponent_view，P029 引号内为作者代拟的劝说者自白（cited_source），均未归给作者。P059 指向的后续文章不在本批，需另行处理。"
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
