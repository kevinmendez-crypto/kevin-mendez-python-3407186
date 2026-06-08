from fastapi import APIRouter
from app.modelos.facturas import Factura, FacturaCrear

router = APIRouter()

lista_facturas: list[Factura] = []


@router.get("/facturas")
async def listar_facturas():
    return lista_facturas


@router.post("/facturas")
async def crear_factura(datos: FacturaCrear):

    factura = Factura.model_validate(
        datos.model_dump()
    )

    factura.id = len(lista_facturas) + 1

    lista_facturas.append(factura)

    return factura