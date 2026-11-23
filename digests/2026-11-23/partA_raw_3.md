## Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction
- **arXiv:** 2611.25061 · https://arxiv.org/abs/2611.25061
- **Submitted:** 2026-11-18 (v1)
- **Authors:** Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum, William T. Freeman, Vincent Sitzmann, Yilun Du, Ayush Tewari
- **Qualifying affiliation(s):** Google DeepMind — Mark Hamilton (other authors: Harvard, MIT, Cambridge)
- **Categories:** cs.CV, cs.LG, cs.RO
- **Open release:** demo (project page, no stated code/weights) — https://amanikiruga.github.io/infer3d-site/

**Summary (≤3 sentences):** Infer3D is an inverse generative modeling framework for monocular 3D reconstruction that recovers the latent variables of a generative model to best match a single input image, rather than using feedforward amortized inference. It couples a generative image prior with a frozen 3D lifting network to keep outputs on a valid, multi-view-consistent 3D manifold and avoid degenerate flat results.
**Purpose (≤3 sentences):** Feedforward 3D reconstruction networks degrade on out-of-distribution (OOD) viewpoints and scene conditions not seen during training. The authors aim to generalize better to unfamiliar viewpoints by mirroring the top-down generative inference strategy that cognitive science attributes to human 3D perception.
**Breakthrough (≤3 sentences):** The authors report Infer3D achieves superior OOD reconstruction accuracy compared to feedforward networks trained on equal or larger datasets, across controlled synthetic and real-world tasks. They also introduce an adaptive inference strategy that spends more test-time compute on ambiguous OOD examples while routing in-distribution inputs efficiently, which they liken to humans taking longer on confusing stimuli.
**Tools & method (≤3 sentences):** The method optimizes the latent variables of a generative image model against the monocular input, constrained by a frozen 3D lifting network that enforces multi-view consistency, with Gaussian-style decoders for novel views (per the project page). Compute is allocated adaptively at test time based on how ambiguous/OOD the input appears.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations. The optimization-based (inverse) inference approach inherently trades off speed for robustness relative to feedforward networks (observed, not stated).

---

## FastFrames: Video Generation at Interactive Latency
- **arXiv:** 2611.23226 · https://arxiv.org/abs/2611.23226
- **Submitted:** 2026-11-17 (v1)
- **Authors:** Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan R. Richter, Vladlen Koltun
- **Qualifying affiliation(s):** Apple — the paper's affiliation list names Apple and Cornell University, and a footnote states "This work was completed during Gene's internship at Apple"; the HTML extraction did not preserve which superscript ties each remaining author to which institution, so the full per-author mapping is unresolved beyond this.
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** FastFrames is a family of fast autoregressive video diffusion models aimed at interactive latency for applications such as camera-conditioned and physics-conditioned video generation. The authors profile state-of-the-art autoregressive video diffusion inference and replace components they find to dominate latency with lightweight alternatives.
**Purpose (≤3 sentences):** Existing autoregressive video diffusion models are, per the authors, orders of magnitude too slow for fluid interactive use, despite being a promising medium for interactive visual experiences.
**Breakthrough (≤3 sentences):** The authors report their 1.3B variant runs at 36 ms per frame (28 responses per second) on a single B200 GPU while matching the generation quality of a state-of-the-art model nearly 8x slower. Their 14B variant runs at 45 ms per frame (22 RPS) on an 8x B200 GPU node with, they state, significantly better visual quality and realism.
**Tools & method (≤3 sentences):** Profiling the inference pipeline, the authors find that VAE decoding and KV-cache updates — often treated as fixed implementation details — account for over half of end-to-end latency, and they replace these with lightweight alternatives. They demonstrate the resulting system on camera-conditioned and physics-conditioned video generation.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations. Reported speeds rely on high-end B200 GPU hardware (observed, not stated).

---

## Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality (EVA-RSI)
- **arXiv:** 2611.23890 · https://arxiv.org/abs/2611.23890
- **Submitted:** 2026-11-18 (v1)
- **Authors:** Yu Yuan, Ruizhou Ding, Shaoheng Fang, Stanley H. Chan, Zhuo Chen
- **Qualifying affiliation(s):** Roblox — Yu Yuan (Roblox internship + Purdue), Ruizhou Ding (Roblox), Shaoheng Fang (Roblox internship + UT Austin), Zhuo Chen (Roblox)
- **Categories:** cs.AI
- **Open release:** none stated

**Summary (≤3 sentences):** EVA-RSI is a multi-agent recursive self-improvement (RSI) framework for training video evaluators that judge the temporal quality (physics, smoothness, dynamics) of generated video. It builds a fixed proxy exam from construction-defined edits (e.g., temporal reversal, frame dropping) to supply supervision without human annotation, anchored by a small human-labeled real-video set.
**Purpose (≤3 sentences):** RSI has worked well in math/coding, where explicit verifiers give reliable single-goal feedback, but video evaluation has no such verifier and must balance multiple dimensions at once where a gain on one can cost another. The authors aim to adapt RSI to this harder, multi-dimensional, verifier-free setting.
**Breakthrough (≤3 sentences):** Starting from Qwen3-VL-8B, the authors report EVA-RSI improves motion evaluation (largest gain on smoothness) with gains that carry over to defect types never seen during the run, and achieves the highest observed scores among 21 tested models on the dynamics subsets of public benchmarks. Used as an RL reward, it increases generated motion and earns higher human preference; a data-selection pipeline using it also increases motion.
**Tools & method (≤3 sentences):** Each quality dimension has its own LLM proposer agent; a leader agent coordinates proposals and a Nash bargaining rule selects updates that balance progress across dimensions. Humans design the proxy exam, review candidate changes, and revise the curriculum between stages.
**Limitation (≤3 sentences):** The authors state video evaluation has no explicit verifier and must judge many dimensions simultaneously, where improving one can cost another — the core difficulty the method is built to manage rather than fully eliminate. The curriculum still requires human design and review between stages.

---

## EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation
- **arXiv:** 2611.23670 · https://arxiv.org/abs/2611.23670
- **Submitted:** 2026-11-18 (v1)
- **Authors:** Yonghan Lee, Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Dinesh Manocha, Yatong An
- **Qualifying affiliation(s):** Meta Reality Labs — Zachary Willms, Kun Liu, Pushkar Anand, Ali Behrooz, Dmitri Model, Yatong An (corresponding author); other authors: University of Maryland, College Park
- **Categories:** cs.CV
- **Open release:** demo (project page, no stated code/weights) — https://lyhan12.github.io/eyedit

**Summary (≤3 sentences):** EyeDiT is an anatomy-grounded, multi-modal 3D eye generation and simulation model trained on optical coherence tomography (OCT), labeled anatomy point clouds, and near-eye images, for synthesizing eye-tracking (ET) data for AR/VR. A Multi-Modal Anatomy VAE first encodes an anatomy-aware latent from all input modalities, then an "Eye Latent DiT" generates latents conditioned on optical axis, pupil position/radius, and subject identity.
**Purpose (≤3 sentences):** Existing synthetic eye generators are largely image-centric and lack high-quality underlying 3D eye anatomy, limiting control mainly to gaze direction and providing no anatomical labels. EyeDiT targets richer, anatomically grounded control and labeling for ET development in AR/VR.
**Breakthrough (≤3 sentences):** The authors report EyeDiT outperforms previous eye-image synthesis models in novel-view synthesis (24.9 dB vs. 21.8 dB PSNR from a single view). A public ET neural network trained on EyeDiT's synthetic data shows a smaller sim-to-real gaze-error gap (3.5° vs. 8.4°) than when trained on other generators' data, approaches a network trained on real data, and improves further (2.3° vs. 2.6°) when combined with real data.
**Tools & method (≤3 sentences):** The pipeline trains a Multi-Modal Anatomy VAE encoding OCT, anatomy point-cloud, and near-eye-image inputs into an anatomy-aware latent, then trains an Eye Latent DiT to generate latent samples conditioned on optical axis, pupil position/radius, and subject identity, paired with Gaussian decoders for novel-view simulation.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations. The approach depends on OCT, point-cloud, and near-eye-image training data, which are likely more costly to collect than ordinary images (observed, not stated).

---

## RFW-S: Everyday Deformable Objects with Independent Simulation Verification
- **arXiv:** 2611.23056 · https://arxiv.org/abs/2611.23056
- **Submitted:** 2026-11-17 (v1; v2 on 2026-11-18)
- **Authors:** Jiarui Guo, Saining Zhang, Jiaying Wan, Jiawei Weng, Junhao Chen, Rui Zhang, Yuanbo Lyu, Zhiheng Lee, Peishuo Li, Jingrun Du, Weiqing Xiao, Weiyi Lin, Zenan Meng, Hu Wei, Lin Qu, Zongzheng Zhang, Hao Zhao, Chaojian Li
- **Qualifying affiliation(s):** Alibaba Group — Zenan Meng (confirmed via corresponding author email at @alibaba-inc.com, matched to the paper's listed "Alibaba Group" affiliation); other listed affiliations: Tsinghua University, Nanyang Technological University, Nanjing University, HKUST
- **Categories:** cs.RO, cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** RFW-S is a large-scale dataset of 83,365 simulation-verified deformable-object assets spanning 485 everyday categories across five structural families (soft solids, cloth sheets, shells, garments, bags), built for robotic simulation. An automated pipeline combines reference-guided 3D generation, structure-aware physical modeling, and LLM-assisted parameter estimation/calibration.
**Purpose (≤3 sentences):** Existing 3D asset collections for robotic simulation emphasize visual diversity but leave scalable physical construction and verification of deformable objects largely unsolved. RFW-S targets assets with executable physical properties and realistic interaction behavior at scale.
**Breakthrough (≤3 sentences):** The authors introduce an independent simulation-verification framework that evaluates object behavior under interactions distinct from those used for parameter calibration, and report this characterizes deformable responses across different physical configurations. They further demonstrate sim-to-real replay of fragile-object manipulation and evaluate robotic grasping in terms of both task success and object integrity.
**Tools & method (≤3 sentences):** The pipeline integrates reference-guided 3D asset generation, structure-aware physical modeling, and LLM-assisted parameter estimation and calibration, followed by independent simulation verification on held-out interaction types. Evaluation covers robotic grasping success, object integrity, and sim-to-real replay for fragile objects.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations.

---

## Efficient World-Model Planning via Physics-Guided Search Distillation (PGSD)
- **arXiv:** 2611.24171 · https://arxiv.org/abs/2611.24171
- **Submitted:** 2026-11-18 (v1; v2 on 2026-11-19)
- **Authors:** Hongyu Zhang, Xiaoshuai Hao, Heye Huang, Qingwen Meng, Wenjun Shi, Jianao Xu, Xin Hu, Xuanru Jin, Jingyi Zhang, Baicang Guo
- **Qualifying affiliation(s):** Xiaomi Corporation — Xiaoshuai Hao. **FLAG: borderline** — Xiaomi is not on the SKILL.md tracked-company list; kept per the "unsure, comparable-standing" rule since Xiaomi runs large in-house AI/robotics research comparable to other flagged companies (e.g. Huawei, Samsung). Other authors: Yanshan University, KAIST, Tsinghua University, Beijing Automotive Technology Center Co., Ltd.
- **Categories:** cs.RO, cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** PGSD is a single-view world-model planning framework for autonomous driving that combines future-scene representations with execution feedback to repair trajectories that would otherwise violate road boundaries. The pretrained planner and rewarder remain frozen, and no future scenes are generated online at inference.
**Purpose (≤3 sentences):** The authors note that accurate future prediction in driving world models does not guarantee road-compliant execution, and when every candidate trajectory violates road boundaries, simple re-ranking cannot select a feasible one. PGSD targets verified, beyond-pool trajectory repair for this failure case.
**Breakthrough (≤3 sentences):** The authors report single-view PGSD achieves 90.97 PDMS on NAVSIM v1, exceeding all compared single-view planners, while retaining 73.2% of the search teacher's PDMS gain over execution-aware selection alone. On NAVSIM v2 navhard it reaches 38.96 EPDMS, improving on WorldDrive by 11.24 points (40.5%), and the distilled student replaces up to ten search rollouts with a single verification rollout per repair trigger.
**Tools & method (≤3 sentences):** Three components: Execution-Aware Selection checks ego-vehicle road compliance under simulated execution; a Clearance-Aware Search Teacher generates beyond-pool corrections favoring larger minimum road-boundary clearance; and a Future-Conditioned Repair Student predicts a single correction from rewarder features and execution feedback. The authors also report qualitative zero-shot transfer evidence on HUGSIM Hard examples.
**Limitation (≤3 sentences):** The zero-shot transfer evidence on HUGSIM Hard is described as qualitative rather than quantitative (observed). The abstract does not state further limitations.

---

## DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting
- **arXiv:** 2611.22805 · https://arxiv.org/abs/2611.22805
- **Submitted:** 2026-11-17 (v1)
- **Authors:** Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
- **Qualifying affiliation(s):** Baidu Research — Jialin Zhu; other authors: University College London
- **Categories:** cs.GR
- **Open release:** none stated (a new evaluation dataset is contributed but no link is given in the abstract)

**Summary (≤3 sentences):** DOOM-GS is, per the authors, the first out-of-core optimization method designed specifically for massive-scale dynamic 3D Gaussian Splatting, handling scenes whose primitives exceed GPU memory. It introduces memory-management strategies for caching spatio-temporal primitives and a fast learning method for large numbers of primitives.
**Purpose (≤3 sentences):** Prior out-of-core Gaussian Splatting training assumes static scenes; dynamic GS primitives that move in space and time break the memory-management assumptions those methods rely on, which DOOM-GS targets.
**Breakthrough (≤3 sentences):** The authors state DOOM-GS makes it possible to reconstruct city-scale dynamic scenes with high quality on moderate hardware. Because no directly comparable methods exist, they adapted several closely related methods for comparison and report improvements over these adapted baselines.
**Tools & method (≤3 sentences):** The method combines memory-management strategies that optimize caching for spatio-temporal Gaussian primitives with a fast learning method for large primitive counts. The authors also contribute a new dataset for evaluation, citing a lack of suitable existing datasets for large-scale dynamic GS.
**Limitation (≤3 sentences):** The authors note there are no directly comparable prior methods, requiring adaptation of related methods for comparison, and no suitable existing large-scale dynamic-GS dataset, requiring a new contributed one — both indicating limited external benchmarking for this problem setting.

# Near-misses
- 2611.25134 · GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning · academic (University of Minnesota, Twin Cities) plus Cisco, a non-qualifying industry co-author not comparable to the tracked 3D/graphics/gaming labs; "Meta" regex match traced to the "Meta-World" benchmark name, not an affiliation
- 2611.23825 · Learning Martial Arts Motion Skills for Animating Opponents in VR Sparring Games · academic only (Arizona State University, Rice University), no qualifying industry co-author; "Meta" regex match traced to the "Meta Quest" headset target hardware, not an affiliation
- 2611.23416 · OCLDA-GS: Object-Centric Local Deformation-Aware Gaussian Streaming · academic only (University of Southern Mississippi, University of Utah), no qualifying industry co-author; "Google" regex match traced to the "Google Immersive" dataset name used for evaluation, not an affiliation
- 2611.22880 · Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving (AgentWorld) · academic only (Shanghai Jiao Tong University, MoE Key Lab of AI), no qualifying industry co-author; "Meta" regex match not traceable to any stated affiliation
- 2611.22769 · ForceBody: Force-Paired Parametric Body Motion with Torque Uncertainty · academic only (Michigan State University, University of North Carolina at Chapel Hill) plus one independent researcher, no qualifying industry co-author
