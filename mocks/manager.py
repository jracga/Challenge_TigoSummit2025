import json
import os

MOCK_FILE = "data/mocks.json"

def load_mocks():
    if not os.path.exists(MOCK_FILE):
        return []
    with open(MOCK_FILE, "r") as f:
        return json.load(f)

def save_mocks(mocks):
    with open(MOCK_FILE, "w") as f:
        json.dump(mocks, f, indent=2)

def add_mock(data):
    mocks = load_mocks()
    mocks.append(data)
    save_mocks(mocks)
    return data

def get_mocks():
    return load_mocks()
