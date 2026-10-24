import json, os, glob, shutil, zipfile, re
R = '/storage/Users/currentUser/Documents/岐伯论'
PK = os.path.join(R, '试打样交付包_卷四甲册上')
m = json.load(open(os.path.join(R, '卷四/甲册/上册/build-manifest.json'), encoding='utf-8'))
src = next(v for v in (m.values() if isinstance(m, dict) else []) if isinstance(v, str) and v.endswith('.docx')) if isinstance(m, dict) else None
if not src or not os.path.exists(src):
    src = max(glob.glob(os.path.join(R, '卷四/甲册/上册/*.docx')), key=os.path.getmtime)
# 校验新导语已入书芯
xml = zipfile.ZipFile(src).read('word/document.xml').decode('utf-8')
txt = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml))
intros = [u['intro'] for u in json.load(open(os.path.join(os.path.dirname(__file__), 'out/B17A.json'), encoding='utf-8'))['units']]
print('书芯', os.path.basename(src), '新导语命中', sum(i in txt for i in intros), '/', len(intros))
old = [f for f in os.listdir(PK) if f.startswith('01_') and f.endswith('.docx')]
dst = os.path.join(PK, old[0] if old else '01_书芯_' + os.path.basename(src))
shutil.copy(src, dst)
zp = PK + '.zip'
if os.path.exists(zp): os.remove(zp)
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(PK)):
        z.write(os.path.join(PK, f), os.path.join(os.path.basename(PK), f))
print('已复制', os.path.basename(dst), '| zip', round(os.path.getsize(zp) / 1024), 'KB')
