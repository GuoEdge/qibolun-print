import csv,json
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
rows=[
{'id':'3709ad01-93e1-5f41-a322-6da2daec3346','title':'好耐磨','primary_print_topic_code':'A01','secondary_print_topic_codes':'A11;A03','classification_status':'manual_confirmed','decision_basis':'正文中心是善良自我认知、道德主体的长期自我约束，以及在压力中维持行为稳定','review_note':'虽使用好人和道德语言，核心是心理主体与持续情绪劳动，不是宗教制度','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'519ff79d-3ef9-5feb-88fe-94b8d61c1259','title':'误导式加密','primary_print_topic_code':'A13','secondary_print_topic_codes':'A03;A14','classification_status':'manual_confirmed','decision_basis':'正文中心是密码设计、错误密钥与可读错误明文的技术机制','review_note':'圆柱隐喻服务于加密工程问题，认识论只是解释辅助','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'b4ecba65-1b4f-55af-82c1-7052cbe399bb','title':'常见猥琐原因','primary_print_topic_code':'A01','secondary_print_topic_codes':'A02','classification_status':'manual_confirmed','decision_basis':'正文以行为习惯对个人气质与社会观感的影响为中心，直接指向人格表现与主体形象','review_note':'虽可能涉及性别身体观感，但正文主轴是人格和行为习惯','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'e006246c-99e4-5167-8b91-f2cc432be493','title':'尊重阴影','primary_print_topic_code':'A15','secondary_print_topic_codes':'A04;A03','classification_status':'manual_confirmed','decision_basis':'正文中心是素描明度、光影基准和绘画训练中的视觉判断','review_note':'技术解释服务于艺术实践，主专题为艺术审美与文化生产','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'ee40cf28-da20-5301-b942-0b8f81516fa8','title':'消声','primary_print_topic_code':'A10','secondary_print_topic_codes':'A05;A13','classification_status':'manual_provisional','decision_basis':'正文中心是邻里噪音纠纷的证据固定、沟通升级、报警与诉讼路径','review_note':'含具体录音和威胁性策略，需法律风险复核；暂归法律秩序','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'c17b7011-2d5a-583f-9720-a695d890ddd2','title':'顺天改命','primary_print_topic_code':'A01','secondary_print_topic_codes':'A11;A03','classification_status':'manual_confirmed','decision_basis':'正文中心是个人志向、命运观、满足感与奋斗压力之间的心理取向','review_note':'涉及宏大叙事和命运哲学，但落点是主体心理与生活选择','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'f25b91d4-959c-56cb-8f41-ee9e293d4147','title':'青衫','primary_print_topic_code':'A09','secondary_print_topic_codes':'A18;A13','classification_status':'manual_confirmed','decision_basis':'正文中心是依据温度变化进行身体保暖、健康适应和分层衣着的照料策略','review_note':'服装审美与材料技术为辅助，核心是身体照料和健康管理','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'5d9a6ef2-0aa4-5f82-9de2-90615095459f','title':'无差评','primary_print_topic_code':'A15','secondary_print_topic_codes':'A04;A01','classification_status':'manual_confirmed','decision_basis':'正文中心是作品为何获得审美认同，以及童心、仁慈和叙事体验造成的文化评价','review_note':'儿童教育和人格理想是作品评价依据，主轴仍是艺术文化生产','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'2c7f5012-3cdb-526e-b972-e32b591abcbd','title':'同来客','primary_print_topic_code':'A02','secondary_print_topic_codes':'A09;A03','classification_status':'manual_confirmed','decision_basis':'正文针对将女性行为归因于激素的性别化命题，说明身体机制的普遍性与论证边界','review_note':'生理知识用于拆解性别刻板论断，主轴是性别身体与同意','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'2007f25c-11d5-598c-b390-49a4a4cb6dec','title':'乱我心者','primary_print_topic_code':'A04','secondary_print_topic_codes':'A01;A03','classification_status':'manual_confirmed','decision_basis':'正文中心是阅读理解、知识传递和诠释者如何降低学习者与作者之间的理解障碍','review_note':'情绪受伤是理解受阻的机制，核心实践是学习与解释','reviewer':'main-thread','reviewed_at':'2026-09-22'},
{'id':'ee68d5da-fae1-52f6-ac17-82d0e0fc6a51','title':'滑滑客厅','primary_print_topic_code':'A05','secondary_print_topic_codes':'A13;A18','classification_status':'manual_confirmed','decision_basis':'正文中心是家庭客厅的可变空间、家人共同生活和安全布置','review_note':'家具工程和用电防水是实现手段，主问题是家庭生活秩序与空间使用','reviewer':'main-thread','reviewed_at':'2026-09-22'},
]
with p.open(encoding='utf-8-sig',newline='') as f: existing=list(csv.DictReader(f)); fields=list(existing[0])
ids={json.loads(x)['id'] for x in open('sooon-q9adg-articles-v2.jsonl',encoding='utf-8')}
existing=[r for r in existing if r['id'] in ids]; by={r['id']:r for r in existing}; added=0
for r in rows:
 if r['id'] not in by: existing.append(r); added+=1
 else: by[r['id']].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(existing)
print('added',added,'rows',len(existing))
