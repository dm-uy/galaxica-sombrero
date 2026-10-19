# Current: GRACE-Q2 minimal QA evidence package (local candidate)

Owner approved [GRACE-Q2](notes/grace-qa-evidence-minimal.md): clarify existing QA evidence, LDD outcome correlation and an agent-operable test guide in neutral owners, then synchronize Codex/Claude/DSH. No new roles, experiments, contract/test reduction or installation. Root owns source/current records in isolated `codex/qa-evidence-minimal`, base00c16ae; canonical main stays clean. Implemented and locally checked: neutral/Codex/DSH source3.0.2 and Claude source2.1.1. Independent document review found no unresolved defect after restoring three historical comments. The local candidate is complete; its next action is the separate integration decision. Checks and their failed-attempt history/limits are in the linked note. No installed update or demonstrated testing-quality improvement is claimed. M37/M38 and all waiting items below remain unchanged.

# Retained canonical checkpoint: M37 and M38 merged

## Owner decisions

Settled:

- **M37 — Claude package actualization.** Merged into `origin/main` through PR11 (merge `380dd00`, 2026-10-17). The owner's verbatim answers are in the [M37 record](notes/m37-claude-parity.md):
  - the M37 scope;
  - keeping the name `methodology-claude`;
  - lifting the M30 Claude deferral;
  - approval of the C2-port specification with mechanism H;
  - accepting the result, with AC5 met by the absolute-path launcher call;
  - push plus PR, merged after the owner's review;
  - the `.methodology/` ignore rule.
- **M38 — DSH native implementation package.** The owner approved the full Codex-twin package, then its `main` merge and the live installation («надо смержить и поставить в профиль этот бандл»), then the rebase onto M37. Merged into `origin/main` through PR10 (merge `1ff633c`, 2026-10-19). [Result, evidence and limits](notes/m38-dsh-package.md).
- **In-house plugins disabled (2026-10-19).** The owner: «Давай придушим вот эти вот старые плагины, потому что, по идее, в новом все уже есть, и надо работать в рамках него.» `product-methodology` and `prompting-methodology` are disabled at user scope, ahead of the consumer migrations. Details, losses and rollback are in the [M37 record](notes/m37-claude-parity.md#in-house-plugin-retirement-2026-10-19).
- **Sandbox check (2026-10-19).** At the owner's request, six live probes in a Claude-only copy of the tasklight sandbox: five passed, and a Russian fact-check request missed `prompting-verify`. A parity check listed seven losses. [Results, losses and name changes](notes/m37-claude-parity.md#sandbox-check-after-the-retirement-2026-10-19).

Waiting for the owner:

1. **Consumer migrations (M37-T7).** Each of the five consumer projects needs its own grant to adopt `methodology-consumer-pm/1.0.0`. The in-house plugins are already disabled, so unmigrated projects run on methodology-claude alone. Expect C2 `orient` to refuse their current profile until they migrate.
2. **DSH probe 3 (M38-T4).** The full Bootstrap-to-Finalize run on DSH needs a matching target and scope; see [M38-RUN-01](notes/m38-run-01.md).
3. **Next bounded framework task.** Choose among the remaining route below.
4. **Losses after the plugin retirement.** Decide whether to port `run_review.py` and `pm-ingest-candidates` or drop them and the model-policy rule's citation, whether to restore a typed brainstorm generator, and whether to extend the neutral quotation rule with the research-wide ellipsis ban and the verifier's exact-string step. Russian trigger phrases are in PR15, which awaits your review and merge.

No packaged release of Claude 2.1.0 or DSH 3.0.1 has been taken; it remains a separate decision.

## Current state

- **Main** includes M37 and M38. Source versions: neutral 3.0.1, Codex 3.0.1, Claude 2.1.0, DSH 3.0.1.
- **Claude package.** 64 members: three launchers that reference the Codex C2 helpers in place, a by-reference consumer PM carrier, routing in nine skills and the searcher, and a root tripwire over 18 Codex files. It loads in place from the canonical checkout. On 2026-10-19, after the M38 merge, the maintainer session that synchronized these records observed the SessionStart hook there report methodology-claude 2.1.0 bound to neutral 3.0.1.
- **DSH package.** Adapter over all 71 neutral files, 27 skill carriers, six role carriers, the six shared helpers and a bundle that mounts the package's own skill root. It is installed into the `web` and `desktop` profiles from the canonical checkout. Live discovery, on-demand loading of `pm` and a bounded smoke with independent verification were shown before the rebase. No full flow and no assigned flow QA/Review ran. The package is byte-identical to that tip, but the live profiles were not re-probed after the merge.
- **In-house plugins.** Disabled at user scope on 2026-10-19 and still installed. A fresh headless session in the canonical checkout listed methodology-claude as the only non-built-in plugin, with its six roles and one SessionStart hook. Sessions started before the disable keep the old plugins until they restart; whether a plugin reload also applies the change was not measured.
- **Claude sandbox.** `011-claude-tasklight` in the owner's sandbox folder is a Claude-only copy of the tasklight sandbox; the DSH sandbox stays untouched. The consumer profile is adopted there additively and uncommitted; `orient --check` fails nine rows on its legacy records.
- **Checks on the merged candidates (Python 3.12).**
  - M37, final candidate before the merge: root 603, Claude 545 and Codex 146 tests passed.
  - M38 after the rebase: root 605, DSH 146 and focused C1 6 tests passed; DSH adapter conformance passed.
  - `bin/conform self` was not run for the M38 rebase, because its private deny list was not supplied.
- **Evidence.** Raw M37 run evidence (about 1 GB) lives in the owner's private evidence directory outside this repository.

## Next action

Read, in order: root AGENTS, this HANDOFF, VISION, ROADMAP, [TASKS](TASKS.md), then only the relevant notes: the [M37 record](notes/m37-claude-parity.md) and the [M38 result](notes/m38-dsh-package.md).

The owner selected GRACE-Q2 above. The four retained waiting items remain separate; do not reopen their scope. Do not edit consumer projects, DSH profiles or user settings without their own grant.

## Retained traps

- **Bare launcher names.** With `product-methodology` disabled, a fresh session resolves `codemap`, `markup-migrate` and `orient` to methodology-claude's `bin/`; the 2026-10-19 sandbox probe measured this with `command -v`. A session started before the disable, or one where the plugin is re-enabled, may still resolve `codemap` and `markup-migrate` to the old `bin/`; the old plugin never had an `orient` launcher. The package's own routes check `command -v` first or use the absolute launcher path.
- **Capabilities without a replacement.** Seven losses are listed in the [M37 record](notes/m37-claude-parity.md#sandbox-check-after-the-retirement-2026-10-19), with the new command names. The `pm-*` skills run only on an explicit command.
- **Root suite interpreter.** Run the root suite with `/opt/homebrew/bin/python3.12`. The C1 helper pins depend on the interpreter: under Python 3.9 the AST omits empty `type_params` fields, so one pin test fails.
- **Checks in a working checkout.** Package tests, several root tests and `bin/conform adapter`/`self` count every `*.md` under the ignored `.methodology/` folder. Run final checks on a clean copy.
- **C1 helper pin.** The merged tree keeps the upstream pins; M38's Python 3.9 recalibration was dropped in the rebase. A pin cannot separate an intentional algorithm change from drift, so review any re-pin against the source delta. The DSH helper stays outside that pin loop. Details are in the [M38 result](notes/m38-dsh-package.md#root-suite-repairs-during-m38).
- **Marketplace installs.** Any marketplace install of the Claude package copies it and reports BLOCKED. Use in-place loading only.
- **DSH profiles.** The DSH GUI runs the `desktop` profile; the first installation went to `web` by mistake. Both profiles keep their previous `package.json` and `cordis.patch.yml` as `.bak-m38` for one-step rollback.
- **Probes launched from a running session.** A child `claude` inherits the parent's environment, including PATH entries of the parent's loaded plugins. Launch live probes with `env -i` and the login shell's PATH.
- **Live headless probes.** Restricting Bash to launcher-only rules can deny the commands the routes legitimately use, such as the absolute launcher path or `command -v`. Match the probe rules to the current routes before reading a failure as a product defect.
- **Run-state helper gaps.**
  - It cannot record an architect-phase response correction after the plan file exists.
  - It cannot continue a terminal run.
- **C3.** Remains exhausted, unaccepted and unmerged: terminal ESCALATED/review, Debug 4/4, no reset or fifth repair.
- **M30.** Source integrated, Debug 1/4 retained. Native Claude AC4/AC5 were observed in M37, but renewed M30 QA, Review and Finalize are still owed.
- **Remaining route.**
  1. Minimal safeguard.
  2. Bounded API/database trial.
  3. Separately scoped C4–C6.
  4. Later: frontend, Telegram and MCP.

Public source visibility and local installation do not satisfy these proofs. See [ROADMAP](ROADMAP.md) and the linked result records for history.
