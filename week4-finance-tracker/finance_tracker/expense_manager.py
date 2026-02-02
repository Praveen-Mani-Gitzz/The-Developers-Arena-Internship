# finance_tracker/expense_manager.py

from .expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)

    def search_by_category(self, category):
        return [e for e in self.expenses if e.category.lower() == category.lower()]

    def get_all(self):
        return self.expenses

    def to_list(self):
        return [e.to_dict() for e in self.expenses]

    def load_from_list(self, data_list):
        self.expenses = [Expense.from_dict(d) for d in data_list]
        
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0

    def set_budget(self, amount):
        self.monthly_budget = float(amount)

    def total_expenses(self):
        return sum(e.amount for e in self.expenses)

    def remaining_budget(self):
        return self.monthly_budget - self.total_expenses()