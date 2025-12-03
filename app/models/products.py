from sqlalchemy import Column, String, Text, Integer, ForeignKey
from app.db.database import Base
from app.models.users import User
from app.models.categories import Category
class Product(Base):
    __tablename__ = "products"

    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey(User.id))
    category_id= Column(Integer, ForeignKey(Category.id))
    quantity=Column(Integer,nullable=False)
    price=Column(Integer,nullable=False)