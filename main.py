from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

lista_clientes = [
    {"id": 1, "nombre": "Lady", "email": "lady@gmail.com", "edad": 22, "descripcion": "NA"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "edad": 19, "descripcion": "NA"},
    {"id": 3, "nombre": "Ana", "email": "ana@gmail.com", "edad": 23, "descripcion": "NA"},
]

#endpoint para obtener o listar todos los clientes

@app.get("/clientes")
def listar_clientes():
    return lista_clientes

#endpoint para obtener o listar un solo cliente de la lista

@app.get("/clientes/{cliente_id}")
def listar_clientes(cliente_id: int):
    
    #recorrer lista clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

