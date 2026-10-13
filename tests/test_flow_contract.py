# region MODULE_CONTRACT [DOMAIN(9): DevelopmentFlow; CONCEPT(9): ContractEvidence; TECH(6): Python]
## @modulecontract
## @purpose Verify actual flow semantics with independent cases and discriminating scratch controls.
## @scope Five subjects, finite cases, actual CLI sink, omitted compound clauses and restoration.
## @input Actual neutral repository clauses and generic finite case facts.
## @output Safe evidence decisions, fingerprints and explicit refusal codes.
## @links [READS_DATA_FROM(9): flow, protocols/role-returns.md; USES_API(6): Python standard library]
## @invariants
## - No repository mutation or agent dispatch occurs; tests alter isolated copies only.
## - Unsupported critical semantics fail closed; no live harness execution is claimed.
## @rationale
## Q: Why interpret selected controlled clauses?
## A: Mutations must affect outcomes without adding a production engine or changing the authoring format.
## @changes
## LAST_CHANGE: [v0.3.0 - Enforce typed returns, read predicates and current evidence after independent boundary findings.]
## @modulemap
## FUNC 7[run probe] => run_probe
## FUNC 7[expose trace] => expose_trace
## FUNC 7[test contract semantics] => test_contract_semantics
## FUNC 7[test five subjects calls and live bodies] => test_five_subjects_calls_and_live_bodies
## FUNC 7[test scenarios] => test_scenarios
## FUNC 7[test probe cli real path] => test_probe_cli_real_path
## FUNC 7[test mutations] => test_mutations
## FUNC 7[test conditional return data rejected before transition] => test_conditional_return_data_rejected_before_transition
## FUNC 7[test probe invalid case input exit two] => test_probe_invalid_case_input_exit_two
## FUNC 7[test terminal events lock stream] => test_terminal_events_lock_stream
## FUNC 7[test visual return rejects boolean exit] => test_visual_return_rejects_boolean_exit
## FUNC 7[test return authority and identity refusals] => test_return_authority_and_identity_refusals
## FUNC 7[test grant bounds and scope] => test_grant_bounds_and_scope
## FUNC 7[test bug report fields require populated text] => test_bug_report_fields_require_populated_text
## FUNC 7[test malformed nested scan is refused] => test_malformed_nested_scan_is_refused
## FUNC 7[test malformed grant evidence is refused] => test_malformed_grant_evidence_is_refused
## FUNC 7[example case] => example_case
## FUNC 7[test initial spend rejected before debug] => test_initial_spend_rejected_before_debug
## FUNC 7[test role payload shape refused before continuation] => test_role_payload_shape_refused_before_continuation
## FUNC 7[test qa non success preserves eight scan payload] => test_qa_non_success_preserves_eight_scan_payload
## FUNC 7[test actual debug fixed return renews qa] => test_actual_debug_fixed_return_renews_qa
## FUNC 7[test activation is required for each phase return] => test_activation_is_required_for_each_phase_return
## FUNC 7[test visual actual threshold and scanned output] => test_visual_actual_threshold_and_scanned_output
## FUNC 7[test declared scan hash mismatch is refused] => test_declared_scan_hash_mismatch_is_refused
## FUNC 7[test malformed nested case cli exit two] => test_malformed_nested_case_cli_exit_two
## FUNC 7[test activation receipt guards each phase] => test_activation_receipt_guards_each_phase
## FUNC 7[test blocked conditional payloads] => test_blocked_conditional_payloads
## FUNC 7[test applicable doxygen current record and refusals] => test_applicable_doxygen_current_record_and_refusals
## FUNC 7[test finalize actual return payload] => test_finalize_actual_return_payload
## FUNC 7[test escalated finalize conditional payload] => test_escalated_finalize_conditional_payload
## FUNC 7[test activation receipt actual assignments] => test_activation_receipt_actual_assignments
## @usecases
## - Maintainer -> weakens actual prose or return data -> independent expected outcomes reject it.
## @GREP_SUMMARY development flow, live clauses, evidence validation, bounded cases, refusal, restoration
## @STRUCTURE live anchored norms -> selected semantics -> finite cases -> evidence decisions -> explicit JSON and LDD

def _module_contract():
    pass
# endregion MODULE_CONTRACT


import hashlib
import json
import logging
import pathlib
import re
import subprocess
import sys

import pytest
import flow_contract_probe as probe

CASE_IDS = [case['case_id'] for case in json.loads((pathlib.Path(__file__).parents[1] / 'examples/flow-contract/cases.json').read_text(encoding='utf-8'))]

# region FUNC_run_probe [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Observe the real consumer stdout, stderr and process exit.
## @io Repository root and cases path -> subprocess.CompletedProcess
## @complexity 7
def run_probe(root, cases):
    command = [sys.executable, str(root / 'tests/flow_contract_probe.py'), '--root', str(root), '--cases', str(cases)]
    print('[IMP:7][run_probe][PROCESS] actual consumer entry point')
    result = subprocess.run(command, cwd=str(root), capture_output=True, text=True)
    print('[IMP:9][run_probe][RESULT] exit=%d stdout=%d stderr=%d' % (result.returncode, len(result.stdout), len(result.stderr)))
    return result
# endregion FUNC_run_probe


# region FUNC_expose_trace [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Expose actual in-process probe events before assertions.
## @io pytest log collector -> printed and returned trajectory lines
## @complexity 7
def expose_trace(caplog):
    lines = [record.getMessage() for record in caplog.records if record.name == 'flow_probe']
    for line in lines:
        print(line)
    return lines
# endregion FUNC_expose_trace


# region FUNC_test_contract_semantics [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify contract semantics.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_contract_semantics(repo_root, caplog):
    caplog.set_level(logging.INFO, logger='flow_probe')
    bundle = probe.load_contract(repo_root)
    lines = expose_trace(caplog)
    print('[IMP:9][test_contract_semantics][VERIFY] full clause meaning and independent expected values')
    assert bundle['default_cap'] == 4
    assert bundle['selected']['STATE-303'] == {'timing':'before','qa_charge':'no'}
    assert bundle['selected']['STATE-304']['failed_spend'] == 'preserves'
    assert bundle['selected']['PHASE-605'] == {'renew':'renew full independent QA','negation':'MUST NOT'}
    assert bundle['transitions'] == {('Bootstrap','SUCCESS'):('Architect','PHASE-901'),('Architect','SUCCESS'):('Code','PHASE-901'),('Code','SUCCESS'):('QA','PHASE-901'),('QA','SUCCESS'):('Review','PHASE-901'),('Review','SUCCESS'):('Finalize','PHASE-901'),('Debug','FIXED'):('QA','PHASE-901')}
    assert set(bundle['common_fields']) == {'phase','role','status','summary','runId','inputIdentity','candidateIdentity','contractVersion','evidence'}
    assert set(bundle['bug_fields']) - {'bugReport'} == {'goal','actual','logAnalysis','dataAnalysis','hypothesis','recommendation'}
    assert any('[load_contract][VALIDATED]' in line for line in lines)
    assert not any('[IMP:10]' in line for line in lines)
# endregion FUNC_test_contract_semantics


# region FUNC_test_five_subjects_calls_and_live_bodies [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify five subjects calls and live bodies.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_five_subjects_calls_and_live_bodies(repo_root, caplog):
    caplog.set_level(logging.INFO, logger='flow_probe')
    bundle = probe.load_contract(repo_root)
    expose_trace(caplog)
    declarations = {}
    for kind,name in (('cap','capabilities'),('param','parameters')):
        text=(repo_root / 'runtime' / (name+'.md')).read_text(encoding='utf-8')
        declarations[kind]=set(re.findall(r'^- \*\*'+kind+r':([^*]+)\*\*',text,re.M))
    expected={'flow/phases.md':('flow.phases','PHASE',10),'flow/run-state.md':('flow.run-state','STATE',7),'flow/delegation.md':('flow.delegation','DELEG',6),'flow/finalize.md':('flow.finalize','FINAL',6),'protocols/role-returns.md':('protocols.role-returns','RETURN',9)}
    for path,(subject,prefix,blocks) in expected.items():
        parsed=bundle['subjects'][path]
        print('[IMP:9][test_five_subjects_calls_and_live_bodies][BODY] subject=%s norms=%d anchors=%d' %(subject,len(parsed['norms']),len(parsed['anchors'])))
        assert parsed['card']['id']==subject and parsed['card']['status']=='draft'
        assert len(parsed['anchors'])>=blocks-1
        assert all(norm.startswith(prefix+'-') and len(body['body'])>40 for norm,body in parsed['norms'].items())
        live=[];fence=False
        for line in parsed['text'].splitlines():
            if line.startswith('```'):fence=not fence
            elif not fence:live.append(re.sub(r'`[^`]*`','',line))
        for kind,name in re.findall(r'\{\{(cap|param):([a-z0-9-]+)\}\}','\n'.join(live)):
            assert name in declarations[kind]
    assert 'debug-entry-cap' in declarations['param']
# endregion FUNC_test_five_subjects_calls_and_live_bodies


# region FUNC_test_scenarios [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify scenarios.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('case_id', CASE_IDS)
def test_scenarios(repo_root, case_id, caplog):
    caplog.set_level(logging.INFO, logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    cases=json.loads((repo_root/'examples/flow-contract/cases.json').read_text(encoding='utf-8'))
    case=next(case for case in cases if case['case_id']==case_id)
    actual=probe.evaluate_case(bundle,case)
    lines=expose_trace(caplog)
    print('[IMP:9][test_scenarios][VERIFY] case=%s expected_decision=%s' %(case_id,case['expected']['decision']))
    assert {key:actual[key] for key in case['expected']}==case['expected']
    if actual['decision']=='REFUSE':
        assert any('[REFUSAL]' in line for line in lines) or actual['refusal']=='CAP_INVALID'
    else:
        assert not any('[IMP:10]' in line for line in lines)
# endregion FUNC_test_scenarios


# region FUNC_test_probe_cli_real_path [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify probe cli real path.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_probe_cli_real_path(repo_root):
    result=run_probe(repo_root,repo_root/'examples/flow-contract/cases.json')
    print(result.stderr)
    assert result.returncode==0
    report=json.loads(result.stdout)
    assert report['ok'] and len(report['cases'])==len(CASE_IDS)
    assert all(row['matches_expected'] for row in report['cases'])
    assert '[IMP:7][main][READ_CASES]' in result.stderr
    assert '[IMP:9][main][EXIT] exit=0' in result.stderr
    assert '[IMP:10][load_contract]' not in result.stderr
    assert '[IMP:10][main]' not in result.stderr
    assert sum('[IMP:10][evaluate_case][REFUSAL]' in line for line in result.stderr.splitlines()) == sum(row['decision']=='REFUSE' for row in report['cases'])
    assert set(report['contract_hashes'])==set(probe.SUBJECTS)
# endregion FUNC_test_probe_cli_real_path


# region FUNC_test_mutations [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify mutations.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('control', ['omit-spend','qa-charge','conditional-return','renewal-negation','transition','visual-threshold','visual-minimum','code-map-condition'])
def test_mutations(repo_copy, control, caplog):
    caplog.set_level(logging.INFO,logger='flow_probe')
    mutations={
        'omit-spend':('flow/run-state.md','Record the Debug entry spend before entering the phase; ','','STATE-303'),
        'qa-charge':('flow/run-state.md','an initial or renewed QA consumes no Debug entry','an initial or renewed QA consumes one Debug entry','STATE-303'),
        'conditional-return':('protocols/role-returns.md','`dataAnalysis`, ','','RETURN-502'),
        'renewal-negation':('flow/phases.md','supplemental E2E MUST NOT replace','supplemental E2E MUST replace','PHASE-605'),
        'transition':('flow/phases.md','QA SUCCESS to Review','QA SUCCESS to Finalize','PHASE-901'),
        'visual-threshold':('flow/phases.md','at least three new or modified component nodes','component nodes','PHASE-403'),
        'visual-minimum':('flow/phases.md','at least one scanned node','zero scanned nodes','PHASE-403'),
        'code-map-condition':('protocols/role-returns.md','When Doxygen is applicable, Code SUCCESS also requires a `doxygen` build record','Code may reuse any map','RETURN-501'),
    }
    relative,before,after,norm=mutations[control]
    path=repo_copy/relative;pristine=path.read_text(encoding='utf-8')
    assert before in pristine,'negative control does not target live text'
    identity_before=hashlib.sha256(path.read_bytes()).hexdigest()
    changed=pristine.replace(before,after,1)
    try:
        path.write_text(changed,encoding='utf-8')
        identity_after=hashlib.sha256(path.read_bytes()).hexdigest()
        with pytest.raises(ValueError,match='CONTRACT_SEMANTICS:'+norm):probe.load_contract(repo_copy)
        expose_trace(caplog)
        process=run_probe(repo_copy,repo_copy/'examples/flow-contract/cases.json')
        report=json.loads(process.stdout)
        print('[IMP:9][test_mutations][REJECTED] control=%s before=%s after=%s refusal=%s exit=%d' %(control,identity_before,identity_after,report['refusal'],process.returncode))
        assert identity_after!=identity_before and process.returncode==1
        assert report=={'ok':False,'refusal':'CONTRACT_SEMANTICS:'+norm}
        assert '[IMP:10][load_contract][REFUSAL]' in process.stderr
    finally:
        path.write_text(pristine,encoding='utf-8')
    restored=run_probe(repo_copy,repo_copy/'examples/flow-contract/cases.json')
    print('[IMP:9][test_mutations][RESTORED] control=%s hash=%s exit=%d' %(control,hashlib.sha256(path.read_bytes()).hexdigest(),restored.returncode))
    assert hashlib.sha256(path.read_bytes()).hexdigest()==identity_before
    assert restored.returncode==0 and json.loads(restored.stdout)['ok']
# endregion FUNC_test_mutations


# region FUNC_test_conditional_return_data_rejected_before_transition [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify conditional return data rejected before transition.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_conditional_return_data_rejected_before_transition(repo_root, caplog):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    cases=json.loads((repo_root/'examples/flow-contract/cases.json').read_text(encoding='utf-8'))
    case=next(case for case in cases if case['case_id']=='bugreport-missing')
    before=hashlib.sha256(json.dumps(case,sort_keys=True).encode()).hexdigest()
    refused=probe.evaluate_case(bundle,case)
    expose_trace(caplog)
    print('[IMP:9][test_conditional_return_data_rejected_before_transition][REFUSED] hash=%s decision=%s spent=%d' %(before,refused['decision'],refused['repair_spent']))
    assert refused['refusal']=='RETURN_BUG_REPORT_REQUIRED' and refused['next_phase']=='Code' and refused['repair_spent']==0
    case['events'][0]['value']['bugReport']['dataAnalysis']='Observed restored data evidence'
    restored=probe.evaluate_case(bundle,case)
    after=hashlib.sha256(json.dumps(case,sort_keys=True).encode()).hexdigest()
    expose_trace(caplog)
    print('[IMP:9][test_conditional_return_data_rejected_before_transition][RESTORED] hash=%s decision=%s' %(after,restored['decision']))
    assert before!=after and restored['decision']=='REPAIR_REQUIRED' and restored['next_phase']=='DebugPending'
# endregion FUNC_test_conditional_return_data_rejected_before_transition


# region FUNC_test_probe_invalid_case_input_exit_two [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify probe invalid case input exit two.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_probe_invalid_case_input_exit_two(repo_copy, tmp_path):
    path=tmp_path/'invalid-cases.json';path.write_text('{}',encoding='utf-8')
    result=run_probe(repo_copy,path)
    print(result.stderr)
    assert result.returncode==2 and json.loads(result.stdout)['refusal']=='CASE_INPUT_INVALID'
# endregion FUNC_test_probe_invalid_case_input_exit_two


# region FUNC_test_terminal_events_lock_stream [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify terminal events lock stream.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('events,phase,spent,expected', [
    ([{'kind':'debug-failed'},{'kind':'enter-debug'}],'Debug',1,('BLOCKED','Debug',1,None)),
    ([{'kind':'finalize','source_repair':True},{'kind':'enter-debug'}],'Finalize',2,('ESCALATE','Owner',2,'ESCALATED_FINALIZE')),
    ([{'kind':'finalize','same_candidate':True},{'kind':'enter-debug'}],'Finalize',1,('WAIT_OWNER','ResultGate',1,None)),
])
def test_terminal_events_lock_stream(repo_root, caplog, events, phase, spent, expected):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    facts=dict(next(case for case in json.loads((repo_root/'examples/flow-contract/cases.json').read_text()) if case['case_id']=='default-cap')['facts'],phase=phase,repair_spent=spent,qa_verified=True,review_verified=True)
    actual=probe.evaluate_case(bundle,{'case_id':'terminal-lock','facts':facts,'events':events})
    expose_trace(caplog)
    print('[IMP:9][test_terminal_events_lock_stream][VERIFY] terminal outcome preserves spend before following events')
    assert tuple(actual[key] for key in ('decision','next_phase','repair_spent','refusal'))==expected
# endregion FUNC_test_terminal_events_lock_stream



# region FUNC_test_visual_return_rejects_boolean_exit [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify visual return rejects boolean exit.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_visual_return_rejects_boolean_exit(repo_root, caplog):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    cases=json.loads((repo_root/'examples/flow-contract/cases.json').read_text(encoding='utf-8'))
    case=next(case for case in cases if case['case_id']=='first-success')
    value=next(event['value'] for event in case['events'] if event.get('value',{}).get('phase')=='Architect')
    value['visualGate']={'status':'PASS','command':'example-check','exitCode':False,'output':'scannedNodes=1','evidence':['FORMAT.md'],'componentNodes':3,'testsOnly':False,'scannedNodes':1}
    facts=dict(case['facts'],phase='Architect',role='architect')
    refusal=probe.validate_return(bundle,value,facts)
    expose_trace(caplog)
    print('[IMP:9][test_visual_return_rejects_boolean_exit][VERIFY] boolean is not a command exit code')
    assert refusal=='RETURN_VISUAL_REQUIRED'
# endregion FUNC_test_visual_return_rejects_boolean_exit


# region FUNC_test_return_authority_and_identity_refusals [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify return authority and identity refusals.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('field,value,expected',[('counter_override',0,'RETURN_UNKNOWN_FIELD'),('candidateIdentity','candidate-b','RETURN_STALE_IDENTITY'),('status','PASS','RETURN_UNKNOWN_STATUS')])
def test_return_authority_and_identity_refusals(repo_root,caplog,field,value,expected):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    case=next(case for case in json.loads((repo_root/'examples/flow-contract/cases.json').read_text()) if case['case_id']=='first-success')
    returned=next(event['value'] for event in case['events'] if event.get('value',{}).get('phase')=='Bootstrap')
    returned[field]=value
    actual=probe.validate_return(bundle,returned,case['facts'])
    lines=expose_trace(caplog)
    print('[IMP:9][test_return_authority_and_identity_refusals][VERIFY] refusal='+expected)
    assert actual==expected
    assert any('[IMP:10][validate_return][REFUSAL]' in line for line in lines)
# endregion FUNC_test_return_authority_and_identity_refusals


# region FUNC_test_grant_bounds_and_scope [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify grant bounds and scope.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('entries,cost,scope,authority,allowed',[(1,0,'candidate-a',True,True),(20,1000,'candidate-a',True,True),(21,0,'candidate-a',True,False),(0,0,'candidate-a',True,False),(True,0,'candidate-a',True,False),(1,-1,'candidate-a',True,False),(1,1001,'candidate-a',True,False),(1,True,'candidate-a',True,False),(1,0,'candidate-b',True,False),(1,0,'candidate-a',False,False)])
def test_grant_bounds_and_scope(repo_root,caplog,entries,cost,scope,authority,allowed):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    case=next(case for case in json.loads((repo_root/'examples/flow-contract/cases.json').read_text()) if case['case_id']=='explicit-grant')
    case['events']=[]
    case['owner_grant']=entries
    case['grant_evidence'].update(additional=entries,extra_cost_usd=cost,scope=scope)
    case['facts']['owner_authority_verified']=authority
    actual=probe.evaluate_case(bundle,case)
    expose_trace(caplog)
    print('[IMP:9][test_grant_bounds_and_scope][VERIFY] supplied authority and bounded grant allowed=%s'%allowed)
    assert actual['repair_spent']==0
    assert actual['decision']==('ALLOW' if allowed else 'REFUSE')
    assert actual['refusal']==(None if allowed else 'CAP_INVALID')
# endregion FUNC_test_grant_bounds_and_scope


# region FUNC_test_bug_report_fields_require_populated_text [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify bug report fields require populated text.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('field,bad_value',[('goal',True),('dataAnalysis',[]),('recommendation','')])
def test_bug_report_fields_require_populated_text(repo_root,caplog,field,bad_value):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    case=next(case for case in json.loads((repo_root/'examples/flow-contract/cases.json').read_text()) if case['case_id']=='coder-origin')
    returned=case['events'][0]['value']
    returned['bugReport'][field]=bad_value
    actual=probe.validate_return(bundle,returned,case['facts'])
    expose_trace(caplog)
    print('[IMP:9][test_bug_report_fields_require_populated_text][VERIFY] malformed diagnostic field refused')
    assert actual=='RETURN_BUG_REPORT_REQUIRED'
# endregion FUNC_test_bug_report_fields_require_populated_text


# region FUNC_test_malformed_nested_scan_is_refused [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify malformed nested scan is refused.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('field,bad_value',[('id',[]),('id',{}),('reason',True),('evidence',1),('evidence',[1])])
def test_malformed_nested_scan_is_refused(repo_root,caplog,field,bad_value):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    case=next(case for case in json.loads((repo_root/'examples/flow-contract/cases.json').read_text()) if case['case_id']=='first-success')
    value=next(event['value'] for event in case['events'] if event.get('value',{}).get('phase')=='QA')
    value['scans'][0][field]=bad_value
    facts=dict(case['facts'],phase='QA',role='qa')
    actual=probe.validate_return(bundle,value,facts)
    expose_trace(caplog)
    print('[IMP:9][test_malformed_nested_scan_is_refused][VERIFY] malformed nested scan refused')
    assert actual in ('RETURN_SCAN_REQUIRED','RETURN_SCAN_EVIDENCE')
# endregion FUNC_test_malformed_nested_scan_is_refused


# region FUNC_test_malformed_grant_evidence_is_refused [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify malformed grant evidence is refused.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('bad_value',[1,True,'unstructured evidence',{}])
def test_malformed_grant_evidence_is_refused(repo_root,caplog,bad_value):
    caplog.set_level(logging.INFO,logger='flow_probe')
    bundle=probe.load_contract(repo_root)
    case=next(case for case in json.loads((repo_root/'examples/flow-contract/cases.json').read_text()) if case['case_id']=='explicit-grant')
    case['events']=[]
    case['grant_evidence']['evidence']=[bad_value]
    actual=probe.evaluate_case(bundle,case)
    expose_trace(caplog)
    print('[IMP:9][test_malformed_grant_evidence_is_refused][VERIFY] malformed grant evidence refused without spend')
    assert actual['decision']=='REFUSE' and actual['refusal']=='CAP_INVALID' and actual['repair_spent']==0
# endregion FUNC_test_malformed_grant_evidence_is_refused


# region FUNC_example_case [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Read a pristine generic case for isolated regression inputs.
## @io Repository root and case id -> fresh decoded case
## @complexity 7
def example_case(root,name):
    return next(case for case in json.loads((root/'examples/flow-contract/cases.json').read_text()) if case['case_id']==name)
# endregion FUNC_example_case


# region FUNC_test_initial_spend_rejected_before_debug [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify initial spend rejected before debug.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('spent',[-1,False,True,1.5,'1',None])
def test_initial_spend_rejected_before_debug(repo_root,caplog,spent):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    case=example_case(repo_root,'default-cap');case['facts']['repair_spent']=spent
    result=probe.evaluate_case(bundle,case);expose_trace(caplog)
    print('[IMP:9][test_initial_spend_rejected_before_debug][VERIFY] invalid accounting is refused before events')
    assert result['refusal']=='SPEND_INVALID' and result['next_phase']=='Bootstrap' and result['repair_spent']==spent
# endregion FUNC_test_initial_spend_rejected_before_debug


# region FUNC_test_role_payload_shape_refused_before_continuation [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify role payload shape refused before continuation.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('phase,field,bad',[
    ('Bootstrap','recommendations',None),('Bootstrap','files',[{'path':'absent.md','summary':'x','structure':'x','relevance':'x'}]),
    ('Architect','featureSlices',False),('Architect','acceptanceCriteria',None),('Architect','specBlocked',None),('Architect','mayEdit',None),
    ('Code','artifacts',[False]),('Code','artifacts',['absent.py']),('Code','testGuidePath','../absent-guide.md'),('Code','testSummary',' '),
    ('QA','testSummary',None),('QA','findings',{}),('QA','limitations',42),('Review','findings',None),
])
def test_role_payload_shape_refused_before_continuation(repo_root,caplog,phase,field,bad):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    case=example_case(repo_root,'first-success');value=next(event['value'] for event in case['events'] if event.get('value',{}).get('phase')==phase)
    value[field]=bad
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase=phase,role=bundle['actors'][phase])
    result=probe.evaluate_case(bundle,{'case_id':'typed-payload','facts':facts,'events':[{'kind':'return','value':value}]});expose_trace(caplog)
    print('[IMP:9][test_role_payload_shape_refused_before_continuation][VERIFY] malformed phase payload cannot advance')
    assert result['decision']=='REFUSE' and result['next_phase']==phase and result['repair_spent']==0
# endregion FUNC_test_role_payload_shape_refused_before_continuation


# region FUNC_test_qa_non_success_preserves_eight_scan_payload [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify qa non success preserves eight scan payload.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('status',['BUG_REPORT','BLOCKED'])
@pytest.mark.parametrize('field',['scans','testSummary','findings','limitations'])
def test_qa_non_success_preserves_eight_scan_payload(repo_root,caplog,status,field):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    case=example_case(repo_root,'first-success');value=next(event['value'] for event in case['events'] if event.get('value',{}).get('phase')=='QA')
    value['status']=status;value['reason']='Observed blocked or defective judgment';value['limitations']=[]
    value['bugReport']={field:'Observed actionable diagnostic' for field in ('goal','actual','logAnalysis','dataAnalysis','hypothesis','recommendation')}
    value['scans'][0]['status']='FAIL' if status=='BUG_REPORT' else 'BLOCKED'
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase='QA',role='qa')
    assert probe.validate_return(bundle,value,facts) is None
    del value[field]
    result=probe.evaluate_case(bundle,{'case_id':'qa-required-fields','facts':facts,'events':[{'kind':'return','value':value}]});expose_trace(caplog)
    print('[IMP:9][test_qa_non_success_preserves_eight_scan_payload][VERIFY] scan evidence applies to every QA status')
    assert result['decision']=='REFUSE' and result['next_phase']=='QA' and result['repair_spent']==0
# endregion FUNC_test_qa_non_success_preserves_eight_scan_payload



# region FUNC_test_actual_debug_fixed_return_renews_qa [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify actual debug fixed return renews qa.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_actual_debug_fixed_return_renews_qa(repo_root,caplog):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase='Debug',role='debugger',repair_spent=1,qa_verified=True,review_verified=True)
    evidence=example_case(repo_root,'coder-origin')['events'][0]['value']['evidence']
    value={'phase':'Debug','role':'debugger','status':'FIXED','summary':'Observed bounded fix','runId':'example-run','inputIdentity':'inputs-a','candidateIdentity':'candidate-a','contractVersion':'0.3.0','evidence':evidence,'rootCause':'Observed cause','fix':'Observed fix','filesTouched':['FORMAT.md'],'postFixAudit':'Scope checked','testSummary':'Observed post-fix test'}
    assert probe.validate_return(bundle,value,facts) is None
    result=probe.evaluate_case(bundle,{'case_id':'actual-debug-return','facts':facts,'events':[{'kind':'return','value':value}]});expose_trace(caplog)
    print('[IMP:9][test_actual_debug_fixed_return_renews_qa][VERIFY] actual FIXED retains spend and invalidates previous QA')
    assert result['decision']=='ALLOW' and result['next_phase']=='QA' and result['repair_spent']==1 and result['fresh'] is False
    for field in ('rootCause','fix','filesTouched','postFixAudit','testSummary'):
        value[field]=None
    assert probe.validate_return(bundle,value,facts)=='RETURN_DEBUG_INVALID'
# endregion FUNC_test_actual_debug_fixed_return_renews_qa



# region FUNC_test_activation_is_required_for_each_phase_return [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify activation is required for each phase return.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_activation_is_required_for_each_phase_return(repo_root,caplog):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    case=example_case(repo_root,'first-success');case['events']=[event for event in case['events'] if event['kind']!='activate']
    result=probe.evaluate_case(bundle,case);expose_trace(caplog)
    print('[IMP:9][test_activation_is_required_for_each_phase_return][VERIFY] omitted receipt refuses first action')
    assert result['refusal']=='ACTIVATION_MISSING' and result['next_phase']=='Bootstrap' and result['repair_spent']==0
# endregion FUNC_test_activation_is_required_for_each_phase_return


# region FUNC_test_visual_actual_threshold_and_scanned_output [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify visual actual threshold and scanned output.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('nodes,tests_only,status,scanned,allowed',[(2,False,'SKIPPED',None,True),(3,False,'SKIPPED',None,False),(3,True,'SKIPPED',None,True),(3,False,'PASS',0,False),(3,False,'PASS',1,True)])
def test_visual_actual_threshold_and_scanned_output(repo_root,caplog,nodes,tests_only,status,scanned,allowed):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    visual={'status':status,'componentNodes':nodes,'testsOnly':tests_only,'activation':'Actual finite component count','reason':'Actual threshold/exception','command':'example-check','exitCode':0,'output':'scannedNodes=%s'%scanned,'scannedNodes':scanned,'evidence':['FORMAT.md']}
    actual=probe.visual_error(bundle,visual);expose_trace(caplog)
    print('[IMP:9][test_visual_actual_threshold_and_scanned_output][VERIFY] actual applicability and nonempty scan constrain status')
    assert (actual is None)==allowed
# endregion FUNC_test_visual_actual_threshold_and_scanned_output



# region FUNC_test_declared_scan_hash_mismatch_is_refused [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify declared scan hash mismatch is refused.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_declared_scan_hash_mismatch_is_refused(repo_root,caplog):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    value=next(event['value'] for event in example_case(repo_root,'first-success')['events'] if event.get('value',{}).get('phase')=='QA')
    value['scans'][0]['evidence'][0]['sha256']='0'*64
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase='QA',role='qa')
    error=probe.validate_return(bundle,value,facts);expose_trace(caplog)
    print('[IMP:9][test_declared_scan_hash_mismatch_is_refused][VERIFY] a scan hash is checked as actual evidence')
    assert error=='RETURN_SCAN_EVIDENCE'
# endregion FUNC_test_declared_scan_hash_mismatch_is_refused


# region FUNC_test_malformed_nested_case_cli_exit_two [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify malformed nested case cli exit two.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('events,facts', [([None],{}),([1],{}),([{}],{}),([{'kind':None}],{}),([],None),([],[]),([],{ 'activationEvidence': []})])
def test_malformed_nested_case_cli_exit_two(repo_copy,tmp_path,events,facts):
    path=tmp_path/'nested-invalid.json';path.write_text(json.dumps([{'case_id':'nested-invalid','facts':facts,'events':events,'expected':{}}]))
    result=run_probe(repo_copy,path);print(result.stderr)
    assert result.returncode==2 and json.loads(result.stdout)=={'ok':False,'refusal':'CASE_INPUT_INVALID'}
# endregion FUNC_test_malformed_nested_case_cli_exit_two


# region FUNC_test_activation_receipt_guards_each_phase [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify activation receipt guards each phase.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('phase',['Bootstrap','Architect','Code','QA','Review','Debug','Finalize'])
def test_activation_receipt_guards_each_phase(repo_root,caplog,phase):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase=phase,repair_spent=1)
    facts['activationEvidence'].pop(phase)
    result=probe.evaluate_case(bundle,{'case_id':'phase-read-predicate','facts':facts,'events':[{'kind':'return','value':{}}]});expose_trace(caplog)
    print('[IMP:9][test_activation_receipt_guards_each_phase][VERIFY] missing current-phase receipt refuses before payload')
    assert result['refusal']=='ACTIVATION_MISSING' and result['next_phase']==phase and result['repair_spent']==1
# endregion FUNC_test_activation_receipt_guards_each_phase


# region FUNC_test_blocked_conditional_payloads [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify blocked conditional payloads.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('phase',['Bootstrap','Architect','Code','QA','Review','Debug','Finalize'])
def test_blocked_conditional_payloads(repo_root,caplog,phase):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    base=example_case(repo_root,'first-success');value=next(event['value'] for event in base['events'] if event.get('value',{}).get('phase')==('QA' if phase=='QA' else 'Bootstrap'))
    if phase=='Review':value['findings']=[]
    if phase in ('QA','Review'):value['limitations']=[]
    value.update(phase=phase,role=bundle['actors'][phase],status='BLOCKED',reason='Required environment unavailable',limitations=[])
    if phase=='Debug':value['rootCause']='Unavailable dependency diagnosed'
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase=phase,role=bundle['actors'][phase],repair_spent=1)
    assert probe.validate_return(bundle,value,facts) is None
    valid=probe.evaluate_case(bundle,{'case_id':'blocked-return','facts':facts,'events':[{'kind':'return','value':value},{'kind':'enter-debug'}]})
    assert valid['decision']=='BLOCKED' and valid['repair_spent']==1 and valid['next_phase']==phase
    for field in ('reason','limitations'):
        changed=dict(value);changed[field]=None
        assert probe.validate_return(bundle,changed,facts) is not None
    expose_trace(caplog)
    print('[IMP:9][test_blocked_conditional_payloads][VERIFY] conditional fields and terminal spend are preserved')
# endregion FUNC_test_blocked_conditional_payloads



# region FUNC_test_applicable_doxygen_current_record_and_refusals [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify applicable doxygen current record and refusals.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
def test_applicable_doxygen_current_record_and_refusals(repo_copy,caplog):
    caplog.set_level(logging.INFO,logger='flow_probe')
    build=subprocess.run(['doxygen','Doxyfile'],cwd=str(repo_copy),capture_output=True,text=True)
    print('[IMP:9][test_applicable_doxygen_current_record_and_refusals][BUILD] exit=%d stdout=%d stderr=%d'%(build.returncode,len(build.stdout),len(build.stderr)))
    assert build.returncode==0 and not build.stderr
    bundle=probe.load_contract(repo_copy)
    value=next(event['value'] for event in example_case(repo_copy,'first-success')['events'] if event.get('value',{}).get('phase')=='Code')
    facts=dict(example_case(repo_copy,'default-cap')['facts'],phase='Code',role='coder',doxygen_required=True,doxygen_final_check_verified=True)
    paths=['doxygen_output/xml/index.xml','doxygen_output/xml/flow__contract__probe_8py.xml','doxygen_output/xml/test__flow__contract_8py.xml']
    refs=[{'path':path,'sha256':hashlib.sha256((repo_copy/path).read_bytes()).hexdigest()} for path in paths]
    record={'applicable':True,'command':'doxygen Doxyfile','exitCode':build.returncode,'output':'exit=0; actual generated XML inspected','evidence':[refs[0]],'mapPath':refs[0],'fileChecks':refs[1:],'candidateIdentity':facts['candidateIdentity'],'inputIdentity':facts['inputIdentity']}
    value['doxygen']=record
    assert probe.validate_return(bundle,value,facts) is None
    for field,bad in [('exitCode',1),('exitCode',False),('candidateIdentity','previous-candidate'),('inputIdentity','previous-input'),('mapPath',{'path':paths[0],'sha256':'0'*64}),('mapPath','absent.xml'),('evidence',[]),('fileChecks',[]),('fileChecks',[{'path':paths[1],'sha256':'0'*64}])]:
        changed=dict(value);changed['doxygen']=dict(record);changed['doxygen'][field]=bad
        assert probe.validate_return(bundle,changed,facts)=='RETURN_DOXYGEN_REQUIRED'
    changed=dict(value);del changed['doxygen']
    assert probe.validate_return(bundle,changed,facts)=='RETURN_DOXYGEN_REQUIRED'
    waived=dict(value);waived['doxygen']={'applicable':False,'reason':'Producer claims exemption','evidence':['FORMAT.md']}
    assert probe.validate_return(bundle,waived,facts)=='RETURN_DOXYGEN_REQUIRED'
    assert probe.validate_return(bundle,value,dict(facts,doxygen_final_check_verified=False))=='RETURN_DOXYGEN_REQUIRED'
    expose_trace(caplog)
    print('[IMP:9][test_applicable_doxygen_current_record_and_refusals][VERIFY] real XML bytes checked; final Code ordering is supplied authenticated caller premise')
# endregion FUNC_test_applicable_doxygen_current_record_and_refusals


# region FUNC_test_finalize_actual_return_payload [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify finalize actual return payload.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('field,bad',[('report','absent-report.md'),('planPath',None),('testsPath',{}),('logPath',False),('doxygenPath','absent-xml'),('acceptanceEvidence',[]),('qaEvidence',None),('reviewEvidence',[{'path':'FORMAT.md','sha256':'0'*64}]),('liveEvidence',[]),('blastRadius',{}),('scopeDeviations',None),('limitations',None)])
def test_finalize_actual_return_payload(repo_root,caplog,field,bad):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    value=next(event['value'] for event in example_case(repo_root,'first-success')['events'] if event.get('value',{}).get('phase')=='Bootstrap')
    evidence=value['evidence'];value={key:value[key] for key in bundle['common_fields']}
    value.update(phase='Finalize',role='finalizer',report='FORMAT.md',classification='BROWNFIELD',planPath='FORMAT.md',testsPath='tests',logPath='FORMAT.md',doxygenPath='FORMAT.md',testSummary='Observed generic example',acceptanceEvidence=evidence,qaEvidence=evidence,reviewEvidence=evidence,liveEvidence=evidence,blastRadius={key:[] for key in ('added','modified','deleted','untracked')},scopeDeviations=[],limitations=[])
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase='Finalize',role='finalizer',repair_spent=1,qa_verified=True,review_verified=True)
    assert probe.validate_return(bundle,value,facts) is None
    valid=probe.evaluate_case(bundle,{'case_id':'final-return','facts':facts,'events':[{'kind':'return','value':value},{'kind':'enter-debug'}]})
    assert valid['decision']=='WAIT_OWNER' and valid['repair_spent']==1 and valid['next_phase']=='ResultGate'
    value[field]=bad
    assert probe.validate_return(bundle,value,facts)=='RETURN_FINALIZE_INVALID'
    expose_trace(caplog)
    print('[IMP:9][test_finalize_actual_return_payload][VERIFY] required report paths and nested evidence remain checked')
# endregion FUNC_test_finalize_actual_return_payload


# region FUNC_test_escalated_finalize_conditional_payload [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify escalated finalize conditional payload.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('field,bad',[('requiredRepair',None),('reason',[]),('limitations',False)])
def test_escalated_finalize_conditional_payload(repo_root,caplog,field,bad):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    base=next(event['value'] for event in example_case(repo_root,'first-success')['events'] if event.get('value',{}).get('phase')=='Bootstrap')
    value={key:base[key] for key in bundle['common_fields']};value.update(phase='Finalize',role='finalizer',status='ESCALATED_FINALIZE',requiredRepair='Source repair required',reason='Build defect observed',limitations=[])
    facts=dict(example_case(repo_root,'default-cap')['facts'],phase='Finalize',role='finalizer',repair_spent=1)
    result=probe.evaluate_case(bundle,{'case_id':'escalated-final-return','facts':facts,'events':[{'kind':'return','value':value},{'kind':'enter-debug'}]})
    assert result['decision']=='ESCALATE' and result['next_phase']=='Owner' and result['repair_spent']==1
    value[field]=bad
    assert probe.validate_return(bundle,value,facts)=='RETURN_FINALIZE_INVALID'
    expose_trace(caplog)
    print('[IMP:9][test_escalated_finalize_conditional_payload][VERIFY] explicit owner route locks subsequent Debug entry')
# endregion FUNC_test_escalated_finalize_conditional_payload


# region FUNC_test_activation_receipt_actual_assignments [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Verify activation receipt actual assignments.
## @io Real or isolated repository inputs -> assertions over actual evidence
## @complexity 7
@pytest.mark.parametrize('field,bad',[('rolePath','roles/coder.md'),('protocolPaths',['FORMAT.md']),('readEvidence',[]),('candidateIdentity','previous-candidate')])
def test_activation_receipt_actual_assignments(repo_root,caplog,field,bad):
    caplog.set_level(logging.INFO,logger='flow_probe');bundle=probe.load_contract(repo_root)
    case=example_case(repo_root,'default-cap');receipt=case['facts']['activationEvidence']['Bootstrap'];receipt[field]=bad
    error=probe.activation_error(bundle,receipt,'Bootstrap',case['facts']);expose_trace(caplog)
    print('[IMP:9][test_activation_receipt_actual_assignments][VERIFY] caller assignments and current readable receipts agree')
    assert error=='ACTIVATION_MISSING'
# endregion FUNC_test_activation_receipt_actual_assignments

