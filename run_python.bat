@echo off
echo Running δme-13.exe simulation...
echo.

REM 獲取bat檔所在目錄
set "SCRIPT_DIR=%~dp0"
set "PYTHON_SCRIPT=%SCRIPT_DIR%delta_me13_sim.py"

REM 嘗試不同的Python路徑
if exist "C:\Program Files\JetBrains\JetBrains Rider 2025.1.4\plugins\cidr-debugger-plugin\bin\lldb\win\x64\bin\python.exe" (
    echo 使用 JetBrains Rider Python...
    "C:\Program Files\JetBrains\JetBrains Rider 2025.1.4\plugins\cidr-debugger-plugin\bin\lldb\win\x64\bin\python.exe" "%PYTHON_SCRIPT%"
    goto :end
)

REM 嘗試系統PATH中的Python
python "%PYTHON_SCRIPT%" 2>nul
if %errorlevel% equ 0 goto :end

py "%PYTHON_SCRIPT%" 2>nul
if %errorlevel% equ 0 goto :end

python3 "%PYTHON_SCRIPT%" 2>nul
if %errorlevel% equ 0 goto :end

echo.
echo 錯誤：未找到 Python 解釋器
echo ==========================
echo 請確保：
echo 1. Python 已安裝並添加到 PATH
echo 2. 或 JetBrains Rider 已安裝
echo 3. delta_me13_sim.py 文件在同一目錄
echo.
pause
exit /b 1

:end
echo.
echo Simulation completed.
pause
