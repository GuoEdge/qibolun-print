# -*- coding: utf-8 -*-
"""批次 r001-b0052 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0052.sessions.py            # 写 out/r001-b0052.out.jsonl
  python3 records/r001-b0052.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0052"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0052.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "320a2135": {
  "analysis": {
   "question_context": "提问者问美术老师口中的“敢画”“画得大胆”是什么意思（Q001，属提问者）。作者不把它当作绘画技法问题，而按字面解释为画面上呈现出来的勇气，并把它扩展为一种面对犯错与后果的行为方式，进而追到教师、父母与亲友的守护责任上。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出“敢画”即在画面上呈现的勇气：敢出手、敢承担出手后果、敢推进画面。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "举例：很多人打大型明知大型不准会出大问题，却反复精准测量直到时间用尽才被迫走下一步。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "该行为模式推展到执行的每一阶段，总被火烧眉毛才前进，永远不提前交卷。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "“敢画”者敢于犯错，大不了画下来后面再改，改不了就重来多遍。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P011"], "summary": "后一种人经验积累与毕业时水平远非前者可比，最终走完全不同的人生道路。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P012"], "summary": "设问：后一种人凭的是什么？", "role": "transition"},
    {"unit_id": "U007", "paragraph_refs": ["P013"], "summary": "第一凭好老师、好守护者，保证交给他的任务错了也错得起，护住安全底线。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P014"], "summary": "第二凭好的父母和亲友，为一次又一次错误有效分担，避免对失败过度敏感恐惧。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P015", "P016"], "summary": "不敢画的小孩被不负责任的任务交付者和不履责的父母亲友隐性遗弃，害怕承担不起失败后果。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P017", "P018"], "summary": "反问后给出行动要求：父母的教育责任是找到能分辨安全任务的教师并为仍发生的失败买单。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "父母把自身失职的负面情绪报复在子女身上，子女就会“不敢画”并走上“天资愚钝”之路，而这“钝”在父母身上。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P024", "P025"], "summary": "收尾劝诫：只能通过改变自己来改变别人，父母改变自己孩子就能好一截。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“敢画”指在画面上呈现出来的勇气：敢于出手、敢于面对出手的后果、敢于推进画面的进展。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人打大型时明知大型不准后面会出大问题，仍反复测量，直到时间用尽才被迫走下一步；这种行为模式推展到执行的每一个阶段。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓敢画的就是敢于犯错：大不了画下来后面再改，真改不了就从头再来多遍。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敢画者的经验积累和毕业时的水平远非不敢画者可比，最终会走上完全不同的人生道路。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敢画的第一凭据是好老师、好守护者：他们保证交给学生的任务错了也错得起，以对交付任务负责的态度和足够智慧保住安全底线。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "敢画的第二凭据是好父母和亲友：其支持为一次又一次错误做了有效分担，避免对失败产生过度敏感和恐惧。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不敢画的小孩子是被不负责任的任务交付者与不履行自己职责的父母亲友隐性遗弃了；他们下意识害怕自己薄弱的承担能力承担不起失败的后果。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母的教育责任在于找到拥有能分辨何谓安全任务的智慧的教师，以及为仍然发生的失败买单的自觉。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母把因自己失职和愚蠢造成的损失所引发的负面情绪报复在没有反抗能力的子女身上，子女就会“不敢画”，于是走上“天资愚钝”之路。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“天资愚钝”并不钝在子女身上，而是钝在父母身上；没检讨清楚这一点的父母没有资格认定子女的天资是否愚钝。", "evidence": ["E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只能通过改变自己来改变别人；父母改变自己，孩子就能好一截。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "以提问者的问题起手（Q001），把“敢画”从画面问题解释为画面上的勇气（P001）。",
    "列勇气三项：敢出手、敢面对后果、敢推进画面（P002）。",
    "举例“打大型—精准测量—拖到时间尽头”的拖延模式（P003—P005），并称该模式推展到执行每一阶段（P006—P008）。",
    "正面对照：敢画者敢于犯错，允许重画、重来多遍（P009—P010）。",
    "给出结论：后一种人经验与毕业水平远非前者可比，人生道路不同（P011）。",
    "设问“凭的是什么呢”，引出两项条件（P012）。",
    "第一凭好老师好守护者，使任务错了也错得起（P013）；第二凭好父母亲友分担错误、避免对失败过度敏感（P014）。",
    "反面推论：不敢画的小孩被隐性遗弃，害怕承担不起后果（P015—P016）。",
    "反问后给行动要求：父母须找有分辨安全任务智慧的教师并为失败买单（P017—P018）。",
    "训诫式推论：父母情绪报复导致子女不敢画、被认定“天资愚钝”，而钝在父母（P019—P023）。",
    "收尾劝改：只能通过改变自己来改变别人（P024—P025）。"
   ],
   "concept_usage": [
    {"term": "敢画", "meaning": "画面上的勇气，即敢出手、敢面对出手后果、敢推进画面，宁可犯错再改或重来。", "evidence": "P001", "ambiguity": "作者自称按字面解释，未讨论绘画技法层面的其他含义"},
    {"term": "敢得起的错误 / 安全底线", "meaning": "教师与家长使交给学生的任务失败了也承受得起，从而不产生无端恐惧。", "evidence": "P013", "ambiguity": "“错得起”的判定标准与范围未说明"},
    {"term": "隐性遗弃", "meaning": "不负责任的任务交付者与不履责的父母亲友让小孩下意识害怕承担失败后果。", "evidence": "P015", "ambiguity": "为作者自造表述，未给出操作定义"},
    {"term": "天资愚钝", "meaning": "被加在不敢画的小孩身上的评价，作者反指其根源在父母。", "evidence": "P021", "ambiguity": "作者以引号使用该词，未给出衡量标准"}
   ],
   "examples_and_targets": [
    "“打大型”“大型不准”：美术训练场景，作作者例证（P003）。",
    "“精准测量”拖延到下课交不了东西：行为模式例证（P004—P005）。",
    "“提前交卷”：作者用作比喻（P008）。",
    "“赔自己打破的玻璃、划伤的车漆”：作者设想的具体恐惧场景（P016）。",
    "好老师、好守护者、好的父母和亲友、不负责任的任务交付者、不履责的父母亲友：作者例举的两类责任主体（P013—P015）。"
   ],
   "conditions": [
    "前提条件：“这些人保证了交给他的任务是错了也错得起的”——教师一侧须使错误可承担（P013）。",
    "前提条件：父母亲友能为一次又一次错误做有效分担，才会避免对失败的过度敏感和恐惧（P014）。",
    "适用范围：作者称该行为模式会推展到执行的每一个阶段（P006）。",
    "作者未明说的边界：年龄、训练阶段、任务类型、失败代价上限均未限定。"
   ],
   "rhetoric_and_tone": "口语化训诫与调侃并用：以“特么”“怕个球啊”“老纸”等粗话增强语气，连续反问“所以，你们看明白我要说的是什么了吗？”直接对父母发话，用“幼崽”“小崽子”等称呼；末段以“不信你试试”收束，带挑衅式劝服。",
   "unresolved_questions": [
    "提问者问的是“美术老师们口中的”用法，作者是否代表美术教师群体、其解释是否与该群体一致，本文未说明。",
    "“错了也错得起”的判定标准和失败代价上限未说明。",
    "作者以“后一种人”对比“前者”，但前一种人的具体指称在行文中靠上下文推定，未明确定义。",
    "文中未给出任何个案、数据或出处支持“经验积累和毕业时的水平远非前者可比”的断言，属待外部核查的事实性断言。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“敢画”当然是指在画面上呈现出来的勇气。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "敢于出手，敢于面对出手的后果，敢于推进画面的进展。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "很多人打大型，心里都知道“大型不准后面要出大问题”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "才万般不情愿的放弃了继续“精准测量”的打算，开始走下一步。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "所谓敢画的，就是敢于犯错，大不了老子画下来后面再改。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "后一种人的经验积累和毕业时的水平远非前者可比。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "这些人保证了交给他的任务是错了也错得起的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "好的父母和亲友的支持，为他们一次又一次的错误做了有效的分担。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "那些不敢画的小孩子们，是被不负责任的任务交付者，和不履行自己职责的父母亲友所隐性的遗弃了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "他们下意识的害怕自己薄弱的承担能力承担不起这失败的后果。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "父母的教育责任，在于找到那些拥有能分辨何谓安全任务的智慧的教师，以及为仍然发生的失败买单的自觉。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "然后把因自己的失职和愚蠢造成的损失引发的负面情绪报复在没有反抗能力的子女身上。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "你的子女就会“不敢画”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "其实这“天资愚钝”，并不钝在他们身上。而是钝在你们身上了。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "没检讨清楚这一点的父母，没有资格去认定子女的天资是否愚钝。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "你只能通过改变自己来改变别人。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["美术教育", "家庭教育与儿童心理", "学习行为与拖延"],
   "issue_candidates": ["“敢画”的含义", "犯错成本与安全感", "教师与家长对失败的分担责任", "天资评价的归因"],
   "text_function_candidates": ["答疑", "经验总结", "训诫式评论"],
   "object_candidates": ["美术教师", "学画者（打大型的学生）", "父母与亲友"],
   "working_keywords": ["敢画", "大型不准", "精准测量", "提前交卷", "隐性遗弃", "天资愚钝", "安全底线"]
  },
  "notes": "无图片节点。正文25段全部读完（lexical 统计 paragraph 25，与 P001—P025 一致）；question 属提问者，未计入作者主张。文中“天资愚钝”“经验积累远非前者可比”等属事实性断言，未附出处，登记为待外部核查，不作外部裁决。"
 },
 "5e41ab6c": {
  "analysis": {
   "question_context": "提问者问如何看待美国黑人被警察跪压7分钟死亡（Q001，属提问者）。作者在承认涉事警察、当地政府与联邦政府令人愤怒的前提下，自称要为美国说几句“公道话”，把事件解读为种族主义者与反种族主义者之争，并据此判断美国的种族矛盾与国势并未到达真正危险的时刻。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "作者要为美国说公道话，同时承认涉事警察、包庇的当地政府与上至特朗普的联邦政府令人愤怒，并斥其背叛立国精神。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "作者称立国精神与道德原则是美国真正的力量源泉，如此下去美国会自己丢掉世界领导权。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "引出“公道话”：抗议人群中也有其他肤色的人，尤其有不少白人；并以图片为据（“仔细看一下这些图片”）。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010"], "summary": "作者判定这不是黑人与白人的种族间矛盾，而是种族主义者与反种族主义者之间的矛盾。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P011", "P012"], "summary": "只要还有足够量的白人站在受害黑人一边承担风险，种族歧视就未到真正危险时刻；真正的种族矛盾是胡图族与图西族那种无人站在对面的仇恨。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "很多人以为此事意味着美国不行了、衰落了，作者认为这不为错；但另一面美国的灵魂并没有死掉，还未到无药可救。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P015"], "summary": "只要这些东西还在，美国这一世代国祚远未享尽，遭遇多大打击都不至真正溃散；在这一点上不丢失核心价值的中国也一样。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P016"], "summary": "只要核心价值仍被有效实践，其他国家就不能以彻底击败或压倒美国为战略设想，只能以互相敬畏、寻求和平共处为合理规划目标。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P017"], "summary": "坦率地说，这并不是美国衰亡开始的无可辩驳的证据，虽然可能是特朗普这一系衰亡的开始。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要为美国说几句公道话，同时承认杀害黑人的警察、包庇遮掩的当地政府以及显著种族主义化的联邦政府的确令人愤怒。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为美国的上层建筑与统治精英在背叛美国最初的立国精神和道德原则，而这东西是美国真正的力量源泉。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这样搞下去美国不走下坡路、不挫折是不可能的；即使中国不做任何主动挑战，只要美国修正不了这种愚蠢走向，自己都会把世界领导权丢掉。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者据抗议人群中有其他肤色者尤其不少白人，判定这不是黑人和白人的种族间矛盾，而是种族主义者与反种族主义者之间的矛盾。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "只要还会有足够量的白人站在受害黑人一边抗议并承担风险，就可以说美国的种族歧视问题并没有到达真正危险的时刻。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的危险是所有的胡图族杀死所有的图西族、没有胡图族站在自己族人对面，那才叫种族之间的仇恨，才叫真正的种族矛盾。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "很多人以为此事意味着美国不行了、衰落了，这不为错；但另一面美国的灵魂并没有死掉，还没有衰落到丧失全部道德力量、无药可救的地步。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "只要这些东西还在，美国这一世代的国祚就远未享尽，遭遇多大打击都不至于真正溃散；在这一点上，不丢失自己核心价值的中国也一样。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "只要美国的国家核心价值仍然被有效实践，其他国家就不能把“彻底击败或者压倒”美国作为战略设想，只能将“互相敬畏、寻求最终和平共处”作为合理的规划目标。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为此事并不是美国衰亡开始的无可辩驳的证据——虽然这可能是特朗普这一系衰亡的开始。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "先声明立场是“为美国说几句公道话”，同时承认警察、地方政府与联邦政府令人愤怒（P001—P002）。",
    "指控统治精英把《人权宣言》当擦桌布、背叛立国精神，并称该精神是美国真正的力量源泉（P003—P004）。",
    "预测美国将走下坡路，甚至自行丢掉世界领导权（P005）。",
    "设问“公道话是什么呢”，援引抗议人群中其他肤色者特别是白人，并指向图片（P006—P009）。",
    "给出重新定性：矛盾不在黑白种族之间，而在种族主义者与反种族主义者之间（P010）。",
    "以白人是否站在受害黑人一边作为危险程度的判据，并以胡图族／图西族为真正的种族矛盾样板（P011—P012）。",
    "让步：承认“美国不行了、衰落了”不为错，但转向另一面，称美国灵魂未死（P013—P014）。",
    "推进为条件性判断：只要核心价值还在、仍被有效实践，美国不至溃散，他国也不得以彻底击败美国为战略设想（P015—P016）。",
    "收尾限定：这不是美国衰亡的无可辩驳证据，但可能是特朗普这一系衰亡的开始（P017）。"
   ],
   "concept_usage": [
    {"term": "公道话", "meaning": "作者为美国辩护的表述，其内容是否定“种族间矛盾”的定性与“美国已衰亡”的判断。", "evidence": "P001", "ambiguity": "“公道”的判准来自作者的立国精神框架，为作者自述立场"},
    {"term": "力量源泉", "meaning": "指美国最初的立国精神和道德原则（以“这东西”回指）。", "evidence": "P004", "ambiguity": "“这东西”指代依赖上文回指，未给出定义式说明"},
    {"term": "种族矛盾", "meaning": "作者限指胡图族与图西族式、无任何一方族人站到对面的种族间仇恨，而非本案中的黑白对立。", "evidence": "P012", "ambiguity": "作者给出的是极端样板，中间形态未界定"},
    {"term": "灵魂 / 核心价值", "meaning": "美国尚未丧失的道德力量与立国精神，作者称其未死故国祚未尽。", "evidence": "P015", "ambiguity": "以“这些东西”模糊指代，缺可核验指标"}
   ],
   "examples_and_targets": [
    "乔治·弗洛伊德事件（提问者所述“美国黑人被警察跪压7分钟死亡”）：文章讨论对象，作者引用其抗议场景（Q001、P007）。",
    "“仔细看一下这些图片（侵删）”“警察加入抗议队伍”：作者作为证据使用的图片与图注，图片内容本身未核验（P008、P009）。",
    "特朗普及“显著种族主义化的联邦政府”：作者批评与归责对象（P002、P003、P017）。",
    "卢旺达胡图族与图西族：作者用作“真正种族矛盾”的类比样本（P012）。",
    "《人权宣言》：作者用作美国统治精英背叛立国精神的对照物（P003）。",
    "中国：作者用作“不丢失自己核心价值也一样”的类比参照（P015）。"
   ],
   "conditions": [
    "条件句：“即使中国不做任何主动挑战，仅仅只是袖手旁观，只要美国自己修正不了自己的这种愚蠢走向……”（P005）。",
    "条件句：“只要还会有足够量的白人站在受害黑人一边抗议……你就可以说美国的种族歧视问题并没有到达真正危险的时刻”（P011）。",
    "条件句：“只要这些东西还在，美国这一世代的国祚就远未享尽”（P015）。",
    "条件句：“只要它的核心价值仍然被有效实践，其他国家就不能把‘彻底击败或者压倒’美国作为战略设想”（P016）。",
    "作者未给出“足够量”“有效实践”的量化标准。"
   ],
   "rhetoric_and_tone": "以“说几句公道话”开篇并自我定位为逆众声的持平者；对特朗普政府用“拿人权宣言当擦桌布用”“赤裸裸地背叛”等强贬义比喻；对“美国灵魂未死”一面转用庄重、格言式短句与排比条件句；末段以“坦率地说”作自我限定，语气由激烈转为克制。",
   "unresolved_questions": [
    "本篇含 8 个图片节点（IMG001—IMG008），图片内容未经核验，需人工或多模态复核；作者称白人参与抗议与“警察加入抗议队伍”的证据部分落在图片上。",
    "“足够量的白人”无量化标准，无法据本文判断何时到达“真正危险的时刻”。",
    "“它的核心价值仍然被有效实践”缺少可核查指标。",
    "提问者所述“跪压7分钟死亡”等事实细节本文未加核验，属待外部核查。",
    "文中“中国也一样”一句以类比方式带出对中国核心价值的判断，未展开论证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我打算为美国说几句公道话。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这个杀害黑人的警察、包庇遮掩的当地政府以及上至特朗普的这整个显著种族主义化的联邦政府，的确令人愤怒。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这帮人是在赤裸裸地背叛美国最初的立国精神和道德原则。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这东西是美国真正的力量源泉。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "美国不走下坡路、不挫折是不可能的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "也有其他肤色的人，尤其是有为数不少的白人。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "这并不是黑人和白人的种族间的矛盾，而是种族主义者（无论其有色无色）和反种族主义者（无论其有色无色）之间的矛盾。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "你就可以说美国的种族歧视问题并没有到达真正危险的时刻。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "真正的危险是所有的胡图族杀死所有的图西族。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "很多人以为发生这样的事情意味着美国不行了、衰落了，这不为错。", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P014", "quote": "也要看到美国的灵魂并没有死掉。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "只要这些东西还在，美国这一世代的国祚就远未享尽。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "只能将“互相敬畏、寻求最终和平共处”作为合理的规划目标。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "这并不是美国衰亡的开始的无可辩驳的证据——虽然这可能是特朗普这一系衰亡的开始。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["美国政治与社会", "种族问题", "国际关系与大国战略"],
   "issue_candidates": ["弗洛伊德事件定性", "种族主义与反种族主义之别", "美国是否衰落", "核心价值与国祚", "他国对美战略设想"],
   "text_function_candidates": ["时事评论", "论辩", "立场声明"],
   "object_candidates": ["美国", "特朗普", "美国联邦政府", "弗洛伊德", "白人抗议者", "胡图族", "图西族", "中国", "《人权宣言》"],
   "working_keywords": ["公道话", "立国精神", "道德原则", "种族矛盾", "核心价值", "国祚", "和平共处", "侵删"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 8 个图片节点（IMG001—IMG008，“仔细看一下这些图片（侵删）”“警察加入抗议队伍”），图片内容未经核验，故 status=needs_reread、image_checked=False；已读部分为正文文本（P001—P017 全部读完）。提问者所述事件细节与图中内容均属待外部核查，本记录不作事实裁决。"
 },
 "556022bb": {
  "analysis": {
   "question_context": "提问者问“你认为你天生就有吃动物的权利吗”（Q001，属提问者）。作者不直接回答该问，而把它转换为“人的自由到底边界在哪里”的伦理问题，给出以“能做到”和“能负担”为两项条件的自由定义，并据此说明吃动物已有选择的权利、真正要计算的是后果的管理与承担。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "作者把提问改写为“人的自由边界在哪”，并给出定义：自由即你能做到而且能负担后果的一切选择的集合，含“你能做到”与“你能负担”两个圆圈。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "“你能做到”覆盖一切物理学允许的可能性，包括吃动物、犯罪、被视为愚蠢之事，也包括体力好或财产多带来的自由；此处无道德审判或法律伦理约束，物理上能否办到才是限制。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "“你能负担”取决于对后果的预料和对自身负担能力的预料：无知者、无道德者因而有更多“实际的自由”，而相信自己承受不起的人自由更少。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "结论：负担得起本身就是一种做得到、一种能力；一切你力所能及的，都是你的权利。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "唯一限制是短期、中期、长期反馈的自然规律；作者强调道德律也是自然规律，并称这就是天赋之人权。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "回到本题：吃动物物理上做得到，已有选择的权利，需考虑的是管理与承担后果（管理指使部分后果不发生、并考虑所处环境的自我持续能力；承担指承担管理成本与失败后果），做完减法各人得出自己的结论，他人不能替代。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022"], "summary": "行动建议：不要再问“我是否有某种权利”或“该不该做某事”，应改问“做某事有哪些潜在的（负面）后果”或反对某事的理由；作者对这类问法及其提问者表示不耐烦。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把提问归结为“人的自由到底边界在哪里”，并给出定义：你的自由即你能做到而且你能负担后果的一切选择的集合。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“你能做到”意味着选择范围覆盖一切物理学所允许的可能性，其中不但包括吃动物，也包括一切人类视为犯罪而你有能力做到的事、被视为愚蠢的事，以及体力好或财产多带来的自由。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在“你能做到”的范围内不存在任何道德审判或者法律伦理约束，物理上能不能办到才是真正的限制。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“你能负担”取决于对选择后果的预料以及对自身负担能力的预料，因此无知的人常常拥有更多“实际的自由”。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有道德的人也常常拥有更多“实际的自由”，因为ta们不相信那背后存在不可逃避的后果。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "相信自己承受不起闲言碎语、得罪不起侵犯者或失去工作就再也找不到更好的人，因此拥有更少的自由。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“负担得起”本身就是一种“做得到”，就是一种能力。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切你力所能及的，都是你的权利。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "唯一限制你的是在一切短期、中期、长期向你反馈的自然规律；不要以为只有物理规律才是自然规律，而道德律就不是自然规律。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "回到本题：吃动物是你物理上做得到的，你就已经有了选择的权利；需要考虑的是吃动物所随附的各种后果你是否管理和承担得了。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "所谓管理指有没有能力使部分后果不发生（如通过宣传解说影响足够的人不敌视不追究，或去到这样的环境），并要考虑该环境是否有足够的自我持续能力。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓承担，是指承担做这些管理的成本，以及管理失败的后果。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人最终不能替代你做这个计算，也不能替你承担计算失败的后果，一切最终都看你自己。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以后不要再问“我是否有某种权利”或“该不该做某事”，因为追根到底他人的结论对你是没有意义的，只能作为观察他人逻辑的窗口。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这类问法常常问到的是一些逻辑不连贯、人格不成熟的小孩子的空洞立场，于是观察意义也有限。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应该问的是“做某事有哪些潜在的（负面）后果”，或者“如果你是反对xxx的，那么你的理由为何”。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "把提问者的“天生权利”之问改述为“人的自由到底边界在哪里”（P001）。",
    "给出定义：自由＝能做到且能负担后果的选择集合，分为“能做到”“能负担”两圈（P002—P003）。",
    "展开“能做到”：范围是一切物理学允许的可能性，含犯罪与被视为愚蠢之事，此层不受道德法律约束（P004—P005）。",
    "展开“能负担”：取决于对后果与自身负担能力的预料，并给无知、无道德、自认承受不起三类人的自由差异作例（P006—P009）。",
    "归结：负担得起即做得到，故一切力所能及的都是权利（P010—P012）。",
    "限定：唯一限制是自然规律，而道德律也属于自然规律（P013）。",
    "回到本题：吃动物物理上做得到，已有选择的权利，问题在后果的管理与承担（P015）。",
    "界定“管理”（使部分后果不发生、环境须自我持续）与“承担”（管理成本及失败后果）（P016—P017）。",
    "结论：减法由各人自己做，他人不能替代也不能代担（P018—P019）。",
    "行动建议：改问潜在负面后果或反对理由，而非问“是否有权利”（P020—P022）。"
   ],
   "concept_usage": [
    {"term": "自由", "meaning": "你能做到而且能负担后果的一切选择的集合；文中又区分“物理上能做到”与带引号的“实际的自由”。", "evidence": "P002", "ambiguity": "“能负担”依赖主观预料，作者未给出客观判准"},
    {"term": "权利", "meaning": "一切你力所能及的即是你的权利，与“天赋之人权”相连。", "evidence": "P012", "ambiguity": "与通常的法权／道德权利用法差别明显，作者未作辨析"},
    {"term": "自然规律", "meaning": "一切短期、中期、长期向你反馈的规律，作者明确把道德律也纳入其中。", "evidence": "P013", "ambiguity": "对“道德律是自然规律”本文只作断言，未给论证"},
    {"term": "管理", "meaning": "有没有能力使部分后果不发生，如通过宣传解说影响足够的人，或迁入合适环境，并须该环境能自我持续。", "evidence": "P016", "ambiguity": "“足够的人”“足够的自我持续能力”均未量化"},
    {"term": "承担", "meaning": "承担做管理的成本，以及管理失败的后果。", "evidence": "P017", "ambiguity": "承担能力的上限于文中未界定"}
   ],
   "examples_and_targets": [
    "吃动物：提问者的原问主题，作者用作物理可达性示例（Q001、P015）。",
    "喝硫酸、拿脑袋撞墙、跳火山口：作者举的“人类视为愚蠢”之事（P005）。",
    "偷国防电缆（因不了解安全法）、拿“公主病，哄一下就好了”解释女孩子心思：作者举的无知者“实际自由”例证（P007）。",
    "闲言碎语、虚张声势的侵犯者、失去这份工作：作者举的自认承受不起者的例证（P009）。",
    "跳到浮冰上安营扎寨、不停从浮冰跳向新浮冰：作者比喻环境缺乏自我持续能力（P016）。",
    "“逻辑不连贯、人格不成熟的小孩子”：作者对部分提问者的贬称（P021）。"
   ],
   "conditions": [
    "定义自带的双条件：自由须同时满足“能做到”与“能负担后果”（P002—P003）。",
    "“能负担”取决于预料，因此判断依主观认知而变（P007）。",
    "“唯一限制你的是……自然规律”，作者把道德律一并算作自然规律（P013）。",
    "管理须考虑所创造或加入的环境是否有足够的自我持续能力（P016）。",
    "作者称他人不能替代计算与承担，结论因此因人而异（P018—P019）。"
   ],
   "rhetoric_and_tone": "以“这答案是很简洁的”开场，用两圈图示式的二分展开定义；中段以“你也常常看到……”三次排比例证；转折用“换句话说”与英文句 Everything in your power, is in your right. 加重；末段转为不耐烦的劝告语气，直接给读者替换问法。",
   "unresolved_questions": [
    "提问者所问的“天生就有……权利”中的“天生”含义，作者未作回应，直接换成了物理可达性与后果负担的框架。",
    "“道德律也是自然规律”只有断言，没有给出论证或判准，属需研究者复核的关键歧义点。",
    "“能负担”依赖主观预料，本文未说明预料错误时如何计算。",
    "“足够的人”“足够的自我持续能力”无量化标准。",
    "作者称他人结论“对你是没有意义的”，但又称可作“观察他人的逻辑的窗口”，两者关系未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人的自由到底边界在哪里？", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你的自由即你能做到而且你能负担后果的一切选择的集合。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "这意味着你的选择范围覆盖了一切物理学所允许的可能性。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "也包括你的财产很多，于是你会拥有付酬请更多人帮你实现你的计划的自由。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "在这里不存在任何道德审判或者法律伦理约束。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "所以你常常看到无知的人有更多“实际的自由”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "你也常常看到没有道德的人拥有更多“实际的自由”。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你也常常看到一些人因此拥有更少的自由", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "实际上“负担得起”本身就是一种“做得到”，就是一种能力。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "一切你力所能及的，都是你的权利。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "唯一限制你的是在一切短期、中期、长期向你反馈的自然规律。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "吃动物是你物理上做得到的，你就已经有了选择的权利。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "所谓的管理，是指你有没有能力使得部分后果不发生", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "你显然不希望跳到一块浮冰上安营扎寨", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "所谓承担，是指承担做这些管理的成本，以及管理失败的后果。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "别人最终不能替代你做这个计算，也不能替你承担计算失败的后果", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "你以后也不要问什么“我是否有某种权利”或者“该不该做某事”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "人格不成熟的小孩子的空洞的（然而是“坚决的”）立场", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "你其实应该问“做某事有哪些潜在的（负面）后果”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／政治哲学", "动物权利与饮食伦理", "自由与权利理论"],
   "issue_candidates": ["自由的边界", "权利是否天生", "吃动物是否有权利", "后果的承担与管理", "道德律是否自然规律"],
   "text_function_candidates": ["答疑", "概念界定", "论辩"],
   "object_candidates": ["提问者（问吃动物权利者）", "无知的人", "没有道德的人"],
   "working_keywords": ["自由", "权利", "你能做到", "你能负担", "实际的自由", "自然规律", "道德律", "天赋之人权", "管理", "承担"]
  },
  "notes": "无图片节点。正文22段（P001—P022）全部读完；lexical 统计 paragraph 23，与阅读包段落标记一致（末段后有字符位空档，未见图文缺失）。Q001 属提问者，未计入作者主张。文中“道德律也是自然规律”等为作者断言，未附论证，登记为需研究者复核的歧义点，不作外部裁决。"
 },
 "44f8c341": {
  "analysis": {
   "question_context": "提问者问“我们可以讽刺无神论者和有神论者吗”（Q001，属提问者）。作者不区分讽刺对象是谁，直接否定讽刺本身：称讽刺是最低级的智慧、是对智慧最不体面的使用，把它归为欺凌，并劝人弃讽刺而不用；文末附《道德经》第三十一章原文以为依据。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开篇定性：讽刺是一种最低级的智慧，或者说是对智慧最不体面的使用。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "以金漆刷马桶、金丝楠木做赌筹为喻，承认物理与法律上可以，质问凭什么要这么做。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "连续追问：因别人错、傻、坏或你们都恨ta就可以讽刺吗，要求对方把论证说出来，并问讽刺基于什么理由可以是正当的。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "质问是否因讽刺是好用兵器而难以放弃，并引“佳兵不祥”“身怀利器，杀心自起”“放下屠刀，立地成佛”相劝。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "结论式告诫：若想穷尽一生最大的可能性，答案永远是“否”；可以耍宝、自嘲，但不要去追寻有毒的讽刺快感。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017"], "summary": "揭示讽刺的威力源泉是欺凌：以给看客快感作贿赂换取喝彩，误把喝彩当正义认证，实则与撒糖的校园恶霸无本质区别，得意值得羞耻。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P018", "P019", "P020"], "summary": "对“人所难免”“人之常情”与“讽刺是与邪恶斗争的有力武器”两类辩解作让步式反问，质疑其为正义战斗的实效。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022"], "summary": "正面行动建议：不喜欢就去做事反对它——正面对抗、侧面牵制、击垮前提、削弱辅助条件、磨缠啃顶，而不要去讽刺它；讽刺会让人误以为做了有效工作。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "论证喝彩不等于证明不正当：若能编出有人喝彩的讽刺即算“不正当的证明”，则世界上无正当可言；至圣先师、任何正义公平之事都能被刻薄讽刺找到花样。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P027", "P028"], "summary": "设问讽刺到底能证明什么，答：只能证明你缺快感来源、连没营养的东西也无法割舍。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036"], "summary": "对女性读者的专项告诫：分不清讽刺与幽默或不在乎的男性要远离，因为这种行为几乎肯定暗示将来的家暴，其辩护必是“你要不要这么敏感”，会把幸福、人格尊严、人身安全切片吃掉；幽默没有受害人，自嘲受害人是自己，明知故犯者敬而远之。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P037", "P038", "P039"], "summary": "解释“讽刺”在近现代中国被高度评价的原因：公共宣传中允许的讽刺几乎都是站在“我们”立场讽刺敌人，如相声小品以笑声为子弹对公众敌人公开处刑，于是讽刺被染上它自身并不具备的感情上的正义性；以悟空的金箍棒为类比。", "role": "reason"},
    {"unit_id": "U013", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "建议去听以中国为敌的脱口秀，体会角色互换后同样的逻辑；再跳出身份、到中立立场与两万英尺高空俯视，追问讽刺对敌人、对自己、对听众的净效果，以及它提高还是降低己方获胜概率，从而明白为何要弃讽刺。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P048", "P049", "P050"], "summary": "收束：做敌人也分品级，即使为敌也要做高贵的敌人；要反对就反对，不要讽刺。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P051", "P052"], "summary": "以引用块补入《道德经·卅一》全文，并说“补一段道德经，你们自己体会一下”。", "role": "context"},
    {"unit_id": "U016", "paragraph_refs": ["P053", "P054", "P055"], "summary": "回应“标新立异”“过于极端”的质疑：称两千多年前这话已经说出来了；承认讽刺是好兵器，但问到底有几个人真是“不得已”才用它。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讽刺是一种最低级的智慧，或者说是对智慧最不体面的使用。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讽刺在物理上当然可以、法律上也没后果，但作者反问凭什么要这么做。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者连续质问：因别人错、傻、坏或你们都恨ta就可以讽刺吗？到底基于什么理由，讽刺可以是正当的？", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者引“佳兵不祥”“身怀利器，杀心自起”“放下屠刀，立地成佛”等语，劝读者多想想。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "永远不要再问“我们可以不可以讽刺xxx”，因为如果你真的想要穷尽你一生最大的可能性，答案永远是“否”。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可以耍宝、可以自嘲，但只能是这样了，不要去追寻讽刺的快感，因为这是有毒的。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讽刺的真正威力源泉是：你其实是在欺凌，只是给看客足额的快感做贿赂以换取喝彩，并误把那喝彩当作对你正义的认证。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讽刺者自以为正义天诛，实则与小学校里给跟班撒糖的恶霸没有任何本质区别。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "悟得通的人会知道这种得意是一种值得羞耻的事。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：“人所难免”“人之常情”又如何，那就正当了吗？并质疑讽刺是否真是为正义战斗的好武器。", "evidence": ["E11", "E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不喜欢、不赞成什么事，就去做一些事去反对它：正面对抗、侧面牵制、击垮它的前提条件、削弱它的辅助条件、去磨去缠去啃去顶，而不要去讽刺它，因为那会让你误以为真的做了点什么有效的工作。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能讽刺、能得喝彩，对“证明这事不正当”没有任何实际意义；若喝彩可作为不正当的证明，则世界上还有任何正当可言吗？", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任是何等至圣先师、大智大贤、仁人志士，人要想讽刺都找得到下嘴处；无论何等正义、公平、正当的事，存心讽刺都能找到一百万种花样。", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讽刺只能证明你有多缺快感来源、以至于连这么没营养的东西也无法割舍。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者告诫姑娘们远离分不出讽刺和幽默的分界线、或分得清却根本不在乎的混蛋，因为这种行为几乎肯定的暗示着将来的家暴；其辩护几乎必定是“你要不要这么敏感”。", "evidence": ["E20", "E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这类人认定自己有牺牲他人“过度敏感”换自己精彩体验的正当权利，这条“公理”将来能把对方的幸福、甚至人格尊严、甚至人身安全当成香肠一片一片切来吃了。", "evidence": ["E22", "E23"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "幽默没有受害人，自嘲的受害人是自己；除此之外只能宽容一时不察，不能接受明知故犯，明知故犯者敬而远之。", "evidence": ["E24", "E25"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“讽刺”在近现代中国被高度评价的一大原因是：公共宣传中允许的讽刺几乎都是站在“我们”的立场上讽刺敌人，如相声小品以笑声为子弹对公众的敌人做公开处刑，讽刺因此被染上它自身并不具备的感情上的正义性。", "evidence": ["E26", "E27"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以悟空的金箍棒作类比：它本是武器，但台上总打妖怪，于是成了正义神兵，使用它成了不容置疑的正义行为，质疑它的成了正义之敌。", "evidence": ["E28"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议去听以中国为敌的脱口秀节目，以受讽刺对象的身份审视，再跳到中立立场、飞到两万英尺高空俯视整个讽刺问题，思考讽刺的净效果与它提高还是降低己方获胜概率。", "evidence": ["E29", "E30", "E31"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做敌人也分品级；即使决定要与对方为敌，也要做一个高贵的敌人；要反对就反对，不要讽刺。", "evidence": ["E32", "E33"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "面对“标新立异”“过于极端”的质疑，作者答称两千多年前这话已经说出来了，只是你们没听见而已。", "evidence": ["E34", "E35"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者承认讽刺当然是件好兵器，但反问到底有几个人真是“不得已”才用它。", "evidence": ["E36"]},
    {"claim_id": "C024", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "引用块《道德经·卅一》主张“夫佳兵者，不祥之器……不得已而用之，恬淡为上”，作者附言让读者自己体会。", "evidence": ["E37", "E38"]}
   ],
   "argument_steps": [
    "开篇给出定性判断：讽刺是最低级的智慧、对智慧最不体面的使用（P001—P002）。",
    "类比金漆刷马桶、金丝楠木做赌筹，承认物理与法律可行，转而追问正当性（P003）。",
    "用四组“因为别人错／傻／坏／你们都恨ta，于是就可以讽刺么？”加要求对方拿出论证，构成对讽刺正当性的连续反驳（P004—P008）。",
    "提出替代解释：讽刺是犀利、易获喝彩、有传播性的好用兵器，故难以放弃（P009）。",
    "引“佳兵不祥”等语（P010），给出答案“永远是‘否’”，并区分耍宝、自嘲与讽刺快感（P011—P012）。",
    "揭示讽刺的威力源泉为欺凌与对看客的快感贿赂，类比校园恶霸（P013—P015），以“值得羞耻”作评价（P017）。",
    "以“人所难免又如何”驳回常情辩解（P018），以“就算是为了某种正义吧”让步后质疑其实效（P019—P020）。",
    "给正面行动方案：正面对抗、侧面牵制、击垮前提、削弱辅助条件、磨缠啃顶（P021—P022）。",
    "论证“喝彩≠证明不正当”，并以至圣先师与一切正当之事皆可被讽刺作反证（P023—P026）。",
    "设问讽刺能证明什么，答为缺快感来源（P027—P028）。",
    "转向对女性读者的告诫：讽刺与家暴的关联预测、辩护话术“你要不要这么敏感”、幽默与自嘲的界限（P029—P036）。",
    "解释讽刺在中国近现代被高评价的公共宣传成因，以金箍棒类比（P037—P039）。",
    "给出亲身体验方法：听以中国为敌的脱口秀、以受讽刺对象身份审视、再跳到高空俯视，比较净效果与胜负概率（P040—P047）。",
    "收束为“做高贵的敌人”“要反对就反对，不要讽刺”（P048—P050）。",
    "以《道德经·卅一》引用块作支撑（P051—P052），回应“过于极端”之讥并保留“不得已”这一限定（P053—P055）。"
   ],
   "concept_usage": [
    {"term": "讽刺", "meaning": "作者指一种以进攻性取笑他人、靠给看客快感换取喝彩的行为，被定性为最低级的智慧与欺凌。", "evidence": "P001", "ambiguity": "作者未区分讽刺的对象、场合与程度，且明确拒绝按对象区分（P011）"},
    {"term": "佳兵不祥", "meaning": "引自《道德经》的成语，作者用以说明兵器虽利而不祥，讽刺亦同。", "evidence": "P010", "ambiguity": "作者把“兵”直接对应到“讽刺”属类比引用"},
    {"term": "威力源泉", "meaning": "作者指讽刺的力量来自欺凌，以及以快感贿赂看客换取喝彩的机制。", "evidence": "P013", "ambiguity": "未说明该机制是否为作者自创分析框架"},
    {"term": "幽默 / 自嘲", "meaning": "作者用作与讽刺相对的可接受行为：幽默没有受害人，自嘲的受害人是自己。", "evidence": "P035", "ambiguity": "幽默与讽刺的分界线如何判定，文中只以“受害人”为标准"},
    {"term": "净效果", "meaning": "作者要求从敌人、自己、听众三方衡量的总账，并落到己方获胜概率是提高还是降低。", "evidence": "P044", "ambiguity": "未给出衡量净效果的具体方法"},
    {"term": "不得已", "meaning": "作者承认讽刺作为兵器在“不得已”前提下可用（并引《道德经》“不得已而用之”）。", "evidence": "P055", "ambiguity": "“不得已”的条件未定义，与开头的整体否定存在张力"}
   ],
   "examples_and_targets": [
    "金漆刷马桶、金丝楠木做赌筹：作者类比材料（P003）。",
    "“佳兵不祥”“身怀利器，杀心自起”“放下屠刀，立地成佛”：作者引用的成语／佛语，属修辞与论据（P010）。",
    "小学校里给跟班撒糖的恶霸：作者类比对象（P015）。",
    "“讽刺是与邪恶斗争的有力武器”：作者设立并回应的对手说法（P019）。",
    "至圣先师、大智大贤、仁人志士：作者举出的可能被讽刺者（P025）。",
    "姑娘们／小男生们：作者直接称呼的告诫对象（P029—P030）。",
    "讽刺相声和小品：作者举的公共宣传实例（P038）。",
    "悟空的金箍棒：作者类比材料（P039）。",
    "以中国为敌的脱口秀节目：作者建议亲身体验的对象（P040—P041）。",
    "《道德经·卅一》全文：作者引用的典籍，置于 quote 段（P051）。",
    "“标新立异”“过于极端”：作者引述的他人对其评价，属被回应对象（P053）。"
   ],
   "conditions": [
    "让步条件：作者承认“就算是为了某种正义吧”，仍要追问讽刺是否真是好武器（P020）。",
    "限定条件：“不得已”才用讽刺可被《道德经》支持，但作者问有几人真是不得已（P055）。",
    "区分条件：耍宝、自嘲可以，讽刺的快感不可以（P012）。",
    "容忍边界：只能宽容一时不察，不能接受明知故犯（P035）。",
    "适用对象限定：关于家暴风险的告诫是对“姑娘们”说的（P029）。",
    "条件句：“如果你真的想要穷尽你一生最大的可能性，答案永远是‘否’”（P011）。"
   ],
   "rhetoric_and_tone": "训诫与讽刺性反问并重，且带有自我暴露的悖论色彩（以讽刺手法批评讽刺）：大量反问句“可以讽刺么？为什么？把你的论证大声说出来听听？”反复五次；用“有句大智慧的话送给你多想想”作劝导；用“你以为你是正义天诛”直斥；对女性读者用“姑娘们要切记”“敬而远之”的告诫口吻；末段以“真是我‘标新立异’，‘过于极端’么？”作自我辩护式收束。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001），图片内容未经核验，需人工或多模态复核；图片在结构上出现于文首附近，未在分段文本中给出对应说明。",
    "作者以大量讽刺性反问批评讽刺，其自身文本是否落入其所批评的行为，本文未作说明（研究者需注意此自我指涉）。",
    "“幽默”与“讽刺”的分界线仅以“有无受害人”界定，判定标准未细化。",
    "“将来会家暴”是对群体的预测性断言，文中未提供经验依据，属待外部核查。",
    "“不得已”使用讽刺的条件未界定，与开篇“讽刺是最低级的智慧”的强度存在张力。",
    "引用的《道德经·卅一》属典籍原文，作者只作类比使用，未逐句解释。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "讽刺是一种最低级的智慧。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "可以吗？物理上当然可以，法律上也没后果。但是，凭什么要这么做？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "因为别人错，于是就可以讽刺么？为什么？把你的论证大声说出来听听？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "到底基于什么理由，讽刺可以是正当的？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "佳兵不祥。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "因为如果你真的想要穷尽你一生最大的可能性，答案永远是“否”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "不要去追寻讽刺的快感——这是有毒的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "你其实是在欺凌，只是你给了看客们足额的快感做贿赂", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "实则和小学校里那些给跟班撒糖的恶霸没有任何本质区别", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "你会知道这种得意是一种值得羞耻的事。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "人所难免又如何？人之常情又如何？那就正当了吗？", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "讽刺就真的是为正义战斗的好武器吗？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "那就去做一些事去反对它，正面的去对抗它、侧面的去牵制它", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "因为那会让你误以为你真的做了点什么有效的工作。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "对“证明这事不正当”没有任何实际意义。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "那么世界上还有任何正当可言吗？", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "人要想讽刺，会找不到下嘴处吗？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "存心讽刺都能轻而易举的找到一百万种花样。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P028", "quote": "只能证明你有多缺快感来源", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "你们要切记离得他们远远的。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P031", "quote": "因为这种行为几乎肯定的暗示着将来的家暴。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P033", "quote": "他们理所当然的认定自己有牺牲他人的“过度敏感”换他们自己精彩体验的正当权利。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P034", "quote": "甚至人格尊严、甚至人身安全当成香肠，一片一片的切来吃了。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P035", "quote": "幽默没有受害人，自嘲的受害人是自己。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P036", "quote": "明知故犯者，敬而远之。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P037", "quote": "因为在公共宣传中被允许的讽刺，几乎都是站在“我们”的立场上在“讽刺”敌人。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P038", "quote": "那其实是以笑声为子弹对公众的敌人做的公开处刑。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P039", "quote": "任何质疑金箍棒的，就成了正义之敌。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P040", "quote": "我建议去听一下以中国为敌的脱口秀节目", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P044", "quote": "飞到20000英尺的高空往下俯视这整个讽刺的问题", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P046", "quote": "还是一种会降低己方获胜概率、抬高己方获胜成本的策略？", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P048", "quote": "做敌人也分品级。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P050", "quote": "要反对就反对，不要讽刺。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P053", "quote": "真是我“标新立异”，“过于极端”么？", "relation": "context"},
    {"key": "E35", "paragraph_id": "P054", "quote": "其实两千多年前这话已经说出来了，你们没听见而已。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P055", "quote": "讽刺当然是件好兵器，但到底有几个人真是“不得已”才用它？", "relation": "qualifies"},
    {"key": "E37", "paragraph_id": "P051", "quote": "《道德经 · 卅一》夫佳兵者，不祥之器。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P052", "quote": "补一段道德经，你们自己体会一下。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／道德批评", "修辞与言论方式", "传统文化经典引用"],
   "issue_candidates": ["讽刺是否可正当", "讽刺与幽默的界限", "讽刺与欺凌／家暴的关联", "公共宣传中的讽刺", "弃讽刺而用的行动替代"],
   "text_function_candidates": ["答疑", "批评", "训诫式论辩"],
   "object_candidates": ["无神论者与有神论者（提问者所述对象）", "提问者", "姑娘们", "小男生们", "《道德经》", "孙悟空（金箍棒）", "相声小品", "以中国为敌的脱口秀"],
   "working_keywords": ["讽刺", "最低级的智慧", "佳兵不祥", "威力源泉", "欺凌", "喝彩", "幽默", "自嘲", "净效果", "不得已", "高贵的敌人"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 1 个图片节点（IMG001，asset.sooon.ai/2020-06/03/…jpg），图片内容未经核验，故 status=needs_reread、image_checked=False；正文 P001—P055（含 1 个 quote 段与末段）已全部读完，已读部分为文本。P051 为引用块《道德经·卅一》原文，其观点归属 cited_source，未计作作者主张；P019 转述的“讽刺是与邪恶斗争的有力武器”为作者设立并回应的对手说法。"
 },
 "c6283199": {
  "analysis": {
   "question_context": "提问者问：倘若把世界重新构造，只留下善良智商高的人类，这个世界会不会变好（Q001，属提问者）。作者以“智商×勇气”的四组等式回应，指出“充足勇气”客观罕见，称该题设实为一项人类灭绝计划，并解释为何高智商加勇气只等于少许善良、低智商加勇气却是高度善良。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以“是这样的：”引出四组等式。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005"], "summary": "给出四组等式：高智商＋缺少勇气＝精明的邪恶；低智商＋缺少勇气＝愚蠢的邪恶；高智商＋充足勇气＝少许善良；低智商＋充足勇气＝高度善良。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "“充足勇气”客观罕见，绝大多数人只在安全感过剩时暂时拥有相对充足的勇气（“在善良既不危险、又不昂贵、且还够爽的时候，不妨且善良着”）；真善良者最起码要置生死于度外。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "而“置生死于度外的善良者”又毫无例外被认定为实践意义上的愚蠢。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "结论一：题设的这个假设其实是一项人类灭绝计划。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "预设有人会问第三第四等式为什么是这样，作者遂作解释。", "role": "transition"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014", "P015"], "summary": "善良在深思熟虑的决策和纪律严明的实施之下，是综合收益最大、最具有可持续性和扩张性的生存策略；越智力发达、阅历深刻、谋算深远，越看清其巨大回报率，于是越不需要道德勇气补足驱动力。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017", "P018"], "summary": "越成功实施，在旁观者眼里善良属性越强、输出能力越强，但真正的善良已在很大程度上被收益预期取代；这样做那样做更多是因为这样更好，而不是因为这样更对。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P019", "P020", "P021"], "summary": "反观阅历不深、智力未充分发展的笨拙者，缺乏善良的方法教育、不懂操作戒律、缺乏收益体验，仅凭相信这是对的就敢付出“穷人的一个铜板”，其实际善良程度远远高过老狐狸们，这就是第三第四等式如此的原因。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出四组等式：高智商＋缺少勇气＝精明的邪恶；低智商＋缺少勇气＝愚蠢的邪恶；高智商＋充足勇气＝少许善良；低智商＋充足勇气＝高度善良。", "evidence": ["E1", "E2", "E3", "E4"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“充足勇气”这个要素目前客观上非常罕见，无论高智商还是低智商，拥有充足勇气的人都是极少数。", "evidence": ["E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "绝大部分人只是在安全感过剩的时候暂时拥有相对充足的勇气，即“在善良既不危险、又不昂贵、且还够爽的时候，不妨且善良着”这种水平。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真善良者最起码也要置生死于度外，不然逻辑上只能是或五十步、或一百步的“且善着”派而已。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“置生死于度外的善良者”又毫无例外的被认定为实践意义上的愚蠢。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "题设的这个假设其实是一项人类灭绝计划。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "善良在深思熟虑的决策和纪律严明的实施之下，是综合收益最大、最具有可持续性和扩张性的生存策略。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你越是智力发达、阅历深刻、谋算深远，越是会意识到善良的细节和操作法则，越是能清晰看到它巨大的回报率。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "于是越不需要道德勇气来补足驱动力的不足——单纯逐利的驱动力已经非常大了。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "越是成功实施，你在旁观者眼里的善良属性越强、输出能力越强，而且举重若轻、高度自持。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "但你真正的善良已经在很大程度上被收益预期取代了；你这样做那样做更多是因为这样更好，而不是因为这样更对——它只是恰巧也对而已。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "阅历不深、智力还没有充分发展的笨拙者没有受到足够的善良的方法教育、不懂微妙复杂的操作戒律、也缺乏正确执行大有收益的体验，仅凭单纯相信这是对的就敢于付出“穷人的一个铜板”。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "ta们的实际善良程度反而要远远的高过老狐狸们，这就是为什么第三第四等式是这样。", "evidence": ["E17", "E18"]}
   ],
   "argument_steps": [
    "以四组“智商×勇气”等式给出善良与邪恶的分类（P001—P005）。",
    "指出“充足勇气”客观罕见，多数人只在安全感过剩时暂时有勇气（P006—P007）。",
    "给出真善良的门槛：最起码要置生死于度外（P008）。",
    "指出这类善良者被认定为实践意义上的愚蠢（P009）。",
    "据此判定题设＝人类灭绝计划（P010）。",
    "自设疑问并作解释（P011—P012）。",
    "解释路径：善良是收益最大、最可持续扩张的生存策略，智力越高越看清回报率，因而越不需要道德勇气（P013—P015）。",
    "让步与限定：成功实施使外显善良更强，但真正的善良已被收益预期取代（P016—P018）。",
    "反向对照：笨拙者缺乏方法教育与收益体验，仅凭“相信这是对的”就敢付出，故实际善良程度远高于老狐狸，这正是第三第四等式成立的原因（P019—P021）。"
   ],
   "concept_usage": [
    {"term": "勇气", "meaning": "使人在善良有危险、有代价时仍去行善的要素；作者以“充足勇气”为罕见变量，并以“置生死于度外”为真善良的门槛。", "evidence": "P006", "ambiguity": "“充足”未量化；“安全感过剩时暂时拥有”与真勇气的界线只在P008以置生死于度外作标尺"},
    {"term": "善良", "meaning": "在本文有两种层次：作为生存策略的善良（收益最大、可持续扩张）与需要道德勇气支撑的真善良（置生死于度外）。", "evidence": "P013", "ambiguity": "作者自承前者“真正的善良已经被收益预期取代”，两义并存易混"},
    {"term": "精明的邪恶 / 愚蠢的邪恶", "meaning": "缺少勇气时，高智商与低智商分别对应的两种邪恶形态。", "evidence": "P002", "ambiguity": "以等式形式给出，未说明是必然对应还是倾向性描述"},
    {"term": "且善着", "meaning": "在善良既不危险、又不昂贵、且还够爽时不妨且善良着的态度。", "evidence": "P007", "ambiguity": "文中P008又称之为“或五十步、或一百步的‘且善着’派”，带贬义"},
    {"term": "人类灭绝计划", "meaning": "作者对提问者题设的定性：只留下善良高智商者，实际后果指向灭绝。", "evidence": "P010", "ambiguity": "作者未展开该定性的推理链条"}
   ],
   "examples_and_targets": [
    "题设“只留下善良智商高的人类”：作者设定并反驳的对象（Q001、P010）。",
    "“在善良既不危险、又不昂贵、且还够爽的时候，不妨且善良着”：作者引述并贬抑的普通人态度（P007）。",
    "“穷人的一个铜板”：作者形容笨拙者付出的代价（P019）。",
    "老狐狸们：作者对阅历深、谋算深者的贬称（P020）。",
    "“或五十步、或一百步”：作者借用成语形容“且善着”派（P008）。"
   ],
   "conditions": [
    "限定词：“目前客观上非常罕见”——关于勇气稀缺的判断带时间限定（P006）。",
    "条件：“在安全感过剩的时候暂时拥有相对充足的勇气”（P007）。",
    "门槛条件：真善良者“最起码也要置生死于度外”（P008）。",
    "前提条件：“善良，在深思熟虑的决策和纪律严明的实施之下”——善良的收益最大性依赖该前提（P013）。",
    "程度条件：“在很大程度上被收益预期取代”保留程度限定（P017）。",
    "作者未说明该四组等式适用于何种人群范围与情境。"
   ],
   "rhetoric_and_tone": "以等式与数学符号式的排版给出命题，语气断然、格言化；用“是这样的：”“那就解释一下。”短句控制节奏；对普通人的善良用“且善着”“老狐狸们”等带讥讽意味的称呼；对笨拙者用“穷人的一个铜板”作褒义化修辞；整体呈训诫式的断言体，少用反问。",
   "unresolved_questions": [
    "“充足勇气”的判定标准与测量方式未说明，四组等式因此难以操作化。",
    "“人类灭绝计划”是对题设的定性，作者未给出推理步骤，读者无法据本文复核该结论。",
    "“善良是综合收益最大、最具有可持续性和扩张性的生存策略”属事实性断言，未附经验依据，待外部核查。",
    "文中“善良”同时指策略性善良与置生死于度外的真善良，二者关系（是否同一概念的两面）未说明。",
    "提问者题设中的“智商高”与作者使用的“高智商”是否同义，未作辨析。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "高智商 + 缺少勇气 = 精明的邪恶", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "低智商 + 缺少勇气 = 愚蠢的邪恶", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "高智商 + 充足勇气 = 少许善良", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "低智商 + 充足勇气 = 高度善良", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "“充足勇气”这个要素，目前客观上非常罕见。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "在善良既不危险、又不昂贵、且还够爽的时候，不妨且善良着", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "真善良者，最起码也要置生死于度外。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "毫无例外的被认定为实践意义上的愚蠢。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "题设的这个假设其实是一项人类灭绝计划。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "是综合收益最大、最具有可持续性和扩张性的生存策略。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "而且越是能清晰的看到它巨大的回报率。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "于是越不需要道德勇气来补足你的驱动力的不足", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "而且举重若轻、高度自持。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "但是你真正的善良已经在很大程度上被收益预期取代了。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P018", "quote": "更多的是因为这样更好，而不是因为这样更对", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "仅仅凭着单纯的相信这是对的，就敢于付出“穷人的一个铜板”。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "ta们的实际善良程度反而要远远的高过老狐狸们。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "这就是为什么第三第四等式是这样。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／人性论", "社会思想实验", "智力与道德关系"],
   "issue_candidates": ["只留善良高智商者是否会变好", "勇气与善良的关系", "善良是否为生存策略", "真善良的门槛", "智力和道德的关系"],
   "text_function_candidates": ["答疑", "反驳题设", "命题式论断"],
   "object_candidates": ["提问者（题设提出者）", "高智商者与低智商者", "老狐狸们（阅历深者）", "笨拙的人们"],
   "working_keywords": ["勇气", "智商", "精明的邪恶", "愚蠢的邪恶", "真善良", "且善着", "置生死于度外", "人类灭绝计划", "生存策略", "回报率"]
  },
  "notes": "无图片节点。正文20段（P001—P021，P001为“是这样的：”引出句）全部读完；lexical 统计 paragraph 21，与段落标记一致。Q001 属提问者，作者对题设的定性（P010）已按 author_explicit 记录，未与提问者立场混同。文中关于“善良是收益最大的生存策略”“充足勇气罕见”等属作者断言，未附经验依据，登记为待外部核查。"
 },
 "6a0e9e07": {
  "analysis": {
   "question_context": "提问者问“宇宙里的真空到底是什么”（Q001，属提问者）。作者以“空，并不是无”作答：把空比作一张没写字的纸，主张空虽无一物却有一切物的规则（自然规律），并反驳“宇宙中没有真正的真空”这一流行说法，称宇宙本来就是空的、只是空得不均匀。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出核心区分：空，并不是无。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "以“一张没写字的纸”作喻：虽没有字，但既然是一张纸，就决定了什么能留下字迹、什么不能。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "空虽无一物，却有一切物的规则：真空中一个粒子都没有，但存在着圆周率、普朗克常量，事实上有一切自然规律。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "类比：在新疆戈壁滩上画一个圆，里面一个中国人也没有，但却有中国的法律。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "反面界定：无则是连这张纸也没有；重申空并不是无。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P008", "P009"], "summary": "反驳流行说法：很多人说“宇宙中没有真正的真空”，这是错的；哪怕把暗物质都算上，“实体”占据的空间仍是宇宙中极小的一部分。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P010"], "summary": "进而主张宇宙本来就是空的，只是空得不均匀。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P011", "P012", "P013"], "summary": "以“疙瘩汤里咬不动的才算有料”与“斑马是白底之上有斑”为喻，指人类只把可见实体算作存在；作者把这种不自觉的简化归因于人类总体思维能力的欠缺。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "空，并不是无。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "空是一张没写字的纸：虽然没有字，但既然是一张纸，就决定了什么能留下字迹、什么不能。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "空虽无一物，但却有一切物的规则。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "虽然一片真空里一个粒子都没有，但却存在着圆周率，也存在着普朗克常量——事实上，它有一切自然规律。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "类比：这就像在新疆戈壁滩上画一个圆，里面一个中国人也没有，但是却有中国的法律一样。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无则是连这张纸也没有；空并不是无。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定流行说法：“宇宙中没有真正的真空”是错的——哪怕把暗物质都算上，“实体”所占据的空间仍然是宇宙中极小的一部分。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "甚至可以说宇宙本来就是空的，只是空得不均匀。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类误把疙瘩汤里咬不动的那些才算做有料，这本质上如同认定斑马是白底之上有斑、黑斑的部分才算存在。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这其实是人类的总体思维能力的欠缺造成的不自觉的简化。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "直接给出判断：空不是无（P001）。",
    "以“一张没写字的纸”作喻说明空规定了可能与不可能（P002）。",
    "推进一步：空虽无一物却有一切物的规则（P003）。",
    "举真空中的圆周率、普朗克常量为例，称其有一切自然规律（P004）。",
    "以新疆戈壁滩画圆与中国的法律作类比（P005）。",
    "反面界定“无”（连纸也没有），重申命题（P006—P007）。",
    "反驳“宇宙中没有真正的真空”，以实体（含暗物质）占比极小为理由（P008—P009）。",
    "给出正面主张：宇宙本来就是空的，只是空得不均匀（P010）。",
    "以疙瘩汤、斑马两喻解释人类为何误认只有实体算存在（P011—P012）。",
    "归因：这是人类总体思维能力欠缺造成的不自觉简化（P013）。"
   ],
   "concept_usage": [
    {"term": "空", "meaning": "不是无，而是“一张没写字的纸”，即一无所有但已规定了一切物的规则、蕴含一切自然规律的状态。", "evidence": "P002", "ambiguity": "作者以纸、圆与法律作比喻性界定，未给出物理定义"},
    {"term": "无", "meaning": "连“这张纸”也没有，与“空”相对。", "evidence": "P006", "ambiguity": "作者未说明“无”是否可能实际存在，也未与传统哲学的无作辨析"},
    {"term": "一切物的规则 / 自然规律", "meaning": "真空中仍然存在的东西，作者举圆周率与普朗克常量为代表。", "evidence": "P004", "ambiguity": "把数学常量与物理常量并列为“自然规律”，未作区分"},
    {"term": "实体", "meaning": "作者加引号使用，指占据空间的物质，包括暗物质在内仍只占极小部分。", "evidence": "P009", "ambiguity": "“实体”的界定与暗物质是否属实体，文中未展开"},
    {"term": "不自觉的简化", "meaning": "人类因总体思维能力欠缺，把“有料”等同于可见可触的实体。", "evidence": "P013", "ambiguity": "属心理学式归因，无证据支撑"}
   ],
   "examples_and_targets": [
    "圆周率、普朗克常量：作者举作真空中仍然存在的规则（P004）。",
    "新疆戈壁滩上画一个圆、里面的中国的法律：作者类比材料（P005）。",
    "“宇宙中没有真正的真空”：作者明确反驳的流行说法（P008）。",
    "暗物质：作者反驳时纳入计算的对象（P009）。",
    "疙瘩汤里咬不动的：作者比喻材料（P011）。",
    "斑马是白底之上有斑：作者比喻材料（P012）。"
   ],
   "conditions": [
    "让步式条件：“哪怕你把暗物质都算上”——结论在把暗物质计入后依然成立（P009）。",
    "限定词：“甚至可以说”，表明宇宙本来就是空的属强化表述（P010）。",
    "类比条件：新疆戈壁滩与中国的法律之比为比喻，并非实际论证（P005）。",
    "作者未限定所谈真空的尺度（量子真空、宇宙学真空等）与物理框架。"
   ],
   "rhetoric_and_tone": "短句、定义式断言与比喻并用，语气通俗笃定；以“空是一张没写字的纸”等日常意象解释抽象问题；“疙瘩汤”“斑马”两喻带调侃色彩；末句转入对人类思维能力的直评，措辞稍带贬抑（“欠缺”“不自觉的简化”）。",
   "unresolved_questions": [
    "作者未说明所论真空属于何种物理含义（量子场论真空、宇宙学空洞等），其“空有一切自然规律”的说法是哲学式表述还是物理主张，本文未界定。",
    "把圆周率、普朗克常量与“自然规律”并置，未区分数学对象与物理常量。",
    "“宇宙本来就是空的，只是空得不均匀”未给出尺度或判据。",
    "“人类总体思维能力的欠缺”属心理学／人类学断言，未附依据，待外部核查。",
    "“新疆戈壁滩……有中国的法律”在法律与主权适用范围上的类比效力，作者未讨论。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "空，并不是无。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "空是一张没写字的纸。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "空虽无一物，但却有一切物的规则。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "虽然一片真空里一个粒子都没有，但却存在着圆周率，也存在着普朗克常量", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "事实上，它有一切自然规律。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "里面一个中国人也没有，但是却有中国的法律一样。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "无则是连这张纸也没有。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "空并不是无。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "很多人在说“宇宙中没有真正的真空”，这是错的。", "relation": "contradicts"},
    {"key": "E10", "paragraph_id": "P009", "quote": "“实体”所占据的空间仍然是宇宙中极小的一部分。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "甚至可以说宇宙本来就是空的，只是空得不均匀。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "人类误把疙瘩汤里咬不动的那些才算做有料罢了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "黑斑的部分才算存在，白底则被视为“没有花纹”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "这其实是人类的总体思维能力的欠缺造成的不自觉的简化。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["物理学（真空概念）", "自然哲学／本体论", "科学普及"],
   "issue_candidates": ["真空到底是什么", "空与无的区别", "真空中是否存在自然规律", "宇宙是否本来就是空的", "人类为何只承认实体"],
   "text_function_candidates": ["答疑", "概念解释", "科普式论辩"],
   "object_candidates": ["宇宙", "真空", "暗物质", "新疆戈壁滩", "斑马", "人类（总体思维能力）"],
   "working_keywords": ["真空", "空", "无", "一切物的规则", "自然规律", "圆周率", "普朗克常量", "实体", "不均匀", "不自觉的简化"]
  },
  "notes": "无图片节点。正文13段（P001—P013）全部读完，与 lexical 统计 paragraph 13 一致。本题原属物理学问题，作者以比喻与哲学式断言作答（纸、戈壁滩画圆、疙瘩汤、斑马）；文中涉及圆周率、普朗克常量、暗物质等事实性内容未附出处，登记为待外部核查，本记录不作事实裁决。"
 },
 "fec831da": {
  "analysis": {
   "question_context": "提问者问“为什么垃圾男追求遭到女方委婉拒绝还继续追不放弃呢”（Q001，属提问者）。作者先剥离“农村男”“城市女”等身份变量，把判定条件归为【追】＋【拒绝】＋【不放弃】，再论证设置排除性条件必须是一辈子不会妥协的条件，并把“不尊重我明确的拒绝的意愿”确立为唯一且足够的绝对排除条件，最后给出爱的实践性定义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "把提问拆为关键词，主张判定“不予考虑”只需【追】＋【拒绝】＋【不放弃】，其他关键词是多余变量。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "拒绝不是因为对方是农村男，也不是因为你是城市女——这根本不重要。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "不应限定理想人选的来源与必须经济条件相当：佳偶本就难求，附加条件更难求；一个条件就足以使概率减半，有的条件一条就排除地球上绝大部分人；设定排除性条件须万分谨慎。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "要求自问能否为全部筛选条件坚守孤独、或只能坚守到38岁、45岁；若注定在38或45岁被放弃，其“净帮助”只是平白剥夺此前的幸福可能。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "结论：排除条件必须是一辈子都不会妥协的、非身份的、与做人原则和爱的本质直接相连的条件；“不尊重我明确的拒绝的意愿”是绝对排除条件，且只要这一条就够了。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "给出拒绝理由的表述：不是因你是农村男，而是因我不接受口说爱我的人不尊重我拒绝的意愿；说了“不”还要纠缠，就已证明不在乎我的意愿。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "以四组“或者你是认为……”追问：认为我的意愿可被说服、心智愚蠢可用计谋摆平、意志软弱可用要挟威逼、对自己轻率可用死缠烂打解决，均不构成托付理由。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020"], "summary": "这与你的判断是否符合客观事实无关：无论我是否真的幼稚／愚蠢／软弱／轻率，有资格爱我的人不会做利用这些弱点来管理我的设想。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P021"], "summary": "提出爱的实践性定义：不故意利用我作为人类必有的弱点来寻求自己的利益。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "收束：拒绝你不是因为你是农村男或我是“城市女”，而是不打算托付给想利用我弱点牟利的人；这条标准无可妥协，并重复强调。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要达成“不予考虑”的判定，只需要【追】＋【拒绝】＋【不放弃】就足够了，其他的关键词是多余的变量，不需要纳入考虑。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "拒绝不是因为对方是农村男，也不是因为你是城市女——这根本不重要。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你不能限定理想人选不可以来自农村，也不可以限定对方一定要经济条件与你相当。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "佳偶本就难求，附加限制条件只会更难求：一个条件加上去就足以把自己得遇良人的概率减半，再加一条再减半，有些条件一条就排除了地球上的绝大部分人。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你必须要对设定排除性条件万分谨慎，否则几个“起码条件”斩下去，你已经先立于难胜之地了。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者要求自问：真的能受得了为全部筛选条件坚守孤独吗？还是只能为此坚守到38岁、45岁？", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果这些条件注定会在你38岁或者45岁时被放弃，那么它们给你的“净帮助”就只是平白无故剥夺了你38、45岁之前的幸福可能。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要设立排除条件，必须是一辈子都不会妥协的条件，是那种没得妥协的、非身份的、与做人原则、与爱的本质直接相连的条件。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“不尊重我明确的拒绝的意愿”是一条绝对排除条件，而且只要这一条就够了。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我拒绝你，不是因为你是农村男，而是因为我不接受口说爱我的人不尊重我拒绝的意愿。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我说了“不”，你还要纠缠，你就已经证明了你不在乎我的意愿。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问拒绝四类托付理由：视我的意愿为幼稚可供说服、视我心智愚蠢可用计谋摆平、视我意志软弱可用要挟威逼妥协、视我对自己轻率可用死缠烂打解决。", "evidence": ["E14", "E15", "E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这跟你的判断是否符合客观事实无关：无论我是否真的幼稚／愚蠢／软弱／轻率，有资格爱我的人不会做利用这些弱点来管理我的设想。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不故意利用我作为人类必有的弱点来寻求自己的利益，这是爱的一种实践性的定义。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "为什么拒绝你？不是因为你是农村男，也不是因为我是“城市女”，而是因为我不打算托付给一个想要利用我的弱点来牟利的人。", "evidence": ["E21", "E22"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这条标准无可妥协（文中两次陈述以加重）。", "evidence": ["E23", "E24"]}
   ],
   "argument_steps": [
    "把提问拆成关键词，剔除【农村男】【城市女】等“多余变量”，只留【追】＋【拒绝】＋【不放弃】（P001—P002）。",
    "明确否认拒绝与双方地域／城乡身份有关（P003）。",
    "提出不应限定理想人选的来源与经济条件相当（P004）。",
    "以概率减半论证附加条件的代价，要求对排除性条件万分谨慎（P005—P007）。",
    "要求自问能否为条件坚守孤独、或只能坚守到38／45岁，并指出此时条件只有剥夺幸福的作用（P008—P010）。",
    "给出标准：排除条件必须是一辈子不会妥协的、非身份的、与做人原则和爱的本质相连的条件（P011）。",
    "据此确立绝对排除条件：“不尊重我明确的拒绝的意愿”，且只需这一条（P012）。",
    "以第一人称重述拒绝理由（P013），并指出纠缠即证明不在乎意愿（P014）。",
    "用四组反问排除“说服／计谋／要挟／死缠烂打”四种托付理由（P015—P018）。",
    "强调结论与客观事实无关，落到“有资格爱我的人不会利用我的弱点管理我”（P019—P020）。",
    "给出爱的实践性定义（P021）。",
    "收束：拒绝的理由是不打算托付给想利用弱点牟利的人，标准无可妥协（P022—P025）。"
   ],
   "concept_usage": [
    {"term": "不予考虑的判定", "meaning": "作者指只需【追】＋【拒绝】＋【不放弃】三要素即可作出的决定，身份变量无需纳入。", "evidence": "P002", "ambiguity": "是在回答提问者“为什么还继续追”的问题，而非评定某个人"},
    {"term": "排除性条件 / 绝对排除条件", "meaning": "筛选伴侣时设定的排除标准；作者要求其必须一辈子不妥协、非身份、与做人原则和爱的本质相连。", "evidence": "P011", "ambiguity": "“一辈子不会妥协”如何预先判定，文中未说明"},
    {"term": "净帮助", "meaning": "作者自造说法，指筛选条件在被放弃前对当事人的实际收益（结论为净损失）。", "evidence": "P009", "ambiguity": "只在38／45岁假设下计算，未给出普遍算法"},
    {"term": "爱（实践性的定义）", "meaning": "不故意利用我作为人类必有的弱点来寻求自己的利益。", "evidence": "P021", "ambiguity": "作者自称为“实践性的定义”，未讨论与情感层面之爱的关系"},
    {"term": "纠缠 / 死缠烂打", "meaning": "已明确拒绝后仍继续追求的行为；作者视其为不尊重意愿的证据。", "evidence": "P014", "ambiguity": "与“继续追”在何程度上等同，文中未划界"}
   ],
   "examples_and_targets": [
    "【农村男】【城市女】：提问者问题中的关键词，作者设为多余的、应剔除的变量（P001—P003、P022）。",
    "38岁、45岁：作者举出的可能放弃条件的年龄（P008—P010）。",
    "四类“或者你是认为……”：作者设想并反驳的追求者心态（P015—P018）。"
   ],
   "conditions": [
    "条件句：“如果这些条件注定会在你38岁或者45岁时被放弃”（P009）。",
    "限定：“必须是一辈子都不会妥协的条件”（P011）。",
    "限定：“这跟你的判断是否符合客观事实无关”（P019）。",
    "范围限定：作者以第一人称“我”陈述拒绝理由，其结论适用于“有资格爱我的人”这一关系（P014、P020）。",
    "适用对象：本文面向提问者所描述的追求情境（已明确拒绝后仍继续追）。"
   ],
   "rhetoric_and_tone": "以拆解关键词的方式冷静起手，中段转为连续反问与排比（四组“或者你是认为……我为什么要把自己托付给……”）逼近结论；用“对不起，这条标准无可妥协。”与“记住，这条标准无可妥协。”重复同一句作收束，语气坚决、带训诫性；对“农村男／城市女”标签反复否认，并反问“你自己也不愿意吧？”以争取读者认同。",
   "unresolved_questions": [
    "作者自述“这句话里一共这么几个关键词：【农村男】【追】【城市女】……”，但提问字段实际只问“为什么垃圾男追求遭到女方委婉拒绝还继续追不放弃”，其中“垃圾男”一词未在正文中被处理，追问的关键词与题面存在差异，需研究者复核（可能依据平台完整题面或回答内嵌的提问版本）。",
    "“一个条件加上去就足以把自己得遇良人的概率减半”是数量化断言，未给出依据，待外部核查。",
    "38岁、45岁为举例性年龄，未说明其依据。",
    "“爱的实践性的定义”是否穷尽作者对爱的理解，本文未说明。",
    "文中未说明若拒绝表达不够明确（非“明确的拒绝”）时结论是否改变。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "只需要【追】+【拒绝】+【不放弃】就足够了。其他的关键词是多余的变量，不需要纳入考虑。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "拒绝不是因为对方是农村男，也不是因为你是城市女。这根本不重要。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "你不能限定理想人选不可以来自农村，也不可以限定对方一定要经济条件与你相当。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "佳偶本就难求，你还附加别的限制条件，那不是更难求了吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "一个条件加上去就足以把自己得遇良人的概率减半，再加一条再减半。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你必须要对设定排除性条件万分谨慎", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "还是说你只能为此坚守到38岁？45岁？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "如果这些条件注定会在你38岁或者45岁时被放弃，那么它们给你的“净帮助”是什么？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "是平白无故的剥夺了你38、45岁之前的幸福可能罢了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "要设立排除条件，必须是一辈子都不会妥协的条件。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这就是为什么“不尊重我明确的拒绝的意愿”是一条绝对排除条件。而且只要这一条就够了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "而是因为我不接受口说爱我的人不尊重我拒绝的意愿。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "你就已经证明了你不在乎我的意愿。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "是可以供你“说服”的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "是可以用计谋摆平的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "是用要挟威逼妥协的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "是可以用死缠烂打来解决的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "这跟你的判断是否符合客观事实无关。", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P020", "quote": "有资格爱我的人ta不会做利用这些弱点来管理我的设想。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "不故意利用我作为人类必有的弱点来寻求自己的利益，这是爱的一种实践性的定义。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "不是因为你是农村男，也不是因为我是“城市女”。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "而是因为我不打算托付给一个想要利用我的弱点来牟利的人", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P024", "quote": "对不起，这条标准无可妥协。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P025", "quote": "记住，这条标准无可妥协。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋与人际关系", "伦理学（爱与尊重）", "性别与交往边界"],
   "issue_candidates": ["被拒后仍追是否可接受", "择偶排除条件的设置", "拒绝意愿的尊重", "爱的实践性定义", "城乡身份是否应作为择偶变量"],
   "text_function_candidates": ["答疑", "论辩", "行动建议"],
   "object_candidates": ["提问者（问“垃圾男”者）", "农村男", "城市女", "被追求者", "追求者"],
   "working_keywords": ["追", "拒绝", "不放弃", "多余变量", "排除性条件", "净帮助", "明确的拒绝的意愿", "绝对排除条件", "弱点", "爱"]
  },
  "notes": "无图片节点。正文25段（P001—P025）全部读完，与 lexical 统计 paragraph 25 一致。注意：正文P001自述的问题是“【农村男】【追】【城市女】【遭到女方委婉拒绝】还【继续追不放弃】”，而本批语料的 question 字段为“为什么垃圾男追求 遭到女方委婉拒绝 还继续追不放弃呢?”——“垃圾男”一词在正文中未被处理，且正文出现题面未含的“农村男／城市女”，疑回答对应平台完整题面或题面有版本差异，登记于 unresolved_questions 待研究者复核；本条不据此改动作者主张。"
 },
 "df738bff": {
  "analysis": {
   "question_context": "提问者问“老公年薪百万的话你愿意全职吗”（Q001，属提问者）。作者认为这没有原则上的问题，回答“不行”者低估了家庭管理的水平与价值；他先指出中国家庭理想仍以自耕农之家为模板，故产生“家庭主妇微不足道”的误解，再说明现代中产家庭管理的复杂度与专业要求，最后补充两点限定：一是“可做／能做成甚好”而非“必做”，二是一切事情都可做、但须有正确的前提。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开篇判断：这没有原则上的问题；回答“不行”的人只是不清楚家庭可以管理得多好、也不清楚经营良好的家庭本身的价值。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "归因：中国的家庭标准模版落后得惊人，客观上以自耕农的家庭为理想，更高的家庭管理水平和更复杂的家庭政务不在一般人常识中；自耕农家庭模型下家庭主妇没有发挥空间，家务极简、资产有限、对子女期望甚低。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "现实变化：现在家庭有一两百万净资产绝不在少数，甚至是一二线城市普通家庭的常态；家庭面对的社会关系、家族挑战、子女教育挑战远非五六十年前雇农想象的自耕农之家可比。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "评价：能管理好一两百万现金和不动产、处理好社会关系、解决子女教育、调理家庭内环境的合格专业人才，其价值、专业知识与人格强健程度远非一般公司中层白领可比，总监一级也没有几个真能平起平坐。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "推论与前提：能管理好现代中产家庭的“家庭主妇”放下婴儿车就能经营起一家业务相当健康的小企业；前提是她要积极主动、自觉、进取地自我发展。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "稀缺性与能力对照：专业有效的家庭主妇远比“年薪百万的丈夫”稀缺；生活点滴中果断正确的处置会让高级社畜敬畏，因为其团队做不到这样的效率和细致。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015"], "summary": "对丈夫一侧的反讽式提醒：丢开你这累赘，人家只会一飞冲天；到底谁嫌弃谁还不一定。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017"], "summary": "转向自问：真正的问题是问问自己，你的“家庭主妇”是怎么当的？是在当家庭主妇，还是在从头当闺女、当宠物？", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P018"], "summary": "明确要求停止喊叫“坚决不能当家庭主妇”，并说那是错的。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P019", "P020"], "summary": "补充说明起点：这里说的是“可做 / 能做成甚好”，而不是“必做”。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "指出中文舆论场的防御性心态：生怕一件事被论证合理就会被列为非做到不可，于是毫无理智地阻击一切合理性论证（以“读大学是合理的人生计划”为例），并连续反问凭什么“合理的”就是“必须的”、为何不能忍受自己没做一切合理之事；作者称这种强迫性逻辑跳跃是心灵创伤，想清楚可让视野放宽三四成。", "role": "rebuttal"},
    {"unit_id": "U012", "paragraph_refs": ["P031", "P032"], "summary": "第二点重申：一切事情都可做，只要有正确的前提；这是不应需要专门强调的默认预设。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P033", "P034"], "summary": "批评把问题篡改成“（无需任何前提）可做／不可做”是人生选择狭窄化的根源；解决问题者更能解决问题的一大优势，在于ta们会去寻找使事情可行的前提，而非仅按平均条件判定。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039"], "summary": "格言式总结：基于“平均水平”凡事皆不可做，因为看似可完成整个动作却无足够利润对冲风险；一事可做必有其“不平均”之处；不要被“正常”捆住手脚，因为正常人不幸福，幸福本身就是一种超常。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P040", "P041", "P042"], "summary": "结论：有称职全职家庭主妇的家庭远强过有双份收入却无有效家政管理的家庭；家庭（尤其有发育家族打算的）决策不宜假手于雇员，雇员的忠诚与能干不能替代主人职责，这份职责不可外包。", "role": "conclusion"},
    {"unit_id": "U016", "paragraph_refs": ["P043", "P044", "P045"], "summary": "对丈夫一方的条件：这份素养和收入没关系，更多是觉悟水平；对方没有这份觉悟当然不能勉强，反而要自己拒绝当家庭主妇；但若对方有觉悟，因社会低水平家庭熏陶出的恐惧心而强迫性选择不做，同样是自己的绝对损失。", "role": "qualification"},
    {"unit_id": "U017", "paragraph_refs": ["P046", "P047"], "summary": "以姚明作职业球员规划为类比：按一般人身体条件不应以此为规划，但如果你是姚明，去听他们的就是欠抽。", "role": "example"},
    {"unit_id": "U018", "paragraph_refs": ["P048", "P049"], "summary": "文末附注：“另外，把这个看掉再回来看这篇”，并给出“家族答集”链接文本（该段被标注为 lexical 未覆盖片段）。", "role": "context"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这没有原则上的问题；回答“不行”的人只是不清楚一个家庭可以管理得有多好，以及不清楚一个经营良好的家庭本身的价值。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的家庭标准模版落后得惊人，它差不多只是雇农们对无需交租、自有耕地的自耕农的家庭的想象。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因特殊历史原因，中国目前传承的家庭理想客观上以自耕农的家庭为理想，更高的家庭管理水平和更复杂的家庭政务的理解不在一般人的常识之中，不管感想如何这就是事实。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为这个认知才产生了“家庭主妇微不足道”的误解：自耕农家庭模型中家庭主妇没有发挥空间，家务极简、资产有限、对子女期望甚低。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在的家庭有一两百万净资产的绝不在少数，这甚至只是一二线城市普通家庭的常态。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家庭要面对的社会关系、人际关系的动荡、家庭内部与家族各方面的挑战、子女教育的挑战，远非五六十年前雇农们想象中的自耕农之家所能比拟。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能管理好一两百万现金和不动产、处理好所有社会关系、解决好子女教育、调理好家庭内环境的合格专业人才，其创造的价值、专业知识与人格强健程度都远非一般的公司中层白领所能比拟。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "甚至就是总监一级也没有几个真的能平起平坐的。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "能管理好现代中产家庭的“家庭主妇”，放下婴儿车就能经营起一家业务相当健康的小企业，专业技能与心理素质都完全过关——前提是她要积极主动、自觉、进取地自我发展。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个世界上，专业有效的家庭主妇远远要比“年薪百万的丈夫”稀缺得多。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生活点滴里流露出的果断而正确的处置，每一条都会让高级社畜们敬畏得发抖，因为ta们只看细节都知道自己的团队做不到这样的效率和细致。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "丢开你这累赘，人家只会一飞冲天；到底谁嫌弃谁还不一定呢。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "真正的问题是问问自己：你的“家庭主妇”是怎么当的？你是在当家庭主妇，还是在从头当闺女？当宠物？", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "停止喊叫“坚决不能当家庭主妇”，那是错的。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "补充说明：这里说的是“可做 / 能做成甚好”，而不是“必做”。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中文舆论场存在一种堪称丧心病狂的防御性心态：生怕一件事被论证是合理的，因为一旦被论证为合理就会被自己列为“非做到不可的”，于是毫无理智的阻击一切合理性的论证。", "evidence": ["E21", "E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：凭什么“合理的”就是“必须的”？是什么造成了你会把一切“合理的”都自动视作“必须的”？", "evidence": ["E23", "E24"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "你为什么不能忍受自己并没有做一切合理的事情这一基本的事实？人类啥时候达成过“一切合理的都做到了”这种神级成就？", "evidence": ["E25", "E26"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种强迫性的逻辑跳跃是一种心灵创伤；想清楚这一点能让你的视野至少放宽个三四成。", "evidence": ["E27", "E28"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切事情都可做，只要有正确的前提；这是一个不应该需要专门强调的默认预设。", "evidence": ["E29", "E30"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有太多人喜欢把问题自己篡改成“（无需任何前提）可做／不可做”，这才是人生选择狭窄化的根源。", "evidence": ["E31"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "解决问题的人之所以总比你更能解决问题，极大的一块优势在于ta们同样会去寻找使得事情变得可行的前提，而不是仅仅基于平均条件来判定事情可做不可做。", "evidence": ["E32"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基于“平均水平”，凡事皆不可做——因为那只是看似可完成整个动作，实际上亦无足够利润去对冲风险；一事可做，必有其“不平均”之处。", "evidence": ["E33", "E34"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要被“正常”捆住手脚，因为正常人不幸福；幸福本身就是一种超常。", "evidence": ["E35", "E36"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个能拥有称职的全职家庭主妇的家庭要远远强大过一个有双份收入但却没有有效家政管理的家庭。", "evidence": ["E37"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家庭（尤其是有发育我家族打算的家庭）的决策是不宜假手于雇员的；雇员再忠诚、再能干也不是（也不可以是）家庭的主人，这份职责事实上不可以外包。", "evidence": ["E38", "E39"]},
    {"claim_id": "C027", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这必须要求丈夫一方有足够的素养——这份素养坦白说和收入没什么关系，更多的是觉悟水平。", "evidence": ["E40"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "对方没有这份觉悟，你当然不能勉强，那反而要自己拒绝当家庭主妇；但如果对方有这个觉悟、对家庭主妇的角色和价值有充分清醒的认识，那么因为社会上的这些低水平家庭熏陶出来的恐惧心而强迫性的选择不做，这同样是你的绝对损失。", "evidence": ["E41", "E42"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "类比：这就像按照一般人的身体条件不应该以职业球员为人生规划，但如果你是姚明，你去听他们的，是不是欠抽？", "evidence": ["E43"]},
    {"claim_id": "C030", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "文末附注让读者先看另一篇（“把这个看掉再回来看这篇”），并标出“家族答集”链接文本。", "evidence": ["E44", "E45"]}
   ],
   "argument_steps": [
    "开门表态：全职没有原则问题；答“不行”者不清楚家庭管理之善与经营良好家庭的价值（P001—P002）。",
    "归因到家庭模板：中国家庭理想仍以自耕农之家为模板，故家务与家庭管理被看轻（P003—P005）。",
    "列举现实变化：中产家庭净资产规模与社会关系、子女教育挑战远超旧模型（P006—P007）。",
    "据此比较能力：合格的家庭管理者不亚于乃至超过公司中层（P008—P009）。",
    "加前提：这种评价以其自我发展为条件（P010—P011）。",
    "指出稀缺性与细节能力（P012—P013），反讽丈夫一侧“丢开你这累赘，人家只会一飞冲天”（P014—P015）。",
    "反问读者“你的‘家庭主妇’是怎么当的”，并要求停止“坚决不能当家庭主妇”的喊法（P016—P018）。",
    "第一点补充限定：可做／能做成甚好，而非必做（P019—P020）。",
    "批评“合理的＝必须的”这一防御性逻辑跳跃，并称其为心灵创伤（P021—P030）。",
    "第二点补充限定：一切事情都可做，只要有正确的前提（P031—P032）。",
    "批评把问题篡改为“无需任何前提可做／不可做”，并以“寻找前提”区分解决问题者（P033—P034）。",
    "格言总结：基于平均水平凡事皆不可做；一事可做必有不平均之处；不要被“正常”捆住（P035—P039）。",
    "回到命题：称职全职主妇的家庭强于双收入无家政管理的家庭，家庭决策不可外包（P040—P042）。",
    "条件落到丈夫一侧：须有觉悟；无觉悟则不能勉强、应自己拒绝，有觉悟而因恐惧不做则是绝对损失（P043—P045）。",
    "以姚明的类比强化“按一般条件判断不适用特殊者”（P046—P047），附参考链接（P048—P049）。"
   ],
   "concept_usage": [
    {"term": "家庭主妇", "meaning": "作者指现代中产家庭的专业管理者，其工作含资产管理、社会关系处理、子女教育与家庭内环境调理，需主动自觉进取地自我发展。", "evidence": "P008", "ambiguity": "与自耕农模型下的“家庭主妇”（仅维护性家务）同名不同义，作者以P005与P010对举"},
    {"term": "自耕农的家庭（模板）", "meaning": "作者称中国目前传承的家庭理想实际以其为模板，特征是家务极简、资产有限、对子女期望低。", "evidence": "P003", "ambiguity": "“雇农们对……自耕农的家庭的想象”一语本身在文中未展开其历史依据"},
    {"term": "家庭政务", "meaning": "比一般家务更高层次的家庭管理事务，作者称其理解不在一般人常识中。", "evidence": "P004", "ambiguity": "未列举具体范围"},
    {"term": "前提", "meaning": "使事情变得可行的条件；作者主张一切事情都可做，只要有正确的前提，且解决问题者的优势在于寻找前提。", "evidence": "P031", "ambiguity": "“正确的前提”的判准未给出"},
    {"term": "防御性心态", "meaning": "生怕一件事被论证合理就会被列为非做到不可，因而阻击合理性论证的心态。", "evidence": "P021", "ambiguity": "属心理学式概括，文中的例证仅“读大学是合理的人生计划”一例"},
    {"term": "正常 / 超常", "meaning": "作者以“平均水平”对应“正常”，以“不平均”对应“超常”，并称幸福本身是一种超常。", "evidence": "P038", "ambiguity": "与统计意义的正常之关系未界定"}
   ],
   "examples_and_targets": [
    "自耕农之家、雇农的想象：作者用于解释家庭模板来源的历史叙述（P003—P005）。",
    "一两百万净资产、一二线城市普通家庭：作者举的数据性描述（P006）。",
    "公司中层白领、总监、高级社畜：作者用于比较能力水平的对象（P008—P009、P013）。",
    "“放下婴儿车就能经营起一家业务相当健康的小企业”：作者比喻（P010）。",
    "“年薪百万的丈夫”：提问者问题中的设定，作者用于比较稀缺性（Q001、P012）。",
    "“读大学是合理的人生计划”：作者举来说明防御性心态的例子（P022）。",
    "姚明与职业球员：作者类比材料（P046）。",
    "“家族答集”链接文本：文末附注（P049，lexical 未覆盖片段）。"
   ],
   "conditions": [
    "限定：“前提是，这位家庭主妇要积极主动的、自觉的、进取的自我发展”（P011）。",
    "限定：“首先，这里说的是‘可做 / 能做成甚好’，而不是‘必做’”（P020）。",
    "限定：“一切事情都可做，只要有正确的前提”（P031）。",
    "条件：“这必须要求丈夫一方有足够的素养……更多的是觉悟水平”（P043）。",
    "条件句：对方无觉悟则不能勉强、应自己拒绝当家庭主妇；对方有觉悟而因恐惧不做则是绝对损失（P044—P045）。",
    "类比限制：“按照一般人的身体条件不应该以职业球员为人生规划”为前提的姚明类比（P046）。"
   ],
   "rhetoric_and_tone": "论辩与训诫并重，语气强硬且带嘲讽：用“丧心病狂”“欠抽”“累赘”“高级社畜”等贬抑词；大量反问推进（“凭什么‘合理的’就是‘必须的’？”“是不是欠抽？”）；用“反省清楚！”“仔细想想清楚。”等命令句；同时对“家庭主妇”能力给出高度肯定式排比（P008）；文末以轻松化表述收尾（“肺活量都会变大，血氧含量都会提高一大截”）。",
   "unresolved_questions": [
    "P049（“家族答集”）被渲染器标注为“⚠lexical未覆盖片段”，其内容仅为链接文本，是否含被截断的链接或后续文字待核。",
    "P041原文作“有发育我家族打算的家庭”，“发育我家族”疑为笔误或特殊用法，作者未作解释。",
    "“一两百万净资产的绝不在少数”“只是一二线城市普通家庭的常态”“专业有效的家庭主妇远比年薪百万的丈夫稀缺”等属数据性断言，未附来源，待外部核查。",
    "作者称家庭决策“不可以外包”给雇员，但对于无称职主妇的家庭如何安排未作说明。",
    "Q001 属提问者，作者未回答“你愿意／不愿意”的个人选择，而是讨论该选择是否合理，两者层次不同，需研究者注意。",
    "“家族答集”为跨文本指引，本篇未展开其内容，不能据以补足本篇论证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "其实这没有原则上的问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "回答“不行”的人只是不清楚一个家庭可以管理得有多好罢了", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这其实是因为中国的家庭的标准模版落后得惊人", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "更高的家庭管理水平和更复杂的家庭政务的理解目前都不在一般人的常识之中。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "因为在自耕农的家庭模型中家庭主妇是没有发挥空间的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "自耕农对子女的期望甚低，大体上只不过是做个本分人", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "现在的家庭有一两百万净资产的绝不在少数——这甚至只是一二线城市普通家庭的常态。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "远非五六十年前雇农们想象中的自耕农之家所能比拟。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "都远非一般的公司中层白领所能比拟。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "甚至就是总监一级也没有几个真的能平起平坐的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "放下婴儿车就能经营起一家业务相当健康的小企业。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "前提是，这位家庭主妇要积极主动的、自觉的、进取的自我发展。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P012", "quote": "专业有效的家庭主妇远远要比“年薪百万的丈夫”稀缺得多。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "因为ta们只看细节都知道自己的团队做不到这样的效率和细致。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "丢开你这累赘，人家只会一飞冲天。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "到底谁嫌弃谁还不一定呢。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "你的“家庭主妇”是怎么当的？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P017", "quote": "你是在当家庭主妇，还是在从头当闺女？当宠物？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "停止喊叫“坚决不能当家庭主妇”，那是错的。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "这里说的是“可做 / 能做成甚好”，而不是“必做”。", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P021", "quote": "我发现中文舆论场有一种普遍存在的堪称丧心病狂的防御性心态", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "于是人们会毫无理智的阻击一切合理性的论证。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P023", "quote": "凭什么“合理的”就是“必须的”？", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P024", "quote": "是什么造成了你会把一切“合理的”都自动视作“必须的”？", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P025", "quote": "你为什么不能忍受自己并没有做一切合理的事情这一基本的事实？", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "人类啥时候达成过“一切合理的都做到了”这种神级成就？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P027", "quote": "这种强迫性的逻辑跳跃是一种心灵创伤", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P028", "quote": "想清楚这一点能让你的视野至少放宽个三四成。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P031", "quote": "一切事情都可做，只要有正确的前提。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P032", "quote": "这是一个不应该需要专门强调的默认预设。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P033", "quote": "这才是人生选择狭窄化的根源。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P034", "quote": "而不是仅仅基于平均条件来判定事情可做不可做。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P036", "quote": "基于“平均水平”，凡事皆不可做", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P037", "quote": "一事可做，必有其“不平均”之处。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P038", "quote": "不要被“正常”捆住手脚，因为正常人不幸福。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P039", "quote": "幸福本身就是一种超常。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P040", "quote": "一个能拥有称职的全职家庭主妇的家庭要远远强大过一个有双份收入但却没有有效家政管理的家庭。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P041", "quote": "的决策是不宜假手于雇员的。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P042", "quote": "这份职责事实上是不可以外包的。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P043", "quote": "更多的是觉悟水平。", "relation": "qualifies"},
    {"key": "E41", "paragraph_id": "P044", "quote": "对方没有这份觉悟，你当然不能勉强。那反而要自己拒绝当家庭主妇。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P045", "quote": "这同样是你的绝对损失。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P046", "quote": "但如果你是姚明呢？你去听他们的，是不是欠抽？", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P048", "quote": "另外，把这个看掉再回来看这篇", "relation": "context"},
    {"key": "E45", "paragraph_id": "P049", "quote": "家族答集", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭社会学", "性别角色与劳动价值", "家庭管理与家政"],
   "issue_candidates": ["年薪百万丈夫下是否全职", "家庭主妇的价值与专业性", "中国家庭模板的历史成因", "合理的与必须的区别", "前提思维与人生选择"],
   "text_function_candidates": ["答疑", "论辩", "经验总结", "反驳舆论成见"],
   "object_candidates": ["提问者", "家庭主妇", "自耕农与雇农", "公司中层白领与总监", "高级社畜", "丈夫一方", "姚明", "家族答集"],
   "working_keywords": ["全职", "家庭主妇", "自耕农", "家庭政务", "家政管理", "可做", "必做", "合理的", "必须的", "前提", "不平均", "超常"]
  },
  "notes": "无图片节点。正文 P001—P049 全部读完；末段 P049 被渲染器标注为“⚠lexical未覆盖片段”，内容为链接文本“家族答集”，已按原文记录并在 unresolved_questions 登记。Q001 属提问者，作者未回答个人是否愿意，而是讨论该选择是否合理。文中净资产规模、稀缺性等属数据性断言，未附来源，待外部核查；P041“发育我家族”疑为笔误，未作改写。"
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
