# -*- coding: utf-8 -*-
"""批次 r001-b0081 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0081.sessions.py            # 写 out/r001-b0081.out.jsonl
  python3 records/r001-b0081.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0081"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0081.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e55438de": {
  "analysis": {
   "question_context": "提问者（Q001）问如何看待大部分男性都强烈主张冠姓权。作者先反驳“说大部分男性强烈主张冠姓权是造谣”这一说法，再由东方文明的“后代观”解释这种主张的心理来源，最后主张：支撑姓氏传承的社会体系已消亡，争冠姓权没有实际意义，应把争夺权拿去交换实际利益，并反省是否挑错了人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "反驳“大部分男性强烈主张冠姓权是造谣”的说法，提出的检测办法是问离婚男性对随母改姓子女的态度。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"],
     "summary": "以改姓后停付生活费、学杂费为例，认为一提钱态度就老实。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"],
     "summary": "质疑自称“对冠姓权无所谓”者是否有孩子，认为未临其事容易大度，真事到临头才算数。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"],
     "summary": "用“由俭入奢易，由奢入俭难”解释男性为何强烈主张冠姓权。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"],
     "summary": "把冠姓问题定性为“后代观”问题：“我有后代”是东方文明未走永生路线时救赎死亡恐惧的思想策略，故传统东方文化对之执念极深。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016"],
     "summary": "指出执念的基础已失效：法律保障的家族强制权利无效化，孝治天下的政治理论被抛弃，忤逆罪消亡，成年人自由改姓成为普遍实践。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018", "P019", "P020"],
     "summary": "对比古今：古人记得族谱与祖宗家法，因为那是求助对象名录与获取资源的资格；福利与约束消亡后，背负这些信息成了额外支出。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026"],
     "summary": "以三四代后被遗忘、说不清曾祖父及其父姓名、缺少遗物与见证为例，论证支撑姓氏传承的社会体系已经消亡。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P027"],
     "summary": "比喻：人们争夺的只是一块转眼就会消失的干冰。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029"],
     "summary": "主张面对争夺最好的策略不是苦争，而是趁其还有“保质期”把争夺权换成有实际意义、不会蒸发的东西。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P030", "P031"],
     "summary": "转向自省：对方如此在乎，应反省是否挑错了人；指出对已无价值的投资品下重本且无自我觉察，令人沮丧。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "“大部分男性强烈主张冠姓权是造谣”这一说法很容易检测：问离婚男性对随母改姓子女的态度即可不攻自破。",
     "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "子女改姓之后，不知多少人就不再给生活费、学杂费。",
     "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned",
     "statement": "口口声声说对冠姓权无所谓的人是否真有孩子值得怀疑；未真有孩子时容易“大度”，真事到临头大度才算数。",
     "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "冠姓本质上是“后代观”问题；“我有后代”是未走永生路线的东方文明救赎死亡恐惧的思想策略，因此传统东方文化对此执念极深。",
     "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "这执念的基础——法律所保障的家族的强制权利——已经无效化了。",
     "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "孝治天下的基本政治理论已被抛弃，忤逆罪已消亡，成年人自由更改姓名已成为普遍的社会实践。",
     "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted",
     "statement": "无论子女姓什么，大约三四代以后大概率会被忘记。",
     "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "支撑姓氏传承的社会体系已经消亡，人们争夺的只是转眼就会消失的干冰。",
     "evidence": ["E009", "E010"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical",
     "statement": "如果对方要争，最好的策略不是苦争，而是趁机把争夺权换成将来不会蒸发的实际东西；主张冠姓权的最明智用法是趁其还值钱时卖出去。",
     "evidence": ["E011", "E012"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified",
     "statement": "对方如此在乎此事，值得反省是否挑错了人；这与对方争取时手段多激烈关系不大，而是对已无价值之物下重本且无自我觉察，令人沮丧。",
     "evidence": ["E013", "E014"]}
   ],
   "argument_steps": [
    "先否定“这是造谣”的说法，给出可检验的反例（离婚男性对改姓子女的态度）。",
    "补充现象：改姓后停付生活费、学杂费；以“提钱才最老实”点出真实态度。",
    "把“无所谓”的宣称限定为尚未有孩子、尚未临事者的容易大度。",
    "用“由俭入奢易，由奢入俭难”解释强烈主张的来源，再转入定性：冠姓本质是“后代观”问题。",
    "给出前提：后代观是东方文明应对死亡恐惧的思想策略，故执念深。",
    "让步式转折：该执念的法律与政治基础（家族强制权利、孝治天下、忤逆罪）已失效。",
    "以族谱、祖宗家法的古今功能对比，说明信息与约束消亡后成本变负担。",
    "用三四代后被遗忘、无实据、无遗物等例证推出结论：传承体系已消亡。",
    "结论：争夺之物如干冰；行动建议：把争夺权换成不会蒸发的东西，趁保质期未到卖给觉得它值钱的人。",
    "收束到自省：可能挑错了人，与手段激烈程度关系不大，问题在于对无价值投资品下重本而无自我觉察。"
   ],
   "concept_usage": [
    {"term": "冠姓权", "meaning": "本文指夫妻争夺子女随父姓还是随母姓的主张与理由；作者把它归入“后代观”问题，并称其已无实际意义。", "evidence": "P012", "ambiguity": "作者既说它是“权”，又说它是最明智策略中可出售的“争夺权”，其权利性质未作界定。"},
    {"term": "后代观", "meaning": "对“我有后代”这一观念的态度；作者称其为不走永生路线的东方文明救赎死亡恐惧的思想策略。", "evidence": "P013", "ambiguity": "“东方文明”“永生路线”在本文未给出定义或范围。"},
    {"term": "干冰", "meaning": "比喻争夺对象转眼就会消失、并无长期价值。", "evidence": "P027", "ambiguity": "是修辞比喻，不是对冠姓权性质的严格界定。"}
   ],
   "examples_and_targets": [
    "离婚男性对女方抚养的子女改姓母姓的态度（作者用作检验“造谣”说法的反例，P003）。",
    "改姓后不再给生活费、学杂费的现象（作者证据，P004）。",
    "自称对冠姓权无所谓的人（作者质疑对象，P006）。",
    "古代人的族谱与祖宗家法（作者用于古今对比的历史叙述，P018）。",
    "闽南门楣上镌刻的“衍派”“传芳”（作者举的地域风俗例证，P019）。",
    "曾祖父的姓名、遗物与见证者（作者用来追问传承实据的例证，P022—P025）。",
    "“说大部分男性强烈主张冠姓权是造谣”的说法（作者反驳对象，P001）。"
   ],
   "conditions": [
    "检测办法依赖的具体条件：问的是离了婚、且子女由女方抚养并改姓母姓的男性（P003）。",
    "“无所谓”的宣称只在尚未有孩子、尚未实际面临时成立（P006—P008）。",
    "成年人自由更改姓名需要一系列法律手续（P016，作者以“尽管”作限定）。",
    "后代观执念的强度限定于传统东方文化之中（P014）。",
    "换置策略以对方确实要争、且仍有人觉得冠姓权值钱为前提（P028—P029）。",
    "三、四代以后的遗忘以“极大概率”表述，非绝对（P021）。"
   ],
   "rhetoric_and_tone": "反问密集（“造谣？”“真的有孩子吗？”“看明白了吗？”），先驳论后立论；把冠姓权比作“干冰”、把争执写为“被割韭菜”，带训诫与调侃；对“无所谓”者用“云淡风轻”“大度”加引号反讽；结论部分自称“冷酷一点说”，语气直接而带劝告。",
   "unresolved_questions": [
    "“由俭入奢易，由奢入俭难”类比冠姓权，其“奢”的具体所指（父姓带来的何种待遇）本文未说明。",
    "“法律所保障的家族的强制权利”具体指哪些法律条文与制度，本文未说明，需外部核查。",
    "“孝治天下”“忤逆罪消亡”的时间与范围（哪个法域、何种罪名）本文未说明，需外部核查。",
    "“三四代以后极大概率忘记”属预测性断言，本文未提供数据或调查依据，需外部核查。",
    "P019“解读：闽南门楣上镌刻的‘衍派’和‘传芳’有什么意义？”在渲染包中标为 ⚠lexical未覆盖片段，疑为平台话题标签或正文中的独立问题行混入。",
    "本篇 lexical divergence=true，正文与结构存在不一致，段落性质需复核。",
    "作者未给出“不主张冠姓权”的正面替代安排，也未说明把争夺权“卖给”对方的具体形式。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P003", "quote": "问问离了婚的男性对女方抚养的子女改姓母姓什么态度，自然不攻自破。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P004", "quote": "改了姓，不知多少人就不给生活费、学杂费了。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P006", "quote": "真的有孩子吗？", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P009", "quote": "真事到临头，还是大度才算数。", "relation": "qualifies"},
    {"key": "E005", "paragraph_id": "P014", "quote": "“我有后代”是没有走永生路线的东方文明救赎死亡恐惧的思想策略。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P015", "quote": "但这执念的基础——由法律所保障的家族的强制权利已经无效化了。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P016", "quote": "忤逆罪已经消亡，成年人自由更改姓名（尽管需要一系列的法律手续）的权利已经成为了普遍的社会实践。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P021", "quote": "大约三四代以后，ta们极大概率会忘记你的存在。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P026", "quote": "支撑姓氏传承的社会体系已经消亡了。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P027", "quote": "人们在争夺的，只不过是一块转眼间就会消失的干冰。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P028", "quote": "而是抓住这个机会将自己的争夺权换一些更有实际意义的、将来不会蒸发的东西。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P029", "quote": "而是拿来趁着保质期没到，赶紧卖给还觉得它值钱的人。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P030", "quote": "你有必要反省一下是不是挑错了人。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P031", "quote": "对这么显然已经没有价值的投资品却因为心理发育滞后而下如此的重本", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别与家庭", "婚姻制度", "文化观念史", "法律与社会变迁"],
   "issue_candidates": ["男性主张冠姓权", "子女姓氏归属", "姓氏传承的社会基础", "后代观与死亡恐惧", "家族强制权利的失效"],
   "text_function_candidates": ["答疑", "反驳", "解释", "分析", "行动建议"],
   "object_candidates": ["传统东方文化", "离婚男性", "闽南地区", "族谱与祖宗家法"],
   "working_keywords": ["冠姓权", "后代观", "族谱", "祖宗家法", "孝治天下", "忤逆罪", "衍派", "传芳", "干冰", "投资品"]
  },
  "notes": "平台为知乎问答，提问字段立场属提问者（Q001），未归给作者。P019 在渲染包标为“⚠lexical未覆盖片段”，P011 后出现字符间隙（201—203），疑有分隔线或平台话题标签混入正文；本篇 divergence=true，正文与 lexical 结构不一致，已登记待复核。"
 },
 "41f48569": {
  "analysis": {
   "question_context": "提问者（Q001）问如何看待大学理工男研究的杀鱼公式、怎样买鱼性价比最高。作者直接判断该分析对买鱼性价比基本没有帮助，理由是鱼市价格基线已含水分、让利空间已被竞争挤压，随后给出替代思路：从降低交易成本入手，并以自己把家常小餐厅调教成私人食堂为例说明具体步骤与要诀。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"],
     "summary": "判断杀鱼公式对买鱼性价比基本没有帮助：价格基线本就含水分，让利部分已被竞争挤压；任何可能进一步压低鱼市老板利润率的策略都行不通，因为老板可以拒卖。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"],
     "summary": "以店家口吻请持此方法者去找接受该交易方式和定价的供货商，小店水平有限伺候不了。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P006"],
     "summary": "提出替代方向：提高交易收益要靠降低交易成本，而不是扣除对方的“不当利润”。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014"],
     "summary": "开始举私人食堂的例子：选一家合意的家常小餐厅，点固定的特殊组合（招牌菜加煎蛋、皮蛋拌豆腐）并提出双面煎溏心等小要求，使后厨能识别出这位客人。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"],
     "summary": "描述回报：这位客人拿到的菜品质不同，可提出更多细节要求，随后获得寄存、充电、特殊点单、折扣乃至代收快递等服务，小店成为生活小据点；在其处买鱼不必写公式，水说不定真的会帮着控干。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"],
     "summary": "总结要诀：接受对方的交易系统、不给对方造成损害利润的负担；多次交易形成惯例以降低交易成本、提高现金流稳定性期望；在对方未付额外成本的情况下继续提改善体验的要求；建立良好关系以扩大“家”的心理范围。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027"],
     "summary": "收束：处久了可以影响餐厅菜谱、定价与经营方式，至少与厨师成为心照不宣的好友；好货会留着、次次合口味；这些点滴温暖的关系让人不必纠结买鱼的水量。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "该杀鱼分析对买鱼性价比基本没有帮助。",
     "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "鱼市场价格基线本按含水量确定，经过竞争博弈后可以让利的部分已被挤压掉；任何可能进一步压低老板利润率的策略都行不通，因为老板可以拒卖。",
     "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "要提高交易收益应从降低交易成本入手，而不是从扣除对方“不当利润”入手。",
     "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified",
     "statement": "接受对方交易系统、不造成对方利润负担的前提下，那些重在改善体验而对方无负担的小要求会被积极满足。",
     "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "多次交易形成惯例可降低交易成本、提高现金流稳定性期望；这份稳定性期望对对方很值钱，是其持续经营的底气。",
     "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified",
     "statement": "建立起良好而积极的关系有大用，最起码可以在实际上扩大你“家”的心理范围。",
     "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "处得久了甚至可以影响餐厅的菜谱、定价策略和经营方式，至少会与厨师成为心照不宣的好友。",
     "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "这些点滴温暖的关系可以让人不必纠结“买鱼的水量”。",
     "evidence": ["E010"]}
   ],
   "argument_steps": [
    "先给结论：杀鱼公式对买鱼性价比没有帮助。",
    "理由一：价格基线按含水量确定，竞争博弈已挤掉让利空间。",
    "理由二：进一步压低利润率的策略会遭拒卖而被排除。",
    "以店家口吻的拟想回应强化该排除（“请您寻找接受这个交易方式和定价的供货商”）。",
    "转向替代问题：怎样提高交易收益——从降低交易成本而非扣对方不当利润着手。",
    "以私人食堂为例，列出选店、点特殊组合、加小要求、规律点单等步骤，说明对方如何识别客人身份。",
    "给出回报清单（寄存、充电、特殊点单、折扣、代收快递、雨伞）与“不必写公式”的结果。",
    "归纳四条要诀：接受对方系统、多次交易形成惯例、继续提无成本改善体验的要求、建立关系。",
    "结论：关系扩大“家”的范围，影响菜谱与经营，最终使买鱼水量不再是纠结对象。"
   ],
   "concept_usage": [
    {"term": "价格基线", "meaning": "鱼市场老板定价时本来就按含水（带水分）的货量确定的价格起点，故扣水不改变可让利空间。", "evidence": "P002", "ambiguity": "未给出量化依据，属作者对市场的判断。"},
    {"term": "交易成本", "meaning": "作者主张应降低的对象，与“扣除对方不当利润”相对；未在本文给出定义或构成项。", "evidence": "P006", "ambiguity": "术语未定义，仅以对比方式使用。"},
    {"term": "现金流稳定性期望", "meaning": "对方因多次交易形成惯例而对未来收入产生的稳定预期，作者称其值钱、能舒缓焦虑。", "evidence": "P022", "ambiguity": "“比黄金还值钱”为修辞性夸张。"},
    {"term": "“家”的心理范围", "meaning": "由良好交易关系扩展出的心理上的归属与便利范围。", "evidence": "P024", "ambiguity": "以引号标出，属作者自造的比喻性表述。"}
   ],
   "examples_and_targets": [
    "大学理工男研究的“杀鱼公式”（提问者引入、作者反驳其效用对象，Q001/P001）。",
    "鱼市场老板与鱼市定价（作者论据，P002—P003）。",
    "作者自己每到一处常住选一家家常小餐厅调教成私人食堂（作者自述经验例证，P008）。",
    "招牌菜加1个煎蛋、加一份皮蛋拌豆腐；煎蛋双面煎带溏心；红烧肉烧烂度、鸡蛋焦边、滴酱油、皮蛋拌开（作者的类比性操作细节，P010/P012/P016）。",
    "临时寄存、临时充电、特殊点单、定制酒席、特殊打折、快递代收、雨伞暂借（作者列举的回报，P017）。",
    "拟想的店家回话“您的方法很好、很强大、很公平”（作者用作修辞性对话，P004）。"
   ],
   "conditions": [
    "对象限定为鱼市场：价格基线按含水量确定、竞争博弈已挤掉让利（P002）。",
    "“任何可能导致利润率进一步下降的策略”都行不通，因为老板可以拒绝交易（P003，条件—结果关系）。",
    "买鱼者需“每到一处常住”，即长期居住，才可能形成规律交易（P008）。",
    "前提是招牌菜得到作者认可，且体现了厨师的某种能力，而不必豪华（P011）。",
    "小要求的边界：重在改善体验、对对方没有负担损失（P021）。",
    "关系扩展以“处得久了”为条件，影响菜谱与经营方式是程度递进的说法（P025）。",
    "作者未说明该策略在只做一次性交易、无固定摊位的场景下是否适用。"
   ],
   "rhetoric_and_tone": "经验传授口吻，第二人称“你”贯穿；以拟想店家回话作反讽（“您的方法很好、很强大、很公平”）；用“调教”“生活小据点”“心照不宣的好友”等带亲近感的措辞；以“我举个例子，你能看懂，将来自然会有收益”建立说教—受教关系；结论部分转为温和的抒情收束。",
   "unresolved_questions": [
    "“杀鱼公式”的具体内容与数学形式本文未说明，也未引用其原文，需外部核查。",
    "鱼市“价格基线按带水分确定”“让利空间已被竞争挤压掉”是作者的断言，本文未提供数据或机制论证，需外部核查。",
    "P023“你可以继续提出这类对方并不需要付出额外太多成本吗而能大幅改善你的体验的要求”中“成本吗而”疑为笔误或输入错误，原样保留。",
    "私人食堂经验与买鱼场景的类推边界（餐厅可识别熟客、鱼摊是否同理）本文未说明。",
    "作者未说明该策略失败的后果或对方不按预期回报时如何处理。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "做这个分析，对于买鱼性价比基本没有帮助。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "因为鱼市场老板的价格基线本身就是按照带着这么多水分来确定的。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "任何可能导致鱼市老板的利润率进一步下降的策略，无论有什么样的大义名分，都是行不通的", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P006", "quote": "你必须从降低交易成本的角度去思考，而不是从“扣除对方的‘不当利润’”的角度思考。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P021", "quote": "首先你要接受对方的交易系统，不要给对方造成明显损害利润的负担。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P023", "quote": "一般都会被积极的满足。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P022", "quote": "多次交易，形成惯例，降低交易成本，提高现金流稳定性期望。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P024", "quote": "最起码，可以在实际上扩大你的“家”的心理范围。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P025", "quote": "你甚至可以影响这家餐厅的菜谱，定价策略和经营方式。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P027", "quote": "这些点滴温暖的关系，可以让你不必纠结“买鱼的水量”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["交易与商业", "日常生活经验", "人际关系"],
   "issue_candidates": ["买鱼性价比与扣水策略", "市场价格基线", "交易成本与人情投资", "长期客户关系的建立"],
   "text_function_candidates": ["答疑", "反驳", "经验总结", "类比说理", "行动建议"],
   "object_candidates": ["鱼市场老板", "家常小餐厅与后厨师傅", "大学理工男（提问引入）"],
   "working_keywords": ["杀鱼公式", "性价比", "价格基线", "竞争博弈", "利润率", "交易成本", "惯例", "现金流稳定性", "私人食堂"]
  },
  "notes": "平台为知乎问答；提问（Q001）提及的“杀鱼公式”属提问者引入的话题，作者并未转述其内容，已在 unresolved_questions 登记。P004 是作者拟想的店家回话，属修辞性对话而非作者引用真实第三方。E003 引文含破折号前的连续片段，未跨句拼接。"
 },
 "8a078085": {
  "analysis": {
   "question_context": "提问者（Q001）问：美籍华人工程师因带公司电脑来中国旅游被美国法院判处38个月监禁，对此怎么看。作者没有评论判决本身，而是从涉密管理角度判断：涉密身份者未经批准出境本就会牵连一串人负责，能把电脑带出去已属安全漏洞，并顺带劝告不要随便接涉密项目。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"],
     "summary": "作者判断该工程师即使没带电脑来中国旅游也会惹麻烦：涉密身份者未经申请批准出境，本来就会有一串人被追责，可能比出境者本人的过失还大。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"],
     "summary": "认为能把涉密电脑带出去更神奇，能带回家就已经是安全漏洞。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"],
     "summary": "顺带给出行动建议：除非自己想好了，不要随便接涉密项目。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted",
     "statement": "这位工程师就算没带电脑到中国旅游，只怕也会惹麻烦。",
     "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "涉密身份的人未经申请和批准出境，本来就会有一串人要负责，搞不好比出境者本人的过失还大。",
     "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "能把电脑带出去更是很神奇，能带回家都已经是安全漏洞了。",
     "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified",
     "statement": "除非自己想好了，不要随便接涉密项目。",
     "evidence": ["E005"]}
   ],
   "argument_steps": [
    "先给出与判决无关的判断：此人即便不带电脑出境也会惹麻烦。",
    "理由：涉密身份者未经申请批准出境会触发连带追责，责任人可能不止本人。",
    "进一步指出管理漏洞：电脑能带出、能带回家已属安全漏洞。",
    "以“顺便”引出对读者的行动建议：想好了再接涉密项目。"
   ],
   "concept_usage": [
    {"term": "涉密身份", "meaning": "承担保密义务、其出境需申请与批准的身份状态。", "evidence": "P002", "ambiguity": "未说明是哪一国的保密制度、由谁审批。"},
    {"term": "安全漏洞", "meaning": "本文指涉密设备被带出可控范围这一管理缺失。", "evidence": "P003", "ambiguity": "仅作断言，未给出具体制度依据。"}
   ],
   "examples_and_targets": [
    "美籍华人工程师因带公司电脑来中国旅游被判38个月监禁（提问者提供的新闻事件，作者以此为讨论背景，Q001）。",
    "“一串人要负责”的连带追责（作者的推断，未给出具体机构或案例，P002）。"
   ],
   "conditions": [
    "作者判断以“涉密身份”为前提，非涉密人员不在其论域内（P002）。",
    "出境需“未经申请和批准”才构成问题（P002）。",
    "劝告带条件：“除非自己想好了”，不要随便接涉密项目（P004）。",
    "“搞不好”“只怕”等词表明作者对判决走向与追责程度的判断均为推测性。"
   ],
   "rhetoric_and_tone": "简短四段，评论式直陈；用“说实在的”“很神奇”带轻微反讽，用“顺便”把话题从个案转向对读者的忠告，语气平淡克制，未对当事人作道德评价。",
   "unresolved_questions": [
    "文章未说明该工程师的涉密级别、所在公司、涉案法域与判决依据，需外部核查。",
    "“未经申请和批准出境本来就会有一串人要负责”中的责任主体、制度依据与“一串人”范围本文未说明。",
    "“能带回家都已经是安全漏洞”属于对涉密设备管理的断言，本文未给出规范条文。",
    "作者未说明自己与涉密项目的经验来源，也未评价38个月刑期是否适当。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "这位就算没带电脑到中国旅游只怕也会惹麻烦。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "涉密身份的人未经申请和批准出境本来就会有一串人要负责，搞不好比出境者本人的过失还大。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "能把电脑带出去更是很神奇", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P003", "quote": "能带回家都已经是安全漏洞了。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P004", "quote": "除非自己想好了，不要随便接涉密项目。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["保密与国家安全", "职场风险", "法律个案评论"],
   "issue_candidates": ["涉密人员出境审批", "涉密设备管控", "连带追责", "是否接涉密项目"],
   "text_function_candidates": ["答疑", "评论", "风险提示"],
   "object_candidates": ["美籍华人工程师", "美国法院", "涉密项目单位"],
   "working_keywords": ["涉密", "出境审批", "安全漏洞", "38个月监禁", "连带责任"]
  },
  "notes": "平台为知乎问答，提问中的新闻事实与刑期属提问者陈述，作者未确认亦未否认，本文未对判决本身作评价。篇幅短（4段120字符），已逐段读完。"
 },
 "27419a6a": {
  "analysis": {
   "question_context": "提问者（Q001）问：战争中男性战死以后，女性有必要反抗到底还是选择投降活着。作者没有直接回答“该反抗还是该投降”，而是先给出一个关于史前部落的推断（战胜部落不虐待战败方妇女儿童），并以长段前置说明预防“用已构造完成的考古遗址反驳”；随后用生育资源与选择压力解释贞操观的起源，最后把问题转为反问：讨论现代贞操观念前必须先回答女性是否是国家/民族的财产、谁有权作此规定等前提问题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"],
     "summary": "提出推断：在最原始的部落状态，战胜部落不会虐待战败方的妇女、儿童。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009"],
     "summary": "括号内的前置防御：在文字、墓葬、祭祀出现之前还有漫长的史前时代，不能用已构造完成的考古遗址论证该阶段不存在；承认现存原始部落已过万年、风俗失去活跃必要性，但认为这并不消除推断的合理性，否则等于用化石空白期否定演化论，是双标。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013"],
     "summary": "给出理由：收容妇女儿童是最重要的战争收获之一；部落势力范围取决于生育速度，瓶颈在雌性；幼童是已付过生育代价的战士半成品，可收养归化；育龄妇女遂成为事关生死的战略资源，同时招来攻击。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"],
     "summary": "用A/B部落对比说明现实风险：拥有更多育龄女性的B部落更可能被攻击，攻击者宁可选择彩头较小的A部落。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021"],
     "summary": "提出选择压力：偏向能建立贞操观念的部落；若战败时妇女自杀而不被归化，生育资源就从“现金”变成“记名债券”，杀死我也一无所获，攻击者于是掉头去瞄准A部落。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023"],
     "summary": "结论：通过贞操观的构建，部落无意间获得安全得多的生存环境，提高幸存几率；这就是贞操观背后真正的动因。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025"],
     "summary": "限定：天降神谕、三言二拍警世通言只是无意间实现该结果的具体路径，不是观念生根发芽的真实保障；不是圣人设教构建了贞操观念，而是不讲贞操的部落早期被群起攻之灭亡逼出了它。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033"],
     "summary": "转向现代：连续提出女性是否只是国家/民族的财产、是否应有此自觉、不自觉是否应被惩戒直到接受或被消灭、为女性打上此烙印是否客观上有利于本社群总体安全等前提问题，并追问基于何种授权程序才有权柄规定一半社会成员的命运。", "role": "open_question"},
    {"unit_id": "U009", "paragraph_refs": ["P034"],
     "summary": "声明：作者没有谈论任何“支持”或“反对”，只是指出讨论该问题需要解决的前提问题与需要了解的信息。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "在最原始的部落状态，战胜部落不会虐待战败方的妇女、儿童。",
     "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "不能用已经构造完成（有文字、墓葬、祭祀痕迹）的考古遗址来论证贞节观构造之前的阶段不存在，这不构成反驳。",
     "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified",
     "statement": "现存原始部落已过万年、风俗失去继续活跃的必要性，但这并不消除该推断过程的合理性；否则等于认可用化石空白期否定演化论，是双标。",
     "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "收容妇女儿童是重要的战争收获：部落势力范围直接取决于生育速度，而生育速度的瓶颈在雌性。",
     "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_reported", "attribution": "author", "modality": "asserted",
     "statement": "幼童可视为现成的战士半成品，可收养和归化，相当于已付过生育代价的成功产品。",
     "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "育龄妇女成为事关部落未来生死的战略资源，因而同时成为招来攻击的重大诱因。",
     "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical",
     "statement": "这造成偏向于能成功建立贞操观念的部落的选择压力；若战败时妇女选择自杀而非被归化，生育资源便由“现金”变为“记名债券”，使攻击者一无所得。",
     "evidence": ["E008", "E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "通过贞操观的构建，部落无意间获得安全得多的生存环境，相对而言大大提高幸存几率；这是贞操观背后真正的动因。",
     "evidence": ["E010", "E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "不是天降神谕或圣人设教构建了贞操观念，而是不讲贞操的部落早期被视为肥肉群起而攻之灭亡，逼出了贞操观念。",
     "evidence": ["E012"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned",
     "statement": "讨论现代贞操观念前必须回答一系列前提问题：女性是否只是国家/民族的财产、是否应有此自觉、不自觉是否应被惩戒、此烙印是否客观上有利于本社群总体安全。",
     "evidence": ["E013", "E014"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned",
     "statement": "还须追问是否有资格和权柄，以及基于何种授权程序才有权对一半社会成员的命运作政策规定。",
     "evidence": ["E015"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "作者声明自己没有谈论任何“支持”或“反对”，只是指出讨论该问题需要解决的前提问题与需要了解的信息。",
     "evidence": ["E016"]}
   ],
   "argument_steps": [
    "提出推断：最原始部落状态不虐待战败方妇女儿童。",
    "预置防御：贞节观在有文字、墓葬、祭祀时已构造完成，故不能用此类遗址反驳；史前时代漫长且社会伦理模糊。",
    "举现存遗风（易洛魁人的默哀战争）作为旁证。",
    "让步：现存部落已过万年、风俗失去必要性；但主张推断仍合理，并以演化论与化石空白期作类比反将一军。",
    "进入解释：生育速度决定部落势力范围，瓶颈在雌性；幼童是可归化的战士半成品。",
    "推出育龄妇女是战略资源也是攻击诱因。",
    "以A/B部落对比说明“肥肉”招攻的现实风险。",
    "引入选择压力：能被归化的资源必然招攻，故需让其不可被归化。",
    "以“记名债券”说明妇女自杀威胁如何改变攻击者的收益计算。",
    "结论：贞操观是无意间获得的安全策略，提高部落幸存几率。",
    "限定：神谕、警世通言只是路径而非保障；真正的动力是灭亡压力。",
    "转向现代，列出一串前提反问，并追问授权程序。",
    "声明中立：不表支持或反对，只指出前提问题。"
   ],
   "concept_usage": [
    {"term": "贞操观", "meaning": "本文指使本部落妇女在战败时不被归化（如自杀）的观念机制，作者称其为部落无意间获得的安全策略。", "evidence": "P023", "ambiguity": "作者把现代意义上的贞操观与史前“不被归化”行为贯通，其等同关系未加论证。"},
    {"term": "记名债券", "meaning": "比喻附条件、不能随意占有的生育资源：杀死持有者则一无所获。", "evidence": "P019", "ambiguity": "经济比喻，非严格术语。"},
    {"term": "选择压力", "meaning": "使能建立贞操观念的部落更可能幸存的筛选机制。", "evidence": "P017", "ambiguity": "作者未说明该机制的作用单位是个体还是群体。"},
    {"term": "国家/民族的财产", "meaning": "作者设问中用于描述女性可能被设定的地位，属待回答的前提问题而非作者主张。", "evidence": "P027", "ambiguity": "作者明确表示未对之表支持或反对。"}
   ],
   "examples_and_targets": [
    "易洛魁人的默哀战争（作者举的现存原始部落遗风，P004）。",
    "新石器时代遗址的考古发现（作者预设的反驳材料并加以排除，P002—P003）。",
    "反演化论者用化石空白期批评演化论（作者用作类比反驳，P007）。",
    "A部落1500名育龄女性与B部落3000名育龄女性的对比，以及CDEFG等部落的选择（作者构造的思想实验，P011/P014）。",
    "天降神谕、三言二拍警世通言（作者举为“具体路径”而非真实保障，P024）。",
    "“如果我们部落战败，我们的妇女将会自杀，而不是任你们归化”（作者拟想的部落宣告，P018）。"
   ],
   "conditions": [
    "推断的适用范围被限定为“人类尚未建立起明晰的社会伦理、甚至连‘父母’‘领导者’这些概念都还模模糊糊”的史前阶段（P003）。",
    "作者承认现存原始部落已过万年、基本完成所在封闭领域的最终霸权，风俗已无活跃的必要性（P005，让步条件）。",
    "论证依赖“生育速度瓶颈在雌性”这一前提（P010）。",
    "贞操观的安全收益以部落为分析单位，且相对于没有构造出该观念的部落而言（P022）。",
    "现代部分的讨论被作者加上前提：先回答那一串问题，且讨论者需有资格与权柄（P031—P033）。"
   ],
   "rhetoric_and_tone": "论证文体带散文气：先以括号插入长段“我先把话说好”预防反驳，用“否则你不是双标吗？”反问；以“这个问题直击灵魂”“肥肉”“假彩头”“记名债券”等比喻推进；结尾连用六个反问后声明不持立场，语气克制而带挑衅性的中立。",
   "unresolved_questions": [
    "“易洛魁人的默哀战争”的具体内容、民族学出处本文未给出，需外部核查。",
    "“育龄女性3000对1500即拥有远期战略优势”“生育速度瓶颈在雌性”等人口学断言本文未给数据来源，需外部核查。",
    "作者用演化生物学类比（化石空白期）支持史前推断，其类比是否成立本文未加论证。",
    "“天降神谕、三言二拍警世通言”与史前贞操观之间的时代跨度未被处理。",
    "对现代社会的六个反问作者未给出自己的答案，也未说明自己主张何种制度安排。",
    "作者声明不表支持或反对，但其“真正的动因”“逼出了贞操观念”等表述被记为作者主张，归属已按原文区分。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "在最原始的部落状态，战胜部落是不会虐待战败方的妇女、儿童的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "不要拿已经构造完成的考古遗址来论证这个阶段的不存在，因为这不构成反驳。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "早已经没有让这个风俗继续活跃、存在的必要性了。", "relation": "qualifies"},
    {"key": "E004", "paragraph_id": "P007", "quote": "否则，你就应该同意反演化论者指着任何一个化石空白期批评演化论是胡说八道。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P010", "quote": "部落的势力范围，直接取决于部落的生育速度。而生育速度的瓶颈一向不在雄性上，而在于雌性上。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P012", "quote": "至于幼童，则可以视为现成的战士半成品，完全可以收养和归化。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P013", "quote": "育龄妇女成了一种事关部落未来生死的战略资源，于是同时是一种会招来攻击的重大诱因。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P017", "quote": "这里造成了一种很大的选择压力，偏向于能成功在自己部落里建立贞操观念的部落。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P019", "quote": "而是成了“记名债券”。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P022", "quote": "通过贞操观的构建，部落无意间获得了安全得多的生存环境", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P023", "quote": "这就是贞操观背后真正的动因。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P025", "quote": "不是天降神谕、或者圣人设教构建了贞操观念", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P027", "quote": "女性是否只是国家/民族的财产？", "relation": "context"},
    {"key": "E014", "paragraph_id": "P030", "quote": "为女性打上这个思想烙印，是否客观上总体有利于本社群的总体安全？", "relation": "context"},
    {"key": "E015", "paragraph_id": "P033", "quote": "基于何种授权程序，你会觉得自己有权柄就一半社会成员的命运做出政策上的规定？", "relation": "context"},
    {"key": "E016", "paragraph_id": "P034", "quote": "我没有谈论任何“支持”或者“反对”", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会生物学", "性别与婚姻制度", "史前史与人类学", "战争与部落社会", "观念起源"],
   "issue_candidates": ["战败方妇女儿童的处置", "生育资源与部落竞争", "贞操观的起源与功能", "女性是否作为国家/民族财产", "讨论该问题的授权前提"],
   "text_function_candidates": ["答疑", "论证", "历史解释", "反问式追问", "方法辩护"],
   "object_candidates": ["史前部落", "易洛魁人", "A/B/CDEFG部落（思想实验）", "现代国家/民族", "新石器时代遗址"],
   "working_keywords": ["贞操观", "贞节观", "战争收获", "生育速度", "育龄女性", "战略资源", "记名债券", "选择压力", "默哀战争", "授权程序"]
  },
  "notes": "平台为知乎问答；提问中的“有必要反抗到底还是选择投降活着”属提问者设问，作者未直接回答，仅在结尾以反问列出前提问题，已按 open_question/context 处理。作者在 P034 明确声明不表支持或反对，故其解释性主张按原文记为作者侧因果解释，未将任何规范立场归给作者。brief 在渲染包中被截断（结尾为“在人类群居和人类有”），未用作证据。"
 },

 "e72842ba": {
  "analysis": {
   "question_context": "提问者（Q001）问如何试探出他人的底线。作者不提供试探方法，而是先判定“底线”说是对人的决策算法的一种非常危险的简化——它把人当成弹簧、高压锅、温度计一类刺激反应单纯且可逆的物品；接着论证人的界限是动态的、多维的、残留式的，因此无法被有效测度，最后把问题反转为：若完全不用“底线”说指导相处，替代方案是什么（文末标“未完，待续”）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"],
     "summary": "指出“底线”说是危险的简化：它把人当作弹簧、高压锅、温度计这类刺激—反应单纯且可逆的物品，并把关键放在不越过屈服极限。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010"],
     "summary": "判定这是误解：人不是这种反应方式；但“把自己当成高压锅来体察”已渗入文化底层——压力、发泄、快爆炸一类说法即把自己视为蒸汽机，是第一次工业革命在文化上的痕迹。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018"],
     "summary": "说明“蒸汽机病”的传染机制：发泄后被认定“好多了”，下次再有压力便被解释为“积累太快”而非发泄无效；这类“医疗理论”是心理上的顺势疗法、扎小人式感应巫术，可有效验但非理想解决方案，因为人毕竟不是蒸汽机。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025"],
     "summary": "把“底线”改述为“关系不可逆阈限”后指出第一点：界限是动态的，受主体处境、心态、生理状态影响，波动幅度大到探索“相对稳定波动范围”也无意义；以相变温度在120K—360K间游走的特殊液体作比，并指出按旧“底线”行事会再次遭遇勃然大怒。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P026", "P027", "P028", "P029"],
     "summary": "第二，界限是多维的：不是单一指标，而像罩住十几条乱窜大鱼的一张网，参数交联、形状变幻，预测其边界的数学复杂度远超三体问题，不可归约为Z值标定的水平面。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035"],
     "summary": "第三，反应不是瞬时而是残留式的：实际强度应视为瞬间强度对过去一段时间的积分，且积分范围动态；上周、去年的事都有影响，影响因子还受事件性质影响，增大还是降低“底线网”弹性则难说。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P036"],
     "summary": "图景可继续画：网的形状基于各人生理基础各不相同，导致能网到的鱼不同、被网住的鱼对不同领域产生不同适应行为，网还会因撞击二次变形。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P037", "P038", "P039"],
     "summary": "强调这一比蒸汽机模型复杂几十个维度的模型仍是对人的决策方式的危险高度简化；并批评九型人格、星座、血型、奇门八卦只是靠增加参数来较劲。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P040", "P041", "P042"],
     "summary": "结论：底线是神秘事物，目前与可见将来都没有有效测度手段；并以可控核聚变会先被解决（因为简单得多）作夸张对比，说等核聚变实现再来检讨此问题。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P043", "P044"],
     "summary": "把问题反转：真正要问的是不用底线说指导相处时的替代方案；文末标“（未完，待续）”。", "role": "open_question"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "“底线”说是对人的决策算法的一种非常危险的简化，它把人视为弹簧、高压锅、温度计一类刺激反应单纯且可逆的物品。",
     "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "这是一种危险的误解：除了把自己当成高压锅来自我体察的人，人类其实不是这样一种行为方式。",
     "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "把自我模拟成高压锅来理解的行为已不知不觉渗入人类文化的底层，“压力”“发泄”等说法即把自己视为蒸汽机，是第一次工业革命在文化上留下的痕迹。",
     "evidence": ["E004", "E005"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified",
     "statement": "发泄式“医疗理论”只是一种心理上的顺势疗法、扎小人式感应巫术；它确实可以有相当程度的实效乃至支撑信仰，但并非人自我认知的理想解决方案。",
     "evidence": ["E006", "E007"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "把“底线”改述为“关系不可逆阈限”后可见：这个界限是动态的，其幅度波动之大使探索“相对稳定波动范围”也没有意义。",
     "evidence": ["E008", "E009"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "这个界限是多维的：不是单一指标，而类似十几个参数交联的“立体防线”，预测其具体边界的数学复杂度远超过三体问题。",
     "evidence": ["E010"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted",
     "statement": "它对刺激信号的反应不是瞬时的而是残留式的：实际强度应被视为瞬间强度对过去一段时间的积分，且积分范围是动态的。",
     "evidence": ["E011"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted",
     "statement": "即使这个比蒸汽机模型复杂几十个维度的模型，仍然是对人的决策方式的一种近乎危险的高度简化。",
     "evidence": ["E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated",
     "statement": "“底线”是一个神秘事物，不但目前，而且在可见的将来也没有有效的手段能测度它。",
     "evidence": ["E013"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned",
     "statement": "真正需要问自己的问题是：如果完全不用“底线”说来指导与他人的相处，替代方案是什么。",
     "evidence": ["E014"]}
   ],
   "argument_steps": [
    "先给判断：底线说是危险的简化，其模型来自弹簧、高压锅、温度计这类反应可逆的物品。",
    "指出该模型的策略含义：关键只在于不越过屈服极限，故人们才高度在意“试探底线”的方法。",
    "反驳：人类不是这种反应方式；但“把自己当高压锅”的说法已渗入文化底层。",
    "追溯来源：压力、发泄、快爆炸等表述把人视为蒸汽机，是第一次工业革命的文化痕迹。",
    "推演“蒸汽机病”的自我实现：发泄后自认好转，下次便归因于压力积累太快，故不构成反驳。",
    "类比定性：这套医疗理论相当于顺势疗法、感应巫术，有效验但不理想。",
    "转换表述为“关系不可逆阈限”，逐条给出三点困难：动态、多维、残留式。",
    "以特殊液体相变温度、乱窜大鱼之网、信号积分三个比喻分别支撑三点。",
    "补充网的形状因人而异、会二次变形，并把星座血型等归为增加参数的努力。",
    "结论：底线不可测度，并以其比可控核聚变更难作夸张收束。",
    "把问题反转成对替代方案的追问，并标明未完待续。"
   ],
   "concept_usage": [
    {"term": "底线", "meaning": "本文中被作者改述为“关系不可逆阈限”：一旦越过便不可回复的关系界限。", "evidence": "P019", "ambiguity": "作者认为该词原义预设了可逆的机械模型，故以改述方式重述，改述本身即作者的重新界定。"},
    {"term": "蒸汽机病/蒸汽机自觉", "meaning": "把自我与他人下意识地理解为一台蒸汽机（压力累积—发泄—恢复）的认知习惯。", "evidence": "P009", "ambiguity": "作者自造表述，未给出诊断标准。"},
    {"term": "顺势疗法、扎小人", "meaning": "作者用来类比发泄式心理调节的修辞：有效验但原理不成立。", "evidence": "P015", "ambiguity": "类比性贬称，作者未论证两者机制等同。"},
    {"term": "关系不可逆阈限", "meaning": "作者为“底线”给出的替代表述，强调越界后不可回复。", "evidence": "P019", "ambiguity": "仅提出，未给出定义或测量方式。"}
   ],
   "examples_and_targets": [
    "弹簧、高压锅、温度计（作者用于刻画“底线”说所预设的物品模型，P002）。",
    "“我最近压力很大”“我需要发泄一下”“I need to blow off some steam”（作者引为蒸汽机式自我描述的日常语例，P008）。",
    "第一次工业革命与蒸汽文明（作者提出的文化来源解释，P009）。",
    "跳大神、出马仙（作者用作“有效验但非正解”的类比，P015—P016）。",
    "凝固相变在120K到360K之间游走的特殊液体（作者构造的思想实验，P023）。",
    "“罩住十几条四面乱窜的大鱼的一张大网”（作者模型比喻，P027）。",
    "九型人格、星座、血型、奇门八卦（作者批评对象，P038）。",
    "可控核聚变（作者用作夸张比较对象，P041）。"
   ],
   "conditions": [
    "作者对“底线”说的批评针对的是把它当作决策算法模型来使用的人（P001、P004）。",
    "三点反驳都限定在把底线改述为“关系不可逆阈限”之后（P019，改述条件）。",
    "界限的动态性被限定为受主体处境、心态、生理状态影响（P021）。",
    "残留效应以“即使加以简化”为前提，且积分范围本身是动态的（P032）。",
    "对网形差异的补充以每个人的生理基础不同为条件（P036）。",
    "“可控核聚变先被解决”为夸张修辞，非预测性承诺（P041）。",
    "全文以“（未完，待续）”收尾，作者明示论述未完成。"
   ],
   "rhetoric_and_tone": "科普—驳论混合文体，第二人称“你”贯穿；用“害死人”“近乎于作死”“这个问题直击灵魂”式重话点明风险，用I need to blow off some steam等引语增强代入；大量比喻（弹簧、蒸汽机、特殊液体、大鱼之网、斑马线）；以“啥时候可控核聚变实现了，再来检讨”作调侃式夸张收束。",
   "unresolved_questions": [
    "作者未给出“底线”说的替代方案，文末明示“（未完，待续）”，本篇论述不完整。",
    "“第一次工业革命给人类文化留下痕迹”“蒸汽机病已被传染”等属作者的文化史断言，本文未提供史料或实证依据，需外部核查。",
    "“跳大神、出马仙也能有一定效果”为作者的类比性断言，本文未给出病例或研究，需外部核查。",
    "“数学复杂度远超过三体问题”是作者的比较判断，本文未给出形式化依据，需外部核查。",
    "“可控核聚变一定会在这个问题可被企及之前被解决”为预言式修辞，作者未给出理由。",
    "P041—P042 用词为绝对断言（“一定会”“没有有效的手段”），其适用范围（对谁、在何种关系下）本文未限定。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "“底线”说是一个对人的决策算法的的简化模型，而且是一个非常危险的简化。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "这是在将人类视为一种简单的常见物品，譬如弹簧，或者高压锅，或者温度计。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P006", "quote": "因为除了把自己当成高压锅来自我体察的人，人类其实不是这样一种行为方式。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P007", "quote": "这种将自我模拟成高压锅来理解的行为已经不知不觉渗入了人类文化的底层。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "这是第一次工业革命生产力的陡然飞跃给人类文化留下的痕迹。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P015", "quote": "这种“医疗理论”，只是一种心理上的“顺势疗法”，一种“扎小人”式的感应巫术。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P017", "quote": "“蒸汽机自觉”也并非人自我认知的理想解决方案。", "relation": "qualifies"},
    {"key": "E008", "paragraph_id": "P020", "quote": "首先，这个界限是动态的。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P022", "quote": "会使得退而求其次去探索“其相对稳定波动范围”都变得没有意义。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P027", "quote": "其数学复杂度远超过三体问题。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P032", "quote": "也应该被视为瞬间强度对过去一段时间的积分——而且这个积分范围还是动态的。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P037", "quote": "仍然是对人的决策方式的一种近乎危险的高度简化。", "relation": "qualifies"},
    {"key": "E013", "paragraph_id": "P040", "quote": "“底线”是一个神秘事物，不但目前，而且在可见的将来也没有有效的手段能测度它。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P043", "quote": "“如果我完全不用底线说来指导我与他人的相处，我的替代方案是什么？”", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学与认知", "人际交往", "科学隐喻与文化批评"],
   "issue_candidates": ["试探底线的可行性", "机械模型套用于人的谬误", "情绪发泄的有效性", "界限的动态性、多维性与残留性", "替代方案之问"],
   "text_function_candidates": ["答疑", "反驳", "解释", "类比说理", "未完成连载"],
   "object_candidates": ["弹簧/高压锅/温度计（模型物）", "蒸汽机与第一次工业革命", "出马仙与跳大神", "九型人格/星座/血型/奇门八卦", "可控核聚变"],
   "working_keywords": ["底线", "关系不可逆阈限", "简化模型", "蒸汽机病", "顺势疗法", "感应巫术", "动态", "多维", "残留式", "三体问题"]
  },
  "notes": "平台为知乎问答（提问属提问者 Q001，作者未提供试探方法而作驳论）。本篇以“（未完，待续）”结尾，属未完成连载，已在 unresolved_questions 登记；作者对“底线”的批评依赖其改述“关系不可逆阈限”，改述为作者自设，未把改述后的模型当作原词定义之外的既成事实。"
 },
 "4c5a7c53": {
  "analysis": {
   "question_context": "提问者（Q001）问清华学姐事件持续发酵、其身份信息与电话号码被全部挖出，万一此女自杀事情会如何。作者未叙述事件走向，先预判参与施暴者中很大一批会觉得“替天行道成功”而痛快，再由“人类的幼崽不是天使，而是天生的恶魔”评论中国父母的管教，继以连续反问质询在此问题下乐见他人死亡者有无定罪、定罚、施刑的资格，最后给出善恶的实践界限并否定鼓动和助长仇恨。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "预判：参与施暴者中很大一批会觉得替天行道成功、觉得很痛快。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "人性前提：幼崽不是天使而是天生的恶魔，父母只有几年时间窗口抑制其攻击性与贪婪；遗憾中国父母很多做得不好。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "以本问题下大量答案中乐见他人死亡和毁灭的恨意，作为父母管教不好的直观表现。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "让步承认当事人有错甚至有罪，再反问是否罪至于死，并要求读者自问。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "三重“退一步”反问：判断有罪、定罚、施罚是否该由你来下；是否要背书公众审判与舆论处决体制。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"], "summary": "反问对方是否受得起同样审判；假设被拉上审判台并预测众人丢陶片看你喝毒药；质疑问审判结果与事实的关联。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P018"], "summary": "结论：这是在挖掘自己的坟墓。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P019"], "summary": "断言酷厉在任何文化、任何社会都不被视为正面品质或人格健康表现。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P020", "P021"], "summary": "提出善恶的实践界限：减轻恨为善、加重恨为恶；无论被高举为正义或被诬为软弱均成立。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P022"], "summary": "理由：世界上没有任何一种仇恨是正义的，否则迟早会找到丢掉一切善意的合理理由。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P023", "P024"], "summary": "警告：以为那种理由只适用于极端情况的人，迟早会发现一切情况都是那种情况。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P025", "P026", "P027"], "summary": "收束：可以反对甚至不惜生命阻止某种行为，但鼓动和助长仇恨没有正义、至少没有健康可言。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "参与施暴的人们中，很大一批会觉得“替天行道”成功，觉得很痛快。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类的幼崽不是天使而是天生的恶魔；父母只有几年的时间窗口去抑制其本能的攻击性和无理性的贪婪，使其子女能在社会中作为功能有效的一分子生存。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的父母们很多在教育上做得不好，直观表现是本问题下大量答案中赤裸裸的乐见他人死亡和毁灭的恨意。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "即算当事人有错甚至就算有罪，作者反问是否罪至于死，并要求读者自问。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以三重“退一步”反问“你”是否有资格判断有罪、定其该受之罚、实施该罚，并质疑是否要背书公众审判与舆论处决体制、自己是否愿意接受这种“司法体制”。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "假设明天有人把“你”拉到审判台上，会有很多人迫不及待丢下陶片想看其喝毒药。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质疑“公众审判”的结果与当事人到底做了什么是否有绝对关联，想看你死的人是否真的在乎你是否罪至于死。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为公众审判背书是在挖掘自己的坟墓。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "酷厉在任何文化里都不会被认定为正面的品质，在任何社会里都不会被视为人格健康的表现。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "善恶有一种最简单的实践界限：看到一种恨，想办法减轻这种恨总是好的，而加重这种恨总是恶的。", "evidence": ["E012"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论这种恨被多少人高举为合理和正义，无论消解仇恨被诬为何种软弱和“背叛”，上述界限都成立。", "evidence": ["E013"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上没有任何一种仇恨是正义的；若不抱定这种彻底的决心，迟早会找到一种丢掉一切善意的合理理由。", "evidence": ["E014"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "以为那种丢掉善意的理由只适用于某种极端情况、无碍大局的人，迟早会发现一切情况都是那种情况。", "evidence": ["E015"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可以反对、甚至不惜生命去阻止某种反对的行为，但鼓动和助长仇恨永远没有任何正义可言，至少没有健康可言。", "evidence": ["E016", "E017"]}
   ],
   "argument_steps": [
    "预判施暴者会觉得“替天行道成功”而痛快（P002）。",
    "前提：幼崽是天生的恶魔，父母只有几年窗口抑制其攻击性与贪婪（P003）。",
    "评中国父母多做得不好，证据是本问题答案中的恨意（P004-P005）。",
    "让步承认当事人可能有错甚至有罪，再反问是否罪至于死（P006-P010）。",
    "三重“退一步”追问定罪、定罚、施刑资格与是否背书公众审判（P011-P014）。",
    "假设“你”被审判，预测众人丢陶片看你喝毒药，并质疑问审判结果与事实的关联（P015-P017）。",
    "结论：这是在挖掘自己的坟墓（P018）。",
    "另作一般判断：酷厉不是正面品质、不是人格健康表现（P019）。",
    "提出善恶的实践界限：减轻恨为善、加重恨为恶（P020）。",
    "限定：无论被高举为正义或被诬为软弱，界限都成立（P021）。",
    "理由：没有仇恨是正义的，否则会找到丢掉善意的理由（P022）。",
    "警告：以为只适用极端情况者迟早发现一切情况都是那种情况（P023-P024）。",
    "收束：可以反对甚至不惜生命阻止，但鼓动仇恨无正义、无健康（P025-P027）。"
   ],
   "concept_usage": [
    {"term": "替天行道", "meaning": "作者转述施暴者自我正当化的说法（加引号标示为他人用语），非作者自己的评价", "evidence": "P002", "ambiguity": "引号表明为转述"},
    {"term": "酷厉", "meaning": "以严酷手段对待他人的品质；作者断言其在任何文化中都不被认定为正面品质", "evidence": "P019", "ambiguity": "文中未给定义"},
    {"term": "公众审判、舆论处决体制", "meaning": "由公众舆论代替司法对当事人定罪并施罚的机制；作者用反问质疑而非直接定义", "evidence": "P014、P017", "ambiguity": "范围与运作方式未说明"},
    {"term": "恨、仇恨", "meaning": "乐见他人死亡和毁灭的情绪以及被鼓动助长的仇恨；被作者作为善恶实践界限的判据", "evidence": "P005、P020、P022", "ambiguity": "情绪与行为的边界未区分"},
    {"term": "挖掘自己的坟墓", "meaning": "隐喻：为公众审判体制背书最终危及自身", "evidence": "P018", "ambiguity": "推论未展开"},
    {"term": "丢下陶片", "meaning": "文中描述围观者对被审判者施以死亡的意象", "evidence": "P016", "ambiguity": "典故出处文中未说明，需外部核查"}
   ],
   "examples_and_targets": [
    "清华学姐事件及身份信息、电话号码被挖出的情境：来自提问者（Q001），作者未叙述事件细节，只指向“这个问题下大量答案”。",
    "参与施暴的人们：作者批评与预判的对象（P002）。",
    "中国的父母们：作者评论其管教做得不好的对象（P004）。",
    "本问题下作答者的恨意：作者用作“管教不好”的直观表现与证据（P005）。",
    "“丢下陶片想看你喝毒药”：作者使用的典故意象（P016），出处未说明。",
    "公众审判、舆论处决体制：被作者以反问质疑的对象（P014、P017）。"
   ],
   "conditions": [
    "P006“即算当事人有错，甚至就算是有罪吧”为让步条件。",
    "P016“如果明天有人把你拉到这审判台上”为假设条件。",
    "P019 以“在任何文化里”“在任何社会里”作全称断言，未设例外。",
    "P020 界限被限定为“最简单的实践界限”，即实践层面而非理论定义。",
    "P023-P024 指出“理由只适用于极端情况”只是一种误认，并预测其终将扩展。",
    "适用对象为参与施暴的网民（“你”）与中国父母；作者未限定时代或地域。"
   ],
   "rhetoric_and_tone": "以连续反问与“退一步”递进质询构成主体，第二人称“你”直呼读者，带训诫与警告口吻（“问问你自己”“真的吗？”）；措辞强烈（“天生的恶魔”“这是在挖掘自己的坟墓”“永远没有任何正义可言”）；结尾连用“永远没有……可言”“至少没有……”作断语。结构上先诊断（幼崽与父母）、再质询（资格与体制）、后立界限（善恶与仇恨），语气由描述转为诘问再转为伦理断言。",
   "unresolved_questions": [
    "提问设定的“万一此女自杀，事情如何”未被正面回答，正文转向对施暴者心态与公众审判的批评。",
    "P008“至于死有余庆吗？”用词与他处常见说法不同，是否为原文用词或笔误，需核对原帖。",
    "P016“丢下陶片”的典故出处文中未说明，待外部核查。",
    "事件本身（当事人行为、身份信息被公开的过程）文中未叙述，无法由本篇判断事实经过。",
    "“酷厉”“公众审判”等词文中未给定义，其边界不明。",
    "作者称“这个问题下大量答案”，但未引用任何具体答案，无法核对其描述。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "参与施暴的人们，只怕还有很大一批觉得替天行道成功，觉得很痛快呢。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "其实人类的幼崽不是天使，而是天生的恶魔。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P004", "quote": "很遗憾，这一点中国的父母们很多做得不好。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "大量答案里赤裸裸的表现出来的这种乐见他人死亡和毁灭的恨意", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "罪至于死吗？", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P013", "quote": "再退一步，她被判该受的罚，该由你来实施吗？", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P014", "quote": "你这样做，是要背书这种公众审判、舆论处决体制吗？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P016", "quote": "如果明天有人把你拉到这审判台上，你知道有多少人会迫不及待丢下陶片想看你喝毒药吗？", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P017", "quote": "你以为“公众审判”的结果真的和你到底做了什么有什么绝对的关联吗？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P018", "quote": "这是在挖掘自己的坟墓。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P019", "quote": "酷厉在任何文化里都不会是一种被认定为正面的品质", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P020", "quote": "当你看到一种恨，想办法减轻这种恨总是好的，而加重这种恨总是恶的。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P021", "quote": "无论这种恨被多少人高举为合理和正义，都是如此", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P022", "quote": "世界上没有任何一种仇恨是正义的", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P024", "quote": "迟早你会发现，一切情况都是那种情况。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P026", "quote": "但鼓动和助长仇恨永远没有任何正义可言。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P027", "quote": "至少没有健康可言。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会伦理与舆论", "网络暴力", "人性与教育"],
   "issue_candidates": ["公众审判与舆论处决", "仇恨是否有正义", "父母对子女攻击性的管教", "以酷厉对待他人"],
   "text_function_candidates": ["评论", "批评", "训诫", "论辩", "答疑"],
   "object_candidates": ["清华学姐事件", "参与施暴的网民", "中国的父母们", "公众审判/舆论处决体制"],
   "working_keywords": ["替天行道", "公众审判", "舆论处决", "酷厉", "仇恨", "实践界限", "陶片", "幼崽", "挖掘自己的坟墓"]
  },
  "notes": "答疑类回答（知乎，提问者为 Q001）。提问设定的“自杀后果”未被正面回答，正文转为对施暴者心态、父母管教与公众审判的批评；P008 用词“死有余庆”与常见说法不同，待核对原文；P016 典故出处未说明。无图片节点，正文 P001-P027 全部读完。"
 },
 "f7642b7d": {
  "analysis": {
   "question_context": "提问者（Q001）问如何快速提高象棋水平。作者不讲授具体棋艺或训练法，而是提出对抗性练习中追求卓越的第一条根本原则——不苟胜，给出“苟胜”的例子与“不苟胜”的定义，列出两项具体实践与一条进阶做法，并以三条“效果验证”收束；全文未出现棋谱、局面或具体象棋技术。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "主张：任何对抗性练习中追求卓越，第一条根本原则就是不苟胜。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "以对方出昏招时喊“落子无悔”抓紧取胜为例，称其为“苟胜”。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "定义不苟胜的本质：不利用对方的失误。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007"], "summary": "两项实践：对方苟胜也不放弃原则；无限允许对方悔棋，即使对方不许你悔棋。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "进阶做法与推论：练习时给对手一切可给的优势再争胜，才能得最强磨练，进而在真战场上有最大竞争力。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "评价：练习时寻找一切机会、空子“获胜”的只是心理不健全的可怜虫。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "三条效果验证：输了不捶胸顿足；人格健全的对手赢了不趾高气扬，否则不值在意；对方输了必定心服口服。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在任何对抗性练习之中，想要追求卓越，第一条根本的原则就是不苟胜。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "看出对方明显出了昏招就抓住机会喊“落子无悔”然后抓紧取胜，这就叫“苟胜”。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不苟胜的本质，就是不利用对方的失误。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使对方自己是苟胜之人，也不要放弃不苟胜这个原则。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要无限允许对方悔棋，即使对方不许你悔棋。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在练习对抗时给予对手一切可以给予的优势再与其争胜，才能得到最强的磨练，于是到了真的战场上才有最大的竞争力。", "evidence": ["E007", "E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那些在练习时就寻找一切机会、空子“获胜”的，只是一些心理不健全的可怜虫。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "效果验证之一：不会因为输了就捶胸顿足、咬牙切齿。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方如果人格健全，赢了你也不会趾高气扬、不可一世；这样赢了就趾高气扬的人人格不健全，对你也没什么值得在意的。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "对方如果输了，必定心服口服。", "evidence": ["E012"]}
   ],
   "argument_steps": [
    "提出总原则：对抗性练习中第一条根本原则是不苟胜（P001）。",
    "举例并命名：抓对方昏招喊“落子无悔”取胜叫“苟胜”（P002-P003）。",
    "定义不苟胜：不利用对方的失误（P004）。",
    "给出两项实践：对方苟胜也不放弃原则；无限允许对方悔棋（P005-P007）。",
    "进阶：练习时给对手一切可给的优势再争胜，才得最强磨练（P008）。",
    "推论：因此到了真的战场上才有最大的竞争力（P009）。",
    "反面评价：练习中钻空子“获胜”者心理不健全（P010）。",
    "以三条效果验证收束：自己不捶胸顿足、健全对手不趾高气扬、输者心服口服（P011-P014）。"
   ],
   "concept_usage": [
    {"term": "苟胜", "meaning": "看出对方明显出昏招后抓住机会（并借“落子无悔”的形式）抓紧取胜的行为；作者自设并命名的贬义用语", "evidence": "P002、P003", "ambiguity": "作者未说明是否涵盖正式比赛"},
    {"term": "不苟胜", "meaning": "不利用对方的失误；作者称之为对抗性练习中第一条根本原则", "evidence": "P001、P004", "ambiguity": "与胜负本身的关系未展开"},
    {"term": "对抗性练习", "meaning": "象棋一类以练习为目的的对局，与作者所说“真的战场”相对", "evidence": "P001、P008、P009", "ambiguity": "范围未限定"},
    {"term": "最强的磨练、最大的竞争力", "meaning": "作者把练习中给予对手优势与实战竞争力建立因果联系", "evidence": "P008、P009", "ambiguity": "无例证或数据支撑"},
    {"term": "人格健全、心理不健全", "meaning": "作者用于评价对手与自身胜负心态的判据", "evidence": "P010、P013", "ambiguity": "未给出判定标准"}
   ],
   "examples_and_targets": [
    "象棋：提问者（Q001）设定的场景，作者未在正文涉及具体棋局、棋谱或技术。",
    "“看出对方明显出了昏招，就立刻赶紧抓住机会喊‘落子无悔’，然后抓紧取胜”：作者举出的苟胜情形（例证）。",
    "“无限允许对方悔棋，即使对方不许你悔棋”：作者提出的实践要求（行动建议）。",
    "“真的战场”：作者推论中的类比场景（类比材料）。",
    "心理不健全的可怜虫、赢了就趾高气扬的人：作者的批评对象（P010、P013）。",
    "无历史人物、机构、数据或引文。"
   ],
   "conditions": [
    "P001 适用范围限定为“任何对抗性练习之中”。",
    "P006“即使对方自己是苟胜之人”为让步条件。",
    "P007“即使对方不许你悔棋”为让步条件。",
    "P008“在练习对抗的时候”限定场景；P009 推论指向“真的战场上”。",
    "P013 以“对方如果人格健全”为条件，并附加对人格不健全者的处置判断。",
    "P014“对方如果输了”为条件，其结论为“必定心服口服”。"
   ],
   "rhetoric_and_tone": "教导与训诫口吻，第二人称“你”贯穿；以反问开场（“你们见过那种……的吧？”）并自答命名（“这就叫‘苟胜’”）；用编号列表（1）2）3））组织实践与效果验证；对苟胜者与心理不健全者用贬抑措辞（“可怜虫”）；语气自信，属经验总结式断言。",
   "unresolved_questions": [
    "正文未给任何象棋技术或训练方法，“如何快速提高象棋水平”只在原则层面回应。",
    "“人格健全”“心理不健全”无判定标准，作者未说明由谁判定。",
    "“苟胜”是否适用于正式比赛或非棋类的对抗练习，文中未说明。",
    "P008-P009 的因果链（给予优势→最强磨练→最大竞争力）为作者断言，正文未提供例证、数据或来源。",
    "作者称三条为“效果验证”，但未说明验证方式与样本，无法判断是经验观察还是设想。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "第一条根本的原则就是不苟胜。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "看出对方明显出了昏招，就立刻赶紧抓住机会喊“落子无悔”，然后抓紧取胜的吧？", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这就叫“苟胜”。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "不苟胜的本质，就是不利用对方的失误。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "即使对方自己是苟胜之人，你也不要放弃这个原则。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "无限允许对方悔棋，即使对方不许你悔棋。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P008", "quote": "给予你的对手一切可以给予的优势，然后再与其争胜，你才能得到最强的磨练。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P009", "quote": "于是到了真的战场上，你才有最大的竞争力。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "那些在练习时就寻找一切机会、空子“获胜”的，只是一些心理不健全的可怜虫而已。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "你不会因为输了就捶胸顿足，咬牙切齿。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "对方如果人格健全，赢了你也不会趾高气扬，不可一世。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "对方如果输了，必定心服口服。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["竞技训练与学习方法", "胜负心态与伦理", "人际相处"],
   "issue_candidates": ["练习中是否应利用对手失误", "让先与磨练的关系", "悔棋的允许", "胜负心态与人格评价"],
   "text_function_candidates": ["经验总结", "答疑", "训诫"],
   "object_candidates": ["象棋", "练习对手（泛称）", "心理不健全者（泛称）"],
   "working_keywords": ["不苟胜", "苟胜", "落子无悔", "悔棋", "磨练", "竞争力", "人格健全"]
  },
  "notes": "答疑类回答（知乎，提问者为 Q001）。提问问“如何快速提高象棋水平”，作者回答的是对抗性练习的一般原则（不苟胜）而非象棋技法；正文未出现棋谱、局面或具体训练方法。无图片节点，正文 P001-P014 全部读完；provenance 为 null，无版本差异信息。"
 },
 "19a2ff4c": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者（Q001）问时间总是不够用怎么办。作者先反问“时间怎么会不够用呢”，把原因归于人的欲求很多、很大且非要不可，指出时间管理与“提升意志力”治标不治本；随即声明自己并不主张闲适生活、反而建议努力充实，再给出两条路径：改变“成功”的概念与接受式的态度，以及学会“爱好”本身并以“有积累、有结晶”为界限，最后收于焦虑的缓解。本篇含 1 个图片节点，未经核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "反问时间怎么会不够用，并把不够用归因于欲求很多、很大、非要不可，要不到就觉得自己完了。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "判断：靠学习时间技巧、时间管理、提升意志力是治标不治本。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "自我澄清：并不主张闲适生活，反而建议过得不要那么闲适、要努力和充实、时间管理技巧都用起来；但这并不解决“时间不够用”。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "出路：靠接受“随遇而安”、命运的安排、有所不得、“成固欣然败亦喜”，靠改变“成功”的概念。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008"], "summary": "理由：想不清楚什么才是成功的人生，即使二十四小时不睡觉也不够用；时间管理甚至常是抑郁之源。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010", "P011"], "summary": "价值观问题先给一个参考，称其至少不容易产生时间管理的大焦虑；P011 为指向“如何树立正确的财富观？”的链接段。", "role": "context"},
    {"unit_id": "U007", "paragraph_refs": ["P012", "P013", "P014"], "summary": "第二个秘诀：学会“爱好”本身；把事情做得有趣是极重要的技能；任何时间管理技巧都比不过喜欢做这件事。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016"], "summary": "钻研：搬砖、扫地也有可钻研处，兼顾达成目标与更优雅地达成目标；钻进去了就不会有“时间不够”的问题。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018"], "summary": "限定与陷阱：不要嗜好“虚空之事”，即能带来快感但不留下长远积累的事。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P019", "P020"], "summary": "例证与界限：写写画画留下纸即为积淀；要爱好有积累、有结晶、成果对他人也有用的事，不要爱好爽过就雁过无痕的事。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P021", "P022"], "summary": "结论：爱好会利用起闲暇时间，有结晶则常能缓解“青春虚度”的焦虑，于是不那么焦虑“时间不够用”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问“时间怎么会不够用呢”，不把时间不足当作绝对事实。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "时间不够用是因为人所想要的很多、很大，而且很紧张的非要不可，要不到就觉得自己完了、没用了、没意义了。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "靠学习使用时间的技巧、时间管理、“提升意志力”，其实是治标不治本的。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者声明并不主张人过闲适的生活；恰恰相反，建议过得不要那么闲适、要努力和充实，时间表上不要有大段空白，时间管理技巧都用起来。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者指出，即使照上述建议去做，也并不会解决“时间不够用”这个问题。", "evidence": ["E005"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "时间不够用问题，是靠接受“随遇而安”、接受命运的安排、接受有所不得、接受“成固欣然败亦喜”来解决的，是靠改变“成功”的概念来解决的。", "evidence": ["E006", "E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若不想清楚什么才是成功的人生，即使二十四小时不睡觉，时间仍然不够用；时间管理并不能解决这问题，甚至从实践上说反而常是抑郁之源。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者给出的参考价值观，不管对与不对、读者喜不喜欢，至少是不容易有时间管理的大焦虑的。", "evidence": ["E009"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把事情做得有趣起来是一项极其重要的技能；什么时间管理的技巧都比不过你喜欢做这件事。", "evidence": ["E010", "E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "好钻研则万事总有好玩的地方；钻进去了，一般都不会有什么“时间不够”的问题了。", "evidence": ["E012", "E013"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“虚空之事”指尽管能带来快感，但本身不会留下任何长远积累的事，是爱好时要避免的陷阱。", "evidence": ["E014", "E015"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要爱好那些有积累、有结晶、成果会对他人也有用的事；不要爱好那些爽过就雁过无痕的事。", "evidence": ["E016", "E017"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "爱好会自然利用起大量闲暇时间，当爱好能有结晶，也常能缓解“青春虚度”的焦虑，这样就不会那么焦虑“时间不够用”。", "evidence": ["E018", "E019"]}
   ],
   "argument_steps": [
    "以反问开篇：时间怎么会不够用（P001）。",
    "归因：欲求很多、很大、非要不可，要不到就觉得自己完了（P002）。",
    "否定常见手段的治本作用：时间技巧、时间管理、提升意志力治标不治本（P003）。",
    "自我澄清与让步：不主张闲适，反而建议充实与使用时间管理技巧（P004），但指出这并不解决该问题（P005）。",
    "给出第一条出路：接受“随遇而安”“有所不得”“成固欣然败亦喜”，改变“成功”的概念（P006-P007）。",
    "理由：不想清楚成功的人生，二十四小时不睡也不够用，时间管理反常是抑郁之源（P008）。",
    "给出价值观参考并链接“如何树立正确的财富观？”（P009-P011）。",
    "给出第二个秘诀：学会“爱好”本身，把事情做得有趣（P012-P014）。",
    "展开钻研：搬砖扫地皆有可钻研处，钻进去就没有“时间不够”的问题（P015-P016）。",
    "设限定与陷阱：不要嗜好不留下长远积累的“虚空之事”（P017-P018）。",
    "以写写画画留下纸为例，划出“有积累、有结晶、对他人有用”的界限（P019-P020）。",
    "结论：爱好的结晶缓解“青春虚度”的焦虑，于是不那么焦虑时间不够用（P021-P022）。"
   ],
   "concept_usage": [
    {"term": "虚空之事", "meaning": "尽管能带来快感，但本身不会留下任何长远积累的事；作者把它设为爱好的陷阱", "evidence": "P017、P018", "ambiguity": "判断“长远积累”的标准未给出"},
    {"term": "积淀、结晶", "meaning": "爱好留下的成果（如写写画画留下的一张纸），并强调成果对他人也有用", "evidence": "P019、P021", "ambiguity": "对“有用”的判定主体未说明"},
    {"term": "成功、成功的人生", "meaning": "作者主张要改变“成功”的概念并想清楚什么才是成功的人生，但本篇未给出其正面定义，仅以链接段指向财富观", "evidence": "P007、P008、P011", "ambiguity": "定义缺失"},
    {"term": "随遇而安、命运的安排、有所不得、成固欣然败亦喜", "meaning": "作者提出的接受式解决路径的用语", "evidence": "P006", "ambiguity": "各组用语之间的关系未说明"},
    {"term": "时间管理", "meaning": "被作者视为可用但治标不治本的技巧；在本情况下甚至常是抑郁之源", "evidence": "P003、P004、P008", "ambiguity": "“治标不治本”与“都用起来”并列，界限未详述"},
    {"term": "爱好", "meaning": "把事情做得有趣的能力与喜爱本身；须以有积累、有结晶为界限", "evidence": "P012、P013、P014、P019", "ambiguity": "与“虚空之事”的界线依积累判定"},
    {"term": "意志力", "meaning": "作者在引号中引述“提升意志力”这一常见主张，并把它与时间技巧并列判为治标不治本", "evidence": "P003", "ambiguity": "引号标示为转述他人说法"}
   ],
   "examples_and_targets": [
    "“搬砖、扫地也有可钻研处”：作者举例说明万事可钻研（例证）。",
    "“你喜欢写写画画，那么爽过一番之后总留下了一张纸”：作者举例界定“不为虚空”（例证）。",
    "学习时间管理技巧、“提升意志力”：被作者降格为治标不治本的对象（批评对象）。",
    "P011“如何树立正确的财富观？”：正文中的链接段，lexical 未覆盖该片段；作者以此作为“价值观问题”的参考。",
    "无人物、机构、历史叙述或数据。"
   ],
   "conditions": [
    "P004“不过不要误会”为明确的立场澄清，否定“主张闲适生活”的读法。",
    "P008“这个问题不想清楚，即使二十四小时不睡觉……”为让步/假设条件。",
    "P010“不管对与不对，你喜不喜欢”为作者对参考价值观的自我限定。",
    "P016“一般都不会”为限定语气，未作绝对断言。",
    "P017“但是要注意陷阱”为对“爱好”的限定条件；P018 给出“虚空之事”的界定标准。",
    "P003 的否定针对的是把时间技巧作为解决方案的用法，而非技巧本身（P004 仍建议使用技巧）。"
   ],
   "rhetoric_and_tone": "以反问开篇，随后自问自答式推进；用“不过不要误会”作自我澄清与让步，避免被读成主张闲适；以“秘诀”“注意陷阱”式提示组织建议，口吻为劝解与指导并带轻微训诫（“这个问题你要想清楚”）；用“甚至……反而常是抑郁之源”“什么时间管理的技巧都比不过……”作强调。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001，src //asset.sooon.ai/p/2020-11/23/59ec10801497a38f4d6b6fba2f243592.jpg），图片内容未经核验，需人工/多模态复核；该图在正文中的位置与作用不明。",
    "P011“如何树立正确的财富观？”为链接段，lexical 未覆盖该片段；其指向内容与作者所说“价值观参考”的具体内容未在本篇正文展开。",
    "作者称“第二个秘诀”，但“第一个秘诀”未明确标号，需核对是否指 P006-P010 的价值观部分。",
    "作者主张改变“成功”的概念，但除链接外未在本篇给出其正面定义。",
    "P021 中引号使用（“青春虚度“）与常规不一致，疑为原文标点，需核对原帖。",
    "provenance 为 null，无版本差异信息；提问者的具体处境（职业、年龄等）文中未说明。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "其实，时间怎么会不够用呢？", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "时间不够用，是因为人所想要的很多、很大，而且很紧张的非要不可，要不到就觉得自己完了，没用了，没意义了。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这个靠学习很多使用时间的技巧、学习时间管理、“提升意志力”，其实是治标不治本的。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "我并不主张人过闲适的生活，恰恰相反，我倒是建议各位过得不要那么闲适，要努力和充实。", "relation": "qualifies"},
    {"key": "E005", "paragraph_id": "P005", "quote": "这并不会解决“时间不够用”这个问题。", "relation": "qualifies"},
    {"key": "E006", "paragraph_id": "P006", "quote": "是靠接受“随遇而安”，接受命运的安排，接受有所不得，接受“成固欣然败亦喜”来解决的。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "是靠改变“成功”的概念来解决的。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "即使二十四小时不睡觉，你的时间仍然是不够用的。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P010", "quote": "至少是不容易有时间管理的大焦虑的。", "relation": "qualifies"},
    {"key": "E010", "paragraph_id": "P013", "quote": "把事情做得有趣起来，是一项极其重要的技能。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P014", "quote": "什么时间管理的技巧都比不过你喜欢做这件事。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P015", "quote": "好钻研，则万事总有好玩的地方。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P016", "quote": "钻进去了，一般都不会有什么“时间不够”的问题了。", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P017", "quote": "但是要注意陷阱——不要嗜好虚空之事。", "relation": "qualifies"},
    {"key": "E015", "paragraph_id": "P018", "quote": "就是尽管能带来快感，但本身不会留下任何长远积累的事。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P019", "quote": "要爱好那些有积累、有结晶、成果会对他人也有用的事。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P020", "quote": "不要爱好那些爽过就雁过无痕", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P021", "quote": "爱好会自然利用起你大量的闲暇时间", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P022", "quote": "这样你就不会那么焦虑“时间不够用”了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["时间管理与自我调节", "价值观与人生目标", "情绪与焦虑"],
   "issue_candidates": ["时间不够用的归因", "时间管理技巧的限度", "成功概念的改变", "爱好的积累与虚空之事的界限"],
   "text_function_candidates": ["答疑", "劝解", "经验总结", "训诫"],
   "object_candidates": ["提问者（泛称“你”）", "时间管理技巧与“提升意志力”主张", "爱好/虚空之事", "财富观（链接指向）"],
   "working_keywords": ["时间不够用", "时间管理", "随遇而安", "成固欣然败亦喜", "成功", "爱好", "虚空之事", "积淀", "结晶", "青春虚度"]
  },
  "notes": "本篇含 1 个图片节点（IMG001，src //asset.sooon.ai/p/2020-11/23/59ec10801497a38f4d6b6fba2f243592.jpg），图片内容未经核验，需图像核验；已读部分为正文文本（P001-P022）。status=needs_reread、image_checked=False 因此篇有图。另：P011“如何树立正确的财富观？”为链接段且 lexical 未覆盖该片段；P021 引号使用异常，均待核对原帖。"
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
