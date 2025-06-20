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
