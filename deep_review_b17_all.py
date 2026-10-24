import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b17 = [e for e in entries if e['slot'] == 'B17']
print(f"Total B17: {len(b17)}")

# 遍历所有 B17 文章，打印序号、标题、问题和前200字
for i, e in enumerate(b17, 1):
    q = e['question'].replace('\n', ' ')
    t_preview = e['text'][:200].replace('\n', ' ')
    print(f"[{i}/157] ID:{e['id']} | 《{e['title']}》 ({e['text_len']}字)")
    print(f"  Q: {q}")
    print(f"  T: {t_preview}")
    print("-" * 60)
