import os
from datetime import datetime
from pathlib import Path

base = Path("/storage/Users/currentUser/Documents/岐伯论")
target_codes = ["B01", "B03", "B04", "B12", "B15", "B17", "B18", "B19", "B20A", 
                "B22", "B23", "B24", "B26", "B27", "B28", "B29", "B30", "B32", "B34", "B39"]

updated = []
for vol_dir in base.glob("卷*"):
    if not vol_dir.is_dir():
        continue
    for docx in vol_dir.rglob("*.docx"):
        mtime = datetime.fromtimestamp(docx.stat().st_mtime)
        if mtime.date() == datetime(2026, 10, 9).date() and mtime.hour >= 20:
            # 提取分册代码
            name = docx.name
            for code in target_codes:
                if code in str(docx.parent.name) or code in name:
                    updated.append((code, mtime.strftime("%H:%M"), docx.stat().st_size, str(docx)))
                    break

print(f"今天 20:00 后更新的分册：{len(updated)}/20")
for code, time, size, path in sorted(updated):
    print(f"  {code} @ {time} ({size//1024}KB)")
