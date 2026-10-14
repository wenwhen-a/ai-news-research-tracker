**[A10] Multics: Generative Multi-Player World Model with Hierarchical Communication**
- **arXiv:** 2610.17201 · <https://arxiv.org/abs/2610.17201>
- **Submitted:** 2026-10-12
- **Authors:** Kaiyi Huang, Wangbo Yu, Yukun Huang, Jiwen Yu, Kunhao Liu, Donglin Yang, Wenbo Hu, Ying Shan, Xihui Liu
- **Qualifying affiliation(s):** Tencent — Wangbo Yu, Yukun Huang, Kunhao Liu, Wenbo Hu, Ying Shan (ARC Lab, Tencent IEG); remaining authors at The University of Hong Kong
- **Categories:** cs.CV
- **Open release:** none found (project page only: karine-huang.github.io/Multics/)
- **Shipped counterpart:** none found

**Summary:** Multics generates video of a shared multiplayer environment from each player's own viewpoint, using a three-level (player/group/global) hierarchical communication scheme in self-attention instead of full pairwise or fully-centralized communication.
**Purpose:** Existing multiplayer world models either use fully-connected attention (quadratic cost as players grow) or a single global representation (interference between unrelated players' events).
**Breakthrough:** The authors report Multics beats both baselines (Solaris, γ-World) on GeoKPM, PSNR, LPIPS, rotation/translation error, FID and FVD at 4 and 6 players (e.g. GeoKPM 54.17% vs. 49.42% at 4 players), and that it trains at 4 players but generalizes to 10 players with GeoKPM 51.54%.
**Tools & method:** Built on Wan2.2 TI2V 5B, trained on the OpenCS2 dataset (ten-player Counter-Strike 2 match renders), with separate 4- and 6-player models and cross-domain evaluation on EgoTeam.
**Limitation:** The authors state that maintaining persistent world states across multiple players over long horizons "remains a challenging but important direction for future work." They also note Multics inherits the limitations of its pretrained video foundation model, including visual artifacts under large and dynamic human motion.
