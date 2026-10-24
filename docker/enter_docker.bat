@echo off
REM Check if container is already running
docker ps -q -f "name=apex_autonomous_env" -f "status=running" > "%TEMP%\docker_check.tmp"
set /p RUNNING=<"%TEMP%\docker_check.tmp"
del "%TEMP%\docker_check.tmp" >nul 2>&1

if "%RUNNING%"=="" (
    echo [ERROR] Container 'apex_autonomous_env' is not running.
    echo Please start the container first using 'run_docker.bat'.
    pause
    exit /b 1
)

echo Connecting new terminal to 'apex_autonomous_env'...
docker exec -it apex_autonomous_env bash
