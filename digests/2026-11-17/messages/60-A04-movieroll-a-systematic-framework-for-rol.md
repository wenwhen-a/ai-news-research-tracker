**[A04] MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos**
- **arXiv:** 2611.21339 · <https://arxiv.org/abs/2611.21339>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Yunyang Ge et al.
- **Qualifying affiliation(s):** Tencent Hunyuan (one of three affiliations listed on the paper, alongside Peking University and HKUST; exact per-author mapping was not extractable from the HTML, but a footnote notes some authors' work was "done during an internship at Tencent Hunyuan," indicating Tencent Hunyuan staff co-authorship)
- **Categories:** cs.CV
- **Open release:** code + weights — project page <https://Tencent-Hunyuan.github.io/MovieRoll/>, GitHub <https://github.com/Tencent-Hunyuan/MovieRoll>, Hugging Face <https://huggingface.co/yunyangge/MovieRoll>
- **Shipped counterpart:** none found

**Summary:** Streaming video generators must sustain quality beyond their training horizon while managing growing self-generated history and KV-cache costs.
**Purpose:** To let streaming/autoregressive video diffusion models generate stable, high-quality long-form video well beyond the duration they were trained on, without exploding cache memory or losing motion naturalness.
**Breakthrough:** The authors report their hierarchical KV-cache compression (HieraKV), which keeps full history in shallow layers and sink-plus-recent history in deeper layers, reduces cache memory by up to 78% while improving generation quality; their cumulative long-tuning distillation (CuLT-DMD) enables efficient long-rollout training of a few-step generator by averaging local gradients while holding parameters fixed during each rollout.
