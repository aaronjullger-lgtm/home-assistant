# Key decisions and evidence

## D-001: Start with package-based HA config layout
- Decision: use `homeassistant: packages` in `config/configuration.yaml` and isolate milestone behavior in one package file.
- Why: keeps modular growth manageable and mirrors proven HA config structures.
- Sources:
  - https://github.com/frenck/home-assistant-config/blob/HEAD/configuration.yaml
  - https://www.home-assistant.io/docs/configuration/packages/
- License compatibility: MIT for borrowed structural ideas.

## D-002: Use explicit override + timer recovery patterns
- Decision: pathway automation uses manual override helper and timer-finished recovery guards.
- Why: reduces writer conflicts and protects manual intent.
- Sources:
  - https://github.com/skalavala/mysmarthome/blob/HEAD/packages/motion_timers.yaml
  - https://github.com/avbor/HomeAssistantConfig/blob/HEAD/packages/pack_autoreboot.yaml
  - https://www.home-assistant.io/docs/automation/modes/
- License compatibility: MIT/Unlicense inspirations; implementation rewritten for this repo.

## D-003: Keep unresolved real entities outside active includes
- Decision: put identity/personal scene sketch under `examples/` only.
- Why: avoids breaking active config with unknown devices and preserves safe iteration.
- Sources:
  - Repository requirement: unresolved entities outside active include path.

## D-004: Stage Frigate migration with pilot coverage before Ring retirement
- Decision: maintain Ring while piloting one local IP camera and validating detection/retention/notification.
- Why: coverage continuity and measurable migration risk reduction.
- Sources:
  - https://docs.frigate.video/
  - https://github.com/blakeblackshear/frigate/blob/HEAD/frigate/config/camera/record.py
  - https://github.com/blakeblackshear/frigate/blob/HEAD/frigate/config/camera/detect.py
- License compatibility: Frigate MIT.
