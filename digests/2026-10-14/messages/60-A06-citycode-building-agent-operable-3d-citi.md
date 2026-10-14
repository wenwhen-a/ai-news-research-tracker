**[A06] CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations**
- **arXiv:** 2610.18342 · <https://arxiv.org/abs/2610.18342>
- **Submitted:** 2026-10-13
- **Authors:** Jiahui Sun, Ran Bi, Yifei Liu, Xiaolong Zhou, Yishuo Xu, Yuanqi Li, Congcong Zhu, Lei Yang, Yanwen Guo, Zhihang Zhong, Hongjie Zhang
- **Qualifying affiliation(s):** SenseTime — Lei Yang; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none (authors state a "code supplement" accompanies the paper and that runnable code is planned, but no URL is published)
- **Shipped counterpart:** none found

**Summary:** CityCode defines a new task of building large-scale, agent-operable 3D city models — metrically scaled, instance-level buildings plus explicit road geometry/connectivity — from a single low-altitude aerial RGB image per region with known camera parameters.
**Purpose:** The goal is a persistent, queryable and editable 3D city representation that downstream agents can inspect, modify and roll back, rather than a static mesh.
**Breakthrough:** The authors report that CityCode's representation recovers metric structure more accurately and produces higher visual fidelity than the evaluated baselines on CitySample-Aerial and UrbanScene3D, and that across 50 task chains of 50 steps each it supported querying, editing, planning, and historical state restoration.
**Tools & method:** Evaluation uses the CitySample-Aerial and UrbanScene3D datasets; the representation assigns persistent entity identities and supports validated, dependency-aware versioned updates.
**Limitation:** The paper has no dedicated limitations section; the closest statement, in the Reproducibility Statement, says end-to-end execution "additionally requires external checkpoints, datasets, API services, and integration components."
