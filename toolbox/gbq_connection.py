### [ ] TODO deprecate old / unused functions

# %% --- Connection variable setup

def project_id_cast(project_id_input='analytics-scfinance-thd'):   # INPUT
    project_id = project_id_input
    return project_id


def client_cast(project_id_input='analytics-scfinance-thd'):  # INPUT
    from google.cloud import bigquery
    project_id = project_id_cast(project_id_input)
    client = bigquery.Client(project=project_id)
    return client


def sql_conn_cast(sql_conn_input='mssql+pyodbc://SCFDW2/scfdw_core?driver=SQL+Server+Native+Client+11.0'):
    sql_conn = sql_conn_input
    return sql_conn


# %% --- imports and append_python_path
# def setup():
#     # append path
#     def append_python_path(dir_path_input):
#         import sys
#         try:
#             # Search for already existing instance of path
#             sys.path.index(dir_path_input)
#         except ValueError:
#             sys.path.append(dir_path_input)  # on success, append
#     append_python_path('c:\\Users\\fxp3365\\trans-finance-data-mgmt')  # INPUT

#     # Main Imports
#     from datetime import datetime
#     import pandas as pd
#     import seaborn as sns
#     import numpy as np
#     import multiprocessing as mp
#     import requests as rq
#     import json

#     # Data connection imports
#     from google.cloud import bigquery
#     from google.cloud.bigquery import SchemaField
#     from google.cloud import storage
#     import pandas_gbq

#     # Visualization imports
#     import matplotlib.pyplot as plt
#     from itertools import chain, combinations
#     from pandas_profiling import ProfileReport
#     from dataprep.datasets import load_dataset
#     from dataprep.eda import create_report
#     import popmon
#     from popmon import resources
#     import dtale
#     import dtale.global_state as global_state
#     import pandasgui

#     # %% --- Defining credential and connection variables for querying...
#     # Set your default Google BigQuery project/SQL dialect here
#     project_id = project_id_cast()
#     pandas_gbq.context.project = project_id
#     pandas_gbq.context.dialect = 'standard'

#     # Pandas display options
#     pd.options.display.max_rows = None
#     pd.options.display.max_columns = None

#     # Adjust the jupyter notebook style for easier navigation of the reports
#     from IPython.core.display import display, HTML
#     # Wider notebook
#     display(HTML("<style>.container { width:80% !important; }</style>"))
#     # Cells are higher by default
#     display(HTML("<style>div.output_scroll { height: 44em; }</style>"))


# %% --- Defining run query functions...
# SQL Query
def run_sql_qry(query, input_con):
    import pandas as pd
    output_df = pd.read_sql(query, input_con)
    return output_df

# run GBQ Query
def run_gbq_qry(query, project_id_input='analytics-scfinance-thd'):  # INPUT
    import pandas_gbq
    output_df = pandas_gbq.read_gbq(query, project_id=project_id_input)
    return output_df

# run GBQ CMD
def run_gbq_cmd(query, project_id_input='analytics-scfinance-thd'):  # INPUT
    import pandas_gbq
    output_df = pandas_gbq.read_gbq(query, project_id=project_id_input)

# GBQ Query (return single variable)
def run_gbq_qry_var(query, project_id_input='analytics-scfinance-thd'):
    import pandas_gbq
    result_df = pandas_gbq.read_gbq(query, project_id_input)
    result = result_df.loc[0].item()
    return result

# %% --- ETL Pipeline functions
# The below method (.to_gbq) creates a GBQ table from a given Pandas df.
# The GBQ table schema is inferred automatically based on the dataframes' datatypes.
# if_exists='replace will replace the table if it already exists.
# Changing this to if_exists='append will have the process append the data into the already existing table.
def df_to_gbq_etl(data_input, tgt_table='TEMP_1DAY.df_to_gbq_etl', project_id_input='analytics-scfinance-thd'):
    import pandas as pd
    df_src = pd.DataFrame(data_input)
    import pandas_gbq
    pandas_gbq.to_gbq(df_src, tgt_table, project_id_input, if_exists='replace',
                    # table_schema = [
                    # {'name': 'shp_dt', 'type': 'DATETIME'},
                    # ]
                    )
    print('pandas df loaded to GBQ table: '+project_id_input+'.'+tgt_table)


# The below method (.to_sql) creates a SQL Server table from a given Pandas df.
def df_to_sql_etl(data_input, input_con='mssql+pyodbc://SCFDW2/scfdw_core?driver=SQL+Server+Native+Client+11.0', schema_input='z_adhoc', tgt_table='temp_table'):
    import pandas as pd
    import pyodbc
    df_src = pd.DataFrame(data_input)
    df_src.to_sql(schema=schema_input, name=tgt_table, con=input_con, if_exists='replace', index=False
                )
    print('pandas df loaded to SQL server table: '+schema_input+'.'+tgt_table)


# parse all .sql files in a folder into a long string for sql server execution
def sql_file_str_parse(dir_input='.\\'):
    import os
    for script in os.listdir(dir_input):
        with open(dir_input+'\\' + script,'r') as inserts:
            sqlScript = ''.join(inserts.readlines())
    return sqlScript

# sql file with multiple statements execute
    # this is useful for scripts and longer, multi-statement procedures
    # executes all files within a given directory
    # dependent on pyodbc connection through DSN
def exec_sql_file(sqlScript_input,dsn_input='SCFDW2'):
    import pyodbc
    print ("Connecting via ODBC")
    conn = pyodbc.connect('DSN='+dsn_input, autocommit=True)
    print ("Connected!\n")
    for statement in sqlScript_input.split(';'):
        with conn.cursor() as cur:
            cur.execute(statement+';')
    print('SQL script succesfully executed using DSN='+dsn_input)



# %% --- Defining pandas df functions...
# Copy pandas df to clipboard
def copi_df(data_input):
    import pandas as pd
    copi_df = pd.DataFrame(data_input)
    copi_df.to_clipboard(excel=True, index=False, header=True)
    del copi_df

# Copy pandas df columns to clipboard
def copi_colm_gbq(gbq_table_input, project_id_input='analytics-scfinance-thd'):
    import pandas as pd    
    import pandas_gbq
    query = """SELECT * FROM """+gbq_table_input+""" LIMIT 1"""
    stg_df = pandas_gbq.read_gbq(query, project_id=project_id_input)
    colm_list = list(stg_df.columns)
    colm_df = pd.DataFrame(data=colm_list)
    colm_df[0] = colm_df[0].astype(str) + ','
    colm_df.to_clipboard(excel=True, index=False, header=False)
    del colm_list
    del colm_df

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






# %% --- Defining visualization functions...

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


# %% --- misc. pandas functions
# converting field to datetime data type
def cast_as_datetime(df_input, colm_input):
    import pandas as pd
    df_input[colm_input] = pd.to_datetime(df_input[colm_input],
                                          infer_datetime_format=True,
                                          errors='coerce'
                                          )


# %% --- Defining main automatic EDA functions

# pandas profiler df report - show minimal
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


# # Pivot table
# def df_pivot_brwsr(df_input, output_file_name='pivottablejs'):
#     import webbrowser
#     from pivottablejs import pivot_ui
#     file_name = output_file_name + '.html'
#     df = df_input
#     new_tab = 2  # open in a new tab, if possible
#     pivot_ui(df, outfile_path=file_name)
#     url = file_name
#     webbrowser.open(url, new=new_tab)
