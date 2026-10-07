**[A04] DistScene: Object-to-Scene Distillation for 3D Scene Generation**
- **arXiv:** 2610.06960 · <https://arxiv.org/abs/2610.06960>
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 16:21:52 UTC)
- **Authors:** Kunming Luo et al.
- **Qualifying affiliation(s):** TeleAI / China Telecom — Chengcheng Zhou, Haibin Huang, Xuelong Li (Kunming Luo via internship); other authors: HKUST. **FLAG: borderline** — TeleAI/China Telecom is not on the tracker's explicit company list and its standing relative to tracked gaming/3D industry labs is unclear, so this is kept per the tracker's guidance for unsure industry labs rather than dropped.
- **Categories:** cs.CV
- **Open release:** none (project page lists code/checkpoint/dataset as "coming soon"; a HuggingFace preview-assets page exists: <https://huggingface.co/coolbeam/DistScene-preview-assets>)
- **Shipped counterpart:** none found

**Summary:** DistScene generates compositional 3D scenes from a single image by jointly producing separate environment and object components in a unified coordinate system, then refining objects and distilling object-level generative priors into the scene.
**Purpose:** It targets single-image 3D scene generation that preserves spatial coherence between objects and their environment alongside the fidelity of individual objects, which the authors say existing scene-level methods have not addressed well.
**Breakthrough:** The authors report improved spatial coherence over existing approaches on indoor (MIDI-test, Gen3DSR-test) and outdoor (UrbanScene3D) benchmarks, with additional qualitative evaluation on ScanNet.
**Tools & method:** Scene-Frame Generation jointly produces environment and object components, Object-Centric Refinement locally enhances each object with scene awareness, and Object-to-Scene Distillation transfers knowledge from pretrained object-generation models into the scene pipeline.
