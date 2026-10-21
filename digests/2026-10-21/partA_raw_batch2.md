# Part A — Papers
Window: last 30 days (2026-09-21 to 2026-10-21). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: fixed candidate batch (pre-screened leads from caller), each verified directly against its arXiv abstract page and arXiv HTML (ar5iv-style) page. Qualifying papers: 4 (2 flagged borderline).

---
## GALA: Geometry-Aware Language Model for Controllable Object Arrangement
- **arXiv:** 2610.28280 · https://arxiv.org/abs/2610.28280
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Chucheng Xiang, Runze Wang, Zhi Deng, Ruchao Bao, Yuanwei Zhang, Yuxuan Xie, Hanliu Wang, Liangzhen Fei, Wenzheng Wu, Cheng Wan, Peifeng Li, Zhongyuan Liu, Ligang Liu
- **Qualifying affiliation(s):** Tencent — Zhi Deng (listed as corresponding author, Tencent, Shenzhen) and several co-authors (e.g. Chucheng Xiang, Runze Wang, Yuxuan Xie, Hanliu Wang) carry dual Tencent + university (USTC / Tsinghua) affiliations per the paper's affiliation block. Not borderline — direct Tencent affiliation confirmed.
- **Categories:** cs.GR (primary); cs.AI; cs.CV
- **Open release:** dataset "will be open-sourced" per the abstract (not yet released); no code/weights stated; project page: https://xccelephant.github.io/paper/gala/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GALA is a geometry-aware language model that predicts the 6D pose of one target object at a time for controllable 3D object arrangement, using explicit point-cloud perception instead of oriented-bounding-box (OBB) approximations. It is trained in two stages — geometry/text alignment pretraining, then autoregressive placement fine-tuning — on a curated multi-source scene dataset of room layouts and furniture arrangements. The authors also build a multi-stage plan-place-verify agent pipeline on top of the model for text-driven scene generation.

**Purpose (≤3 sentences):** The paper targets fine-grained placement constraints such as support and containment that existing OBB-based scene-layout methods cannot reason about because OBBs are blind to detailed object geometry. It aims to make language-model-driven object placement in 3D scenes geometrically accurate rather than approximate.

**Breakthrough (≤3 sentences):** The authors report their 0.7B-parameter model reaches 65.62% Within Valid Rate and 78.59% Instruction Valid Rate on their held-out test split, versus 22.53%/42.29% for a zero-shot GPT-OSS-120B baseline and 10.96%/37.71% for an adapted LayoutVLM baseline (Table 1). It also reports a lower Float Rate (4.63%) and a Support Ratio (96.03%) close to the OBB-based ATISS/ReSpace baselines, which cannot take instructions at all.

**Tools & method (≤3 sentences):** GALA combines a point-cloud perception module with a geometry-to-text projection layer inside an interleaved multimodal context, trained via the two-stage strategy above. It is benchmarked against ATISS, ReSpace, an adapted LayoutVLM, and GPT-OSS-120B on a benchmark the authors build from a SpatialLM-PCG-style dataset expansion.

**Limitation (≤3 sentences):** The authors state GALA currently supports only a predefined set of placement instructions and cannot handle open-ended placement requests, and that performance degrades when generalizing to previously unseen container geometries. They also note that because placement is autoregressive, errors in earlier object placements can propagate to later ones.

---
## Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds
- **arXiv:** 2610.27999 · https://arxiv.org/abs/2610.27999
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Jihai Zhang, Runjia Qian, Kaiqin Kong, Biao Jiang, Puyi Wang, Siru Chen, Tianle Li, Guanjie Chen, Junyi Wu, Chubin Chen, Yuanhang Li, Kaichen Huang, Haobo Zhang, Yangguang Li, Wei Yu, Guibin Chen, Yu Cheng, Yahui Zhou
- **Qualifying affiliation(s):** SkyworkAI — listed affiliation for Jihai Zhang, Puyi Wang/Siru Chen/Tianle Li/Guanjie Chen/Junyi Wu, Chubin Chen/Yuanhang Li/Kaichen Huang/Haobo Zhang/Yangguang Li, and Wei Yu/Guibin Chen/Yu Cheng/Yahui Zhou (the latter is "Project Lead and Corresponding Author"). **FLAG: borderline** — SkyworkAI (the AI lab of publicly-listed Kunlun Tech) is not on the tracker's default company list, but is kept per the tracker's "clearly comparable top-tier lab" rule given it is the originating lab of the prior Matrix-Game releases.
- **Categories:** cs.CV (primary); cs.GR
- **Open release:** code (GitHub), model weights (Hugging Face), and low-poly game assets — the abstract states these are released; project page: https://matrix-game-v4-0.github.io/page/
- **Shipped counterpart:** none found (the paper describes a Steam technical preview as a near-term future goal, not yet shipped)

**Summary (≤3 sentences):** Matrix-Game 4.0 separates game execution from visual generation via an "executable game harness": a lightweight game engine holds persistent world state and interaction rules, a multimodal coding agent turns player ideas into game code and dynamic scene captions, and an autoregressive-video-model renderer turns engine-rendered low-poly proxies into detailed visuals conditioned on those captions. The renderer is trained on paired low-poly/high-fidelity (UE5) video data and distilled into a causal, few-step generator.

**Purpose (≤3 sentences):** The paper argues controllable video generation alone is insufficient for genuinely "playable" worlds, which additionally need persistent state, executable rules, low interaction latency, and mechanics beyond navigation. It proposes an architecture in which an external engine/agent system handles state and rules while the video model is responsible only for rendering.

**Breakthrough (≤3 sentences):** The authors report 480p, 60 FPS gameplay on a single NVIDIA RTX 5090 with a measured key-press-to-display latency of 112 ms; single-step generation reaches 83 FPS steady-state throughput at 18.2 GiB peak GPU memory, with 67 FPS on an RTX 5080 and 58 FPS on an RTX 5070 Ti under fixed prompts. They demonstrate customizable shooter and driving games with engine-enforced mechanics.

**Tools & method (≤3 sentences):** The system pairs a lightweight game engine and a multimodal coding agent (for natural-language scene/gameplay creation and editing) with a causal video generator distilled to produce four-frame chunks using one or two denoising steps, trained on paired UE5 gameplay data. Code, model weights, and low-poly game assets are released alongside the paper.

**Limitation (≤3 sentences):** The authors state that in the near term they will focus on reducing inference cost and hardware requirements toward a Steam technical preview, and list improving visual fidelity, adding a higher-resolution refinement stage, and exploring multiplayer rendering as future work, implying current constraints on hardware cost, resolution, and multiplayer support (observed from stated future work, not phrased as a direct limitation).

---
## Decoupling Action from Egocentric Observation for World Simulation
- **arXiv:** 2610.27946 · https://arxiv.org/abs/2610.27946
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Yue Ma, Pengjie Song, Xinyu Wang, Yi He, Zeqian Long, Fangneng Zhan, Kaichen Zhou, Hongyu Liu, Hongfa Wang, Peihao Li, Haoyang Huang, Nan Duan, Qifeng Chen
- **Qualifying affiliation(s):** JD Explore Academy (JD.com) — appears in the paper's combined institution line ("HKUST, Tsinghua University, Stanford University, MIT, JD Explore Academy") attached to the author group that includes Haoyang Huang and Nan Duan; the arXiv HTML source renders affiliations as one block rather than mapped per author, so the exact author-to-institution pairing within that group is not separable from the source. **FLAG: borderline** — JD.com is named explicitly in the tracker's own guidance as an example company to flag rather than silently drop.
- **Categories:** cs.CV
- **Open release:** code — GitHub repo linked (https://github.com/mayuelala/EgoACT); project page: https://ego-act.github.io/; the EgoActionBench benchmark is introduced alongside the method
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** EgoACT is a test-time framework for "egocentric action transfer" — reproducing the semantic action from an egocentric reference video in a new visual context — that operates directly on the denoising process of a video diffusion model without extra geometric estimators. It combines Velocity-guided Structure Anchoring (stabilizing reference-consistent hand-object structure early in denoising) with Sparse Correspondence Calibration (refining local correspondences mid-to-late in denoising). The authors also introduce EgoActionBench, a benchmark of 350 reference manipulation videos and 1,400 target prompts.

**Purpose (≤3 sentences):** The paper targets a gap in two prior approaches to action transfer: condition-guided methods that convert video into explicit geometric controls (introducing geometric-estimation error) and motion-transfer methods that use motion patterns alone (causing hand-structure collapse and implausible contact). It aims for action transfer that preserves physically plausible hand-object interaction for scalable world simulation, embodied policy learning, and robotic data generation.

**Breakthrough (≤3 sentences):** On EgoActionBench, the authors report EgoACT outperforms five baselines (InterDyn, Mask2IV, CosHand, DiTFlow, VACE) on every reported metric, including Motion Fidelity (0.2750 vs. 0.1910–0.2434 for baselines) and VBench Aesthetic Quality (0.5633 vs. 0.4226–0.5065) (Table 1).

**Tools & method (≤3 sentences):** EgoACT is evaluated against InterDyn, Mask2IV, CosHand, DiTFlow, and VACE using text-similarity and VBench-style metrics (temporal/appearance/subject/background consistency, aesthetic quality, motion smoothness) on the EgoActionBench benchmark the authors construct from egocentric manipulation videos.

**Limitation (≤3 sentences):** The authors state EgoACT still struggles with very fast hand or object motion, producing motion blur, temporal aliasing, or loss of hand-object correspondence, which they attribute to the base video diffusion model not being trained for rapid egocentric dynamics. They plan to extend the method to longer-horizon, multi-step action sequences in future work.

---
## EGGHead: Efficient Generalizable Gaussian Heads from a Single Image
- **arXiv:** 2610.26898 · https://arxiv.org/abs/2610.26898
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Pilseo Park, Andrew Hou, Michel Sarkis, Ning Bi, Yiying Tong, Xiaoming Liu
- **Qualifying affiliation(s):** Qualcomm Technologies, Inc. — Ning Bi (listed with current Qualcomm Technologies, Inc. affiliation); Michel Sarkis is listed as "Formerly of Qualcomm Technologies." Qualcomm is on the tracker's default list, so no borderline flag on the company itself.
- **Categories:** cs.CV
- **Open release:** none found (no code/project-page link stated in the paper)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** EGGHead reconstructs a photorealistic, generalizable 3D Gaussian head avatar from a single image in a single forward pass, using a Gaussian-allocation algorithm that assigns a fixed budget of Gaussians to the head's semantic regions. The method is positioned against mesh/3DMM-based, NeRF-based, and prior Gaussian-splatting head-reconstruction methods.

**Purpose (≤3 sentences):** The paper addresses a three-way trade-off in head-avatar modeling between representation power, rendering/enrollment efficiency, and generalizability — prior Gaussian-splatting methods still scale with the number of rasterized Gaussians and often have high "enrollment" (optimization/preparation) time.

**Breakthrough (≤3 sentences):** On the NeRSemble dataset, the authors report EGGHead renders at 121.19 FPS versus 5.26 FPS (E3DGE), 33.61 FPS (G-NeRF), and 43.43 FPS (GAGAvatar), with an enrollment time of 1.54 seconds — slower than GAGAvatar's 0.06 seconds but faster than E3DGE's 8.63s and G-NeRF's 5.96s (Table 4). The authors state EGGHead also outperforms these single-image face-modeling baselines in reconstruction quality and novel-view synthesis.

**Tools & method (≤3 sentences):** EGGHead's Gaussian-allocation algorithm assigns Gaussians to semantic head regions under a fixed budget in a single forward pass; pseudo-ground-truth supervision for this allocation is derived from single in-the-wild FFHQ images. It is benchmarked against E3DGE, G-NeRF, and GAGAvatar on the NeRSemble dataset.

**Limitation (≤3 sentences):** The authors state the model does not decompose texture into albedo and illumination and so cannot support relighting, and that uneven lighting can break its face-symmetry assumption, causing incorrect shadow reflection or overexposure (mitigable with an off-the-shelf delighting preprocessing step). They also note fully frontal inputs may prevent complete reconstruction of the back of the head.

---

Near-misses dropped: 4 (1 off-topic, 2 no qualifying affiliation — purely academic, 1 affiliation unverifiable — no HTML version). Double-verify pass: every included paper's title, author list, v1 submission date, subject categories, and qualifying affiliation were re-confirmed directly from both its arXiv abstract page and its arXiv HTML page (fetched 2026-10-21); none were found withdrawn.

# Near-misses
- 2610.28192 · Offline Makes Online Better: Calibrated Cache Compression for Video Generation · affiliation unverifiable — no arXiv HTML version exists (404); the abstract page lists only 3 authors (Zhen Wang, Ning Lai, Qingtao Yu) with no stated institution, and no "Google" text is accessible anywhere to confirm the pre-screen match.
- 2610.28131 · OV-Foam: How 3D Representations Shape Semantic Feature Lifting · no qualifying affiliation — the abstract page's explicit author-affiliation footnote lists only King Abdullah University of Science and Technology (KAUST) and Universidad Panamericana; purely academic, no Google or other qualifying industry affiliation (HTML version also unavailable, 404).
- 2610.27998 · LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning · off-topic and no qualifying affiliation — a generic quadruped-robot teleoperation/data-collection paper (Unitree Go2 base + AgileX Piper arm), not 3D/world-model/game content; the "Intel" pre-screen hit is from "Intel RealSense D435/D405" cameras used as sensor hardware, not an author affiliation.
- 2610.27914 · World Models with Configurable Perception · no qualifying affiliation — the HTML author/affiliation block lists only East China Normal University and HKUST; no "Google" or "DeepMind" text appears anywhere in the paper, so the pre-screen match for Google is a false positive.
