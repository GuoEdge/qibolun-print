# -*- coding: utf-8 -*-
import json, csv, io, os, re

BASE='research-rebuild/reports/rebuild-20260926'
OUT=os.path.join(BASE,'round171')
FT=os.path.join(OUT,'round171-fulltext.json')
REG='research-rebuild/data/print-topic-registry-v2.csv'
REVIEWER='subagent+round171-body-review'
DATE='2026-09-26'

packets={a['id']:a for a in json.load(open(FT,encoding='utf-8'))}
reg={r['code'] for r in csv.DictReader(open(REG,encoding='utf-8'))}

R={
 '3391e97d-14c5-567c-964a-72368422ba53': dict(
   primary='A06', secondary=['A02','A08'], status='manual_confirmed', blocking='',
   quote='既然不论你是男还是女、是同性恋还是异性恋，只要是基于爱的亲密关系，本质上都是在寻找属于自己的英雄',
   basis='正文中心是婚恋追求与长期亲密关系为何失败：开篇即把题面重述为“为什么婚姻向的追求者反而比临时向的追求者有如此显然的劣势”，随后用“退出机制／投入密度”“对价（并购 vs 租一天）”两套模型解释短期关系优势，最后把出路落在“不要去选择经济安全最大化的裁判员报名参赛”和“双方必须是成对的英雄，爱这么艰难的事情才有可能基本的运转起来”。全篇的行动建议针对的是如何进入并维持亲密关系，故主专题唯一确定为 A06。',
   risk_note='（1）作者关于女性择偶倾向、进化形成的排序算法、女性文化特征的普遍化概括，均为作者陈述，本轮只核验其在正文中的存在与论证位置，不作事实核验、不构成婚恋建议，也不作为研究者重建结论；（2）经济安全最大化、年化投入预期等经济学类比是作者自建模型，非实证研究结论；（3）历史注记标注“正文未完”，本确认只覆盖现有可见正文（正文结尾“（未完，待续）”），不追认未发表部分。',
   reason='按 R1 升级。正文含作者自己的中心处理（自建两优势模型＋行动选择清单），不是题面复述，能把主专题唯一确定到 A06。副专题保留 A02、A08：A02 由正文持续的性别角色／择偶倾向论述支持（“女性自己甚至意识不到自己的排序结果是怎么排出来的”“女性接受这种游戏规则已经上百万年”），A08 由正文的投入—对价—并购/租用经济论证支持（“只要女性的确遵从物质安全最大化策略，你就是公平的输给了对方”“这就像你在谈的是价值一个亿的兼并——或者在很多情况下不如说是收购——交易”）。未删任何旧副码：旧副码 A02、A08 均有正文支持，保留；不新增 A03 等审核者联想码。主专题 A06 不重复出现在副专题。'
 ),
 '6565e946-d35d-5651-9ba8-b4db73c846d4': dict(
   primary='A01', secondary=['A03','A09','A11'], status='manual_confirmed', blocking='',
   quote='乐观与悲观，特指证据够不着、理论盖不住的那一块。露出了这个角，才开始谈到乐观与悲观。',
   basis='正文中心是悲观／乐观两种心理状态本身：先给“抗悲观手段”设可持续性与不递减两条标准，判定毒品式生理刺激与依赖活人两条路不可行，再把抑郁归因于“考试模型”的认知错误与自大，最后重新定义乐观与悲观的分界（“客观评估”不是悲观），并提出可操作的出路（真诚忏悔、中性零位、系统收集“被动的好运”）。行动场景是主体如何调整自身的情绪与认知，故主专题唯一确定为 A01。',
   risk_note='（1）正文涉及抑郁、毒品（“广义的毒品”）、自杀意念式绝望与“上帝惩罚机制”等表述，均属作者陈述，不是临床诊断或治疗建议，本轮只做主题归类、不改变其风险提示性质；（2）作者关于“考试模型／运气模型”的社会史归因与“盲目乐观者”定义属作者主张，未经外部核验；（3）开头作者自述“这个答案会多次更新”，本确认只覆盖现有可见正文（含结尾“多读、快读吧。”在内的当次版本），不追认后续更新部分；（4）按框架第五节，事实主张未外部核验不构成保留临时状态的理由，故风险写入本栏而不影响 R1 升级。',
   reason='按 R1 升级。正文含作者自己的中心处理（两条胜抑郁路径、乐观/悲观的定义重划、被动好运整理法），能把主专题唯一确定到 A01。副专题 A09 由正文连续的抑郁—药物—生理伤害—副作用论证支持（“会带来思维机能障碍的生理伤害的达成人类乐观的手段，就是广义的毒品”“我们先把这几条限制放好，再看两条基本的胜过抑郁症的路径”）；A11 由正文的上帝惩罚机制、偶像崇拜、忏悔与救赎论述支持（“悔改，莫须可活，不悔改，则自我湮灭”“忏悔不是一种损失，而是一种收获”）；A03 由正文关于证据与判断信度的定义性论证支持（“当判断的信度大于个人喜恶所能扭转的程度，你这个时候的态度叫做‘实事求是’”）。旧副码三个均有正文支持，故不删；不新增审核者联想码。主专题 A01 不重复出现在副专题。'
 ),
 '11ad7ad3-87eb-5681-93e2-de3e21cbd8a2': dict(
  primary='A03', secondary=['A07'], status='manual_confirmed', blocking='',
  quote='批评（criticize）必须也只能是善意的。没有善意，哪怕一个脏词都不带，扯尽了天下正义大旗，本质也是迫害。',
  basis='正文中心是“什么才算批评”的定义与论证方法问题：作者先划出批评只能给逻辑、疑问、论证的红线，把敌意攻击、入人以罪、构陷从批评中区分出去，再给出可执行的标准操作（分析批评冲动、诉求清单、批评权的磨损与增厚）、批评的规范原则（授权、对方立场、对方承认的逻辑法则与证据）与技术性问题（中性词、回避利害关系、最小附带伤害）。全篇的行动建议是“如何做出有效的批评与论证”，故主专题唯一确定为 A03。',
  risk_note='（1）作者关于“只要你真的做到了这些原则，你的批评就一定会有效，一定会得感激”的断言属作者主张，未经外部核验，也不能解释为对所有接受者都成立；（2）人类被从硬件层面设计成只听从遵循尊重法则的不同意见（hard-wired）属作者陈述，非经核验的科学结论；（3）“有永续生存保证的企业，没有不优秀的”“中国的企业领袖大部分都没有这个意识……所以它们大部分都会在五年以内灭亡”等企业存续数据性断言未经外部核验；（4）正文结尾作者标注“（未完，待续）”且第 217 段有“此处语句残缺”的自注，本确认只覆盖现有可见正文，不追认未发表部分；（5）按框架第五节，上述未核验不构成保留临时状态的理由，故写入本栏。',
  reason='按 R1 升级。正文含作者自己的中心处理（批评的四类区分、标准操作五步、规范原则与技术要求），能把主专题唯一确定到 A03（认识论事实与论证：批评与语言边界）。副专题只保留 A07：正文有大段连续的职场组织处理（“作为老板，尤其是生意稳定之后的老板，首要的任务就是保证组织伦理的健康”“不要用‘批评’解决问题”“你有能力就立刻提出辞职申请，换一家”）。旧副码 A06 删除，理由：正文对恋人、配偶等亲密关系只有零星类比与举例（第 42 段拿批评权举例提到“孩子要和小混混真爱不渝”，第 185 段“没人愿意和ta们进入亲密关系”作为论证旁证），没有连续展开的亲密关系中心处理，属审核者附加的邻近领域联想，正文不支持，故删。主专题 A03 不重复出现在副专题。'
 ),
}
TITLES={}
for i in packets.values():
    TITLES[i['id']]=i['title']

# ---------- mechanical checks ----------
def norm(s): return re.sub(r'[\s"“”\'‘’]','',s)
results=[]
def check(cond,label,detail=''):
    results.append((label,cond,detail))

ids=list(packets.keys())
check(len(R)==len(packets),'行数与选择清单一致',f'{len(R)} vs {len(packets)}')
check(set(R)==set(ids),'ID 集合完全相等',f'missing={set(ids)-set(R)} extra={set(R)-set(ids)}')

quote_fail=[]
for i,r in R.items():
    t=norm(packets[i]['text']); q=norm(r['quote'])
    # longest matching run
    best=0; bs=''
    for a in range(len(q)):
        for b in range(len(q),a+best,-1):
            if q[a:b] in t:
                if b-a>best: best=b-a; bs=q[a:b]
                break
    if best<12: quote_fail.append((i,TITLES[i],best,bs))
check(not quote_fail,'每行 body_evidence_quote 去引号/空白后最长可命中连续片段 ≥12 字',str(quote_fail))
check(all(r['primary'] in reg for r in R.values()),'primary 均在 A00–A21 内','')
check(all(c in reg for r in R.values() for c in r['secondary']),'secondary 均在 A00–A21 内','')
check(all(r['primary'] not in r['secondary'] for r in R.values()),'primary 不出现在 secondary','')
check(all(len(r['secondary'])<=3 for r in R.values()),'副专题 ≤3 个','')
check(all(r['status']=='manual_confirmed' for r in R.values()),'本轮无 provisional 行，blocking_reason 均为空','')
LEGAL={'source_empty','source_truncated','body_is_quotation','body_is_pointer','body_question_mismatch','body_too_short_for_center','a00_registry_gap'}
check(all((r['blocking'] in LEGAL) if r['status']=='manual_provisional' else r['blocking']=='' for r in R.values()),'保持暂定的行都填合法 blocking_reason','')

# ---------- write decision files ----------
sel=list(csv.DictReader(open(os.path.join(OUT,'round171-selection.csv'),encoding='utf-8-sig')))
order=[s['id'] for s in sel]
ORD={s['id']:s['source_ordinal'] for s in sel}

def w(path,header,rows):
    with open(path,'w',encoding='utf-8',newline='') as f:
        f.write('\ufeff')
        f.write('\t'.join(header)+'\n' if path.endswith('.tsv') else ','.join(header)+'\n')
        for r in rows:
            if path.endswith('.tsv'):
                f.write('\t'.join(str(x).replace('\t',' ') for x in r)+'\n')
            else:
                f.write(','.join('"'+str(x).replace('"','""')+'"' for x in r)+'\n')

dec=[]; aud=[]; rev=[]
for i in order:
    r=R[i]; p=packets[i]; sec=';'.join(r['secondary'])
    dec.append([i,TITLES[i],r['primary'],sec,r['status'],r['basis'],r['risk_note']])
    aud.append([i,TITLES[i],ORD.get(i,''),p['body_char_count'],p['manual_primary'],p['manual_secondary'],p['manual_status'],r['primary'],sec,r['status'],r['blocking'],r['quote'],r['reason'],REVIEWER,DATE])
    if (p['manual_primary'],p['manual_secondary'],p['manual_status'])!=(r['primary'],sec,r['status']):
        rev.append([i,TITLES[i],p['manual_primary'],p['manual_secondary'],p['manual_status'],r['primary'],sec,r['status'],r['basis'],r['risk_note'],'round171 body review (full text, protocol R1)',DATE])

w(os.path.join(OUT,'round171-decisions.tsv'),['id','title','primary','secondary','status','basis','risk_note'],dec)
w(os.path.join(OUT,'round171-body-evidence-audit.tsv'),['id','title','source_ordinal','body_char_count','old_primary','old_secondary','old_status','new_primary','new_secondary','new_status','blocking_reason','body_evidence_quote','decision_reason','reviewer','reviewed_at'],aud)
w(os.path.join(OUT,'round171-revision-log.csv'),['id','title','old_primary','old_secondary','old_status','new_primary','new_secondary','new_status','basis','risk_note','revision_source','revised_at'],rev)

total=sum(packets[i]['body_char_count'] for i in order)
print('TOTAL_BODY_CHARS',total)
print('ROWS dec/aud/rev',len(dec),len(aud),len(rev))
print('CHECKS')
for l,c,d in results: print(('PASS' if c else 'FAIL'),l,d)
print('QUOTE_LEN', [(TITLES[i], len(norm(R[i]['quote']))) for i in order])
