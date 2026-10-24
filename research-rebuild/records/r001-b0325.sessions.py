# -*- coding: utf-8 -*-
"""批次 r001-b0325 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0325.sessions.py            # 写 out/r001-b0325.out.jsonl
  python3 records/r001-b0325.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0325"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0325.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f1298897": {
  "analysis": {
   "question_context": "afdian 专栏文《早恋1》，question 字段仅为标题“早恋 1”，无独立提问正文；brief 给出的语境是：父母往往突然得知子女开始谈恋爱、远早于自己的预期，作者要讨论“身为父母，如何在这个条件下给予子女可能的最好教育”，并强调不是“引导”而是教育。正文前半以“我们”讨论父母的做法，自 P031 起转为父母对自家孩子（“你”）的直接训话，作者是否即为该父母、还是代拟家长口吻，本文未说明。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "设定语境：父母突然得知子女早恋、不知怎么办；作者提出要讨论父母在此条件下能给出的最好教育。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "区分“引导”与“教育”：引导是已知路线、当引水员指挥舵手；教育是讲规则、举例，但不知具体策略，只能给告知和装备，不能给具体决策。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "提出第一个问题“你能不能反对”，回答是不能；并限定这个“不能”并非无权（监护权赋予合法反对甚至禁止的权限），而是从客观实践看不宜用反对方式处理。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "反对不宜的三重理由：损耗父母影响力；使恋情转入地下并教会子女反侦察；青少年靠对抗直接控制获取存在感、还混入“为爱抗争”的崇高感，故强行禁止适得其反。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "重估反对的真实动机（怕耽误学习）：双方互相看上说明子女是高魅力个体，高魅力对应高社会性发展道路，父母应调整原计划、按高魅力现实加强高社会性训练，犹如命中注定有洪水就学好游泳冲浪。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "以“不反对”为起点列出当即需要解决的问题，第一是揭破窗户纸——你是怎么知道的。", "role": "transition"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026"], "summary": "知情途径分三类；若子女是秘密交往一段时间后才告知，应先反省并修复信任关系，因为没有信任，其他行动几乎没有有效性基础，只剩副作用过强的强制手段。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "重点谈“你没告诉我、我自己知道”的情形：由此引出隐私和自由密切相关，既然做不到密不透风，就要处理走漏风声的后果，子女也会猜测泄密者。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036"], "summary": "作者的监护人行动：与对方家长接触，不是反对，而是提示对方注意交往中的责任；因双方均为未成年人，出问题监护人须承担连带责任，故对称地要求对方也受约束；其后果是对方父母会知情。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P037", "P038", "P039", "P040", "P041", "P042"], "summary": "推演后果：对方父母将紧盯成绩，任何下滑都会以作者的孩子为首要怀疑目标；因为对方不是成年人，世界确实按“不影响年轻人”的原则运转，影响年轻人前途者须向其监护人交代，如今责任落在“你”头上。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047"], "summary": "说明父母为何难以无动于衷：投入已超过六位数字（尚不计时间感情），若外来因素使成果受损，父母不可能对其有任何好感，最多做到尽量不违法；以宠物被他人乱喂致病为类比，指出对方父母正是这样盯着“你”。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P048", "P049", "P050", "P051"], "summary": "推出双方额外的义务：谁都不能表现下滑，各自的下滑会招致对方父母的厌恶；因此加倍努力是对对方最基本的保护和爱；若都是成年人则法律立场不同，但两人都是未成年人。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P052", "P053", "P054", "P055"], "summary": "把避免感情被父母视为诅咒定为最基本的责任，并称这责任由自然法（天命）决定而非父母强加；要求对任何不利于对方学习的事明确反对并记录在案，爱最基本的起点是这种坚持而非甜蜜温柔。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P056", "P057"], "summary": "收尾表明父母总体态度中立（既不反对也不赞成），虽担忧但不提前制造障碍；后续取决于两人如何处理，并祝愿善待对方、保护好自己。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母不能反对子女早恋；这个“不能”不是没有权利（监护权本就赋予合法反对甚至禁止的权限），而是从客观实践来看不宜用反对的方式处理。", "evidence": ["E4", "E5"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反对会严重破坏和耗损父母对子女的影响力，而这种影响力在之后的监护使命中还有至关重要的作用。", "evidence": ["E6"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“我不许”在实践中效果可疑，容易使恋情转入地下；反复的震怒和惩罚只会教会子女反侦察，而不是让其服输、放弃。", "evidence": ["E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "此期青少年有强烈存在感需求，对抗和摆脱直接控制是存在感的重要源泉，还混入“为爱抗争”的崇高感，因此强行禁止往往适得其反。", "evidence": ["E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若双方确实互相看上（而非单恋），说明子女属于高魅力个体；高魅力个体有走高社会性发展道路的强烈合理性，父母应主动调整原计划，顺应高魅力条件加强高社会性方面的训练和教育。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若子女是秘密交往一段时间后才告知，父母应反省并优先修复信任关系；没有信任关系，其他行动几乎没有有效性基础，只剩实力支撑的强制手段，而其副作用过强。", "evidence": ["E14", "E15"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "隐私和自由密切相关；既然没有能力做到不动声色、密不透风，就要处理走漏风声带来的后果。", "evidence": ["E16", "E29"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作为监护人，知情后将与对方家长接触，但不表示反对、不要求对方禁止交往，只是提示对方注意其在这场交往中的责任；因双方都是未成年人，出问题监护人须承担连带责任。", "evidence": ["E17", "E18"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "对方父母知情后会紧盯子女的学习成绩和各方面发展，一旦有任何下滑迹象甚至进展速度不如预期，就会把作者的孩子作为首要怀疑目标。", "evidence": ["E19"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为对方不是成年人，世界的确要围绕“不影响年轻人”的原则转；谁影响年轻人的前途，谁就要向其监护人交代，而不能以“这小孩自己怎么不躲着点”之类的说法卸责。", "evidence": ["E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者在子女身上的总投入已超过六位数字（仅纯金钱，未计时间与感情），因此若外来的人或因素使这一成果受损，父母不可能对造成结果者有任何好感，最多能尽量不违法、不伤天害理。", "evidence": ["E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "早恋的两人因此有一项额外义务——谁都不能表现下滑；从自己立场出发要加倍努力，这其实是对对方最基本的保护和爱。", "evidence": ["E23", "E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "避免感情被父母认定为诅咒和厄运是最基本的责任，这责任不是父母强加的，而是自然法决定的，父母自己也是被自然强制而有这样的不可克服的本能（作者称此为天命）。", "evidence": ["E25"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若对方在确定关系后做任何不利于其学习的事，无论看上去多贴心甜蜜，都要明确表示反对并记录在案，否则将来难以辩护。", "evidence": ["E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者（父母）现在的总体态度是中立的，既不反对也不赞成；确实担忧，但不能仅因担忧就提前故意制造障碍。", "evidence": ["E28"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱最基本的起点是这种坚持（不让爱成为彼此不能成为最好的自己的原因），而不是所谓的甜蜜、温柔。", "evidence": ["E27"]}
   ],
   "argument_steps": [
    "情境设定：父母突然得知子女早恋且远早于预期（P001）。",
    "定义先行：区分“引导”（已知路线、任引水员）与“教育”（讲规则、给装备，不知具体策略）（P003-P005）。",
    "第一问：能不能反对？答：不能反对（P006-P007）。",
    "限定：无权的“不能”不成立，父母有监护权；此处指实践上不宜（P008）。",
    "理由一：反对耗损影响力这一后续监护资源（P009）。",
    "理由二：禁止使恋情转入地下，惩罚训练出反侦察（P010）。",
    "理由三：青少年以对抗控制获取存在感，混入为爱抗争的崇高感（P011）。",
    "小结：强行禁止往往适得其反（P012）。",
    "转向：反对的真实动机是怕耽误学习（P013）。",
    "重估：双方互相看上即证明子女高魅力；高魅力指向高社会性道路（P014-P015）。",
    "推论：父母应调整原计划，按高魅力现实加强高社会性训练（P016-P019）。",
    "转换起点：站在“不反对”的起点上处理当即问题（P020-P022）。",
    "问题一：你是如何知情的（三条途径）（P023-P024）。",
    "条件分支：若子女秘密交往后才告知，先修复信任（P025）。",
    "重点分支：“我自己知道”引出的隐私与走漏风声后果（P027-P030）。",
    "作者的行动方案：接触对方家长、提示责任、连带责任与对称约束（P031-P036）。",
    "后果推演：对方家长盯成绩，“你”成为首要怀疑目标（P037-P039）。",
    "法理说明：未成年人情境下“谁影响前途谁向监护人交代”（P040-P042）。",
    "动机说明：投入与损失厌恶（含宠物类比）（P043-P047）。",
    "义务结论：谁都不能表现下滑，加倍努力即对对方的保护与爱（P048-P051）。",
    "根据升格：责任源于自然法/天命，非父母强加；对不利学习之事须反对并记录（P052-P055）。",
    "收束：父母态度中立，后续取决于两人自己（P056-P057）。"
   ],
   "concept_usage": [
    {"term": "引导", "meaning": "父母已知道具体路线，像引水员站在船头指挥舵手左转右转——即替子女作具体决策。", "evidence": "P004", "ambiguity": "与日常语义的“引导”可能不同，作者是窄化用法。"},
    {"term": "教育", "meaning": "对新加入的玩家讲述游戏规则、操作顺序并举例说明，但对其具体策略和发展一无所知，只给告知与装备。", "evidence": "P004-P005", "ambiguity": "作者以游戏作比，未给正式定义。"},
    {"term": "高魅力个体", "meaning": "被实践判决为“双方对上了眼”的子女，其社会关系会自然大量涌来，对应走高社会性的发展道路。", "evidence": "P014-P015", "ambiguity": "未给出判定标准；仅以“不是单恋”为条件。"},
    {"term": "影响力", "meaning": "父母对子女的影响力，被视为后续监护使命中至关重要的资源，会因反对而被消耗。", "evidence": "P009", "ambiguity": "未说明如何度量或恢复。"},
    {"term": "隐私和自由", "meaning": "二者密切相关；做不到密不透风就必须承担走漏风声的后果。", "evidence": "P028-P029", "ambiguity": "未展开论证二者关系。"},
    {"term": "连带责任", "meaning": "未成年人交往出问题时监护人必须承担的责任，不能以“我一点不知情”搪塞。", "evidence": "P034", "ambiguity": "未指明法律条文，属作者的法律断言，待外部核查。"},
    {"term": "自然法", "meaning": "作者用来指称父母本能的强制来源，与“天命”并用，说明该责任非父母强加。", "evidence": "P052-P053", "ambiguity": "未定义，与法学意义上的自然法关系不明。"},
    {"term": "中立", "meaning": "作者自述对这段早恋的总体态度：既不反对也不赞成，但确实担忧。", "evidence": "P056", "ambiguity": "“担忧”与“中立”的边界未说明。"}
   ],
   "examples_and_targets": [
    "外卖员送一单能赚多少钱、各种劳动者一天的工作（P043）：作者用于核算投入规模的论据。",
    "“我们在你身上付出的总投入已经超过六位数字”（P043）：作者自述数据，未给出核算依据，需外部核查。",
    "“学而优则仕”的“正途”（P016）：作者所指的父母原有计划，作为被调整的对象。",
    "宠物类比：养的小猫/小狗/小兔子被人不经同意喂食致病，回来尾巴不能摆动（P045）：作者类比证据。",
    "对方家长视角的推演（P038）：作者设想对方父母的心理（修辞性推演，非事实陈述）。",
    "假想的对方孩子的话“她几天没跟我讲话，我心里一片空白”（P039）：作者设想的场景引用。",
    "被否定的推搪说法“我一点不知情”（P034）：作者的反驳对象（未指明具体人）。",
    "“走漏风声者”候选名单（P030）：面向读者的修辞性设问。",
    "“为爱抗争”的崇高感（P011）：作者对青少年动机的概括，带引号但未注明来源。"
   ],
   "conditions": [
    "“不能反对”的理由是实践性的：父母在法律上仍有监护权赋予的反对甚至禁止权限（P008）。",
    "高魅力判决只在“不是单恋，而是双方对上了眼”时成立（P014）。",
    "若子女秘密交往一段时间后才告知，修复信任关系优先于其他问题（P025）。",
    "强制手段只有在“有当即的生命安全风险”时才宜使用（P025）。",
    "若双方都是成年人，正文字段所说的“向监护人交代”逻辑与法律立场会不同（P040、P050）。",
    "对方父母紧盯成绩的推演以“未成年人”身份为前提（P037-P041）。",
    "对不利于学习之事的反对须“记录在案”，否则将来难以辩护（P054）。",
    "父母不提前制造障碍的理由是“仅仅因为担忧就制造障碍并不公平、也对上天不敬”（P056）。"
   ],
   "rhetoric_and_tone": "对家长说话与对自家孩子训话两种人称并存：前半以“我们”讨论父母应如何做，P031 起转为“我—你”的直接训诫。大量设问自答（“这就引出第一个问题——你能不能反对。答案非常分明——你不能反对。”）、比喻（引水员与舵手、洪水与游泳冲浪、宠物被乱喂）、反问（“你难道就会因为这个而改变对ta的反感吗？”）、以及“天命”“自然法”“噬脐莫及”“积毁销骨”等庄重措辞。整体为说理加训诫的劝导语气，结尾转缓和（“我们希望你善待对方，保护好自己”）。",
   "unresolved_questions": [
    "question 字段仅为标题“早恋 1”，无独立提问者与提问内容，来源为 afdian 专栏。",
    "brief 与正文首段基本重复，brief 末尾“所谓”为截断，不能据此补充正文。",
    "作者身份不明：文中“我们/我”是父母视角，但作者是否即该父母、或代拟家长口吻，本文未说明。",
    "“六位数字”投入、“一节课折合多少人民币”等为作者自述，未给依据，需外部核查。",
    "“自然法”在本文未定义，与“天命”并用，指涉不明。",
    "“记录在案”的记录形式、保存者与用途未说明。",
    "父母双方意见不一致（一方反对一方中立）时的处理未讨论。",
    "标题为《早恋1》，暗示有后续篇，本篇未给出完整教育方案。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多父母是突然知道自己的子女开始谈恋爱的，远早于自己的预期", "relation": "context"},
    {"key": "E2", "paragraph_id": "P004", "quote": "所谓引导，是指你已经知道具体路线，担任引水员", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "你只能给对方最好的告知和装备，无法给对方具体的决策。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "答案非常分明——你不能反对。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "这个“不能”，是指从客观实践来看不宜用反对的方式来处理", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "这种反对会严重的破坏和耗损你对子女的影响力", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "很容易导致子女把恋情转入地下，变为隐蔽状态", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "对抗和摆脱直接的控制、禁止是证明存在感的重要源泉", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "强行禁止，往往适得其反。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "这可以说是实践给了你一个判决——你的子女属于高魅力个体", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "高魅力个体，有走高社会性的发展道路的强烈合理性", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "也就是要顺应高魅力的条件，提升高社会性方面的训练和教育。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "既然命中注定有洪水，那就索性把游泳和冲浪学好。", "relation": "context"},
    {"key": "E14", "paragraph_id": "P025", "quote": "修复这个信任关系可能比别的问题更首要", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "那些手段的副作用过强", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P028", "quote": "隐私和自由是密切相关的", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P033", "quote": "我不会去表示反对，或者要求对方家长禁止ta和你交往", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P034", "quote": "监护人必须要承担连带责任", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P037", "quote": "就会把你作为首要怀疑目标", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P041", "quote": "谁影响年轻人的前途，谁就要向ta的监护人交代", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P043", "quote": "我们在你身上付出的总投入已经超过六位数字", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P045", "quote": "我们是绝不可能对造成这结果的人或者事物有任何好感的", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P048", "quote": "谁都不能表现下滑", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P051", "quote": "你要加倍努力，这其实是对对方最基本的保护和爱", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P052", "quote": "这责任不是父母强加的，而是自然法决定的", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P054", "quote": "你都一定要表示明确的反对，而且要记录在案", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P055", "quote": "是这种坚持，而不是所谓的甜蜜、温柔，才是爱最基本的起点。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P056", "quote": "我们现在的态度是中立的，既不是反对、也不是赞成", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P029", "quote": "你既然没有能力做到不动声色、密不透风", "relation": "qualifies"},
    {"key": "E30", "paragraph_id": "P040", "quote": "如果对方是成年人，说这种话就没有意义", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P050", "quote": "如果你们都是成年人，这个逻辑就有另一种算法", "relation": "qualifies"},
    {"key": "E32", "paragraph_id": "P045", "quote": "你就想想你养的小猫/小狗/小兔子", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭教育", "亲子关系", "青少年心理", "恋爱与婚恋"],
   "issue_candidates": ["早恋", "父母是否应反对子女恋爱", "监护权与信任关系", "隐私与自由", "未成年人监护人连带责任", "教育投入"],
   "text_function_candidates": ["答疑/专栏答复", "说理", "训诫", "经验与主张陈述"],
   "object_candidates": ["父母", "子女/未成年人", "对方父母", "监护人", "外卖员与劳动者（举例）"],
   "working_keywords": ["早恋", "引导", "教育", "高魅力个体", "高社会性", "影响力", "走漏风声", "隐私和自由", "连带责任", "自然法", "天命", "中立"]
  },
  "notes": "afdian 专栏文；question 字段即标题“早恋 1”，无真实提问者，brief 与正文首段基本重复（brief 末尾截断于“所谓”）。正文 57 段、无图片；lexical 节点计数 60 与正文段落数不一致，但 walk_body 未报告 text/lexical 差异，属空段落被跳过。人称在中途由“讨论父母该怎么做”转为父母对自家孩子的直接训话，已在 unresolved_questions 登记。"
 },
 "a6ce8e89": {
  "analysis": {
   "question_context": "知乎问答，提问为“如何评价柯洁发文「B站动态再见」，随后删光相关动态的行为？”。作者在正文中没有提及柯洁，也没有直接评论该事件，而是就“当众演讲/公众发言需要什么资格”作一般论辩：发言需要深厚的社会学功力、众所周知的德行与足够觉悟，三者构成“三花聚顶”的门槛；未达门槛而轻率触碰高度争议议题，被视为对社会的客观威胁。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出总前提：当众演讲需要非常深厚的社会学功力，来源可以是街头、历史、师门或参谋团队，但必须有经过验证和积淀的功底。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "发言者需对公众反应有基本正确的认知、对误解可能保持敬畏、为公众的“补强倾向”打认知基础；并需有若干众所周知的德行作底层基础，使公众自然地正面理解其话。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "举袁隆平、钟南山、钱学森为例：他们即使说争议性话，人们也很少选择恶意解读的版本；故公众人物一定爱惜羽毛。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "定义式判断：“飞扬跳脱”只是对恶意解读毫无敬畏的美化描述；往好说是英勇无畏，往坏说是不知死活傻大胆。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "德行的保护力会被磨损、可被透支；透支后任何含糊歧义都可能因恶意理解失去抑制而发酵成重大灾难。因此客观上只有德高望重者才有资格讲高度争议性的话，这也给他们巨大社会责任。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010"], "summary": "德高望重者要么慎言少说，要么在社会学功底上下巨大苦工（实地调查走访、参与治理前线实践、久历沉浮、学贯古今识通中外）；这是几千个日夜的点滴之功，有无付出自己知道。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012"], "summary": "没下苦功却轻率触摸高度争议敏感议题，是对社会极为严重的客观威胁；此时公众只有两个选择：认定你“不懂事”而原谅但从此视为不靠谱的娱乐性角色，或认定你认真刻意而清除这个把公众利益视如玩具的威胁。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "以原子弹与核按钮作比：核按钮不能掌握在不严肃的人手中；德行不足又屡次拿核按钮闹着玩，公众忍耐会一次次削薄；不接受“他毕竟没有真的按下去”的辩解，不离开操作台警卫就要开枪。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P017"], "summary": "小结规范：有多少德行、多深的功底、多大的觉悟，就说多少话。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "反驳“社会需要胆大妄为才能保持活力”：社会只需保证“三花聚顶”的人足够多即可既稳定又活泼；把敏感议题挑战权下放到门槛线以下的“宽容社会”有数学上难以抑制的不稳定性，如同变异率过高的机体——高适应力与高致癌率是同一特性的两个副效应，须以优先避免致癌为前提，门槛不可能长期搁置。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P022", "P023"], "summary": "结论：德行、功底、觉悟是真正的说话资格；不要说没资格说的话、参与不够格参与的话题，客观社会规律不会容忍这种妄行。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P024", "P025", "P026"], "summary": "给出出路：若真想参与这些议题，只能加倍厚积德行、增进对社会的浸淫了解、加倍严格审视对人类的爱的信念；人只会接受爱人的冒犯与批评，先厚积德行、先下苦工、先对牺牲毫无侥幸是“真挚爱人”最基本的见证；没有就不要僭越。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当众演讲需要非常深厚的社会学功力；这份功底可以来自街头、历史、师门传承或参谋团队，但必须是经过验证和积淀的功底。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "发言者要对公众的反应有基本正确的认知、对各种被误解的可能性保持敬畏，并需有若干众所周知的德行作底层基础，促使公众正面理解其话、避免被恶意解读。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "袁隆平、钟南山、钱学森哪怕说了有争议、存在恶意解读空间的话，人们也很少选择恶意解读的版本。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓“飞扬跳脱”，只是对恶意解读的可能毫无敬畏、从不回避的美化描述。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "德行的保护力会被磨损，一旦透支，任何含糊、歧义都可能因受众中不可避免的恶意理解失去抑制、迅速发酵而导致重大灾难。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "客观上只有德高望重的人才有资格讲高度争议性的话；这也给他们巨大的社会责任，绝不能轻易用这种特权破坏社会的稳定和和谐。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "德高望重者要么慎言少说，要么在社会学功底上下巨大苦功（实地调查走访、深度参与治理前线实践、久历沉浮、学贯古今识通中外），这是几千个日夜的点滴之功。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没下这份苦功却轻易假设自己能料定大众反应、轻率触摸高度争议的敏感议题，实际上是对社会极为严重的客观威胁。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "此时公众只有两个选择：认定你“不懂事”并原谅，但从此视为不靠谱的娱乐性角色；或认定你认真、严肃、刻意，于是把这个将公众利益视如玩具的威胁清除。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "德行不足以让人寄托信任、又有多次拿核按钮闹着玩的记录，那么每玩一次公众的忍耐就削薄一次；“他毕竟没有真的按下去”这类辩解不能成立。", "evidence": ["E15", "E29"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有多少德行、有多深的功底、有多大的“即使可能被误解、付出代价也值得冒险一试”的觉悟，就说多少话。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对“社会需要这种胆大妄为才能保持活力”的看法，作者反驳称社会只需保证“三花聚顶”的人足够多，就足够既维持稳定又活泼发展。", "evidence": ["E18", "E30"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "把重大敏感议题的挑战权下放到低于三根门槛线以下的“宽容社会”有着数学上难以抑制的不稳定性，如同变异率过高的机体——高适应性和高致癌率是同一种特性不可分割的两个副效应；必须以优先避免致癌为前提追求高适应力，故“三花聚顶”的门槛不可能长期搁置。", "evidence": ["E19", "E20", "E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "德行、功底、觉悟是真正的说话资格；不要说没资格说的话、参与还不够格参与的话题，客观的社会规律不会容忍这种妄行。", "evidence": ["E23", "E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若真希望参与这些议题，正确的选择只能是加倍厚积德行（先无可否定地造福社会）、加倍增进对社会的浸淫和了解、加倍严格审视自己对人类的爱的信念。", "evidence": ["E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人只会接受爱人的冒犯、只会宽容爱人的批评；开口前先厚积德行、先下血汗苦工、先对牺牲毫无侥幸，就是“真挚爱人”最基本的见证；没有这些就不要僭越。", "evidence": ["E26", "E27", "E28"]}
   ],
   "argument_steps": [
    "总前提：公众发言需要深厚且经积淀的社会学功力（P001）。",
    "条件一：对公众反应有清醒认知、对误解保持敬畏、为“补强倾向”打基础（P002）。",
    "条件二：以众所周知的德行作善意理解的底层基础（P003）。",
    "举证：袁隆平、钟南山、钱学森的例子（P004）。",
    "推论：故公众人物爱惜羽毛（P005）。",
    "反例界定：“飞扬跳脱”即对恶意解读毫无敬畏（P006）。",
    "机制：德行保护力可被透支，透支后歧义发酵成灾难（P007）。",
    "资格命题：客观上唯德高望重者有资格讲高度争议的话，并负巨大社会责任（P008）。",
    "两条路径：慎言少说，或下巨大苦功（P009-P010）。",
    "后果：未下苦功而触碰敏感议题，是对社会的客观威胁（P011）。",
    "公众的两种反应：视为不靠谱的娱乐角色，或清除威胁（P012）。",
    "比喻展开：核按钮不能交给不严肃的人，忍耐逐次削薄（P013-P016）。",
    "规范小结：有多大德行、功底、觉悟就说多少话（P017）。",
    "回应异议：不必靠胆大妄为保持活力，“三花聚顶”者够多即可（P018）。",
    "类比论证：宽容社会如高变异率机体，高适应力伴随高致癌率（P018-P021）。",
    "结论：德行、功底、觉悟是说话资格，规律不容妄行（P022-P023）。",
    "行动要求：先厚积德行、了解社会、审视爱人类的信念；无之则勿僭越（P024-P026）。"
   ],
   "concept_usage": [
    {"term": "三花聚顶", "meaning": "文中指德行、功底、觉悟三项门槛（P018 称“三根门槛线”，P022 点明三项），达到者才具备讲高度争议性话的资格。", "evidence": "P018、P020、P022", "ambiguity": "作者自造/借用的比喻性说法，未说明词源，也未给出任何一项的可操作判据。"},
    {"term": "社会学功力", "meaning": "指导公众发言所需的、经检验与积淀的功底，包括对社会反应和误解可能的清醒认知。", "evidence": "P001-P002", "ambiguity": "未界定其构成与衡量方式。"},
    {"term": "德行（保护力）", "meaning": "众所周知的、无可否认的德行，可使公众自然地正面理解发言；其保护力会被磨损、可被透支。", "evidence": "P003、P007", "ambiguity": "未说明德行如何积累与折算。"},
    {"term": "公众的补强倾向", "meaning": "发言者需为其打下认知基础的一种公众心理倾向。", "evidence": "P002", "ambiguity": "全文仅此一处出现，未定义。"},
    {"term": "觉悟", "meaning": "“即使可能被误解、付出代价也值得冒险一试”的觉悟，是说话资格之一。", "evidence": "P017、P022", "ambiguity": "未说明如何判断觉悟是否足够。"},
    {"term": "核按钮（原子弹）", "meaning": "比喻高度争议性议题的发言权：掌握者须严肃且德行足以让人信任。", "evidence": "P013-P016", "ambiguity": "比喻映射关系由读者推断，作者未逐项对应。"},
    {"term": "宽容社会", "meaning": "把重大敏感议题的挑战权下放到门槛线以下的社会形态；作者认为其有不稳定性。", "evidence": "P018-P021", "ambiguity": "未举实例，也未界定“门槛线以下”的具体界线。"}
   ],
   "examples_and_targets": [
    "柯洁发文并删动态（Q001）：提问中的评价对象，正文完全未提及，作者未直接评论。",
    "袁隆平、钟南山、钱学森（P004）：作者例证，用于说明德行作保可抑制恶意解读。",
    "“三花聚顶”“三根门槛线”（P018、P020、P022）：作者自造的比喻性术语。",
    "原子弹、核按钮、控制室、地堡、警卫开枪（P013-P016）：作者的比喻材料。",
    "变异率过高的机体、癌症（P018-P021）：作者类比材料。",
    "假想异议“社会需要这种胆大妄为才能保持活力”（P018）：作者的反驳对象，说话者未指明。",
    "被预设并拒绝的辩解“他毕竟没有真的按下去”（P015）：作者的反驳对象。",
    "“不懂事”的公众评价（P012）：作者设想的公众反应之一。",
    "“英勇无畏”“不知死活傻大胆”（P006）：作者对“飞扬跳脱”的两种评价口径。"
   ],
   "conditions": [
    "发言资格以德行、功底、觉悟三项门槛为条件（P008、P017、P022）。",
    "德行保护力一旦透支，含糊与歧义就可能失控（P007）。",
    "“宽容社会”的不稳定性被作者称为“数学上难以抑制”，且“一旦运气不好就会得癌症，一次就会致命”（P018、P021）。",
    "觉悟的含义包含“即使可能被误解、付出代价也值得冒险一试”（P017）。",
    "若真想参与敏感议题，唯一正确选择是先厚积德行、了解社会、审视爱人类的信念（P024）。",
    "类比论证适用于“把重大敏感议题的挑战权下放到门槛线以下”的情形（P018）。"
   ],
   "rhetoric_and_tone": "第二人称训诫体，语气严厉、断然（“你没有，就不要僭越。”“警卫就要开枪了。”）。密集使用比喻与夸张：原子弹/核按钮/地堡/警卫，机体变异率与致癌率。多处反问（“你站到地堡外面来，看你自己能不能忍？”）。对假想异议先立后破（“也许有人会觉得……”）。末段以短句收束，带有道德训诫色彩；对“飞扬跳脱”一词作贬义重新定义。",
   "unresolved_questions": [
    "提问问柯洁删动态，正文全篇未出现柯洁或该事件，作者与提问的具体对应关系不明，无法确定是否针对该事件。",
    "“三花聚顶”的词源与是否有既有出处（如道教内丹术语）本文未说明。",
    "“公众的补强倾向”全文仅一处出现，未定义，含义不明。",
    "“数学上难以抑制的不稳定性”未给出模型、数据或推理依据，需外部核查。",
    "“宽容社会”未举实例，“三根门槛线”的具体界线未说明。",
    "P018 以逗号结尾接 P019（“不稳定性，/就像……”），跨段成句，按结构仍作两段处理。",
    "“也许有人会觉得”“胆大妄为”处带引号，表明作者在引述某种流行说法，但说话者不明。",
    "作者所称“几十年/几千个日日夜夜”的功底是否可观测、公众如何判断他人是否具备，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "当众演讲是需要非常深厚的社会学功力的", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "对各种被误解的可能性保持充分的敬畏", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你要有若干件众所周知的、无可否认的德行作为一个底层基础", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "人们很少会去选择那个恶意解读的版本来作为自己的理解", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "所谓的“飞扬跳脱”，就是对恶意解读的可能毫无敬畏、从不回避的美化描述而已", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "保护力一旦透支，你的任何含糊、歧义，都可能因为广大受众中不可避免的恶意理解的失去抑制、迅速发酵而导致重大灾难", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "客观上就德高望重的人才有资格讲高度争议性的话", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "绝不能轻易的利用自己的这种特权来破坏社会的稳定和和谐", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "要么就要选择慎言、少说，要么就要在这个社会学功底上下巨大的苦工", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "是几千个日日夜夜的点滴之功", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "实际上是一种对社会极为严重的客观威胁", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "要么认定你是“不懂事”，原谅你，但从此你要被视为一个不靠谱的人物，一个娱乐性的角色", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "要么认定你是认真的、严肃的、刻意的，于是只能把你这个将公众利益视如玩具的威胁清除", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "原子弹不能掌握在不严肃的人手中。", "relation": "context"},
    {"key": "E15", "paragraph_id": "P014", "quote": "那么你每玩一次，公众的忍耐就会削薄一次。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "你不举起双手离开操作台，警卫就要开枪了。", "relation": "context"},
    {"key": "E17", "paragraph_id": "P017", "quote": "有多少德行、有多深的功底、有多大的“即使可能被误解、付出代价也值得冒险一试”的觉悟，就说多少话。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "但事实上社会只需要保证“三花聚顶”的人足够多就足够既维持稳定、又活泼发展", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "有着数学上难以抑制的不稳定性", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P019", "quote": "高适应性和高致癌率是同一种特性的两个不可分割的副效应。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P020", "quote": "你必须以优先避免致癌为前提去追求高适应力", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P020", "quote": "这个“三花聚顶”的门槛是不可能长期搁置的。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P022", "quote": "德行、功底、觉悟，是你真正的说话资格。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "不要说你没资格说的话、参与你还不够格参与的话题，客观的社会规律不会容忍这种妄行。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P024", "quote": "那么你正确的选择只能是加倍厚积你的德行", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "人只会接受爱人的冒犯，只会宽容爱人的批评。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P025", "quote": "就是这个“真挚爱人”最基本的见证。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P026", "quote": "你没有，就不要僭越。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P015", "quote": "看你能不能听那些“他毕竟没有真的按下去”这种辩解？", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P018", "quote": "也许有人会觉得“社会需要这种胆大妄为才能保持活力”", "relation": "context"},
    {"key": "E31", "paragraph_id": "P021", "quote": "但一旦运气不好就会得癌症，一次就会致命。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["公共言论伦理", "社会评论", "舆论与传播", "社会秩序与稳定"],
   "issue_candidates": ["公众人物的发言资格", "德行与信任", "争议性议题的发言边界", "社会稳定与活力的取舍", "误解与恶意解读"],
   "text_function_candidates": ["评论", "论辩", "训诫", "比喻性说理"],
   "object_candidates": ["公众人物", "德高望重者", "公众/受众", "柯洁（仅见提问）", "袁隆平", "钟南山", "钱学森"],
   "working_keywords": ["三花聚顶", "社会学功力", "德行", "功底", "觉悟", "恶意解读", "保护力", "核按钮", "宽容社会", "致癌率", "僭越"]
  },
  "notes": "知乎回答；正文 26 段、无图片、无平台话题标签段。提问对象柯洁未在正文出现，作者以一般论辩作答，对应关系不明，已在 unresolved_questions 登记。P018 句末为逗号，与 P019 构成跨段长句，按结构记录为两段，未合并改写。"
 },
 "5d69d569": {
  "analysis": {
   "question_context": "afdian 专栏文《早恋2》，question 字段仅为标题“早恋 2”，无独立提问正文；brief 说明本篇谈第二个问题“不表演感情”，即不要把交往变成被围观的连续剧。作者以“我们/我”对“你们”（早恋中的两人）说明为何不应让第三方围观恋情，并给出 never tells 的规范。篇名暗示承接《早恋1》，但本篇未复述其“高魅力”等设定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "提出第二个问题“不表演感情”：不要把交往变成一场被围观的连续剧、不要享受旁人围观；两人之间的事除彼此父母可知情外，正常情况下不应有不在场第三方知情，更不必说点评、参与。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "原因一：早恋类型客观上被打上“高魅力”标签，会引发嫉妒与敌意凝视，暗恋者还会视之为深刻损失；自我察觉与控制不足、对权利边界和伦理规范缺少认识的青少年，可能先在情绪上敌对、再在无意识中发起攻击；不低调等于刺激他人未被驯服的内心野兽，害人害己（如把金子丢在桌上）。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013", "P014", "P015"], "summary": "原因二：防止被虚荣绑架、扮演别人编剧的男女主角；“嗑CP”者的反馈实为无声“下单”，不按订单会被贬为“舔狗”，按订单演出则等于认可其编剧、导演、监制职位；将来若要分手就是拆导演的台，会招来群体压力与“公敌、弃民”的处境，且做过多久公共CP主角就有多深罪恶。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "原因三：恋情直播使人难以分辨对方的关心是真情还是“剧情需要”“导演要求”，对方判断极大程度来自“CP参观群”与“后援会”的集体意见，于是问题变成爱的是一个人还是一个人设；人设崩塌后无论选“受害者”还是“罪人”都有代价，后者还须当众忏悔、越陷越深。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P020"], "summary": "提出两难的另一面：若选“受害者”，则对方按“公认一往情深”剧本演了这么久，反而落下“可耻的欺骗”罪，情何以堪。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023"], "summary": "归结：任由外人围观会使所有出路被堵死，因为围观者的诉求是精彩剧情而非主角的良好自我感觉或前途（如大巴车司机把方向盘交给开碰碰车的小朋友）；且“编剧”中还混着想取代主角的女二号、男二号与群演，这是糟糕的创作机制。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026"], "summary": "给出规范：恋情的第一道德是 never tells——非必要，不外露；除非当时就有第三人在场或彼此明确同意，否则不应有合法监护人或者司法机构以外的人知道；不得让作者发现未经许可的第三方知道“我以为只有你我知道的信息”，除非是双方父母或来查案的警察。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P027", "P028", "P029"], "summary": "违反的后果：作者将不认为这是“跟我恋爱”，而认定对方想当男主角、需要作者扮演洋娃娃；明知会带来巨大诅咒却为一己虚荣毫无敬畏，这种“爱”只是残酷的自私游戏，作者的爱第一个不可推卸的义务就是终止它；否则作者即“把黄金放在桌上，害朋友犯罪的愚妄之人”；此条无可妥协，是这种等级亲密关系的起点。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031"], "summary": "补充限定与收束：这是两人之间的事，如果成年连父母也无权刺探；恋情不容围观，这是对感情最基本的珍惜。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二个问题是“不表演感情”，即不要把两人的交往变成一场被围观的连续剧，也不要享受旁人的围观。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两人之间的事，除了彼此的父母可以知情，在正常情况下不应该有任何不在场的第三方知情，更不必说点评、参与。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "早恋的类型客观上会被打上“高魅力”标签，是对他人的强烈刺激信号；一直搞“现场直播”迟早引发难以抑制的嫉妒情绪与大量敌意凝视，且难以察觉的暗恋者会视这段恋情为深刻的损失和遗憾。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自我察觉与控制能力不足、对权利边界和伦理规范缺少深刻有效认识的小孩、青少年，往往会在想明白为什么之前就先讨厌、憎恨甚至敌对你，在计划好、想明白后果之前就无意识发起攻击性、破坏性的行动。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不保持低调等于无时无刻刺激和推搡不够成熟的同学朋友尚未被驯服的内心野兽，会招来难以预料也难以预防的意外曲折，害人害己（如把金子丢在桌上，一般人忍不住要拿）。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "另一个原因是要防止两人不自觉被虚荣绑架、不自觉去扮演别人编剧的男女主角。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "旁观者的“反馈”“建议”“提醒”实际上是在无声地向两人“下单”：不按订单生气就会被评价为“舔狗”“离了男人活不了”。", "evidence": ["E13", "E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若按订单交付合格演出，就会得到观众欢迎，因为通过这些响应等于认可了他们的编剧、导演、监制职位，恋爱就有了他们一份不可分割的参与和功劳。", "evidence": ["E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "将来若不喜欢这些安排、要分手，而对方按导演安排演得非常完美，客观上就是拆导演们的台、砸饭碗、毁灭乐趣、令观众心寒失望，会招来强大群体压力逼你“悔改”“想通”，否则成为整个群体的公敌、弃民。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做多久公共CP主角，分手时就有多深的罪恶：曾经落空、失望、成笑话的关注追捧，都会成为被看作自私、残忍、变态的贱人的“铁证”。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "搞恋情直播，在最开始的迷醉感过去之后，很难确定对方对自己的关心、殷勤到底是出于真情，还是出于“剧情需要”“导演要求”。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方对“该做什么、不该做什么”的判断，极大程度上来自“CP参观群”的主流意见与“后援会”的“集体智慧”。", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者向读者提出的问题：爱你的到底是一个人，还是一个人设？人设崩塌时，你到底是“被伪装欺骗了太久的受害者”，还是“不知道欣赏和怜惜导致对方无法再爱的罪人”？", "evidence": ["E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "选“受害者”则不必背负骂名、还可要求道歉赔偿；选“罪人”则要接受千夫所指、成为对方后援团的公敌，唯一补赎是当众忏悔，在别人导演的剧情里越陷越深。", "evidence": ["E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任由外人围观，最后外人施加的强烈干预会导致两人所有出路都被堵死，因为围观者的诉求是精彩的剧情，而不是男女主角的良好自我感觉或美好前途。", "evidence": ["E25", "E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“编剧”中还隐藏着想代替主角的“女二号”“男二号”以及想不通“凭什么ta们可以当主角”的群演；让这些人当编剧，男女一号落不到好，是糟糕的创作机制。", "evidence": ["E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恋情的第一道德就是 never tells——非必要，不外露。", "evidence": ["E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "两人之间的事，除非当时就有第三人在场，或者彼此明确同意，否则不应该有合法监护人或者司法机构以外的人知道。", "evidence": ["E30"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不得让作者惊讶地发现有不在场且未经许可的第三方知道“我以为只有你我知道的信息”，除非这人是双方父母或者来查案的警察。", "evidence": ["E31"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若违反，作者将不认为是“跟我恋爱”，而认定对方是想当男主角、只是需要作者扮演洋娃娃来实现梦想；这种为一己虚荣而毫无敬畏的“爱”只是残酷的自私游戏，作者的爱第一个不可推卸的义务就是让这游戏立刻终止。", "evidence": ["E32", "E33", "E34"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这一条无可妥协，需要与对方确认其不可动摇性；它是这种等级亲密关系的起点，做不到就给关系蒙上深刻的诅咒。", "evidence": ["E35"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这是两人之间的事，如果他们成年，连父母也无权刺探。", "evidence": ["E36"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "恋情不容围观，这是对感情最基本的珍惜。", "evidence": ["E37"]},
    {"claim_id": "C024", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者设问指出两难：若选“受害者”，则按“公认一往情深”剧本演出很久的对方，“没有功劳也有苦劳”，怎么反而落下“可耻的欺骗”罪。", "evidence": ["E24"]}
   ],
   "argument_steps": [
    "转入第二个问题“不表演感情”（P001-P002）。",
    "定义：不把交往变成被围观的连续剧，除彼此父母外不应有不在场第三方知情（P003-P004）。",
    "设问“为什么要这样”，展开三条理由（P005）。",
    "理由一之机制：高魅力标签→嫉妒与敌意凝视→潜伏暗恋者的损失感（P006）。",
    "理由一之主体：自我察觉与控制不足的青少年可能无意识发起攻击（P007）。",
    "理由一之结论：不低调等于刺激他人未被驯服的内心野兽，害人害己（P008）。",
    "理由二：防止被虚荣绑架、扮演别人编剧的男女主角（P009）。",
    "举证：嗑CP群体的“反馈”实为“下单”，不接单即被贬（P010-P011）。",
    "推论：接单演出即认可其编剧、导演、监制职位（P012）。",
    "推演：将来分手等于拆台，招来群体压力与公敌处境（P013-P014）。",
    "加重：做过多久CP主角就有多深罪恶，旧日追捧成为罪证（P015）。",
    "理由三：无法分辨真情与“剧情需要”，爱的是人还是人设（P016-P018）。",
    "两难：选受害者还是罪人，各有代价（P018-P020）。",
    "归结：外人围观使所有出路被堵死，围观者要的是剧情而非主角前途（P021-P022）。",
    "补强：编剧席中还有想取代主角的配角与群演（P023）。",
    "规范：恋情的第一道德是 never tells（P024）。",
    "例外限定：当场有第三人、彼此明确同意、双方父母、查案警察（P025-P026）。",
    "违约后果：认定对方想当男主角，这段“爱”是自私游戏，须立即终止（P027-P028）。",
    "收束：此条无可妥协，是关系的起点；成年后连父母也无权刺探（P029-P031）。"
   ],
   "concept_usage": [
    {"term": "不表演感情", "meaning": "本篇的核心规范：不把两人交往变成被围观的连续剧，也不享受旁人的围观。", "evidence": "P002-P003", "ambiguity": "未说明“表演”与正常社交分享的界线。"},
    {"term": "高魅力（标签）", "meaning": "早恋类型在客观上会被他人贴上的标签，构成对他人的强烈刺激信号。", "evidence": "P006", "ambiguity": "沿用《早恋1》的用法但本篇未定义，也未说明判断标准。"},
    {"term": "敌意凝视", "meaning": "由嫉妒引发的、来自周围人的敌意注视。", "evidence": "P006", "ambiguity": "未说明如何识别与应对。"},
    {"term": "下单/订单", "meaning": "旁观者的“反馈”“建议”“提醒”被作者类比为消费指令，按指令演出即交付。", "evidence": "P010-P012", "ambiguity": "比喻性用法，作者未说明是否存在明确的施压者。"},
    {"term": "编剧、导演、监制", "meaning": "指围观的同伴群体对两人恋情的剧本化安排与掌控角色。", "evidence": "P012-P013", "ambiguity": "三者未作区分使用。"},
    {"term": "人设", "meaning": "对方按群体期待维持的形象，与“一个人”相对；人设崩塌会引出受害者/罪人的身份选择。", "evidence": "P018", "ambiguity": "未说明人设与真实自我的可分辨性。"},
    {"term": "never tells", "meaning": "作者给出的英文口号式规范，等同“非必要，不外露”。", "evidence": "P024", "ambiguity": "英文表述未注明出处，作者未解释语法或用典。"},
    {"term": "合法监护人 / 司法机构", "meaning": "知情范围的例外主体：合法监护人与司法机构（以及查案警察）可在未经同意时知情。", "evidence": "P025-P026", "ambiguity": "是否包含学校、教师等其他主体未说明。"}
   ],
   "examples_and_targets": [
    "旁观者话术“他这样你还不生气？”“他对你真好，你很感动吧？”（P010）：作者引述的“反馈”“建议”“提醒”。",
    "“舔狗”“离了男人活不了”（P011）：作者引述的旁观者评价。",
    "“CP参观群”“后援会”“集体智慧”（P017）：作者比喻性指称的围观群体。",
    "“女二号”“男二号”“群演”（P023）：作者比喻性角色。",
    "“椎心泣血的当众忏悔”（P019）：作者的修辞性描述。",
    "开大巴车的司机把方向盘交给开碰碰车的小朋友（P022）：作者类比。",
    "把金子丢在桌子上 / 把黄金放在桌上（P008、P028）：作者两次使用的类比。",
    "“我以为只有你我知道的信息”（P026）：作者引述的说法。",
    "洋娃娃、男主角（P027）：作者比喻。",
    "“公认一往情深”的剧本（P020）：作者所指的群体共识脚本。"
   ],
   "conditions": [
    "知情范围的条件：除彼此父母可知情外，正常情况下不应有任何不在场的第三方知情（P004）。",
    "例外一：除非当时就有第三人在场，或者彼此明确同意（P025）。",
    "例外二：除非这人是双方父母或者来查案的警察（P026）。",
    "若两人成年，连父母也无权刺探（P030）。",
    "理由一以“自我察觉能力不足、自我控制能力也不够，对权利边界与伦理规范缺少认识”的青少年为前提（P007）；作者也承认“如果人会自觉的警惕和管理也罢了”。",
    "分手情境的推演以“将来不喜欢这些安排了”为前提（P013）。",
    "作者的违约认定以“在明确的提示下，却不遵守客观存在的最基本的禁忌”为条件（P027）。"
   ],
   "rhetoric_and_tone": "对“你们”的第二人称劝告兼训诫体，句式多为设问自答（“为什么要这样？”“你看懂了没有？”）与连续假设推演。大量影视戏剧比喻贯穿全篇：连续剧、编剧、导演、监制、男女主角、女二号与群演、人设崩塌、拆台砸饭碗。夹用英文口号 never tells，结尾短句断然（“恋情不容围观”）。整体语气严正、带有警告与威吓色彩，并明确表示违约将导致关系终止。",
   "unresolved_questions": [
    "question 字段仅为标题“早恋 2”，无独立提问者与提问内容；brief 与正文前段重复、末尾截断于“你们这些早恋的”，不能据此补足正文。",
    "人称关系不明：P024-P027 的“我们/我”似为恋爱中的一方，而《早恋1》中“我们”指父母；两篇是否同一发信人、同一收件人，本文未说明。",
    "“never tells”为英文表述，未注明出处或依据。",
    "“合法监护人或者司法机构以外的人”是否包含学校与教师，未说明。",
    "P019-P020 提出的受害者/罪人两种身份选择，作者未给出自己的裁决。",
    "“你之前做了多久的公共CP主角，你这时就有多深的罪恶”未给出依据，属修辞性表达，理解时需保留其夸张语气。",
    "“高魅力”未在本篇定义（依赖前篇《早恋1》），若单独阅读则含义不完整。",
    "P010 中“整天八卦你们每天的新剧情”的“小姐妹/小兄弟”是否为真实群体，还是作者设想的典型情形，未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "不表演感情。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "就是不要把你们的交往变成一场被围观的连续剧，不要享受旁人的围观", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "除了彼此的父母可以知情，在正常情况下，不应该有任何不在场的第三方知情", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "客观上就会被打上“高魅力”的标签", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "迟早也要引发很多人难以抑制的嫉妒情绪，招来大量的敌意凝视", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "你们的恋情对于ta们来说是一种深刻的损失和遗憾", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "往往会在想明白为什么之前就先不自觉的讨厌、憎恨甚至敌对你", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "在计划好、想明白后果之前就无意识的发起攻击性、破坏性的行动", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "就等于无时无刻不在刺激和推搡还不够成熟的同学和朋友们那还没有被驯服的内心野兽", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "一般人忍不住就要拿，结果你损失了财富而受引诱的人落了罪名", "relation": "context"},
    {"key": "E11", "paragraph_id": "P009", "quote": "不自觉的去扮演别人编剧的男女主角", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "是不是有一群小姐妹/小兄弟在一起整天八卦你们每天的新剧情", "relation": "context"},
    {"key": "E13", "paragraph_id": "P011", "quote": "这些话实际上是在无声的向你们“下单”", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P011", "quote": "转眼就会变成“舔狗”“离了男人活不了”", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P012", "quote": "你等于认可了ta们的编剧、导演、监制职位", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P013", "quote": "你客观上就是在拆导演们的台、砸ta们的饭碗", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "否则你会成为整个群体的公敌、弃民", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P015", "quote": "你之前做了多久的公共CP主角，你这时就有多深的罪恶。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "到底是出于一片真情，还是出于“剧情需要”、“导演要求”", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P017", "quote": "来自“CP参观群”里七嘴八舌的主流意见，来自“后援会”的“集体智慧”", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P018", "quote": "爱你的到底是一个人，还是一个人设？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P018", "quote": "你到底是“被伪装欺骗了太久的受害者”，还是“不知道欣赏和怜惜导致对方无法再爱的罪人”？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P019", "quote": "唯一的补赎就是“椎心泣血的当众忏悔”", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P020", "quote": "怎么反而落下一个“可耻的欺骗”罪？", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P022", "quote": "任由外人围观，最后外人所施加的强烈干预会导致你们所有的出路都被堵死。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P022", "quote": "围观的人的诉求是精彩的剧情，而不是男女主角的良好自我感觉或者美好前途。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P022", "quote": "就像开大巴车的司机把方向盘交给开碰碰车的小朋友一样", "relation": "context"},
    {"key": "E28", "paragraph_id": "P023", "quote": "让女二号和群演们当编剧，男一号和女一号能落下什么好？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P024", "quote": "恋情的第一道德，就是never tells——非必要，不外露。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P025", "quote": "除非当时就有第三人在场，或者我们彼此明确同意", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P026", "quote": "除非这人是你父母、我父母或者来查案的警察。", "relation": "qualifies"},
    {"key": "E32", "paragraph_id": "P027", "quote": "而是会认定你是想当男主角，只是需要我扮演洋娃娃好让你实现梦想", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P027", "quote": "你的“爱”只不过是一种残酷的自私游戏", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P028", "quote": "否则我就是那个把黄金放在桌上，害朋友犯罪的愚妄之人。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P029", "quote": "这一条是无可妥协的", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P030", "quote": "如果你们成年，连父母也无权刺探。", "relation": "qualifies"},
    {"key": "E37", "paragraph_id": "P031", "quote": "恋情不容围观，这是对感情最基本的珍惜。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["恋爱与亲密关系", "青少年同伴群体", "隐私与边界", "家庭教育"],
   "issue_candidates": ["恋情公开与围观", "同伴压力与CP文化", "虚荣与表演", "隐私边界", "分手的群体压力"],
   "text_function_candidates": ["答疑/专栏答复", "规范训诫", "推演说理", "比喻说理"],
   "object_candidates": ["早恋中的两人", "同学与朋友群体", "嗑CP的旁观者", "后援会/参观群", "父母", "恋人（作者自称一方）"],
   "working_keywords": ["不表演感情", "被围观的连续剧", "高魅力", "敌意凝视", "嗑CP", "下单", "人设", "never tells", "合法监护人", "司法机构", "公敌", "珍惜"]
  },
  "notes": "afdian 专栏文；question 字段即标题“早恋 2”，无真实提问者，brief 与正文前段重复且末尾截断。正文 31 段、无图片、无平台话题标签段；lexical 节点计数 34 与正文段数不一致，属空段落被跳过（walk_body 未报 text/lexical 差异）。人称与《早恋1》不同（此篇“我/我们”似为恋人一方），已在 unresolved_questions 登记。"
 },
 "0d4b57f9": {
  "analysis": {
   "question_context": "知乎问答，提问为“如何跟孩子解释「为什么不能说谎」？”。作者不采用道德训诫，而是从安全策略与信用机制解释：说谎会使人成为无效的谈判对象，从而失去“投降”这一最后的保险；随后又承认宏观解释无法事先预防撒谎，补以“不撒谎而解决问题”的游戏式挑战作为动机。标题《小鸡帽》取自正文所举的游戏道具例子。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接给出答案：说谎会让人成为无效的谈判对象，最后失去最后的保险——投降。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "给出前提：人要保持安全最简单的策略是“打不过就躲，躲不过就投降”；只要对方相信你确实投降，消灭你的必要性就消失，合作积极性成为新筹码；但这个“基本解决方案”对说谎的人不存在。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "说明说谎者的处境：打不过、躲不过、投降没人信，只能至死方休；而且很快会意识到自己不会被原谅、被接纳，因为原谅和接纳都建立在信用之上；随时随地都是背水之战，是令人筋疲力尽的人生体验。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "代价比较：这个代价只换到少交一次作业、少挨一次批评、多摸一下小手手，实属亏本买卖。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "让步与缺口：即使这样解释，孩子还是会撒谎，因为慌张焦虑的体验要很久以后才有，而少交作业等好处是当下立即的；宏观解释只能稍稍抬高犯错门槛，无法事先预防，还缺“挑战不撒谎而解决问题的乐趣”。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010", "P011"], "summary": "提出替代动机：把“不撒谎而解决问题”看作有奖的游戏，投入的精力成本因“撒谎在宏观上得不偿失”而成为一种有奖励的自我挑战；不撒谎才有难度、才构成智力挑战、才值得投入游戏时间；撒谎如同开外挂，游戏简单了但游戏本身也废了。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013", "P014"], "summary": "以游戏例证收束：无敌的马里奥、不掉血的春丽、无限命的魂斗罗、show me the money 的星际霸主、戴小鸡帽的 Snake，都是没出息的低级玩家才沉迷的把戏；那是糟蹋游戏而非享受，高玩不会舍得这么浪费。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不能说谎的原因是：说谎会让你成为一个无效的谈判对象，最后失去最后的保险——投降。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人要安全最简单的策略是“打不过就躲，躲不过就投降”；只要对方相信你确实是投降了，消灭你的必要性就直接消失，接下来的合作积极性会成为新筹码。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个“基本解决方案”对说谎的人不存在：打也打不过、躲也躲不过、投降人信不了，只能至死方休。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说谎的人很快会意识到自己不会被原谅、不会被接纳，因为原谅和接纳都建立在一定程度的信用之上。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说谎者随时随地都是背水之战、无时不刻不要破釜沉舟，这种慌张、焦虑、心里没底的状态是令人筋疲力尽的人生体验。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说谎的代价只换到少交一次作业、少挨一次批评、多摸一下小手手，实属亏本买卖。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "即使这样解释，孩子还是会撒谎：因为“慌张焦虑的人生体验”要很久以后才有切身体验，而少交的作业、少挨的批评、多摸到的小手手是当下立即的，所以很难顶得住；这类宏观解释只能稍稍抬高犯错门槛，无法事先预防撒谎尝试。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "还缺一块——挑战“不撒谎而解决问题”的乐趣；不妨把它看作一个有奖的游戏，花在这上面的精力与成本，因“撒谎在宏观上得不偿失”而实际上是一种有奖励的自我挑战。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不撒谎才有难度、才构成智力上的挑战，才值得投入游戏时间，这跟追求“无伤通关”“全成就达成”一样，就是为了好玩。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "撒谎就跟开外挂一样，游戏倒是简单了，但是游戏本身也废了。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无敌的马里奥、不掉血的春丽、无限命的魂斗罗、show me the money 的星际霸主、戴小鸡帽的 Snake，都是没出息的低级玩家才会沉迷的把戏；那不是享受游戏快乐，而是把游戏糟蹋了。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问表达：高玩怎么可能舍得这么浪费（指用作弊方式毁掉游戏乐趣）。", "evidence": ["E22"]}
   ],
   "argument_steps": [
    "直接回答：说谎使人成为无效谈判对象，失去投降这一最后保险（P001）。",
    "前提铺陈：安全的最简策略是打不过就躲、躲不过就投降（P002）。",
    "机制：投降被相信则被消灭的必要性消失，合作积极性成为新筹码（P002）。",
    "转折：该方案对说谎者不存在（P003）。",
    "后果一：无路可退，只能至死方休（P004）。",
    "后果二：不被原谅、不被接纳，因信用缺失（P004）。",
    "后果三：长期处于背水之战式的高焦虑状态（P005）。",
    "成本核算：所得仅少交作业、少挨批评、多摸小手手，属亏本（P006）。",
    "让步：即便如此，孩子仍会撒谎，因收益当下而体验远期（P007）。",
    "承认限度：宏观解释只能稍稍抬高门槛，无法事先预防（P007）。",
    "补充缺口：还缺“挑战不撒谎而解决问题的乐趣”（P008）。",
    "提出方案：把不撒谎解决问题看作有奖的游戏与自我挑战（P009）。",
    "理由：不撒谎才有难度与智力挑战，才值得投入游戏时间（P010）。",
    "类比：撒谎等同开外挂，令游戏失去意义（P011）。",
    "例证：各种无敌/作弊玩法是低级玩家的把戏（P012-P013）。",
    "收尾反问：高玩不会舍得如此浪费（P014）。"
   ],
   "concept_usage": [
    {"term": "投降", "meaning": "一种以可信承诺换取安全的基本策略：对方相信你确实投降，消灭你的必要性即消失。", "evidence": "P001-P002", "ambiguity": "作者将日常/军事用语用于人际与道德解释，未界定适用范围。"},
    {"term": "谈判对象", "meaning": "能与对方交换承诺与条件的主体；说谎会使人失去这一资格。", "evidence": "P001", "ambiguity": "未说明谈判的具体场景与双方。"},
    {"term": "信用", "meaning": "被原谅与被接纳所依赖的基础；说谎者没有可用的信用。", "evidence": "P004", "ambiguity": "未说明信用如何积累或恢复。"},
    {"term": "背水之战 / 破釜沉舟", "meaning": "形容说谎者无退路、必须硬撑的处境（与原典激励士气的用法不同）。", "evidence": "P005", "ambiguity": "作者是反用其义，读者可能误认为褒义。"},
    {"term": "有奖的游戏 / 自我挑战", "meaning": "把“不撒谎而解决问题”视为有奖励的游戏，投入的精力成本因撒谎宏观不划算而成为挑战。", "evidence": "P009-P010", "ambiguity": "奖励的具体内容由读者推断（对标无伤通关、全成就、全金装备）。"},
    {"term": "开外挂", "meaning": "游戏作弊，作者以此类比撒谎：使游戏变简单同时也使游戏失去意义。", "evidence": "P011", "ambiguity": "未讨论例外情形（如游戏本身不公平时是否可用）。"},
    {"term": "高玩", "meaning": "有品味、追求挑战的玩家，作者用以自况并作为劝导者的身份。", "evidence": "P014", "ambiguity": "未给出判定标准。"},
    {"term": "小鸡帽", "meaning": "正文所举“戴小鸡帽的 Snake”一例中的游戏道具/装扮，作为作弊或无难度玩法的例证；标题取自此处。", "evidence": "P012", "ambiguity": "作者未解释该道具的具体效果，属游戏圈典故，需外部核查。"}
   ],
   "examples_and_targets": [
    "少交一次作业、少挨一次批评、多摸一下小手手（P006、P007）：作者设想的孩子撒谎所得，带调侃语气。",
    "无敌的马里奥、不掉血的春丽、无限命的魂斗罗、show me the money的星际霸主、戴小鸡帽的Snake（P012）：作者列举的游戏无敌/作弊状态，作修辞例证。",
    "“无伤通关”“全成就达成”、全金装备（P010）：作者类比的高难度游戏目标。",
    "“打不过就躲，躲不过就投降”（P002）：作者引用的通俗策略，带引号但未注明出处。",
    "被解释的对象“你/孩子”（Q001、P007）：提问者的说明对象，作者全篇以第二人称对其说话。",
    "“本座”（P010）：作者的自称，带角色扮演/调侃色彩。"
   ],
   "conditions": [
    "投降策略的有效性以“只要对方相信你的确是投降了”为前提（P002）。",
    "说谎不划算的论证依赖“原谅和接纳都建立在一定程度的信用之上”（P004）。",
    "作者明说宏观解释只能“稍稍的抬高你犯这个错的门槛”，无法事先预防撒谎尝试（P007）。",
    "论证的落差条件：慌张焦虑的体验要很久以后才有，而撒谎的好处是当下、立即的（P007）。",
    "游戏式动机是建议性表述（“你不妨把……看作”），非强制规范（P009）。",
    "所举作弊玩法均以“游戏”为前提，作者未讨论非游戏情境下说谎是否有例外（P011-P013）。"
   ],
   "rhetoric_and_tone": "以对“你/孩子”说话的口吻作答，但用词高度口语化并夹杂游戏圈俚语，带明显调侃与逗趣（“多摸一下小手手”“有点品味好不啦？”），自称“本座”。反驳方式不用道德训诫，而用成本核算与游戏类比；结尾以“高玩”身份反问收束，语气轻松但带有训导意味。",
   "unresolved_questions": [
    "提问是“如何跟孩子解释”，正文以游戏语言与“本座”自称作答；目标读者究竟是家长还是孩子、是否适合直接对小孩讲，本文未说明。",
    "“戴小鸡帽的Snake”等游戏典故未作解释（应为游戏作品中的道具/装扮），需外部核查后才能确认所指。",
    "“show me the money”等作弊码属游戏圈常识性说法，如需引用为事实待核查。",
    "“打不过就躲，躲不过就投降”未注明出处，是否为作者自拟或引用他人不明。",
    "brief 与正文首段重复，brief 末尾“如果要争取你积极的合”为截断，不能据此补足正文。",
    "未讨论说谎的例外情形（如对恶意者、紧急避险）与不同年龄孩子的理解能力差异。",
    "“信用”如何积累与恢复、说谎者能否重新获得信用，本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "因为说谎会让你成为一个无效的谈判对象，最后你会失去最后的保险——投降。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "打不过就躲，躲不过就投降", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "只要对方相信你的确是投降了，消灭你的必要性就直接消失了", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "接下来你的合作积极性就会成为新筹码", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P003", "quote": "但是这个“基本解决方案”对说谎的人不存在。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "投降人信不了，只能至死方休", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P004", "quote": "因为原谅和接纳都建立在一定程度的信用之上，而自己没这个信用可用", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P005", "quote": "随时随地都是背水之战，无时不刻不要破釜沉舟", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P005", "quote": "是一种令人筋疲力尽的人生体验", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P006", "quote": "这个代价，只换到少交一次作业、少挨一次批评、多摸一下小手手……实属亏本买卖。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P007", "quote": "你还是会撒谎的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P007", "quote": "所以你很难顶得住要犯一下这些错误的", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P007", "quote": "告诉你这些只能稍稍的抬高你犯这个错的门槛", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P008", "quote": "它还缺一块——那就是挑战“不撒谎而解决问题”的乐趣。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P009", "quote": "你不妨把“不撒谎而解决问题”看作一个有奖的游戏", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P009", "quote": "都因为“撒谎在宏观上得不偿失”而实际上是一种有奖励的自我挑战", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P010", "quote": "因为不撒谎才有难度、才构成智力上的挑战，才值得本座投入游戏时间", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P011", "quote": "撒谎就跟开外挂一样，游戏倒是简单了，但是游戏本身也废了。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P012", "quote": "这都是没出息的低级玩家才会沉迷的把戏。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P012", "quote": "无敌的马里奥、不掉血的春丽、无限命的魂斗罗、show me the money的星际霸主、戴小鸡帽的Snake", "relation": "context"},
    {"key": "E21", "paragraph_id": "P013", "quote": "那其实是把这游戏糟蹋了。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P014", "quote": "高玩怎么可能舍得这么浪费？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["儿童教育", "道德教育", "博弈与策略思维", "游戏文化"],
   "issue_candidates": ["说谎的代价", "信用与承诺", "如何向孩子解释道德规范", "以游戏动机替代说教"],
   "text_function_candidates": ["答疑", "解释", "类比说理", "调侃"],
   "object_candidates": ["孩子", "家长/提问者", "游戏角色（马里奥、春丽、Snake）", "说谎者"],
   "working_keywords": ["说谎", "谈判对象", "投降", "信用", "背水之战", "开外挂", "小鸡帽", "高玩", "无伤通关", "本座"]
  },
  "notes": "知乎回答；正文 14 段、无图片、无平台话题标签段。标题《小鸡帽》取自正文 P012“戴小鸡帽的Snake”一例，该道具含义未在文中解释，已登记为待外部核查。brief 与正文首段重复、末尾截断，仅作导航。"
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
