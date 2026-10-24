# -*- coding: utf-8 -*-
"""批次 r001-b0018 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0018.sessions.py            # 写 out/r001-b0018.out.jsonl
  python3 records/r001-b0018.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0018"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0018.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "fe88ea15": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么随着中国的崛起，周边小国普遍表现出了敌对态度而非顺从局势、积极配合。这一“普遍敌对”的前提与“为什么”属于提问者。作者没有直接回答该“为什么”，而是先指出：在中国大流量网站采样即可让各国情报机构得出“中国强大后可能谋求霸权”的结论，本问题下大量答主也以“能不能欺压其他国家”作为“中国强大”的鉴定指标；随后把重点转向反驳“这是必然而正常的”这一推论，最后落到中国应如何自处、何为荣辱。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003", "P004"],
     "summary": "以中国网络舆论采样为据，指出外界足以据此推断中国强大后会威胁邻国；并反问以“欺压他国”为强大标准的人是否真是极少数、他国能否不害怕。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010"],
     "summary": "增补段：批评从“以前发生过/某国发生过”推出“必然、正常”的思维定势，主张必然性要由内部机制与内在逻辑论证，而不是靠现象的重复认证。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020"],
     "summary": "逐环拆解“常见→正常→健康→什么都不必做”的推进，称“健康”是伪认证，是封建王朝式推卸公共责任、免除超越现状义务的把戏。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P021", "P022", "P023", "P024"],
     "summary": "称这是要在“一切正常”中看出不正常的世代；以ABS、无线通信出现之前无人认为其必要作类比。",
     "role": "example"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P025", "P026", "P027", "P028"],
     "summary": "即使没有先例、没有有把握的策略、他国戒惧是普遍或必然的，中国也要争取和平发展并使其戒惧最小化乃至消除；讨论“为什么”应指向“应该怎么办”。",
     "role": "action_advice"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040"],
     "summary": "以荣辱立论：人因我强而恐惧是耻辱、令人欢欣鼓舞才是荣耀；强大应被用来造福他人以换取拥护帮助，用于掠夺欺压则愚蠢。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"],
     "summary": "主张中国人该有中国式的民族主义，用“不屑”“让路人受连累就算我输”等自述式排比描述这种傲慢，并训诫读者“连傲慢都不会”。",
     "role": "claim"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": ["P057", "P058"],
     "summary": "结尾限定：作者仍不赞同民族主义，但更厌恶不敢承认自己、把榜样帽子戴在美国人头上的“美式民族主义”。",
     "role": "qualification"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出：只要在中国大流量网站稍微扩大采样，就足以支撑各国情报机构作出“中国如果强大，可能在民族主义情绪裹挟下对周边国家谋求极大霸权”的结论；本问题下多数答主也以“能不能欺压其他国家”作为“中国强大了”的鉴定指标。",
     "evidence": ["E1", "E2"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问：以“能不能欺压其他国家”鉴定“中国强大”的人是否真是“极少数”，其他国家能不能不害怕。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否定从“以前发生过/某国发生过”推出“这现象是必然的、正常的”这一思维定势；他认为即使真的没有过例外，也必须谈内部机制与内在逻辑，而不能仅凭现象的重复认证必然性，否则是对经验的迷信、对理性的背叛。",
     "evidence": ["E4", "E5", "E6"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否定“常见即正常、正常即健康、健康即什么都不必做”的连锁推进，称把现状认定为“健康”是意义甚小的伪认证，是为“无需采取行动”找的借口。",
     "evidence": ["E7", "E8"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定这种以“健康”盖章免除行动的做法，本是封建王朝利用人对经验的原始崇拜而创造的推卸公共责任的把戏。",
     "evidence": ["E9"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张：即使世上没有先例、找不到任何有把握的策略，中国也要寻求并尝试和平发展；即使他国戒惧心是“普遍的”“难以避免/必然”的，也要采取措施争取其最小化乃至完全消除。",
     "evidence": ["E10", "E11"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张讨论“为什么会这样”的唯一指向应是谈清之后讨论“应该怎么办”，而不是谈出“这是正常的”然后散会；若还从中谈出“民族自豪感”，则简直是不知好歹。",
     "evidence": ["E12", "E13"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定：人因为我强而恐惧是耻辱，因为只有流氓才会导致这种反应；人因为我强而欢欣鼓舞、觉得看见希望，才是荣耀，是君子之道、为王之道的方向。",
     "evidence": ["E14", "E15"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张强大是为了拥有更强的造福于ta人的力量，从而得到ta人出于自利本能而自发生出的拥护和帮助；若把强变成掠夺和欺压的本钱，则是愚蠢。",
     "evidence": ["E16", "E17"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "结尾作者明确声明自己仍然并不赞同民族主义；但他更厌恶站民族主义还站下三路、连自己都不敢承认、乃至于把榜样帽子戴在美国人头上的“美式民族主义”。",
     "evidence": ["E18", "E19"]
    }
   ],
   "argument_steps": [
    "先承认对方的经验前提：中国网络舆论的样本足以让他国得出“中国强大后会谋求霸权”的判断（P001-P003）。",
    "以反问把“这只是极少数人的观点”这一辩解打掉，并指出他国的恐惧有现实来源（P004）。",
    "转入方法论反驳：从先例的重复推不出必然性，必然性需要内部机制与内在逻辑（P007-P010）。",
    "再拆“常见—正常—健康—不必行动”的链条，用疾病与压迫的反例说明“常见”不等于“正常”，更不等于“健康”（P011-P014）。",
    "指出“健康”是伪认证，是把“暂时顾不上”包装成“本来什么都不用做”以推卸责任（P015-P019）。",
    "以ABS与无线通信在出现前同样“没有必要”作类比，支持“无先例不等于不该做”（P022-P023）。",
    "给出行动结论：无先例、无策略、他国戒惧普遍，仍要和平发展并设法消除戒惧（P025-P027）。",
    "把讨论目的钉在“应该怎么办”，并以“民族自豪感”作为反面靶子（P028-P029）。",
    "以荣辱标准收束：因强致惧是耻辱，因强致人欢欣是荣耀；强应用于造福他人而非掠夺（P030-P040）。",
    "转向民族主义话题，提出中国式民族主义与其“不屑”的自述（P041-P056）。",
    "最后自我限定：不赞同民族主义，但更厌恶伪装的流氓民族主义（P057-P058）。"
   ],
   "concept_usage": [
    {"term": "必然性", "meaning": "作者用它特指需要由内部机制与内在逻辑论证的必然，而非由现象重复“认证”的必然；他指出后者是迷信经验、背叛理性。", "evidence": "P009", "ambiguity": "文中未给出判定“内部机制”成立的标准"},
    {"term": "健康", "meaning": "作者把“健康”当作对现状的伪认证：一旦盖章，不行动就被说成“本来也什么都不用做”。", "evidence": "P017", "ambiguity": "作者未给出何为“健康”的正面标准，只反问“人类知道什么是健康吗”"},
    {"term": "民族主义", "meaning": "作者说自己并不赞同民族主义，但主张若谈民族主义，中国人应有中国式的民族主义，并以“不屑”区别于下三路的流氓民族主义。", "evidence": "P041", "ambiguity": "“中国式的民族主义”具体内涵主要靠排比与自述呈现，未作定义"},
    {"term": "傲慢", "meaning": "文中“傲慢”是作者自称的正面品质（不屑于靠剥削续命），不是通常意义的贬义。", "evidence": "P043", "ambiguity": "与“流氓民族主义”的界线由作者语气划定，未形式化"}
   ],
   "examples_and_targets": [
    "ABS系统：作者类比证据，说明在它出现前汽车在冰面侧滑并不证明ABS无必要（P022）。",
    "无线通信/电话：同类类比，说明“从来如此”不能推出“不可能”（P023）。",
    "“一騎灭国”“虽远必诛”：作者的反驳对象/修辞靶子，指借此类口号自我高潮者（P034）。",
    "“人不知而不愠，不亦君子乎”：作者引用经典为自己的荣辱观作依据（P031）。",
    "“得道多助”：作者引用的判断，用以说明多助者能强到本来做不到的强（P038）。",
    "“子路即死，其冠亦正”：作者引用的典故，用以形容其推崇的傲慢（P054）。",
    "民族自豪感、美式民族主义：作者批评的对象（P029、P057-P058）。"
   ],
   "conditions": [
    "前提条件：只要能在中国大流量网站稍微扩大采样，就足以支撑外界得出中国可能谋求霸权的结论（P001）。",
    "让步条件：即使真的没有过例外，也仍要谈内部机制（P009）；即使外国戒惧是“普遍的”“难以避免/必然”的，也要争取消除（P027）。",
    "行动条件：讨论“为什么”只在谈清之后指向“应该怎么办”才有意义（P028）。",
    "区别条件：作者自称不赞同民族主义，只在此限定下谈“中国式的民族主义”（P041、P057）。",
    "未说明：文中所称“采取措施争取其最小化乃至完全消除”未列出具体措施与代价评估。"
   ],
   "rhetoric_and_tone": "训诫与讥讽并用：大量反问（“历史的‘必然性’就这么简单？”“有哪一步站得住脚？”）、粗口与贬称（“正常”是狗娘、混账们、流氓）、夸张自述（富有四海、投鞭断流、云帆蔽日）、排比式的“不屑”与“就算我输”，并以“小朋友们……抄一百遍，家长签字明天交”的口吻训诫读者；结尾用“不要搞错”自我限定。",
   "unresolved_questions": [
    "作者对提问中“周边小国普遍敌对”这一事实前提本身未作核实或讨论，本文主要反驳的是对它的“必然/正常”论证。",
    "文中“中国式的民族主义”与“流氓民族主义”的界线只由语气和例子划出，缺少明确判据。",
    "“采取措施争取其最小化乃至完全消除”未说明具体手段、成本与可行性。",
    "作者称封建王朝创造“推卸公共责任的把戏”属历史断言，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "可能在民族主义情绪的裹挟下对周边国家谋求极大的霸权", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "很多人干脆就是以“能不能欺压其他国家”作为“中国强大了”的鉴定指标", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这样去鉴定“中国强大”的人真的是“极少数”吗？其他国家能不害怕吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "从“以前发生过这种事”“某国发生过这种事”，推出“可见这现象是必然的、正常的”", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P009", "quote": "即使真的没有过例外，仍然要谈论内部机制、内在逻辑去谈论必然性", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "走后一条路，是一种对经验的迷信，是对理性的背叛。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "似乎“常见”意味着“正常”，“正常”意味着“健康”，“健康”意味着“什么都不必做”", "relation": "contradicts"},
    {"key": "E8", "paragraph_id": "P017", "quote": "你都要意识到这是个“伪认证”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "这本来是封建王朝利用人因蒙昧而养成的对经验的原始崇拜而创造的推卸公共责任的把戏", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P025", "quote": "就算世上没有先例，中国也要寻求和平发展。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P027", "quote": "就算其他国家会产生戒惧心是“普遍的”“难以避免/必然”的，我们也要采取措施争取其最小化乃至完全消除。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P028", "quote": "唯一的指向只能是在讨论清楚之后谈论“应该怎么办”，而不是谈出“这是正常的”然后散会", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P029", "quote": "如果甚至还谈出了“民族自豪感”，这就简直是不知好歹。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P030", "quote": "人因为我强而恐惧，这是耻辱。因为只有流氓才会导致这种反应。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P032", "quote": "人因为我强而欢欣鼓舞、而觉得看见希望，才是荣耀。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P037", "quote": "强大是为了拥有更强的造福于ta人的力量，从而得到ta人出于自利的本能而自发生出的拥护和帮助。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P039", "quote": "强如果拿来变成掠夺和欺压的本钱，则道路以目", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P057", "quote": "我仍然并不赞同民族主义", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P057", "quote": "我更厌恶站民族主义还站下三路的流氓民族主义", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P058", "quote": "猥琐成这样，你们累不累？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系/对外形象", "社会心理与舆论", "方法论/逻辑批评", "民族主义话语"],
   "issue_candidates": ["中国崛起与周边国家戒惧", "以先例论证必然性", "常见—正常—健康的话术", "强国之用的荣辱标准", "中国式民族主义"],
   "text_function_candidates": ["答问", "论辩", "批评", "训诫", "檄文式抒情"],
   "object_candidates": ["中国", "周边小国", "各国情报机构", "网络答主", "美国", "封建王朝", "华人"],
   "working_keywords": ["历史必然性", "伪认证", "戒惧心", "和平发展", "得道多助", "流氓民族主义", "美式民族主义", "不屑"]
  },
  "notes": "无图片、正文非空。提问者的问题与“周边小国普遍敌对”的前提已在 question_context 中与作者立场分开。平台话题标签未混入正文。文中含网络化粗口与训诫语气，已在 rhetoric_and_tone 记录；其所引经典（人不知而不愠、得道多助、子路）为作者引用，未归为作者原创判断。"
 },
 "12ec57be": {
  "analysis": {
   "question_context": "提问者（Q001）问：折叠屏的极致会是什么呢？作者没有讨论折叠屏这一形态的极限，而是借题把“最前沿/极致”重新定义为视觉输入技术的极限与终极方向，并从“视觉是什么”讲起。提问中的折叠屏框架属于提问者，作者的答复实际上把折叠屏一类形态归入走向终极形态的中间道路。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "重新界定题目：要谈的不是十二十年内的显示前沿，而是视觉输入技术的极限、终极方向，先从视觉是什么知觉谈起。",
     "role": "definition"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P004", "P005"],
     "summary": "提出视觉不是一堆图像，而是大脑自动化处理后得到的丰富概念性结论；若绕过眼睛给大脑同样结论，会体验到同样画面。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P006", "P007"],
     "summary": "以梦境为证说明视觉不依赖外部图像输入，据此推出终极方向：经脑机接口接入视觉结论处理中枢后端（“密折路线”），不依赖光学显示器件。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P008", "P009"],
     "summary": "判定此前一切中间形态都只是通往终极形态的中间道路，目前技术仍走“锦衣卫路线”，其他分支最终只能作配角。",
     "role": "claim"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P010", "P011", "P012", "P013"],
     "summary": "中间状态里决定步调与转折的是输入形态；决定移动设备显示形态的不是眼睛而是手，“手输入”使柔性屏最多只能是“灵活硬屏”而非“便携大屏”。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P014", "P015", "P016", "P017"],
     "summary": "预测身边放大屏交互的时代已近尾声，十年左右MR眼镜将成主流、输入转向脑机接口；中间态所需的是极小、高刷新、高分辨率、低功耗的电子光学器件，“柔性”对它是多余特性。",
     "role": "conclusion"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P018"],
     "summary": "给柔性显示技术另行指路：归宿大概在建筑与工程方面，方向是耐老化与降低单位亮度能耗，例如军事视觉迷彩。",
     "role": "action_advice"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者把要讨论的“最前沿”界定为视觉输入技术的极限、终极方向，而不是十年二十年内的显示形态。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张人类真正的视觉是大脑对图像自动化处理后得到的丰富概念性结论，而非图像本身；若以巧妙方式绕过眼睛让大脑获得同样结论，会感受到同样画面。",
     "evidence": ["E2", "E3"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以梦境（有完整视觉但眼睛无输入信号）为证，主张视觉不依赖外部图像；因此视觉技术的终极方向是经脑机接口直接接入视觉结论处理中枢后端（“密折路线”），完全不依赖光学部门、无需光学显示器件。",
     "evidence": ["E4", "E5", "E6"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定目前的视觉输入技术终究仍在走“锦衣卫路线”，只有指向“密折路线”的后续发展会最终被历史接纳，其他分支最终只能作为配角。",
     "evidence": ["E7", "E8"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张在走向终极的中间状态里，决定步调和转折的是输入形态而非显示形态；决定移动设备显示形态的不是眼睛，而是手。",
     "evidence": ["E9", "E10"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为“手输入”决定了“柔性屏”最多只能是“灵活硬屏”（以双手合握、拇指可及的空间范围为上限），而不太能是需借助鼠标、触摸板等传感器的“便携大屏”。",
     "evidence": ["E11"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预测身边放大屏并与之交互的时代已接近尾声：未来十年左右，MR眼镜会替代手持或桌面显示屏成为主流，输入从手指转向脑机接口，保留外部大屏将变得毫无必要且不经济。",
     "evidence": ["E12", "E13"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为走向终极所需的中间态是极小尺寸、极高刷新率、极高分辨率、极低功耗的电子光学器件，而对这一核心组件来说“柔性”是全然多余、没有意义的特性。",
     "evidence": ["E14", "E15"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者判断柔性显示技术不是为桌面电脑或随身设备而生，其归宿大概在建筑与工程方面，应朝耐老化与降低单位亮度能耗发展，例如用作军事装备的视觉迷彩。",
     "evidence": ["E16", "E17"]
    }
   ],
   "argument_steps": [
    "先重述题目，把“显示技术最前沿”改述为视觉输入技术的极限与终极方向（P001-P002）。",
    "从视觉的定义入手：视觉是大脑自动化处理图像后得到的概念性结论，所以关键是结论而非图像（P004）。",
    "用思想实验推进：绕过眼睛给大脑同样结论，人会看到同样画面（P004）。",
    "以梦境为经验证据，说明视觉可以无外部图像输入（P006）。",
    "由此推出终极方案：数据不经眼睛，直接经脑机接口送入视觉结论处理中枢后端，即“密折路线”，无需光学显示器件（P006-P007）。",
    "把现有与未来技术放进该框架排序：现在仍走“锦衣卫路线”，其他分支只能是配角（P008-P009）。",
    "转入中间态的判断依据：决定步调的是输入形态；对移动设备而言限制在“手”（P010-P012）。",
    "由“手输入”推出柔性屏的形态上限是“灵活硬屏”，而非卷轴式便携大屏（P013）。",
    "预测近期转折：大屏在身边交互的时代接近尾声，MR眼镜与脑机接口将成主流（P014-P015）。",
    "由此界定核心组件需求，并判定“柔性”对该组件无意义（P016-P017）。",
    "给柔性显示另指方向：建筑与工程，如军事视觉迷彩（P018）。"
   ],
   "concept_usage": [
    {"term": "视觉", "meaning": "作者特指大脑对图像自动化处理后得到的丰富的概念性结论，而非眼睛接收的图像集合。", "evidence": "P004", "ambiguity": "“换句话说”式的等价表述未给出机制细节"},
    {"term": "密折路线", "meaning": "作者自造的比喻：把数据直接送入视觉结论处理中枢后端，绕过眼睛这一“光学采集部门”。", "evidence": "P006", "ambiguity": "与“锦衣卫路线”的划分是比喻性的，未给技术判据"},
    {"term": "灵活硬屏", "meaning": "作者用来指受“手输入”限制的柔性屏上限：以双手合握拇指可及范围为界。", "evidence": "P013", "ambiguity": "与“便携大屏”的界线以输入方式划分，未给尺寸数据"},
    {"term": "柔性", "meaning": "文中指屏幕可弯折的特性；作者主张它对终极形态所需的核心光学器件毫无意义，其价值应在建筑与工程等场景。", "evidence": "P017", "ambiguity": "作者未否认柔性在其它场景的价值，但未展开"}
   ],
   "examples_and_targets": [
    "梦境：作者的关键经验证据，用于证明视觉可脱离眼睛输入（P006）。",
    "锦衣卫/密折：作者自创的比喻，用于比较现有光学路径与脑机接口直连路径（P006）。",
    "折叠屏：提问者的话题，作者未正面讨论其形态极限，只把它归入中间形态（P001-P002、P008）。",
    "MR眼镜（未来十年左右的主流预测）：作者的预测对象（P015）。",
    "军事装备的视觉迷彩：作者为柔性显示举的用途例子（P018）。",
    "桌面电脑/随身设备、鼠标与触摸板：作者用于说明柔性显示并非为此而生的对照物（P013、P018）。"
   ],
   "conditions": [
    "时间范围条件：所谈“最前沿”不是十年、二十年，而是极限与终极方向；“未来十年左右”是另一处预测的时间尺度（P002、P015）。",
    "限制条件：柔性屏上限由“手输入”决定，以双手合握拇指可及范围为上限（P013）。",
    "语气限定：“不太能是‘便携大屏’”“大概应该在建筑方面和工程方面”为作者留有余地的判断（P013、P018）。",
    "前提条件：作者对终极形态的推论建立在“视觉即概念性结论、可不依赖眼睛输入”这一前提上（P004、P006）。",
    "未说明：脑机接口直连视觉中枢在何时、以何种技术路径实现，文中未给出。"
   ],
   "rhetoric_and_tone": "科普式讲理加比喻：以“锦衣卫路线/密折路线”“皇帝与奏折”作比，用梦境作证，语气自信、断言多；对提问的折叠屏话题不作正面褒贬，而是重新划界并给柔性显示另指去处。",
   "unresolved_questions": [
    "“视觉是大脑处理后的概念性结论”这一前提在文中未给出神经科学依据，需外部核查。",
    "“未来十年左右MR眼镜成为主流”是预测，文中未给出依据或数据。",
    "脑机接口直接接入视觉结论处理中枢的时间表与技术可行性，本文未说明。",
    "文中未讨论折叠屏本身的技术极限（提问所问），只将其归入中间形态。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "不是指十年、二十年，而是指视觉输入技术的极限、终极方向", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "人类真正的视觉，是大脑对图像进行自动化处理之后所得到的丰富的概念性结论。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "如果摘除你的眼睛，直接以巧妙的方式诱使你的大脑获得一系列的同样结论，你将会感受到同样的画面。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "你的梦境就是明证。在梦境里，你有完整的视觉，但你的眼睛此时没有任何输入信号。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "通过脑机接口直接接入你的视觉结论处理中枢的后端", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "这种视觉输入，完全不依赖光学部门，实际上根本无需光学显示器件。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "目前的视觉输入技术，终究仍然是在走“锦衣卫路线”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "其他的分支发展最终都只能作为配角", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "而这中间状态里，决定步调和转折的，不是显示的形态，而是输入形态。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "决定着移动设备显示形态的，不是眼睛，而是手。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "“手输入”决定了“柔性屏”最多只能是“灵活硬屏”", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "未来十年左右，MR眼镜会替代手持或桌面显示屏成为显示技术的真正主流。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "保留外部大屏将会变得毫无必要且不经济。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "尺寸极小、刷新率极高、分辨率极高、同时功耗极低的电子光学器件", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "对于这个核心组件，“柔性”是全然多余的、没有任何意义的特性。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "它的归宿大概应该在建筑方面和工程方面。", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P018", "quote": "它可以用作军事装备的视觉迷彩，其效能将远远的超过现有的迷彩涂装。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["显示与人机交互技术", "脑机接口", "视觉科学（通俗论述）", "技术趋势预测"],
   "issue_candidates": ["折叠屏的极限", "视觉输入技术的终极方向", "手输入对移动设备形态的限制", "柔性屏的适用场景", "MR眼镜替代外部屏幕"],
   "text_function_candidates": ["答问", "解释", "趋势预测", "概念辨析"],
   "object_candidates": ["折叠屏", "MR眼镜", "脑机接口", "柔性屏", "光学显示器件", "锦衣卫/密折（比喻）"],
   "working_keywords": ["视觉输入", "密折路线", "锦衣卫路线", "灵活硬屏", "便携大屏", "脑机接口", "视觉迷彩"]
  },
  "notes": "无图片、正文非空。P006 段落原文约 341 字，超过生成器单段转录上限 300 字（记录中该段 sample_truncated=true），但所引短引均位于前 300 字内，可核验。提问所问“折叠屏的极致”未被正面回答，作者改为讨论视觉输入技术的终极方向，已在 unresolved_questions 记录。"
 },
 "66905294": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么动物几乎一致地进化成拉的屎是臭的？提问把“臭”说成排泄物被进化出来的属性。作者的答复实际上把问题翻转到感知者一侧：从热力学与演化角度论证，负面评价来自摄取者演化出的回避本能与文化反映，而不是排泄物本身被“进化成臭的”。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "从热力学界定营养：营养是蕴藏在大分子中的负熵，摄入大分子、排出小分子获得净熵下降以维持生命；故小分子（除水、氧气等）往往有害，物质堆积只扩大规模且未必良性。",
     "role": "definition"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P004"],
     "summary": "特别指出高活性小分子（尤其无机小分子）是严重潜在危害，加之高渗透性、耐受剂量低，因此成为首先需要养成回避本能的对象。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P005"],
     "summary": "在文化传承之前，判断大分子是否可吃只能靠五感：听觉无用、触觉视觉不可靠、味觉太晚，只有嗅觉是最大依靠，并以自然分解出的小分子碎片为线索；举肉香精为例。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P006"],
     "summary": "由上述机制推出：负熵已被消解完毕的物质，其降解小分子会因暗示缺乏摄取价值而带来负面印象。",
     "role": "conclusion"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P007", "P008"],
     "summary": "感知系统对高活性小分子高度特化敏感、决策系统强烈本能回避，这是成为人类之前就获得的性状；文化对排泄物的贬斥是被它决定的文化反映；其他动物因生命本质相同而有相同厌恶倾向。",
     "role": "claim"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P009", "P010"],
     "summary": "普遍厌恶使排泄物成为跨物种文化符号；地球生物排泄物普遍含H3N、H2S等回避信号，短链酚、醛、卤族气体等也被评为有刺激性气味。",
     "role": "example"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": ["P011"],
     "summary": "一句收束：演化出来的是“差评能力”。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张从热力学看，营养归根到底是蕴含在大分子中的负熵；摄入大分子、排出小分子获得系统净熵值下降，从而强化和维持系统的有序性，也就是生命。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为物质的堆积只对扩大系统规模有贡献，甚至未必良性，有时意味着肥胖和代谢负担。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者主张总体上摄入小分子——除非用作溶剂（水）或分解反应工质（如氧气）——往往有百害而无一益；其中高活性小分子尤其要害，其他高氧化性或还原性小分子（尤其无机小分子）是严重潜在危害，高渗透性使其更甚，因此是人类首先养成回避本能的事物。",
     "evidence": ["E3", "E4", "E5"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张在拥有文化传承之前，判断哪些大分子值得摄取依靠的是本能五感；听觉用不上，触觉、视觉不可靠，味觉为时已晚，只有嗅觉是最大依靠，其办法是以大分子的自然分解物（小分子“碎片”）为线索，并以肉香精闻着香、摆在面前却没有胃口为例。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者推出：既然负熵丰富物质的分解小分子给人正面印象，那么负熵已被消解完毕所剩余物质的降解小分子，因暗示缺乏摄取价值，一定会让人形成负面印象。",
     "evidence": ["E8"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张感知系统对“高活性小分子”演化出高度特化、高度敏感化的探测能力，决策系统演化出强烈的本能回避倾向，这是尚未成为人类时就获得的性状；人类文化中对排泄物的种种贬斥只是这一演化结果的文化反映，是被前者决定的。",
     "evidence": ["E9", "E10"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为其他动物与人类有相同的生命本质，往往也就有相同的对排泄物的厌恶倾向；也正因这种普遍厌恶，排泄物成了一种跨物种的文化符号。",
     "evidence": ["E11", "E12"]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者附带判断：只有“低贱者”会认为另一个种族的排泄物对自己仍有足够营养，并把这种看法称为蛋白链更短、酶结构更简单、更为原始和简陋的表征。",
     "evidence": ["E13"]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出地球生物排泄物中普遍含有H3N、H2S，这两者已构成普遍的回避信号；短链酚、醛、卤族气体分子等也基本一致被评为“有刺激性气味”或“强烈异味”。",
     "evidence": ["E14", "E15"]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以一句总结收束：演化出来的是“差评能力”。",
     "evidence": ["E16"]
    }
   ],
   "argument_steps": [
    "从热力学重新定义营养为负熵，并把摄入大分子、排出小分子与维持有序性联系起来（P001）。",
    "指出物质堆积只扩大规模且未必良性，为“小分子多数无益”作铺垫（P002）。",
    "以汽车作类比：汽油是营养物，润滑油与冷却水只是辅助工作物质，推出摄入小分子（除水、氧气）往往有百害而无一益（P003）。",
    "收窄到高活性小分子：具潜在危害、渗透性高、耐受剂量低，故成为回避本能的对象（P004）。",
    "提出摄取决策的感官条件：文化之前只能靠五感，逐一排除听觉、触觉、视觉、味觉，认定嗅觉最关键（P005）。",
    "说明嗅觉的判据是分解出的小分子碎片，并用肉香精的例子区分“线索”与“摄取物”（P005）。",
    "反向推论：负熵耗尽后的降解小分子提示无价值，故形成负面印象（P006）。",
    "给出演化解释：探测能力与回避倾向是演化性状，文化贬斥是被决定的文化反映（P007）。",
    "推广到其他动物，并指出排泄物因此成为跨物种文化符号（P008-P009）。",
    "举出具体化学信号H3N、H2S与短链酚、醛、卤族气体等，收束为“差评能力才是演化出来的”（P010-P011）。"
   ],
   "concept_usage": [
    {"term": "负熵", "meaning": "文中指蕴含在大分子中的、可被系统摄取利用以维持有序性的东西；营养的本质即负熵。", "evidence": "P001", "ambiguity": "作者以“归根到底”作限定，未给出定量定义"},
    {"term": "高活性小分子", "meaning": "文中指除O2和水以外、具有高氧化性或还原性、渗透性强的小分子（尤其无机小分子），是回避本能的靶标。", "evidence": "P004", "ambiguity": "未列出完整清单，P010 举出H3N、H2S、短链酚、醛、卤族气体"},
    {"term": "差评能力", "meaning": "作者用来指被演化出来的、对无价值或有害物质给出负面评价的感知—决策机制（而非排泄物本身被进化成“臭”）。", "evidence": "P011", "ambiguity": "是作者自造的说法，未与既有术语对应"},
    {"term": "臭", "meaning": "按作者论述，“臭”是摄取者一侧的负面评价（回避信号），不是排泄物被进化出来的属性。", "evidence": "P006", "ambiguity": "文中未讨论“臭”的主观感受机制细节"}
   ],
   "examples_and_targets": [
    "汽车与汽油、润滑油、冷却水：作者的类比，用来说明营养物与辅助工作物质的区分（P003）。",
    "肉香精：作者的例子，说明气味只是搜寻大分子的线索，闻香不等于有胃口（P005）。",
    "H3N、H2S、短链酚、醛、卤族气体分子：作者列举的化学证据性例子（P010）。",
    "“低贱者”与他族排泄物：作者带价值评判的说法与其文化符号论据（P009）。",
    "提问者“动物几乎一致地进化成拉的屎是臭的”这一说法：作者未接受其表述方式，把它改写为摄取者的差评能力（Q001、P011）。"
   ],
   "conditions": [
    "限定条件：小分子有害的判断有例外——用作溶剂（水）或分解反应工质（如氧气）时除外（P003）。",
    "范围限定：“在我们的文化传承之前”“在我们还未成其为人类时”界定了五感与演化性状论述的时间范围（P005、P007）。",
    "程度限定：“往往”“基本上”“几乎”等词表明作者的判断为一般化陈述（P003、P008、P010）。",
    "前提条件：全文论证依赖“营养=负熵”与“演化塑造回避本能”两条前提（P001、P007）。",
    "未说明：作者未给出“负面印象/臭”的神经或心理机制细节，也未讨论例外物种。"
   ],
   "rhetoric_and_tone": "科普式推演，语气笃定、层层递进，多用类比（汽车与汽油）与举例（肉香精）；P009 一处用“低贱者”作贬称并带文明优越色彩的价值判断，属作者修辞而非论证步骤；结尾以短句““差评能力”才是演化出来的。”作警句式收束。",
   "unresolved_questions": [
    "“营养=负熵”与“排泄物小分子必然带来负面印象”是作者的推演，文中未给出实验或文献依据，需外部核查。",
    "P009 关于“低贱者”与他族排泄物的说法带价值评判，属作者看法而非可核验事实。",
    "文中未讨论“为什么是嗅觉而非其他感官承担该功能”的替代解释，也未处理反例物种。",
    "正文末尾“科学答集”为平台话题标签混入正文（lexical 未覆盖片段），不属作者论述内容，已在此登记。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我们摄入大分子、排出小分子，获得系统净熵值的下降，强化和维持了系统的有序性——也就是生命。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "物质的堆积仅仅只对扩大系统的规模有贡献，那甚至未必是良性的——有时那意味着肥胖和代谢负担。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "摄入小分子——除非用作溶剂（水）或分解反应的工质（譬如氧气）——往往有百害而无一益。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "这就犹如对于汽车来说，汽油才算是营养物质，而润滑油和冷却水只是辅助工作物质。", "relation": "context"},
    {"key": "E5", "paragraph_id": "P004", "quote": "其他的高氧化性或还原性的小分子（尤其是无机小分子）对我们的系统都是严重的潜在危害。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "只有嗅觉是最大的依靠。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "我们完全可以提纯出一种肉香精，饱含肉香，一闻就流口水。但是把这香精放一瓶在你面前，你却没有任何胃口。", "relation": "context"},
    {"key": "E8", "paragraph_id": "P006", "quote": "负熵已经完全被消解完毕所剩余的物质的降解小分子因为暗示着此物欠缺摄取的价值一定会让我们形成负面印象。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "我们的感知系统对“高活性小分子”演化出了高度特化、高度敏感化的探测能力，而我们的决策系统演化出了强烈的、本能的回避倾向。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "人类文化中对排泄物的种种贬斥只是这种演化结果的文化反映，是被前者决定的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "其他动物与我们有相同的生命本质，它们往往也就有相同的对排泄物的厌恶倾向。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P009", "quote": "使得排泄物成了一种跨物种的文化符号", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P009", "quote": "只有“低贱者”会认为另一个种族的排泄物对于自己仍有足够的营养。", "relation": "context"},
    {"key": "E14", "paragraph_id": "P010", "quote": "地球生物的排泄物中普遍的含有H3N、H2S，这两种物质已经构成了普遍的回避信号。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P010", "quote": "基本全体一致的被认定“有刺激性气味”或者“强烈异味”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P011", "quote": "“差评能力”才是演化出来的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["演化生物学", "感官生理学（通俗论述）", "热力学类比", "文化符号"],
   "issue_candidates": ["排泄物气味为何令人厌恶", "营养与负熵", "小分子的回避本能", "嗅觉在取食判断中的作用", "文化贬斥与演化性状的关系"],
   "text_function_candidates": ["答问", "解释", "推演", "科普"],
   "object_candidates": ["动物（含人类）", "排泄物", "O2与水", "H3N、H2S", "短链酚、醛、卤族气体分子", "肉香精"],
   "working_keywords": ["负熵", "大分子/小分子", "高活性小分子", "回避本能", "嗅觉", "差评能力", "跨物种文化符号"]
  },
  "notes": "无图片、正文非空。正文末尾 P012“科学答集”为平台话题标签混入正文（structure.divergence=text_tail_not_in_lexical），不属作者论述，未纳入分析单元。提问中“屎是臭的”这一表述属提问者；作者将其改写为感知者一侧的“差评能力”，已在 question_context 说明。文中含价值评判句（“低贱者”），已标注为作者修辞并列入未决问题。"
 },
 "7191d0c0": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么中国允许公开买卖复合弓和反曲弓却禁止复合弩和反曲弩？作者从弓与弩的力学、瞄准难度、杀伤效果和管制先例四方面给出解释，末尾对滑轮复合弓另作保留。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001", "P002"],
     "summary": "核心区分：没有延迟发射的扳机结构时，弓只是人体能量转换器，威力可用标枪实现且更易掌握，用于杀伤效率低。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P003"],
     "summary": "加上延迟发射扳机后性质改变：可用腿蹬、绞盘棘轮杠杆等机械累加腰背腿与体重，动能可能数倍于一拳，接近小口径手枪出口动能。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P004"],
     "summary": "扳机大幅降低射击难度：弓手满弓状态下瞄准困难，带延迟击发的弩瞄准轻松，刺杀时更容易掌握时机。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P005"],
     "summary": "杀伤效果论：国内已禁猎箭头（带宽刃箭头属管制刃具），靶箭头穿透力好但伤口小、出血少、严重情况多为缓症，对杀手是糟糕选择，因此禁掉猎箭头即可，如同只禁带刃矛头而不禁长棍。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": ["P006", "P007"],
     "summary": "补充两点：能用弓有把握杀人的高手难以隐形、容易被抓，其余则为自信过度的玩火者；且作者所知现代国家尚无管制弓的先例，弓在各国合法。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": ["P008"],
     "summary": "结尾保留：作者对滑轮复合弓持保留意见。",
     "role": "qualification"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张：没有延迟发射的扳机结构，弓只是一种单纯的人体能量转换器，同样威力完全可以用标枪实现，而且弓更难掌握；因此用弓杀人伤人的效率远不如木棍、石块、菜刀或标枪，一箭的威力本质上只是一拳能量换了形式。",
     "evidence": ["E1", "E2", "E3"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为带上延迟发射扳机机构就是另一个故事：弩可以用腿蹬开，加绞盘、棘轮、杠杆还能提升蓄能，可动用整个腰背腿肌肉群与体重并机械多次累加，可能数倍于一拳能量、已接近小口径手枪的出口动能，杀伤力不可同日而语。",
     "evidence": ["E4", "E5"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张扳机大大降低了射击难度：弓手瞄准时两臂之间绷着满弓的最大张力、瞄准难度非常大，而带延迟击发的弩瞄准轻松愉快，这意味着弩用于刺杀远比弓容易掌握时机。",
     "evidence": ["E6", "E7"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出国内禁止使用猎箭头（带宽刃的箭头被视为管制刃具），而靶箭头穿透力虽好却杀伤力很小：伤口直径约七毫米，拔出后肌肉回弹几乎看不出、出血面很小；严重杀伤一般指气胸或肺积液、胃肠穿孔感染，很少造成血管破裂大出血，且前者都是缓症，对杀手是糟糕选择；所以禁掉猎箭头就可以了，如同只禁带刃矛头而不禁长棍。",
     "evidence": ["E8", "E9", "E10"]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为能练到用弓箭有把握杀人的高手基本不太可能那么隐形，要抓转眼就抓到；剩下的可能只是水平不高却自信爆棚、要用这个办法玩火的人，这种智商也难逃法网。",
     "evidence": ["E11"]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称就其所知，现代国家还没有管制弓的先例，弓在世界各国都是合法的，出这个头恐怕有点不太光彩。",
     "evidence": ["E12"]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者在结尾声明自己对滑轮复合弓持保留意见。",
     "evidence": ["E13"]
    }
   ],
   "argument_steps": [
    "先立区分标准：有无延迟发射的扳机结构，决定了弓与弩的本质差别（P001）。",
    "论证无扳机时弓的威力上限：只是人体能量转换，可用标枪替代，且更难掌握，故杀伤效率低（P001-P002）。",
    "论证有扳机后能量可被机械放大：腿蹬、绞盘、棘轮、杠杆，动用更大肌群与体重，接近小口径手枪动能（P003）。",
    "补充第二点：扳机降低瞄准难度，使弩在刺杀中更容易掌握时机（P004）。",
    "补充第三点：管制刃具（猎箭头）已足以压制弓的杀伤效果，靶箭头伤口小、致死多为缓症，对杀手不利（P005）。",
    "补充第四点：能用弓杀人的高手不易隐形；其余为自信过度的玩火者（P006）。",
    "补充第五点：现代国家无管制弓先例，各国合法（P007）。",
    "以对滑轮复合弓的保留意见收尾（P008）。"
   ],
   "concept_usage": [
    {"term": "延迟发射的板机结构", "meaning": "文中指能先把能量蓄积、再延迟击发的机构，是作者区分弓与弩的关键；它使能量可由机械累加并降低瞄准难度。", "evidence": "P001", "ambiguity": "原文写作“板机”（应为扳机），本文按原文引用，未改写"},
    {"term": "人体能量转换器", "meaning": "作者用来界定无扳机时的弓：威力不超出人体本身能输出的能量。", "evidence": "P001", "ambiguity": "作者承认弓的威力“即使略大，也不会大出几倍来”，未给数值"},
    {"term": "猎箭头/靶箭头", "meaning": "文中指带宽刃的箭头（属管制刃具）与靶用箭头；后者穿透力好而杀伤力小。", "evidence": "P005", "ambiguity": "作者所述伤情数据未注明来源"},
    {"term": "滑轮复合弓", "meaning": "作者唯一持保留意见的对象，文中未展开理由。", "evidence": "P008", "ambiguity": "保留意见的具体内容本文未说明"}
   ],
   "examples_and_targets": [
    "标枪、木棍、石块、菜刀：作者的比较对象，用来说明无扳机时弓的效率并不突出（P002）。",
    "弩用腿蹬开、绞盘、棘轮、杠杆：作者举的机械蓄能例子（P003）。",
    "小口径手枪的出口动能：作者用于比较弩的威力（P003）。",
    "七毫米左右的伤口、气胸/肺积液、胃肠穿孔：作者给出的伤情叙述，未注明来源（P005）。",
    "夺命书生：作者插入的调侃式引用（P005）。",
    "滑轮复合弓：作者结尾的保留意见对象（P008）。"
   ],
   "conditions": [
    "前提条件：全部论证以“弓是否有延迟发射扳机结构”为分界（P001、P003）。",
    "限定条件：“就我所知”限定现代国家无管制弓先例这一说法（P007）。",
    "条件句：只有能练到有把握用弓杀人的高手才有威胁，而作者判断这类人不易隐形（P006）。",
    "未说明：作者对滑轮复合弓持保留意见的具体理由、以及复合弓是否应受管制，本文未说明。",
    "未说明：文中伤情与威力数据均无来源标注，需外部核查。"
   ],
   "rhetoric_and_tone": "口语化说理，用“这话翻译成大白话就是”“就是另一个故事了”等转述句拉近距离；穿插调侃（夺命书生）与判断句（“这种智商意味着他也难逃法网”）；结尾以短句保留意见收束，语气果断但不展开。",
   "unresolved_questions": [
    "文中“接近小口径手枪的出口动能”“直径七毫米左右”等数据未给来源，需外部核查。",
    "作者对滑轮复合弓的保留意见未说明理由（是否因省力特性接近弩）。",
    "提问所问的“中国为何允许弓而禁弩”只从力学与管制效果解释，未涉及中国具体法规条文，需外部核查。",
    "原文用字为“板机”（扳机），疑为作者笔误或口语写法，本记录按原文引用未作改写。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "没有延迟发射的板机结构，弓只不过是一种单纯的人体能量转换器，同样的威力完全可以用标枪实现。而且相对于标枪，弓还更加难以掌握。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你要杀人伤人，用弓的效率远不如用木棍、石块、菜刀或者标枪。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "一箭的威力，本质上只是你打出一拳所释放的能量换了一个形式", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "带上延迟发射板机机构就是另一个故事了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "那就不是一拳的能量了，而是可能数倍于此，已经接近小口径手枪的出口动能了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "第二，板机大大的降低了射击难度。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P004", "quote": "这意味着后者用于刺杀要远比前者容易掌握时机。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P005", "quote": "国内是禁止使用猎箭头的——带宽刃的箭头被视为管制刃具。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P005", "quote": "将靶箭头拔出，留下的伤口近乎看不见", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P005", "quote": "所以禁止掉猎箭头就可以了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P006", "quote": "能练到用弓箭有把握的杀人的高手，基本不太可能那么隐形，要抓转眼就抓到了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P007", "quote": "就我所知，现代国家还没有管制弓的先例，在世界各国都是合法的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P008", "quote": "但我对滑轮复合弓持保留意见。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["冷兵器知识", "器械管制政策", "力学与杀伤机理"],
   "issue_candidates": ["弓与弩的管制差异", "延迟发射扳机的作用", "猎箭头与靶箭头的杀伤力", "弓箭杀人的可行性"],
   "text_function_candidates": ["答问", "解释", "辨析", "评论"],
   "object_candidates": ["复合弓", "反曲弓", "复合弩", "反曲弩", "猎箭头", "靶箭头", "滑轮复合弓", "小口径手枪"],
   "working_keywords": ["延迟发射板机结构", "人体能量转换器", "管制刃具", "绞盘/棘轮/杠杆", "出口动能"]
  },
  "notes": "无图片、正文非空。作者原文写作“板机”（通常作“扳机”），本记录短引与概念表均按原文用字，未作改写。所引伤情与动能数据均为作者叙述，无来源标注，已列入未决问题。"
 },
 "df82a10c": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么劳动法颁布那么多年，一些企业、单位一直都无视劳动法？作者的答复不解释执法问题，而是给出一个经济学式判断：劳动者利益只能靠劳动力稀缺来保证，靠立法提高劳动保障反而会削弱劳动者的议价能力，最终任何法规都没用。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": ["P001"],
     "summary": "核心主张：保证劳动者利益要靠劳动力稀缺，不能靠立法提高劳动保障。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": ["P002"],
     "summary": "给出因果链：越立法，雇主市场越萎缩，劳动力越相对过剩，议价能力越低。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": ["P003"],
     "summary": "推到个人处境：低到一定程度，必须“自愿”加班才可能有工作。",
     "role": "conclusion"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": ["P004"],
     "summary": "结论句：到时候任何法规都没用。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张保证劳动者的利益要靠劳动力稀缺，不能靠立法提高劳动保障。",
     "evidence": ["E1"]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者提出连锁判断：越立法，雇主市场越萎缩，劳动力越相对过剩，议价能力越低。",
     "evidence": ["E2"]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预测议价能力低到一定程度时，劳动者必须“自愿”加班才有可能有工作。",
     "evidence": ["E3"]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者判定到那种处境时任何法规都没用。",
     "evidence": ["E4"]
    }
   ],
   "argument_steps": [
    "先给出规范判断：劳动者利益靠劳动力稀缺而非立法（P001）。",
    "给出机制：立法使雇主市场萎缩，劳动力相对过剩，议价能力下降（P002）。",
    "推到极端情形：低到一定程度只能“自愿”加班才有工作（P003）。",
    "收束：到时任何法规都没用（P004）。"
   ],
   "concept_usage": [
    {"term": "劳动力稀缺", "meaning": "文中指劳动者相对需求方而言供不应求的状态，是作者认为唯一能保证劳动者利益的条件。", "evidence": "P001", "ambiguity": "如何达成稀缺、以何种政策实现，本文未说明"},
    {"term": "雇主市场", "meaning": "文中指有利于雇主一方的劳动力市场状态，作者称立法会使其萎缩。", "evidence": "P002", "ambiguity": "术语未定义，也未说明立法通过何种路径导致其萎缩"},
    {"term": "“自愿”加班", "meaning": "作者加引号的自愿，指形式自愿而实质被迫的加班。", "evidence": "P003", "ambiguity": "引号表明作者对其“自愿”性质持否定态度，但未展开"}
   ],
   "examples_and_targets": [
    "劳动法与企业无视劳动法的现象：提问者提出的事实前提，作者未讨论其执法层面，只谈立法与劳动力供求（Q001）。",
    "本文无具体案例、人物、机构或数据。"
   ],
   "conditions": [
    "条件推进：判断以“越立法……越……越……”的连续变化为前提（P002）。",
    "临界条件：只有议价能力“低到一定程度”，才出现必须“自愿”加班才可能有工作的情形（P003）。",
    "未说明：本文未说明立法通过什么具体机制导致雇主市场萎缩，也未给出任何经验证据或数据。"
   ],
   "rhetoric_and_tone": "极简断言体，四句话构成一条递进链，无举例、无让步、无出处；用引号标示“自愿”以表达反讽。",
   "unresolved_questions": [
    "本文仅 94 字，未说明“雇主市场越萎缩”的机制与经验依据，属未展开的断言，需外部核查。",
    "作者未回应提问中“企业为何无视劳动法”的执法与守法问题。",
    "“劳动力稀缺”如何实现、与劳动保障立法是否可能并存，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "保证劳动者的利益要靠劳动力稀缺，不能靠立法提高劳动保障。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "越立法，雇主市场越萎缩，劳动力越相对过剩，议价能力越低。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "低到一定程度，你必须“自愿”加班才有可能有工作。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "到时候任何法规都没用。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["劳动经济（通俗论述）", "劳动力市场", "劳动法政策"],
   "issue_candidates": ["劳动法为何被无视", "劳动保障立法与劳动力供求", "议价能力与自愿加班"],
   "text_function_candidates": ["答问", "评论", "断言式短评"],
   "object_candidates": ["劳动者", "雇主", "劳动法", "劳动力市场"],
   "working_keywords": ["劳动力稀缺", "雇主市场", "相对过剩", "议价能力", "自愿加班"]
  },
  "notes": "无图片、正文非空；全文仅 94 字，四段构成一条递进断言，无案例、数据与出处。提问者所述“企业无视劳动法”的前提属提问者，作者未讨论执法层面，只讨论立法与劳动力供求，已在此分开登记。"
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
