---
name: spec-recon
description: "Use for read-only reconnaissance before writing a new specification, or when evidence synthesis is explicitly requested: independent Code, Data and Decisions lanes (Legacy and Web when relevant) with measured claims and citations."
---

# spec-recon

Measure the real situation before anyone specifies a change, and keep measured facts apart from guesses.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/reconnaissance.md`
- `${CLAUDE_PLUGIN_ROOT}/../../roles/searcher.md`
- `${CLAUDE_PLUGIN_ROOT}/../../concepts/glossary.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. The root defines the question, the actual population and the evidence that would answer it, and snapshots Git ownership read-only (`git status --porcelain -uall`, HEAD).
2. Account for the Code, Data and Decisions lanes, and for Legacy and Web when they apply. Dispatch independent read-only lanes with the Agent tool (`subagent_type: methodology-claude:searcher`, `model: haiku` for inventories or `sonnet` for reconnaissance of a named area), within the host's concurrency; the searcher has no web tools, so the root runs the Web lane with WebSearch and WebFetch. Inner roles never dispatch lanes.
3. Each lane returns claims labelled measured, computed, estimated or unverified, original citations, contradictions and unchecked limits. Data may be N/A only for an actual absence trigger, and fixtures are not live data. Record `git status` before and after each dispatch.
4. The root reconciles the pivotal claims against independent evidence, then writes the dated RECON synthesis with contradictions and open forks, and only then the specification.

Limits:
- No negative fact is invented; a missing return is a limitation, not "nothing found".
- Reconnaissance lanes write nothing; the root writes only the RECON note and the specification at their granted homes and commits nothing without a grant.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
