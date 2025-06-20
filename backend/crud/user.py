from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        return None  # or raise an exception, or handle it in some way
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
