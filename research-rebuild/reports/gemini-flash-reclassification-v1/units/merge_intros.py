import json, os, glob, shutil, random
B = os.path.dirname(os.path.abspath(__file__))
OUT, IO = os.path.join(B, 'out'), os.path.join(B, 'intro_out')
for f in os.listdir(IO):
    if not f.endswith('.json'):
        os.remove(os.path.join(IO, f))
samples = []
for f in sorted(glob.glob(os.path.join(OUT, '*.json'))):
    shutil.copy(f, f + '.bak_intro_20261016')
    d = json.load(open(f, encoding='utf-8'))
    it = json.load(open(os.path.join(IO, d['code'] + '.json'), encoding='utf-8'))['intros']
    for u in d['units']:
        samples.append((d['code'], u['name'], u['intro'], it[u['name']]))
        u['intro'] = it[u['name']]
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
random.seed(7)
for s in random.sample(samples, 8):
    print(s[0], s[1], '\n  旧:', s[2], '\n  新:', s[3])
print('合并', len(samples))
