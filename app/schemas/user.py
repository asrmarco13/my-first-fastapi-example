from typing import List, Optional
from pydantic import BaseModel, EmailStr
from schemas.item import Item


class UserBase(BaseModel):
    """
    Default User properties
    """

    email: Optional[EmailStr] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    is_active: Optional[bool] = None


class UserCreate(UserBase):
    """
    Properties for create user via Api
    """

    email: EmailStr
    password: str


class UserInDBBase(UserBase):
    """
    User class
    """

    id: Optional[int] = None
    items: List[Item] = []

    class Config:
        """
        Additional configuration for User class
        """

        orm_mode = True


class UserUpdate(UserBase):
    """
    Properties updates
    """

    password: Optional[str] = None


class User(UserInDBBase):
    """
    Additional properties to return to client
    """


class UserInDB(UserInDBBase):
    """
    Additional properties stored in DB
    """

    password: str


class UserToken(User):
    """
    Additional parameters for OAuth2
    """

    password: str
