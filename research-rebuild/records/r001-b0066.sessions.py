# -*- coding: utf-8 -*-
"""批次 r001-b0066 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0066.sessions.py            # 写 out/r001-b0066.out.jsonl
  python3 records/r001-b0066.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0066"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0066.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "11ad7ad3": {
  "analysis": {
   "question_context": "提问者问“为什么人们不喜欢被批评？”（Q001，属提问者）。作者先把问题改写为性质问题：人厌恶的多半不是批评，而是化妆成批评的迫害；随后应读者“写细一点”的要求，给出批评的标准操作、伦理原则与技术性要求，并逐条排除把批评用于平复情绪、防止连带损失、破坏自信、打击组织地位四类用途。文末以“（未完，待续）”标记未写完。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002"], "summary": "总命题：不是剂量问题而是性质问题；批评的红线是只能给逻辑、疑问、论证，不可讽刺、定罪或作构陷工具。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003","P004","P005","P006","P007"], "summary": "换轮胎未放好千斤顶一例的四种说法：批评、攻击侮辱、入人以罪、构陷。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P008","P009","P010","P011"], "summary": "驳“善意批评/恶意批评”二分：批评只能是善意的；侮辱、入罪、构陷是化妆成批评的恶行。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P012","P013","P014","P015","P016","P017"], "summary": "人不是不欢迎批评：批评是高度复杂敏感的技艺；多数人厌恶的是寄生在恶意本能中的迫害；真正的批评可遇不可求。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P018","P019","P020","P021","P022"], "summary": "应读者要求写细；批评法则是要害技艺（“白魔法”）；第一步是分析自己的批评冲动、列出诉求并检验其是否适合由批评承担。", "role": "transition"},
    {"unit_id": "U006", "paragraph_refs": ["P023","P024","P025","P026","P027","P028"], "summary": "借批评之名追求的典型诉求a—e：补偿情绪、最低代价止损、破坏自信、破坏组织地位、帮助对方成功。", "role": "context"},
    {"unit_id": "U007", "paragraph_refs": ["P029","P030","P031","P032","P033","P034","P035","P036"], "summary": "检验诉求是否适合用批评解决；批评早期可起效但会磨损批评权，批评权比黄金还贵。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P037","P038","P039","P040","P041","P042","P043"], "summary": "长期误用会取消批评权，关键之事上失去分量；正误批评的分界是磨损还是增厚批评权。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054","P055","P056"], "summary": "第一类排除：平复情绪。受伤是中性问题、成本应由自己承担；无共同前提则批评不适用，误用构成占领、统治与战争（来自爱人则是“珍珠港式的偷袭”）。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P057","P058","P059","P060","P061","P062","P063","P064","P065","P066","P067","P068"], "summary": "第二类排除：防止连带损失。应重申工作要求、结束合作、换环境或改进工作指南；真正的领导者是教育家。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P069","P070","P071","P072","P073","P074","P075","P076","P077","P078","P079","P080","P081","P082"], "summary": "第三类排除：破坏自信。利诱优于威逼，威逼不可持续且招致偶像包袱与反噬，得不偿失。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P083","P084","P085","P086","P087","P088","P089","P090","P091","P092","P093","P094","P095","P096"], "summary": "第四类排除：打击组织地位（张总打击李总，涉及老板、张、李与围观者四方）。老板不许批评起打击人的作用：品评个人者私下训诫、公开检讨、屡教不改走人；并以第一人称宣示此法则，违者位阶下移、与业绩造假同等危险。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P097","P098","P099","P100","P101","P102","P103","P104","P105","P106","P107","P108","P109","P110","P111","P112"], "summary": "理由与结论：只有如此才能持续改进、集中力量于业务；管理者的专业是定义和维持红线；无此原则的组织是冢中枯骨，中国企业多因无此意识而五年内灭亡。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P113","P114","P115","P116","P117","P118","P119","P120","P121","P122","P123","P124","P125","P126","P127","P128","P129"], "summary": "被批评者与旁观者的策略：静观老板处理，不哭诉威胁；老板不过关则辞职或发奋换环境；旁观者见势不对即准备跳船，撤退指不再做一般交易之外的额外输出。", "role": "action_advice"},
    {"unit_id": "U015", "paragraph_refs": ["P130","P131","P132"], "summary": "不能用“企业都这样”把人身攻击当正常：普遍不等于正常（血吸虫地区“大肚子是正常体态”之喻）。", "role": "rebuttal"},
    {"unit_id": "U016", "paragraph_refs": ["P133","P134","P135","P136","P137","P138","P139","P140","P141","P142","P143","P144","P145","P146","P147","P148","P149","P150"], "summary": "第二步：先取得被批评者的授权。授权常是隐性的且须有授权能力；批评是甘冒奇险的礼物，多数人不配得；值得重视的只有求来的与公共批评两种（自选的教练老师咨询师领导与父母属预先授权）。", "role": "transition"},
    {"unit_id": "U017", "paragraph_refs": ["P151","P152","P153","P154","P155","P156","P157","P158","P159","P160","P161","P162","P163","P164","P165","P166","P167","P168"], "summary": "批评原理：基于授权，采取对方立场，用对方承认的法则与证据，推出其逻辑不连贯处并说明对其自身目的的危害；批评者唯一拥有的是逻辑运算能力。", "role": "claim"},
    {"unit_id": "U018", "paragraph_refs": ["P169","P170","P171","P172","P173","P174","P175","P176","P177","P178","P179","P180","P181","P182","P183","P184"], "summary": "批评力何来：遵循法则即尊重（法则即尊重的实践法则）；对抗你的是你自己立场与法则的矛盾；故批评法则是客观的自然法。", "role": "reason"},
    {"unit_id": "U019", "paragraph_refs": ["P185","P186","P187","P188"], "summary": "让步：遵守法则不见得结果理想；正确的批评只是及格线，其上还有技术与艺术问题。", "role": "qualification"},
    {"unit_id": "U020", "paragraph_refs": ["P189","P190","P191","P192","P193","P194","P195","P196","P197","P198","P199","P200","P201","P202","P203","P204","P205","P206","P207","P208","P209","P210"], "summary": "三项技术要求：尽量用中性词、不褒贬具体人；回避利害关系并分担成本、分享收益；把附带伤害降到力所能及的最低，唯一可接受的回答是已竭尽所能并致歉。", "role": "action_advice"},
    {"unit_id": "U021", "paragraph_refs": ["P211","P212","P213","P214","P215","P216","P217","P218","P219","P220","P221","P222","P223","P224"], "summary": "作者断言真正做到这些原则批评就一定有效、一定得感激；无效只允许三种自省解释，绝不归咎对方；由此才有真正的尊重与人们授予的影响力。", "role": "claim"},
    {"unit_id": "U022", "paragraph_refs": ["P225","P226","P227","P228","P229","P230","P231","P232","P233"], "summary": "收尾反问：为何一定要选“加强版批评”，而不用物质补偿、诉讼、改变计划或接受损失；文末标“（未完，待续）”。", "role": "conclusion"},
    {"unit_id": "U023", "paragraph_refs": ["P137","P138"], "summary": "正文夹入平台相关问句“该如何对待习惯性论断（judge）他人的人？”，未被lexical结构覆盖。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们不喜欢被批评不是剂量问题而是性质问题；批评的红线是只能给逻辑、疑问、论证，不可讽刺、定罪或作构陷工具。", "evidence": ["E1","E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“善意批评/恶意批评”的分法是错的：批评必须也只能是善意的；侮辱、入罪、构陷是化妆成批评的恶行。", "evidence": ["E3","E4","E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人不是不欢迎批评：批评是高度复杂敏感的技艺，多数人厌恶的是被本能看破的迫害，真正的批评可遇不可求。", "evidence": ["E6","E7","E8","E70"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评的第一步是审查自己的批评冲动：列出想达成的净改变，检验其是否为批评可达到、可合法追求的结果（文中列举a—e五种典型诉求）。", "evidence": ["E9","E10"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“批评权”会因误用而磨损乃至取消：把批评用在不该它承担的任务上，重大之事上就会失去批评权。", "evidence": ["E11","E12","E47"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "正误批评的分界是这一行为磨损还是增厚批评权：错误的批评越批越要加大音量，正确的批评越用越被需要。", "evidence": ["E13"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "情绪受伤不应以批评表达：受伤是中性事务而非罪行，其解决成本理应由自己承担。", "evidence": ["E14","E15","E16"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "感情受伤无共同前提故批评不适用；单方以自己认可的法则判定对方有错并施以攻击，是占领、统治与战争行为。", "evidence": ["E17","E18","E74"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用批评防止连带损失是错误用法：应重申工作要求、结束合作或换环境，而不要用“批评”解决问题。", "evidence": ["E19"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不能用批评破坏对方自信：利诱优于威逼，威逼不可持续且招致偶像包袱与反噬；真正的领导者是教育家。", "evidence": ["E20","E21","E22"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老板不许批评起打击人的作用：品评个人者私下训诫、公开检讨、屡教不改走人；作者并以第一人称宣示此法则是继承人与代理人的红线，违者位阶下移、危险与业绩造假相当。", "evidence": ["E23","E24","E48","E25"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有这条原则的组织都是冢中枯骨：失去对批评红线的掌握，企业就开始坏死。", "evidence": ["E26"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被批评者应静观老板处理而不提条件、不哭诉威胁；老板不过关就有能力立刻辞职、没能力发奋换一家。", "evidence": ["E27","E28"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "普遍不等于正常：不能用“企业都这样”把批评中的人身攻击当成正常现象。", "evidence": ["E29","E65"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评的第一条规范原则是必须先获得被批评者的授权；授权常是隐性的，还须衡量对方的授权能力。", "evidence": ["E30","E31","E49","E66"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "值得重视的批评只有三顾茅庐求来的与公共批评两种；未经邀请主动上门的批评含金量不足。", "evidence": ["E32"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评原理：基于授权，采取对方立场，用对方承认的法则与证据，推出其逻辑不连贯处；批评者唯一拥有的是逻辑运算能力。", "evidence": ["E33","E34","E35"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评的法则是客观存在的自然法，不因当事双方一致否认而无效。", "evidence": ["E36"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "真正做到这些原则批评就一定有效、一定得感激；不相信法则会成为自我实现的预言，而正确的批评只是及格线。", "evidence": ["E37","E38","E55"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评中应回避利害关系：若对方改正使你获利更大须慎重，做了就要分担成本、分享收益。", "evidence": ["E39","E40"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "批评者有义务把附带伤害降到力所能及的最低，因为对方开放批评权是基于信任的托付；唯一可接受的回答是已竭尽所能并致歉。", "evidence": ["E41","E42","E62"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "影响力来自人们感知到批评者的信念与尊重而授予的特权，起作用的与其说是智慧能力，不如说是人自己给的授权。", "evidence": ["E43","E57","E59"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者反问：为何一定要选“加强版批评”，而不用物质补偿、诉讼、改变计划或接受损失。", "evidence": ["E44","E45"]},
    {"claim_id": "C024", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "文章以“（未完，待续）”结束，替代方案与最终结论均未写出。", "evidence": ["E46"]}
   ],
   "argument_steps": [
    "把提问从剂量问题改写为性质问题，先划批评的红线。",
    "用换轮胎例区分批评、攻击侮辱、入人以罪、构陷。",
    "反驳“善意/恶意批评”二分，指出多数人抗拒的是化妆成批评的迫害。",
    "转入操作规范：先审查自己的批评冲动与诉求，提出“批评权”。",
    "以批评权的磨损或增厚区分正误批评。",
    "逐条排除四类不该由批评承担的任务：平复情绪、防止连带损失、破坏自信、打击组织地位。",
    "第一类：受伤是中性问题、无共同前提，误用即占领、统治与战争。",
    "第二类：代之以重申要求、结束合作、换环境、改进工作指南。",
    "第三类：利诱优于威逼，威逼招致偶像包袱与反噬。",
    "第四类：给出老板、当事人、旁观者三方的行动规则，并把伦理红线与永续生存相连。",
    "以“普遍不等于正常”回应“企业都这样”。",
    "第二步：取得授权，讨论隐性授权、授权能力与两类值得重视的批评。",
    "给出批评原理（对方立场、法则、证据，只提供逻辑运算），并归结为客观自然法。",
    "让步：正确批评只是及格线；提出中性用词、回避利害、最小附带伤害三项技术要求。",
    "以“必须相信法则有效”与无效时的三种自省收束，末以四个反问和未完标记结束。"
   ],
   "concept_usage": [
    {"term": "批评（criticize）", "meaning": "基于对方授权、采取对方立场、只用对方承认的法则与证据、仅补足逻辑运算的意见行为。", "evidence": "P004", "ambiguity": "与日常泛指“指出缺点”不同。"},
    {"term": "红线", "meaning": "批评不可讽刺、不可定罪、不可构陷，且不可品评个人。", "evidence": "P002", "ambiguity": "正文未给穷尽清单。"},
    {"term": "批评权", "meaning": "他人愿意听取其批评的信用额度，会磨损、被取消，也能因正确使用而增厚。", "evidence": "P032", "ambiguity": "作者自造比喻，无量化定义。"},
    {"term": "善意", "meaning": "批评的构成性必要条件，而非动机分类标签。", "evidence": "P009", "ambiguity": "与日常“善意/恶意批评”二分相反。"},
    {"term": "迫害", "meaning": "侮辱、入罪、构陷等寄生在恶意本能中而以批评为名的行为。", "evidence": "P011", "ambiguity": "无。"},
    {"term": "授权", "meaning": "被批评者对批评的允许，常为隐性且授权者自己意识不到，还须对方有授权能力。", "evidence": "P136", "ambiguity": "隐性授权如何判定，正文无操作标准。"},
    {"term": "对方承认的逻辑法则", "meaning": "批评可用的唯一法则来源；单方或“大多数”认定的法则不能自动作为对方必须承认的真理。", "evidence": "P160", "ambiguity": "对方承认的法则自相矛盾时未讨论。"},
    {"term": "自然法", "meaning": "作者称批评法则客观存在、由人类本质特性决定，不因双方一致否认而失效。", "evidence": "P184", "ambiguity": "属作者理论断言，待外部核查。"},
    {"term": "加强版批评", "meaning": "把批评升级为攻击、胁迫或言语、经济、肉体强制。", "evidence": "P226", "ambiguity": "无。"},
    {"term": "尊重", "meaning": "作者称批评的法则即尊重的具体实践法则，真正的尊重带来他人授予的影响力。", "evidence": "P171", "ambiguity": "属规定性主张。"},
    {"term": "利诱／威逼", "meaning": "影响他人的两种手段；能利诱则利诱更有效，威逼不可持续。", "evidence": "P071", "ambiguity": "两者都不可用时未讨论。"}
   ],
   "examples_and_targets": [
    "换轮胎未放好千斤顶的四种说法（作者自设例证，区分批评、攻击侮辱、入人以罪、构陷）P003-P007。",
    "教孩子开车：影响力全浪费在开空调，没教会踩刹车、打方向盘（类比）P039。",
    "“拿筷子”“弯腰驼背”“坐有坐相”“笑不露齿”耗尽批评权（举例）P040。",
    "情绪受伤时坦白表达、商量最低成本方案的对话脚本（示范）P046。",
    "雇员、有主管人事权的环境、改进工作指南与“认命”（举例）P058-P064。",
    "击溃自信导致个人崇拜与偶像包袱（论后果）P078-P080。",
    "张总用批评打击李总，涉及老板、张、李与围观群众（设例）P084-P085。",
    "老板的训诫、公开自我检讨与“与业绩造假不相上下”的警告（示范规则）P088-P096。",
    "旁观者撤退的超市卖汽水类比：仍一手钱一手货，但不再打折赊账（类比）P126。",
    "靠借贷撑面子、借遍身边人后突然消失或破产的老板群体（经验性描述）P127。",
    "血吸虫泛滥地区“大肚子是正常体态”（类比，反驳“企业都这样”）P131。",
    "看病者嫌医生说有病、求教者怪教练、提问者怪答案（举例说明隐性授权）P140。",
    "未成年人无权签订劳动合同（类比授权能力）P144。",
    "科学论文、文艺批评、社论、技术文档、学术著作作为公共批评（举例）P149。",
    "医生不能借牙疼求诊批评病人的公司经营或哲学立场、对方想赚钱结婚而你想做大上市、演化论与“上帝七天创世”、“你误导了我”对“你误读了我”（设例）P158/P159/P161/P165。",
    "“中国的企业领袖大部分……五年以内灭亡”“人类被硬-wired成只听遵循尊重法则的意见”（经验／理论断言，待外部核查）P110/P172。"
   ],
   "conditions": [
    "批评须获授权；隐性授权亦须确认对方有授权能力，否则连请求授权也不要做。P136/P144/P145",
    "批评只能用对方承认的法则与事实；对方不承认的须先从对方现有认知推导出来。P155/P160/P161",
    "不得超出授权范围（医生—牙疼病人），也不得脱离对方立场（赚钱结婚vs做大上市），除非对方明确承诺了爱。P158/P159",
    "情绪受伤的表达只在自认应该表达时坦白提出，成本由自己承担、对方出于爱才分担。P046/P049/P050",
    "防止连带损失应先重申工作要求，成本过大则结束合作，无法换人换环境则权衡后认命。P058/P059/P063",
    "利诱优于威逼以“有利可图”为前提。P071",
    "老板的红线要求随职位升高而更严酷，并须对下维护、教导接班人。P095/P099",
    "被批评者静观其变以自身职业能力与人望不差为前提。P123",
    "批评方向与自身利益不一致时最有说服力；动手则须分担成本、分享收益；对方改正意味着立即利益损失时更要慎重。P195/P196/P197/P199",
    "须把附带伤害降到力所能及最低，只有尽力后仍不可避免的风险才可请求宽容。P203/P207",
    "相信法则有效是前提；批评看似无效只允许三种自省解释。P213/P215-P220",
    "值得重视的批评只有求来的与公共批评；自选的教练、老师、咨询师、领导与父母属预先授权。P149/P150",
    "文末标“（未完，待续）”，P214含“（此处语句残缺）”，属未完成稿。P214/P233"
   ],
   "rhetoric_and_tone": "论说与训诫混合体：以“不是A，是B”的对举短句开篇下定义，善用自设对话、连串反问（“何谈厌恶？”“那还搞什么搞？”）与格言式断言；中段转入老板第一人称的训诫与威胁式宣示（“我是老板”“不要有任何侥幸”“想好了你再吐”），口气笃定并直接对读者下判断（“极其愚蠢”“虚掷青春”）；大量比喻类比（白魔法、珍珠港式的偷袭、梧桐树与凤凰、做大即死亡、冢中枯骨、血吸虫地区的大肚子、编译错误）；对提问者不点名、不引用其立场；全文用拼音“ta”作性别中立代词；文末以四个反问与“（未完，待续）”收束。",
   "unresolved_questions": [
    "文章以“（未完，待续）”结束，“加强版批评”的替代方案与最终结论未写出。",
    "P214正文含“（此处语句残缺）”，该句在语料中本身残缺，原意不明。",
    "P137疑为平台插入的相关问句，与上下文不衔接且未被lexical覆盖（divergence char_start=7042），需核对原页面。",
    "老板口吻段落（P090-P096等）的“我”是作者本人还是作者代老板设想的示范口吻，正文未区分；本记录按示范处理。",
    "“批评权”“白魔法”“自然法”等为自造或借用术语，正文未给可外部核验的定义与边界。",
    "关于中国企业五年内灭亡、人类被硬-wired成只听遵循尊重法则的意见等断言需外部核查，本记录不作裁决。",
    "updated_at（2025-10-11）晚于published_at（2020-08-26），是否含后续编辑或版本差异，语料未说明。",
    "提问Q001问的是“为什么人们不喜欢被批评”的心理机制，作者未直接回答而是改写问题；提问者立场未被作者引用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这不是剂量问题，这是性质问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "批评只能给逻辑、给疑问、给论证", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P008", "quote": "这个说法本身其实是错的", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "批评（criticize）必须也只能是善意的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "侮辱、入罪、构陷，都是利用了", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P013", "quote": "批评是一门高度复杂和敏感", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P014", "quote": "而是被人的本能看破的乔装打扮", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "求之且不得，何谈厌恶？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P021", "quote": "你想要这个批评造成哪些净改变？", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P028", "quote": "帮助对方认识到自身的问题", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P032", "quote": "你的批评权就会磨损", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P037", "quote": "那么你的批评权就会被取消", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P041", "quote": "这一项批评的行为是会磨损还是会增厚你的批评权", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P046", "quote": "你的情绪受伤，就不应该用批评来表达。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P047", "quote": "不是一种罪行、一种失败", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P049", "quote": "而且这个成本理所应当由你自己承担", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P054", "quote": "批评必须基于共同接受的逻辑前提", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P055", "quote": "这不是批评，而是一种占领和统治", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P058", "quote": "重新清晰表达工作方法和输出物的质量要求", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P066", "quote": "真正的领导者都是教育家", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P071", "quote": "能“利诱”，绝对是“利诱”更有效", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P076", "quote": "但是造成这效果对你的收益是得不偿失的", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P088", "quote": "谁就私下被训诫，公开做自我检讨", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P089", "quote": "品评人的性格、风格、价值，哪怕玩笑也不许开", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P092", "quote": "其危险程度与业绩造假不相上下", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P111", "quote": "什么时候企业就开始坏死", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P114", "quote": "也可能是因为你的哭诉和威胁的结果", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P117", "quote": "有能力就立刻提出辞职申请", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P132", "quote": "那只是普遍，普遍不等于正常。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P136", "quote": "批评必须先获得被批评者的授权", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P145", "quote": "请求授予批评权的动作也不要做", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P149", "quote": "主动找上门来的批评，往往含金量不足", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P155", "quote": "从对方承认的证据和事实出发", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P157", "quote": "你不能将其中任何一条变成你的。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P167", "quote": "仅仅只有逻辑运算能力", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P184", "quote": "本质上上述“批评的法则”是一种自然法", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P212", "quote": "你的批评就一定会有效", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P213", "quote": "你的不相信本身就会成为自我实现的预言", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P196", "quote": "是否应该开口去请求这个批评权", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P199", "quote": "要分担对方的成本、分享你将来因此获得的收益", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P203", "quote": "将这种附带损失降到你能做到的最低", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P206", "quote": "这已是我能力所能及的伤害最小的方式", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P224", "quote": "不如说是人自己给你的授权", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P226", "quote": "不惜将批评变成“加强版批评”", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P229", "quote": "你为什么不直接用物质补偿交换", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P233", "quote": "（未完，待续）", "relation": "context"},
    {"key": "E47", "paragraph_id": "P031", "quote": "批评是可以在早期起到这些效果的", "relation": "qualifies"},
    {"key": "E48", "paragraph_id": "P090", "quote": "首要的任务就是保证组织伦理的健康", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P143", "quote": "批评是一件甘冒奇险的礼物", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P186", "quote": "正确的批评只是一根及格线", "relation": "qualifies"},
    {"key": "E57", "paragraph_id": "P208", "quote": "正因为甘于接受这种不公平，你才有资格获得真实的权柄", "relation": "supports"},
    {"key": "E59", "paragraph_id": "P221", "quote": "从不将批评无效的责任归咎于对方", "relation": "supports"},
    {"key": "E62", "paragraph_id": "P202", "quote": "会客观上损害对方的影响力", "relation": "supports"},
    {"key": "E65", "paragraph_id": "P131", "quote": "说“大肚子是正常体态”", "relation": "supports"},
    {"key": "E66", "paragraph_id": "P139", "quote": "这种授权常常是隐性的", "relation": "supports"},
    {"key": "E70", "paragraph_id": "P015", "quote": "可以用批评造就常人难以想象的杰出人物", "relation": "supports"},
    {"key": "E74", "paragraph_id": "P055", "quote": "更是一种珍珠港式的偷袭了", "relation": "supports"},
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际沟通与说服", "组织管理与企业伦理", "伦理学／行为规范", "语言行为与修辞", "教育与教养"],
   "issue_candidates": ["批评的边界与红线", "人身攻击、入人以罪与构陷", "批评的授权与同意", "情绪表达与成本分担", "职场政治与组织内斗", "领导者伦理与企业传承", "操纵与委婉批评之别", "批评的技术与艺术"],
   "text_function_candidates": ["答疑", "论辩", "规范／操作指南", "训诫", "经验总结"],
   "object_candidates": ["提问者（知乎）", "老板／管理者", "雇员与下属", "被批评者", "旁观者／围观群众", "张总、李总（示例人物）", "中国企业", "父母与子女", "医生与病人"],
   "working_keywords": ["批评（criticize）", "红线", "批评权", "授权", "善意", "迫害", "构陷（defame）", "入人以罪（criminalize）", "攻击（assault）", "公共批评", "自然法", "加强版批评", "尊重", "白魔法", "ta"]
  },
  "notes": "本篇无图片节点（图片字段不适用，image_checked=false 无影响），status=read。正文233段中：P137为知乎相关问句插入，未被lexical结构覆盖（divergence=1，text_has_content_not_in_lexical，char_start=7042），本记录按正文原样保留并标为other；P214正文含“（此处语句残缺）”、P233为“（未完，待续）”，均为语料原有标记。老板口吻段落（P090-P096等）以第一人称“我”写成，本记录按作者示范／训诫口吻处理，不据此断定作者本人身份。作者关于企业寿命、人类演化等断言为文中事实性主张，仅登记为待外部核查，未作裁决。"
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
