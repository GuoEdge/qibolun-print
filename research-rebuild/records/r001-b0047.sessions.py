# -*- coding: utf-8 -*-
"""批次 r001-b0047 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0047.sessions.py            # 写 out/r001-b0047.out.jsonl
  python3 records/r001-b0047.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0047"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0047.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "3ec58eae": {
  "analysis": {
   "question_context": "提问者（Q001）问中国未来会不会超越美国、成为世界第一强国。作者先指出该问法字面上缺少意义（未来无限久远，只要中国不灭亡总会有超过的时段），再把提问者的实际关切转述为中国是否正处在超过美国的趋势中，并给出“目前还难说”的回答；正文后半段转为反驳“精英与富人外流说明中国赶超不了美国”的观点，并解释人才与富人外流的动因和数量级。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "判定提问字面缺少意义，转述提问者实际想问的趋势问题，回答为“很难说”。", "role": "conclusion"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007"], "summary": "摆出一种以精英留美、富人外流推断中国赶超不了美国的观点，并明确否定。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "以中国市场规模与产业链为据，说明追赶者可凭性价比取胜，先行者优势有限且更易踩坑。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "以钱学森与两弹一星为例，主张势均力敌的精英阶层不是实效上追平美国的必要条件。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018"], "summary": "推进到实效持平后的阶段：美国靠悬殊精英流入维持平手，并以100:5与100:10反问平衡移动方向。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029"], "summary": "以追赶战略非精英密集与细分行业人才分布模型，解释人才外流及其对两国均无显著影响。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "论富人移民：其悲观实为对自己的悲观，因自身处境与运气焦虑而选择静止的环境。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P039", "P040", "P041", "P042"], "summary": "以绿卡与投资移民的数量级对比中国新增富人，判断影响可忽略。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P043", "P044", "P045"], "summary": "结论：中国会追平并在一段时期压倒美国，但可能因文化成熟速度而在超越之时再度落后。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“中国未来会不会超越美国”从字面意义上说是缺少意义的问题，因为未来无限久远，只要中国不灭亡总会有超过美国的时段。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者推测提问者大概想问的是中国是否正处在超过美国的趋势中。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者回答“目前还难说”：美国有挫折、中国有赶超，但实现压倒性优势还有很长的过程，且过程中美国可能改正错误、中国可能遇到意外挫折。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定把“留美学生归国率不高、富人外流、最大来源地是中国而最大目的地是美国”当作中国赶超不了美国的证据，直言这是不对的。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "一种被作者转述的观点认为：顶尖大学相当部分学生留美且归国率不高、很多富人外流，最大来源地是中国而最大目的地是美国，就意味着中国赶超不了美国。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张中国要赶超美国并不需要这么多精英和富商。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把中国的基本特性表述为：用超大规模市场支撑超大规模的制造力，从而使稍次一级的技术在综合性价比上压倒第一线的技术。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者描述追赶的常态：最先进的东西在欧美出现，中国稍后借助自己的人力资源模仿七八成，凭借大市场与完整产业链，以性能约一半、价格不到对手一半的版本竞争。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为高端产品不一定会赢，先行者在极为高超的追赶者面前很难保持数量级优势，往往只有一倍以内的优势。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出先行者比追赶者有更大机会踏入未知的陷阱。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以两弹一星年代为例，主张一旦有并不非常突出的人才在中国点破关窍，中国就能发展出虽弱势但可靠数量竞争的竞品。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言“和美国势均力敌的精英阶层”不是中国以自己的方式在实效上追平美国的必要条件，并强调关键词是“在实效上追平”。", "evidence": ["E14", "E15"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者推测若在实效上持平，世界精英的流向恐怕就不会如此悬殊分明。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称美国正是靠悬殊的精英流入水平（比如100:5）才维持着“实效的平手”。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出：如果100:5时是“实效的平手”，那么100:10会使平衡向哪一方移动；正文未直接给出答案。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以追赶战略的性质解释中国大量人才外流：该战略虽同样需要大量精英，但总体上是非精英密集的策略。", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以细分行业的人才分布说明创新用人：一百个精英朝十个方向探索，最终约两三个成功，约20%精英发财、40%保住饭碗、剩下40%失业转行。", "evidence": ["E20", "E21"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称追赶一方只需追赶两个方向，只有二十个算稳定的就业职位。", "evidence": ["E22"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为追赶国却有规模远超领先国的高等教育，中国出产远超需要的高等教育毕业生，因此大量外溢不可避免。", "evidence": ["E23", "E24"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断外溢到美国的那部分大部分是失业的40%，在国外送外卖、搬砖，或回国去抢那二十个职位。", "evidence": ["E25"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这部分人既未显著改变美国优势、也未耽误中国优势，因为在两国都属过剩部分。", "evidence": ["E26"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑富人移民的动机：如果他们不是在国内失败了，怎么舍得抛家舍业跑路。", "evidence": ["E27"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为这些人对“中国”的悲观实际上是对自己的悲观，他们并不真关心中国悲观与否，也缺少研究与判断的基本工具。", "evidence": ["E28", "E29"]},
    {"claim_id": "C024", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称很多人其实是历史盲，大概率是靠运气而不是能力上位的。", "evidence": ["E30"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把他们的戒慎恐惧解释为江湖越老越发觉自身运气成分而胆子变小，并称他们不会承认且有很强的否认能力。", "evidence": ["E31"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断定他们是因为对自己的悲观而跑路的，并代拟其口吻说“中国悲观不悲观我不知道，但是我自己看起来不妙”。", "evidence": ["E32"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为他们离开的不是“危险”地区而是“快速发展地区”，去往自认为几十年不变、养老金绝对够花的地方。", "evidence": ["E33"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这些人出身精英，但做出该决定起基本就打算退隐江湖。", "evidence": ["E34"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提示数量级：美国一年只发几万张绿卡，其中大量是亲属团聚与技术专长类，投资移民类别人数很少。", "evidence": ["E35"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称中国一年新增的同级别富人比投资移民多出几个数量级，并以四十年多出的几亿中产阶级为旁证。", "evidence": ["E36", "E37"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者判断富人移民对中国的影响基本可以忽略。", "evidence": ["E38"]},
    {"claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者表示毫不怀疑中国会追平美国，并认为挟追平之势的惯性还能在一定时期压倒美国。", "evidence": ["E39"]},
    {"claim_id": "C033", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者怀疑以目前中国文化发展的成熟速度，可能在中国超过美国之时就是再次落后于美国的开始，并以“老王病危而新王未过青春期”作比。", "evidence": ["E40", "E41"]}
   ],
   "argument_steps": [
    "定义/澄清：先指出提问字面上无意义（未来无限久远，只要中国不灭亡总会有超过的时段），再把问题转译为“是否处在超过美国的趋势中”。",
    "初步结论：答案是目前还难说、很难说，并把过程性条件（美国可能改正错误、中国可能遇意外挫折）一并给出。",
    "树靶与否定：提出“精英留美、富人外流即赶超不了”的观点，直接判为不对。",
    "理由一：赶超美国不需要这么多精英和富商；中国的基本特性是超大规模市场支撑超大规模制造力，使稍次一级技术在综合性价比上压倒第一线技术。",
    "类比/常态叙述：最先进技术在欧美出现，中国稍后模仿七八成，以约一半性能、不到一半价格竞争。",
    "理由二：先行者很难保持数量级优势（往往一倍以内），却更可能踏入未知陷阱。",
    "例证：钱学森与两弹一星年代，精英数量质量差距更大，但关窍被点破后即可产出可数量竞争的竞品。",
    "阶段结论：势均力敌的精英阶层不是实效上追平的必要条件（限定“在实效上追平”）。",
    "条件推进：若在实效上持平，精英流向不再悬殊；美国靠100:5式悬殊流入维持实效平手，故反问100:10的平衡走向。",
    "另一面解释：追赶战略是非精英密集策略；用一百精英探索十方向、最终两三个成功、20%/40%/40%的行业模型说明人才过剩与失业。",
    "推论：追赶方只需两个方向、二十个稳定职位，而追赶国有远超领先国的高等教育，故大量外溢不可避免。",
    "外溢者的去向与效果：多为失业的40%，在美中两国都属过剩部分，故两边优势都未显著改变。",
    "富人移民部分：以反问归因于其在国内失败；称其悲观实为对自己的悲观，缺少宏观判断工具、多为运气上位，因自身处境而退隐。",
    "数量级反驳：绿卡总量与投资移民占比有限，中国新增富人高出几个数量级，故影响可忽略。",
    "最终结论与让步：不怀疑中国会追平并在一段时期压倒美国；但怀疑以目前文化成熟速度，超越之时即再度落后的开始。"
   ],
   "concept_usage": [
    {"term": "超英赶美", "meaning": "仅出现在标题，正文未再使用该词；正文实际讨论的是中国追平并一定时期压倒美国、以及之后是否再度落后。", "evidence": "P043", "ambiguity": "标题词与正文结论不完全对应，标题的覆盖范围需读者自行连接。"},
    {"term": "在实效上追平／实效的平手", "meaning": "衡量标准不是名义上的精英数量或产品档次，而是实际竞争结果上的持平；作者特意提醒“注意看清楚”。", "evidence": "P015", "ambiguity": "未给出量化指标或判定标准。"},
    {"term": "中国的基本特性", "meaning": "作者用引号给出的定义式表述：用超大规模市场支撑超大规模的制造力，从而使稍次一级的技术在综合性价比上压倒第一线的技术。", "evidence": "P008", "ambiguity": "被称为“基本特性”，但未说明形成时间、适用范围与反例。"},
    {"term": "非精英密集的策略", "meaning": "形容中国的追赶战略虽需要大量精英，但相对领先国的创新模式对精英数量的需求更低。", "evidence": "P020", "ambiguity": "未定义“精英”，也未给出量化对比。"},
    {"term": "精英", "meaning": "文中在顶尖大学学生、知识精英与富商等意义上使用，未作统一定义。", "evidence": "P005", "ambiguity": "人才与富商被并置讨论，二者是否可归入同一范畴文中未说明。"},
    {"term": "软“强奸适应性”测试", "meaning": "仅出现在末尾，用于描述男性追逐知识时的动机，指对精神侵入的适应或耐受测试。", "evidence": "P005", "ambiguity": "作者自造短语且未定义，加引号表示借喻，含义不确定。"},
    {"term": "文化发展的成熟速度", "meaning": "用于解释中国超越美国后可能再度落后的原因。", "evidence": "P044", "ambiguity": "全文未定义，也无衡量指标或判断依据。"}
   ],
   "examples_and_targets": [
    "钱学森（P012）：作者称为“非常现实的例子”，用作追赶可行性的例证。",
    "两弹一星年代中美知识精英数量与质量差距（P013）：作者的历史叙述与例证，未给数据出处。",
    "细分行业人才分布模型（P021）：一百个精英、十个探索方向、两三家头部企业六个方向、两到三个成功、20%发财／40%保饭碗／40%失业，作者构造的说明性模型，未说明是否为实证统计。",
    "职业列举（P021、P025、P027）：卖二手车、洗盘子、卖保险、搞金融、送外卖、搬砖，属修辞性举例。",
    "酒桌议论与“亲身经历”（P032）：作者用来刻画移民富人的判断方式，属修辞材料兼批评对象。",
    "美国绿卡与投资移民类别（P039）：作者用于数量级反驳的数据性说法，无年份与出处。",
    "四十年多出来的几亿中产阶级（P041）：作者作为旁证的反问式数据，无出处。",
    "“老王眼看病危，而新王却还没有度过青春期”（P045）：结尾比喻，指美国相对衰落而中国尚未成熟。"
   ],
   "conditions": [
    "字面判断依赖“只要中国一直不灭亡”这一前提，且时间范围为无限久远。",
    "“目前还难说”的理由包含两个可能性条件：美国可能会改正自己的错误、中国可能会遇到意外挫折。",
    "“不需要这么多精英和富商”以“仔细考虑清楚”为前提性呼吁，并非给出量化门槛。",
    "性价比竞争故事依赖中国的市场规模大、产业链完整这两个条件。",
    "先行者优势有限的说法限定于面对“极为高超的追赶者”的情形。",
    "P016 明确以“如果走到这一步”“在实效上持平的话”为条件；100:5、100:10 是示例性假设数值。",
    "人才外流的解释建立在作者所观察的“一个细分行业”模型之上，模型的普遍性未说明。",
    "富人移民影响“基本可以忽略”依赖数量级对比这一条件，且原文未说明统计口径与年份。",
    "最终怀疑限定于“以目前的中国的文化发展的成熟速度”，且用“可能”“我怀疑”保留不确定性。"
   ],
   "rhetoric_and_tone": "以答疑开场、随即转为论辩。语气自信、口语化，多用破折号引出断言与反问（“这是不对的”“别忘了”“这么说吧”）；用“注意看清楚”强调限定语。对移民富人一段带有讽刺与训诫意味（“酒桌上头头是道”“历史盲”“靠运气而不是能力上位”），并用第一人称代拟其口吻（“我自己看起来不妙”“我要跳进一个静止的世界里去”“你这里机会是多、危险也多”）以呈现其心态。结尾以“老王／新王”比喻收束，把长时段判断压缩成形象对照。",
   "unresolved_questions": [
    "P035 后半与 P036 使用第一人称（“我自己看起来不妙”“我看不清中国的下一个新革命性政策对我是利空还是利好”“你这里机会是多、危险也多”），正文未加引号或说话人标注；这段是作者完全代拟移民者心态还是转述他人自述，文中未说明。",
    "美国绿卡总量“几万张”、投资移民类别人数、中国新增富人量级、四十年“几亿中产阶级”均无年份、口径与出处，属待外部核查的事实性说法。",
    "P021 的“一百个精英／十个方向／两到三个成功／20%、40%、40%”是示意模型还是实证统计，文中未说明。",
    "标题“超英赶美”未在正文出现，与正文结论（会追平并一段时期压倒、但可能再度落后）的对应关系需读者自行连接。",
    "P010 出现“只有只有一倍以内的优势”，疑为重复字或衍文，本记录按原文保留，是否影响理解待核。",
    "brief 字段在“要实现中国毋庸置疑的压倒性优”处截断，与正文 P003 表述不完全一致；brief 仅作导航，正文为准。",
    "发布时间 2020-05-03 与更新时间 2021-05-25 不同，语料 provenance／superseded 均为 null，未提供版本差异说明；本记录以当前 v2 文本为准。",
    "“文化发展的成熟速度”（P044）未定义，作者也未给出衡量方式与判断依据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这问题从字面意义上说是一个缺少意义的问题", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "提问者大概想问的是中国是不是正在超过美国的趋势中", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "答案是“目前还难说”", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "这个过程里美国可能会改正自己的错误，中国可能会遇到意外挫折", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P004", "quote": "所以答案是很难说", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "以至于最大来源地是中国、最大目的地是美国，就意味着中国赶超不了美国", "relation": "context"},
    {"key": "E7", "paragraph_id": "P006", "quote": "这是不对的", "relation": "contradicts"},
    {"key": "E8", "paragraph_id": "P007", "quote": "中国要赶超美国，并不需要这么多精英和富商", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "用超大规模市场支撑超大规模的制造力，从而使稍次一级的技术在综合性价比上压倒第一线的技术", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "最先进的东西在欧美出现，中国在稍后借助自己的人力资源模仿了个七八成", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "先行者在极为高超的追赶者面前其实很难保持数量级的优势", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "先行者却有比追赶者大得多的机会踏入未知的陷阱", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "一旦有一个并不是非常突出的人才在中国点破了关窍", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "并不是中国以自己的方式在实效上追平美国的必要条件", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "注意看清楚，是“在实效上追平”", "relation": "qualifies"},
    {"key": "E16", "paragraph_id": "P016", "quote": "世界精英的流向恐怕就不是这么悬殊而分明了", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "美国是靠着悬殊的精英流入水平（比如100:5）才维持着“实效的平手”的", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "那么100:10会导致平衡向哪一方移动？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "但却总体上是非精英密集的策略", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P021", "quote": "创新需要一百个精英去朝十个方向探索", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "剩下的40%则会失业", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "却只需要追赶两个方向，只有二十个算是稳定的就业职位", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "中国出产了远远超过需要的高等教育毕业生，多到去送外卖、搬砖", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P025", "quote": "显然不发生大量的外溢是不可能的", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P027", "quote": "大部分都是那失业的40%，后来在国外送外卖、搬砖", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P029", "quote": "既没有显著改变美国的优势——因为在美国他们很不幸的大概率属于过剩的部分", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P031", "quote": "如果他们不是在国内失败了，他们怎么舍得抛家舍业跑路？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P032", "quote": "他们对“中国”的悲观，实际上是对自己的悲观", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P032", "quote": "也根本缺少研究和判断的基本工具", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P033", "quote": "大概率是靠运气而不是能力上位的", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P034", "quote": "与其说是因为中国未来悲观，不如说是江湖越老越发觉自己的运气成分，于是胆子越小了", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P035", "quote": "中国悲观不悲观我不知道，但是我自己看起来不妙", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P037", "quote": "他们是离开了“快速发展的地区”，去一个他们自认为将来几十年都不会变，而自己的养老金绝对够花的地方", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P038", "quote": "基本上就是打算退隐江湖了", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P039", "quote": "属于投资移民类别的一共才多少人？", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P040", "quote": "掂量一下中国一年会出现多少个这个级别的新富人？多出几个数量级", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P041", "quote": "否则这四十年多出来的这几亿中产阶级哪里来的？", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P042", "quote": "影响基本可以忽略", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P043", "quote": "我一点都不怀疑中国会追平美国", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P044", "quote": "但我怀疑以目前的中国的文化发展的成熟速度，可能超过美国时，就是再次落后于美国的开始", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P045", "quote": "老王眼看病危，而新王却还没有度过青春期", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系／中美关系", "经济与技术发展", "人才与人口流动", "社会心态评论"],
   "issue_candidates": ["中国能否超越美国", "精英与富人外流的影响", "追赶型技术战略与性价比竞争", "移民动机与数量级"],
   "text_function_candidates": ["答疑", "论辩", "反驳", "评论"],
   "object_candidates": ["中国", "美国", "钱学森", "两弹一星时期", "留美学生", "投资移民与富人移民", "中产阶级"],
   "working_keywords": ["超英赶美", "实效上追平", "非精英密集", "超大规模市场", "归国率", "绿卡", "投资移民"]
  },
  "notes": "本篇无图片节点，正文 2049 字（UTF-16），全文读完。brief 在“要实现中国毋庸置疑的压倒性优”处截断，与正文 P003 不完全一致，仅作导航。发布时间 2020-05-03 与更新时间 2021-05-25 不一致，provenance/superseded 为 null，无版本差异说明；本记录以当前 v2 正文为准。文中的绿卡数量、投资移民占比、新富人与中产阶级数量级均无出处，已在 unresolved_questions 标记为待外部核查。"
 },
 "212c4ae7": {
  "analysis": {
   "question_context": "提问者（Q001）问如何看待 4 月 30 日媒体在推特发布视频、犀利概括中美对疫情的态度。作者没有直接评价该视频的具体内容，只用一句话给出关于“批评”质量的一般判断（正文未点名该视频，也未出现“疫情”“推特”等词）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "单句给出判断：质量最好的批评是骂到对方又惭愧又想笑的那种。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张质量最好的批评是骂到对方又惭愧又想笑的那种。", "evidence": ["E1"]}
   ],
   "argument_steps": [
    "全文只有一句判断，没有定义、前提、理由、例证或反驳；也未对提问中提到的推特视频作任何评价。"
   ],
   "concept_usage": [
    {"term": "批评", "meaning": "本文中指标对他人（未指明对象）的指责或评论行为，作者关心的是其质量高低。", "evidence": "P001", "ambiguity": "未界定“批评”的场合、对象与边界，也未说明与“骂”的关系。"},
    {"term": "又惭愧又想笑", "meaning": "作者给出的最高质量标准：既让对方承认被说中（惭愧），又因其方式而不至于翻脸（想笑）。", "evidence": "P001", "ambiguity": "两个词均未定义，也没有例子或判据；此处“惭愧／想笑”的解释属读者转述，非作者原文定义。"}
   ],
   "examples_and_targets": [
    "提问者提到的“4 月 30 日媒体在推特发布视频，犀利概括了中美对疫情的态度”（Q001）：属提问者语境，作者正文未提及，仅能作为本篇的写作缘起。",
    "“骂到”（P001）：口语化的修辞用语，用来说明批评的方式而非具体批评对象。"
   ],
   "conditions": [
    "文中未说明适用条件、对象、场合或关系；判断以格言形式给出，未加“如果”“通常”等限定，也未声明例外。"
   ],
   "rhetoric_and_tone": "格言式单句成文，口语、简短、带调侃意味（“骂到对方又惭愧又想笑那种”）；结尾用“那种”收束，语气随意。没有展开论证，也没有对提问对象表态。",
   "unresolved_questions": [
    "正文未提及提问中的推特视频及其内容，作者是否在评价该视频只能由语境推测，文中无明示。",
    "“又惭愧又想笑”的具体判据、适用对象、场合与限度（例如是否包括讽刺、羞辱、攻击性言辞）文中均未说明。",
    "该句是一般性标准还是针对提问事件的评论，主体与所指对象不明。",
    "发布时间 2020-05-03 与更新时间 2021-05-25 不同，语料 provenance／superseded 均为 null，无版本差异说明；本记录以当前 v2 文本为准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "质量最好的批评是骂到对方又惭愧又想笑那种。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["传播与舆论", "修辞与批评方法"],
   "issue_candidates": ["批评的方式与效果", "中美疫情舆论回应"],
   "text_function_candidates": ["短评", "格言式回答"],
   "object_candidates": ["推特", "媒体视频（仅见于提问）", "中美疫情（仅见于提问）"],
   "working_keywords": ["批评", "惭愧", "想笑", "犀利"]
  },
  "notes": "本篇无图片节点，正文仅 21 字（UTF-16），lexical 只有一个 paragraph 节点，无列表、引用块或标题结构；正文与 brief 内容一致，正文为权威。提问中提到的“4 月 30 日媒体在推特发布视频”属外部事实，需外部核查；作者未在正文中评价该视频。发布时间 2020-05-03 与更新时间 2021-05-25 不一致，语料未给版本差异说明。"
 },
 "8561dd6b": {
  "analysis": {
   "question_context": "提问者（Q001）问：是不是大部分女性对科学技术、哲学、政治、历史等知识不感兴趣？如果是，原因是什么。作者没有先确认该前提是否成立，直接以“因为”给出原因：女性不喜欢“强奸”这种勾当；随后在末段把男性对这些知识的追逐动机描述为“秀精神肌肉 + 软‘强奸适应性’测试”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "直接给出原因：女性不喜欢“强奸”这种勾当，并列肉体／精神、主动／被动两种情形。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "语气转折：表示要把话说透。", "role": "transition"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "把男性对知识的追逐解释为秀精神肌肉与“强奸适应性”测试，而非对事实的好奇。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把女性对科学技术、哲学、政治、历史等知识不感兴趣的原因归为：女性不喜欢“强奸”这种勾当，不分肉体上还是精神上、主动还是被动。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称男生不像女生那样清楚自己在干什么：他们对这些知识的追逐绝大部分不是对事实有好奇，而是在秀精神肌肉并做软“强奸适应性”测试。", "evidence": ["E4"]}
   ],
   "argument_steps": [
    "以“因为”开头直接作答，未先论证或确认“大部分女性不感兴趣”这一前提。",
    "用带引号的“强奸”作为比喻性命名，并以“不管是肉体上的，还是精神上的”“不管是主动，还是被动”作全称式对举扩展其覆盖范围。",
    "以“好吧，非要把话说透啊……”表示将给出更直白的版本，构成语气转折。",
    "末段把男性的求知动机重新描述为“秀精神肌肉 + 软‘强奸适应性’测试”，作为对提问的进一步解释，未给例证或依据。"
   ],
   "concept_usage": [
    {"term": "“强奸”（带引号）", "meaning": "并非法律意义上的性侵指控，而是借喻强制、侵入性的知识施加或精神支配；作者把它扩展到“精神上的”和“被动的”情形。", "evidence": "P001", "ambiguity": "作者未界定该比喻的边界；“肉体上的／精神上的”“主动／被动”也未分别说明，含义不确定。"},
    {"term": "秀精神肌肉", "meaning": "口语比喻，指以展示智力或优越感为目的的行为，与“对事实有好奇”相对。", "evidence": "P005", "ambiguity": "未定义，也未说明如何与真实求知区分。"},
    {"term": "软“强奸适应性”测试", "meaning": "作者自造短语，用于描述男性在知识话题上的行为，指对精神侵入的适应或耐受测试。", "evidence": "P005", "ambiguity": "全文未定义，加引号表示借用或临时命名，含义高度不确定。"},
    {"term": "不感兴趣", "meaning": "沿用提问者的说法，指对科学技术、哲学、政治、历史等知识缺乏兴趣；作者未对其重新定义或量化。", "evidence": "Q001", "ambiguity": "“大部分”“感兴趣”均无范围与标准，作者也未回应其实证依据。"}
   ],
   "examples_and_targets": [
    "科学技术、哲学、政治、历史等知识（Q001）：提问者列举的范围，作者未逐项区分。",
    "女性／男生们（P001、P005）：作为被解释的群体，属概括性对举；作者未给范围、样本或例外。",
    "“强奸”（P001）与“秀精神肌肉”“软‘强奸适应性’测试”（P005）：作者的比喻与自造用语，作为解释框架而非经验证据。"
   ],
   "conditions": [
    "正文未给适用条件或限定词；提问中的“大部分”“如果是”等条件未被作者接续，作者直接给出原因。",
    "“不管是……还是……”为全称式对举，但未说明范围与例外。",
    "末段以“男生们”“绝大部分”作群体概括，未说明依据与适用边界。"
   ],
   "rhetoric_and_tone": "极简、挑衅式、口语化。首句用“因为”直答，紧接两组“不管是……还是……”排比；“好吧，非要把话说透啊……”是自问自答式转折，带反讽与不耐烦。末段用“秀精神肌肉”“软‘强奸适应性’测试”等比喻与自造词，把男性的求知动机整体化，语气调侃而绝对。",
   "unresolved_questions": [
    "作者未回应提问的前提“是不是大部分女性对……不感兴趣”本身是否成立，也未给数据、经验依据或反例。",
    "“强奸”的比喻义与“软‘强奸适应性’测试”的确切含义文中未定义，可能严重影响解释，属需谨慎处理的关键歧义。",
    "末段把男性的求知动机整体化（“男生们”“绝大部分”），未给范围、例外或依据，也无法确定是否包含作者自身的经验表述。",
    "正文未区分科学技术、哲学、政治、历史等不同知识领域，问题中的分类被整体处理。",
    "发布时间 2020-05-03 与更新时间 2021-07-13 不同，语料 provenance／superseded 均为 null，无版本差异说明；本记录以当前 v2 文本为准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "因为女性不喜欢“强奸”这种勾当。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不管是肉体上的，还是精神上的，", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "不管是主动，还是被动。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "那绝大部分不是对事实有好奇，而是在秀精神肌肉 + 软“强奸适应性”测试。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别与社会心理", "知识兴趣与动机", "言论风格评论"],
   "issue_candidates": ["女性对科学／哲学／政治／历史的兴趣差异", "求知动机与炫耀性讨论", "性别群体概括"],
   "text_function_candidates": ["答疑", "短评", "讽刺式回应"],
   "object_candidates": ["女性", "男生们", "科学技术、哲学、政治、历史（知识领域）"],
   "working_keywords": ["不感兴趣", "强奸", "精神肌肉", "适应性测试", "求知动机"]
  },
  "notes": "本篇无图片节点，正文 117 字（UTF-16），5 个段落全部读完；brief 内容与正文前四段基本重复，正文为权威。正文以性别群体作概括并含“强奸”借喻，本记录只作中性转述与归属标注，不作价值判断，也不把提问者的前提算作作者立场。作者未确认问题前提，只给出原因；关键比喻词未定义，已在 unresolved_questions 标记。发布时间 2020-05-03 与更新时间 2021-07-13 不一致，语料未给版本差异说明。"
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
