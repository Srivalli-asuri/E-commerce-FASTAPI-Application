# routers/admin.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas import user
from app.services import User_Service
from app.db.database import get_db
from app.core.dependencies import require_admin
from app.core.logging_config import logger

from app.models import config
router = APIRouter()

# @router.get("/users", response_model=list[user.User])
# def list_users(skip: int = 0, limit: int = Query(default=100), db: Session = Depends(get_db), current_user=Depends(require_admin)):
#     logger.info(f"admin : {current_user.username} is Fetching all the Users")
    # return User_Service.get_users(db, skip=skip, limit=limit)


from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

@router.get("/users", response_model=Page[user.User])
def list_users(db: Session = Depends(get_db),currrent_user=Depends(require_admin)):
    users=db.query(config.User)
    return paginate(users)


@router.get("/users/{user_id}", response_model=user.User)
def get_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f" admin : {current_user.username} is trying to fetch the users with user_id")
    u = User_Service.get_user_by_id(db, user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return u

@router.put("/users/{user_id}", response_model=user.User)
def update_user_role(user_id: int, payload: dict, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f" admin :{current_user.username} is trying to update the role of {user_id}")
    role = payload.get("role")
    if not role:
        logger.warning(f"Role field is required")
        raise HTTPException(status_code=400, detail="role field required")
    u = User_Service.update_users(db, user_id, role)
    if not u:
        logger.warning(f"admin is trying to update the user with {user_id} which is not present" )
        raise HTTPException(status_code=404, detail="User not found")
    return u

@router.delete("/users/{user_id}")
def delete_user(user_id: int, hard: bool = False, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    logger.info(f"admin:{current_user.username} is trying to delete the user with user id {user_id}")
    ok = User_Service.delete_user(db, user_id, hard_delete=hard)
    if not ok:
        logger.warning(f"admin {current_user.username} is deleting the user which is not found")
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f" admin {current_user.username} deleted the user with id {user_id} succesfully")
    return {"detail": "User deleted"}
