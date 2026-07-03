from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear

app = FastAPI()



lista_clientes:list[Cliente] = []



#endpoint para obtener o listar todos los clientes

@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes

#endpoint para obtener o listar un solo cliente de la lista

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_clientes(cliente_id: int):
    
    #recorrer lista clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente

#endpoint para listar un cliente y agregar a la lista

@app.post("/clientes", response_model=Cliente)
def crear_clientes(datos_cliente: ClienteCrear):
    Cliente.val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(Cliente.val)
    return Cliente.val