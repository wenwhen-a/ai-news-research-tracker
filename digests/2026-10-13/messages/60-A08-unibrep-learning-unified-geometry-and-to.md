**[A08] UniBRep: Learning Unified Geometry and Topology for Image-conditioned B-Rep Generation**
- **arXiv:** 2610.04092 · <https://arxiv.org/abs/2610.04092>
- **Submitted:** 2026-10-02
- **Authors:** Haiyang Ying, Allen Tu, Jiaye Wu, Tom Goldstein, Matthias Zwicker
- **Qualifying affiliation(s):** Amazon — Jiaye Wu (listed as "Amazon, Bellevue, Washington, USA"); other authors are University of Maryland, College Park
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** none found (no code/demo link in abstract, comments, or HTML)
- **Shipped counterpart:** none found

**Summary:** UniBRep is a geometry-first framework that adapts a pretrained image-to-3D model to generate CAD B-Rep (boundary representation) solids from a single image.
**Purpose:** The authors target image-conditioned CAD generation, aiming to directly produce structured, editable B-Rep CAD models (not just meshes) from a single input image.
**Breakthrough:** The authors report producing valid B-reps for 80.49% of DeepCAD inputs and reducing face Chamfer distance from 0.1096 (CADDreamer) to 0.0345. They also report outperforming the HoLa public demo in a matched comparison, and qualitatively demonstrate generalization to shapes beyond 30 faces, outside the CAD training distribution, and to real photographs.
**Tools & method:** The method adapts a pretrained image-to-3D generative model and adds dual decoder branches for geometry and face-separation features, followed by a CAD-kernel construction pipeline that fits surfaces and recovers curves/connectivity.
**Limitation:** The paper does not state explicit failure-mode limitations beyond reporting the 80.49% valid-B-rep rate (implying ~20% of inputs do not yield a valid B-rep).
