from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "official_snapshots.csv"
OUT = BASE / "figures"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

plt.rcParams["figure.dpi"] = 160
plt.rcParams["font.family"] = "DejaVu Sans"

def add_labels(ax):
    for c in ax.containers:
        ax.bar_label(c, fmt="%.1f", padding=3, fontsize=8)

# Figure 1
fig, ax = plt.subplots(figsize=(10, 5))
labels = ["2022 Q3\n(KSH)", "2023\n(KSH)", "2024 Q4\n(MNB)", "2025 Q1\n(KSH)", "2025 Q1\n(MNB)", "2025 Q1\n(Budapest)"]
vals = [23.0, 5.8, 15.1, 12.5, 15.0, 19.2]
ax.bar(labels, vals)
ax.set_title("Hungary housing price growth: selected official snapshots")
ax.set_ylabel("% year-on-year")
ax.axhline(0, linewidth=1)
ax.set_ylim(0, max(vals) + 6)
add_labels(ax)
ax.text(0.5, -0.18, "Mixes quarterly and annual snapshots to show the recent cycle: peak, slowdown, renewed acceleration.",
        transform=ax.transAxes, ha="center", fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "fig_price_snapshots.png", bbox_inches="tight")
plt.close(fig)

# Figure 2
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
d_labels = ["2023 turnover", "2024 Q1 sales", "2024 Q3 sales", "2025 Q1 transactions", "2024 Q4 loans"]
d_vals = [-25.0, 36.0, 14.0, 7.0, 91.0]
axes[0].bar(d_labels, d_vals)
axes[0].set_title("Demand-side signals")
axes[0].set_ylabel("% year-on-year")
axes[0].axhline(0, linewidth=1)
axes[0].tick_params(axis="x", rotation=20)
axes[0].set_ylim(min(d_vals) - 15, max(d_vals) + 20)
add_labels(axes[0])

axes[1].bar(["2024 completions", "2024 permits"], [-29.0, -27.0])
axes[1].set_title("Supply-side constraints")
axes[1].set_ylabel("% year-on-year")
axes[1].axhline(0, linewidth=1)
axes[1].set_ylim(-40, 10)
add_labels(axes[1])
axes[1].text(0.5, -0.23, "Occupancy permits: 13,300; building permits: 20,500; renewal rate: 0.29%.",
             transform=axes[1].transAxes, ha="center", fontsize=9)
fig.suptitle("Demand recovered, while supply remained constrained", y=1.02, fontsize=14)
fig.tight_layout()
fig.savefig(OUT / "fig_demand_supply.png", bbox_inches="tight")
plt.close(fig)

# Figure 3
fig, ax = plt.subplots(figsize=(10, 5))
labels = ["Gross earnings growth\n2024", "Real earnings growth\n2024", "Housing prices\n2024 Q4", "Overvaluation\n2024 Q4"]
vals = [13.2, 9.0, 15.1, 14.3]
ax.bar(labels, vals)
ax.set_title("Affordability pressure: wages rose, but housing prices rose faster")
ax.set_ylabel("%")
ax.axhline(0, linewidth=1)
ax.set_ylim(0, max(vals) + 6)
add_labels(ax)
ax.text(0.5, -0.18, "KSH reported average gross earnings of HUF 646,600 in 2024; MNB estimated 14.3% overvaluation in 2024 Q4.",
        transform=ax.transAxes, ha="center", fontsize=9)
fig.tight_layout()
fig.savefig(OUT / "fig_affordability.png", bbox_inches="tight")
plt.close(fig)
