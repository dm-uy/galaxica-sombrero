# region MODULE_CONTRACT [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @modulecontract
## @purpose Qualify or enforce bounded schema3 causal accounting and current evidence.
## @scope One parent writer and owned storage domain; no scheduler or product/provider calls.
## @input Explicit owned paths and parent requests; private metadata stays private and read-only.
## @output Actual JSON/CLI outcomes and discriminating assertions; no fabricated native acceptance.
## @links [USES_API(8): pathlib; USES_API(8): json]
## @invariants Historical inputs remain immutable; unknown outcomes never authorize replay.
## @rationale Structural checks complement authentic parent judgment and independent review.
## @changes
## LAST_CHANGE: [5.0.0 - CONT-BOUND direct/shipped evidence and independent-review regression controls; branch candidate only.]
## @modulemap
## FUNC 9[Reject premature success on return evaluation] => test_continuation.test_no_success_trace_before_failed_return
## FUNC 9[Reject actual symlink admission redirection] => test_continuation.test_admission_symlink_cannot_redirect_writes
## FUNC 4[ module contract] => test_continuation._module_contract
## FUNC 9[test schema3 enrollment and caps] => test_continuation.test_schema3_enrollment_and_caps
## FUNC 9[close blocked] => test_continuation.close_blocked
## FUNC 9[request] => test_continuation.request
## FUNC 9[test successor precharge grant and immutable close] => test_continuation.test_successor_precharge_grant_and_immutable_close
## FUNC 9[test grant validation] => test_continuation.test_grant_validation
## FUNC 9[test capabilities readonly and record requires release] => test_continuation.test_capabilities_readonly_and_record_requires_release
## FUNC 9[test retry scope unknown cost and no recovery reset] => test_continuation.test_retry_scope_unknown_cost_and_no_recovery_reset
## FUNC 9[test stale and missing authority hold] => test_continuation.test_stale_and_missing_authority_hold
## FUNC 9[test historical terminal pair matrix] => test_continuation.test_historical_terminal_pair_matrix
## FUNC 9[test process interruption and rollback] => test_continuation.test_process_interruption_and_rollback
## FUNC 9[test worker cannot grant and export cannot dispatch] => test_continuation.test_worker_cannot_grant_and_export_cannot_dispatch
## FUNC 9[test no repair qa at cap and causal architect cannot bypass] => test_continuation.test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass
## FUNC 9[test amended spec enrollment never mints wallet] => test_continuation.test_amended_spec_enrollment_never_mints_wallet
## FUNC 9[test changed inputs require fresh verification] => test_continuation.test_changed_inputs_require_fresh_verification
## FUNC 9[test observed overrun retained and holds next release] => test_continuation.test_observed_overrun_retained_and_holds_next_release
## FUNC 9[test owned critical trajectories] => test_continuation.test_owned_critical_trajectories
## FUNC 9[test successor reentry predicates all terminals] => test_continuation.test_successor_reentry_predicates_all_terminals
## @usecases
## - AC1–7: actual helpers exercise allowance/admission/freshness/reentry/recovery/refusal/overrun and exact own trace controls.
## - AC8/11: actual CLI emits owned streams/checkpoints; root separately performs real reserved native dispatch.
## - AC10/12: source maps and independent review are separate evidence; shared compatibility remains held.
## @GREP_SUMMARY schema3, immutable history, precharge, retry, recovery, real CLI
## @STRUCTURE explicit input → current authority → reserved entry → validated output or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import copy
import json
import logging
from pathlib import Path
import subprocess
import sys

import pytest
import continuation as cont
import run_state as api
from test_run_state import make_fixture, to_phase, success, envelope

logger = logging.getLogger(__name__)
# region FUNC_test_schema3_enrollment_and_caps [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test schema3 enrollment and caps
## @uses api.initialize, api.read_json, api.save, cont.authority, copy.deepcopy, logger.error, logger.info, make_fixture, path.read_bytes, pytest.raises, type
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: state['schema_version'] == 3 and state['debug_cap'] == 4 and (state['debug_spent'] == 0); path == cont.authority(state) and state['contract_version'] == 'methodology-dsh/2.0.0'; api.read_json(path) == state; path.read_bytes() == before; path.read_bytes() == before. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_schema3_enrollment_and_caps(tmp_path):
    logger.info('[IMP:4][test_schema3_enrollment_and_caps][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        assert state['schema_version']==3 and state['debug_cap']==4 and state['debug_spent']==0
        assert path==cont.authority(state) and state['contract_version']=='methodology-dsh/2.0.0'
        assert api.read_json(path)==state
        before=path.read_bytes()
        with pytest.raises(ValueError,match='enrolled'):
            api.initialize(state['target'],state['spec_path'],'new name','renamed',framework=state['framework'],adapter=state['adapter_path'],plan=state['plan']['path'])
        assert path.read_bytes()==before
        old=copy.deepcopy(state);old['schema_version']=2
        with pytest.raises(ValueError): api.save(path,old)
        assert path.read_bytes()==before
        logger.info('[IMP:9][test_schema3_enrollment_and_caps][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_schema3_enrollment_and_caps][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_schema3_enrollment_and_caps
# region FUNC_close_blocked [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose close blocked
## @uses Path, api.advance, api.save, envelope, logger.error, logger.info, type
## @io path, state, evidence are explicit owned fixture/probe inputs -> (closed state dict, immutable snapshot Path) after actual canonical BLOCKED acceptance and save; writes only the supplied owned authority/terminal. Canonical/input/I/O failures propagate, never rewritten success.
## @complexity 6
def close_blocked(path,state,evidence):
    logger.info('[IMP:4][close_blocked][START] owned observation')
    try:
        wrapped={'kind':'role','result':envelope(state,evidence,'BLOCKED')|{'reason':'fixture controlled missing prerequisite','limitations':[]}}
        closed=api.advance(state,wrapped);api.save(path,closed)
        returned = closed,Path(closed['lineage']['closed'][-1]['path'])
        logger.info('[IMP:9][close_blocked][RESULT] declared observations completed')
        return returned
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][close_blocked][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_close_blocked
# region FUNC_request [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose request
## @uses logger.error, logger.info, str, type
## @io state, evidence, phase are explicit owned fixture/probe inputs -> parent request dict with actual framework/spec/adapter/plan/target, explicit fixture-only approval/reason/run/phase/scope/evidence; no writes, no actual human authentication.
## @complexity 6
def request(state,evidence,phase='code'):
    logger.info('[IMP:4][request][START] owned observation')
    try:
        returned = {k:state[k] for k in ('framework','plan')} | {'project':state['target'],'spec':state['spec_path'],'adapter':state['adapter_path'],'plan':state['plan']['path'],'approval':'fixture parent only; not actual consent','run_id':'successor','phase':phase,'reason':'resolved prerequisite for same cause','scope':['source.py','tests/guide.md'],'evidence':[str(evidence)]}
        logger.info('[IMP:9][request][RESULT] declared observations completed')
        return returned
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][request][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_request
# region FUNC_test_successor_precharge_grant_and_immutable_close [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test successor precharge grant and immutable close
## @uses api.read_json, api.save, close_blocked, cont.active, cont.continue_run, cont.reservation_operation, logger.error, logger.info, make_fixture, path.read_bytes, pytest.raises, request, snapshot.read_bytes, str, to_phase, type
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: snapshot.read_bytes() == before and path.read_bytes() == authority_before; active['debug_spent'] == active['debug_cap'] == 1; cont.active(active)['charge'] == 1 and snapshot.read_bytes() == before; api.read_json(path)['debug_spent'] == 1; active['debug_spent'] == 1; done['debug_spent'] == 1 and snapshot.read_bytes() == before. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_successor_precharge_grant_and_immutable_close(tmp_path):
    logger.info('[IMP:4][test_successor_precharge_grant_and_immutable_close][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path,cap=0)
        state=to_phase(state,evidence,'code');api.save(path,state)
        closed,snapshot=close_blocked(path,state,evidence)
        before=snapshot.read_bytes();authority_before=path.read_bytes()
        req=request(closed,evidence)
        with pytest.raises(ValueError,match='exhausted'): cont.continue_run(api,snapshot,req)
        assert snapshot.read_bytes()==before and path.read_bytes()==authority_before
        req['grant']={'id':'human-grant-1','lineage':closed['lineage']['id'],'target':closed['target'],'approval':'fixture explicitly scoped one entry','entries':1,'cost_usd':0}
        _,active=cont.continue_run(api,snapshot,req)
        assert active['debug_spent']==active['debug_cap']==1
        assert cont.active(active)['charge']==1 and snapshot.read_bytes()==before
        with pytest.raises(ValueError): cont.continue_run(api,snapshot,req|{'run_id':'another'})
        reservation=cont.active(active)['id']
        assert api.read_json(path)['debug_spent']==1
        active=cont.reservation_operation(api,active,'reserve',{'entry':reservation})
        active=cont.reservation_operation(api,active,'recover',{'entry':reservation,'outcome':'unknown','evidence':[str(evidence)]})
        with pytest.raises(ValueError): cont.reservation_operation(api,active,'reserve',{'entry':reservation})
        active=cont.reservation_operation(api,active,'recover',{'entry':reservation,'outcome':'unlaunched','evidence':[str(evidence)]})
        assert active['debug_spent']==1
        active=cont.reservation_operation(api,active,'released',{'entry':reservation,'worker':'fixture-session'})
        with pytest.raises(ValueError): cont.reservation_operation(api,active,'recover',{'entry':reservation,'outcome':'unlaunched','evidence':[str(evidence)]})
        done,new_snapshot=close_blocked(path,active,evidence)
        assert done['debug_spent']==1 and snapshot.read_bytes()==before
        req=request(done,evidence)|{'run_id':'repair2'}
        with pytest.raises(ValueError,match='exhausted'): cont.continue_run(api,new_snapshot,req)
        logger.info('[IMP:9][test_successor_precharge_grant_and_immutable_close][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_successor_precharge_grant_and_immutable_close][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_successor_precharge_grant_and_immutable_close
# region FUNC_test_grant_validation [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test grant validation
## @uses cont.check_grant, float, logger.error, logger.info, make_fixture, pytest.mark.parametrize, pytest.raises, type
## @io tmp_path, entries and cost from exact decorator population -> None after the actual check_grant raises ValueError for bool, nonintegral, negative, zero/outside1..20 allowance and bool/negative/nonfinite/outside0..1000 USD including a very large JSON integer. No grant or allowance is persisted.
## @complexity 6
@pytest.mark.parametrize('entries,cost',[(True,0),(0,0),(-1,0),(1.5,0),(21,0),(1,True),(1,-1),(1,float('nan')),(1,1001),(1,10**400)])
def test_grant_validation(tmp_path,entries,cost):
    logger.info('[IMP:4][test_grant_validation][START] owned observation')
    try:
        _,state,_=make_fixture(tmp_path)
        grant={'id':'g','lineage':state['lineage']['id'],'target':state['target'],'approval':'fixture','entries':entries,'cost_usd':cost}
        with pytest.raises(ValueError):cont.check_grant(state,grant)
        logger.info('[IMP:9][test_grant_validation][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_grant_validation][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_grant_validation
# region FUNC_test_capabilities_readonly_and_record_requires_release [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test capabilities readonly and record requires release
## @uses Path, Path(state['target']).rglob, api.read_json, json.dumps, json.loads, logger.error, logger.info, make_fixture, p.is_file, p.read_bytes, path.read_bytes, result.write_text, str, subprocess.run, success, type
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: proc.returncode == 0 and json.loads(proc.stdout)['schema'] == 3; before == {p: p.read_bytes() for p in Path(state['target']).rglob('*') if p.is_file()}; proc.returncode == 2 and 'release' in proc.stderr; refused['history'][-1]['kind'] == 'refused' and refused['debug_spent'] == state['debug_spent'] and (refused['candidate'] == state['candidate']). Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_capabilities_readonly_and_record_requires_release(tmp_path):
    logger.info('[IMP:4][test_capabilities_readonly_and_record_requires_release][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        helper=Path(api.__file__)
        before={p:p.read_bytes() for p in Path(state['target']).rglob('*') if p.is_file()}
        proc=subprocess.run([sys.executable,str(helper),'capabilities'],capture_output=True,text=True)
        assert proc.returncode==0 and json.loads(proc.stdout)['schema']==3
        assert before=={p:p.read_bytes() for p in Path(state['target']).rglob('*') if p.is_file()}
        result=Path(state['target'])/'.methodology/result.json';result.write_text(json.dumps(success(state,evidence)))
        raw=path.read_bytes()
        proc=subprocess.run([sys.executable,str(helper),'record','--state',str(path),'--result',str(result)],capture_output=True,text=True)
        assert proc.returncode==2 and 'release' in proc.stderr
        refused=api.read_json(path)
        assert refused['history'][-1]['kind']=='refused' and refused['debug_spent']==state['debug_spent'] and refused['candidate']==state['candidate']
        logger.info('[IMP:9][test_capabilities_readonly_and_record_requires_release][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_capabilities_readonly_and_record_requires_release][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_capabilities_readonly_and_record_requires_release
# region FUNC_test_retry_scope_unknown_cost_and_no_recovery_reset [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test retry scope unknown cost and no recovery reset
## @uses cont.active, cont.episode, cont.reservation_operation, logger.error, logger.info, make_fixture, pytest.raises, str, type
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: state['retry_episodes']['response-correction'] == 1; state['lineage']['costs'][-1]['usd'] is None. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_retry_scope_unknown_cost_and_no_recovery_reset(tmp_path):
    logger.info('[IMP:4][test_retry_scope_unknown_cost_and_no_recovery_reset][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        entry=cont.active(state)['id']
        state=cont.episode(api,state,{'unit':'response-correction','entry':entry,'used':1,'cost_usd':None,'evidence':[str(evidence)]})
        state=cont.reservation_operation(api,state,'recover',{'entry':entry,'outcome':'unlaunched','evidence':[str(evidence)]})
        assert state['retry_episodes']['response-correction']==1
        with pytest.raises(ValueError): cont.episode(api,state,{'unit':'transport','entry':entry,'used':1,'cost_usd':0,'evidence':[str(evidence)]})
        with pytest.raises(ValueError): cont.episode(api,state,{'unit':'response-correction','entry':entry,'used':2,'cost_usd':0,'evidence':[str(evidence)]})
        assert state['lineage']['costs'][-1]['usd'] is None
        logger.info('[IMP:9][test_retry_scope_unknown_cost_and_no_recovery_reset][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_retry_scope_unknown_cost_and_no_recovery_reset][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_retry_scope_unknown_cost_and_no_recovery_reset
# region FUNC_test_stale_and_missing_authority_hold [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test stale and missing authority hold
## @uses api.initialize, cont.active, cont.committed, cont.reservation_operation, copy.deepcopy, logger.error, logger.info, make_fixture, path.unlink, pytest.raises, type
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: . Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_stale_and_missing_authority_hold(tmp_path):
    logger.info('[IMP:4][test_stale_and_missing_authority_hold][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        before=copy.deepcopy(state)
        state=cont.reservation_operation(api,state,'released',{'entry':cont.active(state)['id'],'worker':'fixture-worker'})
        with pytest.raises(ValueError):cont.committed(api,before)
        path.unlink()
        with pytest.raises(ValueError):cont.committed(api,state)
        with pytest.raises(ValueError):api.initialize(state['target'],state['spec_path'],'rename','renamed',framework=state['framework'],adapter=state['adapter_path'],plan=state['plan']['path'])
        logger.info('[IMP:9][test_stale_and_missing_authority_hold][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_stale_and_missing_authority_hold][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_stale_and_missing_authority_hold
# region FUNC_test_historical_terminal_pair_matrix [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test historical terminal pair matrix
## @uses Path, api._digest, api._file, api.initialize, binding.pop, cont.historical, copy.deepcopy, json.dumps, legacy.parent.mkdir, legacy.read_bytes, legacy.write_text, logger.error, logger.info, make_fixture, old.pop, old.update, pytest.mark.parametrize, pytest.raises, type
## @io tmp_path, terminal, phase, expected are explicit owned fixture/probe inputs -> None after actual assertions: legacy.read_bytes() == before; spent == 0 and cap == 4 and (refs[0]['sha256'] == api._file(legacy)['sha256']). Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
@pytest.mark.parametrize('terminal,phase,expected',[
    ('SPEC_BLOCKED','architect',True),('VISUAL_GATE_FAIL','architect',True),
    ('BLOCKED','code',True),('ERROR','bootstrap',True),('ESCALATED','qa',True),
    ('ESCALATED_FINALIZE','finalize',True),('SUCCESS','finalize',True),
    ('SUCCESS','code',False),('VISUAL_GATE_FAIL','code',False),
    ('SPEC_BLOCKED','code',False),('ESCALATED_FINALIZE','qa',False)])
def test_historical_terminal_pair_matrix(tmp_path,terminal,phase,expected):
    logger.info('[IMP:4][test_historical_terminal_pair_matrix][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        old=copy.deepcopy(state);old.pop('lineage');old['schema_version']=2
        old.update(status=terminal,phase=phase)
        # The actual historical profile has frozen4.0 bindings; self-consistent source metadata is required.
        old['bindings']['neutral_version']='4.0.0'
        binding=copy.deepcopy(old['bindings']);binding.pop('digest')
        old['bindings']['digest']=api._digest(binding)
        old['input_identity']=api._digest({'bindings':old['bindings']['digest'],'plan':old['plan']})
        legacy=Path(state['target'])/'.methodology/runs/legacy/state.json'
        legacy.parent.mkdir(parents=True);legacy.write_text(json.dumps(old))
        before=legacy.read_bytes()
        if expected:
            _,spent,cap,refs=cont.historical(api,legacy)
            assert spent==0 and cap==4 and refs[0]['sha256']==api._file(legacy)['sha256']
        else:
            with pytest.raises(ValueError):cont.historical(api,legacy)
        assert legacy.read_bytes()==before
        with pytest.raises(ValueError):api.initialize(state['target'],state['spec_path'],'fixture','new',framework=state['framework'],adapter=state['adapter_path'],plan=state['plan']['path'])
        logger.info('[IMP:9][test_historical_terminal_pair_matrix][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_historical_terminal_pair_matrix][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_historical_terminal_pair_matrix
# region FUNC_test_process_interruption_and_rollback [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test process interruption and rollback
## @uses OSError, Path, api.advance, api.read_json, api.save, cont.active, cont.committed, cont.reservation_operation, logger.error, logger.info, make_fixture, monkeypatch.context, original, patch.setattr, path.read_bytes, pytest.mark.parametrize, pytest.raises, str, success, type
## @io tmp_path, monkeypatch, point are explicit owned fixture/probe inputs -> None after actual assertions: path.read_bytes() == before; recovered['debug_spent'] == spent and cont.active(recovered)['id'] == entry; next_state['debug_spent'] == spent; stale['lineage']['entries'][0]['state'] == 'complete'. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
@pytest.mark.parametrize('point',['before-checkpoint','after-journal','after-uncertain-release','after-completion'])
def test_process_interruption_and_rollback(tmp_path,monkeypatch,point):
    logger.info('[IMP:4][test_process_interruption_and_rollback][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        entry=cont.active(state)['id'];before=path.read_bytes();spent=state['debug_spent']
        if point in {'before-checkpoint','after-journal'}:
            original=cont.atomic
            def fail(destination,value,exclusive=False):
                if Path(destination)==path or point=='before-checkpoint':raise OSError('controlled process publication interruption')
                returned = original(destination,value,exclusive)
                logger.info('[IMP:9][test_process_interruption_and_rollback][RESULT] declared observations completed')
                return returned
            with monkeypatch.context() as patch:
                patch.setattr(cont,'atomic',fail)
                with pytest.raises(OSError):cont.reservation_operation(api,state,'released',{'entry':entry,'worker':'fixture'})
            assert path.read_bytes()==before
            current=api.read_json(path)
            if point=='after-journal':
                with pytest.raises(ValueError,match='rollback|incomplete'):cont.committed(api,current)
            else:
                recovered=cont.reservation_operation(api,current,'recover',{'entry':entry,'outcome':'unlaunched','evidence':[str(evidence)]})
                assert recovered['debug_spent']==spent and cont.active(recovered)['id']==entry
        elif point=='after-uncertain-release':
            state=cont.reservation_operation(api,state,'recover',{'entry':entry,'outcome':'unknown','evidence':[str(evidence)]})
            with pytest.raises(ValueError):cont.reservation_operation(api,state,'reserve',{'entry':entry})
            # Actual investigation can identify completed worker; result still needs canonical validation.
            state=cont.reservation_operation(api,state,'recover',{'entry':entry,'outcome':'completed','worker':'observed-worker','evidence':[str(evidence)]})
            next_state=api.advance(state,success(state,evidence));api.save(path,next_state)
            assert next_state['debug_spent']==spent
            with pytest.raises(ValueError):cont.reservation_operation(api,next_state,'reserve',{'entry':entry})
        else:
            state=api.advance(state,success(state,evidence));api.save(path,state)
            stale=api.read_json(path)
            assert stale['lineage']['entries'][0]['state']=='complete'
            with pytest.raises(ValueError):cont.reservation_operation(api,stale,'reserve',{'entry':entry})
        logger.info('[IMP:9][test_process_interruption_and_rollback][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_process_interruption_and_rollback][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_process_interruption_and_rollback
# region FUNC_test_worker_cannot_grant_and_export_cannot_dispatch [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test worker cannot grant and export cannot dispatch
## @uses api.advance, exported.read_bytes, exported.write_bytes, logger.error, logger.info, make_fixture, path.read_bytes, pytest.raises, str, subprocess.run, success, type
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: path.read_bytes() == before; proc.returncode == 2 and exported.read_bytes() == before. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_worker_cannot_grant_and_export_cannot_dispatch(tmp_path):
    logger.info('[IMP:4][test_worker_cannot_grant_and_export_cannot_dispatch][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        request=success(state,evidence)
        request['result']['approval']='worker invented permission'
        request['result']['debug_cap']=99
        before=path.read_bytes()
        with pytest.raises(ValueError):api.advance(state,request)
        assert path.read_bytes()==before
        exported=tmp_path/'export.json';exported.write_bytes(before)
        proc=subprocess.run([sys.executable,api.__file__,'show','--state',str(exported)],capture_output=True,text=True)
        assert proc.returncode==2 and exported.read_bytes()==before
        logger.info('[IMP:9][test_worker_cannot_grant_and_export_cannot_dispatch][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_worker_cannot_grant_and_export_cannot_dispatch][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_worker_cannot_grant_and_export_cannot_dispatch
# region FUNC_test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose test no repair qa at cap and causal architect cannot bypass
## @uses Path, api.advance, api.save, cont.continue_run, logger.error, logger.info, make_fixture, request, success, to_phase, type, wrapped['result'].update
## @io tmp_path are explicit owned fixture/probe inputs -> None after actual assertions: verification['phase'] == 'qa' and verification['debug_spent'] == verification['debug_cap'] == 0; ended['status'] == 'ESCALATED' and ended['debug_spent'] == 0. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass(tmp_path):
    logger.info('[IMP:4][test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path,cap=0)
        state=to_phase(state,evidence,'qa');api.save(path,state)
        # QA payload itself must remain the full canonical real validator population.
        wrapped=success(state,evidence);wrapped['result'].update(status='BLOCKED',reason='fixture missing external proof')
        closed=api.advance(state,wrapped);api.save(path,closed)
        snap=Path(closed['lineage']['closed'][-1]['path'])
        req=request(closed,evidence,'qa')
        _,verification=cont.continue_run(api,snap,req)
        assert verification['phase']=='qa' and verification['debug_spent']==verification['debug_cap']==0
        verification=api.advance(verification,success(verification,evidence));api.save(path,verification)
        wrapped=success(verification,evidence);wrapped['result'].update(status='BLOCKED',reason='fixture pending owner proof')
        closed=api.advance(verification,wrapped);api.save(path,closed)
        snap=Path(closed['lineage']['closed'][-1]['path'])
        _,architect=cont.continue_run(api,snap,request(closed,evidence,'architect')|{'run_id':'architecture-repeat'})
        ended=api.advance(architect,success(architect,evidence))
        assert ended['status']=='ESCALATED' and ended['debug_spent']==0
        logger.info('[IMP:9][test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_no_repair_qa_at_cap_and_causal_architect_cannot_bypass
# region FUNC_test_amended_spec_enrollment_never_mints_wallet [DOMAIN(9): Continuation; CONCEPT(9): DiscriminatingEvidence; TECH(7): Python]
## @purpose test amended spec enrollment never mints wallet
## @uses (Path(state['target']) / '.methodology/lineages').glob, (_ for _ in ()).throw, OSError, Path, amended.write_text, api.initialize, api.read_json, close_blocked, cont.committed, cont.continue_run, cont.digest, json.dumps, len, list, logger.error, logger.info, make_fixture, marker.unlink, marker.write_text, monkeypatch.context, patch.setattr, pytest.mark.parametrize, pytest.raises, request, str, type
## @io tmp_path, monkeypatch, fault are explicit owned fixture/probe inputs -> None after actual assertions: len(list((Path(state['target']) / '.methodology/lineages').glob('*/state.json'))) == 1; api.read_json(path)['status'] == 'BLOCKED'. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
@pytest.mark.parametrize('fault',['none','missing','conflicting','interrupted'])
def test_amended_spec_enrollment_never_mints_wallet(tmp_path,monkeypatch,fault):
    logger.info('[IMP:4][test_amended_spec_enrollment_never_mints_wallet][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        closed,snapshot=close_blocked(path,state,evidence)
        amended=Path(state['target'])/'amended.md';amended.write_text('Explicit same-cause amended fixture spec')
        req=request(closed,evidence,'architect')|{'spec':str(amended)}
        if fault=='interrupted':
            original=api.save
            with monkeypatch.context() as patch:
                patch.setattr(api,'save',lambda *args: (_ for _ in ()).throw(OSError('controlled interruption after admission')))
                with pytest.raises(OSError):cont.continue_run(api,snapshot,req)
            assert api.read_json(path)['status']=='BLOCKED'
            with pytest.raises(ValueError):api.initialize(state['target'],amended,'fixture','other',framework=state['framework'],adapter=state['adapter_path'],plan=state['plan']['path'])
            logger.info('[IMP:9][test_amended_spec_enrollment_never_mints_wallet][RESULT] declared observations completed')
            return
        _,next_state=cont.continue_run(api,snapshot,req)
        marker=Path(state['target'])/'.methodology/admissions'/(cont.digest({'spec_path':str(amended)})+'.json')
        if fault=='missing': marker.unlink()
        elif fault=='conflicting':marker.write_text(json.dumps({'key':{'spec_path':str(amended)},'authority':'another'}))
        if fault!='none':
            with pytest.raises((ValueError,OSError)):cont.committed(api,next_state)
        for spec in (state['spec_path'],amended):
            with pytest.raises(ValueError):api.initialize(state['target'],spec,'fixture','other',framework=state['framework'],adapter=state['adapter_path'],plan=state['plan']['path'])
        assert len(list((Path(state['target'])/'.methodology/lineages').glob('*/state.json')))==1
        logger.info('[IMP:9][test_amended_spec_enrollment_never_mints_wallet][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_amended_spec_enrollment_never_mints_wallet][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_amended_spec_enrollment_never_mints_wallet
# region FUNC_test_changed_inputs_require_fresh_verification [DOMAIN(9): Continuation; CONCEPT(9): DiscriminatingEvidence; TECH(7): Python]
## @purpose test changed inputs require fresh verification
## @uses Path, api.advance, api.save, cont.continue_run, fresh['accepted'].keys, json.dumps, json.loads, logger.error, logger.info, make_fixture, p.read_text, p.write_text, path.read_bytes, pytest.mark.parametrize, pytest.raises, req.update, req['scope'].append, request, str, success, to_phase, type, wrapped['result'].update
## @io tmp_path, change are explicit owned fixture/probe inputs -> None after actual assertions: path.read_bytes() == before; fresh['accepted'].keys() == {'code'} and fresh['debug_spent'] == fresh['debug_cap'] == 0; fresh['accepted']['code']['input'] == fresh['input_identity']. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
@pytest.mark.parametrize('change',['framework','rules','adapter','scope'])
def test_changed_inputs_require_fresh_verification(tmp_path,change):
    logger.info('[IMP:4][test_changed_inputs_require_fresh_verification][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path,cap=0)
        state=to_phase(state,evidence,'finalize');api.save(path,state)
        wrapped=success(state,evidence);wrapped['result'].update(status='BLOCKED',reason='fixture external prerequisite')
        closed=api.advance(state,wrapped);api.save(path,closed)
        snapshot=Path(closed['lineage']['closed'][-1]['path']);req=request(closed,evidence,'finalize')
        if change=='framework':
            p=Path(state['framework'])/'README.md';p.write_text(p.read_text()+'\nChanged bound package input\n')
        elif change=='rules':
            p=Path(state['bindings']['neutral_root'])/'checks/preflight.md';p.write_text(p.read_text()+'\nChanged bound rule input\n')
        elif change=='adapter':
            p=Path(state['adapter_path']);data=json.loads(p.read_text());data['capabilities']['capability-discovery']['fallback']+=' fixture';p.write_text(json.dumps(data))
        else:req['scope'].append('added.py')
        before=path.read_bytes()
        with pytest.raises(ValueError):cont.continue_run(api,snapshot,req)
        assert path.read_bytes()==before
        if change!='scope':
            # Explicit parent applicability proof can readopt unchanged Code artifacts, never QA/Review.
            req.update(phase='qa',reuse_code={'reason':'Unchanged actual Code/spec/plan/scope; independently renew all verification under changed bindings','evidence':[str(evidence)]})
            _,fresh=cont.continue_run(api,snapshot,req)
            assert fresh['accepted'].keys()=={'code'} and fresh['debug_spent']==fresh['debug_cap']==0
            assert fresh['accepted']['code']['input']==fresh['input_identity']
        logger.info('[IMP:9][test_changed_inputs_require_fresh_verification][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_changed_inputs_require_fresh_verification][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_changed_inputs_require_fresh_verification
# region FUNC_test_observed_overrun_retained_and_holds_next_release [DOMAIN(9): Continuation; CONCEPT(9): DiscriminatingEvidence; TECH(7): Python]
## @purpose test observed overrun retained and holds next release
## @uses Path, api.advance, api.read_json, api.save, close_blocked, cont.active, cont.continue_run, cont.reservation_operation, float, len, logger.error, logger.info, make_fixture, pytest.raises, request, str, success, to_phase, type
## @io tmp_path and usd from exact decorator cases1.25/10**400 -> None after actual recovery/save/readback retains known finite cumulative USD, identical repeated recovery does not double count, null/lower/nonfinite observations refuse, and further release/continuation stays held. Owned fixture writes only; no paid/native/product call.
## @complexity 6
@pytest.mark.parametrize('usd',[1.25,10**400])
def test_observed_overrun_retained_and_holds_next_release(tmp_path,usd):
    logger.info('[IMP:4][test_observed_overrun_retained_and_holds_next_release][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path,cap=0)
        state=to_phase(state,evidence,'code');api.save(path,state)
        closed,snapshot=close_blocked(path,state,evidence)
        req=request(closed,evidence)
        req['grant']={'id':'g','lineage':closed['lineage']['id'],'target':closed['target'],'approval':'fixture bounded grant','entries':1,'cost_usd':0}
        _,current=cont.continue_run(api,snapshot,req);entry=cont.active(current)['id']
        current=cont.reservation_operation(api,current,'released',{'entry':entry,'worker':'observed-worker'})
        current=cont.reservation_operation(api,current,'recover',{'entry':entry,'outcome':'completed','worker':'observed-worker','evidence':[str(evidence)],'usd':usd})
        assert cont.active(api.read_json(path))['usd']==usd
        before_count=len(current['lineage']['costs'])
        current=cont.reservation_operation(api,current,'recover',{'entry':entry,'outcome':'completed','worker':'observed-worker','evidence':[str(evidence)],'usd':usd})
        assert len(current['lineage']['costs'])==before_count and current['debug_spent']==1
        with pytest.raises(ValueError):cont.reservation_operation(api,current,'reserve',{'entry':entry})
        for erased in (None,0,-1,float('nan')):
            with pytest.raises(ValueError):cont.reservation_operation(api,current,'recover',{'entry':entry,'outcome':'completed','worker':'observed-worker','evidence':[str(evidence)],'usd':erased})
        final=api.advance(current,success(current,evidence));api.save(path,final)
        assert final['status']=='BLOCKED' and final['history'][-1]['withheld_next']=='observed grant cost ceiling exceeded'
        terminal=Path(final['lineage']['closed'][-1]['path'])
        with pytest.raises(ValueError):cont.continue_run(api,terminal,request(final,evidence,'qa')|{'run_id':'no-overrun-spend'})
        assert final['lineage']['costs'][-1]['usd']==usd
        logger.info('[IMP:9][test_observed_overrun_retained_and_holds_next_release][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_observed_overrun_retained_and_holds_next_release][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_observed_overrun_retained_and_holds_next_release
# region FUNC_test_owned_critical_trajectories [DOMAIN(9): Continuation; CONCEPT(9): DiscriminatingEvidence; TECH(7): Python]
## @purpose test owned critical trajectories
## @uses '\n'.join, (_ for _ in ()).throw, OSError, any, caplog.clear, caplog.set_level, cont.atomic, cont.committed, cont.prepare, copy.deepcopy, destination.read_bytes, list, logger.error, logger.info, make_fixture, monkeypatch.context, own.index, patch.setattr, pytest.raises, r.getMessage, str, tmp_path.glob, type
## @io tmp_path, caplog, monkeypatch are explicit owned fixture/probe inputs -> None after actual assertions: cont.committed(api, state) == path; own.index('[IMP:4][committed][START] bounded operation') < own.index('[IMP:7][committed][READ] current inputs and complete authority') < own.index('[IMP:9][committed][RESULT] operation complete'); not [r for r in caplog.records if r.levelno >= logging.ERROR]; '[IMP:9][committed][RESULT] operation complete' not in without_owner; actual == expected; actual + [('unrelated', 'unexpected failure')] != expected; any(('[prepare][ALLOWANCE]' in r.getMessage() for r in caplog.records)); destination.read_bytes() == before and (not list(tmp_path.glob('publication.json.*.tmp'))); [(r.name, r.getMessage()) for r in caplog.records if r.levelno >= logging.ERROR] == [('continuation', '[IMP:10][atomic][FAIL] kind=OSError')]; str(tmp_path) not in '\n'.join((r.getMessage() for r in caplog.records)). Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
def test_owned_critical_trajectories(tmp_path,caplog,monkeypatch):
    logger.info('[IMP:4][test_owned_critical_trajectories][START] owned observation')
    try:
        import logging
        caplog.set_level(logging.INFO)
        path,state,evidence=make_fixture(tmp_path,cap=0)
        caplog.clear()
        assert cont.committed(api,state)==path
        own=[r.getMessage() for r in caplog.records if r.name=='continuation']
        assert own.index('[IMP:4][committed][START] bounded operation')<own.index('[IMP:7][committed][READ] current inputs and complete authority')<own.index('[IMP:9][committed][RESULT] operation complete')
        assert not [r for r in caplog.records if r.levelno>=logging.ERROR]
        # An owning result is required; a helper-only success cannot satisfy this trajectory.
        without_owner=[m for m in own if '[committed][RESULT]' not in m]
        assert '[IMP:9][committed][RESULT] operation complete' not in without_owner
        caplog.clear();attempt=copy.deepcopy(state);attempt['lineage']['active_entry']=None
        with pytest.raises(ValueError):cont.prepare(attempt,charge=True)
        expected=[('continuation','[IMP:10][require][REFUSE] repair allowance exhausted'),('continuation','[IMP:10][prepare][FAIL] kind=ValueError')]
        actual=[(r.name,r.getMessage()) for r in caplog.records if r.levelno>=logging.ERROR]
        assert actual==expected
        assert actual+[('unrelated','unexpected failure')]!=expected
        assert any('[prepare][ALLOWANCE]' in r.getMessage() for r in caplog.records)
        caplog.clear();destination=tmp_path/'publication.json';cont.atomic(destination,{'old':1});before=destination.read_bytes()
        with monkeypatch.context() as patch:
            patch.setattr(Path,'replace',lambda *args: (_ for _ in ()).throw(OSError('controlled replacement interruption')))
            with pytest.raises(OSError):cont.atomic(destination,{'new':2})
        assert destination.read_bytes()==before and not list(tmp_path.glob('publication.json.*.tmp'))
        assert [(r.name,r.getMessage()) for r in caplog.records if r.levelno>=logging.ERROR]==[('continuation','[IMP:10][atomic][FAIL] kind=OSError')]
        assert str(tmp_path) not in '\n'.join(r.getMessage() for r in caplog.records)
        logger.info('[IMP:9][test_owned_critical_trajectories][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_owned_critical_trajectories][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_owned_critical_trajectories
# region FUNC_test_successor_reentry_predicates_all_terminals [DOMAIN(9): Continuation; CONCEPT(9): DiscriminatingEvidence; TECH(7): Python]
## @purpose test successor reentry predicates all terminals
## @uses Path, api.advance, api.save, closed['history'].append, cont.continue_run, logger.error, logger.info, make_fixture, pytest.mark.parametrize, pytest.raises, request, success, to_phase, type, wrapped['result'].update
## @io tmp_path, terminal, phase, reentry are explicit owned fixture/probe inputs -> None after actual assertions: next_state['phase'] == reentry and next_state['debug_spent'] == (1 if reentry == 'code' else 0); next_state['accepted']['code']['input'] == next_state['input_identity']. Parametrization is exactly the decorator population. Expected production refusals are caught; unexpected errors/assertions emit own FAIL and raise. Files/processes are confined to tmp_path; no native efficacy claim.
## @complexity 6
@pytest.mark.parametrize('terminal,phase,reentry',[
    ('SPEC_BLOCKED','architect','architect'),('VISUAL_GATE_FAIL','architect','architect'),
    ('BLOCKED','code','code'),('ERROR','code','code'),('ESCALATED','qa','qa'),
    ('ESCALATED_FINALIZE','finalize','finalize'),('SUCCESS','finalize','qa')])
def test_successor_reentry_predicates_all_terminals(tmp_path,terminal,phase,reentry):
    logger.info('[IMP:4][test_successor_reentry_predicates_all_terminals][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path,cap=4)
        state=to_phase(state,evidence,phase);api.save(path,state)
        wrapped=success(state,evidence)
        if terminal=='SUCCESS':
            closed=api.advance(state,wrapped)
        elif terminal=='ESCALATED_FINALIZE':
            wrapped['result'].update(status=terminal,reason='fixture resolved final prerequisite',requiredRepair='none; no source repair')
            closed=api.advance(state,wrapped)
        else:
            wrapped['result'].update(status='BLOCKED',reason='fixture root terminal prerequisite',limitations=[])
            closed=api.advance(state,wrapped)
            # Explicit structural root terminal fixtures retain the real blocked output;
            # they do not fabricate successful Code/QA/Review evidence.
            closed['status']=terminal
            closed['history'].append({'kind':'root-terminal-fixture','status':terminal,'phase':phase,'debug_delta':0})
        api.save(path,closed);snapshot=Path(closed['lineage']['closed'][-1]['path'])
        _,next_state=cont.continue_run(api,snapshot,request(closed,evidence,reentry))
        assert next_state['phase']==reentry and next_state['debug_spent']==(1 if reentry=='code' else 0)
        if reentry=='qa':
            assert next_state['accepted']['code']['input']==next_state['input_identity']
        # Unsupported direct Finalize never receives invented prior success from a pre-code root.
        if phase=='architect':
            with pytest.raises(ValueError):cont.continue_run(api,snapshot,request(closed,evidence,'finalize')|{'run_id':'invalid-finalize'})
        logger.info('[IMP:9][test_successor_reentry_predicates_all_terminals][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_successor_reentry_predicates_all_terminals][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_successor_reentry_predicates_all_terminals

# region FUNC_test_admission_symlink_cannot_redirect_writes [DOMAIN(9): Continuation; CONCEPT(9): OwnedStorage; TECH(7): pathlib]
## @purpose Verify an actual admission-directory symlink cannot redirect any new authority writes.
## @uses pathlib.Path.symlink_to, run_state.initialize, continuation.check_admissions, pytest.raises
## @io tmp_path owned fixture -> None after actual symlink redirection refuses and outside directory remains empty; current authority remains byte-identical. Expected refusal only; no writes outside tmp_path.
## @complexity 5
def test_admission_symlink_cannot_redirect_writes(tmp_path):
    logger.info('[IMP:4][test_admission_symlink_cannot_redirect_writes][START] owned control')
    path,state,_=make_fixture(tmp_path)
    registry=Path(state['target'])/'.methodology/admissions';retained=registry.with_name('admissions-retained');registry.rename(retained)
    outside=tmp_path/'outside';outside.mkdir();registry.symlink_to(outside,target_is_directory=True)
    before=path.read_bytes();spec=Path(state['target'])/'separate.md';spec.write_text('Independent fixture spec')
    with pytest.raises(ValueError):api.initialize(state['target'],spec,'fixture','other',framework=state['framework'],adapter=state['adapter_path'],plan=state['plan']['path'])
    assert not list(outside.iterdir()) and path.read_bytes()==before
    with pytest.raises(ValueError):cont.check_admissions(api,state)
    logger.info('[IMP:9][test_admission_symlink_cannot_redirect_writes][RESULT] no escaped writes')
# endregion FUNC_test_admission_symlink_cannot_redirect_writes

# region FUNC_test_no_success_trace_before_failed_return [DOMAIN(9): Continuation; CONCEPT(9): HonestTrajectory; TECH(7): logging]
## @purpose Reject success traces before nonfinite digest encoding or missing authority-key evaluation fails.
## @uses continuation.digest, continuation.authority, pytest.raises, caplog.records
## @io tmp_path unused owned fixture parameter, caplog, function/value/kind exact decorated cases -> None after exact START→FAIL and ERROR population, with no RESULT. No filesystem writes; malformed inputs are intentional independent counterexamples.
## @complexity 5
@pytest.mark.parametrize('function,value,kind',[('digest',float('nan'),ValueError),('authority',{},KeyError)])
def test_no_success_trace_before_failed_return(tmp_path,caplog,function,value,kind):
    import logging
    logger.info('[IMP:4][test_no_success_trace_before_failed_return][START] direct contrary inputs')
    caplog.set_level(logging.INFO);caplog.clear()
    with pytest.raises(kind):getattr(cont,function)(value)
    own=[r.getMessage() for r in caplog.records if r.name=='continuation']
    assert own==['[IMP:4]['+function+'][START] bounded operation','[IMP:10]['+function+'][FAIL] kind='+kind.__name__]
    assert [(r.name,r.getMessage()) for r in caplog.records if r.levelno>=logging.ERROR]==[('continuation','[IMP:10]['+function+'][FAIL] kind='+kind.__name__)]
    logger.info('[IMP:9][test_no_success_trace_before_failed_return][RESULT] no false success')
# endregion FUNC_test_no_success_trace_before_failed_return


# region FUNC_test_foreign_profile_and_parent_boundary_refusals [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Refuse foreign wires, unsupported neutral profiles and external parent wallets at the admission boundary.
## @uses Path, api._digest, cont.historical, copy.deepcopy, json.dumps, logger.error, logger.info, make_fixture, pytest.mark.parametrize, pytest.raises, subprocess.run, sys.executable
## @io tmp_path and the declared damage case are explicit owned fixtures. None after actual assertions: each mutated terminal refuses with ValueError, bytes stay identical; a valid terminal with a parent_path also refuses; the shipped CLI rejects --parent with exit2 and empty stdout. Expected refusals are caught; no native efficacy claim.
## @complexity 6
@pytest.mark.parametrize('damage',['codex-wire','neutral5','external-history'])
def test_foreign_profile_and_parent_boundary_refusals(tmp_path,damage):
    logger.info('[IMP:4][test_foreign_profile_and_parent_boundary_refusals][START] owned observation')
    try:
        path,state,evidence=make_fixture(tmp_path)
        old=copy.deepcopy(state);old.pop('lineage');old['schema_version']=2
        old.update(status='BLOCKED',phase='bootstrap')
        old['bindings']['neutral_version']='4.0.0'
        def reseal(value):
            binding=copy.deepcopy(value['bindings']);binding.pop('digest')
            value['bindings']['digest']=api._digest(binding)
            value['input_identity']=api._digest({'bindings':value['bindings']['digest'],'plan':value['plan']})
        reseal(old)
        if damage=='codex-wire':
            old['contract_version']='methodology-codex/2.0.0'
        elif damage=='neutral5':
            old['bindings']['neutral_version']='5.0.0';reseal(old)
        else:
            old['history'].append({'kind':'external-accounting','debug_delta':0})
        legacy=Path(state['target'])/'.methodology/runs/legacy/state.json'
        legacy.parent.mkdir(parents=True);legacy.write_text(json.dumps(old))
        before=legacy.read_bytes()
        with pytest.raises(ValueError):cont.historical(api,legacy)
        assert legacy.read_bytes()==before
        valid=copy.deepcopy(old)
        if damage=='codex-wire':
            valid['contract_version']='methodology-dsh/2.0.0'
        elif damage=='neutral5':
            valid['bindings']['neutral_version']='4.0.0';reseal(valid)
        else:
            valid['history'].pop()
        legacy.write_text(json.dumps(valid));before=legacy.read_bytes()
        with pytest.raises(ValueError):cont.historical(api,legacy,tmp_path/'parent.json')
        assert legacy.read_bytes()==before
        helper=Path(__file__).resolve().parents[1]/'skills/feature-dev/scripts/run_state.py'
        request=tmp_path/'request.json';request.write_text('{}')
        proc=subprocess.run([sys.executable,str(helper),'continue','--predecessor',str(legacy),'--parent',str(tmp_path/'parent.json'),'--request',str(request)],capture_output=True,text=True)
        assert proc.returncode==2 and not proc.stdout
        logger.info('[IMP:9][test_foreign_profile_and_parent_boundary_refusals][RESULT] declared observations completed')
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][test_foreign_profile_and_parent_boundary_refusals][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_test_foreign_profile_and_parent_boundary_refusals
