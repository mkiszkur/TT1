import os
import pandas as pd

# Ruta a la carpeta con los archivos CSV
folder_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados'

# Lista de códigos de país a eliminar
codes_to_remove = [
    'AFE', 'AFW', 'ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA', 'ECS', 'EMU', 'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 
    'IBT', 'IDA', 'IDB', 'IDX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE', 'MEA', 'MIC', 'MNA', 'NAC', 'OED', 
    'OSS', 'PRE', 'PSS', 'PST', 'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA', 'TSS', 'UMC', 'WLD'
]

# Obtener una lista de todos los archivos CSV en la carpeta
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Procesar cada archivo CSV
for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    
    # Leer el archivo CSV
    df = pd.read_csv(file_path)
    
    # Eliminar los registros con los códigos de país especificados
    df_cleaned = df[~df['country_code'].isin(codes_to_remove)]
    
    # Guardar el archivo CSV limpio
    cleaned_output_path = os.path.join(folder_path, f'cleaned_{file_name}')
    df_cleaned.to_csv(cleaned_output_path, index=False)

print("Limpieza completada para todos los archivos.")
