
import pandas as pd

# Cargar los datasets
file_path_resultados = '/Users/miguelkiszkurno/Documents/TT1/data/resultados.csv'
file_path_indicadores = '/Users/miguelkiszkurno/Documents/TT1/data/indicadores.csv'
output_path = '/Users/miguelkiszkurno/Documents/TT1/data/merged_resultados_indicadores.csv'

resultados = pd.read_csv(file_path_resultados)
indicadores = pd.read_csv(file_path_indicadores)

# Realizar el merge usando el campo codigo_indicador en resultados y INDICATOR_CODE en indicadores
merged_data = pd.merge(resultados, indicadores, left_on='codigo_indicador', right_on='INDICATOR_CODE', how='inner')
merged_data.to_csv(output_path, index=False)


# Indicadores que están en resultados pero no en indicadores
resultados_unicos = resultados[~resultados['codigo_indicador'].isin(indicadores['INDICATOR_CODE'])]
output_path_resultados_unicos = '/Users/miguelkiszkurno/Documents/TT1/data/resultados_unicos.csv'
resultados_unicos.to_csv(output_path_resultados_unicos, index=False)
print(f"Indicadores únicos en resultados guardados en: {output_path_resultados_unicos}")

# Indicadores que están en indicadores pero no en resultados
indicadores_unicos = indicadores[~indicadores['INDICATOR_CODE'].isin(resultados['codigo_indicador'])]
output_path_indicadores_unicos = '/Users/miguelkiszkurno/Documents/TT1/data/indicadores_unicos.csv'
indicadores_unicos.to_csv(output_path_indicadores_unicos, index=False)
print(f"Indicadores únicos en indicadores guardados en: {output_path_indicadores_unicos}")

# Guardar el dataframe combinado en un archivo CSV
output_path_merged = '/Users/miguelkiszkurno/Documents/TT1/data/merged_resultados_indicadores.csv'
merged_data.to_csv(output_path_merged, index=False)