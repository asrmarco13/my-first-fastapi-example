from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import crud_items
from schemas.item import Item
from api.deps import get_db


router = APIRouter()


@router.get("/", response_model=List[Item])
def read_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Get list of items
    """
    items = crud_items.get_items(db=db, skip=skip, limit=limit)
    return items
