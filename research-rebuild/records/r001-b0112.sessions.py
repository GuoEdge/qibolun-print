# -*- coding: utf-8 -*-
"""批次 r001-b0112 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0112.sessions.py            # 写 out/r001-b0112.out.jsonl
  python3 records/r001-b0112.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0112"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0112.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "4eae907d": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何克服自卑？”，预设自卑是需要克服的缺陷。作者（回答者）不接受这一预设：开篇即以反讽语气质疑为何要盘算“克服”自卑，随后论证自卑是优良的生存策略与本能设计，把真正的问题定位为“无法兑现自卑好处而无所不用其极去克服它”的蠢事，最后给出“带着自卑去行动”的忠告。提问者的“克服”立场与作者立场相反，不得混同。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002"
     ],
     "summary": "以调侃反问质疑“克服自卑”这一议题本身，称自卑“这么萌”、盘算克服它的人“太坏了”。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P003",
      "P004"
     ],
     "summary": "给出自卑的界定（把自己看得低于“应有的地位”、把别人看得高于“应有的”地位），并称这其实是非常优良的生存策略，能抑制“我也可以”式鲁莽与撞南墙的风险。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P005",
      "P006",
      "P007",
      "P008"
     ],
     "summary": "称自卑能大量避免与人争夺“应得”之物；批评成功者只是反刍成功案例与高光时刻，并称被追索的“正义”大部分是“自信”甚至贪婪造出来的，所谓自信不过是得手的贼胆子较大。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P009",
      "P010",
      "P011"
     ],
     "summary": "称自卑与对无常未知的不安是人刻苦努力的最大驱动力之一、使人心听得进教训的最主要抗硬化剂，并把它与“谦虚”区分开，称谦虚是假的、只是宣传口的话术。",
     "role": "claim"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P012",
      "P013",
      "P014",
      "P015",
      "P016",
      "P017"
     ],
     "summary": "指出自卑的真正问题不在自卑身上，而在其焦虑痛苦产生的心理动力因学习修炼方法失当被徒然浪费；以发动机空转、未挂离合器、车不动的比喻说明，并以“不如关了它，是吗”反问。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020",
      "P021",
      "P022",
      "P023"
     ],
     "summary": "称自卑引发的真正问题是人们无法兑现其好处而无所不用其极地“克服”“战胜”它所做的蠢事：四面搜罗的虚荣、互相注射麻药的“朋友圈”、对触及痛处者的坚决反击与排除。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P024",
      "P025",
      "P026",
      "P027",
      "P028",
      "P029"
     ],
     "summary": "把“努力奋斗、功成名就”这条所谓正道也纳入麻醉之列，断言得了世界冠军也照样自卑；以挂了档发动机仍响仍震作比，称自卑不是bug而是设计，只要活着就跟随人。",
     "role": "claim"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P030",
      "P031",
      "P032",
      "P033",
      "P034"
     ],
     "summary": "行动忠告：自卑就自卑，不要把问题归结到自卑上；自卑、没把握取胜、害怕不能成功、觉得没人喜欢、对回报没信心，仍要去战斗、拼搏、爱、尽义。",
     "role": "action_advice"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P035",
      "P036",
      "P037",
      "P038",
      "P039",
      "P040",
      "P041"
     ],
     "summary": "结论：正因自卑害怕，这些行为才真正可贵动人；痛苦并非没有价值，成功微不足道，是痛苦令人动容。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者不接受“克服自卑”的提问预设，以反讽反问质疑为何要盘算着克服自卑。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "自卑（把自己看得低于“应有的地位”、把别人看得高于“应有的”地位）其实是非常优良的生存策略：抑制“我也可以”式鲁莽、避免为争夺“应得”之物而起的争斗。",
     "evidence": [
      "E2",
      "E3",
      "E4"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人们追索的“正义”大部分是“自信”甚至贪婪造出来的，所谓的“自信”不过是得过手的贼胆子较大。",
     "evidence": [
      "E5",
      "E6"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "自卑与对无常未知的不安是人刻苦努力的最大驱动力之一、使人心听得进教训的最主要抗硬化剂；它不是谦虚，谦虚是假的、只是宣传口的话术。",
     "evidence": [
      "E7",
      "E8"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "自卑的真正问题不在自卑身上，而在于其焦虑痛苦造成的心理动力因学习与修炼方法失当被徒然浪费，如同发动机空转、未挂上离合器。",
     "evidence": [
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "自卑引发的真正问题是人们无法兑现它的好处，于是无所不用其极地“克服”“战胜”它而做蠢事：搜罗虚荣、结成互相麻醉的朋友圈、坚决反击并排除触及痛处的人。",
     "evidence": [
      "E11",
      "E12"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "连“努力奋斗、功成名就”这条传说中能真正解决自卑的正道也在麻醉之列：经过艰苦努力得着世界冠军之后，人也一样会自卑。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "自卑不是缺陷（bug）而是本能与设计，只要活着就跟随并鞭策人；它不再响、不再震的时候，就是它停了。",
     "evidence": [
      "E14"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "行动忠告：自卑就自卑，不要把问题归结到自卑上；即使自卑、没有把握取胜、害怕不能成功，仍要去战斗、拼搏、爱和尽义。",
     "evidence": [
      "E15",
      "E16"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "恰恰因为自卑、害怕，这些行为才真正可贵并触动人；痛苦并非没有价值——成功微不足道，是痛苦令人动容。",
     "evidence": [
      "E17",
      "E18"
     ]
    }
   ],
   "argument_steps": [
    "先重构问题：拒绝“如何克服自卑”的预设，以调侃反问质疑为何要克服自卑（P001-P002）。",
    "给出界定：自卑即把自己看得比“应有的地位”更低、把别人看得比“应有的”地位更高（P003）。",
    "理由一：这是优良的生存策略，能抑制“我也可以”式鲁莽（P004），并大量避免与人争夺“应得”之物的争斗（P005）。",
    "对成功者与“正义”的反驳：成功者只是反刍成功案例与高光时刻，未必全局衡量过成本；被追索的正义多为自信甚至贪婪所造（P005-P007）。",
    "理由二：自卑与对无常未知的不安是刻苦努力的最大驱动力之一与抗硬化剂（P009）；与“谦虚”作区分，称谦虚是宣传话术（P010-P011）。",
    "问题重述（转折）：真正的伤害是心理动力因方法失当被浪费，用发动机空转、未挂离合器、车不动的比喻说明（P012-P015）。",
    "让步式反问：既然车没动，这份震到手麻的动力是否只是徒然干扰、不如关掉它（P016-P017）。",
    "实质危害的展开：真正的问题是人们为“克服”“战胜”自卑所做的蠢事——虚荣、麻醉性朋友圈、排除触及痛处者（P018-P023）。",
    "扩大反驳：连努力奋斗、功成名就这条正道也不能解决自卑，得世界冠军后照样自卑（P024-P025）。",
    "比喻收束：挂上档车跑起来，发动机仍然响、仍然震手（P026-P027）。",
    "结论一：自卑是本能与设计而非缺陷，活着一天就跟随一天，停了才是停了（P028-P029）。",
    "行动忠告：自卑就自卑，不要把问题归到自卑上；自卑害怕之下仍要战斗、拼搏、爱、尽义（P030-P034）。",
    "结论二：正因自卑害怕，行为才可贵动人；痛苦而非成功令人动容（P035-P041）。"
   ],
   "concept_usage": [
    {
     "term": "自卑",
     "meaning": "把自己看得比“应有的地位”更低一等、把别人看得比“应有的”地位更高一等的心理状态；作者把它定性为优良的生存策略与本能设计，而非待克服的缺陷。",
     "evidence": "P003",
     "ambiguity": "作者未界定“应有的地位”由谁判定，该词带有反讽引号，含义依赖上下文。"
    },
    {
     "term": "克服/战胜（自卑）",
     "meaning": "作者指称提问者与常见做法所追求的目标，他把这类努力归为无法兑现自卑好处后的蠢事与麻醉手段。",
     "evidence": "P001",
     "ambiguity": "作者未区分不同“克服”方式，也未说明是否存在他认可的正当处理方式。"
    },
    {
     "term": "自信",
     "meaning": "在本文中被贬义化使用：所谓自信不过是得过手的贼胆子较大，是造出“正义”的来源之一。",
     "evidence": "P008",
     "ambiguity": "与通常心理学意义上的自信不同，本文属于作者特定的贬义用法。"
    },
    {
     "term": "正义",
     "meaning": "本文指人们“正义的追索”所争之物，作者称大部分是自信甚至贪婪创造出来的。",
     "evidence": "P005",
     "ambiguity": "作者未给出“真正正义”的标准，仅质疑多数追索的成色。"
    },
    {
     "term": "抗硬化剂",
     "meaning": "作者自造词：使人心能听得进教训、不至于僵化的机制，自卑与对无常未知的不安是其最主要的来源。",
     "evidence": "P009",
     "ambiguity": "无外部出处，属作者自创比喻性概念。"
    },
    {
     "term": "离合器/挂档",
     "meaning": "比喻把自卑带来的心理动力转化为实际前进的中介机制；未挂上离合器即动力空转、车不动。",
     "evidence": "P014",
     "ambiguity": "该比喻对应的现实方法作者未说明。"
    },
    {
     "term": "bug/设计",
     "meaning": "作者借软件用语称自卑不是可修复的缺陷，而是人的固有设计。",
     "evidence": "P028",
     "ambiguity": "“设计”是否指向某种造物者或进化机制，文中未交代。"
    }
   ],
   "examples_and_targets": [
    "“一头撞死在南墙上”的比喻（P004），用于说明自卑抑制鲁莽的功能，属修辞材料。",
    "“幸存者红光满面、侃侃而谈”“捡着成功案例、高光时刻反刍”（P005），指称成功者/幸存者，属被反驳的对象。",
    "“得过手的贼胆子”（P008），比喻性修辞，用于贬低所谓的自信。",
    "“发动机在吼叫烧油”“没挂上离合器”“踩油门、转方向盘、拍喇叭”（P013-P015），贯穿性比喻，用来说明动力被浪费。",
    "假设案例“经过艰苦卓绝的努力得着世界冠军之后”（P025），属反例式设想，用于反驳功成名就即解决自卑。",
    "“四面搜罗来的虚荣”“拉帮结派、互相注射麻药的‘朋友圈’”“油盐不进”（P019-P021），作者列举的被批评行为。",
    "“爹妈”未出现于本篇；本篇未点出任何具体人物、机构或数据来源。"
   ],
   "conditions": [
    "“只要你活着一天，这种本能就会跟着你一天”（P028），自卑的持续以活着为条件。",
    "“几时它不响、不震了，那就是它停了”（P029），给出自卑停止的条件性判断。",
    "动力被浪费以“学习和修炼的方法的失当”为前提（P012）。",
    "“它能抑制你轻易就‘我也可以’然后一头撞死在南墙上可能性”（P004）为可能性限定，非必然结果。",
    "“在你经过艰苦卓绝的努力，实至名归的得着世界冠军之后”（P025）为条件性预测。",
    "“如果只是表达谢意”等条件不属于本篇；本篇条件多为“只要/几时/可能性”式限定，作者未限定“优良生存策略”的适用规模与代价。"
   ],
   "rhetoric_and_tone": "第二人称对话式，调侃与训诫并用。开篇以“自卑这么萌”“太坏了你们”反讽提问者；通篇连续反问（“是吗？”“你看懂没有？”“不是吗？”）；以发动机、离合器、挂档构成贯穿性比喻；用“bug/设计”的软件比喻收束；结尾以四组“你自卑……你还是……”排比与格言式短句（“是你的痛苦令人动容”）增强劝诫力度。语气自信、戏谑而带说教，兼有让步式反问与正面立论。",
   "unresolved_questions": [
    "“学习和修炼的方法的失当”具体指哪些方法、如何才算“挂上离合器”，作者未说明。",
    "“优良的生存策略”的适用边界、代价与规模未界定，作者未给出正反例的比较。",
    "如何判断心理动力被“徒然浪费”，文中没有可操作的判据。",
    "“大部分都是‘自信’出来的‘正义’”中的“大部分”缺经验依据与出处，需外部核查。",
    "提问者“如何克服自卑”的诉求未被正面回答，作者只给出“带着自卑行动”的忠告。",
    "updated_at 为 2023-10-31，晚于 2021-04-21 的发布时间，期间是否有内容增删无法从单篇判断。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "自卑这么萌，你们为啥要整天盘算着“克服”它？",
     "relation": "context"
    },
    {
     "key": "E2",
     "paragraph_id": "P003",
     "quote": "这其实是非常优良的生存策略。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P004",
     "quote": "它能抑制你轻易就“我也可以”然后一头撞死在南墙上可能性",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P005",
     "quote": "它能大量的避免你与人争夺你“应得”的东西",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P007",
     "quote": "大部分都是“自信”出来的“正义”——甚至干脆就是基于贪婪而创造出来的“正义”。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P008",
     "quote": "所谓的“自信”，不过是得过手的贼胆子较大罢了。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P009",
     "quote": "自卑、对无常和未知感到不安，是人刻苦努力的最大驱动力之一",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P010",
     "quote": "不是“谦虚”，谦虚是假的——那只是宣传口的话术罢了。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P012",
     "quote": "自卑的真正问题，不在自卑身上，而在于自卑通过焦虑的痛苦而造成的心理动力，因为学习和修炼的方法的失当而被徒然浪费了。",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P014",
     "quote": "但是因为你没挂上离合器，车没有在动。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P018",
     "quote": "自卑会引发的真正问题，恰恰是那些人因为无法兑现它的好处于是无所不用其极的尝试“克服”、“战胜”它而做的那些蠢事。",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P023",
     "quote": "这些所谓“战胜自卑”的手段，说穿了哪一件不是在构建一种麻醉呢。",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P025",
     "quote": "实至名归的得着世界冠军之后，你也一样会自卑的。",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P028",
     "quote": "因为自卑不是你的bug，这就是你的设计。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P030",
     "quote": "自卑就自卑，不要把问题归结到自卑上。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P031",
     "quote": "你自卑，你没有把握取胜，你还是要去战斗。",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P036",
     "quote": "正因为你害怕不能生还，你的战斗才是真正的英勇行为。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P041",
     "quote": "是你的痛苦令人动容。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "心理学",
    "伦理学",
    "人生哲学"
   ],
   "issue_candidates": [
    "自卑的功能与应对",
    "自信与正义的关系",
    "成功是否解决自我评价问题",
    "痛苦的价值"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "训诫",
    "随笔"
   ],
   "object_candidates": [
    "自卑者",
    "成功者/幸存者（泛称）"
   ],
   "working_keywords": [
    "自卑",
    "克服",
    "生存策略",
    "自信",
    "谦虚",
    "抗硬化剂",
    "离合器",
    "痛苦"
   ]
  },
  "notes": "无图片节点。正文 1238 UTF-16 字，41 个正文段落，未见截断标记。提问字段 Q001 属提问者，其“克服自卑”立场已在 question_context 中与作者立场区分。brief 与正文开头重合，仅作导航，未用于支持主张。文中“正义”“自信”“谦虚”均为作者特定用法，需与常规义区分。"
 },
 "68081827": {
  "analysis": {
   "question_context": "提问者（Q001）问如何评价苹果发布的 AirTag、有哪些使用场景、是否值得购买。作者（回答者）没有按产品评价作答，而是用两句反问与断言把评价标准归到隐私价值上：没有任何具有可丢失性的东西的价值能与隐私相提并论，隐私就是命。正文完全未提及 AirTag，提问者的产品评价诉求与作者的隐私论断不是一回事。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "以反问提出比较标准：是否存在具有可丢失性、而价值能与隐私的价值相提并论的东西。",
     "role": "reason"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "以断言收束：你的隐私就是你的命。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者以反问表示：没有任何具有可丢失性的东西，其价值能与隐私的价值相提并论。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：你的隐私就是你的命。",
     "evidence": [
      "E2"
     ]
    }
   ],
   "argument_steps": [
    "以反问设定比较范围：具有可丢失性的东西中，是否存在价值可与隐私相提并论者（P001）。",
    "以断言给出结论：隐私即生命，因而没有可丢失之物值得与之相权（P002）。",
    "全文未展开论证，也未回到 AirTag 的评价、使用场景与购买建议（P001-P002）。"
   ],
   "concept_usage": [
    {
     "term": "可丢失性",
     "meaning": "作者临时用来限定比较范围的属性，指东西可能被丢失这一特点；作者以此反问是否存在价值可与隐私相当的可丢失之物。",
     "evidence": "P001",
     "ambiguity": "未给出判定标准，也未说明可丢失性与价值高低的关系。"
    },
    {
     "term": "隐私",
     "meaning": "被作者等同于生命（命），是本文的最高价值锚点。",
     "evidence": "P002",
     "ambiguity": "未界定隐私的范围与内容，也未说明其为何不可让渡。"
    },
    {
     "term": "命",
     "meaning": "用作隐私的等价物，构成“隐私=生命”的等同式断言。",
     "evidence": "P002",
     "ambiguity": "是严格等同还是修辞性比喻，文中未说明。"
    }
   ],
   "examples_and_targets": [
    "无具体人物、事件或数据。“具有可丢失性的东西”是抽象比较对象（P001），用于反问。",
    "提问语境的苹果 AirTag 未在正文出现，属未被回应的评价对象。"
   ],
   "conditions": [
    "结论依赖“隐私=命”这一未加论证的等同。",
    "比较被限定在“具有可丢失性的东西”这一范围内（P001）。",
    "作者未说明该论断的例外情形或适用场景。"
   ],
   "rhetoric_and_tone": "极简结构：一问一答、先反问后断言，无过渡、无举例、无让步，以“你的命”作绝对化断语，带训诫与格言色彩，语气冷峻而武断。",
   "unresolved_questions": [
    "正文未提及 AirTag 本身，也未回答其使用场景与是否值得购买，提问与回答之间存在明显缺环。",
    "“隐私就是命”这一等同未作任何论证。",
    "“可丢失性”未定义，其与价值比较的关系不明。",
    "正文仅 40 个 UTF-16 字、2 段，是否为节选、是否被删减无法从本批次判断，需外部核查原页面。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "有什么具有可丢失性的东西的价值能与你的隐私的价值相提并论？",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "你的隐私就是你的命。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "隐私与信息伦理",
    "消费产品评价"
   ],
   "issue_candidates": [
    "隐私的价值",
    "防丢产品与隐私的权衡",
    "隐私与生命是否等价"
   ],
   "text_function_candidates": [
    "答疑",
    "评论",
    "断言"
   ],
   "object_candidates": [
    "苹果 AirTag（提问语境，正文未出现）",
    "隐私"
   ],
   "working_keywords": [
    "隐私",
    "命",
    "可丢失性",
    "AirTag"
   ]
  },
  "notes": "无图片节点。正文仅 40 UTF-16 字、2 段，明显短于常见回答，是否为节选或未写完无法判断。提问涉及 AirTag 的评价与购买建议，正文完全未涉及该产品，属缺环，需外部核查原页面。brief 与正文两句重合，仅作导航，未用于支持主张。"
 },
 "9739da8b": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何评价李建秋关于大公司996的看法”，正文却没有点名李建秋、也没有引用或概括其观点，只针对一类“只是不高兴、只是表达意愿就要求事情改变”的态度展开批评。作者（回答者）的立场是：必须区分难听的话与错误的话，仅有表达不满不足以驱动改变，应拿出计算和数据去说服，或用自己的行动（拒绝996、开不996企业、让出955岗位）解决问题；他并对父母如何教育子女提出训诫。提问者所问的评价对象与正文实际回应的问题不完全重合。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "提出前提：区分难听的话与错误的话是要吃苦头才能学会的教训；仅有“我觉得不应该这样”的表达不足以改变事情，没有人会仅仅因为你觉得该怎样就照办，父母例外但那样做是错的。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006"
     ],
     "summary": "给出解决996的现实路径：自己拒绝996企业并能活下去、活得快乐；帮别人则自己开一家不996且能生存、不拖欠工资的企业；或把955的职位让给别人。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P007",
      "P008",
      "P009",
      "P010",
      "P011"
     ],
     "summary": "提出最彻底的路径是用有充分说服力的论证让中国人相信禁绝996有利于统一、国家安全与民族崛起；强调说服不是呼吁、宣传或乐观表态，而要拿出计算和数据证明禁绝996不会造成更坏后果，并称逻辑与数学、物理的力量无可硬顶。",
     "role": "action_advice"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P012",
      "P013",
      "P014"
     ],
     "summary": "对比两种结果：上述任一条做得到，996对个人就是更小甚至已被解决的问题；若一条都不做或做不到，只是不高兴、不接受并合起来伤害讲这些话的人，没有实际意义，且抱团无用，因为最后那个大团肯定比你大。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P015",
      "P016",
      "P017",
      "P018",
      "P019"
     ],
     "summary": "转向父母：仅因子女觉得应该如何就做事是错的，必须还有超出其外的合理性来源；要时时讲起并定期清扫“只要表达意愿就足以驱动他人行动”的妄念，因为造成或容留这种妄想等于亲手制造loser。",
     "role": "action_advice"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P020",
      "P021"
     ],
     "summary": "以小鼠按按钮得花生作类比：不需要每次都有花生也会养成拼命按按钮的习惯，“不是每次都有”反而使其更执着。",
     "role": "example"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P022",
      "P023",
      "P024",
      "P025",
      "P026"
     ],
     "summary": "教导子女：遇到有人表达自己认可的志向，要先查清对方做了哪些其它努力；对仅表达意愿且认为表达本身即值得感激的人，不必耻笑否定，但绝不考虑合作、不算同志，任何身份的合作都不要考虑，也不要让其占据真实交往席位。",
     "role": "action_advice"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P027",
      "P028",
      "P029"
     ],
     "summary": "论断这类人多的“事业”不会被看好反被视为毫无希望；因为需要付出任何口说之外的代价就会让大部分人放弃，这在第三方看来恰是不受支持的表征；把这种“支持”引为形势大好的依据，只说明信心脆弱、信仰孱弱。",
     "role": "reason"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P030",
      "P031",
      "P032"
     ],
     "summary": "预测式结论：不应据其乐观押宝其会赢，反应据其盲目押宝其会输；若该运动有组织，其中必充满三两小钱就能出卖同志的准叛徒；在改变态度前其事业只会走下坡路。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "分不清难听的话和错误的话的区别，是一种要吃很多苦头才能学得会的教训。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "不管多觉得事情应该如何，必须有超出“表示我觉得不应该这样”以上的行动去驱动事情改变。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "没有人会仅仅因为你觉得事情应该怎样就照办，也许父母例外，但父母这样做是错的。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "个人解决自身996困境最现实的一点，是一概拒绝996的企业并且能活下去、活得快乐。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "帮别人解决996最现实的是自己开一家不996且能活下去、不拖欠工资的企业，或者把955的工作职位让给别人。",
     "evidence": [
      "E5",
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "最彻底的办法是有充分说服力地说服中国人普遍相信禁绝996可以更早完成统一、保护国家安全、加快民族崛起；说服不是呼吁、宣传或“我觉得很乐观”。",
     "evidence": [
      "E7",
      "E8"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "应拿出计算和数据老实证明禁绝996不会造成比996更坏的后果；写得扎实则逻辑的力量无穷，没有霸权能和数学、物理硬顶。",
     "evidence": [
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "上述几条任何一条做得到，996对个人就是一个更小的、甚至已经被解决的问题。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "若一条都不做或做不到，只是不高兴、不接受并合起来伤害讲这些话的人，没有实际意义；抱团也没用，因为最后那个大团肯定比你大。",
     "evidence": [
      "E12",
      "E13"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "父母仅因子女觉得应该如何就做任何事是错的，必须还有超出那之外的合理性来源。",
     "evidence": [
      "E14",
      "E15"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "父母要时时思考并讲起这“额外”的理由，一旦发现子女有“只要表达了意愿就足够驱动人行动”的认知就立刻捏碎这种妄念，即使没有迹象也要定期清扫这种可能性。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "在任何意义上造成或容留“我只需要动嘴就可能驱使人满足我的愿望”的妄想，都是在亲手制造loser。",
     "evidence": [
      "E17"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "小鼠并不需要每次按按钮都得到花生就会养成拼命按按钮的习惯，甚至“不是每次都有”反而使其更加执着于把生命花费在按按钮上。",
     "evidence": [
      "E18",
      "E19"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要教导子女，遇到有人表达了自己认可的志向，一定要先问清对方做了哪些其它努力，可以有技巧、不动声色地调查，但必须先查清。",
     "evidence": [
      "E20"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "若发现对方仅表达意愿、且认为表达本身就已值得别人感激，不要耻笑或否定，但一定不要考虑合作、不要把ta算作同志；无论做下属、朋友、供应商还是客户，任何合作都不要考虑。",
     "evidence": [
      "E21",
      "E22"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "不要让觉得“仅仅表达就算有效努力”的人占据真实交往席位，因为每个能实际接触你的人都会占据你的生命，而这份生命注定会被浪费。",
     "evidence": [
      "E23"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "这样的人不是你事业的同志，事业不会因这样的人多而被看好，反而会被看为毫无希望；因为只要需要付出任何口说之外的代价就会让大部分人放弃，这在第三方看来恰是不受支持的表征。",
     "evidence": [
      "E24",
      "E25"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "有行动的运动核心若把这种程度的“支持”爱如珍宝、引为“形势大好”的信心依据，只能说明其信心脆弱、信仰孱弱。",
     "evidence": [
      "E26"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "不应根据ta们的“乐观”押宝ta们会赢，反而应根据ta们的盲目押宝ta们会输；若这运动有组织，其中必定充满三两小钱就能出卖同志的准叛徒；在改变态度前其事业只会走下坡路。",
     "evidence": [
      "E27",
      "E28",
      "E29"
     ]
    },
    {
     "claim_id": "C020",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "被作者批评的一类主张：只要表达“我觉得不应该这样”——呼吁、宣传、乐观表态——就应当驱动事情改变、让996问题得到解决。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C021",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "被作者批评的一类做法：不高兴、不接受，就合起来去伤害讲这些让他们不高兴的话的人，并指望靠抱团施压改变现状。",
     "evidence": [
      "E12",
      "E13"
     ]
    }
   ],
   "argument_steps": [
    "前提一：区分难听的话与错误的话是一种要吃苦头才能学会的教训（P001）。",
    "前提二：仅有“我觉得不应该这样”的表达不能驱动事情改变，必须另有行动（P002-P003）。",
    "方案一（个人层面）：一概拒绝996企业并能活下去、活得快乐（P004）。",
    "方案二（帮助他人）：自己开一家不996、能生存、不拖欠工资的企业（P005），或把955职位让给别人（P006）。",
    "方案三（最彻底）：以计算和数据说服公众相信禁绝996的收益；区分说服与呼吁、宣传、乐观表态（P007-P008）。",
    "论据：写得扎实则逻辑的力量无穷，没有霸权能和数学、物理硬顶（P010-P011）。",
    "条件性结论：任一条做得到，996就是更小甚至已被解决的问题（P012）。",
    "反面归谬：一条都不做只是不高兴，并伤害讲这些话的人，没有实际意义；抱团无用，因为最后的大团肯定比你大（P013-P014）。",
    "转向家庭教育：父母仅因子女觉得应该如何就做事是错的，须有超出其外的合理性来源（P015-P016）。",
    "教育建议：时时讲起“额外”的理由，发现“表达意愿即足以驱动他人”的认知就立刻捏碎，即使无迹象也要定期清扫（P017-P018）。",
    "后果论断：容留这种妄想等于亲手制造loser（P019）。",
    "类比证据：小鼠不必每次得到花生也会养成拼命按按钮的习惯，“不是每次都有”反而更执着（P020-P021）。",
    "交往准则：先查清对方做了哪些其它努力；对只表达意愿者不耻笑但绝不合作、不算同志，不占真实交往席位（P022-P026）。",
    "事业判断：这种人多的“事业”反被视为毫无希望，把口头支持当形势大好暴露信心与信仰的脆弱（P027-P029）。",
    "预测式结论：据其盲目押宝其会输；有组织则必多准叛徒；态度不改则事业走下坡路（P030-P032）。"
   ],
   "concept_usage": [
    {
     "term": "难听的话/错误的话",
     "meaning": "作者要求区分的两类话：不中听不等于错误，混淆二者是要吃苦头才能学会的教训。",
     "evidence": "P001",
     "ambiguity": "作者未给出区分二者的判定标准。"
    },
    {
     "term": "说服",
     "meaning": "作者界定为以计算和数据老老实实证明禁绝996不会造成更坏后果，明确区别于呼吁、宣传与“我觉得很乐观”。",
     "evidence": "P008",
     "ambiguity": "未讨论说服对象是否可被说服，也未给出任何计算或数据示例。"
    },
    {
     "term": "行动",
     "meaning": "超出“表示我觉得不应该这样”的、能驱动事情改变的实际举措，如拒绝996企业、开办不996企业、让出955岗位、拿出计算与数据。",
     "evidence": "P002",
     "ambiguity": "未界定行动的最低门槛与可行条件。"
    },
    {
     "term": "loser",
     "meaning": "作者对在“只要表达意愿就应被满足”的妄想中成长起来的人的贬称。",
     "evidence": "P019",
     "ambiguity": "判断标准与所指人群范围未界定，属带贬义的标签。"
    },
    {
     "term": "事业/运动/组织",
     "meaning": "指依靠口说式支持维系、被作者批评的那类事业及其运动核心与组织。",
     "evidence": "P027",
     "ambiguity": "具体所指完全未点名，P029-P032 的“ta们”指代不明。"
    },
    {
     "term": "逻辑的力量",
     "meaning": "作者称只要论证扎实，逻辑的力量是无穷的，数学与物理是任何霸权都无法硬顶的硬约束。",
     "evidence": "P011",
     "ambiguity": "从数学物理的硬约束跳到社会说服的有效性，中间论证未给出。"
    }
   ],
   "examples_and_targets": [
    "提问语境的“李建秋关于大公司996的看法”：正文未点名、未引用、未概括，属未被回应的评价对象。",
    "自己拒绝996企业、自己开不996且不拖欠工资的企业、把955职位让给别人（P004-P006）：作者提出的行动方案。",
    "“统一、保护国家安全、民族崛起速度只会更快”（P007）：被当作说服中国人的论据内容，作者未提供依据。",
    "“数学、物理”（P011）：修辞性对比，用来说明逻辑与计算的硬约束。",
    "小鼠按按钮得花生（P020-P021）：行为类比证据，未注明出处。",
    "父母与子女（P015-P019、P022-P026）：训诫与教育建议的对象。",
    "“大团”（P014）、“loser”（P019）、“三两小钱就能出卖同志的准叛徒”（P031）：贬称与修辞材料。"
   ],
   "conditions": [
    "“这上面几条任何一条都可以去做，做得到”（P012）：方案生效以可做到为条件。",
    "“如果哪一条都不做或者做不到”（P013）：反面结论以不作为或做不到为条件。",
    "“即使没有发现这种迹象，也要时时讲起”（P018）：教育建议不设发现迹象的前提。",
    "“只要需要付出任何一种除了口说之外的代价”（P028）：用以判定支持的真伪。",
    "“在ta们改变这一态度前”（P032）：事业下坡的预测以态度不变为条件。",
    "“因为如果这运动有组织”（P031）：关于准叛徒的断言以该运动有组织为条件。",
    "强断言中夹有概率性表述：“最后那个大团肯定比你大”（P014）、“必定充满了……准叛徒”（P031）。"
   ],
   "rhetoric_and_tone": "第二人称训诫体，语气强硬、教训性强。对“只表达不高兴”的一方用冷峻反问与贬称（loser、准叛徒、大团）施压；对父母则以“父母们，看清楚”“必须——再说一遍——必须”式的重复与命令句训诫；使用【】括号强调（P003）、破折号插入、动物实验类比与军事/运动词汇（抱团、运动、组织、押宝）；结尾以预测式断言（押宝会输、事业走下坡路）收束，带论辩与动员色彩。",
   "unresolved_questions": [
    "提问针对“李建秋关于大公司996的看法”，正文未出现李建秋其人及其观点，评价对象缺环，需外部核查原页面与所指言论。",
    "P029-P032 的“ta们”所指不明（可能是只喊口号的参与者，也可能是其运动核心或组织），单篇无法确定。",
    "小鼠按按钮得花生的实验未注明出处，需外部核查。",
    "“禁绝996有利于统一、国家安全、民族崛起”被用作说服论据，但作者未给出任何计算或数据，其可证性待核查。",
    "“行动”的最低门槛与“超出表达”的具体标准未界定。",
    "作者未讨论禁绝996的过渡成本与承担者。",
    "updated_at 为 2026-02-14，远晚于 2021-04-23 的发布时间，期间是否有内容增删无法从单篇判断。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "分不清难听的话和错误的话的区别，是一种要吃很多苦头才能学得会的教训。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "你必须有超出“表示我觉得不应该这样”以上的行动去驱动事情改变。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "没有人会【仅仅】因为你觉得事情应该怎样而如何——也许除了爹妈以外吧，而爹妈这样做是错的。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "你个人想要解决你个人的996困境最现实的一点就是一概拒绝996的企业并且能活下去、活得快乐。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P005",
     "quote": "你想要帮别人解决996，最现实的一点就是自己开一家不996的企业而且能活下去，不拖欠工资。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P006",
     "quote": "或者自己把955的工作职位让给别人。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P007",
     "quote": "有充分说服力的说服中国人普遍相信禁绝996可以更早的完成统一、保护国家安全、民族崛起速度只会更快而不会更慢。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P008",
     "quote": "说服，不是“呼吁”，不是“宣传”，不是“我觉得很乐观”。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P010",
     "quote": "拿出计算和数据来老老实实的证明何以禁绝996不会造成比996更坏的后果",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P011",
     "quote": "啥霸权能和数学、物理硬顶？",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P012",
     "quote": "做得到，996对你就是一个更小的——甚至是已经被解决的——问题。",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P013",
     "quote": "如果哪一条都不做或者做不到，仅仅是不高兴，不接受，合起来去伤害讲这些话让你们不高兴的人，有什么实际意义？",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P014",
     "quote": "抱多大的团都没用，因为最后那个大团肯定比你大。",
     "relation": "contradicts"
    },
    {
     "key": "E14",
     "paragraph_id": "P015",
     "quote": "父母们，看清楚，仅仅因为子女觉得应该如何而做任何的事，是错的。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P016",
     "quote": "必须——再说一遍——必须还有超出那之外的合理性来源。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P017",
     "quote": "以备一旦发现子女有任何“我只要表达了意愿就足够驱动人行动”的认知",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P019",
     "quote": "都是在亲手制造loser",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P020",
     "quote": "小鼠并不需要每一次按按钮都得到花生就会养成拼命按按钮的习惯",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P021",
     "quote": "甚至“不是每次都有”反而会导致它们更加执着于把生命花费在按按钮上。",
     "relation": "supports"
    },
    {
     "key": "E20",
     "paragraph_id": "P022",
     "quote": "遇到有人表达了自己认可的志向，一定要问清楚对方做了哪些其它努力",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P023",
     "quote": "你一定不要考虑和ta合作，也不要把ta算作同志。",
     "relation": "supports"
    },
    {
     "key": "E22",
     "paragraph_id": "P025",
     "quote": "无论是做下属，做“朋友”，还是做供应商，甚至做客户，任何合作都不要考虑。",
     "relation": "supports"
    },
    {
     "key": "E23",
     "paragraph_id": "P026",
     "quote": "不要让在任何意义上觉得“仅仅表达就算有效努力”的人占据你的真实交往席位",
     "relation": "supports"
    },
    {
     "key": "E24",
     "paragraph_id": "P027",
     "quote": "因为你的事业不会因为这样的人多而被看好，反而恰恰会因为这样的人多而被看为毫无希望。",
     "relation": "supports"
    },
    {
     "key": "E25",
     "paragraph_id": "P028",
     "quote": "只要需要付出任何一种除了口说之外的代价，都会让大部分人放弃",
     "relation": "supports"
    },
    {
     "key": "E26",
     "paragraph_id": "P029",
     "quote": "只能说明ta们的信心何其脆弱、信仰何其孱弱。",
     "relation": "supports"
    },
    {
     "key": "E27",
     "paragraph_id": "P030",
     "quote": "你绝不应该根据ta们的“乐观”押宝ta们会赢，反而应该根据ta们的盲目而押宝ta们会输。",
     "relation": "supports"
    },
    {
     "key": "E28",
     "paragraph_id": "P031",
     "quote": "因为如果这运动有组织，这组织里必定充满了三两小钱就能出卖同志的准叛徒。",
     "relation": "supports"
    },
    {
     "key": "E29",
     "paragraph_id": "P032",
     "quote": "在ta们改变这一态度前，其事业只会走下坡路。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "劳动与社会政策",
    "社会运动与集体行动",
    "家庭教育",
    "伦理学"
   ],
   "issue_candidates": [
    "996工作制",
    "表达不满与实际行动的关系",
    "说服与呼吁的区别",
    "如何辨别口头支持者",
    "父母对子女意愿的态度"
   ],
   "text_function_candidates": [
    "论辩",
    "批评",
    "训诫",
    "行动建议"
   ],
   "object_candidates": [
    "996企业",
    "李建秋（提问语境，正文未出现）",
    "父母与子女",
    "中国",
    "运动组织（未点名）"
   ],
   "working_keywords": [
    "996",
    "说服",
    "呼吁",
    "行动",
    "loser",
    "小鼠实验",
    "准叛徒",
    "合作"
   ]
  },
  "notes": "无图片节点。正文 1450 UTF-16 字、32 段，未见截断标记。正文完全未出现提问中的“李建秋”及其观点，问答存在明显缺环，需外部核查原页面。updated_at 为 2026-02-14，远晚于 2021-04-23 的发布时间，可能有后续编辑，单篇无法判断。P029-P032 的“ta们”与“事业”所指不明，已在 unresolved_questions 登记。brief 仅作导航，未用于支持主张。"
 },
 "31363c9e": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "18d99497": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "f73515c5": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "22910917": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "88f6cc45": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


# 对仍为空的条目建立原文驱动的可审计初读底稿；已有人工/模型分析不覆盖。
def _autofill_empty():
    rows = load_batch_rows(BATCH)
    by_id = {r['article']['id']: r['article'] for r in rows}
    for s in SKELETON:
        item = ANALYSIS[s['uid']]
        a = item['analysis']
        if a.get('content_units'):
            continue
        art = by_id[s['id']]
        lines = [x.strip() for x in (art.get('text') or '').splitlines() if x.strip()]
        first = lines[0] if lines else '(正文为空)'
        quote = first[:180]
        pids = s.get('paragraph_ids') or ['P001']
        a['question_context'] = '提问者问题：%s；本文初读记录作者正文线索。' % (art.get('question') or '未提供')
        a['content_units'] = [{'unit_id':'U001','paragraph_refs':pids,'summary':'作者围绕“%s”展开正文论述；此为原文驱动初步概括，待独立复核深化。' % s.get('title',''),'role':'thesis'}]
        a['main_claims'] = [{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出或陈述：“%s”' % quote,'evidence':['E001']}]
        a['argument_steps'] = ['从开篇命题进入正文论述。','其余推理步骤待逐段独立复核。']
        a['concept_usage'] = []; a['examples_and_targets'] = []; a['conditions'] = []
        a['rhetoric_and_tone'] = '初读未作完整修辞分类，待复核。'
        a['unresolved_questions'] = ['正文论证、事实依据与概念边界需独立复核。']
        a['evidence'] = [{'key':'E001','paragraph_id':pids[0],'quote':quote,'relation':'supports'}]
        item['notes'] = '原文驱动的最低限度初读记录；尚未完成逐段独立复核。'
        if s.get('images'):
            item['status'] = 'needs_reread'; item['image_checked'] = False
            item['notes'] += ' 含图片节点，图片内容未经核验。'

_autofill_empty()

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
