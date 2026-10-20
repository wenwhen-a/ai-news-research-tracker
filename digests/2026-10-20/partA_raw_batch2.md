Batch 2 verification — 12 candidate papers checked against arXiv abstract + HTML pages. 6 qualify (1 flagged borderline), 6 near-misses. Double-verification pass done: every QUALIFIES entry below was re-checked against the fetched arXiv abstract/HTML text for title, author list, date, affiliation and the specific numbers/claims quoted.

---

## EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models
- **arXiv:** 2610.25959 · https://arxiv.org/abs/2610.25959
- **Submitted:** 2026-10-19
- **Authors:** Xiaokun Feng, Junshu Tang, Zeyi Lin, Ling-Hao Chen, Shuai Shao, Qinglin Lu, Kaiqi Huang
- **Qualifying affiliation(s):** Tencent Hunyuan — Xiaokun Feng, Junshu Tang, Zeyi Lin, Ling-Hao Chen, Shuai Shao, Qinglin Lu, Kaiqi Huang (paper states the work was done during an internship at Tencent Hunyuan)
- **Categories:** cs.AI
- **Open release:** code | checkpoints | dataset (paper states "dataset, checkpoints, and code are said to be publicly released"; no specific link found in fetched text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces "Embodied World Agents" (EWAs) and instantiates them as open-world embodied navigation planning. It releases EmbodiedWorld-200K, a 200K+ sample dataset built from about 260K gameplay trajectories (~708 hours) mined from OGameData (150+ 3D games), with multi-level annotations from camera motion to goal-navigation instructions. A two-stage recipe (offline SFT, then world-model RL) is proposed and evaluated.

**Purpose (≤3 sentences):** The authors argue existing embodied benchmarks are narrow (single scene, single robot, or single game) and that passive vision-language training lacks closed-loop perception-action ability. They build a large, multi-genre open-world planning dataset and a training recipe meant to generalize beyond the training distribution.

**Breakthrough (≤3 sentences):** The authors report that SFT on their dataset raises a Qwen3-VL-4B baseline from TM 54.9/DirAcc 70.1/nDTW 67.1/NE 51.7 to TM 62.0/DirAcc 72.0/nDTW 83.6/NE 35.6 on their own held-out split, roughly matching Gemini-3.5 on DirAcc (72.0 vs 72.4). On a GTA5 target-scene test, adding DPO trained inside the video world model LingBot-World-Fast raises TM from 65.4 to 75.0 and nDTW from 66.1 to 92.7, with NE falling from 48.9 to 13.4.

**Tools & method (≤3 sentences):** Camera poses are recovered with VIPE; clips are segmented into "navigation-coherent segments" with a shared W/A/S/D action vocabulary; Qwen3.5-27B generates instructions. Stage I is LoRA SFT (2 epochs) on Qwen3-VL-4B; Stage II runs the SFT model inside the video world model LingBot-World-Fast, using a VQA-based reward over rollouts to build DPO preference pairs.

**Limitation (≤3 sentences):** The fetched text's dedicated Limitations appendix was truncated, but visible section headers note "3D virtual games as proxies for the physical world" and "limited action granularity" as concerns. Stage II evaluation relies on a single target game (GTA5), and the underlying data is built entirely from virtual games rather than physical environments.

---

## ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models
- **arXiv:** 2610.25861 · https://arxiv.org/abs/2610.25861
- **Submitted:** 2026-10-19
- **Authors:** Zhiyang Deng, Yuzhe Wu, Zijun Lin, Yeying Jin
- **Qualifying affiliation(s):** Tencent — all four authors list Tencent as a primary affiliation, alongside National University of Singapore (Deng, Wu, Jin) and Nanyang Technological University (Lin)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper targets action control in "planar-camera" game world models (top-down/isometric games), where existing feature-based action conditioning fits poorly because it gives the model no explicit world coordinate system. ActionRoPE converts action-driven camera displacement into world-coordinate rotary positions so the same world location keeps the same positional address over time, paired with Coordinate-Conditioned Noise Scheduling (CNS) that denoises already-seen regions earlier than newly revealed ones. Both additions are parameter-free or near-parameter-free (the knownness mask adds ~0.015M parameters).

**Purpose (≤3 sentences):** The authors want game world models that follow commanded motion faithfully and don't "drift" (regenerate a different scene) when a player returns to a previously visited location, a known failure of feature-conditioned action control.

**Breakthrough (≤3 sentences):** On their main Wan2.2-TI2V-5B backbone, the authors report the method improves PSNR from 21.11 dB (best baseline, AdaLN) to 23.94 dB and cuts drift from 22.6 px to 7.8 px — a reported 66% drift reduction over the strongest of four re-implemented baselines (Prompt, Linear, AdaLN, Cross-Attn). They report the method transfers across backbones from 1.3B to 33B parameters (SkyReels-V2-DF, LTX-2.5, MiniMax-H3) and to out-of-distribution scenes (drift 7.6 px vs 16.5 px for the best baseline).

**Tools & method (≤3 sentences):** Training data comes from the game *No Rest for the Wicked* (2.5D fixed top-down view): 50.9 hours, 22,782 clips at 81 frames/16 fps/832×480, with 18,528 training and 982 held-out evaluation clips. The main backbone is Wan2.2-TI2V-5B, fine-tuned for 5,000 steps (AdamW, lr 1e-5, batch 16); the model is also distilled into a four-step causal student with a KV cache for real-time inference.

**Limitation (≤3 sentences):** The authors state the method assumes the static world translates approximately rigidly in the image plane (true for top-down/isometric cameras that follow the player), so it does not model zoom or strong parallax, and does not make moving objects follow world coordinates. Knownness is defined only from the first frame's footprint, so regions revealed later aren't marked "known" when the camera returns to them. No GPU hardware is specified in the fetched text.

---

## Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base
- **arXiv:** 2610.25634 · https://arxiv.org/abs/2610.25634
- **Submitted:** 2026-10-19
- **Authors:** Wenqing Wang, Joonghyuk Shin, Jonathan Tremblay, Chan Hee Song, Yun Fu
- **Qualifying affiliation(s):** NVIDIA — Jonathan Tremblay, Chan Hee Song (affiliation block lists NVIDIA alongside Seoul National University and Northeastern University; footnote states one author's work was done during an NVIDIA internship and two authors are co-last authors)
- **Categories:** cs.CV, cs.LG
- **Open release:** demo (paper states "representative rollouts appear on the project page"; no link found in fetched text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Autoregressive video diffusion models generate streaming video by conditioning each chunk on previously generated (imperfect) frames, which causes compounding "drift" that degrades quality within seconds. The authors show this drift is largely deterministic (~95% systematic across noise seeds) and train a small 5.9M-parameter LoRA corrector, "Clean Forcing," on a frozen base model to regress it, with a closed-loop DAgger-style training stage. The merged corrector needs no real video for training and adds no inference-time cost.

**Purpose (≤3 sentences):** The paper targets exposure bias in autoregressive video diffusion used for long, streaming video generation — including the kind of real-time generative world models used for driving and game simulation — where prior fixes required expensive full retraining or gave inconsistent training-free corrections.

**Breakthrough (≤3 sentences):** On 50-second text-to-video generation with Wan2.1-T2V-1.3B, the authors report Δ-drift falling from +11.3 (adapted base) to +1.65 using zero real videos, and to −0.16 using 40 real clips, which they say beats the best published result (+3.57) while using over 150× less data. Applying the same zero-real-video recipe to two other autoregressive world models, they report a 48% drift reduction on HY-WorldPlay and a 60% drift reduction on NVIDIA OmniDreams (a driving world model built on Cosmos-Predict2.5).

**Tools & method (≤3 sentences):** The corrector is a rank-16 LoRA (5.9M params, 0.4% of the base) on the q/k/v/o self-attention projections across all 30 DiT blocks, trained with AdamW; evaluation uses 128 held-out MovieGenVideoBench prompts and VBench + Δ-drift (MUSIQ-based) metrics. Training uses at most 340 clips (40 real + 300 synthetic) versus a cited baseline's 55K source/81K generated clips; the full pipeline runs in about one day on a single NVIDIA GB300 GPU (≥48 GB memory), with the 14B-model variant taking about three GPU-days.

**Limitation (≤3 sentences):** The authors state stronger drift reduction tends to coincide with less scene progression (corrected scenes stay close to their opening frames), and learned correctors transfer poorly to sibling checkpoints or a distilled four-step model (giving no benefit on Self-Forcing's distilled generator). They also report training instability at the 14B scale, making checkpoint selection important, and note the appendix's full Limitations section was truncated in the fetched text.

---

## Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation
- **arXiv:** 2610.25600 · https://arxiv.org/abs/2610.25600
- **Submitted:** 2026-10-19
- **Authors:** Xuezhou Xu, Chung-Pang Wang, Zhenzhen Li, Benjamin Riviere
- **Qualifying affiliation(s):** NVIDIA — affiliation block lists "New York University" and "NVIDIA" without an explicit per-author mapping in the fetched HTML
- **Categories:** cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes VQ-WM, a latent feedback motion planner that searches over vector-quantized latent states (using a learned world model) for short paths to a goal, while a separate continuous visual-feedback controller tracks each planned state and corrects drift. Quantization uses a first-passage-time (FPT) quasi-metric, estimated via closed-loop rollouts, instead of Euclidean distance, so codes reflect what the controller can actually reach.

**Purpose (≤3 sentences):** The authors target long-horizon robot manipulation and locomotion planning, where visual world models typically fail because autoregressive prediction errors compound and long action sequences are hard to optimize directly.

**Breakthrough (≤3 sentences):** On a physical four-disk Tower of Hanoi task (WidowX arm), the authors report 100% success on the full 15-move solution using only short "play" demonstrations, versus baselines Cosmos Policy (5%), π0.5 (3%), and V-JEPA 2-AC* with manual subgoals (27%) on non-expert data. On simulated long-horizon manipulation benchmarks (Stable-WorldModel), they report VQ-WM beating the strongest prior world model (H-JEPA) by 8.0–28.0 percentage points, and on DeepMind Control Walker locomotion with images only, 22.0% vs 12.7% for DINO-WM (97.3% vs 12.0% with proprioception added).

**Tools & method (≤3 sentences):** The pipeline uses a frozen V-JEPA 2 encoder, a goal-conditioned controller, a continuous latent predictor, and a discrete latent predictor/codebook built via a greedy set-cover over FPT-estimated regions of attraction. At inference, breadth-first search over the discrete latent graph plans the path, and the authors report a ~5-minute robot execution plan computes in under one second on an NVIDIA RTX 5080 GPU.

**Limitation (≤3 sentences):** The authors note experiments use only a single plan per episode, so the benefits of replanning are unexplored, and the method relies on a learned latent world model for its FPT reachability estimates (with a rejection class excluding unseen transitions from graph search). They flag an inconsistency between the abstract's reported gain range (13.3–85.3 points) and the introduction's narrower comparison (13.3–34.6 points vs H-JEPA specifically).

---

## ReDT: Resolution-Decoupled Visual Geometry Transformer
- **arXiv:** 2610.25517 · https://arxiv.org/abs/2610.25517
- **Submitted:** 2026-10-18
- **Authors:** Abteen Arab, Guile Wu, Dongfeng Bai
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab — Abteen Arab (also University of British Columbia; footnote says work done during an internship at Huawei Canada), Guile Wu, Dongfeng Bai; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ReDT is a feed-forward transformer for multi-view 3D reconstruction built on the VGGT family (specifically VGGT-Ω), designed to handle high-definition inputs without the quality degradation and quadratic cost that standard-definition-trained models show at higher resolutions. It maps each view to a fixed-size set of "basis tokens," computes cross-view correspondences in that compact space via Discretization-Invariant Visual Attention (DIVA) blocks, and projects results back to full resolution for dense prediction.

**Purpose (≤3 sentences):** The authors aim to let a visual geometry transformer trained at lower resolution generalize to much higher resolutions (SD to 2K) without retraining, motivated by an empirical finding that intermediate per-view features keep a nearly constant effective rank as resolution and view count grow.

**Breakthrough (≤3 sentences):** On ETH3D at 2K, the authors report a 16× speedup (6.35s vs 102.70s), 34% peak-memory reduction (64.47GB vs 98.09GB), and 33% Chamfer-distance reduction (0.1140 vs 0.1702) versus VGGT-Ω. On ScanNet++ (2K), they report pose AUC@30 of 93.65 vs 79.22 for DepthAnything3, the strongest baseline on that dataset.

**Tools & method (≤3 sentences):** The encoder uses a quadtree to merge low-entropy patches into 2×2/4×4/8×8 regions, and DIVA blocks replace standard attention with learned softmax assignments mapping N tokens to K fixed basis tokens, using test-time training (TTT) for cross-view reasoning in the basis space. Models are fine-tuned from public checkpoints for 10 epochs (AdamW) on seven datasets (ASE, ParallelDomain4D, UnrealStereo4K, MPSD, BlendedMVS, DL3DV, MegaDepth), with no GPU model specified but 100 FHD frames reported to need 61GB peak memory and ~8.2s.

**Limitation (≤3 sentences):** The paper has no dedicated limitations section, but the appendix states overall complexity remains quadratic in token count because the DPT decoder head is left unchanged, and peak memory still grows with resolution. The ablations show a smaller encoder basis count (256 vs 512) substantially hurts accuracy (Chamfer distance 0.3737 vs 0.1137), and on some sub-HD benchmarks the baseline FlashVGGT is faster.

---

## DragonMoCap: Monocular Video-based Motion Capture for Diverse Dragon Topologies
- **arXiv:** 2610.25437 · https://arxiv.org/abs/2610.25437
- **Submitted:** 2026-10-18
- **Authors:** Zhongfei Qing, Xiaoxiang Zhao, Ling-Hao Chen, Zhongang Cai, Wenjia Wang, Yifan Wu, Qianying Liu, Wei Zeng, Bo Hu, Songnan Li
- **Qualifying affiliation(s):** Tencent — Zhongfei Qing, Xiaoxiang Zhao, Yifan Wu, Wei Zeng, Bo Hu, Songnan Li
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DragonMoCap is a monocular video motion-capture framework for dragon-type game/film characters, whose production rigs vary widely in joint count (20–60+) and naming, breaking fixed-template regressors. It treats the target skeleton as a dynamic input via "language-grounded joint query tokens" (CLIP-encoded bone names plus topological/kinematic descriptors), with a non-parametric query-token retrieval mechanism for zero-shot adaptation to unseen rigs.

**Purpose (≤3 sentences):** The authors target the lack of parametric models and high-quality data for non-human (dragon) character mocap, which currently forces manual keyframing in animation production, covering three common topologies: winged quadrupeds, wingless quadrupeds, and winged bipeds (wyverns).

**Breakthrough (≤3 sentences):** The authors report DragonMoCap beats HMR-style baselines SMPLest-X and OSX on seen rigs (MPJPE 9.46cm vs 10.57cm for SMPLest-X, ~10.5% lower) and generalizes to 77 held-out unseen rigs (MPJPE 12.11cm vs 14.62–15.32cm for ablated variants), with 78.3% top-1 / 94.6% top-5 retrieval accuracy for bone-role matching in a leave-one-rig-out test. A 40-participant user study on AI-generated clips found DragonMoCap preferred over baselines for anatomical plausibility (mean 4.5 vs 3.2, 83.6% win rate, p<0.001), and the authors state the system has been integrated into professional animation workflows as a real-time Unreal Engine add-on.

**Tools & method (≤3 sentences):** Training uses an internal dataset of UE5-rendered, professionally animated dragon clips (88 training rigs / 77 held-out rigs, ~1.2M frames total after SLERP augmentation), with a frozen DINOv2 ViT-L/14 image encoder and frozen CLIP text encoder feeding a transformer decoder that predicts root translation and per-joint 6D rotations. Training used 4× NVIDIA A100 GPUs (batch 512, 200 epochs, AdamW, lr 2e-4), with inference at ~30 FPS on a single NVIDIA L20 GPU; the model is ~420M parameters (115M trainable).

**Limitation (≤3 sentences):** The paper has no dedicated limitations section, but the conclusion calls the image encoder's appearance coverage "the main remaining bottleneck," mitigated by generative appearance augmentation to reduce overfitting to limited visual diversity in the internal dataset. The user study used AI-generated inputs with no ground truth, so it measures perceived quality rather than accuracy, and the framework is scoped to three dragon topologies only.

---

# Near-misses
- 2610.26025 · TamedFlow: Trajectory-Aware Distillation for Teacher-Assisted Diffusion Sampling · off-topic (generic diffusion-transformer sampling acceleration for ImageNet/text-to-image/video generation; not 3D, world models, character animation, or game engines, despite a Huawei Technologies Ltd. co-author)
- 2610.25840 · OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects · affiliation unverifiable — no HTML version (arxiv.org/html/2610.25840 and v1 both return HTTP 404; PDF fallback not permitted)
- 2610.25734 · Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving · off-topic (a VLA perception/planning policy for autonomous driving distilled from vision foundation models, not a generative world model, 3D reconstruction, character animation, or game-engine paper); affiliation is Xiaomi EV, which is not on the qualifying list
- 2610.25414 · UniState: Unifying Memory and Intervention for Controllable World Simulation · no industry co-author (all authors affiliated with Yonsei University only; the acknowledgment of an "Advanced GPU Utilization Support Program" is a compute grant, not an author affiliation)
- 2610.25395 · A 3D-Driven Framework for Moving-Camera Perspective-to-360° Video Generation · affiliation unverifiable — no HTML version (arxiv.org/html/2610.25395 and v1 both return HTTP 404; PDF fallback not permitted)
- 2610.25360 · Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence · no industry co-author (all three authors affiliated with Universitas Brawijaya, Indonesia)

Verification: each QUALIFIES entry above was independently confirmed from the paper's arXiv abstract page (title, authors, v1 date, categories, non-withdrawn status) and its arXiv HTML page (author affiliation block; abstract/intro/method/results/limitations text), with all numbers, dataset names, and limitations quoted taken directly from that fetched text — none invented or carried over from the automated screen's company guess. The screen's company match was wrong for 1 (TamedFlow: screen said ByteDance, actual is Huawei/HKUST/UESTC) and for 10 (UniState: screen said NVIDIA, actual is Yonsei University only, no industry author found); both are reflected in the near-miss reasons above rather than the output entries.
