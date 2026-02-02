def total_sales(df):
    return df["total_amount"].sum()


def sales_by_category(df):
    return df.groupby("category")["total_amount"].sum()


def monthly_sales(df):
    df = df.copy()  # prevent modifying original dataframe
    df["month"] = df["order_date"].dt.to_period("M")
    return df.groupby("month")["total_amount"].sum()
