from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..listas import lista_facturas, lista_transacciones
from ..conexion_db import Sesion_dependencia
from sqlmodel import select
rutas_transacciones = APIRouter()


#lista_facturas: list[Factura] = []
#lista_transacciones: list[Transaccion] = []



# crear los endpoint para transacciones

# endpoint listar todas las transacciones
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion : Sesion_dependencia):
    #consulta = select(Transaccion)
    #lista_transacciones = sesion.exec(consulta).all(#)
    #return lista_transacciones
    return sesion.exec(select(Transaccion)).all()

# endpoint para obtener o listar una sola transaccion de la lista
@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int, mi_sesion: Sesion_dependencia):
    transaccion_bd = mi_sesion.get(Transaccion, id_transaccion)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {id_transaccion}, no existe."
        )
    return transaccion_bd

# endpoint para crear una transaccion y agregar a la lista
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear, sesion: Sesion_dependencia):
    #Buscar factura
    factura_encontrada = sesion.get(Factura, factura_id)
    # Mensaje si no existe la factura
    if not factura_encontrada:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe.")


     #Validar datos de la transaccion
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)
    #guardar en bd
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val

    # id de la transaccion
    transaccion_val.id = len(lista_transacciones) + 1
    # falto agregar a la lista de transacciones
    lista_transacciones.append(transaccion_val)
    return transaccion_val


#endpoint para editar una transaccion y agregar a la lista
@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: TransaccionEditar, mi_sesion: Sesion_dependencia):
    transaccion_bd = mi_sesion.get(Transaccion, id_transaccion)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {id_transaccion}, no existe."
        )
    transaccion_dict = datos_transaccion.model_dump(exclude_unset=True)
    transaccion_bd.sqlmodel_update(transaccion_dict)
    mi_sesion.add(transaccion_bd)
    mi_sesion.commit()
    mi_sesion.refresh(transaccion_bd)
    return transaccion_bd

# endpoint para eliminar una transaccion

@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int, mi_sesion: Sesion_dependencia):
    transaccion_bd = mi_sesion.get(Transaccion, id_transaccion)
    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transacción con id {id_transaccion}, no existe."
        )
    mi_sesion.delete(transaccion_bd)
    mi_sesion.commit()
    return transaccion_bd