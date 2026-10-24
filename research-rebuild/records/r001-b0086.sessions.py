# -*- coding: utf-8 -*-
"""批次 r001-b0086 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0086.sessions.py            # 写 out/r001-b0086.out.jsonl
  python3 records/r001-b0086.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0086"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0086.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "6eda17f3": {
  "analysis": {
   "question_context": "提问者问：离婚陷入困境，是否可以去对方单位“求施压”解决（Q001，属提问者，不在作者名下）。作者不直接回答可否，而是假设了一个“乌有国白梦市容大姐”的故事：以送礼、交友、拜访领导的方式经营关系，最后客客气气离婚、领导反而叮嘱老赵善待她；再由此引出对“力量”外形的判断与行动建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "虚构故事：容大姐去单位送新年礼物、加青年群、拜访领导感谢其对外子的关心，领导感动并当众叮嘱老赵善待她。", "role": "example"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "结局：容大姐完全没有闹，双方客客气气把婚离了。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "作者评断：真正的力量可以温柔到人无话可说，其间的智慧、坚强和力量会让有心人懂得敬畏。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "限定：这不是让人有样学样、东施效颦，容大姐这种级别的人不是谁都能学；只是借她说明力量看起来是什么样。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "力量的外形：不是哭哭啼啼、自怨自艾、哀怨苦闷，而是安然自若、举重若轻、出乎意料；作者称对这种气度的敬畏写在有战逃本能的高等生物思维底层，狼也不敢轻慢，只会想逃。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019"], "summary": "行动建议与结论：冷静、温柔下来再去解决问题；问题若谈得上解决，几乎总是这样解决的；靠三杯老酒拼鱼死网破虽也可能指向某种结束，但那不被称为“解决”。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以容大姐的故事说明：真正的力量可以温柔到让人无话可说，其间的智慧、坚强和力量会让有心人懂得敬畏。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "negated", "statement": "作者限定：故事不是在让人有样学样、东施效颦，容大姐这种级别的人不是谁都能学的。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称力量永远不是哭哭啼啼、自怨自艾、哀怨苦闷的，一定是安然自若、举重若轻、出乎意料的。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言这种气度写进了一切有战逃本能的高等生物的思维底层，并以狼不敢轻慢能直视它眼睛、泰然自若而超出它预料的存在为例。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者建议冷静、温柔下来再去解决问题；若问题谈得上解决，它几乎总是这样解决的。", "evidence": ["E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称靠三杯老酒拼着鱼死网破去“解决问题”也可能指向某种结束，但那种结束不会被称为“解决”。", "evidence": ["E010"]}
   ],
   "argument_steps": [
    "承接提问（离婚困境求助单位施压）：不直接作答，改以“我给你说个故事吧”引入虚构案例。",
    "例证：容大姐以送礼、交友、加群、专门拜访领导的方式经营单位关系，领导当众表示感动与感谢。",
    "结果：容大姐完全没有闹，双方客客气气把婚离了。",
    "评断：真正的力量可以温柔到人无话可说；这种气度会让有心人敬畏。",
    "让步/限定：不是要人有样学样，容大姐这种级别不是谁都能学；目的只是说明力量看起来是什么样。",
    "外形定义：力量不是哭哭啼啼、自怨自艾、哀怨苦闷，而是安然自若、举重若轻、出乎意料。",
    "理由（生物学类比）：对这种气度的敬畏写在有战逃本能的高等生物思维底层，狼对超出预料者只会想逃。",
    "行动要求：冷静，然后温柔下来，然后去解决问题。",
    "结论/对照：问题几乎总是这样解决的；鱼死网破式的“解决”只是结束，不叫解决。"
   ],
   "concept_usage": [
    {"term": "力量", "meaning": "非情绪化的、安然自若而超出对方预料的气度，表现为“温柔到人无话可说”；与激动、哭闹、拼命相对。", "evidence": "P008", "ambiguity": "未给出可操作的判定标准，仅以外形与故事示例；作者自己承认这种级别“不是谁都能学”。"},
    {"term": "解决", "meaning": "以冷静、温柔方式达成的问题处理结果；与“某种结束”相区分。", "evidence": "P018", "ambiguity": "未说明究竟解决什么、以什么标准算解决。"},
    {"term": "战逃本能", "meaning": "作者用以解释“敬畏气度”具有跨物种普遍性的生物学式说法。", "evidence": "P014", "ambiguity": "属作者的类比/断言，文中未提供来源，需外部核查。"},
    {"term": "施压", "meaning": "提问者所问的“去单位求施压解决”做法；作者未直接使用该词评断，只用“闹/没有闹”作对照。", "evidence": "P006", "ambiguity": "作者对“去单位施压”本身是否可行未作明说，只给出容大姐这一替代路径。"}
   ],
   "examples_and_targets": [
    "容大姐（虚构人物，作者自述“我给你说个故事吧”的故事主角，作为正面示例）",
    "乌有国白梦市（虚构地名，明确标示故事为虚构）",
    "老赵（故事中容大姐的配偶，被领导叮嘱善待妻子的一方）",
    "单位领导（故事中的机构角色，对容大姐致谢并当众表态）",
    "单位小青年群、单身困难户（故事细节：容大姐以介绍对象交朋友）",
    "狼（作者用以类比“战逃本能”的动物例证）",
    "“三杯老酒拼着鱼死网破”（作者使用的反面修辞材料，指情绪化的解决方式）"
   ],
   "conditions": [
    "故事前提是虚构：“我给你说个故事吧，在乌有国白梦市”（P001）。",
    "限定不建议照搬：容大姐这种级别的人不是谁都能学（P010）。",
    "作者以“如果问题谈得上解决的话”为条件表述问题的可解决性（P018）。",
    "对照条件：靠酒劲拼鱼死网破虽可能指向某种结束，但不被称为“解决”（P019）。"
   ],
   "rhetoric_and_tone": "以“我给你说个故事吧”开头，用虚构故事代替直接答疑；叙述中带调侃式反讽（领导拍着老赵的肩膀说“贤内助”“可不能在家给咱们容大姐受委屈”），把单位话语移植到离婚场景制造荒诞感；结论句为格言式短句（“真正的力量可以温柔到人无话可说”）；对读者用第二人称“你/你们”训诫，并预设“你”可能想去东施效颦而先行制止。",
   "unresolved_questions": [
    "故事为作者明示的虚构（乌有国白梦市），其中的单位反应不能视为现实机构行为的证据。",
    "作者未直接回答“能否去单位求施压”；替代路径是否普遍有效、适用何种单位与地域，文中未说明。",
    "“战逃本能”“高等生物”等说法属断言，文中无来源，需外部核查。",
    "“力量”缺乏可判定的标准，作者亦称此级别“不是谁都能学”，读者如何自处未说明。",
    "未说明容大姐婚姻的实质争议（财产、子女、过错等），无法判断该做法的代价。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P008", "quote": "真正的力量可以温柔到人无话可说。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P009", "quote": "每一个有眼睛、有耳朵、有脑袋的人，都会懂得敬畏", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P010", "quote": "这并不是在告诉你要去有样学样、东施效颦", "relation": "qualifies"},
    {"key": "E004", "paragraph_id": "P010", "quote": "容大姐这种级别的人不是谁都能学的", "relation": "qualifies"},
    {"key": "E005", "paragraph_id": "P013", "quote": "它永远不是哭哭啼啼、自怨自艾、哀怨苦闷的，它一定是安然自若、举重若轻、出乎意料的。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P014", "quote": "是写进了一切有战逃本能的高等生物的思维底层的", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P015", "quote": "即使只是一头狼，也不敢轻慢能直视着它的眼睛，泰然自若，而超出它预料的存在。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P017", "quote": "冷静，然后温柔下来，然后去解决问题。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P018", "quote": "如果问题谈得上解决的话，它几乎总是这样解决的。", "relation": "qualifies"},
    {"key": "E010", "paragraph_id": "P019", "quote": "但那种结束不会被称为“解决”。", "relation": "contradicts"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚姻与离婚", "人际策略与权力", "情绪与自我管理"],
   "issue_candidates": ["离婚僵局中向对方单位施压的可行性", "强硬与温柔两种影响力的效果", "情绪化对抗的代价"],
   "text_function_candidates": ["答疑", "叙事", "训诫"],
   "object_candidates": ["容大姐（虚构）", "老赵（虚构）", "单位领导（虚构）", "乌有国白梦市（虚构）"],
   "working_keywords": ["施压", "闹", "力量", "温柔", "敬畏", "战逃本能", "东施效颦", "鱼死网破", "解决"]
  },
  "notes": "本篇无图片节点，正文完整可读（20 段）。P001 起为作者明示的虚构故事（“乌有国白梦市”），已按作者自述标注为虚构示例，未当作现实案例。提问者的问题（去单位求施压）与作者主张已分开：作者未直接评断该做法本身。"
 },
 "f7bb2986": {
  "analysis": {
   "question_context": "提问者问“如何成为一个能独立思考的人”（Q001，属提问者）。作者不提供方法，而先判定该提法本身有问题：认为“非独立思考”这一功能并不存在，问题里的“独立思考”实指一种思考质量标准的指征，并由此展开对“与众不同”崇拜的归因与三条标准。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "判定这是伪问题：人不是心灵感应集群中的计算单元，没有“非独立思考”的功能；所谓独立思考指的是思考的质量标准，而非思考的方式。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "归因：这是存在感焦虑的表现；人想通过不同证实自己存在，把结果与众不同的思考视为“独立”的证据，其实是“可以证明我也是独立的个体的思考”的缩写，不是敢于不同而是不敢相同，是思想的青春期症状。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "以卖烟类比：舆论场高举“可以证明自己独立的思考”，是被“幼稚资源”诱发的现象；如同卖烟者鼓吹吸烟彰显男性气概，吸烟与男性气概无真实关系，结论反主流与独立人格的关系也是鬼扯蛋。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"], "summary": "反驳“与众不同=独立人格”：独立人格无惧于与众不同也往往与众不同，但与众不同不能作为绝对识别标准，因为与众不同是天生的、人人都有。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "归因（崇拜机制）：被恭称为独立思考的人，不是因为与众不同，而是因为被认为成功、优秀、精英，其地位、影响力尤其性资源让人艳羡；人们想用最便宜的仿形巫术转移其魔力，如同画虎斑假装猛虎转世，“思想逆反”就是这虎斑彩绘。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026"], "summary": "三条建议的前两条：独立思考不需要学，任何思考本来就是独立的，谁说你“不是独立思考”就是想骗你“买烟”；与众不同也不需要学，你想与众皆同还做不到。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "第三条与标准：人们说谁独立思考，是因为崇拜其思考质量；关键在站得住脚（内部无逻辑矛盾和脱节）、自我注释（不被自己不能注释的其他文献决定）、有解释力。以引用函数的代码类比：引用源头者会随源头被改，把源头复制进自己定义者才独立。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047"], "summary": "结论与收束：有解释力指内在无矛盾、对外无依赖的理论可以解释现实并让人对其预测性有乐观期待，这种乐观期待是信仰的根基；能达到三条标准的人会引人寄托信仰，古代喊般若菩提，现在喊“独立思考”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称提问是伪问题：人类不是心灵感应连接的思考集群中的计算单元节点，根本没有“非独立思考”这个功能；输入、计算、输出之间没有别人。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称问题里的“独立思考”不是指思考的方式，而是指一种有特殊指征的思考，即某种思考的质量标准。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把对独立思考的追求归因于存在感焦虑：人想通过不同证实自己的存在，把结果与众不同的思考当作自己独立于他人的证据，其实那不是独立思考，而是“可以证明我也是独立的个体的思考”。", "evidence": ["E004", "E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这种追求不是“敢于不同”，而是“不敢相同”，是一种思想的青春期症状。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“结论反主流”与“独立人格”之间的关系是鬼扯蛋，并举卖烟者鼓吹“吸烟彰显男性气概”作类比，反问吸烟与男性气概有何真实关系。", "evidence": ["E009", "E010", "E011"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者承认独立人格无惧于与众不同且往往与众不同，但断言与众不同不能视为独立人格的绝对识别标准，因为与众不同是天生的、每个人都绝对与众不同。", "evidence": ["E012", "E013"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称被加封为“有独立人格”从而思考被恭称为“独立思考”的人，不是因为他们有多与众不同，而是因为被认为很成功、很优秀、很精英，其地位、影响力尤其是性资源让人艳羡。", "evidence": ["E014", "E015"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第一条建议：独立思考不需要学，任何思考本来就是独立的；谁说你“不是独立思考”，你叫他有多远滚多远——这是想骗你“买烟”。", "evidence": ["E016", "E017"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第三条：人们说谁谁是独立思考，只是因为崇拜那人的思考质量；真正的问题不在于与众不同，而在于站得住脚、自我注释、有解释力。", "evidence": ["E018", "E019"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出标准含义：站得住脚指内部没有逻辑矛盾和脱节；自我注释指不被它自己所不能注释的其他文献决定；有解释力指内在无矛盾、对外无依赖的理论可以解释现实，从而让人对其预测性有乐观期待。", "evidence": ["E020", "E021", "E022"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以编程函数类比独立性：引用源头函数者会随源头被改而被改，把源头直接复制进自己定义者虽有很多外来内容却已经独立；并称独立未必就一定不同。", "evidence": ["E023", "E024", "E025"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“乐观期待”就是信仰的根基，能达到三条标准的人会引人寄托信仰；寄托信仰者以顶礼膜拜表达信仰，是人类处置自己焦虑的根本机制，古代喊般若、菩提，现在喊“独立思考”。", "evidence": ["E026", "E027", "E028"]}
   ],
   "argument_steps": [
    "先否定提问的前提：这是伪问题，不存在“非独立思考”的功能（P001—P003）。",
    "重新界定提问中的关键词：独立思考指思考的质量标准，而非思考方式（P004）。",
    "归因一：这是存在感焦虑的表现，人通过“与众不同”证明自己的独立（P005—P007）。",
    "反讽定性：不是敢于不同，而是不敢相同；是思想的青春期症状（P008—P009）。",
    "社会机制：舆论场高举“能证明独立的思考”是被易利用的“幼稚资源”诱发；类比卖烟鼓吹男性气概（P010—P013）。",
    "让步：独立人格确实无惧且往往与众不同；反驳：与众不同是天生的、人人都有，故不能作识别标准（P014—P016）。",
    "归因二：被称独立者实因被视为成功、优秀、精英，其地位影响力性资源令人艳羡；崇拜靠仿形巫术（虎斑彩绘）（P017—P020）。",
    "行动建议：第一条独立思考不需学、说你不是独立的人在骗你买烟；第二条与众不同不需学（P021—P025）。",
    "第三条与质量标准：站得住脚、自我注释、有解释力（P026—P029）。",
    "例证/类比：引用别的文件而不知其意 vs 弄清意思后自己宣布认同；引用函数 vs 复制源头函数（P029—P039）。",
    "补充：独立未必就一定不同（P040）。",
    "结论：有解释力→可解释现实→对预测性有乐观期待→这乐观期待是信仰的根基→达到标准者引人寄托信仰（P042—P047）。"
   ],
   "concept_usage": [
    {"term": "独立思考", "meaning": "作者否认它指某种思考方式（因为不存在非独立思考），转而指一种有特殊指征的思考，即思考的质量标准。", "evidence": "P004", "ambiguity": "作者一面说“独立思考不需要学、任何思考本来就是独立的”，一面又给出三条质量标准，两个用法（本体义/质量义）在文中并存，需注意区分。"},
    {"term": "独立", "meaning": "以编程函数类比：不随所引用的源头被改动而改动，即把源头内容纳入自己定义；独立未必不同。", "evidence": "P039", "ambiguity": "与“与众不同”被明确切开，但“内在无矛盾、对外无依赖”如何实际操作未说明。"},
    {"term": "与众不同", "meaning": "天生的、人人具备的个体差异；作者否认它可作为独立人格的绝对识别标准。", "evidence": "P015", "ambiguity": "作者一面承认独立人格“往往有显而易见的与众不同”，一面否认其判别力。"},
    {"term": "自我注释", "meaning": "不被它自己所不能注释的其他文献决定；即不引用自己说不清来源的内容。", "evidence": "P029", "ambiguity": "术语为作者自造，文中以“上一份文件说得很对但我不知道它是什么意思”等例子说明。"},
    {"term": "有解释力", "meaning": "内在无矛盾、对外无依赖的理论可以解释现实，从而让人对其预测性有乐观期待。", "evidence": "P042", "ambiguity": "未给出解释力的检验方式，且“乐观期待”本身被作者引向信仰而非认识论标准。"},
    {"term": "信仰", "meaning": "对思考质量标准的寄托与顶礼膜拜，被称为人类处置自己焦虑的根本机制。", "evidence": "P045", "ambiguity": "与宗教用法（般若、菩提）并置，作者未区分。"},
    {"term": "仿形巫术", "meaning": "作者用以指幻想以最便宜的方式转移他人魔力的机制（画虎斑假装猛虎转世）。", "evidence": "P019", "ambiguity": "人类学式说法，文中无出处，需外部核查。"}
   ],
   "examples_and_targets": [
    "卖烟的人鼓吹“吸烟彰显男性气概”（作者类比材料，用以说明舆论场对“独立思考”的高举）",
    "画上虎斑假装猛虎转世的仿形巫术（作者类比/修辞材料）",
    "引用了其他函数的函数 Function your_thought(){Return 1 + original_thought()}（作者示例/类比，说明依赖）",
    "复制源头函数 function your_thought(){return 1+3}（作者示例/类比，说明独立）",
    "“我很同意某A，但是某A是什么意思，你去问某A”与“我听了某A的一番论述，我认为是某某意思，我宣布我认同我理解的这个意思”（作者对比示例，说明自我注释）",
    "隔壁家小孩（作者用于反问“真一样，你妈还会叫你向隔壁家小孩学习吗？”的日常例）",
    "般若、菩提（作者引用的宗教用语，用于对照“现在ta们喊独立思考”）",
    "被崇拜的“独立思考者”与其艳羡者（作者归因对象：性资源、地位、影响力带来的崇拜）"
   ],
   "conditions": [
    "“独立思考”被重新定义为质量标准的用法下，作者的三条标准才适用（P004、P027）。",
    "作者对独立人格作了让步式限定：“独立人格的确无惧于与众不同，也往往有显而易见的与众不同”（P014）。",
    "自我注释的成立条件是能自己注释所引文献，而非“你去问某A”（P029—P031）。",
    "独立性被限定为“未必就一定不同”（P040）。",
    "结论以“能达到这三条标准的人”为前提（P044）。"
   ],
   "rhetoric_and_tone": "全篇为反讽与训诫语气：开头“老实说，这是一个伪问题”直接否定提问；大量口语化贬斥（“鬼扯蛋”“有多远滚多远”）；用反问推进（“中间哪有别人？”“实际上吸烟跟男性气概有啥真实的关系？”“真一样，你妈还会叫你向隔壁家小孩学习吗？”）；两处要求读者确认（“看得明白吗？”“看懂了吗？”）；结构上用“记住以下几条——第一/第二/第三”列表化，末尾以“如此而已”收束，语气从讥讽转为断言式的宗教对照。",
   "unresolved_questions": [
    "作者既称“独立思考不需要学”，又给出三条质量标准，两者关系（本体独立 vs 质量独立）未说明。",
    "三条标准如何操作化、由谁判定“站得住脚/有解释力”，文中未给出可检验的方法。",
    "“性资源”“幼稚资源”“仿形巫术”等说法属断言，无文献出处，需外部核查。",
    "P034、P038 为英文代码行，原文大小写混用（Function/Return），未说明是否为作者原文如此（此处按原文保留）。",
    "作者对“非独立思考不存在”的论证仅以“人不是心灵感应集群节点”一句带过，未处理社会影响、宣传、教育等可能情形。",
    "P019 一处疑为笔误或语病：“其原理在身上画上虎斑假装自己猛虎转世没有区别”，语义需核对。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "根本就没有“非独立思考”这个功能", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "你得到输入，你计算，你输出。中间哪有别人？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "不是在指思考的方式，而是在指某种思考的质量标准。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "这只是存在感焦虑的一种表现。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "人想要通过不同来证实自己的存在。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "而是“可以证明我也是独立的个体的思考”，缩写为“独立思考”罢了。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "这不是“敢于不同”，而是“不敢相同”。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "其实只是一种思想的青春期症状。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P013", "quote": "“结论反主流”与“独立人格”之间的关系也是鬼扯蛋。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "就好像急于卖烟的人鼓吹“吸烟彰显男性气概”一样。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "实际上吸烟跟男性气概有啥真实的关系？", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "与众不同根本不能视为独立人格的绝对识别标准", "relation": "qualifies"},
    {"key": "E013", "paragraph_id": "P015", "quote": "因为与众不同是天生的，每个人都绝对的与众不同", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P017", "quote": "而是因为ta们被认为很成功、很优秀、很精英。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P018", "quote": "其享有的地位、影响力，尤其是性资源让人艳羡不已。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P022", "quote": "独立思考不需要学，任何思考本来就是独立的。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P022", "quote": "这是想骗你“买烟”。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P026", "quote": "只不过是因为ta们在崇拜那人的思考质量。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P027", "quote": "问题不在于与众不同，而在于站得住脚，自我注释，而且有解释力。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P028", "quote": "站得住脚，是指内部没有逻辑矛盾和脱节。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P029", "quote": "自我注释，是因为它并不被它自己所不能注释的其他文献决定。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P042", "quote": "可以解释现实，从而可以让人对它的预测性有乐观期待。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P036", "quote": "引用的源头改了，你也就随之被改了。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P039", "quote": "但是后者却已经是独立的，这时候修改源头，根本不会影响到这个函数的定义。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P040", "quote": "独立未必就一定不同。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P043", "quote": "这个“乐观期待”，就是信仰的根基。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P044", "quote": "能达到这三条标准的人会引人寄托信仰。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P046", "quote": "在古代ta们喊般若、菩提，现在ta们喊“独立思考”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["思维与认知", "社会心理与舆论", "信仰与崇拜现象"],
   "issue_candidates": ["独立思考的界定", "与众不同能否作为独立人格的判据", "舆论场对独立思考的推崇机制", "思考质量的三条标准"],
   "text_function_candidates": ["答疑", "论辩", "批评", "解释"],
   "object_candidates": ["提问者（匿名）", "被称“有独立人格”的精英及其崇拜者", "卖烟者（类比）", "某A（举例用代称）"],
   "working_keywords": ["独立思考", "伪问题", "存在感焦虑", "与众不同", "独立人格", "站得住脚", "自我注释", "解释力", "信仰", "虎斑彩绘", "仿形巫术"]
  },
  "notes": "本篇无图片节点，正文完整可读（47 段）。P034、P035、P038 为代码示例行，已按原文保留大小写；P019 疑有笔误，已登入未决问题，未据以立论。作者对提问的立场为否定式（伪问题），提问者立场未被归入作者主张。"
 },
 "927ba21c": {
  "analysis": {
   "question_context": "提问者问“如何看待一边呼吁女性不要做全职妈妈，一边强调要亲自带娃”（Q001，属提问者，指涉两种并存的社会呼吁）。作者不评断该呼吁本身，而是先把“亲自带娃”定义为“一切都要自己操作”，指出其动机多为对“外包服务”的不信任，再分层给出：动机对子女的后果、对“亲自带孩子”的重新定义（三观引导与受托人）、两个基本问题（无法垄断议题、自己也没有确定答案）及各自回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "界定“亲自带娃”：一般表示“一切都要自己操作”，并列举穿衣系鞋带、接送、做饭喂饭、监督作业、洗澡、铺床哄睡等。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "动机归因：多数情况下出于对“外包服务”的不信任（怕外人不上心、怕父母不够科学、怕娃没得到最高级服务），说白了是无法相信除自己以外的其他人；找不到可托付者或付不起酬劳，也无力察觉纠正他人失职，于是“自己来”。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "后果：因这种理由自己带娃会时时显露沮丧、焦虑和懦弱，成为贯穿子女童年（甚至一生）的“背景辐射”，削弱子女将来领导、参与、识别有效合作关系的可能性；恐惧忌讳至此谈何学习合作技术。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "代价与后果补充：“绝对不容闪失”的代价不只一方放弃职业生涯，还有子女人格影响；其背后是信仰的无能；这种心态会被幼崽察觉并用于“自我绑架”，使人格教育变为虚应故事。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013"], "summary": "前提性主张：动机是一种魔法——物理后果等效的行为因动机不同对目睹者有截然不同的精神影响，并影响过程细节。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018"], "summary": "行动建议：可以大量亲自服务子女饮食起居，但动机不可以是对他人的无法信任；不要在饭桌前感叹人心残酷并炫耀“宁可辛苦也要亲自照顾你”，不要以“外人我信不过”拒绝配偶请阿姨的提议；可以做同样选择但不为该理由。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "重新定义：本质上“亲自带孩子”指在一切世界观、价值观、人生观议题上，尽可能由自己或自己选择的受托人对子女实施引导——仅仅指这个。", "role": "definition"},
    {"unit_id": "U008", "paragraph_refs": ["P022"], "summary": "分解其一（世界观）：世界观是关于“世界是什么样”的一切答案；子女需借用父母的判断力与视野，其幼年学习大纲由父母决定而非学校，学校教师只是父母选择的代理人、执行父母意志——除非父母闭着眼睛随波逐流。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "分解其二（价值观，关键部分）：受欺负、学习沮丧、朋友背叛、孤独、助人被辜负等情境的引导需要父母亲自做；在这些点出现、提供关键建议与指导并保护，是父母真正最重要的职责；作者以“谁在做这件事，谁才是你子女真正的父母”“生父、养父，不如教父/教母”强化。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P035", "P036", "P037"], "summary": "由上述定义引出两个基本问题：一是无法垄断所有此类议题，其他不可避免影响这些议题的事物怎么办；二是自己对这些议题也没有确定答案（以自身三十年短暂迷茫的人生为由）怎么办。", "role": "transition"},
    {"unit_id": "U011", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043"], "summary": "答第一个问题：凡不可避免的就是天意；子女还有一个绝对不可能排除的父母即“这个世界”，它是第一教师、权威在父母之上，子女天生天养；父母作为世界选定的看守者有权善尽判断覆盖能覆盖的部分，其余不容选择的东西是世界给子女的教育；举例统一课纲、学区安排；对于不能选择的条件要顺从良心该对抗对抗、该接受接受，但不可用越理非法手段强行控制，因其可能含超出自身境界的深意，是高于自己、更爱子女的安排；否则难道子女只能照父母的模子塑形。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055"], "summary": "答第二个问题：没有最好的答案不是问题，问题是有没有努力寻找、在分辨不同答案上花了多少实在努力（以“背叛”“信任”各想了多少作反问）；要做的不是给正确答案，而是给尽可能正确的答案，让子女不必从零开始；不是送到终点而是留下路标；教导的作用不是“目的地信标”而是“定位星座”，让子女凭反馈信号去自己的目的地；真正关键的是精确严谨完善地表达“你现在在哪里”，传递的像未完成研究的实验记录，重要的是被精心设计的事实记录与观察总结；不需要主张结论正确，只需让对方明白不继承手册是愚蠢的，对方翻阅时没有义务认同结论。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“亲自带娃”界定为一种“一切都要自己操作”的意思，并列举穿衣系鞋带、接送、做饭喂饭、监督辅导作业、洗澡、铺床哄睡等具体事务。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称绝大多数情况下这样做是出于对“外包服务”的不信任，说白了是因为无法相信除自己以外的其他人。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称若因这种理由而自己带，势必时时处处显示出巨大的沮丧、焦虑和懦弱，会成为贯穿子女整个童年甚至一生的“背景辐射”，极大削弱子女将来领导、参与甚至识别有效合作关系的可能性。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“绝对不容闪失”的代价不只是一方放弃职业生涯，还有子女自身在人格上受到的影响；其背后是信仰的无能。", "evidence": ["E007", "E008"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预言这种心态往往会被充满兽性的幼崽察觉并毫不犹豫地做“自我绑架”的运用，把父母玩弄于股掌之上，令一切人格教育变为虚应故事。", "evidence": ["E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出“动机是一种魔法”：看似物理后果等效的行为出于不同动机，对目睹者的精神影响截然不同，也影响从开端到结果的过程细节。", "evidence": ["E010", "E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的建议：仍然可以大量亲自服务子女的饮食起居，但动机不可以是因为对他人的无法信任；并具体要求不要在饭桌前感慨社会新闻以炫耀自己亲自照顾，不要以“外人我信不过”拒绝配偶请阿姨的提议——可以做一样的选择，但不应该是为这样的理由。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“亲自带孩子”重新定义为：在一切世界观、价值观、人生观议题上，尽可能由自己或自己选择的受托人对子女实施引导，仅仅指这个。", "evidence": ["E015", "E016"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称子女幼年时期的整个学习大纲由父母决定而非学校决定，学校与教师实质上是因父母首肯才被放进子女人生安排，只是父母选择的代理人、执行父母意志——除非父母只是闭着眼睛随波逐流。", "evidence": ["E017", "E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列举受欺负、学习沮丧、遭遇朋友背叛、孤独、助人被辜负等情境，称这些思想引导需要父母亲自做，并称在理念实施中提供密切帮助和保护是父母真正最重要的职责。", "evidence": ["E019", "E020"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“谁在做这件事，谁才是你子女真正的父母”“生父、养父，不如教父。生母、养母，不如教母”强化其定义。", "evidence": ["E021", "E022"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者回答“无法垄断议题”：凡不可避免的就是天意；子女还有一个绝对不可能排除的父母即这个世界，它是子女真正意义上的第一教师、权威在父母之上，子女天生也必定由天养；父母有天然权利去善尽判断覆盖能覆盖的部分，其余不容选择的东西是世界给子女的教育。", "evidence": ["E023", "E024", "E025"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议对不能选择的条件顺从良心该对抗对抗、该接受接受，但不要用越理非法的手段强行控制；并以“它会是你子女人格的很大一个组成部分”“那往往是超越你时代局限和人格缺陷的正确的东西”作为理由。", "evidence": ["E026", "E027"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：否则难道子女只能照着你的模子塑形吗？如果你真的成功了（作者自称幸好这是不可能的），你确信那是绝对最好的答案吗？", "evidence": ["E028", "E029"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者回答“自己也没有确定答案”：没有最好的答案不是问题，问题是有没有努力去寻找这些答案、在分辨不同答案上花了多少实实在在的努力。", "evidence": ["E030", "E031"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称要做的不是给予子女“正确的答案”，而是给出一个尽可能正确的答案，好让子女不至于从零开始、从几乎毫无价值的低级错误开始；不是送到终点，而是沿自己行过的路留下路标。", "evidence": ["E032", "E033"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以三盏灯与定位星座为喻：教导的作用不是“目的地信标”而是“定位星座”，让子女凭反馈信号去自己的目的地，因此父母自己离目的地多近是无关问题，关键是精确、严谨、完善地表达“你现在在哪里”。", "evidence": ["E034", "E035", "E036"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称父母传递的更像一项未完成研究的实验记录，更重要的不是结论而是被精心设计、值得重视、表述良好的事实记录及建立其上的观察总结；不需要主张“我的结论是对的”，只需让对方明白不继承你的手册是愚蠢的，而对方翻看手册时没有义务认同你的结论。", "evidence": ["E037", "E038", "E039"]}
   ],
   "argument_steps": [
    "先问“亲自带娃”指什么，给出“一切都要自己操作”的通俗义与事务清单（P001—P003）。",
    "归因：出于对外包服务的不信任，即无法相信除自己以外的人；条件是不好托付或付不起酬劳（P004—P006）。",
    "后果：这种“自己带”会输出沮丧、焦虑、懦弱，成为子女童年的背景辐射，削弱其识别合作关系的能力（P007—P008）。",
    "代价扩展：“绝对不容闪失”的代价包含子女人格影响，其背后是信仰的无能；且会被幼崽用于自我绑架（P009—P011）。",
    "前提：“动机是一种魔法”，动机不同则精神影响与过程细节不同（P012—P013）。",
    "行动要求：可继续亲自服务，但动机不可为不信任他人；给出两个具体的禁止性例子（P014—P017）。",
    "重新定义“亲自带孩子”：在三观议题上由自己或自己选择的受托人引导（P019—P021）。",
    "分解世界观：子女借父母的判断力与视野，学习大纲由父母而非学校决定，学校教师是代理人（P022）。",
    "分解价值观（关键）：五种情境的引导需父母亲自做，这是最重要的职责；“谁在做这件事，谁才是真正的父母”（P023—P034）。",
    "设问：无法垄断议题、自己也没有确定答案，这两个基本问题怎么办（P035—P037）。",
    "答第一问：不可避免即天意，“世界”是权威在父母之上的第一教师，父母只覆盖能覆盖的，其余是世界给的教育；不可越理非法强行控制（P038—P043）。",
    "答第二问：答案不完美不是问题，努力寻找与分辨才是问题；给的是路标与定位星座而非终点；传递的是实验记录，不强加结论（P044—P054）。",
    "收束：“先写到这里”（P055）。"
   ],
   "concept_usage": [
    {"term": "亲自带娃/亲自带孩子", "meaning": "通俗义为“一切都要自己操作”；作者给出的本质义为“在一切世界观、价值观、人生观议题上，尽可能的由你自己或者你选择的受托人对子女实施引导”。", "evidence": "P020", "ambiguity": "两义并用：作者先用通俗义描述现象并批评其动机，再用本质义取代之；读者易混。"},
    {"term": "外包服务", "meaning": "把照料子女的事务交给外人/机构的做法，作者称对其进行不信任是“自己带”的主要动机。", "evidence": "P004", "ambiguity": "未说明外包服务的范围与质量差异。"},
    {"term": "背景辐射", "meaning": "比喻父母沮丧、焦虑、懦弱的日常状态对子女的持续无形影响。", "evidence": "P007", "ambiguity": "为隐喻用法，未给出可观测指标。"},
    {"term": "动机是一种魔法", "meaning": "作者的前提性命题：同等物理后果的行为因动机不同而对目睹者产生截然不同的精神影响。", "evidence": "P012", "ambiguity": "未给论证，属断言式前提。"},
    {"term": "自我绑架", "meaning": "作者用以指子女以自身安危/前途为筹码牵制父母的行为。", "evidence": "P011", "ambiguity": "术语未定义，且称幼崽“充满兽性”，带评价色彩。"},
    {"term": "天意/天养", "meaning": "作者对不可避免、不能选择的条件（统一课纲、学区安排等）的解释框架：世界是子女的第一教师，子女必定由天养。", "evidence": "P039", "ambiguity": "信仰式框架，作者同时说这部分“出于高于你的、比你更爱你的子女的安排”，无外部依据。"},
    {"term": "定位星座/目的地信标", "meaning": "作者对父母教导作用的界定：提供定位参照而非指定终点。", "evidence": "P050", "ambiguity": "为隐喻，未说明如何在具体议题上操作。"},
    {"term": "教父/教母", "meaning": "以“生父、养父，不如教父”强调实施三观引导者才是真正父母。", "evidence": "P032", "ambiguity": "与宗教用语“教父/教母”同形，作者未作区分。"}
   ],
   "examples_and_targets": [
    "亲自给娃穿衣服系鞋带、亲自接送上下学、亲自做饭甚至喂饭、亲自监督和指导作业、亲自洗澡、亲自铺床哄睡着（作者列举的“亲自带娃”通俗含义样本）",
    "怕外人不上心、怕父母不够科学、怕娃没有享受到可能的最高级的服务（作者列举的不信任外包的理由）",
    "饭桌前感叹社会新闻展现人心残酷，然后对子女炫耀“幸亏你有个好妈/爸，宁可辛苦点也要亲自照顾你”（作者要求避免的做法示例）",
    "配偶出于对辛劳的不忍提出请阿姨帮忙，被以“外人我信不过”拒绝（作者要求避免的做法示例）",
    "学校、教师（作者称其为父母选择的代理人，非大纲决定者）",
    "ta在学校受了欺负/学习上感到沮丧/遇到朋友的背叛/感到孤独/帮助别人却觉得受到了辜负（作者列举的价值观引导情境）",
    "生父、养父、教父；生母、养母、教母（作者的口号式工具）",
    "不容选择的统一课纲、无力选择的学区安排（作者举的不可选择环境因素）",
    "一片迷雾之中有三盏灯（作者比喻材料，说明参照而非终点）",
    "三十岁而已的简短、单调、迷茫的人生（作者自述，作为“自己也没有确定答案”的理由）",
    "关于“背叛”“信任”你自己想了多少（作者对读者的反问式检验）",
    "未完成的研究的实验记录、手册（作者对父母所传内容的比喻）"
   ],
   "conditions": [
    "定义限定：“一般来说这都是在表示一种‘一切都要自己操作’的意思”（P002）——指通常用法。",
    "动机条件：作者反复以“如果是因为这样而‘自己带’”“你的动机不可以是因为对ta人的无法信任”作为批评与建议的限定条件（P007、P014、P017）。",
    "例外条件：父母对世界观议题的决定权有例外——“除非你只是闭着眼睛随波逐流”（P022）。",
    "不可选择条件的处理条件：合理合法手段能对抗则对抗，不能抗拒的部分要相信其出于更高安排，且不得用越理非法手段强行控制（P041、P042）。",
    "结论层条件：“如果你真的成功了（幸好这是不可能的）”（P043）——作者否认该假设可实现。",
    "对象范围：以“子女”幼年与成长为场景，时间跨度到“子女整个童年——如果不是一生的话”（P007）。"
   ],
   "rhetoric_and_tone": "训诫与开导并用，第二人称“你/你们”直呼读者。大量格言式短句（“动机是一种魔法。”“生父、养父，不如教父。”“先写到这里。”）；反问密集（“谈何了解和学习合作的技术？”“看懂这是什么意思了吗？”“难道你觉得强加这个义务给ta是一种更好的安排吗？”）；带冲击力的贬抑与夸张（“充满兽性的幼崽”“玩弄于股掌之上”“虚应故事”）；结尾转为温和的比喻（三盏灯、定位星座、手册与实验记录），并以“先写到这里”收束，呈未完成感。",
   "unresolved_questions": [
    "作者未直接回应提问所指的“一边呼吁不做全职妈妈、一边强调亲自带娃”这一矛盾呼吁本身，二者是否冲突本文未评断。",
    "“亲自带孩子”的本质义（三观引导）与通俗义（一切自己操作）并用，容易导致对同一建议的两种理解。",
    "“动机是一种魔法”“信仰的无能”“世界是更爱子女的安排”等属信仰式断言，文中无依据，需外部核查。",
    "“充满兽性的幼崽”“自我绑架”对子女的描述带价值色彩，且未给出适用年龄范围。",
    "P007 中“父母每一天都在用无言的日常生活决定向ta展示”一句疑有笔误或语病，语义需核对（未据以立论）。",
    "父母应“尽可能覆盖”的边界与“世界给的教育”的边界如何划分，文中以举例（课纲、学区）代替标准。",
    "作者以“三十岁而已的简短、单调、迷茫的人生”自陈无确定答案，读者如何识别哪些手册内容值得继承，未给判据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "一般来说这都是在表示一种“一切都要自己操作”的意思。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "亲自给娃穿衣服系鞋带、亲自接送上下学、亲自做饭甚至喂饭、亲自监督和指导作业、亲自洗澡、亲自铺床哄睡着", "relation": "context"},
    {"key": "E003", "paragraph_id": "P004", "quote": "绝大多数情况下，这是出于对“外包服务”的不信任", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "是因为无法相信除自己以外的其他人。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "势必时时处处显示出巨大的沮丧、焦虑和懦弱", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "ta将来能真正领导、参与甚至识别一个有效的合作关系的可能性会被极大的削弱", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "“绝对不容闪失”的代价绝不只是一方放弃职业生涯，还有子女自身在人格上受到的影响。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "“绝对不容闪失”的背后毕竟是信仰的无能", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "被毫不犹豫的做“自我绑架”的运用，而将父母玩弄于股掌之上，令一切的人格教育皆变为虚应故事。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "动机是一种魔法。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "如果出于不同的动机，对目睹这事的人会有截然不同的精神影响。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "但你的动机不可以是因为对ta人的无法信任。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P015", "quote": "对子女炫耀“幸亏你有个好妈/爸，宁可辛苦点也要亲自照顾你”。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P016", "quote": "用“外人我信不过”这样的理由拒绝。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P020", "quote": "这是指在一切世界观、价值观、人生观议题上，尽可能的由你自己或者你选择的受托人对子女实施引导。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "仅仅是指这个。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P022", "quote": "事实上ta在幼年时期的整个学习大纲是你决定的，而绝不是学校决定的。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P022", "quote": "因此学校和老师只是你所选择的代理人，只是在执行你的意志。——除非你只是闭着眼睛随波逐流。", "relation": "qualifies"},
    {"key": "E019", "paragraph_id": "P024", "quote": "ta在学校受了欺负，这个思想引导需要你亲自做。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P030", "quote": "是父母真正最重要的职责。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P031", "quote": "谁在做这件事，谁才是你子女真正的父母。", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P032", "quote": "生父、养父，不如教父。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P038", "quote": "凡是不可避免的，就是天意。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P039", "quote": "这个世界是ta真正意义上的第一教师，权威甚至在你之上", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P039", "quote": "那些不容你选择的东西其实是世界决定给你子女的教育。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P041", "quote": "不要用越理非法的手段强行控制。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P042", "quote": "那往往是超越你时代局限和人格缺陷的正确的东西", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P043", "quote": "难道子女只能照着你的模子塑形吗？", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P043", "quote": "你确信那是绝对最好的答案吗？", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P044", "quote": "你没有最好的答案，这不是问题。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P044", "quote": "在分辨不同的答案上你自己花了多少实实在在的努力。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P047", "quote": "而是要给出一个尽可能正确的答案，好让ta们不至于要从零开始", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P048", "quote": "而是沿着你自己行过的路留下路标", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P050", "quote": "而是作为“定位星座”，让ta们可以凭着反馈信号去ta们自己的目的地。", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P051", "quote": "所以，你自己离目的地有多近是一个无关的问题。", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P052", "quote": "真正关键的问题是要精确、严谨、完善的表达你现在在哪里。", "relation": "supports"},
    {"key": "E037", "paragraph_id": "P052", "quote": "更像是一项未完成的研究的实验记录", "relation": "supports"},
    {"key": "E038", "paragraph_id": "P053", "quote": "只需要让对方明白以ta自己现在下的功夫，不继承你的手册是愚蠢的。", "relation": "supports"},
    {"key": "E039", "paragraph_id": "P053", "quote": "而ta在翻看你的手册的同时，并没有义务认同你的结论。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲子教育", "家庭分工与照料劳动", "动机与人格养成"],
   "issue_candidates": ["全职妈妈与亲自带娃的呼吁冲突", "外包育儿与信任能力", "三观引导的责任归属", "父母自身答案不确定时的教育方式"],
   "text_function_candidates": ["答疑", "训诫", "经验总结", "解释"],
   "object_candidates": ["父母", "子女", "学校与教师", "阿姨（家政服务者）", "配偶", "统一课纲与学区安排（机构性因素）"],
   "working_keywords": ["亲自带娃", "外包服务", "背景辐射", "动机是一种魔法", "自我绑架", "世界观/价值观/人生观", "受托人", "天意", "定位星座", "手册", "教父/教母"]
  },
  "notes": "本篇无图片节点，正文完整可读（56 段）。提问者的问题指向两种社会呼吁的并存矛盾，作者未正面评断该矛盾，而是重定义“亲自带孩子”，已在 question_context 与本篇未决问题中区分。P007 一处疑有语病，仅登记未据以立论。P022、P039、P042 含信仰式断言（天意、世界更爱你子女的安排），已按作者归属记录，未作为外部事实。"
 },
 "0d3cda4e": {
  "analysis": {
   "question_context": "提问者问：为什么有的人认为太重感情的人基本都是穷人？（Q001，属提问者转述的一种社会印象，不在作者名下）。作者不直接评判该印象，而是先拆解“重感情/感情”的词义：称大部分人所谓感情实为“交情”；再追溯传统社会伦理把亲朋故旧规定为互相负有义务的利益共享机制及其古代连坐背景；继而指出连坐观念被现代法理消除后该机制失效、仍按旧观念讲感情会吃亏；最后把“讲感情”转到“对自己选择要爱的人讲感情”，断言相爱关系管理成本极低、产出最丰厚，并以统计可见度解释“富人都不讲感情”的错觉。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "概念辨析：追问“什么叫重感情”“感情是什么东西”，指出大部分人所谓感情其实是“交情”——曾打过交道、姑且未翻脸、双方无利害冲突或明显亏损，如同班、同村、同圈子者。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "理由：传统社会伦理规定有身份关系者天然负有关系义务，有亲就有情，有情就有义。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "例证：引洪门三十六誓的开门头三誓（视他人父母兄弟为自家、助葬、留宿外洋兄弟，违者五雷诛灭或死在万刀之下）作为“被规定的感情”的经典例子。引文说话者为洪门誓词，非作者。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "主张：这种“被规定的感情”是一种利益再分配规则，每个人都负有多条照顾亲朋故旧乡亲同窗同事的义务，对方亦负有帮助当事人的责任。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "论据（古代制度背景）：以连坐族诛作为“必须帮助”的强制保障——一人造反一乡屠尽、一人谋逆九族齐诛、一人失势一众皆黜；人们无从切割、被看作一体，只能从现状中捞回最多好处，遂形成半强制性利益共享机制并成为中国文化中天经地义的义理。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "主张：现代法理原则与治理理念根本变化，从基本实践层面消除连坐；父亲做的事默认儿子不负责，故成功仍按旧伦理须分享、失败依新法理却与他人无关——天平失衡。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019"], "summary": "限定式结论：未意识到失衡已成既成事实、传统“投资保障机制”已失效而仍按传统观念讲感情者会额外受损；若把“讲感情”定义为按传统伦理承担分担风险、分享利益的义务，大概率得不偿失。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021"], "summary": "转折：追问“讲感情”是否就是这个定义；指出人除先天出身带来的伦理义务外，还有自己主动建立的关系。", "role": "transition"},
    {"unit_id": "U009", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027"], "summary": "列举：自己选择要追随、珍惜、报答、缔结并养护关系以及要爱的人。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032", "P033"], "summary": "主张：对自己选择要爱的人讲感情是否必然亏损？作者称若双方确守爱的法则，相爱关系是产出最丰厚的关系，其特征是管理成本极低、内耗极小；消耗极大的关系要么无爱，要么存在对爱的理念性误解或爱的能力有待成熟。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P034", "P035"], "summary": "理由：理想的爱是管理学梦想的圣杯——不需立法、司法成本，几乎无沟通成本（需表达与理解能力），对关系恶性循环有天然抑制作用，除物理毁灭外无法摧毁。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P036", "P037", "P038"], "summary": "主张与结论：二人同心其利断金；几百上千人自愿同心舍命足以震动世界；“财务自由”没资格被当作值得花太多时间探讨的话题，对有感情可讲者富裕实非难事。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P039", "P040"], "summary": "例证与反驳对象：成功且长青的企业常含富贵不能淫、贫贱不能移、威武不能屈的感情，否则撑不住；并警告不要被暴发户被时代浪潮扬起所形成的“大数据”误导，其富有会化为下一代账单、赌债甚至毒资。", "role": "example"},
    {"unit_id": "U014", "paragraph_refs": ["P041", "P042", "P043", "P044"], "summary": "结论：想受得住财富的诅咒必须学会讲感情与学会对谁、怎样讲感情；懂此者遇值得讲感情的对象便马力全开，但对象少见且不炫耀，故事实上没可见度，几乎必然造成“富人都不讲感情”的错觉。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称大部分人所谓的感情其实是一种交情而非感情，即曾打过交道、未翻脸、双方无利害冲突或明显亏损（如同学、同村、同圈子者）。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称传统社会伦理规定有身份关系者天然负有关系义务（有亲有情有义），这种“被规定的感情”构成半强制性的利益再分配规则，各方互相负有照顾与帮助义务。", "evidence": ["E003", "E004", "E005"]},
    {"claim_id": "C003", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引洪门三十六誓开门头三誓为例：入洪门者视他人父母兄弟姊妹妻侄为自家亲属，须助葬、须留宿外洋兄弟，违者五雷诛灭或死在万刀之下（引文说话者为洪门誓词，非作者判断）。", "evidence": ["E006", "E007", "E008"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称古代以连坐族诛保证“必须帮助”：一人造反一乡屠尽、一人谋逆九族齐诛、一人失势一众皆黜，有伦理关系者被看作一体、由不得撇清。", "evidence": ["E009", "E010", "E011"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这套半强制性利益共享机制长盛不衰、深深嵌入中国文化，成为中国人“生下来就知道的天经地义的义理”。", "evidence": ["E012"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称现代社会的法理原则与治理理念发生根本变化，从基本实践层面消除连坐观念：父亲做的事默认儿子不负责，故成功依旧伦理仍须分享、失败依新法理却与他人无关，天平失衡。", "evidence": ["E013", "E014", "E015", "E016"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者限定：若把“讲感情”定义为按传统伦理承担分担风险、分享利益的义务，在传统“投资保障机制”已失效的既成事实下，大概率得不偿失；未意识到失衡者会给自己带来额外损失。", "evidence": ["E017", "E018"]},
    {"claim_id": "C008", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者提出待答问题：“讲感情”是否就是这个（传统伦理义务）定义，并指出人还有自己主动建立的关系。", "evidence": ["E019", "E020"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称以“双方都确确实实遵循爱的法则行事”为前提，相爱的关系是世界上产出最丰厚的关系，因其管理成本极低、内耗极小；消耗极大的关系要么无爱，要么存在对爱的理念性误解或爱的能力有待成熟。", "evidence": ["E021", "E022", "E023", "E024"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称理想的爱是管理学梦想的圣杯：不需立法与司法成本，几乎没有沟通成本，对关系恶性循环有天然抑制作用，除物理毁灭外无法摧毁。", "evidence": ["E025", "E026", "E027"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言二人同心其利断金，几百上千人自愿同心、为彼此舍命足以令山河变色；“财务自由”没资格被当作值得花太多时间探讨的话题，对有感情可讲者富裕实非难事。", "evidence": ["E028", "E029", "E030", "E031"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称成功而且长青的企业中常有富贵不能淫、贫贱不能移、威武不能屈的感情在内；否则树大招风、百年寒暑的企业不可能只靠“多给下属钱”挺住。", "evidence": ["E032", "E033"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者警告不要被暴发户被时代浪潮扬起所形成的“大数据”误导，并预测这类富有很快会转化为下一代的账单、赌债甚至毒资，化为乌有。", "evidence": ["E034"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称想要受得住财富的诅咒，人必须学会讲感情、学会对谁怎样讲感情，根本没得选。", "evidence": ["E035"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称懂此厉害者随时随地愿意讲感情，遇值得讲感情、讲得了感情的对象便马力全开，但这样的人少见且不炫耀，故在统计上没什么可见度，几乎必然造成“富人都不讲感情”的错觉。", "evidence": ["E036", "E037", "E038"]}
   ],
   "argument_steps": [
    "重设问题：先追问“什么叫重感情”“感情是什么东西”，把提问中的“重感情”拆为待定义项。",
    "定义：大部分人所谓感情实为交情——曾打交道、无明显利害亏损（同班、同村、同圈子）。",
    "前提：传统社会伦理按身份关系规定关系义务，有亲有情有义。",
    "例证：洪门三十六誓开门头三誓反复强调此点（引用洪门誓词）。",
    "推论：被规定的感情构成利益再分配规则，各方互负照顾与帮助义务。",
    "历史论据：古代以连坐族诛保证必须帮助，人们无从切割，只能从中捞好处，遂成半强制利益共享机制与天经地义的义理。",
    "转折：现代法理消除连坐，成功仍被要求分享、失败却与他人无关——天平失衡，传统投资保障机制失效。",
    "限定结论：按传统伦理定义讲感情大概率得不偿失；未意识到失衡者会额外受损。",
    "提问式转折：“讲感情”是不是就是这个定义？人还有自己主动建立的关系。",
    "列举正面关系：自己选择要追随、珍惜、报答、缔结与养护关系、要爱的人。",
    "结论一：以双方确守爱的法则为前提，相爱关系产出最丰厚（管理成本极低、内耗极小）；消耗大者或无爱或爱的理念/能力有问题。",
    "理由：理想的爱是管理学圣杯，不需立法司法成本、几无沟通成本，能抑制恶性循环且除物理毁灭外不可摧毁。",
    "推论：同心足以震动世界；财务自由不配作为重要话题；有感情可讲者富裕非难事。",
    "例证：长青企业内常有富贵不能淫、贫贱不能移、威武不能屈的感情；暴发户“大数据”不可信。",
    "最终结论：要受得住财富的诅咒必须学会讲感情；讲感情者不炫耀，故统计可见度低，造成“富人都不讲感情”的错觉。"
   ],
   "concept_usage": [
    {"term": "重感情", "meaning": "提问者所用词；作者未直接采用其含义，而是先追问“什么叫重感情”并把常见用法拆解为“交情”，随后另立“对自己选择要爱的人讲感情”。", "evidence": "P001", "ambiguity": "作者未对提问中的“重感情”给出统一定义，全文实际讨论两种不同的“感情/讲感情”。"},
    {"term": "感情 / 交情", "meaning": "交情＝曾打过交道、姑且不翻脸、双方无利害关系或明显亏损；作者称这才是大部分人所谓的感情。", "evidence": "P003", "ambiguity": "与下文“对自己选择要爱的人讲感情”的用法未明确划界。"},
    {"term": "被规定的感情", "meaning": "由传统社会伦理按身份关系强制规定的互助义务，构成利益再分配规则。", "evidence": "P008", "ambiguity": "作者未讨论该义务在当代是否仍有部分正当性。"},
    {"term": "连坐 / 族诛", "meaning": "古代法律与治理逻辑把有伦理关系者视为一体、共同承担罪责的制度背景；作者称现代法理已从基本实践层面消除该观念。", "evidence": "P010", "ambiguity": "作者对历史制度的概述无出处，需外部核查。"},
    {"term": "讲感情", "meaning": "文中先指按传统伦理承担分担风险、分享利益的义务（作者认为已失效、大概率得不偿失），后指对自己选择要爱的人依爱的法则行事（作者认为产出最丰厚）。", "evidence": "P019", "ambiguity": "同一词两义并存，以“问题在于，‘讲感情’是不是就是这个定义”转折，未给出统一判定标准。"},
    {"term": "爱的法则", "meaning": "作者称双方确守时使关系管理成本极低、内耗极小并使产出最丰厚的原则；未给出具体条文。", "evidence": "P030", "ambiguity": "仅以效果（低成本、低内耗）描述，无可操作判据。"},
    {"term": "财富的诅咒", "meaning": "作者用以指暴发户式财富的后果（下一代账单、赌债甚至毒资）；称受得住须学会讲感情。", "evidence": "P040", "ambiguity": "未界定“诅咒”的作用机制与适用边界。"}
   ],
   "examples_and_targets": [
    "洪门三十六誓开门头三誓（P005-P007，作者引用/引述的誓词文本，作为“被规定的感情”的经典例子；说话者为洪门誓词，非作者）",
    "连坐族诛（P010-P012，作者使用的古代制度论据）",
    "一人造反，一乡屠尽；一人谋逆，九族齐诛；一人失势，一众皆黜（P011，作者的历史性断言，无出处，待外部核查）",
    "自己选择要追随/珍惜/报答/缔结并养护关系/要爱的人（P023-P027，作者列举的正面关系类型）",
    "成功而且长青的企业（P039，作者举例，未指名）",
    "富贵不能淫、贫贱不能移、威武不能屈（P039，作者引用的成语式表述，用以形容企业中的感情）",
    "暴发户及其“大数据”（P040，作者的警示与反驳对象）",
    "提问者转述的“太重感情的人基本都是穷人”（Q001，提问者说法，作者未直接采信而先拆解其前提）"
   ],
   "conditions": [
    "作者以“如果把‘讲感情’定义为按照传统伦理承担‘分担风险、分享利益’的义务”为条件，才得出大概率得不偿失（P019）。",
    "相爱关系产出最丰厚的前提是“双方都确确实实遵循爱的法则行事”（P030）。",
    "关系消耗大的两种解释：要么无爱；只要以爱为名，则不是存在对爱的理念性误解，就是存在爱的能力有待成熟（P033）。",
    "传统“投资保障机制”失效依赖的前提：现代法理与治理理念变化、从基本实践层面消除连坐（P014-P018）。",
    "理想的爱“几乎没有沟通成本”附条件：需要有效的支撑爱、洞石穿金的表达能力和理解能力（P034）。",
    "财富诅咒针对的是被时代浪潮扬起的暴发户式富有（P040）。",
    "讲感情需遇上“值得讲感情、讲得了感情的对象”（P042）。"
   ],
   "rhetoric_and_tone": "以连续追问开篇（“什么叫重感情？”“‘感情’是什么东西？”）重设问题；援引洪门誓词与连坐史例作论据，语气强硬；多用断言式短句与重复强调（“我实实在在的告诉你们”“我再说一遍”）；对读者用第二人称“你们”训诫；对暴发户与“大数据”使用贬抑性修辞（“黄粱一梦”）；结尾以统计可见度回护“富人讲感情”而将其不可见归因于不炫耀。",
   "unresolved_questions": [
    "提问者所指“太重感情的人基本都是穷人”这一印象是否属实，作者未直接承认或否认，而是重定义“感情/讲感情”；本文未给出该经验命题的直接结论。",
    "洪门三十六誓引文未标注版本或文献来源，引文可靠性需外部核查（P005-P006）。",
    "“一人造反，一乡屠尽；一人谋逆，九族齐诛；一人失势，一众皆黜”等历史断言无出处，需外部核查（P011）。",
    "“相爱的关系是世界上产出最丰厚的关系”“管理成本极低，内耗极小”为作者断言，未给衡量方式、范围或数据（P030-P032）。",
    "“成功而且长青的企业”未指名，无法核对其论据（P039）。",
    "“财富的诅咒”未界定机制；“暴发户大数据”所指范围不明（P040）。",
    "“感情/交情”与“讲感情”的两种含义在文中并存且未明确划界，可能影响对结论的解释（P003、P019、P028）。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P003", "quote": "大部分人所谓的感情，说白了是一种交情而不是一种感情。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "比如曾经是一个班的，是一个村子的，一个圈子的", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "只要你们构成这种身份关系，你们之间就被规定了有亲，有亲就有情，有情就有义。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "这种“被规定的感情”构成了一种利益再分配的规则", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "它也规定了这些亲朋故旧相亲等等等等都有责任帮助当事人自己。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "洪门三十六誓，开门头三誓都是在反复强调这一点", "relation": "context"},
    {"key": "E007", "paragraph_id": "P006", "quote": "第一誓：自入洪门之后，尔父母即是我父母，尔兄弟姊妹即是我兄弟姊妹", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P006", "quote": "如有不遵此例，不念此情，即为背誓，五雷诛灭。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "在古代再直白没有——有连坐族诛之罪存在。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "一人造反，一乡屠尽；一人谋逆，九族齐诛；一人失势，一众皆黜。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "你们在古代的法律原则上、治理逻辑上根本就被看作一体，由不得你撇清。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P013", "quote": "构成了一种中国人生下来就知道的天经地义的义理。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "现代社会的法理原则和治理理念发生了根本的变化。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "就是从基本实践的层面消除了连坐这个观念。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P015", "quote": "父亲做的事，默认儿子是不用负责的。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P016", "quote": "你的成功基于原来的伦理逻辑有义务和对方分享，但你的失败基于新的法理观念却与他人无关", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P018", "quote": "还按照传统的观念“讲感情”，就会给自己带来额外的损失。", "relation": "qualifies"},
    {"key": "E018", "paragraph_id": "P019", "quote": "如果把“讲感情”定义为按照传统伦理承担“分担风险、分享利益”的义务，大概率会得不偿失。", "relation": "qualifies"},
    {"key": "E019", "paragraph_id": "P020", "quote": "问题在于，“讲感情”是不是就是这个定义。", "relation": "qualifies"},
    {"key": "E020", "paragraph_id": "P021", "quote": "人还有自己主动建立的关系。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P030", "quote": "如果双方都确确实实遵循爱的法则行事，相爱的关系是世界上产出最丰厚的关系。", "relation": "qualifies"},
    {"key": "E022", "paragraph_id": "P031", "quote": "它的管理成本极低，内耗极小。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P033", "quote": "但凡一段关系让你感到消耗极大，要么它是无爱的", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P033", "quote": "就是存在爱的能力的有待成熟。", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P034", "quote": "理想的爱，是管理学梦想的圣杯。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P034", "quote": "洞石穿金的表达能力和理解能力是必备的", "relation": "qualifies"},
    {"key": "E027", "paragraph_id": "P035", "quote": "除了物理毁灭之外，根本无法摧毁。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P036", "quote": "几百上千人能自觉自愿的同心合意、为彼此舍命，足以令山河变色，震动整个世界。", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P037", "quote": "根本没资格被当做一个值得花太多时间探讨的话题。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P038", "quote": "对幸运到有感情可讲，更幸运到能讲得了感情的人，富裕实非难事。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P032", "quote": "真正相爱的关系，其管理成本必然极低，其内耗必然极小。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P039", "quote": "其中常常有一些富贵未能淫、贫贱未能移、威武未能屈的感情在内。", "relation": "supports"},
    {"key": "E033", "paragraph_id": "P039", "quote": "绝不是靠“多给下属钱”就能挺得住的", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P040", "quote": "ta们的所谓“富有”很快会转化为下一代的账单和赌债甚至毒资，化为乌有", "relation": "supports"},
    {"key": "E035", "paragraph_id": "P041", "quote": "人必须要学会讲感情，学会对谁、怎样讲感情，根本没得选。", "relation": "supports"},
    {"key": "E036", "paragraph_id": "P042", "quote": "懂这厉害的人随时随地愿意讲感情", "relation": "supports"},
    {"key": "E037", "paragraph_id": "P043", "quote": "更不会拿来炫耀给别人知道罢了", "relation": "supports"},
    {"key": "E038", "paragraph_id": "P044", "quote": "几乎必然造成“富人都不讲感情”的错觉。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会伦理与法理变迁", "人际关系与利益分配", "情感与婚恋", "财富观"],
   "issue_candidates": ["“重感情=穷人”印象的成因", "传统伦理义务与现代个人责任", "连坐制度与利益共享机制", "相爱关系的成本与产出", "统计可见度与印象偏差"],
   "text_function_candidates": ["答疑", "概念辨析", "论辩", "训诫", "经验总结"],
   "object_candidates": ["洪门（帮会组织及其誓词）", "亲朋故旧/乡亲/同窗/同事", "暴发户", "长青企业（未指名）", "提问者转述“穷人”说法的持论者"],
   "working_keywords": ["重感情", "交情", "被规定的感情", "利益再分配", "连坐", "族诛", "天平失衡", "投资保障机制", "爱的法则", "管理成本", "内耗", "财富的诅咒"]
  },
  "notes": "本篇无图片节点，正文完整可读（44 段，含 1 个引用块 P006）。P006 为 quote 字段的洪门三十六誓引文，说话者为洪门誓词，已按 quoted_or_cited / cited_source 记录，未归入作者主张。提问者所转述的“太重感情的人基本都是穷人”属提问者说法，作者未直接承认或否认，已在 question_context 与未决问题中登记。P011 历史断言、P039 企业例证、P040 暴发户“大数据”均无出处，只登记为待外部核查，未作事实裁决。"
 },
 "5cc6bd75": {
  "analysis": {
   "question_context": "提问者问：人类真正可以信任的东西是什么？（Q001，属提问者）。作者不列举可信任的对象，而是先给出一个形式判据——“不具有可证伪性的皆可信”，并界定不可证伪为永远没有任何人、任何办法能有效证明其为假；随后以反问（“但你们信了吗？你们信得了吗？”）把问题从对象侧转向主体侧，断言问题出在人类缺少信的能力上；再举四个日常不可证伪命题为例，指出人生中大量命题本无手段严谨证实或证伪、却必须选择立场，唯一要做的是择善固执、坚持到底。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "立论与定义：自问“什么东西是真正可信”，给出判据“不具有可证伪性的皆可信”，界定不可证伪为永远、没有任何人、没有任何办法能有效地证明其为假，并称这已是逻辑上绝对安全的保证。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "反问与归因转换：反问读者是否信、信不信得了，进而否认问题出在“没有可信的对象”，主张问题出在人类缺少信的能力上，并称读者大概把这件事想歪了。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014"], "summary": "例证：不可证伪的事情极多，绝不止一两个命题；举例“你可以做得更好”“ta本来可以不走”“ta是/不是故意的”“世界有 / 没有所谓正义”均不可证伪。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016"], "summary": "主张：你的人生中充斥着没有（实践上可行的）手段严谨证实或证伪、却必须选择立场、且选了永远没人能真的说你错了的命题。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019"], "summary": "行动要求与反问收尾：唯一需要做的就是择善固执、坚持到底；再以“你做到了吗？”“问题真是那些东西‘不可信’吗？”反问读者。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出判据：不具有可证伪性的皆可信。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定不可证伪为“永远、没有任何人、没有任何办法能有效的向你证明其为假”，并称这已是逻辑上绝对安全的保证。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问读者：但你们信了吗？你们信得了吗？（以此指出人并不因该逻辑保证就能信）。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认问题出在“没有可信的对象”上，主张问题出在人类缺少信的能力上。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称不可证伪的事情极多，绝不止读者以为的那么一两个命题。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者举例称“你可以做得更好”“ta本来可以不走”“ta是/不是故意的”“世界有 / 没有所谓正义”这些命题都不可证伪。", "evidence": ["E008", "E009", "E010", "E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人生中充斥着没有手段（或没有实践上可行的手段）足以严谨证实或证伪、却必须选择立场的命题，而人所选的正是永远没人能真的说他错了的命题。", "evidence": ["E012", "E013"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的行动要求：你唯一需要做的就是择善固执，坚持到底。", "evidence": ["E014"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问“你做到了吗？”，指向读者未必做到坚持。", "evidence": ["E015"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者末句反问“问题真是那些东西‘不可信’吗？”，暗示问题不在对象本身。", "evidence": ["E016"]}
   ],
   "argument_steps": [
    "自问式开头：以“什么东西是真正可信的呢？”重申提问。",
    "给出判据：不具有可证伪性的皆可信。",
    "定义不可证伪：永远、没有任何人、没有任何办法能有效地向你证明其为假。",
    "评价：这已经是逻辑上绝对安全的保证。",
    "反问转折：但你们信了吗？你们信得了吗？",
    "归因转换：问题不出在没有可信的对象上，而出在人类缺少信的能力上；并称读者想歪了。",
    "扩充外延：不可证伪的事情极多，不止一两个命题。",
    "例证：四个日常命题（可做得更好、ta本来可以不走、ta是/不是故意的、世界有/没有所谓正义）。",
    "处境描述：人生充斥着无可行手段严谨证实或证伪、却必须选立场、且选了没人能说你错的命题。",
    "行动要求：择善固执，坚持到底。",
    "反问收尾：你做到了吗？问题真是那些东西“不可信”吗？"
   ],
   "concept_usage": [
    {"term": "可信", "meaning": "作者判据下的性质——不具有可证伪性；文中未列举任何具体的可信对象。", "evidence": "P002", "ambiguity": "与日常“信任/值得托付”的用法是否等同，文中未界定。"},
    {"term": "可证伪 / 不可证伪", "meaning": "不可证伪＝永远、没有任何人、没有任何办法能有效地向你证明其为假。", "evidence": "P003", "ambiguity": "只从“无法被证明为假”定义，未讨论能否被证实，也未区分逻辑上的不可证伪与实践上无手段；该术语未注明理论来源。"},
    {"term": "信的能力", "meaning": "被作者归因于人类自身、与“可信对象”相对的能力；作者称问题出在缺少它。", "evidence": "P007", "ambiguity": "如何获得、如何判定其有无，文中未说明。"},
    {"term": "择善固执", "meaning": "作者给出的唯一行动要求——在必须选边而无法证实证伪的命题上选边并坚持到底。", "evidence": "P017", "ambiguity": "“善”的判定标准未给出。"},
    {"term": "不可信", "meaning": "末句加引号使用，指读者归因于对象的那种性质；作者以反问质疑该归因。", "evidence": "P019", "ambiguity": "作者未正面给出“不可信”的判定标准。"}
   ],
   "examples_and_targets": [
    "“你可以做得更好”（P011，作者举例的不可证伪命题）",
    "“ta本来可以不走”（P012，同上）",
    "“ta是/不是故意的”（P013，同上）",
    "“世界有 / 没有所谓正义”（P014，同上）",
    "读者（文中“你们”，P005、P008、P015、P018，被反问与训诫的对象）",
    "提问者的问题“人类真正可以信任的东西是什么”（Q001，提问者说法；作者未列出对象清单，只给判据）"
   ],
   "conditions": [
    "判据依赖作者对“不可证伪”的定义（永远、无人、无法有效证明其为假）（P003）。",
    "作者的处境描述限定于“实际上没有手段（或没有实践上可行的手段）”足以严谨证实或证伪的命题（P016）。",
    "“择善固执”的要求适用于“你必须要选择一个立场”的命题（P016）。",
    "作者未给出适用领域的边界，举例仅涉及日常评价性命题（P011-P014）。"
   ],
   "rhetoric_and_tone": "全篇为短句、反问密集（“但你们信了吗？”“你们看清楚问题没有？”“你做到了吗？”）；第二人称复数“你们”训诫，末段直接质问；以叹词“唉”表达对读者的失望；结论不作展开而近于格言式断言；标题“可信”与正文“信的能力”形成词面回环。",
   "unresolved_questions": [
    "作者未列举任何具体可信对象，提问者所问“真正可以信任的东西是什么”在本文未获正面清单式回答。",
    "“不具有可证伪性的皆可信”是否等价于“凡不可证伪皆应信”，以及其与“择善固执”的关系（是否任意选边皆可），文中未说明。",
    "“信的能力”如何获得或培养、以何判定其有无，文中未说明（P007）。",
    "“择善固执”中“善”的判定标准未给出（P017）。",
    "四个举例均为作者自拟，未说明其来源或是否涵盖宗教、科学等主要争议领域（P011-P014）。",
    "正文完整可读（19 段），本篇无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "不具有可证伪性的皆可信。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "所谓不可证伪，也就是永远、没有任何人、没有任何办法能有效的向你证明其为假。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "这已经是逻辑上绝对安全的保证了。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "但你们信了吗？你们信得了吗？", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "所以，问题出在没有可信的对象上吗？", "relation": "qualifies"},
    {"key": "E006", "paragraph_id": "P007", "quote": "问题出在人类缺少信的能力上。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "不可证伪的事情极多，绝不止是你们以为的那么一两个命题。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P011", "quote": "“你可以做得更好”，这个命题就不可证伪。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P012", "quote": "“ta本来可以不走”，这个命题也不可证伪。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P013", "quote": "“ta是/不是故意的”，也不可证伪。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P014", "quote": "“世界有 / 没有所谓正义”，也不可证伪。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P016", "quote": "你必须要选择一个立场", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P016", "quote": "你选了永远没人能真的说你错了的命题。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P017", "quote": "你唯一需要做的就是择善固执，坚持到底。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P018", "quote": "你做到了吗？", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P019", "quote": "问题真是那些东西“不可信”吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认识论与信念", "逻辑与论证方法", "人生哲学"],
   "issue_candidates": ["可证伪性与可信的关系", "信任的对象与主体能力", "无手段证实/证伪命题上的立场选择", "择善固执"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "反问式短评"],
   "object_candidates": ["读者（“你们”）", "提问者"],
   "working_keywords": ["可信", "可证伪", "不可证伪", "信的能力", "择善固执", "立场", "命题"]
  },
  "notes": "本篇无图片节点，正文完整可读（19 段）。全篇为反问密集的短篇训诫式答复，作者未列举“真正可信的东西”的具体清单，该缺口已登记于 question_context 与未决问题，未据提问者立场补写。文中“可证伪性”未注明理论来源，列为待外部核查项。"
 },
 "81d8887e": {
  "analysis": {
   "question_context": "提问者问：如何看待「奢侈品坏掉了心疼是因为你的经济离这个段位太远，等你真正配得上奢侈品你就不会心疼了」的言论？（Q001，该言论仅出现在提问字段，属提问者转述的他人说法，作者未复述）。作者直接反驳该言论的判断基准：以“有没有资格进博物馆”重设奢侈品的判准，主张心疼与否不是有没有钱的问题，而是有没有基本做人的格调的问题；随后给出拥有奢侈品的“正确姿势”（可扛过几百年、可修复、材质不朽、可传世），并列出材料与工艺上的具体判据，最后把顶配手机、口红、球鞋、超跑排除在“奢侈”之外。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "重设判准：以反问提出标准——没有资格进博物馆的东西没资格叫奢侈品；有资格进博物馆的东西坏了谁都会心疼。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "反驳：这不是有没有钱的问题，而是有没有基本做人的格调的问题；并以“买得起《蒙娜丽莎》烧来取暖也会心疼”“它不只值你买的那点钱”反问对方。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "正面定义与叙事：拥有“奢侈品”的正确姿势是这东西有机会扛过几百年岁月洗礼、其凝聚的智慧与努力有资格得到守护和加持；于是你选了它，过完一生后它加上你的标记，成为一件活的传世之物（A piece of history）。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "行动提醒与例证：为不能像忒修斯之船那样强可修复、同时设计脆弱的东西付过高价格不值得；并以实木/复合板、硬木/软木、榫卯/现代连接件的价格上限排序，及黄金白金因性质稳定可供传承为例。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "列举与推论：列举陶瓷、稳定皮革、无镀层不易锈金属、不带漆层实木、纯贵金属、稳定无辐射毒性硬质矿石、天然矿物颜料、耐降解面料、高温陶瓷等为真正奢侈品的“骨肉来源”；不朽材料用不朽方法组织成的结晶配得上个人灌注的价值。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017"], "summary": "限定式结论：这样的奢侈品只要买得起就是便宜的、最后是赚的；如果是花在品质上，常常越贵反而越赚。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "延伸与排他结论：灵魂会留在遗物上，灵魂可贵则每件遗物成为无价之宝（用了一辈子的钛合金小刀之例）；顶配手机、特制口红、限量球鞋、电驱超跑基本没有资格谈奢侈；收束为“这种浪漫，没有价格”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "提问所引言论主张：奢侈品坏掉时心疼，是因为经济离这个段位太远；真正配得上奢侈品就不会心疼（该言论仅见于 Q001，提问者转述，正文未复述；作者在 P003 以“这不是有没有钱的问题”否定其判断基准）。", "evidence": ["E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以是否“有资格进博物馆”判定奢侈品：没有资格进博物馆的东西没资格叫奢侈品；有资格进博物馆的东西坏了谁都会心疼。", "evidence": ["E001", "E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者反驳心疼与否取决于经济段位的说法：这不是有没有钱的问题，而是有没有基本做人的格调的问题。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：难道因为买得起《蒙娜丽莎》，烧来取暖就不心疼了？并质问对方是否真以为它只值买它的那点钱。", "evidence": ["E004", "E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出拥有“奢侈品”的正确姿势：这东西有机会扛过几百年的岁月洗礼，其凝聚的智慧和努力也有资格得到守护和加持；你选了它，一生过后它加上你的标记，成为一件活的传世之物（A piece of history）。", "evidence": ["E006", "E007", "E008", "E021", "E022"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提醒：为不能像忒修斯之船那样拥有强可修复性、同时自身设计又脆弱的东西付出过高价格是不值得的。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以价格上限排序佐证材质判据：实木家具高于复合板家具，实木中硬木高于软木，榫卯高于特制现代连接件。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称黄金白金之所以是贵金属，是因为它们性质稳定可供传承。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列举真正“奢侈品”的材质来源（陶瓷、稳定良好的皮革、无镀层不易锈的金属、不带漆层的实木、纯贵金属、性质稳定无辐射毒性的硬质矿石、天然矿物颜料、耐降解老化面料、高温陶瓷等），并称不朽材料用配得上不朽的方法组织成的结晶配得上个人灌注的价值。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者限定：这样的“奢侈品”只要你买得起就是便宜的，因为最后是赚的；如果是花在了品质上，常常越贵反而越赚。", "evidence": ["E015", "E016"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称你的灵魂会留在这些遗物上，如果你的灵魂是可贵的，到你离开时追随过你的每一件东西都会是无价之宝；并以用了一辈子的钛合金小刀最后马云也未必买得起为例。", "evidence": ["E017", "E018"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称在真正的奢侈品面前，顶配手机、特制口红、限量球鞋、电驱超跑等基本没有资格谈奢侈。", "evidence": ["E019"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“这种浪漫，没有价格”收束全文。", "evidence": ["E020"]}
   ],
   "argument_steps": [
    "重设判准（反问）：没有资格进博物馆的不配叫奢侈品；有资格进博物馆的坏了谁都会心疼。",
    "否定对方判准：心疼与否不是有没有钱的问题，而是有没有基本做人的格调的问题。",
    "反问反驳：买得起《蒙娜丽莎》烧来取暖也会心疼；它不只值你买的那点钱。",
    "正面定义：拥有“奢侈品”的正确姿势＝这东西有机会扛过几百年岁月洗礼，其凝聚的智慧与努力有资格得到守护和加持。",
    "叙事：你选了它；过完波澜壮阔的一生后它加上你的标记，成为活的传世之物（A piece of history）。",
    "行动提醒：为无强可修复性且设计脆弱的东西付过高价格不值得。",
    "例证（材质与工艺排序）：实木>复合板，硬木>软木，榫卯>特制现代连接件。",
    "例证：黄金白金为贵金属，因其性质稳定可供传承。",
    "列举：真正奢侈品的材料类别（陶瓷、皮革、金属、实木、纯贵金属、硬质矿石、矿物颜料、面料、高温陶瓷等）。",
    "推论：不朽材料＋不朽方法组织成的结晶配得上个人灌注的价值。",
    "限定结论：这样的奢侈品只要买得起就是便宜的、最后是赚的；花在品质上越贵越赚。",
    "延伸：灵魂留在遗物上，可贵的灵魂使每件遗物成为无价之宝（钛合金小刀之例）。",
    "排他结论：顶配手机、特制口红、限量球鞋、电驱超跑没资格谈奢侈。",
    "收束：这种浪漫没有价格。"
   ],
   "concept_usage": [
    {"term": "奢侈品", "meaning": "作者以其是否“有资格进博物馆”重新定义：材料与工艺可扛过几百年、可修复、可传承之物（“真正‘奢侈品’的骨肉来源”）；与高价消费品（手机、口红、球鞋、超跑）相对。", "evidence": "P001", "ambiguity": "未给出“进博物馆”的机构标准，也未讨论品牌、稀缺性等常见维度；P013 清单以省略号收尾。"},
    {"term": "格调", "meaning": "作者用以对立于“有没有钱”的判据：心疼与否属于有没有基本做人的格调的问题。", "evidence": "P003", "ambiguity": "未界定“格调”的判定标准。"},
    {"term": "强可修复性", "meaning": "借“忒修斯之船”指物品可被持续修复而延续；作者以此为是否值得付出高价的判据。", "evidence": "P010", "ambiguity": "未给出可修复性的程度门槛，也未说明“设计脆弱”如何判定。"},
    {"term": "传世之物 / A piece of history", "meaning": "经数百年岁月洗礼、又叠加个人标记而形成的活物，作者视之为奢侈品的正确形态。", "evidence": "P008", "ambiguity": "与“使用价值”“投资价值”的关系未展开。"},
    {"term": "不朽的材料", "meaning": "作者列举的性质稳定、不易锈蚀降解、无辐射毒性的材料类别（陶瓷、纯贵金属、硬质矿石等）。", "evidence": "P013", "ambiguity": "列举为开放式，无完整清单或检测标准。"},
    {"term": "灵魂", "meaning": "作者称人的灵魂会留在遗物上；灵魂可贵则遗物成为无价之宝。", "evidence": "P018", "ambiguity": "属信仰式断言，文中未给出可核验含义。"}
   ],
   "examples_and_targets": [
    "“奢侈品坏掉了心疼是因为你的经济离这个段位太远，等你真正配得上奢侈品你就不会心疼了”（Q001 所引言论，作者的反驳对象；正文未复述）",
    "《蒙娜丽莎》（P004，作者用以反问的类比材料）",
    "忒修斯之船（P010，作者引用的哲学典故，用以说明强可修复性）",
    "实木/复合板家具、硬木/软木、榫卯/特制现代连接件（P011，作者用于价格上限排序的例证）",
    "黄金、白金（P012，作者用以说明性质稳定决定贵金属地位）",
    "陶瓷、稳定良好的皮革、无镀层的不易锈金属、不带漆层的实木、纯贵金属、硬质矿石、天然矿物颜料、耐降解老化面料、高温陶瓷（P013，作者列举的材料类别）",
    "钛合金小刀、马云（P019，作者举例：用了一辈子的小刀最后马云也未必买得起）",
    "顶配手机、特制口红、限量球鞋、电驱超跑（P020，作者列为无资格谈奢侈的对照物）",
    "A piece of history（P009，作者使用的英文短语）"
   ],
   "conditions": [
    "作者的奢侈品判据依赖“有资格进博物馆”“扛过几百年岁月洗礼”“材料不朽”等条件（P001、P006、P013-P015）。",
    "行动提醒的适用条件：不能像忒修斯之船那样拥有强可修复性、同时自身设计又脆弱的东西（P010）。",
    "“只要你买得起，就是便宜的，因为最后是赚的”以买得起为前提（P016）。",
    "“如果是花在了品质上”为条件，才有“越贵反而越赚”的结论（P017）。",
    "“如果你的灵魂是可贵的”为条件，遗物才成为无价之宝（P018）。",
    "作者未说明适用的价格区间、品类边界（如艺术品、数字商品）与时间尺度。"
   ],
   "rhetoric_and_tone": "以连续反问开篇（“有什么资格叫奢侈品？”“坏了谁不心疼？”“难道因为你买得起《蒙娜丽莎》，烧来取暖就不心疼了？”），语气讥诮而强势；以“格调”对“有钱”作对立式断言；中段转训诫口吻（“所以，你们要注意”）；穿插英文短语“A piece of history”；结尾以短句格言收束（“这种浪漫，没有价格”）。",
   "unresolved_questions": [
    "提问所引“心疼因为经济离段位太远”的言论仅见于 Q001，正文未复述，作者只在 P003-P004 以“格调”与反问回应；“配得上就不会心疼”这一心理断言未被逐点反驳。",
    "“有资格进博物馆”的判断主体与标准未说明（P001-P002）。",
    "“格调”的判定标准未界定（P003）。",
    "“强可修复性”的程度门槛、以及“自身设计又脆弱”的判定方式未说明（P010）。",
    "“钛合金小刀最后马云也未必买得起”属夸张修辞式断言，其含义（唯一性/情感价值）未明确界定（P019）。",
    "P013 材料清单以省略号收尾，未给出完整范围或检验标准；P011 的价格上限排序亦无数据来源，需外部核查。",
    "“灵魂留在遗物上”为信仰式断言，文中未给出可核验含义（P018）。",
    "正文完整可读（21 段），本篇无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "没有资格进博物馆的东西，有什么资格叫奢侈品？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "有资格进博物馆的东西，坏了谁不心疼？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这不是有没有钱的问题，而是有没有基本做人的格调的问题。", "relation": "contradicts"},
    {"key": "E004", "paragraph_id": "P004", "quote": "难道因为你买得起《蒙娜丽莎》，烧来取暖就不心疼了？", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P004", "quote": "你真以为它只值你买的那点钱啊？", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "是这东西有机会扛过几百年的岁月洗礼", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P006", "quote": "它里面凝聚的智慧和努力也有这个资格得到守护和加持。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "成了一件活的传世之物。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "为不能像忒修斯之船那样拥有强可修复性，同时自身设计又脆弱的东西付出过高价格是不值得的。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "实木家具要比复合板家具价格上限高，实木之中硬木又比软木高，榫卯又比特制现代连接件的高。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "那是因为它们性质稳定可供传承。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P013", "quote": "陶瓷、稳定良好的皮革、无镀层的不易锈的金属、不带漆层的实木、纯贵金属", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "这些东西都是真正“奢侈品”的骨肉来源。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P015", "quote": "不朽的材料用配得上不朽的方法组织起来，形成的结晶配得上你灌注个人的价值。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P016", "quote": "只要你买得起，就是便宜的，因为最后是赚的。", "relation": "qualifies"},
    {"key": "E016", "paragraph_id": "P017", "quote": "如果是花在了品质上，常常越贵反而越赚。", "relation": "qualifies"},
    {"key": "E017", "paragraph_id": "P018", "quote": "追随过你的每一件东西都会是无价之宝。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P019", "quote": "你兜里这把用了一辈子的钛合金小刀，最后马云也未必买得起。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P020", "quote": "基本没有资格谈奢侈。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P021", "quote": "这种浪漫，没有价格。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P009", "quote": "A piece of history.", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P005", "quote": "拥有“奢侈品”的正确姿势是什么？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["消费与物质文化", "生活方式与格调", "器物与材料知识", "财富观"],
   "issue_candidates": ["奢侈品判准（博物馆资格/可修复性/材质不朽）", "心疼与否是钱的问题还是格调问题", "高价消费品的价值评估", "传世与传承"],
   "text_function_candidates": ["答疑", "批评", "论辩", "经验总结", "训诫"],
   "object_candidates": ["提问者转述的言论持论者", "《蒙娜丽莎》", "忒修斯之船", "马云", "奢侈品消费者"],
   "working_keywords": ["奢侈品", "博物馆", "格调", "忒修斯之船", "强可修复性", "传世之物", "不朽的材料", "骨肉来源", "钛合金小刀", "A piece of history"]
  },
  "notes": "本篇无图片节点，正文完整可读（21 段）。提问所引“心疼是因为经济离段位太远”的言论只在 Q001 出现、正文未复述，已按 opponent_view / opponent 记录并以 P003 作为作者的正面否定证据，未把它归入作者主张。P011 价格排序、P012 贵金属成因、P013 材料清单均无出处，仅登记为待外部核查，未作事实裁决。P018 的“灵魂”说法属信仰式断言，已按作者归属记录并列入未决问题。"
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
