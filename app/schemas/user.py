from typing import List, Optional
from pydantic import BaseModel
from schemas.item import Item


class UserBase(BaseModel):
    """
    Default User properties
    """

    email: str
    name: Optional[str] = None
    surname: Optional[str] = None
    is_active: Optional[bool] = None


class UserCreate(UserBase):
    """
    Properties for create user via Api
    """

    password: str


class User(UserBase):
    """
    User class
    """

    id: int
    items: List[Item] = []

    class Config:
        """
        Additional configuration for User class
        """

        orm_mode = True


class UserUpdate(UserBase):
    """
    Properties updates via Api
    """

    password: Optional[str] = None
