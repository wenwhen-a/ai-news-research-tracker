# Part A — Papers
Window: last 30 days (2026-09-22 to 2026-10-22). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: pre-screened lead list (13 arXiv IDs), each verified individually against its arXiv abstract page and HTML full text. Qualifying papers: 7 (1 flagged).

---
## Agentic World Action Models
- **arXiv:** 2610.30136 · https://arxiv.org/abs/2610.30136
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Renrui Zhang, Roei Herzig, Yutong Bai, Ken Goldberg, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi "Jim" Fan, Trevor Darrell
- **Qualifying affiliation(s):** NVIDIA — Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi "Jim" Fan (per paper's own numbered affiliation footnotes: 1=UC Berkeley, 2=NVIDIA, 3=UPenn; Dantong Niu is 1,2)
- **Categories:** cs.RO
- **Open release:** none stated as released; project page only (agentic-wam.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces AW-0, an "agentic world action model" that jointly generates code, future video, and robot actions as three coupled streams in one mixture-of-transformers architecture. Code serves both to structure multi-step prediction/control and to represent reusable skill programs, built from an automated pipeline that labels robot and human video with aligned programs and consolidates them into skill libraries. The authors evaluate it on RoboTwin 2.0 and physical bimanual manipulation tasks.
**Purpose (≤3 sentences):** The authors state that existing world action models give visual foresight for robot manipulation but lack mechanisms for reusing skills compositionally, while agentic/code-based robotics planning lacks grounding in physical dynamics prediction. AW-0 is proposed to connect planning, prediction, and execution within one world-action-model framework.
**Breakthrough (≤3 sentences):** The authors report improved task performance over VLA (vision-language-action) and WAM (world action model) baselines on RoboTwin 2.0 and physical bimanual manipulation tasks, with additional reported gains in language following, semantic reasoning, and robustness.
**Tools & method (≤3 sentences):** The architecture uses three 28-layer transformer "experts" (code, video, action) sharing a 2,048-dimensional joint attention space, trained via masked joint attention; training data comes from an automated curation pipeline that annotates robot/human demonstration video with programs.
**Limitation (≤3 sentences):** The authors state in their "Limitations and Future Work" appendix that planning quality depends on annotation accuracy and skill-library coverage, since the code stream is trained on automatically annotated demonstrations; they note generated programs can select an appropriate skill but still fill in incorrect arguments.

---
## ALPS: Visual State Encoders for World Models
- **arXiv:** 2610.30120 · https://arxiv.org/abs/2610.30120
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei, Hongliang Fei, Yuyin Zhou, Cihang Xie
- **Qualifying affiliation(s):** Google — Jieru Mei, Hongliang Fei
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper argues that a world model's visual foundation should combine physical-state information, language alignment, and pixel reconstruction in one representation. It introduces ALPS, a ViT-B/16 pretrained from scratch on still images and text with language, reconstruction, and spatial-correspondence objectives, then refined via cross-view self-distillation. Frozen ALPS tokens are tested across 15 public encoders on state-probing and downstream world-model/control benchmarks.
**Purpose (≤3 sentences):** The authors state existing visual encoders typically specialize in only one or two of the three capabilities (state, language, reconstruction), limiting their use as a shared foundation for world models that must predict, follow instructions, and be visually inspected.
**Breakthrough (≤3 sentences):** The authors report ALPS achieves the lowest aggregate LIBERO state-probe error among ViT-B models, matching a 3.5× larger V-JEPA 2-L, and the highest mean LIBERO policy success (85.5%) among tested encoders. They also report ALPS matches or exceeds leading encoders on world-model planning benchmarks PushT, Wall, and Granular, while allowing predicted future tokens to be decoded directly into pixels.
**Tools & method (≤3 sentences):** ALPS is pretrained only on still images and paired text (no video), using joint language, reconstruction, and spatial-correspondence objectives followed by cross-view self-distillation; it is evaluated against 15 public encoders on LIBERO and the PushT/Wall/Granular world-model planning benchmarks.
**Limitation (≤3 sentences):** The authors state in their "Limitations and future work" section that they focus on a single ViT-B/16 backbone and simulation benchmarks for controlled comparison, leaving larger model scales and real-robot deployment to future work. They also note their training recipe relies on a two-stage curriculum to balance reconstruction, language, and spatial-state objectives.

---
## Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation
- **arXiv:** 2610.29989 · https://arxiv.org/abs/2610.29989
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu, Ying Shan, Limin Wang
- **Qualifying affiliation(s):** Tencent — Yukun Huang, Wenbo Hu, Ying Shan (ARC Lab, Tencent IEG)
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper argues that autoregressive video diffusion models trained with teacher forcing can produce plausible continuations without actually learning how scenes evolve, because strong local visual continuity gives a shortcut for denoising the current chunk. It introduces Future Chunk Prediction (FCP), an auxiliary training objective that predicts temporally separated future chunks without access to the intervening visual context. FCP is trained jointly with standard teacher-forced denoising and leaves inference unchanged.
**Purpose (≤3 sentences):** The authors frame this work explicitly as "a pathway toward generative world modeling," aiming to force autoregressive video generators to model visual evolution rather than only local continuity.
**Breakthrough (≤3 sentences):** The authors report FCP achieves superior physical plausibility compared with standard teacher-forced autoregressive training, at a lower overall training compute budget. They also report that FCP produces a more structured representation space in their visualizations.
**Tools & method (≤3 sentences):** FCP draws its supervision directly from training videos (needing no extra pretrained visual encoder) and conditions offset-specific predictors only on the single source chunk rather than the full visible history, which the authors say costs 40–50% less training compute than a full-context variant at matched quality.
**Limitation (≤3 sentences):** The paper's "Limitations and Discussions" appendix is framed mainly as a comparison with concurrent work (Next Forcing), noting their FCP prototype targets autoregressive video generation broadly (as a path to world modeling) rather than robotic world-action modeling specifically; no separate acknowledged weakness beyond this scope distinction is stated in the available text.

---
## CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion
- **arXiv:** 2610.29915 · https://arxiv.org/abs/2610.29915
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Kai Zhu, Yintianrun Zhang, Shuwei Jiang, Ruolin Zuo, Yixin Chen, Duomin Wang, Miao Liu, Yin Li, Daquan Zhou, Yiwu Zhong
- **Qualifying affiliation(s):** NVIDIA — Duomin Wang. FLAG: borderline — core contribution is camera-ego-motion consistency in general-purpose video generation models (VGMs), not a world-model paper per se, though the authors tie results to world action model (WAM) gains on a robotics benchmark.
- **Categories:** cs.CV
- **Open release:** code (github.com/PKU-VaLuE-Lab/CausalAlign) and project page (pku-value-lab.github.io/CausalAlign-homepage)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses camera ego-motion drift over long horizons in diffusion-based video generation models. The authors use linear probes and causal interventions to find that ego-motion information rises then falls across denoising, and propose CausalAlign, which aligns video-model representations at the identified layers to a 3D foundation model via a "delta-token space" encoding frame-to-frame change. They fine-tune Wan2.2 on DL3DV and RealEstate10K.
**Purpose (≤3 sentences):** The authors state camera ego-motion is essential for consistent geometry and trajectories in generated video, but that it drifts over long horizons in existing video generation models, motivating a diagnostic-then-alignment approach.
**Breakthrough (≤3 sentences):** The authors report CausalAlign improves motion accuracy, geometric consistency, and temporal smoothness on fine-tuned Wan2.2, with geometric consistency improved by more than 20% relative to the base model. They also report a 10-point gain in success rate for world action models on mobile-manipulation tasks in the RoboCasa365 benchmark when using the fine-tuned video model.
**Tools & method (≤3 sentences):** The method combines linear probing and causal interventions to locate where/how ego-motion is represented during denoising, then aligns those layers' representations to a 3D foundation model in a delta-token space; it is applied by fine-tuning Wan2.2 on the DL3DV and RealEstate10K datasets.
**Limitation (≤3 sentences):** The authors' own diagnosis finds ego-motion representation "fades away" at late denoising timesteps and in the last few transformer layers, which they interpret as a retention failure of the internal ego-motion state rather than a failure to form camera geometry initially. They also note that unconstrained image-to-video generation is one-to-many (multiple camera trajectories can validly continue one input), which complicates direct ground-truth trajectory-error evaluation.

---
## JointLight: Human-Centric Video Relighting with Asynchronous RGB-Irradiance Joint Modeling
- **arXiv:** 2610.29780 · https://arxiv.org/abs/2610.29780
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Henglei Lv, Bailin Deng, Xiaoqiang Liu, Yichen Wang, Haoxian Zhang, Pengfei Wan, Lin Gao
- **Qualifying affiliation(s):** Kuaishou Technology — Xiaoqiang Liu, Haoxian Zhang, Pengfei Wan
- **Categories:** cs.CV; accepted to SIGGRAPH Asia 2026 Conference Papers (DOI 10.1145/3829340.3842252)
- **Open release:** code and dataset stated as "will be publicly released" (not yet released as of this version)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses precise illumination control in human-centric video relighting, noting that diffusion-based relighting methods either model light transport implicitly (hurting controllability) or use path-traced irradiance cues directly as control signals (introducing artifacts). It proposes an asynchronous joint-modeling paradigm that denoises RGB and ground-truth irradiance frames on separate timestep schedules, with a domain-matching stage bridging irradiance cues and ground-truth maps. Training data comes from a synthetic multi-illumination video dataset with paired irradiance maps built using a game engine.
**Purpose (≤3 sentences):** The authors state existing video relighting approaches lack fine-grained illumination control due to scarce precisely-labeled relighting video datasets and the implicit nature of neural light-transport modeling.
**Breakthrough (≤3 sentences):** The authors report their model, trained exclusively on their synthetic dataset, generalizes robustly to real-world scenes and outperforms prior approaches in both lighting fidelity and generative quality (per their evaluation against prior methods and HumanOLAT ground-truth comparisons).
**Tools & method (≤3 sentences):** The method uses asynchronous denoising timestep schedules for RGB vs. irradiance frames, a domain-matching training stage, and an "asynchronous hijacked generation pipeline" at inference; training data is a multi-illumination synthetic video dataset with paired irradiance maps generated via a game engine, evaluated in part against HumanOLAT one-light-at-a-time captures.
**Limitation (≤3 sentences):** The authors state in their "Limitations and Future Work" section that irradiance captures diffuse transport only, so the method cannot explicitly or physically control full specular transport — polished metal, mirrors, and glass remain difficult, with a shown failure case on highly reflective surfaces. They also note suppressing high-frequency cue errors can over-smooth fine facial detail around the eyes and mouth.

---
## LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces
- **arXiv:** 2610.29408 · https://arxiv.org/abs/2610.29408
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Xinyu Wang, Huafeng Shi, Yue Ma, Zijie Meng, Teng Xi, Yuzhuo Chen, Yucheng Wang, Ruicheng Zhang, Guoxin Zhang, Pengfei Wan, Xiu Li, Fangneng Zhan
- **Qualifying affiliation(s):** Kuaishou Technology — Huafeng Shi, Teng Xi, Guoxin Zhang, Pengfei Wan (listed as "Kling Team," Kuaishou's video-generation research group)
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies multi-agent interactive video world models that generate one joint visual future for several independently controlled agents, which may take heterogeneous controls ranging from game buttons to continuous robot commands. It introduces LiveAct, built on a Heterogeneous Action Interface with Agent-Aware Spatial Modulation (binding each action stream to its visual agent via language-driven spatial gates) and Schema-Guided Action Adaptation (giving each control variable a language-based meaning). The interface is transferred to a blockwise causal generator for streaming generation.
**Purpose (≤3 sentences):** The authors state that most existing interactive video world models assume a single controlled agent and a task-specific action interface, so they target the harder problem of independently controlling multiple agents with differently-typed action spaces (e.g., game vs. robot controls) within one generated video.
**Breakthrough (≤3 sentences):** The authors report 0.898 and 0.942 agent-attribution accuracy for games and robot manipulation respectively, without using agent locations or identity crops, and report their causal generator reaches 17.70 FPS at 512×448 resolution.
**Tools & method (≤3 sentences):** LiveAct is instantiated and evaluated on six multi-agent data sources spanning games and multi-robot manipulation, using teacher forcing and rollout-aware distribution matching to transfer the interface to a blockwise causal (streaming) generator, measured on visual quality, action following, agent attribution, and latency.
**Limitation (≤3 sentences):** The available text does not include an explicit "Limitations" section; the appendix discusses failure modes of comparison baselines (e.g., scene drift, frames degrading to black, game-track quality decaying over time) rather than stating LiveAct's own acknowledged weaknesses. (Observed, not stated): evaluation is confined to the six curated multi-agent sources described in the paper, and generalization beyond them is not reported.

---
## Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision
- **arXiv:** 2610.28954 · https://arxiv.org/abs/2610.28954
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Gonzalo Gómez-Nogales, Daohan Lu, Peiye Zhuang, Tinghui Zhou, Yi Zhou
- **Qualifying affiliation(s):** Roblox and Adobe — both listed among the author team's affiliations (Universidad Rey Juan Carlos, New York University, Roblox, Adobe); the arXiv HTML markup lists these four institutions together in one note without marking which exact author maps to which, though a footnote confirms at least one author did "work done while at Roblox"
- **Categories:** cs.CV
- **Open release:** model and project page stated as "will be released" at https://gonzalognogales.github.io/coarse2real-sharp/ (not yet released as of this version)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses coarse-to-real (C2R) video generation — converting coarse animation, simulation, or game-rendered video into photorealistic video while preserving scene layout, camera motion, and dynamics — without needing expensive aligned (coarse, realistic) video pairs. It exploits the asymmetry that paired real-to-coarse images (unlike paired videos) are easy to construct with existing editing/3D-reconstruction tools, training a DINO-R2C model on such image pairs and applying it frame-wise to real videos to synthesize pseudo-coarse videos. A second model, C2R#, then learns to generate each real video from its corresponding pseudo-coarse video.
**Purpose (≤3 sentences):** The authors state that prior C2R systems require aligned (coarse, realistic) video pairs, which are expensive to create and confine such systems to narrow synthetic domains; their pair-free approach is meant to let training scale with ordinary real-video corpora instead.
**Breakthrough (≤3 sentences):** The authors state their pair-free training "scales with any real-video corpora rather than with paired synthetic videos," and that at inference the DINO-R2C model is discarded so actual coarse (e.g., game-rendered) videos drive the C2R# model directly; no quantitative benchmark numbers were available in the excerpted abstract/intro text reviewed.
**Tools & method (≤3 sentences):** DINO-R2C is trained on real-to-coarse image pairs in DINO feature space and applied frame-wise to real videos to generate pseudo-coarse training videos; C2R# is then trained to map pseudo-coarse videos back to their real counterparts, with coarse inputs at inference able to come from animation, simulation, or game engines.
**Limitation (≤3 sentences):** The authors state in their "Limitations and Discussion" section that performance may degrade when the gap between pseudo-coarse (DINO-R2C output) and actual coarse videos becomes large, since the method relies on pseudo-coarse videos as an approximation of real inference-time coarse inputs. They also note that evaluating on actual coarse videos is difficult because paired realistic ground truth is unavailable, requiring reference-free metrics and human judgment instead.

Near-misses dropped: 6 of 13 candidate leads (listed below), for lacking a qualifying industry affiliation or being off-topic for this tracker. Verification pass: all 7 included papers were checked a second time against their arXiv abstract page (submission date, authors, categories, withdrawal status) and HTML full text (affiliations, abstract claims, limitations) before inclusion.

# Near-misses
- 2610.30036 · Attn-Forcing: Learning Full-Context Attention Proxies for Streaming Video Generation · off-topic: general attention-efficiency technique for streaming video generation, not specifically 3D, world models, character animation, or game engines (has a Tencent co-author, but topic does not fit the tracker's four pillars)
- 2610.29590 · CineEvolve: An Agentic Self-Evolution Framework for Cinematic Multi-Shot Video Generation · off-topic: general cinematic/multi-shot text-to-video generation and RL self-evolution framework, not specifically 3D, world models, character animation, or game engines (has a Tencent co-author, but topic does not fit)
- 2610.29168 · How Representational Priors Shape Generalization in World Action Models · no qualifying industry affiliation (all authors at Seoul National University)
- 2610.29088 · Causal world models under physical parameter shifts · no qualifying industry affiliation (authors at The City College of New York); also robotics/physics-flavored rather than games-specific
- 2610.28950 · HyperDrone: Simulation-to-Reality Transfer at Millions of Frames per Second · no qualifying industry affiliation (paper lists both authors' affiliation as University of California, Berkeley, with no industry co-author); drone-simulation/sim-to-reality framing rather than games-specific despite the ray-tracing rendering engine angle
- 2610.28779 · Second Thoughts: Exploring and Planning through Comparative Imagination in World Models · no qualifying industry affiliation (authors at University of Massachusetts Amherst and University of Massachusetts Lowell)
