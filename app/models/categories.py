from app.db.database import Base
from sqlalchemy import Column,Integer,String


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    # One-to-many: category -> products
   