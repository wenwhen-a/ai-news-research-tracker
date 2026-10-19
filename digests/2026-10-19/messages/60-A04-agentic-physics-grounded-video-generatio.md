**[A04] Agentic Physics-Grounded Video Generation via Memory-Augmented In-Context Reasoning**
- **arXiv:** 2610.23677 · <https://arxiv.org/abs/2610.23677>
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Xikang Guan et al.
- **Qualifying affiliation(s):** Horizon Robotics — Yanqi Bao, Zhengqing Chen (other authors are from Nanjing University, University of Hong Kong, Shenzhen University). FLAG: borderline — Horizon Robotics is a major Chinese autonomous-driving AI/chip company not on the explicit qualified list; kept per the "comparable-standing industry lab" allowance.
- **Categories:** cs.CV
- **Open release:** none (project page only, <https://xxkkxxx.github.io/PhysRepair-Website/>; no code/weights release stated)
- **Shipped counterpart:** none found

**Summary:** PhysRepair reframes physics-grounded video generation as "generate-diagnose-repair" rather than enforcing physics only before generation, using an agent to find and fix implausible dynamics after a video is produced via targeted local regeneration.
**Purpose:** It targets the failure mode where pre-generation physics guidance narrows motion diversity yet still misses physically invalid events — incorrect contact, forces, or material behavior — that only become visible after generation.
**Breakthrough:** On the Physics-IQ Verified benchmark (198 instances across solid mechanics, fluids, optics, thermodynamics, and magnetism), the authors report PhysRepair reaches a Physics-IQ score of 43.6 versus 42.7 for the strongest baseline (Cosmos3-Super-Image2Video) and 39.8 for its own unrepaired base generator, with spatiotemporal IoU rising from 22.8 to 34.7 after repair.
