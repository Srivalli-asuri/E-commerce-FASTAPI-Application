from app.schemas.base_model import Base

########### Users #########
class UserBase(Base):
    username: str

class UserCreate(UserBase):
    password: str
    role: str="user"

class User(UserBase):
    id: int
    
    role: str



    # class Config:
    #     orm_mode = True

# from pydantic import BaseModel

# ########### Users #########
# class UserBase(BaseModel):
#     username: str

# class UserCreate(UserBase):
#     password: str
#     role: str = "user"

# class User(UserBase):
#     id: int
#     role: str

#     class Config:
#         orm_mode = True  # Needed to convert SQLAlchemy model to Pydantic schema
