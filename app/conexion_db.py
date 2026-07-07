from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine

nombre_bd = f"bd_clientes.sqlite3"
Url_bd = f"sqlite:///{nombre_bd}"

#motor de bd
motor_bd = create_engine(Url_bd)

#definir el metodo para crear las tablas

def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield #no hay nada para retornar o ejecutar

#definir el metodo para la sesion
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion #retorna la sesion

#Denominado inyeccion de dependencias

#registrar la sesion como dependencia, utilizada en nuestro endpoint
Sesion_dependencia = Annotated[Session, Depends(obtener_sesion)]