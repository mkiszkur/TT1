import pandas as pd

# Define la ruta al archivo Excel y al archivo CSV de salida
ruta_excel = '/Users/miguelkiszkurno/Documents/TT1/data/xls/API_AG.AGR.TRAC.NO_DS2_en_excel_v2_47959.xls'
ruta_csv_salida = '/Users/miguelkiszkurno/Documents/TT1/data/metadata_countries.csv'

# Lee los datos de la hoja "Metadata - Countries" del archivo Excel
df_metadata = pd.read_excel(ruta_excel, sheet_name='Metadata - Countries')

# Verifica que los datos se hayan cargado correctamente
print(df_metadata.head())

# Guarda los datos en un archivo CSV
df_metadata.to_csv(ruta_csv_salida, index=False)

print(f"Archivo CSV generado: {ruta_csv_salida}")
