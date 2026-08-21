@echo off
echo ============================================
echo   Plant AI - Local Setup
echo ============================================

REM Check if virtual environment exists, create if not
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

REM Check if .env has been configured
findstr /C:"your_vertex_ai_api_key_here" .env >nul 2>&1
if %errorlevel%==0 (
    echo.
    echo WARNING: Please edit the .env file and add your API key before running!
    echo   GEMINI_API_KEY  - Get a Vertex AI key at: https://aistudio.google.com/app/apikey
    echo.
    pause
    exit /b
)

echo.
echo Starting Plant AI on http://localhost:5000
echo Press Ctrl+C to stop.
echo.
python main.py
pause
