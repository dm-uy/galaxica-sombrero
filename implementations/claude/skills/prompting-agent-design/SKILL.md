---
name: prompting-agent-design
description: "Use when authoring another agent's system prompt for a one-shot task or a bounded tool-using loop: the prompt, its rationale and its reproducibility contract, and for a loop also phases, tools, state, approvals, failure routes and costs. Running a ready workflow of this kind uses feature-dev; this skill only designs it."
---

# prompting-agent-design

Author another agent's prompt, and for a loop its authority, state and stopping rules, explicitly before it runs.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../prompting/agent-prompt-design.md`
- `${CLAUDE_PLUGIN_ROOT}/../../runtime/capabilities.md`
- `${CLAUDE_PLUGIN_ROOT}/../../runtime/adapters.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/delegation.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Decide first whether the task is a one-shot bounded action or a real loop; a single action needs no orchestrator.
2. Deliver all three authored artifacts for either mode: the full pasteable prompt, a decision-to-concept rationale map, and a reproducibility contract with the machine output schema, two to four measurable evaluation criteria, version and change log.
3. For either mode collect the actual container, role, goal, input and output schema, available tools, constraints, stakes and context source. Apply loop mechanics only to a loop design: define the phases, inputs and results of each, the role, tool and action authority, approval boundaries, state and its single writer, failure routes and finite costs and retries. Tools perform exact search, arithmetic and execution; the model interprets evidence.
4. Give each agent the smallest sufficient context, keep Code separate from independent QA, and set the model tier by the hardest step.
5. Bind the design to real Claude mechanisms only after discovering them: typed subagents through the Agent tool, hooks, the run-state helper, and the Workflow only where it is actually available and the owner opted in. Reuse the existing feature-dev flow rather than invent another orchestrator.
6. For adversarial stakes keep at least two differently phrased injection inputs and a synthetic-secret probe separate from the production prompt. They and the prompt's injection defenses stay DRAFT/NOT_RUN until a separately authorized evaluation against the target passes; authoring authorizes no tools or evaluation, and tool availability or resilience is not assumed.

Limits:
- A design is not a run and grants no authority to execute it.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
