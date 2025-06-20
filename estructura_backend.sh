#!/bin/bash
# filepath: /home/yolotl/proyectoIntegrador/pos-mariscos/estructura_backend.sh

# Crear carpetas si no existen
mkdir -p backend/models
mkdir -p backend/schemas
mkdir -p backend/crud
mkdir -p backend/routes
mkdir -p backend/utils

# Crear archivo de dependencia de sesión
cat <<EOF > backend/deps.py
from backend.database import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
EOF

# Crear plantilla de modelo Product
cat <<EOF > backend/models/product.py
from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255))
EOF

# Crear plantilla de modelo Order
cat <<EOF > backend/models/order.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Float, nullable=False)
    status = Column(String(50), default="pendiente")
    user = relationship("User")
EOF

# Crear esquema Pydantic para Product
cat <<EOF > backend/schemas/product.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str = ""

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True
EOF

# Crear esquema Pydantic para Order
cat <<EOF > backend/schemas/order.py
from pydantic import BaseModel

class OrderBase(BaseModel):
    total: float
    status: str = "pendiente"

class OrderCreate(OrderBase):
    user_id: int

class OrderOut(OrderBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
EOF

# Crear esquema Pydantic para User (si no existe)
cat <<EOF > backend/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
EOF

# Crear CRUD básico para Product
cat <<EOF > backend/crud/product.py
from sqlalchemy.orm import Session
from backend.models.product import Product
from backend.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()
EOF

# Crear CRUD básico para Order
cat <<EOF > backend/crud/order.py
from sqlalchemy.orm import Session
from backend.models.order import Order
from backend.schemas.order import OrderCreate

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()
EOF

# Crear CRUD básico para User
cat <<EOF > backend/crud/user.py
from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
EOF

echo "Estructura y archivos base creados. ¡Listo para migrar tu backend a MariaDB!"