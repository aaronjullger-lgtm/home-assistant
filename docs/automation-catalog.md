# Automation catalog (prioritized)

Status values: **Proposed**, **Implemented**, **Validated locally**, **Enabled in house**.

## 1) Context + entry pathway lighting (milestone slice)
- Purpose: demonstrate observation → derived context → action with overrides and recovery.
- Prerequisites: helpers in `config/packages/context_pathway_demo.yaml`.
- Trigger: synthetic entry motion helper.
- Conditions: house occupied, sleep mode off, no manual override.
- Action: pathway light helper on + hold timer.
- Override: manual override helper pauses automation.
- Fallback: timer expiry turns light off only if clear.
- Verification scenario: motion on/off with occupied/away and manual override toggles.
- Status: **Implemented**, pending live-entity mapping.

## 2) Humidity-driven bathroom fan + shower light retention
- Purpose: comfort and mold prevention without overrun noise.
- Prerequisites: reliable humidity and fan/light entities.
- Trigger: humidity rise-rate threshold and absolute delta.
- Conditions: occupancy context to avoid premature off.
- Action: fan on, keep light during active shower.
- Override: guest/night mode caps noise and duration.
- Fallback: max runtime cutoff + notification on sensor unavailable.
- Status: **Proposed**.

## 3) Arrival lighting with neutral fallback and optional personal scene
- Purpose: safe useful welcome behavior without over-trusting identity.
- Prerequisites: door/contact + motion + person-arrival signal; optional identity confidence signal.
- Trigger: entry motion near recent door open and arrival context.
- Conditions: not sleep mode, home state transition context.
- Action: neutral arrival path first; personal scene only when corroborated and fresh.
- Override: manual scene selection wins.
- Fallback: stale/uncertain identity always neutral.
- Status: **Proposed** (example in `examples/arrival_personal_scene_example.yaml`).

## 4) Device health watchdog
- Purpose: reduce silent failures.
- Prerequisites: battery/offline sensors for key devices.
- Trigger: low battery/offline for >X minutes.
- Conditions: dedupe/cooldown window.
- Action: actionable notification + dashboard summary entity.
- Override: maintenance mode suppresses repeated alerts.
- Fallback: daily digest if push channel unavailable.
- Status: **Proposed**.

## 5) Kitchen inventory event model
- Purpose: durable stock tracking (IN/OUT/OPEN/SPOILED) with scan UX.
- Prerequisites: Grocy/alternative inventory backend, scan entry point, correction flow.
- Trigger: barcode/manual scan events.
- Conditions: duplicate-scan and debounce safeguards.
- Action: log operation + quick feedback + undo window.
- Override: manual correction pipeline.
- Fallback: unresolved UPC routes to pending-review list.
- Status: **Proposed**.
