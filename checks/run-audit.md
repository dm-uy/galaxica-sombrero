---
id: checks.run-audit
title: Run audit
status: draft
---

# Run audit

A particular-run audit independently relates the original promise to actual accessible records and final artifacts. It is retrospective read-only assessment, not an engine, scorer, repair phase or substitute for the existing [eight QA scans](qa-scans.md#checks.qa-scans.registry). [Run-state identity](../flow/run-state.md#flow.run-state.identity), [check evidence](lints.md#checks.lints.evidence), [QA](../roles/qa.md) and [gates](../process/gates.md) remain the authoritative owners. The [constitution bundle](../concepts/principles.md#concepts.principles.binding) and [term catalog](../concepts/glossary.md#concepts.glossary.terms) supply scoped judgment vocabulary.

<!-- anchor: checks.run-audit.binding -->

## Identity, access and impartiality

- **AUDIT-101** MUST: Identify the specified run, authentic entry role/run shape, original task and approved inputs/scope, original baseline, judged candidate and current-or-historical artifact identity before judging. Record the actual accessible record population and gaps, including truncation, unfinished tools and missing producer/time provenance.
- **AUDIT-102** MUST: Keep the independent auditor read-only over target files and Git state and declare the actual enforcement layer and access limits. Use existing record access and check contracts; route findings to the parent without editing, restarting, advancing, spending, resetting counters or authorizing integration.

The actor is a separately assigned independent reader with a bounded target/run and output contract. Read records through {{cap:run-record-access}} or its declared equivalent. A record database, schema-valid envelope or completion flag is evidence to inspect, not automatic proof of actual completion or consent. Preserve sensitive payload restrictions under [credentials](../policies/credentials.md#policies.credentials.scope); truncated exports remain limited even when privacy motivated. Writing checks require the current QA-owned isolated resource policy, never writes to the judged tree or a judge-created worktree.

<!-- anchor: checks.run-audit.procedure -->

## Read the promise and the final work

1. Authenticate the invocation and original commitments: what run was actually requested, which role/shape was assigned, what approved spec/plan/profile applied and what authority existed. Do not assume a complete cycle from an absent field or infer authority from a worker return. Unknown shape stays unknown until evidence resolves it.
2. Inventory available run events, role assignments/returns, commands/results, costs/counters and actual final artifacts with their access and identity. Check whether the record is complete for each intended conclusion: omitted tool families, shell writes, truncated content or pending calls can leave topology, purity or delivery unverified. Zero recorded writes/errors does not establish their absence outside the observed population.
3. Resolve every applicable obligation from the authentic shape and original governing contracts. Record the actual condition and reason for exclusion. A genuinely authorized single-phase observation may have no cycle/plan/QA obligation. A promised cycle missing QA or a required unreadable plan/log is incomplete or unavailable, never an N/A escape or impartiality pass.
4. Read whole final artifacts, not only edit deltas or write payloads. Compare their actual body, requirements and verification commitments to the approved inputs. A payload supports what was sent; it cannot prove saved bytes, completeness or final artifact conformance. If only payloads are accessible, label that limited evidence and leave final-artifact proof unfulfilled.
5. For historic runs obtain an authentic archived/committed/saved identity that binds the artifact to that run. Today's file can support today's identified artifact assessment, not historic final bytes. An absent logged write proves neither inheritance nor production. Inherited/adopted input needs an explicit locked input or equivalent authentic acquisition record; produced output needs attributable final identity evidence. Unknown provenance remains unknown.
6. Compare each applicable verification promise to the actual shipped tests/probes and results, including declared alternatives and genuine conditional obligations. Check semantic exercised path, asserted outcomes, negative controls and real delivered channel under [tests](../code/tests.md#code.tests.delivery). A token present in unused code, a token identical to the substituted production symbol, mock-only delivery or an empty promise cannot prove fulfillment. Source parser/grep coverage remains separate from this judgment. Absence of a section does not prove an older protocol version; authenticate that version first.
7. Relate each finding to requirement/check, actual actor/action/artifact, evidence, severity and limits. Distinguish measured violation, computed result, source assertion and unavailable proof. Report tool failures in context: an error is not automatically a product defect, and no errors is not delivery proof. Retain cumulative Debug/cost/retry history without changing its budget or treating no Debug as proof of correctness.
8. Return bounded findings and parent-owned disposition. Implementation defects follow the existing Bug Report route; unavailable environment/authority/evidence follows its owning blocked route. Audit does not launch repair or learning/comparative scoring. If requirements include full QA, the original complete registry accounting remains required; this audit adds no ninth scan.

- **AUDIT-201** MUST: Grade actual complete artifacts under their authentic identity; distinguish write payload, current bytes, historic final bytes, adopted input and produced output. Missing logged writes or today's path existence cannot supply historic attribution or inheritance.
- **AUDIT-202** MUST: Preserve missing applicable plan, QA, log or delivery evidence as unverified/blocked under its governing interface. N/A requires an authenticated false trigger or different authorized shape; no QA observation cannot pass QA impartiality.
- **AUDIT-203** MUST: Give each finding its governing check/requirement, severity from the applicable profile, reproducible evidence, claim/access limits and owning parent disposition. Zero findings alone cannot establish terminal SUCCESS or concrete-result acceptance.

Current QA findings retain its LOW/MEDIUM/HIGH profile and six-field Bug Report; other declared audit severity profiles are reported as their own dialect, not silently normalized into wire values. Independent assessment may discover a source implementation defect or proposal, but neither constitutes a delivered check: a proposed attribution guard is not enforcement. A current artifact available without historic provenance may be assessed separately with an explicit current identity while the historic conclusion remains unverified.

<!-- anchor: checks.run-audit.form -->

## Reusable particular-run report

This prose form uses the existing authorized evidence home, not a transcript parser or state extension. Repeat obligations, artifacts and findings for the full selected population.

```text
PARTICULAR-RUN AUDIT
Independent actor / assignment / read-only enforcement and output authority:
Run/entry/shape: authentic invocation reference, time, original task and promised phases:
Locked inputs/grants: spec/plan/rules/adapter identity, baseline acquisition, action/scope consent:
Judged candidate: full inventory/content identity and current-versus-historic basis:
Record inventory: source/access/read extent, complete/truncated/missing/pending populations:
Artifacts: full read identity, current/historic binding, produced/adopted/unknown provenance and proof:
Obligation row: owner/id, actual trigger, applicability/reason, expected promise, actual outcome/evidence:
Verification commitments: promised mechanism/path/alternatives, actual shipped test/probe and delivery limits:
Finding: check/requirement, actor/action/artifact, severity dialect, evidence, violation or unavailable proof:
History: actual Debug/cost/retry records, missing accounting and retained failures:
Disposition: parent route, actionable recommendation or missing access/authority, affected claim withheld:
Overall limit: what this audit establishes, what remains unverified, required QA/result consent outstanding:
```

<!-- anchor: checks.run-audit.cases -->

## Fictional worked cases

Elm's actors, runs, identities and receipts below are fictional and are not actual audit, delivery or enforcement evidence.

```text
FICTIONAL FILLED AUDIT — Elm
Actor/permission: independent J, bounded E-4 assignment; declared read-only layer, report output only.
Run/shape: E-4/I4, imagined t3; architect-led cycle, spec S3 and plan P3 promised.
Inputs/grant: S3/P3/rules U3/adapter A3 locked at B2; authentic imagined human local G3.
Candidate: full K7 saved inventory and immutable identity at A7; historical E-4 binding.
Record: complete selected R7 events/returns/commands, no pending or truncated selected evidence.
Artifacts: full plan/body/test reads at A7; adopted S3/P3 input locks, produced K7 final inventory.
Obligations: original cycle and required QA observed; all eight scan dispositions in R7.
Verification: P3 file-channel promise exercised by F3/Q7, real target readback and missing/reattached control.
Findings: none in this selected population; no inferred historic bytes from current files.
History: R7 retains actual imagined Debug/cost/retry accounting; no reset or new spend.
Disposition: parent checks original terminal predicates; sharing/integration still requires owner decision.
Limit: audit supports the supplied E-4/K7 evidence only; no universal transcript or live adoption proof.
```

**Positive.** Auditor J receives Elm run E-4, authentic architect-led cycle invocation I4 and spec S3/plan P3 locked at baseline B2. Saved snapshot K7 is bound by the run's final artifact inventory and independent receipt A7; J reads its full plan, implementation and test bodies. Records R7 contain the actual QA assignment, complete command streams/exit, eight applicable scan dispositions and finalization evidence for K7. Plan P3 promises an actual file-channel probe: shipped test F3 flushes output, reads the real isolated target and checks a missing/reattached control, with receipt Q7 binding execution. J reports bounded fulfillment at K7, read-only observed QA evidence and no finding in the inspected population. Parent checks the original terminal predicates; J's zero findings grants neither SUCCESS nor merge. Sharing remains reserved by the genuine owner grant.

**Boundary.** The write payload includes P3's verification section, but K7's actual full plan lacks it; J reports the required-artifact violation and actionable parent recommendation. For an older E-3 only today's changed K8 file exists, with no historic identity or logged final inventory: J can report K8's current content separately, but E-3's historic result and provenance remain unknown. An absent logged plan write cannot become “inherited”; only an explicit authentic input lock could establish adoption. If E-4 instead lacks required QA or its plan cannot be read, J records unavailable promised-cycle evidence, not QA purity PASS or N/A, and the parent holds dependent completion.

**Contrary.** An authentic separate invocation I5 assigns only read-only investigation E-5 and explicitly promises no software cycle, plan or QA. J records those false triggers as genuinely nonapplicable and assesses the investigation's actual promised output. A record merely missing the shape field cannot get that exemption. In E-4 a verification token in an unused helper or mocked transport passes a presence grep but fails the real delivered-channel promise; J records that semantic defect despite green token output. A missing transcript prevents a purity conclusion rather than proving no writes.

**Equivalent.** Elm's adapter permits authentic complete append-only event records plus an immutable final archive instead of a database. J reads those identities and full artifacts and makes the same obligation-by-obligation judgment without a parser/scorer installation. If the archive lacks a required artifact or the trace suppresses a relevant write family, J preserves that specific limit and routes missing proof; a convenient current file or truncated export does not fill the historic gap.
