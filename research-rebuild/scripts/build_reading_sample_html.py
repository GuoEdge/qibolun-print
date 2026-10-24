#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a printable HTML reading-edition sample from real corpus articles."""
from __future__ import annotations
import csv, html, json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
INDEX = R / "reports/print-index/print-research-index.csv"
PKG = R / "print-20260926-rebuilt-v2"
OUT = R / "print-design-20260927/reading-sample-book.html"
TITLES = ["自知其美", "多余的问题", "5G", "MMA", "各行其道"]

def load_corpus():
    data={}
    for line in CORPUS.open(encoding="utf-8"):
        if line.strip():
            x=json.loads(line); data[x["id"]]=x
    return data

def load_index():
    with INDEX.open(encoding="utf-8-sig", newline="") as f: return list(csv.DictReader(f))

def safe_topic(row):
    return re.sub(r"[／/]", "-", f"{row['primary_print_topic']}" + "-" + row["primary_print_topic_name"])

def image_paths(row):
    d=PKG/safe_topic(row)/"images"
    return sorted(d.glob(f"{int(row['source_ordinal'])}-{row['id']}-*.jpg"), key=lambda p:int(p.stem.rsplit('-',1)[-1]))

def para_html(text):
    blocks=[]
    for p in re.split(r"\n\s*\n", text.strip()):
        p=p.strip()
        if p: blocks.append(f"<p>{html.escape(p).replace(chr(10), '<br>')}</p>")
    return "\n".join(blocks) or '<p class="empty">（正文为空或仅由图片承载。）</p>'

def article_html(row, article):
    imgs=image_paths(row)
    meta=[f"原文链接：见本册来源索引，源序号 {row['source_ordinal']}", f"主专题：{row['primary_print_topic']} {row['primary_print_topic_name']}"]
    if row.get('secondary_print_topic_names'): meta.append("副专题："+row['secondary_print_topic_names'].replace(';','；'))
    if row.get('native_object_paths'): meta.append("官方路径："+row['native_object_paths'].replace(';','；'))
    if row.get('concept_tags'): meta.append("概念："+row['concept_tags'].replace(';','；'))
    flags=[]
    if row.get('classification_status')=='manual_provisional': flags.append('待审')
    if row.get('reading_status') in {'needs_reread','missing_first_pass'}: flags.append(row['reading_status'])
    if row.get('source_body_state')!='text_present': flags.append(row.get('source_body_state','正文状态异常'))
    if flags: meta.append('状态：'+'；'.join(flags))
    img_block=''
    if imgs:
        parts=['<section class="images"><h4>图片</h4>']
        for p in imgs:
            parts.append(f'<figure><img src="{html.escape(str(p))}" alt="{html.escape(row["title"])} 图片"><figcaption>图 {p.stem.rsplit("-",1)[-1]}</figcaption></figure>')
        parts.append('</section>'); img_block='\n'.join(parts)
    return f'''<article class="article" id="source-{row['source_ordinal']}" data-source="{row['source_ordinal']}">
<h2>{int(row['source_ordinal']):04d}　{html.escape(row['title'])}</h2>
<div class="date">{html.escape(row.get('published_date') or '日期未知')}</div>
<h3>提问</h3><p class="question">{html.escape(article.get('question') or '原始提问缺失')}</p>
<h3>正文</h3><section class="body">{para_html(article.get('text') or '')}</section>
{img_block}
<section class="research-meta">{'<br>'.join(html.escape(x) for x in meta)}</section>
<section class="notes"><div>研究笔记</div><i></i><i></i><i></i></section>
</article>'''

def main():
    corpus=load_corpus(); rows=[r for r in load_index() if r['title'] in TITLES]; rows.sort(key=lambda r:TITLES.index(r['title']))
    toc=''.join(f'<li><a href="#source-{r["source_ordinal"]}">{int(r["source_ordinal"]):04d}　{html.escape(r["title"])}</a><span>{html.escape(r["primary_print_topic_name"])}</span></li>' for r in rows)
    articles='\n'.join(article_html(r, corpus[r['id']]) for r in rows)
    doc=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>岐伯论｜阅读正文版样书</title><style>
:root{{--ink:#262421;--muted:#6b665f;--line:#c9c2b8;--paper:#fffdf8;--note:#f3efe7}}*{{box-sizing:border-box}}body{{margin:0;background:#e9e5dd;color:var(--ink);font-family:"Noto Serif CJK SC","Source Han Serif SC",serif;line-height:1.85}}.book{{max-width:820px;margin:0 auto;background:var(--paper);padding:42px 68px 80px;min-height:100vh}}.cover{{min-height:70vh;display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid var(--line);margin-bottom:42px}}h1{{font-size:34px;letter-spacing:.08em;font-weight:500;margin:0 0 18px}}.subtitle{{font-size:18px;color:var(--muted)}}.edition{{margin-top:80px;font-size:13px;color:var(--muted)}}.toc{{page-break-after:always}}.toc h2,.article h2{{font-weight:500;letter-spacing:.04em}}.toc ol{{padding-left:28px}}.toc li{{padding:5px 0;border-bottom:1px dotted var(--line)}}.toc a{{color:var(--ink);text-decoration:none}}.toc span{{float:right;color:var(--muted);font-size:12px}}.article{{page-break-before:always;position:relative;padding-bottom:30px}}.article h2{{font-size:25px;border-bottom:1px solid var(--line);padding-bottom:10px;margin:0 0 4px}}.date{{font-size:13px;color:var(--muted);margin-bottom:28px}}h3{{font-size:15px;font-weight:500;margin:22px 0 7px;color:#5b5044}}.question{{font-size:16px;margin-top:0;padding-left:14px;border-left:3px solid #b1a08c}}.body p{{margin:0 0 13px;text-indent:2em}}.body p:first-child{{text-indent:0}}.images{{margin:28px 0}}figure{{margin:20px 0;text-align:center;break-inside:avoid}}figure img{{max-width:88%;max-height:520px;object-fit:contain;border:1px solid #ddd5ca}}figcaption{{font-size:12px;color:var(--muted);margin-top:4px}}.research-meta{{border-top:1px solid var(--line);margin-top:34px;padding-top:9px;color:var(--muted);font-size:10.5px;line-height:1.65}}.notes{{margin-top:24px;background:var(--note);padding:10px 14px 12px;color:var(--muted);font-size:11px;break-inside:avoid}}.notes i{{display:block;height:25px;border-bottom:1px solid #bdb4a7}}.empty{{color:var(--muted);font-style:italic}}@media print{{body{{background:white}}.book{{max-width:none;margin:0;padding:24mm 20mm 24mm 24mm}}.cover{{min-height:240mm}}}}
</style></head><body><main class="book"><section class="cover"><h1>岐伯论</h1><div class="subtitle">阅读正文版样书</div><div class="edition">单篇模板、图片版式、篇末研究信息与批注空间测试<br>2026年9月27日</div></section><section class="toc"><h2>本样书目录</h2><p>本样书用于确认阅读版结构，不代表最终册号和页码。</p><ol>{toc}</ol></section>{articles}</main></body></html>'''
    OUT.write_text(doc,encoding='utf-8'); print(OUT)
if __name__=='__main__': main()