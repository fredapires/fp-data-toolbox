# =============================================
# General File Handling


# Check for
def check_dly_data_exists(tgt_directory_str):
    """
    Check if a file in a target directory was created today.

    Parameters:
    tgt_directory_str (str): The file path of the target directory.

    Returns:
    bool: True if a file in the target directory was created today, False otherwise.
    """
    import os
    import datetime as dt
    today = dt.datetime.now().date()

    for file in os.listdir(tgt_directory_str):
        filetime = dt.datetime.fromtimestamp(
            os.path.getctime(os.path.join(tgt_directory_str, file)))
        if filetime.date() == today:
            return True
    return False


# DONE function for creating a directory if it does not exist
def create_directory(tgt_directory):
    import os
    if not os.path.exists(tgt_directory):
        os.makedirs(tgt_directory)
        print("Directory ", tgt_directory,  " Created ")
    else:
        print("Directory ", tgt_directory,  " already exists")


# DONE function for glueing together a series of .csv files
def glue_csv_files_from_dir(src_directory, header=0,
                            sep=',', index_col=None,
                            skiprows=None, dtype=None):
    """
    This function reads all CSV files in the specified directory, 
    performs cleaning and transformation as necessary, 
    and concatenates them into a single DataFrame, which is returned.

    Parameters:
    src_directory (str): The path to the directory containing the CSV files.
    header (int): The row number to use as the column names. Default is 0.
    sep (str): The delimiter used in the CSV files. Default is ','.
    index_col (int or str): The column to set as the index. Default is None.
    skiprows (list): A list of rows to skip. Default is None.
    dtype (dict): A dictionary of columns and data types. Default is None.

    Returns:
    DataFrame: The concatenated DataFrame containing all the data from the CSV files.
    """
    import pandas as pd
    import glob
    df_output = pd.DataFrame()
    for file_name in glob.glob(src_directory+'*.csv'):
        df = pd.read_csv(file_name, header=header, sep=sep,
                         index_col=index_col, skiprows=skiprows,
                         dtype=dtype, low_memory=False)

        # cleaning and transformation here where necessary
        ##

        df_output = pd.concat([df_output, df], axis=0)
    return df_output
