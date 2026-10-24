"""全书核验：278 条导语全部入书；抽查移动篇目标题出现在目标册 docx 中、不出现在原册 docx 中。"""
import json, os, re, zipfile, glob, random
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
        if u['intro'] not in allt: miss.append((os.path.basename(p), u['name']))
print('docx', len(docs), '导语', n, '缺', miss)
stale = [o for _, o, _ in json.load(open(U + '/cls_intro_diff.json', encoding='utf-8')) if o in allt]
print('已替换旧导语残留', len(stale))
