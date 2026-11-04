# region MODULE_CONTRACT
## @modulecontract
## @purpose Own schema3 causal accounting and immutable historical import, without launching workers.
## @scope One parent writer and one target storage domain; no distributed/exactly-once/power-loss promise.
## @input Validated source-bound run state; explicit parent approval, investigation and owned evidence paths.
## @output Atomic JSON checkpoints/reservations and immutable terminal evidence; malformed/unknown paths refuse.
## @invariants Historical bytes are never rewritten; unknown release is never inferred absent; costs may remain unknown.
## @rationale Parent authenticates consent and worker identity; structural validation cannot establish either.
## @links [USES_API(8): pathlib; USES_API(8): json]
## @changes
## LAST_CHANGE: [5.0.0 - CONT-BOUND independent-review repair: amended admission, full input freshness, refusal/cost retention and owned LDD.]
## @modulemap
## FUNC 9[Refuse redirected/escaping storage before writes] => continuation.storage_path
## FUNC 4[Metadata anchor] => continuation._module_contract
## FUNC 9[None when true, else ValueError(reason) with safe own ERROR] => continuation.require
## FUNC 4[canonical SHA256 hex str] => continuation.digest
## FUNC 9[None after UTF8 publication] => continuation.atomic
## FUNC 4[Path target/] => continuation.authority
## FUNC 9[None if exact lineage surface, causal digest, plain original_cap0] => continuation.shape
## FUNC 9[None] => continuation.check_grant
## FUNC 9[SAME state dict with one fresh lineage, admissions/current spec, unknown cost history and original a] => continuation.new_lineage
## FUNC 9[None after exclusive lineage folder, admission markers and enrollment publication] => continuation.enroll
## FUNC 9[exact mutable reservation dict within state] => continuation.active
## FUNC 9[newly attached reservation dict (id/run/phase/candidate/input/fund/charge/state/worker/evidence/usd)] => continuation.prepare
## FUNC 9[None; changes that entry to complete, retains charge, closes retry scopes and clears active ID in me] => continuation.complete
## FUNC 9[canonical authority Path after current bindings/candidate, exact persisted revision, newest immutabl] => continuation.committed
## FUNC 9[None after single-writer revision check, immutable terminal publication when closed, exclusive revis] => continuation.persist
## FUNC 4[dict naming actual native5/neutral4] => continuation.capabilities
## FUNC 9[(historical dict, aggregate spent int, original cap int, immutable file identity list)] => continuation.historical
## FUNC 9[None after required plan/scope and current Code/QA/Review input/scope/artifact identities; Debug als] => continuation.predicates
## FUNC 9[(canonical Path, newly persisted successor state dict)] => continuation.continue_run
## FUNC 9[updated persisted state dict] => continuation.reservation_operation
## FUNC 9[persisted state dict] => continuation.episode
## FUNC 9[None after every adopted spec has a regular exact admission marker pointing to the same canonical au] => continuation.check_admissions
## FUNC 9[None after exclusive current-spec marker creation, or verification of its identical existing owner] => continuation.adopt_spec
## FUNC 9[bool comparing known grant-funded cumulative entry and separate retry costs with each matching USD c] => continuation.costs_within
## @usecases
## - Parent: import native0/parent4 -> reserve repair5 under scoped grant -> readback -> real worker -> canonical closure; originals remain unchanged.
## - Recovery: uncertain release -> hold replay -> actual investigation -> same-entry outcome without refund/double charge.
## - Reviewer: mutate spec admission/input/cost observation -> observe owned refusal/retained history before any further release.
## @GREP_SUMMARY schema3, causal allowance, immutable history, recovery
## @STRUCTURE source binding → authority → reservation → canonical outcome
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import copy
import hashlib
import json
import logging
import math
from pathlib import Path
import re
import uuid

logger = logging.getLogger(__name__)
UNITS = {'response-correction', 'extraction', 'transport', 'test-session'}
TERMINALS = {'SUCCESS','SPEC_BLOCKED','VISUAL_GATE_FAIL','BLOCKED','ERROR','ESCALATED','ESCALATED_FINALIZE'}
# region FUNC_require [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Refuse a named invariant, emitting safe diagnostics without input payloads.
## @uses ValueError, logger.error
## @io ok predicate and safe static reason str -> None when true, else ValueError(reason) with safe own ERROR. No storage reads/writes. Example: false refuses without altering counters.
## @complexity 5
def require(ok, reason):
    """Refuse a named invariant, emitting safe diagnostics without input payloads."""
    if not ok:
        logger.error('[IMP:10][require][REFUSE] %s', reason)
        raise ValueError(reason)
# endregion FUNC_require
# region FUNC_digest [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Hash canonical complete JSON; nonfinite values refuse before mutation.
## @uses hashlib.sha256, json.dumps, logger.error, logger.info, type
## @io value JSON-compatible object -> canonical SHA256 hex str. allow_nan=False rejects nonfinite numbers (ValueError), unserializable objects raise TypeError. No filesystem effects; identical complete JSON yields identical digest.
## @complexity 5
def digest(value):
    """Hash canonical complete JSON; nonfinite values refuse before mutation."""
    logger.info('[IMP:4][digest][START] bounded operation')
    try:
        returned = hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
        logger.info('[IMP:9][digest][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][digest][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_digest
# region FUNC_atomic [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Publish complete JSON in owned existing parent. Exclusive enrollment is never replaced.
## @uses Path, json.dumps, logger.error, logger.info, path.open, path.with_name, stream.write, temporary.replace, temporary.unlink, temporary.write_text, type, uuid.uuid4
## @io path owned destination Path/str, value finite JSON object, exclusive bool=False -> None after UTF8 publication. Exclusive uses x/no overwrite; replacement writes a unique sibling then replaces and always unlinks its own temporary. OSError preserves existing destination before replace; encoding errors precede writes. No worker launch/fsync claim.
## @complexity 5
def atomic(path, value, exclusive=False):
    """Publish complete JSON in owned existing parent. Exclusive enrollment is never replaced."""
    logger.info('[IMP:4][atomic][START] bounded operation')
    try:
        path = Path(path)
        encoded = json.dumps(value, indent=2, allow_nan=False)+'\n'
        if exclusive:
            with path.open('x', encoding='utf-8') as stream:
                stream.write(encoded)
            logger.info('[IMP:9][atomic][RESULT] operation complete')
            return
        temporary = path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
        try:
            temporary.write_text(encoded, encoding='utf-8')
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)
        logger.info('[IMP:9][atomic][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][atomic][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_atomic
# region FUNC_authority [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Derive canonical storage from causal identity, never from successor labels.
## @uses Path, logger.error, logger.info, type
## @io state containing absolute target and validated lineage.id SHA256 -> Path target/.methodology/lineages/id/state.json. Pure path construction plus safe own logs; KeyError/TypeError on incomplete input. Successor names never select a wallet.
## @complexity 5
def authority(state):
    """Derive canonical storage from causal identity, never from successor labels."""
    logger.info('[IMP:4][authority][START] bounded operation')
    try:
        returned = Path(state['target'])/'.methodology/lineages'/state['lineage']['id']/'state.json'
        logger.info('[IMP:9][authority][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][authority][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_authority
# region FUNC_shape [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Validate schema3 accounting, grants and retry histories, with exact control surface.
## @uses any, check_grant, digest, ids.add, len, lineage['episodes'].items, logger.error, logger.info, math.isfinite, re.fullmatch, require, set, state.get, sum, type
## @io state schema3 dict -> None if exact lineage surface, causal digest, plain original_cap0..4, inherited_spent0..cap, summed grants/entry spend, reservations, costs and four episode units agree. ValueError/KeyError/TypeError on contradictions. No storage writes or consent authentication.
## @complexity 9
def shape(state):
    """Validate schema3 accounting, grants and retry histories, with exact control surface."""
    logger.info('[IMP:4][shape][START] bounded operation')
    try:
        lineage = state.get('lineage')
        require(type(lineage) is dict and set(lineage)=={'id','root','revision','original_cap','inherited_spent','grants','entries','active_entry','imports','closed','episodes','costs','admissions'}, 'invalid lineage surface')
        require(re.fullmatch('[a-f0-9]{64}', lineage['id']) is not None and lineage['id']==digest(lineage['root']), 'causal identity mismatch')
        require(re.fullmatch('[A-Za-z0-9_-]+',state['run_id']) is not None,'unsafe run identity')
        require(type(lineage['revision']) is int and lineage['revision']>=0, 'invalid revision')
        require(type(lineage['original_cap']) is int and 0<=lineage['original_cap']<=4, 'invalid original allowance')
        require(type(lineage['inherited_spent']) is int and 0<=lineage['inherited_spent']<=lineage['original_cap'], 'invalid inherited spend')
        require(type(lineage['grants']) is list and type(lineage['entries']) is list and type(lineage['imports']) is list and type(lineage['closed']) is list and type(lineage['episodes']) is dict and set(lineage['episodes'])==UNITS, 'invalid causal history')
        ids=set()
        for grant in lineage['grants']:
            check_grant(state, grant, historical=True)
            require(grant['id'] not in ids, 'duplicate grant')
            ids.add(grant['id'])
        spent=lineage['inherited_spent']+sum(entry['charge'] for entry in lineage['entries'])
        require(state['debug_spent']==spent and state['debug_cap']==lineage['original_cap']+sum(g['entries'] for g in lineage['grants']), 'aggregate accounting mismatch')
        require(len({e['id'] for e in lineage['entries']})==len(lineage['entries']), 'duplicate entry')
        for entry in lineage['entries']:
            require(type(entry) is dict and set(entry)=={'fund','id','run_id','phase','candidate','input','charge','state','worker','evidence','usd'},'invalid entry surface')
            require(entry['fund'] in ({None,'original'}|ids),'unknown funding source')
            require(entry['usd'] is None or type(entry['usd']) in {int,float} and (type(entry['usd']) is int or math.isfinite(entry['usd'])) and entry['usd']>=0,'invalid stored cost')
            require(type(entry['charge']) is int and entry['charge'] in {0,1} and entry['state'] in {'reserved','released','complete','unknown'}, 'invalid reservation')
            require(entry['phase'] in {'bootstrap','architect','code','qa','review','debug','finalize'}, 'invalid reserved phase')
        active=lineage['active_entry']
        require(active is None or any(e['id']==active for e in lineage['entries']), 'missing active reservation')
        for unit, episodes in lineage['episodes'].items():
            require(type(episodes) is list, 'invalid retry history')
            for episode in episodes:
                require(type(episode['used']) is int and episode['used']>=0 and episode['limit']==(1 if unit=='response-correction' else 0) and type(episode['closed']) is bool, 'invalid retry scope')
        require(type(lineage['costs']) is list, 'missing cost history')
        require(type(lineage['admissions']) is list and state['spec_path'] in lineage['admissions'] and len(set(lineage['admissions']))==len(lineage['admissions']),'missing specification admissions')
        logger.info('[IMP:9][shape][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][shape][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_shape
# region FUNC_check_grant [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Validate finite GATE-1209 structure; authentic consent remains parent-owned.
## @uses any, bool, grant[key].strip, logger.error, logger.info, math.isfinite, require, set, type
## @io state current lineage plus grant exact id/lineage/target/approval/entries/cost_usd; historical bool=False -> None. entries plain int1..20; USD finite int/float0..1000 (bool invalid). Wrong target/lineage, duplicate or reserved id refuses ValueError. No writes; approval authenticity remains parent-owned.
## @complexity 5
def check_grant(state, grant, historical=False):
    """Validate finite GATE-1209 structure; authentic consent remains parent-owned."""
    logger.info('[IMP:4][check_grant][START] bounded operation')
    try:
        require(type(grant) is dict and set(grant)=={'id','lineage','target','approval','entries','cost_usd'}, 'invalid grant fields')
        for key in ('id','approval'):
            require(type(grant[key]) is str and bool(grant[key].strip()), 'missing grant provenance')
        require(grant['id']!='original','reserved grant identity')
        require(grant['lineage']==state['lineage']['id'] and grant['target']==state['target'], 'grant scope mismatch')
        require(type(grant['entries']) is int and 1<=grant['entries']<=20, 'grant entries outside 1..20')
        require(type(grant['cost_usd']) in {int,float} and 0<=grant['cost_usd']<=1000 and math.isfinite(grant['cost_usd']), 'grant USD outside 0..1000')
        if not historical:
            require(not any(g['id']==grant['id'] for g in state['lineage']['grants']), 'grant already used')
        logger.info('[IMP:9][check_grant][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][check_grant][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_check_grant
# region FUNC_new_lineage [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Attach one causal authority to a newly source-bound state; no storage writes.
## @uses digest, logger.error, logger.info, type
## @io state current-bound run, optional causal root, inherited spent int=0, cap int0..4 or None, imports list or None -> SAME state dict with one fresh lineage, admissions/current spec, unknown cost history and original allowance. In-memory mutation only; caller validates before enrollment. No existing wallet reset is authorized.
## @complexity 5
def new_lineage(state, root=None, spent=0, cap=None, imports=None):
    """Attach one causal authority to a newly source-bound state; no storage writes."""
    logger.info('[IMP:4][new_lineage][START] bounded operation')
    try:
        root=root or {'kind':'specification','target':state['target'],'spec_path':state['spec_path']}
        state['lineage']={'id':digest(root),'root':root,'revision':0,'original_cap':state['debug_cap'] if cap is None else cap,'inherited_spent':spent,'grants':[],'entries':[],'active_entry':None,'imports':imports or [],'closed':[],'episodes':{u:[] for u in UNITS},'costs':[{'origin':'historical' if imports else 'initial','usd':None}],'admissions':[state['spec_path']]}
        state['debug_spent']=spent
        state['debug_cap']=state['lineage']['original_cap']
        returned = state
        logger.info('[IMP:9][new_lineage][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][new_lineage][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_new_lineage
# region FUNC_enroll [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Exclusive durable admission precedes checkpoint; incomplete enrollment conservatively holds.
## @uses (registry / (digest(key) + '.json')).exists, Path, atomic, authority, digest, folder.exists, folder.mkdir, logger.error, logger.info, registry.mkdir, require, storage_path, str, type
## @io api run_state module and validated fresh state -> None after exclusive lineage folder, admission markers and enrollment publication. Existing/incomplete folder or conflicting admission refuses; partial filesystem publication remains held, never a fresh allowance. No imported source writes.
## @complexity 5
def enroll(api, state):
    """Exclusive durable admission precedes checkpoint; incomplete enrollment conservatively holds."""
    logger.info('[IMP:4][enroll][START] bounded operation')
    try:
        folder=storage_path(state,authority(state).parent)
        require(not folder.exists(), 'lineage already enrolled or incomplete; investigate without reset')
        registry=storage_path(state,Path(state['target'])/'.methodology/admissions')
        registry.mkdir(parents=True, exist_ok=True)
        # Current approved spec path also joins imported causal roots to ordinary init.
        keys=[{'spec_path':state['spec_path']}]+[{'source':r['sha256']} for r in state['lineage']['imports']]
        for key in keys:
            require(not (registry/(digest(key)+'.json')).exists(), 'causal input already enrolled')
        folder.mkdir(parents=True, exist_ok=False)
        for key in keys:
            atomic(registry/(digest(key)+'.json'), {'key':key,'authority':str(authority(state))}, exclusive=True)
        atomic(folder/'enrollment.json', {'root':state['lineage']['root'],'authority':str(authority(state))}, exclusive=True)
        logger.info('[IMP:9][enroll][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][enroll][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_enroll
# region FUNC_active [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Find the current immutable-identity reservation or refuse missing control.
## @uses len, logger.error, logger.info, require, type
## @io state lineage active_entry and entries -> exact mutable reservation dict within state. Missing/ambiguous active ID refuses ValueError. No I/O; caller copies state before mutation. Example: completed prior ID cannot select a future entry.
## @complexity 5
def active(state):
    """Find the current immutable-identity reservation or refuse missing control."""
    logger.info('[IMP:4][active][START] bounded operation')
    try:
        found=[e for e in state['lineage']['entries'] if e['id']==state['lineage']['active_entry']]
        require(len(found)==1, 'entry not reserved')
        returned = found[0]
        logger.info('[IMP:9][active][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][active][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_active
# region FUNC_prepare [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Allocate the next entry in memory; caller checkpoints and reads it before release.
## @uses bool, costs_within, int, logger.error, logger.info, previous.append, require, state['lineage']['entries'].append, type, uuid.uuid4
## @io state RUNNING with no outstanding entry, charge bool=False -> newly attached reservation dict (id/run/phase/candidate/input/fund/charge/state/worker/evidence/usd). Optionally consumes ONE available repair; exhausted allowance or observed grant overrun refuses before allocation. Opens linked per-attempt retry scopes in memory only; save/readback must precede dispatch.
## @complexity 5
def prepare(state, charge=False):
    """Allocate the next entry in memory; caller checkpoints and reads it before release."""
    logger.info('[IMP:4][prepare][START] bounded operation')
    try:
        require(state['status']=='RUNNING', 'terminal cannot reserve')
        require(costs_within(state),'observed grant cost ceiling exceeded; further release held')
        require(state['lineage']['active_entry'] is None, 'outstanding reservation')
        logger.info('[IMP:7][prepare][ALLOWANCE] charge=%s',bool(charge))
        if charge:
            require(state['debug_spent']<state['debug_cap'], 'repair allowance exhausted')
            state['debug_spent']+=1
        fund=None
        if charge:
            offset=state['debug_spent']-state['lineage']['original_cap']
            fund='original'
            if offset>0:
                for grant in state['lineage']['grants']:
                    if offset<=grant['entries']:
                        fund=grant['id'];break
                    offset-=grant['entries']
        reservation={'fund':fund,'id':uuid.uuid4().hex,'run_id':state['run_id'],'phase':state['phase'],'candidate':state['candidate']['digest'],'input':state['input_identity'],'charge':int(charge),'state':'reserved','worker':None,'evidence':[],'usd':None}
        state['lineage']['entries'].append(reservation)
        state['lineage']['active_entry']=reservation['id']
        for unit in UNITS:
            previous=state['lineage']['episodes'][unit]
            # A different phase attempt has a new owning scope; same-attempt recovery never calls prepare.
            previous.append({'id':reservation['id']+':'+unit,'entry':reservation['id'],'previous':previous[-1]['id'] if previous else None,'limit':1 if unit=='response-correction' else 0,'used':0,'closed':False,'costs':[]})
        state['retry_episodes']={u:0 for u in UNITS}
        returned = reservation
        logger.info('[IMP:9][prepare][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][prepare][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_prepare
# region FUNC_complete [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Retain completion identity/evidence and close retry scopes; never refund a charge.
## @uses active, bool, copy.deepcopy, logger.error, logger.info, require, state['lineage']['episodes'].values, type, worker.strip
## @io state with reserved/released active entry, evidence list and optional observed worker str -> None; changes that entry to complete, retains charge, closes retry scopes and clears active ID in memory. Unknown/completed entry or conflicting worker refuses. Does not validate role success or write storage; advance does canonical validation first.
## @complexity 5
def complete(state, evidence, worker=None):
    """Retain completion identity/evidence and close retry scopes; never refund a charge."""
    logger.info('[IMP:4][complete][START] bounded operation')
    try:
        entry=active(state)
        require(entry['state'] in {'reserved','released'}, 'unknown or completed entry cannot accept output')
        if worker is not None:
            require(type(worker) is str and bool(worker.strip()) and entry['worker'] in {None,worker}, 'worker identity mismatch')
            entry['worker']=worker
        entry['state']='complete'
        entry['evidence']=copy.deepcopy(evidence)
        for rows in state['lineage']['episodes'].values():
            rows[-1]['closed']=True
        state['lineage']['active_entry']=None
        logger.info('[IMP:9][complete][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][complete][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_complete
# region FUNC_committed [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Validate persisted current revision and enrollment before any dispatch/control mutation.
## @uses api._file, api.read_json, api.validate_state, authority, bool, check_admissions, logger.error, logger.info, path.is_file, require, revisions.glob, sorted, str, str(state['lineage']['revision']).zfill, type
## @io api and complete state, allow_source_change bool=False -> canonical authority Path after current bindings/candidate, exact persisted revision, newest immutable journal, all admissions/enrollment and frozen source/terminal identities match. Drift/missing/corrupt/rollback/incomplete publication raises; reads only. True source-change permission still requires later exact authored-delta validation.
## @complexity 5
def committed(api, state, allow_source_change=False):
    """Validate persisted current revision and enrollment before any dispatch/control mutation."""
    logger.info('[IMP:4][committed][START] bounded operation')
    try:
        logger.info('[IMP:7][committed][READ] current inputs and complete authority')
        api.validate_state(state, allow_source_change=allow_source_change)
        path=authority(state)
        check_admissions(api,state)
        require(path.is_file() and api.read_json(path)==state, 'stale/rollback/uncommitted authority')
        revisions=path.parent/'revisions'
        published=sorted(revisions.glob('*.json'))
        require(bool(published) and published[-1].stem==str(state['lineage']['revision']).zfill(12) and api.read_json(published[-1])==state,'rollback/incomplete checkpoint publication')
        enrollment=api.read_json(path.parent/'enrollment.json')
        require(enrollment=={'root':state['lineage']['root'],'authority':str(path)}, 'enrollment mismatch')
        for row in state['lineage']['imports']:
            require(api._file(row['path'])==row, 'historical input changed')
        for row in state['lineage']['closed']:
            require(api._file(row['path'])==row, 'closed terminal changed')
        returned = path
        logger.info('[IMP:9][committed][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][committed][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_committed
# region FUNC_persist [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose CAS-like single-writer revision and immutable terminal publication before atomic checkpoint.
## @uses Path, Path(path).resolve, any, api._file, api.read_json, atomic, authority, e.get, journal.mkdir, len, logger.error, logger.info, path.exists, path.parent.is_dir, require, shape, state['lineage']['closed'].append, str, str(state['lineage']['revision']).zfill, terminal.exists, terminal.parent.mkdir, type
## @io api, exact canonical path, structurally valid state -> None after single-writer revision check, immutable terminal publication when closed, exclusive revision journal and atomic checkpoint. Mutates in-memory revision/closed refs only for its publication; stale revision or wrong destination refuses. OSError can leave incomplete publication, which holds release; no power-loss/exactly-once guarantee.
## @complexity 9
def persist(api, path, state):
    """CAS-like single-writer revision and immutable terminal publication before atomic checkpoint."""
    logger.info('[IMP:4][persist][START] bounded operation')
    try:
        shape(state)
        path=Path(path).resolve()
        require(path==authority(state) and path.parent.is_dir(), 'non-authoritative checkpoint path')
        if path.exists():
            old=api.read_json(path)
            require(old['lineage']['id']==state['lineage']['id'] and old['lineage']['revision']==state['lineage']['revision'], 'stale revision')
            if old==state:
                logger.info('[IMP:9][persist][RESULT] operation complete')
                return
            require(old['status']=='RUNNING' or any(e.get('kind')=='continued' for e in state['history'][len(old['history']):]), 'closed authority only continues explicitly')
        if state['status'] in TERMINALS:
            terminal=path.parent/'closed'/(state['run_id']+'.json')
            terminal.parent.mkdir(exist_ok=True)
            if terminal.exists():
                require(api.read_json(terminal)==state, 'terminal artifact immutable')
            else:
                atomic(terminal,state,exclusive=True)
            state['lineage']['closed'].append(api._file(terminal))
        state['lineage']['revision']+=1
        journal=path.parent/'revisions'
        journal.mkdir(exist_ok=True)
        atomic(journal/(str(state['lineage']['revision']).zfill(12)+'.json'),state,exclusive=True)
        atomic(path,state)
        logger.info('[IMP:9][persist][CHECKPOINT] revision=%d',state['lineage']['revision'])
        logger.info('[IMP:9][persist][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][persist][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_persist
# region FUNC_capabilities [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Read-only declared local support; no file/run/Git creation or runtime efficacy claim.
## @uses logger.error, logger.info, type
## @io no inputs -> dict naming actual native5/neutral4.1/schema3/wire2, supported operations/profiles, default4, grant ranges and declared limits. Safe logs only; no state, filesystem, Git or worker action. Declaration does not qualify runtime behavior.
## @complexity 5
def capabilities():
    """Read-only declared local support; no file/run/Git creation or runtime efficacy claim."""
    logger.info('[IMP:4][capabilities][START] bounded operation')
    try:
        returned = {'package':'methodology-codex','version':'5.0.0','neutral':'4.1.0','schema':3,'role_wire':'methodology-codex/2.0.0','operations':['init','show','record','capabilities','continue','reserve','released','recover','episode'], 'historical_profiles':['codex3.2-schema2-parent-bridge','codex4.0-schema2-native-complete','codex5.0-schema3-closed'],'default_cap':4,'grant_entries':[1,20],'grant_usd':[0,1000],'retry_limits':{'response-correction':1,'extraction':0,'transport':0,'test-session':0},'limits':['one parent writer/storage domain','parent authenticates consent and causal identity','unknown release holds replay','no active schema2 migration','no exactly-once or power-loss guarantee','no scheduler; parent reserves, reads back, then dispatches']}
        logger.info('[IMP:9][capabilities][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][capabilities][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_capabilities
# region FUNC_historical [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Admit exact supported historical structure without current-binding validation or writes.
## @uses Path, Path(native_path).resolve, Path(parent['native_state']).resolve, Path(parent_path).resolve, any, api._digest, api._file, api.read_json, binding.pop, bool, copy.deepcopy, e.get, event.get, imports.append, logger.error, logger.info, old.get, require, set, shape, str, str(event).lower, sum, type
## @io api, native_path and optional parent_path -> (historical dict, aggregate spent int, original cap int, immutable file identity list). Accepts exact terminal schema2 Codex3.2 identified parent bridge, complete native4.0 or own3 closed. Source/input digests, terminal pairing, plain counters, chronology and overlap are checked; unsupported/ambiguous data refuses without writes. Native0 plus parent4 imports4, not0 or8.
## @complexity 9
def historical(api, native_path, parent_path=None):
    """Admit exact supported historical structure without current-binding validation or writes."""
    logger.info('[IMP:4][historical][START] bounded operation')
    try:
        native_path=Path(native_path).resolve()
        old=api.read_json(native_path)
        require(type(old.get('schema_version')) is int and old['schema_version'] in {2,3}, 'unsupported historical schema')
        require(old.get('status') in TERMINALS and old.get('phase') in api.PHASE_ROLES, 'historical run is not closed')
        valid_terminal_phases={'SUCCESS':{'finalize'},'SPEC_BLOCKED':{'bootstrap','architect'},'VISUAL_GATE_FAIL':{'architect'},'ESCALATED':{'code','qa','review'},'ESCALATED_FINALIZE':{'finalize'},'BLOCKED':set(api.PHASE_ROLES),'ERROR':set(api.PHASE_ROLES)}
        require(old['phase'] in valid_terminal_phases[old['status']],'unsupported terminal phase pairing')
        require(old.get('contract_version')=='methodology-codex/2.0.0', 'unsupported historical role wire')
        require(api.STATE_FIELDS<=set(old), 'incomplete historical state')
        if old['schema_version']==2:
            require(set(old)<=api.STATE_FIELDS|{'debug_origin'},'unknown historical control fields')
        binding=copy.deepcopy(old['bindings']);saved_digest=binding.pop('digest')
        require(api._digest(binding)==saved_digest,'historical source digest mismatch')
        require(old['bindings']['spec']['sha256']==old['approval']['spec'] and old['approval']['scope']==old['target'] and old['approval']['action']=='execute approved specification', 'historical scope binding mismatch')
        require(old['input_identity']==api._digest({'bindings':old['bindings']['digest'],'plan':old['plan']}), 'historical input digest mismatch')
        require(type(old['history']) is list and bool(old['history']) and set(old['retry_episodes'])==set(old['retry_limits'])==UNITS, 'incomplete historical chronology')
        for event in old['history']:
            require(type(event) is dict and type(event.get('debug_delta',0)) is int and event.get('debug_delta',0)>=0,'invalid historical event accounting')
        for key in ('debug_cap','debug_spent'):
            require(type(old[key]) is int and old[key]>=0, 'historical allowance type')
        require(old['debug_spent']<=old['debug_cap'], 'historical spend exceeds allowance')
        imports=[api._file(native_path)]
        if old['schema_version']==3:
            require(parent_path is None, 'schema3 has no external wallet')
            shape(old)
            returned = old,old['debug_spent'],old['debug_cap'],imports
            logger.info('[IMP:9][historical][RESULT] operation complete')
            return returned
        version=old['bindings']['neutral_version']
        require(version in {'3.2.0','4.0.0'}, 'unsupported historical profile')
        if version=='3.2.0':
            require(parent_path is not None, '3.2 bridge requires identified parent accounting')
            parent_path=Path(parent_path).resolve()
            parent=api.read_json(parent_path)
            require(Path(parent['native_state']).resolve()==native_path and parent['native_input_identity']==old['input_identity'], 'parent/native identity mismatch')
            require(parent['native_status']==old['status'] and parent['native_phase']==old['phase'], 'parent/native phase mismatch')
            totals=parent['cumulative_totals']; repair=parent['repair4']
            spent,cap=totals['debug'],totals['debug_ceiling']
            require(type(spent) is int and type(cap) is int and 0<=spent<=cap<=4, 'parent aggregate invalid')
            require(type(parent['additional_debug_allowance']) is int and parent['additional_debug_allowance']==0 and parent['precharge_pending'] is False and repair['spent']==spent and repair['ceiling']==cap and type(repair['inherited']) is int and repair['inherited']+1==spent, 'ambiguous historical overlap')
            require(old['debug_cap']==old['debug_spent']==0 and parent['plan_sha256']==old['plan']['identity']['sha256'], 'unsupported local-allowance bridge')
            require(parent['precharged_at']==repair['at'] and parent['recorded_at']<=parent['precharged_at']<=parent['updated_at'], 'parent chronology mismatch')
            imports.append(api._file(parent_path))
        else:
            require(parent_path is None and old['debug_cap']<=4, '4.0 requires native-only complete causal accounting')
            require(not any('external' in str(event).lower() or 'inherited' in str(event).lower() for event in old['history']), 'external accounting needs admitted bridge')
            spent,cap=old['debug_spent'],old['debug_cap']
            require(sum(e.get('debug_delta',0) for e in old['history'])==spent, 'native accounting incomplete')
        root={'kind':'legacy','target':old['target'],'run':old['run_id'],'input':old['input_identity']}
        require(old['target']==str(native_path.parents[3]), 'historical location mismatch')
        old['_causal_root']=root
        returned = old,spent,cap,imports
        logger.info('[IMP:9][historical][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][historical][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_historical
# region FUNC_predicates [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Check actual reentry predicates; historical accepted fields are never copied as current success.
## @uses api._evidence, bool, current, logger.error, logger.info, require, row.get, set, state.get, state['accepted'].get, type
## @io api, current successor state, phase and nonempty actual contained evidence paths -> None after required plan/scope and current Code/QA/Review input/scope/artifact identities; Debug also needs causal report. Missing/stale prerequisites raise; no old success or budget is fabricated. Filesystem reads only.
## @complexity 5
def predicates(api, state, phase, evidence):
    """Check actual reentry predicates; historical accepted fields are never copied as current success."""
    logger.info('[IMP:4][predicates][START] bounded operation')
    try:
        require(type(evidence) is list and bool(evidence), 'entry evidence missing')
        api._evidence(state,evidence)
        if phase not in {'bootstrap','architect'}:
            require(state['plan']['status']=='bound' and bool(state['approved_scope']), 'current approved plan/scope required')
        def current(name):
            row=state['accepted'].get(name,{})
            require(row.get('candidate')==state['candidate']['digest'], 'current '+name+' prerequisite missing')
            require(row.get('input')==state['input_identity'] and set(row.get('scope',[]))==set(state['approved_scope']),'stale '+name+' input/scope')
            require(api._evidence(state,row.get('evidence'))==row.get('identities'),'changed '+name+' evidence')
        if phase=='qa':
            current('code')
        if phase in {'review','finalize'}:
            current('code');current('qa')
        if phase=='finalize':
            current('review')
        if phase=='debug':
            require(type(state.get('debug_origin')) is dict, 'Debug needs actual causal report')
        logger.info('[IMP:9][predicates][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][predicates][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_predicates
# region FUNC_continue_run [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Enroll historical input or select explicit successor of a committed closed authority.
## @uses (authority(old_authority).parent / 'revisions').glob, Path, Path(old_path).resolve, Path(request['adapter']).resolve, Path(request['framework']).resolve, Path(request['plan']).resolve, Path(request['project']).resolve, Path(request['spec']).resolve, adopt_spec, any, api._bindings, api._digest, api._evidence, api._file, api._relative, api._stamp, api._text, api.inventory, api.read_json, api.save, authority, bool, check_admissions, check_grant, code.update, copy.deepcopy, enroll, historical, logger.error, logger.info, new_lineage, plan.exists, plan.is_relative_to, predicates, prepare, project.is_dir, re.fullmatch, request.get, require, set, shape, sorted, state.pop, state.update, state['history'].append, state['lineage']['admissions'].append, state['lineage']['episodes'][unit].append, state['lineage']['grants'].append, str, type
## @io api, immutable old_path, exact parent request plus optional admitted legacy parent_path -> (canonical Path, newly persisted successor state dict). Authenticated reason/approval/scope are parent-owned; helper validates structure, actual reentry predicates, full input freshness and optional unchanged-Code applicability proof. Reconciles inherited allowance, grants1..20/USD0..1000, precharges Code/Debug, enrolls every adopted spec, journals/saves; originals never change. Unsupported/unknown/conflicting/exhausted inputs refuse before release; partial publication holds.
## @complexity 9
def continue_run(api, old_path, request, *, parent_path=None):
    """Enroll historical input or select explicit successor of a committed closed authority."""
    logger.info('[IMP:4][continue_run][START] bounded operation')
    try:
        require(type(request) is dict and set(request)<={'project','spec','framework','adapter','plan','approval','run_id','phase','reason','evidence','scope','grant','reuse_code'}, 'unknown continuation controls')
        for key in ('approval','reason','run_id'):
            api._text(request.get(key),'continuation '+key+' required')
        require(re.fullmatch('[A-Za-z0-9_-]+',request['run_id']) is not None, 'unsafe successor id')
        old,spent,cap,imports=historical(api,old_path,parent_path)
        phase=request['phase']
        require(phase in api.PHASE_ROLES, 'unsupported reentry phase')
        status=old['status']
        allowed={'SPEC_BLOCKED':{'bootstrap','architect'},'VISUAL_GATE_FAIL':{'architect'},'BLOCKED':set(api.PHASE_ROLES),'ERROR':set(api.PHASE_ROLES),'ESCALATED':{'code','debug','qa','review','finalize'},'ESCALATED_FINALIZE':{'code','debug','qa','review','finalize'},'SUCCESS':set(api.PHASE_ROLES)}
        require(phase in allowed[status] and request['run_id']!=old['run_id'], 'invalid terminal/reentry pair')
        own=old['schema_version']==3
        logger.info('[IMP:7][continue_run][PROFILE] own_schema3=%s',own)
        if own:
            old_authority=api.read_json(authority(old))
            require(old_authority['status'] in TERMINALS and old_authority['run_id']==old['run_id'] and old_authority['lineage']['closed'] and any(r['path']==str(Path(old_path).resolve()) for r in old_authority['lineage']['closed']), 'historical export is not authoritative terminal')
            # Current candidate/input may be amended; predecessor bytes remain separately checked below.
            require(api.read_json(authority(old_authority))==old_authority,'authority changed')
            for row in old_authority['lineage']['imports']+old_authority['lineage']['closed']:
                require(api._file(row['path'])==row,'predecessor history changed')
            journal=sorted((authority(old_authority).parent/'revisions').glob('*.json'))
            require(bool(journal) and api.read_json(journal[-1])==old_authority,'rollback/incomplete predecessor authority')
            check_admissions(api,old_authority)
            lineage=copy.deepcopy(old_authority['lineage'])
        project=Path(request['project']).resolve();spec=Path(request['spec']).resolve();plan=Path(request['plan']).resolve()
        require(project.is_dir() and plan.is_relative_to(project), 'invalid amended target/plan')
        if own:
            require(str(project)==old['target'], 'cannot move enrolled storage domain')
        bindings=api._bindings(request['framework'],request['adapter'],spec)
        state=copy.deepcopy(old)
        state.pop('_causal_root',None)
        state.update(schema_version=3,run_id=request['run_id'],status='RUNNING',phase=phase,target=str(project),framework=str(Path(request['framework']).resolve()),adapter_path=str(Path(request['adapter']).resolve()),spec_path=str(spec),bindings=bindings,approval={'reference':request['approval'],'action':'execute approved specification','spec':bindings['spec']['sha256'],'scope':str(project)},plan={'path':str(plan),'status':'bound' if plan.exists() else 'pending'})
        if plan.exists(): state['plan']['identity']=api._file(plan)
        state['input_identity']=api._digest({'bindings':bindings['digest'],'plan':state['plan']})
        state['candidate']=api.inventory(project)
        unchanged_artifacts=(state['candidate']==old['candidate'] and state['plan']==old['plan'] and bindings['spec']['sha256']==old['bindings']['spec']['sha256'])
        unchanged_scope=set(request['scope'])==set(old['approved_scope'])
        unchanged_inputs=own and state['input_identity']==old['input_identity'] and unchanged_scope
        logger.info('[IMP:7][continue_run][FRESHNESS] artifacts=%s inputs_scope=%s',unchanged_artifacts,unchanged_inputs)
        if not unchanged_artifacts or not unchanged_inputs:
            state['accepted']={}
        # Optional parent applicability proof may revalidate actual unchanged Code artifacts,
        # never stale QA/Review, for no-repair verification under changed bound rules.
        if request.get('reuse_code') is not None:
            reuse=request['reuse_code']
            require(unchanged_artifacts and unchanged_scope and 'code' in old['accepted'],'Code reuse requires unchanged artifacts/spec/plan/scope')
            require(type(reuse) is dict and set(reuse)=={'reason','evidence'},'invalid Code applicability proof')
            api._text(reuse['reason'],'Code applicability reason required')
            proof=api._evidence(state,reuse['evidence'])
            code=copy.deepcopy(old['accepted']['code'])
            identities=api._evidence(state,code['evidence'])
            if 'identities' in code:
                require(code['identities']==identities,'previous Code evidence changed')
            code.update(input=state['input_identity'],scope=copy.deepcopy(request['scope']),identities=identities,revalidated={'approval':request['approval'],'reason':reuse['reason'],'evidence':proof})
            state['accepted']['code']=code
        if own:
            state['lineage']=lineage
            require(not any(e['run_id']==state['run_id'] for e in lineage['entries']), 'successor already used')
        else:
            new_lineage(state,old['_causal_root'],spent,cap,imports)
            for unit in UNITS:
                used=old['retry_episodes'][unit]
                require(type(used) is int and used>=0, 'historical retry type')
                state['lineage']['episodes'][unit].append({'id':'historical:'+unit,'entry':old['run_id'],'previous':None,'limit':old['retry_limits'][unit],'used':used,'closed':True,'costs':[None]})
        require(type(request['scope']) is list and bool(request['scope']) if phase not in {'bootstrap','architect'} else type(request['scope']) is list, 'amended scope missing')
        state['approved_scope']=[api._relative(p) for p in request['scope']]
        predicates(api,state,phase,request['evidence'])
        logger.info('[IMP:9][continue_run][PREDICATES] eligible phase=%s',phase)
        if request.get('grant') is not None:
            check_grant(state,request['grant'])
            state['lineage']['grants'].append(copy.deepcopy(request['grant']))
            state['debug_cap']+=request['grant']['entries']
        state['history'].append({'kind':'continued','time':api._stamp(),'predecessor':api._file(old_path),'reason':request['reason'],'approval':request['approval'],'phase':phase,'debug_delta':0})
        require(state['lineage']['active_entry'] is None, 'unresolved predecessor reservation')
        if own and state['spec_path'] not in state['lineage']['admissions']:
            state['lineage']['admissions'].append(state['spec_path'])
        prepare(state,charge=phase in {'code','debug'})
        shape(state)
        if not own:
            enroll(api,state)
        else:
            adopt_spec(api,state)
        api.save(authority(state),state)
        returned = authority(state),state
        logger.info('[IMP:9][continue_run][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][continue_run][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_continue_run
# region FUNC_reservation_operation [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Reconcile one persisted entry. Unknown release/completion always holds replay.
## @uses active, api._evidence, api._stamp, api._text, api.save, authority, bool, committed, copy.deepcopy, costs_within, entry.update, logger.error, logger.info, math.isfinite, request.get, require, set, type, updated['history'].append, updated['lineage']['costs'].append
## @io api, committed state, operation reserve/released/recover, exact request -> updated persisted state dict. reserve accepts only active entry ID and withholds overrun/unknown/replayed release. released records observed worker; recover needs actual evidence and unknown/unlaunched/completed outcome. Valid finite nonnegative cumulative USD is retained even over ceiling; known costs cannot become null/lower. Identical repeat does not double charge/cost. Invalid observations refuse; no worker is launched.
## @complexity 9
def reservation_operation(api, state, operation, request):
    """Reconcile one persisted entry. Unknown release/completion always holds replay."""
    logger.info('[IMP:4][reservation_operation][START] bounded operation')
    try:
        require(operation in {'reserve','released','recover'},'unsupported reservation operation')
        logger.info('[IMP:7][reservation_operation][CONTROL] operation=%s',operation)
        committed(api,state,allow_source_change=operation in {'released','recover'})
        require(type(request) is dict and set(request)<={'entry','worker','outcome','evidence','usd'}, 'unknown parent reservation fields')
        if operation=='reserve':
            require(set(request)=={'entry'},'reserve accepts only an entry identity; observations use recover/released')
        updated=copy.deepcopy(state);entry=active(updated)
        require(request.get('entry')==entry['id'], 'reservation identity mismatch')
        if 'usd' in request:
            usd=request['usd']
            require(usd is None or type(usd) in {int,float} and (type(usd) is int or math.isfinite(usd)) and usd>=0,'invalid observed cost')
            entry['usd']=usd
            previous=active(state)['usd']
            require(previous is None or usd is not None and usd>=previous,'known cost cannot be erased or refunded')
            observation={'origin':entry['id'],'usd':usd}
            if not updated['lineage']['costs'] or updated['lineage']['costs'][-1]!=observation:
                updated['lineage']['costs'].append(observation)
        if operation=='reserve':
            require(costs_within(updated),'observed grant cost ceiling exceeded; further release held')
            require(entry['state']=='reserved', 'entry already released/unknown/completed')
        elif operation=='released':
            require(costs_within(state),'observed grant cost ceiling exceeded; further release held')
            require(entry['state']=='reserved', 'entry not releasable')
            api._text(request.get('worker'),'actual worker/session locator required')
            entry.update(state='released',worker=request['worker'])
        else:
            require(operation=='recover','unknown reservation operation')
            api._evidence(updated,request.get('evidence'))
            outcome=request.get('outcome')
            require(outcome in {'unknown','unlaunched','completed'}, 'investigation outcome required')
            if outcome=='unknown': entry['state']='unknown'
            elif outcome=='unlaunched':
                require(entry['state'] in {'reserved','unknown'} and entry['worker'] is None, 'known release cannot be called unlaunched')
                entry['state']='reserved'
            else:
                # Completion must still pass canonical role validation through record; never fake SUCCESS.
                require(type(request.get('worker')) is str and bool(request['worker']), 'observed completed worker required')
                require(entry['worker'] in {None,request['worker']}, 'worker mismatch')
                entry.update(state='released',worker=request['worker'])
            entry['evidence']=copy.deepcopy(request['evidence'])
            updated['history'].append({'kind':'investigated','time':api._stamp(),'entry':entry['id'],'outcome':outcome,'evidence':request['evidence'],'debug_delta':0})
        logger.info('[IMP:7][reservation_operation][OBSERVED] cost_within=%s',costs_within(updated))
        api.save(authority(updated),updated)
        returned = updated
        logger.info('[IMP:9][reservation_operation][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][reservation_operation][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_reservation_operation
# region FUNC_episode [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Record costs for an existing owning retry scope; no automatic new retry allowance.
## @uses active, api._evidence, api.save, authority, committed, copy.deepcopy, logger.error, logger.info, math.isfinite, require, row['costs'].append, set, type, updated['lineage']['costs'].append
## @io api, committed state and exact unit/entry/used/cost_usd/evidence request -> persisted state dict. Four existing units, correct open entry and monotone used<=limit (response1, others0) required; cost null stays unknown, finite nonnegative USD is retained separately. No new episode/retry allowance or worker launch; malformed/exhausted scopes raise.
## @complexity 5
def episode(api,state,request):
    """Record costs for an existing owning retry scope; no automatic new retry allowance."""
    logger.info('[IMP:4][episode][START] bounded operation')
    try:
        committed(api,state)
        require(type(request) is dict and set(request)=={'unit','entry','used','cost_usd','evidence'}, 'invalid retry observation')
        unit=request['unit'];require(unit in UNITS,'unknown retry unit')
        updated=copy.deepcopy(state);entry=active(updated)
        require(request['entry']==entry['id'],'wrong retry attempt')
        api._evidence(updated,request['evidence'])
        row=updated['lineage']['episodes'][unit][-1]
        require(not row['closed'] and type(request['used']) is int and row['used']<=request['used']<=row['limit'], 'exhausted/closed retry scope')
        cost=request['cost_usd']
        require(cost is None or type(cost) in {int,float} and (type(cost) is int or math.isfinite(cost)) and cost>=0,'invalid observed retry cost')
        row['used']=request['used'];row['costs'].append(cost)
        updated['retry_episodes'][unit]=row['used']
        updated['lineage']['costs'].append({'origin':row['id'],'usd':cost})
        api.save(authority(updated),updated)
        returned = updated
        logger.info('[IMP:9][episode][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][episode][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_episode
# region FUNC_check_admissions [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Require every adopted specification to point to this exact canonical authority.
## @uses Path, api._file, api.read_json, authority, digest, logger.error, logger.info, require, storage_path, str, type
## @io api and state -> None after every adopted spec has a regular exact admission marker pointing to the same canonical authority. Reads only. Missing, symlinked, conflicting or unreadable admissions raise; no replacement marker or wallet is fabricated.
## @complexity 5
def check_admissions(api,state):
    """Require every adopted specification to point to this exact canonical authority."""
    logger.info('[IMP:4][check_admissions][START] bounded operation')
    try:
        registry=storage_path(state,Path(state['target'])/'.methodology/admissions')
        for spec in state['lineage']['admissions']:
            key={'spec_path':spec};path=registry/(digest(key)+'.json')
            api._file(path)
            require(api.read_json(path)=={'key':key,'authority':str(authority(state))},'missing/conflicting specification admission')
        logger.info('[IMP:9][check_admissions][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][check_admissions][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_check_admissions
# region FUNC_adopt_spec [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Enroll an explicitly same-cause amended spec before checkpoint; conflict never overwrites.
## @uses Path, api._file, api.read_json, atomic, authority, digest, logger.error, logger.info, path.exists, require, state['lineage']['admissions'].append, storage_path, str, type
## @io api and validated amended state -> None after exclusive current-spec marker creation, or verification of its identical existing owner. Adds the spec to in-memory admissions if absent; marker conflict refuses, never overwrites. Publication before checkpoint can leave a conservative init hold but cannot grant another allowance.
## @complexity 5
def adopt_spec(api,state):
    """Enroll an explicitly same-cause amended spec before checkpoint; conflict never overwrites."""
    logger.info('[IMP:4][adopt_spec][START] bounded operation')
    try:
        registry=storage_path(state,Path(state['target'])/'.methodology/admissions')
        key={'spec_path':state['spec_path']};path=registry/(digest(key)+'.json')
        value={'key':key,'authority':str(authority(state))}
        if path.exists():
            api._file(path);require(api.read_json(path)==value,'specification belongs to another authority')
        else:
            atomic(path,value,exclusive=True)
        if state['spec_path'] not in state['lineage']['admissions']:
            state['lineage']['admissions'].append(state['spec_path'])
        logger.info('[IMP:9][adopt_spec][RESULT] operation complete')
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][adopt_spec][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_adopt_spec
# region FUNC_costs_within [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Check known grant-funded USD without interpreting unavailable costs as zero telemetry.
## @uses e.get, logger.error, logger.info, state['lineage']['episodes'].values, sum, type
## @io state validated lineage -> bool comparing known grant-funded cumulative entry and separate retry costs with each matching USD ceiling. Unknown costs remain stored null and are NOT asserted free or within actual total. No writes/authority grant; False holds future release while actual observations/completion remain recordable.
## @complexity 5
def costs_within(state):
    """Check known grant-funded USD without interpreting unavailable costs as zero telemetry."""
    logger.info('[IMP:4][costs_within][START] bounded operation')
    try:
        for grant in state['lineage']['grants']:
            entries={e['id'] for e in state['lineage']['entries'] if e.get('fund')==grant['id']}
            # Entry cost is cumulative latest observation. Retry costs are separately scoped observations.
            observations=[e['usd'] for e in state['lineage']['entries'] if e['id'] in entries and e['usd'] is not None]
            observations += [c for rows in state['lineage']['episodes'].values() for row in rows if row['entry'] in entries for c in row['costs'] if c is not None]
            if any(value>grant['cost_usd'] for value in observations):
                returned=False
                logger.info('[IMP:9][costs_within][RESULT] operation complete')
                return returned
            known=sum(observations)
            if known>grant['cost_usd']:
                returned = False
                logger.info('[IMP:9][costs_within][RESULT] operation complete')
                return returned
        returned = True
        logger.info('[IMP:9][costs_within][RESULT] operation complete')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][costs_within][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_costs_within

# region FUNC_storage_path [DOMAIN(9): Continuation; CONCEPT(9): OwnedStorage; TECH(7): pathlib]
## @purpose Refuse noncanonical or escaping metadata paths before any enrollment/admission write.
## @uses Path, logger.error, logger.info, path.is_absolute, path.is_relative_to, path.resolve, require, root.is_absolute, root.resolve, type
## @io state with canonical absolute target, path owned metadata Path -> unchanged Path when canonical, within target/.methodology and free of resolved parent/file redirection. ValueError on escape/symlink/noncanonical path, OSError on unavailable resolution. Reads path metadata only; no creation or hard race/isolation guarantee.
## @complexity 5
def storage_path(state,path):
    logger.info('[IMP:4][storage_path][START] owned metadata boundary')
    try:
        path=Path(path);root=Path(state['target'])
        require(root.is_absolute() and root.resolve()==root and path.is_absolute() and path.resolve()==path and path.is_relative_to(root/'.methodology'),'metadata path escapes canonical owned storage')
        returned = path
        logger.info('[IMP:9][storage_path][RESULT] contained canonical metadata')
        return returned
    except (OSError,ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][storage_path][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_storage_path
