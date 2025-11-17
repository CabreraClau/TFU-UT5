import json, os
from services.usuarios_service import get_all as get_usuarios

DATA_FILE = "data/proyectos.json"

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

def add_project(data):
    usuarios = get_usuarios()
    if not any(u["id"] == data["usuario_id"] for u in usuarios):
        raise Exception("Usuario no existe")

    proyectos = _load()
    data["id"] = len(proyectos) + 1
    proyectos.append(data)
    _save(proyectos)
    return data
