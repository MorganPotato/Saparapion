import pandas as pd
import sqlite3

# Función para cargar los datos desde CSV a SQLite
def cargar_datos():
    # Archivos CSV
    archivo_principal = "app/data/API_SH.IMM.MEAS_DS2_en_csv_v2_787.csv"
    archivo_paises = "app/data/Metadata_Country_API_SH.IMM.MEAS_DS2_en_csv_v2_787.csv"
    archivo_indicadores = "app/data/Metadata_Indicator_API_SH.IMM.MEAS_DS2_en_csv_v2_787.csv"

    # Leer datos con pandas
    df_principal = pd.read_csv(archivo_principal, skiprows=3)  # Saltar las primeras 3 filas si es necesario
    df_paises = pd.read_csv(archivo_paises)
    df_indicadores = pd.read_csv(archivo_indicadores)

    # Conectar a SQLite
    conn = sqlite3.connect('app/data/vacunacion.db')

    # Guardar datos en tablas
    df_principal.to_sql('datos_principales', conn, if_exists='replace', index=False)
    df_paises.to_sql('metadata_paises', conn, if_exists='replace', index=False)
    df_indicadores.to_sql('metadata_indicadores', conn, if_exists='replace', index=False)

    conn.close()
    print("Datos cargados correctamente en la base de datos.")
