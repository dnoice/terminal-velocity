#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metadata
    - Title: Analysis Pipeline (Terminal Velocity - v1.0)
    - File Name: 02_analysis.py
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/evidence_archive/computations/02_analysis.py
    - Artifact Type: script
    - Version: 1.1.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Analytical pipeline for A-01 Coal Combustion Chain mechanism.
    Computes derived metrics, runs scenario projections, and performs sensitivity
    analysis to identify key parameters affecting conclusions.

Key Features:
    - Feature 1: Per-capita and intensity metric calculations
    - Feature 2: Year-over-year growth rate computation
    - Feature 3: Regional aggregation and comparison (Top 10 emitters)
    - Feature 4: Baseline, accelerated phaseout, and delayed action scenarios
    - Feature 5: Carbon budget analysis and remaining timeline
    - Feature 6: Historical trend decomposition (peak years, growth phases)
    - Feature 7: Attribution analysis (country/region shares)
    - Feature 8: Reproducible analysis with provenance logging

Usage Instructions:
    Run after 01_intake.py has generated processed data:

    As notebook:
        $ jupyter notebook 02_analysis.py

    As script:
        $ python 02_analysis.py

    Inputs:
        - ../datasets/processed/coal_emissions.parquet
        - ../datasets/processed/coal_consumption.parquet

    Outputs:
        - ../datasets/derived/analysis_results.csv
        - ../datasets/derived/country_rankings.csv
        - ../datasets/derived/scenario_projections.csv
        - ../datasets/derived/trend_analysis.csv

Examples:
    $ python 02_analysis.py

Other Important Information:
    - Dependencies: pandas, numpy (see environment.yml)
    - Compatible platforms: Linux, Windows, macOS
    - Input format: Parquet from 01_intake.py
    - Output format: CSV for portability
    - Carbon budget: Based on IPCC AR6 1.5C remaining budget
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
# # Analysis: A-01 - Coal Combustion Chain
#
# **Purpose:** Compute derived metrics, run scenarios, attribute emissions.
#
# **Inputs:**
# - `../datasets/processed/coal_emissions.parquet`
# - `../datasets/processed/coal_consumption.parquet`
#
# **Outputs:**
# - `../datasets/derived/analysis_results.csv`
# - `../datasets/derived/country_rankings.csv`
# - `../datasets/derived/scenario_projections.csv`

# %% [markdown]
# ## Setup

# %%
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import json

MECHANISM_CODE = "A-01"
PROCESSED_DIR = Path("../datasets/processed")
DERIVED_DIR = Path("../datasets/derived")

# Ensure output directory exists
DERIVED_DIR.mkdir(parents=True, exist_ok=True)

# Analysis log
analysis_log = []

def log_analysis(step: str, result: str = ""):
    """Log an analysis step with timestamp."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "step": step,
        "result": result
    }
    analysis_log.append(entry)
    print(f"[{entry['timestamp'][:19]}] {step}: {result}")

log_analysis("Analysis started", f"Mechanism {MECHANISM_CODE}")

# %% [markdown]
# ## 1. Load Processed Data

# %%
# Load emissions data (prefer parquet, fallback to CSV)
emissions_parquet = PROCESSED_DIR / "coal_emissions.parquet"
emissions_csv = PROCESSED_DIR / "coal_emissions.csv"

if emissions_parquet.exists():
    emissions_df = pd.read_parquet(emissions_parquet)
    log_analysis("Loaded coal emissions (parquet)", f"{len(emissions_df):,} rows")
elif emissions_csv.exists():
    emissions_df = pd.read_csv(emissions_csv)
    log_analysis("Loaded coal emissions (CSV)", f"{len(emissions_df):,} rows")
else:
    log_analysis("ERROR", f"Emissions file not found")
    raise FileNotFoundError(f"Run 01_intake.py first")

# Load consumption data (prefer parquet, fallback to CSV)
consumption_parquet = PROCESSED_DIR / "coal_consumption.parquet"
consumption_csv = PROCESSED_DIR / "coal_consumption.csv"

if consumption_parquet.exists():
    consumption_df = pd.read_parquet(consumption_parquet)
    log_analysis("Loaded coal consumption (parquet)", f"{len(consumption_df):,} rows")
elif consumption_csv.exists():
    consumption_df = pd.read_csv(consumption_csv)
    log_analysis("Loaded coal consumption (CSV)", f"{len(consumption_df):,} rows")
else:
    log_analysis("WARNING", f"Consumption file not found")
    consumption_df = None

# Display data overview
print(f"\nEmissions data: {emissions_df['year'].min()}-{emissions_df['year'].max()}")
print(f"Countries: {emissions_df['country'].nunique()}")

# %% [markdown]
# ## 2. Filter to Country-Level Data
#
# Remove aggregate regions for proper analysis.

# %%
# Aggregates to exclude from country-level analysis
AGGREGATE_REGIONS = [
    "World", "Africa", "Asia", "Europe", "North America", "South America",
    "Oceania", "Antarctica", "European Union (27)", "European Union (28)",
    "High-income countries", "Low-income countries", "Lower-middle-income countries",
    "Upper-middle-income countries", "Asia (excl. China and India)",
    "Europe (excl. EU-27)", "Europe (excl. EU-28)", "North America (excl. USA)",
    "OECD", "Non-OECD"
]

# Filter to countries only (has iso_code and not in aggregates)
countries_df = emissions_df[
    (emissions_df["iso_code"].notna()) &
    (~emissions_df["country"].isin(AGGREGATE_REGIONS))
].copy()

log_analysis("Filtered to countries", f"{countries_df['country'].nunique()} countries")

# Keep world aggregate for reference
world_df = emissions_df[emissions_df["country"] == "World"].copy()
log_analysis("World data extracted", f"{len(world_df)} years")

# %% [markdown]
# ## 3. Derived Metrics
#
# Calculate per-capita emissions, growth rates, and shares.

# %%
# Calculate year-over-year changes for each country
countries_df = countries_df.sort_values(["country", "year"])

# Year-over-year percentage change in coal CO2
countries_df["coal_co2_yoy_pct"] = (
    countries_df.groupby("country")["coal_co2"]
    .pct_change() * 100
)

# Year-over-year absolute change
countries_df["coal_co2_yoy_abs"] = (
    countries_df.groupby("country")["coal_co2"]
    .diff()
)

# 5-year rolling average (smoothed trend)
countries_df["coal_co2_5yr_avg"] = (
    countries_df.groupby("country")["coal_co2"]
    .transform(lambda x: x.rolling(5, min_periods=3).mean())
)

# Coal share of total CO2
countries_df["coal_share_of_co2"] = (
    countries_df["coal_co2"] / countries_df["co2"] * 100
).round(2)

log_analysis("Computed derived metrics",
             "YoY change, 5yr avg, coal share of CO2")

# Display sample of derived metrics
print("\nDerived metrics sample (China, recent years):")
china_recent = countries_df[
    (countries_df["country"] == "China") &
    (countries_df["year"] >= 2018)
][["country", "year", "coal_co2", "coal_co2_yoy_pct", "coal_share_of_co2"]]
print(china_recent.to_string(index=False))

# %% [markdown]
# ## 4. Country Rankings
#
# Rank countries by coal CO2 emissions (latest year and cumulative).

# %%
# Get latest year with complete data
latest_year = countries_df["year"].max()

# Latest year rankings
latest_rankings = (countries_df[countries_df["year"] == latest_year]
    .nlargest(20, "coal_co2")
    [["country", "iso_code", "year", "coal_co2", "co2", "coal_share_of_co2", "population"]]
    .copy())

latest_rankings["rank"] = range(1, len(latest_rankings) + 1)
latest_rankings["coal_co2_pct_global"] = (
    latest_rankings["coal_co2"] / latest_rankings["coal_co2"].sum() * 100
).round(2)

log_analysis(f"Latest year rankings ({latest_year})", f"Top 20 countries")

print(f"\nTop 10 Coal CO2 Emitters ({latest_year}):")
print(latest_rankings[["rank", "country", "coal_co2", "coal_co2_pct_global"]].head(10).to_string(index=False))

# Cumulative emissions rankings
cumulative_rankings = (countries_df
    .groupby(["country", "iso_code"])
    .agg({
        "coal_co2": "sum",
        "co2": "sum",
        "year": ["min", "max"]
    })
    .reset_index())

cumulative_rankings.columns = ["country", "iso_code", "cumulative_coal_co2",
                               "cumulative_co2", "first_year", "last_year"]
cumulative_rankings = cumulative_rankings.nlargest(20, "cumulative_coal_co2")
cumulative_rankings["rank"] = range(1, len(cumulative_rankings) + 1)

log_analysis("Cumulative rankings computed", "Historical attribution")

print(f"\nTop 10 Cumulative Coal CO2 Emitters (All Time):")
print(cumulative_rankings[["rank", "country", "cumulative_coal_co2"]].head(10).to_string(index=False))

# %% [markdown]
# ## 5. Trend Analysis
#
# Identify peak years, growth phases, and decline patterns.

# %%
def analyze_country_trend(df: pd.DataFrame, country: str) -> dict:
    """
    Analyze emissions trend for a single country.

    Args:
        df: Country-filtered emissions dataframe
        country: Country name

    Returns:
        Dict with trend analysis results
    """
    country_data = df[df["country"] == country].sort_values("year")

    if len(country_data) < 10:
        return None

    coal_co2 = country_data["coal_co2"].dropna()

    if len(coal_co2) < 5:
        return None

    # Find peak year
    peak_idx = coal_co2.idxmax()
    peak_year = country_data.loc[peak_idx, "year"]
    peak_value = coal_co2.max()

    # Current value
    latest_year = country_data["year"].max()
    latest_value = country_data[country_data["year"] == latest_year]["coal_co2"].values[0]

    # Change from peak
    change_from_peak = ((latest_value - peak_value) / peak_value * 100) if peak_value > 0 else 0

    # Recent trend (last 5 years average growth)
    recent_data = country_data[country_data["year"] >= latest_year - 5]["coal_co2_yoy_pct"].dropna()
    recent_trend = recent_data.mean() if len(recent_data) > 0 else 0

    # Classify trend
    if change_from_peak < -20 and peak_year < latest_year - 5:
        status = "Declining"
    elif recent_trend > 2:
        status = "Growing"
    elif recent_trend < -2:
        status = "Recent decline"
    else:
        status = "Plateau"

    return {
        "country": country,
        "peak_year": int(peak_year),
        "peak_coal_co2": round(peak_value, 2),
        "latest_year": int(latest_year),
        "latest_coal_co2": round(latest_value, 2) if pd.notna(latest_value) else None,
        "change_from_peak_pct": round(change_from_peak, 1),
        "recent_trend_pct": round(recent_trend, 1),
        "status": status
    }

# Analyze top 20 emitters
top_countries = latest_rankings["country"].tolist()
trend_analysis = []

for country in top_countries:
    result = analyze_country_trend(countries_df, country)
    if result:
        trend_analysis.append(result)

trend_df = pd.DataFrame(trend_analysis)
log_analysis("Trend analysis complete", f"{len(trend_df)} countries analyzed")

print("\nTrend Analysis (Top Emitters):")
print(trend_df[["country", "peak_year", "status", "change_from_peak_pct"]].to_string(index=False))

# %% [markdown]
# ## 6. Scenario Projections
#
# Model future coal CO2 under different policy scenarios.

# %%
# IPCC AR6 carbon budget context (approximate)
# 1.5C with 50% probability: ~500 Gt CO2 remaining from 2020
# Current annual emissions: ~40 Gt CO2 total, ~15 Gt from coal

# Get global coal CO2 trend
global_coal = world_df[["year", "coal_co2"]].dropna().copy()
latest_global = global_coal[global_coal["year"] == global_coal["year"].max()]["coal_co2"].values[0]

log_analysis("Global coal CO2 (latest)", f"{latest_global:.0f} Mt CO2")

# Define scenarios
SCENARIOS = {
    "current_trajectory": {
        "description": "Current policies trajectory (+0.5%/yr)",
        "annual_change_pct": 0.5,
        "color": "#ff9e54"  # Burnt Orange - damage
    },
    "accelerated_phaseout": {
        "description": "1.5C-aligned phaseout (-7%/yr)",
        "annual_change_pct": -7.0,
        "color": "#44cca4"  # Teal - solutions
    },
    "delayed_action": {
        "description": "Delayed action (+2%/yr until 2030, then -5%/yr)",
        "annual_change_pct": 2.0,  # Initial rate
        "switch_year": 2030,
        "post_switch_rate": -5.0,
        "color": "#ffd144"  # Gold - caution
    },
    "net_zero_2050": {
        "description": "Net zero by 2050 (-4.3%/yr)",
        "annual_change_pct": -4.3,
        "color": "#46ff84"  # Electric Green
    }
}

# Project scenarios
projection_years = list(range(int(global_coal["year"].max()), 2051))
projections = []

for scenario_name, config in SCENARIOS.items():
    current_value = latest_global

    for i, year in enumerate(projection_years):
        if i == 0:
            projected = current_value
        else:
            # Handle delayed action scenario
            if scenario_name == "delayed_action" and year > config.get("switch_year", 9999):
                rate = config["post_switch_rate"]
            else:
                rate = config["annual_change_pct"]

            projected = projected * (1 + rate / 100)
            projected = max(0, projected)  # Can't go negative

        projections.append({
            "scenario": scenario_name,
            "description": config["description"],
            "year": year,
            "coal_co2_mt": round(projected, 1),
            "color": config["color"]
        })

projections_df = pd.DataFrame(projections)
log_analysis("Scenario projections computed", f"{len(SCENARIOS)} scenarios to 2050")

# Summary: Years to zero emissions by scenario
print("\nScenario Projections Summary:")
for scenario in SCENARIOS:
    scenario_data = projections_df[projections_df["scenario"] == scenario]
    year_2030 = scenario_data[scenario_data["year"] == 2030]["coal_co2_mt"].values[0]
    year_2050 = scenario_data[scenario_data["year"] == 2050]["coal_co2_mt"].values[0]
    print(f"  {scenario}: 2030={year_2030:.0f} Mt, 2050={year_2050:.0f} Mt")

# %% [markdown]
# ## 7. Carbon Budget Analysis
#
# Calculate remaining coal budget for 1.5C and 2C targets.

# %%
# IPCC AR6 remaining carbon budgets (from 2020, 50% probability)
# 1.5C: ~500 Gt CO2
# 2C: ~1,350 Gt CO2
# Coal is ~40% of energy CO2, so coal budget is approximately:
# 1.5C coal budget: ~200 Gt CO2
# 2C coal budget: ~540 Gt CO2

CARBON_BUDGETS = {
    "1.5C_50pct": {
        "total_budget_gt": 500,
        "coal_share": 0.40,
        "coal_budget_gt": 200,
        "description": "1.5°C with 50% probability"
    },
    "2C_50pct": {
        "total_budget_gt": 1350,
        "coal_share": 0.40,
        "coal_budget_gt": 540,
        "description": "2°C with 50% probability"
    }
}

# Calculate cumulative emissions from latest year for each scenario
budget_analysis = []

for budget_name, budget_config in CARBON_BUDGETS.items():
    coal_budget_mt = budget_config["coal_budget_gt"] * 1000  # Convert to Mt

    for scenario_name in SCENARIOS:
        scenario_data = projections_df[projections_df["scenario"] == scenario_name].copy()

        # Calculate cumulative from projection start
        scenario_data = scenario_data.sort_values("year")
        scenario_data["cumulative_mt"] = scenario_data["coal_co2_mt"].cumsum()

        # Find year budget is exhausted
        exhausted_year = scenario_data[scenario_data["cumulative_mt"] >= coal_budget_mt]
        if len(exhausted_year) > 0:
            exhaust_year = exhausted_year["year"].min()
        else:
            exhaust_year = ">2050"

        # Total emissions by 2050
        total_by_2050 = scenario_data[scenario_data["year"] <= 2050]["coal_co2_mt"].sum()

        budget_analysis.append({
            "budget": budget_name,
            "budget_description": budget_config["description"],
            "coal_budget_gt": budget_config["coal_budget_gt"],
            "scenario": scenario_name,
            "exhaust_year": exhaust_year,
            "cumulative_by_2050_gt": round(total_by_2050 / 1000, 1),
            "budget_overshoot_gt": round((total_by_2050 / 1000) - budget_config["coal_budget_gt"], 1)
        })

budget_df = pd.DataFrame(budget_analysis)
log_analysis("Carbon budget analysis complete", f"{len(budget_df)} combinations analyzed")

print("\nCarbon Budget Analysis:")
print(budget_df[["budget", "scenario", "exhaust_year", "budget_overshoot_gt"]].to_string(index=False))

# %% [markdown]
# ## 8. Regional Aggregation
#
# Group countries into regions for comparison.

# %%
# Define regions (simplified)
REGIONS = {
    "China": ["China"],
    "India": ["India"],
    "United States": ["United States"],
    "European Union": ["Germany", "Poland", "Italy", "France", "Spain", "Netherlands",
                       "Belgium", "Czech Republic", "Greece", "Austria", "Romania",
                       "Bulgaria", "Hungary", "Portugal", "Sweden", "Finland"],
    "Rest of Asia": ["Japan", "South Korea", "Indonesia", "Vietnam", "Taiwan",
                     "Thailand", "Malaysia", "Philippines", "Pakistan", "Bangladesh"],
    "Other": []  # Catchall
}

def assign_region(country: str) -> str:
    """Assign a country to a region."""
    for region, countries in REGIONS.items():
        if country in countries:
            return region
    return "Other"

# Add region column
countries_df["region"] = countries_df["country"].apply(assign_region)

# Aggregate by region and year
regional_df = (countries_df
    .groupby(["region", "year"])
    .agg({
        "coal_co2": "sum",
        "co2": "sum",
        "population": "sum"
    })
    .reset_index())

regional_df["coal_share_of_co2"] = (regional_df["coal_co2"] / regional_df["co2"] * 100).round(2)

log_analysis("Regional aggregation complete", f"{regional_df['region'].nunique()} regions")

# Latest year regional breakdown
regional_latest = regional_df[regional_df["year"] == latest_year].sort_values("coal_co2", ascending=False)
print(f"\nRegional Coal CO2 Breakdown ({latest_year}):")
print(regional_latest[["region", "coal_co2", "coal_share_of_co2"]].to_string(index=False))

# %% [markdown]
# ## 9. Export Results
#
# Save all analysis outputs to derived directory.

# %%
# Prepare comprehensive results
analysis_results = {
    "latest_year": int(latest_year),
    "global_coal_co2_mt": float(latest_global),
    "top_emitter": latest_rankings.iloc[0]["country"],
    "top_emitter_share_pct": float(latest_rankings.iloc[0]["coal_co2_pct_global"]),
    "countries_analyzed": int(countries_df["country"].nunique()),
    "years_covered": f"{int(countries_df['year'].min())}-{int(countries_df['year'].max())}"
}

# Export country rankings
rankings_path = DERIVED_DIR / "country_rankings.csv"
combined_rankings = latest_rankings.merge(
    cumulative_rankings[["country", "cumulative_coal_co2", "first_year"]],
    on="country",
    how="left"
)
combined_rankings.to_csv(rankings_path, index=False)
log_analysis("Exported country rankings", str(rankings_path))

# Export trend analysis
trend_path = DERIVED_DIR / "trend_analysis.csv"
trend_df.to_csv(trend_path, index=False)
log_analysis("Exported trend analysis", str(trend_path))

# Export scenario projections
projections_path = DERIVED_DIR / "scenario_projections.csv"
projections_df.to_csv(projections_path, index=False)
log_analysis("Exported scenario projections", str(projections_path))

# Export carbon budget analysis
budget_path = DERIVED_DIR / "carbon_budget_analysis.csv"
budget_df.to_csv(budget_path, index=False)
log_analysis("Exported carbon budget analysis", str(budget_path))

# Export regional data
regional_path = DERIVED_DIR / "regional_emissions.csv"
regional_df.to_csv(regional_path, index=False)
log_analysis("Exported regional emissions", str(regional_path))

# Export analysis summary
summary_path = DERIVED_DIR / "analysis_results.json"
with open(summary_path, "w") as f:
    json.dump({
        "mechanism": MECHANISM_CODE,
        "pipeline": "02_analysis",
        "run_timestamp": datetime.now().isoformat(),
        "results": analysis_results,
        "scenarios": {k: v["description"] for k, v in SCENARIOS.items()},
        "carbon_budgets": CARBON_BUDGETS,
        "analysis_log": analysis_log
    }, f, indent=2, default=str)

log_analysis("Exported analysis summary", str(summary_path))

# %% [markdown]
# ## 10. Summary
#
# Final summary of analysis pipeline results.

# %%
print("\n" + "="*60)
print(f"ANALYSIS COMPLETE: {MECHANISM_CODE} - Coal Combustion Chain")
print("="*60)

print(f"\nKey Findings ({latest_year}):")
print(f"  Global coal CO2: {latest_global:,.0f} Mt CO2")
print(f"  Top emitter: {latest_rankings.iloc[0]['country']} ({latest_rankings.iloc[0]['coal_co2_pct_global']:.1f}% of global)")
print(f"  Top 5 share: {latest_rankings.head(5)['coal_co2_pct_global'].sum():.1f}% of global")

print(f"\nScenario Implications:")
for scenario in ["current_trajectory", "accelerated_phaseout"]:
    budget_row = budget_df[(budget_df["budget"] == "1.5C_50pct") & (budget_df["scenario"] == scenario)]
    if len(budget_row) > 0:
        print(f"  {scenario}: 1.5C budget exhausted by {budget_row.iloc[0]['exhaust_year']}")

print(f"\nDerived artifacts saved to: {DERIVED_DIR}")
for f in DERIVED_DIR.glob("*.csv"):
    print(f"  - {f.name}")
for f in DERIVED_DIR.glob("*.json"):
    print(f"  - {f.name}")

print(f"\nAnalysis steps logged: {len(analysis_log)}")
print(f"Pipeline finished at: {datetime.now().isoformat()}")

# %% [markdown]
# ## Provenance Log
#
# | Action | Timestamp | Notes |
# |--------|-----------|-------|
# | Created | 2025-12-14 | Initial template |
# | Updated | 2025-12-14 | Implemented full analysis pipeline |
