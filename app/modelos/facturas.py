from pydantic import BaseModel
from app.modelos.transacciones import Transaccion


class FacturaBase(BaseModel):
    cliente_id: int
    valor: float


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None
    transacciones: list[Transaccion] = []