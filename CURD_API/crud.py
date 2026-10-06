from sqlalchemy.orm import Session
from sqlalchemy import text
import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ProductModel).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)          # loads the auto-generated id back
    return db_product

def update_product(db: Session, product_id: int, changes: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for field, value in changes.model_dump(exclude_unset=True).items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product

# --- Example of a RAW SQL query (when the ORM isn't enough) ---
def low_stock_products(db: Session, threshold: int = 10):
    result = db.execute(
        text("SELECT * FROM products WHERE stock < :threshold ORDER BY stock ASC"),
        {"threshold": threshold},
    )
    return result.mappings().all()