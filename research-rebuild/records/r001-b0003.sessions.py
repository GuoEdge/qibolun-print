# -*- coding: utf-8 -*-
"""批次 r001-b0003 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0003.sessions.py            # 写 out/r001-b0003.out.jsonl
  python3 records/r001-b0003.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0003"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0003.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "bd497e81": {
  "analysis": {
   "question_context": "提问者（Q001）问“可控核聚变是否真的有传说中那么美好？”。作者不讨论技术能否实现，而是回答“实现可商用的可控核聚变之后能否随意用能”，给出否定性回答；P021 起为对评论区意见的集中回复，P033 起为 8.12 补充，P057 起为“题外话”。作者在 P058 自称支持核聚变技术，反对的是盲目狂热而非技术本身。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "限定：可商用聚变不等于可随意用能；热力学理由与外推",
     "role": "claim"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006"
     ],
     "summary": "长江支流类比；年增10%百年一万倍；落后即竞争力落后",
     "role": "example"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P007",
      "P008",
      "P009",
      "P010"
     ],
     "summary": "反驳“有核能即可减排回收二氧化碳故不在乎放热”，称妄想并以0.5度反设问",
     "role": "rebuttal"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P011",
      "P012"
     ],
     "summary": "后果链与行动要求：共识管制或星际殖民系统与行星级散热",
     "role": "action_advice"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P013",
      "P014"
     ],
     "summary": "国际政治困境：发展权、民意、战略野心，直到违约只有核战可反制",
     "role": "reason"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P015",
      "P016",
      "P017",
      "P018",
      "P019"
     ],
     "summary": "收束：除非世界级文明革命否则是挑战不是机遇；叹词作结",
     "role": "conclusion"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P020",
      "P021",
      "P022"
     ],
     "summary": "转入评论区回复；太空站散热类比与保温瓶反问",
     "role": "rebuttal"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P023",
      "P024",
      "P025"
     ],
     "summary": "平衡被打破与286-288K极值区间；指出对方两点错误",
     "role": "rebuttal"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P026",
      "P027"
     ],
     "summary": "耗能欲望举例与成本下降推理，人均放热可超万倍",
     "role": "reason"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P028",
      "P029",
      "P030"
     ],
     "summary": "回应温差论与“抵回来”：水是主要温室气体；硫酸与鸡蛋类比",
     "role": "rebuttal"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P031",
      "P032"
     ],
     "summary": "回应“能源无限即可太空殖民”：瓶颈是维生与控制论",
     "role": "rebuttal"
    },
    {
     "unit_id": "U012",
     "paragraph_refs": [
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
      "P046"
     ],
     "summary": "8.12补充：遮阳方案逐条质疑；升温不均匀与0.1度含义",
     "role": "rebuttal"
    },
    {
     "unit_id": "U013",
     "paragraph_refs": [
      "P047",
      "P048",
      "P049",
      "P050",
      "P051",
      "P052",
      "P053",
      "P054",
      "P055"
     ],
     "summary": "回应“聚变利好星际航行”：喷管材料、钱学森计算、1g上限",
     "role": "rebuttal"
    },
    {
     "unit_id": "U014",
     "paragraph_refs": [
      "P056",
      "P057",
      "P058",
      "P059",
      "P060",
      "P061",
      "P062",
      "P063"
     ],
     "summary": "题外话：自称支持者；原子弹时代对照；判定狂热预示滥用",
     "role": "claim"
    },
    {
     "unit_id": "U015",
     "paragraph_refs": [
      "P064",
      "P065"
     ],
     "summary": "文末“更从容的版本”与4个专栏链接及未覆盖尾部片段",
     "role": "other"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "可商用聚变≠可随意用能；限制是地球对大规模放热敏感、热也是污染。",
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
     "statement": "热收入增加地球一定升温，只有升温提高辐射功率才能重归平衡。",
     "evidence": [
      "E003",
      "E004"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "若开始“能源狂欢”，放热远超目前，必致地球“飞速”升温；聚变后功率可望在数量级上接近太阳对地功率。",
     "evidence": [
      "E005",
      "E006"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "长江支流之喻：汇入万分之一水位仍涨；年增10%百年一万倍。",
     "evidence": [
      "E007",
      "E008"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "功率上落后一步，国际竞争力就全面落后一步。",
     "evidence": [
      "E009"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "被反驳观点：有核能即可减排回收二氧化碳，因而不在乎这种规模的放热。",
     "evidence": [
      "E010"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "称此为“妄想”：百年碳排放升温贡献约0.5度；反设问并反问谁盲目。",
     "evidence": [
      "E011",
      "E012"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "若无机制与制度对冲功率狂热，很可能先行释放过量热能，致冰崩、洪灾、昆虫集体死亡、植物凋亡。",
     "evidence": [
      "E013"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "若无强有力共识管制，就必须发展星际殖民系统与行星级散热；共识须超过京都议定书与巴黎气候协议，而两者都未达成。",
     "evidence": [
      "E014",
      "E015",
      "E016"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "偷扩“民用能源”有成本优势且被称“发展权”；无科学与公众教育则无国能抵抗民意，还催生抢占放热份额的野心。",
     "evidence": [
      "E017",
      "E018",
      "E019"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "违约几乎只有核战争可反制；人类被绑架为人质。",
     "evidence": [
      "E020"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "除非出现新的世界级文明革命，否则聚变对人类是巨大挑战而非机遇。",
     "evidence": [
      "E021"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "对“白左”“圣母”的嘲笑如同为自己掘墓的铁锹。",
     "evidence": [
      "E022"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "地球虽大仍只是“巨型太空站”，没有多余特异功能。",
     "evidence": [
      "E023"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "供能、地热与人类放热已在当前温度下平衡，再放热即打破平衡、必须升温输出。",
     "evidence": [
      "E024"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "波动1%意味着高温极值提高；是否已是新极值要等升温到顶再谈。",
     "evidence": [
      "E025",
      "E026"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "人均放热需求可超万倍（烧瓷、火箭炮、超导、数据中心等）；问题不是能否打住而是够不够。",
     "evidence": [
      "E027",
      "E028"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "温室气体不止二氧化碳、最主要的是水；扣除二氧化碳后净排放能否确定下降仍是未知数。",
     "evidence": [
      "E029"
     ]
    },
    {
     "claim_id": "C019",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "孤立剧烈打击不可用有限手段抵消；升降之后世界不会回到从前（鸡蛋类比）。",
     "evidence": [
      "E030"
     ]
    },
    {
     "claim_id": "C020",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "星际殖民瓶颈不是能源而是维生与控制论；不经历千把年经验教训都是扯淡。",
     "evidence": [
      "E031",
      "E032"
     ]
    },
    {
     "claim_id": "C021",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "qualified",
     "statement": "若有拉格朗日点遮阳薄膜技术，建议先搞轨道聚能农场（并质疑镜子的尺度与引力撕裂）。",
     "evidence": [
      "E033"
     ]
    },
    {
     "claim_id": "C022",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "可测全球升0.1度时城市已升n度，热源附近以指数级下降；放热仍不均匀。",
     "evidence": [
      "E034"
     ]
    },
    {
     "claim_id": "C023",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "真空自主机动只有抛射物质一途；不换喷管核动力超不过化学火箭。",
     "evidence": [
      "E035"
     ]
    },
    {
     "claim_id": "C024",
     "claim_type": "quoted_or_cited",
     "attribution": "cited_source",
     "modality": "asserted",
     "statement": "引钱学森计算：核聚变推动下达0.8倍光速每吨载荷需34.8亿吨工质。",
     "evidence": [
      "E036"
     ]
    },
    {
     "claim_id": "C025",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "载人航速上限由人的生理（最多1g）决定；太阳系内航行恐怕化学推进器效率更高。",
     "evidence": [
      "E037",
      "E038"
     ]
    },
    {
     "claim_id": "C026",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者自称聚变技术支持者，泼冷水因见不得盲目狂热；质问谁在探讨和平利用聚变的国际框架。",
     "evidence": [
      "E039",
      "E040",
      "E041"
     ]
    },
    {
     "claim_id": "C027",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "眼下的群众狂热已预示聚变一旦诞生必遭滥用。",
     "evidence": [
      "E041"
     ]
    }
   ],
   "argument_steps": [
    "限定：可商用聚变≠可随意用能（P001-P003）。",
    "长江支流类比与功率外推、竞争压力（P004-P006）。",
    "反驳“有核能即可减排回收二氧化碳”，以0.5度反设问（P007-P010）。",
    "无条件对冲时的后果链与行动要求（P011-P012）。",
    "国际政治困境直到人质逻辑（P013-P014）。",
    "收束为“除非世界级文明革命，否则是挑战不是机遇”（P015-P019）。",
    "评论区回复一：太空站散热类比（P020-P022）。",
    "回复二：平衡被打破与极值区间（P023-P025）。",
    "回复三：耗能欲望与成本下降（P026-P027）。",
    "回复四：水是主要温室气体（P028-P030）。",
    "回复五：维生与社会控制论瓶颈（P031-P032）。",
    "8.12补充：遮阳方案五问与升温不均匀（P033-P046）。",
    "补充后半：喷管材料、钱学森计算、1g上限（P047-P055）。",
    "题外话：原子弹时代对照与群众狂热判断（P056-P063）。"
   ],
   "concept_usage": [
    {
     "term": "可控核聚变",
     "meaning": "作为“功率天花板被打开”的技术条件，本文谈其社会后果而非技术可行性",
     "evidence": "P003",
     "ambiguity": "作者自认支持该技术，反对不加管制的能源狂欢"
    },
    {
     "term": "热也可以是一种污染",
     "meaning": "大规模放热本身构成环境负担，需靠升温提高辐射排出",
     "evidence": "P002",
     "ambiguity": "未给出可承受功率阈值"
    },
    {
     "term": "能源狂欢",
     "meaning": "聚变突破后不加克制的大规模放热用能",
     "evidence": "P003",
     "ambiguity": "无量化定义"
    },
    {
     "term": "功率狂热",
     "meaning": "对提升总功率本身的追求，需以意识形态与社会制度对冲",
     "evidence": "P011",
     "ambiguity": "“足够的机制”未界定"
    },
    {
     "term": "发展权",
     "meaning": "国际语境中扩充“民用能源”规模时无可指责的说辞（作者转述）",
     "evidence": "P013",
     "ambiguity": "带引号，作者持批判态度"
    },
    {
     "term": "巨型太空站",
     "meaning": "把地球当作封闭系统的类比：内部放热必须排出",
     "evidence": "P022",
     "ambiguity": "类比而非严格模型"
    },
    {
     "term": "历史极值/变温周期",
     "meaning": "争议焦点：当前升温是否仍在自然波动范围内",
     "evidence": "P025",
     "ambiguity": "作者称是否已是新极值要等升温到顶"
    },
    {
     "term": "死重",
     "meaning": "核飞船必须始终携带的反应堆与工质重量",
     "evidence": "P049",
     "ambiguity": "“几百吨”为约数"
    },
    {
     "term": "金属氢",
     "meaning": "作者提出的化学推进新燃料，说明化学路线潜能未穷尽",
     "evidence": "P050",
     "ambiguity": "作为待核事实引用"
    }
   ],
   "examples_and_targets": [
    "长江支流水位（作者类比，P004-P005）",
    "太空站散热、保温瓶真空保温（类比与反问，P022）",
    "烧瓷、火箭炮、超导、私人坦克、比特币矿主、格陵兰与海底数据中心（举例，P026）",
    "喝硫酸再喂苛性钠、鸡蛋加温再冷却（类比，P030）",
    "旅行者号、巨型太空城、太阳能板（反驳材料，P032）",
    "拉格朗日点反射薄膜遮阳方案（被质疑的评论观点，P035-P046）",
    "九宫山、北极三十几度、空调声（反讽材料，P043-P045）",
    "钱学森的计算（引用，P052；公式以图片呈现，未核验）",
    "原子弹与核武器控制政策、为苏联提供核技术（历史叙述，P058）",
    "京都议定书、巴黎气候协议（对照物，P012）",
    "特朗普推动的法案（P065 尾部片段，疑为关联文章标题，未核验）"
   ],
   "conditions": [
    "若人类在聚变突破后开始能源狂欢，放热规模将远超目前（P003）。",
    "升温确定，但速度、幅度及是否超越生物耐受极限不确定（P003）。",
    "若无意识形态机制与社会制度对冲功率狂热（P011）。",
    "若聚变突破后没有强有力的人类共识管制其大规模使用（P012）。",
    "管制共识需超过京都议定书与巴黎气候协议，而两者都未真正达成（P012）。",
    "若无前期科学研究与主动公众教育（P013）。",
    "除非出现某种新的世界级文明革命（P015）。",
    "按稳定波动假设推算下次极值区间（P023）；乘员为人类且用工质推进器时加速度最多1g（P054）。",
    "即使有核能源与超喷管（P050）。",
    "作者限定：本文未提到人工智能因素（P015）。"
   ],
   "rhetoric_and_tone": "训诫与反讽并重的论辩体：自称“泼冷水”，密集使用反问（“是我盲目，而是你们的乐观盲目？”）、比喻（长江支流、巨型太空站、硫酸与苛性钠、鸡蛋）与夸张（北极都三十好几度了、空调声音太响），以宗教式祈愿与“唉”收束；对评论区意见以“同学们”“ta们”相称，带嘲讽训诫语气，同时明确自称支持核聚变技术、反对盲目狂热。",
   "unresolved_questions": [
    "P003 括号内“我们现在万分之一……将来我们可能翻一万倍”的具体口径及末尾所附文章未在本文展开。",
    "P023 的286-288K极值区间作者自称“懒得查文献”，需外部核查。",
    "P052 钱学森计算以图片/公式呈现，本文无法核验数值与推导。",
    "P065 尾部“特朗普推动了一项可能导致人类毁灭的法案”未被 lexical 覆盖，疑为关联文章标题或平台插入内容，归属未定。",
    "IMG001（文首图片）未核验，需图像核验。",
    "评论区被回复对象的具体原文不在本文中，其立场只能由作者转述判断。"
   ],
   "evidence": [
    {
     "key": "E001",
     "paragraph_id": "P001",
     "quote": "实现可商用的可控核聚变并不意味着人类可以随意的使用能源",
     "relation": "supports"
    },
    {
     "key": "E002",
     "paragraph_id": "P002",
     "quote": "热也可以是一种污染",
     "relation": "supports"
    },
    {
     "key": "E003",
     "paragraph_id": "P003",
     "quote": "热收入增加，地球一定会升温",
     "relation": "supports"
    },
    {
     "key": "E004",
     "paragraph_id": "P003",
     "quote": "只有升温对外提高辐射功率才能重归热平衡",
     "relation": "supports"
    },
    {
     "key": "E005",
     "paragraph_id": "P003",
     "quote": "如果人类在可控核聚变技术突破后开始能源狂欢",
     "relation": "supports"
    },
    {
     "key": "E006",
     "paragraph_id": "P003",
     "quote": "数量级上大幅接近太阳对地输出功率的可能",
     "relation": "supports"
    },
    {
     "key": "E007",
     "paragraph_id": "P004",
     "quote": "武汉水位是不是上涨？",
     "relation": "supports"
    },
    {
     "key": "E008",
     "paragraph_id": "P006",
     "quote": "只用一百年，我们就能提升一万倍",
     "relation": "supports"
    },
    {
     "key": "E009",
     "paragraph_id": "P006",
     "quote": "谁落后一步，谁的国际竞争力就会全面落后一步",
     "relation": "supports"
    },
    {
     "key": "E010",
     "paragraph_id": "P007",
     "quote": "不在乎这种规模的放热",
     "relation": "supports"
    },
    {
     "key": "E011",
     "paragraph_id": "P008",
     "quote": "一共也就0.5度",
     "relation": "supports"
    },
    {
     "key": "E012",
     "paragraph_id": "P010",
     "quote": "是我盲目，而是你们的乐观盲目？",
     "relation": "supports"
    },
    {
     "key": "E013",
     "paragraph_id": "P011",
     "quote": "在不可逆的后果变得明显之前就释放出过量热能",
     "relation": "supports"
    },
    {
     "key": "E014",
     "paragraph_id": "P012",
     "quote": "发展出星际殖民的系统技术",
     "relation": "supports"
    },
    {
     "key": "E015",
     "paragraph_id": "P012",
     "quote": "我们连这两个最基本的协议也未能真正达成",
     "relation": "supports"
    },
    {
     "key": "E016",
     "paragraph_id": "P013",
     "quote": "偷偷大规模提高自己的“民用能源”规模能带来极大的制造成本优势",
     "relation": "supports"
    },
    {
     "key": "E017",
     "paragraph_id": "P013",
     "quote": "将没有哪个国家能抵抗“全面应用核聚变技术”的民意呼声",
     "relation": "supports"
    },
    {
     "key": "E018",
     "paragraph_id": "P013",
     "quote": "抢占和锁定自己的放热份额",
     "relation": "supports"
    },
    {
     "key": "E019",
     "paragraph_id": "P014",
     "quote": "这种违约几乎只有核战争一种真正的反制手段",
     "relation": "supports"
    },
    {
     "key": "E020",
     "paragraph_id": "P015",
     "quote": "巨大的挑战，而不是机遇",
     "relation": "supports"
    },
    {
     "key": "E021",
     "paragraph_id": "P018",
     "quote": "如同为自己掘墓的铁锹",
     "relation": "supports"
    },
    {
     "key": "E022",
     "paragraph_id": "P022",
     "quote": "地球虽大，仍然是一个“巨型太空站”",
     "relation": "supports"
    },
    {
     "key": "E023",
     "paragraph_id": "P023",
     "quote": "是打破平衡",
     "relation": "supports"
    },
    {
     "key": "E024",
     "paragraph_id": "P023",
     "quote": "地球以后遭遇的高温极值会提高",
     "relation": "supports"
    },
    {
     "key": "E025",
     "paragraph_id": "P025",
     "quote": "还要等这次升温升到顶再谈",
     "relation": "supports"
    },
    {
     "key": "E026",
     "paragraph_id": "P026",
     "quote": "而是一万倍够不够的问题",
     "relation": "supports"
    },
    {
     "key": "E027",
     "paragraph_id": "P027",
     "quote": "那时候你的功耗是多少？",
     "relation": "supports"
    },
    {
     "key": "E028",
     "paragraph_id": "P029",
     "quote": "最主要的温室气体是水",
     "relation": "supports"
    },
    {
     "key": "E029",
     "paragraph_id": "P030",
     "quote": "不要把地球当铁块，要把地球当鸡蛋",
     "relation": "supports"
    },
    {
     "key": "E030",
     "paragraph_id": "P032",
     "quote": "星际殖民的瓶颈根本不是能源，而是维生",
     "relation": "supports"
    },
    {
     "key": "E031",
     "paragraph_id": "P032",
     "quote": "不经历个千把年的经验教训总结，都是扯淡",
     "relation": "supports"
    },
    {
     "key": "E032",
     "paragraph_id": "P037",
     "quote": "先别搞核聚变而是搞轨道聚能农场",
     "relation": "supports"
    },
    {
     "key": "E033",
     "paragraph_id": "P042",
     "quote": "热源附近以指数级下降",
     "relation": "supports"
    },
    {
     "key": "E034",
     "paragraph_id": "P050",
     "quote": "你用核动力，不换喷管，你超不过化学火箭",
     "relation": "supports"
    },
    {
     "key": "E035",
     "paragraph_id": "P052",
     "quote": "每1吨有效载荷，要配34.8亿吨工质",
     "relation": "supports"
    },
    {
     "key": "E036",
     "paragraph_id": "P054",
     "quote": "最多只能1g",
     "relation": "supports"
    },
    {
     "key": "E037",
     "paragraph_id": "P055",
     "quote": "化学推进器的效率更高，未来更光明",
     "relation": "supports"
    },
    {
     "key": "E038",
     "paragraph_id": "P058",
     "quote": "我是核聚变技术的支持者",
     "relation": "supports"
    },
    {
     "key": "E039",
     "paragraph_id": "P058",
     "quote": "是见不得盲目狂热",
     "relation": "supports"
    },
    {
     "key": "E040",
     "paragraph_id": "P059",
     "quote": "谁在探讨和平使用核聚变技术的国际框架？",
     "relation": "supports"
    },
    {
     "key": "E041",
     "paragraph_id": "P062",
     "quote": "都直接预示着核聚变一旦诞生，必遭滥用",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "核能与可控核聚变",
    "气候变化与地球热平衡",
    "国际政治与军控",
    "太空探索与星际航行",
    "技术伦理与社会制度"
   ],
   "issue_candidates": [
    "聚变商用后的废热排放",
    "全球升温与生物适应极限",
    "能源管制的国际共识",
    "发展权与竞争",
    "星际殖民的瓶颈",
    "推进方式与材料学限制"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "反驳",
    "评论区集中答复"
   ],
   "object_candidates": [
    "可控核聚变（技术）",
    "地球环境/大气",
    "京都议定书",
    "巴黎气候协议",
    "NASA",
    "太空站",
    "钱学森",
    "金属氢",
    "特朗普（尾部片段）"
   ],
   "working_keywords": [
    "可控核聚变",
    "热污染",
    "热平衡",
    "能源狂欢",
    "功率狂热",
    "放热份额",
    "行星级散热",
    "星际殖民",
    "工质推进",
    "死重",
    "金属氢",
    "历史极值"
   ]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "超限压缩重做（简报 3.1 节）：原输出 57515 字符（上限 40000），压缩方式为主张由 65 条并为 27 条、证据短引由 88 条并为 42 条（只留承担主张的最短连续片段）、内容单元由 20 并为 15、摘要与论证步骤改为短句；段落定位、归属与语气标记、未决问题均保留，合并处理见本 notes。本篇含 1 个图片节点 IMG001（文首），未核验，故 status=needs_reread；结尾 P065 有一句未被 lexical 覆盖，疑为关联文章标题。",
 },
 "0d19a72d": {
  "analysis": {
   "question_context": "提问者（Q001）问“脱离语言的思考是否等同于直觉？”。作者先声明要谈定义，在“假设我们谈论的是中文”的前提下给出“思考”与“直觉”的定义，据此判定这一问法本身已被定义解决；随后另起一层追问“思考能不能脱离语言”，给出的答案是开放的“不知道能不能”。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "开场评语：“这是一个有意思的问题。”",
     "role": "context"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002"
     ],
     "summary": "定义单元：在“谈论的是中文”的假设下，思考＝产生想法并对想法进行判断的行为；直觉＝直接的感觉；“直接”所跳过的是指一切非直接的过程，这显然包含思考在内。",
     "role": "definition"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P003"
     ],
     "summary": "由定义得结论：若谈论的是中文，这个问题本身已被定义解决；“直觉”就是未经思考而有的感觉，因此绝不可能有任何形式的思考等同于任何形式的直觉。",
     "role": "conclusion"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "转入第二层问题：思考能不能脱离语言？",
     "role": "transition"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "第二层的回答：我们不知道能不能，但知道很难做出可证实肯定结论的研究；需要先了解“不使用语言的思考”是什么行为、大脑如何思考，并从化学的、最终是物理的层面把思考重定义为物理化学过程；作者以“就我的猜想”给出直觉＝随机放电被大脑某些逻辑判断结构强迫性抓住并不断合理化的过程（李自成类比）。",
     "role": "reason"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“假设我们谈论的是中文”为前提，把思考定义为“产生想法，然后对想法进行判断的行为”，把直觉定义为“直接的感觉”。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者认为“直接”所跳过的是指一切非直接的过程，这显然包含“思考”在内。",
     "evidence": [
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者认为若谈论的是中文，这个问题本身已经被问题的定义解决。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者认为所谓“直觉”就是未经思考而有的感觉，因此绝不可能有“（任何形式的）思考”等同于“（任何形式的）直觉”这种事。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "对“思考能不能脱离语言”，作者的答案是：我们不知道能不能，但我们知道很难做出可以证实肯定结论的研究。",
     "evidence": [
      "E5"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者指出：目前首先并不了解“不使用语言的思考”本身是什么样的行为，其次也不知道大脑实际上是如何进行思考的；要回答该问题需要先从化学的、最终是物理的层面理解大脑如何进行思考。",
     "evidence": [
      "E6",
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "作者设问：假设思考脱离语言的确可能，那要做什么样的实验去验证这种可能性。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者以“就我的猜想”提出：直觉是随机发生的放电被大脑某些逻辑判断结构强迫性地牢牢抓住的过程；念头完全随机产生，出生第一脚就踩进“是”的泥潭，被一系列机制滚雪球般不断合理化，最终成为无法被显式判断部门无视的庞然大物（以李自成作比）。",
     "evidence": [
      "E9",
      "E10",
      "E11"
     ]
    }
   ],
   "argument_steps": [
    "先声明要谈定义，并把讨论限定在“我们谈论的是中文”这一假设（P002）。",
    "给出“思考”与“直觉”的定义，并指出“直接”跳过一切非直接过程，其中包含思考（P002）。",
    "由定义推出：提问的表述本身已被定义解决，直觉是未经思考而有的感觉，故任何形式的思考都不等同于任何形式的直觉（P003）。",
    "另起第二层追问：思考能不能脱离语言（P004）。",
    "回答第二层：不知道能不能，但知道很难做出可证实肯定结论的研究；给出研究路径（了解该行为、了解大脑如何思考、把思考重定义为物理化学过程、再了解语言过程的本质）（P005）。",
    "最后以自称的猜想给出直觉的机制描述，并用李自成类比收尾（P005）。"
   ],
   "concept_usage": [
    {
     "term": "思考",
     "meaning": "作者在本文中定义为“产生想法，然后对想法进行判断的行为”，并进一步主张需要把它重新定义为某种物理化学过程才能研究其是否涉及语言。",
     "evidence": "P002、P005",
     "ambiguity": "定义以“假设我们谈论的是中文”为限；作者未说明该定义是否适用于其他语言或非语言符号系统。"
    },
    {
     "term": "直觉",
     "meaning": "作者先定义为“直接的感觉”，并解释为未经思考而有的感觉；后文又以“就我的猜想”给出随机放电被逻辑判断结构抓住并合理化的机制描述。",
     "evidence": "P002、P003、P005",
     "ambiguity": "前后两层用法不同：前者是定义性排除，后者是自称的机制猜想，本文未说明两者如何统一。"
    },
    {
     "term": "直接",
     "meaning": "作者用它指跳过一切非直接过程（包含思考）的感觉方式。",
     "evidence": "P002",
     "ambiguity": "“非直接的过程”的边界本文未列举。"
    },
    {
     "term": "不使用语言的思考",
     "meaning": "作者用来指称第二层问题所假设的对象，并称我们对它“已经极其陌生”、并不了解它是种什么样的行为。",
     "evidence": "P005",
     "ambiguity": "作者未给出任何实例或判定标准，也未说明语言过程本质为何。"
    },
    {
     "term": "物理化学过程",
     "meaning": "作者主张的研究进路：把思考重新定义为某种物理化学过程，从而了解语言的过程本质，并回答是否存在未涉及语言的思考反应。",
     "evidence": "P005",
     "ambiguity": "该进路的具体层次（化学的、最终是物理的）与可操作方案本文未说明。"
    },
    {
     "term": "李自成",
     "meaning": "作者用于比喻直觉的修辞材料：虽不合法但很强大，使人不得不对它有一番正式的反应。",
     "evidence": "P005",
     "ambiguity": "该比喻的历史语境与本文论证的关系未说明，属修辞而非论证依据。"
    }
   ],
   "examples_and_targets": [
    "修辞/历史类比：把已经成形的直觉比作“李自成，虽不合法，但却很强大”（P005）。",
    "比喻材料：“这无来由的念头出生第一脚就踩进了‘是’的泥潭”“滚雪球一样地不断合理化”“庞然大物”“显式的判断部门”（P005）。",
    "被讨论对象：提问者提出的“脱离语言的思考”与“直觉”的等同关系（Q001，属提问者立场，非作者主张）。",
    "作者未使用人物、机构、事件或数据类证据；本文没有引文与文献出处。"
   ],
   "conditions": [
    "“假设我们谈论的是中文”（P002）——第一层定义与结论都以此为限。",
    "“如果我们谈论的是中文，这个问题本身已经被问题的定义解决”（P003）——结论明确限定在中文语境。",
    "“假设这的确可能”（P005）——关于验证实验的设问以该假设为前提。",
    "“就我的猜想”（P005）——直觉机制部分被作者自陈为猜想，不属确定结论。",
    "“我们不知道能不能”（P005）——作者对第二层问题保持未决，未给出肯定或否定答案。",
    "研究者补注：本文的否定性结论（思考不等同于直觉）只针对该定义下的用法，不应推广为作者对所有“直觉”用法的判断。"
   ],
   "rhetoric_and_tone": "简洁的问答体/思辨短文。以“这是一个有意思的问题”开场，延续性用语“还是一样，要先谈定义”提示与前作的写作习惯。以设问推进（“‘直接’所跳过的是什么呢？”“那我们要做什么样实验去验证这种可能性呢？”），先以定义判定原问题“已经被问题的定义解决”，再另起一层把问题打开为未知。语气克制，自称“就我的猜想”，无讽刺与训诫；末段密集使用比喻与历史人物类比（踩进“是”的泥潭、滚雪球、庞然大物、判断部门、李自成），是全文修辞最重的部分。",
   "unresolved_questions": [
    "提问者（Q001）只说“脱离语言的思考是否等同于直觉”，未说明“直觉”的日常用法或理论来源；本文的定义是作者自设的。",
    "作者以“假设我们谈论的是中文”为前提，若换用其他语言或非语言符号系统，结论是否成立本文未说明。",
    "作者对第二层问题给出的是“我们不知道能不能”的开放立场（P005），本文没有肯定或否定的结论；不得据此推断作者的立场。",
    "“直觉是随机发生的放电”属作者自陈的猜想（“就我的猜想”），未给出理论依据、实验或文献；其中“显式的判断部门”“虽不合法”等用语的具体所指未说明。",
    "李自成类比属修辞材料，其历史细节不在本文论证范围内，本记录不据其生成主张。",
    "正文仅 627 字符，是否在采集时被截断无法由本文判断；brief 字段明显在句中被截断（止于“这个问题本身已经被问题”），但 brief 只作导航，不用于支持主张。",
    "本文正文与 lexical 结构一致（无 divergence），未见平台话题标签；原帖的发布时间与更新情况只能依据元数据（published_at=2018-07-26、updated_at=2025-01-05）。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P002",
     "quote": "假设我们谈论的是中文，那么思考是指“产生想法，然后对想法进行判断的行为”，而“直觉”，是指“直接的感觉”。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "是指一切非直接的过程，这显然包含“思考”在内。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "如果我们谈论的是中文，这个问题本身已经被问题的定义解决",
     "relation": "qualifies"
    },
    {
     "key": "E4",
     "paragraph_id": "P003",
     "quote": "因此绝不可能有“（任何形式的）思考”等同于“（任何形式的）直觉”这种事。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P005",
     "quote": "我们不知道能不能，但我们知道我们很难做出可以证实肯定结论的研究",
     "relation": "qualifies"
    },
    {
     "key": "E6",
     "paragraph_id": "P005",
     "quote": "我们目前首先并不了解“不使用语言的思考”本身是个什么样的行为，这对我们已经极其陌生，其次我们也不知道大脑实际上是如何进行思考的。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P005",
     "quote": "我们首先需要从化学的、最终是物理的层面理解大脑如何进行思考。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P005",
     "quote": "假设这的确可能，那我们要做什么样实验去验证这种可能性呢？",
     "relation": "context"
    },
    {
     "key": "E9",
     "paragraph_id": "P005",
     "quote": "就我的猜想，直觉是随机发生的放电被大脑的某些逻辑判断结构强迫性地牢牢地抓住的过程。",
     "relation": "qualifies"
    },
    {
     "key": "E10",
     "paragraph_id": "P005",
     "quote": "念头是完全随机产生的，只是这无来由的念头出生第一脚就踩进了“是”的泥潭。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P005",
     "quote": "它已经成了李自成，虽不合法，但却很强大，你不得不对它有一番正式的反应——是为直觉。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "心智哲学/认知科学",
    "语言学",
    "心理学（直觉研究）"
   ],
   "issue_candidates": [
    "思考与语言的关系",
    "直觉的定义",
    "思考的物理化学还原进路",
    "以定义消解提问"
   ],
   "text_function_candidates": [
    "答疑",
    "概念辨析",
    "猜想性回答"
   ],
   "object_candidates": [
    "中文",
    "大脑",
    "李自成"
   ],
   "working_keywords": [
    "思考",
    "直觉",
    "直接的感觉",
    "不使用语言的思考",
    "物理化学过程",
    "放电",
    "合理化",
    "定义"
   ]
  },
  "notes": "本篇无图片节点，正文非空，按默认 status=read、full_text_checked=true 处理。brief 字段在句中被截断（止于“这个问题本身已经被问题”），仅作导航，未用于支持任何主张；正文（627 字符）与 lexical 结构一致、无 divergence，但原帖是否在采集时被截断无法由本记录判定，已登记为未决问题。提问者立场（脱离语言的思考等同于直觉）未被归给作者；作者对该问法给出的是定义性否定（P003），对第二层问题保持“不知道能不能”的开放立场（P005），其“直觉是随机发生的放电”云云为作者自陈的猜想。"
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
        rec = build_record(
            row, row['batch_id'], row['corpus_sha256'],
            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', ''))
        # 简报 8.1：段落 text 只保留必要短引。本篇段落多（65 段），
        # 样例统一截到 60 字符以控制单篇记录体量；完整定位由 paragraph_id 与字符范围回查语料。
        for _pa in rec['structure']['paragraphs']:
            _t = _pa.get('text') or ''
            if len(_t) > 60:
                _pa['text'] = _t[:60]
                _pa['sample_truncated'] = True
        records.append(rec)
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
