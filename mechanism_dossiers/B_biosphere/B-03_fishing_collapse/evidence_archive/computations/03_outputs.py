# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Outputs: B-03 - Industrial Fishing Collapse
# 
# **Purpose:** Generate all figures, tables, and maps for the dossier.
# 
# **Inputs:**
# - `../datasets/derived/results.csv`
# 
# **Outputs:**
# - `../../exhibits/figures/*.png`
# - `../../exhibits/tables/*.csv`

# %% [markdown]
# ## Setup

# %%
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

MECHANISM_CODE = "B-03"
DERIVED_DIR = Path("../datasets/derived")
FIGURES_DIR = Path("../../exhibits/figures")
TABLES_DIR = Path("../../exhibits/tables")

FIGURES_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)

# Style configuration
plt.style.use("seaborn-v0_8-whitegrid")
COLORS = {
    "primary": "#2e3c44",
    "secondary": "#ff9e54",
    "tertiary": "#46ff84",
    "accent": "#f5f5f4",
    "highlight": "#ffd144",
    "success": "#44cca4",
}

# %% [markdown]
# ## 1. Load Analysis Results

# %%
# TODO: Load data
# results = pd.read_csv(DERIVED_DIR / "results.csv")

print("Load analysis results")

# %% [markdown]
# ## 2. Figure: Main Trend

# %%
# TODO: Create primary figure
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.plot(results["year"], results["value"], color=COLORS["alert"], lw=2)
# ax.set_title(f"Industrial Fishing Collapse: Primary Trend")
# ax.set_xlabel("Year")
# ax.set_ylabel("Value")
# fig.savefig(FIGURES_DIR / "fig_01_trend.png", dpi=150, bbox_inches="tight")
# plt.close()

print("Figure generation step")

# %% [markdown]
# ## 3. Figure: Geographic Distribution

# %%
# TODO: Create map visualization
print("Map generation step - implement if geographic data available")

# %% [markdown]
# ## 4. Summary Tables

# %%
# TODO: Export formatted tables
# summary = results.groupby("category").agg({"value": ["mean", "std", "count"]})
# summary.to_csv(TABLES_DIR / "table_01_summary.csv")

print("Table generation step")

# %% [markdown]
# ## 5. Output Manifest
# 
# List all generated artifacts:

# %%
print("Generated outputs:")
for f in FIGURES_DIR.glob("*"):
    print(f"  - {f}")
for t in TABLES_DIR.glob("*"):
    print(f"  - {t}")

# %% [markdown]
# ---
# 
# **Filed under: Causes of Death, Preventable**
