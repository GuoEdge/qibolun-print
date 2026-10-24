# -*- coding: utf-8 -*-
"""批次 r001-b0026 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0026.sessions.py            # 写 out/r001-b0026.out.jsonl
  python3 records/r001-b0026.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0026"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0026.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "7d32dc18": {
  "analysis": {
   "question_context": "提问者问：战斗机的发动机通过逆向工程不就能再制造出来了吗？（Q001，属提问者立场，不得归给作者）。作者在本文回应这一疑问：先以机械加工与装配中的误差为例说明工业制造的极端复杂性，再以基因组工程的基因交互作类比，论证航空发动机这类复杂工业结晶的误差工艺很难靠测量与试错逆向破解。正文后半（P022 特别声明为 3.8K 赞数之后追加）另展开一个附带论题——系统级总工程师所需的综合能力实际上高于理论物理学家，并从问题规模、公/私问题、名望来源三方面论证；P053 起为收束与收藏夹链接。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "开篇称机械行业奥妙，借《生活大爆炸》谢耳朵瞧不起霍华德作比，提出系统级总工程师所需的综合能力远高于理论物理学家。",
     "role": "claim"
    },
    {
     "unit_id": "U002",
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
      "P014"
     ],
     "summary": "以零件公差、磨平面、钻深孔、车圆、打轴心孔、拧螺栓、装长轴、材料探伤等一系列例子说明误差无处不在、实际值极难确定且相互交联。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P015",
      "P016"
     ],
     "summary": "总结工程师是误差的巫师：控制得好误差互相抵消并出现磨合效应与自维护性，控制不好则动都不动、硬动散架。",
     "role": "conclusion"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P017"
     ],
     "summary": "误差的处置和管理是极复杂的艺术；对航空发动机这种复杂度，没有主动传授而纯靠测量与试错逆向破解极其困难（直接回应提问）。",
     "role": "conclusion"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020",
      "P021"
     ],
     "summary": "以基因组工程中多基因交缠、改动不同位点会使结果反转为例，类比航空发动机误差工艺的破解复杂度。",
     "role": "example"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P022"
     ],
     "summary": "特别声明：以下内容是 3.8K 赞数之后追加，不能认为赞同本答案的人一定赞同下面这一段话。",
     "role": "qualification"
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
      "P032",
      "P033"
     ],
     "summary": "追问理论物理突破中能力与训练扮演什么角色，提出大脑信号处理机—潜意识加工成灵感—显式思维孵化三阶段模型，并说明直觉初筛具有宁错杀勿放过的特性。",
     "role": "reason"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P034",
      "P035",
      "P036",
      "P037"
     ],
     "summary": "高智能者与普通人的差别在于长期专注训练使初筛直觉更好；但最初的灵感本身随机、不受人控制，人只能让自己这块土壤肥沃。",
     "role": "qualification"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P038",
      "P039",
      "P040",
      "P041",
      "P042",
      "P043",
      "P044",
      "P045"
     ],
     "summary": "据此劝导研究者摆脱没成果即能力不足的致命焦虑，把首要任务定为是否坚持自我肥沃、长期等待的游戏，并批评天才偶像崇拜扭曲青年动机。",
     "role": "action_advice"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P046",
      "P047",
      "P048",
      "P049",
      "P050",
      "P051",
      "P052"
     ],
     "summary": "从问题规模超出单个人脑上限、理论问题是公问题而工程问题是私问题、名望源于可感知度不对称三方面，论证工程综合能力要求不低于理论物理研究。",
     "role": "reason"
    },
    {
     "unit_id": "U011",
     "paragraph_refs": [
      "P053",
      "P054",
      "P055"
     ],
     "summary": "题外话收束与收藏夹链接；科学答集、家族答集为平台话题标签混入正文。",
     "role": "transition"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "对航空发动机这种复杂度的工业结晶，在没有主动传授的前提下纯靠测量和试错逆向破解，极其困难——即逆向工程不足以简单再造出战斗机发动机。",
     "evidence": [
      "E6",
      "E7"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "系统级总工程师所需要的综合能力实际上要远远高于理论物理学家。",
     "evidence": [
      "E1",
      "E20"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "加工与装配中误差是要害；零件的实际尺寸极难精确知道，取决于量哪里，图纸上的理想值并不等于实物。",
     "evidence": [
      "E2",
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "工程师是误差的巫师：控制得好误差互相抵消并出现磨合效应与自维护性，控制不好则动都不动、硬动散架。",
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
     "statement": "理论问题建立在可重复、与时空无关的普遍前提上，是公问题；工程问题建立在特定特殊前提上，是私问题；因此工程问题学术条件远比理论物理恶劣。",
     "evidence": [
      "E18",
      "E19",
      "E20"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "理论物理学家有建树时名望往往远高于系统工程师，源于可感知度差异造成的不对称文化崇拜，不能据此推论理论物理学家能力一定更强。",
     "evidence": [
      "E21"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "单纯从智力挑战的艰难度而言，理论物理研究并不比复杂的工程问题挑战大。",
     "evidence": [
      "E17"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "asserted",
     "statement": "高智能的人与普通人的差别在于长期专注训练和积累使初筛机制对特定主题有更好的直觉、潜意识更不易误判，从而能看到更多潜在合理性。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "最初的那个灵感本身是随机的、不受人控制；人不能命令风如何吹，对是否会有种子落在自己身上没有决定权。",
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
     "statement": "研究没有结果、思考没有突破并不是纯然的能力问题，甚至可以说与能力没有太大关系，因此不应焦虑沮丧。",
     "evidence": [
      "E12",
      "E13"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "越是认定理论物理研究靠能力的人，越没有机会真的看到出成果那一天，学术生命反而越悲观，往往最早转行去投行。",
     "evidence": [
      "E14"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "将有建树的理论物理学家推上绝顶聪明宝座的观念是一种大众流行文化、新时代单方面的偶像崇拜，且恰恰扭曲了青年进入该领域的动机和基本姿态。",
     "evidence": [
      "E15"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "真正的问题是年轻人不够诚恳；理论物理研究更多是念念不忘必有回响的功夫，而不是天才绝顶一鸣惊人的游戏。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "如果比较的是现代尖端系统工程，很多工程问题的规模都超出单个人脑所能处理的上限，工程师还须是团队领导者和管理大师。",
     "evidence": [
      "E22"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "基因工程中同一基因参与多个性状、改动位点结果会反转的情形，是理解航空发动机误差工艺破解复杂度的类比。",
     "evidence": [
      "E23"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "作者声明 P023 起为 3.8K 赞数之后追加的内容，赞同本答案前文的人不一定赞同追加部分。",
     "evidence": [
      "E8"
     ]
    }
   ],
   "argument_steps": [
    "前提（P001-P003）：机械行业奥妙；以谢耳朵与霍华德作比，先抛出待论证判断——系统级总工程师综合能力远高于理论物理学家。",
    "理由/例证（P004-P014）：误差是要害；逐一举出公差、平面、深孔、圆度、轴心孔、螺栓紧固、长轴装配、材料探伤与性能、误差交联等情形，说明理想值与实物之差距。",
    "小结（P015-P016）：误差控制的两极结果——磨合效应、自维护性，或不动与散架。",
    "结论之一（P017）：误差的处置和管理是极复杂的艺术，航空发动机级的复杂度无法在没有主动传授时靠测量与试错逆向破解。",
    "类比（P018-P021）：基因组工程中多基因交缠、改位点结果反转，用以说明上述复杂度。",
    "自我限定（P022）：声明后文为追加内容，与前半的赞同者未必一致。",
    "追问与模型（P023-P033）：理论物理突破中能力与训练的角色；潜意识把随机放电加工成灵感，显式思维再孵化；直觉初筛宁错杀勿放过。",
    "让步与限定（P034-P037）：训练能改善特定主题的直觉，但第一推动的灵感随机、不受控。",
    "行动建议（P038-P045）：不要焦虑，首要任务是决定是否坚持长期等待的游戏；批评天才偶像崇拜与及时止损心态。",
    "第二组理由（P046-P052）：智力挑战难度上理论物理并不更大；问题规模、公问题/私问题、名望与可感知度三方面支持综合能力要求之比较。",
    "收束（P053-P055）：题外话与收藏夹链接。"
   ],
   "concept_usage": [
    {
     "term": "误差",
     "meaning": "加工、装配、材料与运行中实际值对理想值的偏离，可相互抵消或累积，也可在运行中迁移；是本文解释工业复杂度与逆向工程困难的核心概念。",
     "evidence": "P004",
     "ambiguity": "文中泛指尺寸、形位、材料、性能等多类偏差，未作严格分类。"
    },
    {
     "term": "磨合效应",
     "meaning": "误差控制得当时机器越跑越顺、甚至具有自维护性的现象。",
     "evidence": "P015",
     "ambiguity": "以引号标出，作者未给出机理或量化条件。"
    },
    {
     "term": "公问题/私问题",
     "meaning": "理论问题建立在可重复、与时空无关的普遍前提上故为公问题；工程问题建立在特定江、山、合金、工艺、市场等特殊前提上故为私问题，能有效沟通者仅限共享同一前提的人。",
     "evidence": "P049",
     "ambiguity": "作者把沟通条件与问题难度并置，二者的因果权重未量化。"
    },
    {
     "term": "灵感（潜意识加工产物）",
     "meaning": "大脑皮层随机放电经潜意识两阶段加工后形成的雏形，是显式思考的起点；其产生随机、不受控。",
     "evidence": "P025",
     "ambiguity": "作者以大脑信号处理机的说法作说明，属其本人表述，本文未给出实证依据。"
    },
    {
     "term": "初筛机制",
     "meaning": "显式思考之前对灵感作快速取舍的直觉判断，其特性是宁错杀勿放过，以免智力资源被无意义念头淹没。",
     "evidence": "P033",
     "ambiguity": "为作者的机制性假设，未标注来源。"
    }
   ],
   "examples_and_targets": [
    "《生活大爆炸》的谢耳朵与霍华德：修辞类比，用于引出能力比较。",
    "15.000±0.008mm 零件公差、切割端面不平（P005）：作者例证。",
    "磨平面与激光反射点、商场地面灯光反射（P006）：作者例证与日常类比。",
    "深孔钻削、滑膛炮炮膛、发热与炮管形变（P007）：作者例证。",
    "车圆成卵形、打轴心孔偏差导致转子声音不对（P008、P009）：作者例证。",
    "六个螺栓紧固两块钢板的应力偏向与金属疲劳（P010）：作者例证。",
    "6 米长、直径 1 米的轴装入轴套，泡软的意大利空心面比喻；船用汽轮机主轴（P011、P012）：作者例证与类比。",
    "探伤、金相检验、晶化、蠕变、疲劳、压电效应、击穿、散热等（P013）：作者例证清单。",
    "基因组工程：改变位点导致肤色、耳垂、先天性心脏病等结果反转（P020）：作者类比（说明性虚构情景）。",
    "航空发动机（P017、P021）：被解释对象，也是提问所指对象。",
    "3.8K 赞数及追加声明（P022）：平台数据，作者自述。",
    "投行（P041）：作者对转行去向的调侃性断言。",
    "歼20 与 F22/F35 设计师之间无法沟通（P050）：作者例证。",
    "三峡工程（P052）：作者例证。",
    "收藏夹科学答集、家族答集（P055）：平台话题标签混入正文。"
   ],
   "conditions": [
    "逆向破解困难的限定条件：必须在没有主动传授的前提下、且对象是航空发动机这种复杂度的工业结晶（P017）。",
    "作者自设边界：P023 起为 3.8K 赞后追加，不能认为赞同前文者一定赞同追加部分（P022）。",
    "高智能者优势的限定：仅针对特定主题，且依赖长期专注训练和积累（P034）。",
    "灵感随机不受控的限定：人只能使自己这块土壤肥沃，对是否有种子落下没有决定权（P036、P037）。",
    "工程能力比较的限定：比较对象是现代的尖端系统工程，且强调问题规模超出单个人脑处理上限（P047）。",
    "公问题/私问题的沟通条件带附加限定：即使不考虑保密限制，能有效沟通的也只有分享同一工程前提的人（P050）。",
    "P041 的转行投行为趋势性预测，非统计数据。"
   ],
   "rhetoric_and_tone": "以第二人称你作训导式举例，层层铺陈；大量排比与递进（P013 的防尘防水防酸防盐防高温防寒、一言难尽），连续反问（P012 那要是你的厂房没这么大、空、高呢？；P018 如何准确的描述问题的复杂度呢？），比喻密集（误差的巫师、泡软的意大利空心面、风中的蒲公英种子、作为土壤的人）；P022 以括号作特别声明以切分追加内容；P041 带讽刺地调侃以能力论者往往最早转行去投行；P038-P045 转为劝慰与训诫语气；整体是答疑式长文，前半说工业、后半转科研心态与体制评论。",
   "unresolved_questions": [
    "Q001 所指的具体对象（哪款战斗机发动机、何种逆向工程说法或传闻）正文未说明，作者也未复述提问原文。",
    "P020 的肤色、大耳垂、先天性心脏病等多基因交互情景为说明性虚构还是有所本，本文未说明。",
    "3.8K 赞数及追加声明对应的评论区争议内容未被保存，无法核验作者所回应的具体反对意见。",
    "徒步/理论物理与系统工程的综合能力比较缺乏可操作指标，本文未给出测量方式，属作者判断。",
    "谢耳朵、霍华德为电视剧角色，以其作能力比较属修辞类比，非事实断言。",
    "P055 的科学答集、家族答集为平台话题/收藏夹标签，lexical 未覆盖该尾部片段，正文与结构不一致。",
    "P013 所列材料与性能问题为概括性罗列，未给出具体案例或标准。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P003",
     "quote": "系统级总工程师所需要的综合能力实际上要远远高于理论物理学家。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P004",
     "quote": "要害就在于误差。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P005",
     "quote": "加工一个零件，设计是15.000mm宽，其实不是。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P015",
     "quote": "工程师就是误差的巫师。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P016",
     "quote": "控制得不好，动都不动，硬动散架。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P017",
     "quote": "想要在没有主动传授的前提下纯靠测量和试错逆向破解，极其的困难。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P021",
     "quote": "你就差不多明白航空发动机的误差工艺奥秘要破解起来是什么样的复杂度了。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P022",
     "quote": "（特别声明，以下内容是在3.8K赞数之后追加，不能认为赞同本答案的人一定赞同下面这一段话）",
     "relation": "qualifies"
    },
    {
     "key": "E9",
     "paragraph_id": "P034",
     "quote": "ta们的初筛机制对特定主题有更好的“直觉”",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P035",
     "quote": "但是最初的那个灵感本身是随机的，是不受人控制的。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P037",
     "quote": "你不能命令风如何吹",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P038",
     "quote": "并不是一个纯然的能力问题",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P039",
     "quote": "你更首要的任务是决定你是否要在这样一种“自我肥沃，长期等待”的游戏中坚持下去。",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P041",
     "quote": "ta们往往最早转行去投行。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P042",
     "quote": "一种新时代的单方面的偶像崇拜",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P044",
     "quote": "其实真正的问题是ta们不够诚恳",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P046",
     "quote": "单纯从智力挑战的艰难度而言，理论物理研究并不比复杂的工程问题挑战大。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P049",
     "quote": "是建立在一种可以重复的、与时间和空间无关的普遍前提之上",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P050",
     "quote": "而工程问题之所以成其为问题，是建立在一个特定的特殊前提之上。",
     "relation": "supports"
    },
    {
     "key": "E20",
     "paragraph_id": "P051",
     "quote": "问题的难度和规模不在理论物理研究之下，但是学术条件却远比后者恶劣。",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P052",
     "quote": "并不能因此推论出理论物理学家一定比系统工程师能力强。",
     "relation": "supports"
    },
    {
     "key": "E22",
     "paragraph_id": "P047",
     "quote": "很多工程的问题规模都是超出单个人脑所能处理的规模上限的",
     "relation": "supports"
    },
    {
     "key": "E23",
     "paragraph_id": "P020",
     "quote": "改变一个基因位点，看似对整体性状有一个确切的结果",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "机械制造与精密加工",
    "航空航天工业",
    "工程与科研体制",
    "认识论/心智与创造力",
    "职业劝诫"
   ],
   "issue_candidates": [
    "航空发动机逆向工程可行性",
    "加工误差与公差控制",
    "系统工程师与理论物理学家能力比较",
    "科研灵感的能力归因",
    "学术生命夭折与转行"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "经验总结",
    "训诫劝导"
   ],
   "object_candidates": [
    "航空发动机",
    "系统级总工程师",
    "理论物理学家",
    "《生活大爆炸》（谢耳朵、霍华德）",
    "基因组工程",
    "歼20/F22/F35 设计师",
    "三峡工程"
   ],
   "working_keywords": [
    "误差",
    "磨合效应",
    "逆向工程",
    "探伤",
    "金相检验",
    "公问题",
    "私问题",
    "潜意识",
    "灵感",
    "初筛机制",
    "宁错杀勿放过"
   ]
  },
  "notes": "structure.divergence=true：text 尾部 chars 4749+ 的科学答集/家族答集为平台话题标签混入正文、lexical 未覆盖，已按正文如实读出并登记。P022 之后系作者自述 3.8K 赞后追加的段落，解读时须与前半区分；P023-P052 的追加内容不应当作前文赞同者的立场。"
 },
 "6468c318": {
  "analysis": {
   "question_context": "提问者问：香港为什么可以成为富豪聚集地？（Q001，属提问者语境）。作者先转述平台上的主流答案——香港有很多适合富豪的环境条件所以富豪多——并明确判定这是把方向想反了，随后提出相反因果：香港适合富豪的条件多，是因为香港事实上是一座富豪管理的城市；文中给出富豪资产占 GDP 比例的数据，讨论香港富豪派系单一、民主治理失效、房地产垄断与加租机制，最后给出和平过渡到真正港人治港的出路主张，并声明自己并不主张推翻寡头统治。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "转述主流答案的方向并判定其想反，提出香港事实上是富豪管理的城市。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P004",
      "P005"
     ],
     "summary": "引 2017 年彭博亿万富翁指数与 IMF 的 GDP 数据计算，称前十大富豪资产约相当于香港年 GDP 的 35%，并以只手遮天形容。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P006",
      "P007"
     ],
     "summary": "明确因果方向：富豪手里有重大实际权力，香港才变得特别适合富豪，而非相反。",
     "role": "claim"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P008",
      "P009",
      "P010",
      "P011"
     ],
     "summary": "香港不是富豪很多而是派系太少，缺制造业与知识产权业大亨；这类人会反对地产霸权，香港本可成为研发与品牌中心。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P012",
      "P013"
     ],
     "summary": "缺少多元利益诉求导致无法形成真正有效的民主治理，只是立场一致的寡头假装成 N 个独立代表；很大程度上是特定形式的寡头体制。",
     "role": "conclusion"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P014",
      "P015"
     ],
     "summary": "转入随便聊聊，并声明不是在主张推翻寡头统治；社会有自己的历史路径，强力迫使巨轮转弯如同安排它撞冰山。",
     "role": "qualification"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P016",
      "P017"
     ],
     "summary": "长远唯一出路是和平过渡到真正的港人治港体制；现体制失效、成为选帝侯体制；极少数集团以房地产垄断和加租绑架经济。",
     "role": "claim"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P018",
      "P019"
     ],
     "summary": "祸乱之源不是大陆也不是被深圳取代；香港地缘优势仍不可取代、前途不可限量，但目前陷入僵局。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P020",
      "P021",
      "P022"
     ],
     "summary": "破局上上策是寄望香港人民在思想、意志、组织上成熟；最上策是真正港人治港取代港豪治港；若实现则五十年期限到达后特区也可能延续。",
     "role": "action_advice"
    },
    {
     "unit_id": "U010",
     "paragraph_refs": [
      "P023"
     ],
     "summary": "希望香港人自己及早看明白这一点。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "被作者反驳的主流答案：香港有很多适合富豪的环境条件，所以富豪多（即香港的环境造就了富豪）。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "主流答案把方向想反了：不是香港很适合富豪所以才有富豪，而是富豪手里有重大实际权力，香港才变得特别适合富豪。",
     "evidence": [
      "E2",
      "E6"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "香港适合富豪的条件多，是因为香港事实上是一座富豪管理的城市，这种高度亲富豪的环境是富豪们亲手塑造的结果。",
     "evidence": [
      "E3",
      "E5"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "asserted",
     "statement": "据 2017 年彭博亿万富翁指数和 IMF 的 GDP 统计数据计算，香港前十大富豪的个人资产总量约相当于香港年 GDP（3414 亿美元）的 35%。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "香港不是富豪很多，而是富豪太少；少不是数量太少而是派系太少，缺制造业大亨与知识产权业大亨。",
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
     "statement": "缺少多元利益诉求使香港无法形成真正有效的民主治理，只是同样几个立场几乎一致的寡头各自分出八只手、假装有 N 个独立代表。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "香港在很大程度上只是走了特定形式的寡头体制。",
     "evidence": [
      "E10"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "negated",
     "statement": "作者声明自己不是在主张推翻寡头统治；任何社会都有自己的历史路径，想要强力迫使巨轮转弯，净效果如同安排它撞冰山。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "长远看香港想要摆脱现有下滑轨迹，唯一的选择是和平过渡到真正的港人治港体制；十大富豪等位 35% GDP 不正常，现行体制已失效并成为实质的选帝侯体制。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "极少数人员集团通过不受管控的房地产垄断绑架香港经济，一句加租就能将一切增长据为己有，也能掀起民意使立法与行政改变权力结构的行动归于无有。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "香港祸乱之源是上述结构，不是大陆，也不是所谓被深圳取代。",
     "evidence": [
      "E14"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "香港的地缘优势仍然不可取代、前途仍不可限量，但目前实际上陷入僵局。",
     "evidence": [
      "E15"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "破局的上上策是寄望真正关注自身命运的香港人民在思想、意志、组织上成熟起来；最上策是实现真正的港人治港，取代港豪治港。",
     "evidence": [
      "E16",
      "E17"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "如果真正港人治港的愿景得以实现，则五十年期限就算到了，香港特区也可能继续作为健康的安排延续下去。",
     "evidence": [
      "E18"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "希望香港人自己及早看明白这一点。",
     "evidence": [
      "E19"
     ]
    }
   ],
   "argument_steps": [
    "转述并否定（P001-P002）：主流答案认为环境条件造就富豪，作者判定方向想反。",
    "正面命题（P003）：香港适合富豪的条件多，是因为香港事实上是富豪管理的城市。",
    "数据支撑（P004-P005）：2017 彭博亿万富翁指数与 IMF 的 GDP 数据算得前十大富豪资产约当香港年 GDP 的 35%。",
    "因果重述（P006-P007）：亲富豪环境是富豪亲手塑造；富豪掌握实际权力在先。",
    "反例与类比（P008-P010）：香港富豪并不多，兜兜转转全是几大豪门及其附庸；如把盖茨所有亲戚算成亿万富翁也会觉得他家有很多富豪。",
    "结构分析（P011）：真正的问题是派系太少，缺制造业与知识产权业大亨，香港本可成为全球研发与品牌中心。",
    "政治后果（P012-P013）：缺少多元利益诉求则无真正有效民主治理，只是寡头分饰多角；很大程度上是寡头体制。",
    "让步与自我限定（P014-P015）：不是主张推翻寡头统治；历史路径不可强扭，强扭如同撞冰山。",
    "出路判断（P016-P017）：唯一选择是和平过渡到真正港人治港；现行体制失效、成为选帝侯体制；房地产垄断与加租机制是症结。",
    "排除替代解释（P018-P019）：祸乱之源不是大陆、不是被深圳取代；地缘优势仍在，只是陷入僵局。",
    "行动主张与条件（P020-P022）：上上策是香港人民成熟，最上策是真正港人治港；若实现则五十年后特区仍可延续。",
    "收束（P023）：希望香港人及早看明白。"
   ],
   "concept_usage": [
    {
     "term": "富豪管理的城市",
     "meaning": "香港的实际权力掌握在富豪手中，因而城市环境被塑造成高度亲富豪；这是作者对香港性质的概括。",
     "evidence": "P003",
     "ambiguity": "作者未界定权力的具体范围与机制。"
    },
    {
     "term": "只手遮天",
     "meaning": "借以形容前十大富豪资产占年 GDP 约 35% 所体现的经济支配力。",
     "evidence": "P005",
     "ambiguity": "为口语化修辞，非分析概念。"
    },
    {
     "term": "派系太少",
     "meaning": "富豪数量不是问题，缺少制造业大亨与知识产权业大亨等能反对地产霸权的多元利益集团才是问题。",
     "evidence": "P011",
     "ambiguity": "作者以香港品牌举例，未给出派系数量的衡量标准。"
    },
    {
     "term": "选帝侯体制",
     "meaning": "作者用来指称极少数立场一致的人员集团实际决定权力归属的失效体制。",
     "evidence": "P016",
     "ambiguity": "术语来源与严格定义本文未说明。"
    },
    {
     "term": "港豪治港",
     "meaning": "作者对现状的称呼，与真正的港人治港相对，指豪门主导的治理。",
     "evidence": "P021",
     "ambiguity": "与港人治港的边界本文未给出制度性标准。"
    },
    {
     "term": "加租",
     "meaning": "房地产垄断者据以将经济增长据为己有、并动员民意阻止权力结构改变的手段。",
     "evidence": "P017",
     "ambiguity": "作者未给出具体案例或数据。"
    }
   ],
   "examples_and_targets": [
    "平台上的大部分答案（P001）：被转述并反驳的观点。",
    "2017 年彭博亿万富翁指数与 IMF 的 GDP 统计数据、3414 亿美元（P004）：作者引用数据（待外部核查）。",
    "比尔·盖茨及其亲戚的假想类比（P009、P010）：作者类比，用以说明富豪数量与家族附庸的混淆。",
    "香港几大豪门及其附庸（P008）：作者对结构的描述。",
    "屈臣氏与香港品牌（银行、保险公司、地产企业）（P011）：作者例证。",
    "泰坦尼克号巨轮与冰山（P015）：作者类比，说明不可强扭历史路径。",
    "大陆与被深圳取代（P018）：被作者否定的两种归因（反驳对象）。",
    "真正的港人治港与港豪治港（P021）：作者的出路主张。",
    "五十年期限（P022）：作者讨论的时间条件。"
   ],
   "conditions": [
    "作者明确否定的推论方向：不要把本文读成主张推翻寡头统治（P015）。",
    "转型方式限定：转弯只能慢慢来，强力迫使转弯净效果如同撞冰山（P015）。",
    "时间限定：摆脱下滑轨迹是长远看的判断，且用唯一的选择作强断言（P016）。",
    "假设条件：如果真正港人治港的愿景得以实现，五十年期限到达后特区也可能延续（P022）。",
    "程度限定：它在很大程度上只是走了特定形式的寡头体制（P013）。",
    "数据限定：35% 为作者依据 2017 年彭博指数与 IMF 的 GDP 数据计算，口径与算法本文未展开（P004）。"
   ],
   "rhetoric_and_tone": "短段落、断言式推进，直接判定主流答案把方向想反了；以你们体会一下、什么叫作只手遮天作反问式感叹；比喻鲜明（泰坦尼克转弯与撞冰山、寡头各自分出八只手假装 N 个独立代表、选帝侯体制）；以随便聊聊标示语气转换；结尾用希望香港人自己及早的看明白这一点作训诫式收束；政治判断用词强烈（祸乱之源、活见鬼的、绑架、失效）。",
   "unresolved_questions": [
    "彭博亿万富翁指数与 IMF 的 GDP 数据、3414 亿美元与 35% 的比例计算方法与口径，需外部核查。",
    "选帝侯体制这一术语的来源与严格含义，本文未说明。",
    "和平过渡到真正港人治港的具体路径、主体与时间表，本文未说明。",
    "被深圳取代所指的具体说法与出处，本文未说明。",
    "几大豪门及附庸的具体所指未被点名，属概括性描述。",
    "香港地缘优势仍不可取代的判断依据与衡量标准，本文未说明。",
    "五十年期限延续的条件（除真正港人治港外）本文未说明。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "大部分的答案都是说“香港有很多适合富豪的环境条件，所以富豪多”。",
     "relation": "context"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "这是恰恰把方向想反了。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "是因为香港事实上是一座富豪管理的城市。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "香港前十大富豪的个人资产总量约相当于香港年GDP（3414亿美元）的35%。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P006",
     "quote": "是因为这是富豪们亲手塑造的结果。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P007",
     "quote": "是因为富豪手里有重大的实际权力，所以香港才变得特别适合富豪，而不是香港很适合富豪所以才有富豪。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P008",
     "quote": "事实上，香港的富豪并不多。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P011",
     "quote": "香港不是“富豪很多”，而是富豪太少。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P012",
     "quote": "缺少多元利益诉求，香港无法形成真正有效的民主治理。",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P013",
     "quote": "它在很大程度上只是走了特定形式的寡头体制。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P015",
     "quote": "不要认为我现在是在主张“推翻寡头统治”。",
     "relation": "qualifies"
    },
    {
     "key": "E12",
     "paragraph_id": "P016",
     "quote": "唯一的选择是和平过渡到真正的港人治港体制。",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P017",
     "quote": "他们只要一句“加租”就能将一切增长据为己有。",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P018",
     "quote": "这才是香港祸乱之源，不是大陆，也不是什么活见鬼的“被深圳取代”。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P019",
     "quote": "香港的地缘优势仍然是不可取代的，前途仍然是不可限量的",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P020",
     "quote": "破局的上上策，反而是寄望于真正懂得关注自身命运的香港人民",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P021",
     "quote": "以真正的港人治港取代“港豪治港”",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P022",
     "quote": "则五十年期限就算到了，香港特区也可能继续作为健康的安排延续下去。",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P023",
     "quote": "希望香港人自己及早的看明白这一点。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "政治经济学",
    "香港社会与治理",
    "房地产与城市",
    "时事评论"
   ],
   "issue_candidates": [
    "香港富豪聚集的成因",
    "寡头体制与民主治理失效",
    "房地产垄断与加租机制",
    "港人治港与五十年期限",
    "香港祸乱归因"
   ],
   "text_function_candidates": [
    "答疑",
    "评论",
    "批评",
    "论辩"
   ],
   "object_candidates": [
    "香港",
    "香港前十大富豪",
    "彭博亿万富翁指数",
    "IMF",
    "比尔·盖茨",
    "屈臣氏",
    "泰坦尼克号",
    "大陆",
    "深圳"
   ],
   "working_keywords": [
    "只手遮天",
    "寡头体制",
    "选帝侯体制",
    "加租",
    "地产霸权",
    "港人治港",
    "港豪治港",
    "五十年期限",
    "制造业大亨",
    "知识产权业大亨"
   ]
  },
  "notes": "本篇无图片、无 text/lexical divergence。文中 2017 年彭博亿万富翁指数与 IMF 数据、3414 亿美元与 35% 比例为作者引述并自行计算，列为待外部核查；对香港体制的判断为作者评论性主张，非本文可核验事实。"
 },
 "dfd1dd77": {
  "analysis": {
   "question_context": "提问者问：如何看待现在的作战机械人无用论？（Q001，属提问者转述的流行观点，不得归给作者）。作者以反问开篇直接反驳无用论，主张大量传统装备可由机械驾驶员驾驶而成为纯无人装备，并称这是人形军用（工业）机器人最正当的用途；随后给出人形机器人可通用人类既有设施这一理由，反证不采用人形方案会导致双版本与兼容问题，并补充军方会保留人类操作者、以及控制系统受干扰时的风险限定。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002"
     ],
     "summary": "以反问否定作战机械人无用论，提出大量传统装备可由机械驾驶员驾驶成为纯无人装备，并称这是人形军用（工业）机器人最正当的用途。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P003",
      "P004"
     ],
     "summary": "替代人类士兵的最好设计就是人形机器人，因为其可通用本来为人类准备的设施；这对延长装备服役周期、降低研发成本、推动人机代际替换是很好甚至必然的方案。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P005"
     ],
     "summary": "反证：否则装备要设计两个版本且不能不经改装转换用途，每种为人准备的设施与机械由机器人接手都要专门设计物理界面，且很容易与人类使用者不兼容。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P006"
     ],
     "summary": "预测军方几乎肯定会保持这些装备仍然对人类操作者可用，否则开发费用太高。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P007"
     ],
     "summary": "风险限定：万一存在对控制系统的干扰（如 EMP 冲击或卫星天网坠落）而人类已被排除出作战体系，将面对战略上的绝望。",
     "role": "qualification"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "questioned",
     "statement": "被作者反驳的流行观点：现在的作战机械人无用（该说法见于提问字段 Q001，作者以反问质疑之）。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "大量传统装备可以由机械驾驶员驾驶而成为纯无人装备；这是人形军用（工业）机器人最正当的用途。",
     "evidence": [
      "E1",
      "E2"
     ]
    },
    {
     "claim_id": "C003",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "替代人类士兵的最好设计就是人形机器人，因为人形机器人显而易见的可以通用本来为人类准备的设施。",
     "evidence": [
      "E3"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "人形方案对于有效延长装备服役周期、降低研发成本、推动人机代际替换，其实是很好的甚至是必然的方案。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "不采用人形通用方案则装备都要设计两个版本且不能不经改装转换用途，为人准备的设施与机械交由机器人接手都要专门设计物理界面，并很容易与人类使用者不兼容。",
     "evidence": [
      "E5",
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "军方几乎肯定会保持这些装备仍然对人类操作者可用，否则开发费用太高。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "hypothetical",
     "statement": "万一存在某种对控制系统的干扰（譬如 EMP 冲击或卫星天网坠落）而人类已被从作战体系中排除，将会面对战略上的绝望。",
     "evidence": [
      "E8",
      "E9"
     ]
    }
   ],
   "argument_steps": [
    "反问否定（P001）：谁说无用？随即给出替代判断——传统装备可由机械驾驶员驾驶成为纯无人装备。",
    "定性（P002）：这是人形军用（工业）机器人最正当的用途。",
    "正面理由（P003）：人形机器人可通用本来为人类准备的设施，故是替代人类士兵的最好设计。",
    "扩展结论（P004）：对延长服役周期、降低研发成本、人机代际替换而言是很好甚至必然的方案。",
    "反证（P005）：否则需要两个版本、专门设计物理界面，且容易与人类使用者不兼容。",
    "预测（P006）：军方几乎肯定会保持装备对人类操作者可用，原因是开发费用。",
    "风险限定（P007）：控制系统被干扰而人类已被排除时，将面对战略上的绝望。"
   ],
   "concept_usage": [
    {
     "term": "纯无人装备",
     "meaning": "由机械驾驶员驾驶原本为人操作设计的传统装备，从而不再需要乘员。",
     "evidence": "P001",
     "ambiguity": "机械驾驶员的技术形态与自主程度本文未说明。"
    },
    {
     "term": "人形军用（工业）机器人",
     "meaning": "外形与操作方式对接人类既有设施与装备的机器人，作者认为其价值在于通用性而非外形本身。",
     "evidence": "P002",
     "ambiguity": "括号并列军用与工业，两者要求是否相同本文未说明。"
    },
    {
     "term": "物理界面",
     "meaning": "机器人与人用设施对接时需专门设计的接口；不通用会带来兼容问题。",
     "evidence": "P005",
     "ambiguity": "作者未给出具体界面事例。"
    },
    {
     "term": "战略上的绝望",
     "meaning": "控制系统受干扰且人类已被排除出作战体系时的处境。",
     "evidence": "P007",
     "ambiguity": "为作者的修辞性判断，未给出推演。"
    }
   ],
   "examples_and_targets": [
    "作战机械人无用论（Q001）：被反驳的流行观点。",
    "传统装备与机械驾驶员（P001）：作者主张中的对象。",
    "为人准备的设施与机械（P003、P005）：作者理由与反证中的对象。",
    "EMP 冲击、卫星天网坠落（P007）：作者举例说明可能的控制系统干扰。",
    "军方（P006）：作者预测其决策行为的机构。"
   ],
   "conditions": [
    "作者预测带几乎肯定这一限定，属预测性判断而非确定结论（P006）。",
    "风险情形以万一存在某种对控制系统的干扰为前提，属假设条件（P007）。",
    "人形方案的价值限定在通用人类既有设施这一理由上，而非泛泛主张人形优越（P003）。",
    "P004 以其实作限定，表明为作者的权衡判断。"
   ],
   "rhetoric_and_tone": "极简短篇，开篇即以反问谁说无用？直接否定提问所预设的流行观点；随后条列式给出理由与反证，用显而易见的、几乎肯定等词加强判断；末段以战略上的绝望作重词警示；无称呼语、无调侃，语气为简洁的论辩与判断。",
   "unresolved_questions": [
    "作战机械人无用论的具体论者与论据，本文未复述，需回查 Q001 原问题。",
    "EMP 冲击与卫星天网坠落的具体场景、来源与可能性，本文未说明。",
    "机械驾驶员的技术形态、自主等级与可靠性，本文未给出指标或实例。",
    "军方几乎肯定会保持人类可用的判断依据，本文未给出数据或文件来源。",
    "brief 字段在语料中呈截断（止于其实是很），正文 P004 为完整句，已以正文为准。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "谁说无用？大量的传统装备可以由机械驾驶员驾驶而成为纯无人装备。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "这是人形军用（工业）机器人最正当的用途。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "替代人类士兵的最好设计就是人形机器人",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "其实是很好的甚至是必然的方案。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P005",
     "quote": "否则装备就都要设计两个版本",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P005",
     "quote": "而且很容易就会与人类使用者不兼容。",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P006",
     "quote": "军方几乎肯定会保持这些装备仍然对人类操作者可用",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P007",
     "quote": "万一存在某种对控制系统的干扰",
     "relation": "qualifies"
    },
    {
     "key": "E9",
     "paragraph_id": "P007",
     "quote": "将会面对战略上的绝望。",
     "relation": "qualifies"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "军事装备",
    "机器人与自动化",
    "国防工业"
   ],
   "issue_candidates": [
    "作战机械人无用论",
    "人形机器人的军用价值",
    "装备通用性与双版本成本",
    "人机代际替换",
    "控制系统受干扰风险"
   ],
   "text_function_candidates": [
    "答疑",
    "论辩",
    "评论"
   ],
   "object_candidates": [
    "人形军用（工业）机器人",
    "机械驾驶员",
    "传统装备",
    "军方",
    "EMP",
    "卫星天网"
   ],
   "working_keywords": [
    "纯无人装备",
    "机械驾驶员",
    "通用设施",
    "物理界面",
    "代际替换",
    "EMP冲击",
    "战略上的绝望"
   ]
  },
  "notes": "本篇无图片、无 text/lexical divergence。brief 字段在语料中呈截断（止于其实是很），正文 P004 为完整句，记录以正文为准。作者对军方行为的判断为预测性表述，已按 predicted 记录。"
 },
 "16c53ed9": {
  "analysis": {
   "question_context": "提问者问：购房选择大平层还是联排别墅？（Q001）。作者先否定两个选项——其实都不舒服——转而建议选择定位高一些的普通格局小区并关注车位比例与物业费，主张把资源从享受性消费转向学与文化阅历，进而展开家族财富、慈善与传承的训诫：被抬高的享受水平是负资产，慈善是经常性事务，能有效捐赠多少才决定能持有多少，富而能俭才是平安之相。P021 起为作者自述的增补，专门回应评论区里人家不过是想舒服一点的说法，以 1200 万别墅为例逐项算账。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001",
      "P002",
      "P003"
     ],
     "summary": "否定两个选项（都不舒服），建议定位高一些的普通格局小区、看车位比例和物业费，并以大隐隐于市、莫隐于野作结。",
     "role": "conclusion"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P004",
      "P005",
      "P006",
      "P007"
     ],
     "summary": "主张衣食住安于一般中产阶级水准而只在学上重金投入，豪奢应用在跨古今中外的文化阅历上；被抬高的享受水平是千秋万代的负资产，享受导致贪婪、愚蠢、疯狂与败亡。",
     "role": "claim"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P008",
      "P009",
      "P010",
      "P011",
      "P012"
     ],
     "summary": "慈善是行有余力者的经常性事务，能有效捐赠多少决定可持有多少；慈善对象首先是团队员工、客户、供应商、社群与可造之才；利润率过高危险，被认定为隐患就无法踏入真正的顶层。",
     "role": "reason"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P013",
      "P014",
      "P015",
      "P016",
      "P017"
     ],
     "summary": "富而能俭才是平安之相；驳自高身份好做生意的托辞；界定生意是与不知道你是谁的人做的；不要开豪车、穿戴豪华珠宝（反问保镖便宜么）。",
     "role": "action_advice"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P018",
      "P019",
      "P020"
     ],
     "summary": "门当户对之问与家族相关回答的合集链接；家族答集为平台话题标签，lexical 未覆盖该片段。",
     "role": "transition"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P021",
      "P022",
      "P023",
      "P024",
      "P025",
      "P026",
      "P027",
      "P028",
      "P029",
      "P030"
     ],
     "summary": "增补回应评论区想舒服一点之说：以 1200 万别墅逐项算账，对比送家族成员留学读博、资助游历与按 5% 年利长住酒店，并指出当事人买别墅只是偶尔睡觉。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P031",
      "P032"
     ],
     "summary": "中国 99% 的别墅主人不知道该怎么住别墅，把别墅区住成了加强版城中村；培育优秀可靠的仆佣团队对生活水平的意义远高于买大房子。",
     "role": "conclusion"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "大平层与联排别墅其实都不舒服。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "建议选择定位高一些的普通格局小区，看车位比例和物业费就好；大隐隐于市，莫隐于野。",
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
     "statement": "更好的选择是在衣食住方面安于一般中产阶级的生活形态和水准，只在学方面投入重金，因为学本身是个无底洞。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "要豪奢应豪奢在跨越古今中外的文化阅历上，不该豪奢在各种享受性的体验上；这方面的投入是绝对的正资产，可传承百代、永远有益于家族后代。",
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
     "statement": "被抬高的享受水平是千秋万代的负资产：由奢入俭难会代代相传，日日一睁眼就欠下一份钱粮。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "享受导致贪婪，贪婪催生愚蠢，愚蠢造成疯狂，疯狂指向败亡。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "慈善事业对行有余力的人是一项经常性事务；一个人能有效捐赠多少，才决定ta可以持有多少，二者有强烈正相关。",
     "evidence": [
      "E9",
      "E10"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "慈善不只是指山里的穷苦人家，还首先包括团队与员工、客户、供应商、所在社群、聪明正直可堪造就的年轻人、不遇的逸才、固穷的君子等。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "落袋为安的利润率过高是非常危险的（不是不妥而是危险）；即便不谈道德，仅从对冲财富危害的现实主义角度，慈善类支出也是绝对必须的。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "被认定为那种隐患就不可能踏入真正的顶层；没有脱出轮回就永有堕落之忧，若一直不跳出红尘之外，衰败不过是早晚的事。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "若如此，大平层还是别墅都不过是歧路的入口；富而能俭，才是平安之相。",
     "evidence": [
      "E14"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "自高身份好做生意之类的托辞最好不要提起；要靠这个才能做成的生意最好干脆不要做，到头一场空。",
     "evidence": [
      "E15"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "生意是和不知道你是谁的人做的才叫生意；从陌生人手里赚到的才是真利润，否则不过是信用抵押贷款。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "不要开豪车，不要穿戴豪华珠宝；并以反问暗示这样做会抬高人身安全成本（难道你是嫌保镖很便宜么）。",
     "evidence": [
      "E17",
      "E18"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "以 1200 万一套别墅为口径算账：按一人 300 万够送 4 人去美国读博、按一人 80 万够送 15 人去德国读博、按一人 10 万够送 120 人在国内读重点本科或硕士、按 4 万每人次够资助 300 次出国游历；按年利 5% 计息则每年 60 万利息可长住上海东方文华酒店。",
     "evidence": [
      "E19",
      "E20",
      "E21",
      "E22"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "中国 99% 的别墅主人根本不知道应该怎么住别墅，把别墅区住成了加强版城中村，很多人没有构建有效的仆佣团队，反把家人父母住成清洁工。",
     "evidence": [
      "E23"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "培育优秀可靠的仆佣团队在提高生活水平上的意义要远远高于买大房子。",
     "evidence": [
      "E24"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "asserted",
     "statement": "被作者增补回应的评论区观点：人家不过是想舒服一点。",
     "evidence": [
      "E25"
     ]
    }
   ],
   "argument_steps": [
    "直接否定选项（P001）：其实都不舒服。",
    "替代建议（P002-P003）：定位高一些的普通格局小区，看车位比例与物业费；大隐隐于市，莫隐于野。",
    "资源重配主张（P004）：衣食住安于一般中产阶级水准，只在学上投入重金，学是无底洞。",
    "价值排序（P005）：豪奢应用于跨古今中外的文化阅历，不应用于享受性体验；此类投入是正资产。",
    "传承推论（P006-P007）：一代有眼界则代代有眼界；抬高的享受水平是负资产，享受—贪婪—愚蠢—疯狂—败亡连锁。",
    "慈善论（P008-P010）：慈善是经常性事务；能有效捐赠多少决定可持有多少；慈善对象首先是身边与社群中的人。",
    "风险论（P011-P012）：利润率过高危险；被认定为隐患则无法进入顶层，衰败早晚之事。",
    "收束判断（P013）：富而能俭才是平安之相，大平层与别墅都不过是歧路入口。",
    "驳托辞与界定（P014-P015）：驳自高身份好做生意的说法，界定生意是与陌生人做的。",
    "行为禁令（P016-P017）：不要开豪车、不要穿戴豪华珠宝，反问保镖成本。",
    "平台链接（P018-P020）：门当户对之问与家族答集合集（含未覆盖片段）。",
    "增补算账（P021-P030）：回应想舒服一点之说，用 1200 万别墅的机会成本对比留学、游历与酒店长住，并反问代价是否太高。",
    "补论（P031-P032）：多数别墅主人不会住别墅，仆佣团队的意义高于买大房子。"
   ],
   "concept_usage": [
    {
     "term": "学",
     "meaning": "作者指对老师、指点、联系与跨古今中外文化阅历的投入；被描述为万分花钱、无底洞，但属可传承的正资产。",
     "evidence": "P004",
     "ambiguity": "具体支出项目与边界在文中以引号强调，未逐项界定。"
    },
    {
     "term": "负资产",
     "meaning": "被抬高的享受水平：由奢入俭难使其代代产生支出与风险。",
     "evidence": "P007",
     "ambiguity": "为作者的价值判断用语，非会计定义。"
    },
    {
     "term": "慈善",
     "meaning": "行有余力者的经常性事务，包括对团队、员工、客户、供应商、社群与可造之才的支持；被论证为持有财富的条件与对冲风险的手段。",
     "evidence": "P010",
     "ambiguity": "作者同时给出道德理由与现实主义理由，二者关系未细究。"
    },
    {
     "term": "落袋为安",
     "meaning": "作者引号借用的说法，指把利润率尽量留在自己手中；作者判定过高则危险。",
     "evidence": "P011",
     "ambiguity": "何为过高，本文未给阈值。"
    },
    {
     "term": "轮回",
     "meaning": "作者用以指财富与家族未能脱出衰败循环的状态。",
     "evidence": "P012",
     "ambiguity": "带宗教/哲思色彩，未作定义。"
    }
   ],
   "examples_and_targets": [
    "大平层与联排别墅（Q001、P001、P013）：提问选项，被作者否定。",
    "定位高一些的普通格局小区、车位比例、物业费（P002）：作者建议对象。",
    "好的老师、文明遗址与博物馆、核心利益伙伴（P004）：作者例证。",
    "山里的穷苦人家、团队和员工、客户、供应商、社群、不遇的逸才、固穷的君子、落难的义人、未起的豪杰（P010）：作者对慈善对象的列举。",
    "豪车、豪华珠宝、保镖（P016、P017）：作者行为禁令与反问材料。",
    "1200 万一套的别墅及当事人（P022、P028）：增补段的算账对象与批评对象。",
    "美国留学读博 300 万、德国 80 万、国内重点本科或硕士 10 万、出国游历 4 万每人次（P023-P026）：作者给出的价格假设。",
    "年利 5%、上海东方文华酒店一天 1200（P027）：作者算账假设与例证。",
    "中国 99% 的别墅主人、加强版城中村、被住成清洁工的家人父母（P031）：作者的观察性断言（待外部核查）。",
    "家族答集（P020）：平台话题/收藏夹标签混入正文。"
   ],
   "conditions": [
    "慈善主张的前提限定：对象是行有余力的人（P008）。",
    "一代有眼界则代代有眼界的推论带正常而言这一限定（P006）。",
    "算账结论依赖作者给出的单价假设：一人 300 万、80 万、10 万、4 万每人次（P023-P026）。",
    "利息结论依赖按年利 5% 计息的假设，且作者注明以上没算利息、若算上孳息数字还可大幅提高（P026、P027）。",
    "增补段的语境限定：专门回答评论区里的想舒服一点（P021），并非原始回答主体。",
    "99% 为作者的概括性比例断言，未给出统计来源，需外部核查（P031）。",
    "未脱出轮回则永有堕落之忧的论断以如果一直不跳出这红尘之外为条件（P012）。",
    "P029 的翻几倍回报以 15 个德国博士里有两三个成才为假设。"
   ],
   "rhetoric_and_tone": "训诫与箴言体，大量第二人称你/你的家族/你的子孙；先以其实都不舒服作斩截否定；格言式短句（大隐隐于市，莫隐于野；富而能俭，才是平安之相）；排比递进（享受导致贪婪，贪婪催生愚蠢，愚蠢造成疯狂，疯狂指向败亡）；反问施压（难道你是嫌保镖很便宜么？、舒服一点的代价有没有觉得太高？）；算账式量化对比把价值判断落为数字；用托辞、隐患、强盗的肉票钱等贬义措辞批评对象；增补段自述专门回答评论区，语气更直接。",
   "unresolved_questions": [
    "P018 什么才是门当户对？与 P020 家族答集为 text 中存在、lexical 未覆盖的片段，正文与结构不一致；家族答集属平台话题/收藏夹标签。",
    "中国 99% 的别墅主人不知道怎么住别墅这一比例需外部核查，本文未给出来源与调查口径。",
    "P023-P027 的留学费用、酒店房价、年利 5% 等数字为作者举例口径，未注明时间、地区与出处。",
    "Q001 提问者的城市、预算、家庭人口等具体条件正文未说明，作者给出的是通用建议。",
    "培育优秀可靠仆佣团队的具体方式、成本与可行性本文未说明。",
    "P001 都不舒服的判断依据（居住体验细节）本文未展开。",
    "P012 的顶层与轮回等表述未给出可操作定义，解释时需保留其修辞性。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "其实都不舒服。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "就定位高一些的普通格局小区就好了。看车位比例和物业费就好。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P003",
     "quote": "大隐隐于市，莫隐于野。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P004",
     "quote": "只在“学”方面投入重金。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P005",
     "quote": "你要豪奢，应该豪奢在这种跨越古今中外的文化阅历上，不该豪奢在各种享受性的体验上。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P005",
     "quote": "是可以传承百代永远有益于你的家族后代的",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P007",
     "quote": "而被抬高的享受水平是千秋万代的负资产。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P007",
     "quote": "享受导致贪婪，贪婪催生愚蠢，愚蠢造成疯狂，疯狂指向败亡。",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P008",
     "quote": "慈善事业对行有余力的人来说是一项经常性事务。",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P009",
     "quote": "一个人能有效的捐赠多少，才决定了ta可以持有多少。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P010",
     "quote": "还首先包括你的团队和员工、你的客户、你的供应商、你所在的社群",
     "relation": "supports"
    },
    {
     "key": "E12",
     "paragraph_id": "P011",
     "quote": "“落袋为安”的利润率过高是非常危险的",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P012",
     "quote": "被认定为这样的隐患，你就不可能踏入真正的顶层",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P013",
     "quote": "富而能俭，才是平安之相。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P014",
     "quote": "至于什么“自高身份好做生意”之类的托辞，最好不要提起。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P015",
     "quote": "生意生意，和不知道你是谁的人做的才叫生意。",
     "relation": "supports"
    },
    {
     "key": "E17",
     "paragraph_id": "P016",
     "quote": "不要开豪车，不要穿戴豪华珠宝。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P017",
     "quote": "难道你是嫌保镖很便宜么？",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P022",
     "quote": "算一套别墅值1200万",
     "relation": "context"
    },
    {
     "key": "E20",
     "paragraph_id": "P023",
     "quote": "按一人300万，这个“房子”的价钱够送家族成员4人去美国留学读到博士。",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P027",
     "quote": "按年利5%计息，1200万每年利息60万",
     "relation": "supports"
    },
    {
     "key": "E22",
     "paragraph_id": "P029",
     "quote": "那15个德国博士里有两三个成才，这1200万你也翻几倍拿回来了。",
     "relation": "supports"
    },
    {
     "key": "E23",
     "paragraph_id": "P031",
     "quote": "就会发现中国99%的别墅主人根本不知道应该怎么住别墅",
     "relation": "supports"
    },
    {
     "key": "E24",
     "paragraph_id": "P032",
     "quote": "而培育优秀可靠的仆佣团队在提高生活水平上的意义要远远的高于买大房子。",
     "relation": "supports"
    },
    {
     "key": "E25",
     "paragraph_id": "P021",
     "quote": "这一段是增补，专门回答评论区里的“人家不过是想舒服一点”",
     "relation": "context"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "家族财富与传承",
    "消费与居住选择",
    "慈善与财富伦理",
    "子女教育与文化资本"
   ],
   "issue_candidates": [
    "大平层与联排别墅的取舍",
    "教育投入与享受性消费的取舍",
    "由奢入俭难与负资产",
    "慈善支出与财富安全",
    "豪车珠宝与人身安全",
    "别墅居住方式与仆佣团队"
   ],
   "text_function_candidates": [
    "答疑",
    "经验总结",
    "训诫劝导",
    "算账论证",
    "增补回应"
   ],
   "object_candidates": [
    "大平层",
    "联排别墅",
    "中产阶级",
    "家族成员",
    "美国/德国留学",
    "上海东方文华酒店",
    "别墅区",
    "仆佣团队",
    "家族答集"
   ],
   "working_keywords": [
    "大隐隐于市",
    "由奢入俭难",
    "负资产",
    "正资产",
    "厚德载物",
    "落袋为安",
    "慈善",
    "门当户对",
    "信用抵押贷款",
    "加强版城中村"
   ]
  },
  "notes": "structure.divergence=true：text 中 P018 什么才是门当户对？与 P020 家族答集为 lexical 未覆盖片段（家族答集属平台话题/收藏夹标签混入正文），已按正文如实读出并登记。P021 起为作者自述的增补段，专门回应评论区想舒服一点之说，与原始回答主体区分记录。文中 99% 比例及各类费用数字均需外部核查。"
 },
 "f371ffd1": {
  "analysis": {
   "question_context": "提问者问：直升机可以飞到珠穆朗玛峰山顶然后把人放下吗？（Q001，属提问者语境）。作者判定并非绝对不可能但危险性相当大，随后逐条说明：高海拔下动力、自反扭矩与进气含氧量问题使事故概率大增且应变能力下降；珠峰用直升机需特殊设计且目前无厂家专攻；积雪地带难以着陆或绳降，风速与乱流使吊挂与回收不可行；常年积雪陡坡上直升机的噪音与反冲气流可能引发滑坡，属严重不道德；热气球不可行、氦气球升限够但风险极高。PS 段先发制人回应所谓直升机在珠峰顶着陆的视频，指出那只是起落架接触、旋翼未停机、不敢下人。正文含 3 个图片节点，图片内容未核验。",
   "content_units": [
    {
     "unit_id": "U001",
     "paragraph_refs": [
      "P001"
     ],
     "summary": "总判断：直升机登珠峰顶放人并非绝对不可能，但危险性相当大。",
     "role": "conclusion"
    },
    {
     "unit_id": "U002",
     "paragraph_refs": [
      "P002",
      "P003"
     ],
     "summary": "高海拔气压低使直升机需高转速，自反扭矩与尾桨负担加重、进气含氧量不足，事故概率提高；动力下降又使对抗横风乱流的能力下降，反应时间由一两秒变三四秒，吊挂人员被甩成大秋千。",
     "role": "reason"
    },
    {
     "unit_id": "U003",
     "paragraph_refs": [
      "P004"
     ],
     "summary": "珠峰用直升机需特殊设计，目前似乎无厂家专攻；不是没有直升机能飞到该高度，而是很难有信心安全绳降人员与器材。",
     "role": "conclusion"
    },
    {
     "unit_id": "U004",
     "paragraph_refs": [
      "P005",
      "P006",
      "P007",
      "P008",
      "P009"
     ],
     "summary": "着陆与垂降的具体困难：新雪下反冲气流扬雪影响视线并引起复杂气动问题；绳索垂降在湍急陌生高海拔空域相当危险；珠峰顶风速轻易可达90米/秒，钟摆难以停住；落地点不平整则飞机不敢触地，跳下与回收都不现实。",
     "role": "reason"
    },
    {
     "unit_id": "U005",
     "paragraph_refs": [
      "P010",
      "P011"
     ],
     "summary": "结论：玩直升机登珠峰的只是飞到峰顶高度悬停一下就下来，做不到两脚踩在实地看风景；并称徒步登顶的累积死亡率才19%。",
     "role": "conclusion"
    },
    {
     "unit_id": "U006",
     "paragraph_refs": [
      "P012",
      "P013",
      "P014"
     ],
     "summary": "第四点：常年积雪陡峭区域极端脆弱，直升机噪音与反冲气流有相当大概率引发积雪滑坡，属严重不道德；若压死下方登山者，作者认为当事人可能面临偿命。",
     "role": "rebuttal"
    },
    {
     "unit_id": "U007",
     "paragraph_refs": [
      "P015",
      "P016"
     ],
     "summary": "替代方案评估：热气球登珠峰目前是做梦（历史记录不过海拔6600米）；氦气球升限倒够，但以珠峰风力之猛算是创意自杀。",
     "role": "other"
    },
    {
     "unit_id": "U008",
     "paragraph_refs": [
      "P017",
      "P018"
     ],
     "summary": "分隔线与 PS 标记。",
     "role": "transition"
    },
    {
     "unit_id": "U009",
     "paragraph_refs": [
      "P019",
      "P020",
      "P021",
      "P022",
      "P023",
      "P024"
     ],
     "summary": "预先回应着陆视频之争：该视频作者已看过，所谓着陆只是起落架接触，旋翼未敢停机，飞机也不敢下人；须放一人落地站五分钟再接走才算完成测试；作者不认为绝对不可能，但相信死亡率不低于19%。",
     "role": "rebuttal"
    }
   ],
   "main_claims": [
    {
     "claim_id": "C001",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "直升机飞到珠峰山顶把人放下，要说是可能性当然不算不可能，但是这个危险性相当大。",
     "evidence": [
      "E1"
     ]
    },
    {
     "claim_id": "C002",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "海拔8848米处气压低，直升机需很高转速维持动力，自反扭矩增强、尾桨对抗任务更艰巨，事故可能性大大提高，而发动机进气含氧量却不足。",
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
     "statement": "动力下降使及时应变对抗横风与乱流的能力下降，原本一两秒可恢复平衡，现在可能需三四秒，吊挂人员会被甩成大秋千并可能撞岩壁或地面骨折。",
     "evidence": [
      "E4"
     ]
    },
    {
     "claim_id": "C004",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "在珠峰用直升机需特殊设计，目前似乎还没有厂家专攻该方向；不是没有直升机能飞到该高度，而是很难有直升机有信心在该条件下安全绳降人员与器材。",
     "evidence": [
      "E5"
     ]
    },
    {
     "claim_id": "C005",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "对积雪地带直升机最好绳索垂降，因为直接着陆若碰上新雪，螺旋桨反冲气流会使积雪飞舞、严重影响视线，雪在空气中含量过大还会引起复杂空气动力学问题。",
     "evidence": [
      "E6"
     ]
    },
    {
     "claim_id": "C006",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "绳索垂降在气流湍急而陌生的高海拔空域是相当危险的。",
     "evidence": [
      "E7"
     ]
    },
    {
     "claim_id": "C007",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "珠峰顶风速轻易可达90米/秒，在乱流中靠操纵停下钟摆的难度一般人难以想象；且峰顶要平整就一定有雪、要没雪就一定有险恶地形。",
     "evidence": [
      "E8"
     ]
    },
    {
     "claim_id": "C008",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "落地点不平整飞机根本不敢触地，弄不好尾桨触地后果严重；飞机不敢触地降落时，也无法从悬停的飞机上跳下去再跳回来。",
     "evidence": [
      "E9"
     ]
    },
    {
     "claim_id": "C009",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "asserted",
     "statement": "玩直升机登珠峰的只是飞到峰顶高度悬停一下就下来，根本做不到两脚踩在实地上看风景。",
     "evidence": [
      "E10"
     ]
    },
    {
     "claim_id": "C010",
     "claim_type": "author_reported",
     "attribution": "author",
     "modality": "asserted",
     "statement": "徒步登顶的累积死亡率才19%，现在已经低多了（作者引用的比较数据）。",
     "evidence": [
      "E11"
     ]
    },
    {
     "claim_id": "C011",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "常年积雪的陡峭区域极端脆弱敏感，直升机这种噪音大户前往是严重不道德的，其声浪与反冲气流有相当大概率引发积雪滑坡，可能一下压死十几二十个登山者。",
     "evidence": [
      "E12"
     ]
    },
    {
     "claim_id": "C012",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "predicted",
     "statement": "若以这种方式造成对方团队死亡，对方可能不讲法律，作者认为当事人搞不好是要偿命的。",
     "evidence": [
      "E13"
     ]
    },
    {
     "claim_id": "C013",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "用热气球登珠峰目前是做梦，历史记录不过海拔6600米；氦气球升限倒够，但以珠峰风力之猛也算是创意自杀。",
     "evidence": [
      "E14",
      "E15"
     ]
    },
    {
     "claim_id": "C014",
     "claim_type": "opponent_view",
     "attribution": "opponent",
     "modality": "questioned",
     "statement": "被作者预先反驳的意见：以那段直升机在珠峰顶着陆的视频为依据，认为直升机可以登顶（作者称已看过该视频并逐点反驳）。",
     "evidence": [
      "E16"
     ]
    },
    {
     "claim_id": "C015",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "negated",
     "statement": "所谓着陆只是起落架那一点接触；旋翼没敢停机，若停机尾桨铁定触地、飞机一定深陷积雪，并因坡面陡峭而翻滚下山。",
     "evidence": [
      "E17",
      "E18"
     ]
    },
    {
     "claim_id": "C016",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "那架直升机不敢下人：只要推开舱门破坏气动外形，时速189公里、温度低至-17～-41摄氏度的寒风就会造成严重后果。",
     "evidence": [
      "E19"
     ]
    },
    {
     "claim_id": "C017",
     "claim_type": "author_explicit",
     "attribution": "author",
     "modality": "asserted",
     "statement": "放一个人落地站五分钟再把ta接走，作者才认可算是完成了测试项目，并认为这不算对登顶过于苛刻的定义。",
     "evidence": [
      "E20"
     ]
    },
    {
     "claim_id": "C018",
     "claim_type": "author_qualified",
     "attribution": "author",
     "modality": "qualified",
     "statement": "作者不认为直升机登顶是绝对不可能的，但相信死亡率不会低于19%。",
     "evidence": [
      "E21"
     ]
    }
   ],
   "argument_steps": [
    "总判断（P001）：不算不可能，但危险性相当大。",
    "动力与气动理由（P002）：高海拔低气压要求高转速，自反扭矩与尾桨负担加重，进气含氧量不足，事故概率提高。",
    "操纵余度理由（P003）：动力下降使抗横风乱流能力下降，反应时间由一两秒变三四秒，吊挂人员成大秋千。",
    "现状判断（P004）：需特殊设计，无厂家专攻；难点在于是否有信心安全绳降而非能否飞到高度。",
    "着陆与垂降理由（P005-P009）：扬雪与视线、复杂气动、绳索垂降危险、90米/秒风速与钟摆、落地点必须平整、跳下与回收不现实。",
    "结论（P010-P011）：所谓登顶只是悬停一下，做不到落地看风景；死亡率过高，并以徒步累积死亡率19%作比较。",
    "道德反驳（P012-P014）：噪音与反冲气流可能引发滑坡，严重不道德；若致人死亡后果严重。",
    "替代方案（P015-P016）：热气球做梦，氦气球创意自杀。",
    "PS 预回应（P019-P024）：视频中的着陆只是起落架接触、旋翼未停机、不敢下人；须落地五分钟才算法标；最后重申非绝对不可能但死亡率不低于19%。"
   ],
   "concept_usage": [
    {
     "term": "自反扭矩",
     "meaning": "机身随旋翼旋转产生的反作用扭矩；高转速下增强，加重尾桨对抗负担。",
     "evidence": "P002",
     "ambiguity": "作者未给出数值或机型差异。"
    },
    {
     "term": "绳降/绳索垂降",
     "meaning": "直升机不接地而以绳索投放或回收人员器材的方式；作者认为在珠峰条件下相当危险。",
     "evidence": "P005",
     "ambiguity": "与直接着陆的适用条件以积雪与平整度划分。"
    },
    {
     "term": "钟摆/大秋千",
     "meaning": "吊挂在直升机下方的人员在乱流中被甩动的状态，难以靠操纵停住。",
     "evidence": "P007",
     "ambiguity": "为形象化描述，未作定量分析。"
    },
    {
     "term": "着陆",
     "meaning": "作者在 PS 段重新界定：视频中的着陆只是起落架接触，不等于可停机、可下人。",
     "evidence": "P020",
     "ambiguity": "作者对登顶着陆的严格定义（放人落地五分钟）是其自设标准。"
    },
    {
     "term": "道德（严重不道德）",
     "meaning": "作者用以评价在脆弱积雪区使用高噪音直升机、可能引发滑坡危及他人的行为。",
     "evidence": "P012",
     "ambiguity": "作者未给出责任或赔偿的制度性讨论，仅给出后果警告。"
    }
   ],
   "examples_and_targets": [
    "珠穆朗玛峰、海拔8848米、峰顶风速90米/秒（P002、P007）：作者论述对象与数据（待核查）。",
    "尾桨、发动机进气含氧量（P002）：作者技术论据。",
    "徒步登顶累积死亡率19%（P011）：作者引用的比较数据（待核查）。",
    "热气球历史记录海拔6600米、氦气球（P015、P016）：作者评估的替代方案（待核查）。",
    "某个直升机在珠峰顶着陆的视频及其起落架接触（P019、P020）：作者预先反驳的对象，且与文中图片相关。",
    "时速189公里、温度-17～-41摄氏度（P022）：作者引用的环境数据（待核查）。",
    "庐山升龙霸、达人秀、流星拳（P008、P009）：作者的调侃性修辞材料。",
    "图片节点 IMG001-IMG003（阅读包列出，未核验）：P020 的所谓上图即其中图片。"
   ],
   "conditions": [
    "作者在开篇保留让步：要说是可能性，当然不算不可能（P001）。",
    "现状判断带不确定限定：目前似乎还没有哪家直升机厂家在专攻这个方向（P004）。",
    "技术推断带条件：如果它敢停机、只要它敢推开舱门（P021、P022）。",
    "风速论断为轻易可达而非恒定值，且以珠峰风力之猛为前提（P007、P016）。",
    "作者对登顶的认可标准为自设条件：放一个人落地站五分钟再把人接走（P023）。",
    "末段结论以我相信标记为作者信念，并给出死亡率不低于19%的下限式判断（P024）。",
    "P003 以如果只是骨折的话作反讽式限定。",
    "P002 提到这个已经说过了，指向本文之外的既有讨论，本批次内不含该上下文。"
   ],
   "rhetoric_and_tone": "以第二人称你贯穿，语气辛辣调侃与警告并用：连续反问（你敢直接从悬停的飞机上往下跳吗？跳了你要怎么跳回来呢，庐山升龙霸吗？、你拿什么赔？）；黑色幽默（你最好兜里已经装了写好的遗言，这时候现写钢笔都不出水了；被湍流舞动的绳头的配重一招流星拳打死的机会更大；为什么风险这个词会跟风姓；创意自杀）；以第三、第四作分点推进；用噪音大户、空中拖拉机作贬称；道德批评段落转严厉（严重不道德的、搞不好是要偿命的）；PS 段以先声明一声先发制人，防止抬杠者以视频反驳。",
   "unresolved_questions": [
    "本篇含 3 个图片节点（IMG001-IMG003），图片内容未经核验，需人工/多模态复核。",
    "P020 的所谓上图这里这点起落架接触依赖图片，正文文本无法确认图中所指。",
    "徒步登顶累积死亡率19%及其现在已经低多了需外部核查，来源未给出。",
    "峰顶风速90米/秒、时速189公里、温度-17～-41摄氏度、热气球历史记录6600米等数值需外部核查，来源均未给出。",
    "作者所指的直升机在珠峰顶着陆视频的具体事件、时间、机型与拍摄方，本文未说明。",
    "P023 所述测试项目的定义方与出处，本文未说明，属作者自设标准。",
    "P002 的这个已经说过了指向本文之外的讨论，本批次内无法取得该上下文。"
   ],
   "evidence": [
    {
     "key": "E1",
     "paragraph_id": "P001",
     "quote": "要说可能性，当然不算不可能，但是这个危险性相当大。",
     "relation": "supports"
    },
    {
     "key": "E2",
     "paragraph_id": "P002",
     "quote": "尾桨在空气稀薄的条件下的对抗任务也就更艰巨。",
     "relation": "supports"
    },
    {
     "key": "E3",
     "paragraph_id": "P002",
     "quote": "你的发动机进气含氧量却不足，更是雪上加霜。",
     "relation": "supports"
    },
    {
     "key": "E4",
     "paragraph_id": "P003",
     "quote": "现在要扳平可能就要三四秒。",
     "relation": "supports"
    },
    {
     "key": "E5",
     "paragraph_id": "P004",
     "quote": "而是说很难有直升机在这个条件下有信心安全的绳降人员、器材。",
     "relation": "supports"
    },
    {
     "key": "E6",
     "paragraph_id": "P005",
     "quote": "螺旋桨巨大的反冲气流会导致积雪飞舞，严重影响视线",
     "relation": "supports"
    },
    {
     "key": "E7",
     "paragraph_id": "P006",
     "quote": "而偏偏绳索垂降在气流湍急而陌生的高海拔空域是相当危险的。",
     "relation": "supports"
    },
    {
     "key": "E8",
     "paragraph_id": "P007",
     "quote": "轻易可达90米/秒",
     "relation": "supports"
    },
    {
     "key": "E9",
     "paragraph_id": "P008",
     "quote": "因为落地点不平整，飞机根本不敢触地。",
     "relation": "supports"
    },
    {
     "key": "E10",
     "paragraph_id": "P010",
     "quote": "根本做不到两脚踩在实地上看风景。",
     "relation": "supports"
    },
    {
     "key": "E11",
     "paragraph_id": "P011",
     "quote": "毕竟徒步登顶的累积死亡率才19%，现在已经低多了。",
     "relation": "context"
    },
    {
     "key": "E12",
     "paragraph_id": "P012",
     "quote": "直升机这种噪音大户前往这些区域是严重不道德的。",
     "relation": "supports"
    },
    {
     "key": "E13",
     "paragraph_id": "P014",
     "quote": "到时候人家不跟你讲法律，你搞不好是要偿命的。",
     "relation": "supports"
    },
    {
     "key": "E14",
     "paragraph_id": "P015",
     "quote": "用热气球登珠峰，目前是做梦——历史记录不过海拔6600米而已。",
     "relation": "supports"
    },
    {
     "key": "E15",
     "paragraph_id": "P016",
     "quote": "但是以珠峰的风力之猛，这也算是创意自杀了。",
     "relation": "supports"
    },
    {
     "key": "E16",
     "paragraph_id": "P019",
     "quote": "你们打算说的那个直升机在珠峰顶“着陆”的视频我当然看过。",
     "relation": "context"
    },
    {
     "key": "E17",
     "paragraph_id": "P020",
     "quote": "所谓的“着陆”，就是上图这里这点起落架接触。",
     "relation": "supports"
    },
    {
     "key": "E18",
     "paragraph_id": "P021",
     "quote": "旋翼可没敢停机",
     "relation": "supports"
    },
    {
     "key": "E19",
     "paragraph_id": "P022",
     "quote": "第二，我说的就是它不敢下人。",
     "relation": "supports"
    },
    {
     "key": "E20",
     "paragraph_id": "P023",
     "quote": "放一个人落地站五分钟再把ta接走，我才认可你算是完成了测试项目",
     "relation": "supports"
    },
    {
     "key": "E21",
     "paragraph_id": "P024",
     "quote": "注意，我不是认为这是“绝对不可能的”，但是我相信死亡率不会低于19%。",
     "relation": "supports"
    }
   ]
  },
  "provisional_tags": {
   "domain_candidates": [
    "航空器运用与飞行安全",
    "登山与高海拔作业",
    "风险与伦理"
   ],
   "issue_candidates": [
    "直升机高海拔性能与自反扭矩",
    "珠峰顶着陆与绳降可行性",
    "积雪区直升机作业的滑坡风险与道德责任",
    "热气球/氦气球登顶可行性",
    "登顶认定标准"
   ],
   "text_function_candidates": [
    "答疑",
    "评论",
    "批评",
    "风险分析",
    "预先反驳"
   ],
   "object_candidates": [
    "直升机",
    "珠穆朗玛峰",
    "尾桨",
    "热气球",
    "氦气球",
    "徒步登山者",
    "直升机厂家",
    "飞行员"
   ],
   "working_keywords": [
    "自反扭矩",
    "绳降",
    "大钟摆",
    "反冲气流",
    "积雪滑坡",
    "90米/秒",
    "19%",
    "起落架接触",
    "创意自杀",
    "噪音大户"
   ]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 3 个图片节点（IMG001..IMG003），图片内容未经核验，需图像核验；已读部分为正文文本。P020 的所谓上图这里这点起落架接触依赖图片，正文无法确认图中所指，故 status=needs_reread、image_checked=false。文中多处数值（19%、90米/秒、189公里、-17～-41摄氏度、6600米）均需外部核查。"
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
