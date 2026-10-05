**[B05 · Update] HappyOyster Acting (happyoyster-1.0-acting)**
- **Company:** Alibaba (ATH Innovation Business Group / Bailian) — borderline unit, flagged
- **Status:** GA (inferred, see caveats) · **Released:** 2026-09-17 (catalog listing date) · **Update**
- **Surface:** cloud API (Alibaba Cloud Model Studio / Bailian Open API)
- **Primary source:** <https://help.aliyun.com/zh/model-studio/newly-released-models#happyoyster-1.0-acting>
- **Underlying research:** no traceable paper
- **Availability:** Singapore-hosted deployment, listed as "国际" (international) region; Open API

**What shipped:** Update since 2026-09-22: HappyOyster Acting, previously tracked as Announced-only, now appears in the same "newly-released-models" table as the GA happyoyster-1.0-adventure entry, with identical formatting and the same 2026-09-17 international/Singapore date. The page describes it as "实时交互的角色演绎模型，基于多模态" (a real-time interactive, multimodal character role-play/performance model).
**What research it translates:** Same HappyOyster world-model/character-interaction line as the other HappyOyster endpoints; no arXiv paper found — "no traceable paper."
**Practical significance:** Exposes the "Acting"/character-interaction mode of HappyOyster as a standalone, developer-callable endpoint distinct from the consumer happyoyster.cn product, if the apparent tier change holds.
**Engineering details:** Deployed via Alibaba Cloud Model Studio, Singapore region; no API call example or pricing figure for Acting specifically could be retrieved this pass.
**Limitation / caveats:** Same caveat as Directing: the page uses no explicit GA/Beta label for any model row, so the Announced→available change is inferred from table placement, not an explicit status statement — moderate confidence. Treat as provisional until an explicit "立即调用"/pricing section for Acting is found.
