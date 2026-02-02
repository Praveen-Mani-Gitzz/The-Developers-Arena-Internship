import matplotlib.pyplot as plt


def plot_monthly_sales(monthly_data):
    monthly_data.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
