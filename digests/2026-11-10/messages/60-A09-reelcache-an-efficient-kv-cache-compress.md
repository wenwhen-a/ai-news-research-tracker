**[A09] ReelCache: An Efficient KV Cache Compression and Management System for Multi-Round Video Generation**
- **arXiv:** 2611.09973 · <https://arxiv.org/abs/2611.09973>
- **Submitted:** 2026-10-31
- **Authors:** Tianyu Wang, Daiyang Yu, Zhiwei Ren, Junbo Li, Jitian Zhang, Longfei Shangguan
- **Qualifying affiliation(s):** Google — Jitian Zhang
- **Categories:** cs.CV, cs.DC
- **Open release:** code — <https://github.com/Tianyu9748/ReelCache>
- **Shipped counterpart:** none found

**Summary:** ReelCache is a system that compresses and manages the attention key-value (KV) caches of autoregressive video diffusion models during multi-round, interactive video generation.
**Purpose:** The authors motivate the work around consumer-facing creative video tools (citing Google Veo, ByteDance Seedance, Adobe Firefly) where users iteratively extend, review, and revise generated video clips — returning to earlier points to replace unsatisfactory segments or explore alternative continuations.
**Breakthrough:** The authors report a combined intra-chunk (low-rank + video coding) and inter-chunk (shared basis directions, tree-structured chunk-state management) compression scheme implemented in SGLang-Diffusion, enabling resume/rewind/fork operations with large storage and latency reductions.
**Tools & method:** The system targets chunk-autoregressive video diffusion transformers, implemented atop SGLang-Diffusion, and is evaluated using six VBench dimensions plus SSIM against uncompressed references on the authors' Synthetic-500 multi-round generation dataset.
**Limitation:** The authors state the method's scope excludes bidirectional-denoising and in-place-editing video models, since their KV may not remain valid as an unchanged prefix; full-attention models see decompression slowdowns of 3.2-4.2%; and the speedup advantage shrinks as rewind frequency increases.
