# Cleaning functions
import pandas as pd
import re


def data_cleaner(data: pd.DataFrame) -> pd.DataFrame:
    '''
    A function to clean a given dataframe.
    This function will normalize the column names and apply separate cleaning methods for each column based on their data type.

    Parameters:
    data (pd.DataFrame): The input dataframe to be cleaned.

    Returns:
    pd.DataFrame: The cleaned dataframe.

    '''
    import pandas as pd
    # Normalizing column names
    data.columns = data.columns.str.lower()
    data.columns = data.columns.str.replace(' ', '_')
    data.columns = data.columns.str.replace('(', '')
    data.columns = data.columns.str.replace(')', '')

    # Initializing an empty dictionary to store cleaning methods for each data type
    cleaning_methods = {}

    # Iterating through each column in the dataframe
    for column in data.columns:
        # Checking the data type of the current column
        if data[column].dtype == 'object':
            # Assigning a cleaning method for object data type columns
            cleaning_methods[column] = lambda x: x.str.strip()
        elif data[column].dtype == 'int64':
            # Assigning a cleaning method for int data type columns
            cleaning_methods[column] = lambda x: x.fillna(0)
        elif data[column].dtype == 'float64':
            # Assigning a cleaning method for float data type columns
            cleaning_methods[column] = lambda x: x.fillna(0)

    # Applying the cleaning methods to the dataframe
    for column, method in cleaning_methods.items():
        data[column] = method(data[column])

    return data


def drop_duplicates(df, subset=None):
    """
    Drops duplicate rows from the DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame from which duplicate rows will be removed.
        subset (list, optional): A list of column names to consider when identifying duplicates. Default is None.

    Returns:
        pandas.DataFrame: The DataFrame with duplicate rows removed.
    """
    return df.drop_duplicates(subset=subset)


def drop_missing_values(df, axis=0, thresh=None, subset=None):
    """
    Drops missing values from the DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame from which missing values will be removed.
        axis (int, optional): 0 for rows, 1 for columns. Default is 0.
        thresh (int, optional): The minimum number of non-NA values required to keep a row or column. Default is None.
        subset (list, optional): A list of column names to consider when identifying missing values. Default is None.

    Returns:
        pandas.DataFrame: The DataFrame with missing values removed.
    """
    return df.dropna(axis=axis, thresh=thresh, subset=subset)


def fill_missing_values(df, method='ffill', axis=0, inplace=False):
    """
    Fills missing values in the DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame in which missing values will be filled.
        method (str, optional): The method to use for filling missing values. Default is 'ffill'.
        axis (int, optional): 0 for rows, 1 for columns. Default is 0.
        inplace (bool, optional): Whether to modify the original DataFrame or return a new one. Default is False.

    Returns:
        pandas.DataFrame: The DataFrame with missing values filled.
    """
    return df.fillna(method=method, axis=axis, inplace=inplace)


def rename_columns(df, columns_map):
    """
    Renames columns of the DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame whose columns will be renamed.
        columns_map (dict): A dictionary containing the old and new column names.

    Returns:
        pandas.DataFrame: The DataFrame with renamed columns.
    """
    return df.rename(columns=columns_map)


def normalize_datetime(df, datetime_col):
    """
    Normalizes datetime data in a pandas DataFrame.
    :param df: DataFrame with datetime data
    :param datetime_col: name of the column containing datetime data
    :return: DataFrame with normalized datetime data in the format 'YYYY-MM-DD HH:MM:SS'
    """
    df[datetime_col] = pd.to_datetime(
        df[datetime_col], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    return df


def cleanup_distinctness(df, groupby_col, operation, join_col='id', join_type='inner'):
    """
    Clean up unnecessary distinctness within a dataframe.

    Parameters:
    df (pandas.DataFrame): The input dataframe
    groupby_col (str): The column to group by
    operation (str): The operation to perform for each group (min or max)
    join_col (str): The column to use as the join key
    join_type (str): The type of join to perform (inner or outer)

    Returns:
    pandas.DataFrame: The cleaned-up dataframe
    """
    # Group the dataframe by the specified column and get the specified operation for each group
    df_stg = df.groupby(groupby_col, as_index=False).agg(operation)

    # Rename the column specified by `operation`
    df_stg.rename(
        columns={operation: f'{operation}_{groupby_col}'}, inplace=True)

    # Merge the original dataframe with the grouped dataframe on the specified join column
    df = df.merge(df_stg, on=join_col, how=join_type)

    # Drop the original column specified by `operation`
    df.drop([operation], axis=1, inplace=True)

    # Rename the cleaned-up column back to its original name
    df.rename(columns={f'{operation}_{groupby_col}': operation}, inplace=True)

    return df

# %%
