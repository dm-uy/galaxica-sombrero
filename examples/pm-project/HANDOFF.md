# Current: CONT-BOUND Claude compatibility checked locally; DSH and owner result pending

Owner, 2026-11-04: «Сначала совместимость», then «Да, поправь здесь» for the stale Codex stamps. Claude 3.1.0 binds neutral 4.1.0 for ordinary operation on `claude/cont-bound-compat`, based on Codex candidate `a3ecb5c`. No continuation port. [Result, evidence and limits](notes/bounded-continuation-claude-compat.md), [tasks](TASKS.md#cont-bound--bounded-continuation-and-earlier-verification).

## Owner decisions

The concrete result of this candidate and of the Codex candidate beneath it; merging this branch also merges Codex 5.0. Merge, push and installation are not granted. Assign a DSH agent for its first bounded packet. Porting continuation to Claude is a separate choice.

## Verified result and next action

On `985795b`: Claude 548 passed, root 616 passed, Codex 201 passed, zero skips, three maps silent. The live native session, on `eba2905`, bound 3.1.0 to 4.1.0, ran `init` and `show` and dispatched a role. One independent reviewer ran three rounds with no blocker; its last two remarks were applied without a further round. The stale Codex stamps are corrected and guarded in both package suites; a second reviewer found one blocker in the first guard, approved its correction and rechecked the record's figures against their logs; its last wording remarks were applied without a further round. The two root failures the Codex checkpoint below retained are resolved on this branch: the Claude release bridge passes with its pins unchanged, and the base markup defect in `test_recon_decision_checkpoint.py`, also red on main at `388c944`, is fixed with no logic change.

Still blocking shared integration: DSH fails 83 of 146 on `neutral version mismatch`; exact combined common/sibling/native validation. Claude 3.1.0 must enter main together with neutral 4.1.0, because the plugin loads in place from main and either one alone blocks every Claude session.

## Storage

Worktree `.claude/worktrees/cont-bound-compat`; main stays clean. Private evidence is in that worktree's ignored `.methodology/continuations/cont-bound-claude-compat/evidence/`: preserve it before archiving. In this environment the shell's working directory can reset between calls, so use absolute paths; one run copied main instead of the candidate that way, as the result note records.

# Preceding checkpoint: CONT-BOUND Codex checked locally; rollout held

Owner approved the specification and lighter procedure on 2026-11-04: short plan, root implementation/checks, one independent cumulative reviewer. Codex source5.0 / neutral4.1 / schema3 is complete and checked in codex/continuation-recon. [Result and evidence](notes/bounded-continuation-result.md), [final independent judgment](notes/bounded-continuation-review-final.md), [short plan](plans/bounded-continuation.md), [actual owner approval](specs/bounded-continuation.md#owner-implementation-and-procedure-decision--2026-11-04).

## Verified result and next action

All F1–F6 are closed by the same independent reviewer; original BUG_REPORT/delta remain preserved. Exact Git-free check-05/exposed commands: Codex200 passed; root614 passed / same2 failed, zero skipped. Both maps build with silent streams; substantive source/location associations431 root /263 Codex. Real3.2+parent import retains aggregate4/native0; actual owned native worker follows persisted/readback5/5 before marker-only dispatch, canonical closure and exhaustion refusal. Actual archived4.0 native terminal uses remaining allowance1/4 without new grant or worker dispatch. Unknown host USD remains null. No Jeni/product execution.

Next: owner considers the concrete isolated result. [Updated Claude/DSH agent instructions](notes/bounded-continuation-transfer-briefs.md) name actual helper/caller/contracts and ordinary compatibility first. Shared main integration is held until their separately authorized accepted compatibility contributions, the independently reproduced out-of-scope baseline test_recon_decision_checkpoint.py markup defect and exact combined common/sibling/native checks are resolved. These two known root failures are retained, never skipped/PASS. Merge, push, installation/profile changes and Jeni continuation are not authorized here. No automatic full-flow role sequence is needed to repeat this completed task.

## Storage and continuation

Only root wrote repository source; native inert worker/reviewer writes stayed within named owned temporary grants, with status/hash checks and behavioral (not hard sandbox) limits. Scope includes the disclosed exact norm-count selectors test_format/test_report1250→1254, independently accepted as a consequence of the four approved additions; no unrelated test algorithms or sibling package bytes changed. Canonical main stays clean; local branch commit is authorized under REPO-103.

Complete private source/maps/streams/probes/original reviews are in ignored `.methodology/continuations/cont-bound-implementation/evidence/` archives and index. Preserve them before worktree archive. Exact earlier raw brief/completeness report remain under ignored cont-bound-docs. Public reviews are labeled local-path projections with original hashes. Full private deny-list publication proof remains unavailable; no release/publish action is claimed.

## Historical preparation handoff

The following is dated preparation history. Its pending-approval and future full-flow directions are superseded by the authentic owner approval and lighter procedure above; retain original reasoning, traps and prior unrelated project obligations.

# Current: CONT-BOUND specification checked; owner review pending

## Owner decisions

Review the concrete [draft specification](specs/bounded-continuation.md). The owner approved preparation and ONE named independent packet, not the unseen schema3 design, implementation, source integration or installation. No code starts from this handoff. Preserve the already settled Codex-only executable scope and external Claude/DSH agents; do not re-ask launch permission.

## Current checked result

Two fresh independent generators, saved unranked HOLD and distinct evaluation are complete; [originals, evaluation and root proposed drafting choice](notes/bounded-continuation-decision/decision.md). Root proposes A: one schema3 operational authority, original historical schema2/parent reconciliation, closed immutable run artifacts and conservative reserved-entry recovery. Native5.0/neutral4.1/rolewire2.0 are proposed separate version domains, not delivered versions. B remains a credible recorded alternative with reopening evidence.

[Original source/document review](notes/bounded-continuation-spec-review.md) found missing neutral release consumers. Root accepted and fixed the exact identity-only scope/correspondence; [final independent delta](notes/bounded-continuation-spec-review-delta.md) says READY FOR OWNER REVIEW. Root document contracts/IDs/links, source identities, whitespace and bounded home-path/email checks passed. Software tests/builds/helper/probes/consumer execution and full private deny-list publication scan were not performed or claimed.

[Claude/DSH transfer instructions](notes/bounded-continuation-transfer-briefs.md) distinguish required ordinary-operation compatibility from later optional continuation parity. Full common/sibling/overall Finalize and shared-neutral main integration remain held until separately authorized accepted compatibility contributions pass against the exact combined source. Do not fix their native code locally or silently repoint installed profiles.

## Storage and next action

Branch `codex/continuation-recon`; source baseline `388c94495d86a771da6fa5e8514249976dc8c8a1`, prior documentation checkpoint `5b499d2`. Current changes are root-owned project documents/evidence only, stored by named-file local commit under REPO-103; recover its exact revision from this branch. Canonical main remains clean. No source/package/version/configuration change, merge, push, installation or Jeni budget/continuation action.

Next: present the checked draft for owner review; incorporate requested changes without restarting recon or repeating settled permissions. A later matching implementation grant would activate the scoped Architect/Code/independent QA route, using a distinct read-only governing framework binding and candidate source as the plan requires. No automatic implementation is granted now.

Complete original brief and earlier completeness report with local paths remain unchanged in ignored `.methodology/continuations/cont-bound-docs/evidence/raw/`; tracked projections are labeled and retain original hashes. Preserve those private originals before any worktree archive. No subagent writes outside the assigned empty write scopes were reported.

## Current traps

- Jeni aggregate4/4 is outside native0/0; no native-only import, reset or free repair5.
- Original3.2 locks and all legacy predecessor bytes remain historical, including diagnostic refusal paths.
- Immutable terminal artifacts differ from the mutable lineage authority; no snapshot may authorize dispatch.
- Retry episodes, no-repair verification, remaining allowance and new-grant repairs retain distinct accounting/predicates; release-stamp absence does not prove nonrelease.
- Shared neutral4.1 with old sibling hard pins would break ordinary paths; compatibility evidence is required before main integration.
- Coupled neutral/root metadata guards and exact Codex AST exceptions are in the specification; never globally replace versions or merely repin algorithms.

## Previous completed delivery

RECON-DEC local merge/installed updates and subsequent owner-authorized remote delivery remain complete. [Original receipt and runtime limits](notes/spec-recon-decision-checkpoint-result.md). This task neither changes installed snapshots nor reopens those decisions.

## Relevant previous state

PM-INVOKE (Claude 2.4.0) was fast-forwarded into canonical `main` under the owner's 2026-10-28 decision, without push. Its first-fresh-session live probe is still unverified. [Original task, authority and retained probe](TASKS.md#pm-invoke--model-invocable-lifecycle-commands-claude-240-branch-in-review). The later explicit push grant covered the accumulated main delta and delivered these commits too; the original local-only decision is retained as history.

PR19 was accepted, merged and installed under its separate grant. [Receipt and limits](notes/brownfield-source-correspondence.md#merge-and-installed-version-update--2026-10-27). Its installed snapshot proof is not a new runtime efficacy result and is not changed by this documentation task. The earlier continuation and failures remain in those records; no release or installed snapshot was repackaged.

## Retained obligations and relevant traps

- GRACE-Q2 is integrated and delivered; its then-withheld installation is now superseded by the installed PR17 snapshot. [Result and history](notes/grace-qa-evidence-minimal.md). This is history, not another current-version or next-action block.
- M37 consumer migrations still need per-project grants; old in-house plugins are disabled. Retirement losses and historical launcher/PATH caveats remain at [M37](notes/m37-claude-parity.md). [M37 tasks](TASKS.md#m37--claude-package-actualization-merged-through-pr11).
- DSH full-flow probe3 needs a matching target/scope; use the desktop profile deliberately and preserve previous profile backups. [M38](notes/m38-dsh-package.md), [probe evidence](notes/m38-run-01.md).
- C3 remains terminal, unaccepted and exhausted at Debug4/4; no fifth repair or reset. [C3 result](notes/m28-c3-result.md).
- M30 source is integrated and native Claude observations exist through M37, but renewed QA/Review/Finalize and full acceptance remain owed. [M30](notes/m30-result.md), [M37](notes/m37-claude-parity.md).
- The later safeguard/API-database/C4-C6/frontend/Telegram/MCP route remains separately scoped. [ROADMAP](ROADMAP.md). No deferred code continuation is authorized by this correction.
- Use Python3.12 for interpreter-bound AST pins. Run source/package checks in a clean Git-free copy: ignored methodology Markdown can alter inventories. Genuine algorithm changes require review, never automatic re-pinning.
- Preserve known run-state limitations (architect response correction after plan creation; terminal runs cannot restart), explicit in-place versus copied loader boundaries, and missing private self-check coverage. Details remain in [M36](notes/m36-session-handoff.md), [M37](notes/m37-claude-parity.md) and [M38](notes/m38-dsh-package.md).
