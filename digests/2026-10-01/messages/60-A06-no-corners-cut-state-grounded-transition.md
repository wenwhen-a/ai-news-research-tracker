**[A06] No Corners Cut: State-Grounded Transitions for Mid-Stream Prompt Switches in Video Generation**
- **arXiv:** 2609.38691 · <https://arxiv.org/abs/2609.38691>
- **Submitted:** 2026-09-30
- **Authors:** Zejing Rao et al.
- **Qualifying affiliation(s):** Kuaishou (Kling AI) — Xiaoqiang Liu, Yiping Meng, Guoxin Zhang
- **Categories:** cs.CV
- **Open release:** none found (no code/weights/demo link in the paper)
- **Shipped counterpart:** none found

**Summary:** The paper proposes a training-free VLM planner plus a distillation technique (SpanDMD) to prevent "corner cutting" — implausible shortcuts — when streaming video generators must respond to mid-stream prompt switches, evaluated on a new OpenTrans-360 benchmark of 1,800 prompt switches.
**Purpose:** It addresses the problem that existing streaming video generation systems keep visual smoothness during prompt changes but produce semantically incoherent transitions, such as object duplication, invalid physical interactions, or abrupt state jumps.
**Breakthrough:** The authors report an overall score of 0.887 on OpenTrans-360 versus 0.866 for the strongest baseline, ranking first on all 8 transition metrics, and a user-study preference rate above 50% against all 12 baselines tested.
**Tools & method:** State-Grounded Segue Planning uses a VLM (JoyAI-VL-Interaction) to generate intermediate "segue prompts" through a Transition Dependency Schema (Terminate, Release, Align, Entry roles); SpanDMD distills a frozen Wan2.1-T2V-14B teacher into a Wan2.1-T2V-1.3B student while restricting each prompt's gradient contribution to its assigned temporal span.
**Limitation:** The authors state the method lacks explicit modeling of physical prerequisites (e.g., support conditions), relies only on the single latest frame which limits motion history, and that there is a training-inference gap because planner training data is text-only while inference is visually grounded.
