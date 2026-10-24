# -*- coding: utf-8 -*-
"""批次 r001-b0098 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0098.sessions.py            # 写 out/r001-b0098.out.jsonl
  python3 records/r001-b0098.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0098"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0098.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "7b7ab164": {
  "analysis": {
   "question_context": "提问者问“中国校服是否扼杀了个性”。作者没有正面回答是或否，而是把校服、统一发型、统一用具（尤其公立学校的这类设置）解释为消除同校学生乃至整个青少年阶层间阶级差异的安排；提问中的“扼杀个性”不是作者立场，作者反而把“个性化”解释为需要成本支撑、常与阶级身份挂钩的东西。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "校服等设置的根源性用意：尽可能消除同校学生乃至整个青少年阶层间的阶级差异，为平等社会、平民社会提前铺路。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "“个性化”为避免被模仿而奢侈化；设计成本越受限选择越少；定制能力与经济资本、知识资本挂钩，故个性化外观常是阶级身份的直接具像化。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "该安排保护中产与下层阶级子弟、延缓阶级意识分化的危机进程；学校是不同阶级青少年平等交往、形成感情关联最重要的平台。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009"], "summary": "公立教育令富裕阶层不满的两面：几乎不承认私立教育合法性，以把最大比例中上阶级子女留在公立系统；在补贴降学费前提下按中间甚至偏下标准设计着装、用具、餐饮，近乎无视富裕阶层的物质需求。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "这是事关国本的底层决策；除非国家定位转向已发展国家，否则难看的运动服会持续；青少年阶段所有人都向中下收入水平看齐。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P012"], "summary": "这是从根源上保证社会稳定的重大事项，不是学生觉得好不好看的小事，所以教育部门态度强硬、基本不理会吐槽。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P013"], "summary": "结尾判断：这是“为你们好”；若不做限制，富裕阶层子女大概到大学毕业时会习惯性地把中下阶层子女看作“另一类人”，犹如有种姓之分。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "校服、统一发型、统一用具，尤其公立学校的这类设置，有一个不常明言但根源性的用意：尽可能消除同校学生乃至整个青少年阶层间的阶级差异，避免青少年期间就出现过于严重的阶级身份意识。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是在为平等社会、平民社会提前铺路。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“个性化”，为避免他人轻易模仿，最基本的策略就是奢侈化；均衡满足所有需求的设计成本越受限则选择越少，只有投入更多成本才能兼容更多方案可能性，这是设计的基本规律。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "展现个性的前提是与之匹配的定制能力，定制能力直接与经济资本、知识资本挂钩，“个性化外观”常是阶级身份的直接具像化。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是在保护中产阶级和下层阶级子弟、避免给ta们造成沉重负担，也是在延缓社会阶级意识分化的危机进程。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学校实际上是不同阶级出身的青少年彼此接近平等交往、形成感情关联最重要的平台。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为这个原因，我国公立教育才设置得如此令富裕阶层不满意。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一方面是几乎不承认私立教育的合法性，以确保最大比例的中上阶级子女进入公立教育系统，与中下阶层青少年从小交往。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "另一方面在公立教育里、在大量补贴降低学费的前提下，按中间甚至偏下标准设计学生着装、用具、餐饮标准，近乎无视富裕阶层的物质条件需求，强迫其子女适应中下收入家庭子女的生活、学习水平。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这是事关国本底层的决策；除非中国整体国家定位转向已发展国家（中等收入家庭已普遍相对富裕、低收入家庭也可得到足够财政补贴），否则一起穿难看的运动服还会一直持续下去。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在青少年阶段，所有人都要向中下收入水平看齐。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是从根源上保证社会稳定的重大事项，不是学生觉得好不好看的小事，所以教育部门在这个问题上态度强硬、随人吐槽基本当作没听见。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若不做这样的限制，大概到大学毕业时，富裕阶层子女将普遍地、习以为常地、熟练地把中下阶层子女看做“另一类人”，犹如有种姓之分。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对读者称：说实在的，这是为你们好。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "先给校服、统一发型、统一用具定性：不常明言但根源性的用意是消除同校及青少年阶层的阶级差异（P001）。",
    "把它上升为目标判断：为平等社会、平民社会提前铺路（P002）。",
    "用设计成本规律说明“个性化”必然奢侈化、选择随成本受限而减少（P003）。",
    "把定制能力接到经济资本、知识资本，得出个性化外观常是阶级身份具像化（P004）。",
    "给出功能判断：保护中下阶级子弟、延缓阶级意识分化（P005）。",
    "补充前提性理由：学校是不同阶级青少年平等交往、形成感情关联最重要的平台（P006）。",
    "由该功能解释公立教育为何令富裕阶层不满（P007），并分“一方面/另一方面”举证（P008、P009）。",
    "定性为国本底层决策，并给出唯一的改变条件（国家定位转向已发展国家），否则现状持续（P010）。",
    "重申青少年阶段向中下收入水平看齐（P011）。",
    "以“社会稳定重大事项”收拢，解释教育部门的强硬态度（P012）。",
    "结尾以“为你们好”和对“种姓化”后果的预测作结（P013）。"
   ],
   "concept_usage": [
    {"term": "个性化", "meaning": "文中所指需要成本支撑的外观差异化：为避免被模仿而奢侈化，与定制能力、经济与知识资本挂钩，常是阶级身份的具像化。", "evidence": "P003", "ambiguity": "作者未直接回答校服是否扼杀个性，而是重构了“个性化”的成本含义"},
    {"term": "阶级身份意识", "meaning": "青少年期间因物质条件差异而形成的阶级身份区分意识；作者认为统一化设置可避免其过于严重。", "evidence": "P001", "ambiguity": "未界定“阶级”的划分标准"},
    {"term": "国本底层决策", "meaning": "作者对公立教育统一着装、用具、餐饮标准这类安排的定性：事关国家根本的底层决策。", "evidence": "P010", "ambiguity": "“国本”未给出定义"},
    {"term": "平等社会、平民社会", "meaning": "作者认为统一化设置所提前铺路的目标社会形态。", "evidence": "P002", "ambiguity": "未说明其具体制度含义"},
    {"term": "种姓", "meaning": "作者对不做限制时富裕阶层子女看待中下阶层子女方式的类比。", "evidence": "P013", "ambiguity": "比喻用法，未对应具体制度"}
   ],
   "examples_and_targets": [
    "校服、统一发型、统一用具、公立学校的这类设置——文章主要对象（P001）",
    "“个性化”与定制能力、经济资本、知识资本——作者的解释性材料（P003、P004）",
    "公立教育、私立教育的合法性、教育部门——机构与政策对象（P007、P008、P012）",
    "中产阶级、下层阶级子弟、中上阶级子女、富裕阶层及其子女、中下收入家庭子女——作者论证中的群体（P005、P008、P009）",
    "“难看到尴尬的运动服”——修辞材料（P010）",
    "“犹如有种姓之分”——类比材料（P013）",
    "提问者的“扼杀个性”提法——被作者重新解释的提问方说法，不是作者立场（Q001、P003）"
   ],
   "conditions": [
    "范围限定在“公立学校的这类设置”，并以“尤其是”标出重点（P001）",
    "程度限定：“尽可能消除”“避免……过于严重”（P001）、“常是”（P004）、“几乎不承认”（P008）、“近乎于无视”（P009）",
    "政策前提：“在大量补贴降低学费的前提下”（P009）",
    "唯一改变条件：“除非中国整体国家定位转向已发展国家——也就是中等收入家庭已经普遍相对富裕，且低收入家庭也可以得到足够财政补贴——否则……还会一直持续下去”（P010）",
    "预测带或然词：“如果不做这样的限制，大概到大学毕业时”（P013）"
   ],
   "rhetoric_and_tone": "解释与辩护语气，断言密集；对读者用第二人称“你们”（“随你们怎么吐槽”“这是为你们好”），带训诫与轻微讽刺；以“阶级”“国本”“社会稳定”等重词把议题抬到国家层面；用“一方面/另一方面”对称结构与“这是设计的基本规律”式的断言增强说服力。",
   "unresolved_questions": [
    "提问为“是否扼杀个性”，作者未直接回答是或否，只给出校服制度的功能解释与对“个性化”的重新定义。",
    "P012“教育部门才会在这个问题上如此强项”中的“强项”按原文保留，疑为原文用词或笔误，含义需核对。",
    "“我国公立教育几乎不承认私立教育的合法性”是作者对政策的事实断言，正文未给依据，需外部核查。",
    "全文未提供数据或机制说明校服与阶级差异消除、社会稳定之间的实际关系。",
    "“知识资本”“阶级身份”“平等社会、平民社会”的具体含义均未界定。",
    "brief 与正文首段重复且被截断（结尾停在“最”字），不作为独立主张依据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "尽可能消除同校学生乃至于整个青少年阶层间的阶级差异", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这是在为平等社会、平民社会提前铺路。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "所谓的“个性化”，为了避免他人轻易模仿，最基本的策略就是奢侈化。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "而定制能力直接与经济资本、知识资本挂钩", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这是在保护中产阶级和下层阶级子弟，避免给ta们造成沉重负担", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "学校实际上是不同阶级出身的青少年彼此接近平等交往、形成感情关联最重要的平台。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "我国的公立教育才设置得如此的令富裕阶层不满意", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "几乎不承认私立教育的合法性，以确保最大比例的中上阶级子女会进入公立教育系统", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "近乎于无视了富裕阶层对这些物质条件的需求", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "除非中国整体国家定位转向已发展国家", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P011", "quote": "在青少年阶段，所有人都要向中下收入水平看齐。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "这是从根源上保证社会稳定的重大事项，不是学生们觉得好不好看这样的小事", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "富裕阶层的子女将普遍的、习以为常的、熟练的把中下阶层子女看做“另一类人”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "说实在的，这是为你们好。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "社会分层", "公共政策"],
   "issue_candidates": ["校服与个性", "公立教育中的阶级差异", "统一化管理的功能"],
   "text_function_candidates": ["答疑", "解释", "论辩", "政策辩护"],
   "object_candidates": ["中国公立学校", "教育部门", "富裕阶层", "中产阶级", "下层阶级"],
   "working_keywords": ["校服", "统一发型", "个性化", "阶级差异", "平等社会", "国本", "种姓"]
  },
  "notes": "无图片节点。brief 为正文节选且截断。作者以第二人称面向读者作答，提问者的“扼杀个性”提法被重新解释而非采纳；“ta们”“强项”等按原文保留。"
 },
 "490bc540": {
  "analysis": {
   "question_context": "提问者设想“假如给你 1 个亿，只能持有 1 天，操作所得的收益归你，你会怎么操作”。作者以一份分步方案作答：先用自己的书法作品把一亿变成“本金”收益，再毁灭生成行为艺术，随后借展、二次拍卖、成立基金会、上市。方案是作者提出的操作路径，不是提问者的主张；作者未讨论该假设本身是否合理。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总策略：一亿拍下自己的书法作品，要赚就赚本金，而不是那点利息。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "毁灭作品，生成《道德的碎片》行为艺术作品，委托方持有产权，当天结束。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "委托方巡回展出并分门票收入；展出后策划方以同样一亿拍下作品，委托方收回成本、净赚门票收入，策划方获得《价值的重生》。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "继续借展，借这项话题作品的名望获得现代艺术史地位。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "适时办慈善拍卖，2亿底价拍出；拍得款成立基金会管理全部作品，邀请买家加入基金会任董事。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P007", "P008"], "summary": "基金会建场馆，以门票收入和资产作保经营收藏、授权开发与拍卖；用年度收入颁奖、资助美院教学创作、设特别教授席位。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P009"], "summary": "最后在港交所上市，融资设立全球办公室。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "操作的总策略是用一亿拍下自己的书法作品——要赚就赚本金，而不是那点利息。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "随后把该作品毁灭，生成《道德的碎片》行为艺术作品，由委托方持有产权，当天结束。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "委托方送作品巡回展出，对展出门票分成，获得门票收入。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "展出完毕后由策划方用一个亿拍下该作品，委托方收回一亿成本、净赚门票收入，策划方获得二次生成的新行为艺术作品《价值的重生》。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "继续借展，同时借助运作这项话题作品的名望获得现代艺术史地位。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "在恰当时组织慈善拍卖会，以2亿底价拍出；拍得金额用来成立基金会管理全部作品，并邀请拍得买家加入该基金会成为董事。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "该基金会将拥有2亿现金，其管理的作品（含《价值的重生》）总值难以估计。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "基金会建立场馆，以门票收入和资产作保，经营艺术品收藏、授权开发和拍卖。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "基金会合理运用年度收入来颁发年度艺术奖项、资助各大美院特定专业教学与创作，并设立特别教授席位。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "方案的最后一步是在港交所上市，融资设立全球办公室。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "先给出总策略：用一亿拍下自己的书法作品，赚本金而非利息（P001）。",
    "把作品毁灭，生成行为艺术作品《道德的碎片》，由委托方持有产权（P002）。",
    "安排巡回展出与门票分成，取得现金流（P003）。",
    "由策划方以同样一亿二次拍下作品，使委托方收回本金、净赚门票收入，并产生新作品《价值的重生》（P004）。",
    "继续借展并积累现代艺术史地位（P005）。",
    "以2亿底价慈善拍卖，用拍得款成立基金会、让买家进入董事会（P006）。",
    "以基金会持有现金与作品，建场馆并经营收藏、授权与拍卖（P007）。",
    "用年度收入颁奖、资助美院教学与创作、设教授席位（P008）。",
    "最后在港交所上市融资、设全球办公室（P009）。"
   ],
   "concept_usage": [
    {"term": "本金/利息", "meaning": "作者把一亿的运用目标定为赚取“本金”式的大额收益，而不是一天内资金产生的利息。", "evidence": "P001", "ambiguity": "“要赚就赚本金”为口语表述，未给出具体含义与算法"},
    {"term": "行为艺术作品", "meaning": "方案中通过毁灭与二次拍卖生成的艺术品：《道德的碎片》《价值的重生》。", "evidence": "P002", "ambiguity": "未说明作品成立的依据与创作者身份"},
    {"term": "委托方/策划方", "meaning": "方案中的两个角色：委托方持有作品产权，策划方负责二次拍下作品。", "evidence": "P002", "ambiguity": "两个角色的具体身份、与资金持有人的关系未说明"},
    {"term": "基金会", "meaning": "用2亿拍卖款设立、管理全部作品并邀请买家任董事的机构。", "evidence": "P006", "ambiguity": "未说明基金会的法律形式、所在地与治理结构"}
   ],
   "examples_and_targets": [
    "作者自己的书法作品——方案的核心标的（P001）",
    "《道德的碎片》《价值的重生》——作者为方案命名的行为艺术作品（P002、P004）",
    "委托方、策划方、拍得买家——方案设定的角色（P002、P004、P006）",
    "慈善拍卖会、基金会、场馆、各大美院、特别教授席位、港交所——方案设定的机构与场景（P006—P009）",
    "以上均为作者方案内的设定与命名，并非外部事实证据。"
   ],
   "conditions": [
    "全篇以提问的假设为前提：只有1个亿、只能持有1天，收益归操作者（Q001、P001）",
    "时间条件：作品毁灭与产权安排要在“今天结束”前完成（P002）",
    "时点未定：“在恰当时组织慈善拍卖会”（P006）",
    "基金会经营以“门票收入和资产作保”为条件（P007）",
    "上市地点限定为港交所（P009）"
   ],
   "rhetoric_and_tone": "冷静的步骤清单式陈述，短句推进、几乎不给论证；仅以“要赚就赚本金，谁要赚那点利息”一句口语化反问带出态度；用《道德的碎片》《价值的重生》等命名营造艺术叙事；结尾以“港交所上市”收束，带调侃式的层层升级。",
   "unresolved_questions": [
    "方案中的书法作品由谁创作、是否预先存在，正文未说明。",
    "“委托方”“策划方”的主体及其与资金持有人的关系未说明。",
    "一亿资金在一天内完成拍卖、产权转移与作品毁灭的时间与法律可行性，正文未说明。",
    "《道德的碎片》《价值的重生》是既有作品还是作者命名，未说明。",
    "借话题作品获得“现代艺术史地位”的机制未说明。",
    "基金会与港交所上市的主体、条件与合规性未说明。",
    "作者未论证该方案能否真实执行，也未给出收益与风险的量化。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "一亿拍下自己的书法作品——要赚就赚本金，谁要赚那点利息。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "将该作品毁灭，生成《道德的碎片》行为艺术作品，委托方持有产权，今天结束。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "委托方送去巡回展出，对展出门票分成。获得门票收入。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "策划方获得二次生成的新行为艺术作品《价值的重生》。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "继续借展，同时借助运作这项话题作品的名望获得现代艺术史地位。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "在恰当时组织慈善拍卖会，以2亿底价拍出。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "管理的作品（含《价值的重生》）总值难以估计。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "基金会建立场馆，以门票收入和资产作保，经营艺术品收藏、授权开发和拍卖。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "资助各大美院特定专业教学与创作，设立特别教授席位。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "港交所上市，融资设立全球办公室。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["艺术市场", "金融操作", "行为艺术"],
   "issue_candidates": ["一亿一天如何操作", "艺术品的金融化运作", "慈善拍卖与基金会"],
   "text_function_candidates": ["答疑", "方案设计", "调侃式推演"],
   "object_candidates": ["港交所", "各大美院", "基金会", "拍卖会"],
   "working_keywords": ["本金", "行为艺术", "巡回展出", "慈善拍卖", "基金会", "上市"]
  },
  "notes": "无图片节点。正文是对假设性提问的分步方案清单，无可行性论证与数据；brief 为同一方案前半部分的节选。文中“委托方”“策划方”等角色主体不明，已记入未决问题。"
 },
 "7cbceef8": {
  "analysis": {
   "question_context": "提问者说男朋友“出于好心”在她的茶里下止痛药，她知情后非常愤怒，问到底是谁的问题。作者不判定“谁的错”，而是给出处理方案：愤怒无用，唯一办法是分手再看能否复合，并附两点执行注意事项与一段由作者拟给读者的道歉示范话术；文中还提到当事人已经写了道歉（P031），属作者对提问方后续动态的转述。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接给出方案：愤怒没用；这种事只有一种解决办法——分手再看能不能复合。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "理由：只有涅槃重生才能压制这种级别的过犯，维持关系存续的沟通劝说都无用；因为关系存续本身就在证明这不是真正要紧的问题。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "反驳“这是小事”：在预先答应的前提下违背明确共识、践踏基本权利且不以为耻反以为荣；无教训则会再犯；原则分歧动摇地基，关系已事实崩溃。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "让步与条件：并非必然万劫不复；若对方能穿越痛苦、不服气、怨恨，看懂份量并明白红线不可逾越，以真诚抱歉、无怨恨、认同分手决定的状态回应，感情可以重生。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "分手是重新修订基本共识的必经之路；否则勉强继续必无善了；拖到婚后恩断义绝更惨；含糊过去会成为“这样没啥不行”的事实依据。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "注意事项1：不要用愤怒驱动执行，疾言厉色的批评指责发出的是要求对方屈服于统治的信号，而非要求尊重原则。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "注意事项2：首次发现分歧时的伦理关系不是“对方有错应受罚”，而只是“发现了分歧”；对方无理所当然的过错；你有权痛苦但无权发泄与伤害；应以补充信息、正式告知的姿态解释立场。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "作者拟出向对方道歉的示范话术（承认未提前说明原则、为耽误时间抱歉、不应强加原则并发泄情绪），并称这的确是事实。", "role": "other"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032"], "summary": "对当事人已写道歉的评论：文字上算过关；但“无论以任何理由都不欺骗”这类许愿发誓的话不宜说。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "愤怒是没用的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种事只有一种解决办法，就是分手再看能不能复合。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有涅槃重生才能压制这种级别的过犯；任何维持着关系存续状态的沟通、商量、劝说、恳求、教育都是无用的。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为“关系存续”本身在以最大事实的身份证明“这不是一个真正要紧的问题”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这不是小事：在预先答应的前提下直接违背双方明确共识、直接践踏对方的基本权利，而且不以为耻、不以为恶，竟以为荣。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这如同野生老虎尝到人血：若没有立刻给予足够负面的信息形成“此事绝对得不偿失”的事实教训，下一次发作时就不知是什么后果。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种级别的原则分歧无法构建任何平等自愿的亲密关系；关系事实上已经崩溃，分手不是在杀死关系，而不过是在补发讣告。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这并不必然意味着关系就此万劫不复；如果对方能穿越痛苦、不服气和怨恨，看懂这件事的份量、明白红线不可逾越，并以真诚抱歉、没有怨恨、认同分手决定并非没有道理的状态回应，那么这份感情可以重生。", "evidence": ["E8", "E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有经过分手、经过以分手为必经之路的基本共识的重新修订，这个关系才可以继续；否则勉强继续必无善了，流毒遗患会反复发作直到彻底恩断义绝。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若等到婚已结、孩子已生、工已辞再彻底恩断义绝，比此刻分手惨烈何止百倍。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "刮骨疗毒，十天半个月治好就好——若对方确实转不过这个弯，那么你只是躲过了一个沦为奴仆的未来。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "含糊过去，它甚至将成为“这样没啥不行”的事实依据，贻害至烈。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "执行这种处置时不要用愤怒去驱动，也不可以通过疾言厉色的批评指责来实施。", "evidence": ["E14", "E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "疾言厉色、剜心刺骨的呵斥、贬损、咒骂发出的是完全另一种信号——不是要人尊重你的原则，而是在惩罚人不接受你的统治。", "evidence": ["E16"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "首次发现对方不符合这个原则时的伦理关系并不是“对方有错，应当受罚”，而仅仅是“发现了分歧”；对方并不存在理所当然的过错。", "evidence": ["E17", "E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是你的原则，不是经过对方同意答应遵守的共识；你有权痛苦，但无权对对方发泄情绪，无权伤害对方。", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以只能、应该而且必须排除对对方不公平的攻击，以补充信息、正式告知的姿态解释立场，并有必要向对方抱歉。", "evidence": ["E20", "E21"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的道歉示范（引号内为作者拟给读者对对方说的话）：承认没有提前清晰告知自己的原则、为可能耽误对方寻找理想伴侣的时间抱歉、不应把个人原则强加于人并因期待落空而发泄情绪。", "evidence": ["E22"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "但这些并不改变“这是我无法接受的原则”这一事实；若对方确实觉得自己的想法是对的，那么双方无法有效共同生活，也没有理由再耽误对方。", "evidence": ["E23"]},
    {"claim_id": "C020", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者称看到当事人已经写了道歉，从文字上看也算过关了。", "evidence": ["E24"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不过“无论以任何理由都不欺骗”这样许愿发誓的话不宜说。", "evidence": ["E25"]}
   ],
   "argument_steps": [
    "先给结论：愤怒没用，唯一办法是分手再看能否复合（P001、P002）。",
    "给出理由：只有涅槃重生式的关系重建才能压制这种级别的过犯；维持关系存续的一切沟通劝说都无用，因为关系存续本身在证明问题不要紧（P003—P005）。",
    "反驳“这是小事”的解读：在预先答应的前提下违背明确共识、践踏基本权利，且不以为耻反以为荣（P006）。",
    "以野生老虎尝人血作类比，说明无即时负面教训就会再犯（P007）。",
    "把原则分歧定性为地基动摇，关系已崩溃，分手只是补发讣告（P008）。",
    "让步：并非必然万劫不复，并给出对方若能达到若干条件则感情可以重生（P009—P011）。",
    "指出这才是真正活着，否则只是过家家、彼此耽误（P012）。",
    "重申只有经过分手与共识重新修订关系才能继续，否则流毒反复（P013）。",
    "用后果比较加强：拖到婚后、生子、辞职后决裂更惨（P014）。",
    "用刮骨疗毒与“沦为奴仆的未来”说明取舍（P015）。",
    "警告含糊过去会成为“这样没啥不行”的事实依据（P016）。",
    "给出执行注意事项一：不要用愤怒驱动，疾言厉色的信号是要求屈服于统治（P017—P021）。",
    "给出执行注意事项二：首次发现分歧不是“对方有错应受罚”，对方无理所当然的过错，无权发泄与伤害，应以告知姿态解释立场（P022—P026）。",
    "提供道歉示范话术并称这的确是事实（P027—P030）。",
    "最后点评当事人已写的道歉，并保留对许愿发誓式话语的意见（P031、P032）。"
   ],
   "concept_usage": [
    {"term": "涅槃重生", "meaning": "作者用来指以分手为必经之路的关系重建，认为只有它才能压制这种级别的过犯。", "evidence": "P003", "ambiguity": "比喻性用法，未界定具体过程与判定标准"},
    {"term": "关系存续", "meaning": "维持关系不分手的状态；作者认为它本身就在证明问题不要紧。", "evidence": "P004", "ambiguity": "作者用“以最大事实的身份证明”作修辞，未给论证"},
    {"term": "红线", "meaning": "作者对“在预先答应的前提下直接违背明确共识、践踏对方基本权利”的定性。", "evidence": "P006", "ambiguity": "红线内容由提问情境推出，正文未逐条列明"},
    {"term": "补发讣告", "meaning": "作者对分手的定性：关系事实上已崩溃，分手只是追认。", "evidence": "P008", "ambiguity": "比喻，未界定关系崩溃的判定标准"},
    {"term": "统治/奴仆", "meaning": "作者描述疾言厉色式攻击所发出的信号：惩罚对方不接受自己的统治，对方没有必要来当奴仆。", "evidence": "P020", "ambiguity": "修辞用词，非制度性概念"},
    {"term": "发现了分歧", "meaning": "作者对首次发现对方不符合自己原则时伦理关系的重新定性，与“对方有错，应当受罚”相对。", "evidence": "P023", "ambiguity": "与 P006“预先答应的前提”如何并存，正文未说明"}
   ],
   "examples_and_targets": [
    "男朋友在茶里下止痛药——提问者的情境，作者据此给出方案（Q001）",
    "野生老虎尝到人血的味道——类比，用来说明未受教训会再犯（P007）",
    "地基动摇、补发讣告——比喻（P008）",
    "过家家、彼此耽误彼此的人生——贬抑性比喻（P012）",
    "刮骨疗毒——比喻，说明短期剧痛换治愈（P015）",
    "沦为奴仆——比喻，说明若对方转不过弯则避免了坏结局（P015、P021）",
    "作者拟的道歉话术（引号内文字）——作者为读者提供的示范文本，不是作者对自身立场的陈述（P028、P029）",
    "“无论以任何理由都不欺骗”——作者评论并建议不宜说的对象（P032）",
    "当事人已经写的道歉——作者对提问方后续动态的转述（P031）"
   ],
   "conditions": [
    "方案以“只有一种解决办法”的排他语气给出（P002）",
    "前提条件：“在预先答应的前提下直接违背双方明确共识”（P006）",
    "假设条件：“如果没有立刻给予足够负面的信息形成‘此事绝对得不偿失’的事实教训”（P007）",
    "让步限定：“这并不必然意味着这关系就此万劫不复了”（P009）",
    "重生条件：“如果对方能穿越由此而来的痛苦、不服气……怨恨……能以真诚抱歉、没有怨恨、认同你的分手决定确实并非没有道理的状态给你回应”（P010）",
    "排他条件：“只有经过分手，经过以分手为必经之路的基本共识的重新修订，这个关系才可以继续。否则勉强继续，必无善了”（P013）",
    "后果假设：“那时候如果婚已经结了、孩子也生了、工也辞了”（P014）",
    "分岔条件：“若对方确实转不过这个弯”（P015）",
    "适用关系限定：“当你首次发现对方不符合这个原则时”（P022）；“这是你的原则，不是经过对方同意答应遵守的共识”（P025）",
    "对对方的条件：“如果你确实觉得你的想法是对的”（P029）"
   ],
   "rhetoric_and_tone": "第二人称训诫式，短句断言密集，穿插反问（“你凭什么教育对方？”“那么，对方又有什么必要上赶着来当你的奴仆呢？”“比此刻分手惨烈何止百倍？”）；比喻强烈（涅槃重生、老虎尝血、地基与讣告、刮骨疗毒、奴仆、过家家）；用“1）2）”编号给出执行细则，末尾嵌入对话式道歉范文并对当事人作点评，语气冷静而强硬。",
   "unresolved_questions": [
    "P006 称“在预先答应的前提下”，P025 又称“这是你的原则，不是经过对方同意答应遵守的共识”，两处前提不一致，正文未说明哪一个成立。",
    "P031“看到当事人已经写了道歉”指谁写的道歉、作者从何处看到，均未说明。",
    "提问者所说“出于好心”的具体情形、下药是否造成后果、事后沟通情况，正文未涉及。",
    "“涅槃重生”“红线”“这的确是事实”等关键判定的具体标准未说明。",
    "分手后再复合的时间、步骤与可行性未说明。",
    "P028、P029 引号内文字是作者建议读者对对方说的话，不能当作作者自身立场或作者对提问者的评价。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "愤怒是没用的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这种事只有一种解决办法，就是分手再看能不能复合。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "只有涅槃重生才能压制这种级别的过犯", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "“关系存续”本身在以最大事实的身份证明“这不是一个真正要紧的问题”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "在预先答应的前提下直接违背双方明确共识、直接践踏对方的基本权利", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "如果没有立刻给予足够负面的信息形成“此事绝对得不偿失”的事实教训", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "关系事实上已经崩溃，分手不是在杀死关系，而不过是在补发讣告而已。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "这并不必然意味着这关系就此万劫不复了。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P010", "quote": "那么这份感情可以重生。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P013", "quote": "只有经过分手，经过以分手为必经之路的基本共识的重新修订，这个关系才可以继续。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "比此刻分手惨烈何止百倍？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "若对方确实转不过这个弯，那么你只是躲过了一个沦为奴仆的未来。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P016", "quote": "含糊过去，它甚至将成为“这样没啥不行”的事实依据，贻害至烈。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "不要用愤怒去驱动执行。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "它不可以通过疾言厉色的批评指责来实施。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "不是要人尊重你的原则，而是在惩罚人不接受你的统治。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "当你首次发现对方不符合这个原则时的伦理关系并不是“对方有错，应当受罚”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "对方并不存在理所当然的过错。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P025", "quote": "你有权痛苦，但无权对对方发泄情绪，无权伤害对方。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P026", "quote": "以补充信息、正式告知的姿态，解释你的立场。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P027", "quote": "你有必要向对方抱歉——", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P028", "quote": "我没有在这之前足够清晰明确的告诉你我的这一条别扭之处。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P029", "quote": "但这些并没有改变这是我无法接受的原则的事实。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P031", "quote": "看到当事人已经写了道歉。从文字上看也算过关了。", "relation": "context"},
    {"key": "E25", "paragraph_id": "P032", "quote": "不过“无论以任何理由都不欺骗”这样许愿发誓的话不宜说。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系伦理", "冲突处理", "沟通方法"],
   "issue_candidates": ["伴侣擅自在茶里下药", "关系中的原则与共识", "分手作为重建关系的必经之路"],
   "text_function_candidates": ["答疑", "行动建议", "训诫", "示范话术"],
   "object_candidates": ["提问者", "提问者的男朋友"],
   "working_keywords": ["愤怒", "分手", "涅槃重生", "关系存续", "红线", "共识", "奴仆"]
  },
  "notes": "无图片节点。作者不判定“谁的错”，而给分手方案与执行注意事项；引号内道歉话术是作者拟给读者的示范文本，不得当作作者自身立场。P006 与 P025 对“是否存在预先共识”的表述不一致，已记入未决问题。"
 },
 "769c9d9a": {
  "analysis": {
   "question_context": "提问者问如何看待天津一老师对比家长收入、称「你妈妈挣多少钱，别怪我瞧不起你」，以及暴露了哪些问题。作者先规定“怎么看”这类问题应有的回答方式（不作褒贬宣判，而给应对方案与论据），再把要害定为“家长们可以怎么办”；作者未直接判定该老师对错，而是追问是否该向子女维持完美世界幻想等一系列前提问题，文章以“（未完，待续）”结束，承诺的“怎么对子女解说”未在本文给出。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "提出“怎么看”类问题的回答规范：不应以个人褒贬为最终回应，应给出基于价值观的应对方案、执行细则、逻辑与论据。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "定出本题要害：家长们可以怎么办；首先要问这是不是一件坏事。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012"], "summary": "指出事情没有看起来那么简单：对老师的愤怒不意味着老师就错了，可能人家说的是事实而批评者只有zz正确；反问维持完美世界幻象为何正确。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "列举孩子被告知的一系列美好命题并反问世界是否如此；追问为何要竭力维持这种默认印象并对揭破者怒不可遏；强调先回答才能有判定“坏事、应制止”的基本立场。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019"], "summary": "追问为何让孩子相信美好但不存在、不符合事实的世界幻想，再让ta们离开羽翼后经历几乎必然的世界观崩溃，以及为何这一定是更好的安排。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "若答不出来，愤怒只是被嵌入的潜意识，是被教育、传统与大众风潮决定的安排；写程序者也许有理，但读者自己的理由与赞同理由不明。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027"], "summary": "先想清为何应反对或不反对才能谈怎么办；并追问为何不让这位老师提前代言社会衡量价值的做法、让子女提前适应现实。", "role": "transition"},
    {"unit_id": "U008", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032"], "summary": "要害在父母、老师是受托不可作恶之人：父母不能自己骗孩子以“提前适应被欺骗”，老师作为“代理父母”继承同样禁忌，不能成为“必然挑战的代言人”。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P033", "P034", "P035"], "summary": "父母被剥夺“自己骗一骗孩子来教孩子防骗”的选择，因为负有爱的义务；给子女痛苦教育的特殊权限“在世界手里”；禁止老师歧视分化是职业伦理要求，并非为营造童话世界。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P036", "P037", "P038", "P039"], "summary": "“故意营造童话世界”也是大忌：不可灌输完美世界幻觉，那不叫保护童真而是不诚实；可按认知由基础到高深的客观限制逐步展示真实图景，但不得打着保护童真的旗号有意维持幻觉。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P040", "P041", "P042"], "summary": "后果：子女会与真实世界迎头相撞、灵魂撕裂、极可能严重抑郁；反对老师“不加害”与反对灌输幻觉是两个不同伦理法则下的并行不悖结论，同时成立。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P043", "P044", "P045"], "summary": "承诺回答“子女遇到这种事情可以怎么对子女解说”，称这才是“怎么看”真正应该结出的果子；文末标“（未完，待续）”。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "凡“怎么看”这类问题，都不应该以表达个人的褒贬为最终的回应；立场可以有，但真正对读者有意义的是立场背后的依据和价值观体系。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正对人有意义的参考不是宣判这事是正义还是邪恶，而是给出基于这种价值观、遇到这事可能怎么应对。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要提供应对的方案、执行细则和背后的逻辑以及论据，这样才能降低对他人时间的浪费。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在这个问题里，最大的要害就是家长们可以怎么办。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这是不是一件坏事，没有看起来那么简单。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "人很容易对这位老师的言论感到愤怒，但这并不理所当然意味着老师就说错了——万一人家说的是事实，而批评者手里持有的不过是一种zz正确。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：为什么继续强制所有人与你们（愤怒者）合谋向子女维持一个完美世界的幻像是正确的。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者列举让孩子相信人人平等、世界一定公平待人、正义永远必胜、好人多、好心必有好报、诚实一定有好结果、努力一定带来成功、圣诞老人、牙仙，并反问“世界并不是这样，不是吗”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：为什么要在子女成长过程中竭力维持这种默认印象，以至于对任何可能揭破这些问题的一切怒不可遏、施以报复。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "要先回答了这个问题，家长才有判定这是件坏事、应该制止的基本立场。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：为什么要让孩子相信一个虽然美好但显然并不存在、并不符合事实的世界幻想，然后在ta们离开羽翼后经历一次逻辑上几乎必然的世界观崩溃；为什么这就一定是更好的安排。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果这里回答不出来，对这位老师的愤怒情绪就只是一种被嵌入的潜意识——不是自己的决定，而是通过教育、传统和大众风潮被决定的安排；只是被决定要愤怒而没有觉察程序是被人写入的。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有先想清楚了为什么应该反对或者不反对，才能考虑接下去要怎么办。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者提出：为什么不一开始就让将来子女走上社会必定会遇到的这种衡量ta价值的做法提前由这位老师代言出来、提前让子女去适应；难道提前适应真正的现实不好吗。", "evidence": ["E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里的要害在于，父母、老师，是受托不可作恶之人。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "孩子将来可能受别人的骗、难以避免，但这绝不意味着父母可以自己去骗ta，以“提前让ta适应被欺骗”。", "evidence": ["E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不但不能自己“安排提前适应”，父母还有责任尽一切可能去防范、避免和对抗这些尽管必然存在的风险。", "evidence": ["E23"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老师作为父母的受托代理人、“代理父母”，因接受委托契约而继承同样的伦理禁忌，所以老师并不能成为“必然挑战的代言人”。", "evidence": ["E24", "E25"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母被剥夺了“自己骗一骗孩子来教孩子防骗”的选择，因为负有当然的爱的义务；为子女准备这些“必然挑战”、给子女以痛苦的教育的特殊权限，在世界手里。", "evidence": ["E26", "E27"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不允许老师对孩子们做这样的歧视行为、分化行为，是出于老师职业伦理的要求，并不是出于“故意要营造完美的童话世界”。", "evidence": ["E28"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“故意营造童话世界”的确也是大忌；不可对子女灌输完美世界幻觉，这一条父母必须无条件牢记，那不叫“保护童真”，而实实在在只是对子女不诚实。", "evidence": ["E29", "E30"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "可以出于“概念构建存在从基础到高深的渐进过程”这一客观限制逐步对子女展示、讲述和解释世界的真实图景，这是合理而且显然应该如此的；但绝不能打着保护童真的旗号有意维持子女对世界的美好幻觉。", "evidence": ["E31", "E32"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "维持幻觉说穿了只是让父母享受子女幼态持续带来的本能愉悦、帮自己回避回答困难的问题、逃避必须承担的教育责任，而付出惨烈代价的是子女。", "evidence": ["E33"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "子女会与真实的世界迎头相撞，灵魂撕裂，极其可能患上严重的抑郁症，陷入极大的人生危机。", "evidence": ["E34"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反对这位老师抛弃代理父母的“不加害”行为，与反对对子女灌输完美世界幻觉，是由两个不同的伦理法则决定的两个并行不悖的结论，同时成立。", "evidence": ["E35", "E36"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在子女遇到了这种事情可以怎么对子女解说，才是“怎么看”真正应该结出的果子（该回答本文未给出，文末标“未完，待续”）。", "evidence": ["E37"]}
   ],
   "argument_steps": [
    "先立回答规范：这类“怎么看”不该以褒贬宣判作结，应给应对方案、细则、逻辑与论据（P001—P005）。",
    "把问题落到家长身上，并先追问“这是不是一件坏事”（P006、P007）。",
    "提出反驳方向：愤怒不代表老师错了，也可能人家说的是事实，批评者只有zz正确（P009、P010）。",
    "连续追问：为何维持完美世界幻象是正确的（P011—P012）。",
    "列举儿童被告知的美好命题，反问世界是否如此（P013、P014）。",
    "追问为何要维持默认印象并对揭破者报复（P015），强调先回答才有判定立场（P016）。",
    "追问为何让子女相信不存在的美好幻想、再经历几乎必然的世界观崩溃（P017—P019）。",
    "指出答不出来则愤怒只是被嵌入的潜意识与被写入的程序（P020—P024）。",
    "要求先想清反对或不反对，再谈怎么办（P025）。",
    "以反问提出“让老师提前代言社会衡量价值的做法”这一可能选项（P026、P027）。",
    "给出核心命题：父母、老师是受托不可作恶之人（P028）。",
    "以“孩子将来可能受骗”作类比，说明父母不能自己去骗孩子（P029），并指出父母有防范风险的责任（P030）。",
    "把老师界定为“代理父母”，推出老师不能成为“必然挑战的代言人”（P031、P032）。",
    "指出父母的爱的义务使其丧失“自己骗孩子教防骗”的选择；给子女痛苦教育的权限“在世界手里”（P033、P034）。",
    "区分两条伦理法则：禁老师歧视分化出于职业伦理，并非为营造童话世界（P035）。",
    "追加限定：营造童话世界同样是大忌，不可灌输完美世界幻觉（P036、P037）。",
    "给出可允许的做法：按认知渐进展示真实图景，但不得有意维持幻觉（P038、P039），并指出维持幻觉的动机与代价（P039、P040）。",
    "结论：两条结论并行不悖、同时成立（P041、P042）。",
    "最后承诺回答“怎么对子女解说”，但本文未给出，以“（未完，待续）”收束（P043—P045）。"
   ],
   "concept_usage": [
    {"term": "怎么看", "meaning": "提问句式；作者把它规定为不应以褒贬宣判作结，而应给出基于价值观的应对方案、执行细则、逻辑与论据。", "evidence": "P001", "ambiguity": "该回答规范是作者自定的写作要求，非提问者所提"},
    {"term": "zz正确", "meaning": "作者对批评该老师者所持立场的贬称，认为可能只是一种未经反思的正确。", "evidence": "P010", "ambiguity": "拼音缩写，正文未给出全称"},
    {"term": "代理父母", "meaning": "作者对老师身份的界定：父母的受托代理人，因委托契约继承父母“不可作恶”的伦理禁忌。", "evidence": "P031", "ambiguity": "委托契约的具体内容与范围未说明"},
    {"term": "受托不可作恶之人", "meaning": "作者对父母与老师伦理位置的概括：受委托因而不可加害。", "evidence": "P028", "ambiguity": "未说明该伦理原则的来源"},
    {"term": "必然挑战", "meaning": "作者指子女走上社会后必然遇到、会带来痛苦的现实挑战（如被骗、被以收入衡量价值）；其教育权限作者称“在世界手里”。", "evidence": "P034", "ambiguity": "“世界”作为授权主体的说法未界定"},
    {"term": "幼态持续", "meaning": "作者用来说明父母维持子女对世界美好幻觉所获得的本能愉悦。", "evidence": "P039", "ambiguity": "借用词，未给出定义"},
    {"term": "完美世界幻觉/童话世界", "meaning": "作者指父母有意维持的、与世界事实不符的美好印象；作者认为营造它是大忌。", "evidence": "P036", "ambiguity": "与“按认知渐进展示真实图景”的界限未给操作标准"}
   ],
   "examples_and_targets": [
    "天津一老师对比家长收入、称「你妈妈挣多少钱，别怪我瞧不起你」——提问者给出的评论对象；作者未复述该言论细节，也未直接判定其对错（Q001）",
    "人人平等、世界一定公平待人、正义永远必胜、好人多、好心有好报、诚实有好结果、努力一定成功、圣诞老人、牙仙——作者列举的“完美世界”信念（P013）",
    "父母的受托代理人、代理父母——作者界定老师身份的角色用词（P031）",
    "教育、传统和大众风潮、写这程序的一方——作者解释愤怒来源时的用语（P020、P022）",
    "“（未完，待续）”——文末结构标记（P045）"
   ],
   "conditions": [
    "适用范围限定：“凡这类问题”（P002）",
    "对象限定为家长：“在这个问题里，最大的要害就是家长们可以怎么办”（P006）",
    "条件推论：“如果这里回答不出来，你对这位老师的愤怒情绪就只是一种被嵌入的潜意识”（P020）",
    "先后条件：“只有先想清楚了为什么应该反对或者不反对，你才能考虑接下去要怎么办”（P025）",
    "允许做法及其限制：“你可以出于‘概念构建存在从基础到高深的渐进过程’这一客观的限制逐步的去对子女展示、讲述和解释这个世界的真实图景”，但“绝不能打着保护童真的旗号有意的维持子女对世界的美好幻觉”（P038、P039）",
    "对老师的判定不以“必然挑战”为由而正当（P032、P035）",
    "文章未完成：所承诺的“怎么对子女解说”在本文中未给出（P045）"
   ],
   "rhetoric_and_tone": "论辩与层层追问为主，连续反问与排比（P013 一连串“相信……”、P017 连续“为什么”）；第二人称“你们”直指愤怒的公众与家长，带训诫与挑战意味；用“zz正确”“程序是被人写入的”“迅雷不及掩耳的愤怒”等带讽刺色彩的表述；结构上先立回答规范，再逐层追问，最后承诺解法却以“（未完，待续）”收束。",
   "unresolved_questions": [
    "文章以“（未完，待续）”结束，正文承诺的“现在子女遇到了这种事情，可以怎么对子女解说”没有给出，需后续篇或复核。",
    "“天津一老师”事件的原话与处理结果正文未提供，作者也未复述，仅有提问者的转述，需外部核查。",
    "作者未直接回答该老师是否错了、是否应受处理，只提出应先回答一连串前提问题；不能把作者的追问当成结论。",
    "P003“遇到这事以作者的见解而言可能怎么应对”以第三人称指称作者自己，属文本疑点，按原文保留。",
    "“你们”“写这程序的一方”的指称对象（愤怒的公众、教育/传统/大众风潮）未明确界定。",
    "“世界手里”的“世界”作为授予特殊权限的主体，含义未说明。",
    "P031“同样的的伦理禁忌”有重复字，按原文保留。",
    "lexical 统计显示本篇含 1 个 heading 节点，阅读包正文分段中未见与之对应的独立标题文本，标题层级需核对。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "凡这类问题，都不应该以表达个人的褒贬为最终的回应。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "不是基于这种价值观去宣判这事是正义的还是邪恶的", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "要提供一个应对的方案、执行细则和背后的逻辑以及论据。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这样才能降低对他人时间的浪费。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "在这个问题里，最大的要害就是家长们可以怎么办。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "这没有看起来那么简单。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P009", "quote": "人很容易会对这个老师的言论感到愤怒", "relation": "context"},
    {"key": "E8", "paragraph_id": "P010", "quote": "这并不就理所当然的意味着这老师就说错了。万一人家说的事实呢？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "为什么继续强制所有人与你们合谋向子女维持一个完美世界的幻像是正确的？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "为什么要让孩子们相信这个世界是人人平等的？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "世界并不是这样，不是吗？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "以至于要对任何可能揭破这些问题的一切怒不可遏、施以报复？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "要先回答了这个问题，你们才有判定这是件坏事、应该制止的基本立场。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P017", "quote": "然后在将来ta们离开你的羽翼之后经历一次逻辑上几乎必然的世界观的崩溃？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "为什么这就一定是更好的安排？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "你对这位老师的愤怒情绪就只是一种被嵌入的潜意识。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "你只是被决定要对此愤怒，而又没有觉察到这程序是被人写入的罢了。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "只有先想清楚了为什么应该反对或者不反对，你才能考虑接下去要怎么办。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "为什么不一开始就让将来子女走上社会必定会遇到的这种衡量ta价值的做法提前由这位老师代言出来", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P027", "quote": "难道提前适应真正的现实不好吗？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P028", "quote": "这里的要害在于，父母、老师，是受托不可作恶之人。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P029", "quote": "但这绝不意味着你可以自己去骗ta，以“提前让ta适应被欺骗”。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P030", "quote": "父母还有责任尽一切可能去防范、避免和对抗这些尽管是必然存在的风险的责任。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P031", "quote": "理所当然的因接受委托契约而继承同样的的伦理禁忌。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P032", "quote": "所以老师并不能成为“必然挑战的代言人”。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P033", "quote": "父母们被剥夺了“自己骗一骗孩子来教孩子防骗”的选择，因为父母们负有当然的爱的义务。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P034", "quote": "为子女们准备这些“必然挑战”、在这些“必然挑战”给子女以痛苦的教育的特殊权限，在世界手里。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "是出于老师的职业伦理而存在的要求，并不是出于“故意要营造完美的童话世界”。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "“故意营造童话世界”的确也是大忌。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "那不叫什么“保护童真”，而实实在在只是对子女不诚实。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P038", "quote": "这是合理而且显然应该如此的。", "relation": "qualifies"},
    {"key": "E32", "paragraph_id": "P039", "quote": "你绝不能打着保护童真的旗号有意的维持子女对世界的美好幻觉。", "relation": "qualifies"},
    {"key": "E33", "paragraph_id": "P039", "quote": "帮你自己回避回答困难的问题、逃避必须承担的教育责任", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P040", "quote": "极其可能患上严重的抑郁症，陷入极大的人生危机。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P041", "quote": "是由两个不同的伦理法则决定的两个并行不悖的结论。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P042", "quote": "同时成立。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P044", "quote": "这才是“怎么看”真正应该结出的果子。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育伦理", "亲子关系", "社会价值观", "教师职业伦理"],
   "issue_candidates": ["教师以家长收入羞辱学生", "是否向儿童维持完美世界幻想", "父母与教师的不可加害义务"],
   "text_function_candidates": ["答疑", "论辩", "追问式批评", "未完待续"],
   "object_candidates": ["天津某教师", "家长", "学生", "学校", "教育部门"],
   "working_keywords": ["怎么看", "zz正确", "代理父母", "受托不可作恶", "完美世界幻觉", "保护童真", "必然挑战"]
  },
  "notes": "无图片节点。提问者引述的教师言论属提问材料，作者未复述也未直接判定其是非；“zz正确”等按原文保留。文章以“（未完，待续）”结束，承诺的“怎么对子女解说”未给出，已在未决问题登记。lexical 含 1 个 heading 节点但正文分段未见对应标题文本，待核对。"
 },
 "abaedfb0": {
  "analysis": {
   "question_context": "提问者问如何看待男同事“不是男女平等吗？换桶装水你们也可以干”的言论。作者没有讨论该言论是否构成歧视或男女平等议题本身，而是接受“可以干”的说法，给出若干替代性解决办法（改喝瓶装水、买抽提器、换企业或自己开企业），并主张等真解决不了再认输。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回应：当然可以干，这有什么问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "替代办法：改喝瓶装水、多给搬水工费用或选可帮换装的送水服务、买直接装桶口的抽提器。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "或者换一家没这种人的企业；或者开一家没这种人的企业。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "这些都是很好的解决办法；等真的解决不了再认输不迟。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问回应：当然可以干，这有什么问题。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "替代办法是改喝瓶装水，多给搬水工点换装费用或者选可以帮换装的送水服务，买直接装桶口的抽提器。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "或者换一家没这种人的企业；或者开一家没这种人的企业。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这都是很好的解决这一问题的办法。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "等真的解决不了再认输不迟。", "evidence": ["E6"]}
   ],
   "argument_steps": [
    "先接受“可以干”的说法并用反问收束（P001）。",
    "给出替代用水与换水方式的方案（P002）。",
    "给出退出或创业的选项（P003、P004）。",
    "总体肯定这些办法并给出“认输”的时机（P005、P006）。"
   ],
   "concept_usage": [
    {"term": "可以干", "meaning": "作者对男同事说法的回应：换桶装水这件事女同事确实可以干，不构成问题。", "evidence": "P001", "ambiguity": "作者未讨论体力差异、工作分工或是否属于性别歧视"},
    {"term": "换装费用", "meaning": "作者建议多给搬水工的费用项，按原文如此。", "evidence": "P002", "ambiguity": "疑为“换桶费用”之误，含义不确定"},
    {"term": "认输", "meaning": "作者建议在所有替代办法都无效后才接受的结局。", "evidence": "P006", "ambiguity": "未说明认输的具体所指（不换水，还是在平等争论中认输）"}
   ],
   "examples_and_targets": [
    "男同事“换桶装水你们也可以干”的言论——提问者引述的评论对象，作者未评价其是否构成歧视（Q001）",
    "桶装水、瓶装水、装桶口的抽提器、搬水工、送水服务——作者提出的替代方案材料（P002）",
    "“没这种人的企业”——作者提出的换职与创业选项（P003、P004）"
   ],
   "conditions": [
    "以让步语气回应：“当然可以干”（P001）",
    "建议以“或者”表示可选项（P002—P004）",
    "给出认输的条件：“等真的解决不了再认输不迟”（P006）"
   ],
   "rhetoric_and_tone": "极简短的回答体，口语化、以反问“这有什么问题？”带过；办法以并列清单给出，不展开论证；对提问者的性别议题不作评价。",
   "unresolved_questions": [
    "作者未回答男同事言论是否构成性别歧视，也未讨论男女平等议题本身。",
    "P002“多给搬水工点换装费用”中的“换装费用”疑为“换桶费用”之误，按原文保留，含义需核对。",
    "“认输”的具体所指（是不换水，还是在平等争论中认输）未说明。",
    "提问者所在企业的具体情况、是否被强制要求换水，正文未涉及。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "当然可以干，这有什么问题？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "改喝瓶装水，多给搬水工点换装费用或者选可以帮换装的送水服务，买直接装桶口的抽提器。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "或者换一家没这种人的企业。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "或者开一家没这种人的企业。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这都是很好的解决这一问题的办法。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "等真的解决不了再认输不迟。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场关系", "性别议题", "日常办公事务"],
   "issue_candidates": ["换桶装水与男女平等", "职场中的替代性解决方案"],
   "text_function_candidates": ["答疑", "行动建议"],
   "object_candidates": ["男同事", "企业", "搬水工"],
   "working_keywords": ["男女平等", "换桶装水", "瓶装水", "抽提器", "认输"]
  },
  "notes": "无图片。正文极短（6段），为建议清单；作者未评价男同事言论的对错，也未讨论性别平等争议本身。“换装费用”按原文保留，疑为“换桶费用”。"
 },
 "95d56649": {
  "analysis": {
   "question_context": "提问者问“怎么样和朋友合伙做生意能成功”。作者先指出这一提法本身是伪命题（人只能与朋友合伙，成功企业创业阶段的领导团队也几乎必是朋友），把真问题改写为“和什么样的朋友合伙”，再区分两种“友情观”，论证只有把友谊理解为“负有更多尊重权利边界义务”的那一种才可以合伙，并在结尾主动限定这不能保证成功。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "该问题是伪命题：人只能与朋友合伙，成功企业创业阶段领导团队几乎必是朋友；真问题是和什么样的朋友合伙。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009"], "summary": "关键在“友情观”：朋友是自认拥有越界特权的人，还是自觉负有更多尊重权利边界义务的人；只有后者才可以合伙。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "第一种朋友观下，你会把对越界的容忍折价计入“友谊存量账户”；而对方认为越界收益本就是“作为朋友应有的收益”，故余额低于你的预期；若全部要全额奉还，交朋友就“没有意义”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"], "summary": "ta们提供的是“保安服务”而非“存款服务”：需定期缴维持费用；以保安公司安装远程报警系统、收安装费月费与出动费作类比。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"], "summary": "因出动请求无上限，对价需替换为“自由的越界权”；真到出动时是否值得出动是魔鬼般的考验，现代熟人社会崩解后总有选择违约而非出动的时刻。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P022"], "summary": "这种朋友观本是为塞外屯垦、应对游牧劫掠的开垦团文化准备的，不是为合伙经营准备的。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027"], "summary": "第二种朋友观相反：以比他人更高标准保护对方权利，加倍将自身利益后置；越界之事别人可做而朋友特别不能做。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032", "P033"], "summary": "有帮助义务不等于可以“全面知情”“全面干预”；这类做法是提前实践侵害，用可能付出的代价为现实侵害辩护不一定成立。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P034", "P035", "P036"], "summary": "亲密与尊重不来自“可越界而不受罚”，这是因果倒置；朋友因高度尊重界限而被授予特权，与擅自夺取特权不同。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P037", "P038", "P039", "P040"], "summary": "“不可以和朋友合伙做生意”流传的原因，是主流朋友观不把这种关系看作朋友；作者认为他们错了，令他们是对的时代已过去。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P041", "P042"], "summary": "结论：当然要和朋友们合伙，只需分清哪种朋友适合合伙；但这不能保证成功。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "人当然是和自己的朋友合伙，难道和仇人或者毫无认同和友谊的人合伙吗。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "成功的企业至少在其创业阶段，其领导团队不是朋友几乎是不可能的；即使不是故交，也一定是再三交往建立起了友谊才谈到合伙的。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以“和朋友合伙是否可以成功”完全是个伪命题——失败的固然是朋友合伙，但是成功的也是朋友合伙。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题不是和朋友合伙还是和非朋友合伙，而是和什么样的朋友合伙。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "要害在“友情观”：所谓朋友，到底是自认拥有越过权利边界特权的人，还是自觉负有更多尊重权利边界义务的人。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有后一种朋友观下的朋友才可以合伙。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "前一种朋友观下的朋友，虽不至于百分之百，但有很大概率在你提出“最起码的要求”时觉得你也不值得ta作“那么大的牺牲”。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为在提出“起码的要求”时，你是把对ta一次次越线的容忍折价计算进了“友谊存量账户”，据此计算要求不应透支、应该获准。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "但信奉第一种朋友观的朋友并不这样看：在ta们的价值观里，越界和越界带来的收益属于“作为朋友应有的收益”，账户余额多半低于（甚至远低于）你的预期。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "落差的原因：如果从你这里得到的全部都要全额奉还，那么交你这个朋友就“有什么意义”、“还算什么朋友”。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在ta们的感受里，ta们提供的是“保安服务”，而不是“存款服务”，即你需要定期缴纳维持费用。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这包括随时赞同你的观点、随时帮你站台、随时提供其职权的方便；不是一定要真的提供服务，而是保持这些服务在你心理上的可得性，已算友谊的实质性内容，并作为“自主越过边界”特权对等的报酬。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "就像保安公司为你加装远程报警系统并保持在线：收取安装费和月使用费；月费在当月已被警戒服务抵消、并无余额；真正需要行动时另有行动费用，且以按月缴纳警戒费用为前提，不缴则不提供出动；“有出价要求出动的机会”本身就是给你的回报和福利。", "evidence": ["E14"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因被请求出动的事情理论上没有上限（“两肋插刀”“赴汤蹈火”），所以“每月固定缴费”这种级别的对价并不足够，需要替换成为“自由的越界权”；开侮辱性玩笑、不告而借/取私人用品、自由占用时间只是其最轻微的应用。", "evidence": ["E15", "E16"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真到出动时，“最轻微的应用”总和是否值得出动是非常微妙的问题，常是“风险是否威胁持续经营”“对方是否有支付能力和支付意愿”“违约风险和出动风险谁更大”的魔鬼般的考验。", "evidence": ["E17", "E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "总有得出“与其冒出动风险，不如冒违约风险”结论的时候——尤其在现代熟人社会已崩解、由熟人社会信用体系支撑的道德审判体系已不复存在，ta确实背叛了友谊，但因此失去的并不多。", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种“自主越界的保安公司”模式的朋友观一开始就不是为“合伙经营”准备的，而是为在塞外抱团屯垦、随时应对北方游牧民族劫掠的开垦团文化准备的。", "evidence": ["E20"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二种朋友观近乎完全相反：把“以比他人更高的标准来保护对方的权利”视为友谊的根本内容，不但不谋求越界，反而加倍将自身利益后置，以最大程度降低对方合法权利受损的可能。", "evidence": ["E21", "E22"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越界的事（窥探隐私、出卖隐私、借便利占用财物、借交情绑架获取帮助）别人可以做，作为朋友不但不是“更可以做”，反而特别不能做；外人可以打听收入、八卦感情、挖掘个人情报、点评举止、随时给忠告、指责不顾念交情，“作为朋友，我不可以”。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "我知道你出事、我多少会受到牵连、有帮助的义务，但这不意味着我因此可以管你的事，更不用说“全面知情”和“全面干预”。", "evidence": ["E26"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "全面知情、全面干预无非是不甘心为自己没有说话权的决定付出连带代价；但付不付出代价本来就不受强迫，对方也无权强迫，你也未必真会付出多少代价，而“全面知情”和“全面干预”却已经实践起来，界限已被跨过、权利已被干扰和剥夺。", "evidence": ["E27", "E28"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "用可能付出的代价为现实侵害的正当理由，不一定成立；对方是否真的肯定接受这种安排也无法断言。", "evidence": ["E29", "E30"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作为朋友，亲密和尊重不是来自“可以越过一般人不能越过的界限而不受惩罚”，这恰恰是因果倒置。", "evidence": ["E31"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "朋友是因为高度尊重对方的界限，而特别容易被授予外人所不被允许享有、只能靠自己窃取和强夺的特权；前者是擅自夺取特权并借朋友身份逃脱惩罚，后者是因让人不必忧虑滥用、因深入合作的需要而得到特殊许可。", "evidence": ["E32", "E33"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不可以和朋友合伙做生意”广为流传，是因为在主流朋友观里，“格外尊重界限，也要求格外尊重界限”的关系不被看成朋友。", "evidence": ["E34", "E35"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "但其实ta们是错的——准确的说，令ta们是对的的时代已经过去了。", "evidence": ["E36"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你当然要和朋友们合伙，只是需要分清楚什么才是可以适应合伙关系的朋友。", "evidence": ["E37"]},
    {"claim_id": "C028", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "另外，这不能保证你们合伙就可以“成功”。", "evidence": ["E38"]}
   ],
   "argument_steps": [
    "以反问否定提问的提法：人只能与朋友合伙（P001）。",
    "以创业团队构成为据，说明成功企业创业阶段几乎不可能不是朋友（P002）。",
    "判定“和朋友合伙是否可以成功”是伪命题（P003），把问题改写为“和什么样的朋友合伙”（P004）。",
    "引入两种“友情观”的对照，并判定只有第二种才可以合伙（P005—P009）。",
    "展开第一种朋友观：你的“友谊存量账户”计算与对方的“应得收益”理解存在结构性落差（P010—P013）。",
    "用保安公司与远程报警系统的类比说明第一种朋友观的运作方式与收费逻辑（P014—P016）。",
    "说明因出动请求无上限而出现的“自由的越界权”，以及真正出动时的风险计算（P017—P020）。",
    "指出现代熟人社会崩解后，选择违约而非出动成为可能（P021）。",
    "追溯第一种朋友观来自塞外开垦团文化，不适用于合伙经营（P022）。",
    "正面展开第二种朋友观：更高标准保护对方权利、越界之事朋友特别不能做（P023—P027）。",
    "反驳“有帮助义务就有全面知情、全面干预之权”：这是以可能的代价为已发生的侵害辩护（P028—P033）。",
    "指出亲密与尊重来自尊重界限而非越界特权，区分授权与擅夺两种特权路径（P034—P036）。",
    "解释“不可以和朋友合伙做生意”流行的原因，并判定这种朋友观已过时（P037—P040）。",
    "给出结论：当然要与朋友合伙，但须分清哪种朋友适合，且不保证成功（P041、P042）。"
   ],
   "concept_usage": [
    {"term": "伪命题", "meaning": "作者对“和朋友合伙是否可以成功”这一提法的定性：失败与成功的都是朋友合伙，提法本身失去区分力。", "evidence": "P003", "ambiguity": "作者未否认失败案例存在，只否认该提法有区分力"},
    {"term": "友情观", "meaning": "作者区分的第一种（自认拥有越界特权）与第二种（自觉负有更多尊重权利边界义务）两种友谊理解。", "evidence": "P005", "ambiguity": "只给出两极，未说明中间形态"},
    {"term": "友谊存量账户", "meaning": "作者用来描述把对越界的容忍折价计入、据此计算要求是否透支的隐喻账户。", "evidence": "P011", "ambiguity": "作者称之为“你的”计算方式，非对方认同的账户"},
    {"term": "保安服务/存款服务", "meaning": "第一种朋友观下友谊的实质：定期缴纳维持费用以保持支持的可得性；作者认为它不是可供支取的存款。", "evidence": "P014", "ambiguity": "类比，未给出费用与服务的具体对应"},
    {"term": "自由的越界权", "meaning": "第一种朋友观下，因出动请求无上限而形成的、以自由越界为对价的特权。", "evidence": "P017", "ambiguity": "作者自创的概括用语"},
    {"term": "全面知情/全面干预", "meaning": "作者所批评的、以“有帮助义务”“会受牵连”为由介入朋友事务的做法。", "evidence": "P028", "ambiguity": "未界定帮助义务与干预之间的界线"},
    {"term": "开垦团文化", "meaning": "作者认为第一种朋友观的历史来源：塞外抱团屯垦、随时应对北方游牧民族劫掠的群体。", "evidence": "P022", "ambiguity": "历史断言，正文未给依据，需外部核查"}
   ],
   "examples_and_targets": [
    "“不可以和朋友合伙做生意”——被作者反驳的流行说法（P037—P039）",
    "保安公司加装远程报警系统、收取安装费与月使用费、另收行动费——作者的核心类比（P016）",
    "“两肋插刀”“赴汤蹈火”——作者引用的俗语，用来说明出动请求无上限（P017）",
    "开侮辱性玩笑、不告而借/而取私人用品、自由占用时间——第一种朋友观下越界的最轻微应用（P018）",
    "窥探隐私、出卖隐私、借便利占用财物、借交情绑架获取帮助——作者列举的越界行为（P025）",
    "打听收入、八卦感情花边、挖掘个人情报、点评行为举止、随时给忠告、指责不顾念亲戚乡亲同学的交情——作者列举外人可做而朋友不可做的事（P026）",
    "塞外抱团屯垦、北方游牧民族劫掠的开垦团——作者对第一种朋友观来源的历史叙述（P022）",
    "熟人社会崩解、由熟人社会信用体系支撑的道德审判体系不复存在——作者对现代处境的判断（P021）"
   ],
   "conditions": [
    "范围与程度限定：“至少在其创业阶段”“几乎是不可能的”“即使不是故交，也一定是再三交往建立起了友谊才谈到合伙的”（P002）",
    "或然限定：“虽不至于百分之百，但是有很大概率”（P010）、“多半会低于（甚至远低于）”（P012）、“常常是”（P020）",
    "条件句：“如果从你这里得到的全部都要全额奉还”（P013）、“如果不按月缴纳，那么自然也不提供出动服务了”（P016）",
    "前提：“需要行动时可以在收取行动费用的前提下安排出动，是以每月按时缴纳警戒费用为前提的”（P016）",
    "身份限定：“作为朋友，我不可以”（P027）等以朋友身份划界的表述",
    "结论限定：“另外，这不能保证你们合伙就可以‘成功’”（P042）"
   ],
   "rhetoric_and_tone": "第二人称说理与训诫（“你一定要记清楚”“你当然要和朋友们合伙”）；大量经济与商业隐喻（友谊存量账户、保安服务与存款服务、安装费月费行动费、违约风险）；反问密集（“难道和仇人或者毫无认同和友谊的人合伙吗？”“否则叫什么朋友呢？”“还算什么朋友呢？”）；结尾以“天已经亮了，有些人还没有睡醒罢了”讽刺收束，并主动加上“不保证成功”的限定。",
   "unresolved_questions": [
    "对“第一种朋友观”人群的描述（如把越界收益视为应得）是概括，正文未给调查或例证来源。",
    "P022 关于第一种朋友观源自塞外开垦团文化的说法是历史断言，正文未给依据，需外部核查。",
    "“熟人社会已经崩解”“道德审判体系已经不复存在”为作者对现代社会的判断，未给论证。",
    "“友谊存量账户”“自由的越界权”“保安服务”等均为作者自创隐喻，未给出可操作定义或边界。",
    "文章未说明如何在实际中辨认一个人属于哪种朋友观，也未涉及合伙协议、股权等具体安排。",
    "作者既称只有第二种朋友观下的朋友才可以合伙，又承认这不能保证成功，二者是必要条件与不充分条件的关系，正文未明确说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人当然是和自己的朋友合伙，难道和仇人或者毫无认同和友谊的人合伙吗？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "成功的企业至少在其创业阶段，其领导团队不是朋友几乎是不可能的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "所以“和朋友合伙是否可以成功”完全是个伪命题", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "而是和什么样的朋友合伙。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "到底是自认拥有越过权利边界特权的人，", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "还是自觉负有更多尊重权利边界义务的人？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "只有后一种朋友观下的朋友、才可以合伙。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "但是有很大概率在你提出“最起码的要求”的时候会觉得你也不值得ta作“那么大的牺牲”。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "是把对ta一次次越线的容忍都折价计算进了你的“友谊存量账户”的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "这种越界和越界带来的收益属于“作为朋友应有的收益”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "那么交你这个朋友又“有什么意义”呢？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "ta们实际上提供的是一种“保安服务”，而不是一种“存款服务”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "而是保持这些服务在你心理上的可得性，已算友谊的实质性内容", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "为你加装了远程报警系统，并且保持着这个系统在线，向你收取安装费和月使用费", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "需要替换成为“自由的越界权”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "都只是这种“自由越界权”最轻微的应用而已。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "这是一个非常微妙的问题。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "“违约风险和出动的风险谁更大”的魔鬼般的考验。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "与其冒出动风险，不如冒违约风险", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "而是为在塞外抱团屯垦，随时要应对北方游牧民族劫掠的开垦团文化准备的。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "它把“以比他人更高的标准来保护对方的权利”视为友谊的根本内容。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "以最大程度的降低对方的合法权利受到损害的可能性。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "作为朋友，不但不是“更可以做”，反而是特别不能做。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "可以指责你怎么可以不顾念亲戚、乡亲、同学……的交情", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P027", "quote": "作为朋友，我不可以。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P028", "quote": "但是我并不认为这意味着我因此可以管你的事，更不用说“全面知情”和“全面干预”了。", "relation": "qualifies"},
    {"key": "E27", "paragraph_id": "P029", "quote": "全面知情、全面干预，无非是不甘心平白无故为自己没有说话权的决定付出连带代价，不是吗？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P031", "quote": "界限已被跨过、权利已被干扰和剥夺，现实的损害已经造成。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P032", "quote": "用可能付出的代价为现实侵害的正当理由，真的一定成立吗？", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P033", "quote": "对方真的肯定接受吗？", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P034", "quote": "不是来自于“可以越过一般人不能越过的界限而不受惩罚”。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P035", "quote": "而特别容易被授予外人所不被允许享有、只能靠自己窃取和强夺的特权。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P036", "quote": "前者是擅自夺取特权而借着朋友身份逃脱惩罚，后者是因为让人不必忧虑滥用、因为深入合作的需要而得到特殊许可。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P037", "quote": "为什么世上广为流传着“不可以和朋友合伙做生意”这样的话？", "relation": "context"},
    {"key": "E35", "paragraph_id": "P038", "quote": "不被看成朋友。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P039", "quote": "准确的说，令ta们是对的的时代已经过去了。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P041", "quote": "你只是需要分清楚什么才是可以适应合伙关系的朋友。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P042", "quote": "另外，这不能保证你们合伙就可以“成功”。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["友谊伦理", "合伙经营", "人际关系", "商业合作"],
   "issue_candidates": ["与朋友合伙能否成功", "权利边界与友谊", "越界特权与尊重义务"],
   "text_function_candidates": ["答疑", "论辩", "概念区分", "经验总结"],
   "object_candidates": ["朋友", "合伙人", "保安公司", "开垦团", "熟人社会"],
   "working_keywords": ["伪命题", "友情观", "权利边界", "友谊存量账户", "保安服务", "自由的越界权", "全面知情", "全面干预"]
  },
  "notes": "无图片。提问者的“怎么样……能成功”被作者改写为“和什么样的朋友合伙”；流行的“不可以和朋友合伙做生意”在文中是被反驳对象。开垦团来源、熟人社会崩解等均为作者的历史与社会断言，正文未给依据，已在未决问题登记。"
 },
 "acf8ecc5": {
  "analysis": {
   "question_context": "提问者问“对人类失望怎么办”。作者不把它当困难，而称这是好事：补上了世界观的大洞，可以正式开始建立人生观、价值观；随后分两点展开——（1）可以停止“换个对象/环境就会好”的想象，学会与问题共同存在、开始学游泳；（2）可以开始学习原谅整个人类，并主张爱不是可选项而是一种诫命、是让世界价值被看见的光，唯一能更改的变量只有自己。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007"], "summary": "定性：对人类失望是好事——补上世界观的大洞，可以开始人生观价值观；过了这个坎就海阔天空，而且非过不可。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "理由1：可以停止“不是我的期待有问题，而是这个人有问题，换一个人就好了”的想象；男友、老板、城市、国家的例子；没有人会真的让你满意。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018"], "summary": "必须学会与问题共同存在；不是说不能重新选择，而是换也免除不了问题，新开始只意味着同样问题以别的剧情、样式、烈度重现；所获只是喘息之机，是学游泳的机会；误以为上岸会被“意外呛水”击垮；世上本无岸。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024"], "summary": "痛苦比较：不放开“完美梦想”，虚无迷茫悲观绝望的痛苦就无限持续；可以停止“下次上岸”的幻想、开始学游泳；学游泳的痛苦不可回避，无论有无准备/条件/信心都只能向前；破釜沉舟时方法与解决未必难。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "世上没有完美的朋友、情人、上司、下属、老师、职业，也不可能通过选择达到幻灭前的标准；这不怪你，因认知必从简单开始且必相对完美、幻灭会反复发生；每次幻灭都逼到“不改变点什么，就接受败亡”，唯一选择是反思，归罪ta人与世界已无意义；不到此时不会承认原本自洽的一套不正确。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034"], "summary": "绝望是世界给人的教育，是必须领受、也是幸而必须领受的教育；痛苦只是成长过程；以毛毛虫化蝶比喻，并提醒别把茧结得太厚。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040"], "summary": "理由2：可以开始学习原谅整个人类——所有人都撒谎、偷窃、傲慢、虚伪、侵犯别人的自由，并无例外；因为所有人都可怜、无知、想活着，并无例外。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045"], "summary": "不是诚实的行为本身使人成为诚实的人，而是宽容的心使不够诚实的人被算为诚实；公平正义等美德乃至爱本身都因爱而被算为人做到了；不爱就没有动力宽容，没有宽容世界必终结于漆黑。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051"], "summary": "爱不是选择、可选的高尚行为或需要牺牲的无私奉献，而是一种诫命：若不守不行，世界会一天比一天黑暗；爱根本上是为了自己；爱是让世界价值被看见的光；世界深爱得令人嫉妒，只爱一个人（哪怕是自己）就算及格。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059"], "summary": "世界在眼里一天天昏暗、终局已可见；唯一可更改的变量只有自己；唯一解脱绝望的方向是自己开始学习爱、放下痛苦执着与“绝对合理理由”去宽容原谅；这是恰好能解决问题的唯一一条路，也是出路；结尾再恭喜。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对人类失望是好事：你终于可以正式开始来点人生观、价值观了，因为刚刚补上了最重要的世界观的大洞；这一条认知对做个稍微可以让人忍受的人有重大意义。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这绝对不是一件坏事，而是一件好事。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "过了这个坎，前头就是海阔天空、自由自在、无忧无虑；而且你非过不可。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到了这个点，你终于可以停止想象“不是我对人的期待有问题，而是这个人有问题，换一个人就会好了”。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到了这个点，你终于可以知道，没有人会真的让你满意的。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你必须要学会与这些问题共同存在，而不是只能转身逃走。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这不是说你不能重新选择，而是说即使要换，也要知道这并不意味着这些问题不必解决；新的对象、新的开始，一般只意味着同样的问题会以另一个剧情、另一种样式、另一种烈度重新浮现。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你所获得的，本质上只是一段宝贵的喘息之机，而并不是摆脱了问题；喘息之机是给你机会学游泳的。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果误把每一次喘息都当作已经上岸了，那么一次又一次的“意外呛水”最后会击垮你；更让人痛苦的是你以为已经上岸了，没想到其实还是在水里。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世上本无岸，只是希望的人多了、误以为自己已经上岸的喘息者多了，合谋编出来的幻觉罢了。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "只要你不放开“完美梦想”，虚无、迷茫、悲观乃至绝望的痛苦就是无限持续的。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在你可以停止“下次上岸”的幻想、开始学习游泳；学会游泳的痛苦不可回避，有准备也好、没准备也好，有条件也好、没条件也好，有信心也好、没信心也好，都只有向前挺进、向前努力。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "到了破釜沉舟、背水一战的时候，你会发现：当你不得不寻找方法，方法并不难找；当你不得不解决，解决未必有这么难。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上并没有完美的朋友、完美的情人、完美的上司、完美的下属、完美的老师、完美的职业；不是说你不能选择，而是说你不可能通过选择真正达到幻灭之前的标准。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这不怪你，因为人必定要从简单的认识开始逐步完成对世界的认知，而简单的认识必定会是一种相对完美的认识；不止初次的认知过于完美必将幻灭，幻灭之后再次建立起的完美想象仍将再次幻灭。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一次幻灭都会把你逼迫到“不改变点什么，就接受败亡”的绝境；你唯一的选择就是重新反思之前有什么东西想错了、什么事情做错了，因为这时归罪于ta人、归罪于世界已经没有意义。", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不到这种时候，人是不会承认自己原本自洽的那一套东西其实并不正确的（所以说，完全自洽是可耻的）。", "evidence": ["E20"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种绝望实际上是世界给人的教育，是人必须领受、也是幸而必须领受的教育；你现在所受的痛苦只是这种成长的一个过程。", "evidence": ["E21", "E22"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若不是戴着旧壳奇痒难当、生不如死，没有毛毛虫愿意撕心裂肺变成蝴蝶；所以恭喜你终于非化蝶不可，但要注意别把茧结得太厚，会死的。", "evidence": ["E23", "E24"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你终于可以开始学习原谅整个人类了：所有的人都撒谎、偷窃、傲慢、虚伪、侵犯别人的自由，并无例外；因为所有的人都可怜、无知、想活着，并无例外。", "evidence": ["E25", "E26"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是诚实的行为本身使得人成为诚实的人，而是宽容的心使得不够诚实的人被算为诚实的人；公平、正义等一切美德乃至爱本身，都是因为爱而被算为人做到了，都是因为被爱才在实践上存在。", "evidence": ["E27", "E28", "E29"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "你如果不爱，就不会有足够的动力宽容；没有足够的宽容，你的世界最后必定将终结于现在的一片伸手不见五指的漆黑；不能爱，就永远活在美德全部幻灭的地狱里。", "evidence": ["E30", "E31"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "爱其实不是一种选择、一种“可选的高尚行为”、一种“需要牺牲的无私奉献”，而是一种诫命：若不守、不行，世界就会一天比一天黑暗，直到在你眼里变成所有的人都是骗子、叛徒、盗匪的地狱。", "evidence": ["E32", "E33", "E34"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱不是为了“别人”、为了“祖国”、为了“全人类”，而根本的其实是为了你自己。", "evidence": ["E35"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱就是让这个世界的一切价值得以让你看见的光；若没有光照在它们身上，它们将淹没在完全的黑暗之中，化而为无。", "evidence": ["E36"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界对人深爱得令人嫉妒，允许你们只要哪怕学会一点、略有姿势地只爱一个人，哪怕这个人就是你自己，就算为你们及格，许你们享有足以支撑的幸福。", "evidence": ["E37"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你唯一真正可以更改的变量只有你自己；唯一能解脱绝望的方向，就是自己开始学习爱，学着放下一切痛苦、执着和所谓的“绝对合理理由”去宽容和原谅。", "evidence": ["E38"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你唯一可以做的恰好能解决问题——只给你留了一条路，而恰恰这条路就是出路；结尾再次恭喜：你终于不得不学习如何真正的获得幸福了。", "evidence": ["E39", "E40"]}
   ],
   "argument_steps": [
    "先反直觉定性：对人类失望是好事，因为补上了世界观的大洞（P001—P004）。",
    "给出前景判断：过了这个坎就海阔天空，而且非过不可（P005、P006）。",
    "理由1：可以停止“换个对象就会好”的想象，并举男友、老板、城市、国家为例（P008—P013）。",
    "提出核心比喻：必须学会与问题共同存在而不是逃走；换来的只是喘息之机，是学游泳的机会（P014—P016）。",
    "警告误把喘息当上岸会被反复呛水击垮，并称世上本无岸（P017、P018）。",
    "以痛苦比较推动选择：不放开完美梦想则痛苦无限持续（P019—P021）。",
    "指出学游泳的痛苦不可回避，无论有无准备、条件、信心都只能向前（P022、P023）。",
    "给出转机判断：不得不找方法时方法不难找（P024）。",
    "论证没有完美的他人与职业，也不该归罪于自己：认知必从简单而相对完美的认识开始，幻灭会反复发生（P025—P027）。",
    "把幻灭定性为逼人反思的绝境，并称不到此时不会承认原本自洽的一套不正确（P028、P029）。",
    "把绝望解释为世界给人的教育、成长的过程，以毛毛虫化蝶比喻并提醒别把茧结得太厚（P030—P034）。",
    "理由2：可以开始学习原谅整个人类，以“所有人都……并无例外”与“所有人都可怜、无知、想活着”作前提（P035—P040）。",
    "提出“因爱被算为做到”的美德观：宽容之心使不够诚实的人被算为诚实（P041—P043）。",
    "推出不爱的后果：世界终结于漆黑、活在地狱里（P044、P045）。",
    "重新定义爱：不是可选项或无私奉献，而是诫命，且根本上为了自己，是让价值被看见的光（P046—P050）。",
    "给出最低限度标准：只爱一个人、哪怕是自己，就算及格（P051）。",
    "收束：终局已可见，唯一可更改的变量是自己，唯一出路是学习爱与宽容；结尾再恭喜（P052—P059）。"
   ],
   "concept_usage": [
    {"term": "完美梦想/完美标准", "meaning": "作者指幻灭之前对朋友、情人、上司、职业等的完美期待；认为不放开它，虚无与绝望的痛苦就无限持续。", "evidence": "P021", "ambiguity": "未界定“完美标准”的具体内容"},
    {"term": "上岸/学游泳/喘息之机", "meaning": "作者的核心比喻：把换对象换环境当作摆脱问题（上岸），实际只能学会与问题共存（学游泳），所获只是喘息之机。", "evidence": "P016", "ambiguity": "比喻未给出可操作的判据"},
    {"term": "世界给人的教育", "meaning": "作者对绝望的定性：人必须领受、也是幸而必须领受的教育。", "evidence": "P030", "ambiguity": "“世界”作为施教与授权主体的说法未界定"},
    {"term": "诫命", "meaning": "作者对爱的定性：不是可选项或无私奉献，而是若不守不行、世界就会一天比一天黑暗的诫命。", "evidence": "P048", "ambiguity": "带宗教语汇色彩，正文未说明其来源"},
    {"term": "宽容", "meaning": "作者认为爱所产生的动力；没有它，世界必定终结于一片漆黑。", "evidence": "P044", "ambiguity": "未界定宽容的限度"},
    {"term": "完全自洽是可耻的", "meaning": "作者由“不到绝境不承认原本自洽的一套并不正确”推出的判断。", "evidence": "P029", "ambiguity": "仅在括号中给出，未展开论证"}
   ],
   "examples_and_targets": [
    "男朋友、老板、公司、城市、国家——作者列举的“再换一个就会好”的对象（P009—P012）",
    "喘息之机、学游泳、上岸、意外呛水——作者的核心比喻群（P016—P018）",
    "毛毛虫撕心裂肺变成蝴蝶、别把茧结得太厚——成长与自我封闭的比喻（P032、P034）",
    "所有的人都撒谎/偷窃/傲慢/虚伪/侵犯别人的自由；所有的人都可怜/无知/想活着——作者的普遍性断言（P037、P039）",
    "诚实、公平、正义等美德与爱本身——作者论证“因被爱才在实践上存在”的对象（P041—P043）",
    "骗子、叛徒、盗匪的地狱；伸手不见五指的漆黑——作者描述无爱状态的修辞（P045、P048）"
   ],
   "conditions": [
    "前提句：“当你到了这个点”“到了这个点”（P008、P013）",
    "澄清性让步：“注意，这不是说你不能重新选择……而是说即使你要换……”（P015）",
    "假设：“如果你误把每一次喘息都当作已经上岸了”（P017）",
    "条件：“只要你不放开‘完美梦想’”（P021）",
    "无条件列举：“有准备也好、没准备也好，有条件也好、没条件也好，有信心也好、没信心也好，都只有向前挺进”（P022）",
    "条件：“当你不得不寻找方法”“当你不得不解决”（P024）",
    "转折限定：“不是说你不能选择，不能通过选择有一定的改善，而是说你不可能通过选择真正达到……标准”（P025）",
    "条件：“你如果不爱”“没有足够的宽容”（P044）",
    "诫命条件：“是你若不守、不行，世界就会一天比一天黑暗”（P048）",
    "最低限度：“只要哪怕学会一点、学会哪怕跌跌撞撞的、略有姿势的只爱一个人，哪怕这个人就是你自己”（P051）",
    "唯一性：“你唯一真正可以更改的变量，只有你自己”（P055）"
   ],
   "rhetoric_and_tone": "第二人称劝慰兼训诫，祝贺语反复并首尾呼应（“恭喜你”）；比喻密集（补洞、尺阔之溪一跃可过、海阔天空、上岸/游泳/呛水、毛毛虫化蝶、茧、光与黑暗、地狱）；连续排比与条件堆叠（“有准备也好……都只有向前”）；箴言体断言（“所以说，完全自洽是可耻的”）；带宗教语汇的“诫命”“光”，语气由调侃渐转庄严。",
   "unresolved_questions": [
    "“对人类失望”的具体遭遇与提问者处境，正文未涉及，作者直接把它重新定性为好事。",
    "“世界给人的教育”“世界对人深爱得令人嫉妒”“世界手里”等表述中的“世界”是拟人主体，正文未界定其含义。",
    "“爱是一种诫命”的来源与依据（宗教或哲学）未说明，属作者断言。",
    "“完全自洽是可耻的”仅在括号中给出，未展开论证。",
    "“别把茧结得太厚，会死的”中的“死”是比喻还是实指，未说明。",
    "“所有的人都撒谎、偷窃、傲慢、虚伪、侵犯别人的自由……并无例外”是普遍断言，正文未给依据，需外部核查。",
    "文中“ta们/ta”按原文保留。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你终于可以正式的开始来点人生观、价值观了，因为你刚刚补上了最重要的世界观的大洞。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "对你做个稍微可以让人忍受的人（甚至是一个有较大可能成功的人）有重大的、决定性的意义。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这绝对不是一件坏事，而是一件好事。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "过了这个坎，前头就是海阔天空、自由自在、无忧无虑了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "而且你非过不可。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "而是这个人有问题，换一个人就会好了", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "没有人会真的让你满意的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "你必须要学会与这些问题共同存在，而不是只能转身逃走。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "一般只意味着同样的问题会以另一个剧情、另一种样式、另一种烈度重新浮现出来。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P016", "quote": "你所获得的，本质上只是一段宝贵的喘息之机，而并不是摆脱了问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "那么一次又一次的“意外呛水”最后会击垮你的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "没想到其实还是在水里。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "世上本无岸", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "只要你不放开“完美梦想”，后者的痛苦就是无限持续的。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P022", "quote": "都只有向前挺进、向前努力了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "当你不得不寻找方法，方法并不难找；当你不得不解决，解决未必有这么难。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "而是说你不可能通过选择真正达到你没有经过这次幻灭之前的标准。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P027", "quote": "幻灭之后再次建立起的完美想象仍将再次幻灭。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "你唯一的选择，就是重新反思之前有什么东西想错了、什么事情做错了。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "（所以说，完全自洽是可耻的。）", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P030", "quote": "这种绝望，实际上是世界给人的教育。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P031", "quote": "你现在所受的痛苦，只是这种成长的一个过程。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P032", "quote": "若不是戴着旧壳奇痒难当、生不如死，有哪只毛毛虫愿意撕心裂肺，变成蝴蝶？", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P034", "quote": "别把茧结得太厚，会死的。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P037", "quote": "所有的人都撒谎，所有的人都偷窃，所有的人都傲慢，所有的人都虚伪，所有的人都在侵犯别人的自由。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P039", "quote": "因为所有的人都可怜，所有的人都无知，所有的人都想活着。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P041", "quote": "而是宽容的心，使得不够诚实的人被算为诚实的人。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P042", "quote": "都是因为爱而被算为人做到了。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P043", "quote": "这些美德，都是因为被爱才在实践上存在。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P044", "quote": "没有足够的宽容，你的世界最后必定将终结于现在的一片伸手不见五指的漆黑。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P045", "quote": "不能爱，你就永远活在美德全部幻灭的地狱里。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P046", "quote": "爱其实不是一种选择", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P048", "quote": "爱是一种诫命。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P048", "quote": "世界就会一天比一天黑暗，直到在你眼里变成所有的人都是骗子、叛徒、盗匪的地狱的诫命。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P049", "quote": "而根本的其实是为了你自己。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P050", "quote": "爱就是让这个世界的一切价值得以让你看见的光。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P051", "quote": "哪怕这个人就是你自己，就算为你们及格", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P055", "quote": "你唯一能解脱绝望的方向，就是自己开始学习爱", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P056", "quote": "只给你留了一条路，而恰恰这条路就是出路", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P059", "quote": "你终于不得不学习如何真正的获得幸福了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生观", "价值观", "伦理学", "心理调适"],
   "issue_candidates": ["对人类失望怎么办", "期待与幻灭", "爱与宽容", "成长的痛苦"],
   "text_function_candidates": ["答疑", "劝慰", "训诫", "箴言式论述"],
   "object_candidates": ["提问者", "人类", "世界"],
   "working_keywords": ["对人类失望", "完美梦想", "上岸", "学游泳", "幻灭", "宽容", "诫命", "光"]
  },
  "notes": "无图片。作者把“对人类失望”重新定性为好事，给出两个理由与一套“爱是诫命”的论述；普遍性断言（所有人……并无例外）、“世界”的拟人用法与“完全自洽是可耻的”均按原文保留并登记于未决问题。"
 },
 "4d34493f": {
  "analysis": {
   "question_context": "提问者问“人类会不会是高等生命的食粮”。作者没有回答是或否，也没有讨论高等生命是否存在，而是反驳以“谁以谁为食”判断高低的框架：把结局搞成“只有智慧生物可吃”的存在从任何意义上说都是低等生命，用“谁以谁为食”决定谁更高级的人还不如细菌高级。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "给“食谱收缩到只有智慧生物可吃”的存在定性：这是总失败结局，因而从任何意义上说都是低等生命。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "反驳以食物链位置论高低的尺度：持这种尺度的人还不如细菌高级，因为ta整天被细菌吃。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "会搞到“只有智慧生物可吃”这种总失败结局的，从任何意义上说都是低等生命。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "会用“谁以谁为食”来决定谁比较高级的，还不如细菌高级——ta整天被细菌吃。", "evidence": ["E2"]}
   ],
   "argument_steps": [
    "先给“把食谱收缩到只有智慧生物可吃”的存在定性为低等生命（P001）。",
    "再反驳以食物链位置论高低的尺度：持此尺度者还不如整天被细菌吃的细菌高级（P002）。"
   ],
   "concept_usage": [
    {"term": "高等生命", "meaning": "提问中的用语；作者未把它当作正面概念使用，而是以“总失败结局”和“以谁为食论高低”反推该尺度不成立。", "evidence": "P001", "ambiguity": "正文未定义“高等生命”，也未回答其是否存在"},
    {"term": "总失败结局", "meaning": "作者对“只有智慧生物可吃”这一状态的性质判定：整体上的失败结局。", "evidence": "P001", "ambiguity": "未说明“失败”的判定标准"},
    {"term": "食粮", "meaning": "提问中的说法；作者未直接回应人类是否为食粮，只反驳“以谁吃谁定高低”的标准。", "evidence": "P002", "ambiguity": "正文未定义“食粮”"}
   ],
   "examples_and_targets": [
    "“只有智慧生物可吃”——作者设定的反例情形（P001）",
    "细菌、ta整天被细菌吃——作者的反例与嘲讽性比较（P002）",
    "提问者“人类会不会是高等生命的食粮”——被作者搁置并转换的提问框架（Q001）"
   ],
   "conditions": [
    "以条件式表述给出判定：“会搞到……这种总失败结局的”（P001）",
    "以“会用……来决定……”界定被反驳的尺度（P002）"
   ],
   "rhetoric_and_tone": "极简短的反驳体，两句即止；以“还不如细菌高级——ta整天被细菌吃”作嘲讽性比较，语气冷峻；不直接回答提问，也不展开论证。",
   "unresolved_questions": [
    "作者未直接回答人类是否为高等生命的食粮，也未说明高等生命是否存在。",
    "“高等生命”“食粮”均未定义，“总失败结局”的判定标准未说明。",
    "以细菌为反例的推理未展开：被细菌吃与“高级”之间的关系未论证。",
    "正文仅两句，提问涉及的宇宙论/科幻设定未获回应。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "从任何意义上说都是低等生命。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "还不如细菌高级——ta整天被细菌吃。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宇宙论想象", "价值判断", "思辨"],
   "issue_candidates": ["人类是否是高等生命的食粮", "以食物链论高低的尺度"],
   "text_function_candidates": ["答疑", "反驳", "嘲讽式短评"],
   "object_candidates": ["人类", "高等生命", "细菌"],
   "working_keywords": ["高等生命", "食粮", "低等生命", "细菌", "总失败结局"]
  },
  "notes": "无图片。正文仅两段，未直接回答提问，而是反驳“以谁以谁为食判断高低”的框架；brief 与正文一致。“ta”按原文保留。"
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
