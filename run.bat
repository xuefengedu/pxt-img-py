@echo off
cd %~dp0
Echo go to dir: "%~dp0"
C:\Users\scxsvc\AppData\Local\Programs\Python\Python37\python test.py -i dt.c -o output.txt
pause