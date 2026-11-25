## PointX: Multi-View Consistent Intrinsics by Querying Surface Points
- **arXiv:** 2611.33157 · https://arxiv.org/abs/2611.33157
- **Submitted:** 2026-11-24
- **Authors:** Miguel Farinha, Sam Sartor, Iliyan Georgiev, Giuseppe Vecchio, Ronald Clark, Michael Fischer
- **Qualifying affiliation(s):** Adobe — Adobe Research (paper lists Adobe Research and University of Oxford as the two affiliations; a footnote notes one author's work was done during an Adobe Research internship)
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** Per-pixel intrinsic-decomposition methods (albedo, roughness, metallicity, normals, irradiance) give the same 3D surface point different answers in different views. The authors propose PointX, a feed-forward model that instead predicts intrinsics once per queried 3D surface point rather than per pixel. A multi-view transformer encodes a set of unposed images, and PointX pools that point's tokens across every view it appears in before decoding its intrinsics.
**Purpose (≤3 sentences):** To make multi-view intrinsic decomposition consistent by construction, enabling view-consistent relighting and material editing instead of ad hoc multi-view averaging.
**Breakthrough (≤3 sentences):** The authors report PointX is more cross-view consistent than existing per-pixel methods, is competitive with them on single-image accuracy, and improves further as more views are added.
**Tools & method (≤3 sentences):** Multi-view transformer encoder over unposed images; per-point token pooling across views; a single decode per queried surface point rather than per pixel/per view.
**Limitation (≤3 sentences):** Not stated in the retrieved material (abstract/author block only); accuracy is explicitly described as only "competitive" rather than superior in the single-image case.

## RFW-W: Scaling Physical Asset Universes for Generative Embodied Simulation
- **arXiv:** 2611.33013 · https://arxiv.org/abs/2611.33013
- **Submitted:** 2026-11-24
- **Authors:** 25 authors, including Jiawei Weng, Rui Zhang, Saining Zhang, Hao Zhao, Chaojian Li (full list on arXiv page)
- **Qualifying affiliation(s):** Alibaba — Alibaba Group (one of six listed affiliations, alongside Tsinghua, NTU, Peking University, Nanjing University, HKUST; per-author mapping not shown in the extracted HTML)
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** The paper presents RFW-W, a unified 3D asset platform spanning rigid, articulated, and deformable objects for embodied simulation, reporting roughly one million asset records across the three types. It describes a common interface for generating/verifying each asset type and for retrieval and scene assembly.
**Purpose (≤3 sentences):** To give embodied-AI/robotics training pipelines a single large-scale source of verified, diverse 3D physical assets instead of fragmented rigid/articulated/deformable datasets.
**Breakthrough (≤3 sentences):** The authors report that policies trained on the platform's assets ("RFW-R") outperform the strongest baseline on five RoboTwin benchmark tasks, in both clean and randomized settings.
**Tools & method (≤3 sentences):** Per-asset-type generation/verification pipelines for rigid, articulated, and deformable 3D objects; a shared retrieval/scene-assembly interface; evaluation on the RoboTwin robotic-manipulation benchmark.
**Limitation (≤3 sentences):** Not stated in the retrieved material. Note: this is a robotics/embodied-simulation asset platform rather than a games-specific tool, though its core contribution is 3D asset generation at scale.

## PhysMend: Verification-Guided Program Refinement for Physics-Aware Video Generation
- **arXiv:** 2611.32821 · https://arxiv.org/abs/2611.32821
- **Submitted:** 2026-11-24
- **Authors:** Meilong Xu, Ziyi Zhao, Bhagyashree Puranik, Shayda Moezzi, Yixiao Zhang, Kushan Thakkar
- **Qualifying affiliation(s):** Amazon — one author (paper's own footnote: "work done during the internship at Amazon"; affiliations listed are Stony Brook University, Amazon, Northeastern University, with no exact per-author mapping shown in the extracted HTML)
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** PhysMend is a training-free framework that makes generated videos better follow physical laws by representing a target event as an editable "physical program," then verifying and repairing that program against a simulated rollout and the depth video conditioning the generator — not against the generated video pixels themselves.
**Purpose (≤3 sentences):** To fix physically implausible video-generation outputs (objects passing through each other, implausible motion) without retraining the underlying video generator.
**Breakthrough (≤3 sentences):** The authors report gains on the Physics-IQ, PhyGenBench, and VBench-2.0 benchmarks across several generator backbones, including raising Alibaba's Wan-VACE model's Physics-IQ score from 27.33 to 39.40.
**Tools & method (≤3 sentences):** A hybrid verifier checking event semantics, physical plausibility, solver stability, and visibility; a vision-language model restricted to judging only event semantics (so it cannot override failed physical measurements); tested against Wan-VACE and other video-generation backbones.
**Limitation (≤3 sentences):** Not stated in the retrieved material.

## COHERE4D: Training-Free Dense Surface Alignment for Coherent Metric 4D Human-Scene Reconstruction
- **arXiv:** 2611.32482 · https://arxiv.org/abs/2611.32482
- **Submitted:** 2026-11-24
- **Authors:** Zhumei Wang, Shaofei Wang, Xiang An, Mingtao Pei, Siyuan Huang
- **Qualifying affiliation(s):** FLAG: borderline — Xiang An, MiniMax (other authors are Beijing Institute of Technology / BIGAI academics)
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** Human-mesh-recovery models produce metric-scale body meshes but no scene grounding, while scene-reconstruction models give globally consistent geometry/camera motion without reliable metric scale. COHERE4D is a training-free framework that registers the human surfaces predicted by pretrained human models directly onto pretrained scene reconstructions, using dense pixel-aligned 3D correspondences and RANSAC with cross-frame consensus to reject outliers, then solves for one shared scale plus per-frame human translation.
**Purpose (≤3 sentences):** To combine separately pretrained human-mesh and scene-reconstruction models into one metrically and temporally coherent 4D human-in-scene reconstruction, without extra training.
**Breakthrough (≤3 sentences):** The authors report better human-scene alignment, metric scene/camera-pose reconstruction, and global human-motion estimation than prior methods, at about 4 ms/frame overhead and inference up to 14 FPS.
**Tools & method (≤3 sentences):** Dense pixel-aligned 3D surface correspondences; RANSAC with cross-frame consensus for outlier rejection; sequence-level shared-scale solve plus per-frame human translation solve.
**Limitation (≤3 sentences):** Not stated in the retrieved material.

## MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction
- **arXiv:** 2611.32462 · https://arxiv.org/abs/2611.32462
- **Submitted:** 2026-11-24
- **Authors:** 18 authors, including Bozhou Li, Yushuo Guan, Yuanxing Zhang (KlingAI Research), plus academics from Peking University, Shanghai Jiao Tong University, Renmin University of China, HKUST, HKU, Nanjing University, Tsinghua
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (3 of 18 authors)
- **Categories:** cs.CV (primary), cs.CL
- **Open release:** none stated

**Summary (≤3 sentences):** MAGPIE represents an intended multi-reference image composition as a simplified, executable 3D scene built from a Blender program. A coding agent checks the resulting geometry/rendering against the instruction and revises the program, and the proxy rendering then guides a downstream image generator trained on a dataset the authors built, MAGPIE-Instruct-3K.
**Purpose (≤3 sentences):** To give multi-reference, instruction-following image generation an explicit, checkable 3D layout to condition on, instead of relying on the generator to infer spatial composition implicitly.
**Breakthrough (≤3 sentences):** The authors report gains for both Qwen and FLUX backbones on the DreamOmni2 and SconeEval benchmarks, including a 28.21 percentage-point improvement in overall success on DreamOmni2 for FLUX.
**Tools & method (≤3 sentences):** Executable Blender-program scene representation; coding-agent-driven geometry/render verification and revision loop; MAGPIE-Instruct-3K training dataset; evaluated on Qwen and FLUX image generators.
**Limitation (≤3 sentences):** Not stated in the retrieved material.

## A Mesh to Remember: Persistent Appearance for Interactive Video Worlds
- **arXiv:** 2611.32445 · https://arxiv.org/abs/2611.32445
- **Submitted:** 2026-11-24
- **Authors:** Joonghyuk Shin, Alex Trevithick, Katarína Tóthová, Liyuan Zhu, Shengyu Huang, Jaesik Park, Shalini De Mello, Laura Leal-Taixé, Riccardo de Lutio, Haithem Turki
- **Qualifying affiliation(s):** NVIDIA — Alex Trevithick, Katarína Tóthová, Liyuan Zhu, Shengyu Huang, Shalini De Mello, Laura Leal-Taixé (6 of 10 authors; Jaesik Park is Seoul National University, Haithem Turki is Stanford, Joonghyuk Shin's contribution was done during an NVIDIA internship)
- **Categories:** cs.CV
- **Open release:** none stated

**Summary (≤3 sentences):** M2R ("A Mesh to Remember") is a few-step, causal video renderer for interactive video-world models, which otherwise tend to lose visual consistency over long user interactions. It stores renderer features on the object meshes they depict, in each object's own local frame, and retrieves those features by rasterizing the mesh whenever that surface reappears.
**Purpose (≤3 sentences):** To keep object appearance persistent across camera/object movement and revisits in interactive, playable video-world generation, and to let that memory scale with visible surface area rather than with elapsed frame count.
**Breakthrough (≤3 sentences):** The authors report better consistency than prior methods on static, dynamic, and multi-agent benchmarks, plus real-time rendering at 720p and 40 FPS; the model is trained only on synthetic data but is reported to transfer zero-shot to real indoor scans and to worlds generated by coding agents.
**Tools & method (≤3 sentences):** Mesh-anchored, per-object local-frame feature storage; mesh-rasterization-based feature retrieval; training on synthetic data only, with zero-shot evaluation on real scans and agent-generated worlds.
**Limitation (≤3 sentences):** Not stated explicitly in the retrieved material beyond the synthetic-only training regime noted above.

# Near-misses
- 2611.32548 · SetCon: Setup-Conditioned IMU-Language Learning from 3D Human Motion · off-topic (final review): wearable-IMU activity-recognition research using 3D mocap only as a calibration signal; not itself a 3D/world-model/character-animation/game-engine contribution. Company affiliation was borderline (Bosch Sensortec) in any case.
- 2611.32035 · DeCo-Attention: Decompose to Compensate for Low-Precision Attention · off-topic (final review): a low-precision-attention quantization/systems paper; evaluated on a video-generation model (Wan2.2) but the contribution itself is generic attention-kernel efficiency, not 3D/world-model/character-animation/game-engine work.
- 2611.31974 · Coding4Games: Can Modern Coding Agents Play Modern Video Games? · off-topic (final review): a benchmark for coding-agent capability (writing programs that play games), not a 3D, world-model, character-animation, or game-engine technical contribution.
- 2611.32547 · Contact Geometry for Generative Models: An Unbalanced Optimal Transport Formulation · off-topic: an optimal-transport/generative-modeling theory paper; video generation is only one of three unrelated evaluation domains (alongside biological-dynamics reconstruction and image-to-image translation), and no qualifying industry affiliation was confirmed (authors appear to be academic/Bosch-adjacent robotics researchers, unconfirmed).
- 2611.32337 · Get the Next Moment Right: Short-Term Event Planning for Physically Plausible Video Generation · academic-only: all authors are Tsinghua University / Harbin Institute of Technology / Pengcheng Laboratory, no qualifying industry affiliation found.
- 2611.32335 · GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM · academic-only: authors are Hunan University, Tsinghua, Karlsruhe Institute of Technology, University of Oxford, and a construction engineering bureau; the screen's "Google" match was a false positive (no "Google" found anywhere on the page) and no qualifying industry affiliation exists.
- 2611.32228 · Disentangling Visual Dynamics for World Model Planning · affiliation unverifiable: no arxiv.org/html version exists for this id (404), so author affiliations could not be confirmed from the HTML page as required; not verified from the abs page alone per policy.
- 2611.32202 · SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens · no qualifying affiliation: authors are UT Austin, Dolby Laboratories, and University of Colorado Boulder; Dolby is not a tracked/comparable company, and the screen's "Google" match was a false positive (no "Google" found anywhere on the page).
