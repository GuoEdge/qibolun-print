"""移动后单元数越界修正：B25 并单元、B38B 拆单元。"""
import json, shutil, time
from pathlib import Path
D = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units')
TS = time.strftime('%Y%m%d_%H%M%S')
names = set()
for p in (D / 'out').glob('B*.json'):
    names |= {u['name'] for u in json.loads(p.read_text(encoding='utf-8'))['units']}
for n in ('讀書治學', '苦難淬煉'):
    assert n not in names, n

def load(c):
    p = D / 'out' / f'{c}.json'; shutil.copy2(p, str(p) + '.bak_clsfix_' + TS)
    return p, json.loads(p.read_text(encoding='utf-8'))

# B25：兩性對立（3 篇）并入 立場極化
p, b = load('B25')
u = {x['name']: x for x in b['units']}
u['立場極化']['ordinals'] = sorted(u['立場極化']['ordinals'] + u['兩性對立']['ordinals'])
u['立場極化']['intro'] = '極端站隊，往往背離初心。此編辨帶節奏之罪名、先論立場再論是非之弊，兼及男女對立之挑動、跟風之盲從與對立中聯合之難。'
b['units'] = [x for x in b['units'] if x['name'] != '兩性對立']
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding='utf-8')

# B38B：明心辨理 拆出 讀書治學；困中守志 拆出 苦難淬煉
p, b = load('B38B')
u = {x['name']: x for x in b['units']}
READ = {658, 840, 1317, 1320, 1610, 1707, 2346, 2516, 3023, 3290, 3320, 3356, 3989, 4075, 4182, 4200}
SUFF = {9, 581, 756, 1002, 1304, 1347, 1352, 1418, 1636, 2623, 2652, 2657, 2739, 3968, 4033, 4161, 4228}
assert READ <= set(u['明心辨理']['ordinals']) and SUFF <= set(u['困中守志']['ordinals'])
u['明心辨理']['ordinals'] = sorted(set(u['明心辨理']['ordinals']) - READ)
u['明心辨理']['intro'] = '心明則理自見。此編論看透本質之能、觀點與事實之別，兼及概算預測、自洽之疑與大腦過擬合之思。'
u['困中守志']['ordinals'] = sorted(set(u['困中守志']['ordinals']) - SUFF)
u['困中守志']['intro'] = '身陷困厄，所恃者唯心志與自救。是編論習得性無助、屈辱與絕望何以自拔，兼及低谷無援、挫折轉化與信念危機。'
new_read = {'name': '讀書治學', 'intro': '為學之道，貴在成系而致用。此編論讀書之法、知識如何串珠成樹，兼及文理兼修、閱歷互證與真學會之驗。', 'ordinals': sorted(READ)}
new_suff = {'name': '苦難淬煉', 'intro': '苦難必至，詛咒無益。是編論挫折何以淬人成器、樂觀如何持守，兼及天意之辨、吃虧之用與值得之犧牲。', 'ordinals': sorted(SUFF)}
out = []
for x in b['units']:
    out.append(x)
    if x['name'] == '明心辨理': out.append(new_read)
    if x['name'] == '困中守志': out.append(new_suff)
b['units'] = out
p.write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding='utf-8')
print('B25', [(x['name'], len(x['ordinals'])) for x in json.loads((D / 'out/B25.json').read_text(encoding='utf-8'))['units']])
print('B38B', [(x['name'], len(x['ordinals'])) for x in b['units']])
