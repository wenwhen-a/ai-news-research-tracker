**[A08] Decoupling Action from Egocentric Observation for World Simulation**
- **arXiv:** 2610.27946 · <https://arxiv.org/abs/2610.27946>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Yue Ma et al.
- **Qualifying affiliation(s):** JD Explore Academy (JD.com) — appears in the paper's combined institution line ("HKUST, Tsinghua University, Stanford University, MIT, JD Explore Academy") attached to the author group that includes Haoyang Huang and Nan Duan; the arXiv HTML source renders affiliations as one block rather than mapped per author, so the exact author-to-institution pairing within that group is not separable from the source. **FLAG: borderline** — JD.com is named explicitly in the tracker's own guidance as an example company to flag rather than silently drop.
- **Categories:** cs.CV
- **Open release:** code — GitHub repo linked (<https://github.com/mayuelala/EgoACT>); project page: <https://ego-act.github.io/>; the EgoActionBench benchmark is introduced alongside the method
- **Shipped counterpart:** none found

**Summary:** EgoACT is a test-time framework for "egocentric action transfer" — reproducing the semantic action from an egocentric reference video in a new visual context — that operates directly on the denoising process of a video diffusion model without extra geometric estimators.
**Purpose:** The paper targets a gap in two prior approaches to action transfer: condition-guided methods that convert video into explicit geometric controls (introducing geometric-estimation error) and motion-transfer methods that use motion patterns alone (causing hand-structure collapse and implausible contact).
**Breakthrough:** On EgoActionBench, the authors report EgoACT outperforms five baselines (InterDyn, Mask2IV, CosHand, DiTFlow, VACE) on every reported metric, including Motion Fidelity (0.2750 vs. 0.1910–0.2434 for baselines) and VBench Aesthetic Quality (0.5633 vs. 0.4226–0.5065) (Table 1).
