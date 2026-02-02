# finance_tracker/file_handler.py

import json
import os
from datetime import datetime


DATA_FILE = "data/expenses.json"
BACKUP_FOLDER = "data/backup"


def save_data(data):
    os.makedirs("data", exist_ok=True)

    # Backup before overwrite
    if os.path.exists(DATA_FILE):
        os.makedirs(BACKUP_FOLDER, exist_ok=True)
        backup_name = f"{BACKUP_FOLDER}/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.replace(DATA_FILE, backup_name)

    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading file:", e)
        return []
