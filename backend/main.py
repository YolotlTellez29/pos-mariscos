from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import Base, engine
from backend.schemas.user import UserCreate, UserLogin, UserOut
from backend.crud.user import create_user, get_user_by_email
from backend.deps import get_db
from passlib.context import CryptContext

# It's better to define CryptContext once, globally, if possible,
# or at least outside the function for performance.
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

    # Prints temporales para depuración
    print("db_user:", db_user)
    print("type(db_user):", type(db_user))
    if db_user:
        print("db_user.password:", db_user.password)
        print("type(db_user.password):", type(db_user.password))

    # Combined and improved check for db_user and its password
    if not db_user or not hasattr(db_user, "password") or not isinstance(db_user.password, str) or not db_user.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    if not user.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    try:
        if not pwd_context.verify(user.password, db_user.password):
            raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    except Exception:
        # Catch any unexpected errors during password verification
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    return {
        "msg": "Login exitoso",
        "user_id": db_user.id,
        "role": db_user.role
    }