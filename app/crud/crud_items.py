from typing import List
from sqlalchemy.orm import Session
from models.item import Item


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return db.query(Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_title: str) -> Item:
    return db.query(Item).filter(Item.title == item_title).first()
