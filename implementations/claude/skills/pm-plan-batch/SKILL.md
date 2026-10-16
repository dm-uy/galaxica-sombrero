---
name: pm-plan-batch
description: "Owner-invoked command: propose the next task or bounded batch in TASKS from the route's current step, the requirements and the open questions, and pass the batch gate through a structured question."
argument-hint: "[route step or focus]"
disable-model-invocation: true
---

# pm-plan-batch

Turn the route's next step into a reviewable packet of tasks. Drafting never activates it: only the owner's approval does.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/batch.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/lifecycle.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/decisions.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/specification.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/../../roles/pm.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Orient, then read the route focus, the requirements and decisions that bear on it, the open questions, and the previous packet with its results. If direction, an authoritative input or an owner choice is missing, describe that blocker before scheduling anything that depends on it.
2. Cut the work into tasks. Each has a goal or route id, an actual grant or pending decision, a deliverable, allowed artifacts and writer, inputs, observable finish conditions, exceptional stops, state and dependencies, result evidence and next disposition. Classify by the changed surface: S is a small change with no contract change, M needs reconnaissance, a specification and the full cycle, L is cut into M tasks first. An M task names its specification at a stable project path with near-top Done when and Stop and ask when conditions; drafting it activates no Architect. Where the project numbers decisions, a task that will need a binding decision records `Reserves: DEC-NNN`; the parent allocates numbers in order from the highest recorded or reserved one, and tasks never take numbers on their own.
3. Partition by prerequisites and shared write surfaces. Put a go/no-go question in its own task and plan the work that depends on its answer for a later packet. Size the packet to a credible horizon.
4. Carry unfinished rows from the previous packet explicitly, with their reasons and return conditions, before replacing it. Keep pending and ineligible tasks held or blocked.
5. Present the outcome, the tasks and finish lines, what is excluded and the owner-only choices, and ask once with AskUserQuestion: approve the batch, rebuild it (say what to change), or cancel. Record the answer verbatim with who, when, the mechanism and the exact packet identity in TASKS and the notes; until then the packet stays proposed.
6. Commit only if that was granted, and then only the named files.

Limits:
- Approval of a batch grants no result decision and never enlarges scope; it is not inferred from silence, a default or a filled-in form.
- The packet custodian alone edits TASKS; every other contributor reports to it.
- A missing, stub or unread required owner is BLOCKED; no merge, publication or installation follows, and an inner role never delegates or commits.
