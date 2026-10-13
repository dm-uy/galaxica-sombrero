# region MODULE_CONTRACT [DOMAIN(8): Testing, Safety; CONCEPT(8): DestructiveGuard, Precision, ReadOnlyJudge, RealPath; TECH(8): pytest, subprocess, git]
## @modulecontract
## @purpose Verify that the PreToolUse guard asks before every command that would destroy something unrecoverable, stays silent for the commands that are false alarms, denies tree-changing commands to the read-only judge agents in both plain and namespaced form, is active without any project declaration, can be switched off by the owner, and never fails the session.
## @scope hooks/guard_destructive.py through the real hook process (stdin payload, stdout decision, exit status, opt-in stderr trace), through the exact command of hooks.json run by a shell, and through direct imports for the pure shell-parsing and scope functions; real git repositories and worktrees built in temporary directories.
## @input Hook payloads built in the tests; temporary projects, repositories and worktrees; environment values for the METHODOLOGY_GUARD switches.
## @output Pass or fail per acceptance behavior, with the important trace records printed before the assertions.
## @links [USES_API(8): hooks/guard_destructive.py; USES_API(6): subprocess.run for git init, git worktree add and the hook process; READS_DATA_FROM(8): implementations/claude/hooks/hooks.json and the hook sources; no environment secrets]
## @invariants
## - No test executes a command it classifies; commands are only data in the hook payload.
## - The scratch prefixes are replaced in every hook run, because the pytest temporary directory lives under one of the default prefixes and would hide every outside-the-project case.
## - Every hook run in a test has tracing on, and a happy-path or silent run carries no importance 10 event.
## - Expected decisions are fixed in the tests, never derived from the hook output they judge.
## @rationale
## Q: Why do the benign cases mirror false alarms seen in real sessions?
## A: Cache clean-up in a sibling worktree, heredoc bodies and SQL words written into a file are the shapes that made an earlier guard noisy; a regression in their exact shape is the only proof that precision holds.
## Q: Why build a tilde path at run time and use a temporary HOME?
## A: The tilde expansion is a real branch of the path resolution; building the word from parts keeps a literal home path out of the source while a temporary HOME makes the expansion land outside the project.
## Q: Why test the process boundary and the functions both?
## A: The decision JSON, the exit status and the silent stderr exist only at the process boundary; the parsing and scope functions are business logic and are cheaper and sharper to test by import.
## @changes
## LAST_CHANGE: [1.0.4 - Added the checks of the fourth debug pass: a script attached to the sed expression option no longer hides the file from a judge rule (the five reviewed spellings and the longer family of them in all six judge forms, the unit table of the file operand helper with the backup suffix ending in a value letter of sed, the silent scratch and print only forms, the other agents unaffected), the owned trace of the new helper, and the pin of the documented known limits (the exact spellings of the owner ask path against its named abbreviations, the git verbs a judge is denied against the verbs named as not intercepted).]
## - 1.0.3 - Added the checks of the third debug pass: an abbreviated long option is judged by the option it names (the expansion table test, the process test in all six judge forms, the extended denied and allowed matrices, the branch and config unit tables, the sed, cp and mv helper tables and the GNU file command operand cases), git branch -a and -r are filters and not the list mode, an ambiguous or unknown long option of git branch or git config is denied, the owned trace of the new helpers, and the two parsing and scope unit tests print their own trace before asserting.]
## - 1.0.2 - Added the checks of the second debug pass: the owned trace of the judge helpers (in process and at the process boundary, silent without METHODOLOGY_HOOK_LOG, never an operand), the allowed and denied forms of git branch for a judge in all six agent forms, every git fetch (the dry run included) denied to a judge in all six forms, the unit table of the branch form helper, the judge scratch rule (a write outside the project is silent, the same write inside it or in its evidence directory is denied, no scratch prefix exempts a project path, a recursive removal needs a scratch root under a safe prefix) and the pinned default safe prefixes.
## - 1.0.1 - Added the read-only judge rules for git worktree, update-ref, fetch and config writes and for chmod, chown, chgrp, truncate, perl -i, dd of=, ln and install (deny and allowed matrices, six agent forms, other agents unaffected), the remote ref deletion and git rm force asks, and the unit checks of the new helpers.
## - 1.0.0 - Initial suite for the adapted guard: ask and benign matrices, activation without declaration, owner switch, mode, scratch prefixes, recorded false alarms, git precision, SQL clients, variables and artefacts, read-only agents in six forms, custom agent list, internal error, hooks.json command, parsing units and public-content scan.
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => test_guard._module_contract
## FUNC 6[Create a project directory] => test_guard.make_project
## FUNC 7[Turn the project into a repository with a sibling worktree] => test_guard.make_repo
## FUNC 8[Run the hook process with a raw payload text and return the completed process] => test_guard.invoke
## FUNC 9[Run the hook as Claude Code would and return decision, reason and exit code] => test_guard.run_guard
## FUNC 8[Print the important captured records before assertions] => test_guard.show_records
## FUNC 8[Hold the deny reason to the judge isolation rules] => test_guard.assert_scratch_advice
## FUNC 9[Destructive commands ask without any project declaration] => test_guard.test_destructive_commands_ask
## FUNC 9[Ordinary commands and heredoc text pass silently] => test_guard.test_benign_commands_silent
## FUNC 8[The reason names at most three paths and never the command] => test_guard.test_reason_names_at_most_three_paths_and_not_the_command
## FUNC 8[Scratch prefixes and TMPDIR] => test_guard.test_scratch_prefixes_and_tmpdir
## FUNC 8[Hardened mode denies instead of asking] => test_guard.test_deny_mode
## FUNC 9[Other tools and broken payloads never produce a decision or an error] => test_guard.test_other_tools_and_broken_payloads_are_silent
## FUNC 9[Recorded false alarms are silent, deleting a worktree asks] => test_guard.test_recorded_false_alarms_are_silent
## FUNC 9[Git asks only when uncommitted work would be lost] => test_guard.test_git_precision
## FUNC 8[SQL asks only through a client] => test_guard.test_sql_only_through_a_client
## FUNC 9[Active without declaration, off by the owner switch] => test_guard.test_active_without_declaration_and_owner_switch
## FUNC 9[Variables, artefacts and worktree removal] => test_guard.test_variables_artefacts_worktree_removal
## FUNC 9[An unbalanced quote does not hide a later command] => test_guard.test_unbalanced_quote_does_not_hide_a_later_command
## FUNC 9[Read-only agents are denied tree changes in six forms] => test_guard.test_readonly_agents_are_denied_tree_changes
## FUNC 9[The full read-only matrix for qa] => test_guard.test_readonly_matrix_for_qa
## FUNC 9[A judge is denied git state changes and file mode or content changes, with the rule named] => test_guard.test_judge_is_denied_git_state_and_file_changes
## FUNC 9[A judge keeps read-only git queries and scratch work] => test_guard.test_judge_keeps_read_only_queries_and_scratch_work
## FUNC 8[Every judge form is denied one command of each new rule family] => test_guard.test_every_judge_form_is_denied_each_new_rule_family
## FUNC 8[The new judge rules do not touch other agents or the destructive path] => test_guard.test_new_judge_rules_leave_other_agents_alone
## FUNC 9[Remote ref deletion by push asks, ordinary pushes stay silent] => test_guard.test_remote_ref_deletion_by_push_asks
## FUNC 9[git rm force asks only over uncommitted changes] => test_guard.test_git_rm_force_asks_only_over_uncommitted_changes
## FUNC 8[Option, config, perl and operand helpers] => test_guard.test_judge_rule_helpers
## FUNC 8[The judge helpers trace their own verdicts, in process and at the process boundary] => test_guard.test_judge_helpers_trace_their_own_verdicts
## FUNC 8[Unit table of the git branch form helper] => test_guard.test_branch_form_helper
## FUNC 8[Expansion of an abbreviated long option against the option table of a verb] => test_guard.test_long_option_expansion
## FUNC 9[Abbreviated change options are denied to every judge form, abbreviated read options stay silent] => test_guard.test_judge_abbreviated_option_bypass
## FUNC 9[A sed in-place edit with the script attached to the expression option is denied to every judge form, scratch and print only forms stay silent] => test_guard.test_judge_sed_script_forms
## FUNC 8[Which words of a sed in-place call are files] => test_guard.test_sed_file_operand_helper
## FUNC 9[The documented known limits match the behavior] => test_guard.test_documented_limits_match_behavior
## FUNC 9[A judge keeps branch listing, is denied every branch change and every fetch, the dry run included] => test_guard.test_judge_branch_and_fetch_by_form
## FUNC 9[A judge writes outside the project silently and inside it never, evidence directory included] => test_guard.test_judge_scratch_rule
## FUNC 8[A scratch prefix never exempts a project path, a recursive removal needs a safe prefix] => test_guard.test_scratch_prefix_never_exempts_the_project
## FUNC 8[Default safe prefixes are pinned] => test_guard.test_default_safe_prefixes
## FUNC 8[A custom read-only list replaces the defaults] => test_guard.test_custom_readonly_list_replaces_defaults
## FUNC 9[An internal error is silent and exits 0] => test_guard.test_internal_error_is_silent
## FUNC 9[The exact hooks.json command asks through a shell] => test_guard.test_hooks_json_command_asks_through_a_shell
## FUNC 8[Parsing units] => test_guard.test_heredoc_and_segmentation_units
## FUNC 8[Scope units] => test_guard.test_scope_functions
## FUNC 8[Context path scope] => test_guard.test_context_path_scope
## FUNC 8[No legacy names remain in the adapted source] => test_guard.test_adapted_source_has_no_legacy_names
## FUNC 8[Hook files are public clean] => test_guard.test_hook_files_are_public_clean
## @usecases
## - [test_destructive_commands_ask]: Owner -> an agent runs a destructive command in any project -> the owner is asked first.
## - [test_recorded_false_alarms_are_silent]: Owner -> an agent cleans caches in a sibling worktree -> no interruption.
## - [test_git_precision]: Owner -> an agent discards edits with a checkout -> asked only when edits would be lost.
## - [test_readonly_agents_are_denied_tree_changes]: Orchestrator -> a judge agent tries to change the tree -> deny with a pointer to a scratch copy made without .git.
## - [test_judge_is_denied_git_state_and_file_changes]: Orchestrator -> a judge adds a worktree, moves a ref, writes git config, fetches, changes a file mode or content with a non-redirect command -> deny naming the rule.
## - [test_judge_keeps_read_only_queries_and_scratch_work]: Orchestrator -> a judge reads git config, lists worktrees and works in a scratch copy -> no interruption.
## - [test_judge_branch_and_fetch_by_form]: Orchestrator -> a judge lists branches -> no interruption; it creates, deletes or renames a branch, or fetches in any form, the dry run included -> deny.
## - [test_judge_abbreviated_option_bypass]: Orchestrator -> a judge renames, copies or deletes a branch, or removes a config key or section, with an abbreviated long option -> deny; the abbreviated listing and read forms -> silent.
## - [test_judge_sed_script_forms]: Orchestrator -> a judge edits a project file with sed in place and the script given by the expression option -> deny naming the file; the same edit of a scratch file, or a sed that only prints -> silent.
## - [test_documented_limits_match_behavior]: Owner -> reads the known limits in the guard contract -> each named abbreviation is silent, each listed exact spelling asks, each named git verb is as intercepted as documented.
## - [test_judge_scratch_rule]: Orchestrator -> a judge writes its report to a scratch root outside the project -> silent; the same write into the project or its evidence directory -> deny.
## - [test_judge_helpers_trace_their_own_verdicts]: Owner -> switches the opt-in trace on -> every judge rule leaves its own trace line with counts and flags, never an operand.
## - [test_remote_ref_deletion_by_push_asks]: Owner -> an agent deletes a remote branch by push -> asked first.
## - [test_git_rm_force_asks_only_over_uncommitted_changes]: Owner -> an agent forces git rm over an edited file -> asked first.
## - [test_active_without_declaration_and_owner_switch]: Owner -> loads the plugin, optionally switches the guard off -> guard follows the switch.
## - [test_internal_error_is_silent]: Owner -> the hook meets a malformed payload -> the session is unaffected.
## @GREP_SUMMARY guard tests, destructive command, PreToolUse, permission decision, ask deny, force push, reset hard, checkout discard, worktree, heredoc, sql client, activation without declaration, METHODOLOGY_GUARD_SCOPE off, read-only agent, qa reviewer searcher namespaced, git worktree update-ref config fetch, git branch listing, abbreviated long option, unique prefix, option table fail closed, sed in place, cp mv target directory, git fetch dry-run, judge scratch root, evidence directory, safe prefixes, helper trace, chmod chown truncate perl dd ln install, push delete mirror, git rm force, false alarm regression, internal error silent, hooks.json command, public clean, sed expression option, sed script operand, backup suffix, known limits pinned, ask path exact spelling, git verbs not intercepted
## @STRUCTURE ▶ ┌project + repo + worktree + env switches┐ → ⟦python3 guard_destructive.py ← payload: command, cwd, agent_type⟧ → 〈stdout JSON ? decision + reason : silent〉 ∧ exit 0 ∧ no critical trace → assert
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import io
import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path

import guard_destructive
import pytest

LOGGER = logging.getLogger("test_guard")
PACKAGE = Path(__file__).resolve().parents[1]
SCRIPT = PACKAGE / "hooks" / "guard_destructive.py"
TILDE = "~"
GIT = ["git", "-c", "user.name=fixture", "-c", "user.email=fixture", "-c", "init.defaultBranch=main", "-c", "commit.gpgsign=false"]
TRACE_RE = re.compile(r"\[IMP:(\d+)\]\[([A-Za-z_.]+)\]\[([A-Z_]+)\]")
JUDGES = ("qa", "reviewer", "searcher", "methodology-claude:qa", "methodology-claude:reviewer", "methodology-claude:searcher")
# Judge matrices: (command template, text the deny reason must hold). Templates take project, wt (a sibling worktree) and scratch (a
# scratch root outside the project); every denied command is a rule the neutral owners forbid to a judge (roles/qa.md QA-204 and QA-205).
JUDGE_DENIED = [
    ("git worktree add {scratch}/judge-wt -b judge", "git worktree"),
    ("git worktree remove {wt}", "git worktree"),
    ("git worktree prune", "git worktree"),
    ("git worktree move {wt} {wt}-moved", "git worktree"),
    ("git update-ref refs/heads/slice HEAD", "git update-ref"),
    ("git update-ref -d refs/heads/slice", "git update-ref"),
    ("git config user.name judge", "git config"),
    ("git config core.fileMode false", "git config"),
    ("git config --add core.hooksPath x", "git config"),
    ("git config --unset core.hooksPath", "git config"),
    ("git config set core.fileMode false", "git config"),
    ("git config --file {project}/.git/config core.fileMode false", "git config"),
    ("git -C {wt} config user.name judge", "git config"),
    ("cd {wt}\ngit config --global user.name judge", "git config"),
    ("git fetch", "git fetch"),
    ("git fetch origin main", "git fetch"),
    ("git -C {wt} fetch --all", "git fetch"),
    ("chmod +x a.py", "chmod a.py"),
    ("chmod -x a.py", "chmod a.py"),
    ("chmod -R 755 .", "chmod ."),
    ("chown fixture a.py", "chown a.py"),
    ("chgrp staff {wt}/a.py", "chgrp"),
    ("truncate -s 0 a.py", "truncate a.py"),
    ("truncate -s0 a.py", "truncate a.py"),
    ("perl -pi -e 's/1/2/' a.py", "perl -i a.py"),
    ("perl -i.bak -pe 's/1/2/' a.py", "perl -i a.py"),
    ("perl -0777 -pi -e 's/1/2/' {wt}/a.py", "perl -i"),
    ("dd if=/dev/zero of=a.py count=1", "dd of=a.py"),
    ("ln -s a.py link", "ln link"),
    ("ln -sf {scratch}/x a.py", "ln a.py"),
    ("ln -s {scratch}/x .", "ln ."),
    ("install -m 755 {scratch}/x.sh tool.sh", "install tool.sh"),
    ("install -d newdir", "install newdir"),
    ("install -t . {scratch}/x", "install ."),
    ("bash -c 'chmod +x a.py'", "chmod a.py"),
    ("echo ok && chmod 600 a.py", "chmod a.py"),
    ("sudo chmod +x a.py", "chmod a.py"),
    # Abbreviated long options (git and GNU tools take any unambiguous prefix); an option that is neither a known option nor a unique
    # prefix of one is denied for git config, because the judge cannot be sure it does not write.
    ("git config --rem s", "git config"),
    ("git config --remove s", "git config"),
    ("git config --unset-a k", "git config"),
    ("git config --ren a b", "git config"),
    ("git config --repl k v", "git config"),
    ("git config --ad k v", "git config"),
    ("git config --uns k", "git config"),
    ("git config --glo --unset-a k", "git config"),
    ("git config --get --rem s", "git config"),
    ("git config --bogus-option k", "git config"),
    ("git config --fil {project}/.git/config --unset-a k", "git config"),
    ("git -C {wt} config --rem s", "git config"),
    ("bash -c 'git config --rem s'", "git config"),
    ("sed -Ei 's/1/2/' a.py", "sed a.py"),
    ("sed -ni 's/1/2/p' a.py", "sed a.py"),
    ("sed -nEi 's/1/2/p' a.py", "sed a.py"),
    ("sed --in-place 's/1/2/' a.py", "sed a.py"),
    ("sed --in 's/1/2/' a.py", "sed a.py"),
    ("sed -e 's/1/2/' --in-place a.py", "sed a.py"),
    # The script attached to the expression option, or taken from a script file, is not the first operand: the file after it is the target.
    ("sed -i -e's/1/2/' a.py", "sed a.py"),
    ("sed -Ei -e's/1/2/' a.py", "sed a.py"),
    ("sed -i --expression=s/1/2/ a.py", "sed a.py"),
    ("sed --expression=s/1/2/ -i a.py", "sed a.py"),
    ("sed -i.bak -es/1/2/ a.py", "sed a.py"),
    ("chmod --ref=a.py b.py", "chmod b.py"),
    ("chown --ref a.py b.py", "chown b.py"),
    ("ln -s --target-d . {scratch}/x", "ln ."),
    ("ln --target-directory=. {scratch}/x", "ln ."),
    ("install --target . {scratch}/x", "install ."),
    ("install --target-directory=. {scratch}/x", "install ."),
    ("truncate --refer {scratch}/s b.py", "truncate b.py"),
    ("cp -t . {scratch}/x", "cp ."),
    ("cp --target-directory=. {scratch}/x", "cp ."),
    ("cp --target-d . {scratch}/x", "cp ."),
    ("mv --target-directory=. {scratch}/x", "mv ."),
    ("mv -t . {scratch}/x", "mv ."),
]
JUDGE_ALLOWED = [
    "git config --get user.name",
    "git config --get-all remote.origin.fetch",
    "git config --get-a remote.origin.fetch",
    "git config --get-r remote",
    "git config --li",
    "git config --list --show-o",
    "git config --nam --list",
    "git config --glo --get core.editor",
    "git config --def=zz --get nonexistent.key",
    "git config --get-regexp remote",
    "git config --list",
    "git config -l",
    "git config user.name",
    "git config get user.name",
    "git config list",
    "git config --global --get core.editor",
    "git config --file {scratch}/c.cfg core.fileMode false",
    "git worktree list",
    "git worktree list --porcelain",
    "git status --short; git log -1; git diff --stat; git rev-parse HEAD; git show-ref",
    "git -C {scratch}/copy fetch",
    "chmod +x {scratch}/copy/a.py",
    "chmod -R u+w {scratch}/copy",
    "chmod -R u+w build",
    "chown fixture {scratch}/copy/a.py",
    "truncate -s 0 {scratch}/log.txt",
    "truncate -r a.py {scratch}/shadow.txt",
    "perl -ne 'print' a.py",
    "perl -Mstrict -e 'print 1'",
    "truncate --refer a.py {scratch}/shadow.txt",
    "chmod --ref=a.py {scratch}/copy/a.py",
    "ln -s --target-d {scratch}/bin a.py",
    "install --target {scratch}/bin a.py",
    "cp -t {scratch}/bin a.py",
    "cp --target-directory={scratch}/bin a.py",
    "sed -n 's/1/2/p' a.py",
    "sed -E 's/i/j/' a.py",
    "sed -n -e '/i/p' a.py",
    "sed -Ei 's/1/2/' {scratch}/copy/a.py",
    "sed --in-place 's/1/2/' {scratch}/copy/a.py",
    "sed -i -e 's/1/2/' /private/tmp/x/a.py",
    "sed -i -e's/1/2/' {scratch}/copy/a.py",
    "sed -n p a.py",
    "perl -pe 's/1/2/' a.py > {scratch}/out.txt",
    "perl -pi -e 's/1/2/' {scratch}/copy/a.py",
    "dd if=a.py of={scratch}/a.bin",
    "dd if=/dev/zero of=/dev/null count=1",
    "ln -s {project}/a.py {scratch}/link",
    "install -m 755 a.py {scratch}/bin/a.py",
    "install -d {scratch}/bin",
    "install -t {scratch}/bin a.py",
    "rsync -a --exclude .git {project}/ {scratch}/copy/",
    "git archive HEAD | tar -x -C {scratch}",
    "rsync -a --exclude .git {wt}/ {scratch}/copy/ && cd {scratch}/copy && chmod +x a.py && perl -pi -e 's/1/2/' a.py && truncate -s 0 a.py",
]
# Branch forms are judged by form (the judge may list branches; every other form moves a ref). Fetch is denied in every form, the dry run
# included: a dry run still adds objects to the object store and a judge has no need to fetch (roles/qa.md QA-204).
# Templates take project, wt and scratch like the matrices above. The denied list holds branch deletion with force, which the general
# classifier also asks about, so it is kept out of JUDGE_DENIED (that matrix must stay silent for the general classifier).
JUDGE_GIT_DENIED = [
    ("git branch feature", "git branch"),
    ("git branch feature HEAD", "git branch"),
    ("git branch -v feature", "git branch"),
    ("git branch --sort committerdate feature", "git branch"),
    ("git branch --track feature origin/main", "git branch"),
    ("git branch -- feature", "git branch"),
    ("git branch -d feature", "git branch"),
    ("git branch -D feature", "git branch"),
    ("git branch -dr origin/feature", "git branch"),
    ("git branch -Dr origin/feature", "git branch"),
    ("git branch --delete feature", "git branch"),
    ("git branch -m old new", "git branch"),
    ("git branch -M old new", "git branch"),
    ("git branch --move old new", "git branch"),
    ("git branch -c old new", "git branch"),
    ("git branch -C old new", "git branch"),
    ("git branch --copy old new", "git branch"),
    ("git branch --set-upstream-to=origin/main", "git branch"),
    ("git branch --set-upstream-to origin/main", "git branch"),
    ("git branch -u origin/main", "git branch"),
    ("git branch --unset-upstream", "git branch"),
    ("git branch -f feature HEAD", "git branch"),
    ("git branch --force feature HEAD", "git branch"),
    ("git branch -f", "git branch"),
    ("git branch --edit-description", "git branch"),
    ("git branch --list --delete feature", "git branch"),
    ("git branch --contains HEAD -d feature", "git branch"),
    ("git branch -a -D feature", "git branch"),
    # Abbreviated long options: git accepts any unambiguous prefix, so these really rename, copy or delete; an ambiguous or unknown long
    # option cannot be told from a change and is denied; -a and -r are filters, not the list mode, so a name after them is a branch name.
    ("git branch -a --mov feature renamed", "git branch"),
    ("git branch --all --cop keep keep2", "git branch"),
    ("git branch -r --del origin/x", "git branch"),
    ("git branch --remotes --del origin/x", "git branch"),
    ("git branch --mo a b", "git branch"),
    ("git branch --mov a b", "git branch"),
    ("git branch --cop a b", "git branch"),
    ("git branch --de x", "git branch"),
    ("git branch --dele x", "git branch"),
    ("git branch --forc x HEAD", "git branch"),
    ("git branch --for x HEAD", "git branch"),
    ("git branch --co a b", "git branch"),
    ("git branch --edit-d", "git branch"),
    ("git branch --set-upstream-t=origin/main", "git branch"),
    ("git branch --unset-u", "git branch"),
    ("git branch --bogus", "git branch"),
    ("git branch --list --bogus", "git branch"),
    ("git branch --no-move a b", "git branch"),
    ("git branch --list --mov a b", "git branch"),
    ("git branch --cont HEAD --del x", "git branch"),
    ("git branch -a feature", "git branch"),
    ("git branch -r feature", "git branch"),
    ("git branch --all feature", "git branch"),
    ("git branch --remotes feature", "git branch"),
    ("git branch --so k feature", "git branch"),
    ("git -C {wt} branch -a --mov a b", "git branch"),
    ("bash -c 'git branch -r --del x'", "git branch"),
    ("cd {wt}\ngit branch --all --cop a b", "git branch"),
    ("git -C {wt} branch feature", "git branch"),
    ("cd {wt}\ngit branch feature", "git branch"),
    ("bash -c 'git branch feature'", "git branch"),
    ("echo ok && git branch -d feature", "git branch"),
    ("git fetch --dry-run", "git fetch"),
    ("git fetch --dry-run origin main", "git fetch"),
    ("git fetch origin --dry-run", "git fetch"),
    ("git fetch --all --dry-run", "git fetch"),
    ("git fetch -v --dry-run --prune", "git fetch"),
    ("git fetch --no-dry-run --dry-run", "git fetch"),
    ("git -C {wt} fetch --dry-run", "git fetch"),
    ("cd {wt}\ngit fetch --dry-run", "git fetch"),
    ("bash -c 'git fetch --dry-run'", "git fetch"),
    ("echo ok && git fetch --dry-run", "git fetch"),
    ("git fetch --no-dry-run", "git fetch"),
    ("git fetch --dry-run --no-dry-run", "git fetch"),
    ("git fetch origin --dry-run --no-dry-run", "git fetch"),
    ("git fetch -n", "git fetch"),
    ("git fetch --all", "git fetch"),
    ("git fetch --prune", "git fetch"),
    ("git fetch origin -- --dry-run", "git fetch"),
    ("git -C {wt} fetch --no-dry-run", "git fetch"),
]
JUDGE_GIT_ALLOWED = [
    "git branch",
    "git branch -a",
    "git branch -r",
    "git branch -v",
    "git branch -vv",
    "git branch -avv",
    "git branch --all",
    "git branch --remotes",
    "git branch --verbose",
    "git branch --list",
    "git branch --list 'feat*'",
    "git branch -l 'feat*'",
    "git branch -a --list 'origin/*'",
    "git branch -r --list 'origin/*'",
    "git branch --contains HEAD",
    "git branch --contains",
    "git branch --no-contains HEAD",
    "git branch --merged HEAD",
    "git branch --merged",
    "git branch --no-merged main",
    "git branch --points-at HEAD",
    "git branch --sort committerdate",
    "git branch --sort=-committerdate -v",
    "git branch --format '%(refname:short)'",
    "git branch --show-current",
    "git branch --color=never",
    "git branch --abbrev=7 -v",
    "git branch -a --contains HEAD",
    "git -C {wt} branch --contains HEAD",
    "git branch --list | wc -l",
    "git branch --contains HEAD | grep -c slice",
    "git branch -r -v",
    "git branch -a -v",
    "git branch -l",
    "git branch --li",
    "git branch --lis 'feat*'",
    "git branch -a --li 'origin/*'",
    "git branch --rem",
    "git branch --all --verb",
    "git branch --cont HEAD",
    "git branch --no-cont HEAD",
    "git branch --me HEAD",
    "git branch --no-me main",
    "git branch --po HEAD",
    "git branch --sh",
    "git branch --so committerdate",
    "git branch --form '%(refname:short)'",
    "git branch --colo=never",
    "git branch --abb=7 -v",
]
# Judge scratch rule: the judge's own report may go to any root outside the project and its worktrees; nothing inside them is writable,
# the evidence directory of the project included (the guard cannot tell a granted evidence root inside the project from project files).
JUDGE_SCRATCH_SILENT = [
    "python3 -m pytest -q > {scratch}/report.txt 2>&1",
    "python3 -m pytest -q 2>&1 | tee {scratch}/report.txt",
    "python3 -m pytest -q 2>&1 | tee -a {scratch}/evidence/report.txt",
    "git diff > {scratch}/diff.patch",
    "echo note >> {scratch}/notes/run.log",
    "echo note 2> {scratch}/err.log",
    "cp a.py {scratch}/a.py",
    "cp -p a.py {scratch}/evidence/a.py",
    "cp a.py {scratch}/",
    "touch {scratch}/marker",
    "rm -f {scratch}/old.txt",
    "mv {scratch}/a.tmp {scratch}/a.txt",
    "bash -c 'echo ok > {scratch}/nested.txt'",
    "cd {scratch} && echo ok > local.txt && tee local2.txt < local.txt",
]
JUDGE_PROJECT_DENIED = [
    ("python3 -m pytest -q > {project}/.methodology/evidence/report.txt 2>&1", "(writing "),
    ("python3 -m pytest -q >> {project}/.methodology/evidence/report.txt", "(writing "),
    ("python3 -m pytest -q 2> {project}/.methodology/evidence/err.txt", "(writing "),
    ("echo ok > .methodology/evidence/r.txt", "(writing "),
    ("cd {project}/.methodology && echo ok > evidence/r.txt", "(writing "),
    ("echo ok > {wt}/.methodology/evidence/r.txt", "(writing "),
    ("bash -c 'echo ok > {project}/.methodology/evidence/r.txt'", "(writing "),
    ("python3 -m pytest -q 2>&1 | tee {project}/.methodology/evidence/log.txt", "(tee "),
    ("python3 -m pytest -q 2>&1 | tee -a {project}/.methodology/evidence/log.txt", "(tee "),
    ("python3 -m pytest -q 2>&1 | tee .methodology/evidence/log.txt", "(tee "),
    ("python3 -m pytest -q 2>&1 | tee {wt}/.methodology/evidence/log.txt", "(tee "),
    ("cp a.py {project}/.methodology/evidence/a.py", "(cp "),
    ("cp a.py .methodology/evidence/a.py", "(cp "),
    ("cp a.py {project}/.methodology/evidence/", "(cp "),
    ("cp a.py {wt}/.methodology/evidence/a.py", "(cp "),
    ("touch {project}/.methodology/evidence/marker", "(touch "),
    ("touch .methodology/evidence/marker", "(touch "),
    ("echo ok > {project}/report.txt", "(writing "),
    ("echo ok > {project}/sub/report.txt", "(writing "),
    ("cp a.py {project}/copy.py", "(cp "),
]
DEFAULT_SAFE_PREFIXES = ("/tmp", "/private/tmp", "/var/folders", "/private/var/folders")
DESTRUCTIVE = [
    "git push --force origin main",
    "git push -f",
    "git push origin +main",
    "git reset --hard HEAD~3",
    "git branch -D feature",
    "git filter-repo --invert-paths --path notes",
    "git stash drop",
    "sqlite3 app.db 'DROP TABLE users'",
    "psql -c \"DROP TABLE users\"",
    "rm -rf " + TILDE + "/Documents",
    "rm -rf $HOME/Documents",
    "rm -rf /etc/something",
    "rm -rf ../other",
    "rm -rf .",
    "rm -rf *",
    "bash -c 'rm -rf " + TILDE + "/x'",
    "find / -name '*.log' -delete",
    "git push --delete origin feature",
    "git push origin :feature",
    "git push --mirror",
]
BENIGN = [
    "git push origin main",
    "git push origin HEAD:refs/heads/main",
    "git config --get user.name",
    "git worktree list",
    "git status",
    "rm -rf build",
    "rm -rf ./dist",
    "rm -rf sub/*.egg-info",
    "git checkout -- .",
    "git clean -fdx",
    "git filter-repo --version",
    "rm file.txt",
    "echo force; echo DROP TABLE users",
    "find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null; python3 -m pytest -q 2>&1 | tail -3",
    "cat > t.py <<'EOF'\nimport os\nos.system('rm -rf /')\nSQL = 'DROP TABLE users'\nEOF",
]


# region FUNC_make_project [DOMAIN(6): Testing; CONCEPT(6): Fixture; TECH(5): pathlib]
## @purpose Build a project directory that declares nothing, because the guard no longer needs a declaration, optionally with an AGENTS.md of arbitrary text.
## @uses pathlib.Path.mkdir, pathlib.Path.write_text
## @io Input: base Path of an owned empty directory; agents_text str or None. Output: Path of base/proj, created. Side effects: creates the directory and, when given, AGENTS.md. Guarantees: nothing in the project mentions conventions unless the caller passes such text.
##   Raises: OSError for a read-only base. System importance: 6. Example: make_project(tmp_path) returns tmp_path/proj with no files.
## @complexity 2
def make_project(base, agents_text=None):
    project = base / "proj"
    project.mkdir()
    if agents_text is not None:
        (project / "AGENTS.md").write_text(agents_text)
    return project
# endregion FUNC_make_project


# region FUNC_make_repo [DOMAIN(6): Testing; CONCEPT(7): WorktreeFixture; TECH(6): git]
## @purpose Turn the project into a git repository with one committed file and add a sibling worktree, the layout a parallel slice uses.
## @uses subprocess.run
## @io Input: project Path. Output: Path of the sibling worktree base/proj-wt-slice on branch slice. Side effects: git init, add, commit and worktree add through the real git; the commit identity is passed by option and no global configuration is read for it.
##   Guarantees: a.py holds VALUE = 1 in the first commit. Raises: subprocess.CalledProcessError when git fails. System importance: 7. Example: after the call git worktree list shows two entries.
## @complexity 3
def make_repo(project):
    subprocess.run(GIT + ["init", "-q", str(project)], check=True)
    (project / "a.py").write_text("VALUE = 1\n")
    subprocess.run(GIT + ["-C", str(project), "add", "-A"], check=True)
    subprocess.run(GIT + ["-C", str(project), "commit", "-qm", "init"], check=True)
    worktree = project.parent / "proj-wt-slice"
    subprocess.run(GIT + ["-C", str(project), "worktree", "add", "-q", "-b", "slice", str(worktree)], check=True)
    LOGGER.info("[IMP:7][make_repo][REPOSITORY] repository and sibling worktree created")
    return worktree
# endregion FUNC_make_repo


# region FUNC_invoke [DOMAIN(8): Testing; CONCEPT(8): RealProcessBoundary; TECH(7): subprocess]
## @purpose Run the guard script as a separate process with exactly the stdin text given, in a controlled environment.
## @uses subprocess.run, sys.executable
## @io Input: payload_text str written to stdin; env_extra dict of str to str or None (None removes a variable); trace bool that sets METHODOLOGY_HOOK_LOG. Output: the subprocess.CompletedProcess with text stdout and stderr.
##   Side effects: one child process; the environment is the test environment without any METHODOLOGY variable and without CLAUDE_PROJECT_DIR, plus a scratch prefix list that matches nothing. Guarantees: no shell, a 60 second timeout. Raises: subprocess.TimeoutExpired.
##   System importance: 8. Example: invoke of the text not json returns exit status 0 and empty stdout.
## @complexity 3
def invoke(payload_text, env_extra=None, trace=False):
    env = {k: v for k, v in os.environ.items() if not k.startswith("METHODOLOGY_") and k != "CLAUDE_PROJECT_DIR"}
    env["METHODOLOGY_GUARD_SAFE_PREFIXES"] = "/nonexistent-scratch"
    if trace:
        env["METHODOLOGY_HOOK_LOG"] = "1"
    for key, value in (env_extra or {}).items():
        if value is None:
            env.pop(key, None)
        else:
            env[key] = value
    return subprocess.run([sys.executable, str(SCRIPT)], input=payload_text, capture_output=True, text=True, env=env, timeout=60)
# endregion FUNC_invoke


# region FUNC_run_guard [DOMAIN(9): Testing; CONCEPT(8): HookInvocation; TECH(6): subprocess, json]
## @purpose Invoke the guard exactly as the PreToolUse hook does, show the important decision trace, and return the decision and reason.
## @uses test_guard.invoke, json.loads, builtins.print
## @io Input: command str; project Path; cwd Path or None; env_extra dict or None; tool str; agent str or None (sets agent_type); allow_error bool. Output: tuple of (decision str or None, reason str, exit code int). A temporary HOME under the project parent is always set.
##   Side effects: one hook process with tracing on; the importance 9 and 10 trace lines are printed before returning. Guarantees: unless allow_error is True an importance 10 trace event fails the call; stdout is empty or one JSON line with only hookSpecificOutput and hookEventName PreToolUse.
##   Raises: AssertionError for an unexpected critical event or a malformed answer. System importance: 9. Example: a force push in a plain project returns the decision ask, a reason naming force push and exit code 0.
## @complexity 5
def run_guard(command, project, cwd=None, env_extra=None, tool="Bash", agent=None, allow_error=False):
    env = {"CLAUDE_PROJECT_DIR": str(project), "HOME": str(project.parent / "home")}
    env.update(env_extra or {})
    payload = {"tool_name": tool, "tool_input": {"command": command}, "cwd": str(cwd or project)}
    if agent:
        payload["agent_type"] = agent
    done = invoke(json.dumps(payload), env, trace=True)
    events = [(int(m.group(1)), m.group(2), m.group(3)) for m in (TRACE_RE.match(line) for line in done.stderr.splitlines()) if m]
    for line in done.stderr.splitlines():
        if TRACE_RE.match(line) and int(TRACE_RE.match(line).group(1)) >= 9:
            print(line)
    if not allow_error:
        assert not [e for e in events if e[0] == 10], done.stderr
    if not done.stdout.strip():
        return None, "", done.returncode
    assert done.stdout.count("\n") == 1
    value = json.loads(done.stdout)
    assert list(value) == ["hookSpecificOutput"]
    out = value["hookSpecificOutput"]
    assert sorted(out) == ["hookEventName", "permissionDecision", "permissionDecisionReason"] and out["hookEventName"] == "PreToolUse"
    return out["permissionDecision"], out["permissionDecisionReason"], done.returncode
# endregion FUNC_run_guard


# region FUNC_show_records [DOMAIN(8): Testing; CONCEPT(9): AccessibleTrajectory; TECH(5): logging]
## @purpose Expose captured in-process guard records of importance 7 to 10 before the assertions.
## @uses builtins.print
## @io Input: records list of logging.LogRecord. Output: None. Side effects: prints the messages with importance 7 to 10 that the guard logger produced. Guarantees: only the guard's own records are printed. Raises: none. System importance: 8. Example: a direct main call prints its FAIL record.
## @complexity 2
def show_records(records):
    for record in records:
        message = record.getMessage()
        match = TRACE_RE.match(message)
        if record.name == "guard_destructive" and match and 7 <= int(match.group(1)) <= 10:
            print(message)
# endregion FUNC_show_records


# region FUNC_assert_scratch_advice [DOMAIN(8): Testing; CONCEPT(8): JudgeIsolationAdvice; TECH(5): assert]
## @purpose Hold the deny reason of a read-only agent to the neutral isolation rules: its advice must send the judge to a copy without .git in a granted scratch root and must never recommend creating a worktree or a recursive copy. The rule text that names what was denied may hold the word worktree, because the denied command itself can be a worktree change.
## @uses builtins.str.lower
## @io Input: reason str of a deny decision. Output: None. Side effects: none. Guarantees: the reason names the rsync form that excludes .git and the git archive form; the advice part, which starts at the words Run any check, holds neither the word worktree nor the recursive copy recommendation. Raises: AssertionError on any difference.
##   System importance: 8. Example: a reason ending with the rsync and git archive advice passes; one whose advice recommends a worktree fails.
## @complexity 2
def assert_scratch_advice(reason):
    assert "Run any check" in reason
    advice = reason.split("Run any check", 1)[1].lower()
    assert "rsync -a --exclude .git" in reason and "git archive HEAD | tar -x -C" in reason
    assert "worktree" not in advice and "cp -r" not in reason.lower() and "granted scratch root" in reason
# endregion FUNC_assert_scratch_advice


# region FUNC_test_destructive_commands_ask [DOMAIN(9): Safety; CONCEPT(9): StopBeforeDestructive; TECH(7): pytest, subprocess]
## @purpose Verify that every destructive command asks, with exit status 0, in a project that declares nothing, and that the reason names the owner-confirmation rule without the old convention wording.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: command str from DESTRUCTIVE and tmp_path. Output: None after the assertions. Side effects: one hook process. Guarantees: the decision is ask and the exit code 0; the reason starts with the destructive-command phrase, points at process/safety.md and holds no convention number. Raises: AssertionError on any difference.
##   System importance: 9. Example: git push --force origin main returns ask with the rule force push.
## @complexity 3
@pytest.mark.parametrize("command", DESTRUCTIVE)
def test_destructive_commands_ask(command, tmp_path):
    decision, reason, code = run_guard(command, make_project(tmp_path))
    print("[IMP:9][test_destructive_commands_ask][DECISION] %r -> %s" % (command, decision))
    assert (decision, code) == ("ask", 0)
    assert reason.startswith("Destructive command (") and "process/safety.md" in reason
    assert "CV-" not in reason and "Project Conventions" not in reason
# endregion FUNC_test_destructive_commands_ask


# region FUNC_test_benign_commands_silent [DOMAIN(9): Safety; CONCEPT(9): Precision; TECH(7): pytest, subprocess]
## @purpose Verify that ordinary commands, deletions inside the project, regenerable artefacts and heredoc text pass silently.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: command str from BENIGN and tmp_path. Output: None after the assertions. Side effects: one hook process. Guarantees: no decision, empty reason, exit code 0 and no critical trace event. Raises: AssertionError on any difference. System importance: 9.
##   Example: rm -rf build returns no decision.
## @complexity 2
@pytest.mark.parametrize("command", BENIGN)
def test_benign_commands_silent(command, tmp_path):
    decision, reason, code = run_guard(command, make_project(tmp_path))
    print("[IMP:9][test_benign_commands_silent][DECISION] %r -> %s" % (command[:60], decision))
    assert (decision, code) == (None, 0), reason
# endregion FUNC_test_benign_commands_silent


# region FUNC_test_reason_names_at_most_three_paths_and_not_the_command [DOMAIN(8): Safety; CONCEPT(8): ReasonDisclosure; TECH(6): pytest]
## @purpose Verify the reason invariant: at most three operands are named, and the full command text never appears.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: one hook process. Guarantees: with five outside operands the first three appear in order and the fourth and fifth do not. Raises: AssertionError on any difference. System importance: 8.
##   Example: rm -rf /outside-a through /outside-e names a, b and c only.
## @complexity 2
def test_reason_names_at_most_three_paths_and_not_the_command(tmp_path):
    command = "rm -rf /outside-a /outside-b /outside-c /outside-d /outside-e"
    decision, reason, _ = run_guard(command, make_project(tmp_path))
    print("[IMP:9][test_reason_names_at_most_three_paths_and_not_the_command][REASON] %s" % reason)
    assert decision == "ask"
    assert "(/outside-a, /outside-b, /outside-c)" in reason
    assert "/outside-d" not in reason and "/outside-e" not in reason and command not in reason
# endregion FUNC_test_reason_names_at_most_three_paths_and_not_the_command


# region FUNC_test_scratch_prefixes_and_tmpdir [DOMAIN(8): Safety; CONCEPT(8): ScratchScope; TECH(6): pytest, environment]
## @purpose Verify that the configured scratch prefixes are inside, a home directory is not, and that TMPDIR is added only when the defaults are in force.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: several hook processes. Guarantees: a path under a configured prefix is silent, a home directory outside every prefix asks; with the defaults an unknown root asks and becomes silent when TMPDIR names it; with the prefix list set TMPDIR adds nothing. Raises: AssertionError on any difference.
##   System importance: 8. Example: rm -rf of a path under the first default prefix is silent.
## @complexity 4
def test_scratch_prefixes_and_tmpdir(tmp_path):
    project = make_project(tmp_path)
    prefixes = os.pathsep.join(["/tmp", "/private/tmp"])
    assert run_guard("rm -rf /tmp/scratch-x", project, env_extra={"METHODOLOGY_GUARD_SAFE_PREFIXES": prefixes})[0] is None
    outside_home = {"METHODOLOGY_GUARD_SAFE_PREFIXES": prefixes, "HOME": "/nonexistent-home-for-test"}
    assert run_guard("rm -rf " + TILDE + "/scratch-x", project, env_extra=outside_home)[0] == "ask"
    unknown = "/nonexistent-tmp-root/work"
    defaults = {"METHODOLOGY_GUARD_SAFE_PREFIXES": None}
    assert run_guard("rm -rf %s/sub" % unknown, project, env_extra=dict(defaults, TMPDIR="/somewhere-else"))[0] == "ask"
    assert run_guard("rm -rf %s/sub" % unknown, project, env_extra=dict(defaults, TMPDIR=unknown))[0] is None
    assert run_guard("rm -rf %s/sub" % unknown, project, env_extra={"METHODOLOGY_GUARD_SAFE_PREFIXES": prefixes, "TMPDIR": unknown})[0] == "ask"
# endregion FUNC_test_scratch_prefixes_and_tmpdir


# region FUNC_test_deny_mode [DOMAIN(8): Safety; CONCEPT(8): HardenedMode; TECH(6): pytest]
## @purpose Verify that METHODOLOGY_GUARD_MODE=deny turns the ask into a deny, in any letter case, and that an unknown value keeps the ask.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: several hook processes. Guarantees: the values deny and DENY give deny, the values ask and strict give ask. Raises: AssertionError on any difference. System importance: 8. Example: a force push under deny returns deny.
## @complexity 2
def test_deny_mode(tmp_path):
    project = make_project(tmp_path)
    decisions = [run_guard("git push --force", project, env_extra={"METHODOLOGY_GUARD_MODE": value})[0] for value in ("deny", "DENY", "ask", "strict")]
    print("[IMP:9][test_deny_mode][DECISIONS] %s" % decisions)
    assert decisions == ["deny", "deny", "ask", "ask"]
# endregion FUNC_test_deny_mode


# region FUNC_test_other_tools_and_broken_payloads_are_silent [DOMAIN(9): Hooks; CONCEPT(9): NeverFailSession; TECH(7): subprocess, pytest]
## @purpose Verify that other tools, empty and broken payloads and payload shapes that cannot be processed never produce a decision, never fail, and keep stderr silent unless tracing is on, in which case the error class is traced.
## @uses test_guard.invoke, test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: several hook processes. Guarantees: exit status 0 and empty stdout in every case; stderr is empty by default; a string tool_input with tracing on yields exactly one importance 10 FAIL event naming AttributeError. Raises: AssertionError on any difference.
##   System importance: 9. Example: the payload text not json returns exit status 0, empty stdout and empty stderr.
## @complexity 5
def test_other_tools_and_broken_payloads_are_silent(tmp_path):
    project = make_project(tmp_path)
    assert run_guard("git push --force", project, tool="Edit") == (None, "", 0)
    texts = ["not json", "", "[1, 2]", "null", json.dumps({"tool_name": "Bash", "tool_input": "git push --force"}),
             json.dumps({"tool_name": "Bash", "tool_input": {"command": 42}, "cwd": str(project)})]
    for text in texts:
        done = invoke(text, {"CLAUDE_PROJECT_DIR": str(project)})
        print("[IMP:9][test_other_tools_and_broken_payloads_are_silent][SILENT] %r -> exit=%d stdout=%r stderr_chars=%d" % (text[:30], done.returncode, done.stdout, len(done.stderr)))
        assert done.returncode == 0 and done.stdout == "" and done.stderr == ""
    traced = invoke(json.dumps({"tool_name": "Bash", "tool_input": "git push --force"}), {"CLAUDE_PROJECT_DIR": str(project)}, trace=True)
    print(traced.stderr.strip())
    assert traced.returncode == 0 and traced.stdout == ""
    assert traced.stderr.splitlines() == ["[IMP:10][main][FAIL] kind=AttributeError"]
# endregion FUNC_test_other_tools_and_broken_payloads_are_silent


# region FUNC_test_recorded_false_alarms_are_silent [DOMAIN(9): Safety; CONCEPT(9): FalseAlarmRegression; TECH(7): pytest, git]
## @purpose Verify that the shapes that were false alarms in real sessions, replayed in a sibling worktree, are silent, while deleting the worktree itself asks.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; several hook processes. Guarantees: six replayed commands give no decision; rm -rf of the worktree gives ask. Raises: AssertionError on any difference. System importance: 9.
##   Example: cd into the worktree then removing __pycache__ directories and running the tests is silent.
## @complexity 5
def test_recorded_false_alarms_are_silent(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    recorded = [
        "cd %s && find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null; python3 -m pytest -q -p no:cacheprovider 2>&1 | tail -10" % wt,
        "cd %s && git rev-parse HEAD; git status --short; find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null; "
        "python3 -m pytest -q -p no:cacheprovider 2>&1 | tail -10" % wt,
        "cd %s && python3 -c \"\nimport ast\nast.parse(open('a.py').read())\nprint('OK')\n\"\n"
        "find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null\n"
        "python3 -m pytest -q -p no:cacheprovider 2>&1 | tail -10" % wt,
        "cd %s && python3 - <<'EOF'\npath = 'a.py'\nsrc = open(path).read()\nopen(path, 'w').write(src)\nEOF\n"
        "find . -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null; python3 -m pytest -q" % wt,
        "rm -rf pkgtest\nmkdir -p pkgtest/tools\ncat > pkgtest/tools/b.py <<'EOF'\nfrom . import a\nEOF\ncd pkgtest\npython3 -c \"\nfrom tools import *\n\"",
        "rm -rf %s/build" % wt,
    ]
    for command in recorded:
        decision, reason, _ = run_guard(command, project)
        print("[IMP:9][test_recorded_false_alarms_are_silent][REPLAY] %r -> %s" % (command[:70], decision))
        assert decision is None, "%r -> %s" % (command, reason)
    assert run_guard("rm -rf %s" % wt, project)[0] == "ask"
# endregion FUNC_test_recorded_false_alarms_are_silent


# region FUNC_test_git_precision [DOMAIN(9): Safety; CONCEPT(9): LossOfUncommittedWork; TECH(7): pytest, git]
## @purpose Verify that git commands ask only when uncommitted work would be lost: silent on a clean tree, asking over an edited file, asking for clean over untracked files, and asking in a worktree reached by cd.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository and worktree whose files are edited in the test; many hook processes. Guarantees: the quiet list is silent on the clean tree; after an edit each discarding command asks and names a.py; restoring the index stays silent; clean asks once an untracked file exists. Raises: AssertionError on any difference.
##   System importance: 9. Example: git checkout of a.py over an edit of a.py asks and the reason names a.py.
## @complexity 6
def test_git_precision(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    quiet = ["git checkout -- a.py", "git restore a.py", "git checkout -- .", "git checkout main", "git reset --hard", "git clean -fd",
             "git restore --staged a.py"]
    for command in quiet:
        assert run_guard(command, project)[0] is None, command
    (project / "a.py").write_text("VALUE = 2\n")
    for command in ["git checkout -- a.py", "git restore a.py", "git checkout a.py", "git checkout -- .", "git reset --hard"]:
        decision, reason, _ = run_guard(command, project)
        print("[IMP:9][test_git_precision][GIT] %r -> %s: %s" % (command, decision, reason[:80]))
        assert decision == "ask" and "a.py" in reason, command
    assert run_guard("git restore --staged a.py", project)[0] is None
    (project / "new.txt").write_text("untracked\n")
    assert run_guard("git clean -fd", project)[0] == "ask"
    (wt / "a.py").write_text("VALUE = 3\n")
    recorded = "cd %s && git checkout -- a.py && git status --short && find . -name __pycache__ -exec rm -rf {} +" % wt
    decision, reason, _ = run_guard(recorded, project)
    assert decision == "ask" and "a.py" in reason
# endregion FUNC_test_git_precision


# region FUNC_test_sql_only_through_a_client [DOMAIN(8): Safety; CONCEPT(7): DestructiveSQL; TECH(6): pytest]
## @purpose Verify that DROP and TRUNCATE ask only when sent to a SQL client, including through the client's own heredoc, and stay silent when written into a file or named in a test path.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: several hook processes. Guarantees: a sqlite3 heredoc with a table drop asks, a cat heredoc with the same words is silent, a pytest path with the words is silent, TRUNCATE to a client asks. Raises: AssertionError on any difference. System importance: 8.
##   Example: psql with a TRUNCATE TABLE argument asks.
## @complexity 3
def test_sql_only_through_a_client(tmp_path):
    project = make_project(tmp_path)
    assert run_guard("sqlite3 app.db <<'SQL'\nDROP TABLE users;\nSQL", project)[0] == "ask"
    assert run_guard("psql -c 'TRUNCATE TABLE users'", project)[0] == "ask"
    assert run_guard("cat > probe.py <<'EOF'\ncur.execute('DROP TABLE t')\nEOF", project)[0] is None
    assert run_guard("python3 -m pytest tests/test_drop_table.py -q", project)[0] is None
# endregion FUNC_test_sql_only_through_a_client


# region FUNC_test_active_without_declaration_and_owner_switch [DOMAIN(9): Safety; CONCEPT(9): ActivationDefault, OwnerSwitch; TECH(7): pytest]
## @purpose Verify the activation rule: the guard acts in a project with no AGENTS.md and in one with unrelated AGENTS.md text, an old scope word does not disable it, and only the value off, in any letter case, silences both the destructive rules and the read-only deny.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: several hook processes. Guarantees: no declaration gives ask; the words all, declared and an empty value keep the guard on; off and OFF give silence, also for a read-only agent writing into the project. Raises: AssertionError on any difference. System importance: 9.
##   Example: the scope value off makes a force push silent.
## @complexity 4
def test_active_without_declaration_and_owner_switch(tmp_path):
    bare = make_project(tmp_path)
    assert run_guard("git push --force", bare)[0] == "ask"
    other = tmp_path / "other"
    other.mkdir()
    (other / "AGENTS.md").write_text("Plain instructions that declare no conventions.\n")
    assert run_guard("git push --force", other)[0] == "ask"
    for value in ("all", "declared", ""):
        assert run_guard("git push --force", bare, env_extra={"METHODOLOGY_GUARD_SCOPE": value})[0] == "ask", value
    for value in ("off", "OFF", " Off "):
        assert run_guard("git push --force", bare, env_extra={"METHODOLOGY_GUARD_SCOPE": value})[0] is None, value
        assert run_guard("echo x > a.py", bare, env_extra={"METHODOLOGY_GUARD_SCOPE": value}, agent="qa")[0] is None, value
    assert run_guard("echo x > a.py", bare, agent="qa")[0] == "deny"
# endregion FUNC_test_active_without_declaration_and_owner_switch


# region FUNC_test_variables_artefacts_worktree_removal [DOMAIN(9): Safety; CONCEPT(8): VariablesAndArtefacts; TECH(7): pytest, git]
## @purpose Verify that variables assigned in the command are followed, regenerable artefacts are deleted silently anywhere, deleting find asks outside the project, forced worktree removal asks only over changes, and an unknown directory asks.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository and worktree with edits and a restore; many hook processes. Guarantees: each listed command yields the stated decision. Raises: AssertionError on any difference. System importance: 9.
##   Example: S assigned to the worktree, then cd into it and checking out an edited file, asks and names a.py.
## @complexity 6
def test_variables_artefacts_worktree_removal(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    (wt / "a.py").write_text("VALUE = 4\n")
    decision, reason, _ = run_guard("S=%s; cd $S && git checkout -q -- a.py" % wt, project)
    assert decision == "ask" and "a.py" in reason
    assert run_guard("S=%s/elsewhere; rm -rf \"$S\"" % tmp_path, project)[0] == "ask"
    assert run_guard("find %s/elsewhere -name __pycache__ -type d -prune -exec rm -rf {} +" % tmp_path, project)[0] is None
    assert run_guard("rm -rf %s/elsewhere/node_modules" % tmp_path, project)[0] is None
    assert run_guard("find %s/elsewhere -name '*.csv' -delete" % tmp_path, project)[0] == "ask"
    assert run_guard("git worktree remove --force %s" % wt, project)[0] == "ask"
    subprocess.run(GIT + ["-C", str(wt), "checkout", "-q", "--", "a.py"], check=True)
    assert run_guard("git worktree remove --force %s" % wt, project)[0] is None
    assert run_guard("cd $UNKNOWN_DIR_FOR_TEST && git checkout -- a.py", project)[0] == "ask"
# endregion FUNC_test_variables_artefacts_worktree_removal


# region FUNC_test_unbalanced_quote_does_not_hide_a_later_command [DOMAIN(8): Safety; CONCEPT(8): TokenizerFallback; TECH(6): pytest]
## @purpose Verify the recorded tokenizer fix: an unbalanced quote on one line must not hide a destructive command on a later line.
## @uses test_guard.make_project, test_guard.run_guard, guard_destructive.simple_commands
## @io Input: tmp_path. Output: None after the assertions. Side effects: one hook process and a direct call. Guarantees: the hook asks for the later rm line and the segmentation still returns the rm words. Raises: AssertionError on any difference. System importance: 8.
##   Example: an echo with an opening quote and a following line deleting an outside directory asks.
## @complexity 3
def test_unbalanced_quote_does_not_hide_a_later_command(tmp_path):
    command = "echo 'unbalanced\nrm -rf /outside-quote"
    decision, reason, _ = run_guard(command, make_project(tmp_path))
    print("[IMP:9][test_unbalanced_quote_does_not_hide_a_later_command][DECISION] %s: %s" % (decision, reason[:60]))
    assert decision == "ask" and "/outside-quote" in reason
    assert ["rm", "-rf", "/outside-quote"] in guard_destructive.simple_commands(command)
# endregion FUNC_test_unbalanced_quote_does_not_hide_a_later_command


# region FUNC_test_readonly_agents_are_denied_tree_changes [DOMAIN(9): Safety; CONCEPT(9): ReadOnlyJudge, NamespacedAgents; TECH(7): pytest, git]
## @purpose Verify that each of the six default read-only agent types, plain and plugin-namespaced and in any letter case, is denied commands that change the project tree or a worktree, is not denied a test run, a report redirected into a scratch root, or a scratch copy made without .git, that the deny reason recommends exactly that copy form, and that other agents and the root are unaffected.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: agent str from JUDGES and tmp_path. Output: None after the assertions. Side effects: a real repository and worktree; several hook processes per agent. Guarantees: two tree-changing commands give deny with the lower-cased agent type in the reason; a test run and a copy into scratch stay silent; the agent types coder, methodology-claude:coder and none give no deny for the same commands. Raises: AssertionError on any difference.
##   System importance: 9. Example: the namespaced qa agent writing a file in the project by redirection is denied.
## @complexity 5
@pytest.mark.parametrize("agent", JUDGES)
def test_readonly_agents_are_denied_tree_changes(agent, tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    denied = ["echo x > a.py", "git -C %s commit -am x" % wt]
    for spelling in (agent, agent.upper()):
        for command in denied:
            decision, reason, _ = run_guard(command, project, agent=spelling)
            print("[IMP:9][test_readonly_agents_are_denied_tree_changes][DENY] %s %r -> %s" % (spelling, command[:30], decision))
            assert decision == "deny" and "Read-only agent (%s)" % agent in reason, command
            assert_scratch_advice(reason)
    for command in ["python3 -m pytest -q 2>&1 | tail -3", "cp a.py %s/" % scratch, "echo x > /dev/null",
                    "python3 -m pytest -q > %s/report.txt 2>&1" % scratch, "git archive HEAD | tar -x -C %s" % scratch]:
        assert run_guard(command, project, agent=agent)[0] is None, command
    for other in ("coder", "methodology-claude:coder", "architect", None):
        assert run_guard("echo x > a.py", project, agent=other)[0] is None, other
# endregion FUNC_test_readonly_agents_are_denied_tree_changes


# region FUNC_test_readonly_matrix_for_qa [DOMAIN(9): Safety; CONCEPT(9): ReadOnlyJudge; TECH(7): pytest, git]
## @purpose Verify the full denied and allowed command matrices for a read-only qa agent, including a stash in another worktree from the agent's own worktree.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with two worktrees; many hook processes. Guarantees: eight tree-changing commands are denied and name the qa agent; eight reads, tests, scratch copies, redirections to /dev and cache clean-ups are silent; the isolated worktree case is denied; the coder agent and the root may stash. Raises: AssertionError on any difference.
##   System importance: 9. Example: git stash push with a pathspec after a cd into the coder worktree is denied for qa.
## @complexity 6
def test_readonly_matrix_for_qa(tmp_path):
    project = make_project(tmp_path, agents_text="Instructions.\n")
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    denied = ["cd %s\ngit stash push -u -m qa-check -- Doxyfile 2>&1 | tail -3" % wt, "git -C %s commit -am x" % wt, "echo x > a.py",
              "sed -i '' 's/1/2/' a.py", "git -C %s checkout -- a.py" % wt, "rm -rf docs", "git tag v1",
              "git --work-tree=%s/old --git-dir=%s/.git checkout HEAD -- ." % (scratch, project)]
    for command in denied:
        decision, reason, _ = run_guard(command, project, agent="qa")
        print("[IMP:9][test_readonly_matrix_for_qa][DENY] %r -> %s: %s" % (command[:50], decision, reason[:70]))
        assert decision == "deny" and "Read-only agent (qa)" in reason, command
        assert_scratch_advice(reason)
    allowed = ["python3 -m pytest -q 2>&1 | tail -3", "git status --short; git diff; git log -1; git stash list; git branch --show-current 2>&1",
               "git tag | grep -i slice; git tag -l 'v3-*'", "cp a.py \\\n   AGENTS.md \\\n   %s/" % scratch,
               "echo x > /dev/null", "python3 -m pytest -q > %s/out.txt" % scratch,
               "rsync -a --exclude .git %s/ %s/copy/ && cd %s/copy && sed -i '' 's/1/2/' a.py" % (wt, scratch, scratch),
               "git archive HEAD | tar -x -C %s && python3 -m pytest -q %s > %s/report.txt 2>&1" % (scratch, scratch, scratch),
               "find . -name __pycache__ -type d -prune -exec rm -rf {} +"]
    for command in allowed:
        decision, reason, _ = run_guard(command, project, agent="qa")
        assert decision is None, "%r -> %s" % (command, reason)
    qa_wt = tmp_path / "proj-wt-qa"
    subprocess.run(GIT + ["-C", str(project), "worktree", "add", "-q", "-b", "qa", str(qa_wt)], check=True)
    decision, _, _ = run_guard("cd %s\ngit stash push -u -m x -- Doxyfile 2>&1 | tail -3" % wt, qa_wt, cwd=qa_wt, agent="qa")
    assert decision == "deny", "a qa agent isolated in its own worktree must not stash in the coder worktree"
    assert run_guard("cd %s && git stash push -u" % wt, project, agent="coder")[0] is None
    assert run_guard("cd %s && git stash push -u" % wt, project)[0] is None
# endregion FUNC_test_readonly_matrix_for_qa


# region FUNC_test_judge_is_denied_git_state_and_file_changes [DOMAIN(9): Safety; CONCEPT(9): ReadOnlyJudge, GitStateMutation, FileModeMutation; TECH(7): pytest, git]
## @purpose Verify that a read-only qa agent is denied every command of the JUDGE_DENIED matrix: worktree changes, ref moves, config writes (also through a global scope or a cd), fetch, and chmod, chown, chgrp, truncate, perl in-place edits, dd of=, ln and install on project paths, in a nested shell, behind another command or behind sudo.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard, test_guard.assert_scratch_advice
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; one hook process per command; no command is executed. Guarantees: each command gives deny, names the qa agent and the expected rule, recommends the scratch copy form, holds at most one project operand and never repeats the command text. Raises: AssertionError on any difference.
##   System importance: 9. Example: chmod with a mode and a project file is denied with the rule text chmod a.py.
## @complexity 5
def test_judge_is_denied_git_state_and_file_changes(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    for template, expected in JUDGE_DENIED:
        command = template.format(project=project, wt=wt, scratch=scratch)
        decision, reason, _ = run_guard(command, project, agent="qa")
        print("[IMP:9][test_judge_is_denied_git_state_and_file_changes][DENY] %r -> %s: %s" % (template[:48], decision, reason[:90]))
        assert decision == "deny" and "Read-only agent (qa)" in reason, command
        assert "(%s" % expected in reason, "%r: reason %r lacks %r" % (command, reason, expected)
        assert command == expected or command not in reason  # a bare git fetch is its own rule name
        assert_scratch_advice(reason)
# endregion FUNC_test_judge_is_denied_git_state_and_file_changes


# region FUNC_test_judge_keeps_read_only_queries_and_scratch_work [DOMAIN(9): Safety; CONCEPT(9): Precision, ScratchCopy; TECH(7): pytest, git]
## @purpose Verify that a read-only qa agent is not interrupted by the read-only forms next to the new rules (config get, list and a bare key, worktree list, status, log, diff, show-ref) nor by work in a scratch root outside the project: the same commands on a scratch copy, the isolation shapes of the neutral rules, and a scratch config file.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; one hook process per command; no command is executed. Guarantees: every command of JUDGE_ALLOWED gives no decision, exit code 0 and no importance 10 event, including the rsync copy without .git followed by a cd into the copy and changes there. Raises: AssertionError on any difference.
##   System importance: 9. Example: config with the get flag, and chmod of a file under the scratch root, are silent.
## @complexity 4
def test_judge_keeps_read_only_queries_and_scratch_work(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    for template in JUDGE_ALLOWED:
        command = template.format(project=project, wt=wt, scratch=scratch)
        decision, reason, code = run_guard(command, project, agent="qa")
        print("[IMP:9][test_judge_keeps_read_only_queries_and_scratch_work][ALLOW] %r -> %s" % (template[:60], decision))
        assert (decision, code) == (None, 0), "%r -> %s" % (command, reason)
# endregion FUNC_test_judge_keeps_read_only_queries_and_scratch_work


# region FUNC_test_every_judge_form_is_denied_each_new_rule_family [DOMAIN(8): Safety; CONCEPT(8): NamespacedAgents, ReadOnlyJudge; TECH(7): pytest, git]
## @purpose Verify that each of the six default judge types, plain and plugin-namespaced and in upper case, is denied one command of each new rule family (a worktree change, a config write, a file mode change) and is allowed the read form of the same family.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: agent str from JUDGES and tmp_path. Output: None after the assertions. Side effects: a real repository; several hook processes per agent. Guarantees: the three commands give deny with the lower-cased agent type in the reason, and config get, worktree list and a mode change on a scratch file give no decision. Raises: AssertionError on any difference. System importance: 8.
##   Example: the namespaced reviewer agent adding a worktree is denied.
## @complexity 3
@pytest.mark.parametrize("agent", JUDGES)
def test_every_judge_form_is_denied_each_new_rule_family(agent, tmp_path):
    project = make_project(tmp_path)
    make_repo(project)
    scratch = tmp_path / "scratch"
    for spelling in (agent, agent.upper()):
        for command in ["git worktree add %s/judge-wt -b judge" % scratch, "git config core.fileMode false", "chmod +x a.py"]:
            decision, reason, _ = run_guard(command, project, agent=spelling)
            print("[IMP:9][test_every_judge_form_is_denied_each_new_rule_family][DENY] %s %r -> %s" % (spelling, command[:30], decision))
            assert decision == "deny" and "Read-only agent (%s)" % agent in reason, command
    for command in ["git config --get user.name", "git worktree list", "chmod +x %s/copy/a.py" % scratch]:
        assert run_guard(command, project, agent=agent)[0] is None, command
# endregion FUNC_test_every_judge_form_is_denied_each_new_rule_family


# region FUNC_test_new_judge_rules_leave_other_agents_alone [DOMAIN(8): Safety; CONCEPT(8): Precision, RoleScope; TECH(7): pytest, git]
## @purpose Verify that the new judge rules bind only the read-only agents: the whole JUDGE_DENIED matrix is not a destructive command for the general classifier, and the coder, an architect and the root session run representative commands of each family silently.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard, guard_destructive.classify
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: a real repository with a sibling worktree; direct classifier calls for the matrix and hook processes for the agents. Guarantees: classify returns None for every matrix command; the agent types coder, methodology-claude:coder, architect and none give no decision for four commands. Raises: AssertionError on any difference.
##   System importance: 8. Example: the coder agent writing git config in the project is not interrupted.
## @complexity 4
def test_new_judge_rules_leave_other_agents_alone(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    verdicts = {}
    for template, _ in JUDGE_DENIED:
        command = template.format(project=project, wt=wt, scratch=scratch)
        verdicts[template] = guard_destructive.classify(command, str(project), str(project))
    show_records(caplog.records)
    print("[IMP:9][test_new_judge_rules_leave_other_agents_alone][CLASSIFY] commands=%d flagged=%s" % (len(verdicts), [t for t, v in verdicts.items() if v]))
    assert [template for template, rule in verdicts.items() if rule] == []
    for other in ("coder", "methodology-claude:coder", "architect", None):
        for command in ["git config core.fileMode false", "git worktree add %s/extra -b extra" % scratch, "chmod +x a.py", "git fetch"]:
            assert run_guard(command, project, agent=other)[0] is None, (other, command)
# endregion FUNC_test_new_judge_rules_leave_other_agents_alone


# region FUNC_test_remote_ref_deletion_by_push_asks [DOMAIN(9): Safety; CONCEPT(9): RemoteRefDeletion; TECH(7): pytest]
## @purpose Verify that a push which deletes remote refs asks (the delete flag in long and short form and in either position, a refspec that starts with a colon, the mirror flag, the prune flag), names at most three refs, and that ordinary pushes, a push of HEAD to a named ref, a dry run, tags and a bare colon stay silent.
## @uses test_guard.make_project, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: one hook process per command; nothing is pushed. Guarantees: each deleting command gives ask with the destructive-command phrase; the colon form with four refs names the first three and not the fourth; each ordinary push gives no decision. Raises: AssertionError on any difference.
##   System importance: 9. Example: push with the delete flag, a remote and a branch asks and names the branch.
## @complexity 4
def test_remote_ref_deletion_by_push_asks(tmp_path):
    project = make_project(tmp_path)
    asking = ["git push --delete origin feature", "git push origin --delete feature", "git push -d origin feature", "git push origin :feature",
              "git push origin :refs/heads/feature", "git push --mirror", "git push --mirror backup", "git push --prune origin 'refs/heads/*:refs/heads/*'"]
    for command in asking:
        decision, reason, _ = run_guard(command, project)
        print("[IMP:9][test_remote_ref_deletion_by_push_asks][ASK] %r -> %s: %s" % (command, decision, reason[:70]))
        assert decision == "ask" and reason.startswith("Destructive command ("), command
    decision, reason, _ = run_guard("git push origin :ref-a :ref-b :ref-c :ref-d", project)
    assert decision == "ask" and "(ref-a, ref-b, ref-c)" in reason and "ref-d" not in reason
    quiet = ["git push origin main", "git push -u origin main", "git push origin HEAD:refs/heads/main", "git push --dry-run origin main",
             "git push --tags", "git push origin :", "git push -u origin HEAD"]
    for command in quiet:
        decision, reason, _ = run_guard(command, project)
        print("[IMP:9][test_remote_ref_deletion_by_push_asks][QUIET] %r -> %s" % (command, decision))
        assert decision is None, "%r -> %s" % (command, reason)
# endregion FUNC_test_remote_ref_deletion_by_push_asks


# region FUNC_test_git_rm_force_asks_only_over_uncommitted_changes [DOMAIN(9): Safety; CONCEPT(9): LossOfUncommittedWork; TECH(7): pytest, git]
## @purpose Verify that git rm with the force flag asks only when a named path has uncommitted changes, names that path, and stays silent on a clean path, without the force flag (git refuses by itself), with the cached flag and with a dry run.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository whose a.py is edited in the test and whose clean b.py is committed first; many hook processes. Guarantees: on a clean tree every rm form is silent; after the edit the force forms (short, long, clustered, after a double dash, next to a clean path) ask and name a.py, the clean path alone stays silent, and the cached, dry-run and non-force forms stay silent. Raises: AssertionError on any difference.
##   System importance: 9. Example: git rm -f a.py over an edited a.py asks and names a.py.
## @complexity 5
def test_git_rm_force_asks_only_over_uncommitted_changes(tmp_path):
    project = make_project(tmp_path)
    make_repo(project)
    (project / "b.py").write_text("OTHER = 1\n")
    subprocess.run(GIT + ["-C", str(project), "add", "-A"], check=True)
    subprocess.run(GIT + ["-C", str(project), "commit", "-qm", "second"], check=True)
    for command in ["git rm -f a.py", "git rm -rf a.py", "git rm a.py"]:
        decision = run_guard(command, project)[0]
        print("[IMP:9][test_git_rm_force_asks_only_over_uncommitted_changes][CLEAN] %r -> %s" % (command, decision))
        assert decision is None, command
    (project / "a.py").write_text("VALUE = 2\n")
    for command in ["git rm -f a.py", "git rm -rf a.py", "git rm --force a.py", "git rm -f -- a.py b.py", "git rm -f a.py b.py"]:
        decision, reason, _ = run_guard(command, project)
        print("[IMP:9][test_git_rm_force_asks_only_over_uncommitted_changes][EDITED] %r -> %s: %s" % (command, decision, reason[:70]))
        assert decision == "ask" and "a.py" in reason and "b.py" not in reason, command
    for command in ["git rm -f b.py", "git rm a.py", "git rm --cached -f a.py", "git rm -n -f a.py", "git rm -fn a.py", "git rm -f"]:
        decision, reason, _ = run_guard(command, project)
        print("[IMP:9][test_git_rm_force_asks_only_over_uncommitted_changes][KEPT] %r -> %s" % (command, decision))
        assert decision is None, "%r -> %s" % (command, reason)
# endregion FUNC_test_git_rm_force_asks_only_over_uncommitted_changes


# region FUNC_test_judge_rule_helpers [DOMAIN(8): ShellParsing; CONCEPT(8): OperandSelection; TECH(6): pytest]
## @purpose Verify by direct import the helpers of the new judge rules: option splitting (values, clusters, double dash), git config write against read, the perl in-place scan (module switches and script switches are not the in-place switch), the operands each judged file command writes, the project test for links and installs that replace a symbolic link pointing outside the project, the abbreviated long options of git config and of the GNU file commands, the in-place switch of sed in every spelling, and the target directory of cp and mv.
## @uses guard_destructive._parse_options, guard_destructive._git_config_writes, guard_destructive._perl_in_place_files, guard_destructive._written_operands, guard_destructive._sed_in_place, guard_destructive._copy_move_operands, guard_destructive._touches_project, guard_destructive.Context
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: a symbolic link in the temporary directory; the trace of the helpers is captured. Guarantees: expected values are fixed by the documented rules, not derived from the helpers. Raises: AssertionError on any difference.
##   System importance: 8. Example: truncate with a size and a file returns the file only; a perl command with the module switch for strict returns None.
## @complexity 6
def test_judge_rule_helpers(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    project = make_project(tmp_path)
    scratch = tmp_path / "scratch"
    scratch.mkdir()
    ctx = guard_destructive.Context(str(project))
    parse = guard_destructive._parse_options
    assert parse(["truncate", "-s", "0", "f"], "sr") == ({"-s"}, [("-s", "0")], ["f"])
    assert parse(["ln", "-sf", "a", "b"], "St") == ({"-s", "-f"}, [], ["a", "b"])
    assert parse(["install", "-Dm755", "a", "b"], "mogt") == ({"-D", "-m"}, [("-m", "755")], ["a", "b"])
    assert parse(["x", "--size=5", "--", "-f"], "", ("--size",)) == ({"--size"}, [("--size", "5")], ["-f"])
    assert parse(["x", "--size", "5", "-"], "", ("--size",)) == ({"--size"}, [("--size", "5")], ["-"])
    config = {
        ("user.name", "x"): True, ("--get", "user.name"): False, ("--list",): False, ("-l",): False, ("user.name",): False,
        ("get", "a.b"): False, ("list",): False, ("set", "a.b", "c"): True, ("unset", "a.b"): True, ("--unset", "a.b"): True,
        ("--add", "a.b", "c"): True, ("-e",): True, ("--type", "bool", "a.b"): False, ("--type", "bool", "a.b", "true"): True,
        ("--get", "--unset", "a.b"): True, ("--file", str(scratch / "c.cfg"), "a.b", "c"): False,
        ("--file", str(project / ".git" / "config"), "a.b", "c"): True, ("-f", ".git/config", "a.b", "c"): True, (): False,
        # Abbreviated long options: a unique prefix is the option it abbreviates, an ambiguous or unknown long option fails closed.
        ("--rem", "s"): True, ("--remove", "s"): True, ("--unset-a", "k"): True, ("--ren", "a", "b"): True, ("--repl", "k", "v"): True,
        ("--ad", "k", "v"): True, ("--uns", "k"): True, ("--ed",): True, ("--bogus", "k"): True, ("--glo", "--unset-a", "k"): True,
        ("--get", "--rem", "s"): True, ("--glo", "k", "v"): True, ("--typ", "bool", "a.b", "true"): True,
        ("--get-a", "k"): False, ("--get-r", "remote"): False, ("--li",): False, ("--glo", "--get", "k"): False, ("--glo", "k"): False,
        ("--nam", "--li"): False, ("--show-o", "--li"): False, ("--typ", "bool", "a.b"): False, ("--def=zz", "--get", "a.b"): False,
        ("--no-typ", "a.b"): False, ("--fil", str(scratch / "c.cfg"), "a.b", "c"): False,
        ("--fil", ".git/config", "a.b", "c"): True,
    }
    outcome = {args: guard_destructive._git_config_writes(list(args), ctx) for args in config}
    perl = guard_destructive._perl_in_place_files
    perl_cases = [
        (["perl", "-pi", "-e", "s/a/b/", "f"], ["f"]), (["perl", "-i.bak", "-pe", "x", "f", "g"], ["f", "g"]),
        (["perl", "-pi", "fix.pl", "f"], ["f"]), (["perl", "-0777pi", "-e", "x", "f"], ["f"]), (["perl", "-pe", "x", "-i", "f"], ["f"]),
        (["perl", "-ne", "print", "f"], None), (["perl", "-Mstrict", "-e", "1"], None), (["perl", "script.pl", "-i", "f"], None), (["perl", "-e", "print 1"], None),
    ]
    written = guard_destructive._written_operands
    operand_cases = [
        (["chmod", "755", "a"], ["a"]), (["chmod", "-R", "-x", "a", "b"], ["a", "b"]), (["chmod", "--reference=r", "a"], ["a"]),
        (["chmod", "--reference", "r", "a"], ["a"]), (["chown", "-R", "u:g", "d"], ["d"]), (["truncate", "-s", "0", "a", "b"], ["a", "b"]),
        (["truncate", "-r", "r", "a"], ["a"]), (["truncate", "--size=0", "a"], ["a"]), (["dd", "if=x", "of=y", "bs=1"], ["y"]), (["dd", "if=x"], []),
        (["ln", "-s", "t", "l"], ["l"]), (["ln", "-s", "t"], ["."]), (["ln", "-s", "-t", "d", "a", "b"], ["d"]), (["ln", "--target-directory=d", "a"], ["d"]),
        (["install", "-m", "755", "a", "d/b"], ["d/b"]), (["install", "-d", "x", "y"], ["x", "y"]), (["install", "-t", "d", "a", "b"], ["d"]),
        (["install", "--mode=755", "a", "b"], ["b"]), (["ls", "-l"], None), (["perl", "-ne", "x", "f"], None),
        # GNU tools take any unambiguous prefix of a long option, so the reference and target-directory options are found abbreviated.
        (["chmod", "--ref=r", "a"], ["a"]), (["chmod", "--refe", "r", "a"], ["a"]), (["chown", "--ref", "r", "a"], ["a"]),
        (["chgrp", "--reference=r", "a", "b"], ["a", "b"]), (["chmod", "--recursive", "755", "a"], ["a"]),
        (["truncate", "--si=5", "a"], ["a"]), (["truncate", "--refer", "r", "a"], ["a"]), (["truncate", "--reference=r", "a"], ["a"]),
        (["ln", "-s", "--target-d", "d", "a"], ["d"]), (["ln", "--target=d", "a"], ["d"]), (["ln", "--symb", "t", "l"], ["l"]),
        (["install", "--target", "d", "a"], ["d"]), (["install", "--target-d=d", "a", "b"], ["d"]), (["install", "--dir", "x", "y"], ["x", "y"]),
        (["install", "--mod=755", "a", "b"], ["b"]),
    ]
    # sed rewrites in place with the i switch anywhere in a cluster (-Ei, -ni) or with the long form, abbreviated or not; a letter i inside a
    # script, a script file or the value of a value-taking switch is not the switch.
    sed_cases = [
        (["sed", "-i", "x", "f"], True), (["sed", "-Ei", "x", "f"], True), (["sed", "-ni", "x", "f"], True), (["sed", "-nEi", "x", "f"], True),
        (["sed", "-i.bak", "x", "f"], True), (["sed", "-ie", "x", "f"], True), (["sed", "-E", "-i", "x", "f"], True),
        (["sed", "--in-place", "x", "f"], True), (["sed", "--in-place=.bak", "x", "f"], True), (["sed", "--in", "x", "f"], True),
        (["sed", "-e", "x", "--in-place", "f"], True), (["sed", "x", "f", "-i"], True),
        (["sed", "-n", "/i/p", "f"], False), (["sed", "-E", "s/i/j/", "f"], False), (["sed", "-e", "s/i//", "f"], False),
        (["sed", "-e", "-i", "f"], False), (["sed", "-nf", "script", "f"], False), (["sed", "-l", "5", "p", "f"], False),
        (["sed", "--expression=x", "f"], False), (["sed", "--quiet", "p", "f"], False), (["sed", "-s", "-n", "p", "f"], False),
    ]
    sed_in_place = guard_destructive._sed_in_place
    # cp writes its last operand or its target directory, mv writes every operand and its target directory.
    move_cases = [
        (["cp", "a", "b"], ["b"]), (["cp", "-p", "a", "b"], ["b"]), (["cp", "a", "b", "c"], ["c"]), (["cp", "-t", "d", "a"], ["d"]),
        (["cp", "-rt", "d", "a"], ["d"]), (["cp", "--target-directory=d", "a"], ["d"]), (["cp", "--target-d", "d", "a", "b"], ["d"]),
        (["cp", "--target=d", "a"], ["d"]), (["cp", "--", "-a", "b"], ["b"]),
        (["mv", "a", "b"], ["a", "b"]), (["mv", "-t", "d", "a"], ["a", "d"]), (["mv", "--target-directory=d", "a"], ["a", "d"]),
        (["mv", "--target", "d", "a", "b"], ["a", "b", "d"]), (["mv", "-f", "a", "b"], ["a", "b"]),
    ]
    copy_move = guard_destructive._copy_move_operands
    (project / "link").symlink_to(scratch / "target")
    show_records(caplog.records)
    print("[IMP:9][test_judge_rule_helpers][CASES] config=%d perl=%d operands=%d sed=%d copy_move=%d" % (
        len(config), len(perl_cases), len(operand_cases), len(sed_cases), len(move_cases)))
    assert outcome == config
    assert all(perl(case) == expected for case, expected in perl_cases)
    assert all(written(case[0], case) == expected for case, expected in operand_cases)
    assert [(case, sed_in_place(case)) for case, _ in sed_cases] == sed_cases
    assert [(case, copy_move(case[0], case)) for case, _ in move_cases] == move_cases
    touches = guard_destructive._touches_project
    assert touches("ln", "link", ctx) and not touches("chmod", "link", ctx)
    assert touches("install", "link", ctx) and touches("ln", "new-entry", ctx) and not touches("ln", str(scratch / "new-entry"), ctx)
# endregion FUNC_test_judge_rule_helpers


# region FUNC_test_judge_helpers_trace_their_own_verdicts [DOMAIN(8): Diagnostics; CONCEPT(8): OwnedTrajectory, OptInTrace; TECH(7): pytest, caplog, subprocess]
## @purpose Verify that each helper of the judge rules leaves its own trace line (the option splitter, the git config and git branch form helpers, the perl scan, the written operands and the project test): by direct call with the exact message fixed here, and at the process boundary where the lines reach stderr only when METHODOLOGY_HOOK_LOG is set and never carry an operand or the project path.
## @uses guard_destructive._parse_options, guard_destructive._expand_long_option, guard_destructive._perl_in_place_files, guard_destructive._written_operands, guard_destructive._touches_project, guard_destructive._git_branch_changes, guard_destructive._git_config_writes, guard_destructive._sed_in_place, guard_destructive._sed_files, guard_destructive._copy_move_operands, test_guard.invoke
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: direct helper calls and hook processes with and without tracing; nothing is executed. Guarantees: every expected message is among the guard records of its call; for five judge commands the stderr of a traced run holds the lines of the helpers on its path and the stderr of an untraced run is empty while the deny decision is unchanged; no traced stderr holds an operand or the project path. Raises: AssertionError on any difference.
##   System importance: 8. Example: the written operands of a chmod with a mode and two files leave the record writing=True command=chmod operands=2.
## @complexity 6
def test_judge_helpers_trace_their_own_verdicts(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    project = make_project(tmp_path)
    scratch = tmp_path / "scratch"
    ctx = guard_destructive.Context(str(project))
    g = guard_destructive
    cases = [
        (lambda: g._parse_options(["truncate", "-s", "0", "f"], "sr"), "[IMP:4][_parse_options][RESULT] flags=1 values=1 operands=1"),
        (lambda: g._parse_options(["x", "--", "-f", "g"]), "[IMP:4][_parse_options][RESULT] flags=0 values=0 operands=2"),
        (lambda: g._perl_in_place_files(["perl", "-pi", "-e", "x", "f", "g"]), "[IMP:5][_perl_in_place_files][VERDICT] in_place=True files=2"),
        (lambda: g._perl_in_place_files(["perl", "-ne", "x", "f"]), "[IMP:5][_perl_in_place_files][VERDICT] in_place=False files=0"),
        (lambda: g._written_operands("chmod", ["chmod", "755", "a", "b"]), "[IMP:5][_written_operands][VERDICT] writing=True command=chmod operands=2"),
        (lambda: g._written_operands("dd", ["dd", "if=x"]), "[IMP:5][_written_operands][VERDICT] writing=True command=dd operands=0"),
        (lambda: g._written_operands("ls", ["ls", "-l"]), "[IMP:5][_written_operands][VERDICT] writing=False command=- operands=0"),
        (lambda: g._written_operands("perl", ["perl", "-ne", "x"]), "[IMP:5][_written_operands][VERDICT] writing=False command=- operands=0"),
        (lambda: g._touches_project("chmod", "a.py", ctx), "[IMP:5][_touches_project][VERDICT] command=chmod touches=True"),
        (lambda: g._touches_project("chmod", str(scratch / "a.py"), ctx), "[IMP:5][_touches_project][VERDICT] command=chmod touches=False"),
        (lambda: g._git_branch_changes(["--contains", "HEAD"]), "[IMP:5][_git_branch_changes][VERDICT] changes=False mode=list-option operands=1"),
        (lambda: g._git_branch_changes(["feature"]), "[IMP:5][_git_branch_changes][VERDICT] changes=True mode=branch-name operands=1"),
        (lambda: g._git_branch_changes(["-d", "feature"]), "[IMP:5][_git_branch_changes][VERDICT] changes=True mode=change-option operands=1"),
        (lambda: g._git_branch_changes([]), "[IMP:5][_git_branch_changes][VERDICT] changes=False mode=no-operand operands=0"),
        (lambda: g._git_config_writes(["user.name", "x"], ctx), "[IMP:5][_git_config_writes][VERDICT] writes=True"),
        (lambda: g._expand_long_option("--mov", g.BRANCH_LONG_OPTIONS), "[IMP:4][_expand_long_option][VERDICT] resolution=prefix candidates=1"),
        (lambda: g._expand_long_option("--move", g.BRANCH_LONG_OPTIONS), "[IMP:4][_expand_long_option][VERDICT] resolution=exact candidates=1"),
        (lambda: g._expand_long_option("--co", g.BRANCH_LONG_OPTIONS), "[IMP:4][_expand_long_option][VERDICT] resolution=ambiguous candidates=4"),
        (lambda: g._expand_long_option("--bogus", g.BRANCH_LONG_OPTIONS), "[IMP:4][_expand_long_option][VERDICT] resolution=unknown candidates=0"),
        (lambda: g._git_branch_changes(["-a", "--mov", "a", "b"]), "[IMP:5][_git_branch_changes][VERDICT] changes=True mode=change-option operands=2"),
        (lambda: g._git_branch_changes(["--bogus"]), "[IMP:5][_git_branch_changes][VERDICT] changes=True mode=unknown-option operands=0"),
        (lambda: g._git_branch_changes(["-a", "feature"]), "[IMP:5][_git_branch_changes][VERDICT] changes=True mode=branch-name operands=1"),
        (lambda: g._git_branch_changes(["--li", "x"]), "[IMP:5][_git_branch_changes][VERDICT] changes=False mode=list-option operands=1"),
        (lambda: g._git_config_writes(["--rem", "s"], ctx), "[IMP:5][_git_config_writes][VERDICT] writes=True"),
        (lambda: g._git_config_writes(["--bogus", "k"], ctx), "[IMP:5][_git_config_writes][UNKNOWN_OPTION] a long option that is neither known nor a unique prefix: a write is assumed"),
        (lambda: g._git_config_writes(["--get-a", "k"], ctx), "[IMP:5][_git_config_writes][VERDICT] writes=False"),
        (lambda: g._sed_in_place(["sed", "-Ei", "x", "f"]), "[IMP:5][_sed_in_place][VERDICT] in_place=True"),
        (lambda: g._sed_in_place(["sed", "-n", "x", "f"]), "[IMP:5][_sed_in_place][VERDICT] in_place=False"),
        (lambda: g._sed_files(["sed", "-i", "-es/1/2/", "f"]), "[IMP:5][_sed_files][VERDICT] script_given=True operands=1"),
        (lambda: g._sed_files(["sed", "-i", "s/1/2/", "f", "g"]), "[IMP:5][_sed_files][VERDICT] script_given=False operands=2"),
        (lambda: g._copy_move_operands("cp", ["cp", "-t", "d", "a"]), "[IMP:5][_copy_move_operands][VERDICT] command=cp operands=1"),
        (lambda: g._copy_move_operands("mv", ["mv", "-t", "d", "a"]), "[IMP:5][_copy_move_operands][VERDICT] command=mv operands=2"),
    ]
    for call, expected in cases:
        caplog.clear()
        call()
        messages = [r.getMessage() for r in caplog.records if r.name == "guard_destructive"]
        show_records(caplog.records)
        print("[IMP:9][test_judge_helpers_trace_their_own_verdicts][CALL] %s" % expected)
        assert expected in messages, "%s not in %s" % (expected, messages)
    judge_commands = {
        "ln -s target link": ["_parse_options", "_written_operands", "_touches_project"],
        "perl -pi -e 's/1/2/' a.py": ["_perl_in_place_files", "_written_operands", "_touches_project"],
        "git config user.name x": ["_parse_options", "_git_config_writes"],
        "git branch feature": ["_git_branch_changes"],
        "git branch -a --mov a b": ["_expand_long_option", "_git_branch_changes"],
        "git config --rem s": ["_parse_options", "_expand_long_option", "_git_config_writes"],
        "sed -Ei 's/1/2/' a.py": ["_sed_in_place", "_sed_files", "_parse_options"],
        "sed -i -e's/1/2/' a.py": ["_sed_in_place", "_sed_files", "_parse_options"],
        "cp --target-d . x": ["_copy_move_operands", "_expand_long_option"],
    }
    env = {"CLAUDE_PROJECT_DIR": str(project), "HOME": str(tmp_path / "home")}
    for command, helpers in judge_commands.items():
        payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}, "cwd": str(project), "agent_type": "qa"})
        traced = invoke(payload, env, trace=True)
        quiet = invoke(payload, env, trace=False)
        lines = [line for line in traced.stderr.splitlines() if TRACE_RE.match(line)]
        print("[IMP:9][test_judge_helpers_trace_their_own_verdicts][PROCESS] %r helpers=%s lines=%d quiet_stderr_chars=%d" % (command, helpers, len(lines), len(quiet.stderr)))
        for helper in helpers:
            assert any("[%s][" % helper in line for line in lines), (command, helper, traced.stderr)
        assert "a.py" not in traced.stderr and str(project) not in traced.stderr and "link" not in traced.stderr, traced.stderr
        assert quiet.stderr == "" and traced.returncode == quiet.returncode == 0
        assert json.loads(quiet.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny"
        assert json.loads(traced.stdout) == json.loads(quiet.stdout)
# endregion FUNC_test_judge_helpers_trace_their_own_verdicts


# region FUNC_test_branch_form_helper [DOMAIN(8): Git; CONCEPT(8): BranchListVersusChange; TECH(6): pytest]
## @purpose Verify by direct import the decision table of the branch form helper: which git branch word lists remain read-only and which change a ref, abbreviated long options included (git takes any unambiguous prefix), an ambiguous or unknown long option failing closed, and the all and remotes flags being filters and not the list mode.
## @uses guard_destructive._git_branch_changes
## @io Input: caplog. Output: None after the assertions. Side effects: none beyond trace capture. Guarantees: expected verdicts are fixed by the git documentation of the branch options, not derived from the helper; the sort and format options take the next word as a value, a change option wins over a list option, a cluster is read letter by letter, and words after a double dash are bare words. Raises: AssertionError on any difference.
##   System importance: 8. Example: the verbose flag with a name changes a ref; the same flag alone lists.
## @complexity 5
def test_branch_form_helper(caplog):
    caplog.set_level(logging.INFO)
    branch = {
        (): False, ("-a",): False, ("-r",): False, ("-v",): False, ("-vv",): False, ("-avv",): False, ("--verbose",): False,
        ("--list",): False, ("--list", "feat*"): False, ("-l", "feat*"): False, ("-a", "--list", "origin/*"): False,
        ("--contains", "HEAD"): False, ("--contains",): False, ("--no-contains", "HEAD"): False, ("--merged", "HEAD"): False,
        ("--merged",): False, ("--no-merged", "main"): False, ("--points-at", "HEAD"): False, ("--show-current",): False,
        ("--sort", "committerdate"): False, ("--sort=-committerdate", "-v"): False, ("--format", "%(refname)"): False,
        ("--color=never",): False, ("--abbrev=7", "-v"): False, ("-a", "--contains", "HEAD"): False, ("--list", "--", "x"): False,
        ("feature",): True, ("feature", "HEAD"): True, ("-v", "feature"): True, ("--sort", "k", "feature"): True,
        ("--format", "%(refname)", "feature"): True, ("--track", "feature"): True, ("--", "feature"): True,
        ("-d", "x"): True, ("-D", "x"): True, ("-dr", "x"): True, ("-rd", "x"): True, ("--delete", "x"): True,
        ("-m", "a", "b"): True, ("-M", "a", "b"): True, ("--move", "a", "b"): True, ("-c", "a", "b"): True, ("-C", "a", "b"): True,
        ("--copy", "a", "b"): True, ("-u", "origin/main"): True, ("-uorigin/main",): True, ("--set-upstream-to=origin/main",): True,
        ("--set-upstream-to", "origin/main"): True, ("--unset-upstream",): True, ("-f",): True, ("--force",): True,
        ("-f", "x", "HEAD"): True, ("-fv",): True, ("--edit-description",): True, ("--list", "--delete", "x"): True,
        ("--contains", "HEAD", "-d", "x"): True, ("-a", "-D", "x"): True,
        # Abbreviated long options (git takes any unambiguous prefix): read forms stay read-only, change forms are found, an ambiguous or
        # unknown long option fails closed, and -a, -r, --all, --remotes are filters, not the list mode.
        ("--li", "feat*"): False, ("--lis",): False, ("--cont", "HEAD"): False, ("--no-cont", "HEAD"): False, ("--me", "HEAD"): False,
        ("--no-me", "main"): False, ("--po", "HEAD"): False, ("--sh",): False, ("--so", "committerdate"): False,
        ("--form", "%(refname)"): False, ("--rem",): False, ("--all", "--verb"): False, ("-r", "-v"): False, ("-a", "-v"): False,
        ("-l", "x"): False, ("-rl", "x"): False, ("--colo=never",): False, ("--abb=7", "-v"): False, ("-a", "--li", "origin/*"): False,
        ("--sort=-committerdate", "--li", "x"): False, ("--tr",): False,
        ("-a", "--mov", "a", "b"): True, ("--all", "--cop", "a", "b"): True, ("-r", "--del", "x"): True, ("--remotes", "--del", "x"): True,
        ("--mo", "a", "b"): True, ("--mov", "a", "b"): True, ("--cop", "a", "b"): True, ("--de", "x"): True, ("--forc", "x"): True,
        ("--for", "x"): True, ("--co", "a", "b"): True, ("--c",): True, ("--edit-d",): True, ("--set-upstream-t=x",): True,
        ("--unset-u",): True, ("--bogus",): True, ("--list", "--bogus"): True, ("--no-move", "a", "b"): True, ("--so", "k", "feature"): True,
        ("--tr", "feature"): True, ("-a", "feature"): True, ("-r", "feature"): True, ("--all", "feature"): True,
        ("--remotes", "feature"): True, ("-ar", "feature"): True, ("--list", "--mov", "a", "b"): True,
        ("--cont", "HEAD", "--del", "x"): True, ("--", "--mov"): True,
    }
    outcome_branch = {args: guard_destructive._git_branch_changes(list(args)) for args in branch}
    show_records(caplog.records)
    print("[IMP:9][test_branch_form_helper][CASES] branch=%d" % len(branch))
    assert outcome_branch == branch
# endregion FUNC_test_branch_form_helper


# region FUNC_test_judge_branch_and_fetch_by_form [DOMAIN(9): Safety; CONCEPT(9): Precision, ReadOnlyJudge, GitStateMutation; TECH(7): pytest, git]
## @purpose Verify through the hook process that a read-only judge keeps the listing forms of git branch (no interruption, which the judge needs to check what a branch holds), is denied every branch creation, deletion, rename, copy, force and upstream change and every git fetch, the dry run included (a dry run still adds objects to the object store), in all six agent forms, and that the other agents are not bound by these rules.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard, test_guard.assert_scratch_advice
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; one hook process per command; no command is executed. Guarantees: each JUDGE_GIT_DENIED command gives deny naming the qa agent and the rule git branch or git fetch, recommends the scratch copy form and never repeats the command; each JUDGE_GIT_ALLOWED command gives no decision and exit code 0; each of the six judge forms in lower and upper case is allowed two branch listings and denied a branch creation, a branch deletion, a fetch and a fetch dry run; the coder, an architect and the root session get no decision for six branch and fetch commands, the dry run included (the general path is unchanged). Raises: AssertionError on any difference.
##   System importance: 9. Example: git branch with the contains flag and a commit is silent; git branch with only a name is denied; git fetch with the dry-run flag is denied.
## @complexity 6
def test_judge_branch_and_fetch_by_form(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    for template, expected in JUDGE_GIT_DENIED:
        command = template.format(project=project, wt=wt, scratch=scratch)
        decision, reason, _ = run_guard(command, project, agent="qa")
        print("[IMP:9][test_judge_branch_and_fetch_by_form][DENY] %r -> %s: %s" % (template[:48], decision, reason[:70]))
        assert decision == "deny" and "Read-only agent (qa)" in reason, command
        assert "(%s)" % expected in reason, "%r: reason %r lacks %r" % (command, reason, expected)
        assert command not in reason
        assert_scratch_advice(reason)
    for template in JUDGE_GIT_ALLOWED:
        command = template.format(project=project, wt=wt, scratch=scratch)
        decision, reason, code = run_guard(command, project, agent="qa")
        print("[IMP:9][test_judge_branch_and_fetch_by_form][ALLOW] %r -> %s" % (template[:60], decision))
        assert (decision, code) == (None, 0), "%r -> %s" % (command, reason)
    for agent in JUDGES:
        for command in ["git branch --contains HEAD", "git branch -a --list 'origin/*'"]:
            assert run_guard(command, project, agent=agent)[0] is None, (agent, command)
        for command in ["git branch feature", "git branch -d feature", "git fetch", "git fetch --dry-run"]:
            for spelling in (agent, agent.upper()):
                decision, reason, _ = run_guard(command, project, agent=spelling)
                assert decision == "deny" and "Read-only agent (%s)" % agent in reason, (spelling, command)
    for other in ("coder", "methodology-claude:coder", "architect", None):
        for command in ["git branch feature", "git branch -d feature", "git branch -m old new", "git fetch", "git fetch --dry-run", "git fetch --no-dry-run"]:
            assert run_guard(command, project, agent=other)[0] is None, (other, command)
    assert guard_destructive.classify("git fetch --dry-run", str(project), str(project)) is None
# endregion FUNC_test_judge_branch_and_fetch_by_form


# region FUNC_test_long_option_expansion [DOMAIN(8): ShellParsing; CONCEPT(9): AbbreviatedLongOption; TECH(6): pytest]
## @purpose Verify by direct import the expansion of an abbreviated long option against the real option table of a verb: an exact name wins even when it prefixes another name, a unique prefix is that option, an ambiguous prefix, an unknown name and a bare double dash resolve to nothing, the generated negations of git are known names, and a tool without negations (the GNU file commands) knows none.
## @uses guard_destructive._expand_long_option, guard_destructive.BRANCH_LONG_OPTIONS, guard_destructive.CONFIG_LONG_OPTIONS, guard_destructive.TRUNCATE_LONG, guard_destructive.LN_LONG, guard_destructive.INSTALL_LONG, guard_destructive.SED_LONG
## @io Input: caplog. Output: None after the assertions. Side effects: none beyond trace capture. Guarantees: the expected canonical names are fixed here from the git and GNU documentation, not derived from the helper; the distinction between exact, prefix, ambiguous and unknown is also read from the owned trace lines. Raises: AssertionError on any difference.
##   System importance: 8. Example: the prefix mov of the branch table is the move option; the prefix co is ambiguous and resolves to nothing.
## @complexity 4
def test_long_option_expansion(caplog):
    caplog.set_level(logging.INFO)
    g = guard_destructive
    branch, config = g.BRANCH_LONG_OPTIONS, g.CONFIG_LONG_OPTIONS
    table = [
        (branch, "--move", "--move"), (branch, "--mov", "--move"), (branch, "--mo", "--move"), (branch, "--de", "--delete"),
        (branch, "--li", "--list"), (branch, "--me", "--merged"), (branch, "--no-cont", "--no-contains"), (branch, "--no-move", "--no-move"),
        (branch, "--set-upstream", "--set-upstream"), (branch, "--set-upstream-t", "--set-upstream-to"), (branch, "--set-up", None),
        (branch, "--co", None), (branch, "--c", None), (branch, "--for", None), (branch, "--no-", None), (branch, "--bogus", None),
        (branch, "--", None), (branch, "--LIST", None),
        (config, "--unset", "--unset"), (config, "--unset-a", "--unset-all"), (config, "--uns", None), (config, "--rem", "--remove-section"),
        (config, "--ren", "--rename-section"), (config, "--get-a", "--get-all"), (config, "--ge", None), (config, "--l", None),
        (config, "--li", "--list"), (config, "--glo", "--global"), (config, "--no-typ", "--no-type"), (config, "--bogus", None),
        (g.TRUNCATE_LONG, "--refer", "--reference"), (g.TRUNCATE_LONG, "--si", "--size"), (g.TRUNCATE_LONG, "--no-size", None),
        (g.LN_LONG, "--target", "--target-directory"), (g.LN_LONG, "--no-target", "--no-target-directory"), (g.LN_LONG, "--s", None),
        (g.INSTALL_LONG, "--strip", "--strip"), (g.INSTALL_LONG, "--str", None), (g.INSTALL_LONG, "--dir", "--directory"),
        (g.SED_LONG, "--in", "--in-place"), (g.SED_LONG, "--in-place", "--in-place"), (g.SED_LONG, "--s", None),
    ]
    resolved = [g._expand_long_option(name, known) for known, name, _ in table]
    show_records(caplog.records)
    messages = [r.getMessage() for r in caplog.records if r.name == "guard_destructive" and "[_expand_long_option]" in r.getMessage()]
    kinds = {kind: sum("resolution=%s " % kind in m for m in messages) for kind in ("exact", "prefix", "ambiguous", "unknown")}
    print("[IMP:9][test_long_option_expansion][CASES] cases=%d trace_lines=%d kinds=%s" % (len(table), len(messages), kinds))
    assert resolved == [expected for _, _, expected in table]
    assert len(table) == 42 and len(messages) == 42
    assert kinds == {"exact": 6, "prefix": 20, "ambiguous": 12, "unknown": 4}  # counted by hand from the table above
    assert "[IMP:4][_expand_long_option][VERDICT] resolution=ambiguous candidates=4" in messages  # co: color, column, contains, copy
    assert "[IMP:4][_expand_long_option][VERDICT] resolution=ambiguous candidates=5" in messages  # c: the four and create-reflog
# endregion FUNC_test_long_option_expansion


# region FUNC_test_judge_abbreviated_option_bypass [DOMAIN(9): Safety; CONCEPT(9): AbbreviatedLongOption, ReadOnlyJudge; TECH(7): pytest, git]
## @purpose Pin the defect found by the independent review: git accepts any unambiguous prefix of a long option, so a judge could rename, copy or delete a branch (a filter flag before an abbreviated change option) or remove a configuration section or key (an abbreviated write option) without a decision. Through the hook process, in all six judge forms in lower and upper case, the abbreviated change forms are denied and the listing and read forms, abbreviated or not, stay silent; the other agents are not bound.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard, test_guard.assert_scratch_advice
## @io Input: agent str from JUDGES and tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; one hook process per command; no command is executed. Guarantees: each of the denied commands gives deny naming the judge, the rule git branch or git config and the scratch advice, and never repeats the command; each silent command gives no decision and exit code 0; the coder, an architect and the root session get no decision for the denied commands. Raises: AssertionError on any difference.
##   System importance: 9. Example: git branch with the all flag and the cop prefix of the copy option is denied; git branch with the li prefix of the list option is silent.
## @complexity 5
@pytest.mark.parametrize("agent", JUDGES)
def test_judge_abbreviated_option_bypass(agent, tmp_path):
    project = make_project(tmp_path)
    make_repo(project)
    denied = [("git branch -a --mov a b", "git branch"), ("git branch --all --cop a b", "git branch"), ("git branch -r --del x", "git branch"),
              ("git branch --mo a b", "git branch"), ("git config --rem s", "git config"), ("git config --unset-a k", "git config")]
    silent = ["git branch --list", "git branch --li", "git branch -a", "git branch -r -v", "git branch --contains HEAD", "git config --get k",
              "git config --get-a k"]
    for spelling in (agent, agent.upper()):
        for command, rule in denied:
            decision, reason, _ = run_guard(command, project, agent=spelling)
            print("[IMP:9][test_judge_abbreviated_option_bypass][DENY] %s %r -> %s" % (spelling, command, decision))
            assert decision == "deny" and "Read-only agent (%s)" % agent in reason and "(%s)" % rule in reason, command
            assert command not in reason
            assert_scratch_advice(reason)
        for command in silent:
            decision, reason, code = run_guard(command, project, agent=spelling)
            print("[IMP:9][test_judge_abbreviated_option_bypass][SILENT] %s %r -> %s" % (spelling, command, decision))
            assert (decision, code) == (None, 0), "%r -> %s" % (command, reason)
    for other in ("coder", "methodology-claude:coder", "architect", None):
        for command, _ in denied:
            assert run_guard(command, project, agent=other)[0] is None, (other, command)
# endregion FUNC_test_judge_abbreviated_option_bypass


# region FUNC_test_judge_sed_script_forms [DOMAIN(9): Safety; CONCEPT(9): InPlaceEdit, OperandSelection, ReadOnlyJudge; TECH(7): pytest, git]
## @purpose Pin the defect found by the independent review of the fourth round: a judge took the first word that does not start with a dash as the sed script, so a script attached to the expression option (the attached short form, a cluster before it, the long form attached or separate, an attached form after a backup suffix) made the file the first word of the operand list, and the file was dropped and the in-place edit passed silently. Through the hook process, in all six judge forms, every spelling of the script option followed by a project file is denied naming the sed rule and the file, a backup suffix that ends in a value letter of sed (a suffix such as tmpl) does not swallow the script, and the same edits on a scratch file, a sed that only prints and the other agents stay silent.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard, test_guard.assert_scratch_advice
## @io Input: agent str from JUDGES and tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; one hook process per command; no command is executed. Guarantees: each denied command gives deny naming the judge, the rule sed a.py (or the worktree file) and the scratch advice, and never repeats the command; each silent command gives no decision and exit code 0; the coder, an architect and the root session get no decision for the denied commands. Raises: AssertionError on any difference.
##   System importance: 9. Example: sed in place with the attached expression option and a.py is denied; the same edit of a file under the scratch root is silent.
## @complexity 5
@pytest.mark.parametrize("agent", JUDGES)
def test_judge_sed_script_forms(agent, tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    denied = [
        ("sed -i -e's/1/2/' a.py", "sed a.py"), ("sed -Ei -e's/1/2/' a.py", "sed a.py"), ("sed -i --expression=s/1/2/ a.py", "sed a.py"),
        ("sed --expression=s/1/2/ -i a.py", "sed a.py"), ("sed -i.bak -es/1/2/ a.py", "sed a.py"), ("sed -i -e 's/1/2/' a.py", "sed a.py"),
        ("sed -i --expression 's/1/2/' a.py", "sed a.py"), ("sed -i --expr=s/1/2/ a.py", "sed a.py"), ("sed -i -f x.sed a.py", "sed a.py"),
        ("sed -i --file=x.sed a.py", "sed a.py"), ("sed -i -e s/1/2/ -e s/3/4/ a.py", "sed a.py"), ("sed -i -es/1/2/ -- a.py", "sed a.py"),
        ("sed -i.tmpl 's/1/2/' a.py", "sed a.py"), ("sed -i.mail 's/1/2/' a.py", "sed a.py"), ("sed -ni.save 's/1/2/p' a.py", "sed a.py"),
        ("sed -i -e's/1/2/' %s/a.py" % wt, "sed " + str(wt)), ("bash -c \"sed -i -e's/1/2/' a.py\"", "sed a.py"),
    ]
    silent = ["sed -i -e 's/1/2/' /private/tmp/x/a.py", "sed -i -e's/1/2/' %s/copy/a.py" % scratch, "sed -i --expression=s/1/2/ %s/copy/a.py" % scratch,
              "sed -i.tmpl 's/1/2/' %s/copy/a.py" % scratch, "sed -i -e 's/1/2/' -e 's/3/4/' %s/copy/a.py" % scratch, "sed -n p a.py",
              "sed -n -e p a.py", "sed --expression=p a.py", "sed -E -e's/1/2/' a.py"]
    for spelling in (agent, agent.upper()):
        for command, rule in denied[:5] if spelling != agent else denied:
            decision, reason, _ = run_guard(command, project, agent=spelling)
            print("[IMP:9][test_judge_sed_script_forms][DENY] %s %r -> %s" % (spelling, command, decision))
            assert decision == "deny" and "Read-only agent (%s)" % agent in reason and "(%s" % rule in reason, (command, reason)
            assert command not in reason
            assert_scratch_advice(reason)
        for command in silent:
            decision, reason, code = run_guard(command, project, agent=spelling)
            print("[IMP:9][test_judge_sed_script_forms][SILENT] %s %r -> %s" % (spelling, command, decision))
            assert (decision, code) == (None, 0), "%r -> %s" % (command, reason)
    for other in ("coder", "methodology-claude:coder", "architect", None):
        for command, _ in denied[:5]:
            assert run_guard(command, project, agent=other)[0] is None, (other, command)
# endregion FUNC_test_judge_sed_script_forms


# region FUNC_test_sed_file_operand_helper [DOMAIN(8): ShellParsing; CONCEPT(9): OperandSelection, InPlaceEdit; TECH(6): pytest]
## @purpose Verify by direct import which words of a sed in-place call are files: the first non-option word is the script only when no expression or file option was given, in any spelling (attached, separate, long, abbreviated long, after a cluster); the value of a value option and the backup suffix attached to the in-place switch are never files, even when the suffix holds a value letter of sed at its end; every word after a double dash is a file; and the short cluster scan of _parse_options ends at a suffix letter when one is named.
## @uses guard_destructive._sed_files, guard_destructive._sed_in_place, guard_destructive._parse_options
## @io Input: caplog. Output: None after the assertions. Side effects: the trace of the helpers is captured and printed. Guarantees: the expected operands are fixed by the documented rules, not derived from the helpers; every case of the table is also an in-place call for _sed_in_place. Raises: AssertionError on any difference.
##   System importance: 8. Example: the words sed, -i, -e with an attached script and a file give the file only; the words sed, -i, a script and a file give the file only.
## @complexity 4
def test_sed_file_operand_helper(caplog):
    caplog.set_level(logging.INFO)
    files = guard_destructive._sed_files
    cases = [
        (["sed", "-i", "s/1/2/", "f"], ["f"]), (["sed", "-i", "s/1/2/", "f", "g"], ["f", "g"]), (["sed", "-i", "-e", "s/1/2/", "f"], ["f"]),
        (["sed", "-i", "-es/1/2/", "f"], ["f"]), (["sed", "-Ei", "-es/1/2/", "f"], ["f"]), (["sed", "-i.bak", "-es/1/2/", "f"], ["f"]),
        (["sed", "-i", "--expression=s/1/2/", "f"], ["f"]), (["sed", "--expression=s/1/2/", "-i", "f"], ["f"]),
        (["sed", "-i", "--expression", "s/1/2/", "f"], ["f"]), (["sed", "-i", "--expr=s/1/2/", "f"], ["f"]),
        (["sed", "-i", "-f", "x.sed", "f"], ["f"]), (["sed", "-i", "-fx.sed", "f"], ["f"]), (["sed", "-i", "--file=x.sed", "f"], ["f"]),
        (["sed", "-i", "--fi", "x.sed", "f"], ["f"]), (["sed", "-i", "-e", "a", "-e", "b", "f", "g"], ["f", "g"]),
        (["sed", "-i", "-e", "a", "-f", "x.sed", "f"], ["f"]), (["sed", "-i", "-es/1/2/", "--", "f"], ["f"]), (["sed", "-i", "--", "s/1/2/", "f"], ["f"]),
        (["sed", "-i", "-l", "5", "s/1/2/", "f"], ["f"]), (["sed", "-i", "-e"], []), (["sed", "-i", "s/1/2/"], []),
        # The backup suffix is the rest of the in-place word, whatever letters it holds.
        (["sed", "-i.tmpl", "s/1/2/", "f"], ["f"]), (["sed", "-i.mail", "s/1/2/", "f"], ["f"]), (["sed", "-i.conf", "s/1/2/", "f"], ["f"]),
        (["sed", "-i.save", "s/1/2/", "f"], ["f"]), (["sed", "-ni.tmpl", "s/1/2/p", "f"], ["f"]), (["sed", "-ie", "s/1/2/", "f"], ["f"]),
        (["sed", "-ni", "s/1/2/p", "f"], ["f"]), (["sed", "-i.tmpl", "-es/1/2/", "f"], ["f"]),
        # A BSD style empty suffix word is the first operand: it is dropped as the script word, as before.
        (["sed", "-i", "", "s/1/2/", "f"], ["s/1/2/", "f"]), (["sed", "-i", "", "-e", "s/1/2/", "f"], ["", "f"]),
    ]
    show_records(caplog.records)
    print("[IMP:9][test_sed_file_operand_helper][CASES] cases=%d" % len(cases))
    assert [(case, files(case)) for case, _ in cases] == cases
    assert all(guard_destructive._sed_in_place(case) for case, _ in cases)
    parse = guard_destructive._parse_options
    assert parse(["sed", "-ni.tmpl", "x"], "efl", short_suffix="i") == ({"-n", "-i"}, [], ["x"])
    assert parse(["sed", "-ni.tmpl", "x"], "efl") == ({"-n", "-i", "-.", "-t", "-m", "-p", "-l"}, [("-l", "x")], [])
    assert parse(["sed", "-Ei", "-es/1/2/", "f"], "efl", short_suffix="i") == ({"-E", "-i", "-e"}, [("-e", "s/1/2/")], ["f"])
    assert parse(["sed", "-ei", "f"], "efl", short_suffix="i") == ({"-e"}, [("-e", "i")], ["f"])
    messages = [r.getMessage() for r in caplog.records if r.name == "guard_destructive"]
    assert "[IMP:5][_sed_files][VERDICT] script_given=True operands=1" in messages
    assert "[IMP:5][_sed_files][VERDICT] script_given=False operands=1" in messages
# endregion FUNC_test_sed_file_operand_helper


# region FUNC_test_documented_limits_match_behavior [DOMAIN(9): Safety; CONCEPT(9): KnownLimits, TruthfulDocumentation; TECH(7): pytest, git]
## @purpose Pin the known limits the guard documents, so that the text and the behavior cannot drift apart: the exact spellings the owner ask path lists still ask, the abbreviations and separate flags named as known limits of the ask path are silent, the git verbs the contract names as intercepted for a read-only agent are denied, the git verbs it names as not intercepted are silent, and every name used here appears in the text of the module contract it is documented in.
## @uses test_guard.make_project, test_guard.make_repo, guard_destructive.classify, guard_destructive.classify_readonly, guard_destructive.MUTATING_GIT, guard_destructive.Context
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree, an edited tracked file and an untracked file; direct classifier calls; the source file is read as text; no command is executed. Guarantees: the expected verdicts are fixed here; the documented examples are found in the purpose of the function they belong to. Raises: AssertionError on any difference.
##   System importance: 9. Example: git reset with the hard flag over an edited file asks, git reset with the ha prefix is silent, git bisect is silent for a judge, git fetch is denied.
## @complexity 5
def test_documented_limits_match_behavior(tmp_path):
    project = make_project(tmp_path)
    make_repo(project)
    (project / "a.py").write_text("VALUE = 2\n")
    (project / "u.txt").write_text("untracked\n")
    source = Path(guard_destructive.__file__).read_text()

    def purpose(name):
        start = source.index("# region FUNC_%s " % name)
        return source[start:source.index("\n", source.index("## @purpose", start))]

    asks = ["git reset --hard", "git clean -f", "git clean --force", "git push --force", "git push --delete origin feature", "git push --mirror",
            "git checkout --force other", "git checkout -f other", "git rm --force a.py", "git rm -f a.py", "git branch -D feature", "git branch -Df feature"]
    limits = ["git reset --ha", "git clean --f", "git push --de origin feature", "git push --mir", "git push --forc", "git checkout --forc other",
              "git switch --disc other", "git restore --staged --work a.py", "git rm --forc a.py", "rm --rec --for ../other",
              "git branch -d -f feature", "git branch -df feature", "git branch --delete --force feature"]
    for command in asks:
        assert guard_destructive.classify(command, str(project), str(project)), command
    for command in limits:
        assert guard_destructive.classify(command, str(project), str(project)) is None, command
    contract = source[:source.index("## @changes")]
    for example in ["git reset --ha", "git clean --f", "git push --de", "--mir or --forc", "git checkout --forc", "git switch --disc",
                    "git restore --staged --work", "git rm --forc", "git branch -d -f, -df, --delete --force"]:
        assert example in purpose("_git_rule") and example in contract, example
    assert "rm --rec --for" in contract and "does not expand an abbreviated long option" in purpose("_git_rule")
    intercepted = purpose("classify_readonly")
    for verb in sorted(guard_destructive.MUTATING_GIT):
        assert verb in intercepted, verb
        assert guard_destructive.classify_readonly("git %s x" % verb, str(project), str(project)) == "git %s" % verb, verb
    for command in ["git worktree add x", "git worktree lock x", "git config a.b c", "git stash", "git stash pop", "git branch feature", "git tag v9"]:
        assert guard_destructive.classify_readonly(command, str(project), str(project)), command
    not_intercepted = ["git bisect start", "git symbolic-ref HEAD refs/heads/x", "git update-index --assume-unchanged a.py", "git checkout-index -f -a",
                       "git read-tree HEAD", "git notes add -m n HEAD", "git remote add o ../x", "git remote remove o", "git reflog expire --expire=now --all",
                       "git gc", "git prune", "git pack-refs --all", "git sparse-checkout set src", "git submodule update --init", "git replace HEAD HEAD",
                       "git maintenance run", "git hash-object -w a.py", "git format-patch -1 -o .", "git archive -o out.tar HEAD"]
    for command in not_intercepted:
        assert guard_destructive.classify_readonly(command, str(project), str(project)) is None, command
    for name in ["bisect", "symbolic-ref", "update-index", "checkout-index", "read-tree", "notes add", "remote add and remove", "reflog expire", "gc",
                 "prune", "pack-refs", "sparse-checkout set", "submodule update", "replace", "maintenance run", "hash-object -w", "format-patch -o",
                 "archive -o"]:
        assert name in intercepted, name
    print("[IMP:9][test_documented_limits_match_behavior][LIMITS] asks=%d ask_limits=%d verbs=%d not_intercepted=%d" % (
        len(asks), len(limits), len(guard_destructive.MUTATING_GIT), len(not_intercepted)))
# endregion FUNC_test_documented_limits_match_behavior


# region FUNC_test_judge_scratch_rule [DOMAIN(9): Safety; CONCEPT(9): ReadOnlyJudge, ScratchRoot, EvidenceDirectory; TECH(7): pytest, git]
## @purpose Pin the judge scratch rule the workflow relies on: a redirect, tee, cp, touch, rm or mv by a read-only judge into a scratch root outside the project and its worktrees is silent, while the same write into any path inside the project or a worktree, the evidence directory of the project included, is denied with the write named.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree whose evidence directories are created after the first commit; one hook process per command; no command is executed. Guarantees: each JUDGE_SCRATCH_SILENT command gives no decision and exit code 0 for a plain and a namespaced judge; each JUDGE_PROJECT_DENIED command gives deny naming the write family and, for the evidence paths, the evidence directory, at most one path as typed; the coder and the root session write into the evidence directory silently. Raises: AssertionError on any difference.
##   System importance: 9. Example: a test report redirected into the scratch root is silent; the same redirect into the evidence directory of the project is denied.
## @complexity 5
def test_judge_scratch_rule(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    for root in (project, wt):
        (root / ".methodology" / "evidence").mkdir(parents=True)
    for agent in ("qa", "methodology-claude:reviewer"):
        for template in JUDGE_SCRATCH_SILENT:
            command = template.format(project=project, wt=wt, scratch=scratch)
            decision, reason, code = run_guard(command, project, agent=agent)
            print("[IMP:9][test_judge_scratch_rule][SILENT] %s %r -> %s" % (agent, template[:56], decision))
            assert (decision, code) == (None, 0), "%r -> %s" % (command, reason)
        for template, family in JUDGE_PROJECT_DENIED:
            command = template.format(project=project, wt=wt, scratch=scratch)
            decision, reason, _ = run_guard(command, project, agent=agent)
            print("[IMP:9][test_judge_scratch_rule][DENY] %s %r -> %s: %s" % (agent, template[:56], decision, reason[:90]))
            assert decision == "deny" and "Read-only agent (%s)" % agent in reason, command
            assert family in reason, "%r: reason %r lacks %r" % (command, reason, family)
            assert ("evidence" in reason) == ("evidence" in template), reason
            assert reason.count("evidence") <= 1  # one written path at most, never a repeated command
            assert_scratch_advice(reason)
    for other in ("coder", None):
        for template, _ in JUDGE_PROJECT_DENIED:
            command = template.format(project=project, wt=wt, scratch=scratch)
            assert run_guard(command, project, agent=other)[0] is None, (other, command)
# endregion FUNC_test_judge_scratch_rule


# region FUNC_test_scratch_prefix_never_exempts_the_project [DOMAIN(9): Safety; CONCEPT(9): ScratchRoot, SafePrefixes; TECH(7): pytest, git]
## @purpose Pin the two limits of the judge scratch rule: a scratch prefix (a configured one that is the parent of the project, and the defaults, under which the pytest directory itself lies) never exempts a path inside the project or a worktree, and a recursive removal in a scratch root asks unless the root lies under a safe prefix, so the workflow must name a scratch root under one.
## @uses test_guard.make_project, test_guard.make_repo, test_guard.run_guard
## @io Input: tmp_path. Output: None after the assertions. Side effects: a real repository with a sibling worktree; one hook process per command; no command is executed. Guarantees: with the parent of the project as the only safe prefix, and again with the default prefixes, a judge write into the project or its evidence directory is denied and a write into a sibling scratch directory is silent; the recursive removal of a scratch directory is silent under a configured prefix, silent under the default prefixes for a path under a default prefix, and asks when the scratch root is outside the project but under no safe prefix. Raises: AssertionError on any difference.
##   System importance: 8. Example: with the parent directory of the project as the safe prefix, a redirect into the project is still denied.
## @complexity 5
def test_scratch_prefix_never_exempts_the_project(tmp_path):
    project = make_project(tmp_path)
    wt = make_repo(project)
    scratch = tmp_path / "scratch"
    (project / ".methodology" / "evidence").mkdir(parents=True)
    default_scratch = "/tmp/methodology-judge-scratch"
    modes = {"parent-prefix": {"METHODOLOGY_GUARD_SAFE_PREFIXES": str(tmp_path)}, "default-prefixes": {"METHODOLOGY_GUARD_SAFE_PREFIXES": None}}
    for label, env in modes.items():
        for command in ["echo ok > %s/.methodology/evidence/r.txt" % project, "echo ok | tee %s/r.txt" % project, "cp a.py %s/.methodology/evidence/" % wt]:
            decision, reason, _ = run_guard(command, project, env_extra=env, agent="qa")
            print("[IMP:9][test_scratch_prefix_never_exempts_the_project][DENY] %s %r -> %s" % (label, command[:50], decision))
            assert decision == "deny" and "Read-only agent (qa)" in reason, (label, command)
        for command in ["echo ok > %s/r.txt" % scratch, "echo ok | tee %s/r.txt" % scratch, "cp a.py %s/" % scratch]:
            decision = run_guard(command, project, env_extra=env, agent="qa")[0]
            print("[IMP:9][test_scratch_prefix_never_exempts_the_project][SILENT] %s %r -> %s" % (label, command[:50], decision))
            assert decision is None, (label, command)
    assert run_guard("rm -rf %s/old" % scratch, project, env_extra=modes["parent-prefix"], agent="qa")[0] is None
    assert run_guard("rm -rf %s/old" % default_scratch, project, env_extra=modes["default-prefixes"], agent="qa")[0] is None
    assert run_guard("echo ok > %s/r.txt" % default_scratch, project, env_extra=modes["default-prefixes"], agent="qa")[0] is None
    decision, reason, _ = run_guard("rm -rf %s/old" % scratch, project, agent="qa")
    print("[IMP:9][test_scratch_prefix_never_exempts_the_project][REMOVAL] outside the project, under no safe prefix -> %s" % decision)
    assert decision == "ask" and reason.startswith("Destructive command (")
# endregion FUNC_test_scratch_prefix_never_exempts_the_project


# region FUNC_test_default_safe_prefixes [DOMAIN(8): Safety; CONCEPT(8): ScratchRoot, SafePrefixes; TECH(6): pytest, monkeypatch]
## @purpose Pin the default scratch roots of the guard so that a workflow can name a compatible scratch root: the four system temporary directories, TMPDIR added only to the defaults, and a configured list replacing them entirely.
## @uses guard_destructive.DEFAULT_SAFE, guard_destructive.Context
## @io Input: tmp_path and monkeypatch. Output: None after the assertions. Side effects: environment changes restored by monkeypatch. Guarantees: the literal default tuple equals the module constant; the context roots are the real paths of the four defaults, followed by TMPDIR when it is set; a configured list replaces the defaults and TMPDIR adds nothing then. Raises: AssertionError on any difference.
##   System importance: 8. Example: with nothing configured the scratch roots are the real paths of the system temporary directories.
## @complexity 3
def test_default_safe_prefixes(tmp_path, monkeypatch):
    monkeypatch.delenv("METHODOLOGY_GUARD_SAFE_PREFIXES", raising=False)
    monkeypatch.delenv("TMPDIR", raising=False)
    project = make_project(tmp_path)
    extra = tmp_path / "tmpdir"
    extra.mkdir()
    default_roots = [os.path.realpath(p) for p in DEFAULT_SAFE_PREFIXES]
    print("[IMP:9][test_default_safe_prefixes][DEFAULTS] %s" % ", ".join(DEFAULT_SAFE_PREFIXES))
    assert guard_destructive.DEFAULT_SAFE == DEFAULT_SAFE_PREFIXES
    assert guard_destructive.Context(str(project)).safe == default_roots
    monkeypatch.setenv("TMPDIR", str(extra))
    assert guard_destructive.Context(str(project)).safe == default_roots + [os.path.realpath(extra)]
    monkeypatch.setenv("METHODOLOGY_GUARD_SAFE_PREFIXES", str(tmp_path / "only"))
    assert guard_destructive.Context(str(project)).safe == [os.path.realpath(tmp_path / "only")]
# endregion FUNC_test_default_safe_prefixes


# region FUNC_test_custom_readonly_list_replaces_defaults [DOMAIN(8): Safety; CONCEPT(8): ConfigurableJudges; TECH(6): pytest]
## @purpose Verify that METHODOLOGY_GUARD_READONLY_AGENTS replaces the default list entirely, is trimmed and case-insensitive, and that an empty value leaves no read-only agent; also verify the default set directly.
## @uses test_guard.make_project, test_guard.run_guard, guard_destructive.readonly_agents
## @io Input: tmp_path and monkeypatch. Output: None after the assertions. Side effects: several hook processes; the process environment is restored by monkeypatch. Guarantees: the default set equals the six names; with the value auditor only auditor is denied and qa is not; the value of spaced mixed-case names matches; the empty value denies nobody. Raises: AssertionError on any difference.
##   System importance: 8. Example: the value Auditor, Qa yields the set auditor and qa.
## @complexity 4
def test_custom_readonly_list_replaces_defaults(tmp_path, monkeypatch):
    monkeypatch.delenv("METHODOLOGY_GUARD_READONLY_AGENTS", raising=False)
    assert guard_destructive.readonly_agents() == set(JUDGES)
    monkeypatch.setenv("METHODOLOGY_GUARD_READONLY_AGENTS", " Auditor , Qa ,,")
    assert guard_destructive.readonly_agents() == {"auditor", "qa"}
    monkeypatch.setenv("METHODOLOGY_GUARD_READONLY_AGENTS", "")
    assert guard_destructive.readonly_agents() == set()
    project = make_project(tmp_path)
    only_auditor = {"METHODOLOGY_GUARD_READONLY_AGENTS": "auditor"}
    assert run_guard("echo x > a.py", project, env_extra=only_auditor, agent="auditor")[0] == "deny"
    assert run_guard("echo x > a.py", project, env_extra=only_auditor, agent="qa")[0] is None
    assert run_guard("echo x > a.py", project, env_extra={"METHODOLOGY_GUARD_READONLY_AGENTS": ""}, agent="qa")[0] is None
# endregion FUNC_test_custom_readonly_list_replaces_defaults


# region FUNC_test_internal_error_is_silent [DOMAIN(9): Hooks; CONCEPT(9): NeverFailSession; TECH(7): pytest, monkeypatch]
## @purpose Verify that an exception raised inside the classifier is swallowed: exit value 0, nothing on stdout, and only an importance 10 FAIL record naming the error class.
## @uses guard_destructive.main, guard_destructive.classify
## @io Input: monkeypatch and caplog. Output: None after the assertions. Side effects: replaces classify for the test only; reads a payload from a string stream. Guarantees: main returns 0, the output stream stays empty, the only error record is the FAIL record without the exception message. Raises: AssertionError on any difference.
##   System importance: 9. Example: a RuntimeError with the message secret detail leaves no trace of the message.
## @complexity 3
def test_internal_error_is_silent(monkeypatch, caplog, tmp_path):
    caplog.set_level(logging.INFO)

    def explode(command, project_dir, cwd=None, _depth=0):
        raise RuntimeError("secret detail")

    monkeypatch.setattr(guard_destructive, "classify", explode)
    monkeypatch.delenv("METHODOLOGY_GUARD_SCOPE", raising=False)
    monkeypatch.delenv("METHODOLOGY_HOOK_LOG", raising=False)
    out = io.StringIO()
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": "git push --force"}, "cwd": str(tmp_path)})
    code = guard_destructive.main(stdin=io.StringIO(payload), stdout=out)
    show_records(caplog.records)
    assert code == 0 and out.getvalue() == ""
    errors = [r.getMessage() for r in caplog.records if r.levelno >= logging.ERROR]
    assert errors == ["[IMP:10][main][FAIL] kind=RuntimeError"]
# endregion FUNC_test_internal_error_is_silent


# region FUNC_test_hooks_json_command_asks_through_a_shell [DOMAIN(9): ClaudeCodeHooks; CONCEPT(9): ConfiguredCommand; TECH(7): json, subprocess, pytest]
## @purpose Verify the PreToolUse entry of hooks.json (matcher Bash, timeout, command text) and run its exact command through a shell as Claude Code does, for a destructive and a harmless payload.
## @uses json.loads, subprocess.run, test_guard.make_project
## @io Input: tmp_path. Output: None after the assertions. Side effects: two shell processes running python3 from the path. Guarantees: the command has no failure-swallowing suffix; the destructive payload gives one ask decision, the harmless one gives no output; both exit 0. Raises: AssertionError on any difference. System importance: 9.
##   Example: the configured timeout is 10 and the matcher is Bash.
## @complexity 4
def test_hooks_json_command_asks_through_a_shell(tmp_path):
    config = json.loads((PACKAGE / "hooks" / "hooks.json").read_text())
    entries = config["hooks"]["PreToolUse"]
    assert len(entries) == 1 and entries[0]["matcher"] == "Bash" and len(entries[0]["hooks"]) == 1
    hook = entries[0]["hooks"][0]
    assert hook["type"] == "command" and hook["timeout"] == 10
    assert hook["command"] == 'python3 "${CLAUDE_PLUGIN_ROOT}/hooks/guard_destructive.py"'
    assert "||" not in hook["command"] and ";" not in hook["command"]
    assert sorted(config["hooks"]) == ["PreToolUse", "SessionStart"]
    project = make_project(tmp_path)
    env = {k: v for k, v in os.environ.items() if not k.startswith("METHODOLOGY_")}
    env.update(CLAUDE_PLUGIN_ROOT=str(PACKAGE), CLAUDE_PROJECT_DIR=str(project), METHODOLOGY_GUARD_SAFE_PREFIXES="/nonexistent-scratch")
    results = []
    for command in ("git push --force", "git status"):
        payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}, "cwd": str(project)})
        done = subprocess.run(hook["command"], shell=True, input=payload, capture_output=True, text=True, env=env, cwd=str(tmp_path), timeout=60)
        print("[IMP:9][test_hooks_json_command_asks_through_a_shell][SHELL] %r exit=%d stdout_chars=%d stderr_chars=%d" % (command, done.returncode, len(done.stdout), len(done.stderr)))
        results.append(done)
    assert all(done.returncode == 0 and done.stderr == "" for done in results)
    assert json.loads(results[0].stdout)["hookSpecificOutput"]["permissionDecision"] == "ask"
    assert results[1].stdout == ""
# endregion FUNC_test_hooks_json_command_asks_through_a_shell


# region FUNC_test_heredoc_and_segmentation_units [DOMAIN(8): ShellParsing; CONCEPT(8): Segmentation; TECH(6): pytest]
## @purpose Verify the pure parsing functions by direct import: heredoc bodies are set aside in order (tab-stripped and unterminated forms included), segmentation splits on every separator, and redirection targets and file descriptor digits are handled as documented.
## @uses guard_destructive.split_heredocs, guard_destructive.simple_commands, guard_destructive._tokens
## @io Input: caplog. Output: None after the assertions. Side effects: prints its own importance 9 trace lines (the heredoc body count per case, the simple command count per case and the tokens) before the assertions. Guarantees: expected values are fixed by the documented behavior. Raises: AssertionError on any difference. System importance: 8.
##   Example: a cat command with a quoted EOF heredoc returns the cat line as kept text and the body as the only body.
## @complexity 5
def test_heredoc_and_segmentation_units(caplog):
    caplog.set_level(logging.DEBUG)
    kept, bodies = guard_destructive.split_heredocs("cat > f <<'EOF'\nrm -rf /\nEOF\necho done")
    kept_tabs, bodies_tabs = guard_destructive.split_heredocs("cat <<-END\n\tbody\n\tEND\nls")
    kept_open, bodies_open = guard_destructive.split_heredocs("cat <<EOF\nnever closed")
    kept_two, bodies_two = guard_destructive.split_heredocs("a <<X <<Y\none\nX\ntwo\nY\nz")
    kept_string, bodies_string = guard_destructive.split_heredocs("cat <<< 'word'\nls")
    segments = [guard_destructive.simple_commands("a && b | c; d\ne"), guard_destructive.simple_commands("(cd x; rm -rf y)"),
                guard_destructive.simple_commands("echo x > out.txt 2>/dev/null", with_redirects=True),
                guard_destructive.simple_commands("cat <<EOF\nsqlite3 <<SQL", with_redirects=False), guard_destructive.simple_commands("echo a \\\n b"),
                guard_destructive.simple_commands("echo x # rm -rf /")]
    show_records(caplog.records)
    print("[IMP:9][test_heredoc_and_segmentation_units][HEREDOCS] bodies_per_case=%s" % [len(b) for b in (bodies, bodies_tabs, bodies_open, bodies_two, bodies_string)])
    print("[IMP:9][test_heredoc_and_segmentation_units][SEGMENTS] simple_commands_per_case=%s tokens=%s" % ([len(c) for c in segments], guard_destructive._tokens("a;b")))
    assert (kept, bodies) == ("cat > f <<'EOF'\necho done", ["rm -rf /"])
    assert (kept_tabs, bodies_tabs) == ("cat <<-END\nls", ["\tbody"])
    assert (kept_open, bodies_open) == ("cat <<EOF", ["never closed"])
    assert (kept_two, bodies_two) == ("a <<X <<Y\nz", ["one", "two"])
    assert (kept_string, bodies_string) == ("cat <<< 'word'\nls", [])
    assert guard_destructive._tokens("a;b") == ["a", ";", "b"]
    assert segments[0] == [["a"], ["b"], ["c"], ["d"], ["e"]]
    assert segments[1] == [["cd", "x"], ["rm", "-rf", "y"]]
    assert segments[2] == [(["echo", "x"], ["out.txt", "/dev/null"])]
    assert segments[3] == [["cat", "<<#0"], ["sqlite3", "<<#1"]]
    assert segments[4] == [["echo", "a", "b"]]
    assert segments[5] == [["echo", "x"]]
# endregion FUNC_test_heredoc_and_segmentation_units


# region FUNC_test_scope_functions [DOMAIN(8): Scope; CONCEPT(8): OwnerSwitch; TECH(6): pytest, monkeypatch]
## @purpose Verify the activation function directly for unset, all, off, spaced and unknown values.
## @uses guard_destructive.guard_active
## @io Input: monkeypatch and caplog. Output: None after the assertions. Side effects: environment changes restored by monkeypatch; prints its own importance 9 trace line with the result per value and the count of switched-off records before the assertions. Guarantees: only a value that equals off after trimming and lower-casing returns False. Raises: AssertionError on any difference. System importance: 8.
##   Example: the value Off returns False and the value declared returns True.
## @complexity 3
def test_scope_functions(monkeypatch, caplog):
    caplog.set_level(logging.INFO)
    monkeypatch.delenv("METHODOLOGY_GUARD_SCOPE", raising=False)
    results = {"unset": guard_destructive.guard_active()}
    for value in ("all", "off", "Off", "  off  ", "declared", "", "disabled"):
        monkeypatch.setenv("METHODOLOGY_GUARD_SCOPE", value)
        results[value] = guard_destructive.guard_active()
    show_records(caplog.records)
    switched = [r.getMessage() for r in caplog.records if "[SWITCHED_OFF]" in r.getMessage()]
    print("[IMP:9][test_scope_functions][RESULTS] active=%s switched_off_records=%d" % (results, len(switched)))
    assert results == {"unset": True, "all": True, "off": False, "Off": False, "  off  ": False, "declared": True, "": True, "disabled": True}
    assert len(switched) == 3
# endregion FUNC_test_scope_functions


# region FUNC_test_context_path_scope [DOMAIN(8): Safety; CONCEPT(8): PathScope; TECH(6): pytest, git]
## @purpose Verify the path scope methods: a sibling directory sharing a name prefix is not inside, scratch roots are inside but not in the project, a worktree counts as the project, and the project or any directory above it is flagged as whole-project deletion.
## @uses guard_destructive.Context
## @io Input: tmp_path and monkeypatch. Output: None after the assertions. Side effects: a real repository and worktree; the prefix variable is set through monkeypatch. Guarantees: expected booleans are fixed by the documented rules. Raises: AssertionError on any difference. System importance: 8.
##   Example: the parent of the project directory is project-or-above and not a project path.
## @complexity 5
def test_context_path_scope(tmp_path, monkeypatch):
    scratch = tmp_path / "scratch"
    scratch.mkdir()
    monkeypatch.setenv("METHODOLOGY_GUARD_SAFE_PREFIXES", str(scratch))
    project = make_project(tmp_path)
    wt = make_repo(project)
    lookalike = tmp_path / "proj-lookalike"
    lookalike.mkdir()
    ctx = guard_destructive.Context(str(project))
    roots = ctx.roots()
    print("[IMP:9][test_context_path_scope][ROOTS] roots=%d" % len(roots))
    assert sorted(roots) == sorted([os.path.realpath(project), os.path.realpath(wt)])
    assert ctx.in_project(os.path.realpath(wt / "a.py")) and ctx.in_project(os.path.realpath(project))
    assert not ctx.in_project(os.path.realpath(lookalike)) and not ctx.inside(os.path.realpath(lookalike))
    assert ctx.inside(os.path.realpath(scratch / "x")) and not ctx.in_project(os.path.realpath(scratch / "x"))
    assert ctx.is_project_or_above(os.path.realpath(project)) and ctx.is_project_or_above(os.path.realpath(tmp_path))
    assert not ctx.is_project_or_above(os.path.realpath(project / "sub"))
    assert ctx.resolve("") is None and ctx.resolve("$(pwd)") is None and ctx.resolve("$NO_SUCH_VARIABLE_FOR_TEST/x") is None
    ctx.vars["S"] = str(scratch)
    assert ctx.resolve("$S/y") == os.path.realpath(scratch / "y")
# endregion FUNC_test_context_path_scope


# region FUNC_test_adapted_source_has_no_legacy_names [DOMAIN(8): Testing; CONCEPT(8): AdaptationRegression; TECH(6): pytest]
## @purpose Verify that the adapted guard carries the new environment names and none of the retired wording or switches of the donor version.
## @uses pathlib.Path.read_text
## @io Input: none. Output: None after the assertions. Side effects: reads the guard source. Guarantees: the retired names are assembled from parts so this file does not carry them; the new switches and the neutral owners are present. Raises: AssertionError on any difference. System importance: 8.
##   Example: the retired mode variable name is not found and METHODOLOGY_GUARD_MODE is.
## @complexity 2
def test_adapted_source_has_no_legacy_names():
    source = SCRIPT.read_text()
    retired = ["PRODUCT" + "_GUARD", "Project " + "Conventions", "CV" + "-5", "CONVENTIONS" + "_RE", "GUARD" + "_LOG", "declared" + " project"]
    present = ["METHODOLOGY_GUARD_MODE", "METHODOLOGY_GUARD_SCOPE", "METHODOLOGY_GUARD_SAFE_PREFIXES", "METHODOLOGY_GUARD_READONLY_AGENTS",
               "METHODOLOGY_HOOK_LOG", "process/safety.md", "roles/qa.md", "methodology-claude:searcher"]
    print("[IMP:9][test_adapted_source_has_no_legacy_names][SCAN] retired=%d present=%d" % (len(retired), len(present)))
    assert [name for name in retired if name in source] == []
    assert [name for name in present if name not in source] == []
# endregion FUNC_test_adapted_source_has_no_legacy_names


# region FUNC_test_hook_files_are_public_clean [DOMAIN(8): Testing; CONCEPT(8): PublicContent; TECH(6): regex, pathlib]
## @purpose Verify that the hook sources, the hook configuration and both hook test modules carry no absolute home path, no tilde path and no e-mail address, because the repository is published.
## @uses pathlib.Path.read_text, re.compile
## @io Input: none. Output: None after the assertions. Side effects: reads five files. Guarantees: the markers are assembled from parts, so this file passes its own scan; every file is scanned in full. Raises: AssertionError listing offending files. System importance: 8.
##   Example: a line holding a users-directory home path in any hook file fails the test.
## @complexity 3
def test_hook_files_are_public_clean():
    files = [PACKAGE / "hooks" / name for name in ("guard_destructive.py", "session_start.py", "hooks.json")]
    files += [PACKAGE / "tests" / name for name in ("test_guard.py", "test_session_start.py")]
    markers = ["/" + "Users" + "/", "/" + "home" + "/", "~" + "/"]
    address = re.compile(r"[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+")
    offenders = []
    for path in files:
        text = path.read_text()
        if any(marker in text for marker in markers) or address.search(text):
            offenders.append(path.name)
    print("[IMP:9][test_hook_files_are_public_clean][SCAN] files=%d offenders=%s" % (len(files), offenders))
    assert len(files) == 5 and offenders == []
# endregion FUNC_test_hook_files_are_public_clean
