#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按预估页数重新平衡分册（只出计划，不改源数据、不生成 DOCX）。

规则：
 - 目标 220 页/册，上限 260，下限 140；
 - 专题总页数 ≤ 80 的独立成册（小专题不合并）；
 - 附录册独立，不参与平衡；
 - 册内保持原有文章顺序（发表日期 → 源序号）。
"""
from __future__ import annotations
import json, re
from pathlib import Path

PRINT = Path(__file__).resolve().parents[2] / 'print-20260926-rebuilt-v2'
OUT = Path(__file__).resolve().parents[2] / 'wps-sample-20260927'

BODY_W_MM, BODY_H_MM = 104.5, 172.0
CHAR_W_MM = 10.5 * 0.3515
LINE_H_MM = 10.5 * 0.3515 * 1.5 + 1
LINES_PER_PAGE = int(BODY_H_MM / LINE_H_MM)
CHARS_PER_LINE = int(BODY_W_MM / CHAR_W_MM)
CHARS_PER_PAGE = LINES_PER_PAGE * CHARS_PER_LINE
NOTE_LINES_PER_PAGE = int(BODY_H_MM / 8.0)

TARGET, VMAX, VMIN = 220, 260, 140
SMALL_TOPIC_PAGES = 80
NOTE_EXTRA_PAGES = 2


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
            if re.match(r'^!\[图\s*(\d+)\]\((.+)\)$', ln):
                images.append(ln); continue
            if ln.startswith(('**问**：', '- ', '**', '<!--')):
                continue
            body.append(ln)
        arts.append({'ordinal': m.group(1), 'title': m.group(2),
                     'body': ''.join(body), 'images': images})
    return arts


def article_pages(a):
    chars = len(a['body'])
    p = chars / CHARS_PER_PAGE + len(a['images']) * 0.45 + max(4, min(12, round(chars / 260))) / NOTE_LINES_PER_PAGE + 0.18
    return max(1.0, p)


def volume_overhead(n_articles):
    return 1 + 1 + max(1, n_articles / 26) + max(1, n_articles / 30) + NOTE_EXTRA_PAGES


def pack(articles, target=TARGET, vmax=VMAX, vmin=VMIN):
    """按总页数均分：先定册数，再按累计页数切成等长段落（避免末册过薄或过厚）"""
    pages = [article_pages(a) for a in articles]
    total = sum(pages)
    body_target = target - 30              # 预留封面/目录/索引/笔记页开销
    n = max(1, round(total / body_target))
    while total / n > body_target * 1.25 and n < 40:   # 每册仍偏厚就再加一册
        n += 1
    per = total / n
    groups, cur, acc_total = [], [], 0.0
    for a, p in zip(articles, pages):
        # acc_total 是全局累计，阈值按段递增，保证每段都在 per 附近
        if cur and len(groups) < n - 1 and acc_total + p / 2 > per * (len(groups) + 1):
            groups.append(cur); cur = []
        cur.append(a); acc_total += p
    if cur:
        groups.append(cur)
    return groups


def main():
    topics = []
    for d in sorted(PRINT.iterdir()):
        if not d.is_dir() or not re.match(r'^(A\d{2}|99)-', d.name):
            continue
        vols = sorted(d.glob('volume-*.md'))
        arts = []
        for v in vols:
            arts += parse_md(v.read_text(encoding='utf-8'))
        if not arts:
            continue
        topics.append({'code': d.name[:d.name.index('-')], 'dir': d.name, 'articles': arts})

    plan, summary = [], []
    for t in topics:
        arts = t['articles']
        pages = [article_pages(a) for a in arts]
        total = sum(pages)
        if t['code'] == '99' or total <= SMALL_TOPIC_PAGES:
            groups = [arts]
            rule = '独立成册（附录或小专题）'
        else:
            groups = pack(arts)
            rule = '按页数平衡切分'
        offset = 0
        for i, g in enumerate(groups, 1):
            body_pages = sum(article_pages(a) for a in g)
            est = round(body_pages + volume_overhead(len(g)))
            start, end = offset + 1, offset + len(g)
            offset = end
            plan.append({
                'code': t['code'], 'dir': t['dir'], 'volume': i, 'volumes': len(groups),
                'from': start, 'to': end,
                'articles': len(g), 'first': g[0]['ordinal'], 'last': g[-1]['ordinal'],
                'chars': sum(len(a['body']) for a in g),
                'images': sum(len(a['images']) for a in g),
                'estPages': est, 'rule': rule,
            })
        summary.append({'code': t['code'], 'dir': t['dir'], 'articles': len(arts),
                        'totalPages': round(total), 'oldVolumes': len(list(filter(lambda v: v.parent == PRINT / t['dir'], (PRINT / t['dir']).glob('volume-*.md')))),
                        'newVolumes': len(groups), 'rule': rule})

    pages = [p['estPages'] for p in plan]
    report = {
        'target': TARGET, 'vmax': VMAX, 'vmin': VMIN,
        'oldVolumes': sum(s['oldVolumes'] for s in summary),
        'newVolumes': len(plan),
        'articles': sum(p['articles'] for p in plan),
        'estPagesTotal': sum(pages),
        'estPagesMin': min(pages), 'estPagesMax': max(pages),
        'estPagesAvg': round(sum(pages) / len(pages), 1),
        'withinTarget': sum(1 for x in pages if VMIN <= x <= VMAX),
        'summary': summary, 'plan': plan,
    }
    (OUT / 'BALANCE-PLAN.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')

    lines = ['# 分册平衡方案（按预估页数重排，未改源数据）', '']
    lines.append(f"- 目标 **{TARGET}** 页/册（下限 {VMIN}，上限 {VMAX}），小专题（≤{SMALL_TOPIC_PAGES} 页）与附录独立成册")
    lines.append(f"- 册数：**{report['oldVolumes']} → {report['newVolumes']}**；篇数 {report['articles']}")
    lines.append(f"- 预估页数：合计 {report['estPagesTotal']}，平均 **{report['estPagesAvg']}**，区间 **{report['estPagesMin']}–{report['estPagesMax']}**")
    lines.append(f"- 落在 {VMIN}–{VMAX} 区间的册：**{report['withinTarget']} / {len(plan)}**")
    lines.append('')
    lines.append('| 专题 | 原册数 | 新册数 | 篇数 | 新册页数 |')
    lines.append('|---|---:|---:|---:|---|')
    for s in summary:
        vols = [p['estPages'] for p in plan if p['code'] == s['code']]
        lines.append(f"| {s['dir']} | {s['oldVolumes']} | {s['newVolumes']} | {s['articles']} | {' / '.join(str(v) for v in vols)} |")
    lines.append('')
    lines.append('> 页数为粗估，实际以 WPS 排版为准。方案只生成计划，未改动任何源数据与现有 DOCX。')
    (OUT / 'BALANCE-PLAN.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ('plan', 'summary')}, ensure_ascii=False, indent=1))
    print(f'\n方案：{OUT / "BALANCE-PLAN.md"}')


if __name__ == '__main__':
    main()
