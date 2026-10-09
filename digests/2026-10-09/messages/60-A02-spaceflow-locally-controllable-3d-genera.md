**[A02] SpaceFlow: Locally Controllable 3D Generation**
- **arXiv:** 2610.12399 · <https://arxiv.org/abs/2610.12399>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Neil De La Fuente et al.
- **Qualifying affiliation(s):** Microsoft — listed as one of the paper's three institutional affiliations (alongside ETH Zürich and Stanford University) in the HTML author block. **Flag: the specific author(s) at Microsoft could not be resolved because the author→affiliation superscript markers failed to render in the arXiv HTML (a LaTeX macro/rendering artifact, confirmed by inspecting the raw HTML); Microsoft is listed identically to the two confirmed academic affiliations, so this is not a "Google Scholar"-style false positive, but the per-author mapping is unverified.**
- **Categories:** cs.CV (primary), cs.AI, cs.GR
- **Open release:** project page only, no code/weights stated — <http://SpaceFlow3D.github.io>
- **Shipped counterpart:** none found

**Summary:** SpaceFlow is a training-free pipeline for locally controllable 3D generation from text and a set of geometric primitives, where each primitive acts as a per-part proxy with its own control strength.
**Purpose:** The authors want users to specify, per object part, whether generation should strictly follow an input shape or allow generative completion, and to localize appearance cues (text/image) to specific parts without cross-part leakage.
**Breakthrough:** The authors report that regional geometry metrics show SpaceFlow preserves specified geometry in high-control regions while allowing plausible shape variation in low-control regions.
**Tools & method:** Structure generation enforces per-primitive spatial constraints inside the generative flow process; for appearance, the generated structure is segmented and matched back to the primitives so each part is conditioned only on its assigned text/image cue.
