-- LINK: https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls


-- 1. Identify missing values in the timeseries data:
---------------------------------------------

WITH time_series AS (
  SELECT DATE_TRUNC(timestamp_column, DAY) AS day,
         COUNT(*) AS count
  FROM `your_table`
  GROUP BY day
  ORDER BY day ASC
)
SELECT *
FROM (
  SELECT day, 
         LAG(day) OVER (ORDER BY day) AS prev_day,
         COUNT(*) AS count,
         LAG(count) OVER (ORDER BY day) AS prev_count
  FROM time_series
)
WHERE prev_day IS NOT NULL AND day > DATE_ADD(prev_day, INTERVAL 1 DAY)
ORDER BY day ASC;
---------------------------------------------


-- 2. Identify anomalies in the timeseries data using a moving average:
--      This calculates a 7-day moving average for the numeric_column over the timeseries data.
---------------------------------------------
SELECT timestamp_column,
       numeric_column,
       AVG(numeric_column) OVER (ORDER BY timestamp_column ROWS BETWEEN 6 PRECEDING AND 6 FOLLOWING) AS moving_average
FROM your_table;
---------------------------------------------


-- 3. Identify trends and seasonality in the timeseries data using a seasonal decomposition:
--      This calculates a 7-day moving average for the numeric_column and a monthly average for each month, and then identifies data points where the moving average is higher than the monthly average, indicating a potential upward trend.
---------------------------------------------
SELECT *
FROM (
  SELECT *,
         AVG(numeric_column) OVER (ORDER BY timestamp_column ROWS BETWEEN 6 PRECEDING AND 6 FOLLOWING) AS moving_average,
         AVG(numeric_column) OVER (PARTITION BY EXTRACT(MONTH FROM timestamp_column) ORDER BY timestamp_column ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS monthly_average
  FROM your_table
)
WHERE moving_average > monthly_average;
---------------------------------------------