# region MODULE_CONTRACT [DOMAIN(9): ConsumerPM; CONCEPT(9): CompleteEvidence, Scope; TECH(7): Python, stdlib]
## @modulecontract
## @purpose Preview and prove scoped comment/alias migration before any authorized per-file source replacement.
## @scope No implicit Git/build/adoption; every supplied interpreter mandatory; recovery outside threat, honest partial effects.
## @input Explicit root/scope/template/interpreters and parent-authenticated exact authority/recovery resources.
## @output Complete Plan, actual token/AST proof streams, diff and ApplyReceipt completed/unwritten/unknown.
## @links [USES_API(9): consumer_files.covered_sources, markup_migrate.verify_change, markup_migrate.write_changes; READS_DATA_FROM(6): MARKUP_MIGRATE_LOG]
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
## CLASS 9[Retain complete immutable-by-contract original/new text, mode and interpreter proofs.] => markup_migrate.FileChange
## CLASS 9[Carry the full source/config/template/interpreter proof population before any apply.] => markup_migrate.Plan
## CLASS 9[Retain actual per-file completed/unwritten/unknown effects and recovery.] => markup_migrate.ApplyReceipt
## FUNC 9[Identify physical rows whose first nonspace token is an actual COMMENT.] => markup_migrate.comment_rows
## FUNC 9[Index actual package/module/class/nested definitions with same-file resolution provenance.] => markup_migrate.definitions
## FUNC 9[Transform only real comment relation/tag spans while retaining literal and ambiguous content.] => markup_migrate.migrate_python
## FUNC 9[Repair owned alias spans right-to-left and validate the effective reset/append result.] => markup_migrate.migrate_doxyfile
## FUNC 9[Produce real installed-interpreter COMMENT/token/AST equality proof before source writes.] => markup_migrate.verify_change
## FUNC 9[Bind complete planned text, exact originals/config/template, interpreter proof results and violations deterministically.] => markup_migrate.plan_identity
## FUNC 9[Freeze complete actual source/config/template originals and every supplied interpreter proof.] => markup_migrate.build_plan
## FUNC 9[Recheck every proof/original/scope, preserve outside recovery and atomically replace each owned regular leaf with honest partial failure effects.] => markup_migrate.write_changes
## FUNC 9[Print every stable report category and the exact planned byte-faithful unified diff.] => markup_migrate.render
## FUNC 9[Route readonly preview/check or exact scoped apply with complete honest effects.] => markup_migrate.run
## FUNC 9[Expose the shipped migration CLI with dry-run default and explicit guarded apply.] => markup_migrate.main
## FUNC 9[Persist the current exact effects atomically inside the newly owned recovery directory.] => markup_migrate.save
## @usecases
## - [declared APIs]: Consumer custodian -> supply actual bounded resources -> inspect complete attributable results.
## - [failure paths]: Independent verifier -> supply unsupported or stale input -> retain refusal evidence.
## @GREP_SUMMARY markup_migrate, consumer PM, explicit paths, complete population, supported grammar, evidence
## @STRUCTURE ▶ explicit inputs → ◇ validate supported shape → ○ own operations → ⎋ attributable result or refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import argparse
import datetime
import time
import ast
import difflib
import hashlib
import io
import json
import logging
import os
import re
import stat
import subprocess
import sys
import tempfile
import tokenize
from dataclasses import dataclass, field
from pathlib import Path
import consumer_files as cf

logger=logging.getLogger('markup_migrate')
CATEGORIES=('qualified','unresolved','moved tags','no_anchor','brackets','split block tags','listed','stale uses info','changed aliases','added aliases','kept aliases','not_parsed','violations')
PROOF_PROGRAM=r'''
import ast,difflib,io,json,sys,tokenize,hashlib
p=json.load(sys.stdin); a=p['old']; b=p['new']
def lines(s):
 return io.StringIO(s,newline=None).readlines()
def tokens(s):
 return list(tokenize.generate_tokens(io.StringIO(s,newline=None).readline))
def comments(s):
 ls=lines(s)
 return {t.start[0]-1 for t in tokens(s) if t.type==tokenize.COMMENT and not ls[t.start[0]-1][:t.start[1]].strip()}
def noncomments(s):
 return [(x.type,x.string) for x in tokens(s) if x.type not in (tokenize.COMMENT,tokenize.NL,tokenize.NEWLINE,tokenize.ENDMARKER)]
try:
 ca=comments(a); cb=comments(b); old=lines(a); new=lines(b); bad=[]
 for tag,i,j,k,l in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
  if tag!='equal':
   bad.extend(('old',x+1) for x in range(i,j) if x not in ca)
   bad.extend(('new',x+1) for x in range(k,l) if x not in cb)
 ast_equal=ast.dump(ast.parse(a),include_attributes=False)==ast.dump(ast.parse(b),include_attributes=False)
 token_equal=noncomments(a)==noncomments(b)
 result={'ok':not bad and ast_equal and token_equal,'changedNoncomments':bad,'astEqual':ast_equal,'tokensEqual':token_equal,'version':sys.version.split()[0]}
except (SyntaxError,IndentationError,tokenize.TokenError,ValueError) as e:
 result={'ok':False,'error':type(e).__name__,'version':sys.version.split()[0]}
print(json.dumps(result,sort_keys=True)); sys.exit(0 if result['ok'] else 2)
'''

# region CLASS_FileChange [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain complete immutable-by-contract original/new text, mode and interpreter proofs.
## @uses dataclasses.dataclass
## @io Input: path relative str; old/new complete str; mode int0..4095; original_identity dict sha256/mode; proofs list real interpreter records. Output: same named fields; construction itself authorizes no write. Example: one changed comment retains exact CRLF old/new texts.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class FileChange:
    path: str
    old: str
    new: str
    mode: int
    original_identity: dict
    proofs: list = field(default_factory=list)
# endregion CLASS_FileChange

# region CLASS_Plan [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Carry the full source/config/template/interpreter proof population before any apply.
## @uses dataclasses.dataclass
## @io Input: root Path; population Population; config/template identities; template_path str; interpreters list[str]; changes list[FileChange]; items categories dict[str,list[str]]; originals dict relative->identity; identity SHA256 str. Output same fields; caller treats as frozen. Example: invalid sibling remains violations even when another change is valid.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class Plan:
    root: Path
    population: object
    config_identity: dict
    template_path: str
    template_identity: dict
    interpreters: list
    changes: list
    items: dict
    originals: dict
    identity: str = ''
# endregion CLASS_Plan

# region CLASS_ApplyReceipt [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Retain actual per-file completed/unwritten/unknown effects and recovery.
## @uses dataclasses.dataclass
## @io Input: completed/unwritten/unknown relative str lists; recovery dict path->backup/mode/SHA; status READY|WRITING|APPLIED|REFUSED|PARTIAL; safe reason/path str. Output: same fields; no multi-file transactional guarantee. Example: first replaced, second denied yields completed first and unwritten second.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
@dataclass
class ApplyReceipt:
    completed: list
    unwritten: list
    unknown: list
    recovery: dict
    status: str
    reason: str
    path: str
# endregion CLASS_ApplyReceipt


# region FUNC_comment_rows [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Identify physical rows whose first nonspace token is an actual COMMENT.
## @uses tokenize.generate_tokens, io.StringIO
## @io Input: text complete Python str. Output: set[int>=0] physical zero-based rows using only CR/LF/CRLF splitting. Raises tokenizer/indentation/syntax errors on unsupported text. Example: # inside a triple-quoted string is absent.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def comment_rows(text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][comment_rows][INIT] begin owned scoped operation')
    lines=io.StringIO(text,newline=None).readlines()
    _trajectory_return = {x.start[0]-1 for x in tokenize.generate_tokens(io.StringIO(text,newline=None).readline) if x.type==tokenize.COMMENT and not lines[x.start[0]-1][:x.start[1]].strip()}; logger.debug('[IMP:3][comment_rows][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_comment_rows


# region FUNC_definitions [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Index actual package/module/class/nested definitions with same-file resolution provenance.
## @uses ast.iter_child_nodes, pathlib.Path
## @io Input: root Path and parsed dict[relative str,ast.Module]. Output: dict token->sorted unique (rel,qualified) pairs, including module prefixes and nested ownership. Reads only package-initializer existence. Example: method C.m gets pkg.mod.C.m, never pkg.mod.m.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def definitions(root,parsed):
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: a flat ast.walk lost Class.method/nested ownership and omitted module prefixes.
    logger.info('[IMP:4][definitions][INIT] begin owned scoped operation')
    result={}
    for rel,tree in parsed.items():
        path=root/rel; module=[] if path.stem=='__init__' else [path.stem]; parent=path.parent
        while parent!=root and (parent/'__init__.py').is_file(): module.insert(0,parent.name); parent=parent.parent
        prefix='.'.join(module)
        for depth in range(1,len(module)+1):
            name='.'.join(module[:depth]); result.setdefault(name,[]).append((rel,name))
        stack=[(tree,prefix)]
        while stack:
            node,owner=stack.pop()
            for child in ast.iter_child_nodes(node):
                if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
                    qualified=owner+'.'+child.name if owner else child.name
                    result.setdefault(child.name,[]).append((rel,qualified)); result.setdefault(qualified,[]).append((rel,qualified))
                    stack.append((child,qualified))
                else: stack.append((child,owner))
    for name in result: result[name]=sorted(set(result[name]))
    logger.info('[IMP:9][definitions][RESULT] names=%d',len(result))
    _trajectory_return = result; logger.debug('[IMP:3][definitions][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic

# endregion FUNC_definitions


# region FUNC_migrate_python [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Transform only real comment relation/tag spans while retaining literal and ambiguous content.
## @uses markup_migrate.comment_rows, markup_migrate.definitions, io.StringIO, re
## @io Input: rel relative str; text complete str; tree ast.Module parsed from identical text; index definitions dict. Output: (new str,categories dict), scoped qualification/legacy relocation/genuine block splits/listed risky prose/stale info. No write; no missing markup generated. Errors tokenizer/AST coordinate violations propagate before apply. Example: wrapped uses target qualifies while description words stay exact.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def migrate_python(rel,text,tree,index):
    # START_BLOCK_Validation
    logger.info('[IMP:4][migrate_python][INIT] begin owned scoped operation')
    lines=io.StringIO(text,newline='').readlines(); comments=comment_rows(text); items={k:[] for k in CATEGORIES}
    ending='\r\n' if '\r\n' in text else '\r' if '\r' in text and '\n' not in text else '\n'
    anchor=next((x for x in tree.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef)) and x.name=='_module_contract'),None)
    region=next((i for i,line in enumerate(lines) if i in comments and re.match(r'^# region MODULE_CONTRACT\b',line)),None)
    old=[(i,re.match(r'^#(?!#)\s*(GREP_SUMMARY|STRUCTURE):\s*(.*)',line.rstrip('\r\n'))) for i,line in enumerate(lines) if i in comments]
    old=[(i,m) for i,m in old if m]
    if old and (anchor is None or region is None or region>=anchor.lineno-1):
        items['no_anchor'].append(rel); _trajectory_return = text,items; logger.debug('[IMP:3][migrate_python][RETURN] owned result evaluated'); return _trajectory_return
    logger.info('[IMP:9][migrate_python][TOKEN_VALID] comment rows=%d',len(comments))
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: regex over every prose word qualified unrelated descriptions and lost wrapped relations.
    # Extract only semantic relation targets with original physical coordinates; use package/nested index.
    replacements={}; blocks=[]; i=0
    while i<len(lines):
        match=re.match(r'^(\s*##\s*)@(uses|links|modulemap)\b(.*)',lines[i]) if i in comments else None
        if not match: i+=1; continue
        tag=match.group(2); segments=[(i,match.start(3),match.group(3).rstrip('\r\n'))]; j=i+1
        while j<len(lines) and j in comments:
            continuation=re.match(r'^(\s*##)(?!\s*@)(.*)',lines[j])
            if not continuation or not continuation.group(2).strip(): break
            segments.append((j,continuation.start(2),continuation.group(2).rstrip('\r\n'))); j+=1
        stream=''; coords=[]
        for row,col,value in segments:
            if stream: stream+=' ';coords.append((row,col))
            stream+=value;coords.extend((row,col+n) for n in range(len(value)))
        targets=[]
        if tag=='modulemap': targets=list(re.finditer(r'(?<==>)\s*([A-Za-z_]\w*(?:\.\w+)*)',stream))
        else:
            ranges=[(m.start(1),m.end(1)) for m in re.finditer(r'\[([^]]*)\]',stream)] if tag=='links' else [(0,len(stream))]
            if not ranges: ranges=[(0,len(stream))]
            for lo,hi in ranges:
                for chunk in re.finditer(r'[^;,]+',stream[lo:hi]):
                    begin=lo+chunk.start();end=lo+chunk.end();colon=stream.find(':',begin,end) if tag=='links' else -1
                    start=colon+1 if colon>=0 else begin
                    found=re.search(r'([A-Za-z_]\w*(?:\.\w+)*)',stream[start:end])
                    if found: targets.append((start+found.start(1),start+found.end(1),found.group(1)))
        actual=[]
        for match in targets:
            start,stop,token=match if isinstance(match,tuple) else (match.start(1),match.end(1),match.group(1))
            candidates=index.get(token,[])
            if not candidates and '.' in token:
                candidates=sorted(set(pair for values in index.values() for pair in values if pair[1].endswith('.'+token)))
            same=[pair for pair in candidates if pair[0]==rel]; selected=same if len(same)==1 else candidates
            if len(selected)==1:
                target=selected[0][1];actual.append(target)
                if target!=token:
                    row,col=coords[start];last,endcol=coords[stop-1]
                    if row==last: replacements.setdefault(row,[]).append((col,endcol+1,target));items['qualified'].append(rel+':'+token+' => '+target)
                    else: items['unresolved'].append(rel+':'+token+':cross-line-token')
            elif candidates: items['unresolved'].append(rel+':'+token+':ambiguous')
            else: items['unresolved'].append(rel+':'+token+':external')
        blocks.append((tag,i,j,actual));i=j
    for row,edits in replacements.items():
        for start,stop,value in sorted(set(edits),reverse=True): lines[row]=lines[row][:start]+value+lines[row][stop:]
    # Informational stale-uses scan; never remove declared relations or borrow another owner.
    owners={min([node.lineno]+[d.lineno for d in node.decorator_list])-1:node for node in ast.walk(tree) if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))}
    aliases={alias.asname or alias.name:alias.name for node in tree.body if isinstance(node,ast.ImportFrom) for alias in node.names}
    for tag,first,last,targets in blocks:
        if tag!='uses': continue
        nextrow=last
        while nextrow<len(lines) and (nextrow in comments or not lines[nextrow].strip()): nextrow+=1
        owner=owners.get(nextrow)
        if owner is None: continue
        referenced={node.id for node in ast.walk(owner) if isinstance(node,ast.Name)}|{node.attr for node in ast.walk(owner) if isinstance(node,ast.Attribute)}
        referenced|={aliases[name] for name in referenced if name in aliases}
        for target in targets:
            if target.rsplit('.',1)[-1] not in referenced: items['stale uses info'].append(rel+':'+owner.name+':'+target)
    moved=[]; deleted=set(); seen=set()
    for row,match in old:
        name=match.group(1)
        current=any(i in comments and re.match(r'^\s*##\s*@'+name+r'\b',line) for i,line in enumerate(lines))
        if name in seen or current:
            items['listed'].append(rel+':'+str(row+1)+':duplicate-or-current-'+name); continue
        seen.add(name); segments=[(row,match.group(2))]; deleted.add(row);j=row+1
        while j<len(lines) and j in comments and re.match(r'^#(?!#)\s+\S',lines[j]) and not re.match(r'^#\s*(?:region|endregion|GREP_SUMMARY:|STRUCTURE:)',lines[j]):
            segments.append((j,re.sub(r'^#(?!#)\s+','',lines[j]).rstrip('\r\n')));deleted.add(j);j+=1
        for n,(oldrow,value) in enumerate(segments):
            prose=re.sub(r'`[^`]*`|[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+',lambda m:' '*len(m.group(0)),value)
            markers=re.findall(r'(?<![.@\\])@[A-Za-z_]\w*',prose)
            if markers: items['listed'].append(rel+':'+str(oldrow+1)+':'+','.join(markers))
            if name=='STRUCTURE':
                for bracket in re.findall(r'<(/?[A-Za-z][A-Za-z0-9_-]*(?:\s[^<>]*)?)>',value): items['brackets'].append(rel+':'+str(oldrow+1)+':'+bracket)
                value=re.sub(r'<(/?[A-Za-z][A-Za-z0-9_-]*(?:\s[^<>]*)?)>',r'〈\1〉',value)
            moved.append(('## @'+name+' ' if n==0 else '##   ')+value+ending)
        items['moved tags'].append(rel+':'+str(row+1))
    rendered=[]
    for row,line in enumerate(lines):
        if anchor is not None and row==min([anchor.lineno]+[d.lineno for d in anchor.decorator_list])-1: rendered.extend(moved)
        if row in deleted:
            # BUG_FIX_CONTEXT: stripping a final blank to preserve no-EOL changed a NONCOMMENT row.
            # Retain the original last comment token as an empty comment; migrated content lives at the anchor.
            if row==len(lines)-1 and not text.endswith(('\r','\n')): rendered.append('#')
            continue
        # Genuine block tag only; wrapped prose mention remains listed, matching original semantics.
        match=re.match(r'^(\s*)##\s*@(modulemap|invariants|usecases|rationale|changes)\s+(\S.*)',line.rstrip('\r\n')) if row in comments else None
        if match:
            prior=lines[row-1].strip() if row and row-1 in comments else ''
            genuine=not prior or prior=='##' or prior[-1] in '.:;!?)]}' or prior[-1].isdigit()
            if genuine:
                line=match.group(1)+'## @'+match.group(2)+ending+match.group(1)+'##   '+match.group(3)+ending;items['split block tags'].append(rel+':'+str(row+1))
            else: items['listed'].append(rel+':'+str(row+1)+':prose-tag-'+match.group(2))
        if row in comments:
            safe=re.sub(r'`[^`]*`|[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+',lambda m:' '*len(m.group(0)),line)
            safe=re.sub(r'^\s*##\s*@[A-Za-z_]\w*','',safe)
            markers=re.findall(r'(?<![.@\\])@[A-Za-z_]\w*|<[/A-Za-z][^<>]*>',safe)
            if markers: items['listed'].append(rel+':'+str(row+1)+':'+','.join(markers))
        rendered.append(line)
    new=''.join(rendered)
    logger.info('[IMP:9][migrate_python][RESULT] moved=%d qualified=%d listed=%d',len(items['moved tags']),len(items['qualified']),len(items['listed']))
    _trajectory_return = new,items; logger.debug('[IMP:3][migrate_python][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic

# endregion FUNC_migrate_python


# region FUNC_migrate_doxyfile [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Repair owned alias spans right-to-left and validate the effective reset/append result.
## @uses consumer_files.parse_doxyfile, io.StringIO
## @io Input: text complete config str, template_text complete trusted seed str. Output: (new text,items categories), custom aliases/settings/order/endings retained; unsafe known custom definitions violations. ConsumerInputError on unsupported config/spans/unaffected settings drift. Example: two aliases on one line both lose only block-closing ^^.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def migrate_doxyfile(text,template_text):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][migrate_doxyfile][INIT] begin owned scoped operation')
    logger.info('[IMP:4][migrate_doxyfile][INIT] original-span transformations')
    info=cf.parse_doxyfile(text); seed=cf.parse_doxyfile(template_text); lines=io.StringIO(text,newline='').readlines(); replacements={}; items={k:[] for k in CATEGORIES}; kept_known=set()
    active_spans={}
    for item in info.physical_spans:
        if item['key']=='ALIASES':
            key,_,value=item['value'].partition('=')
            if info.aliases.get(key)==value: active_spans[key]=item
    for span in info.physical_spans:
        if span['key']!='ALIASES': continue
        name,_,value=span['value'].partition('=')
        if name not in seed.aliases: items['kept aliases'].append(name); continue
        expected=seed.aliases[name]
        # BUG_FIX_CONTEXT: discarded assignments cannot satisfy or invalidate final effective aliases.
        if active_spans.get(name) is not span: continue
        if value==expected: continue
        if name in cf.BLOCK_TAGS and value==expected+'^^':
            start=span['start']; stop=span['end']
            if start[0]!=stop[0]: cf.fail('migrate_doxyfile','multiline-alias-token')
            replacement='"'+name+'='+expected.replace('"','\\"')+'"'
            replacements.setdefault(start[0],[]).append((start[1],stop[1],replacement)); items['changed aliases'].append(name)
        else:
            # Deliberate safe custom titles remain valid own-field bindings; only unsafe/ambiguous forms refuse.
            safe=re.fullmatch(r'@par [^@^<>\r\n]+:(?:\^\^)?',value) and (value.endswith('^^') if name not in cf.BLOCK_TAGS else not value.endswith('^^'))
            items['kept aliases'].append(name+' custom definition')
            if safe: kept_known.add(name)
            else: items['violations'].append('unsafe-custom-known-alias:'+name)
    # BUG_FIX_CONTEXT: original left-to-right offsets corrupted later same-line tokens. Use original spans right-to-left.
    for row,edits in replacements.items():
        for start,stop,value in sorted(edits,reverse=True): lines[row]=lines[row][:start]+value+lines[row][stop:]
    new=''.join(lines); ending='\r\n' if '\r\n' in text else '\r' if '\r' in text and '\n' not in text else '\n'
    effective=cf.parse_doxyfile(new)
    for name,value in seed.aliases.items():
        if name not in effective.aliases:
            if new and not new.endswith(('\r','\n')): new+=ending
            new+='ALIASES += "'+name+'='+value.replace('"','\\"')+'"'+ending; items['added aliases'].append(name)
    final=cf.parse_doxyfile(new)
    if {k:v for k,v in info.settings.items() if k!='ALIASES'}!={k:v for k,v in final.settings.items() if k!='ALIASES'} or any(final.aliases.get(k)!=v for k,v in info.aliases.items() if k not in seed.aliases):
        cf.fail('migrate_doxyfile','unaffected-config-changed')
    if any(final.aliases.get(k)!=v for k,v in seed.aliases.items() if k not in kept_known): items['violations'].append('effective-known-alias-mismatch')
    logger.info('[IMP:9][migrate_doxyfile][RESULT] changed=%d added=%d',len(items['changed aliases']),len(items['added aliases']))
    _trajectory_return = new,items; logger.debug('[IMP:3][migrate_doxyfile][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_migrate_doxyfile


# region FUNC_verify_change [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Produce real installed-interpreter COMMENT/token/AST equality proof before source writes.
## @uses subprocess.Popen, tokenize.generate_tokens, ast.parse, hashlib.sha256
## @io Input: rel safe relative str; old_text/new_text complete str; interpreter explicit executable str|Path. Output: dict ok/astEqual/tokensEqual/version/argv/cwd/envNames/actual start-end/pid/streams/exit/SHA; unavailable returns ok false with retained diagnostic. Executes trusted stdlib text-only proof, no consumer import/write. Example: executable VALUE2->18 fails on both interpreters.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def verify_change(rel,old_text,new_text,interpreter):
    logger.info('[IMP:4][verify_change][INIT] begin owned scoped operation')
    logger.info('[IMP:7][verify_change][PROOF] actual installed interpreter')
    # START_BLOCK_Validation
    argv=[str(interpreter),'-B','-c',PROOF_PROGRAM]
    env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME')}
    record={'argv':argv,'cwd':str(Path.cwd()),'environmentNames':sorted(env),'start':datetime.datetime.now(datetime.timezone.utc).isoformat(),'oldSha256':hashlib.sha256(old_text.encode()).hexdigest(),'newSha256':hashlib.sha256(new_text.encode()).hexdigest()}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: old proof omitted child clock/pid/environment identities and lost failed streams.
    try:
        proc=subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env)
        stdout,stderr=proc.communicate(json.dumps({'old':old_text,'new':new_text}))
        record.update(pid=proc.pid,stdout=stdout,stderr=stderr,exitCode=proc.returncode,end=datetime.datetime.now(datetime.timezone.utc).isoformat())
        proof=json.loads(stdout);record.update(proof)
        if proc.returncode or stderr or not proof.get('ok'): logger.error('[IMP:10][verify_change][PROOF_FAILURE] kind=token-or-AST')
        else: logger.info('[IMP:9][verify_change][PROOF_SUCCESS] version=%s',record['version'])
        _trajectory_return = record; logger.debug('[IMP:3][verify_change][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except (OSError,ValueError):
        logger.error('[IMP:10][verify_change][PROOF_FAILURE] kind=interpreter-unavailable')
        record.update(ok=False,exitCode=record.get('exitCode',2),error='interpreter-unavailable',end=datetime.datetime.now(datetime.timezone.utc).isoformat())
        _trajectory_return = record; logger.debug('[IMP:3][verify_change][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_ErrorHandling

# endregion FUNC_verify_change


# region FUNC_plan_identity [DOMAIN(9): Safety; CONCEPT(9): PlanIntegrity; TECH(8): SHA256]
## @purpose Bind complete planned text, exact originals/config/template, interpreter proof results and violations deterministically.
## @uses hashlib.sha256, json.dumps, markup_migrate.Plan
## @io Input: Plan with contained root, complete identities and FileChange list. Output: lowercase64 SHA256 string.
##   Invariants: every old/new text and numeric mode participates; child clock/pid/streams locators remain receipts, not replay-varying identity.
##   Side effects: none. Guarantees: comment-only tampering changes identity too; no source or proof execution.
##   Errors: TypeError for nonserializable malformed caller Plan. Example: changing one planned invariant makes the approved identity differ. Importance:10.
## @complexity 3
def plan_identity(plan):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][plan_identity][INIT] begin owned scoped operation')
    proof_keys=('ok','changedNoncomments','astEqual','tokensEqual','version','argv','stdout','stderr','exitCode','oldSha256','newSha256','error')
    payload={'root':str(plan.root),'originals':plan.originals,'config':plan.config_identity,'template':plan.template_identity,'interpreters':plan.interpreters,'changes':[{'path':x.path,'old':x.old,'new':x.new,'mode':x.mode,'proofs':[{k:p[k] for k in proof_keys if k in p} for p in x.proofs]} for x in plan.changes],'items':plan.items}
    _trajectory_return = hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest(); logger.debug('[IMP:3][plan_identity][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_plan_identity


# region FUNC_build_plan [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Freeze complete actual source/config/template originals and every supplied interpreter proof.
## @uses consumer_files.covered_sources, markup_migrate.definitions, markup_migrate.migrate_python, markup_migrate.verify_change, markup_migrate.plan_identity
## @io Input: root str|Path; template_path optional trusted seed Path; interpreters nonempty executable iterable; files optional exact covered relative leaves. Output: Plan full old/new/modes/proofs/items/identities. Reads and proof-child effects only; no source write. ConsumerInputError on uncovered/linked/unknown input; syntax failures retained violations. Example: invalid support.py aborts future apply even when records.py has valid changes.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def build_plan(root,template_path=None,interpreters=None,files=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][build_plan][INIT] begin owned scoped operation')
    root=Path(root).resolve(); template_path=Path(template_path or Path(__file__).parent.parent/'templates/Doxyfile').resolve(); interpreters=list(interpreters or [sys.executable]); config_path=root/'Doxyfile'
    config_text=cf.read_text(config_path); info=cf.parse_doxyfile(config_text); population=cf.covered_sources(root,info)
    plan=Plan(root,population,cf.identity(config_path),str(template_path),cf.identity(template_path),[str(x) for x in interpreters],[],{k:[] for k in CATEGORIES},{})
    scope=set(files) if files is not None else set(population.files)|{'Doxyfile'}
    if not scope<=set(population.files)|{'Doxyfile'}: cf.fail('build_plan','uncovered-file-scope')
    parsed={}; originals={}
    for rel in population.files:
        text=cf.read_text(root/rel); originals[rel]=text
        if rel.endswith('.py'):
            try: parsed[rel]=ast.parse(text)
            except SyntaxError: plan.items['not_parsed'].append(rel); plan.items['violations'].append(rel+':parse-failure')
    index=definitions(root,parsed)
    plan.originals={rel:dict(path=rel,**cf.identity(root/rel)) for rel in population.files+['Doxyfile']}
    for rel in sorted(scope):
        path=cf.contained(root,rel,no_symlinks=True); old=cf.read_text(path)
        if rel=='Doxyfile': new,items=migrate_doxyfile(old,cf.read_text(template_path))
        elif rel.endswith('.py') and rel in parsed: new,items=migrate_python(rel,old,parsed[rel],index)
        else: continue
        for key,values in items.items(): plan.items[key].extend(values)
        proofs=[]
        if rel.endswith('.py'):
            for interpreter in interpreters:
                proof=verify_change(rel,old,new,interpreter); proofs.append(proof)
                if not proof.get('ok'): plan.items['violations'].append(rel+':'+str(interpreter)+':proof-failure')
        if old!=new: plan.changes.append(FileChange(rel,old,new,stat.S_IMODE(path.stat().st_mode),cf.identity(path),proofs))
    plan.identity=plan_identity(plan)
    logger.info('[IMP:9][build_plan][RESULT] changes=%d violations=%d',len(plan.changes),len(plan.items['violations']))
    _trajectory_return = plan; logger.debug('[IMP:3][build_plan][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_build_plan


# region FUNC_write_changes [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Recheck every proof/original/scope, preserve outside recovery and atomically replace each owned regular leaf with honest partial failure effects.
## @uses markup_migrate.save, markup_migrate.ApplyReceipt, markup_migrate.plan_identity, markup_migrate.verify_change, consumer_files.covered_sources, consumer_files.identity, consumer_files.contained, consumer_files.provenance, tempfile.mkstemp, os.fsync, os.replace
## @io Input: root Path matching frozen Plan; files exact unique covered relative leaves; authority actual parent-authenticated record with target/action/files/planIdentity/originals/humanSource/parentVerification/generated by-at-via; receipt_dir new owned outside-target path. Output: ApplyReceipt completed/unwritten/unknown/recovery/status/reason/path; no multi-file transaction promise. Side effects: outside recovery and same-directory fsynced staged files, atomic os.replace, numeric mode preservation and durable receipts. Guarantees: all global proofs/preflight before first source write, later failure retains actual completed effects. Errors: safe refused/partial receipt on ConsumerInputError/OSError/ValueError; unavoidable recovery-write failure may prevent saved receipt, returned actual state retained. Importance:10 for source preservation. Example: pass exact recorded two-file fixture grant and both promised interpreters after preview.
## @complexity 7
def write_changes(root,plan,*,files,authority,receipt_dir):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][write_changes][INIT] begin owned scoped operation')
    root=Path(root).resolve(); scope=[]; receipt_dir=Path(receipt_dir).resolve(); paths=[x.path for x in plan.changes]; completed=[]; recovery={}; unknown=[]; owned_receipt=False; pending=None
    receipt_path=receipt_dir/'receipt.json'
    try:
        if not isinstance(files,(list,tuple)) or any(type(item) is not str or not item.strip() for item in files) or len(set(files))!=len(files): cf.fail('write_changes','invalid-exact-file-scope')
        scope=sorted(files)
        if receipt_dir.exists(): cf.fail('write_changes','recovery-already-exists')
        if plan.identity!=plan_identity(plan): cf.fail('write_changes','changed-plan-payload')
        if receipt_dir==root or root in receipt_dir.parents: cf.fail('write_changes','recovery-inside-threat')
        if plan.root!=root or not scope or not set(paths)<=set(scope) or plan.items['violations'] or plan.items['no_anchor']: cf.fail('write_changes','scope-or-proof-not-ready')
        if isinstance(authority,(str,Path)): authority=json.loads(cf.read_text(authority))
        if not isinstance(authority,dict) or authority.get('action')!='markup-migrate-apply' or authority.get('target')!=str(root) or not isinstance(authority.get('files'),list) or any(type(item) is not str or not item.strip() for item in authority['files']) or sorted(authority['files'])!=scope or authority.get('planIdentity')!=plan.identity or authority.get('originals')!=plan.originals or any(type(authority.get(key)) is not str or not authority[key].strip() for key in ('humanSource','parentVerification')):
            cf.fail('write_changes','missing-exact-parent-authenticated-record')
        cf.provenance(authority.get('generated'),gate=True)
        if cf.identity(plan.template_path)!=plan.template_identity or cf.identity(root/'Doxyfile')!=plan.config_identity: cf.fail('write_changes','stale-config-template')
        population=cf.covered_sources(root,cf.parse_doxyfile(cf.read_text(root/'Doxyfile')))
        if population.source_identities!=plan.population.source_identities: cf.fail('write_changes','stale-population')
        for rel,original in plan.originals.items():
            path=cf.contained(root,rel,no_symlinks=True)
            if dict(path=rel,**cf.identity(path))!=original: cf.fail('write_changes','stale-original-byte-mode')
        for change in plan.changes:
            if change.path.endswith('.py'):
                if len(change.proofs)!=len(plan.interpreters) or any(not p.get('ok') or p.get('exitCode')!=0 for p in change.proofs): cf.fail('write_changes','unproved-change')
                for interpreter in plan.interpreters:
                    if not verify_change(change.path,change.old,change.new,interpreter).get('ok'): cf.fail('write_changes','renewed-proof-failed')
        logger.info('[IMP:9][write_changes][PREFLIGHT_VALID] scope=%d originals=%d changes=%d interpreters=%d; no source writes',len(scope),len(plan.originals),len(plan.changes),len(plan.interpreters))
        receipt_dir.mkdir(parents=True,exist_ok=False); owned_receipt=True
        for change in plan.changes:
            name=receipt_dir/(hashlib.sha256(change.path.encode()).hexdigest()+'.original'); name.write_bytes(change.old.encode('utf-8')); name.chmod(change.mode)
            recovery[change.path]={'path':str(name),'mode':change.mode,'sha256':hashlib.sha256(name.read_bytes()).hexdigest()}
        (receipt_dir/'plan.json').write_text(json.dumps({'identity':plan.identity,'originals':plan.originals,'changes':[x.__dict__ for x in plan.changes],'proofs':[p for x in plan.changes for p in x.proofs]},indent=2)+'\n')
        ready=save(receipt_dir,receipt_path,owned_receipt,paths,completed,unknown,recovery,'READY','All proofs/originals/recovery complete; no source effect yet')
        if 'persistence unavailable' in ready.reason: cf.fail('write_changes','recovery-receipt-unavailable')
        for change in plan.changes:
            path=cf.contained(root,change.path,no_symlinks=True)
            if cf.identity(path)!=change.original_identity: cf.fail('write_changes','late-stale-original')
            staged=None
            try:
                fd,staged=tempfile.mkstemp(prefix='.markup-stage-',dir=str(path.parent))
                with os.fdopen(fd,'wb') as stream:
                    stream.write(change.new.encode('utf-8')); stream.flush(); os.fsync(stream.fileno()); os.fchmod(stream.fileno(),change.mode)
                cf.contained(root,change.path,no_symlinks=True)
                if cf.identity(path)!=change.original_identity: cf.fail('write_changes','pre-replace-stale-original')
                # BUG_FIX_CONTEXT: interruption/read failure after replacement is an unknown effect until actual readback.
                pending=change.path
                os.replace(staged,path); staged=None
                if path.read_bytes()!=change.new.encode('utf-8') or stat.S_IMODE(path.stat().st_mode)!=change.mode:
                    unknown.append(change.path); cf.fail('write_changes','post-replace-readback')
                completed.append(change.path); pending=None; logger.info('[IMP:9][write_changes][EFFECT_READBACK] completed=%d remaining=%d unknown=%d',len(completed),len(paths)-len(completed),len(unknown)); saved=save(receipt_dir,receipt_path,owned_receipt,paths,completed,unknown,recovery,'WRITING','Per-file effect read back; remaining files not yet written')
                if 'persistence unavailable' in saved.reason: cf.fail('write_changes','effect-receipt-unavailable')
            finally:
                if staged and Path(staged).exists(): Path(staged).unlink()
        final=save(receipt_dir,receipt_path,owned_receipt,paths,completed,unknown,recovery,'APPLIED','Every actual per-file replacement/readback completed')
        if final.status=='APPLIED': logger.info('[IMP:9][write_changes][APPLIED] completed=%d',len(completed))
        _trajectory_return = final; logger.debug('[IMP:3][write_changes][RETURN] owned result evaluated'); return _trajectory_return
    except (cf.ConsumerInputError,OSError,ValueError) as error:
        if pending and pending not in completed and pending not in unknown:
            try:
                old=next(x.old for x in plan.changes if x.path==pending)
                if (root/pending).read_bytes()!=old.encode('utf-8'): unknown.append(pending)
            except OSError: unknown.append(pending)
        logger.error('[IMP:10][write_changes][APPLY_FAILURE] completed=%d unknown=%d kind=%s',len(completed),len(unknown),type(error).__name__)
        if owned_receipt: _trajectory_return = save(receipt_dir,receipt_path,owned_receipt,paths,completed,unknown,recovery,'REFUSED' if not completed and not unknown else 'PARTIAL','kind='+type(error).__name__+'; investigate before replay'); logger.debug('[IMP:3][write_changes][RETURN] owned result evaluated'); return _trajectory_return
        _trajectory_return = ApplyReceipt(completed,[x for x in paths if x not in completed and x not in unknown],unknown,recovery,'REFUSED','Preflight/recovery unavailable: '+type(error).__name__,''); logger.debug('[IMP:3][write_changes][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_write_changes


# region FUNC_render [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Print every stable report category and the exact planned byte-faithful unified diff.
## @uses difflib.unified_diff, io.StringIO
## @io Input: plan fully assessed Plan. Output: complete str; all categories including zero counts sorted/dedup; CR/LF/CRLF/formfeed payload and no-final-newline markers retained. No writes. Example: CRLF comment hunk contains original CRLF payload, not flattened LF.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def render(plan):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][render][INIT] begin owned scoped operation')
    result=['markup-migrate: sources=%d changes=%d'%(len(plan.population.files),len(plan.changes))]
    for key in CATEGORIES:
        values=sorted(set(plan.items[key])); result.append('%s (%d):'%(key,len(values))); result.extend('  '+x for x in values)
    text='\n'.join(result)+'\n'
    # BUG_FIX_CONTEXT: splitlines flattened CRLF/formfeed content in the printed write payload.
    for change in plan.changes:
        old=io.StringIO(change.old,newline='').readlines();new=io.StringIO(change.new,newline='').readlines()
        for line in difflib.unified_diff(old,new,fromfile='a/'+change.path,tofile='b/'+change.path):
            text+=line
            if not line.endswith(('\r','\n')): text+='\n\\ No newline at end of file\n'
    _trajectory_return = text; logger.debug('[IMP:3][render][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic

# endregion FUNC_render


# region FUNC_run [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Route readonly preview/check or exact scoped apply with complete honest effects.
## @uses markup_migrate.build_plan, markup_migrate.render, markup_migrate.write_changes
## @io Input: project explicit root; mode dry-run|check|apply; optional trusted template/interpreters/exact files/authority/outside receipt_dir. Output: (exit0|1|2,text); dry0 dueallowed, check1 due/0 clean, unavailable2, apply0 only every effect read back and final receipt persisted. No implicit Git/build/adoption; safe exceptions2. Example: partial failure prints full preview+completed/unwritten/unknown receipt.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def run(project,mode='dry-run',template_path=None,*,files=None,authority=None,receipt_dir=None,interpreters=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][run][INIT] begin owned scoped operation')
    try:
        plan=build_plan(project,template_path,interpreters,files); text=render(plan)
        if plan.items['violations']: _trajectory_return = 2,text+'markup-migrate: unavailable safety proof\n'; logger.info('[IMP:9][run][MIGRATION_RESULT] mode=%s exit=%d changes=%d',mode,_trajectory_return[0],len(plan.changes)); return _trajectory_return
        due=len(set(x.path for x in plan.changes)|set(plan.items['no_anchor'])|{x.split(':',1)[0] for x in plan.items['listed'] if 'duplicate-or-current-' in x})
        if mode=='check': _trajectory_return = (1 if due else 0),text+('markup-migrate: migration due: %d files\n'%due if due else 'markup-migrate: up to date\n'); logger.info('[IMP:9][run][MIGRATION_RESULT] mode=%s exit=%d changes=%d',mode,_trajectory_return[0],len(plan.changes)); return _trajectory_return
        if mode=='dry-run': _trajectory_return = 0,text; logger.info('[IMP:9][run][MIGRATION_RESULT] mode=%s exit=%d changes=%d',mode,_trajectory_return[0],len(plan.changes)); return _trajectory_return
        if mode!='apply' or not files or authority is None or receipt_dir is None: cf.fail('run','apply-needs-exact-scope-authority-recovery')
        receipt=write_changes(project,plan,files=files,authority=authority,receipt_dir=receipt_dir)
        text+='effects: '+json.dumps(receipt.__dict__,sort_keys=True)+'\n'
        if receipt.status!='APPLIED': _trajectory_return = 2,text; logger.info('[IMP:9][run][MIGRATION_RESULT] mode=%s exit=%d changes=%d',mode,_trajectory_return[0],len(plan.changes)); return _trajectory_return
        _trajectory_return = 0,text+'applied: %d files written\n'%len(receipt.completed); logger.info('[IMP:9][run][MIGRATION_RESULT] mode=%s exit=%d changes=%d',mode,_trajectory_return[0],len(plan.changes)); return _trajectory_return
    except (cf.ConsumerInputError,OSError,ValueError) as error:
        logger.error('[IMP:10][run][UNAVAILABLE] kind=%s',type(error).__name__); _trajectory_return = 2,'markup-migrate: unavailable: '+type(error).__name__+'\n'; logger.info('[IMP:9][run][MIGRATION_UNAVAILABLE] mode=%s exit=2 kind=%s',mode,type(error).__name__); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_run


# region FUNC_main [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Expose the shipped migration CLI with dry-run default and explicit guarded apply.
## @uses consumer_files.SafeArgumentParser, markup_migrate.run, logging.basicConfig
## @io Input: argv list[str]|None; exact PROJECT plus mutually exclusive --check/--apply and repeated --file/--python, approval-record/receipt-dir. Output: exit0|1|2 and full report stdout, safe diagnostics stderr; no PATH installation. argparse SystemExit on help0/invalid2. Example: bare PROJECT previews without receipts or source writes.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def main(argv=None):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][main][INIT] begin owned scoped operation')
    parser=cf.SafeArgumentParser(); parser.add_argument('project'); modes=parser.add_mutually_exclusive_group(); modes.add_argument('--check',action='store_true'); modes.add_argument('--apply',action='store_true'); parser.add_argument('--file',action='append'); parser.add_argument('--python',action='append'); parser.add_argument('--approval-record'); parser.add_argument('--receipt-dir'); args=parser.parse_args(argv)
    logging.basicConfig(level=getattr(logging,os.environ.get('MARKUP_MIGRATE_LOG','WARNING').upper(),logging.WARNING),format='%(message)s',stream=sys.stderr)
    code,text=run(args.project,'apply' if args.apply else 'check' if args.check else 'dry-run',files=args.file,authority=args.approval_record,receipt_dir=args.receipt_dir,interpreters=args.python)
    print(text,end=''); _trajectory_return = code; logger.debug('[IMP:3][main][RETURN] owned result evaluated'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_main



# region FUNC_save [DOMAIN(9): ConsumerPM; CONCEPT(9): Boundaries, Evidence; TECH(7): Python]
## @purpose Persist the current exact effects atomically inside the newly owned recovery directory.
## @uses markup_migrate.ApplyReceipt, tempfile.mkstemp, os.fsync, os.replace
## @io Input: receipt_dir/receipt_path owned outside-target Path, owned_receipt bool established by write_changes, paths/completed/unknown relative str lists, recovery dict[str,backup identity]; internal write_changes only after its scope/preflight, never independent permission;  status supported local receipt str and safe reason str; supplied completed/unknown/recovery snapshots. Output: ApplyReceipt with current lists, persisted path or honest persistence limitation. Side effects: owned staged receipt only, no foreign overwrite. OSError retained as limitation; required READY persistence failure stops apply. Example: failed WRITING save retains completed first file in returned receipt.
##   Operational guarantees: inputs are not mutated except explicitly documented owned accumulators/resources; no authority is inferred.
##   System importance:9 for complete scoped evidence; complexity below describes finite branches, not performance telemetry.
## @complexity 7
def save(receipt_dir,receipt_path,owned_receipt,paths,completed,unknown,recovery,status,reason):
    # START_BLOCK_BusinessLogic
    logger.info('[IMP:4][save][INIT] begin owned scoped operation')
    receipt=ApplyReceipt(list(completed),[x for x in paths if x not in completed and x not in unknown],list(unknown),recovery,status,reason,str(receipt_path))
    # BUG_FIX_CONTEXT: a failed receipt write must not erase known source effects or overwrite foreign recovery.
    if not owned_receipt: _trajectory_return = receipt; logger.info('[IMP:9][save][EFFECT_RECEIPT] status=%s completed=%d unwritten=%d unknown=%d persistence=%s',receipt.status,len(receipt.completed),len(receipt.unwritten),len(receipt.unknown),'unavailable' if 'persistence unavailable' in receipt.reason else 'saved' if owned_receipt else 'not-created'); return _trajectory_return
    staged=None
    try:
        fd,staged=tempfile.mkstemp(prefix='.receipt-',dir=str(receipt_dir))
        with os.fdopen(fd,'w',encoding='utf-8') as stream:
            stream.write(json.dumps(receipt.__dict__,indent=2)+'\n');stream.flush();os.fsync(stream.fileno())
        os.replace(staged,receipt_path);staged=None
    except OSError:
        receipt.status='PARTIAL' if completed or unknown else 'REFUSED'
        receipt.reason+='; current receipt persistence unavailable; returned effects retained'
        logger.error('[IMP:10][save][RECEIPT_FAILURE] kind=OSError')
    finally:
        if staged and Path(staged).exists(): Path(staged).unlink()
    _trajectory_return = receipt; logger.info('[IMP:9][save][EFFECT_RECEIPT] status=%s completed=%d unwritten=%d unknown=%d persistence=%s',receipt.status,len(receipt.completed),len(receipt.unwritten),len(receipt.unknown),'unavailable' if 'persistence unavailable' in receipt.reason else 'saved' if owned_receipt else 'not-created'); return _trajectory_return
    # END_BLOCK_BusinessLogic
# endregion FUNC_save


if __name__=='__main__':
    raise SystemExit(main())
