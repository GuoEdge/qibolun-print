import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round46-short50.csv'

# Round 46 decisions are filled after full-text reading; keep this table explicit
# so the batch and source IDs are mechanically checked before any write.
S = [
('02d91221-6cbd-5739-ae03-154992a878a5','宏大叙事','A00','A18;A07','论述宏大叙事如何赋予不可避免的苦难以意义，并形成个人价值观与合作秩序，中心是世界观和人生意义。','正文中心明确。','manual_confirmed'),
('10e9991e-b022-56d3-ab44-e3663cace90e','好生之德','A12','A18;A07','分析中国以长期发展和战略耐心等待对手危机，再以“好生”换取利益的国际战略。','正文中心明确。','manual_confirmed'),
('03a465f1-6380-537b-b359-61daff961ab1','炸弹人','A07','A02;A12','讨论利用点赞、踩、算法排序和情绪反应进行低成本舆论战，中心是策略博弈与心理操纵。','按全文中心归类。','manual_confirmed'),
('6599f61e-24ee-525c-864f-9dea398c3b81','亦真亦假','A07','A12;A02','说明条约效力取决于违约成本和现实收益，而非文字本身的真假，中心是契约信用与博弈。','正文中心明确。','manual_confirmed'),
('078ef8e0-ff0d-5aad-969d-577421b2be00','必要过程','A09','A07;A02','强调未经司法程序不得私自定罪，讨论证据、程序和名誉权保护。','正文中心明确。','manual_confirmed'),
('4801d0a4-8479-5fc4-8444-a963cec69498','司法公正','A09','A07;A00','司法不以当事人皆大欢喜为标准，而以全局风险和社会综合损耗最小为标准。','正文中心明确。','manual_confirmed'),
('f64d2354-d498-56e3-8c70-9603ee776258','破防','A02','A07;A05','主张承认他人的自我防御权，以奖励而非惩罚推动降低防御，中心是心理与人际沟通。','正文中心明确。','manual_confirmed'),
('02b905db-f897-5f58-89a0-8cf878a85d91','失业率高','A08','A12;A18','将失业归因于就业机会不足和制度性危机，而非青年劳动意愿不足，中心是就业与社会结构。','正文中心明确。','manual_confirmed'),
('eaa1d952-119f-5ebd-88ec-3093430f7530','爱的底线','A05','A02;A07','说明爱不等于无限帮助或自我牺牲，亲密关系必须尊重不可侵犯的底线。','正文中心明确。','manual_confirmed'),
('8b633042-75dc-513c-b51e-2589a2e36add','阴谋阳谋','A07','A02;A12','阴谋与阳谋本身中性，道德判断取决于是否违背既定契约。','正文中心明确。','manual_confirmed'),
('a4b0e11a-9cf1-59bc-83b7-d671271eb36e','第二层防线','A16','A13;A12','通过交通节点检疫、应急设施和专业机动力量建立常态化疫情防控体系，中心是公共卫生与应急治理。','正文中心明确。','manual_confirmed'),
('f9abacc6-cc2b-557c-a13b-c2b36b317606','尊重你的敌人','A07','A02;A12','主张尊重敌人并客观评估对手能力，避免靠贬低敌人维持勇气。','正文中心明确。','manual_confirmed'),
('d0f1ea97-d404-56e8-8cbe-5e008f726bd3','石与鸟','A12','A15;A07','分析中俄贸易脱美元化、人民币结算体系扩张及其对欧美战略的连锁影响。','正文中心明确。','manual_confirmed'),
]

batch = list(csv.DictReader(BATCH.open(encoding='utf-8-sig', newline='')))
assert {r['id'] for r in batch} == {x[0] for x in S}
assert {r['title'] for r in batch} == {x[1] for x in S}
with PATH.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames
by = {r['id']: r for r in rows}
for aid, title, primary, secondary, basis, note, status in S:
    by[aid] = {'id': aid, 'title': title,
        'primary_print_topic_code': primary,
        'secondary_print_topic_codes': secondary,
        'classification_status': status,
        'decision_basis': basis, 'review_note': note,
        'reviewer': 'main-thread', 'reviewed_at': '2026-09-23'}
with PATH.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader(); writer.writerows(by.values())
print('round46', len(S), 'manual_rows', len(by))
