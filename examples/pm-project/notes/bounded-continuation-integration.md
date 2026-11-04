# CONT-BOUND integration — 2026-11-04

The owner requested analysis of PR21/PR22 compatibility and authorized merging both if sound: «проанализируй оба ПР на наличие конфликтов между собой и если все ок то вливай». This supersedes their integration hold, not the separate installation boundary.

## Source and result

[PR22](https://github.com/dm-uy/galaxica-sombrero/pull/22) head `9c9f556e3d576dd650fa562e59ec36ae341bfc4f` merged first as `3ffc2fda93fb388f0bacf2baaa2ed61a4682166d`. [PR21](https://github.com/dm-uy/galaxica-sombrero/pull/21) head `35611098a642e873df040cc0391959e37d7d4958` then merged as `d37d884083db4eadc4e0ea1d0b21ea580eb47995`. Remote main readback matched exact tested tree `3075e8581f2ce0ffefd472fa52beaf29c4d82d05`. Merge commits preserve both histories; no squash, force push or branch deletion.

The post-common-base branch changes had disjoint paths and merged without textual conflicts. One independent compatibility reviewer found operative DSH schema/path metadata and both smoke specifications' generated-effect scope inconsistent with schema3. Root corrected DSH adapter/runtime/disposition/smoke and Codex admissions/disposition before merging; no helper algorithm changed in these corrections. The same reviewer closed both MEDIUM findings and independently verified the final checks. A remaining LOW DSH manifest stamp is corrected in this documentary closure, together with README and current records.

## Exact combined checks

On a Git-free export of the tested tree, Python3.12, bytecode/cache writes disabled and separately owned basetemps:

| Suite | Result |
|---|---|
| Root | 616 passed |
| Codex | 201 passed |
| Claude | 548 passed |
| DSH | 202 passed |

All four exited0, with no skipped tests. All three actual `bin/conform adapter` calls passed76, warned0, failed0 and not-run0. Root and all three package Doxygen builds exited0 with empty stdout/stderr. Git whitespace checks passed. The first Claude attempt failed because Node was absent from PATH; its original log is retained. The final run explicitly used the existing Node24.21.0 runtime without installation or configuration changes.

Complete final commands/results/streams and the original independent report are preserved in the ignored `.methodology/continuations/cont-bound-integration/evidence/` directory. Prior Codex, Claude and DSH private evidence remains in its original worktree homes; no worktree was archived or evidence deleted. Preserve those homes before later archival.

## Boundaries and remaining work

This is combined source-compatibility verification and owner-authorized integration. Previous package-native proofs retain their original scope; a new full native feature-dev flow on this combined tree was not run or claimed. The separate agents' recorded Claude startup and DSH/Codex continuation probes remain distinct from full model adherence. Private deny-list self-publication coverage remains unavailable; no history sanitization was requested or performed.

No plugin/profile installation or account-default change was performed in this integration task. Updating the canonical checkout advances its existing in-place Claude source to3.1.0 for new sessions; this is the disclosed consequence of the approved merge. Codex installed snapshots were not updated; the separately reported DSH snapshot installation was not repeated. Unfinished old bindings are not silently migrated.

Claude continuation parity, the retained Codex carrier wording and broader successor-accounting/in-place-update issues remain separately scoped; integration does not close them. See [tasks](../TASKS.md) and the original [Claude result](bounded-continuation-claude-compat.md#findings-for-other-owners).

## Documentary delivery boundary

The extra seven-path README/record/stamp closure is saved only in the local integration-record branch. Automatic approval review rejected a direct push of this additional commit to main: the owner grant covered merging PR21/PR22, not a separate direct default-branch publication. No workaround or indirect main write was attempted. Remote and canonical main remain at the verified PR21 merge `d37d884083db4eadc4e0ea1d0b21ea580eb47995`; a separate owner decision is needed to deliver these documentary follow-ups through a PR. Both originally requested PR merges are complete. Additional closure-only checks passed46 root format/DSH-package tests and2 DSH native-contract tests.
