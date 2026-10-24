#!/usr/bin/env bash
set -e

# Enable local X11 forwarding for GUI (Gazebo, RViz, rqt_graph)
xhost +local:root 2>/dev/null || true

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "========================================================"
echo "Starting APEX Autonomous Systems Docker (ROS 2 Jazzy)..."
echo "========================================================"
docker compose build
docker compose up -d

echo "Container 'apex_autonomous_env' is running!"
echo "Entering container shell..."
docker compose exec autonomous_lp bash
