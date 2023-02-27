# TODO deprecate old / unused functions
# TODO refactor simple functions into python language snippets instead
# TODO: refactor pandas_profiling into ydata_profiling :noted_on:2023-02-25
#           pandas_profiling will be deprecated in April 2023
# TODO: add any new functions from professional version to this one :noted_on:2023-02-25

# %%
# imports
import sys
import os
from datetime import date
import pandas as pd
import numpy as np

# personal projects
# import fp_data_toolbox as fpdt
from fp_data_toolbox import file_handling


# %% ---
# Defining pandas df functions...
# =============================================
# Copy pandas df to clipboard

def copi_colm(data_input):
    """
    Copies columns of a Pandas DataFrame to the clipboard.

    Parameters:
    - data_input (pandas.DataFrame): The DataFrame whose columns should be copied.

    Returns:
    None
    """
    colm_list = list(data_input.columns)
    colm_str = ','.join(colm_list)
    pd.set_option('display.max_colwidth', -1)
    colm_str_df = pd.DataFrame({'columns': [colm_str]})
    colm_str_df.to_clipboard(excel=True, index=False, header=False)


# TODO create function that merges and cleans output df
def df_merge_clean_func():
    # df_merge = pd.merge(df, df_existing, on=['name'], how='outer')
    # # cleaning
    # df_merge['count_x'] = df_merge['count_x'].fillna(0)
    # df_merge['count_y'] = df_merge['count_y'].fillna(0)
    # df_merge = df_merge.rename(columns={
    #     "count_x": "count_src",
    #     "count_y": "count_tgt"
    #     })

    # df_merge=df_merge.sort_values(by=['name'])
    # df_merge = df_merge.reindex([ # not sure if this is necessary
    #     'name',
    #     'count_src',
    #     'count_tgt'
    # ], axis=1)
    return


# %% ---
# Defining visualization functions...
# =============================================
def corr_matrix(data_input, corr_cols_input):
    """
    Compute the correlation matrix of the specified columns in the input dataframe.
    Parameters:
        - data_input (pandas DataFrame): the dataframe containing the data to compute the correlation matrix from.
        - corr_cols_input (list): a list of strings representing the columns to include in the correlation matrix.
    Returns:
        - pandas DataFrame: a dataframe containing the correlation matrix of the specified columns.
    """
    df_input = pd.DataFrame(data_input)
    if isinstance(df_input.index, (pd.DatetimeIndex, pd.MultiIndex)):
        # drop df index for calculation
        df_input = df_input.reset_index(drop=True)
    # update columns to strings in case they are numbers
    df_input.columns = [str(c) for c in df_input.columns]
    corr_df = df_input[corr_cols_input]
    corr_df = corr_df.corr()
    corr_df.index.name = str('column')
    # corr_df = corr_df.style.background_gradient(axis=None, cmap='RdBu', vmin = -1, vmax = 1)
    del df_input
    return corr_df


# %% ---
# Defining main automatic EDA functions
# =============================================

def parallel_fuzzy_merge_df(left_df, right_df, left_key, right_key, threshold=0.9, limit=2):
    """
    Fuzzy merge two dataframes using the optimized Jaro-Winkler Distance algorithm
    :param left_df: the left dataframe to join
    :param right_df: the right dataframe to join
    :param left_key: key column of the left dataframe
    :param right_key: key column of the right dataframe
    :param threshold: minimum Jaro-Winkler distance for a match
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from jaro_winkler import JaroWinkler
    left_df = left_df.copy()
    matches = []
    jaro_winkler = JaroWinkler()
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(
            find_matches, jaro_winkler, right_key, threshold, limit, s): s for s in left_df[left_key]}
        for future in as_completed(futures):
            matches.extend(future.result())
    left_df["matches"] = matches
    return left_df

# %%
# # Pandas Data Profile Report functions
# DONE Create function that autogenerates and saves pd_profile_report to output_path


def pandas_profiling_custom(df, config_file, output_dir, title_input="",  calculate_corr_matrix_bool="false"):
    # pandas profiler df report - save custom config
    from pandas_profiling import ProfileReport

    # variable setup
    output_path = output_dir + title_input + "pd_prfl_rprt.html"

    # pandas profiling setup
    profile = ProfileReport(
        #
        df,
        title=title_input,
        config_file=config_file,

        #
        dataset={
            "description": 'Test Pandas Profiling Report. More words here...',
            "creator": 'Fred Pires',
            "copyright_year": str(date.today().year),
        },

        # variables description
        # variables={
        #     "descriptions": {
        #         'SNSH_YR_WK': 'snapshot year week value.'
        #     }
        # },
        #

        correlations={
            "auto": {
                "calculate": calculate_corr_matrix_bool
            }
        },
        #
    )
    # output
    profile.to_file(output_path)
    profile.to_widgets()
    return


# =============================================
def pandas_profiling_min_nb_frame(df, title_input="Pandas Profiling Report"):
    from pandas_profiling import ProfileReport
    profile = ProfileReport(
        #
        df,
        title=title_input,
        minimal=True,
        infer_dtypes=True,
        #
        vars={
            "cat": {
                "length": "false",
                "characters": "false",
                "words": "false"
            }
        },
        #
        correlations={
            "pearson": {
                "calculate": "false"
            },
            "spearman": {
                "calculate": "false"
            },
            "kendall": {
                "calculate": "false"
            },
            "phi_k": {
                "calculate": "false"
            },
            "cramers": {
                "calculate": "false"
            },
            "auto": {
                "calculate": "true"
            }
        },
        #
        plot={
            "histogram": {
                "x_axis_labels": "false"
            }
        },
        #
        samples={
            "random": "10"
        }
    )
    profile.to_notebook_iframe()

# %%

# dataprep report show


def dataprep_rprt_show(df_input):
    from dataprep.eda import create_report
    dataprep_rprt = create_report(df_input)
    dataprep_rprt.show_browser()


# dataprep report save
def dataprep_rprt_save(df_input, title_input="Pandas Profiling Report"):
    from dataprep.eda import create_report
    dataprep_rprt = create_report(df_input)
    dataprep_rprt.save(title_input)
    dataprep_rprt.show_browser()


# default data population monitor report generation popmon
def pm_rprt_func(data_input, time_axis_colm, features_input, time_width_input="1w", outerbound_2=7, outerbound_1=4, ref_wndw_input=4):
    import pandas as pd
    features_input_fmt = time_axis_colm+":"+features_input
    df_input = pd.DataFrame(data_input)
    pm_rprt = df_input.pm_stability_report(
        time_width=time_width_input,
        time_axis=time_axis_colm,
        features=[
            features_input_fmt
        ],
        extended_report=False,
        reference_type="rolling",
        window=ref_wndw_input,
        show_stats=[
            'distinct*',
            # 'filled*',
            # 'nan*',
            'mean*',
            'std*',
            # 'p05*',
            # 'p50*',
            'p95*',
            'max*',
            # 'min*',
            # 'fraction_true*',
            # 'phik*',
            '*chi2_norm*',
            # '*ks*',
            # '*zscore*',
            # 'n_*',
            # 'worst*',
            '*max_prob_diff*',
            # '*psi*',
            # '*jsd*',
            # '*unknown_labels*'
        ],
        skip_empty_plots=False,
        pull_rules={
            "*_pull": [outerbound_2, outerbound_1, -1 * outerbound_1, -1 * outerbound_2]},
        monitoring_rules={
            "*_pull": [outerbound_2, outerbound_1, -1 * outerbound_1, -1 * outerbound_2],
            "*_zscore": [outerbound_2, outerbound_1, -1 * outerbound_1, -1 * outerbound_2],
            "[!p]*_unknown_labels": [0.5, 0.5, 0, 0],
        }
    )
    return pm_rprt

# ---------------------------------
# %%


# %%


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


# %%
# excel data sheet to data profilers function


def excel_auto_eda_run(excel_path, sheet_name, data_profile_type='ydata'):

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
        profile.to_file(excel_parent_directory+'\\' +
                        sheet_name+'-'+'ydata_report.html')

        print('')
        print('Done building ydata_profiling report to ' +
              excel_parent_directory + '  '+'Thanks!')
    if data_profile_type == 'dataprep':
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
    else:
        print('Done building all data profiling reports')
