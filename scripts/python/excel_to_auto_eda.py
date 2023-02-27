# Excel -> eda script
# %% Imports
import os
import sys
import pandas as pd
#
import fp_data_toolbox as fpdt
from fp_data_toolbox import eda
from fp_data_toolbox import file_handling


# ---------------------------------
# %%
excel_path_input = sys.argv[1]
sheet_name_input = sys.argv[2]
# excel_path_input = 'C:\\temp\\test_data_wkbk.xlsm'
# sheet_name_input = 'TEST DATA'


# ---------------------------------
# Converting "ON","OFF" strings to boolean
toggle_general = sys.argv[3] == 'ON'
toggle_ydata = sys.argv[4] == 'ON'
toggle_dataprep = sys.argv[5] == 'ON'
toggle_missingno = sys.argv[6] == 'ON'


# %%
# eda.excel_to_eda_tools(
eda.excel_auto_eda_run(
    excel_path=excel_path_input,
    sheet_name=sheet_name_input,
    toggle_general=toggle_general,
    toggle_ydata=toggle_ydata,
    toggle_dataprep=toggle_dataprep,
    toggle_missingno=toggle_missingno,
)

# %%
