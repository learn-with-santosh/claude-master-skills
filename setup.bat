@echo off
echo 🚀 Running Claude Master Skills Installer...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed or not in PATH.
    pause
    exit /b
)

python setup.py %*
pause
