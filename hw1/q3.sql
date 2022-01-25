SELECT COUNT(*)
FROM yellow_taxi_data
WHERE tpep_pickup_datetime::text LIKE '%-01-15%';