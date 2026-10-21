# Methodology DSH

**For persistent personal use, install this package as the `@methodology/dsh` bundle in a DeepSeek Harness profile.** Cloning the source or asking an agent to read a skill is not installation. The steps below register the bundle and check that the harness actually discovers the methodology skills.

Native DSH implementation package 3.1.0 for neutral methodology 3.1.0.

## Installation

Prerequisites: a DSH installation that exposes `dsh plugin --profile <name> <pnpm args>`, a complete checkout of this repository (both this package and the neutral owners beside it), Python 3, and Doxygen and pytest only when a software task requires them. Check the CLI surface with `dsh plugin --help`; if `dsh plugin` is unavailable, report the actual host or version limitation instead of installing by hand.

1. Clone the complete repository to a permanent checkout, or use an existing one. Keep the target consumer project separate. The package is installed **in place**: the neutral owners live at the repository root, and `adapter.json` resolves them through `spec_root: ../../`.
2. Back up the profile's `package.json` and `cordis.patch.yml` first, so the change can be undone in one step.

```sh
cd /absolute/path/to/galaxica-sombrero
cp "$HOME/.dsh/profiles/web/package.json" "$HOME/.dsh/profiles/web/package.json.bak"
cp "$HOME/.dsh/profiles/web/cordis.patch.yml" "$HOME/.dsh/profiles/web/cordis.patch.yml.bak"
dsh plugin --profile web add ./implementations/dsh
```

Replace `web` with the actual profile name. The command forwards to pnpm in the profile directory, links the package, and appends `@methodology/dsh` to `dsh.profile.bundles` because the package declares `dsh.bundle`.

3. Verify that the bundle layer is composed and that its row is present:

```sh
dsh --profile web --dump-config | grep -A8 'methodology-skill-filesystem'
```

Expect a `# == @methodology/dsh` layer header and then the row carrying `providerName: methodology`, `includeDefaultRoots: false` and one `customSkillDirs` entry. `--dump-config` prints loader expressions unevaluated, so that entry appears as the `!!js` expression rather than as a path; that is expected and is not a failure. A missing layer header means the bundle is not composed: check that `@methodology/dsh` is in the profile's `dsh.profile.bundles` and that the profile was restarted.

To see the value the expression actually produces, resolve it the way the loader does, from the profile directory:

```sh
node -e "const{createRequire}=require('node:module'),p=require('node:path');const r=createRequire(process.argv[1]).resolve('@methodology/dsh/package.json');console.log(p.join(p.dirname(r),'skills'))" "$HOME/.dsh/profiles/web/"
```

The printed path must exist and end in `implementations/dsh/skills`. A successful `add` alone proves nothing about discovery, and a printed expression is not a resolved root.

4. Restart the profile and start a fresh session. Check that the skill catalog contains the methodology entries (`pm`, `pm-bootstrap`, `feature-dev`, `brainstorm`, and the rest of this package's `skills/`). Confirm that the discovered skills resolve to this checkout: open one and compare its `Base directory for this skill:` line with the path printed in step 3. Then confirm that `adapter.json` resolves `../../` to the checkout's matching `SPEC_VERSION` and neutral owners.

Installation does not adopt the methodology in any consumer project. For first use, invoke `pm` in the actual target project; use `pm-bootstrap` only when the owner asks for onboarding.

To update, `git pull` the checkout and restart the profile: the bundle reads this package in place, so there is no snapshot to refresh. To roll back, restore both saved files and restart.

## What installing this package changes

The bundle adds exactly one host-plane row, `methodology-skill-filesystem`: a second local skill provider whose only root is this package's `skills/` directory, with `includeDefaultRoots: false` and a unique `providerName`. It does not touch the base `skill-filesystem` row, the profile's default preset, the model configuration or any tool.

The consequence, and the reason the row is a second provider rather than an edit to the existing one:

| Discovery root | Rank | Owner |
|---|---|---|
| `<project>/.dsh/skills`, `<project>/.agents/skills` | 100, 200 | the preset's own `skill-filesystem` provider |
| **this package's `skills/`** | **300** | **`methodology-skill-filesystem` (this bundle)** |
| the harness home `skills` directory and the shared agents-home `skills` directory | 400, 500 | the preset's provider |

So the methodology catalog reaches every session regardless of the selected preset, while a project skill of the same name still wins on rank. A session in the `minimal` preset, which mounts no skill surface of its own, still receives the methodology catalog through this provider.

This package ships no session-start hook, no tool, no daemon and no model launcher. It cannot force plan mode, cannot restrict a role's tools, and cannot inject instructions into a session: those are preset and profile decisions, described below.

## Role isolation in DSH

A DSH subagent joins its parent's preset revision and inherits that scope chain, including the skill catalog. Neither the `subagent` tool, `subagent_fork`, nor a workflow script can inject per-child instructions or select a different preset for a child. The only native lever is the fixed per-instance configuration of a delegation tool:

```yaml
- id: delegate-qa
  name: '@deepseek-ai/dsh-tool-subagent'
  config:
    provider: spawn
    toolName: delegate_qa
    persona: >-
      You are the methodology QA role. Before acting, read the role carrier named
      in the delegation prompt in full, then read every owner it names, and treat
      the original source and Git as read-only.
    toolFilter:
      deny: [write, edit, workflow]
    maxDepth: 0
```

`persona`, `toolFilter` and `maxDepth` are fixed per registered instance, never per call. `toolFilter` subtracts tools: a filtered tool disappears from the child's prompt and refuses to execute. A numeric `maxDepth` requires the provider's `depthLimit` capability, and an unknown tool name in `toolFilter` fails the plugin mount rather than the first delegation.

A child also runs with the parent session's sandbox override and an approval policy pinned to `never`. An approval-requiring call inside a child is refused deterministically, so an operation that needs interactive approval must happen in the parent.

This package therefore does not ship a preset. Authoring one replaces the complete child-plugin list and takes on the whole standard surface (persona, instructions, tools, compaction, delegation, skills) as your deployment's decision, not as a methodology default. `references/dsh-runtime.md` records what the framework's role contracts require of such a preset and states plainly where the native surface cannot meet them.

## Source loading and package contract

Supported profile is `colocated-explicit-source`: a complete checkout with this package beside the neutral owners it resolves. Resolve this actual package, its adapter and the current neutral root; read [runtime](references/dsh-runtime.md) and [adoption](references/adoption.md) before `pm` or `feature-dev`. A detached package-only copy is unsupported and a missing required neutral dependency is BLOCKED, never a fallback to an older installed package.

`pm` resumes the actual five project record roles and prepares RECON and the specification; `feature-dev` uses an authentic exact approved specification and actual target to dispatch native Bootstrap → Architect → Code → independent QA → Review → separately assigned Architect Finalize. Root alone owns state, counters and integration. This package launches no model engine or daemon and does not alter configured models. Inner roles cannot delegate, commit or merge. Reading a carrier grants no role and no consent.

The current package has 27 narrow skill entries, six role carriers, six Python helpers, a DSH bundle manifest and a plugin manifest. [Layout](references/package-layout.json) enumerates all 75 exact own-format regular members except itself, with no embedded content or self hashes. [Source dispositions](references/source-disposition.md) preserves the original duty and topic catalogue and accounts the current converse obligations. Historical validation is not fresh package proof, and license or publication rights are not invented. Native SKILL cards use DSH `name`/`description` frontmatter; roles and references are Markdown, the adapter, plugin, package and layout files are JSON, helpers and tests are Python, and the composition files are YAML. Neutral cards stay outside this package under their own FORMAT contract.

Run the declared commands on a complete canonical owned source export; do not report strings as executions:

```text
bin/conform self --deny-list PRIVATE_DENY_LIST
bin/conform adapter implementations/dsh/adapter.json
python3 -m pytest tests -p no:cacheprovider -s -v --basetemp OWNED_COMMON_ROOT
python3 -m pytest -c implementations/dsh/pytest.ini implementations/dsh/tests -p no:cacheprovider -s -v --basetemp OWNED_PACKAGE_ROOT
doxygen Doxyfile
```

Set `PYTHONDONTWRITEBYTECODE=1` for Python checks; read warnings, full streams and actual counters. The package map additionally runs `doxygen Doxyfile` from `implementations/dsh`; its own config and XML associations are separate from the root map. [Handoffs](references/handoffs.md) declares helper init/show/record, immutable input locks, the current target digest, eight named scans, a zero-valid default cumulative Debug-entry cap of 4 and separate retries. Neither unit fixtures nor helper state simulations establish native agents or real delivery.

[Smoke specification](examples/smoke-spec.md) is a reusable inventory-report task with exact target paths and source-derived output and refusals. Templates never authenticate grants. Candidate-bound native execution, one real same-run checkpoint and resume, independent source, case, QA, Review and Finalize, and committed-artifact proof remain required before claiming package acceptance; installed historical results do not substitute. SUCCESS does not authorize merge, installation or publication, and the matching concrete-result integration decision stays separate.

Current source version is 3.1.0 over neutral 3.1.0. Wire `methodology-dsh/2.0.0` and schema 2 are the run-state contract shared with the sibling packages. No loader activation and no full-methodology parity is certified by this release.

## Consumer profile and commands

The full opt-in [consumer profile](references/consumer-pm-profile.md) declares its source duties, checklist rows, seeds, actual entries and exact source-only command, grammar, receipt and safety contracts. Use explicit `python3 -B PACKAGE/skills/pm/scripts/orient.py PROJECT [--check]`, `codemap.py PROJECT TARGET`, and `markup_migrate.py PROJECT [--check | --apply]`. Portfolio takes only explicit roots or a roots file. Apply requires exact recorded parent-authenticated scope, originals and plan, plus outside recovery. No automatic adoption, build, Git, provider or installation action.

Automatic hooks and trust, SDK import and ingest, whole autonomous and resume proof, and loader handover remain held. Existing consumer homes, links and history are preserved; a missing preferred filename never implies greenfield.

## Limits of this package

- **Not behaviourally accepted.** The adapter, inventory and the package tests are structural and source checks. No native run, checkpoint, resume or independent QA of this package has been performed on a real target.
- **No preset, no hooks, no role enforcement.** The bundle adds a skill provider and nothing else. Role isolation, plan mode and instruction injection are deployment decisions this package documents but does not impose.
- **A child cannot be given its own instructions or skill catalog.** This is a property of the DSH delegation seam, not a gap this package can close; the workaround is one configured delegation tool per role.
- **The bundle requires a profile restart** to take effect, and an update requires a restart as well.
- **Detection is one level deep.** Only `<root>/<name>/SKILL.md` and `<root>/<name>.md` are discovered; the skill name comes from frontmatter, not the directory name.
