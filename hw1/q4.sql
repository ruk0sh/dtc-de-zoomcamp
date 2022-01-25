SELECT tpep_pickup_datetime, tip_amount
FROM yellow_taxi_data
WHERE tip_amount = (
    SELECT MAX(tip_amount)
    FROM yellow_taxi_data
    WHERE tpep_pickup_datetime::text LIKE '%-01-%'
);