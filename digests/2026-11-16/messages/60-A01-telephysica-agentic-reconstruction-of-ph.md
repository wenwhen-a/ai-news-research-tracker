**[A01] TelePhysica: Agentic Reconstruction of Physically Interactive Scenes**
- **arXiv:** 2611.18078 · <https://arxiv.org/abs/2611.18078>
- **Submitted:** 2026-11-13
- **Authors:** Ruiqi Shu et al.
- **Qualifying affiliation(s):** China Telecom — Institute of Artificial Intelligence (TeleAI), all authors (Shu and Zhan completed the work as TeleAI interns; Li is corresponding author); FLAG: borderline
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none (homepage <https://interactive4d.vercel.app/> shown, but no code/weights/demo release stated for this work)
- **Shipped counterpart:** none found

**Summary:** TelePhysica is a closed-loop, agentic pipeline that reconstructs a physically simulatable 3D scene from a single photo and uses the resulting physics rollouts to condition video diffusion models.
**Purpose:** The authors want a way to recover an executable, physically consistent scene from one uncalibrated image so that downstream video generation can be conditioned on genuine physical dynamics rather than implicit, uncontrollable motion priors, enabling mid-rollout intervention and counterfactual forces.
**Breakthrough:** The authors report that on a 100-scene benchmark, their closed-loop verification raises equilibrium-verified scene recovery from 0% (single-pass synthesis) to 81%.
**Tools & method:** A vision-language coding agent generates visual meshes and declarative physics models from a single photo, verified by silhouette comparison against the input image and a zero-force gravity equilibrium test; the verified scene runs in a unified solver covering rigid bodies, articulated chains, cloth, and 3D elastic tetrahedral (soft-body) models.
**Limitation:** The authors acknowledge that material parameters (mass density, Young's modulus, friction) are assigned from priors rather than identified online from visual feedback, leaving closed-loop physical parameter identification as future work.
