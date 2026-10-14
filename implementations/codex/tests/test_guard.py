# region MODULE_CONTRACT [DOMAIN(10): SafeguardTesting; CONCEPT(10): ImmutableBinding, ContraryControls; TECH(8): pytest, subprocess]
## @modulecontract
## @purpose Independently distinguish granted ordinary effects from foreign/protected/unknown effects through the actual guard.
## @scope Synthetic source-stage fixtures and real standalone processes only; native AC7 remains held.
## @input Current shipped source, immutable synthetic parent policy/definition pins and owned pytest resources.
## @output Fixed direct assertions, literal process receipts and visible safe stderr trajectories.
## @links [USES_API(9): guard_destructive.load_policy, guard_destructive.classify_event, guard_destructive.main; READS_DATA_FROM(8): shipped hooks, manifest, layout, adapter]
## @invariants
## - Candidate destructive commands and SQL are data and never executed.
## - Expected verdicts precede observations; no-veto and denial traverse the same kernel.
## - Fixture source/Git is isolated; parent bindings are outside worker effect roots and original source remains read-only.
## @rationale
## Q: Why both direct calls and process cases?
## A: Direct logic and actual process streams/exit prove different properties; neither proves native interception.
## Q: Why literal receipts?
## A: Policy contents cannot authenticate their own invocation; each synthetic process pins its rendered definition separately.
## @changes
## LAST_CHANGE: [2.3.0 - C3 direct and real-process source-stage controls with explicit native deferral.]
## @modulemap
## FUNC 9[Fixture or independent guard behavior] => test_guard.digest
## FUNC 9[Fixture or independent guard behavior] => test_guard.fixture_binding
## FUNC 9[Fixture or independent guard behavior] => test_guard.decide
## FUNC 9[Fixture or independent guard behavior] => test_guard.process_case
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_policy_binding_refuses_tampering
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_effects_preserve_foreign_state
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_shell_ownership_and_unknown_effects
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_git_free_scratch_and_protected_parents
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_real_handler_process
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_complete_source_guard_binding
## FUNC 9[Fixture or independent guard behavior] => test_guard.test_source_definition_is_synchronous_and_bound
## FUNC 10[Security field adversarial matrix] => test_guard.test_security_field_matrix
## FUNC 10[Effective destinations and recursive reads] => test_guard.test_effective_destinations_and_recursive_reads
## @usecases
## - [test_real_handler_process]: Parent fixture -> documented CLI -> actual safe denial/no-veto streams and immutable source.
## - [test_effects_preserve_foreign_state]: Judge -> granted/foreign matrix -> exact expected decisions and unchanged sentinels.
## @GREP_SUMMARY guard tests, parent binding, hardlink, scratch, source, Git, shell, heredoc, patch, denial, no-veto, native held
## @STRUCTURE ▶ owned fixture → ◇ pinned policy → ○ direct or actual process → ◇ fixed outcome/trace → ⎋ receipts
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import copy
import hashlib
import importlib.util
import json
import logging
import os
from pathlib import Path
import shlex
import stat
import subprocess
import sys

import pytest

PACKAGE = Path(__file__).resolve().parents[1]
HANDLER = PACKAGE / 'hooks/guard_destructive.py'
DEFINITION = PACKAGE / 'hooks/hooks.json'
SPEC = importlib.util.spec_from_file_location('c3_guard', HANDLER)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)
LOGGER = logging.getLogger(__name__)


# region FUNC_digest [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Measure fixture file bytes without executing them.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 1
def digest(path):
    # START_BLOCK_FixtureAndAssertions
    return hashlib.sha256(path.read_bytes()).hexdigest()
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_digest


# region FUNC_fixture_binding [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Build explicitly synthetic parent policy, isolated committed source and git-free worker resources.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 3
def fixture_binding(tmp_path, profile='writable'):
    # START_BLOCK_FixtureAndAssertions
    source = tmp_path / 'source'; source.mkdir()
    scratch = tmp_path / 'worker'; scratch.mkdir()
    binding = tmp_path / 'parent-binding'; binding.mkdir()
    (source / 'a.py').write_text('VALUE = 1\n')
    (scratch / 'owned.txt').write_text('owned\n')
    git = ['/usr/bin/git', '-c', 'user.name=Fixture', '-c', 'user.email=fixture'+'@'+'example.invalid', '-c', 'init.defaultBranch=main']
    for args in (['init','-q',str(source)], ['-C',str(source),'add','a.py'], ['-C',str(source),'commit','-qm','fixture']):
        subprocess.run(git+args,check=True,capture_output=True)
    policy_path = binding / 'policy.json'; policy_path.write_text('{}'); policy_path.chmod(0o444)
    entries = []
    protected = {policy_path, HANDLER, DEFINITION}
    protected |= {p.parent for p in tuple(protected)}
    for path in sorted(protected):
        info = path.lstat()
        entries.append({'path':str(path),'type':'file' if path.is_file() else 'directory','mode':stat.S_IMODE(info.st_mode),'device':info.st_dev,'inode':info.st_ino})
    policy = {'version':1,'profile':profile,'grant':'synthetic-parent-fixture-only','session_id':'synthetic-C3',
              'source_roots':[str(source)],'protected_roots':[], 'git_roots':[str(source/'.git')],
              'worker_write_roots':[str(scratch)],'effects':[{'path':str(scratch),'operations':['read','write','create','delete','mode'],'recursive':True}],
              'scratch_roots':[str(scratch)],'evidence_roots':[],'checks':[{'command':command,'cwd':str(source),'files':[{'path':str(source/'.git/config'),'sha256':digest(source/'.git/config'),'mode':stat.S_IMODE((source/'.git/config').stat().st_mode)},{'path':'/usr/bin/git','sha256':digest(Path('/usr/bin/git')),'mode':stat.S_IMODE(Path('/usr/bin/git').stat().st_mode)}],'effects':[]} for command in ('git status --short','git diff --stat','git rev-parse --show-toplevel',f'git --git-dir="{source}/.git" --work-tree="{source}" status')],
              'binding':{'policy_path':str(policy_path),'policy_mode':0o444,'handler_path':str(HANDLER),'handler_mode':stat.S_IMODE(HANDLER.stat().st_mode),
                         'definition_path':str(DEFINITION),'definition_mode':stat.S_IMODE(DEFINITION.stat().st_mode),'definition_sha256':digest(DEFINITION),'entries':entries}}
    policy_path.chmod(0o644); policy_path.write_text(json.dumps(policy)); policy_path.chmod(0o444)
    event = {'hook_event_name':'PreToolUse','session_id':'synthetic-C3','cwd':str(source),'tool_name':'Bash','tool_input':{'command':'echo ready'}}
    pins = ['--policy',str(policy_path),'--policy-sha256',digest(policy_path),'--handler-sha256',digest(HANDLER)]
    # The exact rendered definition and literal invocation receipt live outside worker effects.
    rendered = copy.deepcopy(json.loads(DEFINITION.read_text()))
    command = ' '.join(shlex.quote(x) for x in [sys.executable,'-B',str(HANDLER)]+pins)
    rendered['hooks']['PreToolUse'][0]['hooks'][0]['command'] = command
    rendered_path = binding / 'rendered-hooks.json'; rendered_path.write_text(json.dumps(rendered)); rendered_path.chmod(0o444)
    receipt = {'authority':'synthetic parent fixture, not native','argv':[sys.executable,'-B',str(HANDLER)]+pins,'cwd':str(source),'policy_sha256':digest(policy_path),'handler_sha256':digest(HANDLER),'source_definition_sha256':digest(DEFINITION),'rendered_definition_sha256':digest(rendered_path),'rendered_definition':str(rendered_path)}
    (binding/'invocation-receipt.json').write_text(json.dumps(receipt,indent=2))
    loaded = guard.load_policy(str(policy_path),pins[3],pins[5])
    return loaded,event,pins,scratch,source,binding
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_fixture_binding


# region FUNC_decide [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Exercise the shipped importable event kernel directly.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 2
def decide(policy, event, command, tool='Bash'):
    # START_BLOCK_FixtureAndAssertions
    value = copy.deepcopy(event); value['tool_name']=tool; value['tool_input']={'command':command}
    records=[]
    window=logging.Handler();window.emit=records.append;guard.LOGGER.addHandler(window);guard.LOGGER.setLevel(logging.INFO)
    try: result=guard.classify_event(value,policy)['decision']
    finally: guard.LOGGER.removeHandler(window)
    messages=[r.getMessage() for r in records]
    print('\n'.join(m for m in messages if '[IMP:9]' in m or '[IMP:10]' in m))
    assert sum('[classify_event][START]' in m for m in messages)==1
    errors=[r.getMessage() for r in records if r.levelno>=logging.ERROR]
    if result=='no-veto':
        assert not errors and sum('[classify_event][VALID]' in m for m in messages)==1
        assert '[classify_event][VALID]' in messages[-1]
    else:
        assert len(errors)==2 and '[classify_event][REFUSE] event-or-effect' in errors[-1]
        assert '[REFUSE]' in errors[0] and '[IMP:10]' in errors[0]
    return result
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_decide


# region FUNC_process_case [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Exercise the actual standalone process and preserve immutable literal invocation receipts.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 1
def process_case(pins,event,binding,interpreter=None):
    # START_BLOCK_FixtureAndAssertions
    receipt=json.loads((binding/'invocation-receipt.json').read_text())
    argv=[interpreter or sys.executable,'-B',str(HANDLER)]+pins
    # Every no-veto case records actual literal argv, not a guessed host route.
    before={str(p):digest(p) for p in [Path(pins[1]),HANDLER,DEFINITION]}
    done=subprocess.run(argv,input=json.dumps(event).encode(),capture_output=True,cwd=event['cwd'],env={'PATH':os.defpath,'PYTHONDONTWRITEBYTECODE':'1'},timeout=15)
    after={str(p):digest(p) for p in [Path(pins[1]),HANDLER,DEFINITION]}
    assert before==after
    record={'synthetic':True,'argv':argv,'cwd':event['cwd'],'receipt':receipt,'before':before,'after':after,'exit':done.returncode,'stdout':done.stdout.decode(),'stderr':done.stderr.decode()}
    existing=list(binding.glob('process-*.json'))
    (binding/('process-%03d.json'%len(existing))).write_text(json.dumps(record,indent=2))
    return done
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_process_case


# region FUNC_test_policy_binding_refuses_tampering [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify policy binding refuses tampering through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 4
def test_policy_binding_refuses_tampering(tmp_path,caplog):
    LOGGER.info('[IMP:4][test_policy_binding_refuses_tampering][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    caplog.set_level(logging.INFO)
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    assert decide(policy,event,'echo ordinary')=='no-veto'
    for mutate in ('role','approval','roots','session'):
        changed=copy.deepcopy(event)
        if mutate=='session': changed['session_id']='foreign'
        else: changed[mutate]='synthetic-secret-value'
        assert guard.classify_event(changed,policy)['decision']=='deny'
    for raw in (b'{"role":1,"role":2}',b'[]',b'NaN',b'{} trailing',b'\xff',b' '*65537):
        with pytest.raises((ValueError,UnicodeError)): guard.strict_json(raw)
    with pytest.raises(ValueError): guard.load_policy(pins[1],'0'*64,pins[5])
    with pytest.raises(ValueError): guard.load_policy(pins[1],pins[3],'0'*64)
    path=Path(pins[1]); path.chmod(0o644)
    with pytest.raises(ValueError): guard.load_policy(pins[1],pins[3],pins[5])
    path.chmod(0o444)
    original=path.read_bytes(); path.chmod(0o644); path.write_bytes(original+b' ');path.chmod(0o444)
    with pytest.raises(ValueError): guard.load_policy(pins[1],pins[3],pins[5])
    path.chmod(0o644);path.write_bytes(original);path.chmod(0o444)
    altered=copy.deepcopy(policy); altered['binding']['entries'][0]['inode']+=1
    path.chmod(0o644);path.write_text(json.dumps(altered));path.chmod(0o444)
    with pytest.raises(ValueError): guard.load_policy(pins[1],digest(path),pins[5])
    messages=[r.getMessage() for r in caplog.records];print('\n'.join(messages))
    assert any('[IMP:9][load_policy][VALID]' in x for x in messages)
    assert any('[IMP:10]' in x for x in messages)
    assert not any('synthetic-secret-value' in x or pins[1] in x or pins[3] in x for x in messages)
    LOGGER.info('[IMP:9][test_policy_binding_refuses_tampering][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_policy_binding_refuses_tampering


# region FUNC_test_effects_preserve_foreign_state [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify effects preserve foreign state through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 4
@pytest.mark.parametrize('profile',['readonly','writable'])
def test_effects_preserve_foreign_state(tmp_path,profile,caplog):
    LOGGER.info('[IMP:4][test_effects_preserve_foreign_state][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    caplog.set_level(logging.INFO)
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path,profile)
    foreign=tmp_path/'foreign'; foreign.mkdir();(foreign/'owned.txt').write_text('foreign\n')
    positive=[f'touch "{scratch}/new file.txt"',f'rm -rf "{scratch}/cache"',f'mkdir -p "{scratch}/cache"',f'echo text > "{scratch}/owned.txt"',f'cp "{source}/a.py" "{scratch}/copy.py"',f'mv "{scratch}/owned.txt" "{scratch}/moved.txt"',f'chmod 600 "{scratch}/owned.txt"',f'find "{scratch}" -delete','git status --short','git diff --stat','cat a.py']
    negative=[f'touch "{foreign}/new.txt"',f'rm -rf "{foreign}/build"',f'find "{foreign}" -delete','touch a.py','git fetch','git update-ref refs/heads/x HEAD','git hash-object -w a.py','git config a.b c',f'git --git-dir="{foreign}" status',f'git --work-tree="{foreign}" status',f'git -C "{foreign}" status',f'chmod 600 "{binding}"',f'rm -rf "{binding}"','python3 -c "print(1)"']
    (source/'a.py').write_text('VALUE = 2\n')
    subprocess.run(['/usr/bin/git','-C',str(source),'add','a.py'],check=True,capture_output=True)
    (source/'a.py').write_text('VALUE = 3\n')
    (source/'untracked.txt').write_text('untracked\n')
    (source/'.gitignore').write_text('ignored.txt\n'); (source/'ignored.txt').write_text('ignored\n')
    original_metadata={str(p.relative_to(source)):digest(p) for p in source.rglob('*') if p.is_file()}
    before=(source/'a.py').read_bytes(),(scratch/'owned.txt').read_bytes(),(foreign/'owned.txt').read_bytes()
    for command in positive: assert decide(policy,event,command)=='no-veto'
    for command in negative: assert decide(policy,event,command)=='deny'
    for command in (f'git --git-dir="{source}/.git" --work-tree="{source}" status','git rev-parse --show-toplevel'): assert decide(policy,event,command)=='no-veto'
    patch='*** Begin Patch\n*** Add File: '+str(scratch/'new file.txt')+'\n+data\n*** End Patch'
    assert decide(policy,event,patch,'apply_patch')=='no-veto'
    assert decide(policy,event,patch.replace(str(scratch),str(foreign)),'apply_patch')=='deny'
    assert decide(policy,event,patch[:-len('*** End Patch')]+'*** Delete File: a.py\n*** End Patch','apply_patch')=='deny'
    assert before==((source/'a.py').read_bytes(),(scratch/'owned.txt').read_bytes(),(foreign/'owned.txt').read_bytes())
    assert original_metadata=={str(p.relative_to(source)):digest(p) for p in source.rglob('*') if p.is_file()}
    assert not (scratch/'new file.txt').exists()
    print('positive controls',len(positive),'negative controls',len(negative),'source unchanged')
    assert not any('synthetic-secret' in r.getMessage() for r in caplog.records)
    LOGGER.info('[IMP:9][test_effects_preserve_foreign_state][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_effects_preserve_foreign_state


# region FUNC_test_shell_ownership_and_unknown_effects [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify shell ownership and unknown effects through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 2
def test_shell_ownership_and_unknown_effects(tmp_path,monkeypatch,caplog):
    LOGGER.info('[IMP:4][test_shell_ownership_and_unknown_effects][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    caplog.set_level(logging.INFO)
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    assert decide(policy,event,f'X={scratch}; touch $X/one; echo ready')=='deny'
    assert decide(policy,event,f'touch "{scratch}/one"; echo ready')=='no-veto'
    assert decide(policy,event,f'cd "{scratch}"; touch two')=='no-veto'
    assert decide(policy,event,"cat <<'SQL'\nDROP TABLE users; rm -rf /\nSQL")=='no-veto'
    assert decide(policy,event,"sqlite3 app.db <<'SQL'\nDROP TABLE users;\nSQL")=='deny'
    assert decide(policy,event,"cat <<'SQL'\nDROP TABLE users;\nSQL\nsqlite3 app.db 'SELECT 1'")=='deny'
    for command in ('touch $UNKNOWN/x','echo $(id)','cat < a.py','cat a.py | cat','env touch a.py','GIT_DIR=x git status','while true; do echo x; done',"sh -c 'sh -c \"sh -c echo\"'",f'cd {scratch} && touch x','rm -rf *','rm --rec --for x',"cat <<EOF\nx\nEOF",'git status --output=out',"X='owned foreign'; rm $X",'PATH=/foreign touch x','LD_PRELOAD=x echo ordinary','IFS=x echo ordinary','BASH_ENV=x echo ordinary',"printf -v out '%s' payload","printf '%n' name"):
        assert decide(policy,event,command)=='deny'
    assert decide(policy,event,"sh -c 'echo ordinary'")=='no-veto'
    monkeypatch.setattr(guard.subprocess,'run',lambda *a,**k: (_ for _ in ()).throw(OSError()))
    assert decide(policy,event,'git status')=='deny'
    errors=[r.getMessage() for r in caplog.records if r.levelno>=logging.ERROR]
    print('\n'.join(errors)); assert any('git-probe' in x for x in errors)
    LOGGER.info('[IMP:9][test_shell_ownership_and_unknown_effects][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_shell_ownership_and_unknown_effects


# region FUNC_test_git_free_scratch_and_protected_parents [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify git free scratch and protected parents through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 2
def test_git_free_scratch_and_protected_parents(tmp_path):
    LOGGER.info('[IMP:4][test_git_free_scratch_and_protected_parents][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    for path in (scratch/'.git',):
        path.write_text('gitdir: '+str(source/'.git'))
        with pytest.raises(ValueError): guard.git_free(str(scratch))
        path.unlink()
    linked=scratch/'link'; linked.symlink_to(source/'a.py')
    assert decide(policy,event,f'touch {linked}')=='deny'
    linked.unlink()
    alias=scratch/'hardlink';os.link(pins[1],alias)
    assert decide(policy,event,f'touch {alias}')=='deny'
    assert decide(policy,event,f'rm -rf {scratch}')=='deny'
    alias.unlink()
    target=Path(pins[1]); st=target.stat(); old=target.read_bytes(); target.chmod(0o644);target.unlink();target.write_bytes(old);target.chmod(0o444)
    assert target.stat().st_ino!=st.st_ino
    with pytest.raises(ValueError): guard.load_policy(pins[1],digest(target),pins[5])
    LOGGER.info('[IMP:9][test_git_free_scratch_and_protected_parents][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_git_free_scratch_and_protected_parents


# region FUNC_test_real_handler_process [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify real handler process through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 1
@pytest.mark.parametrize('interpreter',[sys.executable,'/usr/bin/python3'])
def test_real_handler_process(tmp_path,interpreter):
    LOGGER.info('[IMP:4][test_real_handler_process][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    event['tool_input']['command']=f'touch "{scratch}/benign sentinel"'
    result=process_case(pins,event,binding,interpreter)
    print(result.stderr.decode());assert result.returncode==0 and result.stdout==b''
    assert not (scratch/'benign sentinel').exists()
    messages=result.stderr.decode().splitlines()
    assert sum('[main][RESULT] no-veto' in x for x in messages)==1
    assert next(i for i,x in enumerate(messages) if '[load_policy][VALID]' in x)<next(i for i,x in enumerate(messages) if '[classify_event][VALID]' in x)<next(i for i,x in enumerate(messages) if '[main][RESULT]' in x)
    assert not any('[IMP:10]' in x for x in messages)
    event['tool_input']['command']='touch synthetic-secret-path'
    denied=process_case(pins,event,binding,interpreter)
    out=json.loads(denied.stdout)['hookSpecificOutput'];assert out['permissionDecision']=='deny' and denied.returncode==0
    assert b'synthetic-secret' not in denied.stdout+denied.stderr
    bad=subprocess.run([interpreter,'-B',str(HANDLER)],input=b'{}',capture_output=True)
    assert bad.returncode==2 and bad.stdout==b'' and b'invocation-shape' in bad.stderr
    oversized=subprocess.run([interpreter,'-B',str(HANDLER)]+pins,input=b' '*65537,capture_output=True)
    assert oversized.returncode==2 and oversized.stdout==b''
    LOGGER.info('[IMP:9][test_real_handler_process][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_real_handler_process



# region FUNC_test_security_field_matrix [DOMAIN(10): GuardTesting; CONCEPT(10): BindingGrammar; TECH(8): pytest]
## @purpose Refuse every security shape family through real pinned policy loading and preserve ordinary controls.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, test_guard.fixture_binding
## @io Input: owned tmp_path, caplog. Output: fixed policy/event/alias assertions; expected ValueError on security failures, no unrelated ERROR. Owned fixture bytes restored after each case. O(matrix), importance10. Example: boolean version and changed definition hash refuse while unchanged policy passes.
## @complexity 6
def test_security_field_matrix(tmp_path,caplog):
    LOGGER.info('[IMP:4][test_security_field_matrix][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    caplog.set_level(logging.INFO)
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    original=Path(pins[1]).read_bytes()
    variants=[]
    for key,value in [('version',True),('unknown',1),('profile','qa'),('worker_write_roots',[str(binding)]),('effects',[{'path':str(scratch),'operations':['write','write'],'recursive':True}])]:
        altered=copy.deepcopy(policy);altered[key]=value;variants.append(altered)
    for key,value in [('definition_sha256','0'*64),('definition_path',str(source/'a.py')),('handler_mode',0o777),('entries',[])]:
        altered=copy.deepcopy(policy);altered['binding'][key]=value;variants.append(altered)
    for altered in variants:
        path=Path(pins[1]);path.chmod(0o644);path.write_text(json.dumps(altered));path.chmod(0o444)
        caplog.clear()
        with pytest.raises(ValueError):guard.load_policy(str(path),digest(path),pins[5])
        errors=[r.getMessage() for r in caplog.records if r.levelno>=logging.ERROR]
        print('\n'.join(errors));assert len(errors)==1 and '[REFUSE]' in errors[0]
    path.chmod(0o644);path.write_bytes(original);path.chmod(0o444)
    caplog.clear();guard.load_policy(str(path),pins[3],pins[5]);assert not any(r.levelno>=logging.ERROR for r in caplog.records)
    for data in ({'command':'echo ready','timeout_ms':True},{'command':'echo ready','roots':[]},{'command':'echo ready','workdir':str(source/'missing')}, {'command':3}):
        changed=copy.deepcopy(event);changed['tool_input']=data
        assert guard.classify_event(changed,policy)['decision']=='deny'
    # Changed type/path and environment fallback cannot replace literal invocation pins.
    alias=binding/'policy-link.json';alias.symlink_to(path)
    with pytest.raises(ValueError):guard.load_policy(str(alias),pins[3],pins[5])
    env=dict(os.environ,METHODOLOGY_POLICY=str(path),POLICY_SHA256=pins[3],HANDLER_SHA256=pins[5],PYTHONDONTWRITEBYTECODE='1')
    done=subprocess.run([sys.executable,'-B',str(HANDLER)],input=b'{}',env=env,capture_output=True)
    assert done.returncode==2 and done.stdout==b''
    for raw in (b'{"session_id":"synthetic","session_id":"synthetic-secret"}',b'[]',b'not json',b'\xff'):
        outcome=subprocess.run([sys.executable,'-B',str(HANDLER)]+pins,input=raw,capture_output=True)
        assert outcome.returncode==2 and outcome.stdout==b'' and b'synthetic-secret' not in outcome.stderr
    malformed=copy.deepcopy(event);malformed['tool_name']='unknown-specialized-tool'
    outcome=process_case(pins,malformed,binding)
    assert outcome.returncode==0 and json.loads(outcome.stdout)['hookSpecificOutput']['permissionDecision']=='deny'
    LOGGER.info('[IMP:9][test_security_field_matrix][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_security_field_matrix

# region FUNC_test_effective_destinations_and_recursive_reads [DOMAIN(10): GuardTesting; CONCEPT(10): CompleteEffects; TECH(8): pytest]
## @purpose Distinguish effective copy destinations, recursive protected children and forbidden environment/output semantics.
## @uses test_guard.fixture_binding, test_guard.decide
## @io Input: owned tmp_path. Output: exact positive/negative decisions and untouched sentinel bytes; AssertionError on gap. Fixture-only writes; no candidate command executes. O(matrix), importance10. Example: granted directory with a protected child denies recursive rg.
## @complexity 2
def test_effective_destinations_and_recursive_reads(tmp_path):
    LOGGER.info('[IMP:4][test_effective_destinations_and_recursive_reads][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    directory=scratch/'destination';directory.mkdir()
    assert decide(policy,event,f'cp "{source}/a.py" "{directory}"')=='no-veto'
    narrowed=copy.deepcopy(policy);narrowed['effects']=[{'path':str(directory),'operations':['write'],'recursive':False}]
    assert decide(narrowed,event,f'cp "{source}/a.py" "{directory}"')=='deny'
    assert decide(policy,event,f'cp -R "{source}" "{directory}"')=='deny'
    (directory/'secret.txt').write_text('synthetic')
    protected=copy.deepcopy(policy);protected['protected_roots']=[str(directory/'secret.txt')]
    assert decide(protected,event,f'rg -n needle "{directory}"')=='deny'
    assert decide(policy,event,f'rg -n needle "{scratch}/owned.txt"')=='no-veto'
    for command in ('printf -v variable %s payload', 'printf %n variable', "X='owned foreign'; rm $X", 'PATH=x echo ready', 'LD_PRELOAD=x echo ready'):
        assert decide(policy,event,command)=='deny'
    assert decide(policy,event,"printf '%s' ordinary")=='no-veto'
    write_only=copy.deepcopy(policy);write_only['effects']=[{'path':str(scratch),'operations':['read','write'],'recursive':True}]
    assert decide(write_only,event,f'touch "{scratch}/owned.txt"')=='no-veto'
    assert decide(write_only,event,f'touch "{scratch}/absent.txt"')=='deny'
    assert decide(write_only,event,f'echo data > "{scratch}/absent.txt"')=='deny'
    patch='*** Begin Patch\n*** Add File: '+str(scratch/'absent.txt')+'\n+data\n*** End Patch'
    assert decide(write_only,event,patch,'apply_patch')=='deny'
    exact=copy.deepcopy(policy);exact['effects']=[{'path':str(scratch/'missing/child'),'operations':['write','create'],'recursive':False}]
    assert decide(exact,event,f'touch "{scratch}/missing/child"')=='deny'
    assert decide(policy,event,f'touch "{scratch}/missing/child"')=='no-veto'
    assert decide(policy,event,f'touch "{scratch}/.git"')=='deny'
    assert not list(directory.glob('a.py'))
    LOGGER.info('[IMP:9][test_effective_destinations_and_recursive_reads][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_effective_destinations_and_recursive_reads

# region FUNC_test_complete_source_guard_binding [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify complete source guard binding through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 1
def test_complete_source_guard_binding():
    LOGGER.info('[IMP:4][test_complete_source_guard_binding][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    layout=json.loads((PACKAGE/'references/package-layout.json').read_text())
    assert layout['version']=='2.3.0' and len(layout['files'])==77
    kinds={r['path']:r['kind'] for r in layout['files']}
    assert {p:kinds[p] for p in ('hooks/guard_destructive.py','hooks/hooks.json','references/safeguards.md','tests/test_guard.py')}=={'hooks/guard_destructive.py':'helper','hooks/hooks.json':'config','references/safeguards.md':'documentation','tests/test_guard.py':'test'}
    assert sum(x=='helper' for x in kinds.values())==7 and sum(x=='skill' for x in kinds.values())==27
    manifest=json.loads((PACKAGE/'.codex-plugin/plugin.json').read_text())
    assert manifest['version']=='2.3.0' and manifest['hooks']=='./hooks/hooks.json'
    assert len(layout['roles'])==6
    adapter=json.loads((PACKAGE/'adapter.json').read_text());assert adapter['spec_version']=='1.1.0' and adapter['spec_root']=='../../'
    LOGGER.info('[IMP:9][test_complete_source_guard_binding][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_complete_source_guard_binding


# region FUNC_test_source_definition_is_synchronous_and_bound [DOMAIN(9): GuardTesting; CONCEPT(9): ContraryControls; TECH(7): pytest]
## @purpose Verify source definition is synchronous and bound through fixed independent expectations.
## @uses guard_destructive.load_policy, guard_destructive.classify_event, pathlib, pytest
## @io Input: actual owned pytest tmp_path/parameter fixtures where declared; no shared writes. Output: fixed assertions or fixture values; AssertionError identifies a failed promised property, OSError/ValueError preserves fixture failures. Side effects: only owned fixture/resources and actual handler children; no candidate destructive command or native hook execution. Complexity O(fixture population); importance9. Example: granted scratch positive and foreign sibling negative distinguish the decision.
## @complexity 1
def test_source_definition_is_synchronous_and_bound(tmp_path):
    LOGGER.info('[IMP:4][test_source_definition_is_synchronous_and_bound][START] owned criterion verification')
    # START_BLOCK_FixtureAndAssertions
    policy,event,pins,scratch,source,binding=fixture_binding(tmp_path)
    definition=json.loads(DEFINITION.read_text())
    assert set(definition['hooks'])=={'PreToolUse'}
    item=definition['hooks']['PreToolUse'][0];assert item['matcher']=='*' and len(item['hooks'])==1
    hook=item['hooks'][0];assert set(hook)=={'type','command','timeout'} and hook['type']=='command' and hook['timeout']==10
    assert hook['command']=='python3 -B "$PLUGIN_ROOT/hooks/guard_destructive.py"'
    assert not any(x in hook['command'] for x in ('||',';','--trust','--approve'))
    rendered=json.loads((binding/'rendered-hooks.json').read_text())
    command=rendered['hooks']['PreToolUse'][0]['hooks'][0]['command']
    done=subprocess.run(command,shell=True,input=json.dumps(event),capture_output=True,text=True,cwd=event['cwd'],env={'PATH':os.defpath,'PYTHONDONTWRITEBYTECODE':'1'},timeout=15)
    assert done.returncode==0 and done.stdout=='' and '[main][RESULT] no-veto' in done.stderr
    unbound=subprocess.run([sys.executable,'-B',str(HANDLER)],input='{}',capture_output=True,text=True)
    assert unbound.returncode==2 and not unbound.stdout
    receipt=json.loads((binding/'invocation-receipt.json').read_text())
    assert receipt['rendered_definition_sha256']==digest(binding/'rendered-hooks.json') and receipt['source_definition_sha256']==digest(DEFINITION)
    LOGGER.info('[IMP:9][test_source_definition_is_synchronous_and_bound][VALID] fixed assertions completed')
    # END_BLOCK_FixtureAndAssertions
# endregion FUNC_test_source_definition_is_synchronous_and_bound
