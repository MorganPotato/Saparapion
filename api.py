from flask import Flask
from app.routes import configure_routes

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar las rutas de la aplicación
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
