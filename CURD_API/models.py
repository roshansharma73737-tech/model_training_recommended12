from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProductModel(Base):
    __tablename__ = "products"        # must match the real table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)