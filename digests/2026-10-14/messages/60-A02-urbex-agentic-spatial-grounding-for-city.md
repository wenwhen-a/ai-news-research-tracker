**[A02] Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes**
- **arXiv:** 2610.18356 · <https://arxiv.org/abs/2610.18356>
- **Submitted:** 2026-10-13
- **Authors:** Yu Wang, Rui Dai, Wei Chen, Yi Wang, Bo Dang, Kaikui Liu, Xiangxiang Chu, Yansheng Li
- **Qualifying affiliation(s):** Alibaba (DreamX Team, Alibaba Group) — Kaikui Liu, Xiangxiang Chu (also confirmed via code repo under github.com/AMAP-ML)
- **Categories:** cs.CV, cs.AI
- **Open release:** code — <https://github.com/AMAP-ML/Urbex>
- **Shipped counterpart:** none found

**Summary:** Urbex reframes city-scale 3D visual grounding — locating a referred object in a large outdoor scene from language — as an active search problem rather than ranking precomputed candidate boxes.
**Purpose:** The authors target the slowness and scalability limits of candidate-ranking approaches to 3D grounding once scenes grow to city scale.
**Breakthrough:** The authors report the best Hit@1 and IoU on the CityRefer benchmark among compared methods, candidate-free grounding (no ground-truth box proposals needed), and substantially faster inference than the strongest ranking baseline; zero-shot tests on STPLS3D-Refer are reported to show improved cross-scene robustness.
**Tools & method:** The tool-use policy is trained with reinforcement learning on CityRefer using localization and exploration-shaping rewards, operating over a bird's-eye-view (BEV) rendering and view-to-world calibration pipeline.
**Limitation:** The authors state the method depends on reliable BEV rendering and view-to-world calibration, and that calibration or rendering errors can place a plausible 2D box at the wrong world location.
