from pydantic import BaseModel
from typing import Optional



class  productArea(BaseModel):
    name: str
    price:float
    stock: int = 0 

class productUpdate(  BaseModel):
    name: Optional[str] = None
    price : Optional[float] = None
    stock : Optional[int] = None

class productOut(productArea):
    id : int 
    class config :
        from_attributes = True 
