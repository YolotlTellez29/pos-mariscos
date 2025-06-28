from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from backend.database import Base, engine
from backend.schemas.user import UserCreate, UserLogin, UserOut
from backend.schemas.order import OrderCreate, OrderOut
from backend.crud.user import create_user, get_user_by_email
from backend.crud.order import create_order
from backend.deps import get_db
from passlib.context import CryptContext
from backend.utils.jwt_handler import create_access_token
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return create_user(db, user)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not db_user.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    # Genera el token JWT
    token = create_access_token({"sub": db_user.email, "role": db_user.role, "user_id": db_user.id})
    return {
        "msg": "Login exitoso",
        "user_id": db_user.id,
        "role": db_user.role,
        "access_token": token
    }

# --- Endpoint para crear pedidos ---
@app.post("/orden", response_model=OrderOut)
def crear_orden(order: OrderCreate, authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    # Validar JWT
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No autorizado")
    from jose import JWTError, jwt
    from backend.utils.jwt_handler import SECRET_KEY, ALGORITHM
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    # Crear el pedido
    db_order = create_order(db, order)
    return db_order