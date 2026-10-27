# Methodology Codex

**For persistent personal use, install this package as the `methodology-codex` Codex plugin.** Cloning the source or asking an agent to read a skill is not installation. Follow the steps below on a new machine; explicit source loading remains available for a one-session trial.

## Personal plugin installation

Prerequisites: Git, Python 3, access to this repository, and a Codex CLI exposing `codex plugin marketplace add` and `codex plugin add`. Check those commands with `--help`; if unavailable, report the actual host/version limitation. Doxygen and pytest are not required to register the plugin; software tasks have their own prerequisites.

1. Clone the complete repository to a permanent source checkout, or use an existing checkout. Select the actual commit the owner wants to install. Keep the target consumer project separate. Run the packaging example below from the repository root; it packages committed `HEAD`, excluding uncommitted edits and ignored/private evidence.
2. Prepare a dedicated local marketplace containing a full snapshot. The example uses `$HOME/.local/share/methodology-personal` and marketplace name `methodology-personal`. If that location or marketplace name already exists, preserve it and inspect its configuration before updating; do not overwrite it or replace unrelated entries. For an update, retain the previous snapshot and configuration for rollback.

```sh
git clone REPOSITORY_URL methodology-source
cd methodology-source
```

Replace `REPOSITORY_URL` with the repository URL supplied by the owner. Skip the clone commands if already in the intended checkout. This Python example prepares files only; it does not install or change Codex settings. It deliberately refuses to reuse an existing destination. Choose another unused destination/name if needed, and use that same pair in the commands that follow.

```sh
python3 - <<'PY'
import io
import json
from pathlib import Path
import subprocess
import tarfile

commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
market = Path.home() / ".local/share/methodology-personal"
if market.exists():
    raise SystemExit("Destination exists; inspect and preserve its setup before updating.")
payload = subprocess.check_output(["git", "archive", "--format=tar", commit])
snapshot = market / "releases" / commit / "repository"
snapshot.mkdir(parents=True)
with tarfile.open(fileobj=io.BytesIO(payload)) as archive:
    archive.extractall(snapshot)
manifest = json.loads((snapshot / "implementations/codex/.codex-plugin/plugin.json").read_text())
manifest["skills"] = "./implementations/codex/skills/"
transport = snapshot / ".codex-plugin/plugin.json"
transport.parent.mkdir(exist_ok=True)
transport.write_text(json.dumps(manifest, indent=2) + "\n")
catalog = market / ".agents/plugins/marketplace.json"
catalog.parent.mkdir(parents=True)
catalog.write_text(json.dumps({
    "name": "methodology-personal",
    "plugins": [{
        "name": "methodology-codex",
        "source": {"source": "local", "path": "./releases/" + commit + "/repository"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity"
    }]
}, indent=2) + "\n")
print("Prepared", manifest["name"], manifest["version"], "from", commit)
print("Marketplace:", market)
PY
```

The generated root `.codex-plugin/plugin.json` is a transport overlay: copy the nested manifest and change only `skills` to `./implementations/codex/skills/`. Keep all tracked repository files and executable modes, including the nested adapter and neutral owners. Do not install the nested package by itself or flatten its skills. This repository does not currently ship a root marketplace that makes a bare GitHub URL a complete installation command.

3. Before activation, back up the existing user Codex configuration and any marketplace configuration that will change, retaining their paths for rollback. Register the prepared marketplace and install through the native CLI:

```sh
codex plugin marketplace add "$HOME/.local/share/methodology-personal"
codex plugin add methodology-codex@methodology-personal
codex plugin list --json
```

4. Check that the list reports the intended plugin/version/marketplace as enabled. Start a fresh Codex session and check actual skill discovery for `methodology-codex:pm`, `methodology-codex:pm-bootstrap` and `methodology-codex:feature-dev`, using the host's skill catalog. Confirm that the discovered skills resolve to the installed complete snapshot and that its nested `adapter.json` resolves `../../` to the snapshot's matching `SPEC_VERSION` and shared rules. A successful command alone does not prove discovery; report unavailable checks explicitly. Installation does not by itself adopt the methodology in any consumer project.

For first use, invoke the installed `pm` skill in the actual target project. Use `pm-bootstrap` when the owner requests onboarding; preserve existing project rules and document homes. To update later, prepare a new complete snapshot, preserve the previous version/configuration, update only this plugin's marketplace source, reinstall and repeat the checks. Roll back using the saved source/configuration through the host's native plugin controls.

This follows the existing complete-snapshot transport, not a new installer or standalone package profile. Native marketplace/manifest conventions: [official OpenAI documentation](https://developers.openai.com/plugins/build/plugins). Host capabilities can vary; use its actual CLI help and report missing support.

## Source loading and package contract

Native Codex implementation package3.1.1 for neutral methodology3.1.1. Supported profile is a complete co-located checkout with explicit source loading. Resolve this actual package, its adapter and current neutral root; read [runtime](references/codex-runtime.md) and [adoption](references/adoption.md) before `$pm` or `$feature-dev`. Native installation uses a complete repository snapshot with a generated root transport manifest whose `skills` is `./implementations/codex/skills/`; this preserves the supported nested package binding. A detached package-only cache copy is unsupported; missing required neutral dependency is BLOCKED, never fallback to an older installed package.

`pm` resumes the actual five project record roles and prepares RECON/spec; `feature-dev` uses an authentic exact approved specification and actual target to dispatch native Bootstrap→Architect→Code→independent QA→Review→separately assigned Architect Finalize. Root alone owns state, counters and integration. This package launches no model engine or daemon and does not alter configured models. Inner roles cannot delegate/commit. Reading a carrier grants no role or consent.

The current package has27 narrow skill entries, six role carriers and six helpers. [Layout](references/package-layout.json) enumerates all73 exact own-format regular members including itself, with no embedded content/self hashes. [Source dispositions](references/source-disposition.md) preserves the original38-duty/23-topic catalogue and accounts the current C2 converse obligations; the historical47-member/23-skill/two-helper construction frame is distinct from current composition; true shared-topic parity remains23 after excluding declared lifecycle entries. Historical validation is not fresh package proof and license/publication rights are not invented. Native SKILL cards use name/description, roles/references Markdown, adapter/plugin/layout JSON, helpers/tests Python and native configuration formats. Neutral cards stay outside this package under their own FORMAT contract. All intended public package members remain in publication/privacy traversal.

Run declared target commands on a complete canonical owned source export; do not report strings as executions:

```text
bin/conform self --deny-list PRIVATE_DENY_LIST
bin/conform adapter implementations/codex/adapter.json
python3 -m pytest tests -p no:cacheprovider -s -v --basetemp OWNED_COMMON_ROOT
python3 -m pytest -c implementations/codex/pytest.ini implementations/codex/tests -p no:cacheprovider -s -v --basetemp OWNED_PACKAGE_ROOT
doxygen Doxyfile
```

Set PYTHONDONTWRITEBYTECODE=1 for Python checks; read warnings/full streams and actual counters. Package map additionally runs `doxygen Doxyfile` from implementations/codex; its own config/XML associations are separate from root map. Actual plan/test guide resolves commands and permitted resources. [Handoffs](references/handoffs.md) declares helper init/show/record, immutable input locks and current target digest, eight named scans, zero-valid default4 cumulative Debug-entry cap and separate retries. Neither unit fixtures nor helper state simulations establish native agents or real delivery.

[Smoke specification](examples/smoke-spec.md) is a reusable useful inventory-report task with exact target paths and source-derived output/refusals. Templates never authenticate grants. Actual candidate-bound native execution and one real same-run checkpoint/resume, independent source/case/QA/Review/Finalize and committed-artifact proof remain required before claiming package acceptance; installed historical results do not substitute. SUCCESS does not authorize merge/install/publication. Matching concrete-result integration decision stays separate.

Current source version is3.1.1 over neutral3.1.1. Wire methodology-codex/2.0.0 and schema2 remain unchanged; both complete review owners and the one-shot/loop three-artifact prompt route are read through current adoption. No loader activation or full-methodology parity is certified by this release.

## Consumer profile and commands

The full opt-in [consumer profile](references/consumer-pm-profile.md) declares75 source duties/22 checklist rows/13seeds/four actual entries and exact source-only command/grammar/receipt/safety contracts. Package73 members,27skills,sixhelpers,sixroles; neutral2.0/wire2.0/schema2; established consumer profile unchanged. Use explicit `python3 -B PACKAGE/skills/pm/scripts/orient.py PROJECT [--check]`, `codemap.py PROJECT TARGET`, and `markup_migrate.py PROJECT [--check | --apply]`. Portfolio takes only explicit roots/roots-file. Apply requires exact recorded parent-authenticated scope/originals/plan and outside recovery; C2 promised Python3.9+ and3.12 proof population is supplied through repeated --python. No automatic adoption/build/Git/provider/install. Own map receipt schema: `.methodology/maps/current.json` config path/hash, sources sorted path/hash/mode, index path/hash, build argv/cwd/exitCode/at/stdout/stderr with actual contained captured silent stream files. Read full profile for bounded grammar and current own-XML/query distinction.

C3 automatic hooks/trust, C4 SDK/import/ingest/ledger comparison, C5 whole autonomous/resume/isolation proof and C6 loader handover remain held. Existing original consumer homes/links/history and accepted decision bodies are preserved; missing preferred filename never implies greenfield.
