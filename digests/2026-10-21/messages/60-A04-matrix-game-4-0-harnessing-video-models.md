**[A04] Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds**
- **arXiv:** 2610.27999 · <https://arxiv.org/abs/2610.27999>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Jihai Zhang et al.
- **Qualifying affiliation(s):** SkyworkAI — listed affiliation for Jihai Zhang, Puyi Wang/Siru Chen/Tianle Li/Guanjie Chen/Junyi Wu, Chubin Chen/Yuanhang Li/Kaichen Huang/Haobo Zhang/Yangguang Li, and Wei Yu/Guibin Chen/Yu Cheng/Yahui Zhou (the latter is "Project Lead and Corresponding Author"). **FLAG: borderline** — SkyworkAI (the AI lab of publicly-listed Kunlun Tech) is not on the tracker's default company list, but is kept per the tracker's "clearly comparable top-tier lab" rule given it is the originating lab of the prior Matrix-Game releases.
- **Categories:** cs.CV (primary); cs.GR
- **Open release:** code (GitHub), model weights (Hugging Face), and low-poly game assets — the abstract states these are released; project page: <https://matrix-game-v4-0.github.io/page/>
- **Shipped counterpart:** none found (the paper describes a Steam technical preview as a near-term future goal, not yet shipped)

**Summary:** Matrix-Game 4.0 separates game execution from visual generation via an "executable game harness": a lightweight game engine holds persistent world state and interaction rules, a multimodal coding agent turns player ideas into game code and dynamic scene captions, and an autoregressive-video-model renderer turns engine-rendered low-poly proxies into detailed visuals conditioned on those captions.
**Purpose:** The paper argues controllable video generation alone is insufficient for genuinely "playable" worlds, which additionally need persistent state, executable rules, low interaction latency, and mechanics beyond navigation.
