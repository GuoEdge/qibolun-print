import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round45-short50.csv'
S = [
('d08b3c8b-a3a8-567d-874e-b774e0a7be53','长兄如父','A05','A07;A18','讨论传统长子长女的家庭权力、责任与代际治理，中心是家庭教育和继承结构。','伦理秩序和历史制度为副轴。'),
('b8fb7ab5-b9da-5ac7-a791-88429eff93de','乱发脾气','A02','A11;A03','反对把无法理解的情绪行为粗暴诊断为非理性，主张先承认对方原因并修复沟通，中心是认知判断。','情绪与关系边界为副轴。'),
('54af5c2a-7be2-502e-b290-f3ba462d5b0e','贪官','A12','A18;A10','从监察技术、组织规模和政治晋升解释贪腐官员的升迁边界，中心是政治治理。','历史制度和职业组织为副轴。'),
('d07965f5-b60f-5a09-b91d-c9894cdd7de9','小摊牌','A06','A05;A07','分析姻亲显性提出要求意味着关系已到临界点，讨论家庭协商与边界谈判。','家庭代际和伦理沟通为副轴。'),
('1013ab5e-044e-5e2f-93c0-74fa73f181ac','未战先胜','A12','A18;A07','以禁毒、抗战、反贪等案例说明政治斗争首先取决于联盟、分化和核心定策，中心是政治秩序。','历史权力和组织伦理为副轴。'),
('ade09427-54c5-5338-9116-a655d2b041dd','政治端粒','A12','A18;A10','分析韩国医政冲突背后的财团、政府与社会组织博弈，中心是政治权力。','历史国家和职业组织为副轴。'),
('08ea947b-1005-5736-92dd-0ea2378297b7','如祭','A10','A12;A07','讨论官员评价、绩效压力和政治责任，中心是组织中的职业治理。','政治秩序和伦理责任为副轴。'),
('01cc5e71-1aae-5677-8463-41640aeaa77c','盈利背离','A15','A02;A16','说明股票价格与当期盈利并非简单同步，核心是金融市场定价和预期。','认知判断和风险管理为副轴。'),
('c2db6711-52f9-5b08-ac47-8b80c0d62034','缅甸停战','A12','A18;A16','分析中国介入缅甸停火、协调各方利益和外力平衡的政治机制，中心是国际政治。','历史权力和战争风险为副轴。'),
('cbc1a2c7-7233-5e7d-aa31-e7b7423ac7c3','Deal','A03','A07;A00','以捐赠分量说明爱的价值取决于承担能力与实际牺牲，中心是关系中的付出与信任。','伦理责任和人生价值为副轴。'),
('152354e6-0595-5009-96a2-26ffc5762847','羊奶锅','A12','A18;A16','把美国警察暴力置于阶级矛盾和制度容留中解释，中心是政治治理与社会秩序。','历史权力和风险安全为副轴。'),
('c76c0111-799b-5157-9bb8-1ab937fd1927','兰花指','A02','A03;A07','主张对他人暗示直接求证，获得明确回应后再行动，中心是沟通认知方法。','亲密关系和伦理边界为副轴。'),
('43782e26-e33b-59dd-bff3-bafd0e109413','东方主义','A12','A18;A04','比较中西政府授权、责任和法律复杂度，讨论东方治理模式的政治逻辑。','历史制度和法律秩序为副轴。'),
('566f14ef-53d3-52f7-a203-dd79eb5ca2bf','快改慢','A12','A04;A18','以治安实际效果反思法律理论与社会秩序的关系，中心是制度治理的实效。','法律制度和历史比较为副轴。'),
('56b2e658-77df-5632-becc-4ecd5093d3b8','缅甸暖宝宝','A12','A18;A15','从缅北问题讨论区域权威、间接干预和国际秩序的长期形成，中心是政治秩序。','历史权力和经济资源为副轴。'),
('3df5e47b-73d2-5361-a9b5-0cf2a6bf4221','不优秀的价值','A07','A03;A00','区分提供有限价值与必须卓越，主张普通人的真诚帮助和被帮助也有伦理价值。','关系互惠和人生价值为副轴。'),
('06ee6669-2a0d-50bf-bc68-2e8763e5a1fc','孔-pop','A18','A12;A00','把韩国邪教与文明形成、独立文化和思想传统联系起来，中心是历史文明。','政治自主和人生价值为副轴。'),
]

batch = list(csv.DictReader(BATCH.open(encoding='utf-8-sig', newline='')))
assert len(batch) == len(S)
assert {r['id'] for r in batch} == {x[0] for x in S}
assert {r['title'] for r in batch} == {x[1] for x in S}
with PATH.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames
by = {r['id']: r for r in rows}
for aid, title, primary, secondary, basis, note in S:
    by[aid] = {
        'id': aid, 'title': title,
        'primary_print_topic_code': primary,
        'secondary_print_topic_codes': secondary,
        'classification_status': 'manual_confirmed',
        'decision_basis': basis, 'review_note': note,
        'reviewer': 'main-thread', 'reviewed_at': '2026-09-23',
    }
with PATH.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(by.values())
print('round45', len(S), 'manual_rows', len(by))
