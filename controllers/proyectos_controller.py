from flask import Blueprint, request, jsonify
from services.proyectos_service import get_all, add_project

proyectos_bp = Blueprint("proyectos", __name__)

@proyectos_bp.get("/proyectos")
def listar():
    return jsonify(get_all())

@proyectos_bp.post("/proyectos")
def crear():
    data = request.json
    return jsonify(add_project(data)), 201
