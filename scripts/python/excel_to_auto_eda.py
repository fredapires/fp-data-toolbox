# Excel -> eda script
# %% Imports
import os
import sys
import pandas as pd
#
import fp_data_toolbox as fpdt
from fp_data_toolbox import eda
from fp_data_toolbox import file_handling


# %% define functions


def msno_eda_save_pngs(
    df,
    tgt_directory,
    df_name='df',
):
    import missingno as msno

    # creating target directory + saving variable
    # tgt_msno_directory = tgt_directory+'\\'+'msno_report-'+df_name
    # if os.path.exists(tgt_msno_directory):
    #     print(f"Directory {tgt_msno_directory} already exists.")
    # else:
    #     try:
    #         os.makedirs(tgt_msno_directory)
    #         print(f"Directory {tgt_msno_directory} created.")
    #     except OSError as e:
    #         raise OSError(
    #             f"Error creating directory {tgt_msno_directory}: {str(e)}")

    # saving matrix figures
    fig_matrix = msno.matrix(df)
    fig_matrix = fig_matrix.get_figure()
    fig_matrix.savefig(
        tgt_directory+'\\'+'msno_matrix-'+df_name+'.png',
        bbox_inches='tight'
    )

    # saving heatmap figures
    fig_heatmap = msno.heatmap(df)
    fig_heatmap = fig_heatmap.get_figure()
    fig_heatmap.savefig(
        tgt_directory+'\\'+'msno_heatmap-'+df_name+'.png',
        bbox_inches='tight'
    )


# %% excel_auto_eda_run orchestration function


def excel_auto_eda_run(
    excel_path,
    sheet_name,
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

    print('Starting to build data profiling reports.')
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

    if toggle_ydata == True:
        print('###---------------------------------')
        print('Starting ydata_profiling report. May take a few minutes...')
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
        print('###---------------------------------')
        print('Starting dataprep report. May take a few minutes...')
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
        print('###---------------------------------')
        print('Starting missingno report. May take a few minutes...')
        print('')
        import missingno as msno
        # TODO: fill out this section :noted_on:2023-02-26
        #   [ ] generate missingno report / visualization
        #   [ ] save in excel_parent_directory

        msno_eda_save_pngs(
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
# ---------------------------------
# ---------------------------------
# %%
excel_path_input = sys.argv[1]
sheet_name_input = sys.argv[2]
# excel_path_input = 'C:\\temp\\test_data_wkbk.xlsm'
# sheet_name_input = 'TEST DATA'
# Converting "ON","OFF" strings to boolean
toggle_ydata = sys.argv[3] == 'ON'
toggle_dataprep = sys.argv[4] == 'ON'
toggle_missingno = sys.argv[5] == 'ON'

# %%
# eda.excel_to_eda_tools(
excel_auto_eda_run(
    excel_path=excel_path_input,
    sheet_name=sheet_name_input,
    toggle_ydata=toggle_ydata,
    toggle_dataprep=toggle_dataprep,
    toggle_missingno=toggle_missingno,
)

# %%
