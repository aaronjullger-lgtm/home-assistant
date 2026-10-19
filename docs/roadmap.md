# Roadmap (next slices)

## Slice A (next): map synthetic pathway to first real entry route
- Existing hardware likely usable now: one motion/contact pair + one controllable light group.
- Missing to verify: actual entity IDs, mode helpers, occupant constraints.
- Effort: low-medium (entity mapping + live observation).
- Maintenance: low once override durations and cooldowns are tuned.
- Why worth it: immediate daily value and safer nighttime navigation.

## Slice B: humidity ventilation + shower retention
- Existing hardware likely usable now: humidity sensor(s), bathroom fan switch, bathroom light control.
- Missing to verify: sensor update rates and fan control reliability.
- Effort: medium (hysteresis/rate tuning).
- Maintenance: medium seasonal tuning.
- Why worth it: comfort and moisture control with minimal interaction.

## Staged tracks

### Frigate
1. Identify one pilot camera position and host candidate.
2. Validate day/night detection, retention, and notifications.
3. Keep Ring active until replacement coverage is proven.

### Voice
1. Measure current Voice Preview Edition placement quality.
2. Add area-aware timer/announcement intents.
3. Build coverage plan for additional satellites only after observed gaps.

### Kitchen
1. Select inventory source of truth (Grocy candidate).
2. Define scan event model (IN/OUT/OPEN/SPOILED + undo).
3. Add meal-planning suggestions only after reliable stock updates.
