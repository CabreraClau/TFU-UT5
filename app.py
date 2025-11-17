from flask import Flask
from controllers.usuarios_controller import usuarios_bp
from controllers.proyectos_controller import proyectos_bp
from controllers.tareas_controller import tareas_bp

app = Flask(__name__)

# Registro de blueprints (equivale a cada microservicio antes)
app.register_blueprint(usuarios_bp)
app.register_blueprint(proyectos_bp)
app.register_blueprint(tareas_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
