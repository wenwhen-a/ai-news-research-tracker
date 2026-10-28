**[A03] Hy-Nomas: Towards Free-form Interactive World Generation**
- **arXiv:** 2610.36729 · <https://arxiv.org/abs/2610.36729>
- **Submitted:** 2026-10-27
- **Authors:** Qiaoling Chen et al.
- **Qualifying affiliation(s):** Tencent — all listed authors (Tencent Hy Visual Generation Team)
- **Categories:** cs.CV
- **Open release:** weights + code — the abstract states "We release model weights, code and benchmarks, together with a lightweight adaptation workflow"; no direct link found on the abstract page (comment field just says "Technical Report")
- **Shipped counterpart:** none found

**Summary:** Hy-Nomas is an 8B-parameter diffusion-based video world model that follows free-form text instructions and continuous camera control across multiple interaction turns, generating variable-length video segments from current inputs and cached history.
**Purpose:** The authors target interactive world generation, where a model must follow successive user commands while preserving relevant history and the consequences of prior actions.
**Breakthrough:** The authors report that in human evaluation, Hy-Nomas shows superior performance over existing world models.
**Tools & method:** The model uses an 8B diffusion backbone, a vision-language Prompt Enhancer module, and a multi-stage curriculum that progressively introduces causal generation, text interaction, camera control, and training on model-generated histories, followed by diffusion distillation.
**Limitation:** The paper is described as a technical report rather than a peer-reviewed publication, and the evaluation relies on human preference judgments rather than only automated metrics (as stated).
