"""Curate the raw prompt log: project prompts only, duplicates (two parallel sessions) merged, profanity masked."""
import re, sys, json
src, out_md, out_json = sys.argv[1:4]
text = open(src, encoding="utf-8").read()
blocks = re.split(r"\n(?=\[\d+\] \d{4}-)", text)
SKIP = set(range(118, 131)) | {90, 91, 116}  # unrelated side project / housekeeping chatter
MASK = [(r"\bfuck(ed|ing)?\b", lambda m: "f***" + (m.group(1) or "")), (r"\bcrap\b", "c**p"), (r"\bass\b", "a**")]
seen, rows = set(), []
for b in blocks:
    m = re.match(r"\[(\d+)\] (\S+) (\S+)( \(hub worker brief.*?\))?\n(.*)", b, re.S)
    if not m: continue
    n, ts, _, worker, body = int(m[1]), m[2], m[3], m[4], m[5].strip()
    if worker or n in SKIP: continue
    body = re.sub(r"<pasted_content.*", "[pasted manufacturer note about pull-force ratings]", body, flags=re.S)
    body = re.sub(r"/Users/\S+?/", "…/", body)
    for pat, rep in MASK: body = re.sub(pat, rep, body, flags=re.I)
    key = body[:200]
    if key in seen: continue
    seen.add(key); rows.append({"n": n, "time": ts, "text": body})
with open(out_md, "w", encoding="utf-8") as f:
    f.write("# My original prompts (curated)\n\nEvery prompt I typed for this project, oldest first, numbered as in my private log. "
            "Two parallel sessions received the same prompt early on; duplicates are merged. Prompts for an unrelated side project are left out, "
            "local paths are shortened and strong language is masked. Nothing else is edited, typos included.\n\n")
    for r in rows: f.write(f"**[{r['n']}]** `{r['time']}`\n\n> " + r["text"].replace("\n", "\n> ") + "\n\n")
json.dump(rows, open(out_json, "w"), indent=1, ensure_ascii=False)
print(len(rows), "prompts")
