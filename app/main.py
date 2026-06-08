from fastapi import FastAPI
from app.enrutador.clientes import router as router_clientes

app = FastAPI(
    title="API Clientes",
    version="1.0"
)

app.include_router(router_clientes)


@app.get("/")
async def inicio():
    return {"mensaje": "API de Clientes funcionando correctamente"}