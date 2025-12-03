# # Products endpoints with RBAC enforced (admin can add/delete, user can only view)
from fastapi import APIRouter, Depends, HTTPException, Query
from  sqlalchemy.orm import Session

from app.schemas import product
from app.services import Product_Service
from app.db.database import get_db
from app.core.dependencies import get_current_user, require_admin
from app.core.logging_config import logger
from app.models import config

from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
router = APIRouter()

# @router.get("/", response_model=list[product.Product])
# def list_products_with_range(skip: int = 0 , limit: int = Query(default=100, le=1000), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     logger.info(f"User {current_user.username} fetched all products")
#     return Product_Service.get_products(db, skip=skip, limit=limit)

@router.get("/", response_model=Page[product.ProductBase])
def list_users(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    products=db.query(config.Product)
    return paginate(products)

# @router.get("/", response_model=list[schemas.Product])
# def list_products(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     logger.info(f"User {current_user.username} fetched all products")
#     return crud.get_products(db)


@router.post("/", response_model=product.Product)
def add_product(product: product.ProductCreate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f"ADMIN {current_user.username} adding product: {product.name}")
    try:
        logger.info(f"Product created with admin id:{current_user.id} , {current_user.username}")
        return Product_Service.create_product(db, product, owner_id=current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{product_id}", response_model=product.Product)
def get_product(product_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    logger.info(f"{current_user.username} is trying to fetching the product with product id {product_id}")
    p = Product_Service.get_product_by_id(db, product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"user : {current_user.username} is fetching the product with product id {product_id}")
    return p

@router.put("/{product_id}",response_model=product.ProductCreate)
def update_product(product :product.ProductCreate, product_id:int,db:Session=Depends(get_db) ,current_user=Depends(require_admin)):
    logger.info(f"{current_user.username} is trying to update the details of the product")
    exist=Product_Service.get_product_by_id(db,product_id)
    if not exist:
        logger.info(f"{current_user.username} is trying to remove the product which is not present")
        raise HTTPException(status_code=404,detail="product not found")
    logger.info(f" admin : {current_user.username} is updated the product{exist.name} ")
    return Product_Service.update_product(db,product_id,product)
    

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f"{current_user.username} attempts deleting product with id {product_id}")
    success = Product_Service.delete_product(db, product_id)
    if not success:
        logger.warning(f"product deletion Failed {product_id}")
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"admin {current_user.username} is deleted the product {product_id} succesfully")
    return {"detail": "Product deleted"}
