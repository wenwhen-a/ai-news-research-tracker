**[A12] GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models**
- **arXiv:** 2611.19247 · <https://arxiv.org/abs/2611.19247>
- **Submitted:** 2026-11-14
- **Authors:** Bing He et al.
- **Qualifying affiliation(s):** Tencent (Lightspeed Studios) — all authors
- **Categories:** cs.CV
- **Open release:** none found (no GitHub/HuggingFace link located; the paper describes models up to 33B parameters but gives no public weights link)
- **Shipped counterpart:** none found

**Summary:** The authors propose GameWM, a design for next-generation video games that splits responsibilities between a lightweight "engine" that keeps exact rules/state/camera/world-layout and a generative video model ("VM") that renders the look of the world and the detail of player interactions.
**Purpose:** The paper argues that existing game world models treat the video model merely as a restyling renderer of engine-authored motion, leaving most of its generative capacity unused and limiting game diversity.
**Breakthrough:** The authors report their distilled four-step causal student runs at 3.1s for the first chunk and 0.94-1.30s per subsequent chunk on 8 H200 GPUs (13-18 fps, vs. a 95s run for the bidirectional 33B model), and that character-identity preservation (DINOv2 similarity to a character sheet) shows a 0.107 margin between the protagonist's own sheet and other characters.
**Tools & method:** The system has three backbones — GameWM-H3-33B, GameWM-Wan2.2-14B, and a causal GameWM-Wan2.2-5B — with the 33B model distilled into a four-step causal student for real-time, chunk-by-chunk generation.
**Limitation:** The authors state the evaluation is visual-only on held-out clips with no quantitative ranking against other systems, and that the current system realizes only a few skill looks (bare-handed melee, cars/a helicopter as vehicles), with other looks depending on inference-time text prompts.
