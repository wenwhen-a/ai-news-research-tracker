**[A09] Unravel: Recovering an Interactive 3D Scene from a Single Image**
- **arXiv:** 2610.16146 · <https://arxiv.org/abs/2610.16146>
- **Submitted:** 2026-10-12
- **Authors:** Hui Shan et al.
- **Qualifying affiliation(s):** Adobe — Zhen Chen; Tencent LIGHTSPEED — Keyang Luo, Weikai Chen, Runze Zhang, Xin WANG (affiliation listed as "LIGHTSPEED", Tencent's internal game-development studio) — FLAG: borderline for the LIGHTSPEED mapping since it is not one of the explicitly spelled "Tencent" entries, though Adobe alone is sufficient to qualify
- **Categories:** cs.CV (primary); cs.AI
- **Open release:** code (planned) — "Our code will be released at <https://github.com/SII-Hui/Unravel"> (not available at time of check)
- **Shipped counterpart:** none found

**Summary:** Unravel is a training-free framework that turns a single image into an interactive 3D scene in which every object is a separate, movable asset.
**Purpose:** Existing single-image-to-3D scene generators either produce one entangled, immovable geometry or predict all objects in a single feed-forward pass where wrong guesses can't be detected or repaired.
**Breakthrough:** On a 5-scene, 160-object evaluation, the authors report Unravel reaches a 3D asset VLM score of 8.2 and human score of 8.6 (vs. 4.7/4.9 for direct reconstruction), full 2D mask area coverage (1.000 vs. 0.772) and zero undetected-coverage-ratio error on both 2D masks and 3D scene geometry (vs. 11.3%/10.1% for direct reconstruction).
**Tools & method:** The pipeline is entirely training-free, relying on off-the-shelf hosted models including GPT-5.5, gpt-image-2, and GPT-6 Astra (called via its web interface), with point clouds as the main modality for spatial relationship recovery.
