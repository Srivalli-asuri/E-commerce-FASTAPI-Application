# CRUD operations for products and users

from sqlalchemy.orm import Session
from app.models import config
from app.schemas import carts
# from Utils.hashing import get_password_hash
from app.core.logging_config import logger
from app.services.Product_Service import get_product_by_id
from app.services.User_Service import get_user_by_id


##################CART##############################

def create_cart(db:Session,cart:carts.CartCreate,user_id:int):
    check= get_user_by_id(db,user_id)
    if not check:
        raise ValueError("No user found. Please register to add items to cart")
    
    prod=get_product_by_id(db,cart.product_id)
    if not prod:
        return "Product not found"
    
    if cart.quantity<=0:
        return "please select the quantity"
    
    if prod.quantity<=cart.quantity:
        return {prod.quantity :"select the qunatity as available"}
    
    total_amount=prod.price*cart.quantity
    prod.quantity=prod.quantity-cart.quantity


    db_cart = config.Cart(
        user_id=user_id,
        product_id=cart.product_id,
        quantity=cart.quantity,
        total_amount_in_rs=total_amount,
        place_order=cart.place_order
    )
    
    if cart.place_order:
        db.add(db_cart)
        db.commit()
        db.refresh(db_cart)
        return {"message": "Order Placed Successfully", "cart_id": db_cart.id}
    else:
        return {"message": "Your order is not yet placed", "cart_id": db_cart.id}




def edit_cart(db: Session, cart: carts.CartCreate, cart_id: int):
    db_cart = db.query(config.Cart).filter(config.Cart.id == cart_id).first()
    if not db_cart:
        return {" you entered Invalid cart id " : {cart_id}}
    product = get_product_by_id(db, db_cart.product_id)
    if not product:
        return {"selected Incorrect Product" : {db_cart.product_id}}

    db_cart.quantity = cart.quantity
    db_cart.total_amount_in_rs = product.price * cart.quantity
    db_cart.place_order = cart.place_order


    db.commit()
    db.refresh(db_cart)
    return db_cart




def delete_cart(db:Session,cart_id:int):
    db_cart=db.query(config.Cart).filter(config.Cart.id==cart_id).first()
    if db_cart:
        db.delete(db_cart)
        return { "cart deleted succesfully": {cart_id}}
    return {"cart not found":{cart_id}}


