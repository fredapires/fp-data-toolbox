import os
from fp_data_toolbox import package_handling

# %% 

# input_url='https://github.com/fredapires/fp_data_toolbox'
# package_handling.pip_install_from_github_url(input_url)

# input_url='https://github.com/fredapires/mtg-proj'
# package_handling.pip_install_from_github_url(input_url)


# %% 
### dev_env setup
###=============================================

# cd into package directory
# activating virtual environment
# os.system(
#     "cd C:\git\fp_data_toolbox;"+
#     "venv\scripts\activate"
#     )


# test
os.system(
    'cd C:\\git\\fp_data_toolbox-proj; '+
    'dev_env_setup.bat'
    )

# %% 
# pulling "pip install" of python packages
# os.system(
#     'FOR %x IN (*.bat) DO call "%x";'+
#     'PAUSE'
#     )

# %% 
# cd into package directory
# os.system(
#     "cd C:\git\fp_data_toolbox\;"+
#     "venv\scripts\activate"
#     )
