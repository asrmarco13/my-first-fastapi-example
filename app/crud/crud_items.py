from typing import List
from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemUpdate


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Get list of items
    """
    return db.query(Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Item:
    """
    Get item by id
    """
    return db.query(Item).filter(Item.id == item_id).first()


def delete_item(db: Session, item_id) -> Item:
    """
    Delete item by id
    """
    db_item = db.query(Item).get(item_id)
    db.delete(db_item)
    db.commit()


def update_item(db: Session, item_id: int, item: ItemUpdate) -> Item:
    """
    Update item
    """
    db_item = db.query(Item).get(item_id)
    for field, value in item.__dict__.items():
        setattr(db_item, field, value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
