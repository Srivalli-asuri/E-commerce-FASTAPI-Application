# User registration and authentication endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import user,token
from app.services import User_Service
from app.db.database import get_db
from app.Utils.jwt import create_access_token
from app.Utils.hashing import verify_password
from app.core.logging_config import logger
from app.core.dependencies import get_current_user
router =APIRouter()

from fastapi_pagination import Page, paginate



@router.post("/register", response_model=user.User)
def register_user(user: user.UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Registration attempt: {user.username}")

    db_user = User_Service.get_user_by_username(db, user.username)
    if db_user:
        logger.warning(f"Registration failed. Username already exists: {user.username}")
        raise HTTPException(status_code=400, detail="Username already registered")
    # Use role from user input
    created=User_Service.create_user(db, user, role=user.role)
    logger.info(f"User registered successfully: {user.username} with role {user.role}")
    return created


@router.post("/login", response_model=token.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    logger.info(f"Login attempt: {form_data.username}")
    user = User_Service.get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        logger.warning(f"Login failed — user not found: {form_data.username}")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    logger.info(f"Login successful: {user.username} (role={user.role})")
    return {"access_token": access_token, "token_type": "bearer"}





@router.get("/me")
def current_user(user:user.User =Depends(get_current_user)):
    return user

