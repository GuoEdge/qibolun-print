import csv
from pathlib import Path

p = Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec = [
    ('a6bef4ce-748d-5207-8963-632d78b4ba7c', '凤尾', 'A04', 'A01;A07', 'manual_confirmed', '正文中心是班集体和训练队中的排名、长期训练、逆境韧性与均等机会条件', '心理韧性和集体机会分配为副轴'),
    ('2dcc4d6a-58bf-5e68-9c51-319d51c0f11e', '工德无量', 'A08', 'A07;A15', 'manual_provisional', '正文中心是把工作视为持续生产、再投资和事业生命，而非仅为生活赚钱', '组织劳动与利润再投入为主，艺术家和革命事业为例证，暂定'),
    ('3146e5f6-0769-5784-9040-caf8b2920753', '正衣冠', 'A07', 'A02;A08', 'manual_confirmed', '正文中心是服装如何编码工作角色、权力关系与平等服务边界', '身体呈现和职业财富/服务关系为副轴'),
    ('5d6e0ac8-4818-559e-9449-7f5af8bcd6ec', '人上人上人', 'A10', 'A01;A05', 'manual_confirmed', '正文中心是权力位置、统治风险、公共权柄及其伦理后果', '心理负荷和对父母教育的劝告为副轴'),
    ('a30cf0ae-535b-5f62-bcf8-d7361ddaf2f3', '抢杠铃', 'A04', 'A14;A06', 'manual_confirmed', '正文中心是大学教育、专业选择与综合能力形成', 'AI职业冲击以及组队、友情和爱的能力为副轴'),
    ('fa35c62a-72ac-5f83-806a-cbd66eaef0ab', '三斗金', 'A07', 'A08;A03', 'manual_confirmed', '正文中心是专业服务中的责任履约、风险定价、质量标准与客户关系', '利润成本和责任概念定义为副轴'),
    ('55e2ccc2-9f7c-51c1-89b4-c90ea1c68761', '贫穷的尽头', 'A10', 'A08;A20', 'manual_provisional', '正文中心是国家如何通过制度、救济、资源所有权和公共权力阻断灾年剥夺', '经济贫困和财富集中、历史案例为副轴；政策判断跨度较大，暂定'),
    ('a05bf5e0-e374-5762-9491-68f824cea641', '你好富二代', 'A07', 'A08;A04', 'manual_confirmed', '正文中心是能力、合作、雇佣关系和组织生态中的阶层资源协作', '资本差异和学习技能为副轴'),
]

with p.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
    fields = list(rows[0])

by_id = {r['id']: r for r in rows}
added = 0
updated = 0
for article_id, title, primary, secondary, status, basis, note in spec:
    row = {
        'id': article_id,
        'title': title,
        'primary_print_topic_code': primary,
        'secondary_print_topic_codes': secondary,
        'classification_status': status,
        'decision_basis': basis,
        'review_note': note,
        'reviewer': 'main-thread',
        'reviewed_at': '2026-09-22',
    }
    if article_id not in by_id:
        rows.append(row)
        by_id[article_id] = row
        added += 1
    elif by_id[article_id] != row:
        by_id[article_id].update(row)
        updated += 1

with p.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f'added={added} updated={updated} rows={len(rows)}')
