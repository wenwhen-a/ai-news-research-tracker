**[A01] Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark**
- **arXiv:** 2610.13947 · <https://arxiv.org/abs/2610.13947>
- **Submitted:** 2026-10-09 (v1)
- **Authors:** Xudong Cai, Ruijie Zhu, Haoliang Shang, Ruining Li, Marc Pollefeys, Shangzhe Wu, Andrea Vedaldi, Chuanxia Zheng
- **Qualifying affiliation(s):** Microsoft — Marc Pollefeys (listed jointly with ETH Zurich)
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://physicalvision.github.io/artisan>; no code/weights release stated; an offline human-evaluation demo is mentioned but no URL is given)
- **Shipped counterpart:** none found

**Summary:** The paper introduces Artisan, a multi-agent pipeline for generating articulated 3D assets, together with a new benchmark for evaluating spatial fidelity, physical plausibility, and downstream task performance.
**Purpose:** The authors aim to shift the goal of articulated 3D asset generation from reproducing how objects look to capturing how they move and function — targeting collision-free motion, stability under gravity, and accurate mass/material properties.
**Breakthrough:** The authors report that, across more than 10 evaluated models, Artisan achieves competitive spatial fidelity while obtaining the lowest collision rates and highest stability rates among the methods tested.
**Tools & method:** The pipeline uses MuJoCo for physics/stability feedback, Blender for rendering, and CoACD for convex decomposition, plus GPT-Image-2, Hunyuan3D 3.1, π0.5, and LLM coding/agent systems (Codex, Claude, Antigravity/Gemini, GPT variants) as components; evaluation also draws on RoboTwin 2.0 and RoboCasa365 for downstream robot-task performance.
**Limitation:** The authors acknowledge residual physical failures remain: even the best Artisan variant shows a 13.0% collision rate on multi-joint motion and only 96% stability in the articulated state.
