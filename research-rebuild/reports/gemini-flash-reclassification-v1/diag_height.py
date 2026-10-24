#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""诊断：逐页估算版面高度，找出超高（会被 Word 推页 → 空页）的页块。"""
import zipfile, re, sys, json

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
import xml.etree.ElementTree as ET

PATH = sys.argv[1] if len(sys.argv)>1 else '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx'

z = zipfile.ZipFile(PATH)
root = ET.fromstring(z.read('word/document.xml'))
body = root.find(NS + 'body')

PAGE_H = 16838 - 900 - 1500    # 14438 twips = 721.9pt 版心（上边距 45pt，下边距 75pt）
PAGE_PT = PAGE_H / 20.0

def para_pt(p):
    """估算一个段落的高度(pt)。"""
    pPr = p.find(NS + 'pPr')
    before = after = 0
    line = None
    lineRule = None
    indent_first = 0
    if pPr is not None:
        sp = pPr.find(NS + 'spacing')
        if sp is not None:
            before = int(sp.get(NS + 'before') or 0)
            after = int(sp.get(NS + 'after') or 0)
            if sp.get(NS + 'line'):
                line = int(sp.get(NS + 'line'))
                lineRule = sp.get(NS + 'lineRule')
        ind = pPr.find(NS + 'ind')
        if ind is not None:
            indent_first = int(ind.get(NS + 'firstLine') or 0)
    # 文本
    txt = ''.join(t.text or '' for t in p.iter(NS + 't'))
    has_img = p.find('.//' + NS.replace('main', 'drawing')) is not None or 'drawing' in ET.tostring(p, encoding='unicode')
    n = len(txt)
    # 字号：取最大 sz
    szs = [int(r.get(NS + 'val')) for r in p.iter(NS + 'sz') if r.get(NS + 'val')]
    sz = max(szs) if szs else 23          # half-points
    font_pt = sz / 2.0
    # 行高
    if line and lineRule == 'exact':
        line_pt = line / 20.0
    elif line and lineRule == 'atLeast':
        line_pt = max(line / 20.0, font_pt * 1.25)
    else:
        line_pt = font_pt * 1.45          # 单倍行距近似
    # 列宽：正文单元格 6850 dxa（与 lib_qibo_layout.js 保持一致）
    if has_img:
        return before / 20.0 + 34 + after / 20.0
    if n == 0:
        lines = 1
    else:
        # 半角算 0.5 字；正文单元格宽 6850dxa，右内边距 200dxa
        gl = 0.0
        for ch in txt:
            gl += 0.5 if ord(ch) < 0x2E80 else 1.0
        usable = (6850 - 200) / 20.0
        cpl_first = max(1, int((usable - indent_first / 20.0) / font_pt))
        cpl_cont = max(1, int(usable / font_pt))
        if gl <= cpl_first:
            lines = 1
        else:
            lines = 1 + max(0, -(-int(gl - cpl_first) // cpl_cont))
    return before / 20.0 + lines * line_pt + after / 20.0

def table_row_pt(tbl):
    """估算表格高度 = 各 tr 之和；tr 高度 = max(各 tc 内容高) + 上下 margin。"""
    total = 0.0
    for tr in tbl.findall(NS + 'tr'):
        trH = 0.0
        for tc in tr.findall(NS + 'tc'):
            tcPr = tc.find(NS + 'tcPr')
            mt = mb = 0
            if tcPr is not None:
                m = tcPr.find(NS + 'tcMar')
                if m is not None:
                    t_ = m.find(NS + 'top'); b_ = m.find(NS + 'bottom')
                    if t_ is not None: mt = int(t_.get(NS + 'w') or 0)
                    if b_ is not None: mb = int(b_.get(NS + 'w') or 0)
            h = 0.0
            for ch in tc:
                if ch.tag == NS + 'p':
                    h += para_pt(ch)
                elif ch.tag == NS + 'tbl':
                    h += table_row_pt(ch)
            trH = max(trH, h + (mt + mb) / 20.0)
        # trHeight
        trPr = tr.find(NS + 'trPr')
        if trPr is not None:
            th = trPr.find(NS + 'trHeight')
            if th is not None:
                v = int(th.get(NS + 'val') or 0) / 20.0
                rule = th.get(NS + 'hRule')
                if rule == 'atLeast':
                    trH = max(trH, v)
                elif rule == 'exact':
                    trH = v
        total += trH
    return total

# 逐块（以 pageBreakBefore 段落为分界）
blocks = []
cur = []
for ch in body:
    tag = ch.tag.split('}')[-1]
    if tag == 'p':
        pPr = ch.find(NS + 'pPr')
        has_break = pPr is not None and pPr.find(NS + 'pageBreakBefore') is not None
        if has_break and cur:
            blocks.append(cur); cur = []
        cur.append(('p', ch))
    elif tag == 'tbl':
        cur.append(('tbl', ch))
if cur:
    blocks.append(cur)

print('总块数（含封面/目录）:', len(blocks))
print('版心高度: %.1f pt' % PAGE_PT)
print()

over = []
for i, blk in enumerate(blocks):
    h = 0.0
    kinds = []
    for kind, el in blk:
        if kind == 'p':
            h += para_pt(el); kinds.append('P')
        else:
            h += table_row_pt(el); kinds.append('TBL')
    if h > PAGE_PT - 6:
        over.append((i + 1, round(h, 1), len(blk), ''.join(kinds)))
    if i < 12 or h > PAGE_PT:
        print('块%3d: %7.1f pt  (版心容量 %.0f) 元素=%s' % (i + 1, h, PAGE_PT, ''.join(kinds)))
print()
print('=== 超出或接近版心高度的块数: %d ===' % len(over))
for o in over[:40]:
    print('  块%-4d %7.1f pt  元素%d (%s)' % o)
