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
# # Data Intake: C-05 - Nutrient Loading Dead Zones
# 
# **Purpose:** Download, validate, and clean source datasets for this mechanism.
# 
# **Outputs:**
# - `../datasets/processed/clean_dataset.parquet`
# - `../datasets/derived/data_dictionary.csv`

# %% [markdown]
# ## Setup

# %%
import pandas as pd
from pathlib import Path
from datetime import datetime

# Configuration
MECHANISM_CODE = "C-05"
RAW_DATA_DIR = Path("../datasets/raw")
PROCESSED_DIR = Path("../datasets/processed")
DERIVED_DIR = Path("../datasets/derived")

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
DERIVED_DIR.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# ## 1. Data Acquisition
# 
# Document all data sources and download methods here.

# %%
# TODO: Implement data download
# Example:
# import requests
# url = "https://example.com/data.csv"
# response = requests.get(url)
# (RAW_DATA_DIR / "source_data.csv").write_bytes(response.content)

print(f"[{datetime.now()}] Data acquisition step - implement for C-05")

# %% [markdown]
# ## 2. Schema Validation
# 
# Verify expected columns, types, and constraints.

# %%
# TODO: Load and validate schema
# df = pd.read_csv(RAW_DATA_DIR / "source_data.csv")
# 
# Expected schema:
# EXPECTED_COLUMNS = ["year", "value", "unit", "source"]
# assert all(col in df.columns for col in EXPECTED_COLUMNS), "Missing columns"

print("Schema validation step - implement validation logic")

# %% [markdown]
# ## 3. Data Cleaning
# 
# Handle missing values, outliers, unit conversions.

# %%
# TODO: Implement cleaning pipeline
# df_clean = df.copy()
# df_clean = df_clean.dropna(subset=["value"])
# df_clean["value"] = pd.to_numeric(df_clean["value"], errors="coerce")

print("Data cleaning step - implement cleaning logic")

# %% [markdown]
# ## 4. Export Processed Data

# %%
# TODO: Save cleaned data
# df_clean.to_parquet(PROCESSED_DIR / "clean_dataset.parquet", index=False)
# 
# # Generate data dictionary
# data_dict = pd.DataFrame({
#     "column": df_clean.columns,
#     "dtype": df_clean.dtypes.astype(str),
#     "non_null_count": df_clean.count(),
#     "description": ["TODO"] * len(df_clean.columns)
# })
# data_dict.to_csv(DERIVED_DIR / "data_dictionary.csv", index=False)

print(f"[{datetime.now()}] Intake complete for C-05")

# %% [markdown]
# ## Provenance Log
# 
# | Action | Timestamp | Notes |
# |--------|-----------|-------|
# | Created | 2025-12-14 | Initial template |
