from typing import List
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from schemas.item import ItemCreate
from models.item import Item
from core import security


def get_user(db: Session, user_id: int) -> User:
    """
    Get user by id
    """
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """
    Get list of users
    """
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str) -> User:
    """
    Get user by email
    """
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """
    Create user
    """
    db_user = User(
        email=user.email,
        name=user.name,
        surname=user.surname,
        password=security.get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: ItemCreate, user_id: int) -> Item:
    """
    Create user item
    """
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def remove_user(db: Session, user_id: int):
    """
    Delete user by id
    """
    db_user = db.query(User).get(user_id)
    db.delete(db_user)
    db.commit()


def update_user(db: Session, user: UserUpdate, user_id: int) -> User:
    """
    Update user information
    """
    db_user = get_user(db, user_id)
    for field, value in user.__dict__.items():
        if field == "password":
            value = security.get_password_hash(value)
        setattr(db_user, field, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, username: str, password: str) -> User:
    """
    Check user credentials
    """
    db_user = get_user_by_email(db, username)
    if not db_user:
        return None
    if not security.verify_password(password, db_user.password):
        return None
    return db_user


def is_active(user: User) -> bool:
    """
    Get user is active
    """
    return user.is_active
