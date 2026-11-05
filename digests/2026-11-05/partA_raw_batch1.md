## Motion-guided Contrastive Regularization For Latent World Models
- **arXiv:** 2611.06901 · https://arxiv.org/abs/2611.06901
- **Submitted:** 2026-11-04
- **Authors:** Yiwen Chen, Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Huaizu Jiang, Amir Said
- **Qualifying affiliation(s):** Qualcomm AI Research — Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Amir Said (Yiwen Chen and Huaizu Jiang are at Northeastern University; a footnote states the work was done during an internship at Qualcomm)
- **Categories:** cs.CV
- **Open release:** none (paper mentions a "video demo" but gives no URL; no code/weights link found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies JEPA-style latent world models, which learn action-conditioned dynamics without reconstructing observations, and identifies a failure mode it calls "static collapse," where the encoder keeps episode-specific background content and drops manipulation-relevant state changes. It shows randomized backgrounds degrade planning on OGBench-Cube. It proposes motion-guided contrastive regularization, which uses optical-flow similarity to weight contrastive targets among transitions from the same episode.
**Purpose (≤3 sentences):** The authors address the gap between good reconstruction-free world-model representations and robust downstream planning when visual backgrounds vary, a setting where existing latent world models lose task-relevant signal.
**Breakthrough (≤3 sentences):** Combined with latent prediction and SIGReg, the authors report planning success rising from 52% to 78% on OGBench-Cube with randomized backgrounds and from 14% to 54% on LIBERO-Object, over the LeWorldModel baseline, while staying comparable on four other visual-control benchmarks.
**Tools & method (≤3 sentences):** The method builds on the LeWorldModel JEPA-style architecture and is evaluated on OGBench-Cube and LIBERO-Object plus four other visual-control benchmarks, using optical-flow-derived similarity to weight contrastive targets from the same episode.
**Limitation (≤3 sentences):** The authors state the method depends on sufficient action coverage and is sensitive to shifts in action representations and visual appearance (e.g., rendering-engine changes). It assumes static backgrounds, since background motion "could distort the optical-flow similarities used for supervision," and on LIBERO-Object a frozen pretrained-encoder baseline (DINO-WM) still reaches higher success (68%).

---

## RDT-3D: Resolution-Decoupled Training for High-Fidelity 3D Geometry Generation
- **arXiv:** 2611.06141 · https://arxiv.org/abs/2611.06141
- **Submitted:** 2026-11-04
- **Authors:** Jiale Zhang, Yang Liu, Chengyang Li, Jin Yuan, Qianxi Jia, Taicheng Huang
- **Qualifying affiliation(s):** JD.com, Beijing, China — all listed authors (single affiliation block for the whole author group)
- **Categories:** cs.CV
- **Open release:** none yet (the authors say they "will open-source Dual3D-300K," but give no link)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper targets high-fidelity 3D geometry generation, which needs both global structural coherence and fine surface detail. It identifies a training-inference resolution mismatch in coarse-to-fine frameworks that use Rotary Position Embeddings (RoPE): training aligns coordinate guidance with geometric supervision, but inference decodes high-resolution geometry from coarse coordinates, causing a distribution shift that degrades fine detail. It proposes Resolution-Decoupled Training (RDT) to address this.
**Purpose (≤3 sentences):** The authors aim to fix oversmoothed thin structures and rounded sharp edges that they attribute to the resolution mismatch in existing coarse-to-fine 3D generation pipelines.
**Breakthrough (≤3 sentences):** RDT anchors RoPE guidance at 512 resolution while supervising geometry at 1536 resolution; the authors report this substantially improves sharp geometric regions. They also introduce Dual3D-300K, a dataset of 300K watertight 3D point-cloud pairs aligned across 512³ and 1536³ resolutions, which they position as a scalable benchmark for high-resolution 3D generation.
**Tools & method (≤3 sentences):** Training used the Dual3D-300K dataset (coarse/fine coordinate-aligned point clouds and rendered images) with AdamW, learning rate 1e-5, bfloat16 precision, batch size 64, 300k training steps, and 10,240 latent tokens; the paper states training ran on 88 NVIDIA B200 GPUs (figure may contain a typo for 8).
**Limitation (≤3 sentences):** The paper has no dedicated limitations section. It notes a quality-versus-efficiency trade-off in the choice of 512 coarse guidance resolution, and that using coarse meshes from upstream models directly for training "introduces excessive noise and severe structural divergence from ground-truth targets," which is why they instead train on low-resolution ground-truth meshes.

---

## ReactWorld: Structuring Interaction Responses for Embodied Video Generation
- **arXiv:** 2611.06120 · https://arxiv.org/abs/2611.06120
- **Submitted:** 2026-11-04
- **Authors:** Hanwei Liu, Huijia Zhang, Hanzhang Wang, Guangyu Liu, Hanbei Zhan, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang
- **Qualifying affiliation(s):** Huawei Technologies Co., Ltd. — Hanwei Liu, Huijia Zhang, Hanzhang Wang, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang (remaining authors: Tongji University / Zhejiang University, per paper's author block)
- **Categories:** cs.CV (primary), cs.RO
- **Open release:** none (project page only, no code/weights found) — https://metaengine-world.github.io/ReactWorld/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Embodied video world models can predict scene changes from robot actions, but the paper argues generated object responses may not match task intent or contact dynamics. It introduces ReactWorld, which uses chain-of-thought-inspired interaction anticipation: an interaction response field predictor estimates participant roles, future motion intensity, and local motion changes, and a response feedback adapter updates object features and biases temporal attention using predicted displacements.
**Purpose (≤3 sentences):** The authors target embodied video generation where object/environment reactions to a robot's actions must be physically and semantically plausible, not just visually coherent.
**Breakthrough (≤3 sentences):** The authors report an average score of 77.51 on RBench, 3.29 points above the PhysisForcing baseline with gains in all nine categories, and a Domain score of 86.98 and average of 81.87 on EZS-Bench.
**Tools & method (≤3 sentences):** The method is built on a frozen Wan2.2-I2V-A14B backbone, fine-tuned with rank-32 video LoRA (AdamW, lr 1e-5, effective batch size 32) on 8 H100 GPUs in BF16, using about 500K clips from AgiBot, RoVid-X, and internet robot videos; Qwen3-VL and SAM3/CoWTracker are used for role annotation and object/trajectory extraction, and Qwen3-VL/Qwen2.5-VL serve as RBench/EZS-Bench evaluators.
**Limitation (≤3 sentences):** The authors state that "ReactWorld currently anticipates interactions using a 2D response representation," leaving 3D interaction relations unmodeled, and name exploring temporally consistent 3D motion representations as future work.

# Near-misses
- 2611.06908 · Perceptive Humanoid Motion from Simulation (HALO) · off-topic: humanoid robot locomotion/manipulation learned via sim-to-real transfer (cs.RO), not 3D generation/world-model/character-animation/game-engine research, despite confirmed Apple affiliation
- 2611.06796 · VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation · purely academic, no industry co-author (PDF title page lists only Hong Kong University of Science and Technology and The Chinese University of Hong Kong, Shenzhen)
- 2611.06781 · Semantic Residual Vector Quantization for Sign Language Generation · purely academic, no industry co-author (University of Trento and Fondazione Bruno Kessler only)
- 2611.06061 · TouchéWorld tech report: Towards Online Unified Camera-Hand Exploration in Generative World Models · purely academic, no industry co-author (East China Normal University, Sorbonne Paris Nord/LIPN/CNRS, Université Paris Cité/LLF/CNRS, Dalian Jiaotong University); the screen's "Google" flag was a false positive (no Google affiliation found in the author block)
- 2611.05893 · Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring · off-topic: identity-preserving talking/acting video generation for a media challenge, not 3D/world-model/character-animation(motion)/game-engine research, despite confirmed Huawei Inc. co-authors (Xiaoxiao Sheng, Tianyu Huang)
- 2611.05825 · DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation · off-topic: digital-human e-commerce marketing video generation, not 3D/world-model/character-animation/game-engine research, despite confirmed Ant Group co-authors

Verification pass: each of the 9 leads was checked against its arXiv abstract page (v1 date, categories, withdrawal status) and HTML/PDF author block (real affiliations, not text/keyword matches) on 2026-11-05. All 9 carried a v1 date of 2026-11-04, within the 2026-10-06–2026-11-05 window, and none were withdrawn.
