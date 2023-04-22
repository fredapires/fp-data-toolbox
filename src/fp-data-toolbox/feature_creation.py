
# Feature creation function


# %%

def create_lag_and_window_features(df, target_col, lag_list=[1, 2, 3], window_list=[30, 90, 180]):
    """
    Creates lag and rolling window features for a given target column in a pandas DataFrame.

    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the target column.
    target_col : str
        The name of the target column.
    lag_list : list, optional (default=[1,2,3])
        A list of integers representing the lags to create.
    window_list : list, optional (default=[30,90,180])
        A list of integers representing the windows to create rolling features for.

    Returns:
    --------
    pandas.DataFrame
        The DataFrame with the added lag and rolling window features.
    """
    # Create lag features
    for lag in lag_list:
        df[f'{target_col}_{lag}_LAG'] = df[target_col].shift(lag, freq='M')

    # Create rolling window features
    for window in window_list:
        df[f'{target_col}_{window}_WIN_MEAN_LAG'] = df[target_col].rolling(
            window=f'{window}D').mean()
        df[f'{target_col}_{window}_WIN_MIN_LAG'] = df[target_col].rolling(
            window=f'{window}D').min()
        df[f'{target_col}_{window}_WIN_MAX_LAG'] = df[target_col].rolling(
            window=f'{window}D').max()
        df[f'{target_col}_{window}_WIN_STD_LAG'] = df[target_col].rolling(
            window=f'{window}D').std()

    return df

# %%


def extract_datetime_features(df, date_col):
    """
    Extracts various datetime features from a pandas dataframe column and returns the modified dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataframe containing the date column to extract features from.
    date_col : str
        The name of the date column to extract features from. If 'index', the function will use the index as the date column.

    Returns
    -------
    pandas.DataFrame
        The modified dataframe with the extracted datetime features added as columns.

    Notes
    -----
    This function extracts the following datetime features: day of week, day of month, day of quarter, day of year,
    week of month, week of quarter, week of year, month of year, quarter of year, and year. All extracted features are
    added as new columns to the input dataframe.

    """
    if date_col == 'index':
        df['date_index'] = df.index
        date_col = 'date_index'

    # Extract year, month, week of year, and week of quarter
    df['DAY_OF_WEEK_CAL'] = df[date_col].dt.dayofweek
    df['DAY_OF_MNTH_CAL'] = df[date_col].dt.day
    df['DAY_OF_QTR_CAL'] = df[date_col].dt.dayofyear - \
        ((df[date_col].dt.quarter - 1) * 90)
    df['DAY_OF_YEAR_CAL'] = df[date_col].dt.dayofyear
    df['WEEK_OF_MNTH_CAL'] = (df[date_col].dt.day - 1) // 7 + 1
    df['WEEK_OF_QTR_CAL'] = df[date_col].dt.week % 13
    df['WEEK_OF_YEAR_CAL'] = df[date_col].dt.week
    df['MNTH_OF_YEAR_CAL'] = df[date_col].dt.month
    df['QTR_OF_YEAR_CAL'] = df[date_col].dt.quarter
    df['YEAR_CAL'] = df[date_col].dt.year

    # Convert all new features to int64 data type
    df = df.astype({
        'DAY_OF_WEEK_CAL': 'int64',
        'DAY_OF_MNTH_CAL': 'int64',
        'DAY_OF_QTR_CAL': 'int64',
        'DAY_OF_YEAR_CAL': 'int64',
        'WEEK_OF_MNTH_CAL': 'int64',
        'WEEK_OF_QTR_CAL': 'int64',
        'WEEK_OF_YEAR_CAL': 'int64',
        'MNTH_OF_YEAR_CAL': 'int64',
        'QTR_OF_YEAR_CAL': 'int64',
        'YEAR_CAL': 'int64',
    })

    # Return dataframe with new datetime features merged on the datetime index
    return df

# %%
