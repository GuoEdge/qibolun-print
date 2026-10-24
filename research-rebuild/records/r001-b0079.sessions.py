# -*- coding: utf-8 -*-
"""批次 r001-b0079 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0079.sessions.py            # 写 out/r001-b0079.out.jsonl
  python3 records/r001-b0079.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0079"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0079.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "97c93403": {
  "analysis": {
   "question_context": "提问者问“为什么有些人要骂胡锡进？”，把“骂胡锡进”当作待解释的现象。作者不评价胡锡进本人的言行，而是先给骂的动因（有人要杀鸡骇猴、有人喜欢找机会练“拳脚武艺”），再区分“骂”与“批评”，转而反驳用来指责胡锡进的“没有风骨”“前后矛盾”“立场摇摆”等标准。提问者的说法不等于作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "答骂胡锡进的两种动因：有人要杀鸡骇猴，另有很多人喜欢找机会练“拳脚武艺”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "提出区分：批评是批评，骂是骂。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "以模拟对方语气编对方的话来“证明”其可笑为例，类比穿对方衣服杀人以证明其邪恶，定性为娱乐性手法的攻击而非批评。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "街头殴打类比：看客只为拳脚好看叫好，并据此假定被打者“活该”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "反问水平，借“师傅说”给出评价：这是没水平。", "role": "other"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010", "P011"], "summary": "反驳指责胡锡进的标准：称“没有风骨”的标准幼稚、行不通；对“前后矛盾”“立场摇摆”逐一反问。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013", "P014"], "summary": "结论：这是用定义含糊、没人能做到、不会用在自己身上的“梦幻法则”判别人有罪；按此法连地藏菩萨都有罪。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "骂胡锡进的原因之一是有的人想杀鸡骇猴，另外又有很多人喜欢一切能练一下“拳脚武艺”的机会。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评与骂是两回事，应当区分。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问提出：自己模拟对方语气编一段对方的话来“证明”对方的“可笑”，和“穿上对方的衣服去杀个人来证明对方很邪恶”没有本质区别。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类做法根本不是什么批评，而纯粹是手法有娱乐性的攻击。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以街边殴打为类比：看客只关心拳脚好看，并为这好看就假定被殴打的人必然“活该”。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引述“师傅”的话给上述做法下评价：“这是没水平”。“师傅”身份未说明，作者是否完全认同未明言。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人用来指责胡锡进“没有风骨”的那种标准幼稚得一塌糊涂，现实里根本行不通。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“前后矛盾”的指责不成立：作者称活了几十年没见过能说十年话前后不矛盾的人，缩短到半年也没有；认为有人做得到只是对前后矛盾不敏感。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "对“立场摇摆”的指责提出反问：“不摇摆”是什么境界、能否确切定义、能否在不用政治正确遮脸堵嘴的前提下举出几十年立场从不“摇摆”的实例。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些指责归根到底只是自己设想了一种定义含糊、其实没人能做到、也绝不会用在自己身上的“梦幻法则”来判别人有罪。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按完美的道德法则人人都当然有罪，这是常识；按“梦幻级法则”，连地藏菩萨都有罪。", "evidence": ["E13", "E14"]}
   ],
   "argument_steps": [
    "以“因为有人想杀鸡骇猴”“另外又有很多人喜欢一切能练一下‘拳脚武艺’的机会”回答骂胡锡进的动因。",
    "提出区分前提：“批评是批评，骂是骂”。",
    "举例论证：模拟对方语气编话“证明”其可笑 ≈ 穿对方衣服杀人证明其邪恶，故不构成批评。",
    "以街头殴打与看客叫好作类比，说明围观逻辑会假定被打者“活该”。",
    "反问“这是个什么水平”，引“师傅说——这是没水平”作评价。",
    "转折到被用来指责胡锡进的标准：称其幼稚、现实里行不通。",
    "逐条反驳：“前后矛盾”无人能做到（经验断言）；“立场摇摆”无法定义、无法举证（反问）。",
    "结论：这是以定义含糊、没人能做到、不会用于自身的“梦幻法则”判别人有罪；以地藏菩萨作极端推论。"
   ],
   "concept_usage": [
    {"term": "骂", "meaning": "与批评相对，指以娱乐性手法进行的攻击（P005），不是就事论事的批评。", "evidence": "P003", "ambiguity": "作者只给出区分与定性，未给出判别“骂”与“批评”的可操作标准。"},
    {"term": "杀鸡骇猴", "meaning": "骂胡锡进的动因之一，指借骂某人以警戒他人。", "evidence": "P001", "ambiguity": "“有人”指谁未说明。"},
    {"term": "拳脚武艺", "meaning": "加引号，指借骂人练手、取乐的机会。", "evidence": "P002", "ambiguity": "具体所指（骂的技巧或围观表演）未展开。"},
    {"term": "风骨", "meaning": "引述他人指责胡锡进“没有风骨”时使用的标准；作者认为其幼稚、行不通。", "evidence": "P009", "ambiguity": "作者未给“风骨”下定义，只否定其作为指责标准。"},
    {"term": "梦幻法则/梦幻级法则", "meaning": "作者用语，指定义含糊、其实没人能做到、也绝不会用在自己身上的道德标准。", "evidence": "P012", "ambiguity": "无。"},
    {"term": "zzzq", "meaning": "作者用作“政治正确”的拼音缩写，指以政治正确遮脸堵嘴。", "evidence": "P011", "ambiguity": "未解释缩写的具体范围。"},
    {"term": "地藏菩萨", "meaning": "修辞材料，用来说明在梦幻级法则下连菩萨都有罪。", "evidence": "P014", "ambiguity": "属夸张修辞，非佛理讨论。"}
   ],
   "examples_and_targets": [
    "胡锡进：被骂与被称为“没有风骨”“前后矛盾”“立场摇摆”的对象，作者只反驳这些指责的标准，未评价其本人言行（P009-P011，修辞/反驳对象）。",
    "模拟对方语气编话与穿对方衣服杀人：作者的类比论证材料（P004）。",
    "街边殴打与围观叫好的看客：作者的类比材料，用来说明“骂”的娱乐性（P006）。",
    "“师傅说——这是没水平”：引述式评价，说话者为未具名的“师傅”（P008，引用）。",
    "地藏菩萨：夸张修辞材料（P014）。",
    "提问者的问题“为什么有些人要骂胡锡进？”：本文的回应对象（Q001）。"
   ],
   "conditions": [
    "作者关于“骂”的判断限定在“骂胡锡进”这一现象及以“没有风骨/前后矛盾/立场摇摆”为据的指责上，未推广到其他对象。",
    "P010 的经验断言有范围限定：“活了几十年”“说十年话”“甚至把这个时间周期缩短到半年”。",
    "P011 的举证要求附条件：“不用zzzq遮脸堵嘴的前提下”。",
    "P012 “梦幻法则”的成立条件：定义含糊、其实没人能做到、绝不会用在自己身上。"
   ],
   "rhetoric_and_tone": "口语化与网络化用语（“杀鸡骇猴”“拳脚武艺”“zzzq”“活该”）；密集反问（P004、P007、P011）承担论证；两处类比（P004 穿对方衣服杀人、P006 街头殴打与看客）；引“师傅说”制造评点口吻；末尾以“地藏菩萨都有罪”的夸张推论收束。对提问者不作称呼，直接以“因为……”作答。",
   "unresolved_questions": [
    "P001“有人想杀鸡骇猴”中的“有人”是谁，正文未说明；这是作者的归因判断，非可核查事实。",
    "P008“师傅说”的“师傅”身份不明，作者是引述他人还是自我代言未明说。",
    "作者未正面评价胡锡进本人言行，故不能据本篇推断作者对胡锡进的完整态度。",
    "P010 关于“没人能做到十年（或半年）前后不矛盾”为作者的经验断言，需外部核查其经验依据。",
    "“批评”与“骂”的判别标准正文未给出，仅有定性区分。",
    "brief 与正文开头重合（brief 是正文前段截断），未作为独立证据使用；平台未标注话题标签。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "因为有人想杀鸡骇猴，", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "而另外又有很多人喜欢一切能练一下“拳脚武艺”的机会。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "批评是批评，骂是骂。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "和“穿上对方的衣服去杀个人来证明对方很邪恶”有什么本质区别？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这就根本不是什么批评，而纯粹是手法有娱乐性的攻击罢了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "看客们只关心拳脚好看，就为这拳脚好看，就假定被殴打的人必然“活该”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这是个什么水平？", "relation": "context"},
    {"key": "E8", "paragraph_id": "P008", "quote": "师傅说——这是没水平。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "幼稚得一塌糊涂，现实里根本行不通。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "我还没见过活着的人类有能做到说十年话前后不矛盾的", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "或者不用zzzq遮脸堵嘴的前提下，举一个几十年立场从不“摇摆”的实例？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "也绝不会用在自己身上的梦幻法则来判别人有罪。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "根据完美的道德法则，人当然都有罪，这是常识", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "按梦幻级法则，地藏菩萨都有罪。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["舆论现象与媒介批评", "社会心理与围观", "道德评价标准"],
   "issue_candidates": ["对公众人物的批评与“骂”的区分", "以完美道德标准指责他人", "围观叫好的看客心理"],
   "text_function_candidates": ["答疑（回应知乎提问）", "评论", "论辩与反驳"],
   "object_candidates": ["胡锡进", "提问者", "看客", "未具名的“师傅”", "地藏菩萨"],
   "working_keywords": ["胡锡进", "杀鸡骇猴", "拳脚武艺", "批评", "骂", "风骨", "前后矛盾", "立场摇摆", "zzzq", "梦幻法则", "地藏菩萨"]
  },
  "notes": "无图片，正文与 lexical 一致（仅 paragraph 节点）。brief 与正文开头重合，仅作导航。Q001 属提问者。P008 为引述“师傅”语，未归给作者本人。"
 },
 "7b8df002": {
  "analysis": {
   "question_context": "提问者问“如何解决思维混乱、讲话没条理的情况？”。作者给出名为“一句话+注释”的经典做法，并用“我们主张用严厉的手段打击假冒伪劣现象”逐要素示范如何把一句话展开成问题清单；随后把这一做法提升为分析能力与阅历的问题，再类比“司法解释”，主张沟通技能本质上是立法技术，最后以“私域君主”的比喻界定成功的人生。全篇以第二人称对提问者作方法指导。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出“一句话+注释”的做法：先把方案、建议、主张总结成一句话，再逐个精确解释其中每个要素短语。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "举例并拆解关键词：“我们/主张/严厉的手段/打击/假/冒/伪/劣/现象”。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014"], "summary": "按要素逐项展开成连续提问清单（“我们”的边界、主张的方式与成本、何谓严厉、执行机构与程序、何谓假冒伪劣、现象与绩效）。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016"], "summary": "小结：按此框架一切可回到那一句话；这也是话有轻重之别的奥秘所在。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018"], "summary": "提升判断：每个问题追根到底是深学术问题，最终回到最基本的问题，答案是分析能力与长期阅历反省的综合结果。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020"], "summary": "限定：分析能力可以通过经典著作、做题、研讨会获得，但阅历急不了，须保持耐心。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023"], "summary": "指出缺阅历的后果（展开做不深、答案有裂痕、话缺少权柄），告以坚持并接受被吐槽，勿以学术训练自恃。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "行动建议：等待阅历，等不及可主动冒险经历；能力与阅历兼备才能以“勉力为之、随遇而安”的心态做事，并保持耐心与“学徒自觉”。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P028", "P029"], "summary": "旁论：人生最好的安排是前半生经历尽可能多【正直而光荣的失败】而幸存，而不是“学富五车”。", "role": "other"},
    {"unit_id": "U010", "paragraph_refs": ["P030", "P031", "P032"], "summary": "承认他人看出这近似“司法解释”的风格，并给出理由：有效沟通即“临时约法”，沟通技能即【立法技术】。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P033", "P034", "P035"], "summary": "行动建议：理解法律史、法的原理与各文明法律实践；人人须是“学法律的”，并指向作者置顶贴。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040"], "summary": "“私域君主”比喻的展开：立法不健全使人成为其王国注定的罪人，最终称孤道寡。", "role": "reason"},
    {"unit_id": "U013", "paragraph_refs": ["P041", "P042"], "summary": "结论：重新界定“成功的人生”，并断言明白此点者前途无量。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P043", "P044", "P045", "P046"], "summary": "英文祝词收尾（Long live the Queen/King 等四行）。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有一种简单的经典做法“一句话+注释”：先把方案、建议、主张总结成一句话，再以逐个精确解释这句话里每一个要素短语的方式来阐述其含义。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“我们主张用严厉的手段打击假冒伪劣现象。”为例，其关键词为“我们/主张/严厉的手段/打击/假/冒/伪/劣/现象”，并可按要素逐项展开提问。", "evidence": ["E4", "E5", "E6", "E7"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按这个框架，一切都可以最后回到那一句话上；这也是有的人话轻如鸿毛、有的人的话重有千钧的奥秘所在。", "evidence": ["E8", "E9"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里面的每一个问题追根到底都是非常深的学术问题；每句话都有更深的分解和解释的必要，最终回到“什么是应该的？什么是好的？什么是存在的？以及它是谁？”，而这些答案都是高度分析能力和长期阅历反省的综合结果。", "evidence": ["E10", "E11"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "高度的分析能力可以多看经典著作、做题、参加研讨会请别人砥砺来学，但阅历急不了，所以要保持耐心。", "evidence": ["E12", "E13"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "缺这份阅历，同样的展开自己很难做深，写下的答案会有自己看不出的裂痕；是分解框架和分解结果的缺陷使话缺少权柄。", "evidence": ["E14"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要坚持下去、让别人吐槽，接受“我现在被说不对是很正常的”这一基本认知；不要因为受过“名门正派”的学术训练、掌握套路和书面套话，就以为这组展开可以轻松摆平。", "evidence": ["E15", "E16"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "要等待阅历发生；如果等不及，可以主动去冒险和经历，优先积累这些阅历。", "evidence": ["E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能力和阅历兼备才能靠谱地做这件事，尤其才能以“其实我做不到、勉力为之，随遇而安”的心态来做；这样才不容易得抑郁症、不容易自杀，或不被身边无法再忍受其傲慢的人抛弃。", "evidence": ["E18", "E19"]},
    {"claim_id": "C010", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "有人看出这似乎就是“司法解释”的风格（转述他人观察，说话者身份不明）。", "evidence": ["E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认同上述观察，理由为：每一次有效的沟通本质上都是一次“临时约法”，“沟通技能”本质上就是【立法技术】。", "evidence": ["E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强烈建议人去理解法律史、法的原理和各个文明的法律实践；哪怕不是“学法律的”，只要是人、只要需要与人合作，就必须是个“学法律的”——不是掌握限行法条，而是掌握立法技术，善于敏捷而有效地构建自己的私法。", "evidence": ["E23", "E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人是自己私域的天然君主，每一个踏入其领域的人都预先抱着遵守其法律（即“入乡随俗”）的良好意愿；有些人很难拥有忠实的关系人，是因为其立法精神不健康、立法技术不健全，所立法条语焉不详、漂浮不定、自相矛盾。", "evidence": ["E25"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这使一切踏入其私域之人逻辑上必然成为其王国注定的罪人；而其又毫不仁慈，于是人们若不想做罗宾汉、又不想做宋江，就只好做索尔仁尼琴，最终只好称孤道寡。", "evidence": ["E26", "E27", "E28"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“成功的人生”：不是“亿万家财”“声名卓著”，而是仁慈的君主以简洁、准确、稳定而又有效的约法施行贤明治理，所行之处鲜花盛开、百废俱兴，所居之人没有恐惧却有面对自我的勇气和面对未知的信心。", "evidence": ["E29"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "能明白这一点并把它嵌入自己的本能，就一定前途无量。", "evidence": ["E30"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议读者去看作者的置顶贴，体会这是一种什么样的实践以及它有什么作用。", "evidence": ["E31"]}
   ],
   "argument_steps": [
    "定义方法：方案、建议、主张先总结成一句话，再逐要素精确解释（“一句话+注释”）。",
    "例证：以“我们主张用严厉的手段打击假冒伪劣现象。”拆出九个关键词。",
    "展示展开：对每个要素连续提问（谁是“我们”、主张的实现方式与成本、何谓严厉、执行机构与程序、何谓假/冒/伪/劣、现象与绩效衡量）。",
    "小结：一切最后回到那一句话，故话有轻重之别。",
    "提升：这些追问都是深学术问题，最终归于“应该/好/存在/它是谁”等基本问题，答案是分析能力与阅历的综合。",
    "限定：分析能力可学，阅历急不了，须耐心。",
    "让步式告诫：缺阅历则答案有裂痕、话无权柄；勿以学术训练自恃。",
    "行动要求：等待阅历，等不及则主动冒险经历；能力与阅历兼备方能以随遇而安的心态做事。",
    "旁论：人生最好安排是经历【正直而光荣的失败】而幸存，而非“学富五车”。",
    "类比转折：他人指出这像“司法解释”，作者接受并推出“有效沟通即临时约法”“沟通技能即立法技术”。",
    "行动要求：理解法律史与法理，人人须掌握立法技术以构建私法。",
    "比喻展开：私域君主与私法；立法不健全使关系人成为“注定的罪人”，君主称孤道寡。",
    "结论：重新定义成功的人生为贤明治理；断言明白此点者前途无量。"
   ],
   "concept_usage": [
    {"term": "一句话+注释", "meaning": "作者提出的表达与思维方法：先把主张压缩成一句话，再逐个精确解释其中的要素短语。", "evidence": "P001", "ambiguity": "“经典做法”出自何处未说明。"},
    {"term": "要素短语/关键词", "meaning": "构成那句话的各个语词单位，如“我们”“主张”“严厉的手段”等，是展开注释的入口。", "evidence": "P003", "ambiguity": "拆分粒度由谁决定未说明。"},
    {"term": "权柄", "meaning": "指话语的权威与分量；作者认为它取决于分解框架与分解结果的完整程度。", "evidence": "P021", "ambiguity": "非制度性权力，属作者的比喻用法。"},
    {"term": "阅历", "meaning": "与分析能力并列的条件，指长期的反省与经历，作者认为无法速成。", "evidence": "P020", "ambiguity": "与“经验”的区别未界定。"},
    {"term": "学徒自觉", "meaning": "作者自造提法，指保持学徒心态、承认自己会被指出错误。", "evidence": "P027", "ambiguity": "未给出具体做法。"},
    {"term": "司法解释", "meaning": "他人对上述展开风格的评价，作者在 P031 接受这一类比。", "evidence": "P030", "ambiguity": "说话者身份不明；作者只说“不错”，未展开该类比。"},
    {"term": "临时约法", "meaning": "指每一次有效沟通本质上都是临时订立的约定。", "evidence": "P031", "ambiguity": "借用历史名词作比喻，未界定其范围。"},
    {"term": "立法技术", "meaning": "作者认为等同于“沟通技能”，指构建规则的能力，而非现行法条知识。", "evidence": "P032", "ambiguity": "与法学意义上的立法技术是否同义，作者未说明。"},
    {"term": "私域/私法", "meaning": "指个人自己的人际领域及其中由自己订立的规则。", "evidence": "P036", "ambiguity": "“私法”为法学既有术语，此处被作者移用。"},
    {"term": "成功的人生", "meaning": "作者重新定义：不是财富与声名，而是以简洁、准确、稳定、有效的约法施行贤明治理。", "evidence": "P041", "ambiguity": "属价值主张，无判定指标。"}
   ],
   "examples_and_targets": [
    "“我们主张用严厉的手段打击假冒伪劣现象。”：作者为演示方法自设的例句（P005，示例）。",
    "“我们/主张/严厉的手段/打击/假/冒/伪/劣/现象”：作者的拆词示例（P006）。",
    "作者置顶贴：作者指向的自身其他文本，本篇未给出内容（P035，引用/指引）。",
    "罗宾汉、宋江、索尔仁尼琴：比喻性人物，用来说明不想反抗也不想屈从者的处境（P039，修辞材料）。",
    "Long live the Queen/King 等四行英文：结尾致辞（P043-P046，修辞）。",
    "“名门正派的学术训练”“套路和书面套话”：被作者告诫不可自恃的对象（P023，批评对象）。",
    "提问者的问题：本文回应对象（Q001）。"
   ],
   "conditions": [
    "方法的前提：把自己的方案、建议、主张总结成一句话（P002），并以逐个精确解释要素短语的方式阐述（P003）。",
    "能力条件：需要高度的分析能力与长期阅历反省的综合结果（P018）；阅历“急不了”（P020）。",
    "条件句：“如果你等不急，你可以主动去冒险和经历，去优先积累这些阅历”（P024）。",
    "适用对象条件：“只要你是人、只要你需要与人合作，你必须是个‘学法律的’”（P034）。",
    "私域君主说的依赖前提：每一个踏入其领域的人预先抱着遵守其法律的良好意愿（P036）。",
    "程度限定：本篇用“你很难做得很深”（P021）、“你才能以一个……的心态来做”（P025）等表述，未把效果说成必然。"
   ],
   "rhetoric_and_tone": "教学与训诫并用的第二人称“你”贯穿全篇；以连续排比式提问充当展开示范（P008-P011）；举商业/执法例句作演示；比喻密集（沟通=临时约法、沟通技能=立法技术、私域=王国、君主/罪人）；引俗语与典故（话轻如鸿毛/重有千钧、罗宾汉、宋江、索尔仁尼琴）；结尾突然转为英文祝词（P043-P046），带戏仿君主致辞的调侃色彩；间有自嘲式告诫（P022“让别人吐槽”、P026）。",
   "unresolved_questions": [
    "P035 提到的“我的置顶贴”内容未在本篇给出，需回查该作者置顶贴才能确认所指实践。",
    "P030“有人看出来了”的主体不明，无法判断是读者、评论者还是作者自设。",
    "P034“限行法条”疑为“现行法条”的笔误，原文如此，未擅改，引用与理解时需注意。",
    "P039 罗宾汉、宋江、索尔仁尼琴三者的具体对应关系与所指（反抗、屈从、流亡/揭露？）正文未解释。",
    "P039-P040 中“人们”与“ta们”的指代在句子间切换，所指为“立法不健全者”还是“关系人”存在歧义。",
    "P028“人生最好的安排”为价值主张，不可核查；P016“话轻如鸿毛/重有千钧”为修辞性表述。",
    "版本：published 2020-11-03，updated 2024-07-02；本篇以当前版本正文为准，无法从本记录判断版本差异。",
    "无图片，正文与 lexical 一致（仅 paragraph 节点）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有一种很简单的经典做法。就是采用“一句话+注释”的做法。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "首先，把你的方案、建议、主张，总结成一句话。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "以逐个精确解释这句话里的每一个要素短语的方式来阐述这句话的含义。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "“我们主张用严厉的手段打击假冒伪劣现象。”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "这里面的关键词就是：我们 / 主张 / 严厉的手段 / 打击 / 假 / 冒 / 伪 / 劣 / 现象", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "“我们”是谁？我们的边界是什么？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "“严厉手段”，什么样的手段？经济、舆论、武力、心理手段？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "按照这个框架，一切都可以最后回到那一句话上。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "这也是为什么有的人话轻如鸿毛，有的人的话重有千钧的奥秘所在。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "其实，这里面的每一个问题追根到底都是非常深的学术问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "什么是应该的？什么是好的？什么是存在的？以及它是谁？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "高度的分析能力，你可以多看些经典著作去学，去做题，去参加研讨会请别人砥砺。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "但是这份阅历急不了，所以你要保持耐心。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "是这分解的框架和分解的结果的缺陷，使得你的话缺少权柄。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "但你要坚持下去，让别人吐槽，接受“我现在被说不对是很正常的”的基本认知。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "就以为这组展开你就可以轻松摆平了。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P024", "quote": "你要等待阅历发生。如果你等不急，你可以主动去冒险和经历，去优先积累这些阅历。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "能力和阅历兼备，你才能靠谱的做现在的这件事", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "你才不容易自杀，或者被你身边无法再忍受你的傲慢的人抛弃。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "有人看出来了——这似乎就是“司法解释”的风格。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P031", "quote": "不错，因为每一次有效的沟通，本质上都是一次“临时约法”。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P032", "quote": "“沟通技能”，本质上就是【立法技术】。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P033", "quote": "所以我强烈的建议人去理解法律史、法的原理和各个文明的法律实践。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P034", "quote": "只要你是人、只要你需要与人合作，你必须是个“学法律的”。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P036", "quote": "所立的法条语焉不详、漂浮不定、自相矛盾。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P037", "quote": "这使得一切踏入ta的私域之人都逻辑上必然的成为ta王国的注定的罪人。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P039", "quote": "于是人们若不想做罗宾汉，又不想做宋江，就只好做索尔仁尼琴。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P040", "quote": "所以ta们最终只好称孤道寡。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P041", "quote": "而是指一个仁慈的君主以ta简洁、准确、稳定而又有效的约法所行的贤明的治理", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P042", "quote": "把这一点嵌入你自己的本能，你一定前途无量。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P035", "quote": "你们可以看一下我的置顶贴，体会一下这是一种什么样的实践，以及它有什么作用。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P028", "quote": "人生最好的安排，是前半生经历了尽可能多【正直而光荣的失败】而幸存", "relation": "context"},
    {"key": "E33", "paragraph_id": "P029", "quote": "人类那点“学问”，其实根本不该占用人那么多青春的。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["表达与沟通方法", "思维方法/分析能力", "法理与规则类比", "人生修养"],
   "issue_candidates": ["如何解决思维混乱与讲话没条理", "把主张分解为可解释的要素", "沟通等同于立法", "阅历与分析能力的关系"],
   "text_function_candidates": ["答疑（回应知乎提问）", "方法教学", "经验总结", "训诫"],
   "object_candidates": ["提问者", "作者（“我”）", "例句中的“我们”", "罗宾汉", "宋江", "索尔仁尼琴"],
   "working_keywords": ["一句话+注释", "要素短语", "展开", "权柄", "阅历", "学徒自觉", "司法解释", "临时约法", "立法技术", "私域", "私法", "入乡随俗", "正直而光荣的失败"]
  },
  "notes": "无图片，正文与 lexical 一致（仅 paragraph 节点）。P030 为转述他人观察（说话者不明），未归给作者本人；P043-P046 为英文祝词，按原文保留。P034“限行法条”原文如此，疑为笔误，未擅改。"
 },
 "c58bad68": {
  "analysis": {
   "question_context": "提问者问“踏实是什么？”。作者先以“冗余、备份和信仰”三词作答，再逐条给出定义，最后把前两条归为人事、第三条归为天命，得出“心安就是踏实”。全篇是定义式短答，作者以“你”泛称读者，未引用他人观点，也无对抗性对象。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "先给出三词答案“冗余、备份和信仰”，并提示将作解释。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "分别定义冗余（超额准备成本/努力）、备份（可重来或独立双份）、信仰（能力不足或认知有限时确认用心良好，失败也是“正确的错误”）。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "“正确的错误”自有上天垂怜；前两条属人事，后一条属天命。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "结论：人事和天命都安放好了心就安，心安就是踏实。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "踏实即“冗余、备份和信仰”三事。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "冗余指为一万成本的事准备付出五万成本，只需一分努力的事做五分努力的准备。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "备份指做好重来一次甚至n次的准备，或者干脆做两份独立的放不同地方。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "信仰指当能力不足、做不到上述两条时，或明知做了上述两条也只是基于当前狭隘、幼稚的认知在自以为保险时，知道自己的用心是良好的，即使失败，也是“正确的错误”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“正确的错误”自有上天垂怜。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "冗余与备份是人事，信仰是天命；人事和天命都安放好了，心就安了。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "心安就是踏实。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "先给结论式三词答案：冗余、备份和信仰。",
    "逐条定义：冗余=超额成本与努力；备份=可重来或独立双份；信仰=在能力不足或认知有限时确认用心良好。",
    "以“正确的错误，自有上天垂怜”为信仰一项收束。",
    "归类：前两条为人事，后一条为天命。",
    "结论：人事与天命都安放好则心安，心安即踏实。"
   ],
   "concept_usage": [
    {"term": "冗余", "meaning": "为一万成本的事准备付出五万成本，只需一分努力的事做五分努力的准备，即超额准备。", "evidence": "P003", "ambiguity": "未说明超额比例如何确定。"},
    {"term": "备份", "meaning": "做好重来一次甚至n次的准备，或做两份独立的分放不同地方。", "evidence": "P004", "ambiguity": "与“冗余”的边界未严格区分。"},
    {"term": "信仰", "meaning": "能力不足或明知准备仍可能因认知狭隘而失败时，确认“用心是良好的”，从而安放自己。", "evidence": "P005", "ambiguity": "信仰的对象未明说（非宗教含义的自持？）。"},
    {"term": "正确的错误", "meaning": "用心良好但因此认知所限而失败的行动，作者称其自有上天垂怜。", "evidence": "P005", "ambiguity": "判定标准未给出；“上天垂怜”为不可核验表述。"},
    {"term": "人事/天命", "meaning": "作者把冗余、备份归为人事，把信仰归为天命。", "evidence": "P007", "ambiguity": "沿用传统语汇，未界定范围。"},
    {"term": "踏实", "meaning": "本篇的答案：心安即踏实。", "evidence": "P009", "ambiguity": "以“心安”定义“踏实”，两者均未进一步界定。"}
   ],
   "examples_and_targets": [
    "“一万成本的事、准备付出五万成本”“只需要一分努力的事，做五分努力”：作者为解释“冗余”给出的数量示例（P003，示例）。",
    "“重来一次甚至n次”“做两份独立的放不同地方”：作者为解释“备份”给出的示例（P004）。",
    "“上天”：作者用以收束“正确的错误”的修辞性指涉（P006）。",
    "提问者的问题“踏实是什么？”：本文回应对象（Q001）。",
    "本篇未出现被反驳对象、引文或历史事例。"
   ],
   "conditions": [
    "信仰一项的适用条件有二：能力不足、做不到冗余与备份；或明知做了这两条也只是基于当前狭隘、幼稚的认知在自以为保险（P005）。",
    "结论依赖前提“人事和天命都安放好了”（P008）。",
    "程度/数量限定：“一万成本……五万成本”“一分努力……五分努力”“重来一次甚至n次”（P003、P004），属举例而非精确规则。",
    "全篇以“你”泛指读者，未限定具体人群或场景。"
   ],
   "rhetoric_and_tone": "极简格言体：先以三个名词作答，第二段“好吧，解释一下吧：”转为解释口吻；逐条定义句式整齐；末两段以“人事和天命都安放好了，心就安了”“心安就是踏实”递进收束。“正确的错误，自有上天垂怜”带半文半白的格言腔。无反问、无讽刺、无论辩对象。",
   "unresolved_questions": [
    "“信仰”的对象或内容未明说：P005 只说“知道你的用心是良好的”，未说明是否指宗教信仰、自我信念或其他。",
    "“正确的错误”的判定标准，以及“自有上天垂怜”是实指还是比喻，正文未说明。",
    "三项（冗余、备份、信仰）是否穷尽“踏实”的构成，正文未作论证。",
    "以“心安”定义“踏实”有循环定义的嫌疑（心安本身亦未界定），正文未澄清。",
    "“上天垂怜”属不可外部核验的表述，需按作者的价值语汇处理，不作事实断言。",
    "版本：published 2020-11-05，updated 2021-05-16；本篇以当前版本为准，无法从本记录判断版本差异。",
    "无图片，正文与 lexical 一致（仅 paragraph 节点）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "冗余、备份和信仰。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "冗余，是指一万成本的事、准备付出五万成本。只需要一分努力的事，做五分努力的准备。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "备份，是指做好重来一次甚至n次的准备、或者干脆做两份独立的放不同地方。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "知道你的用心是良好的，即有失败，也是正确的错误。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "正确的错误，自有上天垂怜。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "前两条就是人事，后一条就是天命。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "人事和天命都安放好了，心就安了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "心安就是踏实。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生修养与心理安顿", "风险准备与冗余思维", "天命/信仰语汇"],
   "issue_candidates": ["踏实是什么", "如何获得心安", "超额准备与备份", "用心良好但失败如何自处"],
   "text_function_candidates": ["答疑（回应知乎提问）", "定义式解释", "格言式短答"],
   "object_candidates": ["提问者", "作者（“你”）", "“上天”（修辞指涉）"],
   "working_keywords": ["冗余", "备份", "信仰", "正确的错误", "上天垂怜", "人事", "天命", "心安", "踏实"]
  },
  "notes": "无图片，正文 9 段全部读完，正文与 lexical 一致。brief 与正文重合且被截断（止于“又或者你知道就算做了上述两条你也只”），仅作导航，未用于支持任何主张。全篇无引文、无被反驳对象，提问者立场未被归给作者。"
 },
 "6d972b31": {
  "analysis": {
   "question_context": "提问者问《黑神话：悟空》的建筑和主角盔甲是否是日式的、中式甲与日式甲有何区别。作者先以数段谈盔甲（古代中国甲式多样、实战以好用为准、反对以民族主义论甲），再转谈建筑：反驳“建筑都是歇山顶违背常识和规定”的说法，用古画与建筑结构解释歇山顶为何流行，并主张“破风”等结构并非日本独特发明；后半篇转入纸折扇发明权，质疑“日本发明折扇”的文献依据与合理性。作者的讨论多在“近代以前”的历史层面展开，未逐项评定游戏中的具体盔甲与建筑。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "论盔甲：古代中国除技术做不到者外各种有可取之处的甲都可能有，包括“日式盔甲”；按朝代/民族给军队定甲式是电影与得胜图的分辨需要，实战中什么甲好就用什么，两军样式会互相渗透；在保命装备上讲“民族主义”荒谬。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008"], "summary": "转入建筑：否认“建筑都是歇山顶显然违背常识和规定”，称中国建筑样式丰富灵活。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "以元《江天楼阁图》（主副楼皆歇山顶）、明、隋唐三组图片及图注为证。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"], "summary": "以《清明上河图》反问歇山顶是否高贵违制；并以“若古王朝真能抓尽违制建筑，何至于易亡”反问。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "反对按教科书等级规则理解世界：古画中“庑殿顶”小卖铺、戏园子小庄园的歇山顶、混搭顶与“拱顶”“罗马穹顶”都不稀罕。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "解释歇山顶流行：中式建筑靠柱础立柱、最怕“湿脚”，歇山顶是小建筑整圈护住柱脚的近乎唯一选择；硬山顶两层护不住，三五开间做庑殿顶效果可笑；有钱人盖长住房子几乎必做歇山顶。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033"], "summary": "宫观、城楼几乎必是歇山顶，故“没得选择”；以地方豪强口吻模拟“你不准老子也要修”，带威胁性调侃。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "论“破风”：中国有之不奇怪、不构成“日本风”；近代以前中日皆有的同原理结构源自日本的可能性基本是零，因古代日本对中国的文化影响基本为0，晚清以前中国无物师从日本；作者称这是逻辑问题而非民族自尊心问题。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048"], "summary": "折扇发明权：该说法依据主要是文献资料，但《永乐大典》仅存4%，四库全书时期禁毁严重（引文与统计数字，来源未标注）；文献“有”可证有，文献“没有”只是间接论证，不足为全信。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053"], "summary": "举证日本造纸晚于中国近六百年（公元62-121年 vs 610年以后），此前无文字、住窝棚、缺金属工具与大型城市。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P054", "P055"], "summary": "以殷墟妇好墓出土玉挖耳勺作工艺水平对比（图片证据，未核验）。", "role": "example"},
    {"unit_id": "U012", "paragraph_refs": ["P056", "P057", "P058"], "summary": "类比：让没文字、住窝棚、缺金属工具的群体先发明纸折扇返销中国，如太平洋土著先发明水力锻锤；而水力锻锤需要大量前提知识。", "role": "example"},
    {"unit_id": "U013", "paragraph_refs": ["P059", "P060", "P061", "P062"], "summary": "提出历史记忆形成的内在规律：原型可能出自难被相信的小地方，最终以发扬光大者之名流传；以VCD、U盘为例并作古代假设反问。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067"], "summary": "结论：作者更怀疑“日本纸折扇”是“幸运饼干”式的本地物附会海外品牌；除非经济规律不奏效，看不出其源自日本的现实性；讥文献中“日本所贡”如以为加州牛肉面原产加州。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代中国除了技术做不到的，任何形式的有可取之处的盔甲都可能有，包括“日式盔甲”。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“唐军就是xx甲”“西夏军就是xx甲”一类说法只是拍电影、画得胜图为了让人好分清人的需要，根本不是现实。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真打起来什么甲好就是什么甲；两军样式会因缴获、改装、仿制、测试而打成“你中有我，我中有你”。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问表示：在保命的装备上讲“民族主义”是荒谬的（“谁疯了……？嫌命长么？”）。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“建筑都是歇山顶显然违背常识和规定”的说法并不见得如此，中国建筑的样式丰富灵活得很。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "歇山顶是否高贵、是否违制，看《清明上河图》即可知并非个个都是宫殿、道观。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问表示：若古代王朝真有能力把境内违章建筑抓尽杀光，它们不会这么容易亡。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要根据教科书“庑殿顶最尊贵，歇山顶次之，平民只能用硬山顶”的规则就以为世界按此运行；作者称多翻古画可见“庑殿顶”小卖铺多得是，戏园子、小庄园“几乎间间都是歇山顶”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "各种混搭顶、不知算不算抱厦的“抱厦”、各种“破风”，甚至“拱顶”“罗马穹顶”也不稀罕；不要根据书本介绍理解世界。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "歇山顶流行是因为它几乎是小型建筑想做整圈屋檐保护所有柱脚不受雨水侵蚀的唯一选择（中式建筑靠柱础立柱、最怕湿脚；硬山顶两层护不住柱脚；三五开间做庑殿顶效果可笑）。", "evidence": ["E15", "E16", "E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "有点钱的人要盖不是打算住两年就丢的房子，几乎肯定做歇山顶；宫观建筑、城楼也几乎必是歇山顶。", "evidence": ["E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "所谓“破风”是日本拿着中国的小结构到处用，谈不上“日本的独特发明”；中国有任何结构的“破风”都不奇怪，有了也不成其为任何意义上的“日本风”。", "evidence": ["E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "近代以前，如果一个结构原理一致的东西中国有日本也有，起源地是日本的可能性基本是零，无论日本现存多少数量；因为古代日本对中国的文化影响基本是0。", "evidence": ["E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "日本西渡而来的人物在唐宋明甚至清面前没有可特别教授的东西，加上中国天朝上国的心态不认可日本有优势，故无人去学（以连续反问支撑）。", "evidence": ["E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "晚清以前中国没有任何东西反过来师从日本，故谈不上“源自日本”；作者强调这不是民族自尊心问题，而是逻辑问题。", "evidence": ["E27", "E28"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“折扇是日本发明的”这一说法的依据主要是文献资料。", "evidence": ["E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "文献保存不全：《永乐大典》仅存4%；四库全书时期禁毁规模巨大（作者引用一段评语与一组统计数字，均未标注出处）。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "文献里“有”可以说明“有”，有可信度；文献里“没有”只是间接论证，不足以为全信。", "evidence": ["E33", "E34"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不信日本发明折扇：中国有纸在公元62-121年间，日本人从朝鲜人学会造纸是610年以后，中间差近六百年；此前日本无文字，难以传承复杂工艺。", "evidence": ["E35", "E36", "E37", "E38"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "以类比说明不合理：让没文字、住窝棚、缺金属工具与大型城市的群体发明纸折扇返销中国，如同让太平洋土著先于世界发明水力锻锤；而水力锻锤需要大量前提知识。", "evidence": ["E39", "E40", "E41"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "历史记忆的形成有内在规律：原型可能出自难被相信的小地方，最终以把该物发扬光大者的名字为准；作者以VCD、U盘为例，并假设此事发生在无互联网的古代作反问。", "evidence": ["E42", "E43", "E44"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者更怀疑“日本纸折扇”是一种“幸运饼干”式的发明：根本是本地的东西，因太怪异而扯了“海外品牌”；理由是若它真畅销且不涉及难观摩的冶金工艺，经验多一千多年的中国手工艺者没有理由做不过“日本匠人”。", "evidence": ["E45"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "negated", "statement": "除非经济规律不奏效，作者看不出任何纸折扇真的是源自日本的现实性。", "evidence": ["E46"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对文献中“日本所贡”的记载，作者以“加州牛肉面”为喻，认为把此类记载当作原产地证据不可靠。", "evidence": ["E47"]}
   ],
   "argument_steps": [
    "先立论：古代中国除技术做不到者外，各种有可取之处的甲都可能有，包括“日式盔甲”。",
    "反驳以朝代/民族整体标注甲式的做法：那是电影与得胜图的分辨需要，非现实；实战中什么甲好用就用什么，样式互相渗透。",
    "以反问否定在保命装备上讲“民族主义”。",
    "转入建筑，否认“建筑都是歇山顶显然违背常识和规定”。",
    "举图（元《江天楼阁图》主副楼皆歇山顶、明、隋唐）与《清明上河图》为证。",
    "反问：若古代王朝真能抓尽境内违制建筑，何至于如此容易亡。",
    "反对按教科书等级规则理解世界，举古画中小卖铺的“庑殿顶”、戏园子小庄园的歇山顶、混搭顶与穹顶为例。",
    "解释机制：中式建筑靠柱础、最怕湿脚；歇山顶是小建筑整圈护柱脚的近乎唯一选择，硬山与庑殿顶都不合用；故有钱人、宫观、城楼几乎必用歇山顶。",
    "以拟人独白表现“违制也要修”的现实压力。",
    "论断“破风”非日本独特发明，并给出一般原则：近代以前中日同有的同原理结构源自日本的可能性基本为零，因古代日本对中国文化影响基本为零。",
    "以日本无可教授之物与天朝上国心态解释“无人去学”，并称这是逻辑问题而非民族自尊心问题。",
    "转向折扇：说明该说法依据主要是文献资料，指出文献保存不全（永乐大典仅存4%、四库禁毁），并区分“文献有”与“文献没有”的证据力。",
    "举证日本造纸与中国相差近六百年、此前无文字住窝棚。",
    "以太平洋土著发明水力锻锤作类比。",
    "提出历史记忆形成规律（以发扬光大者命名），举VCD、U盘并作古代假设。",
    "结论：怀疑“日本纸折扇”是“幸运饼干”式发明；除非经济规律不奏效，看不出其源自日本的现实性；讥“日本所贡”记载之不可靠。"
   ],
   "concept_usage": [
    {"term": "“xx甲”/日式盔甲", "meaning": "作者指以朝代或民族整体标注军队盔甲样式的说法，认为那是辨识需要而非现实；并主张中国也可能有“日式盔甲”。", "evidence": "P003", "ambiguity": "“日式盔甲”在文中加引号，具体所指（形制特征）未界定。"},
    {"term": "民族主义", "meaning": "作者在论甲与论建筑起源时批评的立场：以民族归属而非实用/逻辑判断优劣。", "evidence": "P006", "ambiguity": "作者未区分民族主义的不同用法。"},
    {"term": "歇山顶", "meaning": "文中讨论的核心建筑形制：作者主张其流行出于护柱脚的实用需要，而非单纯的等级高贵。", "evidence": "P024", "ambiguity": "未给出形制定义，依赖读者既有知识。"},
    {"term": "违制", "meaning": "指违反建筑等级制度；作者称理论上是大逆罪，但反问古代王朝并无能力普遍执行。", "evidence": "P016", "ambiguity": "未引具体律令条文。"},
    {"term": "破风", "meaning": "一种结构名称；作者称日本沿用中国的小结构，非日本独特发明。", "evidence": "P034", "ambiguity": "未界定“破风”的形制与中日用法差异。"},
    {"term": "源自日本法", "meaning": "作者的反讽说法，指仅凭现存数量或文献记载断定某物源自日本的论证方式。", "evidence": "P040", "ambiguity": "无。"},
    {"term": "幸运饼干", "meaning": "比喻：本地事物因怪异而被附会为海外品牌（如美式中餐的幸运饼干）。", "evidence": "P063", "ambiguity": "比喻的对应关系未逐项说明。"},
    {"term": "历史记忆", "meaning": "作者用语，指发明权最终以将事物发扬光大者之名流传的内在规律。", "evidence": "P059", "ambiguity": "作者称之为“内在规律”，未给系统证据。"},
    {"term": "半开化部落", "meaning": "作者对当时日本的贬称，用于论证其不可能先发明纸折扇。", "evidence": "P056", "ambiguity": "属贬义用语，理解时需保留其修辞色彩。"}
   ],
   "examples_and_targets": [
    "《黑神话：悟空》：提问者所问对象；正文未逐项评定游戏中的盔甲与建筑（Q001，提问对象）。",
    "元《江天楼阁图》、明、隋唐图（IMG001-IMG006 附近，P009-P013 图注）：作者用以证明歇山顶常见；图片未核验（P009-P013，证据/图片）。",
    "《清明上河图》与外链“清明上河图罕见高清全图”：作者的举证材料，正文未给出可核验清单（P014、P015，证据）。",
    "教科书与“庑殿顶最尊贵，歇山顶次之，平民只能用硬山顶”：作者反驳的规则来源（P017，反驳对象）。",
    "地方豪强口吻的独白（“节度使是我姑舅，公安局长是我祖侄……看监控坏不坏？”）：作者的拟人化修辞，用来说明违建难以禁绝（P031-P033，修辞材料/作者拟作）。",
    "“日本拿着中国的小结构到处用”：作者对“破风”来源的判断（P034）。",
    "《永乐大典》仅存4%、四库全书禁毁评语与统计（P045、P046 为引文/引述数据，来源未标注）：作者转引的材料，不属作者原创判断（P044-P046，引用）。",
    "蔡伦改进造纸术、公元62-121年、610年、大化改新645年：作者的历史年代论据，需外部核查（P049-P050）。",
    "殷墟妇好墓玉挖耳勺（IMG007 附近，P055 图注）：作者用以对比工艺水平的图片证据，未核验（P054-P055，证据/图片）。",
    "太平洋土著与水力锻锤：作者的类比材料（P057，类比）。",
    "VCD、U盘：作者举的发明权与历史记忆例子（P060、P061，例证）。",
    "“幸运饼干”、加州牛肉面：作者的比喻材料（P063、P064、P067，修辞）。"
   ],
   "conditions": [
    "论甲的范围限定：“古代中国，除了技术做不到的”（P002）。",
    "论起源的范围限定：“近代以前”（P036）、“如果一个结构原理一致的东西中国有日本也有”（P036）。",
    "结论的例外条件：“除非经济规律不奏效”（P066）。",
    "折扇论证依赖的年代条件：“即使从蔡伦改进造纸术算起”“610年以后”“645年”“中间差着近六百年”（P049-P051）。",
    "文献证据力的条件：文献里有与文献里没有的证据力不同（P047）。",
    "图片证据（IMG001-IMG008）未经核验，凡依赖图注（P009-P013、P027、P055、P064）的判断均待图像复核后确认。",
    "作者对“破风”等的判断针对“各种所谓‘破风’”，未限定具体形制样本（P034）。"
   ],
   "rhetoric_and_tone": "强烈口语与论战语气：反问密集（P006“嫌命长么？”、P009、P016、P040、P056、P062、P066），感叹句（P020“不要根据书本介绍理解世界！”、P030“没得选择！”），粗直用词（“谁疯了”“老子”“半开化部落”）。以拟人化独白模拟地方豪强口吻（P031-P033）制造讽刺效果。引用方面：P045 引一段四库全书评语、P046 为引述统计数据，二者在原文中以引号/quote 节点呈现，均未标注来源。结尾以“加州牛肉面”讥讽文献记载的原产地可信度（P067）。",
   "unresolved_questions": [
    "本篇含 8 个图片节点（IMG001-IMG008），图片内容未经核验，需人工/多模态复核；P009-P013、P027、P055、P064 等图注与图片的对应关系、图中建筑形制是否确为歇山顶、玉挖耳勺等均待图像确认。",
    "P045 的四库全书评语与 P046 的禁毁统计数字均未标注出处（说话者/文献名不明），需外部核查后方可引用。",
    "P049-P050 的年代数据（中国有纸公元62-121年、日本610年后学会造纸、大化改新645年）需外部核查。",
    "“印加”式的外部事实不涉本篇；本篇待核事实还包括：古画中“庑殿顶小卖铺”“几乎间间都是歇山顶的戏园子”的具体样本、“破风”的形制界定。",
    "提问的核心（《黑神话：悟空》盔甲与建筑是否日式）正文只在开头以“关于盔甲”数段回应，未直接评定游戏本身，属答非所全问或另有取舍，正文未说明。",
    "P015 处为外链标题“清明上河图罕见高清全图（超清大图一亿像素以上）”，lexical 未覆盖该片段（skeleton divergence=true），正文与结构存在不一致。",
    "skelton 标 divergence=true，除 P015 外是否还有其他正文/结构不一致处，需按 out 记录中的 text_lexical_divergence 复核。",
    "版本：published 2020-11-05，updated 2026-05-22（时间戳带毫秒），版本差异未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "古代中国，除了技术做不到的，任何形式的有可取之处的盔甲都可能有。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "包括“日式盔甲”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这是拍电影、画得胜图为了让你好分清人的需要，根本不是现实。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "真打起来，什么甲好，就是什么甲。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "总是会打成“你中有我，我中有你”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "谁疯了在保命的家伙上讲“民族主义”？嫌命长么？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "说“建筑都是歇山顶显然违背常识和规定”的，其实并不见得如此。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "事实上中国建筑的样式丰富灵活得很。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "自己看看《清明上河图》，数一数有多少歇山顶建筑，看看是不是个个都是宫殿、道观吧。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "它们还这么容易亡吗？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "不要根据教科书上写了句“庑殿顶最尊贵，歇山顶次之，平民只能用硬山顶”，就以为世界是按照这个规则来的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "你多翻点古画，“庑殿顶”小卖铺都多的是。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "各种所谓“破风”，甚至“拱顶”“罗马穹顶”也不是什么稀罕物。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "不要根据书本介绍理解世界！", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "最怕就是湿脚。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "因为歇山顶几乎是小型建筑想做整圈屋檐保护所有柱脚不受雨水侵蚀的唯一的选择。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "但做到两层高，用硬山是怎么也护不住柱脚的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "而只有三五开间的小房子做庑殿顶，做出来效果简直好笑", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "几乎肯定要做歇山顶，不然能咋办？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "这也是为什么宫观建筑、城楼这些几乎必是歇山顶。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P034", "quote": "日本拿着中国的小结构到处用罢了，谈不上“日本的独特发明”。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P035", "quote": "有了也不成其为任何意义上的“日本风”。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P036", "quote": "起源地是日本的可能性基本是零——无论日本现存多少数量。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P037", "quote": "因为古代日本对中国的文化影响基本是0。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P038", "quote": "在唐宋明甚至清面前没有任何可以特别教授的东西", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P038", "quote": "谁去学？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P040", "quote": "晚清以前中国没有任何东西是反过来师从日本的，怎么个源自日本法？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P041", "quote": "这不是民族自尊心问题，而是一个逻辑问题。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P043", "quote": "这依据是什么呢？主要是文献资料。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P044", "quote": "然而《永乐大典》何在呢？仅存4%。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P045", "quote": "铲毁凿仆之殆遍，摧残文献，皆振古所绝无。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P046", "quote": "据不完全统计，在近20年时间里，全毁书2400多种", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P047", "quote": "你说我们文献里没什么于是证明我们没什么，这只不过间接论证而已。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P048", "quote": "不足以为全信。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P049", "quote": "中国有纸也是公元62-121年间事。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P050", "quote": "日本人从朝鲜人手里学会造纸却是610年以后的事。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P051", "quote": "中间差着近六百年。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P053", "quote": "一个国家，没有文字，根本无法传承太复杂的工艺经验。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P056", "quote": "由一群没文字、住窝棚、缺少金属工具、缺少大型城市的半开化部落发明了纸折扇，返销给我们。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P057", "quote": "结果五十年后他们先于世界发明了水力锻锤。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P058", "quote": "但是实际上需要大量的前提知识。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P059", "quote": "这东西真正的被人所知，反而是以将它发扬光大的人的名字为准。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P060", "quote": "举个例子——VCD是中国企业开发的，但是现在有谁不查资料会这样猜想呢？", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P062", "quote": "形成的历史记忆会是中国发明了VCD吗？", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P063", "quote": "我更怀疑“日本纸折扇”是一种“幸运饼干”式的发明。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P066", "quote": "除非经济规律不奏效，否则我看不出任何纸折扇真的是源自日本的现实性。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P067", "quote": "还以为加州牛肉面真的“原产加州”。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P010", "quote": "主副楼都是歇山顶。", "relation": "context"},
    {"key": "E49", "paragraph_id": "P002", "quote": "任何形式的有可取之处的盔甲都可能有", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["古代军事装备史", "中国古代建筑史", "工艺与发明史", "文化传播与影响"],
   "issue_candidates": ["《黑神话：悟空》建筑与盔甲是否日式", "歇山顶是否高贵/违制", "“破风”是否日本独特发明", "纸折扇的发明权", "文献证据的证明力"],
   "text_function_candidates": ["答疑（回应知乎提问）", "论辩与反驳", "科普/经验分享"],
   "object_candidates": ["《黑神话：悟空》", "唐军/西夏军/明军/清军", "中国", "日本", "《清明上河图》", "《永乐大典》", "四库全书", "蔡伦", "殷墟妇好墓", "VCD", "U盘", "加州牛肉面", "知乎用户@艺萃"],
   "working_keywords": ["日式盔甲", "歇山顶", "庑殿顶", "硬山顶", "柱脚", "破风", "违制", "清明上河图", "永乐大典", "四库全书", "纸折扇", "遣华使", "大化改新", "水力锻锤", "幸运饼干", "历史记忆"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含 8 个图片节点（IMG001-IMG008，均为 asset.sooon.ai 图片），子代理无读图能力，图片内容未经核验，需图像核验；已读部分为正文文本。因图片未核验，本篇 full_text_checked=false、status=needs_reread（按系统提示词第 5 节“图片文章还要求 image_checked=true 才可 full_text_checked=true”的保守解释）。P009/P011/P013/P027/P055/P064 为图注或图片说明（其中 P055“玉挖耳勺”对应妇好墓出土物图），P015 为外链标题且 lexical 未覆盖该片段（skeleton divergence=true），均未作为作者主张采信。P045 全段为四库全书评语引文、P046 为 quote 字段的禁毁统计数字，二者均未标注出处，未归给作者原创判断。P031-P033 为拟人化独白（地方豪强口吻），属修辞材料。提问的核心问题（游戏盔甲与建筑是否日式）只在开头以“关于盔甲”数段回应，未逐项评定游戏本身。"
 },
 "9b65ddf4": {
  "analysis": {
   "question_context": "提问者问“什么样是稳重，怎么样做到稳重？”。作者先以“十动然拒”点题，给出稳重的定义（顶得住各种正负“感动”、不轻易点头；检查可行性有系统方法、做取舍有稳定原则），再列出三条特征（不轻易发泄沮丧、不轻易用全称判断、对原则问题敏感），以黑羊笑话示范保守判断，最后说明稳重者需要一个超越赚钱的理由，并描述“只要赚钱什么都可以”者的结局。全篇以第二人称对提问者作训诫式建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "点题并定义：稳重是顶得住“这很赚钱”“这很有前途”“这很危险”“这没搞头”等正负“感动”而不轻易点头，且检查可行性有系统方法、取舍有稳定原则。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "两条内涵：知做事艰难故不轻易开启新事端、不轻易抛弃现有道路；知是非对错界限故不轻易玩投机获利的把戏。有此品质者做事稳定、合作易有始有终，令人心安。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "两个显著特征：不轻易发泄沮丧情绪（否则外人会觉察你预期失败）；不轻易用全称判断（判断力好的第一特征是判断足够保守）。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015"], "summary": "黑羊笑话：A 说本地羊是黑色、B 说本地羊有一只是黑色、C 限定为“此时此地这只羊型动物朝我们这一面处于黑色状态”；反问谁稳重，要求养成此习惯，如此不易“十动”也用不着“然拒”。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018"], "summary": "第三个特征：对原则问题敏感；“只要赚钱什么都可以”一出口就与稳重感告别，没人还会觉得你稳重（以反问说明合作者的顾虑）。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020"], "summary": "稳重者必有超越赚钱的理由来决定什么钱不赚，人生才有延续性、积累才成为资产；反例：只要赚钱什么都可以者大多折腾死，侥幸得第一桶金者也终成黄粱一梦。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓稳重，就是能够顶得住“这很赚钱”“这很有前途”“这很危险”“这没搞头”等等正面或负面的“感动”，不轻易点头。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "稳重也指检查可行性的时候存在一个系统的方法，做取舍的时候有一个稳定的原则。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "稳重含两条：一是知道做事的艰难、成事的不易，故不轻易开启新的事端、不轻易抛弃现有的道路；二是知道是非、对错的界限，不轻易玩投机获利的把戏。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人本能地知道有这两条品质的人做事稳定、合作容易有始有终，所以在这样的人面前容易心安。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "特征一：不轻易发泄沮丧情绪；既然预先知道艰难就应对艰难有心理预期，动辄发泄会让外人觉察你预期失败，也就意味着没达到第一条。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "特征二：不轻易用全称判断；有好的判断力的第一个特征，就是作判断时足够保守。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以三人见黑羊的笑话反问“看出谁是稳重的了吗？”，暗示 C 那种严格限定的说法代表稳重所需的保守判断。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要养成这样的习惯，才有可能拥有某种程度的稳重；到那时根本不容易“十动”，也用不着“然拒”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "特征三：对原则问题很敏感，而不是这也“可以”、那也“可以”、“只要赚钱都可以”。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要说出“只要赚钱什么都可以”这句“魔咒”，就可以和“稳重感”说再见了；没人还会觉得你稳重，因为每天出现“看起来更赚钱”的事很多，这样的价值观会让合作者担心自己惨死（末句为反问）。", "evidence": ["E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "稳重的人势必有一个赚钱之外（超越赚钱）的理由来决定什么钱不赚，这样人生才有基本的延续性，早期积累才会不断成为后面的资产，从而更有机会积累出真正扎实的硬资产，有一个常青的、抗风险的事业。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要赚钱什么都可以的人，大部分首先就折腾死了，根本没有“赚到钱”；某些侥幸搞到第一桶金的，将来也会把积累撒到各种“更赚钱”的冒险上，只不过黄粱一梦。", "evidence": ["E18"]}
   ],
   "argument_steps": [
    "以“十动然拒”点题：稳重即不轻易被正负“感动”推动。",
    "给出定义：检查可行性有系统方法、做取舍有稳定原则。",
    "展开两条内涵：知艰难而不轻启新事端/不轻易抛弃现有道路；知是非界限而不玩投机获利。",
    "给出合作效果：有这两条品质者做事稳定、有始有终，令人心安。",
    "列出特征一：不轻易发泄沮丧情绪，并说明理由（外人会看出你预期失败）。",
    "列出特征二：不轻易用全称判断，判断力好的第一特征是保守。",
    "以黑羊笑话示范三种判断的保守程度，反问谁稳重。",
    "要求养成此习惯，并说明结果（不易“十动”、用不着“然拒”）。",
    "列出特征三：对原则问题敏感；以“只要赚钱什么都可以”为反例说明后果。",
    "结论：稳重者必有超越赚钱的理由来决定不赚什么钱，从而有延续性与抗风险的事业；反例者终成黄粱一梦。"
   ],
   "concept_usage": [
    {"term": "稳重", "meaning": "顶得住正负“感动”而不轻易点头；有系统方法与稳定原则；并表现为不轻易发泄沮丧、不轻易用全称判断、对原则问题敏感。", "evidence": "P002", "ambiguity": "三项特征与两条内涵之间的对应关系未明确整理。"},
    {"term": "十动然拒", "meaning": "网络梗，作者用作题眼与结尾呼应；在文中转义为“不容易被感动，也就不用拒绝”。", "evidence": "P001", "ambiguity": "原梗的戏谑色彩与作者正面用法之间的张力未说明。"},
    {"term": "感动", "meaning": "加引号，指正面的诱惑与负面的威胁等一切能推动人点头的东西。", "evidence": "P002", "ambiguity": "未给出边界。"},
    {"term": "全称判断", "meaning": "逻辑用语，指对全体对象下断言；作者主张作判断时要保守，避免全称化。", "evidence": "P008", "ambiguity": "未讨论何种场合可用全称判断。"},
    {"term": "原则问题", "meaning": "与“只要赚钱都可以”相对的价值底线。", "evidence": "P016", "ambiguity": "未列举具体原则。"},
    {"term": "超越赚钱的理由", "meaning": "决定什么钱不赚的价值依据，作者视为稳重者具备的条件。", "evidence": "P019", "ambiguity": "具体所指未举例。"},
    {"term": "常青的、抗风险的事业", "meaning": "长期积累硬资产的结果。", "evidence": "P019", "ambiguity": "无量化标准。"}
   ],
   "examples_and_targets": [
    "“这很赚钱”“这很有前途”“这很危险”“这没搞头”：作者列举的正面与负面“感动”（P002，示例）。",
    "黑羊笑话（A/B/C 三人）：作者借用的笑话，用以示范保守判断（P009-P012，例证）。",
    "“只要赚钱什么都可以”：作者反驳与告诫的对象（P016-P020，反驳对象）。",
    "提问者的问题（什么样是稳重、怎样做到稳重）：本文回应对象（Q001）。",
    "本篇未引用具名人物、机构或历史事件。"
   ],
   "conditions": [
    "合作效果有条件：“如果有所合作，容易有始有终”（P005）。",
    "特征一依赖前提：“你预先就知道有多难，你应该对艰难有心理预期”（P007）。",
    "负面后果为条件式：“只要说出‘只要赚钱什么都可以’这句‘魔咒’，你就可以和‘稳重感’说再见了”（P017）。",
    "概称限定：“大部分首先就折腾死了”“某些侥幸搞到第一桶金的”（P020）。",
    "程度限定：“你才有可能拥有某种程度的稳重”（P014）。",
    "结尾反问“我跟你合作我岂不是要惨死？”（P018）为修辞性后果陈述，非事实断言。"
   ],
   "rhetoric_and_tone": "口语化与调侃并用（“十动然拒”“魔咒”“惨死”“撒胡椒面”“黄粱一梦”）；以笑话（黑羊）作例证；连续反问（P013“看出谁是稳重的了吗？”、P018）；第二人称训诫与鼓励交替；文末以“只要赚钱什么都可以”者的结局作警告式收束。",
   "unresolved_questions": [
    "提问分两问，正文偏重“什么样是稳重”；“怎么样做到稳重”只给出“养成这样的习惯”“对原则问题敏感”，未给可操作的步骤。",
    "黑羊笑话中作者未明说谁是稳重的，仅以反问“看出谁是稳重的了吗？”提示为 C；该归属属暗示而非明言。",
    "P005“人本能的知道”的主体为泛称，作者未给依据，属不可核查的经验断言。",
    "P019“超越赚钱的理由”具体所指（信仰、道德、志业等）正文未举例。",
    "三条特征与 P004 的两条内涵是否穷尽“稳重”，正文未作说明。",
    "版本：published 2020-11-06，updated 2026-04-26（时间戳带毫秒）；本篇以当前版本为准，无法从本记录判断版本差异。",
    "无图片，正文与 lexical 一致（仅 paragraph 节点）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "所谓稳重，就是能够顶得住“这很赚钱”“这很有前途”“这很危险”“这没搞头”等等等等种种正面或者负面的“感动”，不轻易点头。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "是指检查可行性的时候存在一个系统的方法，做取舍的时候有一个稳定的原则。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "因此不轻易的开启新的事端、不轻易抛弃现有的道路", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "第二条，是指你知道是非、对错的界限，不轻易玩投机获利的把戏。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "人本能的知道有这两条品质的人做事稳定，如果有所合作，容易有始有终，所以在这样的人面前容易心安。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "第一，是不轻易发泄沮丧情绪。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "动辄发泄沮丧情绪，外人就会觉察到你预期失败了，也就意味着你没有达到第一条。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "第二，是不轻易用全称判断。有好的判断力的第一个特征，就是作判断时足够保守。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "是此时、此地、有一只羊型的动物、朝着我们的这一面、处于黑色的状态。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "看出谁是稳重的了吗？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "你要养成这样的习惯，你才有可能拥有某种程度的稳重。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "你根本不容易“十动”，你也用不着啥“然拒”了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "第三，对原则问题很敏感，而不是这也“可以”，那也“可以”，“只要赚钱都可以”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "只要说出“只要赚钱什么都可以”这句“魔咒”，你就可以和“稳重感”说再见了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "没人还会觉得你稳重。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "稳重的人势必有一个赚钱之外的理由——超越赚钱的理由——来决定什么钱ta不赚。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "从而更有机会积累出真正扎实的硬资产，有一个常青的、抗风险的事业。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "只要赚钱什么都可以的人，大部分首先就折腾死了，根本没有“赚到钱”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["个人品质与决策方法", "商业与职业伦理", "人生修养"],
   "issue_candidates": ["稳重的定义与养成", "全称判断与保守判断", "赚钱之外的原则"],
   "text_function_candidates": ["答疑（回应知乎提问）", "经验总结", "训诫"],
   "object_candidates": ["提问者", "作者（“我”）", "黑羊笑话中的 A/B/C", "“只要赚钱什么都可以”的人"],
   "working_keywords": ["稳重", "十动然拒", "感动", "系统的方法", "稳定的原则", "全称判断", "黑羊", "原则问题", "硬资产", "抗风险", "黄粱一梦"]
  },
  "notes": "无图片，正文 20 段全部读完，正文与 lexical 一致（仅 paragraph 节点）。brief 与正文前段重合且被截断（止于“第一条，是指你知道做事的艰难，成事的不易，因此不轻易的开启新的事”），仅作导航。黑羊笑话中“谁稳重”由反问暗示为 C，未明言，故该条标 modality=questioned。全篇无引文、无外部事实断言，提问者立场未被归给作者。"
 },
 "68434efd": {
  "analysis": {
   "question_context": "提问者问“轮子的发明在文明史上有何意义？”。作者的回答是否定式：轮子的意义被高估了，真正“高科技”的是路；轮子易被想到，但在没有可用道路的地貌上使用体验极差，故印加人与古日本未能发展出轮车；能跑马车的路与平原才是难得条件，而修路所需的规划、组织与养护远超造车。全篇以第二人称“你们”讲解并多处使用图片与类比。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "立论：轮子的意义被高估；真正“高科技”的是路；轮子随时可能被人想到（果子或蛋滚下坡）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009", "P010"], "summary": "说明轮子早期的使用体验：地不平、只能人力拉推、原始样态如老式板车；地势不平则结论是不省力（可亲自拉板车验证）；车加上载重总重更大，认为更省力是愚蠢。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012"], "summary": "印加人没发明轮子：其生在山地（类比云南、贵州山区），而非苏美尔人那样一平如镜的两河流域。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "以道路图片与最低工程量原理解释：大地图上直路必有高架隧道否则起伏；高速公路因高架而平直故能高速；印加古道与茶马古道图；结论为印加人没有可供轮子行的天然的路，所以未能发明轮子。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027"], "summary": "古日本例：车轮技术极不发达，用速度慢、运营范围小的牛车，无高速马车；出门坐轿子（“越野交通”）、送货靠扁担，路是人行道（附图日本中山道）。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "结论性判断：崎岖地貌上的文明里发明轮子的“天才”只换来投资人的臭骂；发明不了轮子不是因为轮子高科技，而是没有路；能让载重马车不散架的路才是高科技，能跑战车的平原是天赐。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034"], "summary": "硬轮子在自然路面上颠簸危险（苏东坡名“轼”的掌故）；只有非常平的平原才能发展战车术，这也是“御术”成为君子六艺之一的原因；其难度类似越野障碍赛与场地房车赛之别。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "提出轮子被接受的条件（社会愿意修专用道路并有组织度与富裕程度养护）；造轮子看着都会，但规划建设好路大部分人凭直觉做不到（含受过中学教育的现代普通人）；造路难度与成本远超造车，古代亦如此，否则买车的后悔也是白瞎。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P042", "P043"], "summary": "以图注“亡命天涯之路”与“如果没有手机基站，怎么发明手机呢？”的类比收尾。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "轮子这东西的意义被高估了。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正“高科技”的根本不是轮子，而是路。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "轮子其实随时有可能被人发明——看到一个果子或者蛋滚下坡就很容易想到。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "轮子刚发明时在地不平的前提下使用体验很差：一开始不能指望坐马车，只能人力拉车或推车，原始试验品只可能是老式板车的样子。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果发明者生在地不够平的地方，得出的结论就是这东西不省力（作者建议亲自拉板车验证）；在那种地面上认为木轮车更省力是愚蠢的，因为车加上载重后总重更大。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "印加人没发明轮子，因为他们生在山地上（类似云南、贵州山区），而没有生在苏美尔人那样一平如镜的两河流域。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "凡是在大地图上看起来比较直的路，要么自带高架桥和隧道（类似高铁），否则基本上肯定是上下起伏的——因为它们是按照最低工程量原则修建的。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "高速公路有高架桥技术就会平直得多，这也是它能高速的原因之一（更短，并通过拉平高差利于车辆发挥性能）。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "印加人没有可以供轮子行的天然的路，所以没能发明轮子。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古日本车轮技术极不发达：主要用速度极慢、“运营范围”很小的牛车，没有发明高速马车；出门一般坐轿子（作者戏称为一种越野交通），送货靠扁担，路是人行道。", "evidence": ["E15", "E16", "E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在不幸生在崎岖地貌上的文明里，每一个偶然发明了轮子的“天才”，测试的结果都是投资人的臭骂；因此这些文明发明不了轮子，不是因为轮子“高科技”，而是因为没有路。", "evidence": ["E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能让载重马车跑起来不散架不翻车的路才是高科技；能让两轮战车飞驰而不会突然一轮腾空车仰马翻的平原，这就是天赐。", "evidence": ["E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "硬轮子在自然路面上跑动极不平稳危险：马就算小跑也非得牢牢抓住围栏扶手（故苏东坡名“轼”）；若飞奔起来一侧轮子轧中半埋的石块，人会立刻失去意识。", "evidence": ["E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有非常平的平原才有条件发展出战车术，这也是“御术”足以成为君子六艺之一的原因；真正的御术是在坡度变化、随时有石块土包坑洼的自然地面上高速避开翻车陷阱，所需观察力、判断力、反应力和执行力非同小可。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "御术的难度约等于场地房车赛和越野障碍赛的区别：前者新手无非慢点，后者新手搞不好直接翻山下去。", "evidence": ["E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "轮子真正被接受的条件是：人类社会能够而且愿意为行车要求修建专用道路，并且有足够的组织度和富裕程度维持道路养护；而这更多是社会科学、工程技术、几何学、测绘学的发展，而不仅仅是手工制造。", "evidence": ["E28", "E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "造轮子看着都会（大不了不圆），但规划和建设一条好路（坡度合理、距离最短、工程量最小、自持力最强即易维护）大部分人凭直觉做不到，绝大部分受过中学教育的现代普通人都做不到。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "造这路的难度远远高于造轮子和马车；要付出的劳动量和成本也远远超出造一批木质车辆。", "evidence": ["E33"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述大部分要求不是现代才有的特殊高标准：即使在古代，道路的设计、建造和维护不达标，路隔三差五一样要断行。", "evidence": ["E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "否则到时候买车的人个个都要后悔，也是白瞎。", "evidence": ["E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问作类比收尾：如果没有手机基站，怎么发明手机呢？", "evidence": ["E36"]}
   ],
   "argument_steps": [
    "先否定通行看法：轮子的意义被高估。",
    "提出替代判断：真正“高科技”的是路。",
    "说明轮子易被想到（果子、蛋滚下坡）。",
    "描述轮子早期的糟糕体验：地不平、只能人力拉推、形态原始。",
    "以“亲自拉板车”为验证方法，说明不平地面上轮车不省力（总重增加）。",
    "举印加：生在山地，非两河流域平原，故未发明轮子。",
    "以道路图与最低工程量原则说明道路的起伏与修建逻辑；高速公路因高架而平直。",
    "归纳：印加人没有可走轮子的天然道路，所以没有轮子。",
    "举古日本：牛车慢、坐轿子、送货靠扁担、路是人行道。",
    "推广判断：崎岖地貌的文明发明不了轮子不是因轮子高科技，而是没有路。",
    "提出正面标准：能跑载重马车的路才是高科技，能跑战车的平原是天赐。",
    "说明硬轮子的危险与御术之难，并指出战车术需极平的平原。",
    "提出轮子被接受的社会条件（修路意愿、组织度、富裕程度与养护）。",
    "对比难度：造轮子易、修好路难，连现代普通人也做不到；古代标准同样不低。",
    "以“没有手机基站怎么发明手机”类比收尾，图注为“亡命天涯之路”。"
   ],
   "concept_usage": [
    {"term": "轮子", "meaning": "作者认为技术含量被高估、易被想到的发明；其价值取决于是否存在可行驶的道路。", "evidence": "P001", "ambiguity": "未区分轮子作为原理与作为实用轮车的差别。"},
    {"term": "路", "meaning": "作者称为真正的高科技，需满足坡度合理、距离最短、工程量最小、自持力最强、易维护等要求。", "evidence": "P037", "ambiguity": "未给出具体技术标准或历史案例细节。"},
    {"term": "高科技", "meaning": "加引号，指真正困难、需要大量前提条件的技术成就。", "evidence": "P002", "ambiguity": "属通俗用法，非严格技术定义。"},
    {"term": "最低工程量原则", "meaning": "作者用以解释大地图上道路多起伏的原因：修路按工程量最小来选线。", "evidence": "P014", "ambiguity": "未说明该原则的适用范围与例外。"},
    {"term": "自持力", "meaning": "作者定义为抗风雨、不容易塌方、不容易被风沙掩埋，即易维护。", "evidence": "P037", "ambiguity": "非通用工程术语，为作者自用表述。"},
    {"term": "御术", "meaning": "君子六艺之一；作者定义为在自然地面上高速行进并敏感避开翻车陷阱的驾驶技术。", "evidence": "P033", "ambiguity": "未引古代文献佐证其定义。"},
    {"term": "越野交通", "meaning": "作者对轿子的戏称（用英文 which is a kind of 连接）。", "evidence": "P024", "ambiguity": "戏谑用法。"},
    {"term": "身份证", "meaning": "比喻轮子被社会正式接受（有专用道路与养护）。", "evidence": "P035", "ambiguity": "比喻，无制度含义。"}
   ],
   "examples_and_targets": [
    "印加人与印加古道（IMG001-IMG005 附近的图）：作者的核心例证，用来说明无路则无轮车；图片未核验（P011-P021，例证/图片）。",
    "苏美尔人与两河流域：作者用作“一平如镜”平原的对照（P012，例证）。",
    "云南、贵州山区：作者用以类比印加山地（P012，类比）。",
    "高速公路与高架桥：作者的现代例证（P016，例证）。",
    "茶马古道（IMG 图注 P020）：作者用以与印加古道对照；图片未核验（P019-P020，例证/图片）。",
    "古日本与日本中山道（IMG 图注 P027）：作者的第二组例证；图片未核验（P022-P027，例证/图片）。",
    "牛车、轿子、扁担：作者对古日本交通方式的描述（P023-P025，例证）。",
    "苏东坡与“轼”：作者的词源掌故，用来说明乘车须抓扶手（P032，修辞/待核事实）。",
    "君子六艺与御术：作者的论据（P033，例证）。",
    "场地房车赛与越野障碍赛：作者的类比材料（P034，类比）。",
    "“亡命天涯之路”（IMG 图注 P042）：图注，与正文关系未说明；图片未核验（P042，图片）。",
    "手机基站与手机：作者的类比材料（P043，类比）。",
    "提问者的问题“轮子的发明在文明史上有何意义？”：本文回应对象（Q001）。"
   ],
   "conditions": [
    "讨论使用体验的前提：“在地不平的前提下”（P004）。",
    "条件句：“如果ta非常不幸的生在地不够平的地方”（P008）、“如果飞奔起来”（P032）。",
    "必要条件式表述：“只有非常平的平原才有这个条件发展出战车术”（P033）。",
    "轮子被接受的条件：“人类社会能够而且愿意为行车的要求而修建专用道路、而且也有足够的组织度和富裕程度能维持道路的养护”（P035）。",
    "概称限定：“绝大部分受过中学教育的现代普通人都做不到”（P038）、“每一个偶然发明了轮子的‘天才’”（P028）。",
    "图片（IMG001-IMG011）未经核验：凡依赖图注（P013、P015、P017、P019、P020、P027、P042）的判断均待图像复核。"
   ],
   "rhetoric_and_tone": "面向“你们”的讲解与挑战口吻；反问（P004“使用体验是啥样的？”、P008、P043）；夸张与调侃（“只有脑子有水的人”“投资人的臭骂”“亡命天涯之路”）；类比（手机基站与手机、场地房车赛与越野障碍赛）；带掌故性的插话（苏“轼”）；混合使用“ta们”“which is a kind of”等网络化书写。",
   "unresolved_questions": [
    "本篇含 11 个图片节点（IMG001-IMG011），内容未经核验，需人工/多模态复核；印加古道、茶马古道、日本中山道等图与图注的对应关系不能确认。",
    "事实待外部核查：印加人是否“没有发明轮子”（学界对印加是否有轮式玩具/实用轮车存在讨论）、苏东坡名“轼”与车前扶手的关联、古日本“主要用牛车”与“没有发明高速马车”的表述、印加古道与两河流域地貌的描述。",
    "P003“轮子其实随时有可能被人发明”为作者判断，未给系统证据（仅举果子、蛋滚下坡的联想）。",
    "P014“最低工程量原则”未给来源，属作者概括。",
    "P042 图注“亡命天涯之路”与上下文的对应关系未说明（疑为配图说明）。",
    "正文含若干图片替代段落，图片内容可能承担部分论证；正文与 lexical 计数（paragraph 55、image 11）不一致处需按 out 记录复核。",
    "版本：published 2020-11-06，updated 2026-03-26（时间戳带毫秒）；本篇以当前版本为准，无法从本记录判断版本差异。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "轮子这东西的意义被高估了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因为真正“高科技”的，根本就不是轮子，而是路啊。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "轮子其实随时有可能被人发明——看到一个果子或者蛋滚下坡就很容易想到。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "一开始你显然不能指望坐马车", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "当然是人力拉车或者推车。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这原始试验品只可能是老式板车那个样", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "如果ta非常不幸的生在地不够平的地方，ta得出的结论会是啥？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "只有脑子有水的人在这种地面上推木轮车会觉得“这东西更省力”。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "我推的可不止100斤——车还有几百斤啊！", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "所以印加人没发明轮子。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "ta们非常不幸，没有生在类似苏美尔人那样的一平如镜的两河流域", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "凡是在大地图上看起来比较直的路，要么它就是自带高架桥和隧道，类似高铁，否则基本上肯定是上下起伏的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "这也是它为什么能高速的原因之一", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "印加人没有可以供轮子行的天然的路，所以没能发明轮子。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "实际上，车轮技术极不发达的还有古日本。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "古日本主要用速度极慢、“运营范围”很小的牛车，根本没有发明高速马车。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P024", "quote": "ta们出门一般坐轿子——which is a kind of 越野交通。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "对应的，ta们的路一样是人行道。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "每一个偶然发明了轮子的“天才”，测试的结果都是投资人的臭骂。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "因此ta们发明不了轮子，不是因为轮子“高科技”，而是因为ta们没有路。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P030", "quote": "能让载重马车跑起来不散架不翻车的路，才是高科技。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P031", "quote": "能让两轮战车飞驰起来不会突然一轮腾空车仰马翻的平原，这就是天赐了。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P032", "quote": "所以苏东坡才叫苏“轼”。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P033", "quote": "只有非常平的平原才有这个条件发展出战车术。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P033", "quote": "这也是为什么“御术”足以成为君子六艺之一。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P033", "quote": "需要的观察力、判断力、反应力和执行力实在非同小可。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P034", "quote": "这约等于场地房车赛和越野障碍赛的区别。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "人类社会能够而且愿意为行车的要求而修建专用道路、而且也有足够的组织度和富裕程度能维持道路的养护了，轮子才算是真的获得了“身份证”了。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P035", "quote": "而这更多的是社会科学、工程技术、几何学、测绘学的发展，而不仅仅是手工制造。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P036", "quote": "让你们造轮子，你们看着都会，大不了不圆罢了。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P037", "quote": "坡度合理、距离最短、工程量最小、自持力最强", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P038", "quote": "绝大部分受过中学教育的现代普通人都做不到。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P039", "quote": "造这路的难度远远的高于造轮子和马车。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P040", "quote": "即使是在古代，道路的设计、建造和维护不达标，这路隔三差五一样要断行", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P041", "quote": "到时候买车的人个个都要后悔，也是白瞎。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P043", "quote": "其实这道理也很简单——如果没有手机基站，怎么发明手机呢？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["技术史与文明史", "交通与道路工程", "地理环境与文明差异"],
   "issue_candidates": ["轮子发明的文明史意义", "路与轮子的技术难度比较", "印加与古日本为何没有轮车", "道路养护与社会组织度"],
   "text_function_candidates": ["答疑（回应知乎提问）", "论辩与反驳（反驳“轮子意义重大”的通行看法）", "科普讲解"],
   "object_candidates": ["印加人", "苏美尔人", "古日本", "苏东坡", "云南/贵州山区", "两河流域", "印加古道", "茶马古道", "日本中山道"],
   "working_keywords": ["轮子", "路", "高科技", "最低工程量原则", "印加古道", "板车", "牛车", "轿子", "扁担", "御术", "君子六艺", "自持力", "高架桥", "手机基站"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含 11 个图片节点（IMG001-IMG011，均为 asset.sooon.ai 图片），子代理无读图能力，图片内容未经核验，需图像核验；已读部分为正文文本。因图片未核验，本篇 full_text_checked=false、status=needs_reread（按系统提示词第 5 节“图片文章还要求 image_checked=true 才可 full_text_checked=true”的保守解释）。P013/P015/P017/P019/P020/P027/P042 为图片相关段落（图注或引导句），其中 P042“亡命天涯之路”与上下文关系未说明，均未作为作者主张采信。P014“最低工程量原则”、P032 苏“轼”掌故、P012 地貌描述、P023 古日本牛车等属需外部核查的事实性表述。"
 },
 "005096aa": {
  "analysis": {
   "question_context": "提问者问如何看待中国武术协会“习武之人不能以门派、拳种名义参加格斗搏击”的倡议。作者认同该倡议，理由是本就不存在有权授权的“xxx派最高委员会”，所谓“代表某门派、某拳种”本就荒谬；随后转入个人主张：更喜欢套路赛，认为套路是中国武学的正路，搏斗术应由军队警察研究传授；最后以“力”与“美”的对举说明武术的价值在于美与背后的哲学。提问者的提问未包含立场，正文亦未复述倡议原文。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "评价倡议：本就不存在“xxx派最高委员会”来做授权，何来“代表某门派、某拳种”；以“谁自告奋勇代表华人参赛算谁的”反问，认为倡议只是把这种荒谬打住了。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "作者个人偏好套路赛：其力与美、自我控制力与身体运动能力、精神力远超过所谓“能打”；作者不在意“能不能打”；习武为强心，强身次要。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "判断“武术套路”才是中国武学的正路，搏斗术应由军队警察研究传授；以反问“能打伤人的技术多的是，有这么美的还有谁”支撑。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010"], "summary": "引用2019年全国武术套路锦标赛女子太极拳视频标题与链接作为正面例证（quote 字段，非作者文字）。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "回应“要美去练健美操”之说：作者称无意贬低健美操，但美不仅是动作，还有背后的哲学；中国武术是用身体挥洒的哲学。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015"], "summary": "引用另一段视频标题（耍棍技术），说明体会不到哲学就学不好武术，会学成那种样子，“完全是两回事”。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "以“人类灭绝后外星文明检视遗产”的假设推证：被记住的会是“人类还能做出这种动作”而非“这招威力好大”；力是现世甚至只属于青春，美是永恒的；反问哪一文化的体术能比美。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021"], "summary": "收束对举：美而不力不过是缺憾（且以力伤敌的时代已过去）；力而不美，到底是空。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "武协倡议本来就是这么回事：本就不存在什么“xxx派最高委员会”来做授权，因此谈不上“代表某门派、某拳种”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问指出代表资格的荒谬：明天不知谁自告奋勇“代表华人”去参加某比赛，这算谁的？", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这本来就很荒谬，倡议只是把这种荒谬打住了。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者个人更喜欢套路赛：它所体现的力与美、人的自我控制力和身体运动能力、人的精神力，远超过所谓的“能打”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“能不能打”，至少作者不是那么在意。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "习武本来就是为了强心，强身是次要的；学到的坚毅、淡定、人生的改变、气质的沉稳、心态的健康，才是习武能带来的最大好处。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为最近备受嘲讽的“武术套路”才是中国武学的正路；搏斗术反而不是，这个应该直接由军队警察去研究和传授。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问提出真正的问题：能打伤人的技术多的是，有这么美的还有谁？", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "有人主张“要美去练健美操”（作者转述并回应的他人说法）。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者回应上述说法：无意贬低健美操，但美可不仅仅是动作，还有这背后的哲学；中国的武术，是用身体挥洒的哲学。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "体会不到这哲学就学不好武术，会学成所引视频那种样子，与真正的武术“完全是两回事”。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "以假设推证：若人类灭绝、外星文明检视人类所有遗产，他们记住的会是“人类还能做出这种动作”而非“人类这招威力好大”；他们恐怕会很奇怪前者怎么会成为一个被关注的话题。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "力是现世的，甚至只是青春的，而美是永恒的。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问提出：世上还有哪一个文化的体术能和我们比美？", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美而不力，不过是缺憾——更何况普通人需要学会以力伤敌的时代已经过去了。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "力而不美，到底是空。", "evidence": ["E21"]}
   ],
   "argument_steps": [
    "表态：倡议本来就是这么回事。",
    "给出理由：不存在有权授权的“xxx派最高委员会”，故无从“代表某门派、某拳种”。",
    "以“谁代表华人参赛算谁的”反问加强荒谬性判断。",
    "结论式评价：倡议只是把这种荒谬打住了。",
    "转入个人偏好：更喜欢套路赛，其力与美、自控力、精神力超过所谓“能打”。",
    "给出习武目的：强心为主、强身为次。",
    "判断：套路才是中国武学的正路，搏斗术应由军队警察研究传授。",
    "以“能打伤人的技术多的是，有这么美的还有谁”反问支撑。",
    "引视频标题作正面例证。",
    "回应“要美去练健美操”：先让步（无意贬低健美操），再指出美背后有哲学。",
    "定性：中国武术是用身体挥洒的哲学；并以另一段视频说明不懂哲学者会学成花哨表演。",
    "以外星文明检视人类遗产的假设论证“动作之美”比“威力”更会被记住。",
    "提出力/美的时间性对举（力现世且青春，美永恒）。",
    "反问哪一文化的体术能比美。",
    "结论：美而不力只是缺憾，力而不美到底是空。"
   ],
   "concept_usage": [
    {"term": "套路赛/武术套路", "meaning": "作者视为中国武学的正路，体现力与美、自控力与精神力；与“搏斗术”相对。", "evidence": "P007", "ambiguity": "未界定套路的技术范围与竞赛形式。"},
    {"term": "能打", "meaning": "加引号，指格斗实战能力；作者称自己并不那么在意。", "evidence": "P004", "ambiguity": "未讨论“能打”与套路训练的关系。"},
    {"term": "强心/强身", "meaning": "作者对习武目的的区分：强心为主，强身为次。", "evidence": "P006", "ambiguity": "“强心”的具体含义未界定。"},
    {"term": "用身体挥洒的哲学", "meaning": "作者对中国武术的定性表述。", "evidence": "P012", "ambiguity": "“哲学”的具体内容未展开。"},
    {"term": "体术", "meaning": "作者用于指各文化的身体技术，作为“比美”的比较单位。", "evidence": "P019", "ambiguity": "比较标准未给出。"},
    {"term": "美/力", "meaning": "全篇的核心对举：力是现世的、甚至只属于青春；美是永恒的；两者互缺后果不同。", "evidence": "P018", "ambiguity": "未给“美”的判定标准。"},
    {"term": "正路", "meaning": "作者对武术套路的定位（中国武学的正路）。", "evidence": "P007", "ambiguity": "与“搏斗术”的关系（是否完全排除）未细说。"}
   ],
   "examples_and_targets": [
    "中国武术协会的倡议：本篇评论对象（Q001、P001-P003，被评论对象）。",
    "“xxx派最高委员会”“代表某门派、某拳种”“代表华人”：作者反驳的说法（P001、P002，反驳对象）。",
    "“有人说‘要美去练健美操’”：他人说法，作者回应并部分让步（P011，被回应的他人观点）。",
    "2019年全国武术套路锦标赛女子太极拳视频（P010，quote 字段：标题+哔哩哔哩链接）：作者的正面例证材料，视频内容未观看。",
    "耍棍视频（P014，quote 字段：标题+哔哩哔哩链接）：作者的反面例证材料，视频内容未观看。",
    "军队警察：作者认为应研究传授搏斗术的主体（P008，行动建议对象）。",
    "外星文明：作者的假设性论证装置（P016-P017，修辞/假设）。",
    "六小龄童：出现在所引视频标题中（P014），非作者评价对象。"
   ],
   "conditions": [
    "个人偏好的限定语：“个人而言”“我本来就更喜欢”（P004）——C004 为作者自陈偏好，非普遍主张。",
    "让步性限定：“我无意贬低健美操”（P011）。",
    "时代条件：“普通人需要学会以力伤敌的时代已经过去了”（P020）。",
    "假设条件：“假设哪天人类灭绝了，外星文明来检视人类的所有遗产”（P016）。",
    "行动建议的适用范围：“这个应该直接由军队警察去研究和传授”（P008）。",
    "比较性反问（P019）未给比较标准，属修辞性主张。"
   ],
   "rhetoric_and_tone": "以“我”“个人而言”标明个人立场；反问密集（P001、P002、P009、P019）；对他人说法先让步再反驳（P011）；引用两段哔哩哔哩视频标题与链接作例证（P010、P014 为 quote 字段，说话者为视频标题作者/平台，非本文作者）；结尾用“美而不力……力而不美……”的对举句收束，带箴言色彩。",
   "unresolved_questions": [
    "正文未复述武协倡议原文，倡议的具体措辞与背景需回查外部（提问字段仅给出概括）。",
    "P010、P014 两条 quote 字段是视频标题+链接，标题作者不明（可能是上传者或平台），不能归给本文作者；视频内容未观看，无法核验“套路之美”与“耍棍表演”的差别。",
    "P007 原文“其实是才是中国武学的正路”有“其实是才是”重复，疑为笔误，原文如此未擅改。",
    "P016-P017 的外星文明设想属思辨假设，非可核查事实；“美是永恒的”为价值判断。",
    "P019“世上还有哪一个文化的体术能和我们比美”为反问，作者未给出比较标准与对象。",
    "P008 主张搏斗术由军队警察研究传授，但未说明与民间武术训练的关系。",
    "无图片；正文与 lexical 一致（paragraph 20、quote 2）；两条 quote 为外链，未核验其内容。",
    "版本：published 2020-11-07，updated 2025-07-08（时间戳带毫秒）；本篇以当前版本为准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "本就不存在什么“xxx派最高委员会”来做授权，何来“代表某门派、某拳种”？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "明天不知道谁自告奋勇“代表华人”去参加某比赛，这算谁的？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这本来就很荒谬，这只是把这种荒谬打住了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "个人而言，我本来就更喜欢套路赛。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "“能不能打”，至少我不是那么在意。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "习武本来就是为了强心，强身是次要的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "气质的沉稳、心态的健康，才是习武能带来的最大好处。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "我觉得最近备受嘲讽的“武术套路”其实是才是中国武学的正路。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "搏斗术反而不是——这个应该直接由军队警察去研究和传授。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "真正的问题是——能打伤人的技术多的是，有这么美的还有谁？", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "有人说“要美去练健美操”", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "但是美可不仅仅是动作，还有这背后的哲学。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "中国的武术，是用身体挥洒的哲学。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "你体会不到这哲学，你学不好武术的，会学成这样：", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "完全是两回事。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "假设哪天人类灭绝了，外星文明来检视人类的所有遗产", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "他们恐怕会很奇怪前者怎么会成为一个被关注的话题。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "力是现世的，甚至只是青春的，而美是永恒的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "世上还有哪一个文化的体术能和我们比美？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "更何况普通人需要学会以力伤敌的时代已经过去了；", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "力而不美，到底是空。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["武术与体育", "身体文化", "美学与哲学"],
   "issue_candidates": ["武协倡议“不得以门派拳种名义参加格斗搏击”", "套路与搏击之争", "习武的目的", "武术之美与哲学"],
   "text_function_candidates": ["答疑/评论（对新闻事件表态）", "论辩与反驳", "个人主张陈述"],
   "object_candidates": ["中国武术协会", "提问者", "军队警察", "健美操练习者", "六小龄童（引自视频标题）", "哔哩哔哩", "2019年全国武术套路锦标赛"],
   "working_keywords": ["玄门正宗", "门派", "拳种", "格斗搏击", "套路赛", "能打", "强心", "强身", "用身体挥洒的哲学", "力与美", "体术"]
  },
  "notes": "无图片（图片节点 0），正文 21 段全部读完，正文与 lexical 一致（paragraph 20、quote 2）。P010、P014 为 quote 字段（哔哩哔哩视频标题+链接），说话者为视频标题作者/平台，未归给本文作者，其内容亦未核验。P011“要美去练健美操”属他人说法，已标 opponent_view。P007“其实是才是”疑为笔误，原文保留未改写。提问字段未含提问者立场。"
 },
 "91a1dfc4": {
  "analysis": {
   "question_context": "提问者问：既然科学对现代文明的进步起着近乎决定性的作用，为什么还有人不相信科学、甚至反过来说“科学教”？作者不回答“为什么有人不信科学”，而是先以一连串个人生活问题（工作选择、下属忠诚、爱人是否爱你）反问科学能否回答，进而主张科学的能力只及于“共性问题”，对个人事务几乎无能为力；再把“人类文明”重新界定为亿万个体生活的总和，据此否定“科学起到近乎决定性作用”这一提问前提，最后给出替代解释：是个人在信息与能力必然不足下的赌注般决策在决定一切。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "以一连串反问质疑科学对个人事务的适用性：如何科学证明工作选择正确、可靠证明下属忠诚、科学判断ta爱不爱你；需要什么模型、控制哪些变量、设计什么实验、提取哪些数据、如何证明结论有效性。", "role": "reason"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "核心判断：科学对个人“不感兴趣”，其能力只及于“共性问题”；用科学指导公共决策或许有某种影响力，但指导个人事务几乎无能为力。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "理由：每个人都是特殊的，没有研究能告诉你是否适用于它的结论；科学院几乎无法回答个人问题，要答须先签免责条款；它不能告诉你人生选择、这个人、理想是否正确；即便理论上能答，成本你也负担不起。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015"], "summary": "以“多花一百万，能治好我的病吗？”与“这个不能保证，只能说从历史数据看有一定希望”的示例对话，标示科学在日常生活中的真正水平。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018"], "summary": "重新界定“人类文明”：其绝大部分是一个个个体人的生活，不是伟大历史人物的关键历史事件，也不是“公共政策”；后者只是引人注目、被额外记住，其分量远不如亿万斯民个人生活的总和，连千分之一都不到。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021"], "summary": "以反问否定提问前提（何来“科学起到近乎决定性的作用”），并给出替代解释：是所有的人在研究、数据、能力必然不足的前提下作出的每分每秒赌注般的决策在决定一切，过去现在将来皆然。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024"], "summary": "收束表态：“幸亏如此”；科学会有影响但永远唱不了主角；每一个无依无靠的成年人都知道这是妄想。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以连续反问提出：如何科学地证明你现在选择的这份工作是正确的、如何可靠地证明下属确实忠诚、如何科学地判断ta爱不爱你；需要设立什么模型、控制哪些变量、如何设计实验、提取哪些数据、如何证明结论的有效性。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "科学对个人“不感兴趣”；科学的能力只及于“共性问题”。", "evidence": ["E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "想要用科学指导某种社会的公共决策，或许能有某种影响力；但用来指导个人事务，科学事实上几乎无能为力。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你是如此特殊，没有任何的研究能告诉你你是否适用于它的结论。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "科学院几乎无法回答你的任何个人问题；一定要它答，那必须先签免责条款。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "科学不能告诉你你的人生选择是不是对的，不能告诉你这个人是不是对的，不能告诉你你的理想是不是对的。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "就算理论上科学可以做出更好的回答，那个成本你仍然负担不起。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“多花一百万，能治好我的病吗？”与“这个不能保证，只能说从历史数据看有一定希望。”的对话示例，说明这才是科学在人日常生活里真正的水平（该对话为作者构造的示例，未标明说话者）。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类文明的绝大部分都是一个个个体人的生活，不是伟大历史人物的关键历史事件，也不是“公共政策”；后者只是引人注目、总被额外记住，其在“人类文明”面前的分量远不如亿万斯民个人生活的总和，连千分之一都不到。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "以反问否定提问者的前提：既然文明的绝大部分是个体生活，何来“科学起到近乎决定性的作用”？", "evidence": ["E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "是所有的人在研究必然不足、数据必然不足、能力必然不足的前提下作出的每分每秒的赌注般的决策在决定一切；过去如此，现在如此，将来也只会如此。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对此表态：“幸亏如此。”", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "科学会对此有影响，但它永远唱不了主角。", "evidence": ["E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一个无依无靠的成年人都知道这是妄想。", "evidence": ["E22"]}
   ],
   "argument_steps": [
    "先设问：以工作选择、下属忠诚、爱与不爱三个个人问题反问科学能否回答。",
    "列出科学方法所需环节（模型、变量、实验、数据、有效性），暗示其在个人事务上不可行。",
    "给出核心判断：科学对个人“不感兴趣”，能力只及于“共性问题”。",
    "区分领域：指导公共决策或许有影响，指导个人事务几乎无能为力。",
    "给出理由：个体特殊，研究结论未必适用于你；科学院回答个人问题须先签免责条款。",
    "以“不能告诉你人生选择/这个人/理想是否对”排比加强，并加让步句“就算理论上可以……成本仍负担不起”。",
    "以看病对话示例标示科学在日常生活中的真实水平。",
    "重新界定“人类文明”为亿万个体生活的总和，压低历史事件与公共政策的分量。",
    "反问否定提问前提（何来“近乎决定性的作用”）。",
    "给出替代解释：个人在必然不足下的赌注般决策决定一切，且古今将来皆然。",
    "表态“幸亏如此”；科学有影响但唱不了主角；无依无靠的成年人都知道这是妄想。"
   ],
   "concept_usage": [
    {"term": "科学", "meaning": "作者将其能力限定于“共性问题”，认为对个人事务几乎无能为力，但仍承认其影响（永远唱不了主角）。", "evidence": "P007", "ambiguity": "未区分自然科学、社会科学与科普/科学主义等不同含义。"},
    {"term": "共性问题", "meaning": "加引号，作者用以界定科学能力的边界，与个人事务相对。", "evidence": "P007", "ambiguity": "未给出“共性”的判定标准。"},
    {"term": "个人事务/个人问题", "meaning": "与共性问题相对，指人生选择、人际关系、理想等；作者称科学对此无能为力。", "evidence": "P008", "ambiguity": "未讨论心理学、医学等应用学科的边缘情形。"},
    {"term": "人类文明", "meaning": "加引号；作者界定为亿万斯民个人生活的总和，而非历史事件与公共政策。", "evidence": "P017", "ambiguity": "属重新定义，未给出计量依据。"},
    {"term": "赌注般的决策", "meaning": "作者用语，指个人在研究、数据、能力必然不足前提下的每分每秒的抉择。", "evidence": "P020", "ambiguity": "比喻性表述，非决策理论术语。"},
    {"term": "免责条款", "meaning": "作者用以说明科学机构回答个人问题须先免除责任（修辞）。", "evidence": "P010", "ambiguity": "无实际制度对应。"},
    {"term": "妄想", "meaning": "指相信科学能起决定作用/能指导个人生活的想法。", "evidence": "P024", "ambiguity": "具体所指需结合 P023 理解。"}
   ],
   "examples_and_targets": [
    "“如何科学的证明你现在选择的这份工作是正确的？”等三问：作者自设的个人问题（P002-P004，示例/论证装置）。",
    "模型、变量、实验、数据、有效性：作者列举的科学方法环节（P005，论证装置）。",
    "“多花一百万，能治好我的病吗？”/“这个不能保证，只能说从历史数据看有一定希望。”：作者构造的示例对话（P013-P014，示例；未标明说话者，非真实引用）。",
    "科学院与免责条款：作者的说明性修辞（P010）。",
    "伟大的历史人物的关键历史事件、“公共政策”：作者用以对照并压低其分量的对象（P017，反驳/对照对象）。",
    "亿万斯民的个人生活：作者用以界定“人类文明”的主体（P017）。",
    "无依无靠的成年人：作者用以加强结论的泛称（P024，修辞）。",
    "提问者的问题与其前提（科学对现代文明进步起近乎决定性作用、有人不信科学、被称“科学教”）：本文的回应与反驳对象（Q001，提问者说法）。"
   ],
   "conditions": [
    "限定（P008）：用科学指导公共决策“或许能有某种影响力”，指导个人事务“事实上几乎无能为力”。",
    "让步条件（P012）：“就算理论上它可以做出更好的回答”。",
    "前提限定（P020）：个人决策是在“研究必然不足、数据必然不足、能力必然不足”的前提下作出的。",
    "条件句（P010）：“一定要它答，那必须先签免责条款”。",
    "全称概称（P024）：“每一个无依无靠的成年人”均如此——作者未给依据。",
    "时间范围（P021）：过去、现在、将来皆然（作者的预测性表述）。"
   ],
   "rhetoric_and_tone": "全篇以第二人称“你”“你们”直接对提问者发问；开篇即用连续反问句组（P002-P005），结论处以反问否定提问前提（P019）；以排比句“不能告诉你……不能告诉你……不能告诉你……”（P011）加强；虚构对话示例（P013-P014）与“唱不了主角”的比喻（P023）；短句顿收（P018“连千分之一都不到。”、P022“幸亏如此。”）。语气直接、略带讥讽与自信，未使用引文或具名数据。",
   "unresolved_questions": [
    "P013-P014 的对话未标明说话者，应为作者构造的示例性对话，已按作者示例处理，非真实引用。",
    "P018“连千分之一都不到”、P017 关于历史事件与公共政策分量的判断无数据来源，需外部核查或按修辞处理。",
    "提问包含两问：为何有人不信科学与为何被称“科学教”；作者只回应了“科学是否起决定性作用”这一前提，未直接解释“不信科学”的原因，也未解释“科学教”一词的用法。",
    "P024“每一个无依无靠的成年人都知道这是妄想”为全称断言，无依据说明；“妄想”的具体所指（信科学能起决定作用？）需结合上下文推断。",
    "P010“科学院”指何机构（中国科学院？泛指科学界？）未说明。",
    "作者对“公共政策”与“个人事务”的边界未给出判据（P008）。",
    "无图片，正文与 lexical 一致（仅 paragraph 节点）。",
    "版本：published 2020-11-08，updated 2026-06-18（时间戳带毫秒）；本篇以当前版本为准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "如何科学的证明你现在选择的这份工作是正确的？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "如何科学的判断ta爱不爱你？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "需要设立什么样的模型？控制哪些变量？如何设计实验？提取哪些数据？如何证明结论的有效性？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "你们也许没有意识到，科学对个人“不感兴趣”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "科学的能力只及于“共性问题”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "但是用来指导个人事务，科学事实上几乎无能为力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "你是如此特殊，没有任何的研究能告诉你你是否适用于它的结论。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "科学院几乎无法回答你的任何个人问题，一定要它答，那必须先签免责条款。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "它不能告诉你你的人生选择是不是对的；不能告诉你这个人是不是对的；不能告诉你你的理想是不是对的……", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "就算理论上它可以做出更好的回答，那个成本你仍然负担不起。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "“多花一百万，能治好我的病吗？”", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "“这个不能保证，只能说从历史数据看有一定希望。”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "这才是科学在人日常生活里真正的水平。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "而人类的文明的绝大部分，都是一个个个体人的生活。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "事实上它们在“人类文明”这个词面前的分量，远远不如亿万斯民的个人生活的总和。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "连千分之一都不到。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "所以，何来“科学起到近乎决定性的作用”？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "是所有的人在研究必然不足、数据必然不足、能力必然不足的前提下作出的每分每秒的赌注般的决策在决定一切。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "过去如此，现在如此，将来也只会如此。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "幸亏如此。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "科学会对此有影响，但它永远唱不了主角。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "每一个无依无靠的成年人都知道这是妄想。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["科学哲学/科学的社会角色", "日常生活与个人决策", "文明观"],
   "issue_candidates": ["科学的能力边界", "科学能否指导个人事务", "科学的决定作用是否被高估", "“科学教”的说法"],
   "text_function_candidates": ["答疑（回应知乎提问）", "论辩与反驳（反驳提问前提）", "评论"],
   "object_candidates": ["提问者", "科学院", "科学", "亿万斯民", "伟大的历史人物", "无依无靠的成年人"],
   "working_keywords": ["科学教", "共性问题", "个人事务", "科学院", "免责条款", "赌注般的决策", "人类文明", "唱不了主角"]
  },
  "notes": "无图片（图片节点 0），正文 24 段全部读完，正文与 lexical 一致（仅 paragraph 节点）。提问包含两问，作者只回应其前提（科学是否起近乎决定性的作用），未直接回答“为何有人不信科学”“何谓科学教”，该缺口已登记于 unresolved_questions。P013-P014 为作者构造的示例对话，未标明说话者，按示例处理，非真实引用；提问者前提未被归给作者，作者以反问否定之（C010）。"
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
