import json, os

DATA_FILE = "data/usuarios.json"

def _load():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f: json.dump([], f)
    with open(DATA_FILE) as f:
        return json.load(f)

def _save(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_all():
    return _load()

def add_user(data):
    usuarios = _load()
    data["id"] = len(usuarios) + 1
    usuarios.append(data)
    _save(usuarios)
    return data
