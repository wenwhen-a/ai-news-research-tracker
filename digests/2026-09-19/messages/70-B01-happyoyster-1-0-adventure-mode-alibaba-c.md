**[B01] HappyOyster 1.0 "Adventure" mode — Alibaba Cloud Model Studio Open API**
- **Company:** Alibaba (ATH Innovation Business Group / Bailian platform)
- **Status:** GA · **Released:** 2026-09-17 · **New**
- **Surface:** Cloud API (Alibaba Cloud Model Studio / Bailian "newly released models" catalog; model id `happyoyster-1.0-adventure`)
- **Primary source:** <https://help.aliyun.com/zh/model-studio/newly-released-models> (catalog listing, dated 2026-09-17); sibling API reference pages e.g. <https://www.alibabacloud.com/help/zh/model-studio/happyoyster-directing-query-world-detail-api-reference> and <https://www.alibabacloud.com/help/zh/model-studio/happyoyster-acting-get-travel-credential-api-reference> confirm the `happyoyster-1.0-*` API family
- **Underlying research:** no traceable paper (only third-party benchmark papers, e.g. arXiv:2606.31672 "WorldRoamBench," reference HappyOyster as an evaluated system, not as its source)
- **Availability:** Priced, self-serve Open API on Alibaba Cloud Model Studio (Bailian); listed pricing is roughly $0.007067 per "World Creation" call and $0.028267 per second of "World Experience" (480p); no waitlist language found on the catalog page.

**What shipped:** Alibaba's Bailian ("Model Studio") "newly released models" catalog added `happyoyster-1.0-adventure` on 2026-09-17, exposing the "Adventure" (world-exploration) mode of its HappyOyster real-time interactive world model as a standalone, priced Open API endpoint.
**What research it translates:** Alibaba describes HappyOyster as a native multimodal, streaming world model that jointly generates audio and video and models state-transition/causal consistency to keep a generated world coherent over time.
