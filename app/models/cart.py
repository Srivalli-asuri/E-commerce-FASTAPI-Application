from sqlalchemy import Column,Integer,ForeignKey,Boolean
from app.db.database import Base
from app.models.users import User
from app.models.products import Product

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_amount_in_rs = Column(Integer)
    place_order = Column(Boolean, default=False)
