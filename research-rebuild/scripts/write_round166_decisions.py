#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round166 decisions: the 28 provisional records with bodies of 1003-1398 chars.

Only writes new files under
``research-rebuild/reports/rebuild-20260926/round166``.  The manual decision
table, the formal index and the corpus are untouched; those are updated later
by a single consolidated apply step.

Decision rule: REVIEWER_PROTOCOL.md R1-R3.  Every one of these 28 records has a
complete authored body in which the centre problem is performed, so all 28 move
to ``manual_confirmed``.  Historical reasons for keeping them provisional were
"author's factual claims not externally verified" (explicitly forbidden by
final-classification-framework-v2.md section 5) or "the article is marked
未完待续" (recorded as a coverage limit in risk_note, not as a topic blocker).
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research-rebuild/reports/rebuild-20260926"
ROUND = OUT / "round166"
REVIEW_DATE = "2026-09-26"
REVIEWER = "main-thread+round166-body-review"

LIMIT = "本确认只覆盖现有可见正文，不追认未发表部分。"

# id -> (primary, secondary, evidence_quote, reason, risk_note_suffix)
D = {
    "9b2b249b-2528-59da-9898-3e18a450a6d0": (
        "A15", "A04;A20",
        "书法实际上并不是“字的艺术”，而是“书写的艺术”。",
        "正文自己给出中心命题并全程展开：书法必须在满足书写功能的前提下追求美，须有临帖底子、尊重字形传统，最终证明的是人格。中心是艺术界定与审美评价，A15 由正文直接支持；临帖训练与人格锻造为副轴 A04，数千年字形传承为副轴 A20。未新增副专题。",
        "示例作品、书法史传统、字形边界及“书写训练造就人格”的判断属作者陈述，未外部核验。",
    ),
    "257fe96f-04ef-5ca0-8677-8f91a179fd70": (
        "A06", "A03",
        "答案是——在任何时候都没有必要追求公开恋情。",
        "正文以“不公开恋情”为中心命题，先论社会性约束对成年人近乎无效，再以超长期战略投资的决策论说明为何不能采用掩盖危险信号的策略。中心是亲密关系中的信任与退出机制，A06 由正文直接支持；决策论推理为副轴 A03。正文末尾“第一性”后中断，属版本限制。",
        LIMIT + " 关于公开恋情的社会约束力、背叛风险识别与长期承诺的判断属作者陈述，未外部核验。",
    ),
    "b42bc4ae-a485-58f5-96b5-cb4efc1bcdef": (
        "A01", "A03",
        "实际上，大多数人对大多数事情的判断都是不可信的。",
        "正文的题面被作者重新界定为“避免受到悲观沮丧的话的影响”，随后论证只有具备周全观察、敏捷理解、严谨表达三项能力的人的输出才值得在意，因此对无此训练痕迹者的负能量可以无视。中心是主体的注意力分配与情绪边界，A01 由正文直接支持；能力门槛的论证为副轴 A03。",
        "关于负能量发言者能力分布、悲观与事实判断关系的判断属作者陈述，未外部核验；不构成心理诊断或人际关系处方。",
    ),
    "23791905-d312-5396-81b0-0749eac16494": (
        "A13", "A08",
        "最大的用处是可以实现很多之前必须靠焊接、铆接、粘合……实现的拼接结构。",
        "正文直接给出中心判断并以公差、装配误差、静态零件、内应力、装备维护逐条论证一体成型如何从根源上消灭装配与维护约束。中心是制造技术与工程路径，A13 由正文直接支持。原副码 A03 删除：正文是工程论证，没有独立的认识论或定义域内容，属审核期附加的邻近领域联想。保留 A08（为加工难度付出的成本）。",
        "关于增材制造内应力、坦克存放、光刻机与大型装备效果的工程断言属作者陈述，未外部核验；不构成设备设计或产业投资建议。",
    ),
    "c8b9d495-94a6-5c22-9dd7-770512e3e82e": (
        "A09", "A06;A08",
        "说服对方买呼吸机，对对方自己也有巨大的好处。",
        "正文以打鼾的五项后果（颌面发育、睡眠与日间表现、社交排斥、同寝关系、进行性疾病）论证应尽早干预并购买呼吸机，中心是疾病干预与身体损伤的社会关系，A09 由正文直接支持；同寝与伴侣关系为副轴 A06，成本收益核算为副轴 A08。",
        "关于打鼾对颌面发育、疾病进展、社交排斥和呼吸机收益的医疗及社会因果属作者陈述，未外部核验；不构成诊断、器械选择或费用建议。",
    ),
    "4f7e63e4-364d-5d12-b771-f70ce29c24cd": (
        "A03", "A20;A16",
        "恰恰就是这种非把辜的传说形象维护住不可的冲动背后的脆弱心态。",
        "正文逐项核验辜鸿铭的学术成就与《论语》译文质量，拆解“十三个博士学位”“倒读英文”等传说，并据此回答“心中的辫子”所指。中心是证据、原文语义与可核查性，A03 由正文直接支持；历史人物评价为副轴 A20，传说与公共形象的塑造为副轴 A16。",
        "辜鸿铭学位、译本版本与具体史料、影视台词来源属作者陈述，未外部核验。",
    ),
    "8a232e01-e8d5-5a3c-ba97-1d9f3e83ff76": (
        "A07", "A01;A04",
        "人人都知道ta们是一笔行走的坏账。",
        "正文把“保持单纯”界定为索取免责特权并把损失转嫁给合作方，逐一推演其后果（无人再支持任何行动、只剩完全听命一条路）。中心是合作责任与组织成本，A07 由正文直接支持；免责动机为副轴 A01，自我修炼的必要性为副轴 A04。",
        "把“单纯”等同于责任逃避属作者的价值主张，未外部核验；不构成对具体人格的评价结论。",
    ),
    "16336056-5d08-5336-a475-bd28c6049c98": (
        "A15", "A03;A20",
        "美的首要含义是“能”。“能”被可持续性加冕，才成为了“善”。",
        "正文以昏君奸臣的长任期与工笔书法的规划、执行难度为例，论证美即能力、可持续的能力才成为善。中心是审美与价值评价，A15 由正文直接支持；“美—能—善”的概念推理为副轴 A03，历史人物为副轴 A20。",
        "所引书法作品、人物史实及“能力可持续即善”的因果属作者陈述，未外部核验；不构成作品归属或艺术质量鉴定。",
    ),
    "00720a35-c252-57cc-9fcf-5ab697528746": (
        "A01", "A04",
        "只有坚信就算减了速，我要提一脚油门就提起来了、就算熄了火，哪怕上坡路，我也能冷启动的人，心里才有这么一份基本的平安。",
        "正文把“摆烂后重新开始”重新界定为冷启动能力，论证对减速与熄火的恐惧如何塑造人际与合作后果，落点在主体信心与平安。中心是主体情绪与自我效能，A01 由正文直接支持；学习重启与练习为副轴 A04。",
        "关于练习、恐惧、血压、人际合作与驾驶能力的心理及健康因果属作者陈述，未外部核验；驾驶比喻不构成教学或治疗建议。",
    ),
    "12b7d5cf-a944-57e4-ba3e-02db106ed7c0": (
        "A07", "A08;A03",
        "执行力，就是传说中推动进度条的神秘力量。",
        "正文把执行力定义为可计算的进度条，给出工时法与当值法两套算法，并把“能否算出进度条”作为胜任与否的判据。中心是组织管理中的任务度量与资源安排，A07 由正文直接支持；劳动计价为副轴 A08，方法性论证为副轴 A03。",
        "关键路径、工时/当值权重与“胜任”判据属作者的方法性主张，未作项目实测或管理学核验。",
    ),
    "5af12600-8940-5fe3-8831-96c4c4ae285d": (
        "A13", "A08;A07",
        "在供料端增加这么个筛选环节，可以一劳永逸的解决这类问题。",
        "正文以投料端预处理站点、实时品质监测与分流为核心方案，并论证其为何是效率最高、成本最低的做法，最后讨论预处理投资由供货商还是进货商承担。中心是生产线流程设计，A13 由正文直接支持；供货成本分担为副轴 A08，甲乙方责任配置为副轴 A07。",
        "生产线常规配置、预处理效率、供应商承责与成本收益属作者陈述，未外部核验；不构成工程设计或合同责任建议。",
    ),
    "265ac1f2-e1fe-5ac2-8117-6eed9fd1460a": (
        "A08", "A11;A20",
        "这三个部门基本构成了人类商业的全部图景，你不是第一第二，就是第三。",
        "正文把商业拆为制造需求、补救需求与两者之外的第三部门（解酒丸、减肥课、保险），论证第三部门如何把“致死边界”外推从而扩展人类自由，并区分微观的堕落判断与宏观的历史价值。中心是商业机制与经济伦理，A08 由正文直接支持；善恶与罪的规范讨论为副轴 A11，历史进步为副轴 A20。",
        "商业部门划分、自由与死亡边界、保险机制及历史价值判断属作者陈述，未外部核验。",
    ),
    "291b5b7d-0a91-5dee-92fa-bc9dac955be6": (
        "A06", "A01",
        "失去了这种对自己、对对方的无罪体认，就意味着无法排除即将在关系中被出卖——或至少被辜负——的怀疑。",
        "正文以儿童“无罪体认”与成人竞争压力、选择余地下降两个前提的崩塌解释友谊为何难建难维。中心是朋友关系与信任的成立条件，A06 由正文直接支持；成人化的主体不安全感为副轴 A01。正文末“（未完，待续）”，属版本限制。",
        LIMIT + " 关于成年人普遍行为、竞争不正当性与关系变化的概括属作者陈述，未外部核验。",
    ),
    "df896b52-02c6-54a8-a942-b71bd50299e6": (
        "A16", "A10;A08",
        "“公关能力”过强是有反噬性的。",
        "正文先判小米在法定强制范围外不承担法律责任，随后把中心转到公关压制言论的自毁后果，主张主动接受“毁誉参半”而不要花钱维护“美誉”。中心是公共形象、舆论反应与信息压制，A16 由正文直接支持；法定责任边界为副轴 A10，信用资产与负债为副轴 A08。",
        "事故事实、法律责任、公关压制与品牌效果属作者陈述，未外部核验；不构成对当事人诚信或侵权责任的判断。",
    ),
    "10ee0a1f-2f19-5f2d-8967-f6f5868f8cc7": (
        "A13", "A12;A20",
        "原因不复杂，就是发动机太多，而且还用了太多新技术，系统太复杂了。",
        "正文以发动机数量、材料、系统复杂度、测试周期与民航对标解释发射失败与漫长测试期，并延伸到中美太空工程竞争及其对其他国家的挤压。中心是航天工程与产业路径，A13 由正文直接支持；大国竞争为副轴 A12，历时差距演变为副轴 A20。",
        "星舰技术判断、测试类比、发射数据与国际竞争预测属作者陈述，未外部核验。",
    ),
    "a987e3e4-b6ad-54eb-8d0f-7dc87db5091d": (
        "A01", "A03",
        "理性太发达，容易推迟你的决策时间。",
        "正文把理性的局限界定为“多谋晚断”，以《猎杀红色十月号》的决策场景说明临界时刻的智力快感如何演变为“理性的毒瘾”，并把超越这种恶习作为智慧的门槛。中心是主体习惯与自我约束，A01 由正文直接支持；理性概念的辨析为副轴 A03。",
        "电影情节、决策心理及“理性毒瘾”的普遍性属作者陈述，未外部核验；不构成对理性能力或风险偏好的心理诊断。",
    ),
    "b7cb4752-da7e-559d-b897-739769d80792": (
        "A04", "A21;A05",
        "首先，选那些有足够深度的玩具。",
        "正文把儿童玩具选择拆为手艺类、技能类、观赏体验类三类，逐类给出深度、长期练习、实际用途与差异化社交的操作要求。中心是能力形成与教育选择，A04 由正文直接支持；泛竞技类玩具为副轴 A21（体育仅作玩具类别出现，不构成主专题），亲子教养为副轴 A05。",
        "玩具图像、儿童发展及同伴社交地位效果属作者陈述，未外部核验。",
    ),
    "d4b1d6e0-69f2-551c-bf92-32cad6755776": (
        "A10", "A04;A01",
        "总的原则是尽量节省体力，以最高效率形成巨大的信号，传递注意者有很大动力去追查和追究的急迫信息。",
        "正文就非法拘禁场景给出八类求救手段（反光、火警、旗帜、阻塞交通、巨响、烟、污染外墙、泼水），并以耗材与体力效率为选择标准，最后落到亲子教育与不绝望的主体能力。场景由犯罪与公共救援链（路人—物业—火警/警察）定义，A10 是注册表中最贴近的中心入口；亲子教育应用为副轴 A04，主体不绝望为副轴 A01。",
        "文中火警、抛掷物、点火、污染外墙与泼水等做法的现实风险及事件背景属作者陈述，未外部核验；不构成消防、救援或公共安全操作建议。",
    ),
    "21593864-66c9-5812-ab4a-fe2023307119": (
        "A15", "A08;A04",
        "你要复制的不是经，而是取经人和取经路。",
        "正文先逐一否定国潮风格、角色设定、动作设计等表层优点，再以玄奘取经为喻论证真正成功的是创作者长期创作能力、信念与承受磨难的文化生产路径。中心是文化生产与作品价值评价，A15 由正文直接支持；产业可复制性为副轴 A08，能力形成为副轴 A04。",
        "游戏成功来源、行业复制条件与《西游记》类比属作者陈述，未外部核验。",
    ),
    "c2241fe8-ab38-5c1e-8d52-181f31ec8a80": (
        "A13", "A08",
        "清洁厨房的首要要害，在于不要弄脏。",
        "正文以“从源头不制造污染”为中心原则，给出控油烟、刀具砧板、锅具、碗碟四组流程与器具方案。中心是家庭操作与器具流程设计，A13 由正文直接支持；成本最小化原则为副轴 A08。原副码 A09 删除：正文无疾病、治疗或护理内容，“良医治其未病”是比喻，不得据比喻归类。",
        "涉及燃气、烹饪温度、食品卫生、一次性用品与锅具安全的做法属作者经验陈述，未作现场或卫生标准核验。",
    ),
    "297f4b21-e387-554c-b1d2-587e34c9d4ce": (
        "A20", "A08;A12",
        "顺着这个剧情多想想，你会对“什么叫金融霸权”“金融霸权的底气到底是什么”“有多少种金融霸权”有深得多、形象得多的体验。",
        "正文以罗马征税与“兑换银钱的人”为历史案例，说明收获季节被迫贱卖收成、债务奴隶与金融霸权的运作机制，再以同一机制解释卢布结算、制裁效果与能源博弈。中心是跨时期的文明机制比较，A20 由正文直接支持；货币结算与市场机制为副轴 A08，战争与制裁策略为副轴 A12。",
        "古代税制、汇率、制裁效果、能源结算与战争预测属作者陈述，未外部核验。",
    ),
    "9a9cc8fa-1fed-5d17-9443-f15488b73654": (
        "A02", "A06;A20",
        "大男子主义是一种自我神化和崇拜渴望。",
        "正文先把大男子主义界定为以保护换取崇拜与主宰，再以二门、内院与恭亲王府说明女性被制度化为囚徒，最后追问失去监狱背书的“典狱长”如何维持关系。中心是性别秩序与身体许可，A02 由正文直接支持；亲密关系结构为副轴 A06，古代制度史为副轴 A20。",
        "府邸图像、古代女性生活制度及大男子主义的历史社会因果属作者陈述，未外部核验。",
    ),
    "d487bc28-9e79-5b7b-8dd9-c62640cf0214": (
        "A02", "A06;A01",
        "说起来也许你们难以置信，但实际上绝大部分的丑陋，其根源是令人不寒而栗的自恋和傲慢。",
        "正文逐项反驳“只喜欢高的帅的”，指出外貌条件几乎都可改变，并把“自下人一等”归因于把努力范围缩小到乐意范围的自恋。中心是男性外貌、身体维护与性别吸引评价，A02 由正文直接支持；恋爱关系为副轴 A06，自我认知为副轴 A01。",
        "外貌标准、性别偏好、减重护肤与心理因果属作者陈述，未外部核验；不构成对具体个人的评价。",
    ),
    "38180b82-4d92-5f78-97e8-21d8e2e3aa46": (
        "A06", "A03",
        "亲密的极限，不是耳鬓厮磨，而是“永远”。",
        "正文提出“亲密量＝亲密度×存续时间”的模型并求极值，论证超过红线（“狎”）的亲密会消耗并损害关系。中心是亲密关系的强度、边界与长期存续，A06 由正文直接支持；概念模型的构造与推理为副轴 A03。正文末“（未完，待续）”，属版本限制。",
        LIMIT + " “关系瓦特/亲密量”不是经验证的亲密度测量；红线与长期损害的判断属作者陈述，未外部核验。",
    ),
    "48ffddab-bda1-5890-8e56-beb21c9d6183": (
        "A01", "A07;A03",
        "只有方法，没有“分寸”。",
        "正文把“严于律己”重新解释为以纪律完全占有自身资源从而获得能动性，把“宽以待人”解释为以实力降低合作门槛从而最大化合作者并形成威慑，结论是这不是尺度问题而是方法问题。中心是主体的自我纪律与自我支配，A01 由正文直接支持；合作门槛与威慑后果为副轴 A07，命题重构与论证为副轴 A03。",
        "关于自律、社交威慑与合作收益的行为因果属作者陈述，未外部核验。",
    ),
    "b2555285-d58b-5c32-9789-c893ed3600a3": (
        "A10", "A16;A03",
        "在评价一个事物的表现的时候，首先都要有一有效的基线。",
        "正文以举重与赛跑为例说明评价需先设基线，再以 omicron 无先例、城市感染峰值对比和治理经验指出公共批评缺失控制变量。中心是公共治理评价与政策判断，A10 由正文直接支持；公共舆论与群体判断为副轴 A16，基线与控制变量方法为副轴 A03。",
        "疫情数据、城市比较、治理成效与公共卫生判断属作者陈述，未外部核验。",
    ),
    "6d36b847-aa59-5af1-ae89-6fcebf74a695": (
        "A01", "A04;A03",
        "世界是对假装甘于平庸的人格外残忍。",
        "正文区分平庸、甘于平庸与假装甘于平庸，论证不平庸的真正收获是与之匹配的强健心态，并以佛教阿罗汉概念界定真正的自甘平庸。中心是主体心态与自我管理，A01 由正文直接支持；基本功与心性训练为副轴 A04，佛教术语的界定为副轴 A03。",
        "佛教术语、人格心态与成就、幸福之间的因果属作者陈述，未外部核验。",
    ),
    "50b7bac2-7f75-5c83-85cd-f633547e3f26": (
        "A04", "A20;A08",
        "综合的看，中国的学科负担太重了，而这其中最可减省的就是英语。",
        "正文论证英语的高学科地位是四十年前资源匮乏与需求缺口造成的历史阶段问题，如今外贸规模与英语人才存量已到顶，主张降低英语分数与课时比重并把时间转向工程、艺术、世界认知与小语种。中心是教育制度与课程负担，A04 由正文直接支持；时代条件变化为副轴 A20，外贸与海外就业机会为副轴 A08。原副码 A17 改为 A08：正文没有民族族群或身份秩序内容，其副轴是贸易与就业。",
        "外贸趋势、英语人才供需、教育政策与海外就业预测属作者陈述，未外部核验。",
    ),
}


def main() -> int:
    packets = {p["id"]: p for p in json.loads((ROUND / "round166-fulltext.json").read_text(encoding="utf-8"))}
    rows = list(csv.DictReader((ROUND / "round166-selection.csv").open(encoding="utf-8-sig")))
    ids = [r["id"] for r in rows]
    assert set(ids) == set(D), set(ids) ^ set(D)

    decision_fields = ["id", "title", "primary", "secondary", "status", "basis", "risk_note"]
    audit_fields = ["id", "title", "source_ordinal", "body_char_count", "old_primary", "old_secondary",
                    "old_status", "new_primary", "new_secondary", "new_status", "blocking_reason",
                    "body_evidence_quote", "decision_reason", "reviewer", "reviewed_at"]
    rev_fields = ["id", "title", "old_primary", "old_secondary", "old_status", "new_primary",
                  "new_secondary", "new_status", "basis", "risk_note", "revision_source", "revised_at"]

    def squash(value: str) -> str:
        """Collapse whitespace so a quotation spanning body line breaks still verifies."""
        return "".join(value.split())

    decisions, audits, revs, bad = [], [], [], []
    for article_id in ids:
        p = packets[article_id]
        new_p, new_s, quote, reason, risk_suffix = D[article_id]
        # The corpus keeps hard line breaks inside paragraphs; store the citation
        # without line breaks and verify it against the whitespace-free body.
        if squash(quote) not in squash(p["text"]):
            bad.append((article_id, p["title"], quote))
        quote = squash(quote)
        risk = (risk_suffix + " " + p["manual_review_note"]).strip()
        decisions.append({"id": article_id, "title": p["title"], "primary": new_p, "secondary": new_s,
                          "status": "manual_confirmed", "basis": reason, "risk_note": risk})
        audits.append({"id": article_id, "title": p["title"], "source_ordinal": p["source_ordinal"],
                       "body_char_count": p["body_char_count"], "old_primary": p["manual_primary"],
                       "old_secondary": p["manual_secondary"], "old_status": p["manual_status"],
                       "new_primary": new_p, "new_secondary": new_s, "new_status": "manual_confirmed",
                       "blocking_reason": "", "body_evidence_quote": quote, "decision_reason": reason,
                       "reviewer": REVIEWER, "reviewed_at": REVIEW_DATE})
        if (p["manual_primary"], p["manual_secondary"], p["manual_status"]) != (new_p, new_s, "manual_confirmed"):
            revs.append({"id": article_id, "title": p["title"], "old_primary": p["manual_primary"],
                         "old_secondary": p["manual_secondary"], "old_status": p["manual_status"],
                         "new_primary": new_p, "new_secondary": new_s, "new_status": "manual_confirmed",
                         "basis": reason, "risk_note": risk,
                         "revision_source": "round166-decisions.tsv (body reread)", "revised_at": REVIEW_DATE})

    if bad:
        print("QUOTE MISMATCH — aborting:", json.dumps(bad, ensure_ascii=False, indent=2))
        return 1

    for name, fields, data in (
        ("round166-decisions.tsv", decision_fields, decisions),
        ("round166-body-evidence-audit.tsv", audit_fields, audits),
        ("round166-revision-log.csv", rev_fields, revs),
    ):
        delim = "\t" if name.endswith(".tsv") else ","
        with (ROUND / name).open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter=delim)
            w.writeheader(); w.writerows(data)

    print(json.dumps({
        "round": 166, "records": len(ids),
        "body_chars": sum(packets[i]["body_char_count"] for i in ids),
        "confirmed": len(ids), "provisional": 0, "revisions": len(revs),
        "primary_changed": sum(1 for i in ids if D[i][0] != packets[i]["manual_primary"]),
        "secondary_changed": sum(1 for i in ids if D[i][1] != packets[i]["manual_secondary"]),
        "quotes_verified_verbatim": len(ids),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
