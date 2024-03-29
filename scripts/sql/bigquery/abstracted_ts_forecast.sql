CREATE OR REPLACE PROCEDURE ``()
BEGIN

/*
Requirements:
    - This procedure will run on user's default project. 
        @@project_id is project_id of user who called stored procedure. Otherwise default is project that owns stored procedure.
    - OUTPUT_DATASET needs to be pre-created
*/

--##### STEP 0: DECLARE & SET VARIABLES #####--
DECLARE query STRING;
DECLARE var_seasonality STRING;
DECLARE var_num_periods INT64;
DECLARE var_calendar_column STRING;
DECLARE var_seasonal_lags INT64;

SET @@dataset_project_id = @@project_id; --set default project, @@project_id is project_id of user who called stored procedure. otherwise default is project that owns stored procedure
SET @@dataset_id = var_output_dataset; --set default dataset

SET var_seasonality = CASE  WHEN UPPER(var_freq) = 'DAY' THEN "[STRUCT('DAILY' AS TYPE, DAILY_SEASON AS SEASON, DAILY_HOLIDAY_FLG AS HOLIDAY_FLG), STRUCT('WEEKLY' AS TYPE, WEEKLY_SEASON AS SEASON, WEEKLY_HOLIDAY_FLG AS HOLIDAY_FLG)]"
                            WHEN UPPER(var_freq) = 'WEEK' THEN "[STRUCT('WEEKLY' AS TYPE, WEEKLY_SEASON AS SEASON, WEEKLY_HOLIDAY_FLG AS HOLIDAY_FLG)]"
                            WHEN UPPER(var_freq) = 'MONTH' THEN "[STRUCT('MONTHLY' AS TYPE, MONTHLY_SEASON AS SEASON, FALSE AS HOLIDAY_FLG)]"
                            ELSE ERROR('var_freq should be one of day/week/month')
                      END;

SET var_num_periods = CASE  WHEN UPPER(var_freq) = 'DAY' THEN 364
                            WHEN UPPER(var_freq) = 'WEEK' THEN 52
                            WHEN UPPER(var_freq) = 'MONTH' THEN 12
                      END;

SET var_calendar_column = CASE  WHEN UPPER(var_freq) = 'DAY' THEN 'CAL_DT'
                                WHEN UPPER(var_freq) = 'WEEK' THEN 'FSCL_WK_BGN_DT'
                                WHEN UPPER(var_freq) = 'MONTH' THEN 'FSCL_PRD_BGN_DT'
                          END;

# Setting temp table tbl_seasonal_union:
IF UPPER(var_freq) = 'DAY' THEN 
    CREATE TEMP TABLE tbl_seasonal_union as 
    (SELECT 'DAILY' AS TYPE, 1 AS LAGS UNION ALL SELECT 'WEEKLY' AS TYPE, 5 AS LAGS);
ELSEIF UPPER(var_freq) = 'WEEK' THEN 
    CREATE TEMP TABLE tbl_seasonal_union as 
    (SELECT 'WEEKLY' AS TYPE, 5 AS LAGS);
ELSEIF UPPER(var_freq) = 'MONTH' THEN 
    CREATE TEMP TABLE tbl_seasonal_union as 
    (SELECT 'MONTHLY' AS TYPE, 3 AS LAGS);
END IF;

SET var_seasonal_lags = (SELECT MAX(LAGS) FROM tbl_seasonal_union);


--##### STEP 1: CREATE SEASONAL CALENDAR #####--
SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_SEASONAL_CALENDAR OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS
   (
        WITH TBL1 AS (
        SELECT *
        , MAX(DAILY_HOLIDAY) OVER (PARTITION BY FSCL_WK_BGN_DT) AS WEEKLY_HOLIDAY
        , CONCAT('BEFORE ', LEAD(DAILY_HOLIDAY) OVER (ORDER BY CAL_DT)) AS LEAD_DAILY_HOLIDAY
        , CONCAT('AFTER ', LAG(DAILY_HOLIDAY) OVER (ORDER BY CAL_DT)) AS LAG_DAILY_HOLIDAY
        FROM (
        SELECT *
            , CASE WHEN (MONTH = 1 AND DAY = 1 AND DAYOFWEEK BETWEEN 2 AND 6) OR (MONTH = 1 AND DAY = 2 AND DAYOFWEEK = 2) OR (MONTH = 12 AND DAY = 31 AND DAYOFWEEK = 6) THEN 'NEW YEARS'
                --WHEN MONTH = 5 AND DAY BETWEEN 25 AND 31 AND DAYOFWEEK = 2 THEN 0
                --WHEN (MONTH = 7 AND DAY = 4 AND DAYOFWEEK BETWEEN 2 AND 6) OR (MONTH = 7 AND DAY = 5 AND DAYOFWEEK = 2) OR (MONTH = 7 AND DAY = 3 AND DAYOFWEEK = 6) THEN 0
                --WHEN MONTH = 9 AND DAY BETWEEN 1 AND 7 AND DAYOFWEEK = 2 THEN 0
                WHEN MONTH = 11 AND DAY BETWEEN 22 AND 28 AND DAYOFWEEK = 5 THEN 'THANKSGIVING'
                WHEN (MONTH = 12 AND DAY = 25 AND DAYOFWEEK BETWEEN 2 AND 6) OR (MONTH = 12 AND DAY = 26 AND DAYOFWEEK = 2) OR (MONTH = 12 AND DAY = 24 AND DAYOFWEEK = 6) THEN 'CHRISTMAS'
                ELSE NULL END AS DAILY_HOLIDAY
        FROM (
            SELECT *
            , EXTRACT(MONTH FROM CAL_DT) AS MONTH, EXTRACT(DAY FROM CAL_DT) AS DAY, EXTRACT(DAYOFWEEK FROM CAL_DT) AS DAYOFWEEK
            FROM `pr-edw-views-thd.SHARED.CAL_PRD_HIER_FD`
        )
        )
        )
        , TBL2 AS (
        SELECT *
        , CONCAT('BEFORE ', LEAD(WEEKLY_HOLIDAY) OVER (ORDER BY FSCL_WK_BGN_DT)) AS LEAD_WEEKLY_HOLIDAY
        , CONCAT('AFTER ', LAG(WEEKLY_HOLIDAY) OVER (ORDER BY FSCL_WK_BGN_DT)) AS LAG_WEEKLY_HOLIDAY
        FROM (SELECT DISTINCT FSCL_WK_BGN_DT, WEEKLY_HOLIDAY FROM TBL1)
        )
        , TBL3 AS (
        SELECT A.CAL_DT, A.FSCL_WK_BGN_DT, A.FSCL_PRD_BGN_DT
        , CAST(COALESCE(A.DAILY_HOLIDAY, A.LEAD_DAILY_HOLIDAY, A.LAG_DAILY_HOLIDAY, CAST(A.DAYOFWEEK AS STRING)) AS STRING) AS DAILY_SEASON
        , CASE WHEN A.DAILY_HOLIDAY IS NULL AND A.LEAD_DAILY_HOLIDAY IS NULL AND A.LAG_DAILY_HOLIDAY IS NULL THEN FALSE ELSE TRUE END AS DAILY_HOLIDAY_FLG
        , CAST(COALESCE(A.WEEKLY_HOLIDAY, B.LEAD_WEEKLY_HOLIDAY, B.LAG_WEEKLY_HOLIDAY, CAST(CASE WHEN A.FSCL_WK_NBR = 53 THEN 52 ELSE FSCL_WK_NBR END AS STRING)) AS STRING) AS WEEKLY_SEASON
        , CASE WHEN A.WEEKLY_HOLIDAY IS NULL AND B.LEAD_WEEKLY_HOLIDAY IS NULL AND B.LAG_WEEKLY_HOLIDAY IS NULL THEN FALSE ELSE TRUE END AS WEEKLY_HOLIDAY_FLG
        , CAST(FSCL_PRD_NBR AS STRING) AS MONTHLY_SEASON
        FROM TBL1 A
        INNER JOIN TBL2 B
        ON A.FSCL_WK_BGN_DT = B.FSCL_WK_BGN_DT
        )
        , TBL4 AS (
        SELECT *
            , SEASONALITY[OFFSET(0)].HOLIDAY_FLG AS HOLIDAY_FLG
        FROM (
        SELECT CAL_DT AS DT
            , """|| var_seasonality ||"""
            AS SEASONALITY
        FROM TBL3
        WHERE CAL_DT = """|| var_calendar_column ||"""
        )
        )
        SELECT *
            , ARRAY_AGG(DT) OVER (ORDER BY DT ROWS BETWEEN 1 FOLLOWING AND @var_horizon FOLLOWING) AS FCST_DTS
            , ROW_NUMBER() OVER (ORDER BY DT) AS DT_RNK
            , LEAD(DT) OVER (ORDER BY DT) AS NEXT_DT
        FROM TBL4
    );
""";
EXECUTE IMMEDIATE query USING var_horizon as var_horizon;



--##### STEP 2: CREATE FORECAST SEASONAL SMOOTHING CALENDAR #####--
SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_SEASONAL_SMOOTHING_CALENDAR OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS 
    (
        WITH TYPES AS 
        (
            SELECT *
            FROM tbl_seasonal_union
        )
        , NON_HOLIDAY_CAL AS 
        (
        SELECT *
            , ROW_NUMBER() OVER (ORDER BY DT) AS NON_HOLIDAY_DT_RNK
        FROM """|| @@dataset_id ||""".BQML_SEASONAL_CALENDAR
        WHERE NOT HOLIDAY_FLG
        )

        SELECT B.TYPE, A.DT, C.DT AS SMOOTH_DT
        FROM NON_HOLIDAY_CAL A
        CROSS JOIN TYPES B
        CROSS JOIN NON_HOLIDAY_CAL C
        WHERE C.NON_HOLIDAY_DT_RNK BETWEEN A.NON_HOLIDAY_DT_RNK - (B.LAGS - 1) / 2 AND A.NON_HOLIDAY_DT_RNK + (B.LAGS - 1) / 2
        
        UNION ALL
        
        SELECT B.TYPE, A.DT, A.DT AS SMOOTH_DT
        FROM """|| @@dataset_id ||""".BQML_SEASONAL_CALENDAR A
        CROSS JOIN TYPES B
        WHERE HOLIDAY_FLG
    );
""";
EXECUTE IMMEDIATE query;

CREATE TEMP FUNCTION PERIOD_AVG(A ANY TYPE, PERIOD INT64) AS 
((
    WITH TBL1 AS (
    SELECT X, ROW_NUMBER() OVER (ORDER BY I) AS R
    FROM UNNEST(A) X WITH OFFSET I
    WHERE X IS NOT NULL
    )
    SELECT AVG(X) FROM TBL1 WHERE R <= PERIOD
));





--##### STEP 3: CREATE FORECAST DATA #####--
SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_DATA OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS 
    (
        WITH TBL1 AS (
            SELECT (SELECT STRING_AGG(X, '|') FROM UNNEST(["""|| var_id_cols ||"""]) AS X) AS KEY --CONCAT("""|| var_id_cols ||""") AS KEY
            , """|| var_date_col ||""" AS DT
            , SUM("""|| var_fcst_col ||""") AS QTY
            FROM """|| var_input_table ||"""
            GROUP BY 1,2
        ),
        KEYS AS ( --CONTROL FOR KEYS APPEARING MIDWAY THROUGH DATA BY TAKING KEY SPECIFIC MIN
        SELECT A.KEY, MIN(B.DT_RNK) AS MIN_DT_RNK
        FROM TBL1 A
        INNER JOIN """|| @@dataset_id ||""".BQML_SEASONAL_CALENDAR B
            ON A.DT = B.DT
        WHERE A.QTY <> 0 --TODO?
        GROUP BY 1
        )
        , MAX_DT AS ( --WANT ALL KEYS TO END AT SAME POINT, SO DON'T TAKE KEY SPECIFIC MAX
        SELECT MAX(B.DT_RNK) AS MAX_DT_RNK
        FROM TBL1 A
        INNER JOIN """|| @@dataset_id ||""".BQML_SEASONAL_CALENDAR B
            ON A.DT = B.DT
        )
        , TBL2 AS (
        SELECT A.KEY
            , C.DT
            , C.SEASONALITY
            , C.FCST_DTS
            , C.NEXT_DT
            , C.DT_RNK BETWEEN A.MIN_DT_RNK AND B.MAX_DT_RNK AS FCST_CRT_DT_FLG --PUSH DATA OUT TO COMPUTE SEASONALITY VALUES FOR ALL NEEDED WEEKS, THIS IS HOW TO RECOVER WEEKS WHERE WE CREATE A FORECAST
            , CASE WHEN C.DT_RNK BETWEEN A.MIN_DT_RNK AND B.MAX_DT_RNK THEN COALESCE(D.QTY, 0.0) ELSE NULL END AS QTY
        FROM KEYS A
        CROSS JOIN MAX_DT B
        CROSS JOIN """|| @@dataset_id ||""".BQML_SEASONAL_CALENDAR C
        LEFT JOIN TBL1 D
            ON A.KEY = D.KEY AND C.DT = D.DT
        WHERE C.DT_RNK BETWEEN A.MIN_DT_RNK - (@var_seasonal_lags - 1) / 2 AND B.MAX_DT_RNK + (@var_seasonal_lags - 1) / 2 + @var_horizon
        )
        , TBL3 AS (
        SELECT *
            , LEAST(GREATEST(QTY, PERCENTILE_1), PERCENTILE_99) AS ADJ_QTY
        FROM (
            SELECT A.*
                , PERCENTILE_CONT(QTY, .99) OVER (PARTITION BY KEY) AS PERCENTILE_99
                , PERCENTILE_CONT(QTY, .01) OVER (PARTITION BY KEY) AS PERCENTILE_1
            FROM TBL2 A
        )
        )
        SELECT *
            -- , AVG(ADJ_QTY) OVER (PARTITION BY KEY ORDER BY DT ROWS BETWEEN @var_num_periods PRECEDING AND 1 PRECEDING) AS PERIOD_AVG_QTY
            -- , COUNT(ADJ_QTY) OVER (PARTITION BY KEY ORDER BY DT ROWS BETWEEN @var_num_periods PRECEDING AND 1 PRECEDING) AS PERIOD_COUNT_QTY
            , PERIOD_AVG(ARRAY_AGG(ADJ_QTY) OVER (PARTITION BY KEY ORDER BY DT ROWS BETWEEN @var_num_periods PRECEDING AND @var_num_periods FOLLOWING), @var_num_periods) AS PERIOD_AVG_QTY
        FROM TBL3
    );
""";

EXECUTE IMMEDIATE query USING var_seasonal_lags as var_seasonal_lags, var_horizon as var_horizon, var_num_periods as var_num_periods;


CREATE TEMP FUNCTION MEDIAN_EXCEPT_CURRENT(curr FLOAT64, arr ARRAY<FLOAT64>)
    RETURNS FLOAT64
    LANGUAGE js
    AS """
    function removeItemOnce(arr, value) { //https://stackoverflow.com/questions/5767325/how-can-i-remove-a-specific-item-from-an-array
        var index = arr.indexOf(value);
        if (index > -1) {
            arr.splice(index, 1);
        }
        return arr;
    }
    function median(values){ //https://stackoverflow.com/questions/45309447/calculating-median-javascript
        values.sort(function(a,b){
            return a-b;
        });

        var half = Math.floor(values.length / 2);
        
        if (values.length % 2)
            return values[half];
        
        return (values[half - 1] + values[half]) / 2.0;
    }
    arr = arr.filter(value => !Number.isNaN(value)); //remove nulls
	return median(removeItemOnce(arr, curr))
""";



--##### STEP 4: CREATE SEASONALITY #####--
SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_SEASONALITY OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS 
    (
        SELECT * EXCEPT(SEASONAL_QTY)
            , MEDIAN_EXCEPT_CURRENT(SEASONAL_QTY, ARRAY_AGG(COALESCE(SEASONAL_QTY, CAST('NAN' AS FLOAT64))) OVER (PARTITION BY KEY, TYPE, SEASON)) AS SEASONAL_QTY
            -- , SAFE_DIVIDE(SUM(SEASONAL_QTY) OVER (PARTITION BY KEY, TYPE, SEASON) - COALESCE(SEASONAL_QTY, 0), 
            --             COUNT(SEASONAL_QTY) OVER (PARTITION BY KEY, TYPE, SEASON) - CASE WHEN SEASONAL_QTY IS NOT NULL THEN 1 ELSE 0 END) AS SEASONAL_QTY
                --SEASONAL ESTIMATE IS AVERAGE OF VALUES EXCLUDING CURRENT ROW - THAT WAY WE'RE KEEPING THE FORECAST FOR A DATE INDEPENDENT OF THE VALUE FOR THAT DATE
        FROM 
        (
            SELECT A.KEY, A.DT
                , SEASONALITY.TYPE
                , SEASONALITY.SEASON
                , A.ADJ_QTY - A.PERIOD_AVG_QTY AS SEASONAL_QTY
                --, CASE WHEN PERIOD_COUNT_QTY = @var_num_periods THEN A.ADJ_QTY - A.PERIOD_AVG_QTY ELSE NULL END AS SEASONAL_QTY
                    --IF WE DON'T HAVE A FULL PERIOD OF DATA THEN OUR SEASONAL ESTIMATE WILL BE BIASED
            FROM """|| @@dataset_id ||""".BQML_DATA A
            CROSS JOIN UNNEST(A.SEASONALITY) AS SEASONALITY
        )
    );
""";

EXECUTE IMMEDIATE query USING var_num_periods as var_num_periods;



--##### STEP 5: CREATE SMOOTHED SEASONALITY #####--
CREATE TEMP FUNCTION DOT(V1 ANY TYPE, V2 ANY TYPE) AS 
((
    --SELECT SUM(X1 * V2[OFFSET(I)])
    SELECT SUM(X1 * CASE WHEN IS_NAN(V2[OFFSET(I)]) THEN NULL ELSE V2[OFFSET(I)] END)
    FROM UNNEST(V1) X1 WITH OFFSET I
));

CREATE TEMP FUNCTION SMOOTH(A ANY TYPE, DECAY FLOAT64) AS 
((
    SELECT DOT(ARRAY_AGG(WT / SUM_WTS ORDER BY I), A)
    FROM 
    (
      SELECT *
        , SUM(WT) OVER () AS SUM_WTS
      FROM (
        SELECT I
          , POW(DECAY, ABS((ARRAY_LENGTH(A) - 1) / 2 - I)) AS WT
        FROM UNNEST(GENERATE_ARRAY(0, ARRAY_LENGTH(A) - 1)) I
      )
    )
));

SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_SEASONALITY_SMOOTHED OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS 
    (
        SELECT KEY, DT
            , SUM(SMOOTH(SEASONAL_QTYS, .5)) AS SMOOTHED_SEASONAL_QTY
            , SUM(SMOOTH(SEASONAL_QTYS, 0)) AS SEASONAL_QTY --USING 0 HERE PROVIDES NO SMOOTHING AT ALL, USED FOR AGGRESSIVE FORECAST, ALSO A BACKUP IN CASE WE HAVE LITTLE HISTORY
        FROM 
        (
            SELECT A.KEY, A.DT, A.TYPE
                , ARRAY_AGG(COALESCE(C.SEASONAL_QTY, CAST('NAN' AS FLOAT64)) ORDER BY B.DT) AS SEASONAL_QTYS
            FROM """|| @@dataset_id ||""".BQML_SEASONALITY A
            INNER JOIN """|| @@dataset_id ||""".BQML_SEASONAL_SMOOTHING_CALENDAR B
                ON A.TYPE = B.TYPE AND A.DT = B.DT
            LEFT JOIN """|| @@dataset_id ||""".BQML_SEASONALITY C
                ON A.KEY = C.KEY AND A.TYPE = C.TYPE AND B.SMOOTH_DT = C.DT
            GROUP BY 1,2,3
        )
        GROUP BY 1,2
    );
""";

EXECUTE IMMEDIATE query;


--##### STEP 6: CREATE EXPONENTIAL SMOOTHING DATA #####--
SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_EXP_SMOOTH_DATA OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS 
    (
        SELECT A.KEY
            , A.DT
            , A.NEXT_DT
            , A.FCST_DTS
            , A.FCST_CRT_DT_FLG
            , A.QTY
            , A.ADJ_QTY
            , COALESCE(B.SMOOTHED_SEASONAL_QTY, B.SEASONAL_QTY, 0) AS SMOOTHED_SEASONAL_QTY
            , A.ADJ_QTY - COALESCE(B.SMOOTHED_SEASONAL_QTY, B.SEASONAL_QTY, 0) AS DESEASONALIZED_ADJ_QTY
            --, COALESCE(B.SEASONAL_QTY, 0) AS SEASONAL_QTY
            --, A.ADJ_QTY - COALESCE(B.SEASONAL_QTY, 0) AS ST_DESEASONALIZED_ADJ_QTY
        FROM """|| @@dataset_id ||""".BQML_DATA A
        INNER JOIN """|| @@dataset_id ||""".BQML_SEASONALITY_SMOOTHED B
            ON A.KEY = B.KEY AND A.DT = B.DT
    );
""";

EXECUTE IMMEDIATE query;



--##### STEP 7: CREATE EXPONENTIAL SMOOTHING OUTPUT #####--
--CREATE TEMP FUNCTION EXP_SMOOTH(data ARRAY<STRUCT<dt DATE, deseasonalized_adj_qty FLOAT64, st_deseasonalized_adj_qty FLOAT64>>)
    --RETURNS STRUCT<data ARRAY<STRUCT<dt DATE, deseasonalized_adj_qty FLOAT64, st_deseasonalized_adj_qty FLOAT64, fcst_deseasonalized_qty FLOAT64, st_fcst_deseasonalized_qty FLOAT64>>, 
    --               alpha FLOAT64, alpha_h1 FLOAT64, alpha_h2 FLOAT64, alpha_q1 FLOAT64, alpha_q2 FLOAT64, alpha_q3 FLOAT64, alpha_q4 FLOAT64>
CREATE TEMP FUNCTION EXP_SMOOTH(data ARRAY<STRUCT<dt DATE, deseasonalized_adj_qty FLOAT64>>)
    RETURNS STRUCT<data ARRAY<STRUCT<dt DATE, deseasonalized_adj_qty FLOAT64, fcst_deseasonalized_qty FLOAT64>>, 
                   alpha FLOAT64, alpha_h1 FLOAT64, alpha_h2 FLOAT64>
    LANGUAGE js
    AS """
    function golden_section_search(f, lb, ub, tol) { //https://en.wikipedia.org/wiki/Golden-section_search
        var gr = 1.618033988
        var x1 = {x: lb, y: f(lb)}
        var x2 = {x: (ub + gr * lb) / (gr + 1)}
        x2.y = f(x2.x)
        var x3 = {x: ub, y: f(lb)}
        function search(f, x1, x2, x3, tol) {
            if (x3.x - x1.x < tol) {
                return (x1.x + x3.x) / 2
            }
            var x4 = {x: x1.x + (x3.x - x2.x)}
            x4.y = f(x4.x)
            if (x4.x > x2.x) {
                if (x4.y < x2.y) {
                    return search(f, x2, x4, x3, tol)
                } else {
                    return search(f, x1, x2, x4, tol)
                }
            }
            else {
                if (x4.y < x2.y) {
                    return search(f, x1, x4, x2, tol)
                } else {
                    return search(f, x4, x2, x3, tol)
                }
            }
        }
        return search(f, x1, x2, x3, tol)
    }
    
    function fit(alpha, input_col, sse_low, sse_high, output_col, output_low, output_high) {
        data[0].temp = data[0][input_col]
        var sse = 0
        data.forEach((d, i) => {
            if (i >= 1) {
                d.temp = alpha * data[i][input_col] + (1 - alpha) * data[i-1].temp
                if (i >= sse_low && i <= sse_high) {
                    sse += Math.pow(d[input_col] - data[i-1].temp, 2)
                }
                if (output_col != undefined && i >= output_low && i <= output_high) {
                    d[output_col] = d.temp
                }
            }
        })
        return {data: data, sse: sse}
    }
    
    h1 = Math.floor(data.length / 2)
    q1 = Math.floor(data.length / 4)
    q2 = q1 * 2
    q3 = q1 * 3
    last = data.length - 1
    
    alpha = golden_section_search(x => fit(x, 'deseasonalized_adj_qty', 0, last).sse, 0, 1, .01) //alpha optimized on all data
    alpha_h1 = golden_section_search(x => fit(x, 'deseasonalized_adj_qty', 0, h1).sse, 0, 1, .01) //alpha optimized for h1
    alpha_h2 = golden_section_search(x => fit(x, 'deseasonalized_adj_qty', h1 + 1, last).sse, 0, 1, .01) //etc.
    //alpha_q1 = golden_section_search(x => fit(x, 'st_deseasonalized_adj_qty', 0, q1).sse, 0, 1, .01) //alpha optimized for q1, using non smoothed seasonal estimate
    //alpha_q2 = golden_section_search(x => fit(x, 'st_deseasonalized_adj_qty', q1 + 1, q2).sse, 0, 1, .01)
    //alpha_q3 = golden_section_search(x => fit(x, 'st_deseasonalized_adj_qty', q2 + 1, q3).sse, 0, 1, .01)
    //alpha_q4 = golden_section_search(x => fit(x, 'st_deseasonalized_adj_qty', q3 + 1, last).sse, 0, 1, .01)
    
    //fit updates data in place
    fit(alpha_h2, 'deseasonalized_adj_qty', 0, 0, 'fcst_deseasonalized_qty', 0, h1) //using alpha optimized for h2 to predict h1
    fit(alpha_h1, 'deseasonalized_adj_qty', 0, 0, 'fcst_deseasonalized_qty', h1 + 1, last - 1) //using alpha optimized for h1 to predict h2
    fit(alpha, 'deseasonalized_adj_qty', 0, 0, 'fcst_deseasonalized_qty', last, last) //using alpha optimized for all data
    //fit(alpha_q4, 'st_deseasonalized_adj_qty', 0, 0, 'st_fcst_deseasonalized_qty', 0, last) //use alpha optimized for q4 to predict q1 and last - filling in like this and overwriting below to avoid an extra pass over data
    //fit(alpha_q1, 'st_deseasonalized_adj_qty', 0, 0, 'st_fcst_deseasonalized_qty', q1 + 1, q2) //using alpha optimized for q1 to predict q2
    //fit(alpha_q2, 'st_deseasonalized_adj_qty', 0, 0, 'st_fcst_deseasonalized_qty', q2 + 1, q3) //using alpha optimized for q2 to predict q3
    //fit(alpha_q3, 'st_deseasonalized_adj_qty', 0, 0, 'st_fcst_deseasonalized_qty', q3 + 1, last - 1) //using alpha optimized for q3 to predict q4
    
    //return {data: data, alpha: alpha, alpha_h1: alpha_h1, alpha_h2: alpha_h2, alpha_q1: alpha_q1, alpha_q2: alpha_q2, alpha_q3: alpha_q3, alpha_q4: alpha_q4}
	return {data: data, alpha: alpha, alpha_h1: alpha_h1, alpha_h2: alpha_h2}
""";



SET query =  
"""CREATE OR REPLACE TABLE """|| @@dataset_id ||""".BQML_EXP_SMOOTH_OUTPUT OPTIONS(EXPIRATION_TIMESTAMP=TIMESTAMP_ADD(CURRENT_TIMESTAMP, INTERVAL 2 DAY)) AS 
    (
        WITH TBL1 AS 
        (
            --SELECT KEY, EXP_SMOOTH(ARRAY_AGG(STRUCT(DT, DESEASONALIZED_ADJ_QTY, ST_DESEASONALIZED_ADJ_QTY) ORDER BY DT)) AS EXP_SMOOTH_OUTPUT
			SELECT KEY, EXP_SMOOTH(ARRAY_AGG(STRUCT(DT, DESEASONALIZED_ADJ_QTY) ORDER BY DT)) AS EXP_SMOOTH_OUTPUT
            FROM """|| @@dataset_id ||""".BQML_EXP_SMOOTH_DATA
            WHERE FCST_CRT_DT_FLG
            GROUP BY 1
        )
        SELECT A.KEY, B.*, A.EXP_SMOOTH_OUTPUT.* EXCEPT(DATA)
        FROM TBL1 A
        CROSS JOIN UNNEST(A.EXP_SMOOTH_OUTPUT.DATA) B
    );
""";

EXECUTE IMMEDIATE query;


--##### STEP 8: CREATE COMBINED #####--
SET query =  
"""CREATE OR REPLACE TABLE """ || @@dataset_id || """.""" || var_output_table || """ AS
    (
        SELECT A.KEY
            --, A.DT AS FCST_CRT_DT
            , A.NEXT_DT AS FCST_CRT_DT
            , FCST_DT
            , LAG + 1 AS LAG --INDEX STARTS AT 0
            , C.QTY AS """ || var_fcst_col || """
            , C.ADJ_QTY AS ADJ_""" || var_fcst_col || """
            
            --LONG TERM FORECAST
            , C.DESEASONALIZED_ADJ_QTY AS DESEASONALIZED_ADJ_""" || var_fcst_col || """ 
            , D.FCST_DESEASONALIZED_QTY AS FCST_DESEASONALIZED_ADJ_""" || var_fcst_col || """
            , C.SMOOTHED_SEASONAL_QTY AS SMOOTHED_SEASONAL_""" || var_fcst_col || """
            , D.FCST_DESEASONALIZED_QTY + C.SMOOTHED_SEASONAL_QTY AS FCST_""" || var_fcst_col || """
            
            --SHORT TERM FORECAST
            --, C.ST_DESEASONALIZED_ADJ_QTY
            --, D.ST_FCST_DESEASONALIZED_QTY
            --, C.SEASONAL_QTY
            --, D.ST_FCST_DESEASONALIZED_QTY + C.SEASONAL_QTY AS ST_FCST_QTY
        FROM """|| @@dataset_id ||""".BQML_EXP_SMOOTH_DATA A
        CROSS JOIN UNNEST(A.FCST_DTS) FCST_DT WITH OFFSET LAG
        INNER JOIN """|| @@dataset_id ||""".BQML_EXP_SMOOTH_DATA C
            ON A.KEY = C.KEY AND FCST_DT = C.DT
        INNER JOIN """|| @@dataset_id ||""".BQML_EXP_SMOOTH_OUTPUT D
            ON A.KEY = D.KEY AND A.DT = D.DT
        WHERE A.FCST_CRT_DT_FLG
    );
""";

EXECUTE IMMEDIATE query;



END;