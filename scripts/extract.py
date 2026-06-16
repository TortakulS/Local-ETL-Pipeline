import pandas as pd

def extract_sales_csv(df):
    df = pd.read_csv(df)
    df["Purchase Date"] = pd.to_datetime(
    df["Purchase Date"]
)
    return df