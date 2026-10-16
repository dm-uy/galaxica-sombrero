# Current: M37 Claude package actualization — Claude 2.1.0 in review

## Owner decisions

Waiting for the owner:

1. **Review and merge the M37 pull request.** The PR takes branch `claude/m37-claude-parity` into main and contains:
   - Claude 2.0.2 (carrier parity);
   - Claude 2.1.0 (the C2 consumer PM profile by reference to the Codex helpers);
   - the M31 root-oracle repair;
   - the M37 records.

   Claude loads main in place, so the merge changes every Claude session at once.

2. **Choose when to migrate consumer projects (M37-T7).** Each of the five consumer projects needs its own grant to adopt `methodology-consumer-pm/1.0.0`. After that, the owner decides on disabling the in-house plugins.

Settled on 2026-10-16. Verbatim answers are in the [M37 record](notes/m37-claude-parity.md):

- the M37 scope;
- keeping the name `methodology-claude`;
- lifting the M30 Claude deferral;
- approval of the C2-port specification with mechanism H;
- accepting the result, with AC5 met by the absolute-path launcher call;
- push plus PR, merged after the owner's review;
- the `.methodology/` ignore rule.

## Current state

- **Main.** Still `b8696a2`: neutral and Codex 3.0.1, Claude 2.0.1.
- **The PR branch.**
  - Claude 2.1.0 with 64 members: three launchers, a by-reference carrier, routing in nine skills and the searcher, and a root tripwire over 18 Codex files.
  - `implementations/codex` is byte-identical to main.
- **Feature-dev run `m37-c2-20261016`.** Bootstrap, Architect, Code, QA, Review, Debug 1 of 4, renewed QA and Review, then Finalize. It ended BLOCKED on the AC5 literal-wording decision, which the owner has since accepted.
- **Checks on Python 3.12.** Root 603, Claude 545 and Codex 146 tests passed. The launcher tests pass on Python 3.9 and 3.12.
- **Evidence.** Raw run evidence (about 1 GB) lives in the owner's private evidence directory. The local `.methodology/` folder is now ignored.

## Next action

Read, in order: root AGENTS, this HANDOFF, VISION, ROADMAP, [TASKS](TASKS.md), and the [M37 record](notes/m37-claude-parity.md).

- **If the PR is merged:** verify main and the in-place binding (the SessionStart hook reports 2.1.0), then plan M37-T7 with the owner.
- **If it is not merged:** apply only the owner's review comments on the branch.

Do not edit consumer projects or user settings without their own grant.

## Retained traps

- **Bare launcher names.** While the in-house `product-methodology` plugin is enabled, the bare names `codemap`, `markup-migrate` and `orient` in a Bash session may resolve to its `bin/`. The package's own routes check `command -v` first or use the absolute launcher path.
- **Root suite interpreter.** Run the root suite with `/opt/homebrew/bin/python3.12`. Under the system Python 3.9, one AST-pin test fails because the pin depends on the interpreter.
- **Marketplace installs.** Any marketplace install of the Claude package copies it and reports BLOCKED. Use in-place loading only.
- **Live headless probes.** Restricting Bash to launcher-only rules can deny the commands the routes legitimately use, such as the absolute launcher path or `command -v`. Match the probe rules to the current routes before reading a failure as a product defect.
- **Run-state helper gaps.**
  - It cannot record an architect-phase response correction after the plan file exists.
  - It cannot continue a terminal run.
- **C3.** Remains exhausted, unaccepted and unmerged.
- **M30.** Debug 1/4 retained. Native Claude AC4/AC5 were observed in M37, but renewed M30 QA, Review and Finalize are still owed.
- **Remaining route (unchanged).**
  1. Minimal safeguard.
  2. API/database trial.
  3. Separately scoped C4–C6.
  4. Later: frontend, Telegram and MCP.
