SET _SRC="C:\source_directory"
SET _DST="C:\destination_directory"
SET _LOG="C:\destination_directory\robocopy_log.log"
::
SET _xd=.git
SET _xd=%_xd% .vscode
SET _xd=%_xd% .venv
SET _xd=%_xd% node_modules

:: add more files to exclude here
SET _xf=.env
SET _xf=%_xf% .gitattributes

:: set options
SET _OPTION=/MIR /XD %_xd% /XF %_xf% 
::/LOG:%_LOG%
:: execute  robocopy
ROBOCOPY %_SRC% %_DST% %_OPTION%
