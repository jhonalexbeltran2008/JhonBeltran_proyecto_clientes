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
4. Dentro de requirements.txt añadir la siguiente linea: fastapi[standard]>=(Poner aqui la versión de fastapi)

---
# Campos 
1. **Clientes:** {id, nombre, email, descripcion}
2. **Facturas:** {id, fecha, vr_total, cliente}
3. **Transacciones:** {id, cantidad, vr_unitario, id_factura}

---
# EJECUTAR TODO EN MAIN.PY

importar las clases: 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Crear endpointd del proyecto para realizar el CRUD, editando main.py

1. Crear el endpoint listar_clientes, obtener todos los clientes de la lista_clientes.

2. Crear el endpoint listar_cliente, obtener un solo cliente de la lista_clientes.
   NOTA: Tener en cuenta el typing o tipado de datos
   
3. Crear el endpoint crear_clientes, enviar datos del cliente y guardarlos en la lista_clientes.
   NOTA: Tener en cuenta el typing o tipado de datos - para la lista_clientes y el modelo que se construira.

4. Crear una **clase o modelo** llamado `Clientes` como se indica en la linea 13 de este archivo.

5. Editar la lista_clientes aplicando typing.

6. Editar el endpoint crear_clientes aplicando typing.

7. Comprobar el funcionamiento de crear_clientes.

NOTA: El ID debe generarse automaticamente en la base de datos, pero como estamos simulando una debemos implementar codigo python, que lo realizaremos mas adelante.

---

# Organizar los modelos, y así editar también la solicitud y respuesta de nuestros endpoint.

1. Editamos la respuesta (response) de la solicitud (GET y POST) de los endpoint, para definir el esquema de los datos que el servidor enviará al cliente.

2. En proyectos, pueden existir muchos modelos.
Opción 1: Podemos crear un solo archivo, y crear los modelos (clientes, facturas, transacciones).
Opción 2: Crear una carpeta modelos, y un archivo diferente (clientes, facturas, transacciones).

- Crear carpeta llamada modelos
- Dentro de la carpeta modelos crear archivos clientes.py y facturas.py

3. Creado el modelo, se debe separar el id, creando otros modelo para organizar la aplicación (genera seguridad).

---

# Navegar entre commits 

Ejecutar en la consola:

-git status
-git log --oneline
-git branch
-git checkout (Pegar aqui el código de cada commit)
-git switch para deshacer cambios
-git branch por si el primero no mostros HEAD en master.

Para devolverse:

-git checkout master
-git log --oneline

---

# Terminar el CRUD de clientes, crear el endpoint para editar y eliminar clientes.

1. Habilitar la programación asíncrona.
2. El ID debe generarse automáticamente en la base de datos, pero como estamos simulando una BD debemos implementar código Python.
3. Crear el endpoint de editar_cliente, aplicando la seguridad y filtrado anteriormente realizado (esquemas de los modelos).

4. **Como ejercicio** pueden crear el endpoint de eliminar.
=======
4. **Como ejercicio** pueden crear el endpoint de eliminar.
5. Comprobar el funcionamiento de la aplicación, el CRUD completo de clientes.

---

# Crear los endpoint de factura y transacciones vacios

**Como ejercicio** pueden crear los endpoint y realizar el CRUD para `facturas` y `transacciones`, al inicio sin validar, para que funcione y desarrollen la apliación; porque hay que tener encuenta la siguiente NOTA.

**NOTA:** Como estamos simulando una BD, recordar las relaciones:

1. `1` cliente puede tener `0` o `n` facturas
2. `1` factura puede tener o pertenecer a `1` cliente
3. `1` factura puede tener `0` o `n` transacciones
4. `1` transaccion puede pertenecer a `1` factura.

Deben validar cada registro, como por ejemplo no se puede agregar una nueva factura si no existe un cliente.

---

# Editar el endpoint listar facturas, listar una factura según el modelo.

**NOTA:**Editar manejo de excepciones.

1. Editar el endpoint listar_facturas, todas las facturas.
2. Editar el endpoint listar_factura, una factura.
3. Comprobar funcionamiento.

---

# Editar el endpoint crear factura, según el modelo

1. Editar el endpoint crear factura
2. Comprobar el funcionamiento

---

# Editar el endpoint crear factura, según el modelo - Continuación

1. Edición del método vr_total del modelo facturas, para que haga el cálculo a las transacciones que pertenecen a esa factura.
   Para comprobar el funcionamiento del método vr_total debemos:
2. Editar endpoint de crear transacciones, también puede editar el de listar todas las transacciones.
3. Comprobar funcionamiento

*Ejercicio Terminar, los endpoint de modificar y eliminar**

---

# Estructurar el proyecto

proyecto_clientes/ <- Carpeta Raiz
├── app/ <- Carpeta principal de la aplicación
│   ├── __init__.py <- Archivo vacío para que Python reconozca el módulo
│   ├── main.py <- Punto de entrada de la API
│   ├── conexion_bd.py <- Configuración de la conexión a la base de datos
│   ├── modelos/ <- Carpeta para los modelos de Base de Datos (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   └── enrutador/ <- Carpeta para los endpoints o rutas (APIRouter)
│       ├── __init__.py
│       ├── clientes.py
│       └── facturas.py
├── .mi_env <- Entorno virtual
├── requirements.txt <- Dependencias del proyecto, si es con uv pyproject.toml
└── README.md <- Documentación de nuestro proceso en el desarrollo del proyecto.

---

# Manejo de Enrutadores o Routers

1. Editar los archivos de la carpeta enrutador (instanciar la clase ROUTER)
2. Cortar el código de las rutas del archivo main.py y copiarlos según corresponda
3. Comprobar las rutas ahora no existen en la UI de Swagger
4. Incluir en main.py las rutas

# Manejo de Enrutadores o Routers

1. Explicación solo con el archivo modelos-enrutadores de transacciones, e importaciones.
2. Comprobar funcionamiento de los endpoint.

---

