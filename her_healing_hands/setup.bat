@echo off
echo ========================================
echo Her Healing Hands - Setup Script
echo ========================================
echo.

echo [1/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    echo Make sure Python 3.10+ is installed
    pause
    exit /b 1
)
echo Virtual environment created successfully!
echo.

echo [2/5] Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo Virtual environment activated!
echo.

echo [3/5] Upgrading pip...
python -m pip install --upgrade pip
echo.

echo [4/5] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

echo [5/5] Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created from template
) else (
    echo .env file already exists, skipping...
)
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo NEXT STEPS:
echo.
echo 1. Edit .env file and add your OpenAI API key:
echo    OPENAI_API_KEY=sk-your-key-here
echo.
echo 2. Validate your setup:
echo    python validate_setup.py
echo.
echo 3. Run the application:
echo    streamlit run app.py
echo.
echo NOTE: Virtual environment is still active (venv)
echo To deactivate later, type: deactivate
echo.
pause
