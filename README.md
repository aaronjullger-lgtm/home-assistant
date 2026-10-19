# home-assistant

Household Home Assistant repository focused on reliable, privacy-conscious, reversible automation.

## Current status

This repository now includes:
- A version-controlled `config/` baseline using Home Assistant packages.
- A synthetic, runnable context + pathway-lighting slice for safe iteration before binding real entities.
- Documentation for inventory, architecture, automation catalog, roadmap, operations, and session handoff.
- Validation workflow for YAML linting and Home Assistant configuration checks (no deployment).

## Project map

- `config/` live YAML configuration intended for Home Assistant.
- `config/packages/context_pathway_demo.yaml` synthetic milestone automation slice.
- `examples/` non-live examples requiring real entity mapping.
- `docs/` inventory, decisions, architecture, catalog, operations, roadmap, and handoff.
- `scripts/validate.sh` local validation entrypoint.
- `.github/workflows/validate.yml` CI validation only.

## Validation

From repository root:

```bash
bash scripts/validate.sh
```

The script:
1. Runs `yamllint` on repository YAML.
2. Runs Home Assistant `check_config` when `hass` is available.

Run the repository regression tests separately with:

```bash
python3 -m unittest discover -s tests -v
```

## Setup notes

- Keep real secrets in `config/secrets.yaml` (gitignored).
- Keep sensitive/private inventory details in `docs/inventory.private.md` (gitignored).
- Do not commit `.storage`, databases, recordings, or occupancy history.
