# CRUD operations for products and users

from sqlalchemy.orm import Session
from app.models import config
from app.schemas import product


from app.services.Categories_Service import get_category_by_id
from app.Utils.hashing  import get_password_hash
from app.core.logging_config import logger

###################  PRODUCTS  ################################

# def get_products(db: Session, skip: int = 0, limit: int | None = None):    
#     q = db.query(config.Product).offset(skip)
#     if limit:
#         q = q.limit(limit)
#     return q.all()

# def get_products(db: Session):
#     return db.query(config.Product)

def get_products(db: Session):
    logger.info("Fetching the data from the database")
    return db.query(config.Product).all()

def create_product(db: Session, product: product.ProductCreate, owner_id: int):

    # checking category exists
    category = get_category_by_id(db, product.category_id)
    if not category:
        raise ValueError("Category not found")
    #.......
    db_product = config.Product(**product.model_dump(), owner_id=owner_id)
    logger.info(f"Admin : {owner_id} created product {db_product}")
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_by_id(db: Session, product_id: int):
    return db.query(config.Product).filter(config.Product.id == product_id).first()


def update_product(db: Session, product_id: int,product:product.ProductCreate):
    prod = get_product_by_id(db, product_id)
    if not prod:
        return None
    prod.name=product.name
    prod.description=product.description
    prod.category_id=product.category_id
    db.commit()
    db.refresh(prod)
    return prod


def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    return False
