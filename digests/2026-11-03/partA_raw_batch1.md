## Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data
- **arXiv:** 2611.03626 · https://arxiv.org/abs/2611.03626
- **Submitted:** 2026-11-02
- **Authors:** Rafał Karp, Gene Liu, Shih-Hsin Li, Eric Courtemanche, Shengze Wang, Josef Spjut, David Pankratz, Mischa Kolbe, Michael Stengel, Sven Elflein, Adam Grygielski, Liwen Wu, Anjul Patney
- **Qualifying affiliation(s):** NVIDIA — all 13 listed authors
- **Categories:** cs.CV
- **Open release:** none found (no code/dataset/project-page link in the paper; only references to Unreal Engine/Fab and the arXiv/build pages)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Isekai3D SDG, a platform for simulating and capturing synthetic 3D gameplay data for vision and world-model research. It pairs reusable environment/character assets with Unreal Engine plugins in a two-stage workflow: a simulation stage that records world state, character movement, actions, and camera tracks, and a capture stage that replays the recording to produce outputs such as video, images, and depth maps.
**Purpose (≤3 sentences):** The authors aim to make it easier to generate diverse synthetic gameplay visual data with frame-aligned camera, character, and action metadata, in a format ready for model training.
**Breakthrough (≤3 sentences):** The authors report that separating simulation from capture lets a single recorded gameplay session produce multiple output variants without re-simulating, and that the platform uploads generated data directly in a training-friendly format, reducing intermediate storage and manual processing.
**Tools & method (≤3 sentences):** The system is built as Unreal Engine plugins around a packaged game; it decouples a simulation pass (recording world/character/action/camera state) from a capture pass (replaying the recording to render selected output modalities).
**Limitation (≤3 sentences):** The paper has no dedicated limitations section. It notes that the benefit of decoupled ("phantom") simulation is greater when recording accounts for a substantial fraction of total generation time, and that per-character behavior, animation, and capture still add computation cost.

## History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models
- **arXiv:** 2611.02782 · https://arxiv.org/abs/2611.02782
- **Submitted:** 2026-11-02
- **Authors:** Hangyi Kuang, Chengzhi Wang, Yefei He, Weijie Wang, Yuke Zhao, Zhuokun Chen, Zisu Huang, Yifan Yang, Xiaoxuan He, Feng Chen, Bohan Zhuang
- **Qualifying affiliation(s):** Microsoft Research — Yuke Zhao, Zisu Huang, Yifan Yang (listed with a dual Zhejiang University / Microsoft Research affiliation). Other authors are affiliated with Zhejiang University, Monash University, and Adelaide University. (Note: a "Google" flag from the screening tool was checked and found to be a false positive — the term does not appear anywhere on the paper's page; the real qualifying affiliation is Microsoft Research.)
- **Categories:** cs.CV
- **Open release:** code (https://github.com/ziplab/History-Forcing); project page (https://ziplab.github.io/History-Forcing-Project-Page/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses weak historical conditioning in few-step autoregressive video diffusion world models, which causes drift and inconsistency over long video horizons. It proposes History Forcing, an on-policy distillation framework that strengthens history-dependence by computing the residual between a teacher's predictions with and without historical context, then weighting and adding that residual to the distillation target.
**Purpose (≤3 sentences):** Few-step autoregressive video diffusion enables efficient generation, but existing few-step generators under-use historical context, limiting consistency and quality in long-horizon video world models.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art results among 1.3B-parameter models, with a VBench quality score of 85.07 on 15-second videos and a VBench-Long score of 79.82 on 60-second videos. For out-of-sight scenarios they report improved Evolution Quality on PlayWorld (2.35 → 2.70) and Object Consistency on MemoBench (58.43 → 62.18).
**Tools & method (≤3 sentences):** The method distills a bidirectional teacher into a few-step autoregressive student using a history-dependence residual weighted into the score/velocity distillation target; experiments use 1.3B teacher/student models for long-video generation and a 5B backbone for world modeling, evaluated on UltraVideo-Long, VidProM, Pexels, PlayWorld, and MemoBench.
**Limitation (≤3 sentences):** The authors state their experiments are limited to 1.3B teacher/student models for long-video generation and a 5B backbone for world modeling, and that historical supervision remains constrained by the underlying models' ability to capture temporal dynamics.

## Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling
- **arXiv:** 2611.02474 · https://arxiv.org/abs/2611.02474
- **Submitted:** 2026-11-02
- **Authors:** Lingwei Dang, Yan Zhou, Juntong Li, Zhenhao Zhang, Yiteng Chen, Xiaoqiang Liu, Liang An, Hongwen Zhang, Wei Min, Guoxin Zhang, Pengfei Wan, Yebin Liu, Qingyao Wu
- **Qualifying affiliation(s):** Kuaishou/KlingAI Research — Lingwei Dang (work done during an internship at KlingAI Research), Yan Zhou (project lead), Guoxin Zhang, Pengfei Wan. Other authors list Nanjing University, Beijing Normal University, Shadow AI, Tsinghua University, and South China University of Technology (corresponding author: Qingyao Wu).
- **Categories:** cs.CV
- **Open release:** demo/project page (https://droliven.github.io/Gnomon4D) (no code or dataset release stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Gnomon4D, a world-action model (WAM) that jointly generates future video, robot actions, and GeoDelta, an explicit 4D geometric motion field capturing how embodiment and object points move in the image plane and change in depth across frames. It adds two attention mechanisms to focus the model on task-relevant interactions and state transitions.
**Purpose (≤3 sentences):** The authors aim to ground world-action models in explicit geometric motion so the model focuses on task-relevant interaction regions and transition moments (e.g., grasp/release), rather than treating the scene uniformly.
**Breakthrough (≤3 sentences):** The authors report that Gnomon4D leads on the RoboTwin 2.0, VLABench, and RoboDojo benchmarks, and beats the strongest real-robot baseline by 7.0 and 16.0 percentage points in in-distribution and out-of-distribution settings, respectively.
**Tools & method (≤3 sentences):** The model uses Interaction-Salient Attention (spatial readout focused on task-relevant interaction regions) and Transition-Anchored Aggregation (evidence gathering around motion-state transitions), pretrained on human egocentric data via a shared human-robot quasi-action representation and then mid-trained on robot data.
**Limitation (≤3 sentences):** The authors note GeoDelta depends on measured camera depth in real-robot experiments and on monocular depth estimates (plus masks and optical flow) for human videos, and that errors on thin, reflective, or transparent surfaces mainly perturb the depth-change component.

## AgiWorld: An Agentic Video World Model for Building Persistent Worlds
- **arXiv:** 2611.02341 · https://arxiv.org/abs/2611.02341
- **Submitted:** 2026-11-02
- **Authors:** Shaoheng Fang, Yiqun Mei, Hanwen Jiang, Xin Sun, Haitian Zheng, Hao Tan, Kalyan Sunkavalli, Georgios Pavlakos, Qixing Huang, Yiwei Hu
- **Qualifying affiliation(s):** Adobe Research — the paper lists two affiliations for the author group, "The University of Texas at Austin" and "Adobe Research" (the exact per-author split was not recoverable from the extracted text, but several co-authors, consistent with prior Adobe Research publications in this area, are Adobe-affiliated; Kalyan Sunkavalli is an established Adobe Research scientist)
- **Categories:** cs.CV, cs.AI
- **Open release:** demo/project page (https://bshfang.github.io/agiworld/); code not yet available (the paper states the agent's guidelines, schemas, and specification "will be released with the code")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents AgiWorld, a system that builds a persistent, explorable video world from a single image and a free-form instruction, combining a planning agent (AgiWorld-Agent) that designs the world and directs exploration with a video world model (AgiWorld-WM) that generates video in chunks and stores it with geometry in a spatial memory.
**Purpose (≤3 sentences):** The authors target long-horizon world generation where previously generated regions must remain consistent when revisited, which plain video generation alone struggles to maintain.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art results on world revisiting and exploration benchmarks, and state that persistence "arises not from the video model alone but from its closed loop with the agent," using occlusion-aware history selection and reliability-based memory maintenance for long rollouts.
**Tools & method (≤3 sentences):** AgiWorld-Agent plans world structure and directs exploration; AgiWorld-WM generates video chunk-by-chunk and maintains a spatial memory with geometry; occlusion-aware history selection and reliability-based memory maintenance manage long rollouts.
**Limitation (≤3 sentences):** No dedicated limitations section was found in the paper's abstract, introduction, system overview, agent/world-model descriptions, training data, experiments, related work, or conclusion sections as fetched.

## Lie Routing Vision Language Models for View-Robust 3D Understanding
- **arXiv:** 2611.02306 · https://arxiv.org/abs/2611.02306
- **Submitted:** 2026-11-01
- **Authors:** Jingjun Yi, Chen Hu, Qi Bi, Hao Zheng, Huimin Huang, Yongkang Li, Wei Ji, Yawen Huang, Xian Wu, Yefeng Zheng
- **Qualifying affiliation(s):** Tencent, China — Hao Zheng, Huimin Huang, Wei Ji, Yawen Huang, Xian Wu. Other authors list Westlake University (Jingjun Yi, Chen Hu, Yefeng Zheng) and University of Amsterdam (Qi Bi, Yongkang Li; Jingjun Yi is also now affiliated with University of Amsterdam).
- **Categories:** cs.CV, cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies "viewpoint-induced semantic drift," where vision-language models give inconsistent answers about the same object as the camera viewpoint changes. It proposes LieVLM, a routing framework that applies local SO(3) rotations to projected visual features within learned subspaces to make the model's understanding more view-robust.
**Purpose (≤3 sentences):** Multimodal large language models are reported to answer inconsistently about the same 3D object or scene depending on viewpoint, which the authors frame as a barrier to reliable 3D scene understanding.
**Breakthrough (≤3 sentences):** The authors report consistent gains over additive-fusion baselines on 3D captioning, grounding, detection, and spatial-reasoning tasks, supported by ablations and viewpoint analyses.
**Tools & method (≤3 sentences):** LieVLM predicts rotation parameters and routing coefficients from geometry tokens extracted by VGGT, then applies local SO(3) rotations to projected visual features within learned subspaces before fusing them into the VLM.
**Limitation (≤3 sentences):** Not confirmed from the fetched content — the paper's table of contents lists a "G Limitations" appendix, but its text was not retrievable from the pages fetched, so it is not reproduced here to avoid inventing content.

# Near-misses
- 2611.02822 · Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion · off-topic: the paper is a distillation-time plug-in for general autoregressive video diffusion models aimed at long-horizon video generation quality/consistency; it is never framed as a world model (the term does not appear anywhere in the paper), and has no 3D, character-animation, or game-engine content. (Affiliation check: Sony AI — Akio Hayakawa, Masato Ishii, Takashi Shibuya, Yuki Mitsufuji — would have qualified; dropped solely on topic grounds.)
- 2611.02631 · UniCross3D: Unified Cross-View and Cross-Domain Diffusion for Consistent Single-Image 3D Generation · no qualifying industry affiliation: all three authors (U-Chae Jun, Jaeeun Ko, Jiwoo Kang) are affiliated solely with Sookmyung Women's University, South Korea (confirmed from the PDF title page; the arXiv HTML mirror 404s for this paper). Topic (single-image 3D generation) would otherwise have qualified.
