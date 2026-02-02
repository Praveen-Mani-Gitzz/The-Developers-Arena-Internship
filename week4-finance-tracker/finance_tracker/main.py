# finance_tracker/main.py

from .expense import Expense
from .expense_manager import ExpenseManager
from .file_handler import save_data, load_data
from .reports import category_breakdown, simple_bar_chart
from datetime import datetime


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        data = load_data()
        self.manager.load_from_list(data)

    def add_expense(self):
        try:
            date = input("Date (YYYY-MM-DD): ")
            amount = input("Amount: ")
            category = input("Category: ")
            description = input("Description: ")

            expense = Expense(date, amount, category, description)
            self.manager.add_expense(expense)
            save_data(self.manager.to_list())

            print("Expense added successfully.")
        except Exception as e:
            print("Error:", e)

    def view_expenses(self):
        for i, e in enumerate(self.manager.get_all()):
            print(f"{i}. {e.date} | {e.category} | {e.amount} | {e.description}")

    def view_category_breakdown(self):
        breakdown = category_breakdown(self.manager.get_all())
        simple_bar_chart(breakdown)

    def run(self):
     while True:
        print("\n1.Add  2.View  3.Report  4.Set Budget  0.Exit")
        choice = input("Choice: ")

        if choice == "1":
            self.add_expense()

        elif choice == "2":
            self.view_expenses()

        elif choice == "3":
            self.view_category_breakdown()

        elif choice == "4":
            try:
                amount = input("Enter monthly budget: ")
                self.manager.set_budget(amount)
                print("Budget set successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == "0":
            print("Exiting application...")
            break

        else:
            print("Invalid choice")



def main():
    tracker = FinanceTracker()
    tracker.run()
