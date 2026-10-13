**[A01] NOFACE3D: NOise-scheduled Focused Anchoring and Controlled Enhancement for 3D Generation**
- **arXiv:** 2610.13050 · <https://arxiv.org/abs/2610.13050>
- **Submitted:** 2026-10-09
- **Authors:** James Rose, Jingwen Liang, Wenchao Ma, Oren Jacob, Haomiao Jiang
- **Qualifying affiliation(s):** Roblox (listed affiliation in author header, alongside The Pennsylvania State University; exact per-author mapping is unclear in the rendered HTML, but Roblox appears as a real author affiliation, not a citation)
- **Categories:** cs.CV
- **Open release:** none stated; project page only — <https://idkcouscous.github.io/NoFACE3D/>
- **Shipped counterpart:** none found

**Summary:** Image-to-3D generators produce convincing overall shapes but render thin, small, or detail-rich regions soft and under-resolved because fixed-resolution voxel grids sample all surfaces at the same density.
**Purpose:** To recover fine geometric and textural detail in generated 3D meshes without retraining the base generator, targeting regions a fixed-resolution grid under-samples.
**Breakthrough:** The authors report improved detail fidelity over the TRELLIS.2 baseline on PAniC-3D (FID 33.02 vs. 43.17, DINO 0.812 vs. 0.792) and TexVerse (DINO 0.741 vs. 0.728, FID 64.92 vs. 66.56), plus a GPT-5.6 judged win-share advantage on both.
**Tools & method:** Built on TRELLIS.2's sparse voxel representation; evaluated on PAniC-3D (329 artist-paired anime character assets, with a larger 4,892-asset version in the appendix), TexVerse (151 PBR-textured objects), and a new 339-asset benchmark, BigDetail, introduced by the authors.
**Limitation:** Because it is training-free and built on a frozen generator, the method inherits TRELLIS.2's limits and cannot produce content the base model otherwise can't generate.
