from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt
from pydantic import ValidationError
from core.database import SessionLocal
from core.settings import settings
from core.security import ALGORITHM
from schemas.user import UserToken
from schemas.token import TokenData
from crud import crud_users


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> UserToken:
    """
    Return a current user
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        data = TokenData(email=payload.get("sub"))
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    user = crud_users.get_user_by_email(db, data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserToken(
        id=user.id,
        email=user.email,
        name=user.name,
        surname=user.surname,
        is_active=user.is_active,
        password=user.password,
        items=user.items,
    )


def get_current_active_user(
    current_user: UserToken = Depends(get_current_user),
) -> UserToken:
    """
    Get current active user
    """
    if not crud_users.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
