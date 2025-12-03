# Authentication methods: password hashing, JWT creation/validation
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from app.schemas.token import TokenData
import os
from dotenv import load_dotenv
# SECRET_KEY = "asdfghjkl"  # Load from .env in real projects

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            raise JWTError()
        return TokenData(username=username, role=role)
    except JWTError:
        return None