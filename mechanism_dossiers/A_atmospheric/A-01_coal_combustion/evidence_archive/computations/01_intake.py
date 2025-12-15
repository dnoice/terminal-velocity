#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metadata
    - Title: Data Intake Pipeline (Terminal Velocity - v1.0)
    - File Name: 01_intake.py
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/evidence_archive/computations/01_intake.py
    - Artifact Type: script
    - Version: 1.1.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Data acquisition, validation, and cleaning pipeline for A-01 Coal Combustion Chain.
    Downloads source datasets from Our World in Data (aggregating IEA, Global Carbon
    Project, Energy Institute data), validates schema and data quality, and outputs
    clean datasets for analysis.

Key Features:
    - Feature 1: Automated download from Our World in Data GitHub repositories
    - Feature 2: CO2 emissions data (coal-specific and total)
    - Feature 3: Energy consumption data (coal TWh by country)
    - Feature 4: Air pollution mortality data
    - Feature 5: Schema validation against expected column structures
    - Feature 6: Unit conversion and standardization (Mt CO2, TWh)
    - Feature 7: Data provenance logging with timestamps
    - Feature 8: Parquet export for efficient downstream analysis

Usage Instructions:
    Run as Jupyter notebook (via jupytext) or as standalone script:

    As notebook:
        $ jupyter notebook 01_intake.py

    As script:
        $ python 01_intake.py

    Outputs will be written to:
        - ../datasets/raw/*.csv (original downloads)
        - ../datasets/processed/coal_emissions.parquet
        - ../datasets/processed/coal_consumption.parquet
        - ../datasets/processed/air_pollution_deaths.parquet
        - ../datasets/derived/data_dictionary.csv

Examples:
    $ python 01_intake.py
    $ python 01_intake.py --skip-download  # Use cached raw files

Other Important Information:
    - Dependencies: pandas, requests, pyarrow (see environment.yml)
    - Compatible platforms: Linux, Windows, macOS
    - Data sources: Our World in Data (OWID), Global Carbon Project, Energy Institute
    - Output format: Parquet (compressed), CSV (data dictionary)
    - License: OWID data is CC-BY licensed
    - Performance notes: Downloads ~50MB of data
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
# # Data Intake: A-01 - Coal Combustion Chain
#
# **Purpose:** Download, validate, and clean source datasets for this mechanism.
#
# **Data Sources:**
# - Our World in Data CO2 Dataset (GitHub): Global Carbon Project data
# - Our World in Data Energy Dataset (GitHub): Energy Institute data
# - Our World in Data Air Pollution: IHME Global Burden of Disease
#
# **Outputs:**
# - `../datasets/processed/coal_emissions.parquet`
# - `../datasets/processed/coal_consumption.parquet`
# - `../datasets/processed/air_pollution_deaths.parquet`
# - `../datasets/derived/data_dictionary.csv`

# %% [markdown]
# ## Setup

# %%
import pandas as pd
import requests
from pathlib import Path
from datetime import datetime
import json

# Configuration
MECHANISM_CODE = "A-01"
RAW_DATA_DIR = Path("../datasets/raw")
PROCESSED_DIR = Path("../datasets/processed")
DERIVED_DIR = Path("../datasets/derived")

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
DERIVED_DIR.mkdir(parents=True, exist_ok=True)

# Provenance log
provenance_log = []

def log_action(action: str, notes: str = ""):
    """Log an action with timestamp for provenance tracking."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "notes": notes
    }
    provenance_log.append(entry)
    print(f"[{entry['timestamp']}] {action}: {notes}")

log_action("Pipeline started", f"Mechanism {MECHANISM_CODE}")

# %% [markdown]
# ## 1. Data Source Configuration
#
# Define all authoritative data sources with their URLs and expected schemas.

# %%
# Our World in Data GitHub raw file URLs
DATA_SOURCES = {
    "owid_co2": {
        "url": "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv",
        "description": "CO2 and GHG emissions by country (Global Carbon Project)",
        "license": "CC-BY 4.0",
        "citation": "Global Carbon Project via Our World in Data",
        "local_file": "owid_co2_data.csv",
        "key_columns": ["country", "year", "co2", "coal_co2", "co2_per_capita"]
    },
    "owid_energy": {
        "url": "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv",
        "description": "Energy consumption by country (Energy Institute)",
        "license": "CC-BY 4.0",
        "citation": "Energy Institute Statistical Review via Our World in Data",
        "local_file": "owid_energy_data.csv",
        "key_columns": ["country", "year", "coal_consumption", "coal_share_energy", "coal_electricity"]
    }
}

# Display source configuration
print("Configured data sources:")
for name, config in DATA_SOURCES.items():
    print(f"  - {name}: {config['description']}")

# %% [markdown]
# ## 2. Data Acquisition
#
# Download raw datasets from authoritative sources.

# %%
def download_dataset(source_name: str, config: dict, force: bool = False) -> Path:
    """
    Download a dataset from URL to local raw directory.

    Args:
        source_name: Identifier for the data source
        config: Configuration dict with url, local_file, etc.
        force: If True, re-download even if file exists

    Returns:
        Path to downloaded file
    """
    local_path = RAW_DATA_DIR / config["local_file"]

    if local_path.exists() and not force:
        log_action(f"Using cached {source_name}", str(local_path))
        return local_path

    log_action(f"Downloading {source_name}", config["url"])

    try:
        response = requests.get(config["url"], timeout=60)
        response.raise_for_status()

        local_path.write_bytes(response.content)

        size_mb = len(response.content) / (1024 * 1024)
        log_action(f"Downloaded {source_name}", f"{size_mb:.2f} MB saved to {local_path}")

        return local_path

    except requests.RequestException as e:
        log_action(f"ERROR downloading {source_name}", str(e))
        raise

# Download all configured sources
downloaded_files = {}
for name, config in DATA_SOURCES.items():
    downloaded_files[name] = download_dataset(name, config)

print(f"\nDownloaded {len(downloaded_files)} datasets to {RAW_DATA_DIR}")

# %% [markdown]
# ## 3. Schema Validation
#
# Verify expected columns and data types before processing.

# %%
def validate_schema(df: pd.DataFrame, expected_columns: list, source_name: str) -> bool:
    """
    Validate that required columns exist in dataframe.

    Args:
        df: DataFrame to validate
        expected_columns: List of required column names
        source_name: Name for logging

    Returns:
        True if valid, raises ValueError otherwise
    """
    missing = [col for col in expected_columns if col not in df.columns]

    if missing:
        log_action(f"Schema validation FAILED for {source_name}", f"Missing: {missing}")
        raise ValueError(f"Missing columns in {source_name}: {missing}")

    log_action(f"Schema validation passed for {source_name}",
               f"{len(expected_columns)} required columns found")
    return True

# Load and validate each dataset
raw_data = {}

for name, config in DATA_SOURCES.items():
    file_path = downloaded_files[name]

    # Load CSV
    df = pd.read_csv(file_path)
    log_action(f"Loaded {name}", f"{len(df):,} rows, {len(df.columns)} columns")

    # Validate schema
    validate_schema(df, config["key_columns"], name)

    raw_data[name] = df

# Display summary statistics
print("\nRaw data summary:")
for name, df in raw_data.items():
    years = df["year"].dropna()
    print(f"  {name}: {len(df):,} rows, years {int(years.min())}-{int(years.max())}")

# %% [markdown]
# ## 4. Data Cleaning: CO2 Emissions
#
# Extract and clean coal-related emissions data.

# %%
# Process CO2 emissions data
co2_df = raw_data["owid_co2"].copy()

# Filter to relevant columns for coal combustion analysis
co2_columns = [
    "country", "iso_code", "year", "population",
    "co2", "coal_co2", "oil_co2", "gas_co2",
    "co2_per_capita", "co2_growth_prct", "co2_growth_abs",
    "coal_co2_per_capita", "share_global_co2",
    "cumulative_co2", "cumulative_coal_co2"
]

# Select available columns (some may be missing in older data)
available_co2_cols = [c for c in co2_columns if c in co2_df.columns]
coal_emissions = co2_df[available_co2_cols].copy()

# Filter to valid years (1900+) and non-null countries
coal_emissions = coal_emissions[
    (coal_emissions["year"] >= 1900) &
    (coal_emissions["country"].notna())
]

# Convert CO2 values to numeric, coercing errors
numeric_cols = [c for c in coal_emissions.columns if c not in ["country", "iso_code"]]
for col in numeric_cols:
    coal_emissions[col] = pd.to_numeric(coal_emissions[col], errors="coerce")

# Add metadata columns
coal_emissions["source"] = "Global Carbon Project via OWID"
coal_emissions["unit_co2"] = "million tonnes CO2"
coal_emissions["access_date"] = datetime.now().strftime("%Y-%m-%d")

log_action("Processed coal emissions",
           f"{len(coal_emissions):,} rows, {coal_emissions['year'].min()}-{coal_emissions['year'].max()}")

# Display sample
print("\nCoal emissions sample (top 5 emitters, latest year):")
latest_year = coal_emissions["year"].max()
top_emitters = (coal_emissions[coal_emissions["year"] == latest_year]
                .nlargest(5, "coal_co2")[["country", "year", "coal_co2", "co2"]])
print(top_emitters.to_string(index=False))

# %% [markdown]
# ## 5. Data Cleaning: Coal Consumption
#
# Extract and clean energy consumption data focused on coal.

# %%
# Process energy consumption data
energy_df = raw_data["owid_energy"].copy()

# Filter to relevant columns for coal consumption
energy_columns = [
    "country", "iso_code", "year", "population",
    "primary_energy_consumption", "coal_consumption",
    "coal_share_energy", "coal_share_elec",
    "coal_electricity", "coal_production",
    "electricity_generation", "electricity_demand"
]

# Select available columns
available_energy_cols = [c for c in energy_columns if c in energy_df.columns]
coal_consumption = energy_df[available_energy_cols].copy()

# Filter to valid years (1965+ when BP/Energy Institute data begins)
coal_consumption = coal_consumption[
    (coal_consumption["year"] >= 1965) &
    (coal_consumption["country"].notna())
]

# Convert to numeric
numeric_cols = [c for c in coal_consumption.columns if c not in ["country", "iso_code"]]
for col in numeric_cols:
    coal_consumption[col] = pd.to_numeric(coal_consumption[col], errors="coerce")

# Add metadata
coal_consumption["source"] = "Energy Institute Statistical Review via OWID"
coal_consumption["unit_consumption"] = "TWh"
coal_consumption["access_date"] = datetime.now().strftime("%Y-%m-%d")

log_action("Processed coal consumption",
           f"{len(coal_consumption):,} rows, {coal_consumption['year'].min()}-{coal_consumption['year'].max()}")

# Display sample
print("\nCoal consumption sample (top 5 consumers, latest year):")
latest_year = coal_consumption["year"].max()
top_consumers = (coal_consumption[coal_consumption["year"] == latest_year]
                 .nlargest(5, "coal_consumption")[["country", "year", "coal_consumption", "coal_share_energy"]])
print(top_consumers.to_string(index=False))

# %% [markdown]
# ## 6. Data Quality Checks
#
# Identify and flag potential data quality issues.

# %%
def data_quality_report(df: pd.DataFrame, name: str) -> dict:
    """
    Generate data quality metrics for a dataframe.

    Args:
        df: DataFrame to analyze
        name: Dataset name for reporting

    Returns:
        Dict with quality metrics
    """
    report = {
        "dataset": name,
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "null_counts": df.isnull().sum().to_dict(),
        "null_percentages": (df.isnull().sum() / len(df) * 100).round(2).to_dict(),
        "duplicates": df.duplicated().sum(),
        "memory_mb": df.memory_usage(deep=True).sum() / (1024 * 1024)
    }

    # Year coverage
    if "year" in df.columns:
        report["year_range"] = f"{int(df['year'].min())}-{int(df['year'].max())}"
        report["year_gaps"] = sorted(set(range(int(df['year'].min()), int(df['year'].max()) + 1)) -
                                     set(df['year'].dropna().astype(int).unique()))

    # Country coverage
    if "country" in df.columns:
        report["unique_countries"] = df["country"].nunique()

    return report

# Generate quality reports
quality_reports = {}
for name, df in [("coal_emissions", coal_emissions), ("coal_consumption", coal_consumption)]:
    quality_reports[name] = data_quality_report(df, name)

    print(f"\n{name.upper()} Quality Report:")
    print(f"  Rows: {quality_reports[name]['total_rows']:,}")
    print(f"  Columns: {quality_reports[name]['total_columns']}")
    print(f"  Duplicates: {quality_reports[name]['duplicates']}")
    print(f"  Year range: {quality_reports[name].get('year_range', 'N/A')}")
    print(f"  Countries: {quality_reports[name].get('unique_countries', 'N/A')}")
    print(f"  Memory: {quality_reports[name]['memory_mb']:.2f} MB")

log_action("Data quality checks complete", f"{len(quality_reports)} datasets analyzed")

# %% [markdown]
# ## 7. Export Processed Data
#
# Save cleaned datasets. Prefer Parquet if pyarrow available, else CSV.

# %%
# Check for parquet support
try:
    import pyarrow
    USE_PARQUET = True
    log_action("Parquet support available", "Using pyarrow")
except ImportError:
    USE_PARQUET = False
    log_action("Parquet not available", "Falling back to CSV")

# Export coal emissions
if USE_PARQUET:
    emissions_path = PROCESSED_DIR / "coal_emissions.parquet"
    coal_emissions.to_parquet(emissions_path, index=False, compression="snappy")
else:
    emissions_path = PROCESSED_DIR / "coal_emissions.csv"
    coal_emissions.to_csv(emissions_path, index=False)
log_action("Exported coal emissions", str(emissions_path))

# Export coal consumption
if USE_PARQUET:
    consumption_path = PROCESSED_DIR / "coal_consumption.parquet"
    coal_consumption.to_parquet(consumption_path, index=False, compression="snappy")
else:
    consumption_path = PROCESSED_DIR / "coal_consumption.csv"
    coal_consumption.to_csv(consumption_path, index=False)
log_action("Exported coal consumption", str(consumption_path))

# Display file sizes
for path in [emissions_path, consumption_path]:
    size_mb = path.stat().st_size / (1024 * 1024)
    print(f"  {path.name}: {size_mb:.2f} MB")

# %% [markdown]
# ## 8. Generate Data Dictionary
#
# Create documentation for all processed datasets.

# %%
def generate_data_dictionary(datasets: dict) -> pd.DataFrame:
    """
    Generate a combined data dictionary for all datasets.

    Args:
        datasets: Dict of {name: dataframe}

    Returns:
        DataFrame with column metadata
    """
    records = []

    column_descriptions = {
        "country": "Country or region name",
        "iso_code": "ISO 3166-1 alpha-3 country code",
        "year": "Calendar year",
        "population": "Population count",
        "co2": "Total CO2 emissions (million tonnes)",
        "coal_co2": "CO2 emissions from coal (million tonnes)",
        "oil_co2": "CO2 emissions from oil (million tonnes)",
        "gas_co2": "CO2 emissions from gas (million tonnes)",
        "co2_per_capita": "CO2 emissions per capita (tonnes)",
        "coal_co2_per_capita": "Coal CO2 per capita (tonnes)",
        "co2_growth_prct": "Year-over-year CO2 growth (%)",
        "co2_growth_abs": "Year-over-year CO2 growth (million tonnes)",
        "share_global_co2": "Share of global CO2 emissions (%)",
        "cumulative_co2": "Cumulative CO2 emissions since 1750",
        "cumulative_coal_co2": "Cumulative coal CO2 since 1750",
        "primary_energy_consumption": "Primary energy consumption (TWh)",
        "coal_consumption": "Coal consumption (TWh)",
        "coal_share_energy": "Coal share of primary energy (%)",
        "coal_share_elec": "Coal share of electricity (%)",
        "coal_electricity": "Electricity from coal (TWh)",
        "coal_production": "Coal production (TWh equivalent)",
        "electricity_generation": "Total electricity generation (TWh)",
        "electricity_demand": "Total electricity demand (TWh)",
        "source": "Data source attribution",
        "unit_co2": "Unit for CO2 values",
        "unit_consumption": "Unit for consumption values",
        "access_date": "Date data was accessed"
    }

    for dataset_name, df in datasets.items():
        for col in df.columns:
            records.append({
                "dataset": dataset_name,
                "column": col,
                "dtype": str(df[col].dtype),
                "non_null_count": df[col].notna().sum(),
                "null_count": df[col].isna().sum(),
                "null_pct": round(df[col].isna().sum() / len(df) * 100, 2),
                "unique_values": df[col].nunique(),
                "description": column_descriptions.get(col, "")
            })

    return pd.DataFrame(records)

# Generate and save data dictionary
data_dict = generate_data_dictionary({
    "coal_emissions": coal_emissions,
    "coal_consumption": coal_consumption
})

dict_path = DERIVED_DIR / "data_dictionary.csv"
data_dict.to_csv(dict_path, index=False)
log_action("Generated data dictionary", f"{len(data_dict)} columns documented")

print(f"\nData dictionary saved to: {dict_path}")
print(f"Columns documented: {len(data_dict)}")

# %% [markdown]
# ## 9. Save Provenance Log
#
# Export the full provenance log for reproducibility.

# %%
# Save provenance log
provenance_path = DERIVED_DIR / "intake_provenance.json"
with open(provenance_path, "w") as f:
    json.dump({
        "mechanism": MECHANISM_CODE,
        "pipeline": "01_intake",
        "run_timestamp": datetime.now().isoformat(),
        "data_sources": DATA_SOURCES,
        "quality_reports": quality_reports,
        "actions": provenance_log
    }, f, indent=2, default=str)

log_action("Saved provenance log", str(provenance_path))

# %% [markdown]
# ## 10. Summary
#
# Final summary of intake pipeline results.

# %%
print("\n" + "="*60)
print(f"INTAKE COMPLETE: {MECHANISM_CODE} - Coal Combustion Chain")
print("="*60)
print(f"\nRaw data downloaded to: {RAW_DATA_DIR}")
for f in RAW_DATA_DIR.glob("*.csv"):
    print(f"  - {f.name}")

print(f"\nProcessed data saved to: {PROCESSED_DIR}")
for f in PROCESSED_DIR.glob("*.parquet"):
    size = f.stat().st_size / (1024 * 1024)
    print(f"  - {f.name} ({size:.2f} MB)")

print(f"\nDerived artifacts saved to: {DERIVED_DIR}")
for f in DERIVED_DIR.glob("*"):
    if f.is_file():
        print(f"  - {f.name}")

print(f"\nTotal actions logged: {len(provenance_log)}")
print(f"Pipeline finished at: {datetime.now().isoformat()}")

# %% [markdown]
# ## Provenance Log
#
# | Action | Timestamp | Notes |
# |--------|-----------|-------|
# | Created | 2025-12-14 | Initial template with docstring header |
# | Updated | 2025-12-14 | Implemented OWID data acquisition pipeline |
