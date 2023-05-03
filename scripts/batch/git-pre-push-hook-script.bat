@REM cd into package directory
@echo off

@REM echo This is the git-pre-push-hook-script running.
call .\scripts\batch\project_push_sync\project_sync_to_onedrive.bat

pause