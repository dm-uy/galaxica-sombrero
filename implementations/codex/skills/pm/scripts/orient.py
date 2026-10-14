# region MODULE_CONTRACT [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteEvidence, Scope; TECH(7): Python, stdlib]
## @modulecontract
## @purpose Assess every selected native consumer checklist row without mutating project or Git.
## @scope Explicit single/layered/portfolio roots; structural checks never human consent.
## @input Explicit root/check/clock and adopted consumer records.
## @output All22 ordered Check results plus actual stdout0/1/2 and safe diagnostics.
## @links [USES_API(9): consumer_files.resolve_layout, consumer_files.repository_changes, consumer_files.covered_sources; READS_DATA_FROM(6): ORIENT_LOG]
## @invariants
## - CHECK09 rejects a generic DevelopmentPlan.md at every distinct actual layout root; checkpoint-specific declared specs plans remain legal.
## - Unavailable required evidence is never converted to an empty clean success.
## - Explicit resources and controlling human scope remain separate from structural recognition.
## - Consumer content is never imported or executed; inherited framework inputs remain read-only.
## @rationale
## Q: Why explicit shared input boundaries?
## A: Complete populations prevent the original source omission and false-clean classes; they also expose unsupported grammar.
## Q: Why keep endpoint receipts separate from captured events?
## A: A log API call cannot prove actual file, process or map delivery.
## @changes
## LAST_CHANGE: [2.2.0 - A2 Debug2 CHECK09 checks both distinct actual root/flow layer roots; prior C2 causal repairs and authority boundaries retained.]
## @modulemap
## CLASS 9[Carry one structural checklist judgment and its explicit authority limit.] => orient.Check
## FUNC 9[Observe only actual repository-root Git or an explicit filesystem baseline.] => orient.git_info
## FUNC 9[Inspect real root-bound commit paths and archived batch chronology for layered writes and leftover merged branches.] => orient.git_history
## FUNC 9[Assess each actual root Doxyfile configuration separately through the shared complete population reader.] => orient.map_lifecycles
## FUNC 9[Read the complete selected operative record/config/Git populations once.] => orient.collect
## FUNC 9[Count actual date-led State items while excluding code fences and table rows.] => orient.dated_state
## FUNC 9[Parse the actual bounded packet task headings and named fields.] => orient.tasks
## FUNC 9[Assess every selected source checklist row without hiding cheap failures or authority limits.] => orient.run_checks
## FUNC 9[Render the actual consumer owner blockers, goal/current/next and every check.] => orient.run
## FUNC 9[Assess all and only explicitly supplied project roots once.] => orient.run_portfolio
## FUNC 9[Expose explicit orient/check/portfolio/roots-file CLI boundaries.] => orient.main
## FUNC 9[Retain exact readonly Git query identity and refuse confirmed execution failures.] => orient.query
## FUNC 9[Append one actual owning checklist judgment and its safe critical trace.] => orient.add
## FUNC 9[Extract the actual first goal paragraph from supported VISION layouts without adopting trailing deferred or example prose.] => orient.vision_purpose
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY orient, consumer PM, explicit paths, complete population, supported grammar, evidence
## @STRUCTURE ▶ explicit inputs → ◇ validate supported shape → ○ own operations → ⎋ attributable result or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import argparse
import datetime
import logging
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
import consumer_files as cf

logger=logging.getLogger('orient')
MARKER='<<< WE ARE HERE'
HEADINGS=['Blocked on the owner','State','Queue','Traps']

# region CLASS_Check [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Carry one structural checklist judgment and its explicit authority limit.
## @uses dataclasses.dataclass
## @io Input: id CHECK-NN str; status PASS|FAIL|N/A|UNAVAILABLE; reason nonempty str; evidence list[str]; limited str. Output: same fields; no authority from construction. Example: CHECK-20 UNAVAILABLE retains missing ledger burden.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class Check:
    id: str
    status: str
    reason: str
    evidence: list
    limited: str = 'Structural recognition only; human authority and full meaning independently judged.'
# endregion CLASS_Check


# region FUNC_git_info [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Observe only actual repository-root Git or an explicit filesystem baseline.
## @uses subprocess.run, consumer_files.identity, consumer_files.fail
## @io Input: root str|Path. Output: dict repository bool, own changed paths/argv/root/reason or complete regular relative baseline path/SHA/mode. Sanitizes GIT_* and disables locks/fsmonitor/cache. Reads only; confirmed Git failure ConsumerInputError, no silent clean fallback. Example: nested root receives only nested filesystem records.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def git_info(root):
    # START_BLOCK_Validation
    # BUG_FIX_CONTEXT: shared actual-root Git binding prevents ancestor adoption and preserves gitfiles.
    logger.info('[IMP:4][git_info][INIT] begin owned scoped operation')
    root=Path(root).resolve();observation=cf.repository_changes(root)
    if observation is None:
        baseline=[dict(path=path.relative_to(root).as_posix(),**cf.identity(path)) for path in sorted(root.rglob('*')) if path.is_file() and not path.is_symlink() and not {'.methodology','.git'}&set(path.relative_to(root).parts)]
        logger.info('[IMP:9][git_info][FILESYSTEM_BASELINE] files=%d',len(baseline))
        _trajectory_return = {'repository':False,'baseline':baseline,'reason':'Explicit current filesystem observation; no Git-clean claim.'}; logger.debug('[IMP:3][git_info][RETURN] owned result evaluated'); return _trajectory_return
    observation['reason']='Actual root-bound no-lock sanitized observer, no mutation.'
    logger.info('[IMP:9][git_info][OBSERVED] changed=%d read-only',len(observation['changed']))
    _trajectory_return = observation; logger.debug('[IMP:3][git_info][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_Validation

# endregion FUNC_git_info


# region FUNC_git_history [DOMAIN(9): ConsumerPM; CONCEPT(9): LayerOwnership, Archive; TECH(8): Git]
## @purpose Inspect real root-bound commit paths and archived batch chronology for layered writes and leftover merged branches.
## @uses orient.query, consumer_files.ConsumerInputError, consumer_files.fail, consumer_files.Layout
## @io Input: Layout with actual contained homes and git_info dictionary. Output: dict crossLayer list of commit IDs, archived int-or-None,
##   leftover branch-name list, worktree paths and commands; no Git returns not-applicable facts. Side effects: readonly Git children only.
##   Guarantees: ancestor Git is excluded; all actual HEAD commits assessed for layer crossing; owner exception recognized structurally and independently judged.
##   Errors: ConsumerInputError when a confirmed repository query fails; never silent no-history PASS.
##   Example: a merged branch tip at100 before last archived batch at200 is leftover even while current TASKS is proposed. Importance:9.
## @complexity 8
def git_history(layout,observation):
    # START_BLOCK_Validation
    logger.info('[IMP:4][git_history][INIT] begin owned scoped operation')
    result={'crossLayer':[],'archived':None,'leftovers':[],'worktrees':[],'commands':[]}
    if not observation['repository']: logger.info('[IMP:9][git_history][NO_REPOSITORY] root absence measured; history not applicable'); _trajectory_return = result; logger.debug('[IMP:3][git_history][RETURN] owned result evaluated'); return _trajectory_return
    command=observation['argv'];env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
    # Unborn own repository has no commit; that bounded absence is measured separately.
    heads=query(command,env,result,['rev-parse','--is-shallow-repository']).strip()
    if heads=='true': cf.fail('git_history','incomplete-shallow-history')
    # rev-list --all succeeds in an unborn repository; HEAD must exist before asking its history.
    all_ids=query(command,env,result,['rev-list','--all']).splitlines()
    if not all_ids: logger.info('[IMP:9][git_history][UNBORN] complete own repository has zero commits'); _trajectory_return = result; logger.debug('[IMP:3][git_history][RETURN] owned result evaluated'); return _trajectory_return
    commits=query(command,env,result,['rev-list','HEAD']).splitlines()
    logger.info('[IMP:9][git_history][HISTORY_VALID] commits=%d',len(commits))
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    if layout.mode=='layered':
        layer=layout.layer.relative_to(layout.root).as_posix().rstrip('/')+'/'
        normative=[layout.homes['vision'].relative_to(layout.root).as_posix(), 'docs/architecture/',layout.homes['decisions'].relative_to(layout.root).as_posix().rstrip('/')+'/']
        for commit in commits:
            paths=query(command,env,result,['diff-tree','--root','--no-commit-id','--name-only','-r','-z',commit]).split('\0')
            if any(path.startswith(layer) for path in paths) and any(path==prefix or path.startswith(prefix) for prefix in normative for path in paths):
                message=query(command,env,result,['show','-s','--format=%B',commit])
                if not re.search(r'owner(?:\s*[-:]?\s*)exception',message,re.I): result['crossLayer'].append(commit)
    notes=layout.homes['notes'].relative_to(layout.root).as_posix()
    archived=query(command,env,result,['log','-1','--format=%ct','--',':(glob)'+notes+'/B-*-tasks.md']).strip()
    if archived:
        if not archived.isdecimal(): cf.fail('git_history','invalid-archive-clock')
        result['archived']=int(archived)
        current=query(command,env,result,['branch','--show-current']).strip()
        branches=query(command,env,result,['branch','--merged','HEAD','--format=%(refname:short) %(committerdate:unix)'])
        for line in branches.splitlines():
            name,separator,stamp=line.rpartition(' ')
            if not separator or not stamp.isdecimal(): cf.fail('git_history','invalid-branch-clock')
            if name!=current and int(stamp)<result['archived']: result['leftovers'].append(name)
        paths={};path=None
        for field in query(command,env,result,['worktree','list','--porcelain','-z']).split('\0'):
            if field.startswith('worktree '): path=field[9:]
            elif field.startswith('branch refs/heads/') and path: paths[field[18:]]=path
        result['worktrees']=[paths[name] for name in result['leftovers'] if name in paths]
    logger.info('[IMP:9][git_history][RESULT] crossings=%d leftovers=%d',len(result['crossLayer']),len(result['leftovers']))
    _trajectory_return = result; logger.debug('[IMP:3][git_history][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_git_history


# region FUNC_map_lifecycles [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteMaps; TECH(8): Filesystem]
## @purpose Assess each actual root Doxyfile configuration separately through the shared complete population reader.
## @uses consumer_files.parse_doxyfile, consumer_files.covered_sources, consumer_files.contained
## @io Input: Layout and root-bound git_info facts. Output: ordered list dict config/index/state/newer/sources/reason;
##   config identities and source identities retained for each map. Side effects: reads only; no rebuild or current-answer claim.
##   Guarantees: root Doxyfile* except .bak/.orig plus explicitly declared config inspected; one failed map never hides others.
##   Errors: safe unavailable row for ConsumerInputError/OSError; nonrepository newer sources are stale.
##   Example: fresh primary plus stale secondary yields two separate rows and CHECK-15 failure. Importance:9.
## @complexity 6
def map_lifecycles(layout,observation):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][map_lifecycles][INIT] begin owned scoped operation')
    root=layout.root; configs=sorted(set([layout.homes['config']]+[p for p in root.glob('Doxyfile*') if p.suffix not in ('.bak','.orig') and p.is_file()]))
    result=[];changed=set(observation.get('changed',[]))
    for path in configs:
        try:
            cf.contained(root,path);config=cf.parse_doxyfile(cf.read_text(path));population=cf.covered_sources(root,config)
            index=cf.contained(root,cf.contained(root,(config.settings.get('OUTPUT_DIRECTORY') or ['doxygen_output'])[0])/(config.settings.get('XML_OUTPUT') or ['xml'])[0]/'index.xml')
            newer=[p for p in population.files if index.is_file() and (root/p).stat().st_mtime_ns>index.stat().st_mtime_ns]
            state='no sources yet' if not population.files else 'not built' if not index.is_file() else 'fresh' if not newer else 'in progress' if observation['repository'] and all(p in changed for p in newer) else 'stale'
            row={'config':str(path),'index':str(index),'state':state,'newer':newer,'sources':population.source_identities,'configIdentity':cf.identity(path),'reason':'Lifecycle only; complete own map answer separately proved'}
            logger.info('[IMP:9][map_lifecycles][MAP_RESULT] state=%s sources=%d',state,len(population.files))
        except (cf.ConsumerInputError,OSError) as error:
            row={'config':str(path),'index':'','state':'unavailable','reason':type(error).__name__}
            logger.error('[IMP:10][map_lifecycles][MAP_UNAVAILABLE] kind=%s',type(error).__name__)
        result.append(row)
    _trajectory_return = result; logger.debug('[IMP:3][map_lifecycles][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_map_lifecycles


# region FUNC_collect [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Read the complete selected operative record/config/Git populations once.
## @uses consumer_files.resolve_layout, consumer_files.parse_front_matter, consumer_files.covered_sources, orient.git_info, orient.git_history
## @io Input: root str|Path, now aware UTC datetime optional. Output: facts root/layout/now/texts/metadata/errors/paths/git/history/config/population/map. Retains unsupported legacy/read/coverage gaps; no writes. Example: fake conventions timestamp remains selected CHECK-08 evidence.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def collect(root,now=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][collect][INIT] begin owned scoped operation')
    logger.info('[IMP:4][collect][INIT] explicit selected project')
    root=Path(root).resolve(); layout=cf.resolve_layout(root)
    facts={'root':root,'layout':layout,'now':now or datetime.datetime.now(datetime.timezone.utc),'texts':{},'metadata':{},'errors':[],'paths':{},'git':git_info(root)}
    if layout.legacy:
        facts['errors'].append('legacy-read-only-dialect; unsupported native assessment'); _trajectory_return = facts; logger.debug('[IMP:3][collect][RETURN] owned result evaluated'); return _trajectory_return
    facts['history']=git_history(layout,facts['git'])
    paths={k:v for k,v in layout.homes.items() if k in ('entry','vision','roadmap','handoff','tasks','open_questions')}
    # BUG_FIX_CONTEXT: selected conventions and optional CLAUDE were silently omitted from operative scans.
    paths['conventions']=root/'CONVENTIONS.md'
    if (root/'CLAUDE.md').exists(): paths['claude']=cf.contained(root,'CLAUDE.md')
    if layout.mode=='layered':
        for kind,filename in (('roadmap','ROADMAP.md'),('handoff','HANDOFF.md'),('tasks','TASKS.md')):
            if (root/filename).is_file() and root/filename!=layout.homes[kind]: paths[kind+':root']=root/filename
    for kind in ('decisions','specs','recon','notes'):
        directory=layout.homes[kind]
        if directory.exists():
            for path in sorted(directory.rglob('*.md')):
                cf.contained(root,path)
                paths[kind+':'+path.relative_to(root).as_posix()]=path
    for key,path in paths.items():
        facts['paths'][key]=path
        if key=='open_questions' and not path.exists(): continue
        try:
            text=cf.read_text(path); facts['texts'][key]=text; facts['metadata'][key]=cf.parse_front_matter(text)
        except cf.ConsumerInputError as error:
            facts['errors'].append(key+':'+str(error))
    try:
        config=cf.parse_doxyfile(cf.read_text(layout.homes['config'])); population=cf.covered_sources(root,config)
        facts['config']=config; facts['population']=population
        index=cf.contained(root,cf.contained(root,(config.settings.get('OUTPUT_DIRECTORY') or ['doxygen_output'])[0])/(config.settings.get('XML_OUTPUT') or ['xml'])[0]/'index.xml')
        newer=[p for p in population.files if index.exists() and (root/p).stat().st_mtime_ns>index.stat().st_mtime_ns]
        changed=set(facts['git'].get('changed',[]))
        state='no sources yet' if not population.files else 'not built' if not index.is_file() else 'fresh' if not newer else 'in progress' if facts['git']['repository'] and all(x in changed for x in newer) else 'stale'
        facts['map']={'state':state,'index':str(index),'newer':newer}
    except cf.ConsumerInputError as error:
        facts['errors'].append('coverage:'+str(error))
    facts['maps']=map_lifecycles(layout,facts['git'])
    logger.info('[IMP:9][collect][COLLECTED] records=%d gaps=%d',len(facts['texts']),len(facts['errors']))
    _trajectory_return = facts; logger.debug('[IMP:3][collect][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_collect


# region FUNC_dated_state [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Count actual date-led State items while excluding code fences and table rows.
## @uses re.fullmatch
## @io Input: text complete handoff str. Output: nonnegative int; paragraphs start after blank/heading, list-date items counted individually. No effects. Example: two date bullets plus fenced dates yield2.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def dated_state(text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][dated_state][INIT] begin owned scoped operation')
    section=None; fence=False; opens=True; count=0
    for line in text.splitlines():
        if line.lstrip().startswith(('```','~~~')):
            # BUG_FIX_CONTEXT: a closing fence/table ends its block; next date starts a paragraph even without a blank.
            fence=not fence; opens=not fence; continue
        if fence: continue
        if line.lstrip().startswith('|'): opens=True; continue
        match=re.fullmatch(r'##\s+(.+?)\s*',line)
        if match:
            section=match.group(1); opens=True; continue
        if section=='State' and not line.lstrip().startswith('|') and re.match(r'^\s*(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*)?\d{4}-\d{2}-\d{2}',line) and (opens or re.match(r'^\s*(?:[-*+]|\d+[.)])\s+',line)):
            count+=1
        opens=not line.strip()
    _trajectory_return = count; logger.debug('[IMP:3][dated_state][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_dated_state


# region FUNC_tasks [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Parse the actual bounded packet task headings and named fields.
## @uses re.finditer
## @io Input: text complete TASKS str. Output: ordered list[{id,title,fields dict lowercase->str}]; class/status/finish/stops/links/evidence remain caller checked. No effects. Example: T-001 heading with Class S exposes fields["class"]==S.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def tasks(text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][tasks][INIT] begin owned scoped operation')
    rows=[]
    matches=list(re.finditer(r'^##\s+(T-\d+)\s+(.+)$',text,re.M))
    for i,match in enumerate(matches):
        body=text[match.end():matches[i+1].start() if i+1<len(matches) else len(text)]
        fields={k.lower():v.strip() for k,v in re.findall(r'^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.*)$',body,re.M)}
        rows.append(dict(id=match.group(1),title=match.group(2),fields=fields))
    _trajectory_return = rows; logger.debug('[IMP:3][tasks][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_tasks


# region FUNC_run_checks [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Assess every selected source checklist row without hiding cheap failures or authority limits.
## @uses orient.add, orient.tasks, orient.dated_state, consumer_files.provenance, consumer_files.timestamp, pathlib.Path.exists
## @io Input: facts complete collect dict. Output: exactly22 ordered Check rows; unavailable profile/read/coverage propagates to all selected rows. Independent structural metadata/budgets/task/DEC/clock/Git/markup predicates; no consent judgment or writes. CHECK09 inspects deduplicated Layout.root/Layout.layer roots, rejects each existing generic DevelopmentPlan.md with actual relative evidence, and reports safe root/violation counts; no invented unadopted roots. Single-layer checks one root; layered root-record recursion retains its observed repeated owning row9 events. Feature-specific specs/PQ1-DevelopmentPlan.md is legal. Example: a generic root plan fails even when the selected flow root is clean.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def run_checks(facts):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][run_checks][INIT] begin owned scoped operation')
    logger.info('[IMP:4][run_checks][INIT] all22 selected rows')
    layout=facts['layout']; texts=facts['texts']; meta=facts['metadata']; root=facts['root']; rows=[]
    limits=dict(cf.BUDGETS); limits.update(layout.overrides)
    if layout.legacy or facts['errors']:
        for number in range(1,23): add(rows,layout,number,False,'Required profile/read/coverage unavailable: '+', '.join(facts['errors']),status='UNAVAILABLE')
        _trajectory_return = rows; logger.debug('[IMP:3][run_checks][RETURN] owned result evaluated'); return _trajectory_return
    agents=texts['entry']; roadmap=texts['roadmap']; handoff=texts['handoff']; packet=texts['tasks']; task_rows=tasks(packet); packet_meta=meta['tasks']
    clause=not (root/'CLAUDE.md').exists() or '@AGENTS.md' in cf.read_text(root/'CLAUDE.md')
    add(rows,layout,1,cf.PROFILE in agents and layout.mode in agents and str(layout.version) in agents and clause,'Explicit profile/mode/version and optional interoperability pointer; actual homes declared.')
    lines=roadmap.splitlines(); steps=[x for x in lines if re.match(r'^\s*[-*]\s+\[[ xX~]\]',x)]
    current=[x for x in steps if MARKER in x]
    ids=re.findall(r'\*\*([A-Z]+\d+[a-z]?)\.',roadmap)
    mermaid=re.search(r'```mermaid\s*\n(.*?)```',roadmap,re.S)
    diagram_ok=bool(mermaid) and all(re.search(r'\b'+re.escape(x)+r'\b',mermaid.group(1)) for x in ids)
    add(rows,layout,2,roadmap.count(MARKER)==1 and len(current)==1 and (not any('🔜' in step for step in steps) or '🔜' in current[0]) and diagram_ok and re.search(r'^## Deferred on purpose\s*$',roadmap,re.M) and all(len(x)<=limits['roadmap_step_chars'] for x in steps) and len(roadmap)<=limits['roadmap_chars'],'One current-step marker/Mermaid matching ids/deferred; measured steps=%d chars=%d'%(len(steps),len(roadmap)),[layout.homes['roadmap']])
    headings=re.findall(r'^##\s+(.+?)\s*$',handoff,re.M)
    add(rows,layout,3,[heading for heading in headings if heading in HEADINGS]==HEADINGS and headings[0]=='Blocked on the owner' and len(handoff.splitlines())<=limits['handoff_lines'],'Actual headings=%s lines=%d'%(headings,len(handoff.splitlines())),[layout.homes['handoff']])
    specs=[k for k in texts if k.startswith('specs:') and not facts['paths'][k].name.endswith('-DevelopmentPlan.md')]
    add(rows,layout,4,all(meta[k].get('status') and meta[k].get('input') and not facts['paths'][k].name.startswith('draft-') and (meta[k]['status']=='draft' or meta[k].get('batch') or isinstance(meta[k].get('gate1'),dict) and meta[k]['gate1'].get('via')) for k in specs),'Every actual specification required fields/naming/gate-or-batch checked; count=%d'%len(specs))
    decisions={}; duplicate=[]
    for k in texts:
        if k.startswith('decisions:'):
            id=meta[k].get('id','')
            if id in decisions: duplicate.append(id)
            decisions[id]=k
    dec_errors=[]
    for id,k in decisions.items():
        data=meta[k]
        if not re.fullmatch(r'DEC-\d{3,}',str(id)) or data.get('status') not in ('accepted','superseded'): dec_errors.append(k+':status/id')
        try: cf.provenance(data.get('decided'),facts['now'],gate=True)
        except cf.ConsumerInputError: dec_errors.append(k+':decided')
        targets=data.get('amended_by',[]); targets=[targets] if isinstance(targets,str) else targets
        if not isinstance(targets,list): dec_errors.append(k+':amendment-shape'); targets=[]
        for target in targets:
            match=re.fullmatch(r'(DEC-\d{3,}):\s*\S.*',str(target))
            if not match or match.group(1) not in decisions: dec_errors.append(k+':missing-amendment-target')
        if data.get('status')=='superseded':
            target=data.get('superseded_by')
            if target not in decisions or meta[decisions[target]].get('supersedes')!=id: dec_errors.append(k+':supersession')
        if data.get('supersedes'):
            target=data['supersedes']
            if target not in decisions or meta[decisions[target]].get('superseded_by')!=id: dec_errors.append(k+':reverse-supersession')
    # BUG_FIX_CONTEXT: original checker ignored amended_by. Each item now resolves exact id, retaining valid siblings.
    add(rows,layout,5,not dec_errors and not duplicate,'Every DEC/amendment/supersession checked; records=%d errors=%d'%(len(decisions),len(dec_errors)))
    recon=[k for k in texts if k.startswith('recon:') and facts['paths'][k].name.startswith('RECON_')]
    add(rows,layout,6,not list(root.glob('RECON_*.md')) and all(all(term in texts[k] for term in ('Contradictions','Not checked','Open forks')) for k in recon),'All declared recon sections and root absence checked; count=%d'%len(recon))
    note_patterns=[r'[A-Z][A-Za-z0-9.]*-[a-z0-9][a-z0-9-]*\.md',r'candidate-[a-z0-9-]+\.md',r'[a-z0-9-]+-\d{4}-\d{2}-\d{2}\.md',r'B-\d{3,}-tasks\.md',r'README\.md']
    add(rows,layout,7,all(any(re.fullmatch(p,facts['paths'][k].name) for p in note_patterns) for k in texts if k.startswith('notes:')),'Every actual note name checked; no undeclared source scanning.')
    provenance_errors=[]
    for k in meta:
        if k in ('entry','claude'): continue
        data=meta[k]
        if not all(data.get(x) for x in ('type','title','status')): provenance_errors.append(k+':fields')
        try: cf.provenance(data.get('generated'),facts['now'])
        except cf.ConsumerInputError: provenance_errors.append(k+':generated')
    add(rows,layout,8,not provenance_errors,'Nested generated metadata checked on every operative document; errors=%d'%len(provenance_errors))
    # BUG_FIX_CONTEXT: checking only the selected flow root missed the adopted normative root.
    # Root-record recursion keeps the same layout and does not aggregate row9; owning row9 must cover both distinct roots itself.
    # Inspect only actual layout roots, not arbitrary unadopted descendants; keep feature-specific plans in declared specs legal.
    plan_roots=sorted({layout.root,layout.layer})
    generic_plans=[path/'DevelopmentPlan.md' for path in plan_roots if (path/'DevelopmentPlan.md').exists()]
    logger.info('[IMP:9][run_checks][PLAN_ROOTS] roots=%d violations=%d',len(plan_roots),len(generic_plans))
    add(rows,layout,9,not generic_plans,'No root/layer DevelopmentPlan.md; checkpoint plans use declared specs home. Checked roots=%d violations=%d'%(len(plan_roots),len(generic_plans)),[path.relative_to(root).as_posix() for path in generic_plans])
    # BUG_FIX_CONTEXT: original native row always withheld actual Git layered duty; inspect real commit paths.
    history=facts['history']
    add(rows,layout,10,not history['crossLayer'],'Actual root-bound layer history: crossings=%d; exception authority separately judged.'%len(history['crossLayer']),status='N/A' if not facts['git']['repository'] or layout.mode=='single-layer' else None)

    add(rows,layout,11,all(meta[k].get('status')=='draft' or all(x in texts[k] for x in ('Done when','Stop and ask when')) for k in specs),'Each non-draft spec actual finish/stops checked.')
    # BUG_FIX_CONTEXT: a missing marker does not erase an actual current checkpoint.
    # Marker validity remains CHECK-02; current-step progress independently controls CHECK-12.
    active=any("🔜" in step for step in steps)
    open_tasks=[x for x in task_rows if x['fields'].get('status') not in ('done','dropped')]
    add(rows,layout,12,active or packet_meta.get('status')=='idle' and not open_tasks,'Idle packet requires no open task when route has no current checkpoint.')
    instruction_text='\n'.join([agents]+[texts[k] for k in ('claude','conventions') if k in texts]+[texts[k] for k in specs])
    normalized=instruction_text.lower().replace('…','...').replace('—','-').replace('“','"').replace('”','"')
    add(rows,layout,13,not any(x in normalized for x in ('think carefully','think step by step','pause and reflect')),'Actual instruction hygiene with Unicode punctuation normalized.')
    total=sum(len(texts[k].splitlines()) for k in ('entry','vision','roadmap','handoff','tasks'))
    add(rows,layout,14,total<=limits['always_read_lines'],'Measured always-read=%d threshold=%d'%(total,limits['always_read_lines']))
    maps=facts['maps'];map_unavailable=any(row['state']=='unavailable' for row in maps)
    add(rows,layout,15,all(row['state'] in ('fresh','in progress','no sources yet') for row in maps),'Every actual configured map lifecycle: '+', '.join(Path(row['config']).name+'='+row['state'] for row in maps),[row['config'] for row in maps],status='UNAVAILABLE' if map_unavailable else None)

    task_errors=[]
    for task in task_rows:
        fields=task['fields']
        if fields.get('class') not in ('S','M') or fields.get('status') not in ('todo','doing','review','done','blocked','dropped') or not all(fields.get(x) for x in ('done when','stop and ask when','links')) or fields.get('status')=='done' and not fields.get('evidence'): task_errors.append(task['id'])
    gate_error=False
    if packet_meta.get('status') in ('approved','active'):
        try:
            cf.provenance(packet_meta.get('gate_a'),facts['now'],gate=True)
            gate_error=packet_meta['gate_a'].get('decision')!='approved' or not packet_meta['gate_a'].get('action') or not packet_meta['gate_a'].get('scope')
        except cf.ConsumerInputError: gate_error=True
    add(rows,layout,16,packet_meta.get('batch') and packet_meta.get('status') in ('proposed','approved','active','merged','idle') and not task_errors and not gate_error,'All task class/status/finish/stops/links/done-evidence and exact gate shape checked; errors=%d'%(len(task_errors)+int(gate_error)))
    # BUG_FIX_CONTEXT: current proposed packet cannot erase leftover branches from an archived earlier batch.
    add(rows,layout,17,not history['leftovers'],'Actual archived batch clock=%s; leftover merged branches=%s; worktrees=%s; no cleanup authority.'%(history['archived'],history['leftovers'],history['worktrees']),status='N/A' if not facts['git']['repository'] or history['archived'] is None else None)

    reservations=re.findall(r'\*\*Reserves:\*\*\s*(DEC-\d{3,})',packet)
    cited=set(re.findall(r'\bDEC-\d{3,}\b','\n'.join(texts[k] for k in ('entry','vision','roadmap','handoff','tasks','open_questions') if k in texts)))
    add(rows,layout,18,not duplicate and len(reservations)==len(set(reservations)) and not set(reservations)&set(decisions) and cited<=set(decisions)|set(reservations),'Exact DEC references/reservations checked; unresolved=%d'%len(cited-set(decisions)-set(reservations)))
    fresh=True
    if packet_meta.get('status') in ('approved','active'):
        try: fresh=cf.provenance(meta['handoff'].get('generated'),facts['now'])>=cf.provenance(packet_meta.get('gate_a'),facts['now'],gate=True)
        except cf.ConsumerInputError: fresh=False
    add(rows,layout,19,fresh,'Active/approved handoff timestamp compared to actual gate, never template authority.')
    candidates=[k for k in texts if k.startswith('notes:') and facts['paths'][k].name.startswith('candidate-')]
    local_candidate_errors=[]
    for key in candidates:
        data=meta[key]
        if data.get('status') not in ('pending','ingested','rejected') or data.get('type')!='Candidate': local_candidate_errors.append(key+':status/type')
        pointer=data.get('source')
        if not isinstance(pointer,str) or not pointer.strip(): local_candidate_errors.append(key+':source')
        else:
            try:
                target=cf.contained(root,pointer)
                if not target.is_file(): local_candidate_errors.append(key+':unresolved-source')
            except cf.ConsumerInputError: local_candidate_errors.append(key+':source-access')
        if data.get('status') in ('ingested','rejected') and not data.get('outcome'): local_candidate_errors.append(key+':outcome')
    if local_candidate_errors: logger.error('[IMP:10][run_checks][CANDIDATE_STATUS_FAILURE] count=%d',len(local_candidate_errors))
    add(rows,layout,20,not local_candidate_errors,'Local candidate rows=%d invalid=%d; required external ledger comparison unavailable C4, no old fallback.'%(len(candidates),len(local_candidate_errors)),status='FAIL' if local_candidate_errors else 'UNAVAILABLE' if candidates else 'N/A')
    counts={key:dated_state(value) for key,value in texts.items() if key=='handoff' or key.startswith('handoff:')}
    count=max(counts.values())
    add(rows,layout,21,all(value<=limits['handoff_dates'] for value in counts.values()),'Actual date-led State items=%d threshold=%d'%(count,limits['handoff_dates']))
    leftovers=[]
    for path in facts['population'].files:
        if path.endswith('.py') and re.search(r'^#(?!#)\s*(?:GREP_SUMMARY|STRUCTURE):',cf.read_text(root/path),re.M): leftovers.append(path)
    aliases=[name for name,value in facts['config'].aliases.items() if name in cf.BLOCK_TAGS and value.endswith('^^')]
    add(rows,layout,22,not leftovers and not aliases,'Covered legacy Python lines=%d/effective old block aliases=%d'%(len(leftovers),len(aliases)))
    # BUG_FIX_CONTEXT: checking only flow homes discarded applicable root-layer route/packet/baton budgets.
    layer_keys=[key for key in ('roadmap:root','handoff:root','tasks:root') if key in texts]
    if layer_keys and not facts.get('_layer_child'):
        required=('roadmap','handoff','tasks')
        if len(layer_keys)!=3:
            for number in (2,3,12,14,16,19,21):
                row=rows[number-1];row.status='UNAVAILABLE';row.reason+='; incomplete actual root-layer records';row.evidence.extend(str(facts['paths'][key]) for key in layer_keys)
        else:
            child=dict(facts);child['texts']=dict(texts);child['metadata']=dict(meta);child['_layer_child']=True
            for kind in required:
                child['texts'][kind]=texts[kind+':root'];child['metadata'][kind]=meta[kind+':root']
            root_rows=run_checks(child)
            for number in (2,3,12,14,16,19,21):
                primary=rows[number-1];other=root_rows[number-1];rank={'N/A':0,'PASS':1,'FAIL':2,'UNAVAILABLE':3}
                if rank[other.status]>rank[primary.status]: primary.status=other.status
                primary.reason+='; root layer: '+other.reason;primary.evidence.extend(str(facts['paths'][key]) for key in layer_keys)
    logger.info('[IMP:9][run_checks][RESULT] rows=%d',len(rows))
    _trajectory_return = rows; logger.debug('[IMP:3][run_checks][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_run_checks


# region FUNC_vision_purpose [DOMAIN(9): ConsumerPM; CONCEPT(9): ActualPurpose; TECH(7): Markdown]
## @purpose Extract the actual first goal paragraph from supported VISION layouts without adopting trailing deferred or example prose.
## @uses re.fullmatch, re.match, str.splitlines
## @io Input: text str read from the layout-selected vision home. Output: whitespace-normalized first goal paragraph str bounded to120 characters, or explicit unavailable reason.
##   Supported inputs: unique Goal/Purpose heading (including descriptive suffix), or unique inline Goal:/Purpose: when no heading goal exists; frontmatter and fenced code excluded.
##   Guarantees: stops at next equal/higher heading; never substitutes audience, constraints, architecture, description or deferred sections. Duplicate goal sections and empty goal text stay unavailable.
##   Side effects: owning status/count log only; no files, imports or consumer execution. Errors: TypeError for a non-string caller contract violation.
##   Example: ## Goal and arrival criterion followed by Create records returns Create records even with later ## Deferred on purpose. Importance9.
## @complexity 5
def vision_purpose(text):
    # START_BLOCK_Validation
    lines=text.splitlines();visible=[];front=bool(lines and lines[0].strip()=='---');fence=None
    for ordinal,line in enumerate(lines):
        if front:
            if ordinal and line.strip()=='---':front=False
            continue
        marker=re.match(r'^\s*(`{3,}|~{3,})',line)
        if marker:
            token=marker.group(1)
            if fence is None:fence=token
            elif token[0]==fence[0] and len(token)>=len(fence):fence=None
            continue
        if fence is None:visible.append(line)
    headings=[(index,len(match.group(1))) for index,line in enumerate(visible) for match in [re.match(r'^(#{1,6})\s+(?:Goal|Purpose)(?:\s.*)?$',line,re.I)] if match]
    inline=[match.group(1).strip() for line in visible for match in [re.match(r'^\s*(?:Goal|Purpose):\s*(.*)$',line,re.I)] if match]
    candidates=len(headings) if headings else len(inline)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    if candidates!=1:
        reason='ambiguous goal' if candidates>1 else 'missing goal text'
        logger.info('[IMP:9][vision_purpose][UNAVAILABLE] cause=%s candidates=%d',reason.replace(' ','-'),candidates)
        return '(unavailable: '+reason+')'
    paragraph=[]
    if headings:
        index,level=headings[0]
        for line in visible[index+1:]:
            heading=re.match(r'^(#{1,6})\s+',line)
            if heading and len(heading.group(1))<=level:break
            if not line.strip():
                if paragraph:break
                continue
            if heading:break
            paragraph.append(line.strip())
    else:paragraph=inline
    result=' '.join(' '.join(paragraph).split())[:120]
    logger.info('[IMP:9][vision_purpose][RESULT] available=%s characters=%d',bool(result),len(result))
    return result or '(unavailable: missing goal text)'
    # END_BLOCK_BusinessLogic
# endregion FUNC_vision_purpose


# region FUNC_run [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Render the actual consumer owner blockers, goal/current/next and every check.
## @uses orient.collect, orient.run_checks, orient.tasks, orient.vision_purpose
## @io Input: project str|Path, check bool. Output: (int,text); unavailable2 dominates failed-check1, plain assessable orientation0. Actual blocker section/mode/version/current step/next task retained; safe input errors2. No writes or permission grant. Example: active T-001 is named while held M task remains pending.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def run(project,check=False):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][run][INIT] begin owned scoped operation')
    try:
        facts=collect(project); rows=run_checks(facts)
    except (cf.ConsumerInputError,OSError,ValueError) as error:
        logger.error('[IMP:10][run][UNAVAILABLE] kind=%s',type(error).__name__)
        _trajectory_return = 2,'orient: unavailable: '+type(error).__name__+'\n'; logger.info('[IMP:9][run][ORIENTATION] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
    unavailable=any(x.status=='UNAVAILABLE' for x in rows); failed=any(x.status=='FAIL' for x in rows)
    # BUG_FIX_CONTEXT: a generic blocker/path/next sentence discarded the actual recoverable consumer baton.
    handoff=facts['texts'].get('handoff','')
    blockers=re.search(r'^## Blocked on the owner\s*\n(.*?)(?=^## |\Z)',handoff,re.M|re.S)
    roadmap=facts['texts'].get('roadmap','');steps=[line for line in roadmap.splitlines() if re.match(r'^\s*[-*]\s+\[[ xX~]\]',line)]
    focus=next((line for line in steps if '🔜' in line),next((line for line in steps if MARKER in line),'(no current checkpoint)'))
    packet=tasks(facts['texts'].get('tasks',''));next_task=next((item for item in packet if item['fields'].get('status') not in ('done','dropped')) ,None)
    output=['Blocked on the owner',blockers.group(1).strip() if blockers else '- Actual owner blocker section unavailable.']
    if unavailable or failed: output.append('- Resolve the failed/unavailable required rows below before their dependent action.')
    output+=['profile: '+facts['layout'].profile,'mode: '+facts['layout'].mode,'conventions_version: '+facts['layout'].version,'purpose: '+vision_purpose(facts['texts'].get('vision','')),'focus: '+focus,'batch: '+str(facts['metadata'].get('tasks',{}).get('batch','(unavailable)')),'next task: '+(next_task['id']+' '+next_task['title']+' status='+str(next_task['fields'].get('status')) if next_task else '(none)'), 'Git: '+facts['git']['reason'],'changed paths: '+(', '.join(facts['git'].get('changed',[])) or '(none observed; filesystem baseline is not Git-clean)'),'layer: '+str(facts['layout'].layer)]
    output.extend('%s %s %s'%(x.id,x.status,x.reason) for x in rows)
    output+=['eligible next: only independently authenticated current exact task scope.','limits: structural checks never authenticate consent; C3/C4/C5/C6 held.']
    _trajectory_return = (2 if unavailable else 1 if check and failed else 0),'\n'.join(output)+'\n'; logger.info('[IMP:9][run][ORIENTATION] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_run


# region FUNC_run_portfolio [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Assess all and only explicitly supplied project roots once.
## @uses orient.run
## @io Input: roots finite iterable str|Path, check bool. Output: (max exit,text) in stable first-root order; duplicate resolved roots removed; empty2. No discovery or writes. Example: good0+unavailable2 yields2 and both full reports.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def run_portfolio(roots,check=False):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][run_portfolio][INIT] begin owned scoped operation')
    results=[run(root,check) for root in dict.fromkeys(str(Path(x).resolve()) for x in roots)]
    if not results: _trajectory_return = 2,'orient: unavailable: empty portfolio\n'; logger.debug('[IMP:3][run_portfolio][RETURN] owned result evaluated'); return _trajectory_return
    _trajectory_return = max(x[0] for x in results),'\n'.join(x[1] for x in results); logger.debug('[IMP:3][run_portfolio][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_run_portfolio


# region FUNC_main [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Expose explicit orient/check/portfolio/roots-file CLI boundaries.
## @uses consumer_files.SafeArgumentParser, orient.run, orient.run_portfolio, consumer_files.read_text
## @io Input: argv list[str]|None. Output: exit0|1|2 and complete stdout reports; ORIENT_LOG stderr diagnostics. Roots-file relative entries resolve from its parent; no implicit registry. argparse SystemExit2 on mutual exclusions/unknown flags/empty scope. Example: --roots-file roots.txt --check assesses every named project.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def main(argv=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][main][INIT] begin owned scoped operation')
    parser=cf.SafeArgumentParser(); parser.add_argument('project',nargs='?'); parser.add_argument('--check',action='store_true'); parser.add_argument('--portfolio',nargs='+'); parser.add_argument('--roots-file')
    args=parser.parse_args(argv)
    logging.basicConfig(level=getattr(logging,os.environ.get('ORIENT_LOG','WARNING').upper(),logging.WARNING),format='%(message)s',stream=sys.stderr)
    if args.project and (args.portfolio or args.roots_file): parser.error('PROJECT and portfolio are mutually exclusive')
    roots=list(args.portfolio or [])
    if args.roots_file:
        try:
            path=Path(args.roots_file).resolve()
            roots.extend(str((path.parent/x.strip()).resolve()) for x in cf.read_text(path).splitlines() if x.strip() and not x.lstrip().startswith('#'))
        except cf.ConsumerInputError:
            _trajectory_return = 2; logger.debug('[IMP:3][main][RETURN] owned result evaluated'); return _trajectory_return
    if roots: code,text=run_portfolio(roots,args.check)
    elif args.project: code,text=run(args.project,args.check)
    else: parser.error('explicit PROJECT or nonempty portfolio required')
    print(text,end=''); _trajectory_return = code; logger.debug('[IMP:3][main][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_main



# region FUNC_query [DOMAIN(8): ConsumerPM; CONCEPT(9): GitEvidence; TECH(8): subprocess]
## @purpose Retain exact readonly Git query identity and refuse confirmed execution failures.
## @uses subprocess.run, consumer_files.fail
## @io Input: command trusted sanitized root-bound Git base argv list[str], env sanitized actual dict[str,str], result owned history dict with commands list; internal git_history only;  args list[str] of internal trusted Git arguments. Output: decoded stdout preserving NUL path delimiters.
##   Side effects: one readonly child; appends command identity to supplied result. Guarantees: no Git environment injection or failure fallback.
##   Errors: ConsumerInputError on nonzero exit/OSError; no commit data in diagnostics. Example: query(['rev-list','HEAD']) returns full actual IDs. Importance:9.
## @complexity 3
def query(command,env,result,args):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][query][INIT] begin owned scoped operation')
    argv=command+args;result['commands'].append(argv)
    try: process=subprocess.run(argv,env=env,capture_output=True)
    except OSError: cf.fail('git_history','query-unavailable')
    if process.returncode: cf.fail('git_history','confirmed-query-failed')
    _trajectory_return = os.fsdecode(process.stdout); logger.info('[IMP:7][query][READ_SUCCESS] operation=%s exit=%d bytes=%d',args[0],process.returncode,len(process.stdout)); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_query




# region FUNC_add [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Append one actual owning checklist judgment and its safe critical trace.
## @uses orient.Check, logging.Logger.error
## @io Input: rows owned list[Check], layout current validated Layout; internal run_checks receives already evaluated real condition;  number int1..22, ok bool, reason nonempty str, evidence optional paths, status optional supported str. Output: None, one Check appended; FAIL emits own run_checks row ERROR10, other statuses INFO9. Example: add(2,False,reason) records CHECK-02 FAIL.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def add(rows,layout,number,ok,reason,evidence=None,status=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][add][INIT] begin owned scoped operation')
    status=status or ('PASS' if ok else 'FAIL')
    rows.append(Check('CHECK-%02d'%number,status,reason,[str(x) for x in (evidence or [layout.homes['entry']])]))
    if status=='FAIL': logger.error('[IMP:10][run_checks][ROW_FAILURE] row=%d',number)
    else: logger.info('[IMP:9][run_checks][ROW_RESULT] row=%d status=%s',number,status)
    # END_BLOCK_BusinessLogic
# endregion FUNC_add


if __name__=='__main__':
    raise SystemExit(main())
