**[A12] Does Native 3D Texture Generation Necessarily Require 3D Assets for Training?**
- **arXiv:** 2609.34621 · <https://arxiv.org/abs/2609.34621>
- **Submitted:** 2026-09-28
- **Authors:** Jiangshan Wang, Zeqiang Lai, Jiayi Guo, Xin Yang, Xin Huang, Jiarui Chen, Ziheng Ouyang, Chunchao Guo, Xiangyu Yue
- **Qualifying affiliation(s):** Tencent — via "Tencent Hunyuan" affiliation for Jiangshan Wang, Xin Yang, Xin Huang, Jiarui Chen, Ziheng Ouyang
- **Categories:** cs.CV
- **Open release:** code — <https://github.com/wangjiangshan0725/Tex-Zero>
- **Shipped counterpart:** none found

**Summary:** The paper introduces Tex-Zero, a native 3D texture generation framework (VAE + diffusion transformer) trained entirely without 3D asset data.
**Purpose:** The authors ask whether native 3D texture generation genuinely requires 3D training assets, arguing that fine-grained 2D color/texture information matters more than 3D geometry data, which can instead be synthesized procedurally.
**Breakthrough:** The authors report that Tex-Zero produces high-fidelity textures with fine detail despite being trained using only 2D image data, and that its VAE generalizes to reconstruct real 3D assets never seen in training.
**Tools & method:** Method: synthetic 3D training samples built from planar-projected 2D images with random rotation/aggregation; a VAE trained on these samples; a diffusion transformer trained on the same data with multi-view image conditioning via the VAE encoder.
**Limitation:** The abstract/HTML reviewed did not list explicit acknowledged limitations beyond the core claim being about texture fidelity; no quantitative benchmark comparisons were surfaced in the sections reviewed.
