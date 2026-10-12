#!/usr/bin/env bash
set -e

# Enable local X11 forwarding for GUI (Gazebo, RViz)
xhost +local:root || true

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Building / Starting APEX Autonomous Systems Docker Container..."
docker compose build
docker compose up -d

echo "Entering container shell..."
docker compose exec autonomous_lp bash
