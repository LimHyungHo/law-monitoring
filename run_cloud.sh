#!/bin/bash
set -eu

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="${VENV_DIR:-$PROJECT_DIR/.venv}"
APP_MODE="${1:-web}"
PORT_VALUE="${PORT:-5000}"

if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
fi

. "$VENV_DIR/bin/activate"
pip install -r "$PROJECT_DIR/requirements.txt"

export WEB_HOST="${WEB_HOST:-0.0.0.0}"
export WEB_PORT="${WEB_PORT:-$PORT_VALUE}"
export WEB_DEBUG="${WEB_DEBUG:-false}"
export LAW_MONITOR_DATA_DIR="${LAW_MONITOR_DATA_DIR:-/tmp/law-monitoring-data}"
export DB_PATH="${DB_PATH:-$LAW_MONITOR_DATA_DIR/law_monitor.db}"
export PDF_OUTPUT_DIR="${PDF_OUTPUT_DIR:-$LAW_MONITOR_DATA_DIR/pdf}"
export LAW_ID_CACHE_PATH="${LAW_ID_CACHE_PATH:-$LAW_MONITOR_DATA_DIR/cache/law_ids.json}"
export LOG_LEVEL="${LOG_LEVEL:-INFO}"

mkdir -p "$LAW_MONITOR_DATA_DIR" "$PDF_OUTPUT_DIR" "$(dirname "$LAW_ID_CACHE_PATH")"

cd "$PROJECT_DIR"
exec python3 main.py "$APP_MODE"
