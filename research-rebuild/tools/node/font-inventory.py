#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""枚举系统字体并解析 sfnt name 表，得到真实字体名（中文名优先）。仅用标准库。"""
from __future__ import annotations
import json, os, struct, sys

DEFAULT_DIRS = [
    '/system/fonts',
    '/storage/Users/currentUser/Download',
    '/storage/Users/currentUser/Documents',
    '/storage/Users/currentUser/HO_DATA_EXT_MISC/Download',
]
DIRS = sys.argv[1:] or DEFAULT_DIRS
EXTS = ('.ttf', '.otf', '.ttc')


def u16(b, o): return struct.unpack('>H', b[o:o + 2])[0]


def read_name_table(data: bytes, base: int = 0):
    """返回 {nameID: {lang: text}} 的简化结构"""
    if len(data) < base + 12:
        return {}
    num_tables = u16(data, base + 4)
    name_off = None
    for i in range(num_tables):
        rec = base + 12 + i * 16
        if rec + 16 > len(data):
            break
        tag = data[rec:rec + 4].decode('latin-1', 'ignore')
        if tag == 'name':
            name_off = struct.unpack('>I', data[rec + 8:rec + 12])[0]
            break
    if name_off is None:
        return {}
    o = name_off
    if o + 6 > len(data):
        return {}
    count = u16(data, o + 2)
    str_off = u16(data, o + 4)
    out = {}
    for i in range(count):
        r = o + 6 + i * 12
        if r + 12 > len(data):
            break
        platform, enc, lang, name_id, length, off = struct.unpack('>6H', data[r:r + 12])
        raw = data[o + str_off + off: o + str_off + off + length]
        if platform == 3:
            try:
                text = raw.decode('utf-16-be')
            except Exception:
                continue
            key = f'win-{lang:04x}'
        elif platform == 1:
            try:
                text = raw.decode('mac_roman')
            except Exception:
                try:
                    text = raw.decode('latin-1')
                except Exception:
                    continue
            key = f'mac-{lang:04x}'
        elif platform == 0:
            try:
                text = raw.decode('utf-16-be')
            except Exception:
                continue
            key = f'uni-{lang:04x}'
        else:
            continue
        out.setdefault(name_id, {})[key] = text
    return out


def pick(names: dict, name_id: int):
    """优先简体中文(0804)/繁体(0404)，其次英文(0409)，再任意"""
    m = names.get(name_id, {})
    for key in ('win-0804', 'win-0404', 'win-0411', 'win-0409', 'uni-0804', 'uni-0409', 'mac-0000'):
        if key in m and m[key].strip():
            return m[key].strip()
    for key, v in m.items():
        if v.strip():
            return v.strip()
    return None


def inspect(path: str):
    try:
        with open(path, 'rb') as f:
            data = f.read()
    except Exception as e:
        return None
    if len(data) < 12:
        return None
    tag = data[:4]
    results = []
    if tag == b'ttcf':
        n = struct.unpack('>I', data[8:12])[0]
        for i in range(min(n, 16)):
            off = struct.unpack('>I', data[12 + 4 * i:16 + 4 * i])[0]
            nm = read_name_table(data, off)
            if nm:
                results.append((pick(nm, 1), pick(nm, 2), pick(nm, 4), pick(nm, 6)))
    elif tag in (b'\x00\x01\x00\x00', b'OTTO', b'true', b'ttcf'):
        nm = read_name_table(data, 0)
        if nm:
            results.append((pick(nm, 1), pick(nm, 2), pick(nm, 4), pick(nm, 6)))
    else:
        return None
    return results


def main():
    out = []
    seen = set()
    for d in DIRS:
        if not os.path.isdir(d):
            continue
        for root, dirs, files in os.walk(d):
            dirs[:] = [x for x in dirs if not x.startswith('.')]
            depth = root[len(d):].count(os.sep)
            if depth >= 5:
                dirs[:] = []
            for fn in sorted(files):
                if not fn.lower().endswith(EXTS):
                    continue
                p = os.path.join(root, fn)
                if p in seen:
                    continue
                seen.add(p)
                res = inspect(p)
                if not res:
                    continue
                for fam, sub, full, ps in res:
                    out.append({
                        'file': fn,
                        'path': p,
                        'dir': root,
                        'family': fam,
                        'subfamily': sub,
                        'full': full,
                        'postscript': ps,
                        'size': os.path.getsize(p),
                    })
    print(json.dumps({'dirs': DIRS, 'count': len(out), 'fonts': out}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
