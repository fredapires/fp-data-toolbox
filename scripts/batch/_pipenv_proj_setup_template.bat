@REM example_pipenv project setup
@echo off
pip install pipenv

@REM set project folder here
set "directory=C:\git\fp_data_toolbox-proj"
set "directory_venv=%directory%.venv"

if not exist "%directory%" (
  mkdir "%directory%"
)

if not exist "%directory_venv%" (
  mkdir "%directory_venv%"
)

cd "%directory%"

@REM setup pipenv in global interpreter, for installation
@REM install dependencies into the .venv directory
@REM pipenv install git+https://github.com/fredapires/fp_data_toolbox#egg=fp_data_toolbox
@REM pipenv install git+https://github.com/fredapires/fp_data_toolbox#egg=fp_data_toolbox

@REM activate venv
@REM .venv\scripts\activate

@REM execute master updater python script
@REM python scripts\python\_master_script.py %*

pause