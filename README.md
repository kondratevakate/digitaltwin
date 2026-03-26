# Process-Driven Digital Twin for Healthcare

Paper submission for **DT4H Workshop** (Digital Twin for Healthcare) at **MICCAI 2026**.

## Overview

This project explores the construction of digital twins from clinical event logs using process mining techniques. We reproduce baseline results on the Sepsis Cases dataset and extend the approach to object-centric event logs (MIMIC-IV-Ext-CEKG).

## Project Structure

```
digitaltwin/
├── experiments/          # Jupyter notebooks for analysis
│   ├── 01_sepsis_eda.ipynb
│   ├── 02_sepsis_discovery.ipynb
│   ├── 03_sepsis_conformance.ipynb
│   ├── 04_sepsis_performance.ipynb
│   ├── 05_sepsis_twin.ipynb
│   └── utils/
├── paper/                # LaTeX source for the paper
├── figures/              # Generated figures for the paper
└── results/              # Output metrics and data
```

## Datasets

### 1. Sepsis Cases Event Log (Primary)

Real-life event log from a hospital ERP system containing ~1,000 sepsis patient cases.

- **Cases**: 1,050
- **Events**: 15,214
- **Activities**: 16
- **Attributes**: 39 (including SIRS criteria, CRP, Lactic Acid)

**Download**: [4TU.ResearchData](https://data.4tu.nl/articles/dataset/Sepsis_Cases_-_Event_Log/12707639)

**Citation**:
```
Mannhardt, F. (2016). Sepsis Cases - Event Log.
Eindhoven University of Technology. Dataset.
https://doi.org/10.4121/uuid:915d2bfb-7e84-49ad-a286-dc35f063a460
```

### 2. MIMIC-IV-Ext-CEKG (Extension)

Object-centric event log derived from MIMIC-IV with ICD-10 and SNOMED-CT mappings.

- **Format**: OCEL 2.0
- **Object types**: Patient, Admission, Diagnosis, Procedure, Medication

**Download**: [PhysioNet](https://physionet.org/content/mimic-iv-ext-cekg/) (requires CITI training)

### 3. MIMIC-IV-ED Demo (Fallback)

Demo subset of MIMIC-IV Emergency Department data.

**Download**: [PhysioNet](https://physionet.org/content/mimic-iv-ed/2.2/)

## Installation

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install pm4py pandas numpy matplotlib jupyter
```

## Usage

```bash
# Start Jupyter
jupyter notebook experiments/

# Or run individual notebooks
jupyter notebook experiments/01_sepsis_eda.ipynb
```

## Baseline Targets

From [Optimizing sepsis care through heuristics methods in process mining](https://www.sciencedirect.com/science/article/pii/S2772442523000540):

| Model | Fitness | Precision | Simplicity | Generalization |
|-------|---------|-----------|------------|----------------|
| Inductive Miner | 84.8% | 25.7% | 62.2% | 90.2% |
| Systematic (expert) | 97.8% | 40.4% | 77.7% | 80.2% |

## References

- Mannhardt, F. (2016). Sepsis Cases - Event Log.
- PM4Py: Process Mining for Python. https://pm4py.fit.fraunhofer.de/
- Munoz-Gama et al. (2022). Process mining for healthcare: Characteristics and challenges. J Biomedical Informatics.

## License

MIT
