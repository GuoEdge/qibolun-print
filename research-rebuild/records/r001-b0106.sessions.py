# -*- coding: utf-8 -*-
"""批次 r001-b0106 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0106.sessions.py            # 写 out/r001-b0106.out.jsonl
  python3 records/r001-b0106.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0106"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0106.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "ab700c31": {
  "analysis": {
   "question_context": "提问者问的是 3 月 29 日美国宣布暂停与缅甸所有贸易往来会带来哪些影响（Q001）。作者没有回应这一具体事件，而是借题转入一般性论辩：先为“军政府”这一统治形态作合理性辩护（对跳过近代化阶段被直接拉入现代的古国而言，军队成为统治支柱是逻辑必然），再落到缅甸，论证民选政府离开军方支持无法运转、“民意支持”不能自动转化为秩序。全文是作者对军政府评价问题的正面立论与对流行谴责话术的反驳；提问者立场（对美国制裁影响的关切）未进入正文。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "开篇断言军政府被妖魔化；对跳过近代化阶段、被直接从古代社会形态拉入现代的古国，最先被系统现代化的军队成为统治结构支柱是逻辑必然；这是逻辑问题，不能用民粹主义、选票主义否定。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "理由：几百万几千万国民中只有几千几万人受过系统教育、有组织与纪律、有斗争经验；其余人识字率堪忧，近乎没有组织经验、纪律训练和行政经验。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "不让军人执政，就只剩脱离群众的海归或不识字的平民执政；军人未必是更坏的选择，甚至军政府时期往往经济发展较好、治安较好、民族较为独立。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011"], "summary": "反驳“军政府天生邪恶”：该说法没有超出宣传构建的论据；承认军政府为维持统治造成流血，但认为没有充分论述能证明存在有把握避免流血的“理想政体”；讥讽这类批评是站着说话不腰疼的马后炮。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "明确限定：不是说军政府一定更好，只是说并不一定更坏，尤其对国民教育水平低下、全局意识和组织经验匮乏的国家。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "转入缅甸：军政府传统有深层原因；民选政府在国内唯一有完善组织性的系统力量不衷心支持的前提下，根本没有能力维持基本运转。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "理由：军方可以消极抗议、以退为进、划地自保；完全离开军方，连足够的上过高中的派出所所长和交通警察都凑不齐。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "反驳民盟：把“民意支持”看得太万能；不能以有效组织把民意转化为秩序，民意一夜之间就能变成另一种东西（水能载舟，亦能覆舟）；与军队势不两立时，即便军队只保持冷漠中立，也没有足够的非军队精英维持秩序；其手中力量闹事败事有余、成事不足。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022", "P023"], "summary": "结论：接管需要足够的人才能接管；靠外部力量夺权，维持局面的租金支付不起，且是按小时论亿的价位。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "军政府这种存在被妖魔化了，这是作者的总体判断。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对跳过近代化阶段、直接从古代社会形态被拉入现代的古国，出于独立和安全本能而最先被系统现代化的军队成为统治结构支柱，是逻辑必然。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是逻辑问题，不能用民粹主义、选票主义否定其现实合理性。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "国民中只有极少数人具备系统教育、系统组织、严格纪律与斗争经验，其余人识字率堪忧且几乎没有组织、纪律与行政管理经验。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不让军人执政，就只能是脱离群众的海归或不识字的平民执政，作者认为后者不可能实现。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "军人未必是更坏的选择；作者并称客观事实上军政府执政时往往经济发展较好、治安较好、民族较为独立。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的一种流行说法：“军政府天生邪恶”。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为“军政府天生邪恶”没有超出宣传构建之上的额外论据。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者承认军政府往往为维持统治造成流血，但认为没有充分的论述能证明存在一个有把握避免这些流血事件的“理想政体”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把上述批评讥为站着说话不腰疼的马后炮。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者限定：不是说军政府一定更好，只是说不一定更坏，尤其对国民教育水平普遍低下、全局意识和组织经验匮乏的国家。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "缅甸根深蒂固的军政府传统有其深层原因。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民选政府在失去国内唯一有完善组织性的系统力量衷心支持的前提下，根本没有能力维持基本运转。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "军方大可以全面消极抗议、以退为进、甩手不管、划地自保，让想全面掌权者自己去掌。", "evidence": ["E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "完全离开军方，连足够的上过高中的派出所所长与交通警察都凑不齐。", "evidence": ["E19"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为民盟把“民意支持”看得太万能：不能以有效组织把民意转化为秩序，民意可能一夜之间变成另一种东西。", "evidence": ["E20", "E21"]},
    {"claim_id": "C017", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者以“水能载舟，亦能覆舟”这一成语式引语说明民意既可支持也可推翻政权；文中未注明出处。", "evidence": ["E22"]},
    {"claim_id": "C018", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在与军队势不两立的前提下，哪怕军队不拆台、只保持冷漠中立，民盟也不可能有足够的非军队精英建立和维持秩序。", "evidence": ["E23"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称民盟手中的力量闹事、败事有余，成事却远远不足。", "evidence": ["E24"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "接管需要足够的人才能接管得了；靠外界力量夺权，其维持局面的租金支付不起。", "evidence": ["E25", "E26", "E27"]}
   ],
   "argument_steps": [
    "前提/定义：把论述对象限定为跳过近代化阶段、从古代社会形态被直接拉入现代的古国。",
    "通则主张：这类国家中最先被系统现代化的军队成为统治结构支柱，是出于独立与安全本能的逻辑必然。",
    "理由：全国只有极少数人具备系统教育、组织、纪律与斗争经验，多数人连识字与行政管理经验都不具备。",
    "二难：不让军人执政，就只能由脱离群众的海归或不识字的平民执政。",
    "比较：军人未必更坏，甚至军政府时期往往经济、治安、民族独立表现较好。",
    "反驳对方：驳“军政府天生邪恶”缺乏超出宣传构建的论据。",
    "让步：承认军政府为维持统治造成流血；但主张没有充分论述证明存在能避免流血的“理想政体”。",
    "讥讽：把这类批评称为站着说话不腰疼的马后炮。",
    "限定：不是说军政府一定更好，只是不一定更坏，尤其对教育水平低、组织经验匮乏的国家。",
    "落到缅甸：军政府传统有深层原因；民选政府失去军方衷心支持就无法维持基本运转。",
    "理由：军方可以消极抗议、划地自保；离开军方连基层执法人员都凑不齐。",
    "反驳民盟：民意支持被看得太万能，无组织则民意可变（水能载舟，亦能覆舟）；缺非军队精英；手中力量成事不足。",
    "结论：接管需要足够的人；靠外部力量夺权，维持局面的租金按小时论亿，无法支付。"
   ],
   "concept_usage": [
    {"term": "军政府", "meaning": "本文指以被系统现代化的军队为统治结构支柱的政权形态，作者视其为特定历史断层期的产物，而非单纯的价值贬义词。", "evidence": "P001", "ambiguity": "作者未区分不同国家、不同时期的军政府类型，也未给出判定标准。"},
    {"term": "逻辑必然", "meaning": "在“跳过近代化、被直接拉入现代”这一前提下，军队执政是唯一可行的统治支柱，作者称之为逻辑问题而非价值偏好。", "evidence": "P002", "ambiguity": "“逻辑必然”的推理前提（独立与安全本能）未展开论证。"},
    {"term": "断层期", "meaning": "指这些军政府所担当的社会矛盾激烈而复杂的转型时期。", "evidence": "P010", "ambiguity": "未说明断层期的起止与判定标准。"},
    {"term": "民意支持", "meaning": "本文指民盟所依赖的民众拥护；作者认为它必须经有效组织转化为秩序才有用。", "evidence": "P017", "ambiguity": "“富有成果的秩序”具体指什么未界定。"},
    {"term": "系统力量", "meaning": "指国内唯一有完善组织性的力量，本文语境下即军方。", "evidence": "P014", "ambiguity": "“唯一”是作者的断言，未给出比较对象与依据。"},
    {"term": "海归们", "meaning": "本文指完全脱离群众、从“天”而降、甚至不熟悉本族语言文化的受西式教育者。", "evidence": "P007", "ambiguity": "未指明具体人物或群体。"}
   ],
   "examples_and_targets": [
    "缅甸军政府传统（P013）：作为作者论点的主要现实对象，属作者论据与论述对象，非外部已证实事实。",
    "民盟与“民意支持”（P017、P019）：作为被反驳对象。",
    "军方“全面消极抗议、以退为进、甩手不管、划地自保”（P015）：作者设想的反事实情景，用作论证手段。",
    "“连足够的上过高中的派出所所长都凑不齐，连交通警察恐怕都凑不够”（P016）：夸张化的修辞论据。",
    "“海归们执政”（P007）：历史类比与修辞材料。",
    "“水能载舟，亦能覆舟”（P018）：引语式修辞材料，文中未注明出处。",
    "“按小时论亿的价位”（P023）：夸张修辞，指外部力量维持局面的租金。",
    "“军政府天生邪恶”（P009）：被引述并反驳的流行说法。"
   ],
   "conditions": [
    "限定对象：跳过近代化阶段、直接从古代社会形态被拉入现代的古国（P002）。",
    "限定场景：以这些军政府所担当的断层期社会矛盾之激烈、之复杂为背景（P010）。",
    "适用范围强调：尤其对国民教育水平普遍低下、全局意识和组织经验普遍匮乏的国家（P012）。",
    "前提条件：民选政府失去国内唯一有完善组织性的系统力量衷心支持（P014）。",
    "前提条件：在与军队势不两立的前提下；即便军队不拆台、只保持冷漠中立（P019）。",
    "隐含条件：接管需要足够的人手，靠外界力量夺权需支付维持局面的租金（P021、P022）。"
   ],
   "rhetoric_and_tone": "整体为论辩与辩护语气，多用断言与口语化插入语（“说实话”“说得不好听一点”“说得尖刻点”）。反问与设问制造压迫感（“不是吗”“你打算拿什么支付？”）。有夸张（连交通警察都凑不够、按小时论亿）、讥讽与训诫（“站着说话不腰疼的马后炮”）。第二人称“你”直接指向论敌与读者，形成对峙结构；用“ta们”指代民盟一方，带轻蔑色彩。引语方面引述“军政府天生邪恶”“民意支持”并加以反驳，另引“水能载舟，亦能覆舟”作修辞支撑。结构上先立通则（P001—P012），再落到缅甸个案（P013—P023），末尾以租金设问收束。",
   "unresolved_questions": [
    "正文完全未回应提问所问的美国暂停对缅贸易往来及其影响，属借题发挥，无法据本篇判断作者对该事件的看法。",
    "“几百万几千万国民，只有这么几千几万人”等数量断言无数据来源与年份。",
    "P008 称军政府执政时“往往经济发展较好、治安较好、民族较为独立”，未指明具体国家、时期与比较基准。",
    "P007“海归们”是否指向缅甸具体政治人物或群体，文中未说明。",
    "P018“水能载舟，亦能覆舟”未注明出处，属成语式引用。",
    "P023“按小时论亿的价位”所指的支付主体与租金内容未具体化。",
    "全文未给出“军政府”“民选政府”的判定标准，也未讨论军人执政的其他代价（如人权、法治），结论边界不明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "军政府这种存在，说实话是被妖魔化了的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "出于独立和安全的本能而被最先系统现代化的军队是逻辑必然的统治结构的支柱。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这是逻辑问题，不能用民粹主义、选票主义否定的现实合理性问题。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "只有这么几千几万人有系统教育、有系统组织、有严格纪律、有斗争经验", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "连识字率都堪忧。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "近乎没有组织经验、没有纪律训练、没有任何行政和管理经验。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "总之是不可能让普遍不识字的平民老百姓真的自己执政。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "军人未必是更坏的选择。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P008", "quote": "可以说客观事实上反而是军政府执政时往往反而是经济发展较好，整体治安较好、民族较为独立的时期。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "“军政府天生邪恶”坦白说没有什么超出宣传构建之上的额外论据。", "relation": "contradicts"},
    {"key": "E11", "paragraph_id": "P010", "quote": "的确，军政府往往为了维持统治造成流血。", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P010", "quote": "实际上根本没有任何充分的论述可以证明存在一个“理想的政体”真的有把握避免那些流血事件。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "那都是些站着说话不腰疼的马后炮。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "这不是说军政府一定更好，只是说军政府并不一定更坏", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P012", "quote": "尤其是对国民教育水平普遍低下、全局意识和组织经验普遍匮乏的国家，尤其如此。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P013", "quote": "缅甸有如此根深蒂固的军政府传统，还有自己的深层原因。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "民选政府实际上根本没有能力在失去国内唯一有完善组织性的系统力量衷心支持的前提下维持基本运转。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P015", "quote": "军方大可以全面消极抗议，以退为进，甩手不管，划地自保", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "完全离开了军方，你连足够的上过高中的派出所所长都凑不齐，连交通警察恐怕都凑不够。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P017", "quote": "民盟把“民意支持”看得太万能了。", "relation": "contradicts"},
    {"key": "E21", "paragraph_id": "P017", "quote": "不能以有效的组织将民意转化为富有成果的秩序，被大混乱刺激得大失所望的民意一夜间就能完全变成另一种东西。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P018", "quote": "水能载舟，亦能覆舟。", "relation": "context"},
    {"key": "E23", "paragraph_id": "P019", "quote": "在与军队势不两立的前提下，哪怕军队不拆台，只是保持冷漠中立，民盟也不可能有足够的非军队的精英来建立和维持这种秩序。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P020", "quote": "ta们手里的这些力量，闹事、败事有余，成事却远远不足。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P021", "quote": "你也要有足够的人去接管才能接管得了啊。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P022", "quote": "这些力量替你维持局面的租金你打算拿什么支付？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P023", "quote": "那可是按小时论亿的价位。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治学", "国际政治", "东南亚研究", "政体比较"],
   "issue_candidates": ["军政府合理性", "缅甸政局", "民选政府与军队关系", "民意与组织能力", "美国对缅制裁"],
   "text_function_candidates": ["论辩", "评论", "答疑"],
   "object_candidates": ["军政府", "缅甸", "民盟", "军方", "美国", "海归群体", "平民"],
   "working_keywords": ["军政府", "断层期", "民意支持", "系统力量", "组织性", "海归", "水能载舟亦能覆舟", "租金"]
  },
  "notes": "无图片，正文已全文读完。提问问的是美国暂停对缅贸易往来的影响，正文未涉及该事件，属借题立论，需在后续研究中标出答非所问。正文含多处无出处的数量与比较断言（几百万几千万、几千几万、按小时论亿），需外部核查。provenance/superseded 均为 null。"
 },
 "45d0fb61": {
  "analysis": {
   "question_context": "提问者问“工厂现在为什么招不到工人？”（Q001）。作者的回应不是补充“待遇差”这一常见解释，而是反驳它：先概述站内多数答案及其进一步推论（招不到人因待遇差；待遇差因制造业不赚钱），再指其把问题看反——中国制造业一直很赚钱，正因钱太好赚才不必靠提高待遇招人，“招不到人”是经营者的一种选择而非意外苦恼。文章后段以评论区一个疫情物资订单实例和利润率算术支持“利润率低却实际很赚钱”的判断。提问者的问因未被质疑，作者与提问者的分歧在于解释方向。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "概述站内多数答案：招不到工人是因为待遇太差，并有人往前推一步说待遇差是因为制造业不赚钱；作者断言这套看似顺畅的逻辑并不对，是把问题看反了。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "中国制造业（含外资、港资、台资）一直在赚钱甚至很赚钱；恰恰因为钱太好赚，不提高待遇也不妨碍赚钱，所以才“招不到工人”；赚不赚钱与是否提高招工吸引力、是否提高劳动力饱和度没有直接关系。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "对无需重度培训的人力资源，“忍受旺季人手不足”是“享受淡季低人力成本”的自然代价；季节性低技能劳动密集型企业认为“平时不养人”远比“忙时不缺人”重要；越这样赚钱越说明策略正确，没有理由改变数十年检验过的经验。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "澄清“中国制造业强”的两层含义：不是来料加工电子组装厂产量大，而是装备制造、重型机械、化工机械等核心部门门类齐全技术高超；简单制造部门也强，但强在劳动者的基础教育、文化素质、对劳动纪律的文化兼容性以及平均教育与社会发展水平，由此提供招之即来的优质劳动力。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "被搬迁到中国的生产体系建立在“临时雇佣军”前提上，以减轻“精锐常备军”的运营压力；淡季机器不发工资、厂房在郊区开发区、运营成本近乎为零；设备可盘给下家，开厂真正的硬成本只是押金；大成本只在接到大订单时发生。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029"], "summary": "平时养一批人等活会被客户看到并恶意压价；作者以厂主口吻说明“极度缺人”意味着不愁生存或业务很饱，所以是客户需要出足够价钱说服厂方去招人；价钱不够宁可空厂打牌，价钱到位才愁不好招人，这是“甜蜜的负担”；结论：“招不到人”是一种选择，不是意外的苦恼。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "转引评论区一个“去年工厂接上海外贸公司疫情物资订单”的实例，并用算术解释“利润率低”为何“赚钱”：1800 万货、成本 1500—1600 万、利润率 12.5%，老板三个月赚 200 万；即便 1600 万成本全为年息 15% 的贷款、三个月摊 3.6%，实际利润率仍为 (12.5-3.6)/3.6 = 247%。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "老板对外算账只算 200 万/1600 万再减 3.6% 贷款成本，哭称只赚百分之几、剩下九个月没活干；实际上即便借年利 24% 的非法借贷仍有 108% 实际利润，借 32% 年利高利贷仍有 56% 利润；风险在于客户花样或生产纰漏导致违约，但要到一百万都摆不平的窟窿才不赚钱。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054"], "summary": "民间制造行业有宗族、乡谊、联姻的连环救命网络（前提是没坑过人、家在村里住得久）；大窟窿几率不高，真倒闭多因厂主染黄赌毒、家庭变故等且名声败坏无人愿救；喊不赚钱而关厂的多半是子女出国、自己有序撤退；设备功能完好还能转卖给去越南、孟加拉、老挝、缅甸开厂的同行；家风严谨、信用良好、正经干活的一般过得不差；末句反问“世界第一制造业大国，真有那么惨”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "站内多数答案的说法：工厂招不到工人是因为工厂待遇太差，其进一步版本是“待遇太差是因为制造业不赚钱”。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为“不赚钱，所以待遇差，所以招不到人”的逻辑看似顺畅其实不对，是把问题看反了。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国制造业（含在华外资、港资、台资企业）一直在赚钱，甚至可以说是很赚钱。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恰恰因为钱太好赚，好赚到不需要特别提高工人待遇也不妨碍赚钱，所以才“招不到工人”。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "企业赚不赚钱，与其是否把赚到的钱投在提高招工吸引力上、是否提高劳动力饱和度，都没有直接关系。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对无需重度培训的人力资源而言，“忍受旺季的人手不足”是“享受淡季的低人力成本”的自然代价。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对季节性、低劳动技能要求的劳动密集型企业，“平时不养人”远比“忙时不缺人”重要。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "赚到再多钱也没必要改变这个完全合理的经营策略；越这样赚钱越说明策略正确，没有理由改变经过数十年检验的赚钱经验。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说中国制造业强，不是说来料加工电子组装厂产量大，而是指装备制造、重型机械、化工机械等核心部门门类齐全、技术高超。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "相对简单的制造部门也强，但不是强在生产技术，而是强在人员的基础教育、文化素质、对劳动纪律的文化兼容性以及平均教育与社会发展水平。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述因素为这类厂家提供大量只需基本培训即可合格、讲解规矩即可遵守的优质劳动力，取之不尽、招之即来，赋予其生产架构极大经营优势。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被搬迁到中国的生产体系本身建立在“用临时雇佣军完成”这一前提上，以减轻“精锐常备军”固有的沉重运营压力。", "evidence": ["E19", "E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "淡季机器不需要发工资，厂房在大郊区开发区、地价便宜或有政策优惠，运营成本近乎为零，已经立于不败之地。", "evidence": ["E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "厂里的设备势头不好时可以盘给下家，开一个厂真正的硬成本其实只是一笔押金，退出时扣折旧归还。", "evidence": ["E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正发生大成本的时候，一定是接到大订单的时候。", "evidence": ["E24"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平时养着一大批人等活干，光被客户看到就会被恶意压价。", "evidence": ["E25"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以厂主口吻说明：“极度缺人”要么说明不开工也不愁生存，要么说明业务很饱，因此是客户需要拿出足够价钱来说服厂方招人，而不是厂方求客户续命。", "evidence": ["E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "价钱不够，宁可空着厂子每天打牌；价钱到位、钱到账才需要愁“不好招人”，而这是“甜蜜的负担”。", "evidence": ["E27", "E28"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：“招不到人”是一种选择，不是一种“意外的苦恼”。", "evidence": ["E29"]},
    {"claim_id": "C020", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者转引评论区一个典型事例：某工厂接上海外贸公司疫情物资订单，3 个月出 1800 万货，从零开始临时搭产线、七八百人全为劳务派遣、两班倒，订单完成后老板提了台卡宴。", "evidence": ["E30", "E31"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以该例算账：1800 万货的成本约 1500—1600 万，利润率 12.5%，但老板三个月赚 200 万；即便 1600 万全为贷款、按年息 15% 摊三个月 3.6%，实际利润率为 (12.5-3.6)/3.6 = 247%。", "evidence": ["E32", "E33", "E34", "E35"]},
    {"claim_id": "C022", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者转述厂主对外的算账方式：算的是 200 万/1600 万再减去 3.6% 贷款成本，并抱怨只赚百分之几、剩下九个月完全没活干。", "evidence": ["E36", "E37"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实际上即便借年利 24% 的非法借贷，只要按期准时结款仍有 (12.5-6)/6 = 108% 的实际利润；即便借 32% 年利的高利贷也仍有 56% 的利润。", "evidence": ["E38", "E39"]},
    {"claim_id": "C024", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "风险在于客户玩花样或自身生产出纰漏导致违约，那时确实倒霉；但有 56% 实际利润顶着，要到捅出一百万都摆不平的窟窿才会不赚钱。", "evidence": ["E40", "E41"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民间制造行业多有宗族、乡谊、联姻的连环救命网络，前提是没坑过人、家在村里住得久。", "evidence": ["E42"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "1800 万单子捅出 100 多万成本、找尽人脉都兜不住的大洞，几率不高；真正倒闭多因厂主染黄赌毒、家庭变故且名声败坏无人愿救。", "evidence": ["E43", "E44"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "喊着不赚钱、养不住人而忍痛关厂的，多半是子女出国或在外扎根、自己有序撤退。", "evidence": ["E45"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "技术落后但功能完好的机器还可以转卖给去越南、孟加拉、老挝、缅甸开厂的同乡，有专门收这些东西的职业贩子。", "evidence": ["E46"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家风严谨、知道好歹、信用良好、智力正常、正经干活的一般过得并不差；作者以反问质疑“世界第一制造业大国真有那么惨”。", "evidence": ["E47", "E48"]}
   ],
   "argument_steps": [
    "引述他人观点：多数答案认为招不到工人是因为待遇差，进一步推论是制造业不赚钱。",
    "反驳并反转因果：这套逻辑把问题看反了。",
    "反命题：中国制造业一直在赚钱甚至很赚钱。",
    "机制：钱太好赚，无需提高待遇也能赚钱，因此不提高待遇是理性选择，与赚不赚钱无直接关系。",
    "经营策略分析：季节性低技能用工以“平时不养人”换“淡季低成本”，忍受旺季缺人是其自然代价。",
    "概念澄清：区分“制造业强”的中高端重化部门含义与简单制造部门强在劳动者素质的含义。",
    "历史/结构前提：该生产体系按“临时雇佣军”模式设计，以减轻常备军的运营压力。",
    "成本结构：淡季成本近零、设备可转手、硬成本仅为押金，故厂方无需为缺人焦虑。",
    "议价机制：淡季养人会被客户压价，因此“缺人”反而成为议价姿态。",
    "结论性判断：“招不到人”是一种选择而非意外苦恼。",
    "引入例证：转引评论区疫情物资订单事例。",
    "算账：以 12.5% 利润率、3.6% 贷款成本推出 247% 实际利润率，解释“利润率低”与“赚钱”并不矛盾。",
    "对比厂主对外话术与实际利润；再以 24%、32% 年利情形说明利润空间仍在。",
    "风险与兜底：违约风险存在，但需要百万级窟窿才致亏损；宗族乡谊网络提供救助。",
    "收束：真正关厂多为有序撤退，设备可转卖，末句反问“真有那么惨”。"
   ],
   "concept_usage": [
    {"term": "招不到工人", "meaning": "本文不视为劳动力市场短缺的结果，而视为企业在给定订单价格下的一种经营选择与议价姿态。", "evidence": "P029", "ambiguity": "作者未区分不同地区、不同工种与不同规模企业的差异。"},
    {"term": "赚钱", "meaning": "本文指投入资金在短周期内获得高额实际回报，与会计上按销售额计的“利润率低”并不冲突。", "evidence": "P038", "ambiguity": "“赚钱”的衡量口径（利润率、年化、绝对额）作者按论证需要切换。"},
    {"term": "临时雇佣军／精锐常备军", "meaning": "比喻两种用工模式：临时招募、招之即来的低技能劳动力，与重度培训、长期福利维持的稳定员工队伍。", "evidence": "P020", "ambiguity": "为比喻性说法，未给出对应的人力资源管理定义。"},
    {"term": "劳动力饱和度", "meaning": "本文指企业对人力的使用强度或人员储备水平。", "evidence": "P008", "ambiguity": "未给出可操作定义。"},
    {"term": "制造业强", "meaning": "本文区分两层：中高端重化装备部门的技术与门类优势；简单制造部门基于劳动者素质与教育水平的优势。", "evidence": "P014", "ambiguity": "两层含义未给出产业分类标准。"},
    {"term": "实际利润率", "meaning": "本文指扣除自有资金或贷款成本后相对于该成本的收益比，如 247%、108%、56%。", "evidence": "P038", "ambiguity": "计算把三个月收益与三个月利息成本直接相比，未年化，作者自称如此“好算点”。"}
   ],
   "examples_and_targets": [
    "评论区“疫情物资订单”事例（P032，field=quote）：作为引用来的论据（cited_source），作者以其利润数据展开算账。",
    "上海外贸公司疫情物资订单、1800W 货、3 个月、七八百人劳务派遣、两班倒、BOSS 提卡宴（P032）：引用事例中的细节。",
    "200 万/1600 万/12.5%/3.6%/247%、24% 年利→108%、32% 年利→56%（P034—P044）：作者计算的数据。",
    "“打死不做陌生印度客户”（P045）：作者顺带提到的行业说法，属修辞材料。",
    "失火、关键设备坏掉找不到兄弟厂子顶包（P045）：作者列举的风险情形。",
    "宗族、乡谊、联姻的连环救命网络（P048）：作者的机制描述。",
    "厂主染黄赌毒、家里闹离婚、子女胡搞、发精神病（P050）：作者对真正倒闭原因的举例。",
    "去越南、孟加拉、老挝、缅甸开厂的同乡与职业贩子（P052）：作者的二手设备流转例子。",
    "“工厂待遇太差”“制造业不赚钱”（P001、P002）：被反驳的观点。"
   ],
   "conditions": [
    "限定范围：语境中的中国制造业包括一切在中国经营的制造业企业，即包括外资、港资、台资（P005）。",
    "限定对象：季节性、低劳动技能要求的劳动密集型企业；对无需重度培训的人力资源（P009、P010）。",
    "条件：企业接到大订单时才发生大成本（P023）；淡季成本近零需以厂房在郊区开发区、地价便宜或享受政策优惠为前提（P021）。",
    "议价前提：平时养人等活会被客户压价（P024）；价钱到位、钱到账后才需要愁招人（P027）。",
    "计算前提：1600 万成本全为贷款、年息按 15% 顶格、直接平摊三个月算 3.6%；按作者自述“为了好算点”（P033、P035）。",
    "风险条件：客户玩花样或自身生产事故、火灾、设备损坏导致违约（P045）；不赚钱需捅出一百万都摆不平的窟窿（P047）。",
    "互助前提：没坑过人、家在村里住三五代（P048）。",
    "例外：真正技术落后且功能不完好的设备不在可转卖之列；倒闭多因厂主个人问题（P050、P052）。"
   ],
   "rhetoric_and_tone": "论战式、反讽与口语化说理并重。开篇即用“这逻辑看似很顺畅，其实却并不对”“把问题看反了”作断语；连续反问施压（“不是吗？”“为什么要改变经过数十年检验的赚钱经验？这难道不荒谬吗？”“我没成本我急什么急？”）。大量使用比喻：临时雇佣军／精锐常备军、甜蜜的负担、机器不是白菜。P025 起改用厂主第一人称口吻模拟对话，制造现场感与挑衅感。P039“看懂了吗？”、P042“实际上呢？”为直接呼告式过渡。末句“大家难道智商欠费上赶着抱团找死？”为调侃加夸张。整体称呼用“ta们”指企业主，语气轻蔑但论证结构清楚；结构上先立论（P001—P012）、再澄清概念（P013—P019）、再算账（P030—P047）、最后收束于行业生态（P048—P054）。",
   "unresolved_questions": [
    "P032 为评论区引用，评论者身份、订单真实性与数据均无从核实，作者据此展开的利润率推算依赖该未经核实的事例。",
    "P033—P038 的算账把三个月收益与三个月贷款成本直接相除（247%），未年化，作者自述“为了好算点”，口径与常规利润率不可直接比较。",
    "“年息按一年 15% 顶格利息”的出处与适用条件未说明。",
    "P045 提到“打死不做陌生印度客户”，此说法来源与理由未交代，可能涉及国别刻板表述。",
    "P005 称中国制造业“一直在赚钱”覆盖全部在华制造业企业，未给出行业、年份与统计数据。",
    "正文未讨论劳动者一方的工资、工时与用工方式（劳务派遣、两班倒）本身是否合理，问题被完全转换为企业理性选择问题。",
    "P021“运营成本近乎于0”忽略设备折旧、环保与合规成本等，作者未说明估算范围。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "大致上的主体意思是工厂招不到工人是因为工厂待遇太差了。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "“工厂待遇太差是因为制造业不赚钱”", "relation": "context"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这逻辑看似很顺畅，其实却并不对。", "relation": "contradicts"},
    {"key": "E4", "paragraph_id": "P004", "quote": "因为这是把问题看反了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "一直在赚钱，甚至可以说是很赚钱。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "恰恰是因为钱太好赚了，好赚到不需要特别提高工人的待遇也不妨碍赚钱，所以“招不到工人”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "ta们赚不赚钱，跟ta们是否会把赚到的钱投在提高招工吸引力上，并没有直接的关系。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "ta们赚不赚钱，跟ta们是否会提高劳动力饱和度，也没有直接关系。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "“忍受旺季的人手不足”，是“享受淡季的低人力成本”的自然代价", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "“平时不养人”，对于这些季节性、低劳动技能要求的劳动密集型企业来说，远比“忙时不缺人”重要。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "赚到再多钱，也没有必要改变这个完全合理的经营策略。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "为什么要改变经过数十年检验的赚钱经验？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "不是在说这种来料加工的电子组装厂产量大。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "而是在说中国的装备制造、重型机械、化工机械等等核心部门门类齐全、技术高超。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "不是指服装箱包、组装手机这类——尽管前者吸纳的劳动力人数远低于后者。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P017", "quote": "这类相对简单的制造部门也强，但不是强在生产技术上，而是强在人员的基础教育和文化素质上。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "强在中国劳动者对劳动纪律根植于文化里的兼容性上", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "取之不尽、用之不竭，招之即来、挥之即去", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "选择的战场、预定的任务，就是算准了要用临时雇佣军来完成", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "所以为什么要改掉自己本来就计算好的“临时募兵”模式，去改成用重度培训、长期福利维持的“精锐常备军”模式？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "没活的时候，机器又不需要发工资", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P021", "quote": "运营成本近乎于0，这是已经立于不败之地。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P022", "quote": "开一个厂真正的硬成本其实只是一笔押金，在你退出时会扣掉折旧归还给你。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "真正发生大成本的时候，也一定是接到大订单的时候。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P024", "quote": "平时就养着一大批人等活干，光是被客户看到都会被恶意压价", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "你想我多做你的单，是你需要拿出足够价钱来说服我去招到足够的人来给你做", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P026", "quote": "你价钱不够，我宁可空着厂子每天打牌，我没成本我急什么急？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P028", "quote": "但这是个“甜蜜的负担”，不是吗？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P029", "quote": "“招不到人”，是一种选择，不是一种“意外的苦恼”。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P032", "quote": "真实事例、去年工厂接到上海那边一个外贸公司疫情物资订单、要求3个月出1800W货", "relation": "context"},
    {"key": "E31", "paragraph_id": "P032", "quote": "有趣的是BOSS隔了几个礼拜提了台卡宴。", "relation": "context"},
    {"key": "E32", "paragraph_id": "P034", "quote": "200/1600万，利润率多少？12.5%。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P035", "quote": "老板3个月赚了200万啊。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P035", "quote": "年息按一年15%顶格利息，直接平摊到三个月算3.6%的贷款成本。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P038", "quote": "是 (12.5-3.6)/3.6 = 247%", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P040", "quote": "他们跟你吃饭时候算账，算的就是200万/1600万再减去3.6%贷款成本。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P041", "quote": "“投了一千六百万，哎呀只赚了百分之几，剩下九个月还‘揭不开锅’‘完全没活干’。”", "relation": "context"},
    {"key": "E38", "paragraph_id": "P043", "quote": "ta们也一样会有（12.5-6）/6 = 108%的实际利润。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P044", "quote": "甚至就是借32%年利的高利贷，他们都仍然有56%的利润。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P045", "quote": "结果搞违约了，那ta们就倒霉了。", "relation": "qualifies"},
    {"key": "E41", "paragraph_id": "P047", "quote": "这时候还有56%的实际利润在这顶着，要到不赚钱得要这个娄子捅得一百万都摆不平的程度。", "relation": "qualifies"},
    {"key": "E42", "paragraph_id": "P048", "quote": "背后有不知多少叔多少哥多少姨可以连环救命", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P049", "quote": "1800万单子捅一个100多万成本、找完全部人脉资源都兜不住的大洞，几率是不高的。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P050", "quote": "这种洞一般是厂主染上了黄赌毒、无心生产，家里闹离婚鸡飞狗跳", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P051", "quote": "其实多半是老油条子女出国、北漂沪漂生了根不想回，自己有序撤退居多。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P052", "quote": "还可以看看那些去越南、孟加拉、老挝、缅甸开厂的同乡要不要。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P053", "quote": "家风严谨、知道好歹、信用良好、智力正常、正经干活的，没有不知天高地厚乱搞的，一般过得都并不差。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P054", "quote": "世界第一制造业大国，真有那么惨，大家难道智商欠费上赶着抱团找死？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["产业经济", "劳动经济", "制造业", "企业管理"],
   "issue_candidates": ["用工短缺", "工厂待遇", "制造业利润率", "劳务派遣与季节性用工", "低技能劳动力供给"],
   "text_function_candidates": ["论辩", "解释", "经验总结", "评论"],
   "object_candidates": ["中国制造业", "外资港资台资企业", "劳务派遣工", "厂主", "上海外贸公司", "越南", "孟加拉", "老挝", "缅甸"],
   "working_keywords": ["招不到工人", "临时雇佣军", "精锐常备军", "利润率", "人力成本", "劳务派遣", "两班倒", "押金", "二手设备"]
  },
  "notes": "无图片，正文已全文读完，含 1 个引用节点（P032，field=quote，来自评论区）。P032 事例的真实性与评论者身份无法核实，作者的利润率推算建立其上。P033—P038 的“实际利润率”未年化，作者自称“为了好算点”，与常规利润率口径不同，后续研究需注意。P045 含“打死不做陌生印度客户”的国别刻板说法。"
 },
 "eb0078aa": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问：为什么小时候表现越“乖”、越“懂事”的孩子，长大之后心理问题越多？（Q001）。作者没有直接回答这一因果问题，而是把它转换为“子女该不该叛逆、该不该听父母”的代际判断问题：先以“看看别人家的儿子”起兴，提出关键在于父母处于什么状况；再对比古代（父母继承的求生之道更可靠，叛逆大概率倒霉）与现代（要看父母是否经历现代化洗礼、是否存在代差级认知倒挂），主张当代多数城市父母的认知优势已恢复，故押注叛逆输面更大。全文另附 5 张图片（IMG001—IMG005），本次未读图，图片内容可能承担了开篇的举例或调侃功能。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以“看看别人家的儿子”起兴，提出“这事”背后有道理，道理在于父母到底是个什么状况。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "古代情形：叛逆大概率倒霉，因为父母承袭历代祖先的求生之道远比放牛娃或落第秀才私塾老师处听来的可靠；逆着父母搞与寻死差别不大；能活着一大半靠父亲的面子，被从族谱抹掉即九死一生。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "现代情形：要看父母是否经历过现代化洗礼、有没有和子女的其他信息源出现代差级认知倒挂；若父母受过高等教育、有职场宦海历练或背井离乡漂泊经历，最好不要根据同学观点或网上爽文抹杀其意见；要分清谁的斤两更大。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "理由：当下被鼓吹的对父母的“多半正确的叛逆”是帝制崩溃、西学东进这一新旧鼎革时期的特殊产物；父母对社会认知几乎作废、不再领先，甚至大部分是文盲，子女读完小学初中即超过父母；这种状态延续近两百年，被误当作“新常态”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016"], "summary": "主张：改革开放后，七五后父母只要是正常接受现代文化洗礼的，已大面积再次获得对青春期子女的压倒性认知优势；若父母满足上述条件且无确凿理由怀疑其不爱自己，押注叛逆往往输面更大；特殊情况无人能代答，自己判断自己负责。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022"], "summary": "收束：这里面没有玄学，都是建立在基本逻辑上的事实；没说一定会输，但输面更大；彼一时你赢面甚大，此一时你输面甚大，看不清这点输面甚至更大。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“这事”背后是有道理的，道理在于父母到底处于什么状况。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "古代大概率叛逆要倒霉，因为父母从历代祖先继承下来的乱世治世求生之道，比自己从放牛娃或落第秀才私塾老师处听到的靠谱。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在古代玩大胆的想法、逆着爹妈指导搞，和寻死没多大差别；能活着大半靠父亲的面子，被从族谱里抹掉便九死一生。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "就现代而言，关键要看父母是否经历过现代化洗礼、有没有与子女的其他信息源出现代差级的认知倒挂。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若父母受过高等教育、有职场宦海历练或背井离乡漂泊经历，最好不要根据班上同学的观点或网上爽文随便抹杀其意见。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要分清楚到底谁的斤两更大。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在普遍被鼓吹和肯定的对父母的“多半正确的叛逆”，是新旧时代鼎革时期的特殊产物。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在鼎革时期，帝制崩溃使父母对社会的整个认知几乎作废，西学东进使文化基础由诗性伦理转向科学实证，父母在新时代不再比子女在认知上领先，甚至大部分父母是文盲，子女读完小学初中即普遍超过父母。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种父母认知落后的状态几乎延续了近两百年，于是人们误以为这就是“新常态”。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只要正常接受了现代文化洗礼，七五后这一代父母已大面积再次获得对青春期子女的压倒性认知优势。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果父母满足文中列出的条件，且没有确凿理由怀疑他们并不爱你，那么押注叛逆立场往往输面更大。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没人能确切告诉你自己的特殊情况如何，要自己判断、自己负责，但要客观意识到输面更大。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这里面没有玄学，都是建立在基本逻辑上的事实；没说你一定会输，但你的输面更大。", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "彼一时你赢面甚大，此一时你输面甚大；看不清这一点，输面甚至还会更大。", "evidence": ["E19", "E20", "E21"]}
   ],
   "argument_steps": [
    "起兴：以“看看别人家的儿子”引入（配图未读，功能待核）。",
    "提出判断框架：现象背后有道理，道理在于父母的状况。",
    "古代论据：父母承袭的求生之道更可靠，叛逆等于寻死；个人生存依附父辈与宗族。",
    "现代转折：判断标准变为父母是否经历现代化洗礼、是否存在代差级认知倒挂。",
    "行动建议：父母具备高等教育与丰富阅历且无明显不爱自己的理由时，不要用同学观点或网络爽文抹杀其意见。",
    "历史解释：被鼓吹的“叛逆多半正确”是帝制崩溃、西学东进这一鼎革期的特殊产物。",
    "机制说明：该时期父母认知作废、多为文盲，子女教育水平反超，形成近两百年的错觉。",
    "当代判断：改革开放后七五后父母已大面积重获认知优势。",
    "条件与限定：无人能替读者判断特殊情况，读者自负其责，但客观上输面更大。",
    "结论：此一时彼一时，看不清则输面更大。"
   ],
   "concept_usage": [
    {"term": "懂事／乖", "meaning": "仅出现在提问字段中，正文未使用该词，也未分析其与心理问题的关系。", "evidence": "P002", "ambiguity": "提问者的核心概念在正文中缺席，正文实际讨论的是“叛逆／顺从”。"},
    {"term": "代差级的认知倒挂", "meaning": "本文指子女的信息来源与认知水平反超父母，形成父母不如子女的局面。", "evidence": "P007", "ambiguity": "未给出判定“代差级”的标准。"},
    {"term": "现代化洗礼", "meaning": "本文指父母接受高等教育、经历职场宦海历练或背井离乡四海漂泊等现代经历。", "evidence": "P007", "ambiguity": "“洗礼”的具体门槛不清，作者仅以举例方式给出。"},
    {"term": "新常态", "meaning": "本文指人们把父母认知落后于子女的鼎革期状态误当作长期常态。", "evidence": "P013", "ambiguity": "作者未说明该误认在社会层面如何形成。"},
    {"term": "斤两", "meaning": "本文指父母与子女在认知判断上的分量与可靠性。", "evidence": "P009", "ambiguity": "为口语化比喻，未量化。"},
    {"term": "彼一时，此一时", "meaning": "本文指古代与鼎革期“叛逆占优”的形势已变为当代“顺从更稳”的形势。", "evidence": "P019", "ambiguity": "成语式表达，未界定时代分界点。"}
   ],
   "examples_and_targets": [
    "“别人家的儿子”（P001）：起兴式例子，具体所指依赖未读的图片。",
    "放牛娃、读了一辈子书考不上秀才的私塾老师（P004）：古代知识来源的举例与贬抑性类比。",
    "“我就当没这个娃”“在族谱里一抹”（P006）：宗族权力运作的举例。",
    "班上同学的观点、网上翻的爽文（P008）：被作者贬为不可靠的信息源，属反驳对象。",
    "帝制崩溃、西学东进（P011）：作者的历史叙述，作为解释框架。",
    "七五后父母（P014）：作者举的代际样本。",
    "IMG001—IMG005（5 张图片）：本篇图片清单，内容未读，功能待核。"
   ],
   "conditions": [
    "古代前提：“如果是古代”且社会几乎在原地转圈（P004）。",
    "现代条件：“如果是现代”，看父母是否经历现代化洗礼、是否出现代差级认知倒挂（P007）。",
    "适用条件：父母受过高等教育、有职场宦海历练或背井离乡漂泊经历（P008）。",
    "例外条件：没有确凿理由怀疑父母并不爱你（P015）。",
    "限定：七五后父母“只要是正常接受了现代文化的洗礼的”（P014）。",
    "免责声明：特殊情况无人能确切告知，读者自己判断、自己负责（P016）。",
    "程度限定：没说一定会输，只是输面更大（P018）。"
   ],
   "rhetoric_and_tone": "训诫与劝导并存的口气，带有长辈式告诫色彩（“你最好不要”“你要分清楚”）。开篇以“看看别人家的儿子”作调侃式起兴，紧接着转为说理。使用夸张与恫吓式比喻（“和寻死也没啥大差别”“九死一生”“族谱里一抹”）。成语与对偶收束（“彼一时，此一时”“彼一时，你赢面甚大。此一时，你输面甚大”），形成节奏感。第二人称“你”“你们”贯穿全文，直接对年轻读者说话。用“ta们”指父母，语气疏离中性。结构上前半段铺陈古代与鼎革期，后半段转向当代判断，末段以对偶句收尾。",
   "unresolved_questions": [
    "本篇含 5 张图片（IMG001—IMG005），本次无读图能力，图片内容与功能未核验，需图像核验后再读。",
    "提问所问的“乖／懂事的孩子长大心理问题更多”这一因果命题，正文完全没有回答，也未使用“懂事”“乖”“心理问题”等词，属话题转移。",
    "P004 称古代社会“几乎是在原地转圈”属宏观历史断言，无出处。",
    "“七五后的这一代父母……大面积的再次获得了压倒性认知优势”无数据或调查支撑。",
    "“这种状态几乎延续了近两百年”的起止时间未界定。",
    "“大部分父母们都是文盲”未说明对应的时期与地域范围。",
    "正文未讨论“懂事”与顺从、心理问题之间的机制，也未给出任何心理学依据。",
    "P001 与图片的关系不明，开篇起兴句可能依赖图片才能理解。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "看看别人家的儿子。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "道理就是父母到底是个什么状况。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "如果是古代，大概率叛逆要倒霉。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "你在这个时代玩大胆的想法，逆着爹妈的指导搞，和寻死也没啥大差别。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "你能活着，一大半要靠着你爹的面子。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "那么看父母是否经历过现代化洗礼，有没有和子女的其他信息源出现代差级的认知倒挂。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "你最好不要根据班上同学的观点", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你要分清楚到底谁的斤两更大。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "现在普遍被鼓吹和肯定的对父母的“多半正确的叛逆”，其实是新旧时代鼎革时期的特殊时代的特殊产物。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "父母们对于社会的整个认知几乎作废了", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "父母们在新的时代没有比子女在认知上领先。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "甚至大部分父母们都是文盲", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "这种状态几乎延续了近两百年，于是人们误以为这就是“新常态”了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "就已经大面积的再次获得了对青春期子女的压倒性认知优势。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "那么你押注叛逆立场往往输面更大。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "没人能确切的告诉你自己的特殊情况如何，你自己判断、自己负责", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P017", "quote": "这里面没有任何玄学，都是最朴素的、最显然的建立在基本逻辑上上的事实。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "没说你一定会输，但是，你的输面更大。", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P020", "quote": "彼一时，你赢面甚大。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "此一时，你输面甚大。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "看不清这一点，你的输面甚至还会更大。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["代际关系", "家庭教育", "社会变迁", "文化史"],
   "issue_candidates": ["懂事与心理问题", "青春期叛逆", "父母认知权威", "代际认知倒挂", "改革开放与代际差异"],
   "text_function_candidates": ["评论", "训诫", "答疑", "经验总结"],
   "object_candidates": ["父母", "子女", "七五后", "私塾老师", "宗族", "族谱", "帝制", "西学"],
   "working_keywords": ["懂事", "乖", "叛逆", "代差级认知倒挂", "现代化洗礼", "新常态", "彼一时此一时", "七五后"]
  },
  "notes": "本篇含 5 张图片（IMG001—IMG005），本次仅读正文，未读图，故 status=needs_reread、image_checked=False；图片内容与开篇“看看别人家的儿子”的关系需图像核验，图像核验前不得按 read 处理。正文未使用“懂事”“乖”“心理问题”等提问核心词，实为代际叛逆与顺从的劝诫文，与提问所问的因果机制不对应，后续研究需标注此错位。文中“近两百年”“大部分父母是文盲”“七五后大面积重获认知优势”等宏观断言均无出处，需外部核查。P008 原文有“自己在自己在网上翻的爽文”重复用字，短引已避开该处。"
 },
 "4f45fb37": {
  "analysis": {
   "question_context": "提问者问：合肥严查加油站扫码支付，你怎么看？为什么不能在加油站使用手机？哪些行为在加油站存在安全隐患？（Q001）。作者不作事实解释，而直接给出监管策略上的反驳性主张：该严查的是无法控制油料外泄水平的油站管理机制，而不是潜在火源；应通过电子鼻抽检油气浓度并对油站开罚单，目标是做到站内点火把都安全，而非反向禁止一切火源去迁就低劣的管理与硬件。全文五段，是一则简短的政策评论，未回答手机为何不能使用、也未列举具体安全隐患。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出核心主张：该严查的是不能控制油料外泄水平的油站管理机制，而不是潜在火源。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "行动建议：督察员应拿电子鼻随机暗访抽查，嗅探到高于百分之一安全阈值的油气分子痕迹就给油站开罚单。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "应做到油站内点火把都能保证安全，而不是反向通过“禁止一切火源”去适应低劣的管理水平和硬件配置。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "类比：这犹如嫌坦克不够安全的人不去惩罚装甲安薄了，而去罚“非法投石”。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "结论：这是无意义的策略方向。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该严查的是不能控制油料外泄水平的油站管理机制，而不是潜在火源。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "督察员应拿电子鼻随机暗访抽查，嗅探到高于百分之一安全阈值的油气分子痕迹就开罚单给油站。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应做到油站内就是点火把都能保证安全，而不是反向通过“禁止一切火源”去适应低劣的管理水平和硬件配置。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以坦克类比：嫌坦克不够安全的人不去惩罚装甲安薄了，却去罚“非法投石”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：这是无意义的策略方向。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "提出主张：严查对象应是油站管理机制而非潜在火源。",
    "给出监管手段：电子鼻随机暗访抽查，超阈值即罚油站。",
    "给出应然目标：站内点火把也安全，反对方是禁止一切火源迁就低劣管理与硬件。",
    "类比论证：坦克不安全应罚装甲太薄，而非罚投石。",
    "结论：现行策略方向无意义。"
   ],
   "concept_usage": [
    {"term": "油料外泄水平", "meaning": "本文指油站对油气泄漏的控制能力，作者视其为真正的安全变量与监管对象。", "evidence": "P001", "ambiguity": "未给出可操作的监测指标与标准，仅在后文给出“百分之一安全阈值”。"},
    {"term": "潜在火源", "meaning": "本文指手机扫码等可能引燃的行为，作者认为它不是问题的根源。", "evidence": "P001", "ambiguity": "作者未讨论火源在油气超标环境中的实际作用。"},
    {"term": "电子鼻", "meaning": "本文指用于嗅探油气分子痕迹的检测设备。", "evidence": "P002", "ambiguity": "设备是否普及、检测精度如何，均未说明。"},
    {"term": "百分之一安全阈值", "meaning": "本文提出的油气浓度执法阈值。", "evidence": "P002", "ambiguity": "该数值来源与依据未说明，是否为爆炸下限的百分比不明。"},
    {"term": "非法投石", "meaning": "坦克类比中被罚的一方，喻指被整治的潜在火源。", "evidence": "P004", "ambiguity": "为修辞说法，无实际所指。"}
   ],
   "examples_and_targets": [
    "合肥严查加油站扫码支付（提问字段 Q001）：文章的触发事件，正文未再提合肥与扫码支付字样。",
    "电子鼻随机暗访抽查（P002）：作者提出的行动建议与工具例子。",
    "油站内点火把（P003）：夸张化的目标表述。",
    "坦克装甲与“非法投石”（P004）：类比论证的材料。"
   ],
   "conditions": [
    "执法条件：嗅探到高于百分之一安全阈值的油气分子痕迹才开罚单（P002）。",
    "目标条件：油站内即便点火把也能保证安全，即安全应靠硬件与管理而非禁令维持（P003）。",
    "隐含前提：存在能够可靠检测油气浓度的执法手段与阈值标准（P002）。"
   ],
   "rhetoric_and_tone": "简短、断言式、带有训诫与讥讽语气。以“该严查的是……而不是……”的对举结构开篇，直接否定现行方向；用“点火把都能保证安全”作夸张表达；以“嫌坦克不够安全……而去罚‘非法投石’”作讽刺性类比，把现行监管比作避重就轻；末句“这是无意义的策略方向”为斩钉截铁的收束。通篇无引语、无数据和出处，属高度浓缩的评论体。",
   "unresolved_questions": [
    "正文未回答提问中的“为什么不能在加油站使用手机”，也未列举哪些行为存在安全隐患。",
    "“百分之一安全阈值”的计量基准与来源未说明（是否为爆炸下限的百分之一）。",
    "电子鼻检测是否具备现实可行性、成本与执法依据，正文未讨论。",
    "“点火把都能保证安全”是否有可比较的行业实例或安全标准支撑，未说明。",
    "文章未提及合肥、扫码支付等触发事件的具体事实，无法据本篇了解案件细节。",
    "作者的安全主张与现行加油站安全规范之间的关系未讨论，可能涉及规范冲突，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "该严查的是不能控制油料外泄水平的油站管理机制，而不是潜在火源。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "督察员应该拿着电子鼻随机暗访抽查，嗅探到到高于百分之一安全阈值的油气分子痕迹就开罚单给油站。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "应该做到油站内就是点火把都能保证安全，而不是反向的通过“禁止一切火源”去适应低劣的管理水平和硬件配置。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这犹如嫌坦克不够安全的人，不去惩罚装甲安薄了，而去罚“非法投石”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这是无意义的策略方向。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["公共安全", "安全生产监管", "石油零售", "政策评论"],
   "issue_candidates": ["加油站扫码支付", "油气泄漏监管", "安全阈值执法", "禁止火源式管理", "监管对象错位"],
   "text_function_candidates": ["评论", "批评", "政策建议"],
   "object_candidates": ["加油站", "督察员", "电子鼻", "合肥", "手机扫码支付", "坦克"],
   "working_keywords": ["油料外泄", "油气分子", "安全阈值", "电子鼻", "火源", "非法投石", "策略方向"]
  },
  "notes": "无图片，正文已全文读完（仅 5 段、176 字）。正文为纯政策评论，未使用提问中的“合肥”“扫码支付”等事实要素，也未回答手机为何不能在加油站使用，属借题立论。P002 原文有“嗅探到到”重复用字，短引照抄。阈值数值、检测手段与安全标准的依据均待外部核查。"
 },
 "94f6ee9b": {
  "analysis": {
   "question_context": "提问者问：年轻人怎么在这个喧嚣的社会中不迷失自我和坚守理想？（Q001）。作者先否定问题的前提：不是“喧嚣的社会”让年轻人难以坚持理想，而是他们当作理想的东西一开始就不是理想。全文围绕“成为理想者”的两个要害展开：一是理想本身的真实性——理想是假定在自己死后仍有意义、值得以死追求的东西，而多数人追求的是会随价值观改变的目标；理想属于“未亡人”的特权，青少年尚不该有，提前僭称理想并以“中二病”方式榨取理想快感，会在真正面对死亡时丧失凭理想超越死亡的能力。二是对理想而言“失败”概念不适用——理想是注定未竟、可无限累积的事业，其免疫力来自它本质上只能是对不特定、无限未来人类的爱。文末给出行动建议：把当下的热爱称为兴趣、目标、打算、计划或志向，不要称为理想。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出成为无所畏惧、永不放弃的理想者有两个要害，其一即理想本身的真实性。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "定义区分：多数人当作理想追求的是目标而非理想；目标是服务于人的工具、随价值观改变，强迫自己为已无价值的目标奋斗荒谬；理想是被假定在自己死后仍有意义、值得以死追求的东西，必须真切见到、摸到、尝到死，才能以高于生存的姿态持有价值。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011"], "summary": "论证理想无法被放弃的机制：理想是“如何燃尽余生”的决定；死亡来临时逃避已无意义，唯一有价值的是让死亡本身有意义，故为逃避死亡而放弃这种意义本身荒谬；以死相威胁已不能让人放弃，何况贫穷、窘迫、危险这些“半死”；理想是人的神性实现，真正的理想主义者因此迸发令人折服、敬畏的力量。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "限定适用对象：这是未亡人的特权，不该是尚在走上坡路、还有未尽可能性的青少年所能有甚至该有的东西；不是社会喧嚣使人难以坚持理想，而是其所谓理想本身不是理想；只有意识到自己将死、只能做最后一次不可更改的决定而仍坚持己见，欲念才升格为理想。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018"], "summary": "告诫提前选择理想不明智：人对任何可造成享乐的机制都能找到“妙计”（如以爱情为模版发明嫖妓）；把理想当烟土萃取快感的“理想游戏”即中二病，会走向极端化与狂热化，最终反而丧失理想的能力。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "行动建议与劝告：不要把目前热爱的东西僭称为理想，称其为兴趣、目标、打算、计划乃至志向；这样自然淘汰时不会背上“一再放弃理想”的烙印；严格说来没有过理想也就没有放弃过理想；提前玩理想游戏会在与死神相遇时丧失凭理想超越死亡的能力；不要为生命方向改变焦虑，那只是换壳必有的折磨；不要理会歌唱青春理想的蠢人，理想本身就是青春的丧钟。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "第二个要害：对理想“失败”这一概念不适用；理想是注定未竟的事业，凡会因“做不完”而被引以为憾者都无资格成为理想；理想是“多做一分，就多好一分”的无限旅程，如堆土为山，堆上去就在了，此后千秋万世再不能回到它未成之前。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039"], "summary": "以英文分行短句重申：即使微小，仍然有差别（there is a difference）。", "role": "transition"},
    {"unit_id": "U009", "paragraph_refs": ["P040", "P041"], "summary": "以类比强调“失败”不适用于理想：就像“通俗易懂”不适用于鲸鱼；若所奉之物没有对失败的绝对逻辑免疫力，那它就不是理想；腰里塞枕头虽圆鼓鼓也不叫怀孕。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P042", "P043"], "summary": "解释理想免疫力的来源：可成其为理想的一切事物本质上只能是对不特定的、无限未来人类的爱，故之后必有同志领受同样召唤而来，终将为山万仞、成全这粒微尘的永恒。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P044", "P045"], "summary": "结论：只要迈出一步就已经成功，迈第二步只是成功两倍，因此不存在“坚持”的困难；真正要考虑的是避免废寝忘食。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想成为无所畏惧、永不放弃的理想者有两个要害。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谈论“年轻人容易放弃理想”的前提是所放弃的的确是理想；而大部分人当作理想追求的东西一开始并不是理想，只是目标。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想和目标之所以常被相提并论，是因为它们都对人的行动有驱动力，所以经常被人混淆。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "定义：理想是人打算为之而死、人为它而存在的东西；目标只是设计出来的标的、服务于人的工具，是为人而存在。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "目标最终为自身的生命质量与人生体验服务；价值观随时变迁，目标随之改变，因此强迫自己为已不再认为有价值的目标继续奋斗是荒谬且不可能的。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想（ideal）是被假定在自己死后仍有意义、因而值得以死追求的东西；必须真切见到、摸到、尝到死，才能真实地以高于自身生存的姿态持有某种价值。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想是“如何燃尽余生”的决定，是人之将死所以言之善；它因凭着被死恩赐的觉悟超脱了执着于生者的顾虑、怯懦与贪婪而美得无法亵渎。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "死亡来临时，继续思考如何逃避死亡已无意义，唯一有价值的是让死亡本身还有某种意义；因此为继续逃避死亡而放弃这种意义本身就是荒谬的。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以死相威胁已不可能让人放弃这最后的念想，何况以贫穷、窘迫、危险这些“半死”相威胁；对成其为理想的东西，放弃本身没有意义，这才是“理想无法被放弃”的原因。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自知必死故不再把求生视为第一诉求；置生死于度外的人与不受生死束缚的神呈现类似位格特质。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想是人的神性实现；真正的理想主义者会迸发令人折服、热爱、敬畏乃至崇拜的力量，源于近似于神而诱发的人对神的感情冲动。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "上述理想状态是未亡人的特权，不是、也不该是尚在走上坡路、还有未尽可能性的青少年所能有甚至该有的东西。", "evidence": ["E13"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不是“喧嚣的社会”让年轻人难以坚持理想，而是一开始被当作理想的那个东西本身就不是理想，即便其文字表述与“未亡人”的一字不差。", "evidence": ["E14"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有清楚意识到自己要死了、只能在一切可能中做最后一次无法再更改的决定时仍然坚持己见，欲念才升格为理想。", "evidence": ["E15"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对任何可造成享乐的机制总能找到“妙计”以既引发类似快感又避免麻烦，犹如以爱情为模版发明嫖妓。", "evidence": ["E16"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想作为强烈的神性享乐触发机制也不例外，其“妙计”是“理想游戏”即中二病：将理想当烟土萃取精神快感，追求的是持有理想的陶醉感而非理想本身，因而走向极端化、狂热化，最终反而丧失理想的能力。", "evidence": ["E17", "E18"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议日渐成熟、未被死神约谈过的青年不要把目前热爱的东西僭称为理想，而应称其为兴趣、目标、打算、计划乃至志向，以免日后背上“一再放弃了理想”的烙印。", "evidence": ["E19"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "严格意义上没有过理想，也就没有放弃过理想；这不是安慰的话术，而是本质的事实。", "evidence": ["E20"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若非要提前玩理想游戏榨取快感，与死神相遇时会丧失凭理想超越死亡的能力，作者称这是罪有应得。", "evidence": ["E21"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在属于自己的时候到来之前，不要为贪图理想的快感做蠢事，也不要为生命方向时常改变这种自然而健康的现象焦虑。", "evidence": ["E22"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成长中的“失败”与“崩溃”是换壳必有的折磨、成长本身的烦恼，不要为逃避它而不择手段；作者并称当理想真正降临时人会羡慕和怀念之前的时光。", "evidence": ["E23"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要理会那些歌唱青春理想的蠢人，他们不过是自己也不自知的瘾君子；理想不属于青春。", "evidence": ["E24"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想本身就是青春的丧钟；丧钟鸣响即开演最后一幕戏，若准备好了这将是最精彩的一幕，但提前让它到来并非福利，为窃取快感而损毁最后一场演出的资格是愚蠢的。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二个要害：对理想“失败”这一概念不适用。", "evidence": ["E28"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想是注定未竟的事业，凡因“做不完”“无法完成”而被引以为憾者都没有成为合格理想的资格；它不会是“没能及时达成就没有意义”的目标，而是“多做一分，就多好一分”的无限旅程。", "evidence": ["E29"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想如堆土为山：背上去一两土山就实多一两土，后来者必在此之上再堆；哪怕一两一钱一毫一芥之微，堆上去就在了。", "evidence": ["E30", "E31"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此后千秋万世再也不能回到它未成之前。", "evidence": ["E32"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“失败”对成其为理想的东西根本不适用，如其对鲸鱼不适用；若所奉为理想者没有这种对失败的绝对逻辑免疫力，那它就不是理想。", "evidence": ["E33", "E34"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理想拥有这种免疫力的原因：可成其为理想的一切事物本质上只能是对不特定的、无限未来人类的爱；因此之后必有无限尽的同志领受同样召唤而来，终将为山万仞，成全这粒微尘的永恒。", "evidence": ["E35", "E36"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要迈出一步就已经成功，迈第二步只是成功两倍，因此不存在“坚持”的困难；真正要考虑的是避免废寝忘食。", "evidence": ["E37", "E38"]}
   ],
   "argument_steps": [
    "总起：成为理想者有两个要害。",
    "第一要害：理想的真实性。",
    "前提澄清：多数人以为的理想其实是目标，混淆源于二者都有驱动力。",
    "定义：理想是人为之而死、为它而存在的东西；目标是为人而存在的工具。",
    "推论：目标随价值观变迁而改变，强迫自己为已无价值的目标奋斗荒谬且不可能。",
    "定义：理想是被假定死后仍有意义、值得以死追求的东西；须真切体验死才能以高于生存的姿态持有价值。",
    "机制论证：死亡当前逃避无意义，唯一有价值的是让死亡本身有意义；为逃避死亡而放弃此意义是荒谬的。",
    "推论：以死相威胁不能使人放弃，何况贫穷、窘迫、危险等“半死”；故“理想无法被放弃”。",
    "引申：置生死于度外者近似神，理想是人的神性实现，理想主义者因此有慑人之力。",
    "限定：这是未亡人的特权，青少年不该有。",
    "否定问题前提：不是喧嚣社会使人难以坚持理想，而是其所持者本非理想。",
    "门槛：只有在将死之际做最后一次不可更改的决定而仍坚持，欲念才升格为理想。",
    "告诫：提前选择理想不明智，因享乐机制会被“妙计”利用，即中二病式的“理想游戏”，会耗尽理想能力。",
    "行动建议：把当下热爱称为兴趣、目标、打算、计划、志向，不称理想。",
    "安慰性推论：没有理想也就没有放弃理想。",
    "警告：提前玩理想游戏者将在与死神相遇时丧失超越死亡的能力。",
    "劝慰：生命方向改变与成长“崩溃”是换壳之苦，不必焦虑，不择手段逃避才是问题。",
    "贬斥对立面：歌唱青春理想者是瘾君子；理想是青春的丧钟。",
    "第二要害：失败概念对理想不适用。",
    "论证：理想是注定未竟的事业，属于可无限累积的“无限旅程”，如堆土为山。",
    "类比：如“通俗易懂”对鲸鱼不适用；腰里塞枕头不叫怀孕。",
    "根据：理想的免疫力来自它本质上是对不特定、无限未来人类的爱，故必有后来同志接续。",
    "结论：迈出一步即已成功，不存在“坚持”的困难，只需避免废寝忘食。"
   ],
   "concept_usage": [
    {"term": "理想", "meaning": "本文指被假定在自己死后仍有意义、因而值得以死追求的东西；人是为它而存在，放弃它本身没有意义。", "evidence": "P006", "ambiguity": "作者把理想与“对无限未来人类的爱”绑定的同时，又以“未亡人特权”限制其主体，标准极高，普通人是否可能有理想存疑。"},
    {"term": "目标", "meaning": "本文指设计出来的标的、服务于人的工具，随人的价值观改变而改变，可因无价值而被放弃。", "evidence": "P004", "ambiguity": "与“志向”“计划”“打算”的界线由作者自行划定，未给出统一判据。"},
    {"term": "未亡人", "meaning": "本文指已经真切领受死亡、只能在最后决定中坚持己见的人，理想是其特权。", "evidence": "P012", "ambiguity": "“未亡人”在此为作者自造用法，与通常指寡妇的义项不同，易生歧义。"},
    {"term": "理想游戏／中二病", "meaning": "本文指把理想当烟土萃取精神快感的模拟行为，追求的是持有理想带来的陶醉与激动而非理想本身，会走向极端化与狂热化。", "evidence": "P018", "ambiguity": "作者未给出区分真实理想与“理想游戏”的可操作标准，仅以动机描述。"},
    {"term": "神性／位格", "meaning": "本文用神学语汇描述置生死于度外者近似神的特质，以及理想作为“人的神性实现”。", "evidence": "P010", "ambiguity": "属比喻性神学框架，作者未说明其本体论承诺。"},
    {"term": "失败", "meaning": "本文主张该概念对理想不适用，因为理想是注定未竟、只论累积的无限事业。", "evidence": "P028", "ambiguity": "作者未讨论理想在实践中被背叛、被放弃等情形是否算失败。"},
    {"term": "爱", "meaning": "本文指可成其为理想的一切事物本质上只能是“对不特定的、无限未来人类的爱”。", "evidence": "P042", "ambiguity": "定义高度抽象，未说明其与具体政治或道德目标的关系。"}
   ],
   "examples_and_targets": [
    "“嫖妓之于爱情”（P017、P018）：作者自造的类比，用以说明享乐机制可被模拟榨取。",
    "“中二病”（P018）：作者借用的流行词，用作被批评的行为类型（属批评对象而非引用来源）。",
    "吸毒者一次次加大注射量（P018）：类比材料。",
    "“我放弃了、又放弃了、一再的放弃了、看来也必将放弃一切的理想”（P019）：作者模拟青年心理的引语式表述。",
    "“人的肉体是哺乳动物，但心灵却是甲壳动物”（P023）：比喻材料。",
    "“理想是青春的丧钟”“最后一幕戏”（P025）：比喻与修辞材料。",
    "“就像‘通俗易懂’这个概念对一头鲸鱼完全不适用”（P040）：类比材料。",
    "“腰里塞个枕头虽然一样圆鼓鼓，但那不叫怀孕”（P041）：类比材料。",
    "堆土为山、一两一钱一毫一芥（P029、P031、P033）：类比与修辞材料。",
    "英文句“This is how it works”“By all means, there is a difference...”（P014、P034—P039）：修辞性插入。",
    "“歌唱青春理想的蠢人”“不自知的瘾君子”（P024）：被贬斥的对立人群。"
   ],
   "conditions": [
    "主体条件：理想是“未亡人”的特权，尚在走上坡路、还有未尽可能性的青少年不该有（P012）。",
    "门槛条件：必须真切见到、摸到、尝到死，而非抽象地风闻死（P006）。",
    "触发条件：清楚意识到自己要死了，只能在一切可能中做最后一次无法再更改的决定，而仍坚持己见（P014）。",
    "建议适用对象：日渐成熟、没有被死神约谈过的青年（P019）。",
    "后果条件：非要提前玩理想游戏者，在与死神相遇时会丧失凭理想超越死亡的能力（P021）。",
    "时间限定：在属于你的时候到来之前不要做蠢事；当它真正降临时你会羡慕之前的时光（P022、P023）。",
    "资格条件：凡会因“做不完”“无法完成”而被引以为憾者，没有成为合格理想的资格（P028）。",
    "判据条件：若所奉为理想者没有对失败的绝对逻辑免疫力，则它不是理想（P040）。",
    "本质条件：可成其为理想的一切事物本质上只能是对不特定的、无限未来人类的爱（P042）。"
   ],
   "rhetoric_and_tone": "布道式与训诫式并重的独白语气，作者以过来人身份对“你们”青年说话（“我额外的告诫你们”“你还没有被死神约谈”）。大量使用死亡主题的强力修辞（“如何燃尽余生”“人之将死所以言之善”“青春的丧钟”“最后一幕戏”）。比喻密集且层层递进：理想游戏如烟土、如嫖妓之于爱情、吸毒者加大剂量；成长之痛如甲壳动物换壳；理想的累积如堆土为山；假理想如腰里塞枕头冒充怀孕。使用贬斥性称呼（“蠢人”“不自知的瘾君子”“罪有应得”）与反问施加压力（“不愚蠢吗？”“你有什么‘坚持’的困难？”）。穿插英文短句（“This is how it works”“By all means, there is a difference...”）与分行断句（P030—P039）造成仪式感与节奏。结构上第一要害（P001—P026）、第二要害（P027—P045），末句以反讽式关切收束（“坦白说，避免废寝忘食才是你要考虑的问题”）。",
   "unresolved_questions": [
    "作者以“必须在死前做最后一次不可更改的决定”定义理想，同时又主张理想是“对不特定、无限未来人类的爱”，两处标准之间的张力未加说明。",
    "“未亡人”为作者自造用法，与通常义项不同，可能造成误读。",
    "如何区分真实的理想与“理想游戏（中二病）”，作者只给出动机描述，无可操作判据。",
    "P018 把“中二病”当作病理化比喻使用，未给出心理学依据。",
    "作者称理想主义者具有“近似于神”的位格并引发崇拜冲动，属未加论证的形而上断言。",
    "文末“避免废寝忘食才是你要考虑的问题”与前文“以死相追”的严肃框架语调落差较大，是否为反讽未明说。",
    "本篇未给出任何可供外部核查的人物、事件或数据，论证完全依赖定义与类比。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "想要成为一个无所畏惧、永不放弃的理想者，有两个要害。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "大部分人当作理想来追求的那个东西一开始就并不是理想，而是目标而已。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "理想和目标之所以常被相提并论，是因为它们都对人的行动有驱动力，所以经常被人混淆。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "理想，是你打算为之而死的东西——你是为它而存在。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "目标，则只是一种设计出来的标的，一种服务于你的追求的工具——它是为你而存在。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "强迫自己为已经不再认为有价值的目标继续奋斗是荒谬的，因而也是不可能的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "而理想，ideal，是被假定在我死后仍有意义、因而值得我以死追求的东西。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "理想，是一个“如何燃尽余生”的决定，是一种人之将死所以言之善。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "因此，为了继续逃避死亡而放弃这种意义，本身就是荒谬的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "对成其为理想的东西，放弃本身是没有意义的。这才是“理想无法被放弃”的原因所在", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "因为自知必死，所以可以不再把求生视为第一诉求。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "理想，是一种人的神性实现。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "但是，这是属于未亡人的特权。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P013", "quote": "而是从一开始你们以为是理想的那个东西本身就不是理想", "relation": "contradicts"},
    {"key": "E15", "paragraph_id": "P014", "quote": "这时你如果仍然坚持己见，它才从你的欲念，升格而成为理想。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "犹如爱情令人欲仙欲死，人们就会以它为模版发明嫖妓。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "“中二病”是一种将“理想”当作烟土来萃取精神快感的模拟行为", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "直到灵魂完全麻木，或者心灵无法负担为止——最终反而丧失了理想的能力。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "那么你最佳的选择，是不要将你目前做热爱的任何东西僭称为理想。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "你没有过理想，所以你也没有放弃过理想。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "那么到你与死神相遇时，你会丧失凭理想超越死亡的能力。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "在属于你的时候到来之前，你不要为了贪图理想的快感而做蠢事。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P023", "quote": "那只是换壳必有的折磨，是成长本身的烦恼。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P024", "quote": "不要理会那些歌唱青春理想的蠢人——他们自己也不过是一群不自知的瘾君子。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P025", "quote": "理想不但绝对不属于青春，它本身就是青春的丧钟。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "但是，提前让它到来真的绝对是一种福利吗？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P026", "quote": "为了在它到来之前窃取它的快感而损毁（或哪怕只是威胁到）自己的最后一场演出的真正资格，不愚蠢吗？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P027", "quote": "第二，对于理想，“失败”这一概念不适用。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P028", "quote": "而是“多做一分，就多好一分”的无限旅程。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P029", "quote": "它一定是一种如堆土为山般的东西——背上去一两土，那山就实实在在多了一两土", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P029", "quote": "哪怕就是一两、一钱、一毫、一芥之微，它堆上去了，就在了，came into being.", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P033", "quote": "此后千秋万世，再也不能回到它未成之前。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P040", "quote": "“失败”这一概念对成其为理想的东西根本不适用。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P040", "quote": "如果你奉为理想的事物没有这种对失败的绝对逻辑免疫力，那么这只意味着你现在持有的这个并不是一个理想。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P042", "quote": "因为可以成其为理想的一切事物，本质上只能是对不特定的、无限未来人类的爱。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P043", "quote": "ta们终将为山万仞，成全你这粒微尘的永恒。这才是理想该有的样子。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P044", "quote": "你只要迈出一步，就已经成功了。迈第二步，只是成功两倍。你有什么“坚持”的困难？", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P045", "quote": "坦白说，避免废寝忘食才是你要考虑的问题。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["价值哲学", "伦理学", "存在主义", "青年文化", "生死观"],
   "issue_candidates": ["理想与目标的区分", "理想能否被放弃", "青春与理想的关系", "中二病式理想消费", "以死为尺度的价值选择"],
   "text_function_candidates": ["答疑", "训诫", "论辩", "劝导"],
   "object_candidates": ["青年", "未亡人", "理想主义者", "死神", "神", "中二病", "同志"],
   "working_keywords": ["理想", "目标", "ideal", "未亡人", "神性实现", "理想游戏", "中二病", "青春的丧钟", "堆土为山", "无限的未来人类"]
  },
  "notes": "无图片，正文已全文读完。含英文插入句（P014“This is how it works”、P034—P039 分行英文）与半角标点（P005“事物的价格当然在变.当我的价值观改变了”），短引已避开该处标点。本篇为高度个人化的哲学劝导文，论证依赖自定义与类比，无外部事实与数据可核；提问所问的“喧嚣社会”被作者直接否定为前提。"
 },
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
