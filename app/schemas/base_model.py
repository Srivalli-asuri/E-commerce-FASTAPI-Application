from pydantic import BaseModel


class Base(BaseModel):
    pass
    
    class Config:
        from_attributes=True
        