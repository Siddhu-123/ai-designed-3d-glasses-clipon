import re
t = open("guide/NON_METAL_FRAMES.md", encoding="utf-8").read()
need = ["## Prerequisites", "## Choose a grip", "## Prompts", "## Checks before printing", "## Safety"]
miss = [h for h in need if h not in t]
assert not miss, miss
assert 1200 <= len(t.split()) <= 3200, len(t.split())
assert t.count("```") >= 8 and t.count("```") % 2 == 0, "need >=4 fenced prompt blocks"
assert not re.search(r"\b(Specsavers|Dylan|/Users/)", t), "keep it generic"
print("ok", len(t.split()), "words")
