---
id: repository.entry
title: Methodology repository maintainer entry
status: draft
---

# Methodology repository maintainer entry

This entry applies when maintaining this repository. Shared PM subjects describe consumer projects; these repository-local instructions are not a harness role assignment.

<!-- anchor: repository.entry.current -->

## Maintainer startup

This complete Git repository and its `origin` are the canonical source for ongoing framework maintenance. Work from a permanent checkout of that origin. The preparation-time records imported in the initial release are historical context; the current records linked below govern the next action. Earlier preparation checkouts and private audit packets are archives, not a parallel development source.

At session start, read this entry and the four current records below, then inspect `git status --short`, the current branch and the relevant code or owning subjects. Continue the actual approved task rather than restarting the project. Share changes through Git branches and PRs; recover decisions, checks and next actions from these records rather than one agent's chat memory.

Before creating a commit, inspect repository-local identity with `git config --local --get user.name` and `git config --local --get user.email`. The owner's permanent checkout has an explicitly configured identity; a new clone needs its own owner-approved local identity. A remote owner, an active CLI login and a commit author are separate settings. Do not infer one from another, change global identity or place credentials in tracked source. Select authenticated access for the intended origin without exposing tokens.

Keep the stable package checkout clean on `main`, as [Local use](README.md#local-use) requires. Develop in an isolated worktree on a scoped branch; one writer owns each edited path. Submit the tested result through a PR and keep result approval separate from implementation approval, honoring any matching approval already given. Record real validation and limits, update the four current records and rewrite HANDOFF at closure.

Use the complete co-located package under `implementations/codex/` or `implementations/claude/` through its documented explicit-source/in-place profile. Resolve the neutral owners from this checkout. Follow the host's actual capabilities and project instructions; report unsupported loading or missing prerequisites instead of silently using a different installed copy. This entry neither installs a plugin nor changes user-level harness configuration.

## Current project records

- **REPO-101** MUST: Read [HANDOFF](examples/pm-project/HANDOFF.md), [VISION](examples/pm-project/VISION.md), [ROADMAP](examples/pm-project/ROADMAP.md) and [TASKS](examples/pm-project/TASKS.md), then only relevant links. They are the sole current maintainer state; preparation records under examples/pm-integration are historical.
- **REPO-102** MUST: Follow [FORMAT](FORMAT.md) for neutral subjects. Actual maintainer state lives under its existing examples exception. Do not add arbitrary root formatting exemptions; the typed implementation-package boundary is defined only by FORMAT and retains independent package validation and complete public coverage. Do not duplicate current documents or treat fictional examples as actual project evidence.

<!-- anchor: repository.entry.authority -->

## Authority and closure

- **REPO-103** MUST: Preserve the actual task grant, foreign/uncommitted work and held/failed history. One writer owns each path. Integration-for-review/local commit is authorized; main merge, publication, external installation and deferred code-layer continuation require their matching owner decisions.
- **REPO-104** MUST: Preserve established software roles, flow/gates, schema/registries and existing execution checks unless an exact task authorizes changing them. At closure retain evidence/limits, reconcile current state and rewrite HANDOFF. Use relevant [experience](process/learning.md), not a mandatory whole-history read.

<!-- anchor: repository.entry.decisions -->

## Important open decisions

- **REPO-105** MUST: Classify actual consequential stakes and load the full [brainstorm owner](prompting/brainstorm.md#prompting.brainstorm.consequential) before an important open product/architecture decision. The authorized root obtains the independent packet; inner roles request it. Record routine/settled/forced exclusions with their reason and link actual decision evidence from existing project homes. Missing required independence holds that choice; this pointer grants no new role, action or installation.
