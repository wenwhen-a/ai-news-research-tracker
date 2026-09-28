**[B01] Motus (Tencent Games' end-to-end AI character-animation pipeline)**
- **Company:** Tencent
- **Status:** GA (internal studio tool — used in production, not an external developer product) · **Released:** 2026-08-27 · **New**
- **Surface:** Internal game-production tooling (animation pipeline used inside Tencent's own studios)
- **Primary source:** <https://www.prnewswire.com/news-releases/bringing-digital-characters-to-life-tencent-games-motus-makes-gamescom-debut-with-end-to-end-ai-animation-pipeline-302861442.html> (corroborated by <https://news.qq.com/rain/a/20260829A0BD2J00)>
- **Underlying research:** no traceable paper — Tencent Hunyuan's separately-published "HY-Motion 1.0: Scaling Flow Matching Models for Text-to-Motion Generation" (arXiv:2512.23464) covers a related text-to-motion model but is not cited by the Motus materials, so it is not recorded as an underlying paper
- **Availability:** Not offered as an external product, SDK or API; Tencent states the technology "has been applied across multiple titles" and is "currently integrated into over 90 projects," including Peace Elite (和平精英) and The Finals. No developer signup, pricing or licensing path for outside studios.

**What shipped:** Tencent Games' Central Tech group publicly unveiled Motus, an end-to-end generative-AI pipeline covering character rigging, skinning, text/video/keyframe-driven motion generation, automated animation-defect correction (jitter, mesh penetration, foot sliding), and real-time audio/text-driven facial and body animation for NPCs and digital humans.
**What research it translates:** Tencent describes Motus as built on "Tencent Games' proprietary family of generative animation foundation models" — in-house motion-generation and rigging research rather than a single named academic paper.
