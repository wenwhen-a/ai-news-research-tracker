**[A09] DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes**
- **arXiv:** 2609.39841 · <https://arxiv.org/abs/2609.39841>
- **Submitted:** 2026-09-30
- **Authors:** Merav Keidar, Tomer Borreda, Rajalakshmi Nandakumar, Or Litany
- **Qualifying affiliation(s):** NVIDIA — Or Litany
- **Categories:** cs.CV
- **Open release:** code — github.com/Dyrad-NVS/DyRad (includes a deterministic generator for the paper's synthetic dataset); project page at dyrad-nvs.github.io
- **Shipped counterpart:** none found

**Summary:** DyRAD addresses radar-based novel view synthesis for dynamic autonomous-driving scenes, where prior methods struggle to render Doppler signatures for moving objects, separate true scene geometry from sensor-induced measurement spreading, and evaluate synthesis at viewpoints away from the recorded trajectory.
**Purpose:** The goal is to let researchers evaluate autonomous-driving perception stacks at radar viewpoints that were never actually recorded, by synthesizing physically faithful range-azimuth-Doppler (RAD) tensors for dynamic scenes.
**Breakthrough:** The authors report off-path detection recovery of 91.7% of reference-detected objects versus 18.1% for the strongest baseline, and on-path full-RAD correlation improving from 0.068 to 0.272 with foreground hit rate rising from 26.9% to 90.7% (RADIal dataset).
**Tools & method:** The method couples zero-extent point reflectors (background + tracked dynamic objects) with a fixed, physics-grounded per-sensor PSF kernel, projecting reflector velocities onto the line-of-sight to render RAD tensors with Doppler used as both output and supervision signal.
**Limitation:** The authors state that reflector-to-object assignments rely on object annotations and remain fixed during optimization, and that the method uses a ground-plane implementation because elevation is absent from the measurements.
