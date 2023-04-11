::@echo off
set "source_dir=C:\git\fp-data-toolbox-proj"

::--- ======================================================
@echo off
set "file_name=.env"

:: copying pipfile to data validation project
set "destination_dir=C:\git\fp-ds-proj-template"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"

:: copying pipfile to dom trans project
set "destination_dir=C:\git\mtg-proj"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"

:: copying pipfile to intl str lnd project
set "destination_dir=C:\git\personal-proj"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"


::--- ======================================================

set "file_name=.gitignore"

:: copying pipfile to data validation project
set "destination_dir=C:\git\fp-ds-proj-template"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"

:: copying pipfile to dom trans project
set "destination_dir=C:\git\mtg-proj"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"

:: copying pipfile to intl str lnd project
set "destination_dir=C:\git\personal-proj"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"


::--- ======================================================

set "file_name=Pipfile"

:: copying pipfile to data validation project
set "destination_dir=C:\git\fp-ds-proj-template"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"

:: copying pipfile to dom trans project
set "destination_dir=C:\git\mtg-proj"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"

:: copying pipfile to intl str lnd project
set "destination_dir=C:\git\personal-proj"
xcopy /Y /F "%source_dir%\%file_name%" "%destination_dir%\%file_name%"



::--- ======================================================


pause