import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round44-short50.csv'
S=[
('e8104b8f-0b99-50e4-9668-1ab38ed9b0a5','解结','A07','A10;A11','以与同事有私怨时仍坚持公私分明、据事实行事和不落井下石为中心，讨论伦理自律。','组织协作和心理主体为副轴。'),
('8473663a-12f7-5171-8859-da815ef9f22a','寡欲','A18','A03;A00','从中国文化、宗教和社会组织解释性欲随年龄转化为家庭与公共责任，中心是历史文明。','性别身体和人生价值为副轴。'),
('1de3d1f9-c5ac-5e35-aabf-599e8fa73ef0','鸡与猴','A07','A08;A10','通过领导私下批评、公开表扬的风险说明信任、担保和组织权力，中心是伦理关系。','组织管理和职业发展为副轴。'),
('f802ebcb-2bb9-59a4-a1f1-92fec9fcfe10','于爱无违','A03','A07;A15','以从个人核算转向共同体核算解释亲密关系中的付出、牺牲与拒绝，中心是婚恋关系。','伦理责任和共同财富为副轴。'),
('d996c22f-42de-5943-9b5a-dcabaeff555d','良缘','A10','A15;A02','把销售定义为产品与客户建立长期有效关系的媒介，中心是职业方法和产品理解。','市场价值和认知判断为副轴。'),
('c96b0938-922f-5b85-980b-0e45fc3607d9','投桃不报李','A03','A11;A07','分析恋爱中期待落空、自我批判与愤怒循环，中心是亲密关系中的主体边界。','情绪调节和伦理责任为副轴。'),
('3354f89f-28ad-5816-b0ff-42b7f93388ca','泥里的智慧','A07','A03;A11','主张拒绝不尊重者、选择有爱且恒常尊重的关系，中心是尊重伦理。','亲密选择和心理安全为副轴。'),
('e830e716-ff9a-5e35-bcbe-b07193fcfab1','站着活','A06','A05;A15','围绕产后探亲住宿费用讨论夫妻、双方家庭和红包的公平协调，中心是家庭关系治理。','代际秩序和财富分配为副轴。'),
('81a27eae-342f-566e-9dec-eb69e613cdb8','龟','A03','A07;A11','把女性安全感与伴侣判断力、执行力和傲慢联系起来，中心是亲密关系中的信任。','伦理责任和心理安全为副轴。'),
('04bfd910-2819-5fab-a687-fa0251fa5af3','四台阶','A12','A18;A07','以战略工程和对外威慑说明强国力量的克制与治理风格，中心是政治秩序。','历史权力和伦理责任为副轴。'),
('b8654507-6bff-5b2e-a5d5-e963065da83b','到此一游','A00','A11;A07','以放下结果焦虑、服务他人和无求心境建立人生策略，中心是人生价值。','心理状态和伦理行动为副轴。'),
('4f5537ae-f1bd-50d1-94f8-3d8f85ae1535','湿地','A16','A03;A07','重新界定暴力为使人受伤、受辱和受亵渎的能力，中心是风险与伤害概念。','关系边界和伦理判断为副轴。'),
('42ee9603-aad6-505d-aaa5-841abc9a81bb','落魄之人','A13','A10;A15','从谋生工具的珍惜和维护讨论劳动者与工具的依存关系，中心是技术工具。','职业劳动和财富生产为副轴。'),
('31dcaf05-d756-5ab9-8ee7-9c6191c35104','厉害思维','A02','A10;A07','把能力差异归因于对失败和责任的心理反应，讨论学习、责任与逃避机制，中心是认知成长。','职业执行和伦理责任为副轴。'),
('b0d184b7-7ca9-5cab-885f-cc3e136c078f','衣甲精洁','A13','A15;A18','从礼服维护、材料和工艺解释高贵审美如何由技术性传统塑造，中心是技术与设计。','财富消费和历史文明为副轴。'),
('a6e1594f-fb8b-5667-bc6b-e2ea029a265a','伊朗求和','A12','A18;A16','分析战争、求和、国内主和派与大国谈判的战略约束，中心是政治秩序。','历史权力和战争风险为副轴。'),
('074c9c16-ed28-5984-8efc-603849bd725b','啥侮辱','A11','A02;A07','主张对疑似侮辱保持事实导向的钝感，先判断事实和利弊而非沉溺被冒犯感，中心是心理主体。','认知纠偏和伦理自律为副轴。'),
('aec08ba5-cba3-5645-95be-0411d92027c4','咩','A12','A15;A07','论证战略模糊和强政府威慑如何约束高风险资本，中心是政治治理与监管。','市场资本和伦理责任为副轴。'),
('619477f4-e5a2-59a6-b9d3-be63246ea2c2','跨伦理合作','A08','A07;A02','主张按合作所需的最低伦理共识循序升级合作，而非事前追求全面价值一致，中心是组织合作。','伦理边界和认知方法为副轴。'),
]
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==len(S)
assert {r['id'] for r in batch}=={x[0] for x in S}
assert {r['title'] for r in batch}=={x[1] for x in S}
with PATH.open(encoding='utf-8-sig',newline='') as f:
    rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for aid,title,p,s,b,n in S:
    by[aid]={'id':aid,'title':title,'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':b,'review_note':n,'reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(by.values())
print('round44',len(S),'manual_rows',len(by))
