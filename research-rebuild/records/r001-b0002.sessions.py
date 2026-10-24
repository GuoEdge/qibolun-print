# -*- coding: utf-8 -*-
"""批次 r001-b0002 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0002.sessions.py            # 写 out/r001-b0002.out.jsonl
  python3 records/r001-b0002.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0002"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0002.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "af9e0837": {
  "analysis": {
   "question_context": "提问者问动物（不包括人）是否需要掏耳朵（Q001）。作者先给出“一般不需要”的结论，再从演化压力、动物对耳道寄生虫的三种应对、幼崽与衰老期动物的例外、清洁耳道所需代价，以及人类采耳技术的意义逐层解释；末段附平台话题标签“科学答集”。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "直接回答提问：一般不需要。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "给出演化前提：耳道寄生虫是动物相当主要的死因，但这类死亡多不在繁殖完成前发生，故未形成足够演化压力被淘汰出基因池；并列举动物的三种应对（发达的耳毛、猛烈的摇头、快速分泌的耳蜡）。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "说明前两种应对足以抵御大型寄生物，耳蜡专门抵御微型寄生虫（耳螨）；并称健康且代谢旺盛的动物几乎总能直接抵抗耳螨。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "指出例外与后果：幼崽极早期感染、以及衰老期或食物匮乏导致低代谢的个体，可能被耳螨爆发性增殖所害，感染几乎必然恶化并致死；作者并推论许多老年动物的野外死亡实为这类疾病，附食腐习性与《利未记》引文的旁注。",
     "role": "qualification"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "说明清洁耳道本可为生存优势，但发育出足以深入耳道抓挠的手指会带来新问题，且耳鼓不坚固使抓挠风险更大。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P006"
     ],
     "summary": "以人类为例：很晚近的年代耳道感染仍相当严重，但人类很早掌握采耳、药水灌耳、滴蜡、油洗等技术；因繁殖期晚、幼崽期长，人类比动物更需要学会掏耳朵。",
     "role": "conclusion"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "文末“科学答集”为平台话题标签，未被 lexical 结构覆盖。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者回答提问：动物一般不需要掏耳朵。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称耳道寄生虫是动物相当主要的死因，但因这种死亡往往不能在动物完成繁殖前发生，故一直没有形成足够的演化压力将其排除出基因池。",
     "evidence": [
      "E2",
      "E3"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称大多数动物针对耳道寄生虫主要发展出三种应对：发达的耳毛、足以靠离心力甩出较大异物的猛烈摇头、以及快速分泌以抵抗微型生物噬咬的耳蜡。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者以“如果耳蜡分泌足够快”为条件，称能使寄生到耳道的微小寄生虫只能啃到性质极其稳定的生物蜡，从而无法获得可赖以生存的能量；并据此称健康且代谢旺盛的动物几乎总是可以直接抵抗耳螨。",
     "evidence": [
      "E5",
      "E6"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为问题出在幼崽和衰老期的动物身上：幼崽耳道皮肤高度裸露使耳螨可以吃到血肉而爆发性增殖，老年或低代谢个体则可能被耳螨咬穿耳蜡获得营养。",
     "evidence": [
      "E7",
      "E8"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称很多看似被猛兽捕获、跌落山崖或溺亡的老年动物，事实上是死于这类耳道疾病。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称动物若能清洁耳道会是特殊的生存优势，但发育出深入耳道抓挠的手指要么要求手指很细、要么要求耳孔很大，且几乎所有陆生动物耳鼓都不坚固，抓挠可致听力障碍甚至开放伤口，后者比长期携带耳螨虫卵更危险。",
     "evidence": [
      "E10",
      "E11"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "quoted_or_cited",
     "attribution": "cited_source",
     "modality": "asserted",
     "statement": "作者引《利未记》7:24（和合本）规定自死的和被野兽撕裂的动物脂油可作别的使用但不可吃，用以旁证捕食者不愿取食病死动物。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称人类直到很晚近的年代，因缺少卫生意识，中耳炎之类的耳道感染仍是相当严重的问题。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称人类很早就学会采耳、药水灌耳、滴蜡、油洗等医疗技术，不太会让感染发展到入侵大脑的严重程度。",
     "evidence": [
      "E14"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者结论：人类的确要比动物更需要学会掏耳朵的技能，理由是人类的繁殖期相对来说过于晚了，而幼崽期又过长。",
     "evidence": [
      "E15"
     ]
    }
   ],
   "argument_steps": [
    "先给出结论“一般不需要”（P001）。",
    "补上演化前提：耳道寄生虫致死多发生在繁殖完成之后，故未形成淘汰压力（P002）。",
    "列举动物针对耳道寄生虫的三种应对方式（P002）。",
    "分别说明前两种应对抵御大型寄生物、耳蜡抵御微型寄生虫，得出健康且代谢旺盛的动物几乎总能抵抗耳螨（P003）。",
    "指出例外：幼崽与衰老期/低代谢个体，并推论其感染后果与野外死亡归因（P004）。",
    "说明动物自行清洁耳道所需付出的形态与听觉代价（P005）。",
    "以人类的耳道感染史与采耳技术作对照，收束为“人类比动物更需要学会掏耳朵”（P006）。"
   ],
   "concept_usage": [
    {
     "term": "演化压力",
     "meaning": "作者指因耳道寄生虫致死通常不发生在繁殖完成之前，该死亡未能成为把相关性状淘汰出基因池的选择压力。",
     "evidence": "P002",
     "ambiguity": "未给出量化或机制细节。"
    },
    {
     "term": "耳蜡",
     "meaning": "动物快速分泌的蜡质，性质极其稳定，使微型寄生虫无法将其分解为可赖以生存的能量。",
     "evidence": "P003",
     "ambiguity": "未说明不同物种间的差异。"
    },
    {
     "term": "代谢旺盛/较低的代谢水平",
     "meaning": "作者用来区分能抵抗耳螨的健康动物与易感的幼崽、衰老或食物匮乏个体。",
     "evidence": "P003、P004",
     "ambiguity": "未给出判定标准或阈值。"
    },
    {
     "term": "采耳",
     "meaning": "人类早期掌握的耳道清理与治疗技术之一，与药水灌耳、滴蜡、油洗并列。",
     "evidence": "P006",
     "ambiguity": "未说明具体年代、地域与有效性。"
    }
   ],
   "examples_and_targets": [
    "例证：耳螨作为不能靠摇头和耳毛抵御的微型寄生虫（P003）。",
    "修辞性描写：猫狗摇头时耳朵拍打脸颊发出啪啪啪的脆响（P002）。",
    "例证：捕食者不愿取食病死在原地的动物，“专业”的食腐动物才有胆量取食（P004）。",
    "引用材料：《利未记》7:24（和合本）关于自死与被野兽撕裂之动物脂油的规定（P004），为作者引用的外部文本。",
    "例证：人类使用的采耳、药水灌耳、滴蜡、油洗等技术（P006）。",
    "被回应对象：提问者“动物（不包括人）需要掏耳朵吗？”（Q001）。"
   ],
   "conditions": [
    "全篇讨论对象限定为“动物（不包括人）”（Q001）。",
    "结论用“一般不需要”限定，非全称否定（P001）。",
    "耳蜡的防御作用以“如果耳蜡分泌足够快”为条件（P003）。",
    "例外条件：幼崽尚未启动耳蜡分泌的极早期；动物进入衰老期，或因食物匮乏导致身体进入较低的代谢水平（P004）。",
    "人类部分以“人类的繁殖期相对来说过于晚了，而幼崽期又过长”为结论依据（P006）。"
   ],
   "rhetoric_and_tone": "答疑式科普说明，结论先行、逐层补条件；含口语化拟声描写（“啪啪啪的脆响”）；用括号插入离题旁注并引圣经；以“事实上”“的确可以说”加强断言；末段“科学答集”为平台话题标签。",
   "unresolved_questions": [
    "“科学答集”为平台话题标签，出现在 text 末尾但不在 lexical 结构内（P007，text_tail_not_in_lexical），作者归属待核。",
    "“耳道寄生虫其实是动物的一种相当主要的死因”等断言未给出来源（待外部核查）。",
    "《利未记》引文与正文论证的关系（类比或证据）本文未说明，亦未给出处页码。",
    "作者未说明采耳等技术的年代、地域与有效性证据。",
    "文中“幼崽再还没启动耳蜡分泌的极早期”等处疑有笔误，按原文保留，未作改写。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "一般不需要。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "耳道寄生虫其实是动物的一种相当主要的死因",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P002",
     "quote": "因此一直没有形成足够的演化压力来将其排除出基因池",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P002",
     "quote": "大多数动物针对耳道寄生虫主要发展出了三种应对",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P003",
     "quote": "如果耳蜡分泌足够快，就能保证成功寄生到耳道中的微小寄生虫无尽的啃到生物蜡",
     "relation": "qualifies"
    },
    {
     "key": "E6",
     "paragraph_id": "P003",
     "quote": "因此健康且代谢旺盛的动物几乎总是可以直接抵抗耳螨。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P004",
     "quote": "问题出在幼崽和衰老期的动物身上。",
     "relation": "qualifies"
    },
    {
     "key": "E8",
     "paragraph_id": "P004",
     "quote": "因为幼崽耳道皮肤的高度裸露，耳螨可以轻易吃到血肉，因此会爆发性的增殖",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P004",
     "quote": "事实上是死于这类疾病",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P005",
     "quote": "动物如果能够做到清洁耳道，会是它们一个特殊的生存优势。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P005",
     "quote": "这甚至要比长期携带耳螨虫卵更危险",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P004",
     "quote": "自死的和被野兽撕裂的，那脂油可以做别的使用，只是你们万不可吃。",
     "relation": "context"
    },
    {
     "key": "E13",
     "paragraph_id": "P006",
     "quote": "因为缺少卫生意识，中耳炎之类的耳道感染都是一个相当严重的问题",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P006",
     "quote": "不过人类很早就学会了各种采耳，药水灌耳，滴蜡，油洗之类的医疗技术",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P006",
     "quote": "因此的确可以说人类要比动物更需要学会掏耳朵的技能",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "进化生物学",
    "动物生理学",
    "寄生虫与疾病"
   ],
   "issue_candidates": [
    "动物是否需要掏耳朵",
    "耳道寄生虫与演化压力",
    "耳蜡的防御作用",
    "人类采耳技术的意义"
   ],
   "text_function_candidates": [
    "答疑",
    "解释"
   ],
   "object_candidates": [
    "动物",
    "人类",
    "耳螨",
    "猫",
    "狗",
    "食腐动物"
   ],
   "working_keywords": [
    "耳道寄生虫",
    "耳蜡",
    "耳螨",
    "演化压力",
    "基因池",
    "采耳"
   ]
  },
  "notes": "本篇无图片节点。文末 P007“科学答集”为平台话题标签，混入 text 但未被 lexical 覆盖（text_tail_not_in_lexical），非作者正文，作者归属待核。P004 超过 300 字，记录中的段落 text 为截断样本（sample_truncated=true），完整原文可按 article_id 与字符位置回查语料。"
 },
 "3ea32315": {
  "analysis": {
   "question_context": "提问者问选育并大规模养殖无菌肉用老鼠是否会比猪肉更划算（Q001）。作者直接否定，并给出“个体越小的动物越不节能”这一理由，再以肉用家畜全为大型兽作为印证。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "直接否定提问预设：并不会。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "给出理由：个体越小的动物越不节能，所食食物热量有很高比例转化为热能散失。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "以该原理解释现实中的肉用家畜全是体型巨大的中大型兽。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否定提问预设：选育并大规模养殖无菌肉用老鼠不会比猪肉更划算。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称个体越小的动物越不节能，它们所食用的食物热量有很高比例会转化成热能散失。",
     "evidence": [
      "E2",
      "E3"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以该原理解释：这正是肉用家畜全是体型巨大的中大型兽的原因。",
     "evidence": [
      "E4"
     ]
    }
   ],
   "argument_steps": [
    "直接否定提问预设（P001）。",
    "给出一般原理：体型越小越不节能，食物热量高比例转为热能散失（P002）。",
    "以肉用家畜全为体型巨大的中大型兽作为该原理的印证并收束（P002）。"
   ],
   "concept_usage": [
    {
     "term": "节能",
     "meaning": "作者指动物所摄入食物热量中未以热能形式散失、可用于身体产出的比例；作者称该比例随体型变小而下降。",
     "evidence": "P002",
     "ambiguity": "未给出度量方式或任何数据。"
    },
    {
     "term": "无菌肉用老鼠",
     "meaning": "提问者设定的养殖方案；作者未讨论其技术细节，仅从能量利用角度回答。",
     "evidence": "Q001",
     "ambiguity": "该词仅出现于提问字段，正文未再提及。"
    },
    {
     "term": "肉用家畜",
     "meaning": "作者用以指现实中已被选择养殖的肉用动物，称其全为体型巨大的中大型兽。",
     "evidence": "P002",
     "ambiguity": "未列举具体物种。"
    }
   ],
   "examples_and_targets": [
    "例证：肉用家畜全是体型巨大的中大型兽（P002），作者用作归纳性证据。",
    "被否定对象：提问者“选育并大规模养殖无菌肉用老鼠会比猪肉更划算”的设想（Q001）。"
   ],
   "conditions": [
    "回答限于提问设定的“大规模养殖”与“比猪肉更划算”的经济比较语境（Q001）。",
    "作者只从食物热量转化比例作答，未讨论无菌养殖技术可行性、饲料种类等其他条件。"
   ],
   "rhetoric_and_tone": "极短答（正文 75 字）。先以“并不会。”一句否定，再用“其实道理很简单”引出通俗解释；断言式语气，无数据、无引文。",
   "unresolved_questions": [
    "作者未给出任何能量转化比例的数值或来源（待外部核查）。",
    "“划算”的判定标准（饲料转化率、成本或其他）本文未说明。",
    "无菌肉用老鼠的养殖方案细节与成本，本文未讨论。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "并不会。",
     "relation": "contradicts"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "其实道理很简单，个体越小的动物越不节能。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P002",
     "quote": "它们所食用的食物热量有很高的比例会转化成热能散失。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P002",
     "quote": "这也是为什么肉用家畜全是体型巨大的中大型兽的原因。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "畜牧学",
    "动物生理学",
    "农业经济"
   ],
   "issue_candidates": [
    "肉用动物体型与饲料转化效率",
    "无菌肉用老鼠养殖的可行性"
   ],
   "text_function_candidates": [
    "答疑",
    "简短否定"
   ],
   "object_candidates": [
    "老鼠",
    "猪",
    "肉用家畜"
   ],
   "working_keywords": [
    "无菌肉用老鼠",
    "节能",
    "热能散失",
    "肉用家畜"
   ]
  },
  "notes": "本篇无图片节点，正文极短（75 字符，2 段），为问答式短答，未展开论证。结论为对提问预设的否定，依据仅为“体型越小越不节能”这一断言，无数据与出处。"
 },
 "527360f8": {
  "analysis": {
   "question_context": "提问者问为什么人类生存需要的食物那么少（Q001）。作者先声明以最宽容的方式假设问题成立，把问题对象限定为青春期以后（28岁以上）的人类；随后以基础代谢下降、人类寿命远长于动物、衰老个体成为遗传累赘、种群“对爷爷们下封印”等论述解释，最后以统计口径（动物的老年个体已死、未被计入）收束。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "方法论声明：先假设问题一定成立，取最宽容、最能让问题自我成立的理解。",
     "role": "qualification"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "界定问题所指对象：很大程度上指青春期以后、年龄在28岁以上的人类。",
     "role": "definition"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "承认现象并给出直接原因：该阶段人类所需食物大为下降，因基础代谢水平大幅下降；并描述中年犯困、发胖与节食。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "提出演化理由：人类寿命相比宠物以外的动物过长；动物性成熟远早于人类，完成最初生育后基因不再关心个体健康；过于陈旧的成年个体是遗传累赘，预期寿命过长会导致“爷爷与孙子争夺地盘”的逆演化问题，对种群致命。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "推论机制：幸存种群几乎都对“爷爷们”下封印，夺走其生理优势；若青春期后相关激素仍高度活跃则极大可能催生癌症，由此反向筛选出青春期后生长激素放缓的特性，并称这是青春期现象的根源。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P006"
     ],
     "summary": "对比动物与人类：动物的“爷爷们”常被孙子夺走地盘而饿死，人类则靠孝道之类的社会规则多活好几十年，因此客观上会观察到“人类似乎比动物吃的少”的整体现象。",
     "role": "reason"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "结论：人类总体得分低，是因为动物里的“爷爷们”都死掉了，未被计入统计范围。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者声明先假设问题一定成立，即在所有可能解释中给予最宽容、最能让问题自我成立的理解。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为该问题很大程度上应指青春期以后的人类，即年龄在28岁以上的人类。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者承认这一阶段的人类确实需要的食物大为下降，因为他们的基础代谢水平大幅下降了。",
     "evidence": [
      "E3",
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者以“假设这存在一个需要解释的理由”为条件，提出人类寿命相比宠物以外的动物来说过于的长了。",
     "evidence": [
      "E5",
      "E6"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称动物的性成熟期远短于人类（人类需十几年才能生育，动物很少超过三年），且在完成最初生育后，从基因角度不再关心个体是否还需保持足够健康。",
     "evidence": [
      "E7",
      "E8"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称过于陈旧的成年个体是遗传上的累赘，预期寿命过长会出现“爷爷和孙子争夺地盘”且爷爷胜率很高的逆演化问题，这对种群而言是致命的。",
     "evidence": [
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称幸存下来的种群几乎都对“爷爷们”下了封印：既然无法剥夺其经验优势，就夺走其生理优势。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者以条件句称，如果在生理期后继续保持相关激素的高度活跃，整体发育的不平衡将会有极大可能催生癌症。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称靠着这一“铁的限制”，反向筛选出了“一旦越过青春期，所有的生长激素都会放缓”的特性，并称这是青春期现象的根源。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称动物不太需要面对这问题，因为“爷爷们”经常被孙子们夺走地盘而饿死；人类则可以靠着孝道之类的社会规则多活好几十年。",
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
     "statement": "作者称因此客观上会观察到“人类似乎比动物吃的少”这样的整体现象。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者结论：人类总体“得分”低，是因为动物里的“爷爷们”都死掉了，没有被计入统计范围。",
     "evidence": [
      "E17"
     ]
    }
   ],
   "argument_steps": [
    "先声明以最宽容的方式假设问题成立（P001）。",
    "把问题对象限定为青春期以后、28岁以上的人类（P002）。",
    "承认现象并给出直接原因：基础代谢水平大幅下降（P003）。",
    "转入演化解释：人类寿命相对动物过长，衰老个体成为遗传累赘（P004）。",
    "描述逆演化风险：“爷爷与孙子争夺地盘”的情景对种群致命（P004）。",
    "推出种群“下封印”与以癌症风险为“铁的限制”的反向筛选，得出青春期后生长激素放缓（P005）。",
    "对比动物与人类：动物的老年个体被自然淘汰，人类靠社会规则存活（P006）。",
    "收束为统计口径结论：动物的“爷爷们”已死，未被计入统计（P007）。"
   ],
   "concept_usage": [
    {
     "term": "青春期以后的人类",
     "meaning": "作者将其等同于“年龄在28岁以上的人类”，作为问题的适用范围。",
     "evidence": "P002",
     "ambiguity": "28岁这一界限本文未给出依据。"
    },
    {
     "term": "遗传上的累赘",
     "meaning": "作者指预期寿命过长、过于陈旧的成年个体对种群的遗传利益构成负担。",
     "evidence": "P004",
     "ambiguity": "未说明“累赘”的判定与度量。"
    },
    {
     "term": "逆演化",
     "meaning": "作者用以指经验占优的老年个体在与年轻个体竞争中胜率过高、从而不利于种群的情形。",
     "evidence": "P004",
     "ambiguity": "修辞性用法，未给出术语出处或形式化定义。"
    },
    {
     "term": "封印",
     "meaning": "作者对种群削弱老年个体生理优势这一筛选结果的比喻说法。",
     "evidence": "P005",
     "ambiguity": "非学术术语，含义依赖上下文。"
    },
    {
     "term": "青春期现象的根源",
     "meaning": "作者把青春期后所有生长激素放缓归因于上述反向筛选，并称之为青春期现象的根源。",
     "evidence": "P005",
     "ambiguity": "未讨论其他可能解释。"
    },
    {
     "term": "总体得分",
     "meaning": "正文只在末段出现“人类的总体得分低”，未给出定义，疑为对问题中“需要的食物少”的简称。",
     "evidence": "P007",
     "ambiguity": "该表述可能影响对结论的解释。"
    }
   ],
   "examples_and_targets": [
    "思想实验/例证：“爷爷和孙子争夺地盘，爷爷强壮程度与孙子相当，而经验有压倒优势，进而导致爷爷对孙子胜率很高”的假设情景（P004，作者引号内自设）。",
    "现象描述：中年人白天犯困、不断发胖、不得不开始节食（P003）。",
    "例证：动物里的“爷爷们”经常被孙子们夺走地盘而饿死（P006）。",
    "提及的社会规则：孝道（P006）——作者用作人类老年个体得以存活的解释因素。",
    "被回应对象：提问者“为什么人类生存需要的食物那么少？”（Q001）。"
   ],
   "conditions": [
    "以“假设问题一定成立”并取最宽容理解为全篇前提（P001）。",
    "适用范围限定为青春期以后、28岁以上的人类（P002）。",
    "解释以“假设这存在一个需要解释的理由的话”为条件（P004）。",
    "对比对象限定为“宠物以外的动物”（P004）。",
    "机制描述使用“几乎都”“极大的可能”“某种程度上”等限定词（P004、P005）。",
    "激素与癌症的关系以“如果你在生理期后继续保持相关激素的高度活跃”为条件（P005）。"
   ],
   "rhetoric_and_tone": "先作方法论让步再展开的说理文；使用“封印”“爷爷们”等拟人化比喻；以“要么……要么……”的二选一结构收束机制（P005）；“事实上，这是青春期现象的根源”为强断言；末段以统计口径作反转式结论。",
   "unresolved_questions": [
    "“28岁以上”这一具体年龄界限本文未给出依据（待外部核查）。",
    "“人类的总体得分低”中的“得分”在正文中未定义，属可能影响解释的歧义。",
    "“这是青春期现象的根源”为强断言，未给出来源（待外部核查）。",
    "作者未讨论28岁以前人类的食物需求，也未回应问题中“食物少”的其他可能解释。",
    "语料记录的 updated_at（2025-10-17）晚于 published_at（2018-07-21），但 provenance 与 superseded 均为 null，版本差异无法从本记录确认。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "我们先假设问题一定成立",
     "relation": "qualifies"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "那么这个问题很大程度上应该是指青春期以后的人类",
     "relation": "qualifies"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "这个阶段的人类的确需要的食物大为下降",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P003",
     "quote": "因为他们的基础代谢水平大幅的下降了",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P004",
     "quote": "假设这存在一个需要解释的理由的话",
     "relation": "qualifies"
    },
    {
     "key": "E6",
     "paragraph_id": "P004",
     "quote": "那么准确的说是人类的寿命相比宠物以外的动物来说过于的长了",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P004",
     "quote": "它们的性成熟期要远远的短于人类",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P004",
     "quote": "它就不太关心个体是否还需要保持足够的健康了",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P004",
     "quote": "某种程度上，过于陈旧的成年个体还是一种遗传上的累赘",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P004",
     "quote": "这个问题对于种群而言是致命的。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P005",
     "quote": "因此，幸存下来的种群几乎都对爷爷们下了封印",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P005",
     "quote": "如果你在生理期后继续保持相关激素的高度活跃，那么整体发育的不平衡将会有极大的可能催生癌症",
     "relation": "qualifies"
    },
    {
     "key": "E13",
     "paragraph_id": "P005",
     "quote": "反向筛选出了“一旦越过青春期，所有的生长激素都会放缓”的特性",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P006",
     "quote": "因为爷爷们经常被孙子们夺走地盘而饿死",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P006",
     "quote": "而人类则可以靠着孝道之类的社会规则多活好几十年",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P006",
     "quote": "这样你客观上会观察到“人类似乎比动物吃的少”这样的整体现象。",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P007",
     "quote": "是因为动物里的爷爷们都死掉了，没有被计入统计范围而已。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "进化生物学",
    "人类生理学",
    "衰老研究"
   ],
   "issue_candidates": [
    "人类食物需求随年龄下降",
    "寿命与演化压力",
    "青春期后生长激素放缓的成因",
    "比较统计的口径偏差"
   ],
   "text_function_candidates": [
    "答疑",
    "演化解释",
    "论证"
   ],
   "object_candidates": [
    "人类",
    "动物",
    "中年人",
    "老年人",
    "宠物"
   ],
   "working_keywords": [
    "基础代谢",
    "青春期",
    "生长激素",
    "逆演化",
    "遗传上的累赘",
    "孝道"
   ]
  },
  "notes": "本篇无图片节点。全文以“先假设问题成立”的让步式方法开篇，属作者自设前提，非提问者立场。updated_at（2025-10-17）明显晚于 published_at（2018-07-21），语料未提供版本差异或修订说明，仅以当前版本 text 为准。"
 },
 "6e00a9d7": {
  "analysis": {
   "question_context": "提问者问死亡如此可怕，为何全人类（或者说高层领导人）不主张把重心放在医学上（Q001）。作者先以资源与效率回答（把全部重心放在攻克死亡上会立刻导致经济崩溃），再给出替代性投入方向与优先级，最后从族群存续所需的“接纳死亡的意识形态构建”论证把攻克死亡当头等大事的危害。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "直接回答：把全部重心都放在攻克死亡上会立刻导致人类经济崩溃，因为耗尽全部资源目前也解决不了这个问题。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "提出替代方向：只有把重心放在更有效率的“让人暂时不死”和“让暂时死不了的人活得好一些”上。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "给出投资优先级判断：应“让必死的人不要那么害怕死亡”的优先级高于“让人不会死”。",
     "role": "action_advice"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "历史与族群层面的理由：过于执着于求生和恐惧死亡对族群是缺点，放大到千年尺度会难以挺过千年一遇的危机；现存所有文明社群都有接纳死亡的意识形态构建（轮回论、永生论、取义论等），否则遇到必须承受牺牲的危机会覆灭。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "结论：把“攻克死亡作为头等大事”与这种生死攸关的意识形态抵触；强行推崇的结局更可能是死亡尚未攻克，族群已因甘于牺牲的个体不足而灭亡。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者称把全部重心都放在攻克死亡上会立刻导致人类经济崩溃，因为把全部资源都耗尽，目前也解决不了这个问题。",
     "evidence": [
      "E1",
      "E2"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张我们只有把重心放在更有效率的“让人暂时不死”和“让暂时死不了的人活得好一些”上。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者进一步主张，应该“让必死的人不要那么害怕死亡”的投资优先级也要高于“让人不会死”。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称历史上经常有“因为总体过于恐惧死亡反而导致更多无谓死亡乃至于族群灭绝”的例子，并断言过于执着于求生和恐惧死亡对整个族群来说是一种缺点。",
     "evidence": [
      "E5",
      "E6"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者称放大到千年的历史尺度，这种缺点会导致该族群很难挺过千年一遇的危机。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称现存的所有文明社群都有接纳死亡的某种意识形态构建，并列举轮回论、永生论、取义论、奉献论、光荣论、解脱论等。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者以反事实条件称：如果没有这些意识形态构建，遇到必须要承受牺牲的危机，这个族群就只好覆灭。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称“将攻克死亡作为头等大事”首先就是和这种生死攸关的意识形态抵触的。",
     "evidence": [
      "E10"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预测强行推崇和追求“将攻克死亡作为头等大事”，结局更可能是死亡尚未攻克，族群就因甘于为族群牺牲的个体不足、无力应对危机而灭亡。",
     "evidence": [
      "E11"
     ]
    }
   ],
   "argument_steps": [
    "先直接回答并给出经济性理由：全力攻克死亡会导致经济崩溃（P001）。",
    "给出替代性投入方向：让人暂时不死、让暂时死不了的人活得好一些（P002）。",
    "进一步给出投资优先级排序：缓解对死亡的恐惧高于让人不会死（P003）。",
    "以历史经验提出“过于恐惧死亡对族群是缺点”（P004）。",
    "把该缺点放大到千年尺度说明其在危机中的后果（P004）。",
    "以现存文明社群普遍存在接纳死亡的意识形态构建作归纳，并给出反事实：没有则覆灭（P004）。",
    "收束：把攻克死亡当头等大事与生存所依赖的意识形态抵触，强行推崇可能导致族群灭亡（P005）。"
   ],
   "concept_usage": [
    {
     "term": "攻克死亡",
     "meaning": "提问者所指的把医学重心全部用于使人不死；作者以“将攻克死亡作为头等大事”这一表述加以回应与反驳。",
     "evidence": "P001、P005",
     "ambiguity": "本文未界定“攻克死亡”的技术含义与可行范围。"
    },
    {
     "term": "让人暂时不死",
     "meaning": "作者认为更有效率的医学投入方向，与“让暂时死不了的人活得好一些”并列。",
     "evidence": "P002",
     "ambiguity": "未说明具体指哪些医疗措施。"
    },
    {
     "term": "意识形态构建",
     "meaning": "作者用以指现存文明社群中接纳死亡的观念体系，举例包括轮回论、永生论、取义论、奉献论、光荣论、解脱论。",
     "evidence": "P004",
     "ambiguity": "未说明所举各论之间的关系与具体所指。"
    },
    {
     "term": "千年一遇的危机",
     "meaning": "作者设定的观察尺度下才会遇到的、需要族群承受牺牲的危机。",
     "evidence": "P004",
     "ambiguity": "未举例说明。"
    }
   ],
   "examples_and_targets": [
    "历史叙述：“历史上经常有‘因为总体过于恐惧死亡反而导致更多无谓死亡乃至于族群灭绝’的例子”（P004）——作者未给出任何具体事例。",
    "列举材料：轮回论、永生论、取义论、奉献论、光荣论、解脱论等等（P004）——作者作为“接纳死亡的意识形态构建”的例举。",
    "被回应对象：提问者“死亡如此可怕，为何全人类(或者说高层领导人)不主张把重心放在医学上？”（Q001）。"
   ],
   "conditions": [
    "“目前”限定：即使耗尽全部资源，目前也解决不了攻克死亡的问题（P001）。",
    "“更有效率”是作者选择投入方向所依据的标准（P002）。",
    "“放大到千年的历史尺度”是作者设定的观察尺度（P004）。",
    "“如果没有这些意识形态构建……”为反事实条件（P004）。",
    "结论用“更可能”保留可能性，未作必然断言（P005）。"
   ],
   "rhetoric_and_tone": "短篇论辩，先给结论再补理由；用“当然”“甚至”递进主张层级；以“等等等等”作口语化铺陈；历史论证借“千年一遇的危机”作宏观尺度修辞；全篇无引文与数据，末尾无总结句。",
   "unresolved_questions": [
    "“历史上经常有……的例子”未给出任何具体历史事例（待外部核查）。",
    "“现存的所有文明社群，都有接纳死亡的某种意识形态构建”为全称断言，本文未提供比较材料（待外部核查）。",
    "提问中的主体“全人类(或者说高层领导人)”在正文中未被单独回应，作者实际讨论的是资源分配与族群意识形态，提问者与作者的论题不完全重合。",
    "brief 末尾的“历史”疑为平台话题标签，正文中无对应内容，属正文与 brief 不一致。",
    "语料记录的 updated_at（2022-01-27）晚于 published_at（2018-07-22），provenance 与 superseded 均为 null，版本差异无法从本记录确认。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "把全部重心都放在攻克死亡上会立刻导致人类经济崩溃",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P001",
     "quote": "因为把我们全部的资源都耗尽，目前也解决不了这个问题。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P002",
     "quote": "我们当然只有把重心放在更有效率的“让人暂时不死”和“让暂时死不了的人活得好一些”上。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P003",
     "quote": "甚至，应该“让必死的人不要那么害怕死亡”的投资优先级也要高于“让人不会死”。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P004",
     "quote": "历史上经常有“因为总体过于恐惧死亡反而导致更多无谓死亡乃至于族群灭绝”的例子",
     "relation": "context"
    },
    {
     "key": "E6",
     "paragraph_id": "P004",
     "quote": "过于执着于求生和恐惧死亡对于整个族群来说是一种缺点",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P004",
     "quote": "这种缺点会导致这族群很难挺过千年一遇的危机。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P004",
     "quote": "现存的所有文明社群，都有接纳死亡的某种意识形态构建",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P004",
     "quote": "如果没有这些意识形态构建，遇到了必须要承受牺牲的危机，这个族群就只好覆灭。",
     "relation": "qualifies"
    },
    {
     "key": "E10",
     "paragraph_id": "P005",
     "quote": "而“将攻克死亡作为头等大事”首先就是和这种生死攸关的意识形态抵触的。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P005",
     "quote": "结局更可能是死亡尚未攻克，族群就因为甘于为族群牺牲的个体不足，无力应对危机而灭亡。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "医学伦理",
    "资源分配",
    "文化人类学",
    "历史哲学"
   ],
   "issue_candidates": [
    "攻克死亡的资源投入优先级",
    "恐惧死亡与族群存续",
    "接纳死亡的意识形态构建"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩"
   ],
   "object_candidates": [
    "全人类",
    "高层领导人",
    "文明社群",
    "族群"
   ],
   "working_keywords": [
    "攻克死亡",
    "让人暂时不死",
    "意识形态构建",
    "千年一遇的危机",
    "牺牲"
   ]
  },
  "notes": "本篇无图片节点。brief 末尾“历史”疑为平台话题标签，正文无对应内容（正文与 brief 不一致）。提问者提出的主体“全人类(或者说高层领导人)”未被作者单独回应，作者转而讨论资源效率与族群意识形态，此点已在 unresolved_questions 登记。updated_at（2022-01-27）晚于 published_at（2018-07-22），语料未提供版本差异说明。"
 }
}  # noqa: E501


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
