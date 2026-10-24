@echo off
echo ========================================================
echo Starting APEX Autonomous Systems Docker (ROS 2 Jazzy)...
echo ========================================================
cd /d "%~dp0"
docker compose build
docker compose up -d
echo Container 'apex_autonomous_env' is running!
echo Entering container shell...
docker compose exec autonomous_lp bash
