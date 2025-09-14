import requests
import pandas as pd
import os

# Paso 1: Definir la URL del archivo y la ruta local
url = "https://raw.githubusercontent.com/jakevdp/data-science-handbook/master/notebooks/data/sales_data.csv"
local_filename = "sales_data.csv"

# Paso 2: Descargar el archivo si no existe
if not os.path.exists(local_filename):
    print("Descargando el archivo de datos...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print("Descarga completa. Archivo guardado como 'sales_data.csv'.")
    else:
        print(f"Error al descargar el archivo. Código de estado: {response.status_code}")
else:
    print("El archivo ya existe. Pasando al análisis.")

# Paso 3: Cargar el archivo con Pandas y realizar el análisis inicial
try:
    df = pd.read_csv(local_filename)
    
    # Mostrar las primeras 5 filas para verificar que se cargó correctamente
    print("\nPrimeras 5 filas del DataFrame:")
    print(df.head())
    
    # Obtener un resumen estadístico básico del conjunto de datos
    print("\nResumen estadístico del DataFrame:")
    print(df.describe(include='all'))
    
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{local_filename}'. Asegúrate de que el script lo haya descargado correctamente.")