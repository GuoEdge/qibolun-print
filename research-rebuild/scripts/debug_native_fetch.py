import re, requests

text = open(r"research/online-increment/.session-curl", encoding="utf-8").read()
cookie = re.search(r"-H 'cookie: ([^']+)'", text).group(1)
csrf = re.search(r"x-graphql-csrf: ([^']+)'", text).group(1)
payload = {
    "operationName": "LeoCategoryList",
    "variables": {},
    "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "sha256:b7d5d72cc4e5fc2162a93126fb9846c7e3f8eab105e203661ac5fcb0e966862c"},},
}
r = requests.post("https://sooon.ai/api/graphql", json=payload, headers={"cookie": cookie, "x-graphql-csrf": csrf, "accept": "application/json", "origin": "https://sooon.ai"}, timeout=30)
print(r.status_code, r.encoding, r.apparent_encoding, r.headers.get("content-type"))
print(r.text[:400])
print(r.json()["data"]["leoCategoryList"][0])
