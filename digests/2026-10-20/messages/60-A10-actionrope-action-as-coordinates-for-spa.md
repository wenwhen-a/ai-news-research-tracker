**[A10] ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models**
- **arXiv:** 2610.25861 · <https://arxiv.org/abs/2610.25861>
- **Submitted:** 2026-10-19
- **Authors:** Zhiyang Deng, Yuzhe Wu, Zijun Lin, Yeying Jin
- **Qualifying affiliation(s):** Tencent — all four authors list Tencent as a primary affiliation, alongside National University of Singapore (Deng, Wu, Jin) and Nanyang Technological University (Lin)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper targets action control in "planar-camera" game world models (top-down/isometric games), where existing feature-based action conditioning fits poorly because it gives the model no explicit world coordinate system.
**Purpose:** The authors want game world models that follow commanded motion faithfully and don't "drift" (regenerate a different scene) when a player returns to a previously visited location, a known failure of feature-conditioned action control.
**Breakthrough:** On their main Wan2.2-TI2V-5B backbone, the authors report the method improves PSNR from 21.11 dB (best baseline, AdaLN) to 23.94 dB and cuts drift from 22.6 px to 7.8 px — a reported 66% drift reduction over the strongest of four re-implemented baselines (Prompt, Linear, AdaLN, Cross-Attn).
**Tools & method:** Training data comes from the game *No Rest for the Wicked* (2.5D fixed top-down view): 50.9 hours, 22,782 clips at 81 frames/16 fps/832×480, with 18,528 training and 982 held-out evaluation clips.
**Limitation:** The authors state the method assumes the static world translates approximately rigidly in the image plane (true for top-down/isometric cameras that follow the player), so it does not model zoom or strong parallax, and does not make moving objects follow world coordinates.
