@echo off
chcp 65001 >nul
echo ═══════════════════════════════════════════════════
echo   δ-me13 Scepter Simulation - 网页版启动器
echo ═══════════════════════════════════════════════════
echo.

cd /d "%~dp0frontend"

echo [1/2] 检查依赖...
if not exist "node_modules" (
    echo 正在安装依赖，请稍候...
    call npm install
)

echo [2/2] 启动开发服务器...
echo.
echo 服务器启动后，请在浏览器打开: http://localhost:5173/
echo 按 Ctrl+C 停止服务器
echo.

npm run dev
