**[A02] Position Forcing: Self-Conditioning 3D Generation**
- **arXiv:** 2610.10342 · <https://arxiv.org/abs/2610.10342>
- **Submitted:** 2026-10-07
- **Authors:** Ziheng Ouyang, Zeqiang Lai, Jiarui Chen, Jiangshan Wang, Yuhao Wan, Jingbo Gong, Xiangyu Yue, Hengshuang Zhao, Qibin Hou, Chunchao Guo
- **Qualifying affiliation(s):** Tencent Hunyuan — one of the paper's four listed institutions (VCIP/Nankai University, Tencent Hunyuan, MMLab/CUHK, Fudan University, Shanghai Innovation Institute, HKU); corresponding author Chunchao Guo lists a tencent.com address
- **Categories:** cs.CV
- **Open release:** none found on the arXiv page
- **Shipped counterpart:** none found (compared against Tencent's own shipped Hunyuan3D-2.1 as a baseline, see below, but Position Forcing itself is not shipped)

**Summary:** The paper targets single-stage 3D generative models that represent shapes as unordered sets of latent tokens (VecSet representations), which must implicitly infer each token's position during denoising.
**Purpose:** The goal is to improve single-stage VecSet 3D generation quality by giving the diffusion transformer explicit, coarse-to-fine positional guidance instead of leaving position purely implicit.
**Breakthrough:** On reconstruction (Chamfer Distance/F1), Position Forcing reports 5.39/95.38 at the largest tested latent size (64×20480) versus Tencent's own Hunyuan3D-2.1 at 7.62/92.06 on the same setting.
**Tools & method:** The method quantizes recovered token positions at progressively finer resolutions across denoising stages and re-injects them as positional encodings into the diffusion transformer; inference runs in BF16 precision.
**Limitation:** The paper has no dedicated limitations section; the authors note as a design trade-off that training uses single-timestep sampling rather than unrolling the full inference trajectory, to avoid added computational overhead.
