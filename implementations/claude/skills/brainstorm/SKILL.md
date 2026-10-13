---
name: brainstorm
description: "Use for an open, consequential choice (architecture, product fork, unfamiliar problem) where the first idea may be only a local optimum. Never reopens settled choices and adds no padding to trivial decisions."
---

# brainstorm

Generate genuinely different alternatives, hold them without choosing, then collapse on stated criteria.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../prompting/brainstorm.md`
- `${CLAUDE_PLUGIN_ROOT}/../../prompting/superposition-collapse.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/decisions.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Check that the choice is open and consequential. Look for a settled answer first (the specification gate record, decision records, the HANDOFF owner block, earlier answers in this session); a settled choice is not reopened and a trivial one gets no ceremony.
2. Propose before you select. For a broad fork write five distinct approaches: conventional, unconventional and intentionally wild. For a bounded choice list the viable alternatives only, without padding.
3. For each alternative state its essence and two side effects first, then score feasibility, impact and risk from 1 to 10 with a reason and the uncertainty. Scores are estimates, not measurements.
4. Hold the set, then collapse on the owner's criteria or on the delegated scope. When the owner owns the choice, ask with AskUserQuestion, put the recommended option first, and record the answer verbatim with who, when and the artifact it covers.
5. Record the chosen and deferred options, the reason, and the evidence that would reopen the choice, in the decision's existing home.

Limits:
- Proposal and selection stay separate; no selection is implemented here.
- Silence, a default, another agent or a tool result is never the owner's choice.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
