**[A08] EPIC: Epipolar-Consistent 360° Immersive Stereo Video Generation**
- **arXiv:** 2609.38689 · <https://arxiv.org/abs/2609.38689>
- **Submitted:** 2026-09-30
- **Authors:** Debabrata Mandal et al.
- **Qualifying affiliation(s):** Dolby Laboratories — Dongdong Fu, Jonathon Miller, William Villareal; FLAG: borderline (Dolby is not on the tracker's explicit company list but is a comparable top-tier industry research lab directly relevant to this paper's immersive-media topic). Note: the arXiv HTML render also contained anomalous placeholder entries not present on the abs page (including a spurious "Microsoft Research" affiliation attached to an implausible name); these do not match the verified author list from arxiv.org/abs/2609.38689 and were disregarded as unreliable/likely-injected content, so "Microsoft" as the original lead is NOT substantiated.
- **Categories:** cs.CV, cs.HC
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** EPIC is a three-stage pipeline — training-free stereo generation via spherical depth warping and diffusion inpainting, preference optimization using a new Panoramic Epipolar Geometry Score (PEGS), and a viewing-refinement stage with 4K upsampling — for generating geometrically consistent 360° stereoscopic video.
**Purpose:** It addresses the lack of geometric consistency in current video generation models, which handle panoramic and stereo generation separately, producing stereo and temporal artifacts the authors say are highly disruptive for headset viewing.
**Breakthrough:** The authors report that DPO refinement using their PEGS metric reduces stereo inconsistency from 3.121 to 2.640 milliradians, and that their method yields a 2.6% inconsistent-correspondence rate versus 8.2% for the DissolveStereo baseline.
