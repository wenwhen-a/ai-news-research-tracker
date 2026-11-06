**[A02] Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation**
- **arXiv:** 2611.07294 · <https://arxiv.org/abs/2611.07294>
- **Submitted:** 2026-11-05
- **Authors:** Tao Jun Lin, Jinhong Ni, Ruyi Zha, Yifu Wang, Xibin Song, Pan Ji, Hongdong Li
- **Qualifying affiliation(s):** Amazon — Hongdong Li (Amazon Scholar, part-time; his full-time appointment is at the Australian National University); other authors are at ANU and Vertex Lab Technology Limited. **FLAG: borderline** — the Amazon affiliation is a part-time "Amazon Scholar" appointment, not the author's primary institution.
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** The paper proposes Householder Motion Embedding (HME), a training-free way to encode motion control into the initial noise of a video diffusion model using a sequence of Householder reflections that form an orthogonal transform on each spatial location's channel vector.
**Purpose:** The paper addresses a stated tension in motion-controllable video generation: existing noise-warping methods inject motion by spatially warping noise, which breaks the i.i.d.
**Breakthrough:** The authors report 2.80ms per latent at reflection count K=2, a 2.7x speedup over GWTF (7.63ms) and 13.6x over HIWYN (38.00ms), with roughly 0.5–6MB of extra peak memory versus 76MB (GWTF) and 49,384MB (HIWYN).
**Tools & method:** Built on CogVideoX-5B-I2V and trained on ~100K videos from RealCam-Vid (sourced from RealEstate10K, MiraData, DL3DV-10K); evaluated on DAVIS (45 videos), MC-Bench (965 samples) and 200 DL3DV scenes.
**Limitation:** The authors state the method "relies on accurate optical flow for training, so noisy motion estimates can weaken motion adherence," and that subjects with complex non-rigid geometric motion "remain challenging," left for future work.
