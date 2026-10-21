# Methodology project route

## Current: QA-REFLECT checked locally; result integration pending

Owner-approved bounded clarification follows the consumer-run review and four independent critiques. [Scope, decisions and evidence](notes/qa-reflection-clarification.md); [tasks](TASKS.md). Bounded source/package checks and independent document review complete; main integration and installation remain separate. Earlier route and held work remain unchanged.

```mermaid
flowchart LR
    QRT1["QA-REFLECT-T1 checked: neutral and native guidance"] --> QRT2["QA-REFLECT-T2 checked: result integration pending"]
```

## Retained: GRACE-Q2 integrated and delivered to origin/main

One canonical checkout is the development source; preparation repositories are archival. Canonical main includes M30 source through owner-approved PR6 and the later M31/M33 updates. Canonical main carries neutral/Codex/DSH 3.0.2 and Claude 2.1.1 after GRACE-Q2; M37/PR11 and M38/PR10 remain the preceding package checkpoints; accepted C2/bafec417 is the historical foundation, not the current version. C3 is not ready for merge. [Current C3 history/result](notes/m28-c3-result.md).

| Checkpoint | Current disposition |
|---|---|
| M1–M20 | Historical PM/code/document/decision/prompting/readiness work and first Codex package; contracts remain in source. |
| M21 | Historical Python/FastAPI/SQLite consumer; frontend → Telegram → MCP remain later scoped stages. |
| M22–M23 | Complete Claude in-place package and MIT adoption. |
| M24 | Historical release preparation, not another development source. |
| M25A | Complete MIT/no-query and Gitignore-aware inventory repair. |
| M25B | Checked261-file projection, owner acceptance and verified private release complete. |
| M25C | Held: separate native consumer decision. |
| M26 | Permanent canonical checkout, verified onboarding and integrated PR1 complete. |
| M27 | Coverage preparation/matrix and C1–C6 route integrated through cumulative PR3; whole behavioral parity remains owed. |
| M28-C1 | Integrated through PR3: required owners, native prompt route and neutral1.1/source2.1 bridge. |
| M28-C2 | Owner-accepted and integrated through PR4: source2.2 consumer profile and commands; original failed history/spend retained. |
| M28-C3 | Unaccepted source2.3; A3 terminal ESCALATED/review, protected-read defect remains after green QA2. Cumulative Debug4/4 exhausted; no fifth repair. |
| M28-C4 | SDK/import/candidate capacity owed/held after the selected practical consumer trial. |
| M29/C5–C6 | Autonomy/resume/isolation proof and actual source-loader handover owed/held after matching decisions. |
| M30 | Source integrated through PR6; BLOCKED/qa Debug1/4 retained. Owner lifted the Claude deferral in M37: native Claude AC4/Claude AC5 observed on candidate2.0.2 ([M37](notes/m37-claude-parity.md)); renewed independent QA/whole Review/assigned Finalize and full acceptance still pending. |
| M31 | Lightweight PM merged, released and installed; actual completion is in the decision receipt below. |
| M32 | Findings retained; T1 and bounded T2/T3 checks complete, with optional practices limited to observed scope. Owner-accepted local integration and canonical remote delivery are complete. Prompting0.6.0 is installed locally; its separate source upstream/release remains undelivered. |
| M33 | Early entry duties and additive bootstrap checked; synthetic/source-review limits retained. Owner-authorized local merge/install and canonical remote delivery complete: neutral/Codex3.0.1, Claude2.0.1; actual discovery/binding evidence retained. |
| M34 | Checked locally: reader-oriented README and two diagrams, preserved contracts and local visual checks. Owner-approved local integration and canonical main push complete. The repository is now public; that does not create a new packaged release or installed update. |
| M35 | New-machine installation entry and complete-snapshot instructions checked locally, including isolated native CLI installation. Owner-requested main integration/push complete with remote readback; actual other-machine installation remains separate. |
| M36 | Completed: checked record synchronization and self-contained chat conclusions integrated into canonical main and pushed under explicit owner approval; [receipt, evidence and preserved baton](notes/m36-session-handoff.md). Next bounded task awaits owner-selected scope. No framework implementation or donor adoption. |
| M37 | Claude package actualization: patch2.0.2, then the C2 consumer PM port as Claude2.1.0 (mechanism H: launchers and carrier referencing the Codex C2 helpers in place). Feature-dev run with independent QA/Review/Finalize; Debug1/4; owner accepted the result with recorded AC5 limits; merged into `origin/main` through PR11 (merge `380dd00`, 2026-10-17). The owner disabled the in-house plugins on 2026-10-19; consumer migrations follow under per-project grants. [Record](notes/m37-claude-parity.md). |
| M38 | DSH native implementation package 3.0.1 over neutral 3.0.1, installed into the live `web`/`desktop` profiles; live discovery, `pm` loading and a bounded smoke observed. Rebased onto M37 and merged into `origin/main` through PR10 (merge `1ff633c`, 2026-10-19). Full Bootstrap-to-Finalize, checkpoint/resume and role isolation on DSH remain unproved (probe 3). [Result](notes/m38-dsh-package.md). |
| GRACE-Q2 | Owner-approved minimal QA/LDD/test-guide clarification, neutral first then three adaptations; implemented, locally checked and independently document-reviewed; package448e575 integrated and delivered to origin/main with remote readback. Working-profile installation withheld. [Scope and checks](notes/grace-qa-evidence-minimal.md). No new roles/runs or contract/test reduction. |
| Public visibility | Public, confirmed by GitHub readback on 2026-10-15. Earlier private-release/publication holds remain historical; future releases still need their own scope. |

Canonical delivery update2026-10-15: owner-requested direct push delivered the canonical M32/M33/M34 commits. This supersedes earlier canonical-PR delivery holds below; no PR was created. Separate prompting-source upstream/release remains outside that push. Repository visibility was separately observed as public on 2026-10-15; see [M36](notes/m36-session-handoff.md).

## M34 — README presentation

Owner-selected polish of the public-facing entry, not permission to publish. [Result and retained review/check evidence](notes/m34-readme.md); [TASKS](TASKS.md).

```mermaid
flowchart LR
    M34T1["M34-T1 checked: README and diagrams"] --> M34T2["M34-T2 complete: local main integration"]
```

## M33 — PM entry continuity

[Authority, reconnaissance, implementation and result](notes/m33-pm-entry.md); [current tasks](TASKS.md). Owner selected the short entry obligations and safe existing-project supplementation. No bulk consumer rewrite or new executable checker is implied.

```mermaid
flowchart LR
    M33T1["M33-T1 checked: seeds and additive bootstrap"] --> M33T2["M33-T2 complete locally: merged and installed"]
```

## M32 — incremental improvement route

The owner selected this route on 2026-10-15: record all book-derived findings, verify incrementally and adopt useful results. [Findings, original authority, source identities and limits](notes/m32-book-findings.md); runnable work stays in [TASKS](TASKS.md).

1. **Checked locally — carrier consistency:** source candidate53b62f0 reconciles the carriers at draft0.6.0; independent document review, structural checks and actual authoring proof support retaining it for review. Owner-approved local source merge is complete; prompting0.6.0 subsequently installed locally. Canonical record delivery is complete; separate prompting-source upstream/release and target readiness remain separate.
2. **Checked locally — document extraction:** retained the optional recipe after seven synthetic sources, simulated truncation/staleness and actual bounded book extraction. No new mandatory carrier/helper.
3. **Checked locally — fresh-reader usefulness:** reader recovered authority/holds, caught a synthetic contract contradiction and stale M31 wording; narrow record corrections made. This is a read-only sample, not the full consumer trial.
4. **Integrated and delivered canonically:** the owner accepted the concrete package and both local main merges completed. The later owner-authorized direct push completed canonical delivery without a PR; the earlier API/browser delivery blocker is superseded. Prompting installation completed locally; its separate source upstream/release remains undelivered.

This is the dependency view for M32 only; older checkpoint rows retain their original states and evidence:

```mermaid
flowchart LR
    M32T1["M32-T1 integrated in local source main"] -->|record disposition| M32T2["M32-T2 checked: optional recipe"]
    M32T2 -->|record disposition| M32T3["M32-T3 checked: fresh-reader sample"]
    M32T3 --> M32T4["M32-T4 canonical delivery done; prompting upstream separate"]
```

Carrier consistency comes first because contradictory active instructions can undermine either later check. Each stage records its question, candidate, actual result, benefit/friction, retain/revise/drop/hold disposition and next action. Findings alone do not approve a new compulsory procedure. Main integration, release and activation remain separate decisions over concrete results.

Replan basis: previously the next proposed practical route was a smaller safeguard followed by the API/database trial. The owner now selects M32's bounded instruction/document checks first. The full trial's original safeguard prerequisite remains; C3 exhaustion, M30 Claude deferral and C4–C6 obligations are preserved. No new safety design or failed-run continuation is authorized by this reordering.

## Retained C3 escalation

Stop C3 implementation. Whole Review2 confirmed that lexical parent normalization hides a symlink traversal and can allow a protected read. Current QA2's597/158/526 passes do not override the defect. No accepted Review/Finalize exists. Native AC7 is HELD/UNFULFILLED, not waived by the approved partial source stage.

Recommended next activity: read-only reconnaissance and a bounded revised design/specification for a smaller safeguard surface, considering exact parent-pinned check recipes rather than generic shell interpretation. No new design or Code is approved by this route note. Preserve cumulative spend and failed terminals; do not rename/reset the run to acquire another repair.

## Retained route and gates

Accepted C2 profile/check/map/migration → genuinely accepted minimal safeguards → bounded single-stream Python API/database trial → separately scoped optional C4 infrastructure → C5 native autonomy/resume/isolation → C6 loader handover. The practical trial precedes optional infrastructure; C4–C6 remain obligations, not waived work or current Code grants.

The owner-approved exact46b7ccc push/private draft PR5 update is complete. Subsequent A3 source and root record closure remain local review work. For that unaccepted C3 candidate, main merge, new remote delivery, install/activation and native proof still need their matching decisions. Repository visibility itself is already public; that observation does not accept or publish the C3 candidate. Other agents start at root AGENTS, use scoped branches and preserve foreign work/clean canonical main. Error recording stays lightweight; systematic learning/measurement and concurrent feature writers remain deferred.

## M30 — independent-decision rule; proof held

Shared owner/PM/Architect/both-carrier source delivered from accepted C2 and independently checked after counted Debug1. Actual Codex important/two-generators/HOLD/evaluator/root-decision/task and trivial/settled controls supported;600/146/526ordinary tests and privacy/adapters/maps pass. [Current result](notes/m30-result.md), [operative plan](plans/m30-independent-decisions-i2.md).

Terminal BLOCKED/qa retains Debug1/4. The owner deferred native Claude; AC4/ClaudeAC5 remain unfulfilled, no auth/retry/waiver. Resume those current-source proofs after that deferral changes, then renew independent QA, whole Review and assigned Finalize before full checkpoint acceptance; owner-authorized source integration through PR6 is complete. INTAKE-01 stays separately scoped; accepted smaller safeguard → single-stream API/database trial → optional C4 → C5/C6 route remains. [Integration record](notes/m30-integration.md). No C3 budget reset, installation or public visibility change.

## M31 — lightweight PM state and development boundary

The owner settled the direction after the PM reflection: state for agents, QA for features/substantial bug fixes, no QA for documentation/small corrections, and affected-record synchronization on material change/grouped progress/before planned compaction. [Decision and scope](notes/pm-lightweight-direction.md). The initial local amendment preceded release; the owner subsequently authorized merge, reissue and installation, completed in the receipt below. Existing M30 Claude deferral, C3 exhausted history and later trial/C4–C6 route remain retained.

M31 release update: the owner authorized merge, reissue and installation of the accepted lightweight PM direction (neutral3.0.0 / Codex3.0.0 / Claude2.0.0). Actual completion is recorded in [the decision receipt](notes/pm-lightweight-direction.md); deferred native Claude acceptance and C3 remain separate.

## M38 — DSH native implementation package (merged through PR10)

The owner asked for the methodology to be implemented for the DeepSeek Harness under `implementations/` and connected as a plugin. Delivered as a third typed package at 3.0.1 over neutral 3.0.1, with an adapter over all 71 neutral files, 27 skill carriers, six role carriers, the shared helpers and a DSH bundle that mounts the package's own skill root. [Result, evidence and limits](notes/m38-dsh-package.md).

Not a release and not accepted behavior. The owner later approved the `main` merge and the live installation: the bundle is installed into the `web` and `desktop` profiles, live discovery and a bounded smoke were observed, and the rebased package was merged into `origin/main` through PR10 (merge `1ff633c`, 2026-10-19). A packaged release and the full Bootstrap-to-Finalize run retain their separate owner decisions. The sibling packages' source, wire, schema and behavior are unchanged, and the retained M30/C3 limits and the later trial/C4–C6 route are untouched.

## GRACE-Q2 — bounded documentation package

```mermaid
flowchart LR
    GQ2T1["T1 done: neutral and carrier clarification"] --> GQ2T2["T2 done: checks, review and main/origin delivery"]
```
