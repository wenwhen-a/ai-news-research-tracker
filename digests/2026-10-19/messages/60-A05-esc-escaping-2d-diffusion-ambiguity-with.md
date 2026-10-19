**[A05] ESC: Escaping 2D Diffusion Ambiguity with Geometric Constraints for Consistent Novel View Synthesis**
- **arXiv:** 2610.23732 · <https://arxiv.org/abs/2610.23732>
- **Submitted:** 2026-10-14 (v1)
- **Authors:** Ge Ya Luo, Daniel Severo, Brian Karrer, Christopher Pal, Adriana Romero-Soriano, Michal Drozdzal
- **Qualifying affiliation(s):** Meta (FAIR) — Daniel Severo, Brian Karrer, Michal Drozdzal, Adriana Romero-Soriano (joint last author); Ge Ya Luo's work was done at Meta. Pal is Mila/Polytechnique Montréal.
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** ESC targets single-image novel view synthesis under large camera changes, where 2D diffusion models can produce plausible but geometrically invalid views that standard 2D or pose metrics fail to catch.
**Purpose:** It aims to improve the 3D consistency of generated novel views by resolving the depth/geometry ambiguity inherent in purely 2D diffusion-based view synthesis.
**Breakthrough:** The authors report that jointly generating RGB and depth, combined with their Projection Consistency Constraint (PCC) used for best-of-N selection (ESC-PCC-BoN), improves consistency over their own base model on DL3DV, RealEstate10K, and Tanks & Temples (e.g., DL3DV LPIPS 0.4340 vs 0.4448, PCC 0.2257 vs 0.2448).
**Tools & method:** Built on a Qwen MM-DiT backbone with LoRA adaptation and a Ray ControlNet for pose conditioning, ESC concatenates depth tokens with image tokens to jointly predict target RGB and depth from a source image, its depth map, and Plücker ray maps for source and target cameras, trained on a DL3DV/RealEstate10K mixture.
**Limitation:** The authors note off-the-shelf DA3 depth is noisy even in consistent scenes, and that best-of-N selection scales compute roughly linearly with N without being compute-matched against single-sample baselines.
