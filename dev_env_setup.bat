@REM cd into package directory
cd C:\git\fp_data_toolbox

@REM activating virtual environment
venv\scripts\activate

@REM pulling "pip install" of python packages
pip install git+https://github.com/fredapires/fp_data_toolbox.git --upgrade

@REM deactivating virtual environment
@REM deactivate

PAUSE