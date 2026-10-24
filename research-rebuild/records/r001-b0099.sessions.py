# -*- coding: utf-8 -*-
"""批次 r001-b0099 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0099.sessions.py            # 写 out/r001-b0099.out.jsonl
  python3 records/r001-b0099.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0099"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0099.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "8a7bdf9f": {
  "analysis": {
   "question_context": "知乎提问“如何学好现代语文？”（Q001，属提问者）之下的答主回答。作者不复述提问者立场，而是先自问“什么叫做学好”，再以“语文能力是一切能力的基础”和自造的“表达刚度”标准作答。brief 只指向作者另一篇讲“年轻时候最核心的能力”的文章，未提供额外语境。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002"
     ],
     "summary": "作者先反问“什么叫做学好”，并称另一篇文里谈过“年轻时候最核心的能力”。",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P003",
      "P004"
     ],
     "summary": "界定语文功能：不用来作诗写散文，而用来说事、说明问题、阐述理由、表达方案；首要功能是正确完整简洁地表达、避免歧义误解。",
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
     "summary": "语文能力是一切能力的基础、不可绕过；语文不好者无资格抱怨被抛弃，第一要害是认清此点。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P009",
      "P010",
      "P011",
      "P012",
      "P013",
      "P014",
      "P015",
      "P016",
      "P017",
      "P018",
      "P019",
      "P020"
     ],
     "summary": "以“半兽人”比喻论证无权自甘不善表达：语言是人的根本属性，人的权利与享受按语言能力打折；第一课是断绝可以不学好语文的妄想。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P021",
      "P022",
      "P023",
      "P024",
      "P025",
      "P026",
      "P027"
     ],
     "summary": "第二课：承担表达责任——别人没听懂即你失败；技术上无条件成立，但改不改取决于是否值得投入成本；先立原则才会复盘改进而非推责。",
     "role": "action_advice"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P028",
      "P029",
      "P030",
      "P031",
      "P032"
     ],
     "summary": "价值链：听众基础越大越有案例客观自评，进而判定分寸、往回收，在语义清晰前提下追求效率；大众浅显长篇、精英简练短篇，简练即利润。",
     "role": "reason"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P033",
      "P034",
      "P035"
     ],
     "summary": "结论：语文能力关系到这条命的价值，直接决定一生赚取利润的上限（中彩票不算赚取）。",
     "role": "conclusion"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
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
     "summary": "技术标准：以中译英再英译中为一轮“刚度检验”，文本保持自身不变的性能即表达刚度，分不合格/良好/优秀/完美四档；自创术语可换缩写。",
     "role": "definition"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P046",
      "P047"
     ],
     "summary": "请读者自测打分，并把学习目标设为“近乎本能地写出刚度良好以上的句子”，不必管高考语文与唐诗宋词。",
     "role": "action_advice"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P048",
      "P049",
      "P050",
      "P051",
      "P052",
      "P053",
      "P054"
     ],
     "summary": "刚度水平的稀有度（百中无一/千中无一/万中无一，第三层是绝对精英）与回报：三十岁前拥有者从商可望巨擘、用学可望泰斗、从艺可望宗师。",
     "role": "claim"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P055",
      "P056"
     ],
     "summary": "反证：说不清话就与真正的权力和地位无缘，太子也只是读稿器、盖章机加替罪羊。",
     "role": "reason"
    },
    {
     "unit_id": "U012",
     "paragraph_refs": [
      "P057",
      "P058",
      "P059",
      "P060",
      "P061",
      "P062",
      "P063",
      "P064",
      "P065",
      "P066",
      "P067",
      "P068",
      "P069",
      "P070"
     ],
     "summary": "要点一：写抗歧义抗干扰的“健康”句子，不随便省略成分以降低上下文依赖（借“高内聚、低耦合”），以“吃了吗？”三例说明；长与费非致命，歧义才致命；并警告避免网络流行语。",
     "role": "action_advice"
    },
    {
     "unit_id": "U013",
     "paragraph_refs": [
      "P071",
      "P072",
      "P073",
      "P074",
      "P075",
      "P076",
      "P077",
      "P078",
      "P079"
     ],
     "summary": "要点二：句子与段落调性一致，以英语成分呼应、日语敬语联动为例，说明多重呼应构成反歧义系统。",
     "role": "action_advice"
    },
    {
     "unit_id": "U014",
     "paragraph_refs": [
      "P080",
      "P081",
      "P082",
      "P083",
      "P084",
      "P085",
      "P086"
     ],
     "summary": "要点三：正确使用标点，尤其逻辑关联类符号要加倍在意；不能用则难表达复杂概念（多因少读复杂文献）；古代中国以“之乎者也矣焉哉”“骈四俪六”实现同一功能。",
     "role": "action_advice"
    },
    {
     "unit_id": "U015",
     "paragraph_refs": [
      "P087",
      "P088",
      "P089",
      "P090",
      "P091"
     ],
     "summary": "要点四：叙述论证要有章法与规划（电子邮件、情书、通知请柬合同请假条的框架）；并斥能把这类文字写得辞能达意、无自相矛盾者之少为我国语文教育之耻辱。",
     "role": "action_advice"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "语文不用来作诗写散文，而用来说事、说明问题、阐述理由、表达方案；首要功能是正确完整简洁地表达、避免歧义误解，为高效低冲突协作打基础。",
     "evidence": [
      "E001",
      "E002"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "语文能力是一切能力的基础、能力之上的能力，绝不能绕过、回避或抱侥幸。",
     "evidence": [
      "E003"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "语文不好者无资格抱怨不被理解、不被原谅，因为是他先以高企的沟通成本抛弃了所有人；学好语文的第一个要害就是认清这一点。",
     "evidence": [
      "E004",
      "E005",
      "E006"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人没有权利自甘“我笨嘴拙舌，不善表达”，因为语言是人类的根本属性、是人区别于动物的要害。",
     "evidence": [
      "E007",
      "E008"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "生而为人的权利、享受与人有别于兽的能力都依语言能力打折；语文能力决定主要成分表里有多少是人。",
     "evidence": [
      "E009",
      "E010"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "第一课是断绝可以不学好语文的任何妄想；政治正确只能帮募捐学费，对争取实际权利与礼遇没有意义。",
     "evidence": [
      "E011",
      "E012"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "第二课是承担自己的表达责任：别人没听懂、听错、听不进去就是你失败，就是你说得不明白、不准确、表达方式仍需改进。",
     "evidence": [
      "E013",
      "E014"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "该责任结论在技术上无条件成立，但具体某件事是否值得改进要看它值不值得投入成本。",
     "evidence": [
      "E015"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "先立此原则才会关心问题出在哪里、复盘修正，而不是把责任推给对方理解力；思考结果不一定用在那人身上，但仍应获得。",
     "evidence": [
      "E016",
      "E017"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "更强的表达能力带来最大的听众基础与足够案例以客观自评，进而能判定分寸、往回收，在语义清晰基础上追求效率。",
     "evidence": [
      "E018",
      "E019"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "效率以可得、必要的接收者能正确接收为前提（大众宜浅显长篇、精英可简练短篇）；简练即效率与利润，但靠更高的“无误压缩算法”而非无视歧义，且必须先有对大众准确表达的能力。",
     "evidence": [
      "E020",
      "E021",
      "E022"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "语文能力关系到这条命最后价值几何；对只听得懂功利语言者，直接决定一生赚取利润的上限（中彩票不算赚取）。",
     "evidence": [
      "E023",
      "E024",
      "E025"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "“刚度检验”是中译英再英译中一轮；表达刚度即文本在此检验中保持自身不变的性能，分不合格/良好/优秀/完美四档；自创术语换专用缩写属合法修正。",
     "evidence": [
      "E026",
      "E027",
      "E028",
      "E029",
      "E030",
      "E031"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "学习目标可直接设为“能近乎本能的写出刚度良好以上的句子”，不必管高考语文与唐诗宋词。",
     "evidence": [
      "E032",
      "E033"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "表达刚度良好以上极稀有：第一稿良好者百中无一、正常打字速度首次成稿者千中无一、一挥而就完美者万中无一，第三层是绝对精英。",
     "evidence": [
      "E034",
      "E035",
      "E036"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "三十岁前拥有这份语言能力，从商可望巨擘、用学可望泰斗、从艺可望宗师；作者称没有任何夸张。",
     "evidence": [
      "E037"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "说不清话就基本与真正的权力和地位告别；生来是太子，实际坐龙椅的也是能说得清的人，自己只是读稿器、盖章机加替罪羊。",
     "evidence": [
      "E038",
      "E039"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要写“健康”（强抗歧义、抗干扰）的句子：要点一是不随便省略成分、降低上下文依赖；长与费非致命，歧义和误解才致命。",
     "evidence": [
      "E040",
      "E041",
      "E042",
      "E043",
      "E045"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要格外警惕并有意避免网络流行语，因其为留深刻印象普遍采用特殊句式或故意构造的异常句式和造词法。",
     "evidence": [
      "E046"
     ]
    },
    {
     "claim_id": "C020",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "除非已经功力深厚、八风不动，否则不要用网络流行语、更不要大量用；那体现可悲的求认同的软弱，而填补心里的洞需要被严肃对待而非被喜欢。",
     "evidence": [
      "E047",
      "E048",
      "E049"
     ]
    },
    {
     "claim_id": "C021",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要点二：句子与段落保持鲜明一致的调性，把意图从句子的每个成分上呼应表示出来；英语靠成分反复呼应构成反歧义系统，听者漏词也往往能维持原意，日语敬语有类似联动。",
     "evidence": [
      "E050",
      "E051",
      "E052",
      "E053",
      "E054",
      "E055"
     ]
    },
    {
     "claim_id": "C022",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要点三：正确使用标点，尤其冒号、引号、顿号、分号、括号、破折号这些逻辑关联符号要加倍在意；不能用则难表达复杂概念（多因少读复杂文献），古代中国以“之乎者也矣焉哉”“骈四俪六”实现同一功能。",
     "evidence": [
      "E056",
      "E057",
      "E058",
      "E059"
     ]
    },
    {
     "claim_id": "C023",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要点四：叙述论证要有章法和基本规划（如电子邮件的称呼、导言、罗列事务、结语、落款，以及单一事务的固定结构）。",
     "evidence": [
      "E060",
      "E061"
     ]
    },
    {
     "claim_id": "C024",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "能把通知、请柬、合同、请假条写得辞能达意、无自相矛盾、无丢三落四者之少，堪称我国语文教育之耻辱。",
     "evidence": [
      "E062"
     ]
    }
   ],
   "argument_steps": [
    "以反问设定议题（什么叫做学好），并指向作者另一篇讲“年轻时候最核心的能力”的文章为前提。",
    "给出语文的功能定义（说事、说明问题、阐述理由、表达方案；正确完整简洁、避免歧义），并提升强度：语文能力是一切能力的基础、不可绕过。",
    "推出责任归属：语文不好者无资格抱怨被抛弃；再以“语言是人的根本属性”论证无权自甘不善表达，用半兽人、打折等比喻推出权利按语言能力折算。",
    "第一课：断绝可以不学好语文的妄想（政治正确帮不上实际权利）；第二课：承担表达责任——别人没听懂即你失败，技术上无条件成立，但改不改取决于是否值得投入成本。",
    "效率论证：更强表达→最大听众基础→足够案例自评→判定分寸往回收→在语义清晰前提下追求效率；大众浅显长篇、精英简练短篇。",
    "落到功利结论：语文能力关系命的价值，直接决定一生赚取利润的上限（中彩票不算赚取）。",
    "转入技术问题：定义刚度检验与表达刚度及四档，给出“近乎本能写出刚度良好以上句子”的目标与稀有度，并以从商巨擘到读稿器、盖章机、替罪羊的两端前景加压。",
    "列出四条要点：不省略成分、降低上下文依赖并警惕网络流行语；调性一致、靠多重呼应反歧义；正确使用标点，尤其逻辑关联类符号；叙述论证有章法与规划。",
    "以批评收尾：能把通知、请柬、合同、请假条写得辞能达意、无自相矛盾、无丢三落四者之少，堪称我国语文教育之耻辱。"
   ],
   "concept_usage": [
    {
     "term": "学好（语文）",
     "meaning": "先以反问提出，后以语文功能与“表达刚度良好以上”间接界定，无统一定义。",
     "evidence": "P001",
     "ambiguity": "目标定在“良好以上”还是“完美”，文中两处标准不完全一致。"
    },
    {
     "term": "语文能力",
     "meaning": "一切能力的基础、能力之上的能力；关系命的价值与一生赚取利润的上限。",
     "evidence": "P005",
     "ambiguity": "与“表达能力”“语言能力”互换使用，未作区分。"
    },
    {
     "term": "刚度检验与表达刚度",
     "meaning": "中译英再英译中为一轮刚度检验；文本在此检验中保持自身不变的性能即表达刚度，分四档。",
     "evidence": "P039",
     "ambiguity": "依赖谷歌翻译，未说明版本与“无需猜测补足”的判定；术语缩写修正的边界未说明。"
    },
    {
     "term": "健康（句子/语法结构）",
     "meaning": "有很强的抗歧义、抗干扰性能。",
     "evidence": "P058",
     "ambiguity": "与“刚度”是何关系，文中未对应。"
    },
    {
     "term": "效率（简练）",
     "meaning": "在保持语义清晰基础上对可得、必要接收者的简练与篇幅压缩，作者称之为效率、利润。",
     "evidence": "P029",
     "ambiguity": "以“值不值得投入成本”为条件，未给阈值。"
    },
    {
     "term": "高内聚、低耦合",
     "meaning": "借自设计领域：功能尽可能不依赖不属于自己的部分，用于说明抗上下文依赖。",
     "evidence": "P061",
     "ambiguity": "工程术语直接移用，未加限定。"
    },
    {
     "term": "无误压缩算法",
     "meaning": "作者自造说法：不引入错误与歧义地压缩篇幅的能力。",
     "evidence": "P032",
     "ambiguity": "未定义、未举例。"
    },
    {
     "term": "半兽人",
     "meaning": "对自称“笨嘴拙舌、不善表达”者的比喻性称呼，由此推出无法领取全人待遇。",
     "evidence": "P009",
     "ambiguity": "修辞性贬称，是否作者严格立场未加限定。"
    },
    {
     "term": "网络流行语",
     "meaning": "为留深刻印象而普遍采用特殊句式或故意构造的异常句式与造词法的说法。",
     "evidence": "P067",
     "ambiguity": "未举例，边界不清。"
    }
   ],
   "examples_and_targets": [
    "作者另一篇谈“年轻时候最核心的能力”的文章——自我引用作前提，篇目与链接未给（P002）。",
    "半兽人、阉人（给阉人变出子女）——比喻，说明语言能力不足者无法以金钱换取全人待遇（P009、P016）。",
    "太子、龙椅、读稿器、盖章机、替罪羊——举例/比喻，说明说不清话者无法真正掌权（P056）。",
    "中彩票（不妨碍中彩票但中彩票不算赚取）——反例，用于限定“赚取”的含义（P035）。",
    "“吃了吗？”／“您吃了吗？”／“您吃了早饭吗？”——举例，说明省略主语加重上下文依赖（P062-P064）。",
    "英语第三人称单数与动词、介词搭配；日语敬语——举例，说明多重成分联动的反歧义设计（P074、P078）。",
    "谷歌翻译——被指定为刚度检验的工具（P039）。",
    "“之乎者也矣焉哉”“骈四俪六”——举例，说明古代中国以更复杂严苛的手段实现标点的逻辑功能（P086）。",
    "电子邮件、情书、通知、请柬、合同、请假条；“吃你几个烂西瓜还要给钱”——举例，说明叙述论证的章法与情书需附解释（P088-P090）。",
    "知乎3.5亿用户——数据，用作刚度稀有度的统计范围（P049）。"
   ],
   "conditions": [
    "讨论对象是现代语文/中文表达，场景以职业与社会协作中的表达与理解为主（P003、P004）。",
    "第二课的责任在技术上无条件成立，但具体是否改进取决于这件事值不值得投入成本（P024）。",
    "效率追求以“可得、必要的接收者可以正确的接收”为前提，对大众与对精英的策略不同（P030）。",
    "简练与短篇以先具备“对大众准确表达的能力”为前提（P032）。",
    "刚度检验依赖谷歌翻译的中译英再英译中，并允许把自创专有术语替换为专用缩写（P039、P045）。",
    "网络流行语的禁令有条件：除非已经功力深厚、八风不动（P068）。",
    "标点要点针对说明艰深关系的文字，作者称极少有能只用情绪类符号交差的（P083）。",
    "稀有度的量化判断以知乎3.5亿用户为范围（P049）。"
   ],
   "rhetoric_and_tone": "训诫文与技术指南的混合体：通篇第二人称“你”直呼读者，断言密集，并自设“第一课／第二课／四个要点”的教程结构。多用夸张与贬抑性比喻（半兽人、阉人、读稿器、盖章机、替罪羊）和口语调侃（no can do、谢谢）；以自我引用建立前提，以反问推进（看看能得多少分？、你要质疑古代中国没有这些符号为什么也行？）；并靠括号补注与自造术语（表达刚度、ES）营造客观标准感；结尾转向对我国语文教育的直接斥责，训诫色彩最强。",
   "unresolved_questions": [
    "P002 指向作者自己另一篇文章（“人在年轻的时候，最核心的能力是什么？”），该篇未给出标题或链接，无法核查这一前提。",
    "全文未给出“学好”的统一定义，只以功能描述与刚度标准间接界定。",
    "“表达刚度”检验依赖具体的机器翻译系统（谷歌翻译），未说明版本、轮次与“语义无需猜测补足”的判定方式，可重复性未交代。",
    "知乎3.5亿用户及百中无一／千中无一／万中无一的比例没有来源与统计口径。",
    "“合法的修正”（自创术语换缩写）的边界未说明，是否会与“保持自身不变”的标准冲突未讨论。",
    "把语文能力不足者称为“半兽人”并断言其权利按比例打折，是严格立场还是修辞夸张，文中未加限定。",
    "阅读包中的 brief 在“为有效率、少冲突的协作打下沟”处被截断，本文不将其作为证据；完整 brief 需回查原始批次数据。"
   ],
   "evidence": [
    {
     "key": "E001",
     "paragraph_id": "P003",
     "quote": "语文不是用来作诗的，不是用来写散文的，而是首先用来说事的",
     "relation": "supports"
    },
    {
     "key": "E002",
     "paragraph_id": "P004",
     "quote": "它首要的功能是正确、完整而简洁的表达你要表达的意思，避免歧义和误解",
     "relation": "supports"
    },
    {
     "key": "E003",
     "paragraph_id": "P005",
     "quote": "语文能力就是一切能力的基础，是能力之上的能力",
     "relation": "supports"
    },
    {
     "key": "E004",
     "paragraph_id": "P006",
     "quote": "身体健康而语文不好的人，没有资格抱怨不被理解和不被原谅。",
     "relation": "supports"
    },
    {
     "key": "E005",
     "paragraph_id": "P007",
     "quote": "在别人努力再三、实在无法负担得起沟通成本而离开你之前，你早已把对方抛弃了。",
     "relation": "supports"
    },
    {
     "key": "E006",
     "paragraph_id": "P008",
     "quote": "学好语文的第一个要害，就是认清楚这一点。",
     "relation": "supports"
    },
    {
     "key": "E007",
     "paragraph_id": "P009",
     "quote": "身为人类，是没有权利自甘“我笨嘴拙舌，不善表达”的。",
     "relation": "supports"
    },
    {
     "key": "E008",
     "paragraph_id": "P010",
     "quote": "身为半兽人确实无法领取全人的待遇。",
     "relation": "supports"
    },
    {
     "key": "E009",
     "paragraph_id": "P014",
     "quote": "甚至一切人有别于兽的能力，对你全都是依照语言能力来打折的。",
     "relation": "supports"
    },
    {
     "key": "E010",
     "paragraph_id": "P017",
     "quote": "语文能力，决定你的主要成分表里有多少是人。",
     "relation": "supports"
    },
    {
     "key": "E011",
     "paragraph_id": "P018",
     "quote": "这是你要学好语文的第一课——断绝可以不学好它的任何妄想。",
     "relation": "supports"
    },
    {
     "key": "E012",
     "paragraph_id": "P020",
     "quote": "政治正确在这里只能帮你募捐学费",
     "relation": "supports"
    },
    {
     "key": "E013",
     "paragraph_id": "P022",
     "quote": "开始承担自己的表达责任。",
     "relation": "supports"
    },
    {
     "key": "E014",
     "paragraph_id": "P023",
     "quote": "别人没听懂、别人听错了、别人听不进去，就是你失败了",
     "relation": "supports"
    },
    {
     "key": "E015",
     "paragraph_id": "P024",
     "quote": "这要看具体这件事值不值得投入这个成本。",
     "relation": "qualifies"
    },
    {
     "key": "E016",
     "paragraph_id": "P025",
     "quote": "只有建立起这个原则，你才会去关心问题出在哪里",
     "relation": "supports"
    },
    {
     "key": "E017",
     "paragraph_id": "P027",
     "quote": "但是你仍然应该获得这些思考结果。",
     "relation": "supports"
    },
    {
     "key": "E018",
     "paragraph_id": "P028",
     "quote": "拥有更强的表达能力，你才能有最大的听众基础",
     "relation": "supports"
    },
    {
     "key": "E019",
     "paragraph_id": "P029",
     "quote": "然后才能有底气去判定表达的分寸，开始往回收",
     "relation": "supports"
    },
    {
     "key": "E020",
     "paragraph_id": "P030",
     "quote": "对大众表达就需要浅显、需要篇幅长",
     "relation": "supports"
    },
    {
     "key": "E021",
     "paragraph_id": "P031",
     "quote": "这种简练，就是效率，是利润。",
     "relation": "supports"
    },
    {
     "key": "E022",
     "paragraph_id": "P032",
     "quote": "是靠更高的“无误压缩算法”来完成的",
     "relation": "supports"
    },
    {
     "key": "E023",
     "paragraph_id": "P033",
     "quote": "关系到你的这条命最后到底价值几何、有多少份量。",
     "relation": "supports"
    },
    {
     "key": "E024",
     "paragraph_id": "P034",
     "quote": "直接决定你一生赚取利润的上限。",
     "relation": "supports"
    },
    {
     "key": "E025",
     "paragraph_id": "P035",
     "quote": "这不妨碍你中彩票，但中彩票不算赚取，谢谢。",
     "relation": "qualifies"
    },
    {
     "key": "E026",
     "paragraph_id": "P039",
     "quote": "先中译英，然后再英译中，这称为一轮“刚度检验”。",
     "relation": "supports"
    },
    {
     "key": "E027",
     "paragraph_id": "P040",
     "quote": "一段文本的表达刚度即一段文本在刚度检验中保持自身不变的性能。",
     "relation": "supports"
    },
    {
     "key": "E028",
     "paragraph_id": "P041",
     "quote": "经过一轮变换后已经不可理解，甚至时态、人称混乱，则其表达刚度为不合格。",
     "relation": "supports"
    },
    {
     "key": "E029",
     "paragraph_id": "P043",
     "quote": "语义无需猜测补足就与原文等效，则可称为表达刚度优秀。",
     "relation": "supports"
    },
    {
     "key": "E030",
     "paragraph_id": "P044",
     "quote": "那么可以称为表达刚度完美",
     "relation": "supports"
    },
    {
     "key": "E031",
     "paragraph_id": "P045",
     "quote": "即你自己创造的专有术语可以替换成专用缩写。",
     "relation": "supports"
    },
    {
     "key": "E032",
     "paragraph_id": "P046",
     "quote": "把上面这条拿来测一测，看看能得多少分？",
     "relation": "context"
    },
    {
     "key": "E033",
     "paragraph_id": "P047",
     "quote": "把你的语文学习的目标直接设定为“能近乎本能的写出刚度良好以上的句子”",
     "relation": "supports"
    },
    {
     "key": "E034",
     "paragraph_id": "P049",
     "quote": "放眼知乎3.5亿用户，能第一稿就做到刚度良好的，百中无一。",
     "relation": "supports"
    },
    {
     "key": "E035",
     "paragraph_id": "P050",
     "quote": "能以正常打字速度第一次成稿就做到这一点的，千中无一。",
     "relation": "supports"
    },
    {
     "key": "E036",
     "paragraph_id": "P051",
     "quote": "能倚马可待，一挥而就，径直就做到完美刚度的，万中无一。",
     "relation": "supports"
    },
    {
     "key": "E037",
     "paragraph_id": "P053",
     "quote": "从商可望巨擘、用学可望泰斗、从艺可望宗师。",
     "relation": "supports"
    },
    {
     "key": "E038",
     "paragraph_id": "P055",
     "quote": "你基本上可以和真正的权力和地位说再见了。",
     "relation": "supports"
    },
    {
     "key": "E039",
     "paragraph_id": "P056",
     "quote": "你只是个读稿器、盖章机加替罪羊而已。",
     "relation": "supports"
    },
    {
     "key": "E040",
     "paragraph_id": "P057",
     "quote": "要掌握健康的语法结构，学会写高健康度的句子。",
     "relation": "supports"
    },
    {
     "key": "E041",
     "paragraph_id": "P058",
     "quote": "所谓的健康，就是指有很强的抗歧义、抗干扰的性能。",
     "relation": "supports"
    },
    {
     "key": "E042",
     "paragraph_id": "P060",
     "quote": "不随便省略句子成分，降低对上下文的依赖程度。",
     "relation": "supports"
    },
    {
     "key": "E043",
     "paragraph_id": "P061",
     "quote": "设计讲究“高内聚、低耦合”",
     "relation": "supports"
    },
    {
     "key": "E044",
     "paragraph_id": "P063",
     "quote": "“吃了吗？”里的主语就严重的依赖于这句话所处的上下文。",
     "relation": "supports"
    },
    {
     "key": "E045",
     "paragraph_id": "P065",
     "quote": "但是长和费暂时不是致命问题，歧义和误解是致命问题。",
     "relation": "supports"
    },
    {
     "key": "E046",
     "paragraph_id": "P066",
     "quote": "这里要格外注意一个问题——要警惕和有意避免使用网络流行语。",
     "relation": "supports"
    },
    {
     "key": "E047",
     "paragraph_id": "P068",
     "quote": "除非你已经功力深厚、八风不动，否则不要用这些东西，更加不要大量的用。",
     "relation": "qualifies"
    },
    {
     "key": "E048",
     "paragraph_id": "P069",
     "quote": "那只是体现出一种可悲的求认同的软弱",
     "relation": "supports"
    },
    {
     "key": "E049",
     "paragraph_id": "P070",
     "quote": "你需要的是被人严肃地对待，而不是被人“喜欢”。",
     "relation": "supports"
    },
    {
     "key": "E050",
     "paragraph_id": "P071",
     "quote": "让整个句子、段落保持鲜明一致的调性。",
     "relation": "supports"
    },
    {
     "key": "E051",
     "paragraph_id": "P074",
     "quote": "在用多处句子成分的反复呼应来复合性的强调着时态、身份、单复数",
     "relation": "supports"
    },
    {
     "key": "E052",
     "paragraph_id": "P075",
     "quote": "这就形成了一种反误解、反歧义的系统策略。",
     "relation": "supports"
    },
    {
     "key": "E053",
     "paragraph_id": "P077",
     "quote": "靠着其他多重保险的补救也往往能在很大程度上维持句子的原意。",
     "relation": "supports"
    },
    {
     "key": "E054",
     "paragraph_id": "P078",
     "quote": "日语里使用敬语也有类似的设计",
     "relation": "supports"
    },
    {
     "key": "E055",
     "paragraph_id": "P079",
     "quote": "你要学会写分明的句子，把你的意图从句子的每一个成分上都呼应着表示出来",
     "relation": "supports"
    },
    {
     "key": "E056",
     "paragraph_id": "P080",
     "quote": "正确使用标点符号。",
     "relation": "supports"
    },
    {
     "key": "E057",
     "paragraph_id": "P082",
     "quote": "冒号、引号、顿号、分号、括号、破折号这些表达逻辑关联的符号，要加倍的在意。",
     "relation": "supports"
    },
    {
     "key": "E058",
     "paragraph_id": "P084",
     "quote": "你将很难准确、简洁的表达比较复杂的概念。",
     "relation": "supports"
    },
    {
     "key": "E059",
     "paragraph_id": "P086",
     "quote": "是用“之乎者也矣焉哉”和“骈四俪六”这些更复杂严苛的手段来实现了这个功能",
     "relation": "supports"
    },
    {
     "key": "E060",
     "paragraph_id": "P087",
     "quote": "叙述论证要有章法和基本规划。",
     "relation": "supports"
    },
    {
     "key": "E061",
     "paragraph_id": "P088",
     "quote": "罗列事务时的单一事务结构为简述、定义问题，解释问题，提出决策的关键点，提出方案",
     "relation": "supports"
    },
    {
     "key": "E062",
     "paragraph_id": "P091",
     "quote": "能把这些东西写得辞能达意、没有自相矛盾、没有丢三落四的人之少，堪称我国语文教育之耻辱。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "语文教育",
    "语言表达与写作",
    "沟通成本",
    "个人能力与职业发展"
   ],
   "issue_candidates": [
    "语文能力的定义与衡量",
    "表达责任的归属",
    "清晰表达与效率的权衡",
    "网络流行语对表达的影响",
    "逻辑标点的使用"
   ],
   "text_function_candidates": [
    "方法论指南",
    "训诫/劝学",
    "概念定义与自造术语",
    "语文教育批评"
   ],
   "object_candidates": [
    "现代语文",
    "表达刚度检验",
    "谷歌翻译",
    "标点符号",
    "网络流行语",
    "知乎用户规模"
   ],
   "working_keywords": [
    "学好语文",
    "表达刚度",
    "刚度检验",
    "表达责任",
    "沟通成本",
    "抗歧义",
    "高内聚低耦合",
    "半兽人"
   ]
  },
  "notes": "正文 91 段已全文读完；无图片节点，status=read。提问者问题仅作语境，未归给作者。brief 在阅读包中被截断（止于“打下沟”），未作为主张依据。文中含自造术语与量化比例，均按作者说法登记并列入 unresolved_questions。"
 },
 "62737881": {
  "analysis": {
   "question_context": "知乎提问“天生优越感，经常瞧不起别人怎么办？”（Q001，属提问者）之下的答主回答：提问者把自己描述为有天生优越感并因此困扰，属提问者自述，本文不将其归给作者。作者不回答“怎么改掉优越感”的操作步骤，而是重新解释优越感的来源与归属：它来自人天生的“上帝自觉”和审判者位置，不属于个人。brief 只是正文导航（并指向正文首段），未提供额外语境。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "立论前提：人天生有“上帝自觉”，可轻易把自己代入上帝的视角看问题；思考本身就是神的能力，人在计算、审判、创造时虽难自觉，心灵上实际已化身为神（超级减配版）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "举出被审判者的市井回呛“你以为你是玉皇大帝啊？！”作为话证据。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "以上帝心态审视任何人类必看到无数缺点、必产生无可置疑的优越感，这是客观事实、自然现象，如芯片发热、风扇生风、线圈生磁，本身中性。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "关键结论：优越感绑定在上帝的神格上，不是绑在自己身上；以警察穿警服、配警官证立刻勇气倍增、权能陡生却不因此变成武打明星作类比。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "审视别人优劣即坐上上帝的位置做审判，极易感受优越感（如老师改卷看个个一身毛病）；一旦离开席位坐进考场，自己也同样是那个鸟样；两个角色的落差使自我认知发生矛盾。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "于是自我分裂，分不清自己是办公室里嘴角挑着冷笑的考官，还是考场上汗出如浆的废柴；两问并答“当然不行”，判定两者不能同时存在。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "结论：那份冷笑权属于上帝，你仍是废柴；那个位置因怜悯你生存不易而说好可随时借坐，坐上就得意非常，但动力绑在座位上——“是宝剑在嘟，不是你在嘟”。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P020"], "summary": "以反问收束，要求读者自查优越感的问题是否已被解释清楚。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人天生有“上帝自觉”，意思是人可以轻而易举地把自己代入上帝的视角来看待问题。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "思考本身就是神的能力；人在计算、审判、创造的时候，尽管很难明确意识到，实际上已在心灵上化身为神（一个超级减配版）。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "被以上帝视角审判的人会回呛“你以为你是玉皇大帝啊？！”——作者引用此语作为审判者被视为自居上帝的语言证据，未注明出处。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以上帝的心态审视任何人类，都会自然而然地看到无数缺点、自然而然地产生无可置疑的优越感；这只是一种客观事实、一种自然现象，本身是中性的。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关键在于要意识到那份优越感是绑定在上帝的神格上的，而不是绑定在自己身上。", "evidence": ["E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当人去审视别人的优劣时，就是在审判、坐上了上帝的位置、在做上帝的事，因此非常容易感受到优越感（如老师改同学卷子时看个个一身毛病）。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一旦离开审判席位、坐进考场，自己也是同样的糟糕（作者原话为“你也是这个鸟样”）。", "evidence": ["E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两个角色转换的落差使自我认知发生矛盾，人会分不清自己究竟是办公室里挑着冷笑的考官，还是考场上汗出如浆的废柴。", "evidence": ["E011", "E012"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "考官式的优越与考场上的无能不能同时成立：作者以反问提出并答“当然不行”，否认两者可以并存于同一人。", "evidence": ["E013", "E014"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那份冷笑权属于上帝，不属于读者本人；读者仍然是那个废柴。", "evidence": ["E015", "E016"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "那个位置因怜悯人生存不易、离开它将失去基本生存能力，已经说好可以随时借坐；坐上去就会得意非常，但这份动力是绑在座位上的，不是绑在人身上。", "evidence": ["E017"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论性比喻：是宝剑在嘟，不是你在嘟。", "evidence": ["E018"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以“现在你的优越病治好了吗？”反问读者，暗示本文的解释即是解决之道，但并未直接断言其已足够。", "evidence": ["E019"]}
   ],
   "argument_steps": [
    "提出前提：人天生有“上帝自觉”，可以轻易代入上帝的视角看问题。",
    "加一层论证：思考本身就是神的能力，人在计算、审判、创造时心灵上已化身为神（超级减配版），只是难以自觉。",
    "引入被审判者的回呛“你以为你是玉皇大帝啊？！”作为审判者自居上帝的旁证。",
    "推演必然结果：以上帝心态审视人类必然看到无数缺点、必然产生优越感，并类比芯片发热、风扇生风、线圈生磁，判定其本身中性。",
    "给出诊断：问题在于把绑定在上帝神格上的优越感误认为绑定在自己身上；以警察穿警服、配警官证作类比。",
    "铺陈心理机制：审视他人即坐上审判席，故优越感易生（老师改卷）；离开席位回考场则同样狼狈。",
    "指出后果：角色落差造成自我认知矛盾与分裂，分不清自己是考官还是废柴；并以二人不能同存作结。",
    "给出归属结论：冷笑权属于上帝，你仍是废柴；那个位置只是因怜悯而可随时借坐，动力绑在座位上。",
    "以“是宝剑在嘟，不是你在嘟”作比喻式收束，并用反问“现在你的优越病治好了吗？”要求读者自查。"
   ],
   "concept_usage": [
    {"term": "上帝自觉", "meaning": "人天生具有的、可以轻而易举把自己代入上帝视角来看待问题的能力。", "evidence": "P001", "ambiguity": "是比喻性说法还是严格命题，文中未界定。"},
    {"term": "上帝的神格", "meaning": "与审判者位置相连的身份属性；作者的诊断是优越感绑定于此，而不是绑定在个人身上。", "evidence": "P007", "ambiguity": "与“位置”“席位”“座位”“宝剑”等比喻混用，均指同一外部身份，但未作统一说明。"},
    {"term": "位置／席位／座位", "meaning": "审判者（如考官）所处的位置，可以借坐、也可以离开；离开后将失去基本生存能力。", "evidence": "P009", "ambiguity": "三种说法交替出现，未说明是否完全同指一物。"},
    {"term": "优越感／优越病", "meaning": "以上帝视角审视人类时必然产生的心理产物，作者判定本来是中性的；只有当它被误认为属于自己时才成为需要治的“病”。", "evidence": "P005", "ambiguity": "中性优越感与“优越病”的分界线未明确划出。"},
    {"term": "废柴", "meaning": "离开审判席位后、在考场上汗出如浆的自己。", "evidence": "P013", "ambiguity": "口语化贬称，属修辞还是作者的严格自我定位，未加限定。"},
    {"term": "是宝剑在嘟", "meaning": "比喻权能来自所持之物（位置）而非人本身，与“动力绑在座位上”同义。", "evidence": "P019", "ambiguity": "“嘟”字用字异常（疑为拟声或别字），具体所指需核原文或版本。"}
   ],
   "examples_and_targets": [
    "被审判者的回呛“你以为你是玉皇大帝啊？！”——引用的市井口语，作为审判者被视为自居上帝的话证据，出处未注明（P003、P004）。",
    "芯片运算发热、风扇旋转导致气流、线圈通电产生磁场——类比，说明优越感的产生属中性自然现象（P006）。",
    "警察穿警服、配警官证即勇气倍增、权能陡生——类比，说明勇气与权能属于职位而非本人（P008）。",
    "老师改同学卷子、一看个个一身毛病——举例/类比，说明坐上审判席时优越感易生（P009）。",
    "考场中做不出卷子的人（汗出如浆的废柴）——举例，与考官角色构成对照（P010、P013）。",
    "办公室里嘴角挑着冷笑的考官——举例/形象化角色，与考场上的废柴并置（P013）。",
    "宝剑——“是宝剑在嘟，不是你在嘟”——比喻，说明权能绑在座位或器物上（P019）。"
   ],
   "conditions": [
    "“优越感中性”的判断限定在“以上帝的心态审视任何人类”这一特定视角下，作者随后才区分它绑定在何处（P005、P007）。",
    "对提问者的隐含处置前提是：问题出在把优越感误绑在自己身上，而不是优越感本身（P007）。",
    "座位可以随时借坐有前提：怜悯你生存不易、离开这个位置将失去基本生存能力（P018）。",
    "作者判定两个角色不能同时存在，以反问加“当然不行”给出，未给论证（P014、P015）。",
    "全文以第二人称设定读者就是那个既有优越感、又会在考场上做不出题的人（P010、P020）。"
   ],
   "rhetoric_and_tone": "通篇第二人称“你”的训诫兼调侃体：短句、断言与反问连用（“难道两者可以同时存在吗？”“明白了吗？”“现在你的优越病治好了吗？”）。用一串类比把抽象心理问题具象化（芯片发热、风扇生风、线圈生磁、警察穿警服、老师改卷、宝剑自鸣），并夹用口语与戏谑贬称（废柴、你老人家、牛得飞起、这个鸟样）以削弱说教的距离感；又引用一句市井回呛作话证据。结构上是“立前提—作类比—下诊断—给归属—反问收束”，结尾不提供操作步骤，而是让读者自省。",
   "unresolved_questions": [
    "提问者问的是“天生优越感，经常瞧不起别人怎么办”，正文重在解释优越感的来源与归属，未给出具体的行动步骤或练习方法，仅在结尾以反问暗示。",
    "“上帝自觉”“上帝的神格”是比喻还是严格命题，文中未界定；其与任何宗教教义的关系也未说明。",
    "作者是否主张一切优越感都只是位置效应、个人才能与努力完全不产生优越感，文中未作细分。",
    "“是宝剑在嘟”一句用字异常（嘟），具体所指（剑鸣？）需核原文或版本差异。",
    "P018 中“那个位置已经说好了可以随时借你坐”的“说好了”是与谁约定的，主体不明。",
    "阅读包中 brief 在“却突遭审判的人怎么”处被截断，未作为作者主张依据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "人天生有“上帝自觉”——意思是人可以轻而易举的将自己代入上帝的视角来看待问题。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "思考本身就是神的能力。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P002", "quote": "但你在那个时候实际上在心灵上已经化身为神了（虽然是个超级减配版）", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "“你以为你是玉皇大帝啊？！”", "relation": "context"},
    {"key": "E005", "paragraph_id": "P005", "quote": "以上帝的心态审视任何人类，都自然而然的能看到无数的缺点，自然而然的会无可置疑的优越感，这只是一种客观事实、一种自然现象。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P006", "quote": "就和芯片运算会发热，风扇旋转会导致气流，线圈里通电会产生磁场一样，这本身是中性的。", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "你的问题是要意识到那个优越感是绑定在上帝的神格上的，不是绑定在你自己身上的。", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "这就像一名警察把警服一穿、警官证一配，立刻勇气倍增，权能陡生，但是警察们并不因此就变成武打明星、功夫小子一样。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "当你去审视别人优劣的时候，你是在审判，你坐上了上帝的位置、在做上帝的事，你非常容易感受到优越感", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P010", "quote": "而你一旦离开了这个席位，坐进考场里，你也是这个鸟样。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P011", "quote": "这两个角色转换的落差，让你对自己的认知发生了矛盾。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P013", "quote": "你分不清哪个是你了，你到底是那个坐在办公室里嘴角挑着冷笑的考官，还是那个坐在考场上汗出如浆的废柴？", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "难道两者可以同时存在吗？你可以同时是两者吗？", "relation": "context"},
    {"key": "E014", "paragraph_id": "P015", "quote": "当然不行。", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P016", "quote": "告诉你了——那份冷笑权是属于上帝的。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P017", "quote": "你老人家还是那个废柴。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P018", "quote": "你坐上就会牛得飞起，遗憾的是，这份能让牛都飞到云端去的动力是绑在座位上的。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P019", "quote": "是宝剑在嘟，不是你在嘟，明白了吗？", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P020", "quote": "现在你的优越病治好了吗？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与自我认知", "道德哲学与宗教隐喻", "人际态度"],
   "issue_candidates": ["优越感的来源与归属", "自我认知的分裂", "把位置赋予的权能误认为个人能力", "如何对待瞧不起别人的心态"],
   "text_function_candidates": ["解释性回答", "类比论证", "训诫/调侃", "反问收束"],
   "object_candidates": ["上帝视角", "优越感", "审判者位置（考官席位）", "警察与警官证", "考场与考卷", "宝剑"],
   "working_keywords": ["上帝自觉", "神格", "优越感", "审判", "废柴", "借坐", "宝剑在嘟"]
  },
  "notes": "正文 20 段已全文读完；无图片节点，status=read。提问者自述的天生优越感仅作语境，未归给作者。brief 在阅读包中被截断（止于“人怎么”），未作为主张依据。提问者索要的应对办法在正文中没有给出具体步骤，已列入 unresolved_questions。"
 },
 "60ac2755": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "知乎提问“相对于中国的价格，美国超市的肉和奶较便宜，而蔬菜水果却较贵，为什么？”（Q001，属提问者，只是提问不含自身立场）之下的答主回答。作者开篇即声明这是自己的猜测（与人口集中度和美国人饮食习惯有关），并欢迎了解具体情况者修正，故全篇结论都带此自述保留；brief 仅摘录正文首段及第三段开头，未提供额外语境。本篇含 4 张图片，本执行者无读图能力。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "作者声明自己的解释是猜测：与美国的人口集中度和美国人的饮食习惯有关，欢迎了解具体情况的人修正。", "role": "qualification"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "中美蔬菜流通形态对比：美国肉类和蔬菜大部分被纳入大型零售集团的分发渠道、蔬菜以净菜甚至半加工形式出售；中国蔬菜采摘后只有为短途运输准备的简单捆扎加工，短途送到产地附近的地级市镇集市销售。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "中国农业生产者基本为100公里以内、甚至50公里范围内的消费者生产，因为该范围内消费者规模常达数百万甚至上千万人。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "用图展示美国农业生产者面对的稀疏聚居画面（作者自注比例尺不同，若用同一比例尺画面里只会有一两个聚居点），并称两图纬度基本相当。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "美国蔬菜的运输链条：先到十几公里外的初级加工中心，再跨数百公里到大型分装中心，再跨平均数百公里到各地区大型超市，居民往往还需自驾前往；运输里程比中国高出一个数量级；又因集中度高，只供最近市镇大概率无法生存，至少要对附近三到四个州供货，里程还要再提高。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012"], "summary": "成本结构比较：美国燃料与过路费显著较低、用人少，但中国农业运输人力单位成本很低（常是本村菜贩子开农用车拖到集散点，收入不及美国卡车司机十分之一），中国高昂过路费又因短途多走不收费的国道省道而被回避，故人力成本相差不大；美国的长途燃油、规费优势不足以挽回大一个数量级的运输距离劣势。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P013", "P014"], "summary": "因运输距离长，美国农业生产者更希望上路产品尽可能去掉多余重量以省运费，由此带来食品初级及次级加工成本（胡萝卜、土豆被削成可直接销售的条块规格、做好批发包装才上路）。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P015"], "summary": "美国消费者时间成本贵、基本没有厨艺，愿意多花钱省工夫；美国生产商体量大可支撑更大投资，故把食品加工到直接下锅甚至装盘级别是显而易见的嘴边肥肉，美国货架蔬菜比中国多一环加工成本。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P016", "P017"], "summary": "价格比较的口径问题：美国价格含洗净切碎成本而刨除了顾客自己加工的时间成本，中国价格省掉自己的加工成本却未计顾客洗切的时间成本；这块机会成本很大，作者认为这对美国一方不太公平。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "品相要求与损耗：既已自行加工上架，品相要求很高，稍大、小、歪、不新鲜的都不值得投入加工与展示资源，因为面对90%更漂亮的同类将永不被选择而致成本沉没并产生垃圾处理成本；次品只会反衬同类并暗示顾客自选，降低单位展示面积效率并伤害品牌；故美国销售高度强调一致性，等于告诉消费者别挑了、快点买单（P022 为配图说明：用本该丢弃的次品胡萝卜加工成 baby carrot，损耗巨大的加工反而是一种节约措施）。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P023", "P024", "P025"], "summary": "超高的外观一致性并不见得有利于口感、味道和营养；作者以商家口吻表示味道问题由消费者自己用调味料解决，食材方面没有必要解决。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P026", "P027"], "summary": "因品相问题被抛弃的比例大很多，也是一块额外成本；故美国蔬菜水果比中国同类多出运输成本、加工成本和损耗，单价自然会高一些。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P028"], "summary": "肉类方面：中国大规模肉类生产销售与美国现在形式上已颇接近，美国更高的肉类生产技术水平和全员肉食带来的行业规模效应使其肉类显著比中国便宜。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P029", "P030", "P031"], "summary": "蔬菜在中国单位价格很低，同样绝对值的成本增加在涨幅比例上非常惊人（2块钱涨1块即贵50%，30块涨1块几乎被视为统计误差），这也更强烈地影响了结论的显著感。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者自述其解释只是猜测：与美国的人口集中度和美国人的饮食习惯有关，并欢迎了解具体情况的人修正。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国的肉类和蔬菜大部分被纳入大型零售集团的分发渠道来销售，蔬菜以净菜甚至半加工形式出售为主。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国蔬菜采摘后只有极其简单的、为短途运输准备的捆扎加工，经短途运输送到产地附近的地级市镇集市销售。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国农业生产者基本为100公里以内、甚至50公里范围内的消费者生产，因为该范围之内的消费者规模常已达数百万甚至上千万人。", "evidence": ["E004", "E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国一斤蔬菜要送到餐桌，需先到十几公里外的初级加工中心，再跨数百公里到大型分装中心，再跨平均数百公里到各地区大型超市，居民往往还需自己开车前往购买。", "evidence": ["E006", "E007", "E008"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "美国蔬菜产品的运输里程数与中国农产品不能相提并论，粗略估计高出一个数量级。", "evidence": ["E009"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "因集中度甚高，在美国只对最近市镇供货大概率生存不下去（太不经济）；至少要对附近三到四个州甚至更大范围的买家供货才能支撑如此大规模的投资，运输里程还要进一步提高。", "evidence": ["E010", "E011", "E012"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国运输燃料费用和过路费用显著较低、用人量较少，但中国农业运输人力单位成本很低（常是农民本村的菜贩子开农用车拖到集散点，工资收入不及美国卡车司机十分之一），中国高昂的过路费又因短途多走不收费的国道省道而被回避，因此在人力成本上相差不大。", "evidence": ["E013", "E014", "E015"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "美国在长途运输上的燃油、规费优势应该并不足以挽回由大一个数量级的运输距离所带来的劣势。", "evidence": ["E016"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因运输距离长，美国农业生产者会更希望被发送上路的产品尽可能去掉多余重量以节省运输成本，这带来食品初级及次级加工成本（胡萝卜、土豆被削成能直接销售的条块规格、做好批发包装才上路）。", "evidence": ["E017", "E018"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国消费者时间成本很贵、基本没有厨艺，绝对愿意多花钱省下工夫；美国生产商体量大可支撑大得多的投资，故把食品加工到直接下锅甚至装盘的食材级别是显而易见的嘴边肥肉，美国架上蔬菜瓜果因此比中国多一环加工成本。", "evidence": ["E019", "E020"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对比中美蔬菜价格时，美国价格含洗净切碎这部分成本而刨除顾客自己加工的时间成本，中国价格省掉了自己的加工成本却没有计算顾客洗切加工的时间成本；这块机会成本非常大，作者认为这在比赛中对美国一方不太公平。", "evidence": ["E021", "E022"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然已经自己加工上架，食品的品相要求就非常高：稍大、小、歪、不够新鲜的都不值得投入更多的加工和展示资源，因为面对90%更为漂亮的同类将永远不被消费者选择，相关成本全部沉没并还要发生垃圾处理成本。", "evidence": ["E023", "E024"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "次品实际担当的作用只是反衬其他同类有多好，并暗示顾客购买前需自己注意挑选，这降低了单位展示面积的时间效率，更不用提会伤害品牌。", "evidence": ["E025"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国蔬菜瓜果销售高度注意产品的一致性，其效果是在告诉消费者别挑了、都一模一样、装进购物车快点买单。", "evidence": ["E026"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "超高的外观一致性要求并不见得总是有利于食品的口感、味道和营养；行业立场是把味道问题交给消费者自己用调味料解决，食材方面没必要解决。", "evidence": ["E027", "E028"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国蔬菜瓜果因为品相问题被抛弃的比例比中国大很多，这也是一块额外成本。", "evidence": ["E029"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因此，美国的蔬菜瓜果比起中国同类多出了运输成本、加工成本和损耗，单价自然会高一些。", "evidence": ["E030"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "肉类方面，中国的大规模肉类生产销售与美国现在形式上已颇为接近；美国全线更高超的肉类生产技术水平以及全员肉食带来的行业规模效应，使其肉类显著比中国便宜。", "evidence": ["E031"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "蔬菜在中国的单位价格很低，意味着同样绝对值的成本增加在涨幅比例上看非常惊人；这也更强烈地影响了结论的显著感。", "evidence": ["E032", "E033", "E034"]}
   ],
   "argument_steps": [
    "先自限：声明这是猜测，与人的人口集中度和美国人饮食习惯有关，欢迎了解情况者修正。",
    "对比两国流通形态：美国蔬菜经大型零售集团分发、以净菜或半加工出售；中国蔬菜只作简单捆扎加工、短途送到产地附近集市。",
    "给出中国侧的条件：生产者基本为100公里甚至50公里内的消费者生产，该范围内消费者规模已达数百万至千万。",
    "以两张地图示意美国聚居点稀疏（作者自注比例尺不同、纬度基本相当），作为密度差异的图示证据。",
    "拆解美国蔬菜的运输链条与里程：初级加工中心→大型分装中心→各地区大型超市→居民自驾，粗略估计里程高出一个数量级。",
    "补充规模约束：只供最近市镇大概率无法生存，至少覆盖三到四个州，里程还要再提高。",
    "比较运输成本结构：美国燃油、规费低但距离远；中国人力成本极低且短途避开了高过路费，故人力成本相近，美国的燃油规费优势不足以抵消距离劣势。",
    "推出加工成本：为省运费而去掉多余重量，于是产生初级与次级加工（削成条块、批发包装才上路）。",
    "推出需求侧原因：美国消费者时间贵、少厨艺，生产商体量大，故把食品加工到可直接下锅装盘是必然选择，价格中因此多一环加工成本。",
    "指出比较口径问题：美国价格含洗切成本而不含顾客时间成本，中国价格反之；这块机会成本很大。",
    "推出品相与损耗：自家加工上架使品相要求极高，次品永不被选择、成本沉没并产生垃圾处理费，还降低展示效率、伤害品牌；故销售强调一致性。",
    "指出一致性不等于品质：外观一致并不见得有利于口感、味道和营养，味道问题被推给消费者。",
    "小结蔬菜侧：运输、加工、损耗三项叠加，使美国蔬菜单价高于中国同类。",
    "解释肉类侧：中国肉类产销形式已接近美国，美国凭技术水平和全员肉食的规模效应胜出，故肉类显著更便宜。",
    "补充观感因素：中国蔬菜单价低，等额成本增加在涨幅比例上被放大，强化了结论的显著感。"
   ],
   "concept_usage": [
    {"term": "人口集中度", "meaning": "作者猜测中的解释变量：美国聚居点稀疏，而中国的消费者在数十至百公里范围内高度聚集。", "evidence": "P001", "ambiguity": "未给出任何数据，仅以两张地图示意，且比例尺不一致。"},
    {"term": "净菜／半加工", "meaning": "蔬菜在销售前已完成清洗、切分等处理的形式。", "evidence": "P002", "ambiguity": "与 P014 所说的“初级及次级加工”边界未严格区分。"},
    {"term": "集散点", "meaning": "中国菜贩子用农用车把菜拖到的汇集地点（运输链条的中转端）。", "evidence": "P011", "ambiguity": "具体形态（批发市场还是收购点）未说明。"},
    {"term": "机会成本", "meaning": "顾客自己洗切加工所耗时间的价值；作者指出中国价格中没有计算这块成本。", "evidence": "P017", "ambiguity": "未量化，也未给出任何估算方法。"},
    {"term": "一致性", "meaning": "美国蔬菜瓜果在外观上高度整齐划一，以至于消费者无需挑选。", "evidence": "P021", "ambiguity": "未给出任何判定标准或抽检口径。"},
    {"term": "全员肉食", "meaning": "美国肉类消费普遍，由此带来行业规模效应。", "evidence": "P028", "ambiguity": "未给数据出处，也未与中国的肉类消费水平作量化对比。"},
    {"term": "涨幅比例", "meaning": "同样绝对值的成本增量，在低单价商品上表现为很高的百分比，从而放大观感。", "evidence": "P029", "ambiguity": "属于感知层面的补充说明，未给出统计口径。"}
   ],
   "examples_and_targets": [
    "两张地图（P005、P006 提到的“上图”“下面这种画面”“这两张图”）——证据性图示，用于展示美国聚居点密度低；作者自注比例尺不同、纬度基本相当，本执行者未读图，仅据文字记录。",
    "IMG001-IMG004（阅读包图片节点）——4 张图片；P019 与 P022 两句（“状态完美整齐划一的蔬菜货架”“用本该丢弃的次品胡萝卜加工的baby carot，讽刺的是，这损耗巨大的加工居然是一种节约措施”）疑为其中两张图的配文，但对应关系未核验。",
    "胡萝卜、土豆被削成能直接销售的条块规格——举例，说明运输距离导致的去重量加工。",
    "baby carrot（婴儿胡萝卜）——举例兼反讽材料，作者称“损耗巨大的加工居然是一种节约措施”。",
    "本村菜贩子自己开着农用车拖到集散点、工资收入不及美国卡车司机十分之一——举例，用于中美人力成本比较。",
    "一斤2块钱涨1块钱 vs 1斤30块钱涨1块钱——数字举例，说明涨幅比例的观感差异。",
    "美国卡车司机、大型零售集团、附近三到四个州——设定中的角色与规模，属举例性描述而非可核查数据。"
   ],
   "conditions": [
    "全篇解释以作者首句的自述为条件：这是猜测，且欢迎了解具体情况的朋友修正（P001）。",
    "对美国侧的描述以“大型零售集团分发渠道”“集中度甚高”“生产商体量很大”为前提（P002、P009、P015）。",
    "运输里程“高出一个数量级”明确为粗略估计而非实测（P008）。",
    "中美成本比较假定中国短途运输基本走不收费的国道、省道（P011）。",
    "肉类便宜的解释以“中国的大规模肉类生产销售和美国现在形式上已经颇为接近”为前提（P028）。",
    "结论的显著感被认为受中国蔬菜低单价导致的涨幅比例放大影响（P029-P031）。",
    "P005、P006 的密度论证直接依赖两张地图，作者自注两者比例尺不同，本执行者无法核验图片。"
   ],
   "rhetoric_and_tone": "答问式的分析说明文，先声明是猜测并欢迎修正，随后用成本链条逐项拆解。多用第二人称虚拟场景推进（“在美国如果你开一家农场却只对自己最近的市镇供货”），以量级对比强化论证（大一个数量级、数百公里、三到四个州），并以括号补注自我限定（注意比例尺不一样、这只省掉了部分重量体积的后半段旅程、说实话这在比赛中对美国一方不太公平）。P024-P025 直接代商家口吻说话（没得挑……我们其实没有多大必要解决），带调侃与讽刺；P022 以“讽刺的是”点出反讽。结尾转到涨幅比例的观感差异，语气由论证转为方法性提醒。",
   "unresolved_questions": [
    "本篇含 4 张图片（IMG001-IMG004），本执行者无读图能力，全部图片状态为 pending、image_checked=false，故 status=needs_reread：需图像核验后方可定稿。",
    "P005、P006 的密度论证（比例尺不同、纬度基本相当、若同比例尺画面里只会有一两个聚居点）完全依赖图片内容，纯文本无法确认其是否成立。",
    "P019、P022 两句疑为图片配文，阅读包将其作为 body 段落收录；其与 IMG003/IMG004 的对应关系、以及是否属于正文，均需核验。",
    "“运输里程高出一个数量级”“至少三到四个州”“平均数百公里”均为作者的粗略估计，无数据来源。",
    "“中国农业运输人力单位成本很低”“工资收入尚不及美国卡车司机的十分之一”无出处与年份，需外部核查。",
    "“全员肉食”“行业规模效应”所依据的规模数据未给出。",
    "作者首句自称猜测并欢迎修正，但正文其余部分是否同样按猜测对待，文中未再声明。",
    "P014 括号中关于“从地头到加工中心的距离没有省掉”的表述较为绕，是否存在笔误或文字缺失需核原文版本。",
    "阅读包 brief 在该篇被截断（止于“送到生产地附近的地级市”），未作为主张依据。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "我猜测和人口集中度和美国人的饮食习惯有关系，欢迎了解具体情况的朋友修正。", "relation": "context"},
    {"key": "E002", "paragraph_id": "P002", "quote": "美国的肉类和蔬菜大部分都被纳入大型零售集团的分发渠道来销售，蔬菜是以净菜甚至半加工形式出售为主。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "这不像中国的蔬菜，采摘之后只有极其简单的、为短途运输准备的捆扎加工", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "中国的农业生产者，基本是在为100公里以内——甚至更小至50公里范围内的消费者生产。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P004", "quote": "因为往往在这个范围之内的消费者规模已经多至数百万甚至上千万人了。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P005", "quote": "如果采用和上图相同的比例尺将根本没法展示“密度”", "relation": "context"},
    {"key": "E007", "paragraph_id": "P007", "quote": "首先要送到十几公里外的初级加工中心，然后再跨越数百公里距离送到大型的分装中心", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P007", "quote": "而居民们往往需要再自己开车前往这些大型超市购买。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P008", "quote": "美国蔬菜产品的运输里程数和中国农产品是不能相提并论的，粗略估计要高出一个数量级。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P009", "quote": "在美国如果你开一家农场却只对自己最近的市镇供货你大概率是生存不下去的，因为太不经济。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P009", "quote": "你至少要对附近的三到四个州——甚至更大范围的买家供货才能支撑你如此大规模的投资。", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P010", "quote": "于是运输里程数还要进一步提高。", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P011", "quote": "但中国农业运输人力单位成本很低", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P011", "quote": "ta们的工资收入尚不及美国卡车司机的十分之一", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P011", "quote": "而中国高昂的过路费用，则因为短途运输基本都是走不收费的国道、省道而被回避了。", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P012", "quote": "因此，美国在长途运输上燃油、规费优势应该并不足以挽回由大一个数量级的运输距离所带来的劣势。", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P013", "quote": "美国的农业生产者会更加希望被发送上路的产品本身尽可能的去掉多余的重量，以节省运输成本。", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P014", "quote": "胡萝卜、土豆等直接被削成能直接销售的条块规格，做好批发包装才送上路", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P015", "quote": "美国消费者的时间成本很贵——更不用提基本没有厨艺可言——ta们是绝对愿意多花一点钱而省下自己的工夫的。", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P015", "quote": "因此对ta们而言，把食品加工到直接下锅甚至装盘的食材级别这一环节是显而易见的嘴边肥肉。", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P016", "quote": "美国的价格里含了洗净切碎这部分成本而刨除了顾客自己加工的时间成本", "relation": "qualifies"},
    {"key": "E022", "paragraph_id": "P017", "quote": "这菜由生产线来洗和切，比起你自己亲自洗切的成本可是要低不少。", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P018", "quote": "稍微大点、小点、歪点、不够新鲜的，都不值得投入更多的加工和展示资源", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P018", "quote": "因为在90%都更为漂亮的同类面前，它们将永远不被消费者选择而导致所有相关成本都将沉没", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P020", "quote": "这些次品实际担当的作用只会是用来反衬其他同类有多好，以及暗示顾客购买前需要自己注意挑选", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P021", "quote": "这是在告诉消费者——别挑了，都一模一样，装进购物车里快点买单拉倒。", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P023", "quote": "这种超高的外观上一致性要求并不见得总是有利于食品的口感、味道和营养。", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P025", "quote": "味道不好的问题，你自己想办法拿调味料解决去", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P026", "quote": "而这导致了美国蔬菜瓜果因为品相问题被抛弃的比例大很多，这也是一块额外成本。", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P027", "quote": "美国的蔬菜瓜果里比起中国同类，多出了运输成本、加工成本和损耗，单价自然会高一些。", "relation": "supports"},
    {"key": "E031", "paragraph_id": "P028", "quote": "美国全线更为高超的肉类生产技术水平，以及因为全员肉食所带来的行业规模效应，自然比较轻松地胜过了中国同行。", "relation": "supports"},
    {"key": "E032", "paragraph_id": "P029", "quote": "另外，蔬菜在中国的单位价格很低，意味着同样绝对值的成本增加，在“涨幅比例”上看就非常惊人。", "relation": "qualifies"},
    {"key": "E033", "paragraph_id": "P030", "quote": "一斤2块钱的东西涨1块钱，就是贵了50%，而1斤30块钱的东西涨1块钱，几乎只被视为统计误差。", "relation": "supports"},
    {"key": "E034", "paragraph_id": "P031", "quote": "这也更加强烈地影响了这个结论的显著感。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中美物价比较", "农产品流通与供应链", "零售与食品加工", "运输成本"],
   "issue_candidates": ["美国蔬菜水果相对中国更贵的原因", "人口集中度与运输距离", "净菜/半加工带来的成本转移", "品相一致性与食品损耗", "价格比较口径是否计入消费者时间成本"],
   "text_function_candidates": ["答问式原因分析", "成本拆解与供应链推演", "自述为猜测的保留性论证"],
   "object_candidates": ["美国超市蔬菜瓜果", "肉类和奶", "大型零售集团", "初级加工中心与分装中心", "baby carrot", "国道省道过路费", "人口密度地图"],
   "working_keywords": ["人口集中度", "运输里程", "净菜", "半加工", "机会成本", "品相一致性", "损耗", "规模效应", "涨幅比例"]
  },
  "notes": "含 4 张图片（IMG001-IMG004），本执行者无读图能力：全部图片 status=pending、image_checked=false，故本篇 status=needs_reread，需图像核验后再定稿，重点是两张人口密度地图与 P019、P022 两处疑似配文。文字部分（31 段）已全文读完。作者首句自称猜测，全篇结论据此带保留。brief 在阅读包中被截断（止于“送到生产地附近的地级市”），未作为主张依据。"
 },
 "fc4c2513": {
  "analysis": {
   "question_context": "知乎提问“为什么现在的歌手吐字不准？”（Q001，属提问者；提问本身含“现在的歌手吐字不准”这一预设，属提问者说法）之下的答主回答。作者不讨论发声、录音或咬字技术，也不复述提问者的预设，而是以五句格言式短句从“个性”“正确/共识”与艺术使命的角度给出解释。brief 与正文完全一致，未提供额外语境。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接给出原因：个性大部分是被错误定义的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "给出前提：共性和“正确”天然联姻；错误是丰富活泼的，正确是单调无聊的。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "推到艺术层面：艺术的使命就是反“共识”，在于找到“明明说来是错的，但是你知道它其实是对的”的东西；看起来很失败是先锋艺术的常态。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "（歌手吐字不准）因为个性大部分是被错误定义的。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "共性和“正确”天然联姻。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "错误是丰富活泼的，正确是单调无聊的。", "evidence": ["E003"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术的使命就是反“共识”，在于找到“明明说来是错的，但是你知道它其实是对的”的东西。", "evidence": ["E004"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "看起来很失败是先锋艺术的常态。", "evidence": ["E005"]}
   ],
   "argument_steps": [
    "先直接给出原因：个性大部分是被错误定义的。",
    "给出第一条前提：共性和“正确”天然联姻。",
    "给出第二条前提：错误是丰富活泼的，正确是单调无聊的。",
    "推出艺术层面的判断：艺术的使命就是反“共识”，在于找到“明明说来是错的，但是你知道它其实是对的”的东西。",
    "以“看起来很失败是先锋艺术的常态”收尾，把失败的外观纳入先锋艺术的常态。"
   ],
   "concept_usage": [
    {"term": "个性", "meaning": "文中未定义，只断言它大部分是被错误定义的。", "evidence": "P001", "ambiguity": "与“共识”“正确”的对立关系只是断言，未展开；个性为何等于“错误”也未说明。"},
    {"term": "共性", "meaning": "与“正确”天然联姻者。", "evidence": "P002", "ambiguity": "未定义，与后文的“共识”是否同义未说明。"},
    {"term": "正确／错误", "meaning": "被同时赋予事实与审美色彩：正确被等同于单调无聊，错误被等同于丰富活泼。", "evidence": "P003", "ambiguity": "未区分事实层面的正确与审美惯例层面的正确。"},
    {"term": "共识", "meaning": "艺术所要反的对象，与“共性／正确”似同指。", "evidence": "P004", "ambiguity": "“共性”“正确”“共识”三词是否同义，文中未交代。"},
    {"term": "先锋艺术", "meaning": "其常态是“看起来很失败”。", "evidence": "P005", "ambiguity": "未举例、未界定范围。"},
    {"term": "吐字不准", "meaning": "提问者提出的问题词（Q001），正文未再出现。", "evidence": "P001", "ambiguity": "作者未在发声或咬字层面解释，是否把吐字不准视为“反共识”的艺术选择，只能由上下文推断。"}
   ],
   "examples_and_targets": [
    "无具体人物、事件、作品或数据。文中唯一被引号括起的长表述“明明说来是错的，但是你知道它其实是对的”是作者自造的格言式定义，不是有出处的引文，本文按作者说法登记。",
    "提问中的“现在的歌手”是提问者设定的对象，正文未点名任何歌手、歌曲或时期。"
   ],
   "conditions": [
    "整个解释以“个性大部分是被错误定义的”这一断言为前提，该断言本身未给论证（P001）。",
    "“正确＝单调无聊、错误＝丰富活泼”是价值判断式前提，未设限定（P003）。",
    "对艺术使命的表述以“反共识”为条件，并要求存在“明明说来是错的，但是你知道它其实是对的”的东西（P004）。",
    "“看起来很失败是先锋艺术的常态”只就先锋艺术而言，作者未推广到全部艺术（P005）。"
   ],
   "rhetoric_and_tone": "极简的格言体回答：五句短句层层递进（个性→共性与正确→错误与正确→艺术使命→先锋艺术），没有例证、没有数据、没有让步，也没有直接回答提问者的技术层面疑问。用引号把“正确”“共识”括起表示存疑或反讽，并以“明明说来是错的，但是你知道它其实是对的”这一对立修辞给出艺术判断标准；语气为断言式，带审美精英立场。",
   "unresolved_questions": [
    "全文仅 5 句、106 字，未展开“个性被错误定义”与“歌手吐字不准”之间的推论链，具体因果机制不明。",
    "未点名任何歌手、作品或时期，“现在的歌手”所指范围不清。",
    "“个性”“共性”“正确”“共识”四个关键词均未定义，彼此关系只靠断言连接。",
    "“吐字不准”在正文中未再出现：作者是否把它视为反共识的艺术选择（而非缺陷），文中没有明说，本文不作推断。",
    "该篇正文与 brief 完全一致，未提供额外语境；提问者对“现在的歌手吐字不准”的预设属提问者说法，未归给作者。"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "因为个性大部分是被错误定义的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P002", "quote": "共性和“正确”天然联姻。", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "错误是丰富活泼的，正确是单调无聊的。", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "艺术的使命就是反“共识”，在于找到“明明说来是错的，但是你知道它其实是对的”的东西。", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P005", "quote": "看起来很失败是先锋艺术的常态。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["音乐与演唱", "艺术观念与美学", "个性与流行文化"],
   "issue_candidates": ["歌手吐字不清的原因", "个性与正确/共识的关系", "先锋艺术的失败外观"],
   "text_function_candidates": ["格言式短答", "美学判断"],
   "object_candidates": ["歌手", "吐字", "个性", "共识", "先锋艺术"],
   "working_keywords": ["个性", "错误定义", "共性", "正确", "共识", "先锋艺术", "吐字不准"]
  },
  "notes": "正文 5 段（全文 106 字）已全部读完；无图片节点，status=read。作者以格言式短答给出美学解释，未提供例证与数据；提问者的预设仅作语境。因果链条未展开处已登记 unresolved_questions。"
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
