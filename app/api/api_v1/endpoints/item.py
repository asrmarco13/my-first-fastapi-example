from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from crud import crud_items
from schemas.item import Item, ItemUpdate
from api.deps import get_db


router = APIRouter()


@router.get("/", response_model=List[Item])
def read_items(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> List[Item]:
    """
    Get list of items
    """
    items = crud_items.get_items(db=db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    """
    Return an item if exists
    """
    item = crud_items.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=Item)
def update_item(item: ItemUpdate, item_id: int, db: Session = Depends(get_db)) -> Item:
    """
    Update item if exists
    """
    item_in_db = crud_items.get_item(db, item_id)
    if not item_in_db:
        raise HTTPException(status_code=404, detail="Item not found")

    item.title = item.title or item_in_db.title
    item.description = item.description or item_in_db.description
    item.owner_id = item.owner_id or item_in_db.owner_id
    return crud_items.update_item(db, item_id, item)


@router.delete("/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_db)) -> Any:
    """
    Delete an item if exists
    """
    item = crud_items.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud_items.delete_item(db, item_id)
    return JSONResponse("Item deleted")
