"""扫描全部生效 docx 中含“冊”的 run 所用字体，并核对本机字体文件是否含 U+518A。"""
import json, os, glob, re, zipfile, collections
from fontTools.ttLib import TTFont
R = '/storage/Users/currentUser/Documents/岐伯论'
B = R + '/research-rebuild/reports/gemini-flash-reclassification-v1'
# 1) 字体名 -> 是否含冊
fonts = {}
for d in ['/storage/Users/currentUser/Download', '/storage/Users/currentUser/Download/com.huawei.hmos.browser', '/system/fonts']:
    for f in glob.glob(d + '/*'):
        if not f.lower().endswith(('.ttf', '.otf', '.ttc')): continue
        try:
            fs = TTFont(f, fontNumber=0, lazy=True)
            has = 0x518A in fs.getBestCmap()
            for rec in fs['name'].names:
                if rec.nameID in (1, 4):
                    try: fonts[rec.toUnicode().strip()] = (has, os.path.basename(f))
                    except Exception: pass
        except Exception: pass
# 2) docx 中含冊 run 的字体
docs = [os.path.join(B, '..', '..', '..', '..', e['dir']) for e in []]
m = json.load(open(B + '/spine_manifest.json', encoding='utf-8'))
files = []
for e in m:
    p = e['dir'] if os.path.isabs(e['dir']) else os.path.join(R, e['dir'])
    mf = os.path.join(p, 'build-manifest.json')
    cand = sorted(glob.glob(p + '/*.docx'), key=os.path.getmtime)
    if cand: files.append(cand[-1])
files += glob.glob(R + '/*外包封*.docx') + glob.glob(R + '/试打样交付包_卷四甲册上/*.docx')
use = collections.Counter(); ex = {}
for f in files:
    x = zipfile.ZipFile(f).read('word/document.xml').decode('utf-8')
    for r in re.findall(r'<w:r>.*?</w:r>|<w:r .*?</w:r>', x, re.S):
        t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', r))
        if '冊' not in t: continue
        fm = re.search(r'w:eastAsia="([^"]+)"', r)
        fn = fm.group(1) if fm else '(默认)'
        use[fn] += t.count('冊'); ex.setdefault(fn, (os.path.basename(f), t[:30]))
print('扫描', len(files), '个 docx')
for fn, c in use.most_common():
    st = fonts.get(fn)
    print(f'{fn}\t冊×{c}\t字库含冊={st[0] if st else "未找到字体文件"}\t{st[1] if st else ""}\t例:{ex[fn]}')
print('夏蝉', {k: v for k, v in fonts.items() if '夏蝉' in k or 'XiaChan' in k})
