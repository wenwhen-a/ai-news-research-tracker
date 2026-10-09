**[A10] Controllable Exaggeration for Generative Motion Models via Training-Time Adaptation and Inference-Time Guidance**
- **arXiv:** 2610.12316 · <https://arxiv.org/abs/2610.12316>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Amirhossein Zamani et al.
- **Qualifying affiliation(s):** Autodesk Research — all three authors are jointly listed under Autodesk Research, Mila (Quebec AI Institute), and Concordia University in the HTML author block (per-author institution not individually distinguished); acknowledgments separately state the work was "supported by Autodesk Research and the Autodesk AI Lab." **Flag: Autodesk is not on the explicit tracked-company list; keeping as a comparable top-tier industry lab for character-animation tooling (comparable to Adobe), for user judgment.**
- **Categories:** cs.CV
- **Open release:** project page (demo/visual results), no code/weights stated — <https://ahhhz975.github.io/ControllableMotionExaggeration/>
- **Shipped counterpart:** none found

**Summary:** The paper addresses the Exaggeration principle of traditional animation — largely absent from recent physically-plausible motion generative models — and proposes a two-stage framework to add it to existing text-to-motion pipelines.
**Purpose:** The authors want motion generative pipelines to produce character motion that is not only physically plausible but also expressive and engaging in the way professional animators design motion, specifically via the exaggeration principle.
**Breakthrough:** The authors report that, against three strong motion-generation baseline models, their methods generate "more exaggerated and expressive motions while preserving neutral reference motion intent and physical plausibility" (authors' claim, qualitative and quantitative evaluation).
**Tools & method:** Training-time: supervised fine-tuning of pretrained text-to-motion models on a curated exaggeration dataset.
