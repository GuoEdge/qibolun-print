# -*- coding: utf-8 -*-
"""批次 r001-b0351 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0351.sessions.py            # 写 out/r001-b0351.out.jsonl
  python3 records/r001-b0351.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import autofill_empty_analysis, build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0351"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0351.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "2b67383c": {
  "analysis": {
   "question_context": "提问者问：如何看待网传浙江大学赵鼎新教授辞职信，中国科研体系与欧美相比有何区别？作者没有直接评论该辞职信，而是从中国社科研究战略定位的两次转轨（自外而内→自内而外）解释当下“引进外部人才、学术标准与国际接轨”的处境，最后给处在被求贤位置上的知识分子以心态预期建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出做事须知来处与去处，决定从中国自身的转轨讲起。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "第一代领导人的立场是“将红旗插遍全球”，教科书与宣传把世界描绘成你死我活、双方都要统一全球的格局。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "七十年代后期第二代领导人调整：停止输出革命，转向经济建设与和平共处五项原则，注意力由外转内，为社科研究划出分水岭。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "转变前的社科研究以共产主义理想范式构造世界观，从全球无产阶级一般处境出发；企业研究优先“符合共产主义原则”而非自身存续壮大。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P010", "P011"], "summary": "转变后转向中国特色社会主义道路与三原则模式，社科研究在本质上成为中国研究、民族研究，而非为全人类提供示范的普适性研究。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "以“什么意思？”设问后举例：西方谈多元文化共存，我们谈新疆民族政策乃至土默特左旗民俗；西方成果对他国有直观借鉴价值，我们的研究要被他国借鉴非常困难。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016"], "summary": "铁幕的要害在于我们信守承诺、自限地步，不争夺美西方对国际意识形态的主导权，以换取国际秩序稳定与大国和平共存；这不是能力不足，而是国家战略划定的指导线。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "吊诡后果：西方“全球普适”研究成了盲目照搬国家的灾难之源；牛顿力学、相对论虽普世，落地仍需工程性适配；越崇拜越照搬者损失越惨重。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P021"], "summary": "中国式“闭门造车”因投入足够智力资源、面向实际数据快速调整而成果斐然。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027"], "summary": "ERP 类比：国际通用原型被客户开箱即用或乱定制而失败，服务自身业务的“土软件”反使企业营收飞天，大开发商却看不上其框架与代码。", "role": "example"},
    {"unit_id": "U011", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032"], "summary": "现状：这家“乡土企业”业绩好到动了整理系统外卖的心思，且全球扩张要求系统兼容多币种、多语言、多时区，规范化、普适化已是自身业务的紧迫需求，市场也在呼唤替代方案。", "role": "context"},
    {"unit_id": "U012", "paragraph_refs": ["P033", "P034"], "summary": "问题实质：我国社科研究再次站到自内而外的分水岭，因而产生“学术标准与国际接轨”和引进外部人才进一步建设中国社会研究范式的需求。", "role": "conclusion"},
    {"unit_id": "U013", "paragraph_refs": ["P035", "P036", "P037"], "summary": "限定：不能单方面下决心，须慎重考虑“中美共治”甚至相当长时间“以美为主”的现实可能；对人类社会的责任要求不提前抛弃和平共治的希望，故在是否国际化上异常慎重、纠结反复。", "role": "qualification"},
    {"unit_id": "U014", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042"], "summary": "以“上市指导团队”和三顾茅庐请诸葛先生却狠不下心与曹操翻脸为喻，说明引进人才的困扰；是非曲直不能只看发票收据。", "role": "example"},
    {"unit_id": "U015", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "写作目的不是评理，而是让读者明白时代走向与心态预期：求贤若渴是真诚的，但仍有反复曲折；回乡报国要做好自力更生、百折不回的准备，只有不计许诺与挫折的决心才有较大成功概率。", "role": "action_advice"},
    {"unit_id": "U016", "paragraph_refs": ["P050"], "summary": "结语：好事多磨。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国第一代领导人的基本立场是“要将红旗插遍全球”，要在国际无产阶级革命中担任领袖和旗手。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "七十年代后期第二代领导人做了历史性调整：停止“输出革命”，转向以经济建设为中心和和平共处五项基本原则。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这一转变给中国社科研究划出分水岭，使其在本质上成为中国研究、民族研究，而非为所有国家提供示范的普适性研究。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "西方研究成果至少在理论上对所有非单一民族国家、移民国家有借鉴价值，而中国的研究要被他国借鉴非常困难。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“中国社会学研究”与“国际性社会学研究”之间铁幕的要害，在于我们信守承诺、自限地步，不争夺美西方对国际意识形态的主导权，以换取国际秩序稳定与和平共存。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不是中国不能搞国际视野的学术，而是国家战略为社科研究划定了范围上、原则上的指导线。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美西方“全球普适”的研究最后成了盲目追随、全盘照搬国家的灾难之源，但不应因此责怪西方学术界或否定这些学术成就的价值。", "evidence": ["E8", "E9", "E17"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国这种“拒绝仰望星空，一心低头看路”的路径，因投入足够智力资源、又能面向实际数据快速调整而成果斐然。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国社科研究经过自外而内阶段后再次站到自内而外的分水岭上，因而出现学术标准与国际接轨、引进外部人才建设中国社会研究范式的需求。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这件事不能由我们单方面下决心，因为必须慎重考虑“中美共治”甚至相当长时间里仍“以美为主”的现实可能。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对人类社会的责任要求我们不能在“和平共治”的可能尚未绝望之前就提前抛弃这一希望。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "存在曲折性和复杂性不表示求贤若渴是假的；但真诚也不意味着没有反复曲折、不意味着心想事成。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只有在“哪怕没有这些美好的许诺，即使要忍受难以想象的挫折，我也绝不错过这个机会”的决心下，才有比较大的概率得到想要的结果。", "evidence": ["E18"]}
   ],
   "argument_steps": [
    "前提：要理解当下处境，须先看清中国自身战略定位的转轨（P001-P002）。",
    "背景：第一代领导人的国际主义革命立场使社科研究从全球无产阶级一般处境出发（P003-P009）。",
    "转轨：第二代领导人停止输出革命、转向经济建设与和平共处，注意力由外转内（P006-P007）。",
    "推论与例证：社科研究由此成为中国研究、民族研究（P010-P011），并以民族议题与研究可移植性举证（P013-P014）。",
    "条件与代价：此定位是为换取国际秩序稳定与和平共存而自限，限制来自国家战略而非学术能力（P015-P016）。",
    "反衬与类比：西方普适研究在照搬国造成灾难（P017-P020），中国面向自身实际的路径反而成功（P021），并以 ERP 与土软件类比（P022-P027）。",
    "现状判断：全球扩张使规范化、普适化成为自身紧迫需求，市场也在呼唤（P028-P032）。",
    "结论：中国社科研究再次处于自内而外的分水岭，产生与国际接轨、引进人才的需求（P033-P034）。",
    "让步与限定：能否国际化不能单方面决定，须考虑“中美共治”甚至“以美为主”的可能（P035-P037）。",
    "行动建议：真诚求贤与过程曲折并存，读者应以不计得失的决心和自力更生的准备应对（P043-P049）。"
   ],
   "concept_usage": [
    {"term": "自外而内／自内而外", "meaning": "指社科研究的定位阶段：先是面向全球无产阶级，后转向立足中国自身，如今又面临向外输出中国范式的分水岭", "evidence": "P007/P033", "ambiguity": "作者用同一词组的语序区分两个阶段，未给出严格定义"},
    {"term": "铁幕", "meaning": "指“中国社会学研究”与“国际性社会学研究”之间的隔断", "evidence": "P015", "ambiguity": "借用冷战语汇作比喻，非字面制度描述"},
    {"term": "三原则模式", "meaning": "从中国自身社会现实、历史现状出发因地制宜、因时制宜，以经济发展和人民生活水平提高为效益标准", "evidence": "P010", "ambiguity": "作者概括性说法，未给出正式名称与完整出处"},
    {"term": "和平共处五项基本原则", "meaning": "七十年代后期起中国对外方针的组成部分，与停止输出革命并列", "evidence": "P006", "ambiguity": "正文未展开其内容"},
    {"term": "土软件／ERP", "meaning": "比喻中国社科研究：服务自身具体业务、不追求通用原型", "evidence": "P022-P024", "ambiguity": "比喻的逐项对应关系由读者推断，作者未声明"},
    {"term": "上市指导团队", "meaning": "比喻被引进帮助中国社会研究规范化、国际化的外部人才", "evidence": "P038", "ambiguity": "具体所指的机构或个人身份不明"},
    {"term": "诸葛先生", "meaning": "借三国典故指被请来却处境尴尬、最终抑郁的引进人才", "evidence": "P040-P042", "ambiguity": "典故中诸葛亮、曹操、刘备各自对应谁，作者未逐一说明"}
   ],
   "examples_and_targets": [
    "网传浙江大学赵鼎新教授辞职信：只出现在提问字段，正文未提及、未评论，属讨论语境（提问者材料）。",
    "教科书与宣传中“解放全世界人民”“资本主义的掘墓人”的表述：作者举例说明转变前的立场（P004）。",
    "新疆民族政策、土默特左旗的民俗溯源：作者举例说明中国研究的本地具体性（P013）。",
    "牛顿力学、相对论需地质勘探、模型测试等工程性适配：作者类比（P018）。",
    "ERP 国际开发商、靠侄子搞 IT 的土家族特产店、淘宝三皇冠：作者类比例证（P022-P027）。",
    "“中美共治”“以美为主”：作者指出的现实可能（P035）。",
    "三顾茅庐请诸葛先生却狠不下心与曹操翻脸：作者修辞性典故（P040-P042）。",
    "钱学森时代从戈壁滩开始：作者类比历史处境（P047）。",
    "“长风破浪会有时，直挂云帆济沧海”：作者引用后否定其为童话叙事（P048）。"
   ],
   "conditions": [
    "判断限定于“现在这个阶段”，以中国已全球扩张、必须自我升级为前提（P028-P030）。",
    "“至少在理论上如此”限定西方研究成果的借鉴价值（P014）。",
    "自限意识形态主导权被说成是为换取国际秩序稳定与和平共存的代价（P015）。",
    "国际化的决心以“和平共治”的可能尚未绝望为前提（P036）。",
    "对读者为条件式建议：只有在不计许诺、能忍挫折的决心下才有较大成功概率（P049）；“很可能”承受委屈（P048）。",
    "本文所说“我们”指中国／中国社科研究者，属作者自称立场（P005 等）。"
   ],
   "rhetoric_and_tone": "长文训诫式说理，先铺垫历史，再以商业类比（ERP、上市、土软件）与典故（诸葛先生、钱学森）收束到对读者的心态建议；设问句“什么意思？”，引号反语（“闭门造车”“朝令夕改”），第二人称“你”直接劝告，语调冷静克制又带调侃与自嘲（“诸葛先生活活抑了郁”），末尾以成语点题。",
   "unresolved_questions": [
    "提问所指的赵鼎新辞职信真伪与内容，正文未核实、未直接评论，需外部核查。",
    "作者所述中国社科研究各阶段定位及“国家战略指导线”的具体依据，本文未给出。",
    "“上市指导团队”“诸葛先生”具体所指的机构或个人身份不明。",
    "“三原则模式”的正式名称与出处未说明。",
    "“中美共治”“以美为主”属作者对未来的判断，本文内无法验证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "中国第一代领导人的基本立场是“要将红旗插遍全球”", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P006", "quote": "我们停止了“输出革命”，转向了以经济建设为中心和和平共处五项基本原则", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P007", "quote": "这就给中国的社会科学研究划定了一个分水岭", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P011", "quote": "在本质上是一种中国研究、民族研究", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P014", "quote": "而我们的研究要在其他国家加以借鉴就非常困难", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P015", "quote": "我们信守承诺，自限地步，不争夺美西方对国际意识形态的主导权", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P016", "quote": "而是我们自己的国家战略为我们的社科研究划定了范围上、原则上的指导线", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "最后却成了一切盲目追随、全盘照搬的忠实信徒国家的灾难之源", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P018", "quote": "这老实说不能责怪西方学术界，也不能否定这些学术成就的价值", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P021", "quote": "因为投入了足够的智力资源、又能身段柔软面向实际数据快速“朝令夕改”而成果斐然", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P033", "quote": "现在已经再次站到了自内而外的分水岭上", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P034", "quote": "因此，我们才有了“学术标准与国际接轨”的需求", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P035", "quote": "我们自己不能单方面的下定这个决心", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P036", "quote": "我们不能在实现“和平共治”的可能尚未绝望之前自己就提前决定抛弃这希望", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P045", "quote": "存在曲折性和复杂性不表示求贤若渴是假的", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P046", "quote": "也并不意味着没有反复和曲折，不意味着心想事成", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "导致了大面积的、普遍的失败", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P049", "quote": "你才有比较大的概率得到你想要的结果", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中国学术体制", "国际关系", "社会科学方法论", "当代史叙述"],
   "issue_candidates": ["中国科研体系与欧美的区别", "社科研究国际化与本土化", "海外人才引进与回国处境", "意识形态主导权与中美关系"],
   "text_function_candidates": ["解释", "评论", "经验总结", "建议", "类比论证"],
   "object_candidates": ["中国第一代／第二代领导人", "美西方", "新疆", "土默特左旗", "钱学森", "诸葛亮", "曹操", "浙江大学（仅提问字段）", "赵鼎新（仅提问字段）"],
   "working_keywords": ["自外而内", "自内而外", "铁幕", "中国特色社会主义道路", "和平共处五项基本原则", "学术标准与国际接轨", "好事多磨", "ERP", "上市指导"]
  },
  "notes": "平台问答（知乎），提问字段提到浙江大学赵鼎新教授辞职信，属提问者材料，正文未提及该信、未直接作答，仅作为背景问题；作者以“我们”自称中国／中国社科研究者立场。"
 },
 "f67c9dc5": {
  "analysis": {
   "question_context": "提问者问：历史上与现实中的俄国为什么扩张侵略成性？这个国家为什么如此热衷于对外扩张？作者不回答“俄国本性如何”，而是反驳“本性论”这种解释方式本身：认为它是为构造“敌人必然愚蠢邪恶”的信仰，主张改用地理条件、地缘环境、经济模式等难变要素结合当下条件来做预测。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "直接回应：这种“本性”论本质上是为了构造对“敌人必然愚蠢邪恶”的信仰。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "反例推理：幼主独揽的村级、乡级君主制小国也许可能纯受本性驱动；而必须依赖精英合作管理千万上亿人口的大国，文化上必然符合同等级社会化标准，否则早因内部反社会性而分裂消亡；以二十层大楼必有合理力学结构作类比。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "结论：用“本性论”预测国家行为非常不可靠；人类是高度智能动物，做事先算账、算可行性，按计算结果决定行为。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011"], "summary": "类比举证：男性天性好色、人类天性贪吃都有“铁证”，却推不出满街强奸或生鲜区抢劫。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "定性：不讲力量对比、局势关系而鼓吹“天性”，是把敌人矮化、丑化、劣化的诉诸无知的愚民手段；把这一要素代入预测公式并放大权重的人“理性致残”，计算结果几乎没有可靠性。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016"], "summary": "补强：这样的方法论必然算出“满大街强奸”和“生鲜区哥谭”。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P017", "P018"], "summary": "正面方法：理智的国家从地理条件、地缘环境、经济模式这类难以短时间改变的要素入手，结合当下具体条件预测；判断张三会动手，是因他可能不得不动手或此时动手收益远大于成本风险。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P019", "P020", "P021", "P022"], "summary": "揭示“本性”宣传的用意：先预设“我的不可战胜”，于是对方的挑战必然是“非理性冲动”；结果起步就从“敌人智商不可能超过八十”出发“料敌从窄”，不断被现实迎头痛击。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P023", "P024", "P025"], "summary": "定性升级：不加前提就认定自己不可能不如愿，是丧心病狂级别的傲慢，简称种族主义；种族主义的意思是“我是人，你不是人”。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P026"], "summary": "收尾：2024年了，人类应该成熟一点了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种“本性”论本质上是为了构造一种对“敌人必然愚蠢邪恶”的信仰。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果是幼主在位而且大权独揽的村级、乡级君主制“国家”，也许还会有“纯受本性驱动”的可能。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个必须依赖精英合作管理几千万上亿人的政令统一大国，文化上必然会符合同等级的社会化标准，否则内部反社会性早已限制其规模，顶多三五十年就分裂消亡。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用“本性论”来预测一个国家会如何行事是非常不可靠的做法。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类是高度智能的动物，做事先算账、算可行性，根据具体计算结果决定行为。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不讲现实的力量对比、局势关系而鼓吹“天性”，本质上是将敌人矮化、丑化、劣化的诉诸无知的愚民手段。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把这种要素代入预测公式并放大权重的人已被宣传伎俩“理性致残”，其计算结果几乎没有任何可靠性。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理智的国家会从地理条件、地缘环境、经济模式这类难以短时间改变的要素入手，结合当下具体条件做预测。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“本性”宣传的用意在于预设“我的不可战胜”，从而把对方的动手解释为被“天性中不可克制的冲动”驱使的非理性结果。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不加任何前提就认定自己无论如何都不可能不如愿，本身就是一种丧心病狂级别的傲慢。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种傲慢简称种族主义；种族主义的意思不是“我是一种人，你是另一种人”，而是“我是人，你不是人”。", "evidence": ["E14", "E15"]}
   ],
   "argument_steps": [
    "提出反命题：所谓“本性论”是为构造敌人必然愚蠢邪恶的信仰（P001）。",
    "举反例并作类比：只有小规模独裁政体才可能纯受本性驱动，大国必受社会化标准约束，如同大楼必有合理力学结构（P002-P003）。",
    "给出理由：人类先算账、算可行性，故本性论预测不可靠（P004-P005）。",
    "用“好色”“贪吃”两个更确定的天性做归谬：天性存在推不出行为必然发生（P006-P011）。",
    "定性：鼓吹天性是诉诸无知的愚民手段，被其俘获者“理性致残”（P012-P015）。",
    "反向验证：该方法论必然算出“满大街强奸”“生鲜区哥谭”（P016）。",
    "给出替代方法：从地理、地缘、经济模式与当下条件预测（P017-P018）。",
    "揭示动机：本性论服务于“我不可战胜”的前提，导致“料敌从窄”与被现实痛击（P019-P022）。",
    "结论：这种无前提的自信是丧心病狂级别的傲慢，即种族主义（P023-P025），并以“人类应该成熟一点”收束（P026）。"
   ],
   "concept_usage": [
    {"term": "本性论", "meaning": "以国家或民族的固有“本性”解释并预测其对外行为的说法", "evidence": "P001/P004", "ambiguity": "作者用“这种‘本性’论”指称提问中的“扩张侵略成性”，未区分不同学派的本性论"},
    {"term": "社会化标准", "meaning": "同规模国家在文化上大致奉行的道德标准", "evidence": "P002", "ambiguity": "未说明其形成机制与衡量方式"},
    {"term": "理性致残", "meaning": "被宣传伎俩影响后丧失正常判断能力", "evidence": "P014", "ambiguity": "修辞性说法，非严格术语"},
    {"term": "料敌从窄", "meaning": "从低估敌人智力与能力的起点做判断", "evidence": "P022", "ambiguity": "作者化用成语，未给出定义"},
    {"term": "种族主义", "meaning": "本文中特指“我是人，你不是人”的自我神化心态，而非一般的人种歧视", "evidence": "P024/P025", "ambiguity": "与通常用法的差别明显，属作者自定义"}
   ],
   "examples_and_targets": [
    "提问中的“俄国扩张侵略成性”：本文的反驳对象（提问者命题，P001 起即针对该说法）。",
    "村级、乡级君主制的“国家”与幼主独揽：作者设想的极端反例（P002）。",
    "二十层高楼的力学结构：作者类比（P003）。",
    "“男性天性好色”“满大街都是强奸”：作者归谬例证（P007-P008）。",
    "“人类天性贪吃”、司美格鲁肽卖断货、减肥课程：作者归谬例证（P009）。",
    "“生鲜区哥谭”“生鲜区都会遇到团伙抢劫”：作者借喻（P011/P016）。",
    "张三会动手的判断：作者虚拟案例（P018-P019）。",
    "“敌人智商不可能超过八十”：作者引述“料敌从窄”心态的说法（P022）。"
   ],
   "conditions": [
    "“如果是幼主在位而且大权独揽的村级、乡级君主制‘国家’……也许”为假设性限定，作者并未断言现实中存在此类国家（P002）。",
    "大国判断以“必须依赖精英合作管理”“几千万上亿人”“政令统一”为条件（P002）。",
    "“理智的国家即使对敌人的属性——或者准确的说，中长期动向——有所判断”界定了作者认可的预测对象是中长期动向（P017）。",
    "对“天性”的批评限定于用它替代力量对比与局势关系分析的做法（P012）。",
    "结论“我是人，你不是人”是对“不加前提的自信”的定性，带修辞夸张。"
   ],
   "rhetoric_and_tone": "短段落密集、口语化论辩体：连续反问（“那又如何？”“是不是铁证如山？”“你难道会因此觉得……”），以归谬与类比压过对手，用词强烈（“愚民手段”“理性致残”“丧心病狂级别的傲慢”“种族主义”），并借“生鲜区哥谭”等戏谑比喻讽刺；结尾以年份与“成熟一点”作训诫式收束。",
   "unresolved_questions": [
    "提问所问的俄国历史与现实扩张行为的具体事实，本文未举证也未逐一回应，需外部核查。",
    "作者称大国“必然”符合同等级社会化标准，其适用范围与反例（如短期战争行为）本文未讨论。",
    "“理智的国家”具体指哪些国家、由谁判断，本文未说明。",
    "作者未正面给出对俄国行为的“地理条件、地缘环境、经济模式”式预测，替代方法只是原则性表述。",
    "行文中的“ta们”所指（宣传者、受众或特定群体）未明确。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "其实这种“本性”论，从本质上是为了构造一种对“敌人必然愚蠢邪恶”的信仰", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "也许还会有所谓的“纯受本性驱动”的可能", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P002", "quote": "一个必须要依赖精英合作来管理的几千万上亿人的政令统一的大国，在文化上必然会高度符合同等级的社会化标准", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "否则内部的反社会性早就限制住了社会的规模", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "因此用“本性论”来预测一个国家会如何如何行事是非常不可靠的做法", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "做事都是一样先算账，算可行性，根据具体计算结果决定行为", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "本质上就是一种将敌人矮化、丑化、劣化的诉诸无知的愚民手段", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "其实已经被这种宣传伎俩把理性致残了", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P015", "quote": "其计算结果几乎没有任何可靠性", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P017", "quote": "而会从地理条件、地缘环境、经济模式这类难以短时间改变的要素入手，结合当下的具体条件去做预测", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "它无非是想说张三动手其实预期收益远小于成本和风险", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "先把“我的不可战胜”看作是无可怀疑的真理", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "这本身就是一种丧心病狂级别的傲慢", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "简称种族主义", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "而是“我是人，你不是人”", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P022", "quote": "于是一起步就一切都从“敌人智商不可能超过八十”的起点开始“料敌从窄”", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P016", "quote": "因为这样的方法论必然算出“满大街强奸”和“生鲜区哥谭”", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P026", "quote": "2024年了，人类应该成熟一点了", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系理论", "认知与宣传分析", "历史方法论", "社会心理学"],
   "issue_candidates": ["俄国扩张的解释", "本性论／国民性论批判", "敌情判断与预测方法", "种族主义与敌人形象建构"],
   "text_function_candidates": ["反驳", "论辩", "方法论批评", "讽刺杂文"],
   "object_candidates": ["俄国", "村级乡级君主制国家", "美西方（隐含对照）", "张三（虚拟人物）"],
   "working_keywords": ["本性论", "社会化标准", "理性致残", "料敌从窄", "种族主义", "地理条件", "地缘环境", "经济模式", "生鲜区哥谭"]
  },
  "notes": "平台问答（知乎），提问者命题（俄国扩张侵略成性）为作者反驳对象，不得归给作者；文中“ta们”所指未明。作者未正面回答俄国问题，只反驳“本性论”这一解释方式。"
 },
 "94ca1d90": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


autofill_empty_analysis(BATCH, SKELETON, ANALYSIS)


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
