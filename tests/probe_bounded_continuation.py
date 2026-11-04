# region MODULE_CONTRACT [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @modulecontract
## @purpose Qualify or enforce bounded schema3 causal accounting and current evidence.
## @scope One parent writer and owned storage domain; no scheduler or product/provider calls.
## @input Explicit owned paths and parent requests; private metadata stays private and read-only.
## @output Actual JSON/CLI outcomes and discriminating assertions; no fabricated native acceptance.
## @links [USES_API(8): pathlib; USES_API(8): json]
## @invariants Historical inputs remain immutable; unknown outcomes never authorize replay.
## @rationale Structural checks complement authentic parent judgment and independent review.
## @changes
## LAST_CHANGE: [5.0.0 - CONT-BOUND direct/shipped evidence and independent-review regression controls; branch candidate only.]
## @modulemap
## FUNC 4[ module contract] => probe_bounded_continuation._module_contract
## FUNC 9[run] => probe_bounded_continuation.run
## FUNC 9[main] => probe_bounded_continuation.main
## @usecases
## - AC1–7: actual helpers exercise allowance/admission/freshness/reentry/recovery/refusal/overrun and exact own trace controls.
## - AC8/11: actual CLI emits owned streams/checkpoints; root separately performs real reserved native dispatch.
## - AC10/12: source maps and independent review are separate evidence; shared compatibility remains held.
## @GREP_SUMMARY schema3, immutable history, precharge, retry, recovery, real CLI
## @STRUCTURE explicit input → current authority → reserved entry → validated output or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import argparse
import hashlib
import json
import logging
from pathlib import Path
import shutil
import subprocess
import sys

logger = logging.getLogger(__name__)
# region FUNC_run [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Capture actual argv/stdout/stderr/exits in owned evidence and require the fixed result.
## @uses (evidence / (name + '.json')).write_text, json.dumps, json.loads, logger.error, logger.info, map, str, subprocess.run, type
## @io helper, evidence, name are explicit owned fixture/probe inputs -> decoded JSON answer or None; launches actual sys.executable helper argv in the owned check environment, writes complete argv/stdout/stderr/exit receipt at evidence/name.json, requires exact expected exit. AssertionError exposes unexpected result; no product/provider process.
## @complexity 6
def run(helper, evidence, name, *args, expected=0):
    """Capture actual argv/stdout/stderr/exits in owned evidence and require the fixed result."""
    logger.info('[IMP:4][run][START] owned observation')
    try:
        result=subprocess.run([sys.executable,str(helper),*map(str,args)],capture_output=True,text=True)
        (evidence/(name+'.json')).write_text(json.dumps({'argv':result.args,'exit':result.returncode,'stdout':result.stdout,'stderr':result.stderr},indent=2))
        assert result.returncode==expected, (name,result.stderr[-500:])
        returned = json.loads(result.stdout) if result.stdout else None
        logger.info('[IMP:9][run][RESULT] declared observations completed')
        return returned
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][run][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_run
# region FUNC_main [DOMAIN(9): Continuation; CONCEPT(9): CausalAccounting; TECH(7): Python]
## @purpose Create an absent owned workspace; qualify actual historic totals and CLI reservation/refusal.
## @uses (target / '.methodology').mkdir, (workspace / 'receipt.json').write_text, Path, Path(__file__).resolve, Path(args.legacy_native).resolve, Path(args.legacy_parent).resolve, Path(args.workspace).resolve, argparse.ArgumentParser, enumerate, evidence.mkdir, hashlib.sha256, json.dumps, json.dumps(root, sort_keys=True, separators=(',', ':')).encode, json.loads, logger.error, logger.info, p.read_bytes, p.stat, parser.add_argument, parser.parse_args, plan.write_text, print, proof.write_text, request_path.write_text, reserve.write_text, run, shutil.copy2, spec.write_text, str, target.mkdir, type, workspace.mkdir
## @io argv are explicit owned fixture/probe inputs -> int0 and JSON receipt after absent owned workspace creation (mode700), actual CLI capability/import/reservation/refusal checks and unchanged legacy bytes/modes. Existing workspace, unavailable input or unexpected CLI result raises; originals read-only. Native dispatch remains PENDING for the actual root tool, never simulated here.
## @complexity 6
def main(argv=None):
    """Create an absent owned workspace; qualify actual historic totals and CLI reservation/refusal."""
    logger.info('[IMP:4][main][START] owned observation')
    try:
        parser=argparse.ArgumentParser()
        for key in ('workspace','legacy-native','legacy-parent'):parser.add_argument('--'+key,required=True)
        args=parser.parse_args(argv)
        workspace=Path(args.workspace).resolve();workspace.mkdir(parents=True,exist_ok=False,mode=0o700)
        source=Path(__file__).resolve().parents[1]
        helper=source/'implementations/codex/skills/feature-dev/scripts/run_state.py'
        evidence=workspace/'evidence';evidence.mkdir()
        originals=[Path(args.legacy_native).resolve(),Path(args.legacy_parent).resolve()]
        before=[(p.read_bytes(),p.stat().st_mode) for p in originals]
        for i,p in enumerate(originals):shutil.copy2(p,evidence/('original-'+str(i)+'.json'))
        target=workspace/'target';target.mkdir();(target/'.methodology').mkdir()
        spec=target/'spec.md';spec.write_text('Owned inert continuation acceptance probe. No consumer/product effects.\n')
        plan=target/'plan.md';plan.write_text('Only owned .methodology/inert-marker and evidence; Code returns BLOCKED as a deliberate closure control.\n')
        proof=target/'.methodology/proof.txt';proof.write_text('Parent received implementation grant including owned inert acceptance probe.\n')
        capability=run(helper,evidence,'capabilities','capabilities')
        assert capability['schema']==3 and capability['default_cap']==4
        native=json.loads(before[0][0]);parent=json.loads(before[1][0])
        root={'kind':'legacy','target':native['target'],'run':native['run_id'],'input':native['input_identity']}
        lineage=hashlib.sha256(json.dumps(root,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        request={'project':str(target),'spec':str(spec),'framework':str(source/'implementations/codex'),'adapter':str(source/'implementations/codex/adapter.json'),'plan':str(plan),'approval':'CONT-BOUND owner implementation approval; inert probe only','run_id':'inert-code-1','phase':'code','reason':'qualify historical aggregate and one bounded inert dispatch','evidence':[str(proof)],'scope':['.methodology/inert-marker']}
        request_path=evidence/'continue-request.json';request_path.write_text(json.dumps(request))
        run(helper,evidence,'exhaustion-before-grant','continue','--predecessor',originals[0],'--parent',originals[1],'--request',request_path,expected=2)
        request['grant']={'id':'inert-one','lineage':lineage,'target':str(target),'approval':'CONT-BOUND acceptance probe only; no consumer repair','entries':1,'cost_usd':0}
        request_path.write_text(json.dumps(request))
        answer=run(helper,evidence,'continued','continue','--predecessor',originals[0],'--parent',originals[1],'--request',request_path)
        state=answer['state'];authority=Path(answer['state_file'])
        assert state['lineage']['inherited_spent']==4 and state['debug_spent']==state['debug_cap']==5
        entry=state['lineage']['active_entry'];reserve=evidence/'reserve-request.json';reserve.write_text(json.dumps({'entry':entry}))
        run(helper,evidence,'reserve-readback','reserve','--state',authority,'--request',reserve)
        run(helper,evidence,'duplicate-enrollment','continue','--predecessor',originals[0],'--parent',originals[1],'--request',request_path,expected=2)
        assert [(p.read_bytes(),p.stat().st_mode) for p in originals]==before
        receipt={'authority':str(authority),'target':str(target),'entry':entry,'spent':5,'cap':5,'historical_spent':4,'historical_cap':4,'originals_unchanged':True,'native_dispatch':'PENDING; root must use actual native tool after this reservation/readback'}
        (workspace/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps(receipt))
        returned = 0
        logger.info('[IMP:9][main][RESULT] declared observations completed')
        return returned
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as error:
        logger.error('[IMP:10][main][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC_main


if __name__=='__main__':sys.exit(main())
