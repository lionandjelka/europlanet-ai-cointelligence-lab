# Model card — PANOPTICON-inspired classroom detector

## Intended purpose

A compact 1-D U-Net3+ style detector used to teach **local transit-event morphology** and contrast it with periodic BLS evidence and multi-diagnostic ExoMiner++ vetting.

## Provenance

- Inspired by the single-event transit-detection task and U-Net-family design discussed by Vivien et al. (2025).
- **Not official PANOPTICON source code.**
- **Not trained with official PANOPTICON weights.**
- Classroom training windows are derived from the supplied PLATO-like simulation metadata.

## Architecture

- 1-D U-Net3+ style network, depth 4.
- Full-scale encoder-to-decoder fusion.
- Node block: Conv1D → BatchNorm → ReLU.
- Max-pooling by two for downsampling.
- One output logit per time sample; sigmoid converts it to event probability.

## Classroom optimization

Positive-event weighting is used to stabilize fast training on short and strongly imbalanced windows.

## Deterministic teaching-realization performance

- Event-level AUC: **0.958**.
- Threshold calibrated to approximately 5% no-planet false alarms: **TPR ≈ 89.0%, FPR ≈ 5.1%**.

These values are **not mission forecasts and not PANOPTICON paper performance claims**. They describe this prepared teaching realization only.

## Appropriate interpretation

Use the model to discuss inductive bias, local morphology, threshold choice, disagreement with BLS, domain shift, and false positives. Do not use it as a production PLATO pipeline or as a substitute for the published PANOPTICON implementation.
