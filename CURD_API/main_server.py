from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)   # auto-creates the table if missing

app = FastAPI(title="Store API with MySQL")

@app.post("/products", response_model=schemas.ProductOut, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products", response_model=List[schemas.ProductOut])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip, limit)

@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_one_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.patch("/products/{product_id}", response_model=schemas.ProductOut)
def patch_product(product_id: int, changes: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = crud.update_product(db, product_id, changes)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/products/{product_id}", status_code=204)
def remove_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

@app.get("/reports/low-stock")
def low_stock(threshold: int = 10, db: Session = Depends(get_db)):
    return crud.low_stock_products(db, threshold)