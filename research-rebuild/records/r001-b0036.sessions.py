# -*- coding: utf-8 -*-
"""批次 r001-b0036 的记录构造器（SKELETON 由 build_sessions.py 机械生成）。

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

BATCH = "r001-b0036"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0036.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}

ANALYSIS = {
    "e0f2d1a4": {
        "analysis": {
            "question_context": "提问者的问题：“资本论中的所描写的工人都惨得不像样，是真的吗？”作者未直接回答真伪，而是面对评论区“偷换概念”“为资本家洗地”的指摘（P001），先用两道反问题检验对方定义，再区分“资本罪恶在工厂”与“罪恶在于背叛契约与义务”，最后就中国企业主的“原罪”作出比较性判断。学生党与“很多人”的立场属被反驳对象，未归给作者。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "点名争论语境与对手口径：学生党指责“偷换概念”“为资本家洗地”，作者要求对方先回答问题。",
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
                        "P008"
                    ],
                    "summary": "第一题：若认定企业间供货即剥削，则要消灭剥削就得连商品经济一起消灭、改为完全中央调拨；并追问对方是否认为该模式能带来普遍幸福与国际生存空间。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P009",
                        "P010",
                        "P011",
                        "P012"
                    ],
                    "summary": "第二题：若认定一切雇佣关系都是剥削，则把企业改组为有限责任公司加一批个人独资企业的协作（报酬等于原工资）后，剥削如何神奇消失；若改判为上下游企业间剥削，则唯一解法是彻底毁灭一切经济活动。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P013",
                        "P014"
                    ],
                    "summary": "斥责对手缺乏那个时代与饥饿的经验，把此事当斗嘴游戏，低估其主张背后的经济浩劫。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P015",
                        "P016",
                        "P017"
                    ],
                    "summary": "针对“罪恶在血汗工厂”的流行看法：对工人来说能进这种工厂已是失去一切后的救命稻草，并反问不做这份劳动还能换成什么、救济由谁出。",
                    "role": "rebuttal"
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
                    "summary": "以“直接汇款一半工资”的设算反将对手：不能既不捐献又抱怨税收又指责血汗工厂；若要打击血汗工厂，请申请提高个人所得税税率，因为向厂主征税只会导致通胀或工厂消失而待吃饭者仍在。",
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
                        "P029",
                        "P030"
                    ],
                    "summary": "重述马克思所指的“资本罪恶”：领主先收回佃农土地制造绝境、再开纺织厂让农民接受低工资；真正的罪恶在于未吸纳全部失地农民，而新生产方式本可让全体领民过得更好。",
                    "role": "claim"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P031",
                        "P032",
                        "P033",
                        "P034"
                    ],
                    "summary": "以欧洲伦理说明贵族的牧养职责与誓言：背叛契约、在有选择时选择贪婪才是十恶不赦；并以《唐顿庄园》说明合格贵族承担责任并不轻松。",
                    "role": "reason"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P035",
                        "P036",
                        "P037",
                        "P038"
                    ],
                    "summary": "归结：资本主义的罪恶发生在“有选择且有绝对义务却做了最贪婪的选择”这一步；并解释马克思不再相信贵族精神或教会能解决人类命运问题，故主张消灭私有制/封建制本身。",
                    "role": "conclusion"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P039",
                        "P040",
                        "P041",
                        "P042",
                        "P043"
                    ],
                    "summary": "回到本题：存在选择才存在罪恶的法理基础；中国长期处于生存危机，与羊吃人的贵族有根本差异，故中国小企业主“原罪”小得多——他们并无把人抛入绝境的能力和权柄。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者以反问要求对方先回答：企业之间签供货合同，采购方是否在剥削供应方。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者指出：若按对方定义把企业间供货也算剥削，则要消灭剥削就必须连商品经济一起消灭，把经济活动改为完全的中央调拨。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者反问对方是否认为完全中央调拨的模式才是绝对无罪、并可帮助中国人赢得普遍幸福和国际生存空间，若是则请把论文上交人大政协。",
                    "evidence": [
                        "E3",
                        "E4"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者以第二题反问：若一切雇佣关系都是剥削，那么在业务流程与资金支付不变、仅改组为有限责任公司与个人独资企业协作后，“剥削”如何神奇消失。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者推出对方定义的后果：若把改组后的关系判为上下游企业间的剥削，则唯一解决方案就是彻底毁灭一切经济活动本身。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指责对手没有经历过那个时代、没挨过饿，把这些问题当作斗嘴刷存在感的智力游戏，不知道其主张背后是何等经济浩劫与灾难。",
                    "evidence": [
                        "E7",
                        "E8"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "opponent_view",
                    "attribution": "opponent",
                    "modality": "asserted",
                    "statement": "作者转述并反驳的流行看法：资本的罪恶在工厂、在“不人道”的生产线上。",
                    "evidence": [
                        "E9"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者反驳上述看法：对那些工人而言，能进这样的工厂已经是一无所有、失去一切之后抓住的救命稻草。",
                    "evidence": [
                        "E10"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者以设算反将对手：请好心人把工人请回家、直接按月汇给其一半工资，去掉损耗与行政“先上交后分配”的消耗，直接打钱还更省。",
                    "evidence": [
                        "E11"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出不能既不捐献、又抱怨税收太高、又指责“血汗工厂”；若要打击血汗工厂，请申请提高个人所得税税率。",
                    "evidence": [
                        "E12"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者分析向“黑心工厂主”征税的后果：要么物价普涨（通货膨胀，等效于普遍强制征税），要么工厂普遍消失，而等着吃饭的人并未消失。",
                    "evidence": [
                        "E13",
                        "E14"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者认为马克思所指责的“资本罪恶”不是指开工厂的老板有多邪恶，而是谴责领主先收回佃农土地制造绝境、再开纺织厂让农民接受低工资。",
                    "evidence": [
                        "E15",
                        "E16"
                    ]
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判定真正的罪恶在于：出于对最大利润率的追求，他们所开的工厂没有吸纳全部被他们剥夺土地的失地农民——因为新生产方式本可让全体领民过得比原来更好。",
                    "evidence": [
                        "E17",
                        "E18",
                        "E19"
                    ]
                },
                {
                    "claim_id": "C014",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者从欧洲伦理判定：贵族因承担牧养众民的职责才享有特殊地位，其行为构成背叛社会责任与宗教义务的双重罪恶。",
                    "evidence": [
                        "E20"
                    ]
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者归结：西方资本主义的罪恶不在流水线与黑心工厂，而在“不是没有选择、而且存在绝对义务不容这样选择的时候，却做了最贪婪的选择”这一步。",
                    "evidence": [
                        "E21"
                    ]
                },
                {
                    "claim_id": "C016",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者解释马克思的推论：因目睹贵族/宗教二元秩序崩塌而不再相信贵族精神或教会信仰，故主张一开始就消灭精英作出贪婪选择的可能性——消灭私有制/封建制本身。",
                    "evidence": [
                        "E22",
                        "E23"
                    ]
                },
                {
                    "claim_id": "C017",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提出法理基础：存在选择，才存在罪恶。",
                    "evidence": [
                        "E24"
                    ]
                },
                {
                    "claim_id": "C018",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者认为中国面对群狼环伺、长期处于强烈生存危机，这一宏观历史前提与当年羊吃人的贵族存在根本差异；虽不能说每家企业都是洁白羔羊，但中国企业主背负的原罪远比西方领主/资本家二位一体者小得多。",
                    "evidence": [
                        "E25",
                        "E26"
                    ]
                },
                {
                    "claim_id": "C019",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者判定：同样生产环境恶劣、待遇微薄，仅凭这两条，中国的小企业主们是无罪的——因为他们没有把人抛入绝境迫使其接受低待遇的能力和权柄。",
                    "evidence": [
                        "E27",
                        "E28"
                    ]
                }
            ],
            "argument_steps": [
                "点出争论语境：学生党指摘“偷换概念”“为资本家洗地”，作者改以两道反问题回应（P001、P002）。",
                "第一题：企业间供货是否等于剥削（P003）；若答“是”，要消灭剥削就须连商品经济一并消灭、改为完全中央调拨（P004、P005）。",
                "把该结论推给对方：是否认为中央调拨模式才绝对无罪并能带来普遍幸福与国际生存空间；若是，请把论文上交人大政协（P006、P007）。",
                "第二题：若一切雇佣关系都是剥削，那么在不改变业务流程与资金支付的改组（有限责任公司＋个人独资企业协作、报酬等于原工资）之后，剥削为何消失（P009、P010）。",
                "若改判为上下游企业间的剥削，则唯一解法是彻底毁灭一切经济活动本身（P011）。",
                "斥责对手缺乏经验、把此当智力游戏，不知其后果（P013、P014）。",
                "反驳“罪恶在工厂”：对工人而言进厂是失去一切后的救命稻草（P015、P016），并反问替代方案与救济来源（P017）。",
                "以“直接汇款一半工资”的设算反将对手（P018）；指出不能三种态度同时持有（P019）；要求打击血汗工厂者申请提高个人所得税税率（P020）。",
                "预判反驳并指出后果：向厂主征税要么导致通胀、要么工厂消失，而待吃饭者仍在（P021—P023）。",
                "重新界定马克思的指责对象：不是老板的邪恶，而是领主制造绝境后开厂的行为（P024、P025）。",
                "指出真正的罪恶：未吸纳全部失地农民，而新生产方式本可让全体领民过得更好（P026—P030）。",
                "以贵族牧养职责与誓言说明“双重罪恶”（P031、P032、P033），并以《唐顿庄园》作正面参照（P034）。",
                "归结命题：罪恶发生在有选择且有绝对义务却做最贪婪选择的这一步（P035）；并解释马克思由此走向消灭私有制/封建制（P036、P037）。",
                "回到本题：存在选择才有罪恶的法理基础（P039）；中国长期生存危机的历史前提与羊吃人的贵族根本不同（P040），故中国企业主原罪小得多（P041），仅凭环境恶劣与待遇微薄不构成罪恶（P042、P043）。"
            ],
            "concept_usage": [
                {
                    "term": "剥削",
                    "meaning": "本文中被检验的对方定义：是否包括企业之间的采购供应、一切雇佣关系；作者通过归谬说明该定义若成立将导致商品经济整体被否定。",
                    "evidence": "P003",
                    "ambiguity": "作者未给出自己的剥削定义，只检验对方定义的后果。"
                },
                {
                    "term": "资本罪恶 / 原罪",
                    "meaning": "作者区分流行用法与马克思用法：罪恶不在工厂，而在持有选择与义务者的贪婪选择；中国企业主的“原罪”因缺乏将人抛入绝境的能力而小得多。",
                    "evidence": "P035",
                    "ambiguity": "“原罪”为借喻，作者未给出可量化标准。"
                },
                {
                    "term": "存在选择",
                    "meaning": "作者提出的罪恶法理基础：有选择才有罪恶可言。",
                    "evidence": "P039",
                    "ambiguity": "无。"
                },
                {
                    "term": "商品经济",
                    "meaning": "作者用以指与中央调拨相对的经济形态：若要消灭企业间与雇佣关系中的“剥削”，就须连它一起消灭。",
                    "evidence": "P004",
                    "ambiguity": "作者未展开其制度含义。"
                },
                {
                    "term": "二位一体",
                    "meaning": "作者用于形容西方资本主义兴起时领主与资本家身份合一的群体。",
                    "evidence": "P041",
                    "ambiguity": "为作者自造表述。"
                }
            ],
            "examples_and_targets": [
                "513厂、936厂、酒泉基地——作者举的中央调拨式经济例子（P004）。",
                "个体户与个人独资企业——作者据中国实有经济实体设置的反问题材料（P009）。",
                "“一个月累死累活也不过是三千”“1500就可以在本地过日子”——作者的设算数字，非实测数据（P018）。",
                "马克思——被作者引述与重新解释的对象（P024、P025、P036、P037）。",
                "英国领主/佃农、纺织厂与失地农民、羊吃人——作者复述的历史叙述（P025、P040）。",
                "《唐顿庄园》——作者举的“合格贵族”参照（P034）。",
                "被反驳对象：“学生党”的“偷换概念”“为资本家洗地”指摘（P001）；“很多人认为资本的罪恶在工厂”的看法（P015）；“你们”要求打击血汗工厂又不捐献、又抱怨税收的立场（P019、P020）。"
            ],
            "conditions": [
                "第一题的推论以“如果你们回答‘是’”为条件（P004）。",
                "第二题以“如果你们认定一切雇佣关系都是剥削关系”为条件，并附“不改变任何业务具体流程和资金支付”“报酬严格的等于原来对应份额的工资”等限定（P009）。",
                "“如果你们要认定这意味着‘上游企业’剥削了‘下游企业’”（P011）——作者对对方可能的改判所设条件。",
                "“正因为他们本来可以，他们没有这么做才构成罪恶”（P030）——罪恶成立依赖“本来可以”的能力条件。",
                "“不能说中国的每一家企业都是洁白羔羊”为作者对自身结论的限定（P041）。",
                "“同样生产环境恶劣、待遇微薄，但是仅仅只是这两条，中国的小企业主们是无罪的”（P042）——以“仅仅只是这两条”限定适用范围。"
            ],
            "rhetoric_and_tone": "论战语气：开篇即指对手“胡喷”，全篇连续使用第二人称“你们”质问（“你们是不是认为……？”“你们根本不知道自己在说什么。”），以反问题与归谬推进，并以“请把你们的论文上交人大政协”“请申请提高个人所得税税率”等反讽式建议施压；也使用“救命稻草”“经济浩劫和灾难”等强烈措辞，末尾转为对历史伦理的分析，语气由斥责转为论证。",
            "unresolved_questions": [
                "提问者所问“《资本论》所描写的工人惨状是否属实”，正文未正面回答真伪，仅转向对剥削定义与资本罪恶的辨析。",
                "P018 的“三千”“1500”等数字为作者设算，无数据来源，需外部核查。",
                "P004 的“513厂”“936厂”具体所指，正文未说明，需外部核查。",
                "P031、P032 关于贵族对上帝承担牧养职责、神前誓言的历史叙述，属外部事实断言，需外部核查。",
                "“原罪”大小如何比较与衡量，正文未给标准。",
                "版本信息：updated_at（2025-09-16）远晚于 published_at（2019-12-30），差异内容未提供，需外部核查。",
                "本文无图片节点。lexical 段落节点 46 与正文段 43 的差异由生成器记录，经核对为结构节点计数差异，不影响阅读。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P003",
                    "quote": "如果一个企业跟另一个企业签供货合同，是否采购方在剥削供应方？",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P004",
                    "quote": "请连商品经济一起消灭",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P006",
                    "quote": "你们是不是认为这样的经济模式才是绝对无罪的模式",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P007",
                    "quote": "请把你们的论文上交人大政协",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P009",
                    "quote": "“剥削”如何就神奇的消失了？",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P011",
                    "quote": "唯一的解决方案",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P013",
                    "quote": "根本不知道放纵你们这种荒谬的蠢论背后是何等样的经济浩劫和灾难。",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P014",
                    "quote": "你们根本不知道自己在说什么。",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P015",
                    "quote": "很多人认为资本的罪恶在工厂",
                    "relation": "contradicts"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P016",
                    "quote": "已经是一无所有、失去一切之后好歹抓住的一根救命稻草了。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P018",
                    "quote": "请工人们回家，你们直接按ta们一半的工资每月汇款给ta们。",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P020",
                    "quote": "请申请提高个人所得税税率。",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P022",
                    "quote": "要么物价普涨一截",
                    "relation": "supports"
                },
                {
                    "key": "E14",
                    "paragraph_id": "P023",
                    "quote": "所以还是请提高个人所得税税率。",
                    "relation": "supports"
                },
                {
                    "key": "E15",
                    "paragraph_id": "P024",
                    "quote": "不是指开工厂的老板有多邪恶",
                    "relation": "supports"
                },
                {
                    "key": "E16",
                    "paragraph_id": "P025",
                    "quote": "先制造农民的绝境，然后另一手开起纺织厂，农民接受低工资打工。",
                    "relation": "supports"
                },
                {
                    "key": "E17",
                    "paragraph_id": "P027",
                    "quote": "他们所开的工厂没有吸纳全部被他们剥夺土地的失地农民。",
                    "relation": "supports"
                },
                {
                    "key": "E18",
                    "paragraph_id": "P028",
                    "quote": "他们本来可以给原本的全体领民提供比原来更好的生活。",
                    "relation": "supports"
                },
                {
                    "key": "E19",
                    "paragraph_id": "P030",
                    "quote": "正因为他们本来可以，他们没有这么做才构成罪恶。",
                    "relation": "supports"
                },
                {
                    "key": "E20",
                    "paragraph_id": "P031",
                    "quote": "背叛社会责任和宗教义务的双重罪恶",
                    "relation": "supports"
                },
                {
                    "key": "E21",
                    "paragraph_id": "P035",
                    "quote": "而是发生在“不是没有选择、而且存在绝对义务不容这样选择的时候，却做了最贪婪的选择”的这一步。",
                    "relation": "supports"
                },
                {
                    "key": "E22",
                    "paragraph_id": "P036",
                    "quote": "不再相信贵族精神或者教会信仰能解决人类命运问题",
                    "relation": "supports"
                },
                {
                    "key": "E23",
                    "paragraph_id": "P037",
                    "quote": "消灭私有制 / 封建制本身。",
                    "relation": "supports"
                },
                {
                    "key": "E24",
                    "paragraph_id": "P039",
                    "quote": "存在选择，才存在罪恶的法理基础。",
                    "relation": "supports"
                },
                {
                    "key": "E25",
                    "paragraph_id": "P040",
                    "quote": "长期处在强烈生存危机之中",
                    "relation": "supports"
                },
                {
                    "key": "E26",
                    "paragraph_id": "P041",
                    "quote": "中国的企业主远比西方资本主义兴起时的领主/资本家二位一体的那一帮背负的原罪小得多。",
                    "relation": "supports"
                },
                {
                    "key": "E27",
                    "paragraph_id": "P042",
                    "quote": "中国的小企业主们是无罪的。",
                    "relation": "supports"
                },
                {
                    "key": "E28",
                    "paragraph_id": "P043",
                    "quote": "ta们并没有“把人抛入绝境迫使ta们不得不接受低待遇”的能力和权柄。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "政治经济学",
                "马克思主义",
                "经济史",
                "伦理"
            ],
            "issue_candidates": [
                "剥削的定义",
                "雇佣关系与商品经济",
                "资本原始积累的罪恶",
                "中国企业主的原罪"
            ],
            "text_function_candidates": [
                "论辩",
                "批评",
                "答疑",
                "历史解释"
            ],
            "object_candidates": [
                "提问者",
                "学生党",
                "马克思",
                "英国领主",
                "佃农",
                "失地农民",
                "中国小企业主",
                "人大政协",
                "唐顿庄园"
            ],
            "working_keywords": [
                "剥削",
                "商品经济",
                "中央调拨",
                "个体户",
                "个人独资企业",
                "血汗工厂",
                "资本罪恶",
                "原罪",
                "存在选择",
                "羊吃人"
            ]
        },
        "notes": "无图片节点。正文以反问题与归谬为主，作者对提问者原问题的正面回答缺失，已登记。对手口径（学生党、“很多人”）分别以 opponent_view 处理，未归给作者。P004“513厂/936厂”、P031—P032 贵族誓言属待外部核查的历史/事实断言。"
    },
    "8d6bfa1a": {
        "analysis": {
            "question_context": "提问者的问题是：国产特斯拉 Model 3 官方降至 29.9 万，是「野心」还是「暴击」？作者把落点转到“与中国脱钩”论的破产上，随后分别处理“对国产电动车的冲击”“特斯拉的野心”“暴击”三问，并对特斯拉的目标作出自己的判断。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "首要判断：降价是对“与中国脱钩”论的暴击；并给出“美国知识产权和资本＋世界资源＋中国行政、制造业与市场”这一组合仍是最有效率的组合。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P003"
                    ],
                    "summary": "条件式推论：若马斯克“降低制造成本65%”属真实数字，则加征100%关税都不足以抹平中国制造的竞争力，该部分关税主要由美国人自己买单。",
                    "role": "reason"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P004",
                        "P005"
                    ],
                    "summary": "修正“制造业外流”的流行理解：外流主要是为洗产地，厂房建设速度与劳动素质表明短期难以真正转移；中国所受伤害主要是买不起的买家放弃生意、订单被关税消灭。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P006"
                    ],
                    "summary": "过渡：特斯拉上海工厂是一记清脆的耳光。",
                    "role": "transition"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P007",
                        "P008",
                        "P009"
                    ],
                    "summary": "对“冲击国产电动车”的回应：冲击向来不是坏事，并以市场开放初期对大众、依维柯冲击农机厂的担忧为例；结论是有一流的竞争者才有一流的本土企业。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P010"
                    ],
                    "summary": "对“野心”的界定：特斯拉的野心不是压倒中国现有电动车厂，而是压垮传统非长途载具厂商。",
                    "role": "claim"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P011"
                    ],
                    "summary": "对“暴击”的回应：国产厂商欠暴击，暴击是其成长的主要动力，并以战斗机引擎的比喻收束。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判断这次降价首先是对“与中国脱钩”论的暴击。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为美国的知识产权和资本、世界的资源与中国稳定高效的行政体系、制造业体系和市场这一组合，仍然是这个星球上最有效率的组合。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者条件式判断：如果马斯克所说的“降低制造成本65%”是真实数字而不仅仅是宣传，那意味着加征100%关税都不足以抹平中国制造的竞争力，那部分关税主要由美国人自己买单。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为“制造业外流”的本质不是从中国制造换成印度或越南制造，而主要是为了洗产地；从厂房建设速度看，那些屋顶下恐怕只有最后的包装流水线。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为中国制造业所受折腾更多是因为关税直接消灭了大量订单——美国人不是去向别人买了，而是干脆买不起了。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者把特斯拉上海工厂评为“一记清脆的耳光”。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者认为“对国产电动车的冲击”向来不是坏事，并举市场开放初期担心大众汽车、依维柯冲击农机厂为例。",
                    "evidence": [
                        "E7"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提出历史经验：以中国人的智力、勤奋与资源，很少有事是真的做不到或学不会，而是缺乏竞争者刺激时宁可抱残守缺、固步不前，不到生死存亡不尽全力。",
                    "evidence": [
                        "E8"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者以格言式短句给出结论：有一流的竞争者，才有一流的本土企业。",
                    "evidence": [
                        "E9"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者判断特斯拉的野心不是要压倒中国现有的电动车厂，而是要压垮传统非长途载具厂商。",
                    "evidence": [
                        "E10"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为国产厂商欠暴击，从历史上看暴击是它们成长的主要动力。",
                    "evidence": [
                        "E11"
                    ]
                }
            ],
            "argument_steps": [
                "开篇定性：降价首先是对“与中国脱钩”论的暴击（P001）。",
                "给出被验证的组合命题：美国知识产权与资本＋世界资源＋中国行政、制造业与市场仍是最有效率的组合（P002）。",
                "条件推论：若成本下降 65% 属实，则 100% 关税也不足以抹平竞争力，关税主要由美国人买单（P003）。",
                "修正“外流”叙事：外流主要是洗产地，短期难有真实产能与劳动素质转移（P004）；伤害来自订单被关税消灭而非买家转向他国（P005）。",
                "评价特斯拉上海工厂为一记耳光（P006）。",
                "回应“冲击”：冲击不是坏事，并举改革开放初期对大众、依维柯的担忧（P007）；给出历史经验判断（P008）；格言式结论——有一流的竞争者才有一流的本土企业（P009）。",
                "界定野心方向：压垮传统非长途载具厂商，而非压倒中国现有电动车厂（P010）。",
                "回应“暴击”：国产厂商欠暴击，暴击是成长主要动力（P011）。"
            ],
            "concept_usage": [
                {
                    "term": "与中国脱钩",
                    "meaning": "本文中被降价事件所反驳的论调。",
                    "evidence": "P001",
                    "ambiguity": "作者未点明该论的具体主张者。"
                },
                {
                    "term": "暴击",
                    "meaning": "标题中的二选一之一，作者用作正面评价：对国产厂商的强烈冲击是其成长的主要动力，与“冲击是坏事”的预设相反。",
                    "evidence": "P011",
                    "ambiguity": "标题中的“暴击”与 P001 中“对脱钩论的暴击”所指对象不同。"
                },
                {
                    "term": "洗产地",
                    "meaning": "作者对“制造业外流”实质的判断：换产地标签而非真实产能转移。",
                    "evidence": "P004",
                    "ambiguity": "作者未给出判断依据之外的数据。"
                },
                {
                    "term": "传统非长途载具厂商",
                    "meaning": "作者对特斯拉真正竞争对手的界定。",
                    "evidence": "P010",
                    "ambiguity": "该表述的确切所指（传统燃油车厂商？）正文未展开。"
                }
            ],
            "examples_and_targets": [
                "国产特斯拉 Model 3 降至 29.9 万——提问所述事件（Q001）。",
                "马斯克“降低制造成本65%”——作者引用的待验证数字（P003）。",
                "印度制造、越南制造——作者反驳“外流”叙事时提到的对象（P004）。",
                "大众汽车、依维柯与各县农机厂——作者举的历史类比（P007）。",
                "“八双铁头牛皮鞋”——作者对国产厂商受刺激而前进的比喻（P011）。",
                "被反驳对象：“与中国脱钩”论（P001）；“制造业外流”的流行理解（P004）；担心冲击国产电动车的声音（P007）。"
            ],
            "conditions": [
                "“如果马斯克所说的‘降低制造成本65%’是真实数字而不仅仅是宣传的话”（P003）——核心推论的前提条件。",
                "“就算对方天资聪颖，也得对方会阅读和识数才行”（P004）——对产能转移困难的补充条件。",
                "“没有竞争者刺激的时候”与“不到生死存亡”（P008）——作者对“做不到/学不会”这一判断所设的条件。",
                "“从那些厂房的建设速度来看”（P004）——判断外流实质的依据条件。"
            ],
            "rhetoric_and_tone": "短评式论辩语气，句式简短、断言密集；使用“暴击”“清脆的耳光”“八双铁头牛皮鞋”等夸张比喻；对“外流”叙事用“恐怕只有最后的包装流水线”“干脆买不起了”等口语化判断；末段以比喻收束，整体带鼓动与调侃色彩。",
            "unresolved_questions": [
                "“降低制造成本65%”与“加征100%关税”均为待外部核查的数据。",
                "P004 关于越南/印度厂房“只有最后的包装流水线”的判断依据，正文未提供数据。",
                "特斯拉“要压垮传统非长途载具厂商”这一判断的依据，正文未说明。",
                "提问中的「野心」与「暴击」两个选项，作者分别作了回应，但未做总体取舍。",
                "版本信息：updated_at（2025-09-29）晚于 published_at（2020-01-05），差异内容未提供，需外部核查。",
                "本文无图片节点。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "这首先是对“与中国脱钩”论的暴击。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "仍然是这个星球上最有效率的组合。",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "那意味着加征100%关税都不足以抹平中国制造的竞争力。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P004",
                    "quote": "而主要是为了洗产地。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P005",
                    "quote": "而是干脆买不起了。",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P006",
                    "quote": "特斯拉上海工厂其实是一记清脆的耳光。",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P007",
                    "quote": "这向来不是坏事。",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P008",
                    "quote": "而是没有竞争者刺激的时候出于对风险的厌恶宁可抱残守缺、固步不前。",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P009",
                    "quote": "有一流的竞争者，才有一流的本土企业。",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P010",
                    "quote": "而是“要压垮传统非长途载具厂商”。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P011",
                    "quote": "国产厂商欠暴击。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "产业经济",
                "中美经贸",
                "汽车产业"
            ],
            "issue_candidates": [
                "特斯拉国产化降价",
                "与中国脱钩论",
                "关税成本归属",
                "制造业外流与洗产地",
                "竞争与本土企业成长"
            ],
            "text_function_candidates": [
                "评论",
                "答疑",
                "论辩"
            ],
            "object_candidates": [
                "提问者",
                "特斯拉",
                "马斯克",
                "国产电动车厂商",
                "大众汽车",
                "依维柯",
                "美国",
                "中国",
                "印度",
                "越南"
            ],
            "working_keywords": [
                "暴击",
                "与中国脱钩",
                "洗产地",
                "制造业外流",
                "关税",
                "降本65%",
                "竞争",
                "一流竞争者",
                "非长途载具"
            ]
        },
        "notes": "无图片节点。P003 的 65% 降本与 100% 关税均为作者引用的待核查数字，已按条件式主张标注（author_qualified/hypothetical）。"
    },
    "840bd308": {
        "analysis": {
            "question_context": "提问者的问题是：34 岁华裔工程师在美国遭抢笔记本电脑、追击歹徒被拖行后身亡，为什么会发生此类事件？是个案吗？作者未就案件本身作答，而是给出对美国安全机制的一般解释：美国高度依赖自卫，责任沿契约链条分配，风险以保险与免责条款处理。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "两条前提：美国高度依赖自卫保证安全，不能沿用东亚的安全观；美国人对生命安全看得不重，不像中国有“人命大过天”的观念。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P003",
                        "P004"
                    ],
                    "summary": "机制说明：重视的是基于契约的责任与天价赔偿责任；沿契约链条追踪会发现经常处在没有任何人要为你的某种死亡负责的状态。",
                    "role": "reason"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P005",
                        "P006"
                    ],
                    "summary": "处理方式：自购保险加免责条款——先请你自担风险，再建议你买保险以防万一。",
                    "role": "other"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P007",
                        "P008"
                    ],
                    "summary": "若要服务方负责安全，服务必然是天价（等于把保险拆成一人份并翻倍打包）；且服务方仍受有限责任公司制度保护，可能根本未投保、打算出事即破产。",
                    "role": "reason"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P009",
                        "P010"
                    ],
                    "summary": "利弊总结：好处是风险有可预见保底（哪怕人命也有确切数字，甚至未必很高），故美国人做生意胆子大；坏处是美国本质上不安全，所需安全意识、技能与投入都很大。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判断美国是一个高度依赖自卫来保证安全的国家，不能沿用在东亚社会里养成的安全观。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为美国人对人的生命安全看得其实不重，并不像中国有一种“人命大过天”的观念。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为在美国人们重视的是基于契约而产生的责任，重视的不是人命本身，而是常常因此而来的天价赔偿责任。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者指出：沿契约链条追踪下去，会发现自己经常处在一种没有任何人要为你的某种死亡负责的状态。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者说明常见处理方式：以自购保险加免责条款处理——先用免责条款请你自担风险，然后建议你购买保险以防万一。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者认为若要服务方为安全负责，这项服务一定是天价——实质上等于把其要买的保险拆成你的一人份并翻几倍强制打包在服务费里。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者指出即使如此，服务方仍受有限责任公司制度保护：说不定提供服务的企业根本没买保险，就是打算一旦出事即破产了事。",
                    "evidence": [
                        "E7"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者判断这一制度的好处是美国人做生意胆子很大：各种风险都有可预见的保底，哪怕闹出人命也有确切数字，甚至这个数字未必很高。",
                    "evidence": [
                        "E8"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判断其坏处是美国在本质上就不安全，需要的安全意识、安全技能、安全投入都很大。",
                    "evidence": [
                        "E9"
                    ]
                }
            ],
            "argument_steps": [
                "给出前提：美国靠自卫保证安全，东亚安全观不适用（P001）；美国人不似中国有“人命大过天”的观念（P002）。",
                "解释机制：责任基于契约与赔偿责任，而非人命本身（P003）。",
                "推论：沿契约链条追踪，常处于无人为你某种死亡负责的状态（P004）。",
                "说明处理方式：免责条款＋自购保险（P005、P006）。",
                "给出代价：要服务方负责则服务天价，等于把保险拆成一人份翻倍打包（P007）。",
                "补充：服务方受有限责任保护，可能根本不投保、出事即破产（P008）。",
                "总结利弊：好处是风险有保底、生意胆大（P009）；坏处是本质不安全、安全投入大（P010）。"
            ],
            "concept_usage": [
                {
                    "term": "自卫",
                    "meaning": "作者指美国安全供给的主要方式：个人自行承担与行使安全防护。",
                    "evidence": "P001",
                    "ambiguity": "作者未说明其与持枪权、警务的关系。"
                },
                {
                    "term": "人命大过天",
                    "meaning": "作者用以描述中国观念中生命安全的最高优先级，并与美国作对照。",
                    "evidence": "P002",
                    "ambiguity": "为口语化概括，作者未给出制度层面的对照依据。"
                },
                {
                    "term": "基于契约而产生的责任",
                    "meaning": "作者认为美国所重视的责任类型：由契约链条界定，因而可以出现无人负责的状态。",
                    "evidence": "P003",
                    "ambiguity": "无。"
                },
                {
                    "term": "免责条款",
                    "meaning": "作者指其与自购保险配套使用的风险分配手段。",
                    "evidence": "P005",
                    "ambiguity": "无。"
                }
            ],
            "examples_and_targets": [
                "34 岁华裔工程师遭抢笔记本电脑、追击歹徒被拖行身亡——提问所述事件（Q001），正文未提及该案细节。",
                "天价赔偿责任、有限责任公司制度、企业出事即破产——作者对美国机制的举例性描述（P003、P007、P008）。",
                "“就算闹出人命也有一个确切的数字”——作者对风险可计价特征的描述（P009）。",
                "被反驳/被纠正对象：沿用东亚安全观在美国行事的预设（P001）。"
            ],
            "conditions": [
                "“如果要服务方为你的安全负责，那么这项服务一定是天价”（P007）——条件式推论。",
                "“而即便如此，服务方仍然是受到有限责任公司制度保护的”（P008）——附加限定。",
                "“说不定向你提供服务的企业根本就没有购买保险”（P008）——以“说不定”标记可能性，非断言。",
                "“这类问题，ta们往往用……”（P005）——以“往往”限定适用频率。"
            ],
            "rhetoric_and_tone": "解释性短评，语气冷静、以论断句排列：多用“其实”“往往”“说不定”等限定词；以“就这样了。”一句独立成段作冷淡收束，带讽刺意味；“天价”“甚至这个数字未必很高”形成反差，暗含批评但不作道德评判。",
            "unresolved_questions": [
                "提问所问的该案是否属个案，正文未回答。",
                "“美国人对人的生命安全看得其实不重”“人命大过天”属对照性概括，其依据与适用范围正文未说明，需外部核查。",
                "关于美国保险、免责条款、有限责任公司制度的具体法律效果，正文未给出条文或案例依据，需外部核查。",
                "正文未提供任何统计数据，故“为什么会发生此类事件”未获实证回答。",
                "版本信息：updated_at（2026-04-20）晚于 published_at（2020-01-06），差异内容未提供。",
                "本文无图片节点。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "美国是一个高度依赖自卫来保证安全的国家，不能沿用在东亚社会里养成的安全观。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "美国人对人的生命安全看得其实不重",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "而是重视常常因此而来的天价赔偿责任。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P004",
                    "quote": "会发现你经常处在一种没有任何人要为你的某种死亡负责的状态。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P005",
                    "quote": "先用免责条款请你自担风险，然后建议你购买保险以防万一。",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P007",
                    "quote": "那么这项服务一定是天价",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P008",
                    "quote": "说不定向你提供服务的企业根本就没有购买保险，就是打算一旦出事就破产了事罢了。",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P009",
                    "quote": "哪怕闹出人命也有一个确切的数字",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P010",
                    "quote": "坏处是美国在本质上就不安全，需要的安全意识、安全技能、安全投入都很大。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "社会制度比较",
                "法律与责任",
                "公共安全"
            ],
            "issue_candidates": [
                "美国安全供给方式",
                "契约责任与赔偿责任",
                "免责条款与保险",
                "有限责任与破产免责"
            ],
            "text_function_candidates": [
                "答疑",
                "解释",
                "评论"
            ],
            "object_candidates": [
                "提问者",
                "受害者（34 岁华裔工程师）",
                "美国",
                "中国",
                "服务方企业",
                "保险公司"
            ],
            "working_keywords": [
                "自卫",
                "人命大过天",
                "契约责任",
                "天价赔偿责任",
                "免责条款",
                "自购保险",
                "有限责任公司",
                "破产"
            ]
        },
        "notes": "无图片节点。正文未涉及提问所述案件的具体情节与“是否个案”，已登记为未决问题；对美国的概括均属作者一般化论断，需外部核查。"
    },
    "8d759a27": {
        "analysis": {
            "question_context": "提问者的问题是：IBM 工程师被抢身亡，为什么在美国湾区抢劫如此普遍？遇上了要怎么做才能最小化损失？作者以人口密度与持枪传统的对比解释治安差异，并提出古代中国已有的应对方案（引《孟子·尽心》语），最后把富人区的治理结构与其所述模式作类比。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002",
                        "P003"
                    ],
                    "summary": "提出历史类比：中国人口密度低时也是同样状态（两千多年前），且当时已有方案，并引“君子不立于危墙之下”一段。",
                    "role": "context"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P004"
                    ],
                    "summary": "解释中国路径：人口密度高导致高密度共居伦理，包含对暴力倾向的警惕与压制，故人身安全较有保障；负面效应是尚武精神与冒险精神受抑制。",
                    "role": "claim"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P005"
                    ],
                    "summary": "解释美国路径：拓荒状态人人带枪，持枪传统使人口密度无法提高到中国水平；高密度聚居会出现帮派与地盘划分、“集体自卫”与“部落复仇”机制，而这些安全服务需额外收益维持，故出现保护费与违禁品销售。",
                    "role": "reason"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P006"
                    ],
                    "summary": "类比推论：富人区实际也在遵循同一模式——警察是正规化的“帮派”，房产税是保护费，垄断商品销售对应其掌握的立法与国家主权、先进科技。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为中国人口密度低的时候也是同样状态，只是那是在两千多年前。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "quoted_or_cited",
                    "attribution": "cited_source",
                    "modality": "asserted",
                    "statement": "作者引《孟子·尽心》句“防祸于先而不致于后伤情。知而慎行，君子不立于危墙之下，焉可等闲视之”，作为当时已有的应对方案。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为中国因人口密度高而形成高密度共居的伦理，其中包含对暴力倾向的警惕和压制，使中国人的人身安全不容易受到威胁。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者同时指出负面效应：中国人的尚武精神和冒险精神也受到了普遍抑制。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者认为美国始于人人带枪的拓荒状态，普遍持枪的文化传统保证了美国人口密度无法提高到中国这个水平。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者推演：持枪者住大筒子楼一定会出现帮派和地盘划分，出现“集体自卫”和“部落复仇”机制提供部分安全服务；而这类服务不依靠额外收益无法维持，于是出现保护费与违禁品销售问题。",
                    "evidence": [
                        "E6",
                        "E7"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为富人区实际上也在遵循同一模式：其“帮派”是正规化了的警察，其保护费是房产税，其垄断商品销售以立法、国家主权与先进科技实现，而非借助犯罪。",
                    "evidence": [
                        "E8"
                    ]
                }
            ],
            "argument_steps": [
                "以历史类比起头：中国人口密度低时也如此，只是那是两千多年前（P001、P002）。",
                "引出古代方案：《孟子·尽心》的“君子不立于危墙之下”（P003）。",
                "给出中国路径的因果链：高人口密度→高密度共居伦理→对暴力的警惕与压制→人身安全较有保障（P004）；并指出其负面效应（P004）。",
                "给出美国路径的因果链：拓荒人人带枪→人口密度无法提高→高密度聚居出现帮派地盘与集体自卫、部落复仇→安全服务需额外收益维持→保护费与违禁品销售（P005）。",
                "作类比推论：富人区同构，只是以警察、房产税、立法与科技实现垄断（P006）。"
            ],
            "concept_usage": [
                {
                    "term": "高密度共居的伦理",
                    "meaning": "作者用以指中国因人口密度高而形成的、包含对暴力倾向警惕与压制的伦理。",
                    "evidence": "P004",
                    "ambiguity": "作者未给出该伦理的具体内容与形成机制。"
                },
                {
                    "term": "集体自卫 / 部落复仇",
                    "meaning": "作者设想的高密度持枪聚居下自发形成安全服务的机制。",
                    "evidence": "P005",
                    "ambiguity": "属推演性描述，作者未举实例。"
                },
                {
                    "term": "保护费",
                    "meaning": "作者用以指维持安全服务所需的额外收益，并将其与富人区房产税作同构类比。",
                    "evidence": "P005",
                    "ambiguity": "该类比为作者自设，未作限定。"
                },
                {
                    "term": "行政垄断",
                    "meaning": "作者对违禁品性质的定义（加引号使用）。",
                    "evidence": "P005",
                    "ambiguity": "未展开。"
                }
            ],
            "examples_and_targets": [
                "《孟子·尽心》引文——作者引用的古籍材料（P003）；引用出处由作者标出，具体文本与出处需外部核查。",
                "两千多年前的中国——作者的历史类比（P001）。",
                "美国拓荒者人人带枪、大筒子楼、帮派与地盘划分（P005）——作者推演材料。",
                "富人区、警察、房产税（P006）——作者类比材料。",
                "提问所述的 IBM 工程师被抢身亡与湾区抢劫——提问背景，正文未涉及具体案件。"
            ],
            "conditions": [
                "“持枪者住大筒子楼一定会出现帮派和地盘划分”（P005）——以持枪者与高密度居住同时成立为条件。",
                "“而这种安全服务不依靠某种额外的收益是没办法维持的”（P005）——维持条件。",
                "“其实曾经中国人口密度低的时候也是这个状态”（P001）——类比以“当时人口密度低”为条件。",
                "“这种伦理里包含了强大的对暴力倾向的警惕和压制，所以导致了……”（P004）——以该伦理成立为因果前提。"
            ],
            "rhetoric_and_tone": "以古喻今的评论语气：先用“其实曾经……只是那是在两千多年前”作历史化处理，再引典籍句；对美国的描述使用“人人带枪的拓荒状态”“部落复仇”等带调侃与推演色彩的措辞；末段用“微妙的是”引出对富人区的同构类比，带讽刺意味但以陈述句写出。",
            "unresolved_questions": [
                "提问的第二问（遇上抢劫要怎么做才能最小化损失）正文未直接回答，只给出“君子不立于危墙之下”的引文。",
                "所引《孟子·尽心》文字的确切出处与原文，需外部核查（作者标注为《孟子·尽心》）。",
                "“富人区也在销售垄断商品”的具体所指，正文未说明。",
                "关于美国持枪传统与人口密度的因果关系属作者推演，正文未提供证据。",
                "版本信息：updated_at（2025-12-10）晚于 published_at（2020-01-06），差异内容未提供。",
                "本文无图片节点；P003 为 quote 字段段落，lexical 段落节点 5 与正文段 6 的差异由生成器记录，不影响阅读。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "其实曾经中国人口密度低的时候也是这个状态，只是那是在两千多年前。",
                    "relation": "context"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P003",
                    "quote": "防祸于先而不致于后伤情。知而慎行，君子不立于危墙之下，焉可等闲视之。《孟子·尽心》",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P004",
                    "quote": "中国是因为人口密度高，导致了高密度共居的伦理。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P004",
                    "quote": "负面效应是中国人的尚武精神和冒险精神也受到了普遍抑制。",
                    "relation": "qualifies"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P005",
                    "quote": "普遍持枪的文化传统已经保证了美国人口密度无法提高到中国这个水平",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P005",
                    "quote": "出现“集体自卫”和“部落复仇”机制来提供一定的安全服务",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P005",
                    "quote": "于是就有保护费、违禁品",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P006",
                    "quote": "ta们有正规化了的“帮派”——警察；富人区也在收保护费——房产税",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "社会治安",
                "社会形态比较",
                "人口与居住形态"
            ],
            "issue_candidates": [
                "湾区抢劫与治安",
                "人口密度与暴力抑制",
                "持枪传统与聚居形态",
                "富人区治理的同构性"
            ],
            "text_function_candidates": [
                "答疑",
                "解释",
                "评论",
                "以古喻今"
            ],
            "object_candidates": [
                "提问者",
                "IBM 工程师",
                "美国湾区",
                "孟子",
                "富人区",
                "警察",
                "帮派"
            ],
            "working_keywords": [
                "低密度安全模式",
                "高密度共居的伦理",
                "君子不立于危墙之下",
                "人人带枪的拓荒状态",
                "集体自卫",
                "部落复仇",
                "保护费",
                "房产税"
            ]
        },
        "notes": "无图片节点。P003 为 quote 段落：引文出自作者标注的《孟子·尽心》，原文与出处待外部核查，故按 quoted_or_cited / cited_source 处理，未写作作者主张。"
    },
    "4891cb93": {
        "analysis": {
            "question_context": "提问者的问题是：无意中在百度接触到「唯我论」「缸中之脑」等，现在快崩溃了，我该怎么走出来？作者以“至少存在一个确定无疑的事实”为起点，做出一串存在论推论，最后把“存在域”的大小与个人的理解力范围联系起来。提问者的心理困境未被直接回应，作者给出的是论证路径。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001"
                    ],
                    "summary": "起点事实：对能想到这个问题的实体，至少存在一个确定无疑的事实——我在思考；即使你是缸中之脑、其他一切都是幻觉，这一点仍是事实。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P002"
                    ],
                    "summary": "推论一：基于该事实，作为思考的主体，“我”必然存在。",
                    "role": "reason"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P003",
                        "P004"
                    ],
                    "summary": "推论二、三：“我思考”与“我存在”存在绝对关联关系，前者可绝对证明后者；这意味着作为“绝对关联”，逻辑亦存在。",
                    "role": "reason"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P005",
                        "P006",
                        "P007",
                        "P008"
                    ],
                    "summary": "推论四及其扩展：与上述存在物存在绝对关联的一切其它事物也必都存在；例如使我能理解这些命题的思考能力、使该能力运转的物质基础与客观规律，以及使它们存在的事物；作者称该链条为“存在性挖掘机”，能开多远是另一个问题，但至少比个人理解力与判断力的覆盖范围远。",
                    "role": "reason"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P009",
                        "P010"
                    ],
                    "summary": "结论与劝勉：人的“存在域”不是装你脑的那个缸的直径，而是心眼所及的一切；若不够大，就开动挖掘机。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为对能想到这个问题的实体，世界上至少存在一个确定无疑的事实，就是“我在思考”；即使你是缸中之脑、其他一切都是幻觉，这一点也是事实。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者推论：作为思考的主体，“我”必然存在。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为“我思考”和“我存在”之间存在绝对的关联关系，以至于前者可以绝对地证明后者。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者由此推出：作为“绝对关联”，逻辑亦存在。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者推出：与上述存在物存在着“绝对关联”的一切其它事物，也必都存在。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者举例：令得“我”能理解上述全部命题的思考能力必然存在，令得这种思考能力得以运转的物质基础和客观规律也必然存在。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者承认“存在性挖掘机”能开多远是另一个问题，但认为它总比自己的理解力和判断力的覆盖范围远。",
                    "evidence": [
                        "E7"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者给出存在域的界定：人的“存在域”并非装你脑的那个缸的直径，而是你的心眼所及的一切。",
                    "evidence": [
                        "E8"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者劝勉：要是不够大，开动你的挖掘机。",
                    "evidence": [
                        "E9"
                    ]
                }
            ],
            "argument_steps": [
                "确立起点：对能想到此问题的实体，“我在思考”是确定无疑的事实，即使缸中之脑假设成立（P001）。",
                "由思考推出思考主体的存在（P002）。",
                "把二者的关系称为绝对关联，据此认为前者可绝对证明后者（P003）。",
                "由“绝对关联”推出逻辑亦存在（P004）。",
                "把该关联关系扩展到一切相关事物：与之有绝对关联者必都存在（P005）。",
                "举例展开：使我理解命题的思考能力、支撑它的物质基础与客观规律、乃至使它们存在的事物（P006、P007）。",
                "对该推链设限：能开多远是另一个问题，但至少远于自身理解力与判断力的覆盖范围（P008）。",
                "结论：存在域由心眼所及的范围决定，不足则继续“挖掘”（P009、P010）。"
            ],
            "concept_usage": [
                {
                    "term": "缸中之脑",
                    "meaning": "提问者提到的怀疑论假设，作者在 P001 中作为最极端的反例使用：即使它成立，“我在思考”仍是事实。",
                    "evidence": "P001",
                    "ambiguity": "作者未讨论该假设的其他含义。"
                },
                {
                    "term": "确定无疑的事实",
                    "meaning": "作者论证的起点：我在思考。",
                    "evidence": "P001",
                    "ambiguity": "无。"
                },
                {
                    "term": "绝对关联",
                    "meaning": "作者用以指“我思考”与“我存在”之间及其扩展链条上的必然关系，并称逻辑因此存在。",
                    "evidence": "P003",
                    "ambiguity": "作者未定义“绝对关联”的判定标准，属自设术语。"
                },
                {
                    "term": "存在性挖掘机",
                    "meaning": "作者对“使得必然存在的东西得以存在的东西也必然存在”这一推链的形象说法。",
                    "evidence": "P008",
                    "ambiguity": "作者自承其能开多远是另一个问题。"
                },
                {
                    "term": "存在域",
                    "meaning": "作者定义为“你的心眼所及的一切”，而非缸的直径。",
                    "evidence": "P009",
                    "ambiguity": "作者未给出度量方式。"
                }
            ],
            "examples_and_targets": [
                "缸中之脑——提问者提到的怀疑论设定，被作者用作极端反例（P001）。",
                "唯我论——提问者提到，正文未直接讨论。",
                "“存在性挖掘机”——作者自造的比喻（P008）。",
                "理解力与判断力的覆盖范围——作者用以对比推链延伸程度（P008）。"
            ],
            "conditions": [
                "“即使你是缸中之脑，其他一切都是幻觉，这一点也是事实”（P001）——以最极端怀疑论假设为条件仍成立。",
                "“与上述存在物存在着‘绝对关联’的一切其它事物，也必都存在”（P005）——结论依赖“绝对关联”这一关系成立。",
                "“至于……能开多远，这是另一个问题了”（P008）——作者对推论范围的明确限定。",
                "“要是不够大，开动你的挖掘机”（P010）——条件式劝勉。"
            ],
            "rhetoric_and_tone": "以短句递推构成的形式化论证语气：反复使用“必然存在”“这意味着”形成链条感；以“存在性挖掘机”“装你脑的那个缸”作形象化比喻，末两句转为第二人称劝勉（“要是不够大，开动你的挖掘机。”），从思辨转向鼓励，未对提问者的情绪困扰作直接安抚。",
            "unresolved_questions": [
                "提问者的实际困扰（“快崩溃了，我该怎么走出来”）未被直接回应，作者只给出论证路径。",
                "“绝对关联”作为术语的定义与成立依据，正文未说明。",
                "由“我思考”推出“物质基础和客观规律必然存在”的论证细节，正文未展开；该推论是否有效需外部哲学核查。",
                "“使得该物质基础和客观规律存在的事物也必然存在”之后的链条无终点，作者自称是另一个问题。",
                "标题“唯二绝对事实”与正文提到的绝对事实数量的对应关系，正文未说明。",
                "版本信息：updated_at（2026-07-05）晚于 published_at（2020-01-07），差异内容未提供。",
                "本文无图片节点。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "世界上至少存在一个确定无疑的事实，就是“我在思考”。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "即作为思考的主体，“我”必然存在。",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "以至于前者可以绝对的证明后者。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P004",
                    "quote": "这意味着作为“绝对关联”，逻辑亦存在。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P005",
                    "quote": "也必都存在。",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P006",
                    "quote": "令得这种思考能力得以运转的物质基础和客观规律也必然存在。",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P008",
                    "quote": "它总比你自己的理解力和判断力的覆盖范围远。",
                    "relation": "qualifies"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P009",
                    "quote": "人的“存在域”，并非装你脑的那个缸的直径，而是你的心眼所及的一切。",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P010",
                    "quote": "要是不够大，开动你的挖掘机。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "哲学（认识论、本体论）",
                "逻辑"
            ],
            "issue_candidates": [
                "缸中之脑与怀疑论",
                "我思故我在式推理",
                "绝对关联与逻辑的存在",
                "存在域"
            ],
            "text_function_candidates": [
                "答疑",
                "论证",
                "劝勉"
            ],
            "object_candidates": [
                "提问者",
                "缸中之脑",
                "唯我论",
                "我"
            ],
            "working_keywords": [
                "唯二绝对事实",
                "我在思考",
                "我存在",
                "绝对关联",
                "逻辑亦存在",
                "存在性挖掘机",
                "存在域",
                "心眼"
            ]
        },
        "notes": "无图片节点。作者使用的“绝对关联”“存在域”“存在性挖掘机”均为本文自设表述，已按本文用法记录，未外部对照哲学术语。提问所涉“唯我论”正文未展开。"
    },
    "f8a15d4a": {
        "analysis": {
            "question_context": "提问者的问题是：为什么很多家长宁愿信外人，也不信自己的孩子？作者把原因拆为两层：家长不敢信的是“那个相信孩子的自己”，以及孩子是不必负最后责任、需由家长兜底的人；并主张只有在子女已自力更生、自负其责时，才谈得上“父母不信任我”有没有错。末段以反问与反讽收束。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "第一层解释：大部分时候家长不敢信的不是孩子，而是那个相信孩子的自己；他们怕那个自己以“信任”为偷懒的借口而害了孩子。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P003"
                    ],
                    "summary": "第二层解释：剩下的大部分时候，他们不敢信的是一个不必对自己的任何决策负最后责任的人——因为追根到底还是要由父母兜底。",
                    "role": "claim"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P004",
                        "P005",
                        "P006"
                    ],
                    "summary": "由“父母从未觉得自己可以不必负责到底”这一（作者称为“错误的认知”）推出两点立场：家长有不信任的权力；享受兜底者须以足够努力赢得信任，直接要求信任在本质上站不住脚。",
                    "role": "reason"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P007",
                        "P008"
                    ],
                    "summary": "对比外人与子女：外人乱来要承担全部责任，而子女不承担责任——故家长更敢信外人。",
                    "role": "reason"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P009",
                        "P010",
                        "P011"
                    ],
                    "summary": "补充理由：每个人都留有无数违约记录而不自知；陌生人一无所知，还能给 benefit of doubt，父母却有几十年时间知道并记得，故以该记录换任何陌生人都没有面见说话的资格；孩子未意识到欠下的信用坑需先填平。",
                    "role": "rebuttal"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P012",
                        "P013",
                        "P014"
                    ],
                    "summary": "划出讨论条件：只有去掉上述两条（兜底与信用记录），在子女已自力更生、自负其责时，才能谈“父母不信任我”有没有错；作者以反问与反讽句作答。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为大部分时候家长不敢信的不是孩子，而是那个相信孩子的自己；他们怕那个自己以“信任”为偷懒并害了孩子。",
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
                    "statement": "作者认为剩下的大部分时候，家长不敢信的是一个不必对自己的决策负最后责任的人——因为追根到底还是要由他们兜底。",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_reported",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出：中国的父母从未觉得自己可以不必负责到底；作者称此为“错误的认知”，并由它导出家长所持的两点立场。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_reported",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者转述的家长立场之一：自己有不信任的权力。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_reported",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者转述的家长立场之二：享受兜底者必须付出足够的努力去赢得信任，而不是直接要求信任；作为被兜底者，直接要求信任在本质上站不住脚。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者解释为何家长宁信外人：外人乱来要承担全部责任，即使法律惩罚不到，父母也不会善罢甘休；而子女不承担责任。",
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
                    "statement": "作者认为任何一个人其实都有无数违约的记录，只是自己意识不到；陌生人一无所知还能给 benefit of doubt，父母却有几十年时间去知道并记得，以其记录换任何陌生人都没有面见说话的资格。",
                    "evidence": [
                        "E9"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出孩子似乎没意识到自己欠了多大的信用坑，需要先填平才有资格要求信任。",
                    "evidence": [
                        "E10"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者划出讨论条件：把兜底与信用记录这两条都去掉，在对待已经自力更生、自负其责的成年子女时，才能谈到“父母不信任我”到底有没有错。",
                    "evidence": [
                        "E11"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者以反问与反讽作答：面对成年子女，父母还是相信陌生人胜过亲生骨肉，当然有错——作者以“他们没能及时改正老习惯，简直该死，对吧？”的句式表达。",
                    "evidence": [
                        "E12"
                    ]
                }
            ],
            "argument_steps": [
                "第一层归因：家长不敢信的是那个相信孩子的自己，怕被自己用作偷懒借口（P001、P002）。",
                "第二层归因：不敢信一个不必承担最后责任、需由自己兜底的人（P003）。",
                "指出其认知前提（作者称为“错误的认知”）：中国父母从未觉得自己可以不必负责到底（P004），由此持有两点立场（P005、P006）。",
                "对比责任承担：外人乱来要负全责，子女不承担责任（P007、P008）。",
                "以信用记录加强论证：人人都有违约记录而不自知，父母记得，故陌生人反而更可能给予 benefit of doubt（P009）；孩子未意识到需先填平信用坑（P010）；父母或许不忍心明说（P011）。",
                "划定讨论条件：两条都去掉后才谈成年子女情形下“父母不信任我”有没有错（P012）。",
                "以反问与反讽回答：当然有错——用“简直该死，对吧？”的反讽句式收尾（P013、P014）。"
            ],
            "concept_usage": [
                {
                    "term": "兜底",
                    "meaning": "作者指父母对子女决策承担最后责任；子女因不必负此责任而在家长看来缺少被信任的资格。",
                    "evidence": "P003",
                    "ambiguity": "作者未说明兜底的具体范围（经济、法律或情感）。"
                },
                {
                    "term": "错误的认知",
                    "meaning": "作者对“中国父母从未觉得自己可以不必负责到底”这一观念的定性（加引号）。",
                    "evidence": "P004",
                    "ambiguity": "作者未说明其为何错误。"
                },
                {
                    "term": "信用坑",
                    "meaning": "作者比喻：子女在父母面前累积的违约记录所形成的信任缺口。",
                    "evidence": "P010",
                    "ambiguity": "属形象化说法，无衡量标准。"
                },
                {
                    "term": "benefit of doubt",
                    "meaning": "作者指陌生人因一无所知而更可能先给予的信任余地。",
                    "evidence": "P009",
                    "ambiguity": "原文直接使用英文，未加解释。"
                }
            ],
            "examples_and_targets": [
                "“外人乱来要承担全部责任，就算法律惩罚不到，你父母也不是吃素的”——作者对外人与子女责任差异的说明（P007）。",
                "“任何一个人其实都有无数违约的记录”——作者的一般化断言（P009）。",
                "成年子女、自力更生自负其责——作者设定的讨论条件（P012、P013）。",
                "被反驳/被回应对象：提问者所转述的“父母宁信外人不信自己孩子”的抱怨及其隐含的“父母不对”预设（Q001、P013）。"
            ],
            "conditions": [
                "“大部分时候”“剩下的大部分时候”限定两层归因的适用频率（P001、P003）。",
                "“孩子无论成年未成年”指明所描述父母心态的适用阶段（P004）。",
                "“把这两条都去掉，在对待已经自力更生、自负其责的成年子女时”（P012）——作者为本问题设定的成立条件。",
                "“就算法律惩罚不到”（P007）——责任差异论述的补充条件。"
            ],
            "rhetoric_and_tone": "简短解释文，语气克制但带讥诮：用“他们不敢信的，不是孩子，是那个相信孩子的自己”作警句式开篇；以第二人称“你”直接对子女说话（“你不用承担责任。”“而你似乎一点也没意识到……”）；末段以反问加反讽（“简直该死，对吧？”）收束，表面认同、实为挖苦。",
            "unresolved_questions": [
                "P009“任何一个人其实都有无数违约的记录”属一般化断言，无证据，需外部核查。",
                "“错误的认知”具体错在何处，正文未说明。",
                "作者对“父母到底该不该信成年子女”的判断以反讽句式给出（P014），其字面立场与真实立场存在歧义，需谨慎解释。",
                "提问者所问的“为什么”得到两层归因，但作者未给出改变这种局面的办法。",
                "版本信息：updated_at（2021-05-25）晚于 published_at（2020-01-07），差异内容未提供。",
                "本文无图片节点。lexical 段落节点 17 与正文段 14 的差异由生成器记录，不影响阅读。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "他们不敢信的，不是孩子，是那个相信孩子的自己。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "他们怕那个自己说“信任”是为了偷懒",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "他们不敢信的是一个不必对自己的任何决策负最后责任的人",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P004",
                    "quote": "中国的父母都从未觉得自己可以不必负责到底。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P005",
                    "quote": "1）自己有不信任的权力",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P006",
                    "quote": "享受兜底者，必须付出足够的努力去赢得信任，而不是直接要求信任。",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P007",
                    "quote": "因为外人乱来要承担全部责任",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P008",
                    "quote": "你不用承担责任。",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P009",
                    "quote": "你父母却有几十年时间去知道，而且他们都记得。",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P010",
                    "quote": "需要先填平才有资格腆着脸要求信任。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P012",
                    "quote": "在对待已经自力更生、自负其责的成年子女时，才能谈到“父母不信任我”到底有没有错。",
                    "relation": "qualifies"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P014",
                    "quote": "他们没能及时改正老习惯",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "家庭关系",
                "亲子信任",
                "责任伦理"
            ],
            "issue_candidates": [
                "父母为何宁信外人",
                "兜底与被信任资格",
                "信用记录与信任",
                "成年子女的信任问题"
            ],
            "text_function_candidates": [
                "答疑",
                "解释",
                "评论",
                "劝诫"
            ],
            "object_candidates": [
                "提问者",
                "父母",
                "子女",
                "外人",
                "成年子女"
            ],
            "working_keywords": [
                "宁信外人",
                "兜底",
                "不信任的权力",
                "赢得信任",
                "信用坑",
                "benefit of doubt",
                "自力更生",
                "自负其责"
            ]
        },
        "notes": "无图片节点。P014 为反讽句，字面“简直该死”不宜作作者的真实主张读，已按 modality=questioned 记录并在 unresolved_questions 标注歧义。"
    },
    "d44c8e93": {
        "analysis": {
            "question_context": "提问者的问题是：孩子很平庸，非常失望，该如何调整积极面对？作者不提供调整技巧，而是先指出“每一个人都是平庸的人”，再分析“平庸＝失败/罪”这一认知如何由竞争式生存观、近代集体创伤与代际传递形成，最后给出替代方案（净输出与原谅）及其对子女教育的含义。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001"
                    ],
                    "summary": "开门立论：每一个人都是平庸的人，即使是那些被神化的人也一样。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P002",
                        "P003"
                    ],
                    "summary": "解释焦虑来源：大部分人都把生存看作竞争，仿佛资源有限、必须胜过别人才不算失败；并转述“弱就是原罪”的说法。",
                    "role": "reason"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P004",
                        "P005",
                        "P006",
                        "P007",
                        "P008",
                        "P009"
                    ],
                    "summary": "第一重痛感（同情）：持有这种世界认知者的生活体验惨烈，随时担忧被淘汰；作者以“无间地狱”“人终有一死反而成了一种安慰”形容。",
                    "role": "other"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P010",
                        "P011",
                        "P012"
                    ],
                    "summary": "第二重痛感：这种认知并非毫无道理，是被人痛苦的对待与“现实”教育出来的；“现实”对此并非没有责任，世界确实存在贪婪、残忍、无耻与卑鄙。",
                    "role": "qualification"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P013",
                        "P014"
                    ],
                    "summary": "历史解释：这个民族在近代史上经受过空前的集体伤害，伤痕深嵌于民族性；由此产生焦虑，焦虑驱使怀疑，而怀疑几乎总是发育成“果然我没看错”的新事实。",
                    "role": "reason"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P015",
                        "P016",
                        "P017",
                        "P018"
                    ],
                    "summary": "以三段引号独白呈现代际传递的信念：把世界是地狱的恐惧传给子女；只能凭优秀去争取被剥削的机会；唯一机会是爬上去成为强者；故得出“平庸是罪”。",
                    "role": "example"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P019",
                        "P020",
                        "P021"
                    ],
                    "summary": "第三重痛感（无力与羞愧）：黑色循环辗转往复、代代相传，而他绝大多数时候只能看着。",
                    "role": "other"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P022",
                        "P023",
                        "P024",
                        "P025",
                        "P026",
                        "P027"
                    ],
                    "summary": "说明为何雄辩无用：放下焦虑不保证得到“好结果”；且这份焦虑同时是其最大的安全感来源，被拿走会让人觉得自己没有尽到全部努力、怕原谅不了自己、甚至活不下去，故会像抗拒缴械一样抗拒它。",
                    "role": "qualification"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P028",
                        "P029",
                        "P030",
                        "P031",
                        "P032",
                        "P033"
                    ],
                    "summary": "作者自陈只能提供一份“也许”的方子：人不必一定要胜过别人；有价值只需坚持“付出大于索取”，成为净帮助、“有你比没你显然更好”就已安全，这才是安身立命的根本。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P034",
                        "P035",
                        "P036",
                        "P037",
                        "P038",
                        "P039"
                    ],
                    "summary": "指出该原则之难：多数人无法稳定做到，因为他们有充分理由觉得别人对不起自己，而且这些理由的确是对的；对方确实亏欠、伤害、出卖过你（包括作者本人在内的任何人都无法例外）。",
                    "role": "reason"
                },
                {
                    "unit_id": "U011",
                    "paragraph_refs": [
                        "P040",
                        "P041",
                        "P042",
                        "P043",
                        "P044",
                        "P045"
                    ],
                    "summary": "由此提出前提条件：坚持净输出就需要原谅，一直原谅；只要有一点不原谅，就会获得充分理由重回“比别人强才有资格活下去”的无间修罗场——那条通往深夜发问“孩子平庸，深感失望，怎么办”的路。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U012",
                    "paragraph_refs": [
                        "P046",
                        "P047",
                        "P048",
                        "P049",
                        "P050",
                        "P051",
                        "P052"
                    ],
                    "summary": "预答质疑与给出承诺性判断：走净输出之路可能被人认为会死于群狼分食（作者承认确有这可能），会遇到可怕对待；但坚持者不会害怕自己平庸，因为与ta相遇是幸运，足够多的人终会成为家人，这样的群体不可能没有一席之地。",
                    "role": "conclusion"
                },
                {
                    "unit_id": "U013",
                    "paragraph_refs": [
                        "P053",
                        "P054",
                        "P055",
                        "P056",
                        "P057",
                        "P058"
                    ],
                    "summary": "转向教育结论：平安之后才知道能给子女的最好铠甲，是善良、温柔同时理智、现实、强健的人格；这份人格的有无才是平庸与不平庸的真实分水岭，拥有者更可能被前辈识别、耐得住挫折并完成一万小时训练。",
                    "role": "conclusion"
                },
                {
                    "unit_id": "U014",
                    "paragraph_refs": [
                        "P059",
                        "P060"
                    ],
                    "summary": "教育判断：人的学习从社会化完成后才真正开始；社会化未完成而只教授大量信息的教育本质上是失败的，故在这种方向性错误的教育里表现“平庸”根本不值得担心。",
                    "role": "claim"
                },
                {
                    "unit_id": "U015",
                    "paragraph_refs": [
                        "P061",
                        "P062",
                        "P063"
                    ],
                    "summary": "收束：世界对人的专业技能要求极低，远低于对社会性功能的要求；几年后会发现那些整天痛感所有人都对不起他的人才是真的平庸——尽管他的指责都是确实的。",
                    "role": "conclusion"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为每一个人都是平庸的人，即使是那些被神化的人也一样。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为平庸之所以成为令人焦虑的问题，是因为大部分人都把生存看作一种竞争：仿佛食物、地皮有限，必须胜过别人才不算失败。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "opponent_view",
                    "attribution": "opponent",
                    "modality": "asserted",
                    "statement": "作者转述并要回应的说法：“弱就是原罪。”",
                    "evidence": [
                        "E3"
                    ]
                },
                {
                    "claim_id": "C004",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者对这种认知表示同情：持有它对世界的认知者，生活体验惨烈，随时担忧被淘汰、出卖、无视甚至消灭。",
                    "evidence": [
                        "E4"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为这种认知并非毫无道理，是受了无数令人痛苦的对待、被“现实”教育而成的；“现实”对此并非没有责任。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出世界确实存在贪婪、残忍、无耻和卑鄙，并认为这个民族在近代史上经受过空前的集体伤害，伤痕深嵌于民族性。",
                    "evidence": [
                        "E6",
                        "E7"
                    ]
                },
                {
                    "claim_id": "C007",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者认为焦虑驱使怀疑，而怀疑永远不会有足够证据能抵挡，几乎总是发育成“果然我没看错”的新事实。",
                    "evidence": [
                        "E8"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_reported",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者以引号独白转述代际传递的信念链：把“世界是地狱”的恐惧传给子女；只能凭优秀去争取被剥削的机会；唯一机会是爬上去成为强者，从而得出“平庸是罪”。",
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
                    "statement": "作者判断这个黑色循环辗转往复、代代相传，而自己绝大多数时候只能看着。",
                    "evidence": [
                        "E11",
                        "E12"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "negated",
                    "statement": "作者认为雄辩无法解决问题：即使把荒唐拆解明白，也不能保证对方放下焦虑就能得到想要的“好结果”。",
                    "evidence": [
                        "E13"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者指出这份让人夜不能寐的焦虑同时是其最大的安全感来源；拿走它，对方可能立刻活不下去，并会像抗拒缴械一样抗拒它。",
                    "evidence": [
                        "E14",
                        "E15"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提出替代原则：人是不必一定要胜过别人的；人要有价值，只需要坚持追求“付出大于索取”。",
                    "evidence": [
                        "E16",
                        "E17"
                    ]
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者认为能力再弱，只要是净帮助、对人“有你比没你显然更好”，就已经安全了，这才是人安身立命的根本。",
                    "evidence": [
                        "E18"
                    ]
                },
                {
                    "claim_id": "C014",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提醒做到净输出并不简单，世界上绝大多数人都无法稳定做到，因为他们觉得别人对不起自己、不配得这份输出——而且作者承认他们的理由的确是对的。",
                    "evidence": [
                        "E19",
                        "E20"
                    ]
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者承认对方确实对不起、亏欠、伤害甚至出卖过你，因为不这样做他们觉得活不下去；即使是公认善良的人也会不自觉这样做，没有人例外，包括作者本人。",
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
                    "statement": "作者提出坚持净输出的前提：需要一直原谅；只要有一点不原谅，就会获得充分理由重回“比别人强才有资格活下去”的无间修罗场。",
                    "evidence": [
                        "E23",
                        "E24"
                    ]
                },
                {
                    "claim_id": "C017",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者承认坚持净输出者可能被人认为会死于群狼分食，并承认这确有可能；但也判断其不会害怕自己平庸，因为与其相遇是幸运，足够多的人终会成为家人。",
                    "evidence": [
                        "E25",
                        "E26",
                        "E27"
                    ]
                },
                {
                    "claim_id": "C018",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为能给子女的最好铠甲不是专业能力或情商，而是善良、温柔同时理智、现实、强健的人格；这份人格的有无才是平庸与不平庸的真实分水岭。",
                    "evidence": [
                        "E28",
                        "E29"
                    ]
                },
                {
                    "claim_id": "C019",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者判断人的学习从社会化完成后才真正开始；社会化使命未完成而只教授大量信息的教育本质上是失败的，故在这种教育里表现“平庸”根本不值得担心。",
                    "evidence": [
                        "E30",
                        "E31"
                    ]
                },
                {
                    "claim_id": "C020",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为这个世界对人的专业技能要求极低，远低于对人的社会性功能的要求。",
                    "evidence": [
                        "E32"
                    ]
                },
                {
                    "claim_id": "C021",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者预言几年以后，那些整天痛感所有人都对不起他的人在你面前才是真的平庸——尽管他的指责都是确实的。",
                    "evidence": [
                        "E33",
                        "E34"
                    ]
                }
            ],
            "argument_steps": [
                "立论：每个人都平庸，被神化者也不例外（P001）。",
                "解释焦虑的认知根源：把生存看作竞争、资源有限必须胜出（P002），并转述“弱就是原罪”（P003）。",
                "第一重痛感：同情——持有该认知者的生活如无间地狱，“人终有一死”反成安慰（P004—P009）。",
                "第二重痛感：这种认知有现实根据，是被人痛苦的对待与“现实”教育出来的，“现实”并非没有责任（P010、P011）。",
                "承认世界确有贪婪、残忍、无耻、卑鄙（P012）；并给出历史解释：近代集体伤害形成的民族性伤痕产生焦虑，焦虑驱使怀疑并被自我证实（P013、P014）。",
                "以三段引号独白呈现代际传递：把地狱信念传给子女、只求被剥削的机会、爬上去成为强者，最终得出“平庸是罪”（P015—P018）。",
                "第三重痛感：黑色循环代代相传，作者只能看着（P019—P021）。",
                "说明雄辩无效且焦虑兼具安全感功能：拿走它可能让人活不下去，故会被拼死抗拒（P022—P027）。",
                "给出“也许”的方子：不必胜过别人，只需坚持付出大于索取、做净帮助者即已安全（P028—P033）。",
                "指出该原则之难：多数人做不到，因为其理由确实成立（P034—P039）。",
                "提出条件：需一直原谅，否则会重回修罗场——那条通向“孩子平庸怎么办”这个提问的路（P040—P045）。",
                "预答质疑并给出承诺性判断：可能被视为会死于群狼分食（作者承认可能），但不会害怕平庸，同类终成家人（P046—P052）。",
                "给出教育结论：能留给子女的最好铠甲是人格；人格才是平庸与否的分水岭（P053—P058）。",
                "教育判断：学习从社会化完成后才真正开始，方向性错误的教育里的“平庸”不值得担心（P059、P060）。",
                "收束：世界对专业技能要求极低，对社会性功能要求更高；最终真正平庸的是整天觉得所有人都对不起他的人（P061—P063）。"
            ],
            "concept_usage": [
                {
                    "term": "平庸",
                    "meaning": "作者先作普遍化断言（人人都平庸），后重新界定：真实意义上的平庸与否取决于是否具备“善良、温柔同时理智、现实、强健”的人格，而非专业能力、学历或智能。",
                    "evidence": "P056",
                    "ambiguity": "作者对“被神化的人也一样平庸”未给论证。"
                },
                {
                    "term": "净输出 / 净帮助",
                    "meaning": "作者提出的安身立命原则：坚持“付出大于索取”，对人而言“有你比没你显然更好”。",
                    "evidence": "P033",
                    "ambiguity": "作者未给出可操作的衡量标准。"
                },
                {
                    "term": "原谅",
                    "meaning": "作者指坚持净输出所需的前提：一直原谅伤害过自己的人（因其出于生存与害怕）。",
                    "evidence": "P040",
                    "ambiguity": "作者未说明原谅是否有边界或例外。"
                },
                {
                    "term": "无间修罗场",
                    "meaning": "作者对“比别人强才有资格活下去”那条竞争之路的比喻。",
                    "evidence": "P043",
                    "ambiguity": "无。"
                },
                {
                    "term": "社会化",
                    "meaning": "作者认为学习真正开始的前提；社会化未完成而仅教授信息的教育是失败的。",
                    "evidence": "P059",
                    "ambiguity": "作者未界定“正确社会化”的内容。"
                },
                {
                    "term": "一万小时训练",
                    "meaning": "作者借用的说法，指完成必要训练所需的时间投入。",
                    "evidence": "P057",
                    "ambiguity": "原说法出处未标注。"
                }
            ],
            "examples_and_targets": [
                "“弱就是原罪。”——作者转述的流行说法（P003）。",
                "“人终有一死”反而成了一种安慰——作者对焦虑者心理的描述（P008）。",
                "P015—P017 的三段引号独白——作者用以呈现代际传递信念的转述材料，未标明具体说话者。",
                "“孩子平庸，深感失望，怎么办”——作者在 P045 直接指涉本提问（元层面自指）。",
                "“群狼分食”——作者对坚持净输出者可能遭遇的比喻（P046）。",
                "浪子回头的青年完成举世瞩目的学业——作者举的例证（P060），未指名。",
                "被反驳对象：把生存视为竞争、以“弱就是原罪”为信的认知（P002、P003）；把专业能力当成平庸与否标准的看法（P056）。"
            ],
            "conditions": [
                "“无论对错也罢”（P006）——作者对同情对象认知的评价悬置。",
                "“你的能力再弱也罢，只要你是一个净帮助”（P033）——替代原则的适用条件。",
                "“因为他们觉得不这样做自己会活不下去”（P037）——对伤害行为原因的限定。",
                "“只要你有一点不原谅，你就立刻会获得一切充分的理由重回那条无间修罗场”（P043）——宽恕要求的严格条件。",
                "“如果你坚持走‘净输出’这条路”（P046）——后文承诺以坚持该路为前提，且作者承认“死于群狼分食”确有可能。",
                "“尽管其中很多需要经过很多坎坷”（P050）——对“成为家人”的限定。",
                "“如果没能及时完成正确社会化的使命，而仅仅是教授了大量的信息”（P059）——教育失败判断的条件。"
            ],
            "rhetoric_and_tone": "长篇劝慰兼论辩，情绪色彩浓：以“我心在滴血”“三个滴血”作结构标记，反复使用“无间地狱”“修罗场”“黑色的循环”“群狼分食”等强烈比喻；以引号独白模拟他人信念（P015—P017）；对读者用第二人称复数“你们”直陈其焦虑的双重性；结尾以“先愿你能有这样的平安”缓和，整体语气由悲悯转向劝勉与承诺。",
            "unresolved_questions": [
                "P015—P017 引号内独白的说话者未标明（是被转述的社会观念还是具体某人），按作者转述处理。",
                "“被神化的人也一样”缺乏例证，正文未说明所指。",
                "“一万小时训练”说法的出处，正文未标注，需外部核查。",
                "“净输出”“付出大于索取”如何衡量，正文未给标准。",
                "提问者所求的“如何调整积极面对”，作者未给具体操作步骤，仅给出原则与理由。",
                "版本信息：updated_at（2021-05-15）晚于 published_at（2020-01-12），差异内容未提供。",
                "本文无图片节点。lexical 段落节点 64 与正文段 63 的差异由生成器记录，不影响阅读。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "每一个人都是平庸的人，即使是那些被神化的人也一样。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "是因为大部分人都把生存看作是一种竞争。",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "弱就是原罪。",
                    "relation": "contradicts"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P006",
                    "quote": "生活的体验该是多么惨烈",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P010",
                    "quote": "是真的受了无数令人痛苦的对待，被“现实”教育成这样的。",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P012",
                    "quote": "这的确不是一个玫瑰色的世界",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P013",
                    "quote": "这份伤痕已经深嵌在民族性的深处，刻在了每一个人的灵魂上。",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P014",
                    "quote": "几乎总是发育成“果然我没看错”的新事实。",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P015",
                    "quote": "让他们继承这份恐惧",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P018",
                    "quote": "所以，平庸是罪。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P020",
                    "quote": "看着这个黑色的循环不断的辗转往复、代代相传",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P021",
                    "quote": "绝大多数时候，我都只能看着。",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P022",
                    "quote": "但我知道那都不能保证你依言放下了这份焦虑，一定就会得到你想要的“好结果”。",
                    "relation": "supports"
                },
                {
                    "key": "E14",
                    "paragraph_id": "P023",
                    "quote": "这份让你夜不能寐的焦虑感，对你却同时是最大的安全感来源。",
                    "relation": "supports"
                },
                {
                    "key": "E15",
                    "paragraph_id": "P026",
                    "quote": "让你们痛苦欲死的东西，拿走了，你们可能立刻就活不下去。",
                    "relation": "supports"
                },
                {
                    "key": "E16",
                    "paragraph_id": "P031",
                    "quote": "人是不必一定要胜过别人的。",
                    "relation": "supports"
                },
                {
                    "key": "E17",
                    "paragraph_id": "P032",
                    "quote": "只需要自己坚持追求“付出大于索取”的原则。",
                    "relation": "supports"
                },
                {
                    "key": "E18",
                    "paragraph_id": "P033",
                    "quote": "这才是人安身立命的根本。",
                    "relation": "supports"
                },
                {
                    "key": "E19",
                    "paragraph_id": "P034",
                    "quote": "这一点世界上的绝大多数人都无法稳定的做到。",
                    "relation": "supports"
                },
                {
                    "key": "E20",
                    "paragraph_id": "P036",
                    "quote": "他们的理由的确是对的。",
                    "relation": "supports"
                },
                {
                    "key": "E21",
                    "paragraph_id": "P037",
                    "quote": "因为他们觉得不这样做自己会活不下去",
                    "relation": "supports"
                },
                {
                    "key": "E22",
                    "paragraph_id": "P038",
                    "quote": "没有人能例外。包括告诉你这件事的我在内。",
                    "relation": "supports"
                },
                {
                    "key": "E23",
                    "paragraph_id": "P040",
                    "quote": "要坚持“保持净输出”这样一个简单的策略，你需要原谅。",
                    "relation": "supports"
                },
                {
                    "key": "E24",
                    "paragraph_id": "P043",
                    "quote": "你就立刻会获得一切充分的理由重回那条无间修罗场",
                    "relation": "supports"
                },
                {
                    "key": "E25",
                    "paragraph_id": "P046",
                    "quote": "事实上，也的确有这可能。",
                    "relation": "qualifies"
                },
                {
                    "key": "E26",
                    "paragraph_id": "P048",
                    "quote": "但是，你不用害怕你自己平庸，你真的不会害怕，而且是永远不会。",
                    "relation": "supports"
                },
                {
                    "key": "E27",
                    "paragraph_id": "P049",
                    "quote": "因为无论谁与你相遇，都是ta的幸运。",
                    "relation": "supports"
                },
                {
                    "key": "E28",
                    "paragraph_id": "P055",
                    "quote": "而是一个善良、温柔同时理智、现实、强健的人格。",
                    "relation": "supports"
                },
                {
                    "key": "E29",
                    "paragraph_id": "P056",
                    "quote": "才是真实意义上平庸和不平庸的分水岭",
                    "relation": "supports"
                },
                {
                    "key": "E30",
                    "paragraph_id": "P059",
                    "quote": "人的学习是从社会化完成后才真正开始的。",
                    "relation": "supports"
                },
                {
                    "key": "E31",
                    "paragraph_id": "P060",
                    "quote": "在这个方向性错误的“教育”里表现“平庸”，根本不值得担心。",
                    "relation": "supports"
                },
                {
                    "key": "E32",
                    "paragraph_id": "P061",
                    "quote": "其实这个世界对人的专业技能要求极低，远远低于对人的社会性功能的要求。",
                    "relation": "supports"
                },
                {
                    "key": "E33",
                    "paragraph_id": "P062",
                    "quote": "你会发现那些整天痛感所有人都对不起他的人在你面前才是真的平庸。",
                    "relation": "supports"
                },
                {
                    "key": "E34",
                    "paragraph_id": "P063",
                    "quote": "——尽管他的指责都是确实的。",
                    "relation": "qualifies"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "家庭教育",
                "社会心理",
                "伦理",
                "民族历史心理"
            ],
            "issue_candidates": [
                "平庸是否等于失败",
                "竞争式生存观",
                "焦虑的代际传递",
                "净输出与原谅",
                "人格与教育目标"
            ],
            "text_function_candidates": [
                "答疑",
                "劝慰",
                "论辩",
                "经验总结"
            ],
            "object_candidates": [
                "提问者",
                "父母",
                "子女",
                "被神化的人",
                "近代史中的民族",
                "善良的人",
                "作者本人"
            ],
            "working_keywords": [
                "平庸",
                "弱就是原罪",
                "无间地狱",
                "黑色的循环",
                "净输出",
                "付出大于索取",
                "原谅",
                "无间修罗场",
                "一万小时训练",
                "社会化"
            ]
        },
        "notes": "无图片节点。P015—P017 的引号独白未标明说话者，按作者转述的社会观念处理（author_reported），未归为作者自身主张；P045 直接指涉本提问，属作者自指。"
    },
    "35af9bf7": {
        "analysis": {
            "question_context": "提问者的问题是：面对新型冠状病毒肺炎疫情，科技公司能够做些什么？作者的回应分两层：先论证超级城市形态面临“完美传染病”的潜在毁灭风险、系统解决只有医学与社会管理两条路，并把武汉封城解读为对社会管理能力与外界信心的展示；再给出科技公司的四个专注方向。",
            "content_units": [
                {
                    "unit_id": "U001",
                    "paragraph_refs": [
                        "P001",
                        "P002"
                    ],
                    "summary": "提出风险命题：人类社会形态存在潜在的毁灭危机，即一次“完美传染病”；并列举其特征（潜伏期难察觉、潜伏期即高传染、死亡率中等、预后不良、变异快、多种常见动物为中间宿主），称其足以击溃超级城市。",
                    "role": "claim"
                },
                {
                    "unit_id": "U002",
                    "paragraph_refs": [
                        "P003"
                    ],
                    "summary": "论证超级城市的地位：它是文明成就最大的产物与支柱，依赖高铁、重载铁路、集装箱海运、国际机场、地铁公交、特高压电网、光纤网等，把数百万平方公里的人财物信息浓缩在极小地域，压缩空间距离这一最大交易成本，是经济繁荣的最大秘密。",
                    "role": "reason"
                },
                {
                    "unit_id": "U003",
                    "paragraph_refs": [
                        "P004",
                        "P005"
                    ],
                    "summary": "判断其脆弱性：这种不超过两百年的生存形态本质上是九龙城寨式的“违章建筑”，等待一次漏电火灾或瘟疫来宣告“你这样不行”；若未系统解决传染病问题，现有人口密度与超级城市形态就是未爆弹。",
                    "role": "claim"
                },
                {
                    "unit_id": "U004",
                    "paragraph_refs": [
                        "P006",
                        "P007",
                        "P008",
                        "P009",
                        "P010"
                    ],
                    "summary": "提出两条可行方案：一是医学进步（作者不多提，因路还长）；二是社会管理方案——对物资与成员行为实现绝对感知和掌控，从而能及时、精确、有效干预，安享高密度聚居红利。",
                    "role": "claim"
                },
                {
                    "unit_id": "U005",
                    "paragraph_refs": [
                        "P011",
                        "P012"
                    ],
                    "summary": "以武汉封城为例：它正在展现这种能力——中国可以、敢于作出决定并能有效执行；无论背后伦理与机制如何，做到这一点才算真正过了“超级城市”这一关。",
                    "role": "example"
                },
                {
                    "unit_id": "U006",
                    "paragraph_refs": [
                        "P013",
                        "P014",
                        "P015",
                        "P016"
                    ],
                    "summary": "以反问作跨国比较：孟买、达卡、河内、曼谷、马尼拉、里约、墨西哥、新奥尔良、纽约、巴黎、台北能否做到这么快、这么彻底，能做多少次、做多久；并由此提出“现代性大考”与保持超级城市形态的“体制许可证”。",
                    "role": "reason"
                },
                {
                    "unit_id": "U007",
                    "paragraph_refs": [
                        "P017",
                        "P018",
                        "P019"
                    ],
                    "summary": "对封城意义的解读：真正意向是为从根上消除世界对中国经济繁荣“医学脆弱性”的焦虑，向世界展示控制传染病的绝对能力与信心；这种能力与信心中国有，其他国家不见得有。",
                    "role": "claim"
                },
                {
                    "unit_id": "U008",
                    "paragraph_refs": [
                        "P020",
                        "P021"
                    ],
                    "summary": "经济逻辑：人类真正的问题只会是经济问题，而经济问题归根到底是信心问题；谁造就并维持信心谁就成为全球资源与资金的目的地；封城客观上是对“全球经济最安全、最强大的增长引擎”宝座的投资，且是好投资。",
                    "role": "reason"
                },
                {
                    "unit_id": "U009",
                    "paragraph_refs": [
                        "P022",
                        "P023",
                        "P024"
                    ],
                    "summary": "科技公司专注点之一、之二：快速廉价的检测技术（试纸、生物芯片）；便捷的消毒手段（喷雾、擦巾、臭氧/紫外光/高温消毒设备）。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U010",
                    "paragraph_refs": [
                        "P025",
                        "P026",
                        "P027",
                        "P028",
                        "P029",
                        "P030"
                    ],
                    "summary": "专注点之三（作者称为最大且近在眼前的风口）：时尚化的个人防护装备；个人防护有常态化机会，口罩可能成为新的领结或墨镜，防护面具成为新的时尚媒体，面料科技各方向获得更大研发市场空间。",
                    "role": "action_advice"
                },
                {
                    "unit_id": "U011",
                    "paragraph_refs": [
                        "P031",
                        "P032",
                        "P033"
                    ],
                    "summary": "专注点之四：远程办公与在线协作的软硬件厂商与咨询机构的机会——真正的聚集危险在办公楼与食堂等场景，生产无人化或远程化在新传染病成为常规威胁的时代会影响估值。",
                    "role": "action_advice"
                }
            ],
            "main_claims": [
                {
                    "claim_id": "C001",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为人类目前的社会形态存在一个潜在的毁灭危机，那就是一次“完美传染病”。",
                    "evidence": [
                        "E1"
                    ]
                },
                {
                    "claim_id": "C002",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者给出“完美传染病”的特征：潜伏期症状几乎不可察觉或混同一般常见病、潜伏期即具高传染性、发病后死亡率中等、预后不良、变异速度快、以多种常见动物为中间宿主，足以击溃超级城市。",
                    "evidence": [
                        "E2"
                    ]
                },
                {
                    "claim_id": "C003",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为人类文明成就最大的产物与支柱恰恰是超级城市这种社会形态，它通过交通、能源、通信网络把数百万平方公里的人财物信息浓缩在极小地域，把空间距离这一最大交易成本压缩到极点，这是目前经济繁荣的最大秘密。",
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
                    "statement": "作者判定这种出现不超过两百年的生存形态本质上只是九龙城寨式的“违章建筑”，在等待一次火灾或瘟疫宣告“你这样不行”。",
                    "evidence": [
                        "E5"
                    ]
                },
                {
                    "claim_id": "C005",
                    "claim_type": "author_qualified",
                    "attribution": "author",
                    "modality": "hypothetical",
                    "statement": "作者提出条件式警告：无论现在如何繁荣，如果没有系统解决传染病问题，目前的人口密度和超级城市形态就都是等待着爆炸的未爆弹。",
                    "evidence": [
                        "E6"
                    ]
                },
                {
                    "claim_id": "C006",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为系统解决传染病只有两个可见方案：医学进步（路还很长，作者不多提）与实现对物资和社会成员行为绝对感知掌控的社会管理方案。",
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
                    "statement": "作者认为拥有这种感知力、判断力与行动力的社会形态，才能安享高密度聚居红利而基本无惧传染病威胁。",
                    "evidence": [
                        "E9"
                    ]
                },
                {
                    "claim_id": "C008",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者把武汉封城解读为这种能力的展现：当真正需要时，中国可以、敢于作出这样的决定并能现实有效地执行。",
                    "evidence": [
                        "E10"
                    ]
                },
                {
                    "claim_id": "C009",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为无论达成该能力背后的伦理与机制如何，能够做到这一点才真正过了“超级城市”这一关。",
                    "evidence": [
                        "E11"
                    ]
                },
                {
                    "claim_id": "C010",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "questioned",
                    "statement": "作者以反问作比较：同样的动作能否在孟买、达卡、河内、曼谷、马尼拉、里约热内卢、墨西哥、新奥尔良、纽约、巴黎、台北做到，能否这么快这么彻底，即使能又能做多少次、做多久。",
                    "evidence": [
                        "E12",
                        "E13"
                    ]
                },
                {
                    "claim_id": "C011",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提出标准：能够做到、多次做到、且总有把握将疫区关闭隔离足够久，就是社会体制的“现代性大考”；考得过才有保持超级城市形态的“体制许可证”。",
                    "evidence": [
                        "E14"
                    ]
                },
                {
                    "claim_id": "C012",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者认为武汉封城真正的意向所指，是为了从根上消除世界对于中国经济繁荣的“医学脆弱性”的焦虑，并向世界展示中国控制传染病传播的绝对能力与绝对信心。",
                    "evidence": [
                        "E15",
                        "E16"
                    ]
                },
                {
                    "claim_id": "C013",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "qualified",
                    "statement": "作者认为这种能力与信心中国有，其他国家、其他经济体可不见得有；同时指出没有任何国家或经济体真正能免于疫情本身的发生。",
                    "evidence": [
                        "E17"
                    ]
                },
                {
                    "claim_id": "C014",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者提出经济逻辑：人类真正的问题只会是经济问题，一切经济问题归根到底是对未来的信心问题；谁能在世界上造就和维持这种信心，谁就会成为全球资源与资金的目的地。",
                    "evidence": [
                        "E18"
                    ]
                },
                {
                    "claim_id": "C015",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "asserted",
                    "statement": "作者把封城定性为对争夺“全球经济最安全、最强大的增长引擎”宝座的投资，而且是一项好投资。",
                    "evidence": [
                        "E19"
                    ]
                },
                {
                    "claim_id": "C016",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者建议科技公司的第一个专注点是快速廉价的检测技术，主要是各类试纸和生物芯片之类。",
                    "evidence": [
                        "E20"
                    ]
                },
                {
                    "claim_id": "C016b",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者建议科技公司的第二个专注点是便捷的消毒手段，包括喷雾、擦巾、便携或便于加装的臭氧消毒、紫外光消毒、高温消毒设备。",
                    "evidence": [
                        "E20b"
                    ]
                },
                {
                    "claim_id": "C017",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者建议科技公司关注时尚化的个人防护装备（称其为最大且近在眼前的风口）：个人防护有常态化机会，口罩可能成为新的领结或墨镜，防护面具可成为新的时尚媒体。",
                    "evidence": [
                        "E21",
                        "E22"
                    ]
                },
                {
                    "claim_id": "C018",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者判断个人防护类产品有机会成为新的大众消费品类并常态化，面料科技在透气性、抗菌性、亲肤性、可降解性、立体剪裁、先进织造、先进印染等方面将有更大市场空间支撑研发。",
                    "evidence": [
                        "E23"
                    ]
                },
                {
                    "claim_id": "C019",
                    "claim_type": "author_explicit",
                    "attribution": "author",
                    "modality": "predicted",
                    "statement": "作者判断远程办公与在线协作是软硬件厂商和咨询机构的机会：真正聚集大量人口的危险场景在办公室与食堂，若实现生产无人化或远程化，在新传染病成为常规威胁的时代将影响股价估值。",
                    "evidence": [
                        "E24",
                        "E25"
                    ]
                }
            ],
            "argument_steps": [
                "提出问题：社会形态存在潜在毁灭危机，即“完美传染病”（P001），并列举其病原特征（P002）。",
                "论证超级城市的地位与效率来源（P003）。",
                "判定其脆弱性：不超过两百年的形态如“违章建筑”，等待火灾或瘟疫检验（P004）；未系统解决传染病则人口密度与超级城市形态皆为未爆弹（P005）。",
                "提问“何谓系统的解决传染病”，列出两个可见方案（P006、P007）。",
                "方案一：医学进步，作者不多提，因路途仍长（P008）。",
                "方案二：社会管理——对物资与成员行为的绝对感知与掌控，实现及时精确有效的干预（P009），从而安享高密度红利（P010）。",
                "以武汉封城为例说明该能力已被展现（P011），并强调能做到才过“超级城市”这一关（P012）。",
                "以跨国反问作比较，提出“现代性大考”与“体制许可证”（P013—P016）。",
                "解读封城意向：消除外界对中国经济繁荣“医学脆弱性”的焦虑，展示绝对能力与信心（P017、P018、P019）。",
                "给出经济逻辑：经济问题即信心问题，信心决定资源与资金流向（P020）；封城因此是争夺增长引擎宝座的好投资（P021）。",
                "转入科技公司的具体专注点：检测技术（P023）、消毒手段（P024）、时尚化个人防护装备（P025—P030）、远程办公与在线协作（P031—P033）。"
            ],
            "concept_usage": [
                {
                    "term": "完美传染病",
                    "meaning": "作者定义的一种假想病原所引发的危机：潜伏期难察觉且高传染、死亡率中等、预后不良、变异快、多动物宿主，足以击溃超级城市。",
                    "evidence": "P002",
                    "ambiguity": "为作者设想的模型，非对既有病原的描述。"
                },
                {
                    "term": "超级城市",
                    "meaning": "作者视为文明最大产物与支柱的高密度聚居形态，其红利来自空间距离这一交易成本的压缩。",
                    "evidence": "P003",
                    "ambiguity": "作者未给出规模界限。"
                },
                {
                    "term": "系统的解决传染病",
                    "meaning": "作者界定为两条路径：医学进步，或实现对物资与成员行为的绝对感知与掌控。",
                    "evidence": "P009",
                    "ambiguity": "作者未说明该掌控的边界与代价。"
                },
                {
                    "term": "现代性大考 / 体制许可证",
                    "meaning": "作者用来衡量社会体制能否维持超级城市形态的标准：能多次、足够久地关闭隔离疫区。",
                    "evidence": "P016",
                    "ambiguity": "为作者自设比喻。"
                },
                {
                    "term": "医学脆弱性",
                    "meaning": "作者指外界对中国经济繁荣在传染病面前脆弱性的焦虑（加引号）。",
                    "evidence": "P017",
                    "ambiguity": "未注明该说法的来源。"
                }
            ],
            "examples_and_targets": [
                "武汉封城——作者用作社会管理能力的例证（P011、P017、P018、P021）。",
                "孟买、达卡、河内、曼谷、马尼拉、里约热内卢、墨西哥、新奥尔良、纽约、巴黎、台北——作者反问比较的城市（P013）。",
                "九龙城寨式的“违章建筑”——作者对超级城市形态的比喻（P004）。",
                "高铁、重载铁路、万吨级集装箱海运、年流量过亿人次的国际机场、日流量达千万的地下铁/公交、高压/特高压输电网络、高速光纤网——作者列举的基础设施（P003）。",
                "口罩、头罩、手套、防护镜、防护面具、罩衫设计、赛博朋克、cos——作者对未来防护时尚化的设想（P026—P030）。",
                "试纸、生物芯片、臭氧/紫外光/高温消毒设备——作者建议的产品方向（P023、P024）。"
            ],
            "conditions": [
                "“无论你现在如何繁荣昌盛，如果你没有系统的解决传染病问题……”（P005）——未爆弹判断的条件。",
                "“无论达成这个能力背后的伦理如何、机制如何”（P012）——作者对价值判断的悬置。",
                "“能够做到、而且是多次做到、而且是总有把握将疫区关闭隔离足够久”（P016）——过关的三重条件。",
                "“它至少可以合法的成为部分人可以选择的生活方式”（P026）——对防护常态化的限缩表述。",
                "“在新传染病成为常规威胁的时代”（P032）——远程办公价值的条件。",
                "“如果能够实现生产无人化或者远程化”（P032）——机会成立的条件。",
                "“很可能”“可能”等词贯穿 P026—P029，作者对时尚化前景用了可能式表述。"
            ],
            "rhetoric_and_tone": "宏观论断式评论，语气自信且带宣传性：以“未爆弹”“炼狱”“违章建筑”“九龙城寨”等强烈比喻制造危机感；用连续反问（“能不能做到这么快、这么彻底？”“即使能，能做多少次？能做多久？”）施压；对武汉封城使用“清脆”“绝对能力和绝对信心”“一项好投资”等肯定语；末尾转为商业机会清单式的实务建议，并出现“coser们终于可以名正言顺的玩scifi风的cos了，赛博朋克就在眼前”的调侃句。",
            "unresolved_questions": [
                "P020“人类真正的问题，只会是经济问题”为极强断言，正文未给论证。",
                "“完美传染病”的具体病原学参数（潜伏期、死亡率、变异速度）为作者设想，正文未给依据，需外部核查。",
                "各国能否执行封城的比较，正文未提供证据或数据。",
                "P026—P029 关于防护装备时尚化、常态化的前景均为预测，正文未给市场数据。",
                "本文发表时间（2020-01-24）与疫情早期信息条件相关，文中对封城的解读属当时判断，需结合时间背景核查。",
                "版本信息：updated_at（2022-04-14）晚于 published_at（2020-01-24），差异内容未提供。",
                "本文无图片节点。"
            ],
            "evidence": [
                {
                    "key": "E1",
                    "paragraph_id": "P001",
                    "quote": "那就是一次“完美传染病”。",
                    "relation": "supports"
                },
                {
                    "key": "E2",
                    "paragraph_id": "P002",
                    "quote": "足以击溃目前人类社会最大的文明成就——超级城市。",
                    "relation": "supports"
                },
                {
                    "key": "E3",
                    "paragraph_id": "P003",
                    "quote": "其实恰恰是超级城市这种社会形态。",
                    "relation": "supports"
                },
                {
                    "key": "E4",
                    "paragraph_id": "P003",
                    "quote": "这是目前的经济繁荣的最大秘密。",
                    "relation": "supports"
                },
                {
                    "key": "E5",
                    "paragraph_id": "P004",
                    "quote": "在本质上却只是一种九龙城寨式的“违章建筑”",
                    "relation": "supports"
                },
                {
                    "key": "E6",
                    "paragraph_id": "P005",
                    "quote": "目前的人口密度和超级城市形态就都是等待着爆炸的未爆弹。",
                    "relation": "supports"
                },
                {
                    "key": "E7",
                    "paragraph_id": "P008",
                    "quote": "第一个当然是医学的进步。",
                    "relation": "supports"
                },
                {
                    "key": "E8",
                    "paragraph_id": "P009",
                    "quote": "实现对物资和社会成员行为的绝对感知和掌控",
                    "relation": "supports"
                },
                {
                    "key": "E9",
                    "paragraph_id": "P010",
                    "quote": "才可以安然的享有高密度聚居所带来的红利而基本无惧传染病的潜在威胁。",
                    "relation": "supports"
                },
                {
                    "key": "E10",
                    "paragraph_id": "P011",
                    "quote": "中国可以、敢于做出这样的决定，并且能够将其现实有效的执行。",
                    "relation": "supports"
                },
                {
                    "key": "E11",
                    "paragraph_id": "P012",
                    "quote": "能够做到这一点，才是真正过了“超级城市”这一关。",
                    "relation": "supports"
                },
                {
                    "key": "E12",
                    "paragraph_id": "P013",
                    "quote": "同样的动作能不能在孟买做到",
                    "relation": "supports"
                },
                {
                    "key": "E13",
                    "paragraph_id": "P015",
                    "quote": "即使能，能做多少次？能做多久？",
                    "relation": "supports"
                },
                {
                    "key": "E14",
                    "paragraph_id": "P016",
                    "quote": "就是社会体制的“现代性大考”。",
                    "relation": "supports"
                },
                {
                    "key": "E15",
                    "paragraph_id": "P017",
                    "quote": "为了从根上消除世界对于中国经济繁荣的“医学脆弱性”的焦虑。",
                    "relation": "supports"
                },
                {
                    "key": "E16",
                    "paragraph_id": "P018",
                    "quote": "同时也是在向世界展示中国对控制传染病传播问题的绝对能力和绝对信心。",
                    "relation": "supports"
                },
                {
                    "key": "E17",
                    "paragraph_id": "P019",
                    "quote": "中国有，其他国家、其他经济体可不见得有。",
                    "relation": "supports"
                },
                {
                    "key": "E18",
                    "paragraph_id": "P020",
                    "quote": "谁能在世界上造就和维持这种信心，谁就会成为全球资源与资金的目的地",
                    "relation": "supports"
                },
                {
                    "key": "E19",
                    "paragraph_id": "P021",
                    "quote": "而且是一项好投资。",
                    "relation": "supports"
                },
                {
                    "key": "E20",
                    "paragraph_id": "P023",
                    "quote": "第一个当然是快速廉价的检测技术",
                    "relation": "supports"
                },
                {
                    "key": "E20b",
                    "paragraph_id": "P024",
                    "quote": "第二，便捷的消毒手段。",
                    "relation": "supports"
                },
                {
                    "key": "E21",
                    "paragraph_id": "P025",
                    "quote": "就是时尚化的个人防护装备。",
                    "relation": "supports"
                },
                {
                    "key": "E22",
                    "paragraph_id": "P027",
                    "quote": "那么口罩也就将成为新的领结或墨镜",
                    "relation": "supports"
                },
                {
                    "key": "E23",
                    "paragraph_id": "P029",
                    "quote": "都可以有更大的市场空间来支撑更多的研发。",
                    "relation": "supports"
                },
                {
                    "key": "E24",
                    "paragraph_id": "P031",
                    "quote": "第四个，是属于远程办公和在线协作的软硬件厂商和咨询机构的机会。",
                    "relation": "supports"
                },
                {
                    "key": "E25",
                    "paragraph_id": "P032",
                    "quote": "真正聚集大量人口的危险场景在这里。",
                    "relation": "supports"
                }
            ]
        },
        "provisional_tags": {
            "domain_candidates": [
                "公共卫生",
                "城市与社会形态",
                "宏观经济",
                "科技产业"
            ],
            "issue_candidates": [
                "完美传染病风险",
                "超级城市脆弱性",
                "封城与社会管理能力",
                "信心与经济",
                "科技公司的疫情机会"
            ],
            "text_function_candidates": [
                "答疑",
                "评论",
                "预测",
                "建议"
            ],
            "object_candidates": [
                "提问者",
                "科技公司",
                "武汉",
                "中国",
                "孟买",
                "达卡",
                "河内",
                "曼谷",
                "马尼拉",
                "里约热内卢",
                "墨西哥",
                "新奥尔良",
                "纽约",
                "巴黎",
                "台北",
                "世界"
            ],
            "working_keywords": [
                "完美传染病",
                "超级城市",
                "违章建筑",
                "未爆弹",
                "现代性大考",
                "体制许可证",
                "医学脆弱性",
                "信心问题",
                "个人防护装备",
                "远程办公"
            ]
        },
        "notes": "无图片节点。P020 的“人类真正的问题，只会是经济问题”为极强断言，已按 asserted 记录并列入待核查；对封城的解读与时尚化前景均属作者判断与预测，未作实证结论。"
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
