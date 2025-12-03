from app.services import Cart_Service
from app.schemas import carts
from app.core.dependencies import get_current_user
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import session
from app.db.database import get_db



router=APIRouter()


@router.post("/add_to_cart" )
def add_to_cart(cart : carts.CartCreate, db:session=Depends(get_db),current_user=Depends(get_current_user)):
    if not current_user:
        return "user not found"
    return Cart_Service.create_cart(db,cart,current_user.id)


@router.put("/edit_cart{cart_id}")
def add_to_cart(cart_id:int ,cart : carts.CartCreate, db:session=Depends(get_db),current_user=Depends(get_current_user)):
    if not cart_id:
        return "cart not found"
    return Cart_Service.edit_cart(db,cart,cart_id)


@router.delete("/delete_cart{cart_id}")
def delete_Cart(cart_id:int , db:session=Depends(get_db),current_user=Depends(get_current_user)):
    return Cart_Service.delete_cart(db,cart_id)