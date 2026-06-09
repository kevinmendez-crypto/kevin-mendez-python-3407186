from fastapi import APIRouter
from app.enrutador.facturas import lista_facturas
from app.modelos.transacciones import (
    Transaccion,
    TransaccionCrear,
    TransaccionEditar
)

router = APIRouter()

lista_transacciones: list[Transaccion] = []


@router.get("/transacciones")
async def listar_transacciones():

    if len(lista_transacciones) == 0:
        return {"mensaje": "No hay transacciones registradas"}

    return {"transacciones": lista_transacciones}


@router.get("/transacciones/{id}")
async def obtener_transaccion(id: int):

    for transaccion in lista_transacciones:

        if transaccion.id == id:
            return transaccion

    return {"mensaje": "Transacción no encontrada"}


@router.post("/transacciones/{factura_id}")
async def crear_transaccion(
    factura_id: int,
    datos: TransaccionCrear
):

    for factura in lista_facturas:

        if factura.id == factura_id:

            transaccion = Transaccion.model_validate(
                datos.model_dump()
            )

            transaccion.id = len(lista_transacciones) + 1
            transaccion.factura_id = factura_id

            lista_transacciones.append(transaccion)

            factura.transacciones.append(
                transaccion
            )

            return {
                "mensaje": "Transacción agregada a la factura",
                "factura": factura
            }

    return {
        "mensaje": "Factura no encontrada"
    }


@router.put("/transacciones/{id}")
async def editar_transaccion(
    id: int,
    datos: TransaccionEditar
):

    for i, transaccion in enumerate(lista_transacciones):

        if transaccion.id == id:

            transaccion_editada = Transaccion.model_validate(
                datos.model_dump()
            )

            transaccion_editada.id = id

            lista_transacciones[i] = transaccion_editada

            return {
                "mensaje": "Transacción actualizada",
                "transaccion": transaccion_editada
            }

    return {"mensaje": "Transacción no encontrada"}


@router.delete("/transacciones/{id}")
async def eliminar_transaccion(id: int):

    for transaccion in lista_transacciones:

        if transaccion.id == id:

            lista_transacciones.remove(transaccion)

            return {
                "mensaje": "Transacción eliminada"
            }

    return {"mensaje": "Transacción no encontrada"}