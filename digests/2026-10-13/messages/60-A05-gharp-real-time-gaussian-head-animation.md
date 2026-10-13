**[A05] GHARP: Real-time Gaussian Head Animation from Large-scale Reconstruction Prior**
- **arXiv:** 2610.10945 · <https://arxiv.org/abs/2610.10945>
- **Submitted:** 2026-10-07
- **Authors:** Ali Benlalah, Sepehr Johari, Patricia Vitoria, Armin Kappeler, Artem Sevastopolsky, Alexander Jung, Gabriele Fanelli, Kevin Mader, Manuel Breitenstein, Claudia Plüss, Jan Rüegg, Simon Biland, Thomas Etterlin, Dmitry Kostiaev, Mathias Deschler, Brian Amberg, Sebastian Martin
- **Qualifying affiliation(s):** Apple — all 17 authors
- **Categories:** cs.CV (primary), cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** GHARP animates 3D human heads in real time from a few input images plus a driving expression signal, splitting the task into an offline per-subject identity stage (building geometry/appearance) and a lightweight runtime animation stage suited to mobile devices.
**Purpose:** To achieve real-time, high-fidelity, mobile-capable 3D Gaussian head animation that is both faster and higher-quality than prior reconstruction-prior-based methods.
**Breakthrough:** The authors report state-of-the-art quality on Ava-256 with 13x faster runtime and 8x fewer Gaussians than compared methods; their body-alignment variant (Ours+BAN) reduces body temporal instability to σ_body^t 0.7 versus 18.8 (Avat3r) and 22.9 (FastGHA).
**Tools & method:** Built on the "HeadsUp" large-scale reconstruction prior trained on studio data (10k subjects, with a 1k-subject ablation); evaluated on Ava-256 and an in-the-wild iPhone 15 video with ARKit-extracted expression codes.
**Limitation:** The HeadsUp prior was trained on studio data with specific camera configurations/focal lenses, and the authors say adapting it to more diverse capture settings is future work.
