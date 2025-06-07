from fastapi import APIRouter, HTTPException
from backend.models.user import UserLogin
from backend.database import db
from passlib.hash import bcrypt
from backend.utils.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")
def login(user: UserLogin):
    print(f"Intentando login para: {user.email}")
    user_in_db = db.users.find_one({"email": user.email})
    
    if not user_in_db:
        print("Usuario no encontrado en la base de datos.")
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    print("Usuario encontrado. Validando contraseña...")

    stored_hash = user_in_db.get("password")
    if not stored_hash:
        print("Campo 'password' no encontrado en el documento.")
        raise HTTPException(status_code=500, detail="Error interno: sin contraseña almacenada")

    try:
        if not bcrypt.verify(user.password, stored_hash):
            print("Contraseña incorrecta.")
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    except Exception as e:
        print(f"Error al verificar contraseña: {e}")
        raise HTTPException(status_code=500, detail="Error interno al verificar contraseña")
    
    print("Contraseña válida. Generando token...")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
