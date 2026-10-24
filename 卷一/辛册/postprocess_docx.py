#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""成书后处理（以原型为只读参照）：
   1) 页边距/页脚距离重排：bottom=1500, footer=600 —— 将汉字叶码下移，同时保留正文与页脚净空；
   2) 关闭 snapToGrid —— 防止 WPS 按文档网格 linePitch=360(18pt) 重排行高；
   3) 注入 <w:pgNumType w:fmt="chineseCountingThousand"/> —— 呈现正统大写汉字叶码；
   4) 承接原型的 mirrorMargins / evenAndOddHeaders —— 双面打印对称镜像订口；
   5) 把 docx 库自动追加的「分节符段落」（pPr 内含 sectPr 的空段）压成 1pt 行高——
      否则它按默认行高（约 14pt）落在整页留白表格之后放不进剩余 6pt，会外溢成一个
      看不见的空白物理页（鸿蒙 WPS「封面后两张空白页」的另一诱因）。
"""
import zipfile, os, re, sys

BASE = "/storage/Users/currentUser/Documents/岐伯论/卷一/辛册/"

# snapToGrid 在 CT_PPrBase 中的合法位置：位于 pBdr/shd/tabs 之后、spacing/ind/jc 之前。
# 旧版把它粗暴置顶（紧跟 <w:pPr>），违反 schema 顺序，WPS 解析失序 pPr 时行为异常。
_AFTER_SNAP = ['w:spacing', 'w:ind', 'w:contextualSpacing', 'w:mirrorIndents',
               'w:suppressOverlap', 'w:jc', 'w:textDirection', 'w:textAlignment',
               'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr', 'w:pPrChange']

def inject_snap_to_grid(xml):
    def repl(m):
        inner = m.group(1)
        if 'w:snapToGrid' in inner:
            return m.group(0)
        for tag in _AFTER_SNAP:
            t = re.search(r'<' + tag + r'[ >/]', inner)
            if t:
                return '<w:pPr>' + inner[:t.start()] + '<w:snapToGrid w:val="0"/>' + inner[t.start():] + '</w:pPr>'
        return '<w:pPr>' + inner + '<w:snapToGrid w:val="0"/></w:pPr>'
    return re.sub(r'<w:pPr>(.*?)</w:pPr>', repl, xml, flags=re.S)

def shrink_section_break_paragraphs(xml):
    # docx 库在每个非末节末尾自动追加一个「空段 + pPr 内嵌 sectPr」作为分节符。
    # 该段默认行高约 14pt；若前一页被整页留白表格占满（仅余约 6pt），它会外溢到下一页，
    # 形成一个看不见的空白物理页。此处把这类段落统一压成 before=0/after=0/1pt 精确行高。
    # spacing 在 schema 中位于 sectPr 之前，直接插到 sectPr 前即可。
    count = [0]
    def repl(m):
        inner = m.group(1)
        if '<w:sectPr' not in inner or '<w:spacing' in inner:
            return m.group(0)
        count[0] += 1
        return ('<w:pPr>' + inner.replace('<w:sectPr',
                '<w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/><w:sectPr', 1)
                + '</w:pPr>')
    out = re.sub(r'<w:pPr>(.*?)</w:pPr>', repl, xml, flags=re.S)
    print('分节符段落压缩    :', count[0], ' (须为 2)')
    return out

DOCX = BASE + "岐伯论·卷一·辛册·宗族傳承與喪祭奠儀.docx"
PROTOTYPE = "/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/岐伯论-现代学者批校手卷本-可编辑原型.docx"

with zipfile.ZipFile(PROTOTYPE) as zp:                       # 只读
    proto_settings = zp.read('word/settings.xml')

pMar = ('<w:pgMar w:top="900" w:right="1020" w:bottom="1500" w:left="1587" '
        'w:header="620" w:footer="600" w:gutter="0"/>')

tmp = DOCX + '.tmp'
with zipfile.ZipFile(DOCX) as zin, zipfile.ZipFile(tmp, 'w') as zout:
    for it in zin.infolist():
        if it.filename == 'word/settings.xml':
            zout.writestr(it, proto_settings)
        elif it.filename == 'word/document.xml':
            x = zin.read(it.filename).decode('utf-8')
            # 1) 页边距与页脚距离
            x = re.sub(r'<w:pgMar[^>]*/>', pMar, x)
            # 2) 关闭网格吸附（按 schema 顺序注入 pPr）
            x = inject_snap_to_grid(x)
            # 2b) 文档网格线距归零，双保险
            x = re.sub(r'<w:docGrid[^>]*/>', '<w:docGrid w:type="default" w:linePitch="0" w:charSpace="0"/>', x)
            # 2c) 分节符空段压成 1pt，防外溢出幽灵空白页
            x = shrink_section_break_paragraphs(x)
            # 4) 仅修改现有页码节点，保留正文节的 start=1；前置节不得生成页码。
            def chinese_page_number(m):
                start = re.search(r'\bw:start="(\d+)"', m.group(0))
                suffix = f' w:start="{start.group(1)}"' if start else ''
                return f'<w:pgNumType w:fmt="chineseCountingThousand"{suffix}/>'
            x = re.sub(r'<w:pgNumType[^>]*/>', chinese_page_number, x)
            # 仅正文节编号；前置节与封底节移除 docx 库自动写入的默认页码节点。
            sections = [0]
            def number_body_section(m):
                sections[0] += 1
                section = m.group(0)
                if sections[0] != 2:
                    return re.sub(r'<w:pgNumType[^>]*/>', '', section)
                return section
            x = re.sub(r'<w:sectPr(?:\s[^>]*)?>.*?</w:sectPr>', number_body_section, x, flags=re.S)
            if sections[0] != 3:
                raise ValueError(f'预期前置节、正文节、封底节共三节，实际 {sections[0]} 节')
            zout.writestr(it, x.encode('utf-8'))
        elif it.filename.startswith('word/footer'):
            x = zin.read(it.filename).decode('utf-8')
            x = inject_snap_to_grid(x)
            zout.writestr(it, x.encode('utf-8'))
        else:
            zout.writestr(it, zin.read(it.filename))
os.replace(tmp, DOCX)

with zipfile.ZipFile(DOCX) as z:
    s = z.read('word/settings.xml').decode()
    d = z.read('word/document.xml').decode()
    print('mirrorMargins      :', 'mirrorMargins' in s)
    print('evenAndOddHeaders  :', 'evenAndOddHeaders' in s)
    print('pgMar              :', re.findall(r'<w:pgMar[^>]*/>', d))
    print('pgNumType          :', re.findall(r'<w:pgNumType[^>]*/>', d))
    print('snapToGrid 段落数  :', d.count('snapToGrid'))
    print('cantSplit 行数     :', d.count('cantSplit'))
    # 题眉（天头「岐伯論 · …」）必须带 keepNext，才能与外框同叶
    heads = re.findall(r'<w:pPr>(?:(?!</w:pPr>).)*?<w:pageBreakBefore/>(?:(?!</w:pPr>).)*?</w:pPr>', d, re.S)
    with_keep = [h for h in heads if '<w:keepNext/>' in h]
    print('天头题眉段         :', len(heads), ' (带 keepNext:', len(with_keep), ')')
    # snapToGrid 是否仍存在 schema 顺序违规（置顶且其后有 pageBreakBefore/pBdr）
    pprs = re.findall(r'<w:pPr>(.*?)</w:pPr>', d, re.S)
    viol = [s for s in pprs
            if s.lstrip().startswith('<w:snapToGrid')
            and any(t in s for t in ('<w:pageBreakBefore', '<w:pBdr', '<w:keepNext'))]
    print('snapToGrid 违规段  :', len(viol), ' (须为 0)')
    print('docGrid            :', re.findall(r'<w:docGrid[^>]*/>', d))
    print('表格宽度(tblW)     :', sorted(set(re.findall(r'<w:tblW w:w="(\d+)"', d)), key=lambda v: -int(v))[:5])
    print('大小               :', round(os.path.getsize(DOCX) / 1024, 1), 'KB')
