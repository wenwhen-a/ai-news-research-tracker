**[A02] State World Models: Execute the Rules, Generate the Pixels**
- **arXiv:** 2610.26811 · <https://arxiv.org/abs/2610.26811>
- **Submitted:** 2026-10-19
- **Authors:** Chan Yan Ki, Yanran Zhang, Wenzhao Zheng, Xiaofeng Wang, Zheng Zhu, Lei Chen, Jie Zhou, Jiwen Lu
- **Qualifying affiliation(s):** GigaAI (co-affiliation alongside Dept. of Automation, Tsinghua University); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** The paper introduces a "Stateful Harness" that separates world-state evolution from video rendering so that identical visible actions produce outcomes consistent with hidden state and explicit rules, plus WorldState-Bench, a set of 50 counterfactual pairs sharing a first frame and action but differing in hidden state (49 hidden variables, 21 themes).
**Purpose:** To test and support "state world models," where the same visible action should yield different outcomes depending on hidden state, evaluated against rules specified up front rather than left to the video model to infer.
**Breakthrough:** The authors report that wrapping a frozen, unmodified video model in their rule-resolution runtime raises PairFollow from 32% to 92%, i.e. no engine integration or model fine-tuning is required to make video generation obey hidden-state rules.
**Tools & method:** The runtime resolves each user action against a semantic ledger and an editable 3D scene using fixed rules, compiles the resolved event into a text instruction plus a 3D-scene preview clip for spatial guidance, and has a frozen video model render it while a VLM (Qwen3.8-27B-VL) updates state for the next turn.
**Limitation:** The authors state that rendering remains stochastic and zone-triggered state cases are the most demanding for the harness.
