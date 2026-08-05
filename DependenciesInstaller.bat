@echo off
title BobsAI Dependencies Installer V1
color 07

echo.
echo /////////////////////////////
echo   <DependenciesInstallerV1>
echo \\\\\\\\\\\\\\\\\\\\\\\\\\\\\
echo.

timeout /t 2 >nul


echo Step 1: Checking for Python...
echo.


python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo Python not found, or not installed!
    echo.
    echo Please install Python from:
    echo https://python.org
    echo.
    echo Recommended versions:
    echo Python 3.12 or Python 3.13+
    echo.

    set /p openpython="Do you want to open the Python website? Y/N: "

    if /i "%openpython%"=="Y" (
        start https://python.org

        echo.
        echo Waiting 15 seconds...
        timeout /t 15 >nul

        set /p rescan="Have you installed Python? Would you like to rescan? Y/N: "

        if /i "%rescan%"=="Y" (
            goto CHECKPYTHON
        )

        echo.
        echo Closing...
        pause
        exit
    )

    echo.
    echo Closing...
    pause
    exit
)


:CHECKPYTHON

python --version >temp_python.txt

set /p PYVERSION=<temp_python.txt

del temp_python.txt


echo Python found! %PYVERSION% installed.
echo.


echo Checking llama-cpp-python PIP...
echo.


python -m pip show llama-cpp-python >nul 2>&1


if %errorlevel%==0 (
    echo llama-cpp-python detected!
    echo.
    echo You have all requirements installed!
    echo.
    echo Press any key to close...
    pause >nul
    exit
)


echo llama-cpp-python not installed!
echo.

set /p installcpp="This dependency can be installed now. Continue? Y/N: "


if /i "%installcpp%" neq "Y" (
    echo.
    echo Installation cancelled.
    echo.
    echo Press any key to close...
    pause >nul
    exit
)


echo.
echo Installing llama-cpp-python PIP...
echo.


python -m pip install llama-cpp-python


if %errorlevel% neq 0 (
    echo.
    echo Failed to install llama-cpp-python :(
    echo.
    echo Ensure you have:
    echo - Python from python.org
    echo - Not the Microsoft Store version
    echo.
    echo Troubleshoot using the error above.
    echo.
    echo Press any key to close...
    pause >nul
    exit
)


echo.
echo All dependencies installed!
echo Run start.bat to start BobsAI!
echo.

echo Press any key to close...
pause >nul