
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv  # Importa la biblioteca csv
import pandas as pd
import os
import re
#Genera un csv con losndatasets que hay en la pagina de world bank
# Hay que hacer un postprocessing porque deja algunos archivos con basura
# Ejemplo de uso del browse_datasets
#p = 'https://data.worldbank.org/indicator?tab=all'
#browse_datasets(p)    

def browse_datasets(p):
    driver = webdriver.Chrome()
    driver.get(p)
    driver.implicitly_wait(0.5)  # Esperar que los elementos estén disponibles

    # Encuentra todos los elementos <li> que contengan un enlace <a>
    list_items = driver.find_elements(By.CSS_SELECTOR, 'li a')

    # Abrir un archivo CSV para escritura
    with open('_datasets_2.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        # Escribir los nombres de las columnas
        writer.writerow(['texto', 'direccion', 'status', 'indicator'])

        # Iterar sobre cada elemento encontrado
        for item in list_items:
            href = item.get_attribute('href')  # Extraer el atributo href
            text = item.text  # Extraer el texto del enlace
            status = 'pendiente'
            if 'indicator' in href:
                match = re.search(r'indicator/(.*?)\?view=chart', href)
                if match:
                    indicator = match.group(1)
                    # Escribir la fila en el archivo CSV si se cumple la condición
                    writer.writerow([text, href, status, indicator])

    # Cerrar el navegador
    print(len(list_items))

    driver.quit()
 

#Prueba para ver como obtener un dataset especifico
def obtener_dataset(p):

    driver = webdriver.Chrome()
    driver.get(p)
    driver.implicitly_wait(0.5)
    excel_link = driver.find_element(By.LINK_TEXT, "EXCEL")
    excel_link.click()
    time.sleep(10)  # Espera (en segundos) puede variar según el tamaño del archivo y la velocidad de conexión
    driver.quit()


#obtener_dataset("https://data.worldbank.org/indicator/AG.LND.AGRI.ZS?view=chart")



#Descarga los datasets a la carpeta downloads. 


def download_from_excel_deprecated(file_path):
    # Leer el archivo Excel
    df = pd.read_csv(file_path, delimiter='|')

    # Configurar el navegador
    driver = webdriver.Chrome()

    # Recorrer las filas del DataFrame
    for index, row in df.iterrows():
        url = row['direccion']
        try:
            driver.get(url)
            driver.implicitly_wait(0.5)  # Esperar para que la página cargue
            
            # Si sabes el texto del enlace puedes cambiar "EXCEL" por el texto correspondiente
            excel_link = driver.find_element(By.LINK_TEXT, "EXCEL")
            excel_link.click()
            
            # Espera para asegurar que el archivo se ha empezado a descargar
            time.sleep(1)
        except Exception as e:
            print(f"Error en la descarga desde {url}: {e}")
    
    # Cerrar el navegador al final de todas las descargas
    driver.quit()

def download_from_excel(file_path):
    # Leer el archivo Excel
    df = pd.read_csv(file_path, delimiter='|')
    print (df.columns)
    # Configurar el navegador
    driver = webdriver.Chrome()

    # Recorrer las filas del DataFrame
    for index, row in df.iterrows():
        if row['status'] != 'descargado':  # Verificar si el status no es 'descargado'
            url = row['direccion']
            try:
                driver.get(url)
                driver.implicitly_wait(0.5)  # Esperar para que la página cargue

                # Si sabes el texto del enlace puedes cambiar "EXCEL" por el texto correspondiente
                excel_link = driver.find_element(By.LINK_TEXT, "EXCEL")
                excel_link.click()

                # Espera para asegurar que el archivo se ha empezado a descargar
                time.sleep(1)  # Aumentado a 10 segundos para dar más tiempo de respuesta

                # Actualizar el status en el DataFrame
                df.at[index, 'status'] = 'descargado'
            except Exception as e:
                print(f"Error en la descarga desde {url}: {e}")

    # Cerrar el navegador al final de todas las descargas
    driver.quit()
    
    # Guardar los cambios en el archivo CSV
    df.to_csv(file_path, index=False, sep='|')



#Ejemplo de uso
download_from_excel('/Users/miguelkiszkurno/Documents/TT1/Data/_datasets_2.csv')



