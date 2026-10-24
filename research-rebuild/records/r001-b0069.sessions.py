# -*- coding: utf-8 -*-
"""批次 r001-b0069 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0069.sessions.py            # 写 out/r001-b0069.out.jsonl
  python3 records/r001-b0069.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0069"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0069.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "26b2f5a9": {
  "analysis": {
   "question_context": "提问者引任正非“年轻人要踏实做好本职工作，不要天天高谈阔论”之说，问作者是否赞同、当代年轻人工作观如何（Q001 为提问者字段，非正文段落，无对应 Pnnn 证据）。作者未直接讨论任正非其人其说，只以“都是大实话”作引子，转入“服从”与“屈服”的辨析，并反驳知乎上“员工不必服从”的主张，末段给出组织内自保的操作办法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "开篇承认此类说法是大实话，但指出说服结构：不信者说服不了，信者不需说服。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "服从需要学习，一般人只学过屈服；以“以服从为耻”与军人反问立论，称未学明白服从者无资格下令，并引“既不能令，又不受命，是绝物也”。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011"], "summary": "界定屈服：心不愿而畏后果地忍受，掩饰不愿甚至加倍亲热，日久麻木自解。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "主张屈服源于软弱、服从是主动选择；以搭船当水手与志愿参军说明服从他人实为执行自己的决定，属勇气。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025"], "summary": "摆出反对者的自我定位（引号内为被转述的他人话语）：自认被父母、生活、社会强征的壮丁，从未有过选择，并讥“奋斗逼”；作者先承认若确属壮丁则其逻辑成立。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P026", "P027"], "summary": "让步：该观点可自洽；但自洽只是意识形态的准生证，不是优胜奖，也不使事实随之改变。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032", "P033"], "summary": "给出“事实”的检验：须能贯彻“员工不应服从”又取得系统、长期胜过对手的生产力，否则自洽理论无实际意义。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039", "P040"], "summary": "连串反问：“不服从派”的管理学著作、成功企业、就业份额何在；并质疑若自己当老板也先开除不服从者即为自欺。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050"], "summary": "检视“因侵犯合法权利而不服从”：侵权指令属命令无效问题；以银行柜员、公司命人杀人两例说明定性落在违法者与违约者。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P051", "P052", "P053", "P054", "P055", "P056"], "summary": "提出判据：须有自愿签订的契约被打破才可能产生“不服从”定性；领导权力只是授权的交集，越权指令不构成“未被服从”，并以抢劫犯类比。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061"], "summary": "判断现象背后是回避成长学习的焦虑；组织间竞争存在则“人必须履行契约责任”不可废除；姓资姓社的组织在服从指令上无差别。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069"], "summary": "除“无合法授权”外无抗命权；警告把不服从合理化会掏空自己签署授权的效力，点赞者与自己无契约、真合作时评价更苛。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081"], "summary": "落到操作：如何确定“超出授权范围”——索取书面命令、自写“理解意图笔记”请对方核实，并依对方反应判断是否早跳船。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P082", "P083", "P084", "P085"], "summary": "以橡皮图章、君权与相权、菜鸟连长管老兵连队说明可不动用抗命而实际制约上级。", "role": "example"},
    {"unit_id": "U015", "paragraph_refs": ["P086", "P087", "P088", "P089"], "summary": "明确建议走第一条路（早跳船）而非斗争手腕路线，主张苦修专业换取再选择主动权；文末自注未完待续。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任正非式说法是大实话，但说服不了不信的人，信的人又不用说服。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "服从是要学的，一般人只学过屈服没有学过服从，且不少人以服从为耻。", "evidence": ["E3", "E33"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问质疑“军人以服从为天职即等于军人是失败者”的推论。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有深刻学明白服从是什么、如何做到的人，没有资格下令。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "屈服源于软弱，服从是主动的选择；看似服从他人实为执行自己下的命令。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "自愿把自己置于他人判断之下不是愚蠢或怯懦，而是勇气。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳一方自述：自己是被合谋逼迫、硬抓来的壮丁，从来没有过选择，并认为“奋斗逼”蠢。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "该观点可以自洽，但自洽只是意识形态的准生证而非优胜奖，不意味着事实会随之转变。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "“不服从”主张要成为事实，须能既贯彻该法则又取得系统、长期强于对立流派的生产力。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问要求“不服从派”拿出有效管理学著作、成功企业与就业份额，否则妙辩无意义。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若自己当老板也先开除不服从者，则其主张“员工可以不服从”是自欺。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "侵犯个人合法权利的指令属命令无效问题，不属于“服从”范围的讨论。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有在自愿签订（或自然继承未声明解除）的契约被打破时，才可能产生“不服从”的定性。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "领导可行使的权力以你给予企业的授权为边界，越权指令不能被定性为“未被服从”，如同抢劫犯不能称店主欺诈。", "evidence": ["E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要人类组织间还存在竞争，为迁就需求而消灭“人必须履行契约责任”这一底层原则根本不可能。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "姓社的组织（coc、解放军、央企）在必须服从领导指令上不比姓资组织放松。", "evidence": ["E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "除依赖“对方没有命令你的合法授权”外，没有其他合法的抗命依据。", "evidence": ["E23"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这类为不服从背书的言论只要有第二人听到，就可能使你在组织中失去一切前途。", "evidence": ["E24"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "点赞者与你之间没有契约，真与你合作时会弃你如敝履。", "evidence": ["E25", "E26"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "操作建议：以“沟通笔记，请您核实”方式自写理解意图笔记，请求对方核实以留下书面印记。", "evidence": ["E27"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "认知水准低下的领导常沦为精明下属的橡皮图章，背锅在其而决策在下属；老手可不动抗命而制约上级。", "evidence": ["E28", "E29"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议选择早跳船而非钻研斗争手腕，并主张苦修专业以获得再选择的主动权。", "evidence": ["E30", "E31"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "主张“不服从”的背后是缺少组织生存知识技能、想靠取消组织基本原则来免除成长学习焦虑的心态。", "evidence": ["E34"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "让步性限定：若当事人确属“被抓的壮丁”，则其不服从的逻辑的确成立。", "evidence": ["E36"]},
    {"claim_id": "C025", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者引任正非“年轻人要踏实做好本职工作，不要天天高谈阔论”并询问作者是否赞同（Q001 属提问者，无正文段落可引）。", "evidence": []}
   ],
   "argument_steps": [
    "以承认提问所引说法是大实话开头（P001-P003），随即提出服从与屈服的区分（P004）。",
    "先定义屈服（P009-P011），再定义服从为主动选择，用搭船水手与志愿参军作例证（P012-P016）。",
    "引出反对者的壮丁自述（P017-P025），先承认其可自洽（P026），再用“自洽非优胜奖”转折（P027）。",
    "提出以生产力与组织竞争结果检验主张（P028-P033），连续反问对方证据（P034-P040）。",
    "逐条检视“不服从”的理由，先处理侵权情形（P041-P050），再给出契约破坏的判据（P051-P052）。",
    "由授权边界推出越权指令无效（P053-P054），以抢劫犯类比（P055-P056）。",
    "指出心理动因与组织竞争前提，并称姓资姓社无差别（P057-P061）。",
    "给出唯一合法抗命依据（P062-P063），加警告与对点赞者的判断（P064-P069）。",
    "转入操作层面：书面命令、理解意图笔记与两条路的选择（P070-P081）。",
    "以橡皮图章、君权相权、军队类比支持上述判断（P082-P085）。",
    "结论性建议：走第一条路、苦修专业，末注未完待续（P086-P089）。"
   ],
   "concept_usage": [
    {"term": "服从", "meaning": "本文指主动选择、执行自己下的决定而听从他人，与畏惧后果的忍受相区分", "evidence": "P012", "ambiguity": "作者把它限定在自愿授权（签约）的组织关系内，未讨论非自愿关系下的服从"},
    {"term": "屈服", "meaning": "心不愿而因畏惧后果忍受，甚至掩饰不愿、以亲热自保", "evidence": "P010", "ambiguity": "与日常语用中的“服从”高度重叠，作者靠自愿与否划线"},
    {"term": "壮丁", "meaning": "比喻反对者自认被强征、从无选择的处境定位", "evidence": "P022", "ambiguity": "作者同时承认若真属壮丁则其逻辑成立（P018），故该词兼具被反驳对象与让步条件双重用法"},
    {"term": "授权（自愿签订的契约）", "meaning": "判断是否发生“不服从”的基准；领导权力为你的授权与企业对其授权的交集", "evidence": "P053", "ambiguity": "“自然继承而未被声明解除”的契约如何认定，本文未展开"},
    {"term": "事实", "meaning": "此处指可在组织竞争中验证的生产力结果，而非论辩自洽", "evidence": "P029", "ambiguity": "未给出可操作的度量标准，只举企业竞争为判据"},
    {"term": "姓资姓社", "meaning": "组织的意识形态标签，作者称其在服从领导指令这一法则上无差别", "evidence": "P061", "ambiguity": "“coc”未在文中说明所指"}
   ],
   "examples_and_targets": [
    "任正非的话（提问者转引，作者仅以“都是大实话”带过，未直接评论其人）",
    "知乎上主张“员工不必服从”的论者及其点赞者（P019、P064-P068）：被反驳对象",
    "自认“被抓来的壮丁”、认为“奋斗逼”蠢的自述（P020-P025）：被转述的被反驳观点",
    "搭船者与水手、船长（P013-P014）：作者类比",
    "志愿参军、敢于置于他人判断之下（P016）：作者例证",
    "被抓的壮丁乖乖听命令是傻、怯懦、好糊弄（P017）：作者对反对者逻辑的转述",
    "银行柜员拒绝把储户存款转入主管账户（P044-P047）：作者例证",
    "公司下令干掉碍事的人而员工未照办（P048-P050）：作者例证",
    "抢劫犯叫店主交出货物（P055）：作者类比",
    "坚船利炮与四书五经（P034）、“不服从派”的坚船利炮（P035）：历史类比与反问材料",
    "君权高于相权而皇帝受制于宰相（P083）、菜鸟连长管老兵连队（P084）：历史与军事例证",
    "coc、解放军、央企（P061）：举例",
    "李总与“abcdefg”要点核实的示范话术（P078）：作者拟写的操作样例"
   ],
   "conditions": [
    "作者明说：如果是被抓的壮丁，那么这逻辑的确是通的（P018），即其反驳只针对自愿签约进入组织者。",
    "判断“不服从”以存在自愿签订的契约被打破为前提（P051-P052）。",
    "唯一合法不照办依据是对方没有命令你的合法授权（P062）。",
    "书面命令情形下取证较易；对方若拒绝出具书面命令，则改用理解意图笔记请其核实（P072-P076）。",
    "对看不懂此流程的领导，作者给两条路二选一（早点跳船／当作较好对付的上司），并声明只建议第一条（P081、P086）。",
    "作者称第二条路以“没有选择环境的能力和机会”为适用条件（P088），否则建议苦修专业。",
    "结论以“只要你还依靠分享人类组织的收益和保护来生存”为条件（P060）。"
   ],
   "rhetoric_and_tone": "以第二人称“你”直面读者，训诫与警告口吻明显（我警告你、让我告诉你残酷的真相），夹用反诘句群与网络化讽刺语（奋斗逼、妙辩无碍、鬼话、混账逻辑）；大量比喻推进（搭船水手、抢劫犯、坚船利炮、橡皮图章），并在引号内整段模拟对方口吻再逐条拆解。结构为概念辨析—反驳—操作流程—结论建议，末句自注未完待续。",
   "unresolved_questions": [
    "正文未回应提问者所引任正非说法的具体内容，也未系统回答“当代年轻人的工作观”，仅就反驳对象的自我定位作评论。",
    "“coc”未说明所指全称，需外部核查或上下文补充。",
    "文末标“（未完，待续）”，本篇非完篇，后续部分是否存在于语料未核。",
    "P029“既能能贯彻”按原文照录，疑为原文笔误，未作改写。",
    "对知乎点赞生态的判断（P068）无数据支撑，属作者断言，需外部核查。",
    "“自然继承而未被声明解除”的契约（P051）如何界定，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "都是大实话。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "可惜说服不了不信的人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "服从是要学的，一般人只学过屈服，没有学过服从。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "军人以服从为天职，按这个理解，军人都是失败者吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "没有深刻的学明白服从是什么、如何能做到，也就没有资格下令。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "屈服的根源是出于软弱。服从，是主动的选择。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "你看似服从的是船长，但是你服从的是你自己对自己下的“今天继续搭这条船”的命令。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "敢于将自己置于ta人的判断之下，这不是愚蠢、不是怯懦，而是勇气。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P022", "quote": "我根本没有选择。我是被你们所有人合谋逼迫，像搜山一样逼得没有藏身之处，硬抓来的壮丁。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P024", "quote": "我们全都觉得“奋斗逼”真的蠢。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P027", "quote": "自洽只是一种意识形态的准生证，而不是一种优胜奖。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P029", "quote": "既能能贯彻“员工不应该服从”的法则，又能发挥出比对立流派更强的生产力", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P036", "quote": "行之有效的基于“不服从”法则的管理学著作有哪些？成功企业有哪些？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P038", "quote": "如果你没有实际能力抬升这个数字，妙辩无碍有何意义？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P040", "quote": "那你现在主张“员工可以不服从”，岂不是在自欺吗？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P043", "quote": "这不是“服从”这个范围的问题，这是命令无效的问题。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P046", "quote": "发生了一次“某主管对公司规章的不服从”和一次“某柜员对公司规章的服从”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P051", "quote": "取决于是否存在自愿签订（或自然继承而未被声明解除）的契约被打破的问题", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P054", "quote": "企业根本无法将你没有授予企业的权力转授给ta。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P055", "quote": "这就好像一个抢劫犯叫店主交出货物，店主没有照办，不能被定性为“交易欺诈”一样。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P058", "quote": "想要组织这种事物为了迁就这种需求而消灭掉“人必须履行契约责任”这种底层原则就是根本不可能的。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P061", "quote": "在必须依照组织原则服从领导指令这一点放诸四海而皆准的法则上没有任何比“姓资的组织”放松的地方。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P062", "quote": "你只能依赖“对方没有命令你的合法授权”来不照办。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P064", "quote": "你都不要惊讶有一天你在这个组织里失去一切可能的前途。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P068", "quote": "这些人给你点赞，只是因为ta们和你之间没有契约，不需要指望你履约。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P069", "quote": "ta们将弃你如敝履。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P076", "quote": "以“沟通笔记，请您核实”的方式自己写一个自己的“理解意图笔记”发给对方请求核实", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P082", "quote": "认知水准低下的人坐在领导的位置上，常常沦为精明下属的橡皮图章", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P084", "quote": "对于深谙组织伦理的老手而言，这简直是常事。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P086", "quote": "建议走前一条路，不建议走后一条路。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P088", "quote": "建议你苦修专业，去获得再选择的主动权", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P005", "quote": "有无数人在心里干脆就以“服从”为耻。", "relation": "context"},
    {"key": "E34", "paragraph_id": "P057", "quote": "希望通过反向消灭组织最基本的原则来免除自己成长和学习的必要的焦虑心态。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P018", "quote": "如果是被抓的壮丁，那么这逻辑的确是通的。", "relation": "qualifies"},
    {"key": "E35", "paragraph_id": "P060", "quote": "只要你还要依靠分享人类组织的收益和保护来生存，就永远不要幻想这一条可能有丝毫的动摇。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理与职场伦理", "劳动关系与契约责任", "权威与服从的政治哲学", "军事组织文化"],
   "issue_candidates": ["服从与屈服的区分", "员工是否应当服从管理指令", "授权边界与抗命的法律／操作界限", "代际工作观与“奋斗”评价", "契约责任可否被意识形态理由取消"],
   "text_function_candidates": ["答复提问", "概念辨析", "论辩与反驳", "经验总结", "操作建议"],
   "object_candidates": ["任正非（提问者引用）", "知乎提问者与点赞者", "企业与主管、员工", "解放军", "央企", "coc（未说明）", "船长与水手（比喻）"],
   "working_keywords": ["服从", "屈服", "壮丁", "授权", "自愿签订的契约", "不服从派", "坚船利炮", "理解意图笔记", "橡皮图章"]
  },
  "notes": "无图片节点，纯文本正文（P001-P089）；正文末段 P089 为作者自注“（未完，待续）”，本篇非完篇。提问字段 Q001 属提问者，不构成正文段落，故未生成 evidence_refs。文中 ta／ta 等网络写法按原文照录。"
 },
 "2e4ef5a8": {
  "analysis": {
   "question_context": "提问者引印度外交部长“当务之急是通过外交途径与中国达成和解”之说，问如何看待（Q001 属提问者字段，无对应 Pnnn 证据）。作者以中国立场（文中自称“我们”）推演中印边境对峙的博弈结构：认为印度被自身煽动的民族主义狂热困住，主动权已转到中国一侧，并主张印度当务之急确为与中国和解；末尾转向对中国自身民族主义风险的提醒，并以长平之战为待回顾的参照（正文未展开）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出印度政治家清楚自身处境危险，并定义对狭隘民族主义最致命的 passive aggressive 策略。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009"], "summary": "推演：不给台阶会形成裹挟决策者的动能；中国持续消极刺激或使印度军事冒险并在中国境内被重创、被制裁；并反驳“美国会投反对票”的预期。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "主张主动权已在中国一侧，未公布的伤亡、部署与声明都是未打的牌，每打一张印方压力升级；拖下去对印度是命运转折。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "描述新德里骑虎难下，北京要求其自己圆场付出政治代价，否则继续毫无把柄地刺激印度民意。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029"], "summary": "以太极拳、大象陷阱、绞肉机比喻该策略：诱使对方按自身惯性前扑，西藏是最合适的陷阱。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P030", "P031"], "summary": "质问印方拿什么交换与抵押以换取中方配合稳定局面，并称印度牌面前所未有地差。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "提出民粹治国的前提是国际关系尤其邻国关系良好；把民粹指向远强于己的强邻最愚蠢，故印度当务之急是与中国和解。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042", "P043"], "summary": "回应“有无参考资料”之问：以美国在南海台海的做法作对照，指出中国有警惕意识与抑制集体无理性的经验，但仍不可掉以轻心，并自省式反问。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P044", "P045"], "summary": "以“可以回顾一下”引出长平之战百度百科链接，正文未展开类比内容。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "印度政治家非常清楚自己现在处境非常危险。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对待狭隘民族主义最致命的策略是 passive aggressive，即用中正和平、无可挑刺的话术让对方句句刺耳。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "狭隘民族主义像没有大脑的野兽，外交上不给台阶下会产生裹挟决策者踏入对方屠宰场的动能。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "中国继续消极刺激，印度领导集团可能压不住民族主义狂热而军事冒险，随后作为入侵者在中国境内被重创，还可能被安理会制裁。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者预设的一种看法：美国会为印度投反对票，使制裁无法通过。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "美国不会为印度撑到底：容忍侵略导致国际秩序崩坏的代价超过占中国上风的收益，最多在制裁条款上从轻从短或投弃权票。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "控制事态进展的主动权已不在印度决策层手里，而在中国一方。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国未公布的伤亡、印军惨状、军事部署与更强硬声明都是手里没打的牌，每打一张印度压力升一级。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "印度的困境只能怪自己煽动的狂热，正是它使这些牌具备引燃狂热的效力。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "牌可以不断打出甚至自己印刷；若不自己转弯，北京会毫无把柄地持续刺激印度民意，直到新德里控制不住而伸手挨刀。", "evidence": ["E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "北京的潜台词是要求新德里自己圆场、自损威望付出政治代价，并需拿东西来换与抵押才谈得上配合稳定局面。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该策略如太极拳，利用对方意图与自身控制不了的惯性诱其前扑；西藏是最合适的大象陷阱，刀已备好等其伸手。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "印度牌面前所未有地差；依靠民粹治国的前提是国际关系尤其邻国关系良好。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把民粹指向远强于自己的强邻是世界上最愚蠢的行为之一，对方可借正当防卫打击你。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对印度而言，现在当务之急确实是和中国和解。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国现在在南海和台海对中国做的事，与中国在中印边界的策略高度相似；区别在于中国有警惕狂热民族主义的意识与抑制集体无理性的长期经验。", "evidence": ["E22", "E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "即便如此，中国仍不能对这类引逗策略掉以轻心，仍然有压力。", "evidence": ["E24"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "凡民族主义过于高涨且强自信的国家，最大弱点就是“不受逗”，被引逗容易失控犯下重大错误。", "evidence": ["E25"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以自省式反问质疑中方视角：当乙方时看得一清二楚，当甲方了是否反而看不明白。", "evidence": ["E26"]},
    {"claim_id": "C020", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者引印度外交部长“当务之急是通过外交途径与中国达成和解”一语并问如何看待（Q001 属提问者，无正文段落可引）。", "evidence": []}
   ],
   "argument_steps": [
    "以“印度处境危险”开题，给出 passive aggressive 的定义（P001-P003）。",
    "从民族主义狂热可被裹挟推出军事冒险与被重创、被制裁的预测（P004-P006）。",
    "插入括号反驳“美国会投反对票”的预期，改以国际秩序代价立论（P007-P009）。",
    "断定主动权已易手，逐项列举未打出的牌（P010-P012）。",
    "把责任归回印度自身煽动的狂热，并给出“自己圆场”的出路要求（P013-P022）。",
    "用太极拳、大象陷阱与绞肉机比喻策略机理（P023-P029）。",
    "质问交换与抵押，指出印度牌面之差（P030-P031）。",
    "提出民粹治国的外部前提，得出印度应与华和解的结论（P032-P036）。",
    "自问参考资料，以美国在南海台海的做法对照，指出中国经验与仍存压力（P037-P043）。",
    "以“可以回顾一下”引出长平之战链接作参照，正文未展开（P044-P045）。"
   ],
   "concept_usage": [
    {"term": "passive aggressive", "meaning": "以中正和平、政治正确到无可挑刺的话术，使心里有鬼者句句刺耳扎心", "evidence": "P003", "ambiguity": "同段末拼作 passive agressive，拼写不一致，按原文照录"},
    {"term": "狭隘民族主义", "meaning": "被作者形容为没有大脑、可被外部刺激点燃并裹挟决策者的野兽式动能", "evidence": "P004", "ambiguity": "未界定其与一般民族主义的边界"},
    {"term": "牌", "meaning": "尚未动用的政策手段与谈判筹码（未公布的伤亡、部署、声明等）", "evidence": "P011", "ambiguity": "“自己印刷”一句为比喻，未说明具体所指"},
    {"term": "太极拳", "meaning": "借对方意图与其无法自控的惯性，诱使其按原方向前扑的策略比喻", "evidence": "P023", "ambiguity": "比喻与具体政策手段之间的对应关系未逐项说明"},
    {"term": "大象陷阱", "meaning": "指西藏被作者视为最适合引诱印度伸手的战略陷阱", "evidence": "P025", "ambiguity": "未说明陷阱的具体机制与触发条件"},
    {"term": "民粹治国", "meaning": "依靠国内民族主义情绪维持执政，作者称其需要良好的国际关系为前提", "evidence": "P032", "ambiguity": "未说明该前提在何种程度上是充分或必要条件"},
    {"term": "乙方／甲方", "meaning": "以合同双方借指此前的被逗引一方与如今处于强势地位的一方", "evidence": "P043", "ambiguity": "具体指向对象未点名"}
   ],
   "examples_and_targets": [
    "印度外交部长有关和解的表态（提问者转引，正文未再引用原文）",
    "“很多小朋友觉得美国会投反对票”（P007）：作者预设并反驳的看法",
    "洗衣粉与好牌子（P008）：以美国在安理会的旧争议作讽刺性修辞",
    "卫星全程录像、上万印军俘虏上镜（P007）：作者设想的宣传手段",
    "太极拳、大象陷阱、绞肉机（P023-P028）：作者比喻",
    "组织刺杀小队刺杀“投降主义”官员（P027）：作者对可能局势的推演",
    "美国在南海和台海对中国干的事（P039）：作者类比证据",
    "《三国演义》《廉颇蔺相如列传》（P040）：作者举的历史教训读物",
    "长平之战（P044-P045，百度百科链接节点）：作者提出的待回顾参照，正文未展开"
   ],
   "conditions": [
    "若中国继续消极刺激印度（P005），则印度领导集团可能压不住国内狂热（预测性条件句）。",
    "美国支持的表达最多体现在制裁条款从轻、年限从短与弃权票（P009）。",
    "若新德里不自己把弯转彻底，则中方会继续刺激印度民意（P021）。",
    "若希望中方配合息事宁人，须拿东西来换、来做抵押（P030）。",
    "民粹治国的前提是国际关系尤其邻国关系良好（P032）。",
    "限定：中国仍不能对引逗策略掉以轻心，仍有压力（P041）。",
    "长平之战类比的具体条件与结论未在正文说明（P044-P045）。"
   ],
   "rhetoric_and_tone": "冷峻的战略推演混合讽刺与训诫口吻：以第二人称“你”直接对印方说话（请你自己想办法圆场、看你能不能按得住），用野兽、屠宰场、太极拳、大象陷阱、绞肉机等密集比喻推进；括号内插入“洗衣粉，我们也有很多好牌子”一类调侃；末段转为对中国自身的自省式反问，并以“可以回顾一下”引出未展开的历史参照。",
   "unresolved_questions": [
    "P045 为链接节点（长平之战百度百科），结构标记 lexical 未覆盖尾段（divergence: text_tail_not_in_lexical），链接内容与作者拟作的类比未核、未展开。",
    "P034“实力远远不如的强邻”视角存在歧义：按印度视角应指强于自己的邻国，字面亦可读作相反，需研究者判断。",
    "P003 末拼写 passive agressive 与同文 passive aggressive 不一致，按原文照录。",
    "对美方立场、制裁结果与印方内部动向（刺杀小队等）的推演属作者预测，需外部核查。",
    "文中“我们”指中国的立场线索来自文本内指称，作者身份与发表语境未在其他字段说明。",
    "提问者所引印度外长表态的出处与时间未给出。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "印度政治家非常清楚自己现在处境非常危险。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "对待狭隘民族主义，最致命的策略就是passive aggressive。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "看起来都是中正和平、政治正确到人打哈欠、完全没有办法挑刺的伟光正的话，但是在心里有鬼的人听起来句句刺耳扎心", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "狭隘民族主义是一头没有大脑的野兽", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "可能会真的做出最愚蠢的军事冒险，然后作为无可抵赖的入侵者在中国境内被名正言顺地重大杀伤。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "顺带还可能会被安理会拉上制裁名单。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "很多小朋友觉得美国会投反对票。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "容忍对主权国家发动侵略而不制裁，造成的国际秩序的崩坏对美国现实利益造成的代价远超过占中国一点上风而带来的利益。", "relation": "contradicts"},
    {"key": "E9", "paragraph_id": "P010", "quote": "控制事态进展的主动权已经不在印度决策层手里了，而在中国一方。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "中国没有公布的伤亡人数、没有公布的印军惨状、没有公布的军事部署、按住没发的更强硬的声明，都是留在手里没打的牌。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "正是你自己煽动起来的狂热，造成了这些牌引燃狂热的强大效力。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "如果一张牌不够，还有第二张、第三张。打完了，还可以自己印刷。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "直到新德里自己也控制不住、非把手伸出来挨这一刀为止。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "请你自己想办法圆场。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P030", "quote": "你们打算拿什么来换？打算拿什么来做抵押让我们相信你的诚意？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "太极拳的要害在于利用对方自己的意图和自己控制不了的惯性，顺着ta的意让ta自己向扑去的方向摔倒。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "西藏实在是最合适的大象陷阱。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P031", "quote": "印度的牌面前所未有地差。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P032", "quote": "依靠民粹治国，有一个至关重要的前提，就是国际关系——尤其是邻国关系——一定要良好。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "尤其是愚蠢地指向实力远远不如的强邻，真的是世界上最愚蠢的行为之一。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P036", "quote": "对印度而言，现在的确当务之急是和中国和解。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P039", "quote": "美国现在在南海和台海对中国干的事，和中国在中印边界的策略高度相似。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P040", "quote": "中国有很强的对于狂热民族主义的警惕意识以及长期积累下来的抑制集体无理性的经验", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P041", "quote": "中国仍然不能对这种“在你面前晃悠，就是想勾引你贸贸然出手”的策略掉以轻心，仍然有压力。", "relation": "qualifies"},
    {"key": "E25", "paragraph_id": "P042", "quote": "凡民族主义过于高涨而且有强自信的国家，最大的弱点就是不受逗，被引逗容易失控犯下重大错误。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P043", "quote": "我们当乙方的时候就看得一清二楚，我们自己当甲方了反而看不明白了吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系与外交战略", "军事冲突与威慑", "民族主义与民粹政治", "中印关系"],
   "issue_candidates": ["中印边境对峙与和解条件", "民族主义对外交决策的裹挟", "passive aggressive 外交策略", "西藏方向的战略诱导", "民粹治国的外部前提"],
   "text_function_candidates": ["答复提问", "时评与战略推演", "论辩", "风险预警"],
   "object_candidates": ["印度", "中国", "新德里", "北京", "美国", "安理会", "印度外交部长（提问者引）", "西藏", "《三国演义》", "《廉颇蔺相如列传》", "长平之战"],
   "working_keywords": ["passive aggressive", "狭隘民族主义", "太极拳", "大象陷阱", "牌", "民粹治国", "正当防卫", "制裁", "长平之战"]
  },
  "notes": "无图片节点，纯文本正文（P001-P045）。本篇结构存在 text/lexical 分歧：P045 为链接节点（长平之战百度百科），lexical 尾段未覆盖（divergence: text_tail_not_in_lexical），链接内容未经核验，正文亦未展开该类比。提问字段 Q001 属提问者，不构成正文段落，故未生成 evidence_refs。"
 },
 "3fb73ea2": {
  "analysis": {
   "question_context": "提问者只问“被人讨厌了怎么办？”（Q001 属提问者字段，无对应 Pnnn 证据），未附具体情境或对方身份。作者以“尊重别人讨厌的权利”为总纲，给出 1)—5) 条操作性规则，并把结论推进到关系伦理层面：做最好的被讨厌者、让他人不必恐惧被报复。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出总纲：最重要的是尊重别人讨厌的权利。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "给出 1)—3) 条规则：私域内允许吐槽；不要听中间人传话也要其不要传；遇犯罪行为依法防卫举报报案但防卫不过当，公共场合侵权则提醒，不听就算了。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "以互惠作理由：你也不会希望自己不被允许讨厌别人。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "指出奉行这些原则会自然获得群体影响力与威望；攻击者会激起受益者义愤，而这些行为也是他人的权利，你无权剥夺。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "说明劝阻公开攻击的两个目的（易招真实危险、被报复者会把账算在你头上），并建议在自己的圈子里请求不要出手；提醒即可，不必勉强。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "第 4)、5) 条：公职与契约责任照旧不受影响；除非对方主动请求，不要辩解说服或强求改变其立场，否则侵犯讨厌权。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014", "P015"], "summary": "提出应做最好的被讨厌者，让对方放心、安全、自由地讨厌，目的是让身边所有人不必恐惧与窒息。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018"], "summary": "给出关系层面的推理：人来往最大的顾虑是闹翻后难以收拾，人逡巡不前是怕被剥夺讨厌的权利而非因为你不可爱。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P019", "P020", "P021"], "summary": "以第一人称作出承诺：对我，你讨厌的权利会一直留着，讨厌我是安全、被尊重、不会招致不择手段报复的，故人们接近你不必顾虑。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023"], "summary": "观察性判断：可爱的人多，能让人不担心关系崩坏被报复的人少；可接近的要害在于后悔是否会受害。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P024", "P025"], "summary": "结论：做最好的被讨厌者才是战胜“讨厌”的办法，这就是被爱的能力。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应对被讨厌，最重要的是尊重别人讨厌的权利。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "只要不是公共场合（别人自己家里、私下聚会等），都允许别人吐槽。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有中间人传私下埋怨或言语攻击，不要听，也要中间人不要传，因为这类怨恨难以消化且妨碍重要的事。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "遇公报私仇或不法侵扰，该防卫就防卫、该举报报案就举报报案；但正当防卫不要过当，对方不超出私域就完全没有反对的立场。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若对方在公共场合以言论等侵犯你的权益，提醒一下不合适；实在不听就算了。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "互惠理由：你也不会希望自己不被允许讨厌别人。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "明白这些原则为何设立并能大体奉行，将会自然而然拥有很大的群体影响力和群体威望。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "攻击你的言论会激起受益群体的义愤，但义愤与维护自身利益同样是他人权利，你不见得有权力剥夺。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "劝对方不要在公开场合攻击，不是为保护名誉或人设，而是因为此举易招真实危险，且被报复者常会把账算在你身上。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若真要保护对方讨厌的权利，有必要在自己的圈子里请求所有人不要出手攻击、给予容忍。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "与人为善可以提醒对方一下，但不必勉强，因为有人会反过来说你是威胁、吓唬，反增误会。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "自己负责的公职一切照办，欠款照偿、合同照样履行，既有契约责任不因对方讨厌自己而受影响。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "除非对方主动请求，否则不要辩解说服、不要强求改变其立场态度，否则本身就是对“讨厌权”的侵犯。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被讨厌了，就当一个对方从未遇到过的最好的被讨厌者，让对方放心、安全、自由地讨厌。", "evidence": ["E17", "E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样做不仅为某一个人，而是为了让身边所有人都能不必恐惧和窒息。", "evidence": ["E19"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人和人往来最大的顾虑是担心有一天闹翻，尤其亲密的人翻脸生厌会难以收拾。", "evidence": ["E20"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人逡巡不前不是因为对方不可爱，而是怕自己被剥夺讨厌的权利。", "evidence": ["E21"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以第一人称承诺：对“我”不必顾虑，讨厌的权利会一直留着，讨厌我是安全、被尊重、不会招致不择手段报复的。", "evidence": ["E22", "E23"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "（承接上句）于是人们接近你就不必顾虑再三。", "evidence": ["E24"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可爱的人甚多，能让你不必担心关系崩坏被报复的人甚少；人可不可接近，要害在于后悔是否会受害。", "evidence": ["E25", "E26"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做一个最好的被讨厌者才是战胜“讨厌”的办法，这就是被爱的能力。", "evidence": ["E27", "E28"]},
    {"claim_id": "C022", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者只问“被人讨厌了怎么办？”，未提供具体情境（Q001 属提问者，无正文段落可引）。", "evidence": []}
   ],
   "argument_steps": [
    "先立总纲“尊重别人讨厌的权利”（P001），再展开为 1)—3) 条具体规则（P002-P004）。",
    "以互惠（你也希望可以讨厌别人）支持该立场（P005）。",
    "说明奉行后的两种后果：获得群体威望；攻击者会招致受益者义愤而你不便剥夺其行动自由（P006-P007）。",
    "转入操作：解释劝阻公开攻击的两个目的，并建议请求圈内人容忍（P008-P010）。",
    "补出第 4)、5) 条：契约责任照旧；不主动辩解说服（P011-P012）。",
    "提出角色姿态“最好的被讨厌者”，并给出其目的（P013-P015）。",
    "解释关系层面机理：人怕的是闹翻后受害，故怕失去讨厌的权利（P016-P018）。",
    "以第一人称承诺示范这一姿态，并指出其效果（P019-P021）。",
    "以观察对比收束，得出“被爱的能力”这一结论（P022-P025）。"
   ],
   "concept_usage": [
    {"term": "讨厌的权利", "meaning": "他人对自己抱持并表达厌恶的自由；作者以是否超出私域为其实际边界", "evidence": "P001", "ambiguity": "公共场合的言论攻击被单列为可提醒事项，与“权利”的界限未严格界定"},
    {"term": "私域", "meaning": "别人自己家里、私下聚会等非公共场合", "evidence": "P002", "ambiguity": "未给出穷尽式界定"},
    {"term": "被讨厌者", "meaning": "能够让他人放心、安全、自由地讨厌自己的人", "evidence": "P013", "ambiguity": "与“被爱的能力”等同使用，未展开定义"},
    {"term": "契约责任", "meaning": "公职、欠款、合同等既有义务，不因对方讨厌自己而改变", "evidence": "P011", "ambiguity": "未说明其与“讨厌权”冲突时的优先顺序"},
    {"term": "被爱的能力", "meaning": "本文用作“最好的被讨厌者”的收束性表述", "evidence": "P025", "ambiguity": "仅一句作结，未有界定，是否属作者自造术语不明"},
    {"term": "群体威望", "meaning": "奉行这些原则后自然获得的群体影响力", "evidence": "P006", "ambiguity": "获得机制未说明"}
   ],
   "examples_and_targets": [
    "别人自己家里、私下聚会的场合（P002）：作者举的私域例子",
    "中间人传私下埋怨乃至言语攻击（P003）：作者提示的应对对象",
    "公报私仇或不法侵扰（P004）：作者举的例外情形",
    "公共场合的言论类侵犯（P004）：作者举的可提醒情形",
    "仰慕者与受益者中血气方刚或实力强大之人出手惩戒报复（P008）：作者设想的风险场景",
    "攻击者被报复后认定“肯定是你煽动的”（P008）：作者设想的归因",
    "公职、欠款、合同（P011）：作者举的契约责任例子",
    "作者自身（“对我就不必”P019）：第一人称示范对象"
   ],
   "conditions": [
    "1) 条以“只要不是公共场合”为条件，私域内允许吐槽（P002）。",
    "3) 条以“遇到公报私仇或者不法侵扰这类犯罪行为”为条件，并附“正当防卫不要过当”“对方不超出自己的私域”两项限定（P004）。",
    "对方在公共场合侵权时的处理以“实在不听就算了”为终点（P004）。",
    "劝阻公开攻击以“有必要”为前提，且提醒“不必勉强”，因可能被误解为威胁（P009、P010）。",
    "5) 条以“除非对方主动请求”为例外条件（P012）。",
    "效果性表述带“客观上”“将会自然而然”的预测限定（P006）。"
   ],
   "rhetoric_and_tone": "教诲与经验总结口吻，条目化编排（1)—5)）夹以说理段；使用“与人为善”“实在不听就算了”等让步语气，避免命令式；末段转为第一人称承诺（对我就不必）作为示范，并以定义式短句“这就是被爱的能力”收束，整体克制平和。",
   "unresolved_questions": [
    "P002“只要不是公共场合……都允许别人吐槽”字面可读作“凡非公共场合一律允许”，与其私域区分的意图之间存在表述歧义，需研究者判断。",
    "“被爱的能力”仅以一句作结，未界定；是否借用外部概念需外部核查。",
    "“群体影响力和群体威望”的获得机制未说明，属作者经验判断。",
    "“对我就不必”所指的关系对象与作者身份未在本文说明。",
    "公共场合言论攻击与“讨厌的权利”之间的界限标准未给出。",
    "提问者未提供情境，本文给出的是通则式建议，未针对具体个案。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "最重要的是尊重别人讨厌的权利。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "1）只要不是公共场合——比如在别人自己家里、或者别人私下聚会的场合——都允许别人吐槽。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "有中间人要传这类私下埋怨乃至言语攻击给你听，不要听，而且要中间人不要传。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "但这样会触发太多本能的怨恨，难以消化，而这些怨恨对于真正重要的事很碍事。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "如果遇到公报私仇或者不法侵扰这类犯罪行为，那么该武力防卫就武力防卫，该举报举报，该报案报案。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "始终记住对方有讨厌你的权利，只要对方不超出自己的私域，就完全没有反对的立场。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P004", "quote": "如果对方在公共场合做侵犯你权益的行为（主要是言论一类），提醒一下对方这样不合适。实在不听就算了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P005", "quote": "你也不会希望不被允许讨厌别人。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P006", "quote": "你将会自然而然拥有很大的群体影响力和群体威望。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "你也不见得有权力去剥夺他人行动的自由。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "不是为了保护自己的“名誉”或者“人设”，而是为了两个目的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "第二，被报复之后，那位攻击者常会将账算在你身上，认定“肯定是你煽动的”，更生仇怨。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P009", "quote": "有必要要在自己的圈子里说明一下请求所有人不要出手攻击，给予容忍。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P010", "quote": "与人为善的话就提醒对方一下，但也不必勉强", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P011", "quote": "一切既有的契约责任不受这一点的影响。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P012", "quote": "除非对方主动请求，否则不要尝试辩解和说服，更不要强求改变对方的立场和态度。这本身就是对对方的“讨厌权”的侵犯。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P013", "quote": "被讨厌了，就当一个对方从未遇到过的最好的被讨厌者。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P014", "quote": "让对方可以放心的、安全的、自由的讨厌。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P015", "quote": "而是为了让所有你身边的人能不必恐惧和窒息。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P016", "quote": "人和人来往，最大的顾虑就是担心如果有一天闹翻了怎么办。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P018", "quote": "不是因为你不可爱，而是担心有这么一天，怕自己被剥夺讨厌的权利。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P019", "quote": "对我就不必，对我，你讨厌的权利我会一直给你留着。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P020", "quote": "讨厌我是可以的，是安全的，是被尊重的，是不会招致不择手段的报复的。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P021", "quote": "于是人们接近你就不必顾虑再三。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P022", "quote": "你觉得“可爱”的人甚多，但可以让你不必担心万一关系崩坏会被报复的人却甚少。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P023", "quote": "人可不可接近，要害根本不在于这人是否可爱，而在于如果后悔是不是会受害。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P024", "quote": "做一个最好的被讨厌者，这才是战胜“讨厌”的办法。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P025", "quote": "这就是被爱的能力。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往与关系伦理", "冲突管理与个人边界", "心理调适与社会评价"],
   "issue_candidates": ["被讨厌时的应对", "讨厌权的私域／公共场合边界", "报复风险与劝阻他人代出气", "契约责任不因好恶改变", "建立可以安全翻脸的关系"],
   "text_function_candidates": ["答复提问", "经验总结", "行动建议", "说理"],
   "object_candidates": ["提问者", "中间人（传话者）", "仰慕者与受益者", "攻击者", "公职与合同相对方"],
   "working_keywords": ["讨厌的权利", "被讨厌者", "私域", "正当防卫", "契约责任", "被爱的能力", "群体威望"]
  },
  "notes": "无图片节点，纯文本正文（P001-P025）。提问字段 Q001 属提问者，不构成正文段落，故未生成 evidence_refs。本篇无版本或结构分歧标记。"
 },
 "34e3b005": {
  "analysis": {
   "question_context": "提问者只问“怎么理解西方的普世价值？”（Q001 属提问者字段，无对应 Pnnn 证据），未给出具体文本或人物。作者从措辞入手判定“西方”加“普世”本身自相矛盾，给出改写表述，并主张普世价值非人所能定义，而是由自然规律强制实施的自然道德律；随后反驳以一时优势地位论证真理的做法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "指出“西方”的“普世”价值是自相矛盾的词组，须改写为【西方】【部分国家】所【主张的】普世价值【候选方案】。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "界定普世价值：不由人定义表决，而是深埋于历史运行规律、由自然规律铁血实施的自然道德律；人负认知义务而无定义权力。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P007"], "summary": "以地球立方体、光速非极速的思想实验反问：一致同意能否改变自然。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "承认西方提出假说与部分实验数据，但离最终结论尚远，其最大基石是部分国家一时的优势地位。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "以希腊幸存、亚历山大帝国与罗马倒掉、蒙古帝国崩溃等反问，说明优势地位不能证明真理，称此为帝国精神病。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "提出只有人类演化到极远未来、银河诸界重新聚首，或许才有差不多真实靠谱的最终答案。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015"], "summary": "结论：现在谈“普世”是利用人类集体无意识的天生幼稚以求野心得逞，鼠目寸光。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“西方”的“普世”价值本身就是一个自相矛盾的词组。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该词必须改写为【西方】【部分国家】所【主张的】普世价值【候选方案】，才能消除其内生的矛盾。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "普世价值不由人来定义和表决，也不能由人自己决定信奉就成立。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的普世价值是深埋在历史运行规律之中、由一切其他自然规律负责铁血实施的自然道德律。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人对普世价值负有无限的认知义务，而没有任何定义的权力。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "以思想实验反问：即使全世界一致投票认定地球是立方体、一致同意光速非极速，也不能把地球变方或让光速改变。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "西方可以提出关于普世价值的假说并给出一些实验数据，但远未到足以作出万世不移的最终结论的程度。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该假说最大的基石，就是部分国家在一时的优势地位。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以历史反问：若优势地位足以证明理论是客观真理，希腊何以从波斯手下幸存、亚历山大帝国与罗马何以倒掉、蒙古帝国凭什么崩溃。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些帝国在顺风顺水时都自认手握真理，这不过是一种帝国精神病。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "普世价值究竟是什么，要等人类踏入太空、广布银河、分化亚种、失落重逢成为常态并演化到再无更多可能之后，银河诸界重新聚首，或许才有差不多真实靠谱的最终答案。", "evidence": ["E11", "E12"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在谈“普世”，不过是企图利用人类集体无意识的天生幼稚让那点可怜的野心得逞，属鼠目寸光。", "evidence": ["E13", "E14"]},
    {"claim_id": "C013", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者问“怎么理解西方的普世价值？”，未给出所据文本或人物（Q001 属提问者，无正文段落可引）。", "evidence": []}
   ],
   "argument_steps": [
    "从措辞切入判定词组自相矛盾（P001），给出带方括号的改写表述并以反问确认（P002-P003）。",
    "正面给出定义：普世价值是自然道德律，人只有认知义务（P004-P006）。",
    "用地球立方体与光速的思想实验类比支持“人不能定义自然”（P007）。",
    "对西方主张作有限承认，指出其基石是一时优势地位（P008-P009）。",
    "以四个帝国兴亡的反问反驳“优势即真理”，并给出“帝国精神病”的判断（P010-P011）。",
    "提出得出结论所需的极远未来条件（P012-P013）。",
    "以贬评收束（P014-P015）。"
   ],
   "concept_usage": [
    {"term": "普世价值", "meaning": "本文指深埋在历史运行规律之中、由一切其他自然规律负责铁血实施的自然道德律，非人所能定义或表决", "evidence": "P005", "ambiguity": "与日常语用中“被普遍接受的价值”不同，作者未说明该定义的来源"},
    {"term": "自然道德律", "meaning": "作者用以指称被自然规律强制实施的道德法则", "evidence": "P005", "ambiguity": "是否为既有哲学术语的借用，本文未注明"},
    {"term": "候选方案", "meaning": "在改写表述中限定西方主张只具候选地位", "evidence": "P002", "ambiguity": "未说明候选者之间的比较或检验程序"},
    {"term": "帝国精神病", "meaning": "指优势地位国家顺风顺水时自认手握真理的心态", "evidence": "P011", "ambiguity": "非严格术语，未给判定标准"},
    {"term": "人类集体无意识的天生幼稚", "meaning": "作者对受众接受“普世”说法的心理判断", "evidence": "P014", "ambiguity": "未引证心理学依据"}
   ],
   "examples_and_targets": [
    "“西方”“普世”这一词组本身（P001-P002）：被批评的对象",
    "地球是立方体、光速不是极速的一致同意设想（P007）：作者思想实验",
    "西方提出的假说与实验数据（P008）：被有限承认的对象",
    "希腊从波斯帝国手下幸存（P010）：作者举的历史反问例",
    "亚历山大帝国、罗马、蒙古帝国的倒掉或崩溃（P010）：作者举的历史反问例",
    "“部分国家在一时的优势地位”（P009）：作者指认的假说基石",
    "人类踏入太空、广布银河、失落而重逢的姐妹文明（P012-P013）：作者设想的未来条件"
   ],
   "conditions": [
    "以“如果全世界人一致投票认定地球是个立方体……或者我们一致同意光速不是极速”为假设条件（P007）。",
    "以“若是你的优势地位就足以证明你的理论肯定是客观真理”为归谬前提（P010）。",
    "有限承认以“也不可否认ta们也提出了一些实验数据”与“远没到……程度”作两重限定（P008）。",
    "得出最终答案的条件为：人类踏入太空、广布银河、分化亚种、失落重逢成为常态、演化到只能坐看宇宙熄灭、银河诸界重新聚首（P012-P013），并以“设若”“或许”标示其非现实性。"
   ],
   "rhetoric_and_tone": "短篇论辩体，先下定义后反驳；反问句密集（是不是一旦这样表述、能不能把地球变成方的、何以会倒掉），并用方括号【】作改写标记以突出措辞问题；末两段转为尖锐贬评（帝国精神病、鼠目寸光，徒增笑耳），带讽刺与训诫色彩。",
   "unresolved_questions": [
    "“自然道德律”与“历史运行规律”的具体所指及理论来源未说明，需外部核查。",
    "P012-P013 的远景条件属作者设想，判定“最终答案”出现的标准未给出。",
    "作者未讨论西方普世价值的具体内容条目，只作总体定性，故对提问者“怎么理解”的回答范围有限。",
    "P008 所称“实验数据”具体所指未列明。",
    "反驳对象为泛指，未点名具体人物、著作或文本。",
    "P010 的历史断言（希腊从波斯手下幸存、诸帝国崩溃原因）属事实性主张，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“西方”的“普世”价值……这本身就是一个自相矛盾的词组。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这东西必须首先做正确的表述才能消除自己内生的矛盾——【西方】【部分国家】所【主张的】普世价值【候选方案】。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "普世价值不是由人来定义和表决的，也不能由人自己决定信奉就成立。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "真正的普世价值是深埋在历史运行规律之中，由一切其他自然规律负责铁血实施的自然道德律。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "人对它负有无限的认知义务，而没有任何定义的权力。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "如果全世界人一致投票认定地球是个立方体，能不能把地球变成方的？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "但这还远没到足以做出万世不移的最终结论的程度。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P009", "quote": "因为这个假说最大的基石，就是部分国家在一时的优势地位。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "那么希腊为何能从波斯帝国的手下幸存？亚历山大帝国何以会倒掉？罗马如何会倒掉？蒙古帝国又凭什么崩溃？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "这不过是一种帝国精神病而已。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "要等人类踏入太空，广布银河，分化出其他亚种，有了失落而重逢的姐妹文明", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "设若那时，银河诸界还能重新聚首，或许能有一个差不多真实靠谱的最终答案。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "现在谈“普世”，不过是企图利用人类集体无意识的天生幼稚以求那点可怜的“野心”得逞。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "鼠目寸光，徒增笑耳。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学与价值理论", "国际政治与意识形态", "历史哲学"],
   "issue_candidates": ["普世价值的定义权", "西方价值主张的普遍性声称", "以优势地位论证真理", "价值的历史检验与未来条件"],
   "text_function_candidates": ["答复提问", "概念辨析", "论辩与批评"],
   "object_candidates": ["西方", "部分国家", "希腊", "波斯帝国", "亚历山大帝国", "罗马", "蒙古帝国", "银河诸界（设想）"],
   "working_keywords": ["普世价值", "自然道德律", "候选方案", "帝国精神病", "集体无意识", "优势地位"]
  },
  "notes": "无图片节点，纯文本正文（P001-P015）。提问字段 Q001 属提问者，不构成正文段落，故未生成 evidence_refs。本篇无结构分歧标记。"
 },
 "ad044d94": {
  "analysis": {
   "question_context": "提问者问如何站在上帝视角评价清初“反清复明”者、他们是可敬还是可笑（Q001 属提问者字段，无对应 Pnnn 证据），其框架预设了后人的“上帝视角”与“可笑”这一评价选项。作者先否定该视角前提，再提出评价标准：为理想行动并敢于牺牲者可敬，与当时是否现实、当下是否符合政治正确无关；并区分可悲与可笑，声明对“反清复明”本身立场中立。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出核心判断：为理想行动且敢于面对艰苦危险牺牲者都可敬，与理想当时是否现实、评判者当下是否符合政治正确无关。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "理由：行动者当时事在人为、现实与否无人能知；现代政治正确是否现实正确或“未来正确”同样未知。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "反驳提问预设：后人所站并非上帝视角，只是知道后续部分剧情的观众视角，严格说还须了解事件之后的全球历史。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "重申有理想并认真献身本身总是可敬的；若理想逻辑不通，则看不通之处是否超出当事人思考能力，超出则无可批评。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "严格限定“可悲”仅指明知逻辑不通仍自欺欺人并栽跟头；即便如此也谈不上可笑，否则是五十步笑百步。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012"], "summary": "正面主张：对己对事实诚实、不自欺、选定有价值的理想并鞠躬尽瘁是人最好的活法之一；超出能力的智慧才能看出的问题不是你的问题；成败不足论。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "反击常觉他人“可笑”的“智慧”者，称其真正嘲笑的是“人有理想”；并声明作者本人对“反清复明”立场中立。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何为了自己的理想而行动、敢于面对艰苦危险乃至牺牲的人，都是可敬的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "可敬与否与该理想在行动者当时是否“现实”、在评判者当下是否符合政治正确没有关系。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "在行动者当时一切都事在人为，无人能断定什么现实；现代的政治正确是否真是现实正确或“未来正确”也无人知道。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "后人所站视角并不是“上帝视角”，只是知道后续部分剧情的观众视角；严格说要了解事件之后的全球历史才算“知道后续”。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人有了理想并认真为此献身，这本身总是可敬的。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若理想本身逻辑不通，要看不通之处是否超出当事人的思考能力；若超出，则其并非明知不通而自欺，便无可批评。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "只有当事人自己明明清楚逻辑不通、硬是自欺欺人并栽了跟头，这才可称可悲。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "即使自欺欺人致败也谈不上可笑；若这算可笑，那不过是五十步笑百步。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对自己与事实诚实、不自欺，选定有价值的理想并鞠躬尽瘁死而后已，是人最好的活法之一。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "要用超出你能力的智慧才能看出的问题，不是你可以避免的问题，不是你的问题。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成败更不足论（不构成评价行动者的依据）。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与献身者相比，常觉他人“可笑”的“智慧”者的人生要可悲得多，因为其真正嘲笑的是“人有理想”这件事。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明：本人对“反清复明”立场中立。", "evidence": ["E15"]},
    {"claim_id": "C014", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者以“上帝视角”发问，问清初“反清复明”者可敬还是可笑（Q001 属提问者，无正文段落可引）。", "evidence": []}
   ],
   "argument_steps": [
    "先立评价标准：为理想行动且敢于牺牲者皆可敬，与是否现实、是否合政治正确无关（P001-P002）。",
    "以行动者当时的不确定性与“未来正确”的不可知作理由（P003-P004）。",
    "先拆提问前提：后人只有观众视角，不是上帝视角（P005）。",
    "重申献身本身可敬，并对“理想逻辑不通”的情形给出以当事人思考能力为准的限定（P006-P007）。",
    "把“可悲”严格限于明知不通而自欺者，否认“可笑”的评价（P008-P009）。",
    "提出正面主张（诚实、不自欺、鞠躬尽瘁），并排除超出能力的问题与成败两项依据（P010-P012）。",
    "以反击嘲笑者作结，并加 PS 声明对评价对象本身立场中立（P013-P014）。"
   ],
   "concept_usage": [
    {"term": "上帝视角", "meaning": "提问者用语；作者否认后人拥有，改称只是知道后续部分剧情的观众视角", "evidence": "P005", "ambiguity": "作者未给出“知道后续”的完整标准，只说至少须了解事件之后的全球历史"},
    {"term": "可敬", "meaning": "本文针对“为理想而行动并敢于牺牲”这一行为样态的评价", "evidence": "P001", "ambiguity": "是否包含道德评价或仅指勇气，本文未展开"},
    {"term": "可悲", "meaning": "限于明知理想逻辑不通仍自欺欺人并因此栽跟头者", "evidence": "P008", "ambiguity": "与“可笑”的区分依赖当事人是否明知，但如何认定“明知”未说明"},
    {"term": "政治正确", "meaning": "评判者当下的正当性标准；作者称其未必是现实正确或“未来正确”", "evidence": "P002", "ambiguity": "未界定其具体内容与判定者"},
    {"term": "事在人为", "meaning": "行动者当时的不确定性，现实与否不可预判", "evidence": "P003", "ambiguity": "未说明其与历史条件的限度关系"}
   ],
   "examples_and_targets": [
    "清初“反清复明”者（提问者提出的评价对象，正文未列举具体人物或事件）",
    "“站在上帝视角”的评价框架（Q001 预设，正文 P005 予以反驳）",
    "常觉他人“可笑”的“充满智慧”者（P013）：被反驳对象",
    "希腊、帝国兴亡一类历史对照未出现；本文历史材料仅为泛指的“后人知道后续剧情”（P005）与“成败”（P012）"
   ],
   "conditions": [
    "如果理想本身逻辑不通，判准是不通之处是否超出当事人自己的思考能力（P007）。",
    "只有当事人明明清楚逻辑不通、仍自欺欺人并栽跟头，才可称可悲（P008）。",
    "如果这算可笑，那也不过是五十步笑百步（P009）。",
    "后人要算“知道后续”，至少要把待评价事件之后的全球历史都了解了（P005）。",
    "作者明说自己对“反清复明”立场中立，其评价针对行为样态而非该理想（P014）。",
    "“要用超出你能力的智慧才能看出的问题”被排除在可归责范围之外（P011）。"
   ],
   "rhetoric_and_tone": "短章评议体，先立标准后回应提问前提；反问句密集（谁知道什么现实？笑人的人自己又如何不可笑呢？），并以“上帝视角／观众视角”“五十步笑百步”作对照比喻；语气由说理转为对嘲笑者的尖锐反讽（充满“智慧”加引号），末句以 PS 作立场声明收束。",
   "unresolved_questions": [
    "正文未列举清初“反清复明”的具体人物、事件或史料，作者未作个案评价，故对提问对象的直接回答有限。",
    "“理想本身逻辑不通”与“超出当事人思考能力”如何判定，本文未给标准。",
    "“政治正确”“未来正确”的所指与判定者未界定。",
    "“可敬”是否含道德评价、与“成败不足论”的关系未展开。",
    "作者身份与对“反清复明”中立声明的背景未在本文说明。",
    "提问者所问“上帝视角”的出处与含义未给出。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "任何为了自己的理想而行动，而且敢于面对艰苦、危险乃至牺牲的人，都是可敬的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这跟这个理想本身在行动者当时而言是否“现实”、在评判者自己的当下是否符合政治正确没有关系。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "因为在行动者的当时，一切都事在人为，谁知道什么现实、什么不现实？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "现代的政治正确是否真的是现实正确、是否是“未来正确”，又有谁知道？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "后人所站的视角也并不是“上帝视角”，而只是一个知道后续部分剧情的观众视角罢了", "relation": "contradicts"},
    {"key": "E6", "paragraph_id": "P006", "quote": "人有了一个理想，然后认真的为此献身了，这本身总是可敬的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "如果这个理想本身逻辑不通，要看这不通的点是不是超出了当事人的思考能力。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P007", "quote": "那么就什么可批评处都没有。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "只有当事人自己明明清楚逻辑不通，硬是自欺欺人，然后栽了跟头，这才可称可悲。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P009", "quote": "如果这算可笑，那么也不过是五十步笑百步而已", "relation": "contradicts"},
    {"key": "E11", "paragraph_id": "P010", "quote": "自己对自己诚实、对事实诚实，不要自欺欺人，选定一个有价值的理想，然后鞠躬尽瘁、死而后已，这是人最好的活法之一。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "要用超出你能力的智慧才能看出的问题，不是你可以避免的问题，不是你的问题。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "成败更不足论。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "因为ta们真正嘲笑的是“人有理想”这件事。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "PS：我本身对“反清复明”立场中立。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["历史评价与史学方法", "价值哲学（理想与行动）", "政治正确批评"],
   "issue_candidates": ["以成败或政治正确评价历史行动者", "后人视角的限度（上帝视角是否存在）", "自欺与可悲的界限", "理想本身是否构成价值"],
   "text_function_candidates": ["答复提问", "评论与论辩", "价值判断"],
   "object_candidates": ["清初“反清复明”者（提问者提出）", "后人／评判者", "常觉他人“可笑”的“智慧”者"],
   "working_keywords": ["上帝视角", "观众视角", "可敬", "可悲", "可笑", "政治正确", "事在人为", "鞠躬尽瘁、死而后已"]
  },
  "notes": "无图片节点，纯文本正文（P001-P014）。提问字段 Q001 属提问者，不构成正文段落，故未生成 evidence_refs。正文未列举“反清复明”具体人物与史料，评价针对行为样态而非该政治立场（P014 声明中立）。"
 },
 "9c38e8c1": {
  "analysis": {
   "question_context": "提问者描述一种讨论僵局：一方摆事实讲史料，另一方以“史料可以被人篡改，所以都不可信”回应，问该如何应对（Q001 属提问者字段，无对应 Pnnn 证据）。提问同时转述了该第三方主张。作者不提供说服办法，而是承认该说法逻辑上无问题，指出它击溃了讨论基础、使局面进入“实力说话／实践检验”阶段，并按边境、劳资、学术、政策四类情形说明“下一阶段”的形态与行动选择。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "承认对方说法在逻辑上毫无问题，并以南海、中印边界问题同样被此类argument顶着作反证式说明。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "界定讨论是文明解决问题、以理论演算替代真实碰撞；提出该argument即击溃讨论基础，直接进入“实力说话”“实践检验”。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "指出这是每个参与讨论者用脚投票的权利。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "分列四类情形进入下一阶段的形态：边境争端看实际控制，劳资纠纷进入辞职/解雇/起诉，学术争论拼引用率与影响因子，政策争论等结果揭晓。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013"], "summary": "结论：探讨阶段结束，不再存在“说服”问题；唯一要确定的是对方是否接受进入下一阶段；只有强势者、决定者才需出于仁慈多问一句。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015"], "summary": "分位势给建议：对方确认后即给其追求的后果；若自己弱势则放弃说服、准备迎接后果。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018"], "summary": "以对句收束：讨论才有所谓结果，行动只有后果；说这话即是不打算要结果而打算接后果。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“史料可以被人篡改，所以都不可信”这话从逻辑上毫无问题。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "南海、中印边界问题至今未解决，也同样是被这样的argument顶着的。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论解决问题是尝试文明的解决问题，用理论演算替代真实的碰撞与物理的挫折。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提出这样的argument本质上击溃了对话讨论的基础，直接进入“实力说话”“实践检验”阶段。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是每一个参与讨论者用脚投票的权利。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "按纠纷类型分别进入下一阶段：边境争端进入“实际控制定结果”，劳资纠纷进入辞职/解雇/起诉，学术争论进入拼引用率与影响因子，政策争论进入等待结果揭晓。", "evidence": ["E6", "E7", "E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "探讨阶段就此结束，已不再存在“说服”问题，因为对方并没有说错什么，也完全有这个选择权。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你唯一要确定的是：就此进入“下一阶段”是不是对方打算接受的结果。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "多问一句主要适用于你是强势者、决定者，且进入下一阶段对方恐怕会很惨的情形，此时才出于仁慈和同情发问。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方确认后，就带着对其勇气和决心的钦佩，给其追求的后果。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果你是弱势一方，对方说出这话就不必继续说服，放弃幻想、准备迎接后果。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论才有所谓结果，行动只有后果；说这话就是不打算要结果、而打算接后果了。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "讨论中的另一方主张“史料可以被人篡改，所以都不可信”，据此拒绝史料举证（经提问者转述，说话者本人未出场、身份未说明）。", "evidence": []},
    {"claim_id": "C014", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者描述该僵局并问该如何应对（Q001 属提问者，无正文段落可引）。", "evidence": []}
   ],
   "argument_steps": [
    "先承认对方说法逻辑上无问题（P001），以南海与中印边界问题作反证式说明（P002）。",
    "界定讨论的性质是文明解决问题、以演算替代真实碰撞（P003）。",
    "指出提出该argument即击溃讨论基础，进入实力说话与实践检验（P004），并称这是用脚投票的权利（P005）。",
    "列举边境、劳资、学术、政策四类情形说明“下一阶段”的形态（P006-P009）。",
    "据此宣布探讨阶段结束、说服问题消失，并把焦点转为对方是否接受下一阶段（P010-P012）。",
    "限定多问一句的适用情形（强势者、决定者，P013），再分位势给出行动建议（P014-P015）。",
    "以“讨论才有结果，行动只有后果”作格言式收束（P016-P018）。"
   ],
   "concept_usage": [
    {"term": "argument", "meaning": "本文特指以“史料可被篡改故不可信”否定对方举证的论述方式（按原文用英文词）", "evidence": "P002", "ambiguity": "单复数与范围未界定，作者两次使用同一词形"},
    {"term": "文明的解决问题", "meaning": "以理论演算替代真实碰撞与物理挫折的讨论方式", "evidence": "P003", "ambiguity": "未说明其与“实力说话”之间的界限是否可以并存"},
    {"term": "用脚投票", "meaning": "参与讨论者退出讨论、转向行动的选择权", "evidence": "P005", "ambiguity": "未区分主动退出与被迫退出"},
    {"term": "实力说话／实践检验", "meaning": "讨论基础被击溃后所处的阶段", "evidence": "P004", "ambiguity": "在学术、政策等非对抗场景中如何落实，本文未展开"},
    {"term": "结果／后果", "meaning": "讨论产生“结果”，行动只产生“后果”，本文以二者对举划定讨论与行动的界限", "evidence": "P016", "ambiguity": "对举用语，未作严格定义"},
    {"term": "下一阶段", "meaning": "各领域对应的实际行动阶段（实际控制、辞职解雇起诉、拼引用率、等待结果）", "evidence": "P012", "ambiguity": "未穷尽列举"}
   ],
   "examples_and_targets": [
    "“史料可以被人篡改，所以都不可信”（提问者转述的第三方主张，P001 起被作者回应）：讨论对手方观点",
    "南海问题、中印边界问题（P002）：作者类比证据（事实性主张，需外部核查）",
    "边境争端的“实际控制定结果”（P006）：作者举例",
    "劳资纠纷的辞职/解雇/起诉（P007）：作者举例",
    "学术争论拼引用率和影响因子（P008）：作者举例",
    "政策争论等待结果揭晓（P009）：作者举例"
   ],
   "conditions": [
    "四类情形的后果分别以“如果是边境争端／劳资纠纷／学术争论／政策争论”为条件（P006-P009）。",
    "多问一句以“你是强势者、决定者”且“进入下一阶段ta恐怕会很惨”为条件（P013）。",
    "给后果以“ta确认了”为前提（P014）。",
    "若“你是弱势一方”，则不继续说服而准备迎接后果（P015）。",
    "作者承认对方“并没有说错什么，也完全有这个选择权”，作为其不再劝说的前提（P011）。"
   ],
   "rhetoric_and_tone": "冷静而带反讽的短论：先以“这话从逻辑上毫无问题”作让步，随即用“不然南海、中印边界问题早就解决了”反刺；主体用“如果是……那就……”四段并列推进，语气克制；结尾转为格言式对句（讨论才有所谓结果，行动只有后果），并以“以上。”干脆收束，带教训意味但不作道德评价。",
   "unresolved_questions": [
    "提问者问“该如何应对”，本文未给说服或反驳办法，只给出退出讨论、转入行动阶段的判准，回答范围与提问不完全对应。",
    "“实力说话”“实践检验”阶段在非对抗场景（学术、政策）中如何落实，未展开。",
    "如何判断自己是强势者还是弱势者，本文只以自指句式交代，未给标准。",
    "第三方主张者的身份、领域与具体讨论语境未说明。",
    "“因为对方并没有说错什么”是否为反讽，存在解读空间，作者未明确表态。",
    "P002 以南海与中印边界问题作类比，属事实性主张，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这话从逻辑上毫无问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不然南海、中印边界问题早就解决了——这些问题也一样是被这样的argument顶着的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "讨论解决问题是在尝试文明的解决问题，尝试用理论的演算来替代真实的碰撞、物理的挫折。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "提出这样的argument，本质上就击溃了对话讨论的基础，直接进入“实力说话”、“实践检验”阶段了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这个是每一个参与讨论者用脚投票的权利。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "如果是边境争端，话说到这个份上就没有继续讨论的基础了，进入“实际控制定结果”阶段了。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "如果是劳资纠纷，那么就进入到辞职/解雇/起诉阶段了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "如果是学术争论，那就进到了各发论文拼引用率和影响因子阶段了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "如果是政策争论，那就进入到下定决心，等待结果揭晓的阶段了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "总而言之，探讨阶段就此结束了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "已经不再存在“说服”问题了——因为对方并没有说错什么，也完全有这个选择权。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "你唯一要确定的是——就此进入“下一阶段”是不是ta打算接受的结果。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "这主要是指你是强势者、决定者，进入下一阶段ta恐怕会很惨，这时你才要出于仁慈和同情多问一句。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P014", "quote": "ta确认了，那就带着对ta的勇气和决心的钦佩，给ta追求的后果就是了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "如果你是弱势一方，对方说出这话就不用继续去说服了，放弃幻想，准备迎接后果就是了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "讨论才有所谓结果，行动只有后果。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "说了这话，就是不打算要结果，而打算接后果了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["论证与讨论方法论", "历史认识论（史料可信性）", "冲突解决与博弈"],
   "issue_candidates": ["以史料可被篡改否定举证", "讨论与行动阶段的转换条件", "用脚投票权", "说服的边界与后果承担"],
   "text_function_candidates": ["答复提问", "评论与短论", "行动建议"],
   "object_candidates": ["讨论中的另一方（史料不可信主张者）", "南海", "中印边界", "劳资纠纷双方", "学术争论者", "政策争论者"],
   "working_keywords": ["argument", "史料篡改", "用脚投票", "实力说话", "实践检验", "实际控制", "结果与后果"]
  },
  "notes": "无图片节点，纯文本正文（P001-P018）。提问字段 Q001 属提问者，不构成正文段落，故未生成 evidence_refs；被转述的第三方主张（史料不可信）归属为 unknown/quoted_or_cited，未归给作者。本篇无结构分歧标记。"
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
