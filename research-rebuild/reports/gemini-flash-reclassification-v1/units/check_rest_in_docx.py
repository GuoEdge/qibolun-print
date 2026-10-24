import json, os, re, zipfile
R = '/storage/Users/currentUser/Documents/岐伯论'
U = R + '/research-rebuild/reports/gemini-flash-reclassification-v1/units'
diff = json.load(open(U + '/rest_intro_diff.json', encoding='utf-8'))
docs = []
for root, ds, fs in os.walk(R):
    if '_legacy' in root or 'node_modules' in root or '试打样' in root or 'research-rebuild' in root:
        continue
    docs += [os.path.join(root, f) for f in fs if f.endswith('.docx') and '外包封' not in f and not f.startswith('~')]
texts = {}
for d in docs:
    x = zipfile.ZipFile(d).read('word/document.xml').decode('utf-8')
    texts[d] = re.sub(r'<[^>]+>', '', x)
hit = miss = stale = 0
for code, rows in diff.items():
    for name, old, new in rows:
        if any(new in t for t in texts.values()): hit += 1
        else: miss += 1; print('缺', code, name)
        if any(old in t for t in texts.values()): stale += 1; print('旧文残留', code, name)
print('docx', len(docs), '命中', hit, '缺', miss, '旧文残留', stale)
