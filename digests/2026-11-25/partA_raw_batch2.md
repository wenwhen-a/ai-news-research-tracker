## DraftKV: Protecting Persistent Worlds through Hierarchical Streaming Retrieval
- **arXiv:** 2611.31944 · https://arxiv.org/abs/2611.31944
- **Submitted:** 2026-11-24
- **Authors:** Xiaoling Zhou, Haopeng Li, Yufa Zhou, Rui Ding, Yu Li, Jun Lin, Enze Xie, Chunhua Shen, Xuan Shen
- **Qualifying affiliation(s):** NVIDIA Research (affiliation listed in the author block; the HTML render does not cleanly map it to one specific name among Yu Li/Jun Lin/Enze Xie, but NVIDIA Research is explicitly listed as one of the paper's institutions)
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** Interactive video world models that respond to actions and camera movement tend to lose spatial and appearance consistency when a user revisits earlier locations. The authors propose DraftKV, a training-free method that retrieves historical KV caches for autoregressive video diffusion models using geometric grounding and query-conditioned relevance, combined with CPU offloading and tile-wise streaming attention.
**Purpose (≤3 sentences):** To let long-horizon, persistent interactive video worlds stay consistent when revisiting earlier content without the latency and memory cost of retrieving and attending over a growing KV-cache history.
**Breakthrough (≤3 sentences):** The authors report a 3.27× end-to-end speedup and a 42.2% reduction in peak GPU memory versus other CPU-offloaded KV-retrieval methods, and demonstrate interactive world generation running on a single H100 GPU with the SolarWM-33B model.
**Tools & method (≤3 sentences):** The method includes a theoretical analysis of retrieval utility loss and a streaming attention scheme that overlaps data transfer with computation; it is training-free and tested with the SolarWM-33B model on a single NVIDIA H100 GPU.
**Limitation (≤3 sentences):** Not stated in the available excerpt beyond the method being evaluated against other CPU-offloaded retrieval baselines rather than against non-offloaded approaches.

## HiGS: A Hierarchical Architecture for Fast Differentiable 3D Gaussian Splatting
- **arXiv:** 2611.31918 · https://arxiv.org/abs/2611.31918
- **Submitted:** 2026-11-24
- **Authors:** Dawid Pająk, Martin Bisson, Rodolfo Lima, François Trudel
- **Qualifying affiliation(s):** NVIDIA (all four authors)
- **Categories:** cs.CV (primary), cs.GR (cross-listed)
- **Open release:** none stated

**Summary (≤3 sentences):** Standard 3D Gaussian Splatting (3DGS) partitions, rasterizes, and schedules work by screen tile, so the densest tiles set the frame time for the whole image. HiGS gives each of those roles its own granularity: Gaussians are partitioned over coarse macro-tiles, rasterized at finer granularity, and processed in bounded, depth-sorted batches so dense regions simply issue more batches.
**Purpose (≤3 sentences):** To remove the tile-bottleneck that limits both rendering and training speed in differentiable 3DGS pipelines, for scenes with uneven density across the view.
**Breakthrough (≤3 sentences):** The authors report HiGS renders faster than every published method they evaluated against, with the largest gains on unevenly loaded views, and that it reconstructs scenes faster and with less memory at equal image quality using exact front-to-back alpha compositing.
**Tools & method (≤3 sentences):** The same batched, depth-sorted structure used for rendering also supports training/backpropagation; the authors fuse the optimizer into the backward pass and halve stored parameters and optimizer moments, deferring appearance updates outside the current view.
**Limitation (≤3 sentences):** Not stated in the available excerpt.

## CaLA: Causal Latent Adjustment for World Models under Adaptive Policies
- **arXiv:** 2611.31431 · https://arxiv.org/abs/2611.31431
- **Submitted:** 2026-11-23
- **Authors:** Robert Ness, Sofiane Ennadir, Oleg Smirnov
- **Qualifying affiliation(s):** Microsoft Research (Robert Ness); King AI Labs, Microsoft Gaming (Sofiane Ennadir, Oleg Smirnov)
- **Categories:** cs.LG
- **Open release:** none stated

**Summary (≤3 sentences):** The authors study how adaptive game-balancing policies — using Match-3 difficulty adjustment as the testbed — create confounding in world-model rollouts, since a player's latent skill affects both the difficulty they are assigned and whether they churn. They build a fully specified structural causal model with ground-truth interventions and show standard models fit to logged data can recommend difficulty settings that actually increase churn.
**Purpose (≤3 sentences):** To build a world model for adaptive-difficulty game systems that gives reliable causal estimates of how a difficulty intervention affects player churn, rather than merely predictive accuracy on logged (confounded) data.
**Breakthrough (≤3 sentences):** The authors report their proposed Causal Latent Adjustment (CaLA), a DAG-constrained world model inferring a variational player representation from pre-treatment history, gives the most reliable population-level intervention estimates among the methods tested, with competitive individual-level decisions.
**Tools & method (≤3 sentences):** CaLA is evaluated against a Match-3 structural causal model built specifically for this study, with ground-truth interventions used to check whether each model's recommended difficulty changes match the true causal effect.
**Limitation (≤3 sentences):** The authors state that rich handcrafted histories can outperform CaLA for individual-level (rather than population-level) adjustment, and that residual correction can hurt causal decision quality even while improving predictive fit.

# Near-misses
- 2611.31910 · ReJEPA: Bounded Predictive Regulation for Latent World Models · no HTML version exists (404) and the abstract page does not state author affiliations, so the affiliation gate is unverifiable
- 2611.31755 · RVLM-X: Towards a Universal VLM Harness · off-topic — a general vision-language-model harness for photos/charts/maps, not 3D, world models, character animation, or game engines; no qualifying-company affiliation stated either
- 2611.31466 · AdProducer: Towards Agentic Advertising Video Generation · off-topic — agentic advertising-video generation, not games or the tracked topics
- 2611.31184 · On-Policy Codec Distillation for Efficient All-in-One Video Generation · qualifying Adobe Research affiliation is present, but the paper is generic infrastructure/efficiency work for conditioned video generation broadly, not specifically 3D, world models, character animation, or game engines
- 2611.30666 · Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning · sole affiliation is "Beijing Freedo Technology Co., Ltd.", an unverified small/unknown company with no evidence of being a tracked or clearly comparable top-tier lab
- 2611.31895 · Loupe: Reinforcing Knowledge-Intensive Video Generation Agents · only a borderline-tier affiliation (Ant Group) is present, and the topic (search-grounded/advertising-adjacent video generation accuracy) is not genuinely on the four tracked topics
- 2611.31836 · Gaze World Model · qualifying Google affiliation (Zhongyi Zhou) is present, but despite "World Model" in the title the paper is about human gaze/attention estimation in video, not interactive 3D/world-model, character-animation, or game-engine content

Verification pass: every passing paper's v1 submission date, author affiliations (from the arXiv HTML render), categories, and topic fit were checked directly against the arxiv.org abstract and HTML pages; claims above are the authors' own stated results, not independently re-run.
