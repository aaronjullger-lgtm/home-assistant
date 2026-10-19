# Agent working rules

- Preserve existing working configuration; keep edits minimal and reversible.
- Do not invent entity IDs, room names, hardware capabilities, addresses, or occupancy claims.
- Treat inventory claims as evidence-backed; mark unknowns explicitly.
- Keep examples with unresolved entities under `examples/`, outside active includes.
- Never commit secrets, `.storage`, recordings, or private history.
- Validate with `bash scripts/validate.sh` and report exact command outcomes.
- Repository work only: no live deployment, purchases, or destructive migrations.
