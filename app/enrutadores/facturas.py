from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaBase, FacturaCrear, FacturaEditar, FacturaLeer, FacturaLeerCompuesta
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas
from ..conexion_db import Sesion_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()

#lista_clientes:list[Cliente] = []
#lista_facturas:list[Factura] = []


# crear los endpoint para facturas

# endpoint listar todas las facturas

@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: Sesion_dependencia):
    #select * from factura
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas

# endpoint para obtener o listar una sola factura de la lista

@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int, mi_sesion: Sesion_dependencia):
    # recorrer la lista_facturas
    factura_bd: Factura | None = mi_sesion.get(Factura, factura_id)
    if factura_bd is None:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura coddn id {factura_id}, no existe."
    )
    return factura_bd

# endpoint para crear una factura y agregar a la lista

@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion: Sesion_dependencia):
   #Buscar cliente en bd


    cliente_encontrado = sesion.get(Cliente, cliente_id)
    # Mensaje si no existe el cliente
    if not cliente_encontrado:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {cliente_id}, no existe.")

     #Validar datos de la factura
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
  
   #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val


#endpoint para editar una factura y agregar a la lista

@rutas_facturas.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: FacturaEditar, mi_sesion: Sesion_dependencia):
    factura_bd = mi_sesion.get(Factura, id_factura)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {id_factura}, no existe."
        )
    factura_dict = datos_factura.model_dump(exclude_unset=True)
    factura_bd.sqlmodel_update(factura_dict)
    mi_sesion.add(factura_bd)
    mi_sesion.commit()
    mi_sesion.refresh(factura_bd)
    return factura_bd
# endpoint para eliminar una factura

@rutas_facturas.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int, mi_sesion: Sesion_dependencia):
    pass
    factura_bd = mi_sesion.get(Factura, id_factura)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {id_factura}, no existe."
        )
    mi_sesion.delete(factura_bd)
    mi_sesion.commit()
    return factura_bd