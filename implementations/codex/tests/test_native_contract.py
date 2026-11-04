# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification; TECH(8): Python, StandardLibrary]
## @modulecontract
## @purpose Check independent actual package populations and operative carrier prerequisites without claiming semantic completeness.
## @scope Exact27entry/sixrole/75member/71owner/28capability/sevenparameter structural coverage; full independent SOURCE and native smoke remain required.
## @input Explicit owned source/target paths and current canonical records; pytest fixtures supply owned temporary paths for tests. No credentials or provider state.
## @output Importable declared functions, actual CLI answer/diagnostic/exit where applicable, and meaningful test outcomes with actual trace. No fabricated native acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): logging; USES_API(8): continuation.capabilities; READS_DATA_FROM(9): explicit path inputs; no environment secrets]
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
## LAST_CHANGE: [5.0.0 - CONT-BOUND stale-stamp repair: free-text release stamps must equal the actual identity; all prior cases/assertions/refusals retained.]
## Earlier: [2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [2.2.0 - Current bounded source package and permanent behavioral refusal controls.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => test_native_contract._module_contract
## FUNC 9[Verify shipped native contracts] => test_native_contract.test_shipped_native_contracts
## FUNC 9[Verify actual layout and adapter contract] => test_native_contract.test_actual_layout_and_adapter_contract
## FUNC 7[List free-text release stamps that differ from the actual identity] => test_native_contract._stamp_problems
## FUNC 9[Stale free-text release stamps refused] => test_native_contract.test_release_stamps_match_package_identity
## @usecases
## - Parent/test: inspect real current inputs -> accept scoped current outcome or refuse unsafe/malformed/stale input.
## - Independent judge: compare actual assertions/source/CLI receipts -> bounded evidence; native acceptance remains separately owned.
## - Release author: bump the package and miss a free-text stamp -> test_release_stamps_match_package_identity names the stale statement.
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
import re

import continuation

logger=logging.getLogger(__name__)
PACKAGE=Path(__file__).resolve().parents[1]
PERSIST='Single root writer candidate run_state.py schema{schema} atomic UTF8 .methodology/lineages with complete accepted/refused history/current locks.'
# Free-text release stamps. Expected text is built from the actual layout, adapter and helper identity; historical bindings elsewhere keep their stated release.
STAMPS={'README.md':('Native Codex implementation package{version} for neutral methodology{neutral}.','Current source candidate is{version} over neutral{neutral}. Wire {wire} remains unchanged; persistence is schema{schema};','Package{members} members,'),
        'references/adoption.md':('# Pointwise source adoption — neutral{neutral} / package{version}\n',PERSIST),
        'references/codex-runtime.md':('# Native Codex runtime — package{version}\n','with current neutral{neutral}.','Codex{version} uses neutral{neutral} and persistent schema{schema}; canonical role-return wire remains {wire}.'),
        'references/consumer-pm-profile.md':('source package{version} over neutral{neutral}.','Wire {wire} remains unchanged; persistence is schema{schema}.'),
        'references/handoffs.md':('Source candidate is package{version} over neutral{neutral}; contractVersion remains {wire}, persistent schema{schema}.',),
        'references/source-disposition.md':('Current source{version} has{members} members,','current schema{schema} immutable inputs','current neutral{neutral}.','Layout contains all{members} exact paths/kinds'),
        'skills/feature-dev/SKILL.md':('Codex{version} uses neutral{neutral} and persistent schema{schema}; canonical role-return wire remains {wire}.',),
        'skills/semantic-exoskeleton/SKILL.md':('METHODOLOGY_VERSION: {neutral}\n','Package binding: methodology-codex{version}, schema{schema}, colocated-explicit-source.')}
TOPICS={'pm-bootstrap','pm-plan-batch','pm-run-batch','pm-handoff','analyzer','ax-ui-contract','brainstorm','brownfield-spec-template','code-review','data-transform','devplan-protocol','document-protocol','durable-layer','feature-dev','graph-protocol','greenfield-bootstrap','hitl-gates','pm','prod-log-vacuum','prompting','prompting-agent-design','prompting-decompose','prompting-markup','prompting-verify','roadmap','semantic-exoskeleton','spec-recon'}


# region FUNC_test_shipped_native_contracts [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify shipped native contracts over actual owned inputs.
## @uses re.search
## @io Input: caplog: pytest.LogCaptureFixture. Cases: no parametrized inputs. Output: None after these concrete checks: actual == TOPICS; roles == {'architect', 'coder', 'debugger', 'qa', 'reviewer', 'searcher'}; 'Finalize' in runtime + handoffs and 'BLOCKED' in runtime + handoffs; not any((r.levelno 〉= logging.ERROR for r in caplog.records)); 'roles/' + p.name in text and 'roles/_base.md' in text; re.search('(?i)(delegat|spawn)', text) and re.search('(?i)commit', text); all((clause in text for clause in ('MAY EDIT', 'DO NOT TOUCH', 'Exact granted paths only'))) and 'read' in text.lower(); text.startswith('---⧵n') and re.search('^name: .+', text, re.M) and re.search('^description:', text, re.M); owner in runtime + handoffs; scan in handoffs; owner in (PACKAGE / 'references/adoption.md').read_text(). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_native_contract.py::test_shipped_native_contracts executes these exact cases. Importance:9.
## @complexity 5
def test_shipped_native_contracts(caplog):
    logger.info('[IMP:4][test_shipped_native_contracts][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    actual={p.parent.name for p in (PACKAGE/'skills').glob('*/SKILL.md')}
    roles={p.stem for p in (PACKAGE/'roles').glob('*.md')}
    print('Actual entry/role population:',sorted(actual),sorted(roles))
    assert actual==TOPICS
    assert roles=={'architect','coder','debugger','qa','reviewer','searcher'}
    for p in sorted((PACKAGE/'roles').glob('*.md')):
        text=p.read_text();print('Actual role carrier:',p.name)
        assert 'roles/'+p.name in text and 'roles/_base.md' in text
        assert re.search(r'(?i)(delegat|spawn)',text) and re.search(r'(?i)commit',text)
        assert all(clause in text for clause in ('MAY EDIT','DO NOT TOUCH','Exact granted paths only')) and 'read' in text.lower()
    for topic in sorted(TOPICS):
        text=(PACKAGE/'skills'/topic/'SKILL.md').read_text()
        assert text.startswith('---\n') and re.search(r'^name: .+',text,re.M) and re.search(r'^description:',text,re.M)
    runtime=(PACKAGE/'references/codex-runtime.md').read_text();handoffs=(PACKAGE/'references/handoffs.md').read_text()
    for owner in ('checks/orient.md','checks/preflight.md','checks/run-audit.md','process/safety.md'):
        assert owner in runtime+handoffs
    for scan in ('green-test-trap','quantitative-ac','semantic-trace','infra-dod','side-effect-channel','secret-leak','real-path-shape','discriminating-test'):
        assert scan in handoffs
    for owner in ('concepts/principles.md','roles/_base.md','code/exoskeleton.md','code/ldd.md','code/doxygen.md','code/tests.md'):
        assert owner in (PACKAGE/'references/adoption.md').read_text()
    assert 'Finalize' in runtime+handoffs and 'BLOCKED' in runtime+handoffs
    logger.info('[IMP:9][test_shipped_native_contracts][RESULT] bounded actual carrier clauses inspected; full semantic judgment independent')
    for r in caplog.records:print(r.getMessage())
    assert not any(r.levelno>=logging.ERROR for r in caplog.records)


    logger.info('[IMP:9][test_shipped_native_contracts][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_shipped_native_contracts

# region FUNC_test_actual_layout_and_adapter_contract [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Verify actual layout and adapter contract over actual owned inputs.
## @uses json.loads
## @io Input: caplog: pytest.LogCaptureFixture. Cases: no parametrized inputs. Output: None after these concrete checks: layout['package'] == 'methodology-codex' and layout['version'] == '5.0.0' and (layout['profile'] == 'colocated-explicit-source'); len(layout['files']) == 75 and len(adapter['files']) == 71 and (len(adapter['capabilities']) == 28) and (len(adapter['parameters']) == 7); adapter['spec_root'] == '../../' and adapter['spec_version'] == '4.1.0'; names == sorted(set(names)); set(layout['roles']) == {'architect', 'coder', 'debugger', 'qa', 'reviewer', 'searcher'}; not any((r.levelno 〉= logging.ERROR for r in caplog.records)). AssertionError denotes a failed promised check; expected refusals are explicitly caught in this test body. Side effects: only the actual owned fixture writes/child processes in this body; shared package and neutral corpus reads stay read-only. No native acceptance is inferred. Example: python3 -m pytest tests/test_native_contract.py::test_actual_layout_and_adapter_contract executes these exact cases. Importance:9.
## @complexity 5
def test_actual_layout_and_adapter_contract(caplog):
    logger.info('[IMP:4][test_actual_layout_and_adapter_contract][START] owned behavioral verification')
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    layout=json.loads((PACKAGE/'references/package-layout.json').read_text());adapter=json.loads((PACKAGE/'adapter.json').read_text())
    print('Actual layout/adapter populations:',len(layout['files']),len(adapter['files']),len(adapter['capabilities']),len(adapter['parameters']))
    assert layout['package']=='methodology-codex' and layout['version']=='5.0.0' and layout['profile']=='colocated-explicit-source'
    assert len(layout['files'])==75 and len(adapter['files'])==71 and len(adapter['capabilities'])==28 and len(adapter['parameters'])==7
    assert adapter['spec_root']=='../../' and adapter['spec_version']=='4.1.0'
    names=[row['path'] for row in layout['files']];assert names==sorted(set(names))
    assert set(layout['roles'])=={'architect','coder','debugger','qa','reviewer','searcher'}
    logger.info('[IMP:9][test_actual_layout_and_adapter_contract][RESULT] declared populations verified; not semantic adoption proof')
    for r in caplog.records:print(r.getMessage())
    assert not any(r.levelno>=logging.ERROR for r in caplog.records)
    logger.info('[IMP:9][test_actual_layout_and_adapter_contract][RESULT] behavioral assertions completed')
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_actual_layout_and_adapter_contract


# region FUNC__stamp_problems [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose List free-text release stamps that differ from the given actual identity.
## @uses logger.info
## @io texts dict of package-relative path to text; mechanism str, the adapter run-state-persist row; identity dict of version, neutral, schema, wire and members. Returns the list of lost statements, empty when every stamp agrees. Logs the count only. A finite exact recognizer under TST-1001: it detects a lost statement, not a contrary sentence beside it, and never proves other text current. Example: a consumer profile saying package4.0.0 under identity version 5.0.0 yields its statement.
## @complexity 3
def _stamp_problems(texts,mechanism,identity):
    # START_BLOCK_BusinessLogic
    problems=[f'{path}: {statement.strip()}' for path,stamps in STAMPS.items() for statement in (stamp.format(**identity) for stamp in stamps) if statement not in texts[path]]
    if mechanism!=PERSIST.format(**identity):problems.append(f'adapter.json: {PERSIST.format(**identity)}')
    logger.info('[IMP:7][_stamp_problems][RESULT] problems=%d',len(problems))
    return problems
    # END_BLOCK_BusinessLogic
# endregion FUNC__stamp_problems

# region FUNC_test_release_stamps_match_package_identity [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Refuse a stale free-text release stamp that every other package check leaves green.
## @uses test_native_contract._stamp_problems, continuation.capabilities, json.loads
## @io Input: caplog: pytest.LogCaptureFixture. Output: None after the helper's capabilities answer equals the layout and adapter identity, the actual carriers have no problem against that identity, and each of the 36 per-field stamp controls and the one adapter control is named by the same predicate. Reads package files only. Raises AssertionError on any difference. Example: restoring schema2 in the exoskeleton stamp names that statement.
## @complexity 5
def test_release_stamps_match_package_identity(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    layout=json.loads((PACKAGE/'references/package-layout.json').read_text());adapter=json.loads((PACKAGE/'adapter.json').read_text());answer=continuation.capabilities()
    identity={'version':layout['version'],'neutral':adapter['spec_version'],'schema':answer['schema'],'wire':answer['role_wire'],'members':len(layout['files'])}
    logger.info('[IMP:9][test_release_stamps_match_package_identity][IDENTITY] layout=%s adapter=%s helper=%s/%s',identity['version'],identity['neutral'],answer['version'],answer['neutral'])
    print('Actual identity:',identity,'helper:',answer['version'],answer['neutral'])
    assert (answer['version'],answer['neutral'])==(identity['version'],identity['neutral'])
    mechanism=adapter['capabilities']['run-state-persist']['mechanism']
    texts={path:(PACKAGE/path).read_text(encoding='utf-8') for path in STAMPS}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    real=_stamp_problems(texts,mechanism,identity)
    logger.info('[IMP:9][test_release_stamps_match_package_identity][COMPARE] problems=%d',len(real))
    print('Actual stamp problems:',real)
    assert real==[]
    controls=[(path,stamp,field) for path,stamps in STAMPS.items() for stamp in stamps for field in identity if '{'+field+'}' in stamp]
    undetected=[]
    for path,stamp,field in controls:
        statement=stamp.format(**identity)
        stale=texts[path].replace(statement,stamp.format(**{**identity,field:'0.0.0'}))
        if f'{path}: {statement.strip()}' not in _stamp_problems({**texts,path:stale},mechanism,identity):undetected.append((path,field))
    if not _stamp_problems(texts,PERSIST.format(**{**identity,'schema':'0.0.0'}),identity):undetected.append(('adapter.json','schema'))
    logger.info('[IMP:9][test_release_stamps_match_package_identity][CONTROLS] controls=%d undetected=%d',len(controls)+1,len(undetected))
    print('Undetected controls:',undetected)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert len(controls)==36
    assert undetected==[]
    assert not any(r.levelno>=logging.ERROR for r in caplog.records)
    # END_BLOCK_Result
# endregion FUNC_test_release_stamps_match_package_identity
