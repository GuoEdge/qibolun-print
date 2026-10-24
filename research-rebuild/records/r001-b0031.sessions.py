# -*- coding: utf-8 -*-
"""批次 r001-b0031 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0031.sessions.py            # 写 out/r001-b0031.out.jsonl
  python3 records/r001-b0031.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0031"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0031.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "fdf47337": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：学习世界史对孩子有什么好处？作者不限于列好处，先把世界史定为“第一重要”同时又“第一容易被轻视、第一容易被教错”的课程，再分两块展开：为何第一重要（决定“交流频宽”、是唯一最佳的社会化与人生观来源）、为何容易被教错（核心目标不是造就知识而是造就技能，要害在史才训练）；最后把“史才”定义为“怀疑与相信的艺术”，并转入怀疑能力的培养。文末标“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "立论：世界史是第一重要的课程，也是最容易被轻视与教错的课程。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "论证重要：世界史版本决定“交流频宽”与文明联结程度；版本冲突者无从对话，版本重合者拥有“共同上下文”，故版本数量决定能沟通多少“频道”。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "推论：掌握够多即获“沟通异界的使者”与管理领导的优势，成为意识形态世界的“马六甲海关”，并保障孩子的生存空间与生存权。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "进一步主张：多版本世界史的交叉洗礼是最重要的社会化手段，远优于“言传身教”；因个人经历不能替代它成为人生信条的提取来源。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "反驳三种人生观来源：模仿成功者（幸存者偏差、“人模子”）、父母经验（残缺、结果随机、算不上教育）、社会传统（被当代借尸还魂的“新传统”）；对第三种承认现实合理性，因管理者为“模范公民”准备生存优势，但兑现在上天手里；声明非针砭时弊。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022"], "summary": "结论：多重世界史教育是唯一最佳模式，因它提供最大可能性的展示与研究，类比科学作为自然史学。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028"], "summary": "转入“被教错”：核心目标不是造就知识，而是造就技能和技能的体验，这是最致命的要害。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P029", "P030", "P031"], "summary": "区分“世界史教育”（人格养成，史才为先、史学次之、史识最轻）与“教世界史”（传统教学，最重史识）。", "role": "definition"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "界定“历史”＝世上曾发生过的一切事件（含自然史学）；“多版本的世界史”＝一切维度对整个绝对历史的交叉观察，起点是时空的开端。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041"], "summary": "重定义史家四长：史才＝鉴定材料的能力；史学＝系统的历史观点；史识＝对基本材料的掌握；史德＝唯理唯真的学术态度。", "role": "definition"},
    {"unit_id": "U011", "paragraph_refs": ["P042", "P043", "P044", "P045"], "summary": "论证核心是史才：史才是一切的前提；史学只是片面、不可靠的副产物；史识是受史学影响的“意识量子”，非“真相只有一个”可概括。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P046", "P047"], "summary": "教育伦理理由：除史才外属受教育者灵魂的私域与人的主权领土，教育者不可擅动，故切入点应专注于史才。", "role": "reason"},
    {"unit_id": "U013", "paragraph_refs": ["P048", "P049", "P050"], "summary": "史才大成会自然带来活的史学、最好的史识与史德；靠麻木自欺制造的“勇气替代品”是病态。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P051", "P052"], "summary": "告诫教育者不要执着于对方的史学或史识，否则立场损坏、史德已失，反失去达成其史才成就的机会。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067"], "summary": "史才＝“怀疑与相信的艺术”；先谈艺术：艺术不是油画音乐，而是坚持创新的结果，是人类天然的使命；其关键词是反复的自我革新，故艺术追求无失败，只有不追求才是唯一失败。", "role": "definition"},
    {"unit_id": "U016", "paragraph_refs": ["P068", "P069", "P070", "P071", "P072", "P073", "P074"], "summary": "指出要害迷思：“相信即是不怀疑”的模型是世界上最邪恶的陷阱，一切意识形态冲突、派系斗争、族群分裂都与之有关，教育应教人揭露和回避它。", "role": "claim"},
    {"unit_id": "U017", "paragraph_refs": ["P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085"], "summary": "提出“信为疑之余，疑为信之本”：所信是竭尽怀疑后仍站立之物；要求展示一切质疑；怀疑技艺幼稚者只享有人道主义待遇，不应获得高于基本人权的礼遇。", "role": "claim"},
    {"unit_id": "U018", "paragraph_refs": ["P086", "P087", "P088", "P089", "P090", "P091", "P092"], "summary": "授权准则：把权力严格授予有怀疑态度与能力者；以“信仰的方式”而非内容为准绳；如此者才明白方法才是核心、才能有效合作并由价值占据资源泉眼。", "role": "action_advice"},
    {"unit_id": "U019", "paragraph_refs": ["P093", "P094", "P095", "P096", "P097", "P098", "P099"], "summary": "警示：仁慈不包括把权柄授予不配得者，宁可直接捐赠也不可滥发“神器”；罪责在授人以柄者，该行的天道是不授予超出其怀疑能力的权力。", "role": "action_advice"},
    {"unit_id": "U020", "paragraph_refs": ["P100", "P101", "P102", "P103", "P104", "P105"], "summary": "反推自身处境：据此筛选老师、上司与子女的教师，则一生与子女一生不虚度、有最大限度的平安。", "role": "action_advice"},
    {"unit_id": "U021", "paragraph_refs": ["P106", "P107", "P108", "P109", "P110", "P111", "P112"], "summary": "该模型附带的“神器”是影响力：不靠装神弄鬼、人多势众或富贵逼人，成本为零、可无限复用；但以神器为恶是极端危险的蠢行。", "role": "claim"},
    {"unit_id": "U022", "paragraph_refs": ["P113", "P114", "P115", "P116", "P117", "P118", "P119"], "summary": "谈培养怀疑能力：首先要说服的对象是自己而非别人；多数人把对话目的设为说服别人，改不动便放弃。文末标“（未完，待续）”并附收藏夹列表。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学习世界史对孩子是第一重要的课程，同时又是第一容易被轻视、第一容易被教错的课程。", "evidence": ["E01", "E02"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "掌握的世界史版本决定一个人的“交流频宽”，从而决定性影响他与他人、与人类文明的联结程度，也决定他能与多少“频道”的人沟通。", "evidence": ["E03"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若掌握得够多，就能获得“沟通异界的使者”式优势，即管理与领导职位的优势，并可凭版本数量成为意识形态世界的“马六甲海关”。", "evidence": ["E04"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "多版本世界史的交叉洗礼是少年儿童最重要也最有意义的社会化手段，其有效性远超“言传身教他如何待人接物”，后者只是一种原始的迷信。", "evidence": ["E05", "E06"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "模仿历史成功者、沿用父母经验教训、跟随社会传统这三种确立人生观的方法都有显而易见的逻辑上的致命缺陷。", "evidence": ["E07"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "历史名人的成功与其人生选择的关系是非必然的，事后看似英明的判断往往只是幸存者偏差造成的错觉；他们被塑造为“人模子”更多是教育话语权掌握者希望生产某个型号的产品。", "evidence": ["E08", "E09"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从父母经验教训出发是残缺不全的荒谬思路：父母的总结能力少经严格思辨训练，其影响结果事实上是随机的，本质上算不上“教育”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何“传统”事实上都只能是被当代重新借尸还魂的“新传统”，是从属于社会管理者当前诉求的产物。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "第三种方法确有一定意义上的现实合理性：管理者会从法理、规则与资源分配上为“模范公民”准备生存优势作为奖励；可虑者是该奖励架构能否支撑足够久以兑现。作者声明这不是“针砭时弊”，各国各文化各时期都在运营此体系。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要得到能应对父母也无法断言的未来挑战的人生观，唯一符合逻辑的教育方法就是“多重世界史教育”。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界史教育的核心目标不是为了造就知识，而是为了造就技能和技能的体验，这是世界史教育最致命的要害。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“世界史教育”是以教授世界史为形式的人格养成，成果史才为先、史学次之、史识最轻；“教世界史”则最重史识。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者语境的“历史”包含世上曾发生过的一切事件；数学、物理、化学也属“自然史学”部门。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“多版本的世界史”不是“多国版本”的人类文明史，而是指一切维度的对整个绝对历史的交叉观察，以自然史为核心与先导，起点是时空的开端。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的史家四长用法：史才是鉴定材料的能力（善辨真伪、善存良疑）；史学是系统的历史观点；史识是对基本材料的掌握；史德是唯理唯真、不唯上不唯古不唯势不唯私的学术态度。", "evidence": ["E20", "E21", "E22", "E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界史教育的核心是史才：史才是一切的前提和核心；史学是上帝专有的奥秘、人类只能得到质量不高的副产物，重要却不可靠；史识是受史学影响的“意识量子”，绝非“真相只有一个”可概括。", "evidence": ["E24", "E25", "E26", "E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从教育者伦理看，除史才之外的内容不可追求也不该由教育擅加干预，因为那属于受教育者灵魂的私域与人的主权的绝对领土。", "evidence": ["E28", "E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "史才大成，人一定会获得自己的活的史学和最好的史识，并因此自然拥有最好的史德；那是人生勇气最好、最健康的来源，而靠麻木与自欺制造的勇气替代品是病态且不会有好结果。", "evidence": ["E30", "E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "教育者若执着于受教育者将持何种史学或史识，会因自身立场损坏、史德已失而失去达成对方任何史才成就的根本机会。", "evidence": ["E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "史才即“怀疑与相信的艺术”；艺术不是油画雕塑音乐舞蹈，而是坚持创新的结果，是人类作为智慧生物天然也是当然的使命。", "evidence": ["E33", "E34", "E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术的关键词是反复的自我革新，“没有什么是够好的，没有什么是不该继续改变的”；因此艺术追求没有失败可言，只有不追求本身才是唯一的失败。", "evidence": ["E36", "E37"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“相信即是不怀疑，怀疑即是不相信”的思维模型是世界上最邪恶、最残酷、最阴暗的陷阱，世界上的意识形态冲突、派系斗争、族群分裂都与之有关；教育若有目的，首先应是教人揭露和回避它。", "evidence": ["E38", "E39"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“信为疑之余，疑为信之本”：所信之物是竭尽怀疑的技术与艺术之后仍站立之物；它有多值得相信只看你为它竭尽了多少怀疑努力，客观世界也是这样看待你的信。", "evidence": ["E40", "E41"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "怀疑技艺幼稚、习惯薄弱者只应享有人道主义待遇，不应获得高于基本人权的额外权利与礼遇；手握影响他人命运的权柄时，应把权力严格授予拥有怀疑态度与能力者（这也正是有信的态度与能力），并以“信仰的方式”而非“信仰内容”为准绳。", "evidence": ["E42", "E43", "E44", "E45"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "遵循该模型者必然经历若干次派别转换，最终明白宗派是虚妄、结论是云烟而“方法”本身才是信仰的核心；只有这样的人才能有效合作，进而由合作产生价值并占据资源泉眼。", "evidence": ["E46", "E47"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有这能力的人在任何社会制度下最终都只能仰赖仁慈，而仁慈不包括把权柄授予不配得者（可直接捐赠但不要滥发“神器”）；不遵从该模型者会把被授予的权力立刻用作党同伐异的利刃，罪责在授人以柄的一方，因为怀疑的能力与态度决定信的质量，而信的质量是领受天赋权力的资格。", "evidence": ["E48", "E49", "E50", "E51", "E52", "E53", "E54"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该模型附带“影响力”这件神器：怀疑的技艺令人敬畏时，所信之物自然获得重量，不靠装神弄鬼、人多势众或富贵逼人；它成本为零、可无限复用，但以神器为恶是极端危险的蠢行。", "evidence": ["E55", "E56", "E57"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "培养怀疑能力的首个关键点是：需要说服的对象是你自己，而不是别人；多数人把对话目的设为说服别人，因此不给自己带来改变，改不动别人便放弃。", "evidence": ["E58", "E59"]}
   ],
   "argument_steps": [
    "立论：世界史是第一重要、也最容易被轻视与教错的课程（P001—P002）。",
    "论证重要：版本决定“交流频宽”（P003）；版本冲突则对话无从继续（P004）；版本重合则拥有“共同上下文”（P005）；故版本数量等于沟通“频道”数（P006）。",
    "推出优势：成为“沟通异界的使者”、领导优势、“马六甲海关”，保障孩子生存空间（P007—P009）。",
    "升级主张：多版本世界史是最重要的社会化手段，优于“言传身教”（P010—P011）。",
    "反驳三种人生观来源：模仿成功者（幸存者偏差）（P012、P014）；父母经验（残缺、随机）（P015）；社会传统（“新传统”）（P016）；对第三种让步并声明非针砭时弊（P017—P019）。",
    "结论：多重世界史教育是唯一最佳模式，类比科学（P020—P022）。",
    "转折：核心目标不是知识而是技能与技能体验（P023—P028）。",
    "区分“世界史教育”与“教世界史”，提出“史才为先，史学次之，史识最轻”（P029—P031）。",
    "重新界定“历史”与“多版本世界史”的范围（P032—P036），重定义史家四长（P037—P041）。",
    "论证核心是史才：史学是副产物、史识是“意识量子”（P042—P045）；教育伦理上唯史才可为（P046—P047）。",
    "推出效果链：史才大成→活的史学与史识→史德（P048—P050）；告诫教育者勿执着（P051—P052）。",
    "定义史才＝怀疑与相信的艺术，先展开“艺术”＝坚持创新（P053—P067）。",
    "指出“相信即是不怀疑”模型是邪恶陷阱（P068—P074）；提出并解释“信为疑之余，疑为信之本”（P075—P085）。",
    "把该模型用作授权准则（P086—P092）并给出警示（P093—P099）；反推自身处境（P100—P105）。",
    "补充“影响力”神器及危险（P106—P112）；转入培养方法：说服对象是自己（P113—P116），文末未完待续（P117—P119）。"
   ],
   "concept_usage": [
    {"term": "世界史／多版本的世界史", "meaning": "不是“多国版本”的文明史，而是“一切维度的对整个绝对历史的交叉观察”，以自然史为核心与先导，起点为时空的开端。", "evidence": "P035", "ambiguity": "“绝对历史”未另作定义；与常识中的世界史学科差别很大。"},
    {"term": "交流频宽", "meaning": "由所掌握的世界史版本决定的、能与多少“频道”的他人沟通的能力。", "evidence": "P003", "ambiguity": "作者自造的比喻，无量化标准。"},
    {"term": "世界史教育／教世界史", "meaning": "前者是以教授世界史为形式的人格养成（史才为先、史学次之、史识最轻）；后者是传统学科式教学，最重史识。", "evidence": "P030", "ambiguity": "作者把“教世界史”倾向归于东亚乃至世界多数文明多数时段的教育传统，属概括判断。"},
    {"term": "史才／史学／史识／史德", "meaning": "史才＝鉴定材料的能力；史学＝系统的历史观点；史识＝对基本材料的掌握；史德＝唯理唯真、不唯上不唯古不唯势不唯私的态度。", "evidence": "P038", "ambiguity": "借用史家四长术语但改动了内涵，易与通行用法混淆（作者已在 P032 声明）。"},
    {"term": "艺术", "meaning": "坚持创新的结果：任何领域不信邪、不守旧、不休止、百折不回、永不放弃的创新所得到的有生命力的结果。", "evidence": "P059", "ambiguity": "与常识中“美的享受”式艺术定义差异很大。"},
    {"term": "神器", "meaning": "两处用法：一是“滥发神器”中指被授予他人的权柄（P095）；二是“另一样神器，那就是影响力”（P106）。", "evidence": "P106", "ambiguity": "同词在不同段落指不同对象。"}
   ],
   "examples_and_targets": [
    "“世界是被一头土狼从一颗乌鸦的蛋里咬出来的”——版本冲突的假设举例（P004）。",
    "“公平”“正义”“友好”——靠共同上下文才对双方含义接近的词（P005）。",
    "“马六甲海关”“沟通异界的使者”——作者的比喻（P007、P008）。",
    "“言传身教他如何待人接物”——作者反驳的流行教育观念（P010）。",
    "“绝对不要相信外乡人，因为你爹我因为相信外乡人吃过大亏”——作者举的父母式经验表达（P015）。",
    "“模范公民”——第三种模式的理想构建产物（P017）。",
    "It is what it is, just how this world works.——作者插入的英文（P018）。",
    "“前半生受足忠君教育，长大了却面对着一个无君无父的异时代”——应许兑现失败的例子（P019）。",
    "万有引力定律与大球小球先落地的说法——科学式现象考察的举例（P021）。",
    "油画、雕塑、音乐、舞蹈——被作者称为狭隘理解的艺术观（P058）。",
    "“艺术家”是上帝创造人类时为人类指定的预定身份——宗教式表述（P064）。",
    "人工智能占领非艺术类工作领域——作者预言的时间条件（P063）。",
    "上帝、自然、科学、神学——作者举的“信仰内容”标签（P087）。",
    "陪审团只能考虑司法程序所察知的事实——就事论事与合作的类比（P090）。",
    "“太阿倒持，授人以柄”——引用的成语式表述（P097）。",
    "家族答集、企管答集、第一性、社科答集、文艺答集、科学答集、军事技术与艺术、百年未有之变局——文末平台标签列表（P119）。"
   ],
   "conditions": [
    "优势以“如果你掌握得够多”为前提（P007）。",
    "“在清楚自己在做什么的教育者手里”是保障生存空间与生存权成立的条件（P009）。",
    "对第三种来源的肯定限于“一定意义上的现实合理性”，并附“这种奖励架构自己需要支撑足够久”（P017）。",
    "作者声明不是“针砭时弊”，并称各国各时期都在运营该体系（P018）。",
    "应许能否兑现“是掌握在上天手里的神秘事物”（P019）。",
    "对教育者的告诫以“凡有这种执着”为条件（P052）。",
    "对怀疑技艺不足者的处置以“人道主义待遇”“基本人权”为底线（P084）。",
    "权力的授予以“当你手握能影响他人命运的权柄”为前提（P086）。",
    "“影响力”仍附警告：“以神器为恶是极端危险的蠢行”（P112）。",
    "培养怀疑能力的讨论在 P117 标“（未完，待续）”，本篇未完成。"
   ],
   "rhetoric_and_tone": "长篇论说兼训诫，第二人称“你”贯穿；以设问推进（“为什么这样说？”“何谓史才？”“什么是艺术？”）；用强烈判语（“最邪恶、最残酷、最阴暗的陷阱”“极端危险的蠢行”）与大量比喻、自造术语（“交流频宽”“马六甲海关”“借尸还魂”“神器”“穿金裂石”“太阿倒持”）；出现一句英文与“上帝”“天道”“预定身份”等宗教性措辞；以“（未完，待续）”与收藏夹列表收尾。",
   "unresolved_questions": [
    "本篇标“（未完，待续）”，培养怀疑能力的具体方法未展开（P117）。",
    "P119 为收藏夹/平台标签列表，属结构残留；“百年未有之变局”位于 lexical 未覆盖片段。",
    "“绝对历史”“天赋权力”“再赋权”的界定本文未说明。",
    "“史学是质量不高的副产物”（P044）与 P039 的史学定义如何调和，作者未展开。",
    "P004“人类学、认知科学、语言学上极其浅白的事实”未给文献，属待外部核查。",
    "P014 的“幸存者偏差”与 P021 的科学结论来源论述均无数据或文献。",
    "以“上帝创造人类时为人类指定的预定身份”说明艺术，其宗教前提本文未论证。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P001", "quote": "学习世界史对孩子而言是第一重要的课程。", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P002", "quote": "世界史又是第一容易被轻视，也是第一容易被教错的课程。", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P003", "quote": "因为一个人所掌握的世界史的版本决定了这个人的“交流频宽”", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P007", "quote": "管理和领导职位的绝对优势条件。", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P010", "quote": "多个版本的世界史的交叉洗礼，是少年儿童最重要也最有意义的社会化手段。", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P010", "quote": "后者仅仅只是一种原始的迷信。", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P013", "quote": "但这三个方法事实上都有显而易见的逻辑上的致命缺陷。", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P014", "quote": "但实际上那只是幸存者偏差所塑造出来的错觉。", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P014", "quote": "教育话语权的掌握者希望生产出某个型号的产品。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "从父母的经验教训出发，实际上也是一个极为残缺不全的荒谬思路。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "本质上甚至都算不上是一种“教育”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "都在事实上只能是被当代重新借尸还魂的“新传统。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "但公平的说，这第三种方法的确存在一定意义上的现实合理性", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P018", "quote": "不要误会我是在“针砭时弊”", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P022", "quote": "唯一符合逻辑的教育方法，就是“多重世界史教育”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "不是为了造就知识，而是为了造就技能和技能的体验。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P030", "quote": "教育的成果史才为先，史学次之，史识最轻。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P034", "quote": "数学，物理学、化学，也是历史研究的成果，只是它们属于“自然史学”部门。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P035", "quote": "而是指一切维度的对整个绝对历史的交叉观察。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P038", "quote": "史才，是鉴定材料的能力。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P039", "quote": "史学，是系统的历史观点", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P040", "quote": "史识，是对基本材料的掌握。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P041", "quote": "史德，是学术的态度。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P043", "quote": "因为史才是一切的前提和核心。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P044", "quote": "史学是神秘事物", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P045", "quote": "史识，则是严重受到史学影响的“意识量子”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P045", "quote": "绝非“真相只有一个”可以概括。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P046", "quote": "其他的内容是不可追求的", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P046", "quote": "属于受教育者灵魂的私域", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P048", "quote": "史才大成，那么人一定会获得自己的活的史学和最好的史识", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P048", "quote": "这将自然而然的造就史德", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P052", "quote": "你都将因为自身立场的损坏而失去达成对方任何史才成就的根本机会", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P054", "quote": "史才即是怀疑与相信的艺术。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P059", "quote": "艺术是坚持创新的结果。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P063", "quote": "天然的也是当然的使命。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P065", "quote": "艺术的关键词，就是反复的自我革新。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P067", "quote": "只有不追求本身才是唯一的失败。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P073", "quote": "这种思维模型是世界上最邪恶、最残酷、最阴暗的陷阱", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P074", "quote": "那就是要教人揭露和回避这个陷阱。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P076", "quote": "信为疑之余，疑为信之本。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P080", "quote": "客观的世界是这样在看待你的信。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P084", "quote": "你不应该被授予高于基本人权的任何额外权利", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P085", "quote": "请你视为别有用心的贿赂。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P086", "quote": "将权力严格的授予那些拥有怀疑的态度与怀疑的能力的", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P087", "quote": "不要以“信仰内容”上与你一致为准绳，而要以“信仰的方式”为准绳。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P089", "quote": "“方法”本身才是信仰的核心。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P091", "quote": "只有这样的人才能有效合作", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P093", "quote": "那些没有这能力的人，在任何社会制度下最终都只能仰赖你的仁慈。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P094", "quote": "但仁慈绝对不包括将这权柄授予还不配得的人", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P095", "quote": "但绝对不要滥发神器", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P096", "quote": "用作党同伐异的利刃。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P097", "quote": "罪责在你，在于太阿倒持，授人以柄的你。", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P098", "quote": "的法则本身才是你该行的天道！", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P099", "quote": "信的质量，是你领受天赋权力的资格。", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P106", "quote": "这个模型还附有另一样神器，那就是影响力。", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P110", "quote": "这是人所不能抗拒的、成本为零、可以无限复用、甚至越用越锋利的神器。", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P112", "quote": "以神器为恶是极端危险的蠢行，不要抱有任何侥幸。", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P114", "quote": "你需要说服的对象是你自己，而不是别人。", "relation": "supports"},
    {"key": "E59", "paragraph_id": "P116", "quote": "而仅仅是在尝试改变别人", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "史学理论", "认识论", "家族与家训", "管理与权力"],
   "issue_candidates": ["世界史教育的价值", "多版本世界史与交流频宽", "人生观的形成途径", "幸存者偏差", "史才与史家四长", "信与疑的关系", "权力授予的标准", "艺术与创新"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "系列讲稿（未完待续）", "教育方案陈述"],
   "object_candidates": ["孩子", "父母", "教育者", "社会管理者", "模范公民", "历史名人", "上帝", "人工智能", "家族答集"],
   "working_keywords": ["世界史", "交流频宽", "共同上下文", "马六甲海关", "多版本世界史", "史才", "史学", "史识", "史德", "人格养成", "自然史学", "意识量子", "怀疑与相信的艺术", "信为疑之余", "疑为信之本", "神器", "影响力"]
  },
  "notes": "正文 119 段、8087 字，文末标“（未完，待续）”（P117），为系列讲稿；P119 为收藏夹/平台标签列表，其中“百年未有之变局”位于 lexical 未覆盖片段。提问问的是“好处”，作者的回答扩展到教育目标、史学理论与授权伦理，已按正文实际结构记录。作者在 P032 声明借用史家四长术语但内涵不同，已在 concept_usage 登记。本记录因超出单篇 40000 字节上限已压缩：合并同类主张与内容单元、短引只留最短连续片段；证据定位与未决问题未删减。"
 },
 "d49d3828": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：从你的经历来看，什么时候感到做一个中国人很幸福？提问者指定“从你的经历来看”。作者以“谢邀。”开头，直接列出六条具体场景作为回答，未作展开论证，也未说明这些场景与“中国人”身份之间的关系。其中第 4 条自带限定“这个算喜忧参半”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以“谢邀。”应答。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "第 1—3 条：写毛笔字；阅读古文／看日文／读韩语；吃饭。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "第 4 条：移动支付——作者注明“这个算喜忧参半”。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "第 5—6 条：在地铁、高铁、大巴上用 4G；半夜撸串。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对“什么时候感到做一个中国人很幸福”的回答是六条场景清单：写毛笔字、阅读古文／看日文／读韩语、吃饭、移动支付、在地铁高铁大巴上用 4G、半夜撸串。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "移动支付这一条被作者附加限定为“喜忧参半”。", "evidence": ["E4"]}
   ],
   "argument_steps": [
    "以“谢邀。”应答（P001）。",
    "依次列出六条场景，中间不展开理由（P002—P007）。",
    "在第 4 条后插入限定“这个算喜忧参半”（P005）。"
   ],
   "concept_usage": [
    {"term": "幸福（很幸福）", "meaning": "本文未给定义，只以六个具体场景示例作答（写毛笔字、读古文／日文／韩语、吃饭、移动支付、用 4G、半夜撸串）。", "evidence": "P002", "ambiguity": "作者未说明这些场景为何与“做一个中国人”相关，也未说明它们与提问者“从你的经历来看”的对应关系。"},
    {"term": "喜忧参半", "meaning": "作者对“移动支付”一条给出的限定性评价，表示它同时带来好处与忧虑。", "evidence": "P005", "ambiguity": "作者未说明“忧”具体指什么。"}
   ],
   "examples_and_targets": [
    "写毛笔字——第 1 条（P002）。",
    "阅读古文 / 看日文 / 读韩语——第 2 条（P003）。",
    "吃饭——第 3 条（P004）。",
    "移动支付——第 4 条，附“喜忧参半”（P005）。",
    "在地铁、高铁、大巴上用 4G——第 5 条（P006）。",
    "半夜撸串——第 6 条（P007）。"
   ],
   "conditions": [
    "提问要求“从你的经历来看”，作者以场景清单作答，未说明这些是否为亲身经历（P001—P007）。",
    "第 4 条自带限定“这个算喜忧参半”（P005）。"
   ],
   "rhetoric_and_tone": "极简清单式回答，全文只有“谢邀。”加六条短语，每条不超过一句；不作解释、不给理由、不表态；唯一带评价色彩的是第 4 条后的“这个算喜忧参半”。",
   "unresolved_questions": [
    "作者未说明这些场景为何属于“做一个中国人很幸福”，也未说明其中哪些是亲身经历，提问所问的“你的经历”未被展开。",
    "“移动支付——这个算喜忧参半”中的“忧”具体所指，本文未说明。",
    "六条清单中的“看日文 / 读韩语”与“中国人”身份的关系，本文未说明。",
    "正文极短（73 字），属清单式回答；brief 内容与正文前六条基本一致，未提供额外正文信息。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "1）写毛笔字", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P006", "quote": "5）在地铁、高铁、大巴上用4G", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "6）半夜撸串", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "4）移动支付——这个算喜忧参半", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生活经验", "文化认同"],
   "issue_candidates": ["身为中国人的幸福时刻", "日常生活中的文化体验", "移动支付的双面性"],
   "text_function_candidates": ["答疑", "清单式回答"],
   "object_candidates": ["作者本人（未展开）", "中国人"],
   "working_keywords": ["谢邀", "毛笔字", "古文", "日文", "韩语", "移动支付", "喜忧参半", "4G", "撸串"]
  },
  "notes": "正文仅 73 字、7 段，为清单式极简回答，无展开论述；提问要求“从你的经历来看”，作者未展开经历细节，已在 unresolved_questions 登记。“移动支付”一条带作者自己的限定“这个算喜忧参半”，已按 author_qualified 记录。"
 },
 "4624f253": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：和弓的效率为什么这么低。？提问者预设了“和弓效率低”。作者不接受该预设，开篇即断言和弓是非常聪明的设计、是弓箭设计的优秀流派，并从古代制弓的材料障碍讲起，推出“把弓做长”的解法、长度的自然限制，以及日本人在对称性上的突破，最后以“受住几百年战场考验”为理由认为和弓可以免于这类简单质疑。本篇含 2 个图片节点，图片内容未经核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "立论：和弓是非常聪明的设计、是弓箭设计的优秀流派；理由是古代制弓最大的障碍是材料。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "材料问题：硬材料与硬而轻的材料都不少，但弹性材料太少；非理想弹性体在拉弯与释放时两次扣除纤维错位摩擦的热能，这是古代单体弓“效能不好”的根源，也影响弓的寿命与工况性能衰减。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "旁证：古代的弓射一会儿就要放下等弓“休息”，作者解释为给时间让木纤维渐渐修复、消除积累的错位。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "解法链：弹性好的软物质为磅数要做粗而加重内摩擦，故把弓做长；拉距相对稳定，弓越长满弓形变越小，从而可用较硬的材料并做得更细，进一步抑制内摩擦、提高效能；弓长因而成为性能的关键参数。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "小结式复述：为磅数加粗会加重双重摩擦损耗，最好的办法是把弓做长；形变足够小则高硬度材料可用；越长、形变越小、越能用硬材料，材料越硬越能做细做轻、效能越好——“可见长就是一切”。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "提出限制问题：弓最多能做多长？下梢受守城俯射（不能过膝盖）与马上携带（不宜超过马镫）的限制，若坚守对称弓形，全长就被限定。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018"], "summary": "转折：各国不约而同认为弓以对称为好（设计更简单、审美更漂亮、发射逻辑更通顺），只有日本人想通了“谁说下面多长上面就要多长”。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020"], "summary": "给出和弓的形制与数据：长 2.2—2.3 米（英国长弓不过 2 米，和弓比欧洲最长的弓还长 15%），而日本人身材与马都更矮小；侧面看上臂比下臂长一倍左右，正面看弦不中分弓臂、完全面对箭头看弦可见。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "结论：这种两轴都不对称的设计在古代非常大胆，至今没有第二家这么做；能造出这种设计的匠师不太可能忽视效率，正如不会怀疑飞机设计师把螺旋桨做小了；和弓受住几百年战场考验，可以免于一切简单的质疑，拥有它该有的地位。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "和弓是非常聪明的设计，称得上弓箭设计的优秀流派；作者把理由落在古代制弓最大的障碍是材料这一点上。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大多数物质弹性形变非线性且非理想弹性体，拉弯与释放各发生一次纤维错位摩擦，于是发生第二次能量扣除；这是古代单体弓“效能不好”的根源，也严重影响弓的寿命与工况性能衰变。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代的弓每射一会儿要放下等弓“休息”，作者解释为给时间让木纤维渐渐修复、尽可能消除前面积累的错位。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "弹性好的软物质为达磅数要做粗，做粗后内摩擦加重；解法是把弓做长——拉距相对稳定时弓越长满弓形变越小，形变足够小就可用较硬材料并做得更细，从而抑制内摩擦、提高效能。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "弓越长对材料的要求越低，可用更硬材料做得更细，且弓变细后更多弹性势能分配给箭而不是弓臂，故弓的长度成为弓的性能的关键参数。", "evidence": ["E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "弓长受下梢限制：为守城俯射下梢一般不能过膝盖，为马上携带下梢不宜超过马镫；若坚守对称弓形，全长也就被限定。", "evidence": ["E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界各国不约而同认为弓以对称为好（设计更简单、审美更漂亮、发射逻辑更通顺），只有日本人想通了“谁说下面多长上面就要多长”。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "和弓长约 2.2—2.3 米，比欧洲最长的弓还长 15%，而日本人与日本马都比欧洲矮小；它侧面不对称（上臂比下臂长一倍左右），正面弦不中分弓臂、完全面对箭头看弦是暴露可见的。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种两轴都不对称的设计在古代非常大胆，至今没有第二家这么做；经验丰富到敢于造这种设计的匠师不太可能犯下忽视效率的错误。", "evidence": ["E19", "E20"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "和弓作为明显的双轴不对称设计受住了几百年战场考验，很自然可以免于一切简单的质疑，拥有它该有的地位。", "evidence": ["E21"]}
   ],
   "argument_steps": [
    "先否定提问预设：和弓是非常聪明的设计（P001）。",
    "指出制弓的根本障碍是材料：硬的、硬而轻的都不缺，缺的是弹性材料（P002—P003）。",
    "解释能量损失机制：非理想弹性体在拉弯与释放时发生两次纤维错位摩擦，造成能量扣除（P003）；这是古代单体弓“效能不好”的根源，并影响寿命与性能衰变（P004）。",
    "以“弓要休息”为旁证说明纤维错位的积累与修复（P004）。",
    "给出解法：软材料为磅数加粗会加重内摩擦，故把弓做长（P005—P006）。",
    "论证长的好处：拉距相对固定，弓越长满弓形变越小，可用更硬的材料并做得更细，进一步抑制内摩擦（P007—P008），故弓长是关键性能参数（P009）。",
    "复述并强化：加粗导致双重摩擦损耗，做长是最好办法；“长就是一切”（P010—P013）。",
    "提出限制：下梢受膝盖与马镫约束，坚守对称则全长被限定（P014—P016）。",
    "对比各国成见与日本的突破：只有日本人质疑上下等长的前提（P017—P018）。",
    "给出和弓的尺寸、对比数据与两轴不对称的形制特征（P019—P020）。",
    "以“设计大胆且无人仿效”“匠师不会忽视效率”作反证（P021—P023），并落在“受住几百年战场考验”上，认为其可免于简单质疑（P024）。"
   ],
   "concept_usage": [
    {"term": "效能／效率", "meaning": "本文中主要指能量转换效率：拉弓储存的弹性势能在释放时有多少被内部摩擦扣除、多少分配给箭。作者用“效能不好”解释古代单体弓，而未直接接受提问中“和弓的效率低”。", "evidence": "P004", "ambiguity": "提问用的“效率”与作者用的“效能”是否同义，作者未说明，也未给出任何效率数值。"},
    {"term": "内摩擦（纤维错位摩擦）", "meaning": "木纤维在超出一定限度的形变中发生错位与恢复不完全，两次摩擦各扣除一次能量，并随拉放次数积累而使弓力下降。", "evidence": "P003", "ambiguity": "作者未给出材料学数据或引用。"},
    {"term": "拉距", "meaning": "取决于人的臂展、相对稳定的拉弓行程；作者以它固定为前提推出“弓越长形变越小”。", "evidence": "P007", "ambiguity": "未给具体数值。"},
    {"term": "对称弓形／双轴不对称", "meaning": "各国默认弓上下等长（对称）；和弓则侧面（上臂长于下臂）与正面（弦不中分弓臂）两轴都不对称。", "evidence": "P020", "ambiguity": "“双轴”具体指哪两轴，作者以“侧面看”“正面看”说明，未作术语定义。"},
    {"term": "守城／马上携带", "meaning": "作者举出的两项使用场景，用来解释下梢长度为何受限（不过膝盖、不超过马镫）。", "evidence": "P015", "ambiguity": "作者未说明这两项限制的史料来源。"}
   ],
   "examples_and_targets": [
    "提问者的“和弓的效率为什么这么低”——被作者质疑的预设（P001、P023）。",
    "古代单体弓——作者用作“效能不好”的对照对象（P004）。",
    "弓射一会儿就要放下等弓“休息”——作者举的实际使用现象（P004）。",
    "英国长弓（不过 2 米）——作者用作和弓长度的对比对象（P019）。",
    "日本人的身材与日本马的身高——作者用作“弓却更长”的对比（P019）。",
    "欧洲马——作者用作与日本马对比（P019）。",
    "“这就好像在怀疑上面这架飞机的设计师把螺旋桨做小了”——作者使用的飞机设计类比（P023）。",
    "“几百年战场考验”——作者用来支持和弓地位的历史论据，未给具体时期或战例（P024）。",
    "图片节点 IMG001、IMG002——本篇含 2 张图片，内容未经核验，无法确认其是否与和弓形制或数据有关（见 structure.images）。"
   ],
   "conditions": [
    "“效能不好”的结论限于“古代单体弓”这一对象（P004）。",
    "做长弓的前提是“拉距确定”（P007）。",
    "可用硬材料的前提是“当形变足够小”（P007）。",
    "下梢限制分两种场景：守城时不能过膝盖、马上携带时不宜超过马镫（P015）。",
    "全长被限定以“你要坚守对称弓形”为条件（P016）。",
    "对匠师的判断用反问句式“有多大可能会犯下忽视效率的错误？”，属推论而非直接断言（P023）。",
    "“免于一切简单的质疑”以“受住了几百年战场考验”为依据（P024）。"
   ],
   "rhetoric_and_tone": "技术性说明与反驳混合，语气自信；以设问组织（“为什么呢？”“如何解决？”“现在问题来了——弓最多能做多长？”）；用递进复述强化（“为了磅数，于是加粗……”“越长，形变越小……可见长就是一切”）；含夸张式比喻（“怀疑上面这架飞机的设计师把螺旋桨做小了”）；以“只有日本人想通了这一层”作转折；结尾用“受住了几百年战场考验”“拥有它该有的地位”收束，带为和弓辩护的色彩。",
   "unresolved_questions": [
    "本篇含 2 个图片节点（IMG001、IMG002），图片内容未核验，无法确认图中是和弓形制、数据图表还是其他内容，需人工或多模态复核。",
    "提问所问的“效率低”作者未给出数值化的效率比较，也未回应提问者据以提问的来源。",
    "纤维错位摩擦的机制描述（两次能量扣除、弓需“休息”修复）无材料学数据或文献，属待外部核查。",
    "“各国不约而同认为弓以对称为好”“只有日本人想通了”的范围与史料依据，本文未说明。",
    "和弓尺寸（2.2—2.3 米）与英国长弓（2 米）、日本人与日本马身高的对比数据未注明来源。",
    "“受住了几百年战场考验”未给出具体时期、战例或文献。",
    "正文中“这就好像在怀疑上面这架飞机的设计师把螺旋桨做小了”一句出现“上面这架飞机”，但正文并无对应图片或上文，所指不明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "和弓是一种非常聪明的设计，称得上弓箭设计的一个非常优秀的流派。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因为在古代制弓最大的障碍就是材料。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你付出的能量有很多都会变成木材内部纤维错位摩擦的热能", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "于是就会发生第二次的能量扣除。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "这就是古代单体弓“效能不好”的根源。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "所谓的休息，就是给时间让木纤维渐渐修复", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "越是弹性好的软物质，为了磅数就要做粗。做粗之后这个内摩擦问题就会加重。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "拉距确定的前提下，弓越长，则满弓时弓臂的形变就越小。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "进一步的抑制内摩擦，进一步的提高效能", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "弓本身细了之后更能保证弹性势能释放时更多的能量被分配给箭而不是分配给弓臂", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "这就使得弓的长度成了弓的性能的关键参数。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "考虑到要守城，下梢一般不能过膝盖，再低俯射就不方便了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "既然下梢只能这么长，你要坚守对称弓形，自然全长也就被限定了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "世界各国都不约而同的认为弓这个东西还是对称为好。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "只有日本人想通了这一层——谁说下面多长上面就要多长？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "和弓长度一般在2.2-2.3米左右。作为对比，即使是英国长弓也不过2米长。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "使用的弓却比欧洲最长的弓还要长15%。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "和弓不但在侧面看不对称，上臂比下臂长一倍左右", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "这种设计真的是古代各家设计中非常大胆的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "已经经验丰富到敢于造这种两轴都不对称的设计的匠师，有多大可能会犯下忽视效率的错误？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "和弓作为一个显然的双轴不对称设计受住了几百年战场考验，很自然就可以免于一切简单的质疑", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["兵器技术史", "材料力学", "日本文化"],
   "issue_candidates": ["和弓的效率", "制弓材料与弹性极限", "内摩擦与能量损耗", "弓长与形变", "对称与不对称弓形", "日本的弓形突破"],
   "text_function_candidates": ["答疑", "技术解释", "反驳（为和弓辩护）"],
   "object_candidates": ["和弓", "古代单体弓", "英国长弓", "欧洲马", "日本马", "日本匠师", "提问者"],
   "working_keywords": ["和弓", "弹性材料", "纤维错位", "内摩擦", "效能", "拉距", "磅数", "对称弓形", "双轴不对称", "英国长弓", "上臂", "下臂", "弦影"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 2 个图片节点（IMG001、IMG002，src 见 structure.images），图片内容未经核验，需图像核验；已读部分为正文文本。正文中“这就好像在怀疑上面这架飞机的设计师把螺旋桨做小了”（P023）提到“上面这架飞机”，但正文与图片清单中无对应对象，所指不明，已在 unresolved_questions 登记。作者未直接否认提问的前提，而是否定“和弓效率低”的质疑，并明确说和弓“可以免于一切简单的质疑”，已在 main_claims 中按反驳对象与作者主张分别记录。"
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
