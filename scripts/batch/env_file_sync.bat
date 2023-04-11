::--- ======================================================
:: env file sync between python projects
:: keeps env consistent across projects
::--- ======================================================
@echo off

:: setup source for sync
set "source_dir=C:\git\fp_data_toolbox-proj"

:: Set up list of file names
set "file_names=(
    Pipfile 
    .env 
    .gitignore
    )"

:: Set up list of destination projects for sync
set "destination_dirs=(
    C:\git\personal-proj
    C:\git\fp-ds-proj-template
    C:\git\mtg-proj
    C:\git\music-prod
    )"

:: Loop through each destination directory
for %%D in %destination_dirs% do (
    :: Loop through each file name
    for %%F in %file_names% do (
        xcopy /Y /F "%source_dir%\%%F" "%%D\%%F"
    )
)

::--- ======================================================