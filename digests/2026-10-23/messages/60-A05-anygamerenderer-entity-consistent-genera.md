**[A05] AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark**
- **arXiv:** 2610.31466 · <https://arxiv.org/abs/2610.31466>
- **Submitted:** 2026-10-22
- **Authors:** Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
- **Qualifying affiliation(s):** Alaya Lab (affiliated with Shanda AI Research) — all authors (FLAG: Alaya Lab/Shanda AI Research is not on the default qualified-company list; kept and flagged as a comparable industry lab)
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** AnyGameRenderer is a video-to-video generative renderer that converts rough game footage — gray blockouts or wireframes — into detailed, game-like visuals while preserving the original layout, camera motion, and entity positions and timing.
**Purpose:** The authors target a gap in generative game rendering where existing models struggle to keep individual entities (characters, objects) visually and positionally consistent across frames and across different games; they introduce an entity-level benchmark to measure this specifically.
**Breakthrough:** The authors report that fine-tuning improves temporal entity-match accuracy from 50.9% to 62.9% over the base model on their new entity-level benchmark, and reduces missed entity-count changes.
**Tools & method:** AnyGameRenderer is built via LoRA fine-tuning of MiniMax-H3, a 33B-parameter reference-video-conditioned video generation model, trained on roughly 10,000 paired clips sourced from agent-made games, Unreal Engine footage, and real gameplay recordings.
**Limitation:** The paper's current abstract/metadata do not state limitations beyond the reported benchmark gains; no cross-engine generalization or real-time performance figures are given.
