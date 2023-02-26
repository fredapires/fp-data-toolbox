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

    print('')

    df = pd.DataFrame()
    df = file_handling.read_excel_to_dataframe(
        workbook_path=excel_path,
        sheet_name=sheet_name,
    )
    print('Succesfully loaded excel data sheet to Pandas dataframe.')
    print('')

    # general data cleaning/prep operations here
    # print('Starting data cleaning operations...')

    # print('Done with data cleaning operations.')
    print('')

    # various profiling report output types here
    # [ ] ydata_profiling
    # [ ] with config
    # [x] minimal
    # [ ] missingno matrix
    # [ ] dataprep

    print('Starting to build data profiling reports.')
    print('')

    if data_profile_type == 'ydata':
        print('Starting ydata_profiling report. May take a few minutes...')
        print('')
        from ydata_profiling import ProfileReport
        profile = ProfileReport(df, minimal=True)

        # save to excel_parent_directory
        profile.to_file(excel_parent_directory+'\\ydata_profiling_report.html')
        print('')
        print('Done building ydata_profiling report to ' +
              excel_parent_directory + '  '+'Thanks!')
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
