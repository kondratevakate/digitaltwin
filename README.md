# Process-Driven Digital Twins for Emergency Department Operations

[![Target](https://img.shields.io/badge/Target-DT4H%20Workshop%20@%20MICCAI%202026-blue)]()
[![Status](https://img.shields.io/badge/Status-Active%20Research-green)]()

## Research Question

> **Can process-mined event logs serve as the foundation for operational digital twins that enable counterfactual policy evaluation in emergency departments?**

## The Gap

| Existing Work | Limitation |
|---------------|------------|
| Process Mining + Healthcare | Descriptive analysis only, no simulation or "what-if" |
| Healthcare Digital Twins | Physiological models (organ systems), not operational workflows |
| ED Simulation | Hand-crafted models that don't adapt to data |
| Causal Inference in Healthcare | No integration with process-level representations |

## Our Approach

We bridge **process mining** and **causal inference** to create data-driven operational digital twins:

```
Event Log → Process Discovery → Calibrated Simulator → Counterfactual Policy Evaluation
    │              │                    │                         │
    │              │                    │                         └─ "What if we routed
    │              │                    │                             patients differently?"
    │              │                    └─ Simulation matches
    │              │                       historical distributions
    │              └─ Automatic structure
    │                 learning from data
    └─ Real clinical workflows
       (MIMIC-IV, Sepsis cases)
```

## Current Status

| Phase | Status | Description |
|-------|--------|-------------|
| 1. Baseline | 🔄 In Progress | Reproduce Sepsis PM results |
| 2. Extension | ⏳ Planned | Apply to MIMICEL (425K ED cases) |
| 3. Causal | ⏳ Planned | Integrate CATE estimation & DR-OPE |

## Quick Start

```bash
# Setup
git clone <repo-url> && cd digitaltwin
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Configure data paths
cp experiments/.env.example experiments/.env
# Edit .env with your local paths

# Run analysis
jupyter notebook experiments/
```

## Datasets

| Dataset | Cases | Events | Access |
|---------|-------|--------|--------|
| [Sepsis Cases](https://data.4tu.nl/datasets/915d2bfb-7e84-49ad-a286-dc35f063a460) | 1,050 | 15K | Public |
| [MIMICEL](https://physionet.org/content/mimicel/) | 425K | 7.5M | PhysioNet |
| [MIMIC-IV-Ext-CEKG](https://physionet.org/content/mimic-iv-ext-cekg/) | OCEL | - | PhysioNet |

## Baseline Targets

Reproducing [prior work](https://doi.org/10.1016/j.health.2023.100147) on Sepsis:

| Metric | Inductive Miner | Our Target |
|--------|-----------------|------------|
| Fitness | 84.8% | ±2% |
| Precision | 25.7% | ±2% |
| Generalization | 90.2% | ±2% |

## Project Structure

```
digitaltwin/
├── docs/
│   └── RESEARCH_DESIGN.md   # Full research design & open tasks
├── experiments/              # Analysis code (notebooks not committed)
│   ├── config.py             # Path configuration
│   └── .env.example          # Template for local paths
├── paper/
│   ├── references.bib        # 15+ key references
│   └── *.tex                 # MICCAI template
├── figures/                  # Generated visualizations
└── results/                  # Output metrics (CSV)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Open research tasks
- Setup instructions
- Workflow guidelines

**Looking for collaborators with expertise in**:
- Process Mining (PM4Py, conformance checking)
- Causal Inference (CATE, doubly robust methods)
- Healthcare Simulation (DES, calibration)

## Key References

- Camargo et al. 2020 — [Event-log-calibrated simulation](https://doi.org/10.1016/j.dss.2020.113284)
- Wager & Athey 2018 — [Causal forests](https://doi.org/10.1080/01621459.2017.1319839)
- Hao et al. 2025 — [ED fast-track routing](https://doi.org/10.1287/msom.2022.0440)
- Munoz-Gama et al. 2022 — [Healthcare PM survey](https://doi.org/10.1016/j.jbi.2022.103994)

See [paper/references.bib](paper/references.bib) for full bibliography.

## License

MIT
