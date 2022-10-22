# TODO deprecate old / unused functions


# %% ---
# Defining pandas df functions...
# =============================================
# Copy pandas df to clipboard
def copi_df(data_input):
    import pandas as pd
    copi_df = pd.DataFrame(data_input)
    copi_df.to_clipboard(excel=True, index=False, header=True)
    del copi_df


# Copy pandas df columns to clipboard
def copi_colm(data_input):
    import pandas as pd
    colm_list = list(data_input.columns)
    colm_df = pd.DataFrame(data=colm_list)
    colm_df[0] = colm_df[0].astype(str) + ','
    colm_df.to_clipboard(excel=True, index=False, header=False)
    del colm_list
    del colm_df


# pandas df join by index
def join_df_index(df1_left_input, df2_right_input, lft_suff='_left', rgt_suff='_right'):
    joined_df = df1_left_input.join(
        df2_right_input, lsuffix=lft_suff, rsuffix=rgt_suff)
    return joined_df


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

# pandas df correlation matrix
def corr_matrix(data_input, corr_cols_input):
    import pandas as pd
    import numpy as np
    df_input = pd.DataFrame(data_input)
    if isinstance(df_input, (pd.DatetimeIndex, pd.MultiIndex)):
        # drop df index for calculation
        df_input = df_input.to_frame(index=False)
    df_input = df_input.reset_index().drop('index', axis=1, errors='ignore')
    # update columns to strings in case they are numbers
    df_input.columns = [str(c) for c in df_input.columns]
    corr_df = df_input[corr_cols_input]
    corr_df = np.corrcoef(corr_df.values, rowvar=False)
    corr_df = pd.DataFrame(
        corr_df, columns=[corr_cols_input], index=[corr_cols_input])
    corr_df.index.name = str('column')
    corr_df = corr_df.reset_index()
    # corr_df = corr_df.style.background_gradient(axis=None, cmap='RdBu', vmin = -1, vmax = 1)
    del df_input
    return corr_df


# %% ---
# misc. pandas functions
# =============================================
# converting field to datetime data type
def cast_as_datetime(df_input, colm_input):
    import pandas as pd
    df_input[colm_input] = pd.to_datetime(df_input[colm_input],
                                          infer_datetime_format=True,
                                          errors='coerce'
                                          )


# %% ---
# Defining main automatic EDA functions
# =============================================

# fuzzy matching logic
def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=2):
    from thefuzz import fuzz
    from thefuzz import process
    """
    pretty inneficient
    :param df_1: the left table to join
    :param df_2: the right table to join
    :param key1: key column of the left tabl
    :param key2: key column of the right table
    :param threshold: how close the matches should be to return a match, based on Levenshtein distance
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    s = df_2[key2].tolist()

    m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit))
    df_1['matches'] = m

    m2 = df_1['matches'].apply(lambda x: ', '.join(
        [i[0] for i in x if i[1] >= threshold]))
    df_1['matches'] = m2

    return df_1


# =============================================
# Pandas Data Profile Report functions
# TODO Create function that autogenerates and saves pd_profile_report to input_path
def pd_profile_fp_save(df, title_input="Pandas Profiling Report", profile):
    # pandas profiler df report - show minimal
    return profile


def pd_profile_min_show(data_input, title_input="Pandas Profiling Report"):
    from pandas_profiling import ProfileReport
    profile = ProfileReport(data_input, title=title_input, minimal=True)
    profile.to_notebook_iframe()
    del profile


# pandas profiler df report - full to HTML file
def pd_profile_save(data_input, title_input="Pandas Profiling Report", minimal='True'):
    from pandas_profiling import ProfileReport
    profile = ProfileReport(data_input, title=title_input, minimal=minimal)
    html_file_name = title_input + ".html"
    profile.to_file(html_file_name)
    del profile
    del html_file_name


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


def dtale_analysis_show(df_input):
    import dtale
    test_dtale = dtale.show(df_input)
    test_dtale.open_browser()
    del test_dtale


# Pivot table
# def df_pivot_brwsr(df_input, output_file_name='pivottablejs'):
#     import webbrowser
#     from pivottablejs import pivot_ui
#     file_name = output_file_name + '.html'
#     df = df_input
#     new_tab = 2  # open in a new tab, if possible
#     pivot_ui(df, outfile_path=file_name)
#     url = file_name
#     webbrowser.open(url, new=new_tab)
