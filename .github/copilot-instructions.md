# Repository instructions for Copilot agents

## Scope
- This repo stores Home Assistant configuration, docs, and validation tooling.
- Prefer native HA helpers/templates/scripts/automations over custom code.

## Safety and privacy
- Never invent live entities or claim deployment/testing in the real house.
- Keep private data out of git: `config/secrets.yaml`, `.storage`, DBs, recordings.
- Use synthetic fixtures for behavior design when device mapping is unknown.

## Validation commands
- Primary: `bash /home/runner/work/home-assistant/home-assistant/scripts/validate.sh`
- If `hass` is unavailable, report that HA schema validation was skipped.

## Architecture expectations
- Separate observations, derived context, and actions.
- Document override precedence, cooldowns, and restart behavior for automations.
- Keep unresolved real-device mappings in `examples/`, not active config includes.
