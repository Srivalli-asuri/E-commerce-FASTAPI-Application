# Pydantic schemas for request and response validation

from app.schemas.base_model import Base

####### Products ############

class ProductBase(Base):
    name: str
    description: str
    category_id:int
    quantity:int
    price:int
    

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    owner_id: int