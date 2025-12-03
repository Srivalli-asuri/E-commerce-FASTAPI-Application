from app.schemas.base_model import Base

############CATEGORIES#########
class CategoryBase(Base):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int