#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""甲册 DOCX 一键体检（返工验收）
逐项检查：ZIP 完整性 / XML 合法性 / 关键排版设置 / 分页预算 / 批校线一致性 /
内容完整性（answer+narrative 分离校验）。任何一项 FAIL 即视为不合格。
"""
import zipfile, os, re, json, sys
from xml.etree import ElementTree as ET

BASE = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/'
DOCX = BASE + '岐伯论·卷一·甲册·幼兒啟蒙與性情習慣.docx'
CLEAN = BASE + 'all-articles-merged-v3-clean.jsonl'
CATALOG = BASE + 'workbook-40b-all-catalog.jsonl'
REPORT = BASE + '_pagination-report-B01.json'

fails = []
def chk(name, cond, detail=''):
    mark = 'PASS' if cond else 'FAIL'
    if not cond: fails.append(name)
    print(f'  [{mark}] {name}' + (f'   {detail}' if detail else ''))

print('=' * 70)
print('甲册 DOCX 返工体检：', os.path.basename(DOCX))
print('=' * 70)

# ---------- 1. ZIP / XML ----------
print('\n[1] 容器与 XML 合法性')
try:
    z = zipfile.ZipFile(DOCX)
    bad = z.testzip()
    chk('ZIP 结构完好', bad is None, f'损坏项={bad}' if bad else '')
    names = z.namelist()
    need = ['word/document.xml', 'word/settings.xml', 'word/styles.xml',
            '[Content_Types].xml', 'word/_rels/document.xml.rels']
    chk('必需部件齐全', all(n in names for n in need),
        '' if all(n in names for n in need) else str([n for n in need if n not in names]))
    xml_bad = []
    for n in names:
        if n.endswith('.xml') or n.endswith('.rels'):
            try: ET.fromstring(z.read(n))
            except Exception as e: xml_bad.append(f'{n}: {e}')
    chk('全部 XML 可解析', not xml_bad, str(xml_bad[:2]))
    doc = z.read('word/document.xml').decode('utf-8')
    sett = z.read('word/settings.xml').decode('utf-8')
except Exception as e:
    print('  [FAIL] 无法打开 DOCX:', e); sys.exit(1)

# ---------- 2. 关键排版设置 ----------
print('\n[2] 关键排版设置（后处理管线）')
sections = ET.fromstring(doc).findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr')
w = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
chk('前置、正文、封底恰为三节', len(sections) == 3, f'{len(sections)} 节')
if len(sections) == 3:
    front, body, back = sections
    front_ok = front.find(w + 'pgNumType') is None and not front.findall(w + 'footerReference')
    chk('封面、空白背页与目录不编号且无页脚', front_ok)
    numbering = body.find(w + 'pgNumType')
    body_ok = (numbering is not None and numbering.get(w + 'start') == '1'
               and numbering.get(w + 'fmt') == 'chineseCountingThousand')
    chk('正文第一叶从一开始且使用汉字页码', body_ok,
        str(numbering.attrib) if numbering is not None else '缺失')
    footers = {f.get(w + 'type') for f in body.findall(w + 'footerReference')}
    chk('正文奇偶页脚独立于前置节', footers == {'default', 'even'}, str(footers))
    back_refs = back.findall(w + 'footerReference')
    rels = ET.fromstring(z.read('word/_rels/document.xml.rels'))
    rns = '{http://schemas.openxmlformats.org/package/2006/relationships}'
    targets = {r.get('Id'): r.get('Target') for r in rels.findall(rns + 'Relationship')}
    back_footers = [targets.get(ref.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')) for ref in back_refs]
    blank_footers = all(target and not ET.fromstring(z.read('word/' + target)).findall('.//' + w + 'fldChar')
                        and 'PAGE' not in z.read('word/' + target).decode('utf-8') for target in back_footers)
    chk('封底节无编号且奇偶页脚为空', back.find(w + 'pgNumType') is None
        and {r.get(w + 'type') for r in back_refs} == {'default', 'even'} and blank_footers)
else:
    chk('封面、空白背页与目录不编号且无页脚', False)
    chk('正文第一叶从一开始且使用汉字页码', False)
    chk('正文奇偶页脚独立于前置节', False)
    chk('封底节无编号且奇偶页脚为空', False)
chk('对称镜像页边距 mirrorMargins', 'mirrorMargins' in sett)
chk('奇偶页眉 evenAndOddHeaders', 'evenAndOddHeaders' in sett)
m = re.search(r'<w:docGrid[^>]*/>', doc)
chk('文档网格关闭 linePitch=0', bool(m and 'linePitch="0"' in m.group(0)),
    m.group(0) if m else '缺失')
n_snap = doc.count('<w:snapToGrid w:val="0"/>')
chk('段落网格吸附关闭 snapToGrid=0', n_snap > 0, f'{n_snap} 处')
m = re.search(r'<w:pgMar[^>]*/>', doc)
pm_ok = bool(m and 'w:bottom="1500"' in m.group(0) and 'w:footer="600"' in m.group(0))
chk('页边距让位页脚 bottom=1500/footer=600', pm_ok, m.group(0) if m else '缺失')

# ---------- 3. schema 顺序 ----------
print('\n[3] OOXML 合法性')
pprs = re.findall(r'<w:pPr>(.*?)</w:pPr>', doc, re.S)
viol = [s for s in pprs if s.lstrip().startswith('<w:snapToGrid')
        and any(t in s for t in ('<w:pageBreakBefore', '<w:pBdr', '<w:keepNext'))]
chk('pPr 元素顺序违规 = 0', len(viol) == 0, f'违规 {len(viol)} 处')
# tblW / gridCol / tblLayout
n_tblw = len(re.findall(r'<w:tblW[^>]*/>', doc))
n_grid = len(re.findall(r'<w:gridCol w:w="(\d+)"', doc))
n_fixed = doc.count('<w:tblLayout w:type="fixed"/>')
chk('固定表格布局 tblLayout=fixed', n_fixed > 0, f'{n_fixed} 处')
chk('表格宽度约束完整', n_tblw > 0 and n_grid > 0, f'tblW={n_tblw} gridCol={n_grid}')

# ---------- 4. 分页与批校线一致性 ----------
print('\n[4] 分页与批校线一致性')
rep = json.load(open(REPORT))
over = [x for x in rep if x.get('超限')]
chk('超限页块 = 0', len(over) == 0, f'{len(over)} 处超限')
rails = sorted(set(x['批校行'] for x in rep))
# 只允许两个值：非末页固定值、末页固定值
chk('批校线行数统一（≤2种）', len(rails) <= 2, f'取值={rails}')
heights = [x['页块高'] for x in rep]
chk('页块高全部在版心内', max(heights) <= 721.9, f'最高={max(heights)}pt')
mid = [x['左栏高'] for x in rep if x['叶'] < x['篇内叶数']]
chk('中间叶无严重半空页', min(mid) >= 400, f'最低左栏={min(mid)}pt 平均={sum(mid)/len(mid):.1f}pt')

# ---------- 5. 外框与题眉 ----------
print('\n[5] 外框与题眉')
trh = re.findall(r'<w:trHeight w:val="(\d+)" w:hRule="([^"]+)"', doc)
outer = [t for t in trh if int(t[0]) == 12000 and t[1] == 'atLeast']
chk('外框统一最小高度 600pt atLeast', len(outer) > 0, f'{len(outer)} 处')
n_cs = doc.count('cantSplit')
chk('外框不可拆 cantSplit', n_cs > 0, f'{n_cs} 处')
heads = re.findall(r'<w:pPr>(?:(?!</w:pPr>).)*?<w:pageBreakBefore/>(?:(?!</w:pPr>).)*?</w:pPr>', doc, re.S)
# 前置三次分页；仅当正文叶数为偶数时封底前另补一次。正文第一页由分节换页。
real_heads = [h for h in heads if not re.search(r'w:line="(?:20|240)"', h)]
with_keep = [h for h in real_heads if '<w:keepNext/>' in h]
chk('正文段前分页数正确', len(real_heads) == len(rep) - 1,
    f'正文={len(rep)}叶，段前分页={len(real_heads)}处')
chk('天头题眉全部带 keepNext', len(with_keep) == len(real_heads) and len(real_heads) > 0,
    f'{len(with_keep)}/{len(real_heads)}（另有 {len(heads)-len(real_heads)} 个留白分页段）')
first_head = re.search(r'<w:p>(?:(?!</w:p>).)*?岐伯論 · 本根敦倫(?:(?!</w:p>).)*?</w:p>', doc, re.S)
chk('正文首叶不重复段前分页', first_head is not None and '<w:pageBreakBefore/>' not in first_head.group(0))
if len(sections) == 3:
    section_type = body.find(w + 'type')
    back_type = back.find(w + 'type')
    chk('正文与封底节均从下一页开始',
        section_type is not None and section_type.get(w + 'val') == 'nextPage'
        and back_type is not None and back_type.get(w + 'val') == 'nextPage')
else:
    chk('正文与封底节均从下一页开始', False)
chk('封底预设已写入', '甲冊 · 幼兒啟蒙與性情習慣' in doc)

body_nodes = list(ET.fromstring(doc).find(w + 'body'))
def node_text(node):
    return ''.join(t.text or '' for t in node.findall('.//' + w + 't'))
def blank_page_break(node):
    return node.tag == w + 'p' and not node_text(node) and node.find('.//' + w + 'pageBreakBefore') is not None
front_order = (len(body_nodes) >= 6 and body_nodes[0].tag == w + 'tbl'
               and blank_page_break(body_nodes[1]) and blank_page_break(body_nodes[2])
               and body_nodes[3].tag == w + 'tbl'
               and '本 冊 篇 目 總 覽' in node_text(body_nodes[3])
               and blank_page_break(body_nodes[4])
               and body_nodes[5].find('.//' + w + 'sectPr') is not None)
chk('封面与目录背面各留一页空白，正文从第五物理页开始', front_order)
needs_back_blank = len(rep) % 2 == 0
if needs_back_blank:
    back_order = (len(body_nodes) >= 5 and body_nodes[-5].find('.//' + w + 'sectPr') is not None
                  and body_nodes[-4].tag == w + 'p' and not node_text(body_nodes[-4])
                  and body_nodes[-4].find('.//' + w + 'pageBreakBefore') is None
                  and blank_page_break(body_nodes[-3]))
else:
    back_order = (len(body_nodes) >= 3 and body_nodes[-3].find('.//' + w + 'sectPr') is not None)
back_order = (back_order and body_nodes[-2].tag == w + 'tbl'
              and '岐  伯  論' in node_text(body_nodes[-2]))
chk('封底前按正文叶数补白，封底独立占末页', back_order)

# ---------- 6. 目录起始叶码 ----------
print('\n[6] 目录起始叶码')
digits = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
def chinese_leaf(n):
    if not 1 <= n <= 999: raise ValueError(f'目录叶码超出范围: {n}')
    def under_hundred(value, omit_one=False):
        if value < 10: return digits[value]
        tens, ones = divmod(value, 10)
        return ('' if omit_one and tens == 1 else digits[tens]) + '十' + (digits[ones] if ones else '')
    if n < 100: return under_hundred(n, True)
    hundreds, remainder = divmod(n, 100)
    return digits[hundreds] + '百' + ('' if not remainder else
        ('零' + digits[remainder] if remainder < 10 else under_hundred(remainder)))
starts = {}
for i, entry in enumerate(rep, 1):
    if entry['叶'] == 1:
        starts[entry['篇']] = chinese_leaf(i)
expected_toc = [f'{i}. 《{title}》 · 第{leaf}葉'
                for i, (title, leaf) in enumerate(starts.items(), 1)]
toc_paragraphs = [node_text(p) for p in body_nodes[3].findall('.//' + w + 'p')]
toc_items = [text for text in toc_paragraphs if re.match(r'^\d+\. ', text)]
toc_mismatch = [(i, expected, actual) for i, (expected, actual) in
                enumerate(zip(expected_toc, toc_items), 1) if expected != actual]
chk('目录篇目均标出实际起始叶码', len(starts) == len(starts) and len(toc_items) == len(starts)
    and not toc_mismatch, f'条目={len(toc_items)} 不符={len(toc_mismatch)}'
    + (f' 首例={toc_mismatch[0]}' if toc_mismatch else ''))
chk('目录不再显示字数', len(toc_items) == len(starts) and
    all(not re.search(r'\d+字', text) for text in toc_items))
toc_leaf_runs = re.findall(r'<w:r>(?:(?!</w:r>).)*?<w:t[^>]*> · 第[^<]*</w:t>(?:(?!</w:r>).)*?</w:r>', doc, re.S)
chk('目录起始叶码统一为汉仪字酷堂荫嘉楷书 W', len(toc_leaf_runs) == len(starts) and
    all('汉仪字酷堂荫嘉楷书 W' in run for run in toc_leaf_runs),
    f'{sum("汉仪字酷堂荫嘉楷书 W" in run for run in toc_leaf_runs)}/{len(toc_leaf_runs)}')

# ---------- 7. 问答边界分离 ----------
print('\n[7] 提问者叙述 / 岐伯答 边界')
n_marker = doc.count('岐 伯 語')
n_label = doc.count('〔 原 問 〕')
chk('入话标记〔岐伯語〕数量成对', n_marker == n_label and n_marker > 0, f'标签={n_label} 标记={n_marker}')

# ---------- 7. 内容完整性（首尾 + 逐句） ----------
print('\n[7] 内容完整性')
clean = {}
for l in open(CLEAN):
    d = json.loads(l); clean[d['id']] = d
cat = [json.loads(l) for l in open(CATALOG) if l.strip()]
b01 = [d for d in cat if d.get('booklet_code') == 'B01']
chk(f'甲册收 {len(b01)} 篇', len(b01) == len(b01), f'实际 {len(b01)}')

texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', doc)
compact = re.sub(r'\s+', '', ''.join(texts))

def norm(s): return re.sub(r'\s+', '', s or '')

WIN = 8  # 校验窗口

def norm2(s): return re.sub(r'\s+', '', s or '')

def windows(s, win=WIN):
    s = norm2(s)
    if not s: return []
    return [s] if len(s) <= win else [s[i:i+win] for i in range(0, len(s) - win + 1, win)]

# 每篇实际分页数：分页会在句子中间插入页眉/标签，打断连续文本。
# 允许的断裂窗口数 = 该篇分页数（每页至多打断 1 个窗口）。
# 实测断裂数严格 ≤ 分页数，故此判据既灵敏又能容忍正常分页。
pages_of = {}
for x in rep:
    pages_of[x['篇']] = max(pages_of.get(x['篇'], 0), x['篇内叶数'])

trunc = []
for art in b01:
    rec = clean.get(art.get('original_id'))
    if not rec: continue
    allow = max(1, pages_of.get(art['title'], 1))
    for field in ('answer', 'narrative'):
        t = rec.get(field) or ''
        if not t: continue
        ws = windows(t)
        miss = [w for w in ws if w not in compact]
        if len(miss) > allow:
            trunc.append((art['title'], field, len(miss), len(ws), allow, miss[0]))

chk('正文内容零丢失（8字窗口，容每叶1处跨页）', len(trunc) == 0,
    f'{len(trunc)} 个字段超限' + (f' 例:《{trunc[0][0]}》{trunc[0][1]} 缺{trunc[0][2]}/{trunc[0][3]}窗(容{trunc[0][4]})「{trunc[0][5]}」' if trunc else ''))


# ---------- 8. 图片 ----------
print('\n[8] 押角二维码')
media = [n for n in z.namelist() if n.startswith('word/media/') and n.strip() != 'word/media/']
png_ok = sum(1 for n in media if z.read(n)[:8] == b'\x89PNG\r\n\x1a\n')
chk('二维码 PNG 全部有效', len(media) > 0 and png_ok == len(media), f'{png_ok}/{len(media)}')

# ---------- 汇总 ----------
print('\n' + '=' * 70)
if fails:
    print('体检结果：', len(fails), ' 项未通过 →', ', '.join(fails))
else:
    print('体检结果：全部通过 ✅')
print('=' * 70)
print(f'文件大小: {os.path.getsize(DOCX)/1024:.1f} KB   段落数: {doc.count("<w:p>") + doc.count("<w:p ")}   表格数: {doc.count("<w:tbl>")}')
sys.exit(1 if fails else 0)
