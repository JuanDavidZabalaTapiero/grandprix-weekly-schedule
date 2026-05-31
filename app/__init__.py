from flask import Flask
from app.core.errors import register_error_handlers
from app.routes.core import core_bp


def create_app():
    app = Flask(__name__)

    # RUTAS
    app.register_blueprint(core_bp)

    # ERRORES
    register_error_handlers(app)

    return app
