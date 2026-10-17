---
name: roadmap
description: "Use to create, inspect or update a project route (ROADMAP) with stable checkpoint identities, a focus marker and a matching dependency diagram."
---

# roadmap

Keep one actual route per project, with ids that never change meaning.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/lifecycle.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/session.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/templates/ROADMAP.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Read the route at its existing home and keep its ids, marker convention, checkboxes and the dependency Mermaid diagram consistent with each other. Create a new route only from the ROADMAP template and only when none exists.
2. Derive tracks and checkpoints from the outcome (session-to-week scale); task-level todos belong in TASKS, not here. A pure status question is read-only: compare the route with the artifacts and write nothing.
3. Close a checkpoint only when its own finish criterion is achieved, and distinguish implemented from integrated. Explain any non-obvious ordering, deferral and re-open condition, and keep pointers to the backlog and snapshot records separate.
4. Replan only inside the granted direction. A meaningful change of direction needs a real owner decision, asked with AskUserQuestion and recorded where the project keeps decisions.

Limits:
- Status is read against artifacts; a checkbox alone is not evidence.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.

Consumer PM profile: for an explicitly adopted `methodology-consumer-pm/1.0.0` target, read `${CLAUDE_PLUGIN_ROOT}/references/consumer-pm-profile.md` and the Codex carrier it names; apply its actual homes, stable ids, the single `<<< WE ARE HERE` marker, the matching Mermaid diagram, the inclusive budgets and the held reasons. `orient PROJECT --check` through the launcher `${CLAUDE_PLUGIN_ROOT}/bin/orient` reports the structural route rows. Existing project declarations win.
