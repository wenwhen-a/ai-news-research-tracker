**[A04] DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models**
- **arXiv:** 2610.35044 · <https://arxiv.org/abs/2610.35044>
- **Submitted:** 2026-10-26
- **Authors:** Jingbo Xu et al.
- **Qualifying affiliation(s):** Xiaomi EV — Hanchao Leng (project leader), JiaHui Huang, Hanbing Li, Jingwei Zhao, Kuiyuan Yang, Guang Chen, Hangjun Ye, and Jingbo Xu (dual-affiliated with Tsinghua University). FLAG: borderline (Xiaomi's EV/automaker division; not on the default illustrative company list, but matches the "automaker AI labs" borderline category named in the brief).
- **Categories:** cs.CV, cs.RO
- **Open release:** none found — no project page, code, or weights link located in the paper.
- **Shipped counterpart:** none found

**Summary:** DriveUniTok is a unified multimodal tokenizer for driving world-action models (WAMs) that encodes appearance, projected-LiDAR metric geometry, and ego motion into a single decodable continuous latent, rather than modeling them separately.
**Purpose:** The paper argues that existing driving world-model approaches model appearance, LiDAR-projected depth, and ego motion partially or independently, despite these being different projections of one underlying world state, causing information loss and cross-modal inconsistency that limits downstream planning performance.
**Breakthrough:** On the NAVSIM benchmark, the authors report that the unified tokenizer design achieves better future prediction and planning performance at lower downstream computational cost than separate-stream alternatives.
**Tools & method:** The method freezes the DriveUniTok tokenizer and adapts a pretrained diffusion model (DriveUniWAM) to predict future unified latents, which are decoded into future appearance, projected LiDAR depth, and ego trajectories; evaluation is on the NAVSIM benchmark, with an added reinforcement-learning post-training stage.
