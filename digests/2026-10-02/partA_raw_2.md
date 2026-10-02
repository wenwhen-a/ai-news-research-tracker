## FutureWorlds: Learning Robotic World Models from Alternative Futures
- **arXiv:** 2610.01019 · https://arxiv.org/abs/2610.01019
- **Submitted:** 2026-10-01
- **Authors:** Hao Wu, Shengju Qian, Weiyan Wang, Fan Xu, Fan Zhang, Yuanpeng He, Qingsong Wen, Yuxuan Liang
- **Qualifying affiliation(s):** Tencent — Weiyan Wang
- **Categories:** cs.CV; cs.RO
- **Open release:** code (GitHub: https://github.com/Alexander-wu/FutureWorlds)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FutureWorlds is a framework for learning robotic world models from "alternative futures": it unifies candidate future-scene construction, persistent memory for diverging trajectories, and learning from relative quality comparisons between candidates. It is built on a multimodal discrete autoregressive model and evaluated on the RT-1, BridgeV2, and RoboCasa robot manipulation datasets.
**Purpose (≤3 sentences):** Robotic world models predict action-conditioned future scenes, but the authors note that turning multiple alternative predictions into a useful learning signal is difficult: similar candidates give little comparative information, while diverging trajectories require persistent tracking of their individual histories.
**Breakthrough (≤3 sentences):** The authors report that FutureWorlds reduces LPIPS for 32-frame predictions by 14.78%, 20.84%, and 9.12% on RT-1, BridgeV2, and RoboCasa respectively, relative to the strongest baseline on each dataset. They also report that only 200 updates of their proposed MemSPO optimization further improve generation quality and extend prediction beyond the training horizon.
**Tools & method (≤3 sentences):** The method uses diverse beam search during reinforcement learning to construct candidate futures balancing confidence and diversity, and candidate-specific bounded memory to keep generation and policy-scoring histories consistent. MemSPO (Memory-Conditioned Search-Guided Policy Optimization) converts video-trajectory rewards into group-relative advantages to optimize the world model; code and a project page are released on GitHub.
**Limitation (≤3 sentences):** The authors state that autoregressive beam search incurs added inference latency, and that validating the approach in closed-loop planning and real robot control is left to future work.

---

## RelationVGGT: Visual Geometry Transformers for 3D Spatial Relation Segmentation
- **arXiv:** 2610.00970 · https://arxiv.org/abs/2610.00970
- **Submitted:** 2026-10-01
- **Authors:** Minsu Kim, Jaesung Choe, Jiwoo Lee, Yu-Chiang Frank Wang, Seon Joo Kim
- **Qualifying affiliation(s):** NVIDIA — Jaesung Choe, Yu-Chiang Frank Wang
- **Categories:** cs.CV; cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RelationVGGT is a feed-forward framework for 3D spatial relation segmentation: given a visually specified subject and a relational text query (with no category name provided), it segments the related target object across multiple views in a pose-free setting. It combines a visual foundation model's semantic features with a 3D geometry foundation model's geometry-aware representations through a relation transformer.
**Purpose (≤3 sentences):** The authors note that existing feed-forward 3D scene-understanding methods remain object-centric and neglect spatial relations between objects; the paper addresses segmenting a target defined by its relation to a subject, without per-scene optimization or known camera poses.
**Breakthrough (≤3 sentences):** The authors present 3D spatial relation segmentation as a new task formulation and report results against baselines including MVGGT and ReferSplat-style 3D referring-segmentation methods, along with a fully automated annotation pipeline for generating training data at scale.
**Tools & method (≤3 sentences):** The annotation pipeline is built on ScanNet++ using VLMs and LLMs to produce relation-labeled training data; the architecture couples a VGGT-style visual geometry transformer with a subject-conditioned relation-prediction transformer head.
**Limitation (≤3 sentences):** The authors state the data pipeline currently depends on datasets with instance-level annotations such as ScanNet++, limiting extension to unannotated or in-the-wild scenes, and that the framework models only object-object spatial relations rather than functional relations or full scene graphs.

---

## SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation
- **arXiv:** 2610.00686 · https://arxiv.org/abs/2610.00686
- **Submitted:** 2026-09-30
- **Authors:** Mikhail Dereviannykh, Vikram Voleti, Simon Donné, Mallikarjun Byrasandra Ramalinga Reddy, Shimon Vainer, Mark Boss
- **Qualifying affiliation(s):** Stability AI — Mikhail Dereviannykh; FLAG: borderline (not on the explicit qualified-company list but a comparable top-tier lab)
- **Categories:** cs.CV; cs.LG
- **Open release:** demo (project page with video examples: https://semantoken.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SemanTok is a flexible video tokenizer for autoregressive video generation that feeds frozen DINO features into its encoder and adds lightweight heads reconstructing those features from each retained token prefix, so early coarse tokens carry stronger global semantics.
**Purpose (≤3 sentences):** The authors state that existing flexible, coarse-to-fine video tokenizers only apply a representation-alignment (REPA) loss on early decoder hidden states, a target the decoder can partly satisfy from its noised input rather than from the tokens themselves.
**Breakthrough (≤3 sentences):** The authors report that a 201M-parameter SemanTok autoregressive model matches or beats a VideoFlexTok AR model 3.4× its size, that larger SemanTok models further improve fidelity, and that semantic alignment is retained on out-of-distribution classes and at every decoder noise level, including pure noise.
**Tools & method (≤3 sentences):** Training uses frozen DINO teacher features as both encoder input and per-prefix reconstruction target, with tokenizer training on Kinetics-600 and uCO3D and a LLaMA-style causal-decoder (RMSNorm, SwiGLU) autoregressive model built on top; a project page with video results is published.
**Limitation (≤3 sentences):** The authors state that at the smallest token budgets SemanTok and VideoFlexTok perform on par, and that with a cleaner (less noisy) latent, VideoFlexTok remains ahead at small token counts under some noise settings.

---

## Uncertainty-Aware RL-Controlled Adaptive 3D Mapping
- **arXiv:** 2610.00188 · https://arxiv.org/abs/2610.00188
- **Submitted:** 2026-09-17
- **Authors:** Alpay Ozkan, Tunc Ozan Aydin, Marc Pollefeys, Jelena Trisovic, Daniel Barath
- **Qualifying affiliation(s):** Microsoft — Daniel Barath (listed as ETH Zurich, Microsoft, ETH AI Center)
- **Categories:** cs.LG; cs.CV; cs.GR; eess.IV
- **Open release:** weights, code (GitHub: https://github.com/alpayozkan/UnRL)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper (project name "UnRL") proposes an adaptive 3D voxel mapping framework that refines voxel resolution based on semantic entropy, geometric curvature, and texture richness, paired with a reinforcement-learning agent that learns voxel-subdivision policies under a user-specified memory budget.
**Purpose (≤3 sentences):** The authors note that fixed-resolution TSDF volumetric mapping wastes memory in uniform regions and loses detail in complex ones, and that prior adaptive methods like MAP-ADAPT require hand-tuned, dataset-specific semantic class lists and give no explicit control over memory usage.
**Breakthrough (≤3 sentences):** The authors report that their multi-resolution TSDF approach matches or surpasses MAP-ADAPT and fixed-resolution baselines in geometric accuracy, semantic consistency, and memory-accuracy trade-offs on both synthetic and real-world datasets, replacing hand-tuned thresholds with a single user-specified memory-budget parameter.
**Tools & method (≤3 sentences):** The RL subdivision policy is trained with PPO across 4 parallel environments for 10M timesteps on a single workstation (Intel Core i7-14700K, NVIDIA GeForce RTX 3080, 10GB VRAM); evaluation uses the ScanNet and HSSD datasets, with additional experiments using SegFormer. Code and models are released on GitHub.
**Limitation (≤3 sentences):** The authors state their evaluation is currently limited to the indoor RGB-D setting of ScanNet and HSSD, and that extending the method to outdoor and larger-scale mapping scenarios is left to future work.

---

Verification pass: each of the 4 qualifying papers above was double-checked against both its arXiv abstract page (title, v1 date, authors, categories, not withdrawn) and its arXiv HTML page (author affiliation block read directly, not inferred from title/topic/lead).

# Near-misses
- 2610.01162 · PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models · academic-only — all six authors affiliated solely with Arizona State University (School of Computing and Augmented Intelligence); "NVIDIA" appears only in citations (Cosmos/Cosmos-Reason1 references), not as an author affiliation.
- 2610.01056 · HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction · academic-only — all authors affiliated with Peking University and Wuhan University; "NVIDIA" appears only as the GPU used for runtime benchmarking, not as an author affiliation.
- 2610.01052 · Towards Subject Consistency over Dynamic Subject Sets in Video Generation · academic-only — all three authors affiliated solely with Tsinghua University; the "Tsinghua-Bosch Joint ML Center" is a lab/center name, not an author affiliation with Bosch (not itself a qualified company), and no author is affiliated with any qualified company.
- 2610.00921 · In CEM, a World Model Is Also a Proposal Mechanism · academic-only — authors affiliated with UNSW Sydney and Harz University of Applied Sciences; "DeepMind" and "NVIDIA" appear only as a benchmark suite citation (DeepMind Control Suite) and GPU hardware (NVIDIA L40S), not as author affiliations.
- 2610.00691 · Soundwich: Video Generation with Layered and Controllable Audio · affiliation unverifiable — no arXiv HTML version exists (arxiv.org/html/2610.00691 returns 404); per instructions, PDF fallback is not permitted for affiliation verification, so the Google lead could not be confirmed or denied from the paper itself.
- 2610.00195 · GS-PQM: A Parameter-Domain Quality Metric for Compressed Gaussian Splatting · affiliation unverifiable — no arXiv HTML version exists (arxiv.org/html/2610.00195 returns 404); per instructions, PDF fallback is not permitted for affiliation verification, so the Google lead could not be confirmed or denied from the paper itself.
