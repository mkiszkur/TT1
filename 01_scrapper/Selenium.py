
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv  # Importa la biblioteca csv
import pandas as pd
import os
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Genera un csv con los ndatasets que hay en la pagina de world bank
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

#Download de todos los archivos de datos que figuran en el archivo de input
def download_from_excel(file_path):
    # Leer el archivo Excel
    df = pd.read_csv(file_path, delimiter=',')
    print (df.columns)
    # Configurar el navegador
    driver = webdriver.Chrome()

    # Recorrer las filas del DataFrame
    for index, row in df.iterrows():
        if row['estado'] != 'descargado':  # Verificar si el status no es 'descargado'
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
                df.at[index, 'estado'] = 'descargado'
            except Exception as e:
                print(f"Error en la descarga desde {url}: {e}")

    # Cerrar el navegador al final de todas las descargas
    driver.quit()
    
    # Guardar los cambios en el archivo CSV
    df.to_csv(file_path, index=False, sep=',')



#Ejemplo de uso
#download_from_excel('/Users/miguelkiszkurno/Documents/TT1/Data/_datasets_2.csv')

#Recorre las secciones de lapaguna en busca de los arvhivos. La deprecamos porque me quedo mejor la funcion que recorre los 
#uls

def encontrar_secciones(p):
    driver = webdriver.Chrome()
    driver.get(p)
    driver.implicitly_wait(0.5)  # Esperar que los elementos estén disponibles

    # Define 'wait' dentro de la función para que esté disponible
    wait = WebDriverWait(driver, 10)
    

    # Encuentra todos los elementos <li> que contengan un enlace <a>
    secciones = driver.find_elements(By.CLASS_NAME, 'nav-item')

    with open('resultados.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribe los encabezados del archivo CSV
        writer.writerow(['Elemento', 'Subelemento', 'Href del Subelemento'])

        # Recorre todas las secciones encontradas
        for seccion in secciones:
            seccion_text = seccion.text
            print (f"***seccion:{seccion.text}***")
            #children = seccion.find_elements(By.XPATH, ".//*")  # Selecciona todos los elementos descendientes
            c = seccion.find_elements(By.XPATH, "./descendant::ul")
            print(type(c))
            children = seccion.find_elements(By.XPATH, "./descendant::ul")
            for child in children:
                #print(f"Tag: {child.tag_name}, Texto: {child.text}, Atributos: {child.get_attribute('outerHTML')}")
                #print(f"Tag: {child.tag_name},href:{child.get_attribute('href')}")
                link_element = child.find_element(By.TAG_NAME, 'a')
                href_value = link_element.get_attribute('href')

                # Extrae el texto visible del enlace
                link_text = link_element.text

                writer.writerow([seccion_text, link_text, href_value])
            # Encuentra el enlace dentro del h3 y haz clic para entrar en la sección
    # Cierra el navegador
    driver.quit()

#encontrar_secciones("https://data.worldbank.org/indicator")




def recorrer_datasets(p):
    driver = webdriver.Chrome()
    driver.get(p)
    driver.implicitly_wait(0.5)  # Esperar que los elementos estén disponibles    

    with open('resultados.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribe los encabezados del archivo CSV
        writer.writerow(['titulo_seccion', 'nombre_dataset', 'codigo_indicador', 'estado', 'direccion'])

        #son 20 secciones
        for i in range(1,20):
            #header con el titulo
            h3 = driver.find_element(By.XPATH, f"//*[@id='main']/div[2]/section[{i}]/h3")
            titulo_seccion = h3.text
            
            #ul con la lista de datasets/indicadores
            c = driver.find_elements(By.XPATH, f"//*[@id='main']/div[2]/section[{i}]/ul")

            #Busco todos los elementos del ultimo ul (que es el que contiene los datos)
            children = c[len(c)-1].find_elements(By.XPATH, "./descendant::a")

            for child in children:
                #me quedo con la url
                href_value = child.get_attribute('href')
                nombre_indicador = re.search(r'indicator/(.*?)\?view=chart', href_value).group(1)

                # Extrae el texto visible del enlace
                
                titulo_indicador = child.text
                #print(f"Tag: {child.tag_name}, Texto: {child.text}, Atributos: {child.get_attribute('outerHTML')}")
                print(f"###Titulo: {titulo_seccion}text: {child.text},href:{child.get_attribute('href')}")
                
                writer.writerow([titulo_seccion, nombre_indicador, titulo_indicador, 'pendiente', href_value ])
    # Cierra el navegador
    driver.quit()


#recorrer_datasets("https://data.worldbank.org/indicator?tab=all")
download_from_excel('/Users/miguelkiszkurno/Documents/TT1/resultados.csv')

