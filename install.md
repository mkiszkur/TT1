# Configuración de Ambiente Virtual para Proyecto de especializacion


1. **Crear el Ambiente Virtual**: Abre una terminal y navega hasta la carpeta de tu proyecto:
   ```bash
   cd /ruta/a/tu/proyecto

   Luego, crea el ambiente virtual en la carpeta del proyecto:
   python3 -m venv especializacion_env


2.	**Activar el Ambiente Virtual**: Activa el ambiente virtual con el siguiente comando:
source especializacion_env/bin/activate

Verifica que el ambiente está activado. Deberías ver el nombre (especializacion) al inicio de la línea en la terminal.


3.	**Instalar ipykernel en el Ambiente Virtual**: Con el ambiente virtual activado, instala ipykernel para poder usar el ambiente virtual como kernel en Jupyter:
    pip install ipykernel

4.	**Registrar el Kernel en Jupyter**: Ejecuta el siguiente comando para registrar el ambiente virtual como un kernel disponible en Jupyter:
python -m ipykernel install --user --name=especializacion_env --display-name "Python (especializacion_env)"
Aquí, "especializacion" es el identificador del kernel (puedes elegir otro nombre si prefieres) y "Python (especializacion_env)" es el nombre que aparecerá en VS Code para este kernel.

5.	**Abrir VS Code y Seleccionar el Kernel en el Notebook**: Abre VS Code y navega hasta la carpeta de tu proyecto. Luego abre tu archivo de notebook (.ipynb) en VS Code. En la esquina superior derecha del notebook, verás un botón que muestra el kernel actual (como "Python 3.x" o "Python (especializacion_env)"). Haz clic en ese botón para abrir el menú de selección de kernel y, en la lista de opciones, selecciona "Python (especializacion_env)" o el nombre que le diste al kernel al registrarlo.
	
6.	**Verificar que el Kernel es Correcto**: Para confirmar que el notebook está usando el ambiente virtual correcto, ejecuta la siguiente celda en el notebook:
import sys
print(sys.executable)
Si el ambiente virtual está activo, el resultado debería mostrar la ruta dentro de la carpeta especializacion de tu proyecto.

Con estos pasos, el ambiente virtual estará configurado como kernel en VS Code, permitiéndote trabajar en tus notebooks con las librerías específicas de tu proyecto.


7.	**Generar un archivo requirements.txt**: Una vez que hayas instalado todas las librerías necesarias en tu ambiente virtual, puedes generar un archivo requirements.txt para registrar esas dependencias. Esto permite que otras personas (o tú mismo en otro equipo) puedan instalar las mismas versiones de librerías. Con el ambiente virtual activado, ejecuta:
pip freeze > requirements.txt

8.	**Instalar Dependencias desde requirements.txt**: Si necesitas instalar todas las dependencias en otro ambiente virtual o en otra computadora, puedes usar el archivo requirements.txt generado. Activa el ambiente virtual donde deseas instalar las dependencias y ejecuta:
pip install -r requirements.txt

9.	Verificar que el Kernel es Correcto: Para confirmar que el notebook está usando el ambiente virtual correcto, ejecuta la siguiente celda en el notebook:
import sys
print(sys.executable)
