---
name: greenfield-bootstrap
description: "Use for a genuinely new product after a measured inventory shows nothing to build on: establish audience, first falsifiable value, stack and MVP, write the greenfield specification and seed the records. Missing records alone do not make a project greenfield."
---

# greenfield-bootstrap

Turn a new product idea into a measured greenfield specification and the five durable records, then route it to the gate.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/bootstrap.md`
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/spec-greenfield.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/specification.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Inventory first: hidden instructions (CLAUDE.md, AGENTS.md), briefs, existing source and Git state, and settled choices. Existing executable code is existing code, not greenfield, even when the records are missing.
2. Establish the audience, one falsifiable first value with its observable pass condition, the arrival criterion, the constraints, the stack with its rationale, the MVP boundary and the authorized transport. Recover answers already given before asking; ask the owner only the genuine gaps, with AskUserQuestion.
3. Run reconnaissance through spec-recon and keep fixtures distinct from live data.
4. Author the full greenfield specification and, under a matching preparation grant, the five durable records at their granted homes through pm-bootstrap, preserving existing Git and ignore rules.
5. Route the specification to the gate through hitl-gates, then to feature-dev.

Limits:
- No auth, billing, environment, launcher or dependency is created unless the approved task needs it.
- Preparation grants no technical authorship: architecture is the Architect's, implementation the coder's.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
