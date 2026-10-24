import csv
import json
from pathlib import Path

p = Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
rows = [
    {
        'id':'8cbfa0fd-2eb5-551e-89ff-c6a18d222905','title':'反恐怖主义的勇气',
        'primary_print_topic_code':'A12','secondary_print_topic_codes':'A01;A07',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是面对恐怖与高风险事件时的勇气、组织协作、可靠情报和行动选择',
        'review_note':'虽有团队和心理因素，核心是公共安全与危机行动秩序，归战争军事外交与大国秩序',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'61ff68ba-4204-5ff1-ad52-749269ff3c06','title':'bug',
        'primary_print_topic_code':'A03','secondary_print_topic_codes':'A13;A08',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是识别概念混淆、反思自我叙述与现实证据之间的差异，并以可验证事实纠正判断',
        'review_note':'标题虽为技术隐喻，主体论证是认识与证据问题；技术/资源分配为辅助语境',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'f7061924-2e18-57c1-ab15-dfec537bad8c','title':'冲动',
        'primary_print_topic_code':'A01','secondary_print_topic_codes':'A07;A10',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是辨识并控制个人冲动、理解安全感与权力位置对行为的影响',
        'review_note':'涉及领导和职业风险但不是制度规则本身，主轴为心理主体与情绪劳动',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'7a538e8c-1d1a-5dc9-beef-bfdc69dd533e','title':'小事',
        'primary_print_topic_code':'A07','secondary_print_topic_codes':'A03;A04',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是组织与职场中识别真实动机、理解领导关系并把原则转化为可执行行动',
        'review_note':'学习案例和认识反思服务于工作组织实践，主轴为职场组织与合作',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'b3d9b767-65e4-5572-b3f6-ddb2d24097a1','title':'中国人的智慧',
        'primary_print_topic_code':'A17','secondary_print_topic_codes':'A03;A20',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是中国社会的体面、尊严、关系边界与身份秩序如何塑造个人选择和共同体行为',
        'review_note':'虽以心理和历史作解释，核心讨论族群文化身份及其规范结构',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'2a1b2428-a8c2-50e7-b0ec-e8be04077e7b','title':'大方的价格',
        'primary_print_topic_code':'A08','secondary_print_topic_codes':'A07;A03',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是服务定价、成本结构、议价与差异化产品之间的市场交换和商业策略',
        'review_note':'涉及谈判关系和决策逻辑，但主问题是价格、成本与市场竞争',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
]
with p.open(encoding='utf-8-sig', newline='') as f:
    existing = list(csv.DictReader(f)); fields = list(existing[0])
corpus_ids = {json.loads(line)['id'] for line in open('sooon-q9adg-articles-v2.jsonl', encoding='utf-8')}
existing = [r for r in existing if r['id'] in corpus_ids]
byid = {r['id']: r for r in existing}
added = 0
for r in rows:
    if r['id'] not in byid:
        existing.append(r); added += 1
    else:
        byid[r['id']].update(r)
with p.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(existing)
print('added', added, 'rows', len(existing))
