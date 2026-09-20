**[A03] Gaussian Process Implicit Surfaces as Participating Media: Realization-Free Rendering from Level-Crossing Statistics**
- **arXiv:** 2609.14695 · <https://arxiv.org/abs/2609.14695>
- **Submitted:** 2026-09-13
- **Authors:** Jack Cui, Kehan Xu, Eugene d'Eon, Wojciech Jarosz
- **Qualifying affiliation(s):** NVIDIA — Eugene d'Eon; FLAG: borderline relevance (theoretical rendering research rather than a game-engine product feature, but squarely cs.GR/volumetric-rendering topic)
- **Categories:** cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper proposes a bidirectional conversion between Gaussian Process Implicit Surfaces (GPISes) and participating media (volumetric rendering primitives), enabling rendering of GPIS-modeled surfaces without sampling explicit geometric realizations.
**Purpose:** The authors address the cost of realization-based rendering of implicit stochastic surfaces, where many explicit surface samples must be generated and rendered to approximate the correct appearance.
**Breakthrough:** The authors apply Kac–Rice level-crossing theory with a local-conditioning approximation to derive anisotropic radiative-transfer parameters directly from pointwise GPIS statistics, reporting the resulting "realization-free" renderer achieves 23–34× lower equal-time estimator MSE than the realization-based baseline.
**Tools & method:** The method treats the implicit surface statistically as a participating medium and derives its radiative-transfer coefficients analytically from local GPIS statistics rather than Monte Carlo sampling of surface realizations.
**Limitation:** Not stated in the material reviewed; the approach relies on a local-conditioning approximation whose accuracy in more general scenes is not characterized in the summarized content.
