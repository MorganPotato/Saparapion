from flask import jsonify, request
from app.utils import get_db_connection

def configure_routes(app):
    # Ruta de prueba
    @app.route("/")
    def index():
        return jsonify({"mensaje": "API de vacunación funcionando correctamente"}), 200

    # Ruta para obtener todos los datos principales
    @app.route("/api/v1/datos", methods=["GET"])
    def obtener_datos():
        conn = get_db_connection()
        datos = conn.execute('SELECT * FROM datos_principales').fetchall()
        conn.close()
        return jsonify([dict(fila) for fila in datos])

    # Ruta para obtener metadatos de países
    @app.route("/api/v1/paises", methods=["GET"])
    def obtener_paises():
        conn = get_db_connection()
        paises = conn.execute('SELECT * FROM metadata_paises').fetchall()
        conn.close()
        return jsonify([dict(fila) for fila in paises])

    # Ruta para obtener metadatos de indicadores
    @app.route("/api/v1/indicadores", methods=["GET"])
    def obtener_indicadores():
        conn = get_db_connection()
        indicadores = conn.execute('SELECT * FROM metadata_indicadores').fetchall()
        conn.close()
        return jsonify([dict(fila) for fila in indicadores])
