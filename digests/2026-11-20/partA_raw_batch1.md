## One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning
- **arXiv:** 2611.26617 · https://arxiv.org/abs/2611.26617
- **Submitted:** 2026-11-19
- **Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou
- **Qualifying affiliation(s):** Tencent — listed in the paper's affiliation block alongside Show Lab/NUS, A*STAR, and Stanford for the first five authors (Jiang, Sun, Li, Gu, Zhang); the HTML affiliation block does not map "Tencent" to one specific name, but the affiliation itself is explicitly present (not a false-match); FLAG: borderline (exact author-to-Tencent mapping unverifiable from the rendered page)
- **Categories:** cs.CV (primary), cs.AI, cs.LG, cs.RO
- **Open release:** code (https://github.com/showlab/O2LaF), project page (https://showlab.github.io/o2laf)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes O²LaF, a self-supervised latent-action framework that initializes both an inverse-dynamics encoder (IDM) and a forward-dynamics video generator (FDM) from the same pretrained video diffusion transformer (Wan2.2-TI2V-5B), trained end-to-end through a compact latent bottleneck, with no action labels required. The FDM is causal and action-conditioned and functions as a world model: actions inferred from one video can drive generation from a different first frame.
**Purpose (≤3 sentences):** Prior latent-action learning largely trains inverse- and forward-dynamics models from scratch or on frozen features, leaving a gap between the two and underusing pretrained video generators. The authors ask whether one pretrained video diffusion transformer can serve both roles at once.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art few-shot action probing on camera navigation (e.g., 94.37% joint exact-match for 3rd-person at k=50) and robot manipulation (EEF R² of 0.277 vs. 0.149 for DreamDojo), plus better zero-shot action transfer across visual contexts and embodiments than AdaWorld and Olaf-World on their reported metrics. They also report competitive results extending the framework to V-JEPA2 as the prior.
**Tools & method (≤3 sentences):** The IDM uses learnable action queries reading only transition endpoint frames, producing a 32-D latent action via a variational Gaussian head; the FDM keeps the initial frame clean, predicts future frame velocities jointly with latent actions injected via AdaLN, and trains with a flow-matching loss plus a small KL term. Training data was MiraData (navigation) and EgoDex (egocentric human demonstrations, manipulation), evaluated on the MIND benchmark and DreamDojo's In-lab Eval.
**Limitation (≤3 sentences):** The authors state future work includes improving the interpretability of the learned latent-action space and extending video-predictive dynamics to efficient planning and closed-loop control.

## Coda-DaVinci: Reimagining Video Generation with Code2Video
- **arXiv:** 2611.26595 · https://arxiv.org/abs/2611.26595
- **Submitted:** 2026-11-19
- **Authors:** Yiyan Ji, Qixun Wang, Yang Shi, Zhuoran Zhang, Yifan Xu, Tengfei Liu, Yuqi Tang, Xiaohan Zhang, Shujie Li, Jiafu Tang, Xuanyu Zhu, Xinyu Liu, Yan He, Yushuo Guan, Zihao Wang, Xianghua Ying, Shixuan Liu, Haotian Wang, Wenjing Yang, Zhaoxiang Zhang, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
- **Qualifying affiliation(s):** Kuaishou — Yiyan Ji, Qixun Wang, Yang Shi, Yushuo Guan, Zihao Wang, Yuanxing Zhang, Pengfei Wan (listed under "KlingAI Research," Kuaishou's Kling AI research division)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies Code2Video, where a coding agent builds a 3D proxy scene (in Blender) to guide video generation, and runs controlled experiments plus blinded human evaluation to see how proxy granularity, physics simulation, and prompting affect output quality. Building on these findings, it proposes Coda-DaVinci, an agentic framework that routes each task between proxy-guided and direct generation, varies modeling detail per entity, and uses a multi-agent harness with an independent acceptance/repair agent.
**Purpose (≤3 sentences):** The authors argue video models still struggle with detailed instructions, state persistence across camera revisits, and physical plausibility, and that existing 3D-proxy pipelines don't adapt proxy detail or prompting to the task. They aim to characterize when and how fine-grained 3D proxies actually help.
**Breakthrough (≤3 sentences):** The authors report Coda-DaVinci reaches a 91.42 checklist score and 11.08% WER on VTR (vs. 59.21% WER for direct generation), the highest reported scene-ID score (1.011) on R2M, and a 60.77 score on the World Models' Last Exam in Physics benchmark (second only to a Claude + Blender baseline at 65.52). It underperforms direct generation on some realism/instruction-following scores (T2AV-Compass) and on long-video transition stability and scene-setting adherence.
**Tools & method (≤3 sentences):** Coda-DaVinci routes tasks needing precise scene/motion control to 3D modeling and human-motion-centric tasks toward direct generation, uses coarse proxies for humans and medium-detail proxies for environments/objects, and has an agent inspect the rendered proxy to write prompts linking subjects to proxy entities. It used Seedance 2.5 for video synthesis, GPT-6-Astra and Claude Opus 5.5 as coding agents, MiniMax H3-Context-IR for prompt enhancement, and Blender 5.2.1 with Cycles/CUDA rendering at 24 FPS/720p.
**Limitation (≤3 sentences):** The authors report weaker motion naturalness and physical plausibility on VGIF-Bench (complex human/object motion), lower transition stability on LongAV-Compass, and weaker scene-setting adherence on WBench versus direct generation. They also note their empirical human-evaluation set was small (94 samples) because some samples were excluded by Seedance's privacy policy, and Blender-based generation costs roughly double the agent tokens of a Three.js alternative.

## Plan4D: Generative Plannable 4D Worlds
- **arXiv:** 2611.26516 · https://arxiv.org/abs/2611.26516
- **Submitted:** 2026-11-19
- **Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- **Qualifying affiliation(s):** Alibaba — Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng (listed under "AMAP, Alibaba Group")
- **Categories:** cs.CV
- **Open release:** project page (https://fogradio.github.io/plan4d-project); accepted at NeurIPS 2026
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Plan4D is a world model that, given an observed scene and text-specified actions, predicts future RGB video together with dense 4D geometry — depth, cameras, point clouds, and scene flow. It combines a pretrained video generator (LongCat-Video, built on the Wan 2.1 VAE) with a 3D reconstructor (Depth Anything 3) via a model-stitching design, with an added scene-flow head.
**Purpose (≤3 sentences):** The authors note most world models focus on RGB synthesis without explicit 4D geometry, and that action-conditioned datasets with dense 3D annotations are scarce. They aim to keep geometric and video-generation priors separate and connect them through a stitched latent model rather than training jointly from scratch.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art results on synthetic and real-world benchmarks for generative 4D modeling of environmental reactions, with examples including an EPE of 0.97 on MOVi-F scene flow and, on HoiGen, AbsRel of 0.1125 and RRA@5 of 0.9809 versus 1.850 AbsRel/0.9256 RRA@5 for the TesserAct baseline. An ablation shows the full RGB+geometry training objective gives the best subject/background consistency compared with using either loss alone.
**Tools & method (≤3 sentences):** A DPT-style scene-flow head is added to a frozen Depth Anything 3 (DA3) backbone; a learnable 3D convolution stitches upsampled Wan-VAE video latents into a selected DA3 encoder block, and the stitched decoder is trained via teacher-student distillation plus ground-truth 3D supervision before joint training with a flow-matching loss and a geometry loss from the frozen stitched decoder. Training data spanned PointOdyssey, Dynamic Replica, Virtual KITTI 2, BlinkVision, OmniWorld-Game, ScanNet++, MVS-Synth, and a subset of Action100M, using 16 H100 GPUs for the scene-flow head and 64 H20 GPUs for the stitched-decoder/DiT stages.
**Limitation (≤3 sentences):** The paper's table of contents lists a dedicated limitations appendix, but its content was not accessible in the retrieved text, so no specific stated limitations could be verified beyond what the method and results sections imply.

## ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step
- **arXiv:** 2611.26389 · https://arxiv.org/abs/2611.26389
- **Submitted:** 2026-11-19
- **Authors:** Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
- **Qualifying affiliation(s):** Kuaishou — Yiming Gao, Pengfei Wan, Kun Gai (listed under "KlingAI Research")
- **Categories:** cs.CV
- **Open release:** project page (https://kevin-thu.github.io/ViDecide)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes ViDecide, which trains video diffusion models to predict state transitions causally, one segment at a time, and to decide when to stop via a learned end-of-sequence frame, rather than treating a solution as one fixed-length clip. It also introduces Corrective Fine-tuning (CFT), which steers failed decision points toward the model's own successful continuations without policy-gradient optimization.
**Purpose (≤3 sentences):** The authors argue leading video generators break physical/logical rules in multi-step reasoning and planning even after reasoning-data training or diffusion RL, because standard training generates clips jointly rather than as a sequence of decisions, and video-level rewards give poor credit assignment. ViDecide targets this gap across abstract games, planning tasks, and robot planning.
**Breakthrough (≤3 sentences):** The authors report an average strict success rate of 83.8%, versus 23.3% for standard fine-tuning and 67.8% for the strongest prior method, with causal generation alone contributing +48.2 points and a decision-focused noise schedule adding +37.0 points. On their new RoboTwin-Plan benchmark, ViDecide solves 78.0% of tasks versus 63.9% for the strongest prior method, and it generalizes to larger Sokoban/FlowFree boards and unseen robot layouts.
**Tools & method (≤3 sentences):** The method combines causal diffusion with adaptive termination (a learned EOS frame), a decision-focused noise schedule that shifts training mass toward high-noise timesteps, and CFT, which branches from rollout failure points and trains the failed noise toward successful continuations mixed with expert data. Experiments used Wan2.2-5B and a 132M-parameter DiT-B trained from scratch, on VideoRLVR (Maze, FlowFree, Sokoban), VBVR-MultiStep, and the new RoboTwin-Plan benchmark built in the RoboTwin 2.0 simulator.
**Limitation (≤3 sentences):** The authors state the model is trained on one benchmark at a time and relies on rule-based verifiers for post-training, and they plan to extend it to broader reasoning data, learned verifiers, and real-world robot planning.

## SpecWM: Turning Verification into Refinement for Streaming World Models
- **arXiv:** 2611.26211 · https://arxiv.org/abs/2611.26211
- **Submitted:** 2026-11-19
- **Authors:** Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma
- **Qualifying affiliation(s):** Tencent — Jiaming Li, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SpecWM is a training-free inference framework for streaming video world models that verifies draft video chunks using the target model's own latent velocity field rather than an external reward model, and reuses that verification as a correction signal. Two thresholds route each chunk to Accept, one-step Refine, three-step Refine, or Reject.
**Purpose (≤3 sentences):** The authors note larger streaming world models give better quality and control but run slowly, while smaller draft models run fast but less accurately, and existing reward-based speculative methods regenerate rejected chunks wholesale with no reusable correction. SpecWM aims to turn verification itself into a source of refinement.
**Breakthrough (≤3 sentences):** On WBench Navigation (LingBot-World 2.0, 1.3B draft/14B target), the authors report a 1.63× speedup over target-only generation while raising NavScore from the draft's 75.99 to 85.63, versus 85.49 for target-only. On their new LongSpecBench (509-frame multi-turn rollouts), they report a 1.67× speedup with comparable or better WMQ/QES scores than target-only generation.
**Tools & method (≤3 sentences):** Each draft chunk gets one final-stage target-model probe whose prediction can be committed directly or used as a seed for 2-3 further target denoising steps, with refinement intensity tied to control-change transitions and a fallback to target-only generation after two consecutive rejections. Evaluation used WBench Navigation, the authors' new LongSpecBench, and Hy-Nomas-Bench, with distilled LingBot-World 2.0 causal-fast models and Hy-Nomas 8B.
**Limitation (≤3 sentences):** The paper has no dedicated limitations section, but the text implies thresholds are calibrated on a small set of 20 cases and then fixed, and draft/target models must share a latent space, chunk length, and control interface, with cross-model latent alignment named as future work.

## Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency
- **arXiv:** 2611.26040 · https://arxiv.org/abs/2611.26040
- **Submitted:** 2026-11-19
- **Authors:** Zhihao Hu, Jianqi Ma, Jun Zhang, Jiayang Bai, Haifeng Shi, Yanxiang Zhuang, Zhongqian Sun, Weidong Zhang, Wei Yang
- **Qualifying affiliation(s):** Tencent — all listed authors (affiliation block lists "Tencent AIPD" for the group)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Streaming-AAA is a system for controllable, long-horizon generation of AAA-quality game video for interactive game simulation, using Genshin Impact as its primary test game. The authors report 1080p gameplay generation at 43 FPS with 198 ms end-to-end latency on NVIDIA A800 GPUs.
**Purpose (≤3 sentences):** The authors argue prior streaming world models for games either degrade over long play sessions or cannot combine high resolution, high frame rate, and low latency simultaneously. They aim to close this gap for practical, playable, long-horizon game-video generation.
**Breakthrough (≤3 sentences):** The authors report a VBench average of 0.832 versus 0.747-0.810 for compared baselines (Lingbot, YUME, Matrix Game 3.0, HY-World1.5), and an imaging-quality score of 0.677 versus 0.589 for HY-World1.5. Baselines ran at 480p-720p and 2.1-6.7 FPS with 6.6-11.3 s latency, versus Streaming-AAA's 1080p/43 FPS/198 ms, and the authors report no visible quality collapse over a one-hour stress test.
**Tools & method (≤3 sentences):** The system uses a causal video VAE (4×16×16 compression with a Pixel Shuffle decoder layer) feeding a factorized 3D-UNet latent diffusion backbone, pretrained with diffusion forcing over clips growing from 64 to 640 frames, then post-trained with distribution matching distillation (DMD) and a hybrid 30-token memory (22 sparse long-term, 8 recent short-term) for two-step inference. Training data was an in-house collection of about 22,000 one-minute 1080p/30fps videos (~40 million frames) gathered via an automated agent-driven recording pipeline in-game, with Qwen-VL used to estimate weather/time-of-day labels.
**Limitation (≤3 sentences):** The authors state the model is trained on data from a single game, so generalization to other titles, art styles, or mechanics is limited, and they describe a universal game-generation model without per-game fine-tuning as an open challenge. They also report motion smoothness marginally lower than baselines (0.982 vs. 0.983-0.988), attributed to fast motion in their rollouts.

# Near-misses
- 2611.26629 · Posterior Matching Distillation · off-topic: text-to-image diffusion distillation (SDXL/FLUX few-step sampling), not 3D content/world models/character animation/game engines, despite a genuine NVIDIA co-author affiliation (Julius Berner, Arash Vahdat)
- 2611.26493 · SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention · no industry-affiliated author (all authors listed under CVLab, EPFL, Switzerland; the "NVIDIA" lead was not confirmed in the author/affiliation block)
- 2611.26464 · Monte Carlo Pass Search for Setpieces · off-topic: soccer corner-kick/set-piece analytics using a sports "world model," not 3D content/world models/character animation/game engines in the tracked sense; also no industry affiliation found (single author, Andrew Kang, no stated institution; the "Google" lead was not confirmed)
- 2611.26334 · Online Temporal Rotations for 2-Bit KV-Cache Quantization in Video Diffusion Transformers · no industry-affiliated author (all authors listed under MIT Operations Research Center; the "Tencent" lead was not confirmed in the author/affiliation block)
- 2611.25847 · TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling · off-topic: generic few-step flow-matching sampling acceleration for image (FLUX.1-dev) and video (Wan2.2-TI2V-5B) diffusion, not specific to 3D content/world models/character animation/game engines
