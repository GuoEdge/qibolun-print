import json, os, glob, re
B = os.path.dirname(os.path.abspath(__file__))
OUT, IO = os.path.join(B, 'out'), os.path.join(B, 'intro_out')
# 常见简体字（繁简异形）抽样表
SIMP = set('这们来说时对为会个过还没么样问题点经发现种实现书论观关系变产处义动应开见长东车门马鸟鱼儿亲务业从众优传伤体农几刘则刚办务动劳区医华单卖历压厅县参双变叶号叹吗听启员团围国图圆坏块坚报场声处备复头夺奋奖妇娱学宁实审宽对寻导层岁币师带帮广庄庆库应废开异弃张弹强归当录彻径忆忧怀态总恋恶悦惊惯愿战户护挂报担拥拦择择击挤损换据摇敌数断无旧显时晋暂术杀杂权条极构样树桥档梦检楼欢气汇汉汤沟没泪洁浅济浏涂润涌渐温湾满灭灵灾炼烦热爱爷牵状独狮献环现电疗盖监盘确离种积称稳竞笔筑简类粮纠红约级纪纳纸线练组细织终经结绝统继续综维罗罢职联肃胜脑脱脸舰艺节苏范荣药获虑虚补装观规视览觉誉计认讨让训议讯记讲许论设证评识诉诊词译试诗诚话诞询该详语误说请诸读课谁调谈谋谓谢谱贝负贡财责贤败货质贩贪贫购贯贵贷费贺资赋赏赔赖赛赞赠趋跃践踪轨轮软轻较辅辆辈辑输辩边达迁过迈运还这进远违连迟适选逊递遗邓郑释针钟钢钱铁银锋错锦键镇长门闪闭问闯闲间闻阅队阳阴阵阶际陆陈险随隐难雾静须顾领频题风飞饭饮馆驱验骗鲁鸡麦黄齐龙')
units = {}
for f in sorted(glob.glob(os.path.join(OUT, '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    units[d['code']] = [u['name'] for u in d['units']]
probs, n, lens = [], 0, []
for code, names in units.items():
    p = os.path.join(IO, code + '.json')
    if not os.path.exists(p):
        probs.append((code, '缺文件')); continue
    d = json.load(open(p, encoding='utf-8'))
    it = d.get('intros', {})
    if set(it) != set(names):
        probs.append((code, '键不符', set(names) ^ set(it)))
    for k in names:
        s = it.get(k, '')
        n += 1; lens.append(len(s))
        if '收' in s: probs.append((code, k, '含收', s))
        if '本單元' in s: probs.append((code, k, '含本單元'))
        if not 36 <= len(s) <= 72: probs.append((code, k, '长度', len(s)))
        if not s.endswith('。'): probs.append((code, k, '结尾'))
        sp = [c for c in s if c in SIMP]
        if sp: probs.append((code, k, '简体', ''.join(sp), s))
print('册', len(units), '单元', n, '长度', min(lens), max(lens), sum(lens) / len(lens))
for x in probs: print(x)
print('问题数', len(probs))
print('残留文件', [f for f in os.listdir(IO) if not f.endswith('.json')])
