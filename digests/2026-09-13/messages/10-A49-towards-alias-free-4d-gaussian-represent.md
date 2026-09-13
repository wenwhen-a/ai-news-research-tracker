**[A49] Towards Alias-Free 4D Gaussian Representations with Motion-Aware Filtering**
- **arXiv:** 2608.21828 · https://arxiv.org/abs/2608.21828
- **Submitted:** 2026-08-22
- **Authors:** Ankit Dhiman, Kunal A Kathare, Pranav Vignesh, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan
- **Qualifying affiliation(s):** Samsung R&D Institute India, Bangalore — Ankit Dhiman, Lokesh R Boregowda; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Addresses aliasing in 4D Gaussian Splatting of dynamic scenes with a motion-aware 3D smoothing filter whose strength adapts to local motion instead of a static filter.
**Purpose:** Static anti-aliasing filters such as Mip-Splatting ignore motion, causing artefacts under zoom or resolution changes in dynamic scenes.
**Breakthrough:** The authors report 29.79 dB PSNR at 4x resolution on Plenoptic Video versus 27.40 dB for SARO-GS, and 32.36 dB versus 28.54 dB (Grid4D) on D-NeRF at 4x, a 5.21 dB gain over base SARO-GS.
**Tools & method:** Joint density of time and focal-length-to-depth ratio estimated by kernel density estimation drives the filter; evaluated on Plenoptic Video, D-NeRF and HyperNeRF; described as representation-agnostic across 4DGS frameworks.
**Limitation:** The authors state memory scales as O(N x D x T) (Gaussians x depth bins x time bins) and flag rapid complex-motion scenes for future optimisation.
