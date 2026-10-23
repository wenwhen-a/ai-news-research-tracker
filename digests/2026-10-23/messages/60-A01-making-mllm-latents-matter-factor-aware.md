**[A01] Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation**
- **arXiv:** 2610.30926 · <https://arxiv.org/abs/2610.30926>
- **Submitted:** 2026-10-22
- **Authors:** Songlin Yang, Zhe Wang, Xiaotong Zhao, Xi Wang, Ran Zhang, Shuai Li, Taiyi Wu, Songlian Li, Eric Liu, Alan Zhao, Anyi Rao
- **Qualifying affiliation(s):** Tencent Video — Xiaotong Zhao, Ran Zhang, Shuai Li, Taiyi Wu, Songlian Li, Eric Liu, Alan Zhao
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** The paper proposes Factor-Aware Predictive Learning (FAPL), a training method that makes latent representations from multimodal large language models (MLLMs) directly usable to condition video diffusion transformers for cinematic video generation.
**Purpose:** The authors address a gap between MLLM-derived representations (built for understanding) and the conditioning signals video diffusion transformers need for controllable generation, aiming to make a single latent space serve both generation and fine-grained editing.
**Breakthrough:** FAPL uses a three-stage training process — grounding the generator on frozen MLLM latents, training factor-specific edits with paired videos, then training limited-input representations (e.g., text-only) to predict complete-video targets — which the authors report outperforms baselines on sparse-to-video generation, factor-aware editing, and multi-shot generation tasks.
**Tools & method:** The method builds on frozen MLLM latent representations combined with a video diffusion transformer, trained in three stages with paired-video supervision for factor-specific (e.g., lighting, camera, subject) edits.
**Limitation:** The paper's current abstract/metadata do not state specific failure modes or compute/data-scale limitations beyond the reported comparative results.
