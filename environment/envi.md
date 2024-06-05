Para crear un archivo de requirements en función de un ambiente virtual en Python, es esencial que primero actives el entorno virtual y luego uses el comando pip freeze para generar una lista de las bibliotecas instaladas junto con sus versiones. Aquí te guío paso a paso:

# Crear y activar el ambiente virtual
Primero, si aún no tienes un ambiente virtual creado, puedes hacerlo usando venv (esto es para usuarios de sistemas basados en Unix como Linux y macOS):

bash
python3 -m venv : /Users/miguelkiszkurno/Documents/GitHub/TT1/environment
Para activar el ambiente virtual en Linux o macOS, usa:

bash
source /Users/miguelkiszkurno/Documents/GitHub/TT1/environment/bin/activate

bash
pip install -r requirements.txt
