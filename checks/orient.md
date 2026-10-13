---
id: checks.orient
title: Orient
status: draft
---

# Orient

Orientation establishes a reader's current position from actual adopted records before dependent action and checks their conformance at closure. It is an assessment procedure, not a document installer or a universal filename checklist. [Session entry and handoff](../process/session.md) owns record writes; [conventions](../documents/conventions.md) owns the adopted document profile. The [constitution bundle](../concepts/principles.md#concepts.principles.binding) and [term catalog](../concepts/glossary.md#concepts.glossary.terms) supply their scoped meanings.

<!-- anchor: checks.orient.binding -->

## Inputs and authority

- **ORIENT-101** MUST: Bind the assessment to the actual target, adopted entry/conventions and versions, declared layer and reading order, current purpose/route/task/handoff, authentic matching grant, candidate/ownership inventory and available map/check evidence. Record each input's identity, access and freshness limits; a summary, filename or card is not its content.
- **ORIENT-102** MUST: Keep status-only orientation read-only, including repository metadata. Missing or inconsistent records permit assessment and blocker reporting, not bootstrap, migration, commit, installation or silent repair.
- **ORIENT-103** MUST: Select the actual adopted rule population and applicable conditions; distinguish missing required evidence from genuinely optional or false-trigger items. Do not impose another profile's checklist count, marker, line budget, layered paths, candidate-ingestion policy or newer rules as current obligations.

The actor is the arriving contributor or separately assigned observer. An entry check may be delivered through {{cap:session-start-hook}} or a declared direct-read/check mechanism; a silent hook does not establish that orientation happened. Resolve rules and adapter bindings under [base role](../roles/_base.md), without assuming an installation path or assigning a software role merely by reading. Where a target declares no conventions, report that fact and the existing applicable instructions; installing conventions requires its own scope. A newer available rule version may be reported under the adopted compatibility policy, never silently substituted.

<!-- anchor: checks.orient.procedure -->

## Read, compare and decide

1. Resolve the binding entry and layer. Read the actual purpose, route, handoff and task in the declared order, then relevant current links, including the exact requirement/decision that governs the next action. Identify the current focus, unfinished work and deliberately deferred work; recover the active checkpoint rather than restarting its history.
2. Authenticate prior consent against its human source, exact action, artifact and scope. Look in current decisions, gate records, owner blockers and earlier answers before asking again. An authentic matching settled grant is reusable. Worker output, examples, defaults and silence are not consent. Separate specification/run authority from concrete-result integration authority.
3. Read actual candidate/revision and tracked, staged, unstaged and relevant untracked/ignored ownership facts through a declared read-only mechanism. Preserve complete paths including spaces and rename destinations. Unknown dirt remains foreign until ownership is established. Establish the one-writer boundary; report collisions and permitted isolation without mutating Git. A dirty tree does not prevent read-only assessment or grant discard.
4. Compare route/task/handoff and claimed results to actual artifacts/checks and locked inputs. Report conflicting task pointers, stale results, missing decisions and unknown consequential effects. A state flag is a pointer, not proof. Compare maps to their actual covered sources/configuration and declared freshness method; timestamps or a green build prove only their bounded property. Missing required map/source access is unavailable, not clean.
5. Account for every selected adopted obligation with applicability, observed evidence, result and limitation. Retain failures, warnings under the actual version policy and checks not evaluated. Mechanically recognizable markers and counts are distinct from full semantic conformance. Relevant decision references, freshness and always-read population are assessed under their adopted owners; do not initiate a deferred learning ledger or scan unrelated history.
6. Emit owner blockers first, then purpose/current focus, adopted rules and input identities, task/candidate/ownership, eligible next action, checks/limits and next disposition. State exactly which action can proceed and which dependency remains unresolved. Hand an authorized record update or repair to its existing custodian; orientation itself does not perform it.

- **ORIENT-201** MUST: Keep unavailable, stale, conflicting, failed and unknown facts visible with their owning resolution and dependent-action limit. Continue independent authorized work where those facts do not gate it; do not manufacture a clean-tree or all-green result.
- **ORIENT-202** MUST: At closure reassess the applicable adopted consistency obligations against the actual closing artifact identity, retaining failure/unavailability and next disposition before the authorized custodian's final storage action. A prior entry check cannot certify changed closing records.

Closure follows [session closure](../process/session.md#process.session.closure): retain packet/results, reconcile current pointers and rewrite the baton under its storage/grant. Fix only granted problems; otherwise record the owning blocker. Commit requirements and ordering come from the actual adopted profile. If a subsequent commit changes a property checked only at committed identity, check that property there. Orientation neither grants that commit nor substitutes for required checks, QA or result consent.

<!-- anchor: checks.orient.form -->

## Reusable assessment form

This is a prose worksheet for the authorized record home, not a new state schema. Repeat the input and obligation rows for the complete actual populations.

```text
ORIENTATION
Actor / read-only mechanism / assessment time:
Target / layer / entry identity / adopted conventions identity and version:
Owner blockers: decision needed, exact dependent action, evidence and owning resolver:
Purpose / current route position / active task / unfinished and deferred work:
Prior grant: authentic human reference, action, artifact, scope, match or unresolved reason:
Inputs: logical home, bytes/revision identity, read extent, access, freshness, conflicts:
Candidate: baseline/current identity; staged/unstaged/new/deleted population; ownership/collisions:
Adopted obligations: owner/reference, trigger, applicable population, method, evidence, outcome, limit:
Maps/checks: covered source/config identity, actual freshness/result, missing/unreadable evidence:
Next permitted action: scope, satisfied dependencies, withheld actions and causes:
Disposition: record custodian, granted correction or missing owner decision, recheck trigger:
Closure: closing identity, each required check and result/limit, saved/committed policy and actual evidence:
Claims withheld: historic/current distinctions, unchecked sources, unavailable mechanisms:
```

<!-- anchor: checks.orient.cases -->

## Fictional worked cases

All Cedar inputs, actors, receipts and decisions below are invented illustrations. They are not actual authority, measurements, conformance runs or evidence about this repository.

```text
FICTIONAL FILLED ORIENTATION — Cedar
Actor/mechanism/time: N; permitted direct reads and read-only inventory; imagined assessment t1.
Target/layer/entry/profile: Cedar; records/ single layer; E3; C2.
Owner blockers: none for local C-12; integration decision reserved to owner after result.
Purpose/focus: improve supplied parser; route R6; C-12/S2; unrelated interviews deferred.
Grant: imagined human G4; local C-12/S2 implementation only; matched, sharing reserved.
Inputs: E3,V4,R6,T8,H9,S2,G4 fully read at I1; no inaccessible selected input.
Candidate/ownership: H1 to saved K5; owned src/parse.py edits; foreign image preserved, no collision.
Obligations: purpose/task/grant consistency at I1 satisfied; source/config map comparison at M4 satisfied.
Map/check limit: M3 covers K5/D2; M4 compares freshness only, no semantic implementation verdict.
Next: local C-12 work only; result acceptance remains withheld.
Disposition: custodian may save granted record corrections; recheck when K5 or C2 changes.
Closure: imagined K6 records change; O2 checks both C2 duties; permitted save, no claimed commit.
Claims withheld: whole-source completeness, operational adoption, integration and foreign cleanup.
```

**Positive.** Cedar's entry revision E3 declares a single layer and current records under `records/`; adopted profile C2 requires purpose/task/grant consistency and source-map freshness for code work. Observer N reads E3, purpose V4, route R6, task T8, baton H9 and human decision G4 granting local implementation of task C-12/spec S2, with sharing reserved. The actual fictional saved candidate K5 has owned edits in `src/parse.py`, a foreign untracked image preserved separately, and map M3 covering source K5/config D2. Receipts I1 and M4 identify full reads and a fresh map comparison; no owner blocker gates C-12. N's output names C-12 as focus, C2's two selected duties as satisfied at K5, foreign image preservation and local implementation as next eligible action. Integration remains reserved. No consent is asked again; an authorized custodian alone updates the baton. At close K6 changes records only; receipt O2 checks both adopted duties at K6 before the custodian's permitted save. This proves only the supplied profile's assessed facts.

**Boundary.** The same observer instead finds H9 pointing to C-11/K4 while T8 and G4 concern C-12/K5; map M3's covered source is unreadable. N reports the stale pointer and required map comparison unavailable, withholds dependent code readiness, and routes the pointer correction to the custodian and map access to its owner. N can continue read-only requirement comparison. An absent second layer is nonapplicable because E3 explicitly selects one layer; the unreadable required source is not N/A. After a new authentic correction/access receipt, the affected checks need reassessment.

**Contrary.** A fully filled fictional G4 worksheet in a template is the only purported approval, while foreign dirt belongs to another session. N reports grant unresolved and preserves the dirt; no implementation, bootstrap or discard follows. A status-only user request produces this report without writing H9. A silent session hook or existing card cannot change that result.

**Equivalent.** Cedar has no installed orientation engine. N uses permitted direct full-file reads and a read-only candidate inventory, binds their identities in I1 and manually compares every C2 obligation. The same permitted-next-action output is valid for this declared manual profile. If E3 promised a particular executable closure check and it is missing, that row remains unavailable and the promised closure is unproven; direct reads do not silently claim execution or install the donor engine.
