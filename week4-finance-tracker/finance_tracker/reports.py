# finance_tracker/reports.py

from collections import defaultdict


def category_breakdown(expenses):
    breakdown = defaultdict(float)

    for e in expenses:
        breakdown[e.category] += e.amount

    return breakdown


def monthly_total(expenses, year, month):
    total = 0
    for e in expenses:
        if e.date.year == year and e.date.month == month:
            total += e.amount
    return total


def simple_bar_chart(breakdown):
    for category, amount in breakdown.items():
        bars = "#" * int(amount // 10)
        print(f"{category:15} | {bars} ({amount})")
