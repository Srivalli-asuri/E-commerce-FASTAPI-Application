from sqlalchemy import Column, Integer, String,Boolean
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String, default="user")  # 'admin' or 'user'
    deleted=Column(Boolean,default=False)