# -*- coding: utf-8 -*-
"""批次 r001-b0035 的记录构造器（SKELETON 由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。
"""

from __future__ import annotations

import json
import os
import sys


_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from authoring import build_record, load_batch_rows, write_jsonl

BATCH = "r001-b0035"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0035.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}

ANALYSIS = {
    "abb8a631": {
        "analysis": {
            "question_context": "提问者的问题是“如何看待工信部表示力争 2020 年底实现全国所有地级市覆盖 5G 网络？”——即如何看待在需求尚未充分显现时先行铺设 5G 网络的表态。作者没有直接评论该政策，而是用 F1 赛车与赛道的相互依存关系作类比作答，标题“蛋生鸡”提示其回应的是“先有鸡还是先有蛋”式的先后之争。（提问者立场属于提问者，未归给作者。）",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001"
                    ],
                    "summary": "假设只有 F1 跑车而没有赛道：跑车会被指为不适应地面起伏与积尘、姿态失控，从而被判定“设计完全不现实”。",
                    "role": "example"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P002"
                    ],
                    "summary": "反过来假设只有赛道而没有 F1 赛车：赛道会被指为代价高而收益小、没有车跑得到在乎这点抓地力的速度，从而被判定“根本没有真实需求”。",
                    "role": "example"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P003"
                    ],
                    "summary": "以反问收束：既然如此，为什么还要抓紧把赛道修起来？以问答形式给出先行建设的立场。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者以 F1 跑车与赛道互为例证指出：在配套条件（赛道/赛车）尚不存在时，单看一方都会得出“设计不现实”“没有真实需求”的否定结论。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者以反问“所以为什么要抓紧把赛道修起来？”收尾，暗示配套基础设施应先于需求证明而抓紧建设。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "opponent_view",
                    "attribution": "opponent",
                    "modality": "asserted",
                    "statement": "文中转述的反对意见（作者假设的挑剔者口径）：没有赛道时 F1 跑车“这种设计完全不现实”，没有 F1 赛车时“这种赛道根本没有真实需求”。",
                    "evidence": [
                        "E3",
                        "E4"
                    ]
                }
            ],
            "argument_steps": [
                "前提（假设情境一）：在没有赛道之前，F1 跑车会被指为不适应地面、抓地力不足，故被判定“设计完全不现实”（P001）。",
                "前提（假设情境二）：在没有 F1 赛车之前，赛道会被指为代价高、减震收益有限，故被判定“根本没有真实需求”（P002）。",
                "两句均用引号转述他人（挑剔者）的评价口径，属于作者设想并要回应其逻辑的反对意见，不是作者自己的判断。",
                "结论：以反问“所以为什么要抓紧把赛道修起来？”把落点放在先行修赛道（先行建设配套）一侧（P003）。",
                "本文未展开说明“赛道/跑车”具体对应什么（5G 网络、终端、应用），也未给出建设时序的具体论证。"
            ],
            "concept_usage": [
                {
                    "term": "赛道",
                    "meaning": "作为类比的配套基础设施一方：本身在缺少对应赛车时看不出价值，需要先行建成。",
                    "evidence": "P002",
                    "ambiguity": "正文未点明其在 5G 议题中的具体所指。"
                },
                {
                    "term": "F1跑车",
                    "meaning": "作为类比的另一方：在配套条件不存在时会被判定为不现实的设计。",
                    "evidence": "P001",
                    "ambiguity": "正文未点明其是否指 5G 终端或应用。"
                },
                {
                    "term": "真实需求",
                    "meaning": "引号内的他人评价用语：在缺乏配套条件时用以否定赛道价值的判据。",
                    "evidence": "P002",
                    "ambiguity": "作者未正面界定“真实需求”的标准。"
                }
            ],
            "examples_and_targets": [
                "F1 跑车——设想中的类比材料（作者假设“没有赛道之前”时他人对跑车的评价，P001）。",
                "赛道——设想中的类比材料（作者假设“没有F1赛车之前”时他人对赛道的评价，P002）。",
                "被反驳/被引述的对象：只以“你”与引号内的评语出现，未指名具体人物或机构（P001、P002）。"
            ],
            "conditions": [
                "两段均以“在没有……之前”为条件，仅在配套一方缺席的假设情境下成立（P001、P002）。",
                "P001 中他人评价的条件是“只要地面稍微有点起伏不平”“只要地面稍微有点积尘”。",
                "P002 中他人评价的条件是“没有什么车可以跑到在乎这点抓地力的速度”。"
            ],
            "rhetoric_and_tone": "全文以设问与反讽式引语构成：两段都用“你”直接称呼假想的挑剔者，并连用引号转述其结论（“你这种设计完全不现实”“这种赛道根本没有真实需求”），制造对称的荒谬感；末句以“所以为什么要抓紧把赛道修起来？”的反问收束，语气简洁、点到即止，不作展开论证。",
            "unresolved_questions": [
                "标题“蛋生鸡”与提问所述 5G 网络覆盖议题的具体对应关系，正文未说明。",
                "“赛道”“F1跑车”分别指向 5G 网络建设中的哪些对象，正文未说明。",
                "该答案是针对“力争 2020 年底实现全国所有地级市覆盖 5G 网络”这一具体表态的何种层面（是否必要、是否过快）作答，正文未说明。",
                "brief 与正文不完全一致（brief 中的引文在正文中分别为两段内的片段），以正文为准；brief 尾句被截断，未参与判断。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "在没有赛道之前，F1跑车的缺点是",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P003",
                    "quote": "所以为什么要抓紧把赛道修起来？",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P001",
                    "quote": "你这种设计完全不现实",
                    "relation": "contradicts"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P002",
                    "quote": "这种赛道根本没有真实需求",
                    "relation": "contradicts"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "通信基础设施",
                "产业政策",
                "技术扩散"
            ],
            "issue_candidates": [
                "5G 网络建设时序",
                "需求与供给孰先",
                "配套基础设施是否应先行"
            ],
            "text_function_candidates": [
                "答疑",
                "类比式评论",
                "论辩"
            ],
            "object_candidates": [
                "工信部",
                "F1 赛车",
                "赛道"
            ],
            "working_keywords": [
                "蛋生鸡",
                "赛道",
                "F1跑车",
                "真实需求",
                "抓紧把赛道修起来"
            ]
        },
        "notes": "无图片节点。追问：正文极短（220 字），除末句反问外未出现显式判断句；其对 5G 政策的态度系由反问推定，已在 main_claims 中标注 modality=questioned，未升级为断言。brief 与正文重复但被截断，仅作导航。"
    },
    "34683c72": {
        "analysis": {
            "question_context": "提问者的问题是“知乎是否应该允许发布个人解答向问题，这类问题对用户是否有价值？”。作者以评论者身份反对知乎以“公共性不足”为由禁止个人向提问，认为该禁令既无必要、又存在逻辑缺陷并会持续消耗平台公信力，最后给出替代做法。提问者的设问立场未被归给作者。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001"
                    ],
                    "summary": "立论前提：任何问题都是成本收益问题。",
                    "role": "definition"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P002"
                    ],
                    "summary": "主张并无禁止个人向问题的必要：算法上不会被强力推荐，看到的人很少，不必赶尽杀绝。",
                    "role": "claim"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P003",
                        "P004"
                    ],
                    "summary": "禁令的维护成本：要投入裁判资源，还要承担维护不力造成的规则严肃性损失；换来的是“美誉”而已。",
                    "role": "reason"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P005",
                        "P006",
                        "P007"
                    ],
                    "summary": "该“美誉”是双刃剑且对观众只是可有可无的收益：真正吸引人的是实际质量而非规则；但对提问者有明显负效应。",
                    "role": "reason"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P008"
                    ],
                    "summary": "规则的根本缺陷：所有问题本质上都必然兼具私人性，每个提问者都有“私人性”的【原罪】。",
                    "role": "claim"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P009",
                        "P010",
                        "P011"
                    ],
                    "summary": "以达尔文与加拉帕戈斯雀为例：只要存在第二个人，问题就不再是纯粹私人的；并给出唯一可操作的法则——沾有公共性即可救赎私人性。",
                    "role": "example"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P012",
                        "P013",
                        "P014",
                        "P015"
                    ],
                    "summary": "推论：确定公共性的唯一条件是“公开发表”；知乎因此不得不无休止辩护、依靠威权，持续消耗公信力，成为永远的开放伤口。",
                    "role": "reason"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P016",
                        "P017"
                    ],
                    "summary": "划界：可以用违法、公序良俗、商业价值等理由禁止，但不能以“不具有（足够）公共性”禁止；公共性应由公众反应而非编辑决定，否则是以公共为名的偷换。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P018",
                        "P019",
                        "P020"
                    ],
                    "summary": "以“罪名”与“收益”的追问加重代价讨论：这样做不会被判无罪，而所得收益可用别的手段获得。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P021",
                        "P022"
                    ],
                    "summary": "替代方案与结论：只需提供“屏蔽该提问者的问题”的功能即可消灭分流效应；能靠“自然法”解决的改用专项立法是错误决策。",
                    "role": "action_advice"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "任何问题都是成本收益问题——作者以此作为分析该禁令的前提。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为没有禁止个人向问题的必要：算法上不会强力推荐，看到的人很少，无需赶尽杀绝。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "立下禁令就要投入裁判资源维护，并承担维护不力导致规则严肃性认知度的损失，作者判定这是一场注定失败、只是看输到什么程度的努力。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为该禁令的“美誉”对观众只是可有可无的收益，真正吸引答题者与阅读者的是实际质量；只要总体质量高于百度知道等对手，有无这条规则都不影响流向。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为这条规则存在根本缺陷：所有问题在本质上都必然兼具私人性，每个提问者追根到底都有“私人性”的【原罪】。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者给出可操作法则：只要沾有一点公共性就可以救赎问题的全部私人性，而不是相反；反过来会因原罪而逻辑触礁。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者断言确定一个问题公共性的唯一条件仅仅是“公开发表”，因此客观上不能以“仅具私人性而不具公共性”否决任何公开发表了的问题。",
                    "evidence": [
                        "E7"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者判断由于这一逻辑破洞，知乎不得不无休止为自己的裁决辩护，且辩护得不到逻辑支持、本质上依靠威权地位被接受，将持续消耗公信力并成为永远的开放伤口（但不见得威胁生存）。",
                    "evidence": [
                        "E8",
                        "E9"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者划出禁止的边界：可以用“违法”“违背公序良俗”“不具有足够商业价值”等规则禁止某些问题，但逻辑上不可以以“不具有（足够）公共性”来禁止。",
                    "evidence": [
                        "E10"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为是否具有“足够的”公共性不应由知乎编辑决定，而应由公众自己的反应给出客观结果；由编辑决定就变成“不具（令我满意的）公共性”，是以公共为名的最糟糕偷换。",
                    "evidence": [
                        "E11"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者给出的替代做法：即使完全不依赖算法，只提供“屏蔽该提问者的问题”的功能，就能天然消灭这些问题的分流效应。",
                    "evidence": [
                        "E12"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "结论：能依赖“自然法”解决的问题改用专项立法解决，是一种错误的决策。",
                    "evidence": [
                        "E13"
                    ]
                }
            ],
            "argument_steps": [
                "定义/前提：任何问题都是成本收益问题（P001）。",
                "必要性判断：算法不会强力推荐、看到的人少，故没有禁止的必要（P002）。",
                "成本核算：禁令需要裁判资源维护，且维护不力会损失规则严肃性的认知度，作者称之为注定失败的努力（P003）。",
                "收益追问：“美誉”是何种收益？（P004）该美誉是双刃剑，会让写问题的人担心投入的生命白费（P005）；对观众是可有可无的收益，实际质量才决定流向（P006）；对提问者的负效应却明显（P007）。",
                "根本缺陷：所有问题本质上必然兼具私人性，提问者都有“私人性”的【原罪】（P008）。",
                "例证：演化论未被认可前是达尔文的个人私念；若他单独提出关于加拉帕戈斯雀的个人问题求助，是否不应得到帮助？（P009）只要存在第二个人，该问题就不是纯粹的私人问题（P010）。",
                "法则与反证：“只要沾有一点公共性，就可以救赎问题的全部私人性，而不是相反”是唯一可实际操作的法则，反过来会因原罪而逻辑触礁（P011）。",
                "推论：确定公共性的唯一条件仅是“公开发表”，故不能以仅具私人性否决公开发表的问题（P012）。",
                "后果推演：逻辑破洞使知乎无休止辩护、依靠威权被接受（P013），消耗公信力（P014），是永远的开放伤口但不必然威胁生存（P015）。",
                "让步/划界：可用违法、公序良俗、商业价值等理由禁止，但不可用公共性不足禁止（P016）。",
                "理由：公共性应由公众反应给出客观结果，由编辑决定即为“不具（令我满意的）公共性”，是以公共为名的偷换，并援引历史教训反问（P017）。",
                "加重：以“你一定不会被判无罪”“背这样的罪名，到底收益是什么呢？”追问代价（P018、P019、P020）。",
                "替代方案：提供“屏蔽该提问者的问题”功能即可消灭分流效应（P021）。",
                "结论：能依赖“自然法”解决的问题改用专项立法解决，是错误决策（P022）。"
            ],
            "concept_usage": [
                {
                    "term": "成本收益问题",
                    "meaning": "作者用于衡量平台规则的一般框架：把该禁令放在收益与成本两侧核算。",
                    "evidence": "P001",
                    "ambiguity": "作者未给出量化标准，仅作定性比较。"
                },
                {
                    "term": "私人性 / 【原罪】",
                    "meaning": "指问题必然带有提问者个人的关切；作者称每个提问者追根到底都有私人性的“原罪”，即私人性无法被彻底清除。",
                    "evidence": "P008",
                    "ambiguity": "“原罪”在本文是比喻性说法，与后文基督教语境无关，正文未做界定。"
                },
                {
                    "term": "公共性",
                    "meaning": "决定一个问题是否值得在平台存在的问题属性；作者主张其唯一判定条件是“公开发表”，并应由公众反应客观给出。",
                    "evidence": "P011",
                    "ambiguity": "与“足够的公共性”并用，作者未给出“足够”的门槛。"
                },
                {
                    "term": "公开发表",
                    "meaning": "作者认为这是确定一个问题公共性的唯一条件。",
                    "evidence": "P012",
                    "ambiguity": "无。"
                },
                {
                    "term": "威权地位",
                    "meaning": "作者对知乎裁决被接受方式的描述：辩护得不到逻辑支持，本质上依靠威权地位而被接受。",
                    "evidence": "P013",
                    "ambiguity": "无。"
                },
                {
                    "term": "自然法",
                    "meaning": "作者用以指称不依赖专项立法的自然调节机制（如屏蔽功能带来的自然分流）。",
                    "evidence": "P022",
                    "ambiguity": "作者未定义其确切范围，属借用词语。"
                },
                {
                    "term": "美誉",
                    "meaning": "作者给禁令换来的声誉加引号，指“我们重视问题质量，而且像猎犬一样严防死守”的名声。",
                    "evidence": "P004",
                    "ambiguity": "加引号表示作者对其为真实收益持保留。"
                }
            ],
            "examples_and_targets": [
                "百度知道——作为竞争对照对象，作者称只要知乎问题总体质量高于这类对手，有无规则都不影响流向（P006）。",
                "达尔文与演化论、加拉帕戈斯雀——作者假设性例证，用来说明私人问题求助的正当性（P009、P010）。",
                "“屏蔽该提问者的问题”功能——作者提出的替代手段（P021）。",
                "“历史上无数的鲜血为此而流”——作者以历史教训作修辞性论据，未指明具体事件（P017）。",
                "被反驳对象：知乎以“不具有（足够）公共性”为由禁止某些问题的做法（P016、P017）。"
            ],
            "conditions": [
                "“只要哪怕存在第二个人，加拉帕戈斯雀问题就不是一个纯粹的私人问题”（P010）——公共性成立的最低条件。",
                "“只要沾有一点公共性，就可以救赎问题的全部私人性”（P011）——法则的适用条件。",
                "“只要知乎问题的总体质量高于百度知道这些对手，其实有无这条规则都不影响这两者的流向”（P006）——结论依赖的对照条件。",
                "“即使完全不依赖算法，只是提供一个‘屏蔽该提问者的问题’的功能”（P021）——替代方案的假设前提。",
                "“虽然这不见得会威胁到知乎的生存”（P015）——作者对后果范围的自我限定。",
                "“你可以用‘违法’‘违背公序良俗’‘不具有足够商业价值’等等规则去禁止某些问题”（P016）——承认其他禁止理由仍可用。"
            ],
            "rhetoric_and_tone": "评论与论辩混合的语气：开篇以格言式短句立论，中段以反问推进（“而这个努力到底换到了什么好处呢？”“背这样的罪名，到底收益是什么呢？”），并给“美誉”加引号表示反讽；对知乎用“你一定不会被判无罪”一类法庭隐喻施压，结尾以“专项立法/自然法”的对照作出判断。第二人称“你”面向平台决策者，措辞直接，但不作人身攻击。",
            "unresolved_questions": [
                "“个人解答向问题”在知乎具体指何种内容形态，正文未说明。",
                "“私人性”的【原罪】是否为作者的正式提法、其来源与含义，正文未说明。",
                "P017“历史上无数的鲜血为此而流”所指的具体历史事件，正文未说明，需外部核查。",
                "作者自陈“刚才已经说了”的屏蔽功能建议，其与算法推荐的具体关系，正文未展开。",
                "brief 为正文摘录而非独立信息，以正文为准；本文无版本差异记录。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "任何问题都是成本收益问题。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "其实并没有禁止的必要",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "这是一场注定失败、只是看输到什么程度的努力。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P006",
                    "quote": "只要知乎问题的总体质量高于百度知道这些对手，其实有无这条规则都不影响这两者的流向。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P008",
                    "quote": "所有的问题在本质上都必然兼具私人性",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P011",
                    "quote": "只要沾有一点公共性，就可以救赎问题的全部私人性，而不是相反",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P012",
                    "quote": "确定一个问题的公共性的唯一条件，仅仅是“公开发表”而已",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P013",
                    "quote": "本质上一直是依靠威权地位而被接受",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P015",
                    "quote": "但是这将永远是一个开放伤口。",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P016",
                    "quote": "但逻辑上不可以以“不具有（足够）公共性”来做禁止。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P017",
                    "quote": "而应该由公众自己的反应来给出客观的结果",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P021",
                    "quote": "只是提供一个“屏蔽该提问者的问题”的功能",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P022",
                    "quote": "能依赖“自然法”解决的问题，改用专项立法解决，是一种错误的决策。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "平台治理",
                "内容社区规则",
                "言论与公共性"
            ],
            "issue_candidates": [
                "个人向提问是否应被禁止",
                "平台规则的合法性来源",
                "公共性的判定权归属",
                "平台公信力成本"
            ],
            "text_function_candidates": [
                "评论",
                "论辩",
                "批评",
                "建议"
            ],
            "object_candidates": [
                "知乎",
                "知乎编辑",
                "百度知道",
                "达尔文",
                "加拉帕戈斯雀",
                "提问者"
            ],
            "working_keywords": [
                "个人解答向问题",
                "成本收益问题",
                "私人性",
                "原罪",
                "公共性",
                "公开发表",
                "威权地位",
                "自然法",
                "专项立法",
                "屏蔽该提问者的问题"
            ]
        },
        "notes": "无图片节点。正文中 P017 提到“历史上无数的鲜血为此而流”属未指名的事实断言，已登记为待外部核查。brief 与正文高度重叠（为正文缩写），未用于支持任何主张。"
    },
    "3d075c9c": {
        "analysis": {
            "question_context": "提问者的问题是“已经被养废的孩子，还有救吗？”，属求助/求判断的育儿情境。作者不接受“废”这一判断本身：先劝阻学生群体作答，再指出“废与不废，非人所能言”，随后给出可操作的帮助原则与宗教语境下的理由。提问者的“养废”预设未被归给作者——作者明确否认人有资格作此断言。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002",
                        "P003",
                        "P004"
                    ],
                    "summary": "开篇限定回答者资格：学生不要回答，其代入式回答对提问者无参考意义；并提出教育及格线与绝大多数普通人资源有限的现实。",
                    "role": "qualification"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P005",
                        "P006"
                    ],
                    "summary": "转折后给出核心判断：问题问错了——废与不废，非人所能言。",
                    "role": "claim"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P007",
                        "P008",
                        "P009",
                        "P010"
                    ],
                    "summary": "划界：你最多有权说“我不知道如何扭转”，这不能等于“这人废了”；从前者跳到后者等于自命为主宰天地的神。",
                    "role": "reason"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P011",
                        "P012"
                    ],
                    "summary": "揭露“口称废了”的动机：下意识想获得他人“免予起诉”的判决，即预先推卸未尽努力的责任。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P013",
                        "P014",
                        "P015",
                        "P016"
                    ],
                    "summary": "信仰语境下的判断：自封为神的行为诅咒了自己的努力；停止断言“废了”即能改变努力对对方影响的基调。",
                    "role": "claim"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P017",
                        "P018",
                        "P019",
                        "P020"
                    ],
                    "summary": "行动要求：不要以“有希望才行动”为动力逻辑；人无法控制明天，故无权谈有无希望；应因天降的责任量力而行地去做，不问后果与好处。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P021",
                        "P022",
                        "P023",
                        "P024"
                    ],
                    "summary": "量力而为的边界与立场优先：不要付出付出不起的以免生怨念，不要贪图“好人”的功德；站稳敬畏、谦抑（无害有益）立场后所做才具帮助性质，此法则适用于一切人类施助情形。",
                    "role": "qualification"
                },
                {
                    "unit_id": "U011",
                    "paragraph_refs": [
                        "P025",
                        "P026",
                        "P027",
                        "P028",
                        "P029",
                        "P030",
                        "P031",
                        "P032",
                        "P033",
                        "P034"
                    ],
                    "summary": "具体操作总原则：立足于增进他人的选择空间；附条件给学费是增加选择空间，附义务给学费是剥夺选择空间；分纯增加与有机会成本两种情况，后者依赖对方自由意志、不可强迫。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U012",
                    "paragraph_refs": [
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
                        "P045"
                    ],
                    "summary": "原理与目的：选择余地增多会增强对生活的信心，越过阈值即可根本改变行为方向；青少年问题多出于绝望，他们需要的是生命，而生命的本质是可能性的总和；弃死向生后外在资源才能造成善果。",
                    "role": "reason"
                },
                {
                    "unit_id": "U013",
                    "paragraph_refs": [
                        "P046"
                    ],
                    "summary": "引述块：专对基督徒说明的段落——神赐予人生命，增加他人的可能性与神的爱同心同向，善行的结果来自上帝对祈祷的回应，基督徒没有资格自称施主。",
                    "role": "claim"
                },
                {
                    "unit_id": "U014",
                    "paragraph_refs": [
                        "P047",
                        "P048"
                    ],
                    "summary": "结尾：单字“祈祷”与圣诞祝福，交代写作时点。",
                    "role": "transition"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者劝阻学生回答此问题：学生只是代入角色说出自己想要得到的待遇，对提问者没有特别参考意义。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者提出教育及格线：孩子不反社会、无犯罪倾向、身体基本健康、有基本科学知识和社会常识即算及格；把期望设得更高是很需要勇气、令人钦佩和同情的做法。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者认为这个问题问错了：废与不废，非人所能言。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者划界：无论父母、教育者还是旁观者，最多有权说“这种情况我不知道如何扭转”，但不能由此推出“这人没有希望”或“这人废了”。",
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
                    "statement": "作者判定从“我看不出办法扭转”跳到“这人废了”，等于自命为主宰天地的神。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者分析“口称废了”的动机：本质上只是下意识想获得他人“免予起诉”的判决，即预先为自己没做的努力开脱。",
                    "evidence": [
                        "E7"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者对有信仰者说：自封为神的行为本身已经诅咒了可能做过的一切努力，使其结果指向恶的方向。",
                    "evidence": [
                        "E8"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者主张仅停止断言“废了”这一改变，就能首先获得最基本的祝福并改变努力对对方影响的基调，即使实际行为没有变化。",
                    "evidence": [
                        "E9"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者反对“一定要有有效的期望，我才有动力去做些事情”的行为逻辑，并主张人无权谈有无希望：明天发生什么无法控制，觉得有希望或没希望都是假的。",
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
                    "statement": "作者的行动要求：把这件事当作天降的责任与义务，不问后果、不问希望，量力而行地尽量去做。",
                    "evidence": [
                        "E12"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者限定付出的边界：不要付出自己付出不起的，以免后来横生怨念；并指出最大的危险是动机上想贪这份“好人”的功德。",
                    "evidence": [
                        "E13"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者主张站稳敬畏、谦抑的“无害有益”立场后，做什么都可以并且最终会有好的果效；此法则适用于一切想做教育或想施予帮助的人类情形。",
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
                    "statement": "作者给出“永远不错的总原则”：立足于增进他人的选择空间；凡根本性质是增加对方选择空间的行为都可定性为帮助。",
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
                    "statement": "作者以附条件与不附条件的给学费为例，说明附加义务的要求会剥夺对方的选择空间，不附条件的帮助则增加选择空间。",
                    "evidence": [
                        "E18"
                    ]
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者对存在机会成本的帮助给出条件：若你不是对方的监护人，就可以依赖对方（或监护人）的自由意志来选择是否付出，不强迫即自然在红线之内。",
                    "evidence": [
                        "E19"
                    ]
                },
                {
                    "claim_id": "C016",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者给出的原理：选择余地增多——尤其是出现自己没有想到还存在的选择余地——会使人对生活的信心增强，强到一定阈值以上就能根本改变人的行为方向。",
                    "evidence": [
                        "E20",
                        "E21"
                    ]
                },
                {
                    "claim_id": "C017",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判断绝大部分青少年（乃至人类）的问题都出于绝望，他们需要的不是“帮助”而是生命，首先要传递给他们的是生命。",
                    "evidence": [
                        "E22",
                        "E23"
                    ]
                },
                {
                    "claim_id": "C018",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者定义生命的本质是可能性的总和，并认为弃死向生后求生的决心会启动人与世界的良性互动循环，外部资源才不致被变卖换取快感。",
                    "evidence": [
                        "E24",
                        "E25"
                    ]
                },
                {
                    "claim_id": "C019",
                    "claim_type": "quoted_or_cited",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "在标为引述块、专对基督徒说的段落中，作者论述神赐予人生命、增加他人的可能性与神的爱同心同向同质，善行的结果来自上帝对祈祷的回应，基督徒没有资格自称施主。",
                    "evidence": [
                        "E26",
                        "E27"
                    ]
                }
            ],
            "argument_steps": [
                "限定回答者资格：学生不要回答，代入式回答对提问者无参考意义；且客观条件未必够满足其所期待的待遇（P001）。",
                "现实前提：在教育所需清单面前，绝大多数普通人的能力和资源苍白无力（P002）；给出教育及格线，指出更高期望需要勇气（P003）。",
                "核心判断：这个问题问错了——废与不废，非人所能言（P006）。",
                "划界：你最多有权说“这种情况我不知道如何扭转”，但不能等于“这人没有希望”或“这人废了”（P007、P008）。",
                "归谬：从前者跳到后者等于自命为主宰天地的神，并以“你是世界之巅吗？”反问（P009、P010）。",
                "动机揭露：口称“废了”是为取得他人的“免予起诉”判决（P011），且无人能逃脱这责备（P012）。",
                "信仰语境：自封为神诅咒了自己的努力（P013）；停止断言“废了”即可获得最基本的祝福并改变影响基调（P014、P015、P016）。",
                "动力逻辑替换：反对“有有效期望才有动力”，声明人无法控制明天因而无权谈希望（P017、P018）。",
                "行动要求：因天降的责任和义务，不问后果与希望，量力而行地尽量去做，不抱“不见兔子不撒鹰”的态度（P019、P020）。",
                "边界与动机警示：不要付出付出不起的、不要贪图功德，最大危险是贪“好人”的功德（P021）。",
                "立场优先：站稳敬畏、谦抑的“无害有益”立场，才有帮助的性质，再谈效率与大小（P022、P023）；此法则适用于一切人类施助情形（P024）。",
                "具体原则：总原则是立足于增进他人的选择空间（P027、P028），并以给学费的两个例子区分增加与剥夺（P029、P030）；遇事自问是增加还是剥夺（P031）。",
                "分情况：纯增加的帮助不必多虑（P032）；有机会成本的帮助依赖对方自由意志、不强迫即不越红线（P033、P034）。",
                "原理：选择余地增多增强生活信心（P035），越过阈值根本改变行为方向（P036）；青少年问题多出于绝望（P037），需要的是生命（P038、P039）。",
                "定义：生命的本质是可能性的总和（P041）；弃死向生启动良性循环，外部资源才可能造成善果（P043）。",
                "宗教层说明（引述块）：增加他人的可能性与神的爱同向同质，善行结果归于上帝对祈祷的回应，故基督徒无资格自称施主（P046）。",
                "结尾：祈祷、祝圣诞快乐（P047、P048）。"
            ],
            "concept_usage": [
                {
                    "term": "废（养废/废了）",
                    "meaning": "作者拒绝承认的判断：对他人未来可能性的终局性否定；作者主张人没有资格作此断言。",
                    "evidence": "P006",
                    "ambiguity": "提问者用“养废”描述既成状态，作者只否定判断权，未讨论该状态的具体所指。"
                },
                {
                    "term": "自封为神",
                    "meaning": "作者对“断言他人废了”这一行为的定性：越过人的认知权限去决定他人的结局。",
                    "evidence": "P009",
                    "ambiguity": "无。"
                },
                {
                    "term": "免予起诉",
                    "meaning": "作者对“口称废了”动机的比喻：预先取得他人对自己未尽努力的宽免。",
                    "evidence": "P011",
                    "ambiguity": "属法庭隐喻，非法律用语。"
                },
                {
                    "term": "选择空间",
                    "meaning": "作者提出的总原则中的核心量：帮助是否成立取决于是否增加对方的选择空间。",
                    "evidence": "P027",
                    "ambiguity": "作者未给出度量方式，但用给学费两例作了正反说明（P029、P030）。"
                },
                {
                    "term": "生命",
                    "meaning": "作者将其定义为可能性的总和，是青少年真正需要、需要被传递的东西。",
                    "evidence": "P038",
                    "ambiguity": "与日常生物学含义不同，属作者的定义用法。"
                },
                {
                    "term": "弃死向生",
                    "meaning": "指对生丧失信心者转向求生，从而点燃内在引擎、启动人与世界的良性互动循环。",
                    "evidence": "P043",
                    "ambiguity": "无。"
                },
                {
                    "term": "功德",
                    "meaning": "作者警示的动机风险：把帮助当作可贪图的“好人”功德。",
                    "evidence": "P021",
                    "ambiguity": "带引号使用，含宗教语感。"
                }
            ],
            "examples_and_targets": [
                "学生群体——作者指定的“不该回答者”，理由是其代入角色、缺乏参考意义（P001）。",
                "“如果你想上大学，我可以帮你解决部分学费”——作者用以说明增加选择空间的正面例子（P029）。",
                "“我给你学费，你要给我努力去上大学，不然对不起我”——作者用以说明剥夺选择空间的负面例子（P030）。",
                "教绘画、带旅游——作者用以说明存在机会成本的帮助的例子（P033）。",
                "父母、教育者、旁观者——作者分析的判断主体（P007）。",
                "基督徒——P046 引述块的指定读者。",
                "被反驳对象：“口称‘废了’的人”及其推卸责任的逻辑（P011、P012）；“一定要有有效的期望，我才有动力去做些事情”的行为逻辑（P017）。"
            ],
            "conditions": [
                "“除非你是豪富之家，否则养育他人的资源对一般人真不是小事”（P001）——资源条件的限定。",
                "教育及格线仅覆盖不反社会、无犯罪倾向、身体基本健康、有基本科学知识和社会常识（P003）。",
                "P013—P016 的祝福论述以“如果你是有信仰的人”“如果你指望你的努力真的得到上天祝福”为前提。",
                "“但我们人类算是什么牌面的东西？我们没有能力控制明天发生什么事”（P018）——作者对希望判断所设的认识论限制。",
                "“不要付出你付出不起的，免得自己后来又横生怨念”（P021）——量力而为的边界。",
                "“这一点你都站不住，那么你的努力首先都还不好说到底是帮助还是伤害”（P023）——立场优先于方法。",
                "“如果你足够幸运，不是对方的监护人，你就可以依赖于对方的自由意志来解决问题”（P033）——存在机会成本时的适用条件。",
                "“只要你守住这个原则，就不必过于顾虑到底做得对与不对”（P034）——原则成立即可放宽具体判断。",
                "“只要你是一个人类，这条基本法则就适用”（P024）——适用对象范围。",
                "“如果你这样的人足够多，那么你们所帮助的对象就有可能弃死向生”（P042）——条件式表述，未断言必然。"
            ],
            "rhetoric_and_tone": "训诫与劝勉混合、宗教语汇浓厚的语气：以“首先……然后……”分段推进，直接以“你”称呼读者并连用反问（“你觉得没希望，于是这人就没有希望了？”“你是世界之巅吗？”）；有口语化斥责（“什么狗屁有希望没希望？”）与自嘲式表达（“我们人类算是什么牌面的东西”）；对读者下判断（“每一个口称‘废了’的人，有一个算一个，没有一个能逃脱这责备”）；末段以单字“祈祷”和“祝各位圣诞快乐”收束，交代写作时点（圣诞节前后）。P046 为独立引述块形式，作者在块内自设说话对象（基督徒）。",
            "unresolved_questions": [
                "P046 在 lexical 中是 quote 节点，但正文并未标明被引用的外部作者或经文出处；此处按“作者专对基督徒的说明段落”处理，是否存在外部引用来源需外部核查。",
                "P001 与 P023—P024 的“学生”“一切人类”等主体范围，正文未给出更明确的界定。",
                "“加拉帕戈斯”式的具体案例在本文无；正文未提供任何被判断为“养废”的具体个案细节，故对提问者情境的直接适用性未说明。",
                "“祝福”“赏赐”“恶的方向”等表述的判定标准，正文未说明。",
                "P047 单字“祈祷”、P048“祝各位圣诞快乐”与正文论证的关系，正文未说明。",
                "版本信息：updated_at 为 2021-07-25，晚于 published_at 2019-12-26；正文是否经修改、修改了哪些内容，语料未提供差异，需外部核查。",
                "本文无图片节点；P046 的目录差异已由生成器记录（lexical true 为 quote 节点、P047 为 lexical 未覆盖片段），不影响正文阅读。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "这个问题，学生们就不要回答了好吗？",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P003",
                    "quote": "教出来的孩子不反社会、没有犯罪倾向，身体基本健康，有基本科学知识和社会常识，就算教育及格了。",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P006",
                    "quote": "废与不废，非人所能言。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P007",
                    "quote": "你最多有权说“这种情况我不知道如何扭转”",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P008",
                    "quote": "完全不能等于“这人没有希望”或者“这人废了”。",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P009",
                    "quote": "就等于首先自命为主宰天地的神了。",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P011",
                    "quote": "本质上只是下意识的想要获得他人的“免予起诉”判决",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P013",
                    "quote": "已经诅咒了你可能做过的一切努力",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P015",
                    "quote": "就能首先获得最基本的祝福",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P017",
                    "quote": "一定要有有效的期望，我才有动力去做些事情",
                    "relation": "contradicts"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P018",
                    "quote": "我们没有能力控制明天发生什么事，哪有资格谈一个东西到底有希望没希望？",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P019",
                    "quote": "你就量力而行的尽量去做，就是这样。",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P021",
                    "quote": "不要付出你付出不起的",
                    "relation": "supports"
                },
                {
                    "key": "E14",
                    "paragraph_id": "P023",
                    "quote": "先站稳了这个“无害有益”的立场",
                    "relation": "supports"
                },
                {
                    "key": "E15",
                    "paragraph_id": "P024",
                    "quote": "只要你是一个人类，这条基本法则就适用。",
                    "relation": "supports"
                },
                {
                    "key": "E16",
                    "paragraph_id": "P027",
                    "quote": "但我可以给你一个永远不错的总原则——立足于增进他人的选择空间。",
                    "relation": "supports"
                },
                {
                    "key": "E17",
                    "paragraph_id": "P028",
                    "quote": "如果最后的根本性质是你增加了对方的选择空间，这种行为都可以定性为帮助。",
                    "relation": "supports"
                },
                {
                    "key": "E18",
                    "paragraph_id": "P030",
                    "quote": "这却是剥夺了对方的选择空间。",
                    "relation": "supports"
                },
                {
                    "key": "E19",
                    "paragraph_id": "P033",
                    "quote": "你就可以依赖于对方的自由意志来解决问题",
                    "relation": "supports"
                },
                {
                    "key": "E20",
                    "paragraph_id": "P035",
                    "quote": "ta对生活的信心一定会增强。",
                    "relation": "supports"
                },
                {
                    "key": "E21",
                    "paragraph_id": "P036",
                    "quote": "就能根本的改变人的行为方向",
                    "relation": "supports"
                },
                {
                    "key": "E22",
                    "paragraph_id": "P037",
                    "quote": "绝大部分青少年（乃至于人类）的问题，都是出于绝望",
                    "relation": "supports"
                },
                {
                    "key": "E23",
                    "paragraph_id": "P038",
                    "quote": "他们需要的不是“帮助”，他们需要的是生命。",
                    "relation": "supports"
                },
                {
                    "key": "E24",
                    "paragraph_id": "P041",
                    "quote": "生命的本质，是可能性的总和。",
                    "relation": "supports"
                },
                {
                    "key": "E25",
                    "paragraph_id": "P043",
                    "quote": "启动人与世界的良性的互动循环",
                    "relation": "supports"
                },
                {
                    "key": "E26",
                    "paragraph_id": "P046",
                    "quote": "因此，增加他人的可能性，必然与神的爱同心同向，因而也同质。",
                    "relation": "supports"
                },
                {
                    "key": "E27",
                    "paragraph_id": "P046",
                    "quote": "因此一个基督徒是没有任何资格自称施主的。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "教育",
                "家庭养育",
                "伦理学",
                "宗教（基督教）"
            ],
            "issue_candidates": [
                "能否断言他人“废了”",
                "帮助的正当性与边界",
                "选择空间与信心",
                "施助动机与功德"
            ],
            "text_function_candidates": [
                "答疑",
                "训诫",
                "劝勉",
                "经验总结",
                "宗教劝谕"
            ],
            "object_candidates": [
                "提问者",
                "学生",
                "父母",
                "教育者",
                "旁观者",
                "青少年",
                "基督徒",
                "上帝"
            ],
            "working_keywords": [
                "养废",
                "废与不废，非人所能言",
                "自封为神",
                "免予起诉",
                "量力而行",
                "选择空间",
                "可能性",
                "生命的本质",
                "弃死向生",
                "功德",
                "祈祷"
            ]
        },
        "notes": "无图片节点。结构差异：generator 记录 divergence=true——lexical 中 P046 为 quote 节点（P001—P045、P047—P048 为 paragraph），正文 text 未标注引用来源；P047“祈祷”被标为 lexical 未覆盖片段。作者在 P046 段首自述“以下这一段是专们说给基督徒看”，故按作者面向基督徒的说明段落处理，非转述他人观点；若后续核查确认其为外部引文，需改标 quoted_or_cited 与相应 attribution。"
    },
    "82389177": {
        "analysis": {
            "question_context": "提问者的问题是“十四岁的孩子说出‘我不要洗碗，因为这是很低贱的事情’这种话，我要如何回应？”——属求教育方法的求助。作者没有直接给“怎么回应”的话术，而是先质疑成人对“工作无贵贱”的坚持，再拆解工作属性与工作态度两个层面，最后给出对“低贱”的重新界定与处世建议。提问者转述的孩子之语属被讨论对象，未被归给作者。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "开篇设问：各位是觉得孩子说得不对，还是觉得说得对、只是不该说？把争点从内容转向言说行为。",
                    "role": "context"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P003",
                        "P004",
                        "P005",
                        "P006",
                        "P007",
                        "P008",
                        "P009"
                    ],
                    "summary": "以“交换工作”思想实验反驳“工作无高下之分”：既然舍不得换，就说明有高低；退一步只承认有高低无贵贱，也无法解释听到“低下”时的愤怒。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P010",
                        "P011",
                        "P012",
                        "P013",
                        "P014"
                    ],
                    "summary": "指出反对的真正对象可能不是说出的内容而是说出的动作；以“国王的新衣”与小男孩作比，讽刺成人的自我安慰与报复心态。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P015",
                        "P016",
                        "P017"
                    ],
                    "summary": "点出待解问题“的确存在卑贱的岗位”，并把流行的政治正确方案定性为皇帝新衣式的虚词伪饰，在事实层面不堪一击、还要在孩子面前硬拗撒谎。",
                    "role": "claim"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P018",
                        "P019"
                    ],
                    "summary": "提出解释框架：社会地位如虎符分两半——工作的属性有高下之分，工作的态度有优劣之别；岗位是否低下常非本人可选择，没有选择就没有罪恶。",
                    "role": "definition"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P020",
                        "P021",
                        "P022"
                    ],
                    "summary": "由此推出对他人社交资源分配的理解与接受义务，并以“让他人活”作结。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P023",
                        "P024",
                        "P025",
                        "P026",
                        "P027",
                        "P028",
                        "P029",
                        "P030",
                        "P031",
                        "P032"
                    ],
                    "summary": "反驳“凭什么要我软弱”的反弹：要求人不区分可替换性地投注社交资源是一种暴政；只有这种心态会停止下滑，仁德者会获得下意识的亲近，这即“偏心”的本质。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P033",
                        "P034"
                    ],
                    "summary": "转入虎符的另一半：岗位卑贱不由你选，虽会导致社交资源不倾斜，但还谈不上沦为下流。",
                    "role": "transition"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P035",
                        "P036",
                        "P037",
                        "P038"
                    ],
                    "summary": "反例：仅因岗位卑贱就无礼待人的蠢人不会有出息；对卑贱的恐惧驱使往上爬，而大事业的人力金字塔必然有大量卑贱下层岗位，且只能由态度同样卑贱者填充。",
                    "role": "reason"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P039",
                        "P040",
                        "P041",
                        "P042",
                        "P043",
                        "P044",
                        "P045",
                        "P046"
                    ],
                    "summary": "以企业内保安、清洁、前台、文员、客服为例说明低岗位士气决定其他部门效率；作践低岗位成员是极其昂贵的蠢行，劝人及时跳槽并警告跳船能力随衰老消退。",
                    "role": "example"
                },
                {
                    "unit_id": "U011",
                    "paragraph_refs": [
                        "P047",
                        "P048",
                        "P049",
                        "P050",
                        "P051",
                        "P052"
                    ],
                    "summary": "正面出路：身处卑贱岗位而态度不卑贱者是团队孜孜以求的珍宝；以人民大会堂清洁、苹果总部保安为例；岗位因你的存在而变得不可替代，态度者稀缺是话事人的心病。",
                    "role": "claim"
                },
                {
                    "unit_id": "U012",
                    "paragraph_refs": [
                        "P053",
                        "P054",
                        "P055",
                        "P056"
                    ],
                    "summary": "结论：不可替代性自然带来尊严；岗位的可替代性可被态度的不可替代性救赎；真正使人低贱的是对低贱岗位采取的低贱态度。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者把争点设为二选一的追问：各位是觉得孩子说得不对，还是觉得说得对、只是不该说？以及到底在反对说出的内容还是说出的动作本身。",
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
                    "statement": "作者以“交换工作”的思想实验反驳工作无高下之分：若真觉得都一样，面对无损于己、有利于对方的交换就没有理由舍不得换，故说明工作有高低之分。",
                    "evidence": [
                        "E3",
                        "E4"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者认为，退一步只辩解“有高低但无贵贱”也无法自洽：若“低下”纯属中性，为何有人说你的工作低下你会愤怒。",
                    "evidence": [
                        "E5",
                        "E6"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者以“国王的新衣”作比推测愤怒的来源：生气是因为国王们确实知道自己没穿新衣、数九寒冬难熬，因而痛恨小男孩伤口撒盐。",
                    "evidence": [
                        "E7"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判定流行的“工作无贵贱之分”方案是皇帝新衣式的政治正确：明知是事实却拒绝面对真相、虚词伪饰，在事实层面不堪一击，还要在小孩面前硬拗撒谎。",
                    "evidence": [
                        "E8",
                        "E9"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提出解释框架：社会地位的虎符分为两半，一半是工作的属性有高下之分，一半是工作的态度有优劣之别，两半合起来才真正决定社会地位。",
                    "evidence": [
                        "E10"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者认为工作职位是否低下、是否具有天然的高可替代性并非全然（有时甚至全然不是）本人可以选择的，并据此提出“没有选择，就没有罪恶”。",
                    "evidence": [
                        "E11",
                        "E12"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者主张他人识别出这种高可替换性而不向你倾注过多社交资源，是你需要理解和接受的，这是你仁爱的义务——让他人活。",
                    "evidence": [
                        "E13",
                        "E14"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者断定要求人不区分可替换性、不分优先级去投注社交资源是一种暴政；社会位阶不高的人也可能是暴君，否则会众叛亲离、妻离子散。",
                    "evidence": [
                        "E15",
                        "E16"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者认为只有上述心态的人才会停止下滑：否则地位会继续被他人按风险控制本能集体性地推挤到更具可替代性的位置，越下沉越依赖“人无贵贱”口号自我安慰。",
                    "evidence": [
                        "E17",
                        "E18"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者解释某些卑微者并未失去尊重的机制：并非善于拍马屁，而是其仁德使他人下意识感到安全，从而不自觉亲近并留三分情——这就是“偏心”的本质。",
                    "evidence": [
                        "E19",
                        "E20"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者判定岗位卑贱不由你选，虽会导致社交资源不向你倾斜，但那还谈不到导致你沦为下流。",
                    "evidence": [
                        "E21"
                    ]
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者预言仅因岗位卑贱就对人无礼的蠢人：第一不会有真出息，第二除非醒悟悔改否则绝对、绝对不会有好下场。",
                    "evidence": [
                        "E22"
                    ]
                },
                {
                    "claim_id": "C014",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者给出的理由链：对卑贱的恐惧驱使往上爬，往上爬必须有大事业，而绝非一个人可做的大事业的人力金字塔里必然有大量卑贱的下层岗位，且只能由态度同样卑贱者填充。",
                    "evidence": [
                        "E23",
                        "E24"
                    ]
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者以企业内保安、清洁、前台接待、复印文员、呼叫中心客服为例，指出这些岗位的工作态度和士气在很大程度上决定企业其他部门的效率，其长期消极抵抗会无声吃掉竞争力与成本。",
                    "evidence": [
                        "E25",
                        "E26"
                    ]
                },
                {
                    "claim_id": "C016",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判定嚣张跋扈、作践低岗位团队成员是极其昂贵的蠢行，劝人若发现团队领袖看不懂这点就及早准备跳槽，并警告跳船能力随衰老不断消退。",
                    "evidence": [
                        "E27",
                        "E28"
                    ]
                },
                {
                    "claim_id": "C017",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出身处卑贱岗位而没有沾染卑贱工作态度的人，将是任何真有宏图大志的团队孜孜以寻的珍宝；不以卑贱态度从事岗位，岗位会因你的存在而变得不可替代。",
                    "evidence": [
                        "E29",
                        "E30"
                    ]
                },
                {
                    "claim_id": "C018",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出懂得并践行此理的人稀缺：岗位本身不稀缺，你这样的人稀缺。",
                    "evidence": [
                        "E31"
                    ]
                },
                {
                    "claim_id": "C019",
                    "claim_type": "author_reported",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者以引号内的第一人称独白，转述“最终话事人们”的心病：团队里连扫地倒茶岗位也需要工作态度绝不卑贱的人，可惜有学历的人太多而有态度的人太少。",
                    "evidence": [
                        "E32"
                    ]
                },
                {
                    "claim_id": "C020",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "结论：不可替代性自然带来尊严，岗位的可替代性可以被态度的不可替代性救赎；的确有低贱的岗位，但那还不足以使你成为低贱的人，对低贱岗位采取低贱态度才使你成为低贱的人——而“这是一种低贱的工作，我才不要干”恰恰是一种低贱的态度。",
                    "evidence": [
                        "E33",
                        "E34",
                        "E35"
                    ]
                }
            ],
            "argument_steps": [
                "把争点设为二选一追问：是觉得孩子说得不对，还是说得对但不该说（P001、P002）。",
                "反驳“工作无高下之分”：设想与觉得你工作更好、能力相当的人交换（对你无损、对ta有收益），追问为何舍不得换（P003—P005），从而推出“有高低之分”（P006）。",
                "继续追问：若只承认有高低但无贵贱，把“低贱”改为“低下”就该没人有意见，可为何仍有人愤愤不平（P007—P009）。",
                "转向言说行为本身：反对的可能是“说出来这个动作”，并以国王的新衣作比，引出讽刺性回应（P010—P014）。",
                "提出待解问题“的确存在卑贱的岗位”，把流行的政治正确方案定性为皇帝新衣式的虚词伪饰（P015、P016）。",
                "给出解释框架：社会地位 = 工作属性（有高下）+ 工作态度（有优劣）（P018）。",
                "第一半：岗位高可替代性常非本人可选，没有选择就没有罪恶（P019）；故他人不向你倾斜社交资源需要理解和接受，这是仁爱义务（P020—P022）。",
                "反驳反弹：要求人不区分可替换性投注社交资源是暴政；只有这种心态会停止下滑，仁德带来下意识的安全与亲近（P023—P032）。",
                "第二半：岗位卑贱不由你选，还谈不到沦为下流（P033、P034）。",
                "反例推演：仅因岗位卑贱而轻慢他人的蠢人不会有好下场（P035）；对卑贱的恐惧驱使其上爬，而大事业金字塔必然有大量卑贱下层岗位（P037、P038）。",
                "企业例证：低岗位成员的士气决定其他部门效率，长期消极抵抗会吃掉竞争力与成本（P039—P041）；加薪可掩盖但不能免除代价（P042、P043）。",
                "行动建议：作践低岗位成员是极昂贵的蠢行，看不懂这点的领袖没有前途，应及早准备跳槽（P045、P046）。",
                "正面出路：态度不卑贱者是稀缺珍宝，岗位因你而不可替代（P047—P052）。",
                "结论：不可替代性带来尊严；可替代性可被态度的不可替代性救赎；使人低贱的是低贱的态度（P053—P056）。"
            ],
            "concept_usage": [
                {
                    "term": "低贱 / 卑贱",
                    "meaning": "作者区分两种用法：用于岗位时指工作的属性（高可替代性、地位低下）；用于人时指其对岗位采取的态度。",
                    "evidence": "P055",
                    "ambiguity": "作者一方面承认“的确有低贱的岗位”，一方面否定“低贱的人”，两处“低贱”含义不同，需按语境区分。"
                },
                {
                    "term": "高低之分 / 贵贱",
                    "meaning": "作者反驳“工作无高下之分”时使用的区分：承认工作有高低，但反对以贵贱为言说方式（P007 转述辩解方口径）。",
                    "evidence": "P006",
                    "ambiguity": "P007 的“有高低，但无贵贱”是作者设想的辩解口径，非作者主张。"
                },
                {
                    "term": "可替代性 / 不可替代性",
                    "meaning": "作者衡量岗位与个人社会地位的核心量：岗位天然高可替代，而人的态度可使岗位因他而变得不可替代。",
                    "evidence": "P019",
                    "ambiguity": "作者未给出可替代性的具体判定标准。"
                },
                {
                    "term": "社会地位的虎符",
                    "meaning": "作者的比喻：社会地位由“工作属性有高下”与“工作态度有优劣”两半合成。",
                    "evidence": "P018",
                    "ambiguity": "“虎符”为比喻，正文未解释其来源。"
                },
                {
                    "term": "暴政 / 暴君",
                    "meaning": "作者对“要求人不区分可替换性、不分优先级去投注社交资源”的定性，并指出位阶不高者也可能成为暴君。",
                    "evidence": "P023",
                    "ambiguity": "属强评价用语，作者未界定其成立标准。"
                },
                {
                    "term": "政治正确",
                    "meaning": "作者用以指“明知事实却强说工作无贵贱之分”的流行方案。",
                    "evidence": "P016",
                    "ambiguity": "带贬义使用。"
                },
                {
                    "term": "仁爱的义务",
                    "meaning": "作者指理解并接受他人基于可替换性分配社交资源的义务。",
                    "evidence": "P021",
                    "ambiguity": "作者未说明该义务的边界。"
                }
            ],
            "examples_and_targets": [
                "十四岁孩子“我不要洗碗，因为这是很低贱的事情”——提问者转述的被讨论对象（P001—P010 讨论其言说）。",
                "交换工作思想实验——作者用以反驳“工作无高下之分”的论证装置（P003、P004）。",
                "国王的新衣与小男孩——作者引用的童话比喻，讽刺成人自我安慰式愤怒（P011—P014）。",
                "人民大会堂区域清洁、苹果总部保安巡逻——作者用以说明某些低岗位实际受尊重的例子（P048、P049）。",
                "企业中的保安大爷、清洁阿姨、前台接待、打印复印文员、呼叫中心客服——作者用以说明低岗位士气影响企业效率的例子（P039）。",
                "“一万二一个月请清洁阿姨”“二十个一万二”——作者用于计算作践低岗位成员代价的假设数字（P042、P043）；属作者设算，非实测数据，需外部核查。",
                "“犯我强汉者虽远必诛”——作者引用的流行语，用以刻画反弹心态（P026）。",
                "被反驳对象：坚持“工作无贵贱之分”的政治正确方案（P016）；要求人不区分可替换性投注社交资源的立场（P023）。"
            ],
            "conditions": [
                "交换工作实验的成立条件：对方能力与你相当、交换对你无损而对ta有收益、且愿意分一半收益给你（P003）。",
                "“没有选择，就没有罪恶”以岗位高可替代性“并非全然是你可以选择的”为前提（P019）。",
                "“除非他能醒悟悔改，否则他绝对、绝对不会有好下场”（P035）——对蠢人的预言以悔改为条件。",
                "“绝非一个人可做的大事业的人力金字塔里，必然有大量卑贱的下层岗位”（P037）——结论依赖“大事业需多人协作”这一前提。",
                "“你不以卑贱的态度去从事你的岗位，那么……你的岗位也会因为你的存在而变得不可替代”（P051）——正面出路以态度为前提。",
                "“你跳船的能力是随着你的衰老不断地消退的”（P046）——行动建议附带的时效条件。",
                "“的确有低贱的岗位，但这还不足以使得你成其为低贱的人”（P055）——作者对自身命题的限定。"
            ],
            "rhetoric_and_tone": "讽刺、训诫与论辩并用的强评价语气：连用反问推进（“你为啥舍不得换？”“为什么还是有人愤愤不平呢？”），以“国王的新衣”“小兔崽子”“真nm没心肝”等口语戏仿成人的自我安慰，称对手立场为“暴政”“暴君”“政治正确”；直接以“你”称呼读者并作预言式警告（“你一天不悔改，你就继续下沉一天”）；亦以企业成本计算与“珍宝”式褒语给出正面出路，末尾以三段短句格言式收束。",
            "unresolved_questions": [
                "P052 引号内的第一人称独白（“我的团队……有态度的人太少”）是作者转述“最终话事人们”的想法还是作者自述，正文未标明说话者，此处按作者转述他人立场处理，需进一步核查。",
                "P042、P043 的“一万二”“二十个一万二”为作者设算数字，无数据来源，需外部核查。",
                "“目前中国行业领先的团队里普遍存在的人力资源短板”属未经证实的事实断言，需外部核查。",
                "人民大会堂、苹果总部两例中“极少有人如此不尊重你”的实际情况，正文未给依据。",
                "作者对“工作无贵贱之分”的批判是否构成对提问者“如何回应孩子”的直接建议，正文未明确给出回应话术。",
                "版本信息：updated_at 为 2025-01-01，晚于 published_at 2019-12-30；正文是否经修改，语料未提供差异，需外部核查。",
                "本文无图片节点。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "各位到底是觉得ta说得不对呢？",
                    "relation": "context"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P010",
                    "quote": "其实你们在反对的到底是小朋友说出来的内容，还是在反对小朋友说出来这个动作本身？",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "工作真的都是没有高下之分的吗？",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P006",
                    "quote": "那么，也就是有高低之分了？",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P007",
                    "quote": "只是想要辩解说有高低，但无贵贱吧？",
                    "relation": "context"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P009",
                    "quote": "那么为什么有人说你的工作低下你要愤怒？",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P011",
                    "quote": "是因为国王们的确知道自己没穿新衣",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P016",
                    "quote": "强要说“工作无贵贱之分”",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P016",
                    "quote": "在事实层面总是不堪一击",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P018",
                    "quote": "一半是工作的属性有高下之分，一半是工作的态度有优劣之别。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P019",
                    "quote": "并非全然是你可以选择的——有时甚至全然不是你可以选择的",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P019",
                    "quote": "没有选择，就没有罪恶。",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P020",
                    "quote": "是你需要理解和接受的。",
                    "relation": "supports"
                },
                {
                    "key": "E14",
                    "paragraph_id": "P022",
                    "quote": "你得让他人活（live and let live）。",
                    "relation": "supports"
                },
                {
                    "key": "E15",
                    "paragraph_id": "P023",
                    "quote": "要求人不区分可替换性、不分优先级去投注社交资源，是一种暴政。",
                    "relation": "supports"
                },
                {
                    "key": "E16",
                    "paragraph_id": "P023",
                    "quote": "不要以为你社会位阶不高，你就不会是一名暴君。",
                    "relation": "supports"
                },
                {
                    "key": "E17",
                    "paragraph_id": "P027",
                    "quote": "凭只有这个心态的人才会停止下滑。",
                    "relation": "supports"
                },
                {
                    "key": "E18",
                    "paragraph_id": "P028",
                    "quote": "你越下沉，你就越会依赖那个“人无贵贱”的政治正确口号来自我安慰",
                    "relation": "supports"
                },
                {
                    "key": "E19",
                    "paragraph_id": "P031",
                    "quote": "在下意识里也感到了安全",
                    "relation": "supports"
                },
                {
                    "key": "E20",
                    "paragraph_id": "P032",
                    "quote": "这三分情，就是你艳羡而诅咒的“偏心”的本质。",
                    "relation": "supports"
                },
                {
                    "key": "E21",
                    "paragraph_id": "P034",
                    "quote": "但那还谈不到导致你沦为下流。",
                    "relation": "supports"
                },
                {
                    "key": "E22",
                    "paragraph_id": "P035",
                    "quote": "除非他能醒悟悔改，否则他绝对、绝对不会有好下场。",
                    "relation": "supports"
                },
                {
                    "key": "E23",
                    "paragraph_id": "P037",
                    "quote": "绝非一个人可做的大事业的人力金字塔里，必然有大量卑贱的下层岗位。",
                    "relation": "supports"
                },
                {
                    "key": "E24",
                    "paragraph_id": "P038",
                    "quote": "只能由工作态度同样卑贱的人填充",
                    "relation": "supports"
                },
                {
                    "key": "E25",
                    "paragraph_id": "P039",
                    "quote": "ta们的工作态度和士气其实在很大程度上决定了这家企业里的其他部门的效率。",
                    "relation": "supports"
                },
                {
                    "key": "E26",
                    "paragraph_id": "P041",
                    "quote": "能无声地吃掉整个企业的竞争力",
                    "relation": "supports"
                },
                {
                    "key": "E27",
                    "paragraph_id": "P045",
                    "quote": "嚣张跋扈，作践低岗位的团队成员，是极其昂贵的蠢行。",
                    "relation": "supports"
                },
                {
                    "key": "E28",
                    "paragraph_id": "P046",
                    "quote": "你跳船的能力是随着你的衰老不断地消退的",
                    "relation": "supports"
                },
                {
                    "key": "E29",
                    "paragraph_id": "P047",
                    "quote": "将是任何真有宏图大志的团队在孜孜以寻的珍宝。",
                    "relation": "supports"
                },
                {
                    "key": "E30",
                    "paragraph_id": "P051",
                    "quote": "你的岗位也会因为你的存在而变得不可替代。",
                    "relation": "supports"
                },
                {
                    "key": "E31",
                    "paragraph_id": "P051",
                    "quote": "岗位本身不稀缺，你这样的人稀缺。",
                    "relation": "supports"
                },
                {
                    "key": "E32",
                    "paragraph_id": "P052",
                    "quote": "可惜有学历的人太多，而有态度的人太少。",
                    "relation": "supports"
                },
                {
                    "key": "E33",
                    "paragraph_id": "P053",
                    "quote": "不可替代性自然带来尊严。",
                    "relation": "supports"
                },
                {
                    "key": "E34",
                    "paragraph_id": "P054",
                    "quote": "岗位的可替代性，可以被态度的不可替代性救赎。",
                    "relation": "supports"
                },
                {
                    "key": "E35",
                    "paragraph_id": "P056",
                    "quote": "而“这是一种低贱的工作，我才不要干”，恰恰是一种低贱的态度。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "职业与社会分层",
                "伦理学",
                "劳动观念",
                "组织管理",
                "家庭教育"
            ],
            "issue_candidates": [
                "工作是否有贵贱",
                "话能不能说与说了会不会被罚",
                "社会地位的构成",
                "对低岗位成员的尊重",
                "政治正确的虚伪"
            ],
            "text_function_candidates": [
                "答疑",
                "论辩",
                "批评",
                "训诫",
                "经验总结"
            ],
            "object_candidates": [
                "提问者",
                "十四岁孩子",
                "保安",
                "清洁工",
                "前台接待",
                "文员",
                "客服",
                "团队领袖",
                "最终话事人",
                "苹果总部",
                "人民大会堂"
            ],
            "working_keywords": [
                "低贱",
                "卑贱",
                "工作无贵贱之分",
                "可替代性",
                "不可替代性",
                "社会地位的虎符",
                "暴政",
                "仁爱的义务",
                "政治正确",
                "皇帝新衣"
            ]
        },
        "notes": "无图片节点。P052 引号内第一人称独白未标明说话者，已登记为待核查（当前按作者转述他人立场计入 C019，modality=reported、attribution=author 表示由作者引出而非作者自身主张）。P042/P043 金额、P052“中国行业领先的团队”均为待外部核查断言。"
    }
}


def main():
    rows = load_batch_rows(BATCH)
    by_uid = {}
    for s in SKELETON:
        by_uid[s['uid']] = s
    records = []
    for row in rows:
        art = row['article']
        uid = art['id'][:8]
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
    write_jsonl(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'out', BATCH + '.out.jsonl'), records)
    print('ok %s' % BATCH)


if __name__ == '__main__':
    main()
