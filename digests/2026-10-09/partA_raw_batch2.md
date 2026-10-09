Part A raw verification — batch 2 (lead IDs, company-name-regex matches)
Verified 2026-10-09. Leads checked: 12. Qualifying: 8. Near-misses: 4.

---

## Phase-aware video generation for physics-grounded dynamics and interactions (PAVG)
- **arXiv:** 2610.11791 · https://arxiv.org/abs/2610.11791
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Jingfeng Ou, Kun Wang, Rui Zhao, Jingwei Guan, Limin Wang, Chao Dong, Xingyu Zeng
- **Qualifying affiliation(s):** SenseTime — Kun Wang, Rui Zhao (flag: SenseTime is not on the default list but is a large, publicly listed Chinese AI company comparable to the tracked tier; kept and flagged). Other authors: Nanjing University, Shenzhen University of Advanced Technology (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper targets physically plausible video generation for scenes where solids and gases behave differently but interact (e.g., smoke, fire, water with solid objects). The authors propose PAVG, a phase-aware generator with a dual-branch architecture that models solid and gas dynamics separately.
**Purpose (≤3 sentences):** To overcome the limits of single-branch video generators that cannot represent the distinct dynamics of solids versus gases within one interacting scene.
**Breakthrough (≤3 sentences, attributed):** The authors report that PAVG improves motion adherence, physical plausibility, and visual quality over existing approaches, trained on a purpose-built simulation corpus of over 700K physical trajectories covering solid, gas, and solid-gas interaction scenarios.
**Tools & method (≤3 sentences):** Dual-branch architecture modeling solid and gas dynamics separately, with spatiotemporal cross-attention to capture their interaction; trained on the authors' 700K+-trajectory simulation dataset.
**Limitation (≤3 sentences):** Not stated in the available abstract text; not independently verified beyond the abstract.

---

## PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors
- **arXiv:** 2610.11612 · https://arxiv.org/abs/2610.11612
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Haobo Jiang, Liang Yu, Jianmin Zheng
- **Qualifying affiliation(s):** Alibaba Group — Liang Yu. Other authors: Nanyang Technological University, Singapore (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses registering unordered multiview RGB-D scans into one metrically consistent coordinate frame. It argues the standard pairwise-then-global pipeline suffers from locally optimized matches, error accumulation, and high cost.
**Purpose (≤3 sentences):** To provide a training-free, zero-shot registration method that avoids per-scene optimization and pairwise pose estimation.
**Breakthrough (≤3 sentences, attributed):** The authors report strong zero-shot accuracy and efficiency on indoor, object-centric, and outdoor datasets using a "foundation-then-refinement" two-stage pipeline built on the VGGT visual-geometry foundation model.
**Tools & method (≤3 sentences):** Stage 1 anchors VGGT's scale-ambiguous pose predictions to metric depth to recover global poses without pairwise estimation; Stage 2 uses voxelized spatial hashing for near-linear-time dense correspondence, refined by a motion-only bundle adjustment solved with conjugate gradient.
**Limitation (≤3 sentences):** Not stated in the available abstract text.

---

## Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher
- **arXiv:** 2610.11479 · https://arxiv.org/abs/2610.11479
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Bowen Zheng, Zhiguang Liu, Jiarong Ou, Rui Chen, Tianyang Hu
- **Qualifying affiliation(s):** Tencent Hunyuan — Zhiguang Liu, Jiarong Ou, Rui Chen. Other authors: The Chinese University of Hong Kong, Shenzhen (academic).
- **Categories:** cs.CV (primary); cs.AI, cs.LG (cross-listed)
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies causal (autoregressive) video diffusion models, which suit streaming and long-video generation but typically underperform bidirectional models of the same size. Prior approaches initialize from or distill a pretrained bidirectional teacher; this work trains causal models from an image-model initialization with no bidirectional video model at any stage.
**Purpose (≤3 sentences):** To close the causal-vs-bidirectional performance gap and to curb error compounding caused by a causal model's dependence on its own (possibly erroneous) generated history at inference.
**Breakthrough (≤3 sentences, attributed):** The authors report Conditional Residual Prediction (CRP) nearly closes a 6.14-point gap to a bidirectional model under controlled, matched-setup experiments. Scaled up as "Optica," a 2B-parameter causal model, it generates 5-second 480p video and reaches 82.78 on VBench using about 15M training videos, per the authors.
**Tools & method (≤3 sentences):** CRP has the model predict the target without its conditioning input first, so the condition (e.g., past frames) only supplies a residual, reducing reliance on history for information the present already provides.
**Limitation (≤3 sentences):** Not stated in the available abstract text beyond the reported performance gap.

---

## Learning to Retrieve: Internalizing Memory Retrieval for Video World Models (L2R)
- **arXiv:** 2610.11444 · https://arxiv.org/abs/2610.11444
- **Submitted:** 2026-10-08 (v1)
- **Authors:** JiaKui Hu, Tailai Chen, Yuqi Pan, Xuerui Qiu, Jialun Liu, Xiao Cao, Zhenxin Zhu, Guang Chen, Hangjun Ye, Bing Wang, Yanye Lu
- **Qualifying affiliation(s):** Xiaomi EV — JiaKui Hu, Zhenxin Zhu, Guang Chen, Hangjun Ye, Bing Wang (flag: Xiaomi EV is Xiaomi's electric-vehicle division; Xiaomi is not on the default list but is a comparable large-scale tech company — kept and flagged). Other authors: Peking University, CASIA, University of Queensland, NUS (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Video world models generate explorable, 3D-consistent scene video from camera trajectories, and existing systems use external memory to retrieve earlier content and limit scene drift. The authors note these memory pathways sit outside the model's generative process, so the model cannot learn when or what to retrieve.
**Purpose (≤3 sentences):** To make memory retrieval learnable and internal to the model rather than an external, hand-engineered system.
**Breakthrough (≤3 sentences, attributed):** The authors report that L2R improves long-term scene consistency across several base models and camera-revisit benchmarks, without needing an external memory bank or 3D conditioning.
**Tools & method (≤3 sentences):** L2R treats the model's own persistent internal state as memory; a camera-conditioned retrieval gate selects relevant history, and a retrieval trigger — supervised with a 3D re-visibility signal — decides when to use it, activating only when previously seen content re-enters view.
**Limitation (≤3 sentences):** Not stated in the available abstract text.

---

## IntactWorld: Joint World Modeling with Intact Features
- **arXiv:** 2610.11174 · https://arxiv.org/abs/2610.11174
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Boming Tan, Xiangdong Zhang, Yan Xia, Qi Zhu, Deyi Ji, Xue Yang, Shaofeng Zhang
- **Qualifying affiliation(s):** KOKONI 3D / Moxin Technology — listed as one of the paper's three institutions, but the HTML extraction could not map the superscript to a specific named author (flag: this company's standing as a "clearly comparable top-tier industry lab" could not be confirmed and is less certain than typical borderline cases like Huawei/Samsung — kept and flagged for user judgment). Other authors: University of Science and Technology of China, Shanghai Jiao Tong University (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The authors argue video generation models produce realistic visuals but lack genuine understanding of real-world logic, and that prior methods absorbing "world knowledge" compress features, losing structural information. They propose IntactWorld, a joint world-modeling architecture built on uncompressed features.
**Purpose (≤3 sentences):** To preserve structural detail in world-model features by avoiding the lossy compression used in prior approaches.
**Breakthrough (≤3 sentences, attributed):** The authors report IntactWorld outperforms established baselines by 2.46 points on VBench 2.0; a companion "Full-to-Compact" training paradigm (swapping full features for CLS tokens) cuts spatial memory use by 11.4% and inference latency by 43.8%, per the authors.
**Tools & method (≤3 sentences):** Predicts the clean feature at intermediate layers instead of flow velocity, which the authors say avoids a manifold gap during optimization, combined with the Full-to-Compact training paradigm.
**Limitation (≤3 sentences):** Not stated in the available abstract text.

---

## AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding
- **arXiv:** 2610.11060 · https://arxiv.org/abs/2610.11060
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song, Jose M. Alvarez, Yunxiang Mao, Jiaqi Ma, Langechuan Liu
- **Qualifying affiliation(s):** NVIDIA — listed among the paper's affiliations, with a footnote noting "work done during an internship at NVIDIA" and co-author Jose M. Alvarez (a known NVIDIA research manager); the HTML extraction could not confirm the exact superscript-to-author mapping. Also 42dot by Hyundai — Hyundai's autonomous-driving subsidiary (flag: not on the default list but comparable to a top-tier industry lab; kept and flagged). Other authors: UCLA, Fudan University (academic).
- **Categories:** cs.CV (primary); cs.AI (cross-listed)
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses world-action models for autonomous driving that jointly predict future scenes and generate trajectories. It argues dense-geometry prediction alone shows scene layout but not which regions matter for the ego vehicle's actions.
**Purpose (≤3 sentences):** To jointly model future action-relevant regions (e.g., drivable areas, collision-critical zones) together with spatial geometry, rather than relying on appearance or geometry alone.
**Breakthrough (≤3 sentences, attributed):** The authors report state-of-the-art results on the NAVSIM benchmark of 91.3 PDMS and 89.9 EPDMS.
**Tools & method (≤3 sentences):** AffordDrive3D uses a VLM backbone for scene semantics and driving context, predicts future geometry from RGB world-model latents, and jointly learns action-relevant affordance regions.
**Limitation (≤3 sentences):** Not stated in the available abstract text.

---

## Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training
- **arXiv:** 2610.10984 · https://arxiv.org/abs/2610.10984
- **Submitted:** 2026-10-07 (v1)
- **Authors:** Hong Huang, Yuqiu Liu, Chenyu You, Daniel Martin, Chuhang Zou, Wuyang Chen
- **Qualifying affiliation(s):** Meta Reality Labs — listed among the paper's affiliations; the HTML extraction could not map the superscript to a specific named author (likely Daniel Martin or Chuhang Zou). Other authors: Simon Fraser University, Stony Brook University, Lawrence Berkeley National Laboratory (academic/national lab).
- **Categories:** cs.CV (primary); cs.GR (cross-listed)
- **Open release:** code and data stated as planned "upon acceptance" (not yet released)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents a training-free framework for generating physically plausible video of fluid-object interactions. It separates physical reasoning, handled by a physics simulator, from appearance synthesis, handled by a pretrained video generator.
**Purpose (≤3 sentences):** To ground existing pretrained video generators in physics for fluid-object interaction scenes without any additional training of the generator.
**Breakthrough (≤3 sentences, attributed):** The authors report reducing object trajectory error by 26.7%-81.5% and fluid endpoint error by 67.9%-84.0% versus baselines, with human raters preferring their outputs in most comparisons.
**Tools & method (≤3 sentences):** A two-level agentic workflow — a vision-language-model agent plans the generation clips, and latent-space guidance injects simulation signals into denoising — is applied plug-and-play to existing video models (Tora, VACE, WanMove) and evaluated on a new benchmark.
**Limitation (≤3 sentences):** The authors state that code and data will be released only upon acceptance, so the method is not yet independently reproducible; no other limitations are stated in the abstract.

---

## Cross-Embodiment Robot Foundation World Models with Latent Actions
- **arXiv:** 2610.10846 · https://arxiv.org/abs/2610.10846
- **Submitted:** 2026-10-07 (v1)
- **Authors:** Huang Huang, Sriram Yenamandra, Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan, Tsung-Yen Yang, Akshara Rai, Michael Rabbat, Li Fei-Fei, Jiajun Wu, Tingfan Wu, Franziska Meier
- **Qualifying affiliation(s):** Meta FAIR Robotics — Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan, Tsung-Yen Yang, Akshara Rai, Michael Rabbat, Tingfan Wu, Franziska Meier, and (partly) Huang Huang and Sriram Yenamandra (flag: the author block credits each as "work partially done while at Meta FAIR Robotics," a past/in-progress note rather than a stated current affiliation; kept and flagged per the borderline-affiliation rule rather than silently dropped). Other authors (current): Stanford University (Li Fei-Fei, Jiajun Wu, and others).
- **Categories:** cs.RO
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces LAC-WM, a robot world model that uses a learned latent action space shared across different robot embodiments, and compares it against EAC-WM, which conditions on explicit motion labels.
**Purpose (≤3 sentences):** To test whether a learned latent action representation transfers across robot embodiments better than conditioning on explicit motion labels.
**Breakthrough (≤3 sentences, attributed):** The authors report LAC-WM improves downstream performance by up to 46.7% on dexterous manipulation and 11.7% on a modified LIBERO benchmark versus EAC-WM, and that LAC-WM's performance improves as the number of pretraining embodiments grows while EAC-WM's declines.
**Tools & method (≤3 sentences):** Evaluated on dexterous manipulation tasks and a modified LIBERO benchmark, directly comparing latent-action conditioning (LAC-WM) against explicit-motion-label conditioning (EAC-WM) for cross-embodiment world models.
**Limitation (≤3 sentences):** Not stated in the available abstract text beyond the EAC-WM comparison itself.

---

Verification pass: each of the 8 qualifying papers above was checked against its own arXiv abstract page (title, authors, v1 date, categories, withdrawal status) and its arxiv.org/html page (author affiliations); all facts and numbers above are drawn from those two pages, and no limitation, number, or claim was invented where the source was silent. Four flagged items (SenseTime, Xiaomi EV, 42dot by Hyundai, KOKONI 3D/Moxin Technology, and the Meta FAIR "work done while at" note) are kept per the skill's borderline-affiliation rule and should be reviewed by the user.

# Near-misses
- 2610.11770 · From Video Clips to Creation Trajectory: Sora100K for AI-Native Video Creation · academic-only — HTML affiliations are Chongqing University of Posts and Telecommunications and GVC Lab, Great Bay University (Dongguan); no qualifying industry co-author found.
- 2610.11736 · Towards Unified Evaluation of Prompt Enhancers for Video Generation (PEBench) · off-topic — a benchmark for evaluating text-prompt-enhancement tools used ahead of video generation (text/image/reference-to-video), not itself a 3D, world-model, character-animation, or game-engine paper, despite a Wan Team/Alibaba Group co-author confirmed in the author block.
- 2610.11572 · PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting · academic-only — HTML affiliations are Chubu University (Japan), DGIST and KAIST (South Korea), and Elith Inc. (a small Japanese startup not comparable to the tracked industry tier); no qualifying affiliation.
- 2610.10855 · OmniHOI: Dexterous Hand-Object Interaction from Monocular Human Video · academic-only — HTML affiliations are Zhejiang University, University of Hong Kong, Shanghai Jiao Tong University, and Shanghai AI Laboratory (a research institute, not an industry company); also off-topic (robot dexterous-manipulation/retargeting, not 3D/world-models/character-animation/game-engines).
