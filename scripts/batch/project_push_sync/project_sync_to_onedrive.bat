SET _SRC="C:\git\fp-data-toolbox-proj"
SET _DST="C:\Users\Fred\OneDrive\git_repos\fp-data-toolbox-proj"

:: add more folders to exclude here
SET _xd=.git
SET _xd=%_xd% .vscode
SET _xd=%_xd% .venv
SET _xd=%_xd% data
SET _xd=%_xd% node_modules

:: add more files to exclude here
SET _xf=.env
SET _xf=%_xf% .gitattributes

:: set options
SET _OPTION=/MIR /XD %_xd% /XF %_xf% 
::/LOG:%_LOG%
:: execute  robocopy
ROBOCOPY %_SRC% %_DST% %_OPTION%
