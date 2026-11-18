**[A01] Towards Data-Efficient, Real-Time World Models**
- **arXiv:** 2611.22497 · <https://arxiv.org/abs/2611.22497>
- **Submitted:** 2026-11-17
- **Authors:** Raluca Stevenson, David Bignell, Jennifer C. White, Tabish Rashid, Emanuele Aiello, Mariya Hendriksen, Junha Hyung, Sadegh Aliakbarian, Abdelhak Lemkhenter, Marko Tot, Katja Hofmann, Sarah Parisot
- **Qualifying affiliation(s):** Microsoft — Sarah Parisot (listed affiliation "Microsoft, Cambridge, United Kingdom"); paper states "This work was carried out at Microsoft." Katja Hofmann is also a known Microsoft Research (Game Intelligence) lead, though per-author affiliation tags were garbled in the HTML.
- **Categories:** cs.AI
- **Open release:** none found (no code/weights/demo link in abstract or comments)
- **Shipped counterpart:** none found

**Summary:** The authors tackle two barriers to real-time, action-conditioned gameplay world models: slow autoregressive inference and the large data requirements of training.
**Purpose:** To make interactive gameplay-generation world models fast enough for real-time play and cheap enough to train that custom/creative use becomes practical, rather than requiring massive datasets and slow inference.
**Breakthrough:** The authors report a 79x inference speedup over the autoregressive baseline with only a modest quality trade-off.
**Tools & method:** Two-stage discrete diffusion replacing next-token prediction, with a lightweight refinement transformer doing iterative masked-token predictions on top of an existing autoregressive world-model backbone (Kanervisto et al., 2025).
**Limitation:** The authors themselves describe the speedup as coming with a "modest quality trade-off"; no separate limitations section or training-hardware details are given in the abstract/comments.
