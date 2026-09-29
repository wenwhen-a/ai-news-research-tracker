**[A12] WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation**
- **arXiv:** 2609.30221 · <https://arxiv.org/abs/2609.30221>
- **Submitted:** 2026-09-24
- **Authors:** Yubo Zhu et al.
- **Qualifying affiliation(s):** Alibaba Group (Wan Team) — multiple co-authors
- **Categories:** cs.CV
- **Open release:** none confirmed (project page only: <https://wan-pe.github.io/;> no code/weights link stated)
- **Shipped counterpart:** none found

**Summary:** WanPE is a large (reported ~397B-parameter) prompt-enhancement model that plans cinematic elements — actions, camera trajectories, lighting, and sound — for text-to-video generation, rather than just elaborating captions descriptively.
**Purpose:** As text-to-video generators now handle multi-shot, tens-of-seconds outputs, prompt enhancement needs to orchestrate cinematic planning (shots, camera moves, audio) rather than merely add descriptive detail, while still preserving the user's original request throughout the sequence.
**Breakthrough:** The authors report their video-grounded reverse-construction supervision beats forward rewriting by 10.37 points, their Semantic-Consistency GRPO (SC-GRPO) improves semantic consistency by 18.6-23.3 points across model scales, and enhanced prompts improve human preference by 50.86 points over raw prompts at 30-second generation lengths.
**Tools & method:** The approach derives supervision by reverse-constructing user requests (via LLM) from cinematic conditions mined from 1.05M real videos, then applies SC-GRPO, a nine-dimensional reward function penalizing omissions, alterations, incorrect bindings, and temporal inconsistencies; training used 512 GPUs, and evaluation used the new WanPEval benchmark (249 requests, ~11K expert pairwise assessments from 60 film professionals).
