import pandas as pd


def clean_data(df):
    if df is None:
        return None

    # Convert order_date safely
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Remove rows where date conversion failed
    df = df.dropna(subset=["order_date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill numeric missing values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    print("Data cleaned successfully.")
    return df
