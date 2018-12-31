@echo off

tasklist /nh /fi "imagename eq Ets2Telemetry.exe" | find /i "Ets2Telemetry.exe" >nul && (
@echo off
) || (
start "" %~dp0server\Ets2Telemetry.exe
)
start "Python" %~dp0python\app.py
