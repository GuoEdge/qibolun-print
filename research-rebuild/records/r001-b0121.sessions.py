# -*- coding: utf-8 -*-
"""批次 r001-b0121 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0121.sessions.py            # 写 out/r001-b0121.out.jsonl
  python3 records/r001-b0121.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0121"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0121.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "4c9e7bbd": {
  "analysis": {
   "question_context": "提问者问“知识重要还是人生阅历重要”，把二者设为二选一（Q001，属于提问者）。作者不接这个二选一，先界定“学习知识”是什么意思，再论阅历与知识互相成就，最后给出“都重要”并排序的回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "先定义学习知识：把新旧知识点用逻辑融会贯通。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "补充学习的含义：还包括学知识诞生的机制与检验真假的技术。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "阅历须兼“历”与“阅”；高质量知识和观察、分析能力是经历转为阅历的条件。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "反向关系：形成阅历也是反思沉淀知识；新发现会刷新老发现，阅历带来对旧知识的新认识。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "限定性推论：反思可能让人发现过去自以为知其实不知，弯路由此而来，连当下的确定也存疑。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P014"], "summary": "结论：都重要；最佳方案是先知识后阅历，基本不考虑反过来。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P015"], "summary": "让步：不排除有人乱世凭运气先得阅历，但那不可作系统方法。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为学习知识的过程就是把新旧知识点用逻辑方式融会贯通的过程。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为学习知识不只是增加已知信息，也是学习知识诞生的机制（思想史、科学史、社会史）和检验知识真假的技术（归纳、演绎、归谬）。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为阅历既要“历”也要“阅”，只历不阅不成其为阅历。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为只有具备高质量知识以及形成观点、检验观点的观察与分析能力，才谈得上“阅”，经历也才可能转化为阅历。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为形成阅历的过程同时是反思和沉淀知识的过程。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者以“如果你们熟悉科学史或者思想史”为条件提出：新发现会以其启示的新方法、新视角刷新所有老发现，使其显出更深刻的真理性与更多维度的内涵。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为从阅历中得到的对原知识的反思和审视会让人对旧知识有全新认识。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为这种刷新可能、甚至部分必然会达到让人发现以前自以为“知道”其实全然不知的程度。", "evidence": ["E009", "E010"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者推测无数弯路恰是先前自以为知道造成的，并假设一开始就不知道或许不至于绕那么远。", "evidence": ["E011", "E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问对当下的确定性表示怀疑：怎么知道三四十岁的自己不是大号的十几二十岁的自己。", "evidence": ["E013"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的回答是二者“都重要”，最佳方案总是先知识后阅历，基本不用考虑反过来。", "evidence": ["E014"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者不排除有人在兵荒马乱年代凭运气先有阅历再渐渐有知识，但认为那是伤亡率极高的淘汰赛的幸运儿，不足以作为系统方法使用。", "evidence": ["E015", "E016"]}
   ],
   "argument_steps": [
    "先说明要从“学习知识是什么意思”入手（P001）。",
    "定义学习知识为以逻辑融会贯通新旧知识点（P002）。",
    "以设问补充：学习还包括掌握知识诞生的机制与检验真假的技术（P003-P004）。",
    "由“阅历”一词拆出“历”与“阅”，反问只历不阅何以称阅历（P005-P006）。",
    "给出条件：高质量知识＋观察与分析能力，方能“阅”，经历才可能转为阅历（P007）。",
    "反向指出形成阅历也是反思沉淀知识，并以科学史/思想史的新老发现关系类比（P008-P010）。",
    "推论反思可能彻底刷新自我认知，并由此解释弯路、波及当下判断（P011-P013）。",
    "收束为“都重要”、先知识后阅历（P014）。",
    "以让步排除乱世凭运气先得阅历的幸存者路径，说明其不可作系统方法（P015）。"
   ],
   "concept_usage": [
    {"term": "知识", "meaning": "经逻辑融会贯通的新旧知识点；也包括知识诞生的机制与检验真假的技术。", "evidence": "P002、P004", "ambiguity": "未区分知识的类型与层次；“高质量的知识”未给判据。"},
    {"term": "阅", "meaning": "在知识基础上形成的观察能力与检验观点的分析能力；经历靠它转为阅历。", "evidence": "P007", "ambiguity": "与后文“反思和审视”是否同义，本文未界定。"},
    {"term": "阅历", "meaning": "经历经“阅”转化后的产物；反过来又是反思沉淀知识的过程。", "evidence": "P005、P007、P008", "ambiguity": "没有给出可操作的判据或程度标准。"},
    {"term": "真理的磨刀石", "meaning": "比喻，指高质量知识对判断真理所起的作用。", "evidence": "P007", "ambiguity": "修辞性表述，未展开具体机制。"},
    {"term": "幸存者", "meaning": "特指兵荒马乱年代凭运气先获阅历、后渐渐有知识的人。", "evidence": "P015", "ambiguity": "未给出年代或人群的具体范围。"}
   ],
   "examples_and_targets": [
    "作者论据（历史性断言，未给具体例证）：科学史、思想史中每次新发现都会以新方法、新视角刷新全部老发现（P009）。",
    "作者用作限定的假想对象：兵荒马乱年代凭运气先有阅历的“幸存者”（P015）。",
    "修辞材料：口语夸张“知道个空气锤锤儿”（P011）、“吃这么多瘪”（P012）、“大号的十几二十岁的自己”（P013）。",
    "跨篇指涉：“什么叫学会了一项知识，这个我们说过了”（P002）指向本文之外的内容，本文未展开。"
   ],
   "conditions": [
    "P007 明确以“高质量的知识”加上观察能力、分析能力为经历转化为阅历的前提。",
    "P009 以“如果你们熟悉科学史或者思想史”为读者条件。",
    "P011 用“可能——甚至部分必然的”保留可能性与程度。",
    "P012 用“没准你要是……”的假设语气谈不知是否反而少走弯路。",
    "P014 用“基本”限定先知识后阅历这一方案。",
    "P015 用“虽然不排除……但……不足以作为一种系统的方法来使用”作让步与排除。"
   ],
   "rhetoric_and_tone": "口语化答疑，通篇以“你”直呼读者；用设问（“如何才算学到东西？”）和反问（“只历不阅，哪有阅历？”“你怎么知道……？”）推进；夹俚俗夸张（“空气锤锤儿”“吃这么多瘪”）；结构是先定义知识，再论知识与阅历互济，末段让步限定后收束。",
   "unresolved_questions": [
    "P002 的“这个我们说过了”指向本文之外的其他文章，具体所指本文未说明。",
    "P009 关于科学史/思想史“老发现被新发现刷新”的断言无具体例证，待外部核查。",
    "“高质量的知识”无判据；“阅”与“反思和审视”的关系未界定。",
    "P001 中“这个”的指代对象本文未说明；P003 在渲染包中标注“⚠lexical未覆盖片段”，text 与 lexical 结构存在不一致，见 structure.text_lexical_divergence。",
    "提问者把知识与阅历设为二选一，作者以“都重要”并加排序作答，未正面接受该二选一框架。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "学习知识的过程，就是将新的知识点和旧的知识点用逻辑的方式融会贯通的过程。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "本身也是在学习知识本身诞生的机制（思想史、科学史、社会史），以及检验知识真假的技术（归纳、演绎、归谬）", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "阅历阅历，不但要历，还要阅。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "只历不阅，哪有阅历？", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "有了高质量的知识作为真理的磨刀石，又有了形成新观点的观察能力、检验观点的分析能力，你才能“阅”", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "形成阅历的过程也是一个反思和沉淀知识的过程", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "所有的老发现也被新发现所启示的新方法、新视角重新刷新了", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "会让你对旧的知识有全新的认识", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "它可能——甚至部分必然的——会新到这个程度", "relation": "qualifies"},
    {"key": "E010", "paragraph_id": "P011", "quote": "以前的你自以为“知道”那些知识，其实你“知道”个空气锤锤儿。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "无数的弯路恰恰是因为之前的你自以为知道而造成的", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P012", "quote": "没准你要是一开始就不知道，你还不至于会绕这么远，吃这么多瘪。", "relation": "qualifies"},
    {"key": "E013", "paragraph_id": "P013", "quote": "你怎么知道三四十岁的你就不是一个大号的十几二十岁的自己？", "relation": "qualifies"},
    {"key": "E014", "paragraph_id": "P014", "quote": "答案是“都重要”。你也不必纠结，你最佳的方案总是先知识后阅历，基本不用考虑反过来。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "虽然不排除有些幸存者是在兵荒马乱的年代凭着运气先有了阅历，然后才渐渐有些知识的。", "relation": "qualifies"},
    {"key": "E016", "paragraph_id": "P015", "quote": "但那是伤亡率极高的淘汰赛剩下的幸运儿，那个是不足以作为一种系统的方法来使用的。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认识论", "学习方法", "知识论"],
   "issue_candidates": ["知识与阅历的关系", "学习过程的含义", "经验与反思"],
   "text_function_candidates": ["答疑", "说理", "经验总结"],
   "object_candidates": ["科学史", "思想史"],
   "working_keywords": ["阅历", "融会贯通", "真理的磨刀石", "归纳", "演绎", "归谬", "幸存者"]
  },
  "notes": "无图片。text 与 lexical 存在分歧（P003 未被 lexical 覆盖），已在 structure.text_lexical_divergence 与未决问题登记。P002“这个我们说过了”为跨篇指涉，本文未展开。"
 },
 "e7cd38a0": {
  "analysis": {
   "question_context": "提问者问中国的社会精英阶层是否正在与社会底层加速脱节（Q001，属于提问者）。作者不直接回答趋势，而是先驳“高智能高技能者也算精英”的说法、重解“精英”一词的词源与所指，再论证精英原理上不可能脱离底层，并把该问题的提出归因于语文教育造成的概念混乱。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "转述他人说法：只会计算、绘画而无领导组织能力的人材也算精英。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "词源考察：elite 出自古法语 élite、拉丁文 eligere，意为“被推举出来的人”，词根同 election。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "主张：不承担领导职能、未获众人认可授权的高智能高技能者不是精英，而是 valuable asset／人材。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "辨析人材与人才：引《易传》三才之说释人才，人材则指可堪使用之人。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P009"], "summary": "例证：出国洗碗的博士生只是人材不是人才，与精英无逻辑必然关系。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "语言观：中文高度精确，写法不同即不同义，严格说没有同义词；不懂这点无法继承中国文化遗产。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "归因批评：现代语文教育与欧美汉学家的水平造成“中国文化大而化之”的糊涂结论，这正是该问题以此形式被提出的根源。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019"], "summary": "转折设问：究竟什么样的人是精英。", "role": "transition"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "以一连串“就是精英”的实例给出判断标准：能带人、能聚人、被请断是非者。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P027"], "summary": "反例：光凭文凭、留学、体制内冗职或无实际成果的“教授”，给前面这些人提鞋都不够资格。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P028", "P029"], "summary": "思想实验：空难落森林后，会被飞快推举出来拿主意、断是非、定计划、明赏罚的才是精英。", "role": "example"},
    {"unit_id": "U012", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036"], "summary": "定义与结论：精英是在每个群体里拿主意、定乾坤的人，凭学历出身钱财不算；故原理上不可能脱离底层，真正敬畏底层同类。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P037", "P038", "P039"], "summary": "条件性反问：想做精英须经死去活来的磨练，未经历者谈不上精英。", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044"], "summary": "结构判断：精英是社会的骨头，不能是阶层而必然贯穿所有阶层，实际是一个集团。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P045", "P046"], "summary": "结语：“精英脱离底层”不可能也从未发生；真正可能的是“高门无良材，英雄尽草莽”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者转述并反驳的说法：只会计算、绘画而没有领导能力和组织能力的人材也应该算精英。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张 elite 一词经古法语 élite 出自拉丁文 eligere，意为 the chosen ones（被推举出来的人），词根与 election 一致。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张不承担领导职能、不需要众人认可和授权委托的高智能高技能者不叫精英，只能叫 valuable asset（人材）。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张人材不是人才：天才、地才、人才分别指精通神哲学、自然科学与政治／伦理／社会学的杰出智者。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引《易传·系辞下》以“三才之道”说作为天才/地才/人才之说的依据。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张“人材”指可堪使用之人，即 reliable human resource。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为出国洗碗的博士生只是人材不是人才，跟精英没有逻辑必然的关系。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者主张除异体写法与译音译法造成的差异外，中文里写法不一样的词就一定不是同一个意思，严格意义上没有“同义词”概念。", "evidence": ["E009", "E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为不明白中文用词精确这一点，就不可能真正继承中国的文化遗产。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为现代语文教育质量令人遗憾，养出满脑子“xx就是yy的意思”的人，并连带断言欧美“汉学家”的中文就是这个水平，因此对中国文化无能。", "evidence": ["E012", "E013"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为上述概念混乱正是这个问题会被人以这种形式提出来的根源。", "evidence": ["E014"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的精英定义：精英是那些在每个群体里拿主意、定乾坤的人，不是凭学历高、出身好、有钱就能让人心服口服。", "evidence": ["E015", "E016"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言精英原理性的不可能脱离底层人民；只有自以为有了钱、学历、官员身份就抖起来而根本不知精英为何物的人才会“脱离底层”。", "evidence": ["E017", "E018"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为真正的精英对越是底层的同类越感到敬畏和不由自主的尊重。", "evidence": ["E019"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张想做精英须先经风刀霜剑、死去活来的磨练，没经历过的人谈不上精英。", "evidence": ["E020", "E021"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张精英不能是一个“阶层”而必然贯穿所有阶层，实际上是一个集团，是一都、一乡、一社、一族、一群之首们的总和。", "evidence": ["E022", "E023"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言“精英脱离底层”是不可能发生的，历史上也从来没有在任何意义上发生过。", "evidence": ["E024"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者认为真正可能发生的是“高门无良材，英雄尽草莽”。", "evidence": ["E025"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以空难落森林的假想情形说明：被飞快推举出来拿主意、断是非、定计划、明赏罚的那些人才是精英。", "evidence": ["E026"]}
   ],
   "argument_steps": [
    "先摆出他人的说法（无领导组织能力的人材也算精英）作为要驳的对象（P001）。",
    "以 elite 的词源（eligere→被推举出来的人）界定词义，把“被推举、被授权”设为精英的构成条件（P002-P004）。",
    "为区分概念插入语文课：人材≠人才，引《易传》三才之说，并以此判博士生出国洗碗一例（P005-P009）。",
    "由此上升到语言观：中文用词精确、严格说无同义词，并归因于语文教育失败与欧美汉学家水平，指出问题的提出根源（P010-P017）。",
    "转入正面回答，用一串“就是精英”的实例和空难思想实验给出判据（P018-P029）。",
    "收束为定义与结论：精英跨阶层、是集团而非阶层，故不可能脱离底层（P030-P044）。",
    "以极端化类比否定“精英脱离底层”的历史可能性，用对句作结（P045-P046）。"
   ],
   "concept_usage": [
    {"term": "精英", "meaning": "承担领导职能、得到众人认可和授权委托、在每个群体里拿主意定乾坤的人。", "evidence": "P004、P030", "ambiguity": "以词源定词义；“众人认可和授权委托”的认定程序、群体范围本文未说明。"},
    {"term": "人材", "meaning": "可堪使用之人，作者注为 reliable human resource；不必然是精英。", "evidence": "P008", "ambiguity": "与“人才”“valuable asset”的边界靠字形差异区分，本文未给操作标准。"},
    {"term": "人才", "meaning": "与天才、地才并列，指精通政治／伦理／社会学的杰出智者。", "evidence": "P006", "ambiguity": "释义来自作者对“三才”的解读，本文未给文献依据。"},
    {"term": "valuable asset", "meaning": "有价值的社会资产，特指不承担领导职能的高智能、高技能者。", "evidence": "P004", "ambiguity": "英文注与中文“人材”是否完全等同，本文未说明。"},
    {"term": "同义词", "meaning": "作者用以指称中文中并不存在的概念（严格意义上）。", "evidence": "P012", "ambiguity": "作者自己用“在严格意义上”限定，未界定“严格意义”的标准。"},
    {"term": "集团／阶层", "meaning": "精英是贯穿各阶层的集团，而非一个阶层。", "evidence": "P042、P043", "ambiguity": "“集团”的组织形态与边界本文未说明。"}
   ],
   "examples_and_targets": [
    "反驳对象：主张“只会计算、绘画，没有领导能力和组织能力的人材也应该算精英”的“很多人”（P001）；把精英脱离底层当作现实问题来问的人（P033、P045）。",
    "被引文献：《易传·系辞下》“三才之道”引文（P007，属被引典籍，非作者自述）。",
    "作者的例证：带农民工干活发钱的领头人（P021）、跳槽能带走整班下属的（P022）、维权时在人群里拿主意的（P023）、开小公司有一群不辞职老员工的（P024）、电话叫得动老部下的（P025）、有人请赐名、问意见、评理仲裁的（P026）。",
    "作者的反例：出国洗碗的博士生（P009）；光凭博士文凭、留学、体制内冗职或没有实际成果的“教授”（P027）。",
    "思想实验：一起空难掉到森林里看谁被推举出来（P028）。",
    "批评对象：现代语文教育（P014）、欧美“汉学家”（P015）。",
    "修辞材料：米老鼠与野狼（P035）、“此小犬也”（P036）、章鱼（P040）、海里的盐自动结块飘到天上（P045）、“高门无良材，英雄尽草莽”（P046）。"
   ],
   "conditions": [
    "P010 的语言断言以“除了异体写法造成的差异和译音词的译法造成的差异”为排除条件，并以“严格意义上”自我限定（P012）。",
    "精英的界定依赖“承担领导职能”“得到众人认可和授权委托”两个条件（P004）；判据是“在每个群体里拿主意、定乾坤”（P030）。",
    "P039 以“如果都没有死去活来过”为条件反问，未经历者不被算作精英。",
    "P028 的空难情形是假想条件，作者未声称现实中可直接检验。",
    "P031 承认群体分布遍及低到高所有层次，并指出低层次群体数量更多、环境更险恶，是结论所依赖的分布前提。",
    "P034 以“事实上”作断言，但本文未给经验材料。"
   ],
   "rhetoric_and_tone": "训诫兼嘲讽的论辩体。第二人称“你们”“你”贯穿；密集反问（“究竟什么样的人是精英？”“还谈何继承？”“你死过没有？”）；夸张与贬斥并用的比喻（米老鼠与野狼、章鱼、海里的盐结块飘上天、“此小犬也”）；引文言典籍作依据；正面回答部分改用“就是精英”的排比句式，末尾以格言式对句收束。",
   "unresolved_questions": [
    "提问问的是精英与底层是否“正在加速脱节”，作者改以词义与原理回答“不可能脱离”，未回应“加速”与当前趋势。",
    "P002 的词源链条（elite←élite←eligere）与 P006 对“三才”的解读均未给出处，待外部核查。",
    "P007 引文的标点与空格为本文原样（“有天道焉， 有人道焉”），与通行本可能存在版本差异，待外部核查。",
    "“众人认可和授权委托”如何认定、群体怎样划定，本文未说明。",
    "P010-P012“中文没有同义词”是作者的强断言，仅以“严格意义上”限定，未给语言学论证。",
    "P014-P015 对现代语文教育与欧美“汉学家”的评价属作者判断，待外部核查。",
    "P034、P045 的“事实上”“历史上从来没有”为全称断言，本文未给史料或数据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "有很多人都在说那些只会计算、绘画，没有领导能力和组织能力的人材也应该算精英。", "relation": "contradicts"},
    {"key": "E002", "paragraph_id": "P002", "quote": "“精英”这个词的英文elite是从古法语的élite来的，élite又是从拉丁文eligere来的。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这意思就是the chosen ones——“被推举出来的人”。elite这个词的词根和election就是一致的。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "这些不叫做“精英”，而只能叫做valuable asset——有价值的社会资产——人材。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "天才、地才、人才，分别是指“有天道焉、有地道焉、有人道焉”", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "兼三才而两之，故六。六者非它也，三才之道也。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "而“人材”，是指“可堪使用之人”，指reliable human resource。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "那些出国洗碗的博士生，只是人材，不是人才，跟精英没有逻辑必然的关系。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "除了异体写法造成的差异和译音词的译法造成的差异，只要是写法不一样的词，就一定不是同一个意思。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "记住了，中文在严格意义上根本就没有“同义词”这个概念。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "你不明白这一点，你根本不可能真正继承中国的文化遗产。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "现代语文教育质量令人遗憾，导致了大量脑袋里装满了“xx就是yy的意思”的糊涂人", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P015", "quote": "无数欧美“汉学家”的中文实际就这么个水平，这已经决定了ta们对中国文化的无能。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P016", "quote": "这甚至就是这个问题之所以会被人以这种形式提出来的根源。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P030", "quote": "精英是那些在每个群体里拿主意、定乾坤的人", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P030", "quote": "这绝不是单凭什么“学历高”“出身好”“有钱”就有这个资格让人心服口服、甘心受教受罚的。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P032", "quote": "所以，精英原理性的不可能脱离底层人民。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P033", "quote": "根本不知精英为何物的人，才会“脱离底层”。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P034", "quote": "事实上真正的精英们对越是底层的同类，越是感到敬畏和不由自主的尊重。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P037", "quote": "想做精英，是要风刀霜剑、雷击火烧、死去活来先百炼钢化做绕指柔的。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P039", "quote": "如果都没有死去活来过，几年冷板凳就想“人生无望”，对真正的风浪噤若寒蝉的人，谈何“精英”？", "relation": "qualifies"},
    {"key": "E022", "paragraph_id": "P042", "quote": "精英根本就不能是一个“阶层”，因为ta们必然贯穿所有的阶层。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P043", "quote": "精英实际上是一个集团。是一都、一乡、一社、一族、一群之首们的总和。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P045", "quote": "“精英脱离底层”这种人文奇观是不可能发生的，历史上也从来没有在任何意义上发生过", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P046", "quote": "真正可能发生的是“高门无良材，英雄尽草莽”。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P028", "quote": "那些人会飞快的被推举出来拿主意、断是非、定计划、明赏罚。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会分层", "语义学／训诂", "语文教育", "领导力"],
   "issue_candidates": ["精英的定义", "精英与底层的脱节", "人材与人才之别", "中文是否有同义词", "语文教育与文化继承"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "概念辨析"],
   "object_candidates": ["中国社会", "农民工群体", "欧美汉学家", "现代语文教育"],
   "working_keywords": ["精英", "elite", "eligere", "人材", "人才", "valuable asset", "三才", "同义词", "阶层", "集团"]
  },
  "notes": "无图片。P007 为 lexical quote 节点（《易传·系辞下》），已按被引典籍归属（cited_source），未归给作者。P001“有很多人都在说……”为作者转述的他人说法，按 opponent_view 处理。更新时间为 2025-02-27，晚于发表时间，本文未说明修订内容。"
 },
 "cfb56d6d": {
  "analysis": {
   "question_context": "提问者问「君子远庖厨」是否伪善，问题本身把“远庖厨”置于“伪善”的定性之下（Q001，属提问者，不得自动归给作者）。作者不直接判定是或否，而是先假定这一定性成立、检查它会导出什么结果（P001），再把问题交回要求者：是否真要未来掌权的人习惯杀戮与行刑（P006、P007、P010）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "方法声明：先看把“远庖厨”定义为“伪善”的结果。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "界定“君子”为孔子社会理想中要去执掌权力的人，并假设由此规定其不准远庖厨。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004", "P005"], "summary": "假设性后果推演：从小亲手屠宰、见血不眨眼，直到视杀生为无额外道德意义的平常事。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "反问对方是否真要如此；并举欧洲领主之子、苏丹王子从小反复看惯处决为例，称此要求会被欣然照办。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "以“谁拿刀、谁在砧板上”反问，并用砧板上的鱼嘲笑屠夫怕见血作比，称之为人间喜剧。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P013"], "summary": "训诫式收束：做事之前先想后果。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张先考察把“远庖厨”定义为“伪善”会带来什么结果，而不是直接判定它是否伪善。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“君子”界定为孔子社会理想中要去执掌权力的人。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者推演：若把远庖厨定为伪善，其结果就是要求这些掌权者从小学亲手杀猪宰牛、剖鱼割鸡，直到把杀戮接受为没有额外道德意义的平常事。", "evidence": ["E003", "E004", "E011"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问要求者：是否真的希望将来掌权的人觉得“远杀”是一种虚伪，并被喝令“面对现实”“接受现实”。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这类要求会被欣然照办，并举欧洲领主之子与苏丹王子从小必须一遍遍把处决看习惯为例（历史断言，出处待外部核查）。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“谁拿着刀、谁在砧板上”反问，把嘲笑屠夫怕见血者比为砧板上的鱼，并称此为人间喜剧。", "evidence": ["E008", "E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的行动要求是：做事之前，想想后果。", "evidence": ["E010"]}
   ],
   "argument_steps": [
    "先声明方法：看把“远庖厨”定义为“伪善”的结果（P001）。",
    "界定“君子”＝孔子社会理想中要去执掌权力的人，据此设想新规定“从今天开始，不准远庖厨”（P002）。",
    "推演后果：必须从小学亲手屠宰，直到接受这是平常事、没有额外道德意义（P003）；并作反讽性具体化（P004、P005）。",
    "反问“是要这样吗？”（P006），把问题交回要求者：是否真要掌权者把“远杀”当虚伪（P007）。",
    "举欧洲领主之子、苏丹王子从小反复看惯处决为例，说明这类要求可被照办（P008、P009）。",
    "再反问“是想要把剧情改成这样吗？”（P010）。",
    "反问“到底谁拿着刀，谁在砧板上”，以砧板上的鱼嘲笑屠夫怕见血作比（P011、P012）。",
    "收束为行动要求：做事之前，想想后果（P013）。"
   ],
   "concept_usage": [
    {"term": "君子", "meaning": "本文指孔子社会理想中要去执掌权力的人（P002）。", "evidence": "P002", "ambiguity": "作者以“这其实是”直接断定，未给文献出处；是否等同孔子原义，本文未说明。"},
    {"term": "远庖厨／远杀", "meaning": "本文把二者并提，指掌权者回避亲自处理杀生与见血（P002、P007）。", "evidence": "P007", "ambiguity": "二者是否完全同义、是否包含“不忍”之意，本文未说明。"},
    {"term": "伪善", "meaning": "提问者给定的定性；作者不定义它，只检查接受这一定性后的后果（P001）。", "evidence": "P001", "ambiguity": "未区分动机层面、行为层面与认知层面的“伪善”。"},
    {"term": "后果／结果", "meaning": "本文的论证支点：以反事实推演代替对“是否伪善”的直接判定（P001、P013）。", "evidence": "P013", "ambiguity": "无。"},
    {"term": "ta们", "meaning": "指将来执掌权力的人（P007、P008）。", "evidence": "P008", "ambiguity": "与P002的“君子”是否完全同指，本文未明说。"}
   ],
   "examples_and_targets": [
    "杀猪宰牛、剖鱼割鸡、割断猪的颈动脉、砍断猪的气管、毛血旺（P003—P005）：作者对假设后果的具体化描写，带反讽，属推演性例示而非实际事例。",
    "欧洲领主（原文写作“欧州”）的儿子们与苏丹们的王子们从小必须反复看惯处决（P008、P009）：作者的历史例证，用于说明要求可被照办；出处待外部核查，原文写法照录。",
    "砧板上的鱼与屠夫（P011、P012）：比喻性修辞材料。",
    "反驳对象：把“君子远庖厨”定义为“伪善”、并要求掌权者“面对现实”的一方（P001、P007）。"
   ],
   "conditions": [
    "全部推论建立在反事实假设上：“我们看看把这定义为‘伪善’的结果”（P001）、“从今天开始，不准远庖厨”（P002）。",
    "依赖作者对“君子”的界定：孔子社会理想中要去执掌权力的人（P002）。",
    "条件句：“你们要真这么要求，ta们是可以欣然照办的”（P008）。",
    "作者未给出“伪善”的界定标准；若按别的定义，后果推演是否仍成立，本文未说明。",
    "收束句“做事之前，想想后果”（P013）把判断与责任交回要求者。"
   ],
   "rhetoric_and_tone": "连续反问推进（P006、P007、P010、P011），并直接称呼提问方为“你们”。反讽性具体化描写（P004“一边聊天，一边割断猪的颈动脉”、P005“毛血旺”）带黑色幽默。以“砧板上的鱼嘲笑屠夫怕见血／人间喜剧”作讽刺比喻（P012）。收尾为简短训诫句（P013）。全篇不提供正面定义或价值论证，语气偏讥诮、逼问。",
   "unresolved_questions": [
    "作者未直接回答“远庖厨是不是伪善”，只给出后果推演与反问；这是否构成对该提问的正面回答，本文未说明。",
    "P008、P009 关于欧洲领主之子与苏丹王子从小反复观看处决的说法无出处，属待外部核查的历史断言。",
    "作者以“这其实是”断定“君子”指孔子社会理想中要去执掌权力的人，未给文献依据；正文与提问均未出现“孟子”，该说法出处本文未说明。",
    "原文“欧州”疑为“欧洲”的写法，按原文照录，未作改动。",
    "“伪善”的判定标准（动机、行为或认知）本文未区分，可能影响对全篇结论的解释。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "我们看看把这定义为“伪善”的结果。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "“君子”——这其实是孔子社会理想中要去执掌权力的人——", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "必须从小学亲手杀猪宰牛、剖鱼割鸡", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "学会一边聊天，一边割断猪的颈动脉，再砍断猪的气管免得它吵耳朵", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P005", "quote": "学会看见血眼睛都不眨", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "你们真的希望将来掌权的人觉得“远杀”是一种虚伪", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "ta们是可以欣然照办的", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "欧州领主的儿子们和苏丹们的王子们可是从小必须要一遍一遍把处决看习惯的", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P011", "quote": "到底谁拿着刀，谁在砧板上啊？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "居然有砧板上的鱼嘲笑屠夫怕见血，这真是人间喜剧。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P013", "quote": "做事之前，想想后果。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治伦理", "儒家思想（孔子·君子）", "暴力与权力", "论辩术"],
   "issue_candidates": ["君子远庖厨是否伪善", "掌权者与杀戮的距离", "以后果推演代替定性判断"],
   "text_function_candidates": ["答疑", "论辩", "反问式反驳", "训诫"],
   "object_candidates": ["孔子", "君子", "欧州领主之子", "苏丹王子", "提问者（“你们”）"],
   "working_keywords": ["君子", "远庖厨", "远杀", "伪善", "庖厨", "处决", "后果", "砧板"]
  },
  "notes": "无图片。P001 即以“把这定义为‘伪善’的结果”作反事实推演，作者未直接判定是否伪善，这是本篇最重要的归属与语气限制。P002 对“君子”的界定是作者自己的解读，未给文献出处。原文“欧州”照录未改，疑为“欧洲”。P008—P009 历史断言无出处，列为待外部核查。正文与提问均未出现“孟子”，该说法出处本文未说明。"
 },
 "fde2618b": {
  "analysis": {
   "question_context": "提问者问〔乐于助人〕和〔有求必应〕该如何区分，只提出区分问题，未表明立场（Q001，属提问者，不得自动归给作者）。作者的回答不是给出行为判别清单，而是主张在“回应”层面人事实上只有“有求必应”一种反应（P024），并把问题移向请求方的性质：对方是在求助，还是在以“求助”为形式的“索债”（P013、P027）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以反问开场：有人求你不吭声也算“应”，应的是一个“沉默”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"], "summary": "界定“应”＝回应（含沉默、不让人看出是否收到），并明确“应”不等于“答应”。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P009"], "summary": "推论：凡有求必有应；接受者因不喜欢所收到的回应，便当作“估计没收到”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "重设问题：把“没拿到满意承诺就当作对方没收到、反复坚持到答应”的态度算不算“求助”；指出“不达目的誓不罢休”的逻辑属于讨债。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "判断许多人并非求助，而是自认为对方欠自己（人情债或义理债），属以“求助”为形式的“索债”，且是对善心人的设计。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021"], "summary": "推演索债的运作：会一直成功直到耗尽“善良余额”；随即让步说事实上耗不尽，因为总有新好人带来新份额；并作市场与善堂施粥的比喻性叙述。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023"], "summary": "连续反问成效：有多少真求助者得到帮助、多少说帮人的真帮到人，还是只培养出更多“喝粥侠”。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "结论与行动建议：乐于助人事实上只有“有求必应”一种反应（指回应非答应）；要管理清楚回应，以“对不答应的人怎么看、怎么说”为最起码的门槛。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P028", "P029"], "summary": "限定：即使过了门槛，也要当心对方要的你没有或不能给；在这门槛之上再考虑帮的事。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为有人求你而你不吭声，你也是应了——你回应了一个“沉默”。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者的条件式通则：凡有求，除非你没收到，否则你都在应。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“应”不等于“答应”：回应就是应，“没有回应”也是一种回应。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为凡有求必有应，只不过有些接受者不喜欢所收到的回应，便把它当作“估计没收到”来处理。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者把真正的问题重设为：把“没拿到满意承诺就当作对方没收到、继续重复直到对方答应”的态度（never take no for an answer）算不算“求助”。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认求助含有“不达目的誓不罢休”的逻辑，认为这种逻辑属于讨债。", "evidence": ["E007", "E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为很多人不是求助，而是自认为对方有债欠自己（人情债或义理债），那只是以“求助”为形式的“索债”，且是对吃这一招的善心人的设计。", "evidence": ["E009", "E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这类索债会一直成功，直到把可以通过这一行为品味自己善良感的人的“善良余额”耗尽为止。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者随即让步：事实上也耗不尽，因为总有新毕业的新好人带来新投资，每天都有新份额投放市场。", "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：这份善良投资耗尽后，有几个真在求助的得到帮助、有几个说帮人的真帮到了人，还是只是培养出更多新的“喝粥侠”。", "evidence": ["E013", "E014"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张：乐不乐于助人，你事实上只有“有求必应”这一种反应——这是指回应，不是指答应。", "evidence": ["E015"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求管理清楚自己的回应，看清对方是不是求助的态度，确保有限的帮助余额落到确实是求助的人手里。", "evidence": ["E016", "E017"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“等着看ta们对不答应的人怎么看、怎么说”作为分辨“求助”与带引号的“求助”的最起码门槛。", "evidence": ["E018"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者限定：即使到了这个门槛，也要当心对方要的东西你没有、或对方要的你不能给；要在这门槛之上再考虑帮的事。", "evidence": ["E019", "E020"]}
   ],
   "argument_steps": [
    "反问开篇：求你不吭声是否没有应；答曰应了一个“沉默”（P001、P002）。",
    "给出条件式通则：凡有求，除非你没收到，否则你都在应（P003）；并补充不让人看出是否收到也是应（P004、P005）。",
    "辨析“应”与“答应”：回应就是应，“没有回应”也是一种回应（P006—P008）。",
    "推出凡有求必有应，解释“当作没收到”源于接受者不喜欢该回应（P009）。",
    "重设问题：never take no for an answer 的态度算不算求助（P010）。",
    "以讨债为对照：不达目的誓不罢休的逻辑属于讨债，不属于求助（P011、P012）。",
    "判定许多“求助”实为索债，理由是自认为对方欠自己，并列举捧场、帮助过、同乡、同学、同事、认识等由头（P013、P014）。",
    "以市场与善堂施粥作比喻推演其运作：耗尽善良余额，但总有新好人补充份额，新好人耗尽后鞠躬下台（P015—P021）。",
    "反问成效：有几个真求助者得到帮助、有几个说帮人的真帮到人，还是只培养出更多“喝粥侠”（P022、P023）。",
    "给出结论与行动建议：回应层面只有“有求必应”；管理清楚回应，以“对不答应的人怎么看、怎么说”为门槛，先看清是否真求助再考虑帮（P024—P029）。"
   ],
   "concept_usage": [
    {"term": "应／回应", "meaning": "本文把“应”界定为回应，包括沉默、不表态、不让人看出是否收到（P002—P008、P024）。", "evidence": "P007", "ambiguity": "“不让人看出你有没有收到”是否仍算“应”，作者以“其实也是应”直接断定，未给判据。"},
    {"term": "答应", "meaning": "指给予对方满意的承诺，只是“应”的一种，不是“应”的全部（P006、P024）。", "evidence": "P024", "ambiguity": "无。"},
    {"term": "求助／“求助”（索债）", "meaning": "真求助不含“不达目的誓不罢休”的逻辑；带引号的“求助”是以求助为形式的索债，预设对方欠自己（P011、P013、P015、P027）。", "evidence": "P015", "ambiguity": "如何在实际行为上区分两者，作者只给出“对不答应的人怎么看、怎么说”这一门槛。"},
    {"term": "人情债／义理债", "meaning": "作者用来说明索债者自认为对方欠自己的两种债（P013）。", "evidence": "P013", "ambiguity": "“义理债”未在本文定义。"},
    {"term": "善良余额", "meaning": "比喻性说法，指善心人可被消耗的善良感与帮助资源（P016、P026）。", "evidence": "P016", "ambiguity": "是否可计量、在什么条件下耗尽，本文未说明。"},
    {"term": "never take no for an answer", "meaning": "英文表述，指不拿到满意承诺就不罢休、把拒绝当作“没收到消息”的态度（P010）。", "evidence": "P010", "ambiguity": "作者以破折号插入，未给出中文定译。"},
    {"term": "喝粥侠／善堂／粥", "meaning": "比喻，指赶来分食善心资源的人与新好人投放的份额（P017—P019、P023）。", "evidence": "P023", "ambiguity": "为修辞性说法，非机构或群体的实际指称。"},
    {"term": "门槛", "meaning": "指判断对方是否真求助的最低标准（P027—P029）。", "evidence": "P027", "ambiguity": "无。"}
   ],
   "examples_and_targets": [
    "讨债（P012）：作者用来与求助相对照的例子。",
    "捧过场、帮助过对方、同乡、同学、同事、曾经认识（P014）：作者列举的索债者自我理由，属说明性示例。",
    "新毕业的新好人、新投资、新份额投放市场、善堂开门、众好汉一哄而上、喝粥侠（P017—P023）：比喻性叙事，非具体事件或数据。",
    "“滴滴香浓，意犹未尽”（P019）：广告语式修辞材料，本文未注明出处，待外部核查。",
    "反驳对象：把拒绝当作“对方没收到消息”、反复坚持到对方答应的态度（P010），以及以“求助”为形式索债的人（P013、P015）。"
   ],
   "conditions": [
    "“凡有求，除非你没收到，否则你都在应”（P003）：以是否收到请求为唯一条件。",
    "“ta们会一直成功，直到把……‘善良余额’耗尽为止”（P016）：以存在可被消耗的善心人为条件；作者随即以“事实上也耗不尽”作让步（P017）。",
    "“即使到了这个门槛”，仍要当心对方要的你没有或不能给（P028）；“在这门槛之上，再考虑帮的事”（P029）给出行动次序。",
    "提问用〔〕框出两个待区分项（Q001）；作者未沿用该框，而把它改写为“乐不乐于助人，你事实上只有‘有求必应’这一种反应”（P024）。"
   ],
   "rhetoric_and_tone": "反问开篇并贯穿（P001、P011、P022、P023）。市场与商业隐喻密集：投资、份额、配额、生意、投放市场（P016—P018），并接善堂施粥的比喻以及“喝粥侠”“滴滴香浓，意犹未尽”的广告语式调侃（P018、P019）。对“新好人”的叙述带调侃式同情（P020、P021）。收尾转为训诫与操作建议，第二人称“你”直接对读者说话，用“ta们”指索债者。",
   "unresolved_questions": [
    "提问问“如何区分”，作者未给出二者在行为上的判别清单，而是主张回应层面只有“有求必应”一种反应（P024）；这是否等同回答该区分问题，本文未说明。",
    "P016 称“善良余额”会被耗尽，P017 又称“事实上也耗不尽”，两处存在张力；作者以“当然，事实上”作让步，但未说明各自的条件。",
    "P010、P013 对“求助者”动机的判断（自认为对方有债欠自己）属作者推断，未提供经验数据或具体案例。",
    "“义理债”未在本文定义；“善良余额”是否可计量，本文未说明。",
    "P019“滴滴香浓，意犹未尽”是否引用广告语及其出处，本文未注明，待外部核查。",
    "无图片。brief 与正文高度重合（为正文节选），未据 brief 立论。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "不，你应了，你回应了一个“沉默”。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "凡有求，除非你没收到，否则你都在应。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P007", "quote": "回应就是应。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "“没有回应”，也是一种回应。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "凡有求，必有应，只不过有些回应的接受者不喜欢自己所收到的回应", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P010", "quote": "never take no for an answer的态度——算不算“求助”？", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P011", "quote": "求助，有“不达目的誓不罢休”的逻辑吗？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P012", "quote": "讨债，才有这不达目的决不罢休的逻辑。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P013", "quote": "很多人哪里是在求助，ta们是自认为对方有债欠自己", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P015", "quote": "那只是以“求助”为形式的“索债”行为", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P016", "quote": "直到把可以通过这个行为品味自己的善良感的人的“善良余额”耗尽为止", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P017", "quote": "当然，事实上也耗不尽，因为总有新毕业的新好人带来新投资", "relation": "qualifies"},
    {"key": "E013", "paragraph_id": "P022", "quote": "有几个真的在求助的得到了帮助？有几个说帮人的真的帮到了人？", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P023", "quote": "还是只是培养出了更多新的喝粥侠？", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "乐不乐于助人，你事实上只有“有求必应”这一种反应——这是指回应，不是指答应。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P025", "quote": "你要记住，你要管理清楚你的回应。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P026", "quote": "确保你有限的帮助余额落到确实是求助的人手里", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P027", "quote": "这是最起码的门槛。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P028", "quote": "即使到了这个门槛，你也要当心有时候对方要的东西你没有，或者对方要的你不能给。", "relation": "qualifies"},
    {"key": "E020", "paragraph_id": "P029", "quote": "在这门槛之上，再考虑帮的事。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际伦理", "助人行为与边界", "语言／概念辨析", "互惠与债务感"],
   "issue_candidates": ["乐于助人与有求必应的区分", "沉默是否算回应", "以求助为形式的索债", "善良资源被消耗", "拒绝与门槛"],
   "text_function_candidates": ["答疑", "概念辨析", "论辩", "经验总结", "行动建议"],
   "object_candidates": ["提问者", "求助者", "索债者（“ta们”）", "新好人", "善心人"],
   "working_keywords": ["乐于助人", "有求必应", "应", "回应", "答应", "沉默", "求助", "索债", "人情债", "义理债", "善良余额", "never take no for an answer", "喝粥侠", "门槛"]
  },
  "notes": "无图片。P002／P007／P008 等把“应”界定为回应而非答应，是本篇核心的概念区分。P010 起作者把提问的区分问题改写为对请求方性质的判断（求助 vs 以“求助”为形式的索债）。P016 与 P017 存在“耗尽／耗不尽”的张力，已在 unresolved_questions 登记。P017—P023 为比喻性叙事（市场、善堂施粥、喝粥侠），非实际事件或数据。brief 与正文高度重合，未据 brief 立论。"
 },
 "4ab974b7": {
  "analysis": {
   "question_context": "提问者自述在外学艺术、自认有些小天赋、不喜社交、内心看不上周围人、又觉得这种想法幼稚，长期独来独往，问“这样的性格需要改变吗”（Q001 提问字段与 P002 引用块均属提问者自述，不得归给作者）。作者先把该陈述固定下来，声明免得将来描述修改后答案失去指向（P001）；其回应不直接说“改”或“不改”，而是区分不可控与可控，主张不必追求变得和大多数人一样，并把方向定为“成为一匹好马”与继续发展（P004—P010、P016、P017）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "方法声明：先把提问者的陈述固定下来，免得将来描述修改后答案失去指向。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "引用提问者自述（引用块）：学艺术、有小天赋、不喜社交、看不上周围人又自责、长期独处，问是否要改。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "前提：人群中自然有出类拔萃者，或因幸运或因天赋对所学真正深入，摆脱多数人受困的看似“快乐”的干扰，走上多数人没机会选择的道路。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "推出不可逆：看到、学会、想到的无法收回，没可能“退回去”或“改掉”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "论证“变得和大多数人一样”既做不到、也没必要、也不应该；勉强“接近群众”会更深刺激“群众”，因为ta们更不能接受特意假装不优越（纡尊降贵）。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P006", "P007"], "summary": "比喻论证：小马发现自己不是鹿，无法通过“变成鹿”解决问题，硬要办只会加倍坏；它只能选择是否成为一匹好马。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P008", "P009"], "summary": "可控与不可控的区分：想法产生不可控、表达可控；高效能不可抛弃、用途可控。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P010"], "summary": "行动建议：习惯和接受这种“孤独”，去考虑“变成一样”之外的解决办法。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P011", "P012", "P013"], "summary": "预测与限定：孤独不会享受太久，合理来说会前往到处都是同类的地方；若不停留向前进，最后一定会遇到越不过其阴影边缘的巨人；在此之前会不断再离开。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P014", "P015", "P016"], "summary": "行动建议：到那时去学这一位如何处理你现在处理的问题，思考为何技术能力超越ta仍不认为自己在ta“之上”；去学那些东西而不要想着“变回去”。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P017"], "summary": "结论：发展的问题，只能用进一步发展解决。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明先把提问者的陈述固定下来，免得将来描述被修改后答案失去指向。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者自述：自认有小天赋、不喜社交、内心看不上周围人、又觉得这种想法幼稚而矛盾，长期独来独往，问这样的性格是否需要改变。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人群中自然会有出类拔萃的人，他们或因幸运或因天赋，对自己所学有了真正深入，摆脱了困扰大多数人的看似“快乐”的干扰，走上大部分人都没机会选择的道路。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为你看到的不能忘记、学会的不能假装没学会、想得到的不能假装想不到，这是没可能“退回去”或者“改掉”的。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为把自己变得和大多数人“一样”以求“不孤独”，既做不到、也没必要、也不应该；勉强挤出的“接近群众”反而会更深刺激“群众”，因为ta们更不能接受“特意假装不优越”（纡尊降贵）。", "evidence": ["E005", "E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以小马发现自己不是鹿为喻：它无法通过“变成鹿”解决自己不是鹿的问题，硬要办只会无意义损耗生命和青春、得到加倍坏的结果，甚至让对方觉得受侮辱。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者由比喻得出结论：它只能选择是否成为一匹好马。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分可控与不可控：无法控制自己会不会产生一个想法，但可以控制要不要表达；无法抛弃自己的高效能，但可以控制把它用在哪里。", "evidence": ["E009", "E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议习惯和接受这种“孤独”，去考虑“变成一样”之外的解决这些孤独的办法。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者预测：合理来说这种孤独不会享受太久，很快就会前往到处都是同类的地方；若不停留向前进，最后一定会遇到一辈子越不过其阴影边缘的巨人，只有这些地方才可能是稳定的栖身之所；在此之前会不断再离开。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议到那时去学这一位如何处理你现在处理的问题，思考为何即使技术能力超越了ta仍不会认为自己在ta“之上”，并去学那些东西而不要想着“变回去”。", "evidence": ["E015", "E016"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的结论：发展的问题，只能用进一步发展解决。", "evidence": ["E017"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "对“这样的性格需要改变吗”，作者的回应方向是：看到／学会／想到的无法“退回去”或“改掉”，可改变的是表达与用途，故应接受这种孤独并继续发展，而不是把自己变得和大多数人一样。", "evidence": ["E004", "E009", "E011"]}
   ],
   "argument_steps": [
    "声明先把提问者的陈述固定下来，免得将来描述修改后答案失去指向（P001）。",
    "引用提问者的自述作为被回应的对象（P002，属提问者）。",
    "给出前提：人群中自然有出类拔萃者，或因幸运或因天赋对所学真正深入，摆脱多数人受困的“快乐”干扰，走上多数人没机会选择的道路（P003）。",
    "推出不可逆：看到、学会、想到的无法收回，没可能“退回去”或“改掉”（P004）。",
    "论证“变得和大多数人一样”既做不到、也没必要、也不应该，且勉强“接近群众”会更深刺激“群众”（P005）。",
    "以小马不是鹿、只能选择是否成为好马作比喻论证（P006、P007）。",
    "区分可控与不可控：想法与高效能不可控／不可抛弃，表达与用途可控（P008、P009）。",
    "给出方向：习惯并接受孤独，另找解决办法（P010）；并预测将遇到同类与“巨人”（P011—P013）。",
    "进一步行动建议：学“巨人”如何处理同一问题，去学那些东西而不要想“变回去”（P014—P016）。",
    "结论：发展的问题，只能用进一步发展解决（P017）。"
   ],
   "concept_usage": [
    {"term": "清高自傲", "meaning": "提问者自述中的自我描述用词（P002）；作者正文未沿用，改用“出类拔萃”“真正的深入”（P003）与“自居优越”（P005）来讨论。", "evidence": "P003", "ambiguity": "作者是否认可提问者“清高自傲”的自我描述，本文未直接表态。"},
    {"term": "“退回去”／“变回去”", "meaning": "指把已获得的见识、能力与高效能假装没有、回到与大多数人一样的状态（P004、P016）。", "evidence": "P016", "ambiguity": "无。"},
    {"term": "纡尊降贵", "meaning": "作者用来指“其实自居优越为了照顾可怜人的感受特意假装不优越”（P005）。", "evidence": "P005", "ambiguity": "作者以此解释“接近群众”为何失败，属作者判断。"},
    {"term": "孤独", "meaning": "本文指因与周围人不同、找不到同类而产生的处境；作者主张习惯与接受，并另寻解决办法（P010、P011）。", "evidence": "P010", "ambiguity": "作者承认它需要被解决，同时又说不会持续太久。"},
    {"term": "高效能", "meaning": "作者认为无法抛弃、只能选择用途的东西（P009）。", "evidence": "P009", "ambiguity": "具体所指（学习能力或产出效率）本文未界定。"},
    {"term": "巨人", "meaning": "指“一辈子越不过其阴影边缘”的更高者，作者认为只有这类地方才可能是稳定的栖身之所（P012）。", "evidence": "P012", "ambiguity": "为比喻性说法，未给出具体指称。"},
    {"term": "马／鹿", "meaning": "比喻（P006）：小马发现自己不是鹿，不能变成鹿，只能选择是否成为好马。", "evidence": "P006", "ambiguity": "标题“指马为鹿”未在正文中解释，二者关系属研究助手的观察。"}
   ],
   "examples_and_targets": [
    "一匹小马发现自己不是鹿（P006）：作者的核心比喻，非实际人物或事件。",
    "一辈子越不过其阴影边缘的巨人（P012）：作者设想的更高者，作为学习对象。",
    "提问者自述的场景（在外学艺术、同学 deadline fail 后哭、周末去博物馆画展、只能与父母倾诉）（P002）：引用的提问者材料，非作者例证。",
    "反驳对象：作者反驳的是“通过把自己变得和大多数人一样来解决孤独”的做法（P005、P010、P016），以及“为了照顾可怜人的感受特意假装不优越”的纡尊降贵（P005）。"
   ],
   "conditions": [
    "前提给出两种来源且未穷尽：“或者出于幸运，或者出于天赋”（P003）。",
    "反效果以条件为前提：“你这样勉强一番硬挤出来的‘接近群众’”（P005）、“硬要办”（P006）。",
    "预测带限定词：“合理的来说”“很快”（P011）；条件句“如果你不停留的向前进……最后你一定会遇到”（P012）。",
    "行动建议以“到时候”（遇到巨人之后）为条件（P014）。",
    "作者未界定“改”的对象是行为、表达还是内心，只在“表达／用途可控”上给出区分（P008、P009）。",
    "正文针对的是提问者学艺术、自认有天赋、不喜社交的具体情形，是否适用于其他情形本文未说明。"
   ],
   "rhetoric_and_tone": "全篇第二人称“你”直接对话提问者，训诫与劝慰混合。引号强调密集（“一样”“不孤独”“群众”“退回去”“改掉”“变回去”“之上”）。比喻链：小马／鹿／好马（P006、P007）、巨人（P012）。含一个反问“难道我们就脆弱到需要你这样来可怜吗？”（P006）。格言式收尾“发展的问题，只能用进一步发展解决。”（P017）。P001 先声明固定提问者陈述，属方法论说明。",
   "unresolved_questions": [
    "作者未直接给出“要改”或“不要改”的判断，而是区分不可控与可控、并把目标改为“成为一匹好马”与继续发展；这是否构成对提问的正面回答，本文未说明。",
    "P002 为提问者自述的引用块，内容归属提问者；作者仅在 P001 声明“把这陈述固定下来”，未逐条评价。",
    "P003“出类拔萃”“真正的深入”的判定标准，本文未说明。",
    "P011“很快会前往到处都是同类的地方”、P012“最后你一定会遇到……巨人”属作者预测，无时间尺度与条件保障。",
    "标题“指马为鹿”与正文“一匹小马发现自己不是鹿”的呼应关系为研究助手的观察，作者未在正文解释标题。",
    "无图片。P002 在记录中按段落转录上限截断（sample_truncated），本篇对其短引均取自截断范围内并与语料原文核对。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "先把这陈述固定下来，免得将来描述修改了这答案失去指向。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "我是在外学艺术的学生，自认有些小天赋，喜欢自己做事，不喜社交。", "relation": "context"},
    {"key": "E003", "paragraph_id": "P003", "quote": "人群中自然会有一些出类拔萃的人存在", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "这是没可能“退回去”或者“改掉”的。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "你既做不到，也没有必要、也不应该去追求把自己变得和大多数人“一样”", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "ta们更不能接受“其实自居优越为了照顾可怜人的感受特意假装不优越”——也就是纡尊降贵。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "一匹小马发现自己不是鹿，它无法选择通过“变成鹿”来解决自己不是鹿的问题", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "它只能选择是否成为一匹好马。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "你无法控制自己会不会产生一个想法，你可以控制你要不要表达这个想法。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P009", "quote": "你无法抛弃自己的高效能，你可以控制你要把这高效能用在哪里。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P010", "quote": "你要习惯和接受这种“孤独”", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P011", "quote": "这种孤独你并不会享受太久", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P012", "quote": "最后你一定会遇到一辈子越不过其阴影边缘的巨人", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P013", "quote": "你其实会不断的再离开。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P014", "quote": "到时候你去学一下这一位是如何处理你现在处理的这个问题的。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P016", "quote": "你要去学那些东西，而不要想着“变回去”。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P017", "quote": "发展的问题，只能用进一步发展解决。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["个人成长与自我认知", "天赋与孤独", "艺术学习环境", "社交与群体适应"],
   "issue_candidates": ["清高自傲要不要改", "是否应把自己变得和大多数人一样", "孤独的处理", "可控与不可控的区分", "纡尊降贵式接近群众"],
   "text_function_candidates": ["答疑", "劝慰", "训诫", "比喻论证", "经验总结"],
   "object_candidates": ["提问者（学艺术的学生）", "周围人／“群众”", "巨人", "小马与鹿（比喻）"],
   "working_keywords": ["清高自傲", "小天赋", "社交", "孤独", "一样", "退回去", "变回去", "纡尊降贵", "高效能", "巨人", "好马", "发展"]
  },
  "notes": "无图片。P002 为 lexical quote 节点，内容属提问者自述（attribution=questioner），不得归给作者；作者仅在 P001 声明把该陈述固定下来。P002 在记录中按段落转录上限截断（sample_truncated），本篇对其短引取自截断范围内并与语料原文核对。P010 原文“变成一样“之外”引号方向相反，照录未改。标题“指马为鹿”与 P006 小马／鹿比喻的呼应为研究助手的观察，作者未在正文解释标题。正文针对提问者学艺术、有天赋、不喜社交的具体情形，是否适用于其他情形本文未说明。"
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
