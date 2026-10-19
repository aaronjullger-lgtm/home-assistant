# Operations and rollout

## Validation workflow
1. Run `bash scripts/validate.sh`.
2. Resolve lint/config issues.
3. Merge only after CI validation passes.

## Staged activation process
1. Backup current Home Assistant config.
2. Add `config/` files in a non-destructive branch.
3. Run HA configuration check with synthetic secrets.
4. Activate only one slice at a time; observe behavior in logs/history.
5. Roll back by disabling package include or restoring backup if needed.

## Rollback
- Remove/disable the specific package file.
- Restore prior known-good backup.
- Re-run configuration check before restart.
