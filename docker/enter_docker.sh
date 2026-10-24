#!/usr/bin/env bash
set -e

# Check if container is running
if ! docker ps --format '{{.Names}}' | grep -q "^apex_autonomous_env$"; then
    echo "[ERROR] Container 'apex_autonomous_env' is not running."
    echo "Please start the container first using './run_docker.sh'."
    exit 1
fi

echo "Connecting new terminal to 'apex_autonomous_env'..."
docker exec -it apex_autonomous_env bash
