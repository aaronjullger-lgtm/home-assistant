# Household inventory (sanitized)

Evidence date: 2026-10-19

Status legend:
- **Reported**: directly reported by household owner
- **Earlier record**: historical/previous inventory source; not yet re-verified
- **Unknown**: ownership/setup/integration/availability not yet verified

| Device / Service | Model (known/unknown) | Area | Protocol | Power | Integration | Capabilities / entities | Ownership | Installation | Integration status | Availability | Evidence | Open questions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Home Assistant host | Home Assistant Green (earlier record) | Infra | LAN | Mains | Home Assistant OS | Core orchestration | Earlier record | Unknown | Unknown | Unknown | Earlier records (2026-10 context) | Confirm host is still Green and active version |
| Voice assistant | Home Assistant Voice Preview Edition | Unknown | LAN/Wi-Fi | USB/Mains | Home Assistant voice pipeline | Voice commands, timers, announcements | Reported | Unknown | Unknown | Unknown | Direct report (2026-10) | Confirm area placement, wake performance, quiet-hours behavior |
| Zigbee connector | SONOFF Zigbee connector (exact model unknown) | Unknown | Zigbee/USB/Ethernet (unknown) | Unknown | ZHA/Zigbee2MQTT (unknown) | Zigbee network bridge | Reported tentative | Unknown | Unknown | Unknown | Direct report: recently acquired | Confirm model, firmware, and adopted stack |
| Cameras | Ring cameras | Entry/exterior (unknown) | Cloud/LAN mix | Mains/Battery (unknown) | Ring integration | Motion/events/video | Reported | Unknown | Unknown | Unknown | Direct report | Which cameras are critical coverage, doorbell requirements, retention needs |
| Lighting | Govee lights (extensive) | Multi-room | Wi-Fi/BLE (unknown) | Mixed | Govee integration (unknown) | Scene/brightness/color | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm mapped entities, latency, local/cloud dependency |
| Motion sensors | Govee H5121 + other presence sensor | Multi-room | Unknown | Battery (likely) | Unknown | Motion/presence | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm IDs, battery status, false-positive areas |
| Temp/humidity sensors | Unknown models | Multi-room | Unknown | Battery | Unknown | Temperature/humidity | Earlier record | Unknown | Unknown | Unknown | Earlier records | Which rooms support comfort automations now |
| Contact sensors | Unknown models | Doors/windows (unknown) | Unknown | Battery | Unknown | Open/close | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm key ingress points and reliability |
| Smart plugs | Kasa models unknown | Various | Wi-Fi | Mains | TP-Link/Kasa | On/off, maybe energy | Earlier record | Unknown | Unknown | Unknown | Earlier records | Which models expose power/energy metrics |
| Thermostat | ecobee Premium (earlier record) | HVAC | Cloud/LAN | Mains | ecobee integration | Climate, occupancy proxy | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm active integration and setpoint ownership model |
| Lock | Philips-branded smart lock (model unknown) | Entry | Unknown | Battery | Unknown | Lock/unlock/status | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm secure integration path and event fidelity |
| Voice/display ecosystem | Echo, Hatch, Skylight/other displays | Multi-room | Wi-Fi | Mains | Various | Alerts/ambient displays | Earlier record | Unknown | Unknown | Unknown | Earlier records | Which are currently useful for HA outputs |
| Desk controls | Stream Deck+ + pedal | Office | USB | USB | Companion app / HA integration (unknown) | Manual scene/control buttons | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm host and profiles |
| Diffusers/warmers | Pura + candle warmers | Various | Unknown | Mains | Unknown | Scent/comfort routines | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm safe control policy and occupancy constraints |
| Robot vacuum | Dreame (backlog) | Floors | Wi-Fi | Battery/dock | Dreame integration (unknown) | Cleaning maps/tasks | Earlier record | Unknown | Unknown | Unknown | Earlier records | Confirm if operational or still backlog |
| Compute candidates | Existing desktops | Office/utility | LAN | Mains | Frigate/AI hosts (proposal) | Camera/AI workloads | Earlier record | Unknown | Unknown | Unknown | Earlier records | Capture CPU/GPU/storage/power profiles |

## Private detail handling

- Keep sanitized table here for version control.
- Put sensitive/private network, account, and exact room mapping details in `docs/inventory.private.md` (gitignored).
