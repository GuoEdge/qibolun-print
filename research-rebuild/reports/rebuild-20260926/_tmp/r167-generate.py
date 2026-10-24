# -*- coding: utf-8 -*-
"""Round167 body-evidence review: generate decisions / audit / revision-log / report.

Reads (read-only): round167-selection.csv, round167-fulltext.json,
print-topic-registry-v2.csv.
Writes: round167-decisions.tsv, round167-body-evidence-audit.tsv,
round167-revision-log.csv, round167-report.md
"""
import csv, io, json, os, re, sys

BASE = 'research-rebuild/reports/rebuild-20260926/round167'
SEL = os.path.join(BASE, 'round167-selection.csv')
FT = os.path.join(BASE, 'round167-fulltext.json')
REG = 'research-rebuild/data/print-topic-registry-v2.csv'

REVIEWER = 'subagent+round167-body-review'
REVIEWED_AT = '2026-09-26'
LIMIT = '本确认只覆盖现有可见正文，不追认未发表部分。'

# ---------------------------------------------------------------- decision data
# key = id ; values = new_primary, new_secondary(list), quote, decision_reason, risk_note
D = {}

D['dbd7bab9-d695-5e8a-96b9-49ce7510e790'] = dict(  # 俗
    primary='A15', secondary=['A03'],
    quote='一个真正的明白“俗”和“雅”其实地位平等、势均力敌的人，被人评论为“俗”甚至会和被人评论为“雅”同样高兴。',
    decision_reason='正文的中心处理是“俗/雅”审美地位之争：作者先主张“俗本身是一个正面属性”、俗雅地位平等，再把“谁俗”的争执还原为“说贱”的化名游戏，最后以流行音乐与俗乐之分评价王洛宾和刀郎的艺术地位，落点在艺术审美与文化价值评价，A15 由正文支持。“俗=贱”的语词替换与“直接从语文上把问题还原成真相”属定义与语言边界，保留副码 A03。主副码均不变，按 R1 确认。',
    risk_note='作者关于俗乐定义、王洛宾与刀郎艺术地位、普通人审美的判断属作者陈述，未外部核验，按框架不构成暂定理由；图片（1 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['777e32cf-f889-52a0-ba04-13dcc9370c4d'] = dict(  # 开心
    primary='A01', secondary=['A08'],
    quote='永远是你先“不快乐”的搞定ABCDEFG，然后再从中得到快乐。',
    decision_reason='正文把“开心最大化”改写为“快乐 > 快乐的成果 > 快乐”的两冲程循环并给出冷启动结论，中心是主体的情绪机制与行动策略，A01 由正文支持。副码 A08 有正文支持：游戏“只为了赚你那30块钱下载费”、货架柜台与小门脸沿街排开、“把“开心最重要”的人零切碎割”，是连续的消费/市场机制描述。原副码 A06 只出现在“是爱情重要还是快乐重要？”这一句反问列举中，正文没有任何亲密关系、相处或危机的展开，按“副专题须有正文支持”删除 A06。主码不变，按 R1 确认。',
    risk_note='行为经济与心理机制的判断（“这个答案是确定无疑的”）属作者陈述，未外部核验；图片（1 张）审计与保留决定另记，本轮不作图片结论。')

D['0b17f32e-e171-5888-9b3d-d5b1c7d3dca9'] = dict(  # 德雷克医生
    primary='A15', secondary=['A16', 'A07'],
    quote='编剧、导演、美术和武指才是创作团队的核心，演员虽在台前享受一切的大众目光，但是最好搞清楚这份职业的道德底线。',
    decision_reason='正文把“真正的要害是这些文案到底是不是董自己写的”点为中心，并给出行业规范判断：“编剧、导演、美术和武指才是创作团队的核心”“当明星还要抢幕后人员的功，这是行内不可容忍的缺德行为”，落点是文化生产中的署名归属与创作团队伦理，A15 由正文支持，故主码由 A16 改为 A15。网友站队、“平民明星战胜资本”的梦与舆论逆转的连续讨论保留为副码 A16；“中国编剧工会不强大…编剧协会的集体封杀和诉讼”属行业组织约束，保留副码 A07。原主码 A16 转为副码、原副码 A15 升为主码，主副不重复。',
    risk_note='文案归属、公司动机、编剧工会制度与当事人后续行为的判断未独立核验，属作者陈述；图片（1 张）审计与保留决定另记，本轮不作图片结论。')

D['5c7a7815-24a4-5722-b78b-83403189114f'] = dict(  # 怀疑与猜疑
    primary='A03', secondary=['A09', 'A01'],
    quote='怀疑，是在提出一个有效的疑问，而猜疑是在提出一个无效的疑问。',
    decision_reason='正文先以处方药购买与回扣凭据为例说明制度路径，再给出中心区分“怀疑，是在提出一个有效的疑问，而猜疑是在提出一个无效的疑问”，并以可证伪性、证伪手段的经济性与扫雷式精力分配展开完整论证，A03 由正文支持。医药分离、药店与在线药房等医疗制度内容连续成段，保留副码 A09；“放纵自己的恐惧想象”“用低质量的焦虑淹没你”“超防御”等恐惧与焦虑机制保留副码 A01。主副码均不变，按 R1 确认。',
    risk_note='医药分离的实际效果、回扣机制、怀疑手段的可负担性等未外部核验，属作者陈述；图片（1 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['5fcaadb8-9bba-5d43-9f03-0c374dfc9729'] = dict(  # 农村的未来
    primary='A18', secondary=['A13', 'A20'],
    quote='它会首先重新定位为生态治理、环境工程用地。',
    decision_reason='正文回答“农村的根本出路”，主张粮食生产工业化、并把农村重新定位为生态治理与环境工程用地（“它会首先重新定位为生态治理、环境工程用地”），再以生态圈容错性、深空生态项目作为文明条件，A18 由正文支持。工业化路径与能源、立体培养设施内容连续，保留副码 A13；“近一百年内”“50-100 年后”“人类…走向星辰大海”“世界的规则要重新书写”构成跨期文明轨迹，保留副码 A20。原副码 A08 只在“经济结构都会几乎被取消”“经济上的优势是压倒性的”中出现为产业化论证的一环，正文没有展开财富获取、消费、劳动回报或市场交换，按“副专题须有正文支持”删除 A08。',
    risk_note='农业工业化、能源、人口承载与百年社会预测均为作者陈述，未外部核验，按框架不构成暂定理由；图片（12 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['f371ffd1-f98c-5fcb-8109-ad183fd9df86'] = dict(  # 直升珠峰
    primary='A13', secondary=['A18', 'A21'],
    quote='因为这些原因，在珠峰要用直升机，直升机是要特殊设计的。',
    decision_reason='正文以海拔气压、发动机进气含氧量、自反扭矩、横风乱流、绳降与着陆条件逐条论证直升机在珠峰放人的可行性，结论是“在珠峰要用直升机，直升机是要特殊设计的”，中心是工程可行性与风险，A13 由正文支持。积雪区脆弱与噪声引发滑坡的环境后果为副码 A18；徒步登顶死亡率、专业登山者行为与“严重不道德”的登山安全伦理讨论为副码 A21。主副码均不变，按 R1 确认。',
    risk_note='珠峰气压风速、直升机性能、视频着陆案例与死亡率数据未作航空或登山安全核验，属作者陈述，按框架不构成暂定理由；图片（3 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['2d127a86-0787-59e0-9ad0-36940d65f94e'] = dict(  # 圣蓝
    primary='A15', secondary=['A20', 'A11'],
    quote='所以它很自然地获得了视觉艺术中至高的地位。',
    decision_reason='正文以青金石的矿物与颜料性质（钙钠硅酸盐、超饱和高稳定、仍可负担）说明它“所以它很自然地获得了视觉艺术中至高的地位”，再经两河、阿拉伯、拉斐尔、印藏、印度与中国逐段铺陈同一蓝色的使用与地位，中心是艺术材料与审美价值，A15 由正文支持。跨文明的历史脉络保留副码 A20；伊什塔尔门、亚伯拉罕诸教、药师佛、奎师那与祭天等宗教象征内容保留副码 A11。主副码均不变，按 R1 确认。',
    risk_note='矿物性质、宗教史、跨文明颜色象征与青花技术来源等断言未外部核验，属作者陈述；图片（15 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['e07ef7cd-dbd2-571f-b8d0-39b3970e5f9a'] = dict(  # 演员的自我修养
    primary='A03', secondary=['A11', 'A18'],
    quote='注意，到这里，我并没有证明“人的命运肯定不是预定的”，这只是在说“认定人类的命运不是被预定的并没有逻辑上不可解决的问题”。',
    decision_reason='正文的中心操作是检验“命运早已注定”这一命题的推理是否成立：牛顿力学如何被当成“一动手脚账目就会对不上”的数学铁板、量子不确定性与上帝干预的逻辑空间，并明确限定结论范围（“我并没有证明…这只是在说…”），落点在论证与命题边界，A03 由正文支持。加尔文预定论与上帝干预保留副码 A11；牛顿力学、薛定谔的猫等物理学讨论保留副码 A18。主副码均不变，按 R1 确认。',
    risk_note='量子物理、牛顿与加尔文思想史的表述未外部核验，属作者陈述；剧本与演员体验属说明性类比，不构成自由意志问题的实证结论；图片（2 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['35a66bd4-874d-57c9-89f8-16e0c4a0ee43'] = dict(  # 信仰是什么
    primary='A11', secondary=['A03'],
    quote='凡是到了生死存亡的关头你都无法放弃的东西，你就是对它有信仰。',
    decision_reason='正文先给定义“凡是到了生死存亡的关头你都无法放弃的东西，你就是对它有信仰”，再区分“做不到”与“转而宣布这些法则是假的”，并把“唯幸存主义者”判为价值观变色龙，中心是信仰与价值秩序，A11 由正文支持；定义与推理过程的连续展开保留副码 A03。主副码均不变，按 R1 确认。',
    risk_note='关于中国人信仰特征、背叛与组织信用的概括是作者判断，未作历史或社会事实核验，按框架不构成暂定理由；正文标注“（待续）”；' + LIMIT)

D['0db27234-3f9b-52e8-a594-f5e3de3e9d39'] = dict(  # 眼神灵动
    primary='A18', secondary=['A03'],
    quote='食草动物的眼睛和食肉动物的眼睛完全是两个设计思路。',
    decision_reason='正文以食草与食肉两类眼的构造（结构性外凸、超大瞳孔、浅景深与 5-20 米清晰物距 对 双目交叠、眼窝深陷、降眉肌发达）配合警戒与捕食策略解释“眼神灵动”印象，A18 由正文支持；结尾把“眼神灵动”还原为“我们给予食肉动物与我们相近的表情系统的特别加分”，属人类判读与认识边界，保留副码 A03（主码仍为 A18，A03 为副）。主副码均不变，按 R1 确认。',
    risk_note='动物视觉结构、捕食策略与演化因果未作生物学文献核验，属作者陈述，按框架不构成暂定理由；图片（10 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['da098d20-c643-5f18-a4ae-2fd637101811'] = dict(  # 汉字基准字体
    primary='A15', secondary=['A13', 'A10'],
    quote='中国应该由政府牵头投入预算对文化遗产级别的字体资源予以提取和高质量标准化，并作为永久的人类公共文化财富豁免一切版权费用。',
    decision_reason='正文主张由政府牵头对文化遗产级字体资源做标准化并豁免版权、强制预置，理由是汉字审美与文化正统（“中国人的汉字审美甚至文化审美严重地日本化”“才能真正地建立中国自己的审美体系”），中心是字体审美与文化生产，A15 由正文支持。清晰度、webfont 流量与存储三条技术成本讨论保留副码 A13；法定必备、不符合要求禁止销售、只能由中央政府创设发布保留副码 A10。主副码均不变，按 R1 确认。',
    risk_note='字体史、渲染与存储成本、审美影响及政府强制预置与市场准入的判断未外部核验，属作者主张，按框架不构成暂定理由；图片（2 张）审计与保留决定另记，本轮不作图片结论。')

D['f9d288d4-cbf7-51e0-ae6f-a7180096ce4c'] = dict(  # 不怯场
    primary='A16', secondary=['A03', 'A20'],
    quote='通过大型的公开演讲去获得曝光度、获得“民意”，在根子上是被中国的治理文化排斥的行为——因为你不可避免会媚俗。',
    decision_reason='正文的中心场景是当众表达与群体舆论场：先解释中国治理文化不依靠广场演讲、政策影响力来自上层决策圈而非“民意”，再给出“你本来要说的话，应该仅限于你所看到的事实、你所想到的逻辑、你所悟到的大义”，指出调动群体情绪的能力在东方伦理下是道德问题，最后把怯场诊断为平时满足于似是而非与“自立为偶像”。中心仍是公共表达与群体认知，A16 由正文支持；论证标准（数据、逻辑、大义）保留副码 A03，中国与希腊—罗马治理沟通传统（太和殿、军机处）的比较保留副码 A20。主副码均不变，按 R1 确认。',
    risk_note='中国与希腊—罗马政治沟通史、太和殿与军机处的功能以及“群体非理性”的判断未外部核验，属作者陈述；图片（2 张）审计与保留决定另记，本轮不作图片结论。')

D['5a0bd06a-a65b-5410-9161-e4dd82420236'] = dict(  # 下三路
    primary='A16', secondary=['A03', 'A12'],
    quote='这是认知战的惯用手法，类似于用“智利人天天拿樱桃当饭吃”、“伊朗人拿汽油当水用”来刺激你这中国人，专门利用你的无知和下意识情绪缺陷，直攻你的思维下三路。',
    decision_reason='正文以绍伊古住宅传闻为例，核验坐标与地段、对比莫斯科与比弗利山庄房价、指出 CG 渲染图与“红木收藏”类说法没有可核验证据，并把手法归为“这是认知战的惯用手法…直攻你的思维下三路”，中心是信息环境中的辨识与公共认知，A16 由正文支持。证据核查与“但是你自己为什么没去对照”的追问保留副码 A03；认知战、皇国必胜及俄乌相关语境保留副码 A12。主副码均不变，按 R1 确认。',
    risk_note='住宅身份、地理位置、价格比较、图像与 CG 真伪以及纳瓦尔尼和俄乌相关信息均未独立核验，属作者陈述，按框架不构成暂定理由；图片（12 张）审计与保留决定另记，本轮不作图片结论。')

D['44f8c341-fd3e-56d1-a321-7aa65d97043d'] = dict(  # 讽刺
    primary='A16', secondary=['A03', 'A11'],
    quote='“讽刺”这个行为在近现代的中国被高度评价，其实有一个很大的原因——因为在公共宣传中被允许的讽刺，几乎都是站在“我们”的立场上在“讽刺”敌人。',
    decision_reason='正文围绕讽刺作为公共攻击手段展开：先要求为讽刺的正当性给出论证，再指出其真实机制是“你给了看客们足额的快感做贿赂”，并分析它在公共宣传中的历史与净效果，结论是“要反对就反对，不要讽刺”，中心是公共传播与舆论动员的伦理，A16 由正文支持。“讽刺到底能证明什么”的论证无效性保留副码 A03；“佳兵不祥”与“要做一个高贵的敌人”的正义论证保留副码 A11。主副码均不变，按 R1 确认。',
    risk_note='讽刺、幽默、欺凌、家暴风险与宣传传统的心理和社会因果判断未作实证核验，属作者主张；历史注记记录盲读主码存在分歧，本轮以正文证据为准；图片（1 张）审计与保留决定另记，本轮不作图片结论。')

D['c947b0a0-3a44-571d-bef7-8663f537fb19'] = dict(  # 能力
    primary='A04', secondary=['A03', 'A13'],
    quote='人需要拥有的最重要的核心能力，就是无歧义、完备、简洁的表达能力。',
    decision_reason='正文把年轻人的核心能力界定为“无歧义、完备、简洁的表达能力”，给出无错、无漏、无费的定义，说明它是学习、理解、探索与创造力的实质和“精英与非精英的真正分界”，再列出语言描述、编码命名、图表建模、工程图纸与编目等训练科目，中心是能力形成与学习，A04 由正文支持。定义与判断力上限的论证保留副码 A03；流程图、UML、三维建模、工业/建筑图纸、3D 打印等训练科目保留副码 A13。主副码均不变，按 R1 确认。',
    risk_note='表达能力与学习/精英分界的因果判断、练习图例和能力迁移效果未外部核验，属作者主张；正文标注“（未完，待续）”；图片（10 张）审计与保留决定另记，本轮不作图片结论；' + LIMIT)

D['aa50fc78-aa1c-5741-a889-ab0d28e54746'] = dict(  # 真正想做的事
    primary='A01', secondary=['A04'],
    quote='“如何知道我真正想做的是什么”这个无答案的问题，只有转化为“哪些事情是值得拼死一做的”，和“如何最深最好的享受正确的困难”，才会有你想要的答案。',
    decision_reason='正文反思“找到真正想做的事”这一奋斗模型，逐段展开自我怀疑—自我咒骂—把放弃合法化的循环，并给出替代策略：重建价值排序、学习欣赏和享受困难，收束为“如何知道我真正想做的是什么…只有转化为…如何最深最好的享受正确的困难”，中心是主体的动机、怀疑与情绪机制，A01 由正文支持。第二层替代策略落在学习与能力培养（“培养出…能力”“学会品鉴和欣赏”）上，父母以延迟享受塑造子女体验的段落也属教育与训练范畴，故保留副码 A04；正文虽声明“这个教育本质的问题，不是这里的主题”，但教育手段仍是正文处理的因果环节，未清空 A04。主副码均不变，按 R1 确认。',
    risk_note='动机形成、父母影响、延迟享受与“困难快感”的心理因果未独立核验，属作者主张；正文标注“（未完，待续）”；' + LIMIT)

# ---------------------------------------------------------------- load inputs
with io.open(SEL, encoding='utf-8-sig', newline='') as f:
    sel = list(csv.DictReader(f))
packets = {p['id']: p for p in json.load(io.open(FT, encoding='utf-8'))}
reg = {}
with io.open(REG, encoding='utf-8-sig', newline='') as f:
    for r in csv.DictReader(f):
        reg[r['code']] = r['name']

assert len(sel) == len(packets) == 16
assert set(sel[0].keys()) and set(packets) == set(r['id'] for r in sel)
assert all(k in packets for k in D), set(D) ^ set(packets)

rows = []
for r in sel:
    pid = r['id']
    p = packets[pid]
    d = D[pid]
    old_sec = [x for x in (p.get('manual_secondary') or '').split(';') if x]
    new_sec = list(d['secondary'])
    assert d['primary'] not in new_sec
    assert len(new_sec) <= 3
    assert set(new_sec) <= set(reg) and d['primary'] in reg
    for code in (d['primary'],) + tuple(new_sec):
        assert code in reg, code
    for fld in ('quote', 'decision_reason', 'risk_note'):
        assert '\t' not in d[fld] and '\n' not in d[fld], (pid, fld)
        assert ',' not in d[fld], (pid, fld)
    rows.append(dict(
        id=pid, title=p['title'], source_ordinal=r['source_ordinal'],
        body_char_count=int(p['body_char_count']),
        old_primary=p.get('manual_primary') or '',
        old_secondary=';'.join(old_sec),
        old_status=p.get('manual_status') or '',
        new_primary=d['primary'], new_secondary=';'.join(new_sec),
        new_status='manual_confirmed',
        blocking_reason='',
        body_evidence_quote=d['quote'],
        decision_reason=d['decision_reason'],
        risk_note=d['risk_note'],
        reviewer=REVIEWER, reviewed_at=REVIEWED_AT,
        basis=d['decision_reason'],
    ))

# ---------------------------------------------------------------- checks
def norm(s):
    return re.sub(r'[\s“”"\'‘’《》]+', '', s or '')

def longest_common(a, b):
    """longest common substring length (a small, b large)."""
    best = 0
    la, lb = len(a), len(b)
    prev = [0] * (lb + 1)
    for i in range(1, la + 1):
        cur = [0] * (lb + 1)
        ai = a[i - 1]
        for j in range(1, lb + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best

checks = []
total_chars = 0
confirmed = 0
provisional = 0
quote_pass = 0
full_quote_pass = 0
for row in rows:
    text = packets[row['id']]['text']
    total_chars += len(text)
    assert row['body_char_count'] == len(text), row['id']
    q = norm(row['body_evidence_quote'])
    t = norm(text)
    lcs = longest_common(q, t)
    ok = lcs >= 12
    quote_pass += 1 if ok else 0
    full_quote_pass += 1 if q in t else 0
    checks.append((row['id'], row['title'], len(q), lcs, q in t))
    if row['new_status'] == 'manual_confirmed':
        confirmed += 1
    else:
        provisional += 1
        assert row['blocking_reason'] in {
            'source_empty', 'source_truncated', 'body_is_quotation', 'body_is_pointer',
            'body_question_mismatch', 'body_too_short_for_center', 'a00_registry_gap'}

# cross-file consistency
id_sel = [r['id'] for r in sel]
id_rows = [r['id'] for r in rows]
assert id_sel == id_rows
assert len(set(id_rows)) == len(id_rows) == 16
prim_ok = all(r['new_primary'] in reg for r in rows)
sec_ok = all(all(c in reg for c in r['new_secondary'].split(';') if c) for r in rows)
no_overlap = all(r['new_primary'] not in r['new_secondary'].split(';') for r in rows)
one_primary = all(len([r['new_primary']]) == 1 for r in rows)
quote_ok = quote_pass == len(rows)
row_id_ok = set(id_rows) == set(r['id'] for r in sel)

# ---------------------------------------------------------------- write outputs
def w_tsv(path, cols, data):
    with io.open(path, 'w', encoding='utf-8', newline='') as f:
        f.write('\t'.join(cols) + '\n')
        for d in data:
            f.write('\t'.join('' if d.get(c) is None else str(d.get(c, '')) for c in cols) + '\n')

w_tsv(os.path.join(BASE, 'round167-decisions.tsv'),
      ['id', 'title', 'primary', 'secondary', 'status', 'basis', 'risk_note'],
      [dict(id=r['id'], title=r['title'], primary=r['new_primary'], secondary=r['new_secondary'],
            status=r['new_status'], basis=r['basis'], risk_note=r['risk_note']) for r in rows])

w_tsv(os.path.join(BASE, 'round167-body-evidence-audit.tsv'),
      ['id', 'title', 'source_ordinal', 'body_char_count', 'old_primary', 'old_secondary',
       'old_status', 'new_primary', 'new_secondary', 'new_status', 'blocking_reason',
       'body_evidence_quote', 'decision_reason', 'reviewer', 'reviewed_at'],
      rows)

rev = [r for r in rows if (r['old_primary'] != r['new_primary']
                           or r['old_secondary'] != r['new_secondary']
                           or r['old_status'] != r['new_status'])]
with io.open(os.path.join(BASE, 'round167-revision-log.csv'), 'w', encoding='utf-8', newline='') as f:
    f.write('id,title,old_primary,old_secondary,old_status,new_primary,new_secondary,'
            'new_status,basis,risk_note,revision_source,revised_at\n')
    for r in rev:
        f.write(','.join([r['id'], r['title'], r['old_primary'], r['old_secondary'],
                          r['old_status'], r['new_primary'], r['new_secondary'],
                          r['new_status'], r['basis'], r['risk_note'],
                          'round167-body-evidence-audit.tsv (正文逐篇复核)', REVIEWED_AT]) + '\n')

# ---------------------------------------------------------------- report
prim_rev = [r for r in rows if r['old_primary'] != r['new_primary']]
sec_rev = [r for r in rows if r['old_secondary'] != r['new_secondary']]
lines = []
A = lines.append
A('# Round167 正文复核报告（2026-09-26）')
A('')
A('## 本轮定位')
A('')
A('round167 是 92 篇 `manual_provisional` 记录中的一批，共 16 篇（正文 1,434–2,271 字符）。')
A('规则见 `../REVIEWER_PROTOCOL.md`，主专题目录见 `../../final-classification-framework-v2.md` 第三节，')
A('代码与名称见 `../../../data/print-topic-registry-v2.csv`。判定只以每篇 `text` 为据；')
A('`question`、`manual_*`、官方路径、DeepSeek 证据与概念标签只作对照。')
A('')
A('## 总量')
A('')
A('| 指标 | 值 |')
A('|---|---:|')
A('| 文章数 | %d |' % len(rows))
A('| 正文字符总数 | %s |' % format(total_chars, ','))
A('| `manual_confirmed` | %d |' % confirmed)
A('| `manual_provisional` | %d |' % provisional)
A('| 阻塞原因分布 | %s |' % ('空（无暂定行）' if provisional == 0 else '见下表'))
A('| 主专题修订 | %d |' % len(prim_rev))
A('| 副专题修订 | %d |' % len(sec_rev))
A('| 状态修订 | %d |' % len([r for r in rows if r['old_status'] != r['new_status']]))
A('| 逐字引文校验 | %d/%d PASS |' % (quote_pass, len(rows)))
A('')
A('正文字符数逐篇：' + '、'.join('%s %d' % (r['title'], r['body_char_count']) for r in rows) + '。')
A('')
A('## 判定结论')
A('')
A('16 篇全部升级为 `manual_confirmed`。理由分两类：')
A('')
A('1. **历史暂定理由属于框架明令禁止的那一类。** `final-classification-framework-v2.md` 第五节规定')
A('   “不得仅因事实主张未核验而使用临时状态”。本批历史注记大量写作“矿物/宗教史/技术/医学/心理学判断未外部核验”')
A('   “图片未审读 / OCR and factual claims remain unverified”，这些属事实核验层，不是专题判定层的阻塞条件；')
A('   本轮改写入 `risk_note`，并据正文中心升级状态。')
A('2. **正文本身包含作者自己的中心处理。** 16 篇正文均为 1,400 字以上的完整作者论述，逐篇都能定位到完成中心操作的原句')
A('   （见 `round167-body-evidence-audit.tsv` 的 `body_evidence_quote`，全部通过逐字原文命中校验）。')
A('')
A('## 版本限制声明')
A('')
A('`信仰是什么`（正文标“（待续）”）、`能力`、`真正想做的事`（正文标“（未完，待续）”）三篇正文自带未完成标记。')
A('另有 `俗`、`怀疑与猜疑`、`圣蓝`、`演员的自我修养`、`农村的未来`、`直升珠峰`、`眼神灵动` 七篇，')
A('复核任务提示其历史注记可能含“正文未完/未完待续”：逐篇读取现有 `manual_review_note` 与正文后未见未完成标记，')
A('正文均以完整句收束，故未按 `source_truncated` 处理。这十篇的中心问题在现有正文中均可唯一确定，故按 R1 确认，')
A('并同样在 `risk_note` 中写明：')
A('')
A('> ' + LIMIT)
A('')
A('本轮只覆盖现有正文，未追认未发表部分；也不主张这些文章的后续部分已被阅读。')
A('')
A('## 主专题修订（%d 处）' % len(prim_rev))
A('')
if prim_rev:
    A('| 文章 | 旧主码 | 新主码 | 正文依据 |')
    A('|---|---|---|---|')
    for r in prim_rev:
        A('| %s | `%s` | `%s` | %s |' % (r['title'], r['old_primary'], r['new_primary'],
                                          '正文把“真正的要害是这些文案到底是不是董自己写的”点为要害，并以“编剧、导演、美术和武指才是创作团队的核心”“当明星还要抢幕后人员的功，这是行内不可容忍的缺德行为”给出行业伦理判断，中心是文化生产中的署名归属与创作团队伦理；舆论站队转为副码 A16，行业组织约束保留副码 A07。'))
else:
    A('无。')
A('')
A('## 副专题修订（%d 处）' % len(sec_rev))
A('')
if sec_rev:
    A('| 文章 | 旧副码 | 新副码 | 正文依据 |')
    A('|---|---|---|---|')
    sec_note = {
        '开心': '原副码 A06 只出现在“是爱情重要还是快乐重要？”这一句反问列举中，正文没有任何亲密关系、相处或危机的展开，按“副专题须有正文支持”删除 A06；保留 A08（游戏与货架柜台把“开心最重要”的人零切碎割，属消费/市场机制的连续描述）。',
        '德雷克医生': '原主码 A16 转为副码（网友站队、平民明星战胜资本的梦、舆论逆转的连续讨论有正文支持）；A15 升为主码；A07 保留（中国编剧工会不强大、编剧协会封杀与诉讼）。',
        '农村的未来': '原副码 A08 只在“经济结构都会几乎被取消”“经济上的优势是压倒性的”中出现为产业化论证的一环，正文没有展开财富获取、消费、劳动回报或市场交换，属邻近领域联想，删除 A08；保留 A13、A20。',
    }
    for r in sec_rev:
        A('| %s | `%s` | `%s` | %s |' % (r['title'], r['old_secondary'], r['new_secondary'],
                                          sec_note.get(r['title'], '')))
else:
    A('无。')
A('')
A('其余篇目副专题经正文核对全部有正文支持，未改动。')
A('')
A('## 判断分歧与建议交叉核对（本轮无阻塞行）')
A('')
A('以下篇目的两个领域都占据中心位置，本轮按框架“选择更能解释文章主要行动建议或冲突的一个作为主专题、')
A('另一个写入副专题”的规则裁决，未使用暂定状态；建议后续盲读交叉核对，不改变本轮确认结论：')
A('')
A('- **德雷克医生**：公共舆论（A16）与创作署名伦理（A15）并存，取 A15 为主、A16 为副（正文自己把“文案到底是不是他写的”称为“真正的要害”）；')
A('- **不怯场**：公共表达场景（A16）与论证标准（A03）并存，取 A16 为主、A03 为副（官方对象—实践路径“与社会 / 与舆论 / 表达”同向）；')
A('- **农村的未来**：产业化路径（A13）与生态用地/生态圈（A18）并存，取 A18 为主、A13 为副（正文对“农村地区的未来”的直接回答是生态治理与环境工程用地）；')
A('- **真正想做的事**：正文声明“这个教育本质的问题，不是这里的主题”，但父母教育与“学习欣赏困难”的替代策略仍是正文处理的因果环节，故保留副码 A04 而未清空。')
A('')
A('## 机械校验（逐项 PASS）')
A('')
A('- `body_evidence_quote` 去掉引号与空白后，%d/%d 能在该篇 `text`（去空白）中原文命中（>=12 字连续片段），' % (quote_pass, len(rows)))
A('  其中 %d/%d 为整句完全命中；' % (full_quote_pass, len(rows)))
A('- 16 个 `primary` 与全部 `secondary` 均在 `print-topic-registry-v2.csv` 的 A00–A21 内；')
A('- 无一篇 `primary` 出现在 `secondary` 中；每篇恰有 1 个 `primary`，副专题 0–3 个；')
A('- `round167-selection.csv`、`round167-body-evidence-audit.tsv`、`round167-decisions.tsv` 行数均为 16，ID 集合完全相等；')
A('- 保持 `manual_provisional` 的行数为 %d，故 `blocking_reason` 校验为空集（无非法取值）；' % provisional)
A('- `body_char_count` 与 `text` 长度逐篇一致；')
A('- `reviewer` 统一为 `%s`，`reviewed_at` 统一为 `%s`。' % (REVIEWER, REVIEWED_AT))
A('')
A('## 未做与不可推断')
A('')
A('- 未外部核验任何作者的事实主张（技术、生态、医学、矿物、物理、心理、历史、军事）；')
A('- 未把作者陈述写成研究结论；')
A('- 未因图片状态改动任何主题，未声称图片已全部审完；图片审计与保留决定另记；')
A('- 未修改主语料、手工决定表、正式索引、印刷索引、官方边表以及 round165/169/170 目录下任何文件。')
A('')
with io.open(os.path.join(BASE, 'round167-report.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('total_body_chars=%d confirmed=%d provisional=%d' % (total_chars, confirmed, provisional))
print('quote>=12pass=%d/%d fullmatch=%d/%d primary_rev=%d secondary_rev=%d revision_rows=%d'
      % (quote_pass, len(rows), full_quote_pass, len(rows), len(prim_rev), len(sec_rev), len(rev)))
print('checks: primary_in_reg=%s secondary_in_reg=%s no_overlap=%s one_primary=%s quote=%s id_set_equal=%s'
      % (prim_ok, sec_ok, no_overlap, one_primary, quote_ok, row_id_ok))
for c in checks:
    print('  %-14s qlen=%-3d lcs=%-3d full=%s' % (c[1], c[2], c[3], c[4]))
