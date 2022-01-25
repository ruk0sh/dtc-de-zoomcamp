SELECT "PULocationID", "DOLocationID", total_amount
FROM yellow_taxi_data
WHERE total_amount = (
    SELECT MAX(total_amount) FROM yellow_taxi_data
);