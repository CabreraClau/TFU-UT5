import json, os
from services.proyectos_service import get_all as get_proyectos

DATA_FILE = "data/tareas.json"

def _load():
    """Carga el archivo JSON de tareas."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    with open(DATA_FILE) as f:
        return json.load(f)

def _save(data):
    """Guarda la lista completa de tareas en el archivo JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_all():
    """Devuelve todas las tareas."""
    return _load()

def add_task(data):
    """Agrega una nueva tarea, validando que el proyecto exista."""
    proyectos = get_proyectos()

    # validar proyecto_id
    if not any(p["id"] == data["proyecto_id"] for p in proyectos):
        raise Exception("Proyecto no encontrado")

    tareas = _load()

    data["id"] = len(tareas) + 1
    tareas.append(data)

    _save(tareas)
    return data
