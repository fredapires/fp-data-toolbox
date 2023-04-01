# # **pires_delgado_financial_model-dev**
# %%
# ## **Variable Inputs**

# %% ---

import numpy as np
import pandas as pd
import plotly.express as px
from fp_data_toolbox import eda, notifier
import numpy_financial as npf
# custom imports
notifier.setup()  # Enable for windows toast notifications on Jupyter cell complete
# Magics env settings...
# env variables
df = pd.DataFrame()  # creating empty dataframe variable
params = {}  # creating empty parameters dictionary

# %% 
start_dt_mortgage = '2023-05-01'
current_date = ''

house_sale_inputs = {
    'house_price': 410000,
    'down_payment': 15000,
    'interest_rate': 0.07,
    'loan_term': 30,  # years
}

income_monthly_inputs = {
    'monthly_fred': 5200,
    'monthly_marissa': 1600,
}

expenses_monthly_inputs = {
    # 'rent': 2600,
    'groceries': 500,
    'gasoline': 200,
    'food_out': 300,
    'utilities': 250,
    'lease_car_audi': 406,
    'insurance_car_audi': 180,
    'insurance_car_mini': 70,
    'maintenance_car_audi': 750,
    'maintenance_car_mini': 500,
    'streaming_service_sub': 50,
    'chatgpt_sub': 20,
    'misc': 200,
}

asset_inputs = {
    'fred_checking': 0,
    'fred_saving': 0,
    # 'fred_espp': 0,
    # 'fred_401k': 0,
    'marissa_checking': 0,
    'marissa_saving': 0,
    # 'marissa_401k': 0,
}


debt_inputs = {
    'fred': 0,
    'marissa': 0,
    # 'marissa_student': 0,
}

#
# ## **Imports / Environment Setup**

# %% ---


# %% ---
# ## **Creating more variables / parameters**

def mortgage_payment(interest_rate, loan_term, loan_amount):
    return npf.pmt(interest_rate/12, loan_term*12, -loan_amount)


# %% ---
loan_amount = house_sale_inputs['house_price'] - \
    house_sale_inputs['down_payment']
monthly_mortgage_payment = mortgage_payment(
    house_sale_inputs['interest_rate'], house_sale_inputs['loan_term'], loan_amount
)

new_expenses_monthly_inputs = {
    'mortgage_payment': monthly_mortgage_payment
}
expenses_monthly_inputs.update(new_expenses_monthly_inputs)


# %% --- Define months array for lining up timing
months = pd.date_range(start=start_dt_mortgage,
                       periods=house_sale_inputs['loan_term']*12, freq='M')


# %% ---------------------------------------------------
# Create the DataFrame directly with the data and the index
df = pd.DataFrame(
    {
        'mortgage_balance': npf.ppmt(house_sale_inputs['interest_rate']/12, range(1, house_sale_inputs['loan_term']*12 + 1), house_sale_inputs['loan_term']*12, -loan_amount).cumsum(),
        **{'income_'+key: value for key, value in income_monthly_inputs.items()},
        **{'expense_'+key: value for key, value in expenses_monthly_inputs.items()},
    },
    index=months
)


# %% ---
# TODO: add inflation growth logic here :noted_on:2023-03-31

# grow with infaltion column function
def grow_column_with_inflation_monthly(
    df,
    column,
    inflation_rate,
):
    # Calculate the growth factor based on the frequency
    growth_factor = (1 + inflation_rate) ** (1/12)

    # Calculate the future values using the growth factor
    growth_array = np.power(growth_factor, np.arange(len(df)))
    df[column + '_inflated'] = df[column] * growth_array

    return df

# %% ---


# %% ---
# Calculate the 'net_cash_flow' column
total_income = df.filter(regex='^income_').sum(axis=1)
total_expenses = df.filter(regex='^expense_').sum(axis=1)
# + df['expense_mortgage_payment']
df['net_cash_flow_monthly'] = total_income - total_expenses
df['expenses_monthly_total'] = sum(expenses_monthly_inputs.values())
df['income_monthly_total'] = df['income_monthly_fred'] + \
    df['income_monthly_marissa']

# %% -----------------------------------------------------


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
    # df['DAY_OF_WEEK_CAL'] = df[date_col].dt.dayofweek
    # df['DAY_OF_MNTH_CAL'] = df[date_col].dt.day
    # df['DAY_OF_QTR_CAL'] = df[date_col].dt.dayofyear - ((df[date_col].dt.quarter - 1) * 90)
    # df['DAY_OF_YEAR_CAL'] = df[date_col].dt.dayofyear
    # df['WEEK_OF_MNTH_CAL'] = (df[date_col].dt.day - 1) // 7 + 1
    # df['WEEK_OF_QTR_CAL'] = df[date_col].dt.week % 13
    # df['WEEK_OF_YEAR_CAL'] = df[date_col].dt.week
    df['mnth_of_year_cal'] = df[date_col].dt.month
    df['qtr_of_year_cal'] = df[date_col].dt.quarter
    df['year_cal'] = df[date_col].dt.year

    # Convert all new features to int64 data type
    df = df.astype({
        # 'DAY_OF_WEEK_CAL': 'int64',
        # 'DAY_OF_MNTH_CAL': 'int64',
        # 'DAY_OF_QTR_CAL': 'int64',
        # 'DAY_OF_YEAR_CAL': 'int64',
        # 'WEEK_OF_MNTH_CAL': 'int64',
        # 'WEEK_OF_QTR_CAL': 'int64',
        # 'WEEK_OF_YEAR_CAL': 'int64',
        'mnth_of_year_cal': 'int64',
        'qtr_of_year_cal': 'int64',
        'year_cal': 'int64',
    })

    # Return dataframe with new datetime features merged on the datetime index
    return df


# %% ---
df = df.reset_index().rename(columns={'index': 'TIME_INDEX'})
df = extract_datetime_features(
    df,
    'TIME_INDEX',
)
df = df.set_index('TIME_INDEX')

# %% ---
# ### re-order columns here

df = df.convert_dtypes()

# %% ---
# ## **Data Profiling/Visualization**

# %% ---
df.info()

# %% --- ---
df.to_clipboard(excel=True, index=False, header=True)

# %% --- ---
# ## **Outputs**

# output conversions
df = df

# %% --- ---
# Save the calculation output as a CSV file
df.to_csv('home_financial_output.csv', index=False)

# Save the calculation output as a Parquet file
df.to_parquet('home_financial_output.parquet', index=False)

# %% --- ---
# stop
