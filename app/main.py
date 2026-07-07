from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar, eliminar_cliente
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from enrutadores import clientes
app = FastAPI()



lista_clientes:list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

#Incluir ruta clientes
app.include_router(clientes.rutas_clientes, tags=["Clientes"])


# crear los endpoint para facturas

# endpoint listar todas las facturas

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

# endpoint para obtener o listar una sola factura de la lista

@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    # recorrer la lista_facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"La factura con id {factura_id}, no existe."
        )


# endpoint para crear una factura y agregar a la lista

@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):
   #Buscar cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
         if cliente.id == cliente.id:
            cliente_encontrado = cliente
    # Mensaje si no existe el cliente
    if not cliente_encontrado:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {cliente_id}, no existe.")

     #Validar datos de la factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    # id de la factura
    factura_val.id = len(lista_facturas) + 1
    lista_facturas.append(factura_val)
    return factura_val


#endpoint para editar una factura y agregar a la lista

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

# endpoint para eliminar una factura

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass

# crear los endpoint para transacciones

# endpoint listar todas las transacciones
@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

# endpoint para obtener o listar una sola transaccion de la lista
@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass

# endpoint para crear una transaccion y agregar a la lista
@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):
    #Buscar factura
    factura_encontrada = None
    for factura in lista_facturas:
         if factura.id == factura_id:
            factura_encontrada = factura
    # Mensaje si no existe la factura
    if not factura_encontrada:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe.")


     #Validar datos de la transaccion
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    factura_encontrada.transacciones.append(transaccion_val)

    # id de la transaccion
    transaccion_val.id = len(lista_transacciones) + 1
    # falto agregar a la lista de transacciones
    lista_transacciones.append(transaccion_val)
    return transaccion_val


#endpoint para editar una transaccion y agregar a la lista
@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass

# endpoint para eliminar una transaccion

@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass