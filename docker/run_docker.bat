@echo off
echo Starting APEX Autonomous Systems Docker Container...
cd /d "%~dp0"
docker compose build
docker compose up -d
echo Entering container shell...
docker compose exec autonomous_lp bash
