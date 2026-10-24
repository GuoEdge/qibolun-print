import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round59-short50.csv'

D = {
    '瘦麒麟': ('A16', 'A12;A03'), '皆大欢喜': ('A09', 'A03;A06'),
    '大金砖': ('A08', 'A13;A12'), '长大线': ('A01', 'A04;A20'),
    '上下不合': ('A07', 'A03;A10'), '顺流直下': ('A16', 'A09;A03'),
    '伤亡': ('A07', 'A16;A06'), '教同存异': ('A04', 'A05;A10'),
    '锯箭杆': ('A05', 'A06;A01'), '要你何用': ('A11', 'A01;A06'),
    '赌你': ('A16', 'A07;A09'), '八行书': ('A10', 'A07;A20'),
    '我上，我负责': ('A10', 'A07;A12'), '清道夫之饵': ('A07', 'A08;A10'),
    '自责': ('A07', 'A12;A06'), '劳资蜀道山': ('A06', 'A09;A01'),
    '与民同乐': ('A03', 'A10;A17'), '爱因斯坦之子': ('A20', 'A15;A06'),
    '反间': ('A12', 'A16;A17'), '发脾气权': ('A01', 'A07;A06'),
    '幼稚的成年人': ('A01', 'A20;A09'), '滑': ('A04', 'A03;A01'),
    '头盔锁': ('A13', 'A16;A08'), '不必急': ('A01', 'A04;A09'),
    '先独立，再自由': ('A08', 'A01;A11'), '发奋读书': ('A04', 'A01;A08'),
    '0day风险': ('A13', 'A16;A10'), '西瓜皮': ('A03', 'A16;A12'),
    'handyman': ('A13', 'A04;A06'), 'my style': ('A15', 'A04;A03'),
    '薪酬基准': ('A08', 'A07;A03'), '无效安慰': ('A01', 'A06;A04'),
    '反驳人': ('A03', 'A01;A11'), '不赏饭': ('A07', 'A08;A10'),
    '演技单薄': ('A15', 'A03;A04'), '作为主人的价值': ('A07', 'A01;A10'),
    '指定幻觉': ('A10', 'A08;A03'), '职业生命': ('A08', 'A07;A01'),
    '不容有失': ('A13', 'A07;A10'), '克里希那穆提': ('A03', 'A11;A15'),
    '人力情报验证': ('A12', 'A03;A10'), '先民特权': ('A10', 'A20;A17'),
    '开朗的抑郁': ('A09', 'A01;A06'), '立正': ('A10', 'A07;A16'),
    '百发百中': ('A04', 'A13;A03'), '王负剑': ('A03', 'A01;A07'),
    '反洗脑': ('A16', 'A04;A03'), '香火情': ('A06', 'A07;A16'),
    '浪里白条': ('A01', 'A12;A16'), '骗子标准': ('A03', 'A07;A16'),
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
        'decision_basis': 'Round 59 full-text review: ' + record['title'],
        'review_note': '按 lexical 正文中心分类，逐篇依据见 round59-review-notes.md。',
        'reviewer': 'main-thread',
        'reviewed_at': '2026-09-23',
    }

with PATH.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(by_id.values())

print('round59', len(batch), 'manual_rows', len(by_id))
