#!/usr/bin/env python3
import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

print(f"Total entries: {len(entries)}")
# Let's inspect B21 text content
b21 = [e for e in entries if e['slot'] == 'B21']
for e in b21:
    print("="*60)
    print(f"[{e['ordinal']}] 《{e['title']}》")
    print(f"问: {e['question']}")
    print(f"答(前300字): {e['text'][:300]}")
