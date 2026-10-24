#!/usr/bin/env python3
import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# Let's inspect B21 first (25 articles)
print("=== READING B21 FULL LIST ===")
b21 = [e for e in entries if e['slot'] == 'B21']
for e in b21:
    print(f"[{e['ordinal']}] 《{e['title']}》")
    print(f"  Q: {e['question'][:100]}")
    print(f"  Text excerpt: {e['text'][:150].replace('\n', ' ')}")
    print("-" * 50)
