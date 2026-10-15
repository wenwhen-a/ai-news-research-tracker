**[A03] OneLA: Learning Many Worlds from Latent Actions**
- **arXiv:** 2610.20160 · <https://arxiv.org/abs/2610.20160>
- **Submitted:** 2026-10-14
- **Authors:** Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Chiyu Wang, Junfeng Ni, Mu Xu
- **Qualifying affiliation(s):** Alibaba Group — Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Chiyu Wang, Mu Xu (all AMAP, Alibaba Group); Junfeng Ni (AMAP, Alibaba Group, with internship work also credited to Tsinghua University)
- **Categories:** cs.CV
- **Open release:** none stated on the abstract/HTML page
- **Shipped counterpart:** none found

**Summary:** OneLA learns continuous latent actions from unlabeled videos spanning games, navigation, driving, and robotics, using a shared orthonormal motion dictionary and a single predictive objective rather than task-specific designs or cross-domain alignment losses.
**Purpose:** The authors motivate the work by noting that "learning shared latent actions across domains remains challenging," since prior latent-action methods tend to require domain-specific alignment tricks.
**Breakthrough:** The authors report a 24.8% reduction in action cycle-transfer rotation error (and 15.5% for translation) over the strongest baseline (OLaF), and a 20.5% improvement in Human Preference Score v3 (HPSv3) for real-scene generation in a joint-training comparison.
**Tools & method:** The method uses an orthonormal motion dictionary built via QR factorization, combined with KL and sparsity regularization and a reconstruction objective, to learn domain-general latent actions from video.
**Limitation:** No explicit limitations section was surfaced in the fetched content; the paper is an empirical benchmark/method paper and the reported gains are relative to specific baselines (e.g., OLaF) rather than absolute task success in deployed systems.
