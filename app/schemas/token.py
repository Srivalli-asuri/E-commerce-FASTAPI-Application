from app.schemas.base_model import Base

######### TOKEN #########

class Token(Base):
    access_token: str
    token_type: str

class TokenData(Base):
    username: str | None = None
    role: str | None = None
