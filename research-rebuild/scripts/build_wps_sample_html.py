#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build an editable WPS-oriented HTML sample from a complete topic volume."""
from __future__ import annotations
import html, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'research-rebuild/print-20260926-rebuilt-v2/A21-体育、运动与竞技伦理/volume-01.md'
OUT=ROOT/'research-rebuild/wps-sample-20260927/A21-体育、运动与竞技伦理-阅读工作本.html'

def esc(s): return html.escape(s, quote=False)

def parse_articles(text):
    parts=re.split(r'(?m)^##\s+',text)
    articles=[]
    for part in parts[1:]:
        lines=part.splitlines(); head=lines[0].strip(); body='\n'.join(lines[1:]).strip()
        m=re.match(r'(\d+)　(.+)',head)
        if m: articles.append((m.group(1),m.group(2),body))
    return articles

def transform_body(body):
    out=[]
    in_meta=False
    for line in body.splitlines():
        if line.startswith('- 证据状态：'): in_meta=True
        if line.startswith('**问**：'):
            out.append(f'<div class="question">{esc(line[6:])}</div>'); continue
        if line.startswith('![图'):
            out.append(f'<div class="image-placeholder">{esc(line)}</div>'); continue
        if line.startswith('_（') and line.endswith('）_'):
            out.append(f'<p class="note">{esc(line[2:-2])}</p>'); continue
        if line=='---':
            continue
        if line.startswith('- ') or line.startswith('**') or line.startswith('### '):
            if not in_meta: out.append(f'<p class="meta">{esc(line)}</p>')
            else: out.append(f'<p class="meta">{esc(line)}</p>')
            continue
        if line.strip(): out.append(f'<p>{esc(line)}</p>')
    return '\n'.join(out)

def main():
    text=SRC.read_text(encoding='utf-8'); title='A21 体育、运动与竞技伦理'; articles=parse_articles(text)
    toc=''.join(f'<li><span>{ordn}</span>{esc(t)}<em>页码待回填</em></li>' for ordn,t,_ in articles)
    blocks=[]
    for ordn,t,b in articles:
        blocks.append(f'''<article class="article" id="a-{ordn}"><h2>{ordn}　{esc(t)}</h2><div class="article-body">{transform_body(b)}</div><div class="research-notes"><strong>研究笔记</strong><div></div><div></div><div></div><div></div></div></article>''')
    doc=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>{title} · WPS 阅读工作本</title><style>
@page{{size:A5; margin:18mm 18mm 20mm 22mm}}body{{margin:0;background:#fff;color:#24201b;font-family:"Noto Serif CJK SC","Source Han Serif SC","SimSun",serif;line-height:1.85}}.book{{max-width:760px;margin:auto}}.cover{{height:245mm;page-break-after:always;display:flex;flex-direction:column;align-items:center;justify-content:center;border:8px double #254458;background:#f8f3e8;position:relative}}.cover h1{{font-size:42pt;font-weight:500;writing-mode:vertical-rl;letter-spacing:.25em;margin:0 0 26mm}}.cover .slip{{border:1px solid #a74736;color:#a74736;padding:12px 18px;writing-mode:vertical-rl;font-size:14pt}}.seal{{position:absolute;right:18mm;top:18mm;border:2px solid #a74736;color:#a74736;padding:8px;font-size:15pt;writing-mode:vertical-rl}}.front{{page-break-after:always}}h2{{font-size:21pt;font-weight:500;border-bottom:1px solid #c9b99f;padding-bottom:8px;margin:0 0 5px}}h3{{font-size:14pt;font-weight:500;color:#a74736}}.toc li{{list-style:none;border-bottom:1px dotted #c9b99f;padding:4px 0}}.toc li span{{display:inline-block;width:48px;color:#a74736}}.toc li em{{float:right;color:#7a6d5e;font-style:normal;font-size:9pt}}.article{{page-break-before:always}}.article h2{{margin-top:0}}.article-body p{{margin:0 0 9px;text-indent:2em}}.article-body p:first-child{{text-indent:0}}.question{{border-left:3px solid #b78a4b;background:#f7f0e3;padding:8px 12px;margin:14px 0 20px;font-size:13pt;text-indent:0}}.meta{{font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;font-size:8.5pt;color:#6b6258;text-indent:0!important}}.note{{font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;color:#7a6d5e;font-size:9pt;text-indent:0!important}}.image-placeholder{{border:1px dashed #b78a4b;background:#faf6ed;color:#7a6d5e;text-align:center;padding:18px;margin:14px 0;font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;font-size:9pt}}.research-notes{{margin-top:20px;padding:8px 12px;background:#fbf7ee;border:1px solid #d9c9ae;font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;font-size:9pt;color:#7a6d5e;page-break-inside:avoid}}.research-notes div{{height:20px;border-bottom:1px solid #d9c9ae}}.backmatter{{page-break-before:always}}table{{border-collapse:collapse;width:100%;font-family:"Noto Sans CJK SC","Microsoft YaHei",sans-serif;font-size:9pt}}td,th{{border-bottom:1px solid #d9c9ae;padding:6px;text-align:left}}@media screen{{body{{background:#d9d1c3}}.book{{background:#fff;padding:40px 65px;box-shadow:0 8px 28px rgba(0,0,0,.12)}}}}
</style></head><body><main class="book"><section class="cover"><div class="seal">岐伯<br>论</div><h1>岐伯论</h1><div class="slip">体育、运动与竞技伦理<br>阅读正文版 · 研究工作本</div></section><section class="front"><h2>体育、运动与竞技伦理</h2><p>本册为 WPS 阅读工作本样册。正文内容来自岐伯论第二轮 rebuild 的 A21 专题册，保留文章顺序、提问、正文、篇末研究信息和研究笔记空间。</p><h3>本册目录</h3><ol class="toc">{toc}</ol></section>{''.join(blocks)}<section class="backmatter"><h2>本册索引（页码待回填）</h2><table><tr><th>源序号</th><th>标题</th><th>页码</th></tr>{''.join(f'<tr><td>{o}</td><td>{esc(t)}</td><td>待回填</td></tr>' for o,t,_ in articles)}</table><h3>WPS 编辑提示</h3><p>本样册适合在 WPS 中继续调整字体、分页、批注、图片和目录。后续确认的批量修改将回写到生成模板。</p></section></main></body></html>'''
    OUT.write_text(doc,encoding='utf-8'); print(OUT)
if __name__=='__main__': main()
