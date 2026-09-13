**[A10] Learning 3D Editing without Paired Supervision via Generative Prior Distillation**
- **arXiv:** 2609.04942 · https://arxiv.org/abs/2609.04942
- **Submitted:** 2026-09-04
- **Authors:** Hao Wen, Weibin Yun, Hongxing Fan, Haotian Lu, Rui Chen, Zehuan Huang, Lu Sheng
- **Qualifying affiliation(s):** VAST — Zehuan Huang; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (https://github.com/thiamine128/PriorEdit3D)
- **Shipped counterpart:** none found

**Summary:** PriorEdit3D is a feed-forward instruction-guided 3D editing framework built on the UniLat3D geometry-appearance latent that learns without paired 3D before/after data, distilling visual priors from 2D image-editing models and semantic priors from vision-language models, with a 3D-aware distribution-matching regulariser.
**Purpose:** It addresses the scarcity of paired 3D editing training data.
**Breakthrough:** The authors report the best scores among compared methods (EditP23, Instant3DiT, 3DEditFormer, VoxHammer, Nano3D): PSNR 24.37, SSIM 0.94, FID 71.96, LLM-Identity 93.13%, LLM-Instruction 86.92%, at a reported 7-second runtime.
**Tools & method:** UniLat3D prior with differentiable rendering; Qwen3-VL-4B for semantic feedback; Qwen-Image-Edit-2511-Lightning for 2D edits; Gemini3-Flash for instruction generation; trained on Objaverse (73,451 objects); evaluated on a 130-sample set plus Amazon Berkeley Objects and Google Scanned Objects.
**Limitation:** The authors state it struggles with fine-grained edits such as text and small dense instances, non-edited regions may drift, and the UniLat3D prior makes large pose or topology changes difficult.
