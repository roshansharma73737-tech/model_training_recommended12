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
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# update the product no the  sever   to database   changes --->

def update_product(db:Session, product_id:int , changes: schema.productUpdate):
    db_product = get_product(db,product_id)
    if not db_product :
        return None
    for field ,value in changes.model_dump(exclude_unset=True).items():
        setattr(db_product ,field,value)

    db.commit()
    db.refresh(db_product)
    return  db_product
 
# delete the product   on the server as the like operation   to remove the  items on the server  --->

def delete_product(db:Session , product_id:int ):
    db_product = get_product(db ,product_id)
    if not db_product:
        return  None
    db.delete(db_product)
    db.commit()
    return  db_product



def  low_stock_product(db:Session, threshold: int = 10):
    result = db.execute(
        text("SELECT * FROM produts WHERE  stock  <:threshold ORDER BY stock ASC"),
        {"threshold": threshold},
    )
    return result.mappings().all()