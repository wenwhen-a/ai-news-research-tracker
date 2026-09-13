**[A28] ECHO: Dyadic 3D Facial Motion Generation with Asymmetric Deterministic Articulation and Stochastic Reaction**
- **arXiv:** 2609.05506 · https://arxiv.org/abs/2609.05506
- **Submitted:** 2026-08-29
- **Authors:** Zhuoqiang Cai, Yujie Sun, Chaoyue Niu, Hongyun Yu, Zhiwen Chen, Chengfei Lv, Fan Wu
- **Qualifying affiliation(s):** Alibaba Group — Hongyun Yu, Zhiwen Chen, Chengfei Lv
- **Categories:** cs.GR, cs.CV, cs.SD
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** ECHO generates 3D facial motion for both roles in a two-person conversation from audio alone, treating the speaker's mouth motion as deterministic and the listener's reaction as stochastic, decomposing motion into a stable anchor trajectory plus a stochastic residual with "Motion Memory" regularisation.
**Purpose:** Audio-only conversational digital humans that need plausible facial behaviour for both talking and listening.
**Breakthrough:** Versus ProbTalk3D the authors report Fréchet distance improving from 7.51 to 2.80 and paired Fréchet distance from 1.61 to 0.59; a user study scored ECHO above UniTalker for lip-sync (3.71 vs 3.03), interaction realism (3.77 vs 2.59) and naturalness (3.82 vs 2.34).
**Tools & method:** About 120 hours of speaker-disjoint dyadic video derived from Seamless-Interaction (30 FPS, 54-dim FLAME coefficients); base training about 10 hours on one NVIDIA RTX 4090.
**Limitation:** No explicit limitations section was found in the extracted text (observed, not stated).
