from pydantic import BaseModel
from .clientes import Cliente

# El decorador @property proviene de Python y sirve para convertir un método de una clase en una propiedad de solo lectura.
# Validación Pydantic v2, @computed_field es un decorador que te permite definir propiedades o métodos que se calculan dinámicamente a partir de otros campos y se incluyen automáticamente en la respuesta JSON de tu API.
# getattr() es una función nativa de Python. Sirve para obtener el valor de un atributo o propiedad de un objeto de forma dinámica.

# Crear el modelo transacciones(id, fecha, vr_total, cliente)

class FacturaBase(BaseModel):
    fecha: str
    vr_total: float  # calcular(cantidad * vr_unitario)
    cliente: Cliente  # esta es la relacion con el cliente(objeto)


class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None