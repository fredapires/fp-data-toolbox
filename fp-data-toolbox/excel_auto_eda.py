# Excel -> eda script
# %% Imports
import os
import sys
import pandas as pd
import numpy as np
# import polars as pl
#
# from scf_data_mgmt import eda


# %%


def convert_columns(df):
    for col in df.columns:
        # ---------------------------------
        if 'SNSH_YR_WK' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_WK' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_WK_KEY_VAL' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_PRD' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_PRD_KEY_VAL' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_QTR' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR' in col:
            df[col] = df[col].astype('category')
        # ---------------------------------
        if 'DPT_NBR' in col:
            df[col] = df[col].astype('category')
        if 'CLS_NBR' in col:
            df[col] = df[col].astype('category')
        if 'MVNDR_NBR' in col:
            df[col] = df[col].astype('category')
        # ---------------------------------
        if 'MOT_ID' in col:
            df[col] = df[col].astype('category')
        if 'SVC_LVL_ID' in col:
            df[col] = df[col].astype('category')
        if 'SHP_TYP_CD' in col:
            df[col] = df[col].astype('category')
        # ---------------------------------
        if 'LOC_ID' in col:
            df[col] = df[col].astype('category')
        if 'LOC_ALS_ID' in col:
            df[col] = df[col].astype('category')
        if 'ALLOC_LOC_NBR' in col:
            df[col] = df[col].astype('category')
        if 'DC_NBR' in col:
            df[col] = df[col].astype('category')
        if 'ORIG_LOC_NBR' in col:
            df[col] = df[col].astype('category')
        if 'DEST_LOC_NBR' in col:
            df[col] = df[col].astype('category')
        # ---------------------------------
        if 'COST' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'RATE' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'AMT' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        # ---------------------------------

    return df


def replace_with_null(df):
    for col in df.columns:
        if df[col].dtype.name == 'category':
            df[col] = df[col].replace([-1, 0, 'UNK', 'NULL', 'NaN'], np.nan)
    return df


# %%


def cleanup_temp_csv_files(dir_path):

    # Get all the files in the directory
    files = os.listdir(dir_path)

    # Loop through all the files
    for file in files:
        # Check if the file is a .csv file
        if file.endswith(".csv"):
            # Construct the full file path
            file_path = os.path.join(dir_path, file)
            # Delete the file
            os.remove(file_path)


# %%


def read_csv_to_dataframe(directory_path, csv_filename):
    # create the Polars DataFrame by reading the CSV file
    df_pd = pd.read_csv(f"{directory_path}/{csv_filename}")
    # df_pd = df_pl.to_pandas()
    return df_pd

# %%


def msno_eda_save_pngs(
    df,
    tgt_directory,
    df_name='df',
):
    import missingno as msno

    # saving matrix figures
    fig_matrix = msno.matrix(df)
    fig_matrix = fig_matrix.get_figure()
    fig_matrix.savefig(
        tgt_directory+'\\'+'msno_matrix-'+df_name+'.png',
        bbox_inches='tight'
    )


# %%


def compare_df_report(
    df1,
    df2,
    df1_title,
    df2_title,
    shared_pk,
    yaml_config_path,
    to_type='notebook_iframe',
    output_directory='.',
):
    """Compare two pandas dataframes and produce a comparison report using ydata_profiling.

    Args:
        df1 (pandas.DataFrame): The first dataframe to compare.
        df2 (pandas.DataFrame): The second dataframe to compare.
        df1_title (str): The title to use for the first dataframe in the produced report.
        df2_title (str): The title to use for the second dataframe in the produced report.
        shared_pk (str): The name of the column that is the shared primary key between the two dataframes.

    Returns:
        None

    Produces a comparison report between the two dataframes using ydata_profiling. The dataframes are sorted by the shared primary key column and the report is saved to a file in the current working directory with the format "<df1_title>_vs_<df2_title>.html".

    Example:
        compare_df_report(df1, df2, 'Sales Data', 'Marketing Data', 'Customer ID')

    """
    from ydata_profiling import ProfileReport

    # sort by the primary keys first
    if shared_pk is not None:
        df1 = df1.sort_values(by=[
            shared_pk]).reset_index(drop=True)
        df2 = df2.sort_values(by=[
            shared_pk]).reset_index(drop=True)
    else:
        df1 = df1.reset_index(drop=True)
        df2 = df2.reset_index(drop=True)

    # Produce the data profiling report
    if yaml_config_path is not None:
        df1_report = ProfileReport(
            df1, title=df1_title, config_file=yaml_config_path)
        df2_report = ProfileReport(
            df2, title=df2_title, config_file=yaml_config_path)
    else:
        df1_report = ProfileReport(
            df1, title=df1_title)
        df2_report = ProfileReport(
            df2, title=df2_title)

    comparison_report = df1_report.compare(df2_report)

    # output format if else statement
    if to_type == 'notebook_iframe':
        comparison_report.to_notebook_iframe()
    elif to_type == 'widgets':
        comparison_report.to_widgets()
    elif to_type == 'file':
        comparison_report.to_file(
            output_directory+'\\'+'ydatacomp_report-'+df1_title+'_vs_'+df2_title+'.html')


# %%

def excel_auto_eda_run(
    excel_path,
    dir_temp_csv,
    sheet_name_primary,
    sheet_name_secondary,
    ydata_config_yaml_path,
    # ------
    toggle_general=True,
    toggle_ydata=True,
    toggle_ydatacomp=True,
    toggle_dataprep=True,
    toggle_autoviz=True,
    # ------
    toggle_ydata_custom=False,
):
    print('###==========================================================================================')
    print('Succesfully located and initiated python interpreter.')
    print('###==========================================================================================')
    print('')
    print('')

    print('Loading data from excel sheet to pandas dataframe...')
    df = pd.DataFrame()
    df2 = pd.DataFrame()
    #
    df = read_csv_to_dataframe(
        directory_path=dir_temp_csv,
        csv_filename=sheet_name_primary+'.csv',
    )
    if toggle_ydatacomp == True:
        # only load data from second sheet if using for comparison
        df2 = read_csv_to_dataframe(
            directory_path=dir_temp_csv,
            csv_filename=sheet_name_secondary+'.csv',
        )

    print('Succesfully loaded excel data sheet to Pandas dataframe.')
    print('')
    print('###==========================================================================================')
    print('Starting excel_auto_script on:')
    print('Excel workbook:'+excel_path)
    print('Sheet name:'+sheet_name_primary)
    print('###==========================================================================================')
    print('')
    print('')

    # general data cleaning/prep operations here
    print('Starting data cleaning operations...')
    print('')

    # TODO: add to this :noted_on:2023-02-27
    #   [ ] replace -1, 0, 'NULL', 'NaN' and 'UNK' in categorical fields with true nan
    #   [ ] search for time field
    #       when none present, join in from fscl_yr_wk, fscl_yr_prd

    convert_columns(df)  # convert column dtypes to the proper type

    df = df.round(2)
    if toggle_ydatacomp == True:
        df2 = df2.round(2)

    replace_with_null(df)  # replace imputed null values with actual nan

    print('Done with data cleaning operations.')
    print('')

    print('')
    print('###==========================================================================================')
    print('###==========================================================================================')
    print('Starting to build data profiling reports.')
    print('###==========================================================================================')
    print('###==========================================================================================')
    print('')
    print('')

    excel_parent_directory = os.path.dirname(excel_path)

    # creating target directory + saving variable
    tgt_directory = excel_parent_directory+'\\'+sheet_name_primary+'-data_profiling'
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

        general_report_out_path = tgt_directory+'\\' + \
            sheet_name_primary+'-general-report.xlsx'
        # TODO: below function has errors, fix later :noted_on:2023-02-27
        # df_info_to_excel(
        #     df=df,
        #     filepath=general_report_out_path,
        #     sheet_name_primary=sheet_name_primary+'-info',
        # )

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

        yaml_config_path = ydata_config_yaml_path
        from ydata_profiling import ProfileReport

        if toggle_ydata_custom == True:
            profile = ProfileReport(df, config_file=yaml_config_path)
        elif toggle_ydata_custom == False:
            profile = ProfileReport(df, minimal=True)

        # save to excel_parent_directory
        profile.to_file(tgt_directory+'\\' +
                        'ydata_report-'+sheet_name_primary+'.html')

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
                    'dataprep_report-'+sheet_name_primary+'.html')
        # report.show_browser()  # show report in the browser

        print('')
        print('Done building dataprep report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')
    if toggle_autoviz == True:
        print('')
        print('###==========================================================================================')
        print('Starting autoviz report. May take a few minutes...')
        print('###==========================================================================================')
        print('')

        # TODO: fill out this section :noted_on:2023-02-26
        # [ ] testing
        from autoviz.AutoViz_Class import AutoViz_Class
        AV = AutoViz_Class()

        filename = ""
        dft = AV.AutoViz(
            filename,
            sep=",",
            depVar="",
            dfte=df,
            header=0,
            verbose=2,
            lowess=False,
            chart_format='html',
            save_plot_dir=tgt_directory,
        )

        print('')
        print('Done building autoviz report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')
    if toggle_ydatacomp == True:
        print('')
        print('###==========================================================================================')
        print('Starting ydata_comparison report. May take a few minutes...')
        print('###==========================================================================================')
        print('')

        # TODO: build this by referencing function already in eda
        yaml_config_path = ydata_config_yaml_path
        compare_df_report(
            df1=df,
            df2=df2,
            df1_title=sheet_name_primary,
            df2_title=sheet_name_secondary,
            shared_pk=None,
            yaml_config_path=yaml_config_path,
            to_type='file',
            output_directory=tgt_directory,
        )

        print('')
        print('Done building ydata_comparison report to ' +
              tgt_directory + '  '+'Thanks!')
        print('')

    # deleting the temp csv files we created earlier through VBA
    cleanup_temp_csv_files(dir_temp_csv)

    print('')
    print('')
    print('')
    print('')
    print('###==========================================================================================')
    print('###==========================================================================================')
    print('Done building all data profiling reports')
    print('Feel free to close this window.')
    print('###==========================================================================================')
    print('###==========================================================================================')


# ---------------------------------
# %%
excel_path_input = sys.argv[1]
dir_temp_csv_input = sys.argv[2]
sheet_name_primary_input = sys.argv[3]
sheet_name_secondary_input = sys.argv[4]

# ---------------------------------
# Converting "ON","OFF" strings to boolean
toggle_general = sys.argv[5] == 'ON'
toggle_ydata = sys.argv[6] == 'ON'
toggle_ydatacomp = sys.argv[7] == 'ON'
toggle_dataprep = sys.argv[8] == 'ON'
toggle_autoviz = sys.argv[9] == 'ON'

# ---------------------------------
toggle_ydata_custom = sys.argv[10] == 'ON'
ydata_config_yaml_path = sys.argv[11]


# %%
# eda.excel_to_eda_tools(
excel_auto_eda_run(
    excel_path=excel_path_input,
    dir_temp_csv=dir_temp_csv_input,
    sheet_name_primary=sheet_name_primary_input,
    sheet_name_secondary=sheet_name_secondary_input,
    # ---------
    toggle_general=toggle_general,
    toggle_ydata=toggle_ydata,
    toggle_ydatacomp=toggle_ydatacomp,
    toggle_dataprep=toggle_dataprep,
    toggle_autoviz=toggle_autoviz,
    # ---------
    toggle_ydata_custom=toggle_ydata_custom,
    ydata_config_yaml_path=ydata_config_yaml_path,
)

# %%
