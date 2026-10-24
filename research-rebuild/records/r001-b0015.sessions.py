# -*- coding: utf-8 -*-
"""批次 r001-b0015 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0015.sessions.py            # 写 out/r001-b0015.out.jsonl
  python3 records/r001-b0015.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0015"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0015.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "20c4c37c": {
  "analysis": {
   "question_context": "提问者（Q001）问“中国芯片产业前景到底怎么样？”，这是提问者的关切。作者没有停留在前景判断上，而是自设回答框架：先说明自己在另一篇回答（《中国大陆明明知道芯片不行，几十年前为什么不发展芯片？》）里批评过中国民间对芯片产业的盲目乐观，容易被误认为悲观；随即表明相反立场——相信中国芯片产业有希望而且是巨大的希望，但不走英特尔/高通式的美国模式老路，转而主张由中国主导主投、知识产权完全开放的开源体系与国际经济合作组织，把“前景如何”改写成“应当走哪条路”的方案论证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "回应语境并给立场：作者此前批评民间对芯片的盲目乐观，容易被误读为悲观；其实相信中国芯片产业有巨大的希望，但这绝不意味着应走英特尔/高通之路或孤注一掷的国力投资、纯靠自有市场买单之路。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "提出替代方案的核心：以世界超级大国国力全力支持开源体系，建立中国主导主投、知识产权完全开放的国际经济合作组织，向全人类提供无偿无限制的共有知识产权；并界定“开源”是放弃一切所有权、仅保留著作权的共产主义式开源，RISC-V 不在其列。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014"], "summary": "列出“开放知识主权联盟”条约实体的六项义务：认缴会费、向成员国提供知识产权准入优惠、五年后向全人类无条件开放联盟所持知识产权、修改本国专利法与市场法规、投资联盟内公共机构与基础设施、贯彻联盟内部国际产业标准。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023"], "summary": "列出条约实体的八项权利：无偿享有联盟所持知识产权、按出资份额审议收购清单与谈判小组组成及表决、分享未开放知识产权的授权收益、按约定价格使用联盟基础设施、参与开源社区年度奖励名单审议、请求各条约实体在对非条约国家的知识产权谈判或纠纷中采取一致行动。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P024", "P025"], "summary": "方案概要及边界：中国牵头团结发展中国家和进步发达国家组织更大市场，对现有知识产权一次性赎买；拒绝赎买的实体被视为不可依赖供应商而被拒绝和限制进入；基于自由交易原则，现有专利巨头仍可保持一定领先和独有产权，但须借框架限制“注册一个算法收全人类几十年税”。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P026", "P027", "P028"], "summary": "不走资本竞争赶超之路的两条理由：其研发体系与底层经济制度严格绑定，中国国情几乎不可能照搬，三心二意的模仿代价巨大，可能成为星球大战计划的重演；独属自己的、充满秘密与专利的芯片业对他人既是福利又是威胁，即使性能更优也会因安全顾虑被大市场弃用。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033"], "summary": "结论性策略：胜战之策需要完全改变游戏规则，不必做第一流芯片卖最高价，只需做出可用芯片送给全人类；创造者的回报改为新生态的一次性奖励与人类史上的地位，不再来自专利税金，从而永久解放全人类。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P034", "P035", "P036", "P037"], "summary": "对中国的意义与资源转向：中国以部分积累财富为全人类永久福利买单，帮助这一国家盈利就是帮助每个人；除军事工业外，把原拟投入秘密研发、独立研发的资源有计划且量力而行地转投完全开源社区。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043", "P044"], "summary": "计划的多重好处：釜底抽薪解决封锁并为中国生产力取得全球市场入场券；赢得全人类最伟大的头脑；以资本市场预期迫使美国降低遏制烈度并重创传统垄断企业股价；使“中国威胁论”不可逆转地破灭，最终不必靠航母驱逐舰捍卫安全。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P045", "P046", "P047", "P048"], "summary": "收束：历史把中国困在与垄断体制无法调和的困境中，既是危机也是无声的赋能；中国被“天命”指明去担当垄断者的敌人，一旦垄断者要价足够高便会看到资助开源的好处；中国仍以解放全人类为己任，但靠对人类的热爱而非苏联式的铁与血。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P049"], "summary": "正文末尾出现平台话题标签“科学答集/家族答集”，lexical 未覆盖该片段，属混入正文的平台字段。", "role": "context"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者相信中国芯片产业有希望，而且是巨大的希望。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不认为中国的芯片产业之路（乃至更广的 IT 产业全产业链之路）可以走美国模式的老路实现弯道超车，也不主张走凭借国力做孤注一掷产业投资、纯靠自有或上合组织共同市场买单的道路。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为中国摆脱芯片困局的最佳（很可能也是唯一的）希望，是以世界超级大国的国力全力支持的开源体系——建立由中国主导和主投、知识产权成果完全开放的国际经济合作组织。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张投入资金研发芯片方案并无偿开放给所有国家生产，投资建设晶圆厂、封装厂、实验室以提供不包含利润的制造支持，并通过国际条约在合作国家之间建立对新行业标准、新操作系统的完全非盈利、非特定化支持。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者所说的开源不是源代码公开但控制权保留的资本主义式开源，而是作者放弃一切所有权、仅保留著作权的共产主义式开源，因此 RISC-V 并不在其列。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列出“开放知识主权联盟”条约实体的义务：认缴会员费用、提供知识产权准入优惠、五年后把联盟所持知识产权向全人类无条件开放、修改本国专利法与相关市场法规、投资联盟内公共机构与联合基础设施、贯彻联盟内部国际产业标准。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者列出条约实体的权利：在主权范围内无偿、无需授权地享有联盟所持知识产权；按出资份额参与收购清单审议、谈判小组组成、收购表决与授权收益分配；按约定价格使用联盟基础设施并参与争议审议；参与开源社区年度奖励名单与奖金分配；请求各条约实体在对非条约国家的知识产权谈判或纠纷中一致行动。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张由中国牵头和支持，团结大批发展中国家和进步发达国家组织更大规模的市场，对现有知识产权进行一次性赎买；拒绝赎买的实体将被这整个市场视为不可依赖的供应商而被拒绝和限制进入，严格程度可一直提升到禁止相关企业进入市场。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "基于自由交易原则，各现有专利巨头仍可保持一定领先和独有产权，但作者要借助该框架严格限制“注册一个算法收全人类几十年税”的现象。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "中国走资本竞争之路想要赶超美国依靠成熟资本制度与市场经济积累的近一个世纪优势，即使不是不可能，也是极其困难的。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理由之一是研发体系与底层经济制度严格绑定，中国因国情几乎不可能照搬；三心二意的“四不像”哪怕只有稍许效率损失，考虑到现实差距，追赶全程将付出极大代价，芯片产业之争足以成为星球大战计划的重演。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理由之二是独属自己的、知识产权充满技术秘密和专利保护的芯片业对任何人既是福利又是威胁，因此中国芯片产业即使有一天性能指标更优，也会因安全顾虑被相当大的市场弃而不用，全力以赴却自处“举一隅而敌全局”极其不利。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者由此提出胜战之策是完全改变游戏规则：不需要把第一流芯片卖给最高端客户、卖第一流价钱，只需做出可用的芯片送给全人类用；创造者的回报来自新生态的一次性奖励及人类史上的地位，不再来自专利权和先发优势的税金。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称中国人以辛勤劳动、沉重责任和劣势贸易地位积累的财富中有一部分用来为全人类永久的福利买单；帮助这个用自己财政无偿为世界基础设施买单的国家盈利就是帮助世界的每一个人，攻击它、剥夺它的盈利就是剥夺每一个人。", "evidence": ["E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议除军事工业之外，在一切会卡脖子的产业领域，把本来打算投入秘密研发、独立研发的资源有计划地、量力而行然而坚持不懈地转投向完全开源社区，完全避免掌握和垄断其成果。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称这一基本策略能釜底抽薪地、决定性地解决所面临的封锁问题，为中国的生产力带来全球市场无法剥夺的入场券，并以连续反问否认拒绝加入该秩序的合理理由。", "evidence": ["E24"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测该计划将理所当然赢得全人类最伟大的头脑：自称关心人类胜过自己的人将不得不解释为什么不通过这个新开源体系分享创造；资本主义百年先发优势在这宏大历史进程面前终究不过一缕青烟。", "evidence": ["E25"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测仅凭全球资本市场对历史倒向哪一边的预期，都将迫使美国降低对中国的遏制烈度；仅公布这一计划就足以重创 intel、高通等全部传统老牌垄断企业的股价，并给美国经济带来重大不确定性。", "evidence": ["E26"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这次不同于冷战、热战和贸易战，是以人类的名义、在尊重一切现有市场伦理的前提下对整个垄断制度宣战；任何不同意由极少数国家与精英向全人类无限征税这一制度的人类都是盟友。", "evidence": ["E27"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测走上这条路“中国威胁论”会被一次性送上黄泉之路并不可逆转地破灭；怀疑者的后代将使用这些产品长大并把“中国威胁论”视为历史上的疯狂，最终中国不再需要依赖航母和驱逐舰捍卫安全。", "evidence": ["E28", "E29"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称历史将中国牢牢困在与既有垄断体制无法调和的困境里，这既是危机也是无声的赋能；换一个视角，中国实际上是被“天命”指明去担当垄断者的敌人。", "evidence": ["E30", "E31"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者称一旦垄断者将要价抬高到中国作为开源受益者所获利益足以对冲研发风险和成本时，中国就会看到大量资助开源版本的好处——既解自己的饥渴，又砸碎威胁者的饭碗。", "evidence": ["E31"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称中国曾经、现在也仍然是以解放全人类为己任的国家，但不靠苏联式的铁与血，而靠实实在在的无法否认的对人类的热爱；并以“中国不做不行，而中国不做，谁做？”收束。", "evidence": ["E32", "E33"]}
   ],
   "argument_steps": [
    "提出语境：作者此前批评民间对芯片产业的盲目乐观，可能被误认为悲观（P001）。",
    "定义立场：相信中国芯片产业有巨大的希望；同时否定英特尔/高通式的国力孤注一掷与自有市场买单之路（P002、P003）。",
    "给出替代定义：唯一希望是以超级大国国力支持的开源体系与完全开放的国际经济合作组织（P004）。",
    "界定概念：共产主义式的开源＝放弃一切所有权、仅保留著作权；排除 RISC-V（P006）。",
    "列框架条款：条约实体的义务六条（P008-P014）与权利八条（P015-P023）。",
    "给方案概要并设边界：一次性赎买；拒绝者被市场排斥；自由交易原则下允许既有巨头保持领先，但限制算法专利收税（P024、P025）。",
    "给出不走资本竞争之路的两条理由（P026-P028）。",
    "转折结论：因此需要完全改变游戏规则，做可用芯片送全人类，回报改为一次性奖励与历史地位（P029-P033）。",
    "说明中国的付出与资源转向，并回应“会不会穷死”（P034-P037）。",
    "列出计划的多重好处：解封锁、聚人才、迫美降烈度、破“中国威胁论”（P038-P044）。",
    "收束：困境即赋能，中国被“天命”指为垄断者的敌人，靠对人类的热爱而非铁与血（P045-P048）。"
   ],
   "concept_usage": [
    {"term": "开源", "meaning": "本文特指作者放弃一切所有权、仅保留著作权的“共产主义式的开源”，区别于源代码公开但控制权保留的资本主义式开源；RISC-V 被明确排除。", "evidence": "P006", "ambiguity": "作者自设定义，与通行开源定义不同，容易误读。"},
    {"term": "开放知识主权联盟", "meaning": "作者设想的条约实体名称，成员以会费、市场准入优惠与专利法修改等义务，换取联盟所持知识产权的无偿使用与治理参与权。", "evidence": "P007", "ambiguity": "名称仅出现一次，组织形态、法律地位与决策机制本文未细说。"},
    {"term": "一次性赎买", "meaning": "由联盟组织更大市场对现有知识产权付费买断，替代按专利持续收费。", "evidence": "P024", "ambiguity": "赎买对象范围、定价方式与资金来源本文未说明。"},
    {"term": "弯道超车", "meaning": "作者用于指走美国模式老路赶超芯片产业领先者，并否定其可行性。", "evidence": "P003", "ambiguity": "无。"},
    {"term": "共产主义式的开源", "meaning": "作者用作其开源主张的自我定性，强调放弃所有权、仅保留著作权。", "evidence": "P006", "ambiguity": "政治修辞性定性，非既有制度术语。"}
   ],
   "examples_and_targets": [
    "英特尔（Intel）、高通：作者列举的传统老牌垄断企业，作为股价受冲击与专利垄断的例证（P003、P040）。",
    "RISC-V：作者用来界定其“开源”不含控制权保留模式的排除对象（P006）。",
    "上合组织成员国：出现在作者所否定的“纯靠自有或共同市场需求买单”道路的表述中（P003）。",
    "美国模式、成熟完善的资本制度与市场经济：作为被比较与否定照搬的对象（P003、P026）。",
    "星球大战计划：作者用类比说明芯片产业之争可能重演的历史参照（P027）。",
    "苏联式的铁与血：作者用来反衬其主张的对照材料（P047）。",
    "另一篇回答《中国大陆明明知道芯片不行，几十年前为什么不发展芯片？》：作者自引的前作语境（P001）。",
    "“中国威胁论”、航母与驱逐舰：作为作者预测将被消解的对象（P042、P044）。"
   ],
   "conditions": [
    "P004：以“世界超级大国的国力全力支持”为前提；“很可能也是唯一的”为作者自加限定。",
    "P024：赎买方案以中国牵头、发展中国家与进步发达国家参与、形成更大规模市场为条件；拒绝赎买者将被市场拒绝和限制进入。",
    "P025：以“自由交易原则”为前提，允许既有专利巨头保持一定领先和独有产权。",
    "P036：“除军事工业之外”的范围限定；资源转投要求“有计划”“量力而行”“坚持不懈”。",
    "P046：“一旦垄断者将要价抬高到……足以对冲研发风险和成本时”为触发条件。",
    "P026：“即使不是不可能，也是极其困难的”为程度限定。",
    "P038：反问中提及“花几千亿人民币”的规模假设。"
   ],
   "rhetoric_and_tone": "长篇论辩与倡议文体：以“我们”自称并直接对读者发话，多处连续反问（P038、P043、P048）；使用共产主义、解放、天命、黄泉之路、烈火战车、诸神之战、釜底抽薪等强修辞与历史叙事；对拒绝赎买者写明市场排斥的强制后果；结尾以“请从我中国始”“我们不会穷死”“中国不做不行，而中国不做，谁做？”等短句收束，带宣言与训诫语气。",
   "unresolved_questions": [
    "正文末段 P049 混入平台话题标签“科学答集/家族答集”，且 lexical 未覆盖该片段，是否为正文需人工确认。",
    "brief 在“走“凭借自”处截断，无法据 brief 补全；以 text 为准。",
    "联盟条约的法律形式、赎买资金规模与来源、定价与执行机制、对拒绝者限制进入市场的合法性，正文均未说明。",
    "RISC-V 被排除的具体理由仅以括号带过，未展开。",
    "作者引用的另一篇回答不在本批语料内，无法互证其“严厉批评盲目乐观”的具体内容。",
    "“天命”一词的使用是修辞还是作者的实际判断，正文未明说。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "恰恰相反，我相信中国芯片产业有希望，而且是巨大的希望。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "我根本不认为中国的芯片产业之路——甚至更广一些，IT产业全产业链之路——可以走美国模式的老路而实现弯道超车。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "中国摆脱芯片困局的最佳（很可能也是唯一的）希望，是以世界超级大国的国力全力支持的开源体系", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "我们投入资金，研发芯片方案，但无偿开放给所有国家生产", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P013", "quote": "5）对联盟内的公共机构进行投资——如建立联盟内的晶圆厂和芯片厂，或某些联合基础设施，向所有联盟成员的知识产权发展提供基础设施。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "我们指的是作者放弃一切所有权，仅仅保留著作权的共产主义式的开源（因此RISC-V并不在其列）。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "3）同意将联盟所持有的知识产权在五年后向全人类无条件开放。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P012", "quote": "4）同意根据条约原则对本国的专利法和相关市场法规进行相应修改。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P016", "quote": "在条约实体的主权范围内，联盟所持有的知识产权被认为是公开的、无偿的、无需授权的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P023", "quote": "8）请求各条约实体在与非条约国家的知识产权谈判或纠纷中采取一致行动。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P024", "quote": "由中国牵头和支持，团结大批的发展中国家和进步发达国家，组织一个更大规模的市场，对现有知识产权进行一次性赎买。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P024", "quote": "拒绝赎买的实体将被这整个市场视为不可依赖的供应商而被拒绝和限制进入", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P025", "quote": "但要借助这个框架严格的限制“注册一个算法收全人类几十年税”这种现象。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "中国走资本竞争之路想要赶超美国依靠成熟完善的资本制度和市场经济所积累起来的近一个世纪的累积优势，即使不是不可能，也是极其困难的。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P027", "quote": "中国因为自己的国情是几乎不可能照搬的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P027", "quote": "以至于芯片产业之争足以成为星球大战计划的重演。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P028", "quote": "这令中国的芯片产业即使有一天在性能指标上更为优胜，也会因为安全的顾虑而被相当大的市场弃而不用。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "这种全力以赴的诸神之战，却要自处举一隅而敌全局的局面，是极其不利的选择。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "因此，胜战之策需要完全的改变游戏规则。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P031", "quote": "我们只需要做出可用的芯片来，送给全人类用。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P032", "quote": "创造者的回报来自整个新生态的一次性奖励以及由此获得人类史上的地位，不再来自凭着专利权和先发优势向全人类收取的税金。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P035", "quote": "一个用自己的财政无偿为世界基础设施买单的国家，帮助它、让它盈利，就是在帮助世界的每一个人；攻击它、剥夺它的盈利，就是剥夺每一个人。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P036", "quote": "将本来打算投入秘密研发、独立研发的资源有计划的、量力而行然而是坚持不懈的转投向完全开源社区。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "这一基本策略能真正釜底抽薪的、决定性的解决我们所面临的封锁问题，彻底的为中国的生产力带来全球市场的无法剥夺的入场券。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P039", "quote": "这个计划将理所当然赢得全人类最伟大的头脑。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P040", "quote": "仅仅公布这一计划，就足以重创intel、高通等全部传统老牌垄断企业的股价", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P041", "quote": "这次，我们是以人类的名义，在尊重一切现有市场伦理的前提下，对整个垄断制度宣战。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P042", "quote": "“中国威胁论”就一次性被送上黄泉之路。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P044", "quote": "最终我们将不再需要依赖航母和驱逐舰来捍卫我们的安全。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P045", "quote": "历史将中国牢牢的困在了与既有垄断体制无法调和的困境里。这既是一种危机，也是一种无声的赋能。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P046", "quote": "中国实际上是在被天命指明去担当垄断者的敌人。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P047", "quote": "但我们不是要靠苏联式的铁与血，而是要靠实实在在的无法否认的对人类的热爱。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P048", "quote": "中国不做不行，而中国不做，谁做？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["产业政策", "半导体产业", "国际政治经济", "知识产权制度", "开源运动"],
   "issue_candidates": ["中国芯片产业前景", "美国模式与弯道超车", "专利制度与开源替代", "国际经济合作组织构想", "技术封锁"],
   "text_function_candidates": ["答疑", "倡议与方案设计", "论辩"],
   "object_candidates": ["中国", "美国", "Intel", "高通", "RISC-V", "上合组织成员国", "苏联"],
   "working_keywords": ["开源", "共产主义式的开源", "开放知识主权联盟", "一次性赎买", "专利制度", "弯道超车", "星球大战计划", "中国威胁论"]
  },
  "notes": "全文 49 段已读完，无图片节点，status=read。要点：①末段 P049 为平台话题标签“科学答集/家族答集”，lexical 未覆盖（skeleton divergence=true），已计入正文段落但属平台字段混入；②brief 在“走“凭借自”处截断；③本篇为方案倡议型长文，含大量条件与反问，已保留限定语气与强制条款；④作者自引的前作不在本批，未作互证。"
 },
 "3e15a2e8": {
  "analysis": {
   "question_context": "提问者（Q001）问“艺术是否会终结于哲学？”，即担心/追问艺术会不会在哲学发展之下走向终结。作者以定义—推演的方式回答：先界定艺术的本质是创造、创造的本质是对现状的反叛，再说明反叛无论成败都对哲学有贡献、哲学本身就是一种思维的艺术，由此否定“艺术终结于哲学”，并把终结关系反转（若艺术终结，哲学才终结）。提问者的担忧与预设属于提问者，作者的回答并不接受该预设。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "界定艺术的本质是创造，创造的本质是对现状的反叛；这种反叛从两个方向上同时对现状作出贡献。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "分说两个方向：反叛成功则成果加入现状，使现状更新为更丰富、更值得信赖、更值得欣赏的新现状；失败则让人更深刻认识到现状的正确性和可依赖性；无论哪种都对哲学作出贡献。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "断言哲学本身就是一种思维的艺术，因此艺术不可能因为哲学发展而终结——艺术就是“哲学的发展”本身。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "反转终结关系：逻辑上哲学倒会因为艺术的终结而终结；又因人类是反叛性深入骨髓的存在、“永不停歇的扬弃现有认知”是智慧发展的基本形式与思维本质，只要有一个人不死，艺术便一天不灭、哲学便多一天活力。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术的本质是创造，创造的本质是对现状的反叛。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反叛无论成功还是失败都对现状作出贡献：成功使其成果加入现状并更新现状，失败则让人更深刻认识到现状的正确性和可依赖性；两者都会对哲学作出贡献。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "哲学本身就是一种思维的艺术。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "艺术不可能因为哲学发展而终结，因为艺术就是“哲学的发展”本身。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在逻辑上，哲学反倒会因为艺术的终结而终结。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“永不停歇的扬弃现有认知”是人类智慧发展的基本形式，也是人类思维的本质；人类但有一人不死，则艺术便有一天不灭，哲学也便有多一天的活力。", "evidence": ["E8", "E9"]}
   ],
   "argument_steps": [
    "定义艺术：艺术的本质是创造（P001）。",
    "定义创造：创造的本质是对现状的反叛，且反叛从两个方向同时对现状作出贡献（P001、P002）。",
    "展开两个方向：成功→现状被更新；失败→更深刻认识现状的正确性与可依赖性（P003、P004）。",
    "合题：无论成败都会对哲学作出贡献（P005）。",
    "给出判断：哲学本身就是一种思维的艺术（P006）。",
    "结论：艺术不可能因哲学发展而终结，因为艺术即“哲学的发展”本身（P007）。",
    "反向推论：逻辑上哲学倒会因艺术的终结而终结（P008）。",
    "补充前提：人类反叛性深入骨髓、“永不停歇的扬弃现有认知”是智慧发展的基本形式，故艺术不灭、哲学有活力（P009）。"
   ],
   "concept_usage": [
    {"term": "艺术", "meaning": "本文中等于创造／对现状的反叛，是“哲学的发展”本身，不因哲学发展而终结。", "evidence": "P001", "ambiguity": "未区分艺术、艺术作品与艺术家；未讨论具体艺术门类。"},
    {"term": "创造", "meaning": "对现状的反叛，其结果无论成败都构成对现状与哲学的贡献。", "evidence": "P001", "ambiguity": "与“反叛”近乎同义替换，未给出可操作判据。"},
    {"term": "反叛", "meaning": "对现状的否定性动作，分成功与失败两种走向，均使现状或认知得到澄清。", "evidence": "P002", "ambiguity": "未说明反叛的动机来源与评价标准。"},
    {"term": "哲学", "meaning": "本文中被界定为一种思维的艺术，且其终结以艺术的终结为条件。", "evidence": "P006", "ambiguity": "“哲学”与“思维的艺术”的关系未展开。"},
    {"term": "扬弃", "meaning": "作者以“永不停歇的扬弃现有认知”描述人类智慧发展的基本形式与思维本质。", "evidence": "P009", "ambiguity": "沿用哲学术语的日常用法，未作界定。"}
   ],
   "examples_and_targets": [
    "本文未使用具体人物、事件、机构或数据；论证以“艺术”“创造”“反叛”“现状”“哲学”“人类”等抽象概念为材料。"
   ],
   "conditions": [
    "P008：“逻辑上”为明确限定，表示这是逻辑推论而非现实预言。",
    "P009：“人类但有一人不死，则艺术便有一天不灭”为条件式表述，艺术与哲学的不灭以人类存续为条件。",
    "P002：“从两个方向上同时对现状作出贡献”为作者自设的完备二分。"
   ],
   "rhetoric_and_tone": "短论体，仅九段；定义—推演—反转结构清晰，使用“事实上”“所以”“逻辑上”“幸亏”等推理连接词；结尾以“人类但有一人不死，则艺术便有一天不灭”式的对仗断言收束，语气笃定而带乐观；无例证、无引文、无对话对象。",
   "unresolved_questions": [
    "brief 在“无论哪个，都会对哲学”处截断，只能以 text 为准。",
    "正文仅约 310 字，未标记“未完待续”，是否完整版本无法由本文判断。",
    "“艺术即哲学的发展本身”“哲学是思维的艺术”两处断言的依据未展开。",
    "“两个方向”是否穷尽反叛的全部结果，本文未论证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "艺术的本质是创造，创造的本质是对现状的反叛。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "要么它成功了，其成果加入到了现状之中，使得现状被更新为更丰富的、更值得信赖的、更值得欣赏的新现状；", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "要么它失败了，从而让人更深刻的认识到现状的正确性和可依赖性。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "无论哪个，都会对哲学作出贡献。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "事实上，哲学本身就是一种思维的艺术。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "所以艺术是不可能因为哲学发展而终结的——因为艺术就是“哲学的发展”本身。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "逻辑上，哲学倒是会因为艺术的终结而终结。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "“永不停歇的扬弃现有认知”是人类智慧发展的基本形式，也是人类思维的本质。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "人类但有一人不死，则艺术便有一天不灭，哲学也便有多一天的活力。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["艺术哲学", "美学", "思维方法"],
   "issue_candidates": ["艺术是否会终结于哲学", "艺术与哲学的关系", "创造与反叛"],
   "text_function_candidates": ["答疑", "哲学短论", "概念界定"],
   "object_candidates": [],
   "working_keywords": ["艺术", "创造", "反叛", "现状", "哲学", "扬弃"]
  },
  "notes": "全文 9 段（约 310 字）已读完，无图片节点，status=read。brief 在“无论哪个，都会对哲学”处截断；正文未标“未完待续”，但篇幅极短且无例证，是否完整无法由本文判断。作者对提问者的“终结于哲学”预设持否定态度。"
 },
 "251d8f00": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何管教写作业拖拉的孩子？”，寻求管教办法。作者给出“基本思路”，分两个策略：先做全家彻底整理并维持秩序（居住环境塑造人格），再从学校教育“概念正确”门槛与孩子快感机制的错位出发，主张改用页面工整、字迹、桌面与时间管理等可直觉判断的指标重建“阶段价值观”。作者自设框架与原理，并在文中说明“另找时间来解释这个策略的原理”，末尾标注“（未完，待续）”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "开场给出基本思路：步骤不复杂，可发散；第一步是全家大扫除、做彻底整理。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012"], "summary": "彻底整理的具体标准：闲散物资收拣干净；存储空间每格编号、中等以上物件标签指定收纳地点；工具改套装；衣物归类标签；外露散置物品用轮廓线定位；打开柜门即见秩序；不兼容物件找位、出售抛弃或替换；建议浅抽屉、一屉一层；家中不应有不在其位的东西。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "第二步是维持秩序：负担沉重、不要高估管理能力，有条件请钟点工或专业家政按标定系统维护；强调“维持，维持，维持”，一乱来就前功尽弃，应提高到“关系到子女未来”的高度看待；称坚持一个月即可观察到孩子拖延作业明显改善，并提示另找时间解释原理、先试试看。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027"], "summary": "原理解释：养移体、居移气；人格类似非牛顿流体，猛击则硬、恒定方向的选择压力则可塑；稳定居住环境是塑造性格的魔法接口，家风—家居—家生形成环境选择压力；性格如内部竞争、不断变异的种群，教育即塑造客观环境让适应版本成为主要性状。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "为何以居住样式为重心：言语教训信息量很低（念一遍只重复很少字节，表情、语气、姿势数据也有限），而居住环境的信息每分每秒都在写入人格；若环境信息与口头理念矛盾，后者会被不断洗掉，因为前者永不止歇而家长要上班、加班、交际；故孟母三迁，并反问家中各空间是否站在家长一边。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062"], "summary": "第二策略从问题说起：学校教育的陡升台阶（很短时间内要求很小的孩子追求概念正确理解，并以其为学术表现的唯一标准）使所有孩子在此阶段严重受挫；孩子快感机制更接近动物、与“概念正确感”无关，于是像用饼干训练狗听哨声那样用社会反馈补偿；以无法理解的外星人反馈作类比，指出最快让反馈者安静的办法是乱排组合，且许多反馈其实针对“你为什么不如别人”；家长很难因孩子“做对这么点东西”产生真诚奖励冲动，导致只有前三分之一获得有效正反馈，后三分之二得到失望、焦虑与无意识报复，而背着石头逆袭概率很小。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071"], "summary": "提出对策：重建“什么是值得高兴、值得奖励”的阶段价值观，且须是父母子女都能本能体察的共同价值；举例以作业页面工整、字迹美妙、桌面与时间管理而非正确程度为主要指标，理由是识别视觉对称与秩序是先天机制、快感直接而原始，抽象错误无具体感，而格式差异显著且可普遍共识。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081"], "summary": "后果推演：对孩子而言因格式不工整被批评可理解且可努力避免，不易产生无望挫折感；对家长老师而言格式与字迹是学习态度的明证，可抑制焦虑并带来更多耐心，有助于孩子迈过从具象敏感到抽象敏感的门槛；以“推3把/6把/8把才暴跳”作类比，称子女会多得到5次有效推动，统计上更易迈过铁门槛、排名靠前并获得“排名靠前红利”，有可能扭转局面。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P082"], "summary": "正文以“（未完，待续）”结束，第二策略尚未收尾。", "role": "context"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出的基本思路是：步骤不复杂、可发散，第一步先全家大扫除、做彻底整理，第二步维持秩序。", "evidence": ["E1", "E2", "E8"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定的“彻底整理”标准包括：存储空间每一格编号、中等以上物件用标签指定收纳地点、工具改套装、衣物有归类标签、外露散置物品沿轮廓定位，打开任何柜门或存储处都应看到计划后的秩序、物品各归其位。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切不能兼容该体系的物件，要么为它找到恰当的计划位置，要么出售抛弃或替换成能计划收纳的替代物；作者建议用浅抽屉而不是深抽屉，因为深抽屉对分格极不友好、浪费空间，一个抽屉只宜放一层东西。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家里不应该有未在使用状态而不在其位的东西存在。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "维持秩序是很沉重的负担，不要高估自己的管理能力；有条件的话建议请钟点工或专业家政按标定系统维护，没有条件就要靠自己。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以训诫口吻强调“维持，维持，维持”：一乱来就会前功尽弃，应提高到“关系到子女未来”的高度看待这个问题。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "坚持一个月，就会观察到孩子在拖延作业问题上有明显的改善。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这一策略背后的原理是“养移体、居移气”；人的人格特性类似非牛顿流体——猛击则硬如钢铁，而润物细无声、推力方向恒定的选择压力可使其像熔融玻璃一样变成任意形状。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的稳定居住环境是一种塑造人的性格的魔法接口：什么样的家风就会有什么样的家居，这些家居支持着什么样的“家生”，而“家生”会对居住者的性格形成环境选择压力。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的性格（尤其是小朋友的性格）犹如不断变异、在内部互相竞争的种群；教育从这个意义上说就是要塑造一个客观环境，让那些适应的版本获得优势并成为主要性状表现。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把重心放在居住样式上，是因为被父母看得非常重要的言语教训信息量很低：把这篇文字念一遍只重复了寥寥无几的字节，加上表情、语气、姿势等数据后传递的实际信息量也非常有限；而居住环境里凝聚的信息每分每秒都在作用，每一次交互与环顾都是环境信息对人格的一次写入。", "evidence": ["E17", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果环境写入的信息与家长用肢体和口头语言表达的理念相矛盾，那么后者写入的信息会不断被洗掉，因为前者永不止歇，而家长要上班、加班、出门交际。", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以孟母要三迁；作者反问读者是否确信客厅、书房、卧室、厨房、卫生间、庭院站在自己这一边，并提醒“它们的声音比你大，它们的时间可比你多”。", "evidence": ["E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "目前的学校教育有一个非常大的陡升台阶——在很短时间内就要求很小的小朋友追求对概念的正确理解，并以概念理解正确与否作为学术表现的唯一衡量标准；这对需要KPI的教育系统可以理解，但造成严重问题：事实上所有孩子都会在这个阶段受到严重挫折。", "evidence": ["E23", "E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "孩子得到正反馈的机制几乎与“概念正确感”无关，其快感机制更接近动物（甜美味道、食物香味、柔软顺滑的触觉、有节奏且协调的声音、运动快感等），无法从“正确计算出1+1=2”中获得直接快感；于是人们试图像用饼干训练狗听哨声那样，用社会关系的正反馈和负反馈来弥补其快感机制的“缺陷”。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问指出：孩子没有学会计算，就无法知道如何通过计算发现“计算错误”。", "evidence": ["E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以外星人示范与反馈的类比说明：在完全不懂的符号系统里，最快让反馈者安静下来的可靠手段是随便排列组合、让其尽快耗尽能量；更糟糕的是，很多反馈并不是对做对/做错题，而是对“你为什么不如别人”这一事实。", "evidence": ["E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "由于家长对十以内加减法、基本拼音、基本字形的熟悉程度远胜孩子，实际上很难因子女“做对了这么点东西”而产生真实的、真诚的奖励冲动；真诚奖赏常常本质上来自孩子相对同龄人、同班同学的优异表现，于是宏观上只有成绩较好的前三分之一能真正得到有效正反馈，后三分之二得到的是失望、焦虑甚至父母无意识的报复。", "evidence": ["E31", "E32", "E33"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不断累积的失望情绪几乎只有靠子女扛着心理负担奋发图强、逆转排到前面才能改观；但大家都在往前跑而孩子还背着一块石头，这种逆袭的概率不大。", "evidence": ["E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "问题的关键在于父母和子女都要重新建立“什么是值得高兴的、值得奖励的东西”的阶段价值观：不能是“题做对了”和“在班里排名靠前”，而要是子女和父母都能本能体察到的某种共同价值。", "evidence": ["E35", "E36"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者举例主张以作业的页面工整程度、字迹的美妙程度和作业期间的桌面管理与时间管理水平——而不是作业的正确程度——作为主要考察指标，因为识别视觉对称性、秩序性对大脑是不需要学习就天然拥有的机制，且这些特性带来的快感直接而原始；而抽象的计算错误没有具体感、非先天，格式差异却是显著的、直觉地根植于大脑基本处理机制的、人类可以达成普遍共识的。", "evidence": ["E37", "E38", "E39", "E40"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对孩子而言，因把算式写得格式不整而被批评可以理解、也可通过有效努力避免，不易产生“反正无论如何都没办法避免被骂”的无望挫折感；对家长和老师而言，格式整齐与字迹工整是学习态度的明证，可在很大程度上抑制“你怎么这么差劲”的焦虑感，从而更有耐心，帮助孩子迈过从具象敏感到抽象敏感的门槛（对抽象错误的敏感是对抽象概念的理解的最实在证据）。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者以“推三把／六把／八把才暴跳”的类比预测：实施以工整优美为优先评价标准后，子女会比其他人多得到5次有效推动，统计上比较容易迈过这道铁门槛、排名比较靠前，从而有更大机会获得“排名靠前红利”和额外的“我为你骄傲”的社交性奖励，有可能扭转局面。", "evidence": ["E44", "E45", "E46"]}
   ],
   "argument_steps": [
    "给出基本思路并说明步骤不复杂（P001、P002）。",
    "第一步：全家大扫除、彻底整理（P003）。",
    "界定彻底整理：编号、标签、套装工具、衣物标签、轮廓定位、柜内秩序（P004-P010）。",
    "处理不兼容物件并给出浅抽屉建议；规定家中不应有不在其位之物（P011、P012）。",
    "第二步：维持秩序，评估负担并提出家政协助方案（P013、P014）。",
    "强化维持要求：一乱即前功尽弃，提高到“子女未来”的高度（P015）。",
    "给出可观察效果：坚持一个月可见拖延改善（P016）。",
    "补充原理：养移体、居移气；人格如非牛顿流体；稳定居住环境是塑造性格的接口（P019-P025）。",
    "把性格视为竞争种群，教育即环境选择（P026、P027）。",
    "比较言语教训与居住环境的信息量，指出环境每分每秒写入，故要孟母三迁（P028-P041）。",
    "转入第二策略：学校教育的概念正确门槛使所有孩子受挫（P042-P044）。",
    "说明孩子快感机制与“概念正确感”无关，以及社会化反馈补偿的失灵（P045-P051）。",
    "以外星人反馈类比说明反馈信号不可解时的行为后果（P052-P057）。",
    "指出家长难以产生真诚奖励冲动，正反馈只覆盖前三分之一（P058-P060）。",
    "指出累积失望难以逆转、逆袭概率小（P061、P062）。",
    "提出重建阶段价值观，并以工整、字迹、桌面与时间管理为主要指标（P063-P071）。",
    "推演该标准对孩子与家长的双向好处及统计后果（P072-P081）。",
    "标注未完待续（P082）。"
   ],
   "concept_usage": [
    {"term": "彻底整理", "meaning": "全家闲散物资收拣干净并建立可定位的收纳体系：编号、标签、套装、轮廓定位，使物品各归其位。", "evidence": "P006", "ambiguity": "与普通“收拾”的界线由作者自定，未给完成标准。"},
    {"term": "养移体、居移气", "meaning": "作者用来概括居住环境对人格的塑造作用。", "evidence": "P020", "ambiguity": "引用式熟语，未注明出处与适用范围。"},
    {"term": "非牛顿流体", "meaning": "作者类比人格特性：猛击变硬、持续恒定方向的选择压力可使其改变形状。", "evidence": "P021", "ambiguity": "类比未给出经验依据与限度。"},
    {"term": "家生", "meaning": "出现在“家风—家居—家生—居住者性格”链条中，作者用以指称家居所支持、并对居住者性格形成选择压力的中间项。", "evidence": "P025", "ambiguity": "疑为笔误或生僻用法，具体所指不明。"},
    {"term": "具象敏感／抽象敏感", "meaning": "作者用来说明孩子跨越“对抽象错误的敏感”这一门槛；称对抽象错误的敏感是对抽象概念的理解的最实在证据。", "evidence": "P074", "ambiguity": "术语为作者自造，未给判据。"},
    {"term": "阶段价值观", "meaning": "父母与子女共同重新建立“什么是值得高兴、值得奖励的东西”的评价标准。", "evidence": "P063", "ambiguity": "未说明如何在校方评价体系不变时落地。"},
    {"term": "排名靠前红利", "meaning": "排名靠前所带来的额外社交性奖励（如“我为你骄傲”）。", "evidence": "P080", "ambiguity": "以引号标示的自创说法，未界定范围。"}
   ],
   "examples_and_targets": [
    "淘宝定制标签纸、书内页标签、水洗标、小布标、不干胶轮廓贴：作者给出的具体操作材料（P006、P008、P009）。",
    "浅抽屉与深抽屉的比较：作者用作收纳方式的例证（P011）。",
    "孟母三迁：作者引用的历史典故，作为环境塑造人的证据（P038）。",
    "1+1=2 与“3 x 4 - 1 = 10”“3x4 - 1 = 10”：作者用作抽象正确性与格式差异的对照例（P046、P067、P069、P070）。",
    "外星人／外星怪兽：作者自设的类比场景，说明不可解反馈下的行为（P052、P053、P055、P057）。",
    "“用饼干训练狗听哨声”：作者用以类比社会性正负反馈的作用方式（P047）。",
    "KPI 教育系统：作者用以解释学校要求概念正确的原因（P044）。"
   ],
   "conditions": [
    "P011：不兼容物件须先“找到恰当的计划位置”，否则出售抛弃或替换。",
    "P014：请钟点工或专业家政维护以“有条件的话”为前提，没有条件则靠自己。",
    "P016：改善以“坚持一个月”为时间条件。",
    "P022：人格可塑以“润物细无声的采取有效的、推力方向恒定的选择压力”为条件。",
    "P036：口头理念被洗掉以“环境信息与之矛盾”为条件。",
    "P045：孩子快感机制“更接近”动物而非“等同于”，并列举多种触发物。",
    "P059：正反馈覆盖范围用“往往只是成绩较好的前三分之一”限定。",
    "P081：“这有可能扭转局面”为或然判断。",
    "P082：正文标注“（未完，待续）”。"
   ],
   "rhetoric_and_tone": "长文答疑兼经验总结，语调训诫与劝导并用：大量“不要……”“记住……”“请提高……的高度”式祈使句；以“维持，维持，维持”重复强调；用外星怪兽、饼干训练狗等夸张类比与“吼吼吼吼吼！！！！”“F*ck，这真的太费耳朵了。”等口语化插话制造戏谑效果；多处反问（P040、P051、P062）向家长施压；对家长既有同情也有批评（如“无意识报复”）。",
   "unresolved_questions": [
    "正文以“（未完，待续）”结束，第二策略未收尾，缺少完整的实施步骤与结论。",
    "P025 的“家生”一词在“家风—家居—家生”链条中疑为笔误或生僻用法，需核对原版本。",
    "P067—P071 用两行算式的格式差异作例，纯文本只能看出空格差异，原页面排版差异无法辨明，需核对原始页面。",
    "P017“另找时间来解释这个策略的原理”与 P019“现在我们来解释一下背后的原理”显示文本可能拼接了不同时间的段落，版本关系未说明。",
    "标题“拖拉机”与正文内容（管教写作业拖拉的孩子）的关系未在正文说明。",
    "“非牛顿流体”“种群变异”等类比均为作者自设，未提供经验依据或适用范围。",
    "“坚持一个月即明显改善”的效果断言未说明依据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我给你一个基本思路，你可以考虑发散开来。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "首先，全家大扫除，做彻底整理。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "而是全家的存储空间的每一个格子都做了编号，每一件中等以上大小的物件都有标签指定收纳地点。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P010", "quote": "打开任何一个柜门，都应该看到计划后的秩序；打开任何一个存储处，都应该看到物品各归其位。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P011", "quote": "一切不能兼容这个体系的物件，要么为它找到恰当的计划位置，要么出售抛弃，或者替换成能计划收纳的替代物", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "建议使用浅抽屉而不是深抽屉", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "家里不应该有未在使用状态而不在其位的东西存在。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "完成彻底的规划之后，进入第二步——维持住这个外貌。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "这是很沉重的负担，不要高估自己的管理能力。有条件的话，建议请钟点工或者专业家政按照你的标定系统进行维护。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "记住，你一乱来，就会前功尽弃。请提高到“关系到子女未来”的高度去看待这个问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "坚持一个月，你就会观察到你的孩子在拖延作业问题上有明显的改善。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "其实道理并不复杂，那就是养移体、居移气。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P022", "quote": "但你如果润物细无声的采取有效的、推力方向恒定的选择压力，你会发现它就如熔融的玻璃，可以柔顺的变成任意的形状。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "人的稳定居住环境是一种塑造人的性格的魔法接口。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "什么样的家风，就会有什么样的家居，而这些家居就支持着什么样的家生，这家生会对居住者的性格形成环境选择压力。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P027", "quote": "所谓的教育，从这个意义上说，就是要塑造一个客观环境，让那些适应的版本获得优势，成为ta的主要性状表现。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P029", "quote": "因为被父母们看得非常重要的言语的教训，其实信息量是很低的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P035", "quote": "ta和这个环境发生的每一次交互，对这个环境的每一次环顾，都是环境信息对ta的人格的一次写入。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P036", "quote": "如果这个信息写入的内容和你用肢体和口头语言表达的理念是矛盾的，那么你用后者所写入的信息会不断的被洗掉。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P038", "quote": "所以孟母要三迁。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P041", "quote": "我可提醒你——它们的声音比你大，它们的时间可比你多。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P043", "quote": "目前的学校教育有一个非常大的陡升台阶，就是在很短的时间内，就要求很小的小朋友们开始追求对概念的正确理解，并且以概念的理解正确与否作为学术表现的唯一衡量标准。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P044", "quote": "事实上所有的孩子都会在这个阶段受到严重挫折。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P045", "quote": "孩子们得到正反馈的机制几乎与“概念正确感”无关。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P046", "quote": "ta们无法从“正确计算出1+1=2”之中获得直接的快感。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P047", "quote": "于是我们试图像用饼干训练狗听哨声那样，用社会关系的正反馈和负反馈来弥补ta们自身快感机制的“缺陷”。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P051", "quote": "ta们没有学会计算，ta们怎么知道如何通过计算发现“计算错误”？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P053", "quote": "最快让外星怪兽安静下来的可靠手段，就是随便排列组合，让ta们最快的耗尽能量，哑着嗓子委顿在地。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P055", "quote": "很多外星人甚至都不是在对做对题/做错题给反馈，而是在对“你为什么不如别人”这个令人沮丧的事实做出反馈。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P058", "quote": "所以实际上很难因为子女“做对了这么点东西”而产生多少真实的、真诚的奖励冲动。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P059", "quote": "于是从宏观上一开始就决定了会在这个阶段真正得到有效正反馈激励的孩子往往只是成绩较好的前三分之一。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P060", "quote": "后三分之二常常得到的是负反馈——是时不时的难以抑制的失望、是焦虑、甚至是来自父母的无意识报复。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P062", "quote": "问题是大家都在往前跑，你还背着一块石头，这种逆袭的概率能有多大呢？", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P063", "quote": "所以，问题的关键在于不论是父母还是子女，都要重新建立“什么是值得高兴的、值得奖励的东西”的阶段价值观。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P064", "quote": "而要是子女和父母都能本能的体察到的某种共同的价值。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P065", "quote": "以作业的页面工整程度、字迹的美妙程度和作业期间的桌面管理、时间管理水平——而不是作业的正确程度——作为主要的考察指标。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P066", "quote": "因为识别视觉上的对称性、秩序性对人的大脑而言是不需要学习就天然拥有的机制，并且这些特性带给人的快感是直接而原始的。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P067", "quote": "3 x 4 - 1 = 10 的错误是抽象的，是没有具体感的，也是非先天的。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P071", "quote": "之间的差异却是显著的、直觉的根植于大脑的基本处理机制的，人类可以达成普遍共识的。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P072", "quote": "对小朋友而言，因为把3 x 4 - 1 = 10 写成3x4 - 1=1 0而被批评，是可以理解的，也是可以通过有效的努力来避免的。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P073", "quote": "而对家长（包括老师）而言，格式的整齐和字迹的工整本身是显而易见的学习态度的明证，这在很大程度上可以抑制“你怎么这么差劲”的焦虑感。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P074", "quote": "这种从无意识的语气、肢体语言里传递出来的耐心对真正的向小朋友提供助力迈过从具象敏感到抽象敏感（对抽象错误的敏感是对抽象概念的理解的最实在证据）的门槛有很大的好处。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P078", "quote": "你的子女会比其他人多得到5次有效推动。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P079", "quote": "从统计学上来讲，ta比较容易迈过这道铁门槛，ta也比较容易排名比较靠前。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P080", "quote": "于是你有更大机会获得“排名靠前红利”，对ta给予额外的“我为你骄傲”的社交性奖励。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭教育", "儿童心理", "收纳与生活管理", "学校教育批评"],
   "issue_candidates": ["孩子写作业拖延", "居住环境与人格塑造", "概念正确门槛与早期挫折", "奖励与评价标准重建", "家校评价错位"],
   "text_function_candidates": ["答疑", "经验总结", "操作建议", "训诫"],
   "object_candidates": ["孩子", "父母", "老师", "学校", "钟点工与专业家政", "孟母"],
   "working_keywords": ["彻底整理", "养移体、居移气", "非牛顿流体", "环境选择压力", "具象敏感", "抽象敏感", "阶段价值观", "排名靠前红利", "未完待续"]
  },
  "notes": "全文 82 段已读完，无图片节点，status=read。要点：①正文以“（未完，待续）”结束，第二策略未收尾；②标题“拖拉机”与正文关系未说明；③P025“家生”疑为笔误或生僻用法；④P067—P071 的算式格式例依赖原页面排版，纯文本仅能看出空格差异；⑤P017 与 P019 显示文本可能由不同时间段落拼接。以上均已在 unresolved_questions 登记，未作补全。"
 },
 "c57b5add": {
  "analysis": {
   "question_context": "提问者（Q001）问“真正的艺术，真的是能雅俗共赏的吗？”，其预设是“真正的艺术”与雅俗共赏之间存在关系。作者直接否定该预设：艺术与能不能雅俗共赏无关，并进一步把“人能否表决艺术”颠倒为“艺术决定着人”，以“艺术与美无关、只与真有关”“艺术的本质是【真】的另一种可能”重述艺术判准，最后把“美的客观性”称为权术把戏，把提问称为被扭曲后的“伤情展示”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "直接否定问题预设：艺术与能否雅俗共赏无关；雅俗都不能赏不见得不是艺术，雅俗都赏不见得不是垃圾；用雅俗能否赏谈艺术，是把艺术当成可由人类表决的造物。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009"], "summary": "反向命题：不是人决定艺术，而是艺术决定人；艺术品是造物而艺术不是，艺术是天成、艺术家只是矿工；以自然规律被实验家揭示、无人能自称发明万有引力定律、莫奈与印象主义、牛顿为类比；并把把知识归功于祖师爷斥为偶像崇拜的恶习。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "提出艺术判准：艺术不在乎人类是否欣赏，人类学会欣赏艺术则自己能得救；艺术与美无关、只与真有关，艺术的本质是【真】的另一种可能；美感只是观赏者的私人感受；把美学观点政治化才会产生“人类不得不普遍承认的客观存在”之说，美的“客观性”是权术把戏，问出该问题是提问者被扭曲的结果，属“伤情展示”，应指出问题严重而非安慰。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "以“忠于真实”区分艺术与非艺术：艺术只需忠于真实；专事“表达艺术家内心感受”的所谓艺术有极高贬值风险、是针对艺术盲的骗局；分享视角与真实是艺术，只让人知道自己的感受是污染和狂妄；诉诸美感习惯的“视觉糖果”如黄泥裹糖霜，最后真正的艺术是解放人类对真实的狭隘认知，觉得美只是被解放者的感激之情。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "艺术和能不能雅俗共赏无关；雅俗都不能赏，并不见得就不再是艺术，雅俗都赏也不见得就不是垃圾。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用雅俗能不能赏来谈论艺术，是在把艺术视为人类的造物，可以由人类自己作出表决。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不但人不能决定艺术，相反，是艺术决定着人。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不应因为艺术品看起来是人画出来雕出来的就以为艺术是人的产物：艺术其实是天成，人类的艺术家只不过是矿工，艺术作品才是人类的造物，艺术不是。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术由艺术作品承载和揭示，犹如自然规律被实验家揭露和展示；没有人敢说万有引力定律是他发明或创造的。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "莫奈借着睡莲探索和展示了印象主义，但印象主义先就存在，莫奈只是以画笔为锹把它刨出来；一旦印象主义艺术被发觉，“印象主义”四字就不再归莫奈说了算，就像牛顿不能把万有引力定律改掉一样。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "将知识归功于祖师爷、把祖师爷捧为主宰该项知识的神、认为一项知识成就是祖师爷的创造和私产，是极其等而下之的偶像崇拜的恶习。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术自身根本不在乎人类欣赏不欣赏；是人类如果能学会欣赏艺术，人类自己能得救。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术与美无关，只与真有关；艺术的本质，是【真】的另一种可能。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "因为它是由真转生，人类无论最初对它是什么感情，最后一定会发展出对它的拥抱；不肯拥抱一切真实的人将被狭隘的认知囚禁在名为“现实”的地牢里。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美感只是人类拥抱艺术时产生的私人感受；这份感情不是艺术的附属属性，而是人的附属属性，“美”只是观赏者的私事。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "只有将某种美学观点政治化、变成抱团结伙的胸章绣箍时，才会有人非要举着刀枪棍棒逼人们承认其感受版本是“人类不得不普遍承认的客观存在”；问出这个问题本身就是提问者被扭曲了的结果，美的“客观性”是一种权术把戏。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "认为“艺术必然美，如果没有任何一个人觉得它美，它就一定不是艺术”并进而问“艺术是不是应该做到雅俗共赏”，本身就是一种伤情展示；人该做的不是安慰，而是指出这事问题很大、赶紧上医院。", "evidence": ["E17"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术只需要忠于真实。", "evidence": ["E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "有些“艺术”专注“表达艺术家内心的感受”，这类艺术品不管目前如何风头十足，几十年后有极高的贬值风险，实际上是一种针对艺术盲的骗局——只需与一些没有良知的写手串通即可。", "evidence": ["E19"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "分享我的视角、给你另一个角度的真实，这是帮助，是艺术；不在乎真实、只是让你知道我的感受，这是污染和狂妄。", "evidence": ["E20", "E21"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "诉诸人的美感习惯、装点成视觉糖果，只是给一团黄泥裹上糖霜；人吃下去即使不被毒死，那点所谓的营养也与直接吃糖当饭无异，除了肥胖和病患没有营养；这种“糖果师”在不知何为美食的人群里声名鹊起，是人类的悲哀。", "evidence": ["E22"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "虚掷的时间和快感的幻灭到最后会告诉你们什么叫对，什么叫错。", "evidence": ["E23"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的艺术是用来解放人类对真实的狭隘认知的，不是让人觉得美的；觉得美只是被解放的奴隶的感激之情，在被解放之前他们和父祖还很可能被奴隶主教导着认为“这帮人是要来共产共妻的”。", "evidence": ["E24", "E25"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称对真正的艺术何止不“赏”，不厌不恨都是好的了。", "evidence": ["E26"]}
   ],
   "argument_steps": [
    "否定问题预设：艺术与能否雅俗共赏无关（P001、P002）。",
    "指出该问法把艺术当作可由人类表决的造物（P003）。",
    "反转命题：不是人决定艺术，而是艺术决定人（P004）。",
    "给出理由：艺术是天成、艺术家只是矿工，艺术作品才是造物（P005、P006）。",
    "以自然规律被揭示、无人能自称发明万有引力定律作类比（P007）。",
    "以莫奈与印象主义、牛顿为例，说明艺术被发现后不再归属发现者（P008）。",
    "把“知识归功祖师爷”判为偶像崇拜的恶习（P009）。",
    "指出艺术不在乎人类欣赏与否，人类学会欣赏则自己能得救（P010）。",
    "给出正面判准：艺术与美无关、只与真有关，本质是【真】的另一种可能（P011-P014）。",
    "推论拥抱真实的必然性与拒绝真实的后果（P015）。",
    "界定美感的归属：是人的私人感受而非艺术属性（P016）。",
    "把“美的客观性”判为权术把戏，并把提问判为被扭曲后的伤情展示（P017）。",
    "收束判准与应用：艺术只需忠于真实；以“表达内心感受”的所谓艺术为反面例并警告收藏者；区分分享真实与只表达感受；真正的艺术是解放对真实的狭隘认知（P018-P026）。"
   ],
   "concept_usage": [
    {"term": "雅俗共赏", "meaning": "提问者预设的艺术判准；作者否定其与艺术有关，并称以此谈艺术是把艺术当人类造物。", "evidence": "P001", "ambiguity": "作者未界定“雅”“俗”各指什么。"},
    {"term": "艺术", "meaning": "本文中艺术是天成而非人的造物，是【真】的另一种可能，与美无关、只与真有关，其功能是解放人类对真实的狭隘认知。", "evidence": "P006", "ambiguity": "与“艺术作品”“艺术家”被明确区分，但“天成”的所指未界定。"},
    {"term": "真", "meaning": "艺术的本源与判准；艺术是【真】的另一种可能，并以“忠于真实”作为艺术与非艺术的分界。", "evidence": "P013", "ambiguity": "“真”与“现实”的关系未展开，但文中把“现实”称为囚禁狭隘认知的地牢之名。"},
    {"term": "美", "meaning": "观赏者拥抱艺术时产生的私人感受，是人的附属属性；美的“客观性”被作者称为权术把戏。", "evidence": "P016", "ambiguity": "作者否定了美的客观性，但未说明审美判断是否可讨论。"},
    {"term": "偶像崇拜", "meaning": "作者用以斥责把知识成就归为祖师爷创造与私产的做法。", "evidence": "P009", "ambiguity": "修辞性贬称，未作定义。"},
    {"term": "视觉糖果／糖果师", "meaning": "作者用以指诉诸美感习惯、装点外观而无真实内容的作品及其作者。", "evidence": "P022", "ambiguity": "自创比喻，未给出判定标准。"}
   ],
   "examples_and_targets": [
    "万有引力定律与牛顿：作者用作“规律先于发现者存在、发现者不能修改规律”的类比（P007、P008）。",
    "莫奈与睡莲、印象主义：作者用作艺术被发现而非被创造的例证（P008）。",
    "“表达艺术家内心的感受”的当代艺术及艺术收藏者：作者的反面例与警告对象（P019）。",
    "“黄泥裹上糖霜”“直接吃糖当饭”：作者用以贬斥无真实内容的作品（P022）。",
    "“你的伤口很适合纹成一朵梅花”“赶紧上医院”：作者用以讽刺安慰式回应（P017）。",
    "“这帮人是要来共产共妻的”：作者用以比喻被解放前受众对解放者的想象（P025），属作者引述奴隶主教导的说法，非作者主张。",
    "提问者：被作者判为“被扭曲了的结果”，是本文的反驳对象（P017）。"
   ],
   "conditions": [
    "P002：以“并不见得”“不见得”保留或然，未作全称判断。",
    "P012：“你想要追求艺术，就牢牢记住我下面这句话”为劝谕式条件。",
    "P015：“人类无论最初对它是什么感情，都最后一定会发展出对它的拥抱”为作者的全称预测；“不肯拥抱一切真实的人”为条件性后果。",
    "P017：美学观点的政治化是出现“普遍承认的客观存在”之说的条件。",
    "P019：贬值风险针对“这一类艺术品”且以“几十年后”为时间尺度。",
    "P022：“即使不被毒死”为让步条件。"
   ],
   "rhetoric_and_tone": "短论兼驳论，语气峻切、断语密集：多用“极其等而下之”“污染和狂妄”“权术把戏”“伤情展示”“赶紧上医院”等贬斥与讽刺语；以反问（“有谁敢说万有引力定律是他发明或者创造的吗？”）施压；用“【真】”方括号强调核心判准；结构上是先否定问题预设、再立判准、最后分类褒贬。",
   "unresolved_questions": [
    "“艺术是天成”中的“天成”具体指什么（自然规律、客观精神还是其他），正文未说明。",
    "“真”与“现实”的关系未展开，而“现实”在文中同时被用作贬义的“地牢”。",
    "“几十年后有极高的贬值风险”“针对艺术盲的骗局”属预测与指控，未提供依据，待外部核查。",
    "P017 把提问者判为“被扭曲了的结果”，其判断依据是提问本身，未说明扭曲的来源。",
    "P025 引述的“这帮人是要来共产共妻的”为奴隶主教导的说法，非作者主张，引用时须保持归属。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "艺术和能不能雅俗共赏无关。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "雅俗都不能赏，也并不见得就不再是艺术。雅俗都赏，也不见得就不是垃圾。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "用雅俗能不能赏来谈论艺术，是在把艺术视为人类的造物，可以由人类自己作出表决。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "实际上呢？不但“人不能决定艺术”，相反，是艺术决定着人。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "不要以为艺术品看起来都是人画出来雕出来的，就以为艺术是人的产物。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "艺术其实是天成。人类的艺术家只不过是矿工罢了。艺术作品才是人类的造物，艺术不是。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "艺术由艺术作品承载和揭示，犹如自然规律被实验家揭露和展示。有谁敢说万有引力定律是他发明或者创造的吗？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "莫奈借着睡莲探索和展示了印象主义。但是印象主义是先就存在的。莫奈只是以画笔为锹把它刨了出来。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "就像牛顿并不能被铅球砸了脚就提笔把万有引力定律改掉一样。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "认为一项知识成就是祖师爷的创造和私产，这是极其等而下之的偶像崇拜的恶习。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "艺术自身根本不在乎人类欣赏不欣赏。是人类如果能学会欣赏艺术，人类自己能得救。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "艺术其实与美无关，只与真有关。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "艺术的本质，是【真】的另一种可能。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P015", "quote": "不肯拥抱一切真实的人，将被狭隘的认知囚禁在名为“现实”的地牢里。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "这份感情不是艺术的附属属性，而是人的附属属性。换句话说，“美”只是观赏者的私事。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "美的“客观性”是一种权术把戏。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "本身就是一种伤情展示。人该做的不是告诉他“你的伤口很适合纹成一朵梅花”，而是应该告诉他这事问题很大，赶紧上医院。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "艺术只需要忠于真实。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "这一类艺术品几十年后有极高的贬值风险，这实际上是一种针对艺术盲的骗局。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "分享我的视角，给你另一个角度的真实，这是帮助，是艺术。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P021", "quote": "不在乎真实，只是让你知道我的感受，这是污染和狂妄。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P022", "quote": "诉诸人的美感习惯，装点成视觉糖果，也只是给一团黄泥裹上糖霜而已。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P023", "quote": "虚掷的时间和快感的幻灭到最后会告诉你们什么叫对，什么叫错。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P024", "quote": "真正的艺术，是用来解放人类对真实的狭隘认知的，不是让人觉得美的。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P025", "quote": "觉得美，是被解放的奴隶的感激之情而已。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P026", "quote": "何止不“赏”，不厌不恨都是好的了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["艺术哲学", "美学", "艺术批评"],
   "issue_candidates": ["艺术与雅俗共赏的关系", "艺术与美／真的关系", "艺术作品的归属与版权式理解", "艺术市场与收藏骗局"],
   "text_function_candidates": ["答疑", "驳论", "艺术批评"],
   "object_candidates": ["提问者", "莫奈", "印象主义", "牛顿", "艺术收藏者", "“糖果师”式作者"],
   "working_keywords": ["雅俗共赏", "天成", "矿工", "偶像崇拜", "真", "美感", "权术把戏", "视觉糖果"]
  },
  "notes": "全文 26 段已读完，无图片节点，status=read。要点：①P017 把提问者判为“被扭曲了的结果”，属作者对提问者立场的反驳，未归给提问者；②P025“这帮人是要来共产共妻的”系作者转述奴隶主教导的说法，已保持归属；③P019 关于艺术品贬值与骗局的断言属预测与指控，已登记待外部核查。"
 },
 "48274dc5": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么一些人会对学艺术的有偏见？”，寻求偏见成因的解释。作者只给出一句概括性判断：大部分偏见的本质是对“走了与我不同的道路居然没有失败、让我时不时怀疑自己选错了”的人的报复。作者未针对“学艺术的人”这一具体对象展开，也未给出论证与例证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以一句话作答：大部分偏见的本质，是对走了与我不同道路却没有失败、从而让我时不时怀疑自己选错了的人的报复。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "大部分偏见的本质都是对“走了与我不同的道路居然没有失败、让我时不时怀疑自己选错了”的人的报复。", "evidence": ["E1"]}
   ],
   "argument_steps": [
    "直接给出结论式判断：偏见的本质是报复（P001）。",
    "未展开论证、未举例证、未说明适用对象与范围。"
   ],
   "concept_usage": [
    {"term": "偏见", "meaning": "本文指对走不同道路却未失败者的报复性态度，其成因被归结为对方的存在使偏见者怀疑自己的选择。", "evidence": "P001", "ambiguity": "仅以“大部分”限定，未界定何为偏见、其余部分由何构成。"},
    {"term": "报复", "meaning": "作者用以定性偏见的内在动机。", "evidence": "P001", "ambiguity": "报复的具体形式与机制未说明。"},
    {"term": "走了与我不同的道路", "meaning": "指他人选择了与偏见者不同的人生／职业路径，且“居然没有失败”。", "evidence": "P001", "ambiguity": "未点名学艺术者，仅由提问语境带入。"}
   ],
   "examples_and_targets": [
    "“走了与我不同的道路居然没有失败”的人：作者用作偏见的对象，未举具体人物、事件或机构。",
    "学艺术的人：仅出现在提问者的问题中，正文未点名。"
   ],
   "conditions": [
    "P001：以“大部分”限定，未声称适用于全部偏见。",
    "P001：以“居然没有失败”“让我时不时怀疑自己选错了”为触发条件。",
    "正文仅一句，未说明时间、场景、规模等其他条件。"
   ],
   "rhetoric_and_tone": "极简的单句作答，无论证与例证；用引号内的第一人称心理独白（“走了与我不同的道路居然没有失败、让我时不时怀疑自己选错了”）刻画偏见者的心态，带讽刺与心理剖析意味；语气断言式，未留讨论余地。",
   "unresolved_questions": [
    "正文仅 47 字一句，是否为完整答案无法由本文判断（brief 与正文首句同文）。",
    "未说明学艺术者为何成为偏见对象，也未讨论偏见的其他成因。",
    "“大部分”的比例与经验依据未说明。",
    "“报复”的具体表现（言语、机会排斥等）未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "大部分偏见的本质都是对“走了与我不同的道路居然没有失败、让我时不时怀疑自己选错了”的人的报复。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理", "教育与社会偏见"],
   "issue_candidates": ["对艺术生的偏见", "偏见的成因", "道路选择与自我怀疑"],
   "text_function_candidates": ["答疑", "论断"],
   "object_candidates": ["学艺术的人", "持偏见者"],
   "working_keywords": ["偏见", "报复", "不同的道路", "自我怀疑"]
  },
  "notes": "全文仅 1 段（47 字）已读完，无图片节点，status=read。brief 与正文首句同文；正文极短且无论证、无例证，是否完整无法由本文判断，已在 unresolved_questions 登记。"
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
