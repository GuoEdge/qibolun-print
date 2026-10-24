# -*- coding: utf-8 -*-
"""批次 r001-b0140 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0140.sessions.py            # 写 out/r001-b0140.out.jsonl
  python3 records/r001-b0140.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0140"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0140.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "25733bb8": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么会有人认为加入外国国籍就是不爱国？作者没有沿用这一中性问法，而在正文开头把问题改述为“为什么有人会认为剥夺非中国籍的华人的热爱权，将自己升级为‘中华民族’的‘正统’，将其他华人视为异己，是一种‘爱国’行为？”——即把“有人”的排外立场当作要反驳的对象。提问者的问法只是语境，文章立场属于作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者改述提问：把非中国籍华人视为异己者自居“中华民族”正统；称回答了改述后的问题就回答了本题。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "给出判据：爱与不爱取决于被爱对象的利益是否受损，而非爱人者自身利益是否受损。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "称自称“利益受损”者受损的多不是利益而是情绪乃至“情绪毒瘾”，并把排斥改籍者解释为对方让自己“吸得不爽”，故必欲除之而后快。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "以连续反问重构并嘲弄“排斥改籍者有利于中国”的几种理由（吓阻叛徒、中国是需要区分人我以团结对抗的帮派、生存之道），并要求对方重溫《英特纳雄耐尔》。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019"], "summary": "给出“中国是天下”的定义：过去的地理围墙今天已不足以界定中国；中国不止是中国人的，甚至不止是汉族、华人的中国。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "以礼仪、理想、道路而非人种、民族、肤色、出身、国籍界定中国人；其他中国人有义务接纳，天下一统靠此而来。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "质问以“国籍”“站队”“种族”“左右”来“强国”；指出国籍概念远晚于中国概念；以训诫式短句收束（多读书、认清楚祖宗）。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "引出“入籍宣誓”文本（P033 为引用材料），转述作者自己的回复称其“配合对方的自欺欺人”，并称宣誓中“绝无任何心智障碍、借口或保留”一句是“无意义的见证”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张爱与不爱不取决于爱人者自身利益是否受损，而取决于被爱的对象的利益是否受损。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为绝大部分人自称“利益受损”时受损的并不是其利益，而只是情绪乃至“情绪毒瘾”，因为确认利益是否受损需要复杂的财务知识、分析能力甚至预测能力。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为排斥改变国籍的前中国人的真实动力，是对方让自己“吸得不爽”，故必欲除之而后快。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "（作者以反问重构的对方立场）将改变中国籍的前中国人一概视为不爱国，是为了吓阻“叛徒”，或因为把中国当成需靠分出中国人与非中国人来团结对抗外国人的帮派，或认为这是中国的“生存之道”。", "evidence": ["E6", "E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国是天下：中国不止是中国人的中国，也不止是汉族的中国、华人的中国，过去圈定中国的地理围墙今天已不再足以界定中国。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国的边界在中国可以企及的最远处；任何向往和奉行中国的礼仪、理想和道路的人，无论人种、民族、肤色、出身甚至国籍，懂得礼义廉耻、揖让进退、天下为公并愿自称中国人，就是中国人。", "evidence": ["E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为其他中国人有义务接纳这样的人，而没有权力拒绝。", "evidence": ["E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑以“国籍”“站队”“种族”“左右”来“强国”，并主张国籍是远晚于中国的概念，轮不到“国籍”来教中国人什么叫中国人。", "evidence": ["E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不承认把中国理解为需要靠分出中国人与非中国人来团结对抗外国人的帮派，并要求对方重溫《英特纳雄耐尔》、回想它唱的是什么。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者转述自己此前的回复：对入籍宣誓的纠结“就是配合一下对方的自欺欺人”。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为入籍宣誓中“我在此自由宣誓，绝无任何心智障碍、借口或保留”是无意义的见证。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "改述提问：把“加入外国国籍就是不爱国”改写为对非中国籍华人的热爱权的剥夺与自我加冕“正统”，并称答此即答本题（P001-P002）。",
    "先立判据：爱不爱取决于被爱对象的利益是否受损，而非爱人者自身利益（P003-P004）。",
    "据此判据指认自称“利益受损”者实为情绪受损，并给出“情绪毒瘾”“大烟枪里的杂质”的解释（P005-P008）。",
    "反过来追问：把改变中国籍者一概视为不爱国，何以是有利于中国的行为？逐条假设对方理由（吓阻叛徒／帮派／生存之道）并予驳斥，要求重溫《英特纳雄耐尔》（P009-P013）。",
    "给出正面定义：中国是天下；地理围墙已不再足以界定中国；中国不止是中国人的、汉族的、华人的中国（P014-P019）。",
    "推出身份判据：以礼仪、理想、道路和自称界定中国人，且其他中国人有接纳义务而无拒绝权力（P020-P023）。",
    "回到当下质问以“国籍”“站队”“种族”“左右”来“强国”，并以国籍概念晚出为据否定其裁判资格，末以训诫收束（P024-P031）。",
    "引出入籍宣誓文本作为分析对象，转述自己的回复，指出其自誓句为无意义的见证（P032-P036）。"
   ],
   "concept_usage": [
    {"term": "中国人", "meaning": "作者按是否向往和奉行中国的礼仪、理想和道路并自愿自称来界定，明确不以人种、民族、肤色、出身甚至国籍为限。", "evidence": "P020-P021", "ambiguity": "与法律国籍／公民身份的关系未说明。"},
    {"term": "天下", "meaning": "作者用以指无远弗届、四海一家、边界在中国可以企及的最远处的中国。", "evidence": "P015-P017, P020", "ambiguity": "“天下”是否仍有实际边界、与主权国家关系如何，正文未说明。"},
    {"term": "国籍", "meaning": "作者视其为近代才出现的概念，不足以界定“中国人”，并以之质疑“强国”论。", "evidence": "P024-P026", "ambiguity": "作者未讨论国籍在现实法律与政治运作中的效力问题。"},
    {"term": "利益受损", "meaning": "作者指真正的利益受损需以复杂财务知识、分析能力甚至预测能力确认，与情绪受损相区分。", "evidence": "P005", "ambiguity": "“利益”的范围（物质、精神）未界定。"},
    {"term": "情绪毒瘾", "meaning": "作者对自称受损者情绪状态的贬称，用来解释排外冲动的来源。", "evidence": "P007", "ambiguity": "是修辞性说法还是严格心理学判断，正文未说明。"}
   ],
   "examples_and_targets": [
    "喜马拉雅、帕米尔高原、沙漠、西伯利亚冰原、太平洋：作者举为前五千年圈定中国的地理围墙，并称今天已不足以界定中国（作者论据）。",
    "《英特纳雄耐尔》：作者要求对方重溫并回想的文本（引用／修辞材料，用作反驳帮派式民族主义的依据）。",
    "“狄夷入华夏，则华夏之”：作者引以支持以文化而非血统界定中国（引用材料，未标出处）。",
    "“普天之下，莫非我土；率土之滨，莫非我民”：作者引作收束语（引用／修辞材料，未标出处）。",
    "美国入籍宣誓文本（P033，quote 字段）：作者引用的分析对象，说话者为宣誓文本本身，不是作者的话。",
    "“入籍宣誓”：作者叙述很多人纠结的对象（他人心态，非作者立场）。",
    "“ta”：作者用来泛指不特定第三人、规避性别指称的写法（书写习惯）。"
   ],
   "conditions": [
    "“爱与不爱”的判据明确以“被爱的对象的利益”为准（P003-P004）。",
    "时间条件：前五千年被山川沙漠冰原大洋围住，而“今天这些已经不再是足以界定中国的围墙了”（P016）。",
    "中国人身份的认定条件：向往和奉行中国的礼仪、理想和道路，并自己愿意称中国人（P020-P021）。",
    "一般条件：确认利益是否受损需要很复杂的财务知识和分析能力甚至预测能力（P005）。",
    "反问中的假设条件：假设中国是一个帮派、假设这是中国的“生存之道”——均由作者设为对方逻辑再予驳斥（P011-P012）。"
   ],
   "rhetoric_and_tone": "通篇质问、训诫与贬抑语气：密集使用反问（“轮得到‘国籍’来教中国人什么叫中国人？”），排比（“玩‘国籍’、搞‘站队’、论‘种族’、分‘左右’”），口语化詈语（“什么狗屁‘国籍’？”），第二人称直呼“你”“你们”；以《英特纳雄耐尔》和“普天之下，莫非我土”作修辞支撑；结尾由激昂训诫转为对入籍宣誓文本的冷静拆解，称其自誓句为“无意义的见证”。",
   "unresolved_questions": [
    "正文在 P036 以“因为这句……是无意义的见证”结束，对“为何是无意义的见证”未展开，疑为截断或未写完，需核验完整版本。",
    "P033 为 quote 字段的美国入籍宣誓文本，正文未标明其说话者与来源出处。",
    "“天下”“中国人”与法律意义上的国籍、公民身份之间的关系，正文未说明。",
    "“狄夷入华夏，则华夏之”“普天之下，莫非我土”等引语未标出处，需外部核查。",
    "“有人”“你们”所指的具体人群未明确。",
    "updated_at（2025-02-03）晚于 published_at（2021-07-06），是否经过修订、修订何处无法判断（provenance、superseded 均为 null）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "爱与不爱，不是取决于爱的人自己的利益是否受损", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "而是取决于被爱的对象的利益是否受损", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "确认利益是否受损，是需要很复杂的财务知识和分析能力甚至预测能力的", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "更确切的说，只是ta的情绪毒瘾", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "所以必欲除你而后快，如此而已", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "为了吓阻“叛徒”？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "你觉得中国是一个帮派，需要靠分出中国人和非中国人", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "觉得这是中国的“生存之道”？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "中国是天下", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P019", "quote": "中国何止并不止是中国人的中国", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "今天这些已经不再是足以界定中国的围墙了", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P020", "quote": "中国的边界在中国可以企及的最远处", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "懂得礼义廉耻、揖让进退、天下为公，愿称自己中国人，ta就是中国人", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "是其他中国人有义务接纳ta，不是其他中国人有权力拒绝ta", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "国籍是什么年代出现的概念？中国是什么时候出现的概念？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "轮得到“国籍”来教中国人什么叫中国人？", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P013", "quote": "我看你是需要重新温习一下《英特纳雄耐尔》，回想一下它唱的是什么。", "relation": "contradicts"},
    {"key": "E18", "paragraph_id": "P034", "quote": "这就是配合一下对方的自欺欺人", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P036", "quote": "因为这句“我在此自由宣誓，绝无任何心智障碍、借口或保留”是无意义的见证。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学", "民族与国家认同", "国际移民与国籍"],
   "issue_candidates": ["加入外国国籍是否等于不爱国", "以国籍界定民族认同", "排外与帮派式民族主义", "入籍宣誓的意义"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "训诫"],
   "object_candidates": ["中国", "中华民族", "非中国籍华人", "美国入籍宣誓", "《英特纳雄耐尔》", "喜马拉雅", "帕米尔高原", "太平洋"],
   "working_keywords": ["国籍", "爱国", "天下", "正统", "异己", "情绪毒瘾", "自欺欺人", "无意义的见证"]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 36 段（含 1 个 quote 段 P033）全部读完，status=read、full_text_checked=true。P033 是引用的美国入籍宣誓文本，已按引用材料处理，未归为作者主张；P034 是作者转述自己此前的回复（author_reported）。brief 与 P001—P005 开头重合，仅作导航，未用于支持主张。平台为知乎，Q001 属提问者，与作者改述后的立场已区分。正文结尾（P036）疑为截断；updated_at 晚于 published_at，是否修订无法判定。"
 },
 "3e952728": {
  "analysis": {
   "question_context":"回应Q001关于上海离婚案抚养费裁定；作者强调现实执行效果而非抽象说理。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010"],"summary":"作者称拒绝承担抚养义务者可隐瞒收入、转移财产、拒付并拖延执行，法院可将抚养费压低。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P011","P012","P013","P014"],"summary":"作者认为判决的现实效果是让子女认识父母的廉价与缺席，法律使违约较易且后果不足，损害总体利益。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者认为现实中逃避离婚后抚养义务的手段多且成本低、成功率高、几乎无风险。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者列举隐瞒收入、假称失业、转移财产、拒付和拖延强制执行等方式。","evidence":["E3"]},{"claim_id":"C003","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"作者认为这类判决实际损伤总体利益，因为违约较容易且后果有限。","evidence":["E4"]}],
   "argument_steps":["把法律说理与实际判决效果区分。","列举规避和拖延执行路径。","据此评价制度后果并以反讽收束。"],
   "concept_usage":[{"term":"抚养义务","meaning":"离婚后对子女承担的经济供养责任。","evidence":"P003","ambiguity":"未讨论具体法定计算标准。"},{"term":"强制执行","meaning":"判决后由法院促成履行的程序。","evidence":"P007","ambiguity":"作者未给案例来源或执行数据。"}],
   "examples_and_targets":["隐瞒收入、失业、转移财产、拒付（P006-P009）——作者列举的规避方式","抚养金压到400至2000（P008）——金额例子","Q001与上海案例——回应对象"],
   "conditions":["作者的判断限定在‘实践上会怎么判’（P002）","‘靠失业、困难’是拖延与降低金额的条件（P008）"],
   "rhetoric_and_tone":"警告式、愤懑和反讽，连续列举后以‘祝好运’冷峻收尾。",
   "unresolved_questions":["文中金额、执行成功率和法律判断未给出处。","未区分个案裁量与普遍制度规则。","未提出具体改革方案。"],
   "evidence":[{"key":"E1","paragraph_id":"P003","quote":"有大量的手段逃脱离婚后的抚养义务","relation":"supports"},{"key":"E2","paragraph_id":"P005","quote":"基本没有风险。","relation":"supports"},{"key":"E3","paragraph_id":"P006","quote":"可以隐瞒收入，可以‘失业’，可以转移财产，可以直接拒付","relation":"supports"},{"key":"E4","paragraph_id":"P012","quote":"这种判决真正损伤的是人的总体利益。","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates":["婚姻法","子女抚养","司法执行"],"issue_candidates":["抚养费裁定","拒付与执行","制度后果"],"text_function_candidates":["案例评论","制度批评"],"object_candidates":["离婚父母","子女","法院执行"],"working_keywords":["抚养费","拒付","强制执行","隐瞒收入"]
  },
  "notes":"无图片；金额与法律效果均按作者陈述记录，未作外部核验。"
 },
 "43a31d80": {
  "analysis": {
   "question_context":"回应Q001关于中国书法家如何评价日本书道；作者先定义书法本体，再比较两种传统。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007"],"summary":"作者把书法本体定义为可用于书写一切文字的字体及字体系统，碑帖等只是投射和承载物。","role":"definition"},{"unit_id":"U002","paragraph_refs":["P008","P009","P010"],"summary":"作者以中国一生专写一个字仅算艺术家、日本类似行为可称书道为对比，批评后者多为短小文字画。","role":"comparison"},{"unit_id":"U003","paragraph_refs":["P011","P012","P013","P014","P015","P016","P017","P018","P019","P020","P021"],"summary":"作者提出中国传统要求人、文、书一体，字体成为日常写作和精神表达的载体，因此称为书法。","role":"claim"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者认为书法作品的本体是字体，而非单件碑帖、匾额或奇趣小品。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"作者以可书写长篇和完整文字创作为标准，认为中国书法与日本书道存在传统要求差异。","evidence":["E3"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者把中国书法理想概括为人、文、书一体，使字体成为一生行文和表达的自然载体。","evidence":["E4","E5"]}],
   "argument_steps":["先定义字体为书法本体。","用临摹、成家和作品承载物说明定义。","以单字创作和日本书道作比较。","以苏轼、颜真卿、毛润之及日常书写说明人文书一体。"],
   "concept_usage":[{"term":"体","meaning":"可贯穿全部文字创作的字体或字体系统。","evidence":"P003-P005","ambiguity":"未讨论现代字体设计与书法边界。"},{"term":"文字画","meaning":"作者对日本短小书道作品的批评性称呼。","evidence":"P010","ambiguity":"是作者评价，未代表日本书道所有实践。"}],
   "examples_and_targets":["碑帖、匾额、扇面、条幅（P007）——承载物","苏轼用苏字写苏词、颜真卿用颜体写颜书（P012）——正面例证","中国单写‘龙’字与日本书道（P008）——比较例子","Q001——回应对象"],
   "conditions":["‘学会’被限定为能用字体完成一切必要文字创作（P004）","中国书法理想要求日常信件、文章均能使用所习字体（P016）"],
   "rhetoric_and_tone":"定义式、比较式，带明显价值判断；通过反复对照‘字体’与‘小品’建立论旨。",
   "unresolved_questions":["日本书道的概括是否代表多样传统，正文未核验。","‘中国书法家眼里’没有引述具体书法家或调查。","字体本体论未处理抽象字体与具体笔迹关系。"],
   "evidence":[{"key":"E1","paragraph_id":"P002","quote":"书法的作品，是字体。","relation":"supports"},{"key":"E2","paragraph_id":"P007","quote":"只是这个真正的本体的投射物和承载物","relation":"supports"},{"key":"E3","paragraph_id":"P010","quote":"它与其说是‘书’，不如说是‘文字画’","relation":"supports"},{"key":"E4","paragraph_id":"P013","quote":"要你为人、文、书一体，三花聚顶。","relation":"supports"},{"key":"E5","paragraph_id":"P021","quote":"所以中国的这门技艺，谓之书法。","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates":["书法理论","艺术比较","汉字文化"],"issue_candidates":["书法本体","中国书法与日本书道","字体与文字创作"],"text_function_candidates":["艺术理论","跨文化比较"],"object_candidates":["中国书法","日本书道","字体"],"working_keywords":["字体","体","人文书一体","文字画"]
  },
  "notes":"无图片；对日本书道的概括是作者观点，未作为外部事实确认。"
 },
 "0d8a4deb": {
  "analysis": {
   "question_context":"回应Q001关于‘被欣赏被利用’是否等于物化及其标准；作者区分一般分工利用与无视权利。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007"],"summary":"社会分工本来互相利用劳动力和资源，顾客使用复印店或餐厅服务不自动构成物化。","role":"distinction"},{"unit_id":"U002","paragraph_refs":["P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019"],"summary":"物化的核心是无视人说不的权利，表现为不给机会、不给条件或无视明确拒绝。","role":"definition"},{"unit_id":"U003","paragraph_refs":["P020","P021","P022","P023","P024"],"summary":"这些手段把人转成任意处置的物件，使用者不再视其为同类，只按总体习性和产出研究。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"negated","statement":"作者否定‘利用人’本身就是物化，认为分工合作必然包含劳动力和资源的相互利用。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者把物化定义为无视人的权利，重点是不考虑其说不的权利。","evidence":["E2"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"不给知情选择机会、制造无法拒绝的贫困条件、或在明确拒绝后继续骚扰，都会把人转向物。","evidence":["E3","E4"]}],
   "argument_steps":["用商业服务例子排除一般利用。","提出说不权利作为标准。","分别解释机会、条件和拒绝三种侵害。","以纳粹和殖民主义类比说明彻底物化。"],
   "concept_usage":[{"term":"物化","meaning":"通过消灭选择和拒绝权，把人当作任意处置的物件。","evidence":"P008-P024","ambiguity":"未讨论权利冲突或同意瑕疵的边界。"}],
   "examples_and_targets":["复印店、餐厅（P002-P003）——正常利用","只给一个选择、不询问决定（P014-P015）——剥夺机会","制造贫困、继续撕衣骚扰（P017-P019）——剥夺条件和无视拒绝","纳粹与殖民主义（P021-P022）——极端类比"],
   "conditions":["只有在无视权利而非单纯使用服务时才称物化（P008）","‘说不’须有机会、条件且被实际尊重（P010-P019）"],
   "rhetoric_and_tone":"先用反问和日常例子澄清，再用定义、分项和历史极端类比强化警告。",
   "unresolved_questions":["未说明商业雇佣中权力不对称何时越过物化界线。","极端历史类比的适用范围未限定。","没有讨论未明确拒绝但无法自由同意的情形。"],
   "evidence":[{"key":"E1","paragraph_id":"P005","quote":"社会分工合作本来就是互相利用劳动力和资源。","relation":"supports"},{"key":"E2","paragraph_id":"P008","quote":"‘物化’是指无视人的权利——这重点是指不考虑人说‘不’的权利。","relation":"supports"},{"key":"E3","paragraph_id":"P014","quote":"根本不让你知道有别的选择存在，从知识上就消灭了说不的可能。","relation":"supports"},{"key":"E4","paragraph_id":"P019","quote":"你说了不要，还是继续撕你衣服，继续对你说黄色笑话","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates":["伦理学","权利与同意","社会分工"],"issue_candidates":["物化标准","拒绝权","劳动利用与权利侵害"],"text_function_candidates":["概念澄清","伦理论证"],"object_candidates":["劳动者","服务使用者","被骚扰者"],"working_keywords":["物化","利用","说不","无视权利"]
  },
  "notes":"无图片；以作者提出的‘说不权利’为工作定义，未补入其他伦理学定义。"
 },
 "2d01ce4c": {
  "analysis": {
   "question_context":"回应Q001关于情感挽回大师能否挽救失恋；作者建议不要参与，并把所谓复合术解释为改变他人自由意志的暴力黑盒。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008"],"summary":"作者认为这类手段危险不在于不灵，而在于一旦成功会形成强烈经验和重复依赖，类似毒品。","role":"warning"},{"unit_id":"U002","paragraph_refs":["P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019","P020","P021","P022"],"summary":"复合术被比作黑盒：在沟通失败后改变结果，使使用者反复投入金钱和资源，目标是改变对方自由意志。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034"],"summary":"作者要求尊重对方决定，把自己的失落换成对方的自由，并以爱是否使决定更轻松反问。","role":"advice"},{"unit_id":"U004","paragraph_refs":["P035","P036","P037","P038","P039","P040","P041","P042","P043"],"summary":"作者区分正确的错误与错误的正确，警告某些成功手段可能成为诅咒。","role":"conclusion"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者建议不要参与情感挽回，因为所谓成功会留下强烈经验并诱发反复依赖。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"作者把复合术描述为在正常沟通失败后通过黑盒改变结果，实质上试图改变对方自由意志。","evidence":["E3","E4"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者主张应尊重对方的自由决定，用承担失落换取对方自由。","evidence":["E5"]},{"claim_id":"C004","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"作者提醒结果成功不等于手段正确，某些成功可能成为诅咒。","evidence":["E6"]}],
   "argument_steps":["从成瘾经验说明‘灵了’的后患。","把复合术抽象为黑盒和暴力。","将伦理标准转为尊重自由意志。","以成功与正确的区分收束。"],
   "concept_usage":[{"term":"黑盒子","meaning":"不透明但能改变关系结果的复合手段。","evidence":"P010-P021","ambiguity":"未指明具体技术或骗局类型。"},{"term":"自由意志","meaning":"对方拒绝或决定关系的自主权。","evidence":"P021-P026","ambiguity":"未讨论胁迫、误导与自主的边界。"}],
   "examples_and_targets":["赌博、占卜、暴力（P004）——成瘾类比","充钱、加大功率（P017-P019）——依赖升级","失恋者与被挽回对象（P011-P023）——关系情境"],
   "conditions":["作者的警告针对沟通已失败、对方明确决定后仍求助黑盒（P011-P014）","‘如果那是爱’引出尊重自由的规范条件（P031-P033）"],
   "rhetoric_and_tone":"强烈警告、类比密集，使用毒品、黑盒和不归路意象，末尾转为伦理追问。",
   "unresolved_questions":["未提供警方案件或行业事实来源。","‘复合术’的实际内容和有效性未核验。","作者关于成瘾和自由意志的心理机制是概括性判断。"],
   "evidence":[{"key":"E1","paragraph_id":"P001","quote":"不要参与任何这类‘情感挽回’的尝试。","relation":"supports"},{"key":"E2","paragraph_id":"P002","quote":"它‘灵了’会有无穷尽的后患。","relation":"supports"},{"key":"E3","paragraph_id":"P009","quote":"这种‘复合术’的本质是什么呢？实际上是对人的一种暴力。","relation":"supports"},{"key":"E4","paragraph_id":"P021","quote":"你是要靠着这黑盒子，改变别人的自由意志。","relation":"supports"},{"key":"E5","paragraph_id":"P023","quote":"学会尊重和接受ta人的自由意志的决定","relation":"supports"},{"key":"E6","paragraph_id":"P041","quote":"某些手段，你如果用它‘成功’了，对你并不是一种经验，而会是一个诅咒和厄运。","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates":["亲密关系","伦理","心理与成瘾"],"issue_candidates":["情感挽回服务","自由意志","关系边界"],"text_function_candidates":["警示","伦理劝告"],"object_candidates":["失恋者","情感挽回大师","伴侣"],"working_keywords":["复合术","黑盒子","自由意志","正确的错误"]
  },
  "notes":"无图片；未把作者对案件和‘复合术’的概括当作外部事实。"
 },
 "462c1386": {
  "analysis": {
   "question_context":"回应Q001在无神论与基督教伴侣关系中应确认什么；作者把重点转为双方是否真正理解自己所宣称的身份。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009"],"summary":"作者称严格无神论者和真正基督徒都极少，许多人只是无知的身份模仿者，尚不足以谈终身托付。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P010","P011","P012","P013","P014","P015","P016"],"summary":"信仰被定义为在痛苦、危机或认知判断中仍坚持的根本确信；主动追求信仰需要运气和能力。","role":"definition"},{"unit_id":"U003","paragraph_refs":["P017","P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033"],"summary":"作者给出无神论者的五项终身标准，并警告年轻人不能凭自信声称身份。","role":"criteria"},{"unit_id":"U004","paragraph_refs":["P034","P035","P036","P037","P038","P039","P040"],"summary":"过早身份认同可缓解焦虑却会使重大决策建立在虚妄自信上；身份焦虑应通过接受现实身份解决。","role":"advice"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"作者认为中国严格意义上的无神论者和真正基督徒都极少，多数是基于无知的身份模仿者。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者把信仰理解为人在危机或认知判断中持续坚持的根本确信，并认为主动追求信仰需要特殊经历与能力。","evidence":["E3","E4"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者用五项行为标准界定严格无神论者，并要求这些标准经受终身实践而非自信预期。","evidence":["E5","E6"]},{"claim_id":"C004","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"作者认为年轻人过早以某种身份抱团会把职业、亲密关系、婚姻和投资建立在虚妄自信上。","evidence":["E7"]}],
   "argument_steps":["质疑双方身份标签的真实性。","定义信仰并举物质守恒为例。","列出无神论标准并强调终身检验。","把身份焦虑与人生决策风险联系起来。"],
   "concept_usage":[{"term":"cosplay无神论者/基督徒","meaning":"作者对只模仿身份、未理解其要求者的贬称。","evidence":"P004-P006","ambiguity":"非宗教学术术语。"},{"term":"无神论者","meaning":"作者按不祈祷、不归因惩罚、不与亡者对话、不占卜且无命运观念定义。","evidence":"P021-P026","ambiguity":"标准极严格，未与哲学或宗教学定义比较。"}],
   "examples_and_targets":["ICU、高考、战壕祈祷（P021-P023）——无神论标准","扫墓、占卜、护身符（P024-P026）——标准例子","婚姻、职业、投资（P034）——身份误用后果","Q001伴侣关系——回应对象"],
   "conditions":["作者要求标准在真实危机中表现，而非靠‘自信’预期（P029-P031）","身份焦虑须靠接受现实身份而非虚构无痛苦身份解决（P037-P039）"],
   "rhetoric_and_tone":"挑衅、训诫和夸张并用，先贬斥身份模仿，再以清单和人生警告加强权威感。",
   "unresolved_questions":["‘四位数’和‘极大概率’无统计来源。","五项标准是否代表无神论共识未说明。","对伴侣应确认的具体沟通问题没有直接列出。","信仰与认知信念的定义有概念扩张。"],
   "evidence":[{"key":"E1","paragraph_id":"P001","quote":"严格意义上的无神论者能凑得齐四位数都够呛。","relation":"supports"},{"key":"E2","paragraph_id":"P006","quote":"绝大部分都是基于无知的‘cosplay基督徒’。","relation":"supports"},{"key":"E3","paragraph_id":"P010","quote":"信仰都是要有极大痛苦和磨难做底的","relation":"supports"},{"key":"E4","paragraph_id":"P013","quote":"你不会立马相信这人是神仙，而是会深信不疑这肯定是障眼法","relation":"supports"},{"key":"E5","paragraph_id":"P021","quote":"真正的无神论者进ICU、上高考考场、进战壕不以任何形式向老天爷、上帝、佛祖、祖先祈祷","relation":"supports"},{"key":"E6","paragraph_id":"P029","quote":"注意这都是终身到死的要求。","relation":"supports"},{"key":"E7","paragraph_id":"P034","quote":"会诱导自己将重大的人生决策——职业、亲密关系、婚姻、投资——建立在虚妄的自信上。","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates":["宗教与无神论","亲密关系","身份认同"],"issue_candidates":["信仰真实性","无神论标准","身份焦虑与伴侣关系"],"text_function_candidates":["概念定义","关系劝告","训诫"],"object_candidates":["无神论者","基督徒","伴侣"],"working_keywords":["cosplay信仰","无神论标准","信仰","身份焦虑"]
  },
  "notes":"无图片；作者的严格定义和数量判断均按作者观点记录，未作宗教学裁定。"
 },
 "38f8ab69": {
  "analysis": {
   "question_context":"回应Q001关于‘看似很傻、实则聪明’的行为；作者把答案集中为认错，并讨论责任、关系和团队中的先手。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009"],"summary":"认错不是倒霉而是技能；真诚认错证明尚有安全感、理智和改进余力。","role":"claim"},{"unit_id":"U002","paragraph_refs":["P010","P011","P012","P013","P014","P015"],"summary":"认错建立在高道德要求和持续强大上，也可成为示强并赢得敬意。","role":"argument"},{"unit_id":"U003","paragraph_refs":["P016","P017","P018","P019","P020","P021","P022","P023","P024","P025","P026","P027","P028"],"summary":"认错不是迎合指责，而是基于更全面的信息自我诊断；领导者需洞察症结并承担不同于对方期待的责任。","role":"qualification"},{"unit_id":"U004","paragraph_refs":["P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040","P041","P042","P043","P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054","P055","P056"],"summary":"责任关系需要一方先认一点；作者给出情绪失控、表达不清、未充分体谅感受三种‘完美错误’，说明可真实承认且仍可改善。","role":"method"},{"unit_id":"U005","paragraph_refs":["P057","P058","P059","P060","P061","P062","P063","P064","P065","P066","P067","P068","P069","P070","P071","P072","P073","P074","P075","P076","P077","P078","P079","P080","P081","P082","P083","P084","P085","P086"],"summary":"作者承认先担责可能吃亏，但认为承担训练会带来实力地位；团队按责任逃避程度分配替罪羊，先手可测试组织是否值得留下。","role":"advice"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"作者认为准确而真诚的认错是展示安全感、理智、道德勇气和领导能力的重要技能。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"认错不等于按对方指责逐字道歉，而是基于更全面信息找到自己应改变的症结。","evidence":["E3"]},{"claim_id":"C003","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"先承认有限且真实的责任可打破互相拒绝承担责任的僵局，作者列出三种可作为起点的普遍错误。","evidence":["E4","E5"]},{"claim_id":"C004","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"组织中责任实际常按实力地位和脆弱性流动，逃避责任者可能成为替罪羊；主动承担可测试团队并获得联盟。","evidence":["E6","E7"]}],
   "argument_steps":["把认错从风险行为重定义为能力。","以安全感、道德勇气和伦理洞察解释其价值。","提出三个‘完美错误’作为可承认的真实起点。","将个人担责连接到团队责任分配和组织筛选。"],
   "concept_usage":[{"term":"完美错误","meaning":"普遍存在、承认不至于虚假且确实可改进的责任表述。","evidence":"P035-P056","ambiguity":"作者未说明三类是否穷尽。"},{"term":"实力地位","meaning":"由承担责任、提供安心和不可替代性带来的组织位置。","evidence":"P060-P064","ambiguity":"属作者的组织解释。"}],
   "examples_and_targets":["情绪失控、表达/理解不清、未充分体谅感受（P036-P050）——认错模板","跳舞与拱桥（P030-P034）——互相担责类比","月薪一万与损失两千（P075）——低成本试探责任","替罪羊逻辑（P069-P073）——团队责任机制"],
   "conditions":["真诚认错不包括假意道歉（P006）","认错须基于自我信息和深思而非照单应承（P022-P027）","不建议对承担不起的责任随便冒险（P075）","先手结果可作为判断组织去留的试验（P076-P80）"],
   "rhetoric_and_tone":"训诫与教练式劝告，兼用比喻、排比和粗粝口语；从个人修养扩展到冷峻的组织现实主义。",
   "unresolved_questions":["责任流动的组织判断是作者经验性概括，未给数据。","‘认错’与承担不属于自己的责任的边界需进一步说明。","文章标记‘未完，待续’，后续论证缺失。","具体团队中如何保护先担责者未讨论。"],
   "evidence":[{"key":"E1","paragraph_id":"P006","quote":"每一个真诚认错和道歉（假意的不算）的人，都有富余的安全感。","relation":"supports"},{"key":"E2","paragraph_id":"P014","quote":"这种不惮于认错的习惯本身就是一种无言的示强","relation":"supports"},{"key":"E3","paragraph_id":"P027","quote":"只有这样经过深思熟虑的自检后认错——而不是简单的按照对方的期待应承了事","relation":"supports"},{"key":"E4","paragraph_id":"P030","quote":"互不认错，拒绝承担责任，是一座越压越结实的石拱桥。","relation":"supports"},{"key":"E5","paragraph_id":"P037","quote":"怪我没有控制好情绪。","relation":"supports"},{"key":"E6","paragraph_id":"P064","quote":"真正决定责任到底会如何分配的，是这种实力地位和脆弱性的对比","relation":"supports"},{"key":"E7","paragraph_id":"P076","quote":"你用了极低的成本就正确判断出了这地方不该呆下去。","relation":"supports"}]
  },
  "provisional_tags": {
  "domain_candidates":["组织与责任","人际关系","领导力"],"issue_candidates":["认错与道歉","责任分配","团队筛选","领导伦理"],"text_function_candidates":["职场劝告","伦理论证","方法建议"],"object_candidates":["认错者","责怪者","团队成员","领导者"],"working_keywords":["认错","完美错误","责任","替罪羊","实力地位"]
  },
  "notes":"无图片；P086明确标记未完待续，已保留为未决范围限制。"
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
