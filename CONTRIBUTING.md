# Contributing Guide

## Quick Start

```bash
# 1. Clone and setup
git clone <repo-url>
cd digitaltwin
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Configure data paths
cp experiments/.env.example experiments/.env
# Edit .env with your local data paths

# 3. Verify setup
cd experiments
python -c "from config import SEPSIS_PATH; print(f'Data ready: {SEPSIS_PATH.exists()}')"
```

## Project Structure

```
digitaltwin/
├── docs/                 # Research design, SOTA analysis
│   └── RESEARCH_DESIGN.md
├── experiments/          # Analysis notebooks (not committed)
│   ├── config.py         # Path configuration
│   └── .env              # Local paths (not committed)
├── paper/                # LaTeX source
│   └── references.bib    # Bibliography
├── figures/              # Generated figures
└── results/              # Output metrics
```

## Open Tasks

### For Process Mining Expertise
- [ ] Implement process discovery comparison (Inductive vs Heuristic Miner)
- [ ] Conformance checking against clinical guidelines
- [ ] Object-centric PM on MIMIC-IV-Ext-CEKG

### For Causal Inference Expertise
- [ ] Define treatment variables from ED routing decisions
- [ ] Implement CATE estimation (causal forests / meta-learners)
- [ ] Doubly robust offline policy evaluation

### For Simulation Expertise
- [ ] Calibrate DES from discovered process model
- [ ] Implement what-if scenario analysis
- [ ] Validate simulation vs historical distributions

## Workflow

1. **Pick a task** from Open Tasks above
2. **Create a branch**: `git checkout -b feature/your-task`
3. **Work in notebooks** (not committed) or **create scripts** in `experiments/`
4. **Export results** to `results/` as CSV
5. **Export figures** to `figures/` as PNG
6. **Update paper** if findings are significant
7. **Submit PR** with description of findings

## Code Style

- Python 3.11+
- Use `config.py` for all paths (no hardcoded paths)
- Notebooks are for exploration, scripts for reproducible analysis
- Document key findings in markdown cells

## Data Access

| Dataset | How to Get |
|---------|------------|
| Sepsis Cases | [4TU.ResearchData](https://data.4tu.nl/datasets/915d2bfb-7e84-49ad-a286-dc35f063a460) — public |
| MIMICEL | [PhysioNet](https://physionet.org/content/mimicel/) — requires CITI training |
| MIMIC-IV-Ext-CEKG | [PhysioNet](https://physionet.org/content/mimic-iv-ext-cekg/) — requires CITI training |

## Communication

- Research questions → open GitHub Issue
- Paper drafts → shared Overleaf (link TBD)
- Quick sync → [TBD: Slack/Discord/Email]
