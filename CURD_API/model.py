from sqlalchemy import column, Integer, String ,Float
from database import Base


class product_Model(Base):
    __tablename__="Products"


    id =  column(Integer, primary_key=True, index =True)
    name =  column(String,(100),  nullable=False)
    price = column(Float, nullable = False)
    stock = column(Integer ,default= 0)

    