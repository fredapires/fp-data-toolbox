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
