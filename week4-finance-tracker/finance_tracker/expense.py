# finance_tracker/expense.py

from datetime import datetime


class Expense:
    def __init__(self, date, amount, category, description):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = category.strip()
        self.description = description.strip()

    def validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def validate_amount(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
            return amount
        except:
            raise ValueError("Amount must be a positive number")

    def to_dict(self):
        return {
            "date": self.date.isoformat(),
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["date"],
            data["amount"],
            data["category"],
            data["description"]
        )
