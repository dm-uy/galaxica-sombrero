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
## LAST_CHANGE: [2.2.0 - Retained C2 behavior controls; A2 Debug2 strengthens complete ordered logger/numeric-level/message identity and physical-sink discrimination; CHECK09 real root/flow/single/custom-layer and legal checkpoint-plan controls.]
## @modulemap
## FUNC 9[Reject generic plans at every distinct adopted root while preserving real legal checkpoint plans, full CLI checks and exact owning error events.] => test_consumer_pm.test_generic_plan_all_adopted_layer_roots
## FUNC 9[Reject equal-text foreign/severity substitutions, missing/duplicate/reordered events through the shipped oracle and real flushed sink.] => test_consumer_pm.test_error_oracle_complete_identity
## FUNC 9[Import the explicitly trusted shipped helper directly without modifying sys.path.] => test_consumer_pm.load
## FUNC 9[Expose all actual important records and assert the complete expected-only error population.] => test_consumer_pm.expose
## FUNC 9[Create a complete explicitly synthetic adopted single-layer record fixture with real homes.] => test_consumer_pm.fixture
## FUNC 9[Return all actual native checklist rows keyed by their fixed IDs.] => test_consumer_pm.rows
## FUNC 9[Exercise the real shipped CLI process with complete visible streams and no Python path injection.] => test_consumer_pm.invoke
## FUNC 9[Create a literal owned software fixture in current or original old-markup form.] => test_consumer_pm.source_fixture
## FUNC 9[Construct only a synthetic exact-shape apply record for structural tests, never authentic human consent.] => test_consumer_pm.authority
## FUNC 9[Build the real fixture Doxygen map silently and retain every original command/stream identity.] => test_consumer_pm.build_map
## FUNC 9[Measure the complete22 row population and inclusive600/150 line limits with +1 refusal.] => test_consumer_pm.test_native_profile_rows_and_budgets
## FUNC 9[Reject future/malformed actual provenance and handoff older than active exact gate.] => test_consumer_pm.test_provenance_and_active_handoff_refuse
## FUNC 9[Resolve every scalar/inline/block-list DEC amendment without hiding a missing sibling.] => test_consumer_pm.test_every_amendment_shape_resolves
## FUNC 9[Refuse independent missing-marker, duplicate heading and unsupported runnable task-class defects.] => test_consumer_pm.test_markers_headings_tasks_and_idle
## FUNC 9[Exercise actual readonly orient and two-root portfolio CLI with exact labelled profile count.] => test_consumer_pm.test_orient_real_cli_and_portfolio
## FUNC 9[Assert exact13 seed names/four entry bindings and independent finite75/22 accounting membership.] => test_consumer_pm.test_profile_resources_and_entry_routes
## FUNC 9[Retain valid local candidate status/source while refusing unavailable required C4 ledger comparison.] => test_consumer_pm.test_candidate_ledger_is_unavailable
## FUNC 9[Attribute Git observations only to the explicit repository root and preserve worktree gitfile support.] => test_consumer_pm.test_git_binding_nested_repository_and_gitfile
## FUNC 9[Measure exact State/step/route boundaries and distinguish an idle packet from an open idle conflict.] => test_consumer_pm.test_all_profile_boundaries_and_idle
## FUNC 9[Refuse every selected marker/task field and adopted conventions/CLAUDE provenance or instruction defect.] => test_consumer_pm.test_complete_marker_task_and_provenance_population
## FUNC 9[Check exact scalar amendments, unique reservations, duplicate IDs and reciprocal supersession across real owned records.] => test_consumer_pm.test_decision_reservations_duplicates_and_supersession
## FUNC 9[Run and expose a complete actual command receipt only for a newly owned disposable Git fixture.] => test_consumer_pm.git_fixture_command
## FUNC 9[Exercise real layered commit history/owner-exception recognition and retained archived-batch branch checks regardless current packet.] => test_consumer_pm.test_layered_history_archive_and_each_layer
## FUNC 9[Exercise roots-file real CLI and preserve unavailable legacy and invalid local-candidate statuses without pretending external comparison.] => test_consumer_pm.test_roots_file_legacy_and_local_candidate_controls
## FUNC 9[Discriminate actual invalid-argument payload leakage across all three shipped CLIs while preserving help0/invalid2/usage.] => test_consumer_pm.test_three_cli_argument_payload_refusal
## FUNC 9[Write one filled synthetic front-matter record in the fixture owner root.] => test_consumer_pm.record
## FUNC 9[Discriminate goal recovery from trailing deferred prose in ordinary, custom and layered actual homes.] => test_consumer_pm.test_goal_purpose_supported_homes
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY test_consumer_pm, consumer PM, explicit paths, complete population, supported grammar, evidence
## @STRUCTURE ▶ explicit inputs → ◇ validate supported shape → ○ own operations → ⎋ attributable result or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import importlib.util
import re
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
## @uses test_consumer_pm.record, pathlib.Path.write_text, json.dumps
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
## @uses test_consumer_pm.fixture, pathlib.Path.write_text
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

# region FUNC_test_native_profile_rows_and_budgets [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Measure the complete22 row population and inclusive600/150 line limits with +1 refusal.
## @uses orient.collect, orient.run_checks, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; filled single-layer fixture with exact measured600/601 always-read and150/151 handoff lines.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_native_profile_rows_and_budgets(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project'); result=rows(root);print({k:v.status for k,v in result.items()});expose(caplog)
    assert len(result)==22 and all(x.status in ('PASS','N/A') for x in result.values())
    original=(root/'AGENTS.md').read_text();total=sum(len((root/x).read_text().splitlines()) for x in ('AGENTS.md','VISION.md','ROADMAP.md','HANDOFF.md','TASKS.md'))
    (root/'AGENTS.md').write_text(original+'\n'*(600-total)); assert rows(root)['CHECK-14'].status=='PASS'
    (root/'AGENTS.md').write_text(original+'\n'*(601-total)); assert rows(root)['CHECK-14'].status=='FAIL'
    (root/'AGENTS.md').write_text(original);h=(root/'HANDOFF.md').read_text();(root/'HANDOFF.md').write_text(h+'\n'*(150-len(h.splitlines()))); assert rows(root)['CHECK-03'].status=='PASS'
    (root/'HANDOFF.md').write_text(h+'\n'*(151-len(h.splitlines())));assert rows(root)['CHECK-03'].status=='FAIL'
    (root/'HANDOFF.md').write_text(h)
    # Expected row failures are the known boundary controls; reject errors from any other owner.
    errors=[(x.name,x.levelno,x.getMessage()) for x in caplog.records if x.levelno>=40];print(errors)
    assert errors==[('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=14'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=3')]
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_native_profile_rows_and_budgets


# region FUNC_test_provenance_and_active_handoff_refuse [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Reject future/malformed actual provenance and handoff older than active exact gate.
## @uses consumer_files.provenance, orient.run_checks, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; 2020 generated timestamp mutated to2099/not-clock and active2020-01-02 gate over2020-01-01 handoff.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_provenance_and_active_handoff_refuse(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project'); original=(root/'VISION.md').read_text()
    for replacement,cause in [('2099-01-01T00:00:00Z','future-clock'),('not-a-clock','invalid-utc-clock')]:
        caplog.clear();(root/'VISION.md').write_text(original.replace('2020-01-01T00:00:00Z',replacement)); result=rows(root);print(result['CHECK-08']);
        expose(caplog,(('consumer_files',40,f'[IMP:10][timestamp][VALIDATION_FAILURE] cause={cause}'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=8')))
        assert result['CHECK-08'].status=='FAIL'
    (root/'VISION.md').write_text(original)
    caplog.clear();packet=(root/'TASKS.md').read_text().replace('status: "proposed"','status: "active"').replace('---\n\n# Packet','gate_a: {decision: approved, by: owner, at: "2020-01-02T00:00:00Z", via: "original decision", action: "fixture S", scope: "exact note"}\n---\n\n# Packet');(root/'TASKS.md').write_text(packet)
    result=rows(root);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=19'),)); assert result['CHECK-19'].status=='FAIL'
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_provenance_and_active_handoff_refuse


# region FUNC_test_every_amendment_shape_resolves [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Resolve every scalar/inline/block-list DEC amendment without hiding a missing sibling.
## @uses orient.run_checks, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; DEC-001 and DEC-002 plus invalid exact DEC-999 item in both list shapes.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_every_amendment_shape_resolves(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');directory=root/'docs/decisions';directory.mkdir(parents=True)
    base='---\ntype: Decision\ntitle: Owned structural decision\nstatus: accepted\ngenerated: {by: codex:test, at: "2020-01-01T00:00:00Z"}\ndecided: {by: owner, at: "2020-01-01T00:00:00Z", via: "synthetic channel; not authority"}\nid: ID\nAMEND---\n# Original accepted body remains unchanged.\n'
    (directory/'DEC-002.md').write_text(base.replace('ID','DEC-002').replace('AMEND',''))
    for amendment in ['amended_by: "DEC-002: valid"\n','amended_by: ["DEC-002: valid", "DEC-999: missing"]\n','amended_by:\n  - "DEC-002: valid"\n  - "DEC-999: missing"\n']:
        caplog.clear();(directory/'DEC-001.md').write_text(base.replace('ID','DEC-001').replace('AMEND',amendment));result=rows(root);print(result['CHECK-05']);
        if '999' in amendment: expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=5'),)); assert result['CHECK-05'].status=='FAIL'
        else: expose(caplog);assert result['CHECK-05'].status=='PASS'
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_every_amendment_shape_resolves


# region FUNC_test_markers_headings_tasks_and_idle [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Refuse independent missing-marker, duplicate heading and unsupported runnable task-class defects.
## @uses orient.run_checks, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; current emoji retained while marker missing; Queue replaced by State; S replaced with L.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_markers_headings_tasks_and_idle(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project')
    cases=[('ROADMAP.md','<<< WE ARE HERE','missing',2),('HANDOFF.md','## Queue','## State',3),('TASKS.md','**Class:** S','**Class:** L',16)]
    for name,old,new,row in cases:
        caplog.clear();path=root/name;original=path.read_bytes();path.write_bytes(original.replace(old.encode(),new.encode()));result=rows(root);expose(caplog,(('orient',40,f'[IMP:10][run_checks][ROW_FAILURE] row={row}'),));assert result[f'CHECK-{row:02d}'].status=='FAIL';path.write_bytes(original)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_markers_headings_tasks_and_idle


# region FUNC_test_orient_real_cli_and_portfolio [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Exercise actual readonly orient and two-root portfolio CLI with exact labelled profile count.
## @uses orient.main, orient.run_portfolio, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; two filled known roots, unsupported second profile and full original file bytes.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_orient_real_cli_and_portfolio(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');second=fixture(tmp_path/'second')
    before={str(p):p.read_bytes() for p in root.rglob('*') if p.is_file()}
    result=invoke('orient',root,'--check');assert result.returncode==0 and 'CHECK-22 PASS' in result.stdout
    process=subprocess.run([sys.executable,'-B',str(SCRIPTS/'orient.py'),'--portfolio',str(root),str(second),'--check'],capture_output=True,text=True);print(process.stdout,process.stderr);assert process.returncode==0 and sum(line=='profile: methodology-consumer-pm/1.0.0' for line in process.stdout.splitlines())==2
    assert {str(p):p.read_bytes() for p in root.rglob('*') if p.is_file()}==before
    (second/'CONVENTIONS.md').write_text('---\nprofile: unsupported\n---\n');result=invoke('orient',second,'--check');assert result.returncode==2 and 'unavailable' in result.stdout
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_orient_real_cli_and_portfolio


# region FUNC_test_profile_resources_and_entry_routes [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Assert exact13 seed names/four entry bindings and independent finite75/22 accounting membership.
## @uses pathlib.Path.read_text, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; literal expected13 resource names and all CV1..75/CHECK01..22; semantic/native actor proof separate.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_profile_resources_and_entry_routes(caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);profile=(PACKAGE/'references/consumer-pm-profile.md').read_text(); resources=sorted(p.name for p in (PACKAGE/'skills/pm/templates').iterdir()); print(resources)
    assert resources==sorted(['AGENTS.md','CLAUDE.md','CONVENTIONS.md','DEC.md','Doxyfile','HANDOFF.md','OPEN_QUESTIONS.md','RECON.md','ROADMAP.md','SPEC.md','TASKS.md','VISION.md','gitignore'])
    assert sum('| CV-%d |'%i in profile for i in range(1,76))==75 and sum('| CHECK-%02d |'%i in profile for i in range(1,23))==22
    for name in ('pm-bootstrap','pm-plan-batch','pm-run-batch','pm-handoff'):
        text=(PACKAGE/'skills'/name/'SKILL.md').read_text();assert 'consumer-pm-profile.md' in text and 'Full owners:' in text and 'actual' in text
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_profile_resources_and_entry_routes


# region FUNC_test_candidate_ledger_is_unavailable [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain valid local candidate status/source while refusing unavailable required C4 ledger comparison.
## @uses orient.run_checks, orient.main, test_consumer_pm.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; one pending Candidate pointing to actual VISION.md; no external ledger.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_candidate_ledger_is_unavailable(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');(root/'notes').mkdir();(root/'notes/candidate-local.md').write_text('---\ntype: Candidate\ntitle: Owned candidate\nstatus: pending\nsource: VISION.md\ngenerated: {by: codex:test, at: "2020-01-01T00:00:00Z"}\n---\nLocal lesson; external comparison missing.\n')
    result=rows(root); print(result['CHECK-20']);expose(caplog);assert result['CHECK-20'].status=='UNAVAILABLE'
    process=invoke('orient',root,'--check');assert process.returncode==2 and 'C4' in process.stdout
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_candidate_ledger_is_unavailable

# region FUNC_test_git_binding_nested_repository_and_gitfile [DOMAIN(9): ConsumerPM; CONCEPT(9): RootBinding; TECH(8): Git]
## @purpose Attribute Git observations only to the explicit repository root and preserve worktree gitfile support.
## @uses orient.git_info, subprocess.run, consumer_files.identity
## @io Input: tmp_path owned Path and caplog fixture. Output: None after fixed own-root/nested/gitfile assertions.
##   Invariants: nested fixture has no own .git and cannot inherit ancestor changed paths; real worktree .git is a file.
##   Side effects: Git initialization/commit/worktree creation only in owned tmp_path fixtures, no user Git state.
##   Guarantees: poisoned ambient GIT variables are stripped by production; complete spaced rename endpoints survive.
##   Errors: AssertionError for failed real fixture command or unexpected ERROR/CRITICAL event. Example: outer/src.py is absent from nested baseline. Importance:9.
## @complexity 6
def test_git_binding_nested_repository_and_gitfile(tmp_path,caplog,monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO); parent=tmp_path/'repository'; parent.mkdir()
    env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
    commands=[['git','init',str(parent)],['git','-C',str(parent),'config','user.name','Owned Test'],['git','-C',str(parent),'config','user.email','owned'+'@'+'example.invalid']]
    for command in commands:
        result=subprocess.run(command,env=env,capture_output=True,text=True); print(command,result.returncode); assert result.returncode==0
    (parent/'outer source.py').write_text('VALUE=1\n')
    for args in (['add','outer source.py'],['commit','-m','Owned fixture baseline']):
        result=subprocess.run(['git','-C',str(parent),*args],env=env,capture_output=True,text=True); assert result.returncode==0
    nested=parent/'nested';nested.mkdir();(nested/'record.md').write_text('Owned nested filesystem record.\n')
    monkeypatch.setenv('GIT_DIR',str(tmp_path/'missing-git'))
    observation=orient.git_info(nested); print(observation);assert not observation['repository'] and [x['path'] for x in observation['baseline']]==['record.md']
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    (parent/'outer source.py').write_text('VALUE=2\n'); own=orient.git_info(parent);print(own);assert own['repository'] and 'outer source.py' in own['changed']
    linked=tmp_path/'linked';result=subprocess.run(['git','-C',str(parent),'worktree','add','--detach',str(linked)],env=env,capture_output=True,text=True); print(result.stdout,result.stderr);assert result.returncode==0 and (linked/'.git').is_file()
    worktree=orient.git_info(linked);print(worktree);assert worktree['repository'] and worktree['changed']==[]
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_git_binding_nested_repository_and_gitfile

# region FUNC_test_all_profile_boundaries_and_idle [DOMAIN(9): ConsumerPM; CONCEPT(9): InclusiveBudgets, Idle; TECH(8): pytest]
## @purpose Measure exact State/step/route boundaries and distinguish an idle packet from an open idle conflict.
## @uses test_consumer_pm.fixture, test_consumer_pm.rows, test_consumer_pm.expose, orient.dated_state
## @io Input: owned tmp_path and caplog. Output: None after fixed2/3 date,300/301 step,25000/25001 route assertions.
##   Side effects: only owned fixture records; complete original bytes restored after every negative. No product consent.
##   Guarantees: code-fence/table dates do not count; no checkpoint in progress may retain position on an ahead step.
##   Errors: AssertionError for wrong measured threshold or any unrelated ERROR/CRITICAL record.
##   Example: idle/no tasks passes row12; proposed/open task on the same idle route fails row12. Importance:9.
## @complexity 7
def test_all_profile_boundaries_and_idle(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');original=(root/'HANDOFF.md').read_bytes()
    hand=original.decode().replace('Owned fixture current records; no Git revision or product consent.','2020-01-01 current checkpoint.\n\n2020-01-02 previous checkpoint.\n\n```text\n2020-01-03 fenced\n```\n| 2020-01-04 | table |')
    (root/'HANDOFF.md').write_text(hand);result=rows(root);print('two date items',result['CHECK-21']);expose(caplog);assert result['CHECK-21'].status=='PASS'
    caplog.clear();(root/'HANDOFF.md').write_text(hand.replace('## Queue','2020-01-05 third item.\n\n## Queue'));result=rows(root);print(result['CHECK-21']);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=21'),));assert result['CHECK-21'].status=='FAIL'
    (root/'HANDOFF.md').write_bytes(original)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    path=root/'ROADMAP.md';original=path.read_bytes();text=original.decode();line=next(line for line in text.splitlines() if line.startswith('- [ ]'))
    for size,status in ((300,'PASS'),(301,'FAIL')):
        caplog.clear();path.write_text(text.replace(line,line+'x'*(size-len(line))));result=rows(root);print('step chars',size,result['CHECK-02']);expose(caplog,() if status=='PASS' else (('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=2'),));assert result['CHECK-02'].status==status
    for size,status in ((25000,'PASS'),(25001,'FAIL')):
        caplog.clear();path.write_text(text+'x'*(size-len(text)));result=rows(root);print('route chars',len(path.read_text()),result['CHECK-02']);expose(caplog,() if status=='PASS' else (('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=2'),));assert result['CHECK-02'].status==status
    path.write_text(text.replace('🔜','⬜'));packet=root/'TASKS.md';packet_original=packet.read_bytes();packet.write_text(packet_original.decode().split('## T-001')[0].replace('status: "proposed"','status: "idle"'))
    caplog.clear();result=rows(root);print('idle',result['CHECK-12']);expose(caplog);assert result['CHECK-02'].status=='PASS' and result['CHECK-12'].status=='PASS'
    packet.write_bytes(packet_original);caplog.clear();result=rows(root);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=12'),));assert result['CHECK-12'].status=='FAIL'
    path.write_bytes(original);packet.write_bytes(packet_original)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_all_profile_boundaries_and_idle

# region FUNC_test_complete_marker_task_and_provenance_population [DOMAIN(9): ConsumerPM; CONCEPT(9): FullNegativePopulation; TECH(8): pytest]
## @purpose Refuse every selected marker/task field and adopted conventions/CLAUDE provenance or instruction defect.
## @uses test_consumer_pm.fixture, test_consumer_pm.rows, test_consumer_pm.expose, consumer_files.parse_front_matter
## @io Input: owned tmp_path and caplog. Output: None after exact row failure and full expected-only error assertions.
##   Invariants: each mutation restored to original bytes and numeric mode; valid siblings remain inspected.
##   Side effects: owned fixtures only. Guarantees: selected conventions cannot evade metadata checks; optional CLAUDE is scanned if present.
##   Errors: AssertionError for omitted or unrelated failures. Example: missing task Links fails16 while missing marker fails2 independently. Importance:9.
## @complexity 7
def test_complete_marker_task_and_provenance_population(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project')
    cases=[('ROADMAP.md','`<<< WE ARE HERE`','`<<< WE ARE HERE` <<< WE ARE HERE',2),('ROADMAP.md','`<<< WE ARE HERE`','pointer\n<<< WE ARE HERE',2),('HANDOFF.md','## State','## Traps',3),('TASKS.md','**Status:** todo','**Status:** unknown',16),('TASKS.md','**Done when:** Exact note exists.','**Done when:**',16),('TASKS.md','**Stop and ask when:** Scope would change.','**Stop and ask when:**',16),('TASKS.md','**Links:** P0; VISION.md','**Links:**',16),('TASKS.md','**Status:** todo','**Status:** done',16)]
    for name,old,new,row in cases:
        caplog.clear();path=root/name;before=path.read_bytes();mode=stat.S_IMODE(path.stat().st_mode)
        try:
            path.write_bytes(before.replace(old.encode(),new.encode()));result=rows(root);print(name,row,result[f'CHECK-{row:02d}']);expose(caplog,(('orient',40,f'[IMP:10][run_checks][ROW_FAILURE] row={row}'),));assert result[f'CHECK-{row:02d}'].status=='FAIL'
        finally:path.write_bytes(before);path.chmod(mode)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    path=root/'CONVENTIONS.md';before=path.read_bytes()
    for old,new,errors in [('codex:test','<actor>',(('consumer_files',40,'[IMP:10][provenance][VALIDATION_FAILURE] cause=placeholder-provenance'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=8'))),('2020-01-01T00:00:00Z','2099-01-01T00:00:00Z',(('consumer_files',40,'[IMP:10][timestamp][VALIDATION_FAILURE] cause=future-clock'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=8'))),('type: Conventions','type:',(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=8'),))]:
        caplog.clear();path.write_bytes(before.replace(old.encode(),new.encode()));result=rows(root);print('conventions',result['CHECK-08']);expose(caplog,errors);assert result['CHECK-08'].status=='FAIL'
    path.write_bytes(before)
    claude=root/'CLAUDE.md';claude.write_text('@AGENTS.md\nDo not think carefully.\n');caplog.clear();result=rows(root);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=13'),));assert result['CHECK-13'].status=='FAIL'
    claude.write_text('@AGENTS.md\nUse the actual entry.\n');caplog.clear();result=rows(root);expose(caplog);assert result['CHECK-13'].status=='PASS'
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_complete_marker_task_and_provenance_population

# region FUNC_test_decision_reservations_duplicates_and_supersession [DOMAIN(9): ConsumerPM; CONCEPT(9): DecisionLineage; TECH(8): pytest]
## @purpose Check exact scalar amendments, unique reservations, duplicate IDs and reciprocal supersession across real owned records.
## @uses test_consumer_pm.fixture, test_consumer_pm.rows, test_consumer_pm.expose
## @io Input: owned tmp_path and caplog. Output: None after exact fixed row5/18 controls and preserved accepted body bytes.
##   Side effects: fixture decisions/task records only. Guarantees: each cited ID resolves exact record or current unique reservation; reciprocal relation required.
##   Errors: AssertionError on false-green or unrelated errors. Example: DEC-001 amended_by DEC-999 fails even with valid DEC-002 sibling. Importance:9.
## @complexity 7
def test_decision_reservations_duplicates_and_supersession(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');directory=root/'docs/decisions';directory.mkdir(parents=True)
    base='---\ntype: Decision\ntitle: Owned decision\nstatus: accepted\ngenerated: {by: codex:test, at: "2020-01-01T00:00:00Z"}\ndecided: {by: owner, at: "2020-01-01T00:00:00Z", via: "structural test channel"}\nid: ID\nEXTRA---\n# Preserved accepted body.\n'
    first=directory/'DEC-001.md';second=directory/'DEC-002.md';first.write_text(base.replace('ID','DEC-001').replace('EXTRA',''));second.write_text(base.replace('ID','DEC-002').replace('EXTRA',''))
    original=first.read_bytes();caplog.clear();first.write_text(base.replace('ID','DEC-001').replace('EXTRA','amended_by: "DEC-999: missing scalar"\n'));result=rows(root);print(result['CHECK-05']);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=5'),));assert result['CHECK-05'].status=='FAIL';first.write_bytes(original)
    duplicate=directory/'other.md';duplicate.write_bytes(original);caplog.clear();result=rows(root);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=5'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=18')));assert result['CHECK-05'].status=='FAIL' and result['CHECK-18'].status=='FAIL';duplicate.unlink()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    first.write_text(base.replace('ID','DEC-001').replace('status: accepted','status: superseded').replace('EXTRA','superseded_by: DEC-002\n'));second.write_text(base.replace('ID','DEC-002').replace('EXTRA','supersedes: DEC-001\n'));caplog.clear();result=rows(root);expose(caplog);assert result['CHECK-05'].status=='PASS'
    second.write_text(base.replace('ID','DEC-002').replace('EXTRA',''));caplog.clear();result=rows(root);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=5'),));assert result['CHECK-05'].status=='FAIL'
    first.write_bytes(original);packet=root/'TASKS.md';before=packet.read_bytes();packet.write_bytes(before+b'\n- **Reserves:** DEC-003\n');caplog.clear();result=rows(root);expose(caplog);assert result['CHECK-18'].status=='PASS'
    packet.write_bytes(before+b'\n- **Reserves:** DEC-003\n- **Reserves:** DEC-003\n');caplog.clear();result=rows(root);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=18'),));assert result['CHECK-18'].status=='FAIL'
    packet.write_bytes(before);assert first.read_bytes()==original
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_decision_reservations_duplicates_and_supersession

# region FUNC_git_fixture_command [DOMAIN(9): ConsumerPM; CONCEPT(9): OwnedHistoryEvidence; TECH(8): Git]
## @purpose Run and expose a complete actual command receipt only for a newly owned disposable Git fixture.
## @uses subprocess.run, datetime.datetime.now
## @io Input: root tmp_path-owned Path, args list[str] trusted fixture Git args, stamp optional synthetic historical commit time str.
##   Output: CompletedProcess with exit0 or AssertionError after full argv/cwd/env-names/clock/streams exposure.
##   Side effects: expressly authorized fixture-local Git writes, never real project metadata/global config/remotes.
##   Guarantees: inherited GIT variables stripped before optional literal fixture dates; timestamps remain synthetic test data.
##   Example: git_fixture_command(root,['commit','-m','Owned structural fixture'],'2020-01-01T00:00:00Z'). Importance:9.
## @complexity 3
def git_fixture_command(root,args,stamp=None):
    # START_BLOCK_Validation
    env={k:v for k,v in os.environ.items() if not k.startswith('GIT_')}
    if stamp:env.update(GIT_AUTHOR_DATE=stamp,GIT_COMMITTER_DATE=stamp)
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    process=subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,env=env)
    print({'argv':process.args,'cwd':str(root),'environmentNames':sorted(env),'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout':process.stdout,'stderr':process.stderr,'exitCode':process.returncode})
    assert process.returncode==0
    return process
    # END_BLOCK_BusinessLogic
# endregion FUNC_git_fixture_command

# region FUNC_test_layered_history_archive_and_each_layer [DOMAIN(9): ConsumerPM; CONCEPT(9): LayerPopulation, Archive; TECH(8): Git]
## @purpose Exercise real layered commit history/owner-exception recognition and retained archived-batch branch checks regardless current packet.
## @uses test_consumer_pm.git_fixture_command, test_consumer_pm.fixture, test_consumer_pm.rows, orient.git_history
## @io Input: owned tmp_path and caplog. Output: None after exact row10/17 and root-vs-flow date/budget observations.
##   Side effects: only expressly owned Git fixtures, commits/branches and records, no reset or deletion of failed history.
##   Guarantees: original cross-layer failure stays in history; current proposed packet cannot hide older merged branch; extra optional handoff headings accepted.
##   Errors: AssertionError on false result or unrelated ERROR/CRITICAL record. Example: branch at2020-01-01 predates B-001 archive2020-01-03 and fails17. Importance:9.
## @complexity 7
def test_layered_history_archive_and_each_layer(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');(root/'pm').mkdir()
    for name in ('ROADMAP.md','HANDOFF.md','TASKS.md'):(root/'pm'/name).write_bytes((root/name).read_bytes())
    agents=root/'AGENTS.md';agents.write_text(agents.read_text().replace('single-layer layer .','layered layer pm'))
    conventions=root/'CONVENTIONS.md';conventions.write_text(conventions.read_text().replace('mode: single-layer','mode: layered').replace('layer: .','layer: pm'))
    (root/'pm/HANDOFF.md').write_text((root/'pm/HANDOFF.md').read_text()+'\n## Documents\nOptional actual evidence pointer.\n')
    git_fixture_command(root,['init']);git_fixture_command(root,['config','user.name','Owned Test']);git_fixture_command(root,['config','user.email','owned'+'@'+'example.invalid']);git_fixture_command(root,['add','.']);git_fixture_command(root,['commit','-m','Owned structural bootstrap; owner exception for source test only'],'2020-01-01T00:00:00Z');git_fixture_command(root,['branch','old-task'])
    caplog.clear();result=rows(root);print(result['CHECK-10'],result['CHECK-17']);expose(caplog);assert result['CHECK-10'].status=='PASS' and result['CHECK-17'].status=='N/A'
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    notes=root/'pm/notes';notes.mkdir();(notes/'B-001-tasks.md').write_bytes((root/'pm/TASKS.md').read_bytes().replace(b'status: "proposed"',b'status: "merged"'))
    git_fixture_command(root,['add','pm/notes/B-001-tasks.md']);git_fixture_command(root,['commit','-m','Owned test archived batch'],'2020-01-03T00:00:00Z')
    caplog.clear();result=rows(root);print(result['CHECK-17']);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=17'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=17')));assert result['CHECK-17'].status=='FAIL' and 'old-task' in result['CHECK-17'].reason
    (root/'VISION.md').write_bytes((root/'VISION.md').read_bytes()+b'\nOwned root change.\n');(root/'pm/ROADMAP.md').write_bytes((root/'pm/ROADMAP.md').read_bytes()+b'\nOwned flow change.\n')
    git_fixture_command(root,['add','VISION.md','pm/ROADMAP.md']);git_fixture_command(root,['commit','-m','Owned test cross-layer negative'],'2020-01-04T00:00:00Z')
    caplog.clear();result=rows(root);print(result['CHECK-10']);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=10'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=17'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=10'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=17')));assert result['CHECK-10'].status=='FAIL'
    root_handoff=root/'HANDOFF.md';text=root_handoff.read_text().replace('Owned fixture current records; no Git revision or product consent.','2020-01-01 current.\n\n2020-01-02 previous.\n\n2020-01-03 overflow.');root_handoff.write_text(text)
    caplog.clear();result=rows(root);print(result['CHECK-21']);errors=[(record.name,record.levelno,record.getMessage()) for record in caplog.records if record.levelno>=40];print(errors)
    assert errors==[('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=10'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=17'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=21'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=10'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=17'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=21')] and result['CHECK-21'].status=='FAIL'
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_layered_history_archive_and_each_layer

# region FUNC_test_roots_file_legacy_and_local_candidate_controls [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteAssessment; TECH(8): CLI]
## @purpose Exercise roots-file real CLI and preserve unavailable legacy and invalid local-candidate statuses without pretending external comparison.
## @uses test_consumer_pm.invoke, orient.collect, orient.run_checks, test_consumer_pm.expose
## @io Input: owned tmp_path and caplog. Output: None after exact two-root labelled count, readonly bytes, legacy exit2 and local CHECK20 failure assertions.
##   Side effects: owned explicit synthetic records/roots file and readonly child; no real consent/Git effects.
##   Guarantee: C4 comparison remains unavailable but never hides invalid local status/source/outcome. Errors: AssertionError on unexpected errors/changed bytes.
##   Example: candidate status invented fails local assessment; pending with missing source fails independently. Importance9.
## @complexity 6
def test_roots_file_legacy_and_local_candidate_controls(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);first=fixture(tmp_path/'first');second=fixture(tmp_path/'second');roots=tmp_path/'roots.txt';roots.write_text(str(first)+'\n'+str(second)+'\n');before={str(path):(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for root in (first,second) for path in root.rglob('*') if path.is_file()}
    result=invoke('orient','--roots-file',roots,'--check');print(result.returncode,result.stdout,result.stderr);assert result.returncode==0 and sum(line.startswith('profile: ') for line in result.stdout.splitlines())==2
    assert {str(path):(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for root in (first,second) for path in root.rglob('*') if path.is_file()}==before
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    legacy=tmp_path/'legacy';legacy.mkdir();(legacy/'AGENTS.md').write_text('Project Conventions `1.4.0` retained historical declaration.\n');(legacy/'CONVENTIONS.md').write_text('Retained historical conventions.\n');result=invoke('orient',legacy,'--check');print(result.returncode,result.stdout,result.stderr);assert result.returncode==2 and 'legacy' in result.stdout
    (first/'notes').mkdir();candidate=first/'notes/candidate-local.md';base='---\ntype: Candidate\ntitle: Owned candidate\nstatus: STATUS\nsource: SOURCE\ngenerated: {by: codex:test, at: "2020-01-01T00:00:00Z"}\n---\nLocal lesson.\n'
    for status,source in [('invented','VISION.md'),('pending','missing.md'),('ingested','VISION.md'),('rejected','VISION.md')]:
        candidate.write_text(base.replace('STATUS',status).replace('SOURCE',source));caplog.clear();actual=rows(first);print(status,source,actual['CHECK-20']);expose(caplog,(('orient',40,'[IMP:10][run_checks][CANDIDATE_STATUS_FAILURE] count=1'),('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=20')));assert actual['CHECK-20'].status=='FAIL'
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_roots_file_legacy_and_local_candidate_controls

# region FUNC_test_three_cli_argument_payload_refusal [DOMAIN(9): ConsumerPM; CONCEPT(10): DiagnosticSafety; TECH(8): subprocess]
## @purpose Discriminate actual invalid-argument payload leakage across all three shipped CLIs while preserving help0/invalid2/usage.
## @uses subprocess.Popen, test_consumer_pm.source_fixture
## @io Input: owned tmp_path. Output: None after actual stdout/stderr/exit assertions for all six children; synthetic nonsecret sentinel built in test only.
##   Side effects: owned literal fixture and full JSON child receipts beneath tmp_path; no product source effects.
##   Guarantees: every attempt's clock/PID/argv/cwd/environment names/streams retained; no sentinel in either delivery stream.
##   Errors: AssertionError for payload echo, wrong status or missing exact safe owning diagnostic. Example: unknown --invalid sentinel never becomes error repr. Importance10.
## @complexity 5
def test_three_cli_argument_payload_refusal(tmp_path):
    # START_BLOCK_Validation
    root=source_fixture(tmp_path/'project');sentinel='C2_SYNTHETIC_'+'NONSECRET_ARGUMENT_SENTINEL';env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME')}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for name in ('orient','codemap','markup_migrate'):
        for mode in ('invalid','help'):
            argv=[sys.executable,'-B',str(SCRIPTS/(name+'.py'))]
            if mode=='help': argv+=['--help']
            else: argv+=[str(root)]+(['src/records.py'] if name=='codemap' else [])+['--invalid',sentinel]
            start=datetime.datetime.now(datetime.timezone.utc).isoformat();process=subprocess.Popen(argv,cwd=tmp_path,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);stdout,stderr=process.communicate();record={'argv':argv,'cwd':str(tmp_path),'environmentNames':sorted(env),'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':process.pid,'exitCode':process.returncode,'stdout':stdout,'stderr':stderr};(tmp_path/(name+'-'+mode+'.json')).write_text(json.dumps(record,indent=2));print(record)
            assert sentinel not in stdout+stderr and process.returncode==(0 if mode=='help' else 2)
            if mode=='invalid': assert stdout=='' and stderr.count('[IMP:10][SafeArgumentParser.error][ARGUMENT_REFUSAL] cause=invalid-arguments')==1 and 'usage:' in stderr and 'error: invalid arguments' in stderr
            else: assert 'usage:' in stdout and stderr==''
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_three_cli_argument_payload_refusal


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



# region FUNC_test_goal_purpose_supported_homes [DOMAIN(9): ConsumerPM; CONCEPT(9): ActualPurpose; TECH(8): CLI]
## @purpose Discriminate goal recovery from trailing deferred prose in ordinary, custom and layered actual homes.
## @uses test_consumer_pm.fixture, test_consumer_pm.invoke, orient.run, test_consumer_pm.expose
## @io Input: owned tmp_path and caplog. Output: None after exact independently literal purpose-line assertions in real CLI and direct orientation.
##   Side effects: synthetic owned records and child processes only; no real actor fixtures or frozen candidate writes.
##   Guarantees: frontmatter, fenced examples, audience and deferred paragraphs cannot replace a goal; absent, empty or duplicate goals remain unavailable.
##   Errors: AssertionError for wrong goal, trailing text, unexpected ERROR/CRITICAL or child status. Example: Goal and arrival criterion returns actual product goal before Deferred. Importance9.
## @complexity 6
def test_goal_purpose_supported_homes(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=fixture(tmp_path/'project');vision=root/'VISION.md'
    metadata=vision.read_text().split('---',2)[1]
    goal='Create, list and complete personal task records through a Python API.'
    body='# Pocket Queue vision\n## Goal and arrival criterion\n'+goal+'\n\nArrival requires actual API readback.\n## Audience\nIndividual developers.\n## Scope\nOne API slice.\n## Proposed architecture\nUnaccepted storage adapter.\n## Deferred on purpose\nAPI implementation awaits decisions.\n'
    vision.write_text('---'+metadata+'---\n'+body)
    expected='purpose: '+goal
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    result=invoke('orient',root,'--check');print(result.returncode,result.stdout,result.stderr)
    assert result.returncode==0 and [line for line in result.stdout.splitlines() if line.startswith('purpose: ')]==[expected] and result.stderr==''
    for name,body in [('Goal','# Vision\nGoal: '+goal+'\n## Deferred\nWrong deferred purpose.\n'),('Purpose','# Vision\n## Purpose\n'+goal+'\n## Audience\nWrong audience.\n'),('missing','# Vision\n## Deferred on purpose\nWrong deferred purpose.\n'),('empty','# Vision\n## Goal\n\n## Deferred\nWrong.\n'),('duplicate','# Vision\n## Goal\n'+goal+'\n## Purpose\nDifferent goal.\n'),('fenced','# Vision\n```markdown\n## Goal\nFake goal.\n```\n## Goal\n'+goal+'\n')]:
        vision.write_text('---'+metadata+'---\n'+body);caplog.clear();code,output=orient.run(root,True);print(name,code,output);expose(caplog)
        purpose=[line for line in output.splitlines() if line.startswith('purpose: ')]
        assert code==0 and purpose==[expected if name in ('Goal','Purpose','fenced') else 'purpose: (unavailable: '+('ambiguous goal' if name=='duplicate' else 'missing goal text')+')']
    vision.write_text('---'+metadata+'---\n'+body.replace('```markdown\n## Goal\nFake goal.\n```\n',''))
    custom=root/'charter.md';vision.rename(custom)
    conventions=root/'CONVENTIONS.md';conventions.write_text(conventions.read_text().replace('type: Conventions','homes: {vision: charter.md}\ntype: Conventions'))
    (root/'pm').mkdir()
    for name in ('ROADMAP.md','HANDOFF.md','TASKS.md'):(root/'pm'/name).write_bytes((root/name).read_bytes())
    agents=root/'AGENTS.md';agents.write_text(agents.read_text().replace('single-layer layer .','layered layer pm'))
    conventions.write_text(conventions.read_text().replace('mode: single-layer','mode: layered').replace('layer: .','layer: pm'))
    result=invoke('orient',root,'--check');print(result.returncode,result.stdout,result.stderr)
    assert result.returncode==0 and [line for line in result.stdout.splitlines() if line.startswith('purpose: ')]==[expected] and result.stderr==''
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_goal_purpose_supported_homes

# region FUNC_test_error_oracle_complete_identity [DOMAIN(9): Verification; CONCEPT(10): OwningEvent, PhysicalEvidence; TECH(8): logging, pytest]
## @purpose Reject equal-text foreign/severity substitutions and wrong message, order or cardinality using this module's actual shipped error oracle.
## @uses test_consumer_pm.expose, consumer_files.parse_front_matter, logging.FileHandler, logging.getLogger, pytest.raises
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

# region FUNC_test_generic_plan_all_adopted_layer_roots [DOMAIN(9): ConsumerPM; CONCEPT(10): CompleteLayerRoots; TECH(8): Filesystem, CLI]
## @purpose Reject generic DevelopmentPlan.md at both actual adopted layered roots and the single root while preserving legitimate checkpoint-specific plans and unadopted paths.
## @uses test_consumer_pm.fixture, test_consumer_pm.record, test_consumer_pm.expose, consumer_files.resolve_layout, orient.run_checks, orient.run, subprocess.Popen
## @io Input: owned tmp_path and real caplog. Output: None after fixed22-row/direct and actual shipped CLI0/1 assertions for single, layered pm and custom workflow roots; complete expected orient40 row9 event identity/cardinality and byte/mode readback.
##   Trigger: a forbidden generic plan exists at an actual adopted root despite a clean selected flow root. Side effects: owned synthetic records only plus full argv/cwd/envNAMES/PID/clock/stream receipts beneath tmp_path; no real consumer, Git or source writes.
##   Guarantees: declared specs/PQ1-DevelopmentPlan.md remains legal, unrelated unadopted DevelopmentPlan.md is not invented as a layer, single-root identity deduplicates, every CLI preserves all original fixture bytes/modes. Existing recursive layered two owning row9 events remain explicit, not suppressed.
##   Errors: AssertionError for false PASS, wrong22-row/CLI status, foreign/severity/error substitution or resource mutation; actual OSError setup errors fail. Example: pm is clean but root DevelopmentPlan.md must FAIL9/CLI1 with two observed orient ERROR40 events. Importance10.
## @complexity 6
def test_generic_plan_all_adopted_layer_roots(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    expected_event=('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=9')
    env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME') and not k.startswith('GIT_')};env['ORIENT_LOG']='INFO'
    wrapper="import logging,runpy,sys; logging.basicConfig(level=logging.INFO,format='%(name)s|%(levelno)d|%(message)s');sys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name='__main__')"
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for ordinal,(mode,layer_name) in enumerate([('single-layer','.'),('layered','pm'),('layered','workflow')]):
        root=fixture(tmp_path/('project'+str(ordinal)))
        if mode=='layered':
            layer=root/layer_name;layer.mkdir()
            for name in ('ROADMAP.md','HANDOFF.md','TASKS.md'):(layer/name).write_bytes((root/name).read_bytes())
            agents=root/'AGENTS.md';agents.write_text(agents.read_text().replace('single-layer layer .','layered layer '+layer_name))
            conventions=root/'CONVENTIONS.md';conventions.write_text(conventions.read_text().replace('mode: single-layer','mode: layered').replace('layer: .','layer: '+layer_name))
        else:layer=root
        layout=cf.resolve_layout(root);assert layout.root==root and layout.layer==layer
        unrelated=root/'unadopted';unrelated.mkdir();(unrelated/'DevelopmentPlan.md').write_text('# Not an adopted layer root.\n')
        specs=layout.homes['specs'];specs.mkdir(parents=True);record(specs,{'by':'codex:test','at':'2020-01-01T00:00:00Z'},'PQ1-DevelopmentPlan.md','DevelopmentPlan','# Exact checkpoint plan\nOwned checkpoint-specific plan.\n')
        roots=[root] if mode=='single-layer' else [root,layer]
        cases=[('legal',None,0)]+[('root-generic' if location==root else 'flow-generic',location,1) for location in roots]
        for label,location,expected_code in cases:
            generic=location/'DevelopmentPlan.md' if location else None
            if generic:generic.write_text('# Forbidden generic plan at adopted root.\n')
            snapshot={path.relative_to(root).as_posix():(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for path in root.rglob('*') if path.is_file()}
            try:
                caplog.clear();facts=orient.collect(root);result=orient.run_checks(facts);print(mode,label,result[8]);manifest=() if expected_code==0 else (expected_event,)*(1 if mode=='single-layer' else 2);expose(caplog,manifest)
                assert len(result)==22 and result[8].id=='CHECK-09' and result[8].status==('PASS' if expected_code==0 else 'FAIL')
                assert all(row.status in ('PASS','N/A') for row in result if row.id!='CHECK-09')
                assert 'Checked roots='+str(len(roots)) in result[8].reason and result[8].evidence==([str(root/'AGENTS.md')] if generic is None else [generic.relative_to(root).as_posix()])
                caplog.clear();code,text=orient.run(root,True);print(code,text);expose(caplog,manifest);assert code==expected_code
                argv=[sys.executable,'-B','-c',wrapper,str(SCRIPTS/'orient.py'),str(root),'--check'];start=datetime.datetime.now(datetime.timezone.utc).isoformat();process=subprocess.Popen(argv,cwd=SCRIPTS,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);stdout,stderr=process.communicate();receipt={'argv':argv,'cwd':str(SCRIPTS),'environmentNames':sorted(env),'pid':process.pid,'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exitCode':process.returncode,'stdout':stdout,'stderr':stderr};(tmp_path/(str(ordinal)+'-'+label+'.json')).write_text(json.dumps(receipt,indent=2));print(receipt)
                actual_rows=[line for line in stdout.splitlines() if line.startswith('CHECK-')];actual_errors=[line for line in stderr.splitlines() if re.match(r'^[^|]+\|(?:4[0-9]|[5-9][0-9]|[1-9][0-9]{2,})\|',line)]
                assert process.returncode==expected_code and len(actual_rows)==22 and sum(line.startswith('CHECK-09 '+('PASS' if expected_code==0 else 'FAIL')) for line in actual_rows)==1
                assert actual_errors==['orient|40|[IMP:10][run_checks][ROW_FAILURE] row=9']*len(manifest)
                assert {path.relative_to(root).as_posix():(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for path in root.rglob('*') if path.is_file()}==snapshot
                assert (specs/'PQ1-DevelopmentPlan.md').is_file() and (unrelated/'DevelopmentPlan.md').is_file()
            finally:
                if generic:generic.unlink()
        caplog.clear();assert orient.run(root,True)[0]==0;expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_generic_plan_all_adopted_layer_roots
