# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification; TECH(8): Python, StandardLibrary]
## @modulecontract
## @purpose Discriminate real co-located source resolution and unavailable/stale/unsafe dependency refusals.
## @scope Actual copied package73/neutral71 source corpus, othercwd process and absence/truncation/profile/unknown-member controls.
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
## FUNC 2[Attach full module documentation with no runtime effects] => test_adoption._module_contract
## FUNC 9[Verify colocated adoption and other cwd] => test_adoption.test_colocated_adoption_and_other_cwd
## FUNC 9[Verify actual adoption dependency refusals] => test_adoption.test_actual_adoption_dependency_refusals
## FUNC 9[Verify fake grant and wrong framework no effect] => test_adoption.test_fake_grant_and_wrong_framework_no_effect
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

import json
import logging
from pathlib import Path

import pytest
import run_state
from test_run_state import make_fixture,cli,expose,error_profile

logger=logging.getLogger(__name__)


# region FUNC_test_colocated_adoption_and_other_cwd [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify colocated adoption and other cwd over actual owned inputs.
## @uses json.loads
## @io Input: tmp_path: owned pathlib.Path, caplog: pytest.LogCaptureFixture. Cases: no parametrized inputs. Output: None after these concrete checks: len(state['bindings']['neutral']) == 71 and len(state['bindings']['package']['files']) == 73; Path(state['bindings']['neutral_root']) == Path(state['framework']).parents[1]; relocated.returncode == 0 and json.loads(relocated.stdout)['state']['input_identity'] == state['input_identity']; set(state['bindings']['core']) == {'concepts/principles.md', 'roles/_base.md', 'code/exoskeleton.md', 'code/ldd.md', 'code/doxygen.md', 'code/tests.md'}. AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_adoption.py::test_colocated_adoption_and_other_cwd executes these exact cases. Importance:9.
## @complexity 5
def test_colocated_adoption_and_other_cwd(tmp_path,caplog):
    logger.info('[IMP:4][test_colocated_adoption_and_other_cwd][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);path,state,_=make_fixture(tmp_path)
    assert len(state['bindings']['neutral'])==71 and len(state['bindings']['package']['files'])==73
    assert Path(state['bindings']['neutral_root'])==Path(state['framework']).parents[1]
    relocated=cli('show','--state',path,cwd=tmp_path.parent)
    assert relocated.returncode==0 and json.loads(relocated.stdout)['state']['input_identity']==state['input_identity']
    assert set(state['bindings']['core'])=={'concepts/principles.md','roles/_base.md','code/exoskeleton.md','code/ldd.md','code/doxygen.md','code/tests.md'}
    expose(caplog,'_bindings')


    logger.info('[IMP:9][test_colocated_adoption_and_other_cwd][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_colocated_adoption_and_other_cwd

# region FUNC_test_actual_adoption_dependency_refusals [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify actual adoption dependency refusals and exact caller-declared error episodes over actual owned inputs.
## @uses json.dumps, json.loads, pytest.mark.parametrize, pytest.raises, run_state.validate_state, test_run_state.error_profile, test_run_state.expose
## @io Input: tmp_path: owned pathlib.Path, caplog: pytest.LogCaptureFixture, damage: case value from the exact parametrization below. Cases: pytest.mark.parametrize('damage', ['missing-core', 'stub-core', 'stale-core', 'missing-via', 'detached', 'unsorted', 'wrong-profile', 'wrong-roles', 'unknown-output', 'unknown-runtime']). Output: None after these concrete checks: not (Path(state['target']) / 'source.py').exists(). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_adoption.py::test_actual_adoption_dependency_refusals executes these exact cases. Importance:9.
## @complexity 5
@pytest.mark.parametrize('damage',['missing-core','stub-core','stale-core','missing-via','detached','unsorted','wrong-profile','wrong-roles','unknown-output','unknown-runtime'])
def test_actual_adoption_dependency_refusals(tmp_path,caplog,damage):
    logger.info('[IMP:4][test_actual_adoption_dependency_refusals][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors={
        'missing-core':error_profile(None,'_bindings','validate_state',kind='FileNotFoundError'),
        'stub-core':error_profile('required core missing/stub/basic structure invalid; full-content judgment belongs to parent','_bindings','validate_state'),
        'stale-core':error_profile('required core missing/stub/basic structure invalid; full-content judgment belongs to parent','_bindings','validate_state'),
        'missing-via':error_profile('package membership mismatch','_bindings','validate_state'),
        'detached':error_profile('co-located spec_root must be ../../','_bindings','validate_state'),
        'unsorted':error_profile('invalid package member declarations','_bindings','validate_state'),
        'wrong-profile':error_profile('unsupported package profile','_bindings','validate_state'),
        'wrong-roles':error_profile('package role locations mismatch','_bindings','validate_state'),
        'unknown-output':error_profile('package membership mismatch','_bindings','validate_state'),
        'unknown-runtime':error_profile('package membership mismatch','_bindings','validate_state')}[damage]
    caplog.set_level(logging.INFO);_,state,_=make_fixture(tmp_path);framework=Path(state['framework']);neutral=Path(state['bindings']['neutral_root']);adapter=framework/'adapter.json';layout=framework/'references/package-layout.json'
    if damage=='missing-core':(neutral/'code/ldd.md').unlink()
    elif damage=='stub-core':(neutral/'code/ldd.md').write_text('---\nid: code.ldd\ntitle: LDD\nstatus: stub\n---\n')
    elif damage=='stale-core':(neutral/'code/ldd.md').write_text((neutral/'code/ldd.md').read_text()[:400])
    elif damage=='missing-via':(framework/'references/adoption.md').unlink()
    elif damage=='detached':
        data=json.loads(adapter.read_text());data['spec_root']='missing';adapter.write_text(json.dumps(data))
    elif damage in {'unsorted','wrong-profile','wrong-roles'}:
        data=json.loads(layout.read_text())
        if damage=='unsorted':data['files'].reverse()
        elif damage=='wrong-profile':data['profile']='installed-offline'
        else:data['roles']['qa']='roles/coder.md'
        layout.write_text(json.dumps(data))
    else:
        folder=framework/('output' if damage=='unknown-output' else '.methodology');folder.mkdir();(folder/'extra.txt').write_text('Unknown published member must not escape package binding.\n')
    with pytest.raises((ValueError,OSError)):
        run_state.validate_state(state)
    assert not (Path(state['target'])/'source.py').exists()
    expose(caplog,'validate_state',True,expected_errors=expected_errors)


    logger.info('[IMP:9][test_actual_adoption_dependency_refusals][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_actual_adoption_dependency_refusals

# region FUNC_test_fake_grant_and_wrong_framework_no_effect [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify fake grant and wrong framework no effect with exact ordered expected errors.
## @uses pytest.raises, run_state.initialize, test_run_state.error_profile, test_run_state.expose
## @io Input: tmp_path: owned pathlib.Path, caplog: pytest.LogCaptureFixture. Cases: no parametrized inputs. Output: None after these concrete checks: not (target / '.methodology').exists(); not (target / '.methodology').exists(). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_adoption.py::test_fake_grant_and_wrong_framework_no_effect executes these exact cases. Importance:9.
## @complexity 5
def test_fake_grant_and_wrong_framework_no_effect(tmp_path,caplog):
    logger.info('[IMP:4][test_fake_grant_and_wrong_framework_no_effect][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    expected_errors=error_profile('authentic parent approval reference required','_text','initialize')+error_profile(None,'read_json','_bindings','initialize',kind='FileNotFoundError')
    caplog.set_level(logging.INFO);_,state,_=make_fixture(tmp_path)
    target=tmp_path/'second';target.mkdir();(target/'spec.md').write_text('Owned fixture only.\n')
    with pytest.raises(ValueError,match='approval'):
        run_state.initialize(target,target/'spec.md','', 'fake',framework=state['framework'],adapter=state['adapter_path'],plan=target/'plan.md')
    assert not (target/'.methodology').exists()
    wrong=tmp_path/'old-framework';wrong.mkdir()
    with pytest.raises((ValueError,OSError)):
        run_state.initialize(target,target/'spec.md','structural fixture reference', 'wrong',framework=wrong,adapter=wrong/'adapter.json',plan=target/'plan.md')
    assert not (target/'.methodology').exists()
    expose(caplog,'initialize',True,expected_errors=expected_errors)
    logger.info('[IMP:9][test_fake_grant_and_wrong_framework_no_effect][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_fake_grant_and_wrong_framework_no_effect

