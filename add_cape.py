import json
import os
import re
import subprocess

DB_FILE = "capes.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("Błąd: Plik capes.json jest uszkodzony lub pusty. Zostanie zainicjowany jako pusty.")
        return []

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def is_valid_code(code):
    pattern = re.compile(r"^[A-Z0-9]{5}(-[A-Z0-9]{5}){4}$")
    return bool(pattern.fullmatch(code))

def add_cape_code(category_name, cape_id):
    data = load_data()

    for category in data:
        if category["name"].lower() == category_name.lower():
            for code in category["codes"]:
                if code["id"] == cape_id:
                    print("Ten kod już istnieje w tej kategorii.")
                    return
            category["codes"].append({"id": cape_id, "used": False})
            save_data(data)
            git_commit_and_push(category_name, cape_id)
            print(f"Dodano kod do istniejącej kategorii: {category_name}")
            return

    new_category = {
        "name": category_name,
        "codes": [{"id": cape_id, "used": False}]
    }
    data.append(new_category)
    save_data(data)
    git_commit_and_push(category_name, cape_id)
    print(f"Utworzono nową kategorię i dodano kod: {category_name}")

def git_commit_and_push(name, cape_id):
    subprocess.run(["git", "add", DB_FILE])
    subprocess.run(["git", "commit", "-m", f"Add cape code {cape_id} to category {name}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    print("=== Dodawanie kodu peleryny ===")
    category_name = input("Podaj nazwę kategorii pelerynki: ").strip()
    cape_id = input("Podaj kod peleryny (np. KFDY7-PY3RY-VVCCW-2VVY3-J73KZ): ").strip().upper()

    if not category_name or not cape_id:
        print("Błąd: nie podano kategorii lub kodu.")
    elif not is_valid_code(cape_id):
        print("Błąd: kod ma nieprawidłowy format. Oczekiwany format to XXXXX-XXXXX-XXXXX-XXXXX-XXXXX.")
    else:
        add_cape_code(category_name, cape_id)