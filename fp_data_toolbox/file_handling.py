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
