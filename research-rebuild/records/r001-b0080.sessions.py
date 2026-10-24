# -*- coding: utf-8 -*-
"""批次 r001-b0080 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0080.sessions.py            # 写 out/r001-b0080.out.jsonl
  python3 records/r001-b0080.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0080"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0080.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "0be8c071": {
  "analysis": {
   "question_context": "提问者（Q001，知乎问题）问市井大妈吵架的形态为何滑稽、人为什么会变成这种样子，并已预设其形态为“滑稽”。作者（本文正文）没有接受“滑稽”这一框架，而是把焦点前移到定性问题：先反问“为什么可以认定这是‘怪异的举止’”，再论证该行为并不构成可判定的“异常”，而是罕见情境下的本能反应；全文未回答“为何滑稽”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者先反问“怪异”这一定性依据何在，答：这只是“罕见”，罕见源于情境罕见，尤其对观察者自身阶层而言罕见。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "要定性“怪异”须把不同人放入同一情境比较，并有大样本显著差异；否则同样可把迪斯尼员工定义为异常，而人们给迪斯尼员工盖“正常”章只是因为能把自己代入该角色。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "人们认定大妈异常，依据是自信“我到了这个情境也不会和她一样”，或干脆想象不到自己会陷入该情境；作者反问这份自信的依据，并指出没有特别理由说明你不会这样。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "作者主张该行为是强烈刺激下依本能的强迫性反应，是预先写好的程序；未经类似消防员面对火焰的长期训练，只有极小概率是天生的例外；此状态下教育不起作用，人会被锁定在机械模式里。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013"], "summary": "以路上遇响尾蛇为例：教育全部失效、本能僵住、对方不动则自己不改反应模式。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P014"], "summary": "推论：威胁相互时双方同处该模式，形成“双锁定”。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P015"], "summary": "以人工智能无人机自主对抗实验中的长时间“对称盘旋”作类比，说明该现象并非人所独有。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018"], "summary": "结论：该现象几乎与教育水平无关；留过学、读过博士者在人生墙角不见得更好，甚至可能更“可笑”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "被作者引述并质疑的定性：大妈吵架是“怪异的举止”（作者以反问提出，未接受该定性）。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该举止只能算“罕见”，其罕见是因为情境罕见，尤其对观察者自身所属阶层而言罕见。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要定性“怪异”，必须把各种不同的人放到同一情境中比较反应，并有大样本量的显著差异，才能定位为“异常”。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若缺上述判据，同样可以把迪斯尼员工定义为“异常”；人们不这样做，只是因为能把自己代入该角色而给其盖上“正常”章。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判定大妈为“异常”的依据，是自信自己在该情境下不会如此，或根本想象不到自己会遭遇该情境；作者反问该自信的依据，并称并没有特别理由说明你不会这样。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大妈们是在强烈刺激下按本能强迫性地做反应；这是人类被逼入墙角后的本能，是预先写好的程序。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若没有受过类似消防员面对火焰那样的长期训练，人只有极小的概率是天生的例外。", "evidence": ["E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "在该状态下，人所受的教育不起作用（连完整句子都想不起来），只会被锁定在重复句式或重复肢体动作的机械模式里。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "威胁相互时对方也处于该模式，于是形成“双锁定”：双方因对方提供的刺激未变而各自锁定在反应模式中。", "evidence": ["E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该现象在人工智能无人机自主对抗实验中也会呈现：两架有最复杂战术预定的无人机几乎总是陷入长时间“对称盘旋”，直到一方靠性能或续航获得压倒优势。", "evidence": ["E19", "E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种现象几乎与教育水平无关，只是同级别主体激烈对抗自然会导致的现象。", "evidence": ["E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "不要以为留过学、读过博士在人生墙角一定会好一些——真不见得，搞不好还更“可笑”。", "evidence": ["E22", "E23"]}
   ],
   "argument_steps": [
    "反问并悬置提问者的“滑稽”框架，改问“凭什么认定这是‘怪异的举止’”（P001）。",
    "削弱定性：这只是罕见，罕见源于情境罕见，尤其对观察者自身阶层罕见（P002）。",
    "给出定性判据：跨人群同情境比较＋大样本显著差异（P003）。",
    "归谬：按同一逻辑也可把迪斯尼员工判为异常，而人们不判，只因能自我代入（P004-P005）。",
    "指出观察者的实际依据是“我不会和她一样”的自信或想象不到该情境，并反问其依据（P006-P007）。",
    "断言没有特别理由说明你不会这样（P008）。",
    "正面解释：强烈刺激下的本能强迫反应，是预先写好的程序（P009-P010）。",
    "限定条件：除非受过长期专门训练，否则极难例外（P010）。",
    "机制描述：此状态下教育失效，人被锁定在机械模式（P011）。",
    "类比一：遇响尾蛇僵住、一步一动（P012-P013）。",
    "推论：相互威胁导致“双锁定”（P014）。",
    "类比二：AI无人机自主对抗的对称盘旋（P015）。",
    "结论：与教育水平几乎无关，是同级主体激烈对抗的自然结果；学历不构成豁免（P016-P018）。"
   ],
   "concept_usage": [
    {"term": "怪异／异常", "meaning": "本文指对行为的定性判断；作者认为它需要跨人群同情境比较与大样本显著差异作判据，否则不成立。", "evidence": "P003", "ambiguity": "作者始终以引号使用该词，未给出可操作阈值；“异常”与“罕见”在文中被明确对立。"},
    {"term": "罕见", "meaning": "作者用来替代“怪异”的描述：罕见的是情境本身，尤其相对于观察者自身的阶层。", "evidence": "P002", "ambiguity": "“观察者自身的阶层”未定义。"},
    {"term": "本能／预先写好的程序", "meaning": "作者用以说明被逼入墙角后的反应是先天预设、可被强烈刺激触发，而非个人品性或教养问题。", "evidence": "P010", "ambiguity": "“程序”是比喻还是实体主张，本文未说明。"},
    {"term": "双锁定", "meaning": "相互威胁下双方因对方刺激未变而各自锁定在反应模式中，形成彼此维持的对峙。", "evidence": "P014", "ambiguity": "作者自造术语，未给出解除条件。"},
    {"term": "训练", "meaning": "作者以消防员面对火焰的长期训练为唯一被点名的例外途径。", "evidence": "P010", "ambiguity": "训练的种类、时长与迁移性未说明。"}
   ],
   "examples_and_targets": [
    "迪斯尼员工用白雪公主腔说话：类比／归谬例证，用来说明“异常”定性可被反向套用（P004-P005）。",
    "路上遇到响尾蛇而僵住、一步一动：类比，用来说明本能锁定与不改变战术即不改变反应（P012-P013）。",
    "人工智能无人机自主对抗实验中的“对称盘旋”：作者作为经验例证引用，未给出实验来源（P015）。",
    "消防员面对火焰的长期训练：作者作为例外条件举例（P010）。",
    "被反驳对象：把大妈举止定性为“怪异／异常”并自信自己不会如此的观察者（P001、P006-P007）。",
    "反问中的“你”：留过学、读过博士者（P017）。"
   ],
   "conditions": [
    "“罕见”是相对于观察者自身阶层而言的（P002）。",
    "定性“异常”需满足：不同人置于同一情境、大样本量、显著差异（P003）。",
    "例外条件：受过类似消防员面对火焰那样的长期训练；否则只有极小概率是天生的意外（P010）。",
    "双锁定以威胁相互为前提（P014）。",
    "结论限定为“几乎”与教育水平无关（P016）。"
   ],
   "rhetoric_and_tone": "以反问句驱动（P001、P007），第二人称“你”直接对话读者、带诘问与调侃意味；用引号表示对“怪异”“正常”“异常”等定性词的保留态度；“搞不好还更‘可笑’”带轻微反讽。结构为：质疑定性—给判据—归谬—正面解释—两个类比—收束。",
   "unresolved_questions": [
    "提问者所问的“为何滑稽”“人为什么变成这种样子”在正文中未被回答；作者转而处理“怪异”的定性问题。",
    "P015 所述“人工智能无人机自主对抗实验”无出处、无实验条件，属需外部核查的事实性断言。",
    "“观察者自身的阶层”未界定；“大样本量的显著差异”未给统计阈值。",
    "P005 原文作“盖了一个‘正常‘章”，引号形式异常（前半为左引号、后半亦为左引号），疑为原文笔误，已按原文保留。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "为什么可以认定这是“怪异的举止”？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这只是“罕见的举止”", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "尤其是对于观察者自身的阶层而言比较罕见", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "要定性为“怪异”，得要把各种不同的人放到同一个情境里去看反应", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "有很大样本量的显著差异，才能定位这个为“异常”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "否则完全也可以定义迪斯尼的员工为“异常”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "只是因为你把自己代入到迪斯尼员工的角色里的时候你会觉得自己也会一样表现", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "所以你认定她是异常", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P006", "quote": "更多的人干脆只是想象不到自己可能遇到那样的情境，就已经判定大妈为“异常”了", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "问题是，你没有陷入过，你依据什么断言你肯定不一样呢？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "这些大妈们只是在强烈刺激下在按照一种本能在强迫性的做反应。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "这是人类被逼入墙角后的本能，是预先写好的程序。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P010", "quote": "如果你没有受过类似消防员面对火焰那样的长期训练，你只有极小的概率是天生的意外", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P011", "quote": "这个状态下，人所受的教育是不起作用的——你连完整的句子都不会想起来。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P011", "quote": "你只会莫名其妙的被锁定在一个机械模式里", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P012", "quote": "你全部的教育都会飞到九霄云外", "relation": "context"},
    {"key": "E17", "paragraph_id": "P014", "quote": "于是会出现“双锁定”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P014", "quote": "互相都因为对方提供的刺激没变，而被锁定在自己的反应模式之中", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P015", "quote": "这种现象在人工智能无人机的自主对抗实验中也会呈现出来", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P015", "quote": "它们最后几乎总是会陷入一种长时间的“对称盘旋”", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P016", "quote": "这种现象几乎是与教育水平无关的，只是同级别的主体激烈对抗自然会导致的一种现象。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P017", "quote": "不要以为你留了学、读了博士，真遇到这种人生墙角一定会好一些。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P018", "quote": "真不见得，搞不好还更“可笑”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理与行为", "阶层与观察视角", "认知偏见"],
   "issue_candidates": ["如何界定“异常”行为", "旁观者对底层行为的污名化", "本能反应与教育/教养的关系"],
   "text_function_candidates": ["答疑", "论辩", "概念澄清", "说理式反驳"],
   "object_candidates": ["市井大妈", "迪斯尼员工", "观察者（读者/评论者）", "留学者与博士", "人工智能无人机"],
   "working_keywords": ["怪异的举止", "罕见", "异常", "大样本量的显著差异", "被逼入墙角", "预先写好的程序", "双锁定", "对称盘旋"]
  },
  "notes": "本篇无图片节点。提问者用“滑稽”预设，作者未沿用该词，改以“怪异／异常”为讨论对象，归属已分开。P004-P005 的迪斯尼员工为归谬类比。P015 无人机实验为无出处的经验断言，已登记待外部核查。P005 引号形式异常照原文保留。"
 },
 "d8038a0d": {
  "analysis": {
   "question_context": "提问者（Q001，知乎问题）以“台‘海军司令部’证实美国海军陆战队已抵达台湾”为前提，问这对两岸关系意味着什么。作者不讨论该事件本身，而以第一人称“我们”（大陆一方视角）主张：该事件不会改变“以武促统”的既定路线，并给出自设指数 RDE 与“内部时间表／倒计时”的推演。文中立场、战略意图与预测均属作者表述，本记录只作归属登记。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "作者以“应该不会”限定地判断：该事件不改变以武促统的既定路线。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "作者称大陆对台收紧不是对具体事件的对话性反应，而是有内部时间表与战略决心的重心调整；目的是重设台湾民众对海峡局势的心理基线、取消虚妄的安全感。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006"], "summary": "引入自设指数“抵抗时间估计”（RDE），称军事战略目标是把 RDE 压到极限；举例逐年压缩数值；手段含侦查监控、水面平台、导弹、快速反应部队；目标是使“蔡英文无机会从卧室跑到车库”成为无法自欺的现实。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "限定：RDE 建立在“假定美日会第一时间全力介入”的想定之上；并称将靠充分准备抹杀“第一时间”这一概念本身。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "称军事准备到这一步后，即使不做实际攻击，两岸问题也成为台湾居民绕不过去的问题；并以“安眠药普遍无效”形容台湾处境。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "称台湾可能出的牌与美国可能的阻挠都在心理准备之内、可能不影响收网步调；推测可能已订好时间表；否认行动是“看对方是否做蠢事”的反应式安排；无论台湾做蠢事、不做事还是主动示好，军事准备都按原定步调全速推进。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "以朝鲜战场“谈对打没有任何迟滞作用”作历史类比；并称即使下一小时签协议，原定总攻计划也不推迟一分钟。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019"], "summary": "以三句同构排比总结：勾结外人、噤若寒蝉、一见如故三种情形下，攻击准备均照计划展开。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "结论：只有统一完成才能停止倒计时，其他外部动作（含“美海军陆战队访台”）都无影响；作者称这恐怕才是“以武促统”的实际意思。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者判断美海军陆战队抵台“应该不会”改变以武促统的既定路线。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称大陆现在对台湾的收紧，不是对具体事件的对话性反应，而是有内部时间表、有战略决心的重心调整。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称该调整的目的是重新设定台湾民众对基本海峡局势的心理基线、取消虚妄的安全感。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者设定指数“抵抗时间估计”（RDE），称军事战略目标是通过系统计划推进，在尽可能快的时间内把 RDE 压缩到极限。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以“举个例子——假设”给出数值推演：RDE 由 7 天逐年压缩至 3 天、1.5 天、1 天、0.5 天。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称要通过侦查监控、水面平台、导弹、快速反应部队等持续建设，使“蔡英文没有机会从卧室跑到车库”变成台湾人人无法再靠幻想自欺的现实。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者限定 RDE 建立在“假定美日会第一时间全力介入”的想定之上。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称会靠充分准备把“第一时间”这一概念本身直接抹杀——对方与台湾恢复联系时，接电话的已是临时管理机构发言人。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称军事准备做到这一步，即使不做实际攻击，两岸问题也会成为每个台湾居民每天每小时每分钟绕不过去、必须解决的问题。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者以夸张语预测“台湾将变成一个安眠药普遍无效的地区”。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称台湾可能打出的牌与美国可能的阻挠都已在心理准备之内，但这可能对收网计划的步调不产生实质影响。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者推测“我们可能其实订好了时间表”。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认行动是反应式安排：并非看台湾或美国二月干不干蠢事再决定第二步。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称无论台湾干蠢事、什么也不干还是主动示好，军事准备都会按原定步调全速推进（示好时也照样推进）。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以朝鲜战场为历史类比，称“谈对打没有任何迟滞作用”。", "evidence": ["E17"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者称即使下一个小时就要签署协议，原定总攻计划也不会推迟一分钟。", "evidence": ["E18"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以排比列举三种情形（勾结外人、噤若寒蝉、一见如故），均称攻击准备照计划展开。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称只有统一完成才能停止倒计时，除此之外的任何外部动作（含“美海军陆战队访台”）都对倒计时没有影响。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称“这恐怕才是‘以武促统’的实际意思”。", "evidence": ["E25"]}
   ],
   "argument_steps": [
    "先给出结论式判断：该事件应该不改变既定路线（P001）。",
    "重新定义现象：收紧不是对事件的对话性反应，而是有内部时间表的战略重心调整（P002）。",
    "给出目的：重设台湾民众的心理基线、取消虚妄的安全感（P003）。",
    "引入自设指数 RDE 并定义战略目标（P004）。",
    "数值化举例：7 天→3 天→1.5 天→1 天→0.5 天（P005）。",
    "列举手段与目标状态（P006）。",
    "加入想定限定：假定美日第一时间全力介入（P007）。",
    "推演：抹杀“第一时间”概念本身（P008）。",
    "推论一：不攻击也能使问题成为台湾居民绕不过去的日常（P009-P010）。",
    "推论二：对方所有牌与阻挠已在准备之内，步调不受影响；推测已订时间表（P011-P012）。",
    "排除反应式理解（P013）。",
    "以三种台湾反应（挑衅／沉默／示好）说明均按原定步调推进（P014）。",
    "历史类比：朝鲜战场谈判不迟滞打（P015）。",
    "极端假设：签约前一小时也不推迟总攻（P016）。",
    "排比收束三种情形（P017-P019）。",
    "结论：倒计时只有统一完成才停止，事件本身无影响（P020-P022）。",
    "点题：这才是“以武促统”的实际意思（P023）。"
   ],
   "concept_usage": [
    {"term": "以武促统", "meaning": "本文中作者把它解释为：军事准备按内部时间表持续推进、不受外部动作影响的“倒计时”，而非对具体事件的反应。", "evidence": "P023", "ambiguity": "作者用“恐怕才是……实际意思”作限定，未说明这一解释是否为官方口径。"},
    {"term": "抵抗时间估计（RDE，Resistance Duration Estimation）", "meaning": "作者自设的指数，指台湾在军事压力下能够抵抗的时长；被当作可逐年压缩的战略目标。", "evidence": "P004", "ambiguity": "无外部来源、无计算方法；数值为“举个例子——假设”。"},
    {"term": "时间表", "meaning": "作者称收紧背后有“内部时间表”，且可能已订好；节奏由己方决定而非由对方行为触发。", "evidence": "P002", "ambiguity": "“可能”限定；是否存在、由谁制定本文未说明。"},
    {"term": "心理基线", "meaning": "台湾民众对海峡基本局势的默认预期；作者称要重新设定并取消“虚妄的安全感”。", "evidence": "P003", "ambiguity": "无衡量方式。"},
    {"term": "第一时间", "meaning": "指美日介入的时间窗口；作者称要靠准备使这一概念本身失去意义。", "evidence": "P008", "ambiguity": "抹杀的具体机制未说明。"},
    {"term": "收网", "meaning": "作者对自己一方行动计划的比喻性称法（“收网计划”）。", "evidence": "P011", "ambiguity": "比喻，未给出具体内容。"}
   ],
   "examples_and_targets": [
    "美海军陆战队访台／抵台：提问者引述的触发事件，亦被作者列为“无影响”的外部动作（P001、P022）。",
    "蔡英文“没有机会从卧室跑到车库”：作者用作目标状态的形象化表述（P006）。",
    "朝鲜战场“谈对打没有任何迟滞作用”：作者使用的历史类比（P015），无具体史料出处。",
    "“假定美日会第一时间全力介入”：作者明确标出的想定前提（P007）。",
    "“茶话会上激动的握手，热情的寒暄”：示好情景的修辞性描写（P014）。",
    "台湾民众／台湾居民：被论述的对象（P003、P009）。",
    "“临时管理机构发言人”：作者设想的接管情景（P008）。"
   ],
   "conditions": [
    "开篇判断以“应该不会”限定（P001）。",
    "RDE 数值为假设性举例（“举个例子——假设”）（P005）。",
    "RDE 以“假定美日会第一时间全力介入”为前提（P007）。",
    "“这期间”“可能”对台湾牌与美国阻挠的影响作限定（P011）。",
    "时间表是否已订以“可能其实”表述（P012）。",
    "“恐怕”限定对“以武促统”实际意思的归纳（P023）。",
    "停止倒计时的唯一条件被设为统一完成（P020）。"
   ],
   "rhetoric_and_tone": "第一人称复数“我们”自居大陆一方、第二人称“你们”指对方，语气为笃定的战略推演兼劝谕；大量排比与反复（“不断的……不断的……”“勾结外人……噤若寒蝉……一见如故……”）；口语化短句与口号式收束（“只有统一完成，才能停止倒计时”）；“安眠药普遍无效”“从卧室跑到车库”为夸张、形象化修辞；全篇未见对提问事件的细节讨论。",
   "unresolved_questions": [
    "提问者所述“台‘海军司令部’证实美国海军陆战队已抵达台湾”的事实与消息来源需外部核查；本文以该前提为背景直接推演，未核实。",
    "RDE 的数值与“内部时间表”均无外部依据，属作者自设与推测（文中以“假设”“可能”“恐怕”限定）。",
    "作者未说明文中战略意图是官方政策的转述、个人解读还是主张，也未标注信息来源。",
    "P011 原文“但这可能对连对我们收网计划的步调不会产生任何实质的影响”有衍字（“对连对”），语句不通，按原文保留，语义存在歧义。",
    "“临时管理机构”的设想未说明依据与时点。",
    "P015 朝鲜战场判断属历史性断言，无史料出处，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这应该不会改变以武促统的既定路线。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不是对台湾具体事件的对话性的反应，而是一种有内部时间表的、有战略决心的重心调整。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "是要重新设定台湾民众对基本海峡局势的心理基线，取消虚妄的安全感。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "我们设定一个指数“抵抗时间估计”（Resistance Duration Estimation，RDE）。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "将RDE从现在的数值压缩到极限", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "举个例子——假设现在RDE是7天，一年后我们要压到3天", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "变成一个台湾每一个人都无法再靠幻想来自欺欺人的现实", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "并且这个RDE是建立在“假定美日会第一时间全力介入”的想定之上的。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P008", "quote": "我们会靠着充分的准备把“第一时间”这个概念本身直接抹杀", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "接电话的已经是临时管理机构发言人", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "两岸关系问题也变成每一个台湾居民每天、每小时、每分钟都绕不过去的、必须要解决的问题。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "台湾将变成一个安眠药普遍无效的地区。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "都已经在心理准备之内", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P012", "quote": "也就是说，我们可能其实订好了时间表。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "并不是一月做了，看看二月台湾或者美国干不干蠢事", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P014", "quote": "但军事准备还是会按照原定步调全速推进。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P015", "quote": "犹如当年朝鲜战场上一样——谈对打没有任何迟滞作用。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "就算是下一个小时就要签署协议，原定总攻计划也不会推迟一分钟。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P017", "quote": "勾结外人、制造事端，攻击准备照计划展开；", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P018", "quote": "噤若寒蝉、避而不谈，攻击准备照计划展开；", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P019", "quote": "一见如故、谈笑风生，攻击准备照计划展开。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P020", "quote": "只有统一完成，才能停止倒计时。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P021", "quote": "除此之外的任何外部动作，都对这倒计时没有影响。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P022", "quote": "包括“美海军陆战队访台”。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P023", "quote": "这恐怕才是“以武促统”的实际意思。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["两岸关系", "军事战略", "政治推演"],
   "issue_candidates": ["美海军陆战队抵台事件的意义", "以武促统路线的解释", "军事准备与谈判的关系"],
   "text_function_candidates": ["时政评论", "战略推演", "答问"],
   "object_candidates": ["台湾", "大陆", "美国", "日本", "蔡英文", "台湾民众", "美海军陆战队"],
   "working_keywords": ["以武促统", "抵抗时间估计", "RDE", "心理基线", "第一时间", "收网计划", "倒计时", "美海军陆战队访台"]
  },
  "notes": "本篇无图片节点。全文以第一人称“我们”（大陆一方）推演，立场、意图与预测均属作者表述，本记录仅作归属登记，不作评价。RDE 为作者自设指数（无出处），P005 数值明确标为假设举例；P012、P023 以“可能”“恐怕”限定。P011 原文“对连对我们”疑为衍字，照原文保留并在未决问题登记。提问事件的真实性未核实。"
 },
 "2cafa14d": {
  "analysis": {
   "question_context": "提问者（Q001，知乎问题）就辉瑞宣布疫苗对90%新冠病毒有效、资本市场巨幅波动，问这是否是操纵市场、是否会成为第一个上市新冠疫苗。作者未回答这两个问题，也未讨论资本市场，而是转向“下一场传染病”的警告：主张人类进入历史性传染病高发期，真正应对只能靠公共卫生制度与对第三世界的援助，并提醒投资人想清楚。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以“恕我直言”开头提出：下一场传染病可能比想象的更近，新冠不会是最后一幕。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "理由：气候变化与大规模经济活动造成生态改变幅度太大，无数物种承受很大选择压力；该压力催生新的食谱、迁徙路线、栖居地、行为模式与接触人类的点位和路径，意味着新的变异与新的接触。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "推论：人类作为总体进入历史性的传染病高发期，COVID-19 只是第一章。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "以标题句要求所有人随时准备第二种新传染病出现的可能。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "应对主张：真正应对不是医疗技术的事后抵抗，而只能靠强有力公共卫生制度与对穷国弱国的卫生援助；更进一步说“援助”不解决问题，要帮第三世界建立有效运转的自我治理体系与真正有效的国际合作机制；玩不得虚假。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "反证：否则下一场传染病可能从尼日利亚、巴西、印尼、孟加拉、印度悄无声息爆发并被漏过；被真正认识到时封堵已无意义。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "反事实比较：这次从中国这种有冠绝全球反应能力的国家爆发已是老天爷格外仁慈；若在印度爆发，等其认识到死者并非死于感冒时，其他国家恐怕已无幸免。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016"], "summary": "连续反问：下一次有什么真凭实据保证剧本不是这样？如果是，拿什么挡？", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P017"], "summary": "限定疫苗的作用：辉瑞、强生、科兴最多让人类对目前的新冠免疫，远不能让人类社会对传染病本身免疫。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P018", "P019", "P020"], "summary": "假设设问：若明天出现新的不明传染病且已有类似患者，世界将会怎样？并建议投资人想清楚。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者判断下一场传染病离人类可能比想象的更近。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认新冠肺炎是这场戏的最后一幕。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称全球气候变化与大规模经济活动引发的生态改变幅度太大，无数物种正承受非常大的选择压力。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称这种选择压力会催生新的食谱、新的迁徙路线、新的栖居地、新的行为模式、新的与人类社会接触的点位和路径。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称上述变化意味着新的变异和新的接触。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者判断人类作为一个总体已进入历史性的传染病高发期，COVID-19 只是这个故事的第一章。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张所有人都应该随时做好出现第二种新传染病的可能。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称真正的应对不是依靠医疗技术的事后抵抗，而只能依靠强有力的公共卫生制度以及对穷国、弱国卫生体系的大力援助。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者进一步称“援助”其实不解决问题，要真正帮助整个第三世界建立有效运转的自我治理体系以及真正有效的国际合作机制。", "evidence": ["E9", "E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“玩不得虚假”强调上述应对不可敷衍。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者警告若不这样做，下一场横扫人类的传染病随时可能从尼日利亚、巴西、印尼、孟加拉、印度悄无声息爆发，并被这些国家效率堪忧的预防体系漏过。", "evidence": ["E12", "E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称当疫病被真正认识到存在时，封堵已无意义。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这次疫情从中国这种有冠绝全球反应能力的国家开始爆发，已是老天爷对人类格外仁慈。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者假设若在印度爆发，当印度认识到本季度死掉的几千人不是死于感冒时，世界其他国家恐怕已经没有幸免的。", "evidence": ["E16", "E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：下一次有什么真凭实据能保证剧本不是这样；如果是，拿什么挡。", "evidence": ["E18", "E19"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者称辉瑞、强生、科兴等最多只能让人类对目前的新冠免疫，远远不能让人类社会对传染病本身免疫。", "evidence": ["E20"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以“如果明天上帝跟人类开一个新玩笑”的假设设问：在 xx 地区发现新的不明传染病、且 xx、xxx 已发现类似患者时，世界将会怎样。", "evidence": ["E21", "E22"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是个很有趣的问题，建议各位投资人想想清楚。", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "以警示句开篇：下一场传染病可能更近（P001）。",
    "否定终局感：新冠不是最后一幕（P002）。",
    "给出生态学理由：气候变化与经济活动造成巨大选择压力（P003）。",
    "列出选择压力导致的接触面变化（P004-P005）。",
    "推出结论：人类进入历史性传染病高发期（P006）。",
    "给出准备要求（标题句）（P007）。",
    "提出应对主张：非技术事后抵抗，而是公共卫生制度＋对穷国弱国援助（P008）。",
    "加码：援助不足以解决问题，需帮助建立自我治理体系与国际合作机制（P009）。",
    "强调不可虚假（P010）。",
    "反证：否则新疫病将从多国漏过，发现时封堵已无意义（P011-P012）。",
    "反事实比较：此次起于中国已属幸运，若起于印度则全球难幸免（P013-P014）。",
    "连续反问施压（P015-P016）。",
    "限定疫苗作用边界：只能对当前新冠免疫（P017）。",
    "以新疫病假设设问，收束到对投资人的提醒（P018-P020）。"
   ],
   "concept_usage": [
    {"term": "选择压力", "meaning": "生态改变施加于物种的适应压力；作者称其催生新的接触路径与变异。", "evidence": "P003", "ambiguity": "作者由生态学概念直接推到公共卫生结论，中间环节未详述。"},
    {"term": "历史性的传染病的高发期", "meaning": "作者对人类总体所处阶段的判断，以 COVID-19 为“第一章”。", "evidence": "P006", "ambiguity": "未给时间范围与衡量标准。"},
    {"term": "事后抵抗", "meaning": "作者用以指称依靠医疗技术的应对方式，并否定其为真正应对。", "evidence": "P008", "ambiguity": "“医疗技术”与“公共卫生制度”的边界未界定。"},
    {"term": "援助", "meaning": "对穷国、弱国卫生体系的援助；作者称其“其实是不解决问题的”，主张升级为帮助建立自我治理体系。", "evidence": "P009", "ambiguity": "作者先说“大力援助”，随后又说援助不解决问题，前后存在张力。"},
    {"term": "对传染病本身免疫", "meaning": "作者用来对照“对目前新冠免疫”，指人类社会整体不再受新发传染病威胁的状态。", "evidence": "P017", "ambiguity": "该状态是否可能实现，作者未说明。"}
   ],
   "examples_and_targets": [
    "辉瑞、强生、科兴：疫苗企业，作者用作疫苗效力边界的例证（P017），未评价其股价或市场行为。",
    "尼日利亚、巴西、印尼、孟加拉、印度：作者点名的可能爆发地与预防体系薄弱对象（P011）。",
    "印度“本季度死掉的那几千人”：反事实假设中的说法，无数据出处（P014）。",
    "中国“有冠绝全球的反应能力”：作者作为比较项的判断（P013）。",
    "“xx地区”“xx、xxx”：原文占位符，未填具体地名（P018）。",
    "“上帝跟人类开一个新玩笑”“老天爷对人类格外仁慈”：拟人化修辞（P013、P018）。",
    "各位投资人：文末劝告对象（P020）。"
   ],
   "conditions": [
    "核心判断以“可能比想象的更近”限定（P001）。",
    "警告以“随时可能”表述（P011）。",
    "印度情景以“如果在印度爆发”假设前提（P014）。",
    "疫苗效力以“最多只能”限定（P017）。",
    "新疫病情景以“如果明天上帝跟人类开一个新玩笑”假设（P018）。",
    "“或者更进一步的说”标示论述加码（P009）。"
   ],
   "rhetoric_and_tone": "开篇“恕我直言”定调为直言告诫；多用警句与独段短句（P002、P005、P010）；连续反问施压（P015-P016、P019）；以“老天爷”“上帝开新玩笑”拟人化并带反讽意味；通篇为面向公众的呼吁，末句转为对投资人的具体劝告。",
   "unresolved_questions": [
    "提问者所问“资本市场巨幅波动是否为操纵市场”“是否会成为第一个上市的新冠疫苗”在正文中完全未被回答，亦未提及资本市场，属答非所问。",
    "P018 中“xx地区”“xx、xxx”为原文占位符，未填具体地名，所指不明，照原文保留。",
    "“有冠绝全球的反应能力”“效率堪忧的预防体系”为作者判断，无数据或来源，需外部核查。",
    "“本季度死掉的那几千人”无数据出处，需外部核查。",
    "“历史性的传染病的高发期”未给出时间范围、判定标准与依据。",
    "P008 主张“大力援助”与 P009 称“援助其实是不解决问题的”之间的张力，作者以“更进一步的说”带过，未说明二者如何兼容。",
    "文中未说明作者身份与其公共卫生专业背景，论断依据不明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "恕我直言，下一场传染病离人类可能比想象的更近。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "新冠肺炎并不会是这场戏的最后一幕。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "全球气候变化与大规模经济活动引发的生态改变幅度太大，有无数的物种在承受非常大的选择压力。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这种选择压力会催生出新的食谱、新的迁徙路线、新的栖居地、新的行为模式、新的与人类社会接触的点位和路径。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "意味着新的变异和新的接触。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这意味着人类作为一个总体进入了一个历史性的传染病的高发期，COVID-19只是这个故事的第一章而已。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "所有人都应该随时做好出现第二种新传染病的可能。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "真正的应对，不是依靠医疗技术的事后抵抗，而只能依靠强有力的公共卫生制度，以及对穷国、弱国的卫生体系的大力援助。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "“援助”其实是不解决问题的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "是要真正的帮助整个第三世界建立真正有效运转的自我治理体系，以及真正有效的国际合作机制。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "玩不得虚假。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "否则，下一场横扫人类的传染病随时可能从尼日利亚、巴西、印尼、孟加拉、印度悄无声息的爆发", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "并被这些国家效率堪忧的预防体系漏过", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "当被真正认识到存在时，封堵已无意义。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "实在已经是老天爷对人类格外仁慈", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P014", "quote": "如果在印度爆发，当印度真正认识到本季度死掉的那几千人不是死于感冒时", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "世界的其他国家恐怕已经没有幸免的了", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P015", "quote": "下一次，有什么真凭实据能保证剧本不是这样呢？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "如果是，拿什么挡？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P017", "quote": "辉瑞、强生、科兴们，最多只能让人类对目前的新冠免疫，远远不能让人类社会对于传染病本身免疫。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P018", "quote": "如果明天上帝跟人类开一个新玩笑——在xx地区发现了新的不明传染病，且在xx、xxx已经发现了类似患者……", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P019", "quote": "世界将会怎样？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P020", "quote": "这是个很有趣的问题，建议各位投资人想想清楚。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["公共卫生", "传染病防治", "生态与环境", "国际援助"],
   "issue_candidates": ["下一场大流行的可能性", "疫苗作用的边界", "穷国卫生体系与国际合作", "生态改变与人畜共患病风险"],
   "text_function_candidates": ["答疑（实为转向式评论）", "预警", "政策主张", "答问"],
   "object_candidates": ["辉瑞", "强生", "科兴", "中国", "印度", "尼日利亚", "巴西", "印尼", "孟加拉", "第三世界", "投资人"],
   "working_keywords": ["下一场传染病", "选择压力", "传染病的高发期", "事后抵抗", "公共卫生制度", "自我治理体系", "国际合作机制", "对传染病本身免疫"]
  },
  "notes": "本篇无图片节点。提问问的是资本市场是否被操纵与首个上市疫苗，作者均未回答，正文转向下一场传染病的预警与公共卫生主张，属明显答非所问，已在未决问题登记。P018 的“xx地区”“xx、xxx”为原文占位符照录。P013-P014 涉及国家间比较与“几千人”数据，均无出处，需外部核查。P007 在 lexical 中为 heading，其余为正文段落。"
 },
 "a81e9f31": {
  "analysis": {
   "question_context": "提问者（Q001，知乎问题）问“德不配位该如何自处”。作者未使用“德不配位”一词，也未讨论“位”与“德”的匹配问题，而把处境重新表述为“陷入力所不能及的工作、面对没把握的新问题”与随之而来的自我怀疑（“怀疑自己是个骗子”），并给出劝慰式建议：安心做事、把煎熬当锻炼。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以格言式全称断言开篇：每一位英雄都会在内心怀疑自己是个骗子，且每天如此。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "普遍化说明：每个人都或迟或早会陷入力所不能及的工作、面对没把握的新问题，不是只有你这样。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006"], "summary": "行动建议：不要多想、安心做事；认真做并确保每次都有心得，包括忍受折磨的心得。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "限定性理由：有时取胜并非因过人之处，只是同样压力下对手失眠更厉害、更早崩溃。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "价值判断：聪明的人没有勇敢的人宝贵；勇敢的最大表现是淡定；并以反问说明镇定只能在没把握的事情中习得。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013"], "summary": "理由与后果：最好在四十岁前受过这种锻炼，因为此后父母身体、子女成长不确定、中年失业、健康问题人人难逃；若向来只做有把握的事，心便没有老茧，届时这些事都是 A 级难题；未磨过的心用最粗砂纸磨才叫撕心裂肺。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P014"], "summary": "以“终逃不过那一日”“没有第二条退路”强调处境不可回避。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016", "P017"], "summary": "结论与劝告：放下焦虑怀疑，把煎熬当作“健心”的酸痛；以力竭时肌肉之痛反问；把痛苦练出快感。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言每一位英雄都会在内心怀疑自己是个骗子，且每天如此。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称每个人都或迟或早会陷入自己力所不能及的工作、面对没把握的新问题，并非只有你如此。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议不要多想、安心做事。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议认真做，确保每次都有一些心得，包括如何忍受这种折磨的心得。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称有的时候取胜不是因为有任何过人之处，只是因为同样的压力下对手失眠更厉害、更早崩溃。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这个世界上聪明的人没有勇敢的人宝贵。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称勇敢最大的表现不是亢奋地往前冲，而是淡定。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问主张：镇定除了能在没有把握的事情中学习，别无学习途径。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者建议最好在四十岁之前受过这种充分的锻炼。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称随后父母的身体、子女成长过程中的不确定、中年失业的风险、身体健康问题是人人难以逃过的。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者设想的后果：若回头发现向来只做过有把握的事，心就没有那层老茧；没有茧垫着，上述事情都是 A 级难题，远非平时工作生意中的问题可比。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以比喻称：从来没磨过的心，用最粗的砂纸磨，那才叫撕心裂肺。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称到头来这一身终逃不过那一日，世界上根本没有第二条退路可走。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者据此劝告：放下自己的焦虑怀疑，把这种煎熬当作“健心”的酸痛。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问渲染：力竭之时肌肉有多痛、多想撒手。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称把这种痛苦练出快感来，你就爽了。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "以英雄亦自我怀疑的格言定调（P001-P002）。",
    "普遍化：人人都会遇到力所不能及之事，并非你独有（P003）。",
    "给出行动建议：少想、做事、积累心得（含忍受折磨的心得）（P004-P006）。",
    "降低胜负的自我归因压力：有时只是对手先崩溃（P007）。",
    "价值排序：勇敢贵于聪明，勇敢即淡定（P008-P009）。",
    "以反问确立“在没把握的事情中学习”的正当性（P010）。",
    "加入时间条件：宜在四十岁前受锻炼（P011）。",
    "列举中年阶段难以逃过的难题作为理由（P011）。",
    "反面推演：只做有把握之事者将缺乏心理老茧，届时难题成为 A 级（P012）。",
    "以砂纸磨心作喻（P013）。",
    "以“没有第二条退路”收束必然性（P014）。",
    "结论式劝告：把煎熬当“健心”酸痛，练出快感（P015-P017）。"
   ],
   "concept_usage": [
    {"term": "德不配位", "meaning": "正文未出现该词，作者未定义或使用；作者以“力所不能及的工作”“没把握的新问题”“怀疑自己是个骗子”指称提问所指的处境。", "evidence": "P003", "ambiguity": "提问者用语与作者用语不一致，作者未做术语对接。"},
    {"term": "英雄／骗子", "meaning": "作者用“英雄”称呼承担重任者，用“怀疑自己是个骗子”描述其自我怀疑；未作定义。", "evidence": "P001", "ambiguity": "全称断言，无经验依据，是否含夸张未说明。"},
    {"term": "勇敢／淡定", "meaning": "作者把勇敢重新定义为淡定，而非亢奋前冲。", "evidence": "P009", "ambiguity": "“淡定”未作界定。"},
    {"term": "老茧／磨／砂纸", "meaning": "心理承受力的比喻：老茧指在没把握之事中练出的耐受层，砂纸指压力的粗粝程度。", "evidence": "P012", "ambiguity": "比喻未给出可操作含义。"},
    {"term": "A级难题", "meaning": "作者用以指中年阶段那些难题的量级，高于平时工作生意中的问题。", "evidence": "P012", "ambiguity": "分级标准未定义。"},
    {"term": "健心的酸痛", "meaning": "把心理煎熬类比为健身后的肌肉酸痛，据此劝人接受煎熬。", "evidence": "P015", "ambiguity": "类比未说明限度。"}
   ],
   "examples_and_targets": [
    "英雄：泛称，作者修辞与劝慰对象（P001）。",
    "对手比你失眠更厉害、更早崩溃：竞争情景的举例（P007）。",
    "四十岁之前：作者给出的锻炼时间窗（P011）。",
    "父母的身体、子女成长过程中的不确定、中年失业的风险、身体健康的问题：作者列举的中年难题（P011）。",
    "最粗的砂纸磨心：比喻材料（P013）。",
    "力竭之时的肌肉之痛：身体化类比与反问（P016）。",
    "提问者所问“德不配位”：正文未出现该词，提问框架未被作者采用。"
   ],
   "conditions": [
    "“或迟或早”标示时间上的不确定性（P003）。",
    "胜负归因以“有的时候”限定（P007）。",
    "锻炼时点以“最好在四十岁之前”表述（P011）。",
    "心无老茧的后果以“如果回头发现”假设引出（P012）。",
    "结尾劝告以反问与类比承载，未给操作步骤（P016-P017）。"
   ],
   "rhetoric_and_tone": "格言体与劝慰训诫混合：独段短句（“每天。”）、全称断言、第二人称“你”直接对话；反问句（P010、P016）承担说理；身体化比喻（老茧、砂纸、肌肉酸痛、健心）；结尾“把这种痛苦练出快感来，你就爽了”转为口语调侃。整体语气温和而带有强推的激励色彩。",
   "unresolved_questions": [
    "正文未出现“德不配位”一词，作者也未定义该词；提问术语与作者论述之间缺少明确对接。",
    "“每一位英雄都会在内心怀疑自己是个骗子”为全称断言，无经验依据或来源，是否属夸张修辞本文未说明。",
    "“四十岁之前”这一时点无依据说明。",
    "“A级难题”的分级标准未定义。",
    "“世界上根本没有第二条退路可走”“终逃不过那一日”所指的具体内容（是否指死亡或其他）本文未明说。",
    "作者身份、写作语境及是否针对该提问作答，正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "每一位英雄，都会在内心怀疑自己是个骗子。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "每天。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "每个人都或迟或早会陷入自己力所不能及的工作，面对着自己没把握的新问题。不是只有你这样，大家都这样。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "不要多想，安心做事。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "认真做，确保每次都有一些心得。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "包括如何忍受这种折磨的心得。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "只是因为同样的压力下，你的对手比你失眠更厉害，更早崩溃。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P008", "quote": "这个世界上，聪明的人没有勇敢的人宝贵。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "而勇敢最大的表现不是亢奋的往前冲，而是淡定。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "镇定除了能在没有把握的事情中学习，还能怎么学习呢？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "事实上，你最好在四十岁之前受过这种充分的锻炼。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "因为随后父母的身体、子女成长过程中的不确定、中年失业的风险、身体健康的问题，是人人难以逃过的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "到时候你如果回头发现你向来只做过有把握的事，你的心就没有那层老茧。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "上面说的这些事其实可都是A级难题", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "从来没磨过的心，用最粗的砂纸磨，那才叫撕心裂肺。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P014", "quote": "其实世界上根本没有第二条退路可走。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P015", "quote": "所以，放下自己的焦虑怀疑，把这种煎熬当作“健心”的酸痛。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "力竭之时你的肌肉有多痛，多想撒手？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P017", "quote": "把这种痛苦练出快感来，你就爽了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理调适", "职业与人生经验", "励志劝慰"],
   "issue_candidates": ["自我怀疑（冒充者感）", "力所不能及的工作如何自处", "中年压力的提前准备"],
   "text_function_candidates": ["答疑", "劝慰", "经验总结", "训诫"],
   "object_candidates": ["提问者", "英雄", "对手", "父母", "子女", "中年人"],
   "working_keywords": ["德不配位", "怀疑自己是个骗子", "力所不能及", "没把握的新问题", "勇敢", "淡定", "老茧", "A级难题", "健心的酸痛"]
  },
  "notes": "本篇无图片节点。正文未使用提问中的“德不配位”，作者以“力所不能及的工作／没把握的新问题／怀疑自己是个骗子”重构处境，已在 concept_usage 与未决问题登记。P001、P014 为格言式全称断言，未给依据；P007 以“有的时候”限定；P012 以“如果”假设。"
 },
 "22f68966": {
  "analysis": {
   "question_context": "提问者（Q001，知乎问题）问中日韩等 15 国正式签署 RCEP 会对亚太及全球经济产生哪些影响。作者未作经济影响分析，而以“第一、第二、第三”三点短评给出评价：以协商谈判达成共同利益值得庆贺、是日本侵略战争“真正的结束音”、只是万里长征第一步需有反复的心理准备、且不应被视为“反美斗争”的胜利。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "第一点：枪炮刀剑做不到的事靠协商谈判与协调共同利益做到了，可喜可贺；作者称这才是日本侵略战争真正的结束音。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "第二点：不可低估协议意义，但这只是万里长征第一步，应对未来的曲折、波动和反复有充分心理准备（以“行百里者半九十”作结）。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "第三点：作者不认为这应被视为“反美斗争”的胜利；称没有“反美”战略目标；该协议是各国人民追求最大繁荣的共同合作，美国优势被削弱是客观结果而非目的。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P008"], "summary": "总评：这是一件好事，可喜可贺。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称枪炮刀剑做不到的事情，靠着协商谈判、协调共同利益做到了，值得庆贺。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以自己的判断称：这才是日本侵略战争真正的结束音。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称不可低估该协议的意义，但也要看到这只是万里长征第一步，要对未来的曲折、波动和反复有充分心理准备。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者引用成语“行百里者半九十”为上述长期性判断作结（未注明出处）。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不认为该协议应被视为“反美斗争”的胜利。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称严格地说“我们没有‘反美’这个战略目标”。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这只是世界各国人民追求最大繁荣的共同合作；美国压倒性优势客观上被削弱，但不是为“削弱美国”而做的事。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总评：这是一件好事，可喜可贺。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "第一点：把协议定性为协商谈判、协调共同利益的成就（P001）。",
    "以历史意义加码：称其为日本侵略战争真正的结束音（P002）。",
    "第二点：先让步（不可低估意义），再转折限定为万里长征第一步（P003）。",
    "引成语强化长期性（P004）。",
    "第三点：否认“反美斗争胜利”的解读（P005）。",
    "以“严格地说”否认存在“反美”战略目标（P006）。",
    "给出正面定性：共同繁荣的合作，削弱美国优势只是客观结果而非目的（P007）。",
    "总评收束：好事，可喜可贺（P008）。"
   ],
   "concept_usage": [
    {"term": "RCEP", "meaning": "正文未出现该缩写或全称，作者仅以“这一协议”“这件事”指称；未涉及任何条款或经济影响内容。", "evidence": "P003", "ambiguity": "标题为“RCEP”但正文未使用该词，标题与正文用语不一致。"},
    {"term": "反美斗争／反美", "meaning": "作者用以指称他所否认的一种解读框架，并明确称不存在“反美”这一战略目标。", "evidence": "P005", "ambiguity": "“我们”指谁（国家、政府或一般立场）未说明。"},
    {"term": "日本侵略战争真正的结束音", "meaning": "作者对该协议历史意义的定性，指以协商合作方式完成枪炮未能完成之事。", "evidence": "P002", "ambiguity": "判断依据与“结束音”的具体所指未说明。"},
    {"term": "万里长征第一步／行百里者半九十", "meaning": "作者用长征与成语比喻该协议只是长期进程的开端，后续会有曲折、波动和反复。", "evidence": "P003", "ambiguity": "未说明“曲折、波动和反复”具体指什么。"},
    {"term": "最大繁荣", "meaning": "作者称各国人民追求的目标，是合作的动因。", "evidence": "P007", "ambiguity": "未界定其衡量方式。"}
   ],
   "examples_and_targets": [
    "中日韩等 15 国签署 RCEP：提问者提供的事件背景，正文以“这一协议”指称（P003）。",
    "日本侵略战争：历史叙述，被作者称为因该协议而真正结束（P002），无史料依据说明。",
    "美国：作者称其压倒性优势客观上被削弱，但否认以此为目的（P007），属作者的解读对象。",
    "“枪炮刀剑”：与协商谈判相对照的修辞材料（P001）。",
    "“万里长征”“行百里者半九十”：成语与典故引用，用作长期性与反复性的论据（P003-P004）。",
    "被反驳对象：把该协议视为“反美斗争”胜利的解读（P005）。"
   ],
   "conditions": [
    "第二点以“当然不可低估……但也要看到”构成让步—转折（P003）。",
    "第三点以“严格地说”限定表述（P006）。",
    "美国优势被削弱以“客观上”限定为结果而非目标（P007）。",
    "三点判断均以“第一/第二/第三”编号，未展开条件分析。"
   ],
   "rhetoric_and_tone": "条目式短评，语气明快祝贺（“可喜可贺”首尾呼应）；用“在我看来”“我不认为”明确标注作者判断；“行百里者半九十”引成语作结；“不要搞错重点”带训诫口吻；第一人称复数“我们”自居一方立场。全篇为评价性短论，不含数据与推演。",
   "unresolved_questions": [
    "提问所问“对亚太及全球经济产生哪些影响”未获实质回答：正文没有任何经济影响、贸易或产业层面的分析。",
    "正文未出现“RCEP”字样（仅称“这一协议”），标题与正文用语不一致。",
    "“这才是日本侵略战争真正的结束音”为历史判断，未给论证依据，其史观依据需外部核查。",
    "“万里长征第一步”“曲折、波动和反复”具体所指未说明。",
    "“我们没有‘反美’这个战略目标”中的“我们”指谁（政府、国家或作者自居的立场）未说明。",
    "三点评价均无数据或文件依据，属作者个人评论。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "第一，枪炮刀剑做不到的事情，靠着协商谈判、协调共同利益做到了，可喜可贺。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "在我看来，这才是日本侵略战争真正的结束音。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "当然不可低估这一协议的意义，但也要看到这只是万里长征第一步", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P003", "quote": "要对这件事未来的曲折、波动和反复有充分的心理准备", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "行百里者半九十。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "第三，我不认为这应该被视为“反美斗争”的胜利。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "严格地说，我们没有“反美”这个战略目标。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "这只是世界各国人民追求最大繁荣的共同合作。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "大家繁荣了，于是美国的压倒性优势客观上被削弱了，但这不是为了“削弱美国”而做的事，不要搞错重点。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "总之，这是一件好事，可喜可贺。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际经济与贸易", "区域合作", "中日关系", "中美关系"],
   "issue_candidates": ["RCEP 的意义评价", "该协议是否应视为反美胜利", "区域合作的长期性"],
   "text_function_candidates": ["短评", "答问", "表态"],
   "object_candidates": ["中日韩等15国", "日本", "美国", "RCEP"],
   "working_keywords": ["RCEP", "协商谈判", "协调共同利益", "日本侵略战争", "万里长征第一步", "行百里者半九十", "反美斗争", "最大繁荣"]
  },
  "notes": "本篇无图片节点。正文未出现“RCEP”字样，仅以“这一协议”“这件事”指称；提问所问的经济影响未获回答，已在未决问题登记。P002 的历史判断与 P006-P007 的立场表述（“我们”）均无依据说明或主体界定，全部归属作者。引用成语“行百里者半九十”未注明出处。"
 },
 "e7c70f42": {
  "analysis": {
   "question_context": "提问者（Q001，知乎问题）问如何界定虚伪、以及为什么人们普遍讨厌虚伪。作者集中处理“如何界定”：先复述并反驳一种流行判据（要件 A＋B），指出它会把“虚伪”概念绝对化乃至虚无化，再补出要件 C 给出自己的三条判据，继而追问放宽到三条仍不足的情形，最后以“明知必有虚伪的罪，为什么还要主张美德”的追问收束。对“为什么人们普遍讨厌虚伪”未直接作答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "复述被审视的流行判据：要件 A（主张或赞同某道德原则）＋要件 B（事实证明或自认触犯该原则），二者同时满足即构成“虚伪”。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006"], "summary": "作者先设问“这听起来很对，对吗”，随即反驳：该判据会把“虚伪”概念绝对化，乃至在事实上虚无化。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "以“诚实”检验：假设诚实意味着“言实相符”，则人类根本没有任何一个人有诚实的能力。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "以“公平”检验：自称公平者只有一种可能——根本不公平且不知道自己不公平或不承认；因为人类根本没有公平的能力。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P015"], "summary": "推论：按 A＋B，“虚伪”成为无意义的“控诉”，如控诉老虎吃肉、指责马儿要跑又要吃草。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "作者补出要件 C（自认违背该原则却自称无罪）并重述三条，主张三条同时满足才成其为虚伪。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "理由与后果：主张原则而自己没做到尚不构成虚伪判定（人无法完美遵从任何美德）；若据此立“虚伪罪”，反而奖励主张“人就应该骗人”的人，因为ta们“不虚伪”。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028"], "summary": "以“你去专门征集一群、去ta们中间生活呀”“你为啥不去”的诘问施压。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P029", "P030"], "summary": "标题句：真正虚伪的恰恰是只取 A＋B、而又认为【自己】不虚伪的人；作者称这只能借无知而暂免。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036"], "summary": "转折：即使放宽到三条仍不足——一认再认而又一犯再犯时，“一认再认”能否免除虚伪性？作者称这才是对每个成年人致命的问题。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P037", "P038", "P039", "P040"], "summary": "以归谬式追问展开：既然虚伪无路可逃，何妨索性不认、不主张“大道理”，做“真小人”，从而“从三重虚伪的无间地狱中解脱”。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P041", "P042"], "summary": "结尾两个追问：为什么宁可选择永恒的（道德）折磨、给人指责你虚伪的立场，仍要主张那些美德；明知必有虚伪的罪，为什么还要主张。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者审视并反驳的流行判据（作者称持此标准者为“很多小孩子”）：要件 A＋要件 B 同时满足即构成“虚伪”。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者反驳该判据：这实际上会把“虚伪”概念绝对化，乃至于在事实上虚无化。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以假设检验：假如诚实意味着“言实相符”，人类根本就没有任何一个人有诚实的能力。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称自称公平者只有一种可能：根本不公平，且连自己有多不公平都不知道或不承认；因为人类根本没有公平的能力。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者推论：按 A＋B，“虚伪”就直接成了无意义的“控诉”，如同控诉老虎要吃肉、指责马儿要跑又要吃草。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出自己的判据：虚伪还差一条——要件 C（在该人自己也承认 A、B 皆满足的前提下，该人自认为无罪）；三条同时满足，才成其为虚伪。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称主张原则而自己没做到，到此为止还不构成虚伪判定，因为人类根本做不到完美遵从任何美德。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称若据此立起“虚伪罪”，等于大力奖励主张“人就应该骗人，越会骗人越有本事”的人，因为ta们反倒“不虚伪”。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张：真正虚伪的，恰恰是只取 A＋B，而又认为【自己】不虚伪的人；这只能借无知而暂免。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：即使把条件放宽到三条仍不足——若一认再认而又一犯再犯，“一认再认”真能免除虚伪性吗，这才是对每一个成年人致命的问题。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以归谬式追问提出：既然这份虚伪无路可逃，何妨索性不认、不再主张“大道理”，做“真小人”，从而从“三重虚伪的无间地狱”中解脱。", "evidence": ["E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以两个未作答的追问收束：明知主张美德必有虚伪的罪、会给人指责自己虚伪的立场，为什么还要主张那些美德。", "evidence": ["E21", "E22"]}
   ],
   "argument_steps": [
    "复述流行判据（A＋B）（P001-P004）。",
    "先认可其表面合理（“这听起来很对，对吗？”）（P005）。",
    "反驳：该判据使“虚伪”绝对化、虚无化（P006）。",
    "以“诚实”为例证成：无人有诚实的能力（P008-P010）。",
    "以“公平”为例证成：无人有公平的能力（P011-P014）。",
    "推出后果：指控沦为无意义控诉（老虎吃肉、马儿吃草类比）（P015）。",
    "补足判据：加入要件 C，重述三条，得出定义（P016-P022）。",
    "说明理由：人无法完美遵从美德，故未做到本身不构成虚伪（P023）。",
    "反推后果：仅按 A＋B 定罪将奖励“主张骗人”者（P024-P026）。",
    "以诘问施压（P027-P028）。",
    "标题句给出结论：真正虚伪者是只取 A＋B 而自认不虚伪的人（P029-P030）。",
    "让步并加难：放宽到三条仍不足，一认再认又再犯者如何（P031-P036）。",
    "归谬：若虚伪无路可逃，索性做“真小人”是否更解脱（P037-P040）。",
    "以两个未回答的“为什么还要主张”收束（P041-P042）。"
   ],
   "concept_usage": [
    {"term": "虚伪", "meaning": "作者给出的界定为三条同时满足：主张或赞同某道德原则（A）、事实证明或自认触犯该原则（B）、在自己也承认 A、B 的前提下自认为无罪（C）。", "evidence": "P022", "ambiguity": "作者亦称放宽到三条后仍不足以处理“一认再认又再犯”的情形，界定的最终形态在文中保持开放。"},
    {"term": "要件A／要件B／要件C", "meaning": "作者对判据的形式化拆解：A＝主张或赞同道德原则；B＝事实证明或自认违背；C＝自认违背却自认无罪。", "evidence": "P021", "ambiguity": "“自认为无罪”与“不承认”的界线未说明。"},
    {"term": "诚实／言实相符", "meaning": "作者假设诚实即“言实相符”，据此称无人具备诚实的能力。", "evidence": "P010", "ambiguity": "该定义是作者为反驳而设的假设，是否即为作者主张的定义未说明。"},
    {"term": "公平", "meaning": "作者称人类根本没有公平的能力，故自称公平者必是不公平且不自知。", "evidence": "P014", "ambiguity": "“公平的能力”未界定，全称否定无依据说明。"},
    {"term": "三重虚伪／无间地狱", "meaning": "作者用佛教语汇形容“一认再认而又一犯再犯”的处境；文中仅此一处出现，未定义“三重”。", "evidence": "P040", "ambiguity": "“三重”所指不明（是否对应 A、B、C 三条）。"},
    {"term": "真小人／表里如一", "meaning": "作者以之指称索性不主张美德、因而“不虚伪”的策略及其自我评价。", "evidence": "P039", "ambiguity": "作者未表明自己是否认可这一策略。"}
   ],
   "examples_and_targets": [
    "“很多小孩子”：作者对被审视判据持有者的称呼（P001），带贬抑色彩。",
    "诚实、公平：作者用来检验 A＋B 判据的两个示例德目（P008-P014）。",
    "控诉老虎要吃肉、指责马儿要跑又要吃草：类比，说明指控失去意义（P015）。",
    "主张“人就应该骗人，越会骗人越有本事”的人：被 A＋B 判据反向奖励的对象（P025）。",
    "“虚伪罪”的绞刑架、“表里如一”的圣地、“真小人”、伪君子：修辞材料（P024、P038、P039）。",
    "被反驳观点：以 A＋B 判定虚伪、并据此指责他人的通俗标准（P001-P004）。",
    "提问者所问“为什么人们普遍讨厌虚伪”：正文未直接回答。"
   ],
   "conditions": [
    "P010 以“假如诚实意味着‘言实相符’的话”作假设前提。",
    "P013 以“你要说你自己公平，只有一种可能”限定推论。",
    "P031 以“即使是把条件放宽到三条，又如何呢？”引入让步后的再追问。",
    "P035 以“如果你一认再认、而又一犯再犯”为条件。",
    "P030 以“这只能借无知而暂免”限定“真正虚伪者”的免责情形。"
   ],
   "rhetoric_and_tone": "通篇第二人称“你”密集诘问，反问句连缀（P005、P008-P009、P011-P012、P024、P027-P028、P032-P034、P035、P037-P042）；以“很多小孩子”这一贬抑称呼引入被批判标准；“绞刑架”“无间地狱”“圣地”等强烈比喻；【自己】用方括号加重；ta 作性别中立指称；结尾两个“为什么还要主张”的追问不作答，形成悬置式收束。",
   "unresolved_questions": [
    "提问的第二部分“为什么人们普遍讨厌虚伪”在正文中未获直接回答。",
    "作者最终立场未明说：全文以“明知如此，你为什么还要主张？”的追问结束，未给出答案，读者无法确定作者是否主张“仍应主张美德”。",
    "“三重虚伪”一词仅出现一次，未定义其“三重”所指。",
    "P030“这只能借无知而暂免”中的“这”指代不明（指“真正虚伪”还是“自认为不虚伪”），影响该句解释。",
    "“很多小孩子”是修辞贬称还是指特定人群，未说明。",
    "“人类根本就没有任何一个人有诚实的能力”“人类根本没有公平的能力”为全称否定断言，无依据或来源，需外部核查（若作为经验主张）。",
    "作者在给出三条判据后又指出其不足以处理“一认再认又再犯”，最终界定是否成立在文中保持开放。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "要件A）该人主张或赞同了一种道德原则。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P004", "quote": "同时满足A和B，就构成“虚伪”。", "relation": "context"},
    {"key": "E3", "paragraph_id": "P006", "quote": "但这实际上会把“虚伪”这个概念绝对化，乃至于在事实上虚无化。", "relation": "contradicts"},
    {"key": "E4", "paragraph_id": "P010", "quote": "假如诚实意味着“言实相符”的话，人类根本就没有任何一个人有诚实的能力", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P013", "quote": "你要说你自己公平，只有一种可能，就是你不但根本不公平，而且还连自己有多不公平都不知道或者不承认。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P014", "quote": "因为人类根本没有公平的能力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P015", "quote": "于是“虚伪”就直接成了无意义的“控诉”。就像控诉老虎要吃肉，指责马儿要跑又要吃草。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "C）当ta认识到自己违背了这条道德原则，ta却说ta自己无罪。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P021", "quote": "要件C）在该人自己也承认A、B皆满足的前提下，该人自认为无罪。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P022", "quote": "三条同时满足，才成其为虚伪。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P023", "quote": "因为人类说实话根本做不到完美的遵从任何美德", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P025", "quote": "你是在大力奖励那些嘴里就主张“人就应该骗人，越会骗人越有本事”的人。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "因为ta们倒是“不虚伪”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P029", "quote": "真正虚伪的，恰恰是只取A+B，而又认为【自己】不虚伪的人。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P030", "quote": "这只能借无知而暂免。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P031", "quote": "但是，即使是把条件放宽到三条，又如何呢？", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P035", "quote": "如果你一认再认、而又一犯再犯，那么“一认再认”真的就能免除你的虚伪性吗？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P036", "quote": "这才是对每一个成年人致命的问题。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P038", "quote": "索性做一个真小人，不就可以从这个怪圈里脱身吗？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P040", "quote": "你不就可以从三重虚伪的无间地狱中解脱了吗？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P041", "quote": "你为什么宁可选择永恒的道德折磨、给一切人指责你虚伪的坚实立场，还是要主张那些美德呢？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P042", "quote": "主张美德，你必有虚伪的罪，明知如此，你为什么还要主张？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学", "道德哲学", "概念分析", "日常语言批判"],
   "issue_candidates": ["如何界定虚伪", "道德原则与行为不一致是否构成虚伪", "道德要求的可实践性", "认罪与再犯的关系"],
   "text_function_candidates": ["答疑", "概念澄清", "论辩", "反诘式说理"],
   "object_candidates": ["很多小孩子（通俗判据持有者）", "真小人", "伪君子", "成年人"],
   "working_keywords": ["虚伪", "要件A", "要件B", "要件C", "言实相符", "公平的能力", "虚伪罪", "一认再认", "三重虚伪", "无间地狱"]
  },
  "notes": "本篇无图片节点。P001-P004 的 A＋B 判据为被作者反驳的流行观点，已用 opponent_view/opponent 归属；P029 在 lexical 中为 heading。全文以两个“为什么还要主张”的反问收束而不作答，作者最终立场未明说，已登记未决。P010、P014 为全称否定断言（人类无诚实／公平的能力），无依据说明。"
 },
 "6ee6c6fa": {
  "analysis": {
   "question_context": "提问者（Q001）问为什么很多年轻女性不喜欢讲道理，已含“女性不讲道理”的预设。作者不接受：主张很多时候不是女性不讲道理，而是指责者把自己认证的道理当普世公理，且双方从未事先约法、也无中立裁判；再以“韩梅梅／李雷”案例逐层分析，指出“无理取闹”的定性本身即爱的反面，结论落在“爱首先是一种尊重，尊重的起点就是不妄断”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "限定性反驳：很多时候不是女性不讲道理，而是小男生认准自己的道理就要判女生“不讲道理”；该机制双向（“闺蜜共识”批评男性本质相同）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "判据：只有对方未遵从ta自己主张且已获同意的道理才算“不讲道理”；以“我的朋友”“我们村里”为依据者，不讲道理的是指控方。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "诊断一：少男少女无事先约法的意识与能力，只想用“三观一致”蒙混，事到临头即失效。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "诊断二与规范：缺中立裁判机构（鱼丸粗面类比）；提出先约道理、先约仲裁机制，这是“讲道理”本身的道理。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "成因：人从小只被老师、父母（后为上司）讲道理，这种“讲道理”混杂教育权柄，且几乎无“不知者不为罪”优惠，教育者常发动“我不是说过”等咒术。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "以三句戏仿自辩与“名场面”过渡，指出后果是绝大多数恋爱期青少年无对等实体间交往伦理经验。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026"], "summary": "规范：对等实体之间是“律法的荒原”，其固有权利是“不知者不为罪”的初犯豁免权而非立法权、审判权；无约定则除非经合法审判否则无罪可言。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "就“爱”作答：爱不是授权立法与审判，而是对立法和审判的克制；作者自述想立规矩但不愿多一个视对方为有罪的理由；末以禅宗语汇自况。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062"], "summary": "设问“真正发生的是什么”，引入并复述韩梅梅／李雷案例（钱包被偷—建议—争吵—哄劝—李雷在知乎称女人不讲道理只能靠哄—三个月后分手），预告逐条分析；lexical 中该案例以 list／quote／listitem 重叠重复呈现。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069"], "summary": "分析工具：一句话是两层信息的复合（内容为表层，身份、场合、上下文为里层，如照片与其 metadata）；只对表层反应是无关者的特权。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P070", "P071", "P072", "P073"], "summary": "让步与反问：李雷的回复在“路人”角度无可指摘，但二人并非陌路；并追问该建议是最大帮助对方，还是对自己成本最小。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081"], "summary": "爱的界定：不问自己成本、先问对方收益；有义务选对方收益最大的措施；对方视你成本为共同成本是爱的内容，不构成你只取最低成本方案的合法理由；“自行节省”与“自居爱人”不可兼得。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P082", "P083", "P084", "P085", "P086", "P087", "P088"], "summary": "双向限定：礼遇是给爱人的特权优待，自行节省使对方觉得被辜负；但待遇是对方自己给的，只能愿赌服输，辜负者无过错；那番道理是陌路人的道理，而你不是陌路人。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P089", "P090", "P091", "P092", "P093", "P094", "P095"], "summary": "作者代拟韩梅梅第一人称独白：可说的道理须你爱我才能说；不问可自欺，问了就要面对离开，而我不想离开，所以不能说；这是她泣不成声后自己也没想明白的话。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P096", "P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105"], "summary": "限定与去性别化：孩子做不到不算其错（没人教过），但法则不因情有可原而宽贷，对方也无法控制自身感受；这不是“女孩子的毛病”而是人类天性；对爱的缺位的觉察内嵌人性。", "role": "qualification"},
    {"unit_id": "U016", "paragraph_refs": ["P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114", "P115", "P116"], "summary": "否定式说明：无标准答案、不是教“正确达标的爱”、应发乎于心；写这些是作反思的起点——不怕犯错而怕不反思，爱是反思和愧悔。", "role": "conclusion"},
    {"unit_id": "U017", "paragraph_refs": ["P117", "P118", "P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130"], "summary": "收束：学话术者只是皮影；要害是停止“无理取闹”的定性，否则以“口袋罪”自我封闭；真相是对方宽纵了你；爱首先是尊重，尊重起点是不妄断，否则即自我迷醉的偶像崇拜。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被全文反驳的定型说法（案例中李雷的知乎回答，与提问预设一致）：女人是感性动物、不讲道理、只能靠哄。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "很多时候（并非一切时候）女性不是不讲道理，而是小男生认准自己的道理就要判女生“不讲道理”；该机制双向，以“闺蜜共识”批评男性本质相同。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有对方未遵从ta自己主张、自己定义的道理才勉强算“不讲道理”；法则须对方也先同意才生效；以“我的朋友没有一个不觉得”之类为依据者，不讲道理的是指控方。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "少男少女根本没有事先约法的意识，即使有意识也无能力；从未约定伦理法则，只想用“三观一致”蒙混过关，事到临头即失效。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "除无立法过程外还缺中立的、双方都接受的裁判机构；作者提出“讲道理之前要先把道理约好，而且要先约好仲裁机制”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成因：人们从小只被老师、父母（后为上司）讲道理，这种“讲道理”混杂教育权柄，且几乎无“不知者不为罪”的优惠。", "evidence": ["E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对等实体之间理所当然享有的是“不知者不为罪”的初犯豁免权，而非立法权与审判权；无具体约定与同意，除非经合法法庭审判，否则ta都无罪可言。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "爱不是互相授予自由立法权与最高审判权，恰恰相反——爱是指对立法和审判的克制；作者自述不愿多一个视对方为有罪的理由。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一句话永远是两层信息的复合：内容是表层，身份、场合、上下文是里层；只对表层作出反应是无关者的特权。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "让步后反问：李雷的回复在“素不相识的路人”角度没有错，但李雷和韩梅梅并非陌路之人。", "evidence": ["E22", "E23"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "追问“你以后多小心点”是能最大帮助韩梅梅的选择，还是对李雷而言成本最小的选择。", "evidence": ["E24"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实践意义上爱就是不问自己的成本如何、先问于对方收益如何；说了爱就有义务选择对方收益最大的措施。", "evidence": ["E25", "E26"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方视你的成本为共同成本而阻止你自行节省，是对方对你的爱的内容，不构成你只提供最低成本方案的合法理由；“自行节省”与“自居爱人”不可兼得。", "evidence": ["E27", "E28"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方给予的依恋、礼遇、信任等是给爱人的特权优待，自行节省使对方觉得被辜负和欺骗；但待遇是对方自己给的，只能愿赌服输，辜负者严格意义上没有过错。", "evidence": ["E29", "E30"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正因如此韩梅梅才无话可说——那番道理是把自己当成“对等的人”、本质是突然转身化为陌路人的道理。", "evidence": ["E31", "E32"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "反问：你不是陌路人，何以可以如此无情地用陌路人的豁免权自辨。", "evidence": ["E33"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者代拟韩梅梅的内心独白：可说的道理须你爱我才能说；不问还可自欺，问了就要面对离开，而我不想离开，所以不能说；这是她自己也没想明白的话。", "evidence": ["E34", "E35", "E36"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这对缺少经验的孩子是困惑挫折的要求，做不到并不算孩子自己的错误（此前没人教过、也没机会积累经验）。", "evidence": ["E37"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这条法则不会因情有可原而高抬贵手：没努力去做就会导致对方心寒；对方想体谅也没用，因为其无法控制这种感受。", "evidence": ["E38", "E39"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "否认这是“女孩子的毛病”，主张这是人类的天性。", "evidence": ["E40", "E41"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原因是这是无爱或失能而空洞的爱的本质特征：人类是毕生追求爱的动物，对爱的缺位的觉察深入骨髓。", "evidence": ["E42", "E43"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不打算肩负这份麻烦就不要轻言爱；不存在既享受爱人礼遇、又不“麻烦”、只付出最轻省边角余热的“爱”。", "evidence": ["E44", "E45"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "否认存在标准答案，也否认这些是用来教“正确达标的爱”的——爱不是照方抓药的体育达标测验，应发乎于心、自由自在地反应。", "evidence": ["E46", "E47"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说这些是给读者作反思的起点：不怕犯错而怕不反思，真正伤害关系的是不反思；爱不是完美，爱是反思和愧悔。", "evidence": ["E48", "E49", "E50"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学话术者只是皮影；李雷真正的要害是停止认定韩梅梅“无理取闹”，否则以“口袋罪”一装了事；真相是对方不忍心难为你而宽纵了你。", "evidence": ["E51", "E52", "E53"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱首先是一种尊重，尊重的起点是不妄断：若爱你，你在我这里永远没有“无理取闹”的定性，找不到解释也只假定自己观察不够；否则即自我迷醉的偶像崇拜。", "evidence": ["E54", "E55", "E56", "E57"]}
   ],
   "argument_steps": [
    "限定反驳提问预设（P001），补充双向性（P002）。",
    "给出“不讲道理”的成立条件与举证责任（P003-P005）。",
    "诊断一：无事先约法，以“三观一致”蒙混（P006-P009）。",
    "诊断二：无中立裁判机构（P010-P012）。",
    "提出规范：先约道理、先约仲裁机制（P013-P014）。",
    "追溯成因：教育权柄与“我不是说过”式追责（P015-P018）。",
    "指出后果：青少年缺乏对等交往伦理经验（P019-P023）。",
    "给出对等关系规范：初犯豁免权而非立法权与审判权（P024-P026）。",
    "界定爱：不是授权立法与审判，而是对立法和审判的克制（P027-P033）。",
    "以禅宗语汇自况过渡（P034-P038）。",
    "引入韩梅梅／李雷案例并复述（P039-P062）。",
    "分析工具：两层信息，只对表层反应是无关者的特权（P063-P069）。",
    "让步与反问：路人角度可行，但二人非陌路；是否为成本最小方案（P070-P073）。",
    "正面界定爱：不问自己成本、先问对方收益；“自行节省”与“自居爱人”不可兼得（P074-P081）。",
    "双向限定：礼遇与愿赌服输，陌路人的道理（P082-P088）。",
    "代拟韩梅梅内心独白（P089-P095）。",
    "限定：孩子做不到不算其错，但法则不宽贷；去性别化（P096-P100）。",
    "机制：对爱的缺位的觉察内嵌人性（P101-P103）；不打算肩负麻烦就不要轻言爱（P104-P105）。",
    "否定式说明：无标准答案、不教话术（P106-P109）。",
    "目的：反思的起点；爱是反思和愧悔（P110-P116）。",
    "回到李雷：皮影、停止“无理取闹”、真相是宽纵（P117-P122）。",
    "收束：爱首先是尊重，不妄断，否则即偶像崇拜（P123-P130）。"
   ],
   "concept_usage": [
    {"term": "讲道理", "meaning": "作者拆为程序要求：先约好道理（立法）、再约好仲裁机制（裁判），以双方事先同意为生效条件；未满足者只是“自以为在讲道理”。", "evidence": "P013", "ambiguity": "“约好”的形式与仲裁机构形态未说明。"},
    {"term": "三观一致", "meaning": "少男少女替代约法的含糊说法；作者称其事到临头即失效，“三观”充满“此一时彼一时”。", "evidence": "P009", "ambiguity": "作者未正面定义“三观”。"},
    {"term": "对等的实体／不知者不为罪", "meaning": "无上下权柄关系的双方；其间是“律法的荒原”，其固有权利是“不知者不为罪”的初犯豁免权。", "evidence": "P024", "ambiguity": "“一切价值都待重估”为尼采式表述；豁免是否有例外未说明。"},
    {"term": "两层信息的复合信息", "meaning": "话语内容为表层，说话的身份、场合、上下文为里层；只对表层反应是“无关者的特权”。", "evidence": "P065", "ambiguity": "里层信息如何判定、由谁判定未说明。"},
    {"term": "爱", "meaning": "本文界定：实践上不问自己成本、先问对方收益；是对立法和审判的克制；是尊重、不妄断、反思和愧悔。", "evidence": "P076", "ambiguity": "多层界定之间的关系未系统说明。"},
    {"term": "自行节省／自居爱人", "meaning": "只提供对自己成本最低的方案／自居爱人身份；作者称二者不可兼得。", "evidence": "P081", "ambiguity": "与合理自我照顾的界线未说明。"},
    {"term": "无理取闹／口袋罪／偶像崇拜", "meaning": "把难解行为定性为“无理取闹”是可套用于任何情形的“口袋罪”；保留此种判断权者所享受的是偶像崇拜而非爱。", "evidence": "P119", "ambiguity": "是否存在确应认定的情形未讨论。"}
   ],
   "examples_and_targets": [
    "韩梅梅与李雷案例：作者自设并自述“这案例够真了吗”的例证，用于逐层分析（P041-P062）。",
    "李雷的知乎回答“女人…不讲道理，只能靠哄”：叙事内被反驳的定型说法（P057）。",
    "“闺蜜共识”批评“直男”“注孤生”：与提问预设对称的反例（P002）。",
    "“我的朋友没有一个不觉得”“我们村里都这样”：作者称为“混账话”的指控依据示例（P005）。",
    "“既没有鱼丸，又没有粗面，吃啥鱼丸粗面？”：影视台词式类比（P012）。",
    "“我不是说过”“难道你妈/爸没教过你吗”：作者称为教育者“咒术”的引语（P018）。",
    "“师傅，我不是悟空，我是八戒啊！！”：戏仿；“名场面——禁忌调教の伦理崩坏”为网络化修辞（P021-P022）。",
    "照片内容与 metadata 的类比：说明两层信息（P066）。",
    "“我有不世法，直指人心，教外别传，不立文字。本来无一物，何处惹尘埃？”：禅宗语汇，未注明出处（P034-P038）。",
    "“三十六计”“情圣先辈”“皮影”：修辞材料（P117）。"
   ],
   "conditions": [
    "核心主张以“很多时候——注意哦，我可没说一切时候哦”限定（P001）。",
    "法则以“对方如果也先同意了”为生效条件（P004）。",
    "豁免以“没有具体的约定与同意”为前提（P026）。",
    "结论对象限定为“恋爱期的青少年”“缺少经验的孩子们”（P023、P096）。",
    "作者声明法则不因“情有可原”而宽贷（P097）。",
    "保留极端情形：客观上无法承受而只能停止关系（P127）。"
   ],
   "rhetoric_and_tone": "长文说理与情感独白交织：第二人称“你”贯穿诘问；口语插话式限定（“注意哦，我可没说一切时候哦”）；反问密集；戏仿影视台词与网络亚文化用语（“の”“名场面”）；禅宗语汇自况（P034-P038）；P089-P095 转第一人称抒情独白；结尾以“偶像崇拜从来不会有任何好结果”断言收束。P014 为引用块（“要讲道理，就要讲讲道理的道理。——真·道理套娃”）。",
   "unresolved_questions": [
    "lexical 与 text 有 2 处结构差异：list(P041)／quote(P061)／listitem(P043-P058)／unmodeled(P042,P062) 相互重叠，同一段对话在结构中重复约 899 字。经核验：130 个节点文本均为 text 子串，text 中未被节点覆盖的 113 个字符全为段落间换行，正文无缺失，差异属结构重复，故仍判 read（如需按结构差异从严可复核）。",
    "作者只以“这其实不止发生在男对女，女对男也一样”带过，未说明案例与“年轻女性”提问预设之间的代表性关系。",
    "“这是人类的天性”“对爱的缺位的觉察能力深入骨髓、内嵌在人性的根基里”为关于人性的全称断言，无依据或来源，需外部核查。",
    "“一片律法的荒原，一切价值都待重估”为尼采式表述，作者未注明出处或借用程度。",
    "P034-P038 禅宗语汇（“教外别传，不立文字”“本来无一物，何处惹尘埃”）未注明出处，属引用还是自述不明。",
    "作者未说明自身性别与经验立场，而多处使用第一人称情感独白（P030-P033、P089-P095）。",
    "“不知者不为罪”的初犯豁免权是否有例外（如重大伤害）未说明。",
    "作者既称“没有标准答案”“不是教正确达标的爱”，又给出“不问自己成本、先问对方收益”等较强规范，二者关系未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P057", "quote": "她们是不讲道理的，只能靠哄", "relation": "contradicts"},
    {"key": "E2", "paragraph_id": "P001", "quote": "女性不是不讲道理", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "又有什么本质的不一样呢？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "对方不讲你主张、你定义的道理，是理所当然的权利。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "对方如果也先同意了，这个“道理”才算生效", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "那么不讲道理的是你。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "根本没有任何事先约法的意识", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "即使有这意识，亦无此能力。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "“三观一致”个狗屁", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "没有中立的、双方都接受的裁判机构", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "讲道理之前要先把道理约好，而且要先约好仲裁机制", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "从小到大都只经历过老师、父母给ta们讲道理的过程", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "享受不到“不知者不为罪”的优惠条件", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P025", "quote": "“不知者不为罪”的初犯豁免权", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "否则ta都无罪可言", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P029", "quote": "爱是指对立法和审判的克制", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P032", "quote": "我将来就多了一个视你为有罪的理由", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P033", "quote": "我不要这个理由。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P065", "quote": "永远是两层信息的复合信息", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P066", "quote": "话的内容是表层，说话的身份、场合、上下文是里层", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P067", "quote": "只对表层信息作出反应是无关者的特权。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P070", "quote": "假设李雷只是一个素不相识、毫无关系的路人", "relation": "qualifies"},
    {"key": "E23", "paragraph_id": "P071", "quote": "但问题是，李雷和韩梅梅是陌路之人吗？", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P073", "quote": "还是这是对李雷而言成本最小的选择？", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P076", "quote": "爱就是不问自己的成本如何，先问于对方收益如何。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P077", "quote": "你有义务选择对方收益最大的措施", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P078", "quote": "因为视你的成本为二人共同的成本而阻止你这样做", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P081", "quote": "“自行节省”和“自居爱人”不可兼得。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P082", "quote": "是给予一名爱人的至高无上的特权优待。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P084", "quote": "辜负者严格意义上没有任何过错。", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P085", "quote": "韩梅梅才无话可说", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P086", "quote": "本质其实是突然转身化为的陌路人", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P088", "quote": "何以可以如此无情的用陌路人的豁免权自辨？", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P090", "quote": "但那是你爱我才可说的道理。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P093", "quote": "我不能冒让我彻底心凉的风险，我不能说。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P095", "quote": "这才是韩梅梅泣不成声后面那无法言明", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P096", "quote": "并不能算是小孩子们自己的错误", "relation": "qualifies"},
    {"key": "E38", "paragraph_id": "P097", "quote": "会因为你情有可原就会对你高抬贵手", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P098", "quote": "因为对方自己无法控制这种感受", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P099", "quote": "绝对不要自以为这是“女孩子的毛病”", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P100", "quote": "错了，这是人类的天性。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P101", "quote": "无爱或者说失能而空洞的爱的本质特征", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P102", "quote": "对于爱的缺位的觉察能力深入骨髓", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P104", "quote": "不打算肩负这份麻烦，不要轻言爱。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P105", "quote": "世界上不存在既可以享受属于爱人的礼遇", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P107", "quote": "这个实在没有标准答案", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P109", "quote": "你本来就应该发乎于心，自由自在的去做反应。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P112", "quote": "不怕犯错，而怕不反思。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P114", "quote": "真正伤害关系的不是犯错，而是不反思", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P116", "quote": "爱不是完美，爱是反思和愧悔。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P117", "quote": "李雷不过是一张皮影罢了。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P118", "quote": "停止认定韩梅梅“无理取闹”", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P121", "quote": "不忍心难为你，于是宽纵了你罢了。", "relation": "contradicts"},
    {"key": "E54", "paragraph_id": "P123", "quote": "爱首先是一种尊重。尊重的起点就是不妄断。", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P124", "quote": "永远没有“无理取闹”这种定性可言", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P127", "quote": "我也绝不考虑这是“无理取闹”。", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P129", "quote": "而是自我迷醉的偶像崇拜", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["两性关系与交往伦理", "伦理学（规则与裁判）", "情感与亲密关系"],
   "issue_candidates": ["“不讲道理”的判据与举证责任", "恋爱关系中约法与仲裁机制的缺失", "“无理取闹”定性的危害", "爱的义务与成本选择", "性别刻板印象"],
   "text_function_candidates": ["答疑", "论辩", "案例分析", "劝诫"],
   "object_candidates": ["年轻女性", "小男生", "韩梅梅", "李雷", "恋爱期的青少年", "教育者（老师、父母、上司）", "知乎"],
   "working_keywords": ["不讲道理", "事先约法", "仲裁机制", "三观一致", "不知者不为罪", "初犯豁免权", "陌路人", "自行节省", "无理取闹", "口袋罪", "两层信息", "反思和愧悔"]
  },
  "notes": "本篇无图片节点。text 与 lexical 有 2 处结构差异：list(P041)/quote(P061)/listitem(P043-P058)/unmodeled(P042,P062) 重叠，同一段对话在结构中重复约 899 字；经核验 130 个节点文本均为 text 子串，text 未覆盖的 113 字符全为段落间换行，正文无缺失，故判 read。案例中“女人不讲道理只能靠哄”为叙事内李雷的说法，用 opponent_view/opponent 归属。P089-P095 为作者代拟韩梅梅的第一人称独白，仍属作者文本。P034-P038 禅宗语汇未注明出处。"
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
