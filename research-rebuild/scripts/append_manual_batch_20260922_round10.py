import csv
from pathlib import Path

p = Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
rows = [
    {
        'id':'d18e5607-e0e0-53ab-a848-10a057c953b1','title':'怯不服',
        'primary_print_topic_code':'A04','secondary_print_topic_codes':'A01',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是克服怯场、围绕听众提供有效内容并通过准备与实践形成公共表达能力',
        'review_note':'官方候选偏A08；按正文中心改为能力形成，职场/组织语境仅作副轴',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'16831df6-92ee-5c09-90de-0cfefbe6f378','title':'百无禁忌',
        'primary_print_topic_code':'A16','secondary_print_topic_codes':'A13;A14;A08',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是平台、MCN、水军和推荐机制如何操弄真实技术事件与公众认知',
        'review_note':'官方候选偏A08；技术案例为被操弄材料，核心是舆论传播与公共认知',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'d4e952de-65d1-5e9b-af1d-083ad874cb67','title':'离巢',
        'primary_print_topic_code':'A13','secondary_print_topic_codes':'A10;A18',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是长期离家时对电水气、密封排水、照明、物业和财产进行系统工程化防护',
        'review_note':'官方候选偏A10；法律/物业安排为辅助，核心是设施安全与工程操作',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    },
    {
        'id':'0c28890b-63ff-500b-9bf4-a7123264a7a8','title':'无遮',
        'primary_print_topic_code':'A02','secondary_print_topic_codes':'A18;A03',
        'classification_status':'manual_confirmed',
        'decision_basis':'正文中心是人类生殖器外露、衣物遮蔽与性别身体规范的演化和社会解释',
        'review_note':'官方候选偏A15；艺术表达不是中心，按性别身体与同意归类',
        'reviewer':'main-thread','reviewed_at':'2026-09-22'
    }
]
with p.open(encoding='utf-8-sig', newline='') as f:
    existing=list(csv.DictReader(f)); fields=f'{f}'.split() if False else list(existing[0])
# Drop legacy decisions whose IDs are no longer present in the authoritative
# corpus; the audit layer intentionally rejects orphan manual records.
import json
corpus_ids={json.loads(line)['id'] for line in open('sooon-q9adg-articles-v2.jsonl',encoding='utf-8')}
existing=[r for r in existing if r['id'] in corpus_ids]
byid={r['id']:r for r in existing}
for r in rows:
    if r['id'] not in byid: existing.append(r)
    else: byid[r['id']].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(existing)
print('rows',len(existing))
