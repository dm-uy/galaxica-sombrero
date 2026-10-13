---
name: prompting-agent-design
description: "Use when designing a bounded, tool-using agent loop (phases, tools, state, approvals, failure routes, costs). Running a ready workflow of this kind uses feature-dev; this skill only designs it."
---

# prompting-agent-design

Design an agent loop whose authority, state and stopping rules are explicit before it runs.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../prompting/agent-prompt-design.md`
- `${CLAUDE_PLUGIN_ROOT}/../../runtime/capabilities.md`
- `${CLAUDE_PLUGIN_ROOT}/../../runtime/adapters.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/delegation.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Decide first whether the task is a bounded action or a real loop; a single action needs no orchestrator.
2. For a loop define the phases, inputs and results of each, the role, tool and action authority, approval boundaries, state and its single writer, failure routes and finite costs and retries. Tools perform exact search, arithmetic and execution; the model interprets evidence.
3. Give each agent the smallest sufficient context, keep Code separate from independent QA, and set the model tier by the hardest step.
4. Bind the design to real Claude mechanisms only after discovering them: typed subagents through the Agent tool, hooks, the run-state helper, and the Workflow only where it is actually available and the owner opted in. Reuse the existing feature-dev flow rather than invent another orchestrator.
5. Write prompt-injection defenses as DRAFT. They become evidence only after a separately authorized evaluation against the target; do not assume tool availability or resilience.

Limits:
- A design is not a run and grants no authority to execute it.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
