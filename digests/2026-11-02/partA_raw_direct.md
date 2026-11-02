## Hierarchical World Models with Implicit Dynamics
- **arXiv:** 2610.42146 · https://arxiv.org/abs/2610.42146
- **Submitted:** 2026-10-30
- **Authors:** Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, Lerrel Pinto, Yann LeCun
- **Qualifying affiliation(s):** Meta-FAIR — Nicolas Ballas, Mido Assran (affiliation marker "2" = Meta-FAIR in the author block)
- **Categories:** cs.RO (primary), cs.AI
- **Open release:** demo (project page with videos, https://id-wm.github.io; no code/weights release found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces ID-WM (Implicit Dynamics World Models), a hierarchical world model for embodied planning that separates state-space reachability from local control. A high-level model samples feasible transitions across the state manifold; a low-level world model acts as an inverse-dynamics solver that grounds those transitions into precise actions.

**Purpose (≤3 sentences):** The authors target long-horizon planning with world models, where existing hierarchical methods use rigid macro-actions or latent skills that produce brittle representations and limited fine-grained control. ID-WM aims to let a planner identify reachable subgoals without being constrained by low-level execution details.

**Breakthrough (≤3 sentences):** The authors report a 38.5% improvement over state-of-the-art policy and diffusion-based planners across three navigation and manipulation suites. They also report a 135% performance gain over single-level world-model MPC, which they attribute to the hierarchy mitigating compounding errors, particularly on long-horizon tasks in unseen configurations.

**Tools & method (≤3 sentences):** The method combines a high-level transition sampler operating in a diffusion latent space with a low-level inverse-dynamics world model; inference-time wall-clock cost was measured on a single NVIDIA L40S GPU against baselines including GCBC, HIQL, Diffuser, and H-Diffuser. Evaluation uses custom navigation and manipulation environments described in the paper's appendix (Environments and Dataset Generation).

**Limitation (≤3 sentences):** The authors state that ID-WM's reliance on search-based optimization within a diffusion latent space incurs higher inference time than reactive policies or deterministic world models, and note future work on amortized or gradient-based planning to address this.

---

## Coarse3D: Controllable and Faithful Sparse Structure Generation for Image-to-3D
- **arXiv:** 2610.41231 · https://arxiv.org/abs/2610.41231
- **Submitted:** 2026-10-30
- **Authors:** Gaige Wang, Bowen Pan, Hao Ren, Jiangjing Lyu, Chengfei Lyu
- **Qualifying affiliation(s):** Alibaba Group (all listed authors)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found (no code/weights/project-page link located on the paper)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Coarse3D is a coarse-stage, sparse-structure generation model for image-to-3D pipelines that produces orientation-controllable, structurally faithful voxel geometry from arbitrary unposed images. It is designed to directly replace the coarse stage of existing coarse-to-fine 3D generation pipelines without retraining the refinement stage.

**Purpose (≤3 sentences):** The authors target two limitations of current coarse-to-fine 3D generators: orientation is hard to control because semantic canonicalization is ambiguous, and generated structures often don't match the input image because of weak 2D-3D grounding.

**Breakthrough (≤3 sentences):** The authors report that Coarse3D raises the F-Score from 0.54 (baseline, as stated in the paper's conclusion) and achieves state-of-the-art performance on sparse-structure quality, which they attribute to three design choices: a first-view-anchored canonical space, a dual-tower diffusion transformer trained jointly with feed-forward reconstruction, and cross-attention regularized by pixel-to-voxel correspondence.

**Tools & method (≤3 sentences):** The model is trained on roughly 2M 3D assets: about 500K filtered assets from TRELLIS-500K (Xiang et al., 2025) plus additional data, with training using a learning rate of 1e-5 and batch size 256 on 64 NVIDIA H20 GPUs (full details in the paper's Appendix A.2).

**Limitation (≤3 sentences):** The paper's conclusion restates the two problems it addresses (orientation control, structural consistency) as the limitations of prior pipelines; the authors do not state an explicit limitation of their own method in the sections checked.

---

## Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation
- **arXiv:** 2610.42031 · https://arxiv.org/abs/2610.42031
- **Submitted:** 2026-10-30
- **Authors:** Jiahua Xu, Yijie Fang, Nannan Wang, Xunhao Lin, Li Cao, Lei Hao, Mingrui Zhu, Fei Gao, Xinbo Gao
- **Qualifying affiliation(s):** FLAG: borderline — Huawei (Technology Planning Dept of the Computing Technology Research Institute, Huawei, Shanghai; and Huawei Noah's Ark Institute, Shenzhen); lead affiliation is Xidian University (academic). Huawei is on the tracker's "borderline, keep + flag" list, not the core tracked-company list.
- **Categories:** cs.CV (primary)
- **Open release:** demo (project page, https://medcx.github.io/Any-Forcing — exact path truncated in source; no code/weights release found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Any Forcing is a framework for autoregressive (streaming) video generation that supports both flexible sampling-step counts and stable one-step generation, addressing the quality/speed tradeoff and the content drift/collapse that one-step methods suffer over long sequences.

**Purpose (≤3 sentences):** Existing autoregressive video generators fix the number of sampling steps, limiting the quality/speed tradeoff; one-step generation is fast but degrades visual quality and accumulates errors over long sequences.

**Breakthrough (≤3 sentences):** The authors report 20.9 FPS for short videos and 24.7 FPS for long videos on a single NVIDIA H100 GPU, evaluated on VBench (5-second videos) and VBench++ (30- and 60-second videos) at 480p, with five independent evaluation runs reported for robustness.

**Tools & method (≤3 sentences):** The framework combines a unified adversarial discriminator that jointly handles real-data-distribution alignment, cross-step consistency, and first-frame quality, with a training-free adaptive long-term memory selection mechanism that picks and temporally remaps past frames (three global "sink" frames, two long-term memory frames, one recent context frame) for stable long-video generation. Experiments were run on 16 NVIDIA A100 GPUs.

**Limitation (≤3 sentences):** No explicit author-stated limitation was located in the sections checked (abstract, intro, method); this is noted as a gap rather than inferred.

---

# Near-misses

- 2610.42135 · A Better Critic Matters for Distribution Matching Distillation · Adobe-affiliated (7 of 8 authors; 1 from MIT), confirmed qualifying company, but off-topic: this is a general diffusion-distillation training technique validated on ImageNet classification, SDXL/FLUX.2 text-to-image, and Wan2.1 text-to-video — not 3D, world models, character animation, or game engines.
- 2610.41564 · Verify–Backtrack Loop: Structured Precondition Recovery for Long-Horizon Language Agents · no author affiliation listed on the abs page (authors include Huawei-associated names per prior context, unconfirmed here); off-topic — general LLM-agent planning/recovery evaluated on AppWorld/ALFWorld/ScienceWorld, not on any of the four tracked topics.
- 2610.40927 · Agentic World Modeling for Agent Test-time Scaling without Environment Replica · affiliation unverifiable (no renderable HTML version; the "Google" screening hit traces to a "Google Scholar" link on the abstract-only page, not an author affiliation — author names (Huseyin A. Inan, Chetan Bansal, Saravan Rajmohan) match known Microsoft Research staff, but this is not independently confirmed from a primary affiliation block); also off-topic — "world modeling" here means an LLM-agent simulator for enterprise tool-use benchmarks (τ-bench, AppWorld, OfficeBench), not a visual/game/robotics world model.

Verification: each of the three included papers was checked against its arXiv HTML page (or abs page where no HTML render exists) for v1 submission date, author affiliation block, and topic; one qualifying industry co-author confirmed for each (Meta-FAIR, Alibaba Group; Huawei flagged as borderline-company). Near-misses were excluded for being off-topic and/or lacking a confirmable qualifying affiliation, not for being unverified in general.
