// region MODULE_CONTRACT [DOMAIN(9): WorkflowVerification, FlowOrchestration; CONCEPT(9): ScriptedFakeAgents, RealHelperMode, HostEmulation, SchemaEnforcement; TECH(7): NodeJS, ESModule, JSONSchema, child_process]
// ## @modulecontract
// ## @purpose Execute workflows/feature-dev.js outside Claude Code with the same restrictions the Workflow host imposes, driving it with scripted role agents so that every route of the spine can be observed without a model, in two modes: a fast fake mode with an emulated ledger, and a real-helper mode in which the recorder stub writes the record file and runs the shipped run_state.py exactly as the recorder prompt tells it, over an owned target initialized by run_state.py init.
// ## @scope Loading the script as text, stripping the export of meta, running the body as an async function with injected globals (agent, phase, log, args, parallel, pipeline), poisoning the clock and randomness, hiding Node APIs, emulating the host's schema enforcement (a schema-failing return becomes null), the fake ledger of the fake mode, and for the real-helper mode: a role set that derives its identities with the show and digest commands quoted in its own prompt, edits the owned target, and a recorder that executes the commands quoted in the recorder prompt through a shell. One JSON line is printed per scenario.
// ## @input argv[2] is a scenario name, --list, --list-real or --meta; the workflow file is read from ../workflows/feature-dev.js relative to this file (or from M22_WORKFLOW when that variable names an absolute path). Real scenarios read M22_REAL_FRAMEWORK (a temporary copy of the package placed at implementations/claude with the neutral files above it), M22_REAL_WORK (an empty owned directory) and M22_REAL_SCRATCH (an owned directory outside the work directory and under a default safe prefix of the guard, used as the scratch argument; the judges write under <scratch>/<runId>/<nn>-<phase>/). M22_NO_SCRATCH, when set, omits the scratch argument and lets a judge fall back to the writable location its own prompt names; it exists only to run the new scratch tests against a spine from before the scratch root and see them fail for the right reason.
// ## @output One JSON line on stdout: {scenario, status, debugSpent, calls:[{agentType, model, label, phase, schemaOk, flags}], logs, records, phases, schemaViolations, unconsumed, reason, ledgerState (real mode), workDir, scratch, judgeFiles (real mode)}. In real mode the prompts of the scenarios that ask for it are also written to <workDir>/prompts/. Exit code 0 when the script ran, 1 on a harness exception.
// ## @links [READS_DATA_FROM(9): workflows/feature-dev.js; READS_DATA_FROM(9): skills/feature-dev/scripts/run_state.py through the shell; USES_API(8): node:fs; USES_API(8): node:vm; USES_API(8): node:child_process; USES_API(7): node:url]
// ## @links_to_spec examples/pm-project/specs/m22-claude-package.md AC-M22-3
// ## @invariants
// ## - The script under test is never modified; the harness only reads it.
// ## - Fake agents are keyed by agent type and consumed in call order; an unscripted call is a harness exception, never a silent default.
// ## - Canned returns are checked against the schema the script handed to agent(); a violation is recorded and the call returns null, as the host does.
// ## - Date.now, Math.random and an argument-less Date constructor throw while the script runs.
// ## - In real-helper mode the helper is the only authority on acceptance: the recorder stub never decides a ledger outcome, it only runs the quoted commands and reports their real exit code and output.
// ## - In real-helper mode a role obtains its identities only from the commands its own prompt quotes; a prompt that omits or misquotes them makes the scenario fail.
// ## - In real-helper mode a judge writes only where its own prompt grants it (the SCRATCH ROOT line, or, for a spine without a scratch root, the writable EVIDENCE ROOT line) and cites what it wrote; the diagnostic file of a correction episode is written to the path the recorder prompt names in STEP 2a, which must equal the control evidence path.
// ## - The scenarios that exercise a refusal of the recorder precheck build their hostile inputs on the real file system (a symbolic link, a destination that already exists in the evidence home, a scratch file that was never written, each beside a valid file); the shipped precheck refuses them, never the harness.
// ## @rationale
// ## Q: Why a text-level loader instead of importing the script?
// ## A: The script has a top-level return and top-level await in a host function body; it is not a valid ES module, so the harness wraps it the way the host does.
// ## Q: Why a real-helper mode beside the fake ledger?
// ## A: A permissive fake accepts what the helper refuses (directory scope entries, evidence outside the target, directory artifact paths); only the shipped helper can say what the ledger accepts, so the routes that matter run through it.
// ## Q: Why does the real-mode role parse its commands from the prompt?
// ## A: A real role can use only what the prompt says; extracting the show and digest commands from the prompt proves that the instruction is complete and runnable.
// ## @changes
// ## LAST_CHANGE: [v1.3.0 - Judge directories namespaced by run (<scratch>/<runId>/<nn>-<phase>/) in both modes, judgeLink for a symbolic-link source, scenarios for the precheck refusals (valid file next to a missing one, existing destination, link source) and for case-variant and alias-spelled citations on the real file system, fake scenarios for the run namespace, the macOS aliases and case-insensitive destinations, the scratch grant path exposed in the prompt flags.]
// ## - v1.2.0 - Scratch argument and judge scratch directories in both modes, import list parsed from the precheck command, recorder that throws on demand, real scenarios with git targets (ignored Anti-Loop counter, ignored Doxygen map directory) and with judges that cite scratch files, diagnostic path parsed from STEP 2a, review findings with a code, prompt dumps for the guard test.
// ## - v1.1.0 - Real-helper mode (recorder stub runs run_state.py through a shell, roles derive real identities), recorder prompt parser shared by both modes, checksum and precheck emulation, control events in the fake ledger.
// ## @modulemap
// ## FUNC 6[Validate a value against the JSON Schema subset the script emits] => validateSchema
// ## FUNC 5[Check that a schema is a flat object schema without top-level alternatives] => schemaShapeOk
// ## FUNC 8[Build one canned role return with the common envelope] => ret
// ## FUNC 9[Declare all fake-mode scenarios] => SCENARIOS
// ## FUNC 8[Parse the commands, paths and import list quoted in a recorder prompt] => parseRecorderPrompt
// ## FUNC 5[Compute the length and code-unit sum of a text] => checksumOf
// ## FUNC 9[Emulate the recorder agent and the fake ledger] => makeRecorder
// ## FUNC 5[Run a shell command and capture its real result] => sh
// ## FUNC 9[Execute the recorder prompt through a real shell and the real helper] => realRecorder
// ## FUNC 9[Build the real-mode scripted roles over an owned target] => realRoles
// ## FUNC 9[Declare all real-helper scenarios] => REAL_SCENARIOS
// ## FUNC 10[Run one real-helper scenario against the script and describe it] => runReal
// ## FUNC 4[Record which self-containment facts a role prompt carries] => flagsFor
// ## FUNC 10[Run one fake-mode scenario against the script and describe it] => runScenario
// ## FUNC 7[Evaluate the meta literal in an empty context] => evaluateMeta
// ## @usecases
// ## - QA: node workflow_harness.mjs green -> one JSON line -> test_workflow.py asserts status, spend and call order.
// ## - QA: M22_REAL_FRAMEWORK=... M22_REAL_WORK=... node workflow_harness.mjs real_green -> the spine drives the real helper to a SUCCESS ledger.
// ## - QA: M22_REAL_FRAMEWORK=... M22_REAL_WORK=... M22_REAL_SCRATCH=... node workflow_harness.mjs real_judge_scratch_dest_exists -> a refused import destination stays untouched and nothing of the record is copied.
// ## - QA: node workflow_harness.mjs --list and --list-real -> the scenario names -> the test tables are checked against them.
// ## @GREP_SUMMARY workflow harness, fake agents, real helper mode, recorder stub, shell commands from prompt, scenario, schema enforcement, ledger emulation, host restrictions, JSON line
// ## @STRUCTURE ▶ load script text → ⊕ strip export → ○ wrap async fn(globals) → ⚡ scripted agent() ⟲ phases → ◇ fake ledger | real run_state.py → ∑ calls/logs/records → ⎋ one JSON line
// endregion MODULE_CONTRACT

import { readFileSync, writeFileSync, mkdirSync, existsSync, rmSync, lstatSync, symlinkSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import vm from 'node:vm'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const WORKFLOW = process.env.M22_WORKFLOW && process.env.M22_WORKFLOW.charAt(0) === '/' ? process.env.M22_WORKFLOW : path.join(HERE, '..', 'workflows', 'feature-dev.js')
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor

const TARGET = '/work/target'
const FW = '/work/methodology/implementations/claude'
const SPEC = '/work/specs/m-spec.md'
const SCRATCH = '/tmp/m22-scratch'
const JUDGE = SCRATCH + '/run-001'
const NO_SCRATCH = !!process.env.M22_NO_SCRATCH
const PLAN = '/work/target/plan/DevelopmentPlan.md'
const RUN_ID = 'run-001'
const CONTRACT = 'methodology-claude/1.0.0'
const AT = 'methodology-claude:'
const SCAN_IDS = [
  'green-test-trap',
  'quantitative-ac',
  'semantic-trace',
  'infra-dod',
  'side-effect-channel',
  'secret-leak',
  'real-path-shape',
  'discriminating-test',
]

// region FUNC_validateSchema [DOMAIN(7): JSONSchema; CONCEPT(8): HostSchemaEnforcement; TECH(5): JavaScript]
// ## @purpose Validate a value against the JSON Schema subset the script emits, as the host structured-output tool would.
// ## @uses Object.keys, Number.isInteger
// ## @io schema, value, string, string[] -> void
// ## @complexity 7
function validateSchema(schema, value, where, errs) {
  if (errs.length > 20) return
  if (schema.oneOf || schema.anyOf || schema.allOf) {
    errs.push(where + ': unsupported alternative keyword in schema')
    return
  }
  if (schema.type === 'object') {
    if (value === null || typeof value !== 'object' || Array.isArray(value)) {
      errs.push(where + ': object expected')
      return
    }
    const props = schema.properties || {}
    if (schema.additionalProperties === false) {
      for (const k of Object.keys(value)) if (!(k in props)) errs.push(where + '.' + k + ': additional property')
    }
    for (const k of schema.required || []) if (value[k] === undefined) errs.push(where + '.' + k + ': required')
    for (const k of Object.keys(props)) if (value[k] !== undefined) validateSchema(props[k], value[k], where + '.' + k, errs)
  } else if (schema.type === 'array') {
    if (!Array.isArray(value)) {
      errs.push(where + ': array expected')
      return
    }
    if (schema.minItems !== undefined && value.length < schema.minItems) errs.push(where + ': minItems')
    if (schema.maxItems !== undefined && value.length > schema.maxItems) errs.push(where + ': maxItems')
    value.forEach((v, i) => validateSchema(schema.items, v, where + '[' + i + ']', errs))
  } else if (schema.type === 'string') {
    if (typeof value !== 'string') errs.push(where + ': string expected')
    else {
      if (schema.minLength !== undefined && value.length < schema.minLength) errs.push(where + ': minLength')
      if (schema.enum && !schema.enum.includes(value)) errs.push(where + ': enum')
    }
  } else if (schema.type === 'integer') {
    if (typeof value !== 'number' || !Number.isInteger(value)) errs.push(where + ': integer expected')
    else if (schema.minimum !== undefined && value < schema.minimum) errs.push(where + ': minimum')
  } else if (schema.type === 'boolean') {
    if (typeof value !== 'boolean') errs.push(where + ': boolean expected')
  } else {
    errs.push(where + ': unknown schema type ' + schema.type)
  }
}
// endregion FUNC_validateSchema

// region FUNC_schemaShapeOk [DOMAIN(6): JSONSchema; CONCEPT(7): FlatObjectSchema; TECH(4): JavaScript]
// ## @purpose Confirm the schema handed to agent() is a flat object schema with properties and no top-level alternatives.
// ## @uses none
// ## @io any -> boolean
// ## @complexity 3
function schemaShapeOk(schema) {
  return (
    !!schema &&
    schema.type === 'object' &&
    typeof schema.properties === 'object' &&
    !('oneOf' in schema) &&
    !('anyOf' in schema) &&
    !('allOf' in schema)
  )
}
// endregion FUNC_schemaShapeOk

// region FUNC_ret [DOMAIN(8): Fixtures; CONCEPT(9): CanonicalEnvelope; TECH(4): JavaScript]
// ## @purpose Build one canned role return: the common envelope plus the status payload.
// ## @uses Object.assign
// ## @io string, string, string, {input, cand}, object -> object
// ## @complexity 3
function ret(phase, role, status, ids, payload) {
  return Object.assign(
    {
      phase,
      role,
      status,
      summary: phase + ' ' + status,
      runId: RUN_ID,
      inputIdentity: ids.input,
      candidateIdentity: ids.cand,
      contractVersion: CONTRACT,
      evidence: [TARGET + '/evidence/' + phase + '.txt'],
    },
    payload,
  )
}
// endregion FUNC_ret

// BUG_FIX_CONTEXT: the canned returns used a directory for the Finalize Doxygen path, a directory entry in DO NOT TOUCH and a
// specification path as evidence, all of which the helper refuses while the permissive fake accepted them; the canned values now
// use the exact forms the helper accepts (index.xml, exact files, evidence inside the target), and the real-helper mode judges the rest.
const bug = (origin) => ({
  goal: 'goal of ' + origin,
  actual: 'actual failure reported by ' + origin,
  logAnalysis: 'the log shows the failing branch',
  dataAnalysis: 'the data confirms it',
  hypothesis: 'the guard compares the wrong field',
  recommendation: 'compare the right field in src/a.py',
})
const bootstrap = (over) =>
  ret('bootstrap', 'searcher', 'SUCCESS', { input: 'in-0', cand: 'c0' }, Object.assign({
    isEmpty: false,
    classificationHint: 'BROWNFIELD',
    fileCount: 1,
    files: [{ path: 'src/a.py', summary: 'module a', structure: 'one function', relevance: 'edit target' }],
    recommendations: ['read src/a.py first'],
    limitations: ['sampled'],
  }, over || {}))
const architect = (over, ids) =>
  ret('architect', 'architect', 'SUCCESS', ids || { input: 'in-0', cand: 'c1' }, Object.assign({
    classification: 'BROWNFIELD',
    projectType: 'Plugin System',
    taskType: 'Code and Tests',
    planPath: PLAN,
    featureSlices: [{ id: 'S1', description: 'slice one', files: ['src/a.py', 'tests/test_a.py'], ui: false }],
    mayEdit: ['src/a.py', 'tests/test_a.py', 'tests/test_guide.md'],
    doNotTouch: ['docs/readme.md'],
    acceptanceCriteria: [{ id: 'AC-1', text: 'a returns one', measurable: true, threshold: '>= 1 test' }],
    specDeficiencies: [],
    specBlocked: false,
    visualGate: { status: 'NOT_APPLICABLE', output: 'gate not active', componentNodes: 1, testsOnly: false, reason: 'fewer than three component nodes' },
  }, over || {}))
const gate = (over) => Object.assign({ status: 'PASS', output: 'ok: 4 nodes scanned', componentNodes: 4, testsOnly: false, command: 'python3 visual_gate_lint.py plan', exitCode: 0, scannedNodes: 4, evidence: [TARGET + '/evidence/gate.txt'] }, over || {})
const code = (cand, over) =>
  ret('code', 'coder', 'SUCCESS', { input: 'in-1', cand }, Object.assign({
    artifacts: [TARGET + '/src/a.py', TARGET + '/tests/test_a.py'],
    testGuidePath: TARGET + '/tests/test_guide.md',
    testSummary: '3 passed',
    deviations: [],
    measurements: ['AC-1: measured=3 >= 1 met'],
    logs: [TARGET + '/.methodology/evidence/run-001/run.log'],
    doxygen: { command: 'doxygen Doxyfile', exitCode: 0, output: 'no warnings', evidence: [TARGET + '/doxygen_output/xml/index.xml'], mapPath: TARGET + '/doxygen_output/xml', candidateIdentity: cand, inputIdentity: 'in-1' },
  }, over || {}))
const codeBug = () => ret('code', 'coder', 'BUG_REPORT', { input: 'in-1', cand: 'c1' }, { bugReport: bug('code') })
const scans = (over, evidence) => SCAN_IDS.map((id) => ({ id, status: (over && over[id]) || 'PASS', reason: id + ' judged', evidence: evidence || [TARGET + '/tests/test_guide.md'] }))
const qa = (cand, status, scanOver, over) =>
  ret('qa', 'qa', status || 'SUCCESS', { input: 'in-1', cand }, Object.assign({
    testSummary: '3 passed',
    scans: scans(scanOver),
    findings: [],
    limitations: ['visual fidelity not judged'],
  }, status === 'BUG_REPORT' ? { bugReport: bug('qa') } : {}, over || {}))
const review = (cand, status, over) =>
  ret('review', 'reviewer', status || 'SUCCESS', { input: 'in-1', cand }, Object.assign({
    findings: [],
    limitations: ['no live service'],
    diffEvidence: [TARGET + '/src/a.py'],
    scopeJudgment: 'every changed path is inside MAY EDIT',
  }, status === 'BUG_REPORT' ? { bugReport: bug('review'), findings: [{ code: 'LOGIC', severity: 'HIGH', message: 'wrong comparison', path: 'src/a.py', line: 7 }] } : {}, over || {}))
const debugFixed = (cand, origin, over) =>
  ret('debug', 'debugger', 'FIXED', { input: 'in-1', cand }, Object.assign({
    rootCause: 'wrong field compared in ' + origin + ' path',
    fix: 'compare the right field',
    filesTouched: [TARGET + '/src/a.py'],
    postFixAudit: 'only src/a.py changed',
    testSummary: '3 passed',
    regressionEvidence: [TARGET + '/tests/test_guide.md'],
    origin,
  }, over || {}))
const debugBlocked = () => ret('debug', 'debugger', 'BLOCKED', { input: 'in-1', cand: 'c2' }, { rootCause: 'no reproducer', reason: 'the failing service is unavailable', limitations: ['service down'] })
const finalizeOk = (cand, over) =>
  ret('finalize', 'architect', 'SUCCESS', { input: 'in-1', cand }, Object.assign({
    report: TARGET + '/.methodology/evidence/run-001/final-report.md',
    classification: 'BROWNFIELD',
    planPath: PLAN,
    testsPath: TARGET + '/tests/test_guide.md',
    logPath: TARGET + '/.methodology/evidence/run-001/run.log',
    doxygenPath: TARGET + '/doxygen_output/xml/index.xml',
    testSummary: '3 passed',
    acceptanceEvidence: [TARGET + '/tests/test_guide.md'],
    qaEvidence: [TARGET + '/evidence/qa.txt'],
    reviewEvidence: [TARGET + '/evidence/review.txt'],
    liveEvidence: [TARGET + '/.methodology/evidence/run-001/run.log'],
    blastRadius: { added: ['tests/test_a.py'], modified: ['src/a.py'], deleted: [], untracked: [] },
    scopeDeviations: [],
    limitations: ['no merge or deploy performed'],
  }, over || {}))
const finalizeEsc = (cand) => ret('finalize', 'architect', 'ESCALATED_FINALIZE', { input: 'in-1', cand }, { reason: 'Doxyfile is missing', limitations: ['map not built'], requiredRepair: 'add a Doxyfile for the package' })
const raw = (value) => ({ __raw: true, value })

const happy = () => ({
  searcher: [bootstrap()],
  architect: [architect(), finalizeOk('c2')],
  coder: [code('c2')],
  qa: [qa('c2')],
  reviewer: [review('c2')],
  debugger: [],
})
const base = (over) => Object.assign({ spec: SPEC, target: TARGET, plan: PLAN, approval: 'approval-ref-1', runId: RUN_ID, framework: FW, recordState: false }, NO_SCRATCH ? {} : { scratch: SCRATCH }, over || {})

// region FUNC_SCENARIOS [DOMAIN(9): Scenarios; CONCEPT(9): RouteCoverage; TECH(4): JavaScript]
// ## @purpose Declare every fake-mode scenario as scripted queues per agent type, optional recorder behavior and the invocation arguments.
// ## @uses none
// ## @io none -> map name -> () => {args, queues, recorder}
// ## @complexity 8
const SCENARIOS = {
  green: () => ({ args: base(), queues: happy() }),
  green_recorded: () => ({ args: base({ recordState: true }), queues: happy() }),
  visual_gate_pass: () => {
    const q = happy()
    q.architect[0] = architect({ visualGate: gate() })
    return { args: base(), queues: q }
  },
  code_bug_debug_fixed: () => {
    const q = happy()
    q.coder = [codeBug()]
    q.debugger = [debugFixed('c3', 'code')]
    q.qa = [qa('c3')]
    q.reviewer = [review('c3')]
    q.architect[1] = finalizeOk('c3')
    return { args: base(), queues: q }
  },
  qa_bug_twice_cap1: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT'), qa('c3', 'BUG_REPORT')]
    q.debugger = [debugFixed('c3', 'qa')]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ maxDebug: 1 }), queues: q }
  },
  maxdebug_zero_qa_defect: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT')]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ maxDebug: 0 }), queues: q }
  },
  review_bug_debug: () => {
    const q = happy()
    q.qa = [qa('c2'), qa('c3')]
    q.reviewer = [review('c2', 'BUG_REPORT'), review('c3')]
    q.debugger = [debugFixed('c3', 'review')]
    q.architect[1] = finalizeOk('c3')
    return { args: base(), queues: q }
  },
  qa_bug_debug_fixed_recorded: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT'), qa('c3')]
    q.debugger = [debugFixed('c3', 'qa')]
    q.reviewer = [review('c3')]
    q.architect[1] = finalizeOk('c3')
    return { args: base({ recordState: true }), queues: q }
  },
  debug_blocked: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT')]
    q.debugger = [debugBlocked()]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  debug_origin_mismatch_corrected: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT'), qa('c3')]
    q.debugger = [debugFixed('c3', 'review'), debugFixed('c3', 'qa')]
    q.reviewer = [review('c3')]
    q.architect[1] = finalizeOk('c3')
    return { args: base(), queues: q }
  },
  spec_blocked: () => ({
    args: base(),
    queues: { searcher: [bootstrap()], architect: [architect({ specBlocked: true, blockReason: 'AC-1 and AC-2 contradict numerically', specDeficiencies: ['AC-1 versus AC-2'] })] },
  }),
  architect_blocked_spec: () => ({
    args: base(),
    queues: {
      searcher: [bootstrap()],
      architect: [ret('architect', 'architect', 'BLOCKED', { input: 'in-0', cand: 'c0' }, { reason: 'required identifier unverifiable', limitations: ['no network'], specBlocked: true, blockReason: 'the external image tag cannot be verified' })],
    },
  }),
  architect_blocked: () => ({
    args: base(),
    queues: { searcher: [bootstrap()], architect: [ret('architect', 'architect', 'BLOCKED', { input: 'in-0', cand: 'c0' }, { reason: 'the specification file is unreadable', limitations: ['nothing designed'] })] },
  }),
  bootstrap_blocked: () => ({
    args: base(),
    queues: { searcher: [ret('bootstrap', 'searcher', 'BLOCKED', { input: 'in-0', cand: 'c0' }, { reason: 'target directory unreadable', limitations: ['no inventory'] })] },
  }),
  visual_gate_fail: () => ({
    args: base(),
    queues: { searcher: [bootstrap()], architect: [architect({ visualGate: { status: 'FAIL', output: 'lint: 4 violations', componentNodes: 4, testsOnly: false } })] },
  }),
  visual_gate_zero_nodes: () => ({
    args: base(),
    queues: { searcher: [bootstrap()], architect: [architect({ visualGate: gate({ scannedNodes: 0 }) })] },
  }),
  visual_gate_waived_active: () => ({
    args: base(),
    queues: { searcher: [bootstrap()], architect: [architect({ visualGate: { status: 'SKIPPED', output: 'skipped', componentNodes: 5, testsOnly: false, reason: 'not needed' } })] },
  }),
  visual_gate_empty_output: () => {
    const q = happy()
    q.architect[0] = architect({ visualGate: { status: 'NOT_APPLICABLE', output: '', componentNodes: 1, testsOnly: false, reason: 'fewer than three component nodes' } })
    return { args: base(), queues: q }
  },
  doxygen_empty_output: () => {
    const q = happy()
    q.coder = [code('c2', { doxygen: { command: 'doxygen Doxyfile', exitCode: 0, output: '', evidence: [TARGET + '/doxygen_output/xml/index.xml'], mapPath: TARGET + '/doxygen_output/xml', candidateIdentity: 'c2', inputIdentity: 'in-1' } })]
    return { args: base(), queues: q }
  },
  null_corrected: () => {
    const q = happy()
    q.qa = [null, qa('c2')]
    return { args: base(), queues: q }
  },
  agent_throws: () => {
    const q = happy()
    q.coder = [() => { throw new Error('transport fault') }]
    q.qa = []
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ recordState: true }), queues: q }
  },
  agent_throws_readonly: () => {
    const q = happy()
    q.qa = [() => { throw new Error('connection reset') }]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  null_twice: () => {
    const q = happy()
    q.qa = [null, null]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  qa_seven_scans: () => {
    const q = happy()
    const seven = () => raw(qa('c2', 'SUCCESS', undefined, { scans: scans().slice(0, 7) }))
    q.qa = [seven(), seven()]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  qa_duplicate_scan: () => {
    const q = happy()
    const dup = () => {
      const rows = scans()
      rows[5] = Object.assign({}, rows[0])
      return raw(qa('c2', 'SUCCESS', undefined, { scans: rows }))
    }
    q.qa = [dup(), dup()]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  qa_seven_then_eight: () => {
    const q = happy()
    q.qa = [raw(qa('c2', 'SUCCESS', undefined, { scans: scans().slice(0, 7) })), qa('c2')]
    return { args: base(), queues: q }
  },
  qa_success_failed_scan: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', { 'semantic-trace': 'FAIL' }), qa('c2', 'SUCCESS', { 'secret-leak': 'BLOCKED' })]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  plan_mismatch_corrected: () => {
    const q = happy()
    q.architect = [architect({ planPath: TARGET + '/other/DevelopmentPlan.md' }), architect(), finalizeOk('c2')]
    return { args: base(), queues: q }
  },
  scope_directory_entry: () => {
    const q = happy()
    q.architect = [architect({ mayEdit: ['src/', 'tests/test_guide.md'] }), architect(), finalizeOk('c2')]
    return { args: base(), queues: q }
  },
  scope_dot_slash_entry: () => {
    const q = happy()
    q.architect = [architect({ mayEdit: ['./src/a.py', 'tests/test_guide.md'] }), architect(), finalizeOk('c2')]
    return { args: base(), queues: q }
  },
  scope_dotdot_entry: () => {
    const q = happy()
    q.architect = [architect({ doNotTouch: ['src/../docs/readme.md'] }), architect(), finalizeOk('c2')]
    return { args: base(), queues: q }
  },
  scope_absolute_entry: () => {
    const q = happy()
    q.architect = [architect({ mayEdit: [TARGET + '/src/a.py', 'tests/test_guide.md'] }), architect(), finalizeOk('c2')]
    return { args: base(), queues: q }
  },
  evidence_spec_outside_target: () => {
    const q = happy()
    q.searcher = [bootstrap({ evidence: [SPEC] }), bootstrap()]
    return { args: base(), queues: q }
  },
  architect_requirements_field: () => {
    const q = happy()
    q.architect = [raw(architect({ businessRequirementsPath: TARGET + '/plan/BR.md' })), architect(), finalizeOk('c2')]
    return { args: base(), queues: q }
  },
  finalize_extensionless_doxygen: () => {
    const q = happy()
    q.architect = [architect(), finalizeOk('c2', { doxygenPath: TARGET + '/doxygen_output/xml/index' })]
    return { args: base(), queues: q }
  },
  doxygen_pass_with_prohibition_fields: () => {
    const q = happy()
    q.coder = [code('c2', { doxygen: { command: 'doxygen Doxyfile', exitCode: 0, output: '', evidence: [TARGET + '/doxygen_output/xml/index.xml'], mapPath: TARGET + '/doxygen_output/xml', candidateIdentity: 'c2', inputIdentity: 'in-1', reason: 'extra' } }), code('c2')]
    return { args: base(), queues: q }
  },
  code_scope_violation: () => {
    const q = happy()
    q.coder = [code('c2', { artifacts: [TARGET + '/docs/readme.md'] })]
    q.qa = []
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ recordState: true }), queues: q }
  },
  ui_discrepancy: () => {
    const q = happy()
    q.coder = [code('c2', { detectedUi: true, classifierEvidence: ['index.html created'] })]
    q.qa = []
    q.reviewer = []
    q.architect = [architect()]
    return { args: base(), queues: q }
  },
  finalize_escalated: () => {
    const q = happy()
    q.architect[1] = finalizeEsc('c2')
    return { args: base(), queues: q }
  },
  finalize_null_twice: () => {
    const q = happy()
    q.architect = [architect(), null, null]
    return { args: base(), queues: q }
  },
  finalize_candidate_mismatch: () => {
    const q = happy()
    q.architect = [architect(), finalizeOk('c9'), finalizeOk('c9')]
    return { args: base(), queues: q }
  },
  judge_scratch_recorded: () => {
    const q = happy()
    const run = JUDGE + '/04-qa/run.log'
    const probe = JUDGE + '/04-qa/probe/run.log'
    const report = JUDGE + '/04-qa/report.md'
    const notes = JUDGE + '/05-review/notes.md'
    q.qa = [qa('c2', 'SUCCESS', undefined, {
      evidence: [run, probe, TARGET + '/tests/test_guide.md'],
      scans: scans(undefined, [report]),
      findings: [{ scan: 'discriminating-test', code: 'WEAK_ASSERT', severity: 'LOW', message: 'one assertion is weak', evidence: [probe], path: 'tests/test_a.py', line: 1 }],
    })]
    q.reviewer = [review('c2', 'SUCCESS', { evidence: [notes], diffEvidence: [TARGET + '/src/a.py', notes], findings: [{ code: 'STYLE', severity: 'LOW', message: 'naming', evidence: [notes], path: 'src/a.py', line: 1 }] })]
    return { args: base({ recordState: true }), queues: q }
  },
  judge_scratch_unrecorded: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [JUDGE + '/01-qa/run.log'] })]
    return { args: base(), queues: q }
  },
  judge_evidence_outside_corrected: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: ['/tmp/elsewhere/run.log'] }), qa('c2')]
    return { args: base(), queues: q }
  },
  judge_scratch_unsafe_corrected: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [JUDGE + '/04-qa/run log.txt'] }), qa('c2')]
    return { args: base(), queues: q }
  },
  judge_scratch_dotdot_corrected: () => {
    const q = happy()
    q.reviewer = [review('c2', 'SUCCESS', { evidence: [JUDGE + '/05-review/../run.log'] }), review('c2')]
    return { args: base(), queues: q }
  },
  judge_scratch_directory_corrected: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [JUDGE + '/04-qa/'] }), qa('c2')]
    return { args: base(), queues: q }
  },
  writer_cites_scratch_corrected: () => {
    const q = happy()
    q.coder = [code('c2', { logs: [JUDGE + '/03-code/run.log'] }), code('c2')]
    return { args: base(), queues: q }
  },
  // The run namespace: a judge may cite only files under <scratch>/<runId>/; the flat layout of the earlier spine and the directory of
  // another run on the same scratch root are refused with the one correction.
  judge_scratch_old_layout_corrected: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [SCRATCH + '/04-qa/run.log'] }), qa('c2')]
    return { args: base(), queues: q }
  },
  judge_scratch_other_run_corrected: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [SCRATCH + '/run-002/04-qa/run.log'] }), qa('c2')]
    return { args: base(), queues: q }
  },
  // The same scratch root under a second run id: the judge directory and the import destination both carry run-002.
  judge_scratch_second_run: () => {
    const swap = (value) => JSON.parse(JSON.stringify(value).split('run-001').join('run-002'))
    const q = swap(happy())
    q.qa = [swap(qa('c2', 'SUCCESS', undefined, { evidence: [SCRATCH + '/run-002/04-qa/run.log', TARGET + '/tests/test_guide.md'] }))]
    return { args: base({ runId: 'run-002', recordState: true }), queues: q }
  },
  // Case-insensitive collision handling: Run.log, probe/run.log; NOTES.md, a/notes.md, b/Notes.md (the numbered candidates are checked too).
  judge_scratch_case_collision: () => {
    const q = happy()
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [JUDGE + '/04-qa/Run.log', JUDGE + '/04-qa/probe/run.log', TARGET + '/tests/test_guide.md'] })]
    q.reviewer = [review('c2', 'SUCCESS', { evidence: [JUDGE + '/05-review/NOTES.md', JUDGE + '/05-review/a/notes.md', JUDGE + '/05-review/b/Notes.md'] })]
    return { args: base({ recordState: true }), queues: q }
  },
  // One physical file cited under both spellings of the macOS alias is imported once and both citations follow the one destination.
  judge_scratch_alias_spellings: () => {
    const q = happy()
    const plain = JUDGE + '/04-qa/run.log'
    const aliased = '/private' + plain
    q.qa = [qa('c2', 'SUCCESS', undefined, { evidence: [plain, aliased, TARGET + '/tests/test_guide.md'] })]
    q.reviewer = [review('c2', 'SUCCESS', { evidence: ['/private' + JUDGE + '/05-review/notes.md'] })]
    return { args: base({ recordState: true }), queues: q }
  },
  // A target and a scratch root that are siblings (one name is the prefix of the other) in mixed alias spellings are disjoint.
  judge_alias_siblings_accepted: () => {
    const q = JSON.parse(JSON.stringify(happy()).split('/work/target').join('/tmp/m22-sib'))
    return { args: base({ target: '/tmp/m22-sib', plan: '/tmp/m22-sib/plan/DevelopmentPlan.md', scratch: '/private/tmp/m22-sib-scratch' }), queues: q }
  },
  review_finding_without_code: () => {
    const q = happy()
    q.reviewer = [raw(review('c2', 'SUCCESS', { findings: [{ severity: 'LOW', message: 'naming' }] })), review('c2')]
    return { args: base(), queues: q }
  },
  args_scratch_missing: () => ({ args: base({ scratch: undefined }), queues: {} }),
  args_scratch_relative: () => ({ args: base({ scratch: 'tmp/scratch' }), queues: {} }),
  args_scratch_in_target: () => ({ args: base({ target: '/tmp/m22-target', plan: '/tmp/m22-target/plan/DevelopmentPlan.md', scratch: '/tmp/m22-target/scratch' }), queues: {} }),
  args_scratch_around_target: () => ({ args: base({ target: '/tmp/m22-sc/target', plan: '/tmp/m22-sc/target/plan/DevelopmentPlan.md', scratch: '/tmp/m22-sc' }), queues: {} }),
  args_scratch_unsafe_root: () => ({ args: base({ scratch: '/opt/m22/scratch' }), queues: {} }),
  args_scratch_prefix_itself: () => ({ args: base({ scratch: '/tmp' }), queues: {} }),
  // The same tree spelled with and without /private (macOS aliases), and a case variant of the target (the default file system ignores case).
  args_scratch_alias_in_target: () => ({ args: base({ target: '/private/tmp/m22-al/target', plan: '/private/tmp/m22-al/target/plan/DevelopmentPlan.md', scratch: '/tmp/m22-al/target/scratch' }), queues: {} }),
  args_scratch_alias_around_target: () => ({ args: base({ target: '/private/tmp/m22-al2/target', plan: '/private/tmp/m22-al2/target/plan/DevelopmentPlan.md', scratch: '/tmp/m22-al2' }), queues: {} }),
  args_scratch_alias_var_folders: () => ({ args: base({ target: '/private/var/folders/m22/T/target', plan: '/private/var/folders/m22/T/target/plan/DevelopmentPlan.md', scratch: '/var/folders/m22/T/target/scratch' }), queues: {} }),
  args_scratch_case_variant: () => ({ args: base({ target: '/tmp/m22-Case/target', plan: '/tmp/m22-Case/target/plan/DevelopmentPlan.md', scratch: '/tmp/m22-case/target/scratch' }), queues: {} }),
  args_scratch_whitespace: () => ({ args: base({ scratch: '/tmp/m22 scratch' }), queues: {} }),
  args_json_string: () => {
    const given = base({ dialogLang: 'German' })
    return { args: given, rawArgs: JSON.stringify(given), queues: happy() }
  },
  args_missing: () => ({ args: base(), rawArgs: undefined, queues: {} }),
  args_unknown_key: () => ({ args: base({ maxDebugIters: 2 }), queues: {} }),
  args_relative_path: () => ({ args: base({ target: 'relative/target' }), queues: {} }),
  args_whitespace_path: () => ({ args: base({ target: '/work/my target', plan: '/work/my target/plan/DevelopmentPlan.md' }), queues: {} }),
  args_metachar_path: () => ({ args: base({ spec: '/work/specs/m;touch x.md' }), queues: {} }),
  args_quote_path: () => ({ args: base({ framework: "/work/methodology/it's/implementations/claude" }), queues: {} }),
  invalid_maxdebug_negative: () => ({ args: base({ maxDebug: -1 }), queues: {} }),
  invalid_maxdebug_fraction: () => ({ args: base({ maxDebug: 1.5 }), queues: {} }),
  invalid_maxdebug_boolean: () => ({ args: base({ maxDebug: true }), queues: {} }),
  invalid_maxdebug_string: () => ({ args: base({ maxDebug: '4' }), queues: {} }),
  maxdebug_above_supported: () => ({ args: base({ maxDebug: 5 }), queues: {} }),
  recorder_nonzero: () => ({
    args: base({ recordState: true }),
    queues: { searcher: [bootstrap()], architect: [architect()], coder: [code('c2')] },
    recorder: { failAt: 3, stderr: 'methodology state: candidate changes outside parent sourceChange scope' },
  }),
  recorder_null: () => ({
    args: base({ recordState: true }),
    queues: { searcher: [bootstrap()], architect: [architect()] },
    recorder: { nullAt: 2 },
  }),
  code_null_corrected_recorded: () => {
    const q = happy()
    q.coder = [null, code('c2')]
    return { args: base({ recordState: true }), queues: q }
  },
  code_null_control_refused: () => {
    const q = happy()
    q.coder = [null, code('c2')]
    return { args: base({ recordState: true }), queues: q, recorder: { failAt: 3, stderr: 'methodology state: target differs from the candidate' } }
  },
  recorder_throws: () => ({
    args: base({ recordState: true }),
    queues: { searcher: [bootstrap()], architect: [architect()] },
    recorder: { throwAt: 2 },
  }),
  recorder_throws_on_correction: () => {
    const q = happy()
    q.qa = [null]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ recordState: true }), queues: q, recorder: { throwAt: 4 } }
  },
  recorder_throws_on_finalize_correction: () => {
    const q = happy()
    q.architect = [architect(), null]
    return { args: base({ recordState: true }), queues: q, recorder: { throwAt: 6 } }
  },
  recorder_null_on_correction: () => {
    const q = happy()
    q.qa = [null]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ recordState: true }), queues: q, recorder: { nullAt: 4 } }
  },
  recorder_checksum_lie: () => ({
    args: base({ recordState: true }),
    queues: { searcher: [bootstrap()], architect: [architect()] },
    recorder: { lieAt: 2 },
  }),
  recorder_precheck_exit: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT'), qa('c3')]
    q.debugger = [debugFixed('c3', 'qa', { filesTouched: [TARGET + '/tests/test_a.py'] }), debugFixed('c3', 'qa')]
    q.reviewer = [review('c3')]
    q.architect[1] = finalizeOk('c3')
    return { args: base({ recordState: true }), queues: q, recorder: { precheckAt: 5 } }
  },
  ledger_spend_mismatch: () => {
    const q = happy()
    q.qa = [qa('c2', 'BUG_REPORT')]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ recordState: true }), queues: q, recorder: { offsetFrom: 4 } }
  },
  null_twice_recorded: () => {
    const q = happy()
    q.qa = [null, null]
    q.reviewer = []
    q.architect = [architect()]
    return { args: base({ recordState: true }), queues: q }
  },
  finalize_null_twice_recorded: () => {
    const q = happy()
    q.architect = [architect(), null, null]
    return { args: base({ recordState: true }), queues: q }
  },
  spec_blocked_recorded: () => ({
    args: base({ recordState: true }),
    queues: { searcher: [bootstrap()], architect: [architect({ specBlocked: true, blockReason: 'AC-1 and AC-2 contradict numerically', specDeficiencies: ['AC-1 versus AC-2'] })] },
  }),
}
// endregion FUNC_SCENARIOS

// region FUNC_parseRecorderPrompt [DOMAIN(8): RunState; CONCEPT(9): CommandsFromPrompt; TECH(5): RegExp]
// ## @purpose Extract from a recorder prompt the record text, the diagnostic text and its target path, the paths, the import list of the precheck command and every command the prompt quotes, tolerating quoted and unquoted path spellings.
// ## @uses String.prototype.match, String.prototype.split
// ## @io string -> object
// ## @complexity 7
function parseRecorderPrompt(prompt) {
  const lines = prompt.split('\n')
  const from = lines.indexOf('BEGIN-RECORD-JSON')
  const dfrom = lines.indexOf('BEGIN-DIAGNOSTIC')
  const dto = lines.indexOf('END-DIAGNOSTIC')
  const lineWith = (prefix) => lines.find((l) => l.indexOf(prefix) === 0) || null
  const runOf = (prefix) => {
    const l = lineWith(prefix)
    if (l === null) return null
    const at = l.indexOf(' RUN: ')
    return at >= 0 ? l.slice(at + 6) : null
  }
  const l1 = lineWith('STEP 1')
  const l4 = lineWith('STEP 4')
  const cmd4 = l4 ? l4.slice(l4.indexOf('python3 ')) : ''
  const grab = (re, source) => {
    const m = (source || prompt).match(re)
    return m ? m[0] : null
  }
  const expect3b = lineWith('STEP 3b EXPECT')
  const expected = expect3b ? expect3b.match(/exactly "(\d+) (\d+)"/) : null
  const l2a = lineWith('STEP 2a')
  const precheck = runOf('STEP 3c')
  const importMatch = precheck ? precheck.match(/ '(\[\[.*\]\])'\s*$/) : null
  return {
    diagPath: l2a ? (l2a.match(/ to '([^']+)'\.\s*$/) || [])[1] || null : null,
    imports: importMatch ? JSON.parse(importMatch[1]) : [],
    text: from >= 0 ? lines[from + 1] : null,
    singleLine: from >= 0 && lines.indexOf('END-RECORD-JSON') === from + 2,
    diagnostic: dfrom >= 0 ? lines.slice(dfrom + 1, dto).join('\n') : null,
    mkdir: l1 ? l1.slice(l1.indexOf('mkdir -p')) : null,
    cmd4: cmd4,
    recordPath: (cmd4.match(/--result '?([^'\s]+)'?/) || [])[1] || null,
    outPath: (cmd4.match(/> '?([^'\s]+)'? 2>/) || [])[1] || null,
    errPath: (cmd4.match(/2> '?([^'\s]+)'?\s*$/) || [])[1] || null,
    parseCheck: grab(/python3 -c "import json,sys; json\.load\(open\(sys\.argv\[1\]\)\)" '?[^'\s]+'?/),
    checksum: runOf('STEP 3b'),
    expectedLength: expected ? Number(expected[1]) : null,
    expectedSum: expected ? Number(expected[2]) : null,
    precheck: precheck,
    oldPrune: lineWith('STEP 2b') !== null,
    readback: grab(/python3 -c "import json,sys; s=json\.load\(open[^"]*" '?[^'\s]+'?/),
    stepLabels: lines.filter((l) => /^STEP /.test(l)).map((l) => l.split(':')[0]),
  }
}
// endregion FUNC_parseRecorderPrompt

// region FUNC_checksumOf [DOMAIN(5): Integrity; CONCEPT(7): LengthAndCodeUnitSum; TECH(4): JavaScript]
// ## @purpose Compute the length and the sum of UTF-16 code units modulo 2^32 of a text, the scheme the recorder reproduces with a one-line python command.
// ## @uses String.prototype.charCodeAt
// ## @io string -> {length, sum}
// ## @complexity 2
function checksumOf(text) {
  let sum = 0
  for (let i = 0; i < text.length; i += 1) sum = (sum + text.charCodeAt(i)) % 4294967296
  return { length: text.length, sum: sum }
}
// endregion FUNC_checksumOf

// region FUNC_makeRecorder [DOMAIN(8): RunState; CONCEPT(9): LedgerEmulation; TECH(5): JavaScript]
// ## @purpose Emulate the recorder agent of the fake mode: parse the record from its prompt, apply the helper's Debug-entry and response-correction rules to a fake ledger and answer with the compact readback and the checksum the script expects, or fail on demand.
// ## @uses parseRecorderPrompt, checksumOf, JSON.parse, JSON.stringify
// ## @io object, object, object[] -> function(prompt, schema) -> object or null
// ## @complexity 8
// BUG_FIX_CONTEXT: the fake ledger accepted anything and answered with three fields only; it now reproduces the checksum and
// precheck answers of the recorder contract and the helper's response-correction episodes, but the fake stays a speed aid: the
// real-helper scenarios are the authority on what the ledger accepts.
function makeRecorder(args, opts, records) {
  const cap = args.maxDebug === undefined ? 4 : args.maxDebug
  const ledger = { status: 'RUNNING', phase: 'bootstrap', debug_spent: 0, episodes: 0 }
  const next = { bootstrap: 'architect', architect: 'code', code: 'qa', qa: 'review', review: 'finalize', debug: 'qa', finalize: 'finalize' }
  let n = 0
  return function (prompt, schema) {
    n += 1
    const p = parseRecorderPrompt(prompt)
    const record = JSON.parse(p.text)
    const result = record.kind === 'role' ? record.result : null
    records.push({
      n,
      file: p.recordPath,
      command: p.cmd4,
      phase: result ? result.phase : record.phase,
      status: result ? result.status : record.event,
      kind: record.kind,
      context: record.context || null,
      evidence: record.kind === 'control' ? record.evidence : null,
      unknownEffect: record.kind === 'control' ? record.unknownEffect : null,
      diagnostic: p.diagnostic,
      precheckStep: p.precheck !== null || p.oldPrune,
      imports: p.imports,
      diagPath: p.diagPath,
      ascii: /^[\x20-\x7e]*$/.test(p.text),
      singleLine: p.singleLine,
      steps: p.stepLabels,
      checksumLine: p.checksum,
      expectedLength: p.expectedLength,
      expectedSum: p.expectedSum,
      text: p.text,
    })
    if (opts.nullAt === n) return null
    if (opts.throwAt === n) throw new Error('recorder transport fault')
    const sums = checksumOf(p.text)
    const isDebug = record.kind === 'role' && record.result.phase === 'debug'
    const answer = { exitCode: 0, stdout: '', stderr: '', recordLength: sums.length, recordSum: sums.sum + (opts.lieAt === n ? 1 : 0), artifactsKept: isDebug ? 1 : -1 }
    if (opts.precheckAt === n && p.precheck !== null) {
      answer.exitCode = 3
      answer.stderr = 'PRECHECK_FAILED ' + (opts.precheckLine || '{"kept": 0, "missing": ["' + TARGET + '/tests/test_a.py"], "count": 1}')
      answer.artifactsKept = isDebug ? 0 : -1
      return answer
    }
    if (opts.failAt === n) {
      answer.exitCode = 2
      answer.stderr = opts.stderr || 'methodology state: refused'
      return answer
    }
    if (result && result.phase === 'architect' && result.status === 'SUCCESS' && result.specBlocked === true) {
      answer.exitCode = 2
      answer.stderr = 'methodology state: SPEC_BLOCKED: Architect human deficiency'
      return answer
    }
    if (record.kind === 'control') {
      ledger.episodes += 1
      if (ledger.episodes > 1) ledger.status = record.phase === 'finalize' ? 'ESCALATED_FINALIZE' : 'BLOCKED'
    } else {
      const r = record.result
      if (r.status === 'BUG_REPORT') {
        if (ledger.debug_spent >= cap) ledger.status = 'ESCALATED'
        else {
          ledger.debug_spent += 1
          ledger.phase = 'debug'
        }
      } else if (r.status === 'BLOCKED' || r.status === 'ESCALATED_FINALIZE') {
        ledger.status = r.status
      } else {
        ledger.phase = next[r.phase]
        if (r.phase === 'finalize') ledger.status = 'SUCCESS'
      }
      ledger.episodes = 0
    }
    const shown = ledger.debug_spent + (opts.offsetFrom !== undefined && n >= opts.offsetFrom ? 1 : 0)
    answer.stdout = JSON.stringify({ state: { status: ledger.status, phase: ledger.phase, debug_spent: shown } })
    return answer
  }
}
// endregion FUNC_makeRecorder

// region FUNC_sh [DOMAIN(5): Process; CONCEPT(6): RealCommand; TECH(5): child_process]
// ## @purpose Run one shell command exactly as written and return its real exit code and streams; no byte-code is written.
// ## @uses child_process.spawnSync
// ## @io string -> {code, out, err}
// ## @complexity 3
function sh(command) {
  const r = spawnSync('/bin/bash', ['-c', command], {
    encoding: 'utf8',
    env: Object.assign({}, process.env, { PYTHONDONTWRITEBYTECODE: '1' }),
    maxBuffer: 256 * 1024 * 1024,
  })
  return { code: r.status === null ? 1 : r.status, out: r.stdout || '', err: r.stderr || '' }
}
// endregion FUNC_sh

// region FUNC_realRecorder [DOMAIN(9): RunState; CONCEPT(10): ShellExecutionOfPrompt, HelperIsAuthority; TECH(6): child_process]
// ## @purpose Behave as the recorder agent would: make the directory, write the record text and the diagnostic text verbatim, run the quoted checksum and precheck commands, run the quoted helper command once, and report the real exit code, readback and stderr tail; the harness decides nothing about acceptance.
// ## @uses parseRecorderPrompt, sh, checksumOf, fs.writeFileSync
// ## @io string, object, object -> object
// ## @complexity 9
function realRecorder(prompt, schema, opts, world) {
  const p = parseRecorderPrompt(prompt)
  const record = JSON.parse(p.text)
  const result = record.kind === 'role' ? record.result : null
  const row = {
    n: world.records.length + 1,
    phase: result ? result.phase : record.phase,
    status: result ? result.status : record.event,
    kind: record.kind,
    context: record.context || null,
    steps: p.stepLabels,
    cmd4: p.cmd4,
    text: p.text,
    helperExit: null,
    reason: null,
    stderrTail: null,
    checksumExit: null,
    pruneOut: null,
  }
  world.records.push(row)
  const finish = (answer) => {
    const out = {}
    Object.keys(schema.properties).forEach((k) => {
      if (answer[k] !== undefined) out[k] = answer[k]
    })
    row.answer = out
    return out
  }
  const fail = (code, reason) => finish({ exitCode: code, stdout: '', stderr: reason, recordLength: 0, recordSum: 0, artifactsKept: -1 })
  if (opts.nullAt === row.n) return null
  if (!p.mkdir || !p.recordPath || !p.outPath || !p.errPath) throw new Error('recorder prompt lacks a quoted mkdir or helper command: ' + p.stepLabels.join(','))
  if (sh(p.mkdir).code !== 0) return fail(1, 'mkdir failed')
  const written = opts.corruptAt === row.n ? p.text.replace('summary', 'summarz') : p.text
  writeFileSync(p.recordPath, written)
  if (p.diagnostic !== null) {
    if (record.kind !== 'control' || !record.evidence || !record.evidence[0]) throw new Error('diagnostic text without a control record')
    // BUG_FIX_CONTEXT: the stub wrote the diagnostic to record.evidence[0], so a recorder prompt that named another path in STEP 2a
    // passed unnoticed; the stub now writes to the path STEP 2a names, which must equal the control evidence path.
    if (p.diagPath === null || p.diagPath !== record.evidence[0]) throw new Error('STEP 2a path ' + p.diagPath + ' differs from the control evidence path ' + record.evidence[0])
    writeFileSync(p.diagPath, p.diagnostic)
  }
  if (p.parseCheck && sh(p.parseCheck).code !== 0) return fail(1, 'record does not parse')
  let sums = checksumOf(written)
  if (p.checksum !== null) {
    const c = sh(p.checksum)
    row.checksumExit = c.code
    const parts = c.out.trim().split(/\s+/)
    sums = { length: Number(parts[0]), sum: Number(parts[1]) }
    if (c.code !== 0 || p.expectedLength === null || sums.length !== p.expectedLength || sums.sum !== p.expectedSum) {
      return finish({ exitCode: 4, stdout: '', stderr: 'RECORD_CHECKSUM_MISMATCH', recordLength: sums.length || 0, recordSum: sums.sum || 0, artifactsKept: -1 })
    }
  }
  let kept = -1
  if (p.precheck !== null) {
    const pr = sh(p.precheck)
    row.pruneOut = pr.out.trim()
    let report = null
    try {
      report = JSON.parse(pr.out)
    } catch (e) {
      report = null
    }
    if (pr.code !== 0 || report === null) return fail(1, 'the precheck command failed: ' + pr.err.split('\n').slice(-2).join(' | '))
    kept = report.kept
    if (report.count > 0 || kept === 0) {
      return finish({ exitCode: 3, stdout: '', stderr: 'PRECHECK_FAILED ' + pr.out.trim(), recordLength: sums.length, recordSum: sums.sum, artifactsKept: kept })
    }
  } else if (p.oldPrune) {
    const pruned = JSON.parse(readFileSync(p.recordPath, 'utf8'))
    const survivors = pruned.context.sourceChange.artifacts.filter((a) => existsSync(a) && lstatSync(a).isFile())
    pruned.context.sourceChange.artifacts = survivors
    writeFileSync(p.recordPath, JSON.stringify(pruned))
    kept = survivors.length
  }
  const run = sh(p.cmd4)
  row.helperExit = run.code
  const errText = existsSync(p.errPath) ? readFileSync(p.errPath, 'utf8') : ''
  const reasonLine = errText.split('\n').filter((l) => l.indexOf('methodology state:') === 0).pop() || null
  row.reason = reasonLine
  if (run.code !== 0) {
    const tailCommand = (prompt.match(/tail -c 4000 '?[^'\s]+'?/) || [])[0] || null
    const stderr = tailCommand ? sh(tailCommand).out : errText.slice(0, 4000)
    row.stderrTail = stderr
    return finish({ exitCode: run.code, stdout: '', stderr: stderr, recordLength: sums.length, recordSum: sums.sum, artifactsKept: kept })
  }
  const rb = p.readback ? sh(p.readback) : { out: '' }
  return finish({ exitCode: 0, stdout: rb.out.trim(), stderr: '', recordLength: sums.length, recordSum: sums.sum, artifactsKept: kept })
}
// endregion FUNC_realRecorder

// region FUNC_realRoles [DOMAIN(9): Fixtures; CONCEPT(10): RealIdentities, TargetEdits; TECH(6): child_process]
// ## @purpose Build the scripted roles of the real-helper mode: each role derives inputIdentity with the show command and candidateIdentity with the digest command quoted in its own prompt, edits the owned target as a real role would, and returns a canonical envelope; scenario overrides wrap the default behavior to inject one defect.
// ## @uses sh, fs.writeFileSync, fs.mkdirSync
// ## @io object -> map role -> function(context) -> object
// ## @complexity 9
function realRoles(world) {
  const T = world.target
  const P = (rel) => T + '/' + rel
  const GUIDE = P('tests/test_guide.md')
  const LOG = P('.methodology/evidence/' + world.runId + '/run.log')
  const MAPREL = world.mapRel || 'doxygen_output/xml'
  const MAP = P(MAPREL)
  const INDEX = MAP + '/index.xml'
  const REPORT = P('.methodology/evidence/' + world.runId + '/final-report.md')
  const env = (phase, role, status, ids, payload, evidence) =>
    Object.assign({ phase, role, status, summary: phase + ' ' + status, runId: world.runId, inputIdentity: ids.input, candidateIdentity: ids.cand, contractVersion: CONTRACT, evidence }, payload)
  const rscans = (over, evidence) => SCAN_IDS.map((id) => ({ id, status: (over && over[id]) || 'PASS', reason: id + ' judged', evidence: evidence || [GUIDE] }))
  const ids = (s) => ({ input: s.input_identity, cand: s.candidate.digest })
  const writeAll = () => {
    world.write('src/a.py', 'def a():\n    return 1\n')
    world.write('tests/test_a.py', 'def test_a():\n    assert True\n')
    world.write('tests/test_guide.md', '# guide\n')
    world.write('.methodology/evidence/' + world.runId + '/run.log', 'ok\n')
    world.write(MAPREL + '/index.xml', '<doxygenindex/>\n')
  }
  const roles = {
    searcher: (c) => {
      const s = c.readState()
      return env('bootstrap', 'searcher', 'SUCCESS', { input: s.input_identity, cand: s.candidate.digest }, {
        isEmpty: false,
        classificationHint: 'BROWNFIELD',
        fileCount: 1,
        files: [{ path: 'src/a.py', summary: 'module a', structure: 'one function', relevance: 'edit target' }],
        recommendations: ['read src/a.py'],
        limitations: ['bounded'],
      }, [c.stateFile])
    },
    architect: (c) => {
      const s = c.showOrState()
      if (c.afterShow) c.afterShow()
      world.write('plan/DevelopmentPlan.md', '# Development plan\nSlice S1: a() returns one.\n')
      return env('architect', 'architect', 'SUCCESS', { input: s.input_identity, cand: c.digest() }, {
        classification: 'BROWNFIELD',
        projectType: 'Plugin System',
        taskType: 'Code and Tests',
        planPath: world.plan,
        featureSlices: [{ id: 'S1', description: 'a returns one', files: ['src/a.py', 'tests/test_a.py'], ui: false }],
        mayEdit: ['src/a.py', 'tests/test_a.py', 'tests/test_guide.md'],
        doNotTouch: ['docs/readme.md'],
        acceptanceCriteria: [{ id: 'AC-1', text: 'a returns one', measurable: true, threshold: '>= 1 test' }],
        specDeficiencies: [],
        specBlocked: false,
        visualGate: { status: 'NOT_APPLICABLE', output: 'gate not active', componentNodes: 1, testsOnly: false, reason: 'fewer than three component nodes' },
      }, [world.plan])
    },
    coder: (c) => {
      const s = c.show()
      writeAll()
      const cand = c.digest()
      return env('code', 'coder', 'SUCCESS', { input: s.input_identity, cand }, {
        artifacts: [P('src/a.py'), P('tests/test_a.py'), GUIDE],
        testGuidePath: GUIDE,
        testSummary: '3 passed',
        deviations: [],
        measurements: ['AC-1: measured=3 >= 1 met'],
        logs: [LOG],
        doxygen: { command: 'doxygen Doxyfile', exitCode: 0, output: 'no warnings', evidence: [INDEX], mapPath: MAP, candidateIdentity: cand, inputIdentity: s.input_identity },
      }, [GUIDE])
    },
    qa: (c) => {
      const s = c.show()
      return env('qa', 'qa', 'SUCCESS', { input: s.input_identity, cand: s.candidate.digest }, { testSummary: '3 passed', scans: rscans(), findings: [], limitations: ['visual not judged'] }, [GUIDE])
    },
    reviewer: (c) => {
      const s = c.show()
      return env('review', 'reviewer', 'SUCCESS', { input: s.input_identity, cand: s.candidate.digest }, { findings: [], limitations: ['no live service'], diffEvidence: [P('src/a.py')], scopeJudgment: 'every changed path is inside MAY EDIT' }, [P('src/a.py')])
    },
    debugger: (c) => {
      const s = c.show()
      world.write('src/a.py', 'def a():\n    # BUG_FIX_CONTEXT: the old value was wrong (repair ' + c.n + ')\n    return 1\n')
      const touched = [P('src/a.py')]
      if (!existsSync(GUIDE)) {
        writeAll()
        touched.push(P('tests/test_a.py'), GUIDE)
      }
      return env('debug', 'debugger', 'FIXED', { input: s.input_identity, cand: c.digest() }, {
        rootCause: 'wrong value returned',
        fix: 'return one',
        filesTouched: touched,
        postFixAudit: 'only files inside MAY EDIT changed',
        testSummary: '3 passed',
        regressionEvidence: [GUIDE],
        origin: s.debug_origin.phase,
      }, [P('src/a.py')])
    },
    finalize: (c) => {
      const s = c.show()
      world.write('.methodology/evidence/' + world.runId + '/final-report.md', '# final report\n')
      return env('finalize', 'architect', 'SUCCESS', { input: s.input_identity, cand: s.candidate.digest }, {
        report: REPORT,
        classification: 'BROWNFIELD',
        planPath: world.plan,
        testsPath: GUIDE,
        logPath: LOG,
        doxygenPath: INDEX,
        testSummary: '3 passed',
        acceptanceEvidence: [GUIDE],
        qaEvidence: [GUIDE],
        reviewEvidence: [GUIDE],
        liveEvidence: [LOG],
        blastRadius: { added: ['tests/test_a.py'], modified: ['src/a.py'], deleted: [], untracked: [] },
        scopeDeviations: [],
        limitations: ['no merge or deploy performed'],
      }, [GUIDE])
    },
  }
  roles.helpers = { P, GUIDE, LOG, MAP, INDEX, REPORT, env, rscans, ids, writeAll }
  return roles
}
// endregion FUNC_realRoles

// region FUNC_REAL_SCENARIOS [DOMAIN(9): Scenarios; CONCEPT(9): RouteCoverage, DiscriminatingNegatives; TECH(4): JavaScript]
// ## @purpose Declare every real-helper scenario: the cap for run_state.py init, optional recorder options and the role overrides, each wrapping a default role so that exactly one defect is injected.
// ## @uses none
// ## @io none -> map name -> (world, roles) => {maxDebug, recorder, over}
// ## @complexity 8
const qaBugOver = (world, h) => (c, dflt) => {
  if (c.n !== 1) return dflt(c)
  const s = c.show()
  return h.env('qa', 'qa', 'BUG_REPORT', { input: s.input_identity, cand: s.candidate.digest }, {
    testSummary: '3 passed',
    scans: h.rscans({ 'semantic-trace': 'FAIL' }),
    findings: [{ scan: 'semantic-trace', code: 'SEMANTIC_TRACE_MISSING', severity: 'MEDIUM', message: 'no trace', evidence: [h.P('src/a.py')], path: 'src/a.py', line: 1 }],
    limitations: ['visual not judged'],
    bugReport: bug('qa'),
  }, [h.GUIDE])
}
const mutate = (fn) => (c, dflt) => (c.n === 1 ? fn(dflt(c), c) : dflt(c))
const naCoder = (h, quote) => (c, dflt) => {
  const r = dflt(c)
  r.doxygen = {
    status: 'NOT_APPLICABLE',
    reason: 'the host instructions forbid running Doxygen',
    prohibition: { path: h.P('AGENTS.md'), quote: quote },
    evidence: [h.P('AGENTS.md')],
    candidateIdentity: r.candidateIdentity,
    inputIdentity: r.inputIdentity,
  }
  return r
}
const REAL_SCENARIOS = {
  real_green: () => ({ maxDebug: 4, over: () => ({}) }),
  real_silent_builds: () => ({
    maxDebug: 4,
    over: () => ({
      architect: (c, dflt) => {
        const r = dflt(c)
        r.visualGate.output = ''
        return r
      },
      coder: (c, dflt) => {
        const r = dflt(c)
        r.doxygen.output = ''
        return r
      },
    }),
  }),
  real_debug_qa: () => ({ maxDebug: 4, over: (w, h) => ({ qa: qaBugOver(w, h) }) }),
  real_debug_code: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      coder: (c, dflt) => {
        if (c.n !== 1) return dflt(c)
        const s = c.show()
        w.write('src/a.py', 'def a():\n    return 9\n')
        return h.env('code', 'coder', 'BUG_REPORT', { input: s.input_identity, cand: c.digest() }, { artifacts: [h.P('src/a.py')], bugReport: bug('code') }, [h.P('src/a.py')])
      },
    }),
  }),
  real_debug_review: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      reviewer: (c, dflt) => {
        if (c.n !== 1) return dflt(c)
        const s = c.show()
        return h.env('review', 'reviewer', 'BUG_REPORT', { input: s.input_identity, cand: s.candidate.digest }, {
          findings: [{ severity: 'HIGH', message: 'wrong comparison', path: 'src/a.py', line: 2, code: 'LOGIC', evidence: [h.P('src/a.py')] }],
          limitations: ['no live service'],
          diffEvidence: [h.P('src/a.py')],
          scopeJudgment: 'inside MAY EDIT',
          bugReport: bug('review'),
        }, [h.P('src/a.py')])
      },
    }),
  }),
  real_cap_zero: () => ({ maxDebug: 0, over: (w, h) => ({ qa: qaBugOver(w, h) }) }),
  real_bound_plan: () => ({ maxDebug: 4, planFirst: true, over: () => ({}) }),
  real_debug_twice: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: qaBugOver(w, h),
      reviewer: (c, dflt) => {
        if (c.n !== 1) return dflt(c)
        const s = c.show()
        return h.env('review', 'reviewer', 'BUG_REPORT', { input: s.input_identity, cand: s.candidate.digest }, {
          findings: [{ severity: 'HIGH', message: 'wrong comparison', path: 'src/a.py', line: 2, code: 'LOGIC', evidence: [h.P('src/a.py')] }],
          limitations: ['no live service'],
          diffEvidence: [h.P('src/a.py')],
          scopeJudgment: 'inside MAY EDIT',
          bugReport: bug('review'),
        }, [h.P('src/a.py')])
      },
    }),
  }),
  real_visual_gate_pass: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      architect: (c, dflt) => {
        const r = dflt(c)
        w.write('.methodology/evidence/' + w.runId + '/visual-gate.txt', 'scanned 4 nodes, no violations\n')
        r.visualGate = { status: 'PASS', output: 'scanned 4 nodes, no violations', componentNodes: 4, testsOnly: false, command: 'python3 visual_gate_lint.py plan', exitCode: 0, scannedNodes: 4, evidence: [h.P('.methodology/evidence/' + w.runId + '/visual-gate.txt')] }
        r.candidateIdentity = c.digest()
        return r
      },
    }),
  }),
  real_architect_blocked_spec: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      architect: (c) => {
        const s = c.showOrState()
        return h.env('architect', 'architect', 'BLOCKED', { input: s.input_identity, cand: s.candidate.digest }, {
          reason: 'the required external image tag cannot be verified',
          limitations: ['no network'],
          specBlocked: true,
          blockReason: 'the external image tag cannot be verified',
          specDeficiencies: ['unverifiable external identifier'],
        }, [w.stateFile])
      },
    }),
  }),
  real_doxygen_prohibited: () => ({
    maxDebug: 4,
    files: { 'AGENTS.md': 'Doxygen documentation is optional in this repository.\nDo not run doxygen in this repository.\n' },
    over: (w, h) => ({
      coder: (c, dflt) => naCoder(h, 'Do not run doxygen in this repository.')(c, dflt),
      finalize: (c, dflt) => {
        const r = dflt(c)
        delete r.doxygenPath
        return r
      },
    }),
  }),
  real_doxygen_quote_no_denial: () => ({
    maxDebug: 4,
    files: { 'AGENTS.md': 'Doxygen documentation is optional in this repository.\nDo not run doxygen in this repository.\n' },
    over: (w, h) => ({
      coder: (c, dflt) => (c.n === 1 ? naCoder(h, 'Doxygen documentation is optional in this repository.')(c, dflt) : naCoder(h, 'Do not run doxygen in this repository.')(c, dflt)),
      finalize: (c, dflt) => {
        const r = dflt(c)
        delete r.doxygenPath
        return r
      },
    }),
  }),
  real_doxygen_quote_paraphrase: () => ({
    maxDebug: 4,
    files: { 'AGENTS.md': 'Doxygen documentation is optional in this repository.\nDo not run doxygen in this repository.\n' },
    over: (w, h) => ({
      coder: (c, dflt) => (c.n === 1 ? naCoder(h, 'Doxygen must not be executed in this repository.')(c, dflt) : naCoder(h, 'Do not run doxygen in this repository.')(c, dflt)),
      finalize: (c, dflt) => {
        const r = dflt(c)
        delete r.doxygenPath
        return r
      },
    }),
  }),
  real_doxygen_pass_extra_field: () => ({
    maxDebug: 4,
    over: () => ({
      coder: mutate((r) => {
        r.doxygen.reason = 'an extra field that belongs to the prohibition arm'
        return r
      }),
    }),
  }),
  real_debug_blocked: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: qaBugOver(w, h),
      debugger: (c) => {
        const s = c.show()
        return h.env('debug', 'debugger', 'BLOCKED', { input: s.input_identity, cand: s.candidate.digest }, {
          rootCause: 'the failing service cannot be reproduced',
          reason: 'the service needed to reproduce the defect is unavailable',
          limitations: ['no reproducer'],
        }, [h.GUIDE])
      },
    }),
  }),
  real_scope_directory: () => ({ maxDebug: 4, over: () => ({ architect: mutate((r) => Object.assign(r, { mayEdit: ['src/', 'tests/test_a.py', 'tests/test_guide.md'] })) }) }),
  real_scope_dot_slash: () => ({ maxDebug: 4, over: () => ({ architect: mutate((r) => Object.assign(r, { mayEdit: ['./src/a.py', 'tests/test_a.py', 'tests/test_guide.md'] })) }) }),
  real_scope_dotdot: () => ({ maxDebug: 4, over: () => ({ architect: mutate((r) => Object.assign(r, { mayEdit: ['src/../src/a.py', 'tests/test_a.py', 'tests/test_guide.md'] })) }) }),
  real_scope_absolute: () => ({ maxDebug: 4, over: (w) => ({ architect: mutate((r) => Object.assign(r, { mayEdit: [w.target + '/src/a.py', 'tests/test_a.py', 'tests/test_guide.md'] })) }) }),
  real_evidence_spec: () => ({ maxDebug: 4, over: (w) => ({ searcher: mutate((r) => Object.assign(r, { evidence: [w.spec] })) }) }),
  real_architect_extra_file: () => ({
    maxDebug: 4,
    over: (w) => ({
      architect: (c, dflt) => {
        if (c.n === 1) {
          c.afterShow = () => w.write('plan/BR.md', '# business requirements\n')
          return { __raw: true, value: Object.assign(dflt(c), { businessRequirementsPath: w.target + '/plan/BR.md' }) }
        }
        rmSync(w.target + '/plan/BR.md', { force: true })
        return dflt(c)
      },
    }),
  }),
  real_finalize_directory: () => ({ maxDebug: 4, over: (w, h) => ({ finalize: mutate((r) => Object.assign(r, { doxygenPath: h.MAP })) }) }),
  real_debug_delete_only: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: qaBugOver(w, h),
      debugger: (c) => {
        const s = c.show()
        rmSync(w.target + '/tests/test_a.py', { force: true })
        return h.env('debug', 'debugger', 'FIXED', { input: s.input_identity, cand: c.digest() }, {
          rootCause: 'a faulty test file',
          fix: 'delete tests/test_a.py',
          filesTouched: [h.P('tests/test_a.py')],
          postFixAudit: 'only the faulty test file was removed',
          testSummary: '2 passed',
          regressionEvidence: [h.GUIDE],
          origin: s.debug_origin.phase,
        }, [h.GUIDE])
      },
    }),
  }),
  real_debug_no_survivor: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: qaBugOver(w, h),
      debugger: (c) => {
        const s = c.show()
        let touched = [h.P('tests/test_a.py')]
        let evidence = [h.P('tests/test_a.py')]
        if (c.n === 1) {
          rmSync(w.target + '/tests/test_a.py', { force: true })
        } else {
          w.write('src/a.py', 'def a():\n    # BUG_FIX_CONTEXT: a faulty test file was deleted\n    return 1\n')
          touched = [h.P('src/a.py')]
          evidence = [h.GUIDE]
        }
        return h.env('debug', 'debugger', 'FIXED', { input: s.input_identity, cand: c.digest() }, {
          rootCause: 'a faulty test file',
          fix: 'delete tests/test_a.py',
          filesTouched: touched,
          postFixAudit: 'only files inside MAY EDIT changed',
          testSummary: '2 passed',
          regressionEvidence: evidence,
          origin: s.debug_origin.phase,
        }, [h.GUIDE])
      },
    }),
  }),
  real_refusal_reason: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      coder: (c, dflt) => {
        const r = dflt(c)
        w.write('docs/unlisted.txt', 'written outside MAY EDIT and not listed in artifacts\n')
        r.candidateIdentity = c.digest()
        r.doxygen.candidateIdentity = r.candidateIdentity
        return r
      },
    }),
  }),
  real_nonexistent_evidence: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: (c, dflt) => {
        const r = dflt(c)
        if (c.n === 1) r.evidence = [h.P('evidence/never-written.txt')]
        return r
      },
    }),
  }),
  real_nonexistent_evidence_twice: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: (c, dflt) => Object.assign(dflt(c), { evidence: [h.P('evidence/never-written.txt')] }),
    }),
  }),
  real_transport_throw: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      coder: (c, dflt) => {
        if (c.n !== 1) return dflt(c)
        h.writeAll()
        throw new Error('transport fault after the edits')
      },
    }),
  }),
  real_qa_null_twice: () => ({ maxDebug: 4, over: () => ({ qa: () => null }) }),
  real_finalize_null_twice: () => ({ maxDebug: 4, over: () => ({ finalize: () => null }) }),
  real_code_null_then_ok: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      coder: (c, dflt) => {
        if (c.n !== 1) return dflt(c)
        h.writeAll()
        return null
      },
    }),
  }),
  real_spec_blocked: () => ({
    maxDebug: 4,
    over: () => ({ architect: mutate((r) => Object.assign(r, { specBlocked: true, blockReason: 'AC-1 and AC-2 contradict numerically', specDeficiencies: ['AC-1 versus AC-2'] })) }),
  }),
  real_visual_gate_fail: () => ({
    maxDebug: 4,
    over: () => ({ architect: mutate((r) => Object.assign(r, { visualGate: { status: 'FAIL', output: 'lint: 4 violations', componentNodes: 4, testsOnly: false } })) }),
  }),
  real_scope_deviation: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      coder: (c, dflt) => {
        const r = dflt(c)
        w.write('docs/readme.md', '# touched outside the scope\n')
        r.artifacts = r.artifacts.concat([h.P('docs/readme.md')])
        r.candidateIdentity = c.digest()
        r.doxygen.candidateIdentity = r.candidateIdentity
        return r
      },
    }),
  }),
  real_checksum_corrupt: () => ({ maxDebug: 4, recorder: { corruptAt: 1 }, over: () => ({}) }),
  // A judge writes its outputs in the scratch directory its prompt grants and cites them: QA 1 is a red run (BUG_REPORT), QA 2 is
  // green after the Debug entry, the reviewer cites two files with one basename; the helper must accept the records with the
  // imported in-target paths.
  real_judge_scratch: () => ({
    maxDebug: 4,
    dumpPrompts: true,
    over: (w, h) => ({
      qa: (c) => {
        const s = c.show()
        const log = c.judgeWrite('run.log', 'pytest run ' + c.n + ': 3 passed\n')
        const probe = c.judgeWrite('probe/run.log', 'probe of run ' + c.n + ' (same basename as the log)\n')
        const note = c.judgeWrite('notes/report.md', '# qa report ' + c.n + '\n')
        if (c.n === 1) {
          return h.env('qa', 'qa', 'BUG_REPORT', h.ids(s), {
            testSummary: '1 failed',
            scans: h.rscans({ 'semantic-trace': 'FAIL' }, [note]),
            findings: [{ scan: 'semantic-trace', code: 'SEMANTIC_TRACE_MISSING', severity: 'MEDIUM', message: 'no trace', evidence: [probe], path: 'src/a.py', line: 1 }],
            limitations: ['visual not judged'],
            bugReport: bug('qa'),
          }, [log, probe, h.GUIDE])
        }
        return h.env('qa', 'qa', 'SUCCESS', h.ids(s), {
          testSummary: '3 passed',
          scans: h.rscans(undefined, [note]),
          findings: [{ scan: 'discriminating-test', code: 'WEAK_ASSERT', severity: 'LOW', message: 'one assertion is weak', evidence: [log], path: 'tests/test_a.py', line: 1 }],
          limitations: ['visual not judged'],
        }, [log, h.GUIDE])
      },
      reviewer: (c) => {
        const s = c.show()
        const notes = c.judgeWrite('review-notes.md', '# review notes\n')
        const other = c.judgeWrite('probe/review-notes.md', '# a second file with the same basename\n')
        return h.env('review', 'reviewer', 'SUCCESS', h.ids(s), {
          findings: [{ code: 'STYLE', severity: 'LOW', message: 'naming', evidence: [other], path: 'src/a.py', line: 1 }],
          limitations: ['no live service'],
          diffEvidence: [h.P('src/a.py'), notes],
          scopeJudgment: 'every changed path is inside MAY EDIT',
        }, [notes, other])
      },
    }),
  }),
  // The first QA return cites a scratch file that was never written: the precheck refuses it before the helper, nothing is copied,
  // the one correction follows and the corrected return is imported.
  real_judge_scratch_missing: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: (c) => {
        const s = c.show()
        if (c.n === 1) {
          return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [c.scratchDir() + '/never-written.log']), findings: [], limitations: ['visual not judged'] }, [c.scratchDir() + '/never-written.log'])
        }
        const log = c.judgeWrite('run.log', 'pytest run: 3 passed\n')
        return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [log]), findings: [], limitations: ['visual not judged'] }, [log])
      },
    }),
  }),
  // The documented refusals of the recorder precheck, each against the real helper and a real file system. In all three the first QA
  // return is refused with exit 3 before the helper and NOTHING is copied (the valid sibling file is not imported either); the
  // corrected return, which cites a valid regular file, is imported under the number of its own record.
  // (1) one valid scratch file and one scratch file that was never written.
  real_judge_scratch_partial: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: (c) => {
        const s = c.show()
        const log = c.judgeWrite('run.log', 'pytest run ' + c.n + ': 3 passed\n')
        if (c.n === 1) {
          const gone = c.scratchDir() + '/never-written.log'
          return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [log]), findings: [], limitations: ['visual not judged'] }, [log, gone])
        }
        return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [log]), findings: [], limitations: ['visual not judged'] }, [log])
      },
    }),
  }),
  // (2) a destination that already exists in the evidence home (a leftover of an earlier attempt): refused, never overwritten.
  real_judge_scratch_dest_exists: () => ({
    maxDebug: 4,
    over: (w, h) => {
      w.write('.methodology/evidence/' + w.runId + '/04-qa/taken.log', 'OLD CONTENT\n')
      return {
        qa: (c) => {
          const s = c.show()
          if (c.n === 1) {
            const taken = c.judgeWrite('taken.log', 'NEW CONTENT\n')
            const fresh = c.judgeWrite('run.log', 'pytest run: 3 passed\n')
            return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [fresh]), findings: [], limitations: ['visual not judged'] }, [taken, fresh])
          }
          const log = c.judgeWrite('second.log', 'pytest run: 3 passed\n')
          return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [log]), findings: [], limitations: ['visual not judged'] }, [log])
        },
      }
    },
  }),
  // (3) a symbolic link as a source: refused although the file it points at is a regular file in the scratch directory.
  real_judge_scratch_link: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: (c) => {
        const s = c.show()
        const real = c.judgeWrite('real.log', 'pytest run ' + c.n + ': 3 passed\n')
        if (c.n === 1) {
          const link = c.judgeLink('link.log', real)
          return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [real]), findings: [], limitations: ['visual not judged'] }, [real, link])
        }
        return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [real]), findings: [], limitations: ['visual not judged'] }, [real])
      },
    }),
  }),
  // Names that are one file on the default macOS file system: Run.log and probe/run.log must receive two destinations, and the file
  // cited in both spellings of the /tmp alias is copied once. The content of each destination proves that nothing was overwritten.
  real_judge_scratch_names: () => ({
    maxDebug: 4,
    over: (w, h) => ({
      qa: (c) => {
        const s = c.show()
        const upper = c.judgeWrite('Run.log', 'upper-case name\n')
        const lower = c.judgeWrite('probe/run.log', 'lower-case name\n')
        const aliased = lower.replace(/^\/private\/tmp\//, '/tmp/')
        return h.env('qa', 'qa', 'SUCCESS', h.ids(s), { testSummary: '3 passed', scans: h.rscans(undefined, [aliased]), findings: [], limitations: ['visual not judged'] }, [upper, lower, aliased, h.GUIDE])
      },
    }),
  }),
  // Git target whose .gitignore names the Anti-Loop counter: a red QA run rewrites the counter (as the pytest hook does), which
  // must not change the candidate identity, so the BUG_REPORT enters a counted Debug entry and the run reaches SUCCESS.
  real_git_counter_debug: () => ({
    maxDebug: 4,
    git: true,
    files: { '.gitignore': 'tests/.test_counter.json\n' },
    over: (w, h) => ({
      qa: (c, dflt) => {
        const r = c.n === 1 ? qaBugOver(w, h)(c, dflt) : dflt(c)
        w.write('tests/.test_counter.json', '{"attempts": ' + (c.n === 1 ? 1 : 0) + '}\n')
        return r
      },
      debugger: (c, dflt) => {
        w.write('tests/.test_counter.json', '{"attempts": 2}\n')
        return dflt(c)
      },
    }),
  }),
  // Negative control of the one above: the same red run without the ignore rule rewrites tracked-or-untracked candidate content,
  // which the helper refuses, and the run ends BLOCKED with the ledger still at QA.
  real_git_counter_unignored: () => ({
    maxDebug: 4,
    git: true,
    over: (w, h) => ({
      qa: (c, dflt) => {
        const r = c.n === 1 ? qaBugOver(w, h)(c, dflt) : dflt(c)
        w.write('tests/.test_counter.json', '{"attempts": 1}\n')
        return r
      },
    }),
  }),
  // Git target whose Doxygen XML directory docs/api/xml is git-ignored: the map is not candidate content, so Code SUCCESS with the
  // map there is accepted.
  real_git_map_ignored: () => ({
    maxDebug: 4,
    git: true,
    mapRel: 'docs/api/xml',
    files: { '.gitignore': 'docs/api/xml/\n' },
    over: () => ({}),
  }),
  // Negative control: the same map directory without an ignore rule is unlisted candidate content and the helper refuses Code.
  real_git_map_unignored: () => ({ maxDebug: 4, git: true, mapRel: 'docs/api/xml', over: () => ({}) }),
}
// endregion FUNC_REAL_SCENARIOS

// region FUNC_flagsFor [DOMAIN(6): Delegation; CONCEPT(8): SelfContainedPrompt; TECH(4): String]
// ## @purpose Record which self-containment facts a role prompt carries, so tests can assert them without storing the prompts.
// ## @uses String.prototype.includes
// ## @io string, object, string -> object
// ## @complexity 4
function flagsFor(prompt, args, lang) {
  return {
    target: prompt.includes(args.target),
    spec: prompt.includes(args.spec),
    plan: prompt.includes(args.plan),
    framework: prompt.includes(args.framework),
    neutral: prompt.includes(args.framework + '/../..'),
    runId: prompt.includes(args.runId),
    language: prompt.includes(lang),
    readInFull: /read in full/i.test(prompt),
    contract: prompt.includes('OUTPUT CONTRACT'),
    mayEdit: prompt.includes('MAY EDIT'),
    doNotTouch: prompt.includes('DO NOT TOUCH'),
    correction: prompt.includes('RESPONSE CORRECTION'),
    finalizeActor: prompt.includes('separately assigned finalization actor'),
    readOnly: prompt.includes('READ ONLY'),
    countedEntry: prompt.includes('The entry is already counted'),
    history: prompt.includes('DEBUG_HISTORY'),
    evidenceRoot: prompt.includes(args.target + '/.methodology/evidence/' + args.runId),
    reportInRuns: prompt.includes('/.methodology/runs/' + args.runId + '/final-report'),
    invitesDirectories: /a directory entry ends with a slash/i.test(prompt) || /cite the approved specification/i.test(prompt) || /business requirements file/i.test(prompt),
    exactFilePaths: /exact target-relative file path/i.test(prompt),
    indexXml: prompt.includes('index.xml'),
    showCommand: /SHOW COMMAND/.test(prompt),
    digestCommand: /DIGEST COMMAND/.test(prompt),
    scratchGrant: prompt.includes('SCRATCH ROOT (writable'),
    evidenceGrant: prompt.includes('EVIDENCE ROOT (writable'),
    scratchRoot: typeof args.scratch === 'string' ? prompt.includes(args.scratch) : false,
    scratchGrantPath: (prompt.match(/^SCRATCH ROOT \(writable[^)]*\): (\S+)$/m) || [])[1] || null,
    targetWritable: prompt.includes('all writes happen here'),
    generatedAdvice: /git-ignored/.test(prompt) && prompt.includes('doxygen_output/, output/ or .methodology/'),
    partialRecorded: prompt.includes('The root recorded the observed partial changes'),
    partialNotRecorded: prompt.includes('The root did not record the observed partial changes'),
  }
}
// endregion FUNC_flagsFor

// region FUNC_runScenario [DOMAIN(10): Harness; CONCEPT(10): HostEmulation, ScriptedAgents; TECH(6): NodeJS]
// ## @purpose Run the script under one fake-mode scenario with the host restrictions and describe everything it did.
// ## @uses AsyncFunction, makeRecorder, validateSchema, schemaShapeOk, flagsFor
// ## @io string -> object
// ## @complexity 10
async function runScenario(name) {
  const scenario = SCENARIOS[name]()
  const args = scenario.args
  const rawArgs = 'rawArgs' in scenario ? scenario.rawArgs : args
  const lang = args.dialogLang || 'Russian'
  const queues = {}
  for (const k of Object.keys(scenario.queues)) queues[AT + k] = scenario.queues[k].slice()
  const calls = []
  const logs = []
  const phases = []
  const records = []
  const schemaViolations = []
  const recorder = makeRecorder(args, scenario.recorder || {}, records)

  async function agent(prompt, opts) {
    const entry = {
      n: calls.length + 1,
      agentType: opts.agentType,
      model: opts.model,
      label: opts.label,
      phase: opts.phase,
      schemaOk: schemaShapeOk(opts.schema),
      flags: flagsFor(prompt, args, lang),
    }
    calls.push(entry)
    if (opts.agentType === 'general-purpose') {
      const errs = []
      const answer = recorder(prompt, opts.schema)
      if (answer !== null) validateSchema(opts.schema, answer, '$', errs)
      if (errs.length) schemaViolations.push({ call: entry.n, label: opts.label, errors: errs.slice(0, 5) })
      return answer
    }
    const queue = queues[opts.agentType]
    if (!queue || queue.length === 0) throw new Error('unscripted call #' + entry.n + ' ' + opts.agentType + ' ' + opts.label)
    let item = queue.shift()
    if (typeof item === 'function') item = item()
    if (item === null) return null
    const bypass = !!(item && item.__raw)
    const value = bypass ? item.value : item
    if (!bypass) {
      const errs = []
      validateSchema(opts.schema, value, '$', errs)
      if (errs.length) {
        schemaViolations.push({ call: entry.n, label: opts.label, errors: errs.slice(0, 5) })
        return null
      }
    }
    return JSON.parse(JSON.stringify(value))
  }

  const phase = (title) => {
    phases.push(title)
  }
  const log = (message) => {
    logs.push(String(message))
  }
  const result = await hostRun(agent, phase, log, rawArgs)
  const unconsumed = {}
  for (const k of Object.keys(queues)) if (queues[k].length) unconsumed[k] = queues[k].length
  return Object.assign(describe(name, result, calls, logs, phases, records, schemaViolations), { unconsumed })
}
// endregion FUNC_runScenario

// region FUNC_hostRun [DOMAIN(8): Harness; CONCEPT(9): HostRestrictions; TECH(6): NodeJS]
// ## @purpose Wrap the script text as the host does, poison the clock and randomness while it runs and return its terminal result.
// ## @uses AsyncFunction, Reflect.construct
// ## @io function, function, function, any -> object
// ## @complexity 6
async function hostRun(agent, phase, log, rawArgs) {
  const unused = async () => {
    throw new Error('parallel and pipeline are not used by this script')
  }
  const source = readFileSync(WORKFLOW, 'utf8')
  const body = source.replace(/^export const meta = /m, 'const meta = ')
  const fn = new AsyncFunction('agent', 'phase', 'log', 'args', 'parallel', 'pipeline', 'process', 'require', 'module', 'Buffer', body)
  const realNow = Date.now
  const realRandom = Math.random
  const RealDate = globalThis.Date
  try {
    Date.now = () => {
      throw new Error('Date.now is forbidden in workflow scripts')
    }
    Math.random = () => {
      throw new Error('Math.random is forbidden in workflow scripts')
    }
    globalThis.Date = new Proxy(RealDate, {
      construct(target, argList, newTarget) {
        if (argList.length === 0) throw new Error('argument-less new Date() is forbidden in workflow scripts')
        return Reflect.construct(target, argList, newTarget)
      },
    })
    return await fn(agent, phase, log, rawArgs, unused, unused, undefined, undefined, undefined, undefined)
  } finally {
    Date.now = realNow
    Math.random = realRandom
    globalThis.Date = RealDate
  }
}
// endregion FUNC_hostRun

// region FUNC_describe [DOMAIN(7): Harness; CONCEPT(8): ScenarioReport; TECH(4): JavaScript]
// ## @purpose Condense a terminal result and the observed calls into the one JSON object a test judges.
// ## @uses Array.prototype.map
// ## @io string, object, object[], string[], string[], object[], object[] -> object
// ## @complexity 5
function describe(name, result, calls, logs, phases, records, schemaViolations) {
  return {
    scenario: name,
    status: result && result.status,
    debugSpent: result && result.debugSpent,
    maxDebug: result && result.maxDebug,
    runId: result && result.runId,
    reason: result && result.reason,
    ownerDecision: result && result.ownerDecision,
    ledger: result && result.ledger,
    ledgerFailure: result && result.ledgerFailure,
    ledgerNote: result && result.ledgerNote !== undefined ? result.ledgerNote : null,
    transportFailure: result && result.transportFailure !== undefined ? result.transportFailure : null,
    escalation: result && result.escalation,
    blockedPhase: result && result.blockedPhase,
    qaRuns: result && result.qaRuns,
    reviewRuns: result && result.reviewRuns,
    doxygenPath: result && result.doxygenPath,
    historyEvents: result && result.history ? result.history.map((h) => h.event || h.phase + ':' + h.status) : [],
    reportEvidence: result && result.reports ? { qa: result.reports.qa ? result.reports.qa.evidence : null, review: result.reports.review ? result.reports.review.evidence : null } : null,
    calls: calls.map((c) => ({ agentType: c.agentType, model: c.model, label: c.label, phase: c.phase, schemaOk: c.schemaOk, flags: c.flags })),
    logs,
    phases,
    records,
    schemaViolations,
  }
}
// endregion FUNC_describe

// region FUNC_runReal [DOMAIN(10): Harness; CONCEPT(10): RealHelperRoute; TECH(6): child_process]
// ## @purpose Run one real-helper scenario: build the owned target, initialize the run with the shipped helper, run the script with scripted roles and the shell recorder, and describe the terminal result together with the ledger the helper left behind.
// ## @uses sh, realRoles, REAL_SCENARIOS, realRecorder, hostRun, describe, validateSchema
// ## @io string -> object
// ## @complexity 10
async function runReal(name) {
  const fw = process.env.M22_REAL_FRAMEWORK
  const work = process.env.M22_REAL_WORK
  const scratch = NO_SCRATCH ? null : process.env.M22_REAL_SCRATCH
  if (!fw || !work || fw.charAt(0) !== '/' || work.charAt(0) !== '/') throw new Error('real scenarios need absolute M22_REAL_FRAMEWORK and M22_REAL_WORK')
  if (!NO_SCRATCH && (!scratch || scratch.charAt(0) !== '/')) throw new Error('real scenarios need an absolute M22_REAL_SCRATCH (or M22_NO_SCRATCH)')
  const def = REAL_SCENARIOS[name]()
  const runId = 'real-001'
  const target = work + '/target'
  const spec = work + '/spec.md'
  const plan = target + '/plan/DevelopmentPlan.md'
  const stateFile = target + '/.methodology/runs/' + runId + '/state.json'
  const cli = fw + '/skills/feature-dev/scripts/run_state.py'
  mkdirSync(target + '/src', { recursive: true })
  writeFileSync(target + '/src/a.py', 'def a():\n    return 0\n')
  writeFileSync(spec, '# specification\nImplement a() returning one, with a test.\n')
  Object.keys(def.files || {}).forEach((rel) => writeFileSync(target + '/' + rel, def.files[rel]))
  if (def.planFirst) {
    mkdirSync(target + '/plan', { recursive: true })
    writeFileSync(plan, '# Development plan\nSlice S1: a() returns one.\n')
  }
  if (def.git) {
    // A git target that is the top level of its own work tree: the helper then follows the target ignore rules (STATE-102).
    const git = "git -C '" + target + "' -c commit.gpgsign=false -c core.hooksPath=/dev/null -c user.name=m22 -c user.email=" + 'm22' + '@' + 'example' + '.invalid' + " "
    const made = sh("git -C '" + target + "' init -q && " + git + "add -A && " + git + 'commit -q -m initial')
    if (made.code !== 0) throw new Error('git setup failed: ' + made.err.split('\n').slice(-3).join(' | '))
  }
  if (def.dumpPrompts) mkdirSync(work + '/prompts', { recursive: true })
  const init = sh("python3 -B '" + cli + "' init --project '" + target + "' --spec '" + spec + "' --approval real-approval-reference --framework '" + fw + "' --adapter '" + fw + "/adapter.json' --plan '" + plan + "' --run-id " + runId + ' --max-debug ' + def.maxDebug)
  if (init.code !== 0) throw new Error('run_state init failed: ' + init.err.split('\n').slice(-3).join(' | '))
  const world = {
    target,
    spec,
    plan,
    runId,
    stateFile,
    mapRel: def.mapRel || null,
    judgeFiles: [],
    records: [],
    write: (rel, text) => {
      mkdirSync(path.dirname(target + '/' + rel), { recursive: true })
      writeFileSync(target + '/' + rel, text)
    },
  }
  const roles = realRoles(world)
  const over = def.over(world, roles.helpers)
  const counters = {}
  const calls = []
  const logs = []
  const phases = []
  const schemaViolations = []
  const args = { spec, target, plan, approval: 'real-approval-reference', runId, framework: fw, maxDebug: def.maxDebug, recordState: true }
  if (scratch) args.scratch = scratch

  async function agent(prompt, opts) {
    const entry = { n: calls.length + 1, agentType: opts.agentType, model: opts.model, label: opts.label, phase: opts.phase, schemaOk: schemaShapeOk(opts.schema), flags: flagsFor(prompt, args, 'Russian') }
    calls.push(entry)
    if (opts.agentType === 'general-purpose') {
      const answer = realRecorder(prompt, opts.schema, def.recorder || {}, world)
      if (answer !== null) {
        const errs = []
        validateSchema(opts.schema, answer, '$', errs)
        if (errs.length) schemaViolations.push({ call: entry.n, label: opts.label, errors: errs.slice(0, 5) })
      }
      return answer
    }
    let key = opts.agentType.replace(AT, '')
    if (key === 'architect' && opts.label.indexOf('architect:finalize') === 0) key = 'finalize'
    counters[key] = (counters[key] || 0) + 1
    if (def.dumpPrompts) writeFileSync(work + '/prompts/' + ('0' + entry.n).slice(-2) + '-' + opts.label.replace(/[^A-Za-z0-9_.-]/g, '_') + '.txt', prompt)
    const showCommand = (prompt.match(/python3 '?[^\s']+run_state\.py'? show --state '?[^\s']+'?/) || [])[0] || null
    const digestCommand = (prompt.match(/python3 -B -c "import sys; sys\.path\.insert[^"]*"/) || [])[0] || null
    const context = {
      n: counters[key],
      label: opts.label,
      stateFile,
      readState: () => JSON.parse(readFileSync(stateFile, 'utf8')),
      show: () => {
        if (!showCommand) throw new Error('prompt of ' + opts.label + ' quotes no show command')
        const r = sh(showCommand)
        if (r.code !== 0) throw new Error('show refused for ' + opts.label + ': ' + r.err.split('\n').slice(-2).join(' | '))
        return JSON.parse(r.out).state
      },
      showOrState: () => {
        try {
          return context.show()
        } catch (e) {
          if (prompt.indexOf('read input_identity directly from the state file') >= 0) return context.readState()
          throw e
        }
      },
      digest: () => {
        if (!digestCommand) throw new Error('prompt of ' + opts.label + ' quotes no digest command')
        const r = sh(digestCommand)
        if (r.code !== 0) throw new Error('digest command failed for ' + opts.label)
        return r.out.trim()
      },
      // The only place a judge may write is the one its own prompt grants: the SCRATCH ROOT line of this spine or, for a spine
      // from before the scratch root, the writable EVIDENCE ROOT line (which the guard test then judges and refuses).
      scratchDir: () => {
        const granted = prompt.match(/^SCRATCH ROOT \(writable[^)]*\): (\S+)$/m)
        if (granted) return granted[1]
        const legacy = prompt.match(/^EVIDENCE ROOT \(writable[^)]*\): (\S+)$/m)
        if (legacy) return legacy[1] + '/judge-' + key + '-' + counters[key]
        throw new Error('prompt of ' + opts.label + ' grants no writable location to a judge')
      },
      judgeWrite: (rel, text) => {
        const full = context.scratchDir() + '/' + rel
        mkdirSync(path.dirname(full), { recursive: true })
        writeFileSync(full, text)
        world.judgeFiles.push({ role: key, n: counters[key], path: full, text })
        return full
      },
      // A symbolic link in the judge directory that points at a regular file the judge wrote: a source the import must refuse.
      judgeLink: (rel, targetFile) => {
        const full = context.scratchDir() + '/' + rel
        mkdirSync(path.dirname(full), { recursive: true })
        symlinkSync(targetFile, full)
        world.judgeFiles.push({ role: key, n: counters[key], path: full, text: null, link: targetFile })
        return full
      },
    }
    const dflt = roles[key]
    const fn = over[key] || dflt
    const produced = fn(context, dflt)
    if (produced === null || produced === undefined) return null
    if (produced.__raw) return JSON.parse(JSON.stringify(produced.value))
    const value = produced
    const errs = []
    validateSchema(opts.schema, value, '$', errs)
    if (errs.length) {
      schemaViolations.push({ call: entry.n, label: opts.label, errors: errs.slice(0, 5) })
      return null
    }
    return JSON.parse(JSON.stringify(value))
  }

  const result = await hostRun(agent, (title) => phases.push(title), (m) => logs.push(String(m)), args)
  const final = JSON.parse(readFileSync(stateFile, 'utf8'))
  const describeHistory = (h) => {
    if (h.kind === 'role') return 'role:' + h.phase + ':' + h.result.status
    if (h.kind === 'control') return 'control:' + h.phase + ':' + h.control.event
    if (h.kind === 'refused') return 'refused:' + h.phase + ':' + h.reason
    return h.kind
  }
  const out = describe(name, result, calls, logs, phases, world.records.map((r) => ({ n: r.n, phase: r.phase, status: r.status, kind: r.kind, context: r.context, helperExit: r.helperExit, reason: r.reason, stderrTail: r.stderrTail, checksumExit: r.checksumExit, pruneOut: r.pruneOut, steps: r.steps, cmd4: r.cmd4, text: r.text, answer: r.answer })), schemaViolations)
  out.workDir = work
  out.scratch = scratch
  out.judgeFiles = world.judgeFiles
  out.ledgerState = {
    candidateFiles: final.candidate.files.map((f) => f.path),
    status: final.status,
    phase: final.phase,
    debug_spent: final.debug_spent,
    debug_cap: final.debug_cap,
    episodes: final.retry_episodes['response-correction'],
    history: final.history.map(describeHistory),
    plan: final.plan.status,
    scope: final.approved_scope,
  }
  return out
}
// endregion FUNC_runReal

// region FUNC_evaluateMeta [DOMAIN(7): Host; CONCEPT(9): PureLiteralMeta; TECH(5): vm]
// ## @purpose Evaluate the meta literal in a context with no globals; any identifier reference or call makes it throw, which proves the literal is pure.
// ## @uses vm.runInNewContext
// ## @io none -> object
// ## @complexity 5
function evaluateMeta() {
  const source = readFileSync(WORKFLOW, 'utf8')
  const start = source.indexOf('export const meta = ')
  const open = source.indexOf('{', start)
  let depth = 0
  let quote = null
  let end = -1
  for (let i = open; i < source.length; i += 1) {
    const ch = source[i]
    if (quote) {
      if (ch === '\\') i += 1
      else if (ch === quote) quote = null
    } else if (ch === "'" || ch === '"' || ch === '`') quote = ch
    else if (ch === '{') depth += 1
    else if (ch === '}') {
      depth -= 1
      if (depth === 0) {
        end = i
        break
      }
    }
  }
  const literal = source.slice(open, end + 1)
  return vm.runInNewContext('(' + literal + ')', Object.create(null), { timeout: 1000 })
}
// endregion FUNC_evaluateMeta

const arg = process.argv[2]
try {
  if (arg === '--list') {
    console.log(JSON.stringify(Object.keys(SCENARIOS)))
  } else if (arg === '--list-real') {
    console.log(JSON.stringify(Object.keys(REAL_SCENARIOS)))
  } else if (arg === '--meta') {
    console.log(JSON.stringify(evaluateMeta()))
  } else if (arg && SCENARIOS[arg]) {
    console.log(JSON.stringify(await runScenario(arg)))
  } else if (arg && REAL_SCENARIOS[arg]) {
    console.log(JSON.stringify(await runReal(arg)))
  } else {
    console.error('usage: node workflow_harness.mjs <scenario>|--list|--list-real|--meta')
    process.exit(2)
  }
} catch (e) {
  console.log(JSON.stringify({ scenario: arg, status: 'HARNESS_EXCEPTION', error: String(e && e.stack ? e.stack : e) }))
  process.exit(1)
}
