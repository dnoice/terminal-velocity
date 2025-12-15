# Computations: B-02

## Running the Pipeline

```bash
cd computations
conda env create -f environment.yml
conda activate tv-research
python 01_intake.py
python 02_analysis.py
python 03_outputs.py
```

## Outputs

- `../datasets/processed/` - Cleaned data
- `../datasets/derived/` - Computed metrics
- `../../exhibits/` - Figures and tables
