import os
import pandas as pd

# Ruta a la carpeta con los archivos CSV
folder_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados/sin regiones'

# Obtener una lista de todos los archivos CSV en la carpeta
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Procesar cada archivo CSV
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    
    # Calcular el dataframe con la cantidad de nulos por país y año
    null_counts_country_year = df.groupby(['country_code', 'anho']).apply(lambda x: x.isnull().sum(axis=1)).reset_index()
    null_counts_country_year.columns = ['country_code', 'anho', 'index', 'null_count']
    null_counts_country_year = null_counts_country_year.drop('index', axis=1)
    
    # Guardar el dataframe en un CSV
    country_year_output_path = os.path.join(folder_path, f'null_counts_country_year_{file_name}')
    null_counts_country_year.to_csv(country_year_output_path, index=False)
    
    # Calcular el dataframe con la cantidad de nulos por indicador y año
    indicator_columns = df.columns[3:]  # Todas las columnas excepto las tres primeras
    null_counts_indicator_year = df.groupby('anho')[indicator_columns].apply(lambda x: x.isnull().sum()).reset_index()
    
    # Guardar el dataframe en un CSV
    indicator_year_output_path = os.path.join(folder_path, f'null_counts_indicator_year_{file_name}')
    null_counts_indicator_year.to_csv(indicator_year_output_path, index=False)

print("Procesamiento completado para todos los archivos.")
