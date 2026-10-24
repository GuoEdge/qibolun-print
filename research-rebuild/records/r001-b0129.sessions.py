# -*- coding: utf-8 -*-
"""批次 r001-b0129 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0129.sessions.py            # 写 out/r001-b0129.out.jsonl
  python3 records/r001-b0129.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0129"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0129.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "22eb3b2f": {
  "analysis": {
   "question_context": "提问者问：为了能跨越阶层，年轻人应该具备哪些「个人素养」和「技术」（Q001，属提问者，不得归给作者）。作者没有列素养或技术清单，而是把问题改述为“最大功率的有效努力”，并用开车爬山作类比，最后建议不要盯着“跨越阶层”这个目标做事。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "把跨越阶层的要害定为“最大功率的有效努力”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "以开车爬山作类比：输出功率要够大、方向把握要得当。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "反例：盯着山顶直线开会导致功率不够、白耗汽油，甚至翻车。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "正解：先研究地图、走盘山公路、紧盯路面、车速恰当，反而上升最快。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "结论式建议：起码不要盯着“跨越阶层”这种目标来做事。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P007"], "summary": "理由：盯目标不利于发挥功率、把握方向，也不利于跨越阶层本身。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“跨越阶层”的要害是最大功率的有效努力。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把最大功率的有效努力比作开车爬山，含输出功率够大与方向把握得当两条。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为做到这两条的要害，是开车的人不能盯着山顶直线开。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为盯着山顶直线开，发动机功率几乎肯定不够，油门踩死不代表有速度，很可能驱动轮悬空白耗汽油，更可能从陡坡翻滚下来。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为应先研究地图、最好走盘山公路，老实紧盯路面、车速恰当，这反而是上升最快的。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议别的东西再努力，起码不要盯着“跨越阶层”这种目标来做事。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的理由是：盯着这种目标既不利于安心发挥最大功率，也不利于把握方向，最后也不利于“跨越阶层”。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "先给结论：跨越阶层的要害是最大功率的有效努力（P001）。",
    "用开车爬山类比，拆成“输出功率够大”和“方向把握得当”两条（P002）。",
    "指出要害在于不能盯着山顶直线开（P003）。",
    "给出直线开的三重后果：功率不够、油门踩死无效、轮子悬空白耗油甚至翻车（P004）。",
    "转向正解：先研究地图、走盘山公路、紧盯路面、车速恰当，反而上升最快（P005）。",
    "收束为“起码不要盯着‘跨越阶层’这种目标来做事”，并给出三条理由（P006-P007）。"
   ],
   "concept_usage": [
    {"term": "跨越阶层", "meaning": "提问者给出的目标，作者沿用而未加界定，并在结论中建议不要把它当作做事时盯着的目标。", "evidence": "P001、P006", "ambiguity": "未界定“阶层”的划分标准与跨越的判据。"},
    {"term": "最大功率的有效努力", "meaning": "作者自造的说法，指既要有足够的输出功率，又要方向得当的努力。", "evidence": "P001、P002", "ambiguity": "“功率”与“有效”如何度量，本文未说明。"},
    {"term": "盯着山顶直线开", "meaning": "比喻只盯着终极目标、走最短直线路径的做法。", "evidence": "P003、P004", "ambiguity": "比喻未给出对应到现实行为的具体所指。"},
    {"term": "盘山公路", "meaning": "比喻迂回但可行的路径，即“研究好地图”后选定的走法。", "evidence": "P005", "ambiguity": "现实中对应何种路径，本文未说明。"}
   ],
   "examples_and_targets": [
    "作者的核心类比：开车爬山（P002-P005），通篇用作说理框架。",
    "作者设想的反例情形：油门踩死、驱动轮悬空、从陡坡翻滚下来（P004）。",
    "作者设想的正例情形：研究地图、走盘山公路、避让落石和破坑（P005）。",
    "修辞材料：口语化的“摔得七荤八素”“油门踩死”（P004）。"
   ],
   "conditions": [
    "P001 用“显然”作断言，未给出论证。",
    "P004 用“几乎肯定”“根本不表示”“很可能”“更可能”保留概率与程度。",
    "P005 用“最好是”“不至于……也不至于”作条件与限定。",
    "P006 用“起码”限定建议的强度：并非禁止追求，而是不要以此为目标。",
    "P002 以“就像”标明是类比而非同一。"
   ],
   "rhetoric_and_tone": "短篇答疑，全篇以开车爬山一个比喻贯穿，第二人称“你”直呼读者；用“油门踩死”“摔得七荤八素”等口语化、夸张化表达；结构是先立结论，再类比、反例、正解，最后收成一条克制的建议。",
   "unresolved_questions": [
    "提问者问的是“个人素养”和“技术”清单，作者没有给出任何具体素养或技术条目。",
    "“跨越阶层”未界定；“最大功率的有效努力”也未给出可操作判据。",
    "“盘山公路”对应现实中的何种路径或方法，本文未说明。",
    "P001“显然是”的根据本文未展开。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "要“跨越阶层”，其要害显然是最大功率的有效努力。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "最大功率的有效努力，就像开车爬山，一个是输出功率要够大、一个是方向把握要得当。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "就是开车的人不能盯着山顶直线开", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "盯着山顶直线开，你的发动机功率几乎肯定不够，油门踩死根本不表示你就会有速度，你很可能会驱动轮悬空白耗汽油，更可能直接从陡坡上翻滚下来，摔得七荤八素。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "开车的人要先研究好地图，最好是走盘山公路。老老实实紧盯路面，车速恰当", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "别的东西你再努力，但起码不要盯着“跨越阶层”这种目标来做事。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这既不利于你安心发挥最大功率，也不利于你把握自己的方向，最后也不利于你“跨越阶层”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生策略", "社会流动", "成功观"],
   "issue_candidates": ["阶层跨越的路径", "目标设定与做事方式", "努力的方向与效率"],
   "text_function_candidates": ["答疑", "说理", "比喻式劝导"],
   "object_candidates": ["年轻人"],
   "working_keywords": ["跨越阶层", "最大功率的有效努力", "盘山公路", "盯着山顶直线开", "方向"]
  },
  "notes": "无图片。作者未按提问者所问列出“个人素养/技术”清单，而是改述问题并给出比喻式建议，已在未决问题登记。"
 },
 "e1ba30a8": {
  "analysis": {
   "question_context": "提问者问 OKR 工具的作用是否被夸大（Q001，属提问者）。作者的回应是：企业实施 OKR 的前提是要有一位“学术与实践的双重大师”级别的领袖，而这类领袖非常罕见，这才是 OKR 普遍流于一阵风的原因。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "实施 OKR 的门槛：需要“学术与实践的双重大师”级领袖；远不如 KPI 平易近人，需要极强的分析、定义和阐述能力，OKR 目标须有十几二十几万字注释才能联系到业务细节。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "这类领袖大体是 500 强大区总裁或全球副总裁级以上，但不排除“野有遗贤”与隐者。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006"], "summary": "条件：须对意识形态与科学方法、商业实践与人类社会都有总览全局又深入细节的认知，才能提出拎起整个企业的 OKR。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "反后果：否则 OKR 只是傲慢吹出来的虚影，没被真正实施是值得庆幸的。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "结论：OKR 的前提是罕见的领袖，这才是 OKR 普遍只是一阵风的原因。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为在企业中实施 OKR 需要“学术与实践的双重大师”这种级别的话事人来领导，远不像 KPI 体系那样平易近人，需要极强的分析、定义和阐述能力。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为一个 OKR 目标如果没有一本十几二十几万字的注释、准确通俗而令人信服地联系到具体业务的一切细节，就无法指导企业的战略发展。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者估计这类领袖大体上是 500 强大区总裁或全球副总裁级别以上的人，同时声明不排除“野有遗贤”、尚处微时者与大隐于市的隐者。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者提出必要条件：必须对意识形态和科学方法有总览全局又深入细节的认知，对商业实践和人类社会有深刻而放眼十年乃至百年的洞见，才能提出一个拎着整个企业往上爬的 OKR。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为否则那个 OKR 就会是傲慢吹出来的虚影，没被真的实施起来是值得庆幸的。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把 OKR 的前提归结为“要有这个足可尚任的领袖”。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这种领袖显然非常罕见，这才是 OKR 普遍只是一阵风、雁过无痕春水平的原因。", "evidence": ["E9"]}
   ],
   "argument_steps": [
    "先给判断：实施 OKR 需要“学术与实践的双重大师”级的话事人（P001）。",
    "与 KPI 对比，指出 OKR 不平易近人，需要极强的分析、定义和阐述能力（P002）。",
    "以条件句说明 OKR 目标须有巨量注释联系业务细节，否则无法指导企业战略（P003）。",
    "给出这类领袖的层级估计（500 强高层级），随即让步：不排除遗贤与隐者（P004-P005）。",
    "提出必备认知条件，并设想其成效（拎着企业往上爬、激励出伟大成就）（P006）。",
    "从反面说未满足条件的后果：OKR 成虚影，未被实施反而是幸事（P007）。",
    "收束为“前提是足可尚任的领袖”，并以此解释 OKR 普遍只是一阵风（P008-P009）。"
   ],
   "concept_usage": [
    {"term": "OKR", "meaning": "一种需要由极高水准领袖提出、并能拎起整个企业的目标管理工具；本文未定义其具体形式。", "evidence": "P001、P003、P008", "ambiguity": "未区分 OKR 工具本身与其实施条件；也未直接回答“作用是否被夸大”。"},
    {"term": "KPI体系", "meaning": "作为对照物出现，被形容为“平易近人”。", "evidence": "P002", "ambiguity": "未展开 KPI 与 OKR 的具体差别。"},
    {"term": "话事人／领袖", "meaning": "提出 OKR 并领导整个企业的人，须兼具学术与实践的双重素养，且非常罕见。", "evidence": "P001、P006、P008", "ambiguity": "未给出识别标准或培养途径。"},
    {"term": "学术与实践的双重大师", "meaning": "带引号的比喻性说法，指同时在理论与商业实践上都达到极高水平的人。", "evidence": "P001", "ambiguity": "为修辞性表述，无判据。"},
    {"term": "注释", "meaning": "指把 OKR 目标准确、通俗而令人信服地联系到具体业务一切细节的说明文本，作者以“十几二十几万字”形容其体量。", "evidence": "P003", "ambiguity": "数字为形容性表述还是实际要求，本文未说明。"}
   ],
   "examples_and_targets": [
    "对照对象：KPI 体系（P002）。",
    "作者给出的层级例子：500 强大区总裁或全球副总裁级别以上的人（P004）。",
    "作者让步时举的三类人：野有遗贤、尚处微时厚积而未发的英杰、大隐隐于市的隐者（P005）。",
    "修辞与历史类比材料：“四渡赤水、转战万里”（P006）、“一阵风，雁过无痕春水平”（P009）、“傲慢吹出来的虚影”（P007）。"
   ],
   "conditions": [
    "P001、P003 均以“在企业中”“如果没有……是无法……”限定实施场景与条件。",
    "P004 用“大体上，这大多是”作估计，非确指。",
    "P005 用“当然不排除”作让步，保留例外。",
    "P006 用“但必须是……才能……”给出必要条件。",
    "P009 用“显然”“普遍”作程度限定，未断言所有企业都失败。"
   ],
   "rhetoric_and_tone": "书面语夹文言化措辞（“恕我直言”“野有遗贤”“大隐隐于市”），对 OKR 实践者带调侃与讥刺（“傲慢吹出来的虚影”“雁过无痕春水平”）；以对照、让步、条件句层层收紧，末尾用对偶式短句收束。",
   "unresolved_questions": [
    "作者未直接回答“OKR 工具的作用是否被夸大”，只谈实施 OKR 的前提条件。",
    "“十几二十几万字的注释”是形容还是实数要求，本文未说明，也无实例。",
    "P006 中“意识形态”一词的具体所指未界定。",
    "“足可尚任”的领袖如何识别、企业若无此领袖应如何做，本文未说明。",
    "P004 关于这类人多出自 500 强高层级的估计无数据支持，属待外部核查的断言。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在企业中要实施OKR，需要“学术与实践的双重大师”这种级别的话事人来领导。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这远不像KPI体系那样平易近人，需要极强的分析，定义和阐述能力。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "一个OKR目标，如果没有一本十几二十几万字的注释，去准确、通俗而又令人不能不信服的联系到具体业务的一切细节，是无法指导企业的战略发展的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "大体上，这大多是500强大区总裁或者全球副总裁级别以上的人。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "当然不排除野有遗贤，以及尚处于微时、厚积而未发的英杰，以及大隐隐于市的隐者。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "但是必须是对意识形态和科学方法都有总览全局而又深入细节的认知，也对商业实践和人类社会有深刻入骨而又放眼十年乃至百年的洞见，才能在这个基础之上提出一个能拎着整个企业后脖领往上爬的OKR", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "否则，那个OKR就会是傲慢吹出来的虚影，你们要庆幸它没有真的被实施起来。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "换句话说，OKR的前提是要有这个足可尚任的领袖。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "而这种领袖显然是非常罕见的，这才是OKR普遍只是一阵风，雁过无痕春水平的原因。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["企业管理", "组织管理", "领导力"],
   "issue_candidates": ["OKR 的适用条件", "目标管理工具的效果", "企业领袖的稀有性"],
   "text_function_candidates": ["答疑", "评论", "批评"],
   "object_candidates": ["OKR", "KPI体系", "500强企业", "企业领袖"],
   "working_keywords": ["OKR", "KPI", "话事人", "学术与实践的双重大师", "足可尚任", "一阵风"]
  },
  "notes": "无图片。本文未直接评价 OKR 工具本身是否被夸大，只论实施前提，已在未决问题登记。"
 },
 "86946c9c": {
  "analysis": {
   "question_context": "提问者问：一直关注一位知乎“大神”，今天突然发现自己对他很有好感，怎么办（Q001，属提问者）。作者先替这种爱慕辩护、反对嘲讽，随后把重点转向提问者自述的“自觉的卑微”，主张卑微＋崇拜是偶像崇拜而非尊重，其危险在于对被崇拜者的毒害，并给出“爱只可顺取、不可逆求”“不强求就是爱”的劝告。提问者与作者是两个人，文中“大神”的性别、婚否等背景未说明。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "为爱慕辩护：嘲讽不该有；在对方无拒绝禁令、无已知道德违碍时，勇敢追求无可厚非。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "结果无人能保证；嘲笑者自己也不是命运的主宰，其成败概率并不占优。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "转折：指出提问者忐忑中的“自觉的卑微”，并称这会是个很大的问题。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "辨析：尊重与尊敬是良性关系的基础，卑微＋崇拜不是它们而是偶像崇拜；粉丝追求对明星很有吸引力，故真正的危险不是不易成功反而是太容易成功。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "排除“养后宫”这一常见担忧（此类关系所在多有、历史不罕见），指出真正的危险是偶像崇拜让被崇拜者丧失必要的谦卑。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "卑微是被崇拜者的毒药：可能满足双方欲望却毁灭对方前途；顺利成功反而预示最坏未来，被礼貌拒绝才是对双方更好的结果。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "爱只可顺取不可逆求；顺取不可得不是损失，可以自我成长并无限继续顺求（非对同一对象无限重试）。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P022"], "summary": "逆求而得往往先胜后败，大概率毁灭再试的心力，浪费本可重试到真正取得的机会。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "若只求欲、不在乎爱，则大可以一试再试；对方扛不住是其为傲慢受劫，对方的拒绝乃至让你由崇拜转愤恨，其实是对你真正的仁慈。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "设问转折：并非不能追求自觉远不及的人；能力、资源、地位不如对方不是卑微的理由。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P031", "P032", "P033"], "summary": "爱的内在逻辑：有爱的自觉即无卑微；人人都能力不足、人人有罪，若只爱能力足、洁白无瑕者，爱便是虚言。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038"], "summary": "反论：若对方的学识人品使其看不到自己也是需要爱且不配得爱的罪人，则其不值得崇拜反而值得可怜；准备给予爱者足以在“伟大”者面前昂首挺胸。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P039", "P040", "P041"], "summary": "爱没有卑微，真正的问题是在合理性、自制力、真实性、谦卑上是否尽力；对方说不时，不强求就是爱。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046"], "summary": "结论：问题不在于条件差“配不上”，而在于你追求的是不是爱；若是，则要看对方配不配受得起，从此点走出去的每种结果都会是好的。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054"], "summary": "PS 的必然推论：有爱的自觉者与任何“大神”一样好、不必卑微，且这样的人在自觉卑微者中比例更高、很可能已在身边。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为对才华出众者心生爱慕是人之常情，这类事本来不该受到嘲讽和调侃。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为在对方没有不接受这样做的禁令、也没有已知的道德违碍可言的情况下，奋身追求是无可厚非的。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "questioned", "statement": "作者以设问指出是否一定会有好结果没人能保证。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为嘲笑提问者“不现实”的人自己也不是命运的主宰，未必不是高估了自己，其感情失败而提问者成功的概率并非不存在、甚至不算小。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出提问者忐忑不安里有一份自觉的卑微（觉得自己条件有限、远远“配不上”“大神”），并判定这会是个很大的问题。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为尊重、尊敬是一切良性关系的绝对基础，而卑微＋崇拜这个组合不是尊重和尊敬，是一种偶像崇拜。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为偶像崇拜听起来比尊重尊敬更礼貌谦恭、品尝起来更甜美，所以“粉丝追求”对“明星”有很大吸引力。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这事的真正危险不在于不容易成功，反而是太容易成功。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认危险真正在于“偶像”“养后宫”，理由是此类关系所在多有、稳定存在的案例已形成自我稳定的内在礼仪，且历史上并不罕见（古代普遍的一夫多妻制并非全是悲剧收场）。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为真正的危险在于偶像崇拜对被崇拜者也极其危险，会让对方不自觉丧失绝对必要的谦卑。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为提问者的卑微对对方是隐秘而致命的毒药：很可能满足双方欲望，却可能毁灭对方的前途和提问者原本看重的宝贵东西。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者提出一条“诡异的逻辑”：卑微的追求若非常顺利地成功，反而预示最坏的未来（对方还没有足够深刻的警觉）；被礼貌拒绝、“失败”了才是对双方更好的结果。", "evidence": ["E18", "E19"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张爱这种东西只可顺取、不可逆求；顺取而不可得并非损失，意味着命运有其他安排。", "evidence": ["E20", "E21"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为逆求而竟然得之往往先胜而后败，很大概率毁灭一切再试一次的心力，浪费本来可以无限重试直到真正取得的机会。", "evidence": ["E22", "E23"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者设条件：若你只是有欲、觉得爱无所谓而及时满足更重要，则大可以去试、一试再试；对方扛不住诱惑是其为自己的傲慢和自我崇拜受劫，双方都是活该。", "evidence": ["E24", "E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为对方若提前知道不可行而让你屡战屡败、乃至让你由崇拜转向愤恨，这种忍受你的憎恨与误解、让你得到“这条路走不通”的现实体验，才是对你真正的仁慈。", "evidence": ["E26", "E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否认不可以爱慕、追求自己觉得远远不及的人（连“难道爱因斯坦只能留给居里夫人了吗”的反问也答以“当然不是”）。", "evidence": ["E28", "E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为能力、资源、地位远远不如对方并不是应该卑微的理由：只要后者有爱的自觉，前者就无卑微可言。", "evidence": ["E30", "E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为真正的爱自然内嵌的基本逻辑是：能力不足和有罪并不是不可以爱的缺陷，因为人人都能力不足、人人都有罪；若只能爱能力足、洁白无瑕的人，爱只是毫无意义的虚言。", "evidence": ["E32", "E33"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为如果对方渊博的知识、深刻的洞察、高贵的人品竟不会导致其看到自己也是千疮百孔的罪人、自己也需要爱且不配得到爱，那么对方不但不值得崇拜，反而值得可怜，其满腹诗书只是自欺欺人的谎言。", "evidence": ["E34", "E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为当一个人打算去爱另一个人，其所准备给予的东西本身就足以让ta在任何所谓“伟大”的人面前昂首挺胸，没有卑微可言；敢嘲笑这份爱的人是不自知的可怜虫。", "evidence": ["E36", "E37"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为爱没有卑微这个概念，真正的问题是是否尽了力（合理性、自制力、真实性、谦卑上尽力）；对方说了不，就要把全部心力放在自我克制、不强求上，这时不强求就是爱。", "evidence": ["E38", "E39", "E40"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为问题不在于是否条件很差、“配不上”对方，而在于你打算给予、追求的是不是爱；若是，则要看对方配不配得上你、有没有福分和资格受得起你的垂爱。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者认为从“你追求的是不是爱”这一点走出去的每一种结果都会是好的（尽管不意味着终成眷属，也可能是温和的拒绝）。", "evidence": ["E44", "E45"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者在 PS 中给出必然推论：根本不是任何意义上的“大神”的人若有爱的自觉，就和任何一个“大神”一样好，不必在“大神”面前卑微，因为ta自己就是一个王。", "evidence": ["E46", "E47"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为有爱的自觉者，在自觉卑微的人之中的比例反而比在自觉“大神”的人中高得多，而且ta们比“大神”更好、很可能已经在提问者身边。", "evidence": ["E48", "E49"]},
    {"claim_id": "C027", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者引述并反驳的一种看法：自认为选择足够靠谱、肯定会有好结果的人，据此嘲笑提问者的追求“不现实”。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "先反对嘲讽：爱慕才华是人之常情，无禁令、无道德违碍时追求无可厚非（P001-P002）。",
    "承认结果无人能保证，但指出嘲笑者的判断同样不可靠（P003-P005）。",
    "以“但是”自我标示转折，指出提问者的“自觉的卑微”，并判其为大问题（P006-P008）。",
    "辨析尊重／尊敬与卑微＋崇拜，定义后者为偶像崇拜（P009-P011）。",
    "反过来指出真正的危险是“太容易成功”，并先排除“养后宫”这一常见担忧（P012-P013）。",
    "给出真正危险：偶像崇拜使被崇拜者丧失谦卑；卑微是对方的毒药（P014-P016）。",
    "以“诡异逻辑”说明顺利成功预示最坏未来、被拒绝反而更好（P017-P018）。",
    "提出爱的原则：只可顺取不可逆求，顺取不得非损失（P019-P021）。",
    "对比逆求而得先胜后败，并给“只求欲者”留出可一试再试的余地（P022-P026）。",
    "设问“难道不可以追求远高于自己的人”，答以“当然不是”，并否定卑微的理由（P027-P030）。",
    "给出爱的内在逻辑：有爱的自觉即无卑微；人人有罪，爱须包容（P031-P033）。",
    "反论：看不到自己是罪人的“大神”不值得崇拜反而值得可怜（P034-P038）。",
    "给出行动标准：爱的问题是是否尽力；对方说不时，不强求就是爱（P039-P041）。",
    "收束：问题不在于“配不上”，而在于你给的是不是爱；若是，每种结果都会是好的（P042-P046）。",
    "PS 作必然推论：有爱者与“大神”一样好，且更可能已在你身边（P047-P054）。"
   ],
   "concept_usage": [
    {"term": "卑微", "meaning": "提问者自述的“觉得自己条件有限、远远配不上大神”的心理，被作者判定为不属于尊重和尊敬的偶像崇拜，并被称为对被崇拜者的毒药。", "evidence": "P006-P010、P015", "ambiguity": "“自觉的卑微”与一般的谦虚、谦卑如何区分，本文未给判据（作者又把“谦卑”列为爱的尽力项之一）。"},
    {"term": "偶像崇拜", "meaning": "卑微者向另一方表达的战战兢兢的崇拜，既不属于尊重也不属于尊敬；对被崇拜者极其危险。", "evidence": "P010、P014", "ambiguity": "与粉丝文化、宗教崇拜的关系未展开。"},
    {"term": "爱", "meaning": "作者赋予其特定内涵：内嵌“人人都能力不足、人人有罪”的逻辑，没有卑微可言，只可顺取不可逆求，真正问题是是否尽力。", "evidence": "P019、P032、P033、P039", "ambiguity": "“爱的自觉”未给判据；未说明其与情感、欲望的界限。"},
    {"term": "顺取／逆求", "meaning": "顺取指顺其自然地求得，逆求指强求；作者主张前者、反对后者。", "evidence": "P019、P022", "ambiguity": "“顺”与“逆”的具体行为界线本文未界定。"},
    {"term": "ta", "meaning": "作者通篇使用的不分性别的第三人称代词，随上下文指对方、被崇拜者或泛指第三人。", "evidence": "P024、P025、P032", "ambiguity": "多处“ta”的指代对象需依上下文判定，如 P025 的“ta”指对方。"},
    {"term": "养后宫", "meaning": "带引号的网络说法，指被崇拜者同时维持多个崇拜者关系的情形；作者用它来排除一种被误认的危险。", "evidence": "P013", "ambiguity": "该词所指的关系形态本文未细说。"}
   ],
   "examples_and_targets": [
    "作者引述并反驳的对象：嘲笑提问者“不现实”的人（P004，opponent_view）。",
    "作者的历史论据：古代普遍的一夫多妻制、稳定的“后宫”案例（P013），属断言，待外部核查。",
    "作者的反问式类比：爱因斯坦只能留给居里夫人了吗（P028）。",
    "修辞材料：“隐秘而致命的毒药”（P015）、“销魂蚀骨的诱惑”（P024）、“活该”（P024）、“可怜虫”（P038）、“ta自己就是一个王”（P051）。",
    "本文设定的人物角色：提问者（爱慕“大神”的读者）、“大神”（被关注者）、旁观嘲讽者，均未具名。"
   ],
   "conditions": [
    "P002 以“尤其是对方没有什么不接受这样做的禁令、也没有什么已知的道德上的违碍可言”为追求可成立的条件。",
    "P003 明说结果无人能保证。",
    "P005 用“概率并非不存在——甚至都不算小”保留程度。",
    "P016、P017 用“很可能”“可能”“如果……反而预示着”保留可能性与假设语气。",
    "P022 用“往往”“很大概率”限定逆求后果。",
    "P023 以“你如果只是有欲……那么你大可以去试”设定前提分支。",
    "P034 以“如果对方的……竟然不会导致……”作条件。",
    "P040 以“对方如果说了不”为条件给出行动要求；P045 用“尽管……也可能是温和的拒绝”保留结果的不确定。"
   ],
   "rhetoric_and_tone": "第二人称“你”全程对话式劝导，先安慰后警告；以“但是——这里要讲‘但是’了”自我标示转折；设问自答（P027-P029）、反问（P003、P028）、排比（P039 四个“在……上尽力”、P020-P021 的“顺取”系列）；夹道德—宗教语汇（罪人、仁慈、垂爱、谦卑）与口语调侃（“活该”“可怜虫”“该着ta……受这一劫”）；结尾以“PS”另起一段作推论，并用短句“ta自己就是一个王”收束。",
   "unresolved_questions": [
    "提问者与“大神”的具体关系、对方是否已婚或有无伴侣等背景，本文未说明。",
    "“爱的自觉”如何识别、如何取得，本文未给判据。",
    "“顺取”与“不强求”的具体边界、以及“无限继续顺求”是否指换对象，本文未完全说明。",
    "P013 关于古代一夫多妻制“显然并非全是悲剧收场”属作者论据，需外部核查。",
    "文中“ta”多处指代需依上下文判断（如 P024 指对方、P032 泛指），本文未明示。",
    "作者称满腹诗书可能是“自欺欺人……的谎言”，其适用对象范围（是否指所有学识渊博者）本文未限定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这里嘲讽你的人很多，但是这事本来是不该受到嘲讽和调侃的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "觉得对方才华出众，忍不住爱慕，这是人之常情。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "尤其是对方没有什么不接受这样做的禁令、也没有什么已知的道德上的违碍可言，那么这是无可厚非的事。", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P003", "quote": "是不是一定会有好结果？这没人能保证。", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P004", "quote": "嘲笑你“不现实”的人，ta们自己也不是自己命运的主宰", "relation": "contradicts"},
    {"key": "E6", "paragraph_id": "P005", "quote": "回头ta们自己感情失败，而你的尝试却成功了的概率并非不存在——甚至都不算小。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "我看到你的忐忑不安里面有一份自觉的卑微。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "也就是你觉得自己条件有限，远远“配不上”“大神”。", "relation": "context"},
    {"key": "E9", "paragraph_id": "P008", "quote": "这个卑微会是个很大的问题。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "尊重、尊敬，是一切良性关系的绝对基础，但是偏偏卑微+崇拜这个组合并不是尊重和尊敬。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "而是一种既不属于尊重、又不属于尊敬的东西——偶像崇拜。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "所以“粉丝追求”对“明星”真的是有很大的吸引力的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "所以这事真正的危险，不在于它不容易成功，反而是它太容易成功。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "它甚至也并不真正的危险在“偶像”“养后宫”", "relation": "contradicts"},
    {"key": "E15", "paragraph_id": "P014", "quote": "真正的危险在于，偶像崇拜对于被崇拜者也极其危险，会让对方不自觉的丧失绝对必要的谦卑。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P015", "quote": "你的卑微，对对方而言是一种隐秘而致命的毒药。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "它很可能确实可以满足你的欲望，甚至也可以满足对方的欲望；但却可能毁灭了对方的前途，毁灭掉你原本看重的那些宝贵的东西。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P017", "quote": "如果你这卑微的追求非常顺利的成功了，反而预示着最坏的未来——因为那意味着对方还没有这种足够深刻的警觉。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "反而是你这卑微的请求被对方礼貌的拒绝了，你“失败”了，才是对你们双方更好的结果。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P019", "quote": "爱这种东西，只可顺取，不可逆求。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P020", "quote": "顺取而不可得，并非一种损失，那意味着你的命运有其他的安排。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "逆求而竟然得之，往往先胜而后败。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P022", "quote": "它事实上会是对本来可以无限重试、直到真正取得的机会的浪费和糟蹋。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "你如果只是有欲，而且觉得爱什么的无所谓，及时满足比较重要——那么你大可以去试，一试而再试。", "relation": "qualifies"},
    {"key": "E25", "paragraph_id": "P024", "quote": "ta若扛不住你这销魂蚀骨的诱惑，那么该着ta为自己的傲慢和自我崇拜受这一劫，ta是活该，你也是活该。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "那么你会屡战屡败，乃至于由崇拜转向愤恨", "relation": "context"},
    {"key": "E27", "paragraph_id": "P026", "quote": "但其实，忍受你的憎恨和误解，让你得到一个“这条路走不通”的现实体验，这才是对你真正的仁慈。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P027", "quote": "那么难道不可以爱慕、追求自己觉得自己远远不及的人了吗？", "relation": "context"},
    {"key": "E29", "paragraph_id": "P029", "quote": "当然不是。", "relation": "contradicts"},
    {"key": "E30", "paragraph_id": "P030", "quote": "你的能力、资源、地位远远不如对方，并不是你应该卑微的理由。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P031", "quote": "一个人在另一个人面前，无论前者如何无能、愚蠢和罪孽深重，若是后者有爱的自觉，前者就无卑微可言", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P032", "quote": "ta很自然的会发现能力不足和有罪并不是不可以爱的缺陷。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P033", "quote": "因为人人都能力不足、人人都有罪。若是只能爱能力足、洁白无瑕的人，那么爱只不过是毫无意义的虚言。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P034", "quote": "对方不但不值得你崇拜，反而值得你可怜。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P035", "quote": "那满腹的诗书，只不过是为了自欺欺人、掩饰自己对自己的可怕鄙视的谎言而已。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P037", "quote": "ta所准备给予的东西本身，就足以让ta在任何所谓“伟大”的人面前昂首挺胸的站立，而没有任何卑微可言。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P038", "quote": "这人都是不自知的可怜虫。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P039", "quote": "所以爱是没有卑微这个概念可言的——它的真正问题是是否尽了力——在合理性上尽力、在自制力上尽力、在真实性上尽力、在谦卑上尽力。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P040", "quote": "对方如果说了不，那么就要把自己的全部心力放在自我克制、不强求上。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P041", "quote": "这时候不强求就是爱。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P042", "quote": "问题并不在于你是否条件很差，“配不上”对方。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P043", "quote": "而在于，你打算给予的、追求的，是爱吗？", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P044", "quote": "那么就要看ta配不配得上你、有没有这个福分和资格受的起你的垂爱。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P045", "quote": "尽管，这并不意味着终成眷属——也可能是温和的拒绝也说不定。", "relation": "qualifies"},
    {"key": "E45", "paragraph_id": "P046", "quote": "但，从这个点走出去的每一种结果都会是好的。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P049", "quote": "一个根本不是任何意义上的“大神”的人，若是有爱的自觉，ta就和任何一个“大神”一样好。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P051", "quote": "有爱的人可以无视出身、平视王侯——因为ta自己就是一个王。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P053", "quote": "这样的人，在自觉卑微的人之中的比例，反而要比自觉“大神”的人中高得多。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P054", "quote": "而且ta们比“大神”更好——因为ta们很可能已经在你身边。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["情感伦理", "人际关系", "道德哲学"],
   "issue_candidates": ["爱慕与追求", "卑微与崇拜", "偶像崇拜的危害", "爱与被爱的资格"],
   "text_function_candidates": ["答疑", "劝导", "说理", "情感建议"],
   "object_candidates": ["知乎“大神”", "粉丝", "提问者"],
   "working_keywords": ["卑微", "偶像崇拜", "尊重", "尊敬", "顺取", "逆求", "爱的自觉", "不强求就是爱"]
  },
  "notes": "无图片。提问者立场（对“大神”有好感）与作者立场（劝其去除卑微、以爱而非欲为准）已区分。文中“ta”为作者使用的不分性别代词，指代需依上下文判定，已在未决问题登记。"
 },
 "d636f210": {
  "analysis": {
   "question_context": "提问者问如何提升一个人的文笔（Q001，属提问者）。作者的回答是：人的语言味道取决于看得多的东西，因此要多看好的文字、看足够多，并强调看剧看电影替代不了，末尾另加一条“等真的有病再呻吟”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总纲：看啥比较多，说话就有啥味道。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006"], "summary": "以鲁迅、金庸、古龙、红楼梦、张爱玲为例，戏仿各自语感。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "方法：多看些好看的、看多点；但看剧看电影替代不了，只能靠看文字解决。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "给出量级建议：先看个一亿两亿字再说。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "附加一条：“等真的有病再呻吟”。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人很简单：看什么比较多，说话就有那个味道。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为提升文笔无非是多看些好看的、看多点，而这一条靠看剧、看电影替代不了，只能靠看文字来解决。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议先从小目标开始——先看个一亿两亿字再说。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者另提一条：“等真的有病再呻吟”。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "先立总纲：说话的味道由看得多的东西决定（P001）。",
    "连举五例戏仿语感：鲁迅、金庸、古龙、红楼梦、张爱玲（P002-P006）。",
    "由例归纳方法：多看好看的、看多点，并排除看剧看电影这条替代路径（P007-P008）。",
    "给出量化到夸张程度的目标：先看一亿两亿字（P009）。",
    "补一条告诫式建议：等真的有病再呻吟（P010）。"
   ],
   "concept_usage": [
    {"term": "文笔", "meaning": "本文未直接定义，实际被等同于由大量阅读养成的语言味道／语感。", "evidence": "P001、P007", "ambiguity": "未定义；也未区分遣词、结构、思想等层面。"},
    {"term": "味道", "meaning": "看某类文字多了之后在说话写作中带出的那种风格痕迹。", "evidence": "P001", "ambiguity": "为口语化表述，无判据。"},
    {"term": "一亿两亿字", "meaning": "作者给出的阅读量建议。", "evidence": "P009", "ambiguity": "是字面数量还是夸张说法，本文未说明。"}
   ],
   "examples_and_targets": [
    "作者例证（戏仿语感，非原文引用）：鲁迅的“大约”“大抵”“的罢”（P002）、金庸的“辣块妈妈”（P003）、古龙的“冷的像孙子似的”（P004）、红楼梦的“哪个妹妹都原是极好的”（P005）、张爱玲的白月光／蚊子血／朱砂痣（P006）。",
    "插话式补充：“此处郭德纲亦有贡献”（P004）。",
    "作者排除的路径：看剧、看电影（P007）。"
   ],
   "conditions": [
    "P007 用“无非是”“但有一条”作限定与强调。",
    "P009 用“不妨先从……开始”将建议降为可选的起步方式。",
    "P010 用“再就是一条”表明是附加建议。"
   ],
   "rhetoric_and_tone": "极短篇，口语调侃，全篇用“天天看X”五个排比句戏仿名家语感；末句以俗语式忠告收束。语气轻松，非论证性文章。",
   "unresolved_questions": [
    "“文笔”未定义，也未说明阅读之外是否还有其他提升途径。",
    "“一亿两亿字”是字面量还是夸张，本文未说明。",
    "P010“等真的有病再呻吟”的确切所指（是否指不要无病呻吟、或指写作须有真实感受）本文未展开。",
    "五处名家风格戏仿均为作者仿写，不是对原文的引用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "人这东西很简单——看啥比较多，说话就有啥味道。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P007", "quote": "所以呢，无非是多看些好看的，看多点。但有一条——这个靠看剧、看电影是替代不了的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P008", "quote": "这只能靠看文字来解决。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "你不妨先从一个小目标开始——先看个一亿两亿字再说。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "再就是一条——等真的有病再呻吟。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["写作", "语言学习", "阅读方法"],
   "issue_candidates": ["文笔提升途径", "阅读与语感", "影视能否替代文字阅读"],
   "text_function_candidates": ["答疑", "经验总结", "调侃式建议"],
   "object_candidates": ["鲁迅", "金庸", "古龙", "曹雪芹", "张爱玲", "郭德纲"],
   "working_keywords": ["文笔", "味道", "看文字", "一亿两亿字", "无病呻吟"]
  },
  "notes": "无图片。五处名家风格句子为作者戏仿，已按修辞材料记录，未当作引用原文。"
 },
 "e4b1fc0a": {
  "analysis": {
   "question_context": "提问者问新能源三大流派（换电、充电、氢燃料）哪一个会是未来（Q001，属提问者）。作者以“如果你说的是汽车的话”限定后表态：自己是坚定的换电派，并给出氢能定位、特斯拉路线判断与中国换电方案的适配理由。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "限定讨论对象为汽车后，表态是坚定的换电派。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "氢能主要用来替换煤、供火电；汽车上最好仍用电池，但电池接口要标准化。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "基本认为特斯拉的技术路线是错的，至少不符合中国的方向。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "中国换电方案的两条理由：减轻车载电池负担、密集换电站缓解里程焦虑且贴合人口稠密国情；换电站可作“边缘蓄水池”缓冲电网。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P005"], "summary": "换电与中央调度的地面无人公交体系天然一体：无人载具需周期性高频自动化检修，换电池是自然一步。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P006"], "summary": "特斯拉自带电池长续航方案只适用于地广人稀的美、加、俄，在世界大部分地区不适用。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P007"], "summary": "渲染包标注 lexical 未覆盖的片段“探全球速度最快的换电站：20秒极速换电”，疑为平台链接卡片文本，非作者论证。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者以“如果你说的是汽车的话”为前提，表明自己是坚定的换电派。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为氢能源主要是用来替换煤、供火力发电厂发电用的；汽车上最好还是用电池，但电池接口无疑要标准化。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者基本上认为特斯拉的技术路线是错的——至少不符合中国的方向。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国换电方案能减轻车辆自身电池负担、靠密集换电站缓解里程焦虑，与中国人口稠密的现状更贴合，且众多换电站可作“边缘蓄水池”为电网稳定提供缓冲。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为换电与中央调度的地面无人公交体系天然一体，因为大量无人载具需要周期性、高频的自动化检修维护，更换电池是很自然的一步。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为特斯拉自带电池的长续航方案除了地广人稀的美国、加拿大、俄罗斯外，在世界大部分地区都不适用。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "先限定讨论对象是汽车，再表态换电（P001）。",
    "给氢能另作定位（替换煤、供火电），并主张汽车用电池、接口须标准化（P002）。",
    "以“基本上”“至少”的保留语气否定特斯拉路线在中国的适配性（P003）。",
    "给出换电贴合中国的两条理由：电池负担与里程焦虑、换电站作电网缓冲（P004）。",
    "给出协同理由：与中央调度的地面无人公交体系天然一体（P005）。",
    "反过来指出特斯拉长续航方案的地域适用范围有限（P006）。"
   ],
   "concept_usage": [
    {"term": "换电", "meaning": "作者所主张的汽车补能路线：车电分离、靠密集换电站补能，并可兼作电网缓冲。", "evidence": "P001、P004", "ambiguity": "未说明换电标准、成本与推广条件。"},
    {"term": "氢能源", "meaning": "作者把它定位为替换煤、供火力发电厂发电用的能源，而非车用主路线。", "evidence": "P002", "ambiguity": "未给出依据，也未讨论氢燃料车的其他用途。"},
    {"term": "边缘蓄水池", "meaning": "带引号的比喻，指众多换电站可为电网稳定运作提供缓冲。", "evidence": "P004", "ambiguity": "为修辞性表述，未展开技术机制。"},
    {"term": "中央调度的地面无人公交体系", "meaning": "作者提到的一种体系，与换电天然一体。", "evidence": "P005", "ambiguity": "本文未说明该体系的现状、规模或来源。"},
    {"term": "特斯拉的技术路线", "meaning": "指自带电池的长续航方案，被作者判为错、至少不符合中国方向。", "evidence": "P003、P006", "ambiguity": "未区分特斯拉的具体车型或技术细节。"}
   ],
   "examples_and_targets": [
    "反驳／否定对象：特斯拉的技术路线与自带电池长续航方案（P003、P006）。",
    "作者举的地域例子：美国、加拿大、俄罗斯（P006，作为长续航方案适用范围的例外）。",
    "作者提及的对象：中央调度的地面无人公交体系（P005）。",
    "平台残留片段：“探全球速度最快的换电站：20秒极速换电”（P007）。"
   ],
   "conditions": [
    "P001 以“如果你说的是汽车的话”限定讨论范围。",
    "P002 用“主要是”“最好还是”“无疑”混合断言与限定。",
    "P003 用“基本上”“至少”保留程度。",
    "P006 用“除了……在世界的大部分地区都不适用”给出地域条件。"
   ],
   "rhetoric_and_tone": "短答，第一人称直接表态（“我是坚定的换电派”），句式短促、断言多；带技术与政策语汇（中央调度、边缘蓄水池、标准化）；对特斯拉路线用“是错的”这类直白判断。",
   "unresolved_questions": [
    "P007“探全球速度最快的换电站：20秒极速换电”在渲染包中标注“⚠lexical未覆盖片段”，疑为视频／链接卡片文本而非作者正文，是否属于作者内容待核。",
    "“中央调度的地面无人公交体系”本文未给出所指或来源。",
    "“边缘蓄水池”的机制、以及换电站建设的成本与规模条件，本文未说明。",
    "作者未逐一比较充电与氢燃料两条路线，也未说明充电与换电是否可以并行。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "如果你说的是汽车的话，我是坚定的换电派。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "氢能源主要是用来替换煤，供火力发电厂发电用的。实际上汽车上最好还是用电池，但电池接口无疑要标准化。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "我基本上认为特斯拉的技术路线是错的——至少不符合中国的方向。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "中国的换电方案可以减轻车辆自身的电池负担，靠足够密集的换电站来缓解里程焦虑。这和中国人口稠密的现状是更加贴合的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "众多换电站的存在也可以作为“边缘蓄水池”为电网的稳定运作提供很大的缓冲。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "更不用说这个和中央调度的地面无人公交体系是天然一体的——大量的无人载具需要周期性的、高频的自动化检修和维护，这其中更换电池是很自然的一步。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "特斯拉的自带电池长续航方案，除了在地广人稀的美国、加拿大、俄罗斯，在世界的大部分地区都不适用。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["新能源汽车", "能源政策", "技术与产业路线"],
   "issue_candidates": ["换电与充电路线之争", "氢能的用途", "特斯拉路线的适用性", "电网调峰"],
   "text_function_candidates": ["答疑", "表态", "产业评论"],
   "object_candidates": ["特斯拉", "中国", "美国", "加拿大", "俄罗斯", "中央调度的地面无人公交体系"],
   "working_keywords": ["换电", "充电", "氢燃料", "里程焦虑", "边缘蓄水池", "电池接口标准化"]
  },
  "notes": "无图片。text 与 lexical 存在分歧：P007 未被 lexical 覆盖，疑为平台链接／视频卡片残留，已在 structure.text_lexical_divergence 与未决问题登记。"
 },
 "a2649809": {
  "analysis": {
   "question_context": "提问者问「在北极科考，却遇到北京朝阳区的小学毕业旅行」反映了什么问题、如何给孩子一个特别的毕业季（Q001，属提问者）。作者的回应是反问式辩护：小学生能去北极毕业旅行是好事，富人消费最终会流向他人，故此事对穷人并非坏事；随后反驳“苦情反衬”与“一切都是剥削”的说法，并建议拉黑煽动情绪的信息源。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以反问开场：小学生能去北极毕业旅行是好事；并追问富人富了、别人过好了对穷人是否真是坏事。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "设定关键环节：好人富了对穷人不是坏事，坏人富了也未必全是坏事；只有故意浪费财富换取无价值之物、或以制造他人痛苦为享乐才是坏事。", "role": "qualification"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "财富终将流向他人（游艇、马戏团例）；只要不用于伤害、不销毁，就总不是坏事。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "落到本例：主办方、员工、老板受益，厨师快递员等间接受益，孩子留下印象；反问有啥不好。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "反驳“苦情反衬”：若因有人饿肚子就不许有人吃饱，类比“有人没工作就禁止探月”，指出禁止体验不会增进贫困者福利、反而减少工作机会。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020"], "summary": "排比反问：为何愤愤不平、口诛笔伐、定罪、打击抑制；看不出对穷人有何客观好处。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023"], "summary": "反驳“贵得不行”：该夏令营约 5 万元、14 天，并非非剥削压迫不能负担。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029"], "summary": "列举高薪职业（飞行员、游戏主创、程序员、研发、总工程师／总会计师、战略咨询与职业经理人），反问“剥削了谁”。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031", "P032"], "summary": "质疑“一切的财富都来自剥削”的依据；以袁隆平、钟南山该领多少工资及其孙辈能否参加反问。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038"], "summary": "行动建议：拉黑煽动情绪的信息源，因其增强不理性与仇恨；指出有人靠制造贫穷换取流量金钱，称之为劫掠。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P021", "P039"], "summary": "渲染包标注 lexical 未覆盖的两个短片段（“是否有很多人歧视奢侈品？”“穷人怎么才能翻身？”），疑为平台相关问题链接。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以反问表明：中国有小孩小学毕业就能到北极毕业旅行是好事。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为一个好人富了，对穷人当然不是坏事；甚至一个坏人富了，对穷人也未必全是坏事。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为只有故意浪费财富换取没有价值的东西（例如虚荣和没有人会记得的体验），或换取以制造他人痛苦为形式的享乐，才是坏事。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为钱即使先集中到谁手里，最后也还是要流向其他人，因为纯留在手里没什么意义；只要没用在伤害人的事情上、也没销毁，就总不是坏事。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者举例说科考毕业旅行主办单位赚了钱，其员工和老板的收益会用在自身与亲人需求上，于是可能很快就会有一大批厨师、快递员等因此受益，孩子也留下深刻印象。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质疑以“还有很多贫苦小孩、高考艰辛”等苦情反衬这些孩子选择错误的论证：这样证明关系怎么能成立。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为若因为有人缺少工作和收入就禁止其他人追求需要经济实力才能有的体验，不但不会增进贫困者的福利，倒是会进一步减少工作机会。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问表示看不出愤愤不平、口诛笔伐、定罪、打击抑制对穷人们到底有什么客观的好处。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者指出该夏令营价格约 5 万人民币、时间 14 天，据此认为这并不是非要剥削、压迫才能负担得起的费用。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以飞行员、游戏主创、程序员、高端研发、总工程师／总会计师、战略咨询与职业经理人等薪资为例反问“ta们剥削了谁”，以此反驳高薪即剥削的说法。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "作者引述并质疑“一切的财富都来自剥削”这一说法的依据；该说法在文中未指明说话者。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以袁隆平、钟南山的工资与其孙辈能否参加夏令营反问，并反问是否希望中国没有哪家的孩子可以去得起这样的夏令营。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议拉黑那些煽动这类情绪的信息源，因为廉价而不分青红皂白的愤怒是在增强不理性与仇恨，而不是理性与宽容。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为如果真不喜欢贫穷，抛弃理性与宽容这两样东西不但不是摆脱贫穷的正确道路，而且是不折不扣的背道而驰。", "evidence": ["E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为有人在靠制造你们的贫穷换取流量和金钱，而你们在给ta们点赞和关注、推高ta们的报酬率，这根本就是劫掠。", "evidence": ["E22", "E23"]}
   ],
   "argument_steps": [
    "以反问立论：孩子能去北极毕业旅行是好事（P001）。",
    "把问题一般化为“富人富了、别人过好了对穷人是否真是坏事”（P002-P003）。",
    "给出关键环节：好人富了不是坏事、坏人富了未必全是坏事，只有故意浪费或以制造痛苦为乐才是坏事（P004-P005）。",
    "用游艇、马戏团两例说明钱会流向他人（P006-P008）。",
    "归纳：钱最终要流向别人，只要不伤害人、不销毁，就总不是坏事（P009-P010）。",
    "把结论用于本例：主办方与相关从业者受益、孩子受教，反问有啥不好（P011-P012）。",
    "反驳苦情反衬论，并以“有人没工作就禁止探月”作类比（P013-P014）。",
    "连用五个“为什么”反问对方举动的实际好处（P015-P020）。",
    "反驳“贵得不行”，给出价格与天数（P022-P023）。",
    "列举高薪职业反问“剥削了谁”（P024-P029）。",
    "质疑“一切的财富都来自剥削”的依据（P030）。",
    "以袁隆平、钟南山反问，反证禁止体验的荒谬（P031-P032）。",
    "给出行动建议：拉黑煽动情绪的信息源（P033-P035）。",
    "收束：有人靠制造你们的贫穷赚流量，你们在推高其报酬率，这是劫掠（P036-P038）。"
   ],
   "concept_usage": [
    {"term": "剥削", "meaning": "作者引述并质疑的说法中的核心词（“一切的财富都来自剥削”），作者以多种职业薪资反问其成立性。", "evidence": "P024-P030", "ambiguity": "作者未给“剥削”下定义，也未区分资本收益与劳动收入。"},
    {"term": "坏事／好事", "meaning": "作者以“是否伤害人”“是否销毁财富”为判据：故意浪费财富换取无价值之物或以制造他人痛苦为享乐是坏事。", "evidence": "P005、P010", "ambiguity": "“没有价值的东西”“没有人会记得的体验”如何界定，本文未说明。"},
    {"term": "苦情", "meaning": "作者指称对方以贫苦小孩、高考艰辛等叙事反衬这些孩子选择错误的做法。", "evidence": "P013", "ambiguity": "未指明持此说法者是谁。"},
    {"term": "劫掠", "meaning": "作者对“靠制造你们的贫穷换取流量和金钱”这一行为的定性（比“剥削”更强）。", "evidence": "P036、P037", "ambiguity": "为修辞性指控，未提供证据。"}
   ],
   "examples_and_targets": [
    "被反驳的观点（opponent_view）：苦情反衬论（P013-P014）；“一切的财富都来自剥削”（P030）——两者均未指明说话者。",
    "作者证据（数据性断言，待外部核查）：夏令营约 5 万人民币、14 天（P023）；30 岁飞行员税后 90 万（P024）；游戏主创年薪百万常见（P025）；有经验程序员一年 30-40 万（P026）。",
    "作者举的人物：梁孟松（P027）、袁隆平、钟南山（P031）。",
    "作者举的类比：南霸天（P006）、“还有人没有工作，你们却发射飞船探测月球”（P014）。",
    "修辞材料：游艇工人买面包、马戏团发工资（P007-P008）、“活生生的被人卖了还帮人数钱”（P038）。",
    "平台残留片段：“是否有很多人歧视奢侈品？”（P021）、“穷人怎么才能翻身？”（P039）。"
   ],
   "conditions": [
    "P005 用“只有……这才是坏事”和“例如”限定坏事的范围。",
    "P006、P010 用“只要不……就总不是坏事”给出条件式判断。",
    "P011 用“想必”“可能很快就会”保留估计语气。",
    "P014 用“因为你们缺少工作和收入，就要禁止……的话”构成假设条件句，并以“吧？”结尾留出不确定。",
    "P023 用“差不多在……左右”给出约数。",
    "P025-P029 多处使用“非常常见”“不罕见”“谈不上高”等程度用语。",
    "P035 以“你如果真的这么不喜欢贫穷”为前提条件。"
   ],
   "rhetoric_and_tone": "通篇反问与排比（P012、P015-P020 连续五问），第二人称“你／你们”直指批评者，语气强硬的训诫与讥刺并用（“活生生的被人卖了还帮人数钱”“劫掠”）；先立一般原理再落到本例，中段大量列举职业薪资，末段转为行动建议。",
   "unresolved_questions": [
    "正文未描述也未核实“重庆生日宴蛋糕大战”这一事件本身，作者直接转入一般性财富论证。",
    "P021、P039 在渲染包中标注“⚠lexical未覆盖片段”，疑为平台相关问题／推荐链接混入正文，见 structure.text_lexical_divergence。",
    "P024-P029 的薪资数字（飞行员 90 万、程序员 30-40 万等）无来源，属待外部核查的断言。",
    "“一切的财富都来自剥削”与“苦情反衬”两种被反驳说法的说话者未指明。",
    "梁孟松、袁隆平、钟南山被用作反问例证，作者未说明其具体薪资主张。",
    "作者未回答提问的第二问“如何给孩子一个特别的毕业季”。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这好事啊，中国有小孩小学毕业就能到北极毕业旅行，这不是很好的事吗？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "一个好人富了，对穷人当然不是坏事；甚至就是一个坏人富了，对穷人也未必全是坏事。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "只有故意浪费财富换取没有价值的东西——例如虚荣和没有人会记得的体验，或甚至换取以制造ta人痛苦为形式的享乐，这才是坏事。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "钱先集中到谁手里，固然是会带给对方一些权利和优势，但是最后也还是要流向其他人的。因为纯留在手里没什么意义。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "只要没用在伤害人的事情上，也没有拿去一把火烧掉或者丢在水里扔了，就总不是坏事。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "于是可能很快就会有一大批厨师、快递员等等等等的人因此受益。小朋友也应该留下了深刻的印象", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "似乎想反衬这些小孩的选择如何错误的，这证明关系怎么能成立呢？", "relation": "contradicts"},
    {"key": "E8", "paragraph_id": "P014", "quote": "不但完全不会增进任何贫困者的福利，倒是会进一步的减少工作机会吧？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "所以，为什么要愤愤不平？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P019", "quote": "实在看不出这对穷人们到底有什么客观的好处。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P023", "quote": "这种夏令营价格差不多在5万人民币左右，时间长度14天。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "这并不是什么贵上天际非要这剥削、那压迫才能负担得起的费用。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "30岁飞行员税后90万，算正常水准，ta剥削了谁？", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "有经验的程序员一年30-40万的根本不罕见，ta们剥削谁了？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "战略咨询、职业经理人，人家能把整个企业的利润率提升一个百分比，年薪百万微不足道。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P030", "quote": "一天到晚剥削剥削，还“一切的财富都来自剥削”，这说法的依据是什么？", "relation": "contradicts"},
    {"key": "E17", "paragraph_id": "P031", "quote": "袁隆平应该一年拿多少工资？钟南山该领多少？ta们的孙子孙女能不能去参加？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P032", "quote": "难道你们希望中国没有哪家的孩子可以去得起这样的夏令营就满意了？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P033", "quote": "整天搞这些廉价而不分青红皂白的愤怒，我实实在在的建议你们拉黑那些煽动你们这些情绪的信息源。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P034", "quote": "因为这是在增强你的不理性，而不是理性；是在增强你的仇恨，而不是宽容。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P035", "quote": "你如果真的这么不喜欢贫穷，抛弃这两样东西不但不是摆脱贫穷的正确道路，而且还是不折不扣的背道而驰。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P036", "quote": "有人在靠制造你们的贫穷换取流量和金钱，而你在给ta们点赞和关注，在推高ta们的报酬率。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "这何止是“剥削”，这根本就是劫掠。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会经济", "财富分配", "舆论现象"],
   "issue_candidates": ["富人消费与穷人福利", "浪费与仇富情绪", "剥削论", "流量经济与情绪煽动"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "评论"],
   "object_candidates": ["北京朝阳区小学生", "北极科考毕业旅行", "袁隆平", "钟南山", "梁孟松"],
   "working_keywords": ["北极夏令营", "剥削", "劫掠", "苦情", "流量", "5万人民币", "涓流"]
  },
  "notes": "无图片。text 与 lexical 存在分歧：P021、P039 未被 lexical 覆盖，疑为平台相关问题链接混入正文，已在 structure.text_lexical_divergence 与未决问题登记。文中数字（5 万、90 万、30-40 万等）均属作者断言，未核。"
 },
 "c2241fe8": {
  "analysis": {
   "question_context": "提问者问厨房达人在整理和清洁厨房中有哪些小窍门（Q001，属提问者）。作者给出成体系的操作建议：首要在于不要弄脏，按油烟、刀具砧板、锅、碗碟四项分述具体做法，结论是让清洁量最小化，成本最小的手段是一开始就不做错。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总原则：清洁的首要要害在于不要弄脏；最根本的断根策略是多吃生鲜、不动火。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010"], "summary": "第一管住油烟：蔬菜下锅不带水、低温油不要烧到出烟、无法避免时及时盖锅盖并借蒸菜自清洁、不要大面积裸露复杂表面、买好点的油烟机；管住油烟后一般就没啥了。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013"], "summary": "第二管住刀具砧板：用朝日合成橡胶砧板不长霉；肉类让超市代切，家里不切肉则砧板不见油，清洁量可压缩到零。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015"], "summary": "第三管住锅：先掌握粘锅原理避免粘锅。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P016"], "summary": "铸铁煎锅掌握得当可永远不必清洗：以煎牛排后淋红酒／矿泉水趁沸腾用木铲搅和、残留变牛肉浓汁为例，锅内自然干净，抹油防下次粘锅。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019"], "summary": "圆底炒锅配弧形铲口的锅铲以铲到锅底每一点；锅最易脏处是汤汁倒出那侧锅沿，残留一烧即碳化，锅底变黑几乎全因此与洗锅不擦干导致的锈蚀；装盘后随手抹或让汤汁流尽，内侧结块每次洗锅铲除。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022"], "summary": "锅铲够好基本不需刷子或钢丝球；锅内有烧结物则开火加水在沸腾态下用锅铲清除；残留的油不要用洗洁精洗掉，开火蒸发水后纸巾抹匀反而养锅。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "第四管住碗碟：易沾污食材用一次性器皿（木皮船小碟、酱油碟、淋膜防油纸盒、铝箔等）；每次做适量不剩菜，省去冷藏器皿与清洗。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032"], "summary": "结果：全部措施到位后清洁工作最小化到几乎没有，用不着洗碗机与强力清污剂。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P033", "P034", "P035"], "summary": "收束格言：成本最小的手段不是强力便捷的补救措施，而是一开始就不错；良医治其未病。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为清洁厨房的首要要害在于不要弄脏，最根本的断根策略是多吃生鲜、不动火。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张第一要管住油烟：蔬菜下锅不要带水、不要把橄榄油之类低温油烧到出烟、无法避免油烟蒸腾时及时盖上锅盖、不要大面积裸露复杂表面、买个好点的油烟机。", "evidence": ["E3", "E4", "E5", "E6"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为管住了油烟一般就没有啥了。", "evidence": ["E7"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张第二管住刀具砧板：直接用朝日的合成橡胶砧板（不长霉），肉类叫超市代切，家里根本不切肉、砧板不见油，从而把清洁量压缩到零。", "evidence": ["E8", "E9"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张第三管住锅，先掌握粘锅原理以避免粘锅。", "evidence": ["E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为铸铁煎锅掌握得当可以永远不必清洗，并给出煎牛排后用红酒或矿泉水趁沸腾以木铲搅和、残留物变牛肉浓汁、锅自然干净、再抹油防粘的做法。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张圆底炒锅必须配弧形铲口的锅铲，确保铲到锅底每一点以强力防粘并省下锅刷；并指出锅最容易脏的是汤汁倒出那一侧的锅沿，锅底变黑几乎完全是有机物残留碳化与洗锅不擦干锅底所致。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为残留清洗时稍加注意即可流水冲净，外沿可在装盘后随手用厨房纸巾一抹；内侧结块则每次洗锅时用锅铲铲除铁色。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为锅铲够好的话原则上基本不需要用刷子或钢丝球洗锅；锅内有烧结物不要拿去水龙头下折腾，应开火加水在沸腾态下用锅铲清除。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张残留的油不要用洗洁精洗掉，放回炉子上开火把水蒸发、用厨房纸巾抹匀，这反而可以养锅。", "evidence": ["E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张第四管住碗碟：不要用碗碟直接装易沾污的食材和成菜，改用一次性器皿（一次性木皮船小碟、酱油碟、淋膜防油纸盒、纸火锅铝箔等）；每次做适量、不要剩菜，省去冷藏器皿与清洗。", "evidence": ["E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者断言全部措施到位后清洁工作会最小化到几乎没有，用不着洗碗机、用不着强力清污剂。", "evidence": ["E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者的收束原则是：成本最小的手段不是强力便捷的补救措施，而是一开始就不错——“良医治其未病”。", "evidence": ["E23", "E24"]}
   ],
   "argument_steps": [
    "先立总原则：清洁的首要要害在于不要弄脏（P001）。",
    "给出断根策略：多吃生鲜、不动火（P002）。",
    "第一项：管住油烟，列五条具体做法（P004-P009），并称管住油烟一般就无大问题（P010）。",
    "第二项：管住刀具砧板，用合成橡胶砧板、肉类代切（P011-P013）。",
    "第三项：管住锅——先讲粘锅原理（P014-P015）。",
    "以铸铁煎锅为例展示“永远不必清洗”的操作（P016）。",
    "讲圆底炒锅的锅铲与锅沿碳化、锅底变黑的成因（P017）。",
    "给出洗锅与养锅的具体手法（P018-P022）。",
    "第四项：管住碗碟，用一次性器皿并控制份量（P023-P030）。",
    "归纳结果：清洁工作最小化，用不着洗碗机与强力清污剂（P031-P032）。",
    "以格言收束：成本最小的手段是一开始就不错，良医治其未病（P033-P035）。"
   ],
   "concept_usage": [
    {"term": "不要弄脏", "meaning": "作者提出的核心策略：从源头避免污染，而不是事后强力补救。", "evidence": "P001、P034", "ambiguity": "未说明在必须动火的场景下这一原则的限度。"},
    {"term": "断根策略", "meaning": "指多吃生鲜、不动火这种从根源上取消清洁需求的做法。", "evidence": "P002", "ambiguity": "为作者的比喻性表述，未给适用范围。"},
    {"term": "养锅", "meaning": "把残留的油开火蒸发水后以厨房纸巾抹匀，使锅保持不粘状态的做法。", "evidence": "P022", "ambiguity": "未说明其原理与适用锅具范围。"},
    {"term": "良医治其未病", "meaning": "借用的成语式说法，用于总结“一开始就不错”胜于事后补救。", "evidence": "P035", "ambiguity": "为修辞引用，未注明出处。"}
   ],
   "examples_and_targets": [
    "作者举的具体商品：朝日合成橡胶砧板（P012）、一次性木皮船小碟（P025）、一次性酱油碟（P026）、一次性淋膜防油纸盒（P027）、纸火锅用铝箔（P029）、特百惠冷藏器皿（P030）、洗碗机与强力清污剂（P032）。",
    "作者举的操作实例：煎牛排后用红酒或矿泉水趁沸腾以木铲搅和，残留物变牛肉浓汁（P016）。",
    "作者主张排除的做法：用洗洁精洗掉残留的油（P022）、把锅拿到水龙头下折腾（P021）。",
    "价格信息（作者给出，未核）：一次性酱油碟十五块钱两百个（P026）、淋膜防油纸盒三十块钱 250 个（P027）。",
    "图片节点 IMG001-IMG005：未经核验，内容不明。"
   ],
   "conditions": [
    "P002 用“可以说”弱化“根本不需要清洁”的断言。",
    "P007 以“如果无法避免油烟蒸腾”为条件给出盖锅盖的做法。",
    "P013 以“这样家里根本不切肉”为前提推出清洁量可压缩到零。",
    "P016 以“掌握得当”为前提说明铸铁煎锅可永远不必清洗。",
    "P020 用“原则上”“基本”限定无需刷子的结论。",
    "P025-P029 以“一次性”器皿的可得性为隐含前提；P030 以“每次做适量”为条件。"
   ],
   "rhetoric_and_tone": "清单式操作指南，分“第一／第二／第三／第四”编号推进，条目内再用 1）2）3）分层；语气自信、口语化，夹自我设问与应答（“丑吗？不丑。环保吗？环保。”）；结尾以格言式短句与“良医治其未病”收束，带有训诫意味。",
   "unresolved_questions": [
    "本篇含 5 个图片节点（IMG001-IMG005），图片内容未经核验，需人工／多模态复核；图片与正文条目（尤其 P025-P029 的一次性器皿）的对应关系无法确认。",
    "“朝日”砧板等商品的具体型号、价格与购买信息未完整给出。",
    "“养锅”的原理与适用锅具范围本文未说明。",
    "“多吃生鲜，不动火”是否适用于所有家庭场景，本文未讨论。",
    "P025-P027 的价格为作者所给，未核实。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "清洁厨房的首要要害，在于不要弄脏。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "最根本的断根策略——多吃生鲜，不动火，可以说根本就不需要清洁。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "1）蔬菜下锅不要带水，免得油烟蒸腾。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "2）不要把橄榄油之类的低温油烧到出烟。它不适合做高油温的菜。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "4）不要大面积裸露复杂表面。放在外面的都最好是很容易洗的东西。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "5）买个好点的油烟机。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "管住了油烟一般就没有啥了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "1）砧板直接用朝日的合成橡胶砧板。不长霉，不用折腾了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "从而可以把清洁量压缩到零。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "1）要掌握粘锅的原理，避免粘锅。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "铸铁煎锅掌握得当可以永远不必清洗", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "圆底炒锅一定要配弧形铲口的锅铲，要确保锅铲能结实紧密的铲到锅底的每一个点。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "锅最容易脏的地方就是汤汁倒出那一侧的锅沿，因为有有机物残留，一烧就会碳化。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "而这个残留其实你清洗时稍加注意就可以流水冲净", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "内侧的残留长期不注意会结块，每次洗锅时注意用锅铲将锅沿内侧铲除铁色。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "原则上你的锅铲够好的话，基本不需要用刷子或者钢丝球来洗锅。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "锅内有烧结物，不要拿去水龙头下折腾，学平底锅的方法，开火加水，在沸腾态下用锅铲没有什么弄不下来的。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "残留的油不要用洗洁精洗掉，放回炉子上开火把水蒸发，用厨房纸巾抹匀，这反而可以养锅。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P024", "quote": "不要用碗碟直接装易沾污的食材和成菜，这类食材要用专门的一次性器皿装", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "每次做适量，不要剩菜，于是用不着占用各种冷藏器皿，也省了洗特百惠。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P031", "quote": "全部措施到位，清洁工作会最小化——小到几乎没有的那种。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P032", "quote": "用不着洗碗机，用不着强力清污剂。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P034", "quote": "成本最小的手段，不是强力便捷的补救措施，而是一开始就不错。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P035", "quote": "良医治其未病。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家务整理", "厨房生活", "清洁方法"],
   "issue_candidates": ["厨房清洁策略", "油烟控制", "锅具保养", "减少洗涤量"],
   "text_function_candidates": ["答疑", "经验总结", "操作指南"],
   "object_candidates": ["朝日合成橡胶砧板", "特百惠", "洗碗机"],
   "working_keywords": ["不要弄脏", "断根策略", "管住油烟", "养锅", "一次性器皿", "良医治其未病"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 5 个图片节点（IMG001..IMG005），图片内容未经核验，需图像核验；已读部分为正文文本。故 status=needs_reread、image_checked=false。"
 },
 "502e3528": {
  "analysis": {
   "question_context": "提问者问年轻人准备入手人生第一辆车该如何选车买车（Q001，属提问者）。作者不比较车型，只给出一条原则性答案：以转手为主线——买售后最好、保值性最强的二手车，提前建立卖车的关系，未虑买先虑卖。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "具体做法：买售后最好、保值性最强的二手车；培养二手车经纪的朋友；打通出手车辆的关系线并找到诚信高效的人选资源。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "原则：未虑买，先虑卖。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "推广到一般资产：除打算放进遗产清单的部分，不要购入不易转手、高折旧、没有成熟出售计划的资产。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议人生第一辆车选售后最好、保值性最强的二手车。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议培养几个二手车经纪的朋友，打通出手车辆的关系线，并找到诚信高效的人选资源。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把原则概括为“未虑买，先虑卖”。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者主张除打算放进遗产清单的那部分外，不要购入任何不易转手、高折旧和没有成熟出售计划的资产。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "给出选车结论：买售后最好、保值性最强的二手车（P001）。",
    "给出配套的人脉准备：培养二手车经纪朋友（P002）。",
    "给出渠道准备：打通出手关系线、找到诚信高效的人选资源（P003）。",
    "概括原则：未虑买，先虑卖（P004）。",
    "把原则推广到一般资产：除遗产清单部分，不买难转手、高折旧、无出售计划的资产（P005）。"
   ],
   "concept_usage": [
    {"term": "保值性最强", "meaning": "衡量二手车的首要标准，与“售后最好”并列，理由与后文“先虑卖”一致。", "evidence": "P001、P004", "ambiguity": "未给出判断保值性的具体口径或车型。"},
    {"term": "未虑买，先虑卖", "meaning": "作者的核心原则：购买前先安排好将来如何出手。", "evidence": "P004", "ambiguity": "为格言式表述，未给出执行步骤。"},
    {"term": "遗产清单", "meaning": "作者用以区分“不必考虑转手”的例外资产。", "evidence": "P005", "ambiguity": "为比喻性说法，未明确其实际范围。"}
   ],
   "examples_and_targets": [
    "本文无具体车型、品牌或价格等例证，只有二手车与“不易转手、高折旧”资产这两类对象。",
    "作者提及的现实角色：二手车经纪（P002）、诚信高效的人选资源（P003）。"
   ],
   "conditions": [
    "P005 用“除打算放进遗产清单的那部分，否则不要……”给出例外条件。",
    "P001 用“最”作强度限定，未给比较依据。"
   ],
   "rhetoric_and_tone": "极简清单式回答，五句话成篇，无解释与举例；以四字格言“未虑买，先虑卖”为轴心，末句把买车建议上升为一般资产原则，语气是断言式忠告。",
   "unresolved_questions": [
    "未给出具体车型、价位、年限或保值率数据，也未说明如何判断“售后最好”。",
    "“遗产清单”的实际所指未说明。",
    "提问者问“如何选车买车”，作者未涉及新车与二手车的具体比较、预算或购车流程。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "选售后最好、保值性最强的二手车。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "培养几个二手车经纪的朋友。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "打通出手车辆的关系线，并且找到诚信高效的人选资源。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "未虑买，先虑卖。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "除打算放进遗产清单的那部分，否则不要购入任何不易转手、高折旧和没有成熟的出售计划的资产。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["消费决策", "购车", "个人理财"],
   "issue_candidates": ["人生第一辆车的选择", "二手车与保值率", "资产流动性"],
   "text_function_candidates": ["答疑", "建议清单", "经验总结"],
   "object_candidates": ["二手车", "二手车经纪", "年轻人"],
   "working_keywords": ["二手车", "保值性", "未虑买，先虑卖", "折旧", "转手"]
  },
  "notes": "无图片。本文为极简建议清单，无具体例证与数据，未决问题已登记。"
 },
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
