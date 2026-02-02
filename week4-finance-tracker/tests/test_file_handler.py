from finance_tracker.file_handler import save_data, load_data

def test_save_and_load():
    test_data = [{"date": "2026-02-01", "amount": 100, "category": "Food", "description": "Test"}]
    save_data(test_data)
    loaded = load_data()
    assert isinstance(loaded, list)
