# -*- coding: utf-8 -*-
"""批次 r001-b0125 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0125.sessions.py            # 写 out/r001-b0125.out.jsonl
  python3 records/r001-b0125.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0125"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0125.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "f87ea15f": {
  "analysis": {
   "question_context": "知乎问题「恋人的性格互补好，还是相同好？」（Q001，属提问者）。作者没有直接比较互补与相同，而是反驳「互补论」本身：认为它不考虑人的变化。提问者的设定（互补 vs 相同二选一）不计入作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "以A/B的假设情境追问：一方变化、双方各自变化、乃至双方变化对互补的需求互相矛盾时，互补关系如何维持，B置身何处。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "判断互补论使关系从最初的「天作之合」滑向此后每天觉得对方「不再适合自己」，并称这是其逻辑的必然结果：同一逻辑促合也促分。", "role": "conclusion"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "以「跟随对方成长」不可能做到为由解释上述必然性，用擎天柱、终结者作夸张类比，指出对方的需求可能同时多样且互相矛盾。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "把互补与相似一并称作「成对耦合」的业务规则，断言它是一切升级的最大障碍，并以「随便找一个程序员都会骂」作旁证。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "移植软件工程标准作为替代方案：系统永续健壮要求业务模块尽可能解耦，模块自身要robust（对他人失败不敏感）与adaptive（对他人个性有宽容）。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023"], "summary": "由此得出对方既可从容易犯错也可自由发展，且没有人和这两点不「互补」；末段把「宽容」定义为和一切可能的你互补，并否定通常所说的「互补」能与之相提并论。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "互补论有个根本的逻辑问题：它基本不考虑人的变化。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "互补论非常容易让两人最初相信彼此是天作之合，此后却每天觉得对方「不再适合自己」。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述结果是互补论逻辑的必然：它怎么让两人走到一起，就会怎样催促他们分开。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "要求人「跟随对方成长」是不可能做到的。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "互补也罢、相似也罢，这种「成对耦合」的业务规则是一切升级的最大障碍。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想要系统永续和健壮，业务模块要尽可能解耦，且模块自身要强壮（robust）并富有适应性（adaptive）。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「健壮」指无论外界环境如何变化都能保持效能、对他人的失败不敏感；「富有适应性」指获得服务的门槛要求低、对他人的个性有宽容。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有人不与这两点「互补」，人们只是常把这种关系感受成「互补」罢了。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "通常所说的「互补」与宽容不能相提并论；所谓宽容，是指和一切可能的你互补。", "evidence": ["E12", "E13"]}
   ],
   "argument_steps": [
    "前提：互补论假设双方现在的互补关系可固定（P001-P002）。",
    "反例式追问：A变了、B也变了、双方变化的需求互相矛盾时，B将置身何处（P002-P005）。",
    "推论：互补论必然导向「不再适合自己」的日常感受（P006-P008）。",
    "理由：跟随对方成长不可能；对方需求可能同时是大卡车、购物车、婴儿车等（P009-P010）。",
    "类比移植：把亲密关系视为系统，成对耦合阻碍升级，程序员会痛骂（P011-P012）。",
    "替代标准：解耦、robust（对他人失败不敏感）、adaptive（对他人个性有宽容）（P013-P018）。",
    "收束：故对方可从容易错也可自由发展；宽容=和一切可能的你互补，与通常「互补」不同（P019-P023）。"
   ],
   "concept_usage": [
    {"term": "互补", "meaning": "两人性格或技能互相补足、彼此需要对方当前特质的配对逻辑；作者把它等同于「成对耦合」的业务规则并加以否定。", "evidence": "P011", "ambiguity": "末段作者又把「宽容」说成和一切可能的你互补，与全文批评的「互补」不是同一含义，同词两义。"},
    {"term": "成对耦合", "meaning": "把互补或相似当作关系基本规则，使双方互相绑定、彼此依赖。", "evidence": "P011", "ambiguity": "作者借软件工程词作类比，未说明类比在何种程度上成立。"},
    {"term": "健壮（robust）", "meaning": "无论外界环境如何变化都能保持自身效能，首先包括自身工作状态免疫于其他模块变化的影响，即对他人的失败不敏感。", "evidence": "P015", "ambiguity": "由软件模块移植到人，作者未说明人的「效能」如何衡量。"},
    {"term": "富有适应性（adaptive）", "meaning": "外界获得服务的门槛要求低，能适应各种奇怪格式的输入与交付形式，即对他人的个性有宽容。", "evidence": "P017", "ambiguity": "同上，属类比用法。"}
   ],
   "examples_and_targets": [
    "假设人物A与B及其变化情境——作者自设的假设性论证材料（P002-P005）。",
    "擎天柱只能变成大卡车、不能变购物车，以及婴儿车、四轮马车、摩托车、大风车——夸张类比，说明同时满足多样需求不可能（P009）。",
    "终结者——夸张类比，强化「都办不到」（P010）。",
    "「随便找一个程序员，都可以骂个三天三夜不重样」——以程序员群体作旁证式修辞（P012）。"
   ],
   "conditions": [
    "作者的批评限定在「互补论」这一说法上，其论证以「人会变化」为前提（P001）。",
    "追问以假设情境展开：设若两人现在很互补、明天A变了（P002）；要是B自己也变化了（P003）；要是双方变化对互补的需求互相矛盾（P004）；需要耐心的人改而需要激进的人（P005）。",
    "解耦与健壮、适应性的建议以「想要系统永续和健壮」为条件（P013-P014）。"
   ],
   "rhetoric_and_tone": "通篇反问密集（B是要自己跟上呢，还是要分手呢），以第二人称假设叙事推进；用擎天柱、终结者、购物车等流行文化意象夸张调侃；中段突然转入软件工程术语（业务模块、解耦、robust、adaptive）作体系类比；末段转为格言式短句下定义。语气是论辩性的否定与训诫，不评价提问者。",
   "unresolved_questions": [
    "作者未说明「宽容」和「和一切可能的你互补」在实践上如何做到，也未给出可操作标准。",
    "提问包含「相同」一方的选项，作者把「相似」与「互补」合并为「成对耦合」一并否定，未单独讨论相似。",
    "「成对耦合」从软件系统到亲密关系的类比是否成立，正文未作论证，属待外部/后续评估。",
    "擎天柱、终结者等形象的具体设定被当作论据使用，其引用来源未注明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "互补论有个根本的逻辑问题，那就是它基本不考虑人的变化。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P006", "quote": "互补论非常容易导致两个人在最开始相信彼此是天作之合", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "这是其逻辑的必然结果。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "它怎么让你们走到一起，就会怎样催促你们分开。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "因为要你“跟随对方成长”，是不可能做到的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "这种“成对耦合”的业务规则，是一切升级的最大障碍。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "想要系统永续和健壮，业务模块要尽可能的解耦。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "业务模块自身要强壮（robust）和富有适应性（adaptive）。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "无论外界环境如何变化，都能保持自己的效能", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "外界获得服务的门槛要求低", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P020", "quote": "没有人和这两点不“互补”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "实际上“互补”和它完全不能相提并论。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "所谓宽容，是指和一切可能的你互补。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系", "性格与配对", "系统论/软件工程类比"],
   "issue_candidates": ["性格互补是否有利于关系", "关系中的变化与适应", "耦合与解耦", "宽容的定义"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "经验总结"],
   "object_candidates": ["恋人", "程序员", "擎天柱", "终结者"],
   "working_keywords": ["互补", "成对耦合", "解耦", "robust", "adaptive", "宽容", "跟随对方成长"]
  },
  "notes": "正文为连续段落，无图片；平台为知乎，属回答体。提问者的问题与作者立场已分开记录。反驳对象是泛称的「互补论」，作者未点名具体出处。"
 },
 "ce35894e": {
  "analysis": {
   "question_context": "知乎问题「如何看待年轻人『躺平』的现象？」（Q001，属提问者）。作者不讨论该现象的社会成因，而是重新界定「躺平」：否定某种常见理解，主张真正的躺平另有门槛与代价。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以反问起头，先否定「不上班在家打王者荣耀」算是躺平，再提出只有出家当和尚、修士、道士才是真实的躺平。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "指出躺平需要另一种努力，比努力赚钱、做题、练习更艰难；并非往后一躺就能平；真想超然物欲还要天赋和老天爷的安排。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "以承受不了搬砖之苦作对比反问；并列举邻居、朋友、父母、女友的失望与鄙视比上司训斥更难忍受，说明躺平的代价。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "总结：选择不努力并不能免除努力，只是放弃一种特定努力，然后被命运踢进另一种更难逃脱的强制努力。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "用和尚口吻判定对方尘缘未了、六根未净，这样的水平躺不平，劝其吃了斋饭早点回去。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不上班在家打王者荣耀不算是躺平。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出家当和尚、当修士、当道士，才是真实的躺平。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "躺平需要另一种努力，比「努力赚钱」「努力做题」「努力练习」更艰难，并不是往后一躺就能平。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "真想超然物欲、目空一切，不光要努力，还要天赋，还要老天爷喜欢你、给你特别安排。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "连搬砖的苦都受不了的人，受不了躺平的苦。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "邻居、朋友、父母、女友那无法掩饰的失望和鄙视，比上司的训斥难受不知多少倍。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "选择不努力并不能免除努力：只是放弃一种特定的努力，然后被命运踢进另一种更不容易逃脱的强制努力。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对Wi-Fi没信号就焦虑、被人说几句就发狠的人，这样的水平是躺不平的。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "反问起头，质疑「躺平」一词被滥用（P001）。",
    "界定：在家打王者荣耀不算躺平（P002）。",
    "正面界定：出家当和尚、修士、道士才是真实躺平（P003）。",
    "指出躺平需要另一种更艰难的努力，靠一躺不能达成（P004-P005）。",
    "补充条件：还要天赋与「老天爷」的安排（P006）。",
    "以搬砖之苦作对比反问，质疑对方能否承受躺平之苦（P007）。",
    "举证代价：亲友的失望与鄙视比上司训斥更难忍（P008）。",
    "结论：选择不努力只是换一种更难逃脱的强制努力（P009）。",
    "以和尚口吻判定对方水平不够，劝其回去（P010-P011）。"
   ],
   "concept_usage": [
    {"term": "躺平", "meaning": "作者用来指彻底超然物欲、目空一切的出家式生活，而不是在家不工作、打游戏的状态；它本身是一种更艰难的努力。", "evidence": "P003", "ambiguity": "作者先否定一种理解、再给出正面界定，但未给出判定躺平的完整标准。"},
    {"term": "努力", "meaning": "可分为「努力赚钱/做题/练习」这类特定努力与躺平所需的另一种努力；放弃前者不等于不用努力。", "evidence": "P004", "ambiguity": "两种努力的具体差别正文未展开。"}
   ],
   "examples_and_targets": [
    "不上班在家打王者荣耀——被作者否定为躺平的反例（P002）。",
    "出家当和尚、当修士、当道士——作者举出的「真实的躺平」（P003）。",
    "「努力赚钱」「努力做题」「努力练习」——被比较的常见努力形态（P004）。",
    "搬砖——苦力的代称，用作对比反问（P007）。",
    "邻居、朋友、父母、女友 vs 上司——社会关系中的失望与训斥之对比（P008）。",
    "Wi-Fi没信号就焦虑——被用来判定对方定力不足的日常例证（P010）。",
    "「施主」「老衲」「斋饭」——借和尚身份作修辞扮演（P010-P011）。"
   ],
   "conditions": [
    "「真实的躺平」被限定为出家修行一类形态，等于把标准收窄（P003）。",
    "论断「躺不平」针对的是「你连搬砖的苦都受不了」「Wi-Fi没信号就焦虑」这类具体表现（P007、P010）。",
    "「真想超然物欲、目空一切」是条件句，所谈论的是这一目标下的要求（P006）。"
   ],
   "rhetoric_and_tone": "全篇短句、口语，反问与调侃并用；以「施主，老衲」「吃了斋饭」装扮和尚口吻作戏谑训诫；把年轻人的躺平话语反转为「躺平更难」的劝退式讽刺。无脏话，无对具体群体的实名指认。",
   "unresolved_questions": [
    "「躺平」的判定标准正文只给出去出家一类例子，未说明在家修行或隐居等形态是否算。",
    "「天赋」「老天爷喜欢你」属戏谑说法，作者未说明其实际所指。",
    "提问所问的「年轻人躺平现象」的社会成因与规模，本文未涉及，只回答了概念界定与代价。",
    "「王者的荣耀/王者荣耀」为游戏名，照原文记为「王者荣耀」。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "不上班在家打王者荣耀不算是躺平。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "出家当和尚、当修士、当道士，才是真实的躺平。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "躺平是需要另一种努力的，比“努力赚钱”“努力做题”“努力练习”更艰难的努力。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "并不是往后一躺，你就能平得了的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "这个不光是要努力，还要天赋、还要老天爷喜欢你，给你特别安排。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "你连搬砖的苦都受不了，你哪里受的了躺平的苦呢？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "比起你的上司那点训斥，难受不知道多少倍。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你只是在选择放弃一种特定的努力，然后被命运一脚踢到另一种更不容易逃脱的强制努力中去。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "这样的水平是躺不平的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心态", "生活方式", "修行/宗教生活"],
   "issue_candidates": ["躺平概念界定", "不努力的代价", "出家的门槛", "社会评价压力"],
   "text_function_candidates": ["答疑", "评论", "讽刺性训诫", "概念澄清"],
   "object_candidates": ["年轻人", "和尚", "修士", "道士"],
   "working_keywords": ["躺平", "出家", "努力", "强制性努力", "尘缘未了", "六根未净"]
  },
  "notes": "正文短、无图片，结构为11个段落，无标题或列表节点。提问者立场的「现象」框架与作者的概念反驳已分开记录。属知乎回答体。"
 },
 "f62a367a": {
  "analysis": {
   "question_context": "知乎问题「如何看待『艺术疗愈』这一概念？」（Q001，属提问者）。作者肯定艺术可以疗愈，但反对把疗愈等同于「用艺术表达/发泄情绪」，并进而给出自己的一套疗愈机制主张与徒手画直线的练习方案。正文含15个「note」分段与7个图片节点。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "定调：艺术可疗愈，但不是靠表达/发泄情绪；作者从根本上反对发泄情绪治疗法，并称任何形式的「发泄治疗」主张都在为发泄赋权、强化患者对它的认知。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "描述发泄疗法的获益结构：患者借此扩权、治疗师收获疗效与报酬、亲属暂得喘息，形成看似皆大欢喜的合谋。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "指出该合谋会催生更多轮情绪，循环至财务、亲情或自信不可持续；作者称之为「无责任协同抛弃」而非疗愈。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "正面界定疗愈机制：借某种实践在方寸之间安全犯错、查错、排除错误执念、寻找可行方式；直接谈人生因痛苦而防御、撒谎，使答复天然武断，沦为木偶戏。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "转为画直线教学：不谈惨痛经历，示范后布置「A4纸画满30度、间距5毫米平行线、允许1度误差」的作业，称徒手能完成者寥寥；因方法完备，线不直即有自欺。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035"], "summary": "以画为据谈心理：弯线、乱距、颤抖都是心的问题，与人生痛苦及傲慢、怯懦、逃避、虚荣、愤怒、悲哀有关；纸上是关系的结果，绝对安全且无法遮掩，纸是最好的评判者，错在心上。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "说明达成状态：安神坐照、物我两忘画完三十二根直线并知其来去对错，就知道事怎么做、如何面对自己与他人，进而看懂明暗冷暖等审美判断；找到通向自由的答案才是艺术的疗愈，停止发泄。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054"], "summary": "号召练习：作者一直等有人真正练起来；只有练起来后面的话才听得进；亲自走过一轮有利于对抑郁症免疫，是一剂抑郁疫苗。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P055", "P056"], "summary": "note 1：进度应以对方法的优化标定，而非「直度」；要的是照做必能画出高质量直线的方法，靠蒙出的结果不可靠。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P057", "P058"], "summary": "note 2：练习要有系统，用固定格式做系统积累，反对随手发图、无记录无总结。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073"], "summary": "note 3前半：获得能力的第一步是界定该能力及其衡量方式；以短跑的两套衡量机制为例，指出原理决定衡量机制、衡量机制决定训练计划。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089"], "summary": "note 3后半：列出画长直线的多项要求并追问优先顺序；强调不先弄清原理，练习终将失败，甚至成为抑郁的种子。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P090", "P091", "P092", "P093", "P094", "P095", "P096"], "summary": "note 3结尾：有原理才有计划，计划的失败可逼近更正确的原理；无原理的尝试是浪费生命、慢性自杀，即自己追求抑郁；反问画直线的原理与「身体里藏的直线」。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112"], "summary": "note 4：不得构建依赖「没有杂念」的方法；那是伪方法与中国技艺观的歧途，所得技能一见真章就崩，只是逼真幻觉；够资格当功夫基础的必须不依赖好状态。", "role": "rebuttal"},
    {"unit_id": "U015", "paragraph_refs": ["P113", "P114", "P115", "P116", "P117", "P118", "P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128"], "summary": "note 5：警惕「把酸痛练过去就行」的节点；用名画家是否相应肌肉发达作检验，指出质量随酸痛起伏即不可靠，强行猛练易劳损；训练要害是形成正确肌肉记忆，关键是体会何时才算「ok了」。", "role": "qualification"},
    {"unit_id": "U016", "paragraph_refs": ["P129", "P130", "P131", "P132", "P133", "P134", "P135", "P136", "P137", "P138", "P139", "P140", "P141", "P142", "P143", "P144", "P145", "P146"], "summary": "note 6：没有量角器时如何确定30度——折纸、以手指宽度记忆交点、利用整张纸尺度误差小、平板界面元素定位；引「善假于物」。", "role": "action_advice"},
    {"unit_id": "U017", "paragraph_refs": ["P147", "P148", "P149", "P150", "P151", "P152", "P153", "P154", "P155", "P156"], "summary": "note 7：以小田原之喻讲坚持：不衰不竭、日日寸进终有胜利；只在人声鼎沸时才士气旺盛的努力是「集体娱乐」，依赖环境者一旦失去环境就完了；不依赖环境的努力是必过一关。", "role": "action_advice"},
    {"unit_id": "U018", "paragraph_refs": ["P157", "P158", "P159", "P160", "P161"], "summary": "note 8：画30度斜线不必身体做30度动作，可转腰或转纸；引穆罕默德与山。", "role": "action_advice"},
    {"unit_id": "U019", "paragraph_refs": ["P162", "P163", "P164", "P165", "P166", "P167", "P168", "P169", "P170", "P171", "P172", "P173", "P174", "P175", "P176", "P177", "P178", "P179", "P180", "P181", "P182", "P183", "P184", "P185"], "summary": "note 9：以「允许无限放慢、无限修改」的笨办法取得百分百可复用的成功，把问题从做不做得到转为做得好不好；以交点密度衡量改进；方法可靠性比随机最优结果重要；先找笨办法再优化是近乎普适的策略。", "role": "claim"},
    {"unit_id": "U020", "paragraph_refs": ["P186", "P187", "P188", "P189", "P190", "P191", "P192", "P193", "P194"], "summary": "note 10：战争、饥荒、灾难牵动情绪时正是压力测试与建立自我信任的良机；世事无常而你可以有常，坐得住即给身边人撑起安宁；手里的线不要停且要更直。", "role": "action_advice"},
    {"unit_id": "U021", "paragraph_refs": ["P195", "P196", "P197", "P198", "P199", "P200", "P201", "P202"], "summary": "note 11—12：追问画出示范线的成功概率与「一群人如何一起研究」；心情不好、水平大乱正是练「心情不好也能画直」的机会。", "role": "open"},
    {"unit_id": "U022", "paragraph_refs": ["P203", "P204", "P205", "P206", "P207", "P208", "P209", "P210", "P211", "P212", "P213", "P214"], "summary": "note 13—14：偶然画出直线已足作研究素材，知其所以然才能复制；坚持=断了会捡回来，须落在记录上，为随时捡起做铺垫，是永续经营的必要习惯。", "role": "action_advice"},
    {"unit_id": "U023", "paragraph_refs": ["P215", "P216", "P217", "P218", "P219"], "summary": "note 15：追问笔尖走直线时腕、肘关节轨迹的曲线及空间关系，提示小臂与掌骨长度基本不变；文末标「（未完，待续）」。", "role": "open"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术可以疗愈，但这绝不是「用艺术将自己的情绪表达/发泄出来」能办到的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者从根本上反对「发泄情绪」治疗法，这与用什么手段发泄无关。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要承认「有情绪就需要发泄」、主张发泄可治愈情绪问题，甚至主张他人应对发泄者退让的特权作为政策，就是在事实上对发泄情绪赋权，帮其确立获得权力的巫术。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论用什么形式主张「发泄治疗」，都是在强化患者对这个观念的认知。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "患者乐意帮证明疗法有效，因为该疗法事实上在帮其扩权；真正让患者「好多了」的是由此获得随时随地「情绪降神」的特权。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被册封为「成功经验」的情绪发泄疗法会迅速催生第二、三、四轮情绪，循环往复直到财务、亲情或自信不可持续。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这种发泄疗法并不是疗愈，而是一种微妙的「无责任协同抛弃」。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术疗愈（乃至任何疗愈方式）是借某种实践在方寸之间提供安全犯错、检查错误、排除错误执念、寻求正确可行方式的过程。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "直接谈人生既过于痛苦也过于武断；因痛苦而高度防御、不自知地撒谎隐瞒，客观上已使医治者能给的答复天然武断。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "画线上没有一个问题事实上是技术问题，每个问题都与人生痛苦有直接关系。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "纸上练习是绝对安全、无法遮掩也无需遮掩的，这张纸就是最好的评判者。", "evidence": ["E20", "E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "练习者从来不是错在技术原因和生来不足上，而是错在心上。", "evidence": ["E22"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "能安神坐照、物我两忘地画完三十二根直线并知其来处去处与对错，就知道事情怎么做、如何面对自己与别人；找到这个通向自由的答案才是艺术的疗愈。", "evidence": ["E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "亲自走过一轮练习将大大有利于对抑郁症免疫，这实际上是一剂抑郁疫苗。", "evidence": ["E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "练习进度不能用所谓的「直度」标定，而要用对方法的优化来标定。", "evidence": ["E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "获得任何一种能力的第一步，是先对这种能力作出界定、确定如何衡量其达成程度。", "evidence": ["E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "选择衡量机制时就决定了「训练游戏」的类型；能力本身的原理决定衡量机制，衡量机制决定训练计划。", "evidence": ["E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若不先回答或研究清楚画直线的原理、哪怕只提出逻辑通顺的假说，一切练习都终将失败，不但不能成为抑郁疫苗反而会成为抑郁的种子。", "evidence": ["E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有了原理才有计划，失败就只是计划的失败而非人本身的失败；没有原理、无法提高下次成功概率的尝试是在浪费生命，长期慢性自杀就是在自己追求抑郁。", "evidence": ["E32", "E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "需要「没有杂念」才能行得通的方法是伪方法；中国技艺观以此为正途是歧途，由此获得的技能只是致命的逼真幻觉。", "evidence": ["E35", "E36", "E37"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "够资格成为功夫逻辑基础的方法，必须不依赖「没有杂念」的好状态。", "evidence": ["E38"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若画直线的方案导致肌肉很快酸痛，直线质量会随酸痛起伏，说明方法不可靠；需要形成肌肉记忆的训练，第一要害是保证形成正确的肌肉记忆。", "evidence": ["E39", "E40"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要城可落，每天只有寸进也迟早有胜利的一天；只在人声鼎沸时才士气旺盛的努力只是「集体娱乐」，而曲终人散仍兴致勃勃的努力是建立不依赖环境的能力必过的一关。", "evidence": ["E44", "E45"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "允许无限放慢、无限修改的笨办法是百分百可以成功复用的方法，它把问题从「做不做得到」转向「做得够不够好」。", "evidence": ["E49", "E50"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "方法的可靠性（稳定的可重复性）比它能随机达到的最理想结果重要；先找到百分百成功的笨办法再将其无限优化，是近乎普适的策略。", "evidence": ["E51", "E52"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有知道为什么会成功，成功才有可能复制；坚持不是「连续不断」，而是「即使断了，也会捡回来」。", "evidence": ["E56", "E57"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在无常世事中坐得住，就等于给身边的人撑起一个角的安宁，这比能做出什么、生产什么更重要。", "evidence": ["E54"]}
   ],
   "argument_steps": [
    "提出反面界定：艺术疗愈不是把情绪表达/发泄出来（P001）。",
    "断言发泄疗法的要害在赋权：承认发泄需要、主张它可治愈、要求他人退让，就是在授予特权（P002-P004）。",
    "分析获益结构：患者得特权、治疗师得疗效报酬、亲属暂得喘息，形成合谋（P005-P008）。",
    "推出后果：合谋使发泄被册封为成功经验，催生更多轮情绪直至不可持续，实为「无责任协同抛弃」（P009-P012）。",
    "给出正面定义：疗愈是借实践在方寸之间安全犯错、排错、寻找可行方式的过程（P013）。",
    "说明为何不谈人生：痛苦→防御→撒谎→答复天然武断，故直接谈人生是木偶戏（P014-P016）。",
    "改换材料：以画直线为「记录在案、证据确凿的事实」，示范并布置作业（P017-P024）。",
    "解释病理：纸上的偏差是心的问题，与人生痛苦相关；纸安全、无法遮掩，故可作评判者（P025-P035）。",
    "给出目标状态：安神坐照画完直线即知事之做法，进而看懂审美与自由（P036-P048）。",
    "行动要求：停止发泄、练起来、系统记录（P049-P058）。",
    "方法论要求：先界定能力与衡量机制，再定计划（P059-P096）。",
    "方法可靠性要求：不依赖无杂念状态，不把酸痛当门槛，先找百分百可复用的笨办法再优化（P097-P185）。",
    "坚持与外境：以日常压力为测试，断了捡回来，并留下追问腕肘轨迹的悬念（P186-P219）。"
   ],
   "concept_usage": [
    {"term": "疗愈", "meaning": "借某种实践在方寸之间安全犯错、检查错误、排除错误执念、寻求正确可行方式的过程，而非把情绪表达或发泄出来。", "evidence": "P013", "ambiguity": "作者既说「任何疗愈的方式其实都一样」，又说「这才是艺术的疗愈」，两者关系未展开。"},
    {"term": "发泄（情绪发泄疗法）", "meaning": "把表达/发泄情绪当作治疗手段，并进而主张发泄者应获他人退让的特权；作者称其在事实上为发泄赋权。", "evidence": "P003", "ambiguity": "未区分一时的发泄行为与作为治疗主张/政策的发泄，批评的边界靠读者自行判断。"},
    {"term": "情绪降神", "meaning": "患者借发泄获得的、可随时索要注意与让步的特权，作者称这才是让其「好多了」的东西。", "evidence": "P006", "ambiguity": "戏谑性命名，正文未给出可检验定义。"},
    {"term": "无责任协同抛弃", "meaning": "患者得特权、治疗师得疗效与报酬、亲属暂得喘息，三方各自获益而无人对后果负责的关系模式。", "evidence": "P012", "ambiguity": "作者以此否定发泄疗法的疗效，但未给出判定该模式出现的标准。"},
    {"term": "原理—衡量机制—训练计划", "meaning": "能力本身的运行原理决定成绩衡量机制，衡量机制决定训练计划；衡量机制的选择同时决定「训练游戏」的类型。", "evidence": "P071", "ambiguity": "作者以短跑为例说明，但画直线的原理在文中始终以提问形式留给读者（P088、P095）。"},
    {"term": "交点密度", "meaning": "首次绘制后弯曲的线与理想直线相交的数量（严格说是每厘米的交点数），被作者用作衡量进步的指标。", "evidence": "P171", "ambiguity": "作者先以「理想交点」表述，随后改写为密度，两者换算未说明。"},
    {"term": "肌肉记忆", "meaning": "靠大训练量形成的自动化动作；作者强调必须形成正确的肌肉记忆，错的肌肉记忆一旦形成很难摆脱。", "evidence": "P124", "ambiguity": "未说明如何界定「正确」。"},
    {"term": "「ok了」", "meaning": "判断方法已经可靠到可以下重注、上大练习量的那个时点。", "evidence": "P125", "ambiguity": "作者说这是修炼要逼迫体会的point，但未给出外部判据。"},
    {"term": "抑郁疫苗", "meaning": "作者对亲自走完一轮直线练习之效果的比喻：有利于对抑郁症免疫。", "evidence": "P054", "ambiguity": "比喻性断言，正文未提供临床或统计依据。"}
   ],
   "examples_and_targets": [
    "短跑能力的两套衡量机制（百米时间分级 vs 最高瞬间速度+启动时间+维持距离）——作者自举的例子（P063-P068）。",
    "名画家是否相应肌肉发达——作者自设的检验假设，用于否定「把肌肉练强即可」的方案（P119-P121）。",
    "「难攻不落小田原」与一鼓作气——历史比喻（P148-P151）；「穆罕默德与山」——典故（P160-P161）。",
    "量角器、A4纸折角、手指宽度、iPad/Procreate界面元素——无设备时定位30度的实操例证（P131-P142）。",
    "「君子性非异也，善假于物耳」及英文戏译「有物不假大傻瓜」、「飞花摘叶，皆可伤敌」——引用与戏仿式修辞（P143-P146）。",
    "「狗肉上不得正席」——俗语，用于形容依赖无压力状态的技能（P103）。",
    "「丢勒」（P043）——单独成段的人名，前接「合拢的双手」「微垂的眼眉」等语，疑与图片或画作有关，因图片未核验不能确定其作用。",
    "图片节点 IMG001—IMG007（IMG001 与 IMG007 为同一 src）——内容未核验，状态 pending。",
    "「note 1」—「note 15」分段标记（P055、P057、P059、P097、P113、P129、P147、P157、P162、P186、P195、P199、P203、P208、P215）——作者自设的补充说明结构。",
    "「ctrl」「point」「procreate」「ok」等英文/软件词混用——语言风格材料，非论据。"
   ],
   "conditions": [
    "对发泄疗法的批评限定在「承认有情绪就需要发泄、主张发泄可治愈、甚至主张他人应退让」这类主张或政策上（P003-P004）。",
    "发泄疗法的负面循环以治疗师、亲属的配合与获益为条件（P007、P010）。",
    "画线作业的参数被明确限定：整张A4纸、30度、间距5毫米、允许1度误差（P021）；目标是三十二根直线（P036）。",
    "方法有效性的条件是：不依赖「没有杂念」的好状态、有杂念也无所谓（P100、P110）。",
    "上大练习量的前提是先确信「这回ok了」（P125-P128）。",
    "「抑郁疫苗」的说法以亲自走完一轮练习为前提（P053-P054）。",
    "练习失败的论断以「不先回答清楚或研究清楚原理」为条件（P089）。",
    "note 10 的安宁论断以「你坐的住」为条件（P191）。",
    "note 8 的转腰/转纸建议以「找到你正坐时最轻松、最直的角度」为前提（P159）。"
   ],
   "rhetoric_and_tone": "第二人称「你」的师徒/治疗者口吻，断言与训诫交替；反问极多（你听懂了这直线是怎么画的了吗、为什么要逃），并直接给读者布置作业。用「木偶戏」「精神嫖宿」「情绪降神」「无责任协同抛弃」等尖锐命名制造冲击；note 段落呈箴言体，夹杂文言引用、英文戏译与软件词；结尾以「（未完，待续）」留悬念。批评对象是发泄疗法及「中国的技艺观」中的一条路径，而非具体个人。",
   "unresolved_questions": [
    "本篇有7个图片节点（IMG001—IMG007，其中IMG001与IMG007为同一src），内容均未核验，图片状态为pending；「丢勒」（P043）这个单段人名的指涉无法与图片对照确认，需人工/多模态复核。",
    "作业「30度、间距5毫米」与「三十二根直线」的对应关系、示范线的具体形态，只能靠图片核实。",
    "正文提到「评论区里有人开始了」，评论区内容不在本记录范围，无法核查。",
    "「抑郁疫苗」「有利于对抑郁症免疫」是作者的经验性/比喻性断言，需外部核查，本文未给依据。",
    "「情绪降神」「巫术」「无责任协同抛弃」等命名属修辞，正文未提供可检验的操作定义。",
    "文末标「（未完，待续）」，后续文章是否存在及其内容，本文未说明。",
    "「小田原」「穆罕默德移山」「君子性非异也」等引用未注明出处，属待外部核查的事实性材料。",
    "note 标记插在正文之间，编号与正文段落的对应关系依语料原顺序记录，未做重排。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "艺术当然是可以疗愈的，但是这绝不是“用艺术将自己的情绪表达/发泄出来”可以办得到的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "我从根本上反对所谓的“发泄情绪”治疗法", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你就是在事实上对发泄情绪赋权，是在帮ta们确立一种获得权力的巫术。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你都是在强化患者对这个观念的认知。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "患者会非常乐意帮你证明这“疗法”有效", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "真正让ta“好多了”的，是由此获得的随时随地“情绪降神”的特权。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "当事人的亲属暂时摆脱了这一次的“情绪紧逼”。", "relation": "context"},
    {"key": "E8", "paragraph_id": "P009", "quote": "会迅速的催生第二轮，第三轮、第四轮情绪。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "循环往复，愈演愈烈，直到不可持续", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "这并不是疗愈，而是一种微妙的“无责任协同抛弃”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "在方寸之间提供一个安全的犯错、检查错误、排除错误执念、寻求正确可行的方式的过程。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "这导致你客观上已经保证了医治者能给你的一切答复都天然是武断的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P016", "quote": "一种花钱请人陪聊的精神嫖宿。", "relation": "context"},
    {"key": "E14", "paragraph_id": "P021", "quote": "就是在一整张A4纸上画满30度的间距为5毫米的平行线", "relation": "context"},
    {"key": "E16", "paragraph_id": "P024", "quote": "你必有自欺欺人之处。", "relation": "context"},
    {"key": "E17", "paragraph_id": "P026", "quote": "你会看到，没有一个问题事实上是技术的问题。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "这些问题，每一个都和你的人生痛苦有直接关系。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "这张纸就是最好的评判者", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P032", "quote": "你是绝对安全的，你也是无法遮掩、无必要遮掩的。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P035", "quote": "你从来就是错在心上。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P038", "quote": "你什么时候就知道事情是怎么做的，该怎么做", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P048", "quote": "找到这个通向自由的答案，这才是艺术的疗愈。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P054", "quote": "亲自走过一轮，将会大大的有利于对抑郁症免疫", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P056", "quote": "你的进度不能用所谓的“直度”来标定，而要用你对方法的优化来标定。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P058", "quote": "发练习要有系统。", "relation": "context"},
    {"key": "E28", "paragraph_id": "P061", "quote": "是要先对这种能力作出界定", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P070", "quote": "在你选择衡量机制的时候，你就决定了你觉得“训练游戏”的游戏类型。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P072", "quote": "而成绩衡量机制，则决定了你的训练计划。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P089", "quote": "反而会成为抑郁的种子。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P090", "quote": "有了计划，失败就只是计划的失败而不是人本身的失败。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P094", "quote": "长期慢性自杀，本身就是在自己追求抑郁。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P098", "quote": "不要构建一个“如果我没有杂念的执行就可以行得通”的办法", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P101", "quote": "本质上其实是个伪方法", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P106", "quote": "只是一种致命的逼真幻觉。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P110", "quote": "必须不依赖“没有杂念”的好状态。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P122", "quote": "直线的质量会随你的肌肉酸痛程度起伏变化", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P124", "quote": "第一个要害就是要保证形成的是正确的肌肉记忆", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P125", "quote": "就是要逼迫你们一步步的体会到“要到什么时候才可以说‘这回ok了’”。", "relation": "context"},
    {"key": "E42", "paragraph_id": "P135", "quote": "其折痕是不是就是30度角？", "relation": "context"},
    {"key": "E43", "paragraph_id": "P143", "quote": "君子性非异也，善假于物耳。", "relation": "context"},
    {"key": "E44", "paragraph_id": "P151", "quote": "只要此城可落，就是每天只有寸进，也迟早有胜利的一天。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P155", "quote": "这是你建立不依赖于环境的能力必过的一关。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P164", "quote": "允许无限放慢速度、无限的修改获得平直的线", "relation": "context"},
    {"key": "E49", "paragraph_id": "P166", "quote": "百分百可以成功复用的笨办法", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P169", "quote": "使得问题从“做不做得到”转向了“做得够不够好”。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P180", "quote": "一个方法的可靠性——即稳定的可重复性——要比这个方法可以随机达到的最理想结果重要。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P184", "quote": "先找到这个百分百成功的笨办法，然后再将这个笨办法无限的优化", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P191", "quote": "你就给你身边的人在无常的世界里撑起了一个角的安宁。", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P206", "quote": "只有知道为什么会成功，成功才有可能复制。", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P209", "quote": "坚持不是“连续不断”，而是“即使断了，也会捡回来”。", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P218", "quote": "你的肘尖走过的是什么轨迹？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理疗愈", "艺术教育", "绘画技法", "方法论/学习法"],
   "issue_candidates": ["艺术疗愈的定义", "情绪发泄疗法的质疑", "治疗关系与特权", "技能衡量机制", "肌肉记忆与训练量", "坚持与记录"],
   "text_function_candidates": ["答疑", "批评", "教学/示范", "经验总结", "箴言式随笔"],
   "object_candidates": ["患者", "治疗师", "艺术家/画家", "丢勒", "中国技艺观", "抑郁症"],
   "working_keywords": ["疗愈", "发泄情绪", "情绪降神", "无责任协同抛弃", "直线练习", "肌肉记忆", "抑郁疫苗", "交点密度", "百分百可复用"]
  },
  "notes": "本篇含7个图片节点（IMG001—IMG007，IMG001与IMG007为同一src），我无图片查看能力，图片内容未经核验，故 status=needs_reread、image_checked=False、full_text_checked=False；已读部分为全部正文文本（P001—P219，body_chars=7506）。正文以「note 1」至「note 15」分段，文末为「（未完，待续）」。逐字短引均取自阅读包正文；图片相关判断留待图像核验。",
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False
 },
 "fdedff1c": {
  "analysis": {
   "question_context": "知乎问题「如何看待恋爱中对一些无伤大雅的承诺的违背？但凡是承诺，就应该较真吗？」（Q001，属提问者）。作者否认「无伤大雅的承诺」这一类别存在，并把讨论限定在恋爱/结婚语境，给出被指出后应如何反馈的判断。提问中的一般性「是否该较真」未被单独回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "直接否定「无伤大雅的承诺」这种东西存在，并称在恋爱中尤其如此。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "让步：结婚是在赌命，恋爱期间有不守承诺的事也可以理解，因为人难免高估自己的能力。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "提出唯一可接受的反馈是愧悔无地、全礼道歉；若不道歉反而辩解、指责对方小题大做，就只有分离一种结果。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "给出理由与结论：一方在赌命而另一方在过家家，后者精神上还是儿童，故不要和儿童谈恋爱。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这个世界上根本没有「无伤大雅的承诺」这种东西。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在恋爱中，承诺更没有「无伤大雅」一说。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "结婚就是在赌命；谈恋爱期间有不守承诺的事情也就罢了，因为人难免有高估自己能力的时候。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一旦不守承诺被指出来，只有一种可以接受的反馈，就是「愧悔无地，全礼道歉」。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若不道歉还要辩解，甚至反过来说「无伤大雅」、判责怪者「小题大做」的罪，就只有一种结果，就是分离。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "之所以如此，是因为一方是在赌命，另一方是在过家家。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "辩解者还没活醒，在精神上还是一个儿童。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要和儿童谈恋爱。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "否定前提：不存在「无伤大雅的承诺」（P001）。",
    "收窄语境：恋爱中更是如此（P002）。",
    "让步：结婚是赌命；恋爱期间偶有不守承诺可理解，因人多半高估自己能力（P003）。",
    "提出唯一可接受的反馈：被指出后应愧悔无地、全礼道歉（P004）。",
    "给出反面后果：若辩解并倒打一耙说对方小题大做，则只有分离（P005）。",
    "说明理由：一方赌命、一方过家家，后者精神上仍是儿童（P006-P007）。",
    "结论式劝告：不要和儿童谈恋爱（P008）。"
   ],
   "concept_usage": [
    {"term": "无伤大雅的承诺", "meaning": "指被认为轻微、违背了也无关紧要的承诺；作者否认这一类别的存在，尤其在恋爱中。", "evidence": "P001", "ambiguity": "作者未说明承诺的轻重如何划分，也未讨论确实无力履行的例外。"},
    {"term": "赌命 / 过家家", "meaning": "「赌命」形容结婚一事的后果重大；「过家家」形容把关系当儿戏的态度。", "evidence": "P006", "ambiguity": "均为比喻，未给出判定某人属于哪一种的标准。"},
    {"term": "儿童", "meaning": "指精神上尚未成熟、不守承诺被指出后仍狡辩的人，与年龄无关。", "evidence": "P007", "ambiguity": "戏谑性称谓，未说明如何识别。"}
   ],
   "examples_and_targets": [
    "恋爱/结婚关系——作者讨论的场景（P002-P003）。",
    "「结婚就是在赌命」——比喻式断言（P003）。",
    "不道歉、辩解、反过来说「无伤大雅」、判责怪者「小题大做」的罪——作者设想并反驳的反馈方式（P005）。",
    "「过家家」「精神上还是一个儿童」「不要和儿童谈恋爱」——修辞性类比与结论（P006-P008）。"
   ],
   "conditions": [
    "论断以恋爱/结婚关系为场景（P002-P003）。",
    "让步条件：恋爱期间不守承诺「也就罢了」，其前提是「人难免有高估自己能力的时候」（P003）。",
    "道歉要求以「一旦被指出来了」为前提（P004）。",
    "分离的结论以「不但不道歉，还要辩解，甚至还要反过来说什么『无伤大雅』」为条件（P005）。"
   ],
   "rhetoric_and_tone": "简短断言与判决式句式（「这个世界上根本没有…」「只有一种…」）；先让步再转折（「也就罢了——但是」）；用「赌命/过家家」「儿童」等类比与戏称下结论，末句格言化（「不要和儿童谈恋爱」）。语气严厉、训诫，未点名任何具体人或事件。",
   "unresolved_questions": [
    "「无伤大雅的承诺」的界定标准、以及确实无力履行时是否仍应归责，正文未说明。",
    "作者未说明「全礼道歉」的具体内容与补救方式，也未说明道歉之后是否仍需其他行动。",
    "「赌命」「过家家」「精神上还是一个儿童」均为比喻，未给可操作判据。",
    "提问中「但凡是承诺，就应该较真吗」的一般性问题（超出恋爱语境）未被单独回答。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个世界上根本没有“无伤大雅的承诺”这种东西。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "在恋爱中就更是如此。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "结婚就是在赌命", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "人难免有高估自己能力的时候。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P004", "quote": "就只有一种可以接受的反馈，就是“愧悔无地，全礼道歉”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "这只有一种结果，就是分离。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "因为你是在赌命，ta是在过家家。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "ta还没活醒，在精神上还是一个儿童。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "不要和儿童谈恋爱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系", "伦理/承诺"],
   "issue_candidates": ["恋爱中承诺的违背", "是否该较真", "道歉与辩解", "关系中的成熟度"],
   "text_function_candidates": ["答疑", "论断", "训诫"],
   "object_candidates": ["恋人", "儿童"],
   "working_keywords": ["无伤大雅的承诺", "较真", "赌命", "过家家", "全礼道歉", "小题大做"]
  },
  "notes": "无图片节点；正文8段，属知乎回答体。提问者的问题框架与作者判断已分开记录。作者未点名任何具体事件或人物。"
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
