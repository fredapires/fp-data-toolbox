# xgboost_explore_test
# ---
#
# <br><br><br><br>

# %% [markdown]
# ## **Environment Setup**
# ---

# %% [markdown]
# ### **Imports and Settings**

# %%
# imports
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# custom imports
# general eda functions and win toast notifier on cell completion
from fp_data_toolbox import eda, notifier
from scf_data_mgmt import fcal, gbq_connection, ssms_connection, environment
# Magics env settings...
# Setup sqlalchemy connection url for MSSQL Server connection here
%matplotlib inline
%load_ext google.cloud.bigquery
%load_ext sql
%env DATABASE_URL = mssql+pyodbc: // SCFDW2/scfdw_core?driver = SQL+Server+Native+Client+11.0
%config SqlMagic.autocommit = True
%config SqlMagic.autopandas = True
# env setup functions
notifier.setup()  # Enable for windows toast notifications on Jupyter cell complete
# Enable to setup a ydata_profiling config.yaml file in the parent project
yaml_config_path = environment.ydata_yaml_setup()
# env variables
gbq_project_id = 'analytics-scfinance-thd'  # USER INPUT
sql_conn = 'mssql+pyodbc://SCFDW2/scfdw_core?driver=SQL+Server+Native+Client+11.0'  # USER INPUT
df = pd.DataFrame()    # creating empty dataframe variable
params = {}            # creating empty parameters dictionary
# params = fcal.pull_fin_cal_temp_var()


# %%

plt.style.use('fivethirtyeight')
color_pal = sns.color_palette()
color_pal

# %% [markdown]
# <br><br><br>

# %% [markdown]
# ## **Function Definition**

# %% [markdown]
# ### **Data Cleaning**

# %%


def convert_columns_for_ml(df):
    for col in df.columns:
        # ---------------------------------
        if 'WK_NBR_IN_YEAR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'WK_NBR_IN_HALF' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'WK_NBR_IN_QTR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'WK_NBR_IN_PRD' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # ---------------------------------
        if 'FSCL_YR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'FSCL_HALF_NBR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'FSCL_QTR_NBR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'FSCL_PRD_NBR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # ---------------------------------
        if 'DPT_NBR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'CLS_NBR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'MVNDR_NBR' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # ---------------------------------
        if 'PNL_IND' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def convert_columns(df):
    for col in df.columns:
        # ---------------------------------
        if 'SNSH_YR_WK' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_WK' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_WK_KEY_VAL' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_PRD' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_PRD_KEY_VAL' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_YR_QTR' in col:
            df[col] = df[col].astype('category')

        if 'WK_NBR_IN_YEAR' in col:
            df[col] = df[col].astype('category')
        if 'WK_NBR_IN_HALF' in col:
            df[col] = df[col].astype('category')
        if 'WK_NBR_IN_QTR' in col:
            df[col] = df[col].astype('category')
        if 'WK_NBR_IN_PRD' in col:
            df[col] = df[col].astype('category')

        if 'FSCL_YR' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_HALF_NBR' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_QTR_NBR' in col:
            df[col] = df[col].astype('category')
        if 'FSCL_PRD_NBR' in col:
            df[col] = df[col].astype('category')

        # ---------------------------------
        if 'PNL_IND' in col:
            df[col] = df[col].astype('category')

        # ---------------------------------
        if 'DPT_NBR' in col:
            df[col] = df[col].astype('category')
        if 'CLS_NBR' in col:
            df[col] = df[col].astype('category')
        if 'MVNDR_NBR' in col:
            df[col] = df[col].astype('category')

        # ---------------------------------
        if 'MOT_ID' in col:
            df[col] = df[col].astype('category')
        if 'SVC_LVL_ID' in col:
            df[col] = df[col].astype('category')
        if 'SHP_TYP_CD' in col:
            df[col] = df[col].astype('category')

        # ---------------------------------
        if 'LOC_ID' in col:
            df[col] = df[col].astype('category')
        if 'LOC_ALS_ID' in col:
            df[col] = df[col].astype('category')
        if 'ALLOC_LOC_NBR' in col:
            df[col] = df[col].astype('category')
        if 'DC_NBR' in col:
            df[col] = df[col].astype('category')
        if 'ORIG_LOC_NBR' in col:
            df[col] = df[col].astype('category')
        if 'DEST_LOC_NBR' in col:
            df[col] = df[col].astype('category')

        # ---------------------------------
        if 'COST' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'RATE' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        if 'AMT' in col:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # ---------------------------------
    return df


def replace_with_null(df):
    for col in df.columns:
        if df[col].dtype.name == 'category':
            df[col] = df[col].replace([-1, 0, 'UNK', 'NULL', 'NaN'], np.nan)
    return df


# %% [markdown]
# <br><br><br><br><br>

# %% [markdown]
# ## **Query Data**

# %%
% % bigquery df
# qry='''
# %%
# df.to_clipboard(excel=True, index=False, header=True)

# %%
len(df)

# %%
# stop

# %% [markdown]
# <br><br><br><br>
#
# ## **Clean Data**

# %%

# df = df[['WK_BGN_DT','FLOW_OB_STR_AMT']]
df = convert_columns(df)
df = replace_with_null(df)
df['WK_BGN_DT'] = pd.to_datetime(df['WK_BGN_DT'])
# df = df.sort_values('WK_BGN_DT', ascending=False)
df = df.set_index('WK_BGN_DT')

# %%
# split into actuals and future dataframes
df_fcst = df.query('IS_FCST == True').copy()
df = df.query('IS_FCST == False').copy()

# %% [markdown]
# <br><br><br>
#
# ## **Data Profiling (Pre-modeling)**

# %%
df.info()

# %%
df.head(5)

# %%
# stop

# %%
df['FLOW_OB_STR_AMT'].plot(
    style='.',
    figsize=(15, 5),
    color=color_pal[0],
    title='Intl Store Landed Flow',
)
plt.show()

# %%
# stop

# %% [markdown]
# <br><br><br>
#
#
# ## **Train / Test Split**

# %%
test_train_split_date = '07-01-2022'  # variable of split date

df_train = df.loc[df.index < test_train_split_date]
df_test = df.loc[df.index >= test_train_split_date]

# %%
fig, ax = plt.subplots(figsize=(15, 5))
df_train['FLOW_OB_STR_AMT'].plot(
    ax=ax, style='.', label='Training Set', title='Train/Test Split')
df_test['FLOW_OB_STR_AMT'].plot(ax=ax, style='.', label='Test Set')
ax.axvline(test_train_split_date, color='black', ls='--')
ax.legend(['Training Set', 'Test Set'])
plt.show()

# %% [markdown]
# <br><br><br>
#
# ## **Forecasting Horizon**
#
# - The forecast horizon is the length of time into the future for which forecasts are to be prepared. These generally vary from short-term forecasting horizons (less than 3 months) to long-term horizons (more than two years).
#

# %% [markdown]
# <br><br><br>
#
# ## **Visualize Feature / Target Relationship**

# %%
fig, ax = plt.subplots(figsize=(20, 8))

ax.set_title = 'OB_FLOW by week in half'
sns.boxplot(
    data=df,
    x='WK_NBR_IN_HALF',
    y='FLOW_OB_STR_AMT',
)

# %% [markdown]
# <br><br><br>
#
# ## **Experiments with creating test models**

# %%
# Define features for training here
FEATURES = [
    'FSCL_YR',
    'FSCL_HALF_NBR',
    'FSCL_QTR_NBR',
    'FSCL_PRD_NBR',
    'WK_NBR_IN_YEAR',
    'WK_NBR_IN_HALF',
    'WK_NBR_IN_QTR',
    'WK_NBR_IN_PRD',
    'PNL_IND',
    'MERCH_DPT_NBR',
    'MERCH_CLS_NBR',
    'lag1',
    'lag2',
    'lag3',
    'lag4',
]

# Define target features here
TARGET = 'FLOW_OB_STR_AMT'

# %%
df_train = convert_columns_for_ml(df_train)
df_test = convert_columns_for_ml(df_test)

# %%
X_train = df_train[FEATURES]
y_train = df_train[TARGET]

X_test = df_test[FEATURES]
y_test = df_test[TARGET]

# %% [markdown]
# <br><br><br>
#
#
# ### **Hyperparameter Optimization WIP**

# %%
# # preprocessing for hyperparameter tuning
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y_train = le.fit_transform(y_train)

# %%
# # import packages for hyperparameters tuning
# from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
# from sklearn.metrics import accuracy_score

# #initialize the domain space for hyperparameters to be optimized
# space={
#         'n_estimators': 100,
#         'max_depth': hp.quniform('max_depth', 3, 12, 1),
#         # 'gamma': hp.uniform ('gamma', 0.2,5),
#         # 'reg_alpha' : hp.quniform('reg_alpha', 0.001, 0.1, 1),
#         # 'reg_lambda' : hp.uniform('reg_lambda', 0,1),
#         # 'colsample_bytree' : hp.uniform('colsample_bytree', 0.5,1),
#         # 'min_child_weight' : hp.quniform('min_child_weight', 1, 8, 1),
#         'seed': 0,
#     }

# def objective(space):
#     clf=xgb.XGBClassifier(
#                     n_estimators =space['n_estimators'],
#                     max_depth = int(space['max_depth']),
#                     # gamma = space['gamma'],
#                     # reg_alpha = int(space['reg_alpha']),min_child_weight=int(space['min_child_weight']),
#                     # colsample_bytree=int(space['colsample_bytree'])
#                     )

#     evaluation = [( X_train, y_train), ( X_test, y_test)]

#     clf.fit(X_train, y_train,
#             eval_set=evaluation, eval_metric="auc",
#             early_stopping_rounds=10,verbose=False)


#     pred = clf.predict(X_test)
#     accuracy = accuracy_score(y_test, pred>0.5)
#     print ("SCORE:", accuracy)
#     return {'loss': -accuracy, 'status': STATUS_OK }

# %%
# trials = Trials()

# best_hyperparams = fmin(fn = objective,
#                         space = space,
#                         algo = tpe.suggest,
#                         max_evals = 100,
#                         trials = trials)

# %%
# print("The best hyperparameters are : ","\n")
# print(best_hyperparams)

# %%
# stop

# %% [markdown]
# <br><br><br>
#

# %% [markdown]
# ### **Train/Test Proof**

# %%
# Save final, optimized hyper parameters for training final model here
reg = xgb.XGBRegressor(
    booster='gbtree',
    objective='reg:squarederror',
    base_score=0.5,
    n_estimators=1500,  # tuned
    min_child_weight=3,
    gamma=0,
    learning_rate=0.048,  # tuned
    subsample=0.8,
    colsample_bytree=0.8,
    max_depth=12,
)


# %%
reg.fit(
    X_train, y_train,
    eval_set=[(X_train, y_train), (X_test, y_test)],
    verbose=100,
)

# %% [markdown]
# **Our model is now trained**

# %% [markdown]
# <br><br><br>
#
# ## **Feature Importance**

# %%
df_fi = pd.DataFrame(
    data=reg.feature_importances_,
    index=reg.feature_names_in_,
    columns=['importance']
)
df_fi.sort_values('importance').plot(kind='barh', title='Feature Importance')
plt.show()

# %% [markdown]
# <br><br><br>
#
# ## **Test forecast on the test set**

# %%
df_test['PREDICTION'] = reg.predict(X_test)
df_test['PREDICTION'] = df_test['PREDICTION'].apply(
    lambda x: 0 if x < 0 else x)  # controlling for negative predictions
cols = [
    'WK_BGN_DT',
    'FSCL_YR_WK',
    'PNL_IND',
    'MERCH_DPT_NBR',
    'MERCH_CLS_NBR',
    'PREDICTION',
]
df_test = df_test[cols]
df_test = convert_columns(df_test)
df_test = df_test.set_index('WK_BGN_DT')

# %%
df_test = pd.merge(
    df,
    df_test,
    how='left',
    on=[
        'WK_BGN_DT',
        'FSCL_YR_WK',
        'PNL_IND',
        'MERCH_DPT_NBR',
        'MERCH_CLS_NBR',
    ],
)
df_test.info()

# %%
ax = df_test[['FLOW_OB_STR_AMT']].plot(figsize=(20, 10), style='.')
df_test['PREDICTION'].plot(
    ax=ax,
    style='.'
)
plt.legend(['Truth Data', 'Predictions'])
ax.set_title('Raw data and predictions')
plt.show()

# %% [markdown]
# <br><br><br>
#
# ## **Calculate root mean squared error**

# %%

df_test = df_test.loc[df_test.index >= test_train_split_date]
score = np.sqrt(mean_squared_error(
    df_test['FLOW_OB_STR_AMT'], df_test['PREDICTION']))
stdev = df_test['FLOW_OB_STR_AMT'].std()
normalized_score = score / stdev
print(f'RMSE Score on Test set: {score:0.6f}')
print(f'RMSE / StdDev on Test set: {normalized_score:0.6f}')

# %% [markdown]
# <br><br><br>
#
# ## **Calculate Nominal Error**
#
# - Look at the worst and best predicted weeks

# %%
df_test['abs_error'] = np.abs(df_test[TARGET] - df_test['PREDICTION'])
df_test['error'] = df_test[TARGET] - df_test['PREDICTION']

# %%
# df_test.to_clipboard(excel=True, index=False, header=True)

# %%
# stop

# %% [markdown]
# <br><br><br>
#
# ## **Predicting into the future**
#
# - Retraining on all data

# %%
# Define features for training here
FEATURES = [
    'FSCL_YR',
    'FSCL_HALF_NBR',
    'FSCL_QTR_NBR',
    'FSCL_PRD_NBR',
    'WK_NBR_IN_YEAR',
    'WK_NBR_IN_HALF',
    'WK_NBR_IN_QTR',
    'WK_NBR_IN_PRD',
    'PNL_IND',
    'MERCH_DPT_NBR',
    'MERCH_CLS_NBR',
    'lag1',
    'lag2',
    'lag3',
    'lag4',
]

# Define target features here
TARGET = 'FLOW_OB_STR_AMT'

x_all = df[FEATURES]
y_all = df[TARGET]

reg = xgb.XGBRegressor(
    booster='gbtree',
    # objective = 'reg:linear',
    objective='reg:squarederror',
    base_score=0.5,
    n_estimators=1500,  # tuned
    # n_estimators = 1000,
    learning_rate=0.042,  # tuned
    # learning_rate = 0.042,
    max_depth=12,  # tuned
    # max_depth = 6,
)
reg.fit(
    x_all,
    y_all,
    eval_set=[(x_all, y_all)],
    verbose=50,
)

# %% [markdown]
# ### **Predict the future**

# %%
df_fcst = convert_columns_for_ml(df_fcst)
df_fcst['PREDICTION'] = reg.predict(df_fcst[FEATURES])

# %%
# plot the future
df_fcst['PREDICTION'].plot(
    figsize=(10, 5),
    style='.',
    color=color_pal[5],
    ms=1,
    lw=1, title='Future Predictions'
)
plt.show()

# %% [markdown]
# <br><br><br>
#
# ## **Saving Model for Later**

# %%
reg.save_model('model.json')

# %% [markdown]
# ### **Loading it back up for validation**

# %%
reg_new = xgb.XGBRegressor()
reg_new.load_model('model.json')
# predict the future
df_fcst['PREDICTION'] = reg.predict(df_fcst[FEATURES])
# plot the future
df_fcst['PREDICTION'].plot(
    figsize=(10, 5),
    style='.',
    color=color_pal[5],
    ms=1,
    lw=1, title='Future Predictions'
)

# %%
df_fcst.to_clipboard(excel=True, index=False, header=True)

# %%
# stop
