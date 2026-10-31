**[A01] Wizard: Manipulate Any World in Real Time via Agentic Control**
- **arXiv:** 2610.40339 · <https://arxiv.org/abs/2610.40339>
- **Submitted:** 2026-10-29
- **Authors:** Yuzhe Wu, Zijun Lin, Yeying Jin
- **Qualifying affiliation(s):** Tencent — Yuzhe Wu, Zijun Lin, Yeying Jin
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://wyzardwu.github.io/wizard>)
- **Shipped counterpart:** none found

**Summary:** Wizard is an agentic game world model that gives real-time, precise control over character motion in generated game worlds. It generalizes zero-shot to new scenes, characters, and actions, conditioning video generation on skeleton and geometry information as intermediate representations. An agentic framework tracks and updates game state alongside an adaptive masking mechanism.
**Purpose:** The authors aim to overcome existing game/world models' limited control flexibility and generalization, where action-conditioned models restrict players to predefined action sets and prompt-conditioned models struggle with instructions unseen during training.
**Breakthrough:** The authors report that Wizard demonstrates strong zero-shot generalization to unseen characters, scenes, and motions, letting players create and manipulate customized game worlds. They built a supporting dataset of 750 scenes and 178 characters to enable this generalization.
**Tools & method:** The method uses skeleton and geometry information as intermediate representations to condition video generation, combined with an adaptive masking mechanism and an agentic framework that maintains and updates explicit game state separate from the visual generation process.
**Limitation:** The authors state that Wizard's reliance on a motion library makes it difficult to find compatible motions for characters with uncommon body structures, and that consistency between scene proxies and generated video may decline over longer rollouts.
