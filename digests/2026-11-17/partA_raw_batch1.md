## Reference Forcing: Long Video Generation with Region-Guided Drift Correction
- **arXiv:** 2611.21559 · https://arxiv.org/abs/2611.21559
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Sheng Zhao, Haitian Zheng, Weikai Lin, Junjie Zhao, Yuhao Zhu
- **Qualifying affiliation(s):** Adobe — Haitian Zheng (co-authors otherwise at University of Rochester)
- **Categories:** cs.CV
- **Open release:** code/demo — project page with visualizations and code at https://zhaosheng-thu.github.io/reference-force/ (no model weights mentioned)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Long autoregressive video generators drift in subject/background appearance over time because they are distilled over short windows and KV-cache history can itself have drifted. The authors propose Reference Forcing, which anchors generation to the very first frames as a ground-truth appearance reference instead of relying on potentially-drifted history. It reports state-of-the-art long-video subject/background consistency, with the advantage growing as videos get longer.

**Purpose (≤3 sentences):** To stop long (minutes-scale) autoregressively generated videos from losing a consistent subject/background appearance over time, a known failure of distillation-based fast video generators.

**Breakthrough (≤3 sentences):** The authors report that a teacher model forces each region of a new frame to attend to the matching region in the initial frames (found via off-the-shelf segmentation), then distills this into a student attention path needing no external models at inference, plus a "value correction" step that pulls drifted KV-cache values back toward the clean initial-frame values. On 128 MovieGenBench prompts at 120 seconds, they report 97.27 subject-consistency vs. 97.06 for the LongLive baseline, ranking first overall on VBench-Long at 30s and 60s, and winning 78% of pairwise VLM-judge comparisons against LongLive.

**Tools & method (≤3 sentences):** Built on top of frozen LongLive-1.3B and Self-Forcing 1.3B base models (only the new "anchor path" is trained), evaluated with VBench-Long metrics, DINOv2-based L-Consistency, MiraBench tracking strength, a 7-participant user study, and a VLM judge, against baselines MemRoPE, LongLive-RAG, ∞-RoPE, and Deep Forcing.

**Limitation (≤3 sentences):** The authors state that only the first chunk serves as a reference, so objects entering the scene later have no reference frame to anchor to, and updating the reference mid-generation is left to future work; they also note slightly lower imaging quality than LongLive (attributed to anchor-path averaging smoothing fine textures) and that the teacher is costly to run, and scenes with several similar subjects remain difficult since the teacher's segmentation tracks a single subject.

## DuoFlow: Towards Synchronized Speech and Motion Generation with Fine-Grained Control
- **arXiv:** 2611.21530 · https://arxiv.org/abs/2611.21530
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Jun Dong, Ronghui Li, Zhongyuan Hu, Yunqi Zhao, Lijie Guo, Ruizhang Xu, Di Kang, Linchao Bao, Xiu Li
- **Qualifying affiliation(s):** Tencent — Di Kang, Linchao Bao (other co-authors at Tsinghua University)
- **Categories:** cs.CV
- **Open release:** none — only a project page (https://jundong-dev.github.io/DuoFlow-project-page/) is mentioned; no code or weights release stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Existing joint speech-motion generation models only implicitly condition on transcript semantics or speech features, giving little explicit control over motion hierarchy, body parts, or vocal style. The authors build MotionSpeech, a new benchmark with transcripts, voice-style descriptions, and two-level hierarchical motion conditions, and propose DuoFlow, a dual-stream latent flow transformer that jointly denoises speech and motion. DuoFlow is reported to substantially outperform cascade and joint-generation baselines on speech quality, motion-contact fidelity, and semantic alignment.

**Purpose (≤3 sentences):** To give embodied-speaker generation (synchronized voice + body motion) fine-grained, explicit control over vocal style and motion at the body-part/hierarchy level, rather than only implicit control via text or speech embeddings.

**Breakthrough (≤3 sentences):** The authors report DuoFlow achieves 4.71% word error rate and 0.94 speaker similarity versus 6.12%/0.80 for a CosyVoice2+MambaTalk cascade baseline, and 87.43%/90.40% pairing accuracy at two granularity levels versus the next-best baseline's 61.37%/62.68% (Motion-Omni). They also report DuoFlow is roughly 2–4x faster at inference (1.33s for a 12.9s clip, RTF 0.10) than the cascade and Motion-Omni baselines.

**Tools & method (≤3 sentences):** DuoFlow uses a dual-stream latent flow transformer with a shared noise level and a unified second-based temporal coordinate, modality-specific residual connectors to inject hierarchical conditions, layer-wise bidirectional cross-modal attention, and a monotonic phoneme pathway with CTC supervision for speech-motion temporal alignment; it was trained on the new MotionSpeech dataset (34,950 clips, ~125.2 hours) using 8×A100 GPUs per stage.

**Limitation (≤3 sentences):** The authors state in their conclusion that "improving physical contact fidelity and extending the framework to streaming generation remain future directions," and their own reported foot-skating rate (29.61%) is noticeably higher than the CosyVoice2+MambaTalk cascade baseline's 46.78%... (note: DuoFlow's 29.61% is actually lower/better than all compared baselines, but still a double-digit skating rate the authors implicitly flag via the contact-fidelity future-work note).

## MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos
- **arXiv:** 2611.21339 · https://arxiv.org/abs/2611.21339
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Yunyang Ge, Weijie Kong, Ryan Xu, Yue Wu, Qi Tian, Jiangfeng Xiong, Bin Lin, Mingzhe Zheng, Shenghai Yuan, Zheyuan Liu, Jianwei Zhang, Li Yuan
- **Qualifying affiliation(s):** Tencent Hunyuan (one of three affiliations listed on the paper, alongside Peking University and HKUST; exact per-author mapping was not extractable from the HTML, but a footnote notes some authors' work was "done during an internship at Tencent Hunyuan," indicating Tencent Hunyuan staff co-authorship)
- **Categories:** cs.CV
- **Open release:** code + weights — project page https://Tencent-Hunyuan.github.io/MovieRoll/, GitHub https://github.com/Tencent-Hunyuan/MovieRoll, Hugging Face https://huggingface.co/yunyangge/MovieRoll
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Streaming video generators must sustain quality beyond their training horizon while managing growing self-generated history and KV-cache costs. MovieRoll is a base-to-distilled framework connecting streaming fine-tuning, long-rollout distillation, and long-horizon inference to address this. The authors report it remains competitive at 30s after training only on up to 15s clips, and that the distilled variant achieves the highest total scores among compared methods up to 60s.

**Purpose (≤3 sentences):** To let streaming/autoregressive video diffusion models generate stable, high-quality long-form video well beyond the duration they were trained on, without exploding cache memory or losing motion naturalness.

**Breakthrough (≤3 sentences):** The authors report their hierarchical KV-cache compression (HieraKV), which keeps full history in shallow layers and sink-plus-recent history in deeper layers, reduces cache memory by up to 78% while improving generation quality; their cumulative long-tuning distillation (CuLT-DMD) enables efficient long-rollout training of a few-step generator by averaging local gradients while holding parameters fixed during each rollout. On HeliosBench, MovieRoll-Distilled is reported as highest-scoring among compared methods on single- and multi-event evaluation up to 60s.

**Tools & method (≤3 sentences):** The framework combines Window-wise Teacher Forcing (bidirectional attention within windows, causal access to prior history) for a multi-step base model, HieraKV cache compression, CuLT-DMD distillation for a few-step generator, KV recomputation and guidance annealing (AnnealCFG) to extend beyond the training horizon, and FBCA attention plus a PS-VAE decoder for efficient streaming output; inference/efficiency measurements were run on NVIDIA H20 GPUs (up to 8 GPUs).

**Limitation (≤3 sentences):** The authors state MovieRoll-Distilled "has not yet achieved real-time generation" — even on 8 H20 GPUs with SageAttention, a 60s video generates at 9.47 FPS versus the 24 FPS needed for real-time playback — and that MovieRoll-Base is insufficiently stable at 60s (so only the distilled model was evaluated at that length), with semantic and drifting-naturalness ratings dropping at 60s versus 10s. They also note, based on their own experience rather than measurement, that streaming models still struggle with complex motion and camera trajectories.

## WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning
- **arXiv:** 2611.21143 · https://arxiv.org/abs/2611.21143
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Hongyu Ma, Hairong Qu, Shiqi Zhao, Yongsong Yang, Kai Shi, Jiahao Ai, Xin You, Peng Yin
- **Qualifying affiliation(s):** FLAG: borderline — CyberOrigin (Xin You); other co-authors are at City University of Hong Kong
- **Categories:** cs.RO
- **Open release:** demo — project website https://fruitrabbit.github.io/WinDEX/ (no code, weights, or public dataset release mentioned in the visible text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Collecting large-scale, metrically accurate 3D hand-motion data in the wild is hard, limiting data for training dexterous robot hands. WinDEX combines geometric-temporal optimization with visual-inertial SLAM to extract metric-scale 3D hand motion from in-the-wild egocentric stereo video, an end-to-end fisheye-native reconstruction network (WinDEX-Net), distilled streaming/offline models, and a low-cost stereo-inertial capture rig (CyberCap), producing the 1,000-hour WinDEX-Hand dataset. The authors report state-of-the-art reconstruction accuracy and large task-success-rate gains for policies trained on this data versus prior motion references.

**Purpose (≤3 sentences):** To produce accurate, metric-scale, real-time-capable 3D hand motion reconstruction from cheap in-the-wild video, for use in training dexterous robot manipulation policies and for live teleoperation.

**Breakthrough (≤3 sentences):** The authors report offline reconstruction running at 43.61 FPS and causal streaming at 171 FPS, with state-of-the-art held-out accuracy of 14.5 pixels in-the-wild reprojection error and 37.29 mm world-frame joint error (with visual-inertial odometry). They report 7.6x and 3.6x the task success rates of reinforcement-learning policies trained with WiLoR and HaWoR motion references, respectively, and demonstrate real-time arm-hand teleoperation on a physical 20-joint "Wuji" robot hand.

**Tools & method (≤3 sentences):** The pipeline integrates geometric-temporal optimization for metric 3D hand annotation with visual-inertial SLAM for world-frame grounding, a fisheye-native stereo network (WinDEX-Net) trained via a model-assisted "data-model flywheel," and distilled models for offline vs. causal streaming inference; training used 4x RTX 4090 GPUs, offline inference/speed tests used a single RTX 4090 (FP16), and the CyberCap capture rig uses 1920x1200 fisheye stereo at 30 fps plus a 300 Hz IMU.

**Limitation (≤3 sentences):** The authors state that during occlusion the method holds the last high-confidence pose rather than recovering unobserved articulation, and that the causal real-time streaming model (WinDEX-Stream) is measurably less accurate than the offline windowed model (e.g., 42.7 mm vs. 20.3 mm wrist error at comparable settings). They also note their visual-inertial odometry camera-trajectory estimate carries 0.150 m RMS absolute trajectory error and 11.69° RMS orientation error against optical motion capture, which propagates into the reported world-frame hand error, and that their physical-robot experiments relied on external camera-based pose tracking as an approximation of simulation-level ground truth.

## Conflict-Aware Multi-Teacher On-Policy Distillation in Aligned Action Spaces for Cross-Game Generalization
- **arXiv:** 2611.21094 · https://arxiv.org/abs/2611.21094
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Jing Yi, Cehao Yang, Hualei Zhang, Haitao Li
- **Qualifying affiliation(s):** FLAG: borderline — LIGHTSPEED (Jing Yi, Haitao Li; likely Tencent's Lightspeed Studios, not independently confirmed beyond the paper's own "LIGHTSPEED" affiliation label); other co-authors at HKUST(GZ)/HKUST
- **Categories:** cs.AI
- **Open release:** none found (paper page links only to the arXiv abstract/PDF)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The authors target zero-shot cross-game generalization: consolidating several single-game vision-language-model (VLM) experts into one model that can control unseen games from raw pixels with no target-game training. They identify two problems in scaling multi-teacher on-policy distillation to autoregressive VLMs — token-to-action misalignment and conflicting corrections from teachers trained under incompatible game dynamics — and propose CAMOPD to resolve both. On held-out games, CAMOPD is reported to outperform prompting, weight-merging, and multi-task baselines.

**Purpose (≤3 sentences):** To build a single VLM game-playing controller that generalizes zero-shot to new games it was never trained on, by better combining knowledge distilled from multiple single-game "teacher" experts without the teachers' conflicting advice canceling out.

**Breakthrough (≤3 sentences):** The authors report CAMOPD achieves 86.7% (26/30) and 80.0% (24/30) zero-shot Task-1 success on the unseen games GeoDash and Doodle Jump respectively, using a Qwen3.5-4B backbone with rank-16 LoRA fine-tuning, evaluated on GameWorld's "Paused 100-Step Reset-on-Fail" protocol (30 executions per task). Their method combines "complete-action alignment" (normalizing command-completion likelihoods over each game's legal action set) with cross-evaluating specialist teachers to upweight compatible ones and suppress conflicting corrections, without needing any target-game data.

**Tools & method (≤3 sentences):** CAMOPD is a post-training (distillation) framework built on a Qwen3.5-4B VLM with LoRA (rank 16, attention + MLP projections, sequence length 2048, AdamW), evaluated on the GameWorld benchmark (Ouyang et al., 2026) using temporal-control (GeoDash) and directional-steering (Doodle Jump) transfer suites against prompting, weight-merging, and multi-task distillation baselines.

**Limitation (≤3 sentences):** The authors note their evaluation protocol pauses the game during each VLM inference step over discrete commands, which they acknowledge differs from "real-time continuous streams." They also state the student model only sees a short 1-2 frame window with no explicit long-horizon episodic memory, and list streaming control and memory-augmented policies as future work.

# Near-misses
- 2611.21517 · Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models · no industry co-author (authors are at CMU and Technion); also topically a robotic task-planning "world model," not a visual/game world model
- 2611.21479 · LynnReal-Hand: Unlocking World Interaction with Hand Control · no qualifying-tier industry co-author — all authors affiliated with LynnReal AI (an early-stage startup) plus Shanghai Jiao Tong University/Fudan University/Shanghai Innovation Institute
- 2611.21383 · The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation · no industry co-author (all authors at Yonsei University)
- 2611.21373 · WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection · off-topic despite keyword match — AI-generated-video forensic detection, not 3D/world-model/character-animation/game-engine generation
- 2611.21302 · Déjà-Events: Multi-view 3D Geometry with Event Cameras via Sparsity-Aware Adaptive Gating · no industry co-author stated in the paper's own affiliation list (ETH Zürich, TU Delft only — Microsoft is not mentioned despite Marc Pollefeys' general dual affiliation elsewhere)
- 2611.21253 · QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting · no industry co-author (Nankai University, Tiangong University, Beihang University)
- 2611.21114 · VAE Rhythm: Temporal Decoding Traces for AI-Generated Video Detection · off-topic despite keyword match — forensic AI-video detection, not generative 3D/world-model/character-animation/game-engine work
- 2611.21072 · Sage S2.1 Flash Technical Report · off-topic despite keyword match — general scientific-reasoning/agentic LLM, not 3D/world models/character animation/game engines
- 2611.21029 · Sparse Attention for Visual Generation: Toward Algorithm-System Co-Design · no industry co-author (Zhejiang University, UCLA, University of Hong Kong); a systems survey, not primary generative research
- 2611.21038 · ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching · no industry co-author (HKUST(GZ), Guangdong University of Technology)
