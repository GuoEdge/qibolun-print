import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
fields = [
    "id", "title", "primary_print_topic_code", "secondary_print_topic_codes",
    "classification_status", "decision_basis", "review_note", "reviewer", "reviewed_at",
]

rows = [
    # Batch reviewed with independent正文复核.
    ("6eb44e7f-c3ba-5212-b188-f39193ff2f5e", "一国书", "A16", "A04;A11", "manual_confirmed",
     "正文中心是面向未来公共读者的可传播、可复用知识回答，而非对单一陌生人的私人交往",
     "教育功能和上帝使者是副轴；官方对象—实践标签保留为索引，不替代打印主专题", "main-thread", "2026-09-22"),
    ("dbe8efe2-7620-5e5f-8692-69b10734c2ef", "优质选择", "A06", "A02;A01", "manual_confirmed",
     "正文中心是以实际责任、行动和互惠检验人格质量，从而进行择偶与长期关系选择",
     "性别角色是问题入口，主体判断和识人心理为副轴；不因男性题面机械归入 A02", "main-thread", "2026-09-22"),
    ("ba725db6-a4a3-5d63-a45d-33eabd849398", "世交", "A06", "A05;A08", "manual_provisional",
     "正文中心是低频但长期的友好关系如何通过诚意礼物、互惠和家族延续得到维护",
     "家族与物质往来是友谊机制；原文含 3 张图片，图片尚未独立复核", "main-thread", "2026-09-22"),
    ("e6589a7d-0d44-5934-9be0-cbf5f637a329", "循序渐进", "A09", "A05;A11", "manual_confirmed",
     "正文中心是年轻人为侄子捐肾时面对的身体风险、医疗决定和亲属照料责任",
     "功德、奉献能力与循序训练是伦理解释层，不把器官捐献机械归入教育或一般心理", "main-thread", "2026-09-22"),
    ("8d0a678f-0ac3-5420-847f-4346d47753f4", "换电关键", "A13", "A18;A08", "manual_confirmed",
     "正文连续讨论换电站、电池集装运输、集中充电、储能中心、回收和基础设施规模",
     "能源调度为 A18 副轴，商业模式为 A08 副轴；机器 A07 不能解释工程中心", "main-thread", "2026-09-22"),
    ("a3789420-2208-5538-8511-460e4a95ab7b", "侵略者", "A12", "A20;A03", "manual_provisional",
     "正文中心是越境战争、侵略者定义、战后政治结果与国际秩序",
     "历史案例和概念论证为副轴；原文含 2 张图片且有外部历史判断，图片复核前保留 provisional", "main-thread", "2026-09-22"),

    # Batch read directly from the source corpus in this turn.
    ("7b685968-b121-5bc0-bb1d-1af008805987", "投暗自首", "A01", "A11;A10", "manual_confirmed",
     "正文中心是性格评价、社会性约束和主体如何处理内耗、边界与行动责任",
     "题面关于心理缺陷的前提被作者反驳；伦理规范和社会防卫为副轴", "main-thread", "2026-09-22"),
    ("bbb941e1-9533-50a5-9260-273e55127886", "无土栽培", "A01", "A04;A06", "manual_confirmed",
     "正文中心是儿童缺少同伴合作与对抗实践后，情绪识别、尺度感和主体稳定能力的发育问题",
     "教育环境与同伴关系是形成机制；不按家长题面机械归入家庭专题", "main-thread", "2026-09-22"),
    ("ea9b5162-0a84-5774-bad0-31d96efddaca", "毒论", "A01", "A03;A20", "manual_confirmed",
     "正文中心是区分苦难、创伤与韧性，并讨论主体如何赋予不可避免的苦难以可承受的意义",
     "论文解读和证据批评为认识论副轴，历史兴替例证为副轴；作者判断不作外部事实结论", "main-thread", "2026-09-22"),
    ("1addb67f-8f67-5299-98aa-53ebc0618259", "成功之母", "A07", "A04;A08", "manual_confirmed",
     "正文中心是组织中的项目授权、风险担保、资历积累以及用眼前功劳换取更高层级实践机会",
     "能力形成和市场资历是副轴；不把个人功劳争议孤立为公平或心理专题", "main-thread", "2026-09-22"),
    ("229d76cd-bb58-5edd-9662-3cde6cc81a37", "站着说话", "A06", "A01;A08", "manual_confirmed",
     "正文中心是亲密关系中坚定选择、牺牲与珍惜的交换逻辑，而非外貌价值本身",
     "主体自我评价和成本—回报比喻为副轴；美貌只是被作者否定的入口", "main-thread", "2026-09-22"),
    ("378fa426-595e-55c4-b84c-8df607af5d8d", "均值模糊", "A10", "A20;A05", "manual_provisional",
     "正文中心是国家以孝治天下、宗族连坐和父母权威作为基层秩序与行政控制机制",
     "历史制度和家庭关系是解释副轴；含 1 张算法图片尚未独立复核", "main-thread", "2026-09-22"),
    ("b5636f46-9279-5242-a25e-95ce95de0ce0", "我来也", "A13", "A10;A09", "manual_provisional",
     "正文中心是用消费级无人机、钢丝绳和输送线构成高层火灾救援技术方案",
     "公共安全指挥和受困者照料为副轴；含 2 张图片，技术参数与图像尚未独立复核", "main-thread", "2026-09-22"),
    ("f1806d37-7f74-5a18-980e-f53a768f9292", "马戛尔尼", "A07", "A06;A20", "manual_confirmed",
     "正文中心是进入群体后识别既有权力结构、遵循组织礼数并以合作适应建立影响力",
     "儿童同伴关系和历史案例是副轴；不把马戛尔尼史例当作文章主专题", "main-thread", "2026-09-22"),
    ("7c21669c-8fe9-5f4e-b8fb-0d98de9f0109", "有谓天赋", "A04", "A01;A15", "manual_confirmed",
     "正文中心是把天赋定义为能转化为行动的热爱、持续实践和承受评价后继续改进的能力",
     "主体动机和写作文化生产为副轴；不把作者对水平的分数比喻当成客观测量", "main-thread", "2026-09-22"),
    ("17649db4-9574-57a1-b386-d7f3e181d218", "无威", "A05", "A06;A01", "manual_provisional",
     "正文中心是家庭中儿童教育、夫妻共同决策、情绪承认和权力取得的现代伦理边界",
     "婚姻协商和情绪调节为副轴；含 1 张图片，保留 provisional", "main-thread", "2026-09-22"),
    ("71e89445-dd77-54af-899d-8cb1747538e9", "绳降逃生", "A13", "A10;A09", "manual_provisional",
     "正文中心是火灾速降设备、固定点、绳缆材料与路线安全的工程操作条件",
     "公共安全和救援照料为副轴；含 1 张图片且具体设备安全性需独立复核", "main-thread", "2026-09-22"),
    ("aa4a85ff-eaa4-57ca-b741-526535b5bc51", "不让小梨", "A05", "A10;A01", "manual_confirmed",
     "正文中心是父母对儿童正当利益的保护责任、冲突干预和承认能力边界",
     "权利秩序与父母的心理包袱为副轴；谦让被限定为正当分配而非放弃被侵犯利益", "main-thread", "2026-09-22"),
]

with path.open(encoding="utf-8-sig", newline="") as f:
    existing = list(csv.DictReader(f))
existing_ids = {r["id"] for r in existing}
new = [dict(zip(fields, row)) for row in rows if row[0] not in existing_ids]
if new:
    with path.open("a", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerows(new)
print({"existing": len(existing), "candidate_rows": len(rows), "appended": len(new), "total": len(existing) + len(new)})
