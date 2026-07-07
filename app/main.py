from fastapi import FastAPI, HTTPException, status
from app.enrutadores.clientes import rutas_clientes
from app.enrutadores.facturas import rutas_facturas
from app.enrutadores.transacciones import rutas_transacciones

app = FastAPI()


#Incluir ruta clientes
app.include_router(rutas_clientes, tags=["Clientes"])
app.include_router(rutas_facturas, tags=["Facturas"])
app.include_router(rutas_transacciones, tags=["Transacciones"])
