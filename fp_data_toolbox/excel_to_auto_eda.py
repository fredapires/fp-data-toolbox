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


def excel_auto_eda_run(
    excel_path,
    sheet_name,
    toggle_general=True,
    toggle_ydata=True,
    toggle_dataprep=True,
    toggle_missingno=True,
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
    # [x] ydata_profiling
    # [ ] with config
    # [x] minimal
    # [x] missingno matrix
    # [x] dataprep

    print('')
    print('###==========================================================================================')
    print('###==========================================================================================')
    print('Starting to build data profiling reports.')
    print('###==========================================================================================')
    print('###==========================================================================================')
    print('')
    print('')

    # creating target directory + saving variable
    tgt_directory = excel_parent_directory+'\\'+sheet_name+'-data_profiling'
    if os.path.exists(tgt_directory):
        print(f"Directory {tgt_directory} already exists.")
    else:
        try:
            os.makedirs(tgt_directory)
            print(f"Directory {tgt_directory} created.")
        except OSError as e:
            raise OSError(
                f"Error creating directory {tgt_directory}: {str(e)}")

    if toggle_general == True:
        print('')
        print('###==========================================================================================')
        print('Starting general data profiling report. May take a few seconds...')
        print('###==========================================================================================')
        print('')

        # TODO: fill out this section :noted_on:2023-02-26
        # [ ] test

        general_report_out_path = tgt_directory+'\\'+sheet_name+'-general-report.xlsx'
        eda.df_info_to_excel(
            df=df,
            filepath=general_report_out_path,
            sheet_name=sheet_name+'-eda_info',
        )

        print('')
        print('Done building general data profiling report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')
    if toggle_ydata == True:
        print('')
        print('###==========================================================================================')
        print('Starting ydata_profiling report. May take a few minutes...')
        print('###==========================================================================================')
        print('')
        from ydata_profiling import ProfileReport
        profile = ProfileReport(df, minimal=True)

        # save to excel_parent_directory
        profile.to_file(tgt_directory+'\\' +
                        'ydata_report-'+sheet_name+'.html')

        print('')
        print('Done building ydata_profiling report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')
    if toggle_dataprep == True:
        print('')
        print('###==========================================================================================')
        print('Starting dataprep report. May take a few minutes...')
        print('###==========================================================================================')
        print('')

        from dataprep.eda import plot, plot_correlation, plot_missing
        from dataprep.eda import create_report
        report = create_report(df)
        report  # show report in notebook
        # save report to local disk
        report.save(tgt_directory+'\\' +
                    'dataprep_report-'+sheet_name+'.html')
        # report.show_browser()  # show report in the browser

        print('')
        print('Done building dataprep report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')
    if toggle_missingno == True:
        print('')
        print('###==========================================================================================')
        print('Starting missingno report. May take a few minutes...')
        print('###==========================================================================================')
        print('')

        # DONE: fill out this section :noted_on:2023-02-26
        #   [x] generate missingno report / visualization
        #   [x] save in excel_parent_directory
        eda.msno_eda_save_pngs(
            df,
            tgt_directory=tgt_directory,
            df_name=sheet_name,
        )

        print('')
        print('Done building missingno report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')

    print('Done building all data profiling reports')


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
excel_auto_eda_run(
    # eda.excel_to_eda_tools(
    excel_path=excel_path_input,
    sheet_name=sheet_name_input,
    toggle_general=toggle_general,
    toggle_ydata=toggle_ydata,
    toggle_dataprep=toggle_dataprep,
    toggle_missingno=toggle_missingno,
)

# %%
