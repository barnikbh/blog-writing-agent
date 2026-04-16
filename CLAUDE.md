# Blog Writing Agent — Claude Context

## What it does
Converts weekly Obsidian notes into Medium blog drafts. Pipeline: reads notes → generates outline → writes draft → appends SEO + LinkedIn footer.

## Run
```bash
cd blog-writing-agent
source venv/bin/activate
python scripts/main.py
```

## Output
Drafts saved to `drafts/YYYY-MM-DD_slug.md`

## Draft format — bottom of every file
Every draft must end with both sections:

### SEO section (`<!-- SEO -->`)
- 3 headline options (under 65 chars, benefit-driven)
- Meta description (140-160 chars)
- 4-6 Medium tags
- Estimated read time

### LinkedIn section (`<!-- LinkedIn -->`)
- `linkedin_summary`: 3-4 short paragraphs, first person. Hook with the core problem → what article covers → key takeaway → low-friction CTA
- `linkedin_hashtags`: 8-12 tags, mix broad (#SoftwareEngineering) and specific (#LLMOps, #AgenticAI)

## Key files
- `scripts/prompts/seo_prompt.txt` — prompt for SEO + LinkedIn generation
- `scripts/seo.py` — `generate_seo()` + `format_seo_footer()` (renders both blocks)
- `scripts/prompts/writer_prompt.txt` — writing style prompt
- `memory/user_background.json` — Barnik's background context

## Published blogs (Medium: @barnikbh)
| # | Title | Date |
|---|-------|------|
| 1 | Observability in Agentic Systems | Apr 2026 |
| 2 | RBAC in Agentic Systems | Mar 2026 |
| 3 | Decoding A2A & MCP as a PM | Aug 2025 |
| 4 | MCP for Product People | Apr 2025 |
| 5 | Developing a Product Security Strategy | Mar 2025 |
| 6 | Balancing Speed & Quality in Semantic Search | Mar 2025 |
| 7 | Building No-Code AI Workflow Agents | Mar 2025 |
| 8 | Building RAG from the Ground Up | Mar 2025 |
| 9 | Building AI Labs: STT Model MLOps | Mar 2025 |
| 10 | Building Voice Gateway Infrastructure | Mar 2025 |

## Next topic candidates (researched Apr 2026 from Obsidian vault)
1. **Balancing Reliability and Innovation: The Parallel Testing Pattern** — STT model upgrade, parallel A/B infra
2. **Semantic Search at Scale: When Algorithms Fail** — recovery from 6th to industry-leading, hard metrics
3. **Data Governance for Multi-Tenant AI Systems** — GDPR, discovery, classification, retention
4. **Batch vs. Stream: When to Choose Each** — prescriptive framework, start with batch
5. **Building Contact Center AI: Smart+ Conversations** — multi-step intent, 30%→50% resolution rate
