# Part A — Papers
Window: last 30 days (2026-08-25 to 2026-09-24). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: website fallback (arxiv.org/search; arXiv API returned HTTP 406 for all queries). Qualifying papers: 4 (0 flagged).

---
## Unity Insight: A Production Code–Asset Index for LLM Coding Agents in Unity Projects
- **arXiv:** 2609.27585 · https://arxiv.org/abs/2609.27585
- **Submitted:** 2026-09-23
- **Authors:** Shenhua Gu, Hongqiang Zhu, Fan Zhang, Jinming Zhang, Hao Chen
- **Qualifying affiliation(s):** Unity — all five authors list "Tuanjie Engine, Unity China, Shanghai, China" (Tuanjie Engine is Unity's own engine brand/joint venture operated for the China market)
- **Categories:** cs.SE
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Unity Insight, a persistent, read-only code–asset index built to let LLM coding agents navigate Unity game-engine repositories, where gameplay logic spans C# scripts, prefabs, scenes, and ScriptableObjects linked by GUIDs and YAML serialization. It is described as already deployed in production. The authors evaluate it on 28 project-specific questions across two Unity games.

**Purpose (≤3 sentences):** Traditional code-only retrieval tools cannot answer cross-file questions common in Unity projects (e.g., "which prefabs instantiate this script?") without manually chaining GUIDs at high token cost. Unity Insight aims to give LLM agents direct, bidirectional access to these code–asset relationships instead.

**Breakthrough (≤3 sentences):** The authors report the index-backed agent used 53.4% fewer total tokens (5M → 2.3M) and 51.6% less wall-clock time (3,363s → 1,626s) than a general-purpose exploration agent, with 23 of 28 questions favoring the index at statistical significance (p=0.0009). A cited example animation-related query dropped from 194.5K tokens/176s to 38.9K tokens/10.4s.

**Tools & method (≤3 sentences):** The system builds a persistent SQLite index that crawls and parses Unity components, resolving GUID↔path mappings between C# source and serialized assets, and exposes five typed query tools (vfs_ls, vfs_glob, vfs_grep, vfs_read, vfs_refs) for agents to traverse references instead of grepping raw GUIDs. Hardware/compute for building or querying the index is not specified in the paper.

**Limitation (≤3 sentences):** The authors state the index "deliberately does not capture runtime or editor state" and represents only a static snapshot, with disclosed blind spots such as string-based `Resources.Load` dynamic loads. No mechanical correctness grading of agent outputs was reported.

## The Past Frames the Future: Memory for Autoregressive Video Generation
- **arXiv:** 2609.28466 · https://arxiv.org/abs/2609.28466
- **Submitted:** 2026-09-23
- **Authors:** Harold Haodong Chen, Rongjin Guo, Disen Lan, Wen-Jie Shu, Hongfei Zhang, Hanzhe Hu, Shengtao Yao, Zixin Zhang, Guibin Zhang, Zhefan Rao, Jinxiu Liu, Yexin Liu, Rui Peng, Yuhao Liu, Bin Ren, Shuai Yang, Yukang Chen, Salman Khan, Ying-Cong Chen, Ser-Nam Lim, Rynson W.H. Lau, Nicu Sebe, Yu Cheng, Ming-Hsuan Yang, Qifeng Chen
- **Qualifying affiliation(s):** NVIDIA — Ser-Nam Lim, per the paper's affiliation list (HKUST, CityUHK, FDU, ZODA, CMU, NYU, HKUST(GZ), NUS, Georgia Tech, PKU, MBZUAI, NVIDIA, UCF, UNITN, NTU, UC Merced)
- **Categories:** cs.CV
- **Open release:** none stated (the authors reference an accompanying GitHub repository tracking related literature, not code/weights for a model of their own)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** This is a survey/framework paper (not an empirical model paper) organizing how autoregressive video generators maintain memory of past frames — entity identities, spatial layout, dynamics — under bounded context windows, covering discrete-token, diffusion, flow, and Transformer-based generators, including long-horizon and interactive world modeling. It introduces no new benchmark results of its own.

**Purpose (≤3 sentences):** The authors argue that as generated video sequences expand, models cannot retain full history due to context-window limits, so historical information can become inaccessible before its relevance to the current frame has passed; the paper aims to systematize how existing work addresses this rather than propose a new method.

**Breakthrough (≤3 sentences):** The authors propose a five-perspective taxonomy — memory forms (visual/pixel-VAE, implicit state, explicit state, adaptive parametric), functions (identity, spatial, dynamic, semantic, causal), operations (query, retrieval, integration, writing, updating), learning objectives, and evaluation protocols — and define memory as "persistent representation of past observations maintained across autoregressive steps and systematically conditioning subsequent generation."

**Tools & method (≤3 sentences):** As a survey, the paper's "method" is its taxonomy construction and literature organization rather than an experimental pipeline; it reports no datasets, quantitative benchmarks, or hardware/compute of its own.

**Limitation (≤3 sentences):** The authors identify open challenges they did not solve: composable and resource-aware memory architectures, trustworthy state-updating mechanisms, self-rollout learning under distribution shift, and standardized evaluation protocols that isolate memory effects from general video quality. They state "effective memory transcends mere capacity" — retained states must also remain accurate, accessible, and causally influential.

## Learn2Splat: Extending the Horizon of Learned 3DGS Optimization
- **arXiv:** 2605.15760 · https://arxiv.org/abs/2605.15760
- **Submitted:** 2026-05-15
- **Authors:** Naama Pearl, Stefano Esposito, Haofei Xu, Amit Peleg, Patricia Gschoßmann, Lorenzo Porzi, Peter Kontschieder, Gerard Pons-Moll, Andreas Geiger
- **Qualifying affiliation(s):** Meta — Haofei Xu, Lorenzo Porzi, Peter Kontschieder listed at "Meta Reality Labs"; other authors list University of Tübingen / Tübingen AI Center and ETH Zurich
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Learn2Splat, a learned optimizer for 3D Gaussian Splatting (3DGS) that replaces manually-scheduled optimizers like Adam, targeting the problem that prior learned optimizers for 3DGS degrade once training runs beyond their training horizon.

**Purpose (≤3 sentences):** Standard 3DGS optimization requires thousands of hand-tuned iterations per scene; the authors aim for a learned optimizer that remains stable across arbitrarily extended optimization horizons without manual learning-rate scheduling and that generalizes zero-shot to new scenes.

**Breakthrough (≤3 sentences):** The authors report Learn2Splat achieves the highest PSNR of the compared methods on all eight tested benchmarks (DL3DV, DTU, LLFF, Mip-NeRF360, RealEstate10K) within a fixed runtime budget, outperforming Adam by 0.1–1.7 dB on dense-view settings and outperforming second-order methods (LMRS, 3DGS-LM) by 0.3 dB while using half the memory, despite running roughly 2x slower per iteration.

**Tools & method (≤3 sentences):** The method combines a meta-training scheme (a checkpoint buffer plus an optimizer-rollout strategy exposing the network to diverse training phases) with a kNN-based Point Transformer architecture and a "State Scale MLP" that encodes gradient-magnitude information, trained with rendering loss plus low-visibility and stability losses. Training used 4 NVIDIA A100 (40GB) GPUs for 150,000 meta-iterations over about 3 days with mixed precision.

**Limitation (≤3 sentences):** The authors state that in complex scenes the learned optimizer can saturate early due to overly conservative updates, causing Adam to catch up under longer horizons; they propose explicit view-awareness and per-parameter-group adaptive scaling, plus learnable densification/pruning, as future work.

## ReCoSplat: Online Feed-Forward Gaussian Splatting via Render-and-Compare
- **arXiv:** 2603.09968 · https://arxiv.org/abs/2603.09968
- **Submitted:** 2026-03-10
- **Authors:** Freeman Cheng, Botao Ye, Xueting Li, Junqi You, Fangneng Zhan, Ming-Hsuan Yang
- **Qualifying affiliation(s):** NVIDIA — Botao Ye, also listed at ETH Zürich; other authors list UC Merced, Shanghai Jiao Tong University, and HKUST
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses online (causal, streaming) novel view synthesis, where a system must build a renderable 3D Gaussian scene incrementally from sequential images without access to future frames, and must handle a "pose distribution mismatch" between ground-truth poses used in training and predicted poses used at inference.

**Purpose (≤3 sentences):** Existing 3DGS reconstruction methods largely assume all images are available offline; the authors aim for a feed-forward, causal method that reconstructs and renders scenes on the fly from a live image stream while staying robust to imperfect predicted camera poses.

**Breakthrough (≤3 sentences):** The authors report on DL3DV (256 views, posed+calibrated) 22.003 PSNR / 0.751 SSIM / 0.202 LPIPS, approaching offline YoNoSplat's 21.549 PSNR while outperforming online baselines (OF3GS, S3PO-GS, a KV-cache variant); for camera pose estimation on the same setting they report 0.709 AUC at a 5° threshold, and processing throughput of 45.1 FPS average (41.1 FPS at end-of-stream) with peak memory under 12 GiB versus 41 GiB for an offline baseline.

**Tools & method (≤3 sentences):** The method's Render-and-Compare (ReCo) module renders the accumulated Gaussian scene from each incoming image's viewpoint and compares it to the real observation to condition local Gaussian prediction; a causal backbone processes image chunks with alternating-attention transformers, and a hybrid KV-cache compression (early-layer truncation plus selective context retention) cuts cache size by over 90% for 100+ frame sequences. Training used 8× A6000 (48GB) GPUs, inference throughput was measured on an RTX 6000 Ada, and brief high-resolution experiments used an H100 (80GB); evaluation datasets included DL3DV-10K (9,894 train / 140 test), ScanNet++, RealEstate10K, ACID, and ScanNet.

**Limitation (≤3 sentences):** The authors acknowledge that while the Render-and-Compare module helps bridge the pose distribution mismatch, "reconstruction quality in unposed settings cannot be fully independent of pose estimation accuracy," and large pose errors can still propagate to Gaussian assembly and degrade rendering fidelity.

# Near-misses
- 2609.27656 · InternW0: A Foundational Physical World Model for Efficient Real-World Interactions · off-topic — a robotics/embodied-AI world model for real-world robot manipulation (evaluated on tasks like metal-organic-framework synthesis and pipetting), not a game/3D/character-animation/engine application; company match was a "borderline" list hit, not independently verified given the topic drop.
- 2609.28258 · Generalizable Robotic Insertion with World Models · off-topic — despite an NVIDIA co-author, this applies "world models" to industrial robotic insertion tasks, not game or interactive-media world modeling.
- 2609.27621 · SHRAV: State-Hypothesis-Reason-Action-Verify Framework for Physical Modeling and Inverse Design · off-topic — physical/inverse-design modeling (engineering/materials), not 3D, world models (game sense), character animation, or game engines; Google company match not pursued given topic mismatch.
- 2609.27650 · Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond · off-topic — brain-computer-interface/neuroscience survey; Google match not pursued.
- 2609.26854 · SsgCaps: A controlled dataset for the evaluation of sound scene generation algorithms · off-topic — audio/sound-scene generation, not a tracked topic; Google match not pursued.
- 2609.27560 · When Visual Quality Misleads: Intent Recognition under Rendered Avatar Distortions · purely academic — all three authors affiliated with National Chengchi University and National Yang Ming Chiao Tung University (Taiwan); the "Adobe" screen match did not correspond to an author affiliation.
- 2603.11298 · InstantHDR: Single-forward Gaussian Splatting Initialization for HDR 3D Reconstruction · purely academic — authors affiliated with Johns Hopkins University and Shenzhen University; the "Meta" screen match was a false positive from the abstract's phrase "a meta-network for generalizable scene-specific tone mapping," not an author affiliation.

Verification: each of the four qualifying papers' arXiv abstract page (v1 submission date, title, authors, categories, no withdrawal notice) and HTML page (author affiliation block, confirming the qualifying company) were fetched and cross-checked directly against the primary source; a second read of each HTML page's method/results/limitations sections was done to populate the five objective blocks above. This is the double-verification pass for today's run.
