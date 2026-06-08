from fastapi import APIRouter
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar

router = APIRouter()

lista_clientes: list[Cliente] = []


@router.get("/clientes")
async def listar_clientes():

    if len(lista_clientes) == 0:
        return {"mensaje": "No hay clientes registrados"}

    return {"clientes": lista_clientes}


@router.get("/clientes/{id}")
async def listar_cliente(id: int):

    for cliente in lista_clientes:

        if cliente.id == id:
            return cliente

    return {"mensaje": "Cliente no encontrado"}


@router.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val = Cliente.model_validate(
        datos_cliente.model_dump()
    )

    cliente_val.id = len(lista_clientes) + 1

    lista_clientes.append(cliente_val)

    return cliente_val


@router.put("/clientes/{id}")
async def editar_cliente(
    id: int,
    datos_cliente: ClienteEditar
):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            cliente_editado = Cliente.model_validate(
                datos_cliente.model_dump()
            )

            cliente_editado.id = id

            lista_clientes[i] = cliente_editado

            return {
                "mensaje": "Cliente actualizado",
                "cliente": cliente_editado
            }

    return {"mensaje": "Cliente no encontrado"}


@router.delete("/clientes/{id}")
async def eliminar_cliente(id: int):

    for cliente in lista_clientes:

        if cliente.id == id:

            lista_clientes.remove(cliente)

            return {
                "mensaje": "Cliente eliminado"
            }

    return {"mensaje": "Cliente no encontrado"}