**[A01] Unity Insight: A Production Code–Asset Index for LLM Coding Agents in Unity Projects**
- **arXiv:** 2609.27585 · <https://arxiv.org/abs/2609.27585>
- **Submitted:** 2026-09-23
- **Authors:** Shenhua Gu, Hongqiang Zhu, Fan Zhang, Jinming Zhang, Hao Chen
- **Qualifying affiliation(s):** Unity — all five authors list "Tuanjie Engine, Unity China, Shanghai, China" (Tuanjie Engine is Unity's own engine brand/joint venture operated for the China market)
- **Categories:** cs.SE
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper presents Unity Insight, a persistent, read-only code–asset index built to let LLM coding agents navigate Unity game-engine repositories, where gameplay logic spans C# scripts, prefabs, scenes, and ScriptableObjects linked by GUIDs and YAML serialization.
**Purpose:** Traditional code-only retrieval tools cannot answer cross-file questions common in Unity projects (e.g., "which prefabs instantiate this script?") without manually chaining GUIDs at high token cost.
**Breakthrough:** The authors report the index-backed agent used 53.4% fewer total tokens (5M → 2.3M) and 51.6% less wall-clock time (3,363s → 1,626s) than a general-purpose exploration agent, with 23 of 28 questions favoring the index at statistical significance (p=0.0009).
**Tools & method:** The system builds a persistent SQLite index that crawls and parses Unity components, resolving GUID↔path mappings between C# source and serialized assets, and exposes five typed query tools (vfs_ls, vfs_glob, vfs_grep, vfs_read, vfs_refs) for agents to traverse references instead of grepping raw GUIDs.
**Limitation:** The authors state the index "deliberately does not capture runtime or editor state" and represents only a static snapshot, with disclosed blind spots such as string-based `Resources.Load` dynamic loads.
