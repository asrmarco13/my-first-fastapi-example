from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserUpdate, User, UserToken
from schemas.item import ItemInDBBase, ItemCreate
from crud import crud_users
from api import deps

router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> List[User]:
    """
    Get list of users (limit 100)
    """
    users = crud_users.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(deps.get_db)) -> User:
    """
    Get user by id
    """
    user = crud_users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)) -> User:
    """
    Create user if not exists
    """
    user_in_db = crud_users.get_user_by_email(db, user.email)
    if user_in_db:
        raise HTTPException(status_code=400, detail="User already exists")
    user = crud_users.create_user(db, user)
    return user


@router.post("/{user_id}/items", response_model=ItemInDBBase)
def create_user_item(
    item: ItemCreate,
    user_id: int,
    current_user: UserToken = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> ItemInDBBase:
    """
    Create item if user is authenticated and is the same of the user_id
    """
    user = crud_users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id != user_id:
        raise HTTPException(
            status_code=400, detail="User authenticated and user_id not the same!"
        )
    user_item = crud_users.create_user_item(db, item, user_id)
    return user_item


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int, user: UserUpdate, db: Session = Depends(deps.get_db)
) -> User:
    """
    Update user if exits
    otherwise create new user
    """
    user_in_db = crud_users.get_user(db, user_id)
    if user_in_db:
        user.email = user.email or user_in_db.email
        user.name = user.name or user_in_db.name
        user.surname = user.surname or user_in_db.surname
        if user.is_active is not None:
            user.is_active = user.is_active
        else:
            user.is_active = user_in_db.is_active
        user.password = user.password or user_in_db.password
        return crud_users.update_user(db, user, user_id)
    return crud_users.create_user(db, user)


@router.delete("/{user_id}", response_model=User)
def remove_user(user_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    Delete user
    """
    user = crud_users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    crud_users.remove_user(db, user_id)
    return JSONResponse("User deleted")


@router.get("/me/", response_model=UserToken)
def read_users_me(
    current_user: UserToken = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> UserToken:
    """
    Return a current cative user
    """
    return current_user
