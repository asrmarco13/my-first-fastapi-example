from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    Default properties
    """

    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """
    Properties for create item
    """


class Item(ItemBase):
    """
    Item Class
    """

    id: int
    owner_id: Optional[int]

    class Config:
        """
        Additional configuration for User class
        """

        orm_mode = True


class ItemUpdate(ItemBase):
    """
    Update item properties
    """

    owner_id: Optional[int]
