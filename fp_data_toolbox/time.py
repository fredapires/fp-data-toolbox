
# %%
import pandas as pd
import calendar

# %%


def create_df_monthly_calendar(start_year, start_month, end_year, end_month):
    """
    Create a pandas dataframe representing a monthly calendar, along with various integer-based categorical features.

    Args:
        start_year (int): The year of the first month.
        start_month (int): The month number (1-12) of the first month.
        end_year (int): The year of the last month.
        end_month (int): The month number (1-12) of the last month.

    Returns:
        pandas.DataFrame: A dataframe representing the monthly calendar, with columns for year, quarter, month of year, and month of quarter.

    Examples:
        >>> df_monthly_calendar = create_df_monthly_calendar(
        ...     start_year=1990,
        ...     start_month=1,
        ...     end_year=2060,
        ...     end_month=12
        ... )
        >>> df_monthly_calendar
        year  quarter  month_of_year  month_of_quarter
        1990-01-01  1990  1  1  1
        1990-02-01  1990  1  2  2
        1990-03-01  1990  1  3  3
        1990-04-01  1990  2  4  1
        1990-05-01  1990  2  5  2
        ...  ...  ...  ...
        2060-08-01  2060  3  8  2
        2060-09-01  2060  3  9  3
        2060-10-01  2060  4  10  1
        2060-11-01  2060  4  11  2
        2060-12-01  2060  4  12  3
        [8520 rows x 4 columns]

    """
    start_date = pd.Timestamp(year=start_year, month=start_month, day=1)
    end_date = pd.Timestamp(year=end_year, month=end_month, day=1)
    date_range = pd.date_range(start=start_date, end=end_date, freq="MS")
    data = []
    for date in date_range:
        month_data = {
            "year": date.year,
            "quarter": (date.month - 1) // 3 + 1,
            "month_of_year": date.month,
            "month_of_quarter": (date.month - 1) % 3 + 1
        }
        data.append(month_data)
    df_calendar = pd.DataFrame(data)
    df_calendar.index = pd.date_range(
        start=start_date, end=end_date, freq="MS")
    return df_calendar


# %%

# %%
