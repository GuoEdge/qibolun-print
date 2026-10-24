# -*- coding: utf-8 -*-
"""批次 r001-b0033 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0033.sessions.py            # 写 out/r001-b0033.out.jsonl
  python3 records/r001-b0033.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0033"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0033.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "3f9030f5": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场，非作者主张）问：为什么自己的 3D 打印机喷头出不来料，而且手动把料退出来时“是这样的（见图）？？？”。作者不复述图片、不给维修步骤，而是直接给出可能故障并解释成因。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "给出故障归因：喷头加热部件坏了，也可能是温度探头坏了。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "按因果链解释现象：材料温度不够、未融到足够流动性，送料轮仍强行作业往送料管硬塞，前端还是固体挤不出去，于是成这样。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者判断故障可能是喷头的加热部件坏了，也可能是温度探头坏了（以“可能”并列两种故障，未排除其他原因）。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者解释成因：材料没有足够温度、没有被融化到足够的流动性，送料轮强行作业把料硬塞进送料管，而前头还是固体、根本挤不出去。", "evidence": ["E002"]}
   ],
   "argument_steps": [
    "由提问描述的现象直接给出两个可能故障点（加热部件、温度探头）。",
    "按“材料温度不足→未达足够流动性→送料轮强行送料→前端仍为固体→无法挤出”的顺序解释现象。"
   ],
   "concept_usage": [
    {"term": "加热部件", "meaning": "喷头上负责加热的部件，作者列为可能故障点之一", "evidence": "P001", "ambiguity": "未说明具体部件与检验方法"},
    {"term": "温度探头", "meaning": "测温部件，作者列为另一个可能故障点", "evidence": "P001", "ambiguity": "未说明两种故障如何区分"},
    {"term": "流动性", "meaning": "材料被加热融化后足以被挤出的状态", "evidence": "P002", "ambiguity": "未给出温度、材料等定量条件"}
   ],
   "examples_and_targets": [
    "3D 打印机喷头堵料现象（提问者提供的问题材料，作者据此作答）",
    "送料轮、送料管、喷头（作者说明用的部件名称，非外部事例）"
   ],
   "conditions": [
    "以提问者描述的现象为前提；作者用“可能”并列两个故障点，未断言必为其中之一。",
    "解释链以“材料没有足够的温度”为起点，未说明适用机型、材料与温度范围。"
   ],
   "rhetoric_and_tone": "直述式答疑，两句即止；无称呼、无修辞铺陈，以“根本挤不出去”“就会成这样了”作口语化收束。",
   "unresolved_questions": [
    "提问称“（见图）”，但本篇正文与 lexical 均无图片节点，提问所指图片未随本篇语料提供，现象无法与图核对。",
    "作者未说明两个可能故障的判别方法与维修建议，也未说明适用的机型与材料。",
    "“成这样了”所指的具体形态只能由提问图片确定，本篇未作描述。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "喷头的加热部件坏了，也可能是温度探头坏了。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "材料没有足够的温度，还没有被融化到足够的流动性，送料轮就强行作业了", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["3D打印/设备故障"],
   "issue_candidates": ["喷头不出料的成因", "加热部件与温度探头故障"],
   "text_function_candidates": ["答疑", "故障诊断"],
   "object_candidates": ["3D打印机喷头", "加热部件", "温度探头", "送料轮", "送料管"],
   "working_keywords": ["喷头", "加热部件", "温度探头", "流动性", "送料轮"]
  },
  "notes": "正文仅两句，与 brief 同源（brief 为正文的截断预览）。提问提到“见图”，但本篇 lexical 无 image 节点、无图片节点，图片未随语料提供，已记入 unresolved_questions；本篇按无图片文章处理，status=read。"
 },
 "cc326f77": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：猫科动物战斗力那么强，为什么没有将犬科动物淘汰掉？作者不直接回答淘汰问题，而是先反驳该问题下以“犬科狩猎成功率更高”为依据的流行论证与“猫科只会咬喉咙”的说法，最后给出自己的解释：能占据最优狩猎场、不必长途追随猎物本身就是优势，并提醒解读统计数据要想深一点。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "以反问质疑比较猫科与犬科狩猎成功率时未按犬群数量折算；用一头花豹捕一头羊（50%）与四头狼捕一只羊（70%）的算例讽刺把群体成功率算成每头都成功，并指出猎获要分四份、需出动四人次，末尾要对方再算算。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P007"], "summary": "主张该比较应改比费效比，以单个狙击手与整个步兵班的命中率作比。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "反驳“猫科只会咬喉咙”“必须紧紧咬着否则猎物跑掉”：称凭咬合力与体力可直接从后方咬断颈椎，长牙长爪配合强肌肉本身足以致命，并反问受伤的猎物能逃到哪去。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013"], "summary": "提出物种谁先消失与谁弱小无关、输给大自然是另一回事，并以火山喷发烧死项羽而韩信出差的假设讽刺该逻辑不通。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015"], "summary": "给出作者的正面解释：有能力凭暴力割据最好用的狩猎场、每天步行两个街区即可打猎，以及只追一公里、失败率全班第一却日子照过、每天睡十几个小时，都是优势地位的表现。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016"], "summary": "以“解读统计数据，要想深一点！”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑：比较猫科与犬科狩猎成功率时，犬科的成功率没有按犬群数量折算。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为拿群体狩猎成功率与单只猫科相比不妥，要比的是费效比（以单个狙击手与整个步兵班作比）。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定“猫科只会咬喉咙”的说法，称以猫科的咬合力和体力可以直接从后方咬断颈椎。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定“必须紧紧咬着否则猎物就会跑掉逃走”，反问受重伤的猎物能逃到哪去。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张哪个物种会先消失与哪个物种比较弱小没有关系，输给大自然根本是另一回事。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为有能力凭暴力强行割据一块最好用的狩猎场、每天步行两个街区就可以开始打猎而不用跟着猎物走几十公里，本身就是一种优势的直观表现。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为只追一公里、再远就不追、失败率全班第一却日子一样过、每天还睡十几个小时，本身也是优势地位的表现。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“解读统计数据，要想深一点！”作结，要求重新理解这类统计口径。", "evidence": ["E009"]}
   ],
   "argument_steps": [
    "以反问质疑对照比较中犬科成功率未按犬群数量折算。",
    "用花豹与四头狼的算例讽刺群体成功率被当成个体成功率，并指出猎获还要分成四份、需出动四人次。",
    "提出应以费效比而非命中率作比较（单个狙击手与整个步兵班的类比）。",
    "逐条反驳“猫科只会咬喉咙”“必须紧咬不放”，称咬合力与体力足以从后方咬断颈椎、牙爪本身足以致命。",
    "以火山喷发烧死项羽而韩信出差的假设，说明物种消失与“弱小”无关、输给大自然是另一回事。",
    "给出正面解释：能暴力割据最好狩猎场、短距离即可打猎，以及只追一公里、失败率第一仍过得很好，都是优势地位的表现。",
    "以“解读统计数据，要想深一点！”收束。"
   ],
   "concept_usage": [
    {"term": "狩猎成功率", "meaning": "被作者质疑的统计口径：以群体捕猎的成功率与单只猫科的成功率直接相比", "evidence": "P001", "ambiguity": "作者未给出该数据的来源与定义"},
    {"term": "费效比", "meaning": "作者提出的替代比较标准，相当于投入（人次、代价）与收获之比", "evidence": "P007", "ambiguity": "只有类比，未给出计算方式"},
    {"term": "优势（优势地位）", "meaning": "文中指能以暴力占据最优狩猎场、不必长途追随猎物、日子仍过得下去等表现", "evidence": "P014", "ambiguity": "未限定具体物种与衡量标准"}
   ],
   "examples_and_targets": [
    "“一头花豹捕一头羊，成功率50%”与“四头狼捕一只羊，成功率70%”（作者自拟或转述的算例，用于讽刺统计口径）",
    "“你干脆算成280%”（作者的反讽修辞）",
    "单个狙击手的命中率与整个步兵班相比（作者类比）",
    "猫科直接咬断颈椎、牙齿与爪的长度（作者论据）",
    "火山喷发把项羽烧死、韩信刚好出差（作者假设性类比）",
    "被反驳对象：“犬科狩猎成功率更高”“猫科只会咬喉咙”“必须紧紧咬着否则猎物跑掉”等流行说法（均由作者转述，未见具体论者与出处）"
   ],
   "conditions": [
    "反驳以对方的统计口径（以群体狩猎成功率与单只猫科比较）为前提，作者未给出数据来源。",
    "“直接从后方咬断颈椎”以猫科的咬合力和体力足够为条件。",
    "P014/P015 的描述指向可占据狩猎场、短距离追击的大型猫科，未指明具体物种与地区。"
   ],
   "rhetoric_and_tone": "反讽、调侃与连串反问为主（“你干脆算成280%，岂不快哉”“拜托，你们再算算吧还是”“好吗？”）；以“狙击手比步兵班”“项羽/韩信”等类比挖苦对方逻辑，结尾转为直接提醒（“解读统计数据，要想深一点！”）。",
   "unresolved_questions": [
    "作者未给出任何统计数据来源；“花豹50%”“四头狼70%”是作者自拟还是引用他人，本文未说明。",
    "对原问题“为什么猫科没有将犬科淘汰”未作正面回答，只否定了“弱小者先被淘汰”的推理。",
    "被反驳的具体说法出自哪些答主或来源，本文未说明。",
    "标题“猫山王”与正文（猫科与犬科之争）的关系本文未说明。",
    "P010“脖子上肚子上挨了几刀倒健步如飞的跑赢了？”中的场景（猎物挨刀后逃走）所指的具体说法与来源未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "犬科的成功率除掉了犬群数量了吗？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "四头狼捕一只羊，成功率70%，所以算成四头狼全部70%，是吧？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P007", "quote": "要比的是费效比才对吧？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P008", "quote": "是可以直接从后方咬断颈椎的。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P010", "quote": "逃能逃到哪去？", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P011", "quote": "哪个物种会先消失，跟哪个物种比较弱小没有关系。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P014", "quote": "有能力凭暴力强行割据一块最好用的狩猎场，每天步行两个街区就可以开始打猎", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P015", "quote": "只追一公里，再远就不追了，失败就失败，失败率全班第一，日子一样过", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P016", "quote": "解读统计数据，要想深一点！", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["动物学/演化", "科普争论"],
   "issue_candidates": ["猫科与犬科的比较", "狩猎成功率的统计口径", "物种存续与“强弱”的关系"],
   "text_function_candidates": ["论辩", "反驳", "科普答问"],
   "object_candidates": ["猫科", "犬科", "花豹", "狼", "狙击手", "步兵班", "项羽", "韩信"],
   "working_keywords": ["狩猎成功率", "费效比", "咬断颈椎", "优势地位", "统计口径"]
  },
  "notes": "本篇为驳论，被反驳观点均由作者转述，未给出具体论者与出处；文中的 50%、70% 等数据无来源，本记录只登记为作者的论证材料，不作事实裁决。"
 },
 "f589a906": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：韩国女团舞蹈是不是本质上在打色情的擦边球？作者没有评断韩国女团或具体舞蹈，而是以连串反问挑战“性感有罪”的前提，讨论性感的贬义词汇、性压抑与性教育缺失，并把“打色情的擦边球”这一视角本身当作要被治好的病来批评。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "以连续反问追问“性感有什么不好”、要求给出依据，反问他不能解释“越落后的国家的国民越不性感”，并以“早恋影响学习”“gdp增长率破7”作类比反讽。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "列举谈到“性感”时使用的贬义词汇（色情、黄色、骚、浪、贱、不正经等），讥讽“色情就不纯”“年老色衰会被抛弃”的说法，反问凭什么“年老”了“色”就要衰、就理应变成黄脸婆、油腻男。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "针对“妨碍追求正义和伟大理想”的说法，提出控制变量只看性满足，反问人类打仗是性满足太多还是太少，并追问为何要处心积虑减少性感教育、消除性满足供应。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P015"], "summary": "以反问提出一种解释（假说）：因为所有人都有性焦虑、害怕自己没有性魅力，所以要掀起鄙视性的人民战争，让大家一致相信“不性感没关系，甚至是一种大好事”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "反列举“威武不能屈、贫贱不能移”“有匪君子，如切如磋，如琢如磨”、理想主义、沧桑的微笑为何不算性感；指出只有迷信极狭隘性感观的人才会站到性感反面、把少数人当性竞争敌人讨伐，依仗的是“我们人多”，并讽刺一面唾骂一面买美白神器蛋白粉。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "假设性感的定义不那么狭隘、文化治好“道德必须反性感”的强迫症，则那些东西本来就是性感的；主张没有性自卑的人才能健康看待别人的性感，才不会用“打色情的擦边球”的视角看性感；“不性感”不应该是中国人的“文化特色”。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P024"], "summary": "判断恐惧性感、贬抑性感是心理发育缺陷、是自卑带来的无能狂怒。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "指出中国缺少正确的性教育，现有性教育停留在避孕教育、性卫生教育、生育常识教育（仅是性知识教育），而性文化、性意识、性伦理没有系统的教育工作甚至没有系统的研究工作，结论是“我们没有性文化教育”。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034"], "summary": "提出“不敢违法的性变态”已成不可忽视的主流性存在，并以“有了钱和权就会纵情声色”“有了钱不搞这些有点亏”的普遍心理为证，称钱和权起“免事金牌”的作用，而那些“有了钱和权后想对异性做的事”才真正反映性心理和性理想，要求按此标准重新估量性文化教育的缺失。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P035"], "summary": "以“这堪称一件国耻”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问追问“性感有什么不好”，要求对方给出依据，并反问有什么依据说明国人普遍性感了就会天下大乱。", "evidence": ["E001", "E002", "E003"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出我们谈到“性感”时用的几乎都是贬义词汇（色情、黄色、骚、浪、贱、不正经、低级趣味等）。", "evidence": ["E004", "E005"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反驳“色情就不纯”“年老色衰会被抛弃”的说法，反问凭什么“年老”了“色”就要衰、就理应变成黄脸婆、油腻男。", "evidence": ["E006", "E007"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者主张控制其他变量只看性满足，反问人类打仗是因为性满足太多还是太少，并追问为何要处心积虑减少性感的教育、恨不得消除性满足的供应。", "evidence": ["E008", "E009"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以反问提出一种假说：因为所有人都有性焦虑、害怕自己没有性魅力，所以要掀起鄙视性的人民战争，好让大家一致相信“不性感没关系，甚至是一种大好事”。", "evidence": ["E010"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问否认“威武不能屈、贫贱不能移”“有匪君子，如切如磋，如琢如磨”、理想主义、沧桑的微笑不性感的说法。", "evidence": ["E011"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为只有迷信“锥子脸、D罩杯、六块腹肌才性感”这种极狭隘性感观的人，才会因绝望站到性感反面、把拥有狭义性感的少数人当作性竞争的敌人去讨伐，其依仗不是正义而是“我们人多”。", "evidence": ["E012", "E013", "E014"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者提出：如果性感的定义不是这么狭隘、如果文化治好了“道德必须反性感”的强迫症，不把那么多东西和性感切分开，那些东西本来就是性感的。", "evidence": ["E015", "E016"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张没有性自卑的人才能健康地看待别人的性感，才不会再用“打色情的擦边球”的视角看待性感；并称“不性感”不应该是中国人的“文化特色”。", "evidence": ["E017", "E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断恐惧性感、贬抑性感是一种心理发育缺陷，是一种自卑带来的无能狂怒。", "evidence": ["E019"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国缺少正确的性教育（现停留在避孕教育、性卫生教育、生育常识教育，即仅是性知识教育），关于性文化、性意识、性伦理没有有效的系统性教育工作甚至没有系统的研究工作，即“我们没有性文化教育”。", "evidence": ["E020", "E021", "E022"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“不敢违法的性变态”已经在事实上成了一种不可忽视的主流性存在。", "evidence": ["E023"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问指出：在“有了钱和权就会纵情声色”“有了钱不搞这些有点亏”的普遍心理中，钱和权起“免事金牌”的作用，而那些“有了钱和权后想对异性做的事”才真正反映性心理和性理想，应按此标准重新估量性文化教育有多缺。", "evidence": ["E024", "E025", "E026"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“这堪称一件国耻”收束对性文化教育缺失的判断。", "evidence": ["E027"]}
   ],
   "argument_steps": [
    "以连串反问开场，要求对方给出“性感有什么不好”的依据，并反问“国人普遍性感就会天下大乱”的依据。",
    "以“越落后的国家的国民越不性感”与“早恋影响学习”“gdp增长率破7”作对照与类比，反讽这类因果推断。",
    "列举谈论性感时使用的贬义词汇，指出这种词汇体系本身构成对性感的道德定罪。",
    "反驳“色情就不纯”“年老色衰”的说法，反问“年老”与“色衰”的必然联系。",
    "对“妨碍追求正义与伟大理想”的说法，提出控制变量、只留性满足来反问：战争源于性满足太多还是太少。",
    "以反问提出假说：对性感的鄙视源于普遍的性焦虑与性自卑。",
    "反列举被认为不性感的正面品质，指出只有极狭隘的性感观才会把性感当敌人，并点出“我们人多”这一依仗。",
    "设想性感定义不狭隘、文化不再要求道德反性感的情形，主张那些品质本来就是性感的。",
    "把“恐惧性感、贬抑性感”判为心理发育缺陷，并转到性教育缺失：只有性知识教育，没有性文化教育。",
    "以“有钱有权后想对异性做的事”为标尺重新估量性文化教育的缺失，最后以“国耻”作结。"
   ],
   "concept_usage": [
    {"term": "性感", "meaning": "作者主张不应被道德定罪的吸引力，其定义不应局限于“锥子脸、D罩杯、六块腹肌”，也包括威武不能屈、理想主义、沧桑的微笑等", "evidence": "P016", "ambiguity": "作者始终用反问与举例表述，未给出定义式界定"},
    {"term": "色情的擦边球", "meaning": "提问使用的说法，作者把它当作性自卑者看待性感的视角来批评", "evidence": "P022", "ambiguity": "作者未讨论韩国女团舞蹈本身，只批评该视角"},
    {"term": "性焦虑／性自卑", "meaning": "作者用来解释鄙视性感的心理机制：害怕自己不帅不美、没有性魅力", "evidence": "P015", "ambiguity": "以反问提出，未给出依据"},
    {"term": "免事金牌", "meaning": "作者对钱和权在性心理中所起作用的比喻，指有钱有权后可以免于约束", "evidence": "P032", "ambiguity": "比喻性说法，未定义"},
    {"term": "性文化教育", "meaning": "作者指区别于避孕教育、性卫生教育、生育常识（性知识教育）的性文化、性意识、性伦理教育", "evidence": "P025", "ambiguity": "作者称其为缺失，未说明应包含什么内容"}
   ],
   "examples_and_targets": [
    "“早恋影响学习”（作者类比的流行说法）",
    "“要是ta们不是那么性感，他们的gdp增长率就一样可以破7”（作者模拟对方口吻的反讽）",
    "贬义词汇表：色情、黄色、骚、浪、贱、不正经、低级趣味、勾引、撩、狐媚、腐朽的生活方式（作者举证的流行语汇）",
    "“年老色衰”“黄脸婆、油腻男”（作者批评的流行表达）",
    "淘宝美白神器、蛋白粉（作者讽刺的消费行为）",
    "“锥子脸、D罩杯、六块腹肌”（作者批评的狭隘性感观）",
    "“威武不能屈、贫贱不能移”（《孟子》语）、“有匪君子，如切如磋，如琢如磨”（《诗经》语）（作者引作正面品质的例子）",
    "被反驳对象：认为性感有罪、妨碍正义与伟大理想、打色情擦边球的流行意见（作者转述）"
   ],
   "conditions": [
    "“性感有什么不好”的追问以要求对方给出依据为前提，文中未见答复。",
    "P004 的对照（越落后的国家国民越不性感）以反问提出，未给出数据来源。",
    "P012 的追问以“别的变量都控制住，只看性满足这个变量”为条件。",
    "P015 的解释以“所有人都有性焦虑”为假设，且以反问形式提出，不是断言。",
    "P020-P021 以“如果性感的定义不是这么狭隘”“如果我们的文化治好了……强迫症”为条件。",
    "P034“按这个标准”指以 P033“有了钱和权后想对异性做的事”为衡量标准。"
   ],
   "rhetoric_and_tone": "全篇以连串反问推进，排比追问、口语化呼告（“同志们，大家朴素一点”“来，谁来说说听听”）与反讽并置；讥讽语（“好一套天马流星舌头拳”“啊呀呀不得了”“累不累啊”“巨婴”式的鄙夷）；模拟对方口吻的引号反讽；结尾由批评转为“国耻”式训诫。",
   "unresolved_questions": [
    "提问（Q001）问的是韩国女团舞蹈，作者未针对韩国女团或任何具体舞蹈作答，“打色情的擦边球”仅作为被批评的视角出现，问答针对性存在落差。",
    "P002/P003“性感到底有什么不好”是在向谁发问（提问者、评论区还是泛指的国人）本文未说明。",
    "P004“越落后的国家的国民越不性感”未给出依据或数据来源；“早恋影响学习”“gdp增长率破7”所指的具体言论与语境未说明。",
    "P012/P013 关于性满足与战争的因果关系只以反问提出，未给出论证或证据。",
    "P029“不敢违法的性变态”所指群体与“性变态”的界定，本文未说明。",
    "P025-P028 所称“正确的性教育”“系统的研究工作”应包含什么内容，本文未说明。",
    "平台与版本：published_at=2019-10-23、updated_at=2021-05-25，正文是否经修订本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "性感有什么不好？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "有什么依据说明要是国人普遍性感了就会天下大乱？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "这个世界反而普遍是越落后的国家的国民越不性感？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P007", "quote": "看看我们提到“性感”用的都是什么词汇？", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P008", "quote": "——“色情”、“黄色”、“骚”、“浪”、“贱”、“不正经”、“低级趣味”", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P009", "quote": "感情最好不要“色情”，要是“色情”了肯定“不纯”。", "relation": "context"},
    {"key": "E007", "paragraph_id": "P010", "quote": "凭啥“年老”了“色”就要衰？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P012", "quote": "到底是人类啪得太多所以打仗，还是因为没得啪所以打仗？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P014", "quote": "为什么要处心积虑的减少性感的教育、恨不得消除性满足的供应呢？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P015", "quote": "因为所有人都有性焦虑，害怕自己不帅、不美，害怕自己没有性魅力", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P016", "quote": "为什么“威武不能屈、贫贱不能移”不是性感的？", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P017", "quote": "只有迷信“锥子脸、D罩杯、六块腹肌才性感”这种极其狭隘的性感观", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P018", "quote": "而是“我们人多”。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P019", "quote": "一面唾骂，一面淘宝美白神器蛋白粉——累不累啊……", "relation": "context"},
    {"key": "E015", "paragraph_id": "P020", "quote": "如果性感的定义不是这么狭隘呢？", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P021", "quote": "那些东西本来就是性感的呀！", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P022", "quote": "没有性自卑的人，才能健康的看待别人的性感。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P023", "quote": "“不性感”不应该是中国人的“文化特色”。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P024", "quote": "恐惧性感、贬抑性感，这是一种心理发育缺陷，是一种自卑带来的无能狂怒。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P025", "quote": "中国缺少正确的性教育。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P027", "quote": "关于我们的性文化、性意识、性伦理，没有任何有效的系统性教育工作", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P028", "quote": "我们没有性文化教育。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P029", "quote": "“不敢违法的性变态”已经在事实上成了一种不可忽视的主流性存在。", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P031", "quote": "我们是不是普遍觉得一旦人有了钱和权，就会纵情声色", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P032", "quote": "钱和权在这里扮演的就是“免事金牌”的作用", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P033", "quote": "那些“有了钱和权后想对异性做的事”，才真正反映人的性心理和性理想。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P035", "quote": "这堪称一件国耻。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性文化/社会批评", "性别与大众文化"],
   "issue_candidates": ["性感是否被道德定罪", "性教育的缺失", "性焦虑与性自卑", "韩国女团舞蹈的争议"],
   "text_function_candidates": ["论辩", "批评", "反问式议论"],
   "object_candidates": ["韩国女团", "中国人", "淘宝", "黄脸婆/油腻男"],
   "working_keywords": ["性感", "性焦虑", "性自卑", "性文化教育", "色情的擦边球", "免事金牌"]
  },
  "notes": "本篇以反问与反讽为主，多处判断是“作者在问”而非“作者在断言”（P002、P004、P012、P015、P031），本记录用 modality=questioned/hypothetical 保留语气；提问中的韩国女团舞蹈未被作者具体讨论，已记入未决问题。"
 },
 "800fb2b2": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：教师个人私下里自愿无偿为学生补课可以吗？作者先给出肯定回答，随即两次加上“前提是对方配得上”这一条件，并给出“配得上”的界定与比例估计。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "回答“当然可以”，但两次强调前提是对方配得上；称真遇到好的，作育人才是值得用生命去做的事情，而这样的比例大概万中无一。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "界定“配得上”：对方明白得到的是人的生命、知道其贵重、绝不肯让牺牲空掷，而不是嬉皮笑脸以为只是得着了便宜；知道珍惜的才配得。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P009"], "summary": "以“知道什么叫珍惜的人，万中无一”收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者回答教师私下自愿无偿补课“当然可以”，但前提是对方配得上。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为真遇到了好的，作育人才是值得用生命去做的事情，而这个比例大概万中无一。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把“配得上”界定为：对方明白得到的是人的生命、知道这是多么贵重、绝不肯让这些牺牲空掷，而不是嬉皮笑脸以为只是得着了便宜。", "evidence": ["E005", "E006"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断知道什么叫珍惜的人万中无一，而知道珍惜的才配得。", "evidence": ["E007", "E008"]}
   ],
   "argument_steps": [
    "直接给出肯定回答，随即附加“前提是对方配得上”。",
    "给出价值判断：真遇到好的，作育人才值得用生命去做。",
    "重复同一前提，并给出比例估计：这个比例大概万中无一。",
    "以设问“什么叫配得上？”给出界定，并区分“知道珍惜”与“嬉皮笑脸贪便宜”。",
    "以“知道什么叫珍惜的人，万中无一”收束。"
   ],
   "concept_usage": [
    {"term": "配得上", "meaning": "本文中指对方明白自己得到的是教师的生命、知道其贵重、绝不肯让牺牲空掷", "evidence": "P006", "ambiguity": "由谁判定、如何判定未说明"},
    {"term": "作育人才", "meaning": "作者称为值得用生命去做的事情", "evidence": "P003", "ambiguity": "未给出范围与方式"},
    {"term": "人的生命", "meaning": "指教师在此事中付出的是自己的生命（时间与生命本身）", "evidence": "P006", "ambiguity": "比喻与实指未区分"}
   ],
   "examples_and_targets": [
    "“嬉皮笑脸，以为只是得着了便宜”的受助者类型（作者描述的行为类型，非具体人物）",
    "“教师私下自愿无偿补课”这一提问情形（问题材料）"
   ],
   "conditions": [
    "回答以“前提是对方配得上”为条件，在 P002 与 P004 重复两次。",
    "“值得用生命去做”以真遇到好的为前提，而作者估计该比例大概万中无一。",
    "“配得上”的成立条件被限定为对方明白所得为人的生命、不肯让牺牲空掷。"
   ],
   "rhetoric_and_tone": "极简格言体，短句成段；首尾与中间重复“前提是对方配得上”“万中无一”形成呼应；以庄重表述（“作育人才是值得用生命去做的事情”）与冷峻判断并置。",
   "unresolved_questions": [
    "“这个比例大概万中无一”“知道什么叫珍惜的人，万中无一”未给出依据或来源。",
    "由谁判定学生是否“配得上”“知道珍惜”，本文未说明。",
    "提问涉及“教师私下自愿无偿补课”这一具体情形（可能涉及学校规定、公平性、安全责任等），作者未讨论这些现实约束。",
    "本篇 brief 与正文同源（brief 为正文的截断预览），无额外信息。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "当然可以。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "前提是对方配得上。", "relation": "qualifies"},
    {"key": "E003", "paragraph_id": "P003", "quote": "真遇到了好的，作育人才是值得用生命去做的事情。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "这个比例大概万中无一。", "relation": "qualifies"},
    {"key": "E005", "paragraph_id": "P006", "quote": "什么叫配得上？就是对方明白得到的是人的生命，知道这是多么贵重，绝不肯让这些牺牲空掷。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "而不是嬉皮笑脸，以为只是得着了便宜。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "知道珍惜的，就配得。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "可惜，知道什么叫珍惜的人，万中无一。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育伦理", "师生关系"],
   "issue_candidates": ["教师私下无偿补课", "受助者是否珍惜", "付出的价值"],
   "text_function_candidates": ["答疑", "经验总结", "格言式回答"],
   "object_candidates": ["教师", "学生"],
   "working_keywords": ["配得上", "作育人才", "珍惜", "万中无一"]
  },
  "notes": "正文九句，与 brief 同源；无图片节点。作者回答简短而条件化，本记录保留“前提是对方配得上”的限定与“万中无一”的估计语气，未将其读作无条件许可。"
 },
 "648c22fb": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：善恶是如何定义的？以下哪些是善人哪些是恶人？作者没有给出善恶定义，也没有逐一评断任何人，而是主张人类没有能力成就绝对的善，并论证任何“重划标准以切出全善典范”的道德规范设计都会失败；末尾附带批评对基督教的流行驳斥。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "给出总回答：人类没有能力成就绝对的善；从绝对意义上说只有恶的程度是大是小的问题，没有恶不恶的问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "任何试图重划标准、把部分人类切分为“全善的典范”的道德规范设计，都会出现“字面符合规范却无可否认邪恶”的案例；哪怕一时看似没有，人类也会迅速学会新规则，十年内把新救世方舟蛀蚀成笑话。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "自问是否存在短暂的“纯洁期”，回答是否定的：几十年后恶显露时才会意识到当时恶已在，只是认不出；并断言“我们连一瞬间也没有成功过”。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "称“巧妙地冲击善良的字面定义获得超额利润”是人类经典的通关战术、智慧种族祖传的手艺；这种重构“道德理想人”的努力只有已破产与暂时未破产两种状态，可悲的是每次新版在输光前总有一个“数量占优的人群相信这次我们能赢”的阶段。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "称这是人类最大的悲剧模型：意识形态鼎革所激起的滔天血海，没有一次真正让我们意识到我们自己就是恶龙的幼兽。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016"], "summary": "附带评论：很多人对基督教没有基本常识，驳斥的只是无知群体中流行的幻觉版本，如同红脖子痛恨“想象的中国”；这种批评与对象是否荒谬无关，只与他们自己想象对方有多荒谬有关，而做这种想象的能力本身也是荒谬的；以“人间喜剧，不亦悲夫”收束。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张在善与恶的问题上人类没有能力成就绝对的善；从绝对意义上说，人类只有恶的程度大小问题，没有恶不恶的问题。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者断言任何试图通过重划标准把部分人类切成“全善的典范”的道德规范设计，都会出现“完全符合字面定义却无可否认邪恶”的尴尬案例。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称哪怕一时看似没有，人类也会迅速学会新的游戏规则，要不了十年就把这艘新救世方舟蛀蚀成笑话。", "evidence": ["E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定存在“纯洁期”：几十年后改头换面的恶显露时会意识到恶在当时已在、只是认不出；并称“我们连一瞬间也没有成功过”。", "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“巧妙地冲击善良的字面定义获得超额利润”是人类经典的通关战术、是“智慧种族”祖传的手艺，这类努力只有已破产和暂时未破产两种状态。", "evidence": ["E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为每次重新下注“新版”，在输到倾家荡产之前总会有一个“数量占优的人群相信‘这次我们能赢’”的阶段。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是人类最大的悲剧模型：每次意识形态鼎革所激起的滔天血海，没有一次真正让我们意识到我们自己就是恶龙的幼兽。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为很多人对基督教没有基本常识，他们整天驳斥的只是无知群体中流行的一种幻觉版本，如同红脖子痛恨根本不在实际维度中存在的“想象的中国”。", "evidence": ["E011", "E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这种批评与所批评对象有多荒谬无关，只与他们自己想象对方有多荒谬有关；而最绝妙的讽刺是他们做这种想象的能力本身都是荒谬的。", "evidence": ["E013"]}
   ],
   "argument_steps": [
    "以“这个问题很好解决”开场，直接给出判断：人类无法成就绝对的善。",
    "由该判断推出：绝对意义上只有恶的大小之分，没有恶与不恶之分。",
    "以全称判断说明任何重划标准、切出“全善典范”的道德规范设计都会出现字面符合却邪恶的案例。",
    "给出机制：人类会迅速学会新规则，十年内蛀空新的救世方舟。",
    "自问是否存在“纯洁期”，并回答否定——恶在当时已在，只是认不出。",
    "以“通关战术”“祖传手艺”说明这种冲击字面定义获利的行为模式。",
    "指出这类重构只有两种状态（已破产／暂时未破产），并点出“相信这次我们能赢”的人群阶段。",
    "把上述归结为人类最大的悲剧模型与“我们自己就是恶龙的幼兽”。",
    "附带转入对基督教批评者的评论，以“想象的中国”作类比，最后以“人间喜剧，不亦悲夫”收束。"
   ],
   "concept_usage": [
    {"term": "绝对的善", "meaning": "作者认为人类没有能力成就的、绝对意义上的善", "evidence": "P002", "ambiguity": "作者未给出善的定义与判定标准"},
    {"term": "全善的典范", "meaning": "道德规范设计试图从人类中切分出来的完美样本", "evidence": "P003", "ambiguity": "以引号使用，属作者批评的对象用语"},
    {"term": "纯洁期", "meaning": "新道德规范发布后似乎无人作恶的短暂时期；作者否认其存在", "evidence": "P005", "ambiguity": "作者以设问提出再否定，未给出经验依据"},
    {"term": "通关战术", "meaning": "作者对人类“巧妙地冲击善良的字面定义获得超额利润”这一行为模式的称呼", "evidence": "P008", "ambiguity": "比喻性说法，未定义"},
    {"term": "恶龙的幼兽", "meaning": "作者对人的自我定位：我们自身就是恶的一部分", "evidence": "P010", "ambiguity": "比喻，未展开"}
   ],
   "examples_and_targets": [
    "“新救世方舟”被蛀蚀成笑话（作者的比喻）",
    "“新版”道德规范的重新下注与“数量占优的人群相信这次我们能赢”（作者描述的历史模式）",
    "意识形态鼎革所激起的滔天血海（作者举的历史现象，未指名具体事件）",
    "对基督教的幻觉版本（作者转述并批评的对象）",
    "红脖子痛恨的“想象的中国”（作者类比）",
    "“我不管，你们肯定就是我相信的那样”（作者引述被批评者的口吻）"
   ],
   "conditions": [
    "作者判断限定在“在善与恶的问题上”“从绝对意义上说”这一范围。",
    "P003 的结论覆盖“任何试图通过重划标准……的道德规范设计”，为全称判断，未给出例外。",
    "“要不了十年”“当几十年后”是作者给出的时间尺度，未给出依据。",
    "P011 以“顺便说一句”标明后文为附带话题，与善恶主题的关联由作者以类比建立。"
   ],
   "rhetoric_and_tone": "冷峻的断言式短句与引号反讽并用（“全善的典范”“通关战术”“智慧种族”“想象的中国”）；自问自答（“那是不是意味着……呢？”）；末尾转文言式感叹“人间喜剧，不亦悲夫”，语气由论说转为悲悯与讥讽。",
   "unresolved_questions": [
    "提问（Q001）“以下哪些是善人哪些是恶人”所指的具体名单未出现在 question 字段中，作者也未逐一评断任何人。",
    "作者未给出善与恶的定义，“恶的程度”如何度量亦未说明。",
    "P012-P015 对基督教批评者的评论未指明具体群体、言论或出处。",
    "P010“意识形态的鼎革所激起的滔天血海”未指名具体历史事件，需外部核查其指涉。",
    "本篇 updated_at（2025-02-08）晚于 published_at（2019-10-27），正文是否经修订本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "在善与恶的问题上，人类没有能力成就绝对的善。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "人类只有恶的程度是大是小的问题，没有恶不恶的问题。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "任何试图通过重划标准、将部分人类切分出来变成“全善的典范”的道德规范设计", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "完全符合这一规范的字面定义，但实际上却是无可否认的邪恶", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P004", "quote": "要不了十年，就能把这艘新救世方舟蛀蚀成笑话。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "其实在那个纯洁期，那个恶已经就在了，只是那时你认不出它而已。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "老实说，我们连一瞬间也没有成功过。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "“巧妙地冲击善良的字面定义获得超额利润”是人类经典的通关战术", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "每次重新下注“新版”，在输到倾家荡产之前", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "我们自己就是恶龙的幼兽。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "整天在驳斥的只不过是一种对基督教近乎完全无知的群体里流行的一种幻觉版本。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P013", "quote": "红脖子们天天痛恨的那个根本不在实际维度中存在的“想象的中国”", "relation": "context"},
    {"key": "E013", "paragraph_id": "P015", "quote": "他们做这种想象的能力本身都是荒谬的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德哲学", "宗教评论"],
   "issue_candidates": ["善恶的定义", "道德规范设计的失败", "意识形态更替的代价", "对基督教的流行误解"],
   "text_function_candidates": ["论说", "批评", "随笔式评论"],
   "object_candidates": ["基督教", "红脖子", "人类", "意识形态"],
   "working_keywords": ["绝对的善", "全善的典范", "纯洁期", "通关战术", "恶龙的幼兽", "想象的中国"]
  },
  "notes": "提问中的“以下（哪些是善人哪些是恶人）”清单未出现在 question 字段，作者也未作人物评断；P011-P016 属作者标明的附带话题，本记录按 other 单元登记，未与前文善恶论证混同。"
 },
 "f6a3ecc2": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：什么样的男人值得结婚？（作者引述为“是嫁给‘爱我的人’，还是‘我爱的人’”的二选一）。作者先否掉这一对立框架，称句中的“爱”实为“欲”，再用概率计算说明基于贪婪的关系难以持久，进而界定“爱”与“值得”，最后声明自己谈的是“值不值得结婚”而非“享有爱情”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出一条规律：两个仿佛阴阳互补、公说公有理婆说婆有理的对立方案，往往意味着答案找错了而不是要取“度”；据此回答：值得携手一生的人既不是所谓爱你的人，也不是所谓你爱的人。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "论证该句中的“爱”不是爱而是欲：实际是在“我欲之人”与“欲我之人”之间选，进一步是在“得到被追求的满足”与“得到追求的满足”两种私欲中二选一；无论怎么选，选到的都是本质的贪婪，关系也只能基于贪婪。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "称若对方没有受到足够的爱的教育，会基于同样的逻辑、以“爱”的名义遮眼，出于同样的贪欲选择你；并设问贪夫贪妇想得“一生幸福”有多难。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016"], "summary": "用概率计算说明长期不决裂之难：日度 99.9% 不决裂时四十年为 0.00000045；日度万分之一翻脸时四十年不翻脸为 23.2%；反问有多少人自问做得到 99.9%，并以“白头贪鬼”因怯于孤独而勉强咽下失败作结。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "提出“想要付出”也是一种贪：“付出”有道德快感并生出“道义”上的【不对称债权】；警告不要自以为正义、善良、无可指责、绝对洁白；称爱不是“付出”或“付出欲”，那些只是带着肉块的铁钩，当渔翁的冲动不是鱼感激鱼饵并“归属”的理由。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023"], "summary": "给出定义：爱在行为上是不求回报的付出；爱的起点不是付出，而是【不求回报】。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "回答“什么样的人值得”：不是出于乡愿和幼稚、而是出于彻悟和信念而奉献的人；“值得”不是对方来疼你哄你供养你满足你，而是你吃的苦通过促进 ta 的努力变成某个正果、成为其成就的一部分；跟着愿意自己吃苦成就他人的人，你所吃的苦也会因他所成就的他人变成不朽价值。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P031", "P032"], "summary": "以“遇见孙中山，值得宋庆龄”“因为郭靖，所以黄蓉”为例。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "点出“是不是只有圣人才配有爱情”这一逻辑陷阱，并限定讨论范围：谈的是“值不值得结婚”而非“享有爱情”；强调分析是冰冷刚硬、纯逻辑甚至数学的，未谈正义、崇高等形而上学概念，只从技术、操作、实践层面给出最大几率获得最好结果的可行方案，并称自己没谈“爱情”。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "指出读者所说的“爱情”其实是男欢女爱、是一种心理应激状态，与抽大麻后的飘飘欲仙本质无别，只是刺激源不同；它与“爱”这个词没有根本关系；无数毫无爱意的人也能有效挑起这种感受；结论是难得的不是“爱情”而是不破灭，不是圣人才配得“爱情”而是圣人才配得不破灭。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出一条规律：当一个问题存在两个仿佛阴阳互补、公说公有理婆说婆有理的对立方案时，往往不是应走向“要掌握一个度”，而是答案完全找错了。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者据此主张：值得携手一生的人既不是所谓爱你的人，也不是所谓你爱的人，因为句中的“爱”不是爱而是欲。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为该选择实际是在“我欲之人”与“欲我之人”之间选，进一步是在“得到被追求的满足”和“得到追求的满足”两种私欲中二选一；无论怎么选，选到的都是本质的贪婪，关系也只能基于贪婪。", "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称若对方没有受到足够的爱的教育，将会基于同样的逻辑、以“爱”的名义遮眼，出于同样的贪欲选择你。", "evidence": ["E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以概率计算说明贪夫贪妇难以得到“一生幸福”：日度 99.9% 不决裂时四十年不决裂的几率只有 0.00000045，即使日度万分之一翻脸也只有 23.2%；白头到老可能只是因怯于孤独而咽下失败。", "evidence": ["E007", "E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出“想要付出”也是一种贪：“付出”有道德的快感且生出“道义”上的【不对称债权】，因此不能自居为正义、善良、无可指责、绝对洁白的一方。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定爱是“付出”或“付出欲”，称那些只是带着肉块的铁钩；有当渔翁的冲动，不是鱼该为鱼饵感激你、“归属”你的理由。", "evidence": ["E013"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义：爱在行为上是不求回报的付出；爱的起点不是付出，而是【不求回报】。", "evidence": ["E014", "E015"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为值得的是那些不是出于乡愿和幼稚、而是出于彻悟和信念而奉献的人；“值得”不是对方来疼你哄你供养你满足你，而是你吃的苦通过促进 ta 的努力转变成了某个正果、成为 ta 成就的一部分。", "evidence": ["E016", "E017", "E018"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张跟着愿意自己吃苦成就他人的人，你将是他的最愿意成就的人，你所吃的苦也会因他所成就的他人变成真正不朽的价值。", "evidence": ["E019"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者限定：本文谈的是“值不值得结婚”而非“享有爱情”；分析本质上是冰冷而刚硬、纯逻辑甚至数学的，没谈正义、崇高等形而上学概念，只从技术、操作、实践层面给出最大几率获得最好结果的可行方案。", "evidence": ["E022", "E023", "E024"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定读者所说的“爱情”：那只是一种心理应激状态，本质上与抽了大麻后的飘飘欲仙没有区别，只是刺激源不同；它与“爱”这个词并没有根本的关系。", "evidence": ["E025", "E026"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者结论：难得的根本不是“爱情”，难得的是不破灭；不是圣人才配得“爱情”，而是圣人才配得不破灭，不破不灭才是所追寻的东西。", "evidence": ["E027", "E028"]}
   ],
   "argument_steps": [
    "以“两个对立方案往往意味着答案找错了”这一规律否掉“爱我的人／我爱的人”二选一。",
    "把该句中的“爱”重新界定为“欲”，并展开为“我欲之人／欲我之人”以及两种私欲的二选一。",
    "指出无论怎么选都是贪婪，关系也只能基于贪婪；并推及对方也会因同样的贪欲选择你。",
    "用日度不决裂概率的长期乘积说明“一生幸福”之难，并追问读者自身经验（三年内闹翻比例）。",
    "提出“想要付出”也是一种贪，指出“付出”的道德快感与【不对称债权】。",
    "把爱界定为不求回报的付出，起点是不求回报。",
    "回答“什么样的人值得”：出于彻悟和信念而奉献的人，值得的标准是苦转化为正果。",
    "以孙中山与宋庆龄、郭靖与黄蓉为例。",
    "点出“只有圣人才配有爱情”的逻辑陷阱，并限定讨论范围与方法的性质（技术、操作、实践层面）。",
    "把读者所说的“爱情”判为心理应激状态，结论落在“不破灭”。"
   ],
   "concept_usage": [
    {"term": "爱／欲", "meaning": "作者区分二者：句中的“爱”实为私欲；爱在行为上是不求回报的付出，起点是【不求回报】", "evidence": "P004", "ambiguity": "作者既称“不再谈爱情”，又大量使用爱与欲的界定，界线由其自述划定"},
    {"term": "不对称债权", "meaning": "作者用【】标注的自造词：付出者因道德快感而在“道义”上取得的不对等索取地位", "evidence": "P018", "ambiguity": "未给出定义式说明，只作提示"},
    {"term": "值得", "meaning": "本文中指你吃的苦通过促进对方的努力变成其成就的一部分（正果），而非对方回报你", "evidence": "P028", "ambiguity": "衡量方式未说明"},
    {"term": "爱情", "meaning": "作者指读者所说的男欢女爱、一种心理应激状态，与“爱”无根本关系", "evidence": "P040", "ambiguity": "与日常语义冲突，作者以引号标记"},
    {"term": "心理应激状态", "meaning": "作者对“爱情”感受的定性，与抽大麻后的感受类比", "evidence": "P040", "ambiguity": "属作者的判定，未给依据"}
   ],
   "examples_and_targets": [
    "“是嫁给‘爱我的人’，还是‘我爱的人’呢？”（提问／作者引述的二选一框架，作者要否定的对象）",
    "“和稀泥策略”（作者批评的“要掌握一个度”式答案）",
    "“贪夫贪妇”“白头贪鬼”（作者对基于贪婪的伴侣的称呼）",
    "概率算例：0.999^(365x4+1)*10 = 0.00000045；0.9999 情形下四十年不翻脸 23.2%",
    "带着肉块的铁钩、渔翁与鱼饵（作者比喻）",
    "孙中山与宋庆龄、郭靖与黄蓉（作者举的正面例子）",
    "抽大麻后的飘飘欲仙（作者类比“爱情”感受）",
    "“是不是只有圣人才配有爱情呢？”（作者自设并回应的话难）"
   ],
   "conditions": [
    "讨论以提问中“爱我的人／我爱的人”这一句用法为前提（P001）。",
    "概率计算以“每天都有决裂的几率”为模型，并自设日度 0.999 与 0.9999 两种情形（P010、P013）。",
    "分析被限定为“值不值得结婚”的讨论，而非“享有爱情”的讨论（P035）。",
    "“值得”以对方是出于彻悟和信念而奉献的人为条件（P025）。",
    "作者声明未谈正义、崇高等概念，只在技术／操作／实践层面给方案（P037）。",
    "P037“最大几率获得最好结果”本身是概率性、非保证性的表述。"
   ],
   "rhetoric_and_tone": "直接呼告（“告诉你们”“记住”“不要以为”）与连串反问并用；以数学式概率计算制造冷硬感（“你甚至可以说是数学的”）；用【】标注自造术语（【不对称债权】【不求回报】）；以孙中山／宋庆龄、郭靖／黄蓉等典故作结；对读者既有调侃（“贪夫贪妇”“白头贪鬼”“带着肉块的铁钩”）也有训诫。",
   "unresolved_questions": [
    "提问与标题都指向“什么样的男人值得结婚”，作者的回答未区分性别，通篇用“ta”；男女是否适用同一分析本文未说明。",
    "P012 算式“0.999^(365x4+1)*10 = 0.00000045”中的“*10”与“365x4+1”的含义本文未解释，需核对原意与计算是否正确。",
    "P013“就算是0.9999……23.2%”的计算过程未给出。",
    "“足够的爱的教育”具体指什么、由谁提供，本文未说明。",
    "作者自称“我没有谈论所谓的‘爱情’”，同时给出大量关于爱与欲的论断，二者关系需研究者判断。",
    "“遇见孙中山，值得宋庆龄”一句的含义（谁值得谁）本文未展开，可作多种解读。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "当你发现一个问题存在两个对立的方案，仿佛阴阳互补，公说公有理，婆说婆有理的时候", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "值得携手一生的人，既不是所谓爱你的人，也不是所谓你爱的人。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "因为在这个句子里的“爱”不是爱，而是欲。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "是在“得到被追求的满足”和“得到追求的满足”两种你本人的私欲中间二选一。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "你只是在两种贪婪之中选择", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "对方如果没有受到足够的爱的教育，将会基于同样的逻辑，以“爱”的名义遮眼，出于同样的贪欲选择你。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P012", "quote": "0.999^(365x4+1)*10 = 0.00000045。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P013", "quote": "四十年不翻脸，机会是多少？——23.2%", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P016", "quote": "到老两个白头贪鬼，只是因为怯于面对孤独的可能而勉强咽下自己的失败，苟且而已。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P017", "quote": "记住，“想要付出”也是一种贪。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P018", "quote": "“付出”有道德的快感，且生出“道义”上的【不对称债权】。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P019", "quote": "不要以为你是“很爱ta”，“很想为ta付出”，你就是正义的一方", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P021", "quote": "爱不是“付出”，也不是“付出欲”，那些东西只是带着肉块的铁钩。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P022", "quote": "爱在行为上，是不求回报的付出。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P023", "quote": "爱的起点，不是付出，而是【不求回报】。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P025", "quote": "那些不是出于乡愿和幼稚、而是出于彻悟和信念而奉献的人。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P027", "quote": "不是ta为了你的艰苦会来疼你、哄你、供养你、满足你叫“值得”。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P028", "quote": "而是你吃的苦通过促进ta的努力，转变成了某个正果——ta的成就的一部分，所以值得。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P029", "quote": "你所吃的苦，也会因为他所成就的他人变成真正不朽的价值。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P031", "quote": "遇见孙中山，值得宋庆龄。", "relation": "context"},
    {"key": "E021", "paragraph_id": "P032", "quote": "因为郭靖，所以黄蓉。", "relation": "context"},
    {"key": "E022", "paragraph_id": "P035", "quote": "首先，我们在谈论“值不值得结婚”的问题，而不是“享有爱情”的问题。", "relation": "qualifies"},
    {"key": "E023", "paragraph_id": "P036", "quote": "而本质上是冰冷而刚硬的、纯逻辑的——你甚至可以说是数学的。", "relation": "qualifies"},
    {"key": "E024", "paragraph_id": "P037", "quote": "而是纯粹从技术层面、操作层面、实践层面出发", "relation": "qualifies"},
    {"key": "E025", "paragraph_id": "P040", "quote": "那只是一种心理应激状态。", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P041", "quote": "这个东西与“爱”这个词并没有根本的关系。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P045", "quote": "——难得的根本不是“爱情”，难得的是不破灭。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P046", "quote": "不是圣人才配得“爱情”，而是圣人才配得不破灭。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋观", "伦理学/价值论", "概率式论证"],
   "issue_candidates": ["什么样的伴侣值得", "爱与欲的区分", "付出与贪婪", "婚姻持久的概率"],
   "text_function_candidates": ["答疑", "论说", "训诫式议论"],
   "object_candidates": ["孙中山", "宋庆龄", "郭靖", "黄蓉", "贪夫贪妇"],
   "working_keywords": ["爱", "欲", "值得", "不对称债权", "不求回报", "不破灭"]
  },
  "notes": "作者自称“我没有谈论所谓的‘爱情’”，但正文对爱与欲有大量界定，本记录按原文保留这一自我限定，不替作者统一。P012 算式与 P013 百分比未给出推导，已记入未决问题。"
 },
 "073d820a": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：《终结者：黑暗命运》里的 Rev-9 如果来到现实世界，以现在的军事实力，我们能干掉它吗？作者不讨论常规军力，而是以伪工程配方给出一个调侃式方案：用混有碳粉、玻璃微珠、铂金粉末和硝酸的沥青粘浆体反复稀释对方。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "否定用炸弹，提出应往对方身上泼混有碳粉、玻璃微珠和铂金粉末的混有硝酸的沥青粘浆体，并建议随身多带几袋。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "给出机理与推演：他变形次数越多体内杂质越多、没有有效手段排出，最后会被“稀释”成“沥青基质终结者乳/悬浊液”；调侃“5%浓度的终结者”威不起来，再泼一万块钱的可以稀释到一鱼塘。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "以玩笑收尾：让对方坐不起来、把稀释后的终结者拆成小瓶卖，并称能补肾、挂淘宝让一亿人喝了。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者主张不要用炸弹这些手段，而应往对方身上泼混有碳粉、玻璃微珠和铂金粉末的混有硝酸的沥青粘浆体，并随身多带几袋。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者提出机理：他变形次数越多体内杂质越多，又没有有效手段排出，最后会被“稀释”成“沥青基质终结者乳/悬浊液”。", "evidence": ["E003", "E004"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者调侃式推演：被稀释到“5%浓度”的终结者就不足为惧，再泼一万块钱的可以稀释到一鱼塘，最后还能拆成小瓶、宣称能补肾并挂淘宝让人喝。", "evidence": ["E005", "E006", "E007"]}
   ],
   "argument_steps": [
    "先否定“用炸弹”这一常规思路。",
    "给出替代方案：以含碳粉、玻璃微珠、铂金粉末与硝酸的沥青粘浆体泼洒，并强调随身多带。",
    "说明机理：变形使杂质在体内累积且无法排出，从而被“稀释”。",
    "以“5%浓度”“一鱼塘”“一小瓶一小瓶的卖”等夸张数量收尾。"
   ],
   "concept_usage": [
    {"term": "稀释", "meaning": "作者把“变形时混入杂质而无法排出”的过程称为稀释，指有效成分占比下降", "evidence": "P004", "ambiguity": "属作者对电影设定的类比，非化学定义"},
    {"term": "沥青基质终结者乳/悬浊液", "meaning": "作者自造的调侃说法，指被杂质稀释后的终结者形态", "evidence": "P004", "ambiguity": "无定义、无依据"},
    {"term": "5%浓度的终结者", "meaning": "作者以浓度比喻其残余威力", "evidence": "P005", "ambiguity": "数值为玩笑式设定"}
   ],
   "examples_and_targets": [
    "Rev-9（《终结者：黑暗命运》的虚构角色，提问设定）",
    "碳粉、玻璃微珠、铂金粉末、硝酸、沥青粘浆体（作者拟出的材料）",
    "“一万块钱的”“一鱼塘”（作者夸张的数量说法）",
    "“补肾”“挂淘宝”（作者用作玩笑的消费与养生话术）"
   ],
   "conditions": [
    "全部主张以提问设定的虚构角色及其液态金属变形能力为前提，不构成现实结论。",
    "“混有硝酸的沥青粘浆体”的配比、用量与有效性本文未说明，只给出“随身多带几袋”“再泼一万块钱的”这类调侃式数量。",
    "“他变形次数越多，体内杂质越多”“没有有效的手段排出”是作者对电影设定的推断。",
    "P007-P009 为玩笑段落，与军事问题无直接关系。"
   ],
   "rhetoric_and_tone": "通篇戏谑、夸张与玩梗：以伪工程配方（碳粉、玻璃微珠、铂金粉末、硝酸、沥青）制造煞有介事的喜感；用“我就不信……还威得起来”“你坐得起来都算我输”“我特么”等口语化狠话推进；“挂淘宝让一亿人喝了你”为荒诞收尾。",
   "unresolved_questions": [
    "提问的正面问题（以现在的军事实力能否干掉 Rev-9）未被回答，作者转向化学“稀释”调侃。",
    "“沥青基质终结者乳/悬浊液”“5%浓度”等为作者自造说法，无定义或依据。",
    "该方案在电影设定下是否可行（变形机制、杂质排出方式）本文未论证。",
    "P009“就说能补肾，挂淘宝让一亿人喝了你”属玩笑内容，其指涉的养生产品与平台现象未展开。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "不要用炸弹这些。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "应该往他身上泼混了碳粉、玻璃微珠和铂金粉末的混有硝酸的沥青粘浆体。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "他变形次数越多，体内杂质越多。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "他最后会被“稀释”成“沥青基质终结者乳/悬浊液”。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "我就不信“5%浓度的终结者”还威得起来。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "给你稀释到一鱼塘。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "就说能补肾，挂淘宝让一亿人喝了你。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["影视/流行文化", "科幻调侃"],
   "issue_candidates": ["虚构角色能否被现实军力消灭", "液态金属的弱点"],
   "text_function_candidates": ["调侃", "玩梗式回答"],
   "object_candidates": ["终结者", "Rev-9", "淘宝"],
   "working_keywords": ["终结者", "稀释", "沥青", "悬浊液", "补肾"]
  },
  "notes": "本篇是对虚构设定的玩笑式回答，不构成现实结论；作者自造的术语与数值均为调侃材料，本记录未据以生成事实性判断。无图片节点。"
 },
 "aeeaa88d": {
  "analysis": {
   "question_context": "提问者（Q001，属提问者立场）问：为什么一般小说和史书中的权谋大多是「一锤子买卖」，而现在的权谋小说则是「俄罗斯套娃」？作者先反驳“套娃式权谋不真实”的流行说法，再以“名义友好／敌对”两组关系为区分标准，最后把两种权谋的消长归因于当前世界整体和平。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "反驳“俄罗斯套娃式的权谋不真实”，主张两种情况都存在，差别的要害在于套娃式权谋出现在名义友好的双方之间，而“一锤子”权谋往往出现在敌对双方之间。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "说明“友好”的大义名分是关键因素：即使权谋失败、东窗事发、出乖露丑，往往也是 the show must go on；以张总李总为例说明下层员工看不出异样、看见看懂的也闭嘴；阴谋只要掌握分寸，失败并不致命，于是出现反转卧底戏，抓到也无非罚酒三杯。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "对敌则后果严重：对敌的谋略一定要简单，复杂就要生变，生变就往往失败。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "结论：当前的世界整体和平，才是两种权谋此消彼长的根源。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定“俄罗斯套娃式的权谋不真实”这一流行说法，认为这是错的。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张两种情况都存在，差别的要害在于套娃式权谋出现在名义友好的双方之间，而“一锤子”权谋往往出现在敌对双方之间。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“友好”的大义名分是关键因素：即使权谋失败、东窗事发、乃至于出乖露丑，往往也是 the show must go on。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称在友好名义下阴谋只要掌握分寸，失败了也并不致命，于是会出现很多匪夷所思的反转卧底戏，抓到也无非罚酒三杯。", "evidence": ["E004", "E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张对敌的谋略一定要简单，复杂就要生变，生变就往往失败。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断当前的世界整体和平才是两种权谋此消彼长的根源。", "evidence": ["E007"]}
   ],
   "argument_steps": [
    "先否定流行说法（“套娃式权谋不真实，这是错的”）。",
    "给出区分标准：名义友好的双方之间／敌对双方之间。",
    "以“大义名分”解释为何友好关系中的权谋失败也不致命（the show must go on）。",
    "以张总李总的例子说明失败权谋在下层与领导层的可见度差异。",
    "由“失败不致命”推出反转卧底戏与“罚酒三杯”式处理。",
    "对照敌方关系：谋略必须简单，复杂则生变、生变则失败。",
    "以“当前的世界整体和平”归结两种权谋的消长。"
   ],
   "concept_usage": [
    {"term": "俄罗斯套娃（式权谋）", "meaning": "沿用提问的说法，指层层嵌套、反复反转的权谋", "evidence": "P001", "ambiguity": "作者未给出定义或作品例证"},
    {"term": "一锤子（权谋）", "meaning": "沿用提问的说法，指一次性、决绝的权谋", "evidence": "P002", "ambiguity": "同上，未定义"},
    {"term": "大义名分", "meaning": "作者指双方名义上保持友好这一关键因素", "evidence": "P003", "ambiguity": "未说明其来源与维持机制"},
    {"term": "the show must go on", "meaning": "作者用来形容友好关系中即使权谋败露、场面仍要继续", "evidence": "P003", "ambiguity": "英文插入语，未加解释"}
   ],
   "examples_and_targets": [
    "张总与李总（作者举例用的泛称：张总吃暗亏、李总结梁子，下层员工看不出异样）",
    "部门里的或明或暗的卧底（作者举的现象）",
    "“罚酒三杯”（作者对处理结果的比喻）",
    "被反驳对象：“很多人都说‘俄罗斯套娃’式的权谋不真实”（作者转述的流行意见，未给出具体论者与出处）"
   ],
   "conditions": [
    "区分标准以“名义友好的双方”与“敌对双方”两组关系为条件。",
    "“阴谋只要掌握分寸，失败了也并不致命”以“友好”的大义名分仍存为前提。",
    "P007 的判断以“当前的世界整体和平”为时间条件。",
    "“对敌的谋略，就一定要简单”是对敌我关系下的主张，未涵盖友好关系。"
   ],
   "rhetoric_and_tone": "短论体：先立驳（“这是错的”），再给区分标准与机制；夹用商业称呼“张总”“李总”作举例、英文插入语“the show must go on”；以反问加强语气（“有多少部门里有或明或暗的卧底？抓到又如何？”）；结句用“此消彼长的根源”作冷峻概括。",
   "unresolved_questions": [
    "“很多人都说”所指的具体论者与出处未说明。",
    "“俄罗斯套娃”式权谋与“一锤子”权谋未给出定义或作品例证，其具体所指只能由提问语推测。",
    "“张总”“李总”是举例用的泛称还是实指，本文未说明。",
    "“当前的世界整体和平”与两种权谋消长之间的机制，作者只给出一句判断，未展开论证。",
    "本篇 updated_at（2026-07-11）晚于 published_at（2019-11-13），正文是否经修订本文未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "很多人都说“俄罗斯套娃”式的权谋不真实，这是错的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "差别的要害在于俄罗斯套娃式的权谋是出现在名义友好的双方之间，而“一锤子”权谋往往出现在敌对双方之间。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "即使权谋失败、东窗事发、乃至于出乖露丑，往往也是the show must go on。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "这时候阴谋只要掌握分寸，失败了也并不致命", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "无非罚酒三杯罢了。", "relation": "context"},
    {"key": "E006", "paragraph_id": "P006", "quote": "对敌的谋略，就一定要简单，复杂就要生变，生变就往往失败。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "当前的世界整体和平，这才是两种权谋此消彼长的根源。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["权谋/政治文化评论", "小说与史书评论"],
   "issue_candidates": ["套娃式权谋是否真实", "友好名义与敌对关系下的谋略差异", "世界和平与权谋形态的关系"],
   "text_function_candidates": ["评论", "论辩", "答疑"],
   "object_candidates": ["张总", "李总", "部门", "领导层"],
   "working_keywords": ["俄罗斯套娃", "一锤子买卖", "大义名分", "卧底", "罚酒三杯"]
  },
  "notes": "无图片节点。作者未给出两种权谋的定义或作品例证，均沿用提问说法；“the show must go on”为原文英文插入语，本记录照录。"
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
