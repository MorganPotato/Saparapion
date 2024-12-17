from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar rutas
    from app.routes import configure_routes
    configure_routes(app)

    return app
