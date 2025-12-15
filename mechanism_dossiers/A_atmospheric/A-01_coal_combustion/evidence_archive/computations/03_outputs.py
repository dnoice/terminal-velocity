#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metadata
    - Title: Output Generation Pipeline (Terminal Velocity - v1.0)
    - File Name: 03_outputs.py
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/evidence_archive/computations/03_outputs.py
    - Artifact Type: script
    - Version: 1.1.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Visualization and table generation pipeline for A-01 Coal Combustion Chain.
    Produces all figures and formatted tables for inclusion in the dossier,
    following the Terminal Velocity visual identity system.

Key Features:
    - Feature 1: Global coal CO2 time series with historical trend
    - Feature 2: Country ranking bar charts (current and cumulative)
    - Feature 3: Regional breakdown stacked area charts
    - Feature 4: Scenario projection comparison charts
    - Feature 5: Carbon budget countdown visualization
    - Feature 6: Terminal Velocity color palette integration
    - Feature 7: Publication-quality PNG export (150 DPI)
    - Feature 8: Output manifest generation for provenance tracking

Usage Instructions:
    Run after 02_analysis.py has generated derived results:

    As notebook:
        $ jupyter notebook 03_outputs.py

    As script:
        $ python 03_outputs.py

    Inputs:
        - ../datasets/derived/*.csv (from 02_analysis.py)
        - ../datasets/processed/*.parquet (from 01_intake.py)

    Outputs:
        - ../../exhibits/figures/*.png
        - ../../exhibits/tables/*.csv

Examples:
    $ python 03_outputs.py
    $ python 03_outputs.py --dpi 300

Other Important Information:
    - Dependencies: pandas, matplotlib, seaborn (see environment.yml)
    - Compatible platforms: Linux, Windows, macOS
    - Color palette: Terminal Velocity standard (all hex codes end in "4")
    - Output format: PNG figures (150 DPI), CSV tables
    - Figure dimensions: 10x6 inches standard, 12x8 for complex charts
---------
"""

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
# # Outputs: A-01 - Coal Combustion Chain
#
# **Purpose:** Generate all figures and tables for the dossier.
#
# **Inputs:**
# - `../datasets/derived/*.csv`
# - `../datasets/processed/*.parquet`
#
# **Outputs:**
# - `../../exhibits/figures/*.png`
# - `../../exhibits/tables/*.csv`

# %% [markdown]
# ## Setup

# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path
from datetime import datetime
import json

MECHANISM_CODE = "A-01"
PROCESSED_DIR = Path("../datasets/processed")
DERIVED_DIR = Path("../datasets/derived")
FIGURES_DIR = Path("../../exhibits/figures")
TABLES_DIR = Path("../../exhibits/tables")

# Ensure output directories exist
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)

# Terminal Velocity color palette
# All colors end in "4" - the harmonic signature
COLORS = {
    "primary": "#2e3c44",      # Deep Slate - Background, authority
    "secondary": "#ff9e54",    # Burnt Orange - Damage, urgency
    "tertiary": "#46ff84",     # Electric Green - Data, evidence
    "accent": "#f5f5f4",       # Soft White - Text, contrast
    "highlight": "#ffd144",    # Gold - Uncertainty, caution
    "success": "#44cca4",      # Teal - Solutions, leverage points
}

# Extended palette for multi-series charts
SERIES_COLORS = [
    "#ff9e54",  # Burnt Orange
    "#46ff84",  # Electric Green
    "#44cca4",  # Teal
    "#ffd144",  # Gold
    "#f5f5f4",  # Soft White
    "#8b9a94",  # Muted green-gray
]

# Figure settings
FIG_DPI = 150
FIG_SIZE_STANDARD = (10, 6)
FIG_SIZE_WIDE = (12, 6)
FIG_SIZE_TALL = (10, 8)

# Output log
output_log = []

def log_output(artifact_type: str, path: str, description: str = ""):
    """Log an output artifact."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "type": artifact_type,
        "path": str(path),
        "description": description
    }
    output_log.append(entry)
    print(f"[{entry['timestamp'][:19]}] {artifact_type}: {path}")

def apply_tv_style(ax, fig, title: str = ""):
    """Apply Terminal Velocity visual style to a matplotlib axes."""
    # Background colors
    ax.set_facecolor(COLORS["primary"])
    fig.patch.set_facecolor(COLORS["primary"])

    # Text colors
    ax.tick_params(colors=COLORS["accent"], which="both")
    ax.xaxis.label.set_color(COLORS["accent"])
    ax.yaxis.label.set_color(COLORS["accent"])

    if title:
        ax.set_title(title, fontsize=14, fontweight="bold", color=COLORS["accent"])

    # Spine colors
    for spine in ax.spines.values():
        spine.set_color(COLORS["accent"])
        spine.set_alpha(0.3)

    # Grid
    ax.grid(True, alpha=0.2, color=COLORS["accent"])

    return ax

print("Terminal Velocity Output Pipeline initialized")
print(f"Figures will be saved to: {FIGURES_DIR.absolute()}")
print(f"Tables will be saved to: {TABLES_DIR.absolute()}")

# %% [markdown]
# ## 1. Load Analysis Results

# %%
# Load processed emissions data (prefer parquet, fallback to CSV)
emissions_parquet = PROCESSED_DIR / "coal_emissions.parquet"
emissions_csv = PROCESSED_DIR / "coal_emissions.csv"

if emissions_parquet.exists():
    emissions_df = pd.read_parquet(emissions_parquet)
    print(f"Loaded emissions (parquet): {len(emissions_df):,} rows")
elif emissions_csv.exists():
    emissions_df = pd.read_csv(emissions_csv)
    print(f"Loaded emissions (CSV): {len(emissions_df):,} rows")
else:
    raise FileNotFoundError(f"Run 01_intake.py first")

# Load derived analysis results
rankings_path = DERIVED_DIR / "country_rankings.csv"
if rankings_path.exists():
    rankings_df = pd.read_csv(rankings_path)
    print(f"Loaded rankings: {len(rankings_df)} countries")
else:
    print("Warning: country_rankings.csv not found - run 02_analysis.py")
    rankings_df = None

trend_path = DERIVED_DIR / "trend_analysis.csv"
if trend_path.exists():
    trend_df = pd.read_csv(trend_path)
    print(f"Loaded trend analysis: {len(trend_df)} countries")
else:
    trend_df = None

projections_path = DERIVED_DIR / "scenario_projections.csv"
if projections_path.exists():
    projections_df = pd.read_csv(projections_path)
    print(f"Loaded projections: {len(projections_df)} data points")
else:
    projections_df = None

regional_path = DERIVED_DIR / "regional_emissions.csv"
if regional_path.exists():
    regional_df = pd.read_csv(regional_path)
    print(f"Loaded regional data: {len(regional_df)} rows")
else:
    regional_df = None

# Extract World data for global trend
world_df = emissions_df[emissions_df["country"] == "World"].copy()
print(f"World data: {len(world_df)} years")

# %% [markdown]
# ## 2. Figure: Global Coal CO2 Trend

# %%
# Create global trend figure
fig, ax = plt.subplots(figsize=FIG_SIZE_STANDARD)

# Filter to years with data
world_trend = world_df[world_df["coal_co2"].notna()].sort_values("year")

# Plot main trend line
ax.plot(world_trend["year"], world_trend["coal_co2"] / 1000,  # Convert to Gt
        color=COLORS["secondary"], lw=2.5, label="Coal CO2")

# Add markers for key years
key_years = [1990, 2000, 2010, 2020]
for year in key_years:
    year_data = world_trend[world_trend["year"] == year]
    if len(year_data) > 0:
        value = year_data["coal_co2"].values[0] / 1000
        ax.scatter(year, value, color=COLORS["tertiary"], s=50, zorder=5)
        ax.annotate(f"{value:.1f}", (year, value), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=9, color=COLORS["accent"])

# Apply Terminal Velocity style
apply_tv_style(ax, fig, "Global Coal CO2 Emissions (1900-Present)")
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("CO2 Emissions (Gt CO2/year)", fontsize=11)
ax.set_xlim(1900, world_trend["year"].max() + 2)
ax.set_ylim(0, None)

# Add legend
ax.legend(loc="upper left", facecolor=COLORS["primary"], edgecolor=COLORS["accent"],
          labelcolor=COLORS["accent"])

# Save figure
fig_path = FIGURES_DIR / "fig_01_global_coal_co2_trend.png"
fig.savefig(fig_path, dpi=FIG_DPI, bbox_inches="tight",
            facecolor=COLORS["primary"], edgecolor="none")
plt.close()

log_output("figure", fig_path, "Global coal CO2 emissions time series")

# %% [markdown]
# ## 3. Figure: Top Emitters Bar Chart

# %%
if rankings_df is not None:
    fig, ax = plt.subplots(figsize=FIG_SIZE_STANDARD)

    # Get top 10 emitters
    top10 = rankings_df.nlargest(10, "coal_co2")

    # Create horizontal bar chart
    bars = ax.barh(range(len(top10)), top10["coal_co2"] / 1000,
                   color=COLORS["secondary"], edgecolor=COLORS["accent"], linewidth=0.5)

    # Add value labels
    for i, (idx, row) in enumerate(top10.iterrows()):
        value = row["coal_co2"] / 1000
        ax.text(value + 0.1, i, f"{value:.1f} Gt", va="center",
                fontsize=9, color=COLORS["accent"])

    # Country labels
    ax.set_yticks(range(len(top10)))
    ax.set_yticklabels(top10["country"])
    ax.invert_yaxis()  # Highest at top

    # Apply style
    apply_tv_style(ax, fig, f"Top 10 Coal CO2 Emitters ({int(top10['year'].iloc[0])})")
    ax.set_xlabel("Coal CO2 Emissions (Gt CO2/year)", fontsize=11)

    # Save
    fig_path = FIGURES_DIR / "fig_02_top_emitters_current.png"
    fig.savefig(fig_path, dpi=FIG_DPI, bbox_inches="tight",
                facecolor=COLORS["primary"], edgecolor="none")
    plt.close()

    log_output("figure", fig_path, "Top 10 coal CO2 emitters bar chart")

# %% [markdown]
# ## 4. Figure: Scenario Projections

# %%
if projections_df is not None:
    fig, ax = plt.subplots(figsize=FIG_SIZE_WIDE)

    # Get unique scenarios
    scenarios = projections_df["scenario"].unique()

    # Color mapping for scenarios
    scenario_colors = {
        "current_trajectory": COLORS["secondary"],      # Orange - damage
        "delayed_action": COLORS["highlight"],          # Gold - caution
        "net_zero_2050": COLORS["tertiary"],           # Green - evidence
        "accelerated_phaseout": COLORS["success"],     # Teal - solutions
    }

    # Plot each scenario
    for scenario in scenarios:
        scenario_data = projections_df[projections_df["scenario"] == scenario]
        color = scenario_colors.get(scenario, COLORS["accent"])
        label = scenario.replace("_", " ").title()
        ax.plot(scenario_data["year"], scenario_data["coal_co2_mt"] / 1000,
                color=color, lw=2, label=label)

    # Add reference lines
    ax.axhline(y=0, color=COLORS["accent"], linestyle="--", alpha=0.3, lw=1)
    ax.axvline(x=2030, color=COLORS["accent"], linestyle=":", alpha=0.3, lw=1)
    ax.text(2030, ax.get_ylim()[1] * 0.95, "2030", color=COLORS["accent"],
            fontsize=9, ha="center", alpha=0.7)

    # Apply style
    apply_tv_style(ax, fig, "Coal CO2 Emission Scenarios (2024-2050)")
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Coal CO2 Emissions (Gt CO2/year)", fontsize=11)
    ax.set_xlim(projections_df["year"].min(), 2050)
    ax.set_ylim(0, None)

    # Legend
    ax.legend(loc="upper right", facecolor=COLORS["primary"], edgecolor=COLORS["accent"],
              labelcolor=COLORS["accent"], fontsize=9)

    # Save
    fig_path = FIGURES_DIR / "fig_03_scenario_projections.png"
    fig.savefig(fig_path, dpi=FIG_DPI, bbox_inches="tight",
                facecolor=COLORS["primary"], edgecolor="none")
    plt.close()

    log_output("figure", fig_path, "Scenario projections comparison")

# %% [markdown]
# ## 5. Figure: Regional Breakdown Over Time

# %%
if regional_df is not None:
    fig, ax = plt.subplots(figsize=FIG_SIZE_WIDE)

    # Filter to recent decades and main regions
    recent_regional = regional_df[regional_df["year"] >= 1990].copy()

    # Pivot for stacked area chart
    pivot_df = recent_regional.pivot(index="year", columns="region", values="coal_co2")

    # Reorder columns by latest year total
    latest_year = pivot_df.index.max()
    col_order = pivot_df.loc[latest_year].sort_values(ascending=False).index.tolist()
    pivot_df = pivot_df[col_order]

    # Create stacked area chart
    colors = [COLORS["secondary"], COLORS["tertiary"], COLORS["success"],
              COLORS["highlight"], COLORS["accent"], "#8b9a94"]

    ax.stackplot(pivot_df.index, [pivot_df[col] / 1000 for col in pivot_df.columns],
                 labels=pivot_df.columns, colors=colors[:len(pivot_df.columns)], alpha=0.8)

    # Apply style
    apply_tv_style(ax, fig, "Regional Coal CO2 Emissions (1990-Present)")
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Coal CO2 Emissions (Gt CO2/year)", fontsize=11)
    ax.set_xlim(1990, pivot_df.index.max())
    ax.set_ylim(0, None)

    # Legend (outside plot)
    ax.legend(loc="upper left", facecolor=COLORS["primary"], edgecolor=COLORS["accent"],
              labelcolor=COLORS["accent"], fontsize=8)

    # Save
    fig_path = FIGURES_DIR / "fig_04_regional_breakdown.png"
    fig.savefig(fig_path, dpi=FIG_DPI, bbox_inches="tight",
                facecolor=COLORS["primary"], edgecolor="none")
    plt.close()

    log_output("figure", fig_path, "Regional coal CO2 stacked area chart")

# %% [markdown]
# ## 6. Figure: Trend Status Summary

# %%
if trend_df is not None:
    fig, ax = plt.subplots(figsize=(8, 6))

    # Count countries by status
    status_counts = trend_df["status"].value_counts()

    # Color mapping for status
    status_colors = {
        "Growing": COLORS["secondary"],        # Orange - damage
        "Plateau": COLORS["highlight"],        # Gold - caution
        "Recent decline": COLORS["tertiary"],  # Green - evidence
        "Declining": COLORS["success"],        # Teal - solutions
    }

    colors = [status_colors.get(s, COLORS["accent"]) for s in status_counts.index]

    # Create pie chart
    wedges, texts, autotexts = ax.pie(status_counts.values, labels=status_counts.index,
                                       autopct="%1.0f%%", colors=colors,
                                       textprops={"color": COLORS["accent"]},
                                       wedgeprops={"edgecolor": COLORS["primary"], "linewidth": 2})

    for autotext in autotexts:
        autotext.set_color(COLORS["primary"])
        autotext.set_fontweight("bold")

    ax.set_title("Coal CO2 Emission Trends\n(Top 20 Emitters)", fontsize=14,
                 fontweight="bold", color=COLORS["accent"])
    fig.patch.set_facecolor(COLORS["primary"])

    # Save
    fig_path = FIGURES_DIR / "fig_05_trend_status.png"
    fig.savefig(fig_path, dpi=FIG_DPI, bbox_inches="tight",
                facecolor=COLORS["primary"], edgecolor="none")
    plt.close()

    log_output("figure", fig_path, "Trend status pie chart")

# %% [markdown]
# ## 7. Figure: China vs Rest of World

# %%
# Extract China and non-China data
countries_only = emissions_df[
    (emissions_df["iso_code"].notna()) &
    (emissions_df["country"] != "World")
].copy()

china_data = countries_only[countries_only["country"] == "China"].copy()
other_data = (countries_only[countries_only["country"] != "China"]
              .groupby("year")["coal_co2"].sum().reset_index())
other_data["country"] = "Rest of World"

# Filter to years with both
years_both = set(china_data["year"]) & set(other_data["year"])
china_data = china_data[china_data["year"].isin(years_both)]
other_data = other_data[other_data["year"].isin(years_both)]

if len(china_data) > 0 and len(other_data) > 0:
    fig, ax = plt.subplots(figsize=FIG_SIZE_STANDARD)

    # Filter to recent decades
    china_recent = china_data[china_data["year"] >= 1990].sort_values("year")
    other_recent = other_data[other_data["year"] >= 1990].sort_values("year")

    ax.fill_between(china_recent["year"], 0, china_recent["coal_co2"] / 1000,
                    color=COLORS["secondary"], alpha=0.7, label="China")
    ax.fill_between(other_recent["year"], china_recent["coal_co2"] / 1000,
                    (china_recent["coal_co2"].values + other_recent["coal_co2"].values) / 1000,
                    color=COLORS["success"], alpha=0.7, label="Rest of World")

    # Apply style
    apply_tv_style(ax, fig, "China vs Rest of World Coal CO2")
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Coal CO2 Emissions (Gt CO2/year)", fontsize=11)
    ax.set_xlim(1990, china_recent["year"].max())
    ax.set_ylim(0, None)

    ax.legend(loc="upper left", facecolor=COLORS["primary"], edgecolor=COLORS["accent"],
              labelcolor=COLORS["accent"])

    # Save
    fig_path = FIGURES_DIR / "fig_06_china_vs_world.png"
    fig.savefig(fig_path, dpi=FIG_DPI, bbox_inches="tight",
                facecolor=COLORS["primary"], edgecolor="none")
    plt.close()

    log_output("figure", fig_path, "China vs Rest of World stacked area")

# %% [markdown]
# ## 8. Export Summary Tables

# %%
# Table 1: Top emitters summary
if rankings_df is not None:
    table_path = TABLES_DIR / "table_01_top_emitters.csv"
    top_emitters_table = rankings_df[["rank", "country", "coal_co2", "co2",
                                       "coal_share_of_co2", "coal_co2_pct_global"]].copy()
    top_emitters_table.columns = ["Rank", "Country", "Coal CO2 (Mt)", "Total CO2 (Mt)",
                                  "Coal % of Total", "% of Global Coal CO2"]
    top_emitters_table.to_csv(table_path, index=False)
    log_output("table", table_path, "Top emitters summary table")

# Table 2: Trend analysis summary
if trend_df is not None:
    table_path = TABLES_DIR / "table_02_trend_analysis.csv"
    trend_table = trend_df[["country", "peak_year", "peak_coal_co2",
                            "latest_coal_co2", "change_from_peak_pct", "status"]].copy()
    trend_table.columns = ["Country", "Peak Year", "Peak Coal CO2 (Mt)",
                           "Latest Coal CO2 (Mt)", "Change from Peak (%)", "Status"]
    trend_table.to_csv(table_path, index=False)
    log_output("table", table_path, "Trend analysis summary table")

# Table 3: Scenario comparison (2030 and 2050)
if projections_df is not None:
    table_path = TABLES_DIR / "table_03_scenario_comparison.csv"

    scenario_summary = []
    for scenario in projections_df["scenario"].unique():
        scenario_data = projections_df[projections_df["scenario"] == scenario]
        desc = scenario_data["description"].iloc[0]

        val_2030 = scenario_data[scenario_data["year"] == 2030]["coal_co2_mt"].values
        val_2050 = scenario_data[scenario_data["year"] == 2050]["coal_co2_mt"].values

        scenario_summary.append({
            "Scenario": scenario.replace("_", " ").title(),
            "Description": desc,
            "2030 (Mt CO2)": val_2030[0] if len(val_2030) > 0 else None,
            "2050 (Mt CO2)": val_2050[0] if len(val_2050) > 0 else None,
        })

    pd.DataFrame(scenario_summary).to_csv(table_path, index=False)
    log_output("table", table_path, "Scenario comparison table")

# %% [markdown]
# ## 9. Output Manifest

# %%
# Generate output manifest
manifest = {
    "mechanism": MECHANISM_CODE,
    "pipeline": "03_outputs",
    "generated_at": datetime.now().isoformat(),
    "figures_dir": str(FIGURES_DIR.absolute()),
    "tables_dir": str(TABLES_DIR.absolute()),
    "artifacts": output_log,
    "color_palette": COLORS,
    "settings": {
        "dpi": FIG_DPI,
        "fig_size_standard": FIG_SIZE_STANDARD,
    }
}

manifest_path = FIGURES_DIR / "output_manifest.json"
with open(manifest_path, "w") as f:
    json.dump(manifest, f, indent=2)

log_output("manifest", manifest_path, "Output manifest with provenance")

# %% [markdown]
# ## 10. Summary

# %%
print("\n" + "="*60)
print(f"OUTPUTS COMPLETE: {MECHANISM_CODE} - Coal Combustion Chain")
print("="*60)

print(f"\nFigures generated ({FIGURES_DIR}):")
for f in sorted(FIGURES_DIR.glob("*.png")):
    size_kb = f.stat().st_size / 1024
    print(f"  - {f.name} ({size_kb:.1f} KB)")

print(f"\nTables generated ({TABLES_DIR}):")
for f in sorted(TABLES_DIR.glob("*.csv")):
    print(f"  - {f.name}")

print(f"\nTotal artifacts: {len(output_log)}")
print(f"Pipeline finished at: {datetime.now().isoformat()}")

# %% [markdown]
# ---
#
# **Filed under: Causes of Death, Preventable**
#
# *︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
