import pandas as pd
import matplotlib.pyplot as plt
from sales_analyzer.data_loader import load_data
from sales_analyzer.data_cleaner import clean_data
from sales_analyzer.analyzer import total_sales, sales_by_category, monthly_sales
from sales_analyzer.visualizer import plot_monthly_sales
def main():
    file_path = "data/raw/sales_data.csv"

    df = load_data(file_path)
    df = clean_data(df)

    print("\nTotal Sales:", total_sales(df))

    print("\nSales by Category:")
    category_data = sales_by_category(df)
    print(category_data)

    print("\nTop Category:", category_data.idxmax())

    monthly_data = monthly_sales(df)

    print("\nMonthly Sales:")
    print(monthly_data)

    plot_monthly_sales(monthly_data)


if __name__ == "__main__":
    main()
    
    
    

    
    

# Load data
df = pd.read_csv("data/raw/sales_data.csv")

print("Dataset Loaded Successfully\n")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())


total_sales = df["total_amount"].sum()
print("\nTotal Sales:", total_sales)


print("\nSales by Category:")

category_sales = df.groupby("category")["total_amount"].sum()

print(category_sales)


top_category = category_sales.idxmax()
print("\nTop Category:", top_category)





monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
