import csv, json
from pathlib import Path

p = Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
rows = [
 {'id':'', 'title':'责打教育','primary_print_topic_code':'A04','secondary_print_topic_codes':'A05;A11','classification_status':'manual_confirmed','decision_basis':'正文中心是惩罚、教育与儿童成长之间的边界和方法','review_note':'家庭与道德语言服务于教育实践判断','reviewer':'main-thread','reviewed_at':'2026-09-22'},
 {'id':'', 'title':'翻车','primary_print_topic_code':'A03','secondary_print_topic_codes':'A01;A20','classification_status':'manual_confirmed','decision_basis':'正文中心是判断失误、事实校验与认知翻转机制','review_note':'个人情绪和历史例证为辅助','reviewer':'main-thread','reviewed_at':'2026-09-22'},
 {'id':'', 'title':'一路向上','primary_print_topic_code':'A05','secondary_print_topic_codes':'A01;A09','classification_status':'manual_confirmed','decision_basis':'正文中心是家庭支持、代际关系与个人成长路径','review_note':'心理动力和健康经历为辅助','reviewer':'main-thread','reviewed_at':'2026-09-22'},
 {'id':'', 'title':'对赌','primary_print_topic_code':'A06','secondary_print_topic_codes':'A01;A03','classification_status':'manual_confirmed','decision_basis':'正文中心是亲密关系中的承诺、博弈与信任','review_note':'主体情绪与理性论证为副轴','reviewer':'main-thread','reviewed_at':'2026-09-22'},
 {'id':'', 'title':'凸 蚓 凸','primary_print_topic_code':'A18','secondary_print_topic_codes':'A03','classification_status':'manual_confirmed','decision_basis':'正文中心是生物形态、自然观察与科学解释','review_note':'认识论仅承担解释方法功能','reviewer':'main-thread','reviewed_at':'2026-09-22'},
 {'id':'', 'title':'铜人','primary_print_topic_code':'A19','secondary_print_topic_codes':'A11;A10','classification_status':'manual_provisional','decision_basis':'正文中心是纪念性物件、死亡记忆与象征秩序','review_note':'涉及宗教和制度象征，保留人工复核状态','reviewer':'main-thread','reviewed_at':'2026-09-22'},
]
with p.open(encoding='utf-8-sig', newline='') as f:
    existing = list(csv.DictReader(f)); fields = list(existing[0])
articles = {}
with open('sooon-q9adg-articles-v2.jsonl', encoding='utf-8') as f:
    for line in f:
        o=json.loads(line); articles[o['title']]=o['id']
by={r['id']:r for r in existing}; added=0
for r in rows:
    r['id']=articles.get(r['title'],'')
    if not r['id']: raise SystemExit(f"title not found: {r['title']}")
    if r['id'] not in by: existing.append(r); by[r['id']]=r; added += 1
    else: by[r['id']].update(r)
with p.open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(existing)
print('added', added, 'rows', len(existing))
