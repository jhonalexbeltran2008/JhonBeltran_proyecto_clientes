from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime

# El decorador @property proviene de Python y sirve para convertir un método de una clase en una propiedad de solo lectura.
# Validación Pydantic v2, @computed_field es un decorador que te permite definir propiedades o métodos que se calculan dinámicamente a partir de otros campos y se incluyen automáticamente en la respuesta JSON de tu API.
# getattr() es una función nativa de Python. Sirve para obtener el valor de un atributo o propiedad de un objeto de forma dinámica.

# Crear el modelo transacciones(id, fecha, vr_total, cliente)

class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente  # esta es la relacion con el cliente(objeto)
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular(Cantidad * vr_unitario)
        #consultar el id actual de la factura
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
             return total_factura
        #recorrer la lista de transacciones, segun el factura_id
        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad

        return total_factura
    
class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None