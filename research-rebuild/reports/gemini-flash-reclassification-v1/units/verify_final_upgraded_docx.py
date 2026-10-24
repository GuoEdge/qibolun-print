"""全书核验：278 条导语全部入书；检查回填册与升格单元在书芯中的正确性。"""
import json, os, re, zipfile, glob
R = '/storage/Users/currentUser/Documents/岐伯论'
U = R + '/research-rebuild/reports/gemini-flash-reclassification-v1/units'
docs = []
for root, ds, fs in os.walk(R):
    if '_legacy' in root or 'node_modules' in root or '试打样' in root or 'research-rebuild' in root:
        continue
    docs += [os.path.join(root, f) for f in fs if f.endswith('.docx') and '外包封' not in f and not f.startswith('~')]

allt = ''
for d in docs:
    allt += re.sub(r'<[^>]+>', '', zipfile.ZipFile(d).read('word/document.xml').decode('utf-8'))

miss = []
n = 0
for p in glob.glob(U + '/out/B*.json'):
    for u in json.load(open(p, encoding='utf-8'))['units']:
        n += 1
        if u['intro'] not in allt:
            miss.append((os.path.basename(p), u['name']))

print(f'docx 总数: {len(docs)} | 导语总数: {n} | 缺失导语: {miss}')

# 检查升格的四个单元名是否都出现在 document.xml 中
for name in ['事理通觀', '商道心法', '心手造物', '權責界分']:
    print(f'单元名 [{name}] 命中:', name in allt)
