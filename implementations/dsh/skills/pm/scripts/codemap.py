# region MODULE_CONTRACT [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteEvidence, Scope; TECH(7): Python, stdlib]
## @modulecontract
## @purpose Answer file/symbol queries with current own XML or explicitly bounded source fallback.
## @scope Read-only shared supported source population; static by-name relations, no consumer imports/build/model.
## @input Explicit project/target, configured sources/XML and authorized current map receipt.
## @output Five-line file or actual symbol blocks with own location/fields/static relations and honest0/1/2.
## @links [USES_API(9): consumer_files.covered_sources, consumer_files.repository_changes, codemap.own_xml_fields; READS_DATA_FROM(6): CODEMAP_LOG]
## @invariants
## - Unavailable required evidence is never converted to an empty clean success.
## - Explicit resources and controlling human scope remain separate from structural recognition.
## - Consumer content is never imported or executed; inherited framework inputs remain read-only.
## @rationale
## Q: Why explicit shared input boundaries?
## A: Complete populations prevent the original source omission and false-clean classes; they also expose unsupported grammar.
## Q: Why keep endpoint receipts separate from captured events?
## A: A log API call cannot prove actual file, process or map delivery.
## @changes
## LAST_CHANGE: [2.2.0 - Completed C2 causal repairs, scoped donor capacity and rich per-entity/trajectory/regression evidence.]
## @modulemap
## FUNC 9[Retain every own contract field and continuation in visible Doxygen rendering semantics.] => codemap.contract_fields
## FUNC 9[Read only comments immediately preceding the requested AST entity and decorators.] => codemap.own_contract
## FUNC 9[Bind one complete actual config-selected population for navigation.] => codemap.source_population
## FUNC 9[Separate map lifecycle from complete current receipt/index answer eligibility.] => codemap.map_state
## FUNC 9[Invert documented XML inline rendering into visible paragraph text.] => codemap.xml_text
## FUNC 9[Read all titled paragraphs only from the supplied entity own detaileddescription.] => codemap.own_xml_fields
## FUNC 9[Associate requested source file/entity location with all its own complete XML fields.] => codemap.mapped_fields
## FUNC 9[Compute the actual local package chain for a configured Python file.] => codemap.module_name
## FUNC 9[Collect finite static called names only from an entity own body.] => codemap.direct_calls
## FUNC 9[Index configured real AST entities, nested ownership and finite import aliases.] => codemap.build_index
## FUNC 9[Match the declared finite exact or dotted-suffix name query.] => codemap.match_name
## FUNC 9[Render a literal file or real symbol answer with attributable own-map/fallback evidence.] => codemap.run
## FUNC 9[Expose the shipped read-only codemap CLI with safe stderr diagnostics.] => codemap.main
## FUNC 9[Recursively attribute definitions under their real module/class/function owner.] => codemap.visit
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY codemap, consumer PM, explicit paths, complete population, supported grammar, evidence
## @STRUCTURE ▶ explicit inputs → ◇ validate supported shape → ○ own operations → ⎋ attributable result or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import argparse
import ast
import hashlib
import logging
import os
import re
import sys
import json
import io
import tokenize
import xml.etree.ElementTree as ET
from pathlib import Path
import consumer_files as cf

logger=logging.getLogger('codemap')


# region FUNC_contract_fields [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain every own contract field and continuation in visible Doxygen rendering semantics.
## @uses re.match
## @io Input: text str of one source contract. Output: dict[str,str] of ordered field paragraphs flattened by whitespace; physical list prefixes alone normalize to visible items. No field borrowing or prose word deletion. Example: two invariants retain both sentences; literal midline hyphen remains.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def contract_fields(text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][contract_fields][INIT] begin owned scoped operation')
    fields={}; current=None
    for line in text.splitlines():
        match=re.match(r'^\s*##\s*@([A-Za-z_]+)\s*(.*)',line)
        if match:
            current=match.group(1); fields.setdefault(current,[]).append(match.group(2).strip())
        elif current and re.match(r'^\s*##(?:\s|$)',line):
            # BUG_FIX_CONTEXT: Doxygen renders physical list prefixes as list structure, not visible text.
            # Strip only a real source-continuation bullet at its original line start; content remains complete.
            content=re.sub(r'^\s*##\s?','',line).rstrip()
            fields[current].append(re.sub(r'^\s*[-*+]\s+','',content))
        else: current=None
    _trajectory_return = {k:' '.join(x for x in values if x).strip() for k,values in fields.items()}; logger.debug('[IMP:3][contract_fields][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_contract_fields


# region FUNC_own_contract [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Read only comments immediately preceding the requested AST entity and decorators.
## @uses codemap.contract_fields
## @io Input: lines list[str] and FunctionDef|AsyncFunctionDef|ClassDef with actual line positions. Output: dict of own nearby fields; stops at previous end-region. Example: nested function receives its own purpose, not enclosing module fields.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def own_contract(lines,node):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][own_contract][INIT] begin owned scoped operation')
    first=min([node.lineno]+[x.lineno for x in node.decorator_list])-1
    start=first
    while start>0 and (not lines[start-1].strip() or lines[start-1].lstrip().startswith('#')):
        if lines[start-1].lstrip().startswith('# endregion'): break
        start-=1
    _trajectory_return = contract_fields('\n'.join(lines[start:first])); logger.info('[IMP:7][own_contract][OWN_SOURCE] line=%d fields=%d',node.lineno,len(_trajectory_return)); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_own_contract


# region FUNC_source_population [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Bind one complete actual config-selected population for navigation.
## @uses consumer_files.parse_doxyfile, consumer_files.read_text, consumer_files.covered_sources
## @io Input: root str|Path. Output: (DoxyfileInfo,Population) from root/Doxyfile. Raises ConsumerInputError/OSError for required configuration or coverage gaps. Example: excluded files are absent from Population but remain queryable only as attributed source fallback.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def source_population(root):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][source_population][INIT] begin owned scoped operation')
    root=Path(root).resolve(); info=cf.parse_doxyfile(cf.read_text(root/'Doxyfile'))
    _trajectory_return = info,cf.covered_sources(root,info); logger.info('[IMP:7][source_population][COMPLETE_POPULATION] sources=%d status=%s',len(_trajectory_return[1].files),_trajectory_return[1].coverage_status); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_source_population


# region FUNC_map_state [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Separate map lifecycle from complete current receipt/index answer eligibility.
## @uses codemap.source_population, xml.etree.ElementTree.fromstring, consumer_files.identity, consumer_files.timestamp
## @io Input: root str|Path. Output: dict root/config/population/index/eligible bool/lifecycle/reason/xml/cache. Current byte/mode/config/index/actual silent build receipt required; requested fields still checked separately. Broken/unavailable receipt sets eligible false; required coverage errors propagate. Example: newer source forbids map answer even if uncommitted lifecycle is in progress.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def map_state(root):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][map_state][INIT] begin owned scoped operation')
    root=Path(root).resolve(); info,population=source_population(root)
    index=cf.contained(root,cf.contained(root,(info.settings.get('OUTPUT_DIRECTORY') or ['doxygen_output'])[0])/(info.settings.get('XML_OUTPUT') or ['xml'])[0]/'index.xml')
    state={'root':root,'config':info,'population':population,'index':index,'eligible':False,'lifecycle':'unavailable','reason':'No current complete build receipt','xml':None,'cache':{}}
    if not population.files:
        state['lifecycle']='no sources yet'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
    if not index.is_file():
        state['lifecycle']='not built'; state['reason']='Map not built'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
    newer=[x for x in population.files if (root/x).stat().st_mtime_ns>index.stat().st_mtime_ns]
    state['lifecycle']='stale' if newer else 'fresh'
    if newer:
        # BUG_FIX_CONTEXT: lifecycle in-progress is distinct from current complete answer eligibility.
        observation=cf.repository_changes(root)
        if observation is not None and all(path in observation['changed'] for path in newer): state['lifecycle']='in progress'
        state['reason']='Map older than covered source; lifecycle '+state['lifecycle']+' never certifies current answer'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
    try:
        # Index first; individual compounds are read only on a requested own location.
        state['xml']=ET.fromstring(cf.read_text(index))
        receipt=json.loads(cf.read_text(root/'.methodology/maps/current.json'))
        expected={'path':'Doxyfile','sha256':cf.identity(root/'Doxyfile')['sha256']}
        if receipt.get('config')!=expected or receipt.get('sources')!=population.source_identities or receipt.get('index')!={'path':index.relative_to(root).as_posix(),'sha256':cf.identity(index)['sha256']}:
            state['reason']='Receipt config/source/index content identity mismatch'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
        build=receipt.get('build',{})
        if build.get('exitCode')!=0 or not build.get('argv') or Path(build.get('cwd','')).resolve()!=root or not build.get('at') or not build.get('stdout') or not build.get('stderr'):
            state['reason']='Incomplete actual build receipt'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
        cf.timestamp(build['at'])
        if cf.read_text(cf.contained(root,build['stdout'])) or cf.read_text(cf.contained(root,build['stderr'])):
            state['reason']='Build streams are not silent'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
    except (cf.ConsumerInputError,ET.ParseError,OSError,ValueError):
        state['reason']='Missing, broken or unavailable current receipt/index'; _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
    state['eligible']=True; state['reason']='Current complete receipt/index; own fields still checked per query'
    logger.info('[IMP:9][map_state][CURRENT] covered=%d',len(population.files))
    _trajectory_return = state; logger.info('[IMP:9][map_state][ASSESSMENT] eligible=%s lifecycle=%s reason=%s',state['eligible'],state['lifecycle'],state['reason']); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_map_state


# region FUNC_xml_text [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Invert documented XML inline rendering into visible paragraph text.
## @uses xml.etree.ElementTree.Element
## @io Input: element Element|None. Output: str; None empty, computeroutput backticks, ndash --, mdash ---, forced spaces one space, other visible text retained. No filesystem effects. Example: code span containing a yields backtick-a-backtick; bold/list formatting is irreversible.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:3 for pure visible-text rendering; no readiness or field completeness verdict.
## @complexity 3
def xml_text(element):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][xml_text][INIT] begin owned scoped operation')
    if element is None: _trajectory_return = ''; logger.debug('[IMP:3][xml_text][RETURN] owned result evaluated'); return _trajectory_return
    result=element.text or ''
    for child in element:
        if child.tag=='computeroutput': value='`'+xml_text(child)+'`'
        elif child.tag=='ndash': value='--'
        elif child.tag=='mdash': value='---'
        elif child.tag in ('sp','linebreak'): value=' '
        else: value=xml_text(child)
        result+=value+(child.tail or '')
    _trajectory_return = result; logger.debug('[IMP:3][xml_text][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_xml_text


# region FUNC_own_xml_fields [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Read all titled paragraphs only from the supplied entity own detaileddescription.
## @uses codemap.xml_text
## @io Input: entity Element and aliases dict[str,str] with actual named paragraph titles. Output: dict field->complete visible own paragraph text; absent description {}. No neighboring description read. Example: invariants para1 and para2 are joined, retaining both.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def own_xml_fields(entity,aliases):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][own_xml_fields][INIT] begin owned scoped operation')
    description=entity.find('detaileddescription'); result={}
    titles={name:re.sub(r'<[^>]*>','',value.split('@par',1)[-1].replace('^^','')).strip().rstrip(':') for name,value in aliases.items() if '@par' in value}
    if description is None: _trajectory_return = result; logger.info('[IMP:7][own_xml_fields][OWN_PARAGRAPHS] fields=%d',len(_trajectory_return)); return _trajectory_return
    for section in description.iter('simplesect'):
        title=xml_text(section.find('title')).strip().rstrip(':')
        for name,wanted in titles.items():
            if title==wanted:
                result[name]=' '.join(xml_text(p).strip() for p in section.findall('para')).strip()
    _trajectory_return = result; logger.info('[IMP:7][own_xml_fields][OWN_PARAGRAPHS] fields=%d',len(_trajectory_return)); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_own_xml_fields


# region FUNC_mapped_fields [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Associate requested source file/entity location with all its own complete XML fields.
## @uses codemap.own_xml_fields, xml.etree.ElementTree.fromstring, consumer_files.read_text
## @io Input: state current map_state dict; rel contained relative str; line positive int for entity, zero module sentinel; expected own field dict; module bool. Output: (dict|None,reason str). Refuses incomplete/foreign/mismatched own paragraphs, unsafe/broken requested compounds or absent entity; caches relevant compounds only. Example: lost invariant returns None despite current index.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def mapped_fields(state,rel,line,expected,module=False):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][mapped_fields][INIT] begin owned scoped operation')
    if not state['eligible']: _trajectory_return = None,state['reason']; logger.info('[IMP:9][mapped_fields][OWN_ASSOCIATION] mapped=%s fields=%d reason=%s',_trajectory_return[0] is not None,len(_trajectory_return[0] or {}),_trajectory_return[1]); return _trajectory_return
    candidates=[]
    for item in state['xml'].findall('compound'):
        if item.get('kind') not in ('namespace','class','file'): continue
        ref=item.get('refid','')
        if not re.fullmatch(r'[A-Za-z0-9_-]+',ref): _trajectory_return = None,'Unsafe compound identity'; logger.info('[IMP:9][mapped_fields][OWN_ASSOCIATION] mapped=%s fields=%d reason=%s',_trajectory_return[0] is not None,len(_trajectory_return[0] or {}),_trajectory_return[1]); return _trajectory_return
        # Namespace/class name is a finite narrowing before bounded compound reads.
        stem=Path(rel).stem
        if item.get('kind')=='file' and Path(item.findtext('name','')).name!=Path(rel).name: continue
        if item.get('kind')=='namespace' and stem not in item.findtext('name','').split('::'): continue
        candidates.append(item)
    for item in candidates:
        ref=item.get('refid'); path=state['index'].parent/(ref+'.xml')
        try:
            if ref not in state['cache']: state['cache'][ref]=ET.fromstring(cf.read_text(path))
            tree=state['cache'][ref]
        except (cf.ConsumerInputError,ET.ParseError): _trajectory_return = None,'Requested compound broken/unavailable'; logger.info('[IMP:9][mapped_fields][OWN_ASSOCIATION] mapped=%s fields=%d reason=%s',_trajectory_return[0] is not None,len(_trajectory_return[0] or {}),_trajectory_return[1]); return _trajectory_return
        for entity in list(tree.iter('memberdef'))+list(tree.iter('compounddef')):
            location=entity.find('location')
            if location is None: continue
            located=location.get('file','').replace('\\','/')
            if not (located==rel or located.endswith('/'+rel)): continue
            if module:
                if entity.findtext('name')!='_module_contract' or (line and int(location.get('line','0'))!=line): continue
            elif int(location.get('line','0'))!=line: continue
            fields=own_xml_fields(entity,state['config'].aliases)
            # Every source-own field must have its own full paragraph; neighboring entities never qualify.
            required={k:v for k,v in expected.items() if k in state['config'].aliases and k!='modulecontract'}
            normalization=lambda x:re.sub(r'\s+',' ',x).strip()
            if not required or any(k not in fields or normalization(v)!=normalization(fields[k]) for k,v in required.items()):
                _trajectory_return = None,'Own full paragraph/content mismatch; rendering may be irreversible'; logger.info('[IMP:9][mapped_fields][OWN_ASSOCIATION] mapped=%s fields=%d reason=%s',_trajectory_return[0] is not None,len(_trajectory_return[0] or {}),_trajectory_return[1]); return _trajectory_return
            _trajectory_return = fields,'Current own XML location and fields; bold/list formatting irreversibility disclosed'; logger.info('[IMP:9][mapped_fields][OWN_ASSOCIATION] mapped=%s fields=%d reason=%s',_trajectory_return[0] is not None,len(_trajectory_return[0] or {}),_trajectory_return[1]); return _trajectory_return
    _trajectory_return = None,'Own entity not mapped at current file/location'; logger.info('[IMP:9][mapped_fields][OWN_ASSOCIATION] mapped=%s fields=%d reason=%s',_trajectory_return[0] is not None,len(_trajectory_return[0] or {}),_trajectory_return[1]); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_mapped_fields


# region FUNC_module_name [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Compute the actual local package chain for a configured Python file.
## @uses pathlib.Path
## @io Input: root resolved Path and path contained Path. Output: dotted str from package-initializer ancestors and stem; an initializer names its package. Reads only package-file existence. Example: pkg/api.py with pkg/__init__.py yields pkg.api.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def module_name(root,path):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][module_name][INIT] begin owned scoped operation')
    path=Path(path); parts=[] if path.stem=='__init__' else [path.stem]; directory=path.parent
    while directory!=root and (directory/'__init__.py').is_file():
        parts.insert(0,directory.name); directory=directory.parent
    _trajectory_return = '.'.join(parts); logger.debug('[IMP:3][module_name][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_module_name


# region FUNC_direct_calls [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Collect finite static called names only from an entity own body.
## @uses ast.iter_child_nodes
## @io Input: body list[ast.stmt]. Output: sorted deduplicated str call names; nested definitions/lambdas excluded. No dynamic or imported-code execution. Example: outer calling nested while nested calls foo returns only nested for outer.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def direct_calls(body):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][direct_calls][INIT] begin owned scoped operation')
    names=set(); stack=list(body)
    while stack:
        node=stack.pop()
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef,ast.Lambda)): continue
        if isinstance(node,ast.Call):
            target=node.func; parts=[]
            while isinstance(target,ast.Attribute): parts.insert(0,target.attr); target=target.value
            if isinstance(target,ast.Name): parts.insert(0,target.id); names.add('.'.join(parts))
        stack.extend(ast.iter_child_nodes(node))
    _trajectory_return = sorted(names); logger.debug('[IMP:3][direct_calls][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_direct_calls


# region FUNC_build_index [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Index configured real AST entities, nested ownership and finite import aliases.
## @uses codemap.source_population, codemap.visit, codemap.module_name, consumer_files.read_text, ast.parse
## @io Input: root str|Path. Output: sorted list[{name,short,file,line,kind,calls,fields}] for functions/async/classes/nested/control-flow definitions. No consumer import. Raises ConsumerInputError on any unparseable covered Python relation population. Example: async outer.inner is attributed to inner body, not outer.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def build_index(root):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][build_index][INIT] begin owned scoped operation')
    root=Path(root).resolve(); info,population=source_population(root); result=[]
    logger.info('[IMP:4][build_index][INIT] supported actual AST population')
    for rel in population.files:
        if not rel.endswith('.py'): continue
        text=cf.read_text(root/rel); lines=text.splitlines()
        try: tree=ast.parse(text)
        except SyntaxError: cf.fail('build_index','unparseable-relation-population')
        aliases={}
        for node in tree.body:
            if isinstance(node,ast.ImportFrom):
                base=node.module or ''
                if node.level:
                    parts=module_name(root,root/rel).split('.')[:-node.level];base='.'.join(parts+([base] if base else []))
                for alias in node.names:
                    if alias.name!='*': aliases[alias.asname or alias.name]=base+'.'+alias.name if base else alias.name
        visit(root,rel,lines,result,tree.body,module_name(root,root/rel)+'.',aliases)
    logger.info('[IMP:9][build_index][RESULT] definitions=%d',len(result))
    _trajectory_return = sorted(result,key=lambda x:(x['file'],x['line'])); logger.debug('[IMP:3][build_index][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_build_index


# region FUNC_match_name [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Match the declared finite exact or dotted-suffix name query.
## @uses str.endswith
## @io Input: query/name str. Output: bool true only exact or name suffix dot+query. No dynamic resolution. Example: summarize matches records.summarize; records.summarize does not match support.summarize.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def match_name(query,name):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][match_name][INIT] begin owned scoped operation')
    _trajectory_return = name==query or name.endswith('.'+query); logger.debug('[IMP:3][match_name][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_match_name


# region FUNC_run [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Render a literal file or real symbol answer with attributable own-map/fallback evidence.
## @uses codemap.map_state, codemap.build_index, codemap.mapped_fields
## @io Input: project str|Path, target str contained file or dotted/plain symbol. Output: (exit int0|1|2,text str); five file lines, source second, missing fields (none); ambiguous symbol blocks sorted. Classes disclose relation absence; static names labeled by name. Reads only; ConsumerInputError/OSError/parse gaps converted to safe2. Example: missing symbol1 only after complete supported population.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def run(project,target):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][run][INIT] begin owned scoped operation')
    root=Path(project).resolve()
    try:
        state=map_state(root)
        candidate=Path(target)
        file_query=candidate.is_absolute() or '/' in target or target.endswith('.py')
        if file_query:
            path=cf.contained(root,candidate)
            if not path.is_file(): _trajectory_return = 1,'codemap: not found\n'; logger.info('[IMP:9][run][ANSWER] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
            text=cf.read_text(path); rel=path.relative_to(root).as_posix(); fields={}; anchor_line=0
            try:
                tree=ast.parse(text); anchors=[node for node in tree.body if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name=='_module_contract']
                if len(anchors)==1: anchor_line=anchors[0].lineno; fields=own_contract(text.splitlines(),anchors[0])
                if not fields:
                    for token in tokenize.generate_tokens(io.StringIO(text).readline):
                        if token.type==tokenize.COMMENT:
                            match=re.fullmatch(r'#\s*(GREP_SUMMARY|STRUCTURE):\s*(.*)',token.string)
                            if match: fields[match.group(1)]=match.group(2)
            except (SyntaxError,tokenize.TokenError,IndentationError): cf.fail('run','unparseable-file-contract')
            mapped,reason=mapped_fields(state,rel,anchor_line,fields,module=True) if anchor_line and rel in state['population'].files else (None,'File excluded from configured map or missing unique own module anchor')
            output=mapped if mapped is not None else fields; source='Doxygen: '+reason if mapped is not None else 'source fallback: '+reason
            _trajectory_return = 0,'\n'.join([f'file: {rel}',f'source: {source}']+[f'{k}: {output.get(k) or "(none)"}' for k in ('GREP_SUMMARY','STRUCTURE','purpose')])+'\n'; logger.info('[IMP:9][run][ANSWER] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
        index=build_index(root); matches=[x for x in index if match_name(target,x['name']) or target==x['short']]
        if not matches: _trajectory_return = 1,'codemap: not found\n'; logger.info('[IMP:9][run][ANSWER] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
        output=[]
        if len(matches)>1: output.append('matches: %d'%len(matches))
        for item in matches:
            fields,reason=mapped_fields(state,item['file'],item['line'],item['fields'])
            actual=fields if fields is not None else item['fields']; source='Doxygen: '+reason if fields is not None else 'source fallback: '+reason
            output.extend(['symbol: '+item['name'],'source: '+source,'defined: %s:%d'%(item['file'],item['line']),'purpose: '+(actual.get('purpose') or '(none)')])
            declared=[x.strip() for x in actual.get('uses','').split(',') if x.strip()]; output.append('declared (%d):'%len(declared)); output.extend('  '+x for x in declared)
            if item['kind']=='class': output.append('relations: classes not recorded; absence proves no non-instantiation'); continue
            callers=[x['name'] for x in index if x!=item and any(match_name(call,item['name']) or call==item['short'] for call in x['calls'])]
            callees=sorted(set(x['name'] for x in index if x!=item and any(match_name(call,x['name']) or call==x['short'] for call in item['calls'])))
            for label,values in (('callers',sorted(set(callers))),('callees',callees)):
                output.append('%s (%d):'%(label,len(values))); output.extend('  '+x+' (by name)' for x in values)
        _trajectory_return = 0,'\n'.join(output)+'\n'; logger.info('[IMP:9][run][ANSWER] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
    except (cf.ConsumerInputError,OSError,ValueError,ET.ParseError) as error:
        logger.error('[IMP:10][run][UNAVAILABLE] kind=%s',type(error).__name__); _trajectory_return = 2,'codemap: unavailable: '+type(error).__name__+'\n'; logger.info('[IMP:9][run][ANSWER] exit=%d lines=%d',_trajectory_return[0],len(_trajectory_return[1].splitlines())); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_run


# region FUNC_main [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Expose the shipped read-only codemap CLI with safe stderr diagnostics.
## @uses consumer_files.SafeArgumentParser, codemap.run, logging.basicConfig
## @io Input: argv list[str]|None. Output: exit0|1|2 and actual stdout answer, stderr on unavailable2; CODEMAP_LOG selects diagnostics. No source/build/model mutation. Raises argparse SystemExit0 for help/2 for invalid args. Example: codemap.py PROJECT src/a.py prints exactly five answer lines.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def main(argv=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][main][INIT] begin owned scoped operation')
    parser=cf.SafeArgumentParser(); parser.add_argument('project'); parser.add_argument('target'); args=parser.parse_args(argv)
    logging.basicConfig(level=getattr(logging,os.environ.get('CODEMAP_LOG','WARNING').upper(),logging.WARNING),format='%(message)s',stream=sys.stderr)
    code,text=run(args.project,args.target)
    print(text,end='',file=sys.stderr if code==2 else sys.stdout); _trajectory_return = code; logger.debug('[IMP:3][main][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_main



# region FUNC_visit [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Recursively attribute definitions under their real module/class/function owner.
## @uses codemap.direct_calls, codemap.own_contract, ast.iter_child_nodes
## @io Input: root resolved Path, rel contained relative str, lines complete physical source rows list[str], result owned list[entity dict]; internal build_index only;  nodes list[ast.stmt], prefix dotted str with terminal dot, inherited_aliases dict[str,str] copied per owner; supplied aliases/result/lines/rel owned. Output: None; appends each definition once with own calls and fields. No consumer execution. Example: class C.method indexes module.C.method.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def visit(root,rel,lines,result,nodes,prefix,inherited_aliases):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][visit][INIT] begin owned scoped operation')
    for node in nodes:
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            name=prefix+node.name; calls=direct_calls(node.body) if not isinstance(node,ast.ClassDef) else []
            # BUG_FIX_CONTEXT: ast.walk included nested bindings, falsely shadowing an outer import alias.
            # Scope-local imports/arguments/stores affect only this entity; nested bodies own their own bindings.
            own=[];pending=list(node.body)
            while pending:
                child=pending.pop()
                if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef,ast.Lambda)): continue
                own.append(child);pending.extend(ast.iter_child_nodes(child))
            assigned={child.id for child in own if isinstance(child,ast.Name) and isinstance(child.ctx,(ast.Store,ast.Del))}
            if not isinstance(node,ast.ClassDef): assigned|={argument.arg for argument in node.args.posonlyargs+node.args.args+node.args.kwonlyargs+([node.args.vararg] if node.args.vararg else [])+([node.args.kwarg] if node.args.kwarg else [])}
            local_aliases=dict(inherited_aliases)
            for child in own:
                if isinstance(child,ast.ImportFrom) and child.module:
                    base=child.module
                    if child.level:
                        parts=module_name(root,root/rel).split('.')[:-child.level];base='.'.join(parts+[base])
                    for alias in child.names:
                        if alias.name!='*': local_aliases[alias.asname or alias.name]=base+'.'+alias.name
            owned_aliases={key:value for key,value in local_aliases.items() if key not in assigned}
            calls=[owned_aliases.get(call.split('.')[0],call.split('.')[0])+('.'+'.'.join(call.split('.')[1:]) if '.' in call else '') for call in calls]
            result.append({'name':name,'short':node.name,'file':rel,'line':node.lineno,'kind':'class' if isinstance(node,ast.ClassDef) else 'function','calls':sorted(set(calls)),'fields':own_contract(lines,node)})
            visit(root,rel,lines,result,node.body,name+'.',owned_aliases)
        else:
            for attr in ('body','orelse','finalbody'):
                value=getattr(node,attr,None)
                if isinstance(value,list): visit(root,rel,lines,result,value,prefix,inherited_aliases)
            for handler in getattr(node,'handlers',[]): visit(root,rel,lines,result,handler.body,prefix,inherited_aliases)
    # END_BLOCK_BusinessLogic
# endregion FUNC_visit


if __name__=='__main__':
    raise SystemExit(main())
