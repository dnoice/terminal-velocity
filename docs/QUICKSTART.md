<!--
✒ Metadata
    - Title: Quick Start Guide (Terminal Velocity - v1.0)
    - File Name: QUICKSTART.md
    - Relative Path: docs/QUICKSTART.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-14
    - Update: Sunday, December 14, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!

✒ Description:
    Fast-track guide to setting up and contributing to Terminal Velocity.
    Gets you from zero to running in 10 minutes.
---------
-->

# Quick Start Guide

> *Get from zero to documenting in 10 minutes.*

---

## Prerequisites

- Python 3.10+
- Git
- ~500MB disk space (full scaffold)
- Optional: conda/mamba for environment management

---

## 1. Clone the Repository

```bash
git clone https://github.com/dnoice/terminal-velocity.git
cd terminal-velocity
```

---

## 2. Set Up Environment

### Option A: Conda/Mamba (Recommended)

```bash
# Create environment from spec
conda env create -f computational_core/environment_specs/environment.yml

# Activate
conda activate tv-research
```

### Option B: Pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r computational_core/environment_specs/requirements.txt
```

---

## 3. Scaffold a Fresh Project (Optional)

If you want to create a new Terminal Velocity instance:

```bash
# Full build
python tools/tv_scaffold.py ./my-research --verbose

# Dry run (preview)
python tools/tv_scaffold.py ./my-research --dry-run

# Specific vectors only
python tools/tv_scaffold.py ./my-research --vectors A B C
```

---

## 4. Explore the Structure

```
terminal-velocity/
├── mechanism_dossiers/     # ← START HERE
│   ├── A_atmospheric/      #   Mechanisms by damage vector
│   ├── B_biosphere/
│   ├── C_hydrological/
│   ├── D_chemical/
│   ├── E_depletion/
│   └── F_systemic/
├── connection_atlas/       # Cross-mechanism links
├── evidence_vault/         # Shared datasets, sources
├── synthesis_products/     # Derived outputs
├── computational_core/     # Shared code, environment
├── visual_assets/          # Templates, colors, icons
├── tools/                  # Scaffold and utilities
└── docs/                   # Documentation
```

---

## 5. Navigate a Dossier

Each mechanism dossier follows the same structure:

```
A-01_coal_combustion/
├── DOSSIER.md              # ← Main document (start here)
├── damage_report/          # What's destroyed
├── pathway_analysis/       # How it happens
├── driver_profile/         # Who benefits/decides
├── evidence_archive/
│   ├── datasets/           # raw → processed → derived
│   ├── sources/            # bibliography, claim traces
│   └── computations/       # Notebooks
├── uncertainty_register/   # What we don't know
├── intervention_assessment/# What would work
├── connection_map/         # Links to other mechanisms
└── exhibits/               # Figures, tables, maps
```

---

## 6. Run a Notebook

```bash
# Navigate to a mechanism's computations
cd mechanism_dossiers/A_atmospheric/A-01_coal_combustion/evidence_archive/computations

# Run the pipeline
python 01_intake.py      # Data acquisition & cleaning
python 02_analysis.py    # Metrics & scenarios
python 03_outputs.py     # Generate figures & tables
```

Or use Jupyter:

```bash
jupyter lab
# Open notebooks and run interactively
```

---

## 7. Make Your First Contribution

### Small: Fix a typo or broken link

```bash
git checkout -b fix/typo-in-readme
# Make changes
git commit -m "[DOCS] Fix typo in README"
git push origin fix/typo-in-readme
# Open PR on GitHub
```

### Medium: Add evidence to existing dossier

```bash
git checkout -b evidence/A-01-updated-sources
# Update sources, claim_trace.md
git commit -m "[EVIDENCE] Add 2024 emissions data to A-01"
git push origin evidence/A-01-updated-sources
# Open PR with Evidence Update template
```

### Large: Propose new mechanism

1. Open issue using "Mechanism Proposal" template
2. Wait for approval
3. Create branch and dossier
4. Submit PR when complete

---

## 8. Key Commands

```bash
# Scaffold new project
python tools/tv_scaffold.py <target> [options]

# Validate notebook execution
python -m pytest mechanism_dossiers/

# Check code style
black --check .
ruff check .

# Generate figures for a dossier
cd <dossier>/evidence_archive/computations
python 03_outputs.py
```

---

## 9. Quick Reference

### Evidence Grades

| Grade | Name | Use For |
|-------|------|---------|
| I | Direct Measurement | Damage quantification |
| II | Official Inventory | Baseline metrics |
| III | Validated Model | Projections, scenarios |
| IV | Expert Assessment | Context, synthesis |
| V | Qualified Report | Supplementary |
| VI | Contextual | Background only |

### Status Icons

| Icon | Status |
|------|--------|
| 🔴 | Critical |
| 🟠 | Accelerating |
| 🟡 | Active |
| 🟢 | Declining |
| ⚪ | Dormant |

### Color Palette

```
#2e3c44  Deep Slate      Background
#ff9e54  Burnt Orange    Damage
#46ff84  Electric Green  Data
#f5f5f4  Soft White      Text
#ffd144  Gold            Uncertainty
#44cca4  Teal            Solutions
```

---

## 10. Get Help

- **Documentation:** `docs/` directory
- **Questions:** Open issue with "Question" label
- **Bugs:** Use "Bug Report" template
- **Ideas:** Open discussion

---

## Next Steps

1. Read [CONTRIBUTING.md](../CONTRIBUTING.md) for full guidelines
2. Review [EVIDENCE_GRADING.md](EVIDENCE_GRADING.md) for source standards
3. Explore existing dossiers as examples
4. Pick a mechanism and start investigating

---

**The record is waiting. Let's build it.**

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
