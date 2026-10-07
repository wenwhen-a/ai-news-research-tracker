## GeoWM: Efficient Direct World Modeling in Explicit Geometry
- **arXiv:** 2610.07381 · https://arxiv.org/abs/2610.07381
- **Submitted:** 2026-10-05
- **Authors:** Mehrdad Noori, Guile Wu, Sam Hosseini, Dongfeng Bai
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab, Canada — all authors; FLAG: borderline (Huawei is on the SKILL.md "genuinely unsure" list, kept per instructions rather than dropped)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Modeling 3D scene geometry and its evolution over time is central to autonomous driving and robotics, but the common world-model paradigm of predicting future images or latent representations and then recovering geometry does not explicitly model geometric structure and relies on recursive rollouts that accumulate error and cost. The authors present GeoWM, a geometry world model that forecasts future scene geometry directly at a specified future horizon without recursive rollout. It leverages a geometry foundation model to turn observed RGB frames into a geometric history that conditions a flow-matching transformer.

**Purpose (≤3 sentences):** The paper aims to forecast 3D scene geometry (depth, camera pose, geometric structure) at arbitrary future horizons more accurately and efficiently than recursive, image/latent-based world models.

**Breakthrough (≤3 sentences):** The authors report that GeoWM outperforms the video- and feature-based world models they evaluated on forecasting depth, camera pose, and 3D scene geometry across four datasets spanning urban driving, aerial flight, and dynamic manipulation, while substantially reducing inference time at longer horizons; they also show a lightweight camera-motion predictor can accurately estimate the future viewpoint to condition this forecast.

**Tools & method (≤3 sentences):** A geometry foundation model converts observed RGB frames into a geometric history; a flow-matching transformer conditions on this history to predict scene geometry at a specified horizon; a lightweight camera-motion predictor estimates the future viewpoint, and the observed geometry is projected into that predicted viewpoint as a prior for the forecast.

**Limitation (≤3 sentences):** The authors do not state an explicit limitations section; in their conclusion they describe conditioning the forecast on robot actions, and jointly predicting motion and geometry (rather than geometry alone), as directions left to future work — implying the current model does not yet incorporate action-conditioning or joint motion/geometry prediction (observed, not stated as a limitation outright).

---

## Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs
- **arXiv:** 2610.07795 · https://arxiv.org/abs/2610.07795
- **Submitted:** 2026-10-06
- **Authors:** Qi Yang, Shuting Xia, Le Yang, Geert Van Der Auwera, Zhu Li
- **Qualifying affiliation(s):** Qualcomm — Geert Van Der Auwera
- **Categories:** cs.CV
- **Open release:** code — https://github.com/Qi-Yangsjtu/GSCV
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents GSCV, a Gaussian Splatting (GS) sequence compression method built on standard video codecs. Prior video-based GS sequence compression relies on Parallel Linear Assignment Sorting (PLAS) plus tracked primitive information to turn GS sequences into smooth 2D videos, but tracked information is unavailable for most practical applications, and vanilla PLAS without it produces images with weak inter-frame correlation due to its stochastic nature.

**Purpose (≤3 sentences):** The goal is to compress GS sequences effectively using off-the-shelf video codecs even when tracked primitive correspondence across frames is not available, which the authors identify as a gap in existing anchors such as GSCodec Studio.

**Breakthrough (≤3 sentences):** The authors report that GSCV shows "obviously improved performance" over MPEG video- and point-cloud-based anchors in GS sequence compression, and that it achieves better performance than video- and point-cloud-based anchors used in the current MPEG standardization study on both tracked and semi-tracked sequences.

**Tools & method (≤3 sentences):** GSCV introduces "Inter-PLAS," a method that produces visually close images between I-frames and P-frames of a GS sequence to strengthen inter-frame correlation for the video codec. It builds a pipeline on state-of-the-art video codecs operating on high-bit-depth GS images, aiming for higher compressibility and a higher achievable quality ceiling; code is released on GitHub.

**Limitation (≤3 sentences):** The authors state that PLAS-derived images differ substantially from natural images, which restricts the compression ratios achievable with generic video codecs. They also note that dividing GS data into multiple separately compressed video sequences fails to fully exploit intra-channel correlations among primitives, particularly for color spherical-harmonics (SH) data.

---

## World Models' Last Exam in Physics
- **arXiv:** 2610.08791 · https://arxiv.org/abs/2610.08791
- **Submitted:** 2026-10-06
- **Authors:** Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin, Zheng Jiang, Wenyi Li, Calvin Xiao, Youjie Zheng, Kaisen Yang, Qinhuai Na
- **Qualifying affiliation(s):** FLAG: borderline — the HTML author-notes block lists a combined affiliation "Navers Lab, Einsia.AI Peking University Tsinghua University" without per-author numbering; Peking University and Tsinghua University are academic, and "Navers Lab" / "Einsia.AI" could not be independently verified as established industry labs (web search was unavailable for this check). Kept per SKILL.md's "genuinely unsure → flag rather than drop" rule.
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Video world models can produce visually convincing but physically inconsistent sequences, which is a concern for their use in prediction and planning for embodied AI. The authors introduce "World Models' Last Exam in Physics," a measurement-based benchmark of 40 controlled tasks spanning mechanics, optics, fluids, thermal/phase-change phenomena, electromagnetism, and surface tension, each pairing an initial image and generation prompt with predefined physical criteria.

**Purpose (≤3 sentences):** The goal is to evaluate physical consistency in video world models using direct, interpretable physical measurements rather than model-based judgments or reference-video comparisons, and to cover physical domains beyond mechanics.

**Breakthrough (≤3 sentences):** Across eight video generation models and 1,280 generated videos, the authors report persistent physical inconsistencies and substantial variation across tasks, with the best-performing model achieving an overall score of 57.76 out of 100; they also report that their evaluator achieves higher agreement with human judgments than a direct vision-language-model baseline, in both within-task rankings and pairwise comparisons.

**Tools & method (≤3 sentences):** The benchmark's evaluator combines task-observability screening with task-specific quantitative physical measurements, validated in part on synthetic videos with known physical relationships. Task-specific first frames and prompts were constructed iteratively, using GPT-Image-2.5 to generate candidate first frames that make the relevant physical quantities observable.

**Limitation (≤3 sentences):** The authors state that current evaluation "remains constrained by the visibility and reliable extraction of task-relevant evidence," and that ambiguous initial geometry, occlusion, or an incomplete observation interval can make a physical test inconclusive and confound model errors with limitations of the input setup. They identify extending task coverage and improving measurement robustness in more complex scenes as future work.

---

# Near-misses
- 2610.07891 · Beyond Retargeting: Low-Latency and Robust Humanoid Whole-Body Teleoperation with Learned Atomic Motion Primitives · Tencent Robotics X affiliation confirmed, but off-topic despite company affiliation match (purely robot teleoperation on a Unitree G1, cs.RO only; no character-animation/game/3D/world-model content).
- 2610.07883 · Revar3r: gauge-aware perturbation uncertainty for feed-forward 3d reconstruction · the "ByteDance" company_match was a false positive; actual affiliations are BRAC University and Mahidol University only — no qualifying industry affiliation (on-topic 3D reconstruction, but academic-only).
- 2610.07355 · Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object · the "NVIDIA" company_match was a false positive; actual affiliation is Technical University of Munich (TUM) only — no qualifying industry affiliation (academic-only, despite on-topic world-models subject).

**Verification note:** All leads were checked against both the arXiv abstract page (title, authors, v1 submission date, categories, withdrawal status) and the arXiv HTML full-text page (author/affiliation block near the top). Submission dates fall inside the 2026-09-07 to 2026-10-07 window; none were withdrawn. Six papers from this batch's original 15 leads were dropped entirely from this file (not near-missed) because a concurrent run already verified and reported them on 2026-10-06 (SteadySplats, MC-Sparse, Real-time Rendering of Pre-integrated Neural Emitters) or already screened/decided them as near-misses that day (InterMimicGen, VGGT-Bridge, MaRO-GS, Level-of-Token Diffusion, HLA-WM, Kandinsky 6.0 Video) — this session's local clone of `state/papers_seen.json` was stale at screening time; it was refreshed via `git merge origin/main` before this file was finalized, and only genuinely new ids (not in the refreshed `papers_seen.json`) are listed above.
