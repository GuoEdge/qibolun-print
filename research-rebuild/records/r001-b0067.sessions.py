# -*- coding: utf-8 -*-
"""批次 r001-b0067 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0067.sessions.py            # 写 out/r001-b0067.out.jsonl
  python3 records/r001-b0067.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0067"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0067.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "ff132074": {
  "analysis": {
   "question_context": "知乎提问（Q001）问如何看待特朗普称如果中方在某些地方不正确对待美国，他必定会让中美「脱钩」。提问引述的是特朗普的威胁性表态，属提问者转述，不得自动归给作者。作者未评价该表态真假，直接转向中美双方各自的脱钩动作与结局推演。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "现状对照：美国喊脱钩口号，中国在动手做脱钩准备。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "结局推测：准备完成的中国可能反过来以脱钩威慑美国。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国喊了很多脱钩口号，而中国在实际做脱钩的准备。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "最终结局有可能是反转的：做完了准备的中国将拿脱钩来威慑美国。", "evidence": ["E2"]}
   ],
   "argument_steps": ["前提/观察对照：美国喊脱钩口号、中国做脱钩准备（P001）。", "推测（未给中间论证）：做完准备的中国反过来以脱钩威慑美国（P002）。"],
   "concept_usage": [
    {"term": "脱钩", "meaning": "中美之间联系的人为切断；本篇既指美国口头施压的口号，也被设想为中国可反向使用的威慑手段。", "evidence": "P001", "ambiguity": "未界定脱钩范围（贸易、技术或全面），也未说明具体措施。"},
    {"term": "威慑", "meaning": "以脱钩作为施压手段，反向对美国施压。", "evidence": "P002", "ambiguity": "未说明威慑机制与作用对象。"}
   ],
   "examples_and_targets": ["美国（作者描述其喊脱钩口号的行为主体）", "中国（作者描述其在做脱钩准备的行为主体）", "特朗普（提问者引述的表态来源；作者正文未点名、未评价）", "「脱钩」口号（作者转述的现象，未给具体出处）"],
   "conditions": ["结论以「倒有可能」标记为可能性而非必然。", "推演以中国「做完了准备」为条件。", "未说明时间尺度、脱钩领域与判断依据。"],
   "rhetoric_and_tone": "全文两句，极简。先以「美国喊／中国做」构成对照，再翻转预期（「倒有可能」）；语气克制、近乎格言，含轻微反讽，无数据与引文。",
   "unresolved_questions": ["「中国却在动手做脱钩的准备」的具体所指（领域、措施、时间）正文未说明，属待外部核查的事实性判断。", "「拿脱钩来威慑美国」的机制与目标未说明。", "作者未直接回应提问所引特朗普表态的真假与可行性。", "正文极短，与提问之间无完整论证链。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "美国喊了很多脱钩的口号，中国却在动手做脱钩的准备。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "最后的结局，倒有可能是做完了准备的中国要拿脱钩来威慑美国。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系/中美关系", "经济与贸易政策"],
   "issue_candidates": ["中美脱钩", "威慑策略", "政策口号与实际准备"],
   "text_function_candidates": ["短评", "预测性评论", "答疑（知乎回答）"],
   "object_candidates": ["美国", "中国", "特朗普"],
   "working_keywords": ["脱钩", "威慑", "准备"]
  },
  "notes": "正文仅55字（P001—P002），无图片节点，lexical 与正文段数一致（2段）。首句关于「中国在做脱钩准备」是作者的事实性判断但无出处，登记为待外部核查；第二句为可能性推测，按 hypothetical 记录，未当作断言。"
 },
 "ac580308": {
  "analysis": {
   "question_context": "知乎提问（Q001）问「长生不老是完全不可能吗？」属提问者语境。作者开篇声明「换一个角度」，不直接判定生理永生能否实现，而是假设生理意义上的长生不死已经实现，转从记忆容量、运算能力与人格连续性追问「真实意义上」的永生是否可能，并逐一反驳替代方案（记忆简略化、忘了也无妨、意识上传与硬件改造）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "换角度并设定反事实前提：假设生理长生不死已实现，问题转为记忆能否无限扩展。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "记忆构成人格基底；删改记忆即改变性格、关系与决策影响。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "容量有限推理：活到数百年时回忆稀薄，人格崩溃、自我认知解体。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "替代路线（只留最近记忆）使前五百年的你等于已死，并反问这种永生的意义。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020"], "summary": "再推一步假设可扩容，仍受「运存」限制：不能同时处理的资料无实际意义。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026", "P027"], "summary": "运算速度与能量散热约束：算力无限也须舍弃大部分数据与算力。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "结论：思维机制本身决定真实永生不可能（非新陈代谢或端粒）；劝人拥抱死亡。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "反驳「长时记忆可令人满意地简略化」：记忆须靠大量细节背书，断裂威胁具摧毁性。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048"], "summary": "两例：三个月失忆者须靠他人讲述确认自己；街上被陌生人认出却毫无印象。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053"], "summary": "高寿者断裂线增多，如被蛀空的小说；有字数上限则结局只能是乱码。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P054", "P055", "P056"], "summary": "退一步假设接受自己记笔记复习的「笔记重生机制」；P056 为单句插入（结构未覆盖）。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065"], "summary": "以「三万小时」上限反驳「忘了也无妨」：寿命越长越必然走向痴呆。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P066", "P067"], "summary": "反问增强大脑手术后醒来的还是不是你；引出「真实案例」。", "role": "transition"},
    {"unit_id": "U014", "paragraph_refs": ["P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081"], "summary": "以藏传佛教活佛转世为已实现的「永生」案例（含双转世），并推论真永生者迟早进入该循环。", "role": "example"},
    {"unit_id": "U015", "paragraph_refs": ["P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094"], "summary": "反驳意识上传/外挂/硬件改造：意识与硬件耦合，改变容器即改变内容。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基本记忆严格构成人格基底；若把记忆完全移植到新载体，重新点亮瞬间的新副本在精神上就是你。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "直接删除部分伤痛记忆足以改变性格；删除对某些关系的记忆，这些要素对决策的影响也等效消失。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生理活动可无限延续，而记忆「硬盘」容量有限，二者构成矛盾。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "在记忆上限只能装一百年记录的假设下，活到六百年时故事线过于稀薄，人格会崩溃、自我认知会解体。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若走只留最后一百年连贯记忆的路线，前五百年记忆被洗掉，那五百年的你其实已经死掉。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "反问：这样的永生的确切意义是什么。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不能同时被处理的资料，即使登记在仓库里也没有实际意义（以计算机「运存」为类比）。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "运算速度、能量与散热构成约束：即使算力无限，只要不想变成核动力附属设施，终究要舍去大部分数据与算力。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是思维机制本身最终决定人无法在真实意义上永生，而不是新陈代谢或端粒限制。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应停止幻想永生、认真拥抱死亡并感谢它，因为死亡使人免于前述两难（承前文「死神救了你的命」）。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的观点：长时记忆可以令人满意地简略化；现在就不记得一周前或小时候的事也没觉得有问题。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "记忆与幻觉的本质区别在于记忆有大量其他细节作辅助背书，而这些细节靠极复杂的系统性关联保证。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被明确感知到的记忆断裂威胁是摧毁性的；不能把人生经历用一根时间线连贯起来就会沿空白线自我断裂。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在容量上限约束下，最终结局只会是无法再总结出中心思想的乱码，没有第二种结局。", "evidence": ["E20", "E21"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "以三万小时为记忆上限推算：寿命越长越必然走向痴呆，活到480年必然成为老年痴呆症患者。", "evidence": ["E22", "E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "反问：做完「增强大脑」手术、在手术台上醒过来的这个人还是你吗。", "evidence": ["E24"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按「忘了不要紧」的标准，藏传佛教的活佛已经算是「永生」的，是前述「失忆也可接受」主张的「离散数学版」。", "evidence": ["E25", "E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若真的永生，或迟或早都将进入永远反复循环的「活佛机制」；哪天放弃学习就开始失去原有身份。", "evidence": ["E27", "E28"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的意识不能无损地与硬件基础分离；作者称这恰是人工智能无法意识到自身存在的原因。", "evidence": ["E29"]},
    {"claim_id": "C020", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "改变容器就是改变内容；「硬件改造」本身就是实质意义上的人格切换，即使不是根本不通，也远不如云盘拷贝那么简单。", "evidence": ["E30", "E31"]}
   ],
   "argument_steps": ["方法声明：换角度，先假设生理长生不死已实现（P001—P002）。", "定义性前提：基本记忆构成人格基底，记忆移植=精神上的你（P004）。", "理由：删改记忆即可改变性格与关系影响（P005）。", "矛盾：生理无限 vs 容量的有限（P006—P008）。", "推演：六百年记忆只留一百年 → 人格崩溃（P009—P010）；只留最近一百年 → 前五百年之你已死（P011—P013）。", "反问永生意义（P014）。", "让步推进：假设可扩容（P015—P016），但运存有限（P018—P020）。", "再限制：时钟频率、能量散热（P021—P024）→ 算力无限仍须舍弃（P025—P026）；硬接核动力成囚徒（P027）。", "结论：思维机制决定真实永生不可能（P028）；劝诫拥抱死亡（P029—P030）。", "反驳「记忆可简略化」：细节背书与系统性关联（P032—P037）；断裂摧毁性（P041）。", "例证：三个月失忆须靠他人写入（P042—P045）；陌生人相认（P046—P048）。", "比喻收束：蛀空的小说与字数上限 → 乱码（P049—P053）。", "让步：笔记重生机制（P054—P055）。", "反驳「忘了也无妨」：三万小时上限（P057—P065）。", "反问手术后是否还是你（P066）。", "案例：活佛转世机制（P068—P081）→ 真永生者迟早进入该循环（P079—P081）。", "反驳技术方案：意识不可无损分离、改容器即改内容（P082—P094）。"],
   "concept_usage": [
    {"term": "人格基底／人格", "meaning": "由基本记忆严格构成；记忆断裂或删改会改变人格乃至使其解体。", "evidence": "P004", "ambiguity": "未给出人格的严格定义，也未说明基底之外是否还有别的成分。"},
    {"term": "硬盘（记忆容量）", "meaning": "比喻记忆存储总量；作者假定其有限，并以「一百年记录」为假设极限。", "evidence": "P006", "ambiguity": "「一百年」为作者设定的假设值，未说明依据。"},
    {"term": "运存", "meaning": "比喻能同时调取、处理的资料量；作者认为它限制记忆的实际可用性。", "evidence": "P019", "ambiguity": "未说明运存能否扩容；后文以「也可以无限扩展吗」反问。"},
    {"term": "算力／时钟频率", "meaning": "运算速度，作者把能量与散热功率一并计入其约束。", "evidence": "P021", "ambiguity": "未给数量级或可行性依据。"},
    {"term": "意识", "meaning": "与硬件基础耦合、不可无损分离的产物；失明与能看见者的意识存在重大区别。", "evidence": "P084", "ambiguity": "未定义意识的判定标准。"},
    {"term": "容器", "meaning": "大脑作为意识的容器，为内容物定制，并反过来影响内容本身。", "evidence": "P087", "ambiguity": "「为内容物定制」的机制未说明。"},
    {"term": "永生／长生不死", "meaning": "作者区分两层：生理意义上的延续，与「真实意义上」的永生（人格连续性）。", "evidence": "P028", "ambiguity": "两层区分是本文论证的关键，但作者未正式定义。"},
    {"term": "活佛机制", "meaning": "作者用语：靠反复学习重新记起身份、循环往复的模式，作者称其为永生者迟早进入的循环。", "evidence": "P077", "ambiguity": "该命名出自作者，非宗教或学术术语。"}
   ],
   "examples_and_targets": ["红色自行车（P036—P037）：作者例证，说明记忆需关联细节背书。", "三个月失忆＋墨镜、奶茶收据、衬衫、踩点笔记（P042—P044）：作者例证，说明空白记忆可被他人写入。", "街上认出你却毫无印象的人（P046—P047）：作者例证兼反问材料。", "被蛀空的小说、一百万字上限（P050—P052）：作者类比。", "三万小时电影（P059—P065）：作者换算例证。", "藏传佛教活佛转世、转世灵童、遗物挑拣、双转世机制（P068—P075）：作者称为「真实的案例」的宗教制度叙述，未注明来源。", "核潜艇改造的深海监狱与环保主义者抗议（P027）：夸张修辞材料。", "爱因斯坦的脑（P089）：作者类比。", "双目失明者与能看见的人（P085）：作者类比例证。", "人工智能无法意识到自身存在（P084）：作者断言，用作旁证，待外部核查。", "端粒限制、新陈代谢（P028）：作者明确排除的解释。", "「意识上传／外挂／大幅改造人脑」主张（P082）：被反驳对象。", "「长时记忆可以令人满意的简略化」「忘了也无妨」论者（P032、P058、P067）：被反驳对象。"],
   "conditions": ["全篇以反事实前提展开：「假设你在生理意义上的长生不死已经确实实现了」（P002）。", "关键数值为作者假设：「假设我们认定它的极限能装一百年的记录」（P007）；「三万小时」为设定的等效上限（P059）。", "运算约束以「如果你不打算把自己改造成核动力供电和海水散热」为条件（P024）。", "推论对象限于生理延续的永生个体；作者以「恐怕」「怕是要」「必然」区分强度。", "结论「无法真实意义上永生」限定在思维机制层面，作者明确排除新陈代谢与端粒（P028）。", "硬件改造方案留有让步：「即使不是根本不通，也远不如人们想象的如云盘拷贝那么简单」（P093）。"],
   "rhetoric_and_tone": "第二人称「你」贯穿，思想实验式层层推进（「再往前推一步」「再退一步」「现在问题来了」）；密集计算机类比（硬盘／运存／时钟频率／拷贝粘贴／云盘）；反问句多（P014、P017、P038、P045、P048、P066）；讽刺夸张（「深海铁棺材上的一块赘生物」「对方怕是孙子都生出来了」「环保主义者无休止的围着你」）；夹入英文短句「Another poetic irony.」；收束为训诫语气（「停止幻想永生，认真的拥抱你的死亡，并且感谢它吧」）；标题用「脑残」称呼论辩对手，带情绪色彩。",
   "unresolved_questions": ["标题「长生不死的脑残」具体指谁，正文未点名。", "活佛转世程序（P070—P075）的叙述无来源，属待外部核查的宗教制度描述。", "「人工智能无法意识到自身的存在」的因果断言（P084）无出处，待外部核查。", "「一百年记录」「三万小时」等记忆上限为作者假设值，正文未说明依据。", "P056「永生是否是一种酷刑？」在 lexical 结构中未被覆盖（lexical 96 段 vs 正文 94 段），疑为平台话题标签或插入句，归属不明，需人工复核。", "P004「记忆移植后副本在精神上就是你」与 P089「改变容器，就是改变内容」之间是否构成张力，作者未处理。", "全篇事实性断言（脑科学、AI 意识）均无引文支撑，需外部核查。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "如果换一个新鲜的载体，把你的记忆完全移植过去", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "在重新点亮的瞬间，这个新的副本在精神上就是你。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "直接删除你的部分伤痛记忆，足以改变你的性格。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "你的生理活动是无限延续的，你的“硬盘”却是容量有限的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "你的人生回忆也怕要把你逼疯——故事线过于稀薄", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "你的人格会崩溃，自我认知会解体，变成若干个人格碎片的杂合体。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "那五百年的你其实已经死掉了。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "这样的永生的确切意义是什么呢？", "relation": "context"},
    {"key": "E9", "paragraph_id": "P019", "quote": "不能同时放在办公桌上的资料，即使确实有登记在仓库里，也没有实际意义。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P024", "quote": "你的运算速度恐怕不足以在保持几百年的记忆能充分有效运用的前提下保持正常社交所需要的语速。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P025", "quote": "就算你的算力无限，只要你不想化身为核电厂附属设施，你终究还是要舍去大部分的数据和算力。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P028", "quote": "实际上是你的思维机制本身最终决定了你无法在真实意义上永生，不是新陈代谢，也不是所谓的端粒限制。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P029", "quote": "停止幻想永生，认真的拥抱你的死亡，并且感谢它吧", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P030", "quote": "其实是死神救了你的命。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P032", "quote": "我发现很多人都觉得“长时记忆可以令人满意的简略化”", "relation": "contradicts"},
    {"key": "E16", "paragraph_id": "P058", "quote": "有一种观点认为“我现在就不记得一周前/小时候的事，我现在就没觉得有问题啊”。", "relation": "contradicts"},
    {"key": "E17", "paragraph_id": "P034", "quote": "就在于记忆会有很多其他细节作为辅助背书", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P037", "quote": "你都将无法将这个念头作为你的记忆来对待", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P041", "quote": "被明确感知到的记忆断裂的威胁是摧毁性的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P052", "quote": "最终的结局只会是变成一片不知所云、无法再总结出任何中心思想的乱码。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P053", "quote": "没有第二种结局可言。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P065", "quote": "总结480年你必然要成为老年痴呆症患者。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P059", "quote": "我们假设你活到八十岁，能记住的内容约等于是三万小时的电影。", "relation": "context"},
    {"key": "E24", "paragraph_id": "P066", "quote": "动完这手术，你确信在手术台上醒过来的这个人还是你吗？", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P068", "quote": "按照这个“忘了不要紧”的标准，世界上已经有人是“永生”的了。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P077", "quote": "这其实就是你们前面再三表示“就算失忆也完全可以接受”的一个“离散数学版”。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P079", "quote": "或迟或早，你都将进入永远反复循环的“活佛机制”。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P081", "quote": "哪天放弃学习，哪天你就会开始失去原有身份", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P084", "quote": "人的意识是不能无损的与硬件基础分离的", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P089", "quote": "改变容器，就是改变内容。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P093", "quote": "“硬件改造”本身就是实质意义上的人格切换", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P070", "quote": "活佛转世的基本程序，就是在前任死亡时留下线索", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心智哲学/人格同一性", "认知科学与记忆", "科幻思想实验评论", "宗教制度观察（藏传佛教活佛转世）"],
   "issue_candidates": ["长生不死的可行性", "记忆容量与人格连续性", "意识上传/硬件改造", "记忆与身份认同", "死亡的意义"],
   "text_function_candidates": ["思想实验式论证", "批评/反驳", "答疑（知乎回答）", "带训诫收束的评论"],
   "object_candidates": ["藏传佛教活佛/转世灵童", "人工智能", "爱因斯坦", "计算机（硬盘/运存）"],
   "working_keywords": ["长生不死", "人格基底", "记忆容量", "运存", "时钟频率", "端粒", "意识上传", "活佛机制", "三万小时"]
  },
  "notes": "①本篇 lexical 与正文段数不一致（lexical 报 96 段，正文 94 段），P056「永生是否是一种酷刑？」被阅读包标为「lexical未覆盖片段」，疑为平台话题标签或插入句，归属待人工复核，故未据其立论。②正文多处事实性断言（活佛转世制度、人工智能无自我意识、脑科学判断）无出处，登记为待外部核查，未当作已证实事实。③无图片节点。④对手观点（P032、P058、P067）与被反驳的技术方案（P082）均按 opponent_view/opponent 记录，未归给作者。"
 },
 "5acee43d": {
  "analysis": {
   "question_context": "知乎提问（Q001）问如何看待大陆唯一一台7nm光刻机被抵押、武汉弘芯千亿级芯片项目停摆、新员工延迟入职。该事件是提问者提出的负面事实，作者既未核实也未否认，而是把它放进「举国体制补贴—骗补—事后追责尺度」与「受控竞争 vs 自由竞争效率」的框架中，主张此类损失应被看作「正常失败」。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "政策奖励刺激的举国体制易生骗补（痼疾）；事后追责作威慑的尺度微妙难掌握。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "理由：政策颁布时缺专业执行者、只能靠非专业办事人，故难以事后成败反推罪责。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "中国基本策略框架对早期混乱有一定宽容；不存在「既要又要」，须接受仍会出现天文数字级错误决策。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "以经济体量（14万亿美元/近100万亿人民币）说明政策尺度的巨额代价：百亿买一两句话的教训不罕见。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "父母念叨在外吃饭/打车的类比，指向「浪费钱」心态，并以反问指出这种心态并不导向「顿顿在家吃」。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "大众同类心态被放大成百上千倍；但政策层面数字没那么可怕，几个亿属正常试错成本，摸实底可能要上百亿。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020"], "summary": "行动主张：要总结经验教训但不必大惊小怪，也不要主张「自由市场机制更有效率」。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022", "P023"], "summary": "反驳：自由市场同样有大量试错成本，灭失财富未必更小；那钱本可以是你的，只是让给了风险承担者。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028"], "summary": "两种体制总效用与总成本一样但「痛感」不同；资本主义民众享受无痛也不能分享成果；作者姑且算作势均力敌。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033"], "summary": "真正的问题是受控竞争是否效率更低；计划经济还存在「计划竞争」模式，作者并反驳「计划经济优势=消灭输家」的旧理解。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038"], "summary": "胜率推理：受控竞争胜率非零；若达一半一半总体不弱于自然竞争；若能积累识别适配场景的知识，三成胜率也可改观总体胜负。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P039", "P040", "P041", "P042"], "summary": "中国体制优势：不预设纯自由竞争必然更优，「有时候受控竞争更好」已由两弹一星、高铁、北斗、J20 等案例竖立。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P043", "P044"], "summary": "决策机制与社会所有制形式持续适配该治理模式，这才是两种制度竞争的真正前线。", "role": "conclusion"},
    {"unit_id": "U014", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049"], "summary": "弘芯式问题被视为战术层面的「正常失败」；但作者强调这不等于不干预不总结，并以侦察连受损的类比收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用政策奖励来刺激的举国体制很容易造成骗补现象，这是一个痼疾。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "事后追究骗补理论上可作威慑，但这个手段的尺度非常微妙、很不容易掌握。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "政策颁布时极端缺乏专业执行者、只能依赖半专业或非专业办事人，因此很难用事后成败反推罪责；因战事不顺而拿「不教民」问罪在组织伦理上无法服众。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国做事的基本策略框架实际上对早期混乱做了一定宽容，早期允许百花齐放、允许犯错误。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现实不是童话，瞻前顾后与大量错误浪费之间没有「黄金分割点」；可以尽力避免，但必须接受仍会产生天文数字级的错误决策。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国14万亿美元、近100万亿人民币的经济体量意味着政策尺度上挪一毫米、改一个词、少写一个字都是巨大窟窿；花1亿、10亿乃至100亿买一两句话的教训实非罕见。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在政策层面（尤其全国范围、数年乃至更长时间跨度的决策），这些数字没有一般人看来那么可怕；几个亿的损失相对该行业一年2.1万亿人民币（3000亿美元）进口额属正常试错成本，远未触及红线。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "光是摸清「哪个班子靠谱、哪个小组有真实力、哪个机制能出成果」的实底，可能都需要上百亿人民币的基本成本。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要总结经验教训，但不必大惊小怪，也不要主张「自由市场机制更有效率」。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自由市场机制一样会有大量试错成本，其灭失财富的总规模未必比几百亿几千亿人民币小。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "并不是只有有钱人才是股民；该机制使财富分配中风险分担要素比重变大，风险承担者因而分走极大比例的利润。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两种体制最终总效用一样、总成本一样，但「痛感」不一样：资本主义民众因「这是别人的钱」而享受无痛，也因此不能在成功之后分享成果（中国的国有资产则承担国计民生使命）。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C013", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的观点：计划经济的长处是可以有效消灭市场竞争带来的输家投入打水漂问题（「我只要一家做研发，就不存在输家了」）；作者称这是对计划经济的狭隘理解。", "evidence": ["E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "计划经济完全可以计划竞争：存在「指定体制内外数家机构彼此竞争」的模式，引入体制外竞争者同样可以是计划经济手段，没有原则性理论障碍。", "evidence": ["E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "受规划的竞争其胜率至少不会是百分之零；一定会有某些情况下人类规划的竞争比纯自由竞争更有效率。", "evidence": ["E27", "E28"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果受控竞争的胜率可以达到一半一半，那么受控竞争模式在总体上并不弱于自然竞争模式。", "evidence": ["E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问提出：如果关于「判断什么样的事情适合使用受控竞争模式」的知识和经验能随时间积累提高，那么即使全部胜率只有三成、但知道哪三成赌局比较会赢，总体胜负就会改观（作者以此支持受控竞争）。", "evidence": ["E30", "E31"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国体制存在一种意识形态上的限定规则，信奉纯自由竞争总是比受控竞争有效（作者对美国体制的概括）。", "evidence": ["E32"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国认为这事得两说（有的好、有的不好），处在既不迷信计划经济绝对比市场经济好、也不迷信自由竞争一定比计划经济好的状态，并把目光转向在实践中寻找和磨练识别尺度界限的理论与经验。", "evidence": ["E33", "E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「有时候受控竞争更好」这一认定已被牢牢竖立，因为存在两弹一星、高铁、北斗、J20 等实实在在的成功案例。", "evidence": ["E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国决策机制与社会所有制形式不断为该治理模式做适配，这才是现在两种制度竞争的真正前线。", "evidence": ["E36"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "类似武汉弘芯这样的问题会被视为需要管理和改进的「正常失败」，即被看作战术问题而不是战略问题。", "evidence": ["E37", "E38", "E39"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "现在的中国已是人类历史上修补政策漏洞最快的政治实体之一，可能仅有明治维新之日本、建国初期之美国可以媲美；其决策链路之短到了其他国家觉得难以接受的程度。", "evidence": ["E40"]}
   ],
   "argument_steps": ["提出痼疾：补贴刺激易生骗补，事后追责尺度微妙（P001—P002）。", "理由：执行者不专业 → 事后成败无法反推罪责（P003—P005）。", "转为策略说明：框架容忍早期混乱，不存在「既要又要」（P006—P007）。", "量级论证：经济体量与政策尺度的天文数字代价（P008—P009）。", "类比：父母念叨与「浪费钱」心态，反问其并不能导向顿顿在家吃（P010—P014）。", "转向政府决策：大众痛感被放大，但政策层面属正常试错成本（P015—P018）。", "行动要求：总结经验但不大惊小怪（P019—P020）。", "反驳自由市场优越论：其试错成本与分配后果（P021—P023）。", "对称性讨论：总效用/总成本相同而「痛感」不同，作者姑且算作对称（P024—P028）。", "重设问题：受控竞争是否更低效；提出「计划竞争」并反驳旧理解（P029—P033）。", "胜率推理与反问（P034—P038）。", "对比美国意识形态限定 vs 中国的「两说」与实践取向（P039—P042）。", "结论一：治理模式适配是竞争前线（P043—P044）。", "结论二：弘芯式损失属战术层面的「正常失败」，但不等于不干预不总结（P045—P049）。"],
   "concept_usage": [
    {"term": "骗补", "meaning": "以政策奖励刺激为动机的骗取补贴行为；作者称之为痼疾。", "evidence": "P001", "ambiguity": "未说明骗补的判定标准与规模。"},
    {"term": "举国体制", "meaning": "作者在本文限定为「用政策奖励来刺激的」体制。", "evidence": "P001", "ambiguity": "该限定用法窄于一般用法。"},
    {"term": "正常失败", "meaning": "被看作战术问题而非战略问题、需要管理和改进的失败。", "evidence": "P045", "ambiguity": "作者强调它不意味着不干预不总结（P046），但未给出「正常/非正常」的判定标准。"},
    {"term": "试错成本", "meaning": "行业变革努力中可接受的损失，以几个亿相对2.1万亿进口额衡量。", "evidence": "P017", "ambiguity": "「红线」的具体位置未说明。"},
    {"term": "受控竞争／计划竞争", "meaning": "由中央计划者设计的竞争，可指定体制内外数家机构彼此竞争以增强效率驱动。", "evidence": "P030", "ambiguity": "未说明其与「骗补」痼疾如何共存。"},
    {"term": "痛感", "meaning": "民众对国有资源投资损失的主观感受；作者用它区别两种体制的分配与分享后果。", "evidence": "P025", "ambiguity": "「痛感」为作者用语，非既有学术概念。"},
    {"term": "自由市场机制", "meaning": "纯自由竞争；作者承认其试错成本，同时指出其分配与成功分享的后果。", "evidence": "P021", "ambiguity": "未界定其边界与国别差异。"},
    {"term": "黄金分割点", "meaning": "作者否定存在瞻前顾后与大量错误浪费之间的最优点。", "evidence": "P007", "ambiguity": "未给出反驳该存在性的论证。"},
    {"term": "不教民", "meaning": "借《论语》语汇指未经训练的办事人／民众。", "evidence": "P004", "ambiguity": "作者以「以不教民战也罢了」化用原文，未标出处。"}
   ],
   "examples_and_targets": ["武汉弘芯千亿级芯片项目（提问者引出的事件；作者作为「正常失败」的实例，P045）", "父母念叨在外吃饭/打车（P010—P014）：作者类比。", "上汤娃娃菜58块、tmd（P013）：作者类比细节，含粗口引述。", "股民与风险承担者（P022—P023）：作者论证材料。", "高铁、北斗、三峡大坝、南水北调、中国电网（P027）：作者论据（国有资产承担国计民生使命）。", "两弹一星、高铁、北斗、J20（P041）：作者论据（受控竞争的成功案例）。", "2.1万亿人民币（3000亿美元）进口额（P017）：作者数据，待外部核查。", "14万亿美元/近100万亿人民币（P008）：作者数据，待外部核查。", "美国体制与「意识形态上的限定规则」（P039）：作者的对比对象。", "明治维新之日本、建国初期之美国（P046）：作者的参照类比。", "侦察连受损的检讨会（P048—P049）：作者类比。", "「自由市场机制更有效率」的主张（P020—P021）：被反驳对象。", "「计划经济优势=消灭输家」的旧理解（P031—P032）：被反驳对象。"],
   "conditions": ["分析前提是中国现有的经济体量与决策尺度（14万亿美元/近100万亿人民币，P008）。", "论断限定于「全国范围的、涉及到几年甚至更久的时间跨度的决策」（P016）。", "概率论证使用假设：「如果这胜率可以达到一半一半」（P036）、「即使我的全部胜率只有三成」（P038）。", "「正常失败」被限定为战术问题而非战略问题（P047），且作者明说它不意味着不干预、不总结和防范（P046）。", "关于美国体制的概括为作者表述，未给证据来源。", "文中经济数据与历史参照均无出处，登记为待外部核查。"],
   "rhetoric_and_tone": "政策辩护性论辩文，反问密集（P014、P049，另 P007、P015 含反问式表述）；大量市井类比（父母念叨、娃娃菜、ppt骗钱）与口语粗话引述（「要tmd58块」）；用「你」拉近读者；先承认问题存在（骗补是痼疾）再重新框定其性质，属让步后反驳的结构；对大众心态作解释性批评（「这不是天大的错误吗？」）；对本国政策亦承认漏洞并强调修补速度。",
   "unresolved_questions": ["文中经济数据（14万亿美元、近100万亿人民币、2.1万亿人民币进口额、3000亿美元）无出处，待外部核查。", "武汉弘芯事件的具体事实（光刻机抵押、停摆、延迟入职）作者未核实也未否认，本文只作体制层面的重新框定。", "「明治维新之日本、建国初期之美国」作为修补漏洞最快政体的参照缺乏指标与来源。", "前文承认骗补是痼疾，后文主张「计划竞争」可行，二者如何衔接（如何防止计划竞争中的骗补）正文未交代。", "「红线」的具体位置与「正常失败」的判定标准未说明。", "平台话题标签是否混入正文无法判定。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "用政策奖励来刺激的举国体制很容易造成骗补现象，这是一个痼疾。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "但其实这个手段的尺度非常微妙，很不容易掌握。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "不得不依赖有限的、半专业甚至非专业的办事人来推进这个过程。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "如过因为战事不顺还要拿不教民问罪，这在组织伦理上无法服众。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "于是很难用事后成败来“反推罪责”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "你会发现我们实际上是把早期的混乱做了一定宽容的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "并没有所谓的“黄金分割点”，你做不到“既要又要”。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "最后仍然不能阻止某些在一般大众在日常生活尺度觉得惊人的、荒谬的、天文数字的错误决策的产生和实施", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "中国的经济体量已经达到14万亿美元，近100万亿人民币。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "乃至100亿买一两句话的教训的事情，实非罕见。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "但实际上在政策层面，这些数字并没有一般看起来那么可怕", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "实际上属于正常的试错成本，远远没有触及红线。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "可能都需要上百亿人民币的基本成本。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "是要总结经验教训，但不必大惊小怪。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "也不要大叫“自由市场机制更有效率”。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "自由市场机制一样会有大量的试错成本", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "它们灭失掉的财富总规模，未必比这几百亿几千亿人民币规模小。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P022", "quote": "并不是只有有钱人才是股民", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "风险承担者分走了极大比例的利润。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P025", "quote": "最后达到的总效用一样、总成本一样，但“痛感”不一样。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P026", "quote": "因为失败固然“与你无关”，但对应的成功也只属于那些下了注的有钱人。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P027", "quote": "而是作为国有资产有承担国计民生使命的天然使命。", "relation": "context"},
    {"key": "E23", "paragraph_id": "P031", "quote": "以前人们一贯认为计划经济的优势是可以有效的消灭市场竞争带来的输家投入打水漂问题", "relation": "contradicts"},
    {"key": "E24", "paragraph_id": "P032", "quote": "这是对计划经济的狭隘理解，", "relation": "contradicts"},
    {"key": "E25", "paragraph_id": "P030", "quote": "它还存在一个“指定体制内外数家机构彼此竞争”的“计划竞争”模式。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P033", "quote": "计划经济完全可以计划竞争。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P035", "quote": "显然，这种赌博的胜率至少不会是百分之零。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "一定会有某些情况下人类规划的竞争比纯自由竞争更有效率。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "如果这胜率可以达到一半一半，那么受控竞争模式就在总体上并不弱于自然竞争模式。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "但如果我们关于“判断什么样的事情适合使用受控竞争模式”的知识和经验可以随着时间积累而提高呢？", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P038", "quote": "但我知道哪三成赌局我比较会赢，这总体的胜负会如何？", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P039", "quote": "美国的体制存在一种意识形态上的限定规则，信奉纯自由竞争总是比受控竞争有效。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P040", "quote": "但中国则认为这事得两说——有的好，有的不好。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P042", "quote": "中国处在一个既不迷信计划经济绝对比市场经济好、也不迷信自由竞争一定比计划经济好的状态", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P041", "quote": "因为的确存在两弹一星、高铁、北斗、J20……这些实实在在的成功案例。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P044", "quote": "这才是现在两种制度竞争的真正前线。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P045", "quote": "那么类似武汉弘芯这样的问题就自然会被视为需要管理和改进的正常失败。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P047", "quote": "是指这种失败会被看作战术问题，而不是战略问题。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P049", "quote": "难道指望一个侦察连都不受损的打赢一场战役吗？", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P046", "quote": "现在的中国已经是人类历史上修补政策漏洞最快的政治实体之一", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["产业政策/科技政策", "政治经济学（计划经济与市场竞争）", "公共财政与补贴治理"],
   "issue_candidates": ["骗补与事后追责", "举国体制的效率", "受控竞争 vs 自由竞争", "试错成本与公众感受", "芯片项目停摆"],
   "text_function_candidates": ["论辩", "政策辩护与解释", "答疑（知乎回答）", "评论"],
   "object_candidates": ["中国", "美国", "武汉弘芯", "日本（明治维新）", "美国（建国初期）"],
   "working_keywords": ["骗补", "举国体制", "正常失败", "试错成本", "计划竞争", "受控竞争", "痛感", "黄金分割点", "不教民"]
  },
  "notes": "无图片节点；lexical 与正文段数一致（49段）。文中经济数据（14万亿美元、近100万亿人民币、2.1万亿/3000亿美元）与历史参照（明治维新之日本、建国初期之美国）均无出处，登记为待外部核查，未当作已证实事实。作者对「自由市场更有效率」（P020—P021）与「计划经济优势=消灭输家」（P031—P032）两种观点均作反驳，按 opponent_view/opponent 记录。P013 引文含粗口「tmd」，为保持逐字一致原样保留。"
 },
 "48ab9554": {
  "analysis": {
   "question_context": "知乎提问（Q001）问马斯克用猪展示 Neuralink 脑机接口设备有哪些亮点和槽点、未来有望应用在人脑吗。提问属提问者语境。作者只回应「能否应用」这一支，先辨析「应用」的广义与狭义，再以「技术焦虑」和「意识安全」为据论证脑机接口在人脑上的应用会带来无法解决的心理与伦理问题。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "辨析「应用」：广义下（如手机砸核桃）答案当然是可以，狭义则难说。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "技术推广即应用者淘汰不应用者的过程；使用任何技术都必有「技术焦虑」这一底层成本。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "以转基因为例说明焦虑结构：可怕想象虽非现实但确实可能，故安全证明解除不了焦虑。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "牵涉大脑的技术更不可能幸免：上市应用后会出现大量幻听幻视幻痛并被归因于该技术，且受害者主张无法被有效推翻（反问）。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014"], "summary": "「意识安全」是核心问题：若不确信意识完全属于自己，效率提升就没有意义。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"], "summary": "结论：作者不认为马斯克能解决该问题，它甚至不属于人类有资格「解决」的问题——解决它必须修正人性。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "按广义的「应用」（如手机也能拿来砸核桃），问脑机接口能否应用于人脑，答案当然是「可以」。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若按狭义的「应用」来问，那就难说了。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何技术的推广过程，都是应用该技术的团体淘汰不应用该技术的团体的过程。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "使用任何技术，除经济收益因素外都一定有一个更基础的「技术焦虑」问题（技术对人类心理健康的挑战），这是技术应用的底层成本、必定要付出。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者刻画焦虑推论：转基因的可怕想象虽不是现实但的确是可能的；只要可能，「我」就很可能是不被承认的特殊受害者，而反对者很可能因巨大利益牵涉而绝不肯承认。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "该技术一旦上市销售、投入具体应用，很快会有大量幻听、幻视、幻痛甚至幻想问题涌现并被直接归因于这项技术；且因人类对脑科学认识肤浅模糊，受害者的主张根本无法有效推翻。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "反问：有什么办法可以证明这位自诉者是在撒谎，或者其感受其实与这个设备绝对无关。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "这涉及人的「意识安全」核心问题：如果我不能再确信我的意识完全属于我，而存在一个我控不了的缺口会引入无法预料的干扰甚至干预，那么这项技术提高点击鼠标效率就没有意义。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不认为马斯克能解决这个问题，并称这甚至都不属于人类有资格「解决」的问题。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "因为要解决这个问题必须修正人性；这种技术焦虑问题恐怕是人类所不能适应和解决的——适应和解决它要求人类变成另一种生物。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": ["定义辨析：区分「应用」的广义与狭义（P001—P003）。", "前提一：技术推广是团体间的淘汰过程（P004）。", "前提二：使用技术必有「技术焦虑」这一底层成本（P005）。", "例证：转基因的焦虑想象不因安全证明而消除（P006—P009）。", "推进：牵涉大脑的技术更不可能幸免；预测大规模归因事件并指出无法反驳自诉者（P010—P012）。", "核心论据：意识安全不可让渡，效率收益失去意义（P013—P014）。", "结论：该问题无法由马斯克或人类解决，因解决它要求修正人性（P015—P017）。"],
   "concept_usage": [
    {"term": "应用（广义/狭义）", "meaning": "广义指任何用途（如手机砸核桃），狭义指技术的实际落地使用；作者借此说明提问方式决定答案。", "evidence": "P002", "ambiguity": "作者未给出狭义「应用」的判定标准。"},
    {"term": "技术焦虑", "meaning": "技术对人类心理健康的挑战，作者称之为技术应用的「底层成本」。", "evidence": "P005", "ambiguity": "作者未给测量或界定方式；「底层成本」是其自造表述。"},
    {"term": "底层成本", "meaning": "必定要付出、无法回避的基础代价。", "evidence": "P005", "ambiguity": "与经济损失的关系未量化。"},
    {"term": "意识安全", "meaning": "意识是否完全属于自己、是否存在自己控制不了的缺口。", "evidence": "P013", "ambiguity": "作者未定义判据，只以「点击鼠标效率」作对照。"},
    {"term": "特殊受害者", "meaning": "焦虑想象中「我」所处的位置——不被承认的受害者。", "evidence": "P009", "ambiguity": "该表述出自作者对焦虑者心态的刻画，非作者自述立场。"},
    {"term": "淘汰", "meaning": "团体层面因是否采用技术而被淘汰（作者的全称断言）。", "evidence": "P004", "ambiguity": "未限定行业、时间与淘汰形式。"}
   ],
   "examples_and_targets": ["手机砸核桃（P002）：作者类比，用来说明广义「应用」。", "转基因技术与转基因作物（P007—P010）：作者例证（焦虑结构）。", "马斯克与 Neuralink 猪演示（提问者引出；P011、P015 为作者评论对象）。", "幻听、幻视、幻痛、幻想问题（P011）：作者预测会出现的现象。", "「自从安装了这些电极，我就没有停止过幻觉」（P012）：作者拟设的自诉者话语（引号内，正文未说明是否真实引述）。", "「赢得了全世界，却失去了自我」（P014）：作者反问中的修辞材料。", "人性（P016）：作者指认需要修正的对象。"],
   "conditions": ["论断以「应用」的广义/狭义区分为条件（P001—P003）。", "预测分两支：要么停留在研发阶段反复融资，要么上市销售投入具体应用（P011）。", "焦虑推论以「只要是可能的」为前提（P009）。", "「意识安全」论断以「如果我不能确信我的意识完全属于我」为条件（P013）。", "结论用「恐怕」限定人类能否适应解决，并把出路设为「变成另一种生物」（P017）。"],
   "rhetoric_and_tone": "以词义辨析开场；反问密集（P012、P013末、P014）；以「你们」指涉可能的反对者并将其动机归为利益牵涉；由转基因类比递进到脑机接口；对技术乐观叙事持批评态度，末句以「要求人类变成另一种生物」作耸动式收束；无数据与文献引用。",
   "unresolved_questions": ["「技术焦虑是必定要付出的底层成本」这一普遍断言未给证据来源，待外部核查。", "「现有的转基因作物被现有的手段证明是安全的」未给出处，待外部核查。", "P012 引号内的自诉者话语是作者拟设示例还是真实引述，正文未说明。", "「必须修正人性」「人类变成另一种生物」的具体含义与可行性未说明。", "提问中的「亮点和槽点」部分作者未涉及，仅回应了能否应用与人脑应用的顾虑。", "平台话题标签是否混入正文无法判定。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "手机也可以拿来砸核桃，也可以算“应用”", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "但是如果算狭义，那就难说了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "任何技术的推广过程，都是应用该技术的团体淘汰不应用该技术的团体的过程。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "都一定会有一个更基础的“技术焦虑”问题——就是技术对人类心理健康的挑战。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "因为那些天马行空的可怕想象尽管不是现实的，但是的确是可能的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "那么具体的“我”就很可能是一名不被承认的特殊受害者", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "你们很可能只是因为巨大的利益牵涉而绝不肯承认。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "一旦上市销售投入具体应用，很快就会有大量的幻听、幻视、幻痛甚至幻想问题涌现", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "受害者的主张根本无法有效的推翻。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "用什么办法可以证明这位自诉者是在撒谎", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "如果我不能再确信我的意识是完全属于我的", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "赢得了全世界，却失去了自我，赢得全世界的意义何在呢？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "我不认为马斯克能解决这个问题", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "因为要解决这个问题，必须修正人性。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "这种设备带来的技术焦虑问题恐怕是人类所不能适应和解决的", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["技术伦理", "脑机接口/神经技术", "科学传播与公众心理"],
   "issue_candidates": ["脑机接口的人脑应用", "技术焦虑", "意识安全", "转基因争议的类比", "技术推广的团体淘汰"],
   "text_function_candidates": ["答疑（知乎回答）", "评论", "批评技术乐观主义", "论证性短文"],
   "object_candidates": ["马斯克", "Neuralink", "转基因作物", "人类/技术使用者团体"],
   "working_keywords": ["应用（广义/狭义）", "技术焦虑", "底层成本", "意识安全", "特殊受害者", "淘汰"]
  },
  "notes": "无图片节点；lexical 与正文段数一致（17段）。P012 引号内话语疑为作者拟设示例，正文未标注真实来源，记录时未归给第三方。文中「转基因作物已被证明安全」与脑科学相关判断属作者表述且无出处，登记为待外部核查。"
 },
 "6f8ec963": {
  "analysis": {
   "question_context": "知乎提问（Q001）仅一句「语言学有什么意义？」属提问者语境，提问本身隐含对语言学价值的疑问。作者以反问开篇否定「无用」，进而主张社会学科的问题首先是语言学问题，并把「语言学无用」的判断归因于评判者立足点太低、视野太近、责任使命太局部。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "以反问否定「语言学无用」，提出社会学科的问题几乎百分之百首先是语言学问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "以「民主/democracy」为例：社会学科基本概念须先从词源、演变、变体传布与竞争史角度解析。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "这种解析是最根源的探索；严格意义上智慧即产生和使用语言的能力；语言决定所处社会、价值观、立场与决策方向。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "反驳：语言学成果未应用于实际，责任不在语言学，而在政治学、经济学、管理学乃至哲学的肤浅和无能（类比数学）。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011"], "summary": "结论/劝诫：觉得语言学、数学、哲学无用只因立足点低、视野近、使命局部，要反省的是得出该结论的自己。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问否定「语言学无用」：语言学怎么会没用。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "社会学科的问题几乎百分之百首先是语言学问题。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「民主／democracy」到底是什么，首先是一个语言学问题，而不是一个政治学问题。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "几乎一切社会学科的基本概念都要先从词源、词汇演变、各变体的传布和竞争史角度先解析一番。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种解析本身就是对人类和人类社会最根源的探索。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在严格的意义上，智慧即产生和使用语言的能力。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你使用什么样的语言，你就在什么样的社会里、遵循什么样的价值观、喜欢什么样的人、站什么样的立场、有什么样的决策方向。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "语言学的研究成果没能应用于实际，不是语言学的无能，而是政治学、经济学、管理学乃至于哲学的肤浅和无能，不是语言学的责任。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "类比数学：数学的成果没能找到现实应用，责任不在数学而在于物理学、工程学、统计学、运筹学。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "觉得语言学、数学和哲学无用，只是因为立足点太低、视野太近、担负的责任和使命太局部而已；要反省和努力的是得出这个结论的自己。", "evidence": ["E11"]}
   ],
   "argument_steps": ["以反问否定「无用」并给出总命题（P001—P002）。", "举例：民主/democracy 的界定属语言学问题（P003）。", "扩展：社会学科基本概念须作词源与词史解析（P004）。", "提升：这种解析是最根源的探索（P005）；给「智慧」下定义（P006）；语言决定社会位置与立场（P007—P008）。", "归责：未能应用的责任在政治学等学科而非语言学（P009）。", "类比数学以支撑归责（P010）。", "劝诫收束：无用判断源于立足点与视野（P011）。"],
   "concept_usage": [
    {"term": "语言学", "meaning": "研究语言本身的规律和事实的学科（作者在本文给出的定义）。", "evidence": "P009", "ambiguity": "作者未说明该定义是否涵盖其主张的全部研究范围。"},
    {"term": "智慧", "meaning": "作者的定义性用法：在严格的意义上即产生和使用语言的能力。", "evidence": "P006", "ambiguity": "限定语「在严格的意义上」表明作者知道存在其他用法，但未说明。"},
    {"term": "民主／democracy", "meaning": "被举为「基本概念须先作语言学解析」的例证；作者主张其界定问题首先是语言学问题。", "evidence": "P003", "ambiguity": "未展开该词的具体词源或竞争史，仅作举例。"},
    {"term": "无用／意义", "meaning": "作者把「无用」判断归因于评判者的立足点、视野与责任范围，而非学科本身。", "evidence": "P011", "ambiguity": "未给衡量学科「有用」的标准。"},
    {"term": "责任", "meaning": "作者用以在学科之间分配「研究成果未能应用」的责任。", "evidence": "P009", "ambiguity": "未说明该责任分配的依据。"}
   ],
   "examples_and_targets": ["「民主 / democracy」的词义界定（P003）：作者例证。", "数学与物理学、工程学、统计学、运筹学（P010）：作者类比。", "政治学、经济学、管理学、哲学（P009）：作者批评的对象（「肤浅和无能」）。", "「觉得语言学、数学和哲学无用」的人（P011）：作者的批评与劝诫对象，可能包括提问者一方。"],
   "conditions": ["断言以「几乎百分之百」「几乎一切」限定（P002、P004）。", "「智慧」的定义被限定为「在严格的意义上」（P006）。", "「责任」论述限定在「没能将研究成果应用于实际」的情形（P009）。", "作者未说明判定某问题「首先是语言学问题」的操作标准。"],
   "rhetoric_and_tone": "以反问开场（「语言学怎么会没用？」）；断言密集、语气强（「肤浅和无能」）；训诫式收尾把反省指向提问者一方（「要反省和努力的是得出这个结论的自己」）；使用数学类比；结构为「反问—命题—举例—扩展—归责—劝诫」；全篇无引文、无数据。",
   "unresolved_questions": ["「社会学科的问题几乎百分之百首先是语言学问题」（P002）的量化说法无出处，待外部核查。", "「在严格的意义上，智慧即产生和使用语言的能力」（P006）未说明所依据的定义来源。", "判定概念或问题「首先是语言学问题」的操作标准未说明，反例未处理。", "对政治学等学科「肤浅和无能」的评断未给证据。", "平台话题标签是否混入正文无法判定。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "语言学怎么会没用？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "社会学科的问题几乎百分之百首先是语言学问题。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "首先就是一个语言学问题，而不是一个政治学问题。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "几乎一切的社会学科的基本概念都要从词源角度、词汇的演变角度", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这种解析本身就是对人类和人类社会最根源的探索。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "在严格的意义上，智慧即产生和使用语言的能力。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "你使用什么样的语言，你就在什么样的社会里", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "以至于没有任何细节是无关紧要的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "不是语言学的无能，而是政治学、经济学、管理学乃至于哲学的肤浅和无能", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "这就像数学的成果没能找到现实应用，责任不在数学而在于物理学、工程学、统计学、运筹学一样。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "只是因为立足点太低、视野太近，担负的责任和使命太局部而已", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["语言学", "社会科学方法论", "学科价值论"],
   "issue_candidates": ["语言学的意义与用处", "社会学科概念的词源解析", "学科间责任归属", "语言与思维/社会的关系"],
   "text_function_candidates": ["答疑（知乎回答）", "论辩", "学科辩护", "训诫式劝告"],
   "object_candidates": ["语言学", "政治学", "经济学", "管理学", "哲学", "数学", "物理学", "工程学", "统计学", "运筹学"],
   "working_keywords": ["语言学", "词源", "词汇演变", "智慧", "民主/democracy", "无用", "立足点"]
  },
  "notes": "无图片节点；lexical 与正文段数一致（11段）。文中量化断言（「几乎百分之百」「几乎一切」）与对政治学等学科「肤浅和无能」的评断均为作者表述且无出处，登记为待外部核查，未当作已证实事实。"
 },
 "25230cca": {
  "analysis": {
   "question_context": "知乎提问（Q001）问一段感情在付出却得不到回报的时候应该放弃还是坚持。提问把「付出得不到回报」当作决策依据，属提问者语境。作者直接否定这一前提，改以「对方是否觉得困扰」作为放弃或坚持的判据，并给出判定是否困扰的方法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "否定提问前提：回报与否和放弃/坚持无关；相关的是所爱对象是否觉得这些行为形成困扰。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "若对方觉得困扰就必须放弃；此时放弃才是付出，而以「付出」为名的继续是掠夺。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "以自问自答给出判据：继续无感谢、停止无挽留，即为困扰。", "role": "definition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "付出得不到回报根本不影响放弃或者坚持，这根本是两个无关的问题。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "影响到放弃或者坚持的，是你所爱的对象是否会觉得你的这些行为形成困扰。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果对方觉得困扰，你必须放弃。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在对方觉得困扰时，放弃才是付出，而以「付出」为名的继续却是掠夺。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判定是否造成困扰的方法：继续无感谢，停止无挽留，即为困扰。", "evidence": ["E5", "E6"]}
   ],
   "argument_steps": ["否定前提：回报问题与去留问题无关（P001）。", "替换判据：以对方是否觉得困扰为准（P002）。", "行动要求：若造成困扰则必须放弃（P003）。", "重估行为：此时放弃是付出，继续是掠夺（P004）。", "给出判据：继续无感谢、停止无挽留即为困扰（P005—P007）。"],
   "concept_usage": [
    {"term": "付出", "meaning": "作者把「付出」与是否被接受挂钩；带引号的「付出」指造成困扰却仍以付出为名的行为。", "evidence": "P004", "ambiguity": "两个层次的「付出」用法并置，作者未分别定义。"},
    {"term": "困扰", "meaning": "所爱对象对行为的感受，作者给出操作性判据（继续无感谢、停止无挽留）。", "evidence": "P002", "ambiguity": "判据依赖对方反应，未说明观察期限与例外情形。"},
    {"term": "放弃／坚持", "meaning": "由对方是否觉得困扰决定，而不由是否得到回报决定。", "evidence": "P001", "ambiguity": "未讨论双方相互困扰或对方态度不明的情形。"},
    {"term": "知止（标题）", "meaning": "正文未出现该词，标题含义未在本文说明。", "evidence": "P001", "ambiguity": "标题与正文的关系属编选层面，需研究者复核。"}
   ],
   "examples_and_targets": ["正文未使用人物、事件、机构或数据例证。", "「继续无感谢，停止无挽留」为判据式表述，非叙事例证（P006—P007）。", "隐含对象：付出却得不到回报的一方，以及「你所爱的对象」（P002）。"],
   "conditions": ["结论以「如果对方觉得困扰」为条件（P003）。", "判据以观察对方反应为前提，未说明观察期限与情境差异。", "未讨论对方不表态、或双方相互造成困扰等情形。"],
   "rhetoric_and_tone": "极简断言体，短句分行（P006—P007 断句成箴言式收束）；直接对「你」下判断与要求（「你必须放弃」）；无举例、无让步、无出处；语气冷静决断，带箴言感；标题「知止」未在正文出现。",
   "unresolved_questions": ["「困扰」的判断依赖对方反应；若对方既不感谢也不挽留但真实态度并非困扰，正文未说明如何处置。", "「放弃才是付出」的适用范围（是否仅限于对方觉得困扰时）未说明。", "未处理已发生的付出／沉没成本是否应影响判断。", "标题「知止」在正文中未出现，其与正文的关系未在本文说明。", "平台话题标签是否混入正文无法判定。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "付出得不到回报根本不影响放弃或者坚持，这根本是两个无关的问题。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "影响到放弃或者坚持的是你所爱的对象是否会觉得你的这些行为形成困扰。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果对方觉得困扰，你必须放弃。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这个时候放弃才是付出，“付出”却是掠夺。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "继续无感谢，停止无挽留，", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "即为困扰。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["情感关系/人际伦理", "行动建议"],
   "issue_candidates": ["付出与回报", "放弃或坚持的判据", "是否对他人造成困扰", "单方面追求与骚扰的界线"],
   "text_function_candidates": ["答疑（知乎回答）", "短答/箴言式建议", "行动指导"],
   "object_candidates": ["（未指名）付出的一方", "（未指名）你所爱的对象"],
   "working_keywords": ["付出", "回报", "放弃", "坚持", "困扰", "感谢", "挽留", "知止"]
  },
  "notes": "无图片节点；lexical 与正文段数一致（7段）。正文极短（132字），为问答式短答，无例证、无出处。标题「知止」未在正文出现，标题与正文的对应关系待研究者复核；此点已登记在 unresolved_questions。"
 },
 "aed1fe34": {
  "analysis": {
   "question_context": "知乎提问（Q001）问历史上有在位长久又得善终的昏君吗。作者先以「乾隆」「万历」两个名字直接作答，再概括「在位久而得善终的皇帝大多数都是昏君」，随后列出四项机制解释这一现象，最后指出只有挣脱这些机制的幸存者才不被称昏君。提问中的「昏君」是提问者的用语，作者沿用但未给出严格定义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "以乾隆、万历作答，并概括：在位久而得善终的皇帝大多数都是昏君。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "强调不是玩笑；理由是稳定在位太久且为实权君主必有极大副作用，几乎总能抵消其正面作用。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "副作用一：削弱文官政治和内阁体制——皇权过稳、安插私人，文官以屏蔽信息对抗，终致特务横行、君臣相疑、执政有效性下降。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "副作用二：妨碍储君继承，祸延三代；若非开国等特殊理由就只是好大喜功、贪恋权位，当「昏」字并不冤枉。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P012"], "summary": "副作用三：年纪大精力不足、危机处理节奏变慢，未必能用「岁月积累的智慧」补足。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P013"], "summary": "副作用四：文官集团握意识形态解释权，有冲动把这类皇帝定性为昏君以儆效尤，故极少有长期在位者最后得好名声。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P014"], "summary": "结论：只有挣脱上述各条的幸存者才不被称昏君，故幸存者很少。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以乾隆、万历为答案例证，并概括：实际上在位久而得善终的皇帝，大多数都是昏君。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "君主稳定在位时间太长而且是实权君主的话，势必有几个极大的副作用，几乎总是可以抵消掉其那点正面作用。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "皇权过于稳固、皇帝在专业官僚中安插的私人越多，越会导致文官系统以屏蔽信息对抗；后期总是导致特务大行其道、君臣相疑、执政有效性大幅下降，只剩下大量歌功颂德的虚假数字。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "皇帝在位超过三十年往往导致下一代君主事实上被跳过；短期继任者来不及吃透政局与人事、来不及留下「太子党」，下一任太子岌岌可危，足以造成外戚专权、社稷倾覆之危。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种祸延三代若非开国之类的特殊理由，就无非为了好大喜功、贪恋权位；只这一条，当一个「昏」字并不冤枉。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "年纪大了精力不足、应付不了统治国家必要的事务处理，势必造成处理危机的节奏变慢，而这未必能用所谓「岁月积累的智慧」补足。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "文官集团手里握着意识形态的解释权，有天然的冲动要把这类皇帝定性为昏君以儆效尤；所以极少有长期在位的皇帝能在最后落下一个好名声。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有把上面几条全都挣脱了，才会有一个满足条件而不被称为昏君的幸存者，自然幸存者也就少得很。", "evidence": ["E13"]}
   ],
   "argument_steps": ["直接作答并举二例（P001—P002）。", "给出总命题：在位久而得善终者大多是昏君（P003—P004）。", "提出理由框架：稳定在位过久的实权君主必有几大副作用（P005）。", "副作用一：削弱文官政治与内阁体制，文官屏蔽信息、特务横行、虚假数字（P006—P007）。", "副作用二：妨碍储君继承、祸延三代；并归因于好大喜功贪恋权位（P008—P011）。", "副作用三：年老精力不足，非「岁月积累的智慧」可补（P012）。", "副作用四：文官集团握解释权，倾向把长期在位者定性为昏君（P013）。", "结论：全部挣脱者才是幸存者，故极少（P014）。"],
   "concept_usage": [
    {"term": "昏君", "meaning": "作者未给严格定义；用法含两层——治理实效不佳（P011），以及文官集团握解释权所作的定性（P013）。", "evidence": "P003", "ambiguity": "两层含义未在文中区分，可能影响该词的解释。"},
    {"term": "实权君主", "meaning": "作者设定的前提条件，指不受制于人的君主。", "evidence": "P005", "ambiguity": "未说明判定实权的标准。"},
    {"term": "文官政治／内阁体制", "meaning": "作者认为会被长期在位的皇帝严重削弱的部分。", "evidence": "P006", "ambiguity": "未举具体朝代制度为例。"},
    {"term": "皇权与相权之争", "meaning": "作者称其与王权与神权之争一样「古老而基要」。", "evidence": "P007", "ambiguity": "未给文献或史例依据。"},
    {"term": "意识形态的解释权", "meaning": "文官集团掌握的能力，作者视为「昏君」定性来源之一。", "evidence": "P013", "ambiguity": "未说明该解释权的作用机制与限度。"},
    {"term": "副作用", "meaning": "作者列出的四项：削弱文官政治、妨碍储君继承、精力不足、文官定性。", "evidence": "P005", "ambiguity": "第四条属对评价本身的影响，与前三条性质不同，作者未作区分。"}
   ],
   "examples_and_targets": ["乾隆、万历（P001—P002）：作者给出的答案例证，正文未展开具体史实。", "特务（P007）：作者所述后期现象，未举朝代与机构。", "「太子党」（P009）：作者用语。", "外戚专权、社稷倾覆（P009）：作者所述风险。", "「岁月积累的智慧」（P012）：作者否定的说法（带「所谓」）。", "歌功颂德的虚假数字（P007）：作者的描述性判断。", "文官集团（P013）：作者指认的行动者。"],
   "conditions": ["论述前提限定为「稳定在位时间太长而且是实权君主」（P005），并以「超过三十年」作为储君问题的尺度（P009）。", "结论使用「大多数」「势必」「几乎总是」「往往」等限定；第四条与其他三条性质不同，涉及标签本身的来源。", "历史条件限定为「古代的健康条件」（P009）。", "作者为「祸延三代」留出例外：「如果不是有什么初代开国这类的特殊理由」（P010）。"],
   "rhetoric_and_tone": "以两个名字直接作答开场；编号列举（1）2）3）4））；用「ta」代称；冷峻论断中带反讽（「当一个昏字并不冤枉」「注意是最后」）；对「岁月积累的智慧」加「所谓」以示不认可；全篇无史料引证、无年份与文献数据。",
   "unresolved_questions": ["乾隆、万历被列为答案，但正文未叙述其具体史实，仅由一般机制推出，需外部史料核查。", "四项机制所依据的历史例证、朝代与文献均未给出。", "第四条（文官集团定性）与前三条所述「实际昏庸」性质是否一致，作者未作区分，可能影响「昏君」一词在文中的用法。", "「超过三十年」等阈值的依据未说明。", "标题「老昏君」与正文的对应关系未在文中说明。", "平台话题标签是否混入正文无法判定。"],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "实际上，在位久而得善终的皇帝，大多数都是昏君。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "乾隆", "relation": "context"},
    {"key": "E3", "paragraph_id": "P002", "quote": "万历", "relation": "context"},
    {"key": "E4", "paragraph_id": "P005", "quote": "势必有几个极大的副作用，几乎总是可以抵消掉ta的那点正面作用。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "索性屏蔽你的信息来源，这样你有权也无用。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "只剩下大量歌功颂德的虚假数字。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "往往导致下一代君主在事实上被跳过", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "足以造成外戚专权、社稷倾覆之危。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "如果不是有什么初代开国这类的特殊理由，就无非为了这位好大喜功、贪恋权位罢了。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "只这一条，当一个昏字并不冤枉。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这未必能用所谓“岁月积累的智慧”补足。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "ta们有天然的冲动要把这类皇帝定性为昏君，以儆效尤。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "上面这几条全都挣脱了，才会有一个满足条件而不被称为昏君的幸存者", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中国古代政治史", "皇权与官僚制度", "历史评论"],
   "issue_candidates": ["长期在位的实权君主", "储君继承", "文官集团与意识形态解释权", "昏君的判定标准"],
   "text_function_candidates": ["答疑（知乎回答）", "史论式评论", "机制归因"],
   "object_candidates": ["乾隆", "万历", "文官集团", "特务", "外戚", "宰相"],
   "working_keywords": ["昏君", "实权君主", "文官政治", "内阁体制", "皇权与相权", "储君", "太子党", "意识形态的解释权"]
  },
  "notes": "无图片节点；lexical 与正文段数一致（14段）。文中史实性论断（乾隆、万历、特务横行、外戚专权、社稷倾覆等）与「超过三十年」等阈值均无出处，登记为待外部核查，未当作已证实事实。第四条（文官集团握解释权而定性强加）与其他三条性质不同，记录时未合并。"
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
