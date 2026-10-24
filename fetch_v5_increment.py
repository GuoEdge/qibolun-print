#!/usr/bin/env python3
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

sys.path.insert(0, "/storage/Users/currentUser/Documents/岐伯论/research/scripts")
import fetch_sooon_increment as fetcher

fetcher.CORPUS_PATH = Path("/storage/Users/currentUser/Documents/岐伯论/sooon-q9adg-articles-v4.jsonl")

cookie = fetcher.resolve_session_cookie(fetcher.SESSION_FILE)
csrf = fetcher.resolve_csrf_token(fetcher.SESSION_FILE)
corpus_by_id, _ = fetcher.load_corpus()

manifest_path = fetcher.OUTPUT_DIR / fetcher.MANIFEST_NAME
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

targets = [t for t in manifest["items"] if str(t["id"]) not in corpus_by_id]
print(f"目标待抓取文章数: {len(targets)}")

stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
out_path = fetcher.OUTPUT_DIR / f"sooon-increment-{stamp}.jsonl"

written = 0
with out_path.open("w", encoding="utf-8") as writer:
    for i, t in enumerate(targets, 1):
        raw_name = f"lexical-{t['id']}"
        r = fetcher.invoke_sooon_query("SourceLexical", {"input": {"sourceId": str(t["id"])}}, cookie, csrf, raw_name)
        payload = r["json"].get("data", {}).get("payload")
        if not payload:
            print(f"FAIL: {t['title']}")
            continue
        lexical = payload.get("lexical")
        text = fetcher.convert_from_lexical(lexical)
        rec = {
            "id": str(t["id"]),
            "url": str(t["url"]),
            "title": str(t["title"]),
            "question": str(t["question"]),
            "brief": str(t["brief"]),
            "text": text,
            "lexical": lexical,
            "publishedAt": int(t["publishedAt"]),
            "updatedAt": int(payload.get("updatedAt", t["updatedAt"])),
            "source": {
                "platform": "zhihu" if "zhihu" in t["url"] else "afdian" if "afdian" in t["url"] or "ifdian" in t["url"] else "other",
                "publicQuestionId": str(t.get("publicQuestionId", "")),
                "planLevel": t.get("planLevel"),
                "status": str(t.get("status", "")),
                "inCorpus": False,
                "changeKind": "new",
                "fetchedAt": datetime.now(timezone.utc).isoformat()
            }
        }
        writer.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")
        writer.flush()
        written += 1
        print(f"[{i}/{len(targets)}] {t['title']} ({len(text)} 字) -> 写入成功")

print(f"抓取完成，共写入 {written} 篇到 {out_path}")
