# -*- coding: utf-8 -*-
"""批次 r001-b0057 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0057.sessions.py            # 写 out/r001-b0057.out.jsonl
  python3 records/r001-b0057.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0057"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0057.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "2a16f998": {
  "analysis": {
   "question_context": "提问者（Q001）问：在聊天时如何克制自己输出知识量以避免气氛尴尬。作者未接受'克制输出量'这一预设，改问输出是否真的扣住对方的需要，并给出双赢前提与'注意力掠夺'的条件判定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "把'如何克制输出知识量'改写为'输出时有没有真的扣住对方的需要'这一判定问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "释放表达欲须以对方的需要和利益得到双赢为前提。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "若场合中对方因社交礼仪无法自行脱离，则构成注意力掠夺。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P004", "P005"], "summary": "这类输出有两种定性：不懂事（对自己在干什么没有觉察）或更糟的'懂而恶'。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "前者尚可原谅，后者将遭流放。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "输出知识是否成为问题，取决于输出时有没有真的扣住对方的需要。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想释放表达欲，需要以对方的需要和利益得到双赢为前提。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果场合中对方出于社交礼仪不能自己脱离，则输出构成注意力掠夺。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述输出要么被定性为不懂事，要么更糟——被定性为懂而恶。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "不懂事尚可原谅，懂而恶将遭流放。", "evidence": ["E6"]}
   ],
   "argument_steps": [
    "把问题从'如何克制输出量'改写为'输出是否扣住对方需要'（P001）",
    "给出前提：释放表达欲须以对方需要与利益的双赢为前提（P002）",
    "给出条件判定：对方因社交礼仪无法自行脱离时，输出构成注意力掠夺（P003）",
    "给出两种定性：不懂事或懂而恶（P004-P005）",
    "结论：前者尚可原谅，后者将遭流放（P006）"
   ],
   "concept_usage": [
    {"term": "注意力掠夺", "meaning": "在对方因社交礼仪无法自行脱离的场合释放表达欲，即对对方注意力的掠夺", "evidence": "P003", "ambiguity": "未给出认定主体与可操作标准"},
    {"term": "懂而恶", "meaning": "明知自己在做什么仍然为之的定性，与'不懂事'相对", "evidence": "P005", "ambiguity": "'懂'的认定依据未说明"},
    {"term": "双赢", "meaning": "释放表达欲以对方的需要和利益得到满足为条件", "evidence": "P002", "ambiguity": "利益由谁判定未说明"}
   ],
   "examples_and_targets": [
    "无具体人物、机构、事件或数据；'流放'为修辞性后果描述（P006）",
    "被改写的提问预设：'克制输出知识量'未被作者当作处理办法正面评估（P001）"
   ],
   "conditions": [
    "取决于输出时是否扣住对方的需要（P001）",
    "前提是对方的需要和利益得到双赢（P002）",
    "条件是对方出于社交礼仪不能自己脱离的社交环境（P003）"
   ],
   "rhetoric_and_tone": "第二人称'你'直接训诫；短句加破折号作裁定式判断；'流放'为夸张威慑；答疑式短评，无例证与数据。",
   "unresolved_questions": [
    "'注意力掠夺'由谁认定、按什么标准认定，正文未说明",
    "'流放'是字面主张、比喻还是戏谑，正文未说明",
    "提问者'克制输出知识量'的预设未被正面评估，作者以'是否扣住对方需要'替代作答"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "那要看你输出的时候，有没有真的扣住对方的需要。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你想释放表达欲，需要以对方的需要和利益得到双赢为前提。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "否则如果是一种对方出于社交礼仪不能自己脱离的社交环境的话，就构成了注意力掠夺。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这要么会被定性为不懂事", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "要么更糟——被定性为懂而恶。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "前者尚可原谅，后者将遭流放。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往", "沟通伦理"],
   "issue_candidates": ["表达欲与社交气氛", "注意力掠夺", "被迫倾听"],
   "text_function_candidates": ["答疑", "短评", "训诫"],
   "object_candidates": ["unknown"],
   "working_keywords": ["注意力掠夺", "懂而恶", "双赢", "扣住对方的需要"]
  },
  "notes": "正文仅151字，属短答；brief 与正文高度重合，全部判断以正文 P001-P006 为据。"
 },
 "9db90b4e": {
  "analysis": {
   "question_context": "提问者（Q001）问：有哪些行为不尊重别人，但自己却难以意识到。作者不列举具体行为，而是给出一个判据：自认'已经够尊重'时并不算尊重，是否够尊重由被尊重方的判定决定。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "在心里说'我这样对ta已经够尊重的了'的时候，并不算尊重；要求记住这一点。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "理由：不存在'够尊重'这个状态；一切未受抱怨的自以为足够的尊重都依赖对方的不计较，从无例外。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "判定权归对方：对方觉得不够就是不够，不能用自己、大众或朋党的标准否决。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "归谬：若按朋党标准计算，一群黑帮彼此点赞即可'完全尊重'地烧铺子。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "给出'真正意义上的、有真实重量的尊重'的判据：接受'对方永远是对的、我必须道歉'这种极端不公平的安排。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013"], "summary": "限定：可以不这么做，因为爱不能作为义务；但该定义不容挑战。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015", "P016"], "summary": "做不到者至多算'礼貌'，在明白人眼里顶多及格。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P017"], "summary": "行动要求：把这一篇背下来。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在心里自认'我这样对ta已经够尊重的了'的时候，并不算尊重。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "事实上不存在'够尊重'这个状态；未受抱怨的自以为足够的尊重都依赖对方的不计较，从无例外。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要对方觉得不够尊重就是不够尊重；不能用'我挺尊重'或朋友、大众、朋党的标准否决对方的判定。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若按发起者或朋党标准计算，则一群黑帮彼此点赞也能'完全尊重'地把别人的铺子烧掉。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有宁可接受'对方永远是对的、我必须道歉'这种极端不公平的安排，才成其为真正意义上的、有真实重量的尊重。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人可以不这么做，因为爱不能作为对人的义务，而必须是绝对自由、自愿的选择。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个尊重的定义不容挑战。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "做不到这条，即使在极好的情况下也至多勉强算'礼貌'，在明白人眼里顶多及格。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把这一篇背下来，它足以改变你的命运。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "以自认'够尊重'为反例，否定这种自我评价（P001）",
    "给出理由：'够尊重'这一状态不存在，未受抱怨的尊重依赖对方不计较（P003-P006）",
    "确立判定权归属：对方说不够就是不够，不得以自己或朋党标准否决（P007-P008）",
    "归谬：朋党标准将推出黑帮互赞即可烧铺子的结论（P009）",
    "定义真正的尊重：接受'对方永远是对的、我必须道歉'的极端不公平安排（P010）",
    "让步与限定：可以不做，爱是自由自愿的选择，但定义不容挑战（P011-P013）",
    "对比：做不到者只算礼貌与及格（P014-P016）",
    "落到行动要求：把这一篇背下来（P017）"
   ],
   "concept_usage": [
    {"term": "尊重", "meaning": "由被尊重方的感受判定的关系状态，不由行为人的自我评价或第三方标准决定", "evidence": "P007", "ambiguity": "未给出'对方判定'的限度"},
    {"term": "够尊重", "meaning": "作者否认其存在的自我评价状态", "evidence": "P004", "ambiguity": "作者同时承认'没更多能力满足'的道歉说法，边界未细化"},
    {"term": "礼貌", "meaning": "低于尊重的形式合规，只到及格分", "evidence": "P014", "ambiguity": "未说明礼貌与尊重的具体分界"},
    {"term": "爱", "meaning": "不能作为对人的义务，必须是绝对自由、自愿的选择", "evidence": "P011", "ambiguity": "未说明与'尊重'义务的关系"},
    {"term": "朋党标准", "meaning": "以朋友圈相互认同替代被尊重方判定的计算方式", "evidence": "P008", "ambiguity": "无"},
    {"term": "大众标准", "meaning": "被明确排除在尊重判定之外的第三方标准", "evidence": "P008", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "假想例：一群黑帮肯积极彼此点赞，就可以'完全尊重'地把铺子烧掉（P009），作者用作归谬",
    "被否定的辩解说法：'我觉得我挺尊重的'、'我的朋友都觉得我对你已经够尊重了'（P007），修辞材料",
    "无具体人物、机构、事件或数据"
   ],
   "conditions": [
    "只要对方觉得不够尊重，就是不够尊重（P007）",
    "尊重不按发起者标准、不按大众标准、更不按朋党标准计算（P008）",
    "可以不做，前提是把爱理解为自由自愿的选择而非义务（P011）",
    "做不到这条时'即使在极好的情况下'至多算礼貌（P014）"
   ],
   "rhetoric_and_tone": "第二人称训诫与断言并用；箴言式命令（'以后记住这一点''把这一篇背下来，它足以改变你的命运'）；'从来——是的，【从来】——'用方括号与重复强调；黑帮比喻带讽刺；反问'身边什么时候缺过“礼貌周全”的人？'；句式短促。",
   "unresolved_questions": [
    "'ta永远是对的，我必须道歉'是否为无限度的字面要求，正文未给边界",
    "'真正的明白人''接触资格'的所指与判定者未说明",
    "黑帮归谬是否主张任何自称被冒犯者都取得判定权，存在解释歧义",
    "本篇无图片节点、无 provenance/superseded 版本差异说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我这样对ta已经够尊重的了", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "尊重人的人，永远不会觉得自己已经“够尊重”了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "根本不存在“够尊重”这个状态", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "都是依赖对方的不计较，从来没有任何例外", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "只要对方觉得不够尊重，就是不够尊重。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "因为是否够尊重，永远也不可能按照发起者的标准来计算", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "否则岂不是只要一群黑帮肯积极彼此点赞ta们就可以“完全尊重”的把你的铺子烧掉？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "才成其为为真正意义上的、有真实重量的尊重", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "因为爱永远不能作为一种对人的义务，而必须是一种绝对的自由、自愿的选择。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "但你不要想去挑战这个定义。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "因为它不容挑战。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "至多也不过能勉强算是“礼貌”罢了", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "顶多给你个及格分", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "把这一篇背下来，它足以改变你的命运。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际伦理", "道德哲学"],
   "issue_candidates": ["尊重的判定标准", "自我评价与他人感受", "礼貌与尊重的区别"],
   "text_function_candidates": ["答疑", "训诫", "定义式论辩"],
   "object_candidates": ["unknown"],
   "working_keywords": ["够尊重", "礼貌周全", "朋党标准", "大众标准", "接触资格"]
  },
  "notes": "正文639字，无图片与版本差异；brief 与正文重合，判断均据正文 P001-P017。"
 },
 "f975f3fe": {
  "analysis": {
   "question_context": "提问者（Q001）问：死亡的意义是什么。作者没有直接谈个人哀悼或生理死亡，而是质疑'人皆有一死'是事实还是信仰，追问现代社会普遍坚信死亡必然性的来源与功能，并给出'死亡首先是社会性意识形态预设、对个人是最大宽慰与现实利益'的回答。文末标'（未完，待续）'。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开场：死亡这件事一言难尽，有一件事读者可能没有注意到。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "主张：人类普遍相信'人皆有一死'是很晚的事，这不是事实而是信仰。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "以连续反问要求给出可验证证据：何时普查、如何确证两百岁以上或千余岁者不存在。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "反驳：DNA、端粒效应不能替代实际验证，那只是信心十足的推测；被证据推翻的自信推测在科学史上比比皆是。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "'人皆有一死'没有也不可能有足够充分的事实证据；并区分'人会死'与'人必然会死'。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023"], "summary": "'普遍死亡'不是任何时代被实验确证的科學事实，且相信不死者无法被证据驳倒。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "转向追问：拥死派压倒否死派必因死亡蕴含重大价值，并提出'这价值是什么'的问题。", "role": "transition"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037"], "summary": "回答：'人终有一死'是最大的宽慰，对古人、老人和常处病痛挫折中的人尤其是最大的安慰。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P038", "P039", "P040", "P041"], "summary": "反面推演：若不相信自然死亡，就须按'可以争取无限活下去'的样式活着，伦理代价惊人。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P042", "P043", "P044"], "summary": "现实例证：印度轮回式永生观支撑种姓制度；普遍相信可永生的社会极难面对牺牲与危险（征兵问题）。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049"], "summary": "永生理论必须打'先天限制'补丁，否则社群会被打垮，由此驱动长生不老理论补丁大赛。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054", "P055"], "summary": "历史机制：技术竞争使'人固有一死'占上风；社会规则无休止惩罚长生信念者，类似相信巫术者。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P056", "P057", "P058"], "summary": "结论：接受'人固有一死'可免于代价，这本身即现实利益；文末标'（未完，待续）'。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "人类普遍相信'人皆有一死'是很晚才有的事，这不是事实而是一种信仰。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：拿不出证明历史上早于两百年前出生者都已死亡的证据，也设计不出证明两百岁以上者不存在的可行手段。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "DNA、端粒效应等不能替代实际验证，那叫 speculation with great confidence，而不是 evidence。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被实际证据推翻的信心十足的理论推测在科学史上几乎每个案例都是。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "'人皆有一死'没有、事实上也不可能有足够充分的事实证据。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "证明'人会死'与证明'人必然会死'是两回事。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "'普遍死亡'不是已被任何时代确凿实验证实过的科学事实，而且恐怕在可见的将来也没有可能做到。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "相信有些人不会死的人无法被证据驳倒，也不能说他们一定是错的。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者追问：为何现代人如此普遍、坚定、彻底地相信人一定会死——必有什么重大价值在奖励拥死派、打击否死派。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "死亡之中蕴含着一种足以压倒相信长生所得一切福利的价值，且这种压倒在这几千年文明史中不断扩大，拥死派从0%增长到100%。", "evidence": ["E15", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "仅凭上述事实即可确信死亡这种信仰一定存在至关重要的、至为强大的价值。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大约五六千年前人们普遍不认为人一定会死。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "'人终有一死'是人类最大的宽慰，对古人、老人和常处病痛衰老灾难中的人尤其是最大的安慰。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若不相信会自然死亡，就须按'可以争取无限活下去'的样式活着；永生若非绝望，整个伦理计算会令现代人瞠目结舌。", "evidence": ["E23", "E24", "E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "印度人大面积相信'此生受苦、来生福报'的轮回式永生观，这给种姓制度以显著的逻辑支撑，并阻碍自由劳动力和资源流动在印度实现。", "evidence": ["E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现世永生的意义根本而巨大，一旦纳入基本议题就会深刻影响社会运行逻辑，使社会极难面对牺牲和危险。", "evidence": ["E28", "E42"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这就必然要求一切现世永生理论作出修正，解释为何有一大部分人先天注定不能追求长生；该限制必须是先天的，否则会引发全民大抢劫。", "evidence": ["E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "补丁不足的社群容易被别的社群打垮，由此驱动'长生不老理论补丁大赛'。", "evidence": ["E31", "E32", "E43"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "交通技术发展与帝国规模上限提高会驱动'人固有一死'的理论逐渐占据上风，因为这是'敢死之士'的竞争。", "evidence": ["E33", "E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实际上是客观历史自己通过技术竞争，逐渐消灭了人类关于长生不老的执念。", "evidence": ["E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "死亡对个人的意义是次要的，它首先是对社会幸存与稳固不可替代的意义，因而成为不容选择、只能接受的'意识形态预设'。", "evidence": ["E36"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "社会的规则设计与运行逻辑会不由自主、无休止地惩罚持有长生观念的人，使其处处碰壁、日益孤独、生不如死。", "evidence": ["E37"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类似相信巫术者：法律与警察不会支持其主张，但其遭受的心理折磨与生理损失真实而无休止。", "evidence": ["E38"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "接受'人固有一死'就能免于上述代价，而免于代价本身就是现实利益，是实打实的价值和意义。", "evidence": ["E39", "E40"]}
   ],
   "argument_steps": [
    "提出信仰论题：'人皆有一死'不是事实而是很晚形成的信仰（P003-P004）",
    "以反问要求举证：普查方式、证明两百岁以上或千余岁者不存在（P005-P012）",
    "反驳以DNA、端粒效应替代实际验证的做法，并援引科学史反例（P013-P016）",
    "得出结论：'人皆有一死'缺乏足够充分的事实证据，并区分'人会死'与'人必然会死'（P017-P020）",
    "指出'普遍死亡'非确证科学事实，相信不死者亦无法被驳倒（P021-P023）",
    "转为追问：拥死派何以压倒否死派，必因死亡蕴含重大价值（P024-P029）",
    "给出答案：'人终有一死'是最大的宽慰；并以现代人寿命经验说明为何现代人不易体会（P032-P037）",
    "反面推演：不相信自然死亡者的生活样式与伦理代价（P038-P041）",
    "以印度轮回永生观与征兵难题为例，说明永生信念的社会后果（P042-P044）",
    "推演永生理论必须补上'先天限制'，并形成补丁大赛（P045-P049）",
    "以技术竞争解释'人固有一死'的胜出，说明社会对长生信念者的无休止惩罚（P050-P055）",
    "结论：接受人固有一死可免于代价，这本身即现实利益（P056-P057）"
   ],
   "concept_usage": [
    {"term": "死亡", "meaning": "本文中主要被当作信仰与意识形态预设处理，而非单纯的生物学事件", "evidence": "P004", "ambiguity": "生物学过程与信仰层面的区分标准未说明"},
    {"term": "人皆有一死／人固有一死", "meaning": "被普遍接受但缺乏充分事实证据的信念，后成为社会性的意识形态预设", "evidence": "P003", "ambiguity": "作者区分'人会死'与'人必然会死'，但未给出后者的证明标准"},
    {"term": "拥死派／否死派", "meaning": "围绕人是否必然死亡形成的两个意识形态阵营", "evidence": "P025", "ambiguity": "'0%到100%'的量化无来源"},
    {"term": "意识形态预设", "meaning": "不容个人选择、只能接受的社会性前提", "evidence": "P053", "ambiguity": "无"},
    {"term": "长生不老理论补丁大赛", "meaning": "各社群为解释'多数人先天不能长生'而追加限制条件的竞争", "evidence": "P049", "ambiguity": "无"},
    {"term": "敢死之士", "meaning": "相信死亡的社会中，争夺统治地位所需的愿意承担死亡风险的人力", "evidence": "P051", "ambiguity": "无"},
    {"term": "speculation with great confidence", "meaning": "作者对'信心十足但无实际验证的推测'的贬称，与evidence相对", "evidence": "P014", "ambiguity": "无"},
    {"term": "现世永生", "meaning": "寄望于此世长生的观念，与轮回来生式永生并列", "evidence": "P043", "ambiguity": "与'来生福报'式永生的关系只作并列，未细分"}
   ],
   "examples_and_targets": [
    "反问材料：挨家挨户敲门问'借问，你大爷死了没？'（P009）；证明两百岁以上（P011）、活了一千多年者不存在（P012）",
    "科学史例证：比萨斜塔的铁球、火车上的光速（P016），作者用以说明自信推测被推翻",
    "经书说法'唯有童子身能成仙，长生不老'（P039）",
    "传说用处女的血洗澡可以返老还童（P040）",
    "印度轮回式永生观与种姓制度（P042），作者用作现实例证",
    "普遍相信可永生之社会的参军难题（P044）",
    "先天限制补丁例：生辰八字不对、'没有慧根''没有仙缘'（P047）",
    "巫术信念者被邻居'妨'、告状不受理、反抗则坐牢的类比（P055）",
    "反讽对象：以DNA、端粒效应替代实际验证者（P013）；在评论区拿'人会死'证明'人必然会死'的人（P020）"
   ],
   "conditions": [
    "作者称该结论'恐怕在可见的将来也没有可能做到这一点'（P022）",
    "若不相信会自然死亡，就须按可以争取无限活下去的样式活着（P038）",
    "只要交通技术发展起来、帝国规模上限提高，补丁大赛就会起效（P050）",
    "一旦现世永生被纳入基本议题，就会深刻影响社会运行逻辑（P043）",
    "对长生的限制必须是先天而不可能后天弥补的条件（P046）",
    "现代人（尤其是尚未老去的婴儿潮一代，各国起始期不同）因人均寿命七十、八十岁而觉得人生是可延续七十几年的盛宴（P033-P034）"
   ],
   "rhetoric_and_tone": "反讽与连续反问（'不信吗？''嗯？''啥时候普查的？'）；口语调侃（'借问，你大爷死了没？'）；中英混用（evidence／speculation with great confidence）作贬抑；对评论区读者的直接喊话与讥讽（P020）；宏大历史叙事加类比论证；文末标'（未完，待续）'。",
   "unresolved_questions": [
    "文末标'（未完，待续）'，本篇论述未完结，后续篇章是否存在未说明",
    "事实性断言需外部核查：'大约五六千年前人们普遍不认为人一定会死'、拥死派'从0%增长到了100%'、印度轮回信仰对种姓制度的支撑、人均寿命七十、八十岁",
    "'这巨大的价值到底是什么'在P031提出、P032以'最大的宽慰'作答，但社会机制层面的价值与个人宽慰的关系未合并说明",
    "'死亡是一种信仰'中信仰与生物学事实的划界标准未给出",
    "本篇无图片节点；无 provenance/superseded 版本差异说明（updated_at 晚于 published_at，差异内容不可知）"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "其实人类普遍相信“人皆有一死”是一件非常非常晚的事情——这不是一种事实，而是一种信仰。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "死亡，是一种信仰。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "你有什么证据证明历史上出生早于两百年前的人类都死了啊", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P011", "quote": "确确实实的【证明】现在绝对没有一个两百岁以上的人类正混在我们中间活着？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P012", "quote": "如何证明绝对没有一个实际活了一千多年的老太爷三百年前刚死？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P014", "quote": "这不叫evidence，这叫speculation with great confidence。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P015", "quote": "被实际证据推翻的信心十足的理论推测多了去了", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "忘了比萨斜塔的铁球了？忘了火车上的光速了？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "事实上也不可能有——【足够充分】的事实证据", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "证明“人会死”和证明“人必然会死”是两回事", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "“普遍死亡”并不是一件已经被（或者在任何时代曾经被）确凿无疑的、有充分解释力的实验证实过的科学事实。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "没人能说相信人不一定会死的人真的就一定是错的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "我们为什么现在会如此普遍的、坚定的、彻底的相信人一定会死呢？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P025", "quote": "这里一定有什么重大的价值，在奖励着拥死派、打击着否死派", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P028", "quote": "死亡之中蕴含着一种价值，足以压倒人通过相信长生而得到的一切福利。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P029", "quote": "你就可以确信死亡这种信仰一定存在至关重要的、至为强大的价值。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P030", "quote": "整个人类文明史完全可以看作相信死亡的文化实体不断从精神和肉体上灭亡对手的过程。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "在大约五六千年前，人们普遍的不认为人一定会死啊。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "你觉得古代人——我都不说多古代，就解放前好了——真的认为人一定会死吗？", "relation": "context"},
    {"key": "E20", "paragraph_id": "P032", "quote": "但“人终有一死”是人类最大的宽慰。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P035", "quote": "“人终有一死”是最大的安慰。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "这是一个多么令人宽慰的事实啊。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P038", "quote": "如果你不相信你会自然死亡，那么你就需要按照“可以争取无限活下去”的样式活着。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P039", "quote": "你想要长生不老的每一秒钟，你都要顶住“破坏童子身”的一切诱惑。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P040", "quote": "在“返老还童”面前，有什么所谓“罪大恶极”？", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "永生如果不是绝望的，人类的整个伦理计算都会令普通的现代人瞠目结舌。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P042", "quote": "印度人大面积的相信“此生受苦、来生福报”的轮回式永生观", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P044", "quote": "一个普遍相信靠巧妙的保养可以永远活下去的社会，要什么样的代价才能吸引到足够的成员参军？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P045", "quote": "就必然要求一切关于现世永生的理论做出修正", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P046", "quote": "这必须是某种你先天就不具备、也不可能在后天弥补的条件。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P047", "quote": "例如生辰八字不对，或者“没有慧根”“没有仙缘”。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P048", "quote": "不把这补丁打足，一个社群就很容易被另一个社群打垮。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P050", "quote": "驱动“人固有一死”的理论逐渐占据上风", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P051", "quote": "这种关系到统治还是被统治的竞争，就是“敢死之士”的竞争。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P052", "quote": "实际上是客观历史自己通过技术竞争，逐渐的消灭了人类关于长生不老的执念。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P053", "quote": "它首先是对社会的幸存和稳固有不可替代的意义", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P054", "quote": "人类社会的存在实际上和个人的长生不老理想是不兼容的", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P055", "quote": "然而你所遭受的心理折磨、生理损失却是真实的、无休止的。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P056", "quote": "反过来，你如果接受“人固有一死”的理念，你就能免于这种代价。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P057", "quote": "能免于这代价，本身对你就是现实利益", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P058", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E42", "paragraph_id": "P043", "quote": "因为现世永生的意义是如此根本和巨大", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P049", "quote": "这自然而然的驱动了一个“长生不老理论补丁大赛”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教与信仰", "社会理论", "科学哲学", "历史人类学"],
   "issue_candidates": ["死亡必然性是否为事实", "长生信念与意识形态竞争", "永生的社会成本", "证据与推测的界限"],
   "text_function_candidates": ["论辩", "答疑", "反讽评论", "思想实验"],
   "object_candidates": ["印度", "种姓制度", "婴儿潮一代", "儒家以外的古代社会（未具体指名）"],
   "working_keywords": ["拥死派", "否死派", "意识形态预设", "长生不老理论补丁大赛", "敢死之士", "speculation with great confidence"]
  },
  "notes": "长文（2828字／58段），文末标'（未完，待续）'，属未完结论述。brief 与正文重合，判断均据正文 P001-P058。文中历史人口与社会事实断言（五六千年前观念、0%到100%、印度种姓、人均寿命）为作者表述，未经外部核查，已登记于 unresolved_questions。"
 },
 "ed9090fa": {
  "analysis": {
   "question_context": "提问者（Q001）问：性格软弱的人怎样做领导。作者先要求界定'性格软弱'，进而主张若指怕得罪人则几乎所有权都是这样的人担任，领导显得强硬另有原因，并最终把'软弱'重定义为有无'打落牙齿往肚里咽'的忍耐的坚强。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "要求先定义'性格软弱'，问题才有实在意义。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007"], "summary": "若指怕得罪人，则除少数例外没有正常人不害怕；几乎所有的领导都是性格软弱的人担任的。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "转折：领导看起来强硬不是因为性格特殊，而是因为别的原因。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "A类原因：职责、战略、原则所在时无法避免得罪人；责任感、契约义务、战略目标、更大利害关系画出底线。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019", "P020"], "summary": "强硬表现源于看到退无可退的理由（如东亚领导者顾虑损失面子与威信）；性格未变而客观表现变硬。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025"], "summary": "新手借解释开导降低伤害的四点不可行：机密不能说、管理操作不能转为拜托关系、无时间精力、人难以超越个人得失。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036"], "summary": "B类原因：有的人人格发育不健全，以自身标准要求一切，礼贤下士被利用、听部分人意见被指偏听偏信，所有选择被堵死。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P037", "P038", "P039"], "summary": "限定：领导不能完全自由选择团队成员与客户，被动局面最煎熬。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P040", "P041"], "summary": "重新定义并给出结论：关键是有无忍耐的坚强，没有则确实不适合。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051"], "summary": "追问'不适合就可以不做吗'：为父母、配偶、子女者都是天然绝对的领导，逃避不了。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P052", "P053"], "summary": "收束限定：不是建议'只管上'，只是性格软弱与否不应成为重大考量因素。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "必须先定义'性格软弱'，这个问题才有实在意义。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若'软弱'指怕得罪人，则除某些大脑发育有问题者和从未见识过厉害的人之外，没有什么正常人不怕得罪人；强力机关的领导也不是无脑不怕得罪人的人。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一两亿或小局长就自认手眼通天者，以及不知死活的富二代官二代，属大概率会被淘汰的人。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "排除上述人后，大部分人都是怕得罪人或不愿意得罪人的；其实几乎所有的领导都是性格软弱的人担任的。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "领导看起来强硬不是因为性格特殊，而是因为基于某种原因看到了退无可退的理由。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "职责所在、战略所在、原则所在时没得选择，极尽与人为善也不能以抛弃这些东西为代价，因为抛弃它们问题的性质和规模比得罪人更深。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "责任感、契约义务、战略目标、更大的利害关系给'怕得罪人'画了一条底线。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "软弱的人走上领导岗位、负起更多责任后，性格没变但客观表现会自然而然地强硬一些。", "evidence": ["E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "新手想通过解释、开导降低伤害不可行：机密不能说、管理操作不能转为拜托关系、未必有时间精力机会、很多人根本做不通。", "evidence": ["E13", "E14", "E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有的人人格发育不健全，别人没有办法不得罪ta；ta要求一切尊重ta的标准、照顾ta的感受、服从ta的道德观。", "evidence": ["E17", "E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对这类人'性格软弱'也没用：礼贤下士被利用为发挥影响力的良机，只听部分人意见又被指搞个人崇拜、偏听偏信，逻辑上所有选择都被堵死，根本没有不得罪这些人的可能。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "领导也不能完全自由地选择团队成员和客户：可能招募看走眼、从别人手里接手，或客户派来对接的是这样的人。", "evidence": ["E23", "E24"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓性格软弱适不适合当领导，不是指是否担心得罪人，而是指有没有'打落牙齿往肚里咽'的忍耐的坚强。", "evidence": ["E25"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有这份忍耐的坚强，的确不适合当领导。", "evidence": ["E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人在家庭中无处可逃：为父母、为配偶、为子女者都是对方天然的、绝对的领导。", "evidence": ["E27", "E28", "E29", "E30", "E31"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "除非准备断然逃避这一切，否则只能想办法变适合；想通过推辞领导职位回避的性格缺陷，到头来还是逃不过。", "evidence": ["E32", "E33"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者声明不是建议'只管上'，只是说性格软弱与否不应成为重大考量因素，应更多考量别的因素。", "evidence": ["E34", "E35"]}
   ],
   "argument_steps": [
    "要求先定义'性格软弱'（P001）",
    "论证怕得罪人是普遍人性，几乎所有权都由性格软弱者担任（P002-P007）",
    "转折：领导显得强硬另有原因（P008-P009）",
    "理由A：职责、战略、原则造成无法避免的得罪，责任感等画下底线（P010-P017）",
    "解释强硬表现：看到退无可退的理由，性格未变而表现变硬（P018-P020）",
    "反驳新手开导策略的四点可行性（P021-P025）",
    "理由B：人格发育不健全者使所有选择被堵死（P026-P036）",
    "限定：领导不能自由选择团队成员与客户（P037-P039）",
    "结论：关键在有无忍耐的坚强（P040-P041）",
    "扩展追问：家庭角色中天然是绝对领导，逃避不了（P042-P051）",
    "收束限定：并非主张'只管上'（P052-P053）"
   ],
   "concept_usage": [
    {"term": "性格软弱", "meaning": "本文若指'怕得罪人'则视为普遍人性；作者最终把它重定义为有无'打落牙齿往肚里咽'的忍耐的坚强", "evidence": "P040", "ambiguity": "两种用法（怕得罪人／缺乏忍耐）在文中并存"},
    {"term": "得罪人", "meaning": "领导岗位上无法完全避免的现实后果（裁员、面谈等）", "evidence": "P010", "ambiguity": "无"},
    {"term": "底线", "meaning": "责任感、契约义务、战略目标、更大利害关系为'怕得罪人'划出的界限", "evidence": "P017", "ambiguity": "无"},
    {"term": "退无可退的理由", "meaning": "领导表现出强硬的原因，作者称绝大多数出于此", "evidence": "P018", "ambiguity": "该理由的具体内容未穷举"},
    {"term": "人格发育不健全", "meaning": "以自身标准要求一切、不以对方自由权利为念的人", "evidence": "P026", "ambiguity": "无判定标准，仅举例"},
    {"term": "天然的、绝对的领导", "meaning": "家庭关系中（父母、配偶、子女）不可推辞的领导位置", "evidence": "P043", "ambiguity": "权限边界未说明"},
    {"term": "礼贤下士、不耻下问", "meaning": "被上述人利用为'发挥影响力'良机的做法", "evidence": "P034", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "现实人物：李天一及'不知死活的富二代官二代'（P004），作者列为会被淘汰的反面例子；相关事实属作者表述，待外部核查",
    "公司业绩不佳要裁员、人事主管做裁员面谈（P012-P016），作者用作职责所在不得不罪人的例证",
    "东亚领导者顾虑损失面子、威信从而丧失动员力（P019），作者称想没想错另说，但动机如此",
    "人格不健全者的三种表现：不听建议即不知好歹、没回礼即有意怠慢、超过三分钟不回即故意欺负人（P027-P029），作者例证",
    "被动的团队成员与客户对接情形（P037-P038），作者例证",
    "家庭角色清单：父母、配偶、子女（P043-P046），作者用作'逃不掉'的论据"
   ],
   "conditions": [
    "若'软弱'指怕得罪人，则论断成立（P002）",
    "在某些情况下，无法避免要造成得罪人的现实（P010）",
    "结论以'排除掉这种大概率会被淘汰的人'为限（P006）",
    "四点不可行的条件：涉机密、正常管理操作、时间精力机会不足、对方难以超越个人得失（P021-P024）",
    "即使团队成员的选择权完全在你手里，仍可能看走眼或从别人手里接手（P037）",
    "除非准备断然逃避家庭角色，否则只能想办法变适合（P050）"
   ],
   "rhetoric_and_tone": "第二人称直接对话，反问连用（'你能不去吗？''爹妈你有吗？''你还有多少地方可逃？'）；冷峻训诫夹杂口语调侃（'专门负责发红包的吗？'）；以反常识断言重定义'软弱'；对人格不健全者的描述带讽刺；结尾自我设限，明确否认鼓励'只管上'。",
   "unresolved_questions": [
    "文中提到李天一与'富二代官二代'并称'结果你们也看见了'，所指事件未在文内说明，需外部核查",
    "'东亚领导者'的具体范围与依据未说明",
    "'某种原因看到了退无可退的理由'中的'某种原因'未具体化",
    "家庭关系中'绝对的领导'的权限边界未说明",
    "本篇无图片节点；无 provenance/superseded 版本差异说明（updated_at 晚于 published_at）"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你要定义一下什么叫“性格软弱”，这话才有实在的意义。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "没有什么正常人会不怕得罪人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "即使是强力机关的领导，也绝不是无脑“不怕得罪人的人”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这种症状也见于一些类似李天一这种不知死活的富二代官二代。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "前者一般命不长", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "大部分人都是怕得罪人——或者不愿意得罪人的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "其实几乎所有的领导都是性格软弱的人担任的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "这不是因为ta们性格上很特殊，而是因为别的原因。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "绝大多数都是因为ta们基于某种原因看到了退无可退的理由。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "职责所在、战略所在、原则所在，你没得选择。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "责任感、契约义务、战略目标、更大的利害关系给“怕得罪人”画了一条底线。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "ta的性格其实完全没变，但是客观表现自然而然的会强硬一些。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P021", "quote": "1）有很多是机密，根本不能说；", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "2）有很多是正常的管理操作，被调动者天然有义务要服从", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P023", "quote": "3）你未必有时间、有精力、有机会去做这项开导安慰的工作；", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "人能超越自己的个人得失去理解别人导致自己受损的举动是非常难得的个人品质", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "B）很遗憾，有的人人格发育不健全，别人没有办法不得罪ta。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P031", "quote": "一切都要尊重ta的标准，照顾ta的感受，服从ta的道德观", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P032", "quote": "这种是非标准就是ta们脑海中的这种。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "结果总是被这样的人利用来作为“发挥影响力”的良机", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P035", "quote": "又会被定义为搞个人崇拜、偏听偏信。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P036", "quote": "逻辑上所有的选择都被堵死，其实你根本没有不得罪这些人的可能。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "你其实也不能完全自由的选择团队成员和客户。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "更多的时候会是客户非常好，只可惜派来和你的人对接的是这样的人。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P040", "quote": "而是指你有没有这种打落牙齿往肚里咽的忍耐的坚强。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "没有这份坚强的话，的确不适合。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P042", "quote": "但是不适合，你就真的可以不做吗？", "relation": "context"},
    {"key": "E28", "paragraph_id": "P043", "quote": "你就是子女长大前天然的、绝对的领导。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P044", "quote": "你是对方一生中一切脆弱无助时天然的、绝对的领导。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P046", "quote": "你就是ta们将来老无所能时绝对天然的、绝对的领导。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P048", "quote": "你还有多少地方可逃？", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P050", "quote": "不适合，除非你准备断然的逃避上面这一切，否则你只能想办法变适合", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P051", "quote": "到头来那一日，还是逃不过。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P052", "quote": "我不是建议你说“只管上”，我只是告诉你性格软弱与否在这里不应该成为一个重大的考量因素。", "relation": "qualifies"},
    {"key": "E35", "paragraph_id": "P053", "quote": "你应该更多的考量别的因素来决定。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理", "领导力", "人格与心理", "家庭伦理"],
   "issue_candidates": ["性格软弱与领导胜任力", "怕得罪人的普遍性", "裁员等得罪人的职责", "家庭角色的不可推辞"],
   "text_function_candidates": ["答疑", "经验总结", "训诫", "论辩"],
   "object_candidates": ["李天一", "东亚领导者", "人事主管", "典狱长"],
   "working_keywords": ["怕得罪人", "退无可退的理由", "打落牙齿往肚里咽", "人格发育不健全", "天然的、绝对的领导"]
  },
  "notes": "正文2240字／53段，无图片。brief 只覆盖开头（开头与正文重合），全部判断据正文 P001-P053。文中李天一及'富二代官二代'等现实人物断言属作者表述，已登记待外部核查。"
 },
 "6f4e8c53": {
  "analysis": {
   "question_context": "提问者（Q001）问：无法保证自己正确的知识是否不应当说给别人。作者引用在一座清真寺墙上看到的一句话'不要用你自己不相信的东西教导人'，据此区分'欺骗'与'僭越'：相信自己所说的即不构成欺骗，但无权利说的话仍然不能说；真正的禁忌是僭越，并给出三条说话注意事项。作者同时公开求助该格言的确切出处。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "交代引语来源：在一座清真寺墙上看到这句话，因此对伊斯兰教保持尊重和敬畏。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "被引格言本身：不要用你自己不相信的东西教导人；作者请求读者告知确切出处。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "作者解释：该句解决了传递信息时不可避免的失误与扭曲带来的道德困境——只要自己确实相信，无论客观对错都不存在欺骗问题。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014"], "summary": "限定与边界：只消解欺骗问题，不等于什么都能说；无权利说的话仍不能说；人没有公共审判权与裁判权。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "真正的禁忌在僭越：先有说这话的权利才谈对错；'你自己相信的'提供免罪保护，因为相信错了只是蠢，蠢无罪。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021"], "summary": "例外条件：有证据证明故意说自己不信的版本时才有罪；作者强调这一区分至关重要。", "role": "transition"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024"], "summary": "被批判现象：有人把别人说法被证伪一律认定为自己被欺骗；作者劝人远离这种人。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029"], "summary": "两条理由与后果：你不是真理之神；这类人对事实的判断能力有严重缺陷，久而久之没人敢反驳ta。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035"], "summary": "总结三条注意事项：不僭越表达边界（最主要是不经邀请评判他人人品）、不讲自己不相信的东西、当心对这两条没概念的人。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P036", "P037", "P038"], "summary": "行动建议：表达前先试探对方态度，若犯禁忌则敷衍回避，保命要紧。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "被引格言：不要用你自己不相信的东西教导人（作者在一座清真寺墙上看到，出处未确定）。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这句话解决了传递信息时不可避免的失误和扭曲带来的道德困境：只要自己的确相信，无论表达客观上对错，都不存在欺骗人的问题。", "evidence": ["E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "negated", "statement": "补充限定：这里仅仅消解了欺骗问题，并不意味着什么都能说、没有其它道德问题。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "你没权利说的话，无论你相不相信，你都没权利说，否则泄露国家机密都没罪了。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问并否定'我相信啥就是绝对真理'的想法，讥讽那样的人就该把诺贝尔奖得全了。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人没有公共审判权、司法权与合法侦查权，对没有合法裁判权的事项只能自己烂肚子里。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讲话真正的禁忌不是客观上对不对（对错无人能定），而在于僭越。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "先有说这话的权利才谈对不对；只要是自己说话时确实相信的东西，即使后来被证明说错也免罪，因为这只是蠢，而蠢是无罪的。", "evidence": ["E14", "E15", "E16"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "除非有证据证明你明明不是这样想、却为达到某种目的故意说一个自己不信的版本给别人，这时才有罪。", "evidence": ["E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人走人生的绝路，是因为一旦发现别人告诉自己的话被事实证明是错的，就深恨别人'欺骗'自己。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被批判的对方立场（作者引述）：不管因为任何原因，只要我认为你讲的东西不符合我对事实的认定，你就一定是骗我，你有罪。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对这种人劝你躲得远远的：你不是真理之神，不可能说的话都符合事实；且这种人逻辑思维能力有严重缺陷，对'事实'的判断能力是江湖神话级别。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "与这类人说话随时可能因与ta的次元真理不匹配而构成大罪，久而久之没人再敢反驳ta。", "evidence": ["E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说话有三个注意事项：不僭越表达边界（最主要禁忌是没有不经邀请评判他人人品的权利）、不对别人讲自己不相信的东西（这是实质的欺骗）、当心对这两条没概念和不接受的人。", "evidence": ["E25", "E26", "E27", "E28", "E29"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "保险起见可先试探对方对这两条的态度，若对方犯这两条禁忌，就敷衍过去，保命要紧。", "evidence": ["E30", "E31", "E32"]}
   ],
   "argument_steps": [
    "引出并引用清真寺墙上的格言，同时声明出处不确定（P001-P004）",
    "给出作者的解释：相信自己所说的即不构成欺骗，因而消解道德困境（P005-P006）",
    "自我限定：只消解欺骗问题，不豁免其它道德问题（P007）",
    "补充边界：无权利说的话仍不能说；人无公共审判权与裁判权（P008-P014）",
    "提出真正禁忌在于僭越，并说明'你自己相信的'提供免罪保护（P015-P019）",
    "给出例外：故意说自己不信的版本才有罪（P020-P021）",
    "批判把被证伪等同于欺骗的人，并劝远离（P022-P024）",
    "给出两条理由与后果（P025-P029）",
    "总结三条说话注意事项（P030-P035）",
    "落到行动建议：先试探、后敷衍、保命要紧（P036-P038）"
   ],
   "concept_usage": [
    {"term": "僭越", "meaning": "讲话真正的禁忌：越过自己合法的表达边界", "evidence": "P016", "ambiguity": "合法边界的具体来源未说明"},
    {"term": "合法的裁判权／公共审判权", "meaning": "说话资格的前提，作者以法官、侦查权、陪审团作类比", "evidence": "P013", "ambiguity": "由谁授予未说明"},
    {"term": "你自己相信的", "meaning": "免罪保护条件：说话时确实相信，被证伪也不算欺骗", "evidence": "P018", "ambiguity": "如何证明'确实相信'未说明"},
    {"term": "欺骗", "meaning": "被区分为相信自己所说的（不是欺骗）与故意讲自己不信的版本（实质的欺骗）", "evidence": "P034", "ambiguity": "无"},
    {"term": "蠢", "meaning": "相信了错误的东西；作者称蠢是没罪的", "evidence": "P019", "ambiguity": "是道德还是法律判断未限定"},
    {"term": "次元真理", "meaning": "讽刺用语，指这类人自认的'事实'标准", "evidence": "P027", "ambiguity": "无"},
    {"term": "真理之神", "meaning": "讽刺用语，指自以为相信即真理者", "evidence": "P012", "ambiguity": "无"}
   ],
   "examples_and_targets": [
    "清真寺墙上看到的一句话（P001）：作者引用的格言，并公开求助确切出处（P004）",
    "泄露国家机密（P008）：作者用作'没权利说的话'的极端例",
    "'你相信班花在谈恋爱'（P009）：作者用作无传播权利的信息之例",
    "亚里士多德'浑身都不对'（P015）：作者用来说明对错判断随时间变化",
    "被批判对象：'你就一定是骗我，你有罪'式的判断者（P023）与'次元真理'者（P027）",
    "修辞材料：'道旁白骨累累，还往这路上走，真的嫌命长么？'（P029）"
   ],
   "conditions": [
    "只要你自己的确相信是如此，就不存在欺骗问题（P006）",
    "你没权利说的话，无论相不相信都没权利说（P008）",
    "只要是你没合法裁判权的事项，就只能自己烂肚子里（P014）",
    "先有说这话的权利，然后才能谈说的话对不对（P017）",
    "除非有证据证明故意说了自己不信的版本，才有罪（P020）",
    "建议在对方询问意见后、表达前先试探对方对这两条禁忌的态度（P036）"
   ],
   "rhetoric_and_tone": "引用加解释的答疑体；对宗教格言表示尊重敬畏并公开求助出处；大量反问与反讽（'难道我相信啥，啥就是绝对真理？''你搬一座出来我看看？''司考能考得过吗？'）；黑色幽默（'自己烂肚子里''道旁白骨累累''保命要紧''哈哈，今天晚上天气真好'）；总结部分改用编号列表。",
   "unresolved_questions": [
    "所引格言的确切出处作者本人未确定并在正文请求读者告知（P004），属待外部核查",
    "'你没合法裁判权的事项'的判定主体与范围，正文未说明",
    "'蠢是没罪的'是道德判断还是法律判断，正文未作限定",
    "P003 为 heading 字段，所引格言单独成行；本条为被引内容，非作者原创表述",
    "本篇无图片节点；无 provenance/superseded 版本差异说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有一句话，是我在一座清真寺的墙上看到的", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "不要用你自己不相信的东西教导人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "（有熟悉圣训的朋友烦请告知这句话的确切出处，因为我找了很久了", "relation": "context"},
    {"key": "E4", "paragraph_id": "P005", "quote": "这句话非常优美的解决了你对人传递信息时不可避免的失误和扭曲所带来的道德困境。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "你都并不存在欺骗人的问题。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "这里仅仅只是消解了欺骗问题，可没说这就意味着啥你都能说、没有任何其它道德问题——", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P008", "quote": "你没权利说的话，无论你相不相信，你都没权利说——否则泄露国家机密都没罪了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "难道我相信啥，啥就是绝对真理？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "真是这样的话，你就是真理之神了", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "你没有公共审判权，你不是有司法权的法官，你没有合法的侦查权", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "你就只能自己烂肚子里", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "这是讲话真正的禁忌——不是什么客观上对不对", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "真正的禁忌在于僭越。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P017", "quote": "你先有说这话的权利，然后才能谈说的话对不对。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "那么即使后来被证明说错了，你也是免罪的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "因为这只是蠢，而世人谁不蠢？蠢是没罪的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "除非有证据证明你明明不是这样想的、你却为达到某种目的故意不这么说，说了一个你自己不信的版本给别人，这时候你才有罪了。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P022", "quote": "很多人为此走了人生的绝路", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "“不管因为任何原因我认为你讲的东西不符合我对事实的认定，你就一定是骗我，你有罪！”", "relation": "contradicts"},
    {"key": "E20", "paragraph_id": "P024", "quote": "这种人，你知道死活的话，劝你躲得远远的。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P025", "quote": "第一，你不是真理之神，你不可能说的话都符合事实。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "第二，脑子里这样想问题的人逻辑思维能力有严重缺陷", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "都不定哪一天就会因为与ta的次元真理不匹配而构成十恶不赦的大罪。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P028", "quote": "久而久之，没人再敢反驳ta了", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P030", "quote": "所以，最后的总结是——你想说什么话，有三个注意事项：", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P031", "quote": "1）注意不要僭越自己的表达边界。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P032", "quote": "最主要的禁忌是你没有不经邀请评判他人人品的权利", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P033", "quote": "2）不要对别人讲你自己不相信的东西。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P035", "quote": "3）当心对这两条没概念和不接受的人。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P036", "quote": "在你表达前先试探一下对方对这两条的态度", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P037", "quote": "如果有的话，你就“哈哈，今天晚上天气真好”。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P038", "quote": "保命要紧。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言伦理", "道德哲学", "宗教格言", "言论边界"],
   "issue_candidates": ["说自己不相信的话是否构成欺骗", "表达边界与僭越", "裁判权与发言资格", "如何对待把被证伪当成欺骗的人"],
   "text_function_candidates": ["答疑", "解释", "训诫", "批评"],
   "object_candidates": ["伊斯兰教", "清真寺", "圣训", "亚里士多德"],
   "working_keywords": ["僭越", "合法的裁判权", "次元真理", "真理之神", "实质的欺骗", "保命要紧"]
  },
  "notes": "正文1422字／38段，无图片。P003 为 heading 字段，是所引格言而非作者原创，已按 quoted_or_cited 处理；其确切出处待外部核查（作者本人在 P004 亦请求读者告知）。brief 与正文开头重合，全部判断据正文 P001-P038。"
 },
 "848b2ead": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者（Q001）问：现在是不是一个礼崩乐坏的时代。作者不直接评判当下，而是批评儒家'复三代之治'的框架：认为理想社会必定是稳定到打不破的礼乐秩序带有政治天真性，并举出反证——任何时代都注定礼崩乐坏。本篇含 1 个图片节点，图片内容未核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开门判断：孔夫子在这一点上执迷不悟。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "指认儒家的政治天真性：理想状态是一套打不破的礼乐，且认为周公制礼作乐已完成此事。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "反驳：人类不可能制定无穷适应未来的礼乐；这种理想剥夺发展权与变化权。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "以父亲怀念幼儿听话作类比反讽，反问是否要约手术缩回去。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P009"], "summary": "结论：无论礼乐是什么，任何时代都注定礼崩乐坏。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011", "P012"], "summary": "反事实推演：若真进入礼不崩、乐不坏的理想状态，大概是'全员NPC'；其后接图片节点 IMG001。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "孔夫子在'礼崩乐坏'这一点上属于执迷不悟。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "儒家对礼崩乐坏与复三代之治的强调，使其总体框架带着背景性的政治天真性：以为理想社会状态必定稳定到打不破，礼乐不再崩坏即达最终理想。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "更天真之处在于他们认为此事已由周公制礼作乐完成，所要做的只是想办法让旧日再来。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原教旨主义者根子里有倔强。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人类不可能智慧到制定一套无穷适应未来的礼乐。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种理想等于剥夺人类社会的发展权甚至变化权，永远诅咒一切导致礼崩乐坏的发展。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论'礼乐'是什么，任何时代都注定礼崩乐坏。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果真如孔子所说进入'无论怎么折腾都礼不崩、乐不坏'的理想状态，那大概就是'全员NPC'。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被批评的儒家（孔子）立场：理想社会有一套稳定到打不破的礼乐，且周公制礼作乐已经完成了这件事。", "evidence": ["E2", "E4", "E5"]}
   ],
   "argument_steps": [
    "先给出判断：孔子执迷不悟（P001）",
    "归纳儒家框架：理想状态是打不破的礼乐秩序（P002-P003）",
    "进一步指认其认为周公已完成制礼作乐（P004）",
    "以'根子里的倔强'作讥评（P005）",
    "反驳：人类不可能制定无穷适应未来的礼乐，该理想剥夺发展权与变化权（P006）",
    "以幼儿听话的类比作反讽（P007-P008）",
    "得出结论：任何时代都注定礼崩乐坏（P009）",
    "反事实推演其终局为'全员NPC'（P010-P012）"
   ],
   "concept_usage": [
    {"term": "礼崩乐坏", "meaning": "儒家视为应被克服的失序状态；作者反转为任何时代的常态", "evidence": "P009", "ambiguity": "作者未正面回答当下是否处于礼崩乐坏"},
    {"term": "复三代之治／先王之治／三代之治", "meaning": "儒家式理想社会的不同称谓", "evidence": "P002", "ambiguity": "三者关系未说明"},
    {"term": "政治天真性", "meaning": "作者对儒家的评语：认为理想社会状态一定稳定到打不破", "evidence": "P002", "ambiguity": "无"},
    {"term": "礼乐", "meaning": "一套规范与秩序；作者称其任何时代都注定崩坏", "evidence": "P006", "ambiguity": "作者未定义礼乐的具体内容"},
    {"term": "发展权／变化权", "meaning": "作者称该理想所剥夺的人类社会权利", "evidence": "P006", "ambiguity": "无"},
    {"term": "全员NPC", "meaning": "作者对'礼不崩、乐不坏'终局的比喻性描述", "evidence": "P012", "ambiguity": "字面还是比喻、是否与所附图片对应，均未说明"}
   ],
   "examples_and_targets": [
    "被批评与反驳的对象：孔子、儒家、'复三代之治'、周公制礼作乐（P001-P004）",
    "类比材料：'还是你小时候可爱，那时候你总坐爹腿上缠着爹讲故事。'与'那要不，约个手术缩回去？'（P007-P008）",
    "图片节点 IMG001（位于 P012'全员NPC。'之后）：内容未核验，用途不明"
   ],
   "conditions": [
    "反事实推演以'如果真如孔子所说'为前提（P010）",
    "'任何时代都注定礼崩乐坏'未附条件（P009）",
    "作者以'这个简单说就是不可能的'作强断言（P006）"
   ],
   "rhetoric_and_tone": "短评式讥评与反讽；'执迷不悟''根子里的倔强'带贬抑；以父亲怀念幼儿听话与'约个手术缩回去'作调侃式归谬；以'全员NPC'收束；全文447字，多为断言，未给出处。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001，src=//asset.sooon.ai/p/2020-07/07/134fa623a41dade74931a4dbf5ea885f.jpg），图片内容未核验，需人工或多模态复核；其位于 P012'全员NPC。'之后，是否承担该句的视觉说明无法确认",
    "'儒家'是被当作整体还是特指某派，正文未区分",
    "'全员NPC'的含义（比喻抑或字面）未展开",
    "提问者问的是'现在'是否礼崩乐坏，作者未直接就当下作答",
    "无 provenance/superseded 版本差异说明（updated_at 晚于 published_at）"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "孔夫子在这一点上属于执迷不悟。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "儒家常年强调“礼崩乐坏”“复三代之治”", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "认为“理想的社会状态”肯定是一种稳定到打不破的社会状态。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "然后从此此礼再也不崩、此乐再也不坏，这样就达到了最终理想了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "伟大的周公制礼作乐，已经搞定了这事，我们所要做的就是想办法让旧日再来。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "原教旨主义者真的都有点……根子里的倔强。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "人类不可能智慧到制定一套无穷适应未来的礼乐，这个简单说就是不可能的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "这种理想等于剥夺了人类社会的发展权，甚至是变化权", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "无论“礼乐”是什么，任何时代都注定礼崩乐坏。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "如果真如孔子所说，人类有一天进入了“无论怎么折腾都礼不崩、乐不坏”的“理想状态”的话，", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "全员NPC。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["思想史", "政治哲学", "儒家研究"],
   "issue_candidates": ["礼崩乐坏的普遍性", "复三代之治的政治天真", "理想社会与稳定性的关系", "发展与秩序"],
   "text_function_candidates": ["评论", "批评", "短评"],
   "object_candidates": ["孔子", "儒家", "周公", "三代之治"],
   "working_keywords": ["礼崩乐坏", "复三代之治", "先王之治", "周公制礼作乐", "全员NPC", "政治天真性"]
  },
  "notes": "本篇含 1 个图片节点（IMG001），图片内容未经核验，故 status=needs_reread、image_checked=False；正文文本447字／12段已完整阅读（full_text_checked=true 仅指文本部分）。图片位于 P012'全员NPC。'之后，需图像核验其内容与作用。brief 与正文开头重合，判断均据正文 P001-P012。"
 },
 "a9f6721f": {
  "analysis": {
   "question_context": "提问者（Q001）问：如果人类现在要炸掉地球有什么可行的方案。作者承认'有'，但拒绝公开讨论，并由此提出并非所有问题都可以当作好奇问题公开谈论，批评把危险问题当智力竞赛挑战的做法与技术/工具无罪论。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "承认存在方案，但声明不宜在大众媒体讨论。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "理由与例证：并非所有问题都可当作好奇的问题公开谈论，并列举危险问题类型。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "判断：把这类问题当成兴致勃勃的智力竞赛来挑战是不对的。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "结论：技术/工具无罪论是可怕的天真——如果不是一种邪恶的话。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "存在炸掉地球的可行方案（作者答'有'，但未给出内容）。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这（类方案）不宜在大众媒体讨论。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界上并不是什么问题都可以当作好奇的问题去公开谈论。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把'最少炸药炸死最多人'这类问题当成兴致勃勃的智力竞赛来挑战，是不对的。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "技术/工具无罪论是一种可怕的天真——如果不是一种邪恶的话。", "evidence": ["E6"]}
   ],
   "argument_steps": [
    "先承认存在可行方案（P001）",
    "立即设限：不宜在大众媒体讨论（P002）",
    "给出理由并列举同类危险问题（P003-P004）",
    "判断：把这类问题当智力竞赛挑战是不对的（P005）",
    "归结到对'技术/工具无罪论'的批评（P006）"
   ],
   "concept_usage": [
    {"term": "技术/工具无罪论", "meaning": "作者批评的观点，被称为可怕的天真，甚至可能是邪恶", "evidence": "P006", "ambiguity": "该论的具体主张与代表人物未说明"},
    {"term": "大众媒体讨论", "meaning": "作者认为危险方案不宜进入的公开传播场景", "evidence": "P002", "ambiguity": "是否也禁止私下或专业讨论未说明"},
    {"term": "好奇的问题", "meaning": "作者否认所有问题都可以按'好奇'来公开谈论", "evidence": "P003", "ambiguity": "可公开谈论的判据未给出"}
   ],
   "examples_and_targets": [
    "提问者索要的炸地球方案：作者承认有但拒绝给出内容（P001-P002）",
    "危险问题清单：'使用最少的炸药炸死最多的人'、'如何最有效的破坏大桥/大坝'、'如何用家常物品制作炸弹'、'捆住一个人最短需要多少绳索'（P004），作者用作不当公开讨论的例子",
    "被批评对象：把此类问题当成智力竞赛者（P005）与'技术/工具无罪论'（P006）"
   ],
   "conditions": [
    "承认'有'以'不宜在大众媒体讨论'为限（P002）",
    "论断针对'公开谈论'这一场景（P003）",
    "对'技术/工具无罪论'的评价带'如果不是一种邪恶的话'的保留（P006）"
   ],
   "rhetoric_and_tone": "极简答复，'有。'独立成段后立即设限；以引号列举排比呈现危险问题；'可怕的天真——如果不是一种邪恶的话'为递进式道德评价；全文167字，未展开论证。",
   "unresolved_questions": [
    "作者称'有'可行方案，但未给出任何方案内容或判断依据，无法核验",
    "'不宜在大众媒体讨论'的范围（是否包括私下、学术或专业讨论）未说明",
    "'技术/工具无罪论'的具体所指与代表观点未说明",
    "本篇无图片节点；无 provenance/superseded 版本差异说明"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "有。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "但是这不宜在大众媒体讨论。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "世界上并不是什么问题都可以当作好奇的问题去公开谈论。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "比如“使用最少的炸药炸死最多的人”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "把这个当成一种兴致勃勃智力竞赛来进行挑战，这是不对的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "技术/工具无罪论是一种可怕的天真——如果不是一种邪恶的话。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["技术伦理", "传播伦理", "公共安全"],
   "issue_candidates": ["危险知识的公开讨论边界", "好奇心的限度", "技术中立性"],
   "text_function_candidates": ["答疑", "拒答", "批评"],
   "object_candidates": ["unknown"],
   "working_keywords": ["技术/工具无罪论", "大众媒体", "智力竞赛", "公开谈论"]
  },
  "notes": "正文仅167字／6段，为极短答复；作者明确拒绝给出方案内容。brief 与正文重合，判断均据正文 P001-P006。无图片。"
 },
 "328145aa": {
  "analysis": {
   "question_context": "提问者（Q001）问：如何看待14岁女孩与男友开房被父亲发现后被打骨折。作者未评论该具体事件，而是对父母给出一套预防性教育主张：成长期是唯一有效的干预窗口，父母的首要甚至唯一根本责任是'正确的社会化'，事后动用权力物理阻止无效且会赔上亲子情分。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "行动建议：长成前培养品味、性格与观察力；自由是需要剑术与武德相配的技能；未负全责者无资格寻求或许诺亲密关系。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "强弱论证：这些是唯一有希望降低此类事件几率的策略；子女长成后什么都来不及，只能等结果买单且不能归咎于ta。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009"], "summary": "否定：事后以社会性、经济性乃至暴力性权力物理阻止，不但阻止不了，还要拿亲子情分陪葬。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "强调时机：成长期是唯一真正有效的机会窗口；反问父母此时在做什么——在揪耳朵改数学题、补语文卷子，等于什么都没做。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017"], "summary": "讽喻后果：只能祈祷成绩换来金钱去补人生方向性错误；'求仁得仁'。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "正面主张：教育的首要甚至唯一根本责任是正确的社会化；知识学习要服务于正确的社会化，二十岁开始学数理也不晚。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "三个反例与反问：北大骄子/斯坦福博士杀人自尽、全A骄女卖身供赌、奥赛冠军削发避世。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027"], "summary": "附注：'无意冒犯佛教'。", "role": "other"},
    {"unit_id": "U009", "paragraph_refs": ["P028"], "summary": "正文尾部残留'家族答集''第一性'（平台标签混入正文，且该尾部未被 lexical 覆盖）。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应在子女没有长成之前，提前培养ta们的品味和性格，教导ta们耐心学习自由。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "培养性格可使贪心的人不能不讨厌和回避ta们，让ta们自然而然地成为更麻烦的目标。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "培养观察力，让ta们观察危险的贪婪信号与贪婪关系的恶性结局，从而自然而然地厌恶这样的人。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自由不仅仅是一种权利，还是一种复杂的技能，需要与之相配的剑术和武德。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "完全为自己的行为负全责并且有充分承担责任的经验之前，人既没有资格寻求亲密关系，也没有资格许诺亲密关系。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这些是唯一有希望降低这种恶性事件几率的策略。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "一旦子女长成而没培养出那样的品味和性格，就什么都来不及，只能等最后结果买单且不能归咎于ta。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "事后动用社会性、经济性乃至暴力性权力物理阻止子女行使自由，不但阻止不了事情发生，还要拿最后一点亲子情分陪葬。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "能干预结果的最佳时机、甚至某种意义上唯一有效的时机，是ta还没有关闭聆听的耳朵、还没有移开注视的眼的成长期。", "evidence": ["E10", "E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问父母此时在做什么，并指出其在揪着ta的耳朵叫ta改数学题、补语文卷子，等于什么都没做。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "事到临头只能祈祷数学分数与语文作文的优秀，让ta能找到足够赚到补上这些人生方向性错误的金钱。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以'这是你自己求的仁''求仁得仁，复何求'讽喻父母自食其选择的结果。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对父母而言，正确的教育的首要甚至唯一根本责任是正确的社会化：建立引正避邪、坚韧不拔的强壮而健康的人格与宁枉勿纵的观察方法。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "数学、物理等知识对具备健全人格者即使二十岁才真正入手也不晚；在这之前，知识的学习要服务于正确的社会化。", "evidence": ["E20", "E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "以三个反例反问：教出北大骄子/斯坦福博士枪杀导师后自尽、全A骄女卖身供赌、奥赛冠军削发避世的结局是否可以接受。", "evidence": ["E22", "E23", "E24", "E25"]}
   ],
   "argument_steps": [
    "给出预防性教育清单：品味、性格、观察力、自由的技能与武德（P001-P005）",
    "断言这是唯一有希望降低恶性事件几率的策略（P006）",
    "指出长成后已来不及，只能等结果买单、不能归咎于ta（P007-P008）",
    "否定事后以社会性、经济性、暴力性权力物理阻止的做法（P009）",
    "反复强调唯一有效时机是成长期，并反问父母当时的作为（P010-P014）",
    "以'求仁得仁'讽喻后果（P015-P017）",
    "提出正面主张：教育首要乃至唯一根本责任是正确的社会化（P018-P021）",
    "以三个反例与反问收束（P022-P025）",
    "附注'无意冒犯佛教'（P026-P027）"
   ],
   "concept_usage": [
    {"term": "自由", "meaning": "不只是权利，还是需要剑术与武德相配的复杂技能", "evidence": "P004", "ambiguity": "剑术与武德的具体所指未说明"},
    {"term": "负全责", "meaning": "寻求与许诺亲密关系的前置资格与经验条件", "evidence": "P005", "ambiguity": "如何认定'充分的经验'未说明"},
    {"term": "正确的社会化", "meaning": "作者称其为父母教育首要甚至唯一的根本责任", "evidence": "P018", "ambiguity": "具体内容与判定标准未给出"},
    {"term": "观察方法", "meaning": "系统的、高概率的、宁枉勿纵的对可纳入生命生态者的观察方法", "evidence": "P019", "ambiguity": "无"},
    {"term": "机会窗口", "meaning": "子女成长期这一唯一有效的干预时机", "evidence": "P011", "ambiguity": "无"},
    {"term": "求'仁'得'仁'", "meaning": "反讽用法，指父母自己选择的教育方式带来的结果", "evidence": "P017", "ambiguity": "与儒家'仁'的原义关系未说明"}
   ],
   "examples_and_targets": [
    "提问所指具体事件（14岁女孩与男友开房、被父亲打成骨折）在正文中完全未被提及或评论，作者只作一般性父母策略论述",
    "反例一：北大骄子、斯坦福博士枪杀导师屠杀同学后自尽（P022）",
    "反例二：全A骄女毕业后卖身卖血供烂赌鬼还债、骗尽亲友（P023）",
    "反例三：奥赛小冠军、少年班毕业万念俱灰削发避世（P024）",
    "修辞材料：'是你可以接受的结局吗？'（P025）、'施主请回，俗我已死'（P024）、'ps：无意冒犯佛教'（P026-P027）",
    "平台标签残留：'家族答集''第一性'（P028），该尾部未被 lexical 覆盖"
   ],
   "conditions": [
    "建议适用于'在子女没有长成之前'（P001）",
    "资格条件：完全为自己的行为负全责并且有充分的承担责任的经验之前（P005）",
    "'一旦ta们长成……你就什么都来不及做了'（P007）",
    "唯一有效时机是ta还没有关闭聆听的耳朵、还没有移开注视的眼的成长期（P010）",
    "'即使二十岁才真正开始入手，也远远没什么来不及'（P020）",
    "'在这之前，知识的学习要服务于正确的社会化'（P021）"
   ],
   "rhetoric_and_tone": "第二人称训诫与连续反问（'这时候你在做什么？''是你可以接受的结局吗？'）；'我再说一遍'反复强调；排比式反例制造警示；'求“仁”得“仁”，复何求？'与'施主请回，俗我已死'带反讽；文末'ps：无意冒犯佛教'为免责式补注。",
   "unresolved_questions": [
    "提问所指具体事件与父亲打骨折的行为，正文完全未评论，无法据此判断作者对该事件本身的立场",
    "三个反例未指明具体人物与事件，属概括性叙述，需外部核查",
    "'正确的社会化''引正避邪''宁枉勿纵'的具体内容与判定标准未说明",
    "正文尾部'家族答集''第一性'疑为平台话题标签混入正文；结构记录显示 text 尾部未被 lexical 覆盖（text_tail_not_in_lexical，char_start=1086），正文与结构不一致",
    "本篇无图片节点；无 provenance/superseded 版本差异说明（updated_at 晚于 published_at）"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在子女没有长成之前，提前培养好ta们的品味和性格，教导ta们耐心学习自由。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "让贪心的人不能不讨厌和回避ta们，让ta们自然而然的成为更麻烦的目标。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "培养ta们的观察力，让ta们学会自然而然的去观察几类危险的贪婪信号", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "自由不仅仅是一种权利，还是一种复杂的技能。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "人既没有资格寻求与ta人的亲密关系，也没有资格去许诺亲密关系。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这些是唯一有希望降低这种恶性事件的几率的策略。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P007", "quote": "你就什么都来不及做了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "你只能静静等着为最后的结果买单，并且不能归咎于ta", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "要动用社会性、经济性乃至于暴力性的权力去物理地阻止子女行使ta们相信自己拥有的自由", "relation": "contradicts"},
    {"key": "E10", "paragraph_id": "P010", "quote": "是在ta还没有关闭聆听的耳朵、还没有移开注视的眼的成长期。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "这是你唯一的真正能做点什么的机会窗口。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "这时候你在做什么？", "relation": "context"},
    {"key": "E13", "paragraph_id": "P013", "quote": "你在揪着ta的耳朵叫ta改数学题，补语文卷子。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "你什么都没做。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "你只能祈祷数学分数、语文作文的优秀，让ta能找到足够赚到能补上这些人生方向性错误的金钱了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "这是你自己求的“仁”，你得着了。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "求“仁”得“仁”，复何求？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "对父母而言，正确的教育的首要——甚至是唯一的根本责任——是正确的社会化。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "是建立一个引正避邪、坚韧不拔的强壮而健康的人格", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "即使二十岁才真正开始入手，也远远没什么来不及。", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P021", "quote": "在这之前，知识的学习要服务于正确的社会化。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "教出北大骄子、读到斯坦福博士枪杀导师屠杀同学自尽，肝脑涂地。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P023", "quote": "教出全A骄女，毕业后“一往情深”卖身卖血供烂赌鬼还债，骗尽亲友。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P024", "quote": "教出奥赛小冠军，少年班毕业万念俱灰削发避世", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P025", "quote": "是你可以接受的结局吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭教育", "青少年成长", "人格养成", "伦理教育"],
   "issue_candidates": ["亲子冲突与干预时机", "自由与责任资格", "知识教育与社会化孰先", "青少年亲密关系"],
   "text_function_candidates": ["答疑", "训诫", "经验总结", "警示"],
   "object_candidates": ["父母", "子女", "北大", "斯坦福", "少年班", "佛教"],
   "working_keywords": ["正确的社会化", "机会窗口", "负全责", "剑术和武德", "家族答集", "第一性", "求“仁”得“仁”"]
  },
  "notes": "正文1094字／28段，无图片。提问所指的具体事件在正文中未被提及或评论，作者只给出一般性父母教育策略。文末 P028'家族答集／第一性'疑为平台话题标签混入正文，且该尾部未被 lexical 覆盖（text_tail_not_in_lexical，char_start=1086），结构记录与正文不一致，需研究者注意。三个反例为概括性叙述，待外部核查。"
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
