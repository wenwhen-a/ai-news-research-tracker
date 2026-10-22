**[A01] Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation**
- **arXiv:** 2610.29989 · <https://arxiv.org/abs/2610.29989>
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu, Ying Shan, Limin Wang
- **Qualifying affiliation(s):** Tencent — Yukun Huang, Wenbo Hu, Ying Shan (ARC Lab, Tencent IEG)
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper argues that autoregressive video diffusion models trained with teacher forcing can produce plausible continuations without actually learning how scenes evolve, because strong local visual continuity gives a shortcut for denoising the current chunk.
**Purpose:** The authors frame this work explicitly as "a pathway toward generative world modeling," aiming to force autoregressive video generators to model visual evolution rather than only local continuity.
**Breakthrough:** The authors report FCP achieves superior physical plausibility compared with standard teacher-forced autoregressive training, at a lower overall training compute budget.
**Tools & method:** FCP draws its supervision directly from training videos (needing no extra pretrained visual encoder) and conditions offset-specific predictors only on the single source chunk rather than the full visible history, which the authors say costs 40–50% less training compute than a full-context variant at matched quality.
**Limitation:** The paper's "Limitations and Discussions" appendix is framed mainly as a comparison with concurrent work (Next Forcing), noting their FCP prototype targets autoregressive video generation broadly (as a path to world modeling) rather than robotic world-action modeling specifically; no separate acknowledged weakness beyond this scope distinction is stated in the available text.
