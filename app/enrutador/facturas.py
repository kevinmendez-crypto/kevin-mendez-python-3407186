from fastapi import APIRouter
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar

router = APIRouter()

lista_facturas: list[Factura] = []


@router.get("/facturas")
async def listar_facturas():

    if len(lista_facturas) == 0:
        return {"mensaje": "No hay facturas registradas"}

    return {"facturas": lista_facturas}


@router.get("/facturas/{id}")
async def obtener_factura(id: int):

    for factura in lista_facturas:

        if factura.id == id:
            return factura

    return {"mensaje": "Factura no encontrada"}


@router.post("/facturas")
async def crear_factura(datos: FacturaCrear):

    factura = Factura.model_validate(
        datos.model_dump()
    )

    factura.id = len(lista_facturas) + 1

    lista_facturas.append(factura)

    return factura


@router.put("/facturas/{id}")
async def editar_factura(
    id: int,
    datos: FacturaEditar
):

    for i, factura in enumerate(lista_facturas):

        if factura.id == id:

            factura_editada = Factura.model_validate(
                datos.model_dump()
            )

            factura_editada.id = id

            lista_facturas[i] = factura_editada

            return {
                "mensaje": "Factura actualizada",
                "factura": factura_editada
            }

    return {"mensaje": "Factura no encontrada"}


@router.delete("/facturas/{id}")
async def eliminar_factura(id: int):

    for factura in lista_facturas:

        if factura.id == id:

            lista_facturas.remove(factura)

            return {
                "mensaje": "Factura eliminada"
            }

    return {"mensaje": "Factura no encontrada"}