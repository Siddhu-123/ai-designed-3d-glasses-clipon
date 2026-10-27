"""Vector charts for the report (report/charts/*.pdf). Numbers come from the version reports of the design workspace."""
import json, os, datetime as dt
from collections import Counter
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
plt.rcParams.update({"font.family": "Avenir Next" if any("Avenir Next" in f.name for f in fm.fontManager.ttflist) else "DejaVu Sans",
                     "font.size": 8.5, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": "#8a93a6",
                     "axes.labelcolor": "#1b2a4a", "xtick.color": "#46506a", "ytick.color": "#46506a", "pdf.fonttype": 42})
NAVY, TEAL, AMBER, RED, GREY, VIOLET = "#1b2a4a", "#0f9d9a", "#f2a541", "#d1495b", "#b8bfcc", "#6c5ce7"
OUT = "report/charts"; os.makedirs(OUT, exist_ok=True)
D = lambda s: dt.date.fromisoformat(s)

# 1. Version timeline: (label, start, end, status, prompts)
V = [("v00 glasses model","2026-10-01","2026-10-22","base",33),("v01 full","2026-10-02","2026-10-02","sup",12),("v02 cut","2026-10-02","2026-10-02","sup",2),
 ("v03 flush","2026-10-02","2026-10-03","sup",5),("v04 flush 4x1","2026-10-02","2026-10-03","sup",6),("v05 wide 4x1","2026-10-02","2026-10-03","sup",5),
 ("v06 strong 4x1","2026-10-02","2026-10-03","sup",1),("v07 strong2 4x1","2026-10-02","2026-10-03","sup",1),("v08 aligned 4x1","2026-10-02","2026-10-03","sup",4),
 ("v09 polished 4x1","2026-10-03","2026-10-03","sup",5),("v10 backload 4x1","2026-10-03","2026-10-03","sup",4),("vX ChatGPT/Codex","2026-10-04","2026-10-05","rej",2),
 ("v11 refined 4x1","2026-10-05","2026-10-13","sup",12),("v12 symmetric 4x1","2026-10-13","2026-10-16","sup",10),("v13 symmetric 6x1","2026-10-14","2026-10-15","sup",3),
 ("v14 faired 6x1","2026-10-19","2026-10-20","sup",10),("v15 scaled","2026-10-21","2026-10-26","sup",16),("v16 photo","2026-10-21","2026-10-21","rej",4),
 ("v17 film","2026-10-21","2026-10-21","rej",2),("v18 hscale","2026-10-21","2026-10-22","kept",4),("v15.1 smooth (FINAL)","2026-10-26","2026-10-27","final",4)]
C = {"base": NAVY, "sup": GREY, "rej": RED, "kept": AMBER, "final": TEAL}
fig, ax = plt.subplots(figsize=(7.2, 4.6))
t0 = D("2026-10-01")
for i, (lab, a, b, st, n) in enumerate(V):
    x0, x1 = (D(a) - t0).days, (D(b) - t0).days + 1
    ax.barh(i, x1 - x0, left=x0, height=0.62, color=C[st], alpha=0.9 if st != "sup" else 0.75, edgecolor="white", lw=0.6)
    ax.scatter(x1 + 0.35, i, s=9 + n * 7, color=C[st], edgecolor=NAVY, lw=0.4, zorder=3)
    ax.text(x1 + 0.9 + n * 0.035, i, f"{n}", va="center", fontsize=6.5, color=NAVY)
ax.set_yticks(range(len(V))); ax.set_yticklabels([v[0] for v in V], fontsize=7); ax.invert_yaxis()
ticks = [0, 4, 9, 12, 17, 20, 25]; ax.set_xticks(ticks); ax.set_xticklabels([(t0 + dt.timedelta(d)).strftime("%d Oct") for d in ticks])
ax.set_xlim(-0.3, 29); ax.grid(axis="x", color="#e3e7ee", lw=0.6); ax.set_axisbelow(True)
for x, txt in [(12, "magnets bought\n& stuck on rims"), (20, "true-scale\ncampaign"), (25, "smooth-curve\naudit")]:
    ax.axvline(x, color=VIOLET, lw=0.8, ls=(0, (3, 2))); ax.text(x + 0.2, 0.2, txt, color=VIOLET, fontsize=6.5, va="top")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=C[k], label=l) for k, l in [("base","base model"),("sup","superseded"),("rej","rejected / abandoned"),("kept","kept, not for print"),("final","final")]],
          loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=5, frameon=False, fontsize=7)
ax.set_xlabel("Calendar (October 2026)   ·   dot size and number = prompts linked to that version")
fig.tight_layout(); fig.savefig(f"{OUT}/version_timeline.pdf"); plt.close(fig)

# 2. Scale evidence: implied width scale vs the symmetric model
fig, ax = plt.subplots(figsize=(7.2, 2.3))
rows = [("Grid-paper stereo photos (21 Oct)", 1.011, 1.008, 1.013, TEAL, "width, 6 mm grid"),
        ("Grid photos top + oblique (22 Oct)", 1.011, None, None, TEAL, "height:width ratio matches v15"),
        ("Retailer listed sizes A/DBL/B", 1.011, None, None, TEAL, "B 41.6 mm agrees with v15 height"),
        ("Per-row height check (21 Oct)", 1.026, 1.021, 1.031, AMBER, "the only outlier: built as v18, not printed")]
for i, (lab, v, lo, hi, c, note) in enumerate(rows):
    if lo: ax.plot([lo, hi], [i, i], color=c, lw=3, alpha=0.45, solid_capstyle="round")
    ax.scatter(v, i, s=46, color=c, edgecolor=NAVY, lw=0.6, zorder=3, marker="o" if lo else "D")
    ax.text(1.0335, i, note, va="center", fontsize=7, color="#46506a")
ax.axvspan(1.008, 1.013, color=TEAL, alpha=0.08); ax.axvline(1.011, color=TEAL, lw=1)
ax.text(1.0112, -0.75, "chosen: ×1.011 (v15)", color=TEAL, fontsize=7.5)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows]); ax.invert_yaxis()
ax.set_xlim(1.0, 1.058); ax.set_ylim(len(rows) - 0.4, -1.1); ax.set_xlabel("implied scale factor of the real glasses vs the mirror-symmetric model")
fig.tight_layout(); fig.savefig(f"{OUT}/scale_evidence.pdf"); plt.close(fig)

# 3. Final margins: measured value / required value
M = [("Plastic wall around magnet pocket", 0.997, 0.95, "mm"), ("Front cover over pocket", 1.183, 0.95, "mm"),
     ("Plastic between pockets", 1.581, 1.4, "mm"), ("Assumed film strain limit vs loading peak", 1.0, 0.898, "%"),
     ("Hold vs clip weight (est.)", 2.0, 0.05, "N"),
     ("PLA strength vs FEA peak (comparative)", 50, 1.4, "MPa")]
fig, ax = plt.subplots(figsize=(7.2, 2.6))
for i, (lab, val, req, u) in enumerate(M):
    r = val / req; w = min(r, 3.0)
    ax.barh(i, 3.0, color="#eef1f6", height=0.6); ax.barh(i, w, color=TEAL if r < 3 else NAVY, height=0.6)
    ax.text(w + 0.04 if w < 2.6 else 2.95, i, f"{val:g} vs {req:g} {u}  ({r:.2f}×)" if r < 10 else f"{val:g} vs {req:g} {u}  ({r:.0f}×, axis capped)",
            va="center", ha="left" if w < 2.6 else "right", fontsize=7, color="white" if w >= 2.6 else NAVY)
ax.axvline(1, color=RED, lw=1); ax.text(1.02, -0.75, "required", color=RED, fontsize=7)
ax.set_yticks(range(len(M))); ax.set_yticklabels([m[0] for m in M]); ax.invert_yaxis(); ax.set_xlim(0, 3.05); ax.set_ylim(len(M) - 0.4, -1.1)
ax.set_xlabel("margin = measured / required (final v15.1)")
fig.tight_layout(); fig.savefig(f"{OUT}/margins.pdf"); plt.close(fig)

# 4. Prompt anatomy (needs scripts/prompt_classes.json)
if os.path.exists("scripts/prompt_classes.json"):
    P = {p["n"]: p for p in json.load(open("scripts/prompts.json"))}
    K = json.load(open("scripts/prompt_classes.json"))
    CAT = ["VISION","EVIDENCE","CONSTRAINT","CHALLENGE","CORRECTION","VERIFY","ORCHESTRATE","HOUSEKEEP","CONTINUE"]
    CC = dict(zip(CAT, [NAVY, "#2a9d8f", "#3d5a80", RED, "#e76f51", TEAL, VIOLET, "#8d99ae", GREY]))
    fig = plt.figure(figsize=(7.2, 3.4)); g = fig.add_gridspec(1, 2, width_ratios=[2.6, 1])
    ax = fig.add_subplot(g[0])
    for r in K:
        p = P[r["n"]]; t = dt.datetime.fromisoformat(p["time"]); x = (t.date() - t0).days + t.hour / 24
        y = CAT.index(r["primary"]); ax.scatter(x, y, s=10 + min(len(p["text"]), 1400) / 9, color=CC[r["primary"]], alpha=0.75, edgecolor="white", lw=0.4)
        for s in r.get("secondary", []): ax.plot([x, x], [y, CAT.index(s)], color=CC[r["primary"]], lw=0.4, alpha=0.35)
    ax.set_yticks(range(len(CAT))); ax.set_yticklabels([c.title() for c in CAT]); ax.invert_yaxis()
    ax.set_xticks(ticks); ax.set_xticklabels([(t0 + dt.timedelta(d)).strftime("%d Oct") for d in ticks]); ax.grid(axis="x", color="#e3e7ee", lw=0.6)
    ax.set_xlabel("prompt time  ·  dot size = prompt length  ·  lines = secondary intent")
    ax2 = fig.add_subplot(g[1]); cnt = Counter(r["primary"] for r in K)
    ax2.barh(range(len(CAT)), [cnt[c] for c in CAT], color=[CC[c] for c in CAT]); ax2.invert_yaxis(); ax2.set_yticks([])
    for i, c in enumerate(CAT): ax2.text(cnt[c] + 0.3, i, str(cnt[c]), va="center", fontsize=7)
    ax2.set_xlabel(f"count (n = {len(K)})")
    fig.tight_layout(); fig.savefig(f"{OUT}/prompt_anatomy.pdf"); plt.close(fig)
    json.dump({c: cnt[c] for c in CAT}, open(f"{OUT}/prompt_counts.json", "w"))

# 5. What changed in each version (from the version reports' "why it was made" sections)
AX = ["Glasses model", "True scale", "Outline / border", "Film shape", "Film loading", "Magnet count / spots", "Pocket geometry", "Bridge / comfort", "Smooth curves"]
VC = [("v01", {"Outline / border": "first\nclip", "Film shape": "uncut"}), ("v02", {"Film shape": "cut to\nlens"}),
      ("v03", {"Outline / border": "flush\nto steel"}), ("v04", {"Magnet count / spots": "4 ×\n4x1"}),
      ("v05", {"Outline / border": "wide", "Film shape": "almost\nuncut"}), ("v06", {"Outline / border": "wider\nborder"}),
      ("v07", {"Magnet count / spots": "my\nsketch"}), ("v08", {"Glasses model": "aligned", "Outline / border": "back on\nsteel"}),
      ("v09", {"Pocket geometry": "square\nto steel", "Outline / border": "smooth\nfront"}), ("v10", {"Film loading": "from\nback"}),
      ("v11", {"Film shape": "real\nsheets"}), ("v12", {"Glasses model": "mirror\nsym."}),
      ("v13", {"Magnet count / spots": "6\nsingle"}), ("v14", {"Bridge / comfort": "arch +\nface fit"}),
      ("v15", {"True scale": "×1.011\nscale"}), ("v16", {"Outline / border": "photo\nre-trace"}), ("v17", {"Film loading": "photo\nre-trace"}),
      ("v18", {"True scale": "height\n×1.026"}), ("v15.1", {"Smooth curves": "slot,\nlips, cut", "Film shape": "smooth\ncut"})]
ST = {"v16": RED, "v17": RED, "v18": AMBER, "v15.1": TEAL}
fig, ax = plt.subplots(figsize=(7.2, 4.0))
for j, (v, ch) in enumerate(VC):
    for i, a in enumerate(AX):
        ax.add_patch(plt.Rectangle((j - 0.46, i - 0.42), 0.92, 0.84, color="#f1f3f7", lw=0))
        if a in ch:
            c = ST.get(v, NAVY)
            ax.add_patch(plt.Rectangle((j - 0.46, i - 0.42), 0.92, 0.84, color=c, lw=0))
            ax.text(j, i, ch[a], ha="center", va="center", fontsize=5.2, color="white", linespacing=0.95)
ax.set_xlim(-0.6, len(VC) - 0.4); ax.set_ylim(len(AX) - 0.5, -0.6)
ax.set_xticks(range(len(VC))); ax.set_xticklabels([v for v, _ in VC], fontsize=7)
for t, (v, _) in zip(ax.get_xticklabels(), VC): t.set_color(ST.get(v, NAVY)); t.set_fontweight("bold" if v == "v15.1" else "normal")
ax.set_yticks(range(len(AX))); ax.set_yticklabels(AX, fontsize=7.5); ax.tick_params(length=0)
for sp in ax.spines.values(): sp.set_visible(False)
ax.xaxis.tick_top()
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=NAVY,label="change kept"),Patch(color=RED,label="rejected / abandoned"),Patch(color=AMBER,label="kept, not for print"),Patch(color=TEAL,label="final")],loc="upper center",bbox_to_anchor=(0.5,-0.01),ncol=4,frameon=False,fontsize=7)
fig.tight_layout(); fig.savefig(f"{OUT}/version_changes.pdf"); plt.close(fig)
print("charts ok")
