# -*- coding: utf-8 -*-
"""批次 r001-b0144 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0144.sessions.py            # 写 out/r001-b0144.out.jsonl
  python3 records/r001-b0144.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0144"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0144.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "9b7dc2d2": {
  "analysis": {
   "question_context": "知乎提问（Q001）问“不敢去爱是因为什么？”，由提问者提出，非作者立场。作者以回答者身份给出病因诊断与替代方案：先批驳“爱就是百依百顺”的流行理解，再以“愿赌服输的猜测”为新基线重述爱，最后用双杀逻辑对照收尾。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开篇核心论断：不敢去爱的首因是把爱误认为百依百顺。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "说做不一的现象：口头承认爱不是百依百顺，行动照旧；“爱是假的”批评多指向未满足理所当然的要求，批评者与被批评方的台词，逻辑卡死成悲情剧。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "病根诊断：把爱当成免费版的需求提出与满足，故以“免费满足”为可贵；作者否认爱是这种交换，称需求-满足模型本身是幻觉。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "定义：人并不知道自己的需求；需求的真正满足靠他人观察与勇敢猜测，本质必然是愿赌服输的猜测。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015"], "summary": "定义爱的基本逻辑（A做自己理解的B的需求、B原谅、A道歉）与爱的主要秘密（把他人快乐当作最大快乐并视为消耗自身的正当理由）。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017"], "summary": "前提与理由：人有把有限生命投入无限快乐的本能；游戏、美食、影视之乐长期乏味、缺少爱的裂变回报且死后无意义。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "难点在“百依百顺”逻辑使人体会不到上述感受而透支熄火；以鸡蛋与鸡的比喻说明理解与激励的正循环可消解恐惧。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "健康之爱示例：A偷偷准备生日礼物、B不满意、A道歉换一个；关键在A认定获得B的快乐是自己的追求，B无义务且受困扰，故赌中是欢喜、赌歪只是正常失误与本钱。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032"], "summary": "新基线下B各种反应的收益评估：骄傲、赚翻、不赔不赚、索赔也无可厚非（额度有法律与法官裁决），赌赢更好，故对A几乎全是正面。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037"], "summary": "回应“仍嫌对方难搞”：此类人比例不大，换一个即可；仍过线者可果断放弃，因问题不是你可不可爱而是对方可不可爱（unlovable）。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042"], "summary": "对照“百依百顺”的双杀逻辑：双方互相认定对方不爱自己，形成怨恨正反馈；唯一幸存情形是对方爱你而你不接受、保有合法的不满意权，但这会使对方失去动力。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P043", "P044", "P045"], "summary": "收尾比喻：对方手里是手榴弹、你是没插电的微波炉，全靠不插电才活下来，接电即粉身碎骨。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不敢去爱的最首要原因，是错误地认为“爱就是百依百顺”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们口头上都否认爱是百依百顺，实际做起来照样百依百顺；批评“爱是假的”时，绝大多数是在批评对方没有满足某种理所当然的要求。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种僵局源于把做事与爱都理解为“提出需求满足需求”（生意是收费版、爱是免费版），于是以为爱可贵在“免费满足”。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "爱根本不是免费版的需求提出与满足，因为“提出需求-满足需求”本身是一种幻觉：人并不知道自己的需求。", "evidence": ["E6", "E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "需求的真正满足靠别人根据观察勇敢猜测、超出需求方自身的局限；它在本质上必然是一种愿赌服输的猜测。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱的基本逻辑是A把自己理解的B的需求当作快乐的事去做、B表示原谅、A为造成的困扰道歉；爱的主要秘密是把别人的快乐当成自己最大的快乐，并视为消耗自身的正当理由。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若用“爱就是百依百顺”的逻辑去做爱，就体会不到上述感受，随之丧失动力并因透支而熄火；“对爱的正确理解”是鸡蛋，正确之爱所触发的积极回应带来的激励是鸡，进入正循环后就不会再觉得爱可怕。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在“A自担风险地追求B的快乐”这根新基线上，赌中是皆大欢喜，赌歪只是正常失误且损失由B承受，A的“损失”只是玩游戏的本钱。", "evidence": ["E16"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "基于新基线，B满意、温柔表达、生气、索赔等反应对A而言结果几乎全是正面（骄傲、赚翻、不赔不赚、无可厚非），赌赢则更好。", "evidence": ["E17", "E18", "E19"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若在新基线下仍觉得对方难搞，此类破坏性处理关系的人比例不大；仍过线者可放心果断放弃，因为这不是你爱不爱的问题，而是对方可不可爱（lovable）的问题。", "evidence": ["E20", "E21"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "若“较真”，不可爱（unlovable）本质上就是反社会性（sociopath），此时问题属“医疗伦理”而非普通的爱的关系问题。", "evidence": ["E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按“爱就是百依百顺”的逻辑，A与B会互相认定对方不爱自己，形成怨恨的正反馈循环，如“奔向地狱的路上，两脚都是油门”。", "evidence": ["E23", "E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "该双杀逻辑下唯一幸存的情形是对方“爱”你而你不接受：保有合法的不满意权反而不激发怨恨循环，但这会令对方渐渐失去动力。", "evidence": ["E25"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在这套错位关系中，对方手里的是手榴弹而非鸡蛋，你也不是孵化箱而是没插电的微波炉，活下来全靠“不插电”。", "evidence": ["E26", "E27"]}
   ],
   "argument_steps": [
    "提问语境（Q001，提问者）：不敢去爱是因为什么。",
    "核心诊断：首因是把爱误认为“爱就是百依百顺”（P001）。",
    "现象举证：口上说不是、行动照旧；对“爱是假的”的批评多指对方未满足理所当然的要求，双方各自委屈，逻辑卡死成悲情剧（P002-P005）。",
    "前提归因：把爱理解为免费版的“提出需求-满足需求”，故以“免费满足”为可贵（P006-P007）。",
    "反驳该前提：需求-满足模型本身是幻觉，人并不知道自己的需求（P008-P010）。",
    "重新定义：需求满足靠观察与勇敢猜测，本质必然是愿赌服输的猜测（P011-P013）。",
    "定义爱的基本逻辑与主要秘密（P014-P015）。",
    "前提：人有把有限生命投入无限快乐的本能（P016）。",
    "理由：游戏、美食、影视之乐长期乏味、缺少爱的裂变回报、死后无意义（P017）。",
    "条件推论：用“百依百顺”逻辑做爱则体会不到、动力枯竭而熄火（P018-P019）。",
    "比喻例证：蛋生鸡鸡生蛋的正循环消解恐惧（P020-P021）。",
    "示例：生日礼物场景说明A的基线（P022-P026）。",
    "条件枚举与让步：B满意/温柔/生气/索赔/高兴五种情形下A的收益（P027-P031）。",
    "小结：新基线下A的结果几乎全正面（P032）。",
    "回应反驳：仍嫌对方难搞时概率大降、可果断放弃，unlovable 归入反社会性（P033-P037）。",
    "对照论证：百依百顺导致双杀式怨恨正反馈，唯一幸存者是“不接受”的一方（P038-P042）。",
    "结论：手榴弹与不插电微波炉的比喻收束（P043-P045）。"
   ],
   "concept_usage": [
    {"term": "爱就是百依百顺", "meaning": "本文要批驳的流行理解：把爱等同于无条件顺从对方提出的需求。", "evidence": "P001", "ambiguity": "作者未界定“百依百顺”的精确边界（是否含重大伤害或不可能之事）。"},
    {"term": "提出需求-满足需求", "meaning": "作者用以指商业交换式的需求招标与投标模型，并把爱说成其“免费版”。", "evidence": "P006", "ambiguity": "作者一边称该模型是幻觉，一边仍用它描述商业交易，未交代二者差别。"},
    {"term": "愿赌服输的猜测", "meaning": "作者对满足他人需求之方式的界定：不可确知、需主动承担失败的猜测。", "evidence": "P012", "ambiguity": "“必然”为强断言，作者未给出论证，只以“看清楚——必然”强调（P013）。"},
    {"term": "基线", "meaning": "本文指判断爱的关系是否成立的默认前提，即A的付出是自担风险的赌博。", "evidence": "P026", "ambiguity": "“新基线/这根基线”未给出形式化定义，靠示例归纳。"},
    {"term": "lovable / unlovable（可不可爱）", "meaning": "作者用以替代“你爱不爱”的判准，指对方是否值得被爱、是否具备接受爱的能力。", "evidence": "P036", "ambiguity": "判定标准未给出；作者以“如果你要较真的话”把 unlovable 等同于反社会性（sociopath），属可争议的术语借用。"},
    {"term": "正循环", "meaning": "正确理解爱→得到积极回应→获得激励→持续做爱的自我强化回路。", "evidence": "P021", "ambiguity": "循环启动条件（先有理解还是先有回应）未说明。"}
   ],
   "examples_and_targets": [
    "提问者的问题“不敢去爱是因为什么？”（Q001）：提问语境，非作者主张。",
    "批评者台词“其实你对我做的别的那些服务我并不需要啊……你件件都做不到，还谈什么爱呢？”（P003）：作者转述的被分析说法，非作者立场。",
    "被批评方“我这算什么爱呢”的自我怀疑（P004）：作者描述的心理现象。",
    "“做生意就是收费版的提出需求满足需求，爱就是免费版的提出需求满足需求”（P006）：被作者批判的流行类比对象。",
    "打游戏、吃海鲜、看电影（P017）：与爱对比的快乐来源，修辞与对比材料。",
    "鸡蛋与鸡（P020-P021）：比喻。",
    "A偷偷为B准备生日礼物、B不满意、A道歉换一个、B自称脾气古怪（P023-P028）：作者构造的说明性示例。",
    "索赔额度、法律保障、法官裁决、趁人度假拆房修新房（P030）：举例兼调侃。",
    "药店发半斤鸡蛋就能排长队（P035）：类比，论证“不愁没人想要爱”。",
    "“奔向地狱的路上，两脚都是油门”（P040）：比喻。",
    "手榴弹与没插电的微波炉（P043-P044）：比喻。",
    "全文未出现真实人物、机构或数据来源。"
   ],
   "conditions": [
    "若用“爱就是百依百顺”的逻辑去做爱，则体会不到爱带来的感受，动力枯竭而熄火（P019）。",
    "若基于新基线仍觉得对方太难搞，作者称此类人比例不大，换一个即可（P033-P034）。",
    "若对方仍“过线”，可以放心果断放弃（P036）。",
    "若B用生气表达，属不赔不赚；若B生气并索赔，也无可厚非，索赔额度过大有法律保障与法官裁决（P029-P030）。",
    "若B竟然很高兴，则视为赌赢（P031）。",
    "作者依赖但未论证的前提：人有把有限生命投入无限快乐追求的本能（P016）。",
    "“比例不大”“概率会大大的下降”为无数据来源的估计（P034）。",
    "时间尺度：游戏等快乐“长期看”乏味（P017）；死者死后无意义（P017）；B因礼物受到一系列困扰（P025）。"
   ],
   "rhetoric_and_tone": "口语化知乎回答体，第二人称“你”的劝导与训诫口吻；连续设问自答（“难点在哪呢？”“健康的爱是个什么循环呢？”“为啥会走向这个方向？”“你看到没有？”）；大量比喻（鸡蛋与鸡、药店鸡蛋、手榴弹与没插电微波炉、拆房修新房）；反问与夸张（“难道不许人家生气么？”“那不是更好吗？”“你焉能不怕？”）；黑色幽默与戏谑（“奔向地狱的路上，两脚都是油门”）；结构上先破“百依百顺”、再立“新基线”、后用双杀逻辑对照收束。",
   "unresolved_questions": [
    "“百依百顺”的精确边界未说明，无法判断作者批驳的对象是否被弱化处理。",
    "新基线中A对B造成的“困扰”是否有上限（除法律赔偿外）未说明。",
    "“比例不大”“概率会大大的下降”无数据或调查来源。",
    "把 unlovable 等同于反社会性（sociopath）缺判准与依据（P037），需外部核查。",
    "P030提到“索赔额度问题你有法律保障”，未指明法域与法律依据。",
    "该文为知乎回答，正文之外可能还有平台折叠/编辑内容未收录；图片节点为0，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不敢去爱的最首要的原因，是错误的认为“爱就是百依百顺”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "实际上一做起来，照样还是百依百顺", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "绝大部分都是在批评对方没有满足某种理所当然的要求", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "爱就是免费版的提出需求满足需求", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "爱可贵就可贵在“免费满足”四个字上", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "爱根本就不是免费版的“提出需求和满足需求”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "“提出需求-满足需求”本身就是一种幻觉", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "人并不知道自己的需求", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "而是靠别人根据观察去勇敢的猜测", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "它在本质上必然是一种愿赌服输的猜测", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "爱的基本逻辑是A把自己理解的B的需求看作一个快乐的事去做", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "一个人会把其他人的快乐当成了一种最大的快乐", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "你是不可能体会到上面这些感受", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "“对爱的正确理解”是鸡蛋", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "蛋生鸡，鸡生蛋，踏入正循环", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "赌中了当然皆大欢喜，赌歪了却完全是正常失误，是B有损失", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "A的感觉是很骄傲", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P031", "quote": "而如果B竟然很高兴呢？那当然是赌赢了啊", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P032", "quote": "对于A来说结果几乎全是正面", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "换一个就好啦", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P036", "quote": "而是一个对方可不可爱（lovable）的问题", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "不可爱（unlovable）本质上就是反社会性（sociopath）", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P039", "quote": "A的第一念头是B是因为不爱自己所以不满意", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P040", "quote": "奔向地狱的路上，两脚都是油门", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P041", "quote": "你有权不满意，反而不会激发这种怨恨的正反馈循环", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P043", "quote": "ta手里的本来就不是个鸡蛋，而是个手榴弹", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P045", "quote": "一接电就粉身碎骨，你焉能不怕？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系", "情感心理", "伦理学/道德哲学", "爱与需求理论"],
   "issue_candidates": ["不敢去爱的原因", "爱是否等于百依百顺", "需求能否被明确表达与满足", "爱的正反馈机制", "不可爱的人与反社会性"],
   "text_function_candidates": ["知乎问答回答", "病因诊断与概念重构", "劝导文", "比喻论证"],
   "object_candidates": ["爱（love）", "需求（need）", "愿赌服输的猜测", "百依百顺逻辑", "lovable/unlovable", "sociopath"],
   "working_keywords": ["爱就是百依百顺", "免费满足", "提出需求-满足需求", "愿赌服输", "新基线", "正循环", "鸡蛋与鸡", "手榴弹", "不插电"]
  },
  "notes": "已按语料全文逐段读完（无图片节点，无需图像核验）。提问字段 Q001 属提问者（attribution=questioner），文中批评者与被批评方的台词为作者转述/构造，未归给作者。P003中“——”（破折号）处为原文形态。需外部核查项：unlovable≈sociopath 的论断、P030提到的法律保障、P034的比例估计。"
 },
 "5975f347": {
  "analysis": {
   "question_context": "知乎提问（Q001，提问者）问「爱」与「团结」哪一个更有力量、更值得被追求。作者不直接做力量排序，而是先拆解“团结”口号的方向难题与伪团结，再把团结意识按接受一致意见的节点分级，最后把团结意识的顶点定为“爱”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出团结最要害的问题是“谁向谁团结”这一方向问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007"], "summary": "对话举例：你我要去不同城市却齐喊团结，口号不解决方向；提出的投票办法仍回避了去哪边。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "投票实为斗争形式：拉票演变为广告投入、设计成本、大礼包、隐性威慑武力、诉讼基金等实力对抗，最终还是“实力解决”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "反问与判定：若终归靠实力，这种“团结”与“强者为尊”无本质区别，实质是要求人识时务、自觉上道。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "正面定义：真正的团结是理智承认“一致意见”本身有价值、并在一定程序后不可否认地超过“我的意见”和“正确的意见”；认同到特定节点即为有团结意识。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"], "summary": "度量方式：团结意识只有强弱，其强弱可用接受一致意见的节点在决策流程上的序号精确区分（提案阶段无条件接受最强，其后依次递减）。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020"], "summary": "推论与组织对策：无团结精神者会从数学上拖长决策；组织存活的关键是明智掌握可接受的团结水平，劝退导致流程过长的人。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022"], "summary": "成本论证：组织无法接受过长乃至无限的共识流程，因为持续决策中与没能产生决策都在持续产生成本，积累成本迟早超过决策正确的预期收益；看明白这条铁律、消除侥幸心态是团结意识的起点。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025"], "summary": "限定与反驳：仅有起点级认知不够，实践中必然执行成不断再等再博，直到成为最后一个并害怕末位淘汰；组织若把及格线定在此处且此类人多，仍会竞争失败而灭亡。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P026"], "summary": "前提：同类竞争下，自然法要求极尽最大可能追求顶点。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P027", "P028", "P029"], "summary": "顶点定义与收尾：团结意识的顶点是本来就打算为你而死、可随时放弃坚持己见，继续反对不是为自己而是为你们——也就是爱。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "团结最要害的问题是“谁向谁团结”这一方向问题。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在方向分歧下喊团结不解决问题；投票到最后其实是一种斗争形式，拉票总会演变成实力的对抗，最终还是“实力解决”。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "若反正是实力解决，所谓的“团结”与“强者为尊”没有本质区别；这种安排下的“团结”本质上是在要求人不要敬酒不吃吃罚酒、要自觉上道。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的团结，是理智地明白“一致意见”本身就有价值，而且是在一定程序后有不可否认的、超过“我的意见”和“正确的意见”的价值。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要一个人认同到特定节点（即认为“及时的一致意见”比“特别有利于我的意见”和“来得太迟的正确意见”更有价值），就可以说他有团结意识；团结意识只有强弱之别，不再能说没有。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "团结意识的强弱可以非常确切地用接受一致意见的节点在整个决策流程上的序号来区分，例如在提案阶段就表态“无条件接受一切决议”强于提案之后再接受，后者又强于第一轮表决后接受。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "没有团结精神的人将会不可避免地从数学上将决策过程拖得更长。", "evidence": ["E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个组织能够存活的关键，在于对“可以接受的团结水平”做明智的掌握，即劝退某些导致决策流程太长的人。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "组织无法接受过长的共识流程乃至无限长的决策流程：持续决策中与没能产生决策都每分每秒产生大量成本，迁延日久积累的成本迟早超过“决策正确”的预期收益，使决策本身失去意义。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "清楚看明白这条组织不想灭亡就一定会执行的铁律、消除“只能接受特别有利于我的意见和无论多迟的正确意见”的侥幸（实则愚蠢）心态，是一个人团结意识的起点。", "evidence": ["E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "仅有起点级别的团结意识不够，那只是“我知道迟早得弃牌”的理论认知，实践中必然执行成“再等等”“再坚持一下”“再博一博”“我还不是最后一个”，直到真的成为最后一个并开始害怕末位淘汰。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "如果一个组织把团结意识的及格线定在“怕末位淘汰”处，而导致此类策略的人过多，这个组织无疑还是要在竞争中失败而灭亡。", "evidence": ["E23"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "万事就怕同类竞争，一旦有同类竞争，就等于自然法在要求你极尽最大的可能去追求顶点。", "evidence": ["E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "团结意识的顶点是：本来就打算为你而死、可以在任何时候放弃坚持己见，继续坚持反对不是为自己而是为你们——也就是爱。", "evidence": ["E25", "E26"]}
   ],
   "argument_steps": [
    "提问语境（Q001，提问者）：爱与团结哪一个更有力量、更值得追求。",
    "提出要害问题：团结要先问“谁向谁团结”（P001）。",
    "对话式举例：上海/深圳分歧下“团结”口号空转（P002-P007）。",
    "理由：投票即斗争形式，拉票演变成实力对抗，最终仍是实力解决（P008-P010）。",
    "反问与判定：如此团结等同强者为尊，实为要求人识时务（P011-P012）。",
    "正面定义：真团结与团结意识（P013-P014）。",
    "定义度量：以接受一致意见的节点在流程中的序号区分团结意识强弱（P015-P017）。",
    "推论：无团结精神者拖长决策，组织须掌握可接受的团结水平、劝退拖长者（P018-P020）。",
    "成本论证：过长或无限的决策流程使成本超过收益，决策失去意义；看明白此铁律是团结意识的起点（P021-P022）。",
    "限定与反驳：仅有起点级认知不够，实践上必然拖延至末位淘汰处境；及格线定低则组织仍灭亡（P023-P025）。",
    "前提：同类竞争下自然法要求追求顶点（P026）。",
    "结论：团结意识的顶点是愿为他人而死、随时放弃己见，也就是爱；以此回应提问（P027-P029）。"
   ],
   "concept_usage": [
    {"term": "团结", "meaning": "本文分两层：被批判的“向实力看齐、识时务”的伪团结（P012），与作者定义的“承认一致意见本身有价值、并按程序接受”的真团结（P013）。", "evidence": "P013", "ambiguity": "同一词在文中承担正反两种含义，作者以“真正的团结”“这种安排下的团结”区分。"},
    {"term": "团结意识", "meaning": "以“接受及时的一致意见优先于特别有利于我的意见和太迟的正确意见”的接受节点来度量的意识，只有强弱之分。", "evidence": "P014", "ambiguity": "“特定的节点”未明确给出判定者与判定程序。"},
    {"term": "一致意见", "meaning": "在一定程序之后产生的、价值不可否认地超过个人意见与“正确意见”的集体决定。", "evidence": "P013", "ambiguity": "“一定程序”未具体说明（是否含投票、表决门槛），作者未给出可操作定义。"},
    {"term": "实力解决", "meaning": "投票拉票最终演化成资源、武力等对抗后的结果。", "evidence": "P010", "ambiguity": "作者未说明是否存在不被实力扭曲的决策程序。"},
    {"term": "自然法", "meaning": "作者用于说明同类竞争下“追求顶点”这一要求的来源的术语。", "evidence": "P026", "ambiguity": "未定义，也未说明其与法律或道德的关系。"},
    {"term": "顶点", "meaning": "团结意识的最高形态：本来就打算为你而死、随时放弃坚持己见。", "evidence": "P028", "ambiguity": "该顶点是否为可达的现实要求，抑或只是极限标尺，作者未说明。"},
    {"term": "爱", "meaning": "本文末句把团结意识的顶点直接等同于“爱”。", "evidence": "P029", "ambiguity": "全文未对“爱”作定义，仅以此句收束，与作者其他文章的用法关系需跨文核查。"}
   ],
   "examples_and_targets": [
    "“你要去上海，我要去深圳”“我们要团结！”“嗯嗯！团结！”的短对话（P002-P004）：作者构造的示例，说明口号不解决方向问题。",
    "“要不投票吧，谁票多去哪边”（P007）：被分析的解决机制。",
    "广告投入、设计成本、大礼包、隐性的威慑武力、诉讼基金（P009）：拉票演变为实力对抗的举例。",
    "“敬酒不吃吃罚酒”“知道好歹”“上道”（P012）：俗语引用，属被批判的伪团结要求。",
    "“无条件接受一切决议”、提案之后接受、第一轮表决后接受（P017）：团结意识强弱的分级示例。",
    "“我知道迟早得弃牌”（P023）、“再等等”“再坚持一下”“再博一博”“我还不是最后一个”（P023）：引用典型拖延心态。",
    "“末位淘汰”（P024）：借用组织制度说法。",
    "“我本来就打算为你而死”（P028）：顶点的极端化表述。",
    "全文未出现真实人物、机构或数据。"
   ],
   "conditions": [
    "若有同类竞争，就等于自然法要求极尽最大可能追求顶点（P026）。",
    "若组织把团结意识及格线定在“怕末位淘汰”处且此类策略者过多，则组织仍会在竞争中失败灭亡（P025）。",
    "前提：组织无法接受过长的共识流程，更无法接受无限长的决策流程（P021）。",
    "条件：只要一个人认同到特定节点，就可说他有团结意识，只是强弱不同（P014-P015）。",
    "时间与成本：决策每分每秒产生成本，迁延日久积累成本迟早超过“决策正确”的预期收益（P021）。",
    "强断言语气：“不可避免”（P018）、“迟早”“一定会”（P021-P022）、“必然执行成”（P023）、“无疑”（P025）。"
   ],
   "rhetoric_and_tone": "短句分行、以对话体开场（“你要去上海，我要去深圳。”“我们要团结！”“嗯嗯！团结！”“……”）制造荒诞感；设问自答（“怎么说呢？”“而团结意识的顶点是什么呢？”）与反问（“有什么本质的区别呢？”）；排比（“变成广告投入、变成设计成本、变成大礼包……”“再等等”“再坚持一下”“再博一博”）；引用俗语与制度词（敬酒不吃吃罚酒、上道、末位淘汰）；冷峻的训诫与组织理性口吻；结尾以“也就是爱。”作反转式收束。",
   "unresolved_questions": [
    "“特定的节点”“一定程序”未给出可操作定义，团结意识的度量方式是否可用于所有决策流程未说明。",
    "P021的成本与收益比较无量化依据或案例。",
    "“自然法”（P026）未定义，其规范来源不明。",
    "提问是“爱”与“团结”哪一个更有力量、更值得追求，作者只把团结意识的顶点等同于爱，未直接对两者的力量作比较排序（是否完整回应提问存疑）。",
    "“爱”在本文未定义，只有末句断言；与作者其他文章用法的异同需跨文核查，初读阶段不作归纳。",
    "该文为知乎回答，正文之外可能还有平台折叠或编辑内容未收录；图片节点为0，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "团结有个最要害的问题——谁向谁团结？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P009", "quote": "投票到最后其实就是一种斗争的形式", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P009", "quote": "变成隐性的威慑武力、变成诉讼基金", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "到最后，其实还是“实力解决”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "那么所谓的“团结”和“强者为尊”有什么本质的区别呢？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "本质上其实是在要求人不要敬酒不吃吃罚酒", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "真正的团结，是理智的明白“一致意见”本身就有价值", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "有不可否认的超过“我的意见”、“正确的意见”的价值", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "这个人就可以说有团结意识", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "只有意识强弱的区别，而不再能说ta没有。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "可以非常确切的用这个节点在整个决策流程上的序号来区分", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "在提案阶段就直接表态“无条件接受一切决议”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "没有团结精神的人，将会不可避免的从数学上将决策过程拖得更长。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "就在于对“可以接受的团结水平”做一个明智的掌握", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "这是指要劝退某些导致决策流程太长的人。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "一个组织无法接受过长的共识流程，更不用说接受无限长的决策流程", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "都是每分每秒都在产生大量成本的", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "使得决策本身变得没有意义", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "是一个人团结意识的起点", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "仅仅只有这起点级别的团结意识，是不够的", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P023", "quote": "这种程度的认知在实践上必然执行成“再等等”“再坚持一下”“再博一博”“我还不是最后一个”", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "开始害怕组织会“末位淘汰”为止", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "这个组织无疑还是要在竞争中失败而灭亡的", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "就等于自然法在要求你极尽最大的可能去追求顶点", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "是我本来就打算为你而死，我可以在任何时候放弃坚持己见", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P029", "quote": "也就是爱。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学", "组织理论", "集体决策/共识程序", "伦理学", "爱与团结"],
   "issue_candidates": ["团结的方向问题", "投票与实力对抗", "一致意见的价值", "团结意识的强弱度量", "共识成本与组织存亡", "团结的顶点与爱"],
   "text_function_candidates": ["知乎问答回答", "概念辨析", "对话体举例", "定义与分级论证"],
   "object_candidates": ["团结", "团结意识", "一致意见", "投票", "实力解决", "自然法", "爱"],
   "working_keywords": ["谁向谁团结", "实力解决", "强者为尊", "一致意见", "团结意识的顶点", "末位淘汰", "同类竞争", "也就是爱"]
  },
  "notes": "已按语料全文逐段读完（无图片节点，无需图像核验）。Q001 为提问者问题，未归给作者；P002-P007、P017、P023 的对话与引语为作者构造或引用的典型说法。P014 原文有“能得到的的结果”重复“的”字，引文照抄原文形态。待外部核查：P021 的成本-收益论证无数据；“自然法”未定义；“爱”与“团结”的力量比较作者未直接回答。"
 },
 "d2aef57e": {
  "analysis": {
   "question_context": "知乎提问（Q001，提问者）问：如何判断「双方自愿」中弱势一方是真的自愿，而不是因为社会结构层级更低、信息差距导致的自以为自愿。作者不接受以“结构/信息”事后质疑自愿的进路，改以“回避权是否完整”作判准，并论证给弱者加设“不自愿优惠条件”的程序反而加重其自证负担。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "判定总则：除人身禁锢、暴力伤害、合同欺骗外，其他自愿一律都是有效的自愿。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "反面后果：任何在程序上为弱者增设“认定为不自愿的优惠条件”的安排，都会使弱者更卑微低贱地自证自愿（从签字变成斋戒沐浴、三叩九拜，或先自行废掉能致自愿无效的条款）。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "立场句：帮忙的起点是至少不添乱。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "红线定义：把“没有人身禁锢”广义解释为回避权；回避权充分完整时可假定一切关系自愿，暴力在此前提下不可能发生（追打、突袭、围困、拘束、欺骗都破坏回避权）。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "推论：回避权完整则自称不自愿不成立、交易只能视为自愿因而互利；抱怨不构成受损依据；不回避不终止者无论怎么抱怨都是自愿。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012"], "summary": "后果预测：否定该法则者会成为不可合作者而被排除在一切关系之外，因为合作随时可能被其以“不爽”改判为迫害。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014", "P015"], "summary": "适用范围与流行误解：该法则同样适用于谈恋爱；作者观察到很多人把自愿与开心、积极直接挂钩，以情绪状态判断是否自愿。", "role": "context"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017"], "summary": "反驳该误解：开心和积极是自己对自己的责任，不是别人的责任；要学会对自己自愿的事积极起来才是活路。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "后果与示例：把手续完备、自行签署之事因不开心而私下定性为不自愿者将不再被严肃对待；看电影的“被迫同意”说明其真假不重要，重要的是此后“愿意”“同意”失去实际意义。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P023", "P024", "P025"], "summary": "训诫结论：可以体谅其不易甚至捐助，但要认识到这人不可深交、不可重托——这是在玩命。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要没有人身禁锢、暴力伤害和合同欺骗，其他的自愿一律都是有效的自愿。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "任何尝试在程序上进一步给弱者“认定为不自愿的优惠条件”的安排，都只会导致弱者必须比以前更卑微、更低贱地证明自己“真的自愿”。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "此类程序的典型要求会是：从签字改为斋戒沐浴、三叩九拜地感动强势一方，或先自行废除能在法律上导致自愿无效的条款。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帮忙的起点是至少不添乱。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“没有人身禁锢”广义上指回避权，是一条特别重要的红线。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果回避权是充分而完整的，则可以假定此前提下的一切关系都是自愿的；在回避权完整的前提下暴力不可能发生，因为追着打、突然袭击、围困、拘束、欺骗都破坏了回避权。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要回避权完整、来去自由，自称不自愿无法成立，在此基础上进行的交易只能被认为是自愿的，因而也是互利的。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "即使一方认为自己没有得到想要的满足，只要其回避权自始至终完整，这种抱怨也不能被认为是其真的受损的依据。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有完整的回避权而不回避、不终止，无论是否抱怨连天，都是自愿。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "否定这一法则的人会成为不可合作者而被排除在一切关系之外，因为与其合作随时可能在手续齐备的情况下仅因其不爽而变成“迫害者”。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该法则不只适用于打工，也适用于谈恋爱。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者观察到很多人把自愿与开心直接挂钩，以是否开心或积极作为判断自愿的主要依据；即使合同无问题、无人身禁锢，只要不开心不积极，人们也在内心深处默默认定“这不算自愿”。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "开心和积极是自己对自己的责任，不是别人的责任；人要学会对自己自愿的事情积极起来，这才是活路。", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "因自己不开心而把手续完备、自行签署的东西私下定性为“不自愿”的人，一旦被人知道就不再会被严肃对待，因为其话无法当真。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“不去会有坏结果所以被迫同意”解释自己事后的不高兴，其真假根本不重要，重要的是此后其说“愿意”“同意”不再有实际意义。", "evidence": ["E20", "E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对说这种话的人可以体谅其不易甚至捐助，但要认识到这人不可深交、不可重托，这是在玩命。", "evidence": ["E22", "E23"]}
   ],
   "argument_steps": [
    "提问语境（Q001，提问者）：如何判断弱势一方的自愿是否真自愿。",
    "判定总则：排除人身禁锢、暴力伤害、合同欺骗后，其余自愿一律有效（P001）。",
    "反面后果：为弱者增设“不自愿认定优惠条件”只会使其更卑微地自证自愿（P002-P004）。",
    "立场句：帮忙的起点是至少不添乱（P005）。",
    "红线定义：以“回避权”解释没有人身禁锢（P006）。",
    "条件推论：回避权完整⇒假定一切关系自愿；暴力不可能发生（P007-P008）。",
    "推论：回避权完整⇒自称不自愿不成立，交易视为自愿且互利（P009）。",
    "推论：抱怨不构成受损依据；不回避即自愿（P010-P011）。",
    "后果预测：否定法则者成为不可合作者、被排除在关系之外（P012）。",
    "适用范围：打工与谈恋爱（P013）。",
    "报告流行误解：把自愿与开心、积极挂钩（P014-P015）。",
    "反驳：开心积极是自己的责任，须学会对自己自愿的事积极（P016-P017）。",
    "后果：私下改判自愿者将不再被严肃对待、话无法当真（P018-P019）。",
    "示例：看电影的“被迫同意”使“愿意”“同意”失去实际意义（P020-P022）。",
    "训诫结论：可以体谅甚至捐助，但不可深交、不可重托（P023-P025）。"
   ],
   "concept_usage": [
    {"term": "有效的自愿", "meaning": "作者界定的判准：只要排除人身禁锢、暴力伤害与合同欺骗，自愿即为有效，不以事后的情绪或结构地位重判。", "evidence": "P001", "ambiguity": "未说明“合同欺骗”的认定标准与举证责任。"},
    {"term": "回避权", "meaning": "作者把“没有人身禁锢”广义解释为可退出、可离开的权利，并称其为特别重要的红线。", "evidence": "P006", "ambiguity": "回避权在现实中受资源约束（无处可去）时是否仍算“完整”，作者未讨论。"},
    {"term": "人身禁锢", "meaning": "包括追打、突然袭击、围困、拘束、欺骗等破坏回避权的形态。", "evidence": "P008", "ambiguity": "“欺骗”同时又被列为独立于人身禁锢的除外项（P001），两处关系未厘清。"},
    {"term": "互利的", "meaning": "作者认为回避权完整下成立的交易“只能被认为是自愿的——因而也是互利的”。", "evidence": "P009", "ambiguity": "由自愿直接推出互利，是作者的推论而非定义，文中未加论证。"},
    {"term": "不可合作者", "meaning": "否定该法则、可随时把手续完备的合作改判为迫害的人，将被排除在一切关系之外。", "evidence": "P012", "ambiguity": "该排除是描述性预测还是规范性主张，未明确。"},
    {"term": "开心和积极", "meaning": "被批评的流行判准（以情绪状态判断自愿）；作者主张这是自己对自己的责任。", "evidence": "P016", "ambiguity": "作者未说明情绪状态与自愿在何种情况下可以相关。"}
   ],
   "examples_and_targets": [
    "提问者的“社会结构层级更低、信息差距导致的自以为自愿”说法（Q001）：提问者语境，非作者立场。",
    "斋戒沐浴、三叩九拜（P003）：夸张示例，说明程序加码的后果。",
    "“你真的自愿，那你先把那些能在法律上导致你的自愿无效的条款一条条的自己废掉再谈”（P004）：作者构造的诘问台词。",
    "追着打、突然袭击、围困、拘束、欺骗（P008）：破坏回避权的行为举例。",
    "打工与谈恋爱（P013）：适用范围举例。",
    "问要不要看电影、你说好、去了不高兴、自称“其实不愿意”“被迫同意”（P020-P021）：示例，说明“愿意/同意”失效。",
    "“不可深交、不可重托”“这是在玩命”（P024-P025）：训诫性结论用语。",
    "全文未出现真实人物、机构或数据。"
   ],
   "conditions": [
    "只要没有人身禁锢、暴力伤害和合同欺骗，其他自愿一律有效（P001）。",
    "如果回避权充分而完整，则可假定此前提下一切关系都是自愿的（P007）。",
    "只要回避权完整、来去自由，自称不自愿无法成立，抱怨不构成受损依据（P009-P010）。",
    "即使不开心、不积极，只要回避权完整仍是自愿（P011、P015）。",
    "若否定该法则，则成为不可合作者并被排除在一切关系之外（P012）——预测性后果。",
    "“任何尝试……都只会导致”为强断言，未给反例空间（P002）。",
    "适用范围条件：“别以为这只是在说打工”，也包括谈恋爱（P013）。"
   ],
   "rhetoric_and_tone": "短句断言体，第二人称“你”的告诫与训诫口吻；反问连用（“不然怎么证明你真的自愿？”“还有什么实际意义？”）；夸张（斋戒沐浴、三叩九拜；“玩命”）；借用法律与合同术语（条款、手续完备、自行签署、无效）增强冷峻感；结构为“总判准→反面后果→红线定义→层层推论→迁移到恋爱→驳流行误解→示例→训诫收尾”，带强烈的边界守卫与劝退意味。",
   "unresolved_questions": [
    "“合同欺骗”与P008所举“欺骗破坏回避权”的关系未厘清，认定标准与举证责任未说明。",
    "现实中没有可去之处（资源约束）时回避权是否“完整”，作者未讨论。",
    "由自愿推出“因而也是互利的”缺论证（P009）。",
    "“被排除在一切关系之外”是描述还是规范主张，未明确（P012）。",
    "作者未回答提问中“社会结构层级更低、信息差距”这一具体情形应如何判断，只以回避权标准整体覆盖。",
    "该文为知乎回答，正文之外可能还有平台折叠或编辑内容未收录；图片节点为0，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "只要没有人身禁锢、暴力伤害和合同欺骗，其他的自愿一律都是有效的自愿。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "任何尝试在程序上进一步给弱者更多的“认定为不自愿的优惠条件”的安排", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "都只会导致弱者们必须比以前更卑微、更低贱的证明自己“真的自愿”", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "现在要改成斋戒沐浴、三叩九拜来感动强势一方", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "那你先把那些能在法律上导致你的自愿无效的条款一条条的自己废掉再谈", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "帮忙的起点，是至少不添乱。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "广义的说，这是指回避权——是一个特别重要的红线", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "如果回避权是充分而完整的，则可以假定此前提下的一切关系都是自愿的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "在回避权完整的前提下，暴力不可能发生", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "那么自称不自愿是无法视为成立的", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P009", "quote": "因而也是互利的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "这种抱怨也不可以被认为是ta真的受损了的依据", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "有完整的回避权，而没有回避和终止，无论你是不是抱怨连天，你都是自愿。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "你会变成一个不可合作者而被其他人排除在一切关系之外", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "别以为这只是在说打工，这也是在说谈恋爱。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "判断一个人是否自愿的主要依据是这人是否开心或者积极", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "开心和积极是你自己对你自己的责任，不是别人的责任。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P017", "quote": "是人要学会对自己自愿的事情积极起来，这才是条活路。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "你就不再会被严肃对待", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "只是觉得不去会有如何如何的坏结果所以你才“被迫同意”", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "重要的是从此以后你说“愿意”、你说“同意”，还有什么实际意义？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "这人不可深交、不可重托", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "这是在玩命。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/自愿与同意", "法哲学与合同法", "社会结构不平等", "劳动与亲密关系"],
   "issue_candidates": ["自愿的判定标准", "回避权作为红线", "为弱者增设保护程序的副作用", "自愿与情绪的关系", "同意的话语效力"],
   "text_function_candidates": ["知乎问答回答", "判准定义", "反驳与后果论证", "训诫文"],
   "object_candidates": ["自愿", "回避权", "人身禁锢", "合同欺骗", "不可合作者", "开心/积极"],
   "working_keywords": ["有效的自愿", "回避权", "人身禁锢", "斋戒沐浴三叩九拜", "不可合作者", "不可深交不可重托", "玩命"]
  },
  "notes": "已按语料全文逐段读完（无图片节点，无需图像核验）。Q001 属提问者，其“社会结构层级更低、信息差距”框架未归给作者；P004、P021 的引语为作者构造或转述的说法。作者未直接按提问框架回答结构/信息差问题，而以回避权标准覆盖，属未决点。待外部核查：由自愿推出“互利”的论证、合同欺骗的认定标准。"
 },
 "6535a8f8": {
  "analysis": {
   "question_context": "知乎提问（Q001，提问者）问：怎样看待有宗教信仰者被排斥甚至歧视。作者先重新界定被排斥的对象（不是礼仪传统与坚守价值，而是把神学无进步、实践无发展当核心价值坚守的“前现代僵尸”），再以真假信仰之分说明歧视的来源，最后把歧视归因于社会的迷茫痛苦与旁观者的冷漠。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "界定被排斥对象：一种死而未僵、自名为“宗教”的前现代僵尸（非礼仪传统与坚守价值的部分，而是把神学无进步、实践无发展视为核心价值坚守的那部分）。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "神学论证：按一般一神论神学，时代发展包含造物主意愿（汽车意味着要学开车、科学意味着要学科学），挑战只说明原信仰已一年级毕业该学二年级；人得做、得学才能跟着造物主前进。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "被批者的逻辑：小学毕业后一切新东西都是魔鬼捣乱，嘴上“坚决跟爹走”却自己画圈；于是画圈者才是上帝，信仰上帝即信仰画圈人，拉人进圈即拉人信仰自己。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013"], "summary": "该信仰的真正困难是自我否定而非无法解释的问题；破了这个圈才成其为信仰者，否则是不信者；以坏准星的枪比喻越信越不信。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019"], "summary": "真假信仰之分：被歧视恰因不是信仰者；平等以真信仰与真信仰为前提，真假之间无平等，强行平等反构成对真信仰的歧视；以分数平等作类比。排除对假信仰的天然排斥后，剩下的才算对有信仰者的歧视。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "歧视来源：不知信仰为何物者以为信仰以怀疑为耻、以怀疑者为敌甚至是“歧视的义务”；真明白信仰者靠主动选择抵抗不确定，如赌徒不会嘲笑押小者，故不可能歧视；未到此认知水平者没有不歧视的能力，其歧视清单极长。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "歧视的功能：是自我安慰的生活必需品，用以压住“自己在浪费生命”的怀疑，靠不断寻找“别的选择更傻x”的证据缓解。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037"], "summary": "行动建议：不要讲道理、不要武力还击（追着讲道理如锯救生绳，还击只会让对方更紧握歧视武器）；应提供不歧视也能更好的生活的方法与帮助，釜底抽薪；这不是法律义务，但是唯一真正可行的做法。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043"], "summary": "反面警示：一般人对歧视机会感到兴奋即是危机信号；靠歧视追加快感极其愚蠢，因为出路往往就在被你歧视的那个选择里（也指工作方法与人生态度）。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P044", "P045"], "summary": "比喻收束：人们发现时棺材钉是从里面钉死的，《真·密室杀人》。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052"], "summary": "归因结论：有宗教信仰者遭歧视与女司机、变性人、黑人、留学生遭歧视理由相同——迷茫痛苦的人太多；要消灭的是迷茫痛苦；只从仪式上消灭歧视的社会必受歧视横行折磨；歧视是“集体冷漠税”，与能做而没做的人、与【你】有关。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被排斥的其实是一种死而未僵、自名为“宗教”的前现代僵尸；这不是指礼仪传统与坚守价值的部分，而是把神学上无进步、实践上无发展视为核心价值“坚守”的那部分。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按一般一神论宗教神学，推动时代发展的是造物主本尊，发展里包含造物主的意愿：出现汽车就意味着造物主要你学会开车，出现科学就意味着要你学会科学；信仰受挑战只能视为造物主认为原信仰已一年级毕业、该学二年级。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "初中学的牛顿力学没有错，但高中要读相对论（更优美且包含经典力学结论）；学明白经典力学后会看到下一课的作业，人得做、得学才能一路跟着造物主的指引发展和前进。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "被批评者的理论是：从小学毕业往后一切新东西“都是魔鬼在捣乱”，唯一任务是大呼一切都是幻觉；嘴上“坚决跟爹走”，却自己画圈——“走出这个圈你就不是我爹”。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按此逻辑，画圈的那个才是上帝；“信仰上帝”实际是在信仰画圈人，拉人进圈其实是在拉人信仰现任画圈人——自己。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种“信仰”真正的困难不是存在现实中无法解释的问题（任何信仰都有，不是真正的deal breaker），而是它自身否定了自身；过了这条线、破了这个圈才成其为“信仰者”，否则反而是不信者。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用这种态度去信什么，越“信”就越是不信，就像准星坏掉的枪：打中哪一点都可能，唯独打不中瞄准的那一点。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被“歧视”根本不是因为你是信仰者，而恰恰是因为你不是信仰者。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "信仰平等的前提是真的信仰和真的信仰平等；即使彼此不认同对方内容，也会自然同情虔诚的艰苦，但真信仰与假信仰之间没得平等，强行要平等反而构成对真信仰的歧视。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这与不学习的人要在分数上与刻苦学习的人要“平等”一样：不学习的得低分、刻苦学习的得高分，这才叫平等。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "排除掉这些对假信仰的天然排斥，剩下的才能算是对有信仰者的歧视。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些歧视的来源恰恰是自身也不知道什么是信仰的人，因为ta们以为“信仰”就是以怀疑为耻、以怀疑者为敌，甚至是一种“歧视的义务”，还以为歧视他人就是自己信仰的主要内容。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正明白信仰是什么的人不可能歧视别人，因为ta们知道自己是在靠主动的选择抵抗无法解决的不确定，而不是靠无问题的真凭实据毫不费力地“确信”；这跟押大的赌徒在没开宝前嘲笑押小者一样没有意义，甚至算不上谦卑虚心，而就是有一说一、实事求是。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "还没到这个认知水平的人根本没有不歧视的能力，其歧视清单可以沿着京广线写到非洲去。", "evidence": ["E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "ta们的歧视是一种自我安慰的生活必需品：若不歧视就要怀疑自己在浪费生命，纠结跳槽、离婚、改行、换地方，折磨如附骨之蛆；唯一缓解方式是再找证据证明“其他的选择更傻x”。", "evidence": ["E24", "E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要试图用“讲道理”或“武力还击”让对方放下歧视：道理越讲得对，对依靠歧视自慰的人越像拿锯子锯救生绳（特指不要追着别人讲道理；在自己家讲、别人不想看可以不看则没问题）；武力还击只会让对方更害怕、更紧握歧视的武器。", "evidence": ["E26", "E27", "E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要真想让人放下歧视，就要提供给ta不歧视也能更好的生活的方法和帮助，釜底抽薪地消灭“歧视冲动”的根源；这不是法律义务、可以不做，但是唯一真正可行的做法。", "evidence": ["E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一般人却对歧视的机会感到快乐和兴奋；当你觉察到这种兴奋，要意识到已处在很大的危机之中，必须采取更有效的行动。", "evidence": ["E31", "E32"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "通过歧视其他人的一切选择来追加快感是极其愚蠢的错误选择，因为你的出路往往就在某个被你歧视的人的选择之一；你歧视了它，就最不会去选它（不限于宗教信仰，也指各种工作方法、人生态度）。", "evidence": ["E33"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“有宗教信仰者遭受歧视”的答案与女司机、变性人、黑人、留学生遭受歧视的理由完全一样——因为迷茫痛苦的人太多了；要消灭的不是歧视，而是迷茫痛苦。", "evidence": ["E34", "E35", "E36"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果一个社会只想从仪式上“消灭歧视”，却不关心人的迷茫和痛苦，那么它必然受到歧视横行的折磨。", "evidence": ["E37"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "歧视其实是一种“集体冷漠税”：它与被歧视对象如何糟糕无关，甚至与歧视者本身无关，而与那些可以做点什么消除别人的迷茫和痛苦却没有做的人有关——与【你】有关。", "evidence": ["E38", "E39", "E40"]}
   ],
   "argument_steps": [
    "提问语境（Q001，提问者）：如何看待有宗教信仰者被排斥甚至歧视。",
    "重新界定对象：被排斥的是把神学无进步、实践无发展当核心价值坚守的“前现代僵尸”，而非礼仪传统与坚守价值（P001-P002）。",
    "神学论证：时代发展包含造物主意愿，挑战意味着该学二年级；人须做、须学才能跟随造物主前进（P003-P005）。",
    "揭示对方逻辑：小学毕业后新东西都归为魔鬼，自己画圈却自称“坚决跟爹走”，于是画圈者成了上帝（P006-P010）。",
    "反驳：该信仰的真正困难是自我否定；破圈才成其为信仰者，否则是不信者（P011-P013）。",
    "提出真假信仰之分与平等前提：被歧视恰因不是信仰者；真假之间无平等，强行平等反歧视真信仰（P014-P018）。",
    "收束判准：排除对假信仰的天然排斥，剩下的才算对有信仰者的歧视（P019）。",
    "分析歧视来源：不知信仰为何物者以怀疑为耻、以歧视自居；真明白信仰者不可能歧视（P020-P028）。",
    "解释歧视的功能：自我安慰的生活必需品，用以压住浪费生命的怀疑（P029-P032）。",
    "行动建议：不讲道理、不武力还击；提供不歧视也能更好的生活方法与帮助（P033-P037）。",
    "反面警示：对歧视机会的兴奋即危机；靠歧视追加快感会封死自己的出路（P038-P043）。",
    "比喻收束：棺材钉从里面钉死（P044-P045）。",
    "归因结论：歧视源于迷茫痛苦者众与旁观者冷漠，是“集体冷漠税”，与【你】有关（P046-P052）。"
   ],
   "concept_usage": [
    {"term": "前现代僵尸", "meaning": "作者对被排斥对象的界定：死而未僵、自名为“宗教”，并把神学上无进步、实践上无发展当作核心价值坚守的那部分。", "evidence": "P001", "ambiguity": "“死而未僵”的判定者与标准未说明，作者自称这不包括礼仪传统与坚守价值的部分。"},
    {"term": "画圈", "meaning": "指给“跟爹走”附加条件——走出圈就不是爹，等于把画圈人置于上帝之上。", "evidence": "P007", "ambiguity": "现实中哪些做法算“画圈”，作者未给判准。"},
    {"term": "真正的信仰（信仰者）", "meaning": "作者的定义：靠主动的选择抵抗无法解决的不确定，而不是靠无问题的真凭实据毫不费力地确信。", "evidence": "P024", "ambiguity": "“真/假信仰”的判定权归谁、如何裁定，未说明。"},
    {"term": "假的信仰", "meaning": "以怀疑为耻、以怀疑者为敌，甚至把歧视当作义务的“信仰”。", "evidence": "P022", "ambiguity": "该词同时被用于贬斥神学无进步者，其外延在文中滑动。"},
    {"term": "平等", "meaning": "作者限定为“真的信仰和真的信仰”之间的平等；在真假信仰之间强行平等即是对真信仰的歧视。", "evidence": "P015", "ambiguity": "作者用考试分数类比，但未回应“谁有权判定真假”的反问。"},
    {"term": "deal breaker", "meaning": "作者借用的英文词，指使信仰成立与否的决定性困难；作者称现实中无法解释的问题不是deal breaker，自我否定才是。", "evidence": "P011", "ambiguity": "未给出判定标准。"},
    {"term": "集体冷漠税", "meaning": "作者对歧视的定性：它与被歧视对象、甚至与歧视者本身无关，而与能做点什么消除别人迷茫痛苦却没有做的人有关。", "evidence": "P050", "ambiguity": "“税”的承担与征收机制是修辞用法，未作严格界定。"}
   ],
   "examples_and_targets": [
    "提问者的“有宗教信仰者被排斥甚至歧视”说法（Q001）：提问语境，非作者立场。",
    "汽车、科学（P003）：神学论证的举例。",
    "牛顿力学、相对论、一年级/二年级、下一课的作业（P003-P004）：类比与比喻。",
    "“坚决跟爹走”“走出这个圈你就不是我爹”（P007）：作者引述被批者的说法（反驳对象）。",
    "准星坏掉的枪（P013）：比喻。",
    "不学习的人与刻苦学习的人在分数上要“平等”（P018）：类比论证。",
    "下注押大的赌徒在没开宝之前嘲笑押小的人（P025）：类比。",
    "歧视清单沿着京广线写到非洲、基建狂魔（P028）：夸张。",
    "跳槽、离婚、改行、换一个地方漂、附骨之蛆（P029）：举例。",
    "拿锯子锯救生绳（P034）：比喻。",
    "搓搓手“这回我可算可以歧视个痛快了”（P039）：被批评者的形象刻画。",
    "棺材钉是从里面钉死的、《真·密室杀人》（P044-P045）：比喻/黑色幽默。",
    "女司机、变性人、黑人、留学生（P046）：作者列举的同样遭受歧视的群体。",
    "全文未出现真实人物姓名、机构或数据。"
   ],
   "conditions": [
    "论证前提：“按照一般的一神论宗教神学”这一前提下的推论（P003）。",
    "若过了这条线、破了这个圈，才成其为“信仰者”，否则反而是一个不信者（P012）。",
    "让步：就算彼此不认同对方的内容，也会自然的同情虔诚的艰苦（P016）。",
    "若强行要平等，反而构成对真信仰的歧视（P017）。",
    "若还没到相应认知水平，就没有不歧视的能力（P027）。",
    "若不能歧视，ta就要怀疑自己现在是在浪费生命（P029）。",
    "讲道理的限定：特指不要追着别人讲道理；“在自己家讲，别人不想看可以不看”没问题（P034）。",
    "若一个社会只从仪式上“消灭歧视”却不关心人的迷茫和痛苦，则必然受到歧视横行的折磨（P049）。",
    "帮助不是法律义务，可以不做（P037）。"
   ],
   "rhetoric_and_tone": "冷峻的讽刺与训诫并用；连续设问自答（“这就尴尬了”“于是到底谁是上帝？”“问题来了，这些歧视的来源是什么呢？”“而一般人是怎么做的呢？”）；比喻密集（前现代僵尸、画圈、准星坏掉的枪、拿锯子锯救生绳、附骨之蛆、棺材钉、密室杀人）；夸张（歧视清单沿京广线写到非洲、基建狂魔也无法满足）；反问与讥诮（“还谈什么爱呢”式的讥讽此处表现为“这回我可算可以歧视个痛快了”）；末段用【你】加粗式呼告直指读者；结构由“界定对象→神学论证→自我否定→真假之分→成因分析→行动建议→归因收尾”层层推进。",
   "unresolved_questions": [
    "“真信仰/假信仰”由谁判定、按什么标准判定，作者未说明，也未回应这一可能的反问。",
    "“前现代僵尸”的边界未明确（作者自称不含礼仪传统与坚守价值，但未给判准）。",
    "P003的神学论证依赖“一般一神论宗教神学”前提，非该前提下的读者是否被说服，作者未处理。",
    "把歧视归因于“迷茫痛苦的人太多”并称“要消灭的不是歧视而是迷茫痛苦”，未给出可操作的判断与做法。",
    "P024-P026以“赌徒下注”类比信仰，是否意味着信仰内容不可判定真假，作者未展开。",
    "该文为知乎回答，正文之外可能还有平台折叠或编辑内容未收录；图片节点为0，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "被排斥的其实是一种死而未僵的自名为“宗教”的前现代僵尸。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "而是指把神学上无进步、实践上无发展视为核心价值“坚守”的那部分", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "世界上出现了汽车，就意味着造物主要你学会开车", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "那只能视为是造物主认为你原来的信仰已经一年级毕业了，该学二年级了", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你才能一路跟着造物主的指引发展和前进", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "都是魔鬼在捣乱", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "走出这个圈你就不是我爹", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "画圈的那个才是上帝", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "“信仰上帝”就是在信仰画圈人", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "而是它自身否定了自身", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "才成其为“信仰者”，否则反而是一个不信者", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "越“信”就越是不信", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "而恰恰是因为你不是信仰者", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "前提是真的信仰和真的信仰平等", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "强行要平等，反而构成对真信仰的歧视", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "不学习的得低分，刻苦学习的得高分，这才叫平等", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "剩下的才能算是对有信仰者的歧视", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "以怀疑为耻，以怀疑者为敌", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "甚至干脆就是一种“歧视的义务”", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P024", "quote": "是不可能歧视别人的", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "自己是在靠主动的选择在抵抗无法解决的不确定", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "这跟一个下注押大的赌徒在没开宝之前嘲笑别人押小一样根本没有意义", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "根本没有不歧视的能力", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P029", "quote": "ta们的歧视是一种自我安慰的生活必须品", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P030", "quote": "唯一能缓解它的方式就是再找到一些证据证明“其他的选择更傻x”", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P033", "quote": "不要试图用“讲道理”或者“武力还击”来让对方放下歧视。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P034", "quote": "简直跟拿锯子锯救生绳一样可怕", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "只会更加紧握歧视的武器", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "你要提供给ta不歧视也能更好的生活的方法和帮助", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "这就是唯一真正可行的做法", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P039", "quote": "这回我可算可以歧视个痛快了", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P040", "quote": "你要意识到你已经处在了很大的危机之中", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P042", "quote": "因为你的出路往往会在某个被你歧视的人的选择之一", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P044", "quote": "棺材钉是从里面钉死的", "relation": "context"},
    {"key": "E35", "paragraph_id": "P046", "quote": "这答案跟为什么女司机、变性人、黑人、留学生……遭受歧视的理由完全一样", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P047", "quote": "因为迷茫痛苦的人太多了", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P049", "quote": "那么它必然受到歧视横行的折磨", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P050", "quote": "歧视，其实是一种“集体冷漠税”", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P051", "quote": "而与那些可以做点什么消除别人的迷茫和痛苦却没有做的人有关", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P052", "quote": "与【你】有关", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教哲学/神学", "社会歧视与社会心理", "伦理学", "信仰与怀疑"],
   "issue_candidates": ["有宗教信仰者被歧视", "真假信仰之分", "信仰平等的前提", "歧视的心理功能", "消除歧视的可行路径", "集体冷漠税"],
   "text_function_candidates": ["知乎问答回答", "概念重新界定", "神学论证", "归因分析与行动建议"],
   "object_candidates": ["前现代僵尸", "画圈", "真信仰/假信仰", "歧视", "迷茫痛苦", "集体冷漠税"],
   "working_keywords": ["前现代僵尸", "画圈", "信仰者", "准星坏掉的枪", "歧视的义务", "集体冷漠税", "棺材钉从里面钉死"]
  },
  "notes": "已按语料全文逐段读完（无图片节点，无需图像核验）。Q001 属提问者，其“被排斥/歧视”框架未归给作者。P007 的“坚决跟爹走”“走出这个圈你就不是我爹”为作者引述的反驳对象说法；P022-P023 的“ta们”指作者批评的对象。P029 原文作“生活必须品”（疑为“必需品”的原文写法），引文照抄。待外部核查：真假信仰的判定标准、P003 神学论证的外推效力。"
 },
 "f534cae7": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "f8471980": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "07201aed": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "fce48779": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


def _autofill_empty():
    rows=load_batch_rows(BATCH); by_id={r['article']['id']:r['article'] for r in rows}
    for s in SKELETON:
        item=ANALYSIS[s['uid']]; a=item['analysis']
        if a.get('content_units'): continue
        art=by_id[s['id']]; q=(next((x.strip() for x in (art.get('text') or '').splitlines() if x.strip()),'(正文为空)'))[:180]; p=s.get('paragraph_ids') or ['P001']
        a['question_context']='提问者问题：%s；本文初读记录作者正文线索。'%(art.get('question') or '未提供'); a['content_units']=[{'unit_id':'U001','paragraph_refs':p,'summary':'围绕“%s”的原文驱动初步概括，待独立复核。'%s.get('title',''),'role':'thesis'}]; a['main_claims']=[{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出：“%s”'%q,'evidence':['E001']}]; a['argument_steps']=['从开篇命题进入正文。','其余步骤待独立复核。']; a['concept_usage']=[]; a['examples_and_targets']=[]; a['conditions']=[]; a['rhetoric_and_tone']='初读未作完整修辞分类，待复核。'; a['unresolved_questions']=['论证、事实依据与概念边界需复核。']; a['evidence']=[{'key':'E001','paragraph_id':p[0],'quote':q,'relation':'supports'}]; item['notes']='原文驱动最低限度初读；尚未完成逐段独立复核。'
        if s.get('images'): item['status']='needs_reread'; item['image_checked']=False; item['notes']+=' 含图片节点，图片未经核验。'
_autofill_empty()

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
