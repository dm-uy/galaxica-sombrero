---
name: devplan-protocol
description: "План разработки для утверждённого среза: «напиши план разработки (DevelopmentPlan)», «план реализации по утверждённому ТЗ». Use when an assigned Architect writes a DevelopmentPlan for an approved slice: ordered sections 1 to 6, a code graph, data flow, measurable acceptance criteria, runtime commands and the visual-gate check."
---

# devplan-protocol

Write a plan another agent can implement and verify without the chat history.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/dev-plan.md`
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/graph.md`
- `${CLAUDE_PLUGIN_ROOT}/../../code/navigation.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Act only as the assigned Architect, at the plan path the assignment dictates. Read the original approved specification and RECON in full first.
2. Stamp the neutral METHODOLOGY_VERSION (3.0.2) and the identities in play: package methodology-claude 2.1.1, the adapter and the specification.
3. Write sections 1 to 6 in order, each with purpose, rationale and verification. Cut independently implementable slices with their tests, record MAY EDIT and DO NOT TOUCH, attach each acceptance threshold to its criterion, and name the delivery sinks and the exact Runtime Commands. Preserve all four applicable patterns: Layer Isolation, Plugin API plus Direct Integration, Backend Tests plus LDD, Headless UI Testing.
4. Run the visual gate when the plan has three or more new or changed component definitions and is not tests-only: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/devplan-protocol/scripts/visual_gate_lint.py" PLAN --spec SPEC`. Record the command, output, exit code and recognized node count. Supported suffixes are `_py`, `_ts`, `_tsx`, `_js`, `_jsx`, `_CLASS`, `_FUNC`, `_METHOD`; zero recognized nodes exits 2, findings exit 1, a clean supported result exits 0.
5. Read all unsupported or mixed carriers manually and disclose the extent; never rename nodes to manufacture coverage. The linter is finite, so also inspect diagram, XML and data-flow fidelity yourself.
6. Re-read the written plan against the specification before returning, and return it through the architect carrier.

Limits:
- A required zero-node, missing or failing visual result refuses Code.
- A command, template or hash never certifies a ready plan; the root checks the plan semantically.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.

Consequential-open duty: classify actual stakes and routine/settled/forced exclusions, then load full `prompting/brainstorm.md` at the actual adapter-resolved neutral root when its mandatory trigger applies. The authorized root obtains the independent decision packet before dependent readiness; an inner PM/Architect requests it and never delegates. Link actual proposal/HOLD/evaluation/authorized-decision evidence in existing plan/task/DEC homes. Missing required independence leaves that choice held/unproven; unrelated authorized work continues.
