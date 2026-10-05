from  fastapi import FastAPI , Depends , HTTPException    # import main things  depend and http httpexception  for the  show th error 
from sqlalchemy.orm import Session    # import the  Session  for theactive the session  until  user or clents is  out of the api  
from typing import List  


import model ,schema ,crud   #  for the  crud operatoins in the  main server  to create the sever 
from database import engine , get_db   # import the engin for the  as for the connection establish  between  file sever and   mysql  database



model.base.metadata.create_all(blind =  engine)
app =  FastAPI (title =' Product_management')

@app.post("/products", response_model= schema.productOut, status_code= 201)
def create_product(product :  schema.productArea, db :Session    =  Depends(get_db)):
    return  crud.create_product(db,product)

@app.get("/product",response_model= List[schema.productArea])
def list_product(skip: int= 0, limit: int = 10, db:Session = Depends(get_db)) :
    return  crud.get_product(db , skip, limit)




@app.get("/products/{product_id}", response_model=schema.productOut)
def get_one_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.patch("/products/{product_id}", response_model=  schema.productOut)
def  patch_product(product_id :int, change :schema.productUpdate, db :Session = Depends(get_db)):
    product =  crud.get_product(db,  product_id)
    if not product: raise HTTPException(status_code= 404 , details= " Product is not founded " )
    return  product 

@app.delete("/products/{product_id}" , response_model=  schema.productOut)
def remove_product( product_id: int , db:Session = Depends(get_db)):
    product =  crud.delete_product(db, product_id)
    if not product :
        raise HTTPException(status_code= 404 , detail= " produc is not founded ")
@app.get("/reports/theshold_low_stock", )
def low_stock(threshold : int =  10  , db :Session   = Depends(get_db)):
    return   crud.low_stock_product(db,  threshold)