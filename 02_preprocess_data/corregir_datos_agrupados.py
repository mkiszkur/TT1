import pandas as pd
import os
# Ruta a la carpeta con los archivos CSV
folder_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados'

# Obtener una lista de todos los archivos CSV en la carpeta
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Renombrar las columnas y guardar los archivos actualizados
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    # Renombrar las primeras tres columnas
    df.rename(columns={df.columns[0]: 'country_code', df.columns[1]: 'country_name', df.columns[2]: 'anho'}, inplace=True)
    
    # Guardar el archivo CSV actualizado
    df.to_csv(file_path, index=False)

print("Renombrado de columnas completado.")