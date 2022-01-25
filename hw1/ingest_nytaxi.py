from time import time

import pandas as pd
from sqlalchemy import create_engine


def ingest_data():

    # Create connection to PostgreSQL
    engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")
    engine.connect()

    # Read data to RAM and infer schema
    data_path = "data/yellow_tripdata_2021-01.csv"
    df = pd.read_csv(data_path, nrows=100)
    print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))

    # Create table in DB
    df.head(n=0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")

    # Populate table by chunk-wise iteration over dataset
    df_iterator = pd.read_csv(data_path, iterator=True, chunksize=100000)
    for chunk in df_iterator:
        t_start = time()
        chunk.tpep_pickup_datetime = pd.to_datetime(chunk.tpep_pickup_datetime)
        chunk.tpep_dropoff_datetime = pd.to_datetime(chunk.tpep_dropoff_datetime)
        chunk.to_sql(name="yellow_taxi_data", con=engine, if_exists="append")
        t_end = time()
        print(f"Ingested another chunk...\nIt took {(t_end - t_start):.3f} seconds")


if __name__ == "__main__":
    ingest_data()
