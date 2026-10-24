import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round56-short50.csv'

D = {
    '没有错': ('A01', 'A03'),
    '无保密自觉': ('A07', 'A06'),
    'Gaze': ('A03', 'A02;A06'),
    '战略定力': ('A12', 'A01'),
    '狠狠的读': ('A04', 'A03;A01'),
    '北方狼族': ('A08', 'A12'),
    '父慈子孝': ('A05', 'A01;A04'),
    '多事': ('A01', 'A07;A11'),
    '消费陷阱': ('A10', 'A08'),
    '过三关': ('A07', 'A01'),
    '投降问题': ('A12', 'A20;A03'),
    '汉语天下': ('A17', 'A20;A12'),
    '女士优先': ('A02', 'A11;A18'),
    '暖气片': ('A01', 'A06;A09'),
    '招蝉': ('A03', 'A16'),
    '好光棍': ('A01', 'A05;A16'),
    'Aaron': ('A11', 'A17;A12'),
    '县里人': ('A08', 'A20;A07'),
    '出门右转': ('A06', 'A02;A01'),
    '合理的艺术': ('A15', 'A03;A20'),
    '纯不勇': ('A10', 'A01;A07'),
    '如血': ('A06', 'A01'),
    '花绣': ('A15', 'A06;A02'),
    '叛徒的代价': ('A12', 'A10;A16'),
    '骰子': ('A06', 'A03;A01'),
    '你先': ('A14', 'A12;A13'),
    '流言蜚语': ('A07', 'A10;A16'),
    '默认隐藏': ('A02', 'A06;A03'),
    '穴居人': ('A06', 'A07;A01'),
    '红毯先生': ('A15', 'A20;A03'),
    '忠诚的卧底': ('A10', 'A07;A01'),
    '多语种剧情': ('A15', 'A03;A17'),
    '来不来': ('A12', 'A08;A07'),
    '我不问，你不说': ('A06', 'A09;A03'),
    '大钱大官': ('A01', 'A20;A11'),
    '睡者为王': ('A01', 'A03;A08'),
    '手心打手背': ('A16', 'A07;A08'),
    '淋雨': ('A17', 'A01;A06'),
    '半星之敌': ('A12', 'A03;A17'),
    '三鞠躬': ('A06', 'A01'),
    '上白班的杰克': ('A09', 'A10;A16'),
    '镜子': ('A03', 'A02;A17'),
    '大排场': ('A06', 'A07;A01'),
    '宁十勿一': ('A10', 'A07;A01'),
    '高铁俱乐部': ('A13', 'A08;A12'),
    '性倒钩': ('A02', 'A06;A10'),
    '不讲究': ('A04', 'A15;A03'),
    '不损人': ('A11', 'A10;A16'),
    '鸡娃仙子': ('A20', 'A13;A09'),
    '新支柱产业': ('A08', 'A13;A12'),
}

batch = list(csv.DictReader(BATCH.open(encoding='utf-8-sig', newline='')))
assert len(batch) == 50
assert {r['title'] for r in batch} == set(D)

with PATH.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames

by_id = {r['id']: r for r in rows}
for record in batch:
    primary, secondary = D[record['title']]
    by_id[record['id']] = {
        'id': record['id'],
        'title': record['title'],
        'primary_print_topic_code': primary,
        'secondary_print_topic_codes': secondary,
        'classification_status': 'manual_confirmed',
        'decision_basis': 'Round 56 full-text review: ' + record['title'],
        'review_note': '按 lexical 正文论证中心裁决；主副专题不重复。',
        'reviewer': 'main-thread',
        'reviewed_at': '2026-09-23',
    }

with PATH.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(by_id.values())

print('round56', len(batch), 'manual_rows', len(by_id))
