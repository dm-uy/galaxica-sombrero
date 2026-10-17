# Canonical handoffs — run-state schema 2

Read the full current `protocols/role-returns.md`, `flow/phases.md` and `flow/run-state.md` and the [runtime](claude-runtime.md) before dispatching or accepting a phase. Those owners define the canonical return fields, statuses and conditional payloads; this file declares only the package transport around them. It adds no status, no wire field and no reduced schema.

## Role returns

Every role ends with one JSON object as its final message: `phase`, `role`, `status`, a nonempty `summary`, `runId`, `inputIdentity`, `candidateIdentity`, `contractVersion` and real `evidence`, plus the full payload its phase and status require. Optional facts that are genuinely absent are omitted, never null or placeholder text. This package binds `contractVersion` to `methodology-claude/1.0.0` and spells phases in lowercase: `bootstrap`, `architect`, `code`, `qa`, `review`, `debug`, `finalize`.

The parent extracts the object, then validates shape, types and conditional fields, the current identities, artifact existence and containment, scope, independence and semantic acceptance, and only then records it. In the Workflow spine the per-phase JSON Schema performs the structural part through StructuredOutput; the rest stays the parent's judgment.

Phase payloads, in brief (the owner text is authoritative):

- Bootstrap SUCCESS: `isEmpty`, `classificationHint`, `fileCount`, `files` (path, summary, structure, relevance), `recommendations` and map evidence.
- Architect SUCCESS: `classification`, `projectType`, `taskType`, `planPath`, slices, scope (`mayEdit`, `doNotTouch`), acceptance criteria, `specDeficiencies`, `specBlocked`, `visualGate`. A human-blocked specification or a failed required visual gate refuses Code.
- Code SUCCESS: artifacts, `testGuidePath`, `testSummary`, deviations, acceptance and log evidence, and the final Doxygen build evidence. Code BUG_REPORT and QA BUG_REPORT carry a populated `bugReport` with `goal`, `actual`, `logAnalysis`, `dataAnalysis`, `hypothesis`, `recommendation`. BLOCKED names the reason, limitations and evidence.
- QA: `testSummary`, `scans`, `findings`, `limitations`. `scans` is a LIST of exactly eight objects with `id`, `status` (PASS, FAIL, N/A, BLOCKED), a nonempty `reason` and real `evidence`, one each for `green-test-trap`, `quantitative-ac`, `semantic-trace`, `infra-dod`, `side-effect-channel`, `secret-leak`, `real-path-shape`, `discriminating-test`. No dict, no ordinals, no duplicates, no extras. Any required FAIL or BLOCKED prevents SUCCESS.
- Review: independent findings, evidence, whole-diff and scope judgment, limitations.
- Debug FIXED: `rootCause`, `fix`, `filesTouched`, `postFixAudit`, `testSummary`, regression evidence and the consumed entry. FIXED always renews QA.
- Finalize SUCCESS: the RETURN-801 report fields. ESCALATED_FINALIZE carries `requiredRepair` and the failure evidence; Finalize never repairs silently.

A legitimate written host prohibition of Doxygen in a Code return is exactly:

```text
doxygen={status:'NOT_APPLICABLE',reason,prohibition:{path,quote},evidence,candidateIdentity,inputIdentity}
```

`path` is the real target rule file, `quote` its exact written prohibition naming Doxygen. Absence of a Doxyfile, a missing tool or "not needed" is not a prohibition.

## Record input

The root records a verified role return with:

```json
{"kind":"role","result":{"phase":"code","role":"coder","status":"SUCCESS","summary":"schematic only; the real record carries the complete canonical return"},"context":{"sourceChange":{"mayEdit":["target-relative-owned-path"],"artifacts":["/absolute/real/authorized/artifact"]}}}
```

This schematic is not a valid return. Evidence must be an existing regular file inside the target: a judge's files from its scratch root outside the target are first copied (no links, no overwrite) into `<target>/.methodology/evidence/<run-id>/<nn>-<phase>/`, and the record cites the copies; the Workflow recorder does this itself, the interactive root does it by hand. `context.sourceChange` is required for Code SUCCESS and Debug FIXED, and for an observed partial Code BUG_REPORT/BLOCKED or Debug BLOCKED that changed target bytes. It is scope evidence, not permission: the helper derives the new candidate digest from the actual bytes and checks the change against the intersection of the accepted Architect scope and the supplied `mayEdit`.

A parent response-correction event is separate from a role result:

```json
{"kind":"control","event":"response-correction","phase":"qa","reason":"actual extraction or schema failure","evidence":["/absolute/real/diagnostic"],"unknownEffect":false}
```

One correction per phase attempt. `unknownEffect: true` refuses replay until the parent has investigated the actual effects. A worker flag never supplies this control.

## Helper

`skills/feature-dev/scripts/run_state.py` (schema 2):

- `initialize(project, spec, approval, run_id, max_debug=4, *, framework, adapter, plan)` returns `(state_path, state)`;
- `advance(state, result)` returns a new state and leaves the input untouched on refusal;
- `save(path, state)` stores atomically;
- CLI `init`, `show`, `record` (see the [runtime](claude-runtime.md)). Success prints JSON and exits 0; a refusal exits 2 with a safe diagnostic on stderr while accepted progress and counters stay unchanged.

The helper binds the package identity (`methodology-claude` 2.1.0, profile `colocated-in-place`, the declared layout equal to the actual members, the six core owners as drafts, the neutral 71-file population and the eight-scan registry) and refuses stale, mismatched, terminal, old-schema or malformed input.

The candidate identity follows `flow/run-state.md` STATE-102: tracked plus untracked content that git does not ignore. For a target that is the top level of its own git work tree the helper asks git read-only and hermetically (`git --no-optional-locks -c core.fsmonitor=false ls-files --others --ignored --exclude-standard --directory`, with inherited `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` and similar variables removed) which paths are ignored and skips them, so hook counters, maps and environments the project ignores never change the candidate. The regenerable names `doxygen_output`, `output`, `__pycache__` and `.pytest_cache` (and `.git`, `.methodology`) are always excluded as well. A target that is not its own work-tree top level uses a declared fallback list (those names plus common caches, virtual environments and the Anti-Loop counter files); a generated directory outside that list then counts as candidate content and must be listed in MAY EDIT. A confirmed repository whose ignore enumeration fails is refused, never downgraded. It launches no agents, sandboxes no tools and cannot authenticate an approval string.

## Workflow recorder

The Workflow spine `/methodology-claude:feature-dev-workflow` cannot touch files. Its arguments are `{spec, target, plan, approval, runId, framework, scratch, maxDebug?, dialogLang?, recordState?}`. `scratch` is required: a real, resolved absolute path under `/tmp`, `/private/tmp`, `/var/folders` or `/private/var/folders`, disjoint from the target in both directions; it is where the judges write. All paths use only ASCII letters, digits and `. _ - / + @ = : ,`; anything else ends in ERROR before an agent runs. The root runs `init` before starting the spine (with `--max-debug` equal to `maxDebug`, at most 4) and `show` after it ends.

Writers (architect, coder, debugger) keep run logs, probes and the final report under the excluded evidence home `<target>/.methodology/evidence/<run-id>/`. Judges (qa, reviewer) never write inside the target (`roles/qa.md` QA-204, QA-206): each creates and writes only `<scratch>/<run-id>/<nn>-<phase>/` (`mkdir -p` first) and cites those files as evidence; when a judge reruns a plan command it sends the output there, never to the evidence home. The plan's Runtime Commands carry no fixed output sink inside the target. `/tmp` and `/private/tmp` (and `/var` and `/private/var`) count as one tree in the scratch checks; several runs may share one scratch root. The searcher writes nothing.

After each accepted phase the spine dispatches a recorder step (`general-purpose`, `haiku`) that:

1. writes the record JSON verbatim to `<target>/.methodology/runs/<run-id>/pending/<nn>-<phase>.json` and prints its length and code-unit checksum, which the spine compares with its own; this detects a transcription mismatch only, it does not prove what the helper read (a mismatch ends BLOCKED, kind `integrity`, and the helper is not run);
2. prechecks and imports: every cited path must be an existing regular file inside the target (deleted touched paths are pruned; a Debug fix keeps at least one surviving regression file); judges' scratch files are copied to `<target>/.methodology/evidence/<run-id>/<nn>-<phase>/` (collision-safe names, compared case-insensitively; nothing is copied unless every cited path passes) and the record, already rewritten by the spine, cites those copies; a missing source, a link or an existing destination stops before the helper with the one response correction;
3. runs `run_state.py record` and returns the exit code and the last 4000 characters of stderr, which end with the helper's `methodology state:` reason.

A nonzero helper exit ends the run BLOCKED with that reason and a `ledgerNote` that `show` keeps refusing while the target holds unrecorded edits; the root investigates (`git status --porcelain -uall`, the diff against the last accepted candidate) before any replay. Every unusable role return is recorded as the helper's `response-correction` control event with a diagnostic file under `pending/`; the second one lands in the ledger as BLOCKED, or ESCALATED_FINALIZE in Finalize. A thrown or lost role agent is a transport failure: BLOCKED with `transportFailure`, never replayed, because the declared transport retry limit is zero and the effect is unknown. A thrown or unusable recorder leaves the ledger outcome unknown: on a progress record or a correction episode the run ends BLOCKED, never ESCALATED_FINALIZE and never continued: a thrown recorder gives `ledger.kind` `transport` with `transportFailure.channel` `recorder`, an unusable recorder answer gives `ledger.kind` `unknown` without `transportFailure`. Outcomes the helper cannot represent (SPEC_BLOCKED, VISUAL_GATE_FAIL, a scope-deviation or UI-discrepancy halt, a control event while the Architect's plan is still pending) come back with a `ledgerNote` that says what the ledger shows and what the root must record. `recordState: false` is a diagnostic and test mode with no durable ledger and placeholder identities. Roles cite regular files only; the Doxygen map is cited as `<map>/index.xml`.

## Consequential decision packet

At the consequential-open trigger load full `prompting/brainstorm.md` through the current adapter binding. The authorized root coordinates its independent packet using the actual native collaboration mechanism; inner roles request it. Carry existing evidence references in the brief/plan/DEC/task, never a new canonical field or phase. Missing required proof holds dependent readiness; preserve reasoned routine/settled/forced exclusions and actual actor/source limits.
