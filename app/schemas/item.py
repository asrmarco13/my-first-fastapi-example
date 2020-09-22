from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    Shared properties
    """

    title: Optional[str] = None
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """
    Create properties via Api
    """

    title: str


class ItemUpdate(ItemBase):
    """
    Update properties via Api
    """

    owner_id: Optional[int] = None


class ItemInDBBase(ItemBase):
    """
    Default properties shared in DB
    """

    id: int
    title: str
    owner_id: int

    class Config:
        """
        Configuration
        """

        orm_mode = True


class ItemInDB(ItemInDBBase):
    """
    Properties to return stored in DB
    """


class Item(ItemInDBBase):
    """
    Properties to return to client
    """
