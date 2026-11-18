**[A04] FailureGen: Scalable Robot Failure Data Generation with World Models**
- **arXiv:** 2611.22367 · <https://arxiv.org/abs/2611.22367>
- **Submitted:** 2026-11-17
- **Authors:** Akul Santhosh, Chaitra Sathe, Aastha Jhunjhunwala
- **Qualifying affiliation(s):** NVIDIA — all three listed authors (HTML affiliation block shows NVIDIA for the author group)
- **Categories:** cs.RO (primary); cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper addresses the scarcity of robot-failure data, which the authors say is "difficult to collect at scale," by generating synthetic failure videos with temporal event annotations. FailureGen reuses action trajectories from recorded real failures and transplants them into new visual contexts using a fine-tuned world model.
**Purpose:** To scale up the diversity and quantity of labeled robot-failure data for training failure-detection and robot-learning systems, without relying solely on scarce, hand-collected real failure recordings.
**Breakthrough:** The authors report that a failure detector trained on real plus generated data reached average precision of 0.51 versus 0.41 with real data alone, and detected 33 of 36 failure intervals versus 28 of 36 with real data alone. They describe this as a "preliminary comparison."
**Tools & method:** Four stages: (1) fine-tune an action-conditioned NVIDIA Cosmos world model on successful and failed real executions; (2) identify failure-related donor segments and compatible successful "host" recordings; (3) transfer donor motion into host contexts (with optional spatial offsets) to generate continuous rollouts; (4) annotate and filter generated samples by detected events and visual quality.
**Limitation:** The authors flag the headline numbers as coming from a "preliminary comparison" rather than a full evaluation; no dataset names or training/inference hardware are specified in the abstract.
