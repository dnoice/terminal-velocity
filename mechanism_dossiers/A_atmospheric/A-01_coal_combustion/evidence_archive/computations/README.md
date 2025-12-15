<!--
Metadata
    - Title: Computations Pipeline README (Terminal Velocity - v1.0)
    - File Name: README.md
    - Relative Path: mechanism_dossiers/A_atmospheric/A-01_coal_combustion/evidence_archive/computations/README.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

Description:
    Documentation for the A-01 Coal Combustion Chain computational pipeline.
    Provides instructions for setting up the environment, running the three-stage
    pipeline, and understanding the output artifacts.

Key Features:
    - Feature 1: Three-stage pipeline (intake, analysis, outputs)
    - Feature 2: Conda environment specification for reproducibility
    - Feature 3: Jupytext-compatible Python scripts
    - Feature 4: Parquet intermediate storage for efficiency
    - Feature 5: Terminal Velocity visual identity integration

Usage Instructions:
    Follow the steps below to run the complete pipeline.

Other Important Information:
    - Dependencies: See environment.yml
    - Compatible platforms: Linux, Windows, macOS
    - Estimated runtime: Varies by dataset size
---------
-->

# Computations: A-01 Coal Combustion Chain

## Overview

This directory contains the computational pipeline for mechanism A-01. The pipeline follows a three-stage architecture:

1. **01_intake.py** - Data acquisition, validation, and cleaning
2. **02_analysis.py** - Metric computation, scenarios, sensitivity analysis
3. **03_outputs.py** - Figure, table, and map generation

## Running the Pipeline

### Environment Setup

```bash
cd computations
conda env create -f environment.yml
conda activate tv-research
```

### Execute Pipeline

```bash
# Stage 1: Data intake
python 01_intake.py

# Stage 2: Analysis
python 02_analysis.py

# Stage 3: Output generation
python 03_outputs.py
```

### Alternative: Jupyter Notebooks

These scripts are Jupytext-compatible. Open directly in Jupyter:

```bash
jupyter notebook 01_intake.py
```

## Directory Structure

```
computations/
├── 01_intake.py          # Data acquisition & cleaning
├── 02_analysis.py        # Metrics & scenarios
├── 03_outputs.py         # Visualization generation
├── environment.yml       # Conda environment spec
└── README.md             # This file
```

## Outputs

| Stage | Output Location | Format |
|-------|-----------------|--------|
| Intake | `../datasets/processed/` | Parquet |
| Intake | `../datasets/derived/data_dictionary.csv` | CSV |
| Analysis | `../datasets/derived/results.csv` | CSV |
| Analysis | `../datasets/derived/parameter_sweeps.csv` | CSV |
| Outputs | `../../exhibits/figures/` | PNG |
| Outputs | `../../exhibits/tables/` | CSV |
| Outputs | `../../exhibits/maps/` | PNG |

## Color Palette

All visualizations use the Terminal Velocity color system:

| Color | Hex | Role |
|-------|-----|------|
| Deep Slate | `#2e3c44` | Background, authority |
| Burnt Orange | `#ff9e54` | Damage, urgency |
| Electric Green | `#46ff84` | Data, evidence |
| Soft White | `#f5f5f4` | Text, contrast |
| Gold | `#ffd144` | Uncertainty, caution |
| Teal | `#44cca4` | Solutions, leverage |

*All colors end in "4" - the harmonic signature.*

---

**Filed under: Causes of Death, Preventable**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
