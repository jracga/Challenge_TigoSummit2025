import json
import os
import uuid # esto es para generar IDs únicos si es necesario

MOCK_FILE = "data/mocks.json"

# Functions to load and save mocks from/to a file
# Load mocks from a file
def load_mocks():
    if not os.path.exists(MOCK_FILE):
        return []
    with open(MOCK_FILE, "r") as f:
        return json.load(f)

# Save mocks to a file
def save_mocks(mocks):
    with open(MOCK_FILE, "w") as f:
        json.dump(mocks, f, indent=2)


# Functions to manage mocks (add, get, update, delete) (create, read, update, delete)(CRUD)
# Add, get, update, and delete mocks
def add_mock(data):
    if "id" not in data:
        data["id"] = str(uuid.uuid4())  # Genera un ID único si no se proporciona
    mocks = load_mocks()
    mocks.append(data)
    save_mocks(mocks)
    return data

def get_mocks():
    return load_mocks()

def get_mock_by_id(mock_id):
    mocks = load_mocks()
    for mock in mocks:
        if mock["id"] == mock_id:
            return mock
    return None 

def update_mock(mock_id, new_data):
    mocks = load_mocks()
    for i, mock in enumerate(mocks):
        if mock["id"] == mock_id:
            mocks[i].update(new_data)
            save_mocks(mocks)
            return mocks[i]
    return None

''' 
def delete_mock(mock_id):
    mocks = load_mocks()
    for i, mock in enumerate(mocks):
        if mock["id"] == mock_id:
            del mocks[i]
            save_mocks(mocks)
            return True
    return False
'''
def delete_mock(mock_id):
    mocks = load_mocks()
    new_mocks = [m for m in mocks if m["id"] != mock_id]
    if len(new_mocks) != len(mocks):
        save_mocks(new_mocks)
        return True
    return False