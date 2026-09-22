## WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory
- **arXiv:** 2609.24984 · https://arxiv.org/abs/2609.24984
- **Submitted:** 2026-09-21
- **Authors:** Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan
- **Qualifying affiliation(s):** Tencent — Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan (ARC Lab, Tencent IEG); other authors are Peking University
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none confirmed in text beyond a project website (https://drexubery.github.io/WorldCrafter); no explicit code/weights link found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldCrafter is a video world model that maintains long-horizon and multi-view consistency using an implicit, camera-queryable 3D-aware memory. It compresses historical multi-view evidence into a fixed token budget shaped by the requested viewpoint, avoiding explicit depth correspondence. It supports streaming scene exploration from a single image or text prompt.

**Purpose (≤3 sentences):** The authors aim to solve the consistency problem in video world models — i.e., maintaining coherent scene content when a camera revisits previously seen viewpoints during long, interactive generation. They target minute-scale, camera-controllable exploration from a single input.

**Breakthrough (≤3 sentences):** The authors report a memory encoder with pose-conditioned readout that integrates historical observations into denoising without explicit depth correspondences, and claim a "47.6% improvement relative to the strongest baseline" in revisit consistency. They also report real-time inference via distillation enabling minute-scale streaming exploration.

**Tools & method (≤3 sentences):** Training combines Open-Sora-Plan, DL3DV, and MIND synthetic datasets across four sequential training stages (~19,000 iterations) using up to 32 GPUs. The pipeline pairs an implicit 3D-aware memory encoder with a camera-controllable autoregressive video generator.

**Limitation (≤3 sentences):** The authors acknowledge that consistency can still break down along particularly complex or extended trajectories. They also note added latency from re-encoding history at each generation step, and propose autoregressive streaming as future work.

## GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay
- **arXiv:** 2609.25001 · https://arxiv.org/abs/2609.25001
- **Submitted:** 2026-09-21
- **Authors:** Yiran Wang, Xingyilang Yin, Junfu Pu, Guangzhi Wang, Kaifeng Li, Mingyu Ouyang, Huiqiang Sun, Lingen Li, Cheng Cheng, Wangbo Yu, Honghao Chen, Xiaodong Cun, Chi-Man Pun, Zhiguo Cao, Ying Shan
- **Qualifying affiliation(s):** Tencent — ARC Lab, Tencent (majority of authors, including Ying Shan); other affiliations include Great Bay University, University of Macau, National University of Singapore, HUST, MMLab CUHK
- **Categories:** cs.CV, cs.AI
- **Open release:** code (GitHub: https://github.com/TencentARC/GameHorizon) and project page (https://gamehorizon-suite.github.io); authors state they "will release our dataset, annotator, and benchmark"
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GameHorizon Suite is an evaluation framework for AI game-playing models spanning multiple task horizons. It bundles an automated multi-horizon instruction annotator, a large-scale gameplay dataset, and an offline/online benchmark. It is used to evaluate 47 models on visual comprehension, instruction parsing, planning, and temporal action control.

**Purpose (≤3 sentences):** The authors aim to systematically measure how well current models handle gameplay tasks across short, medium, and long time horizons, an area they argue lacks standardized data and evaluation. They target both static (offline) and interactive (online) assessment.

**Breakthrough (≤3 sentences):** The authors report a dataset of "5,000 hours of recordings from 21 games" with 6,184,036 distinct instructions and 411.03 million keyboard-mouse action events from 100 expert players, plus an offline benchmark of 5,000 multiple-choice questions and an online, stepwise gameplay evaluation. Evaluating 47 models with over one million invocations, they report the suite reveals "a meaningful hierarchy of task difficulty and pronounced differences in model capabilities."

**Tools & method (≤3 sentences):** The suite includes GameHorizon-Annotator (a three-level instruction pyramid pipeline), GameHorizon-Data (4,571 videos at 60fps across 21 AAA titles), and GameHorizon-Bench (offline MCQs plus online resettable gameplay testing). Online testing is implemented for Minecraft due to accessible game state.

**Limitation (≤3 sentences):** The authors acknowledge the online evaluation track is limited to Minecraft because most AAA titles don't expose underlying game state. They also report long-horizon task success remains low (best model at only 45% success), and note dedicated game agents show severe domain dependence with poor zero-shot performance on unseen AAA games.

## UltraTex: Unleashing 2K Multi-View Diffusion for 3D Texturing
- **arXiv:** 2609.23169 · https://arxiv.org/abs/2609.23169
- **Submitted:** 2026-09-19
- **Authors:** Yibo Zhang, Ze Yuan, Nan Cao, Li Zhang, Yan-Pei Cao, Yuan-Chen Guo, Rui Ma
- **Qualifying affiliation(s):** VAST, Beijing — Yan-Pei Cao, Yuan-Chen Guo; FLAG: borderline (VAST is an industry 3D-generation company but not on the confirmed top-tier list; other authors are Jilin University, University of Hong Kong, Tongji University, Fudan University, Shanghai Innovation Institute)
- **Categories:** cs.CV
- **Open release:** code/data at https://yiboz2001.github.io/UltraTex (per paper statement "Code and data is at ...")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** UltraTex is an efficient multi-view diffusion framework for generating high-quality 3D object textures at 2K (2048) resolution. It addresses the token-count explosion that makes high-resolution multi-view diffusion computationally impractical (unified multi-view sequences otherwise exceeding 212K tokens). It combines token dropping, sparse attention, and specialized decoding to make 2K texturing tractable.

**Purpose (≤3 sentences):** The authors aim to overcome the computational limitations that prevent multi-view diffusion texturing methods from operating at high (2K) resolution. They specifically target the inefficiency caused by background redundancy and sparse foreground interactions in object-centric renderings.

**Breakthrough (≤3 sentences):** The authors report three techniques — background token dropping, block-sparse attention over the compressed foreground sequence, and foreground-aware VAE decoding — that together preserve texture quality while cutting cost. They claim "20.6×–91.1× training speedup and 22.3×–74.6× end-to-end inference speedup" compared to baseline methods.

**Tools & method (≤3 sentences):** The team built the G-buffer TexVerse dataset covering over 268,000 3D assets with multi-view renderings up to 4096×4096 resolution. Training used 64 H200 GPUs across three progressive stages over 18 days, built on the pretrained FLUX model.

**Limitation (≤3 sentences):** The authors acknowledge the method may struggle with objects containing highly repetitive texture patterns, and that quality is bounded by the capability of the pretrained FLUX backbone. They also note the VAE encoder-decoder may blur some high-frequency detail, and that pushing to 4K/8K resolution would require redesigning the underlying DiT-VAE foundation models.

# Near-misses
- 2609.24457 · Constrained Program Generation for 3D Reaction Animation with a 0.8B Model | ChemXRG · off-topic (chemistry-reaction visualization tool, not a games/graphics/character-animation/world-model topic); also no HTML version available to verify affiliation
- 2609.24048 · What Matters in Designing World Action Models: An Empirical Study · off-topic — robot-manipulation "world action model" (cs.RO, evaluated on RoboCasa-GR1/LIBERO/DROID robot benchmarks), not a game/visual world model
- 2609.23797 · MoSAT: Human Motion Generation from Spatial Audio and Textual Description · on-topic (character animation) but no qualifying industry co-author — all affiliations are academic (HKU, MIT, UPenn, Brown, Shanghai AI Lab, Macau UST, HKUST, Texas A&M)
- 2609.23184 · CausalWM: Causal Chain-of-Thought Reasoning for Embodied World Model · off-topic — an embodied/robot physical-control world model (forecasts physical dynamics from visual observations + control inputs for embodied agents), not a game/visual world model
- 2609.22816 · FIRM-WM: State-factorized factual-interventional recurrent modeling for reward-free visual planning · off-topic — a generic reward-free RL/robotic planning world model (cs.LG; evaluated on TwoRoom/Reacher/OGBench-Cube robot-style control benchmarks), not games/graphics
