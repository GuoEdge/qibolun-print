import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round57-short50.csv'

D = {
    '勉强': ('A03', 'A06;A07'),
    '香槟大厅': ('A02', 'A16;A03'),
    '松烟': ('A18', 'A13'),
    '龙门教': ('A04', 'A08;A01'),
    '万金油': ('A18', 'A03;A20'),
    '强人所难': ('A09', 'A05;A10'),
    '不礼貌': ('A06', 'A07;A03'),
    '实力为本': ('A03', 'A12;A10'),
    '非猎不食': ('A07', 'A16;A03;A01'),
    '小飞棍': ('A15', 'A03'),
    '欠债不欠恩': ('A05', 'A07;A08'),
    '见义勇为的福利': ('A10', 'A01;A19'),
    '拒之门外': ('A06', 'A07;A01'),
    '有争议的合法实践': ('A10', 'A03;A16'),
    'Reason of Beauty': ('A15', 'A02;A01'),
    '屠宰': ('A18', 'A09;A03'),
    '武松们': ('A10', 'A16;A03'),
    '以太主义': ('A03', 'A17;A01'),
    'IT装备解决方案': ('A07', 'A13;A08'),
    '贱猫手': ('A18', 'A03;A20'),
    '花与果': ('A09', 'A01;A14'),
    '绝对领域展开': ('A03', 'A11;A01'),
    '邮政': ('A10', 'A07;A13'),
    '小鸡帽': ('A12', 'A10;A07'),
    '无敌铁公鸡': ('A08', 'A07;A10'),
    '严肃活泼': ('A06', 'A03;A07'),
    '扛不住军训的人': ('A04', 'A01;A07'),
    '美国议员': ('A16', 'A12;A10'),
    '相亲难': ('A06', 'A01;A03'),
    '嫁祸': ('A06', 'A02;A17'),
    '志愿参战': ('A12', 'A01;A10'),
    '支持渔夫的鱼': ('A08', 'A07;A11'),
    '好困难': ('A08', 'A07;A04'),
    '非学术问题': ('A06', 'A03;A12;A16'),
    '介错': ('A10', 'A19;A20'),
    '无所畏': ('A01', 'A11;A06'),
    '交强险': ('A08', 'A02;A09'),
    '片刻欢愉': ('A06', 'A01;A08'),
    '地狱的门锁': ('A09', 'A01;A03'),
    '狂热的自恋投射': ('A06', 'A01;A05'),
    '童子功': ('A15', 'A04;A03'),
    '不贰过': ('A10', 'A03;A19'),
    '小婉': ('A06', 'A03;A01'),
    '悬梁刺股': ('A04', 'A01;A03'),
    '德国品牌': ('A15', 'A20;A08'),
    '锅气': ('A04', 'A07;A08;A15'),
    '应付检查': ('A07', 'A08;A13'),
    '此站不停': ('A12', 'A08;A14;A16'),
    '股东打工': ('A08', 'A07;A10'),
    '不两立': ('A14', 'A08;A07;A12'),
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
        'decision_basis': 'Round 57 full-text review: ' + record['title'],
        'review_note': '按 lexical 正文论证中心裁决；主副专题不重复。',
        'reviewer': 'main-thread',
        'reviewed_at': '2026-09-23',
    }

with PATH.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(by_id.values())

print('round57', len(batch), 'manual_rows', len(by_id))
