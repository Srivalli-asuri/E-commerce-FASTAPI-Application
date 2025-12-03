# CRUD operations for products and users

from sqlalchemy.orm import Session
from app.models import config
from app.schemas import category
from  app.Utils.hashing import get_password_hash
from app.core.logging_config import logger

######################CATEGORIES####################

def get_categories(db: Session):
    # q = db.query(models.Category).offset(skip)
    # if limit:
    #     q = q.limit(limit)
    return db.query(config.Category).all()
# def get_categories(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Category).offset(skip).limit(limit).all()
# def get_all(db:Session):
#     return db.query(models.Product).all()

def create_category(db: Session, category: category.CategoryCreate):
    db_cat = config.Category(**category.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def get_category_by_id(db: Session, category_id: int):
    return db.query(config.Category).filter(config.Category.id == category_id).first()

def update_category(db: Session, category_id: int, new_name: str):
    cat = get_category_by_id(db, category_id)
    if not cat:
        return None
    cat.name = new_name
    db.commit()
    db.refresh(cat)
    return cat


def delete_category(db: Session, category_id: int):
    cat = get_category_by_id(db, category_id)
    if not cat:
        return False
    db.delete(cat)
    db.commit()
    return True
