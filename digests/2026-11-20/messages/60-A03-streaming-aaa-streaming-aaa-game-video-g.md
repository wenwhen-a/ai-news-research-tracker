**[A03] Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**
- **arXiv:** 2611.26040 · <https://arxiv.org/abs/2611.26040>
- **Submitted:** 2026-11-19
- **Authors:** Zhihao Hu et al.
- **Qualifying affiliation(s):** Tencent — all listed authors (affiliation block lists "Tencent AIPD" for the group)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** Streaming-AAA is a system for controllable, long-horizon generation of AAA-quality game video for interactive game simulation, using Genshin Impact as its primary test game.
**Purpose:** The authors argue prior streaming world models for games either degrade over long play sessions or cannot combine high resolution, high frame rate, and low latency simultaneously.
**Breakthrough:** The authors report a VBench average of 0.832 versus 0.747-0.810 for compared baselines (Lingbot, YUME, Matrix Game 3.0, HY-World1.5), and an imaging-quality score of 0.677 versus 0.589 for HY-World1.5. Baselines ran at 480p-720p and 2.1-6.7 FPS with 6.6-11.3 s latency, versus Streaming-AAA's 1080p/43 FPS/198 ms, and the authors report no visible quality collapse over a one-hour stress test.
**Tools & method:** The system uses a causal video VAE (4×16×16 compression with a Pixel Shuffle decoder layer) feeding a factorized 3D-UNet latent diffusion backbone, pretrained with diffusion forcing over clips growing from 64 to 640 frames, then post-trained with distribution matching distillation (DMD) and a hybrid 30-token memory (22 sparse long-term, 8 recent short-term) for two-step inference.
**Limitation:** The authors state the model is trained on data from a single game, so generalization to other titles, art styles, or mechanics is limited, and they describe a universal game-generation model without per-game fine-tuning as an open challenge.
