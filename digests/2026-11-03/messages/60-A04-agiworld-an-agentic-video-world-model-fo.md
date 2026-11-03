**[A04] AgiWorld: An Agentic Video World Model for Building Persistent Worlds**
- **arXiv:** 2611.02341 · <https://arxiv.org/abs/2611.02341>
- **Submitted:** 2026-11-02
- **Authors:** Shaoheng Fang et al.
- **Qualifying affiliation(s):** Adobe Research — the paper lists two affiliations for the author group, "The University of Texas at Austin" and "Adobe Research" (the exact per-author split was not recoverable from the extracted text, but several co-authors, consistent with prior Adobe Research publications in this area, are Adobe-affiliated; Kalyan Sunkavalli is an established Adobe Research scientist)
- **Categories:** cs.CV, cs.AI
- **Open release:** demo/project page (<https://bshfang.github.io/agiworld/>); code not yet available (the paper states the agent's guidelines, schemas, and specification "will be released with the code")
- **Shipped counterpart:** none found

**Summary:** The paper presents AgiWorld, a system that builds a persistent, explorable video world from a single image and a free-form instruction, combining a planning agent (AgiWorld-Agent) that designs the world and directs exploration with a video world model (AgiWorld-WM) that generates video in chunks and stores it with geometry in a spatial memory.
**Purpose:** The authors target long-horizon world generation where previously generated regions must remain consistent when revisited, which plain video generation alone struggles to maintain.
**Breakthrough:** The authors report state-of-the-art results on world revisiting and exploration benchmarks, and state that persistence "arises not from the video model alone but from its closed loop with the agent," using occlusion-aware history selection and reliability-based memory maintenance for long rollouts.
