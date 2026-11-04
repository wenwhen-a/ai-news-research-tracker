**[A01] Möbius: A Unified Motion-Language Model Bridging Understanding and Generation**
- **arXiv:** 2611.05279 · <https://arxiv.org/abs/2611.05279>
- **Submitted:** 2026-11-03
- **Authors:** Jiazhi Shu et al.
- **Qualifying affiliation(s):** Tencent Games Motus — Jinyi Wang (project lead), Ronghui Li, Yu Lu, Xinwei Jiang, Zijiao Zeng (corresponding author), and co-affiliation for Jiazhi Shu and Yubo Zhao (other co-authors are HKUST and MIT)
- **Categories:** cs.CV
- **Open release:** code (GitHub repo linked from the project page, <https://github.com/JiazhiShu/mobius-code>, but as of verification contains only a README stating "Code availability is currently under internal review" — no code files published yet); no weights or live demo found
- **Shipped counterpart:** none found

**Summary:** Möbius is a unified motion-language model that understands, generates, and edits human motion within a single framework, rather than pairing a separate language model (for understanding) with a separate diffusion module (for generation).
**Purpose:** The authors state existing motion models are only partially unified because understanding (via a language model) and generation (via a separate diffusion module) remain architecturally split.
**Breakthrough:** The authors report Möbius-0.6B achieves R@1 0.8209 and FID 6.1291 on HumanML3D text-to-motion, versus FID 12.2110 for the strongest same-data baseline (MotionStreamer) and FID 13.5194 for HY-Motion-1B.
**Tools & method:** Clean motion, noisy motion, and text tokens interact through shared attention with role-specific parameters inside one multimodal transformer, so diffusion-based generation and language-model-style understanding share the same representation space.
