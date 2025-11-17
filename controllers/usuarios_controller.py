from flask import Blueprint, request, jsonify
from services.usuarios_service import get_all, add_user

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.get("/usuarios")
def listar():
    return jsonify(get_all())

@usuarios_bp.post("/usuarios")
def crear():
    data = request.json
    return jsonify(add_user(data)), 201
