**[B01] Kling 4.0 Flash API**
- **Company:** Kuaishou (Kling)
- **Status:** GA · **Released:** 2026-11-04 · **New**
- **Surface:** Cloud API (Kling developer API)
- **Primary source:** <https://kling.ai/document-api/updates/api.md>
- **Underlying research:** arXiv:2512.16776, "Kling-Omni Technical Report" (Kling Team, Kuaishou Technology) — inferred from the product family; Kuaishou has not published a paper naming "Kling 4.0 Flash" specifically
- **Availability:** Self-serve via the Kling developer API, no invitation mentioned in the changelog; billing is based on total generated duration (no official per-second price published)

**What shipped:** Kuaishou's Kling developer-API changelog records a new, separate Kling 4.0 Flash API endpoint (dated 2026-11-04), generating 3–20 second videos at 720P.
**What research it translates:** Kuaishou's most recent public technical report for the Kling line is the Kling-Omni Technical Report (arXiv:2512.16776, Dec 2025), describing a unified multimodal system combining generation, editing and reasoning with two-stage distillation for faster long-sequence inference.
**Practical significance:** Kuaishou states Flash is a faster, lower-latency tier of the same Kling 4.0 generation alongside the full model, giving API developers a cheaper/quicker option for shorter clips without waiting for full 1080p/30s generation.
**Engineering details:** Outputs are capped at 20 seconds versus 30 for the full model, and resolution is fixed at 720P (no 1080P option listed).
**Limitation / caveats:** No official per-second price was found on Kuaishou's own pages during this check; only unverified third-party reseller estimates exist, so availability/pricing should be reconfirmed directly against klingai.com before relying on it.
