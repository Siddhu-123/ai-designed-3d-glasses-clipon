"""Gate for scripts/prompt_classes.json: every curated prompt classified once, valid labels, short reasons."""
import json, sys
CATS = {"VISION", "EVIDENCE", "CHALLENGE", "CORRECTION", "CONSTRAINT", "VERIFY", "ORCHESTRATE", "HOUSEKEEP", "CONTINUE"}
prompts = {p["n"] for p in json.load(open("scripts/prompts.json"))}
rows = json.load(open("scripts/prompt_classes.json"))
ns = [r["n"] for r in rows]
assert len(ns) == len(set(ns)), "duplicate n"
assert set(ns) == prompts, f"missing {sorted(prompts - set(ns))} extra {sorted(set(ns) - prompts)}"
for r in rows:
    assert r["primary"] in CATS, r
    assert all(c in CATS for c in r.get("secondary", [])), r
    assert r["primary"] not in r.get("secondary", []), r
    assert 0 < len(r["why"]) <= 140, r
    assert r["skill"] and len(r["skill"]) <= 60, r
print("ok", len(rows))
