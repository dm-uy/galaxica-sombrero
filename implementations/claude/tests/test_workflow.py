# region MODULE_CONTRACT [DOMAIN(9): WorkflowVerification, FlowOrchestration; CONCEPT(9): RouteCoverage, DebugAllowance, ResponseCorrection, RealHelperAgreement; TECH(7): Python, pytest, NodeJS]
## @modulecontract
## @purpose Prove that the Workflow spine workflows/feature-dev.js routes the neutral flow correctly and that what it accepts is what the shipped run-state helper accepts: the green route, every defect route into a counted Debug entry, exhausted and zero allowance, spec and visual-gate refusals, the single response correction recorded in the ledger, role and recorder transport failures that are not corrections, the eight named scans, the separate Finalize, the recorder step with its checksum, the judge scratch root, namespaced by run, whose cited files the recorder imports into the run evidence home (checked against the real guard, with case-insensitive destinations, the macOS aliases and the three precheck refusals judged on the file system), the delivery sink of the plan command output for the judges, real git targets whose ignore rules define the candidate, and the canonical terminal vocabulary.
## @scope Every fake-mode scenario of tests/workflow_harness.mjs run through a real Node process (fast, emulated ledger) and every real-helper scenario, in which the recorder stub writes the record file and runs the shipped run_state.py over an owned target initialized by run_state.py init with a temporary copy of the package as the framework; static contract of the script (pure literal meta, forbidden host APIs, markup regions, terminal vocabulary, owner and package paths).
## @input The real script and harness in this package and the real neutral checkout two levels above; Node, git and python3 on PATH. Real scenarios write only inside pytest temporary directories and their own scratch directories under /tmp. M22_WORKFLOW (an absolute path) swaps the script under test; M22_NO_SCRATCH runs a spine from before the scratch root so the new tests can be seen to fail for the right reason.
## @output Assertions and a visible IMP:7-10 trace printed before them.
## @links [READS_DATA_FROM(9): workflows/feature-dev.js; READS_DATA_FROM(9): tests/workflow_harness.mjs; READS_DATA_FROM(9): skills/feature-dev/scripts/run_state.py through the harness; USES_API(9): hooks/guard_destructive.py main; READS_DATA_FROM(8): references/package-layout.json; READS_DATA_FROM(8): neutral flow, protocols and checks owners; USES_API(8): subprocess; USES_API(6): git for the real targets]
## @links_to_spec examples/pm-project/specs/m22-claude-package.md BR-4, AC-M22-3
## @invariants
## - The expected statuses, spends and call orders in this module come from the neutral flow (PHASE-901, PHASE-904, STATE-301, STATE-303, STATE-403, DELEG-503, DELEG-504, RETURN-603), not from the script under test.
## - Every scripted answer of a fake scenario is consumed and no canned return violates the schema the script supplied.
## - A scenario that ends before a phase proves it by the absence of that phase calls.
## - Real-helper scenarios judge the ledger the helper left behind, never the script's own claim about it; every discriminating negative names a return the helper refuses and requires the script to have rejected it before recording.
## - The tests never modify the package or the neutral checkout; the framework of the real scenarios is a temporary copy.
## - A write location an assignment grants to a judge is judged by the shipped guard module, never by a reimplementation of its rules; the guard's verdicts are asked in process with the payload and the streams a hook uses.
## - A refusal of the recorder precheck is judged by the file system the real run leaves (what was copied, what stayed untouched) and always with a valid sibling file cited beside the failing one; the verdict alone proves nothing about the copy.
## - Every test prints its important observations (IMP 7-10) before the assertions that depend on them, the static scans included.
## @rationale
## Q: Why a real Node process per scenario?
## A: The script runs only as a host function body with injected globals; a Node process with the same restrictions is the closest check available without a model.
## Q: Why assert exact agent-type and model sequences?
## A: The route and the model tier per phase are the contract; a changed order or an inherited model is a defect that a status alone would hide.
## Q: Why a real-helper mode beside the fast fake ledger?
## A: A permissive fake accepted directory scope entries, evidence outside the target and directory artifact paths that the helper refuses; only the shipped helper is the reference contract.
## Q: Why is a missing Node a failure and not a skip?
## A: A skipped suite would report green while verifying nothing (Green-Test-Trap).
## Q: Why ask the real guard about the judge prompts instead of comparing strings?
## A: The earlier spine named an in-project evidence root as writable for the judges and no test put that grant against the guard that denies it (Mock-Channel-Trap); the prompts are read from a real run, the grants are extracted from the assignment text and the shipped guard decides.
## Q: Why does every precheck refusal scenario cite a valid file beside the failing one?
## A: A refusal that cites only the failing file cannot tell a precheck that copies the valid files of a refused record from one that copies nothing, nor an overwrite of an existing destination from a refusal; three mutants of the recorder snippet survived the single-file scenario of the earlier round.
## Q: Why are the assignments read as text and not only compared with flags?
## A: The delivery of the plan command output is a promise made in prose to three roles (Architect, qa, reviewer); a flag cannot show that the plan is no longer told to send it where a judge may not write, so the prompts of a real run are read and the judge forms are put against the guard.
## Q: Why real git targets?
## A: The candidate identity of a git target follows the target's ignore rules, so a red run that rewrites the ignored Anti-Loop counter, and a Doxygen map under an ignored directory, can only be judged on a real repository with the shipped helper; each positive route has a negative control without the ignore rule.
## @changes
## LAST_CHANGE: [v1.3.0 - Real-helper scenarios for the three precheck refusals (missing next to valid, existing destination, link source) with file-system assertions, case-insensitive and alias-aware import names, run-namespaced judge directories (grants, citations of the flat layout and of another run), alias and case variants of the scratch argument with a sibling positive control, the prompt text of the plan command output sink for the Architect, qa and reviewer, the guard forms of the plan command and of mkdir -p, and visible IMP traces in the diagnostic-path and spine-claims tests.]
## - v1.2.0 - Scratch argument rules, judge grants against the real guard, scratch evidence imported into records (fake and real helper), git targets with an ignored Anti-Loop counter and an ignored Doxygen map plus negative controls, recorder transport failures, correction note depending on the accepted control, review finding code, no doxygenPath extension heuristic, helper refusal note, truthful spine statements.
## - v1.1.0 - Real-helper scenarios (green, three Debug origins, zero cap, discriminating negatives per helper refusal), transport failure and recorded-correction tests, checksum and precheck tests, workflow renamed feature-dev-workflow.
## @modulemap
## FUNC 6[Run one scenario in Node and decode its JSON line] => _run
## FUNC 7[Build a temporary copy of the package with the neutral files above it] => _framework_copy
## FUNC 2[Build the shared framework copy once] => real_framework
## FUNC 8[Run every real scenario once, concurrently, and decode the lines] => real_runs
## FUNC 6[Fetch one decoded real scenario] => _real
## FUNC 4[Ask the real guard for its decision on one command of one agent type] => _guard_verdict
## FUNC 5[Print the scenario trace before assertions] => _show
## FUNC 6[Map a call to its short token] => _token
## FUNC 7[Extract the meta literal text of the script] => _meta_text
## FUNC 8[Table of scenarios equals the harness lists] => test_scenarios_are_declared_once
## FUNC 10[Terminal status, Debug spend and exact agent-type and model order per fake scenario] => test_scenario_route
## FUNC 8[Every role prompt is self-contained and every call has a flat schema] => test_prompts_and_schemas
## FUNC 9[Prompts carry quoted commands, exact file paths and the excluded evidence root] => test_prompt_contract_facts
## FUNC 9[Finalize is a separate architect call after Review] => test_finalize_is_a_separate_architect_call
## FUNC 9[Recorded green route writes six records with the exact helper command and checksum] => test_recorded_green_route
## FUNC 9[Recorded defect route counts the Debug entry before the debugger runs] => test_recorded_debug_route
## FUNC 9[Allowance exhaustion, zero cap and blocked Debug facts] => test_debug_allowance_facts
## FUNC 9[One response correction per phase attempt and none charges Debug] => test_single_response_correction
## FUNC 9[A thrown agent error is a transport failure, never a correction] => test_transport_failure_is_not_a_correction
## FUNC 9[Eight named scans enforced in code] => test_eight_scans_enforced
## FUNC 9[Scope, evidence, directory, field and Doxygen shapes the helper refuses are corrected before recording] => test_helper_shapes_rejected_in_script
## FUNC 8[Invalid invocation ends ERROR before any agent] => test_invalid_invocation_dispatches_nothing
## FUNC 8[Recorder failures end BLOCKED with the stderr, the unknown outcome or the integrity cause] => test_recorder_failures
## FUNC 8[The scratch argument is mandatory and judged before any agent] => test_scratch_argument_rules
## FUNC 10[Judge assignments grant the scratch directory only, writers keep the evidence root] => test_judge_assignments_grant_scratch_only
## FUNC 10[Scratch citations are imported and the records carry the in-target paths] => test_judge_scratch_citations_are_imported
## FUNC 9[Scratch paths are citable by judges only and only in the safe form] => test_scratch_citation_rules
## FUNC 10[A thrown recorder ends BLOCKED on progress records and correction episodes] => test_recorder_transport_failures
## FUNC 9[The correction note claims recorded changes only for an accepted control] => test_correction_note_depends_on_the_accepted_control
## FUNC 9[A Review finding needs a code] => test_review_finding_requires_a_code
## FUNC 8[Spec, visual gate, scope and UI refusals] => test_pre_code_and_scope_refusals
## FUNC 8[All runtime statuses are canonical and every log line has the LDD shape] => test_vocabulary_and_trace_shape
## FUNC 9[Real helper: terminal status, ledger status and Debug spend per route] => test_real_routes
## FUNC 9[Real helper: green route records six accepted returns] => test_real_green_route
## FUNC 9[Real helper: silent builds with empty output] => test_real_silent_builds
## FUNC 9[Real helper: Doxygen arms, visual gate arm and accepted spec halt] => test_real_arms_of_the_records
## FUNC 9[Real helper: bound plan and BLOCKED Debug] => test_real_bound_plan_and_blocked_debug
## FUNC 9[Real helper: Debug from QA, Code and Review] => test_real_debug_origins
## FUNC 9[Real helper: scope entries the helper refuses are corrected first] => test_real_scope_forms
## FUNC 9[Real helper: evidence outside the target, extra Architect file, directory artifact path] => test_real_containment_and_files
## FUNC 9[Real helper: a cited file that does not exist is corrected before the helper] => test_real_cited_files_exist
## FUNC 9[Real helper: deletion-only Debug fix and no surviving artifact] => test_real_debug_deletion
## FUNC 9[Real helper: refusal reason, transport failure and integrity cause] => test_real_refusals_and_causes
## FUNC 9[Real helper: second unusable return lands in the ledger] => test_real_corrections_in_ledger
## FUNC 9[Real helper: halts and their ledger notes] => test_real_halts
## FUNC 10[Every judge grant is silent and every in-project path denied under the real guard] => test_judge_grants_agree_with_the_guard
## FUNC 10[Real helper: scratch evidence accepted with the imported in-target paths] => test_real_judge_scratch_import
## FUNC 10[Real helper: a missing scratch file is stopped before the helper and nothing is copied] => test_real_judge_scratch_missing
## FUNC 10[Real helper: missing next to valid, existing destination and link source are refused and nothing is copied] => test_real_precheck_refusals
## FUNC 10[Case-insensitive destinations and alias spellings of one file in the import plan] => test_import_names_are_case_insensitive_and_alias_aware
## FUNC 7[Real file system: Run.log and run.log both survive the import] => test_real_import_keeps_case_variant_names_apart
## FUNC 9[Judge directories carry the run id and citations stay in the run namespace] => test_judge_directories_are_namespaced_by_run
## FUNC 10[The plan commands have a deliverable output sink for writers and judges] => test_plan_command_output_has_a_deliverable_sink
## FUNC 10[Real helper: git targets with an ignored counter and an ignored map, with negative controls] => test_real_git_targets
## FUNC 6[The real harness writes the diagnostic to the STEP 2a path and refuses a path that differs] => test_real_harness_checks_the_diagnostic_path
## FUNC 9[No forbidden host API in the script] => test_forbidden_apis_absent
## FUNC 9[Meta is a pure literal] => test_meta_is_a_pure_literal
## FUNC 7[Meta evaluates in an empty context and lists the seven phases] => test_meta_evaluates_in_an_empty_context
## FUNC 8[Every function carries a region pair and the contract markup is present] => test_markup_regions
## FUNC 8[Terminal literals in the script are canonical and the owner decision is honest] => test_static_terminal_literals
## FUNC 8[Referenced neutral owners and package paths exist] => test_referenced_paths_exist
## FUNC 8[Checksum, transport, path and scratch statements of the spine are accurate] => test_spine_claims_are_accurate
## @usecases
## - [test_scenario_route]: QA -> run each route in Node -> a wrong terminal, spend or call order refused
## - [test_real_scope_forms]: QA -> return a scope entry the helper refuses -> the script corrects it before the ledger sees it
## - [test_real_corrections_in_ledger]: QA -> two unusable returns in a row -> the ledger ends BLOCKED or ESCALATED_FINALIZE
## - [test_forbidden_apis_absent]: QA -> scan the script text -> a clock, randomness or Node API refused
## - [test_judge_grants_agree_with_the_guard]: QA -> read the judge prompts of a real run and ask the shipped guard -> a granted location the guard denies, or an in-project path it lets a judge write, refused
## - [test_real_judge_scratch_import]: QA -> a judge cites scratch files in every evidence field -> the real helper accepts the records with the imported paths
## - [test_real_precheck_refusals]: QA -> a record cites a valid scratch file beside a missing file, an existing destination or a link -> the precheck stops the whole record before the helper and the file system shows nothing copied and nothing overwritten
## - [test_plan_command_output_has_a_deliverable_sink]: QA -> read the Architect and judge prompts of a real run -> a plan told to send command output to the evidence root, or a judge not told to mkdir -p and redirect there, refused
## - [test_real_git_targets]: QA -> a red run rewrites the ignored counter, a map sits in an ignored directory -> the route reaches SUCCESS; without the ignore rule the helper refuses
## @GREP_SUMMARY workflow spine, scenarios, real helper, Debug allowance, response correction, transport failure, eight scans, Finalize, recorder checksum, terminal vocabulary, pure meta, precheck refusals, run namespace, macOS alias, case-insensitive import, plan command output sink
## @STRUCTURE ▶ node harness ⟲ fake scenarios → ◇ status/spend/order → ○ prompts+schemas → ⚡ real run_state.py ⟲ real scenarios → ◇ ledger status/history → ○ static contract → ⎋ assertions
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import concurrent.futures
import functools
import io
import json
import logging
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

import guard_destructive
import pytest
import run_state

LOGGER = logging.getLogger(__name__)
PACKAGE = pathlib.Path(__file__).resolve().parents[1]
NEUTRAL = PACKAGE.parents[1]
WORKFLOW = pathlib.Path(os.environ["M22_WORKFLOW"]) if os.environ.get("M22_WORKFLOW", "").startswith("/") else PACKAGE / "workflows" / "feature-dev.js"
HARNESS = PACKAGE / "tests" / "workflow_harness.mjs"
TERMINAL = {"SUCCESS", "SPEC_BLOCKED", "VISUAL_GATE_FAIL", "ESCALATED", "BLOCKED", "ERROR", "ESCALATED_FINALIZE"}
PHASE_TITLES = ["Bootstrap", "Architect", "Code", "QA", "Review", "Debug", "Finalize"]
TOKENS = {
    "S": ("methodology-claude:searcher", "haiku", "searcher:bootstrap"),
    "A": ("methodology-claude:architect", "opus", "architect:design"),
    "C": ("methodology-claude:coder", "sonnet", "coder:implement"),
    "Q": ("methodology-claude:qa", "sonnet", "qa#"),
    "R": ("methodology-claude:reviewer", "opus", "reviewer#"),
    "D": ("methodology-claude:debugger", "sonnet", "debugger#"),
    "F": ("methodology-claude:architect", "opus", "architect:finalize"),
    "X": ("general-purpose", "haiku", "recorder:"),
}
ROLE_FLAGS = ("target", "spec", "plan", "framework", "neutral", "runId", "language", "readInFull", "contract")
LDD_LINE = re.compile(r"^\[IMP:(10|[1-9])\]\[[A-Za-z_]+\]\[[A-Z_]+\] .+")
TARGET = "/work/target"
FORBIDDEN = {
    "Date.now": r"\bDate\.now\b",
    "Math.random": r"\bMath\.random\b",
    "new Date": r"\bnew\s+Date\b",
    "require(": r"\brequire\s*\(",
    "import fs": r"\bimport\s+fs\b",
    "dynamic import": r"\bimport\s*\(",
    "node: specifier": "[\\x27\\x22]node:",
    "process API": r"\bprocess\.[A-Za-z]",
    "Buffer": r"\bBuffer\b",
    "fetch": r"\bfetch\s*\(",
    "timer": r"\bset(?:Timeout|Interval|Immediate)\b",
}

# (scenario, terminal status, Debug spend, token order); S searcher, A architect design, C coder, Q qa, R reviewer,
# D debugger, F architect finalize, X recorder. A corrected call repeats its token.
SCENARIOS = [
    ("green", "SUCCESS", 0, "S A C Q R F"),
    ("green_recorded", "SUCCESS", 0, "S X A X C X Q X R X F X"),
    ("visual_gate_pass", "SUCCESS", 0, "S A C Q R F"),
    ("code_bug_debug_fixed", "SUCCESS", 1, "S A C D Q R F"),
    ("qa_bug_twice_cap1", "ESCALATED", 1, "S A C Q D Q"),
    ("maxdebug_zero_qa_defect", "ESCALATED", 0, "S A C Q"),
    ("review_bug_debug", "SUCCESS", 1, "S A C Q R D Q R F"),
    ("qa_bug_debug_fixed_recorded", "SUCCESS", 1, "S X A X C X Q X D X Q X R X F X"),
    ("debug_blocked", "BLOCKED", 1, "S A C Q D"),
    ("debug_origin_mismatch_corrected", "SUCCESS", 1, "S A C Q D D Q R F"),
    ("spec_blocked", "SPEC_BLOCKED", 0, "S A"),
    ("architect_blocked_spec", "SPEC_BLOCKED", 0, "S A"),
    ("architect_blocked", "BLOCKED", 0, "S A"),
    ("bootstrap_blocked", "BLOCKED", 0, "S"),
    ("visual_gate_fail", "VISUAL_GATE_FAIL", 0, "S A"),
    ("visual_gate_zero_nodes", "VISUAL_GATE_FAIL", 0, "S A"),
    ("visual_gate_waived_active", "VISUAL_GATE_FAIL", 0, "S A"),
    ("visual_gate_empty_output", "SUCCESS", 0, "S A C Q R F"),
    ("doxygen_empty_output", "SUCCESS", 0, "S A C Q R F"),
    ("null_corrected", "SUCCESS", 0, "S A C Q Q R F"),
    ("agent_throws", "BLOCKED", 0, "S X A X C"),
    ("agent_throws_readonly", "BLOCKED", 0, "S A C Q"),
    ("null_twice", "BLOCKED", 0, "S A C Q Q"),
    ("qa_seven_scans", "BLOCKED", 0, "S A C Q Q"),
    ("qa_duplicate_scan", "BLOCKED", 0, "S A C Q Q"),
    ("qa_seven_then_eight", "SUCCESS", 0, "S A C Q Q R F"),
    ("qa_success_failed_scan", "BLOCKED", 0, "S A C Q Q"),
    ("plan_mismatch_corrected", "SUCCESS", 0, "S A A C Q R F"),
    ("scope_directory_entry", "SUCCESS", 0, "S A A C Q R F"),
    ("scope_dot_slash_entry", "SUCCESS", 0, "S A A C Q R F"),
    ("scope_dotdot_entry", "SUCCESS", 0, "S A A C Q R F"),
    ("scope_absolute_entry", "SUCCESS", 0, "S A A C Q R F"),
    ("evidence_spec_outside_target", "SUCCESS", 0, "S S A C Q R F"),
    ("architect_requirements_field", "SUCCESS", 0, "S A A C Q R F"),
    ("finalize_extensionless_doxygen", "SUCCESS", 0, "S A C Q R F"),
    ("doxygen_pass_with_prohibition_fields", "SUCCESS", 0, "S A C C Q R F"),
    ("code_scope_violation", "BLOCKED", 0, "S X A X C"),
    ("ui_discrepancy", "BLOCKED", 0, "S A C"),
    ("finalize_escalated", "ESCALATED_FINALIZE", 0, "S A C Q R F"),
    ("finalize_null_twice", "ESCALATED_FINALIZE", 0, "S A C Q R F F"),
    ("finalize_candidate_mismatch", "ESCALATED_FINALIZE", 0, "S A C Q R F F"),
    ("judge_scratch_recorded", "SUCCESS", 0, "S X A X C X Q X R X F X"),
    ("judge_scratch_unrecorded", "SUCCESS", 0, "S A C Q R F"),
    ("judge_evidence_outside_corrected", "SUCCESS", 0, "S A C Q Q R F"),
    ("judge_scratch_unsafe_corrected", "SUCCESS", 0, "S A C Q Q R F"),
    ("judge_scratch_dotdot_corrected", "SUCCESS", 0, "S A C Q R R F"),
    ("judge_scratch_old_layout_corrected", "SUCCESS", 0, "S A C Q Q R F"),
    ("judge_scratch_other_run_corrected", "SUCCESS", 0, "S A C Q Q R F"),
    ("judge_scratch_second_run", "SUCCESS", 0, "S X A X C X Q X R X F X"),
    ("judge_scratch_case_collision", "SUCCESS", 0, "S X A X C X Q X R X F X"),
    ("judge_scratch_alias_spellings", "SUCCESS", 0, "S X A X C X Q X R X F X"),
    ("judge_alias_siblings_accepted", "SUCCESS", 0, "S A C Q R F"),
    ("judge_scratch_directory_corrected", "SUCCESS", 0, "S A C Q Q R F"),
    ("writer_cites_scratch_corrected", "SUCCESS", 0, "S A C C Q R F"),
    ("review_finding_without_code", "SUCCESS", 0, "S A C Q R R F"),
    ("code_null_corrected_recorded", "SUCCESS", 0, "S X A X C X C X Q X R X F X"),
    ("code_null_control_refused", "SUCCESS", 0, "S X A X C X C X Q X R X F X"),
    ("args_json_string", "SUCCESS", 0, "S A C Q R F"),
    ("args_missing", "ERROR", 0, ""),
    ("args_unknown_key", "ERROR", 0, ""),
    ("args_relative_path", "ERROR", 0, ""),
    ("args_whitespace_path", "ERROR", 0, ""),
    ("args_metachar_path", "ERROR", 0, ""),
    ("args_quote_path", "ERROR", 0, ""),
    ("args_scratch_missing", "ERROR", 0, ""),
    ("args_scratch_relative", "ERROR", 0, ""),
    ("args_scratch_in_target", "ERROR", 0, ""),
    ("args_scratch_around_target", "ERROR", 0, ""),
    ("args_scratch_unsafe_root", "ERROR", 0, ""),
    ("args_scratch_prefix_itself", "ERROR", 0, ""),
    ("args_scratch_alias_in_target", "ERROR", 0, ""),
    ("args_scratch_alias_around_target", "ERROR", 0, ""),
    ("args_scratch_alias_var_folders", "ERROR", 0, ""),
    ("args_scratch_case_variant", "ERROR", 0, ""),
    ("args_scratch_whitespace", "ERROR", 0, ""),
    ("invalid_maxdebug_negative", "ERROR", 0, ""),
    ("invalid_maxdebug_fraction", "ERROR", 0, ""),
    ("invalid_maxdebug_boolean", "ERROR", 0, ""),
    ("invalid_maxdebug_string", "ERROR", 0, ""),
    ("maxdebug_above_supported", "BLOCKED", 0, ""),
    ("recorder_nonzero", "BLOCKED", 0, "S X A X C X"),
    ("recorder_null", "BLOCKED", 0, "S X A X"),
    ("recorder_throws", "BLOCKED", 0, "S X A X"),
    ("recorder_throws_on_correction", "BLOCKED", 0, "S X A X C X Q X"),
    ("recorder_null_on_correction", "BLOCKED", 0, "S X A X C X Q X"),
    ("recorder_throws_on_finalize_correction", "BLOCKED", 0, "S X A X C X Q X R X F X"),
    ("recorder_checksum_lie", "BLOCKED", 0, "S X A X"),
    ("recorder_precheck_exit", "SUCCESS", 1, "S X A X C X Q X D X X D X Q X R X F X"),
    ("ledger_spend_mismatch", "BLOCKED", 0, "S X A X C X Q X"),
    ("null_twice_recorded", "BLOCKED", 0, "S X A X C X Q X Q X"),
    ("finalize_null_twice_recorded", "ESCALATED_FINALIZE", 0, "S X A X C X Q X R X F X F X"),
    ("spec_blocked_recorded", "SPEC_BLOCKED", 0, "S X A X"),
]
NAMES = [row[0] for row in SCENARIOS]

# (real scenario, terminal status, ledger status, Debug spend in both); every real scenario runs the shipped helper.
REAL = [
    ("real_green", "SUCCESS", "SUCCESS", 0),
    ("real_silent_builds", "SUCCESS", "SUCCESS", 0),
    ("real_debug_qa", "SUCCESS", "SUCCESS", 1),
    ("real_debug_code", "SUCCESS", "SUCCESS", 1),
    ("real_debug_review", "SUCCESS", "SUCCESS", 1),
    ("real_cap_zero", "ESCALATED", "ESCALATED", 0),
    ("real_debug_twice", "SUCCESS", "SUCCESS", 2),
    ("real_bound_plan", "SUCCESS", "SUCCESS", 0),
    ("real_debug_blocked", "BLOCKED", "BLOCKED", 1),
    ("real_visual_gate_pass", "SUCCESS", "SUCCESS", 0),
    ("real_architect_blocked_spec", "SPEC_BLOCKED", "BLOCKED", 0),
    ("real_doxygen_prohibited", "SUCCESS", "SUCCESS", 0),
    ("real_doxygen_quote_no_denial", "SUCCESS", "SUCCESS", 0),
    ("real_doxygen_quote_paraphrase", "SUCCESS", "SUCCESS", 0),
    ("real_doxygen_pass_extra_field", "SUCCESS", "SUCCESS", 0),
    ("real_scope_directory", "SUCCESS", "SUCCESS", 0),
    ("real_scope_dot_slash", "SUCCESS", "SUCCESS", 0),
    ("real_scope_dotdot", "SUCCESS", "SUCCESS", 0),
    ("real_scope_absolute", "SUCCESS", "SUCCESS", 0),
    ("real_evidence_spec", "SUCCESS", "SUCCESS", 0),
    ("real_architect_extra_file", "SUCCESS", "SUCCESS", 0),
    ("real_finalize_directory", "SUCCESS", "SUCCESS", 0),
    ("real_debug_delete_only", "SUCCESS", "SUCCESS", 1),
    ("real_debug_no_survivor", "SUCCESS", "SUCCESS", 1),
    ("real_refusal_reason", "BLOCKED", "RUNNING", 0),
    ("real_nonexistent_evidence", "SUCCESS", "SUCCESS", 0),
    ("real_nonexistent_evidence_twice", "BLOCKED", "BLOCKED", 0),
    ("real_transport_throw", "BLOCKED", "RUNNING", 0),
    ("real_qa_null_twice", "BLOCKED", "BLOCKED", 0),
    ("real_finalize_null_twice", "ESCALATED_FINALIZE", "ESCALATED_FINALIZE", 0),
    ("real_code_null_then_ok", "SUCCESS", "SUCCESS", 0),
    ("real_spec_blocked", "SPEC_BLOCKED", "RUNNING", 0),
    ("real_visual_gate_fail", "VISUAL_GATE_FAIL", "RUNNING", 0),
    ("real_scope_deviation", "BLOCKED", "RUNNING", 0),
    ("real_checksum_corrupt", "BLOCKED", "RUNNING", 0),
    ("real_judge_scratch", "SUCCESS", "SUCCESS", 1),
    ("real_judge_scratch_missing", "SUCCESS", "SUCCESS", 0),
    ("real_judge_scratch_partial", "SUCCESS", "SUCCESS", 0),
    ("real_judge_scratch_dest_exists", "SUCCESS", "SUCCESS", 0),
    ("real_judge_scratch_link", "SUCCESS", "SUCCESS", 0),
    ("real_judge_scratch_names", "SUCCESS", "SUCCESS", 0),
    ("real_git_counter_debug", "SUCCESS", "SUCCESS", 1),
    ("real_git_counter_unignored", "BLOCKED", "RUNNING", 0),
    ("real_git_map_ignored", "SUCCESS", "SUCCESS", 0),
    ("real_git_map_unignored", "BLOCKED", "RUNNING", 0),
]
REAL_NAMES = [row[0] for row in REAL]
SCOPE_FORMS = ["real_scope_directory", "real_scope_dot_slash", "real_scope_dotdot", "real_scope_absolute"]


# region FUNC__run [DOMAIN(7): Harness; CONCEPT(8): RealNodeProcess; TECH(6): subprocess]
## @purpose Run one fake-mode harness scenario in a real Node process and decode its single JSON line; a missing Node or a harness exception fails loudly.
## @uses subprocess.run, json.loads, shutil.which
## @io str -> dict
## @complexity 4
@functools.lru_cache(maxsize=None)
def _run(name):
    node = shutil.which("node")
    assert node, "node is required: skipping would report green while verifying nothing"
    proc = subprocess.run([node, str(HARNESS), name], capture_output=True, text=True, timeout=60)
    LOGGER.info("[IMP:7][_run][PROCESS] scenario=%s exit=%d", name, proc.returncode)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    out = json.loads(proc.stdout.strip().splitlines()[-1])
    assert out.get("status") != "HARNESS_EXCEPTION", out.get("error")
    return out
# endregion FUNC__run


# region FUNC__framework_copy [DOMAIN(8): InPlaceBinding; CONCEPT(9): OwnedFramework; TECH(6): shutil, run_state.inventory]
## @purpose Build the framework the helper binds in the real scenarios: a temporary copy of the package placed at implementations/claude with the adapter-declared neutral files and SPEC_VERSION above it, with generated and undeclared files dropped, so the real package is never read as live state.
## @uses shutil.copytree, shutil.copyfile, run_state.inventory, json.loads
## @io Path -> Path
## @complexity 5
# BUG_FIX_CONTEXT: the spine and its tests were never run against run_state.py, whose refusals (directory scope entries, evidence
# outside the target, directory artifact paths) a permissive fake had hidden; the real scenarios bind a temporary copy of the package.
def _framework_copy(dest):
    package = dest / "source" / "implementations" / "claude"
    shutil.copytree(PACKAGE, package, ignore=shutil.ignore_patterns("doxygen_output", "__pycache__", ".pytest_cache"))
    declared = {row["path"] for row in json.loads((package / "references/package-layout.json").read_text(encoding="utf-8"))["files"]}
    for row in run_state.inventory(package, run_state.PACKAGE_GENERATED)["files"]:
        if row["path"] not in declared:
            (package / row["path"]).unlink()
            LOGGER.info("[IMP:7][_framework_copy][UNDECLARED_DROPPED] path=%s", row["path"])
    adapter = json.loads((package / "adapter.json").read_text(encoding="utf-8"))
    for relative in adapter["files"]:
        destination = dest / "source" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(NEUTRAL / relative, destination)
    shutil.copyfile(NEUTRAL / "SPEC_VERSION", dest / "source" / "SPEC_VERSION")
    LOGGER.info("[IMP:9][_framework_copy][RESULT] declared=%d neutral=%d", len(declared), len(adapter["files"]))
    return package.resolve()
# endregion FUNC__framework_copy


# region FUNC_real_framework [DOMAIN(8): InPlaceBinding; CONCEPT(8): SharedFrameworkCopy; TECH(5): pytest fixture]
## @purpose Build the temporary framework copy once per module so that the concurrent real scenarios and the harness self-check bind the same copy.
## @uses _framework_copy
## @io tmp_path_factory -> Path
## @complexity 2
@pytest.fixture(scope="module")
def real_framework(tmp_path_factory):
    return _framework_copy(tmp_path_factory.mktemp("framework"))
# endregion FUNC_real_framework


# region FUNC_real_runs [DOMAIN(9): Harness; CONCEPT(10): ConcurrentRealScenarios; TECH(6): concurrent.futures, subprocess]
## @purpose Run every real-helper scenario once, concurrently, in its own owned work directory and its own scratch directory (outside the work directory, under /tmp, one of the default safe prefixes of the guard, whatever basetemp pytest was given) against one shared temporary framework copy, hand the decoded lines to the tests and remove the scratch directories afterwards; an unreadable line is kept as its error text so that only the tests that need it fail.
## @uses _framework_copy, subprocess.run, concurrent.futures.ThreadPoolExecutor, json.loads, tempfile.mkdtemp
## @io tmp_path_factory -> dict name -> dict or str
## @complexity 7
@pytest.fixture(scope="module")
def real_runs(tmp_path_factory, real_framework):
    node = shutil.which("node")
    assert node, "node is required: skipping would report green while verifying nothing"
    framework = real_framework
    works = {name: tmp_path_factory.mktemp(name).resolve() for name in REAL_NAMES}
    scratches = {name: pathlib.Path(tempfile.mkdtemp(prefix="m22-scratch-", dir="/tmp")).resolve() for name in REAL_NAMES}

    def one(name):
        env = dict(os.environ, M22_REAL_FRAMEWORK=str(framework), M22_REAL_WORK=str(works[name]), M22_REAL_SCRATCH=str(scratches[name]), PYTHONDONTWRITEBYTECODE="1")
        proc = subprocess.run([node, str(HARNESS), name], capture_output=True, text=True, timeout=240, env=env)
        lines = proc.stdout.strip().splitlines()
        if proc.returncode != 0 or not lines:
            return proc.stdout[-3000:] + proc.stderr[-3000:]
        return json.loads(lines[-1])

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            results = dict(zip(REAL_NAMES, pool.map(one, REAL_NAMES)))
        LOGGER.info("[IMP:9][real_runs][RESULT] scenarios=%d failed=%d", len(results), sum(1 for v in results.values() if isinstance(v, str)))
        yield results
    finally:
        for path in scratches.values():
            shutil.rmtree(path, ignore_errors=True)
# endregion FUNC_real_runs


# region FUNC__real [DOMAIN(7): Harness; CONCEPT(8): DecodedRealScenario; TECH(4): pytest]
## @purpose Fetch one decoded real scenario and fail with the harness error text when it did not run.
## @uses none
## @io dict, str -> dict
## @complexity 2
def _real(runs, name):
    out = runs[name]
    assert isinstance(out, dict), out
    assert out.get("status") != "HARNESS_EXCEPTION", out.get("error")
    return out
# endregion FUNC__real


# region FUNC__show [DOMAIN(5): Tests; CONCEPT(6): VisibleTrace; TECH(4): print]
## @purpose Expose the scenario trace (status, call order, important script log lines, and for real scenarios the ledger left by the helper) before the assertions that depend on it.
## @uses builtins.print
## @io dict -> None
## @complexity 3
def _show(out):
    print("scenario=%s status=%s debugSpent=%s" % (out["scenario"], out["status"], out["debugSpent"]))
    for call in out["calls"]:
        print("  call %-3d %-30s %-7s %s" % (out["calls"].index(call) + 1, call["agentType"], call["model"], call["label"]))
    for line in out["logs"]:
        if re.match(r"\[IMP:(7|8|9|10)\]", line):
            print("  " + line)
    if "ledgerState" in out:
        led = out["ledgerState"]
        print("  ledger status=%s phase=%s spent=%s episodes=%s" % (led["status"], led["phase"], led["debug_spent"], led["episodes"]))
        for item in led["history"]:
            print("    history " + item)
    if out.get("ledgerNote"):
        print("  ledgerNote: " + out["ledgerNote"])
# endregion FUNC__show


# region FUNC__token [DOMAIN(5): Tests; CONCEPT(6): CallIdentity; TECH(4): str]
## @purpose Map one recorded call to the short token of the table, or None when its type, model or label does not match any.
## @uses str.startswith
## @io dict -> str or None
## @complexity 3
def _token(call):
    label = call["label"]
    for token, (agent_type, model, prefix) in TOKENS.items():
        if call["agentType"] == agent_type and call["model"] == model and label.startswith(prefix):
            if token == "A" and label.startswith("architect:finalize"):
                continue
            return token
    return None
# endregion FUNC__token


# region FUNC__meta_text [DOMAIN(6): Static; CONCEPT(7): LiteralExtraction; TECH(5): str]
## @purpose Extract the exact text of the meta object literal by brace matching that respects single-quoted strings.
## @uses str.index
## @io none -> str
## @complexity 5
def _meta_text():
    text = WORKFLOW.read_text(encoding="utf-8")
    start = text.index("export const meta = ")
    open_at = text.index("{", start)
    depth, quote, i = 0, None, open_at
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 1
            elif ch == quote:
                quote = None
        elif ch in "'\"`":
            quote = ch
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[open_at:i + 1]
        i += 1
    raise AssertionError("meta literal is not closed")
# endregion FUNC__meta_text


# region FUNC_test_scenarios_are_declared_once [DOMAIN(8): Coverage; CONCEPT(8): NoDriftBetweenTableAndHarness; TECH(5): subprocess]
## @purpose Refuse a harness scenario the tables do not judge and a table row the harness does not define, for both modes.
## @uses subprocess.run, json.loads
## @io caplog -> None
## @complexity 4
def test_scenarios_are_declared_once(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    node = shutil.which("node")
    assert node, "node is required"
    listed = json.loads(subprocess.run([node, str(HARNESS), "--list"], capture_output=True, text=True, timeout=60).stdout)
    listed_real = json.loads(subprocess.run([node, str(HARNESS), "--list-real"], capture_output=True, text=True, timeout=60).stdout)
    LOGGER.info("[IMP:9][test_scenarios_are_declared_once][COMPARE] fake=%d/%d real=%d/%d", len(listed), len(NAMES), len(listed_real), len(REAL_NAMES))
    print("[IMP:9] harness scenarios=%d table rows=%d real=%d real rows=%d" % (len(listed), len(NAMES), len(listed_real), len(REAL_NAMES)))
    assert len(set(NAMES)) == len(NAMES) and sorted(listed) == sorted(NAMES)
    assert len(set(REAL_NAMES)) == len(REAL_NAMES) and sorted(listed_real) == sorted(REAL_NAMES)
# endregion FUNC_test_scenarios_are_declared_once


# region FUNC_test_scenario_route [DOMAIN(10): Routing; CONCEPT(10): TerminalSpendOrder; TECH(6): pytest.mark.parametrize]
## @purpose Judge each fake scenario by its terminal status, cumulative Debug spend and the exact ordered agent type and model of every call, with every scripted answer consumed and no schema violation.
## @uses _run, _show, _token
## @io scenario row -> None
## @complexity 6
@pytest.mark.parametrize("name,status,spent,order", SCENARIOS, ids=NAMES)
def test_scenario_route(name, status, spent, order, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run(name)
    tokens = [_token(call) for call in out["calls"]]
    LOGGER.info("[IMP:9][test_scenario_route][OBSERVED] %s status=%s spent=%s order=%s", name, out["status"], out["debugSpent"], " ".join(str(t) for t in tokens))
    _show(out)
    assert out["status"] == status
    assert out["debugSpent"] == spent
    assert " ".join(str(t) for t in tokens) == order
    assert out["schemaViolations"] == [] and out["unconsumed"] == {}
    assert out["status"] in TERMINAL and out["ownerDecision"]
# endregion FUNC_test_scenario_route


# region FUNC_test_prompts_and_schemas [DOMAIN(8): Delegation; CONCEPT(9): SelfContainedAssignment; TECH(5): pytest]
## @purpose Require that every role prompt carries the roots, the neutral root, the run, the language, the read-in-full duty and the output contract, that judges are read-only and that every call hands over a flat object schema.
## @uses _run, _show
## @io scenario name -> None
## @complexity 6
@pytest.mark.parametrize("name", NAMES)
def test_prompts_and_schemas(name, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run(name)
    _show(out)
    for call in out["calls"]:
        flags = call["flags"]
        LOGGER.info("[IMP:8][test_prompts_and_schemas][CALL] %s %s", name, call["label"])
        assert call["schemaOk"] is True
        if call["agentType"] == "general-purpose":
            assert flags["target"] and flags["framework"] and flags["runId"]
            continue
        missing = [f for f in ROLE_FLAGS if not flags[f]]
        assert missing == [], (call["label"], missing)
        role = call["agentType"].split(":")[1]
        if role in ("coder", "debugger", "qa", "reviewer") or call["label"].startswith("architect:finalize"):
            assert flags["mayEdit"] and flags["doNotTouch"], call["label"]
        assert flags["readOnly"] == (role in ("qa", "reviewer")), call["label"]
        assert flags["correction"] == call["label"].endswith(":correction"), call["label"]
        assert flags["finalizeActor"] == call["label"].startswith("architect:finalize"), call["label"]
        if role == "debugger":
            assert flags["countedEntry"] and flags["history"], call["label"]
# endregion FUNC_test_prompts_and_schemas


# region FUNC_test_prompt_contract_facts [DOMAIN(8): Delegation; CONCEPT(10): HelperAlignedInstructions; TECH(5): pytest]
## @purpose Require, in a recorded run, that every role prompt invites no directory scope entry, no citation of the approved specification and no extra Architect file, demands exact target-relative file paths and the index.xml file for the map, keeps run logs and the Finalize report under the excluded evidence root (never under the root-owned runs folder) and quotes runnable show and digest commands.
## @uses _run, _show
## @io none -> None
## @complexity 6
def test_prompt_contract_facts(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run("green_recorded")
    _show(out)
    roles = [c for c in out["calls"] if c["agentType"] != "general-purpose"]
    LOGGER.info("[IMP:9][test_prompt_contract_facts][ROLES] count=%d", len(roles))
    assert len(roles) == 6
    for call in roles:
        flags = call["flags"]
        assert flags["invitesDirectories"] is False, call["label"]
        assert flags["reportInRuns"] is False, call["label"]
        assert flags["generatedAdvice"] is (call["label"] in ("architect:design", "coder:implement")), call["label"]
        if call["label"] != "searcher:bootstrap":
            assert flags["showCommand"] and flags["digestCommand"] == (call["label"] in ("architect:design", "coder:implement")), call["label"]
        if call["label"] in ("architect:design", "coder:implement", "architect:finalize"):
            assert flags["evidenceRoot"] is True, call["label"]
        if call["label"] in ("architect:design", "coder:implement"):
            assert flags["exactFilePaths"] is True, call["label"]
        if call["label"] in ("coder:implement", "architect:finalize"):
            assert flags["indexXml"] is True, call["label"]
# endregion FUNC_test_prompt_contract_facts


# region FUNC_test_finalize_is_a_separate_architect_call [DOMAIN(9): Finalize; CONCEPT(10): SeparateAssignment; TECH(5): pytest]
## @purpose Require that Finalize is a second, distinct architect call with its own label and phase, made after the last reviewer call, and that no scenario finalizes without an accepted Review.
## @uses _run, _show
## @io none -> None
## @complexity 5
def test_finalize_is_a_separate_architect_call(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    checked = 0
    for name in NAMES:
        out = _run(name)
        tokens = [_token(call) for call in out["calls"]]
        if "F" not in tokens:
            continue
        checked += 1
        _show(out)
        first_final = tokens.index("F")
        assert "R" in tokens and first_final > max(i for i, t in enumerate(tokens) if t == "R"), name
        design = [c for c, t in zip(out["calls"], tokens) if t == "A"]
        final = out["calls"][first_final]
        LOGGER.info("[IMP:9][test_finalize_is_a_separate_architect_call][SEPARATE] %s design=%d finalize=%s", name, len(design), final["label"])
        assert final["phase"] == "Finalize" and final["agentType"] == "methodology-claude:architect" and final["model"] == "opus"
        assert all(c["phase"] == "Architect" for c in design) and design
        assert final["flags"]["finalizeActor"] and not any(c["flags"]["finalizeActor"] for c in design)
    assert checked >= 10
# endregion FUNC_test_finalize_is_a_separate_architect_call


# region FUNC_test_recorded_green_route [DOMAIN(9): RunState; CONCEPT(9): RecorderCommand, Checksum; TECH(5): pytest]
## @purpose Require six records in phase order with the exact quoted helper command, a single-line ASCII record, no context except the Code source change and the Code artifacts equal to the Code return, and a checksum line whose expected length and code-unit sum equal the values this test recomputes from the record text.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_recorded_green_route(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run("green_recorded")
    _show(out)
    state = TARGET + "/.methodology/runs/run-001/state.json"
    cli = "/work/methodology/implementations/claude/skills/feature-dev/scripts/run_state.py"
    records = out["records"]
    LOGGER.info("[IMP:9][test_recorded_green_route][RECORDS] count=%d", len(records))
    assert [r["phase"] for r in records] == ["bootstrap", "architect", "code", "qa", "review", "finalize"]
    assert [r["status"] for r in records] == ["SUCCESS"] * 6
    for i, r in enumerate(records, start=1):
        pending = "%s/.methodology/runs/run-001/pending/%02d-%s.json" % (TARGET, i, r["phase"])
        assert r["file"] == pending and r["ascii"] and r["singleLine"] and r["kind"] == "role"
        assert r["command"].startswith("python3 '%s' record --state '%s' --result '%s' > '" % (cli, state, pending)), r["command"]
        assert r["precheckStep"] is True and r["diagnostic"] is None
        assert r["checksumLine"] and "python3 -c" in r["checksumLine"], r["steps"]
        text = r["text"]
        units = sum(ord(ch) for ch in text) % 4294967296
        LOGGER.info("[IMP:8][test_recorded_green_route][CHECKSUM] record=%d length=%d sum=%d", i, len(text), units)
        assert (r["expectedLength"], r["expectedSum"]) == (len(text), units)
        if r["phase"] == "code":
            assert r["context"] == {"sourceChange": {"mayEdit": ["src/a.py", "tests/test_a.py", "tests/test_guide.md"],
                                                       "artifacts": [TARGET + "/src/a.py", TARGET + "/tests/test_a.py"]}}
        else:
            assert r["context"] is None
# endregion FUNC_test_recorded_green_route


# region FUNC_test_recorded_debug_route [DOMAIN(9): RunState; CONCEPT(10): SpendBeforeEntry; TECH(5): pytest]
## @purpose Require that the QA BUG_REPORT is recorded before the debugger is dispatched, that the Debug record carries the precheck step and the touched files together with the regression evidence and the envelope evidence as the surviving artifacts, and that the record order is chronological.
## @uses _run, _show
## @io none -> None
## @complexity 6
def test_recorded_debug_route(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run("qa_bug_debug_fixed_recorded")
    _show(out)
    tokens = [_token(call) for call in out["calls"]]
    records = out["records"]
    bug_at = next(i for i, call in enumerate(out["calls"]) if call["label"].startswith("recorder:qa#04"))
    debugger_at = tokens.index("D")
    LOGGER.info("[IMP:9][test_recorded_debug_route][ORDER] bug_record_call=%d debugger_call=%d", bug_at + 1, debugger_at + 1)
    assert bug_at + 1 == debugger_at and tokens[bug_at] == "X"
    assert [(r["phase"], r["status"]) for r in records] == [
        ("bootstrap", "SUCCESS"), ("architect", "SUCCESS"), ("code", "SUCCESS"), ("qa", "BUG_REPORT"),
        ("debug", "FIXED"), ("qa", "SUCCESS"), ("review", "SUCCESS"), ("finalize", "SUCCESS")]
    debug = records[4]
    assert debug["precheckStep"] is True
    assert debug["context"] == {"sourceChange": {"mayEdit": ["src/a.py", "tests/test_a.py", "tests/test_guide.md"],
                                                 "artifacts": [TARGET + "/src/a.py", TARGET + "/tests/test_guide.md", TARGET + "/evidence/debug.txt"]}}
    assert records[3]["context"] is None
    assert out["debugSpent"] == 1 and out["status"] == "SUCCESS"
# endregion FUNC_test_recorded_debug_route


# region FUNC_test_debug_allowance_facts [DOMAIN(10): Debug; CONCEPT(10): CumulativeCap, ZeroValid, HonestEscalation; TECH(5): pytest]
## @purpose Require the escalation facts at an exhausted cap (spent, cap, chronological attempts paired with causes), no Debug at all for cap zero, a preserved entry after a BLOCKED Debug, and an owner decision that offers no extra Debug entries because the helper has no grant mechanism.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_debug_allowance_facts(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    capped = _run("qa_bug_twice_cap1")
    zero = _run("maxdebug_zero_qa_defect")
    blocked = _run("debug_blocked")
    green = _run("green")
    above = _run("maxdebug_above_supported")
    for out in (capped, zero, blocked):
        _show(out)
    LOGGER.info("[IMP:9][test_debug_allowance_facts][CAP] capped=%s zero=%s", capped["escalation"]["debugSpent"], zero["escalation"]["debugSpent"])
    assert green["maxDebug"] == 4
    esc = capped["escalation"]
    assert (esc["origin"], esc["debugSpent"], esc["cap"]) == ("qa", 1, 1)
    assert len(esc["attempts"]) == 1 and esc["attempts"][0]["origin"] == "qa" and esc["attempts"][0]["filesTouched"]
    assert esc["attempts"][0]["rootCause"] and esc["stillRed"]["recommendation"]
    assert zero["escalation"]["attempts"] == [] and zero["maxDebug"] == 0
    assert not any(call["agentType"].endswith("debugger") for call in zero["calls"])
    assert blocked["debugSpent"] == 1 and blocked["blockedPhase"] == "debug"
    assert "debug:BLOCKED" in blocked["historyEvents"]
    decision = capped["ownerDecision"]
    assert "Grant" not in decision and "additional Debug" not in decision and "1 to 20" not in decision
    assert "BLOCKED" in decision and "owner decision" in decision and "supported bounded mechanism" in decision
    assert above["status"] == "BLOCKED" and "above" in above["reason"] and "unsupported" in above["reason"] and above["calls"] == []
# endregion FUNC_test_debug_allowance_facts


# region FUNC_test_single_response_correction [DOMAIN(10): Correction; CONCEPT(10): OnePerPhaseAttempt; TECH(5): pytest]
## @purpose Require exactly one correction re-dispatch of the same phase with the correction note, none charged to Debug, a second failure ending BLOCKED or ESCALATED_FINALIZE, and the control event of every unusable return recorded in the ledger when the run state is recorded.
## @uses _run, _show
## @io none -> None
## @complexity 8
def test_single_response_correction(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    once = _run("null_corrected")
    twice = _run("null_twice")
    wrong_origin = _run("debug_origin_mismatch_corrected")
    final_twice = _run("finalize_null_twice")
    recorded = _run("null_twice_recorded")
    final_recorded = _run("finalize_null_twice_recorded")
    for out in (once, twice, wrong_origin, final_twice, recorded, final_recorded):
        _show(out)
    qa_calls = [c for c in once["calls"] if c["agentType"].endswith(":qa")]
    LOGGER.info("[IMP:9][test_single_response_correction][CORRECTION] qa_calls=%d labels=%s", len(qa_calls), [c["label"] for c in qa_calls])
    assert [c["label"] for c in qa_calls] == ["qa#1:verify", "qa#1:verify:correction"]
    assert [c["flags"]["correction"] for c in qa_calls] == [False, True]
    assert once["historyEvents"].count("response-correction") == 1 and once["debugSpent"] == 0
    assert twice["status"] == "BLOCKED" and twice["historyEvents"].count("second-unusable-return") == 1
    assert len([c for c in twice["calls"] if c["agentType"].endswith(":qa")]) == 2
    assert not any(c["agentType"].endswith(":reviewer") or c["agentType"].endswith(":debugger") for c in twice["calls"])
    assert wrong_origin["debugSpent"] == 1 and sum(1 for c in wrong_origin["calls"] if c["agentType"].endswith(":debugger")) == 2
    assert final_twice["status"] == "ESCALATED_FINALIZE" and final_twice["calls"][-1]["label"] == "architect:finalize:correction"
    assert not any(c["agentType"].endswith(":debugger") for c in final_twice["calls"])
    for out, phase in ((recorded, "qa"), (final_recorded, "finalize")):
        controls = [r for r in out["records"] if r["kind"] == "control"]
        assert len(controls) == 2 and [r["phase"] for r in controls] == [phase, phase]
        for r in controls:
            assert r["status"] == "response-correction" and r["unknownEffect"] is False
            assert len(r["evidence"]) == 1 and r["evidence"][0].startswith(TARGET + "/.methodology/runs/run-001/pending/") and r["evidence"][0].endswith("-" + phase + "-correction.txt")
            assert r["diagnostic"] and "STEP 2a" in " ".join(r["steps"])
            assert r["diagPath"] == r["evidence"][0]
        assert "ledger" not in out or out["ledger"] is None
# endregion FUNC_test_single_response_correction


# region FUNC_test_transport_failure_is_not_a_correction [DOMAIN(10): Correction; CONCEPT(10): TransportRetryLimitZero, UnknownEffect; TECH(5): pytest]
## @purpose Require that a thrown agent error in a writer phase and in a read-only phase ends BLOCKED with the typed cause and the instruction to investigate before replay, that the phase is dispatched exactly once, that no control event is recorded (the helper refuses an unknown effect) and that the root is told what the ledger shows.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_transport_failure_is_not_a_correction(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    writer = _run("agent_throws")
    reader = _run("agent_throws_readonly")
    for out in (writer, reader):
        _show(out)
        LOGGER.info("[IMP:9][test_transport_failure_is_not_a_correction][BLOCKED] %s %s", out["scenario"], out["blockedPhase"])
        assert out["status"] == "BLOCKED" and "transport" in out["reason"] and "unknown effect: investigate before replay" in out["reason"]
        assert out["historyEvents"].count("transport-failure") == 1 and "response-correction" not in out["historyEvents"]
    assert [c["label"] for c in writer["calls"] if c["agentType"].endswith(":coder")] == ["coder:implement"]
    assert [c["label"] for c in reader["calls"] if c["agentType"].endswith(":qa")] == ["qa#1:verify"]
    assert not any(r["kind"] == "control" for r in writer["records"])
    assert writer["blockedPhase"] == "code" and reader["blockedPhase"] == "qa"
    assert writer["transportFailure"] == {"kind": "transport", "phase": "code", "cause": "transport fault", "retryLimit": 0, "replayed": False}
    assert reader["transportFailure"]["phase"] == "qa" and reader["transportFailure"]["cause"] == "connection reset"
    assert "show --state" in writer["ledgerNote"] and "RUNNING" in writer["ledgerNote"] and "unknown effect" in writer["ledgerNote"]
# endregion FUNC_test_transport_failure_is_not_a_correction


# region FUNC_test_eight_scans_enforced [DOMAIN(10): QA; CONCEPT(10): EightNamedScans; TECH(5): pytest]
## @purpose Require that seven scans, eight rows with a duplicated and a missing name, and a SUCCESS that contradicts a FAIL or BLOCKED scan, are not accepted (one correction, then BLOCKED, no Review), while a corrected eight-scan return proceeds.
## @uses _run, _show
## @io none -> None
## @complexity 6
def test_eight_scans_enforced(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    seven = _run("qa_seven_scans")
    duplicated = _run("qa_duplicate_scan")
    contradicted = _run("qa_success_failed_scan")
    corrected = _run("qa_seven_then_eight")
    for out in (seven, duplicated, contradicted, corrected):
        _show(out)
    LOGGER.info("[IMP:9][test_eight_scans_enforced][SCANS] seven=%s duplicated=%s contradicted=%s corrected=%s", seven["status"], duplicated["status"], contradicted["status"], corrected["status"])
    for out in (seven, duplicated, contradicted):
        assert out["status"] == "BLOCKED" and out["blockedPhase"] == "qa"
        assert not any(c["agentType"].endswith(":reviewer") for c in out["calls"])
        assert out["historyEvents"].count("response-correction") == 1
    assert corrected["status"] == "SUCCESS" and corrected["qaRuns"] == 1
    assert len([c for c in corrected["calls"] if c["agentType"].endswith(":qa")]) == 2
# endregion FUNC_test_eight_scans_enforced


# region FUNC_test_helper_shapes_rejected_in_script [DOMAIN(10): Alignment; CONCEPT(10): HelperRefusalsCaughtFirst; TECH(5): pytest]
## @purpose Require that directory, dot-slash, dot-dot and absolute scope entries, evidence outside the target, the extra Architect requirements field and a Doxygen PASS record that carries prohibition fields each earn the one response correction in the script, while silent builds (empty Doxygen and visual gate output) and a Finalize doxygenPath without a file extension (no extension heuristic; the recorder precheck judges directories and missing files, see test_real_containment_and_files) are accepted without a correction.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_helper_shapes_rejected_in_script(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    corrected = ["scope_directory_entry", "scope_dot_slash_entry", "scope_dotdot_entry", "scope_absolute_entry", "evidence_spec_outside_target",
                 "architect_requirements_field", "doxygen_pass_with_prohibition_fields"]
    for name in corrected:
        out = _run(name)
        _show(out)
        LOGGER.info("[IMP:9][test_helper_shapes_rejected_in_script][CORRECTED] %s status=%s", name, out["status"])
        assert out["status"] == "SUCCESS" and out["historyEvents"].count("response-correction") == 1, name
    for name in ("visual_gate_empty_output", "doxygen_empty_output", "finalize_extensionless_doxygen"):
        out = _run(name)
        _show(out)
        assert out["status"] == "SUCCESS" and "response-correction" not in out["historyEvents"], name
# endregion FUNC_test_helper_shapes_rejected_in_script


# region FUNC_test_invalid_invocation_dispatches_nothing [DOMAIN(8): Invocation; CONCEPT(9): FailClosed; TECH(5): pytest]
## @purpose Require ERROR with zero agent calls for a missing, mistyped, relative, unknown, whitespace, shell-metacharacter or quote-bearing path argument, for every refused scratch root (twenty-one scenarios in all) and for every invalid Debug cap (-1, 1.5, true, the string 4).
## @uses _run, _show
## @io none -> None
## @complexity 4
def test_invalid_invocation_dispatches_nothing(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    names = [n for n in NAMES if n.startswith(("args_missing", "args_unknown", "args_relative", "args_whitespace", "args_metachar", "args_quote", "args_scratch", "invalid_maxdebug"))]
    assert len(names) == 21
    for name in names:
        out = _run(name)
        _show(out)
        LOGGER.info("[IMP:9][test_invalid_invocation_dispatches_nothing][ERROR] %s calls=%d", name, len(out["calls"]))
        assert out["status"] == "ERROR" and out["calls"] == [] and out["reason"]
        assert out["debugSpent"] == 0 and out["historyEvents"] == []
    assert "maxDebug" in _run("invalid_maxdebug_string")["reason"]
    assert "maxDebugIters" in _run("args_unknown_key")["reason"]
    for name in ("args_whitespace_path", "args_metachar_path", "args_quote_path"):
        assert "shell" in _run(name)["reason"] or "whitespace" in _run(name)["reason"], name
        assert "ASCII letters" in _run(name)["reason"], name
    assert _run("args_json_string")["status"] == "SUCCESS"
# endregion FUNC_test_invalid_invocation_dispatches_nothing


# region FUNC_test_recorder_failures [DOMAIN(8): RunState; CONCEPT(9): ExitCodeAuthority, UnknownOutcome, Integrity; TECH(5): pytest]
## @purpose Require BLOCKED with the helper stderr for a nonzero exit, BLOCKED with the unknown-outcome instruction for a dead recorder (no replay), BLOCKED for a ledger whose Debug spend disagrees with the script count, BLOCKED with the integrity cause for a recorder that reports a checksum different from the record, and the response correction of a Debug return that has no surviving artifact.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_recorder_failures(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    refused = _run("recorder_nonzero")
    dead = _run("recorder_null")
    mismatch = _run("ledger_spend_mismatch")
    lie = _run("recorder_checksum_lie")
    precheck = _run("recorder_precheck_exit")
    for out in (refused, dead, mismatch, lie, precheck):
        _show(out)
    LOGGER.info("[IMP:9][test_recorder_failures][LEDGER] refused=%s dead=%s mismatch=%s lie=%s", refused["ledger"]["kind"], dead["ledger"]["kind"], mismatch["ledger"]["kind"], lie["ledger"]["kind"])
    assert refused["status"] == "BLOCKED" and refused["blockedPhase"] == "code"
    assert refused["ledger"]["exitCode"] == 2 and "outside parent sourceChange scope" in refused["ledger"]["stderr"]
    assert refused["ledgerNote"] and "show keeps refusing" in refused["ledgerNote"] and "unexpected target candidate change" in refused["ledgerNote"] and "HANDOFF" in refused["ledgerNote"]
    assert dead["status"] == "BLOCKED" and dead["ledger"]["kind"] == "unknown" and "show --state" in dead["reason"]
    recorder_calls = [c for c in dead["calls"] if c["agentType"] == "general-purpose"]
    assert len(recorder_calls) == 2 and dead["calls"][-1]["agentType"] == "general-purpose"
    assert mismatch["ledger"]["kind"] == "mismatch" and "debug_spent" in mismatch["reason"] and mismatch["debugSpent"] == 0
    assert lie["status"] == "BLOCKED" and lie["ledger"]["kind"] == "integrity" and "checksum" in lie["reason"] and lie["blockedPhase"] == "architect"
    assert precheck["status"] == "SUCCESS" and precheck["historyEvents"].count("response-correction") == 1
    debug_calls = [c["label"] for c in precheck["calls"] if c["agentType"].endswith(":debugger")]
    assert debug_calls == ["debugger#1:from-qa", "debugger#1:from-qa:correction"]
# endregion FUNC_test_recorder_failures


# region FUNC_test_scratch_argument_rules [DOMAIN(9): Invocation; CONCEPT(10): JudgeScratchRoot, FailClosed; TECH(5): pytest]
## @purpose Require that the scratch argument is mandatory and is judged before any agent: absent, relative, inside the target, around the target (also when the two are spelled with and without /private, under /var/folders too, or differ only by case), outside the default safe prefixes of the guard, the prefix itself and a path with whitespace each end ERROR with a reason that names the rule; a sibling target and scratch root in mixed alias spellings are accepted (the positive control).
## @uses _run, _show
## @io none -> None
## @complexity 5
def test_scratch_argument_rules(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    expected = {
        "args_scratch_missing": ("scratch must be a canonical absolute path", "required"),
        "args_scratch_relative": ("scratch must be a canonical absolute path", "required"),
        "args_scratch_in_target": ("disjoint from target", "never writes inside the target"),
        "args_scratch_around_target": ("disjoint from target", "never writes inside the target"),
        "args_scratch_unsafe_root": ("scratch must lie strictly under one of", "/private/var/folders"),
        "args_scratch_prefix_itself": ("scratch must lie strictly under one of", "/tmp"),
        "args_scratch_whitespace": ("scratch contains whitespace", "ASCII letters"),
        "args_scratch_alias_in_target": ("disjoint from target", "never writes inside the target"),
        "args_scratch_alias_around_target": ("disjoint from target", "never writes inside the target"),
        "args_scratch_alias_var_folders": ("disjoint from target", "never writes inside the target"),
        "args_scratch_case_variant": ("disjoint from target", "case is ignored"),
    }
    for name, parts in expected.items():
        out = _run(name)
        _show(out)
        LOGGER.info("[IMP:9][test_scratch_argument_rules][ERROR] %s reason=%s", name, out["reason"][:120])
        assert out["status"] == "ERROR" and out["calls"] == [], name
        assert all(part in out["reason"] for part in parts), (name, out["reason"])
    siblings = _run("judge_alias_siblings_accepted")
    _show(siblings)
    print("[IMP:9] positive control: target /tmp/m22-sib and scratch /private/tmp/m22-sib-scratch (siblings, mixed alias spellings) status=%s" % siblings["status"])
    assert siblings["status"] == "SUCCESS" and "response-correction" not in siblings["historyEvents"]
# endregion FUNC_test_scratch_argument_rules


# region FUNC_test_judge_assignments_grant_scratch_only [DOMAIN(10): Delegation; CONCEPT(10): WriteGrantsMatchGuard, JudgeScratchRoot; TECH(5): pytest]
## @purpose Require that the qa and reviewer assignments grant the scratch directory scratch-root/RUN/NN-phase/ and no writable location inside the target, name the target as read only, still name the evidence home as the place the root fills, and that the writer assignments keep the in-target evidence root and no scratch grant.
## @uses _run, _show
## @io none -> None
## @complexity 6
def test_judge_assignments_grant_scratch_only(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run("judge_scratch_recorded")
    _show(out)
    roles = [c for c in out["calls"] if c["agentType"] != "general-purpose"]
    LOGGER.info("[IMP:9][test_judge_assignments_grant_scratch_only][ROLES] count=%d", len(roles))
    assert len(roles) == 6
    for call in roles:
        flags = call["flags"]
        role = call["agentType"].split(":")[1]
        if role in ("qa", "reviewer"):
            assert flags["scratchGrant"] is True and flags["scratchRoot"] is True, call["label"]
            assert flags["evidenceGrant"] is False and flags["targetWritable"] is False, call["label"]
            assert flags["evidenceRoot"] is True, call["label"]
        elif role in ("architect", "coder", "debugger"):
            assert flags["evidenceGrant"] is True and flags["scratchGrant"] is False and flags["targetWritable"] is True, call["label"]
        elif role == "searcher":
            assert flags["evidenceGrant"] is False and flags["scratchGrant"] is False, call["label"]
        if call["label"] in ("architect:design", "coder:implement"):
            assert flags["generatedAdvice"] is True, call["label"]
# endregion FUNC_test_judge_assignments_grant_scratch_only


# region FUNC_test_judge_scratch_citations_are_imported [DOMAIN(10): Evidence; CONCEPT(10): ScratchImportInRecord; TECH(5): pytest]
## @purpose Require, for a recorded route whose qa and reviewer cite scratch files (under scratch-root/RUN/NN-phase/) in every judge evidence field, that the records sent to the helper carry only the imported paths under target/.methodology/evidence/RUN/NN-phase/ (same basename, a numbered prefix for a second file with the same basename), that the recorder prompt names the matching import pairs, that no scratch path reaches a record and that the accepted results in the terminal follow the records.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_judge_scratch_citations_are_imported(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run("judge_scratch_recorded")
    _show(out)
    root = "/tmp/m22-scratch"
    scratch = root + "/run-001"
    home = TARGET + "/.methodology/evidence/run-001"
    qa = next(r for r in out["records"] if r["phase"] == "qa")
    review = next(r for r in out["records"] if r["phase"] == "review")
    LOGGER.info("[IMP:9][test_judge_scratch_citations_are_imported][IMPORTS] qa=%s review=%s", qa["imports"], review["imports"])
    assert qa["imports"] == [
        [scratch + "/04-qa/run.log", home + "/04-qa/run.log"],
        [scratch + "/04-qa/probe/run.log", home + "/04-qa/2-run.log"],
        [scratch + "/04-qa/report.md", home + "/04-qa/report.md"],
    ]
    assert review["imports"] == [[scratch + "/05-review/notes.md", home + "/05-review/notes.md"]]
    for record in (qa, review):
        assert root not in record["text"]
        assert record["ascii"] is True and record["singleLine"] is True
        sent = json.loads(record["text"])["result"]
        cited = list(sent["evidence"]) + list(sent.get("diffEvidence", []))
        for row in sent.get("scans", []) + sent["findings"]:
            cited += row["evidence"]
        assert all(path.startswith(TARGET + "/") for path in cited), cited
        assert {dst for _, dst in record["imports"]} <= set(cited)
        units = sum(ord(ch) for ch in record["text"]) % 4294967296
        assert (record["expectedLength"], record["expectedSum"]) == (len(record["text"]), units)
    assert [r["imports"] for r in out["records"] if r["phase"] not in ("qa", "review")] == [[]] * 4
    assert out["reportEvidence"]["qa"][:2] == [home + "/04-qa/run.log", home + "/04-qa/2-run.log"]
    assert out["reportEvidence"]["review"] == [home + "/05-review/notes.md"]
# endregion FUNC_test_judge_scratch_citations_are_imported


# region FUNC_test_scratch_citation_rules [DOMAIN(9): Evidence; CONCEPT(10): ContainedOrScratchOnly; TECH(5): pytest]
## @purpose Require that the run namespace of the scratch root is accepted only in the evidence fields of a judge: a judge that cites a file outside the target and the namespace, a path with a space, a dot segment or a directory, the flat layout of the earlier spine or another run's directory, and a writer that cites a scratch file each earn the one response correction; the diagnostic mode without a ledger accepts a scratch citation and imports nothing.
## @uses _run, _show
## @io none -> None
## @complexity 6
def test_scratch_citation_rules(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    for name in ("judge_evidence_outside_corrected", "judge_scratch_unsafe_corrected", "judge_scratch_dotdot_corrected",
                 "judge_scratch_directory_corrected", "writer_cites_scratch_corrected", "judge_scratch_old_layout_corrected",
                 "judge_scratch_other_run_corrected"):
        out = _run(name)
        _show(out)
        LOGGER.info("[IMP:9][test_scratch_citation_rules][CORRECTED] %s status=%s", name, out["status"])
        assert out["status"] == "SUCCESS" and out["historyEvents"].count("response-correction") == 1, name
    unrecorded = _run("judge_scratch_unrecorded")
    _show(unrecorded)
    assert unrecorded["status"] == "SUCCESS" and unrecorded["records"] == [] and "response-correction" not in unrecorded["historyEvents"]
    assert unrecorded["reportEvidence"]["qa"] == ["/tmp/m22-scratch/run-001/01-qa/run.log"]
# endregion FUNC_test_scratch_citation_rules


# region FUNC_test_recorder_transport_failures [DOMAIN(10): RunState; CONCEPT(10): RecorderThrows, UnknownOutcome, NoSilentContinuation; TECH(5): pytest]
## @purpose Require that a recorder call that throws ends the run BLOCKED with ledger kind transport and a transportFailure on the recorder channel, both on a progress record and on a response-correction episode (the run does not continue to SUCCESS with only a ledger note), that an unusable recorder answer on a correction episode ends BLOCKED with kind unknown, that nothing is replayed, and that the role transport failure keeps its own shape.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_recorder_transport_failures(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    progress = _run("recorder_throws")
    episode = _run("recorder_throws_on_correction")
    unusable = _run("recorder_null_on_correction")
    finalize = _run("recorder_throws_on_finalize_correction")
    role = _run("agent_throws")
    for out in (progress, episode, unusable, finalize, role):
        _show(out)
    LOGGER.info("[IMP:9][test_recorder_transport_failures][KINDS] progress=%s episode=%s unusable=%s", progress["ledger"]["kind"], episode["ledger"]["kind"], unusable["ledger"]["kind"])
    for out, phase in ((progress, "architect"), (episode, "qa"), (finalize, "finalize")):
        assert out["status"] == "BLOCKED" and out["blockedPhase"] == phase
        assert out["ledger"] == {"kind": "transport", "exitCode": None, "stderr": ""}
        assert out["transportFailure"] == {"kind": "transport", "phase": phase, "cause": "recorder transport fault", "retryLimit": 0, "replayed": False, "channel": "recorder"}
        assert "unknown" in out["reason"] and "show --state" in out["ledgerNote"] and "never replays a recorder call" in (out["reason"] + out["ledgerNote"])
        assert out["calls"][-1]["agentType"] == "general-purpose"
    assert "episode 1" in episode["reason"] and "recorder-lost" in episode["historyEvents"]
    assert len([c for c in episode["calls"] if c["agentType"].endswith(":qa")]) == 1
    assert not any(c["agentType"].endswith((":reviewer", ":debugger")) for c in episode["calls"])
    assert unusable["status"] == "BLOCKED" and unusable["ledger"]["kind"] == "unknown" and unusable["transportFailure"] is None
    assert "episode 1" in unusable["reason"] and "recorder-lost" in unusable["historyEvents"]
    assert finalize["status"] == "BLOCKED" and "episode 1" in finalize["reason"] and finalize["historyEvents"].count("recorder-lost") == 1
    assert role["transportFailure"] == {"kind": "transport", "phase": "code", "cause": "transport fault", "retryLimit": 0, "replayed": False}
# endregion FUNC_test_recorder_transport_failures


# region FUNC_test_correction_note_depends_on_the_accepted_control [DOMAIN(9): Correction; CONCEPT(10): HonestRecordedClaim; TECH(5): pytest]
## @purpose Require that the correction note of a Code writer says the root recorded the observed partial changes only when the control event of the first attempt was accepted, and says it did not record them (with the recovery steps) when that event was refused.
## @uses _run, _show
## @io none -> None
## @complexity 5
def test_correction_note_depends_on_the_accepted_control(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    accepted = _run("code_null_corrected_recorded")
    refused = _run("code_null_control_refused")
    for out in (accepted, refused):
        _show(out)

    def second(out):
        return next(c for c in out["calls"] if c["label"] == "coder:implement:correction")["flags"]

    LOGGER.info("[IMP:9][test_correction_note_depends_on_the_accepted_control][NOTES] accepted=%s refused=%s", second(accepted)["partialRecorded"], second(refused)["partialRecorded"])
    assert second(accepted)["partialRecorded"] is True and second(accepted)["partialNotRecorded"] is False
    assert second(refused)["partialRecorded"] is False and second(refused)["partialNotRecorded"] is True
    assert accepted["ledgerNote"] is None and "episode 1 of code" in refused["ledgerNote"]
# endregion FUNC_test_correction_note_depends_on_the_accepted_control


# region FUNC_test_review_finding_requires_a_code [DOMAIN(9): ReturnValidation; CONCEPT(10): ReviewFindingCode; TECH(5): pytest]
## @purpose Require that a Review finding without a nonempty code (REV-1102) is an unusable return that earns the one response correction, and that the corrected return proceeds.
## @uses _run, _show
## @io none -> None
## @complexity 4
def test_review_finding_requires_a_code(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _run("review_finding_without_code")
    _show(out)
    reviewer = [c["label"] for c in out["calls"] if c["agentType"].endswith(":reviewer")]
    LOGGER.info("[IMP:9][test_review_finding_requires_a_code][CALLS] %s", reviewer)
    assert reviewer == ["reviewer#1:review", "reviewer#1:review:correction"]
    assert out["status"] == "SUCCESS" and out["historyEvents"].count("response-correction") == 1
# endregion FUNC_test_review_finding_requires_a_code


# region FUNC_test_pre_code_and_scope_refusals [DOMAIN(9): Refusals; CONCEPT(9): SpecVisualScopeUi; TECH(5): pytest]
## @purpose Require SPEC_BLOCKED and VISUAL_GATE_FAIL before Code (no coder call), BLOCKED for a scope deviation and for undeclared UI work, that a PASS needs scanned nodes while an active gate cannot be waived, and that a recorded halt either reaches the helper (the spec halt) or is deliberately not recorded as progress (the scope deviation) with a ledger note in both cases.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_pre_code_and_scope_refusals(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    for name in ("spec_blocked", "architect_blocked_spec", "visual_gate_fail", "visual_gate_zero_nodes", "visual_gate_waived_active"):
        out = _run(name)
        _show(out)
        LOGGER.info("[IMP:9][test_pre_code_and_scope_refusals][PRE_CODE] %s %s", name, out["status"])
        assert not any(c["agentType"].endswith(":coder") for c in out["calls"])
        assert out["reason"]
        if out["status"] == "SPEC_BLOCKED":
            assert out["blockedPhase"] == "architect"
    assert "SCOPE_DEVIATION" in _run("code_scope_violation")["reason"]
    assert "PHASE-504" in _run("ui_discrepancy")["reason"]
    assert "scanned node" in _run("visual_gate_zero_nodes")["reason"] and "cannot be waived" in _run("visual_gate_waived_active")["reason"]
    assert _run("visual_gate_pass")["status"] == "SUCCESS"
    recorded_spec = _run("spec_blocked_recorded")
    deviation = _run("code_scope_violation")
    _show(recorded_spec)
    _show(deviation)
    assert [r["phase"] for r in recorded_spec["records"]] == ["bootstrap", "architect"] and recorded_spec["records"][1]["status"] == "SUCCESS"
    assert "SPEC_BLOCKED" in recorded_spec["ledgerNote"] and "refused" in recorded_spec["ledgerNote"]
    assert [r["phase"] for r in deviation["records"]] == ["bootstrap", "architect"]
    assert "not recorded" in deviation["ledgerNote"] and "SCOPE_DEVIATION" in deviation["ledgerNote"]
# endregion FUNC_test_pre_code_and_scope_refusals


# region FUNC_test_vocabulary_and_trace_shape [DOMAIN(8): Terminals; CONCEPT(9): CanonicalVocabulary, LDDShape; TECH(5): re]
## @purpose Require that every scenario ends in the canonical vocabulary with a named owner decision and that every log line of the script has the [IMP:n][function][BLOCK] shape; the seven terminals are all produced across the suite.
## @uses _run
## @io none -> None
## @complexity 5
def test_vocabulary_and_trace_shape(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    seen, lines = set(), 0
    for name in NAMES:
        out = _run(name)
        seen.add(out["status"])
        for line in out["logs"]:
            lines += 1
            assert LDD_LINE.match(line), (name, line)
        assert set(out["phases"]) <= set(PHASE_TITLES), (name, out["phases"])
    LOGGER.info("[IMP:9][test_vocabulary_and_trace_shape][VOCAB] statuses=%s lines=%d", sorted(seen), lines)
    print("[IMP:9] terminals produced:", sorted(seen), "log lines checked:", lines)
    assert seen == TERMINAL
# endregion FUNC_test_vocabulary_and_trace_shape


# region FUNC_test_real_routes [DOMAIN(10): RealHelper; CONCEPT(10): SpineAndLedgerAgree; TECH(6): pytest.mark.parametrize]
## @purpose Judge each real-helper scenario by the terminal status of the script, the status the helper left in the ledger and the Debug spend in both, with no schema violation and the Debug spend counted by the script equal to the ledger.
## @uses _real, _show
## @io real row -> None
## @complexity 6
@pytest.mark.parametrize("name,status,ledger_status,spent", REAL, ids=REAL_NAMES)
def test_real_routes(name, status, ledger_status, spent, real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, name)
    _show(out)
    led = out["ledgerState"]
    LOGGER.info("[IMP:9][test_real_routes][OBSERVED] %s status=%s ledger=%s spent=%s/%s", name, out["status"], led["status"], out["debugSpent"], led["debug_spent"])
    assert out["status"] == status
    assert led["status"] == ledger_status
    assert out["debugSpent"] == spent == led["debug_spent"]
    assert out["schemaViolations"] == []
    assert out["status"] in TERMINAL and out["ownerDecision"]
# endregion FUNC_test_real_routes


# region FUNC_test_real_green_route [DOMAIN(9): RealHelper; CONCEPT(9): SixAcceptedRecords, SilentBuild; TECH(5): pytest]
## @purpose Require that the green route reaches the helper six times in phase order, that the helper accepted every record, that the silent Doxygen build (empty output) and the Finalize map file are in the accepted records, that the report lies under the excluded evidence root and that no correction was needed.
## @uses _real, _show
## @io dict -> None
## @complexity 6
def test_real_green_route(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_green")
    _show(out)
    records = out["records"]
    assert [(r["phase"], r["status"], r["helperExit"]) for r in records] == [
        ("bootstrap", "SUCCESS", 0), ("architect", "SUCCESS", 0), ("code", "SUCCESS", 0), ("qa", "SUCCESS", 0), ("review", "SUCCESS", 0), ("finalize", "SUCCESS", 0)]
    assert out["historyEvents"] == ["bootstrap:SUCCESS", "architect:SUCCESS", "code:SUCCESS", "qa:SUCCESS", "review:SUCCESS", "finalize:SUCCESS"]
    code = json.loads(records[2]["text"])["result"]
    final = json.loads(records[5]["text"])["result"]
    bootstrap = json.loads(records[0]["text"])["result"]
    LOGGER.info("[IMP:9][test_real_green_route][RECORDS] doxygen_output=%r doxygenPath=%s", code["doxygen"]["output"], final["doxygenPath"])
    assert code["doxygen"]["output"] and code["doxygen"]["exitCode"] == 0
    assert final["doxygenPath"].endswith("/doxygen_output/xml/index.xml") and out["doxygenPath"] == final["doxygenPath"]
    assert "/.methodology/evidence/real-001/final-report.md" in final["report"] and "/.methodology/runs/" not in final["report"]
    assert bootstrap["evidence"][0].endswith("/.methodology/runs/real-001/state.json")
    assert out["ledgerState"]["history"][0] == "initialized" and out["ledgerState"]["episodes"] == 0
    assert out["ledgerState"]["scope"] == ["src/a.py", "tests/test_a.py", "tests/test_guide.md"]
    assert out["ledgerNote"] is None
# endregion FUNC_test_real_green_route


# region FUNC_test_real_silent_builds [DOMAIN(9): RealHelper; CONCEPT(9): EmptyOutputAccepted; TECH(5): pytest]
## @purpose Require that a silent Doxygen build and a visual-gate record with empty output, which the helper accepts, are accepted by the script without any correction and reach an accepted ledger.
## @uses _real, _show
## @io dict -> None
## @complexity 4
def test_real_silent_builds(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_silent_builds")
    _show(out)
    architect = json.loads(out["records"][1]["text"])["result"]
    code = json.loads(out["records"][2]["text"])["result"]
    LOGGER.info("[IMP:9][test_real_silent_builds][EMPTY] gate=%r doxygen=%r", architect["visualGate"]["output"], code["doxygen"]["output"])
    assert architect["visualGate"]["output"] == "" and code["doxygen"]["output"] == ""
    assert [r["helperExit"] for r in out["records"]] == [0] * 6 and "response-correction" not in out["historyEvents"]
# endregion FUNC_test_real_silent_builds


# region FUNC_test_real_bound_plan_and_blocked_debug [DOMAIN(9): RealHelper; CONCEPT(9): BoundPlan, PreservedEntry; TECH(5): pytest]
## @purpose Require that a plan which already exists at init stays bound through an unchanged Architect return (accepted, no correction) and that a BLOCKED Debug return keeps its consumed entry in the ledger and ends BLOCKED in both.
## @uses _real, _show
## @io dict -> None
## @complexity 4
def test_real_bound_plan_and_blocked_debug(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    bound = _real(real_runs, "real_bound_plan")
    blocked = _real(real_runs, "real_debug_blocked")
    for out in (bound, blocked):
        _show(out)
    arch = [(r["kind"], r["helperExit"]) for r in bound["records"] if r["phase"] == "architect"]
    LOGGER.info("[IMP:9][test_real_bound_plan_and_blocked_debug][RECORDS] bound=%s blocked=%s", arch, blocked["ledgerState"]["history"][-1])
    assert arch == [("role", 0)] and bound["ledgerState"]["plan"] == "bound" and "response-correction" not in bound["historyEvents"]
    assert blocked["blockedPhase"] == "debug" and blocked["ledgerState"]["debug_spent"] == 1 and blocked["ledgerState"]["history"][-1] == "role:debug:BLOCKED"
# endregion FUNC_test_real_bound_plan_and_blocked_debug


# region FUNC_test_real_arms_of_the_records [DOMAIN(9): RealHelper; CONCEPT(9): DoxygenArms, VisualGateArm, SpecHaltAccepted; TECH(5): pytest]
## @purpose Require that the prohibition arm of the Doxygen record is accepted when the quote carries a denial word and the rule file is in the evidence, that a quote without a denial word and a PASS record with a prohibition field are rejected by the script before the helper (one correction each), that a passing visual gate with real evidence is accepted, and that a BLOCKED Architect return with a human deficiency is accepted by the helper as BLOCKED and described as such.
## @uses _real, _show
## @io dict -> None
## @complexity 6
def test_real_arms_of_the_records(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    prohibited = _real(real_runs, "real_doxygen_prohibited")
    quote = _real(real_runs, "real_doxygen_quote_no_denial")
    extra = _real(real_runs, "real_doxygen_pass_extra_field")
    gate = _real(real_runs, "real_visual_gate_pass")
    halted = _real(real_runs, "real_architect_blocked_spec")
    for out in (prohibited, quote, extra, gate, halted):
        _show(out)
    LOGGER.info("[IMP:9][test_real_arms_of_the_records][ARMS] prohibited=%s quote=%s extra=%s", prohibited["status"], quote["historyEvents"].count("response-correction"), extra["historyEvents"].count("response-correction"))
    final = json.loads(prohibited["records"][-1]["text"])["result"]
    assert "doxygenPath" not in final and "doxygenPath" not in prohibited and "response-correction" not in prohibited["historyEvents"]
    paraphrase = _real(real_runs, "real_doxygen_quote_paraphrase")
    _show(paraphrase)
    first = next(r for r in paraphrase["records"] if r["phase"] == "code")
    assert [(r["kind"], r["helperExit"]) for r in paraphrase["records"] if r["phase"] == "code"] == [("role", None), ("control", 0), ("role", 0)]
    assert first["answer"]["exitCode"] == 3 and "quote not found" in first["answer"]["stderr"] and paraphrase["historyEvents"].count("response-correction") == 1
    for out in (quote, extra):
        code = [(r["kind"], r["helperExit"]) for r in out["records"] if r["phase"] == "code"]
        assert code == [("control", 0), ("role", 0)], code
        assert out["historyEvents"].count("response-correction") == 1 and not any(r["helperExit"] == 2 and r["kind"] == "role" for r in out["records"])
    assert [r["helperExit"] for r in gate["records"]] == [0] * 6 and json.loads(gate["records"][1]["text"])["result"]["visualGate"]["status"] == "PASS"
    assert halted["records"][-1]["phase"] == "architect" and halted["records"][-1]["helperExit"] == 0
    assert "BLOCKED" in halted["ledgerNote"] and "SPEC_BLOCKED" in halted["ledgerNote"] and "accepted" in halted["ledgerNote"]
# endregion FUNC_test_real_arms_of_the_records


# region FUNC_test_real_debug_origins [DOMAIN(10): RealHelper; CONCEPT(10): CausalDebug, SpendBeforeEntry; TECH(5): pytest]
## @purpose Require that a QA, a Code and a Review defect each spend exactly one ledger entry before the debugger is dispatched, that the Debug record is accepted with its pruned artifact list, and that renewed QA and Review follow before Finalize.
## @uses _real, _show
## @io dict -> None
## @complexity 7
@pytest.mark.parametrize("name,origin", [("real_debug_qa", "qa"), ("real_debug_code", "code"), ("real_debug_review", "review")])
def test_real_debug_origins(name, origin, real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, name)
    _show(out)
    labels = [c["label"] for c in out["calls"]]
    bug_record = next(i for i, label in enumerate(labels) if label.startswith("recorder:" + origin) and out["records"][int(label.split("#")[1]) - 1]["status"] == "BUG_REPORT")
    debugger_at = next(i for i, label in enumerate(labels) if label.startswith("debugger#1"))
    LOGGER.info("[IMP:9][test_real_debug_origins][ORDER] %s bug_record_call=%d debugger_call=%d", name, bug_record + 1, debugger_at + 1)
    assert bug_record + 1 == debugger_at
    phases = [(r["phase"], r["status"], r["helperExit"]) for r in out["records"]]
    tail = [("debug", "FIXED", 0), ("qa", "SUCCESS", 0), ("review", "SUCCESS", 0), ("finalize", "SUCCESS", 0)]
    assert phases[-4:] == tail and phases[-5][1] == "BUG_REPORT" and phases[-5][2] == 0
    debug = json.loads(out["records"][-4]["text"])
    assert debug["result"]["origin"] == origin
    kept = [a for a in debug["context"]["sourceChange"]["artifacts"]]
    assert set(debug["result"]["filesTouched"]) | set(debug["result"]["regressionEvidence"]) >= set(kept) and kept
    assert out["ledgerState"]["debug_spent"] == 1 and out["debugSpent"] == 1
    twice = _real(real_runs, "real_debug_twice")
    _show(twice)
    LOGGER.info("[IMP:9][test_real_debug_origins][CUMULATIVE] history=%s", twice["ledgerState"]["history"])
    assert twice["ledgerState"]["history"].count("role:debug:FIXED") == 2 and twice["ledgerState"]["debug_spent"] == 2 and twice["qaRuns"] == 3 and twice["reviewRuns"] == 2
    zero = _real(real_runs, "real_cap_zero")
    _show(zero)
    assert not any(c["agentType"].endswith("debugger") for c in zero["calls"]) and zero["escalation"]["debugSpent"] == 0
# endregion FUNC_test_real_debug_origins


# region FUNC_test_real_scope_forms [DOMAIN(10): RealHelper; CONCEPT(10): ExactRelativeScope; TECH(5): pytest]
## @purpose Require, for a directory entry, a dot-slash entry, a dot-dot entry and an absolute entry in mayEdit, that the script rejected the Architect return before recording (the first architect record is the correction control, never a refused role record) and that the corrected return was accepted with the exact relative scope in the ledger.
## @uses _real, _show
## @io dict -> None
## @complexity 6
@pytest.mark.parametrize("name", SCOPE_FORMS)
def test_real_scope_forms(name, real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, name)
    _show(out)
    arch = [r for r in out["records"] if r["phase"] == "architect"]
    LOGGER.info("[IMP:9][test_real_scope_forms][RECORDS] %s architect=%s", name, [(r["kind"], r["helperExit"]) for r in arch])
    assert [r["kind"] for r in arch] == ["control", "role"]
    assert arch[1]["helperExit"] == 0 and not any(r["helperExit"] == 2 and r["kind"] == "role" for r in out["records"])
    assert out["historyEvents"].count("response-correction") == 1
    assert out["ledgerState"]["scope"] == ["src/a.py", "tests/test_a.py", "tests/test_guide.md"] and out["ledgerState"]["plan"] == "bound"
    assert not any("unsafe relative path" in (r["reason"] or "") for r in out["records"])
# endregion FUNC_test_real_scope_forms


# region FUNC_test_real_containment_and_files [DOMAIN(10): RealHelper; CONCEPT(10): ContainedRegularFiles; TECH(5): pytest]
## @purpose Require that evidence outside the target and an extra file written by the Architect were rejected by the script before the helper saw them, and that a directory given as the Finalize Doxygen path (no extension heuristic in the script) was stopped by the recorder precheck before the helper (exit 3, no helper exit), each with the one correction, and that the corrected returns were accepted by the helper.
## @uses _real, _show
## @io dict -> None
## @complexity 6
def test_real_containment_and_files(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    for name, phase in (("real_evidence_spec", "bootstrap"), ("real_architect_extra_file", "architect")):
        out = _real(real_runs, name)
        _show(out)
        mine = [r for r in out["records"] if r["phase"] == phase]
        LOGGER.info("[IMP:9][test_real_containment_and_files][RECORDS] %s %s", name, [(r["kind"], r["helperExit"], r["reason"]) for r in mine])
        assert [r["kind"] for r in mine] == ["control", "role"], name
        assert mine[1]["helperExit"] == 0 and out["historyEvents"].count("response-correction") == 1, name
        assert not any(r["kind"] == "role" and r["helperExit"] == 2 for r in out["records"]), name
    directory = _real(real_runs, "real_finalize_directory")
    _show(directory)
    mine = [r for r in directory["records"] if r["phase"] == "finalize"]
    LOGGER.info("[IMP:9][test_real_containment_and_files][FINALIZE] %s", [(r["kind"], r["helperExit"], r["answer"]["exitCode"]) for r in mine])
    assert [(r["kind"], r["helperExit"], r["answer"]["exitCode"]) for r in mine] == [("role", None, 3), ("control", 0, 0), ("role", 0, 0)]
    assert json.loads(mine[0]["pruneOut"])["count"] == 1 and directory["historyEvents"].count("response-correction") == 1
    final = json.loads(mine[-1]["text"])["result"]
    assert final["doxygenPath"].endswith("/index.xml")
# endregion FUNC_test_real_containment_and_files


# region FUNC_test_real_cited_files_exist [DOMAIN(10): RealHelper; CONCEPT(10): PrecheckBeforeHelper; TECH(5): pytest]
## @purpose Require that a cited file which does not exist is stopped by the recorder precheck before the helper runs (exit 3, no helper exit), earns the one correction recorded as a control event and is then accepted, and that the same mistake twice ends BLOCKED in the script and in the ledger through two accepted control events.
## @uses _real, _show
## @io dict -> None
## @complexity 6
def test_real_cited_files_exist(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    once = _real(real_runs, "real_nonexistent_evidence")
    twice = _real(real_runs, "real_nonexistent_evidence_twice")
    for out in (once, twice):
        _show(out)
    qa = [(r["kind"], r["helperExit"], r["answer"]["exitCode"]) for r in once["records"] if r["phase"] == "qa"]
    LOGGER.info("[IMP:9][test_real_cited_files_exist][ONCE] qa records=%s", qa)
    assert qa == [("role", None, 3), ("control", 0, 0), ("role", 0, 0)]
    assert once["historyEvents"].count("response-correction") == 1 and "control:qa:response-correction" in once["ledgerState"]["history"]
    first = next(r for r in once["records"] if r["phase"] == "qa")
    assert json.loads(first["pruneOut"])["count"] == 1 and first["answer"]["stderr"].startswith("PRECHECK_FAILED ")
    assert twice["status"] == "BLOCKED" and twice["blockedPhase"] == "qa" and twice["historyEvents"].count("second-unusable-return") == 1
    assert twice["ledgerState"]["status"] == "BLOCKED" and twice["ledgerState"]["history"][-2:] == ["control:qa:response-correction"] * 2
    assert not any(r["helperExit"] is not None and r["phase"] == "qa" and r["kind"] == "role" for r in twice["records"])
# endregion FUNC_test_real_cited_files_exist


# region FUNC_test_real_debug_deletion [DOMAIN(10): RealHelper; CONCEPT(10): SurvivingArtifact, PrunedDeletion; TECH(5): pytest]
## @purpose Require that a Debug fix that only deletes a file is accepted because the regression evidence survives and the deleted path is pruned from the artifacts, and that a Debug return whose every artifact and regression path is gone is stopped by the recorder precheck, corrected once, recorded as a control and then accepted.
## @uses _real, _show
## @io dict -> None
## @complexity 7
def test_real_debug_deletion(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    only = _real(real_runs, "real_debug_delete_only")
    none = _real(real_runs, "real_debug_no_survivor")
    for out in (only, none):
        _show(out)
    debug = [r for r in only["records"] if r["phase"] == "debug"]
    LOGGER.info("[IMP:9][test_real_debug_deletion][ONLY] records=%s", [(r["status"], r["helperExit"], r["pruneOut"]) for r in debug])
    assert len(debug) == 1 and debug[0]["helperExit"] == 0
    sent = json.loads(debug[0]["text"])
    assert sent["result"]["filesTouched"][0].endswith("/tests/test_a.py")
    assert sent["context"]["sourceChange"]["artifacts"][0].endswith("/tests/test_a.py")
    assert json.loads(debug[0]["pruneOut"]) == {"kept": 1, "missing": [], "count": 0, "imported": 0}
    kinds = [(r["phase"], r["kind"], r["helperExit"]) for r in none["records"] if r["phase"] == "debug"]
    LOGGER.info("[IMP:9][test_real_debug_deletion][NONE] records=%s", kinds)
    assert kinds == [("debug", "role", None), ("debug", "control", 0), ("debug", "role", 0)]
    assert none["records"][[r["phase"] for r in none["records"]].index("debug")]["answer"]["exitCode"] == 3
    assert none["historyEvents"].count("response-correction") == 1
    assert "control:debug:response-correction" in none["ledgerState"]["history"]
# endregion FUNC_test_real_debug_deletion


# region FUNC_test_real_refusals_and_causes [DOMAIN(10): RealHelper; CONCEPT(10): HelperReasonReported, TransportUnknownEffect, Integrity; TECH(5): pytest]
## @purpose Require that a helper refusal reaches the owner with the helper reason (the last line, not the log head), that a transport failure after real edits ends BLOCKED without a replay and without a ledger event, and that a record corrupted on its way to the file is stopped by the checksum before the helper runs.
## @uses _real, _show
## @io dict -> None
## @complexity 7
def test_real_refusals_and_causes(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    refusal = _real(real_runs, "real_refusal_reason")
    transport = _real(real_runs, "real_transport_throw")
    corrupt = _real(real_runs, "real_checksum_corrupt")
    for out in (refusal, transport, corrupt):
        _show(out)
    LOGGER.info("[IMP:9][test_real_refusals_and_causes][REASON] tail=%s", refusal["ledger"]["stderr"][-120:])
    assert refusal["blockedPhase"] == "code" and refusal["ledger"]["exitCode"] == 2 and refusal["ledger"]["kind"] == "refused"
    assert "methodology state: candidate changes outside parent sourceChange scope" in refusal["ledger"]["stderr"]
    assert len(refusal["ledger"]["stderr"]) <= 4100
    assert "refused:code:candidate changes outside parent sourceChange scope" in refusal["ledgerState"]["history"]
    assert [c["label"] for c in transport["calls"] if c["agentType"].endswith(":coder")] == ["coder:implement"]
    assert transport["calls"][-1]["agentType"].endswith(":coder")
    assert "unknown effect: investigate before replay" in transport["reason"] and "transport" in transport["reason"]
    assert transport["ledgerState"]["phase"] == "code" and transport["ledgerState"]["history"] == ["initialized", "role:bootstrap:SUCCESS", "role:architect:SUCCESS"]
    assert "show --state" in transport["ledgerNote"] and "RUNNING" in transport["ledgerNote"]
    assert refusal["ledgerNote"] and "show keeps refusing" in refusal["ledgerNote"] and "git status --porcelain -uall" in refusal["ledgerNote"] and "outside parent sourceChange scope" in refusal["ledgerNote"]
    first = corrupt["records"][0]
    assert corrupt["ledger"]["kind"] == "integrity" and first["helperExit"] is None and first["answer"]["exitCode"] == 4
    assert corrupt["ledgerState"]["history"] == ["initialized"] and corrupt["ledgerState"]["phase"] == "bootstrap"
# endregion FUNC_test_real_refusals_and_causes


# region FUNC_test_real_corrections_in_ledger [DOMAIN(10): RealHelper; CONCEPT(10): SecondFailureInLedger; TECH(5): pytest]
## @purpose Require that two unusable returns in a row land in the ledger as BLOCKED (QA) or ESCALATED_FINALIZE (Finalize) through two accepted control events, that one unusable Code return after real edits is absorbed by an accepted control with a scoped source change and is followed by an accepted Code record, and that the episode counter is reset by the accepted return.
## @uses _real, _show
## @io dict -> None
## @complexity 7
def test_real_corrections_in_ledger(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    qa = _real(real_runs, "real_qa_null_twice")
    fin = _real(real_runs, "real_finalize_null_twice")
    code = _real(real_runs, "real_code_null_then_ok")
    for out in (qa, fin, code):
        _show(out)
    LOGGER.info("[IMP:9][test_real_corrections_in_ledger][LEDGER] qa=%s fin=%s", qa["ledgerState"]["history"][-2:], fin["ledgerState"]["history"][-2:])
    assert qa["ledgerState"]["history"][-2:] == ["control:qa:response-correction"] * 2 and qa["ledgerState"]["episodes"] == 2
    assert fin["ledgerState"]["history"][-2:] == ["control:finalize:response-correction"] * 2 and fin["ledgerState"]["episodes"] == 2
    assert [r["helperExit"] for r in qa["records"] if r["kind"] == "control"] == [0, 0]
    assert [r["helperExit"] for r in fin["records"] if r["kind"] == "control"] == [0, 0]
    steps = [(r["phase"], r["kind"], r["helperExit"]) for r in code["records"] if r["phase"] == "code"]
    assert steps == [("code", "control", 0), ("code", "role", 0)]
    control = next(r for r in code["records"] if r["kind"] == "control")
    assert len(control["context"]["sourceChange"]["artifacts"]) == 1 and control["context"]["sourceChange"]["artifacts"][0].endswith("-code-correction.txt")
    assert control["context"]["sourceChange"]["mayEdit"] == ["src/a.py", "tests/test_a.py", "tests/test_guide.md"]
    assert code["ledgerState"]["episodes"] == 0 and "control:code:response-correction" in code["ledgerState"]["history"]
# endregion FUNC_test_real_corrections_in_ledger


# region FUNC_test_real_halts [DOMAIN(10): RealHelper; CONCEPT(10): HaltsAndLedgerNotes; TECH(5): pytest]
## @purpose Require that a spec halt and a visual-gate halt reach the helper, which refuses them by design and records the reason as a refused event, that the ledger note tells the root what the ledger shows, and that a scope deviation is deliberately not recorded as progress (the ledger stays at Code) with a note that says what to record.
## @uses _real, _show
## @io dict -> None
## @complexity 7
def test_real_halts(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    spec = _real(real_runs, "real_spec_blocked")
    gate = _real(real_runs, "real_visual_gate_fail")
    deviation = _real(real_runs, "real_scope_deviation")
    for out in (spec, gate, deviation):
        _show(out)
    LOGGER.info("[IMP:9][test_real_halts][NOTES] spec=%s", spec["ledgerNote"][:120])
    assert "refused:architect:SPEC_BLOCKED: Architect human deficiency" in spec["ledgerState"]["history"]
    assert "refused:architect:VISUAL_GATE_FAIL: visual outcome" in gate["ledgerState"]["history"]
    for out in (spec, gate):
        assert out["records"][-1]["phase"] == "architect" and out["records"][-1]["helperExit"] == 2
        assert out["ledgerState"]["status"] == "RUNNING" and out["ledgerState"]["phase"] == "architect"
        assert "RUNNING" in out["ledgerNote"] and "refused" in out["ledgerNote"] and "HANDOFF" in out["ledgerNote"]
    assert "SCOPE_DEVIATION" in deviation["reason"] and deviation["blockedPhase"] == "code"
    assert not any(r["phase"] == "code" for r in deviation["records"]) and deviation["ledgerState"]["phase"] == "code"
    assert "not recorded" in deviation["ledgerNote"] and "RUNNING" in deviation["ledgerNote"] and "BLOCKED" in deviation["ledgerNote"]
# endregion FUNC_test_real_halts


# region FUNC__guard_verdict [DOMAIN(8): Safety; CONCEPT(9): RealGuardRealPayload; TECH(6): guard_destructive.main]
## @purpose Ask the real PreToolUse guard (the module hooks/guard_destructive.py, in process, with the stdin payload and stdout stream it uses as a hook) what it decides for one Bash command of one agent type in one project, with every METHODOLOGY switch removed from the environment so that the defaults are in force.
## @uses guard_destructive.main, json.dumps, io.StringIO
## @io monkeypatch, str, str, str -> str or None (the permissionDecision, None when the guard is silent)
## @complexity 4
def _guard_verdict(monkeypatch, project, agent, command):
    for name in [n for n in os.environ if n.startswith("METHODOLOGY_")]:
        monkeypatch.delenv(name)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", project)
    payload = {"tool_name": "Bash", "tool_input": {"command": command}, "cwd": project, "agent_type": agent}
    stdout = io.StringIO()
    assert guard_destructive.main(io.StringIO(json.dumps(payload)), stdout) == 0
    text = stdout.getvalue().strip()
    return json.loads(text)["hookSpecificOutput"]["permissionDecision"] if text else None
# endregion FUNC__guard_verdict


# region FUNC_test_judge_grants_agree_with_the_guard [DOMAIN(10): Safety; CONCEPT(10): SideEffectChannelWired, WriteGrantsMatchGuard; TECH(6): pytest, guard_destructive]
## @purpose Require, over the real prompts of the qa and reviewer calls of a real-helper route and with the real guard module, that every location a judge prompt grants as writable is silent under the guard for the agent types qa, reviewer, methodology-claude:qa and methodology-claude:reviewer in every write form a judge uses (the mkdir -p of the grant and a plan command run from the target with its output redirected into the grant included), that each judge prompt grants exactly one writable location and that it is a scratch directory outside the target, and that every path inside the target that the prompts name (the target itself and the evidence home included) is denied for the same agent types in every write form; a grant the guard denies is a side-effect channel that no judge can use.
## @uses _real, _guard_verdict, _show
## @io dict, monkeypatch -> None
## @complexity 8
# BUG_FIX_CONTEXT: the spine granted qa and reviewer the evidence home inside the target while the guard denies those agent types every
# write inside the project, so the delivery channel for their outputs was a promise no test had put against the guard. This test
# reads the prompts of a real run, extracts the grants from the assignment text itself and asks the shipped guard.
def test_judge_grants_agree_with_the_guard(real_runs, monkeypatch, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_judge_scratch")
    _show(out)
    work = pathlib.Path(out["workDir"])
    target = str(work / "target")
    agents = ("qa", "reviewer", "methodology-claude:qa", "methodology-claude:reviewer")
    grant_line = re.compile(r"^(SCRATCH|EVIDENCE) ROOT \(writable[^)]*\): (\S+)$", re.M)
    path_token = re.compile(r"/[A-Za-z0-9._+@=:,/-]+")
    # Write forms the guard judges (a redirection, touch, tee, cp, nested shells, a redirection after cd): silent outside the project,
    # denied inside it. The copy forms (rsync and tar are not judged by the guard) are only required to be silent on a grant.
    write_forms = ("printf x > '{p}/probe.txt'", "touch '{p}/probe.marker'", "tee '{p}/probe.log' < /dev/null", "cp /dev/null '{p}/probe.copy'",
                   "bash -c \"printf x > '{p}/nested.txt'\"", "cd '{p}' && printf x > local.txt && python3 -m pytest -q > run.log 2>&1",
                   "mkdir -p '{p}/copy' && rsync -a --exclude .git '{t}/' '{p}/copy/' && cd '{p}/copy' && python3 -m pytest -q > ../run.log 2>&1",
                   "printf x > '{p}'", "touch '{p}'",
                   "cd '{t}' && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider > '{p}/plan-run.log' 2>&1")
    # mkdir -p of the granted directory is the first step of every judge assignment (the guard leaves a directory creation alone even inside
    # the project, so this form is only required to be silent on a grant); the plan-command form above is the delivery of the plan command output.
    copy_forms = ("git -C '{t}' archive HEAD | tar -x -C '{p}'", "rsync -a --exclude .git '{t}/' '{p}/copy/'", "mkdir -p '{p}'")
    granted_forms = write_forms + copy_forms
    files = [f for f in sorted((work / "prompts").glob("*")) if re.match(r"\d+-(qa|reviewer)_", f.name)]
    LOGGER.info("[IMP:8][test_judge_grants_agree_with_the_guard][PROMPTS] judge prompts=%d", len(files))
    assert [f.name.split("-", 1)[1].split("_")[0] for f in files] == ["qa", "qa", "reviewer"]
    silent = denied = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        grants = grant_line.findall(text)
        for label, grant in grants:
            for agent in agents:
                for form in granted_forms:
                    verdict = _guard_verdict(monkeypatch, target, agent, form.format(p=grant, t=target))
                    LOGGER.info("[IMP:9][test_judge_grants_agree_with_the_guard][GRANT] %s %s %s -> %s", f.name, agent, label, verdict)
                    assert verdict is None, "the guard stops %s on the location its own prompt grants as writable: %s via %r -> %s" % (agent, grant, form, verdict)
                    silent += 1
        assert [label for label, _ in grants] == ["SCRATCH"], (f.name, grants)
        grant = grants[0][1]
        assert grant.startswith(out["scratch"] + "/") and not (grant + "/").startswith(target + "/"), grant
        inside = sorted({tok.rstrip(".,:;/") for tok in path_token.findall(text) if tok.rstrip(".,:;/") == target or tok.startswith(target + "/")})
        assert target in inside and target + "/.methodology/evidence/real-001" in inside and len(inside) >= 5, inside
        for path in inside:
            for agent in agents:
                for form in write_forms:
                    verdict = _guard_verdict(monkeypatch, target, agent, form.format(p=path, t=target))
                    assert verdict == "deny", "the guard lets %s write inside the project: %s via %r -> %s" % (agent, path, form, verdict)
                    denied += 1
    print("[IMP:9] judge prompts=%d silent grant checks=%d denied in-project checks=%d" % (len(files), silent, denied))
    LOGGER.info("[IMP:9][test_judge_grants_agree_with_the_guard][RESULT] silent=%d denied=%d", silent, denied)
    assert silent == 3 * 4 * len(granted_forms) and denied >= 3 * 4 * 5 * len(write_forms)
# endregion FUNC_test_judge_grants_agree_with_the_guard


# region FUNC_test_real_judge_scratch_import [DOMAIN(10): RealHelper; CONCEPT(10): ScratchEvidenceAcceptedByHelper, ImportedPaths; TECH(5): pytest]
## @purpose Require, in a real-helper route whose QA (a red and a green run) and Review write their outputs in the scratch directory their prompt grants and cite them in every evidence field, that the shipped helper accepted every judge record with the imported in-target paths (same basename, a numbered prefix for the second file with one basename), that the files were copied byte for byte while the scratch originals stay, that the scratch directories (inside the run namespace) and the evidence directories share the record numbers, that no scratch path reached a record, and that the Debug and Finalize briefings name the imported files and never the scratch root.
## @uses _real, _show
## @io dict -> None
## @complexity 9
def test_real_judge_scratch_import(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_judge_scratch")
    _show(out)
    scratch, work = out["scratch"], pathlib.Path(out["workDir"])
    assert isinstance(scratch, str) and scratch.startswith("/"), "the run had no scratch root, so no judge could have been granted one"
    target = work / "target"
    home = target / ".methodology" / "evidence" / "real-001"
    judge = [r for r in out["records"] if r["phase"] in ("qa", "review")]
    LOGGER.info("[IMP:9][test_real_judge_scratch_import][RECORDS] %s", [(r["phase"], r["status"], r["helperExit"]) for r in judge])
    assert [(r["phase"], r["status"], r["helperExit"], r["answer"]["exitCode"]) for r in judge] == [
        ("qa", "BUG_REPORT", 0, 0), ("qa", "SUCCESS", 0, 0), ("review", "SUCCESS", 0, 0)]
    assert out["debugSpent"] == 1 and out["ledgerState"]["debug_spent"] == 1 and out["ledgerState"]["status"] == "SUCCESS"
    first, second, review = judge
    for record in judge:
        assert scratch not in record["text"], record["phase"]
        assert json.loads(record["pruneOut"])["count"] == 0
    sent = json.loads(first["text"])["result"]
    assert sent["evidence"] == [str(home / "04-qa" / "run.log"), str(home / "04-qa" / "2-run.log"), str(target / "tests" / "test_guide.md")]
    assert [row["evidence"] for row in sent["scans"]] == [[str(home / "04-qa" / "report.md")]] * 8
    assert sent["findings"][0]["evidence"] == [str(home / "04-qa" / "2-run.log")]
    assert json.loads(first["pruneOut"])["imported"] == 3
    sent = json.loads(review["text"])["result"]
    assert sent["evidence"] == [str(home / "07-review" / "review-notes.md"), str(home / "07-review" / "2-review-notes.md")]
    assert sent["diffEvidence"] == [str(target / "src" / "a.py"), str(home / "07-review" / "review-notes.md")]
    assert sent["findings"][0]["evidence"] == [str(home / "07-review" / "2-review-notes.md")]
    assert (home / "04-qa" / "run.log").read_text() == "pytest run 1: 3 passed\n"
    assert (home / "04-qa" / "2-run.log").read_text() == "probe of run 1 (same basename as the log)\n"
    assert (home / "04-qa" / "report.md").read_text() == "# qa report 1\n"
    assert (home / "06-qa" / "run.log").read_text() == "pytest run 2: 3 passed\n"
    assert (home / "07-review" / "2-review-notes.md").read_text() == "# a second file with the same basename\n"
    for item in out["judgeFiles"]:
        original = pathlib.Path(item["path"])
        assert str(original).startswith(scratch + "/") and original.read_text() == item["text"]
    parts = {pathlib.Path(item["path"]).relative_to(scratch).parts[:2] for item in out["judgeFiles"]}
    shared = sorted(second for first, second in parts)
    LOGGER.info("[IMP:9][test_real_judge_scratch_import][NUMBERS] scratch dirs=%s", sorted(parts))
    assert {first for first, _ in parts} == {"real-001"}, "every judge directory lies in the run namespace <scratch>/<runId>/"
    assert shared == ["04-qa", "06-qa", "07-review"] and sorted(p.name for p in home.iterdir() if p.is_dir()) == shared
    prompts = {f.name: f.read_text(encoding="utf-8") for f in (work / "prompts").glob("*")}
    debugger = next(text for name, text in prompts.items() if "-debugger_" in name)
    finalizer = next(text for name, text in prompts.items() if "architect_finalize" in name)
    assert str(home / "04-qa" / "run.log") in debugger and str(home / "04-qa" / "2-run.log") in debugger and scratch not in debugger
    assert str(home / "06-qa" / "run.log") in finalizer and str(home / "07-review" / "review-notes.md") in finalizer and scratch not in finalizer
# endregion FUNC_test_real_judge_scratch_import


# region FUNC_test_real_judge_scratch_missing [DOMAIN(10): RealHelper; CONCEPT(10): PrecheckBeforeImport, NothingCopiedOnRefusal; TECH(5): pytest]
## @purpose Require that a judge return citing a scratch file that was never written is stopped by the recorder precheck before the helper (exit 3, no helper exit, nothing imported), earns the one correction recorded as a control event, and that the corrected return is imported under the number of its own record.
## @uses _real, _show
## @io dict -> None
## @complexity 6
def test_real_judge_scratch_missing(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_judge_scratch_missing")
    _show(out)
    home = pathlib.Path(out["workDir"]) / "target" / ".methodology" / "evidence" / "real-001"
    qa = [(r["kind"], r["helperExit"], r["answer"]["exitCode"]) for r in out["records"] if r["phase"] == "qa"]
    LOGGER.info("[IMP:9][test_real_judge_scratch_missing][QA] %s", qa)
    assert qa == [("role", None, 3), ("control", 0, 0), ("role", 0, 0)]
    first = next(r for r in out["records"] if r["phase"] == "qa")
    report = json.loads(first["pruneOut"])
    assert report["count"] == 1 and report.get("imported") == 0 and report["missing"][0].endswith("/04-qa/never-written.log")
    assert not (home / "04-qa").exists()
    assert (home / "06-qa" / "run.log").read_text() == "pytest run: 3 passed\n"
    assert out["historyEvents"].count("response-correction") == 1 and "control:qa:response-correction" in out["ledgerState"]["history"]
# endregion FUNC_test_real_judge_scratch_missing


# region FUNC_test_real_precheck_refusals [DOMAIN(10): RealHelper; CONCEPT(10): PrecheckBeforeImport, NothingCopiedOnRefusal, NoOverwrite, NoLinkSource; TECH(5): pytest]
## @purpose Require, against the real helper and a real file system, the three documented refusals of the recorder precheck: a valid scratch file cited next to a scratch file that was never written, an import destination that already exists, and a symbolic link as an import source each stop the record before the helper (exit 3, no helper exit), copy NOTHING (the valid sibling stays out of the evidence home), leave an existing destination byte for byte as it was, earn the one correction recorded as a control event, and the corrected return is imported under the number of its own record.
## @uses _real, _show
## @io dict -> None
## @complexity 9
# BUG_FIX_CONTEXT: the earlier suite had one refusal scenario that cited a single missing file, so a precheck that copied the valid files of a
# refused record, overwrote an existing destination or followed a link source passed every test (three survivors of the independent mutation
# run). Each refusal now has its own real-helper scenario with a valid sibling file, and the assertions look at the file system, not at the verdict.
def test_real_precheck_refusals(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    partial = _real(real_runs, "real_judge_scratch_partial")
    exists = _real(real_runs, "real_judge_scratch_dest_exists")
    link = _real(real_runs, "real_judge_scratch_link")
    for out in (partial, exists, link):
        _show(out)

    def home(out):
        return pathlib.Path(out["workDir"]) / "target" / ".methodology" / "evidence" / "real-001"

    def first(out):
        row = next(r for r in out["records"] if r["phase"] == "qa")
        return row, json.loads(row["pruneOut"])

    for out in (partial, exists, link):
        steps = [(r["kind"], r["helperExit"], r["answer"]["exitCode"]) for r in out["records"] if r["phase"] == "qa"]
        row, report = first(out)
        LOGGER.info("[IMP:9][test_real_precheck_refusals][STEPS] %s qa=%s precheck=%s", out["scenario"], steps, report)
        print("[IMP:9] %s: qa records=%s precheck=%s" % (out["scenario"], steps, report))
        assert steps == [("role", None, 3), ("control", 0, 0), ("role", 0, 0)], out["scenario"]
        assert row["answer"]["stderr"].startswith("PRECHECK_FAILED ") and report["count"] == 1 and report["imported"] == 0 and report["kept"] == -1
        assert out["historyEvents"].count("response-correction") == 1 and "control:qa:response-correction" in out["ledgerState"]["history"]
        assert not any(r["kind"] == "role" and r["helperExit"] == 2 for r in out["records"]), "the helper never saw the refused record"
        assert out["status"] == "SUCCESS" and out["ledgerState"]["status"] == "SUCCESS"
        assert not (home(out) / "04-qa" / "run.log").exists() and not (home(out) / "04-qa" / "real.log").exists(), "nothing of a refused record is copied"
    # (1) a valid scratch file next to one that was never written: the valid one is not imported either.
    assert first(partial)[1]["missing"] == [partial["scratch"] + "/real-001/04-qa/never-written.log"]
    assert not (home(partial) / "04-qa").exists()
    assert (home(partial) / "06-qa" / "run.log").read_text() == "pytest run 2: 3 passed\n"
    # (2) an existing destination is refused, never overwritten, and its sibling is not imported.
    taken = home(exists) / "04-qa"
    assert first(exists)[1]["missing"] == [str(taken / "taken.log") + " (exists)"]
    assert sorted(p.name for p in taken.iterdir()) == ["taken.log"] and (taken / "taken.log").read_text() == "OLD CONTENT\n"
    assert (pathlib.Path(exists["scratch"]) / "real-001" / "04-qa" / "taken.log").read_text() == "NEW CONTENT\n"
    assert (home(exists) / "06-qa" / "second.log").read_text() == "pytest run: 3 passed\n"
    # (3) a link source is refused although it points at a regular file; the valid file cited with it is not imported.
    assert first(link)[1]["missing"] == [link["scratch"] + "/real-001/04-qa/link.log"]
    assert not (home(link) / "04-qa").exists()
    assert (pathlib.Path(link["scratch"]) / "real-001" / "04-qa" / "link.log").is_symlink()
    copied = home(link) / "06-qa" / "real.log"
    assert copied.is_file() and not copied.is_symlink() and copied.read_text() == "pytest run 2: 3 passed\n"
# endregion FUNC_test_real_precheck_refusals


# region FUNC_test_import_names_are_case_insensitive_and_alias_aware [DOMAIN(10): Evidence; CONCEPT(10): CaseInsensitiveDestinations, MacOsAliasCitations; TECH(5): pytest]
## @purpose Require that two cited files whose basenames differ only by case receive two distinct destinations (the numbered candidate is compared without regard to case too), that one physical file cited under both spellings of the macOS alias (/tmp and /private/tmp) is imported once while every citation follows the one destination, and that a /private spelling of a /tmp scratch root is accepted as a citation without a correction.
## @uses _run, _show
## @io none -> None
## @complexity 7
def test_import_names_are_case_insensitive_and_alias_aware(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = "/tmp/m22-scratch/run-001"
    home = TARGET + "/.methodology/evidence/run-001"
    collided = _run("judge_scratch_case_collision")
    aliased = _run("judge_scratch_alias_spellings")
    for out in (collided, aliased):
        _show(out)

    def record(out, phase):
        return next(r for r in out["records"] if r["phase"] == phase)

    LOGGER.info("[IMP:9][test_import_names_are_case_insensitive_and_alias_aware][IMPORTS] qa=%s review=%s", record(collided, "qa")["imports"], record(collided, "review")["imports"])
    print("[IMP:9] case collision imports: qa=%s review=%s" % (record(collided, "qa")["imports"], record(collided, "review")["imports"]))
    print("[IMP:9] alias spellings imports: qa=%s review=%s" % (record(aliased, "qa")["imports"], record(aliased, "review")["imports"]))
    renamed = [line for line in collided["logs"] if "[IMP:8][importPlan][RENAMED]" in line]
    merged = [line for line in aliased["logs"] if "[IMP:8][importPlan][ALIAS]" in line]
    print("[IMP:9] executed path: %d renamed destinations, %d alias citations merged" % (len(renamed), len(merged)))
    assert len(renamed) == 3 and len(merged) == 1, "the spine reports each rename and each merged alias citation at importance 8"
    assert record(collided, "qa")["imports"] == [
        [root + "/04-qa/Run.log", home + "/04-qa/Run.log"],
        [root + "/04-qa/probe/run.log", home + "/04-qa/2-run.log"],
    ]
    assert record(collided, "review")["imports"] == [
        [root + "/05-review/NOTES.md", home + "/05-review/NOTES.md"],
        [root + "/05-review/a/notes.md", home + "/05-review/2-notes.md"],
        [root + "/05-review/b/Notes.md", home + "/05-review/3-Notes.md"],
    ]
    for phase in ("qa", "review"):
        lowered = [dst.lower() for _, dst in record(collided, phase)["imports"]]
        assert len(set(lowered)) == len(lowered), (phase, lowered)
    assert collided["status"] == "SUCCESS" and aliased["status"] == "SUCCESS"
    assert "response-correction" not in aliased["historyEvents"], "a /private spelling of a /tmp scratch root is a citation inside the scratch root"
    assert record(aliased, "qa")["imports"] == [[root + "/04-qa/run.log", home + "/04-qa/run.log"]]
    sent = json.loads(record(aliased, "qa")["text"])["result"]
    assert sent["evidence"] == [home + "/04-qa/run.log", home + "/04-qa/run.log", TARGET + "/tests/test_guide.md"]
    assert record(aliased, "review")["imports"] == [["/private" + root + "/05-review/notes.md", home + "/05-review/notes.md"]]
# endregion FUNC_test_import_names_are_case_insensitive_and_alias_aware


# region FUNC_test_real_import_keeps_case_variant_names_apart [DOMAIN(10): RealHelper; CONCEPT(10): NoLostFile, CaseInsensitiveFileSystem; TECH(5): pytest]
## @purpose Require, on the real file system, that Run.log and probe/run.log cited by one judge are both present in the evidence home with their own content (on a case-insensitive file system one destination would have overwritten the other), and that the file cited in both alias spellings was copied once; the helper accepted the record.
## @uses _real, _show
## @io dict -> None
## @complexity 5
def test_real_import_keeps_case_variant_names_apart(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_judge_scratch_names")
    _show(out)
    home = pathlib.Path(out["workDir"]) / "target" / ".methodology" / "evidence" / "real-001" / "04-qa"
    row = next(r for r in out["records"] if r["phase"] == "qa")
    report = json.loads(row["pruneOut"])
    listing = sorted(p.name for p in home.iterdir())
    LOGGER.info("[IMP:9][test_real_import_keeps_case_variant_names_apart][FILES] listing=%s precheck=%s", listing, report)
    print("[IMP:9] evidence home 04-qa holds %s after the precheck %s" % (listing, report))
    assert row["helperExit"] == 0 and report["count"] == 0 and report["imported"] == 2
    assert listing == ["2-run.log", "Run.log"]
    assert (home / "Run.log").read_text() == "upper-case name\n" and (home / "2-run.log").read_text() == "lower-case name\n"
    sent = json.loads(row["text"])["result"]
    assert sent["evidence"][:3] == [str(home / "Run.log"), str(home / "2-run.log"), str(home / "2-run.log")]
# endregion FUNC_test_real_import_keeps_case_variant_names_apart


# region FUNC_test_judge_directories_are_namespaced_by_run [DOMAIN(10): Delegation; CONCEPT(10): RunNamespace, NoStaleCitation; TECH(5): pytest]
## @purpose Require that the judge directory granted by the assignment is scratch-root/RUN/NN-phase/ (a second run id on the same scratch root is handed other directories and imports into its own evidence home), that every file a judge wrote in a real route lies under scratch-root/RUN/, and that a citation of the flat layout of the earlier spine or of another run's directory earns the one correction.
## @uses _run, _real, _show
## @io dict -> None
## @complexity 6
def test_judge_directories_are_namespaced_by_run(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = "/tmp/m22-scratch"
    first = _run("judge_scratch_recorded")
    second = _run("judge_scratch_second_run")
    real = _real(real_runs, "real_judge_scratch")
    for out in (first, second, real):
        _show(out)

    def grants(out):
        return [c["flags"]["scratchGrantPath"] for c in out["calls"] if c["flags"]["scratchGrant"]]

    LOGGER.info("[IMP:9][test_judge_directories_are_namespaced_by_run][GRANTS] first=%s second=%s", grants(first), grants(second))
    print("[IMP:9] judge grants: run-001=%s run-002=%s" % (grants(first), grants(second)))
    assert grants(first) == [root + "/run-001/04-qa", root + "/run-001/05-review"]
    assert grants(second) == [root + "/run-002/04-qa", root + "/run-002/05-review"]
    assert not set(grants(first)) & set(grants(second))
    qa = next(r for r in second["records"] if r["phase"] == "qa")
    assert qa["imports"] == [[root + "/run-002/04-qa/run.log", TARGET + "/.methodology/evidence/run-002/04-qa/run.log"]]
    assert second["status"] == "SUCCESS" and "response-correction" not in second["historyEvents"]
    assert real["judgeFiles"] and all(item["path"].startswith(real["scratch"] + "/real-001/") for item in real["judgeFiles"])
    for name in ("judge_scratch_old_layout_corrected", "judge_scratch_other_run_corrected"):
        out = _run(name)
        _show(out)
        qa_labels = [c["label"] for c in out["calls"] if c["agentType"].endswith(":qa")]
        print("[IMP:9] %s: qa calls=%s status=%s" % (name, qa_labels, out["status"]))
        assert qa_labels == ["qa#1:verify", "qa#1:verify:correction"] and out["status"] == "SUCCESS", name
# endregion FUNC_test_judge_directories_are_namespaced_by_run


# region FUNC_test_plan_command_output_has_a_deliverable_sink [DOMAIN(10): Delegation; CONCEPT(10): PlanCommandOutputSink, WriteGrantsMatchGuard; TECH(5): pytest]
## @purpose Require, over the real prompts of a real-helper route, that the Architect assignment does not tell the plan to send command output to the evidence root (the plan states its commands without a fixed output sink or with a sink parameter; the writers supply the evidence root, qa and reviewer a scratch directory), and that the qa and reviewer assignments tell the judge to create its scratch directory with mkdir -p first, to run the plan commands with their output there and never to the evidence root or anywhere in the target.
## @uses _real, _show
## @io dict -> None
## @complexity 7
# BUG_FIX_CONTEXT: the Architect assignment told the plan that its Runtime Commands send run logs and test output to the evidence root while QA
# is told to run the plan commands (QA-403) and the guard denies qa every write there, so the commands the plan dictated had no deliverable
# output sink for a judge; the assignments are read as the roles read them.
def test_plan_command_output_has_a_deliverable_sink(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    out = _real(real_runs, "real_judge_scratch")
    _show(out)
    work = pathlib.Path(out["workDir"])
    evidence = str(work / "target") + "/.methodology/evidence/real-001"
    prompts = {f.name: f.read_text(encoding="utf-8") for f in sorted((work / "prompts").glob("*"))}
    architect = next(text for name, text in prompts.items() if "architect_design" in name)
    judges = [(name, text) for name, text in prompts.items() if re.match(r"\d+-(qa|reviewer)_", name)]
    LOGGER.info("[IMP:9][test_plan_command_output_has_a_deliverable_sink][PROMPTS] architect=%d judges=%s", len(architect), [name for name, _ in judges])
    print("[IMP:9] checked the Architect prompt (%d chars) and %d judge prompts: %s" % (len(architect), len(judges), [name for name, _ in judges]))
    assert [name.split("-", 1)[1].split("_")[0] for name, _ in judges] == ["qa", "qa", "reviewer"]
    assert "Runtime Commands send run logs, test output and probe files to" not in architect
    assert re.search(r"Runtime Commands[^.]*\bsend[^.]*" + re.escape(evidence), architect) is None
    for phrase in ("with its output sink as a parameter", "no fixed output sink at all", "never hard-code the evidence root",
                   "The writers (coder and debugger) supply " + evidence, "qa and reviewer supply a scratch directory of their own outside the target"):
        assert phrase in architect, phrase
    for name, text in judges:
        grant = re.search(r"^SCRATCH ROOT \(writable[^)]*\): (\S+)$", text, re.M).group(1)
        assert "create your scratch directory first with mkdir -p '%s'" % grant in text, name
        assert "send every log, test output, report and probe file of those commands to %s and nowhere else" % grant in text, name
        assert "never to the evidence root %s and never to any other location inside the target" % evidence in text, name
        assert "set that parameter to your scratch directory" in text and "A command that names a fixed sink inside the target is not run as written" in text, name
        assert "send run logs, test output and probe files to " + evidence not in text, name
# endregion FUNC_test_plan_command_output_has_a_deliverable_sink


# region FUNC_test_real_git_targets [DOMAIN(10): RealHelper; CONCEPT(10): GitIgnoreCandidate, AntiLoopCounter, IgnoredMap; TECH(6): pytest, git]
## @purpose Require, on real git targets that are the top level of their own work tree, that a red QA run which rewrites the git-ignored Anti-Loop counter enters a counted Debug entry and the route reaches SUCCESS with the counter outside the candidate, that a Doxygen map under the git-ignored docs/api/xml is accepted during Code, and that the same red run and the same map without an ignore rule are refused by the helper (BLOCKED, ledger still at the phase, helper reason and the show-keeps-refusing note reported), so the two positive routes are not vacuous.
## @uses _real, _show, subprocess.run
## @io dict -> None
## @complexity 8
def test_real_git_targets(real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    counter = _real(real_runs, "real_git_counter_debug")
    counter_bad = _real(real_runs, "real_git_counter_unignored")
    mapped = _real(real_runs, "real_git_map_ignored")
    mapped_bad = _real(real_runs, "real_git_map_unignored")
    for out in (counter, counter_bad, mapped, mapped_bad):
        _show(out)

    def ignored(out, path):
        done = subprocess.run(["git", "-C", out["workDir"] + "/target", "check-ignore", "-q", path], capture_output=True)
        return done.returncode == 0

    led = counter["ledgerState"]
    LOGGER.info("[IMP:9][test_real_git_targets][COUNTER] history=%s candidate=%d", led["history"], len(led["candidateFiles"]))
    assert ignored(counter, "tests/.test_counter.json") and not ignored(counter_bad, "tests/.test_counter.json")
    assert (pathlib.Path(counter["workDir"]) / "target" / "tests" / ".test_counter.json").read_text() == '{"attempts": 0}\n'
    assert "tests/.test_counter.json" not in led["candidateFiles"] and "src/a.py" in led["candidateFiles"]
    assert led["debug_spent"] == 1 and "role:qa:BUG_REPORT" in led["history"] and "role:debug:FIXED" in led["history"]
    assert [r["helperExit"] for r in counter["records"] if r["phase"] == "qa"] == [0, 0]
    assert counter_bad["blockedPhase"] == "qa" and counter_bad["ledger"]["kind"] == "refused" and counter_bad["ledgerState"]["phase"] == "qa"
    assert "methodology state:" in counter_bad["ledger"]["stderr"] and counter_bad["debugSpent"] == 0
    assert counter_bad["ledgerNote"] and "show keeps refusing" in counter_bad["ledgerNote"] and "unexpected target candidate change" in counter_bad["ledgerNote"]
    assert ignored(mapped, "docs/api/xml/index.xml") and not ignored(mapped_bad, "docs/api/xml/index.xml")
    code = json.loads(next(r for r in mapped["records"] if r["phase"] == "code")["text"])["result"]
    assert code["doxygen"]["mapPath"].endswith("/target/docs/api/xml") and code["doxygen"]["evidence"][0].endswith("/docs/api/xml/index.xml")
    assert (pathlib.Path(mapped["workDir"]) / "target" / "docs" / "api" / "xml" / "index.xml").is_file()
    assert "docs/api/xml/index.xml" not in mapped["ledgerState"]["candidateFiles"] and "src/a.py" in mapped["ledgerState"]["candidateFiles"]
    assert mapped_bad["blockedPhase"] == "code" and mapped_bad["ledger"]["kind"] == "refused" and mapped_bad["ledgerState"]["phase"] == "code"
    assert "candidate changes outside parent sourceChange scope" in mapped_bad["ledger"]["stderr"]
    assert mapped_bad["ledgerNote"] and "show keeps refusing" in mapped_bad["ledgerNote"]
# endregion FUNC_test_real_git_targets


# region FUNC_test_real_harness_checks_the_diagnostic_path [DOMAIN(8): Harness; CONCEPT(9): Step2aPathEqualsEvidencePath; TECH(6): subprocess, re]
## @purpose Require, with the outcome of both runs printed before the assertions (TST-301), that the real-helper harness takes the diagnostic path from the STEP 2a line of the recorder prompt and refuses a prompt whose path differs from the control evidence path: a copy of the spine whose STEP 2a names another path makes the recorder stub raise instead of writing the diagnostic where the record says, which the spine meets as a thrown recorder (BLOCKED, transport on the recorder channel) while the unmutated spine ends BLOCKED only through its second unusable return.
## @uses _framework_copy, subprocess.run, re.sub
## @io tmp_path, real_framework, real_runs -> None
## @complexity 6
def test_real_harness_checks_the_diagnostic_path(tmp_path, real_framework, real_runs, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = WORKFLOW.read_text(encoding="utf-8")
    mutated, count = re.subn(r"(lines\.push\('STEP 2a WRITE:[^\n]*?)q\(p\.diag\.path\)", r"\1q(p.diag.path + '.moved')", text)
    assert count == 1
    copy = tmp_path / "feature-dev-moved-diagnostic.js"
    copy.write_text(mutated, encoding="utf-8")
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="m22-scratch-", dir="/tmp")).resolve()
    work = (tmp_path / "work").resolve()
    work.mkdir()
    try:
        env = dict(os.environ, M22_WORKFLOW=str(copy), M22_REAL_FRAMEWORK=str(real_framework), M22_REAL_WORK=str(work), M22_REAL_SCRATCH=str(scratch), PYTHONDONTWRITEBYTECODE="1")
        proc = subprocess.run([shutil.which("node"), str(HARNESS), "real_qa_null_twice"], capture_output=True, text=True, timeout=120, env=env)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    out = json.loads(proc.stdout.strip().splitlines()[-1])
    plain = _real(real_runs, "real_qa_null_twice")
    LOGGER.info("[IMP:9][test_real_harness_checks_the_diagnostic_path][RESULT] status=%s", out["status"])
    # TST-301: the observed outcome of both runs is printed before any assertion depends on it.
    print("[IMP:9] mutated spine (STEP 2a names another path): status=%s ledger.kind=%s channel=%s cause=%s" % (
        out["status"], (out.get("ledger") or {}).get("kind"), (out.get("transportFailure") or {}).get("channel"), (out.get("transportFailure") or {}).get("cause")))
    print("[IMP:10] unmutated spine: status=%s transportFailure=%s recorder-lost events=%d" % (plain["status"], plain["transportFailure"], plain["historyEvents"].count("recorder-lost")))
    assert out["status"] == "BLOCKED" and out["transportFailure"]["channel"] == "recorder" and out["ledger"]["kind"] == "transport"
    assert out["transportFailure"]["cause"].startswith("STEP 2a path "), out["transportFailure"]["cause"]
    assert plain["status"] == "BLOCKED" and plain["transportFailure"] is None and "recorder-lost" not in plain["historyEvents"]
# endregion FUNC_test_real_harness_checks_the_diagnostic_path


# region FUNC_test_forbidden_apis_absent [DOMAIN(9): HostRestrictions; CONCEPT(10): PureScript; TECH(5): re]
## @purpose Refuse a clock, randomness, dynamic import, Node specifier, process, Buffer, network or timer API in the script text.
## @uses re.search
## @io caplog -> None
## @complexity 4
def test_forbidden_apis_absent(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = WORKFLOW.read_text(encoding="utf-8")
    hits = {label: re.findall(pattern, text) for label, pattern in FORBIDDEN.items() if re.search(pattern, text)}
    LOGGER.info("[IMP:9][test_forbidden_apis_absent][SCAN] patterns=%d hits=%s", len(FORBIDDEN), sorted(hits))
    print("[IMP:9] forbidden API patterns checked:", len(FORBIDDEN), "hits:", sorted(hits))
    assert hits == {}
    assert len(re.findall(r"^export\b", text, re.M)) == 1
# endregion FUNC_test_forbidden_apis_absent


# region FUNC_test_meta_is_a_pure_literal [DOMAIN(8): Host; CONCEPT(9): PureLiteralMeta; TECH(5): re]
## @purpose Require that the meta object contains only quoted strings, array and object punctuation and the declared keys: no template, no identifier, no call; and that the workflow name differs from the interactive skill name.
## @uses re.sub, re.findall
## @io caplog -> None
## @complexity 5
def test_meta_is_a_pure_literal(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    literal = _meta_text()
    stripped = re.sub(r"'(?:[^'\\]|\\.)*'", "''", literal)
    words = set(re.findall(r"[A-Za-z_$][A-Za-z0-9_$]*", stripped))
    leftovers = set(re.findall(r"[^\s{}\[\],:']", stripped)) - set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_")
    LOGGER.info("[IMP:9][test_meta_is_a_pure_literal][LITERAL] words=%s leftovers=%s", sorted(words), sorted(leftovers))
    print("[IMP:9] meta words:", sorted(words), "leftover punctuation:", sorted(leftovers))
    assert "${" not in literal and "`" not in literal
    assert words == {"name", "description", "phases", "title", "detail"}
    assert leftovers == set()
    text = WORKFLOW.read_text(encoding="utf-8")
    assert re.search(r"^export const meta = \{\s*name: 'feature-dev-workflow'", text, re.M)
    assert not re.search(r"name: 'feature-dev'", text)
# endregion FUNC_test_meta_is_a_pure_literal


# region FUNC_test_meta_evaluates_in_an_empty_context [DOMAIN(7): Host; CONCEPT(9): PureLiteralMeta; TECH(6): NodeJS]
## @purpose Evaluate the literal in a Node context with no globals and require the seven phase titles of the route; every phase title the script announces is one of them.
## @uses subprocess.run, json.loads
## @io caplog -> None
## @complexity 5
def test_meta_evaluates_in_an_empty_context(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    proc = subprocess.run([shutil.which("node"), str(HARNESS), "--meta"], capture_output=True, text=True, timeout=60)
    assert proc.returncode == 0, proc.stderr
    meta = json.loads(proc.stdout)
    LOGGER.info("[IMP:9][test_meta_evaluates_in_an_empty_context][META] keys=%s", sorted(meta))
    assert meta["name"] == "feature-dev-workflow" and sorted(meta) == ["description", "name", "phases"]
    assert [p["title"] for p in meta["phases"]] == PHASE_TITLES
    assert all(isinstance(p["detail"], str) and p["detail"] for p in meta["phases"])
    announced = set(re.findall(r"phase\('([A-Za-z]+)'\)", WORKFLOW.read_text(encoding="utf-8")))
    print("[IMP:9] announced phases:", sorted(announced))
    assert announced == set(PHASE_TITLES)
# endregion FUNC_test_meta_evaluates_in_an_empty_context


# region FUNC_test_markup_regions [DOMAIN(8): Markup; CONCEPT(9): SemanticExoskeleton; TECH(5): re]
## @purpose Require the module contract with its tags, GREP_SUMMARY and STRUCTURE, a paired region around every top-level function, the declared diagnostic-only nature of recordState false, the ledger-note and transport statements, and log() calls that carry the IMP shape.
## @uses re.findall
## @io caplog -> None
## @complexity 6
def test_markup_regions(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = WORKFLOW.read_text(encoding="utf-8")
    functions = re.findall(r"^(?:async )?function (\w+)\(", text, re.M)
    unpaired = [f for f in functions if not re.search(r"^// region FUNC_%s \[" % f, text, re.M) or "// endregion FUNC_%s\n" % f not in text]
    LOGGER.info("[IMP:9][test_markup_regions][REGIONS] functions=%d unpaired=%s", len(functions), unpaired)
    print("[IMP:9] functions:", len(functions), "unpaired:", unpaired)
    assert unpaired == [] and len(functions) >= 35
    contract = text[text.index("// region MODULE_CONTRACT"):text.index("// endregion MODULE_CONTRACT")]
    for tag in ("@purpose", "@scope", "@input", "@output", "@links", "@invariants", "@rationale", "@changes", "@modulemap", "@usecases", "@GREP_SUMMARY", "@STRUCTURE"):
        assert "// ## " + tag in contract, tag
    mapped = re.findall(r"=> (\w+)", contract)
    assert sorted(mapped) == sorted(functions)
    flat = " ".join(contract.split())
    assert "recordState false" in flat and "diagnostic" in flat and "no durable ledger" in flat
    assert "ledgerNote" in flat and "unknown effect" in flat
    bad_logs = [m for m in re.findall(r"log\('([^']*)'", text) if not re.match(r"\[IMP:(10|[1-9])\]\[\w+\]\[[A-Z_]+\] ", m)]
    assert bad_logs == []
    assert text.count("BUG_FIX_CONTEXT") >= 10
# endregion FUNC_test_markup_regions


# region FUNC_test_static_terminal_literals [DOMAIN(8): Terminals; CONCEPT(9): CanonicalVocabulary, HonestOwnerDecision; TECH(5): re]
## @purpose Require that every terminal named by finish() or by an audit status literal in the script is canonical, that the script defines exactly the seven, and that no text offers a Debug grant mechanism the helper does not have.
## @uses re.findall
## @io caplog -> None
## @complexity 4
def test_static_terminal_literals(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = WORKFLOW.read_text(encoding="utf-8")
    named = set(re.findall(r"finish\('([A-Z_]+)'", text)) | set(re.findall(r"\bstatus: '([A-Z_]+)'", text))
    declared = set(re.search(r"const TERMINAL = \[([^\]]*)\]", text).group(1).replace("'", "").replace(" ", "").split(","))
    LOGGER.info("[IMP:9][test_static_terminal_literals][LITERALS] named=%s declared=%d", sorted(named), len(declared))
    print("[IMP:9] terminals named in script:", sorted(named))
    assert declared == TERMINAL
    assert named <= TERMINAL
    assert "Grant a bounded number" not in text and "1 to 20" not in text and "GATE-1209" not in text
# endregion FUNC_test_static_terminal_literals


# region FUNC_test_referenced_paths_exist [DOMAIN(8): InPlaceBinding; CONCEPT(9): ReferenceResolution; TECH(5): json]
## @purpose Require that every neutral owner the prompts name exists in the neutral checkout and every package path the script builds is a declared member of the package layout.
## @uses json.loads, pathlib.Path.is_file
## @io caplog -> None
## @complexity 5
def test_referenced_paths_exist(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = WORKFLOW.read_text(encoding="utf-8")
    owners = sorted(set(re.findall(r"'((?:concepts|roles|code|flow|protocols|checks|process|policies|documents)/[A-Za-z_-]+\.md)[ ']", text)))
    missing = [o for o in owners if not (NEUTRAL / o).is_file()]
    layout = {row["path"] for row in json.loads((PACKAGE / "references/package-layout.json").read_text(encoding="utf-8"))["files"]}
    package_paths = sorted(set(re.findall(r"'/(skills/[\w-]+/scripts/[\w.]+)", text)))
    undeclared = [p for p in package_paths if p not in layout]
    LOGGER.info("[IMP:9][test_referenced_paths_exist][PATHS] owners=%d missing=%s package=%s", len(owners), missing, package_paths)
    print("[IMP:9] neutral owners referenced:", len(owners), "missing:", missing, "package paths:", package_paths)
    assert len(owners) >= 25 and missing == []
    assert package_paths == ["skills/devplan-protocol/scripts/visual_gate_lint.py", "skills/feature-dev/scripts/run_state.py"]
    assert undeclared == []
# endregion FUNC_test_referenced_paths_exist


# region FUNC_test_spine_claims_are_accurate [DOMAIN(8): Documentation; CONCEPT(10): HonestStatements; TECH(5): re]
## @purpose Require, with the findings of the text scan printed before the assertions (TST-301), that the checksum is described as detecting a transcription mismatch and never as proof that the helper read the record, that the transport statements name the role agent (the recorder has its own statement), that the shell-safe path message says ASCII letters, that the doxygenPath extension heuristic is gone, and that the module contract states the scratch argument, the run-namespaced judge write boundary, the macOS alias rule, the mkdir -p duty, the output sink of the plan commands and the recorder transport rule.
## @uses re.search
## @io caplog -> None
## @complexity 5
def test_spine_claims_are_accurate(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = WORKFLOW.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    contract = text[text.index("// region MODULE_CONTRACT"):text.index("// endregion MODULE_CONTRACT")]
    flat_contract = " ".join(contract.split())
    banned = [phrase for phrase in ("proves that the helper read", "proves the helper read", "helper read the record the script sent", "A thrown agent error is a transport failure",
                                    "A file name without an extension is treated as a directory", "<scratch>/<nn>-<phase>/ as its writable location") if phrase in flat]
    wanted = ("scratch is required", "<scratch>/<runId>/<nn>-<phase>/", "(copy, same basename, collision safe", "transportFailure channel recorder", "never continued with only a ledgerNote",
              "mkdir -p", "/private/tmp", "no fixed output sink")
    missing = [phrase for phrase in wanted if phrase not in flat_contract]
    LOGGER.info("[IMP:9][test_spine_claims_are_accurate][TEXT] chars=%d banned=%s missing=%s", len(text), banned, missing)
    # TST-301: what the scan found is printed before the assertions that depend on it.
    print("[IMP:9] spine claims: chars=%d, banned statements present=%s, contract phrases missing=%s" % (len(text), banned, missing))
    assert banned == []
    assert "transcription mismatch" in flat and "does not prove that the helper read" in flat
    assert "A thrown ROLE agent call is a transport failure" in flat
    assert "a thrown recorder call is a different channel" in flat.lower() or "A thrown recorder call is a different channel" in flat
    assert "only ASCII letters, digits and . _ - / + @ = : , are allowed" in flat
    assert not re.search(r"doxygenPath\.slice\(res\.doxygenPath\.lastIndexOf", text)
    assert missing == []
# endregion FUNC_test_spine_claims_are_accurate
