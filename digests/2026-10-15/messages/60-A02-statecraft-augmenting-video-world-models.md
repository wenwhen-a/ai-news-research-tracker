**[A02] StateCraft: Augmenting Video World Models with Abstract-State Reasoning**
- **arXiv:** 2610.19795 · <https://arxiv.org/abs/2610.19795>
- **Submitted:** 2026-10-14
- **Authors:** Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool
- **Qualifying affiliation(s):** Microsoft — listed among the paper's affiliations (INSAIT/Sofia University, ETH Zurich, University of Ulm, TUM MCML, Microsoft); the HTML page does not print an explicit per-author marker mapping, but Microsoft appears in the affiliation block for this author list
- **Categories:** cs.CV (primary); cs.AI; cs.LG
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** StateCraft decouples a persistent, updatable "abstract state" from the visual state in a video world model, so that actions can change parts of the world that are not currently visible on screen.
**Purpose:** Standard video world models struggle to track changes to parts of a scene that fall outside the current camera view, since they condition only on visible history.
**Breakthrough:** The authors report revisit self-consistency staying near 0.9 SSIM over up to 512 actions versus about 0.5–0.6 for baselines, and a 10.29 dB PSNR gain from state conditioning on their CF++ backbone.
**Tools & method:** A vision-language model predicts state transitions from incoming actions and updates a graph of views and elements; a video diffusion model generates frames conditioned on this predicted state, the action, and visual history.
**Limitation:** The authors report that inserting new elements onto an empty background is markedly weaker (48% success) than other controllability edits (up to 98%).
