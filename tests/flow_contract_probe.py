# region MODULE_CONTRACT [DOMAIN(9): DevelopmentFlow; CONCEPT(9): ContractEvidence; TECH(6): Python]
## @modulecontract
## @purpose Consume selected actual flow clauses in a finite test/example interpretation.
## @scope Live norm extraction, role evidence, finite event evaluation and real CLI output.
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
## FUNC 7[trace] => trace
## FUNC 7[refusal] => refusal
## FUNC 7[read subject] => read_subject
## FUNC 7[load contract] => load_contract
## FUNC 7[artifact error] => artifact_error
## FUNC 7[evidence error] => evidence_error
## FUNC 7[visual error] => visual_error
## FUNC 7[activation error] => activation_error
## FUNC 7[payload error] => payload_error
## FUNC 7[validate return] => validate_return
## FUNC 7[evaluate case] => evaluate_case
## FUNC 7[run cases] => run_cases
## FUNC 7[case input valid] => case_input_valid
## FUNC 7[main] => main
## @usecases
## - Adopter -> mutates a required clause -> sees explicit refusal before continuation.
## @GREP_SUMMARY development flow, live clauses, evidence validation, bounded cases, refusal, restoration
## @STRUCTURE live anchored norms -> selected semantics -> finite cases -> evidence decisions -> explicit JSON and LDD

def _module_contract():
    pass
# endregion MODULE_CONTRACT


import argparse
import hashlib
import json
import logging
import pathlib
import re
import sys

LOGGER = logging.getLogger('flow_probe')
SUBJECTS = ('flow/phases.md', 'flow/run-state.md', 'flow/delegation.md', 'flow/finalize.md', 'protocols/role-returns.md')
# Selected controlled sentences are test support, not a required authoring format.
PATTERNS = {'STATE-301': ('MUST',
               'The default Debug-entry cap is (?P<cap>four|\\d+); .* The counted unit is entry into Debug, '
               'not QA visits, successful fixes, subprocess retries or response corrections;'),
 'STATE-302': ('MUST',
               'An adapter cap must be a nonnegative integer; boolean, negative and nonintegral values are '
               'invalid\\. Where the adapter schema stores parameters as text, the adapter declares strict '
               'decimal parsing to this semantic integer and rejects ambiguous coercion\\. An adapter may '
               'lower the default cap\\. An increase above the current allowance requires an explicit '
               'bounded owner grant under GATE-1209 recorded with scope, reason and additional allowance '
               'before the next entry;'),
 'STATE-303': ('MUST',
               'Record the Debug entry spend (?P<timing>before) entering the phase; an initial or renewed QA '
               'consumes (?P<qa_charge>no) Debug entry\\. Code-origin BUG_REPORT, QA/Review defects and '
               'extension-origin actionable failures share this unit;'),
 'STATE-304': ('MUST',
               'A failed or BLOCKED Debug (?P<failed_spend>preserves) the consumed entry\\. Missing '
               'responses, crashes, changed candidates, amendments and recovery neither refund nor reset the '
               'cumulative spend; resuming the already recorded entry does not charge that same entry '
               'twice\\.'),
 'STATE-305': ('MUST',
               'When spent Debug entries reach the authorized cap, refuse the next Debug entry and '
               'escalate.*A recorded bounded owner grant extends permission while preserving cumulative '
               'spend and causal history\\. QA after the last permitted repair remains allowed;'),
 'STATE-401': ('MUST',
               'Maintain distinct response-correction, extraction/schema-validation, transport/error and '
               'test Anti-Loop counters with declared finite caps, episode/phase/session scope and increment '
               'rules\\. Response correction is at most (?P<response_cap>one) per phase attempt.*No retry '
               'kind resets Debug spend'),
 'STATE-404': ('MUST',
               'Keep test Anti-Loop/session failure counters separate from run repair allowance\\. Do not '
               'reset them to conceal a red run\\. For an unknown side-effect outcome, investigate actual '
               'completion and sink state before replay;'),
 'PHASE-201': ('MUST',
               'Before any phase action, load the assigned role and its applicable protocols.*Record the '
               'actual read evidence; absent assigned protocol/read evidence refuses phase action as '
               'CRITICAL_RULE_VIOLATION\\.'),
 'PHASE-403': ('MUST',
               'An applicable visual PASS requires the real command, output, exit code and evidence '
               'artifact; a NOT_APPLICABLE or SKIPPED result requires the actual activation facts and a '
               'reason\\.'),
 'PHASE-605': ('MUST',
               'After every fix that changes the candidate implementation, (?P<renew>renew full independent '
               'QA) before Finalize, including a scoped UI fix\\. Renew Review when its judged evidence '
               'changed\\. A prior-green flag, a scoped recheck, a debugger file list or supplemental E2E '
               '(?P<negation>MUST NOT) replace the required renewed QA\\.'),
 'STATE-501': ('MUST',
               'Changes to the specification, plan, rules, adapter, approved scope or candidate invalidate '
               'affected approval/verification evidence\\. Dirty tracked changes and untracked bytes are '
               'candidate changes even if HEAD is unchanged;'),
 'STATE-503': ('MUST',
               'Every candidate-changing fix invalidates the earlier QA verdict and requires full renewed '
               'independent QA before Finalize, including UI-only changes\\.'),
 'STATE-601': ('MUST',
               'Accept a recovered phase result only for the same run/task, current return schema, approved '
               'inputs/scope and actual candidate facts\\. Revalidate its role payload, evidence/artifact '
               'existence and containment, producer identity, timestamps and phase predicate'),
 'STATE-602': ('MUST',
               'A worker record must not set counters, budgets, approval, phase routing or authoritative '
               'freshness flags\\..*counter injection or claimed approval from a return is rejected before '
               'state mutation\\.'),
 'STATE-701': ('MUST NOT', 'Automatically resume or advance a terminal run\\.'),
 'PHASE-801': ('MAY',
               'Each declaration names producer and consumer, activation, required inputs/outputs/evidence, '
               'permissions, independence, counters and failure route;'),
 'PHASE-802': ('MUST',
               'An extension preserves approved gates, all shared phase evidence and scope restrictions, '
               'independent QA/Review, cumulative budgets and the full renewed QA predicate\\.'),
 'PHASE-804': ('MUST',
               'if E2E satisfies a required acceptance criterion, flaky cannot count as passed and its '
               'unsatisfied outcome must be routed explicitly\\.'),
 'PHASE-901': ('MUST',
               'The ordinary success route is (?P<routes>.+?); Debug FIXED returns to QA\\. These routes '
               'depend on each phase predicate above, not status text alone\\.')}
PATTERNS.update({
    'FINAL-401': ('MUST', r'If completing Finalize requires a source, configuration, syntax or annotation repair, return explicit (?P<outcome>ESCALATED_FINALIZE) with the required repair and evidence\. Obtain an owner continuation decision before that work; do not edit source/configuration in Finalize and do not automatically return to Debug\.'),
    'RETURN-101': ('MUST', r'Every return includes `phase`, `role`, `status`, nonempty `summary`, `runId`, `inputIdentity`, `candidateIdentity`, `contractVersion` and actual `evidence` references\.'),
    'RETURN-502': ('MUST', r'Code BUG_REPORT requires a populated `bugReport` containing nonempty `goal`, `actual`, `logAnalysis`, `dataAnalysis`, `hypothesis` and `recommendation`, plus actual failure evidence\. QA BUG_REPORT requires the same six fields\..*A missing conditional field rejects the return before continuation\.'),
    'RETURN-603': ('MUST', r'The `scans` list contains exactly all eight named identities: `green-test-trap`, `quantitative-ac`, `semantic-trace`, `infra-dod`, `side-effect-channel`, `secret-leak`, `real-path-shape` and `discriminating-test`\. Every entry has `id`, `status` as PASS/FAIL/N/A/BLOCKED, nonempty `reason` and actual `evidence` paths\.'),
    'RETURN-201': ('MUST', r'Extract the candidate payload, validate shape/types, validate status-dependent required fields, then verify semantics and evidence before writing accepted state\.'),
    'RETURN-102': ('MUST', r'Bootstrap and Architect use SUCCESS or BLOCKED; Code, QA and Review use SUCCESS, BUG_REPORT where actionable, or BLOCKED; Debug uses FIXED or BLOCKED; Finalize uses SUCCESS, BLOCKED or ESCALATED_FINALIZE\.'),
    'RETURN-104': ('MUST', r'Reject unknown fields unless an adapter extension explicitly declares their type, meaning, producer, consumer, required conditions and version before use\.'),
})


# region FUNC_trace [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Deliver safe LDD events to the configured logger.
## @io Function/block identifiers, importance and safe message -> logged event
## @complexity 7
def trace(func, block, importance, message):
    LOGGER.log(logging.ERROR if importance == 10 else logging.INFO, '[IMP:%d][%s][%s] %s', importance, func, block, message)
# endregion FUNC_trace


# region FUNC_refusal [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Emit the rejection trajectory and preserve its explicit code.
## @io Function identifier and refusal code -> same code
## @complexity 7
def refusal(func, code):
    trace(func, 'REFUSAL', 10, 'code=' + code)
    return code
# endregion FUNC_refusal


# region FUNC_read_subject [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Read live anchored full norm bodies while excluding fenced examples.
## @io Markdown path -> card, anchors, full norms, source text and content digest; malformed content raises ValueError
## @complexity 7
def read_subject(path):
    trace('read_subject', 'READ', 7, 'subject=' + path.name)
    try:
        text = path.read_text(encoding='utf-8').replace('\r\n', '\n')
    except OSError:
        trace('read_subject','REFUSAL',10,'code=CONTRACT_READ_FAILED')
        raise
    norms, anchors, current, active, fence = {}, [], None, None, None
    parts = text.split('---',2)
    if len(parts) != 3:
        raise ValueError(refusal('read_subject','CONTRACT_CARD_MALFORMED'))
    card = dict(re.findall(r'^([a-z-]+): (.+)$', parts[1], re.M))
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            char = marker.group(1)[0]
            fence = None if fence == char else char if fence is None else fence
            continue
        if fence:
            continue
        anchor = re.fullmatch(r'<!-- anchor: (\S+) -->', line)
        if anchor:
            current, active = anchor.group(1), None
            if current in anchors:
                raise ValueError(refusal('load_contract', 'CONTRACT_DUPLICATE_ANCHOR'))
            anchors.append(current)
        hit = re.match(r'^- \*\*([A-Z]+-\d+)\*\* (MUST NOT|SHOULD NOT|MUST|SHOULD|MAY): (.+)$', line)
        if hit:
            active = hit.group(1)
            if not current or active in norms:
                raise ValueError(refusal('load_contract', 'CONTRACT_DUPLICATE_OR_UNANCHORED_NORM'))
            norms[active] = {'anchor': current, 'level': hit.group(2), 'body': hit.group(3)}
        elif active and line.startswith(('  ', '\t')):
            norms[active]['body'] += '\n' + line.strip()
        elif line.strip():
            active = None
    if fence:
        raise ValueError(refusal('load_contract', 'CONTRACT_UNCLOSED_FENCE'))
    trace('read_subject', 'PARSED', 9, 'norms=%d anchors=%d' % (len(norms), len(anchors)))
    return {'card': card, 'anchors': anchors, 'norms': norms, 'text': text, 'sha256': hashlib.sha256(text.encode()).hexdigest()}
# endregion FUNC_read_subject


# region FUNC_load_contract [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Derive the selected semantic bundle from actual anchored clauses and grant bounds.
## @io Repository root -> semantic bundle; unsupported critical semantics raise ValueError
## @complexity 7
def load_contract(root):
    root = pathlib.Path(root).resolve()
    subjects = {path: read_subject(root / path) for path in SUBJECTS}
    norms = {}
    for relative, subject in subjects.items():
        if subject['card'].get('status') != 'draft':
            raise ValueError(refusal('load_contract', 'CONTRACT_NOT_DRAFT'))
        for name, norm in subject['norms'].items():
            if name in norms:
                raise ValueError(refusal('load_contract', 'CONTRACT_DUPLICATE_NORM'))
            norms[name] = dict(norm, path=relative)
    selected = {}
    for name, (level, pattern) in PATTERNS.items():
        norm = norms.get(name)
        match = re.search(pattern, norm['body']) if norm and norm['level'] == level else None
        if not match:
            trace('load_contract', 'REFUSAL', 10, 'unsupported norm=' + name)
            raise ValueError('CONTRACT_SEMANTICS:' + name)
        selected[name] = match.groupdict()
    # Dynamic numeric/field extraction is kept separate from independently authored case expectations.
    default_word = selected['STATE-301']['cap']
    default_cap = {'four': 4}.get(default_word, int(default_word) if default_word.isdigit() else None)
    if default_cap is None:
        raise ValueError(refusal('load_contract', 'CONTRACT_CAP_UNSUPPORTED'))
    common = re.findall(r'`([A-Za-z][A-Za-z0-9]*)`', norms['RETURN-101']['body'])
    bug_fields = re.findall(r'`([A-Za-z][A-Za-z0-9]*)`', norms['RETURN-502']['body'])
    transitions = {}
    route_text = selected['PHASE-901']['routes']
    for source, target in re.findall(r'(Bootstrap|Architect|Code|QA|Review) SUCCESS to (Architect|Code|QA|Review|Finalize)', route_text):
        transitions[(source, 'SUCCESS')] = (target, 'PHASE-901')
    phase_clauses = {'Bootstrap':'PHASE-303','Architect':'PHASE-405','Code':'PHASE-503','QA':'PHASE-603','Review':'PHASE-604'}
    for source,norm_id in phase_clauses.items():
        target_match = re.search(r'On a validated '+source+r' SUCCESS.*?proceed to (?:independent )?(\w+)', norms[norm_id]['body'])
        if not target_match or transitions.get((source,'SUCCESS'),(None,None))[0] != target_match.group(1):
            trace('load_contract','REFUSAL',10,'inconsistent transition norm=PHASE-901')
            raise ValueError('CONTRACT_SEMANTICS:PHASE-901')
    if len(transitions) != 5 or not common or not bug_fields:
        raise ValueError(refusal('load_contract', 'CONTRACT_INTERFACE_UNSUPPORTED'))
    debug_route = re.search(r'Debug FIXED returns to (\w+)',norms['PHASE-901']['body'])
    if not debug_route or debug_route.group(1)!='QA':
        raise ValueError(refusal('load_contract','CONTRACT_SEMANTICS:PHASE-901'))
    transitions[('Debug','FIXED')]=(debug_route.group(1),'PHASE-901')
    required = {}
    for phase, norm_id in {'Bootstrap':'RETURN-301','Architect':'RETURN-401','Code':'RETURN-501','QA':'RETURN-601','Review':'RETURN-604','Debug':'RETURN-701','Finalize':'RETURN-801'}.items():
        body = norms[norm_id]['body']
        if norms[norm_id]['level'] != 'MUST' or 'includes' not in body and 'returns' not in body:
            raise ValueError(refusal('load_contract','CONTRACT_ROLE_PAYLOAD:' + norm_id))
        required[phase] = re.findall(r'`([A-Za-z][A-Za-z0-9]*)`', body.split('. ', 1)[0])
        if not required[phase]:
            raise ValueError(refusal('load_contract','CONTRACT_ROLE_PAYLOAD:' + norm_id))
    status_fields = {(phase,'FIXED' if phase=='Debug' else 'SUCCESS'):fields for phase,fields in required.items()}
    for phase in required:
        status_fields[(phase,'BLOCKED')]=['reason','limitations']
    status_fields[('Debug','BLOCKED')]=['rootCause','reason','limitations']
    for phase in ('Code','QA','Review'):
        status_fields[(phase,'BUG_REPORT')]=['bugReport']
    for status in ('SUCCESS','BUG_REPORT','BLOCKED'):
        status_fields[('QA',status)]=list(dict.fromkeys(required['QA']+status_fields[('QA',status)]))
        status_fields[('Review',status)]=list(dict.fromkeys(['findings','limitations']+status_fields[('Review',status)]))
    status_fields[('Finalize','ESCALATED_FINALIZE')]=['requiredRepair','reason','limitations']
    visual = re.search(r'at least (three|\d+) new or modified component nodes.*except for tests-only.*at least (one|\d+) scanned node',norms['PHASE-403']['body'])
    if not visual:
        raise ValueError(refusal('load_contract','CONTRACT_SEMANTICS:PHASE-403'))
    numbers={'three':3,'one':1}
    visual_threshold=numbers.get(visual.group(1),int(visual.group(1)) if visual.group(1).isdigit() else None)
    visual_minimum_scanned=numbers.get(visual.group(2),int(visual.group(2)) if visual.group(2).isdigit() else None)
    if not re.search(r'When Doxygen is applicable, Code SUCCESS also requires a `doxygen` build record',norms['RETURN-501']['body']):
        raise ValueError(refusal('load_contract','CONTRACT_SEMANTICS:RETURN-501'))
    scans = re.findall(r'`([a-z][a-z-]+)`', norms['RETURN-603']['body'].split('Every entry', 1)[0])
    scans = [name for name in scans if name != 'scans']
    gate = read_subject(root / 'process/gates.md')['norms']['GATE-1209']
    bounds = re.search(r'range-check extra iterations in (\d+)\.\.(\d+), default (\d+), and extra cost ceiling in USD (\d+)\.\.(\d+), default (\d+)', gate['body'])
    if gate['level'] != 'MUST' or not bounds:
        raise ValueError(refusal('load_contract', 'CONTRACT_GRANT_UNSUPPORTED'))
    grant_bounds = tuple(int(value) for value in bounds.groups())
    trace('load_contract', 'VALIDATED', 9, 'selected=%d cap=%d transitions=%d' % (len(selected), default_cap, len(transitions)))
    return {'root': root, 'subjects': subjects, 'norms': norms, 'selected': selected, 'default_cap': default_cap,
            'common_fields': common, 'bug_fields': bug_fields, 'transitions': transitions, 'role_fields': required, 'scans': scans, 'grant_bounds': grant_bounds,'status_fields':status_fields,'valid_statuses':{phase:(('FIXED','BLOCKED') if phase=='Debug' else ('SUCCESS','BLOCKED','ESCALATED_FINALIZE') if phase=='Finalize' else ('SUCCESS','BLOCKED') if phase in ('Bootstrap','Architect') else ('SUCCESS','BUG_REPORT','BLOCKED')) for phase in required},'actors':{'Bootstrap':'searcher','Architect':'architect','Code':'coder','QA':'qa','Review':'reviewer','Debug':'debugger','Finalize':'finalizer'},'visual_threshold':visual_threshold,'visual_minimum_scanned':visual_minimum_scanned}
# endregion FUNC_load_contract


# region FUNC_artifact_error [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Validate a required artifact against the granted root and its declared content hash.
## @io Semantic bundle and path/reference -> refusal code or None
## @complexity 7
def artifact_error(bundle, value, require_hash=False, allow_directory=False):
    # BUG_FIX_CONTEXT: An envelope's readable FORMAT artifact did not validate separately required role paths or hashes.
    trace('artifact_error','CHECK',7,'checking declared artifact')
    reference = {'path':value} if isinstance(value,str) else value
    if not isinstance(reference,dict) or not isinstance(reference.get('path'),str) or not reference['path'].strip():
        return refusal('artifact_error','RETURN_ARTIFACT_MALFORMED')
    try:
        path = (bundle['root']/reference['path']).resolve()
    except (OSError,ValueError):
        return refusal('artifact_error','RETURN_ARTIFACT_MALFORMED')
    if bundle['root'] not in path.parents or not (path.is_file() or allow_directory and path.is_dir()):
        return refusal('artifact_error','RETURN_ARTIFACT_MISSING')
    if 'sha256' in reference or require_hash:
        digest=reference.get('sha256')
        if not isinstance(digest,str) or not re.fullmatch(r'[0-9a-f]{64}',digest) or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
            return refusal('artifact_error','RETURN_ARTIFACT_HASH')
    trace('artifact_error','VALIDATED',9,'artifact containment and declared hash verified')
    return None
# endregion FUNC_artifact_error


# region FUNC_evidence_error [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Validate every supported evidence reference before role continuation.
## @io Semantic bundle and reference list -> refusal code or None
## @complexity 7
def evidence_error(bundle, value, require_hash=False):
    trace('evidence_error','CHECK',7,'checking declared evidence collection')
    if not isinstance(value,list) or not value:
        return refusal('evidence_error','RETURN_EVIDENCE_REQUIRED')
    for reference in value:
        error=artifact_error(bundle,reference,require_hash=require_hash)
        if error:
            return refusal('evidence_error','RETURN_EVIDENCE_HASH' if error=='RETURN_ARTIFACT_HASH' else error)
    trace('evidence_error','VALIDATED',9,'references=%d'%len(value))
    return None
# endregion FUNC_evidence_error


# region FUNC_visual_error [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Check measured activation counts and nonempty canonical scan output.
## @io Semantic bundle and visual result -> refusal code or None
## @complexity 7
def visual_error(bundle, visual):
    # BUG_FIX_CONTEXT: Status/reason alone waived the actual threshold and zero scanned nodes still passed.
    trace('visual_error','CHECK',9,'checking actual visual activation and output predicates')
    if not isinstance(visual,dict) or type(visual.get('componentNodes')) is not int or visual['componentNodes']<0 or type(visual.get('testsOnly')) is not bool:
        return refusal('visual_error','RETURN_VISUAL_REQUIRED')
    applies=visual['componentNodes']>=bundle['visual_threshold'] and not visual['testsOnly']
    status=visual.get('status')
    if applies and status!='PASS':
        return refusal('visual_error','RETURN_VISUAL_REQUIRED')
    if status=='PASS':
        observed=re.search(r'(?:^|\n)scannedNodes=(\d+)(?:\n|$)',visual.get('output','')) if isinstance(visual.get('output'),str) else None
        if not observed or int(observed.group(1))!=visual.get('scannedNodes') or not isinstance(visual.get('command'),str) or not visual['command'].strip() or type(visual.get('exitCode')) is not int or visual['exitCode']!=0 or not isinstance(visual.get('output'),str) or not visual['output'].strip() or type(visual.get('scannedNodes')) is not int or visual['scannedNodes']<bundle['visual_minimum_scanned'] or evidence_error(bundle,visual.get('evidence')):
            return refusal('visual_error','RETURN_VISUAL_REQUIRED')
    elif status not in ('NOT_APPLICABLE','SKIPPED') or applies or not isinstance(visual.get('reason'),str) or not visual['reason'].strip() or not isinstance(visual.get('activation'),str) or not visual['activation'].strip():
        return refusal('visual_error','RETURN_VISUAL_REQUIRED')
    trace('visual_error','VALIDATED',9,'mechanical activation=%s'%applies)
    return None
# endregion FUNC_visual_error


# region FUNC_activation_error [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Require assigned role and protocol read receipts before a phase action.
## @io Semantic bundle, receipt, phase and current facts -> refusal code or None
## @complexity 7
def activation_error(bundle, receipt, phase, facts):
    # BUG_FIX_CONTEXT: An optional activate event never guarded continuation when omitted.
    trace('activation_error','CHECK',7,'checking assigned phase receipt')
    if not isinstance(phase,str):
        return refusal('activation_error','ACTIVATION_MISSING')
    if not isinstance(receipt,dict) or receipt.get('phase')!=phase or receipt.get('role')!=bundle['actors'].get(phase) or receipt.get('inputIdentity')!=facts.get('inputIdentity') or receipt.get('candidateIdentity')!=facts.get('candidateIdentity') or receipt.get('runId')!=facts.get('runId'):
        return refusal('activation_error','ACTIVATION_MISSING')
    role_path=receipt.get('rolePath');protocols=receipt.get('protocolPaths');reads=receipt.get('readEvidence')
    if not isinstance(role_path,str) or not isinstance(protocols,list) or not protocols or any(not isinstance(path,str) for path in protocols) or evidence_error(bundle,reads,require_hash=True):
        return refusal('activation_error','ACTIVATION_MISSING')
    expected=facts.get('assigned_protocol_paths',{}).get(phase)
    if not isinstance(expected,list) or not expected or any(not isinstance(path,str) for path in expected) or not set(expected).issubset(protocols):
        return refusal('activation_error','ACTIVATION_MISSING')
    observed={item.get('path') for item in reads if isinstance(item,dict)}
    if not {role_path,*protocols}.issubset(observed) or role_path!=facts.get('assigned_role_paths',{}).get(phase):
        return refusal('activation_error','ACTIVATION_MISSING')
    trace('activation_error','VALIDATED',9,'assigned role and protocol read receipts verified')
    return None
# endregion FUNC_activation_error


# region FUNC_payload_error [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Check supported typed role/status conditions and separately required artifacts.
## @io Semantic bundle, role payload and current facts -> refusal code or None
## @complexity 7
def payload_error(bundle,value,facts):
    # BUG_FIX_CONTEXT: Presence-only required fields accepted null diagnostics, malformed collections and absent paths.
    phase,status=value['phase'],value['status']
    text=lambda item:isinstance(item,str) and bool(item.strip())
    strings=lambda item:isinstance(item,list) and all(text(member) for member in item)
    fieldsets=bundle['status_fields'].get((phase,status),[])
    if phase=='Finalize' and status=='SUCCESS' and facts.get('doxygen_required') is False:
        fieldsets=[field for field in fieldsets if field!='doxygenPath']
    if not fieldsets or any(field not in value for field in fieldsets):
        return refusal('payload_error','RETURN_ROLE_FIELD_REQUIRED')
    if status=='BLOCKED' and (not text(value.get('reason')) or not strings(value.get('limitations'))):
        return refusal('payload_error','RETURN_BLOCKED_REASON_REQUIRED')
    if status=='BUG_REPORT':
        bug=value.get('bugReport')
        if not isinstance(bug,dict) or any(not text(bug.get(field)) for field in bundle['bug_fields'] if field!='bugReport'):
            return refusal('payload_error','RETURN_BUG_REPORT_REQUIRED')
    if phase=='Bootstrap' and status=='SUCCESS':
        files=value.get('files')
        if type(value.get('isEmpty')) is not bool or value.get('classificationHint') not in ('GREENFIELD','BROWNFIELD') or type(value.get('fileCount')) is not int or value['fileCount']<0 or not isinstance(files,list) or len(files)!=value['fileCount'] or not strings(value.get('recommendations')):
            return refusal('payload_error','RETURN_BOOTSTRAP_INVALID')
        for item in files:
            if not isinstance(item,dict) or any(not text(item.get(field)) for field in ('path','summary','structure','relevance')) or artifact_error(bundle,item['path']):
                return refusal('payload_error','RETURN_BOOTSTRAP_INVALID')
    if phase=='Architect' and status=='SUCCESS':
        if any(not text(value.get(field)) for field in ('classification','projectType','taskType')) or any(not strings(value.get(field)) for field in ('mayEdit','doNotTouch')) or not isinstance(value.get('specDeficiencies'),list) or type(value.get('specBlocked')) is not bool:
            return refusal('payload_error','RETURN_ARCHITECT_INVALID')
        slices=value.get('featureSlices');criteria=value.get('acceptanceCriteria')
        if not isinstance(slices,list) or not slices or not isinstance(criteria,list) or not criteria:
            return refusal('payload_error','RETURN_ARCHITECT_INVALID')
        for item in slices:
            if not isinstance(item,dict) or not text(item.get('id')) or not text(item.get('description')) or not strings(item.get('files')) or not item['files'] or type(item.get('uiApplicable')) is not bool:
                return refusal('payload_error','RETURN_ARCHITECT_INVALID')
            if any(artifact_error(bundle,path) for path in item['files']):
                return refusal('payload_error','RETURN_ARCHITECT_INVALID')
        for item in criteria:
            if not isinstance(item,dict) or not text(item.get('id')) or not text(item.get('text')) or type(item.get('measurable')) is not bool or item['measurable'] and (type(item.get('threshold')) not in (int,float,str) or isinstance(item['threshold'],str) and not item['threshold'].strip()):
                return refusal('payload_error','RETURN_ARCHITECT_INVALID')
        if value['specBlocked']:
            return refusal('payload_error','RETURN_PLAN_BLOCKED')
        if value.get('planPath')!=facts.get('dictated_plan_path') or artifact_error(bundle,value.get('planPath')):
            return refusal('payload_error','RETURN_PLAN_PATH')
        if visual_error(bundle,value.get('visualGate')):
            return refusal('payload_error','RETURN_VISUAL_REQUIRED')
    if phase=='Code' and status=='SUCCESS':
        artifacts=value.get('artifacts')
        if not isinstance(artifacts,list) or not artifacts or not text(value.get('testSummary')) or not strings(value.get('deviations')) or any(artifact_error(bundle,item) for item in artifacts) or artifact_error(bundle,value.get('testGuidePath')):
            return refusal('payload_error','RETURN_CODE_PAYLOAD_INVALID')
        build=value.get('doxygen')
        if type(facts.get('doxygen_required')) is not bool or not isinstance(build,dict) or type(build.get('applicable')) is not bool or build['applicable']!=facts['doxygen_required']:
            return refusal('payload_error','RETURN_DOXYGEN_REQUIRED')
        if build['applicable']:
            if facts.get('doxygen_final_check_verified') is not True or evidence_error(bundle,build.get('fileChecks'),require_hash=True) or any(not text(build.get(field)) for field in ('command','output')) or type(build.get('exitCode')) is not int or build['exitCode']!=0 or build.get('candidateIdentity')!=facts.get('candidateIdentity') or build.get('inputIdentity')!=facts.get('inputIdentity') or evidence_error(bundle,build.get('evidence'),require_hash=True) or artifact_error(bundle,build.get('mapPath'),require_hash=True):
                return refusal('payload_error','RETURN_DOXYGEN_REQUIRED')
        elif not text(build.get('reason')) or evidence_error(bundle,build.get('evidence')):
            return refusal('payload_error','RETURN_DOXYGEN_REQUIRED')
    if phase in ('QA','Review'):
        if not isinstance(value.get('findings'),list) or not strings(value.get('limitations')):
            return refusal('payload_error','RETURN_JUDGMENT_INVALID')
        for finding in value['findings']:
            if not isinstance(finding,dict) or any(not text(finding.get(field)) for field in ('code','severity','message')) or phase=='QA' and not text(finding.get('scan')):
                return refusal('payload_error','RETURN_JUDGMENT_INVALID')
        if phase=='QA':
            scans=value.get('scans')
            if not text(value.get('testSummary')) or not isinstance(scans,list) or len(scans)!=len(bundle['scans']) or any(not isinstance(scan,dict) or not text(scan.get('id')) for scan in scans) or {scan['id'] for scan in scans}!=set(bundle['scans']):
                return refusal('payload_error','RETURN_SCAN_REQUIRED')
            valid=('PASS','N/A') if status=='SUCCESS' else ('PASS','FAIL','N/A','BLOCKED')
            for scan in scans:
                if scan.get('status') not in valid or not text(scan.get('reason')) or evidence_error(bundle,scan.get('evidence')):
                    return refusal('payload_error','RETURN_SCAN_EVIDENCE')
    if phase=='Debug':
        if not text(value.get('rootCause')) or status=='FIXED' and (not text(value.get('fix')) or not text(value.get('postFixAudit')) or not text(value.get('testSummary')) or not strings(value.get('filesTouched')) or not value['filesTouched'] or any(artifact_error(bundle,path) for path in value['filesTouched'])):
            return refusal('payload_error','RETURN_DEBUG_INVALID')
    if phase=='Finalize' and status=='SUCCESS':
        for field in ('report','planPath','testsPath','logPath','doxygenPath'):
            if field not in value and field=='doxygenPath' and facts.get('doxygen_required') is False:
                continue
            if artifact_error(bundle,value.get(field),allow_directory=field in ('testsPath','doxygenPath')):
                return refusal('payload_error','RETURN_FINALIZE_INVALID')
        if not text(value.get('classification')) or not text(value.get('testSummary')) or any(not strings(value.get(field)) for field in ('scopeDeviations','limitations')) or any(evidence_error(bundle,value.get(field)) for field in ('acceptanceEvidence','qaEvidence','reviewEvidence','liveEvidence')):
            return refusal('payload_error','RETURN_FINALIZE_INVALID')
        radius=value.get('blastRadius')
        if not isinstance(radius,dict) or any(not strings(radius.get(field)) for field in ('added','modified','deleted','untracked')):
            return refusal('payload_error','RETURN_FINALIZE_INVALID')
    if phase=='Finalize' and status=='ESCALATED_FINALIZE' and (not text(value.get('requiredRepair')) or not text(value.get('reason')) or not strings(value.get('limitations'))):
        return refusal('payload_error','RETURN_FINALIZE_INVALID')
    trace('payload_error','VALIDATED',9,'phase=%s status=%s'%(phase,status))
    return None
# endregion FUNC_payload_error


# region FUNC_validate_return [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Refuse malformed, stale or unsupported role evidence before continuation.
## @io Semantic bundle, role value and current declared facts -> refusal code or None
## @complexity 7
def validate_return(bundle, value, facts):
    trace('validate_return', 'START', 7, 'return evidence validation')
    if not isinstance(value, dict):
        return refusal('validate_return', 'RETURN_MALFORMED')
    missing = [name for name in bundle['common_fields'] if name not in value]
    if missing:
        trace('validate_return', 'REFUSAL', 10, 'missing=%d' % len(missing))
        return refusal('validate_return', 'RETURN_REQUIRED_FIELD')
    if any(not isinstance(value[name],str) or not value[name].strip() for name in bundle['common_fields'] if name != 'evidence'):
        return refusal('validate_return','RETURN_MALFORMED')
    role_fields = set(field for fields in bundle['role_fields'].values() for field in fields)
    conditional_fields = {'bugReport','reason','limitations','blockReason','detectedUi','requiredRepair','visualGate','doxygen'}
    extensions = facts.get('declared_return_extensions', {})
    if not isinstance(extensions, dict) or any(not isinstance(declaration, dict) or not all(declaration.get(field) for field in ('type','meaning','producer','consumer','required_conditions','version')) for declaration in extensions.values()):
        return refusal('validate_return', 'RETURN_EXTENSION_UNDECLARED')
    allowed = set(bundle['common_fields']) | role_fields | conditional_fields | set(extensions)
    if set(value) - allowed:
        return refusal('validate_return', 'RETURN_UNKNOWN_FIELD')
    declared_types = {'string':str,'integer':int,'boolean':bool,'array':list,'object':dict}
    for field,declaration in extensions.items():
        if not isinstance(declaration['type'],str) or declaration['type'] not in declared_types or (field in value and type(value[field]) is not declared_types[declaration['type']]):
            return refusal('validate_return','RETURN_EXTENSION_TYPE')
    if value['candidateIdentity'] != facts['candidateIdentity'] or value['inputIdentity'] != facts['inputIdentity']:
        return refusal('validate_return', 'RETURN_STALE_IDENTITY')
    if value['runId'] != facts.get('runId', 'example-run') or value['contractVersion'] != '0.3.0':
        return refusal('validate_return', 'RETURN_STALE_CONTRACT')
    if not isinstance(value['summary'], str) or not value['summary'].strip():
        return refusal('validate_return', 'RETURN_MALFORMED')
    if value['status'] not in ('SUCCESS', 'FIXED', 'BUG_REPORT', 'BLOCKED', 'ESCALATED_FINALIZE'):
        return refusal('validate_return', 'RETURN_UNKNOWN_STATUS')
    if value['phase'] != facts.get('phase') or value['role'] != facts.get('role', facts.get('phase', '').lower()):
        return refusal('validate_return', 'RETURN_WRONG_ACTOR')
    valid_statuses = bundle['valid_statuses'].get(value['phase'], ())
    if value['status'] not in valid_statuses:
        return refusal('validate_return','RETURN_STATUS_PHASE_MISMATCH')
    error = payload_error(bundle,value,facts)
    if error:
        return refusal('validate_return',error)
    error = evidence_error(bundle,value.get('evidence'),require_hash=True)
    if error:
        return refusal('validate_return',error)
    trace('validate_return','VALIDATED',9,'phase=%s status=%s'%(value['phase'],value['status']))
    return None
# endregion FUNC_validate_return


# region FUNC_evaluate_case [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Interpret finite supplied events under the extracted obligations without dispatch or persistence.
## @io Semantic bundle and finite case -> decision dictionary with phase, spend, retries, freshness and refusal
## @complexity 7
def evaluate_case(bundle, case):
    facts = dict(case.get('facts', {}))
    phase = facts.get('phase', 'Bootstrap')
    spent = facts.get('repair_spent', 0)
    retries = dict(facts.get('retries', {kind: 0 for kind in ('response', 'parse', 'transport', 'test')}))
    result = {'case_id': case['case_id'], 'decision': 'ALLOW', 'next_phase': phase, 'repair_spent': spent,
              'retries': retries, 'fresh': True, 'refusal': None, 'norms': []}
    # BUG_FIX_CONTEXT: Negative and boolean initial spend admitted a fifth free entry.
    if type(spent) is not int or spent<0:
        result.update(decision='REFUSE',refusal='SPEND_INVALID',norms=['STATE-201','STATE-303'])
        trace('evaluate_case','REFUSAL',10,'code=SPEND_INVALID')
        return result
    if facts.get('terminal_status'):
        result.update(decision='REFUSE',refusal='TERMINAL_RESTART',norms=['STATE-701'])
        trace('evaluate_case','REFUSAL',10,'code=TERMINAL_RESTART')
        return result
    cap = case.get('adapter_cap', bundle['default_cap'])
    grant = case.get('owner_grant', 0)
    grant_record = case.get('grant_evidence')
    grant_valid = 'owner_grant' not in case
    if 'owner_grant' in case:
        low,high,default,cost_low,cost_high,cost_default = bundle['grant_bounds']
        grant_valid = (type(grant) is int and low <= grant <= high and isinstance(grant_record,dict)
                       and facts.get('owner_authority_verified') is True
                       and grant_record.get('scope') == facts.get('candidateIdentity')
                       and grant_record.get('inputIdentity') == facts.get('inputIdentity')
                       and grant_record.get('additional') == grant and grant_record.get('reason')
                       and type(grant_record.get('extra_cost_usd')) in (int,float)
                       and cost_low <= grant_record['extra_cost_usd'] <= cost_high)
        if grant_valid:
            proof = dict(grant_record)
            paths = proof.get('evidence')
            grant_valid = isinstance(paths,list) and bool(paths)
            for item in paths if grant_valid else []:
                if not isinstance(item,dict) or not isinstance(item.get('path'),str):
                    grant_valid = False
                    break
                path = (bundle['root']/item.get('path','')).resolve()
                if bundle['root'] not in path.parents or not path.is_file() or item.get('sha256') != hashlib.sha256(path.read_bytes()).hexdigest():
                    grant_valid = False
    if type(cap) is not int or cap < 0 or cap > bundle['default_cap'] or not grant_valid:
        result.update(decision='REFUSE', refusal='CAP_INVALID', norms=['STATE-302'])
        trace('evaluate_case','REFUSAL',10,'code=CAP_INVALID')
        return result
    qa_verified = facts.get('qa_verified') is True
    review_verified = facts.get('review_verified') is True
    activations=dict(facts.get('activationEvidence',{}))
    for event in case.get('events', []):
        kind = event['kind']
        refusal, norm = None, None
        trace('evaluate_case', 'EVENT', 9, 'case=%s event=%s spent=%d' % (case['case_id'], kind, result['repair_spent']))
        action_phase = 'Debug' if kind in ('enter-debug','debug-success','debug-failed') else 'Code' if kind=='ui-fix' else result['next_phase']
        if kind in ('return','visual','enter-debug','debug-success','debug-failed','ui-fix','finalize','extension','e2e'):
            error=activation_error(bundle,activations.get(action_phase),action_phase,facts)
            if error:
                result.update(decision='REFUSE',refusal=error,norms=['PHASE-201'])
                break
        if kind == 'enter-debug':
            norm = 'STATE-303'
            if result['repair_spent'] >= cap + grant:
                refusal = 'DEBUG_EXHAUSTED'
            else:
                result['repair_spent'] += 1 if bundle['selected']['STATE-303']['timing'] == 'before' else 0
                result['next_phase'] = 'Debug'
                result['fresh'] = False
        elif kind in ('debug-success', 'ui-fix'):
            qa_verified, review_verified = False, False
            result.update(next_phase='QA' if bundle['selected']['PHASE-605']['renew'] == 'renew full independent QA' else 'Finalize', fresh=False)
            norm = 'PHASE-605'
        elif kind == 'debug-failed':
            result.update(decision='BLOCKED', next_phase='Debug', fresh=False)
            norm = 'STATE-304'
        elif kind == 'retry':
            norm = 'STATE-401'
            retry_kind = event.get('counter')
            if retry_kind not in retries or type(event.get('bound')) is not int or event['bound'] < 0:
                refusal = 'RETRY_INVALID'
            elif event.get('unknown_side_effects'):
                refusal = 'UNKNOWN_SIDE_EFFECTS'
            elif retries[retry_kind] >= min(event['bound'], 1 if retry_kind == 'response' else event['bound']):
                refusal = 'RETRY_EXHAUSTED'
            else:
                retries[retry_kind] += 1
        elif kind == 'activate':
            norm='PHASE-201'
            receipt=event.get('receipt')
            phase=event.get('phase',result['next_phase'])
            refusal=activation_error(bundle,receipt,phase,facts)
            if not refusal:
                activations[phase]=receipt
        elif kind == 'visual':
            norm='PHASE-403'
            refusal='VISUAL_EVIDENCE_MISSING' if visual_error(bundle,event.get('value',event)) else None
        elif kind == 'change':
            norm = 'STATE-501'
            qa_verified, review_verified = False, False
            result.update(next_phase='QA', fresh=False)
            if event.get('input') in ('spec', 'plan', 'rules') and not event.get('approval_reconciled'):
                refusal = 'APPROVAL_RECONCILIATION_REQUIRED'
        elif kind == 'recover':
            norm = 'STATE-601'
            if event.get('terminal'):
                refusal = 'TERMINAL_RESTART'
            elif event.get('unknown_side_effects'):
                refusal = 'UNKNOWN_SIDE_EFFECTS'
            elif not all(event.get(field) for field in ('ledger_complete', 'identities_match', 'artifacts_verified', 'authority_verified')):
                refusal = 'RECOVERY_INVALID'
            elif 'counter_override' in event:
                refusal = 'RECOVERY_COUNTER_INJECTION'
        elif kind == 'finalize':
            norm = 'FINAL-401'
            if event.get('source_repair'):
                result.update(decision='ESCALATE', next_phase='Owner', fresh=False, refusal=bundle['selected']['FINAL-401']['outcome'])
            elif not result['fresh'] or not event.get('same_candidate') or not qa_verified or not review_verified:
                refusal = 'FINALIZE_STALE'
            elif event.get('output_regeneration') and not event.get('declared_output'):
                refusal = 'FINALIZE_UNDECLARED_OUTPUT'
            else:
                result.update(next_phase='ResultGate', decision='WAIT_OWNER')
        elif kind == 'extension':
            norm = 'PHASE-801'
            if not all(event.get(field) for field in ('declared', 'evidence_equivalent', 'permissions_equivalent', 'independence_preserved', 'failure_route','producer','consumer','activation')):
                refusal = 'EXTENSION_INVALID'
        elif kind == 'e2e':
            norm = 'PHASE-804'
            if event.get('required_ac') and (event.get('flaky', 0) or event.get('failed', 0)):
                refusal = 'E2E_REQUIRED_AC_UNSATISFIED'
        elif kind == 'return':
            facts.update(phase=result['next_phase'], role={'Bootstrap': 'searcher', 'Architect': 'architect', 'Code': 'coder', 'QA': 'qa', 'Review': 'reviewer', 'Debug': 'debugger','Finalize':'finalizer'}.get(result['next_phase'], result['next_phase'].lower()))
            value = event.get('value')
            refusal = validate_return(bundle, value, facts)
            norm = 'RETURN-101'
            if not refusal:
                transition = bundle['transitions'].get((value['phase'], value['status']))
                if transition:
                    result['next_phase'], norm = transition
                    if value['phase']=='Debug':
                        result['fresh']=False
                        qa_verified,review_verified=False,False
                        result['decision']='ALLOW'
                    elif value['phase'] == 'QA':
                        result['fresh'] = True
                        qa_verified = True
                        result['repair_spent'] += 0 if bundle['selected']['STATE-303']['qa_charge'] == 'no' else 1
                    elif value['phase'] == 'Review':
                        review_verified = True
                elif value['status'] == 'BUG_REPORT':
                    result.update(next_phase='DebugPending', decision='REPAIR_REQUIRED')
                elif value['phase']=='Finalize' and value['status']=='ESCALATED_FINALIZE':
                    result.update(decision='ESCALATE',next_phase='Owner',fresh=False,refusal='ESCALATED_FINALIZE')
                elif value['phase']=='Finalize' and value['status']=='SUCCESS':
                    if not qa_verified or not review_verified or not result['fresh']:
                        refusal='FINALIZE_STALE'
                    else:
                        result.update(decision='WAIT_OWNER',next_phase='ResultGate')
                elif value['status'] == 'BLOCKED':
                    result['decision'] = 'BLOCKED'
                else:
                    refusal = 'TRANSITION_UNSUPPORTED'
        else:
            refusal = 'EVENT_UNSUPPORTED'
        if norm and norm not in result['norms']:
            result['norms'].append(norm)
        if refusal:
            result.update(decision='REFUSE', refusal=refusal)
            trace('evaluate_case', 'REFUSAL', 10, 'code=' + refusal)
            break
        if result['decision'] in ('BLOCKED','ESCALATE','WAIT_OWNER'):
            trace('evaluate_case','TERMINAL',9,'event stream stopped decision='+result['decision'])
            break
    trace('evaluate_case', 'RESULT', 9, 'case=%s decision=%s spent=%d' % (case['case_id'], result['decision'], result['repair_spent']))
    return result
# endregion FUNC_evaluate_case


# region FUNC_run_cases [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Compare actual decisions against independently authored finite expectations.
## @io Semantic bundle and cases -> JSON-ready agreement report and contract hashes
## @complexity 7
def run_cases(bundle, cases):
    outcomes = []
    for case in cases:
        result = evaluate_case(bundle, case)
        result['matches_expected'] = all(result.get(key) == value for key, value in case['expected'].items())
        outcomes.append(result)
    trace('run_cases', 'RESULT', 9, 'cases=%d matched=%d' % (len(outcomes), sum(row['matches_expected'] for row in outcomes)))
    return {'ok': all(row['matches_expected'] for row in outcomes), 'cases': outcomes,
            'contract_hashes': {path: subject['sha256'] for path, subject in bundle['subjects'].items()}}
# endregion FUNC_run_cases


# region FUNC_case_input_valid [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Classify malformed supported case data before reading the contract.
## @io Decoded case list -> boolean validity
## @complexity 7
def case_input_valid(cases):
    # BUG_FIX_CONTEXT: Malformed nested events reached interpretation and were mislabeled as contract exit one.
    trace('case_input_valid','CHECK',7,'checking finite case input shapes')
    if not isinstance(cases,list):
        return not refusal('case_input_valid','CASE_INPUT_INVALID')
    for case in cases:
        if not isinstance(case,dict) or not isinstance(case.get('case_id'),str) or not case['case_id'].strip() or not isinstance(case.get('expected'),dict) or not isinstance(case.get('facts',{}),dict) or not isinstance(case.get('events',[]),list):
            return not refusal('case_input_valid','CASE_INPUT_INVALID')
        facts=case.get('facts',{})
        if any(field in facts and not isinstance(facts[field],dict) for field in ('activationEvidence','assigned_role_paths','assigned_protocol_paths','retries','declared_return_extensions')):
            return not refusal('case_input_valid','CASE_INPUT_INVALID')
        if 'phase' in facts and not isinstance(facts['phase'],str) or any(type(value) is not int or value<0 for value in facts.get('retries',{}).values()):
            return not refusal('case_input_valid','CASE_INPUT_INVALID')
        for event in case.get('events',[]):
            if not isinstance(event,dict) or not isinstance(event.get('kind'),str) or not event['kind'].strip() or 'phase' in event and not isinstance(event['phase'],str) or 'counter' in event and not isinstance(event['counter'],str):
                return not refusal('case_input_valid','CASE_INPUT_INVALID')
    trace('case_input_valid','VALIDATED',9,'cases=%d'%len(cases))
    return True
# endregion FUNC_case_input_valid


# region FUNC_main [DOMAIN(9): DevelopmentFlow; CONCEPT(8): Evidence; TECH(5): Python]
## @purpose Deliver the real example report and trajectory with a bounded process exit.
## @io Argument list or process arguments -> integer exit code 0, 1 or 2
## @complexity 7
def main(argv=None):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    parser = argparse.ArgumentParser(description='Bounded example consumer of selected development-flow clauses.')
    parser.add_argument('--root', required=True, type=pathlib.Path)
    parser.add_argument('--cases', required=True, type=pathlib.Path)
    args = parser.parse_args(argv)
    try:
        trace('main', 'READ_CASES', 7, 'reading case input')
        cases = json.loads(args.cases.read_text(encoding='utf-8'))
        if not case_input_valid(cases):
            raise ValueError('CASE_INPUT_INVALID')
    except (OSError, ValueError, TypeError) as error:
        trace('main', 'REFUSAL', 10, 'invalid case input')
        print(json.dumps({'ok': False, 'refusal': 'CASE_INPUT_INVALID'}))
        return 2
    try:
        bundle = load_contract(args.root)
        report = run_cases(bundle, cases)
    except (OSError, ValueError, KeyError, TypeError) as error:
        trace('main', 'REFUSAL', 10, 'contract or case cannot be evaluated')
        code = str(error) if isinstance(error, ValueError) else 'CONTRACT_OR_CASE_INVALID'
        print(json.dumps({'ok': False, 'refusal': code}))
        return 1
    print(json.dumps(report, sort_keys=True))
    trace('main', 'EXIT', 9, 'exit=%d' % (0 if report['ok'] else 1))
    return 0 if report['ok'] else 1
# endregion FUNC_main


if __name__ == '__main__':
    sys.exit(main())
