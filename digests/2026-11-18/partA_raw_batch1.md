## FastFrames: Video Generation at Interactive Latency
- **arXiv:** 2611.23226 · https://arxiv.org/abs/2611.23226
- **Submitted:** 2026-11-17
- **Authors:** Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan Richter, Vladlen Koltun
- **Qualifying affiliation(s):** Apple — Gene Chou (paper states the work was completed during his internship at Apple); Apple is also listed as institution #1 in the paper's affiliation block, and Vladlen Koltun is an Apple researcher.
- **Categories:** cs.CV
- **Open release:** demo (project page: https://apple-aiml-research.github.io/ml-fastframes/); no code/weights link found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FastFrames is a family of fast autoregressive video diffusion models built for interactive-latency generation. The authors profiled existing systems and found components usually treated as fixed overhead — VAE decoding and KV-cache updates — account for over half of end-to-end latency, and redesigned both with lightweight alternatives.

**Purpose (≤3 sentences):** The goal is to make autoregressive video generation fast enough for fluid, real-time interaction (e.g., a user steering a camera or applying physics inputs while video is generated live), which current models are reported to be far too slow for.

**Breakthrough (≤3 sentences):** The authors report a 1.3B-parameter variant running at 36 ms/frame (28 responses per second) on a single B200 GPU, matching the quality of a state-of-the-art model nearly 8x slower. A 14B variant runs at 45 ms/frame (22 responses per second) on an 8×B200 node with better visual quality, and the authors demonstrate real-time interaction in camera-conditioned and physics-conditioned video generation.

**Tools & method (≤3 sentences):** The core technique is a latency-profiling-driven redesign of an autoregressive video diffusion pipeline, replacing the VAE decoder and the KV-cache update mechanism with lightweight alternatives rather than treating them as fixed costs.

**Limitation (≤3 sentences):** The abstract does not state explicit limitations, but the reported 14B configuration still requires an 8-GPU (B200) node to reach its stated frame rate.

---

## RFW-S: Everyday Deformable Objects with Independent Simulation Verification
- **arXiv:** 2611.23056 · https://arxiv.org/abs/2611.23056
- **Submitted:** 2026-11-17
- **Authors:** Jiarui Guo, Saining Zhang, Jiaying Wan, Jiawei Weng, Junhao Chen, Rui Zhang, Yuanbo Lyu, Zhiheng Lee, Peishuo Li, Jingrun Du, Weiqing Xiao, Weiyi Lin, Zenan Meng, Hu Wei, Lin Qu, Zongzheng Zhang, Hao Zhao, Chaojian Li
- **Qualifying affiliation(s):** Alibaba Group — listed as one of five institutions in the paper's affiliation block (alongside Tsinghua University, Nanyang Technological University, Nanjing University, and HKUST); the HTML rendering did not preserve a clean per-author mapping, but Alibaba Group is a stated affiliation for this author group.
- **Categories:** cs.RO, cs.CV
- **Open release:** demo (project page: https://sjijs.github.io/RFW-S_website/); no dataset/code download link confirmed on the arXiv page
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RFW-S is a dataset of 83,365 simulation-verified deformable 3D assets across 485 everyday object categories and five structural families (soft solids, cloth sheets, shells, garments, bags), built with an automated reference-guided 3D generation and physics-modeling pipeline. The authors add an independent verification framework that tests each object's physical behavior under interactions different from the ones used to calibrate it.

**Purpose (≤3 sentences):** The work targets the lack of scalable, physically grounded 3D asset construction and verification for deformable objects in existing simulation/robot-learning datasets.

**Breakthrough (≤3 sentences):** The authors report robotic grasping results (task success and object integrity) and sim-to-real replay of fragile-object manipulation using the dataset, positioning it as a scalable foundation for physically grounded simulation and robot learning.

**Tools & method (≤3 sentences):** The pipeline combines reference-guided 3D generation, structure-aware physical modeling, and LLM-assisted parameter estimation and calibration, followed by the independent verification framework described above.

**Limitation (≤3 sentences):** No explicit limitation of the authors' own method is stated in the fetched abstract.

---

## DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting
- **arXiv:** 2611.22805 · https://arxiv.org/abs/2611.22805
- **Submitted:** 2026-11-17
- **Authors:** Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang
- **Qualifying affiliation(s):** Baidu Research — Jialin Zhu
- **Categories:** cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DOOM-GS is presented as the first out-of-core optimization method designed specifically for massive-scale dynamic Gaussian Splatting, where spatio-temporal primitives exceed available GPU memory. Prior out-of-core GS methods handled only static scenes.

**Purpose (≤3 sentences):** The authors address the memory-management and training challenges created by dynamic primitives that move through space and time, which static out-of-core GS methods cannot handle.

**Breakthrough (≤3 sentences):** The authors report that DOOM-GS can reconstruct city-scale dynamic scenes with high quality on moderate hardware; they also contribute a new large-scale dynamic-GS dataset because, per the abstract, suitable datasets were lacking.

**Tools & method (≤3 sentences):** The method includes memory strategies for caching spatio-temporal primitives and a fast learning method for handling large primitive counts, with existing out-of-core approaches adapted as comparison baselines.

**Limitation (≤3 sentences):** No explicit limitation is stated in the fetched abstract.

---

## Evolve in Panorama, Render in View: Panoramic World State Evolution for Video World Models
- **arXiv:** 2611.22733 · https://arxiv.org/abs/2611.22733
- **Submitted:** 2026-11-17
- **Authors:** Longtao Jiang, Mingfei Han, Jianmin Bao, Tingjun Dai, Jinjie Wei, Zhiran Zhang, Xin Tao, Zhihui Li, Salman Khan, Xiaojun Chang
- **Qualifying affiliation(s):** Kuaishou Technology — the paper's affiliation block lists Mohamed bin Zayed University of Artificial Intelligence and Kuaishou Technology as the only two institutions; Xin Tao is independently confirmed (public researcher profile) as Senior Researcher/Tech Lead in Kuaishou's Visual Generation ("Kling") Group. Exact per-author mapping was not fully resolvable from the HTML rendering.
- **Categories:** cs.CV
- **Open release:** none yet (abstract states "code, models, and data will be released")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PanoEvo is a video world model that keeps the entire scene evolving even when the camera isn't looking at parts of it, using a Panoramic Evolver that updates scene state in the latent space of a panoramic video diffusion model so every viewing direction changes consistently over time. A Perspective Renderer then reads that state to produce sharp perspective views.

**Purpose (≤3 sentences):** The authors target a gap in current video world models, which they say only update what the camera currently sees rather than maintaining a persistently evolving world.

**Breakthrough (≤3 sentences):** The authors report the best overall score among 23 publicly evaluated models on WRBench and the highest total score on STEVO-Bench.

**Tools & method (≤3 sentences):** The Evolver is trained coarse-to-fine as an image-to-panoramic-video model on PanoEvo-Data, a new event-centric dataset built from real 360° videos; the Perspective Renderer, built on a perspective video diffusion model, reads world state via latent-space projection and direction-restricted cross-attention.

**Limitation (≤3 sentences):** No explicit limitation is stated in the fetched abstract.

---

## FVScore: Specification-Driven Neuro-Symbolic Video Evaluation
- **arXiv:** 2611.22673 · https://arxiv.org/abs/2611.22673
- **Submitted:** 2026-11-17
- **Authors:** Do Xuan Long, Long T. Le, Yiwen Song, Min-Yen Kan, Tomas Pfister, Yale Song
- **Qualifying affiliation(s):** Google Cloud AI Research — Long T. Le, Yiwen Song, Tomas Pfister, Yale Song
- **Categories:** cs.CV, cs.AI
- **Open release:** demo (project page: https://dxlong2000.github.io/FVSCORE/); no code/weights link found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FVScore is a neuro-symbolic framework for evaluating specification-driven video generation. It converts each video into explicit propositions covering both the prompt's stated requirements and unstated physical, temporal, and cross-modal constraints, then checks them with specialized perception tools.

**Purpose (≤3 sentences):** The work targets evaluation of video-generation outputs more faithfully than existing holistic or agent-based evaluators, particularly for complex, multi-event videos.

**Breakthrough (≤3 sentences):** The authors report that FVScore correlates better with human judgments than holistic and agent-based evaluators on public and complex multi-event benchmarks.

**Tools & method (≤3 sentences):** Soft temporal operators inspired by Linear Temporal Logic evaluate confidence traces produced by the perception tools, and a significance-aware calibration step filters these down to perceptually significant violations, producing a timestamp- and evidence-grounded report.

**Limitation (≤3 sentences):** No explicit limitation is stated in the fetched abstract.

---

# Near-misses
- 2611.22880 · Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving (AgentWorld) · no industry co-author — all four authors affiliated solely with Shanghai Jiao Tong University (MoE Key Lab of AI); accepted at NeurIPS 2026.
- 2611.22769 · ForceBody: Force-Paired Parametric Body Motion with Torque Uncertainty · no industry co-author — authors affiliated with Michigan State University, UNC Chapel Hill, and one independent researcher; no qualifying/comparable company found.
- 2611.22717 · PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation · no qualifying co-author — sole listed affiliation "Anorak Games" is a $5M pre-seed AI-generative-video startup (per press coverage), not a tracked company or a comparable top-tier industry lab.
