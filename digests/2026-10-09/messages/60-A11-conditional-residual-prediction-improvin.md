**[A11] Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher**
- **arXiv:** 2610.11479 · <https://arxiv.org/abs/2610.11479>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Bowen Zheng, Zhiguang Liu, Jiarong Ou, Rui Chen, Tianyang Hu
- **Qualifying affiliation(s):** Tencent Hunyuan — Zhiguang Liu, Jiarong Ou, Rui Chen. Other authors: The Chinese University of Hong Kong, Shenzhen (academic).
- **Categories:** cs.CV (primary); cs.AI, cs.LG (cross-listed)
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** The paper studies causal (autoregressive) video diffusion models, which suit streaming and long-video generation but typically underperform bidirectional models of the same size. Prior approaches initialize from or distill a pretrained bidirectional teacher; this work trains causal models from an image-model initialization with no bidirectional video model at any stage.
**Purpose:** To close the causal-vs-bidirectional performance gap and to curb error compounding caused by a causal model's dependence on its own (possibly erroneous) generated history at inference.
**Breakthrough (≤3 sentences, attributed):** The authors report Conditional Residual Prediction (CRP) nearly closes a 6.14-point gap to a bidirectional model under controlled, matched-setup experiments. Scaled up as "Optica," a 2B-parameter causal model, it generates 5-second 480p video and reaches 82.78 on VBench using about 15M training videos, per the authors.
**Tools & method:** CRP has the model predict the target without its conditioning input first, so the condition (e.g., past frames) only supplies a residual, reducing reliance on history for information the present already provides.
**Limitation:** Not stated in the available abstract text beyond the reported performance gap.
