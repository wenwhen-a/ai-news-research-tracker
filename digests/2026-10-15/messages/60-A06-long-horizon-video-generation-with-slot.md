**[A06] Long-horizon Video Generation with Slot Memory Addressed By Region Tokens**
- **arXiv:** 2610.19257 · <https://arxiv.org/abs/2610.19257>
- **Submitted:** 2026-10-13
- **Authors:** Eren Cetin et al.
- **Qualifying affiliation(s):** Google — Hyojun Go, Nikolai Kalischek, Federico Tombari (each listed with a joint "ETH Zurich / Google" affiliation note)
- **Categories:** cs.CV
- **Open release:** none found (no code repository or project page link located in the retrieved text)
- **Shipped counterpart:** none found

**Summary:** The paper introduces SMART, a slot-based memory for long-horizon video generation that keeps constant storage size while still supporting accurate recall of content when a camera revisits a previously seen location.
**Purpose:** The authors target a core tension in long video generation: memory must stay bounded so generation can continue indefinitely, but it must also recall distant, previously observed content accurately regardless of elapsed time, which neither reconstruction-based nor purely recurrent memories do well.
**Breakthrough:** The authors report that on long trajectories in Memory Maze and Minecraft, SMART achieves high-fidelity recall beyond the training horizon while maintaining constant memory size and per-step computational cost.
**Tools & method:** Memory writes are indexed by the observing camera and reads are queried by the rendering camera; each read also produces a confidence score that conditions a chunk-causal diffusion transformer, letting it selectively trust retrieved memory content versus falling back on its generative prior; evaluated in Memory Maze and Minecraft environments.
