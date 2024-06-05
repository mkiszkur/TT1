from pathlib import Path
import pandas as pd

current_dir = Path.cwd()
print("Current directory:", current_dir)

# Ir un nivel arriba y luego a la carpeta 'data'
parent_dir = current_dir.parent
path_data = parent_dir / 'data'

file_indicadores = path_data / 'resultados.csv'


# Cargar el dataset
file_name = 'combined_indicators_ALL.csv'
file_path = path_data / 'datasets_preprocesados/sin regiones' / file_name

data = pd.read_csv(file_path)



# Calcular la cantidad de indicators únicos por file_name a partir del archivo cobined_indicators.csv
combined_indicators_area = data.groupby('file_name')['indicator'].nunique().reset_index()
combined_indicators_area.columns = ['file_name', 'unique_indicators']

# Guardar el resultado en un archivo CSV
combined_indicators_area.to_csv(path_data / 'combined_indicators_area.csv', index=False)


# Agrupar por file_name y anho y calcular el ratio
combined_indicators_area_ano = data.groupby(['file_name', 'anho']).agg(
    ratio_ones=('is_not_null', 'mean')
).reset_index()

# Guardar el resultado en un archivo CSV
combined_indicators_area_ano.to_csv(path_data / 'combined_indicators_area_ano.csv', index=False)



# Agrupar por file_name e indicator y calcular el ratio
combined_indicators_area_indicator = data.groupby(['file_name', 'indicator']).agg(
    ratio_ones=('is_not_null', 'mean')
).reset_index()

# Guardar el resultado en un archivo CSV
combined_indicators_area_indicator.to_csv(path_data / 'combined_indicators_area_indicator.csv', index=False)


# Agrupar por file_name y country_code y calcular el ratio
combined_indicators_area_country = data.groupby(['file_name', 'country_code']).agg(
    ratio_ones=('is_not_null', 'mean')
).reset_index()

# Guardar el resultado en un archivo CSV
combined_indicators_area_country.to_csv(path_data / 'combined_indicators_area_country.csv', index=False)


# 5. Ratio de cantidad de unos sobre cantidad total de valores de todos los registros por file_name, country_code y anho
combined_indicators_area_country_anho = data.groupby(['file_name', 'country_code', 'anho']).agg(
    ratio_ones=('is_not_null', 'mean')
).reset_index()
combined_indicators_area_country_anho.to_csv(path_data / 'combined_indicators_area_country_anho.csv', index=False)

# 6. Ratio de cantidad de unos sobre cantidad total de valores de todos los registros por file_name, country_code e indicator
combined_indicators_area_country_indicador = data.groupby(['file_name', 'country_code', 'indicator']).agg(
    ratio_ones=('is_not_null', 'mean')
).reset_index()
combined_indicators_area_country_indicador.to_csv(path_data / 'combined_indicators_area_country_indicador.csv', index=False)

# 7. Ratio de cantidad de unos sobre cantidad total de valores de todos los registros por file_name, anho e indicator
combined_indicators_area_anho_indicador = data.groupby(['file_name', 'anho', 'indicator']).agg(
    ratio_ones=('is_not_null', 'mean')
).reset_index()
combined_indicators_area_anho_indicador.to_csv(path_data / 'combined_indicators_area_anho_indicador.csv', index=False)