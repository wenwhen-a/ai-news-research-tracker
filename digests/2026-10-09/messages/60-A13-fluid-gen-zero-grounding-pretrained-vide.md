**[A13] Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training**
- **arXiv:** 2610.10984 · <https://arxiv.org/abs/2610.10984>
- **Submitted:** 2026-10-07 (v1)
- **Authors:** Hong Huang, Yuqiu Liu, Chenyu You, Daniel Martin, Chuhang Zou, Wuyang Chen
- **Qualifying affiliation(s):** Meta Reality Labs — listed among the paper's affiliations; the HTML extraction could not map the superscript to a specific named author (likely Daniel Martin or Chuhang Zou). Other authors: Simon Fraser University, Stony Brook University, Lawrence Berkeley National Laboratory (academic/national lab).
- **Categories:** cs.CV (primary); cs.GR (cross-listed)
- **Open release:** code and data stated as planned "upon acceptance" (not yet released)
- **Shipped counterpart:** none found

**Summary:** The paper presents a training-free framework for generating physically plausible video of fluid-object interactions. It separates physical reasoning, handled by a physics simulator, from appearance synthesis, handled by a pretrained video generator.
**Purpose:** To ground existing pretrained video generators in physics for fluid-object interaction scenes without any additional training of the generator.
**Breakthrough (≤3 sentences, attributed):** The authors report reducing object trajectory error by 26.7%-81.5% and fluid endpoint error by 67.9%-84.0% versus baselines, with human raters preferring their outputs in most comparisons.
**Tools & method:** A two-level agentic workflow — a vision-language-model agent plans the generation clips, and latent-space guidance injects simulation signals into denoising — is applied plug-and-play to existing video models (Tora, VACE, WanMove) and evaluated on a new benchmark.
**Limitation:** The authors state that code and data will be released only upon acceptance, so the method is not yet independently reproducible; no other limitations are stated in the abstract.
