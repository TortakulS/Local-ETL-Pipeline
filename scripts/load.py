
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:159@localhost:5432/ELT_Data")
def load(dataframes):

    for table_name, df in dataframes.items():

        print(f"Loading {table_name}")

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )