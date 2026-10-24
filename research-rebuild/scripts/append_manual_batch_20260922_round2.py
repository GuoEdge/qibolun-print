import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'data' / 'print-topic-manual-decisions-v2.csv'
rows = [
    ('335d23ed-6d1a-598c-8324-645e0a7b52a2', '鲜廉寡耻', 'A17', 'A11;A03;A04', 'manual_confirmed', '正文中心是台湾与大陆之间的族群身份、政治文化归属和污名化语言', '教育与媒体是成因，伦理和论证是批判工具；保留作者论断与研究者分类的区分', 'main-thread', '2026-09-22'),
    ('254474b3-8e21-5b51-b5ca-d69122124e58', '现代性', 'A03', 'A20;A11', 'manual_confirmed', '正文中心是现代性概念的定义、真理判断和今古关系的认识论前提', '历史时代材料服务于概念界定，价值判断不作为外部事实结论', 'main-thread', '2026-09-22'),
    ('b41728e2-5953-58ca-b781-22dea32d0f7e', '第三术式', 'A07', 'A10;A16;A04', 'manual_confirmed', '正文中心是普通人通过可模仿且有效的集体行动影响社会', '公共安全治理、传播和能力训练为副轴；救援案例是问题入口', 'main-thread', '2026-09-22'),
    ('193509b8-7624-56a7-bd6d-26a3edfd5efa', '包装袋', 'A13', 'A08;A12', 'manual_confirmed', '正文中心是技术创新的工程路径、需求、资本和市场回报机制', '市场回报与全球秩序是条件和解释轴，不把作者历史判断当外部事实', 'main-thread', '2026-09-22'),
    ('635ab91b-7547-59b2-a395-dfc56265db12', '尖夵', 'A01', 'A07;A11', 'manual_confirmed', '正文中心是利他行为排座次如何制造焦虑、自我否定，并如何维持主体的向善动力', '同志关系和团队扩展为合作副轴，善行平等原则为伦理副轴', 'main-thread', '2026-09-22'),
    ('7a8ae88b-e317-5e82-a9fb-405e1849f57a', '变性倾向', 'A02', 'A05;A09', 'manual_confirmed', '正文中心是未成年人的性别认同、身体选择与父母控制边界', '家庭教育和心理医疗是解释与干预层，不替作者作医学诊断', 'main-thread', '2026-09-22'),
    ('76a5ac8d-0aa2-525d-91a7-981ccf6c8f4b', '人人如是', 'A01', 'A06', 'manual_confirmed', '正文中心是分手后的后悔、比较、理想化和主体如何恢复行动信心', '亲密关系是案例和应用场景，正文与后悔类心理专题保持边界一致', 'main-thread', '2026-09-22'),
    ('1b66c244-0ee7-58d9-bbc6-0649d5a38f50', '毋以善小而不为', 'A01', 'A11', 'manual_confirmed', '正文中心是陌生人的微小帮助如何维持他人的希望、社会期待并降低绝望', '善行规范是行动入口，心理机制是正文中心，不按新闻事件标题归入案件或死亡主题', 'main-thread', '2026-09-22'),
    ('586249cd-9555-5dd8-9779-1bfe22bdb6b3', '瞎比比', 'A07', 'A20;A01', 'manual_confirmed', '正文中心是英雄与人民之间的相互依赖、组织支持和集体行动', '英雄史观是思想副轴，勇气、自我实现和心理支撑为副轴；不把军事比喻误作战争主题', 'main-thread', '2026-09-22'),
    ('e7cddc02-f86d-5271-a815-cd603d3c4335', '地塔', 'A17', 'A01;A13', 'manual_provisional', '正文中心是城乡身份等级、地域污名和由此产生的社会自贬', '主体心理和地方产业例证为副轴；图片未独立复核，保留 provisional', 'main-thread', '2026-09-22'),
]
fields = ['id','title','primary_print_topic_code','secondary_print_topic_codes','classification_status','decision_basis','review_note','reviewer','reviewed_at']
with path.open(encoding='utf-8-sig', newline='') as f:
    existing = list(csv.DictReader(f))
ids = {r['id'] for r in existing}
new = [dict(zip(fields, r)) for r in rows if r[0] not in ids]
if new:
    with path.open('a', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        for r in new:
            w.writerow(r)
print({'existing': len(existing), 'appended': len(new), 'total': len(existing) + len(new)})
