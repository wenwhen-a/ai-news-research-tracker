**[A11] Providing Rapid Design Feedback for 3D Obstacle Course Games Using Constrained Solvability Queries**
- **arXiv:** 2609.36225 · <https://arxiv.org/abs/2609.36225>
- **Submitted:** 2026-09-28
- **Authors:** Zander Majercik et al.
- **Qualifying affiliation(s):** Roblox — Zander Majercik, Sharon Zhang, Maneesh Agrawala, Kayvon Fatahalian (dual-affiliated with Stanford University); other authors solely at Stanford University
- **Categories:** cs.GR
- **Open release:** code — <https://zandermajercik.github.io/interactive-obstacle-course-feedback/> (paper states "we release code for our interactive tool, simulator, training setup, and procedural level generation system")
- **Shipped counterpart:** none found

**Summary:** The paper presents an interactive design tool that gives 3D obstacle-course game designers rapid feedback by answering "constrained solvability queries" (e.g., can a waypoint be reached while avoiding a region, within a jump/time budget) using a GPU-accelerated digital-twin simulator built on the Madrona engine.
**Purpose:** Manual playtesting or hiring external testers to evaluate obstacle-course navigability is slow and disruptive to creative iteration, so the authors aim to give designers near-instant, constraint-based feedback on how players can traverse and potentially break a level design.
**Breakthrough:** The authors report the custom GPU-accelerated simulator runs about 14,000× real-time gameplay (over 800K game steps/second across 8K parallel simulations), solving most queries within seconds, and that Policy Selection reduces average solve time by more than 15 seconds on long queries versus baseline Go-Explore variants.
