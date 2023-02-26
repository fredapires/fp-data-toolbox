# %% Imports
import os
import sys
import pandas as pd
#
import fp_data_toolbox as fpdt
from fp_data_toolbox import eda
from fp_data_toolbox import file_handling


# %% define functions

def excel_to_eda_tools(excel_path, sheet_name, data_profile_type='ydata'):

    excel_parent_directory = os.path.dirname(excel_path)

    df = pd.DataFrame()
    df = file_handling.read_excel_to_dataframe(
        workbook_path=excel_path,
        sheet_name=sheet_name,
    )

    # general data cleaning/prep operations here

    # various profiling report output types here
    # [ ] ydata_profiling
    # [ ] with config
    # [x] minimal
    # [ ] missingno matrix
    # [ ] dataprep
    if data_profile_type == 'ydata':
        from ydata_profiling import ProfileReport
        profile = ProfileReport(df, minimal=True)

        # save to excel_parent_directory
        profile.to_file(excel_parent_directory+'\\ydata_profiling_report.html')
    else:
        print('data_profile_type input invalid')


# %%
excel_path_input = sys.argv[1]
sheet_name_input = sys.argv[2]
# excel_path_input = 'C:\\temp\\test_data_wkbk.xlsm'
# sheet_name_input = 'TEST DATA'

# %%
# eda.excel_to_eda_tools(
excel_to_eda_tools(
    excel_path=excel_path_input,
    sheet_name=sheet_name_input,
)

# %%
