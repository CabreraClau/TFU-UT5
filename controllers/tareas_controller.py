from flask import Blueprint, request, jsonify
from services.tareas_service import get_all, add_task

tareas_bp = Blueprint("tareas", __name__)

@tareas_bp.get("/tareas")
def listar():
    return jsonify(get_all())

@tareas_bp.post("/tareas")
def crear():
    data = request.json
    return jsonify(add_task(data)), 201
