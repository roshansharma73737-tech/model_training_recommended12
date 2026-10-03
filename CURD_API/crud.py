from sqlalchemy.orm import Session
from sqlalchemy import  text
import  model , schema


# create the function  of the store the  product  on the server  to create the maintain  the browser  for the user and client---->

def get_product(db:Session  ,   skip:int = 0 , limit:int = 10):
    return db.query(model.product_Model).offset(skip).limit(limit).all()

# create the  off set of the  the unique id of the product on eserver  and maintain the records  in database --->


def get_product(db:Session, product_id: int ):
    return db.query(model.product_Model).filter(model.product_Model.id == product_id).first()

# create the  final product  on the server to show the   as the mysql database  from the
 
def create_product(db:  Session, product:schema.productArea):
    db_product =  model.product_Model(**product.model_dump())
