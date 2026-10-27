# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification, InPlacePlugin; TECH(8): Python, pytest]
## @modulecontract
## @purpose Verify that the Claude Code package run-state helper keeps the schema2 contract: package identity binding to the declared layout, candidate lifecycle, eight named scans, cumulative Debug allowance, separate retry units and the real init/show/record CLI.
## @scope Direct helper logic and real subprocess channels over an owned copy of the actual package plus the adapter-declared neutral files; real git repositories for the candidate exclusion policy (git ignore rules, declared fallback list) and for the hermetic git observation (a marker core.fsmonitor program, foreign repository-redirecting variables); the member-completeness check of the real package and its visible-runner trace; the package membership diagnostic and the ambient .DS_Store file; no simulated native acceptance.
## @input Owned pytest tmp_path trees, the real package sources (read only) and canonical fixture records; no credentials or provider state.
## @output Pass or fail outcomes with the actual IMP 7 to 10 trace printed, exact ordered error populations compared with caller-declared profiles, and real CLI streams; no fabricated native acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): subprocess; USES_API(8): shutil; USES_API(8): logging; USES_API(7): pytest; USES_API(7): doxygen; READS_DATA_FROM(9): references/package-layout.json and adapter.json of the real package]
## @links_to_spec AC-M22-3 run-state contract and refusals; AC-M22-5 owned trace and map; BR-4 flow mechanics
## @invariants
## - Fixtures are isolated, deterministic and order-independent; the real package and neutral sources stay read-only.
## - A declared package member that does not exist yet is replaced by a small placeholder inside the temporary copy only and logged as PENDING_MEMBER; the real package is never written.
## - Only test_real_package_complete judges the real package membership, so concurrent package work never hides behind a placeholder.
## - Every failure-capable test declares its exact ordered ERROR population before the refusal; no profile is inferred from observed logs.
## - Fixture role envelopes are structural cases, never authentic approval, independent QA or native execution.
## - Candidate exclusion cases run against real git repositories created in owned directories under a hermetic git environment (no developer global or system configuration); git is the delivery channel under test, so no git call is mocked.
## - The fsmonitor probe arms a marker program outside the target and first proves with a plain git command that this git runs it (otherwise the test is skipped as unprobeable), so an absent marker is evidence and not an unarmed trap; the foreign-environment probe sets the redirecting variables after the hermetic setup and compares the polluted observation with a clean one taken from the same repository.
## - Every membership refusal expectation is a literal label naming the exact relative paths, never recomputed by the helper under test.
## - test_real_package_complete prints the actual IMP 7 to 10 trace before its first assertion (TST-301), and a child-runner probe proves it under pytest -s -v.
## @rationale
## Q: Why direct logic tests and real subprocess tests both?
## A: Direct imports prove the bounded logic with an exact trace; the subprocess proves the shipped channel: argv, stdout answer, stderr trace, exit code and saved ledger.
## Q: Why copy the real package into the fixture instead of a reduced stand-in?
## A: The binding hashes the actual package, adapter and neutral bytes; only the real shapes prove the identity, membership and core checks.
## Q: Why pin the package identity refusals here and not only in the package contract suite?
## A: The binding is the one place this helper differs from its sibling; a refusal case per identity field proves the change is enforced, not just declared.
## Q: Why real git repositories and not a faked ignore list for the candidate exclusion cases?
## A: The defect was that the helper did not follow what git reports as ignored; a faked list would only prove the helper calls its own API (Test-Capture Antipattern), while a real repository with a real ignore file, a real forced add and a real failing index proves the shipped behavior.
## Q: Why a positive control before the fsmonitor absence is asserted?
## A: A marker that is absent proves nothing if the configured program could never have run on this git; the control (a plain git ls-files in the same armed repository creates the marker) turns the absence of the marker during init, show, record, inventory and baseline into evidence, and skips honestly when the control cannot be armed.
## Q: Why does the visible-runner probe start a child pytest instead of inspecting the source?
## A: TST-301 is about what the documented visible runner shows; only a child process under -s -v shows what a reader of the test run sees, and a source scan would pass a print that never executes.
## @changes
## LAST_CHANGE: [1.1.0 - Port of the sibling package suite to the Claude Code package: pending-member placeholders, member completeness check, package identity and layout refusals, adapter Debug allowance refusals. Debug repair of independent Review round 2: candidate exclusion follows git ignore rules with a declared fallback list and keeps the generated build and cache names excluded by name in git targets; 19 cases over real git repositories. Debug repair of independent Review and QA round 3: hermetic git probes (marker core.fsmonitor program never runs during init, show, record, inventory and baseline; foreign GIT_DIR, GIT_INDEX_FILE and GIT_WORK_TREE leave the candidate and baseline unchanged), the ambient .DS_Store file in the package, literal membership diagnostics naming offending paths, and the printed trace of test_real_package_complete with its child-runner probe.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => test_run_state._module_contract
## FUNC 8[List the member paths the real layout declares] => test_run_state.layout_declared
## FUNC 8[List declared members absent from the real package] => test_run_state.missing_members
## FUNC 8[List real package files the layout does not declare] => test_run_state.undeclared_members
## FUNC 7[Choose a small placeholder body for a pending member] => test_run_state.placeholder_text
## FUNC 9[Copy the real package and neutral corpus into an owned tree with pending-member placeholders] => test_run_state.build_tree
## FUNC 9[Initialize an owned schema2 run over the copied tree] => test_run_state.make_fixture
## FUNC 8[Prepare the canonical fixture role envelope] => test_run_state.envelope
## FUNC 9[Supply phase-specific structural fixture evidence] => test_run_state.success
## FUNC 9[Reach an explicitly requested phase in the fixture] => test_run_state.to_phase
## FUNC 9[Declare one exact ordered refusal episode] => test_run_state.error_profile
## FUNC 8[Print the filtered IMP 7 to 10 records and every error before assertions] => test_run_state.print_trace
## FUNC 10[Print the trace and compare the exact ERROR population] => test_run_state.expose
## FUNC 9[Observe the real shipped state process streams] => test_run_state.cli
## FUNC 8[Rewrite a JSON file in the owned copy] => test_run_state.edit_json
## FUNC 10[The real package has every declared member and no undeclared file, and binds] => test_run_state.test_real_package_complete
## FUNC 10[The visible runner shows the real-package trace before its outcome] => test_run_state.test_real_package_complete_exposes_trace_before_asserting
## FUNC 10[Reject unrelated same/foreign logger errors and criticals] => test_run_state.test_expected_error_profile_rejects_unrelated
## FUNC 9[Identity and schema refusals] => test_run_state.test_identity_and_schema_refusals
## FUNC 9[Package identity, profile, roles, kinds and membership refusals] => test_run_state.test_package_binding_identity_and_layout_refusals
## FUNC 9[Layout-driven member count, extended kinds and run contract identity] => test_run_state.test_layout_driven_count_and_identity
## FUNC 10[Ambient .DS_Store is not a package member] => test_run_state.test_ambient_ds_store_in_package_does_not_break_binding
## FUNC 10[Membership refusal names offending paths] => test_run_state.test_membership_refusal_names_offending_paths
## FUNC 9[Adapter Debug allowance refusals and lowering] => test_run_state.test_adapter_debug_allowance
## FUNC 9[Invalid Debug cap types] => test_run_state.test_debug_invalid_type_refusal
## FUNC 9[Debug budget and causal routes] => test_run_state.test_debug_budget_and_causal_routes
## FUNC 9[Zero allowance and green route through Review] => test_run_state.test_zero_allowance_and_green_route
## FUNC 9[Eight named scan verdicts] => test_run_state.test_named_scan_verdicts
## FUNC 9[Pending plan binding and source scope] => test_run_state.test_pending_plan_and_source_scope
## FUNC 9[Response correction once and unknown effects] => test_run_state.test_retry_and_unknown_effects
## FUNC 9[Terminal run and late Finalize] => test_run_state.test_terminal_and_late_finalize
## FUNC 9[Real state CLI and checkpoint resume] => test_run_state.test_real_state_cli_and_checkpoint
## FUNC 9[Own helper trace order and generated map associations] => test_run_state.test_own_helper_trace_and_map
## FUNC 9[Strict textual Debug spelling in the real CLI] => test_run_state.test_real_cli_strict_debug_spelling
## FUNC 9[Unknown return fields, control injection and source drift] => test_run_state.test_unknown_return_control_injection_and_unexpected_source
## FUNC 9[Locked input and containment refusals through the CLI] => test_run_state.test_locked_input_and_containment_process_refusals
## FUNC 9[Zero repair refusal and default allowance] => test_run_state.test_zero_repair_refusal_and_default_allowance
## FUNC 9[Real CLI initialization and no overwrite] => test_run_state.test_real_cli_initialization_and_nonoverwrite
## FUNC 9[Scoped Debug deletion and mode inventory] => test_run_state.test_scoped_debug_deletion_and_mode_inventory
## FUNC 9[Pre-Code BLOCKED routes direct and CLI] => test_run_state.test_precode_blocked_routes_direct_and_cli
## FUNC 9[Explicit Doxygen prohibition and false waivers] => test_run_state.test_explicit_doxygen_prohibition_and_false_waivers
## FUNC 9[Partial Code BUG_REPORT direct and CLI] => test_run_state.test_partial_code_bug_direct_and_cli
## FUNC 9[Partial Code BLOCKED and effect controls] => test_run_state.test_partial_code_blocked_and_effect_controls
## FUNC 9[Full prohibition Finalize route] => test_run_state.test_full_prohibition_finalize_route
## FUNC 8[Disable developer global and system git configuration for one test] => test_run_state.hermetic_git
## FUNC 8[Run one real git command in an owned repository] => test_run_state.git
## FUNC 9[Prepare an owned target that is a real git repository with ignore rules] => test_run_state.prepare_git_target
## FUNC 9[Initialize an owned schema2 run over a real git repository target] => test_run_state.make_git_fixture
## FUNC 8[Prepare the red QA BUG_REPORT of a failing suite run] => test_run_state.qa_bug_report
## FUNC 8[Create ignored virtual environment shapes holding links] => test_run_state.make_venv_links
## FUNC 7[Create one unignored file or directory link] => test_run_state.make_stray_link
## FUNC 7[Create a decomposed Unicode cache directory] => test_run_state.make_decomposed_directory
## FUNC 10[Ignored Anti-Loop counter is not candidate content and QA BUG_REPORT enters Debug] => test_run_state.test_ignored_anti_loop_counter_does_not_change_candidate
## FUNC 10[Ignored Doxygen map written during Code is not candidate content] => test_run_state.test_ignored_code_map_output_is_not_candidate_content
## FUNC 10[Ignored virtual environment with links does not block initialization] => test_run_state.test_ignored_virtual_environment_links_do_not_block_initialization
## FUNC 10[Unignored links are still refused with the exact cascade] => test_run_state.test_unignored_links_are_still_refused
## FUNC 10[Unignored new file still changes the digest and is refused outside scope] => test_run_state.test_unignored_new_file_still_changes_candidate_and_is_refused
## FUNC 10[Ignored file that becomes tracked or unignored is candidate content] => test_run_state.test_ignored_file_that_becomes_tracked_or_unignored_is_candidate
## FUNC 10[Declared fallback list without usable git rules] => test_run_state.test_fallback_exclusion_list_without_usable_git_rules
## FUNC 9[Failing ignore enumeration is refused, not downgraded] => test_run_state.test_git_enumeration_failure_is_refused_not_downgraded
## FUNC 9[Explicit exclusion set never consults git] => test_run_state.test_explicit_exclusion_set_never_consults_git
## FUNC 8[Decomposed Unicode ignored directory is skipped] => test_run_state.test_ignored_decomposed_unicode_directory_is_skipped
## FUNC 10[Generated build and cache names stay excluded in a git target that does not ignore them] => test_run_state.test_generated_outputs_stay_excluded_in_git_target_without_ignore_entries
## FUNC 10[Unignored ordinary file still candidate beside generated outputs] => test_run_state.test_unignored_ordinary_file_still_candidate_beside_generated_outputs
## FUNC 8[Commit named files into a fixture repository] => test_run_state.commit_fixture
## FUNC 9[Arm a marker core.fsmonitor program in a fixture repository] => test_run_state.arm_fsmonitor
## FUNC 7[Read and reset the fsmonitor marker] => test_run_state.consume_marker
## FUNC 7[Build the real init argument list] => test_run_state.init_arguments
## FUNC 10[Repository fsmonitor program never runs] => test_run_state.test_repository_fsmonitor_program_never_runs
## FUNC 10[Foreign git environment leaves the candidate unchanged] => test_run_state.test_foreign_git_environment_leaves_candidate_unchanged
## @usecases
## - [AC-M22-3 package completeness]: Maintainer → add or remove a package member → test_real_package_complete fails until layout and tree agree
## - [AC-M22-3 identity]: Root orchestrator → init over a damaged layout or adapter → test_package_binding_identity_and_layout_refusals and test_adapter_debug_allowance refuse before any state exists
## - [AC-M22-3 Debug cap]: Root orchestrator → request a Debug allowance → test_debug_invalid_type_refusal, test_zero_allowance_and_green_route and test_zero_repair_refusal_and_default_allowance keep zero valid and default four
## - [BR-4 causal Debug]: Root orchestrator → record Code, QA or Review defects → test_debug_budget_and_causal_routes charges once before entry and escalates at the cap
## - [BR-4 eight scans]: Root orchestrator → record a QA return → test_named_scan_verdicts accepts only the eight named list rows
## - [BR-4 Review and Finalize]: Root orchestrator → record Review and Finalize → test_zero_allowance_and_green_route, test_terminal_and_late_finalize and test_full_prohibition_finalize_route keep the order and the late-repair escalation
## - [BR-4 one correction]: Root orchestrator → record a response correction → test_retry_and_unknown_effects allows one then BLOCKED and refuses unknown effects
## - [AC-M22-3 CLI]: Root orchestrator → run init, show and record → test_real_state_cli_and_checkpoint and the CLI refusal tests observe real streams and saved ledgers
## - [AC-M22-5 map]: Maintainer → build the Doxygen map → test_own_helper_trace_and_map checks the owned modules in a copied package
## - [STATE-102 candidate]: Root orchestrator → record a red QA run, a Code map build or an init beside an ignored virtual environment → the ignore-rule tests accept the record and keep the digest; the generated build and cache names stay excluded even when a git project does not ignore them; an unignored file, a forced add or a removed rule still changes it
## - [round 3 hermetic git]: Root orchestrator → init, show or record over a target repository that configures core.fsmonitor or beside a caller environment with a foreign GIT_DIR, GIT_INDEX_FILE or GIT_WORK_TREE → test_repository_fsmonitor_program_never_runs and test_foreign_git_environment_leaves_candidate_unchanged show the program never runs and the candidate and baseline stay the target own
## - [package membership]: Maintainer → ambient .DS_Store or a real stray or missing member in the package → test_ambient_ds_store_in_package_does_not_break_binding and test_membership_refusal_names_offending_paths keep the binding working and name the offender
## - [declared fallback]: Root orchestrator → target without usable git rules → test_fallback_exclusion_list_without_usable_git_rules shows the heuristic list, its limits and that a surrounding repository cannot blind the candidate
## @GREP_SUMMARY Claude Code package, run state tests, schema2 ledger, package identity refusal, pending member placeholder,
##   eight named scans, causal Debug budget, response correction, real CLI init show record, Doxygen map association,
##   candidate identity, git ignore rules, real git repository, Anti-Loop counter, fallback exclusion list, hermetic git,
##   core.fsmonitor marker, foreign GIT_DIR, .DS_Store, membership diagnostic, TST-301 visible trace
## @STRUCTURE ▶ real package + neutral → ○ owned copy with placeholders → ◇ helper logic or real subprocess
##   → ⊕ printed IMP trace + exact ERROR profile → ⎋ assertions on state, ledger and streams
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import ast
import copy
import json
import logging
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import unicodedata
import xml.etree.ElementTree as ET

import pytest
import run_state

logger = logging.getLogger(__name__)
PACKAGE = Path(__file__).resolve().parents[1]
NAMES = ('green-test-trap', 'quantitative-ac', 'semantic-trace', 'infra-dod', 'side-effect-channel', 'secret-leak', 'real-path-shape', 'discriminating-test')
OWN_MODULES = ('skills/feature-dev/scripts/run_state.py', 'skills/devplan-protocol/scripts/visual_gate_lint.py', 'tests/test_run_state.py', 'tests/test_visual_gate.py')
PHASE_ROLE = {'bootstrap': 'searcher', 'architect': 'architect', 'code': 'coder', 'qa': 'qa', 'review': 'reviewer', 'debug': 'debugger', 'finalize': 'architect'}
BUG_FIELDS = ('goal', 'actual', 'logAnalysis', 'dataAnalysis', 'hypothesis', 'recommendation')
GITIGNORE = 'tests/.test_counter.json\ndocs/api/xml/\n.venv\n'


# region FUNC_layout_declared [DOMAIN(8): NativeMethodology; CONCEPT(8): PackageLayout; TECH(7): json]
## @purpose Give every completeness check one reading of the member paths the real layout declares.
## @uses json.loads, pathlib.Path.read_text
## @io No arguments; reads references/package-layout.json of the real package. Returns list of declared relative path str in file order. Side effects: read only. Errors: OSError or ValueError when the layout is unreadable or malformed. Example: the list contains adapter.json.
## @complexity 2
def layout_declared():
    # START_BLOCK_BusinessLogic
    layout = json.loads((PACKAGE / 'references/package-layout.json').read_text(encoding='utf-8'))
    declared = [row['path'] for row in layout['files']]
    logger.info('[IMP:7][layout_declared][READ] declared=%d', len(declared))
    return declared
    # END_BLOCK_BusinessLogic
# endregion FUNC_layout_declared

# region FUNC_missing_members [DOMAIN(8): NativeMethodology; CONCEPT(8): PackageLayout; TECH(7): pathlib]
## @purpose Report which declared members the real package does not hold yet, so pending concurrent work stays visible.
## @uses test_run_state.layout_declared, pathlib.Path.is_file
## @io No arguments. Returns sorted list of declared relative path str that are not regular files in the real package. Side effects: read only. Errors: as layout_declared. Example: an empty list when the package is complete.
## @complexity 2
def missing_members():
    # START_BLOCK_BusinessLogic
    missing = sorted(path for path in layout_declared() if not (PACKAGE / path).is_file())
    logger.info('[IMP:7][missing_members][RESULT] missing=%d', len(missing))
    return missing
    # END_BLOCK_BusinessLogic
# endregion FUNC_missing_members

# region FUNC_undeclared_members [DOMAIN(8): NativeMethodology; CONCEPT(8): PackageLayout; TECH(7): run_state.inventory]
## @purpose Report real package files the layout does not declare, using the same inventory rules as the helper.
## @uses test_run_state.layout_declared, run_state.inventory, run_state.PACKAGE_GENERATED
## @io root Path defaulting to the real package. Returns sorted list of relative path str present on disk but not declared, generated caches excluded. Side effects: reads every file of the tree. Errors: OSError or ValueError on an unreadable or linked member. Example: a stray notes file in the package root appears in the list.
## @complexity 3
def undeclared_members(root=PACKAGE):
    # START_BLOCK_BusinessLogic
    declared = set(layout_declared())
    actual = {row['path'] for row in run_state.inventory(root, run_state.PACKAGE_GENERATED)['files']}
    extra = sorted(actual - declared)
    logger.info('[IMP:7][undeclared_members][RESULT] undeclared=%d', len(extra))
    return extra
    # END_BLOCK_BusinessLogic
# endregion FUNC_undeclared_members

# region FUNC_placeholder_text [DOMAIN(8): NativeMethodology; CONCEPT(8): PendingMember; TECH(7): pathlib]
## @purpose Choose a small, syntactically harmless body for a pending member by its file type.
## @uses pathlib.PurePosixPath.suffix
## @io relative str declared package path. Returns str: an empty JSON object for json, a comment line for py, js, mjs and ini, plain text otherwise. Side effects: none. Errors: none. Example: hooks/hooks.json yields an empty JSON object text.
## @complexity 2
def placeholder_text(relative):
    # START_BLOCK_BusinessLogic
    suffix = Path(relative).suffix
    note = 'Pending placeholder: this declared member does not exist yet in the real package; fixture copy only.'
    if suffix == '.json':
        return '{}\n'
    if suffix in {'.py', '.ini'}:
        return '# ' + note + '\n'
    if suffix in {'.js', '.mjs'}:
        return '// ' + note + '\n'
    return note + '\n'
    # END_BLOCK_BusinessLogic
# endregion FUNC_placeholder_text

# region FUNC_build_tree [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, PendingMember; TECH(7): shutil, json]
## @purpose Give each test an owned realistic corpus: the actual package copy laid out as implementations/claude beside the adapter-declared neutral files and SPEC_VERSION, a target repository tree and an evidence file.
## @uses shutil.copytree, shutil.copyfile, run_state.inventory, test_run_state.layout_declared, test_run_state.placeholder_text
## @io tmp_path owned Path; pending bool leaves the plan file absent; initial_source bool pre-creates source.py in the target; prohibition optional str written as a host instruction file. Returns tuple of package Path, target Path, plan Path, evidence Path. Creates every declared-but-missing member as a placeholder inside the copy only and logs PENDING_MEMBER for each; drops undeclared files from the copy with a trace; the real package is never written. Errors: OSError when a source file is unavailable. Example: with all members present no PENDING_MEMBER line is logged.
## @complexity 6
def build_tree(tmp_path, pending=False, initial_source=False, prohibition=None):
    logger.info('[IMP:4][build_tree][START] owned copy of the actual package and neutral corpus')
    # START_BLOCK_BusinessLogic
    source = tmp_path / 'source'
    package = source / 'implementations/claude'
    shutil.copytree(PACKAGE, package, ignore=shutil.ignore_patterns('doxygen_output', '__pycache__', '.pytest_cache'))
    declared = layout_declared()
    for relative in sorted(set(undeclared_members(package))):
        (package / relative).unlink()
        logger.info('[IMP:7][fixture][UNDECLARED_MEMBER_DROPPED] path=%s', relative)
    for relative in declared:
        destination = package / relative
        if not destination.is_file():
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(placeholder_text(relative), encoding='utf-8')
            logger.info('[IMP:7][fixture][PENDING_MEMBER] path=%s', relative)
    adapter = json.loads((package / 'adapter.json').read_text(encoding='utf-8'))
    for relative in adapter['files']:
        destination = source / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PACKAGE.parents[1] / relative, destination)
    shutil.copyfile(PACKAGE.parents[1] / 'SPEC_VERSION', source / 'SPEC_VERSION')
    target = tmp_path / 'target'
    target.mkdir()
    (target / 'spec.md').write_text('Approved fixture requirement: actual complete inventory, no integration.\n')
    if initial_source:
        (target / 'source.py').write_text('VALUE = 11\n')
    if prohibition is not None:
        (target / 'AGENTS.md').write_text('# Controlled fixture host instruction\n' + prohibition + '\n')
    (target / 'tests').mkdir()
    (target / 'tests/guide.md').write_text('Fixture coverage evidence is structural, never native role acceptance.\n')
    plan = target / 'plan.md'
    if not pending:
        plan.write_text('Fixture approved plan; source.py and tests/guide.md only.\n')
    evidence = target / '.methodology/evidence.txt'
    evidence.parent.mkdir()
    evidence.write_text('Actual owned test fixture observation; no human consent claimed.\n')
    logger.info('[IMP:9][build_tree][RESULT] owned tree ready package_members=%d', len(declared))
    return package, target, plan, evidence
    # END_BLOCK_BusinessLogic
# endregion FUNC_build_tree

# region FUNC_make_fixture [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture; TECH(7): run_state.initialize]
## @purpose Initialize one owned schema2 run over the copied tree so a test starts from a real bound ledger.
## @uses test_run_state.build_tree, run_state.initialize
## @io tmp_path owned Path; cap object deliberately exercised as a valid or invalid Debug input (default 4); pending, initial_source and prohibition as in build_tree. Returns tuple of state file Path, state dict, evidence Path. Side effects: writes only the owned tree and its ledger. Errors: ValueError or TypeError from the helper for invalid input, OSError for unavailable inputs. Example: cap 0 yields an initialized zero-allowance fixture with debug_spent 0.
## @complexity 4
def make_fixture(tmp_path, cap=4, pending=False, initial_source=False, prohibition=None):
    logger.info('[IMP:4][make_fixture][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    package, target, plan, evidence = build_tree(tmp_path, pending, initial_source, prohibition)
    path, state = run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'fixture', cap, framework=package, adapter=package / 'adapter.json', plan=plan)
    logger.info('[IMP:9][make_fixture][RESULT] fixture initialized')
    return path, state, evidence
    # END_BLOCK_BusinessLogic
# endregion FUNC_make_fixture

# region FUNC_envelope [DOMAIN(8): NativeMethodology; CONCEPT(8): CanonicalReturn; TECH(7): run_state.inventory]
## @purpose Prepare the unmodified current canonical fixture role envelope for the state phase.
## @uses run_state.inventory, test_run_state.PHASE_ROLE
## @io state schema2 dict; evidence owned Path; status str defaulting to SUCCESS. Returns dict with phase, role, status, summary, runId, inputIdentity, candidateIdentity, contractVersion and evidence, using the current real target digest. Side effects: reads the target tree. Errors: ValueError or OSError for an invalid inventory. Example: a QA state yields role qa.
## @complexity 3
def envelope(state, evidence, status='SUCCESS'):
    logger.info('[IMP:4][envelope][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    phase = state['phase']
    result = {'phase': phase, 'role': PHASE_ROLE[phase], 'status': status, 'summary': 'Actual fixture structural observation', 'runId': state['run_id'], 'inputIdentity': state['input_identity'], 'candidateIdentity': run_state.inventory(state['target'])['digest'], 'contractVersion': state['contract_version'], 'evidence': [str(evidence)]}
    logger.info('[IMP:9][envelope][RESULT] current fixture envelope phase=%s', phase)
    return result
    # END_BLOCK_BusinessLogic
# endregion FUNC_envelope

# region FUNC_success [DOMAIN(8): NativeMethodology; CONCEPT(9): CanonicalReturn, PhaseEvidence; TECH(7): run_state]
## @purpose Supply phase-specific structural fixture evidence without claiming real native execution.
## @uses test_run_state.envelope, run_state.inventory, pathlib.Path.write_text
## @io state schema2 dict and owned evidence Path. Returns the record wrapper with kind role, the canonical successful phase fields and, for Code, a scoped sourceChange context. Code writes only the fixture source.py and recomputes the candidate digest. Side effects: the Code phase writes source.py. Errors: OSError or ValueError on fixture access. Example: a QA state yields eight named list rows, never an ordinal mapping.
## @complexity 5
def success(state, evidence):
    logger.info('[IMP:4][success][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    phase = state['phase']
    result = envelope(state, evidence)
    context = {}
    if phase == 'bootstrap':
        files = [{'path': r['path'], 'summary': 'Actual fixture member', 'structure': 'regular source', 'relevance': 'fixture baseline'} for r in state['candidate']['files']]
        result.update(isEmpty=False, classificationHint='BROWNFIELD', fileCount=len(files), files=files, recommendations=['retain source scope'], mapEvidence=[str(evidence)])
    elif phase == 'architect':
        result.update(classification='BROWNFIELD', projectType='CLI', taskType='Implementation', planPath=state['plan']['path'], featureSlices=[{'id': 'fixture', 'description': 'source only', 'files': ['source.py'], 'ui': False}], mayEdit=['source.py', 'tests/guide.md'], doNotTouch=['spec.md'], acceptanceCriteria=[{'id': 'fixture-count', 'text': 'One actual artifact', 'measurable': True, 'threshold': 1}], specDeficiencies=[], specBlocked=False, visualGate={'status': 'NOT_APPLICABLE', 'output': 'fixture has one component', 'componentNodes': 1, 'testsOnly': False, 'reason': 'one component below activation'})
    elif phase == 'code':
        source = Path(state['target']) / 'source.py'
        source.write_text('VALUE = 18\n')
        result['candidateIdentity'] = run_state.inventory(state['target'])['digest']
        result.update(artifacts=[str(source)], testGuidePath=str(Path(state['target']) / 'tests/guide.md'), testSummary='Structural fixture evidence only', deviations=[], measurements=[{'fixture': 'actual member'}], logs=[str(evidence)], doxygen={'command': 'owned fixture map record', 'exitCode': 0, 'output': 'fixture structural record only', 'evidence': [str(evidence)], 'mapPath': str(evidence), 'candidateIdentity': result['candidateIdentity'], 'inputIdentity': state['input_identity']})
        context = {'sourceChange': {'mayEdit': ['source.py'], 'artifacts': [str(source)]}}
    elif phase == 'qa':
        result.update(testSummary='structural fixture scans', scans=[{'id': name, 'status': 'PASS', 'reason': 'fixture structure observed, semantic/native proof separate', 'evidence': [str(evidence)]} for name in NAMES], findings=[], limitations=['helper fixture is not real QA'])
    elif phase == 'review':
        result.update(findings=[], limitations=['helper fixture is not independent Review'], diffEvidence=[str(evidence)], scopeJudgment='fixture scoped contents')
    elif phase == 'finalize':
        result.update(report=str(evidence), classification='BROWNFIELD', planPath=state['plan']['path'], testsPath=str(Path(state['target']) / 'tests/guide.md'), logPath=str(evidence), doxygenPath=str(evidence), testSummary='helper fixture only', acceptanceEvidence=[str(evidence)], qaEvidence=[str(evidence)], reviewEvidence=[str(evidence)], liveEvidence=[str(evidence)], blastRadius={'added': ['source.py'], 'modified': [], 'deleted': [], 'untracked': ['source.py']}, scopeDeviations=[], limitations=['not native completion'])
    logger.info('[IMP:9][success][RESULT] fixture phase payload prepared')
    return {'kind': 'role', 'result': result, **({'context': context} if context else {})}
    # END_BLOCK_BusinessLogic
# endregion FUNC_success

# region FUNC_to_phase [DOMAIN(8): NativeMethodology; CONCEPT(8): PhaseRoute; TECH(7): run_state.advance]
## @purpose Reach an explicitly requested phase in the structural fixture by the normal successful route.
## @uses run_state.advance, test_run_state.success
## @io state schema2 fixture dict, evidence owned Path, phase known canonical phase str. Returns the new state after normal transitions; Code through success writes the fixture source.py. Errors: ValueError or OSError from a real helper refusal; an unreachable phase would loop, so tests pass only phases on the normal route. Example: to_phase of a fresh state to qa returns a QA state with no charged repair.
## @complexity 4
def to_phase(state, evidence, phase):
    logger.info('[IMP:4][to_phase][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    while state['phase'] != phase:
        state = run_state.advance(state, success(state, evidence))
    logger.info('[IMP:9][to_phase][RESULT] desired fixture phase=%s', phase)
    return state
    # END_BLOCK_BusinessLogic
# endregion FUNC_to_phase

# region FUNC_error_profile [DOMAIN(9): NativeMethodology; CONCEPT(10): ExpectedErrorOracle; TECH(7): logging]
## @purpose Declare one exact ordered refusal episode independently of captured records.
## @uses logging.ERROR
## @io cause literal str or None, propagation ordered owning function names, kind literal exception class name defaulting to ValueError. Returns immutable ordered tuple of triples logger name, level and message; cause None represents a direct input and output exception without an _expect rejection. Reads no logs and no producer registry; no writes. Example: error_profile of invalid Debug cap through _plain_integer and initialize declares exactly three events.
## @complexity 2
def error_profile(cause, *propagation, kind='ValueError'):
    logger.info('[IMP:4][error_profile][START] declare exact refusal episode')
    # START_BLOCK_BusinessLogic
    head = () if cause is None else (('run_state', logging.ERROR, '[IMP:10][_expect][REJECT] invariant=' + cause),)
    profile = head + tuple(('run_state', logging.ERROR, '[IMP:10][' + owner + '][FAIL] kind=' + kind) for owner in propagation)
    logger.info('[IMP:9][error_profile][RESULT] declared events=%d', len(profile))
    return profile
    # END_BLOCK_BusinessLogic
# endregion FUNC_error_profile

# region FUNC_print_trace [DOMAIN(8): NativeMethodology; CONCEPT(10): SemanticTrace; TECH(7): pytest caplog]
## @purpose Show the actual filtered IMP 7 to 10 records and every error before any assertion, so the documented visible runner (pytest -s) exposes the trace (TST-301) even when the test then fails.
## @uses pytest.LogCaptureFixture.records, builtins.print
## @io caplog LogCaptureFixture. Returns the list of the records captured so far after printing each record of importance 7 to 10, or of level error or above, as logger name, level name and message. Side effects: prints only, no logging, no source or state change. Errors: none. Example: after a helper call that logged an IMP 9 RESULT, the line with that RESULT is printed.
## @complexity 2
def print_trace(caplog):
    # START_BLOCK_BusinessLogic
    records = list(caplog.records)
    for record in records:
        if record.levelno >= logging.ERROR or any('[IMP:' + str(i) + ']' in record.getMessage() for i in range(7, 11)):
            print(record.name, record.levelname, record.getMessage())
    return records
    # END_BLOCK_BusinessLogic
# endregion FUNC_print_trace

# region FUNC_expose [DOMAIN(8): NativeMethodology; CONCEPT(10): ExpectedErrorOracle, SemanticTrace; TECH(7): pytest caplog]
## @purpose Print the actual IMP 7 to 10 trace and every error, then reject any ERROR or CRITICAL outside the caller exact ordered profile.
## @uses test_run_state.print_trace, logging.Logger.info
## @io caplog LogCaptureFixture; owner logical function str; failure bool defaulting to False; expected_errors predeclared immutable tuple defaulting to empty. Returns None after the complete ERROR and CRITICAL population equals the profile on logger, numeric level and full message, order and cardinality exact. A failure case needs a nonempty profile and an owning IMP 10 record; a success case needs an empty profile and an owning IMP 9 record. A mismatch emits one IMP 10 REJECT with safe counts and raises AssertionError. Side effects: prints records, no source or state change. Example: a schema refusal declares the exact cascade of _expect, _state_shape, validate_state and advance.
## @complexity 5
def expose(caplog, owner, failure=False, *, expected_errors=()):
    logger.info('[IMP:4][expose][START] expected-only complete error population')
    # START_BLOCK_BusinessLogic
    records = print_trace(caplog)
    actual = tuple((r.name, r.levelno, r.getMessage()) for r in records if r.levelno >= logging.ERROR)
    if actual != expected_errors:
        logger.error('[IMP:10][expose][REJECT] expected_events=%d actual_events=%d', len(expected_errors), len(actual))
        raise AssertionError('unexpected or missing ordered error profile')
    if failure:
        assert expected_errors
        assert any('[IMP:10][' + owner + ']' in r.getMessage() for r in records)
    else:
        assert not expected_errors
        assert any('[IMP:9][' + owner + ']' in r.getMessage() for r in records)
    logger.info('[IMP:9][expose][RESULT] exact expected error population=%d', len(actual))
    # END_BLOCK_BusinessLogic
# endregion FUNC_expose

# region FUNC_cli [DOMAIN(8): NativeMethodology; CONCEPT(9): RealChannel; TECH(7): subprocess]
## @purpose Observe the actual shipped state helper through a real process: argv, stdout, stderr and exit code.
## @uses subprocess.run, sys.executable, os.environ
## @io args CLI values converted to str; cwd keyword-only owned directory Path. Returns the CompletedProcess with real argv, returncode, stdout and stderr. Launches only the real package helper over supplied owned fixtures; PYTHONDONTWRITEBYTECODE keeps source caches out of the package. Prints the complete real channels. Errors: OSError when the interpreter cannot start. Example: show on a valid ledger returns exit 0 and a JSON object on stdout.
## @complexity 3
def cli(*args, cwd):
    logger.info('[IMP:4][cli][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    proc = subprocess.run([sys.executable, str(PACKAGE / 'skills/feature-dev/scripts/run_state.py'), *map(str, args)], cwd=cwd, env=environment, text=True, capture_output=True)
    print('Actual helper invocation:', proc.args, 'exit', proc.returncode)
    print('stdout:', proc.stdout)
    print('stderr:', proc.stderr)
    logger.info('[IMP:9][cli][RESULT] exit=%d', proc.returncode)
    return proc
    # END_BLOCK_BusinessLogic
# endregion FUNC_cli

# region FUNC_edit_json [DOMAIN(8): NativeMethodology; CONCEPT(8): FixtureDamage; TECH(7): json]
## @purpose Apply one deliberate change to a JSON file inside the owned copy so a test can damage the layout or adapter.
## @uses json.loads, json.dumps, pathlib.Path.write_text
## @io path Path of a JSON file in the owned copy; change callable taking the parsed object and mutating it in place. Returns the mutated object. Side effects: rewrites that one file with indented UTF-8 JSON. Errors: OSError or ValueError for an unreadable file. Example: edit_json of the layout with a lambda that renames the package.
## @complexity 2
def edit_json(path, change):
    # START_BLOCK_BusinessLogic
    value = json.loads(Path(path).read_text(encoding='utf-8'))
    change(value)
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    logger.info('[IMP:7][edit_json][WRITE] owned copy damaged on purpose')
    return value
    # END_BLOCK_BusinessLogic
# endregion FUNC_edit_json

# region FUNC_test_real_package_complete [DOMAIN(9): NativeMethodology; CONCEPT(10): PackageCompleteness, SemanticTrace; TECH(7): run_state._bindings]
## @purpose Prove the real package holds exactly the members its layout declares and that the helper binds the real package, so no placeholder-backed test can hide an incomplete delivery, and show the actual IMP 7 to 10 trace before the first assertion.
## @uses test_run_state.missing_members, test_run_state.undeclared_members, test_run_state.print_trace, run_state._bindings
## @io Input: caplog LogCaptureFixture. Output: None after printing the actual trace and then asserting zero declared members missing from the real package, zero undeclared files, and that binding the real package against the real neutral tree yields one package row per declared member and 71 neutral rows. Side effects: reads the real package and neutral files, writes nothing; the trace is printed in a finally block so a failing or raising observation still shows it. Errors: AssertionError listing the missing and undeclared paths; this test is expected to fail while other package members are still being written and to pass at integration. Example: a complete package reports empty lists.
## @complexity 4
def test_real_package_complete(caplog):
    logger.info('[IMP:4][test_real_package_complete][START] judge the real package, not a copy')
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: Review and QA round 3 (TST-301) found that this test printed only its own lists and no IMP 7 to 10 record before asserting under pytest -s.
    # Previous: asserts first, trace never printed. Fix: observe inside try, print the filtered trace in finally, assert afterwards.
    caplog.set_level(logging.INFO)
    bindings = None
    try:
        missing, extra = missing_members(), undeclared_members()
        print('Actual missing declared members:', missing)
        print('Actual undeclared files:', extra)
        logger.info('[IMP:9][test_real_package_complete][MEMBERS] missing=%d undeclared=%d', len(missing), len(extra))
        if not missing and not extra:
            bindings = run_state._bindings(PACKAGE, PACKAGE / 'adapter.json', PACKAGE.parents[1] / 'SPEC_VERSION')
            print('Actual real binding: package rows', len(bindings['package']['files']), 'neutral rows', len(bindings['neutral']))
            logger.info('[IMP:9][test_real_package_complete][BINDING] package=%d neutral=%d', len(bindings['package']['files']), len(bindings['neutral']))
    finally:
        print_trace(caplog)
    assert missing == [] and extra == [], ('missing', missing, 'undeclared', extra)
    assert len(bindings['package']['files']) == len(layout_declared()) and len(bindings['neutral']) == 71
    logger.info('[IMP:9][test_real_package_complete][RESULT] real package complete and bound')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_package_complete

# region FUNC_test_real_package_complete_exposes_trace_before_asserting [DOMAIN(9): NativeMethodology; CONCEPT(10): SemanticTrace, VisibleRunner; TECH(7): subprocess, pytest]
## @purpose Verify through the documented visible runner (pytest -s -v) that the real-package completeness test prints actual IMP 7 to 10 records before its outcome, so TST-301 holds for it and cannot regress to a bare assertion.
## @uses subprocess.run, sys.executable, os.environ, re.search, test_run_state.print_trace
## @io No fixture arguments. Output: None after running only test_real_package_complete in a child pytest with -s and -v from the package directory, then asserting that the child output holds the MEMBERS IMP 9 record and the layout IMP 7 record of that test before its PASSED or FAILED outcome word. The outcome itself is not judged here, so concurrent package work cannot fail this check. Side effects: one child pytest process; PYTHONDONTWRITEBYTECODE keeps caches out of the package. Errors: AssertionError, or OSError when the interpreter cannot start. Example: before the repair the child printed only the two member lists and no IMP record.
## @complexity 4
def test_real_package_complete_exposes_trace_before_asserting():
    logger.info('[IMP:4][test_real_package_complete_exposes_trace_before_asserting][START] visible runner probe')
    # START_BLOCK_BusinessLogic
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    proc = subprocess.run([sys.executable, '-m', 'pytest', '-c', 'pytest.ini', 'tests/test_run_state.py::test_real_package_complete', '-s', '-v', '-p', 'no:cacheprovider'], cwd=PACKAGE, env=environment, text=True, capture_output=True)
    outcome = re.search(r'\b(PASSED|FAILED)\b', proc.stdout)
    before = proc.stdout[:outcome.start()] if outcome else proc.stdout
    imp_lines = re.findall(r'\[IMP:(?:7|8|9|10)\]\[[^\]]+\]\[[^\]]+\]', before)
    print('Actual child runner:', proc.args, 'exit', proc.returncode, 'outcome', outcome.group(1) if outcome else None)
    print('Actual IMP 7 to 10 records before the outcome:', imp_lines)
    logger.info('[IMP:9][test_real_package_complete_exposes_trace_before_asserting][TRACE] child records before outcome=%d', len(imp_lines))
    assert outcome is not None, proc.stdout[-2000:]
    assert '[IMP:9][test_real_package_complete][MEMBERS]' in imp_lines and '[IMP:7][layout_declared][READ]' in imp_lines
    logger.info('[IMP:9][test_real_package_complete_exposes_trace_before_asserting][RESULT] trace precedes the outcome')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_package_complete_exposes_trace_before_asserting

# region FUNC_test_identity_and_schema_refusals [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): pytest]
## @purpose Verify that an old schema and a drifted package input are refused without mutating the state, and that the checkpoint round-trips.
## @uses run_state.advance, run_state.validate_state, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting that a schema 1 copy is refused with a historical message and left unchanged, that a changed package README is refused as an immutable input change, that restoring it validates again, and that the saved file equals the indented JSON of the state. Side effects: temporary edits to the README inside the owned copy, restored byte for byte. Errors: AssertionError; the exact four plus two event error population is declared first. Example: schema_version 1 raises ValueError mentioning historical.
## @complexity 5
def test_identity_and_schema_refusals(tmp_path, caplog):
    logger.info('[IMP:4][test_identity_and_schema_refusals][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('unsupported state schema; historical records are read-only', '_state_shape', 'validate_state', 'advance') + error_profile('immutable input identity changed', 'validate_state')
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path)
    stale = copy.deepcopy(state)
    stale['schema_version'] = 1
    before = copy.deepcopy(stale)
    with pytest.raises(ValueError, match='historical'):
        run_state.advance(stale, success(state, evidence))
    readme = Path(state['framework']) / 'README.md'
    old = readme.read_bytes()
    readme.write_bytes(old + b'changed\n')
    with pytest.raises(ValueError, match='immutable'):
        run_state.validate_state(state)
    readme.write_bytes(old)
    restored = run_state.validate_state(state)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    assert stale == before
    assert restored == state['candidate']
    assert path.read_text() == json.dumps(state, indent=2, ensure_ascii=False) + '\n'
    logger.info('[IMP:9][test_identity_and_schema_refusals][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_identity_and_schema_refusals

# region FUNC_test_package_binding_identity_and_layout_refusals [DOMAIN(9): NativeMethodology; CONCEPT(10): PackageIdentity, LayoutRefusal; TECH(7): pytest, json]
## @purpose Verify that initialization refuses, before any state exists, every layout or tree that does not match the methodology-claude 1.0.0 colocated-in-place identity: package name, version, profile, layout keys, agents role locations, member kinds, ordering, duplicates and membership in both directions.
## @uses pytest.mark.parametrize, run_state.initialize, test_run_state.build_tree, test_run_state.edit_json, test_run_state.expose, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, damage str from package-name, package-version, profile, layout-key, roles, kind, unsorted, duplicate, missing-member, extra-member. Output: None after asserting that initialization raises ValueError with the owning invariant, that no run directory exists, and that the exact ordered error population is the invariant followed by the _bindings and initialize failures. Side effects: damages only the owned copy of the layout or tree. Errors: AssertionError. Example: renaming the layout package to methodology-codex is refused with package identity mismatch; a removed member or a stray file is refused with the label naming that exact relative path.
## @complexity 6
@pytest.mark.parametrize('damage', ['package-name', 'package-version', 'profile', 'layout-key', 'roles', 'kind', 'unsorted', 'duplicate', 'missing-member', 'extra-member'])
def test_package_binding_identity_and_layout_refusals(tmp_path, caplog, damage):
    logger.info('[IMP:4][test_package_binding_identity_and_layout_refusals][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    example = next(path for path in layout_declared() if path.startswith('examples/'))
    labels = {'package-name': 'package identity mismatch', 'package-version': 'package identity mismatch', 'profile': 'unsupported package profile', 'layout-key': 'unsupported package profile', 'roles': 'package role locations mismatch', 'kind': 'invalid package member declarations', 'unsorted': 'invalid package member declarations', 'duplicate': 'invalid package member declarations', 'missing-member': 'package membership mismatch: missing ' + example, 'extra-member': 'package membership mismatch: undeclared stray.txt'}
    expected_errors = error_profile(labels[damage], '_bindings', 'initialize')
    caplog.set_level(logging.INFO)
    package, target, plan, _ = build_tree(tmp_path)
    layout_path = package / 'references/package-layout.json'
    if damage == 'package-name':
        edit_json(layout_path, lambda layout: layout.update(package='methodology-codex'))
    elif damage == 'package-version':
        edit_json(layout_path, lambda layout: layout.update(version='9.0.0'))
    elif damage == 'profile':
        edit_json(layout_path, lambda layout: layout.update(profile='colocated-explicit-source'))
    elif damage == 'layout-key':
        edit_json(layout_path, lambda layout: layout.update(extra=True))
    elif damage == 'roles':
        edit_json(layout_path, lambda layout: layout['roles'].update(qa='roles/qa.md'))
    elif damage == 'kind':
        edit_json(layout_path, lambda layout: layout['files'][0].update(kind='banana'))
    elif damage == 'unsorted':
        edit_json(layout_path, lambda layout: layout['files'].reverse())
    elif damage == 'duplicate':
        edit_json(layout_path, lambda layout: layout['files'].append(dict(layout['files'][-1])))
    elif damage == 'missing-member':
        (package / example).unlink()
    else:
        (package / 'stray.txt').write_text('undeclared member\n')
    with pytest.raises(ValueError, match=re.escape(labels[damage])):
        run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'damaged', 4, framework=package, adapter=package / 'adapter.json', plan=plan)
    expose(caplog, 'initialize', True, expected_errors=expected_errors)
    assert not (target / '.methodology/runs/damaged').exists()
    logger.info('[IMP:9][test_package_binding_identity_and_layout_refusals][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_package_binding_identity_and_layout_refusals

# region FUNC_test_layout_driven_count_and_identity [DOMAIN(9): NativeMethodology; CONCEPT(10): PackageIdentity, LayoutDrivenCount; TECH(7): pytest, json]
## @purpose Verify the positive side of the binding: the run contract is methodology-claude/1.0.0 at schema 2, hook-config and workflow member kinds are accepted, and the package member count follows the declared layout instead of a literal.
## @uses run_state.initialize, test_run_state.build_tree, test_run_state.edit_json, test_run_state.expose
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. The test removes one declared example member from both the layout and the owned tree, then initializes. Output: None after asserting the contract version, schema 2, a package row count equal to the shortened layout, the dropped member absent from the rows, the layout containing hook-config and workflow kinds, 71 neutral rows, neutral version 2.0.0, and the six core names. Side effects: owned copy only. Errors: AssertionError. Example: a layout shorter by one member binds with one row fewer and no error record.
## @complexity 5
def test_layout_driven_count_and_identity(tmp_path, caplog):
    logger.info('[IMP:4][test_layout_driven_count_and_identity][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    package, target, plan, _ = build_tree(tmp_path)
    layout_path = package / 'references/package-layout.json'
    dropped = next(p for p in layout_declared() if p.startswith('examples/'))
    layout = edit_json(layout_path, lambda value: value.update(files=[row for row in value['files'] if row['path'] != dropped]))
    (package / dropped).unlink()
    path, state = run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'counted', 4, framework=package, adapter=package / 'adapter.json', plan=plan)
    rows = state['bindings']['package']['files']
    kinds = {row['kind'] for row in layout['files']}
    print('Actual bound package rows:', len(rows), 'declared:', len(layout['files']), 'kinds:', sorted(kinds))
    expose(caplog, 'initialize')
    assert state['schema_version'] == 2 and state['contract_version'] == 'methodology-claude/1.0.0'
    assert len(rows) == len(layout['files']) and dropped not in {row['path'] for row in rows}
    assert {'hook-config', 'workflow'} <= kinds
    assert len(state['bindings']['neutral']) == 71 and state['bindings']['neutral_version'] == '3.2.0'
    assert state['bindings']['core'] == list(run_state.CORE) and path.is_file()
    logger.info('[IMP:9][test_layout_driven_count_and_identity][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_layout_driven_count_and_identity

# region FUNC_test_ambient_ds_store_in_package_does_not_break_binding [DOMAIN(9): NativeMethodology; CONCEPT(10): PackageMembership, AmbientFile; TECH(7): pytest, subprocess]
## @purpose Verify that the ambient macOS .DS_Store file, ignored by the repository and never published, is not a package member: it neither breaks init when present beforehand nor breaks show and record when it appears during the run, at the package root and in subdirectories.
## @uses run_state.initialize, test_run_state.build_tree, test_run_state.cli, test_run_state.expose, test_run_state.layout_declared, test_run_state.success
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting that initialization binds a copy holding three .DS_Store files, that the package rows equal the declared layout exactly with no .DS_Store among them and .DS_Store among the recorded exclusions, and that after one more .DS_Store appears the real show and record commands exit 0 and the saved phase is architect. Side effects: owned copy and ledger, two child processes. Errors: AssertionError. Example: before the repair init failed with a pathless package membership mismatch.
## @complexity 5
def test_ambient_ds_store_in_package_does_not_break_binding(tmp_path, caplog):
    logger.info('[IMP:4][test_ambient_ds_store_in_package_does_not_break_binding][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    package, target, plan, evidence = build_tree(tmp_path)
    for relative in ('.DS_Store', 'skills/.DS_Store', 'references/.DS_Store'):
        (package / relative).write_bytes(b'\x00\x00\x00\x01Bud1 ambient Finder metadata, fixture bytes\n')
    path, state = run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'ds-store', 4, framework=package, adapter=package / 'adapter.json', plan=plan)
    (package / 'agents/.DS_Store').write_bytes(b'late ambient Finder metadata, fixture bytes\n')
    shown = cli('show', '--state', path, cwd=tmp_path)
    result_path = tmp_path / 'bootstrap-result.json'
    result_path.write_text(json.dumps(success(state, evidence)))
    recorded = cli('record', '--state', path, '--result', result_path, cwd=tmp_path)
    saved = json.loads(path.read_text())
    expose(caplog, 'initialize')
    rows = {row['path'] for row in state['bindings']['package']['files']}
    assert rows == set(layout_declared()) and not any(row.endswith('.DS_Store') for row in rows)
    assert '.DS_Store' in state['bindings']['package']['exclusions']
    assert shown.returncode == 0 and recorded.returncode == 0 and saved['phase'] == 'architect'
    logger.info('[IMP:9][test_ambient_ds_store_in_package_does_not_break_binding][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_ambient_ds_store_in_package_does_not_break_binding

# region FUNC_test_membership_refusal_names_offending_paths [DOMAIN(9): NativeMethodology; CONCEPT(10): PackageMembership, Diagnostic; TECH(7): pytest]
## @purpose Verify that a real undeclared or missing package member still refuses initialization, now with a diagnostic that names the offending relative paths (at most three of each kind, then the count of the rest), and that an ambient .DS_Store beside the offender is neither the cause nor named.
## @uses pytest.mark.parametrize, pytest.raises, run_state.initialize, test_run_state.build_tree, test_run_state.error_profile, test_run_state.expose, test_run_state.layout_declared
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, case one-undeclared, five-undeclared, four-missing or both. Output: None after planting a .DS_Store and the case damage in the owned copy, then asserting a ValueError whose message equals the literal label (for example package membership mismatch: undeclared stray.txt, or three sorted paths followed by and 2 more), the exact three-event error population of the invariant, _bindings and initialize, no run directory, and no .DS_Store in the message. Side effects: owned copy only. Errors: AssertionError. Example: five stray files name the first three sorted paths and and 2 more.
## @complexity 5
@pytest.mark.parametrize('case', ['one-undeclared', 'five-undeclared', 'four-missing', 'both'])
def test_membership_refusal_names_offending_paths(tmp_path, caplog, case):
    logger.info('[IMP:4][test_membership_refusal_names_offending_paths][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    literal = {
        'one-undeclared': 'package membership mismatch: undeclared stray.txt',
        'five-undeclared': 'package membership mismatch: undeclared extra/e1.txt, extra/e2.txt, extra/e3.txt and 2 more',
        'four-missing': 'package membership mismatch: missing agents/architect.md, agents/coder.md, agents/debugger.md and 1 more',
        'both': 'package membership mismatch: missing agents/architect.md; undeclared stray.txt',
    }[case]
    expected_errors = error_profile(literal, '_bindings', 'initialize')
    caplog.set_level(logging.INFO)
    package, target, plan, _ = build_tree(tmp_path)
    declared = layout_declared()
    assert all(name in declared for name in ('agents/architect.md', 'agents/coder.md', 'agents/debugger.md', 'agents/qa.md'))
    (package / '.DS_Store').write_bytes(b'ambient Finder metadata beside the offender\n')
    if case in {'one-undeclared', 'both'}:
        (package / 'stray.txt').write_text('undeclared member\n')
    if case == 'five-undeclared':
        (package / 'extra').mkdir()
        for number in range(1, 6):
            (package / 'extra' / ('e%d.txt' % number)).write_text('undeclared member\n')
    removed = {'four-missing': ['agents/architect.md', 'agents/coder.md', 'agents/debugger.md', 'agents/qa.md'], 'both': ['agents/architect.md']}.get(case, [])
    for relative in removed:
        (package / relative).unlink()
    with pytest.raises(ValueError, match=re.escape(literal)) as refused:
        run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'membership', 4, framework=package, adapter=package / 'adapter.json', plan=plan)
    expose(caplog, 'initialize', True, expected_errors=expected_errors)
    assert str(refused.value) == literal and '.DS_Store' not in str(refused.value)
    assert not (target / '.methodology/runs/membership').exists()
    logger.info('[IMP:9][test_membership_refusal_names_offending_paths][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_membership_refusal_names_offending_paths

# region FUNC_test_adapter_debug_allowance [DOMAIN(9): NativeMethodology; CONCEPT(10): DebugAllowance; TECH(7): pytest, json]
## @purpose Verify the adapter side of the Debug allowance: an extension above four is BLOCKED, an ambiguous textual spelling is refused, a lowered allowance below the request is refused, and a lowered allowance that is honored caps the run.
## @uses pytest.mark.parametrize, run_state.initialize, test_run_state.build_tree, test_run_state.edit_json, test_run_state.expose, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, adapter_cap str from the parametrized adapter values 5, 04, 2 and the honored case 2 with a request of 2. Output: None after asserting the refusal text and exact error profile for the three refusals, and for the honored case a run with debug_cap 2, debug_spent 0 and a bound profile cap of 2. Side effects: edits only the owned copy of adapter.json. Errors: AssertionError. Example: an adapter value of 5 raises BLOCKED adapter Debug extension unsupported.
## @complexity 5
@pytest.mark.parametrize('adapter_cap,request_cap,outcome', [('5', 4, 'extension'), ('04', 4, 'spelling'), ('2', 4, 'lowered'), ('2', 2, 'honored')])
def test_adapter_debug_allowance(tmp_path, caplog, adapter_cap, request_cap, outcome):
    logger.info('[IMP:4][test_adapter_debug_allowance][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    refusals = {'extension': ('BLOCKED: adapter Debug extension unsupported', error_profile('BLOCKED: adapter Debug extension unsupported', '_bindings', 'initialize')),
                'spelling': ('Debug text requires canonical unsigned decimal spelling', error_profile('Debug text requires canonical unsigned decimal spelling', '_decimal_cap', '_bindings', 'initialize')),
                'lowered': ('requested Debug cap exceeds declared adapter allowance', error_profile('requested Debug cap exceeds declared adapter allowance', 'initialize'))}
    caplog.set_level(logging.INFO)
    package, target, plan, _ = build_tree(tmp_path)
    edit_json(package / 'adapter.json', lambda adapter: adapter['parameters'].update({'debug-entry-cap': adapter_cap}))
    arguments = (target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'adapter-cap', request_cap)
    if outcome == 'honored':
        path, state = run_state.initialize(*arguments, framework=package, adapter=package / 'adapter.json', plan=plan)
        expose(caplog, 'initialize')
        assert state['debug_cap'] == 2 and state['debug_spent'] == 0 and state['bindings']['debug_cap_profile'] == 2
    else:
        label, expected_errors = refusals[outcome]
        with pytest.raises(ValueError, match=re.escape(label)):
            run_state.initialize(*arguments, framework=package, adapter=package / 'adapter.json', plan=plan)
        expose(caplog, 'initialize', True, expected_errors=expected_errors)
        assert not (target / '.methodology/runs/adapter-cap').exists()
    logger.info('[IMP:9][test_adapter_debug_allowance][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_adapter_debug_allowance

# region FUNC_test_debug_invalid_type_refusal [DOMAIN(8): NativeMethodology; CONCEPT(9): DebugAllowance; TECH(7): pytest]
## @purpose Verify that a boolean, negative, fractional, text or above-four Debug cap is refused at initialization without creating a ledger.
## @uses pytest.mark.parametrize, pytest.raises, test_run_state.expose, test_run_state.make_fixture, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, cap from the parametrized values True, False, -1, 1.5, the text 4 and 5. Output: None after asserting ValueError or TypeError, no state file under the target, and the exact error profile: the above-four BLOCKED rejection for 5, otherwise the invalid Debug cap rejection through _plain_integer and initialize. Side effects: owned fixture only. Errors: AssertionError. Example: cap True is refused because a boolean is not a plain integer.
## @complexity 4
@pytest.mark.parametrize('cap', [True, False, -1, 1.5, '4', 5])
def test_debug_invalid_type_refusal(tmp_path, caplog, cap):
    logger.info('[IMP:4][test_debug_invalid_type_refusal][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = (error_profile('BLOCKED: above-default Debug extensions unsupported', 'initialize') if type(cap) is int and cap > 4 else error_profile('invalid Debug cap', '_plain_integer', 'initialize'))
    caplog.set_level(logging.INFO)
    with pytest.raises((ValueError, TypeError)):
        make_fixture(tmp_path, cap)
    expose(caplog, 'initialize', True, expected_errors=expected_errors)
    assert not list((tmp_path / 'target/.methodology/runs').glob('*/state.json'))
    logger.info('[IMP:9][test_debug_invalid_type_refusal][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_debug_invalid_type_refusal

# region FUNC_test_debug_budget_and_causal_routes [DOMAIN(8): NativeMethodology; CONCEPT(10): CausalDebug, CumulativeSpend; TECH(7): pytest]
## @purpose Verify that a Code, QA or Review defect charges exactly one Debug entry before entering Debug, that a fix invalidates the QA verdict, and that the next defect at the cap escalates with no further spend.
## @uses pytest.mark.parametrize, run_state.advance, run_state.save, run_state.validate_state, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, origin from code, qa, review with a cap of 1. Output: None after asserting debug_spent moves 0 to 1 with phase debug, debug_delta 1 and the recorded origin; the saved state validates; a scoped FIXED return moves to qa with qa not accepted and spend still 1; a renewed QA moves to review; a second defect ends ESCALATED with spend 1 and debug_delta 0. Side effects: fixture source.py edits and one ledger save. Errors: AssertionError. Example: a Review defect with cap 1 spends the entry once and the next defect escalates.
## @complexity 6
@pytest.mark.parametrize('origin', ['code', 'qa', 'review'])
def test_debug_budget_and_causal_routes(tmp_path, caplog, origin):
    logger.info('[IMP:4][test_debug_budget_and_causal_routes][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path, cap=1)
    state = to_phase(state, evidence, origin)
    result = envelope(state, evidence, 'BUG_REPORT')
    result['bugReport'] = {key: 'Fixture observed cause and actionable local correction' for key in BUG_FIELDS}
    if origin == 'qa':
        q = success(state, evidence)['result']
        q['status'] = 'BUG_REPORT'
        q['bugReport'] = result['bugReport']
        q['scans'][0]['status'] = 'FAIL'
        result = q
    original = copy.deepcopy(state)
    state = run_state.advance(state, {'kind': 'role', 'result': result})
    entered = copy.deepcopy(state)
    run_state.save(path, state)
    validated = run_state.validate_state(state)
    source = Path(state['target']) / 'source.py'
    source.write_text('VALUE = 23\n')
    fixed = envelope(state, evidence, 'FIXED')
    fixed.update(rootCause='fixture cause', fix='correct actual value', filesTouched=[str(source)], postFixAudit='actual scope comparison', testSummary='fixture only', regressionEvidence=[str(evidence)], origin=origin)
    state = run_state.advance(state, {'kind': 'role', 'result': fixed, 'context': {'sourceChange': {'mayEdit': ['source.py'], 'artifacts': [str(source)]}}})
    after_fix = copy.deepcopy(state)
    state = run_state.advance(state, success(state, evidence))
    after_qa = copy.deepcopy(state)
    next_bug = envelope(state, evidence, 'BUG_REPORT')
    next_bug['bugReport'] = result['bugReport']
    state = run_state.advance(state, {'kind': 'role', 'result': next_bug})
    expose(caplog, 'advance')
    assert original['debug_spent'] == 0 and entered['debug_spent'] == 1 and entered['phase'] == 'debug'
    assert entered['history'][-1]['debug_delta'] == 1 and entered['debug_origin']['phase'] == origin
    assert validated == entered['candidate']
    assert after_fix['phase'] == 'qa' and after_fix['debug_spent'] == 1 and 'qa' not in after_fix['accepted']
    assert after_qa['phase'] == 'review' and after_qa['debug_spent'] == 1
    assert state['status'] == 'ESCALATED' and state['debug_spent'] == 1 and state['history'][-1]['debug_delta'] == 0
    logger.info('[IMP:9][test_debug_budget_and_causal_routes][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_debug_budget_and_causal_routes

# region FUNC_test_zero_allowance_and_green_route [DOMAIN(8): NativeMethodology; CONCEPT(9): ZeroAllowance, PhaseOrder; TECH(7): pytest]
## @purpose Verify that a run with a zero Debug allowance walks the whole normal route Bootstrap, Architect, Code, QA, Review, Finalize to SUCCESS with no Debug spend.
## @uses run_state.advance, test_run_state.expose, test_run_state.make_fixture, test_run_state.success
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting the final status SUCCESS, debug_spent 0 and the exact phase order of the history after initialization, which proves Review precedes Finalize. Side effects: owned fixture and fixture source.py. Errors: AssertionError. Example: the history phases read bootstrap, architect, code, qa, review, finalize.
## @complexity 4
def test_zero_allowance_and_green_route(tmp_path, caplog):
    logger.info('[IMP:4][test_zero_allowance_and_green_route][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path, cap=0)
    while state['status'] == 'RUNNING':
        state = run_state.advance(state, success(state, evidence))
    expose(caplog, 'advance')
    assert state['status'] == 'SUCCESS' and state['debug_spent'] == 0
    assert [e['phase'] for e in state['history'][1:]] == ['bootstrap', 'architect', 'code', 'qa', 'review', 'finalize']
    logger.info('[IMP:9][test_zero_allowance_and_green_route][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_zero_allowance_and_green_route

# region FUNC_test_named_scan_verdicts [DOMAIN(8): NativeMethodology; CONCEPT(10): EightNamedScans; TECH(7): pytest]
## @purpose Verify that a QA return is accepted only with exactly the eight named scans as a list of rows, each with a passing status, a reason and evidence.
## @uses pytest.mark.parametrize, pytest.raises, run_state.advance, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, damage from missing, extra, ordinal, duplicate, FAIL, BLOCKED, no-evidence, empty-reason, dict. Output: None after asserting that every damaged QA return raises ValueError or TypeError with its exact declared error cascade and leaves the input state equal to its deep copy. Side effects: owned fixture only. Errors: AssertionError. Example: renaming the first scan id to 1 is refused with scan identity population mismatch.
## @complexity 5
@pytest.mark.parametrize('damage', ['missing', 'extra', 'ordinal', 'duplicate', 'FAIL', 'BLOCKED', 'no-evidence', 'empty-reason', 'dict'])
def test_named_scan_verdicts(tmp_path, caplog, damage):
    logger.info('[IMP:4][test_named_scan_verdicts][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    profiles = {
        'missing': error_profile('eight named scan rows required', '_payload', 'advance'),
        'extra': error_profile('eight named scan rows required', '_payload', 'advance'),
        'ordinal': error_profile('scan identity population mismatch', '_payload', 'advance'),
        'duplicate': error_profile('scan identity population mismatch', '_payload', 'advance'),
        'FAIL': error_profile('QA cannot pass failed/blocked scan', '_payload', 'advance'),
        'BLOCKED': error_profile('QA cannot pass failed/blocked scan', '_payload', 'advance'),
        'no-evidence': error_profile('nonempty evidence list required', '_evidence', '_payload', 'advance'),
        'empty-reason': error_profile('scan reason missing', '_text', '_payload', 'advance'),
        'dict': error_profile('missing or invalid scans', '_typed_fields', '_payload', 'advance')}
    expected_errors = profiles[damage]
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    state = to_phase(state, evidence, 'qa')
    request = success(state, evidence)
    rows = request['result']['scans']
    if damage == 'missing':
        rows.pop()
    elif damage == 'extra':
        rows.append({'id': 'extra', 'status': 'PASS', 'reason': 'extra', 'evidence': [str(evidence)]})
    elif damage == 'ordinal':
        rows[0]['id'] = '1'
    elif damage == 'duplicate':
        rows[1]['id'] = rows[0]['id']
    elif damage in {'FAIL', 'BLOCKED'}:
        rows[0]['status'] = damage
    elif damage == 'no-evidence':
        rows[0]['evidence'] = []
    elif damage == 'empty-reason':
        rows[0]['reason'] = ''
    else:
        request['result']['scans'] = {str(i): row for i, row in enumerate(rows)}
    before = copy.deepcopy(state)
    with pytest.raises((ValueError, TypeError)):
        run_state.advance(state, request)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    assert state == before
    logger.info('[IMP:9][test_named_scan_verdicts][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_named_scan_verdicts

# region FUNC_test_pending_plan_and_source_scope [DOMAIN(8): NativeMethodology; CONCEPT(9): PendingPlan, SourceScope; TECH(7): pytest]
## @purpose Verify that a pending plan is bound exactly once when the Architect result is accepted, changing the input identity, and that a later Code change outside the saved Architect scope is refused.
## @uses pytest.raises, run_state.advance, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting phase code, plan status bound and an input identity different from the pre-bind one, then that a Code record whose sourceChange adds spec.md raises ValueError mentioning the approved Architect scope, leaves the state unchanged and produces the exact two-event error cascade. Side effects: owned fixture plan file. Errors: AssertionError. Example: mayEdit extended by spec.md is refused with sourceChange exceeds approved Architect scope.
## @complexity 5
def test_pending_plan_and_source_scope(tmp_path, caplog):
    logger.info('[IMP:4][test_pending_plan_and_source_scope][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('sourceChange exceeds approved Architect scope', '_source_change', 'advance')
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path, pending=True)
    state = to_phase(state, evidence, 'architect')
    old = state['input_identity']
    Path(state['plan']['path']).write_text('Actual newly produced fixture plan.\n')
    state = run_state.advance(state, success(state, evidence))
    bound = copy.deepcopy(state)
    request = success(state, evidence)
    request['context']['sourceChange']['mayEdit'].append('spec.md')
    before = copy.deepcopy(state)
    with pytest.raises(ValueError, match='approved Architect'):
        run_state.advance(state, request)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    assert bound['phase'] == 'code' and bound['plan']['status'] == 'bound' and bound['input_identity'] != old
    assert state == before
    logger.info('[IMP:9][test_pending_plan_and_source_scope][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_pending_plan_and_source_scope

# region FUNC_test_retry_and_unknown_effects [DOMAIN(8): NativeMethodology; CONCEPT(10): ResponseCorrection; TECH(7): pytest]
## @purpose Verify that one response correction per phase attempt is allowed, the second ends BLOCKED, neither spends Debug, and a correction with an unknown effect is refused before replay.
## @uses pytest.raises, run_state.advance, test_run_state.expose, test_run_state.make_fixture, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting that the first correction counts 1 with debug_spent 0, the second yields status BLOCKED with debug_spent 0, an unknownEffect true control raises ValueError mentioning investigation, and the initial ledger entry stays initialized. Side effects: owned fixture only. Errors: AssertionError. Example: two corrections in Bootstrap end BLOCKED.
## @complexity 5
def test_retry_and_unknown_effects(tmp_path, caplog):
    logger.info('[IMP:4][test_retry_and_unknown_effects][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('unknown effect requires investigation before replay', 'advance')
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    control = {'kind': 'control', 'event': 'response-correction', 'phase': 'bootstrap', 'reason': 'missing/null response; no effects occurred', 'evidence': [str(evidence)], 'unknownEffect': False}
    first = run_state.advance(state, control)
    blocked = run_state.advance(first, control)
    bad = dict(control, unknownEffect=True)
    with pytest.raises(ValueError, match='investigation'):
        run_state.advance(state, bad)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    assert first['retry_episodes']['response-correction'] == 1 and first['debug_spent'] == 0
    assert blocked['status'] == 'BLOCKED' and blocked['debug_spent'] == 0
    assert state['history'][0]['kind'] == 'initialized'
    logger.info('[IMP:9][test_retry_and_unknown_effects][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_retry_and_unknown_effects

# region FUNC_test_terminal_and_late_finalize [DOMAIN(8): NativeMethodology; CONCEPT(10): TerminalRun, LateFinalize; TECH(7): pytest]
## @purpose Verify that a late repair found in Finalize ends ESCALATED_FINALIZE with no Debug spend, and that a terminal run refuses any further record unchanged.
## @uses pytest.raises, run_state.advance, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting that an ESCALATED_FINALIZE return with a reason, limitations and requiredRepair is accepted with debug_spent 0, that a following success record raises ValueError mentioning terminal, and that the escalated state equals its deep copy. Side effects: owned fixture only. Errors: AssertionError. Example: advancing an ESCALATED_FINALIZE run is refused as terminal.
## @complexity 5
def test_terminal_and_late_finalize(tmp_path, caplog):
    logger.info('[IMP:4][test_terminal_and_late_finalize][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('terminal run cannot advance; owner continuation required', 'advance')
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    state = to_phase(state, evidence, 'finalize')
    result = envelope(state, evidence, 'ESCALATED_FINALIZE')
    result.update(reason='current map needs source repair', limitations=['no repair grant'], requiredRepair='repair annotation after owner continuation')
    escalated = run_state.advance(state, {'kind': 'role', 'result': result})
    before = copy.deepcopy(escalated)
    with pytest.raises(ValueError, match='terminal'):
        run_state.advance(escalated, success(state, evidence))
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    assert escalated['status'] == 'ESCALATED_FINALIZE' and escalated['debug_spent'] == 0
    assert escalated == before
    logger.info('[IMP:9][test_terminal_and_late_finalize][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_terminal_and_late_finalize

# region FUNC_test_real_state_cli_and_checkpoint [DOMAIN(8): NativeMethodology; CONCEPT(9): RealChannel, CheckpointResume; TECH(7): subprocess]
## @purpose Verify through real processes that show is read only, record advances and saves the ledger, a fresh show resumes the saved state, and a duplicate-key result is refused with exit 2 while a refusal event is appended and progress is kept.
## @uses json.dumps, json.loads, test_run_state.cli, test_run_state.expose, test_run_state.make_fixture, test_run_state.success
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting show exit 0 with stdout state equal to the in-memory state and unchanged file bytes; record exit 0 with the saved phase architect and debug_spent 0; a resumed show equal to the saved state; a result file with duplicate keys exit 2 with empty stdout, the saved phase unchanged and the last history kind refused; and the main RESULT and REFUSAL trace on stderr. Side effects: owned ledger and result files. Errors: AssertionError. Example: record of a valid Bootstrap result leaves the ledger in the architect phase.
## @complexity 6
def test_real_state_cli_and_checkpoint(tmp_path, caplog):
    logger.info('[IMP:4][test_real_state_cli_and_checkpoint][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path)
    before = path.read_bytes()
    shown = cli('show', '--state', path, cwd=tmp_path)
    shown_unchanged = path.read_bytes() == before
    request = success(state, evidence)
    result_path = tmp_path / 'result.json'
    result_path.write_text(json.dumps(request))
    recorded = cli('record', '--state', path, '--result', result_path, cwd=tmp_path)
    saved = json.loads(path.read_text())
    resumed = cli('show', '--state', path, cwd=tmp_path)
    result_path.write_text('{"kind":"role","kind":"control"}')
    rejected = cli('record', '--state', path, '--result', result_path, cwd=tmp_path)
    refused = json.loads(path.read_text())
    expose(caplog, 'cli')
    assert shown.returncode == 0 and json.loads(shown.stdout)['state'] == state and shown_unchanged
    assert recorded.returncode == 0
    assert saved['phase'] == 'architect' and saved['debug_spent'] == 0
    assert resumed.returncode == 0 and json.loads(resumed.stdout)['state'] == saved
    assert rejected.returncode == 2 and not rejected.stdout
    assert refused['phase'] == 'architect' and refused['debug_spent'] == 0 and refused['history'][-1]['kind'] == 'refused'
    assert '[IMP:9][main][RESULT]' in shown.stderr and '[IMP:10][main][REFUSAL]' in rejected.stderr
    logger.info('[IMP:9][test_real_state_cli_and_checkpoint][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_state_cli_and_checkpoint

# region FUNC_test_own_helper_trace_and_map [DOMAIN(8): NativeMethodology; CONCEPT(9): SemanticTrace, CodeMap; TECH(7): doxygen, xml]
## @purpose Verify that the helper emits its START, VALIDATION_SUCCESS and RESULT trace in order, and that a real Doxygen build over the owned package copy associates every top-level function of the four modules owned by this suite with its Purpose, Uses API, I/O and Complexity Score fields at the right source line.
## @uses ET.parse, ast.parse, subprocess.run, run_state.advance, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.missing_members
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting the ordered advance trace; a build with exit 0 that is completely silent when the real package has no pending member, or silent for the four owned modules while foreign output is tolerated and printed when other members are still pending; and for each owned module that every function has exactly one XML member with the four field labels and a location line equal to its source line. Side effects: runs doxygen inside the owned package copy only. Errors: AssertionError, including when the real Doxyfile is missing, which is not replaced by a placeholder. Example: run_state.advance maps to one member whose line equals its def line.
## @complexity 7
def test_own_helper_trace_and_map(tmp_path, caplog):
    logger.info('[IMP:4][test_own_helper_trace_and_map][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    accepted = run_state.advance(state, success(state, evidence))
    messages = [r.getMessage() for r in caplog.records]
    pending = missing_members()
    assert 'Doxyfile' not in pending, 'the real Doxyfile is required to build the map'
    package = Path(state['framework'])
    built = subprocess.run(['doxygen', 'Doxyfile'], cwd=package, text=True, capture_output=True)
    print('Actual owned package map:', built.args, 'cwd', package, 'exit', built.returncode, 'stdout', built.stdout, 'stderr', built.stderr)
    output_lines = (built.stdout + built.stderr).splitlines()
    own_names = [Path(m).name for m in OWN_MODULES]
    own_output = [line for line in output_lines if any(name in line for name in own_names)]
    xmlroot = package / 'doxygen_output/xml'
    members = []
    for compound in ET.parse(xmlroot / 'index.xml').getroot().findall('compound'):
        doc = ET.parse(xmlroot / (compound.attrib['refid'] + '.xml')).getroot()
        members.extend(doc.findall('.//memberdef'))
    checked = []
    for relative in OWN_MODULES:
        module = package / relative
        for function in [node for node in ast.parse(module.read_text(encoding='utf-8')).body if isinstance(node, ast.FunctionDef) and node.name != '_module_contract']:
            matches = [m for m in members if m.findtext('name') == function.name and m.find('location') is not None and Path(m.find('location').get('file', '')).name == module.name]
            detail = matches[0].find('detaileddescription') if len(matches) == 1 else None
            description = ' '.join(detail.itertext()) if detail is not None else ''
            checked.append((module.name + ':' + function.name, len(matches), all(label in description for label in ('Purpose:', 'Uses API:', 'I/O:', 'Complexity Score:')), int(matches[0].find('location').get('line')) == function.lineno if len(matches) == 1 else False))
    print('Actual own function associations:', checked)
    logger.info('[IMP:9][test_own_helper_trace_and_map][MAP_RESULT] own source associations=%d pending_members=%d foreign_output_lines=%d', len(checked), len(pending), len(output_lines) - len(own_output))
    expose(caplog, 'advance')
    assert accepted['phase'] == 'architect'
    assert messages.index('[IMP:4][advance][START] validate one parent-owned event') < next(i for i, m in enumerate(messages) if '[IMP:9][advance][VALIDATION_SUCCESS]' in m) < next(i for i, m in enumerate(messages) if '[IMP:9][advance][RESULT]' in m)
    assert built.returncode == 0 and not own_output
    if not pending:
        assert not built.stdout and not built.stderr
    assert checked and len({name for name, _, _, _ in checked}) == len(checked)
    assert all(count == 1 and labelled and located for _, count, labelled, located in checked)
    logger.info('[IMP:9][test_own_helper_trace_and_map][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_own_helper_trace_and_map

# region FUNC_test_real_cli_strict_debug_spelling [DOMAIN(8): NativeMethodology; CONCEPT(9): DebugAllowance, RealChannel; TECH(7): subprocess]
## @purpose Verify that the real init command refuses ambiguous textual Debug spellings with exit 2, creates no run directory and names the parsing failure on stderr.
## @uses pytest.mark.parametrize, test_run_state.cli, test_run_state.expose, test_run_state.make_fixture
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, spelling from the parametrized values +4, 04, a space before 4, a space after 4, -1 and 1.5. Output: None after asserting exit 2, empty stdout, no text-refusal run directory and the _decimal_cap FAIL trace on stderr. Side effects: owned fixture and one child process. Errors: AssertionError. Example: the spelling +4 is refused while 4 and 0 are valid.
## @complexity 4
@pytest.mark.parametrize('spelling', ['+4', '04', ' 4', '4 ', '-1', '1.5'])
def test_real_cli_strict_debug_spelling(tmp_path, caplog, spelling):
    logger.info('[IMP:4][test_real_cli_strict_debug_spelling][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    _, state, _ = make_fixture(tmp_path)
    target = Path(state['target'])
    request = ['init', '--project', target, '--spec', state['spec_path'], '--approval', 'structural fixture reference', '--framework', state['framework'], '--adapter', state['adapter_path'], '--plan', state['plan']['path'], '--run-id', 'text-refusal', '--max-debug', spelling]
    proc = cli(*request, cwd=tmp_path)
    expose(caplog, 'cli')
    assert proc.returncode == 2 and not proc.stdout and not (target / '.methodology/runs/text-refusal').exists()
    assert '[IMP:10][_decimal_cap][FAIL]' in proc.stderr
    logger.info('[IMP:9][test_real_cli_strict_debug_spelling][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_cli_strict_debug_spelling

# region FUNC_test_unknown_return_control_injection_and_unexpected_source [DOMAIN(8): NativeMethodology; CONCEPT(10): WorkerInjection, SourceDrift; TECH(7): pytest]
## @purpose Verify that a worker return carrying counters, approval or routing fields is rejected before any state change, and that an unapproved file in the target is refused as a candidate change.
## @uses pytest.raises, run_state.advance, run_state.validate_state, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting that debug_spent, approval and phaseRoute injected into a canonical result each raise ValueError mentioning unknown role return field with the state unchanged, and that a foreign file in the target raises a candidate change refusal; the exact error population is three payload cascades plus one validate_state cascade. Side effects: writes foreign.txt into the owned target. Errors: AssertionError. Example: a result with debug_spent set to a worker value is refused.
## @complexity 5
def test_unknown_return_control_injection_and_unexpected_source(tmp_path, caplog):
    logger.info('[IMP:4][test_unknown_return_control_injection_and_unexpected_source][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('unknown role return field', '_payload', 'advance') * 3 + error_profile('unexpected target candidate change', 'validate_state')
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    unchanged = []
    for extra in ('debug_spent', 'approval', 'phaseRoute'):
        request = success(state, evidence)
        request['result'][extra] = 'worker injection'
        before = copy.deepcopy(state)
        with pytest.raises(ValueError, match='unknown role return field'):
            run_state.advance(state, request)
        unchanged.append(state == before)
    (Path(state['target']) / 'foreign.txt').write_text('Unapproved current source drift.\n')
    with pytest.raises(ValueError, match='candidate change'):
        run_state.validate_state(state)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    assert unchanged == [True, True, True]
    logger.info('[IMP:9][test_unknown_return_control_injection_and_unexpected_source][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_unknown_return_control_injection_and_unexpected_source

# region FUNC_test_locked_input_and_containment_process_refusals [DOMAIN(8): NativeMethodology; CONCEPT(10): LockedInputs, RealChannel; TECH(7): subprocess]
## @purpose Verify through real processes that a changed spec, plan, adapter, core owner or package member, an old-schema ledger and an incomplete ledger are each refused with exit 2, empty stdout and an untouched state file.
## @uses json.dumps, pytest.mark.parametrize, test_run_state.cli, test_run_state.expose, test_run_state.make_fixture, test_run_state.success
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, damage from spec, plan, adapter, core, package, old-schema, incomplete-ledger. Output: None after asserting exit 2, empty stdout, byte-identical state file and that no source.py exists in the target. Side effects: appends bytes to one owned input or rewrites the owned ledger; one child process. Errors: AssertionError. Example: appending to the neutral code tests owner makes show fail on the immutable input identity.
## @complexity 5
@pytest.mark.parametrize('damage', ['spec', 'plan', 'adapter', 'core', 'package', 'old-schema', 'incomplete-ledger'])
def test_locked_input_and_containment_process_refusals(tmp_path, caplog, damage):
    logger.info('[IMP:4][test_locked_input_and_containment_process_refusals][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path)
    if damage in {'old-schema', 'incomplete-ledger'}:
        content = copy.deepcopy(state)
        if damage == 'old-schema':
            content['schema_version'] = 1
        else:
            content.pop('history')
        path.write_text(json.dumps(content))
        before = path.read_bytes()
        request = tmp_path / 'return.json'
        request.write_text(json.dumps(success(state, evidence)))
        proc = cli('record', '--state', path, '--result', request, cwd=tmp_path)
    else:
        destination = {'spec': Path(state['spec_path']), 'plan': Path(state['plan']['path']), 'adapter': Path(state['adapter_path']), 'core': Path(state['bindings']['neutral_root']) / 'code/tests.md', 'package': Path(state['framework']) / 'README.md'}[damage]
        destination.write_bytes(destination.read_bytes() + b'changed input\n')
        before = path.read_bytes()
        proc = cli('show', '--state', path, cwd=tmp_path)
    expose(caplog, 'cli')
    assert proc.returncode == 2 and not proc.stdout and path.read_bytes() == before
    assert not (Path(state['target']) / 'source.py').exists()
    logger.info('[IMP:9][test_locked_input_and_containment_process_refusals][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_locked_input_and_containment_process_refusals

# region FUNC_test_zero_repair_refusal_and_default_allowance [DOMAIN(8): NativeMethodology; CONCEPT(10): ZeroAllowance, DefaultFour; TECH(7): pytest]
## @purpose Verify that initialization without an explicit cap defaults to four, and that a Code defect under a zero allowance escalates in place with no Debug entry.
## @uses run_state.advance, run_state.initialize, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.to_phase
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting a second run initialized without max_debug has debug_cap 4 and debug_spent 0, and a cap-0 run receiving a Code BUG_REPORT ends ESCALATED in phase code with debug_spent 0, debug_delta 0 and the recorded origin code. Side effects: owned fixture and a second ledger. Errors: AssertionError. Example: cap 0 never enters Debug.
## @complexity 5
def test_zero_repair_refusal_and_default_allowance(tmp_path, caplog):
    logger.info('[IMP:4][test_zero_repair_refusal_and_default_allowance][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path, cap=0)
    target = Path(state['target'])
    _, default = run_state.initialize(target, state['spec_path'], 'structural fixture parent reference', 'default', framework=state['framework'], adapter=state['adapter_path'], plan=state['plan']['path'])
    state = to_phase(state, evidence, 'code')
    result = envelope(state, evidence, 'BUG_REPORT')
    result['bugReport'] = {key: 'Owned fixture actionable failure evidence' for key in BUG_FIELDS}
    refused = run_state.advance(state, {'kind': 'role', 'result': result})
    expose(caplog, 'advance')
    assert default['debug_cap'] == 4 and default['debug_spent'] == 0
    assert refused['status'] == 'ESCALATED' and refused['debug_spent'] == 0 and refused['phase'] == 'code'
    assert refused['history'][-1]['debug_delta'] == 0 and refused['debug_origin']['phase'] == 'code'
    logger.info('[IMP:9][test_zero_repair_refusal_and_default_allowance][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_zero_repair_refusal_and_default_allowance

# region FUNC_test_real_cli_initialization_and_nonoverwrite [DOMAIN(8): NativeMethodology; CONCEPT(9): RealChannel, NoReset; TECH(7): subprocess]
## @purpose Verify that the real init command creates a schema 2 ledger for the textual caps 0 and 4, and that repeating the same run id is refused with exit 2 and cannot overwrite or reset the first ledger.
## @uses json.loads, pytest.mark.parametrize, test_run_state.cli, test_run_state.expose, test_run_state.make_fixture
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, cap text 0 or 4. Output: None after asserting the first init exit 0 with schema 2, the cap and debug_spent 0 in the JSON answer, the second init exit 2 with empty stdout and byte-identical state file, the initialize RESULT trace on the first stderr and the initialize FAIL trace on the second. Side effects: owned fixture and two child processes. Errors: AssertionError. Example: cap text 0 gives a run with debug_cap 0.
## @complexity 4
@pytest.mark.parametrize('cap', ['0', '4'])
def test_real_cli_initialization_and_nonoverwrite(tmp_path, caplog, cap):
    logger.info('[IMP:4][test_real_cli_initialization_and_nonoverwrite][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    _, state, _ = make_fixture(tmp_path)
    args = ['init', '--project', state['target'], '--spec', state['spec_path'], '--approval', 'structural fixture reference', '--framework', state['framework'], '--adapter', state['adapter_path'], '--plan', state['plan']['path'], '--run-id', 'cli-init', '--max-debug', cap]
    first = cli(*args, cwd=tmp_path)
    actual = json.loads(first.stdout)
    p = Path(actual['state_file'])
    before = p.read_bytes()
    duplicate = cli(*args, cwd=tmp_path)
    expose(caplog, 'cli')
    assert first.returncode == 0
    assert actual['state']['schema_version'] == 2 and actual['state']['debug_cap'] == int(cap) and actual['state']['debug_spent'] == 0
    assert duplicate.returncode == 2 and not duplicate.stdout and p.read_bytes() == before
    assert '[IMP:9][initialize][RESULT]' in first.stderr and '[IMP:10][initialize][FAIL]' in duplicate.stderr
    logger.info('[IMP:9][test_real_cli_initialization_and_nonoverwrite][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_cli_initialization_and_nonoverwrite

# region FUNC_test_scoped_debug_deletion_and_mode_inventory [DOMAIN(8): NativeMethodology; CONCEPT(10): ScopedDeletion, ModeInventory; TECH(7): pytest]
## @purpose Verify that the candidate inventory records numeric file modes, that a Debug fix may delete an in-scope file, and that renewed QA and Review follow the deletion with one Debug spend.
## @uses run_state.advance, run_state.inventory, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting that an executable obsolete.py in scope is recorded with mode 493, a Review defect enters Debug, the FIXED return after deleting the file moves to qa with spend 1, the obsolete.py row gone and the source change listing exactly that path, and a renewed QA moves to review with the file absent. Side effects: creates and deletes obsolete.py in the owned target. Errors: AssertionError. Example: removing an approved obsolete member passes without a new spend.
## @complexity 6
def test_scoped_debug_deletion_and_mode_inventory(tmp_path, caplog):
    logger.info('[IMP:4][test_scoped_debug_deletion_and_mode_inventory][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    state = to_phase(state, evidence, 'architect')
    architect = success(state, evidence)
    architect['result']['mayEdit'].append('obsolete.py')
    state = run_state.advance(state, architect)
    request = success(state, evidence)
    obsolete = Path(state['target']) / 'obsolete.py'
    obsolete.write_text('OLD = 7\n')
    obsolete.chmod(0o755)
    request['context']['sourceChange']['mayEdit'].append('obsolete.py')
    request['result']['candidateIdentity'] = run_state.inventory(state['target'])['digest']
    request['result']['doxygen']['candidateIdentity'] = request['result']['candidateIdentity']
    state = run_state.advance(state, request)
    recorded_mode = next(r for r in state['candidate']['files'] if r['path'] == 'obsolete.py')['mode']
    state = to_phase(state, evidence, 'review')
    bug = envelope(state, evidence, 'BUG_REPORT')
    bug['bugReport'] = {key: 'Owned fixture obsolete member must be removed' for key in BUG_FIELDS}
    state = run_state.advance(state, {'kind': 'role', 'result': bug})
    obsolete.unlink()
    fixed = envelope(state, evidence, 'FIXED')
    fixed.update(rootCause='obsolete owned member', fix='remove declared obsolete source', filesTouched=[str(obsolete)], postFixAudit='actual removal compared to approved scope', testSummary='structural deletion fixture', regressionEvidence=[str(evidence)], origin='review')
    source = Path(state['target']) / 'source.py'
    updated = run_state.advance(state, {'kind': 'role', 'result': fixed, 'context': {'sourceChange': {'mayEdit': ['obsolete.py'], 'artifacts': [str(source)]}}})
    after_fix = copy.deepcopy(updated)
    updated = run_state.advance(updated, success(updated, evidence))
    expose(caplog, 'advance')
    assert recorded_mode == 0o755
    assert after_fix['phase'] == 'qa' and after_fix['debug_spent'] == 1 and 'obsolete.py' not in {r['path'] for r in after_fix['candidate']['files']}
    assert after_fix['history'][-1]['source_change']['changed'] == ['obsolete.py']
    assert updated['phase'] == 'review' and updated['debug_spent'] == 1 and not obsolete.exists()
    logger.info('[IMP:9][test_scoped_debug_deletion_and_mode_inventory][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_scoped_debug_deletion_and_mode_inventory

# region FUNC_test_precode_blocked_routes_direct_and_cli [DOMAIN(8): NativeMethodology; CONCEPT(9): PreCodeBlocked, RealChannel; TECH(7): subprocess]
## @purpose Verify that a BLOCKED return in Bootstrap or Architect is accepted directly and through the real CLI as a terminal BLOCKED run with no Code acceptance, no source written and no Debug spend.
## @uses json.dumps, json.loads, pytest.mark.parametrize, run_state.advance, run_state.save, test_run_state.cli, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.to_phase
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, phase bootstrap or architect. Output: None after asserting the direct advance leaves its input unchanged, yields status BLOCKED in the same phase with debug_spent 0 and the stated reason in history, no Code acceptance, and that the CLI record of the same request exits 0 with a saved BLOCKED ledger, no source.py and debug_spent 0. Side effects: owned fixture, one ledger save and one child process. Errors: AssertionError. Example: a blocked Architect never reaches Code.
## @complexity 5
@pytest.mark.parametrize('phase', ['bootstrap', 'architect'])
def test_precode_blocked_routes_direct_and_cli(tmp_path, caplog, phase):
    logger.info('[IMP:4][test_precode_blocked_routes_direct_and_cli][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path)
    state = to_phase(state, evidence, phase)
    run_state.save(path, state)
    result = envelope(state, evidence, 'BLOCKED')
    result.update(reason='Actual fixture prerequisite deliberately unavailable', limitations=['controlled structural pre-Code refusal'])
    request = {'kind': 'role', 'result': result}
    before = copy.deepcopy(state)
    blocked = run_state.advance(state, request)
    supplied = tmp_path / 'blocked.json'
    supplied.write_text(json.dumps(request))
    proc = cli('record', '--state', path, '--result', supplied, cwd=tmp_path)
    saved = json.loads(path.read_text())
    expose(caplog, 'advance')
    assert state == before and blocked['status'] == 'BLOCKED' and blocked['phase'] == phase and blocked['debug_spent'] == 0
    assert blocked['history'][-1]['result']['reason'] == result['reason'] and 'code' not in blocked['accepted']
    assert proc.returncode == 0 and saved['status'] == 'BLOCKED' and not (Path(state['target']) / 'source.py').exists()
    assert saved['debug_spent'] == 0
    logger.info('[IMP:9][test_precode_blocked_routes_direct_and_cli][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_precode_blocked_routes_direct_and_cli

# region FUNC_test_explicit_doxygen_prohibition_and_false_waivers [DOMAIN(8): NativeMethodology; CONCEPT(10): DoxygenProhibition; TECH(7): pytest]
## @purpose Verify that only an explicit written host prohibition naming Doxygen, found verbatim in a contained rule file, can replace the Code map record, and that a vague, tool-missing or absent-quote waiver is refused.
## @uses pytest.mark.parametrize, pytest.raises, run_state.advance, run_state.inventory, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, waiver from permitted, not-needed, missing-tool, absent-quote. Output: None after asserting that the permitted case advances to qa with the PROHIBITION_VALID trace and no error record, while each false waiver raises ValueError mentioning quote lacks, leaves the state unchanged and produces the exact three-event error cascade. Side effects: writes an AGENTS.md rule file in the owned target. Errors: AssertionError. Example: the text Doxygen is not needed is refused.
## @complexity 6
@pytest.mark.parametrize('waiver', ['permitted', 'not-needed', 'missing-tool', 'absent-quote'])
def test_explicit_doxygen_prohibition_and_false_waivers(tmp_path, caplog, waiver):
    logger.info('[IMP:4][test_explicit_doxygen_prohibition_and_false_waivers][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = () if waiver == 'permitted' else error_profile('quote lacks bounded explicit Doxygen denial evidence; absence is not prohibition', '_doxygen', '_payload', 'advance')
    quote = 'Target instruction: Doxygen XML generation is prohibited.'
    if waiver == 'not-needed':
        quote = 'Doxygen is not needed.'
    elif waiver == 'missing-tool':
        quote = 'Doxygen tool/configuration is missing.'
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path, prohibition=quote)
    state = to_phase(state, evidence, 'code')
    request = success(state, evidence)
    rule_path = Path(state['target']) / 'AGENTS.md'
    request['result']['candidateIdentity'] = run_state.inventory(state['target'])['digest']
    if waiver == 'absent-quote':
        quote = 'Target instruction: Doxygen XML generation must not run.'
    request['result']['doxygen'] = {'status': 'NOT_APPLICABLE', 'reason': 'Controlled fixture written target prohibition; parent truth separate', 'prohibition': {'path': str(rule_path), 'quote': quote}, 'evidence': [str(rule_path)], 'candidateIdentity': request['result']['candidateIdentity'], 'inputIdentity': state['input_identity']}
    if waiver == 'permitted':
        accepted = run_state.advance(state, request)
        expose(caplog, 'advance')
        assert accepted['phase'] == 'qa'
        assert any('[IMP:9][_doxygen][PROHIBITION_VALID]' in r.getMessage() for r in caplog.records)
    else:
        before = copy.deepcopy(state)
        with pytest.raises(ValueError, match='quote lacks'):
            run_state.advance(state, request)
        expose(caplog, 'advance', True, expected_errors=expected_errors)
        assert state == before
    logger.info('[IMP:9][test_explicit_doxygen_prohibition_and_false_waivers][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_explicit_doxygen_prohibition_and_false_waivers

# region FUNC_test_partial_code_bug_direct_and_cli [DOMAIN(8): NativeMethodology; CONCEPT(10): PartialCode, CausalDebug; TECH(7): subprocess]
## @purpose Verify that a Code defect after a partial write keeps the observed bytes in the candidate without accepting Code, charges the Debug entry (or escalates at cap 0), and that a stale candidate identity or a foreign change is refused with the ledger untouched.
## @uses json.dumps, json.loads, pytest.mark.parametrize, pytest.raises, run_state.advance, run_state.inventory, run_state.save, test_run_state.cli, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, and the parametrized cases initial, cap, damage: a fresh target, a target with a pre-existing source, cap 0, a stale candidate identity and a foreign file outside the scoped change. Output: None after asserting for the clean cases the new candidate digest, origin code, the scoped changed path, the spend or the ESCALATED status at cap 0, Code not accepted and the same outcome through the CLI; for the damaged cases ValueError with the exact error cascade, an unchanged input state and a CLI exit 2 with the saved candidate and spend unchanged. Side effects: writes source.py and possibly foreign.txt in the owned target. Errors: AssertionError. Example: cap 0 escalates in the code phase with debug_spent 0.
## @complexity 7
@pytest.mark.parametrize('initial,cap,damage', [(False, 4, 'none'), (True, 4, 'none'), (False, 0, 'none'), (False, 4, 'stale'), (True, 4, 'foreign')])
def test_partial_code_bug_direct_and_cli(tmp_path, caplog, initial, cap, damage):
    logger.info('[IMP:4][test_partial_code_bug_direct_and_cli][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = {'none': (), 'stale': error_profile('role candidate identity mismatch', 'advance'), 'foreign': error_profile('candidate changes outside parent sourceChange scope', '_source_change', 'advance')}[damage]
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path, cap=cap, initial_source=initial)
    state = to_phase(state, evidence, 'code')
    run_state.save(path, state)
    source = Path(state['target']) / 'source.py'
    source.write_text('VALUE = 3\n')
    evidence.write_text('Actual owned source observation: VALUE3 differs from fixture required18; partial Code failure.\n')
    result = envelope(state, evidence, 'BUG_REPORT')
    result.update(artifacts=[str(source)], bugReport={key: 'Actual partial fixture Code value3 requires correction to18' for key in BUG_FIELDS})
    if damage == 'stale':
        result['candidateIdentity'] = state['candidate']['digest']
    elif damage == 'foreign':
        (Path(state['target']) / 'foreign.txt').write_text('Outside accepted source scope.\n')
        result['candidateIdentity'] = run_state.inventory(state['target'])['digest']
    request = {'kind': 'role', 'result': result, 'context': {'sourceChange': {'mayEdit': ['source.py'], 'artifacts': [str(source)]}}}
    before = copy.deepcopy(state)
    updated = None
    if damage == 'none':
        updated = run_state.advance(state, request)
    else:
        with pytest.raises(ValueError):
            run_state.advance(state, request)
    supplied = tmp_path / 'partial-code.json'
    supplied.write_text(json.dumps(request))
    proc = cli('record', '--state', path, '--result', supplied, cwd=tmp_path)
    saved = json.loads(path.read_text())
    expose(caplog, 'advance', damage != 'none', expected_errors=expected_errors)
    assert state == before
    if damage == 'none':
        assert updated['candidate']['digest'] == result['candidateIdentity']
        assert updated['debug_origin']['phase'] == 'code' and updated['history'][-1]['source_change']['changed'] == ['source.py']
        assert updated['status'] == ('ESCALATED' if cap == 0 else 'RUNNING') and updated['debug_spent'] == (0 if cap == 0 else 1)
        assert updated['phase'] == ('code' if cap == 0 else 'debug') and 'code' not in updated['accepted']
        assert proc.returncode == 0 and saved['debug_spent'] == (0 if cap == 0 else 1)
        assert saved['debug_origin']['candidate'] == result['candidateIdentity']
    else:
        assert proc.returncode == 2 and saved['phase'] == 'code' and saved['debug_spent'] == 0 and saved['candidate'] == before['candidate']
    logger.info('[IMP:9][test_partial_code_bug_direct_and_cli][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_partial_code_bug_direct_and_cli

# region FUNC_test_partial_code_blocked_and_effect_controls [DOMAIN(8): NativeMethodology; CONCEPT(10): PartialCode, UnknownEffect; TECH(7): subprocess]
## @purpose Verify that a Code BLOCKED return after a partial write, and a parent response correction with a known effect, keep the observed bytes without accepting Code or spending Debug, while a correction with an unknown effect is refused and recorded as an investigation dependency.
## @uses json.dumps, json.loads, pytest.mark.parametrize, pytest.raises, run_state.advance, run_state.inventory, run_state.save, test_run_state.cli, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, kind from blocked, known-correction, unknown-correction. Output: None after asserting for the first two the candidate digest equal to the real tree, debug_spent 0, Code not accepted, phase code with status BLOCKED or RUNNING, the correction counter 1 only for the known correction and the changed path source.py, with the same outcome through the CLI; for the unknown correction ValueError mentioning investigation, an unchanged input, a CLI exit 2 and a saved refusal event naming the investigation. Side effects: writes source.py in the owned target. Errors: AssertionError. Example: unknownEffect true never accepts the observed bytes.
## @complexity 7
@pytest.mark.parametrize('kind', ['blocked', 'known-correction', 'unknown-correction'])
def test_partial_code_blocked_and_effect_controls(tmp_path, caplog, kind):
    logger.info('[IMP:4][test_partial_code_blocked_and_effect_controls][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('unknown effect requires investigation before replay', 'advance') if kind == 'unknown-correction' else ()
    caplog.set_level(logging.INFO)
    path, state, evidence = make_fixture(tmp_path)
    state = to_phase(state, evidence, 'code')
    run_state.save(path, state)
    source = Path(state['target']) / 'source.py'
    source.write_text('PARTIAL = 3\n')
    context = {'sourceChange': {'mayEdit': ['source.py'], 'artifacts': [str(source)]}}
    if kind == 'blocked':
        role = envelope(state, evidence, 'BLOCKED')
        role['candidateIdentity'] = run_state.inventory(state['target'])['digest']
        role.update(reason='controlled permitted environment prerequisite unavailable after partial Code writes', limitations=['no Code completion'], artifacts=[str(source)])
        request = {'kind': 'role', 'result': role, 'context': context}
    else:
        request = {'kind': 'control', 'event': 'response-correction', 'phase': 'code', 'reason': 'actual observed partial write; ' + ('effect investigated and known' if kind == 'known-correction' else 'destination fate remains unknown; investigation required'), 'evidence': [str(evidence)], 'unknownEffect': kind == 'unknown-correction', 'context': context}
    before = copy.deepcopy(state)
    updated = None
    if kind == 'unknown-correction':
        with pytest.raises(ValueError, match='investigation'):
            run_state.advance(state, request)
    else:
        updated = run_state.advance(state, request)
    supplied = tmp_path / 'partial-control.json'
    supplied.write_text(json.dumps(request))
    proc = cli('record', '--state', path, '--result', supplied, cwd=tmp_path)
    saved = json.loads(path.read_text())
    expose(caplog, 'advance', kind == 'unknown-correction', expected_errors=expected_errors)
    assert state == before
    if kind == 'unknown-correction':
        assert proc.returncode == 2 and saved['phase'] == 'code' and saved['debug_spent'] == 0 and saved['retry_episodes']['response-correction'] == 0
        assert saved['candidate'] == before['candidate'] and 'investigation' in saved['history'][-1]['reason']
    else:
        assert updated['candidate']['digest'] == run_state.inventory(state['target'])['digest'] and updated['debug_spent'] == 0 and 'code' not in updated['accepted']
        assert updated['phase'] == 'code' and updated['status'] == ('BLOCKED' if kind == 'blocked' else 'RUNNING')
        assert updated['retry_episodes']['response-correction'] == (1 if kind == 'known-correction' else 0)
        assert updated['history'][-1]['source_change']['changed'] == ['source.py']
        assert proc.returncode == 0 and saved['candidate']['digest'] == run_state.inventory(state['target'])['digest'] and saved['debug_spent'] == 0
    logger.info('[IMP:9][test_partial_code_blocked_and_effect_controls][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_partial_code_blocked_and_effect_controls

# region FUNC_test_full_prohibition_finalize_route [DOMAIN(8): NativeMethodology; CONCEPT(10): DoxygenProhibition, Finalize; TECH(7): pytest]
## @purpose Verify the full route under a valid retained Doxygen prohibition: Finalize may omit the map path only while the prohibition rule bytes are unchanged and the map was not applicable, including after a counted Debug repair; a missing prohibition or a changed rule is refused.
## @uses pytest.mark.parametrize, pytest.raises, run_state.advance, test_run_state.envelope, test_run_state.expose, test_run_state.make_fixture, test_run_state.success, test_run_state.to_phase, test_run_state.error_profile
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, damage from none, debug, missing-applicable, stale-rule. Output: None after asserting for none and debug a SUCCESS run whose Finalize record has no doxygenPath (and one Debug spend for debug), and for missing-applicable and stale-rule ValueError with their exact error cascades. Side effects: writes and for stale-rule rewrites the AGENTS.md rule file and, for debug, source.py. Errors: AssertionError. Example: removing the prohibition text after Code makes Finalize fail on a changed candidate.
## @complexity 7
@pytest.mark.parametrize('damage', ['none', 'debug', 'missing-applicable', 'stale-rule'])
def test_full_prohibition_finalize_route(tmp_path, caplog, damage):
    logger.info('[IMP:4][test_full_prohibition_finalize_route][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = {'none': (), 'debug': (), 'missing-applicable': error_profile('applicable Finalize Doxygen path missing', '_payload', 'advance'), 'stale-rule': error_profile('unexpected target candidate change', 'validate_state', 'advance')}[damage]
    caplog.set_level(logging.INFO)
    quote = 'Do not run Doxygen in this controlled target.'
    path, state, evidence = make_fixture(tmp_path, prohibition=quote if damage != 'missing-applicable' else None)
    state = to_phase(state, evidence, 'code')
    request = success(state, evidence)
    if damage != 'missing-applicable':
        rule = Path(state['target']) / 'AGENTS.md'
        request['result']['doxygen'] = {'status': 'NOT_APPLICABLE', 'reason': 'actual controlled host rule; parent judgment separate', 'prohibition': {'path': str(rule), 'quote': quote}, 'evidence': [str(rule)], 'candidateIdentity': request['result']['candidateIdentity'], 'inputIdentity': state['input_identity']}
    state = run_state.advance(state, request)
    spent_after_repair = None
    if damage == 'debug':
        bug = success(state, evidence)['result']
        bug['status'] = 'BUG_REPORT'
        bug['scans'][0]['status'] = 'FAIL'
        bug['bugReport'] = {key: 'actual controlled fixture correction' for key in BUG_FIELDS}
        state = run_state.advance(state, {'kind': 'role', 'result': bug})
        source = Path(state['target']) / 'source.py'
        source.write_text('FIXED = 24\n')
        fixed = envelope(state, evidence, 'FIXED')
        fixed.update(rootCause='controlled cause', fix='actual source change', filesTouched=[str(source)], postFixAudit='scope observed', testSummary='controlled actual helper route', regressionEvidence=[str(evidence)], origin='qa')
        state = run_state.advance(state, {'kind': 'role', 'result': fixed, 'context': {'sourceChange': {'mayEdit': ['source.py'], 'artifacts': [str(source)]}}})
        spent_after_repair = state['debug_spent']
    state = to_phase(state, evidence, 'finalize')
    request = success(state, evidence)
    request['result'].pop('doxygenPath')
    if damage == 'stale-rule':
        rule.write_text('Doxygen prohibition removed after Code.\n')
    updated = None
    if damage in {'none', 'debug'}:
        updated = run_state.advance(state, request)
    else:
        with pytest.raises(ValueError):
            run_state.advance(state, request)
    expose(caplog, 'advance', damage not in {'none', 'debug'}, expected_errors=expected_errors)
    if updated is not None:
        assert updated['status'] == 'SUCCESS' and 'doxygenPath' not in updated['history'][-1]['result']
    if damage == 'debug':
        assert spent_after_repair == 1
    logger.info('[IMP:9][test_full_prohibition_finalize_route][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_full_prohibition_finalize_route

# region FUNC_test_expected_error_profile_rejects_unrelated [DOMAIN(9): NativeMethodology; CONCEPT(10): DiscriminatingErrorOracle; TECH(7): pytest, logging]
## @purpose Prove that the real refusal baseline passes the exact error oracle while one unrelated ERROR or CRITICAL record, from the helper logger or a foreign logger, always fails it.
## @uses pytest.mark.parametrize, pytest.raises, logging.getLogger, run_state.advance, copy.deepcopy, test_run_state.make_fixture, test_run_state.success, test_run_state.error_profile, test_run_state.expose
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, injected_logger from run_state and foreign_error_oracle, level ERROR and CRITICAL (four cases). The legitimate four-event historical-schema cascade passes first; then one injected record forces AssertionError, and the final population equals the baseline plus the injected record plus the oracle own REJECT with counts 4 and 5. No producer is mocked and no source is changed. Side effects: clears caplog at the end. Errors: AssertionError on mismatch. Example: a foreign CRITICAL event after a clean refusal fails the oracle.
## @complexity 5
@pytest.mark.parametrize('injected_logger', ['run_state', 'foreign_error_oracle'])
@pytest.mark.parametrize('level', [logging.ERROR, logging.CRITICAL])
def test_expected_error_profile_rejects_unrelated(tmp_path, caplog, injected_logger, level):
    logger.info('[IMP:4][test_expected_error_profile_rejects_unrelated][START] discriminate actual extra errors')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('unsupported state schema; historical records are read-only', '_state_shape', 'validate_state', 'advance')
    caplog.set_level(logging.INFO)
    _, state, evidence = make_fixture(tmp_path)
    stale = copy.deepcopy(state)
    stale['schema_version'] = 1
    before = copy.deepcopy(stale)
    with pytest.raises(ValueError, match='historical'):
        run_state.advance(stale, success(state, evidence))
    assert stale == before
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    logging.getLogger(injected_logger).log(level, '[IMP:10][diagnostic_unrelated][INJECTED_ERROR] no refusal cause')
    with pytest.raises(AssertionError, match='ordered error profile'):
        expose(caplog, 'advance', True, expected_errors=expected_errors)
    actual = tuple((r.name, r.levelno, r.getMessage()) for r in caplog.records if r.levelno >= logging.ERROR)
    assert actual == expected_errors + ((injected_logger, level, '[IMP:10][diagnostic_unrelated][INJECTED_ERROR] no refusal cause'), (__name__, logging.ERROR, '[IMP:10][expose][REJECT] expected_events=4 actual_events=5'))
    print('Actual baseline accepted and injected extra refused:', injected_logger, logging.getLevelName(level))
    caplog.clear()
    logger.info('[IMP:9][test_expected_error_profile_rejects_unrelated][RESULT] baseline passes; extra rejected')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_expected_error_profile_rejects_unrelated

# region FUNC_hermetic_git [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, GitIgnoreRules; TECH(7): pytest monkeypatch, os.environ]
## @purpose Make every git call of a fixture and of the helper under test read only the fixture repository rules, never the developer global or system configuration.
## @uses pytest.MonkeyPatch.setenv, pytest.MonkeyPatch.delenv, os.devnull, logging.Logger.info
## @io monkeypatch MonkeyPatch and tmp_path owned Path. Returns None. Side effects: for the test process and every child it starts, removes repository-redirecting variables, disables the global and system configuration files, overrides core.excludesFile with an empty file through GIT_CONFIG_COUNT and points XDG_CONFIG_HOME at an empty owned directory. Errors: none. Example: after the call a user-level ignore rule for .venv cannot change a fixture candidate.
## @complexity 3
def hermetic_git(monkeypatch, tmp_path):
    # START_BLOCK_BusinessLogic
    for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_CEILING_DIRECTORIES'):
        monkeypatch.delenv(key, raising=False)
    quiet = tmp_path / 'quiet-git-config'
    quiet.mkdir(exist_ok=True)
    monkeypatch.setenv('XDG_CONFIG_HOME', str(quiet))
    monkeypatch.setenv('GIT_CONFIG_GLOBAL', os.devnull)
    monkeypatch.setenv('GIT_CONFIG_NOSYSTEM', '1')
    monkeypatch.setenv('GIT_CONFIG_COUNT', '1')
    monkeypatch.setenv('GIT_CONFIG_KEY_0', 'core.excludesFile')
    monkeypatch.setenv('GIT_CONFIG_VALUE_0', os.devnull)
    logger.info('[IMP:7][hermetic_git][ENVIRONMENT] global and system git configuration disabled for this test')
    # END_BLOCK_BusinessLogic
# endregion FUNC_hermetic_git

# region FUNC_git [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, GitIgnoreRules; TECH(7): subprocess]
## @purpose Run one real git command inside an owned fixture repository and return its stdout, so fixtures change tracked, staged and ignored state through the real tool.
## @uses subprocess.run
## @io target owned directory Path, args git arguments. Returns the command stdout str after asserting exit 0. Side effects: the git command, for example init or add, changes only the owned fixture repository; prints the real arguments, exit and stderr. Errors: AssertionError on a nonzero exit. Example: git of init with the quiet flag creates a repository at the target.
## @complexity 2
def git(target, *args):
    # START_BLOCK_BusinessLogic
    proc = subprocess.run(['git', '-C', str(target), *map(str, args)], capture_output=True, text=True)
    print('Actual fixture git:', args, 'exit', proc.returncode, 'stderr', proc.stderr.strip())
    assert proc.returncode == 0
    logger.info('[IMP:7][git][RESULT] command=%s exit=%d', args[0], proc.returncode)
    return proc.stdout
    # END_BLOCK_BusinessLogic
# endregion FUNC_git

# region FUNC_prepare_git_target [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, GitIgnoreRules; TECH(7): shutil, subprocess]
## @purpose Give a test the actual package copy and a target that is the top level of a real git repository whose ignore rules name the Anti-Loop counter, the Doxygen map directory and the virtual environment.
## @uses test_run_state.hermetic_git, test_run_state.build_tree, test_run_state.git
## @io monkeypatch MonkeyPatch, tmp_path owned Path, prepare optional callable receiving the target Path before the repository is used, gitignore str rule text defaulting to GITIGNORE. Returns the tuple package, target, plan, evidence Paths exactly as build_tree does. Side effects: runs git init in the owned target and writes its gitignore file; nothing is committed. Errors: AssertionError when git cannot initialize. Example: the target then lists tests/.test_counter.json as ignored once the file exists.
## @complexity 3
def prepare_git_target(tmp_path, monkeypatch, prepare=None, gitignore=GITIGNORE):
    # START_BLOCK_BusinessLogic
    hermetic_git(monkeypatch, tmp_path)
    package, target, plan, evidence = build_tree(tmp_path)
    (target / '.gitignore').write_text(gitignore)
    git(target, 'init', '-q')
    if prepare is not None:
        prepare(target)
    logger.info('[IMP:9][prepare_git_target][RESULT] real repository target ready')
    return package, target, plan, evidence
    # END_BLOCK_BusinessLogic
# endregion FUNC_prepare_git_target

# region FUNC_make_git_fixture [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, GitIgnoreRules; TECH(7): run_state.initialize]
## @purpose Initialize one owned schema2 run over a real git repository target so a test starts from a bound ledger whose candidate follows git ignore rules.
## @uses test_run_state.prepare_git_target, run_state.initialize
## @io tmp_path owned Path, monkeypatch MonkeyPatch, cap Debug allowance defaulting to 4, prepare optional callable run on the target before initialization, gitignore str rule text defaulting to GITIGNORE. Returns the tuple state file Path, state dict, evidence Path like make_fixture. Side effects: the owned repository, tree and ledger only. Errors: ValueError or OSError from the helper, for example a refused link. Example: the returned candidate records exclusion_mode git.
## @complexity 3
def make_git_fixture(tmp_path, monkeypatch, cap=4, prepare=None, gitignore=GITIGNORE):
    # START_BLOCK_BusinessLogic
    package, target, plan, evidence = prepare_git_target(tmp_path, monkeypatch, prepare, gitignore)
    path, state = run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'fixture', cap, framework=package, adapter=package / 'adapter.json', plan=plan)
    logger.info('[IMP:9][make_git_fixture][RESULT] git fixture initialized')
    return path, state, evidence
    # END_BLOCK_BusinessLogic
# endregion FUNC_make_git_fixture

# region FUNC_qa_bug_report [DOMAIN(8): NativeMethodology; CONCEPT(9): CanonicalReturn, CausalDebug; TECH(7): run_state]
## @purpose Prepare the structural fixture QA BUG_REPORT that a red suite run produces, with one failed scan and the six-field report.
## @uses test_run_state.success
## @io state QA-phase schema2 dict and evidence owned Path. Returns the record wrapper with status BUG_REPORT, the first scan FAIL and a populated bugReport, bound to the current target digest. Side effects: none beyond the reads of success. Errors: ValueError or OSError from the inventory. Example: recording it with a cap of 4 enters Debug once.
## @complexity 3
def qa_bug_report(state, evidence):
    # START_BLOCK_BusinessLogic
    request = success(state, evidence)
    request['result'].update(status='BUG_REPORT', bugReport={key: 'Fixture observed cause and actionable local correction' for key in BUG_FIELDS})
    request['result']['scans'][0]['status'] = 'FAIL'
    logger.info('[IMP:9][qa_bug_report][RESULT] fixture red QA return prepared')
    return request
    # END_BLOCK_BusinessLogic
# endregion FUNC_qa_bug_report

# region FUNC_make_venv_links [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, IgnoredTree; TECH(7): os.symlink]
## @purpose Create the ignored virtual environment shapes that used to make the target inventory refuse a link: a real tree holding a file link and a directory link, or the environment itself linked to a directory outside the target.
## @uses os.symlink, pathlib.Path.mkdir, pathlib.Path.write_text
## @io target owned Path, variant tree or link, shared Path of the outside directory used by the link variant. Returns None. Side effects: creates .venv under the target, and for link the outside directory with a configuration file. Errors: OSError when links are unsupported. Example: variant tree gives .venv/bin/python as a file link and .venv/lib64 as a directory link.
## @complexity 3
def make_venv_links(target, variant, shared):
    # START_BLOCK_BusinessLogic
    if variant == 'tree':
        (target / '.venv/bin').mkdir(parents=True)
        (target / '.venv/lib').mkdir()
        (target / '.venv/lib/site.txt').write_text('ignored interpreter packages\n')
        os.symlink(sys.executable, target / '.venv/bin/python')
        os.symlink('lib', target / '.venv/lib64')
    else:
        shared.mkdir()
        (shared / 'pyvenv.cfg').write_text('shared virtual environment outside the target\n')
        os.symlink(shared, target / '.venv')
    logger.info('[IMP:7][make_venv_links][WRITE] variant=%s', variant)
    # END_BLOCK_BusinessLogic
# endregion FUNC_make_venv_links

# region FUNC_make_stray_link [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, LinkRefusal; TECH(7): os.symlink]
## @purpose Create one link that git does not ignore, so a test can prove that links in candidate content are still refused.
## @uses os.symlink
## @io target owned Path, kind file or dir. Returns None. Side effects: creates spec-link.md pointing at the specification for file, or tests-link pointing at the tests directory for dir. Errors: OSError when links are unsupported. Example: kind dir yields a directory link at the target root.
## @complexity 2
def make_stray_link(target, kind):
    # START_BLOCK_BusinessLogic
    if kind == 'file':
        os.symlink(target / 'spec.md', target / 'spec-link.md')
    else:
        os.symlink(target / 'tests', target / 'tests-link')
    logger.info('[IMP:7][make_stray_link][WRITE] kind=%s', kind)
    # END_BLOCK_BusinessLogic
# endregion FUNC_make_stray_link

# region FUNC_make_decomposed_directory [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, UnicodeNormalization; TECH(7): pathlib]
## @purpose Create a cache directory whose on-disk name is decomposed Unicode, the form a composing git does not print back.
## @uses pathlib.Path.mkdir, pathlib.Path.write_text
## @io target owned Path, name decomposed str directory name. Returns None. Side effects: creates the directory with one file. Errors: OSError. Example: the name made of the base letter and its combining breve is created as typed.
## @complexity 2
def make_decomposed_directory(target, name):
    # START_BLOCK_BusinessLogic
    (target / name).mkdir()
    (target / name / 'f.txt').write_text('ignored cache content\n')
    logger.info('[IMP:7][make_decomposed_directory][WRITE] directory created')
    # END_BLOCK_BusinessLogic
# endregion FUNC_make_decomposed_directory

# region FUNC_test_ignored_anti_loop_counter_does_not_change_candidate [DOMAIN(9): NativeMethodology; CONCEPT(10): AntiLoopCounter, CandidateIdentity; TECH(7): pytest, git]
## @purpose Verify that the git-ignored session counter, created and bumped by red suite runs while QA works, is not candidate content, so a QA BUG_REPORT is accepted into counted Debug instead of being refused as an unexpected candidate change.
## @uses pytest.mark.parametrize, run_state.advance, run_state.inventory, test_run_state.cli, test_run_state.expose, test_run_state.make_git_fixture, test_run_state.qa_bug_report, test_run_state.to_phase
## @io Input: tmp_path owned Path, monkeypatch, caplog, channel direct or cli. Output: None after asserting that the digest is the same before the counter exists, with attempts 1 and with attempts 2, that the counter path is not in the candidate files, that the BUG_REPORT is accepted with phase debug, one Debug entry spent and origin qa, that the candidate keeps its digest and records exclusion_mode git, and for the cli channel exit 0 with the saved ledger. Side effects: owned repository, counter file and one child process for cli. Errors: AssertionError. Example: before the repair the same record was refused with unexpected target candidate change.
## @complexity 6
@pytest.mark.parametrize('channel', ['direct', 'cli'])
def test_ignored_anti_loop_counter_does_not_change_candidate(tmp_path, monkeypatch, caplog, channel):
    logger.info('[IMP:4][test_ignored_anti_loop_counter_does_not_change_candidate][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_git_fixture(tmp_path, monkeypatch)
    state = to_phase(state, evidence, 'qa')
    run_state.save(path, state)
    target = Path(state['target'])
    counter = target / 'tests/.test_counter.json'
    clean = run_state.inventory(target)['digest']
    counter.write_text('{"attempts": 1}\n')
    first = run_state.inventory(target)['digest']
    request = qa_bug_report(state, evidence)
    counter.write_text('{"attempts": 2}\n')
    after = run_state.inventory(target)
    if channel == 'direct':
        entered = run_state.advance(state, request)
    else:
        result_path = tmp_path / 'qa-red.json'
        result_path.write_text(json.dumps(request))
        proc = cli('record', '--state', path, '--result', result_path, cwd=tmp_path)
        assert proc.returncode == 0
        entered = json.loads(path.read_text())
    expose(caplog, 'advance' if channel == 'direct' else 'cli')
    assert clean == first == after['digest'] == state['candidate']['digest'] == request['result']['candidateIdentity']
    assert 'tests/.test_counter.json' not in {row['path'] for row in after['files']} and after['exclusion_mode'] == 'git'
    assert entered['phase'] == 'debug' and entered['debug_spent'] == 1 and entered['debug_origin']['phase'] == 'qa'
    assert entered['history'][-1]['debug_delta'] == 1 and entered['candidate']['digest'] == clean and entered['candidate']['exclusion_mode'] == 'git'
    logger.info('[IMP:9][test_ignored_anti_loop_counter_does_not_change_candidate][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_ignored_anti_loop_counter_does_not_change_candidate

# region FUNC_test_ignored_code_map_output_is_not_candidate_content [DOMAIN(9): NativeMethodology; CONCEPT(10): DoxygenMap, CandidateIdentity; TECH(7): pytest, git]
## @purpose Verify that a Doxygen map written during Code into a git-ignored directory is not candidate content: Code is accepted, only the authored source is the observed change, and the ignored map files stay on disk.
## @uses run_state.advance, test_run_state.expose, test_run_state.make_git_fixture, test_run_state.success, test_run_state.to_phase
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after asserting Code SUCCESS accepted with phase qa, the observed source change exactly source.py, no docs path among the candidate files and the map index still present and cited as the map path. Side effects: owned repository, map files under docs/api/xml and source.py. Errors: AssertionError. Example: before the repair the new map files were reported as changes outside the sourceChange scope.
## @complexity 5
def test_ignored_code_map_output_is_not_candidate_content(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_ignored_code_map_output_is_not_candidate_content][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_git_fixture(tmp_path, monkeypatch)
    state = to_phase(state, evidence, 'code')
    xml = Path(state['target']) / 'docs/api/xml'
    xml.mkdir(parents=True)
    (xml / 'index.xml').write_text('<doxygenindex/>\n')
    (xml / 'file_8py.xml').write_text('<doxygen/>\n')
    request = success(state, evidence)
    request['result']['doxygen']['mapPath'] = str(xml / 'index.xml')
    accepted = run_state.advance(state, request)
    expose(caplog, 'advance')
    assert accepted['phase'] == 'qa' and accepted['history'][-1]['source_change']['changed'] == ['source.py']
    assert not any(row['path'].startswith('docs/') for row in accepted['candidate']['files']) and (xml / 'index.xml').is_file()
    assert accepted['candidate']['digest'] == request['result']['candidateIdentity']
    logger.info('[IMP:9][test_ignored_code_map_output_is_not_candidate_content][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_ignored_code_map_output_is_not_candidate_content

# region FUNC_test_ignored_virtual_environment_links_do_not_block_initialization [DOMAIN(9): NativeMethodology; CONCEPT(10): IgnoredTree, LinkRefusal; TECH(7): pytest, git, os.symlink]
## @purpose Verify that a git-ignored virtual environment holding file and directory links, or itself a link to a directory outside the target, does not make initialization refuse the target, in-process and through the real init and show commands.
## @uses pytest.mark.parametrize, os.symlink, run_state.initialize, run_state.validate_state, test_run_state.cli, test_run_state.expose, test_run_state.prepare_git_target
## @io Input: tmp_path owned Path, monkeypatch, caplog, variant tree or link and channel direct or cli. Output: None after asserting initialization succeeds, that no candidate row lies under .venv, that the candidate is validated again and records exclusion_mode git, and for cli exit 0 for init and show. Side effects: owned repository with links; one or two child processes for cli. Errors: AssertionError. Example: before the repair init refused with input must be a regular nonsymlink file.
## @complexity 6
@pytest.mark.parametrize('variant,channel', [('tree', 'direct'), ('link', 'direct'), ('tree', 'cli')])
def test_ignored_virtual_environment_links_do_not_block_initialization(tmp_path, monkeypatch, caplog, variant, channel):
    logger.info('[IMP:4][test_ignored_virtual_environment_links_do_not_block_initialization][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    package, target, plan, evidence = prepare_git_target(tmp_path, monkeypatch, lambda target: make_venv_links(target, variant, tmp_path / 'shared-venv'))
    if channel == 'direct':
        _, state = run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'links', framework=package, adapter=package / 'adapter.json', plan=plan)
        validated = run_state.validate_state(state)
    else:
        init = cli('init', '--project', target, '--spec', target / 'spec.md', '--approval', 'structural fixture reference', '--framework', package, '--adapter', package / 'adapter.json', '--plan', plan, '--run-id', 'links', cwd=tmp_path)
        assert init.returncode == 0
        state = json.loads(init.stdout)['state']
        shown = cli('show', '--state', target / '.methodology/runs/links/state.json', cwd=tmp_path)
        assert shown.returncode == 0
        validated = json.loads(shown.stdout)['state']['candidate']
    expose(caplog, 'inventory' if channel == 'direct' else 'cli')
    assert not any(row['path'].startswith('.venv') for row in state['candidate']['files']) and state['candidate']['exclusion_mode'] == 'git'
    assert {row['path'] for row in state['candidate']['files']} >= {'spec.md', 'tests/guide.md', 'plan.md', '.gitignore'}
    assert validated == state['candidate']
    logger.info('[IMP:9][test_ignored_virtual_environment_links_do_not_block_initialization][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_ignored_virtual_environment_links_do_not_block_initialization

# region FUNC_test_unignored_links_are_still_refused [DOMAIN(9): NativeMethodology; CONCEPT(10): LinkRefusal, NoWeakening; TECH(7): pytest, git, os.symlink]
## @purpose Verify that a link in candidate content, one git does not ignore, is still refused at initialization with the same exact error cascade, so the ignored-tree relief does not weaken link refusal.
## @uses pytest.mark.parametrize, pytest.raises, os.symlink, run_state.initialize, test_run_state.error_profile, test_run_state.expose, test_run_state.prepare_git_target
## @io Input: tmp_path owned Path, monkeypatch, caplog, kind file or dir. Output: None after asserting ValueError and the exact declared cascade, a file link ending in _file, inventory and initialize events and a directory link in inventory and initialize events, and that no run directory was created. Side effects: owned repository with one link. Errors: AssertionError. Example: a link named spec-link.md to the specification is refused.
## @complexity 5
@pytest.mark.parametrize('kind', ['file', 'dir'])
def test_unignored_links_are_still_refused(tmp_path, monkeypatch, caplog, kind):
    logger.info('[IMP:4][test_unignored_links_are_still_refused][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = {'file': error_profile('input must be a regular nonsymlink file', '_file', 'inventory', 'initialize'), 'dir': error_profile('source directory link unsupported', 'inventory', 'initialize')}[kind]
    caplog.set_level(logging.INFO)
    package, target, plan, _ = prepare_git_target(tmp_path, monkeypatch, lambda target: make_stray_link(target, kind))
    with pytest.raises(ValueError):
        run_state.initialize(target, target / 'spec.md', 'parent fixture structural reference; not authentic consent', 'refused', framework=package, adapter=package / 'adapter.json', plan=plan)
    expose(caplog, 'initialize', True, expected_errors=expected_errors)
    assert not (target / '.methodology/runs/refused').exists()
    logger.info('[IMP:9][test_unignored_links_are_still_refused][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_unignored_links_are_still_refused

# region FUNC_test_unignored_new_file_still_changes_candidate_and_is_refused [DOMAIN(9): NativeMethodology; CONCEPT(10): CandidateIdentity, NoWeakening; TECH(7): pytest, git]
## @purpose Verify that git-ignored changes are invisible but an unignored new file still changes the candidate digest and is refused by the Code sourceChange scope, so the ignore relief hides no authored content.
## @uses pytest.raises, run_state.advance, run_state.inventory, test_run_state.error_profile, test_run_state.expose, test_run_state.make_git_fixture, test_run_state.success, test_run_state.to_phase
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after asserting that an ignored counter leaves the digest unchanged, that an unignored notes.txt changes it and appears in the candidate files, that Code recorded with that stray file raises ValueError about the sourceChange scope with the exact two-event cascade and leaves the state unchanged. Side effects: owned repository, counter, notes.txt and source.py. Errors: AssertionError. Example: notes.txt outside the declared mayEdit is refused while the counter is not even mentioned.
## @complexity 5
def test_unignored_new_file_still_changes_candidate_and_is_refused(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_unignored_new_file_still_changes_candidate_and_is_refused][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('candidate changes outside parent sourceChange scope', '_source_change', 'advance')
    caplog.set_level(logging.INFO)
    path, state, evidence = make_git_fixture(tmp_path, monkeypatch)
    state = to_phase(state, evidence, 'code')
    target = Path(state['target'])
    clean = run_state.inventory(target)['digest']
    (target / 'tests/.test_counter.json').write_text('{"attempts": 3}\n')
    ignored_only = run_state.inventory(target)['digest']
    (target / 'notes.txt').write_text('unapproved fixture note outside the declared scope\n')
    stray = run_state.inventory(target)
    request = success(state, evidence)
    before = copy.deepcopy(state)
    with pytest.raises(ValueError, match='outside parent sourceChange scope'):
        run_state.advance(state, request)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    paths = {row['path'] for row in stray['files']}
    assert clean == ignored_only and stray['digest'] != clean
    assert 'notes.txt' in paths and 'tests/.test_counter.json' not in paths
    assert state == before
    logger.info('[IMP:9][test_unignored_new_file_still_changes_candidate_and_is_refused][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_unignored_new_file_still_changes_candidate_and_is_refused

# region FUNC_test_ignored_file_that_becomes_tracked_or_unignored_is_candidate [DOMAIN(9): NativeMethodology; CONCEPT(10): CandidateIdentity, IgnoreLifecycle; TECH(7): pytest, git]
## @purpose Verify that candidate membership follows git live: a file that was ignored and then force-added, or whose ignore rule was removed, becomes candidate content and the unchanged ledger refuses the drift.
## @uses pytest.mark.parametrize, pytest.raises, run_state.inventory, run_state.validate_state, test_run_state.error_profile, test_run_state.expose, test_run_state.git, test_run_state.make_git_fixture
## @io Input: tmp_path owned Path, monkeypatch, caplog, change tracked or unignored. Output: None after asserting the counter path is absent at initialization, present in the candidate files after git add with force or after the rule is removed, the digest differs, and validate_state raises ValueError about the candidate change with the exact two-event cascade. Side effects: owned repository index or rule file. Errors: AssertionError. Example: git add with force of the counter makes it tracked and therefore candidate content.
## @complexity 5
@pytest.mark.parametrize('change', ['tracked', 'unignored'])
def test_ignored_file_that_becomes_tracked_or_unignored_is_candidate(tmp_path, monkeypatch, caplog, change):
    logger.info('[IMP:4][test_ignored_file_that_becomes_tracked_or_unignored_is_candidate][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('unexpected target candidate change', 'validate_state')
    caplog.set_level(logging.INFO)
    relative = 'tests/.test_counter.json'
    path, state, evidence = make_git_fixture(tmp_path, monkeypatch, prepare=lambda target: (target / relative).write_text('{"attempts": 1}\n'))
    target = Path(state['target'])
    assert relative not in {row['path'] for row in state['candidate']['files']}
    if change == 'tracked':
        git(target, 'add', '-f', relative)
    else:
        (target / '.gitignore').write_text('docs/api/xml/\n.venv\n')
    now = run_state.inventory(target)
    with pytest.raises(ValueError, match='unexpected target candidate change'):
        run_state.validate_state(state)
    expose(caplog, 'validate_state', True, expected_errors=expected_errors)
    assert relative in {row['path'] for row in now['files']} and now['digest'] != state['candidate']['digest'] and now['exclusion_mode'] == 'git'
    logger.info('[IMP:9][test_ignored_file_that_becomes_tracked_or_unignored_is_candidate][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_ignored_file_that_becomes_tracked_or_unignored_is_candidate

# region FUNC_test_fallback_exclusion_list_without_usable_git_rules [DOMAIN(9): NativeMethodology; CONCEPT(10): FallbackHeuristic, CandidateIdentity; TECH(7): pytest, git, os.symlink]
## @purpose Verify the declared fallback: a target that is not a repository, a repository whose git cannot be launched, or a subdirectory of a larger repository excludes only the declared counter names and regenerable caches, still includes ordinary files, and never applies a surrounding repository ignore rule that could blind the candidate.
## @uses pytest.mark.parametrize, os.symlink, run_state.inventory, test_run_state.expose, test_run_state.git, test_run_state.hermetic_git
## @io Input: tmp_path owned Path, monkeypatch, caplog, situation no-repository, git-unavailable or subdirectory-of-repository. Output: None after asserting exclusion_mode fallback; ordinary files including an unlisted docs map are present; the counter, attempts file, coverage data, ruff, mypy, node_modules, venv, htmlcov, pytest caches and a virtual environment with links are absent without any link refusal; the digest is unchanged by edits of excluded files and changed by an edit of an ordinary one. Side effects: owned trees and, for git-unavailable, a PATH without git. Errors: AssertionError. Example: for a subdirectory of a repository whose rule ignores everything the ordinary files are still present.
## @complexity 7
@pytest.mark.parametrize('situation', ['no-repository', 'git-unavailable', 'subdirectory-of-repository'])
def test_fallback_exclusion_list_without_usable_git_rules(tmp_path, monkeypatch, caplog, situation):
    logger.info('[IMP:4][test_fallback_exclusion_list_without_usable_git_rules][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    hermetic_git(monkeypatch, tmp_path)
    root = tmp_path / 'plain'
    if situation == 'subdirectory-of-repository':
        outer = tmp_path / 'outer'
        outer.mkdir()
        (outer / '.gitignore').write_text('*\n')
        git(outer, 'init', '-q')
        root = outer / 'project'
    root.mkdir()
    ordinary = ['src/app.py', 'README.md', 'data/rows.csv', 'docs/api/xml/index.xml']
    excluded = ['tests/.test_counter.json', '.test_attempts', '.coverage', '.ruff_cache/CACHEDIR.TAG', '.mypy_cache/meta.json', 'node_modules/pkg/index.js', 'venv/pyvenv.cfg', 'htmlcov/index.html', '.pytest_cache/v/cache', '.venv/lib/site.txt']
    for relative in ordinary + excluded:
        (root / relative).parent.mkdir(parents=True, exist_ok=True)
        (root / relative).write_text('fixture content for ' + relative + '\n')
    os.symlink(sys.executable, root / '.venv/python')
    os.symlink('lib', root / '.venv/lib64')
    if situation == 'git-unavailable':
        (root / '.gitignore').write_text('docs/api/xml/\n')
        git(root, 'init', '-q')
        empty = tmp_path / 'no-git-here'
        empty.mkdir()
        monkeypatch.setenv('PATH', str(empty))
    first = run_state.inventory(root)
    for relative in excluded[:6]:
        (root / relative).write_text('changed generated content\n')
    second = run_state.inventory(root)
    (root / 'src/app.py').write_text('changed authored content\n')
    third = run_state.inventory(root)
    expose(caplog, 'inventory')
    paths = {row['path'] for row in first['files']}
    assert first['exclusion_mode'] == 'fallback' and paths >= set(ordinary)
    assert not paths & set(excluded) and not any(path.startswith('.venv') for path in paths)
    assert first['digest'] == second['digest'] and third['digest'] != first['digest']
    logger.info('[IMP:9][test_fallback_exclusion_list_without_usable_git_rules][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_fallback_exclusion_list_without_usable_git_rules

# region FUNC_test_git_enumeration_failure_is_refused_not_downgraded [DOMAIN(9): NativeMethodology; CONCEPT(10): FailClosed, CandidateIdentity; TECH(7): pytest, git]
## @purpose Verify that once the target is confirmed as a repository top level, a failing ignore enumeration refuses the inventory instead of silently falling back to the weaker heuristic.
## @uses pytest.raises, run_state.inventory, test_run_state.error_profile, test_run_state.expose, test_run_state.prepare_git_target
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after damaging the repository index of an owned fixture and asserting ValueError about the ignore enumeration with the exact three-event cascade of _expect, _git_ignored and inventory. Side effects: overwrites the owned repository index file. Errors: AssertionError. Example: a corrupt index makes inventory raise instead of reporting mode fallback.
## @complexity 4
def test_git_enumeration_failure_is_refused_not_downgraded(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_git_enumeration_failure_is_refused_not_downgraded][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('git ignore enumeration failed', '_git_ignored', 'inventory')
    caplog.set_level(logging.INFO)
    _, target, _, _ = prepare_git_target(tmp_path, monkeypatch)
    git(target, 'add', '.gitignore')
    (target / '.git/index').write_bytes(b'this is not a git index file')
    with pytest.raises(ValueError, match='enumeration'):
        run_state.inventory(target)
    expose(caplog, 'inventory', True, expected_errors=expected_errors)
    logger.info('[IMP:9][test_git_enumeration_failure_is_refused_not_downgraded][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_git_enumeration_failure_is_refused_not_downgraded

# region FUNC_test_explicit_exclusion_set_never_consults_git [DOMAIN(9): NativeMethodology; CONCEPT(10): PackageInventory, Determinism; TECH(7): pytest, git]
## @purpose Verify that an inventory taken with an explicit exclusion set, as the package binding does, ignores git rules entirely and keeps its original result shape, so package identity cannot vary with a repository ignore file.
## @uses run_state.inventory, test_run_state.expose, test_run_state.prepare_git_target
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after asserting that a git-ignored log file is present with an explicit set, absent for the default target inventory, and that only the target result carries exclusion_mode. Side effects: one owned ignored file. Errors: AssertionError. Example: a.log ignored by rule is a package member for the explicit call.
## @complexity 3
def test_explicit_exclusion_set_never_consults_git(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_explicit_exclusion_set_never_consults_git][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    _, target, _, _ = prepare_git_target(tmp_path, monkeypatch, gitignore='*.log\n')
    (target / 'a.log').write_text('ignored by rule, present on disk\n')
    explicit = run_state.inventory(target, {'.git', '.methodology'})
    default = run_state.inventory(target)
    expose(caplog, 'inventory')
    assert 'a.log' in {row['path'] for row in explicit['files']} and 'a.log' not in {row['path'] for row in default['files']}
    assert 'exclusion_mode' not in explicit and default['exclusion_mode'] == 'git'
    logger.info('[IMP:9][test_explicit_exclusion_set_never_consults_git][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_explicit_exclusion_set_never_consults_git

# region FUNC_test_ignored_decomposed_unicode_directory_is_skipped [DOMAIN(9): NativeMethodology; CONCEPT(10): UnicodeNormalization, IgnoredTree; TECH(7): pytest, git, unicodedata]
## @purpose Verify that a directory whose on-disk name is decomposed Unicode is skipped when git, which reports composed names on file systems that precompose, lists it as ignored.
## @uses unicodedata.normalize, run_state.inventory, test_run_state.expose, test_run_state.git, test_run_state.prepare_git_target
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after creating the decomposed directory with a composed rule and, when git lists it as ignored, asserting the directory is not in the candidate files while an ordinary file is; when this platform does not report it the test is skipped with that reason. Side effects: one owned directory. Errors: AssertionError. Example: on macOS the composed name from git matches the decomposed name from the walk only after normalization.
## @complexity 4
def test_ignored_decomposed_unicode_directory_is_skipped(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_ignored_decomposed_unicode_directory_is_skipped][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    composed = unicodedata.normalize('NFC', '\u0438\u0306-cache')
    decomposed = unicodedata.normalize('NFD', '\u0438\u0306-cache')
    _, target, _, _ = prepare_git_target(tmp_path, monkeypatch, lambda target: make_decomposed_directory(target, decomposed), gitignore=composed + '/\n')
    listed = git(target, 'ls-files', '--others', '--ignored', '--exclude-standard', '--directory', '-z')
    if not any(entry.rstrip('/') in {composed, decomposed} for entry in listed.split('\0')):
        pytest.skip('this platform and git do not report the decomposed directory as ignored')
    result = run_state.inventory(target)
    expose(caplog, 'inventory')
    paths = {row['path'] for row in result['files']}
    assert 'spec.md' in paths and not any(unicodedata.normalize('NFC', path).startswith(composed) for path in paths)
    logger.info('[IMP:9][test_ignored_decomposed_unicode_directory_is_skipped][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_ignored_decomposed_unicode_directory_is_skipped

# region FUNC_test_generated_outputs_stay_excluded_in_git_target_without_ignore_entries [DOMAIN(9): NativeMethodology; CONCEPT(10): GeneratedOutputs, NoRegression; TECH(7): pytest, git]
## @purpose Verify the deliberate superset of the git rule: the regenerable build and cache directories excluded before the repair (doxygen_output, output, __pycache__, .pytest_cache) stay excluded in a git target whose ignore file does not name them, so a Doxygen build and a test run during Code are accepted.
## @uses run_state.advance, run_state.inventory, test_run_state.expose, test_run_state.make_git_fixture, test_run_state.success, test_run_state.to_phase
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after creating, during Code and in a repository whose ignore file names only the counter, a Doxygen map under doxygen_output, files under output, __pycache__ and .pytest_cache, then asserting Code SUCCESS accepted with phase qa, the observed source change exactly source.py, none of those directories among the candidate files, mode git and the map index cited and still present. Side effects: owned repository and generated files. Errors: AssertionError. Example: without the superset a project that does not ignore doxygen_output was refused at Code with a change outside the sourceChange scope.
## @complexity 5
def test_generated_outputs_stay_excluded_in_git_target_without_ignore_entries(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_generated_outputs_stay_excluded_in_git_target_without_ignore_entries][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    path, state, evidence = make_git_fixture(tmp_path, monkeypatch, gitignore='tests/.test_counter.json\n')
    state = to_phase(state, evidence, 'code')
    target = Path(state['target'])
    generated = ['doxygen_output/xml/index.xml', 'doxygen_output/html/index.html', 'output/report.json', '__pycache__/note.txt', 'src/__pycache__/note.txt', '.pytest_cache/v/cache/lastfailed']
    for relative in generated:
        (target / relative).parent.mkdir(parents=True, exist_ok=True)
        (target / relative).write_text('regenerable fixture output for ' + relative + '\n')
    request = success(state, evidence)
    request['result']['doxygen']['mapPath'] = str(target / 'doxygen_output/xml/index.xml')
    accepted = run_state.advance(state, request)
    expose(caplog, 'advance')
    paths = {row['path'] for row in accepted['candidate']['files']}
    assert accepted['phase'] == 'qa' and accepted['history'][-1]['source_change']['changed'] == ['source.py']
    assert accepted['candidate']['exclusion_mode'] == 'git' and not paths & set(generated)
    assert not any(row.startswith(('doxygen_output/', 'output/', '__pycache__/', '.pytest_cache/')) for row in paths) and (target / 'doxygen_output/xml/index.xml').is_file()
    assert run_state.inventory(target)['digest'] == accepted['candidate']['digest']
    logger.info('[IMP:9][test_generated_outputs_stay_excluded_in_git_target_without_ignore_entries][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_generated_outputs_stay_excluded_in_git_target_without_ignore_entries

# region FUNC_test_unignored_ordinary_file_still_candidate_beside_generated_outputs [DOMAIN(9): NativeMethodology; CONCEPT(10): GeneratedOutputs, NoWeakening; TECH(7): pytest, git]
## @purpose Verify that the generated-output superset hides nothing authored: in a git target that ignores nothing but the counter, generated directories leave the digest unchanged while an unignored ordinary file, at the root and below a directory that merely shares a generated name as a file prefix, changes it and is refused outside the sourceChange scope.
## @uses pytest.raises, run_state.advance, run_state.inventory, test_run_state.error_profile, test_run_state.expose, test_run_state.make_git_fixture, test_run_state.success, test_run_state.to_phase
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after asserting that generated directories alone leave the digest unchanged, that notes.txt and outputs/data.csv (a directory named outputs, not output) each appear in the candidate files and change the digest, and that Code recorded with them raises ValueError about the sourceChange scope with the exact two-event cascade and leaves the state unchanged. Side effects: owned repository, generated files, notes.txt, outputs/data.csv and source.py. Errors: AssertionError. Example: doxygen_output is invisible while notes.txt is not.
## @complexity 5
def test_unignored_ordinary_file_still_candidate_beside_generated_outputs(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_unignored_ordinary_file_still_candidate_beside_generated_outputs][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors = error_profile('candidate changes outside parent sourceChange scope', '_source_change', 'advance')
    caplog.set_level(logging.INFO)
    path, state, evidence = make_git_fixture(tmp_path, monkeypatch, gitignore='tests/.test_counter.json\n')
    state = to_phase(state, evidence, 'code')
    target = Path(state['target'])
    clean = run_state.inventory(target)['digest']
    for relative in ('doxygen_output/xml/index.xml', '__pycache__/note.txt'):
        (target / relative).parent.mkdir(parents=True, exist_ok=True)
        (target / relative).write_text('regenerable fixture output\n')
    generated_only = run_state.inventory(target)['digest']
    (target / 'notes.txt').write_text('unapproved fixture note outside the declared scope\n')
    (target / 'outputs').mkdir()
    (target / 'outputs/data.csv').write_text('a,b\n1,2\n')
    stray = run_state.inventory(target)
    request = success(state, evidence)
    before = copy.deepcopy(state)
    with pytest.raises(ValueError, match='outside parent sourceChange scope'):
        run_state.advance(state, request)
    expose(caplog, 'advance', True, expected_errors=expected_errors)
    paths = {row['path'] for row in stray['files']}
    assert clean == generated_only and stray['digest'] != clean
    assert {'notes.txt', 'outputs/data.csv'} <= paths and not any(p.startswith(('doxygen_output/', '__pycache__/')) for p in paths)
    assert state == before
    logger.info('[IMP:9][test_unignored_ordinary_file_still_candidate_beside_generated_outputs][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_unignored_ordinary_file_still_candidate_beside_generated_outputs

# region FUNC_commit_fixture [DOMAIN(8): NativeMethodology; CONCEPT(9): OwnedFixture, GitIgnoreRules; TECH(7): subprocess]
## @purpose Give a fixture repository one real commit with the named files, force-added so a tracked file may lie inside an ignored directory, so HEAD, the index and the status observation are non-trivial.
## @uses test_run_state.git
## @io target owned repository Path, paths relative file names under it. Returns None after git add with force and git commit with a fixed test identity and signing off, through the real tool. Side effects: the owned repository only; prints the real commands. Errors: AssertionError when git refuses. Example: committing .gitignore and build/keep.txt makes build/keep.txt a tracked file inside an ignored directory.
## @complexity 2
def commit_fixture(target, *paths):
    # START_BLOCK_BusinessLogic
    git(target, 'add', '-f', *paths)
    git(target, '-c', 'user.name=Fixture', '-c', 'user.email=fixture', '-c', 'commit.gpgsign=false', 'commit', '-q', '-m', 'fixture commit')
    logger.info('[IMP:7][commit_fixture][WRITE] committed=%d', len(paths))
    # END_BLOCK_BusinessLogic
# endregion FUNC_commit_fixture

# region FUNC_arm_fsmonitor [DOMAIN(8): NativeMethodology; CONCEPT(10): HermeticGit, FsmonitorProgram; TECH(7): subprocess, shlex]
## @purpose Configure a marker program as the core.fsmonitor setting of a fixture repository, so any git command that runs the repository-configured program leaves visible proof.
## @uses test_run_state.git, shlex.quote, pathlib.Path.write_text, pathlib.Path.chmod
## @io target owned repository Path, tmp_path owned Path outside the target. Returns the marker Path the program appends to. The program is an executable shell script outside the target that appends one line and exits 1; the setting is written with git config into the repository configuration. Side effects: two files outside the repository and one repository configuration entry. Errors: AssertionError when git refuses. Example: after arming, a plain git ls-files --others creates the marker on a git that runs the program.
## @complexity 3
def arm_fsmonitor(target, tmp_path):
    # START_BLOCK_BusinessLogic
    marker = tmp_path / 'fsmonitor-marker.txt'
    program = tmp_path / 'fsmonitor-program.sh'
    program.write_text('#!/bin/sh\necho "fsmonitor-ran $*" >> ' + shlex.quote(str(marker)) + '\nexit 1\n')
    program.chmod(0o755)
    git(target, 'config', 'core.fsmonitor', shlex.quote(str(program)))
    logger.info('[IMP:7][arm_fsmonitor][WRITE] repository configured with a marker fsmonitor program')
    return marker
    # END_BLOCK_BusinessLogic
# endregion FUNC_arm_fsmonitor

# region FUNC_consume_marker [DOMAIN(8): NativeMethodology; CONCEPT(9): HermeticGit; TECH(7): pathlib]
## @purpose Read and reset the fsmonitor marker so each stage of a test is judged on its own.
## @uses pathlib.Path.is_file, pathlib.Path.unlink
## @io marker Path. Returns True when the marker file existed and removes it, False otherwise. Side effects: deletes the marker file. Errors: OSError on a failing removal. Example: after a stage that ran the program the call returns True and the next call returns False.
## @complexity 1
def consume_marker(marker):
    # START_BLOCK_BusinessLogic
    ran = marker.is_file()
    if ran:
        marker.unlink()
    return ran
    # END_BLOCK_BusinessLogic
# endregion FUNC_consume_marker

# region FUNC_init_arguments [DOMAIN(8): NativeMethodology; CONCEPT(9): RealChannel; TECH(7): subprocess]
## @purpose Build the argument list of the real init command over an owned fixture, so process-level tests start runs the same way.
## @uses str
## @io package, target and plan owned Paths, run_id str. Returns the list of CLI arguments for init with the textual cap 4. Side effects: none. Errors: none. Example: the list starts with init and ends with the cap.
## @complexity 1
def init_arguments(package, target, plan, run_id):
    # START_BLOCK_BusinessLogic
    return ['init', '--project', str(target), '--spec', str(target / 'spec.md'), '--approval', 'structural fixture reference', '--framework', str(package), '--adapter', str(package / 'adapter.json'), '--plan', str(plan), '--run-id', run_id, '--max-debug', '4']
    # END_BLOCK_BusinessLogic
# endregion FUNC_init_arguments

# region FUNC_test_repository_fsmonitor_program_never_runs [DOMAIN(9): NativeMethodology; CONCEPT(10): HermeticGit, FsmonitorProgram; TECH(7): pytest, git, subprocess]
## @purpose Verify that observing a target repository never executes the program the repository configures as core.fsmonitor: not during the real init, show and record commands, not during a direct inventory and not during the baseline observation, while a plain git command in the same repository does run it.
## @uses run_state.inventory, run_state._baseline, test_run_state.arm_fsmonitor, test_run_state.cli, test_run_state.commit_fixture, test_run_state.consume_marker, test_run_state.expose, test_run_state.init_arguments, test_run_state.prepare_git_target, test_run_state.success
## @io Input: tmp_path owned Path, monkeypatch, caplog. Output: None after a positive control (a plain git ls-files in the armed repository creates the marker, otherwise the test is skipped because this git cannot run the program) and then asserting the marker stays absent after init, show, a direct inventory through the record request, record and a direct baseline, with init, show and record exiting 0 and the saved phase architect. Side effects: owned repository with a marker program outside it; three child processes. Errors: AssertionError. Example: before the repair every stage that listed ignored files or read the status left the marker.
## @complexity 6
def test_repository_fsmonitor_program_never_runs(tmp_path, monkeypatch, caplog):
    logger.info('[IMP:4][test_repository_fsmonitor_program_never_runs][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    package, target, plan, evidence = prepare_git_target(tmp_path, monkeypatch)
    commit_fixture(target, '.gitignore', 'spec.md', 'plan.md', 'tests/guide.md')
    marker = arm_fsmonitor(target, tmp_path)
    git(target, 'ls-files', '--others', '--ignored', '--exclude-standard', '--directory', '-z')
    if not consume_marker(marker):
        pytest.skip('this git does not run a configured core.fsmonitor program for ls-files; the property cannot be probed here')
    ran = {}
    initialized = cli(*init_arguments(package, target, plan, 'fsmonitor'), cwd=tmp_path)
    ran['init'] = consume_marker(marker)
    state_file = Path(json.loads(initialized.stdout)['state_file'])
    shown = cli('show', '--state', state_file, cwd=tmp_path)
    ran['show'] = consume_marker(marker)
    state = json.loads(state_file.read_text())
    request = success(state, evidence)
    ran['inventory'] = consume_marker(marker)
    result_path = tmp_path / 'fsmonitor-result.json'
    result_path.write_text(json.dumps(request))
    recorded = cli('record', '--state', state_file, '--result', result_path, cwd=tmp_path)
    ran['record'] = consume_marker(marker)
    baseline = run_state._baseline(target)
    ran['baseline'] = consume_marker(marker)
    expose(caplog, 'inventory')
    print('Actual stages that ran the repository fsmonitor program:', ran)
    assert initialized.returncode == 0 and shown.returncode == 0 and recorded.returncode == 0
    assert json.loads(state_file.read_text())['phase'] == 'architect' and baseline['head']['exit'] == 0
    assert ran == {'init': False, 'show': False, 'inventory': False, 'record': False, 'baseline': False}
    logger.info('[IMP:9][test_repository_fsmonitor_program_never_runs][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_repository_fsmonitor_program_never_runs

# region FUNC_test_foreign_git_environment_leaves_candidate_unchanged [DOMAIN(9): NativeMethodology; CONCEPT(10): HermeticGit, FailOpen, CandidateIdentity; TECH(7): pytest, git, subprocess]
## @purpose Verify that repository-redirecting variables inherited from the caller (a foreign GIT_DIR, GIT_INDEX_FILE or GIT_WORK_TREE) cannot change the candidate or the baseline: a tracked file inside an ignored directory stays candidate content, the mode stays git, and the real show and init commands agree with the clean observation.
## @uses pytest.mark.parametrize, run_state.inventory, run_state._baseline, test_run_state.cli, test_run_state.commit_fixture, test_run_state.git, test_run_state.init_arguments, test_run_state.make_git_fixture
## @io Input: tmp_path owned Path, monkeypatch, caplog, variables tuple of the redirecting names set for the child and the test process. Output: None after taking a clean inventory and baseline, setting the variables to a second owned repository, and asserting the inventory equals the clean one (files, digest, mode git, build/keep.txt present, build/gen.o absent), the baseline equals the clean one with an existing HEAD, the real show exits 0 on the clean ledger with the same digest and a new init under the variables records the clean candidate and the clean baseline. Side effects: two owned repositories and ledgers; two child processes. Errors: AssertionError. Example: before the repair a foreign GIT_DIR dropped build/keep.txt from the candidate.
## @complexity 7
@pytest.mark.parametrize('variables', [('GIT_DIR',), ('GIT_INDEX_FILE',), ('GIT_WORK_TREE',), ('GIT_DIR', 'GIT_INDEX_FILE', 'GIT_WORK_TREE')])
def test_foreign_git_environment_leaves_candidate_unchanged(tmp_path, monkeypatch, caplog, variables):
    logger.info('[IMP:4][test_foreign_git_environment_leaves_candidate_unchanged][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)

    def prepare(target):
        (target / 'build').mkdir()
        (target / 'build/keep.txt').write_text('tracked file inside an ignored directory\n')
        (target / 'build/gen.o').write_text('ignored build output\n')
        commit_fixture(target, '.gitignore', 'spec.md', 'plan.md', 'tests/guide.md', 'build/keep.txt')

    path, state, _ = make_git_fixture(tmp_path, monkeypatch, prepare=prepare, gitignore=GITIGNORE + 'build/\n')
    target = Path(state['target'])
    package = Path(state['framework'])
    foreign = tmp_path / 'foreign'
    foreign.mkdir()
    git(foreign, 'init', '-q')
    (foreign / 'other.txt').write_text('a different repository\n')
    commit_fixture(foreign, 'other.txt')
    redirect = {'GIT_DIR': str(foreign / '.git'), 'GIT_INDEX_FILE': str(foreign / '.git/index'), 'GIT_WORK_TREE': str(foreign)}
    clean = run_state.inventory(target)
    clean_baseline = run_state._baseline(target)
    for name in variables:
        monkeypatch.setenv(name, redirect[name])
    polluted = run_state.inventory(target)
    polluted_baseline = run_state._baseline(target)
    shown = cli('show', '--state', path, cwd=tmp_path)
    initialized = cli(*init_arguments(package, target, Path(state['plan']['path']), 'foreign-env'), cwd=tmp_path)
    expose(caplog, 'inventory')
    paths = {row['path'] for row in polluted['files']}
    print('Actual candidate under', variables, ':', sorted(paths))
    assert polluted == clean and polluted['exclusion_mode'] == 'git'
    assert 'build/keep.txt' in paths and 'build/gen.o' not in paths
    assert polluted_baseline == clean_baseline and clean_baseline['head']['exit'] == 0
    assert shown.returncode == 0 and json.loads(shown.stdout)['state']['candidate']['digest'] == clean['digest']
    assert initialized.returncode == 0
    recorded = json.loads(Path(json.loads(initialized.stdout)['state_file']).read_text())
    assert recorded['candidate'] == clean and recorded['baseline'] == clean_baseline
    logger.info('[IMP:9][test_foreign_git_environment_leaves_candidate_unchanged][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_foreign_git_environment_leaves_candidate_unchanged
