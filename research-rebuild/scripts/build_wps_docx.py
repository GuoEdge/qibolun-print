#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build WPS-editable DOCX from Qibo reading volumes without external packages."""
from __future__ import annotations
import html, json, re, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'research-rebuild/print-20260926-rebuilt-v2/A21-体育、运动与竞技伦理/volume-01.md'
OUT = ROOT / 'research-rebuild/wps-sample-20260927/docx-output/A21-体育、运动与竞技伦理-阅读工作本.docx'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def esc(s: str) -> str:
    return html.escape(s or '', quote=False)


def style_ref(sid: str) -> str:
    return f'<w:pStyle w:val="{sid}"/>'


def runs(text: str, size: int, bold: bool = False, color: str | None = None, font: str | None = None):
    props = ['<w:rPr>']
    if bold:
        props.append('<w:b/>')
    if color:
        props.append(f'<w:color w:val="{color}"/>')
    props.append(f'<w:sz w:val="{size * 2}"/>')
    if font:
        props.append(f'<w:rFonts w:ascii="{font}" w:eastAsia="{font}" w:hAnsi="{font}"/>')
    props.append('</w:rPr>')
    rpr = ''.join(props)
    parts = []
    for chunk in re.split(r'(\n)', text):
        if chunk == '\n':
            parts.append('<w:r><w:br/></w:r>')
        elif chunk:
            parts.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(chunk)}</w:t></w:r>')
    return ''.join(parts)


def para(text: str, size: int = 21, bold: bool = False, color: str | None = None,
         align: str | None = None, indent: int = 0, before: int = 0, after: int = 120,
         font: str | None = None, rule: str | None = None, style_id: str | None = None):
    ppr = ['<w:pPr>']
    if style_id:
        ppr.append(style_ref(style_id))
    if align:
        ppr.append(f'<w:jc w:val="{align}"/>')
    if indent:
        ppr.append(f'<w:ind w:firstLineChars="{indent * 100}"/>')
    ppr.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="360" w:lineRule="auto"/>')
    if rule:
        ppr.append('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" '
                   f'w:color="{rule}"/></w:pBdr>')
    ppr.append('</w:pPr>')
    return f'<w:p>{"".join(ppr)}{runs(text, size, bold, color, font)}</w:p>'


def note_block(lines: int):
    out = [para('研究笔记', size=16, bold=True, color='7A6D5E', before=160, after=60, font='微软雅黑', style_id='QBLNoteLabel')]
    for _ in range(lines):
        out.append(para('', size=16, after=200, rule='D9C9AE'))
    return ''.join(out)


def build_styles() -> str:
    def style(sid: str, name: str, size: int, font: str, color: str | None = None,
              bold: bool = False, before: int = 0, after: int = 120, align: str | None = None,
              indent: int = 0, based: str | None = None, next_style: str | None = None):
        rpr = ['<w:rPr>']
        if bold:
            rpr.append('<w:b/>')
        if color:
            rpr.append(f'<w:color w:val="{color}"/>')
        rpr.append(f'<w:rFonts w:ascii="{font}" w:eastAsia="{font}" w:hAnsi="{font}"/>')
        rpr.append(f'<w:sz w:val="{size * 2}"/>')
        rpr.append('</w:rPr>')
        ppr = ['<w:pPr>']
        if align:
            ppr.append(f'<w:jc w:val="{align}"/>')
        if indent:
            ppr.append(f'<w:ind w:firstLineChars="{indent * 100}"/>')
        ppr.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="360" w:lineRule="auto"/>')
        ppr.append('</w:pPr>')
        extra = f'<w:basedOn w:val="{based}"/>' if based else ''
        nxt = f'<w:next w:val="{next_style}"/>' if next_style else ''
        return (f'<w:style w:type="paragraph" w:styleId="{sid}">'
                f'<w:name w:val="{name}"/>{extra}{nxt}{"".join(ppr)}{"".join(rpr)}</w:style>')

    body = [
        style('QBLBody', 'QBL-Body', 21, '宋体', after=120, indent=2),
        style('QBLArticleTitle', 'QBL-ArticleTitle', 32, '宋体', bold=True, before=0, after=100),
        style('QBLQuestion', 'QBL-Question', 22, '宋体', after=160),
        style('QBLQuestionLabel', 'QBL-QuestionLabel', 15, '微软雅黑', color='A74736', bold=True, before=180, after=40),
        style('QBLBodyLabel', 'QBL-BodyLabel', 15, '微软雅黑', color='A74736', bold=True, before=180, after=40),
        style('QBLResearchMeta', 'QBL-ResearchMeta', 16, '微软雅黑', color='6B6258', after=20),
        style('QBLResearchLabel', 'QBL-ResearchLabel', 15, '微软雅黑', color='7A6D5E', bold=True, before=200, after=40),
        style('QBLNoteLabel', 'QBL-NoteLabel', 16, '微软雅黑', color='7A6D5E', bold=True, before=160, after=60),
        style('QBLCoverTitle', 'QBL-CoverTitle', 64, '宋体', bold=True, align='center', before=2400, after=600),
        style('QBLCoverSubtitle', 'QBL-CoverSubtitle', 28, '宋体', color='A74736', align='center', after=900),
        style('QBLCoverEdition', 'QBL-CoverEdition', 20, '宋体', color='7A6D5E', align='center', after=400),
        style('QBLFrontTitle', 'QBL-FrontTitle', 28, '宋体', bold=True, after=200),
        style('QBLTOC', 'QBL-TOC', 20, '微软雅黑', after=40),
        style('QBLIndex', 'QBL-Index', 18, '微软雅黑', after=40),
        style('QBLHint', 'QBL-Hint', 18, '微软雅黑', color='7A6D5E', before=240),
    ]
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:styles xmlns:w="{W}"><w:docDefaults><w:rPrDefault><w:rPr>'
            '<w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="宋体"/>'
            '<w:sz w:val="21"/></w:rPr></w:rPrDefault></w:docDefaults>'
            f'{"".join(body)}</w:styles>')


def parse_articles(text: str):
    articles = []
    for part in re.split(r'(?m)^##\s+', text)[1:]:
        lines = part.splitlines()
        head = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        m = re.match(r'(\d+)　(.+)', head)
        if m:
            articles.append((m.group(1), m.group(2), body))
    return articles


def article_xml(ordinal: str, title: str, body: str):
    out = [para(f'{ordinal}　{title}', size=32, bold=True, before=0, after=100, rule='C9B99F', style_id='QBLArticleTitle')]
    meta, question, notes = [], None, []
    in_meta = False
    for line in body.splitlines():
        if line.startswith('**问**：'):
            question = line[6:]
            continue
        if line.startswith('- 日期：'):
            meta.append(line[2:])
            in_meta = False
            continue
        if line.startswith('- 证据状态：'):
            in_meta = True
            meta.append(line[2:])
            continue
        if line.startswith('- 标记：') or line.startswith('- 官方对象') or line.startswith('- 23 概念'):
            meta.append(line[2:])
            continue
        if line.startswith('![图'):
            notes.append(f'图片：{line[2:].split("](")[0]}')
            continue
        if line.startswith('_（') and line.endswith('）_'):
            notes.append(line[2:-2])
            continue
        if line == '---':
            continue
        if line.startswith('- ') or line.startswith('**') or line.startswith('### '):
            meta.append(line.replace('**', '').replace('### ', ''))
            continue
        if line.strip():
            notes.append(line)
    if question:
        out.append(para('提问', size=15, bold=True, color='A74736', before=180, after=40, font='微软雅黑', style_id='QBLQuestionLabel'))
        out.append(para(question, size=22, after=160, style_id='QBLQuestion'))
    out.append(para('正文', size=15, bold=True, color='A74736', before=180, after=40, font='微软雅黑', style_id='QBLBodyLabel'))
    for p in notes:
        out.append(para(p, size=21, indent=2, after=120, style_id='QBLBody'))
    if meta:
        out.append(para('研究信息', size=15, bold=True, color='7A6D5E', before=200, after=40, font='微软雅黑', style_id='QBLResearchLabel'))
        for m in meta:
            out.append(para(m, size=16, color='6B6258', after=20, font='微软雅黑', style_id='QBLResearchMeta'))
    out.append(note_block(4))
    return ''.join(out)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = SRC.read_text(encoding='utf-8')
    articles = parse_articles(text)
    body = []
    body.append(para('岐伯论', size=64, bold=True, align='center', before=2400, after=600, style_id='QBLCoverTitle'))
    body.append(para('体育、运动与竞技伦理', size=28, align='center', color='A74736', after=900, style_id='QBLCoverSubtitle'))
    body.append(para('阅读正文版 · 研究工作本', size=20, align='center', color='7A6D5E', after=400, style_id='QBLCoverEdition'))
    body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    body.append(para('本册说明', size=28, bold=True, after=200, rule='C9B99F', style_id='QBLFrontTitle'))
    body.append(para('本册为 WPS 阅读工作本样册。正文来自第二轮 rebuild 的 A21 专题册，保留文章顺序、提问、正文、篇末研究信息和研究笔记空间。', size=21, indent=2, after=200, style_id='QBLBody'))
    body.append(para('本册目录', size=24, bold=True, before=280, after=160, style_id='QBLFrontTitle'))
    for ordinal, title, _ in articles:
        body.append(para(f'{ordinal}　{title}', size=20, after=40, font='微软雅黑', style_id='QBLTOC'))
    body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    for ordinal, title, content in articles:
        body.append(article_xml(ordinal, title, content))
        body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    body.append(para('本册索引', size=28, bold=True, after=200, rule='C9B99F', style_id='QBLFrontTitle'))
    for ordinal, title, _ in articles:
        body.append(para(f'{ordinal}　{title}　　页码待回填', size=18, after=40, font='微软雅黑', style_id='QBLIndex'))
    body.append(para('WPS 编辑提示：可在 WPS 中直接修改字体、分页、批注、图片、目录和方印；后续批量调整将回写到生成模板。', size=18, color='7A6D5E', before=240, font='微软雅黑', style_id='QBLHint'))
    sect = ('<w:sectPr><w:pgSz w:w="8391" w:h="11906"/>'
            '<w:pgMar w:top="1021" w:right="992" w:bottom="1134" w:left="1247" '
            'w:header="709" w:footer="709" w:gutter="227"/></w:sectPr>')
    body.append(sect)
    document = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:document xmlns:w="{W}"><w:body>{"".join(body)}</w:body></w:document>')
    content_types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                     '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                     '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                     '<Default Extension="xml" ContentType="application/xml"/>'
                     '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                     '</Types>')
    styles = build_styles()
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<dc:title>岐伯论 · 体育、运动与竞技伦理 · 阅读工作本</dc:title>'
            '<dc:creator>岐伯论编册生成器</dc:creator>'
            '<cp:lastModifiedBy>岐伯论编册生成器</cp:lastModifiedBy>'
            '</cp:coreProperties>')
    app = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
           'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
           '<Application>Qibo Reading Compiler</Application></Properties>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
            '</Relationships>')
    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
                '</Relationships>')
    content_types = content_types.replace(
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>',
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>')
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', content_types)
        z.writestr('_rels/.rels', rels)
        z.writestr('word/document.xml', document)
        z.writestr('word/_rels/document.xml.rels', doc_rels)
        z.writestr('word/styles.xml', styles)
        z.writestr('docProps/core.xml', core)
        z.writestr('docProps/app.xml', app)
    print(json.dumps({'docx': str(OUT), 'bytes': OUT.stat().st_size, 'articles': len(articles)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
