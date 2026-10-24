# -*- coding: utf-8 -*-
"""批次 r001-b0063 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0063.sessions.py            # 写 out/r001-b0063.out.jsonl
  python3 records/r001-b0063.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0063"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0063.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "6a726629": {
  "analysis": {
   "question_context": "知乎提问者问“通过技术的进步，人类能成为神吗？”（Q001，属提问者，不得归给作者）。作者答“当然不能”，并从神人分界的绝对性、神与人在伦理体系中的不同角色、灾难责任的归属三个层面作答。正文 13 段、391 字，无图片、无引用块。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开门见山否定提问中的设想", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "神人分界是绝对界限，且分界不只在能力上，还在伦理角色上", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "界定神的地位（不受审判的最终决定者、在价值判断之外）；神的行为即使致人灭绝，自救自存责任仍完全在人", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "由责任在人推出：人须提前探知危机预兆、在灾难中自存，失败只能静思己过", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "假设对比：若换成有超强技术的人类或外星人做同样的事，人类会判其有罪并追索；技术领先只使过程漫长复杂，不改变性质", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P011"], "summary": "归结真正差别在“神行无咎”，而非能力更强", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P012"], "summary": "神格与人格非对等位格，人转化为神无任何逻辑途径", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P013"], "summary": "劝告读者不要作成为神的妄想", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人类不能通过技术进步成为神——对提问设想的直接否定。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "神人分界是绝对界限，没有任何手段可以突破。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种分界不只体现在能力上，还体现在伦理体系中的不同角色上。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "神是不受审判的最终决定者，完全处在价值判断之外，其作为在客观上被称为无责任的不可抗力。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "火山、地震、战争瘟疫乃至人类灭绝，自救自存的责任仍然完全在人这一方。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人有必要提前探知危机爆发的预兆，有责任在灾难中自存；失败则只能静思己过。", "evidence": ["E6", "E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若做这些事的是有超强技术的人类（包括外星人），人类的反应会完全不同：会判定其有罪并发动不死不休的惩罚与消灭进程。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使技术领先非常多，也只是使该过程变得漫长而复杂，不会改变其性质。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "神与人的真正差别是“神行无咎”，而不是神比人能力强。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "神格与人格不是对等位格，不存在人转化为神的任何逻辑途径。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "劝告：为了自己好，不要作成为神的妄想。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "先给结论式否定：当然不能（P001）。",
    "给出总纲判断：神人分界是绝对界限，且分界兼在能力与伦理角色（P002-P003）。",
    "定义神的地位：不受审判的最终决定者、价值判断之外、无责任的不可抗力（P004）。",
    "以灾祸为例把责任落到人：即使致人类灭绝，自救自存责任仍在人（P005）。",
    "由责任推出行动要求：探知预兆、灾难自存，失败只能静思己过（P006-P007）。",
    "用反事实对比反证分界性质：同样的行为若出自技术超人/外星人，人必判其有罪并追究（P008-P009）。",
    "限定该反驳的强度：技术领先只使过程漫长复杂，不改变性质（P010）。",
    "收束为差别定义：神行无咎而非能力强（P011）；并由位格不对等推出无转化途径（P012）。",
    "以劝诫结尾：不要作此妄想（P013）。"
   ],
   "concept_usage": [
    {"term": "神人分界", "meaning": "神与人之间的界限；本文称其为绝对界限，任何手段不能突破，且同时是能力层面与伦理角色层面的界限。", "evidence": "P002", "ambiguity": "未说明这一界限的来源、判定标准或是否可被重新定义。"},
    {"term": "神", "meaning": "不受审判的最终决定者，完全处在价值判断之外，其作为被称为无责任的不可抗力；用“祂”指称。", "evidence": "P004", "ambiguity": "未说明是何种宗教/神学意义上的神，也未说明是一神还是多神。"},
    {"term": "神行无咎", "meaning": "神的作为无咎、不受审判，是作者认定的神人真正差别所在（相对于能力更强）。", "evidence": "P011", "ambiguity": "术语只在本文出现一次，未展开其内涵与判准。"},
    {"term": "位格", "meaning": "神格与人格被视为不对等的位格，因此不存在人转化为神的逻辑途径。", "evidence": "P012", "ambiguity": "“位格”的用法未加界定，是否取自神学人格/位格概念，文中未说明。"},
    {"term": "无责任的不可抗力", "meaning": "对神的作为的客观称法：神造成灾难也不承担可归责的责任。", "evidence": "P004", "ambiguity": "“客观上被称为”暗示这是某种外在的称法，但主体未明。"}
   ],
   "examples_and_targets": [
    "火山爆发、地震海啸、战争瘟疫乃至人类灭绝（P005）：作者例证，用以说明灾难中责任仍在人而不在神。",
    "某个有超强技术的人类、包括外星人（P008）：作者设定的反事实类比对象，用来对比神的作为与人的作为招致的不同反应。",
    "人类对该“技术超人”判定有罪并发动不死不休的惩罚与消灭进程（P009）：作者的反事实推演，属修辞性/论证性材料，非外部事实断言。",
    "“为了你自己好”（P013）：训诫式修辞对象为读者本人。"
   ],
   "conditions": [
    "全篇结论以“如果可以靠技术成为神”这一提问假设为对照面，作者的否定是该假设条件下的判断（P001-P002）。",
    "神免责的判断限定在“客观上被称为无责任的不可抗力”这一称法下（P004）。",
    "反事实对比的条件明写为“但假设是”（P008），属假设语气，不等于作者断言现实中已有此类技术超人。",
    "技术领先的影响被限定为“只是使这个过程变得漫长而复杂”，不改变性质（P010），即作者不排除技术上更强的对手存在。"
   ],
   "rhetoric_and_tone": "语气冷峻、断然，带训诫色彩：全文以“当然不能”开篇，以祈使句“不要作这种妄想”收尾，中间以“即使……也只是……不会改变”的让步-否定句式强化界限的绝对性；使用“祂”“ta”两种指称区分神与人；宗教语汇（价值判断、审判、不可抗力、神格/人格）密集，但未标明教派来源。",
   "unresolved_questions": [
    "“神”的所指未说明：是某一宗教的神、抽象位格还是修辞用法，正文未交代，影响对整个分界论的解释。",
    "“技术上成为神”的具体含义（延长寿命、改造身体、获得神的能力）未界定，作者的否定针对何种具体手段不明。",
    "P004“完全置身于在价值判断之外”与 P005“自救自存的责任任然完全在人”中的“于在”“任然”疑为原文用字如此，未作改动，是否笔误需研究者比对原始发布版本。",
    "“客观上被称为无责任的不可抗力”中“客观”的判定主体未明（是谁在这样称呼）。",
    "本文未说明人类若掌握超强技术是否会改变伦理判定的标准，该问题只在 P008-P010 以反事实方式带过。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "当然不能。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "神人分界是绝对界限，没有任何手段可以突破。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这种分界不光体现在能力上，还体现在伦理体系中的不同角色上。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "神是不受审判的最终决定者，完全置身于在价值判断之外", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "自救自存的责任任然完全在人。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "是你有责任灾难中自存。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "如果失败，人类只能静思己过。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "但假设是某个有超强技术的人类——包括外星人——在做这些事", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "人类就会判定这人有罪", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "即使技术领先非常多，也只是使这个过程变得漫长而复杂，不会改变其性质。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "神和人的真正差别其实是神行无咎，而不是神比人能力强。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "不存在人转化为神的任何逻辑途径。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "为了你自己好，不要作这种妄想。", "relation": "supports"}
   ],
   "notes": ""
  },
  "provisional_tags": {
   "domain_candidates": ["宗教/神学观念", "技术与人的界限", "伦理学（责任归属）"],
   "issue_candidates": ["技术能否使人成神", "神人界限的绝对性", "灾难责任的归属", "神的无责任性/不可抗力"],
   "text_function_candidates": ["答疑", "论辩", "训诫"],
   "object_candidates": ["神", "人类", "外星人（假设）", "提问者"],
   "working_keywords": ["神人分界", "神行无咎", "位格", "无责任的不可抗力", "静思己过"]
  },
  "notes": "13 段均为 body，无图片、无引用块、无平台标签混入。正文有两处疑为原文用字：“完全置身于在价值判断之外”（P004）、“自救自存的责任任然完全在人”（P005），为保持逐字引用原样保留，未作改动。提问字段不在 structure 段落内，故未为 question 建证据条目，仅在 question_context 中记录其归属。"
 },
 "8daac81c": {
  "analysis": {
   "question_context": "知乎提问：「如何评价『没有祖国你什么都不是』这句话？」（Q001，属提问者引用的待评句子，不是作者主张）。作者不直接接受也不直接反转该句，而是给出限定式回答：不至于“什么都不是”，但公共服务确实构成个人实际财富的很大一部分，并以公安、立法司法、国防、医疗、基础设施等反事实逐一铺陈。正文 16 段、1418 字，无图片。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "给出限定式总答：不至于“什么都不是”，但公共服务是个人实际财富的很大一部分", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "以公安系统为例：无公安则治安消耗的财富远大于税金，私人卫队昂贵", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "历史对比：不靠国家的时代宗族提供人身保护，代价是征兵权与审判权，难以定价", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "反事实：无立法司法系统则营商成本更高、供应链向第一产业倒退", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "反事实：无现代国防则所有权随时可能被宣布非法，极端情况下失去生命", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P006"], "summary": "反事实：无公共医疗体系，大部分人寿命可能无法超过50岁", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P007"], "summary": "反事实：无公共基础设施，现代化生活即使可能也成本高昂", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P008"], "summary": "提出正面判断：有效的国家公务员体系代为执行的长期投资是普通人能参与的最有效率与成果的投资之一", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P009"], "summary": "理由：普通人的财富花费多为维持性与享乐性，个人“投资”绝大部分以失败告终", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P010"], "summary": "假设性例证：数百万人集资办企业做宏大基建，因盈利冲动与投资原则冲突更可能化为闹剧", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P011"], "summary": "小结：基于税金的国家级战略性投资几乎是个人能分享利润的最有成效的投资之一", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P012"], "summary": "限定：真正的问题是行政体系须总体有效、收益多大程度被共同投资人享受、强制投资份额是否危及财务安全", "role": "qualification"},
    {"unit_id": "U013", "paragraph_refs": ["P013"], "summary": "条件结论：若三问答案都是积极的，“国家”会成为普通公民个人财富中占比极大的一部分", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P014"], "summary": "例证：身无分文的美国公民凭可给绿卡的身份也能卖出钱，并分享军事敬畏与好莱坞文化仰视等可资本化财富", "role": "example"},
    {"unit_id": "U015", "paragraph_refs": ["P015"], "summary": "理由：祖国是能最大化兑现母语能力价值的地方，失去母语等于凭空失去一大笔财富", "role": "reason"},
    {"unit_id": "U016", "paragraph_refs": ["P016"], "summary": "收束：在祖国是运转有效实体的前提下，没有它虽不至于“什么都不是”，但绝对是非常现实的沉重损失", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“没有祖国你什么都不是”不至于成立，但公共服务确实是个人实际财富的很大一部分。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若无整个公安系统，治安问题消耗的个人财富将远大于目前公安系统所花税金。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在不靠国家的时代，宗族提供人身保护的交换条件是征兵权与族规审判权（可令人沉潭），这些难以用金额定价。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若无现有立法和司法系统，营商成本可能高很多，依赖的上下游低利润友商会消失，供应链会大幅向第一产业靠拢。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若无现代国防，一切所有权都可能随时被宣布为非法；某些极端情况下种族、宗教都不被允许存在，可能失去生命。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "没有公共医疗体系，大部分人的寿命可能无法超过50岁（尚不计战乱饥荒）。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "没有大量公共基础设施，现代化的生活即使不是不可能，至少也是成本高昂的。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有效的国家公务员体系代为执行的长期投资，是普通人能参与的最有效率和成果的投资之一。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "普通人对财富的花费更多是维持性和享乐性的，其所谓“投资”绝大部分将以失败告终。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "数百万人集资办企业做宏大基建，因股东盈利冲动与投资原则混乱冲突，更大可能是化为闹剧、资金化为乌有。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基于税金和财政收入的公务员体系国家级战略性投资，几乎是个人能参与和分享利润的最有成效的投资之一；这些税金若真被留下，想获得同样收益率几乎不可能。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题是三项条件：行政体系必须总体有效而非总体无效；收益在多大程度上确实被共同投资人享受；近乎“强制投资”的份额是否危及投资人的财务安全。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果这三个问题的答案都是积极的，“国家”就会成为普通公民个人财富中占比极大的一部分。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国公民身份、军事优势带来的敬畏与好莱坞文化强势带来的仰视，都是容易品牌化资本化的现实财富。", "evidence": ["E14"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "祖国是唯一能最大化兑现人的语言能力价值的地方，不能使用母语等于凭空失去很大一笔财富。", "evidence": ["E15"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在祖国是一个运转有效的实体的前提下，没有它虽不至于使一个人“什么都不是”，但绝对是一份非常现实的、沉重的损失。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "先对提问所引口号作降调处理并提出核心判断：不至于“什么都不是”，但公共服务是个人实际财富的一大部分（P001）。",
    "用公安系统作第一个反事实例证，并辅以私人卫队昂贵的类比（P002）。",
    "以宗族时代的人身保护作历史对比，指出其代价是征兵权与审判权（P003）。",
    "依次以立法司法、国防、公共医疗、公共基础设施四项“如果没有/没有”推演公共服务的财富意义（P004-P007）。",
    "从反面转到正面：有效公务员体系的长期投资是普通人能参与的最有效率的投资之一（P008），并先驳个人自主投资的可行性（P009-P010）。",
    "小结为国家级战略性投资的收益率优势（P011）。",
    "提出三项限定条件，把结论从无条件改为有条件（P012-P013）。",
    "补充两项个人财富来源：身份与军事/文化优势的可资本化（P014）、母语能力的兑现（P015）。",
    "收束为条件化结论：在祖国运转有效的前提下，损失是现实而沉重的（P016）。"
   ],
   "concept_usage": [
    {"term": "公共服务", "meaning": "由“祖国/国家”提供的公安、立法司法、国防、公共医疗、公共基础设施等；本文视其为个人实际财富的组成部分。", "evidence": "P001", "ambiguity": "未给出定义，也未见穷举；列举以反事实方式展开。"},
    {"term": "祖国", "meaning": "提供上述公共服务与身份、文化、语言变现条件的实体；其价值以“运转有效”为前提。", "evidence": "P016", "ambiguity": "与“国家”“公务员体系”在文中交替使用，未区分民族/文化意义上的祖国与政权意义上的国家。"},
    {"term": "税金 / 近乎“强制投资”的份额", "meaning": "公民纳税被作者视为参与国家级长期投资、分享收益的份额，因此需评估其收益与财务安全风险。", "evidence": "P012", "ambiguity": "“强制投资”加引号，作者未表明这是自己的定性还是引述他人说法。"},
    {"term": "个人实际财富", "meaning": "不仅指现金与资产，还包括由公共服务、身份、文化优势与母语能力带来的现实可兑现价值。", "evidence": "P001", "ambiguity": "未说明如何计量，P003 明说“能不能用一个金额来定价还是个玄学问题”。"},
    {"term": "国家公务员体系", "meaning": "代为执行长期投资、基于税金和其他财政收入运作的行政体系。", "evidence": "P008", "ambiguity": "“有效/无效”的判准未在本文给出。"}
   ],
   "examples_and_targets": [
    "提问所引“没有祖国你什么都不是”（Q001）：评价对象，属提问者提供的待评句子，非作者主张。",
    "李嘉诚要防住张子强们（P002）：作者例证/修辞材料，用于说明私人安保昂贵；属事实性断言，本文未给来源。",
    "不靠国家的时代的宗族（P003）：作者的历史对比材料，含抢水械斗征兵权、族规沉潭审判权。",
    "美国公民靠结婚给移民绿卡而把身份卖出钱、好莱坞文化强势（P014）：作者例证，属事实性断言，未给来源。",
    "数百万人集资成立企业进行宏大基建投资（P010）：作者设定的假设性思想实验，非史实叙述。",
    "“从门口地里刨出来，趁赶集卖掉”（P004）：作者用于形容供应链倒退的修辞性说法。"
   ],
   "conditions": [
    "全篇多项判断以反事实条件句给出：“如果没有整个公安系统”（P002）、“如果没有现有的立法和司法系统”（P004）、“如果没有现代国防”（P005）、“没有公共医疗体系”（P006）、“没有大量的公共基础设施”（P007），均非对现实状态的断言。",
    "个人投资失败的判断以“绝大部分”为量词（P009），非全部。",
    "结论的适用前提明写为“在祖国是一个运转有效的实体的前提下”（P016）；P013 另加“如果这三个问题的答案都是积极的”条件。",
    "对立法司法系统有让步限定：“尽管它们并不令人满意”（P004）。",
    "极端情形被单独限定：“某些极端情况下”（P005）。",
    "多项事实断言带“可能”修饰（P004、P005、P006），保留不确定语气。"
   ],
   "rhetoric_and_tone": "论辩兼答疑语气，克制而口语化。结构上以五个“如果/没有”的反事实排比铺陈公共服务的价值，再转为正面论证；多处使用让步（“固然是”“尽管它们并不令人满意”）、量词限制（“绝大部分”“很大的一部分”）与调侃式表达（“还是个玄学问题”“被更美好的称为‘改善生活’”）。对提问所引口号不作正面批判，而是以“不至于……但是……”的折中式句式重新定价。",
   "unresolved_questions": [
    "标题“基准财”未在正文任何段落出现，标题与正文的关系及含义需研究者复核。",
    "李嘉诚/张子强、美国公民绿卡可卖钱、无公共医疗则寿命难超50岁、好莱坞文化强势等均为作者事实性断言，本文未给数据或来源，待外部核查。",
    "“公共服务”未定义也未穷举，作者只列公安、立法司法、国防、医疗、基础设施，是否有其他项未说明。",
    "P012 三项条件中“总体有效”“多大程度”“是否危及财务安全”均未给出判定标准或阈值。",
    "“强制投资”带引号，文中未说明是否为引述他人用语。",
    "提问所引“没有祖国你什么都不是”的原始说话者与语境未在正文说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不至于“什么都不是”，但是公共服务的确实实在在的是你个人实际财富的很大的一部分。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "如果没有整个公安系统，那么治安问题要消耗的你的财富要远大过目前公安系统所花掉的你的税金", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "宗族向你提供人身保护的交换条件可是可以命令你参加抢水械斗的征兵权", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你的营商成本可能比现在高很多", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你的一切所有权都可能会随时被宣布为非法", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "没有公共医疗体系，大部分人的寿命可能无法超过50岁", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "现代化的生活即使不是不可能的，至少也是成本高昂的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "是一个普通人能参与的最有效率和成果的投资之一", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "而这些所谓的“投资”，其中绝大部分将以失败告终。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "实际上更大的可能是会化为一场闹剧，这几千亿化为乌有", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "几乎是个人能参与和分享利润的最有成效和现实果实的投资之一", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "1）行政体系必须是总体有效的，而不能是总体无效的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "如果这三个问题的答案都是积极的，“国家”就会成为一个普通公民个人财富中占比极大的一部分。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "仅仅凭着可以靠结婚给予移民绿卡，这个身份就可以卖出钱来。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "祖国是唯一能最大化兑现人的语言能力的价值的地方", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "在祖国是一个运转有效的实体的前提下，没有它虽然的确不至于使一个人“什么都不是”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治经济学", "公共财政/税收", "国家与个人关系", "社会评论"],
   "issue_candidates": ["“没有祖国你什么都不是”的评价", "公共服务的个人财富价值", "税金作为强制投资", "国家能力与个人财务安全"],
   "text_function_candidates": ["答疑", "论辩", "评论"],
   "object_candidates": ["祖国/国家", "公务员体系", "公民", "宗族", "美国", "李嘉诚", "张子强"],
   "working_keywords": ["基准财", "公共服务", "税金", "强制投资", "个人实际财富", "母语", "绿卡"]
  },
  "notes": "16 段正文＋提问字段，无图片、无引用块、无平台标签混入。语料 updated_at 为 2026-04-05（晚于发文与常见改稿期），是否含后续增补未在正文标明，需版本复核。标题“基准财”未在正文出现。多项事实性举例（李嘉诚/张子强、绿卡、50岁寿命）未给来源，标为待外部核查。"
 },
 "c3be7e08": {
  "analysis": {
   "question_context": "知乎提问：「帝国主义的定义什么？」（Q001，属提问者）。作者不评论既有定义，而是“抓这个机会”给出自己的“帝国病”论述：先自定义帝国的两个要件，再由要件演绎出帝国必然的行为模式与不可持续的宿命，最后给出唯一出路。正文 59 段、3512 字，无图片、无引用块。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "借提问引入“帝国病”话题，声明先给帝国下定义", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "提出帝国定义的两个要件：A 场域内对每一单独对手的压倒性优势且维持甚久形成“不败神话”；B 利用优势兑换经济利益并孳生相关人口和经济组织", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "政体与有无皇帝不影响实质帝国判定；以鸭子/达克作类比", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "解释为何两要件导致帝国病：不败神话创造额外收入并被转化为岗位、项目、机构、人口；但神话天生脆弱，可能一夜破灭", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "神话破灭的后果：收入蒸发而事业人口组织无法蒸发→重大利益再分配与秩序挑战甚至灾难；帝国竭力避免后往往已精疲力竭；体面退场反而多是善终", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016"], "summary": "双子楼式倒塌是最大噩梦却也是常态，故帝国必转向特定行为模式", "role": "transition"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018"], "summary": "第一行为模式：制造分裂和矛盾——因无帝国能一己胜过所有他国总和，神话须仰赖敌手间不可调和的矛盾；此举使其成为麻烦制造者与邪恶根源，种下仇恨并推高武力成本", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020"], "summary": "第二行为模式：插手一切国家事务、扶持依赖帝国的代理人；但扶持是陷阱，无论对象胜任与否都成为亏本买卖", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022"], "summary": "总结：该行为模式即帝国主义的本质，帝国主义的行为模式定义了帝国", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028"], "summary": "帝国生命公式与帝国病机制：额外利益须大于维持霸权成本；维持霸权本身推高成本并恶化崩溃后果；额外利益被食利内部集团吃掉；因崩溃后果已过重，亏本买卖只能继续；模式数学上不可持续，审判日终会到来", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "三阶段病程：一、新强国怀理想、被欢迎、深入各国经济生活；二、商业冲突引出当地司法独立与主权问题，强国陷入实力自信与“秩序税”两个心结；三、积极运用武力优势索求不对等地位与司法豁免，并不断扩军、杀鸡骇猴、制造对立", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P042", "P043", "P044"], "summary": "第三阶段后彻底发育成新帝国，进入越赌越需要赢的恐惧，把核心资产压上赌桌，依次出卖理想、盟友、信用与伦理底线", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P045", "P046", "P047", "P048"], "summary": "限定：末期并非每个帝国都能走到；历史上大部分帝国在末期前因其他原因崩溃；未至末期的倒塌反可摆脱病态负担、锤炼新精英团体成为复兴种子；至末期决堤则万劫不复", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P049", "P050", "P051", "P052"], "summary": "断言历史上帝国无一例外沿此轨迹，并以因果链收束崩溃结局", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P053", "P054", "P055", "P056", "P057", "P058", "P059"], "summary": "出路：需强国历经无数次帝国轮回学会“仁爱”，相信仁爱而受损胜过霸道而获益，才可能从单打独斗天下无敌挺到胜于所有可能敌人之总和；作者称此为唯一出路，并以“难如登天”作结", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帝国的定义含两个要件：A）在自场域内对每一个单独对手拥有已维持甚久的压倒性优势，因而拥有“不败神话”；B）利用该优势地位兑换相当规模的经济利益，并据此孳生相关人口和经济组织。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帝国内部政体如何、有无皇帝，都不影响符合两要件的国家成为实质帝国。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不败的神话”创造额外收入，且这份收入很难不被转化成新的工作岗位、建设项目、机构与人口。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“不败的神话”有天生脆弱性，可能在一夜之间破灭，无人能确信自己永恒不败。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "神话一旦破灭，相关收入飞快蒸发，但仰赖这份收入的事业、人口与组织无法蒸发，必将引起帝国内部重大利益再分配、秩序的重大挑战乃至灾难。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "帝国必竭尽一切可调动资源避免崩溃，真发生时往往已精疲力竭无法阻止；因此在大多数情况下“帝国斜阳缓缓下沉”式的体面退场反而是一种善终。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如双子楼那样上半截倒塌连带下半截毁灭，是帝国最大的噩梦，而这恰恰是帝国退下历史舞台的常态。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帝国将不可避免地制造分裂和矛盾：因至今没有任何强大帝国能凭一己之力胜过所有其他国家综合国力之和，其不败神话必须仰赖潜在敌手之间不可调和的矛盾；这使它成为麻烦制造者与邪恶根源，并种下报复的种子、增大所需武力与成本。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帝国有强烈冲动插手一切国家事务，并倾向扶持必须依赖帝国托举才能维持的代理人，以保证对地域政治局势的最大影响力。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种扶持是陷阱：扶持对象若未获主流民意认可便成无底洞与道德脓疮；若获认可而上台，则几乎总会摆脱扶持者去主张令宗主国不满的主权与内政自由——仍是一桩亏本买卖。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述行为模式就是“帝国主义”的本质，而帝国主义的行为模式定义了帝国。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帝国的生命公式是“由霸权所带来的额外利益”大于“维持霸权的成本”。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "帝国病（致命问题）在于：维持霸权的行为本身注定一方面不断推高维持霸权的成本，另一方面恶化霸权崩溃的后果。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "霸权带来的额外利益总被食利的内部集团吃掉，使弥缝飞速升高的霸权维持成本越来越困难，终有一天变成亏本买卖。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因崩溃后果已积累得过于严重，这桩亏本买卖必须一直做下去。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "帝国的宿命悲剧在于该模式从数学上不可持续；总有一天不败的神话破灭、“审判日”到来。", "evidence": ["E21", "E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切踏入帝国主义之路的强国总是挣扎着迈向单向发展、几乎没有回头路的病程，作者将其分为三个阶段描述。", "evidence": ["E23", "E24"]},
    {"claim_id": "C018", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "第二阶段的新强国面对两个心结：一是相信自己与“落后国家”相矛盾的理念才是对的，其自信来自对自身实力的自信；二是意识到自己在承担维持秩序的成本，遂产生收取“秩序税”的心态与特殊优待的“合理诉求”。", "evidence": ["E25", "E26"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到第三阶段新强国已彻底发育成新帝国，进入越赌越需要赢、越赢越需要赌，并活在“一旦输掉可能被总反攻、总清算”的恐惧之中。", "evidence": ["E27"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "帝国末期会依次出卖自己的理想与最无关紧要的盟友、信用与可忍受牺牲的盟友，最后是伦理底线和全部盟友。", "evidence": ["E28"]},
    {"claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "并非每个帝国都能走到末期；历史上大部分帝国在末期之前已因其他原因崩溃；未至末期就发作的帝国往往经由倒塌摆脱病态负担、在灾难中锤炼出新精英团体，成为下一次国家复兴的种子。", "evidence": ["E29", "E30"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真的发展到末期而决堤，帝国就万劫不复。", "evidence": ["E31"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类历史上波澜壮阔的帝国无一不是沿这条轨迹走向地狱，“一个例外都没有”。", "evidence": ["E32", "E33"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要摆脱该宿命，需有强国历经无数次帝国轮回、从无数历史教训中学会强者最难学会的能力——仁爱；要相信仁爱而受损胜过霸道而获益；作者称只有这一条出路。", "evidence": ["E34", "E35"]},
    {"claim_id": "C025", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "只有这样的国家才有机会真正从“单打独斗天下无敌”挺到“胜于所有可能敌人的总和”；即需要一个民族在天下无敌时仍相信“被打了左脸，还要送上右脸”是对的，而作者认为这难如登天。", "evidence": ["E36", "E37"]},
    {"claim_id": "C026", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "questioned", "statement": "作者以反问形式代述帝国的自我辩解逻辑：若强大换不来优待，强大就反而成了诅咒。", "evidence": ["E38"]},
    {"claim_id": "C027", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "questioned", "statement": "作者以引号独白代述帝国的心声：无论怎样自我克制都摆脱不了被认定为恶人的宿命，那又何必为虚名放弃巨大现实利益。", "evidence": ["E39"]},
    {"claim_id": "C028", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "即使一时出于对帝国病的警惕而自我警醒，随着时间推移该结构会造成越来越强的压力与冲动；它至多无力阻止新强国以“最大的节制”争取“最起码的公平”，而这样的要求仍会被对方认定为蛮横干涉和仗势凌人。", "evidence": ["E40", "E41"]}
   ],
   "argument_steps": [
    "声明先定义帝国（P002-P003）。",
    "给出构成定义的两个要件 A、B（P004-P005）。",
    "以“政体无关”与鸭子/达克类比排除名义标准（P006-P007）。",
    "设问为何两要件必然导致帝国病，答以“不败神话创造额外收入”与其脆弱性（P008-P010）。",
    "推演神话破灭的连锁后果：收入蒸发而事业人口组织不可蒸发（P011-P012）。",
    "加入帝国的应对变量：竭尽资源避免→真发生时已精疲力竭（P013），由此推出体面退场是善终（P014）。",
    "以双子楼类比给出常态判断，并转入行为模式分析（P015-P016）。",
    "第一条行为模式及其机制说明（P017-P018）；第二条行为模式及其陷阱（P019-P020）。",
    "归纳：该行为模式即帝国主义的本质（P021-P022）。",
    "给出生命公式（P023），并由公式推出帝国病机制（P024）。",
    "补充食利集团与路径锁定（P025-P026），得出数学上不可持续的宿命判断（P027-P028）。",
    "以三阶段病程展开历史叙述性论证（P029-P041），其中插入两处帝国自我辩解的反问与独白（P034、P039）。",
    "指出第三阶段完成向帝国的转化并进入赌局恐惧（P042），预测末期的出卖次序（P043-P044）。",
    "以“并非每个帝国都走到末期”作限定，并区分灾变与复兴两种结局（P045-P048）。",
    "断言历史无例外（P049-P050），以因果链收束崩溃（P051-P052）。",
    "最后从诊断转向劝谕：唯一出路是学会仁爱（P053-P058），以“难如登天”收束（P059）。"
   ],
   "concept_usage": [
    {"term": "帝国", "meaning": "同时满足两要件（对每一单独对手的持久压倒性优势即“不败神话”；以优势兑换经济利益并孳生人口与经济组织）的国家，政体与名义称号无关。", "evidence": "P004", "ambiguity": "“自己的场域”与“压倒性优势”的衡量标准未定义；也未举任何具体国家为例。"},
    {"term": "帝国病", "meaning": "维持霸权的行为本身注定推高维持霸权的成本，同时恶化霸权崩溃的后果，使生命公式终将不成立。", "evidence": "P024", "ambiguity": "是否可逆、能否预防，文中只在 P036 提到“一时……自我警醒”，未给可操作判据。"},
    {"term": "不败神话", "meaning": "长期压倒性优势所形成、被视为不可战胜的信念；它创造额外收入，也天生脆弱、可能一夜破灭。", "evidence": "P004", "ambiguity": "“一夜之间”为修辞性表述，破灭的速度与判据未说明。"},
    {"term": "生命公式", "meaning": "“由霸权所带来的额外利益”大于“维持霸权的成本”；是作者判断帝国可持续性的算式。", "evidence": "P023", "ambiguity": "两项均无计量方式，P027 的“从数学上不可持续”未给出模型或推导。"},
    {"term": "帝国主义", "meaning": "本文不沿用既有辞书定义，而指上文所述帝国必然的行为模式（制造分裂矛盾、插手他国事务、扶持代理人等）。", "evidence": "P021", "ambiguity": "作者自认此用法与通行定义的关系未作讨论，虽然提问正是问“帝国主义的定义”。"},
    {"term": "秩序税", "meaning": "第二阶段强国因自认承担维持秩序成本而产生的、要求以特殊优待折抵成本的诉求。", "evidence": "P033", "ambiguity": "带引号，未说明是作者自造术语还是引述他人用语。"},
    {"term": "食利的内部集团", "meaning": "吃掉霸权额外利益的帝国内部集团，使弥缝霸权维持成本越来越困难。", "evidence": "P025", "ambiguity": "未说明其构成、规模或与政体的关系。"},
    {"term": "仁爱", "meaning": "作者给出的唯一出路：强国在天下无敌时仍相信“被打了左脸，还要送上右脸”是对的，甘愿为仁爱受损。", "evidence": "P054", "ambiguity": "与 P055 的宗教语汇关系未说明，也无制度化路径，作者自评“难如登天”。"}
   ],
   "examples_and_targets": [
    "鸭子／自称“达克”（P007）：作者类比材料，用于说明名义不决定实质。",
    "双子楼倒塌（P015）：作者类比材料，喻帝国连带毁灭式崩溃。",
    "“帝国斜阳缓缓下沉”（P014）与“被打了左脸，还要送上右脸”（P058）：引号内的成句引用，出处均未标注，待外部核查（后者疑为宗教文本语句）。",
    "赌桌、坐庄、抵押（P042-P043）与“海洛因、不归路”（P055）：修辞性比喻，非事实叙述。",
    "历史帝国整体（P046、P049-P050）：作者以泛称给出的历史断言，未举任何具体帝国、时期或事件。",
    "提问者所问“帝国主义的定义”（Q001）：作者回应的语境与靶子，其定义主张出自作者本人。"
   ],
   "conditions": [
    "两要件中“因为这个优势已经维持甚久”是必要条件（P004），即新近获得的优势不构成帝国。",
    "多处以条件句展开：一旦神话破灭（P011）、“当这种情况真的发生时”（P013）、“真的发展到末期而决堤”（P048）。",
    "量词与概率限定：“可能在一夜之间破灭”（P010）、“在大多数情况下”（P014）、“几乎总是会选择摆脱原有的扶持者”（P020）、“历史上大部分的帝国”（P046）、“并非每个帝国都能走到这个末期”（P045）。",
    "时间限定：“直到现在，仍然没有任何一个强大帝国能做到……”（P018）表明该无例外判断限于迄今。",
    "场景限定：第二阶段冲突发生在“在正常的经济交往之中”（P031）。",
    "帝国自我警醒的可能被限定为“即使一时”（P036），暗示其不可持续。"
   ],
   "rhetoric_and_tone": "冷峻、断言式的理论推演，兼有历史叙事的铺陈与末段的道德劝谕。手法上：以定义-演绎结构推进；密集使用反问（“谁能忍住不……”“谁能确信自己永恒不败？”“不是吗？”“难道两头落空？”“要到何时才会有一个强国摆脱这个宿命？”）；以引号标示自造术语（“不败神话”“秩序税”“帝国病”）并标示成句引用（“帝国斜阳缓缓下沉”“被打了左脸，还要送上右脸”）；用鸭子、双子楼、赌桌、海洛因等多组比喻；第二人称“你们必须自己判我赢”等句式模拟帝国口吻（P040-P041），属代入式修辞而非作者自述立场。结尾由“只有这一条出路可言”转“难如登天”，语气由冷峻转为悲悯。",
   "unresolved_questions": [
    "全文未举任何一个具体帝国（罗马、英国、美国等）为例，“一个例外都没有”的全称历史断言无个案支撑，需研究者补证或外部核查。",
    "“自己的场域”（P004）未定义，边界如何划定不明。",
    "“从数学上不可持续”（P027）未给出模型、变量或推导。",
    "“秩序税”、“帝国斜阳缓缓下沉”（P014）、“被打了左脸，还要送上右脸”（P058）均带引号但未标出处；后者疑为宗教文本语，须外部核查。",
    "P039 引号内独白的说话者未标明：是作者代拟的帝国心声，还是引述某文本，正文未交代。",
    "P034 的反问句主体在“我们/他们”之间滑动（P033 用“他们”，P034 用“我们”），指称是否一致需复核。",
    "三阶段病程是否适用于非西方、古代帝国未说明；“强国”与“帝国”在文中未严格区分（P029 称强国，P042 才称发育成帝国）。",
    "提问所问为“帝国主义的定义”，但作者未讨论通行定义与自身定义的差异，也未说明是否取代之。",
    "帝国病是否可预防、仁爱是否有制度化可能，文中只在 P036、P054-P058 作原则性表述，未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "A）在自己的场域内拥有对每一个单独的对手的压倒性优势", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "B）帝国利用了这种优势地位，兑换了有相当规模的经济利益", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "帝国内部采用什么样的政体、有没有一个皇帝，都并不影响符合这两个要件的国家成为实质上的帝国", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "因为“不败的神话”创造了额外收入，谁能忍住不把这份收入转化成新的工作岗位、新的建设项目、新的机构、新的人口？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "而“不败的神话”却有天生的脆弱性，可能在一夜之间破灭", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "但收入可以一夜蒸发，仰赖这份收入的事业、人口和组织却无法蒸发。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "这必将引起帝国内部的重大利益再分配，导致帝国内部秩序的重大挑战，甚至演变成灾难。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "帝国往往也已经处在精疲力竭，无法阻止它发生的状态。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "“帝国斜阳缓缓下沉”这种体面的退场反而是一种善终。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "这是帝国最大的噩梦，而且恰恰是帝国退下历史舞台的常态。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "第一，帝国将不可避免地要去制造分裂和矛盾。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "所以帝国的不败神话一定要仰赖于所有潜在敌手之间不可调和的矛盾", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "第二，帝国有强烈的冲动去插手一切国家的事务。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "但这种扶持却是一种陷阱", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "上面这种行为模式，就是帝国主义四个字的本质。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P022", "quote": "而帝国主义的行为模式定义了帝国。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "帝国的生命公式，就是“由霸权所带来的额外利益”要大于“维持霸权的成本”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "维持霸权的行为本身，就注定会一方面不断推高维持霸权的成本，而在另一方面恶化霸权崩溃的后果。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P025", "quote": "由霸权所带来的额外利益，总是会被食利的内部集团吃掉。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P026", "quote": "这亏本买卖必须一直做下去，一直一直地做下去。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P027", "quote": "帝国的宿命悲剧在于，这个模式从数学上不可持续。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P028", "quote": "总有一天，不败的神话破灭，审判日到来。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P029", "quote": "一切踏入这条帝国主义之路的强国都总是挣扎着迈向这个单向发展、几乎没有回头路的病程", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P030", "quote": "第一阶段，新生的强国心怀美好的理想。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P032", "quote": "它全身心地相信“落后国家”的与自己相矛盾的理念本身是错误的", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P033", "quote": "这无法不让他们产生“我们应该收取某种秩序税”的心态。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P042", "quote": "新生的强国已经彻底地发育成了新的帝国。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P044", "quote": "首先它出卖的是自己的理想、最无关紧要的盟友", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P045", "quote": "并非每个帝国都能走到这个末期。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P047", "quote": "在灾难中锤炼出一个新的精英团体，成为下一次国家复兴的种子。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P048", "quote": "真的发展到末期而决堤，帝国就万劫不复了。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P049", "quote": "细细地分析下来没有一个不是沿着这条轨迹走向地狱。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P050", "quote": "一个例外都没有。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P054", "quote": "去从无数的历史教训中学会强者最难学会的能力——仁爱。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P057", "quote": "只有这一条出路可言。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P056", "quote": "有机会真正地从“单打独斗天下无敌”，挺到“胜于所有可能敌人的总和”。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P058", "quote": "却能相信“被打了左脸，还要送上右脸”是对的。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P034", "quote": "否则我们的强大不但不是我们的祝福，反而成为了我们的诅咒，不是吗？", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P039", "quote": "我又何必为了这留不住的虚名放弃那么巨大的现实利益呢？难道两头落空？", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P036", "quote": "这种“继续坚持毫无收益、撕破却可以得到立竿见影的巨大利益”的结构会造成越来越强大的压力和冲动。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P037", "quote": "它无力阻止新生的强国去以“最大的节制”争取“最起码的公平”。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P001", "quote": "抓这个机会说说“帝国病”问题。", "relation": "context"},
    {"key": "E43", "paragraph_id": "P053", "quote": "要到何时才会有一个强国摆脱这个宿命？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际政治/地缘政治", "政治理论（帝国研究）", "历史哲学", "经济与霸权成本"],
   "issue_candidates": ["帝国与帝国主义的定义", "霸权成本与额外收益", "霸权崩溃的机制", "代理人扶持的困境", "秩序税与司法豁免", "大国兴衰的出路"],
   "text_function_candidates": ["答疑", "论辩", "理论阐述", "批评", "劝谕"],
   "object_candidates": ["帝国", "帝国主义", "强国", "宗主国", "代理人", "食利的内部集团", "被统治国家/落后国家"],
   "working_keywords": ["帝国病", "不败神话", "生命公式", "秩序税", "三阶段病程", "仁爱", "审判日"]
  },
  "notes": "59 段全部为 body，无图片节点、无结构缺口（divergence=false）。文中所有“帝国”均为泛称，未点名任何具体国家或历史事件，故“一个例外都没有”的全称断言只记录为作者主张，不做事实认定。P014、P033、P058 的引号成句出处未标注，P039 独白说话者未标明，均已登记为待核查。P004 的“达克”出自 P007 鸭子类比。"
 },
 "5ccc226d": {
  "analysis": {
   "question_context": "知乎提问：「50 多位老人众筹买房，抱团养老 15 年却『曲终人散』，原因是什么？老龄化社会如何解决养老问题？」（Q001，属提问者，含提问者对案例的描述）。作者未评论该具体案例，也未直接回答老龄化政策问题，而是给出“好的养老团体”应具备的三个条件：向下延伸形成梯队、团体充裕而非贫瘠、以“志同道合”的价值观为灵魂并一代代引入继承者。正文 10 段、531 字，无图片；末段存在结构差异（见 notes）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "好的养老团体必须向下延伸到五十岁左右乃至三四十岁阶层以形成梯队效应、维持组织延续，否则总要“曲终人散”", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "团体应充裕而非贫瘠，主要驱动力应是“志同道合”而非“可以省钱”；充裕指资产性收入足以维持正常体面的半集体生活，使孤独生活成本更高且质与量有落差，从而形成筛选余地", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "这种团体客观上会把影响力延伸到早年教育：成员从子女一出生起（或传人被选定时）按特定价值观标准进行人格教育，为子女/传人争取接力加入的归宿资格", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "找到“遵从即可一起终老”的价值观才是团体的灵魂；缺少这套一代代引入继承者的价值观体系，基于一时情投意合的养老安排都不能摆脱曲终人散", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "养老团体必须同时是价值观大学和研究所，且预科录取年龄至少四十岁", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "末段为一问句“你心目中完美的养老院是什么样的？”，疑为平台引导语，归属不明", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个好的养老团体必须向下延伸到接纳五十岁左右的中老年人，最好延伸到三四十岁阶层，才能形成梯队效应、长期维持组织延续。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "否则（缺少梯队效应时）很自然总要“曲终人散”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "团体本身应该是充裕的而不是贫瘠的，形成团体的主要驱动力不应该是“可以省钱”而必须是“志同道合”。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "充裕不等于人人都要有钱，而是团体资产性收入足以维持正常体面的半集体生活，使孤独生活成本更高且在质与量上难以与团体生活相比，从而形成对申请者的选择动力与筛选“适格候选人”的余地。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这种团体客观上最后会自然把影响力延伸到早年教育：成员从子女一出生起（或传人被选定时）就按特定价值观标准进行人格教育，为子女/传人争取接力加入体系的归宿资格。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "找到“遵从即可一起终老”的价值观，才是这个团体的灵魂所在。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "没有作为灵魂的价值观体系去一代代引入继承者，任何基于一时情投意合的养老安排都不能摆脱最终曲终人散的命运。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "养老团体不能仅仅是集体食堂/疗养院/度假酒店，它同时必须是一处价值观大学和研究所。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这所“大学”的预科录取年龄至少也应该是四十岁。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "先给规范判断：好养老团体必须向下延伸吸纳较年轻阶层以形成梯队（P001）。",
    "以反证说明缺此条件的结果：否则总要“曲终人散”（P002）。",
    "给出第二个条件：团体须充裕、驱动力须是志同道合而非省钱（P003）。",
    "对“充裕”作限定解释：不是人人有钱，而是资产性收入足以维持体面半集体生活并形成筛选余地（P004）。",
    "推出该团体的延伸后果：影响力会自然延伸到早年教育与继承人培养（P005）。",
    "给出第三个、也是被称为“灵魂”的条件：一套“遵从即可一起终老”的价值观（P006）。",
    "反面强调该条件的必要性：缺之则任何情投意合的养老安排终将曲终人散（P007）。",
    "用机构类比落实主张：团体必须是价值观大学和研究所（P008），并给出招生年龄标准（P009）。",
    "末段以问句收尾（P010），未再展开。"
   ],
   "concept_usage": [
    {"term": "养老团体", "meaning": "本文讨论的对象，被要求兼具生活共同体与价值观传承机构的性质；作者未指称任何具体组织。", "evidence": "P001", "ambiguity": "与提问所述“众筹买房抱团养老”案例的关系未在正文说明。"},
    {"term": "梯队效应", "meaning": "通过向下延伸接纳五十岁左右乃至三四十岁阶层而形成的年龄梯队，被作者视为组织长期延续的条件。", "evidence": "P001", "ambiguity": "未给出梯队规模、比例或年龄结构的量化标准。"},
    {"term": "志同道合", "meaning": "形成团体的主要驱动力，与“可以省钱”相对；其内容即“遵从即可一起终老”的价值观。", "evidence": "P003", "ambiguity": "作者未说明这套价值观的具体条目或判定方式。"},
    {"term": "充裕", "meaning": "团体资产性收入足以维持正常体面的半集体生活，使孤独生活成本更高且在质与量上难以相比。", "evidence": "P004", "ambiguity": "无金额或收入标准；与“人人都要有钱”被明确区分。"},
    {"term": "价值观大学和研究所 / 预科", "meaning": "对养老团体的机构性比喻：它同时承担价值观教育与价值观研究功能，四十岁被定为预科录取年龄。", "evidence": "P008", "ambiguity": "比喻与实体制度如何对应，文中未说明。"},
    {"term": "传人", "meaning": "团体成员的接班人选，可自子女一出生起或在其被选定时接受价值观人格教育。", "evidence": "P005", "ambiguity": "传人的选定机制与身份关系未展开。"}
   ],
   "examples_and_targets": [
    "提问所述“50 多位老人众筹买房，抱团养老 15 年却曲终人散”（Q001）：提问者提供的案例，作者正文未提及、未分析。",
    "集体食堂 / 疗养院 / 度假酒店（P008）：作者用作反面对照的类比对象，说明养老团体不能只具备这些功能。",
    "价值观“大学”与“预科”（P008-P009）：机构类比材料，用于表达价值观教育与继承者培养的制度性要求。",
    "“曲终人散”（P002、P007）：作者借用提问用语作反复出现的修辞表达，并被用作对失败结局的概括。"
   ],
   "conditions": [
    "梯队要求带程度限定：“必须要向下延伸到接纳五十岁左右的中老年人，甚至最好向下延伸到三四十岁的阶层”（P001）——“最好”表示更优而非必需。",
    "“充裕”被明确定义为团体资产性收入足以维持正常体面的半集体生活（P004），并以“不是说这个团体里人人都要有钱”排除误读。",
    "传承后果被限定为“客观上最后会自然的”（P005），指为可预期的自然延伸而非硬性设计。",
    "年龄标准被限定为下限：“至少也应该是四十岁”（P009）。",
    "适用对象是“一个好的养老团体”（P001），即规范建议而非对所有养老安排的描述。"
   ],
   "rhetoric_and_tone": "规范建议与训导混合的语气，密集使用“必须”“应该”“才是”“不能仅仅”“必须是”，以条件-后果的对照（P002、P007）施压。修辞上以“灵魂”喻价值观体系，以“集体食堂/疗养院/度假酒店”与“价值观大学和研究所”构成俗／雅的对照，并以“预科录取年龄”把机构比喻推向字面化使用。全文无反问、无对手指认、无具体案例，属原则性建言而非案例评论。",
   "unresolved_questions": [
    "结构差异：P010“你心目中完美的养老院是什么样的？”为 lexical 未覆盖的尾部片段（divergence: text_tail_not_in_lexical），疑为平台引导语或提问回显，说话者与归属不明，需人工/版本复核。",
    "作者全文未提及、未解释提问中的“50 多位老人众筹买房，抱团养老 15 年”案例，也未回答“老龄化社会如何解决养老问题”，两者之间只能由研究者推断关联。",
    "“充裕”的量化标准（资产性收入的规模或门槛）未给出。",
    "“适格候选人”的筛选判准、以及“遵从即可一起终老”的价值观具体内容均未说明，仅以“某种特定的价值观标准”带过。",
    "传人／继承者的选定与接力机制、与子女的法律与财产关系未展开。",
    "“价值观大学和研究所”是比喻还是制度设计，文中未区分。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "一个好的养老团体必须要向下延伸到接纳五十岁左右的中老年人", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "否则很自然总要“曲终人散”的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "形成这个团体的主要驱动力不应该是“可以省钱”而必须是“志同道合”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "而是说团体的资产性收入足以维持一个正常体面的半集体生活", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这种团体客观上最后会自然的把影响力延伸到早年教育", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "找到这组“遵从即可一起终老”的价值观，才是这个团体的灵魂所在。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "任何基于一时情投意合的养老安排都不能摆脱最终曲终人散的最终命运。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "它同时必须是一处价值观大学和研究所。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "这所大学的预科录取年龄至少也应该是四十岁。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "你心目中完美的养老院是什么样的？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["养老/社会保障", "社会组织与共同体", "价值观传承与教育"],
   "issue_candidates": ["抱团养老为何曲终人散", "养老团体的年龄梯队", "团体的经济基础与筛选机制", "价值观体系的代际继承"],
   "text_function_candidates": ["答疑", "经验总结", "建议/建言"],
   "object_candidates": ["养老团体", "中老年人", "三四十岁阶层", "子女/传人", "养老院"],
   "working_keywords": ["梯队效应", "志同道合", "可以省钱", "资产性收入", "半集体生活", "曲终人散", "遵从即可一起终老", "价值观大学和研究所"]
  },
  "notes": "10 段正文＋提问字段，无图片。骨架标记 divergence=true，原因 text_tail_not_in_lexical：P010（“你心目中完美的养老院是什么样的？”）不在 lexical 结构内，疑为平台引导语/提问回显，未据其补写作者主张，仅在 U006 与 unresolved_questions 登记。正文未出现提问中的案例内容，二者关系留待复核。status 记为 read（正文完整可读、无图片），不改标 needs_reread。"
 },
 "b9973f8a": {
  "analysis": {
   "question_context": "知乎提问：「说服他人的能力太强怎么办？」（Q001，属提问者，其预设是“说服力强”构成一个问题）。作者接受这一预设并展开：先论证说服力之所以是重担（会干预他人命运、带来道德压力与内疚），再列举三类应对方案（组织性消解、物质补偿、以甘愿承受为前提的自我管理），最后重定义“真正的说服力”并归于“爱”。正文 35 段 body ＋ 1 段 heading、2300 字，无图片。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "前提：人对人有操纵能力，最主要的是说服力，能以相当大概率在很大程度上改变他人立场或态度，故为人所向往", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "转折：真拥有这种能力才会发现它本身就是重担，因为会干预到人的命运", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "举例说明干预的广度：改专业、恋爱分手结婚离婚、让人跳槽；这些是伸手可及的果实，会带来复杂影响", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "第一重压力：是否承受道德压力；不得用“人的命运应该自己负责”推卸；即使法理上无责任，你仍是造成艰难的原因之一", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P009"], "summary": "机制说明：上帝为保护弱者设置内疚本能，使造成他人痛苦者无论有无过错都无一例外承受痛苦；其功能是防止人类发明“无需内疚的奴役手段”", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011"], "summary": "以父母管教子女为类比；并指出寻找“我在法理上没错”的理由对痛苦几乎无消解作用", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "小结：开口说服人必然背负他人命运且痛苦随事项重大程度增大；无可逃避；故必须有值得扛这份痛苦的理由；未体认此点者难有真正的说服力", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018"], "summary": "提出替代方案之一：以系统性组织方法回避和消解痛苦，如心理咨询师的督导系统", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P019", "P020"], "summary": "替代方案之二：取得足够的物质补偿；这是许多靠说服力为生者对抗痛苦的基本方式（抱团互证“这不是你的错”加“适当收费”）", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025"], "summary": "第三条路：以甘愿承受痛苦的志愿、识别独立人格者的眼光、保守而被动的表达依序管理痛苦；志愿绝对优先；无智慧可摆脱；想彻底摆脱痛苦本身不道德；先接受才能真正有效管理，否则终将走向泯灭良知以“降低运行成本”", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "识人标准：看人是否清楚知道听取意见的决策责任仍完全在自己；这样的人“成了自己的王”，只有这种王者值得额外考虑；以刘备/诸葛亮、曹操/杨修、袁绍/田丰、徐庶为喻；“刘备”极罕见", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P030", "P031", "P032"], "summary": "第三种办法（多数情况适用）：“不问不说”——把分析意见放在大路上任人拾取，或只对公众而非具体个人给意见，从而免于主动干预他人命运的负担", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P033", "P034"], "summary": "重定义：真正撼动人心的说服力不来自口才与博闻强识，也不来自万人的方言、天使的话语、先知之能、奥秘、全备的信或移山倒海的成就——那些只是被贪婪与崇拜蒙蔽的盲从", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P035", "P036"], "summary": "结论：真正能造就人的“说服”是世界上最大的奇迹，它只会是出于爱（“爱”被独立为标题段）", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对人是有操纵能力的，其中最主要的是说服力；晓之以理、动之以情，可以以相当大的概率在很大程度上改变他人的立场或态度。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真的拥有这种能力后会发现，这个能力本身就是一种重担，因为它会干预到人的命运。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "凭借说服力，人完全可能说服侄子从理科改学文科、说服某人恋爱/分手/结婚/离婚，或一句话让人对自己的工作左看右看都看不上眼而最终跳槽。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对拥有强大说服力的人，这些事是伸手就可能触及的果实，会带来很多复杂的影响。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不应用“人的命运应该自己负责”来推卸责任、假装道德压力不存在；即使你毫无责任，你毕竟是导致他人艰难的原因之一。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "从法理上讲你可能没有任何责任、过错在对方，但你毕竟是造成这种令人呼痛的重大困难的原因之一。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上帝为了保护弱者设置了一种本能，令一切直接造成他人痛苦的人，无论有无过错，都无一例外要承受内疚的痛苦。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该本能的功能在于避免人类发明一套说辞把制造他人痛苦说成完全正当，否则这种说辞势必将发育成“无需内疚的奴役手段”。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要指望“法理上没有过错”就可以逃过内疚这种心灵的痛苦。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母管教子女时对此有切身感受：明知“天下哪有完美的父母”，仍不可能心安理得、毫无自责与痛苦。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "找寻“我在法理上没错”的理由对这种痛苦几乎没有消解作用，久而久之父母们都懒得找了。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "开口说服人就必然不可推卸地背负他人的命运；他人命运中不可避免的痛苦，只要知道了就必然要负担一份；说服的事情越重大、越根本、影响越全局，这份痛苦可能也就越大。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要想逃避这种负担，因为没得逃避。", "evidence": ["E14"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以开口说服人必须有充分的、值得扛这份痛苦的理由。", "evidence": ["E15"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果这一点都没体认到，人也很难有真正的说服力。", "evidence": ["E16"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“值得背负痛苦的理由”存在别的方案，其中之一是通过系统性的组织方法来回避和消解痛苦。", "evidence": ["E17"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "心理咨询师的督导系统实际上就是借助组织庇护、同侪安慰来消解痛苦的机制：它加强“这不是你的错”的安慰强度、增强对同等强度关切心的钝感，使咨询师变得比较“耐久”。", "evidence": ["E18"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "另一种方法是获得足够的物质补偿——这是很多靠说服力为生的人对抗痛苦的基本方式：抱团互相说服“这不是你的错”外加“适当收费”。", "evidence": ["E19", "E20"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若不打算走上述道路，则只有另一条路：靠愿赌服输甘愿承受痛苦的志愿、识别有独立人格者的眼光，辅以保守而被动的表达来管理痛苦，并严格依此顺序。", "evidence": ["E21"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "甘愿承受痛苦的志愿是绝对必要而优先的准备。", "evidence": ["E22"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "没有任何办法可以靠什么智慧摆脱这种负担。", "evidence": ["E23"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想要彻底摆脱这种痛苦本身是不道德的。", "evidence": ["E24"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "先接受痛苦再管理痛苦，才能真正有效地管理它；若管理的目的本身是拒绝痛苦，管理注定走向前一条路，最终迈向靠彻底泯灭良知来“降低运行成本”“提高利润”。", "evidence": ["E25"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在接受痛苦的前提下要学会识人：默默观察，看人是否能清清楚楚地知道听取别人的意见后决策的责任仍然完全在自己。", "evidence": ["E26"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "完全为自己负责、听了任何意见而出任何后果都仍知道无人可以责怪的人，就成了自己的王。", "evidence": ["E27"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有经过再三观察鉴定被确认的这种“王者”才有资格得到额外考虑；遇到刘备才能做诸葛亮，遇到曹操会变成杨修、遇到袁绍会变成田丰，而其实这时本应做徐庶。", "evidence": ["E28"]},
    {"claim_id": "C027", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "“刘备”极其罕见，出现在很年轻的人身上就更稀少；若觉得这样的人比比皆是，只会是因为评判标准还过于天真和宽松。", "evidence": ["E29"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绝大多数时候要靠第三种办法管理问题——“不问不说”：要么把各种分析和意见放在大路上随人自行搜寻拾取，要么只对公众而非具体的个人问题给出意见。", "evidence": ["E30", "E31"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "前一种做法完全被动和无知觉、后一种非个人，因此可以在很大程度上免于主动干预他人命运的负担。", "evidence": ["E32"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真正能撼动人心的说服力并不来自舌灿莲花的口才和博闻强识的智慧；只有这两条的人，其“说服力”有多强，人们的警戒心就有多强。", "evidence": ["E33"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种警戒心常常可以无视一切雄辩，甚至压倒基本的理性判断，去消解基于绝对逻辑、来自基本理智的强制力。", "evidence": ["E34"]},
    {"claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "真正的说服力不是来自万人的方言、天使的话语、先知讲道之能、明白各样的奥秘、全备的信或移山倒海的成就——那些所达成的只是被贪婪和崇拜蒙蔽的盲从。", "evidence": ["E35"]},
    {"claim_id": "C033", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正能造就人的“说服”是世界上最大的奇迹，它只会是出于爱。", "evidence": ["E36", "E37"]}
   ],
   "argument_steps": [
    "以一般命题开场：说服力是最主要的操纵能力，可显著改变他人立场（P001）。",
    "转折定性：这种能力本身是重担，因为干预他人命运（P002-P003）。",
    "以四组具体情境（改专业、恋爱/分手/结婚/离婚、跳槽）说明干预的日常性与易得性（P004-P005）。",
    "设问“是否打算承受道德压力”，并预先驳掉“命运应自己负责”的免责说辞（P006）。",
    "以法理无责与因果有责的区分深化（P007-P008）。",
    "给出内疚本能的机制与其功能解释（P009）。",
    "以父母管教子女作类比，并指出法理免责说辞对痛苦无效（P010-P011）。",
    "小结为负荷随说服事项重大程度增加，且不可逃避，故需“值得扛痛苦的理由”（P012-P014）。",
    "以“没体认到这点的人也很难有真正的说服力”把该前提与说服力本身挂钩（P015）。",
    "转入替代方案：说明“这不是故事的全部”（P016），列出组织性消解（P017-P018）与物质补偿（P019-P020）两条回避路线。",
    "给出作者认可的第三条路及其严格次序：志愿—识人—保守被动的表达（P021）。",
    "逐条强调：志愿绝对优先（P022）；无智慧可摆脱（P023）；想彻底摆脱即不道德（P024）；管理目的决定走向（P025）。",
    "以“识人”标准与“自己的王”界定谁值得被说服（P026-P027）。",
    "用三国人物对应关系给出实践推论：遇刘备才做诸葛亮，误判则成杨修、田丰，本应做徐庶（P028）。",
    "限定该标准之稀缺（P029），并给出多数场合的第三种办法“不问不说”（P030-P032）。",
    "最后反驳“口才与智慧即说服力”的通俗理解（P033-P034）。",
    "以“它只会是出于/爱”作断句式收束（P035-P036）。"
   ],
   "concept_usage": [
    {"term": "说服力", "meaning": "本文有两层用法：一是作为操纵能力、可改变他人立场态度的实际影响力（P001-P004）；二是文末被重新定义的“真正的说服力”——不来自口才、智慧与异能，而只出于爱（P033-P036）。", "evidence": "P001", "ambiguity": "同一篇内前后两层含义未明确交代其转换，P033 的“所谓说服力”与 P035 的“真正能造就人的说服”是否同一概念需研究者判断。"},
    {"term": "重担 / 道德压力 / 内疚的痛苦", "meaning": "说服他人所引发的道德与心灵负担：内疚被说成上帝为保护弱者而设置的本能，无论有无过错都不可避免。", "evidence": "P009", "ambiguity": "“上帝”的所指与宗教立场未说明；该机制是信仰陈述还是功能性假设，文中未区分。"},
    {"term": "愿赌服输甘愿承受痛苦的志愿", "meaning": "作者列为第三条路中绝对必要而优先的准备，是接受痛苦而非消除痛苦的前提。", "evidence": "P022", "ambiguity": "如何形成这种志愿、可否培养，文中未说明。"},
    {"term": "自己的王 / 独立人格者", "meaning": "完全为自己负责、听了任何意见而出了任何后果都仍知道无人可以责怪的人；只有这种人才有资格得到说服者额外的考虑。", "evidence": "P027", "ambiguity": "“王者”与“独立人格者”是否同义，文中未明说。"},
    {"term": "不问不说", "meaning": "第三种管理办法：把意见放在大路上任人拾取，或只对公众而非具体个人给意见。", "evidence": "P030", "ambiguity": "“放着”与“只对公众说”的边界（如公开答问、专栏写作是否算）未界定。"},
    {"term": "无需内疚的奴役手段", "meaning": "内疚本能所要防止的后果：一套把制造他人痛苦说成完全正当的说辞。", "evidence": "P009", "ambiguity": "概念只在括号内出现一次，未展开其历史或现实所指。"},
    {"term": "爱", "meaning": "真正的“说服”的唯一来源，被作者置于全文末段并以独立标题段呈现；未作定义或展开。", "evidence": "P036", "ambiguity": "内涵完全未说明，与宗教语汇（P009、P034）的关系亦未交代。"}
   ],
   "examples_and_targets": [
    "说服侄子从理科改学文科、说服某人恋爱/分手/结婚/离婚、一句话让人跳槽（P004）：作者假设性举例，用于说明干预范围。",
    "父母管教子女的自责（P010）：作者类比材料，以第二人称代入父母视角。",
    "心理咨询师的督导系统（P018）：作者援引的现实机构机制，作为“组织性消解痛苦”的例证；属事实性断言，本文未给来源。",
    "刘备/诸葛亮、曹操/杨修、袁绍/田丰、徐庶（P028）：以三国人物关系作类比，说明说服对象选择与自身定位，非史实论断。",
    "“万人的方言，也非天使的话语，也非来自先知讲道之能，或明白各样的奥秘，甚至并非来自全备的信，或者移山倒海的成就”（P034）：作者列举的宗教式表述，句面似有所本而正文未标出处，待外部核查。",
    "文末“爱。”（P036）：作为独立标题段的结构性收束，属修辞安排而非例证。"
   ],
   "conditions": [
    "说服效力被双重限定：“以相当大的概率在很大程度上改变他人的立场或者态度”（P001），非必然、非彻底。",
    "全篇压力论述以条件句展开：“如果你真的有了这种能力”（P002）、“如果你不打算走这条路”（P021）、“在接受痛苦的前提下”（P026）。",
    "免责被限定在法理层面：“从法理上讲，你没有任何责任”（P008），作者随即以“但是你毕竟是……原因之一”加以平衡。",
    "内疚的普遍性被表述为“无论有无过错，都无一例外”（P009）。",
    "第三条路要求严格的次序：“严格依此顺序”（P021），且志愿“绝对必要而优先”（P022）。",
    "识人标准设有门槛：“只有经过再三观察鉴定被确认的这种王者”（P028）。",
    "第三种办法的适用面被限定为“绝大多数时候”（P030），非全部情形。",
    "对说服力的否定被限定范围：否定的只是“上面两条”（P033），但所指哪两条在文中存在歧义（见未决问题）。"
   ],
   "rhetoric_and_tone": "以第二人称“你”通篇对话式论说，兼具心理分析与道德劝谕，语气由开篇的冷静分析逐渐转为训诫与信仰告白。手法包括：连续反问（“你要怎么面对？”“怎么可能因此就心安理得，毫无自责和痛苦？”）；口语提示语（“实话跟你们说——”“说得直白一点——”）；括号补注与引号强调术语（“耐久”“不问不说”“无需内疚的奴役手段”）；三国人物典故的比附；宗教语汇（上帝、奇迹、方言、先知、信、爱）；结构上把结论的最后一个字“爱”单独设为 heading 段（P036），使“它只会是出于/爱”跨段断裂，形成留白与强调。",
   "unresolved_questions": [
    "P034 的列举（万人的方言、天使的话语、先知讲道之能、明白各样的奥秘、全备的信、移山倒海的成就）句面似为宗教文本用语，正文未标出处，待外部核查；作者是否在引用某文本亦未说明。",
    "P033“仅仅只有上面两条的人”中“上面两条”具体指哪两条（口才与博闻强识？抑或前述两种方案？）存在歧义，影响该反驳的指向。",
    "文中方案计数不一致：P017“其中之一”、P019“另一种方法”、P021“只有另一条路”、P030“第三种办法”，三套编号难以对齐，需研究者厘清。",
    "“爱”未作任何定义，全文以单字标题段收束，其内涵与 P009、P034 宗教语汇的关系不明。",
    "心理咨询师督导系统的功能描述（组织庇护、同侪安慰、钝感、耐久）为作者断言，本文无来源，待外部核查。",
    "“不道德”（P024）的判定依据未给出，是宗教性还是伦理论证未说明。",
    "作者未说明自身是否属于“靠说服力为生的人”，其立场位置不明。",
    "提问为“说服他人的能力太强怎么办”，作者给出的三种办法是否穷尽，正文未作穷尽性声明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人对人是有操纵能力的，其中最主要的操纵能力就是说服力。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你才会发现这个能力本身就是一种重担。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "因为你会干预到人的命运。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你完全可能说服你侄子从理科改学文科。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "而的的确确是伸手就可能触及的果实", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "不要用“人的命运应该自己负责”来推卸责任", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "但是你毕竟是造成这种令人呼痛的重大困难的原因之一。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "令一切直接造成他人痛苦的人，无论有无过错，都无一例外要承受内疚的痛苦。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "这种说辞势必将发育成“无需内疚的奴役手段”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "因此，你不要指望“法理上没有过错”就可以逃过这种心灵的痛苦。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "但怎么可能因此就心安理得，毫无自责和痛苦？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "找寻这种“我在法理上没错”的理由对这个痛苦几乎没有消解作用。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "开口说服人，就必然要不可推卸的背负他人的命运。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "不要想逃避，因为没得逃避。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "必须有充分的、值得扛这份痛苦的理由。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "如果这一点都没体认到的人，也很难有真正的说服力。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "其中之一就是通过系统性的组织方法来加以回避和消解。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "所谓心理咨询师的督导系统，实际上就是一个借助组织庇护、同侪安慰来消解这种痛苦的机制。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "另一种方法，就是获得足够的物质补偿。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "抱团互相说服“这不是你的错”外加“适当收费”。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "靠愿赌服输甘愿承受痛苦的志愿、识别有独立人格者的眼光，辅以保守而被动的表达来管理这种痛苦——严格依此顺序。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "甘愿承受痛苦的志愿是绝对必要而优先的准备。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P023", "quote": "可以靠什么智慧摆脱这种负担。", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P024", "quote": "甚至，想要彻底摆脱这种痛苦本身是不道德的。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P025", "quote": "并且最终会迈向尝试靠彻底泯灭良知而“降低运行成本”，“提高利润”。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P026", "quote": "看人是不是能清清楚楚的知道听取别人的意见决策的责任仍然完全在自己。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P027", "quote": "完全为自己负责、听了任何意见而出了任何后果都仍然知道无人可以责怪，人就成了自己的王。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P028", "quote": "遇到刘备你才能做诸葛亮，大部分人没注意这点，ta们遇到了曹操，变成了杨修；遇到了袁绍，变成了田丰——其实这时ta们本应该做徐庶。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P029", "quote": "你如果觉得这样的人比比皆是，只会是因为你评判的标准还过于天真和宽松。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P030", "quote": "你要靠第三种办法来管理问题——就是“不问不说”。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P031", "quote": "要么只对公众而非具体的个人的问题给出意见。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P032", "quote": "你可以在很大程度上免于主动干预ta人命运的负担。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P033", "quote": "真正能撼动人心的所谓说服力，并不是来自那种舌灿莲花的口才和博闻强识的智慧。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P033", "quote": "这种警戒心常常可以无视一切雄辩，甚至压倒基本的理性判断", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P034", "quote": "真正的说服力不是来自于万人的方言，也非天使的话语，也非来自先知讲道之能", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P035", "quote": "真正能造就人的“说服”，是世界上最大的奇迹，它只会是出于", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P036", "quote": "爱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学/心理咨询", "伦理学（责任与良知）", "说服与影响", "宗教语汇与道德劝谕"],
   "issue_candidates": ["说服力的道德负担", "内疚的功能", "说服者的自我保护机制", "谁值得被说服", "不问不说的表达伦理", "真正说服力的来源"],
   "text_function_candidates": ["答疑", "经验总结", "论辩", "劝谕"],
   "object_candidates": ["说服者/心理咨询师", "被说服者", "父母与子女", "刘备", "诸葛亮", "曹操", "杨修", "袁绍", "田丰", "徐庶", "上帝"],
   "working_keywords": ["说服力", "操纵能力", "重担", "内疚的痛苦", "愿赌服输", "不问不说", "自己的王", "无需内疚的奴役手段", "爱"]
  },
  "notes": "35 段 body ＋ 1 段 heading（P036“爱。”），无图片、无引用块标记；结构上 P035 以“它只会是出于”结尾、P036 为 heading，跨段断句构成刻意的留白，已在 rhetoric_and_tone 与 content_units 中保留。P034 的宗教式列举与 P018 的督导系统描述均为作者断言且未标来源，登记为待外部核查。P033 的“上面两条”指代不明、三套方案编号不一致，已登记为未决问题。"
 },
 "c7951d41": {
  "analysis": {
   "question_context": "知乎提问：「为什么部分女性不能接受有处女情结的男人？」（Q001，属提问者，其中的“处女情结”预设出自提问者）。作者未分析该提问中的性别议题，仅以两句作概念区分式回答：把“不接受”与“不尊重”分开，并判定“尊重我”就要“接受我xxx”这种要求属于强奸罪。正文仅 2 段、41 字，无图片、无引用块。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出概念区分：“不接受”和“不尊重”是两回事", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "引述“尊重我”就要“接受我xxx”的表述，并判定其为一种强奸罪", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不接受”和“不尊重”是两回事，二者不可混同。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把“尊重我”等同于“接受我xxx”的要求，是一种强奸罪。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "存在一种主张：既然要“尊重我”，就必须“接受我xxx”——此为作者引述并否定的观点对象（“xxx”原文即以字母占位，未具体化）。", "evidence": ["E2"]}
   ],
   "argument_steps": [
    "先做概念切分：把“不接受”与“不尊重”区分为两回事（P001）。",
    "再给出否定性判定：以“尊重”为名要求“接受我xxx”，被作者定为强奸罪（P002）。",
    "全文未展开论证过程，未给出推理链条或例证。"
   ],
   "concept_usage": [
    {"term": "不接受", "meaning": "本文中被列为与“不尊重”不同的一种态度；作者未定义，也未说明其对象与限度。", "evidence": "P001", "ambiguity": "未定义，仅通过与“不尊重”的对举获得含义。"},
    {"term": "不尊重", "meaning": "与“不接受”相对举而被区分开的另一种态度；文中未给出判准。", "evidence": "P001", "ambiguity": "同上；二者的分界标准未说明。"},
    {"term": "尊重我 / 接受我xxx", "meaning": "作者引号引述的一种要求式表述：把尊重与接受某事物（以“xxx”占位）绑定。", "evidence": "P002", "ambiguity": "“xxx”是原文占位符，所指内容未交代；说话者亦未标明。"},
    {"term": "强奸罪", "meaning": "作者对该绑定式要求所作的定性用语。", "evidence": "P002", "ambiguity": "是法律意义上的罪名指认还是修辞性类比，文中未说明，也未给出构成要件。"}
   ],
   "examples_and_targets": [
    "“尊重我”就要“接受我xxx”（P002）：作者引述并否定的表述，被反驳对象；其提出者未在文中标明。",
    "提问中的“有处女情结的男人”与“部分女性”（Q001）：提问者提供的语境与主体，作者正文未提及。"
   ],
   "conditions": [
    "该判定针对的是“把尊重混同于接受”这一绑定式要求（P002），而非针对提问所指的具体人群。",
    "“xxx”为原文占位，说明作者有意不限定所指事项，判定因此被表述为一般性命题。"
   ],
   "rhetoric_and_tone": "极简短句式，不展开论证：两句独立成段，第一句为概念区分，第二句为定性判断，语气斩钉截铁、不作限定。使用引号引述被否定的表述并直接以“这是一种强奸罪”作重词定性，具有强烈的压缩式修辞效果；全文无反问、无称呼、无举例。",
   "unresolved_questions": [
    "作者正文完全未出现“处女情结”“女性”等提问关键词，两段回答与提问的具体关联需研究者解读，不能据提问补写作者主张。",
    "“不接受”与“不尊重”的分界标准正文未说明，本文只给出区分的断言。",
    "“xxx”为原文字母占位符，其实际所指（性、婚史、某项行为等）无法确定。",
    "P002 中被引述的“尊重我就要接受我xxx”未标明说话者，属作者引述的、被否定的观点对象，归属记为 opponent（提出者具体身份不明）。",
    "“强奸罪”是法律定性还是修辞类比，文中未说明；若为法律指认，其构成要件与依据需外部核查。",
    "正文过短（41 字），是否存在被截断或删节，需与原始发布版本比对。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“不接受”和“不尊重”是两回事。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "“尊重我”就要“接受我xxx”，这是一种强奸罪。", "relation": "contradicts"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["两性/情感话题", "伦理与权利边界", "语义区分（概念辨析）"],
   "issue_candidates": ["不接受与不尊重的区分", "以尊重为名的强制要求", "处女情结争议（提问语境）"],
   "text_function_candidates": ["答疑", "评论", "反驳"],
   "object_candidates": ["提问者", "被引述表述的持有者（未标明）", "部分女性（提问语境）", "有处女情结的男人（提问语境）"],
   "working_keywords": ["不接受", "不尊重", "尊重我", "接受我xxx", "强奸罪"]
  },
  "notes": "2 段正文＋提问字段，无图片。正文仅 41 字，未使用提问中的任何关键词，作者主张与提问议题之间的对应关系留待研究者判断，未作补写。P002 的引号内容归属记为被反驳观点（opponent），提出者身份正文未标明；“强奸罪”一词的用法（法律指认或修辞类比）未定，登记为待决。"
 },
 "a0bebc70": {
  "analysis": {
   "question_context": "知乎提问：「中国人和犹太人是世界上最聪明、最勤奋的民族吗，为什么二者的命运相差那么大？」（Q001，属提问者，其“最聪明/最勤奋”与“命运相差大”的预设出自提问者）。作者否定“最勤劳”的提法并质疑“民族”这一概念工具的适用性，主张中国人与犹太人已是“文明级别的实体”；文中另有“时隔多年，增补一下这个答案”（P024）标记的后续补充，转以“最成功的统治者／最成功的被统治者”重述差异。正文 34 段、1693 字，无图片、无引用块。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "答问缘起：因受邀而简要作答", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "直接否定：中国人和犹太人不是世界上最勤劳的民族", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "更确切的说法：“民族”是以岛民和山民为理想蓝本发明的漏洞百出的概念；交通原始时代偏远乡民即可构成“民族”（“陆地之岛”）", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "民族概念在民族国家崛起时吃香，恰是欧洲“陆地岛”碰撞融合、实质“民族”概念走向坟墓的开端——作者称之为上帝开的黑色玩笑", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007", "P008"], "summary": "理由：中国人与犹太人两千年前起就不再是“岛民”——犹太人失去祖国散布世界成为半个世界的“文化基础设施”，中国实现两千年总体大一统成为大半个世界的中心", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010", "P011"], "summary": "因此二者是文明级别的实体，无法用“民族”概括：接触太多太久，问题与思考中心是泛域的历史的，不能“一事一议”，故必须有更超越的原则", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013"], "summary": "与二者并肩的不是具体民族而是希腊/罗马、基督教、伊斯兰教、佛教；只有超越地域与时间看待根本利益者才能并列", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P014", "P015", "P016"], "summary": "所谓“智慧”的第一特征是高度历史自觉性；“勤劳”只是这种自觉性产生的高行动焦虑的结果，人皆按“最大限度偷懒”原则生存", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023"], "summary": "对“命运如此不同”的质疑：活着的存在命运未完结；只有短命运之间才有有限相似；须先证明“命运高度相似才是常态”才能把“如此不同”当作需额外找原因的问题；原因则显而易见（地理、邻居、气候不同）", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P024", "P025"], "summary": "增补标记：时隔多年补充，指出中国人跟犹太人之间有一个有意思的巧合，也是两个文明最本质的差异", "role": "transition"},
    {"unit_id": "U011", "paragraph_refs": ["P026", "P027"], "summary": "中国人是世界上最成功的统治者：文化积累侧重“如何有效的统治”、精通王霸之道，心态自上而下", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P028", "P029"], "summary": "犹太民族是世界上最成功的被统治者：文化积累沉淀在“如何在别人的统治下获得最大的成功”，三千余年从未成为统治性帝国，长期只是臣属、边藩、客旅与寄居者", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P030", "P031", "P032"], "summary": "二者互为最深刻的了解者（有时超过对方对自己的了解），但“作为对手的了解”毕竟不是对手自己", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P033", "P034"], "summary": "归结：二者是同一种游戏里两个角色强化到极致；中国的悲剧来自向下管理的失败，犹太人的灾难来自向上管理的失败；末句以“顺着这个视角，再去看……差异”收束而未展开", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "中国人和犹太人不是世界上最勤劳的民族。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "更确切地说，“民族”这个概念是以岛民和山民为理想蓝本发明出来的漏洞百出的概念；在交通非常原始落后的时代，稍处偏远的偏乡之民就可能构成一个“民族”，因为那实际上是一种“陆地之岛”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“民族”概念在民族国家崛起时之所以吃香，是上帝给人类开的黑色玩笑——这恰恰是欧洲“陆地岛”开始碰撞融合、边界模糊、实质“民族”概念走向坟墓的开端。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国人和犹太人从两千年前开始就不再是任何意义上的“岛民”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "犹太人是失去了祖国、散布到全世界，自己成了半个世界的“文化基础设施”；中国则实现了两千年的总体大一统，成了大半个世界的中心。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是两个文明级别的实体，无法用“民族”来概括；因与其他文化接触太多太久，形成了远不同于一般“民族”实体的自我体认和行事逻辑。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "它们面对的问题与思考的中心不是局域的、当即的，而是泛域的、历史的；因为它们不能搞“一事一议”，交往对象与事务复杂度远超一般“海陆岛民”。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "它们的生存现状要求它们必须有更超越的原则。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与犹太“民族”、华夏“民族”并肩的，根本不是什么壮族、回族、塞尔维亚族、图西族，而是希腊/罗马、基督教、伊斯兰教、佛教；只有同样以超越地域、超越时间的心态看待自己根本利益的存在才能与这两者并列。", "evidence": ["E9", "E10"]},
    {"claim_id": "C010", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "有人会说这两个民族“有智慧”（作者转述他人说法，说话者未标明）。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对上述“智慧”的解释：其第一个最明显的特征就是高度的历史自觉性。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“勤劳”，只是拥有了这种历史自觉性所产生的一种比较高的行动焦虑的结果。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "谁都是按照“最大限度偷懒”原则生存，谁也不会凭空“勤劳”；他们其实一点也不勤劳，只是比别人更清楚地知道和记得低于这个限度的勤劳会倒多大霉，于是再懒一些会产生不安。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "“命运如此不同”这一提法更难成立：还活着的东西命运还没完，相不相同还难说。", "evidence": ["E14"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有命运足够短的两者之间的命运可以有有限的相似——比如两个人类的一生。", "evidence": ["E15"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对命运历程长到三四千年的存在，必须先找出几个命运相似的存在，先证明“命运高度相似才是常态”，才能把“如此不同”定义为一个需要额外找原因的问题。", "evidence": ["E16"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两者命运不同的原因太明显：地理条件不同、邻居不同、气候不同等。", "evidence": ["E17"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "（增补部分）中国人跟犹太人之间有一个非常有意思的巧合，也是这两个文明最本质的差异。", "evidence": ["E18"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国人是世界上最成功的统治者，所有文化积累都侧重于“如何有效的统治”，精通王霸之道。", "evidence": ["E19"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "整个中华民族的心态都是自上而下的，乃至人人都会不假思索地考虑“如果换了我来当皇帝／领袖／总经理，我要如何做不同的统治／领导／管理”的问题。", "evidence": ["E20"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "犹太民族是世界上最成功的被统治者，所有文化积累都沉淀在“如何在别人的统治下获得最大的成功”。", "evidence": ["E21"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "犹太民族三千多年的历史从来没有成为过统治性的帝国，即使作为独立国家也只是他国臣属、边藩；两千年里连国家都没有，只是客旅和寄居者。", "evidence": ["E22"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "最成功的统治者恰恰是最了解被统治者的人（甚至超过其他被统治者），最成功的被统治者也恰恰是最了解统治者的人（甚至超过其他统治者）。", "evidence": ["E23"]},
    {"claim_id": "C024", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "有时候在这两者之间，对方对自己的了解甚至有连自己都不及之处。", "evidence": ["E24"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种“作为对手的了解”尽管比所有外人都深刻，但毕竟不是对手自己。", "evidence": ["E25"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两个民族的突出特性是同一种游戏里两个不同角色强化到极致的表现：中国的悲剧总是来自向下管理的失败，犹太人的灾难总是来自向上管理的失败。", "evidence": ["E26", "E27"]}
   ],
   "argument_steps": [
    "先交代答问缘起（受邀作答），表明简要作答（P001-P002）。",
    "直接否定提问中的“最勤劳”提法（P003）。",
    "改为质疑概念工具：指出“民族”是以岛民/山民为蓝本发明的概念（P004）。",
    "补充该概念的历史反讽：其走红之时正是实质“民族”概念走向坟墓之始（P005）。",
    "以反问过渡，给出理由：这两者两千年前起已非“岛民”（P006-P008）。",
    "推出性质判断：它们是文明级别实体，问题与原则都是泛域、历史、超越的（P009-P011）。",
    "给出并列物作横向定位：希腊/罗马、基督教、伊斯兰教、佛教（P012-P013）。",
    "解释“智慧”的实指是历史自觉性，并把“勤劳”还原为行动焦虑（P014-P016）。",
    "转而对提问的第二半作方法论反驳：先质疑“命运不同”这一问题的成立条件（P017-P020）。",
    "以连续反问否定“相同”的可比性，并归因于地理、邻居、气候（P021-P023）。",
    "以“时隔多年，增补一下这个答案”另起一段（P024），提出新的核心对照：统治者与被统治者（P025-P029）。",
    "深化为相互了解的不对称与限度（P030-P032）。",
    "归结为同一种游戏的两个角色，并给出“向下管理/向上管理”的失败类型（P033）。",
    "以“顺着这个视角，再去看中国人和犹太人的差异”结束，未展开（P034）。"
   ],
   "concept_usage": [
    {"term": "民族", "meaning": "本文中被质疑其适用性的概念：以岛民和山民为理想蓝本发明的、漏洞百出的概念；在交通原始时代，偏远乡民即可构成一个“民族”，即“陆地之岛”。", "evidence": "P004", "ambiguity": "未给出替代概念的操作性定义，也未说明“民族”与“文明级别实体”的判定边界。"},
    {"term": "陆地之岛 / 岛民 / 海陆岛民", "meaning": "以地理隔绝为条件的封闭人群；作者用它解释“民族”概念的产生条件，并称中国人与犹太人两千年前起已非此类。", "evidence": "P004", "ambiguity": "“岛”是地理还是文化隐喻，文中两种用法并存。"},
    {"term": "文明级别的实体", "meaning": "作者用以替代“民族”的定位：接触太多太久、问题与思考中心是泛域与历史的实体，可与希腊/罗马、基督教、伊斯兰教、佛教并列。", "evidence": "P009", "ambiguity": "概念未定义，其判定标准与“文明”一词的通行用法关系未说明。"},
    {"term": "文化基础设施", "meaning": "作者对散布世界的犹太人所起作用的一种比喻性定位（“半个世界的‘文化基础设施’”）。", "evidence": "P008", "ambiguity": "比喻的具体所指（语言、宗教、金融、学术等）未展开。"},
    {"term": "历史自觉性", "meaning": "作者所称“智慧”的第一个最明显特征；也是“勤劳”这种行动焦虑的来源。", "evidence": "P014", "ambiguity": "未说明其形成机制与衡量方式。"},
    {"term": "最大限度偷懒原则", "meaning": "作者主张的一般行为原则：没有人凭空勤劳，只是知道低于某限度的勤劳会倒大霉而不安。", "evidence": "P016", "ambiguity": "该原则被表述为普适命题，文中未给依据。"},
    {"term": "最成功的统治者 / 最成功的被统治者", "meaning": "增补部分的核心对照：中国人侧重“如何有效的统治”、精通王霸之道；犹太人的文化积累沉淀在“如何在别人的统治下获得最大的成功”。", "evidence": "P026", "ambiguity": "“最成功”的比较标准与衡量口径未给出。"},
    {"term": "向下管理 / 向上管理", "meaning": "作者用于概括两种失败类型的框架：中国的悲剧来自向下管理的失败，犹太人的灾难来自向上管理的失败。", "evidence": "P033", "ambiguity": "两个术语的内涵与失败机制未展开，末段亦未继续解释。"}
   ],
   "examples_and_targets": [
    "北大出版社邀请回答（P001）：答问缘起的机构性说法，属作者自述，本文未给凭据，待外部核查。",
    "壮族、回族、塞尔维亚族、图西族（P012）：作者作为对照面列举的具体民族，用于说明与二者“并肩”的并非此类实体。",
    "希腊/罗马、基督教、伊斯兰教、佛教（P012）：作者给出的可并列实体，属作者判断而非引述。",
    "“如果换了我来当皇帝／领袖／总经理”（P027）：以角色类比说明“自上而下”的心态。",
    "犹太民族三千多年的历史叙述（P029）：作者的历史断言（从未成为统治性帝国、长期为臣属、边藩、客旅、寄居者），未给史料来源，待外部核查。",
    "“上帝给人类开的一个黑色玩笑”（P005）：宗教语汇的修辞性表述，非事实断言。",
    "“两个人类的一生”（P019）：用于说明“命运可有有限相似”的类比。"
   ],
   "conditions": [
    "“民族”概念的产生被限定在“在交通非常原始落后的时代”这一条件下（P004）；其走红被限定在“民族国家崛起的时候”（P005）。",
    "“半个世界”的表述被作者自己加括号限定为“虽然在绝大多数时候都只是半个世界”（P010）。",
    "方法论反驳设有前提：“对命运历程长到三四千年的存在”必须先证明“命运高度相似才是常态”（P020）。",
    "相似性被限定为“只有命运足够短的两者之间”且仅“有限的相似”（P019）。",
    "相互了解的深度带频率限定：“有时候在这两者之间”（P031）。",
    "犹太史的表述带让步限定：“即使作为独立国家的阶段、也只是其它国家的臣属、边藩”（P029）。",
    "文本含版本/增补限定：“时隔多年，增补一下这个答案”（P024），但未标明增补起止。"
   ],
   "rhetoric_and_tone": "以答问口吻开篇（“居然是北大出版社邀请回答？那就简单答一答吧。”），随后转入概念批评与宏观历史论断，语气自信、带调侃与断言色彩。修辞手法：密集反问（“这里你应该看出来为什么说……了吧？”“否则怎么个‘相同’起来法……”“命运怎么相同法？”）；引号高频标示术语与成句（“民族”“陆地之岛”“文化基础设施”“最大限度偷懒”“最成功的统治者”）；比喻与宗教语汇（黑色玩笑、走向坟墓、客旅和寄居者）；以“第一/第二”分点（P018、P019）组织反驳。结构上分为两个时段：前半回应“聪明/勤劳/命运”，P024 起为“时隔多年”的增补，改以统治者/被统治者重述差异；末段以未展开的引导句收束。",
   "unresolved_questions": [
    "P024“时隔多年，增补一下这个答案”表明文本含后续添加内容，但未标明增补的起止范围；语料 updated_at 为 2025-11-21，与发文时间相差多年，版本关系需复核。",
    "末段 P034“顺着这个视角，再去看中国人和犹太人的差异。”未展开即结束，是否原文被截断或作者刻意留白，需与原始发布版本比对。",
    "“居然是北大出版社邀请回答？”所述机构与邀请事实待外部核查，本文未给凭据。",
    "“最成功的统治者／最成功的被统治者”的比较标准（成功如何衡量、在何种范围内比较）未给出。",
    "“文明级别的实体”未定义，与“民族”“文明”“宗教”的界限未说明；P012 把民族与宗教、古代文明并列的判准亦未说明。",
    "“半个世界”“大半个世界的中心”为修辞性量化，无数据支撑。",
    "犹太民族三千年历史叙述（无统治性帝国、长期臣属边藩、客旅寄居者）为作者概括，未引史料，待外部核查。",
    "“上帝给人类开的一个黑色玩笑”（P005）所用的宗教语汇与作者立场的关系未交代。",
    "提问所问“最聪明”一项，作者仅在 P006 的反问中以“不是最勤劳智慧的民族”一并带过，未单独论证“聪明”。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "中国人和犹太人不是世界上最勤劳的民族。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "这是因为“民族”这个概念是以岛民和山民为理想蓝本发明出来的漏洞百出的概念。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "这只是上帝给人类开的一个黑色玩笑", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "因为这俩从两千年前开始，就不再是任何意义上的“岛民”了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "自己成了半个世界的“文化基础设施”", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "这是两个文明级别的实体，你无法用“民族”来概括它们。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "面对的问题、思考的中心，都不是局域的、当即的，而是泛域的、历史的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "它们的生存现状要求它们必须有更超越的原则。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "而是希腊/罗马、基督教、伊斯兰教、佛教。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "才能与这两者并列。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "这就是为什么有人会说这两个民族“有智慧”——这个所谓的“智慧”的第一个最明显的特征就是高度的历史自觉性。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "只是拥有了这种历史自觉性所产生的一种比较高的行动焦虑的结果。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "谁都是按照“最大限度偷懒”原则生存的，谁也不会凭空“勤劳”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "还活着的东西命运还没完，相不相同还难说。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "只有命运足够短的两者之间的命运可以有有限的相似", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "才能把“如此不同”定义为一个需要额外找到原因的问题。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "地理条件不同、邻居不同、气候不同……", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P025", "quote": "也是这两个文明最本质的差异。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "中国人是世界上最成功的统治者，所有的文化积累都侧重于“如何有效的统治”，精通王霸之道。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P027", "quote": "整个中华民族的心态都是自上而下的", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P028", "quote": "而犹太民族则是世界上最成功的被统治者。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P029", "quote": "犹太民族整个三千多年的历史从来没有成为过统治性的帝国", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P030", "quote": "最成功的统治者恰恰是最了解被统治者的人", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P031", "quote": "对方对自己的了解甚至有连自己都不及之处。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P032", "quote": "这种“作为对手的了解”尽管会比所有外人都深刻，但是却毕竟不是对手自己。", "relation": "qualifies"},
    {"key": "E26", "paragraph_id": "P033", "quote": "其实是同一种游戏里两个不同的角色强化到了极致的表现。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P033", "quote": "中国的悲剧，总是来自于向下管理的失败；而犹太人的灾难，总是来自于向上管理的失败。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P024", "quote": "时隔多年，增补一下这个答案。", "relation": "context"},
    {"key": "E29", "paragraph_id": "P001", "quote": "居然是北大出版社邀请回答？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["民族与文明理论", "历史比较", "文化批评", "国际/文明关系"],
   "issue_candidates": ["“民族”概念的适用性", "中国人/犹太人是否最聪明勤劳", "两群体命运差异的可比性", "统治者与被统治者的文化积累", "向下管理与向上管理"],
   "text_function_candidates": ["答疑", "评论", "论辩", "概念批评"],
   "object_candidates": ["中国人", "犹太人", "中华民族", "犹太民族", "北大出版社", "壮族", "回族", "塞尔维亚族", "图西族", "希腊/罗马", "基督教", "伊斯兰教", "佛教"],
   "working_keywords": ["聪明族", "陆地之岛", "民族概念", "文明级别的实体", "历史自觉性", "最大限度偷懒", "最成功的统治者", "最成功的被统治者", "向下管理", "向上管理"]
  },
  "notes": "34 段正文＋提问字段，无图片、无引用块、无结构缺口（divergence=false）。文本含 P024“时隔多年，增补一下这个答案”的增补标记，增补起止范围未标明（语料 updated_at 2025-11-21，晚于发文多年），已在 notes 与 unresolved_questions 登记为版本问题。P014 的“有人会说……‘有智慧’”为转述他人说法（claim_type=author_reported，attribution=unknown），作者对“智慧”的解释单列为 C011，未混同。末段 P034 未展开，是否截断待版本复核。"
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
