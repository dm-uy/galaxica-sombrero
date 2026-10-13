# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification; TECH(8): Python, StandardLibrary]
## @modulecontract
## @purpose Discriminate bounded visual helper regressions and real CLI stream/read-failure behavior.
## @scope Direct supported/orphan/unknown/uncovered/missing cases, actual0/2 CLI and explicit unsupported/fallback limits.
## @input Explicit owned source/target paths and current canonical records; pytest fixtures supply owned temporary paths for tests. No credentials or provider state.
## @output Importable declared functions, actual CLI answer/diagnostic/exit where applicable, and meaningful test outcomes with actual trace. No fabricated native acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): logging; READS_DATA_FROM(9): explicit path inputs; no environment secrets]
## @invariants
## - Current neutral role/phase/scan/gate owners remain controlling; structural checks never prove human authority or role independence.
## - Test fixtures are isolated, deterministic and order-independent; real package sources remain read-only.
## - Private locators/payloads/credentials are absent from source; logs use safe logical classes/counts.
## @rationale
## Q: Why direct logic and actual CLI tests separately?
## A: Native imports prove bounded logic; real subprocess/file/stream/exit observations prove their actual shipped channel.
## Q: Why preserve unavailable/unsupported limits?
## A: Same-author fixtures and bounded recognizers cannot replace independent source meaning, current maps or actual native smoke.
## @changes
## LAST_CHANGE: [2.0.0 - Current bounded source package and permanent behavioral refusal controls.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => test_visual_gate._module_contract
## FUNC 9[Verify visual gate real controls] => test_visual_gate.test_visual_gate_real_controls
## FUNC 9[Verify visual actual cli and unreadable] => test_visual_gate.test_visual_actual_cli_and_unreadable
## FUNC 9[Verify mixed requirement and unsupported limits] => test_visual_gate.test_mixed_requirement_and_unsupported_limits
## @usecases
## - Parent/test: inspect real current inputs -> accept scoped current outcome or refuse unsafe/malformed/stale input.
## - Independent judge: compare actual assertions/source/CLI receipts -> bounded evidence; native acceptance remains separately owned.
## @GREP_SUMMARY native package, actual source identity, current canonical returns, owned fixtures,
##   real CLI streams, causal budget, refusal and no inferred consent
## @STRUCTURE ▶ explicit owned inputs → ◇ validate actual shape and identity → ○ bounded operation
##   → ⊕ actual observation/assertions → ⎋ current result or honest refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import logging
import os
from pathlib import Path
import subprocess
import sys

import pytest
import visual_gate_lint

logger=logging.getLogger(__name__)
PACKAGE=Path(__file__).resolve().parents[1]


# region FUNC_test_visual_gate_real_controls [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify visual gate real controls over actual owned inputs.
## @uses pytest.mark.parametrize, visual_gate_lint.main
## @io Input: tmp_path: owned pathlib.Path, caplog: pytest.LogCaptureFixture, capsys: pytest.CaptureFixture, graph: case value from the exact parametrization below, spec: case value from the exact parametrization below, expected: case value from the exact parametrization below, label: case value from the exact parametrization below. Cases: pytest.mark.parametrize('graph,spec,expected,label', [('〈one_py satisfies="BR-1"/〉', '- BR-1: valid', 0, 'PASS'), ('〈one_py/〉', '- BR-1: valid', 1, 'SCOPE_CREEP'), ('〈one_py satisfies="AC-1"/〉', '- BR-1: valid', 1, 'SCOPE_CREEP'), ('〈one_py satisfies="BR-2"/〉', '- BR-1: valid', 1, 'UNKNOWN_BR'), ('〈one_py satisfies="BR-1"/〉', '- BR-1: valid⧵n1. BR-2 — uncovered', 1, 'UNCOVERED_REQUIREMENT'), ('〈one_md satisfies="BR-1"/〉', '- BR-1: valid', 2, 'no supported'), ('', '- BR-1: valid', 2, 'no DraftCodeGraph')]). Output: None after these concrete checks: actual == expected and label in captured.out + captured.err; any(('[IMP:9][main][RESULT]' in r.getMessage() for r in caplog.records)); not any((r.levelno 〉= logging.ERROR for r in caplog.records)); any(('[IMP:10][main]' in r.getMessage() for r in caplog.records)); all((r.name == 'visual_gate_lint' for r in caplog.records if r.levelno 〉= logging.ERROR)). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_visual_gate.py::test_visual_gate_real_controls executes these exact cases. Importance:9.
## @complexity 5
@pytest.mark.parametrize('graph,spec,expected,label',[
    ('<one_py satisfies="BR-1"/>','- BR-1: valid',0,'PASS'),
    ('<one_py/>','- BR-1: valid',1,'SCOPE_CREEP'),
    ('<one_py satisfies="AC-1"/>','- BR-1: valid',1,'SCOPE_CREEP'),
    ('<one_py satisfies="BR-2"/>','- BR-1: valid',1,'UNKNOWN_BR'),
    ('<one_py satisfies="BR-1"/>','- BR-1: valid\n1. BR-2 — uncovered',1,'UNCOVERED_REQUIREMENT'),
    ('<one_md satisfies="BR-1"/>','- BR-1: valid',2,'no supported'),
    ('','- BR-1: valid',2,'no DraftCodeGraph'),
])
def test_visual_gate_real_controls(tmp_path,caplog,capsys,graph,spec,expected,label):
    logger.info('[IMP:4][test_visual_gate_real_controls][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    plan=tmp_path/'plan.md';task=tmp_path/'spec.md'
    plan.write_text('<DraftCodeGraph>'+graph+'</DraftCodeGraph>');task.write_text(spec)
    actual=visual_gate_lint.main([str(plan),'--spec',str(task)])
    captured=capsys.readouterr()
    with capsys.disabled():
        print('Actual direct output:',captured.out,captured.err)
        for r in caplog.records:
            if '[IMP:9]' in r.getMessage() or '[IMP:10]' in r.getMessage():print(r.levelname,r.getMessage())
    assert actual==expected and label in captured.out+captured.err
    if expected==0:
        assert any('[IMP:9][main][RESULT]' in r.getMessage() for r in caplog.records)
        assert not any(r.levelno>=logging.ERROR for r in caplog.records)
    else:
        assert any('[IMP:10][main]' in r.getMessage() for r in caplog.records)
        assert all(r.name=='visual_gate_lint' for r in caplog.records if r.levelno>=logging.ERROR)


    logger.info('[IMP:9][test_visual_gate_real_controls][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_visual_gate_real_controls

# region FUNC_test_visual_actual_cli_and_unreadable [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify visual actual cli and unreadable over actual owned inputs.
## @uses subprocess.run
## @io Input: tmp_path: owned pathlib.Path, caplog: pytest.LogCaptureFixture. Cases: no parametrized inputs. Output: None after these concrete checks: good.returncode == 0 and '1 node(s), 2 BR(s)' in good.stdout and ('[IMP:9][main][RESULT]' in good.stderr); bad.returncode == 2 and (not bad.stdout) and ('[IMP:10][main][READ_FAILURE]' in bad.stderr). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_visual_gate.py::test_visual_actual_cli_and_unreadable executes these exact cases. Importance:9.
## @complexity 5
def test_visual_actual_cli_and_unreadable(tmp_path,caplog):
    logger.info('[IMP:4][test_visual_actual_cli_and_unreadable][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    plan=tmp_path/'plan.md';task=tmp_path/'spec.md'
    plan.write_text('<DraftCodeGraph><one_ts satisfies="BR-1, BR-2"/><Link TARGET="existing"/></DraftCodeGraph>')
    task.write_text('### BR-1: first\n2) BR-2 — second\nA prose mention of BR-9 is not declared.\n')
    argv=[sys.executable,str(PACKAGE/'skills/devplan-protocol/scripts/visual_gate_lint.py'),str(plan),'--spec',str(task)]
    good=subprocess.run(argv,cwd=tmp_path,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,capture_output=True)
    print('Actual visual CLI:',argv,'exit',good.returncode,good.stdout,good.stderr)
    assert good.returncode==0 and '1 node(s), 2 BR(s)' in good.stdout and '[IMP:9][main][RESULT]' in good.stderr
    plan.write_bytes(b'\xff')
    bad=subprocess.run(argv,cwd=tmp_path,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,capture_output=True)
    print('Actual visual refusal:',argv,'exit',bad.returncode,bad.stdout,bad.stderr)
    assert bad.returncode==2 and not bad.stdout and '[IMP:10][main][READ_FAILURE]' in bad.stderr
    logger.info('[IMP:9][test_visual_actual_cli_and_unreadable][RESULT] real0/2 channels observed')


    logger.info('[IMP:9][test_visual_actual_cli_and_unreadable][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_visual_actual_cli_and_unreadable

# region FUNC_test_mixed_requirement_and_unsupported_limits [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify mixed requirement and unsupported limits over actual owned inputs.
## @uses visual_gate_lint._NODE_RE.findall, visual_gate_lint._spec_brs
## @io Input: caplog: pytest.LogCaptureFixture. Cases: no parametrized inputs. Output: None after these concrete checks: actual == {'BR-1', 'BR-2', 'BR-3'}; visual_gate_lint._spec_brs('Unstructured prose BR-8') == {'BR-8'}; not visual_gate_lint._NODE_RE.findall('〈ordinary_md satisfies="BR-1"/〉'); not any((r.levelno 〉= logging.ERROR for r in caplog.records)). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_visual_gate.py::test_mixed_requirement_and_unsupported_limits executes these exact cases. Importance:9.
## @complexity 5
def test_mixed_requirement_and_unsupported_limits(caplog):
    logger.info('[IMP:4][test_mixed_requirement_and_unsupported_limits][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    actual=visual_gate_lint._spec_brs('### BR-1: one\n- **BR-2** – two\n3. BR-3 — three\nSee BR-99 in prose.\n')
    print('Actual requirement population:',sorted(actual))
    for r in caplog.records:
        if '[IMP:9]' in r.getMessage():print(r.getMessage())
    assert actual=={'BR-1','BR-2','BR-3'}
    assert visual_gate_lint._spec_brs('Unstructured prose BR-8')=={'BR-8'}
    assert not visual_gate_lint._NODE_RE.findall('<ordinary_md satisfies="BR-1"/>')
    assert not any(r.levelno>=logging.ERROR for r in caplog.records)
    logger.info('[IMP:9][test_mixed_requirement_and_unsupported_limits][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_mixed_requirement_and_unsupported_limits

