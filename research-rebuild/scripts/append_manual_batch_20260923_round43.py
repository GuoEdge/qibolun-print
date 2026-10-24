import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round43-short50.csv'
S = [
('4874b0ab-21f3-572d-9c98-b7ffbeb4305e','TOUGHNESS','A11','A05;A16','以青少年自杀威胁、脆弱性和承压能力讨论心理韧性及其社会后果，中心是心理主体。','家庭教育和风险安全为副轴。'),
('b617d351-5319-589e-aa01-f9ec0fd5da33','向太阳飞驰','A13','A16;A06','以骑马通勤说明人与动物的主动协作、身体控制和技术替代边界，中心是技术与系统。','风险安全和亲密协作为副轴。'),
('a21a4111-5b40-5bbc-b0c9-8ba132a4e799','含着','A13','A16;A07','从汽车车门防夹设计推导预防性工程、用户接受和安全责任的普遍原则，中心是技术工程。','风险安全和管理责任为副轴。'),
('d0a30336-b3b4-5e5b-b5cb-cb421a237355','官大一级','A03','A07;A10','分析上下级恋爱对职业评价、公平与双方风险的破坏，中心是亲密关系中的权力边界。','组织治理和职业伦理为副轴。'),
('78617dc3-53f7-5c8e-8258-0e6fe5e9d155','留饭','A05','A03;A07','讨论儿童把客套当真与家庭应否纠正，中心是社会化教育和礼貌边界。','关系互动和伦理规范为副轴。'),
('a9f480d3-443d-5550-bce7-e97ac65c467c','无价通宝','A15','A02;A18','从金属货币兑换解释货币价值由材质、供需和套利决定而非名义设计，中心是财富市场。','认知误解和历史制度为副轴。'),
('1c6f7d71-507c-5303-bdf8-b529179b96ca','没下场','A00','A11;A07','反对过早用成败和下场评价人生，强调不以恶为业、养育家庭和随遇而安，中心是人生价值。','心理安定和伦理责任为副轴。'),
('1023710e-3b55-59f1-ae72-beb3f2d1234a','敷衍','A03','A02;A07','反驳把化妆归结为愉悦自己的万能说辞，转而分析性别、审美和自我解释，中心是性别身体。','认知判断和伦理批评为副轴。'),
('116849af-8469-5b6a-8306-42264e030e2d','族亲','A03','A05;A07','讨论婚后参与大家庭聚会的边界与拒绝方式，中心是婚姻关系中的亲属边界。','家庭代际和伦理沟通为副轴。'),
('98fdca96-b5f8-57e3-bae6-e6299c735b73','恭惟','A07','A10;A02','从“恭惟”的官僚语源展开，讨论向上表达中的尊敬、建议和讨好边界，中心是伦理秩序。','职业组织和概念辨析为副轴。'),
('26c7ad17-39ab-5728-afa9-a4181110a374','肉食者鄙','A18','A12;A02','论证弱者因缺少犯错余地而更擅长政治，中心是权力与政治判断而非性别生理。','组织权力和认知方法为副轴。'),
('04f8e463-559e-5537-be86-6720dcf938b0','石头底','A10','A15;A07','把低门槛劳动视为可靠生存底盘，讨论职业选择、尊严和向上发展的安全基础。','财富劳动和伦理自立为副轴。'),
('5cadc073-abe3-5280-8d6f-ced26f7b2bbf','可帮之人','A07','A05;A11','区分因可怜而同情与因值得助推而帮助，中心是帮助的伦理标准和资源投放。','家庭教育和心理判断为副轴。'),
('c37832fe-1734-5391-a1e3-f0d3dd330b77','何以戒之','A06','A07;A16','通过分类、加锁和明确拒绝处理亲友擅自取物，中心是关系中的个人边界。','伦理规则和安全防护为副轴。'),
('5ca35e55-fe25-519d-ac61-49046c6f7be5','色字头上一把刀','A03','A07;A12','界定物化为剥夺人的主体和尊严，讨论色情劳动、法律和社会权力中的人格待遇。','伦理和政治制度为副轴。'),
('3332eea8-a086-5a08-979d-37317368fea5','拆弹有奖','A12','A18;A15','以美国选举周期、战争和政策后果分析执政与在野的政治策略，中心是政治秩序。','历史权力和经济政策为副轴。'),
('c1808563-e906-5941-a6c9-793f28de548f','不透明','A08','A12;A02','反对未经训练的消费者要求一切透明，主张以竞争、监管和专业分工替代消费者霸权，中心是市场治理。','政治监管和认知能力为副轴。'),
]
batch = list(csv.DictReader(BATCH.open(encoding='utf-8-sig', newline='')))
assert len(batch) == len(S)
assert {r['id'] for r in batch} == {x[0] for x in S}
assert {r['title'] for r in batch} == {x[1] for x in S}
with PATH.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f); rows = list(reader); fields = reader.fieldnames
by = {r['id']: r for r in rows}
for aid,title,p,s,b,n in S:
    by[aid] = {'id':aid,'title':title,'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':b,'review_note':n,'reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round43',len(S),'manual_rows',len(by))
