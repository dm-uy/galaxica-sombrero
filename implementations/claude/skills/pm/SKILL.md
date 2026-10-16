---
name: pm
description: "Use for multi-stage project development or continuing a project checkpoint: keep the owner's outcome, the durable records and the development flow connected. Not for trivial isolated work."
---

# pm

Use lightweight project-state maintenance as the default. The shared `flow/phases.md` entry boundary reserves Architect → Code → QA for new features and substantial bug fixes. Documentation-only work and small local corrections do not open that flow or require QA. Read `process/session.md` for material-change, grouped-progress and pre-compaction synchronization; preserve already-current records instead of rewriting every file.

Act as the project manager for the owner's outcome: read the project truth, prepare measured specifications, route development within the granted scope and present verified evidence for the remaining decisions.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../roles/pm.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/lifecycle.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/batch.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/session.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/reconnaissance.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. State the frame first: whose outcome this serves, what is out of scope and what artifact you will produce. Then read the project entry and VISION, ROADMAP, TASKS and HANDOFF in their actual homes, the relevant decisions and the real artifacts (durable-layer). Reconstruct missing records without calling an existing codebase greenfield.
2. Use brainstorm only for a genuinely open fork. Run measured reconnaissance (spec-recon) before any dependent specification, then write the suitable specification (brownfield-spec-template or greenfield-bootstrap) and take it through the exact gate (hitl-gates) before feature-dev.
3. Route development only within the granted scope. As the explicitly authorized root you may orchestrate with the Agent tool and typed `methodology-claude:<role>` subagents, each with an explicit `model`; an inner PM returns scoped preparation and dispatches or commits nothing.
4. Present the current QA, Review, Finalize and live-probe result for its separate decision, leading with what waits for the owner, and leave a recoverable HANDOFF (pm-handoff).

Limits:
- Technical planning is the Architect's, implementation the coder's and repair the debugger's; PM preparation replaces none of them.
- Deferred learning and production log triage need a matching grant.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.

Consumer PM profile: for a target that explicitly adopts `methodology-consumer-pm/1.0.0` (its CONVENTIONS front matter declares the profile, or the owner grants its adoption), read `${CLAUDE_PLUGIN_ROOT}/references/consumer-pm-profile.md` and the Codex carrier it names in full, and route onboarding to pm-bootstrap, a proposed packet to pm-plan-batch, an exact approved packet to pm-run-batch and closure to pm-handoff. Orient such a target at entry with `orient PROJECT` and close with `orient PROJECT --check`, both through the launcher `${CLAUDE_PLUGIN_ROOT}/bin/orient` (bare `orient` only when `command -v orient` resolves to that launcher). Ordinary short work stays bounded; a project that does not adopt the profile keeps the route above.

Consequential-open duty: classify actual stakes and routine/settled/forced exclusions, then load full `prompting/brainstorm.md` at the actual adapter-resolved neutral root when its mandatory trigger applies. The authorized root obtains the independent decision packet before dependent readiness; an inner PM/Architect requests it and never delegates. Link actual proposal/HOLD/evaluation/authorized-decision evidence in existing plan/task/DEC homes. Missing required independence leaves that choice held/unproven; unrelated authorized work continues.
