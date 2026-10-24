#!/usr/bin/env python3
import zipfile,os,json,re,sys
DOCX="/storage/Users/currentUser/Documents/岐伯论/卷七/乙册/岐伯论·卷七·乙册·名相辨析與語言牢籠.docx"
REPORT="/storage/Users/currentUser/Documents/岐伯论/卷七/乙册/_pagination-report-B32.json"
LABEL="乙冊 · 名相辨析與語言牢籠"
EXPECTED=191
BLANKS=2
fail=[]
def ck(n,v):
 print('[%s] %s' % ('PASS' if v else 'FAIL',n)); fail.append(n) if not v else None
with zipfile.ZipFile(DOCX) as z:
 ck('ZIP完整',z.testzip() is None); d=z.read('word/document.xml').decode(); s=z.read('word/settings.xml').decode()
 ck('三节',len(re.findall(r'<w:sectPr(?:\s[^>]*)?>',d))==3); ck('正文起始页码', 'chineseCountingThousand' in d and 'w:start="1"' in d); ck('镜像页边距','mirrorMargins' in s); ck('固定表格', '<w:tblLayout w:type="fixed"/>' in d); ck('目录标签', '本 冊 篇 目 總 覽' in d); ck('封底标签',LABEL in d); ck('留白页数',len(re.findall(r'trHeight[^>]*w:val="14318"',d))==BLANKS); ck('分页报告无超限',not any(x.get('超限') for x in json.load(open(REPORT)))); ck('篇数',len(set(x['篇'] for x in json.load(open(REPORT))))==EXPECTED); media=[n for n in z.namelist() if n.startswith('word/media/') and n != 'word/media/']; ck('二维码有效',bool(media) and all(z.read(n).startswith(b'\x89PNG') for n in media))
print('结果：'+('通过' if not fail else '失败 '+','.join(fail))); sys.exit(bool(fail))
