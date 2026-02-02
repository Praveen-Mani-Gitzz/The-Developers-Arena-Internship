from finance_tracker.expense import Expense

def test_expense_creation():
    e = Expense("2026-02-01", 100, "Food", "Lunch")
    assert e.amount == 100
    assert e.category == "Food"
