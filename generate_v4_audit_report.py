import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 组织结构化分析
# 1. 卷四定位说明
# 2. B18（作息节律与病理常识）全量 22 篇逐篇实质判定
# 3. B19（知行精进与克服拖延）全量 75 篇逐篇实质判定
# 4. B17（情志平复与容貌自和）全量 157 篇实质判定
# 5. 错位篇目统计与归位建议

print(f"Total entries: {len(entries)}")
