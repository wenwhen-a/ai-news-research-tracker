**[A01] Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity**
- **arXiv:** 2609.12090 · https://arxiv.org/abs/2609.12090
- **Submitted:** 2026-09-10
- **Authors:** Aditi Tiwari et al.
- **Qualifying affiliation(s):** Adobe Research — Akshit Bhalla, Darshan Prasad (Aditi Tiwari: work done during an internship at Adobe Research; primary university affiliation University of Illinois Urbana-Champaign)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper introduces "read-time memory substitution," a causal-audit method that swaps out the memory content a video model retrieves at inference time while leaving the rest of its computation unchanged, in order to separate whether a model's memory helps at all from whether the specific retrieved content is what actually drives that benefit.
**Purpose:** Standard memory ablations (removing memory entirely) can show that memory helps, but cannot show whether the gain depends on retrieving the correct past content versus just having some generic memory representation present.
**Breakthrough:** The authors report that on frozen video world models, identity-free control memories (containing no evaluation-specific content) recover "essentially the full benefit" on the Ego-Exo4D and 7-Scenes benchmarks and about 70% on TUM, and that in an Ego-Exo4D dose-response test, recovery falls from 102% to 1% as substituted memory values move away from observed training-memory representations — evidence the authors interpret as "representation repair" rather than true content-specific recall for those models.
**Tools & method:** Method: "read-time memory substitution" — replacing the memory value a model consumes at a given read step without altering surrounding computation — applied across a "substitution ladder," dose-response tests, and a leakage-safe TUM split.
