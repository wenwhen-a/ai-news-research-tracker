## Training-Free Target-Aware Refinement of 3D Gaussian Language Map
- **arXiv:** 2610.21619 · https://arxiv.org/abs/2610.21619
- **Submitted:** 2026-10-15 (v1, 10:00:53 UTC)
- **Authors:** Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu
- **Qualifying affiliation(s):** Samsung Electronics, Republic of Korea — Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo (remaining authors: Sungkyunkwan University). FLAG: borderline — Samsung Electronics is not on the core qualified list; kept per the "clearly comparable top-tier industry lab" rule.
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** code/demo — project page states "Project page and code:" https://lab-of-ai-and-robotics.github.io/target-aware-langmap/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents a training-free method to refine an already-distilled 3D Gaussian Splatting (3DGS) language map so that a small set of user-specified text targets is retrieved reliably, without retraining the underlying map. It also identifies and corrects a shared-bias problem in the standard cosine query read-out.

**Purpose (≤3 sentences):** Existing open-vocabulary 3DGS language maps often fail to localize specific user-named targets reliably because of embedding biases in the distilled features. The authors aim to fix this at inference time, with no additional training and no per-scene hyperparameter tuning.

**Breakthrough (≤3 sentences):** The authors report the refinement roughly doubles base open-vocabulary segmentation mIoU on Replica (0.207 → 0.436) and raises top-1 instance-aware localization success from 44.6 to 76.8 on Replica. In a real-world legged-robot demo, they report a language-goal navigation success rate of 78% with the refined map versus 22% with the base map, and the method also lifts LangSplat's mIoU by 79–123% across three datasets as a plug-in.

**Tools & method (≤3 sentences):** A text-promptable segmenter (SAM 3) locates each target per view, and its visual embedding is blended toward the target's SigLIP 2 text embedding using a closed-form minimal blending coefficient (no tuning), on top of a SAM 2 + SigLIP 2 base map; a centering step at query read-out removes a shared bias the authors identify in injected embeddings. The method was demonstrated on a Unitree Go2 quadruped using LiDAR-inertial SLAM (LIO-SAM) and A* path planning on a 2D occupancy grid.

**Limitation (≤3 sentences):** The authors state that classes the segmenter never detects remain at zero IoU (the segmenter's recall is the bottleneck there), and that the minimal-overwrite strategy "may leave the most stubborn views unrecovered." They also note the object-level plug-in does not improve results on Replica because injection cannot create missing small-object instances.

---

## GRASE: Geometry-native Real-to-sim Agentic Scene Modeling from Video
- **arXiv:** 2610.21498 · https://arxiv.org/abs/2610.21498
- **Submitted:** 2026-10-15 (v1, 08:34:00 UTC)
- **Authors:** Zhaorui Lin, Haohan Liu, Zhen Chen, Xiangru Huang
- **Qualifying affiliation(s):** Adobe Systems — Zhen Chen (other authors: Xi'an Jiaotong University, Fuzhou University, Westlake University)
- **Categories:** cs.CV
- **Open release:** none found (no Comments field, project page, or code link on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GRASE is an agentic framework that turns a captured multi-view video of a real indoor space into an editable, simulation-ready 3D scene, treating the original video as a persistent reference it checks against throughout. It fits the room's structural shell and openings, places generated assets in a shared coordinate frame, and iteratively refines each asset's geometry and placement.

**Purpose (≤3 sentences):** The authors target error accumulation in one-pass real-to-sim pipelines, where mistakes made in early stages (layout fitting, object placement) propagate uncorrected into the final scene. GRASE instead keeps revising its scene hypothesis whenever rendered views disagree with the captured video.

**Breakthrough (≤3 sentences):** On the authors' Imaginarium benchmark (15 scenes) and 8 Replica scenes, the authors report GRASE substantially lowers scene-level Chamfer Distance versus the strongest baseline (e.g., Imaginarium: 3.14 cm vs. 11.00 cm for GPT-6 + TRELLIS.2 + point cloud) and raises object instance mIoU (e.g., Imaginarium: 0.74 vs. 0.21). They report it outperforms SAM3D and GPT-6-based real-to-sim baselines, including one built on "GPT6-Astra."

**Tools & method (≤3 sentences):** The pipeline samples video frames, runs Depth Anything 3 and SAM 3 for depth/segmentation, fits the room shell with RANSAC and parametric patches for curved surfaces, and places/generates objects via TRELLIS.2 or Blender-MCP-built primitives. A tool-using VLM agent iteratively verifies rendered views against the captured video and accepts only edits that reduce the diagnosed discrepancy without regressions.

**Limitation (≤3 sentences):** The authors acknowledge reconstruction is limited in heavily occluded regions with insufficient geometric evidence, which are completed by extending surfaces or generative priors and marked as inferred rather than observed. They also note the inventory/support-graph/verification steps depend on VLM judgments (so early errors can persist under ambiguous evidence), and that the method assumes a static scene, not recovering articulation, materials, or physical properties.

---

## DeSpatial: The devil of Agentic Spatial Reasoning Lies in 3D Itself
- **arXiv:** 2610.20990 · https://arxiv.org/abs/2610.20990
- **Submitted:** 2026-10-14 (v1, 22:05:23 UTC)
- **Authors:** Yifei Liu, Xiaolong Zhou, Ziyang Gong, Yifan Zhou, Yuanyuan Gao, Yuning Gong, Yuchen Yang, Hongjie Zhang, Xue Yang, Xiao Sun, Zhihang Zhong
- **Qualifying affiliation(s):** Tencent — co-author(s) within the group of Yuning Gong, Yuchen Yang, Hongjie Zhang, Xue Yang, Xiao Sun, Zhihang Zhong (HTML affiliation block lists "Shanghai Jiaotong University / HKUST / Tencent / Fudan University" jointly for this author group; exact per-author mapping not resolvable from the page). Other authors: Shanghai Artificial Intelligence Laboratory, Beihang University.
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DeSpatial splits agentic spatial reasoning into a shared 3D perception stage — building one unified, metric, gravity-aligned scene with consistent object identities — and a separate reasoning stage that operates on that scene. The authors argue, and verified on-topic by close reading, that this is a 3D scene-reconstruction and -understanding paper, not a generic agentic-reasoning benchmark paper: its core contribution is a perception pipeline that fuses segmentation and depth into consistent 3D geometry.

**Purpose (≤3 sentences):** The paper addresses the problem that spatial agents combine independently predicted tools (segmentation, depth, detection) whose outputs disagree with each other, producing fragmented or duplicated object identities that corrupt downstream spatial answers. The authors set out to show that unreliable 3D perception, not reasoning, is the main bottleneck.

**Breakthrough (≤3 sentences):** In an oracle test, the authors report that swapping ground-truth 3D bounding boxes into the agent raises accuracy on five object-centric VSI-Bench tasks from 50.38% (raw perception pipeline) to 98.23%. With DeSpatial's own perception pipeline (no ground truth), they report 69.22% average on full VSI-Bench, 87.19% on MindCube-Tiny, 68.35% on ViewSpatial, and recall of 86.7–90.3% across time windows up to 240 minutes on VSI-SUPER, versus baselines such as S-Agent (75.0–77.2% recall) and Cambrian-S-7B-LFP (40.0–45.0%).

**Tools & method (≤3 sentences):** A joint segmentation-depth co-refinement module merges same-object masks across a frame and removes projection artifacts, and a cross-view instance fusion module links overlapping instances of the same object across different views (not within one frame) using 3D structure and mask-appearance checks. Results use a Qwen3-VL-8B-Instruct backbone with SAM3, Pi3, Depth Anything 3, VGGT, and GeoCalib as the perception tools.

**Limitation (≤3 sentences):** The authors state the unified representation depends on detection quality, reconstructed geometry, metric scale, and gravity estimates, so it cannot recover unobserved surfaces or missing detections, and incorrect part-count or identity judgments can discard valid geometry or wrongly merge distinct objects. They also note the oracle result covers only five object-centric categories with annotation-consistent answers, so it does not show perception is the only bottleneck across all spatial tasks.

---

## WorldCast: Exploring Intelligent Visual Generation in World State Prediction
- **arXiv:** 2610.20731 · https://arxiv.org/abs/2610.20731
- **Submitted:** 2026-10-14 (v1, 18:00:07 UTC)
- **Authors:** Wenhao Yan, Haodong Li, Xiaotong Li, Yaxin Luo, Zhengrong Yue, Jialv Zou, Xu Huang, Haojin Yang, Nan Jia, Yan Feng, Peng Pei, Xunliang Cai
- **Qualifying affiliation(s):** Meituan (LongCat team) — co-author(s) among the 12 listed (HTML affiliation block lists "THU / Meituan LongCat / CUHK / PKU / MBZUAI / SJTU / HUST" without a resolvable per-author mapping; one author's footnote says work was "done during internship at Meituan"). FLAG: borderline — verification found **no Google/Google DeepMind author affiliation** (Google appears only as a cited external model, e.g. "Nano Banana Pro," never as an author institution), contrary to the expected lead; Meituan is kept as a large Chinese tech company with its own foundation-model line (LongCat), comparable in standing to other borderline-flagged firms, for the user to judge.
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found (page states no release of benchmark, code, or data)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldCast is a 320-case, 8-category benchmark for multi-step "world state prediction" — testing whether visual generative models can produce the correct sequence of future visual states given a scenario, beyond basic text-to-image/video generation. It sits at the top (L3/L4) of a four-level capability hierarchy the authors propose for multimodal generation.

**Purpose (≤3 sentences):** The authors argue that existing benchmarks mostly test simpler generation (static text-to-image, editing, basic video) and that the highest-level tasks — dynamic, physically plausible transitions guided by visual/physical/procedural references — are underexplored. WorldCast is built to probe this gap across 1,352 requested visual states.

**Breakthrough (≤3 sentences):** The authors report evaluating 12 models and finding frontier proprietary image models advancing quickly (GPT-Image-2.5 scores 72.8 overall) while substantial gaps remain versus other systems (Nano Banana Pro 42.8, best open-source model SenseNova-U1 at 20.1; best video model Seedance 2.0 at 47.2). They also report that stronger underlying language-model reasoning correlates with better generative world-state prediction performance.

**Tools & method (≤3 sentences):** Scoring combines Task Completion, Causal Plausibility, and Visual Consistency (weighted 0.4/0.4/0.2) using GPT-5.5 as an LMM-as-a-judge, with "GPT-6 Astra" (via Codex) as an agentic video adapter that extracts keyframes from generated videos for scoring. The authors report judge-vs-human agreement of Pearson r ≥ 0.97 across four validation dimensions, and that rescoring with other judges (GLM-5.3-Flash, Gemini 3.1 Pro) preserved the model ranking.

**Limitation (≤3 sentences):** The paper has no dedicated limitations section; the authors note video world-model benchmarks were deliberately excluded because they don't test the reasoning-based transitions and heterogeneous references WorldCast targets. They suggest distilling expensive code-based simulation into direct visual generation as future work, and state no release of the benchmark, code, or data.

---

# Near-misses
- 2610.21129 · Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search · No qualifying affiliation: all six authors list only South China University of Technology in the HTML affiliation block; NVIDIA (A800/H800 GPUs) and Tencent do not appear anywhere as author affiliations, only as hardware/absent.
- 2610.21121 · ResStreamGS: Residual-Sensitive Dual-Stream Gaussian Splatting for Mobile Volumetric Video Streaming · Affiliation unverifiable: the HTML version exists but its IEEE-VGTC LaTeX template failed to render any author/affiliation block (raw HTML shows unresolved `\vgtccategory`/`\onlineid` macros and no institution text); Qualcomm appears only as the Snapdragon 778G test-device SoC. Per instructions, affiliation was not guessed from the PDF.
- 2610.21758 · Beyond Source Prompts: Towards Visually Grounded AI-Generated Video Quality Assessment · No qualifying affiliation and off-topic: all four authors are affiliated solely with the University of Bristol; Amazon appears only in the acknowledgments (thanking an Amazon Prime Video employee for advice), not as an author affiliation. The paper is also a generic video-quality-assessment metric (VGCap) with no connection to building 3D/world-model/animation/engine technology.
- 2610.22282 · Routing Policy Optimization for Online Diffusion Reinforcement Learning · Off-topic despite a real qualifying affiliation (ByteDance, alongside National University of Singapore, confirmed in the HTML affiliation block): RPO is a generic online-RL training method for diffusion/flow generators, demonstrated on Stable Diffusion 3.5 (image) and Wan2.2-TI2V-5B (video) with no specific 3D/world-model/character-animation/game-engine application; the authors state it is architecturally restricted to attention-based backbones and has not been extended further.
- 2610.22364 · T2-z: Test-Time Optimization of Environment Latents for Robotic World Models · Off-topic: a robotic-manipulation world model (Stanford/CMU/Toyota Research Institute); not a 3D/game/animation/engine paper.
- 2610.22356 · DK-VLM: Geometry as Position for Spatial Reasoning in Vision-Language Models · Off-topic: a generic vision-language-model spatial-reasoning paper (Huawei, borderline affiliation but wrong topic area), not 3D generation or game tech.
- 2610.22340 · Dexterity from Supervised Play · Off-topic: robot dexterous-manipulation paper (Amazon Frontier AI & Robotics); not game/3D/animation/engine.
- 2610.20939 · MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training · Off-topic: GUI agent evaluation platform (Alibaba), explicitly excluded category per the tracker's screening rule.
- 2610.21910 · CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model · Affiliation unverifiable: no HTML version exists on arXiv; the screening "Google" hit was a false positive from a "Google Scholar" citation-tool link on the abstract page, not an author affiliation.
