"""
单元升格脚本：将庸俗杂项单元名升级为典雅古籍单元名，并更新导语
1. B02/世情雜論 -> 事理通觀
2. B22B/商外人生 -> 商道心法
3. B20C/技藝格物 -> 心手造物
4. B03/是非權界 -> 權責界分
"""
import json, os, shutil, time

U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
TS = time.strftime('%Y%m%d_%H%M%S')

RENAMES = {
    'B02': ('世情雜論', '事理通觀', '事理紛繁，由近及遠皆可觀。是編借公共事件辨世道人心，因謠言私德推制度公信；見微知著，窮理致用。'),
    'B22B': ('商外人生', '商道心法', '經商謀利，終歸於立身為人。是編論財富聚散之度、冒險自負之責，兼及商道之餘如何持守良知、安頓身心。'),
    'B20C': ('技藝格物', '心手造物', '器以載道，技進乎道。此編論建模繪圖、字體工藝與手藝之精，見心手相應之妙，兼推獨立造物之實。'),
    'B03': ('是非權界', '權責界分', '是非之辨，要在權責相當。此編論管教邊界、資訊差之責與防身自保，兼辨制度失靈之際如何自衛守權。')
}

for code, (old_name, new_name, new_intro) in RENAMES.items():
    p = os.path.join(U, 'out', f'{code}.json')
    d = json.load(open(p, encoding='utf-8'))
    shutil.copy2(p, p + '.bak_rename_' + TS)
    found = False
    for u in d['units']:
        if u['name'] == old_name:
            u['name'] = new_name
            u['intro'] = new_intro
            found = True
            break
    assert found, f'{code} 未找到 {old_name}'
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{code}: {old_name} -> {new_name} 升格完成')
