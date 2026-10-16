---
name: pm-run-batch
description: "Owner-invoked command: work through the approved batch in TASKS autonomously with typed role subagents, stop only at the listed stop points, and finish with the result decision. Invoking it is the owner's opt-in to run the feature-dev Workflow for the batch's M tasks."
argument-hint: "[batch id]"
disable-model-invocation: true
---

# pm-run-batch

Execute an approved packet task by task. Routine steps inside the grant need no repeated approval; consequential ungranted forks and the result decision stay with the owner.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/batch.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/phases.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/delegation.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/run-state.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/code-review.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/safety.md`
- `${CLAUDE_PLUGIN_ROOT}/../../policies/models.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Orient. Verify that the batch gate record matches the packet and its scope; otherwise stop and use pm-plan-batch. Activate the permitted tasks and rewrite the HANDOFF baton in the same state update.
2. Take unfinished active or review work before opening the next eligible task. Give each assignee its full contract: goal, inputs, allowed paths, finish line, checks, stops and the evidence to return. Pass `model` explicitly on every delegation, chosen by the task's hardest step (haiku mechanical, sonnet routine, opus judgment), and note in each task's evidence which model ran which part. Record `git status --porcelain -uall` before and after each dispatch; report writes outside the granted paths without reverting them.
3. S task: a `methodology-claude:coder` implements the change inside the exact allowed paths with its tests; a separate `methodology-claude:qa` verifies it.
4. M task: reconnaissance through spec-recon, then a specification inside the approved scope (one outside it stops the run for renewed authorization), then the feature-dev cycle. This invocation is the opt-in for `/methodology-claude:feature-dev-workflow`; if the Workflow is unavailable follow the manual route of the feature-dev skill with run state. An L task is cut into M tasks before it runs.
5. Verify each result yourself: separate author claims from independent review, list every skipped, deferred or blocked check with its reason, and run what the cycle did not run before calling the task done. A SUCCESS covers only what was checked.
6. Record start, observations, blocks and finish in TASKS as they happen; route a binding decision to the decision home. At a stop condition record the reason and the return condition, and continue independent granted tasks. A non-gate question to the owner goes out while other tasks keep running, and is not asked if the answer is already recorded.
7. At the end present blockers first, then changes and evidence, then findings and limits. Prepare the concrete result, run the live probe, then ask once with AskUserQuestion: merge, rework with a concrete Bug Report, or reject. Archiving the packet, cleanup and commits are consequential effects: before each, name its actual targets and the matching grant, and keep any not granted for the owner. Archive the packet with all task states. Before cleaning a branch, worktree or other resource, verify that it belongs to this run, inspect its ignored and uncommitted content, preserve nonregenerable state and hold the applicable integration or cleanup authority; a clean status alone is insufficient. Then close with pm-handoff.

Limits:
- No merge, push, publication or deployment without the separate result decision; rejection grants no destructive rollback.
- Inner roles never delegate or commit; the root alone integrates.
- A missing, stub or unread required owner is BLOCKED; no installation follows from this command.
