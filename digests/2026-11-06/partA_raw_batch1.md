## PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State
- **arXiv:** 2611.07867 · https://arxiv.org/abs/2611.07867
- **Submitted:** 2026-11-05
- **Authors:** Jihai Zhang, Yuhan Zhou, Junyou Li, Deheng Ye, Qi Dou, Yu Cheng
- **Qualifying affiliation(s):** Tencent — Junyou Li, Deheng Ye (Jihai Zhang's internship was at Tencent; other authors: Chinese University of Hong Kong, Wellington College, Nanyang Technological University)
- **Categories:** cs.CV, cs.LG
- **Open release:** code + weights — https://github.com/MajorDavidZhang/PlayGen-2 (paper states "code and pretrained model weights are publicly available")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PlayGen2 is a real-time interactive world model that separates learned 3D state evolution from neural rendering, keeping a persistent world memory (a volumetric occupancy grid for static geometry plus identity-indexed 3D states for the player and other entities) and a separate neural renderer that turns depth/semantic projections of that state into first-person views. Tested on Doom (Freedoom2 MAP01 for training, seven unseen Scythe levels for evaluation), the authors report geometry-aware player motion and player-NPC interaction that generalizes zero-shot to unseen maps. The system supports multiplayer through model composition and rule-based gameplay changes.
**Purpose (≤3 sentences):** The paper targets real-time, interactive "playable world" generation where a game can be played rather than merely watched, addressing the gap between video-generation-style world models (which tend to drift and lack persistent, explicit state) and traditional game engines.
**Breakthrough (≤3 sentences):** The authors report backend latency of about 160ms on a consumer MacBook Pro (M4 Pro) — 200.6ms serial / 275.7ms pipelined at 8 denoising steps, 4.98–7.16 FPS — using a 41.2M-parameter world-state model and a 29.1M-parameter renderer (plus a 55.3M-parameter VAE) at 160×120 resolution. They state the explicit 3D-state design is what allows zero-shot generalization to unseen maps and compositional multiplayer, rather than the model relearning geometry from pixels alone.
**Tools & method (≤3 sentences):** Training used roughly 500 hours (~500GB) of ViZDoom gameplay from a rule-based controller on four NVIDIA A100 GPUs (288 GPU-hours, ~3 days); the method combines a volumetric occupancy grid, identity-indexed entity states, and a neural renderer conditioned on depth/semantic projections, with no runtime collision correction (physical consistency relies on learned dynamics).
**Limitation (≤3 sentences):** The authors note that because depth/semantic conditions don't specify native texture details, reference-based metrics on unseen maps reflect both structural and appearance discrepancies and must be read alongside qualitative results; local-initialized generation is scored against an unpaired reference pool with no aligned ground truth; and design comparisons use checkpoints with differing training budgets rather than budget-matched retraining. The system has no runtime collision correction, so physical consistency depends entirely on learned dynamics (acknowledged by the authors, not just observed).

---

## Bri3D: Bridging the Object-Scene Gap in Single-Image 3D Generation via Scene-Anchor
- **arXiv:** 2611.07961 · https://arxiv.org/abs/2611.07961
- **Submitted:** 2026-11-05
- **Authors:** Hongye Hou, Shuai Zhang, Hongjie Li, Zhuoxiao Li, Haiping Wang, Yuan Liu, Wufan Zhao
- **Qualifying affiliation(s):** Alibaba — one of Hongye Hou / Shuai Zhang / Hongjie Li at Taobao & Tmall Group of Alibaba (the paper lists Hong Kong University of Science and Technology (Guangzhou), Taobao & Tmall Group of Alibaba, and Hong Kong University of Science and Technology as the three affiliations but the author-to-affiliation mapping was lost in page extraction)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Bri3D generates compositional 3D scenes from a single image by first predicting a color-coded scene scaffold of coarse object geometry and layout, extracting each object as a voxel "scene anchor," refining it into a pose-preserving support, and then using a frozen object generator to synthesize detailed textured geometry within that anchor. The authors state this separates scene organization from object-level detail and reuses pretrained object-generation priors rather than retraining a scene-level generator from scratch. They report better scene layout, object geometry, visual quality, and generalization than prior object-to-scene methods (SAM3D, MIDI, SceneGen).
**Purpose (≤3 sentences):** The paper addresses a stated failure mode of existing single-image object-to-scene 3D generators: under limited scene-level supervision they struggle to coordinate multiple objects, and naively extending object generators to whole scenes can corrupt geometry, instance scale, orientation, and pose.
**Breakthrough (≤3 sentences):** On the MIDI-cleaned 3D-FRONT test split, the authors report CD-S 0.87 and BBox IoU 0.7540 versus the best baseline SAM3D's CD-S 2.11 and BBox IoU 0.6271; on a 300-scene cross-dataset test (HSSD/BlendSwap) Bri3D scores CD-S 3.42 versus SAM3D's 3.85. Full-scene generation takes 78.4s versus 230.2s (SceneGen) and 179.6s (SAM3D), with a reported object-collision rate of 4% versus 14–38% for the three baselines.
**Tools & method (≤3 sentences):** Training data is Objaverse-XL (object-level) plus a ~15,000-scene cleaned split of 3D-FRONT (scene-level) from MIDI; evaluation adds a 300-scene cross-dataset test (150 HSSD + 150 BlendSwap) and qualitative-only tests on ScanNet. The frozen object generator synthesizes textured geometry inside each refined voxel anchor, decoupling per-object detail from scene-level layout.
**Limitation (≤3 sentences):** The authors report that under extreme clutter or ambiguous layouts the method "may incorrectly merge distinct objects," and in scenes with more than 30 objects "it may omit some instances." They also state that a systematic treatment of structural elements (floors, walls, ceilings) — excluded from the main experiments — remains future work, with the current extension "preliminary" and dependent on reliable labels.

---

## EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling
- **arXiv:** 2611.08477 · https://arxiv.org/abs/2611.08477
- **Submitted:** 2026-11-05
- **Authors:** Yanlin Jin, Bowen Yang, Cheng Zhang, Yifan Yang, Zhe Li, Jianfei Cai, Kai Zhu
- **Qualifying affiliation(s):** Ant Group (Ant Digital Technologies) — among Yanlin Jin / Bowen Yang / Cheng Zhang / Yifan Yang (other affiliations: Monash University, Institute of Automation, Chinese Academy of Sciences); **FLAG: borderline** — Ant Group is a separate entity from Alibaba Group and is treated here as a comparable top-tier industry lab per the tracker's borderline rule, not as "Alibaba" itself
- **Categories:** cs.CV
- **Open release:** none (project page only, no code/weights stated) — https://www.neiljin.site/egogeneralist_page/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** EgoGeneralist adapts pretrained video generators to jointly handle action-conditioned egocentric video generation, 3D hand/body pose estimation, and joint action-video generation, using a "role-adaptive action renderer" that represents metric 3D motion as both a controllable signal and a recoverable generation target. The authors report the model generalizes from controlled lab recordings (EgoDex) to diverse unseen scenes and interactions (Xperience-10M) while preserving pretrained visual quality.
**Purpose (≤3 sentences):** The paper targets the gap between video generators' strong visual priors and their lack of a native, metric 3D representation of human action, aiming for a single framework spanning five action-video tasks instead of separate task-specific models.
**Breakthrough (≤3 sentences):** On EgoDex, the authors report hand pose estimation Abs-MPJPE of 27.73mm versus 111.98mm for the HaWoR baseline, and text-to-video PCK of 67.91% versus 35.41% for Wan2.2 Fun-Control; on the HOT3D world-action policy benchmark, mean minimum target distance is 3.81cm versus 6.32cm for VITRA, with 58.59% of trials reaching within 2cm.
**Tools & method (≤3 sentences):** The model is trained on EgoDex (one 41-frame clip per episode, 111-clip in-domain test set) and evaluated for out-of-distribution generalization on 50 Xperience-10M clips and for world-action policy on 50 HOT3D initial states; a "cross-stream action-video coupling" mechanism links metric motion to visual dynamics through lightweight adaptation while keeping the pretrained video prior frozen/preserved.
**Limitation (≤3 sentences):** The authors state that EgoDex's multi-camera fusion "introduces projection mismatches between 3D annotations and images," which can carry into generated sequences and affect action-video alignment; they also note the EgoDex training data "cover a limited range of environments and body motion" (no standing, walking, or outdoor activity), limiting generalization to those regimes.

---

## Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation
- **arXiv:** 2611.07294 · https://arxiv.org/abs/2611.07294
- **Submitted:** 2026-11-05
- **Authors:** Tao Jun Lin, Jinhong Ni, Ruyi Zha, Yifu Wang, Xibin Song, Pan Ji, Hongdong Li
- **Qualifying affiliation(s):** Amazon — Hongdong Li (Amazon Scholar, part-time; his full-time appointment is at the Australian National University); other authors are at ANU and Vertex Lab Technology Limited. **FLAG: borderline** — the Amazon affiliation is a part-time "Amazon Scholar" appointment, not the author's primary institution.
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes Householder Motion Embedding (HME), a training-free way to encode motion control into the initial noise of a video diffusion model using a sequence of Householder reflections that form an orthogonal transform on each spatial location's channel vector. Unlike prior noise-warping methods, HME adds cross-frame temporal correlation for motion control while keeping each frame's noise exactly i.i.d. Gaussian, avoiding the need for an expensive Jacobian-based correction. The authors report it matches or beats state-of-the-art motion control while running 2.7x faster than the GWTF noise-warping baseline.
**Purpose (≤3 sentences):** The paper addresses a stated tension in motion-controllable video generation: existing noise-warping methods inject motion by spatially warping noise, which breaks the i.i.d. Gaussian structure diffusion models are trained on and requires costly correction.
**Breakthrough (≤3 sentences):** The authors report 2.80ms per latent at reflection count K=2, a 2.7x speedup over GWTF (7.63ms) and 13.6x over HIWYN (38.00ms), with roughly 0.5–6MB of extra peak memory versus 76MB (GWTF) and 49,384MB (HIWYN). On DAVIS motion transfer (γ=0.5 vs. GWTF) they report Flow EPE improving from 5.644 to 4.486 and PSNR from 14.748dB to 15.162dB; on DL3DV camera control (γ=0.3) PSNR improves from 12.626dB to 13.656dB.
**Tools & method (≤3 sentences):** Built on CogVideoX-5B-I2V and trained on ~100K videos from RealCam-Vid (sourced from RealEstate10K, MiraData, DL3DV-10K); evaluated on DAVIS (45 videos), MC-Bench (965 samples) and 200 DL3DV scenes. HME works with any network architecture and plugs into standard video-diffusion fine-tuning without architectural changes.
**Limitation (≤3 sentences):** The authors state the method "relies on accurate optical flow for training, so noisy motion estimates can weaken motion adherence," and that subjects with complex non-rigid geometric motion "remain challenging," left for future work. They also note the reflection count K involves an expressivity-efficiency trade-off requiring tuning, and that baselines were evaluated using released checkpoints rather than retrained on the authors' data/flow estimator.

# Near-misses
- 2611.08407 · Social Humanoid: Socially Responsive Human-Humanoid Interaction · has qualifying industry co-authors (Sony Group Corporation, Meta) but the paper is about controlling a physical Unitree G1 humanoid robot's whole-body motion, not game/virtual-character animation or any of the four tracked topics — off-topic.
- 2611.08156 · La-JEPA: Compact Robot Policies with Latent World Modeling · has a borderline industry affiliation (Huawei Technologies, as author internships) but is a robot-control-policy paper (RoboTwin/LIBERO-Plus benchmarks), not a game/3D/character-animation/engine world model — off-topic.
- 2611.07873 · PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation · screened as a "Google" hit, but verified authors (Peking University, Pengcheng Laboratory) show no Google or other qualifying industry affiliation — the screen match was almost certainly a false positive (e.g. a "Google Scholar" link), not a textual Google affiliation; no qualifying industry author found.
- 2611.07551 · Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion · screened as a "Google" hit, but it has no arxiv.org/html version (404), so affiliations could not be verified against the author block; the abs page itself shows no stated institutional affiliation for any author — affiliation unverifiable, likely a false Google Scholar match.
