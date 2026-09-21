# Part A — Papers
Window: last 30 days (2026-08-22 to 2026-09-21). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: website fallback (arXiv API returned HTTP 406 on all queries). Qualifying papers: 3 (2 flagged borderline affiliation).

---
## GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development
- **arXiv:** 2609.21293 · https://arxiv.org/abs/2609.21293
- **Submitted:** 2026-09-18
- **Authors:** Xiuhui Zhang, Yi Chen, Shusheng Xu, Fan Li, Huan Wang, Tongkai Yang, Binhang Yuan
- **Qualifying affiliation(s):** Ant Group — Xiuhui Zhang, Yi Chen, Shusheng Xu, Fan Li, Huan Wang, Tongkai Yang, Binhang Yuan (co-affiliated with Beihang University and HKUST for two authors); FLAG: Ant Group is a borderline-listed organization (not on the core tracked list; kept and flagged per policy)
- **Categories:** cs.AI, cs.SE
- **Open release:** code — https://github.com/areal-project/GameASG-Bench
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces GameASG-Bench, a benchmark for evaluating whether AI agents can autonomously generate complete, working browser-based games rather than just individual code components. It defines a pre-declared evaluation interface (reset, loadScenario, input, getSnapshot) so tasks are reproducible and testable, and covers 47 browser-native game tasks across 12 genres (32 2D, 15 3D).
**Purpose (≤3 sentences):** Existing code-generation benchmarks check source-level compliance but not whether the resulting application actually behaves correctly at runtime; the authors argue high structural compliance does not guarantee interactive gameplay logic works. GameASG-Bench is built to close that gap with two-tier checking: L1 (source-level, 336 checks) and L2 (runtime behavior in headless Chromium, 885 checks).
**Breakthrough (≤3 sentences):** The authors report that across nine agent stacks, the highest "strict task success" rate (passing all L1 checks plus applicable L2 P0/P1 checks) was only 55.3% (26/47 tasks, GPT-6-Astra with Codex CLI), despite mean L2 check pass rates of 93.2% for the same model — a gap the authors say shows partial-credit metrics overstate real capability. They also report that restricting tool access cut strict successes roughly in half (18/47 with full tools vs. 6–9 restricted) and that Claude Code and Codex CLI both reached 18/47 but agreed on only 10 of the same tasks.
**Tools & method (≤3 sentences):** Evaluation runs in headless Chromium at a fixed 1280×800 viewport; the benchmark combines tool checks, regex checks, and anti-pattern checks (L1) with P0/P1/P2-tiered runtime checks (L2). The authors report per-task-set costs ranging $0.18–$11.85 and note reference implementations for all 47 tasks pass every applicable check.
**Limitation (≤3 sentences):** The authors state the benchmark excludes concepts requiring backends, user accounts, external databases, paid assets, unbounded multiplayer, or behavior unreachable within bounded browser execution, so it does not test full production game stacks. They also note NOT_APPLICABLE L2 checks are not currently restricted for required P1 checks, a scoring edge case they flag but do not resolve.

---
## Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Pose Tracking
- **arXiv:** 2609.21347 · https://arxiv.org/abs/2609.21347
- **Submitted:** 2026-09-18
- **Authors:** Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang
- **Qualifying affiliation(s):** Ant Group — Xiangfei Guo, Hao Shi (co-affiliated with Zhejiang University; other authors are Zhejiang University only); FLAG: Ant Group is a borderline-listed organization (not on the core tracked list; kept and flagged per policy)
- **Categories:** cs.CV
- **Open release:** code + dataset — https://github.com/guoxf304/CubeSplat (source code and the SynPano dataset)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Cube-Splat, a 3D Gaussian Splatting SLAM system for 360° panoramic cameras, built to overcome the limited field of view of pinhole-camera SLAM pipelines that increases drift in large scenes. It converts each panoramic frame into four fixed-orientation virtual pinhole views sharing one optical center ("cubemap factorization") and tracks pose via an "adjoint-consistent" gradient-aggregation scheme across the four faces.
**Purpose (≤3 sentences):** Most existing 3DGS SLAM pipelines assume pinhole cameras, which the authors say reduces scene coverage and worsens drift; panoramic imagery is harder to integrate into a single coherent pose because observations from different directions must stay geometrically consistent. Cube-Splat is designed to combine panoramic coverage with the rendering quality of Gaussian Splatting mapping.
**Breakthrough (≤3 sentences):** On the PALVIO indoor benchmark, the authors report a tracking error (ATE) of 0.0769 m versus 2.23 m (Photo-SLAM), 2.89 m (MonoGS), and 1.93 m (S3PO-GS); on their new outdoor SynPano benchmark, Cube-Splat reaches 0.1058 m ATE while S3PO-GS fails to track. They also report higher rendering quality on SynPano indoor scenes (33.56 dB PSNR vs. 32.27 dB for S3PO-GS and 28.92 dB for MonoGS).
**Tools & method (≤3 sentences):** The system runs on a single NVIDIA RTX 4070 Ti SUPER GPU in PyTorch on Ubuntu 22.04, processing at roughly 1.53 FPS (12.8 ms/iteration, ~35 tracking iterations per frame). The authors introduce SynPano, a new synthetic benchmark of 10 sequences (5 indoor, 5 outdoor) rendered in Blender's Cycles engine with parameterized 6DoF trajectories and multi-modal ground truth, alongside the existing PALVIO and OmniBlender datasets. The paper is accepted to ECCV 2026.
**Limitation (≤3 sentences):** The paper's provided content does not include an explicit stated-limitations section; the authors' ablation study shows performance depends on sufficient optimization iterations and multi-face observations, with baseline methods degrading more sharply than Cube-Splat under reduced iterations (observed, not stated as a limitation by the authors).

---
## GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression
- **arXiv:** 2609.21576 · https://arxiv.org/abs/2609.21576
- **Submitted:** 2026-09-18
- **Authors:** Pinxin Liu, Haiyang Liu, Jiahao Luo, Junhua Huang, Chunhao Zou, Luchuan Song
- **Qualifying affiliation(s):** Meta — one author (exact name-to-affiliation mapping not resolvable from the rendered HTML; the paper lists five institutions — University of Rochester, University of Tokyo, UC Santa Cruz, UCLA, Meta — against six authors without a clear footnote pairing in the fetched content)
- **Categories:** cs.CV, cs.GR, cs.HC
- **Open release:** demo — https://andypinxinliu.github.io/GestureFAR (project page; no code/GitHub link found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GestureFAR is a streaming co-speech gesture generation system that produces body motion for conversational agents in real time, using continuous (not discretized) motion latents to avoid the "representation ceiling" the authors say discrete tokenization imposes. It combines a causal continuous-motion VAE tokenizer, a causal audio-motion transformer, and a flow-matching head that samples each next motion latent autoregressively.
**Purpose (≤3 sentences):** The authors state that streaming gesture generation must be strictly causal — using only past motion and currently available speech — while prior discrete-token systems trade away motion expressiveness for streamability. GestureFAR is designed to keep continuous, expressive motion representation while still supporting real-time, token-causal generation.
**Breakthrough (≤3 sentences):** On the BEAT2 benchmark (speaker-22 split), the authors report their one-step distilled student model reaches FGD 3.08 versus 4.57 for LiveGesture and 8.06 for MIBURI (ground truth FGD is 0.703); on Audio2PhotoReal they report FGD 2.08, best among compared methods. They also report a real-time factor of 0.246 on a MacBook Air (about 4.1× faster than real-time) after distillation, versus 24.4 ms/token for the 88-step teacher model.
**Tools & method (≤3 sentences):** The tokenizer is a 1D causal VAE (128-dim latent, stride 4); the transformer is 8 layers (hidden size 384, 6 attention heads) with a lightweight MLP flow head (6.51M parameters). The authors introduce "Multi-Procedure Distribution Matching Distillation" to compress the flow head to one-step sampling, reporting head-only distillation takes ~10 minutes versus 4 hours for whole-model distillation and 8 hours for teacher training; training/evaluation data is BEAT2 (~6,060 hours of SMPL-X motion and speech from 2,525 speakers, 17,621 clips).
**Limitation (≤3 sentences):** The authors do not provide a formal limitations section in the fetched content. Their own ablations show the discrete consistency warm-up objective alone is insufficient (FGD 0.570 vs. 0.308 combined with other objectives), and they note diffusion-forcing alternatives underperform their approach, suggesting narrower generalization to other motion-generation paradigms (observed, not stated).

# Near-misses
- 2609.21787 · Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models · no HTML version available (404), affiliation unverifiable via PDF-free process; abs-page "Google" match unconfirmed (likely a citation/scholar-link false positive)
- 2605.26880 · GScomp-QA: A Subjective Dataset for Quality Assessment of Compressed Gaussian Splatting · out of window (v1 submitted 2026-05-26, before the 2026-08-22 cutoff); Google affiliation also unconfirmed on fetched pages
- 2604.23692 · Personalizing Causal Audio-Driven Facial Motion via Dynamic Multi-modal Retrieval · out of window (v1 submitted 2026-04-26, before cutoff); Meta affiliation unconfirmed on fetched pages
- 2609.21799 · Comparing Hand and Controller Avatars with Hand Tracking and Controller-Based Interaction · academic-only affiliation confirmed (Carleton University, Monash University); no qualifying industry co-author — the screening "Meta" match was a false positive
- 2609.21112 · Demonstration Synthesis from a Single Scan via Gaussian Splatting for Visuomotor Policy Learning (GaussianFactory) · academic-only affiliation confirmed (George Mason University, New York University); no qualifying industry co-author — the screening "Google, Microsoft" match was a false positive
- 2609.21107 · Learning Scene-Aware Humanoid Locomotion through 3D Clutter from Immersive Human Demonstrations (MTC) · academic-only affiliation confirmed (George Mason University, New York University); no qualifying industry co-author — the screening "Google, Microsoft" match was a false positive
- 2609.21897 · Multi-Resolution Wire-Fencing for Efficient Path Sampling · off-topic (molecular dynamics / protein-ligand simulation, cond-mat.stat-mech); screening "Google" match was a false positive, dropped without further verification
- 2609.21965 · The ecological collapse of color: photoreceptor number buys a geometric hue manifold · off-topic (vision/color science); screening "Amazon" match was a false positive (unrelated to Amazon.com), dropped without further verification
- 2504.15776 · Refining Ground Truth Poses in Autonomous Driving Datasets via Neural Rendering · out of window (v1 submitted April 2025); also only tangentially on-topic (autonomous-driving dataset tooling), dropped without further verification

Double-verification pass: each of the 3 qualifying papers above was checked against its arXiv abstract page (submission date, categories, comments/code links) and its arXiv HTML rendering (author affiliation block, abstract, method, and results text) before inclusion; all near-misses were checked against at least the abstract page and, where an HTML page existed, the affiliation block.
