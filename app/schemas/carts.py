from app.schemas.base_model import Base
#########CART########

class CartBase(Base):
    
    # product_id:int
    quantity:int
    place_order:bool

class CartCreate(CartBase):
    product_id:int
    pass
    
class Cart(CartCreate):
    id:int