---
id: process.safety
title: Safety
status: draft
---

# Safety

Safety connects actual authority to threatened state, conditional recovery and effect verification. It does not install a guard, snapshot tool or universal backup ritual. [Session intent](session.md#process.session.evidence), [ownership](session.md#process.session.baton), [gates](gates.md), [read-only role boundaries](../roles/_base.md#roles.base.boundaries), [QA isolation](../roles/qa.md#roles.qa.isolation) and [credentials](../policies/credentials.md) retain authority. The [constitution bundle](../concepts/principles.md#concepts.principles.binding) and [term catalog](../concepts/glossary.md#concepts.glossary.terms) supply scoped meanings.

<!-- anchor: process.safety.authority -->

## Classify the actual action

- **SAFE-101** MUST: Before consequential action identify its actual effect/targets, actor, matching authentic grant, ownership, threatened work/evidence and active permission/guard coverage. A backup, recognized guard match, silent hook, worker output or generic task grant cannot authorize a different destructive or external action.
- **SAFE-102** MUST: Require recoverability before an authorized action actually threatens work/evidence; do not impose snapshots on every read, check or ordinary edit. Missing threat coverage or required recovery proof blocks that threatening action while unrelated authorized safe work continues.

The action custodian first resolves actual target containment, links, destination, effect and one-writer ownership. Unknown or foreign state is preserved until its owner/scope is established. A dirty tree does not authorize reset, stash, discard, commit or cleanup. Existing matching owner permission prevents a duplicate request for the same settled action; changed effect, target or scope requires its missing decision. Read-only roles cannot become writers through a safety exception. Checks needing mutations follow the current authorized isolated-resource policy, never a judge-created worktree or a recursive copy retaining Git metadata.

Declare whether {{cap:role-permissions}} is a hard boundary or a behavioral policy, and whether {{cap:pre-tool-guard}} is present with actual coverage. A precise opt-in tripwire can leave unsupported tools, unknown substitutions/variables, piped targets or xargs input unrecognized and can stay silent on internal errors. Silence is no safety or consent verdict. A denial is reported, not bypassed. Do not copy another guard's regenerable-path classification into authority to delete foreign ignored work or claim complete isolation from a command prefix alone.

<!-- anchor: process.safety.recovery -->

## Preserve what the action can destroy

1. Bind the exact granted action, target/candidate and threat extent. Inventory affected tracked HEAD, index, worktree, new/untracked/ignored paths and needed metadata/configuration, including foreign populations and access limits. Use path-preserving inventories rather than whitespace splitting; preserve type, mode, symlink target and explicit absence/deletion state. Resolve Git metadata's actual home rather than assuming `.git` is a directory.
2. Before an irreversible or otherwise consequential action preserve intent under the adopted storage policy: what, where, why and how its outcome will be checked. Only if the action threatens that record/history, retain its recoverable copy outside the threatened extent in an authorized protected home. Committing intent follows actual commit authority/policy; no inner role gains Git-write permission.
3. Declare the capture/restore mechanism, exact protected sink and containment proof, confidentiality/access policy, retention and actual effects. The sink must survive the threatened operation, including resolved link containment. Capture that leaves index/worktree unchanged can still write objects, refs, stash entries or reflogs; name those effects and obtain their matching authority before capture. Do not call it wholly read-only or authorize history export merely to make a bundle.
4. Account for every actually threatened state class: recoverable HEAD/baseline; exact index entries/stages/modes; staged-new bytes; staged plus further unstaged bytes as distinct versions; unstaged edits; staged/unstaged deletions and absent paths; untracked and ignored content; necessary configuration/metadata, directory/file/link types and link destinations. State each class's method, identity and uncovered limits. A HEAD/history bundle alone cannot cover uncommitted/index state. An untracked-only threat remains real even when tracked content equals HEAD.
5. Verify restore feasibility before relying on capture. Use only separately authorized owned disposable resources and an independent comparison over the relevant promised population. Compare restored full contents and index identity, exact path inventory, types/modes/link targets, tracked/untracked/ignored classifications and deletion/absence states against capture; preserve spaced names and links without following unintended targets. A file's existence, member count or successful archive command is insufficient. Never reset the actual target or another session's tree as a drill.
6. Record the actual independent verification evidence, capture/fixture/input identities, commands/results, differences and access/coverage limits. If a required class cannot be protected or the mechanism/proof is unavailable, withhold the threatening action and route the specific missing coverage/authority to its owner. Partial capture stays partial; a fictional worked case is no restore receipt.
7. Recheck action scope, target freshness, sink access and coverage before the granted act. Changed candidate/threat population invalidates affected recovery evidence. Execute only the granted operation; verify the actual target effect through the recorded method and retain its outcome and limits. Cleanup affects only resources created by this run and only under its grant.

- **SAFE-201** MUST: Keep protected recovery outside the actual threatened extent with declared privacy/access limits and coverage of every actually threatened state class, including index and untracked/ignored content. Sensitive preservation supplies no permission to discover credentials, expose payloads or export all history.
- **SAFE-202** MUST: Declare and authorize the capture mechanism's real metadata effects separately; index/worktree preservation is not proof that refs/objects/reflogs are unchanged.
- **SAFE-203** MUST: Establish promised restore coverage by actual independently checked content/index/path/type/link/mode/deletion comparisons in authorized owned disposable resources. Snapshot existence, HEAD-only coverage, whitespace-losing inventories or existence-only restoration cannot prove complete recoverability.

Private payloads stay in the authorized protected sink; public reports use logical pointers and safe metadata. Credential values, prefixes, lengths and reversible fingerprints are not report evidence. If required private bytes cannot lawfully be captured, declare that gap and block only the operation relying on them. This procedure does not import a donor stash/tar implementation, create a snapshot capability, prescribe an automatic history export or repair the donor. Any future mechanism must disclose unsafe archive-member/type/link handling and actual Git metadata placement rather than infer fidelity from its header.

<!-- anchor: process.safety.outcomes -->

## Unknown effects and stop routing

- **SAFE-301** MUST: Treat consequential outcomes as observed success, observed failure or unknown; timeout/abort does not establish delivery or absence. Inspect retained intent and actual destination/effect before replay. If authority or evidence cannot settle an unknown outcome, retain it and route the required owner decision rather than repeat blindly.

A completed effect observed after interruption may avoid duplicate action only with authentic current identity and recovery checks. A known failed effect follows the existing failure route; an unknown one cannot be reclassified as failure to justify retry. Preserve denied commands, attempted workarounds, partial capture/restore and all prior failed evidence. Safety assessment does not clear terminal state, reset cumulative allowances or supply merge/publication consent. The parent uses the existing [terminal and continuation contracts](../flow/run-state.md#flow.run-state.terminal).

<!-- anchor: process.safety.form -->

## Reusable action and recovery worksheet

This complete prose form belongs in the existing authorized intent/evidence home; it adds no engine or state schema. Repeat state rows for all threatened populations.

```text
ACTION SAFETY
Actor / action / effect targets / current artifact identity:
Authentic grant: human action/artifact/scope reference, matching authority and reserved decisions:
Ownership: one writer, owned/foreign/unknown state, target containment/link resolution:
Threat: work/evidence/config/metadata affected, reason recovery applies or genuine no-threat profile:
Permissions/guard: hard or behavioral layer, active coverage, denied/unsupported/error limits:
Intent: what/where/why/check, storage authority/policy, protected outside copy if itself threatened:
Capture mechanism/sink: authorized location, containment, confidentiality/access, effects on Git metadata:
State coverage row: class/path inventory, HEAD/index/worktree versions, type/mode/link/absence, method and limit:
Restore verification: independently owned disposable resource, separate grant, input/capture identity:
Comparison: full bytes, index entries/stages/modes, paths/classifications/types/links/deletions; actual differences:
Evidence: actual commands/cwd/streams/exits, safe private pointers, read/access limitations:
Disposition: eligible exact act or blocked coverage/authority, owner resolver and unrelated safe continuation:
Effect: actual destination observation, success/failure/unknown, investigation/replay decision and limits:
Retention/cleanup: run-created resources only, actual authority, retained failures and recheck trigger:
```

<!-- anchor: process.safety.cases -->

## Fictional worked cases

All Willow actions, fixtures, grants and receipts below are invented instructional inputs. No recovery, deletion, capture or enforcement was executed to produce these examples; they cannot prove operational recoverability.

```text
FICTIONAL FILLED SAFETY — Willow
Actor/action/identity: C replaces owned fixture F2 at H2/I2 after recovery; imagined t4.
Grants: imagined human G8 exact replacement; G9 capture metadata and independent D/F3 drill.
Ownership: F2 owned, one writer C; foreign material excluded and preserved; resolved containment known.
Threat: all listed fixture work/index/evidence classes; replacement destroys local intent, recovery applies.
Permissions/guard: declared fixture write boundary; guard tripwire only, no complete enforcement claim.
Intent: I8 names replacement/location/purpose/effect readback; authorized protected outside copy P2.
Mechanism/sink: declared capture into outside P2; private access C/D; C8 names refs/objects/reflog effects.
Coverage: H2/I2; staged-new/both versions/edit; both deletion states; untracked/ignored; mode/link/name fidelity.
Restore: separate G9, owned F3, D independent comparison; capture C8 and input F2 identities bound.
Comparison: imagined R8 full bytes/index/path/type/mode/link/classification/absence, no differences.
Evidence limit: C8/R8 are invented examples, no actual commands or restoration claimed here.
Disposition: supplied evidence permits only G8 on unchanged F2; missing real proof would block it.
Effect/retention: after act inspect destination per I8; unknown means investigate, never blind replay.
Cleanup: only separately granted run-created resources; private P2 retained under declared access policy.
```

**Positive.** Willow custodian C has authentic imagined grant G8 to replace an owned disposable fixture F2 after preserving it; separate grant G9 covers capture metadata writes and independent restorer D's fixture drill. The threat inventory includes HEAD H2, index I2, staged-new `new note.txt`, staged `both.txt` version A with unstaged version B, unstaged `edit.txt`, staged deletion `gone.txt`, unstaged deletion `removed.txt`, untracked `draft note.txt`, ignored `.local/input.txt`, executable mode and link `alias` to `draft note.txt`. Protected sink P2 is outside F2's resolved threatened extent, with access limited to C and D; intent I8 has an outside copy because replacement threatens its local record. Imagined capture receipt C8 names refs/objects/reflog effects rather than calling capture read-only. Imagined restore receipt R8, over separately owned fixture F3, compares all listed full bytes, index entries/stages/modes, names, classifications, link targets and absent deletion paths with no differences. The worksheet permits only G8's exact fixture action at unchanged F2, retains foreign work outside its scope and names actual effect readback as the next obligation. These supplied receipts explain the required evidence shape; they are not real R8.

**Boundary.** With the same threat inventory, a HEAD-only bundle misses new/staged/index/ignored versions; a sink inside F2 dies with replacement; a comparison losing `new note.txt` through whitespace splitting, following `alias`, changing its type/mode, or recreating deleted paths cannot establish full coverage. A receipt showing only restored member existence is insufficient even when the count matches. C reports each failed/unavailable class and withholds replacement while continuing authorized read-only inventory. An untracked-only fixture with index equal to HEAD still needs its threatened untracked/ignored bytes protected. A worktree whose `.git` is a file requires its actual metadata binding, not a directory-copy assumption.

**Contrary.** An owner requests only a read-only source query. C reports no threatened recoverable state and reads without a blanket snapshot. Alternatively someone proposes deletion of another session's ignored directory: even a complete outside backup provides no grant, so deletion stays unauthorized. A silent opt-in hook, unrecognized substitution or internal guard error cannot supply consent. A QA actor attempting target capture through stash is denied/reported under read-only Git rules, not promoted to writer by the safety procedure.

**Equivalent and unknown.** Willow's declared mechanism preserves exact full file/index/type/absence state into a protected authorized sink without stash/ref writes; independently verified restoration over F3 can support the same coverage without installing the donor tool. If instead the chosen mechanism writes metadata, G9 must cover those actual effects. A granted external replacement then times out: C retains intent I8 and checks the real destination. An observed matching completed effect is recorded without duplicate replacement; if completion remains unknown, C preserves that outcome and requests the owning disposition, continuing unrelated reads. No blind replay, automatic cleanup or wider credential export follows.
