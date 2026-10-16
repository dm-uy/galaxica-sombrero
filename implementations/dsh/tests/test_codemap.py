# region MODULE_CONTRACT [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteEvidence, Scope; TECH(7): Python, stdlib]
## @modulecontract
## @purpose Discriminate actual native C2 behavior through direct imports and real CLI/filesystem/map/interpreter boundaries.
## @scope Owned tmp_path fixtures only; source read-only, fixed independent expectations, every expected error owned.
## @input Explicit deterministic literals, actual shipped trusted imports, caplog and owned tmp_path.
## @output Meaningful outcome/order/population/error assertions and visible actual important trace.
## @links [USES_API(9): consumer_files.covered_sources, orient.run_checks, codemap.run, markup_migrate.build_plan; READS_DATA_FROM(8): shipped trusted helpers and seed resources]
## @invariants
## - Expected error profiles retain literal logger, exact numeric level, complete message, order and cardinality.
## - Unavailable required evidence is never converted to an empty clean success.
## - Explicit resources and controlling human scope remain separate from structural recognition.
## - Consumer content is never imported or executed; inherited framework inputs remain read-only.
## @rationale
## Q: Why explicit shared input boundaries?
## A: Complete populations prevent the original source omission and false-clean classes; they also expose unsupported grammar.
## Q: Why keep endpoint receipts separate from captured events?
## A: A log API call cannot prove actual file, process or map delivery.
## @changes
## LAST_CHANGE: [2.2.0 - Retained C2 behavior controls; A2 Debug2 strengthens complete ordered logger/numeric-level/message identity and physical-sink discrimination.]
## @modulemap
## FUNC 9[Reject equal-text foreign/severity substitutions, missing/duplicate/reordered events through the shipped oracle and real flushed sink.] => test_codemap.test_error_oracle_complete_identity
## FUNC 9[Import the explicitly trusted shipped helper directly without modifying sys.path.] => test_codemap.load
## FUNC 9[Expose all actual important records and assert the complete expected-only error population.] => test_codemap.expose
## FUNC 9[Create a complete explicitly synthetic adopted single-layer record fixture with real homes.] => test_codemap.fixture
## FUNC 9[Return all actual native checklist rows keyed by their fixed IDs.] => test_codemap.rows
## FUNC 9[Exercise the real shipped CLI process with complete visible streams and no Python path injection.] => test_codemap.invoke
## FUNC 9[Create a literal owned software fixture in current or original old-markup form.] => test_codemap.source_fixture
## FUNC 9[Construct only a synthetic exact-shape apply record for structural tests, never authentic human consent.] => test_codemap.authority
## FUNC 9[Build the real fixture Doxygen map silently and retain every original command/stream identity.] => test_codemap.build_map
## FUNC 9[Inspect every actual own rich module field and location after silent real Doxygen build.] => test_codemap.test_codemap_own_xml_fields_and_location
## FUNC 9[Keep async/nested call ownership and disclose two actual same-name symbol blocks.] => test_codemap.test_codemap_static_nested_async_alias_ambiguity
## FUNC 9[Distinguish absent-map source fallback, syntax-incomplete relation refusal2 and complete missing1.] => test_codemap.test_codemap_fallbacks_and_unavailable_population
## FUNC 9[Verify actual file five-line/source-second shape and CLI0/1/2 endpoint delivery.] => test_codemap.test_codemap_real_cli_shape
## FUNC 9[Accept a real independently shaped list contract while refusing lost content and foreign own fields.] => test_codemap.test_real_list_contract_and_foreign_fields
## FUNC 9[Resolve only unshadowed own-scope from-import aliases and keep nested/async/control-flow definitions separate.] => test_codemap.test_alias_shadow_class_control_flow_and_nested_ownership
## FUNC 9[Exercise actual current/broken/stale/in-progress map responses without promoting lifecycle or fallback to complete own XML.] => test_codemap.test_current_broken_stale_and_inprogress_real_maps
## FUNC 9[Refuse current-module certification at a wrong actual source line and resolve module-level relative aliases without importing consumer code.] => test_codemap.test_unique_actual_module_anchor_and_relative_alias
## FUNC 9[Write one filled synthetic front-matter record in the fixture owner root.] => test_codemap.record
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY test_codemap, consumer PM, explicit paths, complete population, supported grammar, evidence
## @STRUCTURE ▶ explicit inputs → ◇ validate supported shape → ○ own operations → ⎋ attributable result or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import importlib.util
import json
import logging
import os
import stat
import subprocess
import sys
import hashlib
import datetime
from pathlib import Path
import pytest
import xml.etree.ElementTree as ET

PACKAGE=Path(__file__).resolve().parents[1]
SCRIPTS=PACKAGE/'skills/pm/scripts'
LOGGER=logging.getLogger(__name__)
FLOOR='/usr/bin/python3'
AUTHOR='/opt/homebrew/bin/python3.12'


# region FUNC_load [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Import the explicitly trusted shipped helper directly without modifying sys.path.
## @uses importlib.util.spec_from_file_location, importlib.util.module_from_spec
## @io Input: name one of consumer_files/orient/codemap/markup_migrate str. Output: actual module registered in sys.modules under that name for dataclasses; never a consumer module. Side effects: trusted helper import only. Errors: ImportError/OSError for missing source. Example: load("consumer_files") exposes native parse_front_matter.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def load(name):
    # START_BLOCK_BusinessLogic
    spec=importlib.util.spec_from_file_location(name,SCRIPTS/(name+'.py')); module=importlib.util.module_from_spec(spec); sys.modules[name]=module; spec.loader.exec_module(module); return module
    # END_BLOCK_BusinessLogic
# endregion FUNC_load

cf=load('consumer_files')
orient=load('orient')
codemap=load('codemap')
migrate=load('markup_migrate')


# region FUNC_expose [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Expose all actual important records and assert the complete expected-only error population.
## @uses logging.LogRecord.getMessage
## @io Input: caplog pytest fixture; expected_errors ordered tuple[tuple[str,int,str],...] default empty, each independently literal owning logger name, exact numeric level40 and complete function/block/cause message. Output: None only after exact full event-list equality, including cardinality and order.
##   Side effects: visible important logger/level/message stdout; capture and runtime loggers unchanged. Guarantees: foreign equal-text ERROR, owning CRITICAL/custom41, missing/extra/reordered errors cannot substitute for expected owning ERROR40; no string compatibility conversion.
##   Errors: AssertionError on any identity/population mismatch. Example: (("consumer_files",40,"[IMP:10][scalar][VALIDATION_FAILURE] cause=malformed-quoted-value"),) admits only that actual owning event. Importance9.
## @complexity 7
def expose(caplog,expected_errors=()):
    # START_BLOCK_BusinessLogic
    for record in caplog.records:
        if any('[IMP:%d]'%n in record.getMessage() for n in range(7,11)): print(record.name,record.levelno,record.levelname,record.getMessage())
    errors=[(record.name,record.levelno,record.getMessage()) for record in caplog.records if record.levelno>=40]
    assert errors==list(expected_errors)
    # END_BLOCK_BusinessLogic
# endregion FUNC_expose


# region FUNC_fixture [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Create a complete explicitly synthetic adopted single-layer record fixture with real homes.
## @uses test_codemap.record, pathlib.Path.write_text, json.dumps
## @io Input: root absent owned tmp_path Path. Output: same root Path containing five filled homes, full CONVENTIONS provenance and known-empty Doxyfile src. Side effects: owned fixture directory/files only. Errors: OSError on setup failure; no overwritten preexisting root. Example: fixture(tmp_path/"project") carries proposed T-001 and no product consent.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def fixture(root):
    # START_BLOCK_BusinessLogic
    root.mkdir(); (root/'src').mkdir()
    generated={'by':'codex:test','at':'2020-01-01T00:00:00Z'}
    (root/'AGENTS.md').write_text('profile methodology-consumer-pm/1.0.0 conventions_version 1.0.0 mode single-layer layer .\nRead actual five declared homes; fixtures authenticate no product consent.\n')
    (root/'CONVENTIONS.md').write_text('---\nprofile: methodology-consumer-pm/1.0.0\nconventions_version: 1.0.0\nmode: single-layer\nlayer: .\ntype: Conventions\ntitle: Owned synthetic conventions\nstatus: adopted\ngenerated: {by: codex:test, at: "2020-01-01T00:00:00Z"}\n---\n')
    record(root,generated,'VISION.md','Vision','# Owned record pilot\nGoal: read the bounded queue; arrival is recoverable current state.\n')
    record(root,generated,'ROADMAP.md','Roadmap','# Route\n- [ ] **P0.** 🔜 Useful records `<<< WE ARE HERE`\n## Deferred on purpose\n- Product Code held until exact spec.\n```mermaid\nflowchart LR\nP0["P0 🔜 Useful records"]\n```\n')
    record(root,generated,'HANDOFF.md','Handoff','# Handoff\n## Blocked on the owner\n- Product Code and integration remain reserved.\n## State\nOwned fixture current records; no Git revision or product consent.\n## Queue\nTASKS.md next T-001.\n## Traps\nDo not promote fixture metadata to authentic consent.\n')
    record(root,generated,'TASKS.md','Tasks','# Packet\n## T-001 bounded note\n- **Class:** S\n- **Status:** todo\n- **Done when:** Exact note exists.\n- **Stop and ask when:** Scope would change.\n- **Links:** P0; VISION.md\n',{'batch':'B-001','status':'proposed'})
    (root/'Doxyfile').write_text('INPUT = src\nFILE_PATTERNS = *.py\nRECURSIVE = YES\nOUTPUT_DIRECTORY = map\nGENERATE_XML = YES\nXML_OUTPUT = xml\n')
    return root
    # END_BLOCK_BusinessLogic
# endregion FUNC_fixture


# region FUNC_rows [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Return all actual native checklist rows keyed by their fixed IDs.
## @uses orient.collect, orient.run_checks
## @io Input: root owned project Path. Output: dict[str,orient.Check] exactly22 IDs; source errors retained through actual APIs. Side effects: reads and actual safe logs only. Errors: native ConsumerInputError for unavailable layout. Example: rows(root)["CHECK-02"] judges actual marker.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def rows(root):
    # START_BLOCK_BusinessLogic
    return {x.id:x for x in orient.run_checks(orient.collect(root))}
    # END_BLOCK_BusinessLogic
# endregion FUNC_rows


# region FUNC_invoke [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Exercise the real shipped CLI process with complete visible streams and no Python path injection.
## @uses subprocess.run
## @io Input: name trusted helper basename str, root explicit owned Path, args declared CLI strings/Paths. Output: CompletedProcess actual argv/returncode/stdout/stderr. Side effects: real authorized child; writes only when explicitly invoking owned apply. Errors: OSError on unavailable executable. Example: invoke("orient",root,"--check") exposes real exit0/1/2.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def invoke(name,root,*args):
    # START_BLOCK_BusinessLogic
    result=subprocess.run([sys.executable,'-B',str(SCRIPTS/(name+'.py')),str(root),*map(str,args)],capture_output=True,text=True,env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME')})
    print('actual argv',result.args,'stdout',result.stdout,'stderr',result.stderr,'exit',result.returncode)
    return result
    # END_BLOCK_BusinessLogic
# endregion FUNC_invoke


# region FUNC_source_fixture [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Create a literal owned software fixture in current or original old-markup form.
## @uses test_codemap.fixture, pathlib.Path.write_text
## @io Input: root absent owned Path, old bool false by default. Output: project Path with src/records.py rich exact-count contract and support.py constant11; actual shipped seed config bound to src/map. Side effects: fixture writes only. Errors: OSError on unavailable seed/setup. Example: old=True leaves real legacy summary/structure and one effective ^^ defect.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def source_fixture(root,old=False):
    # START_BLOCK_BusinessLogic
    fixture(root)
    config=(PACKAGE/'skills/pm/templates/Doxyfile').read_text().replace('INPUT                  = src tests','INPUT                  = src').replace('OUTPUT_DIRECTORY       = doxygen_output','OUTPUT_DIRECTORY       = map')
    (root/'Doxyfile').write_text(config.replace('invariants=@par Invariants:', 'invariants=@par Invariants:^^') if old else config)
    text='''# region MODULE_CONTRACT
## @modulecontract
## @purpose Keep exact count sum.
## @scope Pure fixture counts.
## @input Finite plain counts.
## @output Exact total.
## @links [USES_API(7): sum]
## @invariants
## All values counted.
## Wrapped own paragraph survives.
## @rationale
## Q: Why unequal values?
## A: Sum differs from first, last and max.
## @changes
## LAST_CHANGE: [1.0.0 - owned fixture.]
## @modulemap
## FUNC 9[Sum every value] => records.summarize
## @usecases
## Caller -> exact counts ->18.
## @GREP_SUMMARY own count sum
## @STRUCTURE counts to total
def _module_contract():
    pass
# endregion MODULE_CONTRACT

# region FUNC_summarize
## @purpose Return exact unequal-count sum.
## @uses sum
## @io values sequence to total integer; no external effect.
## @complexity 2
def summarize(values):
    return sum(values)
# endregion FUNC_summarize
'''
    if old:
        text=text.replace('## @GREP_SUMMARY own count sum\n','').replace('## @STRUCTURE counts to total\n','')+'\n# GREP_SUMMARY: own count sum\n# STRUCTURE: counts to total\n'
    (root/'src/records.py').write_text(text)
    (root/'src/support.py').write_text('VALUE = 11\n')
    return root
    # END_BLOCK_BusinessLogic
# endregion FUNC_source_fixture


# region FUNC_authority [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Construct only a synthetic exact-shape apply record for structural tests, never authentic human consent.
## @uses markup_migrate.Plan
## @io Input: plan fully assessed Plan, files exact relative str list. Output: dict action/target/files/planIdentity/originals/humanSource/parentVerification/generated; sorted scope matches plan. No filesystem effects. Errors: malformed caller Plan attribute access errors. Example: this record tests shape, while root separately authenticates actual C2 probe authority.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def authority(plan,files):
    # START_BLOCK_BusinessLogic
    return {'action':'markup-migrate-apply','target':str(plan.root),'files':sorted(files),'planIdentity':plan.identity,'originals':plan.originals,'humanSource':'Synthetic exact-scope test control; no consumer consent','parentVerification':'Test-created structural record only; actual parent must authenticate real run','generated':{'by':'codex:test','at':'2020-01-01T00:00:00Z','via':'owned structural test'}}
    # END_BLOCK_BusinessLogic
# endregion FUNC_authority


# region FUNC_build_map [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Build the real fixture Doxygen map silently and retain every original command/stream identity.
## @uses subprocess.run, codemap.source_population, consumer_files.identity
## @io Input: root owned software fixture Path. Output: index Path after exact exit0/zero-stream assertions; complete current config/source/index receipt. Side effects: fixture map XML plus unique build-NNN streams/receipt and current pointer; prior builds preserved. Errors: AssertionError for nonzero/warnings/missing map, OSError for unavailable resource. Example: rebuild writes build-002 records and points current.json to that real build.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def build_map(root):
    # START_BLOCK_BusinessLogic
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result=subprocess.run(['doxygen','Doxyfile'],cwd=root,capture_output=True,text=True)
    print('actual Doxygen',result.args,start,result.returncode,result.stdout,result.stderr)
    assert result.returncode==0 and not result.stdout and not result.stderr
    directory=root/'.methodology/maps';directory.mkdir(parents=True,exist_ok=True)
    number=len(list(directory.glob('build-*.json')))+1;prefix='build-%03d'%number
    (directory/(prefix+'.stdout')).write_text(result.stdout);(directory/(prefix+'.stderr')).write_text(result.stderr)
    info,pop=codemap.source_population(root); index=root/'map/xml/index.xml'
    receipt={'config':{'path':'Doxyfile','sha256':cf.identity(root/'Doxyfile')['sha256']},'sources':pop.source_identities,'index':{'path':'map/xml/index.xml','sha256':cf.identity(index)['sha256']},'build':{'argv':result.args,'cwd':str(root),'exitCode':result.returncode,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'start':start,'environmentNames':sorted(os.environ),'stdout':'.methodology/maps/'+prefix+'.stdout','stderr':'.methodology/maps/'+prefix+'.stderr'}}
    (directory/(prefix+'.json')).write_text(json.dumps(receipt));(directory/'current.json').write_text(json.dumps(receipt))
    return index
    # END_BLOCK_BusinessLogic

# endregion FUNC_build_map

# region FUNC_test_codemap_own_xml_fields_and_location [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Inspect every actual own rich module field and location after silent real Doxygen build.
## @uses codemap.map_state, codemap.mapped_fields, codemap.run, test_codemap.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; records own wrapped invariants/change/modulemap/source/config receipt; neighboring support lacks that contract.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_codemap_own_xml_fields_and_location(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');build_map(root);state=codemap.map_state(root);print('actual current',state['eligible'],state['reason']);expose(caplog)
    assert state['eligible']
    code,text=codemap.run(root,'src/records.py');print(text);assert code==0 and 'source: Doxygen:' in text and 'Keep exact count sum.' in text
    expected=codemap.contract_fields((root/'src/records.py').read_text().split('# endregion MODULE_CONTRACT')[0]); fields,reason=codemap.mapped_fields(state,'src/records.py',0,expected,module=True)
    assert fields is not None and 'Wrapped own paragraph survives.' in fields['invariants'] and 'LAST_CHANGE' in fields['changes'] and 'Sum every value' in fields['modulemap']
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_codemap_own_xml_fields_and_location


# region FUNC_test_codemap_static_nested_async_alias_ambiguity [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Keep async/nested call ownership and disclose two actual same-name symbol blocks.
## @uses codemap.build_index, codemap.run, test_codemap.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; records.summarize and support.summarize; async support.outer with own nested definition.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_codemap_static_nested_async_alias_ambiguity(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');(root/'src/support.py').write_text('def summarize(values):\n    return max(values)\n\nasync def outer(values):\n    def nested():\n        return summarize(values)\n    return nested()\n')
    index=codemap.build_index(root);print(index);expose(caplog)
    assert any(x['name']=='support.outer.nested' and x['calls']==['summarize'] for x in index)
    assert next(x for x in index if x['name']=='support.outer')['calls']==['nested']
    code,text=codemap.run(root,'summarize');print(text);assert code==0 and 'matches: 2' in text and text.count('symbol: ')==2 and '(by name)' in text
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_codemap_static_nested_async_alias_ambiguity


# region FUNC_test_codemap_fallbacks_and_unavailable_population [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Distinguish absent-map source fallback, syntax-incomplete relation refusal2 and complete missing1.
## @uses codemap.run, test_codemap.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; map missing then actual built map plus malformed support.py followed by restored valid source.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_codemap_fallbacks_and_unavailable_population(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');code,text=codemap.run(root,'src/records.py');print(text);expose(caplog);assert code==0 and 'source fallback: Map not built' in text
    build_map(root); (root/'src/support.py').write_text('def broken(:\n')
    caplog.clear();code,text=codemap.run(root,'summarize');print(text);expose(caplog,(('consumer_files',40,'[IMP:10][build_index][VALIDATION_FAILURE] cause=unparseable-relation-population'),('codemap',40,'[IMP:10][run][UNAVAILABLE] kind=ConsumerInputError')));assert code==2
    (root/'src/support.py').write_text('VALUE=11\n');caplog.clear();code,text=codemap.run(root,'missing');expose(caplog);assert code==1
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_codemap_fallbacks_and_unavailable_population


# region FUNC_test_codemap_real_cli_shape [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Verify actual file five-line/source-second shape and CLI0/1/2 endpoint delivery.
## @uses codemap.main, test_codemap.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; owned src/records.py, absent symbol and ../outside.py traversal.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_codemap_real_cli_shape(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');result=invoke('codemap',root,'src/records.py');expose(caplog);lines=result.stdout.splitlines();assert result.returncode==0 and len(lines)==5 and lines[1].startswith('source: ') and lines[2].startswith('GREP_SUMMARY: ')
    result=invoke('codemap',root,'missing');assert result.returncode==1
    result=invoke('codemap',root,'../outside.py');assert result.returncode==2 and 'unavailable' in result.stderr
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_codemap_real_cli_shape

# region FUNC_test_real_list_contract_and_foreign_fields [DOMAIN(9): CodeMap; CONCEPT(9): OwnAssociation; TECH(8): Doxygen]
## @purpose Accept a real independently shaped list contract while refusing lost content and foreign own fields.
## @uses test_codemap.source_fixture, test_codemap.build_map, codemap.mapped_fields, codemap.run, xml.etree.ElementTree
## @io Input: tmp_path owned Path and caplog pytest log fixture. Output: None after exact source/own XML assertions.
##   Invariants: two substantive invariant items and one usecase survive real Doxygen; no field is borrowed from a sibling.
##   Side effects: writes/builds only under tmp_path; source package read-only. Guarantees: corrupted own text degrades to source fallback even when receipt/index stay current.
##   Errors: AssertionError for unexpected status, content/location mismatch or any ERROR/CRITICAL event.
##   Example: source bullets 'No database' and 'Every row' render as two visible list items and both remain required. Importance:9.
## @complexity 5
def test_real_list_contract_and_foreign_fields(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO); root=source_fixture(tmp_path/'project')
    path=root/'src/records.py'; text=path.read_text().replace('## All values counted.','## - All values counted.').replace('## Wrapped own paragraph survives.','## - Wrapped own paragraph survives.').replace('## Caller -> exact counts ->18.','## - Caller -> exact counts ->18.')
    path.write_text(text); build_map(root); state=codemap.map_state(root)
    expected=codemap.contract_fields(text.split('# endregion MODULE_CONTRACT')[0])
    fields,reason=codemap.mapped_fields(state,'src/records.py',0,expected,module=True)
    print('real list fields',fields,reason); expose(caplog)
    assert fields is not None and 'All values counted.' in fields['invariants'] and 'Wrapped own paragraph survives.' in fields['invariants']
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    compound=root/'map/xml/namespacerecords.xml'; original=compound.read_bytes()
    try:
        compound.write_bytes(original.replace(b'Wrapped own paragraph survives.',b'Foreign sibling paragraph.'))
        damaged=codemap.map_state(root); result,reason=codemap.mapped_fields(damaged,'src/records.py',0,expected,module=True)
        print('corrupt own field',result,reason); assert result is None and 'mismatch' in reason
        code,answer=codemap.run(root,'src/records.py'); assert code==0 and 'source fallback:' in answer and 'source: Doxygen:' not in answer
        wrong,reason=codemap.mapped_fields(state,'src/support.py',0,expected,module=True)
        assert wrong is None and 'Own entity not mapped' in reason
    finally: compound.write_bytes(original)
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_list_contract_and_foreign_fields

# region FUNC_test_alias_shadow_class_control_flow_and_nested_ownership [DOMAIN(9): CodeMap; CONCEPT(9): StaticScope; TECH(8): ast]
## @purpose Resolve only unshadowed own-scope from-import aliases and keep nested/async/control-flow definitions separate.
## @uses codemap.build_index, codemap.run, test_codemap.source_fixture, test_codemap.expose
## @io Input: owned tmp_path and caplog. Output: None after exact fixed names/calls and class disclaimer assertions.
##   Side effects: writes literal fixture Python only; consumer never imported. Guarantees: an inner parameter cannot shadow an outer alias.
##   Errors: AssertionError on wrong call population or any ERROR/CRITICAL event. Example: outer calls records.summarize while inner(tally) retains unresolved tally. Importance:9.
## @complexity 6
def test_alias_shadow_class_control_flow_and_nested_ownership(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project')
    (root/'src/support.py').write_text('from records import summarize as tally\n\nasync def outer(values):\n    def inner(tally):\n        return tally(values)\n    return tally(values)\n\ndef shadow(tally, values):\n    return tally(values)\n\ndef local(values):\n    from records import summarize as local_sum\n    return local_sum(values)\n\nif True:\n    class Holder:\n        def method(self, values):\n            return tally(values)\n')
    index=codemap.build_index(root);names={item['name']:item['calls'] for item in index};print(names);expose(caplog)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    assert names['support.outer']==['records.summarize'] and names['support.outer.inner']==['tally'] and names['support.shadow']==['tally'] and names['support.local']==['records.summarize']
    assert names['support.Holder']==[] and names['support.Holder.method']==['records.summarize']
    code,text=codemap.run(root,'Holder');print(text);assert code==0 and 'relations: classes not recorded' in text and 'no non-instantiation' in text
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_alias_shadow_class_control_flow_and_nested_ownership

# region FUNC_test_current_broken_stale_and_inprogress_real_maps [DOMAIN(9): CodeMap; CONCEPT(9): FreshOwnEvidence; TECH(8): Doxygen, Git]
## @purpose Exercise actual current/broken/stale/in-progress map responses without promoting lifecycle or fallback to complete own XML.
## @uses test_codemap.build_map, codemap.map_state, codemap.run, subprocess.run
## @io Input: owned tmp_path and caplog. Output: None after exact actual receipt/lifecycle/fallback readback assertions.
##   Side effects: real maps and expressly owned fixture-local Git initialization/commit, no inspected product execution.
##   Guarantees: a corrupted relevant compound affects its own answer only; newer uncommitted source is in progress but ineligible.
##   Errors: AssertionError for unexpected status/stream or ERROR/CRITICAL events. Example: committed base map then dirty support.py yields source fallback in progress. Importance:9.
## @complexity 6
def test_current_broken_stale_and_inprogress_real_maps(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');build_map(root);state=codemap.map_state(root);assert state['eligible']
    compound=root/'map/xml/namespacerecords.xml';before=compound.read_bytes();mode=stat.S_IMODE(compound.stat().st_mode)
    try:
        compound.write_text('<broken');code,text=codemap.run(root,'src/records.py');print(text);assert code==0 and 'source fallback: Requested compound broken/unavailable' in text
    finally:compound.write_bytes(before);compound.chmod(mode)
    (root/'src/support.py').write_text('VALUE=24\n');state=codemap.map_state(root);print(state['lifecycle'],state['reason']);assert state['lifecycle']=='stale' and not state['eligible']
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    env={key:value for key,value in os.environ.items() if not key.startswith('GIT_')}
    for args in (['init'],['config','user.name','Owned Test'],['config','user.email','owned'+'@'+'example.invalid'],['add','.'],['commit','-m','Owned map fixture baseline']):
        start=datetime.datetime.now(datetime.timezone.utc).isoformat();process=subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,env=env);print({'argv':process.args,'cwd':str(root),'environmentNames':sorted(env),'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exitCode':process.returncode,'stdout':process.stdout,'stderr':process.stderr});assert process.returncode==0
    build_map(root);(root/'src/support.py').write_text('VALUE=31\n');state=codemap.map_state(root);print(state['lifecycle'],state['reason']);assert state['lifecycle']=='in progress' and not state['eligible']
    code,text=codemap.run(root,'src/records.py');print(text);assert code==0 and 'source fallback:' in text and 'in progress' in text and 'source: Doxygen:' not in text
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_current_broken_stale_and_inprogress_real_maps

# region FUNC_test_unique_actual_module_anchor_and_relative_alias [DOMAIN(9): Navigation; CONCEPT(10): OwnAssociation; TECH(8): AST, Doxygen]
## @purpose Refuse current-module certification at a wrong actual source line and resolve module-level relative aliases without importing consumer code.
## @uses codemap.run, codemap.build_index, test_codemap.build_map, xml.etree.ElementTree
## @io Input: owned tmp_path, caplog. Output: None after current positive/wrong-location fallback and literal qualified-call assertions.
##   Side effects: owned fixture build and XML corruption only; original compound restored exactly. Guarantee: complete fields do not excuse a false source coordinate.
##   Errors: AssertionError on wrong association or unexpected ERROR/CRITICAL. Example: same name/fields with line9999 must fall back. Importance10.
## @complexity 5
def test_unique_actual_module_anchor_and_relative_alias(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');build_map(root);state=codemap.map_state(root);code,text=codemap.run(root,'src/records.py');print(text);assert code==0 and 'source: Doxygen:' in text
    compound=next(path for path in (root/'map/xml').glob('*.xml') if any(entity.findtext('name')=='_module_contract' and entity.find('location') is not None and entity.find('location').get('file','').endswith('records.py') for entity in ET.fromstring(path.read_text()).iter('memberdef')));original=compound.read_bytes();tree=ET.fromstring(original)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for entity in tree.iter('memberdef'):
        if entity.findtext('name')=='_module_contract' and entity.find('location') is not None: entity.find('location').set('line','9999')
    compound.write_bytes(ET.tostring(tree));code,text=codemap.run(root,'src/records.py');print(text);assert code==0 and 'source fallback:' in text;compound.write_bytes(original)
    package=root/'src/pkg';package.mkdir();(package/'__init__.py').write_text('');(package/'api.py').write_text('def target():\n    return 18\n');(package/'client.py').write_text('from .api import target as alias\ndef caller():\n    return alias()\n')
    indexed=codemap.build_index(root);caller=next(item for item in indexed if item['name']=='pkg.client.caller');print(caller);assert caller['calls']==['pkg.api.target'];expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_unique_actual_module_anchor_and_relative_alias


# region FUNC_record [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Write one filled synthetic front-matter record in the fixture owner root.
## @uses json.dumps, pathlib.Path.write_text
## @io Input: root fresh owned fixture Path, generated dict[str,str] with explicit synthetic by/at; internal fixture record author only, no actual human authority;  name relative fixture filename str, kind/body str, extra optional dict override; supplied root owned. Output: None; one complete UTF8 record. Side effects: one fixture file. Errors: OSError/TypeError on unsupported supplied test data. Example: TASKS record extra batch B-001 and proposed status.
##   Operational guarantee: standard tmp_path ownership, deterministic literal data and no real consumer consent; importance9.
## @complexity 7
def record(root,generated,name,kind,body,extra=None):
    # START_BLOCK_BusinessLogic
    fields={'type':kind,'title':'Owned synthetic '+kind,'generated':generated,'status':'current'};fields.update(extra or {})
    text='---\n'+'\n'.join(k+': '+json.dumps(v) for k,v in fields.items())+'\n---\n\n'+body
    (root/name).write_text(text)
    # END_BLOCK_BusinessLogic
# endregion FUNC_record



# region FUNC_test_error_oracle_complete_identity [DOMAIN(9): Verification; CONCEPT(10): OwningEvent, PhysicalEvidence; TECH(8): logging, pytest]
## @purpose Reject equal-text foreign/severity substitutions and wrong message, order or cardinality using this module's actual shipped error oracle.
## @uses test_codemap.expose, consumer_files.parse_front_matter, logging.FileHandler, logging.getLogger, pytest.raises
## @io Input: caplog actual pytest capture and tmp_path fresh owned Path. Output: None after genuine owning scalar ERROR40 acceptance and eight identity/population refusals, with complete independent flushed UTF8 file readback.
##   Trigger: regression of expected-only logging validation. Side effects: one owned error-events.log, root handler installed then removed/closed in finally; adversarial logger events confined to test capture, no product writes or fake consent.
##   Guarantees: expected logger names/40/message literals never come from captured records or runtime logger objects; normal production exception, equal-text foreign ERROR, own CRITICAL/custom41, wrong function/cause, missing/extra/reordered records are distinguished. All negative records remain visible in physical sink.
##   Errors: AssertionError on oracle admission, absent sink event or failed cleanup; actual ConsumerInputError remains required for genuine malformed input. Example: consumer_files40 scalar failure passes, oracle_foreign40 with identical message fails. Importance10.
## @complexity 5
def test_error_oracle_complete_identity(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    first=('consumer_files',40,'[IMP:10][scalar][VALIDATION_FAILURE] cause=malformed-quoted-value')
    second=('consumer_files',40,'[IMP:10][parse_front_matter][VALIDATION_FAILURE] cause=invalid-or-duplicate-key')
    expected=(first,)
    sink=tmp_path/'error-events.log';handler=logging.FileHandler(sink,encoding='utf-8');handler.setLevel(40);handler.setFormatter(logging.Formatter('%(name)s|%(levelno)s|%(message)s'))
    root_logger=logging.getLogger();root_logger.addHandler(handler)
    physical_expected=[]
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    try:
        caplog.clear()
        with pytest.raises(cf.ConsumerInputError):cf.parse_front_matter('---\na: "broken\n---\n')
        expose(caplog,expected);handler.flush();physical_expected.append('consumer_files|40|'+first[2])
        assert sink.read_text().splitlines()==physical_expected
        caplog.clear()
        with pytest.raises(cf.ConsumerInputError):cf.parse_front_matter('---\na: "broken\n---\n')
        with pytest.raises(cf.ConsumerInputError):cf.parse_front_matter('---\na: 1\na: 2\n---\n')
        expose(caplog,(first,second));handler.flush();physical_expected+=['consumer_files|40|'+first[2],'consumer_files|40|'+second[2]]
        assert sink.read_text().splitlines()==physical_expected
        cases=[('foreign',(('oracle_foreign',40,first[2]),),expected),('critical',(('consumer_files',50,first[2]),),expected),('custom-level',(('consumer_files',41,first[2]),),expected),('wrong-function',(('consumer_files',40,'[IMP:10][parse_front_matter][VALIDATION_FAILURE] cause=malformed-quoted-value'),),expected),('wrong-cause',(('consumer_files',40,'[IMP:10][scalar][VALIDATION_FAILURE] cause=invalid-or-duplicate-key'),),expected),('missing',(),expected),('duplicate',(first,first),expected),('reordered',(second,first),(first,second))]
        for label,events,manifest in cases:
            caplog.clear()
            for name,level,message in events:logging.getLogger(name).log(level,message)
            handler.flush()
            with pytest.raises(AssertionError):expose(caplog,manifest)
            physical_expected.extend(name+'|'+str(level)+'|'+message for name,level,message in events)
            actual=sink.read_text().splitlines();print(label,actual)
            assert actual==physical_expected
        caplog.clear();expose(caplog)
    finally:
        root_logger.removeHandler(handler);handler.close()
    assert handler not in root_logger.handlers
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_error_oracle_complete_identity
