# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): BoundedVerification, VisualGate; TECH(8): Python, pytest]
## @modulecontract
## @purpose Verify that the packaged visual gate helper reports supported-node requirement coverage correctly and delivers its real 0/1/2 CLI channels, so an Architect plan is never passed on an orphan, unknown or uncovered requirement.
## @scope Direct supported, orphan, unknown, uncovered and missing-graph cases; a real CLI process with exit 0 and exit 2; the specification-less and argument-refusal paths; the explicit unsupported-carrier and loose-fallback limits.
## @input Owned pytest tmp_path plan and specification files and the real package script; no credentials or provider state.
## @output Pass or fail outcomes with the actual helper output and the IMP 9 and 10 trace printed; no fabricated semantic or native acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): subprocess; USES_API(7): contextlib; USES_API(8): logging; USES_API(7): pytest; READS_DATA_FROM(9): skills/devplan-protocol/scripts/visual_gate_lint.py]
## @links_to_spec AC-M22-3 visual gate lint; BR-4 flow mechanics
## @invariants
## - Fixtures are isolated, deterministic and order-independent; the real package sources stay read-only.
## - Each test prints the observed helper output and the IMP 9 and 10 trace before it asserts on them.
## - The suite proves only the bounded recognizer; full XML, Mermaid and semantic coverage stay independent judgments.
## @rationale
## Q: Why direct calls and a real subprocess separately?
## A: Direct calls prove the bounded logic with the caller-visible trace; the subprocess proves the shipped channel: argv, stdout report, stderr trace and exit code.
## Q: Why keep the unsupported-carrier and loose-fallback cases?
## A: They are the documented limits of a suffix recognizer; pinning them prevents a silent widening that would claim coverage the helper cannot judge.
## @changes
## LAST_CHANGE: [1.0.0 - Port of the sibling package visual gate suite to the Claude Code package, plus the specification-less and argument-refusal paths.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => test_visual_gate._module_contract
## FUNC 8[Run the helper main with captured streams and print what was observed] => test_visual_gate.run_main
## FUNC 9[Seven verdict cases: pass, orphan, non-BR satisfies, unknown BR, uncovered BR, unsupported carrier, missing graph] => test_visual_gate.test_visual_gate_real_controls
## FUNC 9[Real CLI process: exit 0 report and exit 2 unreadable plan] => test_visual_gate.test_visual_actual_cli_and_unreadable
## FUNC 9[Mixed BR declaration furniture, loose fallback and unsupported suffix] => test_visual_gate.test_mixed_requirement_and_unsupported_limits
## FUNC 9[Plan-only pass, argument refusal and help] => test_visual_gate.test_plan_only_and_argument_paths
## @usecases
## - [AC-M22-3]: Maintainer → change the recognizer → test_visual_gate_real_controls keeps all seven verdicts
## - [AC-M22-3]: Architect → run the shipped script → test_visual_actual_cli_and_unreadable observes exit 0 and exit 2 channels
## - [AC-M22-3]: Reviewer → compare declared BR grammar → test_mixed_requirement_and_unsupported_limits pins the grammar and its limits
## - [AC-M22-3]: Architect → run without a specification or with bad arguments → test_plan_only_and_argument_paths keeps those exits
## @GREP_SUMMARY visual gate tests, DraftCodeGraph, BR coverage, SCOPE_CREEP, UNKNOWN_BR, UNCOVERED_REQUIREMENT,
##   real CLI exit 0/1/2, unsupported carrier, loose fallback, owned fixtures, Claude Code package
## @STRUCTURE ▶ owned plan + spec → ○ helper main or real subprocess → ⊕ printed output + IMP trace
##   → ◇ exit code and violation label → ⎋ bounded verdict
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import contextlib
import io
import logging
import os
from pathlib import Path
import subprocess
import sys

import pytest
import visual_gate_lint

logger = logging.getLogger(__name__)
PACKAGE = Path(__file__).resolve().parents[1]
SCRIPT = PACKAGE / 'skills/devplan-protocol/scripts/visual_gate_lint.py'


# region FUNC_run_main [DOMAIN(8): NativeMethodology; CONCEPT(8): BoundedVerification; TECH(7): contextlib, pytest]
## @purpose Let a test observe the helper main exit code, stdout, stderr and IMP 9/10 trace together, and print them before any assertion.
## @uses visual_gate_lint.main, contextlib.redirect_stdout, contextlib.redirect_stderr, io.StringIO
## @io argv list of str passed to main; caplog pytest LogCaptureFixture. Returns tuple of exit int, stdout str, stderr str. Prints the three values and every IMP 9 or IMP 10 record before returning. Side effects: none beyond the helper own reads; no file writes. Errors: SystemExit from argparse is converted by the helper into its returned code, so nothing is raised. Example: run_main of a plan path with a clean graph returns exit 0 and a PASS line.
## @complexity 3
def run_main(argv, caplog):
    logger.info('[IMP:4][run_main][START] observe helper main with captured streams')
    # START_BLOCK_BusinessLogic
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = visual_gate_lint.main(argv)
    print('Actual direct output:', code, repr(out.getvalue()), repr(err.getvalue()))
    for record in caplog.records:
        message = record.getMessage()
        if '[IMP:9]' in message or '[IMP:10]' in message:
            print(record.name, record.levelname, message)
    logger.info('[IMP:9][run_main][RESULT] exit=%d', code)
    return code, out.getvalue(), err.getvalue()
    # END_BLOCK_BusinessLogic
# endregion FUNC_run_main

# region FUNC_test_visual_gate_real_controls [DOMAIN(8): NativeMethodology; CONCEPT(9): BoundedVerification; TECH(7): pytest, parametrize]
## @purpose Verify that each of seven plan and specification pairs yields exactly its documented exit code and violation label, with the owning trace.
## @uses pytest.mark.parametrize, test_visual_gate.run_main, visual_gate_lint.main
## @io Input: tmp_path owned Path, caplog LogCaptureFixture, graph str, spec str, expected int, label str from the seven parametrized cases (pass, SCOPE_CREEP without satisfies, SCOPE_CREEP with a non-BR satisfies, UNKNOWN_BR, UNCOVERED_REQUIREMENT, unsupported suffix, missing graph). Output: None after asserting exit equals expected and the label appears in the output; a clean run emits IMP 9 RESULT and no error record; a refusal emits an IMP 10 main record and only visual_gate_lint errors. Side effects: writes two files under tmp_path only. Errors: AssertionError on any mismatch. Example: a one_py node satisfying BR-1 against a spec declaring BR-1 returns 0 and PASS.
## @complexity 5
@pytest.mark.parametrize('graph,spec,expected,label', [
    ('<one_py satisfies="BR-1"/>', '- BR-1: valid', 0, 'PASS'),
    ('<one_py/>', '- BR-1: valid', 1, 'SCOPE_CREEP'),
    ('<one_py satisfies="AC-1"/>', '- BR-1: valid', 1, 'SCOPE_CREEP'),
    ('<one_py satisfies="BR-2"/>', '- BR-1: valid', 1, 'UNKNOWN_BR'),
    ('<one_py satisfies="BR-1"/>', '- BR-1: valid\n1. BR-2 — uncovered', 1, 'UNCOVERED_REQUIREMENT'),
    ('<one_md satisfies="BR-1"/>', '- BR-1: valid', 2, 'no supported'),
    ('', '- BR-1: valid', 2, 'no DraftCodeGraph'),
])
def test_visual_gate_real_controls(tmp_path, caplog, graph, spec, expected, label):
    logger.info('[IMP:4][test_visual_gate_real_controls][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    plan = tmp_path / 'plan.md'
    task = tmp_path / 'spec.md'
    plan.write_text('<DraftCodeGraph>' + graph + '</DraftCodeGraph>')
    task.write_text(spec)
    actual, out, err = run_main([str(plan), '--spec', str(task)], caplog)
    assert actual == expected and label in out + err
    if expected == 0:
        assert any('[IMP:9][main][RESULT]' in r.getMessage() for r in caplog.records)
        assert not any(r.levelno >= logging.ERROR for r in caplog.records)
    else:
        assert any('[IMP:10][main]' in r.getMessage() for r in caplog.records)
        assert all(r.name == 'visual_gate_lint' for r in caplog.records if r.levelno >= logging.ERROR)
    logger.info('[IMP:9][test_visual_gate_real_controls][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_visual_gate_real_controls

# region FUNC_test_visual_actual_cli_and_unreadable [DOMAIN(8): NativeMethodology; CONCEPT(9): BoundedVerification; TECH(7): subprocess, pytest]
## @purpose Verify that the shipped script delivers its real exit 0 report with the IMP 9 trace and its exit 2 refusal for an unreadable plan with the IMP 10 READ_FAILURE trace, through real process streams.
## @uses subprocess.run, sys.executable, os.environ
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Launches the real script on an owned plan with a ts node satisfying BR-1 and BR-2 against a spec declaring those two, then on a plan holding one invalid UTF-8 byte. Output: None after asserting exit 0, the 1 node and 2 BR report on stdout and the RESULT trace on stderr for the first run, and exit 2, empty stdout and the READ_FAILURE trace on stderr for the second. Side effects: child processes run with PYTHONDONTWRITEBYTECODE; files only under tmp_path. Errors: AssertionError on mismatch; OSError if the interpreter cannot start. Example: the first run prints VISUAL GATE PASS with 1 node and 2 BR covered.
## @complexity 5
def test_visual_actual_cli_and_unreadable(tmp_path, caplog):
    logger.info('[IMP:4][test_visual_actual_cli_and_unreadable][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    plan = tmp_path / 'plan.md'
    task = tmp_path / 'spec.md'
    plan.write_text('<DraftCodeGraph><one_ts satisfies="BR-1, BR-2"/><Link TARGET="existing"/></DraftCodeGraph>')
    task.write_text('### BR-1: first\n2) BR-2 — second\nA prose mention of BR-9 is not declared.\n')
    argv = [sys.executable, str(SCRIPT), str(plan), '--spec', str(task)]
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    good = subprocess.run(argv, cwd=tmp_path, env=environment, text=True, capture_output=True)
    print('Actual visual CLI:', argv, 'exit', good.returncode, good.stdout, good.stderr)
    plan.write_bytes(b'\xff')
    bad = subprocess.run(argv, cwd=tmp_path, env=environment, text=True, capture_output=True)
    print('Actual visual refusal:', argv, 'exit', bad.returncode, bad.stdout, bad.stderr)
    assert good.returncode == 0 and '1 node(s), 2 BR(s)' in good.stdout and '[IMP:9][main][RESULT]' in good.stderr
    assert bad.returncode == 2 and not bad.stdout and '[IMP:10][main][READ_FAILURE]' in bad.stderr
    logger.info('[IMP:9][test_visual_actual_cli_and_unreadable][RESULT] real 0/2 channels observed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_visual_actual_cli_and_unreadable

# region FUNC_test_mixed_requirement_and_unsupported_limits [DOMAIN(8): NativeMethodology; CONCEPT(9): BoundedVerification; TECH(7): pytest, regex]
## @purpose Pin the declared BR grammar over mixed heading, bold, ordered-list and prose forms, the loose fallback when nothing is declared, and the unsupported suffix limit.
## @uses visual_gate_lint._spec_brs, visual_gate_lint._NODE_RE
## @io Input: caplog LogCaptureFixture. Output: None after asserting that heading, bold and ordered-list declarations yield BR-1, BR-2 and BR-3 while a prose mention of BR-99 is ignored, that a text with no declaration falls back to the single prose BR-8, that an ordinary md node is not a supported carrier, and that no error record was emitted. Side effects: none. Errors: AssertionError on mismatch. Example: the text Unstructured prose BR-8 selects the set containing BR-8.
## @complexity 4
def test_mixed_requirement_and_unsupported_limits(caplog):
    logger.info('[IMP:4][test_mixed_requirement_and_unsupported_limits][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    actual = visual_gate_lint._spec_brs('### BR-1: one\n- **BR-2** – two\n3. BR-3 — three\nSee BR-99 in prose.\n')
    fallback = visual_gate_lint._spec_brs('Unstructured prose BR-8')
    print('Actual requirement population:', sorted(actual), sorted(fallback))
    for record in caplog.records:
        if '[IMP:9]' in record.getMessage():
            print(record.getMessage())
    assert actual == {'BR-1', 'BR-2', 'BR-3'}
    assert fallback == {'BR-8'}
    assert not visual_gate_lint._NODE_RE.findall('<ordinary_md satisfies="BR-1"/>')
    assert not any(r.levelno >= logging.ERROR for r in caplog.records)
    logger.info('[IMP:9][test_mixed_requirement_and_unsupported_limits][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_mixed_requirement_and_unsupported_limits

# region FUNC_test_plan_only_and_argument_paths [DOMAIN(8): NativeMethodology; CONCEPT(9): BoundedVerification; TECH(7): pytest, argparse]
## @purpose Verify the paths the verdict cases do not reach: a plan checked without a specification passes on orphan-free nodes, a missing plan argument is refused with exit 2, and help is delivered with exit 0.
## @uses test_visual_gate.run_main, visual_gate_lint.main
## @io Input: tmp_path owned Path, caplog LogCaptureFixture. Output: None after asserting exit 0 and a PASS line with 1 node and 1 BR for a plan-only run; exit 2 with the ARGUMENT_REFUSAL trace when the plan argument is absent; exit 0 with the HELP trace for the help flag. Side effects: one plan file under tmp_path; argparse usage text goes to the captured streams. Errors: AssertionError on mismatch. Example: main of an empty argument list returns 2.
## @complexity 4
def test_plan_only_and_argument_paths(tmp_path, caplog):
    logger.info('[IMP:4][test_plan_only_and_argument_paths][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    plan = tmp_path / 'plan.md'
    plan.write_text('<DraftCodeGraph><one_py satisfies="BR-1"/></DraftCodeGraph>')
    passed = run_main([str(plan)], caplog)
    refused = run_main([], caplog)
    helped = run_main(['--help'], caplog)
    messages = [r.getMessage() for r in caplog.records]
    assert passed[0] == 0 and '1 node(s), 1 BR(s)' in passed[1]
    assert refused[0] == 2 and '[IMP:10][main][ARGUMENT_REFUSAL] invalid CLI arguments' in messages
    assert helped[0] == 0 and '[IMP:9][main][HELP] declared usage delivered' in messages
    logger.info('[IMP:9][test_plan_only_and_argument_paths][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_plan_only_and_argument_paths
