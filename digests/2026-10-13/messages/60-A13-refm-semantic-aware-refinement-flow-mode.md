**[A13] ReFM: Semantic-Aware Refinement Flow Model for Motion Retargeting**
- **arXiv:** 2609.32068 · <https://arxiv.org/abs/2609.32068>
- **Submitted:** 2026-09-25
- **Authors:** Jingxiang Qu, Lucie Taglienti, Evan Atherton
- **Qualifying affiliation(s):** Autodesk (borderline/comparable company, flagged) — Lucie Taglienti and Evan Atherton listed under "Affiliation: Autodesk Research"; Jingxiang Qu's work was conducted "during an internship at Autodesk" under their mentorship
- **Categories:** cs.CV (primary), cs.AI, cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** ReFM addresses motion retargeting — transferring motion between characters with different skeletons — by treating it as progressive refinement rather than single-pass regression or direct copying of source motion.
**Purpose:** The authors argue existing retargeting methods carry over artifacts from mismatched character proportions when copying source motion as initialization, and that single-pass regression is too restrictive for this underdetermined problem.
**Breakthrough:** The authors report that ReFM works as a refinement layer compatible with different initializations, including both direct motion copying and Autodesk HumanIK (an industry-standard full-body IK retargeting system), improving on both.
**Tools & method:** Core components: an SO(3) canonicalizer for orientation normalization, a contrastively pretrained cross-character semantic encoder, and a learned flow-based refinement model conditioned on semantic/physical/temporal objectives.
**Limitation:** The abstract/HTML reviewed did not state explicit acknowledged limitations; no quantitative results or dataset details beyond the method description were extracted.
