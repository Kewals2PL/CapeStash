import json
import subprocess
import os

DB_FILE = "capes.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_cape(name, cape_id):
    data = load_data()

    # Sprawdź, czy peleryna o tym ID już istnieje
    for entry in data:
        if entry["id"] == cape_id:
            print("Cape ID already exists. Skipping.")
            return

    # Dodaj nową pelerynę
    data.append({"name": name, "id": cape_id})
    save_data(data)
    git_commit_and_push(name)

def git_commit_and_push(name):
    subprocess.run(["git", "add", DB_FILE])
    subprocess.run(["git", "commit", "-m", f"Add new cape: {name}"])
    subprocess.run(["git", "push"])

# Przykład użycia
if __name__ == "__main__":
    add_cape("Ender_Cape", "abcd-efgh-1234")
