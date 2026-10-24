# -*- coding: utf-8 -*-
"""批次 r001-b0114 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0114.sessions.py            # 写 out/r001-b0114.out.jsonl
  python3 records/r001-b0114.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0114"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0114.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "05a4a9b4": {
  "analysis": {
   "question_context": "提问者（Q001）问作者自己是怎么复盘的、有哪些高效方法推荐。作者没有讲个人经验，而是给出一套组织级复盘的操作规程，按 Step 1 提出问题（Name the Issue）、Step 2 案情重建（Case Building）、Step 3 方案探讨（Solution Forging）依次展开，文末标“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P027"], "summary": "Step 1 提出问题：给 issue 编号并写临时单句描述（问题主体＋疑似条件＋现象，主体不得为个人）；采集标本材料形成标准样本；反复迭代，以“令人满意”（命名时间资源耗尽处）为边界，不追求彻底、全面、绝对正确。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P028", "P042"], "summary": "Step 2 案情重建：按时间线罗列全部事实、采集相关人证词并完整描述要素，类比刑事侦查；先不急于判断凶手与真相，排除不可能并追查叙事分歧机制；问题描述与样本随之反复修正；批评凭情绪与心理焦虑定义问题。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P043", "P057"], "summary": "Step 3 方案探讨起手：先给问题估价，估出总价作为可投入资源上限；识别整理问题的成本已从此上限支出且要留利润，故并非所有问题都值得解决；可用泛化问题的办法把支出科目转入战略研究基金。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P058", "P072"], "summary": "任务小组三种组建方案（a 仅必要专家与决策层闭门、b 彻底解决导向全专家闭门、c 根绝问题导向公开讨论）及成本与组织影响比较；各方案可加见习后备人员作梯队培养；非紧急问题异步留言讨论，紧急问题线上线下会议。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P073", "P095"], "summary": "界定“解决方案”指且仅指组织规则的更新（章程、奖惩条例、工艺规范、标准、计划等文件的修改/增补）；进而断言组织本质是规则而非行为、人员、财产、地点，以空账户作类比；经验教训只有形成文本才对组织存在。", "role": "definition"},
    {"unit_id": "U006", "paragraph_refs": ["P096", "P100"], "summary": "复盘讨论不涉及个人奖惩判决，奖惩由另一专责小组在复盘后按当事人坦诚程度自由裁量；积极参与并形成规则沉淀可获酌情减免。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P101", "P113"], "summary": "讨论方案的九步规范流程：提案与讲解答疑、评论者点评、提案人修正、二次提案（可循环）、超额投票采集倾向、提交决策机构、挑选候选方案、追加预算完善、最终决定。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P114", "P137"], "summary": "讨论关键原则：禁止未经主持人批准发言（擅自对话视为窃取公司资产）、禁止针对人的褒贬词汇、不设双人自由对话或“自由发言”议程、除章程规定外禁止用投票表决作决策；主持人的特权、失职赔偿与专业训练要求；文末标“（未完，待续）”。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "复盘第一步须给问题一个不表意的编号与临时单句描述，描述包含问题主体、疑似条件与现象，且问题主体不允许是具体个人。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题识别的完整性以“令人满意”为边界条件，其标准是分配给问题命名的时间资源耗尽时达到的水平，而非追求彻底、全面、绝对正确。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "案情重建应先有序罗列全部事实，不急于判断凶手与案情真相，以免对某种假说的过度投入使证据搜索只为证实该假说。", "evidence": ["E5", "E30"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题描述、样本与案情重建三者需反复修正并互相协调；这种反复正是问题被正确提出的复杂性所在，也是多数人在提出问题阶段失败的主要原因。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是所有问题都需要或值得解决，有些可以直接接受；也可通过泛化问题定性，把支出科目从项目备用金转移到战略研究基金。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "解决方案指且仅指组织规则的更新，即“哪一份文件的哪一部分需要修改或增补成什么样子”的答案。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "组织的本质是组织的规则，而不是组织的行为、人员组合、财产和地点；增强组织即推动规则自洽化、与目的一致化、与环境兼容化、与挑战适应化。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "站在组织角度，经验与教训只有在形成文本的意义上才存在；开了会而未形成任何文本，在最终意义上没有意义。", "evidence": ["E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "关于复盘的讨论不涉及个人奖惩判决，奖惩由另一专责小组在复盘完毕后按当事人在复盘中的坦诚程度自由裁量。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "会议中不经主持人批准而直接互相对话应被视为窃取公司资产，须严厉警告并视情况作出财务赔偿，因为所占用的时间由公司全额成本购置。", "evidence": ["E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "除组织章程规定需要投票表决的事务之外，严格禁止用投票表决作为决策机制；决策是后果承担者的特权，只能由后果承担者或其授权受托人作出。", "evidence": ["E20", "E21"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "讨论中禁止使用针对人的褒贬词汇，贬低与褒扬都要制止，只应对方案本身发表意见；被警告者应立即无条件向全体讨论者道歉。", "evidence": ["E37", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原则上不作任何允许两人自由对话的议程安排，也不允许所谓“自由发言”议程存在，因为这类议程会系统性增加讨论失败的风险。", "evidence": ["E23"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "在三种任务小组方案中，仅纳入绝对必要专家与决策层的闭门讨论效率最高、最被推荐；彻底解决导向的方案成本往往大 8-10 倍。", "evidence": ["E25", "E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "主持人的首要职责是保护会议时间效率，其应在维护讨论伦理基础上高效节省地使用会议资源，并应受过专业会议训练。", "evidence": ["E38", "E39"]}
   ],
   "argument_steps": [
    "定义问题命名程序：编号＋临时 issue 句式描述（主体不得为个人），并说明“临时”是因为过程未完成前难以正确认识问题实质（P001-P013）。",
    "提出样本/标本材料要求，称原始标本才是 issue 的实体、描述只是名字，资料与描述须存档留痕（P016-P023）。",
    "给出迭代终止条件：以“令人满意”为边界，解释其为时间资源耗尽处的实践标准，反对追求绝对正确（P024-P027）。",
    "转入案情重建：按相关关系建时间线、采集证词与要素，类比刑事侦查，强调先罗列事实而非预设凶手（P028-P035）。",
    "处理叙事分歧：先用物理定律类绝对限制排除不可能，再追查分歧机制，并据案情回改问题描述与样本（P036-P039）。",
    "反驳常见做法：一般人凭情绪与焦虑，在样本残缺、案情不全时定义问题，会造成极端不公的结论（P040-P042）。",
    "提出估价与预算上限：按概率、损失、时间场合估总价，识别成本已从上限定支出且需留利润，故问题可不解决或被泛化以改变支出科目（P045-P057）。",
    "给出任务小组 a/b/c 三方案及成本与组织影响比较，允许加入见习人员作梯队考察，按紧急程度选择会议形式（P058-P072）。",
    "定义解决方案＝组织规则的更新，列举典型规则文件，并把组织本质论证为规则、把规则背后的原则目的称为灵魂（P073-P085）。",
    "推出组织强化＝规则四化建设，进而断言经验教训只有形成文本才存在、未形成文本的会议无意义（P086-P095）。",
    "限定范围：复盘不涉及个人奖惩判决，奖惩归另一专责小组，且按复盘中的坦诚程度裁量（P096-P100）。",
    "给出讨论方案九步流程与超额投票办法，交决策机构逐级筛选与追加预算（P101-P113）。",
    "列出四条关键讨论原则（发言须批准、禁止人身褒贬、不设自由对话议程、禁止以投票作决策），并说明主持人职责、特权与培训要求（P114-P136）。",
    "以“（未完，待续）”结束本段文本（P137）。"
   ],
   "concept_usage": [
    {"term": "issue／问题", "meaning": "带唯一编号、可反复修正的描述；作者称原始标本才是 issue 的实体，描述只是它的名字。", "evidence": "P022", "ambiguity": "文中 issue 与“问题”混用，未给统一界定。"},
    {"term": "复盘", "meaning": "被限定为以修订组织规则文档为中心和唯一形式的组织改进过程，而非个人总结经验。", "evidence": "P093", "ambiguity": "提问者问的是个人复盘方法，作者答的是组织规程，二者范围不同。"},
    {"term": "令人满意", "meaning": "识别完整性的边界条件，实践上指分配给 issue naming 的时间资源耗尽时达到的水平。", "evidence": "P027", "ambiguity": "标准由时间资源而非质量标准定义，文中未说明资源如何核定。"},
    {"term": "案情重建（Case Building）", "meaning": "按与 issue 的相关关系建立从发端到发作的时间线并罗列全部事实，作者类比刑事侦查。", "evidence": "P029", "ambiguity": "类比未说明企业场景中取证权限与刑事侦查的差别。"},
    {"term": "解决方案", "meaning": "指且仅指组织规则的更新，即某份文件某部分如何修改或增补。", "evidence": "P074", "ambiguity": "把方案等同于文本修改，排除了非文本类行动。"},
    {"term": "组织", "meaning": "本质是组织的规则；规则条文背后的总原则、目的和纲领是其灵魂。", "evidence": "P082", "ambiguity": "以空账户类比规则实体的论证方式，文中未回应无成员组织如何运作。"},
    {"term": "超额投票", "meaning": "参与者每人有两票以上，可投自己但不可投同一人、不可弃权，仅作决策参考。", "evidence": "P108", "ambiguity": "票数与计票规则未具体化。"},
    {"term": "主持人", "meaning": "受托分配会议时间资源者，享有不经申请发言、打断、延长、重述议题等特权，失职须担责。", "evidence": "P134", "ambiguity": "主持人报酬与会议成本挂钩只是括注中的建议。"}
   ],
   "examples_and_targets": [
    "鸡蛋羹气泡、颜色偏白、组织强度不足等作为 issue 描述句式的示例（作者举例，P007）。",
    "“服务器在无人值守期间频繁自动重启”作为非食品类 issue 示例（作者举例，P007）。",
    "“张三在总账清结时频繁出现计算错误（错）”与“项目财务助理……（对）”作为主体不得为个人的对照示例（作者举例，P011、P012）。",
    "“xxx质量不佳／感觉不对／表现不好”作为应避免的无意义描述（作者举例，P015）。",
    "客户对某交付物延迟不满、调取该交付物生产全过程记录与相关人员证词，作为案情重建示例（作者举例，P030-P033）。",
    "刑事侦查中的案情重建作为类比（作者类比，P034）。",
    "“鸡蛋羹的组织强度不稳定”与泛化后的“食物口感控制的系统方法在热成型布丁类应用中不可靠”，用以说明问题泛化可改变预算科目（作者举例，P053、P054）。",
    "项目备用金（十几二十万、价值在项目收入中表现）与战略研究基金（千万、亿级别、价值在股价中表现）作为预算科目对比（作者主张中的数字性说法，P054）。",
    "企业章程、奖惩条例、工艺流程、培训手册、招聘标准、组织架构等作为“解决方案”所指的规则文件清单（作者列举，P076）。",
    "银行数据库里创建的空账户（持有人、交易记录、余额、名称、序列号皆空）作为组织本质是规则的类比（作者类比，P084、P085）。",
    "“铁打的营盘流水的兵”作为组织与成员关系的比喻（作者修辞，P090）。",
    "任务小组方案 a/b/c 的成本比较（b 比 a 大 8-10 倍；c 与 b 同数量级）（作者主张，P062、P065）。",
    "Q&A 环节甲提问、乙回应、甲追加提问须向主持人请求的操作示例（作者举例，P117）。"
   ],
   "conditions": [
    "带“[]”的描述成分可以从缺（P005）。",
    "以“令人满意”为边界的前提是承认人不可能达到彻底、全面、绝对正确；勉强追求会降低效率、使进度不可见（P025、P026）。",
    "条件性表述：如果是仅在某非经常性项目中出现的生命周期问题，则按概率、损失、时间与场合区域估总价（P046）。",
    "成本约束：识别与整理问题的支出已占用预算上限，只能用余额解决且需留合理利润；余额可能不够召集会议（P048、P049）。",
    "泛化问题以转移支出科目的做法，取决于能否把它表述为更普适的问题（P052、P054）。",
    "方案 b 适用于会导致经营战略被修正的重大问题；方案 c 适用于涉及企业伦理、文化、基本规章制度修正的问题（P063、P067）。",
    "非紧急问题可异步留言讨论以节约成本；紧急问题适合线上线下会议（P071、P072）。",
    "复盘参与者若积极参与并形成规则沉淀，责任可酌情减免；除非错误纯属不遵守明文规章、无规则改进的教育意义（P099、P100）。",
    "禁止以投票表决作决策的例外是组织章程规定需投票表决的事务；讨论小组获授权直接决策属需明确授权的特殊情况（P130、P132）。",
    "主持人的特权以其负有管理会议成本的特殊责任为前提，一般宜在制度上将会议成本与主持人报酬挂钩（P133、P134）。"
   ],
   "rhetoric_and_tone": "训诫式操作规程，第二人称“你”直接指教，频繁使用“必须”“严格禁止”“绝对的必要”等强规范用语；夹用反问与设问（“看明白了吗？”），也有“逻辑地狱”“其实就是在冤枉人”“浪费苦难本身”等重话；使用“铁打的营盘流水的兵”、空账户等比喻；结构为三级 Step 标题加编号条目，末尾标明未完待续。",
   "unresolved_questions": [
    "文末标“（未完，待续）”，Step 3 之后的内容（是否还有后续 Step 或落地部分）在本篇缺失，本文不是完整文本。",
    "P098“它的工作只是按照修正前与复盘小组的主要关系”一句语义不通，疑为原文脱漏或截断，确切含义待核。",
    "提问者问个人复盘方法与“高效方法推荐”，作者答组织级规程，未直接回应个人层面问题，是答非所问还是刻意区分层次，本文未说明。",
    "P054 中项目备用金“十几二十万”、战略研究基金“千万、亿级别”等数字与财务科目设定，依赖特定组织背景，本文未给出来源或适用规模。",
    "作者以企业为默认场景（“公司资产”“企业章程”），但未说明该规程是否适用于非营利组织、家庭或个人场景。",
    "“令人满意”以时间资源耗尽为准，但本文未说明时间资源如何分配与核定，也未给出可检验的判据。",
    "本篇无图片节点，不涉及图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P009", "quote": "其中，问题主体不允许为具体个人。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P013", "quote": "才有一个绝对的必要给issue一个不表意的编号", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P025", "quote": "以“令人满意”为边界条件", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P027", "quote": "是指分配给issue naming的时间资源耗尽时你所达到的水平", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P035", "quote": "以免对某种假说的过度倾向（over investment）造成证据搜索只为证实该假说而进行", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P039", "quote": "也是导致绝大多数人在提出问题阶段失败的主要原因", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P038", "quote": "使得三者互相协调一致", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P051", "quote": "不是所有问题都需要或者值得解决，有一些问题你可以直接接受。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P054", "quote": "把支出科目从“项目备用金”科目转移到“战略研究基金”科目下", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P074", "quote": "所谓的解决方案，指且仅指组织规则的更新。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P077", "quote": "我们的哪一份文件的哪一部分需要修改/增补成什么样子", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P079", "quote": "组织的本质，不是组织的行为，不是组织的人员组合，也不是组织的财产和地点", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P080", "quote": "组织的本质，是组织的规则。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P086", "quote": "增强一个组织，就是推动它的规则自洽化", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P091", "quote": "经验和教训只有在形成一些文本的意义上才是存在的", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P096", "quote": "关于复盘的讨论，不涉及个人的奖惩判决。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P099", "quote": "如果当事人积极参与复盘，并形成了良好的规则沉淀，那么ta的责任会被酌情减免。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P120", "quote": "被视为窃取公司资产", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P121", "quote": "这些时间都是由公司支付全额成本购置的公司资产", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P130", "quote": "严格禁止用投票表决来作为决策机制", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P132", "quote": "决策是后果承担者的特权，只能由后果承担者或其授权的受托人作出。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P127", "quote": "被警告者应立即无条件向全体讨论者（注意，不是被评价对象）道歉", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P129", "quote": "原则上不作任何允许两人自由对话的议程安排", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P062", "quote": "它比方案A的成本往往大8-10倍。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P060", "quote": "这个方案效率最高，也是最推荐、最常见的处理方式。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P034", "quote": "这非常像刑事侦查中的案情重建步骤。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P126", "quote": "而仅仅应该只对方案本身发表意见", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P123", "quote": "主持人的首要职责就是保护会议的时间效率", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P136", "quote": "会议主持人应该受过专业会议训练", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["组织管理", "管理方法论", "会议与决策制度", "流程/知识管理"],
   "issue_candidates": ["复盘方法", "问题定义与命名", "案情重建", "解决方案即规则更新", "会议伦理与主持人职责", "投票与决策权限"],
   "text_function_candidates": ["答疑", "操作规程/方法说明", "训诫", "评论批评"],
   "object_candidates": ["企业/公司", "任务小组（task force）", "主持人", "决策机构", "issue 编号系统"],
   "working_keywords": ["复盘", "issue naming", "案情重建", "Case Building", "Solution Forging", "超额投票", "组织规则", "令人满意"]
  },
  "notes": "长文（137 段）方法规程，正文按 Step 1/2/3 组织；P137 明标“（未完，待续）”，故本篇为不完整文本，已在 unresolved_questions 记录。P098 语句疑有脱漏。全文无图片节点。提问者（Q001）问个人复盘方法，作者答组织复盘规程，回答与提问层次不同；未把提问者立场归给作者。"
 },
 "5d8d149d": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何才能做到不在乎？”。作者没有给出“停止在乎”的方法，而是先重新定义“在乎”（资源分配行为），再断言“在乎某人”是语法误用、被停止的对象不配称为“在乎”，从而否定该问法的前提。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P005"], "summary": "定义“在乎”为资源分配行为，分注意力、思考、行动三个阶段；推出两个结论中的第一个：在乎有三个递进等级，在乎程度可用进展到哪个阶段与投入多少资源来量度，以避免自欺欺人。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P015"], "summary": "推出结论二：在乎的对象只能是议题，不能是人或任何意志体；“在乎某人”是逻辑不合法的句子。列出两个致命错误：只关心与该人有关的部分议题；这些议题完整表达时都会出现你自己。于是构成两重偷换，把“我在乎自己的感受”换成“我在乎ta”。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P016", "P026"], "summary": "用三阶段向下检验：人不能被填在“思考”“行动”之后作宾语，故“在乎某人”无法合法向下生长，是“假种子”；真在乎是能长出思考枝干、计划花、行动果的活种子，因此宾语必须是议题。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P027", "P034"], "summary": "反问真在乎者其思考、计划、行动、结果是什么；若都不存在而只以某人为题沉溺于名为“痛苦”的快乐，则是在吸名为“在乎”的毒品；并反驳以“痛苦很难受”否认吸毒，称痛苦是最容易上瘾的毒品，与嗜辣同质。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P035", "P041"], "summary": "结论：要被停止的东西没有资格被称为“在乎”，拿掉桂冠它立刻死亡；先给它戴免罪桂冠再问如何停止，是自欺与快感反刍，所以问者得不到可用回答——报案的是你，绑匪也是你。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“在乎”实质上是资源分配行为，按注意力资源、思考资源、行动资源三个阶段依次分配。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在乎天然分为三个递进等级（决定注意＜决定思考＜决定行动），其具体程度可用进展到哪个阶段、在该阶段投入多少资源来准确量度。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在乎的对象只能是议题，不能是人或任何其他意志体；“在乎某人”是不合法的句式，属被滥用后的语法误用。", "evidence": ["E5", "E6", "E9"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“在乎一个人”可有的含义只能归化为某个议题，例如“这个人不愿如何如何做”，或“在乎某人是否能实现ta的一切愿望”，后者仍是议题，不能无损代替。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以“在乎某人”为题掩盖了两个事实：你只关心与此人有关的部分议题；而那些议题若完整表达，里面都会出现你自己。", "evidence": ["E10", "E11"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓在乎某人，是借议题的双重相关性隐去关于自己的陈述、忽略自己漠不关心的议题，从而把“我在乎自己的感受”偷换成“我在乎ta”。", "evidence": ["E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "语法上不能把“人”填入“思考”“行动”之后作宾语（不能“思考张三”、不能“就张三采取行动”），所以“在乎某人”无法向下合法生长。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“在乎某人”是无法向下生长的“假种子”；真在乎是活种子，能长出思考的枝干、计划的花、行动的果，其前提是宾语为议题。", "evidence": ["E16", "E17"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若真在乎却没有相应的思考、计划、行动与结果，只是以某人为题沉溺于名为“痛苦”的快乐，那就是在吸一种名为“在乎”的毒品。", "evidence": ["E18", "E19"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不存在“让我痛苦的必定不会让我快乐”这样的规则；痛苦是人类最容易上瘾的毒品，与嗜辣火锅无法割舍没有本质区别。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要被停止的那个东西没有资格被称为“在乎”，拿掉桂冠它就会立刻死亡；先给它戴上免于一切罪责的桂冠再问如何停止，是虚情假意的自欺与快感反刍。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这样问的人根本不想那个东西停止，因此得不到可用的回答——报案的是你，绑匪也是你，给人质解救建议没有意义。", "evidence": ["E26", "E27"]}
   ],
   "argument_steps": [
    "先给“在乎”下定义：注意力→思考→行动的三阶段资源分配（P001、P002）。",
    "由定义抽出结论一：三个递进等级；并把“进展到哪一阶段、投入多少资源”作为量度，以免自欺欺人（P003-P005）。",
    "抽出结论二：在乎的对象只能是议题，不能是人（P006）。",
    "对“在乎某人”作出“斩钉截铁的新断言”：该句式不合法（P007）。",
    "用归化法论证：把“在乎某人”的每种含义归化为议题，指出“在乎某人能否心想事成”仍是议题（P008、P009）。",
    "指认归化后暴露的两个致命错误：只关心部分议题；议题完整表达时都有你自己（P012-P014）。",
    "给出偷换结论：两重隐去与忽略，把“在乎自己的感受”说成“在乎ta”（P015）。",
    "用三阶段向下检验语法：人不能作“思考”“行动”的宾语，故该句式无法向下生长（P018-P024）。",
    "以种子比喻作结：假种子 vs 能长出思考、计划、行动的活种子（P024-P026）。",
    "反问真在乎者其思考、计划、行动、结果何在（P027）。",
    "引入“毒品”判断：不存在上述产出而沉溺痛苦，即为吸食名为“在乎”的毒品（P028）。",
    "预先反驳“痛苦很难受”这一否决理由：不存在痛苦必不快乐的规则，痛苦最容易上瘾（P029-P032）。",
    "收束：拿掉“在乎”的桂冠，该物即死；问法本身是不想让它停止的自欺（P035-P039）。",
    "以绑匪与报案者同一人的比喻说明为何没有可用回答（P040、P041）。"
   ],
   "concept_usage": [
    {"term": "在乎", "meaning": "本文指对议题依次分配注意力、思考、行动三种资源的决定与行为；作者主张它不能以人为宾语。", "evidence": "P002", "ambiguity": "日常语义中“在乎某人”被普遍使用，作者以严格语义宣告其不合法，属作者的重新定义。"},
    {"term": "议题", "meaning": "在乎的合法对象，可被思考、可据以行动；作者未给形式定义。", "evidence": "P006", "ambiguity": "“议题”的边界（是否包含愿望、状态、事件）文中未界定。"},
    {"term": "资源分配", "meaning": "注意力资源、思考资源、行动资源三阶段的先后投入，被用作衡量在乎程度的标准。", "evidence": "P002", "ambiguity": "三种资源如何计量、能否折算，文中未说明。"},
    {"term": "痛苦（作为毒品）", "meaning": "作者称沉溺于痛苦本身可获得快乐，痛苦是最容易上瘾的毒品，与嗜辣同质。", "evidence": "P031", "ambiguity": "该断言以类比与断言方式给出，未提供经验依据。"},
    {"term": "假种子／活种子", "meaning": "能否向下生出思考与行动的比喻：以人为宾语是假种子，以议题为宾语是活种子。", "evidence": "P025", "ambiguity": "比喻性判据，未给出可操作的检验标准。"},
    {"term": "桂冠", "meaning": "指先给该物戴上“在乎”之名与免罪之名，使其免于被否定的修辞。", "evidence": "P037", "ambiguity": "“桂冠”未明确定义，靠上下文推断。"}
   ],
   "examples_and_targets": [
    "“思考张三”“就张三采取行动”作为语法反例（作者举例，P021、P022）。",
    "“这个人不愿如何如何做”“某人能否心想事成”作为把“在乎某人”归化为议题的例子（作者举例，P008、P009）。",
    "酷爱吃辛辣火锅、辣得涕泪横流却无法割舍，作为痛苦成瘾的类比（作者类比，P032）。",
    "“让我痛苦的必定不会让我快乐”作为作者反驳的流行说法（被反驳观点，P030）。",
    "“要如何停止它”的问法本身，作为作者批评的自欺与快感反刍对象（被反驳对象，P038）。",
    "报案者与绑匪同为一人的比喻，用来说明问者不想让人质（即该物）被解救（作者修辞，P041）。"
   ],
   "conditions": [
    "作者声明“在乎”不能接人是在“严格语义的限定下”提出的（P009）。",
    "该结论以“当所有人都在误用时，语法缺陷被‘约定俗成’的保护伞遮掩”为背景条件（P023）。",
    "“吸毒”判定以“这些东西都不存在”为条件，即没有相应的思考、计划、行动与结果（P028）。",
    "作者的反驳针对的是以“痛苦很难受”为理由否决“这是在吸毒”的可能性的论法（P029）。",
    "结论成立的隐含前提是“在乎”必须能向下生长出思考与行动，文中以语法与比喻给出而非论证（P024-P026）。"
   ],
   "rhetoric_and_tone": "冷峻、断言式、第二人称质问（“你如果真的在乎”“何以见得？”），大量反问与排比（“你的思考是什么？你的计划是什么？”）；使用“斩钉截铁的新断言”“致命的错误”等强化措辞与“假种子／活种子”“毒品”“桂冠”“绑匪”等比喻；结尾以“（报案的是你，绑匪也是你）”式的反转收束，带训诫与讽刺意味。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001），图片内容未经核验，需人工/多模态复核；已读部分仅为正文文本。",
    "提问者问“如何才能做到不在乎”，作者只否定问法前提，未给出“不在乎”的正面做法，本文未说明。",
    "“议题”的判定边界（哪些心理内容算议题）本文未界定，因此“在乎只能接议题”在操作上不可判。",
    "作者以语法有效性支撑哲学断言，但未讨论“在乎某人”在自然语言中的实际用法是否应被算作反例。",
    "“痛苦是人类最容易上瘾的毒品”为强断言，未给出证据或外部来源，需外部核查。",
    "IMAGE/正文关系不明：图片节点位于正文之后，未说明其内容与论证的关系。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在乎，就是你决定将注意力分配到一个议题上", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "“在乎”在实质上是一种资源分配行为", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "在乎到决定注意 < 在乎到决定思考 < 在乎到决定行动", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "可以用你进展到了哪个阶段，在该阶段投入了多少资源作为准确的量度", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "在乎的对象只能是议题，而不能是人或者任何其他意志体。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "“在乎”是不能合法的接在“某个人”前面的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "你在乎的不是这个人，而在实质上是“这个人不愿如何如何做”这个议题。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "那就是“在乎某人是否能实现ta的一切愿望”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "“在乎一个人”只是一种被滥用后的语法误用", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "你只是用“在乎某人”为题，遮掩了“你其实只关心与这人有关的部分议题”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "就是如果你完整的表达它们，里面都会出现你自己。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "从而将“我在乎自己的感受”，偷换成了“我在乎ta”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "因为你不能将“人”填入到思考的后面作为思考的宾语。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "你可以“思考一个议题”，但是无法“思考张三”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P022", "quote": "你并不能“就张三采取行动”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P024", "quote": "是一颗“假种子”。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P025", "quote": "真在乎却是一颗活种子", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "你不过是在吸一种名为“在乎”的毒品。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P027", "quote": "你的思考是什么？你的计划是什么？你的行动是什么？你的结果是什么？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "世界上根本不存在“让我痛苦的必定不会让我快乐”这么美好的规则。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P031", "quote": "痛苦是人类最容易上瘾的毒品。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P032", "quote": "这和酷爱吃辛辣的火锅，辣得涕泪横流却无法割舍，没有本质的区别。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P036", "quote": "要被停止的那个东西，根本没有丝毫的资格被称为“在乎”。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P037", "quote": "拿掉它的桂冠，它就会立刻死亡。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P038", "quote": "只不过是一种虚情假意的自欺和花样巧妙的快感反刍。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P039", "quote": "只要这样问，你就根本不想那个东西停止。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P041", "quote": "别看报案的是你，但其实绑匪也是你", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学/情绪", "语言哲学/语义分析", "情感关系", "自我认识"],
   "issue_candidates": ["在乎的定义", "在乎某人是否合法", "自我欺骗与偷换", "痛苦成瘾", "提问前提的否定"],
   "text_function_candidates": ["答疑", "概念辨析", "论辩", "训诫/批评"],
   "object_candidates": ["提问者（“你”）", "“在乎某人”这一说法", "议题"],
   "working_keywords": ["在乎", "议题", "资源分配", "注意力资源", "假种子", "痛苦", "毒品", "桂冠"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 1 个图片节点（IMG001：//asset.sooon.ai/p/2021-05/01/7bdc3549fdca20243c43f5f52d092697.jpg），图片内容未经核验，需图像核验；已读部分为正文文本。作者未直接回答“如何才能做到不在乎”，而是否定该问法的前提，属作者有意的重构，未把提问者立场归给作者。"
 },
 "a4294198": {
  "analysis": {
   "question_context": "提问者（Q001）问：在南方完全没有蟑螂的房子存在吗？如果存在，是如何做到使蟑螂不入侵的？作者没有回答“是否存在”或自身经验，而是给出一条防治思路：把第一道防线从家门口推到室外。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P003"], "summary": "指出家里有蟑螂的主要原因是人把第一道防线设在自己家门口；苦恼方法无效其实是在苦恼家门以内的方法无效；并以“野战无能，则城不可守”作类比。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P007"], "summary": "给出具体做法：把杀蟑饵剂投放范围扩到门外五十米以外，强化投放邻居、上下各三层楼的阴角转折处、接近水源和排水管道的墙角、垃圾投放处等，并定期维持、再观察效果。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P010"], "summary": "以防蚊同理作推广：消灭驱散窗外、门廊、花园、公共绿地及附近积水处的蚊子，室内密度自然下降，只在卧室灭蚊则事倍功半、永无穷尽；末句点明这说的不是治虫。", "role": "example"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家里有蟑螂的一大主要原因，是人总是把第一道防线设置在自己家门口。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "苦恼方法无效时，其实是在苦恼自己家门以内的方法无效，即防线位置本身有问题。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应把杀蟑饵剂的投放范围扩张到家门外五十米以外，强化投放邻居、上下各三层楼的阴角转折处、接近水源和排水管道的墙角、垃圾投放处等，并定期维持后再观察效果。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "防蚊同理：消灭和驱散窗外、门廊、花园、公共绿地和附近一切积水处的蚊子，室内蚊子密度自然下降；只在自己卧室灭蚊则事倍功半且永无穷尽。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本文所讲的并不真的是治虫（作者以此点明前文是借题说明的道理）。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "先把问题重新定位：家庭蟑螂的主要成因是防线设在自家门口（P001）。",
    "指认苦恼的错位：所苦恼的是家门以内方法无效（P002）。",
    "以兵家格言“野战无能，则城不可守”作类比，支持把战场推到室外（P003）。",
    "给出行动方案：门外五十米以外扩大饵剂投放，覆盖邻居、上下三层楼、阴湿墙角与垃圾投放处（P004、P005）。",
    "补充维持与验证要求：定期维持、再观察效果（P006、P007）。",
    "用防蚊作同构推广，反证只在室内处理事倍功半（P008、P009）。",
    "末句抽离：这说的不是治虫（P010）。"
   ],
   "concept_usage": [
    {"term": "第一道防线", "meaning": "防治的初始拦截位置；作者指人默认把它设在自家门口，因而错误。", "evidence": "P001", "ambiguity": "未说明除“家门口／门外五十米”之外还应有哪些防线层级。"},
    {"term": "家门以内／以外", "meaning": "区分室内单点治理与室外环境治理的空间范围。", "evidence": "P002", "ambiguity": "以“五十米”“上下各三层楼”作边界，但未给出该范围的确定依据。"},
    {"term": "强化投放", "meaning": "在关键点位增加饵剂投放（作者未给剂量、频次与药种）。", "evidence": "P005", "ambiguity": "具体操作参数本文未说明。"},
    {"term": "野战／城", "meaning": "以军事攻守比喻室外治理与室内防护的关系。", "evidence": "P003", "ambiguity": "比喻未展开，且与后文“不是治虫”的指向关系未明说。"}
   ],
   "examples_and_targets": [
    "杀蟑饵剂及其投放范围（家门外五十米以外）（作者建议的措施，P004）。",
    "邻居、上下各三层楼的阴角转折处、接近水源与排水管道的墙角、垃圾投放处（作者列举的投放点位，P005）。",
    "防蚊：窗外、门廊、花园、公共绿地及附近一切积水处（作者用作同构例证，P008）。",
    "只在卧室灭蚊的做法（作者指为事倍功半的反面做法，P009）。",
    "“野战无能，则城不可守”（作者引用的兵家式格言作类比，P003）。",
    "末句所指的“不是治虫”的真正对象（作者未明说，待核，P010）。"
   ],
   "conditions": [
    "提问场景限定为南方（提问者语境）与“如果存在”的条件问法（Q001）。",
    "投放范围条件：家门以外五十米、邻居与上下各三层楼（P004、P005）。",
    "要求定期维持，并“再观察一下效果”，即以效果复核为后续条件（P006、P007）。",
    "防蚊推广的成立条件被表述为“附近一切积水处”都被处理（P008）。",
    "方案涉及邻居与公共区域空间，本文未讨论其可行性与合规条件。"
   ],
   "rhetoric_and_tone": "短促、口诀式，句子极简并多用祈使句（“试试看”“定期维持”“再观察一下效果”）；用“野战无能，则城不可守”的兵家格言作类比；结尾以“其实，这说的不是治虫”陡然抽离，暗示借题说理，带寓言与留白意味。",
   "unresolved_questions": [
    "作者未回答提问者所问的“南方完全没有蟑螂的房子是否存在”，只给方法思路。",
    "末句“其实，这说的不是治虫”未说明究竟在说什么，所指对象待核。",
    "“家门外五十米”“上下各三层楼”的范围依据、饵剂种类、剂量与投放频次、成本均未说明。",
    "把饵剂投放到邻居与楼道、垃圾投放处等他人/公共空间，涉及许可、安全与他人影响，本文未讨论。",
    "防蚊与治蟑被作者当作同一道理，但两者在孳生机制上的差异未作说明。",
    "本篇无图片节点，不涉及图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "是人总是把第一道防线设置在自己家门口", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "其实是在苦恼自己家门以内的方法无效", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "野战无能，则城不可守。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "试试看将杀蟑饵剂的投放范围扩张到家门外五十米以外看看。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "一切接近水源、排水管道的墙角、垃圾投放处等等都强化投放", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "则室内的蚊子密度自然下降", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "只在自己卧室里“灭蚊”，当然是事倍功半，而且永无穷尽了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "其实，这说的不是治虫。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生活经验/居家防治", "公共卫生/病媒防治", "管理隐喻"],
   "issue_candidates": ["蟑螂防治", "防治防线位置", "室外源头治理", "防蚊同理", "借虫喻理"],
   "text_function_candidates": ["答疑", "经验建议", "隐喻/寓言式短评"],
   "object_candidates": ["南方住宅", "邻居与楼道/上下三层楼", "杀蟑饵剂", "蚊子与积水处"],
   "working_keywords": ["第一道防线", "杀蟑饵剂", "阴角转折处", "定期维持", "积水处", "野战无能则城不可守"]
  },
  "notes": "极短文（10 段，264 字）。提问者问“南方完全没有蟑螂的房子是否存在”，作者未答存在性，只给室外防线思路，末句点明“不是治虫”但未说明所指，已记入 unresolved_questions。无图片节点。"
 },
 "1e6709b6": {
  "analysis": {
   "question_context": "提问者（Q001）问“芯片半导体是否为未来五年的科技风口？”作者直接回答：真正的风口是精细化工、精密加工、精密光学等一批与“芯”“半导体”“微电子”名字无关的行业，“芯片半导体”并不是；后半篇另就知识管理体系补充几句。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "正面给出未来五年的风口清单（精细化工、精密加工、精密光学、自动化控制、系统集成与测试、公共关系管理、政府关系管理、行业规划与治理、税收规划和战略财务管理、研发体制的效率研究、学术组织的伦理研究、知识体系建设与管理），并否定“芯片半导体”是风口。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P007"], "summary": "论证这些行业才真正卡住芯片行业，且相比光刻机、晶圆制造、产线管理、封装测试等“纯正芯片产业”，其优势是达到芯片极端要求后可替代的领域远不止芯片；而纯正芯片产业即使做成也要面对现存领先对手的强烈竞争；故其威胁性、战略意义与投资预期有效性全面压倒被追捧的芯片产业本身，是“隐形赛手”与真正主攻方向。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P008"], "summary": "正文中出现“中国芯片产业前景到底怎么样？”一行，疑为站内链接或话题文本，阅读包标为 lexical 未覆盖片段。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P015"], "summary": "补充知识管理体系：不只是建文件夹放 md 文件，而要拉近知识沉淀与应用的距离、建立迭代规范和基于工具的工作管线；批评过于注重产品而轻视过程中产生的知识与工具，称后者才是最重要的产出物；举 CATIA、Solidworks、Alias、AutoCAD、Unreal、EDA 为过程工具；指出只停在存档化、文件化不够，需规范化尤其工具化，只做知识库只是一半且徒耗成本。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "精细化工、精密加工、精密光学、自动化控制、系统集成与测试、公共关系管理、政府关系管理、行业规划与治理、税收规划和战略财务管理、研发体制的效率研究、学术组织的伦理研究、知识体系建设与管理才是未来五年的风口。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“芯片半导体”并不是未来五年的科技风口。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述行业是真正拦住芯片行业的东西，它们相比“纯正芯片产业”的优势在于：若能支撑芯片产业的极端要求，可实现工艺替代的领域远不止芯片。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“纯正芯片产业”即使实现，也要面对现存领先对手的强烈竞争。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些芯片相关产业对西方技术优势的威胁性、对中国整个产业技术能力的战略性意义，尤其是投资的预期有效性，全面压倒被直接瞩目、无脑追捧的“芯片产业”本身。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些产业是名字与“芯”“半导体”“微电子”无关的隐形赛手，它们才是真正的主攻方向。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "知识管理体系并不只是建立一个文件夹放一堆 md 文件，而是要拉近知识沉淀和知识应用的距离，建立迭代规范和基于工具的工作管线。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我们过于注重产品、过于轻视产品过程中产生的知识和工具，实际上后者才是生产过程中最重要的产出物，而不是产品本身。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "CATIA、Solidworks、Alias、AutoCAD、Unreal 以及芯片设计的 EDA 软件，都是为完成某个项目目的而产生的过程工具，是知识管理体系自然沉淀的结果；EDA 工具研发可典型地归入这一类。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在的做法往往只停留在存档化、文件化，要做到规范化尤其工具化才算真正建立起知识体系；“做出知识库”顶多算建立前提和基础，只做这一半徒耗成本，也难坚持。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "直接给出判断：把一批非芯片命名的行业列为未来五年风口（P001）。",
    "否定提问所问的对象：“芯片半导体”其实并不是（P002）。",
    "给出理由一：这些行业才是真正拦住芯片行业的东西（P003）。",
    "给出理由二：它们的技术一旦满足芯片的极端要求，可替代的领域远不止芯片（P003）。",
    "给出对比：纯正芯片产业即使做成仍要面对领先对手的强烈竞争（P004）。",
    "作出比较性结论：在威胁性、战略意义与投资预期有效性上全面压倒芯片产业本身（P005）。",
    "命名与收束：称之为“隐形赛手”，并称它们才是真正的主攻方向（P006、P007）。",
    "转入补充议题：关于知识管理体系“多说几句”（P009）。",
    "界定知识管理不只是文件夹与 md 文件，而是迭代规范与工具化工作管线（P010）。",
    "提出价值重排：知识与工具才是生产过程中最重要的产出物（P011）。",
    "举例支撑：CATIA、Solidworks、Alias、AutoCAD、Unreal、EDA 皆为过程工具与自然沉淀的结果（P012）。",
    "指出落差与结论：只做存档化、文件化不够，须规范化、工具化；只做知识库只是一半，徒耗成本（P013-P015）。"
   ],
   "concept_usage": [
    {"term": "风口", "meaning": "本文指未来五年值得投入、具有战略与投资价值的产业方向，判据被表述为威胁性、战略意义与投资预期有效性。", "evidence": "P001", "ambiguity": "“风口”未给定义，与提问者的“科技风口”是否同义未说明。"},
    {"term": "“纯正芯片产业”", "meaning": "作者用来指光刻机制造、晶圆制造、产线管理、封装测试等直接与晶片工艺相关的环节（带引号，属作者自造提法）。", "evidence": "P003", "ambiguity": "该分类边界由作者自定，未说明依据。"},
    {"term": "隐形赛手", "meaning": "名字与“芯”“半导体”“微电子”无关、因而不被瞩目但被作者视为真正主攻方向的产业。", "evidence": "P006", "ambiguity": "哪些具体企业或行业算“隐形赛手”，本文未列举名单。"},
    {"term": "知识管理体系", "meaning": "拉近知识沉淀与知识应用距离、建立迭代规范和基于工具的工作管线的机制，而非文件夹＋md 文件的集合。", "evidence": "P010", "ambiguity": "“md 文件”“规范化”“工具化”的具体所指与实现方式未展开。"},
    {"term": "过程工具", "meaning": "为完成某个项目目的而产生、可沉淀复用的工具（如 CATIA、EDA 等），被作者称为生产过程中最重要的产出物。", "evidence": "P012", "ambiguity": "未说明工具化的投入产出如何衡量。"}
   ],
   "examples_and_targets": [
    "精细化工、精密加工、精密光学、自动化控制、系统集成与测试、公共关系管理、政府关系管理、行业规划与治理、税收规划和战略财务管理、研发体制的效率研究、学术组织的伦理研究、知识体系建设与管理（作者列出的风口行业清单，P001）。",
    "光刻机制造、晶圆制造、产线管理、封装测试（作者所称“纯正芯片产业”的举例，P003）。",
    "“被直接瞩目、无脑追捧”的芯片产业（作者批评的对象，P005）。",
    "CATIA、Solidworks、Alias、AutoCAD、Unreal 与芯片设计的 EDA 软件（作者用作过程工具与知识沉淀的例证，P012）。",
    "“建立一个文件夹放一堆 md 文件”的做法（作者否定的知识管理做法，P010）。",
    "EDA 工具研发（作者建议归入工具化一类的例子，P014）。",
    "西方技术优势、中国整个产业技术能力（作者论述中的比较对象，P005）。"
   ],
   "conditions": [
    "时间范围由提问限定为“未来五年”，作者的判断也在该跨度内作出（Q001、P001）。",
    "条件句：上述行业“如果做到能支撑芯片产业的极端要求”，才可实现远不止芯片的工艺替代（P003）。",
    "比较性判断以“投资的预期有效性”等为标准，但本文未给出标准权重或数据（P005）。",
    "知识管理的讨论被作者定位为“关于知识管理体系，多说几句”的补充，不是全篇主论点（P009）。",
    "结论性表述“只做这一半，其实只是徒耗成本”的前提是知识管理必须做到工具化（P015）。"
   ],
   "rhetoric_and_tone": "判断直下、口径强硬：开篇即以长清单正面断言，第二段用“其实并不是”直接否定提问；使用“无脑追捧”“隐形赛手”“真正的主攻方向”等带评价色彩的措辞；后半篇转入实务评论口吻（“多说几句”），以产品与知识的价值高低作对比，带训诫与行业评论意味。",
   "unresolved_questions": [
    "P008“中国芯片产业前景到底怎么样？”在阅读包中标为“lexical未覆盖片段”，疑为站内问题链接或话题文本混入正文，是否属正文待核。",
    "作者未说明“未来五年”判断的依据、数据来源或时间起点，也未给出可检验的判定标准。",
    "“对西方技术优势的威胁性”“投资的预期有效性”等比较性断言未附论证或外部依据，需外部核查。",
    "“md 文件”具体所指（Markdown 文件？内部文档？）与“工具化”的实现方式本文未说明。",
    "风口清单与知识管理两部分之间缺少过渡，二者是否属同一论证，本文未说明。",
    "本篇无图片节点，不涉及图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "知识体系建设与管理才是未来五年的风口。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "“芯片半导体”其实并不是。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "以上这些行业是真正拦住芯片行业的东西", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "那么它们可以实现工艺替代的领域可是远不止芯片这么简单", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "却即使实现了也要面对现存领先的对手的强烈竞争", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "要全面的压倒那些被直接瞩目、无脑追捧的“芯片产业”本身", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "这都是些名字根本与“芯”、“半导体”、“微电子”无关的隐形赛手。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "它们才是真正的主攻方向。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "这并不只是建立一个文件夹放一堆md文件而已", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "建立迭代规范和基于工具的工作管线", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "实际上后者才是生产过程中最重要的产出物，而不是产品本身。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "这些都是为了完成某个项目目的而产生的过程工具，是知识管理体系自然沉淀的结果。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "你可以典型的把“EDA工具研发”加入这一类。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "但实际上要做到规范化——尤其是——工具化，才算是真正建立起了这样的知识体系。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "顶多算建立了知识管理的前提和基础，只做这一半，其实只是徒耗成本", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P008", "quote": "中国芯片产业前景到底怎么样？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["产业经济/科技政策", "半导体产业", "投资方向判断", "知识管理/研发管理"],
   "issue_candidates": ["芯片半导体是否风口", "产业卡点与工艺替代", "隐形赛手与主攻方向", "投资预期有效性", "知识管理体系与工具化"],
   "text_function_candidates": ["答疑", "判断/评论", "行业批评"],
   "object_candidates": ["芯片半导体产业", "光刻机/晶圆制造/封装测试", "CATIA/Solidworks/Alias/AutoCAD/Unreal/EDA", "西方技术优势", "中国产业技术能力"],
   "working_keywords": ["风口", "纯正芯片产业", "隐形赛手", "工艺替代", "知识管理体系", "工具化", "EDA工具研发"]
  },
  "notes": "短文（15 段，782 字）。P008“中国芯片产业前景到底怎么样？”在阅读包中标为“lexical未覆盖片段”，疑为站内问题链接/话题文本混入正文，已在 unresolved_questions 与 evidence（E16，relation=context）登记，未据此改写正文。作者对“未来五年风口”的判断属其本人主张，未把提问者的问法当作作者立场。无图片节点。"
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
