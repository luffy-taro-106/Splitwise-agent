#!/usr/bin/env bash
set -e

# ---- paths ----
FRONT_DIR="splitwise-chat"
BACK_MAIN="backend:app"       # FastAPI app lives in backend.py
BACK_PORT=8000

echo "Starting frontend …"
(cd "$FRONT_DIR" && npm start) &
FRONT_PID=$!

echo "Starting backend …"
uvicorn "$BACK_MAIN" --reload --port $BACK_PORT --host 0.0.0.0 &
BACK_PID=$!

# Ensure both are terminated on script exit (Ctrl-C)
cleanup() {
  echo "Stopping servers …"
  kill $FRONT_PID $BACK_PID 2>/dev/null || true
  exit 0
}

trap cleanup SIGINT SIGTERM

# Wait on background jobs
wait $BACK_PID

# chmod +x run_app.sh   # only once
# ./run_app.sh