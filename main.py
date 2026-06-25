from fastapi import FastAPI

cliente = FastAPI()

@cliente.get("/")
def inicio():
    return{"Mensaje"}
