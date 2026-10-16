# Current: M37 Claude package actualization

## Owner decisions

Waiting for the owner. All of this is on branch `claude/m37-claude-parity`, which is not merged and not pushed.

1. Approve, or rework, the [C2-port specification](specs/m37-claude-consumer-profile.md). Approving it selects mechanism H from the [decision packet](notes/m37-decision-c2-port/README.md) and authorizes the feature-dev run.
2. Decide how to integrate the checked patch 2.0.2: local main integration, push, or a pull request. Claude loads the main checkout in place, so a main merge changes every Claude session immediately.
3. Optional: start M30 full acceptance (renewed independent QA, whole Review, assigned Finalize). Native Claude AC4 and the Claude half of AC5 have now been observed.

Settled on 2026-10-16 (verbatim answers are in the [M37 record](notes/m37-claude-parity.md)):

- the scope;
- the name `methodology-claude` stays;
- the M30 Claude deferral is lifted;
- the in-house plugins stay until orient is ported.

## Current state

Main is unchanged at `b8696a2` (equal to origin/main): neutral 3.0.1, Codex 3.0.1, Claude 2.0.1.

The branch adds:

- Claude 2.0.2:
  - carrier parity: prompting route, RUNREV-301, lifecycle owner sets;
  - corrected install claims.
- A repair of the root-suite oracles, which M31 had left red. The root suite now passes 600 on Python 3.12.
- The live Claude M30 probe record.
- The C2-port decision packet and the draft specification.
- Synchronized current records.

Raw probe streams and the unredacted decision originals stay in the owner's private evidence directory, outside this public repository.

The owner's Claude Code still loads canonical main in place through `CLAUDE_CODE_PLUGIN_DIRS`. The in-house `product-methodology` and `prompting-methodology` plugins are still enabled beside it.

Carried forward from earlier receipts: the installed Codex snapshot `471c02f` and prompting 0.6.0. The prompting-source upstream release is still undelivered.

## Next action

Read, in order: root AGENTS, this HANDOFF, VISION, ROADMAP, [TASKS](TASKS.md), and the [M37 record](notes/m37-claude-parity.md).

- If the owner approved the specification: run M37-T6 through `/methodology-claude:feature-dev` on that exact specification.
- Otherwise: obtain the owner's decision first.

Do not edit consumer projects or user settings without their own grant.

## Retained traps

- **Root suite interpreter.** Run it with `/opt/homebrew/bin/python3.12`. Under system Python 3.9, one AST-pin test fails because the pin is tied to the interpreter; the pin is protected.
- **Re-run the root suite after any neutral-owner edit.** M31 changed `flow/phases.md` and `roles/pm.md` without doing so, and 66 root tests stayed red until M37.
- **Marketplace installs.** Any marketplace install of the Claude package (git or local directory) copies it into the plugin cache, and the binding check reports BLOCKED. Use in-place loading only.
- **Consumer migration.** C2 `orient` accepts only `methodology-consumer-pm/1.0.0`. The five consumer projects declare older in-house conventions. Each needs its own migration before the in-house plugins are disabled.
- **C3.** Unaccepted, unmerged, terminal ESCALATED/review, Debug 4/4 exhausted. No reset and no fifth repair.
- **M30.** Debug 1/4 is retained.
- **Remaining route, unchanged by M37:**
  1. minimal safeguard;
  2. bounded API/database trial;
  3. separately scoped C4–C6;
  4. later frontend, Telegram and MCP.
