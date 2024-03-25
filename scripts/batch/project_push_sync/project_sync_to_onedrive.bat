@echo off
setlocal

rem Load variables from .env file
for /f "delims=" %%a in ('type .env') do (
    set "%%a"
)
@REM echo PROJECT_PATH is %PROJECT_PATH%

SET _SRC="C:\fp-pkm\git-repos\fp-data-toolbox"
SET _DST="C:\Users\Fred\OneDrive\git_repos\fp-data-toolbox-proj"

:: add more folders to exclude here
SET _xd=.git
SET _xd=%_xd% .vscode
SET _xd=%_xd% .venv
SET _xd=%_xd% dist
SET _xd=%_xd% data
SET _xd=%_xd% node_modules

:: add more files to exclude here
SET _xf=.env
SET _xf=%_xf% .gitattributes
SET _xf=%_xf% poetry.lock

:: set options
SET _OPTION=/MIR /XD %_xd% /XF %_xf% 
::/LOG:%_LOG%
:: execute  robocopy
ROBOCOPY %_SRC% %_DST% %_OPTION%
