# Architecture (milestone 1)

## Behavioral layers

1. **Observations**: raw sensor states/events (motion, contacts, person/zone, climate, camera events).
2. **Derived context**: freshness/confidence/provenance helpers (e.g., occupancy confidence and source).
3. **Actions**: lighting/scenes/notifications/device commands with explicit override precedence.

## Ownership boundaries

- **YAML-owned** (this repo): package structure, synthetic milestone slice, validation workflow, documented automation rules.
- **UI-owned** (current and future): existing UI-created automations/integrations unless intentionally migrated.
- **External-service-owned**: Frigate, voice pipelines, grocery systems once introduced.

## Precedence and recovery principles

- Manual override beats routine automation for its scope/duration.
- Sleep/focus/movie/guest/cleaning mode constraints are conditions, not assumptions.
- Unknown/unavailable context never treated as false-safe.
- Timed changes expire with explicit recovery checks.
- Automation modes are selected intentionally (`restart` for motion restarts, `single` for finish events, `queued` for event logging).

## Applied pattern references

- Package modularity and minimal bootstrap from `frenck/home-assistant-config`.
- Watchdog/timer patterns from `skalavala/mysmarthome` and `avbor/HomeAssistantConfig`.
- Frigate retention/detection tuning concepts from `blakeblackshear/frigate`.

See `docs/decisions.md` for exact links and license notes.
