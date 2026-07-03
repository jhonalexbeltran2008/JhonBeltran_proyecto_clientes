from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar, ClienteEliminar

app = FastAPI()



lista_clientes:list[Cliente] = []



#endpoint para obtener o listar todos los clientes

@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

#endpoint para obtener o listar un solo cliente de la lista

@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_clientes(cliente_id: int):
    
    #recorrer lista clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente

#endpoint para listar un cliente y agregar a la lista

@app.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
  #generar id 
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

#endpoint para editar un cliente y agregar a la lista

@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return cliente_val
    raise HTTPException(
        status_code=40, detail=f"El cliente con id {cliente_id} no existe."
    )

# endpoint para eliminar un cliente


@app.delete("/clientes/{cliente_id}", response_model=ClienteEliminar)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            lista_clientes.pop(i)
            return ClienteEliminar(id=cliente_id, detail="Cliente eliminado correctamente.")
    raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id} no existe."
    )