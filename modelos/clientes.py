from pydantic import BaseModel

#crear modelo clientes con los campos{id, nombre, email, descripcion}

class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass

class eliminar_cliente(ClienteBase):
    pass
    
class Cliente(ClienteBase):
    id: int | None = None