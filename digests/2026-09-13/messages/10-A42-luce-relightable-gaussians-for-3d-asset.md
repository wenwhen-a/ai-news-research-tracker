**[A42] Luce: Relightable Gaussians for 3D Asset Generation**
- **arXiv:** 2608.23943 · https://arxiv.org/abs/2608.23943
- **Submitted:** 2026-08-25
- **Authors:** Mayank Singh, Michele Stoppa, Alvise Memo, Rui Yu, Harsha Kalli, Srimanth Gunturi, Muhammad Ahmed Riaz, Behrooz Shahsavari, Waleed Abdulla, David E. Jacobs
- **Qualifying affiliation(s):** Apple — all authors
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Luce introduces a PBR Gaussian representation that unifies geometry with albedo, metallic-roughness and tangent-space normals in voxelised Gaussian clouds, compresses it with a VAE into a diffusible latent, and generates assets from a single image with a rectified-flow transformer.
**Purpose:** Relightable, PBR-shaded 3D assets (Gaussians or textured meshes) from one image, so downstream renderers can relight them under arbitrary lighting.
**Breakthrough:** On Toys4K (N=412) the authors report FID 20.99 versus 29.22 for TRELLIS 2 and 29.76 for LiTo, and CLIP alignment 0.9062 versus 0.8898 for TRELLIS GS; on a PBR reconstruction subset (N=338) they report colour PSNR 36.1 dB and normal PSNR 34.6 dB.
**Tools & method:** Multi-layer DINOv2 conditioning; about 500K PBR-filtered assets from Objaverse and Objaverse-XL plus a 158K-asset TexVerse subset; 64 H100 GPUs for about 14 days each for the VAE and the flow model; inference on one H100.
**Limitation:** The authors state the voxelised representation may under-resolve fine detail, that the Cook-Torrance model omits subsurface scattering, anisotropy and thin-film effects, and that the pipeline targets object-centric assets rather than scenes.
