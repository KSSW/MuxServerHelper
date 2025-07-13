@echo off
cd /d %~dp0

:: Persian lessons https://easypersian.com/
set PERSIA=1
set /p user_args=Command args(Don't add py):

echo Running: Main_arg.py %user_args%
echo --------------------------------------------------------------------------^|
C:\Users\48716\AppData\Local\Programs\Python\Python310\python.exe Main_arg.py %user_args%
echo --------------------------------------------------------------------------^|
echo Execution Completed
pause