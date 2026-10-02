**[A08] SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation**
- **arXiv:** 2610.00686 · <https://arxiv.org/abs/2610.00686>
- **Submitted:** 2026-09-30
- **Authors:** Mikhail Dereviannykh et al.
- **Qualifying affiliation(s):** Stability AI — Mikhail Dereviannykh; FLAG: borderline (not on the explicit qualified-company list but a comparable top-tier lab)
- **Categories:** cs.CV; cs.LG
- **Open release:** demo (project page with video examples: <https://semantoken.github.io>)
- **Shipped counterpart:** none found

**Summary:** SemanTok is a flexible video tokenizer for autoregressive video generation that feeds frozen DINO features into its encoder and adds lightweight heads reconstructing those features from each retained token prefix, so early coarse tokens carry stronger global semantics.
**Purpose:** The authors state that existing flexible, coarse-to-fine video tokenizers only apply a representation-alignment (REPA) loss on early decoder hidden states, a target the decoder can partly satisfy from its noised input rather than from the tokens themselves.
**Breakthrough:** The authors report that a 201M-parameter SemanTok autoregressive model matches or beats a VideoFlexTok AR model 3.4× its size, that larger SemanTok models further improve fidelity, and that semantic alignment is retained on out-of-distribution classes and at every decoder noise level, including pure noise.
**Tools & method:** Training uses frozen DINO teacher features as both encoder input and per-prefix reconstruction target, with tokenizer training on Kinetics-600 and uCO3D and a LLaMA-style causal-decoder (RMSNorm, SwiGLU) autoregressive model built on top; a project page with video results is published.
