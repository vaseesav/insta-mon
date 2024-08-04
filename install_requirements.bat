@echo off
rem Script to install all the requirements from the requirements.txt

rem Check if requirements.txt file exists
IF EXIST requirements.txt (
    echo requirements.txt found. Installing requirements...

    rem Upgrade pip to the latest version
    echo Upgrading pip...
    python -m pip install --upgrade pip

    rem Install requirements from requirements.txt
    echo Installing requirements...
    pip install -r requirements.txt

    echo All requirements installed.
) ELSE (
    echo requirements.txt not found. Please make sure the file exists in the current directory.
    exit /b 1
)
