---
name: prompting-verify
description: "Проверка факта или утверждения с источниками: «проверь факт», «проверь с источниками», «верифицируй утверждение», «подтверди источниками». Use when a factual claim, an agent decision or a design needs evidence and a bounded checking plan: name the pivotal claims, the sources and tools, the independent checks and the stop route."
---

# prompting-verify

Replace confidence with checks: each pivotal claim gets a source, a tool or an independent check, and a finite route when the check fails.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../prompting/verification.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/preflight.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/run-audit.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Name the pivotal claims and, for each, the real source or tool: Read, Grep and Bash for repository facts; WebSearch and WebFetch for external facts, preferring primary documentation for technical identifiers.
2. Plan factual, consistency and context checks. Verification questions and agreement of the same model are not external proof. Where the stakes are high use an independent actor and a contrary control, and apply the Diagnostic Trio (logs, code, data) to failures.
3. Preserve failed checks and stated uncertainty; do not fake consensus or demand hidden reasoning.
4. Give every check a finite retry count and a terminal route. Debug-entry spend in feature-dev is a different unit from response, transport and test retries and is never reset by them.
5. If a required proof is unavailable, the claim is BLOCKED or reported as unverified, never passed.

Limits:
- Structural conformance is not semantic verification.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
