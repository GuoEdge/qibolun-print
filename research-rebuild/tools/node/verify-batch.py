#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量校验生成的 DOCX，并粗估每册页数（用于检查分册厚薄是否均匀）。"""
from __future__ import annotations
import json, os, re, sys, zipfile
from pathlib import Path
from xml.dom import minidom

OUT = Path(__file__).resolve().parents[2] / 'wps-sample-20260927' / 'docx-output'
PRINT = Path(__file__).resolve().parents[2] / 'print-20260926-rebuilt-v2'

# A5 版心估算参数（twips → mm）
BODY_W_MM = 148 - 22 - 17.5 - 4      # 版心宽 ≈ 104.5mm
BODY_H_MM = 210 - 18 - 20            # 版心高 ≈ 172mm
CHAR_W_MM = 10.5 * 0.3515            # 10.5pt 字宽
LINE_H_MM = 10.5 * 0.3515 * 1.5 + 1  # 1.5 倍行距 + 段后
LINES_PER_PAGE = int(BODY_H_MM / LINE_H_MM)
CHARS_PER_LINE = int(BODY_W_MM / CHAR_W_MM)
CHARS_PER_PAGE = LINES_PER_PAGE * CHARS_PER_LINE
NOTE_LINE_MM = 8.0                   # 笔记横线行高
NOTE_LINES_PER_PAGE = int(BODY_H_MM / NOTE_LINE_MM)


def estimate_pages(articles, images, note_extra_pages=2):
    total = 0.0
    detail = []
    for a in articles:
        chars = len(a['body'])
        text_pages = chars / CHARS_PER_PAGE
        img_pages = len(a['images']) * 0.45
        lines = max(4, min(12, round(chars / 260)))
        note_pages = lines / NOTE_LINES_PER_PAGE
        meta_pages = 0.18                      # 篇题 + 提问 + 篇末研究信息
        p = text_pages + img_pages + note_pages + meta_pages
        pages = max(1.0, p)                    # 每篇另起一页
        total += pages
        detail.append(round(pages, 2))
    # 前置：封面 1 + 说明 1 + 目录
    front = 1 + 1 + max(1, len(articles) / 26)
    back = max(1, len(articles) / 30) + note_extra_pages
    return round(total + front + back), detail


def parse_md(text):
    arts = []
    for part in re.split(r'(?m)^##\s+', text)[1:]:
        lines = part.splitlines()
        m = re.match(r'(\d+)　(.+)', lines[0].strip())
        if not m:
            continue
        body, images = [], []
        for ln in lines[1:]:
            ln = ln.strip()
            if not ln or ln == '---':
                continue
            img = re.match(r'^!\[图\s*(\d+)\]\((.+)\)$', ln)
            if img:
                images.append(img.group(2)); continue
            if ln.startswith('**问**：') or ln.startswith('- ') or ln.startswith('**') or ln.startswith('<!--'):
                continue
            body.append(ln)
        arts.append({'ordinal': m.group(1), 'title': m.group(2), 'body': ''.join(body), 'images': images})
    return arts


def check_docx(path):
    res = {'file': path.name, 'bytes': path.stat().st_size}
    try:
        z = zipfile.ZipFile(path)
    except Exception as e:
        res['error'] = f'zip 打开失败: {e}'
        return res
    names = z.namelist()
    res['parts'] = len(names)
    res['media'] = len([n for n in names if n.startswith('word/media/') and not n.endswith('/')])
    res['imageDrawings'] = len(re.findall(r'<w:drawing', z.read('word/document.xml').decode('utf-8')))
    bad = []
    for n in names:
        if n.endswith('.xml') or n.endswith('.rels'):
            try:
                minidom.parseString(z.read(n))
            except Exception:
                bad.append(n)
    res['xmlBad'] = bad
    doc = z.read('word/document.xml').decode('utf-8')
    res['paragraphs'] = len(re.findall(r'<w:p[ >]', doc))
    res['sections'] = len(re.findall(r'<w:sectPr', doc))
    res['pageBreaks'] = len(re.findall(r'w:pageBreakBefore', doc))
    res['hyperlinks'] = len(re.findall(r'<w:hyperlink', doc))
    res['hasHeader'] = any('header' in n for n in names)
    res['hasFooter'] = any('footer' in n for n in names)
    res['hasPageField'] = 'PAGE' in doc or any('PAGE' in z.read(n).decode('utf-8') for n in names if 'footer' in n)
    fonts = sorted(set(re.findall(r'w:eastAsia="([^"]+)"', doc + z.read('word/styles.xml').decode('utf-8'))))
    res['fonts'] = fonts
    return res


def main():
    plan_path = OUT.parent / 'BALANCE-PLAN.json'
    plan = json.loads(plan_path.read_text(encoding='utf-8')) if plan_path.exists() else None
    balanced = '--plan' in sys.argv or '--balanced' in sys.argv

    if balanced and plan:
        files = sorted(OUT.glob('*第*-阅读工作本-Node.docx'))
        pmap = {(p['dir'], p['volume']): p for p in plan['plan']}
        rows = []
        for p in files:
            r = check_docx(p)
            m = re.match(r'(.+?)-第(\d+)册-阅读工作本-Node\.docx$', p.name)
            key = (m.group(1), int(m.group(2))) if m else (p.name, 1)
            info = pmap.get(key, {})
            code = key[0][:key[0].index('-')] if '-' in key[0] else key[0]
            r.update({'code': code, 'dir': key[0], 'volume': key[1],
                      'articles': info.get('articles', 0), 'sourceImages': info.get('images', 0),
                      'chars': info.get('chars', 0), 'estPages': info.get('estPages', 0)})
            rows.append(r)
    else:
        files = sorted([p for p in OUT.glob('*volume-*-阅读工作本-Node.docx')])
        rows = []
        for p in files:
            r = check_docx(p)
            m = re.match(r'([^/]+?)-volume-(\d+)-阅读工作本-Node\.docx$', p.name)
            code = m.group(1) if m else p.name[:3]
            vol = int(m.group(2)) if m else 1
            md = PRINT / code / f'volume-{vol:02d}.md'
            if md.exists():
                arts = parse_md(md.read_text(encoding='utf-8'))
                imgs = sum(len(a['images']) for a in arts)
                pages, _ = estimate_pages(arts, imgs)
                r.update({'code': code, 'volume': vol, 'articles': len(arts),
                          'sourceImages': imgs, 'chars': sum(len(a['body']) for a in arts),
                          'estPages': pages})
            rows.append(r)

    rows.sort(key=lambda x: (x.get('code', ''), x.get('volume', 0)))
    total_bytes = sum(r['bytes'] for r in rows)
    bad = [r['file'] for r in rows if r.get('xmlBad') or r.get('error')]
    report = {
        'volumes': len(rows),
        'totalMB': round(total_bytes / 1048576, 1),
        'totalArticles': sum(r.get('articles', 0) for r in rows),
        'totalImages': sum(r.get('media', 0) for r in rows),
        'estPagesTotal': sum(r.get('estPages', 0) for r in rows),
        'estPagesMin': min(r.get('estPages', 0) for r in rows),
        'estPagesMax': max(r.get('estPages', 0) for r in rows),
        'estPagesAvg': round(sum(r.get('estPages', 0) for r in rows) / len(rows), 1),
        'xmlBadFiles': bad,
        'missingHeaderFooter': [r['file'] for r in rows if not (r.get('hasHeader') and r.get('hasFooter'))],
        'missingPageField': [r['file'] for r in rows if not r.get('hasPageField')],
        'imageMismatch': [{'file': r['file'], 'drawings': r.get('imageDrawings'), 'media': r.get('media'), 'plan': r.get('sourceImages')}
                          for r in rows if r.get('sourceImages') is not None and r.get('imageDrawings') != r.get('sourceImages')],
        'rows': rows,
    }
    suffix = '-BALANCED' if balanced else ''
    outjson = OUT.parent / f'BATCH-REPORT{suffix}.json'
    outjson.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')

    # Markdown 报告
    tag = '平衡分册版（52 册，按页数重排）' if balanced else '原分卷版（32 册）'
    lines = [f'# 全量编册报告 · {tag}（Node docx，A5，原图）', '']
    lines.append(f"- 册数 **{report['volumes']}**　文章 **{report['totalArticles']}**　图片 **{report['totalImages']}**")
    lines.append(f"- 总体积 **{report['totalMB']} MB**")
    lines.append(f"- 预估页数：合计 **{report['estPagesTotal']}**，平均 **{report['estPagesAvg']}**，最少 **{report['estPagesMin']}**，最多 **{report['estPagesMax']}**")
    lines.append(f"- XML 异常文件：{bad or '无'}")
    lines.append(f"- 缺页眉页脚：{report['missingHeaderFooter'] or '无'}")
    lines.append(f"- 缺页码域：{report['missingPageField'] or '无'}")
    lines.append('')
    lines.append('| 专题 | 册 | 篇数 | 图片 | 字数 | 预估页数 | 体积(MB) |')
    lines.append('|---|---:|---:|---:|---:|---:|---:|')
    for r in rows:
        lines.append(f"| {r.get('code','')} | {r.get('volume','')} | {r.get('articles',0)} | {r.get('media',0)} | "
                     f"{r.get('chars',0):,} | {r.get('estPages',0)} | {r['bytes']/1048576:.1f} |")
    lines.append('')
    lines.append('> 页数为粗估（按 A5 版心、10.5pt 正文、1.5 倍行距、每篇另起一页、每册 2 页笔记页计算），'
                 '实际页数以 WPS 排版后为准；目录与索引页码仍待回填。')
    md_out = OUT.parent / f'BATCH-REPORT{suffix}.md'
    md_out.write_text('\n'.join(lines), encoding='utf-8')

    print(json.dumps({k: v for k, v in report.items() if k != 'rows'}, ensure_ascii=False, indent=1))
    print(f'\n报告：{md_out}')


if __name__ == '__main__':
    main()
