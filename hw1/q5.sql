SELECT "DOLocationID", COUNT("DOLocationID")
AS value_occurrence
FROM yellow_taxi_data
GROUP BY "DOLocationID"
ORDER BY value_occurrence
DESC LIMIT 1;