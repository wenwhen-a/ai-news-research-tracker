## UNITE: Consolidating Embodied VLM Specialists via Shared-Anchor One-Bit Factorization
- **arXiv:** 2611.20767 · https://arxiv.org/abs/2611.20767
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Tao Tao, Anke Tang, Enneng Yang, Zhi Hou, Xiaogang Wang, Dacheng Tao
- **Qualifying affiliation(s):** ACE Robotics, Shanghai — Tao Tao, Zhi Hou, Xiaogang Wang. FLAG: borderline — ACE Robotics (not on the explicit qualified-company list; standing unclear, kept per borderline rule). Other authors: Sichuan University, Nanyang Technological University, Sun Yat-sen University (Shenzhen).
- **Categories:** cs.LG (primary), cs.CV
- **Open release:** none (no GitHub/HuggingFace/project page found in abstract or HTML body)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** UNITE consolidates multiple fine-tuned vision-language-model (VLM) "specialists" — for visual grounding, spatial reasoning, navigation, and driving understanding — into a single compact mixture-of-experts model instead of deploying them separately or merging them into one conflict-prone dense model. It keeps each specialist's feed-forward block as a routable expert, compressed via a shared floating-point "anchor" plus per-expert binary deviations, and adapts only the router. Built from four Qwen3-VL-8B specialists, it is evaluated on 22 benchmarks plus R2R Val-Unseen navigation.

**Purpose (≤3 sentences):** The authors aim to avoid the storage cost of deploying many separate embodied VLM specialists while avoiding the capability loss and parameter conflicts that come from naively merging them into a single dense model. UNITE targets near-single-model storage while retaining each specialist's expertise.

**Breakthrough (≤3 sentences):** The authors report the full UNITE model occupies 20.3 GB — 1.16× the storage of one dense specialist and 59.6% below the uncompressed mixture-of-experts — while updating fewer than 0.6M router parameters (under 0.01% of the 8.8B active parameters), using only source weights with no calibration data. They report it matches six static merging methods in mean retention of best-specialist performance, leads all of them on Scan2Cap, ScanQA, and all four navigation metrics (up to +19.1 on Scan2Cap over the best source specialist), and is nearly lossless relative to the uncompressed MoE on 21 of 22 benchmarks.

**Tools & method (≤3 sentences):** UNITE represents the expert bank through a "shared-anchor one-bit factorization" — a shared floating-point anchor plus expert-specific, row-scaled binary deviations — optimized jointly via closed-form alternating updates with no calibration data, then adapts only token-level routing with the backbone and experts frozen.

**Limitation (≤3 sentences):** The authors report one clear exception to otherwise near-lossless compression: on VSI-Bench, frame-count experiments suggest the factorized model has impaired use of cross-frame evidence compared to the uncompressed mixture-of-experts.

## BlockAlign: Preference Optimization for Trajectory-Distilled Video Generation
- **arXiv:** 2611.20351 · https://arxiv.org/abs/2611.20351
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Jingyuan Zhu, Biaolong Chen, Yangyang Qin, Shengyang Shen, Yaohua Wang, Weiming Bai, Miao Lu, Aixi Zhang
- **Qualifying affiliation(s):** Alibaba Group — all eight authors (contact emails on alibaba-inc.com domain).
- **Categories:** cs.CV
- **Open release:** none (no GitHub/HuggingFace/project page found in abstract or HTML body)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** BlockAlign is a preference-optimization framework for aligning few-step, "trajectory-distilled" video generators (e.g., Parallel Decoding Distillation and Parametric Trajectory Distillation models) without teacher fine-tuning or re-distillation. It fixes a mismatch between standard flow-matching preference objectives, which assume single-head local velocity supervision, and the finite-interval, block-average transition interface these distilled generators actually use. The authors test it on multi-reference video generation using Alibaba's in-house RefVid-V4 model and the MiniMax-H3 Ref2VA model.

**Purpose (≤3 sentences):** The goal is to directly align deployed few-step video generators on their native sampling interface — cutting rollout costs relative to full-trajectory alignment — rather than naively supervising only the primary velocity sub-head, which the authors show induces a training-inference mismatch (their "DirectAlign" baseline) that degrades quality below the unaligned model.

**Breakthrough (≤3 sentences):** The authors report BlockAlign unlocks the underlying distilled model's (PDD) 5x few-step rollout speedup, yielding 3x faster end-to-end online training, and achieves statistically significant human-preference wins over PDD baselines (54.0% vs. 33.3% wins/losses, a 61.8% non-tie win rate, on RefVid-V4; 51.3% vs. 34.7%, a 59.7% non-tie win rate, on MiniMax-H3). They also report up to an 82.7% win rate against the naive DirectAlign approach.

**Tools & method (≤3 sentences):** BlockAlign constructs states at valid block boundaries and supervises "span-normalized transition residuals" against the fused block-level velocity predictor, supporting DPO-, NFT-, and rollout-style objectives while preserving the native few-step sampler. It is paired with a post-training pipeline combining offline preference pairs, reward-free semi-online continuations, and online rollouts, with hierarchical preference selection and objective-aware block scheduling.

**Limitation (≤3 sentences):** The authors note the method's cross-block guidance is only an "empirical approximation" that broadcasts a guidance direction across blocks without achieving exact multi-block credit assignment, and that an ablation on their scheduling choice was statistically inconclusive (p = 0.0709, confidence intervals including parity). They also report BlockAlign's automated aesthetic score (GPT-4o NaturalScore) came out slightly lower than baselines', which they partly attribute to baselines' stronger commercial-style aesthetics rather than a genuine quality deficit.

# Near-misses
- 2611.20950 · ROSE: A Shared Cross-Embodiment Facial-Motion Latent Space for Humanoid Robot Expression · no industry co-author (University of Bristol, China University of Mining and Technology, Cardiff University, Bristol Robotics Laboratory, and small firm Intelliface — none on or comparable to the qualified-company list); also physical humanoid-robot hardware work, not game/virtual character animation
- 2611.20899 · SciWorldBench: Do Video World Models Really Understand Scientific Experiments? · no industry co-author (Peking University, with an NTU visiting affiliation)
- 2611.20888 · Driving the Style: Velocity-Conditioned Whole-Body Control from Motion Demonstrations · no industry co-author (Agile Robots SE and a small China-based innovation center, neither on/comparable to the qualified list); off-topic despite keyword match — physical humanoid-robot locomotion control, not character animation
- 2611.20791 · QTOP: Scaling Humanoid Motion Tracking with Quantile Critics · off-topic despite keyword match — physical humanoid-robot whole-body control/sim-to-real RL (Qualcomm AI Research authors, but the paper is robotics hardware control, not game/virtual character animation)
- 2611.20788 · VA-Assembly: View-Aligned Score Guidance for Training-Free 3D Part Assembly · no industry co-author (Yonsei University only)
- 2611.20704 · QASK-Edit: Adaptive Sparse Attention Across Queries and Key Sources for Efficient Video Editing · no industry co-author (Sun Yat-sen University only)
- 2611.20703 · Efficient Multi-View Generation with Iterative Global-Local Proxy Attention · no industry co-author (Southeast University, HKUST, Southwest University, Chinese Academy of Sciences, University of Surrey)
- 2611.20546 · A Gaussian Primitive Data Management Framework for Efficient 3DGS Trajectory Rendering · no industry co-author (HKUST(GZ), Soochow University, HKUST)
- 2611.20452 · XMimic and XSoma: Learning Humanoid Motion Tracking and Locomotion in Under a Minute · no industry co-author (TU Darmstadt, DFKI, hessian.AI only); also off-topic — physical humanoid-robot control, not character animation
- 2611.20107 · SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving · no industry co-author (Purdue University, University of Wisconsin–Madison only)
- 2611.20090 · Latent World Modeling for Point-Cloud Video Pretraining · no industry co-author (Xi'an Jiaotong University, Hunan University, University of Western Australia)
- 2611.20076 · SGIP: Learning Scene-Grounded Interaction Priors for Scene-Aware Human Motion Prediction · no industry co-author (DGIST and UNIVA only)
- 2611.19998 · MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams · off-topic despite keyword match — physical humanoid-robot teleoperation/control (University of Hong Kong, NUS, Beijing Institute of Technology, and small firm EngineAI — none on/comparable to the qualified list), not game/virtual character animation
