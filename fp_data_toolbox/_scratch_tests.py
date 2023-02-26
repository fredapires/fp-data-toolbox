# %%
import sys
import pandas as pd

import fp_data_toolbox as fpdt
from fp_data_toolbox import eda

# %%

excel_path_input = sys.argv[1]
sheet_name_input = sys.argv[2]

# %%
# excel_path_input = 'C:\\temp\\test_data_wkbk.xlsm'
# sheet_name_input = 'TEST DATA'

eda.excel_to_eda_tools(
    excel_path=excel_path_input,
    sheet_name=sheet_name_input,
)

# %%
