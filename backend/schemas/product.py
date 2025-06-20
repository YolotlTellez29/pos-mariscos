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
