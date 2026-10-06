from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = 0

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

class ProductOut(ProductCreate):
    id: int
    class Config:
        from_attributes = True   # lets Pydantic read SQLAlchemy objects directly