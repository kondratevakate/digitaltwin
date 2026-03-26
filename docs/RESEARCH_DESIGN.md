# Research Design: Process-Driven Digital Twins for ED Operations

## Research Question

**Primary RQ**: Can process-mined event logs serve as the foundation for operational digital twins that enable counterfactual policy evaluation in emergency departments?

**Sub-questions**:
1. How accurately can process discovery algorithms reconstruct ED patient pathways?
2. Can discovered process models be calibrated to simulate realistic patient flow?
3. What is the validity of counterfactual estimates from process-based digital twins compared to causal inference baselines?

## Gap Analysis

| Existing Work | Gap |
|---------------|-----|
| Sepsis + Process Mining | Descriptive only, no simulation/twin |
| Healthcare Digital Twins | Physiological models, not operational/process-based |
| ED Simulation | Hand-crafted models, not data-driven discovery |
| Causal Inference in Healthcare | No integration with process mining |

**Our contribution**: Bridge process mining and causal inference to create *data-driven operational digital twins* that can:
1. Automatically discover process structure from event logs
2. Calibrate simulation parameters from historical data
3. Evaluate counterfactual policies with uncertainty quantification

## Methods Pipeline

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Event Log      │────▶│ Process Discovery │────▶│ Discovered      │
│  (MIMICEL/      │     │ (Inductive Miner) │     │ Process Model   │
│   Sepsis XES)   │     └──────────────────┘     └────────┬────────┘
└─────────────────┘                                       │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Counterfactual  │◀────│ Policy Evaluation │◀────│ Calibrated      │
│ Estimates       │     │ (DR-OPE)          │     │ Simulator       │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

## Datasets

| Dataset | Role | Size | Access |
|---------|------|------|--------|
| Sepsis Cases | Baseline reproduction | 1,050 cases | Public |
| MIMICEL | Primary experiments | 425K cases | PhysioNet (CITI) |
| MIMIC-IV-Ext-CEKG | Object-centric extension | OCEL format | PhysioNet (CITI) |

## Baselines to Reproduce

From literature (Sepsis Cases dataset):

| Metric | Inductive Miner | Target |
|--------|-----------------|--------|
| Fitness | 84.8% | Reproduce ±2% |
| Precision | 25.7% | Reproduce ±2% |
| Generalization | 90.2% | Reproduce ±2% |

## Novelty Claims

1. **First process-mined digital twin for ED** with simulation capabilities
2. **Integration of causal inference** (CATE estimation, DR-OPE) with process mining
3. **Validation framework** comparing twin predictions to causal baselines

## Open Research Tasks

See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to pick up tasks.

### Phase 1: Baseline (Sepsis)
- [x] Data loading and EDA
- [ ] Process discovery (Inductive/Heuristic Miner)
- [ ] Conformance checking
- [ ] Performance/bottleneck analysis
- [ ] Simulation from discovered model

### Phase 2: Extension (MIMICEL)
- [ ] OCEL data preparation
- [ ] Object-centric process mining
- [ ] Multi-object simulation
- [ ] Comparison with single-object approach

### Phase 3: Causal Integration
- [ ] Define "treatments" (routing decisions, timing)
- [ ] CATE estimation (causal forests, meta-learners)
- [ ] DR offline policy evaluation
- [ ] Comparison: simulation vs causal estimates

## Key References

See [references.bib](../paper/references.bib) for full citations.

**Process Mining**:
- Camargo et al. 2020 — Event-log-calibrated simulation discovery
- Munoz-Gama et al. 2022 — Healthcare PM survey (200+ papers)

**Causal Inference**:
- Wager & Athey 2018 — Causal forests
- Künzel et al. 2019 — Meta-learners (S/T/X)
- Dudík et al. 2014 — Doubly robust policy evaluation

**ED Operations**:
- Hao et al. 2025 — Fast-track routing with IV + simulation
- Clarke et al. 2023 — Synthetic control for ED redesign evaluation
