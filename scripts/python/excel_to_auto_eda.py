# Excel -> eda script
# %% Imports
import os
import sys
import pandas as pd
#
import fp_data_toolbox as fpdt
from fp_data_toolbox import eda
from fp_data_toolbox import file_handling

# %%
excel_path_input = sys.argv[1]
sheet_name_input = sys.argv[2]
# excel_path_input = 'C:\\temp\\test_data_wkbk.xlsm'
# sheet_name_input = 'TEST DATA'
# Converting "ON","OFF" strings to boolean
ydata_toggle = sys.argv[3] == 'ON'
dataprep_toggle = sys.argv[4] == 'ON'
missingno_toggle = sys.argv[5] == 'ON'

# %% define functions


def excel_to_eda_tools(
    excel_path,
    sheet_name,
    ydata_toggle=True,
    dataprep_toggle=True,
    missingno_toggle=True,
):

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

    if ydata_toggle == True:
        print('Starting ydata_profiling report. May take a few minutes...')
        print('')
        from ydata_profiling import ProfileReport
        profile = ProfileReport(df, minimal=True)

        # save to excel_parent_directory
        profile.to_file(excel_parent_directory+'\\' +
                        sheet_name+'-'+'ydata_report.html')

        print('')
        print('Done building ydata_profiling report to ' +
              excel_parent_directory + '  '+'Thanks!')
    elif dataprep_toggle == True:
        print('Starting dataprep report. May take a few minutes...')
        print('')
        from dataprep.eda import plot, plot_correlation, plot_missing
        from dataprep.eda import create_report
        report = create_report(df)
        report  # show report in notebook
        # save report to local disk
        report.save(excel_parent_directory+'\\' +
                    sheet_name+'-'+'dataprep_report.html')
        report.show_browser()  # show report in the browser

        print('')
        print('Done building dataprep report to ' +
              excel_parent_directory + '  '+'Thanks!')
    elif missingno_toggle == True:
        print('Starting missingno report. May take a few minutes...')
        print('')
        print('')
        print('Done building missingno report to ' +
              excel_parent_directory + '  '+'Thanks!')
    else:
        print('Done building all data profiling reports')


# %%
# eda.excel_to_eda_tools(
excel_to_eda_tools(
    excel_path=excel_path_input,
    sheet_name=sheet_name_input,
    ydata_toggle=ydata_toggle,
    dataprep_toggle=dataprep_toggle,
    missingno_toggle=missingno_toggle,
)

# %%
