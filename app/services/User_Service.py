from sqlalchemy.orm import Session
from app.models import config
from app.schemas import user
from app.Utils.hashing import get_password_hash
from app.core.logging_config import logger
# from fastapi_pagination import Page, add_pagination, paginate 

##################USERS###########################
def create_user(db: Session, user: user.UserCreate, role: str = "user"):
    hashed_password = get_password_hash(user.password)
    db_user = config.User(username=user.username, hashed_password=hashed_password, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def get_users(db: Session):
#     return db.query(config.User)


def get_users(db: Session, skip: int = 0, limit: int | None = None):
    q = db.query(config.User).offset(skip)
    if limit:
        q = q.limit(limit)
    return q.all()
    

def get_user_by_username(db: Session, username: str):
    return db.query(config.User).filter(config.User.username == username).first()

def get_user_by_id(db:Session,user_id:int):
    return db.query(config.User).filter(config.User.id==user_id).first()

def update_users(db:Session,user_id:int,role:str):
    user=get_user_by_id(db,user_id)
    if not user:
        return "user doesnt exists"
    user.role=role
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int, hard_delete: bool = False):
    user = get_user_by_id(db, user_id)
    if not user:
        return False
    if hard_delete:
        db.delete(user)
    else:
        user.deleted=True
        # simple soft-delete: set username to deleted_... and role to 'deleted'
        # user.username = f"deleted_{user.id}_{user.username}"
        # user.role = "deleted"
    db.commit()
    return True