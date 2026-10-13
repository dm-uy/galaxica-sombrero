---
id: checks.preflight
title: Preflight
status: draft
---

# Preflight

Preflight accounts for the prerequisites of an identified launch before its dependent effects or spend. It composes the existing [run-state](../flow/run-state.md), [gates](../process/gates.md), [base permissions](../roles/_base.md#roles.base.boundaries), [credential binding](../policies/credentials.md) and [check evidence](lints.md#checks.lints.evidence) contracts. The [constitution bundle](../concepts/principles.md#concepts.principles.binding) and [term catalog](../concepts/glossary.md#concepts.glossary.terms) remain scoped inputs. This subject adds neither a launch phase nor a registry or wire-status dialect.

<!-- anchor: checks.preflight.binding -->

## Select the launch and predicates

- **PREFLIGHT-101** MUST: Before the action they gate, identify the actual launch/profile, actor, target/framework and task/plan/rules/adapter identities, matching authority, acquired baseline/candidate, prerequisites, resource units and remaining allowance, permitted mechanisms and claim limits. Select every applicable predicate from its actual owning contract; record false-trigger exclusions with reasons.
- **PREFLIGHT-102** MUST: Distinguish declared mechanisms and configured permissions from observed behavior. A green local inspection cannot prove future structured delivery, role isolation, timeout behavior under load or per-turn accounting where those properties remain structurally uncheckable in advance.

The responsible launch custodian performs or receives the assessment through {{cap:check-runner}} and the declared {{cap:launch-environment}} binding. The parent remains the only authoritative state writer and transition owner. Resolve actual permission policy, including hard enforcement versus behavioral fallback, protocol-read access, delegation denial, and last-match ordering where that semantics applies. Inspect only permitted credential presence and consumer scope, never values or unauthorized stores. No preflight failure grants login, provider change, install or wider access.

The selected population can include acquisition of the actual target/baseline, readable nonempty approved task and required plan, framework and protocol identity/content, available launch resources, active phase predicates, permission/isolation binding, declared recursion guard, credential consumer readiness and action-specific safety dependencies. Applicability follows the invoked profile; a non-repository task does not acquire a universal Git requirement. The exact predicate list is recorded before assessment so loss or substitution is visible. Runtime-specific playbook counts, model/server names, free request quotas and fixed recursion constants belong to adapters. A protocol-loading prohibition must not be transplanted into a runtime requiring those reads.

<!-- anchor: checks.preflight.walk -->

## Account before spending

1. Bind the launch to the approved inputs and candidate; reconcile mismatches under existing amendment/gate rules before advancing. Retain actual baseline acquisition evidence, prior refused/failed attempts and cumulative costs. A renamed run or fresh shell is no resource reset.
2. List the full selected predicate population, owner/trigger, applicability, prerequisite relationships, cost/effect tier, exact method and recognizer/claim limits. Include properties lacking an advance-check mechanism as unverified claims. Distinguish optional false-trigger exclusion from missing required evidence.
3. Attempt every independent cheap local check even after another local check fails. Record each actual result, command or direct observation, input identity, complete relevant streams/exit and safe exception class. An exception or unreadable/empty-required input is a failed or unavailable assessment under the owner's interface, never a clean result; do not stop the local walk and lose other failures.
4. Assess structurally unverifiable rows explicitly with their claim limits. Presence/configuration can be checked while future behavioral enforcement remains unverified. Do not relabel such a row PASS just because the executable local rows passed.
5. Before a dependent paid, remote, expensive or consequential action, examine all its required prerequisite rows and authority. Withhold it after a failed/unavailable prerequisite; keep its row with named causes and actual spend/effect absence or uncertainty. Independent safe checks continue. An optional authorized fallback follows its declared condition and records reduced coverage.
6. Execute an eligible dependent check only through the existing permitted mechanism and allowance, then retain its result and actual cost provenance. A failed remote check stays failed; a timeout's effect remains unknown and follows [safety](../process/safety.md). No automatic retry or spend beyond the owning allowance is introduced.
7. Reconcile the selected population with reported rows in both directions: no omitted predicate and no unexplained invented row. Aggregate all failures/unavailability and withheld dependencies; route through the current phase/role/state contract. State the exact eligible or blocked launch and unresolved claims. The report alone supplies no authority or phase success.

- **PREFLIGHT-201** MUST: Account for every selected predicate with applicability, actual outcome, evidence, reason and claim limit; independent cheap checks continue after failure, while dependent effects and spend are withheld before execution and reported with their prerequisite causes.
- **PREFLIGHT-202** MUST: Preserve each owning interface's statuses and failure routing. Skipped because a prerequisite failed, unverified because proof is unavailable, a measured failure and genuine N/A are distinct facts, not interchangeable success or new canonical enums.
- **PREFLIGHT-203** MUST: Check the actual current allowance in its unit without conflating recursion, Debug entries, response/transport retries and test-session attempts. Respect a valid zero additional Debug allowance; it permits no new Debug entry but does not invalidate otherwise eligible work or QA after the last repair. Retain consumed entries and all prior costs.

Current [repair accounting](../flow/run-state.md#flow.run-state.repairs) governs cumulative Debug spend, including failed entries, and [separate retries](../flow/run-state.md#flow.run-state.retries) governs other counters. Recursion sizing follows STATE-204's declared segment between owner resumes, not an invented universal bound. A profile requiring an explicit spend ceiling checks that actual requirement; another profile's currency or numeric quota is not imported. An unavailable promised launch mechanism blocks its dependent launch, while a declared direct-read/manual mechanism may establish its stated bounded predicate. Neither supplies runtime enforcement proof.

<!-- anchor: checks.preflight.form -->

## Reusable total assessment

The following prose form belongs in an existing authorized record home. Rows repeat for every selected predicate; it does not extend an adapter or state schema.

```text
PREFLIGHT
Actor / launch action / profile identity / assessment time:
Authority: authentic action/artifact/scope reference; exclusions and missing decisions:
Inputs: target/framework/task/plan/rules/adapter identity and read/access limits:
Baseline/candidate: actual acquisition, current inventory/identity and ownership:
Resources: each unit, cap, cumulative spent, remaining, scope and enforcement mechanism:
Predicate selection: complete owner/id population and genuinely false triggers:
Predicate row: id/owner, trigger/applicability, dependencies, cost/effect tier, method and limits:
Row evidence: input identity, observation or argv/cwd/streams/exit, safe exception, actual outcome:
Unverifiable claims: row, absent advance mechanism, exact property not established:
Withheld rows: prerequisite ids/reasons, no execution evidence or unknown effect, spend:
Population reconciliation: selected vs reported; omissions/extras and disposition:
Launch disposition: eligible action or blocked dependency; current parent route and next resolver:
Retained history: failed/refused attempts, costs/counters, reuse identity, recheck conditions:
```

<!-- anchor: checks.preflight.cases -->

## Fictional worked cases

All Birch inputs, actors and receipts are invented. Status names in these illustrations describe the supplied check profile only; they create no canonical enum, permission or live-run proof.

```text
FICTIONAL FILLED PREFLIGHT — Birch
Actor/action/profile/time: P; launch local L/B-7; F1; imagined t2.
Authority: imagined human G2 grants L on S2/D2/K2; no provider/configuration changes.
Inputs: target Birch, framework W1, S2/D2/rules U1/adapter F1; full local reads R1.
Baseline/candidate: acquired H1/K2 at R2; owned launch state, no foreign writes.
Resources: 5 worker turns, 2 spent, 3 remaining at R4; connectivity has one-request unit.
Selection: four local predicates, dependent connectivity, behavior-under-load claim; no other F1 rows.
Local rows: input R1 pass; acquisition R2 pass; permission binding R3 pass; allowance R4 pass.
Limits: R3 establishes declared policy only; behavior-under-load unverified, no advance mechanism.
Dependent row: connectivity R5 pass; actual imagined one-request cost retained.
Withheld rows: none under F1; later behavioral/delivery claims not established by this assessment.
Reconciliation: all six selected rows reported once; no extras or omissions.
Disposition: L eligible under G2/F1; no terminal SUCCESS; parent owns transition.
History: original two spent turns retained; recheck on input, allowance or binding change.
```

**Positive.** Birch custodian P assesses local phase L of task B-7 at candidate K2 under authentic grant G2 and profile F1. F1 selects exactly input-readability, baseline-acquisition, permission-binding and allowance as local checks, plus later worker-connectivity dependent on all four; behavior-under-load is an explicitly unverifiable claim. Receipts R1–R4 bind readable spec S2/plan D2, acquired baseline H1/K2, declared read/write/delegation policy P2 and remaining 3 worker turns out of 5 with 2 already spent. A fifth receipt R5 shows the eligible permitted connectivity check actually ran and charged its declared one-request unit. Output accounts for all six rows: five observed passes and behavior-under-load unverified. L may proceed under F1 because the latter is a declared launch claim limit, not a promised criterion completed in advance. No role-hardening or terminal SUCCESS is claimed.

**Boundary.** At the same launch spec S2 is missing, allowance is invalid for the next paid turn, and permission inspection raises a safe read error. P still finishes the independent baseline check. The report retains missing-input, failed-allowance and unavailable-permission rows, baseline pass and behavior-under-load unverified; connectivity is withheld with all three causal row ids and no request/spend. P routes the defects/access gap through the existing parent contract, rather than omitting rows or emitting green. A required promised behavior criterion would remain unfulfilled even if R1–R5 passed.

**Contrary.** Birch changes to a granted final QA visit with additional Debug allowance zero after its last permitted repair; a valid ledger confirms spent entries and no further repair grant. P accepts the zero value, permits eligible QA and refuses any new Debug entry. A separate absent optional search service is N/A only because this task's F1 profile does not use it. Missing required worker access is unavailable, never that same N/A. A local permission file saying read-only does not prove an agent cannot write; the behavior claim remains unverified.

**Equivalent.** F1 explicitly permits manual acquisition and direct full-file permission/input comparison. P supplies those observations with identities and accounts for the same four local predicates, without installing a preflight engine or importing seven playbooks or a fixed recursion pin. The assessment supports only those observed properties. If F1 instead promises a runtime-resolved recursion check and no authorized mechanism can read it, P leaves it unverified and withholds dependent launch; a guessed configuration value cannot replace that check.
