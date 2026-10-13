---
id: checks.qa-scans
title: QA scans
status: draft
---

# QA scans

<!-- anchor: checks.qa-scans.registry -->

## Registry

| Scan id | Applicability |
|---|---|
| green-test-trap | Always. |
| quantitative-ac | Always examine the acceptance map; measurements apply when numeric thresholds exist. |
| semantic-trace | Always, with backend edit-local instrumentation and UI accessibility assertions where applicable. |
| infra-dod | When task, plan or requirements promise container startup, compose/run, curl or wget endpoints, healthcheck, healthy state, reachable service, endpoint HTTP code or availability on a port, including equivalent dialog-language phrases. |
| side-effect-channel | When a channel is a DoD deliverable or crosses a process/container boundary; pure logic with pytest-process stdout may be N/A. |
| secret-leak | Always, before the suite for files and after evidence-producing execution for streams. |
| real-path-shape | By slice class: real-path when shipping an entry point, real-shape when consuming an artifact family; assess both clauses independently. |
| discriminating-test | Always, once per acceptance-map row. |

- **SCAN-101** MUST: Run mandatory preflight text checks before the suite is trusted, then runtime-dependent scans after their evidence-producing operations; a green suite alone is not SUCCESS and any failed applicable scan is a Bug Report.
- **SCAN-102** MUST: Use stable named scan ids in prompts, skills, verdicts and tests rather than ordinals; the registry is the single authority, and a two-directional equality check rejects extra or missing ids in any consumer.
- **SCAN-103** MUST: Account for every registry id in the verdict as PASS, FAIL, N/A or BLOCKED with reason and evidence; a spine's applicability hint cannot drop an id, and the orchestrator treats a missing id as a skipped scan requiring explanation.
- **SCAN-104** MUST: Declare each scan's applicability class and record a nonapplicable scan N/A with its trigger-based reason rather than omit it.
- **SCAN-105** MUST: Represent one structured item per finding through {{cap:structured-output}}, with scan, code, severity, message and evidence locations rather than a count in prose.
- **SCAN-106** SHOULD: Keep each scan's neutral failure-class rationale as well as its procedure; skipping a scan for speed silently removes the guarantee it closes.
- **SCAN-107** SHOULD: Give QA the coder's final-message path or mark it absent via {{cap:workflow-orchestration}}; scan readers of deferred declarations and measured lines record absence without inventing report contents.
- **SCAN-108** MUST: For each mock, stub, caplog, capsys, in-memory transport, mocked HTTP server or driver whose channel is a DoD deliverable or crosses a process/container boundary, run the corresponding real-environment probe; semantic capture is necessary but not sufficient, while pure logic with pytest-process stdout needs only the visible test trace.
- **SCAN-109** SHOULD: Distinguish Green-Test-Trap, where a skip or NotImplemented stub asserts nothing; Mock-Channel-Trap, where captured API output never reaches its real sink; and the vacuous-test class, where a present test cannot discriminate a reverted behavior.
- **SCAN-110** SHOULD: Use command execution and observed output as Chain-of-Verification rather than recalling a presumed answer.
- **SCAN-111** MUST: Return BUG_REPORT when any applicable scan fails, regardless of the suite exit code; an environment or authorization gap instead uses BLOCKED and cannot be passed.
- **SCAN-112** MUST: Use PASS, FAIL, N/A and BLOCKED scan statuses with reason and evidence; BLOCKED means the check could not run in the permitted environment and is never PASS.
- **SCAN-113** MUST: Let scans create ordinary artifacts only in authorized isolated resources or a QA copy without .git, using {{cap:launch-environment}} and {{cap:role-permissions}}; probes do not authorize arbitrary writes or external messages.
- **SCAN-114** MUST: Keep eight named scans in the registry: green-test-trap, quantitative-ac, semantic-trace, infra-dod, side-effect-channel, secret-leak, real-path-shape and discriminating-test; SUCCESS requires every applicable scan to pass and every other scan recorded N/A with its reason.
- **SCAN-115** MUST: Declare an absent scan in the adapter with a reason and trigger, adopt it after a control run on pilots shows no false positives, and require conformance reporting of any undeclared gap; a structural file/anchor conformance result alone does not establish that the semantic scan-absence obligation is implemented.

<!-- anchor: checks.qa-scans.green-test-trap -->

## Green test trap

- **SCAN-225** MUST: Purpose: Stop a green suite from claiming coverage from skipped or unimplemented tests.
- **SCAN-226** MUST: Applicability: Always.
- **SCAN-227** MUST: Evidence: Location of each stub hit and coder declaration or explicit absence.
- **SCAN-228** MUST: Verdict: FAIL/HIGH GREEN_TEST_TRAP for undeclared stubs; declared deferral contributes no accepted coverage. Required unverified coverage prevents SUCCESS.

<!-- anchor: checks.qa-scans.green-test-trap.procedure -->

## Green test trap — procedure

- **SCAN-201** MUST: Before the suite, search every project test file, including tests outside the conventional tests directory, for Python forms `@pytest\.mark\.skip` and `raise NotImplementedError` through {{cap:check-runner}}; the skip prefix includes skipif, and matches identify coverage hidden by skipped stubs.
- **SCAN-202** MUST: Search JS/TS test/spec files for the pattern `\b(it|test|describe)\.(skip|todo|fixme)\(|\bxit\(|\bxdescribe\(`, excluding dependency and generated folders such as node_modules, dist, build and virtual environments.
- **SCAN-203** MUST: For each hit, cross-check the coder's final report and Deviations: a declared TEST_DEFERRED needs reason, required infrastructure, exact run command and acceptance mapping; it is disclosed but covers no accepted criterion, and QA runs it where environment and authorization permit, otherwise marks the required criterion unverified and blocks SUCCESS.
- **SCAN-204** MUST: Report HIGH GREEN_TEST_TRAP for an undeclared hit, a hit without a reason, or a NotImplementedError test body; a skipped empty assertion never becomes evidence through declaration alone.
- **SCAN-205** MUST: Subtract every skipped criterion from satisfied acceptance counts; a skip never covers a criterion.
- **SCAN-206** MUST: Require the coder's final-message input for declaration cross-checks and record absent if it was not supplied rather than infer an undeclared report value.
- **SCAN-207** SHOULD: Extend Python detection to pytest.skip in a body, importorskip, unittest.skip and xfail so language-pattern gaps are visible without asserting these forms are failures when legitimately declared.

<!-- anchor: checks.qa-scans.quantitative-ac -->

## Quantitative ac

- **SCAN-325** MUST: Purpose: Measure promised counts, latency or size rather than infer them from structure.
- **SCAN-326** MUST: Applicability: Always examine the acceptance map; measurements apply when numeric thresholds exist.
- **SCAN-327** MUST: Evidence: Per criterion: operator, threshold, actual value, command and output, or justified absence of a numeric threshold.
- **SCAN-328** MUST: Verdict: FAIL AC_UNMAPPED on missing criterion rows or AC_QUANTITATIVE_FAIL on a violated bound or equality; absent required evidence is unverified.

<!-- anchor: checks.qa-scans.quantitative-ac.procedure -->

## Quantitative ac — procedure

- **SCAN-301** MUST: Extract quantitative criteria from both plan and task: ≥, ≤, exactly, at least and at most, together with the forms of {{param:dialog-language}} such as minimum and maximum; a lower bound fails below it, an upper bound above it and exactly at every unequal value.
- **SCAN-302** MUST: Locate every acceptance criterion's covering tests through the test-guide map, using behavioral test names rather than grepping source code for criterion ids; a deferred-only row is unsatisfied and must be executed by its declared command where possible or reported unverified without SUCCESS.
- **SCAN-303** MUST: Report AC_UNMAPPED for an acceptance criterion with no mapped test, TEST_DEFERRED row or justified N/A row.
- **SCAN-304** MUST: Check that each quantitative criterion has a coder report line giving its id, measured value, threshold and met/not-met outcome rather than a qualitative claim.
- **SCAN-305** MUST: Run the measurement through {{cap:check-runner}} when the coder line is absent: use the documented SQL count, line count, healthy-service count, test collection, log query, file size or process-state command appropriate to the criterion, and record actual output.
- **SCAN-306** MUST: Report AC_QUANTITATIVE_FAIL with criterion, actual value and threshold when the bound or equality in SCAN-301 is violated, even if tests passed.
- **SCAN-307** MUST: Say all measurable criteria pass only when each produced an actual number compared to its required operator; file presence, typecheck or structural readiness cannot prove count, size or latency.

<!-- anchor: checks.qa-scans.semantic-trace -->

## Semantic trace

- **SCAN-425** MUST: Purpose: Prove critical operations and their correct path, closing cosmetic passes and swallowed-error passes.
- **SCAN-426** MUST: Applicability: Always, with backend edit-local instrumentation and UI accessibility assertions where applicable.
- **SCAN-427** MUST: Evidence: Mapped test traces, unexpected-error inventory, owned-code markup checks and UI observable assertions or live snapshots.
- **SCAN-428** MUST: Verdict: FAIL SEMANTIC_TRACE_MISSING, UNEXPECTED_ERROR_TRACE, LDD_MISSING, EXOSKELETON_MISSING or EXOSKELETON_MISPLACED on the corresponding missing or erroneous guarantee.

<!-- anchor: checks.qa-scans.semantic-trace.procedure -->

## Semantic trace — procedure

- **SCAN-401** MUST: For every criterion backed by a real non-deferred mapped test, find that test's trace in the log at the supplied absolute path.
- **SCAN-402** MUST: Confirm at least one importance 7 through 10 trace for the criterion's critical operation, such as a database write, validation or state transition; search both bracket IMP records and structured imp/func/block fields before concluding absence, using the host's logging encoding.
- **SCAN-403** MUST: Report SEMANTIC_TRACE_MISSING when a green test lacks the critical-path trace or a UI test lacks its required observable state; a correct result alone can be a cosmetic pass.
- **SCAN-404** MUST: Scan the passing run for ERROR/CRITICAL records not declared expected by a test and report UNEXPECTED_ERROR_TRACE with test and count; a swallowed exception in a green run is still a defect.
- **SCAN-405** MUST: Check owned backend LDD by edit locality: a new function's meaningful control flow and new branches, I/O or error paths in an existing function need their own trajectory, while trivial changes and generated migrations are exempt; report LDD_MISSING even if surrounding untouched code is unlogged, since the host controls encoding rather than presence.
- **SCAN-406** MUST: Reject borrowed wrapper, decorator, middleware or guard-helper logs as a substitute for the module's own introduced control flow; do not retrofit untouched branches as the price of editing a function.
- **SCAN-407** MUST: Check full exoskeleton on every new backend module including new tests, and entity-local markup on touched functions of existing modules; generated migration files are exempt, and absence needs a quoted explicit host prohibition, never an unlogged neighborhood or an unquoted house-style claim, otherwise report EXOSKELETON_MISSING.
- **SCAN-408** MUST: For each new module, verify module contract first above imports, with GREP_SUMMARY and STRUCTURE as the last in-contract tags before the Doxygen anchor or region end; standalone lines are valid only in pre-existing modules, no redundant module docstring precedes the contract, and a repository without Doxyfile omits the anchor rather than suppress E402; report EXOSKELETON_MISPLACED for violations.
- **SCAN-409** MUST: Verify that the route to the result was correct and critical operations happened, rather than infer trajectory from the final value.
- **SCAN-410** MUST: For every UI-facing criterion, require an assertion on rendered output or accessibility snapshot of role, accessible name and state, or a stable test-id anchored state; client code carries no backend LDD, and a component function merely returning is insufficient semantic evidence.
- **SCAN-411** SHOULD: When the frontend runs and {{cap:browser}} is available, navigate to the tested route, perform the user action and capture the live accessibility snapshot verifying the named role and resulting state.
- **SCAN-412** MUST NOT: Claim visual fidelity such as layout or color through this scan; name the pending human screenshot/prototype review separately in the verdict.
- **SCAN-413** MUST NOT: Use mocked outputs alone to claim the actual execution path occurred.
- **SCAN-414** SHOULD: Read semantic trace from the declared log file so a quiet suite can preserve evidence; for an in-process test stdout sink, record the documented verbose run that exposes the trace.

<!-- anchor: checks.qa-scans.infra-dod -->

## Infra dod

- **SCAN-525** MUST: Purpose: Prove a promised service or container actually starts and serves its endpoints; mocked-driver business logic cannot establish runtime readiness.
- **SCAN-526** MUST: Applicability: When task, plan or requirements promise container startup, compose/run, curl or wget endpoints, healthcheck, healthy state, reachable service, endpoint HTTP code or availability on a port, including equivalent dialog-language phrases.
- **SCAN-527** MUST: Evidence: Actual image-tool preflight, port listener check, stack-state snapshot, endpoint expected/actual HTTP codes, failure logs and owned-cleanup record.
- **SCAN-528** MUST: Verdict: FAIL with INFRA_HEALTHCHECK_BROKEN, INFRA_STACK_FAILED, INFRA_ENDPOINT_FAIL or INFRA_PORT_HARDCODED for implementation faults; BLOCKED with INFRA_DOD_NOT_VERIFIED for environment or authorization gaps; N/A only without runtime DoD.

<!-- anchor: checks.qa-scans.infra-dod.procedure -->

## Infra dod — procedure

- **SCAN-501** MUST: Treat mocks as business-logic evidence only; they cannot confirm an infrastructural DoD and cannot replace its runtime steps.
- **SCAN-502** MUST: Before launching container infrastructure, check each healthcheck's required executable in its actual image through {{cap:check-runner}}; for shell images a command-v curl/wget check is appropriate, and an image lacking its required utility is HIGH INFRA_HEALTHCHECK_BROKEN because that healthcheck will fail indefinitely.
- **SCAN-503** MUST: Before launch, inspect the configured host port for listeners with the documented port command, and flag a colliding fixed host mapping without a configurable variable as MEDIUM INFRA_PORT_HARDCODED, recording the port and conflicting process without private data.
- **SCAN-504** MUST: Start the isolated container stack with the documented wait-for-health command, equivalent to compose up -d --wait --wait-timeout 120 where supported; an unhealthy or unstarted service at timeout is INFRA_STACK_FAILED with stack-state output and its last 100 service log lines, redacted.
- **SCAN-505** MUST: Probe every DoD endpoint through the real runtime with the documented request command, comparing actual to expected HTTP code; mismatch is INFRA_ENDPOINT_FAIL with redacted endpoint identity and actual/expected codes.
- **SCAN-506** MUST: Always tear down probe-owned resources after endpoint and applicable channel verification, even on failure; never remove shared volumes or tear down a stack the probe did not start, and record cleanup failures without widening ownership.
- **SCAN-507** MUST: Accept infrastructural done criteria only when image preflight where applicable, port handling, startup readiness, endpoint verification and owned teardown completed without implementation failures.
- **SCAN-508** MUST: When the DoD names a runtime service without containers, replace image and container-start steps with the plan's run command and readiness wait, then probe endpoints and stop only the owned process; do not require containers unless the DoD names them.
- **SCAN-509** MUST: Report INFRA_DOD_NOT_VERIFIED when the required stack never ran, distinguishing BUG_REPORT for software failure from BLOCKED for missing permitted environment or authorization; business logic verified alone never satisfies runtime DoD.
- **SCAN-510** MUST: Run documented infrastructure probes only in isolated permitted resources and select the container procedure only when the DoD requires containers.

<!-- anchor: checks.qa-scans.side-effect-channel -->

## Side effect channel

- **SCAN-625** MUST: Purpose: Verify observable logging, metrics, events or audit delivery at the real sink, closing Mock-Channel-Trap.
- **SCAN-626** MUST: Applicability: When a channel is a DoD deliverable or crosses a process/container boundary; pure logic with pytest-process stdout may be N/A.
- **SCAN-627** MUST: Evidence: Delivery-contract reference, real trigger command, real sink query and observed marker/outcome.
- **SCAN-628** MUST: Verdict: FAIL SIDE_EFFECT_CHANNEL_UNWIRED for missing delivery or DELIVERY_CONTRACT_MISSING for absent path; BLOCKED for unavailable environment or required external-send authorization.

<!-- anchor: checks.qa-scans.side-effect-channel.procedure -->

## Side effect channel — procedure

- **SCAN-601** MUST: Confirm delivery through the configured production-equivalent channel and real sink, because semantic traces, caplog, capsys and mock capture prove only a channel API call; a missing logging configuration or handler is invisible to such capture.
- **SCAN-602** MUST: Trigger the behavior through its real permitted entry point, such as the documented request after stack readiness, actual module entry or CLI, rather than pytest.
- **SCAN-603** MUST: Observe the actual sink named by the delivery contract after the trigger, such as service logs since the action, real stdout/file, metric, event or audit query; if the expected marker is absent, report HIGH SIDE_EFFECT_CHANNEL_UNWIRED with channel and sink identity, without sensitive content.
- **SCAN-604** MUST: Back-check the plan's delivery contract for sink and mechanism whenever a criterion or invariant declares the channel; absent delivery path is DELIVERY_CONTRACT_MISSING.
- **SCAN-605** MUST: Count the channel DoD as satisfied only after the expected output is confirmed at its real sink.
- **SCAN-606** MAY: Use the visible pytest trace alone for pure in-process logic whose sink is pytest stdout; mark this scan N/A with that scope reason instead of requiring a redundant delivery probe.
- **SCAN-607** MUST: Require explicit authorization for a probe that sends to a third party; absence is BLOCKED and testing does not grant messaging permission.
- **SCAN-608** SHOULD: For containers, perform side-effect delivery verification after the infrastructure endpoint probe while the stack is running and before its teardown; teardown first destroys the sink this scan needs.

<!-- anchor: checks.qa-scans.secret-leak -->

## Secret leak

- **SCAN-725** MUST: Purpose: Catch credentials leaked as literals or through a stream, including INFO request URLs.
- **SCAN-726** MUST: Applicability: Always, before the suite for files and after evidence-producing execution for streams.
- **SCAN-727** MUST: Evidence: Only file/stream identity, line and redacted credential class; never matched values.
- **SCAN-728** MUST: Verdict: FAIL/HIGH SECRET_LEAK for a real credential literal or channel leak; environment indirection and documented placeholder values do not fail.

<!-- anchor: checks.qa-scans.secret-leak.procedure -->

## Secret leak — procedure

- **SCAN-701** MUST: Before running the suite, scan the target for the provider-class example bot[0-9]{6,}:[A-Za-z0-9_-]{20,}, excluding dependency folders, virtual environments, git metadata and generated/cache directories; use a location-only scanner through {{cap:check-runner}} so output cannot echo credential values.
- **SCAN-702** MUST: Scan generic credential literals with the provider-class example `(api[_-]?key|secret|token|password|passwd)[[:space:]]*[:=][[:space:]]*[A-Za-z0-9_./+=-]{16,}` across source and tracked text including py, ts, js, toml, yaml, yml, json, md, log, txt, .env files, sh, cfg, ini, Dockerfile and compose files; parameterize provider patterns, exclude dependencies and git, and return locations only.
- **SCAN-703** MUST: Report a real literal hit as HIGH SECRET_LEAK with file and line; environment indirection such as environment-variable access and documented fixture placeholders are not literal leaks, but a real secret may never appear as a tracked literal.
- **SCAN-704** MUST: Inspect changed source, tests, tracked surfaces and relevant logs and report only file, line and redacted credential class, never the secret value; include stream output after execution rather than trusting only a pre-suite grep.
- **SCAN-705** MUST: After suite and service probes, inspect their captured streams and real service logs for credentials crossing a channel, including request-URL INFO logs; a stream token is a leak even if no source literal matched.

<!-- anchor: checks.qa-scans.real-path-shape -->

## Real path shape

- **SCAN-825** MUST: Purpose: Prove a shipped command works and consumed real inputs have the supported shape, closing the library-only green-test trap.
- **SCAN-826** MUST: Applicability: By slice class: real-path when shipping an entry point, real-shape when consuming an artifact family; assess both clauses independently.
- **SCAN-827** MUST: Evidence: Acceptance-map row and actual real invocation or corpus artifact test output, with declared deferral when corpus is unavailable.
- **SCAN-828** MUST: Verdict: FAIL GREEN_TEST_TRAP under real-path-shape for an unmet applicable clause; BLOCKED when a required declared artifact cannot be verified, N/A only when neither clause applies.

<!-- anchor: checks.qa-scans.real-path-shape.procedure -->

## Real path shape — procedure

- **SCAN-801** MUST: When the slice ships a CLI, script or entry point, require at least one acceptance-map test exercising the real entry end-to-end through its actual invocation rather than only an import or the library functions it wraps.
- **SCAN-802** MUST: When the slice consumes an input-artifact family, require at least one test consuming a real artifact from its own corpus rather than only an in-process synthetic fixture; a missing ignored artifact can be skip-guarded only with a TEST_DEFERRED declaration containing reason, prerequisite, command and criterion mapping, and still does not cover acceptance.
- **SCAN-803** MUST: When neither real-entry nor artifact-consumption clause applies, record real-path-shape as N/A with the library-only reason, retaining its id in the verdict.
- **SCAN-804** MUST: Fail any unmet applicable real-path or real-shape clause with GREEN_TEST_TRAP under scan id real-path-shape and return BUG_REPORT; green library tests alone cannot prove either clause.
- **SCAN-805** SHOULD: Make the producer's test-guide map explicit about the real entry and artifact, matching the recognizer so coverage is authored with knowledge of what QA reads.

<!-- anchor: checks.qa-scans.discriminating-test -->

## Discriminating test

- **SCAN-925** MUST: Purpose: Detect a test that executes real code and sink but constrains nothing because its scenario cannot exhibit the covered defect.
- **SCAN-926** MUST: Applicability: Always, once per acceptance-map row.
- **SCAN-927** MUST: Evidence: Per criterion: quoted assertion and reasoned answer to whether reverting the behavior makes it fail, including real-shape/default and threshold checks.
- **SCAN-928** MUST: Verdict: FAIL VACUOUS_TEST when a covering assertion would stay green after reversion; every row must discriminate for SUCCESS.

<!-- anchor: checks.qa-scans.discriminating-test.procedure -->

## Discriminating test — procedure

- **SCAN-901** MUST: For each acceptance-map row ask whether its covering assertion would fail if the covered behavior were reverted; an assertion passing either way is VACUOUS_TEST, even with real code and sink.
- **SCAN-902** MUST NOT: Mutate the candidate to answer the reversion question; the read-only judge reasons from the assertion and scenario.
- **SCAN-903** MUST: Bound discriminating-test verification to one reversion question per acceptance-map row rather than an audit of every test.
- **SCAN-904** MUST: Compare fixture or double defaults with the real vendor, parser or database's actual shape; flag defaults that encode a production state never taken, because deleting the real branch could leave the artificial scenario green.
- **SCAN-905** MUST: Look for guards unreachable because an earlier layer now enforces them, and scenarios with less seeded data than the threshold under test, such as fewer rows than a page limit; neither can expose the intended failure.
- **SCAN-906** MUST: Require every acceptance-map row's covering assertion to discriminate its covered behavior before SUCCESS.
- **SCAN-907** MUST: Report a defect even with every test green when a no-unexpected-errors assertion observes an empty capture, including when logger defaults silently suppress records; absence of records cannot establish correct behavior.

<!-- anchor: checks.qa-scans.codes -->

## Codes

One stable code table covers scan findings, isolation/verdict checks and producer evidence.

| Code | Scan or contract | Severity / class | Meaning |
|---|---|---|---|
| `GREEN_TEST_TRAP` | green-test-trap; real-path-shape | HIGH | Undeclared skip or unimplemented test, or unmet real entry/artifact coverage. |
| `AC_UNMAPPED` | quantitative-ac | by impact | Acceptance criterion missing from the coverage map. |
| `AC_QUANTITATIVE_FAIL` | quantitative-ac | by impact | Measured lower/upper/equality requirement violated. |
| `SEMANTIC_TRACE_MISSING` | semantic-trace | by impact | Critical operation trace or required observable UI assertion absent. |
| `UNEXPECTED_ERROR_TRACE` | semantic-trace | by impact | Passing run contains ERROR/CRITICAL records that no test declares expected. |
| `LDD_MISSING` | semantic-trace | by impact | Owned introduced backend control flow lacks its LDD trajectory. |
| `EXOSKELETON_MISSING` | semantic-trace | by impact | Required module or edit-local entity markup absent without explicit host prohibition. |
| `EXOSKELETON_MISPLACED` | semantic-trace | by impact | New-module contract or navigation tags violate placement requirements. |
| `INFRA_HEALTHCHECK_BROKEN` | infra-dod | HIGH | Image lacks the executable required by its healthcheck. |
| `INFRA_STACK_FAILED` | infra-dod | by impact | A required service never becomes started or healthy within the startup wait. |
| `INFRA_ENDPOINT_FAIL` | infra-dod | by impact | Real endpoint response differs from its promised HTTP code. |
| `INFRA_PORT_HARDCODED` | infra-dod | MEDIUM | A fixed nonconfigurable host port collides with a listener. |
| `INFRA_DOD_NOT_VERIFIED` | infra-dod | by impact | Required stack never ran; BLOCKED for environment/authorization, BUG_REPORT for implementation failure. |
| `SIDE_EFFECT_CHANNEL_UNWIRED` | side-effect-channel | HIGH | Expected delivery absent from the real sink despite capture evidence. |
| `DELIVERY_CONTRACT_MISSING` | side-effect-channel | by impact | Declared channel lacks its sink/mechanism delivery contract. |
| `SECRET_LEAK` | secret-leak | HIGH | Actual credential literal or stream exposure, reported only as redacted class and location. |
| `VACUOUS_TEST` | discriminating-test | by impact | Covering assertion stays green when its covered behavior is reverted. |
| `QA_MUTATED_FILES` | isolation | by impact | Judge changed original files or git state; if no QA phase ran, its retrospective check is N/A. |
| `MALFORMED_VERDICT` | verdict shape | by impact | Machine envelope violates contract, including BUG_REPORT without populated bugReport. |
| `TEST_DEFERRED` | producer marker; green-test-trap | not a finding | Declared unavailable test with reason, prerequisite, command and criterion mapping; no satisfied coverage while deferred. |
| `EXTERNAL_DEPENDENCY / HALLUCINATION_RISK` | producer classifications | not a new scan | Verified or unresolved external identifier evidence; no new QA recognizer is introduced by this table. |

- **SCAN-1001** MUST: Use the single table in this section for every finding code, carrying both stable code and scan id; GREEN_TEST_TRAP identifies undeclared skips or unimplemented tests under green-test-trap, and unmet real-entry or real-artifact coverage under real-path-shape, with HIGH severity.
- **SCAN-1002** MUST: Use AC_UNMAPPED for Acceptance criterion missing from the coverage map. under quantitative-ac; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1003** MUST: Use AC_QUANTITATIVE_FAIL for Measured lower/upper/equality requirement violated. under quantitative-ac; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1004** MUST: Use SEMANTIC_TRACE_MISSING for Critical operation trace or required observable UI assertion absent. under semantic-trace; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1005** MUST: Use UNEXPECTED_ERROR_TRACE for Passing run contains ERROR/CRITICAL records that no test declares expected. under semantic-trace; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1006** MUST: Use LDD_MISSING for Owned introduced backend control flow lacks its LDD trajectory. under semantic-trace; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1007** MUST: Use EXOSKELETON_MISSING for Required module or edit-local entity markup absent without explicit host prohibition. under semantic-trace; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1008** MUST: Use EXOSKELETON_MISPLACED for New-module contract or navigation tags violate placement requirements. under semantic-trace; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1009** MUST: Use INFRA_HEALTHCHECK_BROKEN for Image lacks the executable required by its healthcheck. under infra-dod; severity HIGH.
- **SCAN-1010** MUST: Use INFRA_STACK_FAILED for A required service never becomes started or healthy within the startup wait. under infra-dod; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1011** MUST: Use INFRA_ENDPOINT_FAIL for Real endpoint response differs from its promised HTTP code. under infra-dod; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1012** MUST: Use INFRA_PORT_HARDCODED for A fixed nonconfigurable host port collides with a listener. under infra-dod; severity MEDIUM.
- **SCAN-1013** MUST: Use INFRA_DOD_NOT_VERIFIED for Required stack never ran; BLOCKED for environment/authorization, BUG_REPORT for implementation failure. under infra-dod; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1014** MUST: Use SIDE_EFFECT_CHANNEL_UNWIRED for Expected delivery absent from the real sink despite capture evidence. under side-effect-channel; severity HIGH.
- **SCAN-1015** MUST: Use DELIVERY_CONTRACT_MISSING for Declared channel lacks its sink/mechanism delivery contract. under side-effect-channel; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1016** MUST: Use SECRET_LEAK for Actual credential literal or stream exposure, reported only as redacted class and location. under secret-leak; severity HIGH.
- **SCAN-1017** MUST: Use VACUOUS_TEST for Covering assertion stays green when its covered behavior is reverted. under discriminating-test; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1018** MUST: Use QA_MUTATED_FILES for Judge changed original files or git state; if no QA phase ran, its retrospective check is N/A. under isolation; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1019** MUST: Use MALFORMED_VERDICT for Machine envelope violates contract, including BUG_REPORT without populated bugReport. under verdict shape; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1020** MUST: Use TEST_DEFERRED for Declared unavailable test with reason, prerequisite, command and criterion mapping; no satisfied coverage while deferred. under producer marker; green-test-trap; classify severity by impact for findings, and retain producer markers as evidence only.
- **SCAN-1021** MUST: Use EXTERNAL_DEPENDENCY / HALLUCINATION_RISK for Verified or unresolved external identifier evidence; no new QA recognizer is introduced by this table. under producer classifications; classify severity by impact for findings, and retain producer markers as evidence only.

<!-- anchor: checks.qa-scans.producer-mirror -->

## Producer mirror

- **CODER-901** MUST: Verify each new external identifier using the project's declared dependency-verification command or a real package-version query, image-manifest check, import of the actual library symbol or endpoint request as appropriate through {{cap:check-runner}}; return External IDs verified with command and output evidence, which QA reads as producer evidence without adding a new QA recognizer until a measured run justifies one.
- **CODER-902** MAY: Annotate a verified identifier with EXTERNAL_DEPENDENCY, command and date only when the target comment policy permits that provenance; the report remains the evidence channel where source annotations are forbidden.
- **CODER-903** MUST: Stop on unresolved external identifier verification, select a verified alternative or disclose HALLUCINATION_RISK in Deviations; inherited specification approval does not prove an identifier exists.
- **CODER-904** MUST: Measure every threshold criterion and report one line with its id, measured value, operator, threshold and met/not-met outcome, declaring any failure as a deviation rather than substituting structurally ready, files exist or typecheck claims.
- **CODER-905** MUST NOT: Use undeclared skipped or NotImplementedError test bodies to claim coverage; Python skip-stubs and JS/TS skip, todo, fixme, xit and xdescribe forms need honest declaration and contribute no satisfied criterion while deferred.
- **CODER-906** MUST: For a genuinely unavailable live database, GPU, network, token or artifact test, declare TEST_DEFERRED in Deviations with four fields: path and covered criterion, Required runtime, How to run with exact command, and Why deferred; this transfers verification to QA but is not acceptance.
- **CODER-907** MUST: Include an acceptance-map test for any shipped real entry point end-to-end and print evidence of its real invocation before the suite summary so the producer matches the real-path recognizer.
