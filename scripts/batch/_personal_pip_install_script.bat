@REM project cd
cd C:\git\fp_data_toolbox-proj

@REM pip install main toolbox repo
pip install git+https://github.com/fredapires/fp_data_toolbox

@REM pip install mtg proj
pip install git+https://github.com/fredapires/mtg-proj

@REM activate venv
@REM venv\scripts\activate

@REM execute main python script
@REM python C:\git\fp_data_toolbox-proj\scripts\python\_master_script.py %*



pipenv install git+https://github.com/fredapires/fp_data_toolbox#egg=fp_data_toolbox

pause