## World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models
- **arXiv:** 2610.17434 · https://arxiv.org/abs/2610.17434
- **Submitted:** 2026-10-12
- **Authors:** Junyi Wu, Zekun Li, Chenhongyi Yang, Chen Guo, Lingchen Yang, Yongan Zhang, Xinyi Zhang, Hongbing Hu, Bartek Rymkowski, Srinath Sridhar, Yan Yan, Xijie Huang
- **Qualifying affiliation(s):** Meta — Junyi Wu, Zekun Li, Chenhongyi Yang, Chen Guo, Lingchen Yang, Yongan Zhang, Xinyi Zhang, Hongbing Hu, Bartek Rymkowski, Xijie Huang (all Meta Reality Labs, several with joint academic appointments at UIC/Brown)
- **Categories:** cs.CV (primary); cs.AI; cs.MM
- **Open release:** none found (project page only: adreamwu.github.io/World-T3/, no code/weights link)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** World-T3 is a camera-controlled, autoregressive video world model that stores past observations in dedicated test-time-trained model parameters rather than a growing context window, so memory and per-step compute stay constant as rollouts lengthen. It is distilled into a 4-step generator for real-time inference. On a 120-clip "out-and-back" revisit benchmark it substantially improves scene recall and pose accuracy over prior fast world models.

**Purpose (≤3 sentences):** Long-horizon interactive video world models need to "remember" previously seen parts of a scene when the camera revisits them, but standard approaches either truncate context or grow memory/compute unboundedly. The authors target real-time, pose-consistent revisit memory without unbounded cost growth.

**Breakthrough (≤3 sentences):** The authors report that a recursive-least-squares update, keyed by camera pose, consolidates observations into persistent "fast weights" inside the generator. On their revisit benchmark this raises PSNR from 13.52 dB (best prior baseline, SANA-WM) to 18.31 dB and cuts rotation error from 3.344° to 1.075°, while the distilled 4-step model runs at 20.6 FPS at 1280×704 on a single NVIDIA B200 GPU (vs. 14.2 FPS for the strongest baseline).

**Tools & method (≤3 sentences):** Built on Wan2.2-TI2V-5B and trained on a curated 908K-clip corpus (601K base + 307K revisit-augmented, mixing real footage and game-engine renders with ground-truth poses), using camera poses from 3D foundation models such as VGGT-Ω. Training used 512/256/128 GPUs across three stages; the final stage uses dual-teacher distribution matching to compress a 50-step teacher into a 4-step real-time student.

**Limitation (≤3 sentences):** The authors state the method depends on external camera-pose estimators, which can drift under weak texture or fast motion and misalign the pose-keyed memory retrieval, with errors compounding over long horizons. They also report that visual fidelity and generalization well beyond the training context length remain open problems, and the distilled student trades some VBench visual-quality score for speed versus its teacher.

## Multics: Generative Multi-Player World Model with Hierarchical Communication
- **arXiv:** 2610.17201 · https://arxiv.org/abs/2610.17201
- **Submitted:** 2026-10-12
- **Authors:** Kaiyi Huang, Wangbo Yu, Yukun Huang, Jiwen Yu, Kunhao Liu, Donglin Yang, Wenbo Hu, Ying Shan, Xihui Liu
- **Qualifying affiliation(s):** Tencent — Wangbo Yu, Yukun Huang, Kunhao Liu, Wenbo Hu, Ying Shan (ARC Lab, Tencent IEG); remaining authors at The University of Hong Kong
- **Categories:** cs.CV
- **Open release:** none found (project page only: karine-huang.github.io/Multics/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Multics generates video of a shared multiplayer environment from each player's own viewpoint, using a three-level (player/group/global) hierarchical communication scheme in self-attention instead of full pairwise or fully-centralized communication. It reports state-of-the-art consistency, controllability and interference robustness at 4 and 6 players, and generalizes to 6/8/10 players at inference without retraining.

**Purpose (≤3 sentences):** Existing multiplayer world models either use fully-connected attention (quadratic cost as players grow) or a single global representation (interference between unrelated players' events). The authors want robust, scalable cross-player generation that avoids both failure modes.

**Breakthrough (≤3 sentences):** The authors report Multics beats both baselines (Solaris, γ-World) on GeoKPM, PSNR, LPIPS, rotation/translation error, FID and FVD at 4 and 6 players (e.g. GeoKPM 54.17% vs. 49.42% at 4 players), and that it trains at 4 players but generalizes to 10 players with GeoKPM 51.54%. Self-attention compute at 10 players is reported at 9.6 TFLOPs versus 69.1 TFLOPs for fully-connected communication.

**Tools & method (≤3 sentences):** Built on Wan2.2 TI2V 5B, trained on the OpenCS2 dataset (ten-player Counter-Strike 2 match renders), with separate 4- and 6-player models and cross-domain evaluation on EgoTeam. Group tokens with shared parameters aggregate nearby-player information and connect to global tokens, and a budget-constrained dynamic grouping method uses recent camera trajectories to decide who communicates; training used 16 GPUs (model unspecified) with bfloat16 and gradient checkpointing.

**Limitation (≤3 sentences):** The authors state that maintaining persistent world states across multiple players over long horizons "remains a challenging but important direction for future work." They also note Multics inherits the limitations of its pretrained video foundation model, including visual artifacts under large and dynamic human motion.

## World Models Need a Physical Registry: Learning Internal Predictive States for Physically Plausible World Models
- **arXiv:** 2610.16365 · https://arxiv.org/abs/2610.16365
- **Submitted:** 2026-10-12
- **Authors:** Shinseong Kim, Jaeseok Jeong, Jianlong Fu, Youngjung Uh
- **Qualifying affiliation(s):** Microsoft — Shinseong Kim (joint Yonsei/Microsoft Research Asia), Jianlong Fu (Microsoft Research Asia)
- **Categories:** cs.AI (ACM classes I.2.10, I.4.8)
- **Open release:** none found (project page only: grainsack.github.io/physical-registry/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces the Physical Registry, a set of temporally grounded registry slots inside a video diffusion transformer that hold an explicit, readable predictive-dynamics state separate from appearance tokens. It is tested across four video world-model backbones (Cosmos, WAN) and improves physical plausibility on Physics-IQ Verified and WorldModelBench. A companion Physical Registry Selector (PRS) ranks candidate futures using intermediate registry readouts before full denoising completes.

**Purpose (≤3 sentences):** Current video world models encode appearance and dynamics jointly in standard tokens, giving no distinct, readable state for learning or auditing predicted physical evolution. The authors ask where inside the generator physical dynamics predictions should live, and propose making that state explicit.

**Breakthrough (≤3 sentences):** The authors report Physical Registry improves vanilla fine-tuning by 9.9/8.7 points on Physics-IQ I2V/V2V, the largest gain among interfaces compared (vs. REPA, cross-attention, AdaLN, joint generation). With only 0.45% additional parameters it lets Cosmos 3 Nano 16B (43.56) surpass the published I2V score of the much larger Cosmos 3 Super 64B (42.7), and PRS improves I2V scores by 5.6–15.9% across backbones without scoring completed videos.

**Tools & method (≤3 sentences):** Registry slots are initialized from an observation-conditioned forecast, co-evolve with video tokens, and receive future-representation supervision from a frozen V-JEPA 2.1 ViT-g encoder. Training used a curated "Enlarge" set of ~212,100 clips (~375 hours) from WISA, InternVid, SDG-PhysXSim and SDG-RobotSim on four backbones (Cosmos 3 Nano 16B, Cosmos v2.5 2B, WAN 2.2 I2V-A14B, WAN 2.2 TI2V-5B), using 8×H100 or 8×A100 40GB for fine-tuning and a single H100 80GB for sampling-cost measurements.

**Limitation (≤3 sentences):** The authors report instruction-following scores on WorldModelBench decrease slightly for Cosmos v2.5 and WAN TI2V-5B even as physical adherence improves, and sampling cost rises to 1.55–1.67× per step. An ablation shows strong dependence on forecast content: zeroing the registry's mask drops Cosmos Nano I2V from 36.01 to 16.78, and the expanded-prompt setting relies on an external model (Claude Opus 5) to rewrite prompts.

## Unravel: Recovering an Interactive 3D Scene from a Single Image
- **arXiv:** 2610.16146 · https://arxiv.org/abs/2610.16146
- **Submitted:** 2026-10-12
- **Authors:** Hui Shan, Keyang Luo, Binjia Zhou, Ming Li, Kai Li, Xin Wang, Zhenyang Li, Zesong Yang, Weikai Chen, Runze Zhang, Xin WANG, Yanwei Fu, Zhen Chen, Xiangru Huang
- **Qualifying affiliation(s):** Adobe — Zhen Chen; Tencent LIGHTSPEED — Keyang Luo, Weikai Chen, Runze Zhang, Xin WANG (affiliation listed as "LIGHTSPEED", Tencent's internal game-development studio) — FLAG: borderline for the LIGHTSPEED mapping since it is not one of the explicitly spelled "Tencent" entries, though Adobe alone is sufficient to qualify
- **Categories:** cs.CV (primary); cs.AI
- **Open release:** code (planned) — "Our code will be released at https://github.com/SII-Hui/Unravel" (not available at time of check)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Unravel is a training-free framework that turns a single image into an interactive 3D scene in which every object is a separate, movable asset. It iteratively removes visible objects with a vision-language model and image editor, verifies each edit, then rebuilds the scene in reverse removal order so occluded regions become directly observed before reconstruction. A physical settling and agentic audit step then fixes floating objects, interpenetrations, and placement errors.

**Purpose (≤3 sentences):** Existing single-image-to-3D scene generators either produce one entangled, immovable geometry or predict all objects in a single feed-forward pass where wrong guesses can't be detected or repaired. The authors want a decompose-then-rebuild pipeline that can verify and correct itself as it goes.

**Breakthrough (≤3 sentences):** On a 5-scene, 160-object evaluation, the authors report Unravel reaches a 3D asset VLM score of 8.2 and human score of 8.6 (vs. 4.7/4.9 for direct reconstruction), full 2D mask area coverage (1.000 vs. 0.772) and zero undetected-coverage-ratio error on both 2D masks and 3D scene geometry (vs. 11.3%/10.1% for direct reconstruction). Observed points are treated as a lower bound on object size so assets can only grow, not shrink, to match evidence.

**Tools & method (≤3 sentences):** The pipeline is entirely training-free, relying on off-the-shelf hosted models including GPT-5.5, gpt-image-2, and GPT-6 Astra (called via its web interface), with point clouds as the main modality for spatial relationship recovery. No hardware details are reported since there is no training.

**Limitation (≤3 sentences):** The authors state the method "is limited by current image editing models," and that in highly cluttered scenes, edits may alter the appearance or position of remaining objects, with drift that can accumulate across rounds and disrupt alignment. They note a comparison baseline (Seeing Through Clutter) was excluded because it showed hallucinations and unstable editing in their tests, and they suggest stronger editing models, geometric feedback, and uncertainty-aware retries as future work.

## Gen Through the Lens: Camera-Controllable Video Generation via Cross-Coordinate Conditioning Fusion
- **arXiv:** 2610.15900 · https://arxiv.org/abs/2610.15900
- **Submitted:** 2026-10-11
- **Authors:** Shuai Li, Jinxu Xiang, Xinyuan Li, Hanlei Guo, Xiyang Tan, Alan Zhao, Xiaotong Zhao, Ran Zhang
- **Qualifying affiliation(s):** Tencent — all authors (affiliation listed as "Tencent Video Solar System")
- **Categories:** cs.CV (primary); cs.AI; cs.GR; cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** "Gen Through the Lens" (GTL) is a camera-controllable image-to-video generation framework that decomposes and fuses control signals across three coordinate spaces — camera (intrinsics), world (spatial geometry hints), and object (3D bounding boxes) — to drive camera motion, focus/depth-of-field, and framing from a single reference image. The authors report it outperforms prior camera-conditioned video generators in realism and editability.

**Purpose (≤3 sentences):** Prior camera-controllable video generators treat camera motion as abstract conditioning or rely on a single coordinate system, limiting precise, physically consistent control of camera, object motion, and focus together. The authors aim for explicit, decomposed control signals that stay temporally and spatially coherent.

**Breakthrough (≤3 sentences):** On a held-out 1k-clip test set, the authors report their 14B model (GTL 14B) scoring best or near-best across FID (53.71), FVD (86.54), Qwen VQA (0.81), camera translation error (8.59) and bounding-box metrics against baselines including PAC, RC-I2V, and GEN3C. A custom camera-pose extraction pipeline is also reported to beat off-the-shelf estimators (MapAnything, Pi3, VGGT) at 11.74/17.11° translation/rotation error.

**Tools & method (≤3 sentences):** Trained on ~110k clips with camera trajectories and 3D bounding-box annotations from DynPose-100K, MultiCamVideo, BEDLAM2.0 and internal data, plus 8k zoom and 15k bokeh samples, all 81 frames at 480p; ablations use a Wan2.1-1.3B model. Training used 8× NVIDIA H800 GPUs for about 288 GPU hours across three stages.

**Limitation (≤3 sentences):** The authors note the object-motion condition is trained only on human subjects (though they report it generalizes to other objects), and that depth-of-field cues are encoded in subtle pixel-level variations that "may not be visually salient." They also flag that several baseline metrics may be biased because those methods lack explicit object control, and that the Seedance 2.0 baseline sometimes transfers appearance from the reference video, causing inconsistencies.

## Totem: Object-Centric 3D Memory for World-Consistent Video Generation
- **arXiv:** 2610.15807 · https://arxiv.org/abs/2610.15807
- **Submitted:** 2026-10-11
- **Authors:** Zichen Wan, Tianyu Huang, Fan Li, Kai Wang, Hongzhi Zhang, Wangmeng Zuo
- **Qualifying affiliation(s):** Huawei — Tianyu Huang, Fan Li (Huawei Technologies Ltd.) — FLAG: borderline; remaining authors at Harbin Institute of Technology
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Totem represents selected objects as persistent 3D memories anchored to a shared world coordinate frame, each with its own state, and combines these object memories with scene geometry in a dual-stream conditioning architecture to synthesize new-viewpoint video. The object memories also constrain the model's attention with 3D structural information to preserve object surfaces and spatial relationships under large camera viewpoint changes.

**Purpose (≤3 sentences):** Generating video that stays coherent to a single underlying 3D world is difficult under large viewpoint changes, where existing methods struggle to keep individual objects' surfaces and layouts stable. The authors target object-level consistency specifically, rather than only scene-level consistency.

**Breakthrough (≤3 sentences):** The authors report Totem scoring highest overall on WorldScore (86.43 vs. 85.53 for the strongest baseline, UniWorld-View) and best on all three metrics of ConsIDVid-Bench (Object Similarity 73.2, Chamfer Distance 0.0976, MEt3R 0.0818 vs. 71.4/0.1053/0.0964 for the best baseline). On an out-of-distribution ablation against a Wan2.2 camera-branch baseline, PSNR improves from 17.31 to 25.67 and SSIM from 0.528 to 0.838.

**Tools & method (≤3 sentences):** Trained on ~80K clips (about 40K each) from RealEstate10K and DL3DV, resampled to 15fps, split into 81-frame windows, and center-cropped to 720p. Evaluation uses WorldScore (2,000 static examples), the public ConsIDVid-Bench subset (370 videos), and a custom 400-clip out-of-distribution benchmark; no hardware specifics are reported in the available text.

**Limitation (≤3 sentences):** The available paper content contains no dedicated limitations section and the authors do not explicitly discuss failure cases beyond qualitative baseline-artifact comparisons (e.g., blurred textures, distorted structures in competing methods). Hardware and training cost are also not disclosed in the visible text, limiting reproducibility assessment.

# Near-misses
None identified in this batch — every candidate either qualified on affiliation (6 papers, listed above) or was excluded as genuinely off-topic for this tracker (6 papers: a video-reward-modeling/RLHF benchmark, two generic training-free diffusion-caching/acceleration papers, a pure robot-manipulation VLA paper, and a CFD-style liquid-dynamics forecasting paper — none centered on 3D generation/reconstruction, world models in the tracked sense, character animation/motion, or game engines/rendering).
