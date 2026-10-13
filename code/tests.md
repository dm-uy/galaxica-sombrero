---
id: code.tests
title: Tests
status: draft
---

# Tests

This body states source-backed conditional authoring and evidence duties. Runtime mechanisms remain adapter-owned; completion of text supplies no operational adoption claim.

<!-- anchor: code.tests.core -->

## Current core dependency

- **TST-101** MUST: Applicable current rich contracts, correctly paired regions, qualified relations, field continuations, current placement and actual Doxygen associations remain governed by [exoskeleton](exoskeleton.md), [navigation](navigation.md) and [Doxygen](doxygen.md). The completed core is a dependency; filling LDD/tests cannot waive its full module/function/class/method duties or reopen it through a reduced template. Older configured-or-specified Doxygen/no-config forms remain historical profiles; current mandatory bootstrap and explicit-prohibition conditions govern current authoring.

<!-- anchor: code.tests.traceability -->

## Conditional identifiers and generated exceptions

- **TST-102** MUST: Put specification identifiers in source only where the host permits them; otherwise retain canonical traceability in the development plan and AC-to-test guide. The generated migration revision exception is precisely scoped: its generator header/revision structure, revision message and inline why comments govern it. An ordinary new backend or test module cannot claim that generated-revision exception for its markup or LDD.

<!-- anchor: code.tests.native -->

## Framework, layout and direct logic

- **TST-201** MUST: Use the actual target-documented test framework and layout, with pytest in root tests as fallback. Call business logic through native direct imports; subprocess execution is forbidden as a substitute for business-logic tests. Tests of a genuinely shipped CLI, process or session boundary may invoke that real boundary. The source backend/frontend pattern separates their modules even for simple tasks; backend modules SHOULD expose a clear independent entry point. Creating a console CLI is conditional on the user requesting a strictly console utility, rather than an automatic infrastructure step.

<!-- anchor: code.tests.isolation -->

## Explicit owned resources

- **TST-202** MUST: Use tmp_path or the actual framework equivalent for owned isolated resources and pass explicit paths; do not hardcode filesystem paths or alter sys.path to make tests import. Keep reference files read-only in the documented test-data location and create integration databases through the actual isolated plugin/API initialization boundary. Read the actual framework/plugin API before using it; do not guess APIs, install incidental dependencies or use a shared database/schema.

<!-- anchor: code.tests.exposure -->

## Accessible pre-assert trajectory

- **TST-301** MUST: Backend tests expose actual filtered importance7–10 records and relevant results before assertions through the documented visible runner. Actual host structured fields and level fields count as the supported encoding. A print swallowed by capture or a fabricated trace is not accessible execution evidence; the UI trace surface is actual AX state.

<!-- anchor: code.tests.semantic-trace -->

## Outcome and operation sequence

- **TST-302** MUST: Assert meaningful outcomes together with actual critical operation presence, correct order, cardinality and relevant key population. A nonempty result or any importance9 marker alone is insufficient Semantic Trace Verification. Historical one-shot examples illustrate the minimal exposure mechanism; they are not a complete correctness oracle.

<!-- anchor: code.tests.errors -->

## Expected-only error assertions

- **TST-303** MUST: Every happy-path test rejects all unexpected ERROR or CRITICAL records. A deliberate failure test requires its expected ERROR/CRITICAL event and rejects every unrelated error; use the host level field where applicable. Do not delete or weaken these assertions to repair a failing test.

<!-- anchor: code.tests.slices -->

## Atomic and scenario coverage

- **TST-304** MUST: For an applicable functional slice provide atomic tests of its elements and a complete scenario integration check. Trivial reversible low-impact edits do not require invented test infrastructure, while explicitly required planned delivery checks remain owed.

<!-- anchor: code.tests.metadata -->

## Full new test metadata

- **TST-305** MUST: A new test module receives the same full metadata field set as production code, with suite purpose, isolation/determinism invariants, strategy rationale Q/A, AC actor/action/goal usecases and every test/helper in the weighted qualified modulemap. Each test has its own purpose and rich entity contract; existing-file edits remain entity-local with affected existing module facts current. Preserve the invoked rich language profile and paired logical-step boundaries; a reduced test template is not permitted.

<!-- anchor: code.tests.ui -->

## Conditional UI evidence

- **TST-401** MUST: For web components use the documented component stack with typed fixtures and assert role, accessible name, state and stable test identity; use the documented E2E runner for end-to-end browser behavior. For non-web or Gradio controller units call handlers directly and assert return types without hand-launching a server or using a browser emulator inside those units. The historical Gradio emulator prohibition does not prohibit genuine later web E2E. Browser/client code has its actual AX/component verification surface and no backend-LDD requirement; detailed [AX](ax-ui.md) remains a separate home.

<!-- anchor: code.tests.integration -->

## Conditional data and lesson fixtures

- **TST-402** MAY: For a simple Lesson, create a test database/schema directly inside the test using owned tmp_path resources.

- **TST-404** MUST: This permission does not authorize shared schemas or change integration obligations: a Plugin/integration project uses actual isolated API-created databases, read-only references, logical ETL invariants and isolated parsing with static data-driven fixtures.

<!-- anchor: code.tests.di -->

## Dependency injection preference

- **TST-403** SHOULD: Prefer dependency injection and explicit paths over patching internal state. Under the integration profile retain its explicit-path, initialization, fixture and invariant instructions. This preference is not a universal ban on mocks/fakes; a fake target cannot prove delivery to the declared real endpoint.

<!-- anchor: code.tests.counter -->

## Actual pytest session counter

- **TST-501** MUST: Where the pytest Anti-Loop hook applies, the session hooks own the ignored counter file; never increment inside individual tests or manually reset it. The actual current hook reads attempts at session start, increments once on nonzero session exit at finish and resets on every exit0, including a targeted green run. Missing or damaged reads become0 and counter write errors are ignored in this advisory implementation; advice cannot certify a verdict.

<!-- anchor: code.tests.non-pytest -->

## Non-pytest tracking

- **TST-502** MUST: Non-pytest suites use the actual runtime/parent attempt contract and applicable escalation ladder rather than a fictional pytest counter file. Historical self-tracking examples remain conditioned on their runtime; tracking never refunds parent repair spend.

<!-- anchor: code.tests.emission -->

## Advisory emission profiles

- **TST-503** MUST: Retain the attributed historical positive-counter instruction: expose checklist and attempt status EVERY TIME tests run beginning with counter >0, including a successful run. Later failure-conditioned source profiles remain separately attributed. Describe the actual current protected hook distinctly: it reads at start, prints red advice at nonzero finish and resets on every exit0 without advisory emission. The historical every-run instruction is neither a failure-only condition nor a universal current-hook policy; this text changes no hook.

<!-- anchor: code.tests.early-attempts -->

## Attempts one and two

- **TST-504** MUST: At attempts1–2 use the common-error checklist and retain new learned-error evidence. The historical source requests adding learned checklist items; the current fixed implementation checklist is protected and this text delivery neither rewrites it nor introduces a learning service.

<!-- anchor: code.tests.research -->

## Attempt three

- **TST-505** MUST: At attempt3 consult available research/documentation capability; when unavailable state that limitation explicitly and continue the ladder. Historical vendor tool names are attributed runtime examples; the current documentation/map/trace hint is not a claim that research ran.

<!-- anchor: code.tests.reflection -->

## Attempt four

- **TST-506** MUST: At attempt4 rederive the failing invariant from the specification, state two genuinely untried alternative approaches with evidence and switch to one. Retain weaker historical looping/superposition warnings as their profile; book needs-human wording grants no new owner gate or permission to repeat the same approach.

<!-- anchor: code.tests.stop -->

## Attempt five and escalation

- **TST-507** MUST: At attempt5+ stop the agent implementation loop and return failing tests, logs, tried hypotheses and an actionable Bug Report through the parent. The current pytest STOP message is advisory and neither aborts pytest nor raises HaltError. The book max-attempts5/HaltError illustration remains a separate historical profile; it does not alter the actual hook.

<!-- anchor: code.tests.parent-budget -->

## Separate cumulative workflow budget

- **TST-508** MUST: Keep local session attempts separate from the parent-owned cumulative causal Debug-entry budget under [run state](../flow/run-state.md) and [phases](../flow/phases.md). The historical donor ceiling2 and current native parent ceiling4 are different runtime/version profiles. Targeted green, local reset, retry, model/context change or a new run name cannot refund spent parent entries; the parent records spend before entry and renews independent QA after repair.

<!-- anchor: code.tests.proportionality -->

## Inner iteration and final suite

- **TST-601** MUST: Match inner-loop checks to impact: an edited test uses its node, changed source uses covering tests, and a red run iterates on its actual failure subset. Collect the assigned fixes, then obtain one final full relevant-suite green result before SUCCESS/FIXED; independent QA remains full. Do not repeat full suites per edit without new changes, failures or unresolved concerns. Generic comment/document-only proportionality advice cannot waive explicitly required source-fidelity or behavior checks.

<!-- anchor: code.tests.verbosity -->

## Attributable runner profiles

- **TST-602** MUST: Follow the actual approved plan/host runner commands while preserving accessible required trace. Historical always-visible -s-v and later quiet-full -q/failure-verbose/targeted-verbose-MAY profiles both remain attributed, with no universal verbosity policy inferred. The current repository delivery profile is visible -s -v; historical timing/byte/token figures are not current benchmark measurements.

<!-- anchor: code.tests.guide -->

## AC-to-test guide

- **TST-701** MUST: Give every AC an actual covering behavioral test or an explicit deferred/N-A row with its reason. The guide states input data, native fixtures and ownership, exact commands/queries, thresholds and measured met/NOT-met values, expected important trace or AX state, runtime limitations and verification owner. Test names remain behavioral unless host permission allows specification identifiers; the guide is the canonical code-side AC map. When a CLI/script/entrypoint ships, map a test exercising its real invocation end to end, with actual invocation evidence before the summary. A legacy guide recognizer accepting older bare rows does not automatically certify a new formatted table.

<!-- anchor: code.tests.quantities -->

## Actual threshold measurement

- **TST-702** MUST: For every quantitative AC measure the actual runtime number and compare it with the exact required threshold, reporting met or NOT met. Files existing, typecheck passing or structural readiness is not that measurement; unavailable required measurement stays unverified with its limitation.

<!-- anchor: code.tests.deferred -->

## No skipped acceptance

- **TST-703** MUST: Skipped or NotImplemented tests cover zero acceptance criteria. TEST_DEFERRED records test path, AC, required runtime, exact command, reason and verification owner and transfers the burden to QA/escalation. A deferred declaration is not acceptance; unavailable mandatory evidence remains NOT_RUN/BLOCKED.

<!-- anchor: code.tests.diagnosis -->

## Diagnostic Trio and lasting regression

- **TST-801** MUST: Before repair independently compare the original task/specification, actual code/protection/contracts, produced logs and real data; gather traceback modules and relevant dependencies and establish the evidenced root cause before editing. Keep competing hypotheses and evidence where the cause is ambiguous; repair the cause within scope. Preserve a discriminating permanent regression and BUG_FIX_CONTEXT recording issue, previous approach, problem and chosen fix, with affected metadata and logs current. After repair audit the new actual trace against contract intent and remove all temporary DebugProbe instrumentation. Independent QA evaluates the result before release; the Diagnostic Trio increases justified confidence and is not proof that all defects are absent.

<!-- anchor: code.tests.delivery -->

## Capture and either real-channel trigger

- **TST-901** MUST: A mock, stub, caplog, capsys, in-memory transport, mocked HTTP server or DB driver closing a channel proves an API call rather than delivery to its real endpoint. A DoD-declared channel deliverable OR an actual process/container crossing independently requires the corresponding real-target runtime probe. Do not require both triggers together; inspect actual handler/configuration, target receipt, argv/environment/streams/exit where applicable. A fake/local server cannot replace a different declared endpoint; a missing mandatory target probe remains unaccepted rather than a broad N-A. Capture-based Semantic Trace is necessary but insufficient when either trigger applies.

<!-- anchor: code.tests.stdout -->

## Narrow pure-logic sufficiency

- **TST-902** MUST: For actual pure logic with no external sink, whose actual channel is visible test-process stdout, documented print-visible output is sufficient; do not demand a redundant external probe. Prove that scope/channel condition from actual evidence, rather than a fixture name or self-declared waiver.

<!-- anchor: code.tests.real-shape -->

## Shipped shape and negative restoration

- **TST-1001** MUST: Exercise the shipped producer/checker through the same real filesystem and input shape as its consumer and assert actual status/property, rather than reimplemented behavior or verdict wording alone. Negative controls actually trigger the defect, retain meaningful protective siblings and restore complete original bytes and numeric modes. Same-author fixtures share assumptions and pin regressions; independent real artifacts and full ordinary-meaning review are separately necessary. Fixed expected results precede observation; finite literal/regex recognizers do not prove unrestricted prose semantics.

<!-- anchor: code.tests.discrimination -->

## Discriminating values and call boundaries

- **TST-1002** MUST: Use inputs that distinguish the claimed property: for summation choose multiple values whose sum differs from first, last and maximum. When a call/lifecycle boundary is the property, preserve actual arguments, order and cleanup observations at call time, even for constructed but abandoned streams. This testing lesson grants no scheduler, worker, cost-engine or port implementation authority.

<!-- anchor: code.tests.worker-lineage -->

## Original worker profile

- **TST-1101** MUST: When referring to the original `StubWorker` profile, preserve its exact implementation facts rather than claim a neutral port. It consumes ordered turns, private copied queues by default or a single shared per-role queue in creation order; fork copies only remaining turns and preserves the original. Unknown/closed prompt sessions raise TRANSIENT; unknown roles and exhausted scripts raise FATAL; Hang is documented to stall forever until cancellation, but its actual `_play` branch awaits `asyncio.sleep(3600)` then returns if uncancelled; that finite implementation contradicts the declared indefinite intent; scripted failures propagate. Create records role, cwd, model, title and response_schema; prompt/resume records actual session/message/kind at call time before lazy playback, including abandoned streams. Configured unsupported resume raises NotImplementedError; supported resume reopens a closed session; fork records original/fork identity. Close state is idempotent while every call, including repeats, is recorded; single-step and multistep helpers retain ordered tool events, cost-bearing step events and final text. These implementation obligations remain at the worker adapter/runtime home; no queue, scheduler, schema or cost port is supplied here.

<!-- anchor: code.tests.launcher-lineage -->

## Conditional Lesson launcher

- **TST-1102** MUST: In an invoked Lesson launcher profile retain lazy heavy imports in main, KeyboardInterrupt handling, browser-opening launch and duplicate file/stdout logs. The Plugin profile skips this launcher step because isolated plugins do not require their own entrypoint. Actual shipped product/host requirements govern; this condition grants no unsolicited server/UI/dependency installation.

<!-- anchor: code.tests.unittest-lineage -->

## Original standalone audit profile

- **TST-1103** MUST: Retain the original dependency-free distribution audit as stdlib unittest with script verbosity2 and its local file-directory import binding. That attributed local sys.path insertion does not authorize path hacks in neutral pytest tests. Its plan-header and named mock-transport/production-symbol fixtures assert audit status over actual artifacts; they do not send messages or prove delivery to that external endpoint.

<!-- anchor: code.tests.io-lineage -->

## Original migration file-I/O profile

- **TST-1104** MUST: Retain the original migration read_text behavior: read without newline normalization, catch OSError/UnicodeDecodeError and return None on failure. Its StringIO line splitting uses only CR, LF and CRLF so AST/tokenize coordinates do not split on form-feed or Unicode separators; inserted lines match the file ending. The related trailing scanner tokenizes quoted/bare tokens with column spans and stops at an unquoted hash; it remains an owning tokenizer detail, not a new logging/runtime port.

<!-- anchor: code.tests.returns -->

## Existing role authority

- **TST-1201** MUST: Use existing role-return envelopes and actual artifacts, guide, measurements, verified external identifiers, deviations and actionable failure evidence under [role returns](../protocols/role-returns.md). Compact historical source JSON is not a new wire/schema or execution authority; the parent alone owns transitions, counted repair routing and result acceptance.

<!-- anchor: code.tests.later-documents -->

## Later lifecycle homes

- **TST-1202** MUST: Keep detailed document/lifecycle conventions at [document protocol](../protocols/document.md), [conventions](../documents/conventions.md) and [batch](../process/batch.md). The test guide is this body’s dependency; filling two code bodies does not complete lifecycle/templates or change those conventions.

<!-- anchor: code.tests.later-learning -->

## Attributed rationale and learning

- **TST-1203** MUST: Retain historical cognitive/model explanations, timing/byte/token observations and incidents as attributed source rationale rather than current benchmarks or theorems. Detailed verification/prompting and learning remain at [verification](../prompting/verification.md) and [learning](../process/learning.md). Independent verification is not consensus or copying; historical lessons do not become global policy automatically.
