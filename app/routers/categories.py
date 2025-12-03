# routers/categories.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas import category
from app.services import Categories_Service
from app.db.database import get_db
from app.core.dependencies import get_current_user, require_admin
from app.core.logging_config import logger
router = APIRouter()


@router.get("/", response_model=list[category.Category])
def list_categories( db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    logger.info(f" admin {current_user.username} is fetching all the categories")
    return Categories_Service.get_categories(db)

@router.post("/", response_model=category.Category)
def create_category(category: category.CategoryCreate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f"admin {current_user.username} is added new category")
    return Categories_Service.create_category(db, category)

@router.put("/{category_id}", response_model=category.Category)
def update_category(category_id: int, payload: category.CategoryCreate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f"{current_user.username} is trying to update the category with {category_id}")
    updated = Categories_Service.update_category(db, category_id, payload.name)
    if not updated:
        logger.warning(f"{current_user.username} is trying to update the category with {category_id} which is not found")
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f" admin {current_user.username} is trying to delete the category with id: {category_id}")
    ok = Categories_Service.delete_category(db, category_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"detail": "Category deleted"}