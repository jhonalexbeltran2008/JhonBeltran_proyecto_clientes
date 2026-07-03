# Proyecto: Clientes

# Tecnología: FastAPI

# Datos personales
Jhon Alex Beltran Herrera
Ficha:3407180

# Descripción
Proyecto realizado con FastAPI para mostrar un mensaje principal y una lista de clientes.           
 
# Guia inicial

1. Crear carpeta de proyecto y abrir con VsCode.
2. En la consola de VsCode digitar los siguientes comandos:

-Crear entorno: python -m venv mienv (dos veces)
-Activar entorno: source mienv/Scripts/activate
-Instalar framework fastapi: pip install "fastapi[standard]"
-Ver listado de las instalaciones: pip list

3. Crear Archivo main.py.
4. Dentro de main.py importar la clase: 

from fastapi import FastAPI

5. Crear aplicación.

app = FastAPI()

6. Crear endpoint.

-Crear decorador: @app.get("/")

-Definir función:
def inicio():
    return{"Mensaje:Hola"}

7. Ejecutar modo de desarollo en la consola:

fastapi dev main.py

8. Ver documentación intercativa:

SERVER  http://127.0.0.1:8000
Int. Gráfica  http://127.0.0.1:8000/docs 

---

1. Añadir el documento de texto requeriments.txt
2. Usar en la consola el comando pip list para ver el listado de las instalaciones con sus respectivas versiones
3. Buscar la version de fastapi 
4. Dentro de requeriments.txt añadir la siguiente linea: fastapi[standard]>=(Poner aqui la versión de fastapi)
