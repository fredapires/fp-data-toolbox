### casting sql connection string
def sql_conn_cast(sql_conn_input='mssql+pyodbc://SCFDW2/scfdw_core?driver=SQL+Server+Native+Client+11.0'):
    sql_conn = sql_conn_input
    return sql_conn


# %% --- Defining run query functions...
# SQL Query
def run_sql_qry(query, input_con):
    import pandas as pd
    output_df = pd.read_sql(query, input_con)
    return output_df

# The below method (.to_sql) creates a SQL Server table from a given Pandas df.
def df_to_sql_etl(data_input, input_con='mssql+pyodbc://SCFDW2/scfdw_core?driver=SQL+Server+Native+Client+11.0', schema_input='z_adhoc', tgt_table='temp_table'):
    import pandas as pd
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

