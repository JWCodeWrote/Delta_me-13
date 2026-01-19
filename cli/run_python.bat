@echo off
chcp 65001 >nul
echo ═══════════════════════════════════════════════════
echo   δ-me13 Scepter Simulation - 命令行版启动器
echo ═══════════════════════════════════════════════════
echo.

cd /d "%~dp0"

python delta_me13_sim.py

echo.
pause
