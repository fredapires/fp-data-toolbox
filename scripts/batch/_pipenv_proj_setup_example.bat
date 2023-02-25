@REM example_pipenv project setup
@echo off

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

@REM this is where we will install dependencies into the .venv directory
pipenv install git+https://github.com/fredapires/fp_data_toolbox




@REM this is where we will install dependencies into the .venv directory
git+https://github.com/fredapires/fp_data_toolbox



pause

@REM pipenv install git+https://github.com/fredapires/fp_data_toolbox

@REM pip install mtg proj
@REM pip install git+https://github.com/fredapires/mtg-proj

@REM activate venv
@REM venv\scripts\activate

@REM execute main python script
@REM python C:\git\fp_data_toolbox-proj\scripts\python\_master_script.py %*

pause