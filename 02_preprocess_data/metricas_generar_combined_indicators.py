import os
import pandas as pd
from datetime import datetime

# Ruta a la carpeta con los archivos CSV
folder_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados/sin regiones'


# Obtener una lista de todos los archivos CSV en la carpeta
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]



filtrar_areas = False
filtrar_paises = False #Setear si queremos trabajar con un sobconjunto de paises
country_codes_to_include = ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'MEX', 'URY']
areas_to_include = ['Agriculture & Rural Development.csv', 'Aid Effectiveness.csv', 'Climate Change.csv', 'Economy & Growth.csv']
# Lista para almacenar las filas del resultado
result_data = []

# Procesar cada archivo CSV
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    
    # Leer el archivo CSV
    df = pd.read_csv(file_path)


    if filtrar_paises:
        df = df[df['country_code'].isin(country_codes_to_include)]

    if filtrar_areas:
        df = df[df['file_name'].isin(areas_to_include)]

    # Obtener el nombre del archivo sin la extensión
    file_base_name = os.path.splitext(file_name)[0]
    print (f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: procesando {file_base_name}')

    # Transformar el DataFrame para obtener la estructura deseada
    for index, row in df.iterrows():
        for indicator in df.columns[3:]:
            result_data.append({
                'file_name': file_base_name,
                'country_code': row['country_code'],
                'anho': row['anho'],
                'indicator': indicator,
                'is_not_null': 1 if pd.notnull(row[indicator]) else 0
            })

# Convertir la lista de diccionarios en un DataFrame
result_df = pd.DataFrame(result_data)

# Guardar el DataFrame resultante en un nuevo archivo CSV
output_path = os.path.join(folder_path, 'combined_indicators_ALL.csv')
result_df.to_csv(output_path, index=False)

print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Procesamiento completado y archivo combinado guardado.')
