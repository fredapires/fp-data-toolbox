-- ==================================================
	-- Fiscal week adjustment temp table; -1 weeks running difference;
    SELECT
         CAST(a.year_week_number as INT64) as year_week_number
        ,CAST(a.FSCL_YR_WK_KEY_VAL as INT64) as fscl_yr_wk
        ,CAST(b.FSCL_YR_WK_KEY_VAL as INT64) as adj_fscl_yr_wk
    FROM (
        SELECT 
            row_number() over (
                order by 
                    FSCL_YR asc
                   ,FSCL_WK_NBR asc
                ) as year_week_number
            ,* 
        FROM `pr-edw-views-thd.SHARED.FSCL_WK_HIER_FD` 
            ORDER BY FSCL_YR asc ,FSCL_WK_NBR asc
        ) as a
    LEFT JOIN (
        SELECT 
            row_number() over (
                order by 
                    FSCL_YR asc
                   ,FSCL_WK_NBR asc
                ) as year_week_number
            ,* 
        FROM `pr-edw-views-thd.SHARED.FSCL_WK_HIER_FD` 
        ) as b
        ON b.year_week_number = a.year_week_number - 1 -- Adjust weeks here
    -- ==================================================

-- ===================================================================

ORDER BY
    1;



