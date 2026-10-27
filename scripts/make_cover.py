"""Cover and blueprint drawings from the real v15.1 design data (refined_design.npz + magnets_symmetric.json)."""
import sys, json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Avenir Next"
D = sys.argv[1]  # blender_ai/frame/clipon_v2/v15_1_smooth/data
d = np.load(f"{D}/refined_design.npz", allow_pickle=True)
mag = json.load(open(f"{D}/magnets_symmetric.json"))
TEAL, AMBER = "#0F9D9A", "#F2A541"
def close(a): return np.vstack([a, a[:1]])
def draw(fname, line, fill, mark, txt, dims=True):
    fig, ax = plt.subplots(figsize=(7.5, 3.0))
    co = close(d["CO"]); ax.fill(co[:, 0], co[:, 1], color=fill, alpha=0.22, lw=0)
    ax.plot(co[:, 0], co[:, 1], color=line, lw=1.6)
    for s in "RL":
        fw = close(d["FW_" + s]); ax.fill(fw[:, 0], fw[:, 1], color="white" if txt == "#1b2a4a" else "#1b2a4a", lw=0)
        ax.plot(fw[:, 0], fw[:, 1], color=line, lw=1.0)
        g = close(d["G_" + s]); ax.plot(g[:, 0], g[:, 1], color=line, lw=0.6, ls=(0, (4, 2)), alpha=0.8)
    for k, (x, z) in mag.items():
        ax.add_patch(plt.Circle((x, z), 2.0, color=mark, zorder=4)); ax.add_patch(plt.Circle((x, z), 3.6, fill=False, color=mark, alpha=0.4, lw=0.8))
    if dims:
        y = d["CO"][:, 1].min() - 6
        ax.annotate("", (-72.24, y), (71.91, y), arrowprops=dict(arrowstyle="<->", color=txt, lw=0.7))
        ax.text(0, y - 1.5, "144.15 mm", ha="center", va="top", color=txt, fontsize=8)
        ax.annotate("6 × Ø4×1 mm NdFeB, epoxied in blind rear pockets", (67.13, 25.67), (22, 44), color=txt, fontsize=7,
                    arrowprops=dict(arrowstyle="-", color=txt, lw=0.5))
        ax.annotate("0.2 mm film in a 0.4 mm back-loaded slot (dashed)", (-64.5, 5), (-80, 44), color=txt, fontsize=7,
                    arrowprops=dict(arrowstyle="-", color=txt, lw=0.5))
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-80, 80); ax.set_ylim(-30, 48)
    fig.savefig(fname, transparent=True, bbox_inches="tight", pad_inches=0.02); plt.close(fig)
draw("report/charts/cover_outline.pdf", TEAL, TEAL, AMBER, "white")
draw("report/charts/blueprint.pdf", "#1b2a4a", TEAL, AMBER, "#1b2a4a")
print("ok")
