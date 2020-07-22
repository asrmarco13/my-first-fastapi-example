from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import User, UserCreate
from schemas.item import Item, ItemCreate
from crud import crud_users, crud_items
from api.deps import get_db


router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> List[User]:
    """
    Get list of users (limit 100)
    """
    users = crud_users.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> User:
    """
    Get user by id
    """
    user = crud_users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    """
    Create user if not exists
    """
    user_in_db = crud_users.get_user_by_email(db, user.email)
    if user_in_db:
        raise HTTPException(status_code=400, detail="User already exists")
    user = crud_users.create_user(db, user)
    return user


@router.post("/{user_id}/items", response_model=Item)
def create_user_item(
    item: ItemCreate, user_id: int, db: Session = Depends(get_db)
) -> Item:
    """
    Create user item if not exists
    """
    item_in_db = crud_items.get_item(db, item.title)
    if item_in_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    user = crud_users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_item = crud_users.create_user_item(db, item, user_id)
    return user_item
