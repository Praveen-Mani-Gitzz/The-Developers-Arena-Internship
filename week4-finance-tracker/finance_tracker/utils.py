# finance_tracker/utils.py

def validate_category(category):
    allowed = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Health", "Other"]
    if category not in allowed:
        raise ValueError(f"Category must be one of {allowed}")
    return category


def validate_string(value, field_name):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()
