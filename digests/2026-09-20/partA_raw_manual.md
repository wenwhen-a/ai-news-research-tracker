## PART: Learning 3D Part Assembly and Retrieval with Transformers
- **arXiv:** 2609.19872 · https://arxiv.org/abs/2609.19872
- **Submitted:** 2026-09-17
- **Authors:** Ruchao Bao, Wenzheng Wu, Chucheng Xiang, Zhongyuan Liu, Yuan Liu, Jinxin Dong, Ligang Liu, Ziqi Wang
- **Qualifying affiliation(s):** Tencent — Zhongyuan Liu, Jinxin Dong
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents PART, a unified transformer-based framework that reconstructs target 3D shapes by retrieving appropriate parts from a library and predicting their 6-DoF poses. It formulates retrieval and assembly jointly as a set-prediction problem, accepted as a SIGGRAPH Asia 2026 Conference Paper.
**Purpose (≤3 sentences):** The authors target the practical problem of assembling target shapes from existing part libraries rather than generating geometry from scratch, useful for asset reuse and shape editing pipelines.
**Breakthrough (≤3 sentences):** The authors report exploiting a duality between assembly and segmentation through joint training and segmentation-enhanced optimization, and report a Shape Chamfer Distance of 1.19 on PartNet Chair versus roughly 5–6 for prior best methods, 86.44% part accuracy and 69.90% connectivity accuracy.
**Tools & method (≤3 sentences):** Trained on curated part datasets exceeding 80K shapes drawn from PartNet, PartNeXt, 3DCoMPaT++ and PartVerse-XL, with 3D-FRONT used for scene-level evaluation and Redwood for real-world scan generalization; training used 8 NVIDIA A800 GPUs.
**Limitation (≤3 sentences):** The authors state the method does not consider inter-part connections or physical constraints, and assumes rigid transformations without part scaling or non-rigid deformation.

---

## DSD: Learning Diverse and Reusable Motor Skills via Diffusion Skill Discovery
- **arXiv:** 2609.17682 · https://arxiv.org/abs/2609.17682
- **Submitted:** 2026-09-15
- **Authors:** Sun Woo Kim, Xue Bin Peng
- **Qualifying affiliation(s):** NVIDIA — Xue Bin Peng (also Simon Fraser University)
- **Categories:** cs.LG (procedural animation, reinforcement learning)
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DSD trains a diffusion model alongside a control policy to discover diverse, reusable motor skills for simulated characters by approximating entropy gradients over states, rather than relying on discriminator-based skill discovery.
**Purpose (≤3 sentences):** The authors aim to learn character motor skills that are both diverse (covering distinct behaviors, and spatial/temporal variation) and reusable for downstream zero-shot control tasks.
**Breakthrough (≤3 sentences):** The authors report their diffusion-based entropy approximation yields skills with distinct behaviors as well as spatial and temporal variation, evaluated on three motion datasets: Reallusion (~30 min of gladiator-style sword/shield motions), LaFAN1 (~160 min of everyday/expressive motions), and MimicKit (2.5 min of highly dynamic behaviors).
**Tools & method (≤3 sentences):** The method combines a diffusion model with a reinforcement-learning policy trained under a state-marginal-entropy objective, conditioned on latent skill variables.
**Limitation (≤3 sentences):** The authors acknowledge the current objective does not explicitly organize the latent space according to semantic relationships, and that zero-shot control performance depends on whether a suitable behavior was recorded in the offline trajectory pool.

---

## Gaussian Process Implicit Surfaces as Participating Media: Realization-Free Rendering from Level-Crossing Statistics
- **arXiv:** 2609.14695 · https://arxiv.org/abs/2609.14695
- **Submitted:** 2026-09-13
- **Authors:** Jack Cui, Kehan Xu, Eugene d'Eon, Wojciech Jarosz
- **Qualifying affiliation(s):** NVIDIA — Eugene d'Eon; FLAG: borderline relevance (theoretical rendering research rather than a game-engine product feature, but squarely cs.GR/volumetric-rendering topic)
- **Categories:** cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes a bidirectional conversion between Gaussian Process Implicit Surfaces (GPISes) and participating media (volumetric rendering primitives), enabling rendering of GPIS-modeled surfaces without sampling explicit geometric realizations.
**Purpose (≤3 sentences):** The authors address the cost of realization-based rendering of implicit stochastic surfaces, where many explicit surface samples must be generated and rendered to approximate the correct appearance.
**Breakthrough (≤3 sentences):** The authors apply Kac–Rice level-crossing theory with a local-conditioning approximation to derive anisotropic radiative-transfer parameters directly from pointwise GPIS statistics, reporting the resulting "realization-free" renderer achieves 23–34× lower equal-time estimator MSE than the realization-based baseline.
**Tools & method (≤3 sentences):** The method treats the implicit surface statistically as a participating medium and derives its radiative-transfer coefficients analytically from local GPIS statistics rather than Monte Carlo sampling of surface realizations.
**Limitation (≤3 sentences):** Not stated in the material reviewed; the approach relies on a local-conditioning approximation whose accuracy in more general scenes is not characterized in the summarized content.

# Near-misses
- 2609.20524 · S4R: Scaling for Rigid-Body Interpenetration Resolution · no qualifying industry affiliation found (authors' institutions not stated on the fetched page; academic/SIGGRAPH Asia paper)
- 2609.19750 · DELUGE: Decomposed Entropy-coded Live Unstructured Geometry Exchange for Real-time Particle Streaming · academic-only (Cluster Metaverse Lab, University of Tsukuba); uses Apple Vision Pro as evaluation hardware but no Apple-affiliated author
- 2609.12306 · Grid-Free Monte Carlo for Time-Dependent Diffusion · has NVIDIA co-authors (Rohan Sawhney, Eugene d'Eon) but topic is general PDE/thermal-diffusion solving, not on the tracked 3D/world-model/animation/engine topics
- 2609.20744 · Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation · no qualifying industry affiliation (authors from UC Berkeley, UT Austin, and startup "Impossible, Inc.")
- 2609.20816 · Paint-Anything: Unified Any-Color Control for Image Generation and Editing · off-topic (color-control image editing, not one of the four tracked topics); a "ByteDance" text match was a "Seed Technical Report" comment-tag artifact, not a confirmed author affiliation
- Several additional arXiv-search hits (2609.16042, 2609.20358, 2609.20056, 2609.14971) were confirmed false-positive company matches (boilerplate "Google Scholar" links or an unrelated citation to "(Microsoft, 2026)") and are off-topic besides.

Verification: each qualifying paper's abstract page and HTML full text were fetched directly to confirm v1 submission date, author affiliations (from the paper's own author/affiliation block), topic, and the reported facts above; double-checked before inclusion.
