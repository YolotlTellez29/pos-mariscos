from fastapi import APIRouter, Depends, HTTPException, Header
from backend.database import db

router = APIRouter()

@router.post("/orden")
def crear_orden(payload: dict, authorization: str = Header(None)):
    # Aquí deberías validar el JWT (no implementado en este ejemplo)
    if not authorization:
        raise HTTPException(status_code=401, detail="No autorizado")
    # Guarda el pedido en la base de datos
    db.pedidos.insert_one(payload)
    return {"msg": "Pedido recibido"}