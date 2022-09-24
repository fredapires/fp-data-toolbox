
# TODO: replace all references to "curr" with "cur" (this is the actual standard for SCFDW2)
# TODO: create some sort of universal / master fiscal calendar table (most useful to transportation team)
#  [ ] abstract out what this would look like; what would be the PK? data_version should probably be in there
#       [ ] snsh_wk, data version, fiscal week? use data version to distinguish between:
#                       Actuals, Plan, LY, Forecast, Relevant Forecast (end of fscl_qtr), LLY
#       [ ] second table for fiscal week delay (for rolling run-rate forecasting)
#                       R1 delay, R2 delay, R3 delay, R4 delay, R8 delay, R13 delay
#       [ ]


# %% ---importing main module for query functions and more

from toolbox import eda


# %% --- Defining time functions...
# --- current
def get_curr_dt():
    query = """
    SELECT cast(CURRENT_DATE() as string);
    """
    output_var = eda.run_gbq_qry_var(query)
    global curr_dt  # declaring as a global variable for passing to other functions
    curr_dt = output_var
    return output_var


def get_curr_fywk():
    # curr_dt = get_curr_dt();
    query = """select CAST(FSCL_YR_WK_KEY_VAL as STRING)
    from`pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    where CAL_DT = '"""+curr_dt+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_curr_fprd():
    # curr_dt = get_curr_dt();
    query = """select CAST(FSCL_PRD_KEY_VAL as STRING)
    from`pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    where CAL_DT = '"""+curr_dt+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var

# --- last close week


def get_lst_cls_fywk():
    # curr_dt = get_curr_dt();
    query = """select CAST(PREV_FYRWK_KEY_VAL as STRING)
    from`pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    where CAL_DT = '"""+curr_dt+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_lst_cls_fprd():
    # curr_dt = get_curr_dt();
    query = """select CAST(PREV_FPRD_KEY_VAL as STRING)
    from`pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    where CAL_DT = '"""+curr_dt+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


# --- get from
def get_wk_from_dt(dt_input):
    query = """SELECT DISTINCT cast(FSCL_YR_WK_KEY_VAL as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAL_DT = '"""+dt_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_prd_from_dt(dt_input):
    query = """SELECT DISTINCT cast(FSCL_PRD_KEY_VAL as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAL_DT = '"""+dt_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_qtr_from_dt(dt_input):
    query = """SELECT DISTINCT cast(FSCL_QTR_KEY_VAL as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAL_DT = '"""+dt_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


# --- mins
def get_min_dt_from_wk(wk_input):
    query = """SELECT DISTINCT CAST(MIN(CAL_DT) as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_YR_WK_KEY_VAL AS STRING) = '"""+wk_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_min_dt_from_prd(prd_input):
    query = """SELECT DISTINCT CAST(MIN(CAL_DT) as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_PRD_KEY_VAL AS STRING) = '"""+prd_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)

    return output_var


def get_min_dt_from_qtr(qtr_input):
    query = """SELECT DISTINCT CAST(MIN(CAL_DT) as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_QTR_KEY_VAL AS STRING) = '"""+qtr_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_min_wk_from_prd(prd_input):
    query = """SELECT DISTINCT MIN(cast(FSCL_YR_WK_KEY_VAL as STRING))
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_PRD_KEY_VAL AS STRING) = """+prd_input+""";
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_min_wk_from_qtr(qtr_input):
    query = """SELECT DISTINCT MIN(cast(FSCL_YR_WK_KEY_VAL as STRING))
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_QTR_KEY_VAL AS STRING) = """+qtr_input+""";
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


# --- maxes
def get_max_dt_from_wk(wk_input):
    query = """SELECT DISTINCT CAST(MAX(CAL_DT) as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_YR_WK_KEY_VAL AS STRING) = '"""+wk_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_max_dt_from_prd(prd_input):
    query = """SELECT DISTINCT CAST(MAX(CAL_DT) as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_PRD_KEY_VAL AS STRING) = '"""+prd_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_max_dt_from_qtr(qtr_input):
    query = """SELECT DISTINCT CAST(MAX(CAL_DT) as STRING)
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_QTR_KEY_VAL AS STRING) = '"""+qtr_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_max_wk_from_prd(prd_input):
    query = """SELECT DISTINCT MIN(cast(FSCL_YR_WK_KEY_VAL as INT64))
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_PRD_KEY_VAL AS STRING) = '"""+prd_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var


def get_max_wk_from_qtr(qtr_input):
    query = """SELECT DISTINCT MIN(cast(FSCL_YR_WK_KEY_VAL as INT64))
    FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
    WHERE CAST(FSCL_QTR_KEY_VAL AS STRING) = '"""+qtr_input+"""';
    """
    output_var = eda.run_gbq_qry_var(query)
    return output_var

# %% --- main time variables and dictionary setup


def setup_time_range_params(input_type, bgn_input, end_input, slim=True, delay=False):
    import time
    params = {}

    if input_type == 'prd':
        input_type_cd = 1
    if input_type == 'wk':
        input_type_cd = 2
    if input_type == 'dt':
        input_type_cd = 3

    if ('params' in globals() and
        params["input_type_cd"] == input_type_cd and
        params["bgn_input"] == bgn_input and
            params["end_input"] == end_input):
        print(params)
    else:
        params = {}
        params["input_type_cd"] = input_type_cd
        params["bgn_input"] = bgn_input
        params["end_input"] = end_input

    # ---

    if input_type == 'prd':
        bgn_fscl_prd = params["bgn_input"]
        end_fscl_prd = params["end_input"]

        bgn_fscl_dt = get_min_dt_from_prd(bgn_fscl_prd)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        end_fscl_dt = get_max_dt_from_prd(end_fscl_prd)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        bgn_fscl_yr_wk = get_wk_from_dt(bgn_fscl_dt)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        end_fscl_yr_wk = get_wk_from_dt(end_fscl_dt)

        params["bgn_fscl_prd"] = bgn_fscl_prd
        params["end_fscl_prd"] = end_fscl_prd
        params["bgn_fscl_dt"] = bgn_fscl_dt
        params["end_fscl_dt"] = end_fscl_dt
        params["bgn_fscl_yr_wk"] = bgn_fscl_yr_wk
        params["end_fscl_yr_wk"] = end_fscl_yr_wk

    # ---

    if input_type == 'wk':
        bgn_fscl_yr_wk = params["bgn_input"]
        end_fscl_yr_wk = params["end_input"]

        bgn_fscl_dt = get_min_dt_from_wk(bgn_fscl_yr_wk)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        end_fscl_dt = get_max_dt_from_wk(end_fscl_yr_wk)

        params["bgn_fscl_dt"] = bgn_fscl_dt
        params["end_fscl_dt"] = end_fscl_dt
        params["bgn_fscl_yr_wk"] = bgn_fscl_yr_wk
        params["end_fscl_yr_wk"] = end_fscl_yr_wk

    # ---

    if input_type == 'dt':

        bgn_fscl_dt = params["bgn_input"]
        end_fscl_dt = params["end_input"]

        bgn_fscl_yr_wk = get_wk_from_dt(bgn_fscl_dt)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        end_fscl_yr_wk = get_wk_from_dt(end_fscl_dt)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        bgn_fscl_prd = get_prd_from_dt(bgn_fscl_dt)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        end_fscl_prd = get_prd_from_dt(end_fscl_dt)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        bgn_fscl_qtr = get_qtr_from_dt(bgn_fscl_dt)
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
        end_fscl_qtr = get_qtr_from_dt(end_fscl_dt)

    # ---

    if slim == False:
        curr_dt = get_curr_dt()
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
    if slim == False:
        curr_fscl_yr_wk = get_curr_fywk()
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
    if slim == False:
        curr_fscl_prd = get_curr_fprd()
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
    if slim == False:
        lst_cls_fscl_yr_wk = get_lst_cls_fywk()
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)
    if slim == False:
        lst_cls_fscl_prd = get_lst_cls_fprd()
        if delay == True:
            time.sleep(10)
        else:
            time.sleep(0.5)

    if slim == False:
        params["curr_dt"] = curr_dt
        params["curr_fscl_yr_wk"] = curr_fscl_yr_wk
        params["curr_fscl_prd"] = curr_fscl_prd
        params["lst_cls_fscl_yr_wk"] = lst_cls_fscl_yr_wk
        params["lst_cls_fscl_prd"] = lst_cls_fscl_prd

    print(params)

    return params


# ---

# SOMEDAY: add more time variables pulls if necessary

# %% --- utility functions
