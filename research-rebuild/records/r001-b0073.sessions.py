# -*- coding: utf-8 -*-
"""批次 r001-b0073 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0073.sessions.py            # 写 out/r001-b0073.out.jsonl
  python3 records/r001-b0073.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0073"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0073.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "1143d898": {
  "analysis": {
   "question_context": "提问者（Q001）问：管理者发现下属对自己不满，该如何沟通？提问预设了“应当去沟通”。作者不接受该预设：先论证对方未明确表达时不应主动沟通，再用排除法收窄“不满”的适用情形，最后给出按成本效益处置、并把制度改进与人员处置分开的建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总原则：除非对方明确表达，否则不要随便沟通；因为未表达即不想被知道，去沟通就要交代自己如何得知。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "若答“听别人反映”：等于出卖反映者，被谈者会怀疑所有人、感到被背叛、团队信任受损，反映者与旁观者亦自危。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "若答“自己看出来”：对方可否认，追问就要力证其说谎；若是误会，则显出管理者刚愎多疑，人员将尽走。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"], "summary": "排除三类情形：专业理由反对领导意见、年轻人不知进退、压力大情绪失控，都不算对领导不满。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019"], "summary": "“对我不满”是极严重的定性，不应纵容不安全感滥用；克制这种定性是上位者必修的学分。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "疑心不满时当作真的来评估成本效益：成本不可接受就不动声色（多数随机愤怒会自行消退）；可接受且在改革路线上则借机推进，把个别不满者视为同类人的代表。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "不主动捅破的理由：主动沟通等于授予不满者额外权力，形成“会哭的小孩有糖吃”的示范，伤及不哭的人。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P030", "P031"], "summary": "不满者不享有特权；值得额外帮助的是自担情绪责任、不使情绪成为团队障碍的人，那属于另一话题与另一套原则。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034", "P035"], "summary": "对认为别人亏欠自己情绪者：应届初入职场可宽容观望一两次；二次就业或超过25岁则问责HR筛查，或调岗、差评、给赔偿解雇。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P036", "P037", "P038"], "summary": "制度改进与团队构成改善分开并行；以公交公司处理醉驾司机为类比：既改进辅助驾驶，也要开除醉驾者。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "除非对方明确地表达出来，否则不要随便去沟通。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "未明确表达就意味着对方不想被知道；若称“听别人反映”，等于出卖反映者，被谈者会怀疑所有人、感到被深刻背叛，团队信任与旁观者安全感同时受损。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若称自己看出来，对方可以否认，追问下去就要力证其说谎乃至开除；若本是误会，则暴露管理者刚愎多疑、精神不健康，人员会走光。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出于专业理由反对领导意见、年轻人说话不知进退、压力大或焦虑导致情绪失控，都不构成对领导不满。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“对我不满”是极严重的定性，不应纵容不安全感随意下此定性；克制这种定性是上位者必修的学分，否则无法长期有效领导团队。", "evidence": ["E10", "E11", "E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "疑心不满时不论真假都当作真来处理，先判断有无成本效益划算的方案；成本不可接受就不动声色，很多不满只是随机愤怒、没有长性，大概率会自行消失。", "evidence": ["E13", "E14"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若成本可接受、又处在自己的改革路线上且时间表可提前，就应借机推进改进；把不满者视为千万同类人的代表，可降低人力资源门槛、提高组织的人力资源安全性。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "主动捅破窗户纸等于授予不满者额外权力，造成“越不满越有话语权”的示范，并使不会“哭”的人对团队文化深恶痛绝。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "单纯不满者不应有任何特权，最多只有暂时不予处置的宽容；值得额外帮助的是自担情绪责任的人，那属于另一话题与另一套处理原则。", "evidence": ["E21", "E22"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对流露“别人亏欠我情绪”者：应届初入职场可宽容观望并给一两次机会；第二次工作或超过25岁者应交由HR总监解释筛查并提交改进计划，或以调岗、差评、足额赔偿解雇处理。", "evidence": ["E23", "E24", "E25", "E26"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "系统改进与团队构成改善是两件事，应各归各并行处理；制度上减少出错不替代对失当者的处置。", "evidence": ["E27", "E28"]},
    {"claim_id": "C012", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者设问：管理者发现下属对自己不满，该如何沟通？", "evidence": []}
   ],
   "argument_steps": [
    "立总原则：未明确表达的不满不主动沟通（P001）。",
    "理由一：未表达即不愿被知道，沟通必须交代消息来源（P002）。",
    "推演两条交代路径的后果：说出反映者导致背叛与信任崩塌（P003–P007）；说成自己看出则陷入举证与反噬（P008–P013）。",
    "用排除法收窄“不满”的适用范围（P014–P016）。",
    "给出定性规范：不满属严重定性，应克制（P017–P019）。",
    "转入处置框架：先算成本效益，不可接受则不动，可接受则借势改革（P020–P024）。",
    "补第二个理由：主动沟通会给不满者额外权力并形成坏示范（P025–P029）。",
    "划例外边界：自担情绪责任者属另一话题（P030–P031）。",
    "按工龄/年龄给出分层处置办法（P032–P035）。",
    "结论：制度改进与团队构成改善并行，以醉驾司机类比收束（P036–P038）。"
   ],
   "concept_usage": [
    {"term": "不满", "meaning": "被作者称为“极其严重的定性”，指下属对上级的敌意性态度；文中把专业反对、年轻鲁莽、情绪失控排除在其外。", "evidence": "P014", "ambiguity": "未给正面判定标准，只给排除项与“明确表达”这一门槛"},
    {"term": "成本效益", "meaning": "处置疑似不满时先算方案成本是否可接受，再决定动不动。", "evidence": "P020", "ambiguity": "未说明成本口径与量级"},
    {"term": "会哭的小孩有糖吃", "meaning": "形容主动安抚不满者会被其他人解读为闹情绪者有好处。", "evidence": "P028", "ambiguity": "俗语，作者用作贬义评价"},
    {"term": "捅破窗户纸", "meaning": "指管理者主动挑明自己察觉到对方不满。", "evidence": "P025", "ambiguity": "无"},
    {"term": "人力资源门槛／安全性", "meaning": "指组织可用人选范围的宽窄与关键岗位不缺合适人选的程度。", "evidence": "P023", "ambiguity": "未量化"}
   ],
   "examples_and_targets": [
    "管理者与下属的上下级情境（全篇设定，属作者设定的论证场景）。",
    "“ta上知乎刷到我气得要死，踩我的答案都顾不过来”等四个随机愤怒自行消退的例子（P021，作者例证，带自嘲调侃）。",
    "“全世界只有两个圣人能做，只能跪倒在地恳求圣人看在你穷的份上帮你做事而且少要工资”（P023，夸张修辞）。",
    "HR总监被叫来解释筛查流程、提交降低概率的新计划（P033，机构角色例证）。",
    "公交公司发现醉驾司机（P038，作者类比：既改进无人辅助驾驶与紧急智能干预，又须开除司机）。",
    "被反驳的隐含做法：得知下属不满就主动找其沟通（提问的预设，文中未点名为某具体主张或人物）。"
   ],
   "conditions": [
    "总原则的前提是对方“没有明确地表达出来”（P001–P002）；对方已明确表达时应如何沟通，本文未说明。",
    "处置分岔取决于成本是否可接受（P020），以及是否正处在自己的改革路线上、时间表能否提前（P022）。",
    "分层宽容以“刚出校园、初入职场”为条件、给一两次机会（P032）；第二次工作或超过25岁则转严格处理（P033）。",
    "对自担情绪责任者的额外帮助被明确排除在本文范围外，适用另一套处理原则（P031）。"
   ],
   "rhetoric_and_tone": "连续反问构成压力测试（“你要说你是听别人反映的？”“你接下去要力证ta在说谎吗？”），以极端后果推演作警示；用“格子间里从此一片如坟墓般的死寂”“会哭的小孩有糖吃”“醉驾司机”等比喻；对管理者用训诫与命令口吻（“你要清楚”“记住”“自己掂量”），同时对下属处境作代述式同情（“ta会怀疑所有人”），并夹有自嘲式调侃（“刷到我气得要死”）。",
   "unresolved_questions": [
    "对方确实已明确表达不满时该如何沟通，本文未说明，只论证“未表达则不沟通”。",
    "“成本可以接受／不可接受”的判定标准与量级未说明，读者难以据此操作。",
    "把疑似不满者视为“千千万万这类人的代表”是否适用于所有岗位与规模，未加限定。",
    "P021 举例提到“知乎”“我的答案”，属平台自指，是否影响论证未说明。",
    "本篇 lexical 记录 paragraph 节点 40 个，而正文切分出 38 段（P001–P038），差额疑为空段落节点，需复核是否有未渲染内容。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "除非对方明确地表达出来了，否则不要随便沟通。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "因为既然对方没有明确的表达出来，自然就是不想你知道。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "ta会怀疑所有人，感到受到了深刻的背叛", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "我们之中有第三只眼，我们所说的随时会成为对我们不利的呈堂证供", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "你接下去要力证ta在说谎吗？摆事实讲道理必须证明对方就是不满然后不认账？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "而是你这老大似乎精神不太健康，还是提前躲开以免哪天溅一身的问题了", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "讨论问题对方出于专业理由反对领导意见——哪怕事后证明是ta搞错了——这不算对你不满。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P015", "quote": "年轻人说话没有轻重，不知进退上下，这也并不见得是对你不满", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "压力很大，焦虑程度很高，无法控制自己的情绪，这也不算对你不满。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "“对我不满”是一个极其严重的定性", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "极尽可能不要随便给人定性为“不满”“有敌意”是身为上位者必须要修到的学分。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "否则你是不可能长期有效地领导你的团队的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "当你疑心有某种不满，那么真的或者假的都没所谓，就当它是真的来思考你有没有什么成本效益划算的方案可以解决这类问题。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "很多“不满”其实只是愤怒的青春挤出来的随机愤怒，没有长性。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "那么让你看到这些迹象就是上帝给你的“把这事先办”的预兆，你可以办起来。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "不要把这个不满的人看作一个人，而要看做千千万万这类人的代表。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "你做得越好，你的组织的人力资源安全性就越高", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "因为那样的话，你等于授予了不满者额外的权力。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "你以为这是“宽厚”，在其他人眼里这叫“会哭的小孩有糖吃”。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P029", "quote": "不会“哭”的那部分人会对你的团队文化深恶痛绝。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P030", "quote": "单纯不满者没有也不允许有任何一丝一毫的特权", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P031", "quote": "只有知道不满是自己的责任、挣扎着付出艰难的努力去管理自己的情绪", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P032", "quote": "如果是刚出校园、初入职场，那么可以宽容观望，给一两次机会。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P033", "quote": "如果是第二次工作，或者超过了25岁，就把HR总监叫来让ta解释这样的人是怎么通过筛查的", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P034", "quote": "按下差评，给ta一个干净的新起点。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P035", "quote": "或者直接发足赔偿金，解除雇佣关系。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P037", "quote": "但系统改进归系统改进，改善团队构成归改善团队构成。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P038", "quote": "一边要改进无人辅助驾驶和紧急智能干预，使得就算有人喝醉了也不容易出错误，另一面却很有必要开除掉这个醉驾司机一样。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理", "职场关系", "人力资源管理"],
   "issue_candidates": ["上下级沟通", "下属不满的识别与定性", "情绪责任边界", "HR筛查与解雇处置"],
   "text_function_candidates": ["答疑", "建议", "论辩"],
   "object_candidates": ["管理者", "下属", "HR总监", "团队", "知乎"],
   "working_keywords": ["不满", "定性", "成本效益", "会哭的小孩有糖吃", "捅破窗户纸", "醉驾司机"]
  },
  "notes": "无图片节点，正文完整可读，按默认 status=read 处理。lexical 段落计数(40)与正文段落数(38)不一致，差额疑为空段落节点，已登记待复核。updated_at(2025-01-22) 晚于 published_at(2020-09-21)，平台侧可能修订过正文，版本差异无法从本记录判断。"
 },
 "4c4d69f2": {
  "analysis": {
   "question_context": "提问者（Q001）问：该怎么拒绝自己不喜欢的好男生，把伤害降到最低？作者给出的是一套信息边界与冷却操作的清单：先封锁日程、关注事务、人际关系与人生理想四类信息，说明泄露即等于授予追求许可；再针对“恶性关系”给出慢回应与请父母出面直接反对两种做法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "四条操作建议：屏蔽日程安排、避免对方了解你关注的事务、不讨论自己的人际关系、不谈人生理想。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006"], "summary": "限定说明：封锁这些信息不妨碍谈天文地理政治人文科学艺术，且属成年人常态，陌生人知道这些信息极不正常。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P007"], "summary": "提出“无知迷雾是最好的防护”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "主动透露即等于许可对方进一步尝试；知道你空闲时间的人在客观上就拥有追求许可，事后声明“我没这个意思”无意义。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013"], "summary": "转入针对恶性关系的做法：控制查看与回复的热度，回复不超过礼貌标准回复范围；激烈对抗反招致长期跟踪。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "第二个办法：与父母谈困扰，由父母出面直接向对方表示反对；不成熟者难面对家长强烈明确的反对，尤其当你不站在对方一边时，对方也无法再自称“出于爱”。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "补充说明：此举可能使对方移恨父母，但分摊了集中在你身上的恨意；父母并非当然有此义务，但许多父母愿意挡在前面且比想象中强大。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "拒绝不喜欢的人时应屏蔽自己的日程安排，避免对方了解自己关注的事务，不与之讨论自己的人际关系与人生理想。", "evidence": ["E1", "E2", "E3", "E4"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "封锁这些信息不妨碍双方谈天文地理政治人文科学艺术；这类保留是成年人之间的常态，陌生人知道这些信息才是极端不正常的。", "evidence": ["E5", "E6"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无知迷雾是最好的防护。", "evidence": ["E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "主动向对方透露这些信息等于许可其作进一步尝试；知道你何时空闲可以约吃饭的人在客观上就已拥有追求许可，而“客观上”意味着事后说“我没这个意思”没有意义。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若要让一段关系直接冷却，就不要飞快查看与情绪激动地回复，回复不超出“礼貌标准回复”的范围；因为无人能对总是隔天礼貌回复者长期保持兴趣，而激烈对抗者反而被长期跟踪关注。", "evidence": ["E11", "E12"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "另一个办法是与父母谈论困扰，由父母出面直接打给对方表示反对该关系；不成熟的人往往难以面对对方家长强烈而明确的反对，尤其在你自己没有坚定站在对方一边时。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母已经明确反对而对方自己也没站在你这边时，对方若继续强行坚持，至少不能再自称是“出于爱”，无法再自我正义化。", "evidence": ["E16"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这种做法可能导致对方移恨你的父母，但至少分摊了集中在你一个人身上的恨意。", "evidence": ["E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "父母分担这种仇恨并非其当然义务，但在很多情况下父母是愿意的；若有机会选择，相当部分父母会挡在子女前面，而且比子女想象的强大很多。", "evidence": ["E18", "E19"]},
    {"claim_id": "C010", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者设问：该怎么拒绝自己不喜欢的好男生，并把伤害降到最低？", "evidence": []}
   ],
   "argument_steps": [
    "先给四条信息边界建议（P001–P004）。",
    "限定这些建议不影响正常话题往来，并给出成年人常态的判断（P005–P006）。",
    "提出“无知迷雾是最好的防护”作为概括（P007）。",
    "说明理由：透露信息即授予追求许可，且“客观上”优先于事后的口头否认（P008–P011）。",
    "转入对恶性关系的处置：以慢回应降温（P012–P013）。",
    "给出第二办法：父母出面直接反对，并推演对方的处境（P014–P016）。",
    "承认副作用（移恨父母）但给出分摊恨意的收益（P017）。",
    "以父母并非当然有义务、但愿意且有力量作结（P018–P019）。"
   ],
   "concept_usage": [
    {"term": "无知迷雾", "meaning": "指对追求者封闭日程、关注事务、人际关系与人生理想等信息，使对方无从下手。", "evidence": "P007", "ambiguity": "隐喻式表述，未说明信息封边界限"},
    {"term": "客观上拥有你的追求许可", "meaning": "只要对方掌握了可约你吃饭的时间等信息，就事实上获得了进一步追求的许可，与你的主观声明无关。", "evidence": "P009", "ambiguity": "作者强调“客观上”，但未讨论信息被第三方转告等情形"},
    {"term": "礼貌标准回复", "meaning": "冷却关系时不超出礼貌范围的回复方式，用于使对方失去持续兴趣。", "evidence": "P013", "ambiguity": "未给出具体标准与频率"},
    {"term": "恶性关系", "meaning": "P012 之后建议的适用对象，用以区别一般的不喜欢。", "evidence": "P012", "ambiguity": "未界定何种关系算恶性关系"},
    {"term": "自我正义化（justify）", "meaning": "对方用以把自己的坚持解释为“出于爱”的自我辩护。", "evidence": "P016", "ambiguity": "无"},
    {"term": "父母的当然义务", "meaning": "作者强调父母出面分担仇恨并非其应尽义务。", "evidence": "P018", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "“好男生”追求者（提问设定的对象）。",
    "父母出面对话的场景，含作者拟出的台词“我们看得到ta很受困扰，我们不希望这样的状况继续下去”（P015，属作者给出的示例话术，不是真实引文）。",
    "想约吃饭的追求者（P009，用作说明“客观许可”的例子）。",
    "激烈对抗导致长期跟踪关注的对象（P013，作者举例说明反向效应）。",
    "被反驳或修正的隐含做法：把拒绝理解为一次性表态／靠言语声明“我没这个意思”即可（P008、P011 中被作者否定的思路）。"
   ],
   "conditions": [
    "P012 明确限定后半部分建议“是针对恶性关系的”，不能自动套用于所有拒绝情形（P012）。",
    "父母出面办法以对方“不成熟”、以及你自己没有坚定站在对方那一边为前提（P015）。",
    "父母分担仇恨被限定为并非其当然义务，只是很多时候愿意（P018）。",
    "全文以异性追求场景为背景，未讨论职场、权力不对等等其他关系形态。"
   ],
   "rhetoric_and_tone": "以“第一……第四”的条目式祈使句给出操作清单，语气冷静、工具化；用引号反复强调“客观上”以点出题眼；拟出父母台词作为可直接套用的话术；末两段转为抒情式肯定（“ta们会宁肯去恨自己，而少恨一点你”），带轻微的温情与安抚。",
   "unresolved_questions": [
    "提问对象是“不喜欢的好男生”，而作者第二部分明确只针对恶性关系；两部分与提问对象的对应关系未说明。",
    "“礼貌标准回复”的具体频率与内容标准未给出，操作性有限。",
    "让父母出面可能引发的报复、家庭冲突与法律后果未讨论。",
    "若父母不愿或不能出面，未给出替代方案。",
    "未说明“不喜欢的好男生”若并不属于恶性关系时，应如何把伤害降到最低。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "第一，对对方屏蔽你的日程安排。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "第二，避免对方了解你现在关注的事务。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "第三，不和对方讨论自己的人际关系。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "第四，不要谈论自己的人生理想。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这不会妨碍你们谈天文地理政治人文科学艺术。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "其实这是成年人之间的常态，陌生人知道这些信息是极端不正常的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "无知迷雾是最好的防护。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "如果你兴高采烈向人透露这些信息，就等于在许可对方做进一步的尝试。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "每一个知道你什么时候空闲可以约吃饭的人，都在客观上拥有你的追求许可。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "“客观上”的意思是——说“我没这个意思”没有意义。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "回复也不要超出“礼貌标准回复”的范围", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "没人能对总是隔天才回复简单礼貌回答的人长期保持兴趣。但是人往往能对激烈对抗的人长期跟踪关注。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "第二个办法，是跟父母谈论这个困扰。由父母出面直接打给对方，表示自己反对这个关系。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "不成熟的人往往很难面对对方家长的强烈而明确的反对。尤其是你自己又没坚定站在ta那边。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "我们看得到ta很受困扰，我们不希望这样的状况继续下去", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "如果继续强行坚持，至少不能再自称自己是“出于爱”了", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "但这至少分摊了集中在你一个人身上的恨意。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "这并非父母的当然义务", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "而且ta们比你想象的强大很多。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系", "情感交往", "沟通策略"],
   "issue_candidates": ["拒绝追求者", "降低拒绝伤害", "个人信息边界", "父母代为出面"],
   "text_function_candidates": ["答疑", "建议", "操作清单"],
   "object_candidates": ["提问者（被追求者）", "好男生／追求者", "父母", "恶性关系对象"],
   "working_keywords": ["无知迷雾", "追求许可", "客观上", "礼貌标准回复", "自我正义化", "恶性关系"]
  },
  "notes": "无图片节点，正文完整可读，按默认 status=read 处理。lexical 段落计数(19)与正文段落数(19)一致。P012 明确把后半部分限定为“针对恶性关系”，提问所指的“好男生”与恶性关系的对应关系需研究者复核。updated_at(2021-05-23) 晚于 published_at(2020-09-22)。"
 },
 "716cfc56": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么有的男生喜欢在女性面前开黄色玩笑？作者没有直接给心理动机清单，而是把它归入一种更大的社交策略：用“冒犯被容忍的程度”试探关系可靠度（老手会以利益输出作对冲），先复述该策略的内在逻辑，再逐一指出其三个致命缺陷，最后以“义不受辱”“非以利相结的义士”论定其对做大事者的排除效果。文末标注“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出主题：用冒犯被容忍的程度试探关系可靠度；老手会辅以真金白银的利益输出作平衡对冲；该策略远超“对女生讲黄段子”，还包括灌酒、调侃、恶作剧、取外号、借钱不还、有意冤枉等。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "复述该策略的总逻辑（受不起侮辱者终将闹翻，只有受得起小侮辱者才值得长期关系），并承认它看上去确有一定合理性且有效案例很多。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "限定讨论范围：排除只学会冒犯试探一半的无意识模仿者，只讨论明白全部做法并积极实施者。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012"], "summary": "缺陷一：严重依赖试探者的利益输送能力；忍受侮辱是交易定金／投名状，利益不到位则轻则被贴“不懂事”打入另册，重则被报复求偿；为免成为众人的“测试对象”必须痛击，故放逐已是仁慈；试探者须有实力兜底。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017"], "summary": "该逻辑的另一面：被试探方因对方押上受罚风险而反成主动方；对称冒犯的变种可形成双向投名状与有限信任。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "缺陷二：不可靠。关系抗压能力受投名状大小约束，尺度微妙易误判，机制复杂如破解密码，许多人已在此阶段折戟。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027"], "summary": "缺陷三（最大）：不能兼容真正的能人义士。能人本钱足可恃才傲物，惯用侮辱试探者对其反而礼敬有加；用侮辱测试本身即已排除对你能力稀缺性的认可，真正的侮辱在于对方作出“你没有不可替代价值”的判断。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032"], "summary": "给出义士定义（取中性义）：有原则理想信仰、可舍身取义者；其负重受损不用于交换、不计债、不转立场；只有这样的人能攻坚克难。", "role": "definition"},
    {"unit_id": "U009", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040"], "summary": "要害岗位掌握你的生死存亡，任何重赏都保证不了唯利是图者不反噬；能被收买或为现实利益忍受侮辱者不可委以重任，故这些地方非义士不可。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045"], "summary": "结论一：义不受辱；普遍以侮辱测试作为构建关系的先导手段，等于放弃成就大事业的基本资格，将缺少义士辅佐而不敢托付要事。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051"], "summary": "结论二：真正成就过事业的人正以这个标准评价你——惯用黄色笑话、侮辱性外号不是“会来事”，而是“不能做任何重要的事”；文末标示未完待续。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "存在一种流行做法：用冒犯被容忍的程度试探关系的可靠度；对懂这套策略的老手而言，试探后常辅以真金白银的利益输出作为平衡对冲。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "该策略的总逻辑是：不能接受侮辱的人迟早会因长期关系中的负面体验闹翻，因此只有被证实受得起显而易见的小侮辱、小委屈的人才值得考虑长期关系。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这个逻辑看上去确有相当合理性，且因有效案例足够多而流传广、渗透深。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论范围只限明白全部做法并积极实施者；只学会冒犯试探这一半、没有利益输送另一半的无意识模仿者被排除在外，其结果是陷自己于社交绝境。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "缺陷一：该策略严重依赖试探者的利益输送能力，配合者把忍受侮辱的代价当作交易定金与投名状；后续利益不到位时，轻则被贴“不懂事”打入另册，重则被视为可合法求偿报复的对象。", "evidence": ["E6", "E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为免自己成为众人眼中的“测试对象”，试探者必须痛击失约者，因此放逐已属仁慈；伸手试探者须有足够实力兜底，否则如同插标卖首、送肉上门。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "在该逻辑统治的文化圈内，被冒犯试探反被视为受欢迎的合作邀请，受试探的一方反而是主动方；对称冒犯的变种可形成双向投名状与默契，进而产生一定强度的信赖与合作。", "evidence": ["E12", "E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "缺陷二：这种策略不可靠——靠双向投名状建立的关系其抗压能力受投名状大小约束，尺度微妙易误判，机制复杂如破解密码，且不知多少人已在此阶段折戟沉沙。", "evidence": ["E16", "E17", "E18", "E19"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "缺陷三也是最大缺陷：该策略不能兼容真正的能人义士——能人有足够本钱恃才傲物，反要试探者交投名状；惯用侮辱试探者对软硬不吃的能人却礼敬有加。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用侮辱测试本身就意味着已排除对你能力稀缺性的认可；话语的侮辱性次要，对方作出的“你没有不易替代价值”的判断才是真正的侮辱，接球即接受了该判断。", "evidence": ["E23", "E24"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "义士指确有一些原则、理想、信仰，乃至威武不能屈、富贵不能淫、贫贱不能移、能舍身取义的人；作者明确只取中性义，不先问其义是否被主流价值观认可。", "evidence": ["E25", "E26"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "义士为原则和理想负重、受损，不会拿去交换，不因尽义计算谁欠债，也不因吃亏委屈转变立场；只有这样的人才能攻坚克难，做大事业必须有非以利相结的义士。", "evidence": ["E27", "E29"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要害岗位上的人事实上掌握你的生死存亡，任何丰厚贿赂都无法保证唯利是图者不反噬；可被收买或为现实利益忍受侮辱的人不能被委以此类责任。", "evidence": ["E28", "E30"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "义不受辱；普遍把“侮辱测试”当作构建关系的先导手段，等于放弃成就大事业的基本资格——将缺少义士辅佐，对真实威胁的事不敢托付。", "evidence": ["E31", "E32", "E33"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正成就过事业、知道事情怎么做成的人在用这个标准看待你：拿黄色笑话撩妹、以侮辱性外号套近乎成习惯成风格，绝不是“会来事”的好评价，而是“不能做任何重要的事”。", "evidence": ["E34", "E35"]},
    {"claim_id": "C016", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者设问：为什么有的男生喜欢在女性面前开黄色玩笑？", "evidence": []}
   ],
   "argument_steps": [
    "把提问现象重新描述为“用冒犯试探关系可靠度”的策略，并加上利益输出的一半（P001–P002）。",
    "复述该策略的内在逻辑，并承认其表面合理性（P003–P004）。",
    "限定讨论对象，排除只学一半的模仿者（P005–P006）。",
    "展开缺陷一：依赖利益输送能力、投名状与报复机制（P007–P012）。",
    "补述该逻辑下受试探方的实际位置与对称冒犯变种（P013–P017）。",
    "展开缺陷二：不可靠与误判（P018–P021）。",
    "展开缺陷三：不兼容能人义士，并指出真正的侮辱在于对方的判断（P022–P027）。",
    "定义义士（中性义）及其行为特征（P028–P032）。",
    "论证要害岗位非义士不可，重赏无法替代（P033–P040）。",
    "由“义不受辱”推出：普遍使用侮辱测试者放弃做大事业的基本资格（P041–P045）。",
    "以“真正成事者如何看你”收束，并标未完待续（P046–P051）。"
   ],
   "concept_usage": [
    {"term": "冒犯试探／侮辱测试", "meaning": "以对方能否容忍冒犯来判断关系可靠度与合作价值的做法，本文主要反驳对象。", "evidence": "P003", "ambiguity": "作者在复述他人逻辑与自己的批评之间切换，需按段落区分归属"},
    {"term": "投名状／定金", "meaning": "把忍受侮辱的代价当作建立合作关系的抵押物。", "evidence": "P007", "ambiguity": "借用江湖用语，未给严格定义"},
    {"term": "不懂事", "meaning": "试探者对被判为不守这套伦理者的标签，意味着打入另册乃至可被报复。", "evidence": "P009", "ambiguity": "无"},
    {"term": "能人", "meaning": "有足够本钱恃才傲物、不需靠受辱换取机会的人。", "evidence": "P023", "ambiguity": "未给出判定稀缺性的标准"},
    {"term": "义士", "meaning": "确实有原则、理想、信仰，可为原则理想受损乃至牺牲的人；本文明确只取中性义。", "evidence": "P029", "ambiguity": "中性义的“义”以何为判准未说明"},
    {"term": "义不受辱", "meaning": "义士不会以忍受侮辱为代价换取利益，故侮辱测试无法与之兼容。", "evidence": "P041", "ambiguity": "无"},
    {"term": "板刀面", "meaning": "比喻被托付者反噬谋害托付者，用以说明重赏不能保证安全。", "evidence": "P034", "ambiguity": "典故出处未点名，需外部核查"},
    {"term": "会来事", "meaning": "社会上对惯用黄色笑话、侮辱性外号者的常见好评，作者明确否定这种评价。", "evidence": "P048", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "酒桌灌酒、当众调侃、恶作剧、取外号、借钱不还、有意冤枉（P002，作者列举的同一策略的表现）。",
    "黄色笑话与强行劝酒（P025、P048，作者点名的具体做法）。",
    "山贼交投名状（P008，比喻）。",
    "划到江心请吃板刀面、借高利贷（P034–P039，水浒式比喻与修辞材料，作者未点名出处）。",
    "“强哥”（P039，作者假设读者自比的人物，所指未说明，需外部核查）。",
    "“威武不能屈、富贵不能淫、贫贱不能移”、舍身取义（P029，典故化表述，未点名出处）。",
    "能人、义士（P022–P031，作者的分析对象与理想类型）。",
    "被反驳对象：以侮辱试探筛选合作者、并把这套做法当作进身之道的使用者群体（未指名个体或文献）。"
   ],
   "conditions": [
    "讨论范围以“明白全部做法并在积极实施”者为限（P006）。",
    "策略有效性依赖试探者的利益输送能力（P007）；关系抗压能力受投名状大小约束（P019）。",
    "义士的定义只取中性义，作者明确把“其义是否被主流价值观认可”先搁置（P030）。",
    "结尾判断针对的是“普遍应用侮辱测试为先导手段”的情形（P042）。",
    "文末标注“（未完，待续）”，本篇尚未完成（P051）。"
   ],
   "rhetoric_and_tone": "冷峻的分析口吻与江湖黑话式比喻并用（投名状、插标卖首、送肉上门、板刀面、强哥）；以“首先”“第二个”“第三个，也是最大的缺陷”分层推进；多用反讽递进（“讽刺的是”“更讽刺的是”）与连续反问（“看明白没有？”“就是把你搓成粉又能包几个汤圆？”）；对读者最终转为直接警告（“自己掂量着办吧”）；文末“（未完，待续）”提示文本未完成。",
   "unresolved_questions": [
    "文末标注“（未完，待续）”，本篇未完成，后续内容缺失，结论是否还有下文不得而知。",
    "“强哥”所指人物未说明，需外部核查。",
    "“板刀面”等典故出处未点名（是否为《水浒传》浔阳江一节需外部核查）。",
    "“这个策略在中国蔓延之广、渗透之深”为程度判断，缺少数据与范围界定，待外部核查。",
    "“义士”的中性义以何为判准、如何识别，本文未给出可操作标准。",
    "lexical 段落计数(55)与正文段落数(51)不一致，差额疑为空段落节点，需复核是否有未渲染内容。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人喜欢用冒犯被容忍的程度来试探关系的可靠度。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "对真正懂得这个策略的老手而言，这种试探常随后辅以真金白银的利益输出作为平衡对冲。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "不能接受侮辱的，必然会因为长期关系中迟早会发生的或有意或无意的负面体验而闹翻", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这个逻辑本身不是没有一定合理性的——至少看上去的确如此。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "大部分这么做的蠢人都只学会了冒犯试探这一半，没有意识到还有利益输送的另一半", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "首先，它严重的依赖于试探者的利益输送能力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "配合你这个伦理的人实际上是在把忍受侮辱的代价作为一份交易定金，一份投名状。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "如果你让我失望，我对你最仁慈的处置也是给你贴上“不懂事”的标签把你打入另册。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "我不让你受到足够教训，别人看在眼里，我将成为不知多少人的“测试对象”。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "所以你有必要被痛击——也因此只是放逐你的确是一种仁慈。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "你要伸手试人，你最好手里有足够的实力为你的试探兜底，否则你就犹如插标卖首、送肉上门。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "因为那意味着对方在以受惩罚的风险做抵押，准备和你建立对你承诺了利益输出的合作邀请", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "受试探的一方反而是主动方。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "就是你冒犯我一点，我还以另一种对称的冒犯，我接受你的冒犯，你也接受我的冒犯。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "接下去我们就可以在一定强度内信赖我们的关系了，也就可以有一定的合作了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "它还有第二种风险——它不可靠。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "这种靠双向交投名状而建立起来的关系，其抗压能力自然受到投名状大小的约束。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "什么样的试探对应什么样的信号，什么样的关系能承受什么样的考验，这个机制之复杂，不亚于破解密码。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "也不知道有多少人在这个阶段就已经折戟沉沙了。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "第三个，也是最大的缺陷，是这个策略不能兼容真正的能人义士。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "能人有足够的本钱，足以“恃才傲物”。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "在这些软硬不吃的能人面前完全是另一副样子，规规矩矩、礼敬有加，唯恐对方误以为不够恭敬。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P026", "quote": "正是觉得你没有什么不易替代的价值，所以ta才选择走第二条路与你建立关系。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "ta的话本身的侮辱性是次要的，ta做出的这个判断才是真正的侮辱所在。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P029", "quote": "义士就是一些确实有原则、有理想、有信仰", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P030", "quote": "我们不取褒义，只取中性义", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P031", "quote": "这种人为自己的原则和理想负重、受损，是不会拿来跟人换什么东西的", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P034", "quote": "手一歪就能决定你的生死存亡的人，该拿什么“重赏”来保证对方不这么做？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "所以要做大事必须有非以利相结的义士不可。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "如果一个人是可以被收买的、可以看在一点现实利益的份上忍受侮辱，这人就不能被委以这样的责任。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P041", "quote": "而义不受辱。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P042", "quote": "你如果普遍应用“侮辱测试”为构建关系的先导手段，就等于已经放弃了真正成就什么大事业的基本资格。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P043", "quote": "你必定缺少义士辅佐，于是一切对你有真实威胁的事你根本不敢托付与人。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P048", "quote": "一个人拿黄色笑话撩妹、用侮辱性外号跟人套近乎已成习惯、已成风格，绝不是什么“会来事”之类的好评价。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P049", "quote": "“不是不能用来跑腿打杂，但是不能做任何重要的事。”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会交往伦理", "组织用人", "文化批评"],
   "issue_candidates": ["冒犯试探与关系筛选", "投名状式交换关系", "侮辱测试与用人风险", "能人与义士"],
   "text_function_candidates": ["答疑", "论辩", "批评"],
   "object_candidates": ["策略使用者群体（未具名）", "受试探者", "能人", "义士", "强哥（所指未明）"],
   "working_keywords": ["冒犯试探", "投名状", "不懂事", "义不受辱", "板刀面", "恃才傲物", "重赏之下必有勇夫", "会来事"]
  },
  "notes": "无图片节点，正文可读；但文末 P051 标注“（未完，待续）”，属未完成文本，后续内容缺失，故本篇判断均以已刊出部分为限。本篇 opponent 指文中未具名的策略使用者群体，不是特定个人或文献。lexical 段落计数(55)与正文段落数(51)不一致，差额疑为空段落节点，待复核。updated_at(2025-02-27) 晚于 published_at(2020-09-22)。"
 },
 "7eee6fed": {
  "analysis": {
   "question_context": "提问者（Q001）问：与别人讨论时，如何发现对方在偷换概念？作者先立起“很多人”的判定逻辑作为靶子（自己先有默认理解→发现他人理解不同→即认定对方偷换概念），指出其实质是自认理解即终极正确；随后给出严格的成立条件（须违背对方自己所作／认可的定义），并把这种糊涂判定归因于应试教育下形成的“教科书定义为准”的思维惯性，最后转为对社会后果的警告。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "立靶：很多人判定“偷换概念”的三步逻辑，其实是确信自己的理解即宇宙真理、顺之者正确逆之者错误。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P006"], "summary": "该思路的更强版本：只要对方推出的结论令其不满而论证找不到破绽，就逆推对方一定偷换了概念。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "给出成立条件：必须先有对方的独立定义且其后论证违背其自己所作／认可的定义；违背“你的”定义且你未明确接受，不构成逻辑问题。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P010"], "summary": "反问式补刀：按同一伦理，你自己一开始也违背了对方心中默许的定义。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013"], "summary": "归因：这种糊涂判定是被考试害的——学生因违背教科书定义被判偷换概念，教学双方默认“教科书定义为准”而跳过共识环节。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"], "summary": "让步：对学校教育（至少中国学校教育）无可厚非——高考只有评卷组一种定义，参加统一考试即接受该考核标准，故一概以大纲教材为准。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019"], "summary": "转折：学生出校后仍假定别人在参加自己任首席权威的“私家高考”；长期做受评价者会延续这种默认伦理，直到自己创业担责才意识到教科书不是终极标准。", "role": "transition"},
    {"unit_id": "U008", "paragraph_refs": ["P020", "P021"], "summary": "两个反驳：若教科书定义即终极真理，为何有大量失败的博士；人类思想史本就是不断重新界定概念的过程，按此判罪法大师们首先该被处决。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P022", "P023", "P024"], "summary": "定性：信奉高考阅卷式偷换概念观，对己是自甘为奴，对人是禁止他人不为奴；即便以“爱国”立场为之也阻碍国家进步，因为进步本身即是概念的更新。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P025", "P026"], "summary": "结论：只有违背自己声明的定义才构成偷换概念；任何人都有天然不可剥夺的权利阐述自己的定义，这种不可剥夺还包括贯彻蠢行的社群将自取灭亡。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031"], "summary": "警告与预判：这种思路在社会上一显露就必然倒霉；网上共鸣者给的自信不足恃；并预判仍会有人说本文“偷换偷换概念的概念”，作者以 Poetic irony 收尾。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "许多人对“偷换概念”的判定逻辑是：自己先有默认理解，发现他人理解与自己不一致，即认定对方偷换概念；其实质是确信自己的理解即宇宙真理、终极正确。", "evidence": ["E1", "E2", "E3", "E4", "E5"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "该思路的更强版本是：只要对方基于该概念推出的结论令其不满、而论证过程找不到破绽，就必然可以逆推“对方一定是偷换了概念”。", "evidence": ["E6"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "偷换概念必须成立的条件是：对方先对某概念作了独立定义，而在其后论证中又违背了自己所作／认可的定义。", "evidence": ["E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "若双方事先就某概念达成共识（如约定以某版本文献的约定为标准定义），发现对方违背该定义可以算作偷换概念；但其本质仍是对方违反了自己所作的声明。", "evidence": ["E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在对方没有明确接受的前提下违背“你的”定义，不构成任何意义上的逻辑问题；按同一伦理，你自己一开始也违背了对方心中默许的概念定义。", "evidence": ["E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种糊涂判定是被考试害的：学生学逻辑时因违背教科书定义被判偷换概念；这对学校教育（至少中国学校教育）无可厚非，因为高考只有一种定义即评卷组的定义，参加统一高考即接受该考核标准，故一概以大纲教材为准。", "evidence": ["E12", "E13", "E14", "E15", "E16"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题是学生出校后仍想当然假定别人在参加自己任阅卷组首席权威的“私家高考”；长期作为受评价者、生活在别人划定的定义范围内，会一直延续这种默认伦理。", "evidence": ["E17", "E18"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：如果教科书的定义就是终极而完全的真理，为何还有满坑满谷一败涂地的博士？", "evidence": ["E19"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类的整个思想史都是不断重新界定概念的过程；按这种判罪法，他们所崇拜的大师们首先就该被处决。", "evidence": ["E20", "E21"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "信奉高考阅卷式的偷换概念观——不允许任何人重定义或更精细地定义“主流解释”，并一概加上偷换概念的罪——加之于己是在追求真理上自甘为奴，加之于他人是不许他人不与自己一同为奴；即便自认为出于“爱国”立场，也是在阻碍国家自己的进步，因为进步本身即是概念的更新。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有违背自己声明的定义才构成偷换概念；任何人都有天然不可剥夺的权利在自己的论述中阐述自己的定义，这种“不可剥夺”还包括贯彻这种蠢行的社群必将落后挨打乃至自取灭亡。", "evidence": ["E25", "E26"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这种“与我／我所崇拜的文献／伟人理解不同即偷换概念”的思路在社会上一旦显露出来，倒霉是肯定的；对有名有姓的成熟独立者如此指责，还是早点开始找工作。", "evidence": ["E27", "E28"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预判：即使把话说透，仍会有人说这篇东西是在“偷换偷换概念的概念”，并称之为 Poetic irony。", "evidence": ["E29", "E30"]},
    {"claim_id": "C014", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者设问：与别人讨论时，如何发现对方在偷换概念？", "evidence": []}
   ],
   "argument_steps": [
    "先复述“很多人”的三步判定逻辑并点明其实质（P001–P005）。",
    "补出其更强版本（P006）。",
    "给出真正成立条件：须违背对方自己所作／认可的定义（P007）。",
    "区分有共识与无明确接受两种情形（P008–P009）。",
    "反问式指出对方同样可以指控你违背其默许定义（P010）。",
    "归因于应试教育：教科书定义为准的惯性（P011–P013）。",
    "让步：校内／高考场域这样做无可厚非（P014–P016）。",
    "转折：出校后仍假定他人参加自己的“私家高考”（P017–P019）。",
    "用博士失败与思想史两个反驳拆解教科书权威（P020–P021）。",
    "把该思路定性为对己对人之奴役，并指出其阻碍进步（P022–P024）。",
    "给出正面结论：定义权不可剥夺（P025–P026）。",
    "以社会后果警告与对反驳的预判收尾（P027–P031）。"
   ],
   "concept_usage": [
    {"term": "偷换概念", "meaning": "本文严格含义：对方先对概念作了独立定义，其后论证又违背该定义；不包括“与我的理解不同”。", "evidence": "P007", "ambiguity": "与日常用法（理解不同即偷换）正相反，作者对此有明确交代"},
    {"term": "定义／共识", "meaning": "需要有对方的独立声明或双方事先明确约定，违背才可成立。", "evidence": "P008", "ambiguity": "默示接受、部分接受是否算作接受未说明"},
    {"term": "私家高考", "meaning": "比喻把他人当作自己任阅卷组首席权威的考试对象、以教科书答案判分的心态。", "evidence": "P017", "ambiguity": "比喻性表述"},
    {"term": "教科书定义", "meaning": "学校场域内的唯一标准；作者认为在校内以此为准则无可厚非。", "evidence": "P013", "ambiguity": "作者把它限定在学校场域，未主张在社会讨论中适用"},
    {"term": "概念更新", "meaning": "作者用以说明进步即概念被重新界定的过程。", "evidence": "P024", "ambiguity": "无"},
    {"term": "不可剥夺", "meaning": "作者给出双重含义：想剥夺也做不到；以及若真贯彻这种蠢行，社群必将落后挨打乃至自取灭亡。", "evidence": "P026", "ambiguity": "第二重含义是强预测，缺少论证"} 
   ],
   "examples_and_targets": [
    "高考／评卷组／大纲教材（P014–P016，作者例证，用来说明校内标准唯一）。",
    "在卷子上写“在我的理论中，剥削是指xxxx”（P014，作者举的无效答卷写法）。",
    "重新定义加减法（P015，反问例证）。",
    "满坑满谷一败涂地的博士（P020，反问例证，未给数据）。",
    "答辩委员会、老板、客户（P018，受评价者处境例证）。",
    "思想史与“拉去土墙前挨个处决”（P021，夸张化的反问材料）。",
    "网上社区的同为学生心态而不自知的共鸣者（P028，作者描述的现象）。",
    "“偷换偷换概念的概念”（P030，作者预判中的反驳者说法）。",
    "被反驳对象：以“与我／我所崇拜的文献／伟人理解不同”判定偷换概念的思路及其持有者（未指名个人）。"
   ],
   "conditions": [
    "偷换概念成立的前提是“对方先对一个概念做了独立定义”，或在双方事先明确达成共识的情形下对方违背该共识（P007–P008）。",
    "“无可厚非”的让步被明确限定在学校教育、至少中国学校教育，以及高考这一考核场域（P014–P016）。",
    "作者把校内（以教科书为准）与社会（须自担解释义务、自己出合同条款）区分为两种不同场景（P014–P019）。",
    "社会后果的警告针对“有名有姓的对任何已经成熟而独立的人”使用该指责、甚至只让对方感到你有这个意思的情形（P028）。"
   ],
   "rhetoric_and_tone": "驳论结构：先树靶再逐层拆解；反问密集（“你难道就不是偷换ta所认定的概念的罪人？”“为何还有满坑满谷一败涂地的博士？”）；措辞口语化且带斥责与讽刺（“这是被考试害的”“什么狗屁教科书？”“糊涂人”）；后段转为预言式警告与近乎威胁的劝告（“倒霉是肯定的”“你还是早点开始找工作吧”“没人会接受你的”）；以英文短句“Poetic irony.”收尾，并预先写出对手可能用来反驳自己的说法。",
   "unresolved_questions": [
    "“独立定义”“明确接受”的判定标准未说明：默示接受、部分接受、约定俗成是否算作接受，本文未交代。",
    "“主流解释”的边界，以及“更加精细的定义”与“重定义”的界线，未给出判准。",
    "P022 原文存在讹字与引号不配对（“自甘为为奴”“偷换概念“的罪”），本次只按可确认的连续片段引证，未据讹字推断语义，建议复核原文。",
    "“贯彻这种蠢行的社群必将陷入落后挨打乃至于自取灭亡”属强预测，本文未给依据，待外部核查。",
    "提问问的是“如何发现”，作者给出的是成立条件与心态批评，未给可操作的识别步骤（如对方确实在论证中滑动词义时怎么办）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人所谓的“偷换概念”的判定逻辑是这样的：", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "1）自己先对某个概念有个默认理解。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "2）发现别人的理解和自己的理解不一致。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "3）认定别人偷换概念。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "ta确信自己的理解是宇宙真理，终极正确，顺之者正确，逆之者错误", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "只要对方基于这个概念推导出的结论令ta不满，而论证过程又找不到任何破绽，则必然可以逆推“对方一定是偷换了概念”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "偷换概念必须是以对方先对一个概念做了独立定义，而在其后的论证中又违背了其【自己所作/认可的定义】，才能成立的", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "那么你发现对方违背了这个定义，可以算作偷换概念", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P008", "quote": "本质上那仍然是对方通过特殊的简短方法声明了自己的定义，然后自己违反了ta自己的声明", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P009", "quote": "对方在没有明确接受的前提下违背了【你的】定义，根本不构成任何意义上的逻辑问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "因为如果按照这个伦理法则，你不是同样一开始就违背了对方心中默许的概念定义？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "这是被考试害的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "常常因为违背教科书的定义而被判定有偷换概念的错误", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "高考可不管你自己什么想法什么理解，高考只有一种定义，评卷组的的定义。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "既然你参加全国统一高考，就是来接受全国统一高考的考核标准的。", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P016", "quote": "谁和大纲教材不符，谁就构成偷换概念或理解错误。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "想当然的假定别人默认就是在参加ta自任阅卷组首席权威的“私家高考”。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "总是生活在由别人划定好的定义范围之内", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "如果教科书的定义就是终极而完全的真理，为何还有满坑满谷一败涂地的博士？", "relation": "contradicts"},
    {"key": "E20", "paragraph_id": "P021", "quote": "人类的整个思想史都是不断重新界定概念的过程。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "按你们这种判罪法，你们自己崇拜的大师们首先就得拉去土墙前挨个处决。", "relation": "contradicts"},
    {"key": "E22", "paragraph_id": "P022", "quote": "即不允许任何人重定义或更加精细的定义“主流解释”", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P023", "quote": "甚至哪怕你自以为是在基于某种“爱国”的立场去这样做，你也是在阻碍这个国家自己的进步。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P024", "quote": "因为进步本身即是概念的更新。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P025", "quote": "对方违背自己声明的定义，才构成偷换概念，并且任何人都有天然不可剥夺的权利去在自己的论述中阐述自己的定义。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P026", "quote": "贯彻这种蠢行的社群必将陷入落后挨打乃至于自取灭亡", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P027", "quote": "这种“与我/我所崇拜的文献/伟人理解不同即偷换概念”的思路，在社会上一旦显露出来，倒霉是肯定的。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P028", "quote": "你还是早点开始找工作吧。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P030", "quote": "还是会有人说这篇东西是在“偷换偷换概念的概念”。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P031", "quote": "Poetic irony.", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["逻辑与论证", "概念论", "教育批评", "社会批评"],
   "issue_candidates": ["偷换概念的判定标准", "定义权与共识", "应试教育形成的思维惯性", "概念的重新界定与进步"],
   "text_function_candidates": ["答疑", "驳论", "批评"],
   "object_candidates": ["学生／知乎用户（未具名）", "评卷组", "博士", "大师", "答辩委员会／老板／客户", "创业者"],
   "working_keywords": ["偷换概念", "定义", "共识", "私家高考", "教科书定义", "概念更新", "不可剥夺", "Poetic irony"]
  },
  "notes": "无图片节点，正文完整可读，按默认 status=read 处理。P022 存在讹字与引号不配对（“自甘为为奴”“偷换概念“的罪”），本次只按可确认的连续片段引证，未据讹字推断语义，建议复核原文。opponent 指文中未具名的“糊涂人”群体思路，非特定个人。lexical 段落计数(31)与正文段落数(31)一致。updated_at(2021-05-25) 晚于 published_at(2020-09-22)。"
 },
 "78fbcfee": {
  "analysis": {
   "question_context": "提问者（Q001）问：摩托车究竟有什么魅力？作者以用词区分切入（摩托车叫“驾”，汽车叫“驶”），给出两条理由：一是“超透明”带来的沉浸体验，二是多感官并存的“超立体”驾驶体验，并由此推出摩托车更容易让人觉得魅力更大。属经验说明型回答，不作外部论证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以用词切入：摩托车称“驾”，汽车称“驶”。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "第一项魅力“超透明”：视野中几乎看不到车体、无需主动发力，实体感被削弱，易转化为“人车合一”式沉浸体验，并列出一批同类体验。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "补充：这种沉浸感带来的“我tm是超人”之感是很大的加分项。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "第二项魅力“超立体”：列举重心、风压风噪、引擎排气声、震动、路感、离心力、冷热、头盔光学与通信等众多子项。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "与汽车对比：汽车各方面都弱一截且缺少风压、热晒、重心变化感，故驾驶感不如摩托车立体。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P006"], "summary": "推论：子项变化构成私人体验特征项，使体验如位数更多的密码；越立体越易形成独特感受与对座驾的感情联结。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P007"], "summary": "结论：所以人比较容易觉得摩托车的魅力更大。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在用语上，摩托车叫“驾”，汽车叫“驶”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "摩托车的第一项魅力是“超透明”：正常驾驶视野里几乎看不到车体，驾驶员可完全专注路面；它又不像自行车需主动发力驱动，进一步削弱了摩托车的“实体感”，这种透明感易转化为“人车合一”式沉浸体验。", "evidence": ["E2", "E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种沉浸感带来的“我tm是超人”的感觉是一个很大的加分项。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "摩托车的第二项魅力是驾驶体验“超立体”，其子项包括重心变化、风压、风噪、排气声、引擎声、机身震动、减震缓冲、握把与座位传来的路感、离心力、阳光的热、风的凉等。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "汽车在所有方面都弱掉一截，而且少了风压、热晒、重心变化感，因此驾驶感不如摩托车立体。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "各子项的变化构成私人驾驶体验的特征项，使摩托车驾驶体验像位数多几倍的密码、因人而异；体验越立体，越容易形成独特感受（深刻记忆）与对座驾的感情联结。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "所以人比较容易觉得摩托车的魅力更大。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者设问：摩托车究竟有什么魅力？", "evidence": []}
   ],
   "argument_steps": [
    "以“驾／驶”的用词区分开场（P001）。",
    "给出第一项理由：超透明带来的实体感削弱与沉浸体验（P002）。",
    "补充沉浸感的情绪收益（P003）。",
    "给出第二项理由：多感官叠加的超立体体验（P004）。",
    "与汽车逐项对比，说明其驾驶感较弱（P005）。",
    "由子项差异推出个体化体验与感情联结（P006）。",
    "以概率化表述作结论（P007）。"
   ],
   "concept_usage": [
    {"term": "驾／驶", "meaning": "以用词差异区分摩托车与汽车的驾驶方式，作为全文切入点。", "evidence": "P001", "ambiguity": "未说明这是语言事实还是作者的修辞设定"},
    {"term": "超透明", "meaning": "驾驶视野中几乎看不到车体、又无需主动发力，摩托车的存在感被削弱。", "evidence": "P002", "ambiguity": "自造词，未给度量标准"},
    {"term": "实体感", "meaning": "驾驶者对车体存在感的感知强度，作者认为摩托车此项较弱。", "evidence": "P002", "ambiguity": "无"},
    {"term": "人车合一", "meaning": "透明感转化成的沉浸体验类型，作者以引号标出。", "evidence": "P002", "ambiguity": "借用常见说法，未定义"},
    {"term": "超立体", "meaning": "驾驶体验同时包含风压、声音、震动、路感、离心力、冷热等多通道输入。", "evidence": "P004", "ambiguity": "自造词，未给度量标准"}
   ],
   "examples_and_targets": [
    "速降自行车、滑雪板、滑水板、滚轮滑板、冰鞋、滑翔伞、飞行翼装（P002，作者列举的同类沉浸体验，属类比材料）。",
    "汽车（P005，全篇的对比对象）。",
    "密码（P006，类比：体验如位数更多、因人而异的密码）。",
    "“我tm是超人”（P003，口语化感叹，修辞材料）。"
   ],
   "conditions": [
    "“超透明”以“正常的驾驶视野”为前提（P002）。",
    "论证以汽车为唯一对比基准，未讨论其他交通工具（P005）。",
    "结论使用“比较容易”的概率化表述，不是全称判断（P007）。",
    "未涉及安全、事故风险、法规、成本、气候与路况等条件（正文未说明）。"
   ],
   "rhetoric_and_tone": "说明文式的两层列举（“首先”“第二”），并用引号标注自造概念（“超透明”“超立体”）；以多感官清单堆叠制造代入感，中间插入一句粗口式感叹加强趣味（“我tm是超人”）；结尾以“所以人比较容易……”平缓收束，整体是轻松的经验分享语气，末尾出现两个句号（原文如此）。",
   "unresolved_questions": [
    "“驾”与“驶”的用词区分是语言事实还是作者的修辞设定，本文未给依据。",
    "结论建立在个人驾驶经验上，未给出车型、骑行条件或任何样本依据，待外部核查。",
    "未讨论摩托车的风险、事故率、法规限制与成本，属本文未涉及的方面。",
    "P007 结尾原有双句号（“魅力更大。。”），疑为笔误，建议复核原文。",
    "P004 提到“头盔减速透镜对道路的扭曲”等装备细节，表述是否准确需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "摩托车叫“驾”，汽车叫“驶”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "首先摩托车是“超透明”的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "在正常的驾驶视野里几乎看不到车体本身的存在，驾驶员可以完全专注在路面上。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "而它又不像自行车那样去要主动发力去驱动，这更加削弱了摩托车本身的“实体感”。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P002", "quote": "这种透明感很容易转化为“人车合一”这类沉浸体验", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P003", "quote": "这种沉浸感所带来的“我tm是超人”的感觉是一个很大的加分项。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P004", "quote": "第二，摩托车的驾驶体验是超立体的", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P004", "quote": "重心变化、风压、风噪、排气声、引擎声、机身震动、减震缓冲、握把和座位传来的路感、离心力、阳光的热、风的凉", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P005", "quote": "汽车在所有方面都弱掉一截，而且还少了风压、热晒、重心变化感", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P006", "quote": "这导致摩托车驾驶的体验犹如一串位数多几倍的密码，每个人都有很大的不同。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P006", "quote": "驾驶体验越立体，越容易形成独特感受（也就是深刻记忆）和与座驾的感情联结。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P007", "quote": "所以人比较容易觉得摩托车的魅力更大。。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["交通工具体验", "驾驶感受", "休闲骑行"],
   "issue_candidates": ["摩托车魅力来源", "沉浸体验", "多感官驾驶体验", "摩托与汽车对比"],
   "text_function_candidates": ["答疑", "解释", "经验总结"],
   "object_candidates": ["摩托车", "汽车", "自行车", "速降自行车／滑雪板／滑翔伞等"],
   "working_keywords": ["驾", "驶", "超透明", "实体感", "人车合一", "超立体", "沉浸感"]
  },
  "notes": "无图片节点，正文完整可读，按默认 status=read 处理。lexical 段落计数(7)与正文段落数(7)一致。P007 末尾原有双句号，按原文保留。updated_at(2021-08-09) 晚于 published_at(2020-09-23)。"
 },
 "13ff0e77": {
  "analysis": {
   "question_context": "提问者（Q001）问：什么是「大公司病」，在你看来有哪些互联网公司已经出现了大公司病的现象？作者只回答了前一半：承认大公司病存在，但否定通行的“官僚主义／繁文缛节”归因，主张病在价值观与组织意志，并追溯根子到领导层丧失理想和原则。对“哪些互联网公司”一问，正文未点名任何公司。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开宗明义：大公司病是有的，但一般都不出在“官僚主义”上。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "复述一般人的批评：很简单的事情被搞得很复杂，层层转达、协调多部门、来回审批走流程、搞议程文档日志，并认为根本不必要。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "反驳：这是误解——要保证大量人员稳妥合作、责权清晰、步调一致，这些设计基本是题中应有之义，不能省略；少一两条就会有可怕的空子、扯皮、诉讼责任乃至事故死伤。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "给出真正的病灶：宗旨上的异变与组织意志上的涣散，以致人们恶意利用规则；规章只是做事的规矩和方法。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "归结：大企业病一般都是病在价值观，是自上而下丧失理想、自下而上丧失共识的精神病。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P008"], "summary": "说明病的表现：不是繁文缛节、叠床架屋，而是虚伪和道德虚无主义；具体为员工低自尊与无原则，进而生出各谋私利、欺上瞒下、窝案与僵尸化。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P009", "P010"], "summary": "追溯根子：总在领导层丧失理想和原则（创始人受名利侵蚀、传承所托非人、并购引入投机性文化基因）；灵魂中毒则失去义士的忠诚，而义士是企业的真正脊梁。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P011", "P012"], "summary": "结论：义士一失望，企业立刻开始腐烂；这才是大企业病的要害，不是那些规章制度。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "大公司病是存在的，但一般都不出在“官僚主义”上。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "一般人对“大公司病”的批评是：很简单的事情被搞得很复杂，一点事要层层转达、协调好几个部门、来回审批走流程、搞议程文档日志，并认为这“根本不必要”。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述批评是误解：要保证大量人员稳妥合作、各项责权清晰、步调协调一致，这些设计基本都是题中应有之义、不能省略；少一两条就会有可怕的空子、数不清的扯皮，还可能惹出诉讼责任乃至生产事故与死伤。", "evidence": ["E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的问题是企业出现了宗旨上的异变与组织意志上的涣散，以致人们恶意利用规则；规章只是做事的规矩和方法，真问题是到底想做什么、为什么而做、参与者中有多少真想做成。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大企业病一般都是病在价值观，是一种自上而下丧失理想、而又自下而上丧失共识的精神病。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "它不体现为“繁文缛节”“叠床架屋”，而体现为虚伪和道德虚无主义，具体表现为员工的低自尊和无原则，再由此生出各谋私利、欺上瞒下、窝案与底层员工心知肚明且普遍存在的僵尸化。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个根子总是在于领导层丧失了理想和原则，其来源包括创始人受不住名利侵蚀、公司传承所托非人、战略并购引入虚无主义与唯利是图的投机性文化基因。", "evidence": ["E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "企业灵魂中毒就会失去义士的忠诚；这些无法被有效收买、也不能被暴力屈服的人，才是挺住企业最基本伦理原则、保证出力者得善果、偷窃者被驱逐的真正脊梁。", "evidence": ["E16", "E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "义士一失望，企业立刻开始腐烂；这才是大企业病的要害，而不是那些规章制度。", "evidence": ["E18", "E19"]},
    {"claim_id": "C010", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者设问：什么是「大公司病」，有哪些互联网公司已经出现了大公司病的现象？", "evidence": []}
   ],
   "argument_steps": [
    "先承认大公司病存在，再否定“官僚主义”这一通行归因（P001）。",
    "复述一般人的批评内容（P002–P003）。",
    "以“这是误解”反驳，并说明流程设计的必要性与省略后果（P004）。",
    "转向真正的病灶：宗旨异变与组织意志涣散，规章只是方法（P005）。",
    "归结为价值观之病与精神病（P006–P007）。",
    "描述病的具体表现层次：虚伪、道德虚无主义、员工低自尊无原则、再到谋私与僵尸化（P008）。",
    "追溯根子到领导层，并列举三种失理想／失原则的来源（P009–P010）。",
    "以义士失望则企业腐烂收束，重申要害不在规章（P011–P012）。"
   ],
   "concept_usage": [
    {"term": "大公司病", "meaning": "作者把它重新定位为价值观与组织意志之病，而非官僚主义或繁文缛节。", "evidence": "P006", "ambiguity": "未给判定标准与可观察指标"},
    {"term": "官僚主义", "meaning": "通行的归因；作者承认病存在但一般不出在此处。", "evidence": "P001", "ambiguity": "“一般”留有余地，未说明例外情形"},
    {"term": "宗旨上的异变", "meaning": "企业“到底想做什么、为什么而做”发生偏移。", "evidence": "P005", "ambiguity": "未说明如何识别宗旨是否已异变"},
    {"term": "组织意志上的涣散", "meaning": "参与者共识瓦解，以致恶意利用规则。", "evidence": "P005", "ambiguity": "无"},
    {"term": "道德虚无主义", "meaning": "与虚伪并列的病症表现，对应员工低自尊与无原则。", "evidence": "P008", "ambiguity": "借用的外来词，本文未作界定"},
    {"term": "僵尸化", "meaning": "底层员工心知肚明且普遍存在的状态。", "evidence": "P008", "ambiguity": "比喻，未给行为特征"},
    {"term": "义士", "meaning": "无法被有效收买、也不能被暴力屈服、挺住企业基本伦理原则的人。", "evidence": "P010", "ambiguity": "本文未给正式定义，与常见词义的关系未说明"}
   ],
   "examples_and_targets": [
    "一般人批评中的“繁文缛节”“叠床架屋”、层层转达、审批流程、议程文档日志（P002、P008，被作者反驳的通行归因，未指名个人）。",
    "创始人受不住名利侵蚀、公司传承所托非人、战略并购引入虚无主义与唯利是图的投机性文化基因（P010，作者列举的三种成因）。",
    "“威武不能屈、贫贱不能移、富贵不能淫”（P010，典故化表述，未点名出处，用作修辞材料）。",
    "义士、出力者、偷窃者、底层员工、领导层、创始人（P008–P011，作者的分析对象与角色）。",
    "提问要求列举的“已经出现大公司病的互联网公司”——正文未点名任何公司（缺口）。"
   ],
   "conditions": [
    "作者用“一般都不出在”留有余地，未完全排除官僚主义问题（P001）。",
    "病因链以“只要企业的灵魂中毒”为条件表述（P010）。",
    "未限定行业、企业规模、国别或发展阶段（正文未说明）。",
    "未给出判定“大公司病”的操作指标、案例或数据（正文未说明）。"
   ],
   "rhetoric_and_tone": "先让步后转折的驳论结构（“大公司病是有的，但……”）；以病理与身体隐喻贯穿（“精神病”“灵魂中毒”“腐烂”“僵尸化”）；判断句短促有力（“大企业病，一般都是病在价值观”“这才是大企业病的要害”）；借用“威武不能屈、贫贱不能移、富贵不能淫”的排比典故强化义士形象；语气为评论式、训诫式，全程不针对具体公司或人物。",
   "unresolved_questions": [
    "提问的第二部分（有哪些互联网公司已经出现了大公司病）本文完全未回答，未点名任何公司，属明确缺口。",
    "“义士”在本文未定义，其判准与识别方式未说明（不得以其他篇目的用法补入）。",
    "“僵尸化”“灵魂中毒”“精神病”均为比喻，未给可操作的判别标准。",
    "“战略并购引入虚无主义、唯利是图的投机性的文化基因”等因果断言未给案例或依据，待外部核查。",
    "updated_at(2026-04-10) 明显晚于 published_at(2020-09-24)，平台侧可能修订过正文，版本差异无法从本记录判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "大公司病是有的，但一般都不出在“官僚主义”上。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "一般人批评“大公司病”，批评的往往是“很简单的事情搞得很复杂”", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "觉得这“根本不必要”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "但这是一个误解。", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P004", "quote": "要保证大量人员稳妥的合作，各项责权清晰，步调协调一致，这些设计基本都是题中应有之义，是不能省略的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "少了一条两条，就会有可怕的空子可以钻，数不清的皮可以扯", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "真正的问题，是企业出现了宗旨上的异变，出现了组织意志上的涣散，以至于人们会恶意的利用这些规则。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P005", "quote": "规章只是做事的规矩和方法，真正的问题是到底想做什么、为什么而做", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P006", "quote": "换句话说，大企业病，一般都是病在价值观。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "这是一种自上而下丧失理想，而又自下而上丧失共识的精神病。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "它不体现为“繁文缛节”“叠床架屋”，而体现为虚伪和道德虚无主义。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "具体而微的表现为其具体员工的低自尊和无原则。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P008", "quote": "然后才由此而生发出肉眼可见的各谋私利、欺上瞒下，出现窝案、出现底层员工心知肚明且普遍存在的僵尸化。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P009", "quote": "而这个根子，总是在于领导层丧失了理想和原则。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P010", "quote": "无论是创始人受不住名利侵蚀，还是公司传承所托非人，又或者因为战略并购引入了虚无主义、唯利是图的投机性的文化基因", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P010", "quote": "只要企业的灵魂中毒，企业就会失去那些威武不能屈、贫贱不能移、富贵不能淫的义士的忠诚", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P010", "quote": "才是挺住这个企业最基本的伦理原则，保证出力者得善果、偷窃者被驱逐的真正脊梁。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P011", "quote": "ta们一失望，企业立刻开始腐烂。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P012", "quote": "这才是大企业病的要害，不是那些规章制度。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["企业管理", "组织文化", "公司治理"],
   "issue_candidates": ["大公司病的病因", "官僚主义是否为病根", "价值观与组织意志", "义士与核心岗位用人"],
   "text_function_candidates": ["答疑", "解释", "评论", "论辩"],
   "object_candidates": ["大公司／互联网公司（未点名）", "领导层", "创始人", "底层员工", "义士"],
   "working_keywords": ["大公司病", "官僚主义", "宗旨上的异变", "组织意志涣散", "价值观", "道德虚无主义", "僵尸化", "义士"]
  },
  "notes": "无图片节点，正文完整可读，按默认 status=read 处理。opponent 指文中未具名的“一般人”常见批评，非特定个人。提问第二部分（哪些互联网公司已出现大公司病）在正文中完全没有回答，已登记为未决问题与缺口。lexical 段落计数(12)与正文段落数(12)一致。updated_at(2026-04-10) 晚于 published_at(2020-09-24)。"
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
