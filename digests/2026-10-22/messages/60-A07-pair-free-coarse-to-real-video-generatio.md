**[A07] Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision**
- **arXiv:** 2610.28954 · <https://arxiv.org/abs/2610.28954>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Gonzalo Gómez-Nogales et al.
- **Qualifying affiliation(s):** Roblox and Adobe — both listed among the author team's affiliations (Universidad Rey Juan Carlos, New York University, Roblox, Adobe); the arXiv HTML markup lists these four institutions together in one note without marking which exact author maps to which, though a footnote confirms at least one author did "work done while at Roblox"
- **Categories:** cs.CV
- **Open release:** model and project page stated as "will be released" at <https://gonzalognogales.github.io/coarse2real-sharp/> (not yet released as of this version)
- **Shipped counterpart:** none found

**Summary:** The paper addresses coarse-to-real (C2R) video generation — converting coarse animation, simulation, or game-rendered video into photorealistic video while preserving scene layout, camera motion, and dynamics — without needing expensive aligned (coarse, realistic) video pairs.
**Purpose:** The authors state that prior C2R systems require aligned (coarse, realistic) video pairs, which are expensive to create and confine such systems to narrow synthetic domains; their pair-free approach is meant to let training scale with ordinary real-video corpora instead.
**Breakthrough:** The authors state their pair-free training "scales with any real-video corpora rather than with paired synthetic videos," and that at inference the DINO-R2C model is discarded so actual coarse (e.g., game-rendered) videos drive the C2R# model directly; no quantitative benchmark numbers were available in the excerpted abstract/intro text reviewed.
