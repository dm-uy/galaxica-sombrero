# Current: M31 merged, released and installed

## Completed

Owner-authorized lightweight PM change merged through PR8 at3dd4d626. Release v3.0.0 is published in the private repository with the complete co-located archive and SHA256SUMS. Versions: neutral3.0.0 / Codex3.0.0 / Claude2.0.0. [Decision and actual installation receipt](notes/pm-lightweight-direction.md).

Codex CLI installed methodology-codex from a complete snapshot of3dd4d626. Its actual app-server discovers all27 enabled skills, including methodology-codex:pm and methodology-codex:feature-dev at the nested package paths. All tracked installed bytes match that release commit. Old personal codex-pm1.0 is disabled and retained. Claude global settings now point to the canonical main package; strict manifest validation and actual SessionStart binding pass against neutral3.0.0. Prior settings and global entry were backed up for rollback. The global fallback entry points at canonical source. Receipt-only maintainer changes after the release do not change the frozen installed snapshot.

## Next action

Use a fresh session to consume the new discovery catalog. Continue with a separately bounded single-stream API/database consumer trial when selected; observe actual friction before adding process. QA belongs to new features/substantial bug fixes, while docs and small corrections use relevant local checks. Synchronize only affected agent state on material changes, grouped progress and before planned compaction/handoff.

## Retained boundaries

M30 live native Claude behavioral acceptance remains explicitly deferred; installation and binding checks do not close it. C3 remains exhausted/unaccepted and unmerged; no continuation or counter reset. C4–C6 full proof remains separately scoped. No public visibility change, live Claude model run, full feature-dev or new QA ledger was performed. Original failure/held history and foreign archival work remain intact. Canonical main is the development home; cached Codex snapshots require reinstallation after accepted releases.
