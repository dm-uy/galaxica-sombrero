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
## FUNC 9[Reject equal-text foreign/severity substitutions, missing/duplicate/reordered events through the shipped oracle and real flushed sink.] => test_consumer_files.test_error_oracle_complete_identity
## FUNC 9[Import the explicitly trusted shipped helper directly without modifying sys.path.] => test_consumer_files.load
## FUNC 9[Expose all actual important records and assert the complete expected-only error population.] => test_consumer_files.expose
## FUNC 9[Create a complete explicitly synthetic adopted single-layer record fixture with real homes.] => test_consumer_files.fixture
## FUNC 9[Return all actual native checklist rows keyed by their fixed IDs.] => test_consumer_files.rows
## FUNC 9[Exercise the real shipped CLI process with complete visible streams and no Python path injection.] => test_consumer_files.invoke
## FUNC 9[Create a literal owned software fixture in current or original old-markup form.] => test_consumer_files.source_fixture
## FUNC 9[Construct only a synthetic exact-shape apply record for structural tests, never authentic human consent.] => test_consumer_files.authority
## FUNC 9[Build the real fixture Doxygen map silently and retain every original command/stream identity.] => test_consumer_files.build_map
## FUNC 9[Preserve nested generated/gate/amendment and unknown values; reject malformed duplicate/quoted/anchor metadata.] => test_consumer_files.test_metadata_nested_and_unknown_keys
## FUNC 9[Agree on the fixed complete quoted/reset/append/excluded source population and discriminate source omission.] => test_consumer_files.test_population_reset_append_quotes_exclusions
## FUNC 9[Separate YES link exclusion from armed NO external-link refusal and unreadable/unknown coverage.] => test_consumer_files.test_population_links_unknown_and_unreadable
## FUNC 9[Compare fixed independent populations for recursion/pattern reset+append/contained cycles and every secondary map lifecycle.] => test_consumer_files.test_complete_patterns_recursion_cycles_and_secondary_maps
## FUNC 9[Write one filled synthetic front-matter record in the fixture owner root.] => test_consumer_files.record
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY test_consumer_files, consumer PM, explicit paths, complete population, supported grammar, evidence
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
## @uses test_consumer_files.record, pathlib.Path.write_text, json.dumps
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
## @uses test_consumer_files.fixture, pathlib.Path.write_text
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

# region FUNC_test_metadata_nested_and_unknown_keys [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Preserve nested generated/gate/amendment and unknown values; reject malformed duplicate/quoted/anchor metadata.
## @uses consumer_files.parse_front_matter, test_consumer_files.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; literal nested generated.by=codex:test, two DEC amendment items and unknown [alpha,beta].
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_metadata_nested_and_unknown_keys(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    text='---\ngenerated:\n  by: codex:test\n  at: "2020-01-01T00:00:00Z"\ngate: {by: owner, via: "original channel", at: "2020-01-01T00:00:00Z"}\namended_by:\n  - "DEC-002: effect"\n  - "DEC-003: other"\nunknown: [alpha, beta]\n---\n'
    result=cf.parse_front_matter(text);print(result);expose(caplog)
    assert result['generated']['by']=='codex:test' and result['amended_by']==['DEC-002: effect','DEC-003: other'] and result['unknown']==['alpha','beta']
    for text,cause in [('---\na: 1\na: 2\n---\n','invalid-or-duplicate-key'),('---\na: "broken\n---\n','malformed-quoted-value'),('---\na: &shared\n---\n','unsupported-yaml-construct')]:
        caplog.clear()
        with pytest.raises(cf.ConsumerInputError): cf.parse_front_matter(text)
        expose(caplog,(('consumer_files',40,'[IMP:10][%s][VALIDATION_FAILURE] cause=%s'%('parse_front_matter' if 'duplicate' in cause else 'scalar',cause)),))
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_metadata_nested_and_unknown_keys


# region FUNC_test_population_reset_append_quotes_exclusions [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Agree on the fixed complete quoted/reset/append/excluded source population and discriminate source omission.
## @uses consumer_files.covered_sources, orient.collect, codemap.build_index, markup_migrate.build_plan, test_consumer_files.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; fixed quoted space/extra.py,src/records.py,src/support.py; excluded skip.py and INPUT reset.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_population_reset_append_quotes_exclusions(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO); root=source_fixture(tmp_path/'project')
    (root/'quoted space').mkdir();(root/'quoted space/extra.py').write_text('A=2\n'); (root/'src/skip.py').write_text('B=5\n')
    config='INPUT = absent-reset\nINPUT = src\nINPUT += "quoted space" \\\n # genuine continuation comment\nFILE_PATTERNS = *.py\nRECURSIVE = YES\nEXCLUDE = src/skip.py\nOUTPUT_DIRECTORY = map\n'
    (root/'Doxyfile').write_text(config)
    pop=cf.covered_sources(root,cf.parse_doxyfile(config)); actual=pop.files; print('actual configured',actual);expose(caplog)
    assert actual==['quoted space/extra.py','src/records.py','src/support.py']
    assert orient.collect(root)['population'].files==actual
    assert sorted(set(x['file'] for x in codemap.build_index(root)))==['src/records.py']
    assert migrate.build_plan(root,interpreters=[FLOOR,AUTHOR]).population.files==actual
    mutant=cf.covered_sources(root,cf.parse_doxyfile(config.replace('INPUT += "quoted space" \\\n # genuine continuation comment\n','')))
    assert mutant.files==['src/records.py','src/support.py'] and mutant.files!=actual
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_population_reset_append_quotes_exclusions


# region FUNC_test_population_links_unknown_and_unreadable [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Separate YES link exclusion from armed NO external-link refusal and unreadable/unknown coverage.
## @uses consumer_files.covered_sources, consumer_files.parse_doxyfile, test_consumer_files.expose
## @io Input: standard owned tmp_path Path and caplog fixture where declared; contained support.py alias plus external target, mode0 sibling and unsupported variable controls.
##   Output: None only after meaningful fixed outcome/population and complete expected-only ERROR/CRITICAL assertions.
##   Invariants: no producer-derived expectation, skipped assertion, product execution, foreign cleanup or invented human grant.
##   Side effects: only named owned fixtures and real declared CLI/map/proof/write boundaries; pure cases capture/visible stdout.
##   Guarantees: happy path rejects all errors; deliberate failure retains only exact expected owning events and original evidence.
##   Errors: AssertionError identifies regression; actual resource errors remain explicit failed evidence. Importance9.
##   Example: the literal control population above distinguishes the specified behavior from the original failure.
## @complexity 7
def test_population_links_unknown_and_unreadable(tmp_path,caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project'); (root/'src/link.py').symlink_to(root/'src/support.py')
    info=cf.parse_doxyfile((root/'Doxyfile').read_text());pop=cf.covered_sources(root,info);print(pop.files);expose(caplog)
    assert pop.files==['src/records.py','src/support.py']
    for change,cause,owner in [('external','outside-or-cyclic-path','contained'),('unreadable','not-readable-regular-file','read_text'),('unknown','unsupported-effect-construct','parse_doxyfile')]:
        caplog.clear()
        if change=='external':
            # BUG_FIX_CONTEXT: YES excludes the link, so the old negative never armed refusal.
            info=cf.parse_doxyfile((root/'Doxyfile').read_text().replace('EXCLUDE_SYMLINKS       = YES','EXCLUDE_SYMLINKS       = NO'))
            (root/'src/link.py').unlink();(root/'src/link.py').symlink_to(tmp_path/'outside.py');(tmp_path/'outside.py').write_text('X=1\n')
        if change=='unreadable':
            (root/'src/link.py').unlink();(root/'src/support.py').chmod(0)
        try:
            with pytest.raises(cf.ConsumerInputError):
                if change=='unknown': cf.parse_doxyfile('INPUT = $(ROOT)\n')
                else: cf.covered_sources(root,info)
            expose(caplog,(('consumer_files',40,f'[IMP:10][{owner}][VALIDATION_FAILURE] cause={cause}'),))
        finally: (root/'src/support.py').chmod(0o644)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_population_links_unknown_and_unreadable

# region FUNC_test_complete_patterns_recursion_cycles_and_secondary_maps [DOMAIN(9): ConsumerPM; CONCEPT(9): CompletePopulation; TECH(8): Filesystem]
## @purpose Compare fixed independent populations for recursion/pattern reset+append/contained cycles and every secondary map lifecycle.
## @uses consumer_files.covered_sources, orient.collect, codemap.source_population, markup_migrate.build_plan
## @io Input: owned tmp_path/caplog. Output: None after exact sorted paths, symlink cycle termination and separate map failure assertions.
##   Side effects: only fixture files/links; no maps built or source applied. Guarantees: root-only markup population stays separate from second map.
##   Errors: AssertionError for omitted paths or unrelated ERROR/CRITICAL events. Example: secondary map covering other/extra.py cannot hide behind empty current primary. Importance:9.
## @complexity 6
def test_complete_patterns_recursion_cycles_and_secondary_maps(tmp_path,caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO);root=source_fixture(tmp_path/'project');(root/'src/deep').mkdir();(root/'src/deep/nested.py').write_text('VALUE=3\n');(root/'src/data.txt').write_text('owned plain data\n')
    config='INPUT = src\nFILE_PATTERNS = *.absent\nFILE_PATTERNS = *.py\nFILE_PATTERNS += *.txt\nRECURSIVE = NO\nEXCLUDE_SYMLINKS = NO\nOUTPUT_DIRECTORY = map\n'
    (root/'Doxyfile').write_text(config);expected=['src/data.txt','src/records.py','src/support.py'];population=cf.covered_sources(root,cf.parse_doxyfile(config));print(population.files);expose(caplog);assert population.files==expected
    assert orient.collect(root)['population'].files==expected and codemap.source_population(root)[1].files==expected and migrate.build_plan(root,interpreters=[FLOOR,AUTHOR]).population.files==expected
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    (root/'src/deep/cycle').symlink_to(root/'src',target_is_directory=True);recursive=config.replace('RECURSIVE = NO','RECURSIVE = YES');population=cf.covered_sources(root,cf.parse_doxyfile(recursive));print('contained cycle',population.files);assert population.files==['src/data.txt','src/deep/nested.py','src/records.py','src/support.py']
    empty=root/'empty';empty.mkdir();(root/'Doxyfile').write_text('INPUT = empty\nFILE_PATTERNS = *.py\nOUTPUT_DIRECTORY = map\n')
    (root/'other').mkdir();(root/'other/extra.py').write_text('VALUE=5\n');(root/'Doxyfile.legacy').write_text('INPUT = other\nFILE_PATTERNS = *.py\nOUTPUT_DIRECTORY = legacy_map\n')
    caplog.clear();facts=orient.collect(root);result=orient.run_checks(facts);print(facts['maps'],result[14]);expose(caplog,(('orient',40,'[IMP:10][run_checks][ROW_FAILURE] row=15'),));assert [(Path(row['config']).name,row['state']) for row in facts['maps']]==[('Doxyfile','no sources yet'),('Doxyfile.legacy','not built')] and result[14].status=='FAIL'
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_complete_patterns_recursion_cycles_and_secondary_maps


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
## @uses test_consumer_files.expose, consumer_files.parse_front_matter, logging.FileHandler, logging.getLogger, pytest.raises
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
