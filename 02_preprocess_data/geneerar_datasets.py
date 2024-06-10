import pandas as pd
import os

# Define la ruta al archivo principal y a la carpeta de CSVs
ruta_principal = '/Users/miguelkiszkurno/Documents/TT1/data/resultados.csv'
ruta_csvs = '/Users/miguelkiszkurno/Documents/TT1/data/csv/'

# Leer el archivo principal
df_principal = pd.read_csv(ruta_principal)
#df_principal = df_principal[df_principal['titulo_seccion'] == 'Urban Development'] #esto es por si quiero generar una seccion en particular
print(df_principal.head())
# Agrupar por 'titulo_seccion' y procesar cada grupo
for titulo, grupo in df_principal.groupby('titulo_seccion'):
    # DataFrame para almacenar los datos combinados de todos los indicadores en este grupo
    df_combinado = pd.DataFrame()
    # Procesar cada indicador en este grupo
    for indicador in grupo['codigo_indicador'].unique():
        archivo_csv = os.path.join(ruta_csvs, f"{indicador}.csv")
        print(archivo_csv)
        if os.path.exists(archivo_csv):
            df_indicador = pd.read_csv(archivo_csv)
            # Asegúrate de que el nombre de la columna de valores coincida con el nombre del archivo
            nombre_columna_valor = indicador  # Ajusta según sea necesario
            if nombre_columna_valor in df_indicador.columns:
                # Concatenar horizontalmente
                if df_combinado.empty:
                    df_combinado = df_indicador
                else:
                    df_combinado = pd.merge(df_combinado, df_indicador[['country_name','country_code','Año', nombre_columna_valor]],
                                            on=['country_name','country_code','Año'], how='outer')

    # Guardar el DataFrame combinado en un nuevo CSV
    if not df_combinado.empty:
        df_combinado.to_csv(os.path.join(ruta_csvs, f"{titulo}.csv"), index=False)
        print(f"Archivo guardado: {titulo}.csv")
    else:
        print(f"No se encontraron datos para {titulo}")

