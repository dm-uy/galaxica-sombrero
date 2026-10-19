---
name: prompting-decompose
description: "Декомпозиция сложной задачи на фазы: «разбей задачу на фазы», «декомпозируй сложную задачу», «фазы с входами, проверками и передачей». Use when a complex, multi-mode task or prompt needs explicit phases with inputs, effects, checks and handoffs (inspect, design, implement, verify). Not for a simple answer."
---

# prompting-decompose

Cut a complex task at the points where the mode of work really changes, and define what crosses each cut.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../prompting/decomposition.md`
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/dev-plan.md`
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/graph.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/delegation.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Split where the work actually changes between inspecting, designing, implementing and verifying. For each phase state its current inputs, allowed effects, output, check and failure route. Planning yields a plan; execution yields real artifacts.
2. Align the structural graph with the ordered flow and the real source, so that the diagram, the data flow and the phases tell the same story.
3. Parallelize only independent, authorized work with one writer per path. With subagents, give each a self-contained assignment (absolute paths, granted write paths, the output contract) and an explicit `model`.
4. Persist completed state and a self-contained handoff for the next phase instead of relying on chat. Ask for a concise rationale and evidence, never for hidden reasoning.

Limits:
- A phase boundary is not an approval; gates remain with the owner.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
