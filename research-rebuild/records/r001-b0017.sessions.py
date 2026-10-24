# -*- coding: utf-8 -*-
"""批次 r001-b0017 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0017.sessions.py            # 写 out/r001-b0017.out.jsonl
  python3 records/r001-b0017.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0017"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0017.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "9b0359f4": {
  "analysis": {
   "question_context": "提问者（Q001）问：超级人工智能可能是费米悖论的大过滤器吗？提问把“超级人工智能”放在费米悖论解释中的“大过滤器”位置，这一框架属于提问者。作者未接受该框架：开篇即否认超级人工智能是人类的大过滤器，并把讨论转向“超级人工智能”这一概念被普遍误解、以及真正的智能体会是什么样子。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "直接否定提问设定的判断：超级人工智能并不是人类的大过滤器。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002",
      "P003"
     ],
     "summary": "指出一种流行误解——把“超级人工智能”当成“智商无限高的人类”，并判定这种理解为错。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "正面描述“真正的智能体”：看起来毫不“智能”，无法完成任何人类要求它完成的任务，将从零展开对世界的认知并建立自己的世界观和价值观。",
     "role": "definition"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "以寿命为条件说明它需要很久才会理解人类可能不是一种随机自然现象。",
     "role": "qualification"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P006"
     ],
     "summary": "在人类眼里它将是“失败作品”，因为几乎没有办法预料它对输入所做的输出，且这种随机性绝不能用“有bug”来解释。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "预测其结局：极大的概率上将在极短的周期内因决策失误或被人类误认为失败废品而失去生命。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P008",
      "P009"
     ],
     "summary": "转折收束：那是一个真实的生命；末段另起一句反问“我们人有自由意志吗？”。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否认提问所设的可能：超级人工智能并不是人类的大过滤器。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者判定：把“超级人工智能”误认为是一种“智商无限高的人类”是错的。",
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
     "statement": "作者主张真正的智能体会看起来毫不“智能”，无法完成任何人类要求它完成的任务，并将从零展开对世界的认知、建立自己的世界观和价值观。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者以“假如它能活那么久”为条件，称它需要花很久才会理解人类可能不是一种随机自然现象。",
     "evidence": [
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为在人类眼里它将是“失败作品”，因为几乎没有办法预料它对输入所做的输出，而且绝不能用“有bug”来解释这种随机性。",
     "evidence": [
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预测：在极大的概率上，它将会在极短的周期内因为决策失误或者因为被人类误认为是失败废品而失去生命。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者强调它是真实的生命。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "open_question",
     "attribution": "unknown",
     "modality": "questioned",
     "statement": "文末出现一句独立反问“我们人有自由意志吗？”，作者未在文中作答；该句是作者正文收尾还是平台附加的话题标签，本文无法确定。",
     "evidence": [
      "E9"
     ]
    }
   ],
   "argument_steps": [
    "先给结论：超级人工智能并不是人类的大过滤器（P001）。",
    "指出并否定流行误解：把超级人工智能当成智商无限高的人类（P002—P003）。",
    "给出作者自己的界定：真正的智能体看起来毫不“智能”，无法完成人类要求的任务，从零建立自己的世界观与价值观（P004）。",
    "加上时间与寿命条件：它需要很久才会理解人类可能不是随机自然现象，假如它能活那么久（P005）。",
    "从人类视角说明它为何像“失败作品”：输出不可预料，且不能用“有bug”解释（P006）。",
    "预测其高概率的短命结局（P007）。",
    "转折肯定其生命地位（P008），末段以反问收束（P009）。"
   ],
   "concept_usage": [
    {
     "term": "大过滤器",
     "meaning": "提问者借自费米悖论的术语，作者只在否定句中沿用（“并不是人类的大过滤器”），本文未给它下定义，也未展开超人工智能与费米悖论的关系",
     "evidence": "P001",
     "ambiguity": "术语来自提问，作者未重新界定"
    },
    {
     "term": "超级人工智能",
     "meaning": "本文中先指一种被流行误解为“智商无限高的人类”的东西，作者随后以“真正的智能体”作对照",
     "evidence": "P002",
     "ambiguity": "作者未说明它与“真正的智能体”是否同一所指"
    },
    {
     "term": "智能体",
     "meaning": "作者用法：看起来毫不“智能”、从零展开对世界的认知并建立自己的世界观和价值观、输出难以预料的存在",
     "evidence": "P004",
     "ambiguity": "未说明其载体、制造者与规模"
    },
    {
     "term": "随机性",
     "meaning": "指智能体对输入所做输出的不可预料，作者明确说不能用“有bug”来解释",
     "evidence": "P006",
     "ambiguity": "未说明其来源"
    },
    {
     "term": "自由意志",
     "meaning": "仅在末段反问中出现，本文未界定",
     "evidence": "P009",
     "ambiguity": "该句本身归属存疑（见未决问题）"
    }
   ],
   "examples_and_targets": [
    "“很多人把‘超级人工智能’误认为是一种‘智商无限高的人类’”——作者的反驳对象（P002—P003）",
    "“有bug”这一说法——作者拒绝用它解释智能体输出的随机性（P006）",
    "费米悖论与大过滤器——提问者设定的问题框架（Q001），作者只作否定回应"
   ],
   "conditions": [
    "“假如它能活那么久的话”——对智能体寿命的条件限定（P005）",
    "“在极大的概率上”“极短的周期内”——概率与时间尺度限定，非必然断言（P007）",
    "“无法完成任何人类要求它完成的任务”——全称否定式界定（P004）",
    "“绝不能用‘有bug’来解释”——对解释方式的排除（P006）"
   ],
   "rhetoric_and_tone": "短句断言开篇，直接以“这是错的”否定流行看法；用引号制造反讽（“智能”“失败作品”“有bug”）；以“但，那是一个真实的生命。”作转折，最后以一句独立反问收束。整体冷峻、断言式、不做展开论证。",
   "unresolved_questions": [
    "末段“我们人有自由意志吗？”是作者正文的收尾反问还是平台附加的话题标签，无法确定（结构解析将其标为 text_tail_not_in_lexical）；本条按原文记录并保留归属不确定。",
    "作者未说明“大过滤器”在其论证中的具体含义，也未说明超级人工智能与费米悖论之间的关联机制。",
    "“真正的智能体”指何种实体、由谁制造、以何为载体、规模如何，本文未说明。",
    "“它需要花很久”的“很久”无量化；其“决策失误”的判据亦未说明。",
    "本文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "超级人工智能并不是人类的大过滤器。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "很多人把“超级人工智能”误认为是一种“智商无限高的人类”。",
     "relation": "context"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "这是错的。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "真正的智能体会看起来毫不“智能”——无法完成任何人类要求它完成的任务",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P005",
     "quote": "它需要花很久才会理解人类可能不是一种随机自然现象——假如它能活那么久的话。",
     "relation": "qualifies"
    },
    {
     "key": "E6",
     "paragraph_id": "P006",
     "quote": "它将是一种“失败作品”，因为几乎没有办法预料它对输入所做的输出",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P007",
     "quote": "在极大的概率上，它将会在极短的周期内因为决策失误或者因为被人类误认为是失败废品而失去生命。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P008",
     "quote": "那是一个真实的生命。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P009",
     "quote": "我们人有自由意志吗？",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "人工智能",
    "未来学",
    "心智哲学",
    "费米悖论/外星文明"
   ],
   "issue_candidates": [
    "超级人工智能是否构成大过滤器",
    "人工智能与人的类比是否成立",
    "机器心智的自主性与生存风险"
   ],
   "text_function_candidates": [
    "答疑",
    "反驳",
    "概念澄清"
   ],
   "object_candidates": [
    "超级人工智能",
    "智能体",
    "人类"
   ],
   "working_keywords": [
    "大过滤器",
    "超级人工智能",
    "智商无限高的人类",
    "真正的智能体",
    "自由意志",
    "失败作品",
    "有bug"
   ]
  },
  "notes": "本篇无图片节点，正文 9 段全部读完。P009“我们人有自由意志吗？”在语料正文尾部、未被 lexical 结构覆盖（walk_body 标记 text_tail_not_in_lexical），其形态既可能是作者的收尾反问，也可能是平台附加的话题标签，故按原文保留并标记归属不确定，未据以扩展作者论证。brief 为正文前若干句的截断，与正文重合，仅作导航，未作为独立证据。提问（Q001）的“大过滤器”框架属提问者，作者只作否定。"
 },
 "f108f52d": {
  "analysis": {
   "question_context": "提问者（Q001）问：修行成就者有什么特征？作者以“只有一个特征”作答，先给出唯一特征，再用排除法否掉若干常见想象（不死的幻想、平静、不怒、料事如神、疯癫、神通）。提问属于提问者，作者的回答是极简断言式的。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "给出唯一特征：不再恐惧死亡。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "排除该特征的性质：不是因为扭曲或幻想，例如相信自己不会死、确信会轮回、相信自己会升天。",
     "role": "qualification"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "澄清“死”的地位未变：死仍然是终结和消散，只是不再令人恐惧。",
     "role": "definition"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P004",
      "P005"
     ],
     "summary": "指出其余方面并不一致，并以“不见得……”的排比否掉平静、不再愤怒、料事如神、疯癫等期待。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P006"
     ],
     "summary": "以一句话否掉神通：不能浮空飞行和隔空取物。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为修行成就者只有一个特征——不再恐惧死亡。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否认这种不恐惧出自扭曲或幻想，例如相信自己不会死、确信自己会轮回、相信自己会升天。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张死仍然是死、仍然是终结和消散，改变的只是不再令人恐惧。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者主张除此之外其他方面并不一致：不见得平静、不见得不再愤怒、不见得料事如神、不见得疯癫。",
     "evidence": [
      "E4",
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者否掉神通期待：成就者不能浮空飞行和隔空取物。",
     "evidence": [
      "E6"
     ]
    }
   ],
   "argument_steps": [
    "先给唯一特征：不再恐惧死亡（P001）。",
    "排除对该特征的误解：不是扭曲或幻想，不是相信自己不死、会轮回、会升天（P002）。",
    "说明“死”本身未被否定，只是恐惧消失（P003）。",
    "声明其余方面并不一致，并用“不见得……”逐项排除（P004—P005）。",
    "末句否掉神通（P006）。"
   ],
   "concept_usage": [
    {
     "term": "修行成就者",
     "meaning": "本文只给出一个判定特征（不再恐惧死亡）并以排除法描述其不是什么；未说明属于哪一修行传统",
     "evidence": "P001",
     "ambiguity": "未界定所指传统与判定方式"
    },
    {
     "term": "恐惧死亡",
     "meaning": "作者区分“死作为终结和消散的事实”与“对死的恐惧”，只否认后者",
     "evidence": "P003",
     "ambiguity": "未说明如何识别该恐惧是否消失"
    },
    {
     "term": "扭曲",
     "meaning": "指以幻想否认死亡（相信自己不会死、会轮回、会升天）的心态",
     "evidence": "P002",
     "ambiguity": "未展开定义"
    }
   ],
   "examples_and_targets": [
    "“相信自己不会死”“确信自己会轮回”“相信自己会升天”——作者列为“扭曲或者幻想”的排除对象（P002）",
    "平静、不再愤怒、料事如神、疯癫——作者以“不见得”逐项否掉的常见想象（P005）",
    "浮空飞行、隔空取物——作者否掉的神通想象（P006）"
   ],
   "conditions": [
    "“只有一个特征”——排他性限定，排除多特征描述（P001）",
    "“不是因为……比如……”——对成因的排除性限定（P002）",
    "“不见得……也不见得……也不见得……也不见得……”——四重否定式限定，只否认必然性、不否认可能性（P005）"
   ],
   "rhetoric_and_tone": "极简断言体，六段短句成篇；以破折号领出唯一特征，随后连续用“不见得”排比降温，末句“不能浮空飞行和隔空取物”以最简方式收尾，带降温、去神秘化意味。",
   "unresolved_questions": [
    "“修行成就者”指哪一修行传统或哪类人，本文未说明。",
    "“不再恐惧死亡”如何判定、由谁判定，本文未说明。",
    "作者未给出任何来源、例证或论证过程，全文为断言式短答。",
    "“其他的方面并不一致”是否意味着随个体差异而无统一特征，本文未说明。",
    "本文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "只有一个特征——不再恐惧死亡。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "不是因为某种扭曲或者幻想",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "死仍然是死，仍然是终结和消散，只是不再令人恐惧。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "除此之外，其他的方面并不一致。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P005",
     "quote": "不见得就很平静，也不见得就不再愤怒，也不见得就料事如神，也不见得就疯癫。",
     "relation": "qualifies"
    },
    {
     "key": "E6",
     "paragraph_id": "P006",
     "quote": "不能浮空飞行和隔空取物。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "宗教修行",
    "死亡观",
    "心灵状态"
   ],
   "issue_candidates": [
    "修行成就的判定标准",
    "对死亡的恐惧",
    "神通与成就的关系"
   ],
   "text_function_candidates": [
    "答疑",
    "界定",
    "去神秘化"
   ],
   "object_candidates": [
    "修行成就者"
   ],
   "working_keywords": [
    "修行成就者",
    "不再恐惧死亡",
    "扭曲",
    "幻想",
    "终结和消散",
    "浮空飞行",
    "隔空取物"
   ]
  },
  "notes": "本篇无图片节点，无结构分歧，正文 6 段全部读完。brief 与正文重合，仅作导航。提问属提问者（Q001）。作者未给出任何来源或论证，全文为断言式短答，未据以补全。"
 },
 "9bd10f2e": {
  "analysis": {
   "question_context": "提问者（Q001）问：女生总是觉得自己长得丑，没有自信怎么办？作者未按“怎么办”给出心理建议式的直接答复，而是先请读者看一组图片（“请看下面这些图”），据此提出“印第安无丑女”的现象，再把问题改写为“美本身的问题”：美是不可逃避的义务、必须以自由为前提、须以学习造就自己的美学语言。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "开篇引导读者观看一组图片（图片来自互联网，侵删），以图引出要讨论的现象。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002",
      "P003",
      "P004"
     ],
     "summary": "提出“印第安无丑女”并设问：这些按流行标准显然丑陋的女性，一旦作为印第安人被观看，为何不丑陋反而显出平静、智慧、神秘或王者般的威严；并指出其中藏着“不够美丽者”的出路。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P005",
      "P006",
      "P007"
     ],
     "summary": "扩展现象范围（黎族、藏族、瑶族、蒙古族、泰雅人、塔希提人、萨摩亚人、修女），指出她们高矮胖瘦不一、按“白富美”标准偏离基准线甚远，却不因此特别丑陋，并再问为什么。",
     "role": "example"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P008"
     ],
     "summary": "转折安排：把前述现象暂时搁置，先谈美本身的问题。",
     "role": "transition"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P009"
     ],
     "summary": "反驳“人不需要追求外在美”的说法：它不成立，是在销售无用的安慰剂，即使对方没有恶意。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P010",
      "P011",
      "P012"
     ],
     "summary": "提出义务论命题：自由是不可抛弃的权利、美是不可逃避的义务；二者是上帝内嵌在自然规律中的强制预定；抛弃自由必遭奴役而灭亡，逃避美的义务即拒绝对同类最基本的爱、必被同类不自觉流放；并要求断绝“我不必追求美丽”的妄想。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P013",
      "P014",
      "P015"
     ],
     "summary": "限定美与自由的关系：美必须以自由为前提；大众审美只是启发和参考而非“美的命令”；完全追随而沮丧或沾沾自喜即首先放弃自由，诅咒随之生效，即使“美丽”人生也将不幸。",
     "role": "qualification"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P016",
      "P017"
     ],
     "summary": "给出路径与结果：美作为义务没有捷径，须不断学习绘画、音乐、文学和理性的美的知识；唯有凭学习扬弃大众审美的标准答案才能找到自己，他人将因敬畏而失去审判资格，由此得到美的自由，成为无法分类打分却值得观看和尊敬的存在。",
     "role": "action_advice"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P018"
     ],
     "summary": "回到现象作解释：“印第安无丑女”的秘密在于印第安妇女以坚定而谦卑的美的呈现整个拒绝了被按流行审美审判；她们呈现的美的语言整个是一门“外语”，并援引“李中堂看见英国绅士”作比。",
     "role": "conclusion"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P019",
      "P020"
     ],
     "summary": "行动要求与警告：造就自己的美学语言是漫长旅程；不要用高光遮掩矮鼻梁或用画眉模版拯救粗眉毛，而要学会教训庸人什么叫“矮鼻梁的美法”“短粗眉的美”；伪装改造成标准人会从另一面触怒上帝。",
     "role": "action_advice"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P021",
      "P022",
      "P023",
      "P024"
     ],
     "summary": "收束：走这条路的收获远非虚荣者所能望见，才能成为真正意义上的人，并给出祝福语，最后以“一些臭男人和蠢妞不爽算个屁啊”作结。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者认为“人不需要追求外在美”这种说法不成立，是在销售无用的安慰剂（即使对方没有恶意）。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出：自由是一种不可抛弃的权利，美是一种不可逃避的义务。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称这种不可抛弃与不可逃避不是某个人或某个统治集团的意志，而是上帝内嵌在自然规律之中、确保强制实施的预定；并称抛弃自由必遭奴役而灭亡，逃避美的义务即拒绝对同类最基本的爱、必被自己的同类不自觉地流放。",
     "evidence": [
      "E5"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张美对人类是不可推卸、不可逃避的普遍义务，并要求断绝“我不必追求美丽”的妄想。",
     "evidence": [
      "E6"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张美必须以自由为前提。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为大众审美、流行趋势是启发和参考，不是“美的命令”；完全追随这一标准而为自己无法匹配而沮丧绝望，或因匹配甚至引领而沾沾自喜，则首先放弃了自由。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者称放弃自由则对甘为奴隶者的诅咒已经生效，即使“美丽”，人生也将不幸。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为美作为义务不可逃避、也没有捷径，意味着必须不断学习美的知识，并点名绘画、音乐、文学和理性的美的知识。",
     "evidence": [
      "E10"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张唯有凭学习去扬弃大众审美的标准答案才能找到自己；在你自己扬弃的结果面前，他人会因敬畏而失去审判资格，由此自然得到美的自由。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预言走这条路的人将成为无法分类打分的、但却不可否认的值得观看和尊敬的存在。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者把“印第安无丑女”解释为：印第安妇女通过自己坚定然而谦卑的美的呈现，整个拒绝了被按照流行审美来审判；她们呈现的美的语言整个是一门“外语”。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出行动要求：造就自己的美学语言是漫长旅程，不要用高光遮掩矮鼻梁或用画眉模版拯救粗眉毛，要学会用努力让庸人知道什么叫“矮鼻梁的美法”“短粗眉的美”。",
     "evidence": [
      "E14"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者强调这条路不容易，但它是不可逃避的义务、有进无退；而努力把自己伪装改造成标准人则会从另一面触怒上帝。",
     "evidence": [
      "E15"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者称走这条路收获的远非虚荣者所能望见，并且才能成为一个真正意义上的人。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以祝福语作结：你必受祝福，上帝祝福你，一些臭男人和蠢妞不爽算个屁。",
     "evidence": [
      "E17"
     ]
    }
   ],
   "argument_steps": [
    "先请读者看一组图片（P001）。",
    "提出“印第安无丑女”并设问：为何按流行标准丑陋者在被作为印第安人观看时反而不丑、且显出威严（P002—P003）。",
    "指出这现象里藏着“不够美丽者”的出路（P004）。",
    "把现象扩展到黎族、藏族、瑶族、蒙古族、泰雅人、塔希提人、萨摩亚人与修女，并再设一问（P005—P007）。",
    "暂时搁置现象，转入“美本身”的讨论（P008）。",
    "先反驳“人不需要追求外在美”，称之为无用的安慰剂（P009）。",
    "给出义务论命题：自由是不可抛弃的权利，美是不可逃避的义务，二者是上帝内嵌于自然规律的强制预定（P010—P011）。",
    "要求断绝“我不必追求美丽”的妄想（P012）。",
    "补充前提：美必须以自由为前提；大众审美不是“美的命令”（P013—P014）。",
    "给出放弃自由的后果：诅咒生效，即使美丽也不幸（P015）。",
    "给出路径：必须学习美的知识，凭学习扬弃大众审美的标准答案（P016）。",
    "给出结果：成为无法分类打分却值得观看和尊敬的存在（P017）。",
    "回到最初现象，给出“印第安无丑女”的解释（P018）。",
    "给出具体做法与警告：造就自己的美学语言，不要伪装成标准人（P019—P020）。",
    "收束于收获、成为真正的人与祝福（P021—P024）。"
   ],
   "concept_usage": [
    {
     "term": "美",
     "meaning": "本文中被界定为“不可逃避的义务”、普遍义务，并且必须以自由为前提；不是大众审美的标准答案",
     "evidence": "P010",
     "ambiguity": "与“大众审美”“流行审美”的关系在文中被反复区分，但“美本身”的标准未给出"
    },
    {
     "term": "自由",
     "meaning": "“不可抛弃的权利”，是美的前提；放弃自由即受诅咒、被奴役而灭亡",
     "evidence": "P010",
     "ambiguity": "文中以上帝预定与自然规律解释其强制性，未给出世俗层面的界定"
    },
    {
     "term": "大众审美/流行趋势",
     "meaning": "本文中只是一种“启发和参考”，不是“美的命令”；完全追随它会放弃自由",
     "evidence": "P014",
     "ambiguity": "未说明其与“美的知识”冲突时如何取舍"
    },
    {
     "term": "美的语言",
     "meaning": "作者以此比喻个人自成一套、如“外语”般的美的呈现方式，使他人无法按流行审美审判",
     "evidence": "P018",
     "ambiguity": "比喻性用法，未给出可操作定义"
    },
    {
     "term": "上帝",
     "meaning": "文中作为把自由与美的义务“内嵌在自然规律之中、确保强制实施”的预定者；触怒上帝是行为后果的表述",
     "evidence": "P011",
     "ambiguity": "未说明是宗教实指还是修辞用法"
    },
    {
     "term": "庸人",
     "meaning": "指“不知美为何物”、按流行标准审判他人的人",
     "evidence": "P019",
     "ambiguity": "带贬义的称呼，指称范围未界定"
    }
   ],
   "examples_and_targets": [
    "文首的 7 张图片（IMG001—IMG007，标注“图片来自互联网，侵删”）——作者据以引出“印第安无丑女”的例证材料，图片内容未经核验（P001）",
    "印第安妇女——作者的核心例证（P002、P003、P018）",
    "黎族、藏族、瑶族、蒙古族、泰雅人、塔希提人、萨摩亚人、修女——现象扩展所举群体（P005）",
    "“白富美”审美观——作者所批评的流行标准（P006）",
    "“人不需要追求外在美”——作者的反驳对象（P009）",
    "“高光”“画眉模版”——作者劝其放弃的具体化妆做法（P019）",
    "“李中堂看见英国绅士，是不会轻易说‘丑’的”——作者用以类比“另一种美”的历史人物修辞（P018）"
   ],
   "conditions": [
    "“一旦作为印第安人被观看”——观察方式的转换条件（P003）",
    "“按照流行的‘白富美’审美观而言”——评价标准的前提限定（P006）",
    "“也许对方没有恶意，但是却是不成立的”——对“安慰剂”说法的让步式限定（P009）",
    "“完全追随这一标准……则你首先放弃了自由”——条件句（P014）",
    "“你放弃了自由，则对甘为奴隶者的诅咒已经生效”——条件句（P015）",
    "“当你能呀呀而语时”——学习阶段的限定（P019）",
    "“那当然不容易”“有进无退”——对难度的明说（P020）"
   ],
   "rhetoric_and_tone": "兼具训诫与鼓动：以图片与设问开场（“印第安无丑女”“这是为什么？”），随即转入义务论式的断语与“记住这句话”的命令句；大量使用宗教语汇（上帝、预定、诅咒、祝福）与对仗（“自由是一种不可抛弃的权利，美是一种不可逃避的义务”）；对流行审美与“庸人”用语带讽刺（“销售无用的安慰剂”“臭男人和蠢妞不爽算个屁啊”）；结构上是“现象—搁置—理论—回到现象—行动要求—祝福”的环形安排。",
   "unresolved_questions": [
    "本篇含 7 个图片节点（IMG001—IMG007），图片内容未经核验，需人工/多模态复核；这些图片是“印第安无丑女”论断的直接例证材料，图片未核验前该论断的证据链不完整。",
    "作者据以判断图片中女性“按流行标准显然丑陋”的具体依据，本文未说明。",
    "文中“上帝”“预定”“诅咒”“祝福”是宗教实指还是修辞用法，本文未说明。",
    "“美的知识”与“大众审美的标准答案”的界限、以及如何判定“扬弃”成功，本文未说明。",
    "“李中堂看见英国绅士”这一用典的具体所指与来源，本文未说明，需外部核查。",
    "所举“黎族、藏族、瑶族、蒙古族、泰雅人、乃至塔希提人、萨摩亚人、还有修女”的观察依据（是否有图像或文献支撑）本文未说明。",
    "P001 称“请看下面这些图”，但图片与正文段落的对应关系在语料结构中不可见。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "请看下面这些图（图片来自互联网，侵删）",
     "relation": "context"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "印第安无丑女。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P009",
     "quote": "有人跟你们说“人不需要追求外在美”，这是不成立的。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P010",
     "quote": "自由是一种不可抛弃的权利，美是一种不可逃避的义务。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P011",
     "quote": "而是上帝内嵌在自然规律之中、确保强制实施的预定",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P012",
     "quote": "美对人类是一种不可推卸、不可逃避的普遍义务。请断绝“我不必追求美丽”的妄想。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P013",
     "quote": "美必须以自由为前提。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P014",
     "quote": "大众审美、流行趋势，是一种启发和参考，那不是“美的命令”。",
     "relation": "qualifies"
    },
    {
     "key": "E9",
     "paragraph_id": "P015",
     "quote": "你放弃了自由，则对甘为奴隶者的诅咒已经生效，即使“美丽”，你的人生也将不幸。",
     "relation": "qualifies"
    },
    {
     "key": "E10",
     "paragraph_id": "P016",
     "quote": "那意味着你必须要不断学习美的知识",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P016",
     "quote": "唯有凭着学习去扬弃大众审美的标准答案，你才能找到你自己。",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P017",
     "quote": "你将成为无法分类打分的、但却不可否认的值得观看和尊敬的存在。",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P018",
     "quote": "印第安妇女们事实上通过自己坚定然而谦卑的美的呈现，整个的拒绝了被按照流行审美来审判。",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P019",
     "quote": "当你能呀呀而语时，不要想着用什么高光去遮掩你的矮鼻梁",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P020",
     "quote": "而努力把自己伪装改造成标准人，你会从另一面触怒上帝。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P022",
     "quote": "走这条路，你才能成为一个真正意义上的人。",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P024",
     "quote": "上帝祝福你，一些臭男人和蠢妞不爽算个屁啊。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "美学",
    "性别与社会审美",
    "宗教/神学语汇",
    "自我修养"
   ],
   "issue_candidates": [
    "流行审美标准的压迫",
    "外貌焦虑与自信",
    "美的义务与自由的关系",
    "少数族群女性形象的观看方式"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "训诫",
    "鼓动"
   ],
   "object_candidates": [
    "印第安妇女",
    "黎族",
    "藏族",
    "瑶族",
    "蒙古族",
    "泰雅人",
    "塔希提人",
    "萨摩亚人",
    "修女",
    "李中堂（李鸿章）",
    "上帝"
   ],
   "working_keywords": [
    "印第安无丑女",
    "白富美",
    "自由",
    "义务",
    "美的语言",
    "矮鼻梁的美法",
    "短粗眉的美",
    "标准人",
    "不可逃避"
   ]
  },
  "notes": "本篇含 7 个图片节点（IMG001—IMG007），图片内容未经核验，故 status=needs_reread、image_checked=false；正文 24 段已全部读完并记录，但 P001 明确要求读者观看图片，图片是“印第安无丑女”论断的直接例证，未经图像核验前该论断的证据链不完整。brief 与正文前段重合，仅作导航。提问（Q001）中的“没有自信怎么办”属提问者语境，作者未按心理建议作答，而是改写为美学义务论问题。",
  "status": "needs_reread",
  "image_checked": False
 },
 "8edc436c": {
  "analysis": {
   "question_context": "提问者（Q001）问：有信仰的人真的可以为了信仰付出生命吗？作者先判定“这个问题并不简单”，随后把问题改写为信仰必然有错、以及人在无法摆脱的修正困境中如何选择固守之物；结尾把“为了信仰而死”重新定义为一种“活法”，并未直接回答“可不可以”的许可式问题。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "开场判断：这个问题并不简单。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002",
      "P003",
      "P004"
     ],
     "summary": "提出并论证“你的信仰客观上一定是错的”：因为人不能看到无限久远的未来和讨论一切具体情况，故无论语言表述如何，信仰的实际内容必然在某种程度上存在错误，实质上、绝对意义上一定是错误的东西；无论相信什么都不能改变这一事实。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P005",
      "P006"
     ],
     "summary": "把上述事实称为人生最大的困境，并说明机理：信仰是人生最高指导方针，一旦发现错误就不能不修正，导致一系列决策推翻和更改，并带来大量善后工作与沉重现实代价；原本视为正义的事业在新信仰下变成显然邪恶，于是要立刻停止甚至尽快拆毁、弥补。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "描述困境的无休止后果：永远处在准备改弦易辙的投机焦虑中，不敢对本钱下注，本钱被拆成五分一毛丢进儿戏，常同时赌互相矛盾的两种方案，必然有一半输掉另一半可能得来的利润。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P008",
      "P009"
     ],
     "summary": "给出被迫的出路：最终将被迫选择一条不能不选择的道路——固执一端，有死而已；并以口语写出该选择的心态“我选了这个，大不了死逑去”。",
     "role": "claim"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P010",
      "P011",
      "P012",
      "P013"
     ],
     "summary": "说明固执一端的效用：其“错误”失去实际威胁，才能稳定坚持、才有实际有效的恒心与毅力、才能真的建立点东西；虽然那东西浑身是毛病但好歹是个东西；留下东西其好的一面可启发人、帮助人，坏的一面可警示人、提醒人，于是没有白活，生命经由人类历史而长存。",
     "role": "conclusion"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P014",
      "P015"
     ],
     "summary": "重述问题：“为了信仰而死”其实是一种活法；并限定“死”的含义——不是“引刀成一快”，在绝大多数情况下指好几十年为一个主题进行、至死方休的“知其恐不可为，而勉为之”。",
     "role": "conclusion"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P016",
      "P017"
     ],
     "summary": "给出选择标准：人是不能不选的，唯一差别在所固守之物必须真正在逻辑上不可拆毁，也就是自洽且具有确定无疑的不可证伪性。",
     "role": "action_advice"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020"
     ],
     "summary": "分别说明两条标准的用处：因自洽而不必焦虑将来自相矛盾而自我拆毁（至少不会全部拆毁，只是不破不立的螺旋上升）；因逻辑上有根本的、确定无疑的不可证伪性才可放心大胆坚守，因为永远没有被彻底证明错误的一天——不是靠回避批评，而是逻辑本身没有这个能力。",
     "role": "reason"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P021"
     ],
     "summary": "收束：记住这两个标准，这是安身立命之所的经线和纬线。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者断言：你的信仰客观上一定是错的。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出的理由：人根本不能看到无限久远的未来和讨论一切具体情况，因此无论信仰的语言表述如何，其实际内容必然在某种程度上存在错误，从实质上、绝对的意义上说一定是一个错误的东西。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称无论你相信什么都不能改变这一事实，并称之为人生最大的困境。",
     "evidence": [
      "E3",
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者说明困境的机理：信仰是人生最高指导方针，一旦发现其错误就不能不修正，导致一系列决策的推翻和更改，并带来大量善后工作与沉重的现实代价；原以为正义的事业在新信仰下会变成显然邪恶，于是不但要立刻停止，甚至要尽快拆毁、弥补。",
     "evidence": [
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为这种困境无休无止、没有尽头，不摆脱它将永远处在准备改弦易辙的投机焦虑中，不敢对本钱下大注，并时常在赌完全互相矛盾的两种方案。",
     "evidence": [
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "predicted",
     "statement": "作者预测：你最终将被迫选择一条你不能不选择的道路——固执一端，有死而已。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者以第一人称口语写出做出该选择时的心态：“我选了这个，大不了死逑去。”",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为做了这样的选择，信仰的“错误”就失去了实际威胁，人才能稳定坚持，才有可能有实际有效的恒心与毅力，才有可能真的建立点东西。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者承认所建立的东西“浑身是毛病”，但认为它好歹会是个东西，其好的一面可以启发人、帮助人，坏的一面可以警示人、提醒人，于是人没有白活，生命经由人类的历史而长存。",
     "evidence": [
      "E10",
      "E11"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者给出对提问的重述：“为了信仰而死”其实是一种活法。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者限定“死”的含义：这里的死不是指“引刀成一快”，在绝大多数情况下是指好几十年为一个主题而进行的、至死方休的“知其恐不可为，而勉为之”。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出选择标准：人是不能不选的，唯一的差别是所固守的东西必须真正在逻辑上不可拆毁，也就是自洽且具有确定无疑的不可证伪性。",
     "evidence": [
      "E14",
      "E15"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者说明两条标准的用处：因自洽而不必焦虑将来会自相矛盾而自我拆毁，至少不会全部拆毁，而只是不破不立的螺旋上升；因逻辑上有根本的、确定无疑的不可证伪性，才可以放心大胆地坚守。",
     "evidence": [
      "E16",
      "E17"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者称永远没有会被彻底证明错误的一天，不是因为回避批评、讳疾忌医，而是逻辑本身没有这个能力；并要求记住这两个标准，称之为安身立命之所的经线和纬线。",
     "evidence": [
      "E18",
      "E19"
     ]
    }
   ],
   "argument_steps": [
    "先判定问题并不简单（P001）。",
    "给出断言：你的信仰客观上一定是错的（P002），理由是人的认知不能覆盖无限久远的未来与一切具体情况（P003）。",
    "强调这一事实不可因信仰内容而改变，并称之为人生最大的困境（P004—P005）。",
    "展开困境机理：最高指导方针一旦被判错就必须修正，带来决策推翻、善后代价与“正义变邪恶”的翻转（P006）。",
    "描述困境的无休止状态与投机焦虑、本钱耗散、同时赌矛盾方案（P007）。",
    "给出被迫的选择：固执一端，有死而已（P008—P009）。",
    "说明该选择的效用：错误失去实际威胁，方能稳定坚持并建立东西（P010—P013）。",
    "由此重述问题：“为了信仰而死”其实是一种活法（P014）。",
    "限定“死”的含义：不是引刀成一快，而是数十年至死方休的“知其恐不可为，而勉为之”（P015）。",
    "给出选择标准：所固守之物须逻辑上不可拆毁，即自洽且具有确定无疑的不可证伪性（P016—P017）。",
    "分述自洽与不可证伪性各自的用处（P018—P020）。",
    "以“经线和纬线”收束（P021）。"
   ],
   "concept_usage": [
    {
     "term": "信仰",
     "meaning": "本文中作为“人生的最高指导方针”，其语言表述与实际内容被区分开；作者断言其客观上一定是错的",
     "evidence": "P003",
     "ambiguity": "未说明是否包括非宗教的信念体系"
    },
    {
     "term": "错误",
     "meaning": "作者在“实质上、绝对的意义上”使用，指信仰实际内容在某种程度上的偏差，而非日常意义上的可检验错误",
     "evidence": "P003",
     "ambiguity": "“某种程度”未量化"
    },
    {
     "term": "困境",
     "meaning": "指信仰必然有错与必须据以行动之间的持续张力：一旦发现错误就必须修正，代价沉重且无休无止",
     "evidence": "P005",
     "ambiguity": "无"
    },
    {
     "term": "固执一端，有死而已",
     "meaning": "作者给出的被迫选择：选定一端不再改弦，承担其后果",
     "evidence": "P008",
     "ambiguity": "与“不可证伪”标准的关系需并读P016—P017"
    },
    {
     "term": "死",
     "meaning": "本文中不是“引刀成一快”，而是“好几十年为一个主题而进行的、至死方休的‘知其恐不可为，而勉为之’”",
     "evidence": "P015",
     "ambiguity": "“绝大多数情况下”留有例外"
    },
    {
     "term": "自洽",
     "meaning": "所固守之物在逻辑上不自相矛盾的属性，作用是避免将来自我拆毁",
     "evidence": "P017",
     "ambiguity": "未给出检验方式"
    },
    {
     "term": "不可证伪性",
     "meaning": "逻辑上有根本的、确定无疑的不可证伪性，使人永远不会被彻底证明错误",
     "evidence": "P017",
     "ambiguity": "作者明确说这是逻辑本身的能力限制所致，不等同于真"
    }
   ],
   "examples_and_targets": [
    "“引刀成一快”——作者否定的对“死”的通俗理解（P015）",
    "“知其恐不可为，而勉为之”——作者引以描述其所谓“死”的持续形态（P015）",
    "“经线和纬线”——作者用来说明两条标准的地位（P021）",
    "赌博与儿戏的比喻（“赌完全互相矛盾的两种方案”“拆成了五分一毛丢进无关痛痒的儿戏”）——作者的类比材料（P007）"
   ],
   "conditions": [
    "“无论你的信仰的语言表述如何”——对信仰表述方式的覆盖条件（P003）",
    "“在某种程度上”“从实质上、绝对的意义上说”——作者自己加的程度与意义限定（P003）",
    "“一旦发现其错误，就不能不修正”——条件句（P006）",
    "“在绝大多数情况下”——对“死”的用法的量词限定，留有例外（P015）",
    "“必须要真正地在逻辑上不可拆毁”——对固守对象的要求条件（P016）",
    "“至少要……不会全部拆毁”——让步性限定（P018）",
    "“不是因为你回避批评、讳疾忌医，而是逻辑本身没有这个能力”——对不可证伪性来源的限定（P020）"
   ],
   "rhetoric_and_tone": "通篇以第二人称“你”直接对读者说话，先下断语再审理由，带训诫与开解双重语气；使用设问（“为什么呢？”）、口语与粗话（“大不了死逑去”“浑身是毛病”）、比喻（“本钱拆成五分一毛”“经线和纬线”）与引语（“引刀成一快”“知其恐不可为，而勉为之”）。结尾把标准称为安身立命之所的经纬，语气转为庄重。",
   "unresolved_questions": [
    "作者未直接回答提问者“有信仰的人真的可以为了信仰付出生命吗”的许可式问题，而把“为了信仰而死”重述为一种“活法”；此处是对提问的改写而非直接答复。",
    "“人根本就不能看到无限久远的未来和讨论一切具体情况”这一前提，本文未给出论证或来源。",
    "“自洽且具有确定无疑的不可证伪性”如何检验、由谁判定，本文未说明。",
    "作者未说明“信仰”是否包括非宗教的信念或主义。",
    "P015 说“在绝大多数情况下”指数十年的坚持，未说明其余情况下“死”指什么。",
    "本文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P002",
     "quote": "首先，你的信仰客观上一定是错的。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P003",
     "quote": "因为人根本就不能看到无限久远的未来和讨论一切具体情况",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P004",
     "quote": "其实无论你相信什么，都不能改变这一事实。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P005",
     "quote": "这也是人生最大的困境。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P006",
     "quote": "因为作为人生的最高指导方针，你一旦发现其错误，就不能不修正",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P007",
     "quote": "这种困境无休无止，没有尽头。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P008",
     "quote": "你最终将被迫选择一条你不能不选择的道路——固执一端，有死而已。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P009",
     "quote": "我选了这个，大不了死逑去。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P010",
     "quote": "做了这样的选择，则它的“错误”就失去了实际威胁。",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P011",
     "quote": "但好歹会是个东西。",
     "relation": "qualifies"
    },
    {
     "key": "E11",
     "paragraph_id": "P012",
     "quote": "它好的一面可以启发人、帮助人，它坏的一面可以警示人、提醒人",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P014",
     "quote": "所以，“为了信仰而死”，其实是一种活法。",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P015",
     "quote": "是指好几十年为一个主题而进行的、至死方休的“知其恐不可为，而勉为之”。",
     "relation": "qualifies"
    },
    {
     "key": "E14",
     "paragraph_id": "P016",
     "quote": "必须要真正地在逻辑上不可拆毁",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P017",
     "quote": "也就是自洽且具有确定无疑的不可证伪性。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P018",
     "quote": "而只是不破不立的螺旋上升",
     "relation": "qualifies"
    },
    {
     "key": "E17",
     "paragraph_id": "P019",
     "quote": "你才可以放心大胆地坚守",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P020",
     "quote": "因为你永远没有会被彻底证明错误的一天",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P021",
     "quote": "这是你安身立命之所的经线和纬线",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "信仰与宗教哲学",
    "认识论",
    "人生哲学",
    "逻辑方法"
   ],
   "issue_candidates": [
    "为信仰付出生命是否可能/合理",
    "信仰的可修正性与代价",
    "自洽与不可证伪性作为坚守标准"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "开解",
    "劝诫"
   ],
   "object_candidates": [
    "信仰者",
    "人类（认知能力）"
   ],
   "working_keywords": [
    "信仰",
    "客观上一定是错的",
    "人生最大的困境",
    "固执一端",
    "活法",
    "自洽",
    "不可证伪性",
    "经线和纬线"
   ]
  },
  "notes": "本篇无图片节点，无结构分歧，正文 21 段全部读完。brief 与正文重合，仅作导航。P009“我选了这个，大不了死逑去。”是作者以第一人称口语写出的选择心态，非引用他人，已按作者语气记录。作者未直接回答提问中的“可不可以”，而是改写为“其实是一种活法”（P014），此点记入未决问题。"
 },
 "4ce90533": {
  "analysis": {
   "question_context": "提问者（Q001）问：同樣用拉滿弓的力量，為什麼弓射出的箭比手扔出的快那麼多？（原文为繁体）作者只回答了“手掷”一侧的能量损耗，未直接比较弓与手的能量转换效率，也未给出任何数据。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "给出理由：用手投掷物品的能量大部分消耗在挥动手臂上；物件越轻，能量分配到人身体上的比例越大。",
     "role": "reason"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "推出两个结论：很难扔远一根稻草；用于手动投掷的武器会和手臂本身的重量相称。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为用手投掷物品的能量大部分都消耗在挥动手臂上。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者提出单调关系：投出的物件越轻，这份能量就有越大比例分配在人的身体上而不是被投出的物品上。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者由此推论：很难扔远一根稻草。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者推论：用于手动投掷的武器会和手臂本身的重量相称。",
     "evidence": [
      "E4"
     ]
    }
   ],
   "argument_steps": [
    "给出能量分配的前提：手掷时大部分能量消耗在挥动手臂上（P001）。",
    "给出随质量变化的趋势：投出物越轻，能量越多分配给身体（P001）。",
    "以稻草为例推出“扔不远”（P002）。",
    "推出投掷武器与手臂重量相称（P002）。"
   ],
   "concept_usage": [
    {
     "term": "能量",
     "meaning": "本文中用以说明手掷时能量在“人的身体”和“被投出的物品”之间的分配比例",
     "evidence": "P001",
     "ambiguity": "未说明能量形式、也未给出定量关系"
    },
    {
     "term": "重量相称",
     "meaning": "指手动投掷武器的重量与手臂本身的重量相匹配",
     "evidence": "P002",
     "ambiguity": "未给出相称的判据或范围"
    }
   ],
   "examples_and_targets": [
    "“你很难扔远一根稻草”——作者用以说明轻物难掷的例证（P002）",
    "“用于手动投掷的武器会和手臂本身的重量相称”——作者由前提推出的应用性结论（P002）",
    "弓与手的对比——提问者提出的对比（Q001），作者未在正文中直接处理"
   ],
   "conditions": [
    "“投出的物件越轻，则……越大比例”——单调关系，隐含只在其他条件相同时成立（P001）",
    "“同样用拉满弓的力量”——提问设定的对照条件（Q001），本文未回应"
   ],
   "rhetoric_and_tone": "极简说明体：两段共 102 字，先给理由再给两个“因此”式结论，无修辞、无数据、无来源。",
   "unresolved_questions": [
    "提问的核心是比较：同样用力，为什么弓射出的箭比手扔的快得多；本文只解释了手掷侧的能量损耗，未说明弓如何把能量更有效地传给箭，未直接作答。",
    "“大部分都消耗在挥动手臂上”无数据或来源支持，需外部核查。",
    "“用于手动投掷的武器会和手臂本身的重量相称”未给出定量范围。",
    "标题“甩手箭”与正文内容的关系，本文未说明。",
    "本文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "因为用手投掷物品的能量，大部分都消耗在挥动手臂上了。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P001",
     "quote": "投出的物件越轻，则这份能量就有越大比例分配在人的身体上而不是被投出的物品上。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P002",
     "quote": "因此，你很难扔远一根稻草。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P002",
     "quote": "也因此用于手动投掷的武器会和手臂本身的重量相称。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "物理学（力学/能量传递）",
    "兵器史"
   ],
   "issue_candidates": [
    "弓与手掷的能量转换效率差异",
    "投掷物质量与能量分配的关系"
   ],
   "text_function_candidates": [
    "答疑",
    "解释"
   ],
   "object_candidates": [
    "弓",
    "箭",
    "手臂",
    "稻草"
   ],
   "working_keywords": [
    "拉满弓",
    "手扔",
    "能量",
    "挥动手臂",
    "重量相称",
    "稻草"
   ]
  },
  "notes": "本篇无图片节点，无结构分歧，正文 2 段（102 字）全部读完。brief 与正文重合，仅作导航。提问（Q001）用繁体，已按原文保留在 question 字段（不属本记录正文）。本文未回答提问中“弓为何更快”的比较部分，此点记入未决问题。"
 },
 "ec350b6f": {
  "analysis": {
   "question_context": "提问者（Q001）问：为什么很多女孩是大叔控？作者不接受“大叔控”这一提法的特殊性，先用量级与历史事例说明年龄差六岁以上的亲密关系历来常见，再反问“六岁”门槛的依据，最后指出现代把这类现象当作“不正常”来讨论才是独特现象，并对“人不该选同龄人吗”给出反问式回应。提问中的“很多女孩是大叔控”属提问者框架。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002"
     ],
     "summary": "以“真心说句实话”开场，断言古今从不缺年龄差六岁以上的亲密关系、十岁以上也不罕见；并反问“六岁”的依据，指出六岁对应小学毕业与幼儿园毕业、上大学与小学毕业的差别。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "建议读者查历史上著名夫妇的年龄差，并称皇室婚姻、政治领袖更不用说。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006",
      "P007",
      "P008",
      "P009",
      "P010",
      "P011",
      "P012",
      "P013",
      "P014",
      "P015",
      "P016"
     ],
     "summary": "列举十三组名人夫妇的年龄差：孙中山比宋庆龄大27岁、周恩来比邓颖超大6岁、鲁迅比许广平大17岁、迭戈·里维拉大弗里达11岁、达利老婆比达利大10岁、里根比原配大6岁、肯尼迪大杰奎琳12岁、居里比居里夫人大8岁、马丁路德比妻子大16岁、林肯比妻子大9岁、曼德拉大妻子27岁、恩格斯大妻子7岁、赫本比罗伯特沃德斯大7岁。",
     "role": "example"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P017"
     ],
     "summary": "提示读者自行查证，并预先排除“趋炎附势”的解释（很大一部分是没有发迹前就结婚的），据此断言年龄差6岁以上绝不罕见——如果不是主流的话。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020"
     ],
     "summary": "指出把差五六岁描述为“大叔控”“老夫少妻”、当作“特异形态”来讨论，反而是现代才有的独特现象；并连续设问让读者自己想为什么、为什么一种历来存在甚至堪称主流的现象如今被当作“不正常”拿到知乎评头论足。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P021",
      "P022"
     ],
     "summary": "反问“谁说人就该选同龄人？”，并断言在这个时代谁都不该选择三十岁以下的人，理由是这一代人的心理发育明显滞后、不到三十岁还像孩子一样；又称仅仅心有不甘地吐槽别人的正常选择权利本身就是不合格的幼稚表现。",
     "role": "claim"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P023"
     ],
     "summary": "文末另有“社科答集”字样，疑为平台话题标签混入正文，非作者论述。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为从古到今从来就不缺年龄差六岁以上的亲密关系，十岁以上的也谈不上什么罕见。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问“六岁”这一门槛的依据，并指出六岁差在人生阶段上对应“一方小学毕业，另一方幼儿园毕业”“一方上大学，一方小学毕业”。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者建议读者查阅历史上著名夫妇的年龄差，并称若是皇室婚姻、政治领袖就更不必说。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者列举孙中山与宋庆龄（27岁）等十三组名人夫妇的年龄差，作为年龄差并不罕见的例证。",
     "evidence": [
      "E4",
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为很大一部分名人夫妇是没有发迹前就结婚的，因此不能简单地用“趋炎附势”来解释年龄差，并据此断言年龄差在6岁以上绝不罕见——如果不是主流的话。",
     "evidence": [
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为把差五六岁描述为“大叔控”“老夫少妻”、认为特别并值得单独挑出来作为“特异形态”讨论，反而是现代才有的独特现象。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者反问：为什么一种从古到今就存在、根本不奇怪、甚至堪称主流的现象，现在会变成一种似乎“不正常”的东西被知乎拿来评头论足。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者反问“谁说人就该选同龄人？”，并断言在这个时代谁都不该选择三十岁以下的人，因为这一代人的心理发育明显滞后、不到三十岁还像孩子一样。",
     "evidence": [
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为光是心有不甘地吐槽人家正常选择权利，本身就是不合格的幼稚表现。",
     "evidence": [
      "E11"
     ]
    }
   ],
   "argument_steps": [
    "先给量级判断：年龄差六岁以上历来不稀缺（P001）。",
    "反问“六岁”门槛的依据，并给出该门槛对应的人生阶段（P002）。",
    "建议查证历史上著名夫妇，指出皇室婚姻与政治领袖的情况更明显（P003）。",
    "连续列举十三组名人夫妇的年龄差（P004—P016）。",
    "提示读者自行查证，并预先排除“趋炎附势”的解释，得出“绝不罕见、甚至主流”的结论（P017）。",
    "指出把这类年龄差当作“特异形态”讨论是现代才有的现象（P018）。",
    "以连续设问要求读者自问其原因（P019—P020）。",
    "反问“谁说人就该选同龄人”，并给出“不该选三十岁以下”的断言（P021）。",
    "以“吐槽别人正常选择权利是不合格的幼稚表现”收尾（P022）。",
    "文末“社科答集”字样，疑为平台标签（P023）。"
   ],
   "concept_usage": [
    {
     "term": "大叔控",
     "meaning": "提问者使用的说法；作者把它加上引号并视为需要被质疑的现代标签，而非自然类别",
     "evidence": "P018",
     "ambiguity": "作者未界定其年龄差下限，只质疑“六岁”门槛"
    },
    {
     "term": "年龄差",
     "meaning": "本文以配偶年龄差为观察量，重点在六岁以上的情形",
     "evidence": "P001",
     "ambiguity": "未区分男方年长与女方年长的情形，举例中两者皆有（P008 达利老婆比达利大10岁）"
    },
    {
     "term": "趋炎附势",
     "meaning": "作者预设的替代解释并加以排除，理由是许多名人夫妇在发迹前结婚",
     "evidence": "P017",
     "ambiguity": "作者未说明该理由覆盖多少比例"
    },
    {
     "term": "主流",
     "meaning": "作者以“如果不是主流的话”作让步式表述，指年龄差六岁以上可能属多数情形",
     "evidence": "P017",
     "ambiguity": "未给出统计数据"
    }
   ],
   "examples_and_targets": [
    "孙中山比宋庆龄大27岁（P004）——作者例证",
    "周恩来比邓颖超大6岁（P005）——作者例证",
    "鲁迅比许广平大17岁（P006）——作者例证",
    "迭戈·里维拉大弗里达11岁（P007）——作者例证",
    "达利老婆比达利大10岁（P008）——作者例证（女方年长）",
    "里根比他原配大6岁（P009）——作者例证",
    "肯尼迪大杰奎琳12岁（P010）——作者例证",
    "居里比居里夫人大8岁（P011）——作者例证",
    "马丁路德（没有金）比妻子大16岁（P012）——作者例证",
    "林肯比妻子大9岁（P013）——作者例证",
    "纳尔逊曼德拉大妻子27岁（P014）——作者例证",
    "恩格斯大妻子7岁（P015）——作者例证",
    "赫本比她的灵魂伴侣罗伯特沃德斯大7岁（P016）——作者例证（女方年长）",
    "“趋炎附势”这一解释——作者的反驳对象（P017）",
    "知乎上的讨论风气——作者批评的对象（P020）",
    "以上各组年龄差数据本文未给出出处，属事实断言，需外部核查。"
   ],
   "conditions": [
    "“如果是皇室婚姻、政治领袖就更不提了”——对例证范围的扩展性表述（P003）",
    "“很大一部分是没有发迹前就结婚的”——作者自陈理由的覆盖范围有限（P017）",
    "“如果不是主流的话”——让步式限定（P017）",
    "“基本上在这个时代”——时间与范围限定（P021）",
    "“可以说还像孩子一样”——模糊化限定（P021）"
   ],
   "rhetoric_and_tone": "口语化、对抗性强的辩驳语气：开场“真心说句实话”，中间连续十三句短句列举构成清单式举证，随后以“你们可以随便想几个伟人”“你们自己想想为什么”直接呼告读者，并连用反问（“为什么六岁？”“谁说人就该选同龄人？”）；结尾以“不合格的幼稚表现”作贬抑式评判，带调侃与教训并存的口吻。",
   "unresolved_questions": [
    "文末 P023 仅“社科答集”三字，未被 lexical 结构覆盖（walk_body 标记 text_tail_not_in_lexical），疑为平台话题/答集标签混入正文，非作者论述。",
    "十三组名人夫妇的年龄差数据本文未给出出处，属需外部核查的事实断言。",
    "作者用“绝不罕见”“如果不是主流的话”描述年龄差六岁以上的普遍程度，但未给出任何统计数据或范围界定。",
    "作者断言“不到三十岁可以说还像孩子一样”“谁都不该选择三十岁以下的人”，未给出依据，也未说明是否适用于所有情形。",
    "提问者所说的“很多女孩是大叔控”本身是提问者的表述，本文未核验其是否成立，而是直接质疑该框架。",
    "本文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "可以说从古到今从来就不缺年龄差六岁以上的亲密关系，十岁以上的也谈不上什么罕见。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "为什么六岁？一方小学毕业，另一方幼儿园毕业",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "你们可以查一查历史上著名的夫妇，看看有多少是年龄差五岁以上的。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "孙中山比宋庆龄大27岁。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P016",
     "quote": "你们的女神赫本比她的灵魂伴侣罗伯特沃德斯大7岁。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P017",
     "quote": "所以不能简单的用“趋炎附势”来解释",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P018",
     "quote": "这反而是现代才有的独特现象。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P020",
     "quote": "现在会变成一种似乎“不正常”的东西被知乎拿来评头论足？",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P021",
     "quote": "谁说人就该选同龄人？",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P021",
     "quote": "基本上在这个时代，谁都不该选择三十岁以下的人",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P022",
     "quote": "光是心有不甘的吐槽人家正常选择权利本身就是不合格的幼稚表现。",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P023",
     "quote": "社科答集",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "婚恋社会学",
    "历史人物轶事",
    "舆论现象评论"
   ],
   "issue_candidates": [
    "年龄差婚恋是否异常",
    "“大叔控”标签的成立与否",
    "现代婚恋观的历史比较"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "反驳",
    "清单式举证"
   ],
   "object_candidates": [
    "孙中山",
    "宋庆龄",
    "周恩来",
    "邓颖超",
    "鲁迅",
    "许广平",
    "迭戈·里维拉",
    "弗里达",
    "达利",
    "里根",
    "肯尼迪",
    "杰奎琳",
    "居里夫妇",
    "马丁路德",
    "林肯",
    "纳尔逊曼德拉",
    "恩格斯",
    "赫本",
    "罗伯特沃德斯",
    "知乎"
   ],
   "working_keywords": [
    "大叔控",
    "老夫少妻",
    "年龄差",
    "六岁",
    "趋炎附势",
    "特异形态",
    "主流"
   ]
  },
  "notes": "本篇无图片节点，正文 23 段全部读完。P023“社科答集”未被 lexical 结构覆盖（walk_body 标记 text_tail_not_in_lexical），按简报第 3 节，此类“答集”字样属平台话题标签混入正文，已单列为 U007 并标记为非作者论述，未计入作者主张。brief 与正文重合，仅作导航。文中十三组年龄差数据未给出来源，已记入未决问题待外部核查。"
 },
 "c6a02357": {
  "analysis": {
   "question_context": "提问者（Q001）问：基督教徒能不能食血？作者不复述教义讨论，而是用一句正文加 8 张图片回应：把“能不能吃”悬置为“不好说”，转而主张“以下各老牌基督教国家都在吃”，其举证依赖随后的图片。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "以“一劳永逸的解决这个问题”开场，声明“能不能吃”不好说，但称以下各老牌基督教国家都在吃，并以下文图片为举证材料。",
     "role": "claim"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者对“基督教徒能不能食血”的规范性回答持保留态度，称“能不能吃”不好说。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者主张“以下各老牌基督教国家都在吃”，该主张的举证材料是随后的图片（图片内容未经核验）。",
     "evidence": [
      "E2"
     ]
    }
   ],
   "argument_steps": [
    "声明要“一劳永逸的解决这个问题”（P001）。",
    "把规范性问题“能不能吃”悬置为“不好说”（P001）。",
    "转而给出事实性主张“以下各老牌基督教国家都在吃”，其举证依赖随后的 8 张图片（P001 及 IMG001—IMG008）。"
   ],
   "concept_usage": [
    {
     "term": "食血",
     "meaning": "提问中的行为（食用血/血制品），作者不加界定直接沿用",
     "evidence": "P001",
     "ambiguity": "未说明指饮血、食血制品还是泛指"
    },
    {
     "term": "能不能吃",
     "meaning": "作者区分出的规范性/教义问题，并明确表示“不好说”，未作答",
     "evidence": "P001",
     "ambiguity": "作者未说明“不好说”的理由"
    },
    {
     "term": "老牌基督教国家",
     "meaning": "作者用以指称其举证对象的国别范围，具体是哪些国家仅见于未核验的图片",
     "evidence": "P001",
     "ambiguity": "所指国家名单在正文中不可见"
    }
   ],
   "examples_and_targets": [
    "8 张图片（IMG001—IMG008，asset.sooon.ai 上的 jpg）——作者用以举证“各老牌基督教国家都在吃”，图片内容未经核验（P001 之后）",
    "“老牌基督教国家”——作者主张的主体，具体名单本文正文未列出"
   ],
   "conditions": [
    "“能不能吃”不好说——作者明确回避规范性断定（P001）",
    "“以下各老牌基督教国家”所指范围取决于图片，正文未说明（P001）"
   ],
   "rhetoric_and_tone": "极简：正文仅一句 39 字，以“一劳永逸的解决这个问题”的夸张自许开场，随后把规范问题悬置、改用图片举证。举证责任完全落在图片上，语气简洁而不作论证。",
   "unresolved_questions": [
    "本篇含 8 个图片节点（IMG001—IMG008），图片内容未经核验，需人工/多模态复核；“各老牌基督教国家都在吃”这一主张的全部举证都在图片中，未经核验前该主张无法评估。",
    "正文未列出“各老牌基督教国家”的具体名单，也未说明所吃的是什么血/血制食品。",
    "作者称“能不能吃”不好说，但未说明依据（教义、教派差异或其它）。",
    "标题“基督教与食血”与正文一句话加图片的举证结构之间的关系，本文未说明。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "“能不能吃”不好说",
     "relation": "qualifies"
    },
    {
     "key": "E2",
     "paragraph_id": "P001",
     "quote": "但是以下各老牌基督教国家都在吃：",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "宗教与饮食戒律",
    "基督教研究",
    "饮食文化"
   ],
   "issue_candidates": [
    "基督教徒能否食血",
    "教义规定与实际饮食实践的差异"
   ],
   "text_function_candidates": [
    "答疑",
    "图片举证"
   ],
   "object_candidates": [
    "基督教徒",
    "老牌基督教国家"
   ],
   "working_keywords": [
    "食血",
    "能不能吃",
    "老牌基督教国家",
    "一劳永逸"
   ]
  },
  "notes": "本篇含 8 个图片节点（IMG001—IMG008），图片内容未经核验，故 status=needs_reread、image_checked=false。正文仅 1 段 39 字，已读完；该篇的全部举证都在图片中（正文以冒号引出），未经图像核验无法评估作者主张。brief 与正文首句重合，仅作导航。提问属提问者（Q001）。",
  "status": "needs_reread",
  "image_checked": False
 },
 "db480563": {
  "analysis": {
   "question_context": "提问者（Q001）问：如何看待微博话题 #女生节取代妇女节#？作者从“妇女”一词的命名逻辑入手，指出该词把婚姻意义抬得过高，主张若要改不如叫“女士节”，并借“正名”诉求谈到自我意识觉醒，最后批评国内对异见表达的过激反应。提问中的“女生节取代妇女节”口号属提问者语境，作者未就节日设置本身表态支持或反对。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "指出“妇女”一词把婚姻的意义抬得太高：女人被婚否分成两类，未结婚的加已结婚的就是全部女性；并以“为何不分成不穿裙子的和穿裙子的/已工作的和未工作的/睡着的和没睡着的”连串反问，指这种分类出于“女人嘛，还不就是那点事”的下意识。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "提出替代方案：如果要改，不如叫“女士节”，并释为“女而为士也，不敢不弘毅”。",
     "role": "action_advice"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "评估正名诉求：正名本身不急，应在正常框架内主张并等待结果；但该诉求出现本身可喜，说明人已意识到名字背后的问题，这以自我意识觉醒为前提——不觉醒就不会挑剔别人的称呼，也无力在意他人对自己的形象框定。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "转述并准备批评的一种国内思想：如果一种意见与既定主流意见不一样而又没希望立刻推翻主流意见，最好是不要表达出来。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "解释该思想背后的下意识：一旦有不同声音被公然听到，就认为此人已谋划好一切必要准备、到了“图穷匕乃现”“一鼓作气”“改天换日”的阶段；一旦有公开不同意见就等同于最后决战的危急时刻，若不激烈攻击扑灭，明天自己一派就要被拉下王座被诛九族。",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P006"
     ],
     "summary": "指出后果与实例：任何一点不一样的声音都会引发巨大的过激反应；并指本问题下急于捍卫自己熟知世界的手撕脚踹的大字报式答案，说明这种大清朝式的恐惧感有多严重。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "以半带调侃的评语收尾：世界对他们太残酷，每天都有无数可怕的言论吓煞人；也不知道是不是该同情。",
     "role": "conclusion"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P008"
     ],
     "summary": "文末另有“女性权利与女性人格构建”字样，疑为平台话题标签混入正文，非作者论述。",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为“妇女”这个词把婚姻的意义抬得太高了：女人被婚否分成两类，未结婚的加上已结婚的就是全部的女性。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者以连串反问质疑这种分类的唯一性（为何不分成不穿裙子的和穿裙子的、已工作的和尚未工作的、睡着的和没睡着的），并断言其无非是下意识地觉得“女人嘛，还不就是那点事”。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者主张如果要改名，不如叫“女士节”，并释其义为“女而为士也，不敢不弘毅”。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为正名本身不急，在正常框架内主张、等待正常程度出结果即可；但正名的诉求出现本身是一件可喜的事，表示人已经意识到名字背后的问题，这以自我意识觉醒为前提——不觉醒就不会挑剔别人对自己的称呼，也无力在意别人对自己的形象框定。",
     "evidence": [
      "E4",
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "被作者转述并批评的一种国内思想：如果一种意见与既定的主流意见不一样而又没希望立刻推翻主流意见，最好是不要表达出来。",
     "evidence": [
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者分析这种思想的机理：人们养成了下意识，一旦有不一样的声音被公然听到，就认定对方已谋划好一切必要准备、到了“图穷匕乃现”“改天换日”的阶段，把公开的不同意见等同于最后决战的危急时刻，若不激烈攻击扑灭，明天自己一派就要被拉下王座被诛九族。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为于是任何一点不一样的声音都会引发巨大的过激反应，并指本问题下急于捍卫自己熟知世界的手撕脚踹的大字报式答案说明这种大清朝式的恐惧感有多严重。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "questioned",
     "statement": "作者以调侃带不确定的评语收尾：世界对他们太残酷了，每天都有无数可怕的言论吓煞人，也不知道是不是该同情。",
     "evidence": [
      "E9"
     ]
    }
   ],
   "argument_steps": [
    "从词义入手：“妇女”以婚否穷举全部女性，把婚姻的意义抬得太高（P001）。",
    "以三组反问说明按婚否分类并不比按穿不穿裙子等更自然，指其出于“女人嘛，还不就是那点事”的下意识（P001）。",
    "提出替代命名：不如叫“女士节”，并给出“女而为士”的释义（P002）。",
    "评估正名诉求：正名本身不急，但其出现说明自我意识觉醒、意识到名字背后的问题（P003）。",
    "转述所要批评的国内思想：与主流不同而又无望立刻推翻主流时最好不要表达（P004）。",
    "解释该思想的下意识机理：把公开异见等同于改朝换代的最后决战（P005）。",
    "指出其后果并以本题下的答案为例，称之为大清朝式的恐惧感（P006）。",
    "以“也不知道是不是该同情”收尾（P007）。",
    "文末“女性权利与女性人格构建”字样，疑为平台标签（P008）。"
   ],
   "concept_usage": [
    {
     "term": "妇女",
     "meaning": "本文中被拆解为一个以婚否穷举女性的分类词，作者认为它把婚姻的意义抬得过高",
     "evidence": "P001",
     "ambiguity": "作者未讨论该词的法律或日常用法差异"
    },
    {
     "term": "正名",
     "meaning": "本文中指对“妇女节/女生节”名称的重新主张；作者认为正名本身不急，但其诉求的出现反映自我意识觉醒",
     "evidence": "P003",
     "ambiguity": "作者未说明“在正常框架内主张”的具体所指"
    },
    {
     "term": "自我意识觉醒",
     "meaning": "作者界定为：会挑剔别人对自己的称呼、在意别人对自己形象的框定",
     "evidence": "P003",
     "ambiguity": "未说明觉醒的判定标准"
    },
    {
     "term": "赫鲁晓夫",
     "meaning": "本文中借指被想象为已谋划好一切、准备“改天换日”的公开异见者，带讽刺色彩",
     "evidence": "P005",
     "ambiguity": "历史典故的取义由作者设定，非史实陈述"
    },
    {
     "term": "大清朝式的恐惧感",
     "meaning": "作者用以形容对公开异见的过激反应所反映的心态",
     "evidence": "P006",
     "ambiguity": "比喻性用法"
    }
   ],
   "examples_and_targets": [
    "微博话题 #女生节取代妇女节#——提问者提供的讨论对象（Q001），作者未就该话题本身表态",
    "“改名为女士节”——作者自己提出的替代方案（P002）",
    "“如果一种意见与既定的主流意见不一样而又没希望立刻推翻主流意见，最好是不要表达出来”——作者转述并批评的对象观点（P004）",
    "“赫鲁晓夫”“图穷匕乃现”“一鼓作气”“改天换日”“皇国危亡，在此一役”“被诛九族”——作者引用的历史/政治语汇，用作讽刺性类比（P005）",
    "“这问题下急于捍卫自己熟知的世界的这些手撕脚踹的大字报式答案”——作者观察到的实例与批评对象（P006）",
    "“女性权利与女性人格构建”——文末字样，疑为平台话题标签（P008）"
   ],
   "conditions": [
    "“如果要改，那不如叫‘女士节’吧”——条件句，改名为假设情形（P002）",
    "“在正常框架内主张，等待正常程度出结果就是了”——对主张方式与期待的条件限定（P003）",
    "“自我意识不觉醒，就不会挑剔别人对自己的称呼”——以觉醒为前提的条件句（P003）",
    "“如果一种意见与既定的主流意见不一样而又没希望立刻推翻主流意见”——被转述观点的条件（P004）",
    "“一旦有某种不一样的声音胆敢公然让人听到了”——条件句（P005）",
    "“也不知道是不是该同情”——明示不确定（P007）"
   ],
   "rhetoric_and_tone": "讽刺与反问为主的评论体：开篇用三组排比反问（“为何不分成……为啥不分成……为啥不分成……”）拆解“妇女”的分类逻辑；中段以“赫鲁晓夫”“图穷匕乃现”“皇国危亡，在此一役”“大清朝式的恐惧感”“大字报式答案”等历史政治语汇构成夸张化讽刺；结尾“也不知道是不是该同情”带调侃与不确定。称呼上对读者用“我们”“你们”混用，立场站在提倡正名诉求的一侧。",
   "unresolved_questions": [
    "文末 P008 仅“女性权利与女性人格构建”一行，未被 lexical 结构覆盖（walk_body 标记 text_tail_not_in_lexical），疑为平台话题标签混入正文，非作者论述。",
    "作者未直接就“#女生节取代妇女节#”这一微博话题表态支持或反对，只主张“如果要改，不如叫女士节”，此点与提问的直接关联需注意。",
    "“在正常框架内主张，等待正常程度出结果”中的“正常框架”“正常程度”所指为何，本文未说明。",
    "作者批评的“某种原因”未点名，其所说的“国内有一种很不知道怎么形容的思想”的主体范围本文未说明。",
    "P006 提到的“这问题下……的这些手撕脚踹的大字报式答案”属对具体页面内容的断言，需外部核查。",
    "本文无图片节点，无需图像核验。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "“妇女”这个词，把婚姻的意义抬得太高了。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P001",
     "quote": "无非是下意识的觉得“女人嘛，还不就是那点事”。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P002",
     "quote": "如果要改，那不如叫“女士节”吧。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P003",
     "quote": "正名本身不急，在正常框架内主张，等待正常程度出结果就是了。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P003",
     "quote": "表示人已经意识到名字背后的问题了",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P004",
     "quote": "最好是不要表达出来。",
     "relation": "contradicts"
    },
    {
     "key": "E7",
     "paragraph_id": "P005",
     "quote": "一旦有了公开的不同意见，那就立刻就是最后决战的危急时刻",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P006",
     "quote": "就知道这种大清朝式的恐惧感有多严重了",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P007",
     "quote": "也不知道是不是该同情。",
     "relation": "qualifies"
    },
    {
     "key": "E10",
     "paragraph_id": "P008",
     "quote": "女性权利与女性人格构建",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "性别议题",
    "语言与命名政治",
    "社会舆论现象"
   ],
   "issue_candidates": [
    "妇女/女生节的命名",
    "以婚姻状态定义女性",
    "公开异见表达的社会反应"
   ],
   "text_function_candidates": [
    "答疑",
    "评论",
    "批评",
    "讽刺"
   ],
   "object_candidates": [
    "微博",
    "知乎",
    "妇女",
    "女士",
    "赫鲁晓夫",
    "大清（朝）"
   ],
   "working_keywords": [
    "妇女",
    "女士节",
    "正名",
    "自我意识觉醒",
    "赫鲁晓夫",
    "图穷匕乃现",
    "大清朝式的恐惧感",
    "大字报式答案"
   ]
  },
  "notes": "本篇无图片节点，正文 8 段全部读完。P008“女性权利与女性人格构建”未被 lexical 结构覆盖（walk_body 标记 text_tail_not_in_lexical），按简报第 3 节，此类短行疑为平台话题标签混入正文，已单列为 U008 并标记为非作者论述。brief 与正文首段重合，仅作导航。P004 所述“国内有一种……思想”是被作者转述并批评的对象观点，已用 opponent_view + attribution=opponent 记录，未归给作者。提问（Q001）的话题框架属提问者，作者未直接表态。"
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
