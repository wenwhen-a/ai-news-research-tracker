**[A10] UniCaMo: Unified Camera and Motion Control for Video Diffusion Models**
- **arXiv:** 2611.00810 · <https://arxiv.org/abs/2611.00810>
- **Submitted:** 2026-10-31
- **Authors:** Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian, Binh-Son Hua, Hung Bui, Minh Hoai Nguyen, Phong Nguyen-Ha
- **Qualifying affiliation(s):** Qualcomm AI Research — Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian, Hung Bui, Minh Hoai Nguyen, Phong Nguyen-Ha. Note: Binh-Son Hua is primarily affiliated with Trinity College Dublin; his contribution is noted as "work done under consultancy capacity" for Qualcomm.
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** none found (reproducibility statement says code, model checkpoints, and datasets "will be publicly available upon acceptance"); project page with qualitative videos: <https://phongnhhn.info/Unicamo/>
- **Shipped counterpart:** none found

**Summary:** UniCaMo is a unified framework for jointly controlling camera motion and object motion in image-and-text-to-video diffusion models.
**Purpose:** The authors aim to provide unified, precise control over both camera and object motion in video diffusion generation, avoiding the need for dedicated control modules or architectural changes to the base model.
**Breakthrough:** The authors report state-of-the-art motion controllability and high visual quality with minimal inference overhead.
**Tools & method:** The method constructs motion-consistent input noise through a foreground noise propagation stage guided by 3D point tracks and camera poses, and a spherical noise sampling stage using a coarse 3D sphere proxy for background.
**Limitation:** The authors state the foreground noise propagation stage depends heavily on accurate 3D point tracks and camera poses, so tracking or calibration errors can degrade controllability.
