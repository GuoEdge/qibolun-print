# -*- coding: utf-8 -*-
"""批次 r001-b0071 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0071.sessions.py            # 写 out/r001-b0071.out.jsonl
  python3 records/r001-b0071.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0071"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0071.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
  "28128546": {
   "analysis": {
    "question_context": "提问者问「人类社会的终极目标是什么？」（Q001），属提问者语境，非作者立场。作者未直接给出某个具体终极目标，而是先区分「终极目标」的双重含义并指出该问法本身可被解构。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001"
      ],
      "summary": "提出人类社会的永恒任务是保持幸存。",
      "role": "claim"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P002",
       "P003"
      ],
      "summary": "指出「终极目标」有双重意义；第一重是人们自定的终极目标，实为服务于最大幸存机会的工具。",
      "role": "definition"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P004",
       "P005"
      ],
      "summary": "以沙漠旅人瞄准远方沙丘导航作类比，说明该目标是导航手段而非终点，并会随时过境迁而翻覆。",
      "role": "example"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P006",
       "P007",
       "P008"
      ],
      "summary": "第二重是这条曲折道路总体指向的遥远彼岸；以两万米高空俯瞰为喻，承认难以由几千年轨迹断言方向，但人类仍相信它有方向。",
      "role": "qualification"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P009",
       "P010"
      ],
      "summary": "结论：人类社会只存在对终极目标的信念，并无真正意义上的终极目标，只有被加冕为终极目标的当下政治正确。",
      "role": "conclusion"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "人类社会有一个永恒任务，即保持幸存。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "人类自定的「终极目标」在功能上是为最大幸存机会服务的工具，而非目的本身。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "这种「终极目标」常因时过境迁而翻覆。",
      "evidence": [
       "E3"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "人类走出的道路虽难由残缺轨迹断言方向，但人类仍相信它指向某个方向。",
      "evidence": [
       "E4"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "人类社会只存在对终极目标的信念，并没有真正意义上的终极目标可言。",
      "evidence": [
       "E5"
      ]
     },
     {
      "claim_id": "C006",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "实际被当作终极目标的，只是眼下被加冕为终极目标的政治正确。",
      "evidence": [
       "E6"
      ]
     }
    ],
    "argument_steps": [
     "前提：人类社会的永恒任务是保持幸存（P001）。",
     "定义拆分：「终极目标」有双重意义（P002）。",
     "第一重：自定的终极目标是服务最大幸存机会的工具（P003）。",
     "类比：迷路旅人瞄准远方沙丘只为脱离原险境，下一险境再另瞄准一座沙丘（P004）。",
     "推论：这类目标会因时过境迁而翻覆（P005）。",
     "第二重：一路走出的盘旋道路总体指向的遥远彼岸（P006）。",
     "让步：几千年残破轨迹不足以断言方向，但人类仍相信它有方向（P008）。",
     "结论：只有对终极目标的信念，没有真正的终极目标，只剩下被加冕的当下政治正确（P009、P010）。"
    ],
    "concept_usage": [
     {
      "term": "终极目标（第一重）",
      "meaning": "人类自己因各种原因自定的目标，功能上是为最大幸存机会服务的导航工具。",
      "evidence": "P003",
      "ambiguity": "作者明说其「存在双重意义」，须与第二重区分，不可合并理解。"
     },
     {
      "term": "终极目标（第二重）",
      "meaning": "人类在短视导航逻辑下实际走出的曲折道路所总体指向的遥远彼岸。",
      "evidence": "P006",
      "ambiguity": "作者承认只能「相信有指向」，未给出该方向的内容。"
     },
     {
      "term": "幸存",
      "meaning": "被称作人类社会的永恒任务，是该文全部论证的出发点。",
      "evidence": "P001",
      "ambiguity": "未界定幸存的单位与标准。"
     },
     {
      "term": "政治正确",
      "meaning": "眼下被加冕为终极目标的那个「下一个沙丘」。",
      "evidence": "P010",
      "ambiguity": "此处为作者对当下目标的贬称式用法，未举例。"
     }
    ],
    "examples_and_targets": [
     "沙漠里迷路的旅人瞄准远方沙丘以维持行进方向——类比，用于说明终极目标的工具性（P004）。",
     "飞到两万米高空往下看人类的导航逻辑——比喻性视角，用于说明总体轨迹仍有指向（P007）。",
     "被加冕为终极目标的政治正确——作者指认的替代物/批评对象（P010）。"
    ],
    "conditions": [
     "第一重终极目标的工具性论断以「无论人类自己因为什么原因而自定」为无条件前提（P003）。",
     "轨迹方向的判断附条件：虽「很难因为短短几千年残破不全……就断言如何」，但人类仍相信其有指向（P008）。",
     "作者用「应该明白了」（P009）预设读者已接受前述机制，属推论式引导而非独立证据。"
    ],
    "rhetoric_and_tone": "第二人称引导（「如果你飞到两万米的高空往下看」「你就应该明白了」），以沙漠沙丘作贯穿性比喻；结论处用「加冕」带轻微讽意，整体为冷峻的机制讲解语气，非训诫。",
    "unresolved_questions": [
     "第二重「遥远彼岸」具体指向什么，正文未说明。",
     "「政治正确」被加冕为终极目标的具体实例，正文未举出。",
     "「保持幸存」的主体单位（人类整体/文明/物种）与判定标准未界定。",
     "该回答与提问「人类社会的终极目标是什么」之间的关系是解构而非正面作答，需研究者注意。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "人类社会有一个永恒任务，就是保持幸存。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P003",
      "quote": "其实是一种为最大幸存机会服务的工具",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P005",
      "quote": "这种“终极目标”，常因时过境迁而翻覆。",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P008",
      "quote": "但人类仍然是相信它有指向某个方向",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P009",
      "quote": "却并没有真正意义上的终极目标可言",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P010",
      "quote": "眼下被加冕为终极目标的政治正确而已",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "社会理论",
     "历史哲学",
     "政治哲学"
    ],
    "issue_candidates": [
     "人类社会终极目标",
     "目标与幸存的关系",
     "政治正确的功能"
    ],
    "text_function_candidates": [
     "答疑",
     "概念辨析",
     "论辩"
    ],
    "object_candidates": [
     "人类社会",
     "人类"
    ],
    "working_keywords": [
     "终极目标",
     "幸存",
     "沙丘",
     "政治正确",
     "彼岸",
     "导航"
    ]
   },
   "notes": "无图片节点。正文10段完整。question 为提问者所问，作者未正面给出某个终极目标，而是区分双重含义并解构该问法；本记录未把提问者预设当作作者立场。"
  },
  "1503fedf": {
   "analysis": {
    "question_context": "提问者问「如何评价『连锁餐厅成功毁掉了中国地方菜』的观点？」（Q001），该命题属提问者转述的待评价观点。作者先重构「地方菜到底是什么」，再判定连锁餐厅与地方菜消失之间不是因果关系。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001",
       "P002"
      ],
      "summary": "把问题转为先界定「地方菜」与「地方菜系」如何出现。",
      "role": "transition"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P003",
       "P004"
      ],
      "summary": "提出分析框架：生鲜食材、耐储食材、味觉（文化）审美三方面，并给出一道菜的定义。",
      "role": "definition"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P005",
       "P006",
       "P007",
       "P008"
      ],
      "summary": "暂置味觉审美；界定耐储食材并称菜系实为耐储食材池与域内生鲜食材及生活方式结合的产物；决定菜的生命的是最不耐储运的成分。",
      "role": "definition"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P009"
      ],
      "summary": "提出地方菜生存只取决于该项食材能否方便外运。",
      "role": "claim"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P010",
       "P011",
       "P012"
      ],
      "summary": "以云南见手青为唯一举例，说明不耐储运食材如何催生地方名菜；并给出产地属性与储运限制不变则菜一直是地方的这一条件。",
      "role": "example"
     },
     {
      "unit_id": "U006",
      "paragraph_refs": [
       "P013",
       "P014",
       "P015"
      ],
      "summary": "连锁餐厅要求全区域标准化故不能用地域性太强的食材，与地方菜井水不犯河水；地方菜消失只是错觉，两事同时发生而非因果。",
      "role": "rebuttal"
     },
     {
      "unit_id": "U007",
      "paragraph_refs": [
       "P016",
       "P017",
       "P018",
       "P019"
      ],
      "summary": "地方菜同样要卖给出价最高者；交通改善后土特产外运省城乃至海外，相应做法随之而去，地方菜是搬家到省城且规模往往扩大。",
      "role": "reason"
     },
     {
      "unit_id": "U008",
      "paragraph_refs": [
       "P020",
       "P021"
      ],
      "summary": "同一逻辑也解释连锁店得以深入地县；两者是同一原因的两个不同结果。",
      "role": "conclusion"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "决定菜的生命的是菜中最不耐储运的那个成分。",
      "evidence": [
       "E4"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "地方菜的生存只取决于一个关键因素，即这里的该项食材能否方便地运输到别处。",
      "evidence": [
       "E5"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "只要生鲜食材的独特产地属性不变且储运手段仍有限制，这道菜就会一直是地方的。",
      "evidence": [
       "E6"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "连锁餐厅要求全经营区域高度一致，因此不能使用任何地域性太强的食材，与地方菜井水不犯河水。",
      "evidence": [
       "E7"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "opponent_view",
      "attribution": "opponent",
      "modality": "questioned",
      "statement": "「连锁餐厅消灭了地方菜」是一种直观感受，作者转述之并指出地方菜正在消失的感觉是错觉。",
      "evidence": [
       "E8"
      ]
     },
     {
      "claim_id": "C006",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "地方菜的迁徙与连锁店的入侵并非后者驱逐前者，而是同一原因的两个不同结果。",
      "evidence": [
       "E11"
      ]
     },
     {
      "claim_id": "C007",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "地方菜并没有消失，而是搬家去了省城，规模往往还反而扩大了。",
      "evidence": [
       "E9",
       "E10"
      ]
     }
    ],
    "argument_steps": [
     "先立定义：一道菜＝生鲜/耐储食材经特定味觉审美指引下的烹饪加工（P004）；味觉审美暂时按下不表（P005）。",
     "界定耐储食材为干制、腌制、熏制、精炼之后的食材，常因商业流通关系构成菜系底色（P006）。",
     "断言菜系本质上是耐储食材池与域内生鲜食材及生活方式结合的产物（P007）。",
     "推出单一关键变量：最不耐储运的成分决定菜的生命，即能否方便外运（P008、P009）。",
     "举例：云南见手青不耐储存、最好只在本地食用，故自然养出一系列地方菜与地方名菜（P010）。",
     "条件限定：产地属性与储运限制不变，菜就一直是地方的（P011、P012）。",
     "反驳直觉：连锁餐厅因标准化不能用地域性强的食材，与地方菜井水不犯河水（P013）。",
     "解释错觉来源并给出机制：地方菜也追求最高售价，交通改善使其外运省城与海外，做法随之跟去（P016、P017）。",
     "结论：地方菜搬家且规模扩大，连锁店亦因交通提升深入地县，二者同因异果（P018、P019、P020、P021）。"
    ],
    "concept_usage": [
     {
      "term": "地方菜",
      "meaning": "由本地不耐储运的生鲜食材在本地搭配耐用食材、用本地手段实践出的最佳食用方案之结果。",
      "evidence": "P009",
      "ambiguity": "作者把它与「地方名菜」并用，二者关系未明确区分。"
     },
     {
      "term": "地方菜系",
      "meaning": "一组特定耐储食材（往往作为调味料）池，与域内各地不耐储生鲜食材及生活方式结合的产物。",
      "evidence": "P007",
      "ambiguity": "P007句末以「的产物。」结束，缺中心语，疑似渲染截断或原文脱字，解读需回查语料。"
     },
     {
      "term": "耐储食材",
      "meaning": "干制、腌制、熏制、精炼之后的食材。",
      "evidence": "P006",
      "ambiguity": "未给判定标准。"
     },
     {
      "term": "生命线",
      "meaning": "地方菜得以成为地方的条件，即食材无法方便外运。",
      "evidence": "P012",
      "ambiguity": "修辞性表述，非严格术语。"
     }
    ],
    "examples_and_targets": [
     "云南的见手青——作者唯一具体例证，用作论证不耐储食材催生地方菜的证据（P010、P011）。",
     "城际高速公路和铁路、冷链、真空包装、航空货运——作者列举的外运条件（P017）。",
     "「连锁餐厅消灭了地方菜」的直观感受——被反驳的观点（P014、P015）。"
    ],
    "conditions": [
     "分析范围限定：味觉（文化）审美「暂时按下不表」，故框架不含味觉变量（P005）。",
     "地方菜持续为地方的条件：生鲜食材「出了云南的特定产地就无法生长」，且储运手段仍有限制（P011）。",
     "外运行为以「一旦交通改善，食材可以在合理的成本之内输送到更大的区域」为前提（P016）。",
     "作者用「几乎肯定会找到一个比产地更高的售价」的强度词，保留例外空间（P016）。"
    ],
    "rhetoric_and_tone": "自问自答式推进（「到底怎样才会出现一道地方菜？」「那么是什么给人造成了……感觉呢？」），以「井水不犯河水」「搬了家」「触须」等口语比喻收束；结尾四段短句递进，语气是论断式的解惑，无讥刺。",
    "unresolved_questions": [
     "P007 末尾「的产物。」缺少中心语，需回查语料确认是否有截断或脱字。",
     "「味觉（文化）审美」被明确暂时按下不表，作者未说明它如何影响地方菜形成。",
     "例子只有云南见手青一例，其余菜系未举，概括力范围待判。",
     "作者未说明提问中「中国」这一限定是否影响其结论。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P002",
      "quote": "到底怎样才会出现一道地方菜？",
      "relation": "context"
     },
     {
      "key": "E2",
      "paragraph_id": "P004",
      "quote": "一道菜，就是生鲜/耐储食材，在特定的味觉审美的指引下经由烹饪过程加工而成的食物。",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P006",
      "quote": "它们常常因为特定的商业流通关系构成一个菜系的底色。",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P008",
      "quote": "决定菜的生命的，是菜中最不耐储运的那个成分。",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P009",
      "quote": "所有的地方菜的生存，只决定于一个关键因素，是否我这里的这一项食材无法方便的运输到别处？",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P011",
      "quote": "这道菜就会一直是地方的",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P013",
      "quote": "因此它将不能使用任何地域性太强的食材",
      "relation": "supports"
     },
     {
      "key": "E8",
      "paragraph_id": "P014",
      "quote": "甚至是“连锁餐厅消灭了地方菜”的直观感受呢？",
      "relation": "contradicts"
     },
     {
      "key": "E9",
      "paragraph_id": "P018",
      "quote": "地方菜并没有消失，而是去了省城。它搬家了。",
      "relation": "supports"
     },
     {
      "key": "E10",
      "paragraph_id": "P019",
      "quote": "甚至，规模往往还反而扩大了。",
      "relation": "supports"
     },
     {
      "key": "E11",
      "paragraph_id": "P021",
      "quote": "而是同一个原因的两个不同结果而已",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "饮食文化",
     "经济地理",
     "商业分析"
    ],
    "issue_candidates": [
     "连锁餐厅与地方菜的关系",
     "地方菜的形成条件",
     "食材储运与菜系分布"
    ],
    "text_function_candidates": [
     "答疑",
     "概念辨析",
     "反驳",
     "经验总结"
    ],
    "object_candidates": [
     "中国",
     "云南",
     "连锁餐厅",
     "地方菜系"
    ],
    "working_keywords": [
     "地方菜",
     "菜系",
     "生鲜食材",
     "耐储食材",
     "见手青",
     "冷链",
     "省城"
    ]
   },
   "notes": "无图片节点。正文21段完整。P007 末尾「的产物。」缺中心语，疑为渲染截断或原文脱字，已在 unresolved_questions 登记。提问中的「连锁餐厅毁掉地方菜」为用户待评价观点，本记录以 opponent_view/questioned 处理，未归给作者。"
  },
  "126518f7": {
   "analysis": {
    "question_context": "提问者问「超高层建筑未来的发展，面临哪些挑战？」（Q001）。作者给出单一核心回答：需求疲软；并进一步论证超高建筑除特殊实用需求外唯一核心价值是纪念碑，而该价值可由其他形式更优地实现。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001"
      ],
      "summary": "直接给出结论性回答：超高建筑发展的最大挑战是需求疲软。",
      "role": "claim"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P002"
      ],
      "summary": "理由：人类已稍微成熟，渐渐意识到无需依靠超高建筑展现实力。",
      "role": "reason"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P003"
      ],
      "summary": "限定超高建筑的价值：除电视塔这类特殊实用需求外，唯一核心价值是纪念碑；而纪念碑价值不如直接做大地艺术或纯雕塑，若要兼实用则不如做歌剧院、图书馆、体育场。",
      "role": "qualification"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P004",
       "P005"
      ],
      "summary": "把上时代赛造摩天楼判为人类幼稚病；如今不流行且无利益冲动，便须高度重视性价比；技术问题给足成本并不难突破，但讲性价比就尴尬。",
      "role": "rebuttal"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "超高建筑发展面临的最大挑战是需求疲软。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "人类已渐渐意识到没有必要依靠超高建筑来展现实力。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "除电视塔这类特殊实用需求外，超高建筑唯一的核心价值是作为「纪念碑」；而纪念碑价值不如直接做大地艺术或纯雕塑，若要兼有实用价值则不如做歌剧院、图书馆、体育场这类公共建筑。",
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
      "statement": "上一个时代比着赛造摩天大楼是人类幼稚病的表现。",
      "evidence": [
       "E5"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "只要给足够的成本，超高建筑的技术问题并没有那么难突破；难点在性价比。",
      "evidence": [
       "E6",
       "E7"
      ]
     }
    ],
    "argument_steps": [
     "结论先行：最大挑战是需求疲软（P001）。",
     "理由：人类成熟化，不再需要靠超高建筑展现实力（P002）。",
     "价值分析：超高建筑除电视塔等特殊实用需求外，唯一核心价值是纪念碑（P003）。",
     "替代方案比较：纪念碑价值宜用大地艺术或纯雕塑实现；要兼实用则宜用歌剧院、图书馆、体育场（P003）。",
     "定性：上一时代的摩天楼竞赛是幼稚病，如今不流行（P004）。",
     "转向成本视角：无利益冲动后须重视性价比，技术问题在足够成本下不难突破（P004）。",
     "落点：一讲性价比就尴尬（P005）。"
    ],
    "concept_usage": [
     {
      "term": "需求疲软",
      "meaning": "被指为超高建筑发展最大挑战的需求侧问题。",
      "evidence": "P001",
      "ambiguity": "未给需求疲软的成因或数据。"
     },
     {
      "term": "纪念碑",
      "meaning": "作者认定超高建筑在特殊实用需求之外唯一的核心价值，即以建筑体量作象征。",
      "evidence": "P003",
      "ambiguity": "加引号，作者未界定纪念碑的判定标准。"
     },
     {
      "term": "幼稚病",
      "meaning": "对上一时代各国比着赛造摩天大楼的定性。",
      "evidence": "P004",
      "ambiguity": "评价性用语，未举具体建筑或国家。"
     },
     {
      "term": "性价比",
      "meaning": "在失去利益冲动后衡量超高建筑是否值得的尺度。",
      "evidence": "P004",
      "ambiguity": "作者未给出衡量口径。"
     }
    ],
    "examples_and_targets": [
     "电视塔——作者承认的特殊实用需求例外（P003）。",
     "大地艺术、纯雕塑——作者提出的纪念碑价值替代形式（P003）。",
     "歌剧院、图书馆、体育场——作者提出的兼实用价值替代形式（P003）。",
     "上一时代比着赛造摩天大楼——被贬为幼稚病的对象（P004）。"
    ],
    "conditions": [
     "价值判断的例外条件：「除了拿来满足电视塔这种特殊的实用需求之外」（P003）。",
     "替代建议带条件：「如果要兼有建筑的实用价值，则不如做……」（P003）。",
     "技术判断带条件：「其实只要给足够的成本」（P004）。",
     "时间限定：摩天楼竞赛被限定为「上一个时代」，流行性判断限于当下（P004）。"
    ],
    "rhetoric_and_tone": "短段递进、结论先行；以「人类幼稚病」「小孩子的事」「尴尬了」等降格比喻与口语化评价表达贬抑，属评论性调侃语气。",
    "unresolved_questions": [
     "未给出任何具体超高层建筑、城市或数据支撑需求疲软的判断。",
     "「人类已经稍微成熟一些」的主体与判据未说明。",
     "「纪念碑」与「大地艺术/纯雕塑」的比较未给出成本或效果依据。",
     "提问所问的「未来」时间尺度未界定。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "超高建筑发展的最大挑战，是需求疲软。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P002",
      "quote": "没有必要依靠超高建筑来展现什么实力",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P003",
      "quote": "唯一的核心价值就是作为“纪念碑”",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P003",
      "quote": "不如直接做大地艺术或者纯雕塑",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P004",
      "quote": "其实是一种人类幼稚病的表现而已",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P004",
      "quote": "只要给足够的成本，超高建筑的技术问题并没有那么难突破。",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P005",
      "quote": "但是要讲起“性价比”，那就尴尬了。",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "建筑",
     "城市建设",
     "经济社会评论"
    ],
    "issue_candidates": [
     "超高层建筑的未来挑战",
     "摩天大楼的象征价值",
     "建筑性价比"
    ],
    "text_function_candidates": [
     "答疑",
     "评论",
     "批评"
    ],
    "object_candidates": [
     "电视塔",
     "歌剧院",
     "图书馆",
     "体育场",
     "摩天大楼"
    ],
    "working_keywords": [
     "超高建筑",
     "摩天大楼",
     "需求疲软",
     "纪念碑",
     "性价比",
     "大地艺术"
    ]
   },
   "notes": "无图片节点。正文5段完整。全文为短评式答疑，未举具体建筑或数据；「人类幼稚病」「小孩子的事」为作者评价性用语，本记录如实记为作者判断而未作价值裁决。"
  },
  "4d268f38": {
   "analysis": {
    "question_context": "提问者问「为什么身为右派的川普反而成了民粹？」（Q001），该问法预设川普属右派且被指为民粹。作者未接受该预设，改从程序与定义层面主张选票民主政治本质上就是民粹政治，并指出「民粹」被用作专指自己不喜欢那一派的说法。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001",
       "P002"
      ],
      "summary": "提出核心判断：选票民主政治本质上就是民粹政治；任何党与意识形态在此制度下胜出就必定是民粹。",
      "role": "claim"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P003"
      ],
      "summary": "称这是程序与定义在本质上决定的；人们另造说法用民粹专指自己不喜欢的一派，实为抹杀其选民的「理性公民」身份。",
      "role": "reason"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P004",
       "P005",
       "P006"
      ],
      "summary": "论证非民粹派别与其对立面无本质区别；中立观点下没有有效指标作划分；差别只是有无无视部分民意的本钱，属机会性而非纲领性；多数「非民粹派别」只是留存冗余安全感的民粹派别（以兜里有钱作类比）。",
      "role": "rebuttal"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P007",
       "P008",
       "P009"
      ],
      "summary": "给出严格定义：只有无论选情如何都纲领性抗拒民众直接多数意见中非理性部分的派别才算非民粹政党；在选票民主下只有能不在乎席位、纯粹关注表达立场的政党才有此属性，例如tw以前的新党和日共；一旦争夺执政权即丧失该地位。",
      "role": "definition"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P010",
       "P011",
       "P012"
      ],
      "summary": "结论：这类坚持立场的党派本应是选票民主的政党模范，但恰恰因此选不赢；能赢的不该，应该的不能赢；以英文短语收束。",
      "role": "conclusion"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "选票民主政治本质上就是民粹政治。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "无论哪个党、什么意识形态，只要在选票民主制度下胜出，就必定是民粹。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "用民粹专指自己不喜欢的那一派，与其说是评价领导人、党派，不如说是为了抹杀其选民的「理性公民」身份。",
      "evidence": [
       "E3"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "在观点中立的前提下，没有有效指标可以把号称「非民粹」的那一派与其对立面划分为非民粹。",
      "evidence": [
       "E4"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "非民粹派别之所以显得非民粹，只是自恃对手弱小而有更大本钱无视部分直接民意，这是机会性的而非纲领性的。",
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
      "statement": "严格意义上只有无论选情如何都纲领性抗拒民众直接多数意见中非理性部分的派别，才可以被归类为非民粹政党。",
      "evidence": [
       "E7"
      ]
     },
     {
      "claim_id": "C007",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "在选票民主制度下，只有能不在乎自己选票席位、纯粹关注表达立场的政党才可拥有非民粹属性，如tw以前的新党和日共。",
      "evidence": [
       "E8"
      ]
     },
     {
      "claim_id": "C008",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "predicted",
      "statement": "这类政党一旦开始争夺执政权，也一样会立刻丧失非民粹地位。",
      "evidence": [
       "E9"
      ]
     },
     {
      "claim_id": "C009",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "能赢的恰恰是不该的，应该的恰恰不能赢。",
      "evidence": [
       "E11"
      ]
     }
    ],
    "argument_steps": [
     "提出主张：选票民主政治本质上就是民粹政治（P001）。",
     "全覆盖推论：任何党与意识形态只要胜出就必定是民粹（P002）。",
     "给出理由：程序与定义在本质上决定；「民粹」标签的实际功能是抹杀对方选民的理性公民身份（P003）。",
     "对称性反驳：号称非民粹的一派在迎合与鼓动选民上与对立面没有本质区别（P004）。",
     "指标质疑：观点中立下没有有效指标作划分（P004）。",
     "归因改写：差别只在有无无视部分民意的本钱，属机会性非纲领性（P004、P005）。",
     "类比：兜里有钱时敢坚持己见，口袋空空就客户导向；看似判若两人，其实同一性格算法包含两个情境设定（P006）。",
     "严格定义：纲领性抗拒多数非理性部分者才是非民粹政党（P007）。",
     "举例：tw以前的新党与日共（P008）。",
     "条件反转：一旦争夺执政权即丧失该地位（P009）。",
     "结论：此类党派本是制度模范却选不赢，能赢的不该、应该的不能赢（P010、P011）。"
    ],
    "concept_usage": [
     {
      "term": "民粹",
      "meaning": "在选票民主程序下胜出者必然具备的属性，被作者视为该制度的本质属性而非某一派的特征。",
      "evidence": "P001",
      "ambiguity": "作者既称其为程序与定义决定，又批评该词被用作贬斥标签，两种用法并存。"
     },
     {
      "term": "非民粹政党",
      "meaning": "严格意义上指无论选情如何都纲领性抗拒民众直接多数意见中非理性部分的派别。",
      "evidence": "P007",
      "ambiguity": "作者自设的窄定义，与日常用法不同，作者已标「严格意义上」。"
     },
     {
      "term": "机会性的/纲领性的",
      "meaning": "作者用于区分无视民意的本钱来自暂时处境还是来自坚持的立场。",
      "evidence": "P005",
      "ambiguity": "未给判定这两种性质的判据。"
     },
     {
      "term": "冗余安全感",
      "meaning": "被称为多数「非民粹派别」的真实特征，即有余裕时敢于坚持己见。",
      "evidence": "P006",
      "ambiguity": "以比喻方式提出，未量化。"
     }
    ],
    "examples_and_targets": [
     "tw以前的新党和日共——作者举出的、符合其非民粹定义的政党例子（P008）。",
     "号称「非民粹」的那一派——被作者反驳的对手方（P004）。",
     "兜里有钱就自信、口袋空空就客户导向——作者类比材料（P006）。",
     "提问中的川普与被称民粹的现象——作者未直接讨论该人物，仅以制度层面回应（Q001）。"
    ],
    "conditions": [
     "全称判断的适用范围限于「在这个制度下」，即选票民主制度之内（P002）。",
     "对称性判断以「在观点中立的前提下」为条件（P004）。",
     "政党非民粹属性的前提是「能够不在乎自己的选票席位、只纯粹关注表达立场」（P008）。",
     "丧失该属性的触发条件是「一旦它们要开始争夺执政权」（P009）。"
    ],
    "rhetoric_and_tone": "论断式短句推进，结尾用反讽式对称句与英文收束（「Poetic irony.」）；使用「黑色幽默」「悲哀」「客户导向」等带情绪词，整体为论辩性、讥刺性的政治评论语气；把 tw 作为地区简称使用。",
    "unresolved_questions": [
     "作者未直接回答提问中的川普与右派问题，二者关系留白。",
     "「tw」为地区简称，需回查语料确认原写法与所指（正文用「tw以前的新党」）。",
     "作者既称民粹由程序与定义决定、又称该词被用作抹杀标签，两种用法需研究者复核是否冲突。",
     "日共「该有几帕就几帕」为音译/口语说法，所指未说明。",
     "非民粹政党的严格定义未给出「非理性部分」的判定标准。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "选票民主政治，本质上就是民粹政治。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P002",
      "quote": "在这个制度下只要胜出，就必定是民粹",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P003",
      "quote": "倒不如是为了抹杀其选民的“理性公民”身份",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P004",
      "quote": "你根本没有有效的指标去将其划分为“非民粹”",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P004",
      "quote": "只不过是自恃对手弱小，于是有更大的无视直接民意里的某些部分的本钱罢了",
      "relation": "qualifies"
     },
     {
      "key": "E6",
      "paragraph_id": "P005",
      "quote": "那是机会性的，不是纲领性的。",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P007",
      "quote": "可以被归类为非民粹政党",
      "relation": "supports"
     },
     {
      "key": "E8",
      "paragraph_id": "P008",
      "quote": "譬如tw以前的新党和日共",
      "relation": "supports"
     },
     {
      "key": "E9",
      "paragraph_id": "P009",
      "quote": "也一样会立刻丧失这样的地位",
      "relation": "supports"
     },
     {
      "key": "E10",
      "paragraph_id": "P010",
      "quote": "但偏偏黑色幽默的是——就是这样，它们才选不赢。",
      "relation": "supports"
     },
     {
      "key": "E11",
      "paragraph_id": "P011",
      "quote": "能赢的恰恰是不该的，应该的恰恰不能赢。",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "政治学",
     "政制比较",
     "政治评论"
    ],
    "issue_candidates": [
     "民粹与选票民主的关系",
     "非民粹政党的界定",
     "政党立场与选举胜负"
    ],
    "text_function_candidates": [
     "答疑",
     "论辩",
     "概念辨析",
     "批评"
    ],
    "object_candidates": [
     "川普",
     "新党",
     "日共",
     "tw",
     "选票民主制度"
    ],
    "working_keywords": [
     "民粹",
     "非民粹",
     "选票民主",
     "纲领性",
     "机会性",
     "理性公民"
    ]
   },
   "notes": "无图片节点。正文12段完整。提问预设「川普属右派且是民粹」，作者未接受该预设亦未直接评价川普，本记录未把提问预设归给作者。P008 使用地区简称「tw」，已在 unresolved_questions 登记待回查原写法。"
  },
  "7a185bd7": {
   "analysis": {
    "question_context": "提问者自述为十三岁女生，不爱追星看综艺、喜欢研究古埃及，问「是不是心理不正常」（Q001），这是提问者的自我怀疑。作者否认「不正常」这一说法，改称其为「不寻常、不普通」，并从中国文化与庇护性法则角度说明突出的风险，最后给出两种处境的分类与劝告。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001",
       "P002"
      ],
      "summary": "纠正用词：这叫不寻常、不普通（common），不叫不正常（normal）。",
      "role": "definition"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P003",
       "P004"
      ],
      "summary": "解释成因：中国文化看重「常」的正面价值，是对「法不责众」这条庇护性法则的极端利用；藏身于正态分布的方差中安全，突出则会暴露。",
      "role": "reason"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P005",
       "P006",
       "P007"
      ],
      "summary": "第一重危险：即使当下评价体系鼓励这种突出，评价体系一变即可能由褒转贬，而大多数因法不责众不受波及。",
      "role": "reason"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P008",
       "P009"
      ],
      "summary": "第二重危险：在某派评价体系中正面突出，在其敌人眼里即为负面突出；而关心现实势力的派别都不会把大多数人划到对立面。",
      "role": "reason"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P010",
       "P011"
      ],
      "summary": "小结：两重危险叠加密不透风，任何角度的突出都暴露在交叉火力下；最安全的是成为大多数中的一员、成为「常」。",
      "role": "conclusion"
     },
     {
      "unit_id": "U006",
      "paragraph_refs": [
       "P012",
       "P013"
      ],
      "summary": "行动劝告：不必愤愤不平，应把这一点当作既定前提来考虑选择；无论因何异于多数都要意识到其中隐含的危险，父母在要求子女出人头地前也应先想清楚。",
      "role": "action_advice"
     },
     {
      "unit_id": "U007",
      "paragraph_refs": [
       "P014",
       "P015",
       "P016",
       "P017"
      ],
      "summary": "提出追问（是否准备承受风险、基于何理由），并列出第一种情形：你没得选——天赋异禀、继承王位或被命运放在特定位置上，注定不能平常；这既不幸也幸运，因为不必再想意义与代价问题。",
      "role": "qualification"
     },
     {
      "unit_id": "U008",
      "paragraph_refs": [
       "P018",
       "P019",
       "P020"
      ],
      "summary": "第二种情形：有得选，则选了就要认，不要出人头地后又埋怨过不了普通人的生活；以当偶像被粉丝反噬为例；文末标「（未完，待续）」。",
      "role": "action_advice"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "提问者的情形属于「不寻常、不普通（common）」，不叫作「不正常（normal）」。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "中国文化里把「常」的正面价值看得很重，这是对「法不责众」这条庇护性法则的极端利用造成的。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "突出会带来两重危险：评价体系变化可使今日受鼓励的突出转为负面；且在一派眼中正面突出即在其敌人眼中负面突出，而各派都不会把大多数人划到对立面。",
      "evidence": [
       "E3",
       "E4",
       "E5"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "所有角度的突出都是将自己暴露在交叉火力之下，最安全的是成为大多数中的一员。",
      "evidence": [
       "E6",
       "E7"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "不应愤愤不平，只能以此为既定和永久的事实前提来考虑自己的选择；异于多数者须意识到其中天然隐含的危险性，父母在求子女出人头地前也应先想清楚。",
      "evidence": [
       "E8",
       "E9"
      ]
     },
     {
      "claim_id": "C006",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "异于大多数人分两种：一种没得选（天赋异禀、继承王位等注定不能平常，既不幸也幸运）；一种有得选，则选了就要认。",
      "evidence": [
       "E10",
       "E11",
       "E12"
      ]
     }
    ],
    "argument_steps": [
     "先纠正提问用词：是 uncommon 而非 abnormal（P001、P002）。",
     "解释「常」何以被重视：对「法不责众」庇护性法则的极端利用（P003）。",
     "机制说明：藏身方差中安全，突出即暴露（P004）。",
     "列出第一重危险：评价体系会变，多数不受波及（P005、P006、P007）。",
     "列出第二重危险：任何一派都有敌人，而各派都不把多数划为对立面（P008、P009）。",
     "收束：两重叠加，最安全的是成为「常」（P010、P011）。",
     "劝告：把它当既定永久前提，不作道德抱怨（P012、P013）。",
     "追问读者：是否准备承受、基于什么理由（P014）。",
     "第一种情形：没得选者的处境与「既不幸也幸运」（P015、P016、P017）。",
     "第二种情形：有得选则选了就认，并以偶像被粉丝反噬为例（P018、P019）。"
    ],
    "concept_usage": [
     {
      "term": "常",
      "meaning": "成为大多数中的一员的状态；文中被指为中国文化赋予正面价值的目标。",
      "evidence": "P003",
      "ambiguity": "作者在「常」上叠加了文化批评与安全策略两层含义。"
     },
     {
      "term": "正常/不寻常（normal/common）",
      "meaning": "作者用英文词区分：不正常（normal）与不寻常、不普通（common），主张提问者属后者。",
      "evidence": "P001",
      "ambiguity": "作者的 normal 与 common 对应关系与常见英文用法不同，属作者自设区分。"
     },
     {
      "term": "法不责众",
      "meaning": "被称为庇护性法则，是多数免于波及的机制。",
      "evidence": "P003",
      "ambiguity": "作者将其当作稳定机制使用，未说明是否有例外。"
     },
     {
      "term": "交叉火力",
      "meaning": "各方评价体系对突出者形成的双向攻击态势。",
      "evidence": "P010",
      "ambiguity": "比喻性表述。"
     },
     {
      "term": "突出（stand out）/暴露（exposed）",
      "meaning": "异于大多数者所处的可见状态。",
      "evidence": "P004",
      "ambiguity": "作者对突出的种类未作枚举。"
     }
    ],
    "examples_and_targets": [
     "提问者的自述爱好（研究古埃及、不追星看综艺）——被回应的情境，非作者例证（Q001）。",
     "从「惟有读书高」变成「反动权威」、从「世代簪缨」变成「恶贯满盈」——作者举的评价体系翻转例（P006）。",
     "继承王位（作者注明没有反讽之意）——属于「没得选」的例子（P016）。",
     "偶像被粉丝反噬——属于「有得选」后果的例子（P019）。"
    ],
    "conditions": [
     "文化判断的适用范围限于「中国文化里」（P003）。",
     "第一重危险带条件：「即使在目前的评价体系里你这种突出是受鼓励的、正面的，难保明天评价体系一变」（P006）。",
     "第二重危险的适用条件：「只要它是关心现实势力的」派别才不把多数划为对立面（P009）。",
     "劝告以「无论你因为什么原因异于大多数人」为前提，并要求放弃政治正确的安慰（P013）。",
     "文本状态限定：文末标「（未完，待续）」，分类只列出两种情形（P020）。"
    ],
    "rhetoric_and_tone": "第二人称直接对提问者说话，语气为冷静的训诫与风险提示；用英文词标注（common/normal/stand out/exposed）作概念区分；「密不透风」「总有一枪瞄准你」「你就老老实实去扛吧」等句带宿命感与硬朗口吻；结尾注明待续。",
    "unresolved_questions": [
     "文末明标「（未完，待续）」，两种情形之后是否还有内容不明。",
     "作者未回答提问者所问的心理健康问题本身（是否心理不正常），只作词义与风险层面的回应。",
     "「反动权威」「世代簪缨」等历史比拟未给具体年代与事件。",
     "「常」的正面价值是否仅为负面机制（法不责众）所致，作者未讨论其他成因。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "这个叫“不寻常、不普通（common）”。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P003",
      "quote": "这其实是对“法不责众”这条庇护性法则的极端利用造成的。",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P006",
      "quote": "难保明天评价体系一变",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P008",
      "quote": "那么你在其敌人的眼里就是负面突出",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P009",
      "quote": "都不会把大多数人划到对立面去。",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P010",
      "quote": "所有角度的突出都是将自己暴露在交叉火力之下",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P011",
      "quote": "最安全的就是成为大多数中的一员，成为“常”。",
      "relation": "supports"
     },
     {
      "key": "E8",
      "paragraph_id": "P012",
      "quote": "你只能以此为既定和永久的事实前提来考虑自己的选择。",
      "relation": "supports"
     },
     {
      "key": "E9",
      "paragraph_id": "P013",
      "quote": "你都要意识到这其中天然隐含着危险性",
      "relation": "supports"
     },
     {
      "key": "E10",
      "paragraph_id": "P015",
      "quote": "第一种，是你没得选。",
      "relation": "supports"
     },
     {
      "key": "E11",
      "paragraph_id": "P017",
      "quote": "这既是不幸，也是幸运",
      "relation": "supports"
     },
     {
      "key": "E12",
      "paragraph_id": "P018",
      "quote": "那么你选了就要认，不要选了要出人头地",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "社会心理",
     "文化批评",
     "个人处世"
    ],
    "issue_candidates": [
     "与众不同与安全感",
     "法不责众",
     "评价体系变化的风险",
     "父母对子女出人头地的期待"
    ],
    "text_function_candidates": [
     "答疑",
     "劝诫",
     "经验总结"
    ],
    "object_candidates": [
     "提问者（十三岁女生）",
     "父母",
     "粉丝"
    ],
    "working_keywords": [
     "常",
     "法不责众",
     "突出",
     "方差",
     "交叉火力",
     "stand out",
     "未完待续"
    ]
   },
   "notes": "无图片节点。正文20段完整，但 P020 为「（未完，待续）」，本篇自述未完成，已在 unresolved_questions 登记。提问者自述爱好与自我怀疑属提问者说法，本记录未归给作者。"
  },
  "37d7b49b": {
   "analysis": {
    "question_context": "提问者问「怎么看待8.18晚南京航空航天大学跳楼事件?」（Q001）。作者未叙述或评论该事件本身，只以理想主义者的心理机制为对象作答，且行文用 ta 指代当事人。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001",
       "P002"
      ],
      "summary": "主张理想需要技能与同志，并希望有志之士有更好的运气学到必要技能。",
      "role": "claim"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P003",
       "P004",
       "P005"
      ],
      "summary": "列举所需技能：解决问题、团结同志、忍受困难、信仰、原谅和宽恕。",
      "role": "definition"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P006",
       "P007"
      ],
      "summary": "提出反直觉判断：支撑不断努力的不是对美好世界的向往，后者将来会是最凶恶的敌人；真正支撑的是不断的原谅和宽恕。",
      "role": "rebuttal"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P008"
      ],
      "summary": "主张同志不是「对美好世界的共同向往」的产物，而是宽恕和原谅的产物。",
      "role": "claim"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P009",
       "P010"
      ],
      "summary": "对自杀的理想主义者作动机解释：不是在惩罚自己而是在惩罚世界，不是因为绝望，而是因为决定不再原谅。",
      "role": "conclusion"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "理想需要技能、需要同志。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "希望有志之士能有更好的运气学到必要的技能。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "最终支撑不断努力的不是对美好世界的向往；恰恰相反，「对美好世界的向往」将来会是最凶恶的敌人。",
      "evidence": [
       "E3"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "支撑无限努力的是不断的原谅和宽恕。",
      "evidence": [
       "E4"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "同志不是「对美好世界的共同向往」的产物，而是宽恕和原谅的产物。",
      "evidence": [
       "E5"
      ]
     },
     {
      "claim_id": "C006",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "自杀的理想主义者不是在惩罚自己，而是在惩罚世界；不是因为绝望，而是因为决定不再原谅。",
      "evidence": [
       "E6",
       "E7"
      ]
     }
    ],
    "argument_steps": [
     "前提出发：理想需要技能与同志（P001）。",
     "表达愿望：希望有志之士有好运气学到必要技能（P002）。",
     "列举技能清单：解决问题、团结同志、忍受困难、信仰、原谅和宽恕（P003、P004、P005）。",
     "反转常识：努力的真实支撑不是对美好世界的向往，后者将来会是最凶恶的敌人（P006）。",
     "给出替代：支撑无限努力的是不断的原谅和宽恕（P007）。",
     "重新定义同志：同志是宽恕和原谅的产物，而非共同向往的产物（P008）。",
     "对自杀动机作解释：惩罚世界而非惩罚自己，因决定不再原谅而非因绝望（P009、P010）。"
    ],
    "concept_usage": [
     {
      "term": "技能",
      "meaning": "实现理想所需的能力，文中列举五类，含信仰与原谅宽恕这类非技术性能力。",
      "evidence": "P001",
      "ambiguity": "未说明这些技能如何习得。"
     },
     {
      "term": "同志",
      "meaning": "被重新定义为宽恕和原谅的产物，而非共同理想认同的产物。",
      "evidence": "P008",
      "ambiguity": "与通常以共同目标界定同志的做法不同，属作者改写。"
     },
     {
      "term": "对美好世界的向往",
      "meaning": "被指为将来最凶恶的敌人，即理想主义者的内在风险来源。",
      "evidence": "P006",
      "ambiguity": "作者未解释它为何会转为敌人。"
     },
     {
      "term": "原谅和宽恕",
      "meaning": "被称为支撑无限努力的真实来源。",
      "evidence": "P007",
      "ambiguity": "未区分原谅与宽恕，也未说明对象。"
     },
     {
      "term": "惩罚世界",
      "meaning": "作者对自杀的理想主义者行为动机的定性。",
      "evidence": "P009",
      "ambiguity": "以 ta 指代当事人，主体未具名，属作者的动机推断。"
     }
    ],
    "examples_and_targets": [
     "「对美好世界的向往」——被作者指认为最凶恶敌人的对象，属被反驳的常见信念（P006）。",
     "自杀的理想主义者（以 ta 指代）——作者作动机解释的对象；未提姓名与具体事件（P009、P010）。",
     "南京航空航天大学跳楼事件——仅出现在提问字段，作者正文未叙述（Q001）。"
    ],
    "conditions": [
     "技能清单以「理想需要技能」为前提，未限定适用对象（P001）。",
     "「希望有志之士能有更好的运气」以运气为条件，含不确定性（P002）。",
     "对自杀动机的解释以「理想主义者」为限定主体（P009）。",
     "时间限定：对美好世界的向往「在将来会」成为敌人，属预测性判断（P006）。"
    ],
    "rhetoric_and_tone": "短句与断行式列举，语气近乎格言；用「最凶恶的敌人」作强反转修辞；以 ta 作中性人称指代当事人，未作道德评价；对具体事件保持沉默，属克制而抽象的说理语气。",
    "unresolved_questions": [
     "作者未叙述或评论提问所指的 8.18 南京航空航天大学跳楼事件本身，与该事件的关系需研究者判断。",
     "「对美好世界的向往」为何会成为最凶恶的敌人，正文未展开。",
     "「不再原谅」的对象（世界、他人还是自己）未说明。",
     "P009、P010 以 ta 指代当事人，其主体是否即事件当事人不能确定。",
     "该回答是否为完整文本，正文无明显待续标记，但结构上是格言式结尾，完整性无法由文本内部确认。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "理想需要技能、需要同志。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P002",
      "quote": "希望有志之士能有更好的运气学到必要的技能。",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P006",
      "quote": "不会是对美好世界的向往——恰恰相反，“对美好世界的向往”在将来会是你最凶恶的敌人。",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P007",
      "quote": "支撑你无限努力的，是不断的原谅和宽恕。",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P008",
      "quote": "而是宽恕和原谅的产物。",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P009",
      "quote": "并不是在惩罚自己，ta是在惩罚世界。",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P010",
      "quote": "而因为ta决定不再原谅。",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "心理与伦理",
     "理想主义议题",
     "社会评论"
    ],
    "issue_candidates": [
     "理想实现的技能条件",
     "理想主义者的心理机制",
     "原谅与宽恕的作用"
    ],
    "text_function_candidates": [
     "答疑",
     "劝诫",
     "格言式说理"
    ],
    "object_candidates": [
     "理想主义者",
     "同志",
     "有志之士"
    ],
    "working_keywords": [
     "理想",
     "技能",
     "同志",
     "宽恕",
     "原谅",
     "美好世界的向往"
    ]
   },
   "notes": "无图片节点。正文10段完整。作者全文未提及提问所指的具体跳楼事件与当事人姓名，P009/P010 以 ta 指代，主体不明，已在 unresolved_questions 登记；本记录未把事件细节补入作者主张。"
  },
  "96a1dbf3": {
   "analysis": {
    "question_context": "提问者问「如何看待温柔junz最新视频《豫章书院曝光者温柔，深陷“网络暴力”泥潭》 并声称自己一生没有做坏事？」（Q001）。作者回应行善与免受不公正对待之间的关系，并给出应对网暴的具体做法，文末引用德兰修女箴言赠予当事人。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001",
       "P002"
      ],
      "summary": "提出核心判断：世界不按「我没做坏事，于是我不应受不公正对待」的法则运转；「我不做坏事」与「我不该受到不公正的对待」是两件事。",
      "role": "claim"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P003",
       "P004",
       "P005"
      ],
      "summary": "界定行善的唯一对价是「有所作为」的价值感，游戏发热式的副效应不算在内；义人感、善良债、额外尊敬都不是合法回报，行善根本不指向不受不公正对待或优待。",
      "role": "definition"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P006",
       "P007",
       "P008"
      ],
      "summary": "指出免责靠的是御侮的方法而非行善；行善归行善，御侮归御侮，行了善不意味着无需做御侮功夫。",
      "role": "claim"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P009",
       "P010"
      ],
      "summary": "让步与反驳：东亚社会确曾以相当社会资本构建「你只管行善，大众/政府会帮你御侮」的承诺，但人类没有富有到能彻底、普遍、及时地实施，将来也不可能有。",
      "role": "rebuttal"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P011",
       "P012",
       "P013",
       "P014",
       "P015"
      ],
      "summary": "行动建议：对抗网暴首先要拒绝成为偶像；其次不断提供对最广泛大众有价值的新信息，而不是针对某个让你不爽的个人；以发论文遭骂为例，最有效的手段是继续发第二篇第三篇，直到对方自己后悔删话。",
      "role": "action_advice"
     },
     {
      "unit_id": "U006",
      "paragraph_refs": [
       "P016",
       "P017",
       "P018",
       "P019"
      ],
      "summary": "对当事人的具体劝告：接着做豫章书院这样的事才是最好的回应；不断辩白证明自己无辜虽可理解但客观无效，因为这是强行攫取公众注意力，而容忍有限度、其薄如冰。",
      "role": "action_advice"
     },
     {
      "unit_id": "U007",
      "paragraph_refs": [
       "P020",
       "P021",
       "P022",
       "P023"
      ],
      "summary": "呼吁关心当事人者给予恰当帮助，即提供庇护、阻止非法手段的迫害威胁，而不是针锋相对反唇相讥；是提醒和鼓励、是陪伴；并指出其真正脆弱点是孤独。",
      "role": "action_advice"
     },
     {
      "unit_id": "U008",
      "paragraph_refs": [
       "P024",
       "P025",
       "P026",
       "P027",
       "P028",
       "P029",
       "P030",
       "P031",
       "P032",
       "P033",
       "P034",
       "P035",
       "P036",
       "P037",
       "P038",
       "P039",
       "P040",
       "P041",
       "P042",
       "P043",
       "P044",
       "P045",
       "P046",
       "P047",
       "P048",
       "P049",
       "P050",
       "P051",
       "P052",
       "P053",
       "P054",
       "P055",
       "P056",
       "P057",
       "P058",
       "P059",
       "P060",
       "P061",
       "P062"
      ],
      "summary": "以中英对照逐条引用德兰修女箴言赠予当事人，内容为「不管怎样」式的劝勉：原谅、友善、成功、诚实率直、营造、快乐、行善、给出最好的东西。",
      "role": "other"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "这个世界并不是按照「我没做坏事，于是我不应该/不会受到不公正的对待」这样的法则来运转的。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "「我不做坏事」和「我不该受到不公正的对待」是两件事。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "行善所能交换的唯一切实回报是「有所作为」的价值感，其余只是副效应；义人感、善良债与额外尊敬都不是行善的合法回报。",
      "evidence": [
       "E3",
       "E4"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "行善根本不指向「我不会受到不公正的对待」甚至「优待」；是防止受不公正对待的做法在起防止作用。",
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
      "statement": "行善并非御侮的全部内容，御侮对应的是御侮的方法而非行善。",
      "evidence": [
       "E7"
      ]
     },
     {
      "claim_id": "C006",
      "claim_type": "author_reported",
      "attribution": "author",
      "modality": "qualified",
      "statement": "东亚社会确曾构建并投入社会资本宣传「你只管行善，大众/政府会帮你御侮」的承诺，使人相信之。",
      "evidence": [
       "E8"
      ]
     },
     {
      "claim_id": "C007",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "人类没有富有到能彻底、普遍、及时地实施这条承诺，事实上将来也不可能有如此的富有。",
      "evidence": [
       "E9"
      ]
     },
     {
      "claim_id": "C008",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "对抗这类网暴，首先要拒绝成为偶像；第二要不断提供新的、对最广泛大众有价值的新信息，而不是空洞针对某个让你不爽的个人。",
      "evidence": [
       "E10",
       "E11"
      ]
     },
     {
      "claim_id": "C009",
      "claim_type": "author_qualified",
      "attribution": "author",
      "modality": "qualified",
      "statement": "像论文作者被骂那样，最有效的手段是继续发第二篇第三篇，直到对方自己删话，而非申辩对方哪里不礼貌、哪里批评得不正确。",
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
      "statement": "不断进行辩白证明自己无辜，心情可以理解、值得同情，但客观上没有效果，因为这是在强行攫取公众注意力资源以谋自己的利益。",
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
      "statement": "作者呼吁关心当事人的人给予恰当的帮助：提供庇护、阻止以非法手段进行语言和暴力迫害，而非压倒敌人；并指出其真正脆弱的点应是觉得孤独。",
      "evidence": [
       "E16",
       "E17",
       "E18"
      ]
     }
    ],
    "argument_steps": [
     "命题：世界不按「行善即应免受不公正对待」的法则运转（P001）。",
     "概念切分：不作恶与不该受不公正对待是两件事（P002）。",
     "界定对价：行善的唯一切实回报是价值感，其余是手机发热式副效应（P003）。",
     "排除项：义人感、善良债、额外尊敬不是合法回报（P004）。",
     "收窄结论：行善不指向免于不公正对待或优待（P005）。",
     "机制归因：是防止受不公正对待的做法在起作用（P006）。",
     "区分领域：行善归行善、御侮归御侮（P007、P008）。",
     "让步：东亚社会确曾构建「行善则大众/政府帮你御侮」的承诺并投入成本（P009）。",
     "反驳：人类没有富有到能彻底、普遍、及时实施该承诺，将来也不可能有（P010）。",
     "行动建议一：拒绝成为偶像，持续提供对大众有价值的新信息（P011、P012）。",
     "类比：论文被骂应以续写第二、三篇回应，而非纠正对方态度（P013、P014、P015）。",
     "具体劝告：接着做豫章书院式的事才是最好的回应，辩白无偿且消耗公众容忍（P016、P017、P018、P019）。",
     "对他人的呼吁：提供庇护、阻止非法迫害，是提醒、鼓励与陪伴（P020、P021、P022、P023）。",
     "以德兰修女箴言中英对照作结（P024 及以后）。"
    ],
    "concept_usage": [
     {
      "term": "合法的回报/对价",
      "meaning": "行善所能交换的切实回报，作者限定为有且仅有的「尽义」的价值感。",
      "evidence": "P003",
      "ambiguity": "「合法」在文中指正当可得，非法律意义。"
     },
     {
      "term": "副效应",
      "meaning": "以手机玩游戏发热作比，指行善附带而生、非其交换所得的东西。",
      "evidence": "P003",
      "ambiguity": "作者举「我比别人善良」的义人感等，但未穷举副效应范围。"
     },
     {
      "term": "御侮",
      "meaning": "防止受到不公正对待的功夫，被作者与行善明确区分。",
      "evidence": "P007",
      "ambiguity": "作者未系统说明御侮的方法清单。"
     },
     {
      "term": "成为偶像",
      "meaning": "被作者列为对抗网暴时首要不做的事。",
      "evidence": "P011",
      "ambiguity": "未界定成为偶像的判据。"
     },
     {
      "term": "容忍",
      "meaning": "公众注意力的让渡，被形容为有限度、其薄如冰。",
      "evidence": "P019",
      "ambiguity": "修辞性表述，未给尺度。"
     }
    ],
    "examples_and_targets": [
     "拿着手机玩游戏、手机所发的热——类比材料，说明副效应（P003）。",
     "东亚社会构建的「你只管行善，大众/政府会帮你御侮」承诺——被反驳的制度性信念（P009、P010）。",
     "发论文被破口大骂、应继续发第二篇第三篇——类比性行动建议（P013、P014、P015）。",
     "嘲笑爱因斯坦不懂科学、被钉在耻辱柱上——修辞性比拟材料（P015）。",
     "做了一次豫章书院——被作者正面肯定的当事人行为（P016）。",
     "@温柔JUNZ 与豫章书院曝光者——被呼吁给予帮助的对象（P020、P021、P024）；事件本身细节未叙述。",
     "德兰修女箴言（中英对照）——引用材料，作者注明为赠予当事人的箴言（P024）。"
    ],
    "conditions": [
     "社会承诺的构建被限定于「东亚社会」，并限定为「至少是宣传成本」的投入（P009）。",
     "承诺无法落实的判断带时间与规模限定：不能「彻底、普遍、及时」，且「将来也不可能有」（P010）。",
     "行动建议以「对抗这类网暴」为适用场景（P011）。",
     "论文类比的有效手段以「有人对你破口大骂」为触发条件；作者并注明体谅性回应「是留给理性而有爱的批评者的」（P013）。",
     "公众容忍有限度，故辩白方式被作者判为无效（P018、P019）。"
    ],
    "rhetoric_and_tone": "面向三类听众分层行文：对抽象读者说理、对当事人直接称呼（「对 @温柔JUNZ 你自己，送给你德兰修女箴言」）、对关心者发出呼吁；用「手机发热」「其薄如冰」「钉在耻辱柱上」「嘲笑爱因斯坦不懂科学」等具体比喻；有明确训诫与同情并存的语气，结尾以大段引文转为劝慰。",
    "unresolved_questions": [
     "作者未叙述豫章书院事件与网暴经过的细节，仅以提问与当事人行为为背景，事件事实需外部核查。",
     "「大众/政府会帮你御侮」的承诺未给具体制度、文件或时期。",
     "德兰修女箴言的中英对照文本未注明版本来源，且中英段落在正文中交错排列，是否为完整版本不明。",
     "「恰当帮助」的操作界限（如何区分庇护与压倒敌人）作者只作原则说明。",
     "P024 提及 @温柔JUNZ，为知乎提及语法，索引时需注意。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "这个世界并不是按照“我没做坏事，于是我不应该/不会受到不公正的对待”这样的法则来运转的。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P002",
      "quote": "“我不做坏事”和“我不该受到不公正的对待”是两件事。",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P003",
      "quote": "也就是它唯一的切实回报，是“有所作为”的价值感",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P004",
      "quote": "都并不是行善的“合法回报”的一部分",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P005",
      "quote": "它根本就不指向“我不会受到不公正的对待”甚至“优待”。",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P006",
      "quote": "是“防止我受到不公正对待的做法”防止“受到不公正的对待”。",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P007",
      "quote": "而“行善”并非御侮的全部内容——远远不是。",
      "relation": "supports"
     },
     {
      "key": "E8",
      "paragraph_id": "P009",
      "quote": "来说服人们相信这种“你只管行善，大众/政府会帮你御侮”的承诺",
      "relation": "supports"
     },
     {
      "key": "E9",
      "paragraph_id": "P010",
      "quote": "事实上，将来也不可能有如此的富有。",
      "relation": "supports"
     },
     {
      "key": "E10",
      "paragraph_id": "P011",
      "quote": "对抗这类网暴，首先要拒绝成为偶像。",
      "relation": "supports"
     },
     {
      "key": "E11",
      "paragraph_id": "P012",
      "quote": "而不是空洞的去针对某个让你不爽的个人。",
      "relation": "supports"
     },
     {
      "key": "E12",
      "paragraph_id": "P013",
      "quote": "最有效的手段不是去说明对方哪里不礼貌，哪里批评得不正确",
      "relation": "supports"
     },
     {
      "key": "E13",
      "paragraph_id": "P014",
      "quote": "你应该再发第二篇、第三篇、第四篇。",
      "relation": "supports"
     },
     {
      "key": "E14",
      "paragraph_id": "P017",
      "quote": "而不是不断进行对其他公众并没有什么额外信息的辩白，证明自己有多无辜。",
      "relation": "supports"
     },
     {
      "key": "E15",
      "paragraph_id": "P018",
      "quote": "你是在强行攫取公众的注意力资源来谋求自己的利益",
      "relation": "supports"
     },
     {
      "key": "E16",
      "paragraph_id": "P020",
      "quote": "我呼吁关心@温柔JUNZ 的人给予他恰当的帮助。",
      "relation": "supports"
     },
     {
      "key": "E17",
      "paragraph_id": "P021",
      "quote": "而是指站出来提供庇护、阻止别人用非法的手段对人进行语言和暴力的迫害和威胁。",
      "relation": "supports"
     },
     {
      "key": "E18",
      "paragraph_id": "P023",
      "quote": "他现在真正脆弱的点应该是觉得孤独。",
      "relation": "supports"
     },
     {
      "key": "E19",
      "paragraph_id": "P024",
      "quote": "送给你德兰修女箴言：",
      "relation": "context"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "伦理",
     "网络舆论",
     "社会评论"
    ],
    "issue_candidates": [
     "行善与免受不公正对待的关系",
     "网络暴力的应对",
     "公众注意力与容忍限度",
     "对受害者的恰当帮助"
    ],
    "text_function_candidates": [
     "答疑",
     "评论",
     "行动建议",
     "劝诫",
     "引用"
    ],
    "object_candidates": [
     "温柔JUNZ",
     "豫章书院",
     "东亚社会",
     "大众",
     "政府",
     "德兰修女",
     "爱因斯坦",
     "公众"
    ],
    "working_keywords": [
     "行善",
     "御侮",
     "对价",
     "副效应",
     "网暴",
     "偶像",
     "容忍",
     "箴言"
    ]
   },
   "notes": "无图片节点。正文62段完整，其中 P024-P062 为中英对照引用的德兰修女箴言（说话者为德兰修女，属引用材料，本记录以 quoted_or_cited/context 处理，未归给作者）。作者未叙述豫章书院与网暴事件细节，事件事实待外部核查。P020/P024 含知乎 @ 提及语法。"
  },
  "09080646": {
   "analysis": {
    "question_context": "提问者问「如何看待对于相同商品或服务，女性会受到价格歧视等「粉红税」现象？我们该从哪些方面努力实现「性别平等」？」（Q001）。作者不承认粉红税构成伦理问题，而从经营自由与政治正确干预的代价两方面作答，未就「如何实现性别平等」给出正面方案。",
    "content_units": [
     {
      "unit_id": "U001",
      "paragraph_refs": [
       "P001"
      ],
      "summary": "提出前提：非垄断商品完全可以自由定价，这属于经营自由。",
      "role": "claim"
     },
     {
      "unit_id": "U002",
      "paragraph_refs": [
       "P002"
      ],
      "summary": "以反问反驳歧视性价格的伦理指控：否则学生价、早鸟价、老年人特惠、乡村特卖怎么算。",
      "role": "rebuttal"
     },
     {
      "unit_id": "U003",
      "paragraph_refs": [
       "P003"
      ],
      "summary": "指出歧视性定价的天然压力来自价格表与服务复杂化、不当设计影响利润，以及市场对不良定价的自动负面反应。",
      "role": "reason"
     },
     {
      "unit_id": "U004",
      "paragraph_refs": [
       "P004"
      ],
      "summary": "以假设方式说明市场自纠：若有人喜欢男贱女贵，就让他自己尝试，自然有不这么做的商家接过生意。",
      "role": "claim"
     },
     {
      "unit_id": "U005",
      "paragraph_refs": [
       "P005",
       "P006"
      ],
      "summary": "主张用政治正确干预经济运行必须奉行谦抑原则；一旦开口就会面临「凭什么ta的权利重要」的连锁要求，几乎必定导致整体社会运行效率显著下降。",
      "role": "qualification"
     },
     {
      "unit_id": "U006",
      "paragraph_refs": [
       "P007",
       "P008",
       "P009"
      ],
      "summary": "预测长期后果：国际竞争中因缺少实力而失败、国家失败，任何政治正确都会化为乌有；以「我们非常正确」与产品更贵、军队更脆弱的对照作讽刺。",
      "role": "conclusion"
     },
     {
      "unit_id": "U007",
      "paragraph_refs": [
       "P010"
      ],
      "summary": "收束原则：要干预经营自由，要有重大得多的理由，因为经营自由无小事。",
      "role": "conclusion"
     }
    ],
    "main_claims": [
     {
      "claim_id": "C001",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "非垄断商品完全可以自由定价，这属于经营自由。",
      "evidence": [
       "E1"
      ]
     },
     {
      "claim_id": "C002",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "negated",
      "statement": "即使是「歧视性价格」也没有任何伦理问题，否则学生价、早鸟价、老年人特惠、乡村特卖都无法解释。",
      "evidence": [
       "E2"
      ]
     },
     {
      "claim_id": "C003",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "「歧视性定价」的主要天然压力是价格表复杂、服务复杂化、不当设计影响利润，其次是市场本身会对不良定价自动作出负面反应。",
      "evidence": [
       "E3"
      ]
     },
     {
      "claim_id": "C004",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "hypothetical",
      "statement": "若有人喜欢男贱女贵，就让他自己尝试，自然有不这么做的商家接过他的生意。",
      "evidence": [
       "E4"
      ]
     },
     {
      "claim_id": "C005",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "用政治正确去干预经济运行，必须奉行谦抑原则，否则会带来严重的长期后果。",
      "evidence": [
       "E5"
      ]
     },
     {
      "claim_id": "C006",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "predicted",
      "statement": "政治正确的风向复杂多变，只要开一个口子就会出现「凭什么ta的权利重要」的连锁要求，这几乎必定导致整体社会运行效率显著下降。",
      "evidence": [
       "E6"
      ]
     },
     {
      "claim_id": "C007",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "predicted",
      "statement": "长此以往会在国际竞争中因缺少实力而失败，国家失败后任何政治正确都会化为乌有。",
      "evidence": [
       "E7"
      ]
     },
     {
      "claim_id": "C008",
      "claim_type": "author_explicit",
      "attribution": "author",
      "modality": "asserted",
      "statement": "要干预经营自由，要有重大得多的理由，因为经营自由无小事。",
      "evidence": [
       "E9"
      ]
     }
    ],
    "argument_steps": [
     "立前提：非垄断商品自由定价属经营自由（P001）。",
     "归谬式反问：若歧视性价格有伦理问题，学生价、早鸟价、老年人特惠、乡村特卖如何解释（P002）。",
     "替代机制说明：歧视性定价的压力来自复杂化成本、利润影响与市场负面反应（P003）。",
     "假设性市场自纠：允许尝试男贱女贵，商家竞争会使顾客流向不这样做的商家（P004）。",
     "提出原则：政治正确干预经济运行须奉行谦抑（P005）。",
     "滑坡式预测：开口子将引发各群体争相要求专属禁令，几致社会运行效率显著下降（P006）。",
     "推到国际竞争：缺实力则国家失败，政治正确随之化为乌有（P007）。",
     "讽刺对照：「我们非常正确」与产品成本更高、军队更脆弱（P008、P009）。",
     "收束：干预经营自由需要重大得多的理由（P010）。"
    ],
    "concept_usage": [
     {
      "term": "经营自由",
      "meaning": "非垄断商品的自由定价权，被作者当作需要强理由才能干预的前提性权利。",
      "evidence": "P001",
      "ambiguity": "作者以「非垄断商品」作限定，但未界定垄断的判定标准。"
     },
     {
      "term": "歧视性价格/歧视性定价",
      "meaning": "对不同群体给不同价格的定价方式，作者主张其本身没有伦理问题。",
      "evidence": "P002",
      "ambiguity": "作者在描述意义上使用「歧视」，与提问中带道德谴责的「粉红税」用法不同。"
     },
     {
      "term": "政治正确",
      "meaning": "被作者视为可能干预经济运行的规范性要求，其风向复杂多变。",
      "evidence": "P006",
      "ambiguity": "作者未列举具体政治正确条目，也未区分不同类型。"
     },
     {
      "term": "谦抑原则",
      "meaning": "作者主张干预经济运行时应遵循的克制原则。",
      "evidence": "P005",
      "ambiguity": "未给出谦抑的判断标准或操作界限。"
     },
     {
      "term": "经营自由无小事",
      "meaning": "作为要求干预方提出重大理由的依据。",
      "evidence": "P010",
      "ambiguity": "格言式表述，未说明重大理由的尺度。"
     }
    ],
    "examples_and_targets": [
     "学生价、早鸟价、老年人特惠、乡村特卖——作者列举的同类歧视性定价例，用作反问证据（P002）。",
     "「有人喜欢男贱女贵」——假设性情形，用于说明市场自纠（P004）。",
     "「我们非常正确，虽然我们的产品比人家成本高、我们的军队比人家脆弱」——讽刺性引语，作者用作修辞材料（P008、P009）。",
     "提问中「女性受到价格歧视的粉红税现象」与「性别平等」——被回应的问题；作者未使用「粉红税」一词（Q001）。"
    ],
    "conditions": [
     "主张限定于「非垄断商品」，未覆盖垄断商品定价（P001）。",
     "市场自纠以假设条件表述：「有人喜欢男贱女贵，就让ta自己尝试」（P004）。",
     "干预原则带后果条件：用政治正确干预「必须奉行谦抑原则，否则会带来严重的长期后果」（P005）。",
     "连锁要求起因于「只要你开一个口子」这一条件（P006）。",
     "强度词保留余地：效率下降用「几乎必定」，国际竞争失败与政治正确化为乌有以「长此以往」为前提（P006、P007）。"
    ],
    "rhetoric_and_tone": "以反问归谬开篇（「否则学生价……怎么算？」），中间用「开一个口子」「凭什么ta的权利重要」等口语化表述，末尾以假想引语作反讽（「但我们非常正确。」），整体为论辩性、讥刺性的评论语气；未对提问者作人身评价。",
    "unresolved_questions": [
     "作者未正面回答提问第二问「该从哪些方面努力实现性别平等」，该问在正文中无对应内容。",
     "作者未使用「粉红税」一词，也未讨论提问所指的具体商品或服务案例。",
     "「非垄断商品」的判定标准、以及垄断商品是否适用其结论，正文未说明。",
     "「谦抑原则」与「重大得多的理由」的具体尺度未给出。",
     "P008、P009 的引语未标明说话者，是作者虚拟还是引用他人不明，本记录按作者修辞处理。"
    ],
    "evidence": [
     {
      "key": "E1",
      "paragraph_id": "P001",
      "quote": "非垄断商品完全可以自由定价，这属于经营自由。",
      "relation": "supports"
     },
     {
      "key": "E2",
      "paragraph_id": "P002",
      "quote": "即使是“歧视性价格”也没有任何伦理问题",
      "relation": "supports"
     },
     {
      "key": "E3",
      "paragraph_id": "P003",
      "quote": "第二是市场本身会对不良定价自动作出负面反应。",
      "relation": "supports"
     },
     {
      "key": "E4",
      "paragraph_id": "P004",
      "quote": "自然有不这么做的商家接过ta的生意",
      "relation": "supports"
     },
     {
      "key": "E5",
      "paragraph_id": "P005",
      "quote": "用政治正确去干预经济运行，必须奉行谦抑原则",
      "relation": "supports"
     },
     {
      "key": "E6",
      "paragraph_id": "P006",
      "quote": "这几乎必定导致整体社会运行效率的显著下降。",
      "relation": "supports"
     },
     {
      "key": "E7",
      "paragraph_id": "P007",
      "quote": "国家失败，任何政治正确都会化为乌有。",
      "relation": "supports"
     },
     {
      "key": "E8",
      "paragraph_id": "P008",
      "quote": "我们的产品比人家成本高、我们的军队比人家脆弱。",
      "relation": "context"
     },
     {
      "key": "E9",
      "paragraph_id": "P010",
      "quote": "因为经营自由无小事。",
      "relation": "supports"
     }
    ]
   },
   "provisional_tags": {
    "domain_candidates": [
     "经济学",
     "价格与市场",
     "公共政策",
     "性别议题"
    ],
    "issue_candidates": [
     "粉红税与价格歧视",
     "经营自由与定价权",
     "政治正确对经济的干预",
     "性别平等的实现路径"
    ],
    "text_function_candidates": [
     "答疑",
     "论辩",
     "评论",
     "反驳"
    ],
    "object_candidates": [
     "女性消费者",
     "商家",
     "国家",
     "军队"
    ],
    "working_keywords": [
     "粉红税",
     "歧视性价格",
     "经营自由",
     "政治正确",
     "谦抑原则",
     "价格歧视"
    ]
   },
   "notes": "无图片节点。正文10段完整。作者全文未使用「粉红税」一词，亦未回答提问中「如何实现性别平等」一问，该缺口已在 unresolved_questions 登记。P008/P009 引语未标说话者，按作者修辞材料处理，未归给第三方。"
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
