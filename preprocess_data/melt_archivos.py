
import pandas as pd
import csv
import os

def generar_csv_from_archivo(file_path):
    # Cargamos el dataset
    df = pd.read_excel(file_path, sheet_name='Data', skiprows=3)

    # Usamos la función melt para transformar el dataset
    df_long = pd.melt(df, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                    var_name='Año', value_name='Valor')

    indicator_code = df['Indicator Code'].iloc[0]
    df_long.rename(columns={'Valor': indicator_code}, inplace=True)

    base_name = os.path.splitext(file_path)[0]
    
    new_base_name = base_name.replace('API_', '').split('_DS2')[0]
    csv_base_path = os.path.join(os.path.dirname(file_path), new_base_name)
    csv_file_path = f"{csv_base_path}.csv"


    counter = 1
    while os.path.exists(csv_file_path):
        csv_file_path = f"{csv_base_path} ({counter}).csv"
        counter += 1
   
    df_long[['Country Name', 'Country Code', 'Año', indicator_code]].to_csv(csv_file_path, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, index=False)

    # Muestra las primeras filas del dataframe transformado para verificar
    #print(df_long.head())


def procesar_archivos_en_directorio(directorio):
    # Lista todos los archivos en el directorio
    archivos = os.listdir(directorio)
    
    # Filtra los archivos que terminan en '.xls'
    archivos_xls = [archivo for archivo in archivos if archivo.endswith('.xls')]
    
    # Llama a la función generar_csv_from_archivo para cada archivo .xls
    for archivo_xls in archivos_xls:
        ruta_completa = os.path.join(directorio, archivo_xls)
        print(f"Procesando archivo: {ruta_completa}")
        generar_csv_from_archivo(ruta_completa)

# Definir la ruta del directorio
directorio = '/Users/miguelkiszkurno/Documents/TT1/data/'

# Llamar a la función para procesar todos los archivos
procesar_archivos_en_directorio(directorio)

#generar_csv_from_arhivo('/Users/miguelkiszkurno/Documents/TT1/data/API_DT.NFL.IFAD.CD_DS2_en_excel_v2_48189.xls')

