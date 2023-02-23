# Validation functions
import pandas as pd
import re
import datetime
import numpy as np

# %% value validation functions


def is_valid_email(email):
    """
    Check if the input is a valid email address
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_phone_number(phone):
    """
    Check if the input is a valid phone number
    """
    pattern = r'^[+0-9]{10,15}$'
    return re.match(pattern, phone) is not None


def is_valid_zip_code(zip_code):
    """
    Check if the input is a valid zip code
    """
    pattern = r'^[0-9]{5}(?:-[0-9]{4})?$'
    return re.match(pattern, zip_code) is not None


def is_valid_date(date):
    """
    Check if the input is a valid date in the format YYYY-MM-DD
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# %% pandas validation functions


def check_null_values(df):
    """
    Check for any null values in the dataframe
    :param df: pandas dataframe
    :return: dictionary with column name as key and number of null values as value
    """
    return {col: df[col].isnull().sum() for col in df.columns}


def check_column_data_types(df):
    """
    Check the data types of all columns in the dataframe
    :param df: pandas dataframe
    :return: dictionary with column name as key and data type as value
    """
    return {col: df[col].dtype for col in df.columns}


def check_column_value_counts(df, columns):
    """
    Check value counts for specific columns in the dataframe
    :param df: pandas dataframe
    :param columns: list of columns to check value counts for
    :return: dictionary with column name as key and value counts as value
    """
    return {col: df[col].value_counts() for col in columns}


def check_duplicate_rows(df):
    """
    Check for duplicate rows in the dataframe
    :param df: pandas dataframe
    :return: boolean indicating if duplicate rows are present in the dataframe
    """
    return df.duplicated().any()


def check_string_column_length(df, columns):
    """
    Check the length of string values in specific columns
    :param df: pandas dataframe
    :param columns: list of columns to check string length for
    :return: dictionary with column name as key and a list of tuple (index, string length) as value
    """
    string_length = {}
    for col in columns:
        if df[col].dtype == 'object':
            string_length[col] = [(i, len(str(x)))
                                  for i, x in df[col].iteritems()]
    return string_length


def check_null_values(df, columns=None):
    """
    Check for null values in the specified columns of a DataFrame.
    If no columns are specified, check for null values in all columns.
    :param df: pandas DataFrame
    :param columns: list of columns to check for null values
    :return: dictionary with column name as key and number of null values as value
    """
    if columns is None:
        columns = df.columns
    null_cols = {col: df[col].isna().sum() for col in columns}
    return null_cols


def check_duplicate_values(df, columns=None):
    """
    Check for duplicate values in the specified columns of a DataFrame.
    If no columns are specified, check for duplicates in all columns.
    :param df: pandas DataFrame
    :param columns: list of columns to check for duplicates
    :return: dictionary with column name as key and number of duplicates as value
    """
    if columns is None:
        columns = df.columns
    dup_cols = {col: df.duplicated(subset=col).sum() for col in columns}
    return dup_cols


def check_string_pattern(df, columns, pattern):
    """
    Check for a specific pattern in the specified string columns of a DataFrame.
    :param df: pandas DataFrame
    :param columns: list of string columns to check for pattern
    :param pattern: regular expression pattern to match
    :return: dictionary with column name as key and number of matches as value
    """
    pattern_cols = {col: df[col].str.contains(
        pattern, na=False).sum() for col in columns}
    return pattern_cols


def check_numerical_range(df, columns, min_value=None, max_value=None):
    """
    Check for values in the specified numerical columns of a DataFrame that fall within a specified range.
    :param df: pandas DataFrame
    :param columns: list of numerical columns to check
    :param min_value: minimum value of the range (inclusive)
    :param max_value: maximum value of the range (inclusive)
    :return: dictionary with column name as key and number of matches as value
    """
    range_cols = {}
    for col in columns:
        if min_value is not None and max_value is not None:
            range_cols[col] = ((df[col] >= min_value) &
                               (df[col] <= max_value)).sum()
        elif min_value is not None:
            range_cols[col] = (df[col] >= min_value).sum()
        elif max_value is not None:
            range_cols[col] = (df[col] <= max_value).sum()
    return range_cols


def test_df_equals(df1, df2):
    pd.testing.assert_frame_equal(
        df1, df2,
        check_exact=False,
        check_like=True,
        atol=1
    )


# %% 

