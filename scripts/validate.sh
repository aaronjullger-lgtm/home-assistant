#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

echo "[1/2] YAML lint"
if command -v yamllint >/dev/null 2>&1; then
  yamllint -c .yamllint .
else
  echo "yamllint not installed; skipping lint step"
fi

echo "[2/2] Home Assistant config check"
if command -v hass >/dev/null 2>&1; then
  hass --script check_config --config "$repo_root/config"
else
  echo "hass not installed; skipping Home Assistant check_config"
fi
