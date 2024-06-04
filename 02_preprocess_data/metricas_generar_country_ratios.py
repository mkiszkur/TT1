import pandas as pd

def country_code_sin_filtrar():
    # Leer el archivo CSV proporcionado
    file_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados/sin regiones/combined_indicators.csv'
    df = pd.read_csv(file_path)

    # Crear una tabla pivot para calcular el ratio de valores no nulos (unos) sobre el total de registros
    pivot_table = df.pivot_table(index='file_name', columns='country_code', values='is_not_null', aggfunc='mean')

    # Guardar la tabla pivot resultante en un nuevo archivo CSV
    output_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados/metricas/country_ratios.csv'
    pivot_table.to_csv(output_path)

    print(f"Archivo guardado en {output_path}")
    

def country_code_filtrado_por_anho():

    # Leer el archivo CSV proporcionado
    file_path = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados/sin regiones/combined_indicators.csv'
    df = pd.read_csv(file_path)

    # Filtrar los datos por los años 2015 a 2018
    df_filtered = df[(df['anho'] >= 2015) & (df['anho'] <= 2018)]

    # Crear una tabla pivot para calcular el ratio de valores no nulos (unos) sobre el total de registros
    pivot_table = df_filtered.pivot_table(index='file_name', columns='country_code', values='is_not_null', aggfunc='mean')

    # Guardar la tabla pivot resultante en un nuevo archivo CSV
    output_path_filtered = '/Users/miguelkiszkurno/Documents/TT1/data/datasets_preprocesados/metricas/country_ratios_filtered_2015_2018.csv'
    pivot_table.to_csv(output_path_filtered)

#elijo a quien llamar en funcion de si quiero filtrar o no
country_code_sin_filtrar()
#country_code_filtrado_por_anho()
