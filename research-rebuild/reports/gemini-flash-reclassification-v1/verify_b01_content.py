#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""甲册成书内容完整性校验（滑动窗口法）：
   把每篇正文（压平空白后）切成 30 字窗口、步长 15，逐一核对是否出现在 document.xml；
   窗口若被跨叶拆分（头尾各在、中间插入了下一叶题眉等），同样视为完整。
   此法可覆盖「超长段被按 200 字硬切成多块」的情形。
"""
import json, zipfile, re, html

BASE = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/'
DOCX = BASE + '岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx'
WIN, STEP = 30, 15


def lp(p, flat):
    lo, hi = 0, len(p)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        lo, hi = (mid, hi) if p[:mid] in flat else (lo, mid - 1)
    return lo


def ls(p, flat):
    lo, hi = 0, len(p)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        lo, hi = (mid, hi) if p[-mid:] in flat else (lo, mid - 1)
    return lo


with zipfile.ZipFile(DOCX) as z:
    d = z.read('word/document.xml').decode('utf-8')
txt = ''.join(html.unescape(m) for m in re.findall(r'<w:t(?:\s[^>]*)?>(.*?)</w:t>', d, re.S))
flat = re.sub(r'\s+', '', txt)

b01 = [json.loads(l) for l in open(BASE + 'workbook-40b-all-catalog.jsonl', encoding='utf-8')
       if l.strip() and json.loads(l).get('booklet_code') == 'B01']
cor = {}
for l in open(BASE + 'all-articles-merged-v3.jsonl', encoding='utf-8'):
    if l.strip():
        a = json.loads(l)
        cor[a['id']] = a

miss, total, wins = [], 0, 0
for c in b01:
    a = cor.get(c['original_id'])
    if not a:
        miss.append((c.get('title'), '语料缺失'))
        continue
    body = re.sub(r'\s+', '', a.get('text') or '')
    total += len(body)
    for i in range(0, max(1, len(body) - WIN + 1), STEP):
        w = body[i:i + WIN]
        wins += 1
        if w in flat:
            continue
        if lp(w, flat) + ls(w, flat) >= len(w) - 2:   # 被跨叶在句读处拆分
            continue
        miss.append((c.get('title'), '第%d字处 → %s' % (i, w[:24])))

print('篇数            :', len(b01))
print('核对窗口数      :', wins)
print('缺失窗口        :', len(miss), ' (须为 0)')
for m in miss[:12]:
    print('   ', m)
print('语料正文总字数  :', total)
print('文档文本总字数  :', len(flat))
