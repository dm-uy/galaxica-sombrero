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
## FUNC 9[Reject equal-text foreign/severity substitutions, missing/duplicate/reordered events through the shipped oracle and real flushed sink.] => test_markup_migrate.test_error_oracle_complete_identity
## FUNC 9[Import the explicitly trusted shipped helper directly without modifying sys.path.] => test_markup_migrate.load
## FUNC 9[Expose all actual important records and assert the complete expected-only error population.] => test_markup_migrate.expose
## FUNC 9[Create a complete explicitly synthetic adopted single-layer record fixture with real homes.] => test_markup_migrate.fixture
## FUNC 9[Return all actual native checklist rows keyed by their fixed IDs.] => test_markup_migrate.rows
## FUNC 9[Exercise the real shipped CLI process with complete visible streams and no Python path injection.] => test_markup_migrate.invoke
## FUNC 9[Create a literal owned software fixture in current or original old-markup form.] => test_markup_migrate.source_fixture
## FUNC 9[Construct only a synthetic exact-shape apply record for structural tests, never authentic human consent.] => test_markup_migrate.authority
## FUNC 9[Build the real fixture Doxygen map silently and retain every original command/stream identity.] => test_markup_migrate.build_map
## FUNC 9[Retain same-line alias spans/custom order while repairing effective block closers right-to-left.] => test_markup_migrate.test_same_line_alias_offsets_and_effective_reset
## FUNC 9[Require actual COMMENT/noncomment-token/whole-AST proofs on both installed Python versions.] => test_markup_migrate.test_real_comment_ast_proofs_each_interpreter
## FUNC 9[Leave triple-quoted comment-shaped literal untouched and retain unmovable no-anchor report.] => test_markup_migrate.test_migration_no_anchor_external_and_literals
## FUNC 9[Reject a stale full population before any requested source replacement.] => test_markup_migrate.test_migration_apply_scope_current_bytes_and_links
## FUNC 9[Retain exact actual OS partial effects and full original recovery when later staging is denied.] => test_markup_migrate.test_migration_late_write_receipt_and_recovery
## FUNC 9[Deliver real preview/check/apply bytes/modes/receipt and clean second check plus rebuilt own map.] => test_markup_migrate.test_migration_real_cli_dry_check_apply_idempotence
## FUNC 9[Qualify only actual relation targets across package/nested blocks and retain prose/literals/endings on both interpreters.] => test_markup_migrate.test_relation_blocks_packages_nested_prose_and_endings
## FUNC 9[Refuse missing/forged/out-of-scope/tampered/stale-mode and internal-recovery requests before every source write.] => test_markup_migrate.test_all_preflight_failures_leave_every_original
## FUNC 9[Retain failed parse/interpreter proof populations and prevent every valid sibling from being applied.] => test_markup_migrate.test_failed_sibling_and_missing_interpreter_prevent_apply
## FUNC 9[Mark a real completed replacement as unknown when its required readback becomes unavailable, retaining recovery without replay.] => test_markup_migrate.test_actual_replace_unknown_readback_retains_effects
## FUNC 9[Preserve deliberate safe custom titles and honor an empty reset while refusing unsafe known block closure.] => test_markup_migrate.test_custom_titles_empty_reset_and_unsafe_alias_refusal
## FUNC 9[Prove zero-change apply writes no source and final receipt failure never yields APPLIED after actual completed effects.] => test_markup_migrate.test_zero_change_apply_and_final_receipt_failure
## FUNC 9[Refuse a real source byte change after staging and before replace, preserving the independently changed target and original recovery.] => test_markup_migrate.test_pre_replace_actual_race_refuses_candidate_write
## FUNC 9[Write one filled synthetic front-matter record in the fixture owner root.] => test_markup_migrate.record
## FUNC 9[Inject only the required unavailable readback after a real replacement, preserving all other actual reads.] => test_markup_migrate.unavailable_after_replacement
## FUNC 9[Raise only for the actual final APPLIED receipt replacement, allowing all real source and earlier evidence writes.] => test_markup_migrate.fail_final_receipt
## FUNC 9[Create the actual requested staging file, then inject one owned source change only at the source staging boundary.] => test_markup_migrate.change_after_stage
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY test_markup_migrate, consumer PM, explicit paths, complete population, supported grammar, evidence
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
import functools

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
## @uses test_markup_migrate.record, pathlib.Path.write_text, json.dumps
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
## @uses test_markup_migrate.fixture, pathlib.Path.write_text
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

# region FUNC_test_same_line_alias_offsets_and_effective_reset [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain same-line alias spans/custom order while repairing effective block closers right-to-left.
## @uses markup_migrate.migrate_doxyfile, test_markup_migrate.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; discarded first reset, two active aliases with distinct titles and unknown custom alias.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_same_line_alias_offsets_and_effective_reset(caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);seed='ALIASES = "invariants=@par Invariants:" "changes=@par Change Summary:"\n';old='INPUT = src\nALIASES = "discarded=@par Old:^^"\nALIASES = "invariants=@par Invariants:^^" "changes=@par Change Summary:^^" "custom=@par Custom:^^"\n'
    new,items=migrate.migrate_doxyfile(old,seed);print(new,items);expose(caplog)
    info=cf.parse_doxyfile(new);assert info.aliases=={'invariants':'@par Invariants:','changes':'@par Change Summary:','custom':'@par Custom:^^'} and items['changed aliases']==['invariants','changes']
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_same_line_alias_offsets_and_effective_reset


# region FUNC_test_real_comment_ast_proofs_each_interpreter [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Require actual COMMENT/noncomment-token/whole-AST proofs on both installed Python versions.
## @uses markup_migrate.build_plan, markup_migrate.verify_change, test_markup_migrate.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; old legacy count fixture under3.9.6 and3.12.13; executable2->18 negative.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_real_comment_ast_proofs_each_interpreter(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR]);print(plan.identity,plan.items);expose(caplog);assert plan.changes and not plan.items['violations']
    proofs=[p for x in plan.changes for p in x.proofs];assert {p['version'].split('.')[0:2][1] for p in proofs}=={'9','12'} and all(p['ok'] and p['tokensEqual'] and p['astEqual'] for p in proofs)
    caplog.clear();proof=migrate.verify_change('records.py','VALUE=2\n','VALUE=18\n',FLOOR);expose(caplog,(('markup_migrate',40,'[IMP:10][verify_change][PROOF_FAILURE] kind=token-or-AST'),));assert not proof['ok']
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_real_comment_ast_proofs_each_interpreter


# region FUNC_test_migration_no_anchor_external_and_literals [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Leave triple-quoted comment-shaped literal untouched and retain unmovable no-anchor report.
## @uses markup_migrate.build_plan, markup_migrate.run, test_markup_migrate.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; real legacy records.py plus triple string and support.py legacy tag without metadata anchor.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_migration_no_anchor_external_and_literals(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);literal='\nTEXT = """\n# GREP_SUMMARY: do not change string\n"""\n';(root/'src/records.py').write_text((root/'src/records.py').read_text()+literal)
    (root/'src/support.py').write_text('# region MODULE_CONTRACT\n# GREP_SUMMARY: no anchor\nVALUE=11\n')
    plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR]);print(plan.items);expose(caplog);assert plan.items['no_anchor']==['src/support.py'] and literal in next(x for x in plan.changes if x.path=='src/records.py').new
    code,text=migrate.run(root,'check',interpreters=[FLOOR,AUTHOR]);assert code==1 and 'migration due' in text
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_migration_no_anchor_external_and_literals


# region FUNC_test_migration_apply_scope_current_bytes_and_links [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Reject a stale full population before any requested source replacement.
## @uses markup_migrate.write_changes, test_markup_migrate.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; frozen Doxyfile/records.py grant while support.py changes from11 to24.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_migration_apply_scope_current_bytes_and_links(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);files=['Doxyfile','src/records.py'];plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);before={x:(root/x).read_bytes() for x in plan.originals}
    grant=authority(plan,files);(root/'src/support.py').write_text('VALUE=24\n');caplog.clear();receipt=migrate.write_changes(root,plan,files=files,authority=grant,receipt_dir=tmp_path/'recovery');print(receipt)
    expose(caplog,(('consumer_files',40,'[IMP:10][write_changes][VALIDATION_FAILURE] cause=stale-population'),('markup_migrate',40,'[IMP:10][write_changes][APPLY_FAILURE] completed=0 unknown=0 kind=ConsumerInputError')));assert receipt.status=='REFUSED' and not receipt.completed and all((root/x).read_bytes()==before[x] for x in files)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_migration_apply_scope_current_bytes_and_links


# region FUNC_test_migration_late_write_receipt_and_recovery [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain exact actual OS partial effects and full original recovery when later staging is denied.
## @uses markup_migrate.write_changes, test_markup_migrate.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; sorted Doxyfile first, records.py later under actual readonly src parent mode0555.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_migration_late_write_receipt_and_recovery(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);files=['Doxyfile','src/records.py'];plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);grant=authority(plan,files)
    # Actual OS read-only parent causes later same-directory stage failure after sorted Doxyfile replacement.
    (root/'src').chmod(0o555)
    try:
        caplog.clear();receipt=migrate.write_changes(root,plan,files=files,authority=grant,receipt_dir=tmp_path/'recovery');print(receipt)
        expose(caplog,(('markup_migrate',40,'[IMP:10][write_changes][APPLY_FAILURE] completed=1 unknown=0 kind=PermissionError'),));assert receipt.completed==['Doxyfile'] and receipt.unwritten==['src/records.py'] and receipt.status=='PARTIAL'
        for change in plan.changes:
            original=Path(receipt.recovery[change.path]['path']);assert original.read_bytes()==change.old.encode() and stat.S_IMODE(original.stat().st_mode)==change.mode
    finally:(root/'src').chmod(0o755)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_migration_late_write_receipt_and_recovery


# region FUNC_test_migration_real_cli_dry_check_apply_idempotence [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Deliver real preview/check/apply bytes/modes/receipt and clean second check plus rebuilt own map.
## @uses markup_migrate.main, codemap.run, test_markup_migrate.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; two explicit changed leaves with both proof interpreters, exact-shape synthetic grant and outside recovery.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_migration_real_cli_dry_check_apply_idempotence(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);files=['Doxyfile','src/records.py'];before={str(p):p.read_bytes() for p in root.rglob('*') if p.is_file()};result=invoke('markup_migrate',root,'--python',FLOOR,'--python',AUTHOR);assert result.returncode==0 and '--- a/src/records.py' in result.stdout
    result=invoke('markup_migrate',root,'--check','--python',FLOOR,'--python',AUTHOR);assert result.returncode==1 and {str(p):p.read_bytes() for p in root.rglob('*') if p.is_file()}==before
    plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);grant=tmp_path/'grant.json';grant.write_text(json.dumps(authority(plan,files)))
    result=invoke('markup_migrate',root,'--apply','--file','Doxyfile','--file','src/records.py','--python',FLOOR,'--python',AUTHOR,'--approval-record',grant,'--receipt-dir',tmp_path/'recovery');print(result.stdout);assert result.returncode==0
    for change in plan.changes:assert (root/change.path).read_bytes()==change.new.encode() and stat.S_IMODE((root/change.path).stat().st_mode)==change.mode
    result=invoke('markup_migrate',root,'--check','--python',FLOOR,'--python',AUTHOR);assert result.returncode==0 and 'up to date' in result.stdout
    build_map(root);code,text=codemap.run(root,'src/records.py');print(text);assert code==0 and 'source: Doxygen:' in text
    expose(caplog)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_migration_real_cli_dry_check_apply_idempotence

# region FUNC_test_relation_blocks_packages_nested_prose_and_endings [DOMAIN(9): Migration; CONCEPT(9): SemanticTokens, PhysicalRows; TECH(8): tokenize]
## @purpose Qualify only actual relation targets across package/nested blocks and retain prose/literals/endings on both interpreters.
## @uses markup_migrate.build_plan, markup_migrate.verify_change, test_markup_migrate.source_fixture, test_markup_migrate.expose
## @io Input: owned tmp_path and caplog. Output: None after exact qualified targets/prose/stale/diff and both-version proof assertions.
##   Side effects: fixture files and trusted text-only child proofs. No apply. Invariants: metadata is not invented; ambiguous/external symbols remain.
##   Guarantees: form-feed/Unicode remain physical-row content; no-final-newline and CRLF survive; stale uses is information only.
##   Errors: AssertionError for any wrong target or unexpected ERROR/CRITICAL event. Example: Helper.method becomes pkg.mod.Helper.method while prose word method stays. Importance:9.
## @complexity 7
def test_relation_blocks_packages_nested_prose_and_endings(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');package=root/'src/pkg';package.mkdir();(package/'__init__.py').write_text('')
    text='# region MODULE_CONTRACT\r\n## @modulecontract\r\n## @purpose Retain every physical row.\r\n## @links [USES_API(8): Helper.method; READS_DATA_FROM(7): external.provider]\r\n## @modulemap\r\n## CLASS 8[Helper method prose stays] => Helper\r\ndef _module_contract():\r\n    pass\r\n# endregion MODULE_CONTRACT\r\n\r\nclass Helper:\r\n    def method(self):\r\n        def inner():\r\n            return 18\r\n        return inner()\r\n\r\n## @uses Helper.method described method remains,\r\n##   external.provider\r\ndef caller():\r\n    return 2\r\n\r\n# GREP_SUMMARY: preserve Unicode … and formfeed\fhere\r\n# STRUCTURE: <count> to result'
    path=package/'mod.py';path.write_bytes(text.encode());plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR]);change=next(change for change in plan.changes if change.path=='src/pkg/mod.py');print(plan.items,change.new);expose(caplog)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    assert 'USES_API(8): pkg.mod.Helper.method' in change.new and '=> pkg.mod.Helper' in change.new
    assert 'Helper method prose stays' in change.new and 'described method remains' in change.new and 'external.provider' in change.new
    assert '## @STRUCTURE 〈count〉 to result\r\n' in change.new and '\fhere' in change.new and '…' in change.new and not change.new.endswith(('\r','\n'))
    assert plan.items['stale uses info']==['src/pkg/mod.py:caller:pkg.mod.Helper.method']
    assert all(proof['ok'] and proof['astEqual'] and proof['tokensEqual'] and proof['pid']>0 and proof['start'] and proof['end'] and proof['environmentNames'] for proof in change.proofs)
    rendered=migrate.render(plan);print(rendered);assert '\r\n' in rendered and '\fhere' in rendered and '\\ No newline at end of file' in rendered
    assert path.read_bytes()==text.encode()
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_relation_blocks_packages_nested_prose_and_endings

# region FUNC_test_all_preflight_failures_leave_every_original [DOMAIN(9): Migration; CONCEPT(10): ZeroWrites; TECH(8): Filesystem]
## @purpose Refuse missing/forged/out-of-scope/tampered/stale-mode and internal-recovery requests before every source write.
## @uses markup_migrate.build_plan, markup_migrate.write_changes, test_markup_migrate.authority, test_markup_migrate.expose
## @io Input: owned tmp_path, caplog. Output: None after exact REFUSED/completed0 and complete before-after bytes/modes assertions for each control.
##   Invariants: fresh fixture per cause; no restored foreign state or blind replay. Side effects: fixture setup only; rejected apply source effects0.
##   Guarantees: full plan integrity covers comment edits as well as AST; stale numeric mode is a source identity change.
##   Errors: AssertionError for writes or unrelated ERROR/CRITICAL events. Example: forged approved=true fails exact record shape. Importance:10.
## @complexity 7
def test_all_preflight_failures_leave_every_original(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    cases=[('missing','missing-exact-parent-authenticated-record'),('scope','scope-or-proof-not-ready'),('payload','changed-plan-payload'),('mode','stale-population'),('config','stale-config-template'),('inside','recovery-inside-threat'),('scope-type','invalid-exact-file-scope'),('scope-duplicate','invalid-exact-file-scope'),('grant-type','missing-exact-parent-authenticated-record'),('link','stale-population'),('leaf-type','stale-population')]
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for ordinal,(kind,cause) in enumerate(cases):
        root=source_fixture(tmp_path/('project'+str(ordinal)),True);files=['Doxyfile','src/records.py'];plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);grant=authority(plan,files);scope=files;receipt_dir=tmp_path/('recovery'+str(ordinal))
        if kind=='missing': grant={'approved':True}
        if kind=='scope': scope=['Doxyfile']
        if kind=='payload': next(change for change in plan.changes if change.path.endswith('.py')).new+='\n# forged comment\n'
        if kind=='mode': (root/'src/support.py').chmod(0o600)
        if kind=='config': (root/'Doxyfile').write_bytes((root/'Doxyfile').read_bytes()+b'\n# later change\n')
        if kind=='inside': receipt_dir=root/'recovery'
        if kind=='scope-type': scope='src/records.py'
        if kind=='scope-duplicate': scope=files+['Doxyfile']
        if kind=='grant-type': grant['files']=[False]
        if kind=='link': (root/'src/support.py').unlink();(root/'src/support.py').symlink_to(root/'src/records.py')
        if kind=='leaf-type': (root/'src/support.py').unlink();(root/'src/support.py').mkdir()
        before={str(path.relative_to(root)):(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for path in root.rglob('*') if path.is_file()}
        links={str(path.relative_to(root)):os.readlink(path) for path in root.rglob('*') if path.is_symlink()}
        caplog.clear();receipt=migrate.write_changes(root,plan,files=scope,authority=grant,receipt_dir=receipt_dir);print(kind,receipt)
        expose(caplog,(('consumer_files',40,f'[IMP:10][write_changes][VALIDATION_FAILURE] cause={cause}'),('markup_migrate',40,'[IMP:10][write_changes][APPLY_FAILURE] completed=0 unknown=0 kind=ConsumerInputError')))
        assert receipt.status=='REFUSED' and receipt.completed==[] and receipt.unknown==[]
        assert {str(path.relative_to(root)):os.readlink(path) for path in root.rglob('*') if path.is_symlink()}==links
        assert {str(path.relative_to(root)):(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for path in root.rglob('*') if path.is_file()}==before
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_all_preflight_failures_leave_every_original

# region FUNC_test_failed_sibling_and_missing_interpreter_prevent_apply [DOMAIN(9): Migration; CONCEPT(10): AllProofs; TECH(8): Python]
## @purpose Retain failed parse/interpreter proof populations and prevent every valid sibling from being applied.
## @uses markup_migrate.build_plan, markup_migrate.write_changes, test_markup_migrate.authority, test_markup_migrate.expose
## @io Input: owned tmp_path and caplog. Output: None after violated Plan/REFUSED0/full byte-mode equality assertions.
##   Side effects: setup and trusted interpreter child; no source apply. Guarantees: missing executable cannot silently narrow both-version proof.
##   Errors: AssertionError on any changed sibling or unrelated errors. Example: valid records.py plus invalid support.py produces not_parsed and no apply. Importance:10.
## @complexity 5
def test_failed_sibling_and_missing_interpreter_prevent_apply(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);(root/'src/support.py').write_text('def broken(:\n');before={str(path.relative_to(root)):(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for path in root.rglob('*') if path.is_file()}
    plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR]);print(plan.items);expose(caplog);assert plan.items['not_parsed']==['src/support.py'] and 'src/support.py:parse-failure' in plan.items['violations']
    caplog.clear();files=['Doxyfile','src/records.py'];receipt=migrate.write_changes(root,plan,files=files,authority=authority(plan,files),receipt_dir=tmp_path/'recovery');expose(caplog,(('consumer_files',40,'[IMP:10][write_changes][VALIDATION_FAILURE] cause=scope-or-proof-not-ready'),('markup_migrate',40,'[IMP:10][write_changes][APPLY_FAILURE] completed=0 unknown=0 kind=ConsumerInputError')));assert receipt.status=='REFUSED' and receipt.completed==[]
    assert {str(path.relative_to(root)):(path.read_bytes(),stat.S_IMODE(path.stat().st_mode)) for path in root.rglob('*') if path.is_file()}==before
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    caplog.clear();proof=migrate.verify_change('records.py','# old\n','# new\n',str(tmp_path/'missing-python'));print(proof);expose(caplog,(('markup_migrate',40,'[IMP:10][verify_change][PROOF_FAILURE] kind=interpreter-unavailable'),));assert proof['ok'] is False and proof['exitCode']==2 and proof['start'] and proof['end']
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_failed_sibling_and_missing_interpreter_prevent_apply

# region FUNC_test_actual_replace_unknown_readback_retains_effects [DOMAIN(9): Migration; CONCEPT(10): UnknownEffect; TECH(8): os.replace]
## @purpose Mark a real completed replacement as unknown when its required readback becomes unavailable, retaining recovery without replay.
## @uses markup_migrate.write_changes, test_markup_migrate.authority, pathlib.Path.read_bytes
## @io Input: owned tmp_path, caplog, monkeypatch readback fault. Output: None after actual sink/recovery comparison and exact unknown receipt.
##   Side effects: real scoped replacements in owned fixture; one injected readback error after the actual replacement.
##   Guarantees: completed first file retained, unknown second is never falsely unwritten/APPLIED. Error: AssertionError on wrong effect or unrelated trace.
##   Example: Doxyfile completed, records.py physically new but unreadable to writer => PARTIAL unknown records.py. Importance:10.
## @complexity 5
def test_actual_replace_unknown_readback_retains_effects(tmp_path,caplog,monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);files=['Doxyfile','src/records.py'];plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);change=next(change for change in plan.changes if change.path=='src/records.py');actual_read=Path.read_bytes
    monkeypatch.setattr(Path,'read_bytes',functools.partialmethod(unavailable_after_replacement,actual_read,root,change))
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    caplog.clear();receipt=migrate.write_changes(root,plan,files=files,authority=authority(plan,files),receipt_dir=tmp_path/'recovery');print(receipt);expose(caplog,(('markup_migrate',40,'[IMP:10][write_changes][APPLY_FAILURE] completed=1 unknown=1 kind=OSError'),))
    assert receipt.status=='PARTIAL' and receipt.completed==['Doxyfile'] and receipt.unwritten==[] and receipt.unknown==['src/records.py']
    assert actual_read(root/'src/records.py')==change.new.encode()
    for item in plan.changes: assert actual_read(Path(receipt.recovery[item.path]['path']))==item.old.encode()
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_actual_replace_unknown_readback_retains_effects

# region FUNC_test_custom_titles_empty_reset_and_unsafe_alias_refusal [DOMAIN(9): Migration; CONCEPT(9): EffectiveAliases; TECH(8): Doxygen]
## @purpose Preserve deliberate safe custom titles and honor an empty reset while refusing unsafe known block closure.
## @uses markup_migrate.migrate_doxyfile, consumer_files.parse_doxyfile, test_markup_migrate.expose
## @io Input: caplog. Output: None after exact effective aliases/custom bytes/violation assertions.
##   Side effects: none; full config strings transformed in memory. Guarantees: inactive old definitions cannot count as present or make current safe config invalid.
##   Errors: AssertionError on lost custom title or unrelated ERROR/CRITICAL event. Example: ALIASES= clears old aliases before missing seed append. Importance:9.
## @complexity 4
def test_custom_titles_empty_reset_and_unsafe_alias_refusal(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);seed='ALIASES = "invariants=@par Invariants:" "purpose=@par Purpose:^^"\n'
    old='INPUT = src\nALIASES = "invariants=@par Discarded:^^"\nALIASES =\nALIASES += "invariants=@par Domain invariants:" "custom=@par Custom:^^"\n'
    new,items=migrate.migrate_doxyfile(old,seed);print(new,items);expose(caplog)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    assert 'ALIASES = "invariants=@par Discarded:^^"' in new and not items['violations']
    assert cf.parse_doxyfile(new).aliases=={'invariants':'@par Domain invariants:','custom':'@par Custom:^^','purpose':'@par Purpose:^^'}
    unsafe='INPUT = src\nALIASES = "invariants=@par Domain invariants:^^"\n';new,items=migrate.migrate_doxyfile(unsafe,seed);print(items);expose(caplog);assert new.startswith(unsafe) and 'unsafe-custom-known-alias:invariants' in items['violations']
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_custom_titles_empty_reset_and_unsafe_alias_refusal

# region FUNC_test_zero_change_apply_and_final_receipt_failure [DOMAIN(9): Migration; CONCEPT(10): DurableEffects; TECH(8): Filesystem]
## @purpose Prove zero-change apply writes no source and final receipt failure never yields APPLIED after actual completed effects.
## @uses markup_migrate.build_plan, markup_migrate.write_changes, test_markup_migrate.authority, os.replace
## @io Input: owned tmp_path, caplog, monkeypatch final receipt replacement only. Output: None after exact completed/status/durable-history/source-byte assertions.
##   Side effects: two owned projects/recovery roots; actual scoped source replacements. Guarantee: previous WRITING receipt preserved when final APPLIED receipt cannot persist.
##   Errors: AssertionError for false success or unrelated ERROR/CRITICAL; actual injected PermissionError is isolated to final evidence delivery.
##   Example: current fixture changes0 -> APPLIED completed[]; legacy fixture effects2 plus failed final receipt -> PARTIAL completed2. Importance10.
## @complexity 6
def test_zero_change_apply_and_final_receipt_failure(tmp_path,caplog,monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'clean');files=['Doxyfile','src/records.py'];plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);assert plan.changes==[]
    before={path:(root/path).read_bytes() for path in plan.originals};receipt=migrate.write_changes(root,plan,files=files,authority=authority(plan,files),receipt_dir=tmp_path/'clean-recovery');print(receipt);expose(caplog)
    assert receipt.status=='APPLIED' and receipt.completed==[] and receipt.unwritten==[] and all((root/path).read_bytes()==value for path,value in before.items())
    root=source_fixture(tmp_path/'old',True);plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);directory=tmp_path/'failed-final-recovery';real_replace=os.replace
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    monkeypatch.setattr(os,'replace',functools.partial(fail_final_receipt,directory,real_replace));caplog.clear();receipt=migrate.write_changes(root,plan,files=files,authority=authority(plan,files),receipt_dir=directory);print(receipt);expose(caplog,(('markup_migrate',40,'[IMP:10][save][RECEIPT_FAILURE] kind=OSError'),))
    assert receipt.status=='PARTIAL' and receipt.completed==['Doxyfile','src/records.py'] and receipt.unwritten==[] and receipt.unknown==[]
    assert 'persistence unavailable' in receipt.reason and json.loads((directory/'receipt.json').read_text())['status']=='WRITING'
    assert all((root/change.path).read_bytes()==change.new.encode() for change in plan.changes)
    assert not any('[APPLIED]' in record.getMessage() for record in caplog.records)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_zero_change_apply_and_final_receipt_failure

# region FUNC_test_pre_replace_actual_race_refuses_candidate_write [DOMAIN(9): Migration; CONCEPT(10): Race; TECH(8): Filesystem]
## @purpose Refuse a real source byte change after staging and before replace, preserving the independently changed target and original recovery.
## @uses markup_migrate.write_changes, test_markup_migrate.authority, tempfile.mkstemp
## @io Input: owned tmp_path, caplog, monkeypatch stage boundary. Output: None after REFUSED0, exact actor-change bytes, safe errors and full original recovery.
##   Side effects: owned setup/recovery/stage and one explicitly synthetic concurrent-source byte change; writer source effects0.
##   Guarantee: comparison immediately before os.replace catches the race; no rollback erases the independent changed bytes.
##   Errors: AssertionError on overwritten target or unrelated ERROR/CRITICAL. Example: stage created then actor appends # later; pending candidate is not installed. Importance10.
## @complexity 5
def test_pre_replace_actual_race_refuses_candidate_write(tmp_path,caplog,monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project',True);files=['src/records.py'];plan=migrate.build_plan(root,interpreters=[FLOOR,AUTHOR],files=files);grant=authority(plan,files);target=root/'src/records.py';old=target.read_bytes();later=old+b'\n# Independently changed owned actor bytes.\n';real_stage=migrate.tempfile.mkstemp
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    monkeypatch.setattr(migrate.tempfile,'mkstemp',functools.partial(change_after_stage,real_stage,target,later));caplog.clear();receipt=migrate.write_changes(root,plan,files=files,authority=grant,receipt_dir=tmp_path/'recovery');print(receipt);expose(caplog,(('consumer_files',40,'[IMP:10][write_changes][VALIDATION_FAILURE] cause=pre-replace-stale-original'),('markup_migrate',40,'[IMP:10][write_changes][APPLY_FAILURE] completed=0 unknown=0 kind=ConsumerInputError')))
    assert receipt.status=='REFUSED' and receipt.completed==[] and receipt.unknown==[] and receipt.unwritten==files
    assert target.read_bytes()==later and Path(receipt.recovery['src/records.py']['path']).read_bytes()==old
    assert not list(target.parent.glob('.markup-stage-*'))
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_pre_replace_actual_race_refuses_candidate_write


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




# region FUNC_unavailable_after_replacement [DOMAIN(9): Migration; CONCEPT(10): ReadbackFailure; TECH(8): pathlib]
## @purpose Inject only the required unavailable readback after a real replacement, preserving all other actual reads.
## @uses pathlib.Path.read_bytes, OSError, functools.partialmethod
## @io Input: actual_read saved real Path reader, root owned Path, change actual FileChange; path passed through method descriptor;  path Path. Output: original bytes except actual changed records target raises OSError after observed new bytes.
##   Side effects: reads only; no fake replacement. Guarantee: owning test can still independently inspect actual sink through saved reader.
##   Error: OSError only for the fixed new byte payload. Example: old records bytes return normally; new bytes trigger once per read. Importance10.
## @complexity 2
def unavailable_after_replacement(path,actual_read,root,change):
    # START_BLOCK_BusinessLogic
    value=actual_read(path)
    if path==root/'src/records.py' and value==change.new.encode(): raise OSError('owned readback fault')
    return value
    # END_BLOCK_BusinessLogic
# endregion FUNC_unavailable_after_replacement




# region FUNC_fail_final_receipt [DOMAIN(9): Migration; CONCEPT(10): ReceiptFailure; TECH(8): os.replace]
## @purpose Raise only for the actual final APPLIED receipt replacement, allowing all real source and earlier evidence writes.
## @uses os.replace, json.loads, pathlib.Path.read_text, functools.partial
## @io Input: directory owned recovery Path, real_replace saved actual os.replace; injected source effects remain real;  src/dst path-like pair. Output: real os.replace result except final owned APPLIED payload raises PermissionError.
##   Side effects: delegated actual replace; no fake source effects. Guarantee: READY/WRITING remain durable.
##   Errors: isolated PermissionError for final receipt; test restores monkeypatch. Example: WRITING receipt replaces normally. Importance10.
## @complexity 3
def fail_final_receipt(directory,real_replace,src,dst):
    # START_BLOCK_BusinessLogic
    if Path(dst)==directory/'receipt.json' and json.loads(Path(src).read_text())['status']=='APPLIED': raise PermissionError('owned final receipt fault')
    return real_replace(src,dst)
    # END_BLOCK_BusinessLogic
# endregion FUNC_fail_final_receipt




# region FUNC_change_after_stage [DOMAIN(9): Migration; CONCEPT(10): RaceControl; TECH(8): tempfile]
## @purpose Create the actual requested staging file, then inject one owned source change only at the source staging boundary.
## @uses tempfile.mkstemp, pathlib.Path.write_bytes, functools.partial
## @io Input: real_stage saved real mkstemp, target owned source Path, later independently changed bytes;  positional/keyword actual mkstemp arguments. Output: real (fd,path); target changes only for .markup-stage- prefix.
##   Side effects: actual temp file and owned synthetic actor source edit. Guarantee: receipt staging remains unaffected; no fake writer replacement.
##   Errors: original OS errors propagate. Example: .receipt- never changes target. Importance10.
## @complexity 2
def change_after_stage(real_stage,target,later,*args,**kwargs):
    # START_BLOCK_BusinessLogic
    result=real_stage(*args,**kwargs)
    if kwargs.get('prefix')=='.markup-stage-': target.write_bytes(later)
    return result
    # END_BLOCK_BusinessLogic
# endregion FUNC_change_after_stage



# region FUNC_test_error_oracle_complete_identity [DOMAIN(9): Verification; CONCEPT(10): OwningEvent, PhysicalEvidence; TECH(8): logging, pytest]
## @purpose Reject equal-text foreign/severity substitutions and wrong message, order or cardinality using this module's actual shipped error oracle.
## @uses test_markup_migrate.expose, consumer_files.parse_front_matter, logging.FileHandler, logging.getLogger, pytest.raises
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
