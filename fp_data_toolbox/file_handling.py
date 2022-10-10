###=============================================
### General File Handling


## Check for 
def check_dly_data_exists(tgt_directory_str):
    import os
    import datetime as dt

    today = dt.datetime.now().date()

    for file in os.listdir(tgt_directory_str):
        filetime = dt.datetime.fromtimestamp(
                os.path.getctime(tgt_directory_str + file))
        print(filetime)
        if filetime.date() == today:
            ### use output variable in calls to APIs for data. 
            ### Reduces unnecessary pulls when testing or running scripts multiple times in a day.
            print('true')


### DONE function for creating a directory if it does not exist
def create_directory(tgt_directory):
    import os
    if not os.path.exists(tgt_directory):
        os.makedirs(tgt_directory)
        print("Directory " , tgt_directory ,  " Created ")
    else:
        print("Directory " , tgt_directory ,  " already exists")



### DONE function for glueing together a series of .csv files
def glue_csv_files_from_dir(src_directory):
    import pandas as pd
    import glob
    df_output = pd.DataFrame()
    for file_name in glob.glob(src_directory+'*.csv'):
        df = pd.read_csv(file_name, low_memory=False)
        
        ## cleaning and transformation here where necessary
        ##

        df_output = pd.concat([df_output,df],axis=0)
    return df_output



