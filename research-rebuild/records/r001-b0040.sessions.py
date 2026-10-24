# -*- coding: utf-8 -*-
"""批次 r001-b0040 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0040.sessions.py            # 写 out/r001-b0040.out.jsonl
  python3 records/r001-b0040.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0040"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0040.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "575a9421": {
  "analysis": {
   "question_context": "提问者（Q001）问“该不该把保姆当家人看待？”。作者没有停留在这一家庭伦理提问上，而是把它归入自己提出的“内务班子”概念来处理：先定义内务班子（P006），指出保姆问题属于私人管家的职权（P007），判定保姆当然不能当家人（P008），再延伸到“内务班子、外务班子是否应视为家庭成员乃至联姻对象”的一般问题（P015-P017），并明确表示不建议结拜、收义子、纳婿、联姻的路线（P019-P020）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "系列定位与概念提出：本篇是家族系列的一篇，先谈内务班子；第一代家族谈不到这个概念，第二三代则几乎必须有两套班子；外务班子另文再谈。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "定义内务班子：对家务事、个人私产负责的一群人，含保安主管、私人会计、私人律师、私人医生、私人科学顾问、私人管家；保姆能否当家人属于私人管家的职权。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010"], "summary": "给出回答：保姆当然不能当家人；这只是观察私人管家是否称职的窗口；保姆过线则管家受训斥甚至安排退休，且是退休不是解雇。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "理由：解雇内务班子成员是大忌，选定即终身，只可下野、退休，必须保证对方平安喜乐，这是上对下的忠诚；反过来说明选择何等重大，相应试炼另文探讨。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020"], "summary": "把问题一般化：内务、外务班子是否应视为家庭成员，甚至预定联姻对象；指出历史上领袖多有结拜兄弟、收义子、纳婿、联姻之举，作者不建议，理由是几千年历史提示此举不祥。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "回应“这不自相矛盾吗”的两条理由之一：家族成员不等于家庭成员，两者并非疏远次要之别，而是适用不同管理规则，各有各的严厉与温情。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030"], "summary": "第二条理由：当下绝大多数人对待家庭成员的方式是极无原则、极无远见的毁灭性放纵，这种待遇其实是一种伤害；因此争取家人待遇本身是勇敢者游戏，把这种爱加诸只想要宠爱的人是残忍；答案同样是否。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "边界与例外：即使下属心向往之，也应保守对待、不主动招纳；对亲生骨肉是优先而非勉强，且警告不要理解为斯巴达式筛选；唯一例外是深知其难仍坚贞不屈、愿意接受一切必要磨练并接此责任的人。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P042", "P043", "P044"], "summary": "结论：这样的人才是可被当作家人而不会招来诅咒的人；此人可能原是保姆之类的仆人，但资格绝非因保姆或近身侍从身份而自然获得。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者回答提问：保姆当然不能当家人看待。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义内务班子为对家务事、个人私产负责的一群人，并把它与私人管家职权挂钩。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为解雇内务班子成员是大忌：选定即性命相托的终身雇佣，只能下野、退休，必须保证对方一份平安喜乐。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不建议把看重的部属以结拜兄弟、收义子、纳婿、联姻的方式当成亲人，理由是历史提示此举不祥。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分家族成员与家庭成员：不是亲疏轻重之别，而是不同管理规则，各有各的严厉与温情。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为现在绝大多数人对待家庭成员的方式是错的，是毁灭性的放纵，这种待遇其实是伤害。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为把“家人的爱”加诸实际上只想要宠爱的人是残忍，因此对“是否该让下属获得家人待遇”的答案同样是否；即使下属心向往之，也应保守对待、不主动寻求。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者给出唯一例外：深知其难仍坚贞不屈、愿意接受一切必要磨练并愿接这个责任的人，且确认其不图权力荣耀而是确实打算走这条路，才可让其进入家人的道场。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者强调：家人资格绝不是因为某人是保姆或近身侍从而“自然”获得的。", "evidence": ["E16"]}
   ],
   "argument_steps": [
    "提出全文要谈的基本概念：内务班子（P002）。",
    "设定前提：家族处于第一代则谈不到此概念，第二三代则几乎必须有两套班子（P003-P004）。",
    "定义内务班子及其组成，并把提问的保姆问题定位为私人管家的职权（P006-P007）。",
    "直接给出判断：保姆不能当家人；这是考核私人管家的窗口（P008-P009）。",
    "区分“退休”与“解雇”，给出解雇为大忌的理由：性命相托、上对下的忠诚、自我保护本能会导致大出血（P010-P011）。",
    "由终身雇佣反推选择之重，指明试炼另文（P012-P014）。",
    "把问题提升为一般问题：内务、外务班子是否算家庭成员、是否算联姻对象（P015-P016）。",
    "以历史经验为例证反驳结拜、收义子、纳婿、联姻的路线（P017-P020）。",
    "预设读者反问“是否自相矛盾”，给出两条理由：家族成员不等于家庭成员；现行对家人的对待方式本身是错的（P021-P030）。",
    "补充边界：即使对方愿意也不主动招纳；对亲骨肉是优先而非勉强（P031-P039）。",
    "给出唯一例外条件并收束结论（P040-P044）。"
   ],
   "concept_usage": [
    {"term": "内务班子", "meaning": "对家务事、个人私产负责的一群人，含保安主管、私人会计、私人律师、私人医生、私人科学顾问、私人管家", "evidence": "P006", "ambiguity": "与“外务班子”并列，本篇只谈内务班子，外务班子未定义"},
    {"term": "退休/解雇", "meaning": "内务班子成员只能下野、退休，不能解雇；作者以此强调终身性", "evidence": "P010", "ambiguity": "“退休”的具体安排与对价未说明"},
    {"term": "家族成员", "meaning": "与家族正常运作直接相关的核心人员；作者说其不等于家庭成员，适用不同管理规则", "evidence": "P023", "ambiguity": "“家族”与“家庭”的边界由谁划定未说明"},
    {"term": "家人的道场", "meaning": "接受家人待遇所意味的磨练场域，进入条件是深知其难仍坚贞不屈", "evidence": "P041", "ambiguity": "比喻性用法，具体内容未展开"}
   ],
   "examples_and_targets": [
    "保安主管、私人会计、私人律师、私人医生、私人科学顾问、私人管家：作者对内务班子组成的列举（P006）。",
    "结拜兄弟、收义子、纳婿、联姻：作者举出的领袖把部属当亲人的做法，属被作者以“此举不祥”否定的对象（P017-P019）。",
    "历史数据／几千年历史：作者用作否定上述路线的证据，但未给出具体案例（P018-P019）。",
    "斯巴达手段、选蛊策略：作者警告读者不要把自己的话理解为这类筛选子嗣的做法（P033）。",
    "“小兔崽子”“泡蜜饯式的对待”：口语化修辞材料（P025、P035）。"
   ],
   "conditions": [
    "如果你的家族还只是在第一代，那么你目前还谈不到这个概念（P003）；已是第二代第三代，则几乎必须要有两套班子（P004）。",
    "解雇为大忌的前提是内务班子一旦选定即终身雇佣（P011-P012）。",
    "即使下属心向往之、明白代价，也仍要保守对待（P031）。",
    "对自己的子女也只是优先而不能勉强（P039），唯一例外见 P040。",
    "整个磨练过程要适可而止，即使是血脉也未必受得住（P037）。"
   ],
   "rhetoric_and_tone": "训诫与告诫口吻，直接以“我警告你”“我是不建议的”“你不要把这话理解为”对读者下令；大量设问自答（何谓家人、是否矛盾）；用“大忌”“性命相托”“诅咒”“残忍”等重词施压；以“小兔崽子”“泡蜜饯式”“挖坑”类口语化贬抑与比喻行文；结论以“以上。”冷收。",
   "unresolved_questions": [
    "提问者所说的“保姆”与作者定义的“私人管家”是否为同一角色，正文未说明二者关系。",
    "“你们可以回头去翻翻历史数据”未给出任何具体案例或出处，属待外部核查的事实断言。",
    "内务班子的“试炼”标准与内容作者声明另文探讨，本篇未说明。",
    "“内外班子的标准是一致的”“这也是成为家族成员的统一标准”只有一句断言，未给出理由。",
    "brief 在阅读包中被截断（止于“一套内务班子，一”），未据其补写正文；正文亦未提及提问所指的具体保姆情形。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P008", "quote": "答案是不言而喻的——当然不能。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P006", "quote": "内务班子，是对你的家务事、个人私产负责的一群人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "其实是这个私人管家的职权。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P011", "quote": "解雇内务班子的成员是大忌，选择了就是性命相托，没有“分手”可言。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "可以下野、可以退休，但是你必须要保证对方的一份平安喜乐。这是上对下的忠诚。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P019", "quote": "其实几千年的历史已经给了提示——此举不祥。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P020", "quote": "我是不建议走这个路线的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P023", "quote": "第一，家族成员，不等于家庭成员。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P025", "quote": "现在绝大多数人对待自己家庭成员的方式是错的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P025", "quote": "极无原则、极无远见、进而是极不负责任的毁灭性的放纵。这种待遇，其实是一种伤害。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P027", "quote": "把这种爱加诸于实际上只想要宠爱的人们身上，本身甚至是一种残忍。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P030", "quote": "所以答案同样是否。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P031", "quote": "你也要保守对待，不要主动的寻求让他们接纳这种待遇。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P040", "quote": "只有一种例外——深知其难，仍然坚贞不屈的愿意接受一切必要的磨练，愿意接这个责任的人。", "relation": "qualifies"},
    {"key": "E15", "paragraph_id": "P041", "quote": "但你确认他不是贪图所谓的权力和荣耀，而是确实打算选你的路，你可以如他所愿，让他进那个家人的道场。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P043", "quote": "但绝不是因为ta是个保姆或者近身侍从而“自然”获得的这个资格。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家族治理", "组织与人事", "家庭伦理"],
   "issue_candidates": ["保姆能否当家人", "内务班子与外务班子", "下属能否被视为家庭成员", "联姻与结拜式笼络", "家族继承人的教养"],
   "text_function_candidates": ["答疑", "训诫", "经验总结", "概念界定"],
   "object_candidates": ["内务班子", "私人管家", "保姆", "家族第二三代", "领袖与部属"],
   "working_keywords": ["内务班子", "外务班子", "私人管家", "上对下的忠诚", "家族成员", "家庭成员", "家人的道场", "此举不祥"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。brief 在阅读包中截断，仅作导航，未据其补写正文。"
 },
 "5d5b4502": {
  "analysis": {
   "question_context": "提问者（Q001）问“孙杨清白吗？”。作者没有直接回答孙杨是否清白，也未在正文中点名孙杨，而是先指出职业体育圈对“干净”的定义与知乎众的想象不一致（P001），把“有没有问题”转换为检测方式与违规定义问题（P002-P005，并声明为虚拟举例 P006），随后讨论竞技体育背后的利益结构（P007-P013），再把话题转到中国观众对金牌与民族自豪感的尺度（P014-P055）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006"], "summary": "判断“干净”“有没有问题”取决于检测方式与对违规的定义；以阈值、检测时点、检测权重为例说明（作者声明这些是虚拟举例，不要照进现实）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "理由：竞技体育背后的经济利益、社会利益大到不道德、不健康的程度，竞争已不止是更高更快更强，还包括更浓更滑更轻更弹、药物与装备科技等。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012", "P013"], "summary": "推论：有科技条件的前几大强国第一集团内“有罪”“无罪”在脏的程度上差别不大；不踩红线走纯天然路线的队伍基本只是国际旅游团；科技协助足以让九十分的运动员系统打败纯天然天才，而国际体育圈靠几大国养活。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018"], "summary": "结论一：这类八卦不必上升到民族荣誉；冠军不足以说明伟大，只有手续是否合规有国际法实践的技术性看点；希望各位对金牌少点不该有的兴奋。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "提出作者认为真正严肃的问题：中国人的民族自豪感应是什么尺度，并以中美对照连问要读者自问。", "role": "transition"},
    {"unit_id": "U006", "paragraph_refs": ["P023", "P024", "P025", "P026"], "summary": "给出作者期待的姿态：对奥运金牌应是“小儿辈破敌矣”“小儿无赖”式的反应，“泰山崩于前而色不变”，并质问读者是否懂中国人应是什么样的人。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "批评：很多人在追随未经反思的其他民族的自豪观，是作为出生在中国的“美国人”追求美国式自豪；美国的理想未经历史考验，即使“完美的美国”也不是中国应追求的目标；美国低估了中国文化的高度和深度。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "进一步判断：中国不走美国道路不是因为落后走不到，而是美国模式太短视、太脆弱、质量上不值得考虑；美国会越来越像中国并因抗拒“中国路线”被“意外”惩罚；中历史彩票不是真实优秀，真正的审判者是上帝与永续的历史。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048"], "summary": "回应“如果世界冠军不值得骄傲，还有什么值得骄傲”：不推荐“总要找到某种可以骄傲的东西才能活下去”的人生模式；作者自称只是讲事实，事实恰好令你高兴；应学会中性看待事实，不因正面事实骄傲、不因负面事实气馁（以玄烨得天花为例）。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055"], "summary": "回到“自豪的尺度”：引中美人均期望寿命、医疗支出、人口与人均GDP数据，认为其比所有金牌相加值钱百倍不止，以此说明尺度问题，末段追问自信与中华文明自信的来源。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为职业体育圈对于什么叫做“干净”的定义，与知乎众的一般想象不一致。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为是否“没问题”与检测方式和对违规的定义关系很大。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以阈值高低、检测时点、检测权重不同会导致不同结果为例说明上述判断，并明确声明这些是虚拟举例，要求读者不要“比喻照进现实”。", "evidence": ["E3", "E4", "E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为竞技体育背后的经济利益、社会利益已大到不道德、不健康的程度，竞争已不再是更高、更快、更强。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出兴奋剂与训练补剂的竞争只是一个方面，还有各类药物与装备科技助攻，赛场上比赛的已很难说是人。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为对有科技条件的前几大强国而言，只要在第一集团，被裁决有罪或无罪在“脏”的程度上差别不大。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为不把手段用到红线上走钢丝、还走“纯天然”路线的队伍，基本上只是国际旅游团。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为科技协助已足以让九十分的运动员系统打败纯天然天才，并判断整个国际体育圈靠几大国养活，裁判与委员的职业退路都在人间。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这类八卦没有必要上升到民族荣誉，得冠军不足以说明中国多么伟大。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为手续是否合规有国际法实践的技术性看点，但那是纯技术性看点，与国家荣誉无关。", "evidence": ["E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者希望读者对金牌少点不该有的兴奋：得了是好的，但不要上升到“国家民族的荣耀”这个级别，否则不配超级大国大国民的水准。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者提出真正严肃的问题：中国人的民族自豪感应是什么尺度，中国人是否应为美国人所自豪的同一件事自豪。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国人对奥运金牌应是“小儿辈破敌矣”“小儿无赖”式的反应，态度应是泰山崩于前而色不变。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断很多人在追随一种没有反思过的其他民族的自豪观，如同作为出生在中国的“美国人”追求美国式自豪感。", "evidence": ["E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者质疑美国自己的理想是否值得中国追求，指出它还未经过历史考验，即使美国设想中的“完美的美国”也不是中国应追求的目标。", "evidence": ["E26", "E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国不可能走美国道路，原因不是中国落后走不到，而是美国模式在长期历史挑战面前太短视、太脆弱、质量上不值得考虑。", "evidence": ["E28"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者预测读者很有机会看到美国不由自主地越来越像中国，并因极端抗拒“中国路线”被一次次“意外”惩罚。", "evidence": ["E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中历史彩票并不是一种真实的优秀，真正的审判者是上帝和永续的历史，而不是点赞的人。", "evidence": ["E30"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为为金牌激动到面红耳赤或怒火攻心是历史不超过三百年国家才该有的表现，不是五千年文明史国家国民该有的气度。", "evidence": ["E31"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不推荐“总要找到某种可以骄傲的东西才能活下去”的人生模式，认为其埋藏更深的负面因素（怕失去骄傲、自卑或幻想身份攫取骄傲）。", "evidence": ["E32"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自称只是在讲事实，事实恰好令人高兴，其他令人不高兴的事实与本题无关，不应把点赞当作对指引者的感谢。", "evidence": ["E33", "E34"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张应学会有足够勇气接受事实、中性看待事实，不因正面事实“骄傲”，也不因负面事实“气馁”。", "evidence": ["E35"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者引中美人均期望寿命、医疗支出、人口与人均GDP的对比数据，判断这比所有金牌相加还要值钱一百倍不止，以此说明自豪的尺度问题。", "evidence": ["E36", "E37"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者在结尾追问：人当然要有自信，但“自信”到底应该是什么、中华文明的自信来源于何处。", "evidence": ["E38", "E39"]}
   ],
   "argument_steps": [
    "拒绝正面回答孙杨个人是否清白，改以“干净”的定义问题作答（P001）。",
    "把“有没有问题”拆为检测方式与违规定义问题，并举例说明（P002-P005）。",
    "声明上述例子是虚拟举例，禁止读者对号入座（P006）。",
    "给出原因：竞技体育背后的经济与社会利益大到不道德不健康的程度（P007-P010）。",
    "由此推出强国之间的“脏”难以区分、纯天然路线近乎国际旅游团（P011-P012）。",
    "补以科技优势与国际体育圈的资金依赖，说明裁判与委员的处境（P013）。",
    "转向结论：这类八卦不必上升到民族荣誉，只有手续合规有技术性看点（P014-P016）。",
    "提出行动建议与更高一层的问题：少点不该有的兴奋；自豪的尺度是什么（P017-P022）。",
    "给出期望姿态：小儿辈破敌矣式的反应与泰山崩于前而色不变（P023-P026）。",
    "反驳追随他国自豪观的心态，质疑美国理想是否值得追求（P027-P034）。",
    "给出中国不走美国道路的理由与对未来趋势的预测（P035-P041）。",
    "回应“还有什么值得骄傲”，主张中性看待事实（P042-P048）。",
    "回到尺度问题，以中美数据对比作结并留下自信来源之问（P049-P055）。"
   ],
   "concept_usage": [
    {"term": "干净（清白）", "meaning": "职业体育圈内部按检测方式与规则定义判定的合规状态，不等于一般想象的“没有问题”", "evidence": "P001", "ambiguity": "作者未给出“干净”的确定判准，只说是定义与检测方式问题"},
    {"term": "自豪的尺度", "meaning": "中国人应为哪些事、以何种程度感到自豪的衡量标准", "evidence": "P019", "ambiguity": "除中美数据对比外未给出完整尺度"},
    {"term": "中历史彩票", "meaning": "指因历史机运而非真实优秀而得到的位置", "evidence": "P037", "ambiguity": "“中历史彩票”的所指对象需结合上下文，作者未点名"},
    {"term": "自信", "meaning": "作者在结尾追问其内涵，与“骄傲”“虚荣”相区分", "evidence": "P054", "ambiguity": "正文未给出答案，以问题收束"}
   ],
   "examples_and_targets": [
    "1ppm／0.9ppm／0.95ppm 阈值与强弱国差异：作者自述为虚拟举例（P003、P006）。",
    "三点测与五点测、唾液与血液检测权重：作者自述为虚拟举例（P004-P006）。",
    "“哮喘药”“多动症药”“安眠药”、胶水、鲨鱼皮、高弹性弓片、科技鞋：作者举出的赛场科技与药物手段（P010）。",
    "国际旅游团：作者对走“纯天然”路线队伍的贬称（P012）。",
    "“小儿辈破敌矣”“小儿无赖”：作者引用的成语式说法，用于说明应持的态度（P023）。",
    "爱新觉罗玄烨得天花：作者举出的历史例子，用来说明事实的正面／负面难以简单判定（P048）。",
    "中美人均期望寿命、医疗支出、人口、人均GDP数据：P050 以引号引出，未注明出处，作者据此作价值比较（P050-P052）。",
    "美国、中国、前几大强国、国际体育圈、裁判员与委员会委员：被讨论或被批评的对象（P011-P013、P027-P036）。",
    "知乎众：作者在第 1 段设定的对话对象（P001）。"
   ],
   "conditions": [
    "“有没有问题”的结论依赖于检测方式与对违规的定义（P002）。",
    "关于阈值与检测时点的说法被作者限定为虚拟举例，须与孙杨案脱钩（P006）。",
    "对“脏不脏”的判断限定于“有这个科技条件的前几大强国”且“你在第一集团”（P011）。",
    "作者说手续是否合规只是国际法实践的技术性看点，与国家荣誉无关（P016）。",
    "对中国不走美国道路的判断以“不是因为落后走不到，而是因为美国模式……不值得考虑”的排除式限定给出（P035）；对未来的说法用“很有机会会看到”作预测而非断言（P036）。",
    "对古代与当代中国的比较判断，作者称“这种存在感只对当年那个瘦弱贫穷、几乎完全丧失自信的幼年的中国弥足珍贵”（P014），即以时期为条件。"
   ],
   "rhetoric_and_tone": "以答问开篇，先立判断再拆解概念；大量反问句直接质问读者（你们想过没有、你几岁）、讥讽“出生在中国的美国人”“讨打”“国际旅游团”；用“泰山崩于前而色不变”“小儿辈破敌矣”等文言化表达与训诫口吻；末尾连用“一百倍不止／一千倍也不止／甚至一万倍也不止”的递进夸张；以两个问句收束，不给出自信的定义。",
   "unresolved_questions": [
    "提问者问的是孙杨个人是否清白，正文全篇未出现“孙杨”姓名，也未给出对该人的直接判断，只讨论“干净”的判定方式与更广的体育政治经济结构。",
    "P050 引号内的中美数据未注明出处与统计口径，属待外部核查的事实断言。",
    "P055 之后（“中华文明的自信来源于何处？”）在 lexical 结构中标注为未覆盖片段，正文与结构在此处不完全对齐，末句是否完整待核。",
    "“中历史彩票”的具体所指（哪一国的哪一段历史机运）正文未点名。",
    "作者自称 P003-P005 为虚拟举例，但这些例子与提问所涉事件的对应关系未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "答案是——职业体育圈，对于什么叫做“干净”的定义和知乎众的一般想象是不一致的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "到底是不是没问题，和你的检测方式关系很大，和你对违规的定义关系很大。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你规定合法下限是1ppm，那么就会有人用到0.9ppm，强国会搞到0.95ppm。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "你三点来测，跟你五点来测，结果就不一样。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你把唾液检测的权重调高点，或者把血液检测权重调高点，结果就可能不一样。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "我先郑重说明，上面这可是虚拟举例，你们不要“比喻照进现实”。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P007", "quote": "因为竞技体育背后的经济利益、社会利益已经大到了不道德、不健康的程度。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "早就不再是更高、更快、更强的竞争了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "兴奋剂和各种训练补剂的竞争只不过是一个方面而已。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "可以说现在在赛场上比赛的已经很难说是人了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "只要你在第一集团，那么裁决你有罪，你也没比被裁决无罪的脏到哪里去；裁决你无罪，你也没有比有罪的干净到哪里去。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "因为不把这些手段用到在红线上走钢丝的程度，还傻傻的走“纯天然”路线的队伍，基本上都只是国际旅游团罢了。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "科技对运动员水平的提高，已经使得九十分而有充分资本技术协助的运动员足以系统的打败纯天然的天才。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "整个国际体育圈，可以说都是靠这几大国养活的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "所以这类八卦，根本没有必要上升到什么民族荣誉的地步。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P014", "quote": "得了冠军，不足以说明我们多么伟大", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "但这是纯国际法实践的技术性看点，和国家荣誉没什么关系。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P017", "quote": "我更希望各位对金牌少点不该有的兴奋。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P017", "quote": "但是不要上升到“国家民族的荣耀”这个级别。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P019", "quote": "这里提出一个真正严肃的问题——中国人的民族自豪感，应该是什么尺度？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "难道美国人为美国的何事自豪，中国人就应该为中国的同一件事自豪吗？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "中国人对奥运金牌这种事应该是“小儿辈破敌矣”和“小儿无赖”这样的反应。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "我们谈的是什么？泰山崩于前而色不变。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "很多人其实是在追随着一种没有反思过的其他民族的自豪观在追逐根本不该中国人在意的虚荣。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "你们是在作为一名出生在中国的“美国人”，希望中国成为“优秀版的美国”，满足自己美国式的自豪感需求。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P030", "quote": "那本来就是个还没经过历史考验的理想好吗？", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P031", "quote": "即使美国自己设想中的“完美的美国”，其实也根本不是中国应该追求的目标。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "不是因为什么“中国太落后，所以不能走、走不到”，而是因为美国模式在历史的长期挑战面前太短视、太脆弱，在质量上不值得考虑。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "你们很有机会会看到美国一天天的不由自主的变得更像中国，以及因为极端抗拒走“中国路线”而被一次次的“意外”惩罚。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "中历史彩票，并不是一种真实的优秀。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P039", "quote": "这是那些历史不超过三百年的国家才该有的表现，不是一个有五千年文明史的国家国民该有的气度。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P043", "quote": "首先，不推荐“总要找到某种可以骄傲的东西才能活下去”这个人生模式。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P046", "quote": "这只是一种误会。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P047", "quote": "我只是在讲一种事实。事实就是事实，只不过这个事实恰好令你高兴喜欢罢了。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P048", "quote": "你应该学会的是应有足够的勇气去接受事实，学会中性的看待事实。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P050", "quote": "中国的人均期望寿命和美国几乎相当，而中国的人均医疗支出只是美国人的二十分之一。", "relation": "context"},
    {"key": "E37", "paragraph_id": "P050", "quote": "这比所有的金牌相加还要值钱一百倍不止。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P054", "quote": "人当然要有自信才行。但是“自信”到底应该是什么？", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P055", "quote": "中华文明的自信来源于何处？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["体育与竞技", "国际政治", "民族心理与文化自信", "媒体与舆论"],
   "issue_candidates": ["孙杨事件与兴奋剂检测", "职业体育的干净定义", "金牌与民族荣誉", "中国人的自豪尺度", "中美道路比较"],
   "text_function_candidates": ["答疑", "评论", "批评", "论辩"],
   "object_candidates": ["孙杨（提问者提出，正文未点名）", "知乎众", "前几大强国", "国际体育圈", "美国", "中国", "裁判员与委员会委员"],
   "working_keywords": ["干净", "检测方式", "违规的定义", "国际旅游团", "民族荣誉", "自豪的尺度", "小儿辈破敌矣", "泰山崩于前而色不变"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。P055 在 lexical 中标注为未覆盖片段（正文与结构不完全对齐），已记入 unresolved_questions；P050 引号内数据出处未注明。"
 },
 "c5e0fe48": {
  "analysis": {
   "question_context": "提问者（Q001）问“中华民族是一个伟大的民族吗？为什么？”。作者先承认中华民族有生命力、非常重要、地位举足轻重，随即给出否定判断“还不算是真正意义上伟大的民族”（P001-P002），然后重新定义“伟大”与“强大”的区别（P003-P015），最后以“我们还算不上伟大”作结并把问题推向人类争霸循环的终局（P023-P027）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "先肯定中华民族有生命力、重要、地位举足轻重，再提出核心判断：还不算真正意义上伟大的民族。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "以设问界定反面：强大（很强、让人不敢冒犯）不等于伟大，让人仰慕崇拜只是强大的副效应；很多“伟大”赞誉只是偶像崇拜者的空洞贡品。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010"], "summary": "正面定义：让自己繁荣不叫伟大，让别人能繁荣才叫伟大；须有以其他所有人的客观繁荣为己任的使命感并有行动与成效；“客观繁荣”指不考虑自己的意识形态价值观、不把“变得更像我”当作对方关键利益。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015"], "summary": "补充条件：不必丰功伟绩，要的是真诚心意；能向困境中的“敌人”“仇人”伸出援手且族人不视为出卖民族利益；困窘时不反悔怨恨；强大是身强，伟大是心强，身强心不强与伟大无缘，对强大民族而言伟大是一份道德责任。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "把标准用到世界：尚无足够伟大的民族，大家都不及格；古代中国与未抛弃道德责任前的美国曾是接近及格线的候选人，但未迈过线；他们未强大到能承担这份代价，后悔玷污了当初的努力；真正的伟大背后是真正的无私与无怨无悔。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P023", "P024"], "summary": "结论与期望：答案是我们还算不上伟大；作者希望中华民族子孙终有一天明白伟大是沉重而“愚蠢”的理想，仍能无怨无悔地欣然接受。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027"], "summary": "升华到人类处境：人类被困在强国争霸循环中，只有毁灭于一次无法承受的争霸、或终于有一次坐上王座的是真正伟大的民族这两个结局；到那时才知道哪个民族可称伟大。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中华民族很有生命力、非常重要、地位举足轻重，但还不算是真正意义上伟大的民族。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为强、让人不敢冒犯不叫伟大，顶多算强大；让人仰慕崇拜只是强大的副效应。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为很多所谓的“伟大”赞誉只是偶像崇拜者缴纳的空洞贡品，意在换取实利，有的是有意，有的是无意。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义：让自己繁荣不叫伟大，让别人能繁荣才称为伟大。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为伟大须有主动的、明确的、以其他所有人的客观繁荣为己任的使命感，兼且有行动、有成效。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定“客观繁荣”：不考虑自己的意识形态和价值观，不把“变得更像我”定义为对方的关键利益，而是贡献于其他民族的民生纾困与经济繁荣。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者认为不必丰功伟绩，要的是真诚心意，相信“无论是敌是友，天下兴亡，于我有责”。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为能向困境中的“敌人”伸出援手、向“仇人”施以尊重和人道主义，且族人不视其为出卖民族利益的民族，才有资格称为伟大。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为困窘时不反悔、不怨恨“悔不该帮这些白眼狼”的民族才称得上伟大。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为伟大是建基于一份额外的、无怨无悔的责任感和使命感；强大是身强，伟大是心强；身强心不强与伟大无缘；作为强大的民族，“伟大”是一份道德责任。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断这个世界上还没有足够伟大的民族，大家都是不及格的。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为曾恩抚四海的古代中国和没有抛弃自己道德责任之前的美国，算是曾很接近及格线的前几排候选人，但仍未迈过伟大的线。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为他们也不能多加苛责，因为其未曾强大到能承担这份伟大的代价，所以盛极时追逐理想，困窘时却多少有些后悔。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为后悔玷污了当初的努力，把之前无私的帮助追认成了将本求利的利益之举，意味着当初只是自欺欺人的无私。", "evidence": ["E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为真正的伟大背后是真正的无私，无私背后是无怨无悔，这才是真正强者的高傲与高贵的冠冕。", "evidence": ["E22", "E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的答案是：我们还算不上伟大。", "evidence": ["E24"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者希望我们正在走向伟大的路途中，希望中华民族子孙有一天明白伟大是何等沉重而“愚蠢”的理想，仍能无怨无悔地欣然接受。", "evidence": ["E25"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人类被困在强国争霸的无限循环里，这个循环只有两个结局：毁灭于一次无法承受的争霸，或终于有一次坐上王座的是真正伟大的民族。", "evidence": ["E26", "E27"]}
   ],
   "argument_steps": [
    "先给出两项肯定（有生命力、重要），再下否定判断（不算伟大）（P001-P002）。",
    "设问“何谓伟大”，先从反面排除强大与让人崇拜（P003-P005）。",
    "提出正面定义：让别人能繁荣才叫伟大，并加上使命感、行动、成效三项要求（P007-P008）。",
    "界定“客观繁荣”，排除以意识形态同化为目标的“帮助”（P009-P010）。",
    "补充条件：心意而非丰功伟绩、对敌仇亦施援手、族人不以为出卖、困窘不反悔（P011-P013）。",
    "抽象为“身强／心强”之别，并把伟大定为强大民族的道德责任（P014-P015）。",
    "用该标准衡量世界，判定无人及格，并讨论曾经最接近的两个候选者（P016-P019）。",
    "分析后悔如何玷污当初的无私，推出无私与无怨无悔的关系（P020-P022）。",
    "给出结论“我们还算不上伟大”，并表达期望（P023-P024）。",
    "以人类争霸循环的两个结局收束全文（P025-P027）。"
   ],
   "concept_usage": [
    {"term": "伟大", "meaning": "让别人能繁荣、以其他所有人的客观繁荣为己任并有行动成效、无怨无悔的心态与担当", "evidence": "P007-P008", "ambiguity": "作者承认这是一种沉重而“愚蠢”的理想，标准极高，现实中无人达标"},
    {"term": "强大", "meaning": "自己很强、让人不敢冒犯、令人仰慕崇拜；作者称之为伟大之外的另一回事（身强）", "evidence": "P003-P004", "ambiguity": "强大与伟大是否可能部分重叠，正文未展开"},
    {"term": "客观繁荣", "meaning": "不考虑自己的意识形态与价值观，不把“变得更像我”当成对方的关键利益", "evidence": "P009", "ambiguity": "如何判定“客观”未给出操作标准"},
    {"term": "无怨无悔", "meaning": "不会在困窘时反悔、追认此前的帮助为将本求利", "evidence": "P020-P021", "ambiguity": "与“不后悔”的边界由作者以自欺概念解释"}
   ],
   "examples_and_targets": [
    "偶像崇拜者缴纳的空洞贡品：作者对流行“伟大”赞誉的比喻性批评（P005）。",
    "古代中国（曾恩抚四海）：作者举出的接近及格线候选人之一（P017）。",
    "没有抛弃自己的道德责任之前的美国：作者举出的另一候选人（P017），属对美国的限定性评价而非全盘肯定。",
    "“无论是敌是友，天下兴亡，于我有责”：作者引以为伟大心态的说法（P011）。",
    "“悔不该帮这些白眼狼”：作者引作反悔者口吻的说法（P013）。",
    "强国争霸、坐上王座：作者用于描述人类历史循环的叙述框架（P025-P026）。"
   ],
   "conditions": [
    "不强、不让人冒犯、不被仰慕，都不足以称伟大（P003-P004）。",
    "伟大要求有行动、有成效，且不以意识形态同化为目的（P008-P009）。",
    "不要求丰功伟绩，但要求真诚心意（P011）。",
    "对“敌人”“仇人”施援且族人不视为出卖，才构成资格（P012）。",
    "困窘时不反悔是必备条件（P013）。",
    "作者对古代中国与美国用了“曾经很接近及格线的前几排候选人”“还没有迈过真正的伟大的线”等限定语（P017-P018）。",
    "作者承认他们“不能多加苛责”，理由是其未曾强大到能承担代价（P019）。"
   ],
   "rhetoric_and_tone": "以设问（何谓伟大？）反复切分概念，语气庄重近于训诫与布道；把自己的标准称为沉重而“愚蠢”的理想，带自嘲与悲壮色彩；对偶像崇拜式赞誉使用“空洞的贡品”“虚无的捐纳”等贬抑比喻；结尾以人类毁灭或真正伟大民族坐上王座的两结局收束，带末世论式修辞。",
   "unresolved_questions": [
    "“伟大”的判定由谁作出、以何种证据认定，正文未说明；标准本身由作者提出。",
    "对古代中国“恩抚四海”与美国“没有抛弃自己的道德责任之前”的历史叙述未给出具体史实与时期，属待外部核查。",
    "“世界上还没有足够伟大的民族”是作者的总体断言，未列举全部候选者。",
    "未说明按此标准衡量时，当代中国的具体差距与改进路径（只有期望，无行动方案）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中华民族是一个很有生命力的民族。中华民族也是世界上非常重要、地位举足轻重的民族。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P002", "quote": "但是中华民族还不算是真正意义上伟大的民族。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "何谓伟大？不是自己很强，很让人不敢冒犯。这不叫伟大，顶多算强大。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "也并不是让人仰慕，让人崇拜，让人趋之若鹜。这只是强大的副效应。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "很多所谓的“伟大”赞誉，只是偶像崇拜者缴纳的空洞的贡品，试图靠这些虚无的捐纳换到某些实利罢了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "让自己繁荣不叫伟大，让别人能繁荣才称为伟大。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "有主动的、明确的、以其他所有人的客观繁荣为己任的使命感，兼且有行动，有成效，才成其为伟大。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "“客观繁荣”，这意思是不考虑自己的意识形态和价值观，不把“变得更像我”定义为对方的“关键利益”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "不必丰功伟绩，要的是这个心意", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P011", "quote": "相信“无论是敌是友，天下兴亡，于我有责”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "能向困境中的“敌人”伸出援手、能向“仇人”施以尊重和人道主义，而其族人能够视其为当然义务，不会大规模的大骂“出卖民族利益”——这样的民族，才有资格称为伟大。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "这样做了，不会在自己困窘时反悔，咬牙切齿的怨恨“悔不该帮这些白眼狼”的民族，才有资格称得上伟大。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "伟大，是建基于一份额外的、无怨无悔的责任感和使命感。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "强大是身强，伟大是心强。心强身不强，仍然是伟大的，只是结果常常令人遗憾。但身强、心不强，则是与“伟大”无缘的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "作为一个强大的民族，“伟大”是一份道德责任。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "从这个意义上说，这个世界上还没有足够伟大的民族，大家都是不及格的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "曾经恩抚四海的古代中国和没有抛弃自己的道德责任之前的美国算是曾经很接近及格线的前几排候选人。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "这难能可贵，但是还没有迈过真正的伟大的线。", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P019", "quote": "他们并未曾强大到能承担得起这份伟大的代价的程度。", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P019", "quote": "所以，当盛极的时候，ta们追逐了自己的理想，在困窘的时候却多少有些后悔。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P020", "quote": "这一后悔，就玷污了自己当初的努力，把之前无私的帮助追认为了一种将本求利的利益之举。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P021", "quote": "真正的伟大背后是真正的无私，而真正的无私，背后是无怨无悔。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P022", "quote": "这份无怨无悔，才是真正的强者的高傲，真正的高贵的冠冕。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P023", "quote": "所以，答案是我们还算不上伟大。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P024", "quote": "希望中华民族的子孙们能够有一天在毫无疑问的明白伟大是一种何等样沉重而“愚蠢”的理想，而仍然能真正无怨无悔的欣然接受。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P025", "quote": "人类一直被困在“强国争霸，此起彼伏”的无限循环里", "relation": "context"},
    {"key": "E27", "paragraph_id": "P026", "quote": "这个循环只有两个结局——人类最终毁灭于一次无法承受的争霸，或者终于有一次，坐上王座的是一个真正伟大的民族。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文明比较", "民族心理", "历史哲学", "国际政治"],
   "issue_candidates": ["中华民族是否伟大", "伟大与强大的区别", "客观繁荣与意识形态输出", "道德责任与无怨无悔"],
   "text_function_candidates": ["答疑", "概念界定", "评论", "训诫"],
   "object_candidates": ["中华民族", "古代中国", "美国", "偶像崇拜者", "强国争霸中的各国"],
   "working_keywords": ["伟大", "强大", "客观繁荣", "无怨无悔", "天下兴亡", "道德责任", "强国争霸"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。"
 },
 "7e19ce1e": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么很多人会觉得自己不配被爱？”。作者不把它当作心理症状来解释，而是直接翻转命题：没有人配被爱（P001），人爱你是因为ta们决定要爱你（P002），并进一步用“被爱资格考”的比喻（P011 起）说明“配不配”这套评分机制本身如何运作、为何必然人人不及格，最后给出“无人配得爱，包括我自己”作为爱与接受爱的前提（P042）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "核心命题：没有人配被爱；爱是出于对方决定要爱，与你的条件无关；坚守这一认知是对爱你的人最基本的爱，也是“配与不配”资格问题的第一条要求。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "推论：任何认为自己配得爱的人必然不配；但“不配”不成问题，因为爱本就是交给不配的人的，否则只是崇拜、贿赂或投资。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012"], "summary": "引入比喻：假设有“被爱资格考”，及格分60分，并开始考察这条规则实际如何执行。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "评分机制的缺陷：评卷人年幼时凭片面证据评分（写得好、画得好即想象全面及格）；社会习俗与从众压力要求快速评完；考生学会应试技巧，在有利时机与条件下作最好展现；主考官年轻识浅、标准超低并故意放水，使“全面的被爱资格试”被偷换成“被爱的首轮资格试”。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028"], "summary": "高分基础必然被挑战：自我激励的心理动力散失、主考官见多识广，分数逐年下滑且斜率不收敛；当初的高分只是没见过真正好字好文好画的结果，其他科目估计也错；阅历增长后同一份试卷评得更低。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034"], "summary": "机制结论：考试科目无数，要求每科都过60分不现实；一门八十分不能抵消另一门不及格；只要一门不及格，所有优秀都无意义；这不是平均分制而是以最低分为准制；因此只要是有限的人都是不配的。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P035", "P036", "P037", "P038"], "summary": "由结论转出实践含义：明白这一点才是付出真正谈得上爱的关键；爱有绕不过去的前提——必将赋予一个不配的人，并作为一个不配的人接受它；由此你的爱成为知情同意之下付出的爱，对方再没有“辜负”的可能，也不再被强制要求回报，爱里附赠自由。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043"], "summary": "接受爱的一方：只能接受同样明白这一点的人的爱，才能在预先同意的“用户协议”下免于被时时审判、定罪与“抽走银根”的恐惧；微薄而接受协议的是爱，丰厚而未接受协议的是债；无论给爱还是得到爱，都必须从接受“无人配得爱，包括我自己”开始，逻辑上没有其他解。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P044", "P045", "P046"], "summary": "收束：在一切不及格之中，懂得这一点的人分数才是正的；不懂的人无论素质多优秀分数是负的，因为其能力会用来向你要债，收得越多越近乎奴隶；所以在一切不配之中，懂得这一点的人总是更配。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言没有人配被爱；有人爱你只是因为ta们决定要爱你，不是因为你配被爱。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为无论对方付出多么微不足道、你多么人中龙凤，这个结论都不变；坚守这一认知是对爱你的人最基本的爱。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者设定：如果爱有所谓配与不配的资格问题，那么有这个认知是认证要求的第一条。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为任何认为自己配得爱的人，都必然不配。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为爱注定是交给不配的人的，正因如此它才是爱；否则不过是崇拜、谋求青睐的贿赂或投资。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以“被爱资格考（及格分60分）”为比喻，说明配不配的资格实际上如何被评分执行。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者描述评卷缺陷：评卷人年幼时凭片面证据（字好、文好、画好）就给超过六十分的评分；社会习俗与从众本能又要求很快评完卷子。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为考生会无师自通学会应试技巧，在有利时机与条件下作最好展现，诱使考官由局部优良想象总体最高分。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为主考官年轻识浅、判断力肤浅、标准超低并故意放水，以致“全面的被爱的资格试”被偷换成“被爱的首轮资格试”，其分数有效性之低令父母辗转难眠。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测这两个高分基础随着剧情发展一定受到严重挑战：心理动力散失、主考官见多识广，分数每年下滑，斜率不收敛。", "evidence": ["E19", "E20"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者说明分数下滑的原因：当初的高分只是没见过真正好的字、文、画的结果，据以想象的其他科目高分部分是错误估计；阅历增长后同一份试卷评得更低。", "evidence": ["E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出评分体系残酷：考试要考无数科目，要求每科都至少60分以上不现实；一门八十分不能抵消另一门不及格；只要一门不及格所有优秀都无意义。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者结论：这场考试不是平均分制，而是“以最低分为准制”；所有人只要是有限的人，都是不配的。", "evidence": ["E26", "E27"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为明白“人人不配”这一点，恰恰是你的付出真正谈得上爱的关键，也是爱之所以为爱的前提。", "evidence": ["E28"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出爱绕不过去的前提：要么抛弃它，要么接受游戏规则——必将把它赋予一个不配的人，并作为一个不配的人来接受它。", "evidence": ["E29"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为从此付出的爱是知情同意之下的爱，对方再没有“辜负”的可能，“不配”也不再构成欺骗；同时解除了对方必须如何才配得上、对得起你的爱的强制性要求，爱里附带无价的礼物——自由。", "evidence": ["E30", "E31"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为明白这一事实后，你只能接受同样明白这一点的人的爱，因为只有在这预先同意的“用户协议”之下才能免于被时时审判、定罪与“抽走银根”的恐惧。", "evidence": ["E32"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者区分爱与债：无论多么微薄，接受这协议的才是爱，拿到就是受益；无论多么丰厚，没有接受这协议的都是债，拿到就是欠债。", "evidence": ["E33", "E34"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张：无论想给人爱还是想得到爱，都必须从完全接受“无人配得爱，包括我自己”这一条理念开始，逻辑上没有其他解。", "evidence": ["E35", "E36"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者判断：在一切不及格之中，懂得这一点的人分数才是正的；不懂的人无论个人素质多优秀分数其实是负的，因为其能力与“付出”将来都要你连本带利归还，收得越多越近乎奴隶。", "evidence": ["E37", "E38"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者重申：在一切不配之中，懂得这一点的人总是更配。", "evidence": ["E39"]}
   ],
   "argument_steps": [
    "给出反直觉起点：没有人配被爱（P001）。",
    "给出理由：爱源于对方决定要爱，不取决于被爱者的条件（P002-P003）。",
    "把该认知定为对爱的基本义务与资格要求第一条（P004-P005）。",
    "推出“自认配得者必然不配”，并消解“不配”的负面含义（P006-P009）。",
    "以“被爱资格考”比喻重构问题（P010-P012）。",
    "逐项拆解评分机制的缺陷：片面评分、快速评卷、应试技巧、考官低标准与放水（P013-P021）。",
    "说明高分基础必然崩解与分数下滑趋势（P022-P028）。",
    "得出结论：科目无数、不可抵消、以最低分为准，人人不配（P029-P034）。",
    "转出实践含义：知情同意的爱、无“辜负”、附带自由（P035-P038）。",
    "说明接受爱一侧的条件与“爱与债”的区分（P039-P041）。",
    "给出总原则并收束为正分／负分的判别（P042-P046）。"
   ],
   "concept_usage": [
    {"term": "配被爱", "meaning": "一种被作者设定为虚构的资格判定；作者主张无人合格，且自认合格者必然不合格", "evidence": "P006", "ambiguity": "作者先以反问式“没有人配被爱呀”立论，后又称“如果爱有所谓配与不配的资格问题”（P005），资格问题本身被设定为假设"},
    {"term": "被爱资格考", "meaning": "作者用来说明评分机制（考官、考生、科目、分数）的比喻", "evidence": "P011", "ambiguity": "比喻与现实的对应关系未完全逐项说明"},
    {"term": "以最低分为准制", "meaning": "只要一门不及格，其他优秀都无意义的评分规则", "evidence": "P032", "ambiguity": "“科目”具体指哪些方面，正文只举了物理、化学、数学等示例"},
    {"term": "用户协议", "meaning": "双方预先同意“无人配得爱”这一前提的比喻性说法", "evidence": "P039", "ambiguity": "原文此处引号作“用户协议“（后引号方向与常例不同），系原文标点，未作改动"},
    {"term": "债", "meaning": "未接受该协议而给出的丰厚付出，接受者要连本带利归还", "evidence": "P041", "ambiguity": "与“爱”的界限由是否接受协议判定"}
   ],
   "examples_and_targets": [
    "“被爱资格考”、评卷人、考生、主考官、60分及格线：作者自造的核心比喻（P011-P034）。",
    "写字很漂亮／一篇作文很优秀／画一手好画：作者举例说明片面证据如何被推广为全面高分（P014、P026）。",
    "高分物理、高分化学、高分数学；物理几乎是零分，化学三十，数学二十五：作者虚构的科目分数示例（P026）。",
    "约会时展现完美：作者举例说明应试技巧（P018）。",
    "“抽走银根”“用户协议”：作者使用的经济与契约类比喻（P039）。",
    "“辜负”“欺骗”：被作者重新解释的通俗说法（P037）。"
   ],
   "conditions": [
    "“配与不配的资格问题”被作者明确设为假设条件（P005）。",
    "评分机制的描述限定在“评卷人自己年纪很小的时候”“主考官们自己还没有见过世面”等条件下（P013、P019）。",
    "分数下滑被表述为趋势判断（一定受到严重挑战、不是收敛的），并附带“如果不是飞速跳水的话”的退让（P022-P025）。",
    "接受爱的一侧作者用“只能接受同样明白这一点的人的爱”给出限定（P039）。",
    "作者把结论限定为对“有限的人”的判断（P034）。"
   ],
   "rhetoric_and_tone": "开篇以口语化断言“没有人配被爱呀”定调，随后用考试比喻铺陈，语气从调侃（乖乖式反问“但是不配又怎样呢？”）转为冷峻推演；大量使用“残酷”“无价”“奴隶”“欠债”等强对比词；对读者使用第二人称“你”直接下判断与要求，末尾以“逻辑上没有其他解”作封闭式收束。",
   "unresolved_questions": [
    "提问者问的是“为什么很多人会觉得自己不配被爱”，作者没有直接解释这种心理的成因，而是主张“不配”是普遍事实；两者关系正文未说明。",
    "“被爱资格考”是比喻还是作者认为的实然机制，正文未明确。",
    "“物理、化学、数学”的分数示例属虚构举例，作者未说明对应现实中的哪些品质。",
    "P039 “用户协议“ 一处引号方向与常规不同，系原文标点，未作改动。",
    "父母“辗转难眠”一句中的父母指代哪一方（考官的父母还是考生的父母）正文未明确。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "没有人配被爱呀。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "有人爱你只是因为ta们决定要爱你，根本不是因为你配被爱。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "无论对方付出的是多么微不足道，而你是多么人中龙凤、如何伟大，这个结论都是不会变的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "坚守这个基本认知，是你对爱你的人的最基本的爱。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "如果爱有所谓配与不配的资格问题，那么有这个认知是认证要求的第一条。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "任何认为自己配得爱的人，都必然不配。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "爱注定是交给不配的人的。正因为它是交给不配得的人，它才是爱。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "否则，不过是崇拜、不过是谋求青睐的贿赂、不过是投资罢了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "假设有一种“被爱资格考”，而且及格分60分。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "现在我们来看看这条规则实际上是怎么被执行的——", "relation": "context"},
    {"key": "E11", "paragraph_id": "P013", "quote": "最初，在评卷人自己年纪很小的时候，常常因为缺少综合评卷的能力而凭借片面的证据评分。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "从而给出了超过六十分的评分。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "ta们觉得自己必须要在一个很短的时间内评完卷子，好歹挑出一个及格的来完成自己眼下的人生科目。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "“考生”们哪怕不经过任何训练，也会明白这个考试的缺陷所在，所以纷纷学会了“应试技巧”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "约会的时候展现完美，诱使对方想象出整体的完美。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "主考官们自己还没有见过世面，一般家庭也极少做洞察力的训练", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "考试机制本来就已经在实质上将“全面的被爱的资格试”偷换成了“被爱的首轮资格试”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "这轮考试得出的分数的有效性之低，不知令多少父母辗转难眠。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "上面这两个高分基础，随着剧情发展是一定会受到严重挑战的。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P025", "quote": "主考官们也已经看到了悲观的趋势——向下的斜率不是收敛的，甚至看起来不是匀速的。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P026", "quote": "原来当初的“写字很漂亮/一篇作文很优秀/画一手好画”，仅仅只是我没有见过真正的好字、好文、好画的结果。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P027", "quote": "不但如此，随着我的阅历增长，同一份试卷让我再评，连二十五分都没有了。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P029", "quote": "这个评分体系是如此的残酷——它其实要考无数科目，以至于要求每一科都至少有60分以上是不现实的。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P030", "quote": "而另一方面，更加残酷的是，这一门八十分，并不能“抵消”另一门的不及格。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P031", "quote": "只要一门不及格，所有的优秀都无意义。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P032", "quote": "原来这场考试不是平均分制，而是“以最低分为准制”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P034", "quote": "所有人，只要是有限的人，都是不配的。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "而明白这一点，恰恰是你的付出真正谈得上爱的关键。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "你必将将它赋予一个不配的人，并且你必将作为一个不配的人来接受它。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "你再赋予人的爱，就是你自己知情同意之下付出的爱。对方再没有“辜负”的可能。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P038", "quote": "于是，你的爱里面除了最基本的物质帮助，还附带了一份无价的礼物——自由。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P039", "quote": "只有在这预先同意的“用户协议“之下，你才能免于被时时审判、时时定罪，被随时随地“抽走银根”的恐惧。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P040", "quote": "无论多么微薄，只有接受了这个协议的，才是爱，你拿到了就是受益的。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P041", "quote": "无论多么丰厚，没有接受这协议的，都是债，你拿到了就是欠债的。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P042", "quote": "都必须从完全接受“无人配得爱，包括我自己”这一条理念开始。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P043", "quote": "逻辑上没有其他解。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P044", "quote": "所以，在一切的不及格之中，懂得这一点的人分数才是正的。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P045", "quote": "不懂的人，无论其个人素质多么优秀，其实分数是负的", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P046", "quote": "所以我说在一切不配之中，懂得这一点的人总是更配。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["情感与亲密关系", "伦理与价值观", "心理机制"],
   "issue_candidates": ["配不配被爱", "爱的资格与条件", "应试式展现与评分", "爱与债的区分", "知情同意的爱"],
   "text_function_candidates": ["答疑", "论辩", "概念界定", "劝导"],
   "object_candidates": ["提问者", "评卷人／主考官", "考生", "父母", "爱你的人"],
   "working_keywords": ["配被爱", "被爱资格考", "应试技巧", "以最低分为准制", "无知之幕式的用户协议", "自由", "债"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。P039 原文引号作“用户协议“，为原文标点，未改写。"
 },
 "87e68270": {
  "analysis": {
   "question_context": "提问者（Q001）问“聪明有什么坏处？”。作者没有分点列举，而是用五行短句给出一个总括判断：聪明大多被用在自我欺骗与推卸、攻击性的话术上，最终是给自己挖坑（P001-P005）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总起：聪明人骗起自己来，神仙都挡不住。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "列举聪明的实际用途：否认事实、推卸责任、冷嘲热讽、以辞害意、造谣、诬陷、说谎；并判断人的聪明绝大部分都用在这些把戏上。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "以比喻收束：满把子力气大多数时候用来给自己挖坑，挖坑挖到练出一身腱子肉。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为聪明人骗起自己来，神仙都挡不住。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列举聪明的常见用途：否认事实、推卸责任、冷嘲热讽、以辞害意、造谣、诬陷、说谎。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断人的聪明其实绝大部分都用在这些把戏上。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这些力气大多数时候被用来给自己挖坑。", "evidence": ["E4"]}
   ],
   "argument_steps": [
    "以自欺为最大坏处总起（P001）。",
    "列举聪明被使用的具体方向（P002）。",
    "把列举提升为总体比例判断（P003）。",
    "用“挖坑／腱子肉”的比喻作结，不含解决办法（P004-P005）。"
   ],
   "concept_usage": [
    {"term": "聪明", "meaning": "本文中主要指用于自我欺骗、推卸责任与话术攻击的心智能力", "evidence": "P002-P003", "ambiguity": "作者未区分聪明的正面用法，也未给定义"},
    {"term": "挖坑", "meaning": "比喻聪明反害自身的结果", "evidence": "P004", "ambiguity": "“坑”的具体所指未说明"}
   ],
   "examples_and_targets": [
    "否认事实、推卸责任、冷嘲热讽、以辞害意、造谣、诬陷、说谎：作者列举的七种“把戏”（P002）。",
    "“乖乖隆地咚”“满把子力气”“腱子肉”：口语化与方言色彩的修辞材料（P001、P004-P005）。"
   ],
   "conditions": [
    "本文为短答，未给出“聪明在何种条件下才带来好处”的说明，也未加限定语。"
   ],
   "rhetoric_and_tone": "极简短答，五行成篇；以方言口语“乖乖隆地咚”起句，用夸张和连续排比列举，末尾以“挖坑挖到练出一身腱子肉”的黑色幽默反讽收束，无解释、无论证展开。",
   "unresolved_questions": [
    "正文只有 131 字，未说明“聪明”的定义、判断依据或例证，也未给出应对办法。",
    "作者列举后以省略号结束（P002），是否还有未尽项目本文未说明。",
    "“绝大部分”是作者的总体判断，正文未给出数据或来源。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "聪明人骗起自己来，乖乖隆地咚，神仙都挡不住。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "聪明用在否认事实上，用在推卸责任上，用在冷嘲热讽上，用在以辞害意上，用在造谣上，用在诬陷上，用在说谎上……", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "人的聪明，其实绝大部分都用在这些把戏上了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "满把子力气，大多数时候用来给自己挖坑。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["认知与心理", "为人处世"],
   "issue_candidates": ["聪明的坏处", "自欺", "聪明被用于话术与推责"],
   "text_function_candidates": ["答疑", "短评", "讽刺"],
   "object_candidates": ["聪明人"],
   "working_keywords": ["聪明", "骗自己", "以辞害意", "挖坑", "腱子肉"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。本篇为超短答（131 字），无展开论证。"
 },
 "7ccadecd": {
  "analysis": {
   "question_context": "提问者（Q001）问“没专业背景的人自学houdini，可否请大佬们给我指条明路？”。作者给出一条自称最短、最直、最实惠、适用于自学一切公开技术的通用路径（P001），用六步列出做法：找 QQ 兴趣群、问前发红包、答后发红包、请前辈引入更内圈社区、以啃完官方手册和案例为主线、为大佬打下手；最后判断走到这一步行业想进就进（P008-P010）。正文未涉及 houdini 的专业内容。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "总起：作者称自己给的是一条最短、最直、最实惠的通用明路，永远适合自学一切公开的技术。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "前两步：搜索 QQ 相关兴趣群（人越多越好、建立时间越久越好、优先教材读者群或作者官方群）；入群后问问题之前必先发红包；得到解答后必发红包（参与者小额随机红包，被采纳者按所花时间发大红包）。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "关于红包的补充说明：对方很可能推辞，但收不收在ta，给不给在你；要主动，不废话。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007"], "summary": "后三步：建立关系与经验后请经验最丰富的前辈拉进更活跃和内圈的社区；在社区支持下以啃完官方手册和案例为主线推进，学习完成的标准是啃完手册而不是做出让外行惊叹的作品；自告奋勇为大佬打下手，免费或低费用参与项目边角实践。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009", "P010"], "summary": "结论与宽慰：走到这一步这个行业想进就进，职业路基本上最直；行业和这些前辈永远缺这样的人；敞开发红包也不及培训班学费多。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称自己给出的是一条最短、最直、最实惠的通用明路，永远适合于自学一切公开的技术。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议搜索 QQ 兴趣群并遵循三个原则：人越多越好、建立时间越久越好、最好找教材读者群或教材作者官方群。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要求入群后问问题之前必先发红包，问题得到解答后必发红包，并按贡献分配：参与者小额随机红包，回答被采纳者按所花时间发大红包。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者提醒对方很可能推辞，但收不收在对方、给不给在自己，要主动、不废话。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议建立一定关系与经验后，请经验最丰富的前辈把自己拉进更活跃和内圈的社区。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张在社区支持下以啃完官方手册和案例为主线推进，并把学习完成的标准定为啃完手册，而不是做出让外行惊叹的作品。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议自告奋勇为大佬打下手，免费或低费用参与项目边角实践。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者判断走到这一步基本上这个行业想进就进，职业路基本上是最直的，行业和这些前辈永远缺这样的人。", "evidence": ["E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为敞开发红包也不及交给培训班的学费多。", "evidence": ["E11"]}
   ],
   "argument_steps": [
    "先声明所给路径的通用性与“最短、最直、最实惠”的定位（P001）。",
    "按序号给出六步操作（P002-P007）。",
    "在第三步内补充红包的给与不收的处理原则（P004）。",
    "为第五步设定学习完成的判定标准（啃完手册而非作品）（P006）。",
    "以职业前景和成本比较收尾（P008-P010）。"
   ],
   "concept_usage": [
    {"term": "明路", "meaning": "作者所称自学一切公开技术的通用路径，以进入社区并遵守互惠规则为核心", "evidence": "P001", "ambiguity": "作者未说明该方法对无网络社区资源的领域是否适用"},
    {"term": "红包", "meaning": "向社群提问与答谢时给出的金钱回报，被作者当作进入圈子的通行做法", "evidence": "P003-P004", "ambiguity": "金额、频率只给出“小额随机”“按所花时间”的相对标准"},
    {"term": "学习完成的标准", "meaning": "作者定义为啃完官方手册，而非做出让外行惊叹的作品", "evidence": "P006", "ambiguity": "“啃完”的程度与检验方式未展开"}
   ],
   "examples_and_targets": [
    "QQ 群、兴趣群、教材读者群、教材作者官方群：作者推荐的具体渠道（P002）。",
    "红包、小额随机红包、大红包：作者提出的互惠做法（P003-P004）。",
    "官方手册和案例：作者指定的学习主线材料（P006）。",
    "给大佬打下手、项目边角实践：作者建议的入行方式（P007）。",
    "培训班学费：作者用作成本比较的对照项（P010）。",
    "houdini：仅出现在提问者的提问中，正文未提及该软件或相关专业内容。"
   ],
   "conditions": [
    "方法被作者限定为适用于“自学一切公开的技术”（P001）。",
    "选群三原则使用了“如果有可能，最好是……”的限定（P002）。",
    "第四步以“建立一定关系且有一定经验后”为前提（P005）。",
    "第五步以“在社区支持之下”为前提（P006）。",
    "第六步的实践参与被限定为“免费或者低费用”（P007）。",
    "对结果的判断用“基本上”限定（P008）。"
   ],
   "rhetoric_and_tone": "以“我告诉你”开篇的指点式口吻，条目编号清晰、可执行性强；用“必先”“必发”“要主动，不废话”等命令句；末段以“放心，敞开了发红包”作安抚性收尾；全篇不含讽刺，接近经验传授与操作指南。",
   "unresolved_questions": [
    "正文完全没有提到 houdini，也没有讨论“没专业背景”如何补足，提问的具体专业问题未获回答。",
    "“永远适合于自学一切公开的技术”是作者的普遍性断言，未给出适用边界或反例。",
    "红包金额、发放频率、群规模等只有相对标准，无具体数值。",
    "作者身份与相关行业经验的依据正文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我告诉你一条最短、最直、最实惠的通用明路，永远适合于自学一切公开的技术。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "1）搜索qq群里的相关兴趣群。遵循三个原则：人越多越好；建立时间越久越好；如果有可能，最好是找那种教材的读者群或者教材作者官方群。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "2）入群后，问问题之前必先发红包。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "3）问题得到解答后必发红包。参与者都有小额随机红包，回答被采纳者按所花时间发大红包。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "对方很可能推辞，但收不收在ta，给不给在你。要主动，不废话。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P005", "quote": "4）建立一定关系且有一定经验后，请经验最丰富的前辈拉进更活跃和内圈的社区。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "学习完成的标准是你把手册啃完了，而不是做出了什么让外行惊叹的作品。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "6）自告奋勇为大佬打打下手，免费或者低费用参与项目边角实践。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "走到这一步，基本上这个行业你想进就进，而且职业路基本上是最直的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "行业和这些前辈永远缺你这样的人。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "放心，敞开了发红包，也不及你交给培训班的学费多。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["自学方法", "职业发展", "社群交往"],
   "issue_candidates": ["无专业背景自学技术", "进入行业社群的方式", "红包式互惠", "以手册为主线的学习标准"],
   "text_function_candidates": ["答疑", "行动指南", "经验总结"],
   "object_candidates": ["提问者", "QQ 群与兴趣群", "教材作者", "前辈与大佬", "培训班"],
   "working_keywords": ["明路", "qq群", "红包", "官方手册", "打下手", "边角实践"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。提问提到 houdini，但正文未涉及该软件或任何具体专业内容，仅给通用方法。"
 },
 "5316551a": {
  "analysis": {
   "question_context": "提问者（Q001）问“狄俄尼索斯为什么可以取代宙斯？”。作者只以一句因果句作答：麻醉剂必将替代兴奋剂成为人类最廉价的终极方案（P001）。正文未出现狄俄尼索斯或宙斯的名字，也未解释该神话命题与这句话的对应关系。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "唯一一句：麻醉剂必将替代兴奋剂成为人类最廉价的终极方案。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者判断：麻醉剂必将替代兴奋剂，成为人类最廉价的终极方案。", "evidence": ["E1"]}
   ],
   "argument_steps": [
    "直接以“因为……必将……”给出预言式回答，无前提、无例证、无展开（P001）。"
   ],
   "concept_usage": [
    {"term": "麻醉剂", "meaning": "被作者视为将取代兴奋剂的“人类最廉价的终极方案”", "evidence": "P001", "ambiguity": "未说明指药物意义上的麻醉剂还是比喻义，也未给出“终极方案”针对的问题"},
    {"term": "兴奋剂", "meaning": "被作者设定为将被麻醉剂取代的现有方案", "evidence": "P001", "ambiguity": "与体育语境中的兴奋剂是否同义，正文未说明"},
    {"term": "狄俄尼索斯／宙斯", "meaning": "仅出现在提问者的问题中，正文未使用", "evidence": "P001", "ambiguity": "作者未说明酒神取代天神的比喻对应何物"}
   ],
   "examples_and_targets": [
    "狄俄尼索斯取代宙斯：提问者提出的神话命题，正文未出现该名字，也未展开对应（Q001）。",
    "麻醉剂、兴奋剂：作者用于作答的两个对照项（P001）。"
   ],
   "conditions": [
    "作者用“必将”作全称预测，未附条件、时间尺度或适用范围（P001）。"
   ],
   "rhetoric_and_tone": "极简短答，一句话成篇；以“因为……必将……”的断然语气作答，不作解释，带有预言式与戏谑式留白。",
   "unresolved_questions": [
    "正文仅一句、25 字，未说明麻醉剂与兴奋剂在此处的具体所指，也未说明与酒神、天神神话的对应关系。",
    "“人类最廉价的终极方案”针对何种问题（痛苦、竞争、治理或其他）正文未说明。",
    "该判断的依据与时间尺度正文未说明，属待外部核查或需追加阅读的悬置判断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "因为麻醉剂必将替代兴奋剂成为人类最廉价的终极方案。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文明与人性", "神话隐喻", "社会趋势判断"],
   "issue_candidates": ["麻醉剂与兴奋剂", "人类廉价终极方案", "酒神与天神的替代关系"],
   "text_function_candidates": ["答疑", "短评", "预言式断语"],
   "object_candidates": ["狄俄尼索斯（提问者提出）", "宙斯（提问者提出）", "人类"],
   "working_keywords": ["麻醉剂", "兴奋剂", "最廉价的终极方案"]
  },
  "notes": "无图片节点，正文非空（仅一句），按 read 处理。本篇为超短答（25 字），正文未出现提问中的神名。"
 },
 "c4d83310": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待 WHO 新冠肺炎问答「不要吃传统草药」的建议被删除？”。作者没有评论 WHO 删帖一事本身，而是先声明自己不支持把中医理论当作直接医疗指导（P001），再对在该问题下对 traditional medicine 冷嘲热讽的答主们提出一串反问：美洲大蠊提取物算不算中药、在美国广泛使用的阿片类止痛剂是西药还是中药、动植物提取物是否有“医学原罪”、长期使用是否是额外扣分项、被命名为“肺炎一号方”是否就一定意味着是“传统药物”（P002-P008），最后批评这类反对者的心态（P009-P010）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "作者自我声明立场：不支持将中医理论作为直接医疗指导，可作为医疗思想的灵感来源，但不宜直接作为治疗方案的基础。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "提出反问对象与两个具体问题：对在该问题下嘲讽 traditional medicine 的各位发问——美洲大蠊提取物算不算中药？在美国广泛使用的阿片类止痛剂是西药还是中药？", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "要求对方思考的两个问题与追加一问：动植物提取药物是否有“医学原罪”而应绝对禁用；若无原罪，长期使用数百年上千年是否是额外扣分项；某种动植物提取物制剂经临床观察有效并被命名为“肺炎一号方”，是否一定是“传统药物”。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "结论式批评：很多人以为自己反对任何动植物、矿物提取物就是在反中药、反中医、反“愚昧落后”，是在展现科学素养、为“科学”张目；其实展现的是视科学如无物的部落心态。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明不支持将中医理论作为直接医疗指导，但认为可作为医疗思想的灵感来源，不宜直接作为治疗方案的基础。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者向在该问题下嘲讽 traditional medicine 的答主发问：美洲大蠊提取物算不算中药，在美国广泛使用的阿片类止痛剂是西药还是中药。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者要求对方思考：从动植物提取的药物是否有“医学原罪”而应划入绝对禁用；若无原罪，大规模使用过数百上千年是否是额外扣分项。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者追问：某种“动植物提取物制剂”通过临床观察有效并被取名为“肺炎一号方”，是否一定意味着这是“传统药物”。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为很多人以为自己反对任何动植物、矿物提取物就是在反中药、反中医、反“愚昧落后”，是在展现科学素养、为“科学”张目，其实展现的是视科学如无物的部落心态。", "evidence": ["E7", "E8"]}
   ],
   "argument_steps": [
    "先自我声明立场，与“支持中医理论作直接指导”的立场切割（P001）。",
    "把矛头指向该问题答案下嘲讽 traditional medicine 的答主（P002）。",
    "以“美洲大蠊提取物”“美国阿片类止痛剂”两个例子逼问分类标准（P003-P004）。",
    "要求对方在回答时思考两个问题：提取物是否有原罪、长期使用是否是扣分项（P005-P007）。",
    "追加第三问：名字与“传统药物”的归属是否等同（P008）。",
    "给出批评性结论：这类反对姿态是部落心态而非科学素养（P009-P010）。"
   ],
   "concept_usage": [
    {"term": "中医理论", "meaning": "作者区分于中药／提取物：它可作医疗思想的灵感来源，但不宜直接作为治疗方案的基础", "evidence": "P001", "ambiguity": "“直接医疗指导”与“灵感来源”的边界未展开"},
    {"term": "traditional medicine", "meaning": "问题与答主们讨论的对象；作者以此反问嘲讽者的分类标准", "evidence": "P002", "ambiguity": "作者未给出自己对该词的定义"},
    {"term": "医学原罪", "meaning": "作者假想的指控：从动植物提取药物本身即应绝对禁用", "evidence": "P006", "ambiguity": "作者以反问提出，未表明自己是否认为存在原罪"},
    {"term": "传统药物", "meaning": "作者质疑仅凭命名（“肺炎一号方”）是否就能归入此类", "evidence": "P008", "ambiguity": "作者未给出判定传统药物的标准"},
    {"term": "部落心态", "meaning": "作者对以“反中医”自我标榜者的贬称，指其立场先行而非依科学判断", "evidence": "P010", "ambiguity": "具体指向哪些答主，正文未点名"}
   ],
   "examples_and_targets": [
    "美洲大蠊提取物：作者用以逼问“算不算中药”的例子（P003）。",
    "在美国广泛使用的阿片类止痛剂：作者用以逼问“是西药还是中药”的例子（P004）。",
    "“肺炎一号方”：作者举出的命名与归类问题案例，未说明其具体来源与成分（P008）。",
    "对 traditional medicine 冷嘲热讽的答主们：作者的反驳对象，未点名（P002、P009）。",
    "WHO 新冠肺炎问答及“不要吃传统草药”建议被删除：提问者提供的语境，正文未评论该事件本身（Q001）。"
   ],
   "conditions": [
    "作者立场附有限定：中医理论可作灵感来源，但“不宜直接作为治疗方案的基础”（P001）。",
    "第二个问题以“如果直接提取自动物、植物和矿物中的药物并没有原罪”为条件（P007）。",
    "对“肺炎一号方”的追问以“通过临床观察有效”为描述前提（P008）。",
    "作者对“反中医者”的判断用“很多人以为”描述其自我认知，再给出自己的评价（P009-P010）。"
   ],
   "rhetoric_and_tone": "以“我先声明一点”作立场切割，随后连用反问句逼迫对方表态（算不算、是不是、是否一定意味着）；用词带有讥讽：“冷嘲热讽的各位”“视科学如无物的部落心态”；不直接论证中医有效性，而是攻击对方的分类与态度，属论辩式短评。",
   "unresolved_questions": [
    "提问涉及的 WHO 删除“不要吃传统草药”建议一事，正文未作任何评论或事实说明。",
    "作者未正面回答自己所提的三组反问，因此其对“提取物是否算中药／有无原罪”的实际立场只能从反问方向推断。",
    "“美洲大蠊提取物”“阿片类止痛剂”“肺炎一号方”的实际情况（如是否属传统药物、临床证据等级）需外部核查，作者未提供出处。",
    "被批评的“各位”是哪些答主、其原话为何，正文未引具体文本。",
    "lexical 结构统计为 11 个 paragraph 节点，而正文渲染出 10 段（P001-P010），正文与结构节点数不完全一致，是否有空段或末段缺失待核。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我先声明一点，我是不支持将中医理论作为直接医疗指导的。可以作为医疗思想的灵感来源，但是不宜直接作为治疗方案的基础。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "美洲大蠊提取物，算不算中药？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "在美国广泛使用的阿片类止痛剂，是西药还是中药？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "A）从动植物里提取的药物是不是有“医学原罪”？应该划入绝对禁用范围？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "B）如果直接提取自动物、植物和矿物中的药物并没有原罪，那么大规模使用过数百上千年，是不是一个额外的扣分项？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "某种“动植物提取物制剂”通过临床观察有效，被取了一个“肺炎一号方”的名字，是否一定意味着这是“传统药物”？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "很多人以为自己只要反对任何动植物、矿物提取物就是在反中药、反中医、反“愚昧落后”，是在展现科学素养，在为“科学”张目。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "其实展现的是视科学如无物的部落心态。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["医学与药学", "科学传播与科学素养", "公共争议"],
   "issue_candidates": ["WHO 传统草药建议被删", "中医理论与中药提取物", "动植物提取物的分类与原罪", "反中医姿态与部落心态"],
   "text_function_candidates": ["答疑", "论辩", "反问式批评"],
   "object_candidates": ["WHO（提问者提出）", "traditional medicine", "美洲大蠊提取物", "阿片类止痛剂", "肺炎一号方", "冷嘲热讽的答主们"],
   "working_keywords": ["中医理论", "traditional medicine", "医学原罪", "传统药物", "部落心态"]
  },
  "notes": "无图片节点，正文非空，按 read 处理。lexical 统计为 11 个 paragraph 节点而正文为 10 段，已记入 unresolved_questions。"
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
