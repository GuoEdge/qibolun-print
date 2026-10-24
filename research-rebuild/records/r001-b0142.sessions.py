# -*- coding: utf-8 -*-
"""批次 r001-b0142 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0142.sessions.py            # 写 out/r001-b0142.out.jsonl
  python3 records/r001-b0142.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0142"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0142.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "9dc3b9d2": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何坦然地面对人生中的离别？”，是求安慰或方法的求助立场。作者不直接给情绪安抚，而是先把“生离”重新定义为“死别的预演”，再按两种信念（人死即终结／灵魂不灭）分别推演分离是否等于失去，最后把坦然归结为“记住”与“愿意再相聚”两个决定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出生离是死别的预演，故生离意义很大。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "以两个反问设定议题：难再见是否等于失去；只知道对方仍存在是否足够安慰。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006"], "summary": "条件推演：若相信人死即终结，分离且无法期待重逢则对方等于实际死亡，是死别而非生离。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "以毕业、离乡、同事离职、恋人分手为例，说明生离同时是死别。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "反驳“保持联系”方案：终究失去大部分人，且可能被视为纠缠和打扰。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011"], "summary": "反驳“高度珍惜当下、分开就不想”方案：只有一种珍惜档位，无从上调，属自欺。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013"], "summary": "论证“绝对不能接受分离”扭曲关系人格与地位，实为捕获与戴手铐。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015"], "summary": "提出悖论：正是“不要分离”导致别人要分离。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P016"], "summary": "断定无法用有效手段“解决”该问题。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022"], "summary": "条件反转：若信灵魂不灭，时空不构成障碍，记得并愿相认即从未分离。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P023", "P024", "P025"], "summary": "把问题收敛为两问：你决定记住吗、你愿意再相聚吗。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "结语：记住且愿意则生离死别都化为乌有，可放心毕业、留学、分手、离开医院。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生离的意义很大，因为它是死别的预演。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若相信人的存在以死亡为终结，且分离后不能乐观期待再遇、终将渐停联系，则此人在本质上等于实际死亡，属死别而非生离。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "毕业、离乡打拼、同事离职、恋人分手都不只是生离，也同时是死别。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "再怎么加强联系终究会失去一大部分人，且其中许多你不想失去的人会把你的联系视为纠缠和打扰。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人只有一种珍惜档位，之前珍惜的程度就是做得到的最大的程度，没有“更珍惜”可上调，所谓决定是自欺欺人。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“绝对不能接受分离”的态度扭曲了关系中的人格和地位。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恰恰是“不要分离”导致别人要和你分离。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论怎么看待，都无法用什么有效手段“解决”分离问题。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若相信灵魂不灭，则公式反转：对方无论如何都存在、总有再见机会，只要记得、认得出且愿意相认，在严格意义上就从未与你分离。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在无限的时间中一切可能的都终会发生。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "分离与否取决于是否记住、是否愿意再相聚；记住且愿意，则生离死别都化为乌有。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "定义/命题：生离是死别的预演，故生离有意义（P001）。",
    "以反问设定两难：难再见是否等于“失去”；知道对方仍存在、总有再见之日是否足够安慰（P002-P003）。",
    "分支一（条件推演）：相信死亡是终结 → 分离且无法期待重逢、终将停止联系 → 对方等于实际死亡（P004-P006）。",
    "举例：毕业是至少一半同学的最终告别礼；离乡、离职、分手同属死别（P007）。",
    "反驳备选方案一“保持联系”：终究失去大部分人，联系可能被视为纠缠打扰（P008-P009）。",
    "反驳备选方案二“更珍惜当下”：只有一种珍惜档位，无上调余地，是自欺（P010-P011）。",
    "让步/深入：指出“绝对不能接受分离”的态度扭曲人格与地位，本质是消灭分离的可能即捕获与戴手铐（P012-P013）。",
    "反讽式结论：正是“不要分离”导致别人要分离（P014-P015）。",
    "判定：无法用有效手段解决该问题（P016）。",
    "分支二（条件推演）：相信灵魂不灭 → 公式反转，时空对永生灵魂是虚无概念，同一世界即永恒相聚（P017-P022）。",
    "结论：分离与否只看是否记住、是否愿意再相聚（P023-P026）。",
    "行动收束：可放心毕业、留学、分手、离开医院；再以两问催决（P027-P029）。"
   ],
   "concept_usage": [
    {"term": "生离／死别", "meaning": "生离指分离后仍有再见可能的别离；死别指本质上的永别。作者主张在“人死即终结”信念下，停止联系的生离等于实际死亡。", "evidence": "P004", "ambiguity": "“本质上的死亡”是作者的判定标准，非通常语义；判定取决于是否“能乐观期待再相遇”。"},
    {"term": "预演", "meaning": "生离作为死别的提前演练，故有意义。", "evidence": "P001", "ambiguity": "“预演”的具体作用机制未展开。"},
    {"term": "珍惜的档位", "meaning": "作者设定人只有单一珍惜程度，不存在可上调的更高档位。", "evidence": "P011", "ambiguity": "该设定为作者断言，未给论证。"},
    {"term": "消灭分离的可能", "meaning": "作者将其解为“捕获并戴上手铐”的文言说法，即对关系的强制占有。", "evidence": "P013", "ambiguity": "无。"},
    {"term": "灵魂不灭／同一世界", "meaning": "若灵魂不灭，同在一个世界即终极而永恒的相聚，时空距离对永生灵魂是虚无概念。", "evidence": "P021", "ambiguity": "属信念条件，作者未论证其为真。"},
    {"term": "ta", "meaning": "作者用无性别第三人称指关系对象。", "evidence": "P009", "ambiguity": "P009“尤其是ta”具体所指未明。"}
   ],
   "examples_and_targets": [
    "毕业——“至少一半同学的最终告别礼”，作者例证（P007）。",
    "离乡打拼、同事离职、恋人分手——作者例证，其中尤重恋人分手（P007）。",
    "“保持联系”——被作者反驳的应对方案（P008）。",
    "“我高度珍惜在一起的时间，分开了我就不想了”——被作者设为假想读者方案并反驳（P010-P011）。",
    "“别人明明不如我珍惜，奈何ta不识货”——作者引述并质疑的感叹，属反讽材料（P015）。",
    "放心毕业、放心留学、放心分手、放心离开医院——结语列举的应用场景（P027）。"
   ],
   "conditions": [
    "“如果你相信人的存在以死亡为终结”（P004）。",
    "分离且“不能乐观的期待会再相遇”，并且“知道彼此终究会渐渐停止联系”（P004）。",
    "“反过来，如果你相信人的灵魂是不灭的”（P017）。",
    "“只要你记得，再相会时认得出而且愿意相认”（P020）。",
    "“因为在无限的时间中一切可能的都终会发生”（P022）——作为无分离结论的前提。",
    "“你记住、你愿意”（P026）——结论成立的条件。"
   ],
   "rhetoric_and_tone": "第二人称“你”全程直接对话；密集反问（P002、P003、P015、P024、P025、P029）；两条信念分支的对照推演使“公式反转”；短句排比与断言（P012“你要绝对保险，你要忠诚证明……”）；反讽与直言（“只是‘捕获并戴上手铐’的文言说法而已”）；结尾以两问反复追问形成决断式劝服，兼具心理劝导与训诫语气。",
   "unresolved_questions": [
    "两种信念（死亡即终结／灵魂不灭）何者为真，作者未裁决，只作条件推演，读者无法据本文确定应采哪支。",
    "P009“尤其是ta”所指对象不明。",
    "“分离与否的唯二问题”为何恰为两个、是否充分条件，“记住”与“愿意”的具体含义未界定。",
    "“在无限的时间中一切可能的都终会发生”未给论证或出处。",
    "本篇正文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "生离的意义很大，因为它是死别的预演。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "那么这个人在本质上对你来说等于实际死亡了", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "在将来离乡打拼、同事离职、恋人分手——尤其是恋人分手，全都不只是生离，也同时是死别。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "你再怎么加强联系，终究也会失去一大部分人", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "恐怕会把你的联系视为纠缠和打扰", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "你只有一种珍惜的档位，你之前珍惜的程度，就是你做得到的最大的珍惜的程度", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "扭曲了关系中的人格和地位", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "恰恰正是这个“不要分离”，导致别人要和你分离。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "无论你怎么看待，你是无法用什么有效的手段“解决”这个问题的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "如果你相信人的灵魂是不灭的", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P019", "quote": "对方无论如何都存在，彼此也无论如何都有机会再见。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "在严格的意义上就从未与你分离。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "因为在无限的时间中一切可能的都终会发生", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "你记住、你愿意，那就没有分离可言。无论生离，还是死别，都化为乌有。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生死观", "人际关系", "心理劝导", "离别与丧失"],
   "issue_candidates": ["如何面对离别", "生离是否等于死别", "灵魂不灭与永恒相聚", "占有与分离的关系"],
   "text_function_candidates": ["问答回应", "条件推演", "劝导", "概念重定义"],
   "object_candidates": ["生离", "死别", "灵魂不灭", "保持联系", "珍惜档位"],
   "working_keywords": ["生离", "死别", "预演", "灵魂不灭", "记住", "再相聚", "珍惜的档位"]
  },
  "notes": "正文与结构一致，无图片节点。作者对提问未直接给情绪安抚，而以两种信念分支作条件推演；“哪一支为真”留待后续研究，不在本篇裁决。"
 },
 "8f6c9025": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待大批曾为北约部队工作的阿富汗翻译申请避难被拒？”，是就一则时事的求评立场。作者不评论避难个案本身，而把它当作“无并吞意图却打成占领状态”这一战略失当的最直接表现之一，由此展开对外战争目的、边界与止点的讨论，并延伸到对越／对印战争、美国扩张能力与台湾问题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "由阿富汗翻译被抛弃引出对印、对越边境战争的决策合理性。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "提出对外战争须先掂量目的、边界与止点，切忌无并吞意图却打成占领。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "若有并吞计划须先有文化、舆论、思想、组织、人事准备，基本准备期以十年百年计，军事只是工具。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "无民意根基的占领终将结束且是大失败，会留下更敌对的敌国；阿富汗结局一开始就已注定。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "无并吞打算时只能是快速打击、快速脱离的惩戒战；对越对印为范例，须留下压倒性敬畏。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011"], "summary": "敬畏使对方残存敌对派难以主张报复，政商精英会在务实层面起刹车作用。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013"], "summary": "击溃后毫不留恋撤退、寻求邦交正常化并扶持友好合作派，才能长期有利。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "对普通人：要分辨两种情况，对方缺乏经济文化组织准备时不宜轻易合作，误判可能致命，这是自然法。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "把同一法则移用到个人与邻人：人是互相矛盾念头的竞争结果，不可因力量强就越界。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026"], "summary": "推论美国无力再扩张：军事条件仍足，但支撑兼并的组织条件已不存在。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P027"], "summary": "由此推断台湾命运注定，因大陆在做军事行动前的充分准备与实际动作。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "阿富汗翻译被抛弃一事显示出对印、对越边境战争决策的合理性。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强国发动对外战争必须掂量清楚战争为了什么、以什么为边界、以什么为止点，切忌在没有永久并吞意图的前提下打成占领状态。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若确有永久并吞计划，须在军事行动前完成文化、舆论、思想、组织、人事准备，在对方内部培育呼唤合并的社会力量，基本准备期以十年甚至百年计；军事只是摘果子的剪刀和除虫的镊子，不是行动的主要部分。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "除非有并吞的战略决心，否则不可仅因军事压倒优势就寻求占领；无民意根基的占领终会结束，且结束时必是大失败，还会留下更激进、更敌对、更有信心的敌国。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“辅助人员被抛弃”只是这种战略失当最直接的表现之一；美国决定占领阿富汗时这一点就已注定。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有并吞打算时，对外军事行动只能是快速打击、快速脱离的惩戒战，对越、对印战争是教科书式范例；一旦决定就要雷霆一击，在敌人社会意识中留下无法绕过的敬畏，使其评估报复成本时绝望。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这种敬畏会成为对方残存敌对派的一大阻力：报复主张在务实层面因付不起代价而被抛弃，政商精英会起刹车和抑制作用。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "干脆利落的击溃、毫不留恋的撤退，再寻求邦交正常化并给予对方内部友好合作派外部有利条件，足以长期稳定有利关系，这样才是赚的。", "evidence": ["E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "普通人要分辨占领与惩戒两种情况；对方若没有足够的经济、文化、组织准备，就不要在民族情绪仍敌对时轻易考虑合作，做错判断可能致命。", "evidence": ["E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这其实是一种自然法，没有什么冤枉和可怜可言。", "evidence": ["E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个人也由大量互相矛盾的念头在意志内部竞争而成，故对个人采取干预同样不可因力量强就越界，否则也有仓皇大撤退的一天。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "美国没有能力再进一步扩张：军事条件仍充足，但支撑“兼并”规模野心的组织条件已不存在——体制无法构思八年以上战略规划，也无充分人力资源重组各地人事管理架构。", "evidence": ["E23", "E24", "E25", "E26"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "台湾的命运是注定的，因为大陆在锲而不舍地做军事行动前的充分准备和大量实际动作。", "evidence": ["E27"]}
   ],
   "argument_steps": [
    "由时事切入：阿富汗翻译被抛弃显示对印、对越边境战争决策的合理性（P001）。",
    "提出一般原则：对外战争先定目的、边界、止点；切忌无并吞意图而打成占领（P002-P003）。",
    "分支一：若确有并吞计划，须先做文化、舆论、思想、组织、人事等非军事准备，培育内部呼唤合并的力量，准备期以十年百年计；军事只是剪刀与镊子（P004-P005）。",
    "反面论证：无民意根基的占领必以失败告终，并留下更激进、更敌对、更有信心的敌国（P006）。",
    "回到时事：阿富汗结局从一开始就已注定（P007）。",
    "分支二：无并吞打算时只能做快速打击、快速脱离的惩戒战；对越对印为例，需以压倒性胜利留下敬畏（P008-P009）。",
    "机制说明：敬畏压制对方主战派，务实成本考量使其报复主张被抛弃（P010-P011）。",
    "结论：击溃—撤退—邦交正常化—扶持合作派，方能长期有利（P012-P013）。",
    "转向个人层面：普通人要分辨两种情况，判断错可能致命；称为自然法（P014-P017）。",
    "类比延伸：对邻人采取干预也要考虑同样问题，不可恃强越界（P018-P021）。",
    "推论：美国无力再扩张，因组织条件不足以支撑兼并（P022-P026）。",
    "结论延伸：台湾命运注定（P027）。"
   ],
   "concept_usage": [
    {"term": "占领状态", "meaning": "在没有永久并吞意图的情况下长期以军事控制对方领土的状态，作者视其为战略失当。", "evidence": "P003", "ambiguity": "未给出占领与惩戒战的判定标准。"},
    {"term": "惩戒战", "meaning": "快速打击、快速脱离、以留下敬畏为目的的对外军事行动类型，对越、对印战争被举为范例。", "evidence": "P008", "ambiguity": "作者未展开其国际法或政治代价。"},
    {"term": "兼并", "meaning": "永久并吞他国／他地的野心规模，需组织条件支撑。", "evidence": "P023", "ambiguity": "引号标示为作者的用语。"},
    {"term": "自然法", "meaning": "作者用来指称上述战略法则的客观必然性，不含道德褒贬。", "evidence": "P017", "ambiguity": "作者未说明其来源或依据。"},
    {"term": "民意根基／社会力量", "meaning": "占领或合并须在对方内部培育的、呼唤合并的社会支持。", "evidence": "P004", "ambiguity": "培育方式与成败判据未说明。"},
    {"term": "辅助人员被抛弃", "meaning": "指为占领方工作的本地辅助人员（如阿富汗翻译）在撤离后被舍弃。", "evidence": "P007", "ambiguity": "作者只举为表现之一，未展开个案。"}
   ],
   "examples_and_targets": [
    "大批曾为北约部队工作的阿富汗翻译申请避难被拒——提问者话题，作者用为战略失当的最直接表现之一（P007）。",
    "对越、对印边境战争——作者正面范例／“教科书式的范例”（P001、P008）。",
    "美国决定占领阿富汗——作者判断其结局一开始已注定（P007）。",
    "大英帝国派遣本国人担任各殖民地民政民生部门长官——作者类比与对照例证（P015）。",
    "美国“培训本土力量”——被作者讽刺为幻想、必然一场空（P025-P026）。",
    "台湾——作者预测对象（P027）。"
   ],
   "conditions": [
    "“在没有永久并吞意图的前提下”（P003）。",
    "“如果确有永久并吞的计划”（P004）。",
    "“除非有这样的战略决心”（P006）。",
    "“只要没有这种打算”（P008）。",
    "“一旦决定”（P009）。",
    "“在迅雷不及掩耳之间”（P009）。",
    "“在没有政治正确绑架的决策场合”（P011）。",
    "“对方如果没有足够的经济的，文化的、组织的准备”（P015）。",
    "“在民族情绪仍然保持着反抗精神和敌视情绪的前提下”（P015）。"
   ],
   "rhetoric_and_tone": "军事格言式断言与比喻密集（撒种、育苗、种树；摘果子用的剪刀和除虫的镊子；雄狮搏兔；迅雷不及掩耳；雷霆一击），规范句式“一定要／要切忌／除非／只要／一旦”；对美国的讥讽（“只能一天到晚幻想”“这只不过是自己想得美，最终必然一场空”）；结构由国际战略推及个人处世（“从另一方面，你作为一个人”），以“这样才会是赚的”“这其实是一种自然法”等短句作结，语气冷静、训导而带战略训诫色彩。",
   "unresolved_questions": [
    "提问涉及的阿富汗翻译避难被拒的具体事实、数量与政策过程，正文未给，也未直接评论。",
    "“八年以上的战略规划甚至都无法构思”未给出处或依据（P024）。",
    "台湾“命运注定”未给时间表、判据或可能变量（P027）。",
    "“辅助人员被抛弃”的具体所指与责任主体未详（P007）。",
    "对越、对印战争被称为“教科书式范例”的史实细节与争议未展开。",
    "本篇正文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这就显示出对印、对越边境战争的决策合理性来了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "强国发动对外战争这种事，一定要掂量清楚这场战争是为了什么，以什么为边界，以什么为止点。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "要切忌在没有永久并吞意图的前提下打成占领状态。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "那么在军事行动之前就要有文化准备、舆论准备、思想准备和相应的组织准备、人事准备。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "其基本准备期都要以十年甚至百年计。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "军事，只是摘果子用的剪刀和除虫的镊子。根本不是整个行动的主要部分。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "否则根本不可以仅仅因为军事上有压倒优势就轻易的寻求占领。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P006", "quote": "更意味着你会反过来因为自己的占领留下一个比之前更激进、更敌对，尤其是更有信心的敌国。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "只是这种战略失当最直接的表现之一。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "这一点其实在最开始美国决定占领阿富汗的时候就已经注定了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "对外军事行动就只能是快速打击、快速脱离的惩戒战。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "我们的对越、对印战争就是教科书式的范例。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P009", "quote": "以压倒性的摧枯拉朽般的胜利在敌人的社会意识中留下不可否认、无法绕过的敬畏。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P010", "quote": "这种敬畏，会是对方的残存敌对派的一大阻力。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P011", "quote": "就会发现自己不可能支付得起代价。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P012", "quote": "干脆利落的击溃，毫不留恋的撤退，在这个基础之上，寻求邦交正常化", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P015", "quote": "就不要在民族情绪仍然保持着反抗精神和敌视情绪的前提下轻易考虑和对方合作。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "做错判断的结果很可能是致命的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P017", "quote": "这其实是一种自然法，没有什么冤枉和可怜可言。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P019", "quote": "事实上一个人自己也可以说是由大量互相矛盾的念头在意志内部竞争的结果。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P020", "quote": "不要因为你胳膊比较粗就轻易的做出越界举动", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P021", "quote": "否则你也有无法维持而仓皇大撤退的一天。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P022", "quote": "实际上美国没有什么能力再进一步的扩张自己的存在了。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "但是想要支撑“兼并”这种规模的野心的组织上的条件已经不存在了。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P024", "quote": "ta们的体制已经决定了超过八年以上的战略规划甚至都无法构思，更不必谈执行了。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "美国没得派，只能一天到晚幻想“培训本土力量”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P027", "quote": "这也从另一个角度可以看到台湾的命运是注定的", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际政治", "军事战略", "大国兴衰", "两岸关系"],
   "issue_candidates": ["对外战争的边界与止点", "占领与并吞的条件", "辅助人员被抛弃", "美国扩张能力的限度", "台湾问题"],
   "text_function_candidates": ["时事评论", "战略论断", "类比推演", "行动建议"],
   "object_candidates": ["占领", "惩戒战", "并吞", "阿富汗翻译", "对越对印战争", "美国", "台湾"],
   "working_keywords": ["占领状态", "永久并吞", "惩戒战", "敬畏", "自然法", "组织条件", "台湾"]
  },
  "notes": "正文与结构一致，无图片节点。作者未直接评论阿富汗翻译避难个案，而是把它作为战略失当的表现之一；本篇多处涉及现实政治判断与预测（美国扩张、台湾），属作者论断，需外部核查，初读不予裁决。"
 },
 "8bb20447": {
  "analysis": {
   "question_context": "提问者问如何与持续否定、打击自己的人共同生活并保持自信。作者把问题转为能力与再选择权问题：先获得离开的能力，再谈不受对方轻易触犯；没有选择余地时，话术和翻脸都不能根治处境。",
   "content_units": [{"unit_id":"U001","paragraph_refs":["P001","P002","P003"],"summary":"把共同生活困境归因于缺少能力和选择余地，主张先增强能力以获得再选择权。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P004","P005","P006","P007"],"summary":"说明明显的离开或更换选项本身会形成威慑，不需斗争话术即可改变对待。","role":"reason"},{"unit_id":"U003","paragraph_refs":["P008","P009","P010","P011","P012","P013"],"summary":"否定巧妙话术、委曲求全和翻脸的根治作用，并把不努力与自我侮辱联系起来。","role":"rebuttal"},{"unit_id":"U004","paragraph_refs":["P014","P015","P016"],"summary":"将持续折磨解释为阻止放弃努力的机制，委曲求全只能争取时间，最终仍靠再选择权。","role":"reason"},{"unit_id":"U005","paragraph_refs":["P017","P018","P019"],"summary":"把努力说成客观义务，并把常见自信解释为由安全感造成的错觉。","role":"conclusion"}],
   "main_claims": [{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"解决与否定者共同生活的根本条件是增强能力并获得明显的再选择权。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"有明显的离开、跳槽或更换选项时，对方会因知道你可离开而收敛，不必依靠斗争妙招。","evidence":["E3"]},{"claim_id":"C003","claim_type":"author_qualified","attribution":"author","modality":"qualified","statement":"没有选择余地时，不存在能根治问题的巧妙话术、委曲求全或翻脸；委曲求全最多只能争取时间和机会。","evidence":["E4","E5"]},{"claim_id":"C004","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者把不学习、不劳动和好逸恶劳等归为对自身无能的默许，并称为自我侮辱。","evidence":["E6","E7"]},{"claim_id":"C005","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者将努力称为客观世界中的天定义务，并把没有再选择权时的自信解释为安全感错觉。","evidence":["E8","E9"]}],
   "argument_steps":["追问为何必须共同生活（P001）。","缺少能力导致缺少选择余地，先提升能力（P002-P003）。","以可离家、跳槽、更换关系为例说明选择权形成威慑（P004-P007）。","否定话术、翻脸和委曲求全的根治作用（P008-P016）。","把努力和再选择权提升为客观条件，并重新定义自信（P017-P019）。"],
   "concept_usage":[{"term":"选择余地/再选择权","meaning":"能离开当前关系、工作或居所并选择替代方案的现实能力。","evidence":"P002","ambiguity":"作者未说明能力门槛及现实资源差异。"},{"term":"自信","meaning":"作者重释为由成功构建的安全感产生的错觉。","evidence":"P018","ambiguity":"这是作者定义，非心理学共识。"}],
   "examples_and_targets":["父母与子女独立居住、老板与可跳槽员工、关系中的可更换对象（P005）。","目标对象是打击、否定他人的共同生活者，以及作者认为缺乏努力的当事人（P008-P013）。"],
   "conditions":["有明显的离开或更换选项（P003-P005）。","没有选择余地时（P008）。","委曲求全只能作为争取时间和机会的权宜之策（P016）。"],
   "rhetoric_and_tone":"连续反问、命令式劝诫和贬抑性标签密集；以不怒而自威作警句，用“自取其辱”“躺赢”等强烈措辞把结构性困境个人化。",
   "unresolved_questions":["能力不足是否可能由照护、疾病、经济或暴力控制造成，正文未区分。","作者关于努力义务和自信的普遍化断言未提供外部依据。","无图片节点。"],
   "evidence":[{"key":"E1","paragraph_id":"P002","quote":"首先增强你的能力，以便获得不必忍受这些的选择余地。","relation":"supports"},{"key":"E2","paragraph_id":"P016","quote":"最终靠的还是“明显的再选择权”。","relation":"supports"},{"key":"E3","paragraph_id":"P005","quote":"你可以随便跳槽，老板自然客气三分；你可以轻松的换一个，这一个自然不敢放肆。","relation":"supports"},{"key":"E4","paragraph_id":"P008","quote":"没有什么所谓“巧妙”的办法来解决这个问题","relation":"supports"},{"key":"E5","paragraph_id":"P016","quote":"委曲求全只能是争取时间和机会的权宜之策","relation":"supports"},{"key":"E6","paragraph_id":"P010","quote":"你已经通过默许和接受自己的无能侮辱了你自己。","relation":"supports"},{"key":"E7","paragraph_id":"P011","quote":"谁叫你不学习？谁叫你不劳动？","relation":"supports"},{"key":"E8","paragraph_id":"P017","quote":"努力是一种天定的义务","relation":"supports"},{"key":"E9","paragraph_id":"P018","quote":"“自信”本质上不过是成功构建的安全感错觉。","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": "正文与结构一致，无图片节点。作者把提问改写为能力、努力和选择权问题；其中“努力是天定义务”“自信是安全感错觉”等为作者断言，未在本篇外部核验。"
 },
 "74ec1c2d": {
  "analysis": {
   "question_context":"提问者问是否应举全家之力支持男友读博。作者将其处理为风险分配和识人方法，建议把无条件资助改成有抵押、责任边界清晰的私人助学贷款，并用对方反应判断关系。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"允许支持，但以叔叔名义设计低息私人助学贷款并以男方房产抵押。","role":"action_advice"},{"unit_id":"U002","paragraph_refs":["P005","P006","P007","P008","P009"],"summary":"婚姻存续期可分担部分利息，婚姻结束后未还款由男方承担，明确帮助范围。","role":"condition"},{"unit_id":"U003","paragraph_refs":["P010","P011","P012"],"summary":"以男方是否感恩、是否接受清晰责任边界来判断其品性，并将拒绝视为离婚信号。","role":"evaluation"},{"unit_id":"U004","paragraph_refs":["P013","P014","P015","P016"],"summary":"强调抵押降低家庭财务风险，具名帮助限于公平交易，直接给钱则不具名。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"支持男友读博可以做，但应设计成有私人房产抵押的优惠利率助学贷款，而非无条件给付。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"婚姻结束后未清偿部分应由男方个人承担，因为学位不能在离婚后分割。","evidence":["E3","E4"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"男方对公平条件的感谢或拒绝可被用来判断其是否懂得感恩、是否值得继续共同生活。","evidence":["E5","E6"]},{"claim_id":"C004","claim_type":"author_qualified","attribution":"author","modality":"qualified","statement":"具名帮助应严格限于公平交易；直接给钱则不具名。","evidence":["E7"]}],
   "argument_steps":["把问题定性为做事方法问题（P001）。","提出低息、抵押、私人贷款方案（P002-P004）。","按婚姻存续与结束分担利息和本金责任（P005-P009）。","把感谢或反对条件作为识人测试（P010-P012）。","以抵押说明风险可控，并总结具名交易与匿名给钱的界线（P013-P016）。"],
   "concept_usage":[{"term":"公平条件/公平交易","meaning":"有抵押、利率和责任边界的可执行资助安排。","evidence":"P004","ambiguity":"公平标准及法律可行性未展开。"},{"term":"帮助","meaning":"作者区分具名的交易性帮助与不具名的直接赠与。","evidence":"P014-P015","ambiguity":"不具名赠与的追责与伦理边界未说明。"}],
   "examples_and_targets":["叔叔作为贷款安排的名义主体、男方私人房产作为抵押（P003-P004）。","目标对象是准备读博的男友及其对资助条件的反应（P010-P012）。"],
   "conditions":["婚姻关系存续时可分担部分利息（P005）。","婚姻结束后未还清部分由男方承担（P005-P006）。","具名帮助限于公平交易，直接给钱不具名（P014-P015）。"],
   "rhetoric_and_tone":"方案式、交易式和测试式表达，使用“赌对了”“看错了人”“准备离婚”等强判断和戏剧化后果。",
   "unresolved_questions":["私人贷款、房产抵押和婚姻财产安排的法律有效性未核验。","作者将感恩反应直接推及未来前途，推理依据不足。","无图片节点。"],
   "evidence":[{"key":"E1","paragraph_id":"P003","quote":"有个叔叔可以商量，先把关系拉开。","relation":"supports"},{"key":"E2","paragraph_id":"P004","quote":"发放优惠利率的私人助学贷款，用ta的私人房产作抵押","relation":"supports"},{"key":"E3","paragraph_id":"P005","quote":"如果婚姻关系结束，则未还清部分要完全由他自己承担。","relation":"supports"},{"key":"E4","paragraph_id":"P006","quote":"要视为他的个人贷款。","relation":"supports"},{"key":"E5","paragraph_id":"P010","quote":"如果他对你的这个提案表示感谢，对你心怀感激，那么恭喜你，你赌对了","relation":"supports"},{"key":"E6","paragraph_id":"P011","quote":"他如果摆出“夫妻还算这么清楚”的套路来，那么你就准备离婚","relation":"supports"},{"key":"E7","paragraph_id":"P014","quote":"帮，如果是具名的，就只能严格限于给予好的公平交易。","relation":"supports"}] 
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文与结构一致，无图片节点。本文是作者的风险控制与识人建议；贷款、抵押和婚姻债务的法律效果未核验，不应当作法律意见。"
 },
 "11f2ffba": {
  "analysis": {
   "question_context":"提问者比较国内 IT 公司高层少写代码与 Jeff Dean 仍写代码的做法。作者明确偏向先写核心代码和原型、再开会，反对没有原型支撑的 PPT、文档和讨论。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"主张直接写代码、先跑通原型再开会，认为原型未通前连业务模型和 vision 都未想清。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P005","P006"],"summary":"把高成本会议描述为闲扯皮，否定抽象商量。","role":"rebuttal"},{"unit_id":"U003","paragraph_refs":["P007","P008","P009"],"summary":"要求下属用原型证明点子，拒绝 PPT，并区分做不到与做得到却不做。","role":"action_advice"},{"unit_id":"U004","paragraph_refs":["P010","P011"],"summary":"断言伟大开发项目应由核心代码作者主导，其他高职级领导者只是高级服务员。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"直接写核心代码、先跑通原型再开会，是最快最简单的推进方式。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"原型未跑通前，业务模型和 vision 尚未想明白，开会通常只是高成本闲扯。","evidence":["E3","E4"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"真正伟大的开发项目实质上只能由写核心代码的人主导，高职级领导者只是高级服务员。","evidence":["E5"]}],
   "argument_steps":["拒绝图表和文档优先（P001）。","提出代码和原型优先（P002-P004）。","以会议成本否定原型前的讨论（P005-P006）。","要求所有点子拿原型证明并拒绝 PPT（P007-P009）。","以核心代码作者主导项目作总括（P010）。"],
   "concept_usage":[{"term":"原型","meaning":"可运行的初步实现，用于验证点子和业务模型。","evidence":"P003","ambiguity":"未说明何种项目适合原型优先。"},{"term":"高级服务员","meaning":"作者对高职级、非核心代码领导者的贬称，强调服务而非技术主导。","evidence":"P010","ambiguity":"属于修辞性角色判断，非组织管理通则。"}],
   "examples_and_targets":["国内 IT 公司 leader 以上与 Jeff Dean 的比较由提问者提出；正文未提供 Jeff Dean 的事实材料。","目标是管理者的会议、PPT 和技术决策方式（P005-P010）。"],
   "conditions":["原型尚未跑通时不宜开会（P004）。","点子应以可运行原型证明（P007）。","做得到却不做被视为自误（P009）。"],
   "rhetoric_and_tone":"极端的技术实践主义和强烈口语攻击，反复使用“老子”“开什么鸟会”“商量个球”等粗俗表达，以绝对化断言收束。",
   "unresolved_questions":["未讨论安全、合规、架构、协作和探索型项目中原型与文档的必要性。","未核验 Jeff Dean 或国内公司事实。","无图片节点。"],
   "evidence":[{"key":"E1","paragraph_id":"P002","quote":"直接写代码最快最简单好吗。","relation":"supports"},{"key":"E2","paragraph_id":"P003","quote":"先跑通了原型再开会。","relation":"supports"},{"key":"E3","paragraph_id":"P004","quote":"原型没跑通之前，老子自己对业务模型也没想明白","relation":"supports"},{"key":"E4","paragraph_id":"P005","quote":"开个会算算所有成本一小时几万几十万美元，净闲扯皮。","relation":"supports"},{"key":"E5","paragraph_id":"P010","quote":"一个真正伟大的开发项目在实质上只能是写核心代码的人主导的。","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文与结构一致，无图片节点。作者表达的是强烈偏向代码和原型优先的个人方法论；提问中的公司和人物比较未由正文举证。"
 },
 "2767684f": {
  "analysis": {
   "question_context":"提问者描述绝症与婆家冲突，作者把责任焦点放在伴侣是否管控其父母、道歉、补偿，而不是要求受影响者无条件承受。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"子女应管控父母造成的困扰，向伴侣道歉，提出改进和补偿方案，以取得共同承担风险的资格。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P005","P006","P007","P008","P009"],"summary":"管控、补偿和致歉被作者视为最低义务；爱不能降低责任，反而应加强。","role":"reason"},{"unit_id":"U003","paragraph_refs":["P010","P011","P012","P013","P014","P015","P016","P017","P018"],"summary":"反驳把既有付出换成要求对方承担拖累的逻辑，质疑其是否公平交易。","role":"rebuttal"},{"unit_id":"U004","paragraph_refs":["P019","P020","P021","P022","P023","P024","P025"],"summary":"把爱与奉献定义为不计价，禁止将付出当筹码剥夺对方自由。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"子女应负责管控父母给伴侣造成的困扰，并承担道歉、改进和补偿责任。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"这三重努力是让伴侣考虑承担剩余风险、继续共同生活的资格条件。","evidence":["E3"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"爱不能成为降低责任的理由；给对方造成困扰时，管控、补偿和致歉至少是基本责任。","evidence":["E4","E5"]},{"claim_id":"C004","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"既有付出不能被称为交换筹码，以此换取剥夺对方自由的特权。","evidence":["E6","E7"]}],
   "argument_steps":["划定子女对父母行为的责任范围（P001-P004）。","把责任提升为爱与做人基本义务（P005-P009）。","反驳“我对你好所以你应承受拖累”的交易逻辑（P010-P018）。","以不计价的爱和不得用筹码换自由作结（P019-P025）。"],
   "concept_usage":[{"term":"管控、补偿、致歉","meaning":"伴侣面对原生家庭造成损害时的三项最低行动。","evidence":"P003","ambiguity":"管控能力及补偿标准未定义。"},{"term":"爱无筹码","meaning":"既有爱的付出不能转化为要求对方承受损害或放弃自由的债权。","evidence":"P020-P024","ambiguity":"作者未处理双方长期互惠与资源分配的复杂情形。"}],
   "examples_and_targets":["婆家/父母给伴侣造成困扰的家庭关系（P001-P003）。","以院子挖坑烧烤、留下垃圾却向主人收费作类比（P021）。"],
   "conditions":["父母对伴侣造成困扰时（P001）。","爱与付出造成了实际负担时（P006-P007）。","不得以既有积极影响交换剥夺自由（P024）。"],
   "rhetoric_and_tone":"规范性强、对抗性明显；用反问和“倒霉和噩耗”否定不负责任的爱，以生活化烧烤垃圾类比强化道德指责。",
   "unresolved_questions":["未给出具体家庭事实，无法判断管控责任的可执行程度。","绝症、婆家关系和医疗决策的实际背景未展开。","无图片节点。"],
   "evidence":[{"key":"E1","paragraph_id":"P001","quote":"自己的父母对对方造成的困扰，是身为子女的自己要负责管控的责任范围。","relation":"supports"},{"key":"E2","paragraph_id":"P003","quote":"对管控不佳造成的损伤打算采用什么措施来补偿。","relation":"supports"},{"key":"E3","paragraph_id":"P004","quote":"是这三重努力的存在使得别人可以考虑承担剩余的风险","relation":"supports"},{"key":"E4","paragraph_id":"P007","quote":"对方有爱，这个责任只能加强，绝没有任何削弱这个责任的合理性","relation":"supports"},{"key":"E5","paragraph_id":"P009","quote":"这种“爱”，对人根本是倒霉和噩耗。","relation":"supports"},{"key":"E6","paragraph_id":"P012","quote":"我对你好换将来拖累你的权利","relation":"supports"},{"key":"E7","paragraph_id":"P020","quote":"以此为筹码来换自己剥夺对方自由的特权。","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文与结构一致，无图片节点。作者讨论的是责任和关系伦理，不是对提问者具体医疗或婚姻事实的裁判。"
 },
 "91ee65f7": {
  "analysis": {
   "question_context":"提问者问分子人类学与民族作为想象共同体是否冲突。作者并未做中性比较，而是提出强烈的政治历史论断：民族不是血统实体，民族史观与多元化政治被描述为殖民和分化工具。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"把中华民族界定为文化认同，并否定民族分类较其他历史分类具有额外合理性。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P005","P006","P007","P008","P009","P010","P011","P012","P013","P014"],"summary":"以混血儿和民族差异为例，断言民族史观服务于歧视、分裂和殖民。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P015","P016","P017","P018"],"summary":"把所有民族称为虚构、伪概念和意识形态陷阱，并否认种族民族存在。","role":"conclusion"},{"unit_id":"U004","paragraph_refs":["P019","P020","P021","P022","P023"],"summary":"将美国及殖民主义者关于新疆、西藏、香港和少数民族的叙事解释为制造差异和分裂。","role":"argument"},{"unit_id":"U005","paragraph_refs":["P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040","P041"],"summary":"进一步把多元化、少数民族保护和福山历史终结论批判为新殖民主义工具，并以“他错了”结尾。","role":"argument"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"中华民族不是血统身份而是文化认同身份。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"民族视角的历史划分是欧洲近代围绕殖民文化构建的思想武器，其合理性不高于其他分类体系。","evidence":["E2","E3"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"民族差异概念从诞生起就用于制造歧视链、猜疑链、仇恨和混乱。","evidence":["E4","E5"]},{"claim_id":"C004","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"所有民族和种族都是虚构，民族概念是意识形态陷阱。","evidence":["E6","E7"]},{"claim_id":"C005","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者把西方以保护多样化和少数民族为名的政治，解释为维持分裂、阻碍融合并服务新殖民主义。","evidence":["E8","E9"]}],
   "argument_steps":["先提出文化认同与血统身份之分（P001）。","比较民族、伦理、宗教、城邦、种族和阶级分类（P002-P004）。","以混血儿困难论证民族史观的排斥性（P005-P014）。","将民族概念总体否定为虚构和殖民工具（P015-P018）。","把当代多元化和少数民族议题纳入新殖民主义解释（P019-P037）。","以福山为例提出历史仍会变化并收束为“他错了”（P038-P041）。"],
   "concept_usage":[{"term":"民族","meaning":"作者否定其作为自然血统或种族实体的存在，同时承认文化认同层面可使用。","evidence":"P001/P018","ambiguity":"文化、政治、法律和人口统计意义混用。"},{"term":"多元化/多样性","meaning":"作者将其解释为被西方政治武器化、维持分裂的口号。","evidence":"P024-P034","ambiguity":"正文未区分不同语境下的多元化主张。"}],
   "examples_and_targets":["混血儿、犹太民族、大和民族、大韩民族（P005-P013）。","美国在新疆、西藏、香港议题上的叙事及香港身份旗帜（P019-P023）。","西方保护少数民族、多元化与福山（P024-P040）。"],
   "conditions":["作者讨论的是民族作为血统实体或政治分类时（P001-P003）。","在宣传机器强调群体差异时（P019）。","把同化、融合或统一视为灭绝时（P034）。"],
   "rhetoric_and_tone":"高度立场化、对抗性和阴谋论式叙述；大量绝对化词语、贬称和反问，直接指向美国、西方、殖民主义者及多元化倡导者。",
   "unresolved_questions":["关于民族、种族、殖民主义和具体地区议题的事实与学术依据均未给出。","“所有民族都是虚构”与文化认同、法律身份之间的关系未澄清。","本文是作者政治论述，不应将其断言当作已核验史实。无图片节点。"],
   "evidence":[{"key":"E1","paragraph_id":"P001","quote":"“中华民族”根本就不是一个血统身份，而是一个文化认同身份。","relation":"supports"},{"key":"E2","paragraph_id":"P002","quote":"这是欧洲近代的学术观点，是围绕着殖民文化而构建起来的思想武器。","relation":"supports"},{"key":"E3","paragraph_id":"P003","quote":"并没有什么额外的合理性。","relation":"supports"},{"key":"E4","paragraph_id":"P010","quote":"就是为了制造歧视链和猜疑链，为了制造仇恨和混乱。","relation":"supports"},{"key":"E5","paragraph_id":"P011","quote":"你们彼此有重大差别","relation":"supports"},{"key":"E6","paragraph_id":"P015","quote":"所有“民族”，追根到底都是虚构的。","relation":"supports"},{"key":"E7","paragraph_id":"P018","quote":"世界上根本就没有什么“种族”“民族”这两种东西存在。","relation":"supports"},{"key":"E8","paragraph_id":"P024","quote":"恰恰是为了制造最大的不平等","relation":"supports"},{"key":"E9","paragraph_id":"P025","quote":"西方的新殖民主义正在通过一种看起来似乎与殖民没有任何关系的、看似恰好相反的方式进行全新的实践","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文与结构一致，无图片节点。本文是强烈立场性的政治论述；作者断言、历史指涉和对当代地区议题的归因均需独立外部核验，本记录不替作者裁决真伪。"
 },
 "1cf4e727": {
  "analysis": {
   "question_context":"提问者问塔利班炸毁巴米扬大佛是否只是禁绝偶像崇拜。作者通过列举多起历史文化遗产破坏事件，论证意识形态动荡中破坏旧文化是反复出现的人类机制，并批评借此选择性指责新兴政权。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011"],"summary":"列举阿房宫、英国宗教改革、法国大革命、巴黎公社、太平天国、十月革命、破四旧和伊拉克等破坏文物事件。","role":"examples"},{"unit_id":"U002","paragraph_refs":["P012","P013","P014"],"summary":"归纳意识形态动荡会把旧遗产视为苦难源头，因此高概率发生文化遗产破坏。","role":"claim"},{"unit_id":"U003","paragraph_refs":["P015","P016","P017","P018","P019"],"summary":"把破坏解释为需要主观克制才能压制的人类习性，并以美国抗议中的雕像破坏作近例。","role":"reason"},{"unit_id":"U004","paragraph_refs":["P020","P021"],"summary":"认为借毁灭文物指责新兴政权，是利用人类习性和旁观者缺乏历史视野的选择性策略。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_reported","attribution":"author","modality":"asserted","statement":"历史上多个意识形态或政治动荡时期都发生过文化遗产破坏，塔利班并非唯一案例。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"意识形态动荡若把旧意识形态视为苦难源头，发生文化遗产破坏的概率基本接近必然。","evidence":["E3"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"破坏文物更像需要强力克制才能压制的人类习性，而不只是政策选择。","evidence":["E4","E5"]},{"claim_id":"C004","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"借毁灭文物指责新兴政权，是对人类破坏习性和旁观者历史无知的利用。","evidence":["E6"]}],
   "argument_steps":["先反问塔利班行为是否极端（P001）。","列举历史案例形成比较集合（P002-P011）。","从案例归纳意识形态动荡与文物破坏的关联（P012-P014）。","将其解释为人类习性并补充美国雕像案例（P015-P019）。","以选择性指责和幼稚利用作结（P020-P021）。"],
   "concept_usage":[{"term":"意识形态动荡","meaning":"导致旧意识形态被视为苦难源头的政治变动。","evidence":"P012","ambiguity":"范围和判断标准未定义。"},{"term":"人类习性","meaning":"在政治冲突中破坏旧文化遗产、需强力克制的倾向。","evidence":"P015-P016","ambiguity":"作者以历史例子归纳，未提供系统证据。"}],
   "examples_and_targets":["阿房宫、英国宗教改革、法国大革命、巴黎公社、太平天国、十月革命、破四旧、美国解放伊拉克（P003-P010）。","“黑命贵”抗议中的美国雕像破坏（P018）。","批评对象是借文物破坏选择性指责新兴政权的论述者（P020）。"],
   "conditions":["形成“旧意识形态应为苦难负责”的政治正确时（P012）。","当事人把遗产看作旧世界合理性的证明时（P013）。","缺乏强主观能动性克制时（P015-P016）。"],
   "rhetoric_and_tone":"以反问、历史清单和“谁又比谁高明”制造对比，语气讥讽并试图削弱对塔利班的单独道德谴责；结论带有强烈归因概括。",
   "unresolved_questions":["列举事件的具体史实、规模和因果关系未核验。","正文没有直接解释巴米扬大佛事件的宗教、政治和政策背景。","“概率百分之百”和人类习性是作者概括，不是已证明的统计结论；无图片节点。"],
   "evidence":[{"key":"E1","paragraph_id":"P002","quote":"来，我们来随便列举一下历史上比较出名的文化遗产破坏事件","relation":"supports"},{"key":"E2","paragraph_id":"P004","quote":"普遍的破坏了英国境内的天主教修道院和教堂","relation":"supports"},{"key":"E3","paragraph_id":"P012","quote":"发生“震惊世界”的“文化遗产破坏”的概率基本上是百分之百。","relation":"supports"},{"key":"E4","paragraph_id":"P015","quote":"它与其说是一种“政策”，不如说是一种“习性”。","relation":"supports"},{"key":"E5","paragraph_id":"P016","quote":"一种需要极强的主观能动性才能克制的人类习性。","relation":"supports"},{"key":"E6","paragraph_id":"P020","quote":"所以，借“毁灭文物”来指责新兴政权其实是一种对人类的幼稚的巧妙利用","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文与结构一致，无图片节点。作者用历史类比提出一般化解释，但未核验所列事件或巴米扬个案；本记录保留其论证，不将“百分之百”等修辞当作统计事实。"
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
