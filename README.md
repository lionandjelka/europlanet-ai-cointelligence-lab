# From Signal to Scientific Decision — EUROPLANET AI Co-Intelligence Lab
![Exoplanet Cointelligence](https://img.shields.io/badge/Exoplanet-Cointelligence-6f42c1?style=for-the-badge)
A 90-minute planetary-science research practical on **information, transit detection, AI vetting, relational inference, uncertainty, and human–AI scientific decision making**.

## Scientific path

```text
PLATO-like simulated light curves
        ↓
BLS periodic evidence
        ↓
PANOPTICON-inspired local event detection
        ↓
official NASA ExoMiner++ vetting showcase
        ↓
local Neural Process / relational inference
        ↓
human–AI follow-up decision
```

The lab is **not a model leaderboard**. Each method receives a different representation of the evidence and answers a different scientific question.

## AI co-intelligence goals

Students learn to work with AI as a **scientific reasoning partner**, not a black-box classifier. By the end of the practical they should be able to:

- separate observation, representation, prediction, and scientific inference;
- ask what information an AI system received, preserved, compressed, or never had;
- identify inductive bias, target leakage, domain shift, false positives, and model–data mismatch;
- use disagreement between methods as information rather than treating it only as error;
- distinguish detection from astrophysical vetting;
- reason with uncertainty and missing context;
- use AI outputs together with physical knowledge to decide **what observation should come next**.

A recurring question throughout the lab is:

> **What did the model see, why did it make this prediction, what evidence is missing, and what measurement would most reduce the scientific uncertainty?**

## What is original, reimplemented, and official

| Component | Status in this repository |
|---|---|
| BLS | Precomputed results from the PLATO-like simulation project used for the school |
| PANOPTICON | **PANOPTICON-inspired 1-D U-Net3+ classroom reimplementation. Not author code and not author weights.** |
| ExoMiner++ | This repository provides helper scripts only. The actual ExoMiner++ software is the **official NASA ExoMiner pipeline/container**, run separately. |
| Neural Process | Compact **ConvCNP-style local Neural Process teaching implementation**; not author code and not QNPy-Latte |

See [`REFERENCES.md`](REFERENCES.md), [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), and [`models/MODEL_CARD.md`](models/MODEL_CARD.md).

## Repository layout

```text
europlanet-ai-cointelligence-lab/
├── README.md
├── environment.yml
├── requirements.txt
├── CITATION.cff
├── LICENSE
├── REFERENCES.md
├── THIRD_PARTY_NOTICES.md
├── DATA_PROVENANCE.md
├── student/
│   └── Europlanet_Research_Lab_90min.ipynb
├── examples/
│   └── Europlanet_Research_Lab_90min_EXECUTED.ipynb
├── data/
├── models/
├── assets/
├── exominer_official/
└── docs/
    ├── STUDENT_SETUP.md
    ├── AI_COINTELLIGENCE_OUTCOMES.md
    ├── PUBLISH_TO_GITHUB.md
    └── EUROPLANET_Student_Setup_and_Run_Guide_CoIntelligence.docx
```

The public package deliberately omits the instructor answer key and hidden mission-board truth.

## Quick start with Anaconda

```bash
conda env create -f environment.yml
conda activate europlanet-lab
python -m ipykernel install --user --name europlanet-lab --display-name "EUROPLANET Lab"
jupyter lab
```

Open:

```text
student/Europlanet_Research_Lab_90min.ipynb
```

and choose the **EUROPLANET Lab** kernel.

If you prefer pip inside an existing Python 3.11 conda environment:

```bash
python -m pip install -r requirements.txt
```

## 90-minute teaching flow

| Time | Activity | Scientific question | AI co-intelligence gain |
|---|---|---|---|
| 0–6 min | Mission, provenance, setup | What information reaches each algorithm? | Audit the AI evidence chain |
| 6–14 min | Data inspection | What is evidence, derived information, or simulation truth? | Detect leakage and representation traps before modelling |
| 14–26 min | BLS | When does periodic evidence become a false positive? | Challenge an apparently strong algorithmic score |
| 26–44 min | PANOPTICON-inspired U-Net3+ | Can local morphology rescue/reject BLS candidates? | Compare inductive biases and exploit model disagreement |
| 44–57 min | Official NASA ExoMiner++ showcase | Why is vetting different from detection? | Combine heterogeneous evidence rather than one score |
| 57–72 min | Local Neural Process | Why does locality/context matter? | Test what AI can infer from observed versus missing information |
| 72–87 min | Mission board | Which five targets deserve scarce follow-up? | Make human–AI decisions under resource constraints |
| 87–90 min | Exit ticket | What should a scientific representation preserve? | Move from prediction to scientific inference |

## ExoMiner++

ExoMiner++ is not vendored into this repository. The `exominer_official/` directory contains only helper files for the teaching demonstration. Obtain/run the official NASA pipeline from:

- NASA ExoMiner repository: https://github.com/nasa/Exominer

The live official-pipeline step requires network access and Podman. For a classroom, pre-run the official pipeline and cache its outputs before the session.

## Data and provenance

The distributed tables and short windows are teaching products derived from the supplied PLATO-like simulation project. The package does **not** claim to contain the original large raw simulation HDF5 files. See [`DATA_PROVENANCE.md`](DATA_PROVENANCE.md) before public redistribution.

## Citation

GitHub will read [`CITATION.cff`](CITATION.cff). Scientific methods must also be cited separately; see [`REFERENCES.md`](REFERENCES.md).

## License

Original lab code, original teaching text, and original diagrams in this repository are released under the terms described in [`LICENSE`](LICENSE). Third-party software and publications retain their own licenses. The official NASA ExoMiner software is **not included** here.
